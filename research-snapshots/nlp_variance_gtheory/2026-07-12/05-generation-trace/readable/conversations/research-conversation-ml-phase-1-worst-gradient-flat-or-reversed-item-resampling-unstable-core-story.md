# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Gradient flat or reversed; item resampling unstable; core story reduces to 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/434afb6d-4140-450b-b4ba-5f06ef1dacab.jsonl`
- **Structured JSON:** [`0ca29de6cb553954301a.json`](../../sessions/0c/0ca29de6cb553954301a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T08:06:28.451Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T08:06:28.451Z",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Gradient flat or reversed; item resampling unstable; core story reduces to single-benchmark (MMLU) model×item finding — must reframe angle\n核心假设：['exp-002: item_id varies < 8pp across benchmarks — variance structure is roughly benchmark-invariant, killing the gradient narrative', 'exp-002: model×item on GSM8K/ARC similar to MMLU (30-36%) — no task-type modulation', 'exp-001b: item resampling CV(item_id) > 10% — item_id estimate is sample-sensitive, 42% is not robust', 'exp-003: hardware×methodology = 3-6% — separability claim broken under multi-GPU; or exp-003 blocked entirely (no second GPU access)', \"D-study cross-benchmark Δ > 0.03 — D-study projections don't generalize well\", 'Leave-one-model-out matched-spec rerun reveals G_item spread > 0.05 — 4-model estimate is fragile', 'IRT vs G-theory ratio collapses to < 2× on some benchmarks — comparison is not universal']\n关键指标范围：{'cross_bench_item_id_range_pp': [0, 8], 'gsm8k_item_id_pct': [35, 48], 'gsm8k_model_x_item_pct': [28, 36], 'item_resample_cv_item_id': [0.1, 0.2], 'hardware_x_method_interaction_pct': [3.0, 6.0], 'g_item_cross_bench_min': [0.65, 0.72], 'd_study_cross_bench_delta': [0.03, 0.06], 'irt_gtheory_ratio_range': [1.5, 4.0], 'separability_binary_cross_bench_max_pct': [2.0, 5.0]}\n叙事方向：Gradient narrative死掉，必须reframe。新angle：聚焦MMLU单benchmark的深度分析 作为\"case study in multi-facet evaluation measurement\"。Primary contribution 变为三条：(1) model×item interaction的量化及其对single-model G-study的影响 （42%→61%的inflation效应，D-study Δ=0.004验证——这些数字已锁定不受exp-002影响）； (2) IRT vs G-theory的direct comparison（即使ratio不universal，MMLU上3.6-4.4× 的差异本身就是publishable finding，且能解释清楚why）；(3) 实证发现variance structure对benchmark不敏感——这本身可以reframe为positive result：\"practitioners can cautiously extrapolate MMLU-derived budgets to other knowledge benchmarks\"。 Separability退出claims，降为observation。Item resampling instability如果出现， 正面spin为\"item sampling itself is a major variance source, reinforcing the need for G-theory over fixed-benchmark evaluation\"。Toolkit release补充实质性。 Title改为聚焦model×item：\"The Hidden Second Factor: Model×Item Interaction Accounts for 34% of LLM Evaluation Variance\"。AAAI仍可冲（5-6/10），但需要 execution完美——writing必须极其clean，figures必须compelling，related work必须 滴水不漏。若AAAI被拒，ACL ARR October cycle有充分时间补实验。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: nlp_variance_gtheory\nfocus: Re-dream #4 after: (1) Actual 4-model data now available — item_id=42.1%, model×item=33.6%, G_item=0.820, D-study prediction validated Δ=0.004; (2) Major framing revision per D006: recentered on model×item + IRT comparison as primary contributions, infrastructure→\"precision separability\" secondary, positioned as empirical extension of Mesting not new framework, removed unsupported \"first\" claims; (3) Two new robustness analyses: BF16-vs-FP16 shows precision→0.0006% without FP32, leave-one-model-out G_item spread=0.023; (4) 6 new bibliography entries addressing all-tier missing related work (Sclar'24, Kunievsky'25, Bui'25, binary G-theory literature); (5) Fine-tuning downgraded to Discussion observation; (6) Practitioner toolkit now concretely defined. Key question: do these changes push best≥7/10, median≥borderline accept, worst≥5/10?\n\n## paper_framing.md\n\n# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Model-Conditional Item Dominance**: Item selection is the single largest variance source in single-model LLM evaluation (61.1% on MMLU), but model×item interaction (26.2%) emerges as the second-largest source when model is treated as a crossed facet. Item difficulty rankings are model-specific: two models with similar aggregate accuracy (Llama 66.4% vs Gemma 73.2%) disagree dramatically at the item level — item_id drops from 61% (single-model) to 38% (cross-model) as model×item absorbs the model-conditional portion. This means single-model variance decompositions overestimate item dominance by conflating universal and model-specific item difficulty. Cross-benchmark gradient (pending exp-002) is hypothesized to further modulate this structure.\n**Empirical anchors (exp-001, 4 models, balanced bf16, 345,600 records)**: Single-model item_id=61.1%, cross-model item_id=42.1% [36.0-48.8%] (↓19pp), model×item=33.6% [28.4-37.9%] (second-largest source, increased from 3-model 31.7%). G_item=0.820 [0.782-0.861]. D-study prediction validated out-of-sample: 3-model predicted G=0.816 for n=4, actual=0.820 (Δ=0.004). Forward projection: 5 models → G=0.848, 8→0.893, 10→0.910 (G≥0.90 requires ~10 models). Residual dropped 24%→19.5% as 4th model split residual into model×item. Per-model interaction: Mistral 29.25% (lowest accuracy 63.8%) > Qwen 27.11% > Gemma 23.95% > Llama 19.69%.\n**REML robustness**: REML-EM (500 iter, practical convergence Δ<0.003pp) confirms Henderson I: all components differ <0.5pp. Henderson I unbiased for balanced designs. Dataset B differences (item_id 38→52%, model×item 26→12%) due to design differences (factor selection), not estimator bias — measurement design choices themselves affect observed variance structure.\n**Pending**: BF16-vs-FP16-only sensitivity (exclude FP32 confound); leave-one-model-out stability (4-model marginal concern).\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent and temperature-conditional. Binary correct: G=0.611 (200 items), G≥0.80 requires ~510 items (all facets random) or ~414 items (practical: precision+temperature fixed). Text-exact-match: G=0.007 (temperature dominates at 79.7%), unreliable at any temperature >0. Temperature-stratified analysis reveals binary G degrades monotonically (T=0.0: 0.760 → T=0.7: 0.549). G-theory requires 3.6-4.4× more items than IRT (510 vs 116) because it accounts for prompt×item (4.6%), seed×item (4.7%), and residual (21.6%) dimensions that IRT ignores. Current practices (1 prompt, 1 seed, ≤200 items) yield G=0.611 — below the 0.80 threshold for dependable measurement.\n\n## Contributions (4 条，明确区分)\n\n1. **Model×item interaction as the hidden dominant source**: In a balanced 4-model design (345,600 records), model×item interaction (33.6%, CI [28.4-37.9%]) is the second-largest variance source, while item_id drops from 61% (single-model) to 42%. Item difficulty rankings are model-specific — single-model G-studies overestimate item dominance by conflating universal and model-specific difficulty. G_item=0.820 [0.782-0.861] with 4 models; D-study prediction validated out-of-sample (3-model predicted 0.816, actual 0.820, Δ=0.004). Reaching G≥0.90 requires ~10 models. [Note: position as quantification of a phenomenon expected from measurement theory, not as a surprising discovery. The novelty is the magnitude, the out-of-sample D-study validation, and the cross-model generalizability implications.]\n\n2. **Precision separability with metric qualification**: Precision×methodology interactions are negligible under binary scoring (<0.1%), providing empirical support for isolated-factor studies. Under text-exact-match scoring, precision×temperature reaches 4.15%, consistent with floating-point non-associativity. Separability is confirmed as metric-conditional. [Note: scope to \"numerical precision on single GPU architecture\" — not \"infrastructure\" broadly. This is a confirmatory secondary finding, not a primary contribution. Pending BF16-vs-FP16 sensitivity to isolate FP32/vLLM confound.]\n\n3. **IRT vs G-theory: the cost of multi-facet reliability**: The first direct comparison showing G-theory requires 3.6-4.4× more items than IRT (510 vs 116 for MMLU) because it accounts for prompt, seed, and ordering dimensions that IRT ignores. At IRT's recommended 116 items, G-theory G is only 0.529. This quantifies the \"hidden cost\" of evaluation dimensions invisible to IRT.\n\n4. **Practitioner toolkit**: Open-source G-theory variance decomposition pipeline + D-study budget calculator for LLM evaluation. Includes: (a) benchmark-specific reproducibility budget tables (items × prompts × seeds for target G), (b) temperature-stratified reliability guide, (c) model-as-facet analysis template. Addresses \"purely diagnostic\" criticism — provides actionable tools, not just warnings.\n\n## Methodological Robustness Package (6 验证分析)\nAll completed on Llama 239,200 records:\n- **Binary data not artifact**: Null simulation item_id=0.08% vs observed 61.1% (737.5×); obs/Bernoulli ratio=1.0008\n- **Fixed vs random insensitive**: Binary G ranges 0.611-0.664 across all facet classification choices\n- **Bootstrap = jackknife**: CI width ratio 0.96-1.04, independence violation negligible\n- **Temperature stratification**: Binary G degrades T=0.0 (0.760) → T=0.7 (0.549); text metric unreliable at all T>0\n- **D-study formula verified**: Monotonicity assertion added; min_items_G80=414 (practical) / 510 (all random)\n- **IRT comparison**: G-theory 3.6-4.4× more conservative than IRT; difference attributable to prompt/seed/ordering dimensions\n- **REML vs Henderson I**: REML-EM (500 iter) confirms all components within <0.5pp of Henderson I; Henderson I unbiased for balanced designs\n- **BF16-vs-FP16 sensitivity**: Excluding FP32, precision effect drops from 0.4% to 0.0006% (precision×item: 1.3%→0.04%). FP32 anomaly is entirely a vLLM enforce_eager artifact, not a fundamental precision effect. BF16≈FP16 (Δ=0.23pp accuracy)\n- **Leave-one-model-out stability**: All 4 three-model subsets preserve item_id dominance and G_item>0.80 (pending matched-specification rerun for absolute comparability)\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of 345,600 evaluation records across 4 models on MMLU (200 items × 6 prompts × 6 seeds × 3 temperatures × 4 orderings), item selection accounts for 42% of variance when model is treated as a crossed facet — but model×item interaction (34%) emerges as the second-largest source, revealing that item difficulty rankings are substantially model-specific (G_item=0.82, requiring ~10 models for G≥0.90). A D-study from 3 models predicted the 4-model G coefficient within 0.004 — out-of-sample validation of the D-study methodology. G-theory requires 3.6-4.4× more items than IRT for reliable measurement because it accounts for prompt, seed, and ordering dimensions that IRT ignores. Numerical precision×methodology interactions are negligible under binary scoring (<0.1%). We release an open-source G-theory pipeline and D-study budget calculator.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (5 figures):\n  1. **Stacked-bar: single-model vs cross-model variance decomposition** — item_id shrinks from 61% to 42%, model×item appears at 34%, residual drops 24%→20%. The \"reveal\" figure.\n  2. **G-theory crossed design diagram** — facets, levels, crossing structure\n  3. **D-study projection curves** — G vs item count for binary (practical vs all-random) and text metric. Shows G≥0.80 threshold at ~414/510 items.\n  4. **IRT vs G-theory item requirement comparison** — bar chart showing 116 (IRT) vs 510 (G-theory) items, with breakdown of where the extra items go (prompt×item, seed×item, residual)\n  5. **Temperature-stratified G coefficient heatmap** — binary vs text metric × 3 temperatures, showing metric×temperature interaction\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).\n\n## Methodological Defenses (Dream #2 审稿问题逐条应对)\n\n### MD1. Binary Data in G-theory\n**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).\n**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is \"mechanical\" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.\n\n### MD2. Fixed vs Random Facet Sensitivity\n**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.\n**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.\n\n### MD3. Separability Claim Scope\n**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).\n**Defense**: Qualify all separability claims as \"under binary scoring on knowledge-retrieval benchmarks.\" Present benchmark-conditional separability as a finding (not a limitation): \"separability itself varies across task types.\"\n\n### MD4. D-study Optimization Documentation\n**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).\n**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).\n\n### MD5. G-coefficient Interpretation\n**Issue**: G=0.22 for 200 items ≠ \"MMLU is unreliable\" (standard MMLU uses ~14K items).\n**Defense**: (a) Clearly distinguish \"G for our 200-item subsample design\" from \"reliability of full MMLU\"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as \"cost of subsampling\" rather than \"MMLU is broken.\"\n\n### MD6. Bootstrap Independence\n**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.\n**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.\n\n### MD7. IRT vs G-theory Comparison\n**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.\n**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the \"cost of multi-facet reliability\" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.\n\n### MD8. Cross-benchmark Design Asymmetry\n**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.\n**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.\n\n### MD9. Title-Content Alignment\n**Issue**: Title promises \"Evaluation Metrics\" but logprob analysis is minimal.\n**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to \"...Across Benchmarks and Models.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical, Ch.12 on binary data)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n- **Sclar et al. (2024, ICLR)** — Up to 76% accuracy swing from prompt formatting; directly relevant to prompt×item variance [Dream #3: all 3 tiers flagged as missing]\n- **Kunievsky & Evans (2025)** — Alternative decomposition: intent/articulation/model uncertainty; competing framework to G-theory [Dream #3: all 3 tiers flagged]\n- **Bui et al. (2025)** — Extreme seed sensitivity in fine-tuning (RTES variance=18.22 for RoBERTa on COPA) [Dream #3: relevant to exp-006]\n- **Jiang & Skorupski (2017)** — Logistic-link generalized G-theory for binary data [Dream #3 worst: methodological defense for REML on binary]\n- **Mushquash & O'Connor (2006)** — Binary-data G-theory [Dream #3: classical psychometrics gap]\n- **Shavelson et al. (1989)** — Binary response G-theory treatment [Dream #3: classical psychometrics]\n\n## Dream #3 Framing Directives (2026-05-21, D006)\nPost-analysis framing adjustments based on three-tier consistent feedback:\n1. **Center gradient + model×item as primary contributions** — infrastructure crossing is confirmatory secondary\n2. **Position explicitly as empirical extension of Mesting (2026)** with novel findings (model×item quantification, D-study out-of-sample validation, IRT comparison), not a new framework. Remove \"first\" claims where not defensible.\n3. **Scope Claim 2 to \"precision separability\"** — not \"infrastructure\" broadly. Single GPU architecture.\n4. **Item dominance is psychometrically expected** — contribution is quantification of magnitude, metric-conditionality, and D-study implications\n5. **Fine-tuning (exp-006) downgraded** to Discussion-section preliminary observation, not a numbered contribution\n6. **Add explicit judge-facet exclusion discussion** vs Mesting: we fix judge to isolate other factors; Mesting's 43.8% judge variance would dominate\n7. **Practitioner toolkit must be concrete**: specify released scripts, D-study calculator, budget lookup tables\n8. **Figures are non-negotiable**: 5 planned figures address all-tier \"zero figures\" criticism\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Full-scale precision study: 4 models (Qwen3-8B, Llama-3.1-8B-Instruct,\n    Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3) × 3 precisions (FP32, BF16, FP16) × 6\n    prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified).\n    All precisions use consistent vLLM engine (V0 enforce_eager) to eliminate the\n    float32 engine confound found in MVP. Validates item dominance finding at scale\n    and with multiple models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 100\n  hardware: westd-32570 (RTX PRO 6000 96GB)\n  deps: []\n  status: planned\n- id: exp-001b\n  claim: 1\n  description: 'Item resampling stability test: 3 independent stratified samples of\n    200 MMLU items (seeds 0, 7, 99) × 1 model (Llama-3.1-8B-Instruct) × 3 precisions\n    × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether\n    the 58% item dominance finding is stable across different item draws from MMLU,\n    not an artifact of the specific 200-item sample. Critical for defending the headline\n    claim.\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Multi-benchmark replication: same 4 models × BF16/FP16 × 6 prompts\n    × 6 seeds × 2 temperatures × 4 orderings on GSM8K (200 items), ARC-Challenge (200\n    items), HellaSwag (200 items). Tests whether item dominance and separability hold\n    across task types (math reasoning, science reasoning, commonsense).\n\n    '\n  priority: P0\n  gpu_budget_hours: 200\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-003\n  claim: 2\n  description: 'Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16,\n    FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. Tests\n    hardware × methodology interaction — the core separability question that MVP couldn''t\n    address with only 1 GPU type.\n\n    '\n  priority: P0\n  gpu_budget_hours: 120\n  hardware: westd-32570 + TBD (second GPU type from Manager)\n  deps: []\n  status: planned\n- id: exp-004\n  claim: 3\n  description: 'Comprehensive analysis of combined exp-001/001b/002/003 data. Includes:\n    (a) Model-as-facet G-theory reanalysis — treat model as crossed random facet to\n    properly attribute model×item interaction and reduce inflated item_id/residual\n    (Dream critical); (b) Bootstrap CIs (1000 resamples) on ALL variance components\n    in ALL tables, especially direct infra×method interaction term (Dream critical);\n    (c) D-study projections with CIs for optimal allocation across facets for G≥0.90/0.95/0.99,\n    with benchmark-specific budgets and comparison to IRT-based subsampling (tinyBenchmarks);\n    (d) REML vs Henderson Method I comparison as sensitivity analysis; (e) Logprob-based\n    scoring as third response variable; (f) Ranking stability analysis — does precision×temperature\n    interaction alter model rankings? (g) Higher-order interaction estimation to decompose\n    the residual component; (h) G-theory vs IRT direct comparison — same MMLU data,\n    D-study vs tinyBenchmarks IRT subsampling, compare recommended item counts and\n    discuss why G-theory is more conservative (accounts for prompt/seed dimensions\n    IRT ignores). First direct comparison in the literature; (i) Power analysis —\n    verify statistical power to detect ≥X% interaction effects given 5184×200 design\n    scale, preempt \"underpowered\" reviewer concern; (j) Practitioner evaluation protocol\n    guide (Discussion/Appendix); (k) Fixed vs random sensitivity — rerun G-study with\n    temperature/ordering as fixed facets, compare variance decomposition (MD2 defense);\n    (l) Binary data limitation analysis — correlate Bernoulli p(1-p) with observed\n    item variance, parallel binary vs text_exact_match analysis (MD1 defense); (m)\n    Bootstrap vs jackknife CI comparison — delete-1 jackknife as independence-safe\n    alternative, compare CI widths (MD6 defense); (n) Cross-benchmark design asymmetry\n    sensitivity — re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7),\n    compare with full 3×3 (MD8 defense); (o) G-coefficient at full benchmark size\n    — D-study projection to 14K MMLU items (MD5 defense); (p) Logprob-based scoring\n    across all benchmarks — expand from MMLU-only to all 5 benchmarks, support \"Evaluation\n    Metrics\" in title (MD9 defense); (q) GPU cost analysis — estimate compute cost\n    for recommended D-study budgets.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  hardware: none\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  status: planned\n- id: exp-005\n  claim: 2\n  description: '14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter\n    GPUs at BF16/FP16. Tests whether variance attribution patterns change with model\n    scale and architecture (dense vs reasoning-distilled).\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  hardware: TBD (needs ≥48GB VRAM per GPU)\n  deps:\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA. Fully crossed:\n    6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task\n    × 4 tasks = 1,728 total fine-tuning runs. Validates whether variance hierarchy\n    differs between inference and fine-tuning.\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  hardware: westd-32570 (RoBERTa-large fits easily on 96GB)\n  deps: []\n  status: planned\n- id: exp-007\n  claim: 2\n  description: 'Test LayerCast (FP16 storage + FP32 compute) as additional precision\n    condition on MMLU. Quantifies variance reduction from this mitigation strategy.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 1\n  description: 'MATH benchmark (200 items) — tests whether item dominance pattern\n    differs for reasoning-heavy tasks where chain-of-thought introduces additional\n    variance.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  hardware: westd-32570\n  deps:\n  - exp-002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase_a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 5400\n    conditions: 108\n    overall_accuracy: 0.6557\n    accuracy_bfloat16: 0.6844\n    accuracy_float16: 0.6833\n    accuracy_float32: 0.5994\n    g_coefficient_correct: 0.357\n    top_variance_correct:\n      item_id: 0.5844\n      residual: 0.1759\n      precision:item_id: 0.0724\n      temperature:item_id: 0.0685\n      prompt_template:item_id: 0.0573\n    top_variance_text_match:\n      residual: 0.407\n      prompt_template:item_id: 0.375\n      temperature: 0.169\n      temperature:item_id: 0.025\n      precision:temperature: 0.013\n    pass_criteria_a_pipeline: true\n    pass_criteria_b_components: true\n    pass_criteria_c_interaction: true\n    pass_criteria_c_detail: precision:temperature 1.3% CI not containing zero (text_exact_match)\n- exp_id: bf16_eager_disentangle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bf16_v1_accuracy: 0.6844\n    bf16_eager_accuracy: 0.6822\n    fp32_v0_accuracy: 0.5994\n    engine_effect_pct: 2.6\n    precision_effect_pct: 97.4\n    engine_gap_pp: 0.22\n    precision_gap_pp: 8.28\n    total_gap_pp: 8.5\n- exp_id: exp001_pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 20000\n    expected_records: 20000\n    overall_accuracy: 0.616\n    gpu0_acc: 0.605\n    gpu1_acc: 0.622\n    gpu2_acc: 0.627\n    gpu3_acc: 0.61\n    avg_latency_ms: 180.9\n    output_size_mb: 13\n    precision_coverage: float32 only (100 conditions)\n    temperature_coverage: T=0.0 only (100 conditions)\n    fields_complete: true\n- exp_id: exp001_llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 239200\n    expected_records: 239200\n    conditions: 1196\n    items_per_condition: 200\n    overall_accuracy: 0.6814\n    accuracy_bfloat16: 0.7108\n    accuracy_float16: 0.7114\n    accuracy_float32: 0.604\n    accuracy_T0.0: 0.6987\n    accuracy_T0.3: 0.6795\n    accuracy_T0.7: 0.6699\n    null_predictions: 42\n    null_pct: 0\n- exp_id: exp001_gemma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 172800\n    bf16_records: 86400\n    fp32_records: 86400\n    fp16_records: 0\n    precisions_available:\n    - bfloat16\n    - float32\n    fp16_note: Gemma2 does not support float16 (vLLM numerical instability)\n    conditions_bf16: 432\n    conditions_fp32: 432\n    total_conditions: 864\n    items_per_condition: 200\n- exp_id: exp001_mistral\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 259200\n    expected_records: 259200\n    conditions: 1296\n    items_per_condition: 200\n    overall_accuracy: 0.6124\n    accuracy_bfloat16: null\n    accuracy_float16: null\n    accuracy_float32: null\n    precisions_available:\n    - bfloat16\n    - float16\n    - float32\n    per_precision_records: 86400\n    per_temperature_records: 86400\n- exp_id: exp001_qwen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 259200\n    overall_accuracy: 0.7252\n    accuracy_bf16: 0.726\n    accuracy_fp16: 0.7257\n    accuracy_fp32: 0.7235\n    unique_conditions: 1227\n    temperatures:\n    - 0\n    - 0.3\n    - 0.7\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T08:06:28.454Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T08:06:28.454Z",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab"
}
```

---

## Round 1

29 recorded events

### User

_source line 3 · 2026-05-21T08:06:28.472Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Gradient flat or reversed; item resampling unstable; core story reduces to single-benchmark (MMLU) model×item finding — must reframe angle
核心假设：['exp-002: item_id varies < 8pp across benchmarks — variance structure is roughly benchmark-invariant, killing the gradient narrative', 'exp-002: model×item on GSM8K/ARC similar to MMLU (30-36%) — no task-type modulation', 'exp-001b: item resampling CV(item_id) > 10% — item_id estimate is sample-sensitive, 42% is not robust', 'exp-003: hardware×methodology = 3-6% — separability claim broken under multi-GPU; or exp-003 blocked entirely (no second GPU access)', "D-study cross-benchmark Δ > 0.03 — D-study projections don't generalize well", 'Leave-one-model-out matched-spec rerun reveals G_item spread > 0.05 — 4-model estimate is fragile', 'IRT vs G-theory ratio collapses to < 2× on some benchmarks — comparison is not universal']
关键指标范围：{'cross_bench_item_id_range_pp': [0, 8], 'gsm8k_item_id_pct': [35, 48], 'gsm8k_model_x_item_pct': [28, 36], 'item_resample_cv_item_id': [0.1, 0.2], 'hardware_x_method_interaction_pct': [3.0, 6.0], 'g_item_cross_bench_min': [0.65, 0.72], 'd_study_cross_bench_delta': [0.03, 0.06], 'irt_gtheory_ratio_range': [1.5, 4.0], 'separability_binary_cross_bench_max_pct': [2.0, 5.0]}
叙事方向：Gradient narrative死掉，必须reframe。新angle：聚焦MMLU单benchmark的深度分析 作为"case study in multi-facet evaluation measurement"。Primary contribution 变为三条：(1) model×item interaction的量化及其对single-model G-study的影响 （42%→61%的inflation效应，D-study Δ=0.004验证——这些数字已锁定不受exp-002影响）； (2) IRT vs G-theory的direct comparison（即使ratio不universal，MMLU上3.6-4.4× 的差异本身就是publishable finding，且能解释清楚why）；(3) 实证发现variance structure对benchmark不敏感——这本身可以reframe为positive result："practitioners can cautiously extrapolate MMLU-derived budgets to other knowledge benchmarks"。 Separability退出claims，降为observation。Item resampling instability如果出现， 正面spin为"item sampling itself is a major variance source, reinforcing the need for G-theory over fixed-benchmark evaluation"。Toolkit release补充实质性。 Title改为聚焦model×item："The Hidden Second Factor: Model×Item Interaction Accounts for 34% of LLM Evaluation Variance"。AAAI仍可冲（5-6/10），但需要 execution完美——writing必须极其clean，figures必须compelling，related work必须 滴水不漏。若AAAI被拒，ACL ARR October cycle有充分时间补实验。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: nlp_variance_gtheory
focus: Re-dream #4 after: (1) Actual 4-model data now available — item_id=42.1%, model×item=33.6%, G_item=0.820, D-study prediction validated Δ=0.004; (2) Major framing revision per D006: recentered on model×item + IRT comparison as primary contributions, infrastructure→"precision separability" secondary, positioned as empirical extension of Mesting not new framework, removed unsupported "first" claims; (3) Two new robustness analyses: BF16-vs-FP16 shows precision→0.0006% without FP32, leave-one-model-out G_item spread=0.023; (4) 6 new bibliography entries addressing all-tier missing related work (Sclar'24, Kunievsky'25, Bui'25, binary G-theory literature); (5) Fine-tuning downgraded to Discussion observation; (6) Practitioner toolkit now concretely defined. Key question: do these changes push best≥7/10, median≥borderline accept, worst≥5/10?

## paper_framing.md

# Paper Framing — nlp_variance_gtheory

## Target Venue
- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
- Extended: TACL (rolling)

## Title
Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics

## Core Claims (3 条，可证伪)

**Claim 1 — Model-Conditional Item Dominance**: Item selection is the single largest variance source in single-model LLM evaluation (61.1% on MMLU), but model×item interaction (26.2%) emerges as the second-largest source when model is treated as a crossed facet. Item difficulty rankings are model-specific: two models with similar aggregate accuracy (Llama 66.4% vs Gemma 73.2%) disagree dramatically at the item level — item_id drops from 61% (single-model) to 38% (cross-model) as model×item absorbs the model-conditional portion. This means single-model variance decompositions overestimate item dominance by conflating universal and model-specific item difficulty. Cross-benchmark gradient (pending exp-002) is hypothesized to further modulate this structure.
**Empirical anchors (exp-001, 4 models, balanced bf16, 345,600 records)**: Single-model item_id=61.1%, cross-model item_id=42.1% [36.0-48.8%] (↓19pp), model×item=33.6% [28.4-37.9%] (second-largest source, increased from 3-model 31.7%). G_item=0.820 [0.782-0.861]. D-study prediction validated out-of-sample: 3-model predicted G=0.816 for n=4, actual=0.820 (Δ=0.004). Forward projection: 5 models → G=0.848, 8→0.893, 10→0.910 (G≥0.90 requires ~10 models). Residual dropped 24%→19.5% as 4th model split residual into model×item. Per-model interaction: Mistral 29.25% (lowest accuracy 63.8%) > Qwen 27.11% > Gemma 23.95% > Llama 19.69%.
**REML robustness**: REML-EM (500 iter, practical convergence Δ<0.003pp) confirms Henderson I: all components differ <0.5pp. Henderson I unbiased for balanced designs. Dataset B differences (item_id 38→52%, model×item 26→12%) due to design differences (factor selection), not estimator bias — measurement design choices themselves affect observed variance structure.
**Pending**: BF16-vs-FP16-only sensitivity (exclude FP32 confound); leave-one-model-out stability (4-model marginal concern).

**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), "infrastructure" is currently limited to the precision facet.

**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent and temperature-conditional. Binary correct: G=0.611 (200 items), G≥0.80 requires ~510 items (all facets random) or ~414 items (practical: precision+temperature fixed). Text-exact-match: G=0.007 (temperature dominates at 79.7%), unreliable at any temperature >0. Temperature-stratified analysis reveals binary G degrades monotonically (T=0.0: 0.760 → T=0.7: 0.549). G-theory requires 3.6-4.4× more items than IRT (510 vs 116) because it accounts for prompt×item (4.6%), seed×item (4.7%), and residual (21.6%) dimensions that IRT ignores. Current practices (1 prompt, 1 seed, ≤200 items) yield G=0.611 — below the 0.80 threshold for dependable measurement.

## Contributions (4 条，明确区分)

1. **Model×item interaction as the hidden dominant source**: In a balanced 4-model design (345,600 records), model×item interaction (33.6%, CI [28.4-37.9%]) is the second-largest variance source, while item_id drops from 61% (single-model) to 42%. Item difficulty rankings are model-specific — single-model G-studies overestimate item dominance by conflating universal and model-specific difficulty. G_item=0.820 [0.782-0.861] with 4 models; D-study prediction validated out-of-sample (3-model predicted 0.816, actual 0.820, Δ=0.004). Reaching G≥0.90 requires ~10 models. [Note: position as quantification of a phenomenon expected from measurement theory, not as a surprising discovery. The novelty is the magnitude, the out-of-sample D-study validation, and the cross-model generalizability implications.]

2. **Precision separability with metric qualification**: Precision×methodology interactions are negligible under binary scoring (<0.1%), providing empirical support for isolated-factor studies. Under text-exact-match scoring, precision×temperature reaches 4.15%, consistent with floating-point non-associativity. Separability is confirmed as metric-conditional. [Note: scope to "numerical precision on single GPU architecture" — not "infrastructure" broadly. This is a confirmatory secondary finding, not a primary contribution. Pending BF16-vs-FP16 sensitivity to isolate FP32/vLLM confound.]

3. **IRT vs G-theory: the cost of multi-facet reliability**: The first direct comparison showing G-theory requires 3.6-4.4× more items than IRT (510 vs 116 for MMLU) because it accounts for prompt, seed, and ordering dimensions that IRT ignores. At IRT's recommended 116 items, G-theory G is only 0.529. This quantifies the "hidden cost" of evaluation dimensions invisible to IRT.

4. **Practitioner toolkit**: Open-source G-theory variance decomposition pipeline + D-study budget calculator for LLM evaluation. Includes: (a) benchmark-specific reproducibility budget tables (items × prompts × seeds for target G), (b) temperature-stratified reliability guide, (c) model-as-facet analysis template. Addresses "purely diagnostic" criticism — provides actionable tools, not just warnings.

## Methodological Robustness Package (6 验证分析)
All completed on Llama 239,200 records:
- **Binary data not artifact**: Null simulation item_id=0.08% vs observed 61.1% (737.5×); obs/Bernoulli ratio=1.0008
- **Fixed vs random insensitive**: Binary G ranges 0.611-0.664 across all facet classification choices
- **Bootstrap = jackknife**: CI width ratio 0.96-1.04, independence violation negligible
- **Temperature stratification**: Binary G degrades T=0.0 (0.760) → T=0.7 (0.549); text metric unreliable at all T>0
- **D-study formula verified**: Monotonicity assertion added; min_items_G80=414 (practical) / 510 (all random)
- **IRT comparison**: G-theory 3.6-4.4× more conservative than IRT; difference attributable to prompt/seed/ordering dimensions
- **REML vs Henderson I**: REML-EM (500 iter) confirms all components within <0.5pp of Henderson I; Henderson I unbiased for balanced designs
- **BF16-vs-FP16 sensitivity**: Excluding FP32, precision effect drops from 0.4% to 0.0006% (precision×item: 1.3%→0.04%). FP32 anomaly is entirely a vLLM enforce_eager artifact, not a fundamental precision effect. BF16≈FP16 (Δ=0.23pp accuracy)
- **Leave-one-model-out stability**: All 4 three-model subsets preserve item_id dominance and G_item>0.80 (pending matched-specification rerun for absolute comparability)

## Story Spine

**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.

**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.

**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.

**Headline result template**: "In a G-study of 345,600 evaluation records across 4 models on MMLU (200 items × 6 prompts × 6 seeds × 3 temperatures × 4 orderings), item selection accounts for 42% of variance when model is treated as a crossed facet — but model×item interaction (34%) emerges as the second-largest source, revealing that item difficulty rankings are substantially model-specific (G_item=0.82, requiring ~10 models for G≥0.90). A D-study from 3 models predicted the 4-model G coefficient within 0.004 — out-of-sample validation of the D-study methodology. G-theory requires 3.6-4.4× more items than IRT for reliable measurement because it accounts for prompt, seed, and ordering dimensions that IRT ignores. Numerical precision×methodology interactions are negligible under binary scoring (<0.1%). We release an open-source G-theory pipeline and D-study budget calculator."

## Hook (Counter-Intuitive Quantified Claim)
"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory."

## Narrative Strategy
- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)
- **Tension**: "No universal recipe" — the field seeks standardization but variance structure varies qualitatively across task types
- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)
- **Figure plan** (5 figures):
  1. **Stacked-bar: single-model vs cross-model variance decomposition** — item_id shrinks from 61% to 42%, model×item appears at 34%, residual drops 24%→20%. The "reveal" figure.
  2. **G-theory crossed design diagram** — facets, levels, crossing structure
  3. **D-study projection curves** — G vs item count for binary (practical vs all-random) and text metric. Shows G≥0.80 threshold at ~414/510 items.
  4. **IRT vs G-theory item requirement comparison** — bar chart showing 116 (IRT) vs 510 (G-theory) items, with breakdown of where the extra items go (prompt×item, seed×item, residual)
  5. **Temperature-stratified G coefficient heatmap** — binary vs text metric × 3 temperatures, showing metric×temperature interaction
- **Key framing shifts from Dream feedback**:
  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty
  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient
  - Cross-benchmark gradient is the **primary novel finding**
  - "Fully crossed" language qualified to MMLU exp-001 only; other benchmarks use reduced designs

## Venue Fit Risks
- AAAI: Strong fit for "evaluation methodology" track. Risk: tight 9-week timeline requires overlapping experiments with writing.
- Reviewer concern 1: "Only open-weight models, not API models" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.
- Reviewer concern 2: "G-theory is borrowed methodology, not novel" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.
- Reviewer concern 3: "Item dominance is obvious from measurement theory" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.

## Anticipated Reviewer Concerns & Planned Responses
1. **"Only N GPU types"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to "numerical precision" and frame hardware as future work.
2. **"float32 engine confound"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.
3. **"Only MMLU"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.
4. **"Small item sample"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.
5. **"No training-time analysis"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.
6. **"Missing scale validation"** → exp-005 (14B models)
7. **"G-theory may not be right framework"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.
8. **"Separability claim is metric-dependent"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.
9. **"FP32 degradation is already known (Yuan 2025)"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.
10. **"Incremental over Mesting (2026)"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.
11. **"Model not treated as G-theory facet"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.
12. **"No CIs on variance components"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.
13. **"Missing related work — IRT, tinyBenchmarks, Bouthillier"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.
14. **"Diagnostic tool claim unsubstantiated"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as "empirical analysis + data release."
15. **"Fine-tuning uses encoder-only RoBERTa"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.

## Design Decisions
- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.
- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.
- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.
- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.
- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.
- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as "reduced crossing" rather than "fully crossed."
- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).

## Methodological Defenses (Dream #2 审稿问题逐条应对)

### MD1. Binary Data in G-theory
**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).
**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is "mechanical" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.

### MD2. Fixed vs Random Facet Sensitivity
**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.
**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.

### MD3. Separability Claim Scope
**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).
**Defense**: Qualify all separability claims as "under binary scoring on knowledge-retrieval benchmarks." Present benchmark-conditional separability as a finding (not a limitation): "separability itself varies across task types."

### MD4. D-study Optimization Documentation
**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).
**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).

### MD5. G-coefficient Interpretation
**Issue**: G=0.22 for 200 items ≠ "MMLU is unreliable" (standard MMLU uses ~14K items).
**Defense**: (a) Clearly distinguish "G for our 200-item subsample design" from "reliability of full MMLU"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as "cost of subsampling" rather than "MMLU is broken."

### MD6. Bootstrap Independence
**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.
**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.

### MD7. IRT vs G-theory Comparison
**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.
**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the "cost of multi-facet reliability" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.

### MD8. Cross-benchmark Design Asymmetry
**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.
**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.

### MD9. Title-Content Alignment
**Issue**: Title promises "Evaluation Metrics" but logprob analysis is minimal.
**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to "...Across Benchmarks and Models."

## Required Bibliography (minimum 25 references)
Key references to include beyond current literature_map:
- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA
- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP
- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP
- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling
- Perlitz et al. (2023) — Efficient LLM benchmarking
- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition
- Shavelson & Webb (1991) — G-theory primer (canonical)
- Brennan (2001) — G-theory textbook (canonical, Ch.12 on binary data)
- Lu et al. (2022) — Option ordering effects in MC evaluation
- Pezeshkpour & Hruschka (2024) — Option ordering effects
- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)
- Sellam et al. (2022) — MultiBERTs, multi-seed training
- Dehghani et al. (2021) — Benchmark Lottery
- Biderman et al. (2024) — Evaluation reproducibility lessons
- Vania et al. (2021) — IRT item properties in NLP
- **Sclar et al. (2024, ICLR)** — Up to 76% accuracy swing from prompt formatting; directly relevant to prompt×item variance [Dream #3: all 3 tiers flagged as missing]
- **Kunievsky & Evans (2025)** — Alternative decomposition: intent/articulation/model uncertainty; competing framework to G-theory [Dream #3: all 3 tiers flagged]
- **Bui et al. (2025)** — Extreme seed sensitivity in fine-tuning (RTES variance=18.22 for RoBERTa on COPA) [Dream #3: relevant to exp-006]
- **Jiang & Skorupski (2017)** — Logistic-link generalized G-theory for binary data [Dream #3 worst: methodological defense for REML on binary]
- **Mushquash & O'Connor (2006)** — Binary-data G-theory [Dream #3: classical psychometrics gap]
- **Shavelson et al. (1989)** — Binary response G-theory treatment [Dream #3: classical psychometrics]

## Dream #3 Framing Directives (2026-05-21, D006)
Post-analysis framing adjustments based on three-tier consistent feedback:
1. **Center gradient + model×item as primary contributions** — infrastructure crossing is confirmatory secondary
2. **Position explicitly as empirical extension of Mesting (2026)** with novel findings (model×item quantification, D-study out-of-sample validation, IRT comparison), not a new framework. Remove "first" claims where not defensible.
3. **Scope Claim 2 to "precision separability"** — not "infrastructure" broadly. Single GPU architecture.
4. **Item dominance is psychometrically expected** — contribution is quantification of magnitude, metric-conditionality, and D-study implications
5. **Fine-tuning (exp-006) downgraded** to Discussion-section preliminary observation, not a numbered contribution
6. **Add explicit judge-facet exclusion discussion** vs Mesting: we fix judge to isolate other factors; Mesting's 43.8% judge variance would dominate
7. **Practitioner toolkit must be concrete**: specify released scripts, D-study calculator, budget lookup tables
8. **Figures are non-negotiable**: 5 planned figures address all-tier "zero figures" criticism


## experiment_plan (with registry status)

- id: exp-001
  claim: 1
  description: 'Full-scale precision study: 4 models (Qwen3-8B, Llama-3.1-8B-Instruct,
    Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3) × 3 precisions (FP32, BF16, FP16) × 6
    prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified).
    All precisions use consistent vLLM engine (V0 enforce_eager) to eliminate the
    float32 engine confound found in MVP. Validates item dominance finding at scale
    and with multiple models.

    '
  priority: P0
  gpu_budget_hours: 100
  hardware: westd-32570 (RTX PRO 6000 96GB)
  deps: []
  status: planned
- id: exp-001b
  claim: 1
  description: 'Item resampling stability test: 3 independent stratified samples of
    200 MMLU items (seeds 0, 7, 99) × 1 model (Llama-3.1-8B-Instruct) × 3 precisions
    × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether
    the 58% item dominance finding is stable across different item draws from MMLU,
    not an artifact of the specific 200-item sample. Critical for defending the headline
    claim.

    '
  priority: P0
  gpu_budget_hours: 15
  hardware: westd-32570
  deps:
  - exp-001
  status: planned
- id: exp-002
  claim: 1
  description: 'Multi-benchmark replication: same 4 models × BF16/FP16 × 6 prompts
    × 6 seeds × 2 temperatures × 4 orderings on GSM8K (200 items), ARC-Challenge (200
    items), HellaSwag (200 items). Tests whether item dominance and separability hold
    across task types (math reasoning, science reasoning, commonsense).

    '
  priority: P0
  gpu_budget_hours: 200
  hardware: westd-32570
  deps:
  - exp-001
  status: planned
- id: exp-003
  claim: 2
  description: 'Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16,
    FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. Tests
    hardware × methodology interaction — the core separability question that MVP couldn''t
    address with only 1 GPU type.

    '
  priority: P0
  gpu_budget_hours: 120
  hardware: westd-32570 + TBD (second GPU type from Manager)
  deps: []
  status: planned
- id: exp-004
  claim: 3
  description: 'Comprehensive analysis of combined exp-001/001b/002/003 data. Includes:
    (a) Model-as-facet G-theory reanalysis — treat model as crossed random facet to
    properly attribute model×item interaction and reduce inflated item_id/residual
    (Dream critical); (b) Bootstrap CIs (1000 resamples) on ALL variance components
    in ALL tables, especially direct infra×method interaction term (Dream critical);
    (c) D-study projections with CIs for optimal allocation across facets for G≥0.90/0.95/0.99,
    with benchmark-specific budgets and comparison to IRT-based subsampling (tinyBenchmarks);
    (d) REML vs Henderson Method I comparison as sensitivity analysis; (e) Logprob-based
    scoring as third response variable; (f) Ranking stability analysis — does precision×temperature
    interaction alter model rankings? (g) Higher-order interaction estimation to decompose
    the residual component; (h) G-theory vs IRT direct comparison — same MMLU data,
    D-study vs tinyBenchmarks IRT subsampling, compare recommended item counts and
    discuss why G-theory is more conservative (accounts for prompt/seed dimensions
    IRT ignores). First direct comparison in the literature; (i) Power analysis —
    verify statistical power to detect ≥X% interaction effects given 5184×200 design
    scale, preempt "underpowered" reviewer concern; (j) Practitioner evaluation protocol
    guide (Discussion/Appendix); (k) Fixed vs random sensitivity — rerun G-study with
    temperature/ordering as fixed facets, compare variance decomposition (MD2 defense);
    (l) Binary data limitation analysis — correlate Bernoulli p(1-p) with observed
    item variance, parallel binary vs text_exact_match analysis (MD1 defense); (m)
    Bootstrap vs jackknife CI comparison — delete-1 jackknife as independence-safe
    alternative, compare CI widths (MD6 defense); (n) Cross-benchmark design asymmetry
    sensitivity — re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7),
    compare with full 3×3 (MD8 defense); (o) G-coefficient at full benchmark size
    — D-study projection to 14K MMLU items (MD5 defense); (p) Logprob-based scoring
    across all benchmarks — expand from MMLU-only to all 5 benchmarks, support "Evaluation
    Metrics" in title (MD9 defense); (q) GPU cost analysis — estimate compute cost
    for recommended D-study budgets.

    '
  priority: P0
  gpu_budget_hours: 0
  hardware: none
  deps:
  - exp-001
  - exp-002
  - exp-003
  status: planned
- id: exp-005
  claim: 2
  description: '14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter
    GPUs at BF16/FP16. Tests whether variance attribution patterns change with model
    scale and architecture (dense vs reasoning-distilled).

    '
  priority: P1
  gpu_budget_hours: 100
  hardware: TBD (needs ≥48GB VRAM per GPU)
  deps:
  - exp-003
  status: planned
- id: exp-006
  claim: 2
  description: 'Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA. Fully crossed:
    6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task
    × 4 tasks = 1,728 total fine-tuning runs. Validates whether variance hierarchy
    differs between inference and fine-tuning.

    '
  priority: P1
  gpu_budget_hours: 200
  hardware: westd-32570 (RoBERTa-large fits easily on 96GB)
  deps: []
  status: planned
- id: exp-007
  claim: 2
  description: 'Test LayerCast (FP16 storage + FP32 compute) as additional precision
    condition on MMLU. Quantifies variance reduction from this mitigation strategy.

    '
  priority: P2
  gpu_budget_hours: 30
  hardware: westd-32570
  deps:
  - exp-001
  status: planned
- id: exp-008
  claim: 1
  description: 'MATH benchmark (200 items) — tests whether item dominance pattern
    differs for reasoning-heavy tasks where chain-of-thought introduces additional
    variance.

    '
  priority: P2
  gpu_budget_hours: 50
  hardware: westd-32570
  deps:
  - exp-002
  status: planned


## registry (completed experiments)

- exp_id: mvp_phase_a
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_records: 5400
    conditions: 108
    overall_accuracy: 0.6557
    accuracy_bfloat16: 0.6844
    accuracy_float16: 0.6833
    accuracy_float32: 0.5994
    g_coefficient_correct: 0.357
    top_variance_correct:
      item_id: 0.5844
      residual: 0.1759
      precision:item_id: 0.0724
      temperature:item_id: 0.0685
      prompt_template:item_id: 0.0573
    top_variance_text_match:
      residual: 0.407
      prompt_template:item_id: 0.375
      temperature: 0.169
      temperature:item_id: 0.025
      precision:temperature: 0.013
    pass_criteria_a_pipeline: true
    pass_criteria_b_components: true
    pass_criteria_c_interaction: true
    pass_criteria_c_detail: precision:temperature 1.3% CI not containing zero (text_exact_match)
- exp_id: bf16_eager_disentangle
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    bf16_v1_accuracy: 0.6844
    bf16_eager_accuracy: 0.6822
    fp32_v0_accuracy: 0.5994
    engine_effect_pct: 2.6
    precision_effect_pct: 97.4
    engine_gap_pp: 0.22
    precision_gap_pp: 8.28
    total_gap_pp: 8.5
- exp_id: exp001_pilot
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_records: 20000
    expected_records: 20000
    overall_accuracy: 0.616
    gpu0_acc: 0.605
    gpu1_acc: 0.622
    gpu2_acc: 0.627
    gpu3_acc: 0.61
    avg_latency_ms: 180.9
    output_size_mb: 13
    precision_coverage: float32 only (100 conditions)
    temperature_coverage: T=0.0 only (100 conditions)
    fields_complete: true
- exp_id: exp001_llama
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_records: 239200
    expected_records: 239200
    conditions: 1196
    items_per_condition: 200
    overall_accuracy: 0.6814
    accuracy_bfloat16: 0.7108
    accuracy_float16: 0.7114
    accuracy_float32: 0.604
    accuracy_T0.0: 0.6987
    accuracy_T0.3: 0.6795
    accuracy_T0.7: 0.6699
    null_predictions: 42
    null_pct: 0
- exp_id: exp001_gemma
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_records: 172800
    bf16_records: 86400
    fp32_records: 86400
    fp16_records: 0
    precisions_available:
    - bfloat16
    - float32
    fp16_note: Gemma2 does not support float16 (vLLM numerical instability)
    conditions_bf16: 432
    conditions_fp32: 432
    total_conditions: 864
    items_per_condition: 200
- exp_id: exp001_mistral
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_records: 259200
    expected_records: 259200
    conditions: 1296
    items_per_condition: 200
    overall_accuracy: 0.6124
    accuracy_bfloat16: null
    accuracy_float16: null
    accuracy_float32: null
    precisions_available:
    - bfloat16
    - float16
    - float32
    per_precision_records: 86400
    per_temperature_records: 86400
- exp_id: exp001_qwen
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_records: 259200
    overall_accuracy: 0.7252
    accuracy_bf16: 0.726
    accuracy_fp16: 0.7257
    accuracy_fp32: 0.7235
    unique_conditions: 1227
    temperatures:
    - 0
    - 0.3
    - 0.7

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: worst
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6db0ed55-735c-4b34-9746-8009bac2d7df",
  "type": "user",
  "uuid": "32cf39f3-bc6f-4ac9-a0fa-7b7d1a121652",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T08:06:28.470Z_

```json
{
  "parentUuid": "32cf39f3-bc6f-4ac9-a0fa-7b7d1a121652",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "9466aaeb-5e42-4f03-a049-71e3d02db54b",
  "timestamp": "2026-05-21T08:06:28.470Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T08:06:28.470Z_

```json
{
  "parentUuid": "9466aaeb-5e42-4f03-a049-71e3d02db54b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "52eabbe5-88f0-4ebe-8a1d-7e1348a089b4",
  "timestamp": "2026-05-21T08:06:28.470Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Gradient flat or reversed; item resampling unstable; core story reduces to single-benchmark (MMLU) model×item finding — must reframe angle 核心假设：['exp-002:…",
  "leafUuid": "52eabbe5-88f0-4ebe-8a1d-7e1348a089b4",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Model×item interaction in LLM evaluation variance",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab"
}
```

---

### Assistant

_source line 8 · 2026-05-21T08:07:12.386Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for the "worst" tier scenario for each planned experiment in the experiment plan. I need to carefully consider the worst-tier definition and produce results consistent with it.

Let me review the worst tier definition:

**Worst tier meaning**: Gradient flat or reversed; item resampling unstable; core story reduces to single-benchmark (MMLU) model×item finding — must reframe angle

**Core assumptions for worst**:
- exp-002: item_id varies < 8pp across benchmarks — variance structure is roughly benchmark-invariant, killing the gradient narrative
- exp-002: model×item on GSM8K/ARC similar to MMLU (30-36%) — no task-type modulation


- exp-001b: item resampling shows high sensitivity with CV(item_id) > 10%, making the 42% estimate unreliable across samples
- exp-003: hardware×methodology effects shrink to 3-6%, undermining the separability claim under multi-GPU conditions or blocking the experiment entirely due to resource constraints
- D-study projections fail to generalize across benchmarks with Δ > 0.03
- Leave-one-model-out validation exposes fragility in the 4-model estimate, with G_item spread exceeding 0.05
- IRT versus G-theory comparison collapses to less than 2× on certain benchmarks, weakening the methodological contrast

Now I'm looking at the metric ranges across these validation checks—item_id variability spans 0-8 percentage points on cross-benchmark tasks, GSM8K shows 35-48% item effects, and the hardware×method interaction stays in the 3-6% band. The G-theory item component ranges from 0.65 to 0.72, D-study deltas run 0.03-0.06, and the IRT-to-G-theory ratio varies between 1.5 and 4.0 depending on the benchmark.

If the gradient narrative doesn't hold up universally, I'm pivoting to frame this as a deep MMLU case study instead—treating it as a methodological exploration of multi-faceted evaluation measurement. The key contributions shift to quantifying model×item interactions and their inflation effect on single-model G-studies (jumping from 42% to 61%), validating the D-study delta at 0.004 regardless of experimental conditions. I can also make a direct IRT versus G-theory comparison work—even if the ratio isn't universal, the 3.6-4.4× difference on MMLU alone is publishable. The variance structure becomes a strength rather than a limitation, letting practitioners cautiously apply MMLU-derived budgets to other contexts. Item resampling instability gets reframed as a positive finding, and releasing the toolkit adds practical value to the work.

For exp-001, the individual model runs are already complete, but I need to clarify whether the full combined balanced analysis across all four models has actually been executed or if that's still pending. The registry shows individual experiments done but exp-001 itself marked as planned, so the cross-model analysis might still need to happen. Now I'm sketching out worst-case scenarios for each planned experiment: exp-001b would show item resampling instability with cross-validation variance exceeding 10%, exp-002 would flatten the gradient narrative by showing item_id consistency across benchmarks within 8 percentage points, exp-003 would reveal hardware×methodology interactions around 3-6% that undermine the separability claim, and exp-004 would aggregate these findings into a comprehensive analysis that compounds the fragility.

Writing YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52eabbe5-88f0-4ebe-8a1d-7e1348a089b4",
  "isSidechain": false,
  "requestId": "req_011CbFNPxXJfMbwHoCbudzgM",
  "type": "assistant",
  "uuid": "17786134-a992-492d-8573-3b4692893d73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgLLgTuiwbkF9p8DLNH57h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16603,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1749,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16603,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1749,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16603
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

_source line 9 · 2026-05-21T08:07:13.090Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QinERqGb5rMiadaCxJ9aXG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17786134-a992-492d-8573-3b4692893d73",
  "isSidechain": false,
  "requestId": "req_011CbFNPxXJfMbwHoCbudzgM",
  "type": "assistant",
  "uuid": "36e6e3e4-9a0c-4574-be97-6bf0c9ebe027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgLLgTuiwbkF9p8DLNH57h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16603,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1749,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16603,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1749,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16603
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

_source line 10 · 2026-05-21T08:07:13.102Z_

<details><summary>↩ Tool result · `toolu_01QinERqGb5rMiadaCxJ9aXG`</summary>

```text
0	
1	## 输出风格
2	
3	- 回复简洁直接，不说废话
4	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
5	- 不要复述用户的问题
6	- 不要给未被要求的建议或补充说明
7	- 推理要彻底，但输出只保留结论和必要信息
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36e6e3e4-9a0c-4574-be97-6bf0c9ebe027",
  "isSidechain": false,
  "promptId": "6db0ed55-735c-4b34-9746-8009bac2d7df",
  "type": "user",
  "uuid": "028e874b-8f96-41c8-91a9-ef7dcc770c23",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 0,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "36e6e3e4-9a0c-4574-be97-6bf0c9ebe027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T08:07:13.735Z_

<details><summary>↩ Tool result · `toolu_011kupFUvFyvg8UYG1uCRfBp`</summary>

```text
projects/nlp_variance_gtheory/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3aeb0f4-08ee-404d-a665-5a956b0fee37",
  "isSidechain": false,
  "promptId": "6db0ed55-735c-4b34-9746-8009bac2d7df",
  "type": "user",
  "uuid": "e6df0047-9a68-4b1b-83e5-9013f7c1ddaf",
  "toolUseResult": {
    "filenames": [
      "projects/nlp_variance_gtheory/experiment_plan.yaml"
    ],
    "durationMs": 33,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "b3aeb0f4-08ee-404d-a665-5a956b0fee37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T08:07:13.697Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011kupFUvFyvg8UYG1uCRfBp`</summary>

```json
{
  "pattern": "**/*experiment*plan*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "028e874b-8f96-41c8-91a9-ef7dcc770c23",
  "isSidechain": false,
  "requestId": "req_011CbFNPxXJfMbwHoCbudzgM",
  "type": "assistant",
  "uuid": "b3aeb0f4-08ee-404d-a665-5a956b0fee37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgLLgTuiwbkF9p8DLNH57h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16603,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1749,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16603,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1749,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16603
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

_source line 13 · 2026-05-21T08:07:17.180Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J611CSBcP14WqMqXJ3jgNL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6df0047-9a68-4b1b-83e5-9013f7c1ddaf",
  "isSidechain": false,
  "requestId": "req_011CbFNTJAq3WdP2cFNLVt4K",
  "type": "assistant",
  "uuid": "b1b2f597-9195-4149-aa2d-290c12b7e4aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197kTPpgUS1YMN6up4xZE1A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1982,
      "cache_read_input_tokens": 28444,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1982,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 28444,
          "cache_creation_input_tokens": 1982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1982
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

_source line 14 · 2026-05-21T08:07:17.184Z_

<details><summary>↩ Tool result · `toolu_01J611CSBcP14WqMqXJ3jgNL`</summary>

```text
1	experiments:
2	  # === P0: Must-run for paper submission ===
3	
4	  - id: exp-001
5	    claim: 1  # Item dominance at scale
6	    description: >
7	      Full-scale precision study: 4 models (Qwen3-8B, Llama-3.1-8B-Instruct, Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3)
8	      × 3 precisions (FP32, BF16, FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings
9	      × 200 MMLU items (stratified). All precisions use consistent vLLM engine (V0 enforce_eager)
10	      to eliminate the float32 engine confound found in MVP. Validates item dominance finding at
11	      scale and with multiple models.
12	    priority: P0
13	    gpu_budget_hours: 100
14	    hardware: westd-32570 (RTX PRO 6000 96GB)
15	    deps: []
16	    status: planned
17	
18	  - id: exp-001b
19	    claim: 1  # Item dominance stability across item samples
20	    description: >
21	      Item resampling stability test: 3 independent stratified samples of 200 MMLU items
22	      (seeds 0, 7, 99) × 1 model (Llama-3.1-8B-Instruct) × 3 precisions × 3 prompts
23	      × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether the 58% item
24	      dominance finding is stable across different item draws from MMLU, not an artifact
25	      of the specific 200-item sample. Critical for defending the headline claim.
26	    priority: P0
27	    gpu_budget_hours: 15
28	    hardware: westd-32570
29	    deps: [exp-001]  # reuses exp-001 pipeline, runs after main study
30	    status: planned
31	
32	  - id: exp-002
33	    claim: 1  # Item dominance generalizes across benchmarks
34	    description: >
35	      Multi-benchmark replication: same 4 models × BF16/FP16 × 6 prompts × 6 seeds
36	      × 2 temperatures × 4 orderings on GSM8K (200 items), ARC-Challenge (200 items),
37	      HellaSwag (200 items). Tests whether item dominance and separability hold across
38	      task types (math reasoning, science reasoning, commonsense).
39	    priority: P0
40	    gpu_budget_hours: 200
41	    hardware: westd-32570
42	    deps: [exp-001]  # need analysis pipeline validated first
43	    status: planned
44	
45	  - id: exp-003
46	    claim: 2  # Separability with hardware factor
47	    description: >
48	      Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16, FP16)
49	      × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items.
50	      Tests hardware × methodology interaction — the core separability question
51	      that MVP couldn't address with only 1 GPU type.
52	    priority: P0
53	    gpu_budget_hours: 120
54	    hardware: westd-32570 + TBD (second GPU type from Manager)
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
77	      (j) Practitioner evaluation protocol guide (Discussion/Appendix);
78	      (k) Fixed vs random sensitivity — rerun G-study with temperature/ordering as fixed facets,
79	      compare variance decomposition (MD2 defense);
80	      (l) Binary data limitation analysis — correlate Bernoulli p(1-p) with observed item variance,
81	      parallel binary vs text_exact_match analysis (MD1 defense);
82	      (m) Bootstrap vs jackknife CI comparison — delete-1 jackknife as independence-safe alternative,
83	      compare CI widths (MD6 defense);
84	      (n) Cross-benchmark design asymmetry sensitivity — re-analyze MMLU with matched 2×2 design
85	      (bf16/fp16 × T=0.0/T=0.7), compare with full 3×3 (MD8 defense);
86	      (o) G-coefficient at full benchmark size — D-study projection to 14K MMLU items (MD5 defense);
87	      (p) Logprob-based scoring across all benchmarks — expand from MMLU-only to all 5 benchmarks,
88	      support "Evaluation Metrics" in title (MD9 defense);
89	      (q) GPU cost analysis — estimate compute cost for recommended D-study budgets.
90	    priority: P0
91	    gpu_budget_hours: 0  # pure analysis, no GPU
92	    hardware: none
93	    deps: [exp-001, exp-002, exp-003]
94	    status: planned
95	
96	  # === P1: Important for paper strength ===
97	
98	  - id: exp-005
99	    claim: 2  # Scale validation
100	    description: >
101	      14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter GPUs
102	      at BF16/FP16. Tests whether variance attribution patterns change with model scale
103	      and architecture (dense vs reasoning-distilled).
104	    priority: P1
105	    gpu_budget_hours: 100
106	    hardware: TBD (needs ≥48GB VRAM per GPU)
107	    deps: [exp-003]
108	    status: planned
109	
110	  - id: exp-006
111	    claim: 2  # Training-time variance
112	    description: >
113	      Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA.
114	      Fully crossed: 6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions
115	      = 432 runs/task × 4 tasks = 1,728 total fine-tuning runs.
116	      Validates whether variance hierarchy differs between inference and fine-tuning.
117	    priority: P1
118	    gpu_budget_hours: 200
119	    hardware: westd-32570 (RoBERTa-large fits easily on 96GB)
120	    deps: []
121	    status: planned
122	
123	  # === P2: Nice-to-have ===
124	
125	  - id: exp-007
126	    claim: 2  # LayerCast mitigation
127	    description: >
128	      Test LayerCast (FP16 storage + FP32 compute) as additional precision condition
129	      on MMLU. Quantifies variance reduction from this mitigation strategy.
130	    priority: P2
131	    gpu_budget_hours: 30
132	    hardware: westd-32570
133	    deps: [exp-001]
134	    status: planned
135	
136	  - id: exp-008
137	    claim: 1  # Reasoning benchmark extension
138	    description: >
139	      MATH benchmark (200 items) — tests whether item dominance pattern differs
140	      for reasoning-heavy tasks where chain-of-thought introduces additional variance.
141	    priority: P2
142	    gpu_budget_hours: 50
143	    hardware: westd-32570
144	    deps: [exp-002]
145	    status: planned
146	
147	# MVP experiment (completed)
148	mvp:
149	  - id: mvp-001
150	    registry_id: null  # MVP was run directly, not through registry
151	    description: >
152	      MVP Phase A: 1 model (Llama-3.1-8B) × 1 hardware (RTX PRO 6000) × 3 precisions
153	      × 3 prompts × 3 seeds × 2 temps × 2 orderings = 108 conditions × 50 MMLU items.
154	    result: >
155	      PASS. item_id=58.4%, precision×item=7.2%, temp×item=6.9%, prompt×item=5.7%.
156	      Direct precision×methodology <0.02%. G=0.357. float32 engine confound identified.
157	    status: completed
158	
159	# GPU budget summary
160	budget:
161	  P0_total: 435  # exp-001(100) + exp-001b(15) + exp-002(200) + exp-003(120) + exp-004(0)
162	  P1_total: 300  # exp-005(100) + exp-006(200)
163	  P2_total: 80   # exp-007(30) + exp-008(50)
164	  grand_total: 815
165	  available: "4× RTX PRO 6000 96GB (westd-32570) + TBD second GPU type"
166	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1b2f597-9195-4149-aa2d-290c12b7e4aa",
  "isSidechain": false,
  "promptId": "6db0ed55-735c-4b34-9746-8009bac2d7df",
  "type": "user",
  "uuid": "aa17c5fe-229b-444a-80a0-156b34daa9a0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/experiment_plan.yaml",
      "content": "experiments:\n  # === P0: Must-run for paper submission ===\n\n  - id: exp-001\n    claim: 1  # Item dominance at scale\n    description: >\n      Full-scale precision study: 4 models (Qwen3-8B, Llama-3.1-8B-Instruct, Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3)\n      × 3 precisions (FP32, BF16, FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings\n      × 200 MMLU items (stratified). All precisions use consistent vLLM engine (V0 enforce_eager)\n      to eliminate the float32 engine confound found in MVP. Validates item dominance finding at\n      scale and with multiple models.\n    priority: P0\n    gpu_budget_hours: 100\n    hardware: westd-32570 (RTX PRO 6000 96GB)\n    deps: []\n    status: planned\n\n  - id: exp-001b\n    claim: 1  # Item dominance stability across item samples\n    description: >\n      Item resampling stability test: 3 independent stratified samples of 200 MMLU items\n      (seeds 0, 7, 99) × 1 model (Llama-3.1-8B-Instruct) × 3 precisions × 3 prompts\n      × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether the 58% item\n      dominance finding is stable across different item draws from MMLU, not an artifact\n      of the specific 200-item sample. Critical for defending the headline claim.\n    priority: P0\n    gpu_budget_hours: 15\n    hardware: westd-32570\n    deps: [exp-001]  # reuses exp-001 pipeline, runs after main study\n    status: planned\n\n  - id: exp-002\n    claim: 1  # Item dominance generalizes across benchmarks\n    description: >\n      Multi-benchmark replication: same 4 models × BF16/FP16 × 6 prompts × 6 seeds\n      × 2 temperatures × 4 orderings on GSM8K (200 items), ARC-Challenge (200 items),\n      HellaSwag (200 items). Tests whether item dominance and separability hold across\n      task types (math reasoning, science reasoning, commonsense).\n    priority: P0\n    gpu_budget_hours: 200\n    hardware: westd-32570\n    deps: [exp-001]  # need analysis pipeline validated first\n    status: planned\n\n  - id: exp-003\n    claim: 2  # Separability with hardware factor\n    description: >\n      Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16, FP16)\n      × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items.\n      Tests hardware × methodology interaction — the core separability question\n      that MVP couldn't address with only 1 GPU type.\n    priority: P0\n    gpu_budget_hours: 120\n    hardware: westd-32570 + TBD (second GPU type from Manager)\n    deps: []  # independent, can run as soon as second GPU available\n    status: blocked  # waiting for second GPU type\n\n  - id: exp-004\n    claim: 3  # D-study reproducibility budget\n    description: >\n      Comprehensive analysis of combined exp-001/001b/002/003 data. Includes:\n      (a) Model-as-facet G-theory reanalysis — treat model as crossed random facet to properly\n      attribute model×item interaction and reduce inflated item_id/residual (Dream critical);\n      (b) Bootstrap CIs (1000 resamples) on ALL variance components in ALL tables, especially\n      direct infra×method interaction term (Dream critical);\n      (c) D-study projections with CIs for optimal allocation across facets for G≥0.90/0.95/0.99,\n      with benchmark-specific budgets and comparison to IRT-based subsampling (tinyBenchmarks);\n      (d) REML vs Henderson Method I comparison as sensitivity analysis;\n      (e) Logprob-based scoring as third response variable;\n      (f) Ranking stability analysis — does precision×temperature interaction alter model rankings?\n      (g) Higher-order interaction estimation to decompose the residual component;\n      (h) G-theory vs IRT direct comparison — same MMLU data, D-study vs tinyBenchmarks IRT\n      subsampling, compare recommended item counts and discuss why G-theory is more conservative\n      (accounts for prompt/seed dimensions IRT ignores). First direct comparison in the literature;\n      (i) Power analysis — verify statistical power to detect ≥X% interaction effects given\n      5184×200 design scale, preempt \"underpowered\" reviewer concern;\n      (j) Practitioner evaluation protocol guide (Discussion/Appendix);\n      (k) Fixed vs random sensitivity — rerun G-study with temperature/ordering as fixed facets,\n      compare variance decomposition (MD2 defense);\n      (l) Binary data limitation analysis — correlate Bernoulli p(1-p) with observed item variance,\n      parallel binary vs text_exact_match analysis (MD1 defense);\n      (m) Bootstrap vs jackknife CI comparison — delete-1 jackknife as independence-safe alternative,\n      compare CI widths (MD6 defense);\n      (n) Cross-benchmark design asymmetry sensitivity — re-analyze MMLU with matched 2×2 design\n      (bf16/fp16 × T=0.0/T=0.7), compare with full 3×3 (MD8 defense);\n      (o) G-coefficient at full benchmark size — D-study projection to 14K MMLU items (MD5 defense);\n      (p) Logprob-based scoring across all benchmarks — expand from MMLU-only to all 5 benchmarks,\n      support \"Evaluation Metrics\" in title (MD9 defense);\n      (q) GPU cost analysis — estimate compute cost for recommended D-study budgets.\n    priority: P0\n    gpu_budget_hours: 0  # pure analysis, no GPU\n    hardware: none\n    deps: [exp-001, exp-002, exp-003]\n    status: planned\n\n  # === P1: Important for paper strength ===\n\n  - id: exp-005\n    claim: 2  # Scale validation\n    description: >\n      14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter GPUs\n      at BF16/FP16. Tests whether variance attribution patterns change with model scale\n      and architecture (dense vs reasoning-distilled).\n    priority: P1\n    gpu_budget_hours: 100\n    hardware: TBD (needs ≥48GB VRAM per GPU)\n    deps: [exp-003]\n    status: planned\n\n  - id: exp-006\n    claim: 2  # Training-time variance\n    description: >\n      Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA.\n      Fully crossed: 6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions\n      = 432 runs/task × 4 tasks = 1,728 total fine-tuning runs.\n      Validates whether variance hierarchy differs between inference and fine-tuning.\n    priority: P1\n    gpu_budget_hours: 200\n    hardware: westd-32570 (RoBERTa-large fits easily on 96GB)\n    deps: []\n    status: planned\n\n  # === P2: Nice-to-have ===\n\n  - id: exp-007\n    claim: 2  # LayerCast mitigation\n    description: >\n      Test LayerCast (FP16 storage + FP32 compute) as additional precision condition\n      on MMLU. Quantifies variance reduction from this mitigation strategy.\n    priority: P2\n    gpu_budget_hours: 30\n    hardware: westd-32570\n    deps: [exp-001]\n    status: planned\n\n  - id: exp-008\n    claim: 1  # Reasoning benchmark extension\n    description: >\n      MATH benchmark (200 items) — tests whether item dominance pattern differs\n      for reasoning-heavy tasks where chain-of-thought introduces additional variance.\n    priority: P2\n    gpu_budget_hours: 50\n    hardware: westd-32570\n    deps: [exp-002]\n    status: planned\n\n# MVP experiment (completed)\nmvp:\n  - id: mvp-001\n    registry_id: null  # MVP was run directly, not through registry\n    description: >\n      MVP Phase A: 1 model (Llama-3.1-8B) × 1 hardware (RTX PRO 6000) × 3 precisions\n      × 3 prompts × 3 seeds × 2 temps × 2 orderings = 108 conditions × 50 MMLU items.\n    result: >\n      PASS. item_id=58.4%, precision×item=7.2%, temp×item=6.9%, prompt×item=5.7%.\n      Direct precision×methodology <0.02%. G=0.357. float32 engine confound identified.\n    status: completed\n\n# GPU budget summary\nbudget:\n  P0_total: 435  # exp-001(100) + exp-001b(15) + exp-002(200) + exp-003(120) + exp-004(0)\n  P1_total: 300  # exp-005(100) + exp-006(200)\n  P2_total: 80   # exp-007(30) + exp-008(50)\n  grand_total: 815\n  available: \"4× RTX PRO 6000 96GB (westd-32570) + TBD second GPU type\"\n",
      "numLines": 166,
      "startLine": 1,
      "totalLines": 166
    }
  },
  "sourceToolAssistantUUID": "b1b2f597-9195-4149-aa2d-290c12b7e4aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T08:07:17.556Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019oxfZvvUtu4rzTBASJQV66`</summary>

```json
{
  "pattern": "projects/nlp_variance_gtheory/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa17c5fe-229b-444a-80a0-156b34daa9a0",
  "isSidechain": false,
  "requestId": "req_011CbFNTJAq3WdP2cFNLVt4K",
  "type": "assistant",
  "uuid": "3f60412d-afad-46e7-9932-516284690272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197kTPpgUS1YMN6up4xZE1A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1982,
      "cache_read_input_tokens": 28444,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1982,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 28444,
          "cache_creation_input_tokens": 1982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1982
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

_source line 16 · 2026-05-21T08:07:17.586Z_

<details><summary>↩ Tool result · `toolu_019oxfZvvUtu4rzTBASJQV66`</summary>

```text
projects/nlp_variance_gtheory/literature_map.yaml
projects/nlp_variance_gtheory/distill_tmp/hua2025flaw.yaml
projects/nlp_variance_gtheory/distill_tmp/mesting2026hidden.yaml
projects/nlp_variance_gtheory/distill_tmp/brittlebench2026.yaml
projects/nlp_variance_gtheory/distill_tmp/yuan2025layercast.yaml
projects/nlp_variance_gtheory/distill_tmp/kunievsky2025intent.yaml
projects/nlp_variance_gtheory/distill_tmp/thinkingmachines2025batch.yaml
projects/nlp_variance_gtheory/distill_tmp/messina2026background.yaml
projects/nlp_variance_gtheory/distill_tmp/generalizit2024.yaml
projects/nlp_variance_gtheory/distill_tmp/bui2025seeds.yaml
projects/nlp_variance_gtheory/distill_tmp/sameprompt2026.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/median/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/median/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/meta.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/meta.yaml
projects/nlp_variance_gtheory/experiment_plan.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/median/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/worst/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/median/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/worst/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/meta.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/best/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/median/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/worst/imagined_experiments.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/best/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/median/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/worst/review_context.yaml
projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/meta.yaml
projects/nlp_variance_gtheory/mistakes.yaml
projects/nlp_variance_gtheory/decisions.yaml
projects/nlp_variance_gtheory/dream_registry.yaml
projects/nlp_variance_gtheory/artifacts/manifest.yaml
projects/nlp_variance_gtheory/registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f60412d-afad-46e7-9932-516284690272",
  "isSidechain": false,
  "promptId": "6db0ed55-735c-4b34-9746-8009bac2d7df",
  "type": "user",
  "uuid": "8576179c-df24-40b1-bcc0-4431a320c2e4",
  "toolUseResult": {
    "filenames": [
      "projects/nlp_variance_gtheory/literature_map.yaml",
      "projects/nlp_variance_gtheory/distill_tmp/hua2025flaw.yaml",
      "projects/nlp_variance_gtheory/distill_tmp/mesting2026hidden.yaml",
      "projects/nlp_variance_gtheory/distill_tmp/brittlebench2026.yaml",
      "projects/nlp_variance_gtheory/distill_tmp/yuan2025layercast.yaml",
      "projects/nlp_variance_gtheory/distill_tmp/kunievsky2025intent.yaml",
      "projects/nlp_variance_gtheory/distill_tmp/thinkingmachines2025batch.yaml",
      "projects/nlp_variance_gtheory/distill_tmp/messina2026background.yaml",
      "projects/nlp_variance_gtheory/distill_tmp/generalizit2024.yaml",
      "projects/nlp_variance_gtheory/distill_tmp/bui2025seeds.yaml",
      "projects/nlp_variance_gtheory/distill_tmp/sameprompt2026.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/median/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/median/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/worst/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/meta.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/best/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/median/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/worst/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T222113/meta.yaml",
      "projects/nlp_variance_gtheory/experiment_plan.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/median/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/worst/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/best/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/median/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/worst/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T032813/meta.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/best/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/median/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/worst/imagined_experiments.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/best/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/median/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/worst/review_context.yaml",
      "projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/meta.yaml",
      "projects/nlp_variance_gtheory/mistakes.yaml",
      "projects/nlp_variance_gtheory/decisions.yaml",
      "projects/nlp_variance_gtheory/dream_registry.yaml",
      "projects/nlp_variance_gtheory/artifacts/manifest.yaml",
      "projects/nlp_variance_gtheory/registry.yaml"
    ],
    "durationMs": 26,
    "numFiles": 45,
    "truncated": false
  },
  "sourceToolAssistantUUID": "3f60412d-afad-46e7-9932-516284690272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17 · 2026-05-21T08:07:17.640Z_

````json
{
  "parentUuid": "8576179c-df24-40b1-bcc0-4431a320c2e4",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**nlp_variance_gtheory**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"nlp_variance_gtheory\")` 或 `load_project_config(\"nlp_variance_gtheory\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n- **LLM Evaluation Variance — Research Patterns** — Experimental consensus on variance sources, decomposition methods, and gaps in LLM evaluation reproducibility (10 papers, 2024-2026)  →  `/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-research.skill.md`\n- **LLM Evaluation Variance — Writing Patterns** — Narrative strategies, figure/table conventions from LLM evaluation variance papers (8 deep-read, 2024-2026)  →  `/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-writing.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/nlp_variance_gtheory/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "cbbc4f0d-2273-4efa-9be5-6576a5db0076",
  "timestamp": "2026-05-21T08:07:17.640Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Gradient flat or reversed; item resampling unstable; core story reduces to single-benchmark (MMLU) model×item finding — must reframe angle 核心假设：['exp-002:…",
  "leafUuid": "cbbc4f0d-2273-4efa-9be5-6576a5db0076",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Model×item interaction in LLM evaluation variance",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab"
}
```

---

### Assistant

_source line 20 · 2026-05-21T08:07:22.784Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the previous worst-tier imagined experiments to understand the format used before.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbbc4f0d-2273-4efa-9be5-6576a5db0076",
  "isSidechain": false,
  "requestId": "req_011CbFNTaf2S7wUPzaeTHsZW",
  "type": "assistant",
  "uuid": "b3f52395-7713-45fb-a026-3ce30bcd997f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoWTfdaGJL6jWobQVmFNAB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9604,
      "cache_read_input_tokens": 30426,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 156,
          "cache_read_input_tokens": 30426,
          "cache_creation_input_tokens": 9604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9604
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

_source line 21 · 2026-05-21T08:07:23.781Z_

Let me check the most recent dream report's worst-tier format for consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3f52395-7713-45fb-a026-3ce30bcd997f",
  "isSidechain": false,
  "requestId": "req_011CbFNTaf2S7wUPzaeTHsZW",
  "type": "assistant",
  "uuid": "8b790835-8bca-49d3-a2a6-eccf6247c947",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoWTfdaGJL6jWobQVmFNAB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9604,
      "cache_read_input_tokens": 30426,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 156,
          "cache_read_input_tokens": 30426,
          "cache_creation_input_tokens": 9604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9604
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

_source line 22 · 2026-05-21T08:07:24.691Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F6cznVetWjfsnpL1QEV7LA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b790835-8bca-49d3-a2a6-eccf6247c947",
  "isSidechain": false,
  "requestId": "req_011CbFNTaf2S7wUPzaeTHsZW",
  "type": "assistant",
  "uuid": "7e0cd282-e1e2-4092-9146-8de24cbe1fef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoWTfdaGJL6jWobQVmFNAB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9604,
      "cache_read_input_tokens": 30426,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 156,
          "cache_read_input_tokens": 30426,
          "cache_creation_input_tokens": 9604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9604
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

_source line 23 · 2026-05-21T08:07:25.064Z_

<details><summary>↩ Tool result · `toolu_01F6cznVetWjfsnpL1QEV7LA`</summary>

```text
1	tier: worst
2	narrative_guidance: '核心reframe：放弃model×item作为headline finding，整篇论文重心从"variance source
3	  discovery" 转向"G-theory as a framework for metric-conditional evaluation reliability"。
4	  新Claim 1：Metric-conditional reproducibility budgets——binary vs text-exact-match的G系数
5	  差异(0.611 vs 0.007)作为headline数字，这基于已完成的Llama数据，不依赖4-model结果。 新Claim 2：IRT vs G-theory直接对比——3.0-3.5×的item需求差异作为standalone
6	  finding， 论证G-theory捕获了IRT忽略的prompt/seed/ordering维度，这是文献中首个此类对比。 新Claim 3：原Claim
7	  1降为"preliminary evidence"——model×item在2-model设计中显著(26%) 但随模型数增加衰减至7%，讨论可能原因并标注为需更大规模验证。
8	  标题调整为"Reproducibility Budgets for LLM Evaluation: Why G-theory Demands 3-4× More
9	  Items Than IRT"—— 突出IRT对比而非方差分解。Contribution 4工具包升级为主要卖点之一。 温度分层分析(已完成)和6项方法学鲁棒性验证(已完成)成为论文方法学贡献的核心。
10	  仍投AAAI同一track，目标borderline（5.0-5.5/10），但有清晰的rebuttal策略。 若时间允许，将exp-002剩余benchmark数据作为camera-ready补充。
11	  关键风险：cross-benchmark gradient叙事完全不可用，论文失去"cross-benchmark"维度， scope收窄至"single-benchmark
12	  deep dive + metric-conditional framework"。
13	
14	  '
15	imagined_experiments:
16	- name: 'exp-001: Full-scale 4-model MMLU precision study'
17	  plan_id: exp-001
18	  description: '4 models × 3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings
19	    × 200 items。 Llama/Gemma已完成，Mistral完成，Qwen3完成但有部分数据质量问题(~3%条件因OOM重跑， 引入时间混淆)。4-model
20	    G-theory分析揭示2-model结果被Llama/Gemma架构差异放大。
21	
22	    '
23	  expected_results:
24	    total_records: 825600
25	    total_conditions: 5184
26	    models_completed: 4
27	    qwen3_data_quality_issues_pct: 3.2
28	    llama_single_model_item_id_pct: 61.1
29	    gemma_single_model_item_id_pct: 57.3
30	    mistral_single_model_item_id_pct: 59.8
31	    qwen3_single_model_item_id_pct: 55.2
32	    avg_single_model_item_id_pct: 58.4
33	    avg_single_model_G_binary: 0.594
34	    cross_4model_item_id_pct: 42.1
35	    cross_4model_model_x_item_pct: 7.3
36	    cross_4model_model_pct: 18.6
37	    cross_4model_residual_pct: 19.8
38	    cross_4model_prompt_x_item_pct: 4.2
39	    cross_4model_seed_x_item_pct: 3.9
40	    cross_4model_temp_pct: 1.1
41	    cross_4model_precision_pct: 0.8
42	    cross_4model_G_binary: 0.31
43	    two_model_model_x_item_pct: 26.2
44	    four_model_model_x_item_pct: 7.3
45	    interaction_decay_ratio: 3.59
46	    two_model_cross_G: 0.073
47	    four_model_cross_G: 0.31
48	    infra_x_method_binary_pct: 0.3
49	    infra_x_method_text_pct: 3.8
50	    precision_x_temperature_text_pct: 4.15
51	    llama_bf16_fp16_gap_pp: 0.06
52	    gemma_bf16_fp32_gap_pp: 7.8
53	    mistral_bf16_fp16_gap_pp: 0.09
54	    qwen3_bf16_fp16_gap_pp: 0.12
55	    fp32_degradation_all_models_avg_pp: 7.2
56	  result_rationale: '2-model设计中26.2%的model×item交互源于Llama(decoder-only, GQA)与Gemma(decoder-only,
57	    grouped-query attention, 不同tokenizer)之间的架构最大化差异：两者在知识编码方式上 根本不同，导致同一item对Llama容易而对Gemma难（或反之）。加入Mistral(与Llama架构
58	    高度同源，同为Llama-family decoder)和Qwen3(类似架构但中文语料占比高)后， model facet的universe从"两个极端"扩展到"四个含重叠的点"。Mistral/Qwen3的item
59	    difficulty profile与Llama高度相关(r>0.85)，稀释了Gemma带来的交互方差。 统计上，2-model设计中model只有1个自由度，任何两模型间的系统差异都被完全分配到
60	    model×item交互项；4-model设计中model有3个自由度，交互被分散。model主效应从<1% 升至18.6%反映了模型间整体能力差异(Gemma
61	    73.2% vs Llama 66.4% vs Mistral 62.1% vs Qwen3 68.5%)在4-model设计中被正确分离。cross-model
62	    G从0.073回升至0.31意味着 item difficulty rankings在4模型间有moderate一致性——"崩塌"叙事不成立，但0.31仍
63	    远低于0.80的dependability阈值，model-specificity是真实存在的，只是程度被2-model 设计夸大了约3.6倍。infra×method在binary下仍<0.5%，text-exact-match下precision×
64	    temperature仍~4%，与Llama-only结果一致——这一finding是robust的。
65	
66	    '
67	  tables:
68	  - name: 'Table 1: Single-model variance decomposition (4 models separately)'
69	    data:
70	      columns:
71	      - source
72	      - llama_pct
73	      - gemma_pct
74	      - mistral_pct
75	      - qwen3_pct
76	      - avg_pct
77	      rows:
78	      - - item_id
79	        - 61.1
80	        - 57.3
81	        - 59.8
82	        - 55.2
83	        - 58.4
84	      - - residual
85	        - 17.2
86	        - 19.8
87	        - 18.6
88	        - 21.3
89	        - 19.2
90	      - - prompt_template:item_id
91	        - 4.6
92	        - 5.1
93	        - 4.8
94	        - 5.9
95	        - 5.1
96	      - - seed:item_id
97	        - 4.7
98	        - 4.3
99	        - 4.5
100	        - 5.2
101	        - 4.7
102	      - - precision:item_id
103	        - 7.2
104	        - 8.1
105	        - 6.9
106	        - 6.3
107	        - 7.1
108	      - - temperature:item_id
109	        - 3.1
110	        - 3.5
111	        - 3.2
112	        - 3.8
113	        - 3.4
114	      - - temperature
115	        - 1.2
116	        - 1.0
117	        - 1.4
118	        - 1.1
119	        - 1.2
120	      - - precision
121	        - 0.5
122	        - 0.4
123	        - 0.3
124	        - 0.7
125	        - 0.5
126	      - - other_interactions
127	        - 0.4
128	        - 0.5
129	        - 0.5
130	        - 0.5
131	        - 0.5
132	  - name: 'Table 2: 2-model vs 4-model crossed variance decomposition'
133	    data:
134	      columns:
135	      - source
136	      - two_model_pct
137	      - four_model_pct
138	      - delta_pp
139	      rows:
140	      - - item_id
141	        - 37.9
142	        - 42.1
143	        - 4.2
144	      - - model_x_item
145	        - 26.2
146	        - 7.3
147	        - -18.9
148	      - - model
149	        - 0.8
150	        - 18.6
151	        - 17.8
152	      - - residual
153	        - 21.6
154	        - 19.8
155	        - -1.8
156	      - - prompt_template:item_id
157	        - 4.6
158	        - 4.2
159	        - -0.4
160	      - - seed:item_id
161	        - 4.7
162	        - 3.9
163	        - -0.8
164	      - - precision:item_id
165	        - 2.8
166	        - 2.4
167	        - -0.4
168	      - - temperature
169	        - 0.9
170	        - 1.1
171	        - 0.2
172	      - - precision
173	        - 0.3
174	        - 0.8
175	        - 0.5
176	  - name: 'Table 3: G-coefficients comparison'
177	    data:
178	      columns:
179	      - design
180	      - metric
181	      - G_coeff
182	      - se
183	      rows:
184	      - - single_model_avg
185	        - binary
186	        - 0.594
187	        - 0.032
188	      - - single_model_avg
189	        - text_exact
190	        - 0.008
191	        - 0.003
192	      - - 2_model_crossed
193	        - binary
194	        - 0.073
195	        - 0.018
196	      - - 4_model_crossed
197	        - binary
198	        - 0.31
199	        - 0.041
200	      - - 4_model_crossed
201	        - text_exact
202	        - 0.005
203	        - 0.002
204	  figures_description:
205	  - 'Fig 1: 并排stacked-bar图，左侧2-model右侧4-model方差分解。model×item从红色26.2%的大色块缩小为7.3%的窄条，model主效应从几乎不可见扩展为18.6%的蓝色块。视觉上''reveal''效果减弱——不再是dramatic
206	    collapse，而是moderate shift。'
207	  - 'Fig 2: 4模型间item difficulty rank correlation热力图。Llama-Mistral r=0.88, Llama-Qwen3
208	    r=0.82, Llama-Gemma r=0.61, Gemma-Mistral r=0.58。显示Gemma是outlier，解释为何2-model设计(恰好选了Llama+Gemma)夸大了交互。'
209	  analysis: '4-model结果对原Claim 1构成实质性削弱。model×item从26.2%降至7.3%意味着这不再是 "second-largest
210	    source"——它现在排在item_id(42.1%)、residual(19.8%)、model(18.6%) 之后，仅列第四。cross-model
211	    G从0.073升至0.31意味着"崩塌"叙事需要大幅修正。 但0.31仍远低于0.80，model-specificity仍然是一个真实现象。论文策略：将model×item
212	    降级为"preliminary evidence"，报告2-model和4-model结果，讨论sample size对 interaction estimation的影响(2-model只有1
213	    df for model)，标注需要8+模型验证。 转而将metric-conditional G差异(binary 0.594 vs text 0.008)和IRT对比作为headline。
214	    单模型方差分解的稳定性(4模型间item_id=55-61%)是一个正面发现——可以支撑 "item dominance is robust across
215	    models"的claim，但这是psychometrically expected 而非novel。
216	
217	    '
218	- name: 'exp-001b: Item resampling stability test'
219	  plan_id: exp-001b
220	  description: '3个独立200-item分层抽样(seeds 0, 7, 99) × Llama × 3 precisions × 3 prompts
221	    × 3 seeds × 2 orderings = 54条件/样本。测试item_id dominance是否依赖具体抽样。 在worst档中，resampling显示item_id有显著波动，200-item子集不够stable。
222	
223	    '
224	  expected_results:
225	    total_samples: 3
226	    conditions_per_sample: 54
227	    records_per_sample: 10800
228	    total_records: 32400
229	    sample_seed0_item_id_pct: 61.1
230	    sample_seed7_item_id_pct: 52.4
231	    sample_seed99_item_id_pct: 68.3
232	    item_id_mean_pct: 60.6
233	    item_id_sd_pct: 8.0
234	    item_id_cv: 0.132
235	    item_id_cv_strict: 0.3
236	    sample_seed0_G_binary: 0.611
237	    sample_seed7_G_binary: 0.528
238	    sample_seed99_G_binary: 0.697
239	    G_binary_mean: 0.612
240	    G_binary_sd: 0.085
241	    G_binary_cv: 0.139
242	    variance_structure_profile_corr_01: 0.82
243	    variance_structure_profile_corr_02: 0.71
244	    variance_structure_profile_corr_12: 0.77
245	    avg_profile_corr: 0.77
246	    sample_seed0_residual_pct: 17.2
247	    sample_seed7_residual_pct: 22.8
248	    sample_seed99_residual_pct: 13.1
249	    residual_cv: 0.28
250	    resampling_item_id_cv: 0.3
251	  result_rationale: '200 items是MMLU 14,042题的1.4%。即使使用分层抽样(按subject category)，每个category
252	    内部的item difficulty分布仍有大量变异。MMLU的57个subjects中，部分subjects只有 ~100题，200-item分层抽样在小subjects上可能只抽到2-3题，这些题的难度方差极大。
253	    seed 99的样本恰好抽到了更多高方差subjects(如abstract_algebra, formal_logic)中的 极端难度item，导致item_id膨胀至68.3%——这些item的p值接近0或1，Bernoulli方差
254	    p(1-p)很小，但它们与其他item的巨大difficulty差异推高了item_id方差成分。 seed 7的样本则抽到了更"中等难度"的集中分布，item间差异较小，item_id降至52.4%。
255	    CV=0.30意味着200-item子集的方差结构有约30%的相对变异——这不是catastrophic (方差ranking仍然是item_id > residual
256	    > others)，但足以让reviewer质疑具体百分比 的精确性。对论文的影响：不能把"61.1%"当作point estimate来报告，需要报告 range
257	    [52-68%]或CI。这削弱了精确数字的说服力，但"item dominance"的定性结论 (item_id始终是最大source)仍然成立。G系数的CV=0.14较低，说明reliability
258	    estimate本身比方差百分比更robust——这是一个可以强调的正面发现。
259	
260	    '
261	  tables:
262	  - name: 'Table 4: Resampling stability across 3 item draws'
263	    data:
264	      columns:
265	      - source
266	      - seed0_pct
267	      - seed7_pct
268	      - seed99_pct
269	      - mean_pct
270	      - sd_pct
271	      - cv
272	      rows:
273	      - - item_id
274	        - 61.1
275	        - 52.4
276	        - 68.3
277	        - 60.6
278	        - 8.0
279	        - 0.3
280	      - - residual
281	        - 17.2
282	        - 22.8
283	        - 13.1
284	        - 17.7
285	        - 4.9
286	        - 0.28
287	      - - precision:item_id
288	        - 7.2
289	        - 8.5
290	        - 5.8
291	        - 7.2
292	        - 1.4
293	        - 0.19
294	      - - prompt_template:item_id
295	        - 4.6
296	        - 5.9
297	        - 4.1
298	        - 4.9
299	        - 0.9
300	        - 0.19
301	      - - seed:item_id
302	        - 4.7
303	        - 5.1
304	        - 4.3
305	        - 4.7
306	        - 0.4
307	        - 0.09
308	      - - temperature:item_id
309	        - 3.1
310	        - 3.2
311	        - 2.9
312	        - 3.1
313	        - 0.2
314	        - 0.05
315	      - - temperature
316	        - 1.2
317	        - 1.1
318	        - 1.0
319	        - 1.1
320	        - 0.1
321	        - 0.09
322	      - - precision
323	        - 0.5
324	        - 0.6
325	        - 0.3
326	        - 0.5
327	        - 0.2
328	        - 0.33
329	  - name: 'Table 5: G-coefficient stability'
330	    data:
331	      columns:
332	      - metric
333	      - seed0_G
334	      - seed7_G
335	      - seed99_G
336	      - mean_G
337	      - sd_G
338	      - cv
339	      rows:
340	      - - binary
341	        - 0.611
342	        - 0.528
343	        - 0.697
344	        - 0.612
345	        - 0.085
346	        - 0.139
347	      - - text_exact
348	        - 0.007
349	        - 0.005
350	        - 0.009
351	        - 0.007
352	        - 0.002
353	        - 0.286
354	  figures_description:
355	  - 'Fig 3: 三组200-item样本的方差分解并排stacked-bar。item_id始终是最大source但高度变化明显(52-68%)。添加误差线显示±1SD范围。'
356	  analysis: 'resampling结果对论文有双重影响。负面：具体百分比不可作为precise point estimate， 需要报告range或bootstrap
357	    CI，reviewer可以合理质疑"为什么不用更大的item sample"。 正面：item_id在所有3次抽样中都是最大的方差源(最低52.4%仍远超第二名residual的
358	    22.8%)，定性结论robust。G系数的较低变异(CV=0.14)意味着reliability estimate 本身是stable的——即使方差成分百分比波动，最终的reliability判断不变。
359	    论文策略：报告mean±SD而非point estimate，在Limitations中讨论200-item的局限性， 引用D-study中500+item的建议作为methodological回应。但这会让数字less
360	    punchy， reviewer可能觉得"连自己的item sample都不stable，怎么能给别人开D-study budgets"。
361	
362	    '
363	- name: 'exp-002: Multi-benchmark replication (partial)'
364	  plan_id: exp-002
365	  description: '原计划4 models × 2 prec × 6 prompts × 6 seeds × 2 temps × 4 orderings
366	    × 200 items on GSM8K/ARC/HellaSwag。在worst档中，仅完成GSM8K(1个模型完整 + 1个模型部分)和ARC-Challenge(1个模型部分)。HellaSwag未开始。
367	    时间被exp-001的4-model数据收集和debug消耗。
368	
369	    '
370	  expected_results:
371	    gsm8k_models_completed: 1.5
372	    arc_models_completed: 0.7
373	    hellaswag_models_completed: 0
374	    total_benchmarks_with_usable_data: 2
375	    total_benchmarks_fully_completed: 0
376	    gsm8k_llama_records: 57600
377	    gsm8k_llama_conditions: 288
378	    gsm8k_llama_item_id_pct: 38.2
379	    gsm8k_llama_residual_pct: 31.4
380	    gsm8k_llama_prompt_template_item_id_pct: 12.8
381	    gsm8k_llama_seed_item_id_pct: 6.1
382	    gsm8k_llama_temperature_pct: 5.3
383	    gsm8k_llama_precision_item_id_pct: 2.9
384	    gsm8k_llama_precision_pct: 0.4
385	    gsm8k_llama_G_binary: 0.421
386	    gsm8k_llama_overall_accuracy: 0.487
387	    arc_llama_records: 40320
388	    arc_llama_conditions: 202
389	    arc_llama_item_id_pct: 54.7
390	    arc_llama_residual_pct: 20.3
391	    arc_llama_prompt_template_item_id_pct: 7.2
392	    arc_llama_G_binary: 0.563
393	    arc_llama_overall_accuracy: 0.531
394	    arc_data_quality_note: partial, missing T=0.7 conditions and orderings 3-4
395	    mmlu_item_id_pct: 61.1
396	    gsm8k_item_id_pct: 38.2
397	    arc_item_id_pct: 54.7
398	    benchmark_item_id_spread_pp: 22.9
399	    benchmark_gradient_rank_corr: 0.0
400	    mmlu_gsm8k_profile_corr: 0.42
401	    mmlu_arc_profile_corr: 0.78
402	    gsm8k_arc_profile_corr: 0.38
403	    gsm8k_infra_x_method_binary_pct: 1.1
404	    arc_infra_x_method_binary_pct: 0.6
405	  result_rationale: 'GSM8K是数学推理任务，与MMLU的知识检索本质不同。GSM8K的item_id仅38.2%(vs MMLU 61.1%)的原因：数学题的难度方差较小——大多数GSM8K题都需要类似步骤数的算术推理，
406	    item间difficulty差异不如MMLU(从trivia到advanced physics)那么大。相应地， prompt_template:item_id升至12.8%，因为chain-of-thought
407	    prompt的具体措辞对 推理过程影响更大(某些prompt引导更好的step-by-step分解)。residual升至31.4% 反映了推理任务的内在随机性——同一条件下模型可能走不同推理路径得到不同结果。
408	    temperature对GSM8K的影响更大(5.3% vs MMLU 1.2%)因为推理任务在T>0时的token sampling对中间步骤的影响会cascade到最终答案。ARC-Challenge(科学推理)的item_id
409	    54.7%介于MMLU和GSM8K之间，但仅有部分数据不能做firm conclusion。 关键问题：3个数据点(MMLU 61%, ARC 55%, GSM8K
410	    38%)没有形成任何可解释的梯度—— 按"知识→推理"排序是MMLU>ARC>GSM8K，看起来有趋势但(a)ARC也是部分数据， (b)HellaSwag缺失，(c)
411	    3个点无法区分线性趋势和噪声(任何3点都可以拟合线性)。 Rank correlation无法计算或为trivially 1.0(3个点完美排序)，无统计意义。
412	    infra×method在GSM8K上为1.1%(高于MMLU的<0.1%)，可能反映precision对推理中间 步骤的累积效应，但也可能是noise——CI会很宽。这个结果让"separability
413	    is benchmark-conditional"无法作为firm claim。
414	
415	    '
416	  tables:
417	  - name: 'Table 6: Cross-benchmark variance decomposition (single-model Llama, binary)'
418	    data:
419	      columns:
420	      - source
421	      - mmlu_pct
422	      - gsm8k_pct
423	      - arc_partial_pct
424	      rows:
425	      - - item_id
426	        - 61.1
427	        - 38.2
428	        - 54.7
429	      - - residual
430	        - 17.2
431	        - 31.4
432	        - 20.3
433	      - - prompt_template:item_id
434	        - 4.6
435	        - 12.8
436	        - 7.2
437	      - - seed:item_id
438	        - 4.7
439	        - 6.1
440	        - 5.8
441	      - - temperature
442	        - 1.2
443	        - 5.3
444	        - 3.1
445	      - - precision:item_id
446	        - 7.2
447	        - 2.9
448	        - 5.2
449	      - - temperature:item_id
450	        - 3.1
451	        - 1.8
452	        - 2.4
453	      - - precision
454	        - 0.5
455	        - 0.4
456	        - 0.3
457	      - - other
458	        - 0.4
459	        - 1.1
460	        - 1.0
461	  - name: 'Table 7: G-coefficients by benchmark'
462	    data:
463	      columns:
464	      - benchmark
465	      - n_items
466	      - G_binary
467	      - G_text_exact
468	      - data_completeness
469	      rows:
470	      - - MMLU
471	        - 200
472	        - 0.611
473	        - 0.007
474	        - 100%
475	      - - GSM8K
476	        - 200
477	        - 0.421
478	        - 0.003
479	        - 100% (1 model)
480	      - - ARC-Challenge
481	        - 200
482	        - 0.563
483	        - 0.006
484	        - ~70% (1 model)
485	      - - HellaSwag
486	        - 200
487	        - null
488	        - null
489	        - 0%
490	  figures_description:
491	  - 'Fig 4: 3-benchmark stacked-bar图（MMLU/GSM8K/ARC），但ARC标注''partial data''虚线边框。没有清晰的monotonic梯度——更像是每个benchmark有自己的idiosyncratic方差签名。'
492	  analysis: 'exp-002的部分完成是worst档的核心打击之一。原计划的"cross-benchmark gradient" 需要4+ benchmarks才能做credible的趋势分析，现在只有1.5-2个可用benchmark。
493	    MMLU 61% vs GSM8K 38%的差异是real的，但2个数据点无法支撑"gradient"叙事—— reviewer会问"这只是两个不同benchmark有不同方差结构，这不是trivially
494	    obvious吗？" ARC的部分数据(54.7%)暗示MMLU和GSM8K之间可能有中间值，但数据不完整不能claim。 论文策略：完全放弃"cross-benchmark
495	    gradient"作为finding，改为在Discussion中 报告MMLU vs GSM8K的差异作为"preliminary observation
496	    suggesting task-type dependence"。GSM8K的数据可以用来支持"metric-conditional"叙事——GSM8K的
497	    G=0.421(vs MMLU 0.611)意味着reasoning benchmarks需要更多items，但这是 a secondary point。主要损失：论文scope从"multi-benchmark"收缩为"primarily
498	    MMLU with limited cross-benchmark evidence"。
499	
500	    '
501	- name: 'exp-003: Multi-hardware G-study'
502	  plan_id: exp-003
503	  description: '原计划4 models × 2+ GPU types × 2 precisions × full crossing on MMLU。
504	    在worst档中，exp-003完全缺失——第二种GPU类型从未获得。
505	
506	    '
507	  expected_results:
508	    status: NOT_COMPLETED
509	    gpu_types_available: 1
510	    second_gpu_acquired: false
511	    records_collected: 0
512	    blocking_reason: second GPU type not procured; Manager unable to allocate additional
513	      hardware within timeline
514	  result_rationale: 'exp-003的核心依赖是获得第二种GPU类型(如A100、H100或不同架构的consumer GPU)。 在worst档中，Manager未能在AAAI截稿前分配额外硬件——可能因预算审批延迟、
515	    GPU集群排队过长、或所需硬件型号不可用。没有第二种GPU，"multi-hardware crossing" 无法执行。论文只能在单一GPU(RTX PRO
516	    6000)上讨论"numerical precision"而非 "hardware"。这意味着Claim 2(Conditional Separability)中的"infrastructure"
517	    实际上仅限于"precision facet on a single GPU architecture"——reviewer会指出 这是一个substantial
518	    scope limitation。Yuan et al. (2025)记录的hardware-specific 差异(CUDA kernel implementation,
519	    memory bandwidth effects)完全无法验证。 但论文可以将此framing为"precision is the infrastructure
520	    facet we can study; hardware crossing is future work"——这是honest但weakens the contribution。
521	    exp-003的缺失也影响exp-004(无hardware数据可分析)和exp-005(deps on exp-003)。
522	
523	    '
524	  tables: []
525	  figures_description: []
526	  analysis: 'exp-003缺失是worst档的defining characteristic之一。impact chain: (1) Claim 2的"infrastructure"缩窄为"precision"；
527	    (2) exp-004的hardware分析完全消失； (3) exp-005被block； (4) "fully crossed infrastructure
528	    × methodology"的framing需要大幅qualifier； (5) 论文title如果含"hardware"需要修改。 Mitigation：将exp-003的缺失作为explicit
529	    limitation，引用Yuan et al. (2025)的 hardware结果作为motivation for future work，强调我们的precision分析是
530	    complementary而非替代。在rebuttal策略中准备"we agree hardware crossing is essential and plan
531	    to include it in camera-ready"（如果能在rebuttal期间拿到GPU）。
532	
533	    '
534	- name: 'exp-004: Comprehensive analysis (partial)'
535	  plan_id: exp-004
536	  description: '基于exp-001/001b/002/003数据的全面分析。在worst档中，缺失exp-003数据， exp-002仅有部分数据。分析范围大幅收缩。仍可执行的分析：
537	    (a) 4-model G-theory交叉分析(exp-001)，(b) bootstrap CIs，(c) IRT对比， (d) 温度分层，(e) 固定vs随机敏感性，(f)
538	    D-study投影。
539	
540	    '
541	  expected_results:
542	    planned_analyses: 17
543	    executable_analyses: 11
544	    blocked_analyses: 6
545	    irt_recommended_items_mmlu: 142
546	    gtheory_recommended_items_mmlu_practical: 468
547	    gtheory_recommended_items_mmlu_all_random: 498
548	    irt_vs_gtheory_item_ratio_practical: 3.3
549	    irt_vs_gtheory_item_ratio_all_random: 3.51
550	    irt_gtheory_gap_attribution:
551	      prompt_x_item_contribution_pct: 32
552	      seed_x_item_contribution_pct: 28
553	      ordering_residual_contribution_pct: 40
554	    item_id_pct_CI_95:
555	    - 56.8
556	    - 65.4
557	    model_x_item_4model_pct_CI_95:
558	    - 3.1
559	    - 12.8
560	    residual_pct_CI_95:
561	    - 15.3
562	    - 23.1
563	    G_binary_CI_95:
564	    - 0.571
565	    - 0.652
566	    cross_model_G_4model_CI_95:
567	    - 0.22
568	    - 0.4
569	    bootstrap_jackknife_CI_width_ratio_mean: 1.01
570	    bootstrap_jackknife_CI_width_ratio_range:
571	    - 0.96
572	    - 1.04
573	    G_all_random: 0.594
574	    G_temp_fixed: 0.628
575	    G_ordering_fixed: 0.641
576	    G_both_fixed: 0.664
577	    fixed_random_max_delta_G: 0.07
578	    d_study_items_G80_practical: 468
579	    d_study_items_G80_all_random: 498
580	    d_study_items_G90_practical: 1240
581	    d_study_items_G90_all_random: 1380
582	    d_study_14k_items_G_projected: 0.972
583	    bernoulli_variance_obs_variance_corr: 0.91
584	    null_sim_item_id_pct: 0.08
585	    obs_bernoulli_ratio: 1.0008
586	    min_detectable_interaction_pct: 0.8
587	    power_at_1pct_interaction: 0.94
588	    power_at_5pct_interaction: 0.99
589	    gpu_hours_for_G80_budget: 340
590	    gpu_hours_for_G90_budget: 890
591	  result_rationale: 'IRT vs G-theory对比是worst档中最重要的surviving finding。ratio降至3.3-3.5×
592	    (vs原预期的3.6-4.4×)因为：(1) IRT在4-model数据上估计更保守(142 items vs 原2-model数据的116 items)，缩小了分母差距；(2)
593	    G-theory的D-study在4-model 分析中因model×item降至7.3%而需要fewer items来compensate，numerator从510
594	    降至498。但3.3×仍然是substantial——意味着IRT忽略的facets(prompt, seed, ordering) 贡献了约70%的额外item需求。这个finding不依赖model×item的magnitude，因此
595	    在worst档中仍然robust。 Bootstrap CIs显示item_id的95% CI为[56.8, 65.4]，range=8.6pp——与exp-001b的
596	    resampling变异一致，进一步确认point estimate的精度有限。model×item的4-model CI为[3.1, 12.8]，range很宽(9.7pp)，包含0附近——reviewer可能argue
597	    "model×item is not reliably different from zero with only 4 models"。这是对原Claim
598	    1的 又一打击：不仅point estimate从26%降至7%，CI还包含了trivially small values。 Fixed vs random
599	    sensitivity分析显示delta仅0.070——这是一个正面结果，说明 facet classification choice对G影响不大，MD2
600	    defense成立。 D-study投影到14K items给出G=0.972——这回应了MD5 "MMLU is unreliable"的误读， 但468
601	    items for G≥0.80(vs原文510)的变化需要更新所有D-study tables。
602	
603	    '
604	  tables:
605	  - name: 'Table 8: IRT vs G-theory item requirements comparison'
606	    data:
607	      columns:
608	      - method
609	      - framework
610	      - recommended_items
611	      - target
612	      - accounts_for
613	      rows:
614	      - - IRT_2PL
615	        - IRT
616	        - 142
617	        - SE<0.3
618	        - item difficulty + discrimination
619	      - - G_practical
620	        - G-theory
621	        - 468
622	        - G≥0.80
623	        - item + prompt + seed + ordering (temp/prec fixed)
624	      - - G_all_random
625	        - G-theory
626	        - 498
627	        - G≥0.80
628	        - item + prompt + seed + ordering + temp + prec
629	      - - G_high_rel
630	        - G-theory
631	        - 1240
632	        - G≥0.90
633	        - item + prompt + seed + ordering (temp/prec fixed)
634	  - name: 'Table 9: Bootstrap CIs on 4-model variance components'
635	    data:
636	      columns:
637	      - source
638	      - point_est_pct
639	      - ci_lower
640	      - ci_upper
641	      - ci_width
642	      rows:
643	      - - item_id
644	        - 42.1
645	        - 36.5
646	        - 47.8
647	        - 11.3
648	      - - model
649	        - 18.6
650	        - 12.1
651	        - 25.4
652	        - 13.3
653	      - - residual
654	        - 19.8
655	        - 15.3
656	        - 23.1
657	        - 7.8
658	      - - model_x_item
659	        - 7.3
660	        - 3.1
661	        - 12.8
662	        - 9.7
663	      - - prompt_x_item
664	        - 4.2
665	        - 2.8
666	        - 5.9
667	        - 3.1
668	      - - seed_x_item
669	        - 3.9
670	        - 2.5
671	        - 5.6
672	        - 3.1
673	      - - precision_x_item
674	        - 2.4
675	        - 1.1
676	        - 4.0
677	        - 2.9
678	      - - temperature
679	        - 1.1
680	        - 0.4
681	        - 2.2
682	        - 1.8
683	  - name: 'Table 10: D-study projections (4-model, binary metric)'
684	    data:
685	      columns:
686	      - design
687	      - n_items
688	      - n_prompts
689	      - n_seeds
690	      - G_projected
691	      - ci_95
692	      rows:
693	      - - current_practice
694	        - 200
695	        - 1
696	        - 1
697	        - 0.594
698	        - '[0.571, 0.652]'
699	      - - practical_G80
700	        - 468
701	        - 2
702	        - 3
703	        - 0.801
704	        - '[0.782, 0.831]'
705	      - - all_random_G80
706	        - 498
707	        - 2
708	        - 3
709	        - 0.8
710	        - '[0.778, 0.825]'
711	      - - practical_G90
712	        - 1240
713	        - 3
714	        - 4
715	        - 0.901
716	        - '[0.887, 0.918]'
717	      - - full_mmlu
718	        - 14042
719	        - 6
720	        - 6
721	        - 0.972
722	        - '[0.968, 0.979]'
723	  - name: 'Table 11: Fixed vs random facet sensitivity (MD2)'
724	    data:
725	      columns:
726	      - configuration
727	      - G_binary
728	      - delta_from_all_random
729	      rows:
730	      - - all_random
731	        - 0.594
732	        - 0.0
733	      - - temp_fixed
734	        - 0.628
735	        - 0.034
736	      - - ordering_fixed
737	        - 0.641
738	        - 0.047
739	      - - temp+ordering_fixed
740	        - 0.664
741	        - 0.07
742	  - name: 'Table 12: Bootstrap vs Jackknife CI comparison (MD6)'
743	    data:
744	      columns:
745	      - component
746	      - bootstrap_ci_width
747	      - jackknife_ci_width
748	      - ratio
749	      rows:
750	      - - item_id
751	        - 8.6
752	        - 8.4
753	        - 1.02
754	      - - residual
755	        - 7.8
756	        - 8.1
757	        - 0.96
758	      - - model_x_item
759	        - 9.7
760	        - 9.4
761	        - 1.03
762	      - - prompt_x_item
763	        - 3.1
764	        - 3.0
765	        - 1.03
766	      - - G_binary
767	        - 0.081
768	        - 0.079
769	        - 1.03
770	  figures_description:
771	  - 'Fig 5: D-study curve — G vs item count，显示IRT曲线(陡峭上升，142 items达到目标)和G-theory曲线(缓慢上升，468
772	    items达到G≥0.80)。两曲线的gap用阴影标注，标签''cost of multi-facet reliability''。'
773	  - 'Fig 6: 温度分层G系数热力图 — 3 temperatures × 2 metrics。binary从T=0.0(0.760)降至T=0.7(0.549)，text_exact_match全部<0.01。'
774	  analysis: 'exp-004在worst档中的核心价值：IRT对比(3.3×)和方法学robustness package。 IRT对比是self-contained的——不需要4-model结果或cross-benchmark数据，完全基于
775	    已完成的单模型Llama MMLU数据。3.3×的ratio比原预期低，但仍是"首个G-theory vs IRT直接对比"的文献贡献。Bootstrap
776	    CIs的宽度(model×item CI包含接近0的值)进一步 支持将model×item降级为"preliminary"的策略。方法学robustness的6项验证全部
777	    基于exp-001 Llama数据，不受worst档的数据缺失影响——这是论文的"guaranteed floor"。 Missing analyses:
778	    hardware crossing(exp-003缺失)、full cross-benchmark gradient (exp-002不完整)、full logprob
779	    analysis across benchmarks(只能做MMLU)。 论文需要在Methods中明确标注哪些分析是"planned but not completed"。
780	
781	    '
782	- name: 'exp-005: 14B model extension'
783	  plan_id: exp-005
784	  description: 'Qwen3-14B和DeepSeek-R1-Distill-14B在datacenter GPU上的BF16/FP16测试。 在worst档中，因exp-003缺失(deps)且无可用的48GB+
785	    VRAM GPU而完全未执行。
786	
787	    '
788	  expected_results:
789	    status: NOT_COMPLETED
790	    blocking_reason: Depends on exp-003 (not completed); no 48GB+ VRAM GPU available
791	    records_collected: 0
792	  result_rationale: 'exp-005有两个blocking依赖：(1) exp-003需要先完成以确定multi-hardware protocol；
793	    (2) 14B模型需要≥48GB VRAM GPU(RTX PRO 6000的96GB可以跑，但如果被exp-001/002 占用则无法parallel执行)。在worst档中exp-003未完成，且GPU时间被P0实验消耗，
794	    P1实验无法启动。这意味着论文没有model scale的evidence——所有结论限于7-9B模型。 reviewer concern "Missing
795	    scale validation"完全无法回应。
796	
797	    '
798	  tables: []
799	  figures_description: []
800	  analysis: 'exp-005缺失意味着reviewer concern #6 "Missing scale validation"只能在Limitations
801	    中acknowledge。论文需要argue "7-9B models represent the most commonly used open-weight
802	    model class"并cite usage statistics。但sophisticated reviewer会 指出14B+模型可能有qualitatively
803	    different variance structure(更稳定的internal representations → lower item×model interaction)。这是一个honest
804	    limitation， 不fatal但weakens generalizability claims。
805	
806	    '
807	- name: 'exp-006: Fine-tuning G-study'
808	  plan_id: exp-006
809	  description: 'RoBERTa-large在SST-2/MNLI/RTE/COPA上的fine-tuning方差分解。 在worst档中未执行——P1优先级，GPU时间不足。
810	
811	    '
812	  expected_results:
813	    status: NOT_COMPLETED
814	    blocking_reason: P1 priority; GPU budget exhausted by P0 experiments
815	    records_collected: 0
816	  result_rationale: 'exp-006需要1,728次fine-tuning runs × ~15min each ≈ 430 GPU-hours。在worst档中
817	    P0实验消耗了大部分GPU预算(exp-001 ~100h实际可能超支至130h due to reruns， exp-002 ~80h for partial
818	    completion)，剩余GPU时间不足以执行P1实验。 此外，exp-006是encoder-only(RoBERTa) fine-tuning，与主论文的decoder
819	    LLM inference focus有methodological gap——即使完成，reviewer可能argue "fine-tuning variance
820	    structure is a different question"。在worst档的reframed narrative中(focus on metric-conditional
821	    reliability)，fine-tuning分析不是 核心贡献，缺失的impact有限。
822	
823	    '
824	  tables: []
825	  figures_description: []
826	  analysis: 'exp-006缺失不fatal。论文可以在Future Work中提到"extending G-theory to fine-tuning
827	    variance decomposition"作为natural extension。reviewer concern #5 "No training-time
828	    analysis"的回应是"this paper focuses on inference-time evaluation reliability; fine-tuning
829	    stability is a complementary question studied by Dodge et al. (2020) and Sellam
830	    et al. (2022)"。
831	
832	    '
833	- name: 'exp-007: LayerCast precision mitigation'
834	  plan_id: exp-007
835	  description: 'LayerCast(FP16 storage + FP32 compute)作为额外precision条件。 P2优先级，在worst档中未执行。
836	
837	    '
838	  expected_results:
839	    status: NOT_COMPLETED
840	    blocking_reason: P2 priority; not attempted within timeline
841	    records_collected: 0
842	  result_rationale: 'P2实验在worst档中完全被deprioritize。LayerCast是一个mitigation strategy的
843	    evaluation——属于"nice to have"而非核心贡献。论文可以在Discussion中提到 LayerCast作为"practitioners
844	    can reduce precision-related variance via mixed precision strategies"的建议，无需实验数据支撑(cite
845	    existing LayerCast papers)。
846	
847	    '
848	  tables: []
849	  figures_description: []
850	  analysis: '零影响。LayerCast从未进入任何版本的核心claims。
851	
852	    '
853	- name: 'exp-008: MATH benchmark'
854	  plan_id: exp-008
855	  description: 'MATH benchmark(200 items)测试reasoning-heavy任务的item dominance。 P2优先级且deps
856	    on exp-002，在worst档中未执行。
857	
858	    '
859	  expected_results:
860	    status: NOT_COMPLETED
861	    blocking_reason: P2 priority; depends on exp-002 (incomplete)
862	    records_collected: 0
863	  result_rationale: 'exp-008依赖exp-002的multi-benchmark infrastructure和protocol。exp-002本身
864	    在worst档中仅部分完成，exp-008作为P2自然被skip。MATH作为reasoning benchmark 可能会显示更低的item_id(类似GSM8K的38%)和更高的residual，但没有数据只能
865	    在Discussion中speculate。reviewer concern "Only MMLU"的回应依赖GSM8K的 部分数据("we have preliminary
866	    evidence from GSM8K suggesting task-type dependence")。
867	
868	    '
869	  tables: []
870	  figures_description: []
871	  analysis: 'exp-008缺失加剧了"primarily MMLU"的scope limitation，但由于worst档已放弃 cross-benchmark
872	    gradient叙事，这个实验的缺失与narrative adjustment是consistent的。
873	
874	    '
875	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e0cd282-e1e2-4092-9146-8de24cbe1fef",
  "isSidechain": false,
  "promptId": "6db0ed55-735c-4b34-9746-8009bac2d7df",
  "type": "user",
  "uuid": "8178af32-c3df-4766-b955-99b87afb4c60",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T044739/worst/imagined_experiments.yaml",
      "content": "tier: worst\nnarrative_guidance: '核心reframe：放弃model×item作为headline finding，整篇论文重心从\"variance source\n  discovery\" 转向\"G-theory as a framework for metric-conditional evaluation reliability\"。\n  新Claim 1：Metric-conditional reproducibility budgets——binary vs text-exact-match的G系数\n  差异(0.611 vs 0.007)作为headline数字，这基于已完成的Llama数据，不依赖4-model结果。 新Claim 2：IRT vs G-theory直接对比——3.0-3.5×的item需求差异作为standalone\n  finding， 论证G-theory捕获了IRT忽略的prompt/seed/ordering维度，这是文献中首个此类对比。 新Claim 3：原Claim\n  1降为\"preliminary evidence\"——model×item在2-model设计中显著(26%) 但随模型数增加衰减至7%，讨论可能原因并标注为需更大规模验证。\n  标题调整为\"Reproducibility Budgets for LLM Evaluation: Why G-theory Demands 3-4× More\n  Items Than IRT\"—— 突出IRT对比而非方差分解。Contribution 4工具包升级为主要卖点之一。 温度分层分析(已完成)和6项方法学鲁棒性验证(已完成)成为论文方法学贡献的核心。\n  仍投AAAI同一track，目标borderline（5.0-5.5/10），但有清晰的rebuttal策略。 若时间允许，将exp-002剩余benchmark数据作为camera-ready补充。\n  关键风险：cross-benchmark gradient叙事完全不可用，论文失去\"cross-benchmark\"维度， scope收窄至\"single-benchmark\n  deep dive + metric-conditional framework\"。\n\n  '\nimagined_experiments:\n- name: 'exp-001: Full-scale 4-model MMLU precision study'\n  plan_id: exp-001\n  description: '4 models × 3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings\n    × 200 items。 Llama/Gemma已完成，Mistral完成，Qwen3完成但有部分数据质量问题(~3%条件因OOM重跑， 引入时间混淆)。4-model\n    G-theory分析揭示2-model结果被Llama/Gemma架构差异放大。\n\n    '\n  expected_results:\n    total_records: 825600\n    total_conditions: 5184\n    models_completed: 4\n    qwen3_data_quality_issues_pct: 3.2\n    llama_single_model_item_id_pct: 61.1\n    gemma_single_model_item_id_pct: 57.3\n    mistral_single_model_item_id_pct: 59.8\n    qwen3_single_model_item_id_pct: 55.2\n    avg_single_model_item_id_pct: 58.4\n    avg_single_model_G_binary: 0.594\n    cross_4model_item_id_pct: 42.1\n    cross_4model_model_x_item_pct: 7.3\n    cross_4model_model_pct: 18.6\n    cross_4model_residual_pct: 19.8\n    cross_4model_prompt_x_item_pct: 4.2\n    cross_4model_seed_x_item_pct: 3.9\n    cross_4model_temp_pct: 1.1\n    cross_4model_precision_pct: 0.8\n    cross_4model_G_binary: 0.31\n    two_model_model_x_item_pct: 26.2\n    four_model_model_x_item_pct: 7.3\n    interaction_decay_ratio: 3.59\n    two_model_cross_G: 0.073\n    four_model_cross_G: 0.31\n    infra_x_method_binary_pct: 0.3\n    infra_x_method_text_pct: 3.8\n    precision_x_temperature_text_pct: 4.15\n    llama_bf16_fp16_gap_pp: 0.06\n    gemma_bf16_fp32_gap_pp: 7.8\n    mistral_bf16_fp16_gap_pp: 0.09\n    qwen3_bf16_fp16_gap_pp: 0.12\n    fp32_degradation_all_models_avg_pp: 7.2\n  result_rationale: '2-model设计中26.2%的model×item交互源于Llama(decoder-only, GQA)与Gemma(decoder-only,\n    grouped-query attention, 不同tokenizer)之间的架构最大化差异：两者在知识编码方式上 根本不同，导致同一item对Llama容易而对Gemma难（或反之）。加入Mistral(与Llama架构\n    高度同源，同为Llama-family decoder)和Qwen3(类似架构但中文语料占比高)后， model facet的universe从\"两个极端\"扩展到\"四个含重叠的点\"。Mistral/Qwen3的item\n    difficulty profile与Llama高度相关(r>0.85)，稀释了Gemma带来的交互方差。 统计上，2-model设计中model只有1个自由度，任何两模型间的系统差异都被完全分配到\n    model×item交互项；4-model设计中model有3个自由度，交互被分散。model主效应从<1% 升至18.6%反映了模型间整体能力差异(Gemma\n    73.2% vs Llama 66.4% vs Mistral 62.1% vs Qwen3 68.5%)在4-model设计中被正确分离。cross-model\n    G从0.073回升至0.31意味着 item difficulty rankings在4模型间有moderate一致性——\"崩塌\"叙事不成立，但0.31仍\n    远低于0.80的dependability阈值，model-specificity是真实存在的，只是程度被2-model 设计夸大了约3.6倍。infra×method在binary下仍<0.5%，text-exact-match下precision×\n    temperature仍~4%，与Llama-only结果一致——这一finding是robust的。\n\n    '\n  tables:\n  - name: 'Table 1: Single-model variance decomposition (4 models separately)'\n    data:\n      columns:\n      - source\n      - llama_pct\n      - gemma_pct\n      - mistral_pct\n      - qwen3_pct\n      - avg_pct\n      rows:\n      - - item_id\n        - 61.1\n        - 57.3\n        - 59.8\n        - 55.2\n        - 58.4\n      - - residual\n        - 17.2\n        - 19.8\n        - 18.6\n        - 21.3\n        - 19.2\n      - - prompt_template:item_id\n        - 4.6\n        - 5.1\n        - 4.8\n        - 5.9\n        - 5.1\n      - - seed:item_id\n        - 4.7\n        - 4.3\n        - 4.5\n        - 5.2\n        - 4.7\n      - - precision:item_id\n        - 7.2\n        - 8.1\n        - 6.9\n        - 6.3\n        - 7.1\n      - - temperature:item_id\n        - 3.1\n        - 3.5\n        - 3.2\n        - 3.8\n        - 3.4\n      - - temperature\n        - 1.2\n        - 1.0\n        - 1.4\n        - 1.1\n        - 1.2\n      - - precision\n        - 0.5\n        - 0.4\n        - 0.3\n        - 0.7\n        - 0.5\n      - - other_interactions\n        - 0.4\n        - 0.5\n        - 0.5\n        - 0.5\n        - 0.5\n  - name: 'Table 2: 2-model vs 4-model crossed variance decomposition'\n    data:\n      columns:\n      - source\n      - two_model_pct\n      - four_model_pct\n      - delta_pp\n      rows:\n      - - item_id\n        - 37.9\n        - 42.1\n        - 4.2\n      - - model_x_item\n        - 26.2\n        - 7.3\n        - -18.9\n      - - model\n        - 0.8\n        - 18.6\n        - 17.8\n      - - residual\n        - 21.6\n        - 19.8\n        - -1.8\n      - - prompt_template:item_id\n        - 4.6\n        - 4.2\n        - -0.4\n      - - seed:item_id\n        - 4.7\n        - 3.9\n        - -0.8\n      - - precision:item_id\n        - 2.8\n        - 2.4\n        - -0.4\n      - - temperature\n        - 0.9\n        - 1.1\n        - 0.2\n      - - precision\n        - 0.3\n        - 0.8\n        - 0.5\n  - name: 'Table 3: G-coefficients comparison'\n    data:\n      columns:\n      - design\n      - metric\n      - G_coeff\n      - se\n      rows:\n      - - single_model_avg\n        - binary\n        - 0.594\n        - 0.032\n      - - single_model_avg\n        - text_exact\n        - 0.008\n        - 0.003\n      - - 2_model_crossed\n        - binary\n        - 0.073\n        - 0.018\n      - - 4_model_crossed\n        - binary\n        - 0.31\n        - 0.041\n      - - 4_model_crossed\n        - text_exact\n        - 0.005\n        - 0.002\n  figures_description:\n  - 'Fig 1: 并排stacked-bar图，左侧2-model右侧4-model方差分解。model×item从红色26.2%的大色块缩小为7.3%的窄条，model主效应从几乎不可见扩展为18.6%的蓝色块。视觉上''reveal''效果减弱——不再是dramatic\n    collapse，而是moderate shift。'\n  - 'Fig 2: 4模型间item difficulty rank correlation热力图。Llama-Mistral r=0.88, Llama-Qwen3\n    r=0.82, Llama-Gemma r=0.61, Gemma-Mistral r=0.58。显示Gemma是outlier，解释为何2-model设计(恰好选了Llama+Gemma)夸大了交互。'\n  analysis: '4-model结果对原Claim 1构成实质性削弱。model×item从26.2%降至7.3%意味着这不再是 \"second-largest\n    source\"——它现在排在item_id(42.1%)、residual(19.8%)、model(18.6%) 之后，仅列第四。cross-model\n    G从0.073升至0.31意味着\"崩塌\"叙事需要大幅修正。 但0.31仍远低于0.80，model-specificity仍然是一个真实现象。论文策略：将model×item\n    降级为\"preliminary evidence\"，报告2-model和4-model结果，讨论sample size对 interaction estimation的影响(2-model只有1\n    df for model)，标注需要8+模型验证。 转而将metric-conditional G差异(binary 0.594 vs text 0.008)和IRT对比作为headline。\n    单模型方差分解的稳定性(4模型间item_id=55-61%)是一个正面发现——可以支撑 \"item dominance is robust across\n    models\"的claim，但这是psychometrically expected 而非novel。\n\n    '\n- name: 'exp-001b: Item resampling stability test'\n  plan_id: exp-001b\n  description: '3个独立200-item分层抽样(seeds 0, 7, 99) × Llama × 3 precisions × 3 prompts\n    × 3 seeds × 2 orderings = 54条件/样本。测试item_id dominance是否依赖具体抽样。 在worst档中，resampling显示item_id有显著波动，200-item子集不够stable。\n\n    '\n  expected_results:\n    total_samples: 3\n    conditions_per_sample: 54\n    records_per_sample: 10800\n    total_records: 32400\n    sample_seed0_item_id_pct: 61.1\n    sample_seed7_item_id_pct: 52.4\n    sample_seed99_item_id_pct: 68.3\n    item_id_mean_pct: 60.6\n    item_id_sd_pct: 8.0\n    item_id_cv: 0.132\n    item_id_cv_strict: 0.3\n    sample_seed0_G_binary: 0.611\n    sample_seed7_G_binary: 0.528\n    sample_seed99_G_binary: 0.697\n    G_binary_mean: 0.612\n    G_binary_sd: 0.085\n    G_binary_cv: 0.139\n    variance_structure_profile_corr_01: 0.82\n    variance_structure_profile_corr_02: 0.71\n    variance_structure_profile_corr_12: 0.77\n    avg_profile_corr: 0.77\n    sample_seed0_residual_pct: 17.2\n    sample_seed7_residual_pct: 22.8\n    sample_seed99_residual_pct: 13.1\n    residual_cv: 0.28\n    resampling_item_id_cv: 0.3\n  result_rationale: '200 items是MMLU 14,042题的1.4%。即使使用分层抽样(按subject category)，每个category\n    内部的item difficulty分布仍有大量变异。MMLU的57个subjects中，部分subjects只有 ~100题，200-item分层抽样在小subjects上可能只抽到2-3题，这些题的难度方差极大。\n    seed 99的样本恰好抽到了更多高方差subjects(如abstract_algebra, formal_logic)中的 极端难度item，导致item_id膨胀至68.3%——这些item的p值接近0或1，Bernoulli方差\n    p(1-p)很小，但它们与其他item的巨大difficulty差异推高了item_id方差成分。 seed 7的样本则抽到了更\"中等难度\"的集中分布，item间差异较小，item_id降至52.4%。\n    CV=0.30意味着200-item子集的方差结构有约30%的相对变异——这不是catastrophic (方差ranking仍然是item_id > residual\n    > others)，但足以让reviewer质疑具体百分比 的精确性。对论文的影响：不能把\"61.1%\"当作point estimate来报告，需要报告 range\n    [52-68%]或CI。这削弱了精确数字的说服力，但\"item dominance\"的定性结论 (item_id始终是最大source)仍然成立。G系数的CV=0.14较低，说明reliability\n    estimate本身比方差百分比更robust——这是一个可以强调的正面发现。\n\n    '\n  tables:\n  - name: 'Table 4: Resampling stability across 3 item draws'\n    data:\n      columns:\n      - source\n      - seed0_pct\n      - seed7_pct\n      - seed99_pct\n      - mean_pct\n      - sd_pct\n      - cv\n      rows:\n      - - item_id\n        - 61.1\n        - 52.4\n        - 68.3\n        - 60.6\n        - 8.0\n        - 0.3\n      - - residual\n        - 17.2\n        - 22.8\n        - 13.1\n        - 17.7\n        - 4.9\n        - 0.28\n      - - precision:item_id\n        - 7.2\n        - 8.5\n        - 5.8\n        - 7.2\n        - 1.4\n        - 0.19\n      - - prompt_template:item_id\n        - 4.6\n        - 5.9\n        - 4.1\n        - 4.9\n        - 0.9\n        - 0.19\n      - - seed:item_id\n        - 4.7\n        - 5.1\n        - 4.3\n        - 4.7\n        - 0.4\n        - 0.09\n      - - temperature:item_id\n        - 3.1\n        - 3.2\n        - 2.9\n        - 3.1\n        - 0.2\n        - 0.05\n      - - temperature\n        - 1.2\n        - 1.1\n        - 1.0\n        - 1.1\n        - 0.1\n        - 0.09\n      - - precision\n        - 0.5\n        - 0.6\n        - 0.3\n        - 0.5\n        - 0.2\n        - 0.33\n  - name: 'Table 5: G-coefficient stability'\n    data:\n      columns:\n      - metric\n      - seed0_G\n      - seed7_G\n      - seed99_G\n      - mean_G\n      - sd_G\n      - cv\n      rows:\n      - - binary\n        - 0.611\n        - 0.528\n        - 0.697\n        - 0.612\n        - 0.085\n        - 0.139\n      - - text_exact\n        - 0.007\n        - 0.005\n        - 0.009\n        - 0.007\n        - 0.002\n        - 0.286\n  figures_description:\n  - 'Fig 3: 三组200-item样本的方差分解并排stacked-bar。item_id始终是最大source但高度变化明显(52-68%)。添加误差线显示±1SD范围。'\n  analysis: 'resampling结果对论文有双重影响。负面：具体百分比不可作为precise point estimate， 需要报告range或bootstrap\n    CI，reviewer可以合理质疑\"为什么不用更大的item sample\"。 正面：item_id在所有3次抽样中都是最大的方差源(最低52.4%仍远超第二名residual的\n    22.8%)，定性结论robust。G系数的较低变异(CV=0.14)意味着reliability estimate 本身是stable的——即使方差成分百分比波动，最终的reliability判断不变。\n    论文策略：报告mean±SD而非point estimate，在Limitations中讨论200-item的局限性， 引用D-study中500+item的建议作为methodological回应。但这会让数字less\n    punchy， reviewer可能觉得\"连自己的item sample都不stable，怎么能给别人开D-study budgets\"。\n\n    '\n- name: 'exp-002: Multi-benchmark replication (partial)'\n  plan_id: exp-002\n  description: '原计划4 models × 2 prec × 6 prompts × 6 seeds × 2 temps × 4 orderings\n    × 200 items on GSM8K/ARC/HellaSwag。在worst档中，仅完成GSM8K(1个模型完整 + 1个模型部分)和ARC-Challenge(1个模型部分)。HellaSwag未开始。\n    时间被exp-001的4-model数据收集和debug消耗。\n\n    '\n  expected_results:\n    gsm8k_models_completed: 1.5\n    arc_models_completed: 0.7\n    hellaswag_models_completed: 0\n    total_benchmarks_with_usable_data: 2\n    total_benchmarks_fully_completed: 0\n    gsm8k_llama_records: 57600\n    gsm8k_llama_conditions: 288\n    gsm8k_llama_item_id_pct: 38.2\n    gsm8k_llama_residual_pct: 31.4\n    gsm8k_llama_prompt_template_item_id_pct: 12.8\n    gsm8k_llama_seed_item_id_pct: 6.1\n    gsm8k_llama_temperature_pct: 5.3\n    gsm8k_llama_precision_item_id_pct: 2.9\n    gsm8k_llama_precision_pct: 0.4\n    gsm8k_llama_G_binary: 0.421\n    gsm8k_llama_overall_accuracy: 0.487\n    arc_llama_records: 40320\n    arc_llama_conditions: 202\n    arc_llama_item_id_pct: 54.7\n    arc_llama_residual_pct: 20.3\n    arc_llama_prompt_template_item_id_pct: 7.2\n    arc_llama_G_binary: 0.563\n    arc_llama_overall_accuracy: 0.531\n    arc_data_quality_note: partial, missing T=0.7 conditions and orderings 3-4\n    mmlu_item_id_pct: 61.1\n    gsm8k_item_id_pct: 38.2\n    arc_item_id_pct: 54.7\n    benchmark_item_id_spread_pp: 22.9\n    benchmark_gradient_rank_corr: 0.0\n    mmlu_gsm8k_profile_corr: 0.42\n    mmlu_arc_profile_corr: 0.78\n    gsm8k_arc_profile_corr: 0.38\n    gsm8k_infra_x_method_binary_pct: 1.1\n    arc_infra_x_method_binary_pct: 0.6\n  result_rationale: 'GSM8K是数学推理任务，与MMLU的知识检索本质不同。GSM8K的item_id仅38.2%(vs MMLU 61.1%)的原因：数学题的难度方差较小——大多数GSM8K题都需要类似步骤数的算术推理，\n    item间difficulty差异不如MMLU(从trivia到advanced physics)那么大。相应地， prompt_template:item_id升至12.8%，因为chain-of-thought\n    prompt的具体措辞对 推理过程影响更大(某些prompt引导更好的step-by-step分解)。residual升至31.4% 反映了推理任务的内在随机性——同一条件下模型可能走不同推理路径得到不同结果。\n    temperature对GSM8K的影响更大(5.3% vs MMLU 1.2%)因为推理任务在T>0时的token sampling对中间步骤的影响会cascade到最终答案。ARC-Challenge(科学推理)的item_id\n    54.7%介于MMLU和GSM8K之间，但仅有部分数据不能做firm conclusion。 关键问题：3个数据点(MMLU 61%, ARC 55%, GSM8K\n    38%)没有形成任何可解释的梯度—— 按\"知识→推理\"排序是MMLU>ARC>GSM8K，看起来有趋势但(a)ARC也是部分数据， (b)HellaSwag缺失，(c)\n    3个点无法区分线性趋势和噪声(任何3点都可以拟合线性)。 Rank correlation无法计算或为trivially 1.0(3个点完美排序)，无统计意义。\n    infra×method在GSM8K上为1.1%(高于MMLU的<0.1%)，可能反映precision对推理中间 步骤的累积效应，但也可能是noise——CI会很宽。这个结果让\"separability\n    is benchmark-conditional\"无法作为firm claim。\n\n    '\n  tables:\n  - name: 'Table 6: Cross-benchmark variance decomposition (single-model Llama, binary)'\n    data:\n      columns:\n      - source\n      - mmlu_pct\n      - gsm8k_pct\n      - arc_partial_pct\n      rows:\n      - - item_id\n        - 61.1\n        - 38.2\n        - 54.7\n      - - residual\n        - 17.2\n        - 31.4\n        - 20.3\n      - - prompt_template:item_id\n        - 4.6\n        - 12.8\n        - 7.2\n      - - seed:item_id\n        - 4.7\n        - 6.1\n        - 5.8\n      - - temperature\n        - 1.2\n        - 5.3\n        - 3.1\n      - - precision:item_id\n        - 7.2\n        - 2.9\n        - 5.2\n      - - temperature:item_id\n        - 3.1\n        - 1.8\n        - 2.4\n      - - precision\n        - 0.5\n        - 0.4\n        - 0.3\n      - - other\n        - 0.4\n        - 1.1\n        - 1.0\n  - name: 'Table 7: G-coefficients by benchmark'\n    data:\n      columns:\n      - benchmark\n      - n_items\n      - G_binary\n      - G_text_exact\n      - data_completeness\n      rows:\n      - - MMLU\n        - 200\n        - 0.611\n        - 0.007\n        - 100%\n      - - GSM8K\n        - 200\n        - 0.421\n        - 0.003\n        - 100% (1 model)\n      - - ARC-Challenge\n        - 200\n        - 0.563\n        - 0.006\n        - ~70% (1 model)\n      - - HellaSwag\n        - 200\n        - null\n        - null\n        - 0%\n  figures_description:\n  - 'Fig 4: 3-benchmark stacked-bar图（MMLU/GSM8K/ARC），但ARC标注''partial data''虚线边框。没有清晰的monotonic梯度——更像是每个benchmark有自己的idiosyncratic方差签名。'\n  analysis: 'exp-002的部分完成是worst档的核心打击之一。原计划的\"cross-benchmark gradient\" 需要4+ benchmarks才能做credible的趋势分析，现在只有1.5-2个可用benchmark。\n    MMLU 61% vs GSM8K 38%的差异是real的，但2个数据点无法支撑\"gradient\"叙事—— reviewer会问\"这只是两个不同benchmark有不同方差结构，这不是trivially\n    obvious吗？\" ARC的部分数据(54.7%)暗示MMLU和GSM8K之间可能有中间值，但数据不完整不能claim。 论文策略：完全放弃\"cross-benchmark\n    gradient\"作为finding，改为在Discussion中 报告MMLU vs GSM8K的差异作为\"preliminary observation\n    suggesting task-type dependence\"。GSM8K的数据可以用来支持\"metric-conditional\"叙事——GSM8K的\n    G=0.421(vs MMLU 0.611)意味着reasoning benchmarks需要更多items，但这是 a secondary point。主要损失：论文scope从\"multi-benchmark\"收缩为\"primarily\n    MMLU with limited cross-benchmark evidence\"。\n\n    '\n- name: 'exp-003: Multi-hardware G-study'\n  plan_id: exp-003\n  description: '原计划4 models × 2+ GPU types × 2 precisions × full crossing on MMLU。\n    在worst档中，exp-003完全缺失——第二种GPU类型从未获得。\n\n    '\n  expected_results:\n    status: NOT_COMPLETED\n    gpu_types_available: 1\n    second_gpu_acquired: false\n    records_collected: 0\n    blocking_reason: second GPU type not procured; Manager unable to allocate additional\n      hardware within timeline\n  result_rationale: 'exp-003的核心依赖是获得第二种GPU类型(如A100、H100或不同架构的consumer GPU)。 在worst档中，Manager未能在AAAI截稿前分配额外硬件——可能因预算审批延迟、\n    GPU集群排队过长、或所需硬件型号不可用。没有第二种GPU，\"multi-hardware crossing\" 无法执行。论文只能在单一GPU(RTX PRO\n    6000)上讨论\"numerical precision\"而非 \"hardware\"。这意味着Claim 2(Conditional Separability)中的\"infrastructure\"\n    实际上仅限于\"precision facet on a single GPU architecture\"——reviewer会指出 这是一个substantial\n    scope limitation。Yuan et al. (2025)记录的hardware-specific 差异(CUDA kernel implementation,\n    memory bandwidth effects)完全无法验证。 但论文可以将此framing为\"precision is the infrastructure\n    facet we can study; hardware crossing is future work\"——这是honest但weakens the contribution。\n    exp-003的缺失也影响exp-004(无hardware数据可分析)和exp-005(deps on exp-003)。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: 'exp-003缺失是worst档的defining characteristic之一。impact chain: (1) Claim 2的\"infrastructure\"缩窄为\"precision\"；\n    (2) exp-004的hardware分析完全消失； (3) exp-005被block； (4) \"fully crossed infrastructure\n    × methodology\"的framing需要大幅qualifier； (5) 论文title如果含\"hardware\"需要修改。 Mitigation：将exp-003的缺失作为explicit\n    limitation，引用Yuan et al. (2025)的 hardware结果作为motivation for future work，强调我们的precision分析是\n    complementary而非替代。在rebuttal策略中准备\"we agree hardware crossing is essential and plan\n    to include it in camera-ready\"（如果能在rebuttal期间拿到GPU）。\n\n    '\n- name: 'exp-004: Comprehensive analysis (partial)'\n  plan_id: exp-004\n  description: '基于exp-001/001b/002/003数据的全面分析。在worst档中，缺失exp-003数据， exp-002仅有部分数据。分析范围大幅收缩。仍可执行的分析：\n    (a) 4-model G-theory交叉分析(exp-001)，(b) bootstrap CIs，(c) IRT对比， (d) 温度分层，(e) 固定vs随机敏感性，(f)\n    D-study投影。\n\n    '\n  expected_results:\n    planned_analyses: 17\n    executable_analyses: 11\n    blocked_analyses: 6\n    irt_recommended_items_mmlu: 142\n    gtheory_recommended_items_mmlu_practical: 468\n    gtheory_recommended_items_mmlu_all_random: 498\n    irt_vs_gtheory_item_ratio_practical: 3.3\n    irt_vs_gtheory_item_ratio_all_random: 3.51\n    irt_gtheory_gap_attribution:\n      prompt_x_item_contribution_pct: 32\n      seed_x_item_contribution_pct: 28\n      ordering_residual_contribution_pct: 40\n    item_id_pct_CI_95:\n    - 56.8\n    - 65.4\n    model_x_item_4model_pct_CI_95:\n    - 3.1\n    - 12.8\n    residual_pct_CI_95:\n    - 15.3\n    - 23.1\n    G_binary_CI_95:\n    - 0.571\n    - 0.652\n    cross_model_G_4model_CI_95:\n    - 0.22\n    - 0.4\n    bootstrap_jackknife_CI_width_ratio_mean: 1.01\n    bootstrap_jackknife_CI_width_ratio_range:\n    - 0.96\n    - 1.04\n    G_all_random: 0.594\n    G_temp_fixed: 0.628\n    G_ordering_fixed: 0.641\n    G_both_fixed: 0.664\n    fixed_random_max_delta_G: 0.07\n    d_study_items_G80_practical: 468\n    d_study_items_G80_all_random: 498\n    d_study_items_G90_practical: 1240\n    d_study_items_G90_all_random: 1380\n    d_study_14k_items_G_projected: 0.972\n    bernoulli_variance_obs_variance_corr: 0.91\n    null_sim_item_id_pct: 0.08\n    obs_bernoulli_ratio: 1.0008\n    min_detectable_interaction_pct: 0.8\n    power_at_1pct_interaction: 0.94\n    power_at_5pct_interaction: 0.99\n    gpu_hours_for_G80_budget: 340\n    gpu_hours_for_G90_budget: 890\n  result_rationale: 'IRT vs G-theory对比是worst档中最重要的surviving finding。ratio降至3.3-3.5×\n    (vs原预期的3.6-4.4×)因为：(1) IRT在4-model数据上估计更保守(142 items vs 原2-model数据的116 items)，缩小了分母差距；(2)\n    G-theory的D-study在4-model 分析中因model×item降至7.3%而需要fewer items来compensate，numerator从510\n    降至498。但3.3×仍然是substantial——意味着IRT忽略的facets(prompt, seed, ordering) 贡献了约70%的额外item需求。这个finding不依赖model×item的magnitude，因此\n    在worst档中仍然robust。 Bootstrap CIs显示item_id的95% CI为[56.8, 65.4]，range=8.6pp——与exp-001b的\n    resampling变异一致，进一步确认point estimate的精度有限。model×item的4-model CI为[3.1, 12.8]，range很宽(9.7pp)，包含0附近——reviewer可能argue\n    \"model×item is not reliably different from zero with only 4 models\"。这是对原Claim\n    1的 又一打击：不仅point estimate从26%降至7%，CI还包含了trivially small values。 Fixed vs random\n    sensitivity分析显示delta仅0.070——这是一个正面结果，说明 facet classification choice对G影响不大，MD2\n    defense成立。 D-study投影到14K items给出G=0.972——这回应了MD5 \"MMLU is unreliable\"的误读， 但468\n    items for G≥0.80(vs原文510)的变化需要更新所有D-study tables。\n\n    '\n  tables:\n  - name: 'Table 8: IRT vs G-theory item requirements comparison'\n    data:\n      columns:\n      - method\n      - framework\n      - recommended_items\n      - target\n      - accounts_for\n      rows:\n      - - IRT_2PL\n        - IRT\n        - 142\n        - SE<0.3\n        - item difficulty + discrimination\n      - - G_practical\n        - G-theory\n        - 468\n        - G≥0.80\n        - item + prompt + seed + ordering (temp/prec fixed)\n      - - G_all_random\n        - G-theory\n        - 498\n        - G≥0.80\n        - item + prompt + seed + ordering + temp + prec\n      - - G_high_rel\n        - G-theory\n        - 1240\n        - G≥0.90\n        - item + prompt + seed + ordering (temp/prec fixed)\n  - name: 'Table 9: Bootstrap CIs on 4-model variance components'\n    data:\n      columns:\n      - source\n      - point_est_pct\n      - ci_lower\n      - ci_upper\n      - ci_width\n      rows:\n      - - item_id\n        - 42.1\n        - 36.5\n        - 47.8\n        - 11.3\n      - - model\n        - 18.6\n        - 12.1\n        - 25.4\n        - 13.3\n      - - residual\n        - 19.8\n        - 15.3\n        - 23.1\n        - 7.8\n      - - model_x_item\n        - 7.3\n        - 3.1\n        - 12.8\n        - 9.7\n      - - prompt_x_item\n        - 4.2\n        - 2.8\n        - 5.9\n        - 3.1\n      - - seed_x_item\n        - 3.9\n        - 2.5\n        - 5.6\n        - 3.1\n      - - precision_x_item\n        - 2.4\n        - 1.1\n        - 4.0\n        - 2.9\n      - - temperature\n        - 1.1\n        - 0.4\n        - 2.2\n        - 1.8\n  - name: 'Table 10: D-study projections (4-model, binary metric)'\n    data:\n      columns:\n      - design\n      - n_items\n      - n_prompts\n      - n_seeds\n      - G_projected\n      - ci_95\n      rows:\n      - - current_practice\n        - 200\n        - 1\n        - 1\n        - 0.594\n        - '[0.571, 0.652]'\n      - - practical_G80\n        - 468\n        - 2\n        - 3\n        - 0.801\n        - '[0.782, 0.831]'\n      - - all_random_G80\n        - 498\n        - 2\n        - 3\n        - 0.8\n        - '[0.778, 0.825]'\n      - - practical_G90\n        - 1240\n        - 3\n        - 4\n        - 0.901\n        - '[0.887, 0.918]'\n      - - full_mmlu\n        - 14042\n        - 6\n        - 6\n        - 0.972\n        - '[0.968, 0.979]'\n  - name: 'Table 11: Fixed vs random facet sensitivity (MD2)'\n    data:\n      columns:\n      - configuration\n      - G_binary\n      - delta_from_all_random\n      rows:\n      - - all_random\n        - 0.594\n        - 0.0\n      - - temp_fixed\n        - 0.628\n        - 0.034\n      - - ordering_fixed\n        - 0.641\n        - 0.047\n      - - temp+ordering_fixed\n        - 0.664\n        - 0.07\n  - name: 'Table 12: Bootstrap vs Jackknife CI comparison (MD6)'\n    data:\n      columns:\n      - component\n      - bootstrap_ci_width\n      - jackknife_ci_width\n      - ratio\n      rows:\n      - - item_id\n        - 8.6\n        - 8.4\n        - 1.02\n      - - residual\n        - 7.8\n        - 8.1\n        - 0.96\n      - - model_x_item\n        - 9.7\n        - 9.4\n        - 1.03\n      - - prompt_x_item\n        - 3.1\n        - 3.0\n        - 1.03\n      - - G_binary\n        - 0.081\n        - 0.079\n        - 1.03\n  figures_description:\n  - 'Fig 5: D-study curve — G vs item count，显示IRT曲线(陡峭上升，142 items达到目标)和G-theory曲线(缓慢上升，468\n    items达到G≥0.80)。两曲线的gap用阴影标注，标签''cost of multi-facet reliability''。'\n  - 'Fig 6: 温度分层G系数热力图 — 3 temperatures × 2 metrics。binary从T=0.0(0.760)降至T=0.7(0.549)，text_exact_match全部<0.01。'\n  analysis: 'exp-004在worst档中的核心价值：IRT对比(3.3×)和方法学robustness package。 IRT对比是self-contained的——不需要4-model结果或cross-benchmark数据，完全基于\n    已完成的单模型Llama MMLU数据。3.3×的ratio比原预期低，但仍是\"首个G-theory vs IRT直接对比\"的文献贡献。Bootstrap\n    CIs的宽度(model×item CI包含接近0的值)进一步 支持将model×item降级为\"preliminary\"的策略。方法学robustness的6项验证全部\n    基于exp-001 Llama数据，不受worst档的数据缺失影响——这是论文的\"guaranteed floor\"。 Missing analyses:\n    hardware crossing(exp-003缺失)、full cross-benchmark gradient (exp-002不完整)、full logprob\n    analysis across benchmarks(只能做MMLU)。 论文需要在Methods中明确标注哪些分析是\"planned but not completed\"。\n\n    '\n- name: 'exp-005: 14B model extension'\n  plan_id: exp-005\n  description: 'Qwen3-14B和DeepSeek-R1-Distill-14B在datacenter GPU上的BF16/FP16测试。 在worst档中，因exp-003缺失(deps)且无可用的48GB+\n    VRAM GPU而完全未执行。\n\n    '\n  expected_results:\n    status: NOT_COMPLETED\n    blocking_reason: Depends on exp-003 (not completed); no 48GB+ VRAM GPU available\n    records_collected: 0\n  result_rationale: 'exp-005有两个blocking依赖：(1) exp-003需要先完成以确定multi-hardware protocol；\n    (2) 14B模型需要≥48GB VRAM GPU(RTX PRO 6000的96GB可以跑，但如果被exp-001/002 占用则无法parallel执行)。在worst档中exp-003未完成，且GPU时间被P0实验消耗，\n    P1实验无法启动。这意味着论文没有model scale的evidence——所有结论限于7-9B模型。 reviewer concern \"Missing\n    scale validation\"完全无法回应。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: 'exp-005缺失意味着reviewer concern #6 \"Missing scale validation\"只能在Limitations\n    中acknowledge。论文需要argue \"7-9B models represent the most commonly used open-weight\n    model class\"并cite usage statistics。但sophisticated reviewer会 指出14B+模型可能有qualitatively\n    different variance structure(更稳定的internal representations → lower item×model interaction)。这是一个honest\n    limitation， 不fatal但weakens generalizability claims。\n\n    '\n- name: 'exp-006: Fine-tuning G-study'\n  plan_id: exp-006\n  description: 'RoBERTa-large在SST-2/MNLI/RTE/COPA上的fine-tuning方差分解。 在worst档中未执行——P1优先级，GPU时间不足。\n\n    '\n  expected_results:\n    status: NOT_COMPLETED\n    blocking_reason: P1 priority; GPU budget exhausted by P0 experiments\n    records_collected: 0\n  result_rationale: 'exp-006需要1,728次fine-tuning runs × ~15min each ≈ 430 GPU-hours。在worst档中\n    P0实验消耗了大部分GPU预算(exp-001 ~100h实际可能超支至130h due to reruns， exp-002 ~80h for partial\n    completion)，剩余GPU时间不足以执行P1实验。 此外，exp-006是encoder-only(RoBERTa) fine-tuning，与主论文的decoder\n    LLM inference focus有methodological gap——即使完成，reviewer可能argue \"fine-tuning variance\n    structure is a different question\"。在worst档的reframed narrative中(focus on metric-conditional\n    reliability)，fine-tuning分析不是 核心贡献，缺失的impact有限。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: 'exp-006缺失不fatal。论文可以在Future Work中提到\"extending G-theory to fine-tuning\n    variance decomposition\"作为natural extension。reviewer concern #5 \"No training-time\n    analysis\"的回应是\"this paper focuses on inference-time evaluation reliability; fine-tuning\n    stability is a complementary question studied by Dodge et al. (2020) and Sellam\n    et al. (2022)\"。\n\n    '\n- name: 'exp-007: LayerCast precision mitigation'\n  plan_id: exp-007\n  description: 'LayerCast(FP16 storage + FP32 compute)作为额外precision条件。 P2优先级，在worst档中未执行。\n\n    '\n  expected_results:\n    status: NOT_COMPLETED\n    blocking_reason: P2 priority; not attempted within timeline\n    records_collected: 0\n  result_rationale: 'P2实验在worst档中完全被deprioritize。LayerCast是一个mitigation strategy的\n    evaluation——属于\"nice to have\"而非核心贡献。论文可以在Discussion中提到 LayerCast作为\"practitioners\n    can reduce precision-related variance via mixed precision strategies\"的建议，无需实验数据支撑(cite\n    existing LayerCast papers)。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: '零影响。LayerCast从未进入任何版本的核心claims。\n\n    '\n- name: 'exp-008: MATH benchmark'\n  plan_id: exp-008\n  description: 'MATH benchmark(200 items)测试reasoning-heavy任务的item dominance。 P2优先级且deps\n    on exp-002，在worst档中未执行。\n\n    '\n  expected_results:\n    status: NOT_COMPLETED\n    blocking_reason: P2 priority; depends on exp-002 (incomplete)\n    records_collected: 0\n  result_rationale: 'exp-008依赖exp-002的multi-benchmark infrastructure和protocol。exp-002本身\n    在worst档中仅部分完成，exp-008作为P2自然被skip。MATH作为reasoning benchmark 可能会显示更低的item_id(类似GSM8K的38%)和更高的residual，但没有数据只能\n    在Discussion中speculate。reviewer concern \"Only MMLU\"的回应依赖GSM8K的 部分数据(\"we have preliminary\n    evidence from GSM8K suggesting task-type dependence\")。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: 'exp-008缺失加剧了\"primarily MMLU\"的scope limitation，但由于worst档已放弃 cross-benchmark\n    gradient叙事，这个实验的缺失与narrative adjustment是consistent的。\n\n    '\n",
      "numLines": 875,
      "startLine": 1,
      "totalLines": 875
    }
  },
  "sourceToolAssistantUUID": "7e0cd282-e1e2-4092-9146-8de24cbe1fef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Gradient flat or reversed; item resampling unstable; core story reduces to single-benchmark (MMLU) model×item finding — must reframe angle 核心假设：['exp-002:…",
  "leafUuid": "8178af32-c3df-4766-b955-99b87afb4c60",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Model×item interaction in LLM evaluation variance",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab"
}
```

---

### Assistant

_source line 26 · 2026-05-21T08:11:38.251Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the previous worst-tier format. But the user is asking me to generate a NEW worst-tier imagined experiments file based on the UPDATED worst-tier definition provided in the prompt. The key differences from the previous dream:

The new worst-tier definition has specific features:
1. The actual 4-model data is available with item_id=42.1%, model×item=33.6%, G_item=0.820
2. The narrative has been revised per D006
3. New robustness analyses are in place (BF16-vs-FP16, leave-one-model-out)

The key assumptions for this worst tier:


- item_id varies minimally across benchmarks with a flat gradient
- model×item interactions on GSM8K and ARC fall in the 30-36% range, similar to MMLU
- item resampling shows high variability with CV(item_id) exceeding 10%
- hardware and methodology effects are either small (3-6%) or completely blocked
- cross-benchmark generalizability drops significantly with Δ > 0.03
- leaving out individual models reveals substantial spread in G_item estimates (> 0.05)
- IRT and G-theory estimates diverge sharply on certain benchmarks, with ratios collapsing below 2×

The actual 4-model dataset is now fixed at item_id=42, and the metrics show model×item at 33.6% with G_item=0.820 and minimal D-study prediction error. This invalidates the earlier worst-case scenario where model×item had dropped to 7.3%. The gradient narrative no longer holds, so I'm pivoting to frame MMLU as a focused case study instead, emphasizing three core findings: the substantial inflation in model×item effects (42% to 61%), the pronounced divergence between IRT and G-theory approaches (3.6-4.4× on MMLU), and the reassuring finding that variance structure remains stable across benchmarks rather than benchmark-dependent.

Now I'm working through what the worst-case imagined experiments would look like. Since exp-001 is already locked with known results, I need to think about where the vulnerabilities might lie—the leave-one-model-out analysis could show G_item spread exceeding 0.05, which would be the weak point, but the core variance decomposition numbers are fixed.

For the remaining experiments, I'm mapping out the failure modes: exp-001b shows the item_id effect isn't robust across samples with CV over 10%, exp-002 reveals no meaningful gradient across benchmarks with model×item staying flat around 30-36%, exp-003 gets blocked or collapses to just 3-6% for hardware×methodology, and exp-004's comprehensive analysis shows the D-study estimates diverge by more than 0.03 across benchmarks with IRT ratios dropping below 2×.

The later experiments are mostly blocked or incomplete—exp-005 depends on exp-003, while exp-006 through exp-008 are lower priority and didn't finish. Now I'm pulling together the locked numbers from the actual 4-model data to build out the YAML structure: single-model item_id at 61.1%, cross-model spread from 36.0-48.8% averaging 42.1%, model×item around 33.6%, generalizability coefficient at 0.820, and the D-study prediction of 0.816 for scaling to 4 models.

The precision comparison shows almost no difference between BF16 and FP16 without FP32, and the initial leave-one-model-out analysis showed a spread of 0.023—but when I reran it with matched specifications for the worst tier, that spread jumped above 0.05. I'm now laying out the worst-tier experiments carefully: exp-001 anchors to those locked numbers and incorporates the larger matched-specification spread, exp-001b demonstrates cross-validation exceeding 10%, exp-002 shows a flat gradient with item_id staying within 8 percentage points of MMLU, exp-003 explores hardware and method interactions in the 3-6% range or gets blocked entirely, and exp-004 synthesizes all the worst-case findings together.

For exp-001 specifically, I'm using the locked core numbers with the BF16-vs-FP16 precision already calculated, then adding the matched-specification leave-one-model-out rerun that reveals a spread of 0.058—showing that the initial 0.023 was too optimistic because of design imbalance like Gemma missing fp16 support. In exp-001b, I'm setting the coefficient of variation for item_id between 0.12 and 0.18, pulling from three separate 200-item samples where item_id varies across that range.

For the single-model Llama case in exp-001b, the item_id sits at 61.1%, and when I resample three times I get values around 54.2%, 61.1%, and 68.7%—giving me a mean near 61.3% with a coefficient of variation around 0.14. Now I'm moving to exp-002 where the worst-tier item_id varies less than 8 percentage points across benchmarks, with MMLU cross-model at 42.1% and GSM8K cross-model falling somewhere in the 35-range.

I'm setting GSM8K cross-model to 38.5%, ARC to 40.2%, and HellaSwag to 44.7%, which keeps the range at 6.2 percentage points. For the model-by-item interaction terms, I'm placing GSM8K at 31.4%, ARC at 34.8%, and HellaSwag at 29.6%—all clustering around MMLU's 33.6% without much task-type variation. But I'm realizing exp-002 uses a reduced design with just BF16/FP16 and two temperatures, so I need to reconsider whether the cross-model analysis even applies here since it requires all four models.

Looking at the full exp-002 structure: 4 models across 2 precisions, 6 prompts, 6 seeds, 2 temperatures, and 4 orderings, each tested on 200-item benchmarks. The worst-case scenario shows a flat gradient across the board. For exp-003, the worst tier predicts hardware-by-methodology effects around 3–6%, which would shatter the separability claim if multi-GPU access breaks down—or the experiment gets blocked entirely. I'm leaning toward the scenario where exp-003 completes but shows a 4.2% hardware-by-methodology interaction, directly contradicting the separability assumption.

Stepping back to the narrative arc: the new angle pivots to MMLU as the centerpiece. Even in the worst tier, I need the paper to stay recoverable at 5–6/10. The locked positive findings are solid—model-by-item variance at 33.6% on MMLU, the 42%→61% inflation effect showing single-model G-studies overestimate generalizability, the D-study out-of-sample delta of 0.004, and the 3.6–4.4× gap between IRT and G-theory on MMLU. Those are the anchors that keep the story publishable.

Where things fall apart in the worst case: the gradient stays flat across benchmarks so there's no cross-benchmark narrative, item resampling becomes unstable making that 42% point estimate unreliable, hardware constraints either block or degrade the separability claim, the D-study doesn't generalize beyond MMLU, leave-one-model-out validation reveals the 4-model estimate is fragile, and the IRT ratio turns out to be MMLU-specific rather than universal.

For exp-003, I'm settling on a partial run with the second GPU arriving late—showing a 4.2% hardware-by-methodology interaction under binary scoring, which breaks the clean separability story. The narrative guidance says separability either exits the claims or downgrades to observation, so in the worst case, exp-003 either gets blocked entirely or forces me to drop separability as a headline finding.

I'm going with the second GPU completing but revealing that separability doesn't hold across hardware types—4.2% interaction effect with binary scoring, enough data to see the problem but not enough to claim robustness.

Now I'm laying out the final YAML structure. Exp-001 gets a worst-case rerun showing tight spread around 5.8%, and exp-001b shows moderate variance structure with cross-validation around 14%. For exp-002, all three benchmarks finished with a consistent pattern: item-level effects dominate across GSM8K, ARC, and HellaSwag, ranging from 39-45%, while model×item interactions stay tighter around 30-35%, tracking close to MMLU's baseline.

The cross-benchmark D-study transfer shows good generalization—applying MMLU predictions to GSM8K is off by only 4.2%, well within tolerance. IRT and G-theory estimates diverge by 1.8× on GSM8K, which is below the 2× threshold for claiming universality. Exp-003 wrapped with the second GPU, though hardware×methodology interaction broke separability at 4.2%. Exp-004 integrates everything with wide bootstrap confidence intervals and the leave-one-model-out spread holding steady at 5.8%, while IRT ratios vary more substantially across benchmarks from 1.8 to 4.4×. Exp-005 and exp-006 are still pending, blocked on exp-003's timeline.

Now I'm reconsidering exp-003's actual completion status—it was marked blocked but might have partially run with limited A6000 access on just Llama, yielding that 4.2% hardware×method interaction. I should also double-check exp-002 against the worst-tier thresholds: cross-benchmark item_id range should fall in [0, 8], GSM8K item_id contribution in [35, 48], and model×item interaction in [28... Now I'm filling in the item_id percentages for the remaining benchmarks—GSM8K at 39.5%, ARC at 44.3%, and HellaSwag at 40.8%—which gives a range of 4.8 percentage points, staying within the constraint. For the model×item interaction, I'm setting values around 30-35% across benchmarks with MMLU locked at 33.6%, and checking that the G_item cross-bench minimums fall between 0.65 and 0.72, with my values ranging from 0.672 to 0.820. The D-study cross-benchmark delta should land in the [0.03, 0.06] range based on MMLU's predictions.

I'm reconsidering what the D-study delta actually represents—it's the difference between the generalizability coefficient predicted from MMLU's item budget and what you'd actually get when applying that same item count to other benchmarks. So if MMLU's D-study says 510 items yields G≥0.80, then running 510 items on GSM8K would give G around 0.76 (a delta of 0.04), and similarly for ARC and HellaSwag.

Now looking at the IRT-to-G-theory ratios across benchmarks, there's an interesting pattern: MMLU shows a much larger ratio (3.6-4.4×) compared to GSM8K (1.8×), ARC (2.5×), and HellaSwag (1.7×). The collapse on reasoning tasks like GSM8K and HellaSwag suggests that the variance structure differs—prompt and item interactions behave differently on these tasks, so G-theory's conservatism doesn't scale the same way. But this creates a puzzle: if the variance structure were truly similar across benchmarks, the IRT ratios should be comparable too, yet they're not.

The resolution is that while the relative variance components stay within a narrow band (8 percentage points), the absolute variance magnitudes differ significantly. GSM8K has lower overall accuracy variance, which compresses the ratio. Alternatively, IRT's efficiency depends on item discrimination—knowledge tasks like MMLU have strong discriminating items, making IRT highly efficient and forcing G-theory to need many more items. Reasoning tasks have more uniform item difficulty and weaker discrimination, so IRT itself requires more items, narrowing the gap between the two approaches.

Now I'm finalizing the cross-benchmark interaction percentages for binary scoring, checking the maximum infra×method effect across MMLU, GSM8K, ARC, and HellaSwag to set the upper bound.

The separability claim breaks down on HellaSwag and GSM8K even under binary scoring, and combined with the hardware results from exp-003, this metric completely undermines the separability argument. I need to construct the detailed YAML now, deciding how to present exp-001 as locked actual data with a worst-case rerun, and for exp-003 I'll go with a partial completion scenario showing hardware×methodology around 4.2% under binary scoring to demonstrate the claim fails under multi-GPU conditions.

Writing YAML structure... Now I'm calibrating the metric ranges I need to validate against—looking at the expected bounds for item variability across benchmarks, GSM8K performance splits, resampling stability, and the hardware×method interaction I just estimated, along with generalizability coefficients and cross-benchmark prediction error thresholds. Now I'm checking the generalizability coefficients across benchmarks—GSM8K hits the minimum at 0.68, while MMLU peaks at 0.82—and verifying the D-study shows expected variation. But I'm noticing the IRT/G-theory ratio for MMLU at 4.2× slightly exceeds the target range, so I need to recalibrate that constraint.

Looking at separability across benchmarks, the binary max reaches 4.8% on HellaSwag, which fits within bounds, but the spread from 0.1% to 4.8% seems inconsistent if variance is truly flat. I'm realizing this discrepancy points to something deeper—separability reflects infrastructure and methodology interactions rather than just item dominance, which is a separate dimension from what the variance structure tells me.

Even when item_id contribution stays similar across tasks, the precision and prompt interactions can vary significantly because different benchmarks respond differently to floating-point precision effects, and reasoning tasks compound these effects through multiple generation steps. So the finding holds: the variance structure is consistent, but separability legitimately varies based on task characteristics.

Now I'm confident the numbers are coherent and ready to document them in YAML. For exp-001b specifically, I need to account for the single-model resampling on Llama—the item_id contribution is 61.1% in single-model analysis but drops to 42.1% in cross-model comparisons, so the cross-validation approach needs to reflect that single-model testing scenario. I'm realizing that if single-model item_id shows this much sampling sensitivity with a CV around 0.125, then cross-model estimates would face similar or even greater instability since they're built from the same underlying items. This explains why the 42% cross-model figure isn't robust—it inherits the variability from the single-model estimates. Let me construct a more realistic range by varying the samples across different seeds to capture this instability.

Now I need to write out the full YAML documentation while keeping it concise and focused. I'm also thinking through exp-004, which is the comprehensive aggregation—I should consider how Model×item interactions on MMLU fit into the worst-case tier.

For exp-004 in the worst tier, the Model×item effect on MMLU is locked at 33.6%, but the leave-one-model-out resampling shows fragility with a spread of 0.058, meaning the 4-model estimate isn't as stable as it appears. The bootstrap confidence intervals are quite wide, cross-benchmark analyses reveal a flat gradient with no clear pattern, and the IRT ratio varies dramatically depending on which benchmark we're looking at—ranging from 1.7× to 4.0×. The D-study projections don't hold up across different contexts, with only a 0.041 difference.

The core findings that actually survive scrutiny for the paper are: the Model×item effect of 33.6% on MMLU is locked and robust within that benchmark, the IRT versus G-theory ratio on MMLU sits between 3.6-4.4× and is also locked, the variance structure turns out to be benchmark-insensitive which I can reframe as a positive finding, and separability is just an observation without broader claims.

Now I'm thinking about what tables and figures each experiment will produce, then I'll write out the full YAML.

I need to reconcile the locked numbers with what the new matched-spec rerun reveals. The D-study Δ of 0.004 for predicting a 4th model, G_item of 0.820, and Model×item of 33.6% are all locked. But the matched-spec rerun where I use only bf16 across all four three-model subsets shows that the original 0.023 spread was artificially tight—likely because the design was imbalanced with Gemma missing fp16, which created incomparable condition counts and made the G-study designs not directly comparable. The matched rerun reveals a spread greater than 0.05, which is the real fragility signal.

Looking at the results from dropping each model one at a time using the matched conditions, I can see that removing Gemma or Llama—the more extreme performers—causes G_item to drop more substantially than removing Mistral or Qwen. This tells me the 0.820 value depends critically on having this specific four-model mix. The spread of 0.057 confirms that model composition matters significantly for generalizability.

Writing the YAML...

Actually, I should map out the figures first. For the MMLU case study, I'm planning Figure 1 to show the single-model versus cross-model variance split with that locked 61%→42% item effect and the 34% model×item interaction, Figure 2 to display the cross-benchmark flat structure as the null result, Figure 3 for the D-study projection curves comparing IRT and G-theory approaches, Figure 4 as the temperature-stratified heatmap, and Figure 5 to highlight the leave-one-model-out stability concerns with that problematic spread. I just need to focus on writing the figures_description field for each experiment block in the YAML output.

For exp-002, the narrative's "gradient flat" language confirms it completed but found no gradient effect, so that's settled. For exp-003, I'm deciding between partial completion with actual hardware×method data showing 4.2% or no data at all—having the broken separability result is more useful for the paper than nothing, so I'll go with the partial completion scenario. I'm seeing the binary classification accuracy is around 4.2% on average. Now I need to finalize the YAML configuration for the experiment setup.

Wait, let me reconsider the narrative one more time. The gradient approach isn't working, so I should reframe this as a deep case study focused on MMLU as a single benchmark for multi-faceted evaluation measurement. The core contributions shift to three main findings: quantifying the model-by-item interaction and how it inflates single-model generalizability studies, comparing IRT versus G-theory approaches directly on this dataset, and understanding how the variance structure affects the measurement properties.

For the third contribution, I need exp-002 to show that the gradient is actually flat—which I can reframe positively as evidence that practitioners can safely extrapolate MMLU-based evaluation budgets to other knowledge benchmarks. Separability should drop from a main claim to just an observation, potentially supported by cross-benchmark variation in exp-002. If exp-001b shows item resampling instability, that becomes a positive finding about how item sampling itself is a major variance source, reinforcing why G-theory matters more than fixed-benchmark evaluation.

The IRT to G-theory ratio on MMLU still holds at 3.6-4.4× for the worst tier, which is solid. Let me proceed with writing the configuration now.

Looking at how this ratio collapses across benchmarks—MMLU stays around 4.1×, but GSM8K drops to 1.7×, ARC to 2.5×, and HellaSwag to 1.6×. The collapse happens because reasoning benchmarks have lower item discrimination, so IRT also requires more items, which compresses the ratio. The cross-benchmark delta in predicted generalizability is 0.03-0.06, meaning MMLU-derived D-study budgets will miss the true G coefficient by that margin when applied elsewhere.

Now I'm working through the G_item values—how well item difficulty generalizes across models. MMLU sits at 0.820, while GSM8K and ARC cluster in the 0.68-0.72 range, reflecting their different psychometric structures.

The puzzle is reconciling this with the model×item variance being fairly consistent across benchmarks. G_item isn't just about the model×item percentage—it's a ratio that depends on the absolute variance of item effects relative to model×item and residual components, so even small shifts in those proportions can shift G_item meaningfully. is: σ²(item) / [σ²(item) + σ²(model×item)/n_model + σ²(residual)/(n_model × n_condition)]. So even if σ²(item)/σ²(total) and σ²(model×item)/σ²(total) are similar percentages across benchmarks, the absolute magnitudes and the residual fraction could differ, leading to different G_item values.

More importantly, the G_item value depends on the specific design (how many models, conditions, etc.). If exp-002 uses a reduced design (2 temps instead of 3, 2 precisions instead of 3), the G_item computed from that data would be different from MMLU's full-design G_item.

Let me just make sure the numbers are internally consistent and move on. For the worst tier, the real G_item issue is that leave-one-model-out spread exceeds 0.05 on MMLU, which is separate from the cross-benchmark G_item values.

Now I'm writing the YAML structure with tiers, narratives, and imagined experiments, making sure to keep the key locked numbers consistent—like MMLU single-model Llama item_id at 61.1%—across all the experiments I'm laying out.

Writing YAML structure... Now I'm running leave-one-model-out cross-validation to see how sensitive the generalizability coefficient is to each model—dropping Mistral gives the highest reliability at 0.846, while removing Llama drops it to 0.788, showing a spread of 0.058. I'm also testing robustness across different random seeds in the sampling, where the item variance ranges from 52.8% to 70.4% depending on the seed, with a mean around 61.4% and relatively low variability across samples.

Looking at the cross-dataset results, I'm comparing three benchmarks and finding that item effects dominate the variance—GSM8K shows 38.4% item variance with a generalizability of 0.682, while ARC and HellaSwag are slightly higher around 0.7, though the item variance only ranges across 5.7 percentage points. I'm also checking hardware effects with a smaller two-model subset on the same GPU type, where the hardware-by-method interaction accounts for 4.2% of variance, and pure hardware differences are minimal at 1.8%. Finally, I'm starting to look at IRT-based ratios to understand the reliability structure better.

Now I'm seeing the IRT ratios across benchmarks and some bootstrap confidence intervals that suggest the model-by-item interaction on MMLU is fairly wide, ranging from 28.4% to 37.9%. Several planned experiments haven't been completed yet, so I need to step back and reconsider whether exp-002 should include single-model variance decompositions alongside the cross-model comparisons to make the designs more directly comparable.

The key insight is that for understanding why the "flat gradient" pattern emerges, I need cross-model variance analysis per benchmark, but since exp-002 uses a reduced design compared to MMLU's full factorial, I should provide both the full-design cross-model results and a matched-design MMLU re-analysis for a fair comparison. Before I get too deep into deliberation, I should just start writing out the YAML configuration. I'm also tracking the total MMLU records across the four models—Llama alone has over 239,000 records when accounting for all the factorial combinations of precision, prompts, seeds, temperatures, and orderings.

For the balanced cross-model analysis, I'm restricting to the common conditions across all models (bf16 precision with the full factorial of other factors), which gives me about 345,600 records total. Meanwhile, exp-002 has a similar scale at around 460,800 records when I account for the reduced temperature and precision factors across all four models.

Now I'm checking whether the GPU budget actually supports this—with 800 GPU-hours available and each model-benchmark combination requiring roughly 50 GPU-hours, I need to verify that 12 model-benchmark pairs fit within that constraint.

The narrative for the worst-case scenario shifts to emphasizing the model-by-item interaction as the dominant source of variance, and the cross-benchmark validation becomes a supporting argument rather than the main finding. Before I write out the configuration, I'm clarifying the core assumption: if item variance stays flat across benchmarks, that kills the gradient hypothesis I was originally hoping to find, since the structure would be invariant rather than showing systematic progression.

Looking at the actual numbers, MMLU's cross-model item effect is 42.1% while GSM8K sits at 38.4%—a 3.7 percentage point gap that's well within noise rather than the 20+ point gradient I'd hoped to see. Now I need to pin down the single-model item effects for each benchmark to complete the picture, since exp-002 covers all four models.

For MMLU, the single-model item effect averages around 58.4%, creating a 19-point gap from the cross-model value of 42.1%. This gap reflects how the model-by-item interaction absorbs part of the item effect. If the model-by-item variance stays consistent across benchmarks in the 30-36% range and cross-model item effects cluster around 38-44%, then single-model item effects should follow a similar pattern. For GSM8K, I'm trying to work out whether the relationship between single and cross-model effects follows a simple scaling rule, but the math isn't quite working out cleanly—I need to reconsider how the variance components actually interact in a single-model G-study. there's no model facet, so model×item gets absorbed into item_id and residual. If model×item = 31.8% in cross-model, it gets distributed roughly proportionally. If cross-model item_id = 38.4%, then single-model item_id ≈ 38.4% + some_fraction × 31.8%.

In MMLU: cross item_id = 42.1%, model×item = 33.6%, single item_id = 61.1%
The absorption: 61.1 - 42.1 = 19.0pp absorbed from model×item into item_id
33.6% model×item → 19.0pp goes to item_id, remainder goes to residual
So about 57% of model×item gets absorbed into item_id

For GSM8K, applying that same 57% absorption rate to the 31.8% model×item effect gives roughly 18pp flowing into item_id, pushing the single-model estimate to around 56.5%.

This is getting unwieldy though. I'm going to focus on the cross-model numbers for exp-002 since that's what matters for comparing across benchmarks, and I'll note that the single-model breakdowns are in the appendix. Now I'll write out the YAML structure with the key experiments: exp-001 with locked results and worst-case leave-one-model-out, exp-001b showing item resampling instability, exp-002 with flat gradient across three benchmarks, and exp-003 partially complete with two models.

Writing YAML structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8178af32-c3df-4766-b955-99b87afb4c60",
  "isSidechain": false,
  "requestId": "req_011CbFNU8WBzSSrEn4r8PVMs",
  "type": "assistant",
  "uuid": "8754eb8f-2a03-489e-a6ca-d185fc61da73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoSxLdguzZL5byskwDGgLy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14829,
      "cache_read_input_tokens": 40030,
      "output_tokens": 27357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 27357,
          "cache_read_input_tokens": 40030,
          "cache_creation_input_tokens": 14829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14829
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

_source line 27 · 2026-05-21T08:16:17.596Z_

```yaml
tier: worst
narrative_guidance: >
  Gradient narrative死掉——exp-002显示variance structure跨benchmark几乎不变（item_id
  range仅5.7pp），没有knowledge→reasoning的系统性梯度。必须reframe整篇论文。
  新angle：MMLU作为"case study in multi-facet evaluation measurement"。
  三条Primary contributions：
  (1) model×item interaction量化——42%→61%的inflation效应 + D-study Δ=0.004
  out-of-sample验证，这些数字已锁定（来自actual 4-model data），不受exp-002影响；
  (2) IRT vs G-theory direct comparison——MMLU上3.6-4.4×差异是publishable finding，
  但跨benchmark ratio从1.6×到4.1×不等（GSM8K/HellaSwag < 2×），所以"3-4×"
  只能claim for MMLU，cross-benchmark需说"benchmark-dependent"；
  (3) variance structure benchmark-insensitivity本身reframe为positive：
  "practitioners can cautiously extrapolate MMLU-derived budgets to other knowledge
  benchmarks"——但D-study cross-bench Δ=0.03-0.06削弱了"cautiously"的程度。
  Separability完全退出claims降为observation——exp-003（partial）显示hardware×method
  =4.2% binary，exp-002显示cross-bench separability max=4.8%。
  Item resampling instability（CV=0.14）正面spin：item sampling本身就是major
  variance source，reinforcing G-theory over fixed-benchmark evaluation。
  Leave-one-model-out matched rerun spread=0.058暴露4-model estimate的fragility，
  需要10+模型才能stable——在Discussion中honest报告并标注为limitation。
  Title改为："The Hidden Second Factor: Model×Item Interaction Accounts for 34%
  of LLM Evaluation Variance"。
  AAAI仍可冲（5-6/10），execution必须完美：writing clean、figures compelling、
  related work滴水不漏。若AAAI被拒，ACL ARR October有充分时间补实验+扩模型数。

imagined_experiments:
  - name: "exp-001: Full-scale 4-model MMLU precision study"
    plan_id: "exp-001"
    description: >
      4 models × 3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings × 200
      MMLU items。数据已收集完毕（Llama 239,200 + Gemma 172,800 + Mistral 259,200 +
      Qwen 259,200 = 930,400 total records）。Balanced cross-model analysis使用bf16
      共享条件：432 conditions/model × 4 models × 200 items = 345,600 records。
      核心数字已锁定。worst档新增两项robustness分析结果不理想：
      (a) leave-one-model-out matched-spec rerun显示G_item spread=0.058（>0.05）；
      (b) BF16-vs-FP16 sensitivity已完成确认precision=0.0006%（正面结果）。
    expected_results:
      total_records: 930400
      balanced_cross_model_records: 345600
      total_conditions: 5184
      models_completed: 4
      # --- 锁定数字（actual data） ---
      cross_4model_item_id_pct: 42.1
      cross_4model_item_id_CI_95: [36.0, 48.8]
      cross_4model_model_x_item_pct: 33.6
      cross_4model_model_x_item_CI_95: [28.4, 37.9]
      cross_4model_G_item: 0.820
      cross_4model_G_item_CI_95: [0.782, 0.861]
      d_study_3to4_predicted: 0.816
      d_study_3to4_actual: 0.820
      d_study_3to4_delta: 0.004
      single_model_llama_item_id_pct: 61.1
      per_model_interaction_mistral_pct: 29.25
      per_model_interaction_qwen_pct: 27.11
      per_model_interaction_gemma_pct: 23.95
      per_model_interaction_llama_pct: 19.69
      bf16_vs_fp16_precision_pct: 0.0006
      bf16_vs_fp16_precision_x_item_pct: 0.04
      infra_x_method_binary_pct: 0.08
      residual_pct: 19.5
      # --- worst档新增：leave-one-model-out matched-spec ---
      lomo_matched_spec_design: "bf16 × 4 prompts × 4 seeds × 2 temps × 2 orderings"
      lomo_drop_mistral_G_item: 0.846
      lomo_drop_qwen_G_item: 0.834
      lomo_drop_gemma_G_item: 0.802
      lomo_drop_llama_G_item: 0.788
      lomo_spread: 0.058
      lomo_mean_G_item: 0.818
      lomo_sd_G_item: 0.026
      # --- D-study forward projections ---
      d_study_5model_G_item: 0.848
      d_study_8model_G_item: 0.893
      d_study_10model_G_item: 0.910
    result_rationale: >
      核心cross-model数字已锁定不受worst档影响。worst档的关键问题在leave-one-model-out
      matched-spec rerun：初始unmatched analysis显示spread=0.023（看起来stable），
      但那是因为不同3-model子集使用了不同条件数（Gemma缺fp16→432 conditions/model
      vs其他648），设计不可比。matched-spec rerun统一使用最大公约数设计
      （bf16 × 4 prompts × 4 seeds × 2 temps × 2 orderings = 64 conditions/model），
      条件数大幅减少使得估计精度下降。
      Drop-Llama（spread最大端）G_item=0.788，因为Llama是interaction最低的模型
      （19.69%），去掉它后剩余3模型（Mistral 29.25%、Qwen 27.11%、Gemma 23.95%）
      的model×item更大，item difficulty generalizability更差。
      Drop-Mistral（spread最小端）G_item=0.846，因为Mistral是interaction最高的模型
      （29.25%），去掉它反而让剩余3模型的item ranking更一致。
      Spread=0.058意味着G_item在[0.788, 0.846]区间内depending on model selection——
      reviewer可以argue"4个模型不够，G_item的point estimate不可靠"。
      但所有4个子集都保持G_item>0.78（>0.75阈值），item_id始终>35%且为最大source，
      定性结论robust。这个fragility是real的，需要10+模型才能stabilize，
      但在论文中可以honest报告并用D-study projection（10 models→G=0.910）
      来argue方向是对的、只是当前sample不够大。
    tables:
      - name: "Table 1: Cross-model variance decomposition (4 models, MMLU, balanced bf16)"
        data:
          columns: [source, pct, CI_lower, CI_upper]
          rows:
            - [item_id, 42.1, 36.0, 48.8]
            - [model_x_item, 33.6, 28.4, 37.9]
            - [residual, 19.5, 16.2, 23.1]
            - [prompt_x_item, 4.6, 3.1, 6.4]
            - [seed_x_item, 4.7, 3.2, 6.5]
            - [temperature, 1.2, 0.4, 2.3]
            - [model, 0.8, 0.1, 2.1]
            - [precision, 0.0006, 0.0, 0.002]
            - [other_interactions, 0.5, 0.1, 1.2]
      - name: "Table 2: Leave-one-model-out matched-spec G_item"
        data:
          columns: [dropped_model, G_item, item_id_pct, model_x_item_pct]
          rows:
            - [Mistral, 0.846, 44.8, 28.3]
            - [Qwen, 0.834, 43.2, 30.1]
            - [Gemma, 0.802, 40.5, 35.8]
            - [Llama, 0.788, 39.1, 37.6]
            - [All_4, 0.820, 42.1, 33.6]
      - name: "Table 3: Per-model single-model variance decomposition"
        data:
          columns: [source, llama_pct, gemma_pct, mistral_pct, qwen_pct]
          rows:
            - [item_id, 61.1, 57.8, 59.4, 55.6]
            - [residual, 17.2, 19.1, 18.4, 20.8]
            - [precision_x_item, 7.2, 7.8, 7.1, 6.5]
            - [prompt_x_item, 4.6, 5.3, 4.9, 6.2]
            - [seed_x_item, 4.7, 4.5, 4.6, 5.1]
            - [temperature_x_item, 3.1, 3.4, 3.2, 3.6]
            - [temperature, 1.2, 1.1, 1.5, 1.2]
            - [precision, 0.5, 0.6, 0.5, 0.7]
    figures_description:
      - >
        Fig 1 (The Reveal): 并排stacked-bar图。左侧single-model（Llama）：item_id
        61.1%占据主导，residual 17.2%次之。右侧cross-model（4 models）：item_id
        缩至42.1%，model×item以33.6%的红色大色块出现为second-largest source，
        residual微降至19.5%。箭头标注"19pp absorbed by model×item"。
        视觉效果强烈——明确显示single-model G-study how much overestimates item dominance。
      - >
        Fig 2: Leave-one-model-out G_item waterfall chart。4个子集的G_item从0.788到
        0.846，标注spread=0.058。全4-model G_item=0.820用虚线标注。
        红色区域标注"fragility zone"。
    analysis: >
      exp-001的锁定数字是worst档论文的foundation——model×item=33.6%和D-study
      Δ=0.004无论其他实验如何都是solid findings。leave-one-model-out matched-spec
      spread=0.058是worst档的核心concern：它意味着4-model estimate有~3%的standard
      deviation，reviewer可以argue point estimate不够precise。
      Defense策略：(1) 所有4个子集都保持qualitative结论（item_id最大，model×item
      second largest），spread影响的是magnitude不是ranking；(2) D-study projection
      清晰显示adding models monotonically improves G_item，当前4-model是under-powered
      但方向正确；(3) unmatched analysis的spread仅0.023，matched的0.058部分归因于
      reduced design（64 vs 432 conditions），真实spread可能介于两者之间。
      BF16-vs-FP16 sensitivity确认FP32 anomaly是vLLM artifact（positive result）。

  - name: "exp-001b: Item resampling stability test"
    plan_id: "exp-001b"
    description: >
      3个独立200-item分层抽样（seeds 0, 7, 99）× Llama × 3 precisions × 3 prompts
      × 3 seeds × 2 orderings = 54 conditions/sample × 200 items = 10,800 records/sample。
      Total 32,400 records。在worst档中，CV(item_id)=0.143，显示42%的point estimate
      对item sampling敏感。
    expected_results:
      total_samples: 3
      conditions_per_sample: 54
      records_per_sample: 10800
      total_records: 32400
      sample_seed0_item_id_pct: 61.1
      sample_seed7_item_id_pct: 52.8
      sample_seed99_item_id_pct: 70.4
      item_id_mean_pct: 61.4
      item_id_sd_pct: 8.8
      item_id_cv: 0.143
      sample_seed0_G_binary: 0.611
      sample_seed7_G_binary: 0.536
      sample_seed99_G_binary: 0.689
      G_binary_mean: 0.612
      G_binary_sd: 0.077
      G_binary_cv: 0.126
      sample_seed0_residual_pct: 17.2
      sample_seed7_residual_pct: 23.1
      sample_seed99_residual_pct: 12.8
      residual_cv: 0.293
      variance_ranking_preserved_all_samples: true
      item_id_always_largest: true
      profile_corr_seed0_seed7: 0.79
      profile_corr_seed0_seed99: 0.73
      profile_corr_seed7_seed99: 0.76
      avg_profile_corr: 0.76
    result_rationale: >
      200 items是MMLU 14,042题的1.4%。即使分层抽样（按57个subjects），每个subject
      内的difficulty分布仍有大量变异。seed 99抽到更多high-variance subjects
      （abstract_algebra, formal_logic, professional_medicine——这些subjects的item
      difficulty range极大，从trivial到near-impossible），导致item间方差膨胀至70.4%。
      seed 7则抽到更多"中等难度集中"的subjects（high_school_biology, marketing），
      item间差异较小，item_id降至52.8%。
      CV=0.143意味着单次200-item抽样的item_id%有约14%的相对变异。
      这不是catastrophic——variance ranking在所有3次抽样中保持（item_id始终最大），
      但足以让reviewer质疑"42.1%"这个具体数字。G系数的CV=0.126较低，说明
      reliability estimate比variance percentage更robust——从0.536到0.689变化较大
      但定性判断不变（全部<0.80阈值，需要more items）。
      profile correlation平均0.76说明方差结构的shape有moderate一致性，
      但不足以claim"structure is invariant to item sampling"。
      关键defense：把instability本身spin为finding——"item sampling is itself a major
      variance source, providing empirical justification for G-theory's item-as-facet
      treatment and D-study budgeting approach。"
    tables:
      - name: "Table 4: Resampling stability across 3 item draws (single-model Llama)"
        data:
          columns: [source, seed0_pct, seed7_pct, seed99_pct, mean_pct, sd_pct, cv]
          rows:
            - [item_id, 61.1, 52.8, 70.4, 61.4, 8.8, 0.143]
            - [residual, 17.2, 23.1, 12.8, 17.7, 5.2, 0.291]
            - [precision_x_item, 7.2, 8.7, 5.6, 7.2, 1.6, 0.217]
            - [prompt_x_item, 4.6, 5.8, 3.9, 4.8, 1.0, 0.201]
            - [seed_x_item, 4.7, 5.2, 4.2, 4.7, 0.5, 0.106]
            - [temperature_x_item, 3.1, 3.3, 2.7, 3.0, 0.3, 0.100]
            - [temperature, 1.2, 1.0, 0.9, 1.0, 0.2, 0.153]
            - [precision, 0.5, 0.6, 0.3, 0.5, 0.2, 0.333]
      - name: "Table 5: G-coefficient stability across item draws"
        data:
          columns: [metric, seed0_G, seed7_G, seed99_G, mean_G, sd_G, cv]
          rows:
            - [binary, 0.611, 0.536, 0.689, 0.612, 0.077, 0.126]
            - [text_exact, 0.007, 0.005, 0.009, 0.007, 0.002, 0.286]
    figures_description:
      - >
        Fig 3: 三组200-item样本的方差分解并排stacked-bar。item_id始终最大但高度
        显著不同（52.8%/61.1%/70.4%）。误差棒标注mean±1SD。右侧小panel显示
        G-coefficient across samples较为stable（0.536-0.689），标注"G more robust
        than variance %"。
    analysis: >
      CV=0.143直接影响headline claim的precision——论文不能报告"item_id=42.1%"
      作为definitive number，需要报告"42.1% [range across item samples: ~36-48%]"。
      但这与bootstrap CI [36.0, 48.8]一致，说明resampling instability和statistical
      uncertainty是同一量级的——bootstrap CI已经captures了item sampling variability。
      正面spin：(1) item_id始终是largest source（even at 52.8%远超residual 23.1%），
      定性结论robust；(2) resampling instability本身reinforces G-theory的item-as-facet
      treatment——如果item sampling无关紧要，就不需要G-theory了；
      (3) G_binary的CV=0.126 < item_id的CV=0.143，reliability比raw variance %更stable。
      Reviewer concern "连自己的estimate都不stable"可以用"this is precisely why
      D-study budgets recommend 500+ items"来回应。

  - name: "exp-002: Multi-benchmark replication (flat gradient)"
    plan_id: "exp-002"
    description: >
      4 models × 2 precisions (bf16/fp16) × 6 prompts × 6 seeds × 2 temperatures
      (T=0.0/T=0.7) × 4 orderings × 200 items on GSM8K, ARC-Challenge, HellaSwag。
      Per benchmark: 4×2×6×6×2×4=2304 conditions × 200 items = 460,800 records。
      Total: 1,382,400 records。Cross-model balanced analysis: bf16 only,
      576 conditions/model × 4 × 200 = 230,400/benchmark。
      结果：variance structure跨benchmark几乎不变，item_id range仅5.7pp，
      gradient narrative完全不成立。
    expected_results:
      total_records_all_benchmarks: 1382400
      benchmarks_completed: 3
      # --- Cross-model variance decomposition per benchmark ---
      mmlu_cross_item_id_pct: 42.1
      mmlu_cross_model_x_item_pct: 33.6
      mmlu_cross_residual_pct: 19.5
      mmlu_cross_G_item: 0.820
      gsm8k_cross_item_id_pct: 38.4
      gsm8k_cross_model_x_item_pct: 31.8
      gsm8k_cross_residual_pct: 22.6
      gsm8k_cross_prompt_x_item_pct: 8.4
      gsm8k_cross_seed_x_item_pct: 5.8
      gsm8k_cross_temperature_pct: 3.2
      gsm8k_cross_G_item: 0.682
      gsm8k_cross_G_binary_200items: 0.438
      gsm8k_overall_accuracy: 0.512
      arc_cross_item_id_pct: 44.1
      arc_cross_model_x_item_pct: 30.5
      arc_cross_residual_pct: 18.8
      arc_cross_prompt_x_item_pct: 5.2
      arc_cross_seed_x_item_pct: 4.6
      arc_cross_temperature_pct: 1.4
      arc_cross_G_item: 0.718
      arc_cross_G_binary_200items: 0.521
      arc_overall_accuracy: 0.548
      hellaswag_cross_item_id_pct: 41.8
      hellaswag_cross_model_x_item_pct: 35.2
      hellaswag_cross_residual_pct: 17.4
      hellaswag_cross_prompt_x_item_pct: 3.8
      hellaswag_cross_seed_x_item_pct: 4.2
      hellaswag_cross_temperature_pct: 0.8
      hellaswag_cross_G_item: 0.668
      hellaswag_cross_G_binary_200items: 0.492
      hellaswag_overall_accuracy: 0.621
      # --- Gradient metrics ---
      cross_bench_item_id_range_pp: 5.7
      cross_bench_item_id_min: 38.4
      cross_bench_item_id_max: 44.1
      cross_bench_model_x_item_range_pp: 4.7
      gradient_rank_knowledge_to_reasoning: null
      gradient_linear_fit_R2: 0.12
      # --- Cross-benchmark separability ---
      separability_binary_mmlu_pct: 0.08
      separability_binary_gsm8k_pct: 3.6
      separability_binary_arc_pct: 2.4
      separability_binary_hellaswag_pct: 4.8
      separability_binary_max_pct: 4.8
      # --- D-study cross-benchmark transfer ---
      d_study_mmlu_510items_G: 0.800
      d_study_gsm8k_510items_G: 0.753
      d_study_arc_510items_G: 0.768
      d_study_hellaswag_510items_G: 0.742
      d_study_cross_bench_delta_max: 0.058
      d_study_cross_bench_delta_min: 0.032
      d_study_cross_bench_delta_mean: 0.047
      # --- IRT vs G-theory ratio per benchmark ---
      irt_gtheory_ratio_mmlu: 4.1
      irt_gtheory_ratio_gsm8k: 1.7
      irt_gtheory_ratio_arc: 2.5
      irt_gtheory_ratio_hellaswag: 1.6
      # --- G_item cross-benchmark ---
      g_item_cross_bench_min: 0.668
      g_item_cross_bench_max: 0.820
      g_item_cross_bench_mean: 0.722
      # --- Matched 2×2 MMLU re-analysis for fair comparison ---
      mmlu_matched_2x2_item_id_pct: 43.8
      mmlu_matched_2x2_model_x_item_pct: 32.4
      mmlu_matched_2x2_delta_from_full: 1.7
    result_rationale: >
      Gradient叙事死掉的核心原因：item_id跨4个benchmark的range仅5.7pp
      （38.4%-44.1%）。原假设是knowledge benchmarks（MMLU）有高item_id（>55%），
      reasoning benchmarks（GSM8K）有低item_id（<30%），形成20+pp的gradient。
      实际结果是所有benchmark都落在38-44%的狭窄区间内。
      为什么flat？model×item交互在所有benchmark上都在30-36%——这意味着无论
      task type如何，模型间的item difficulty ranking disagreement程度类似。
      直觉上，这是因为7-9B模型在knowledge和reasoning tasks上都有类似程度的
      model-specific strengths/weaknesses：Llama在MMLU的history和GSM8K的
      word problems上都相对strong，Mistral在MMLU的STEM和GSM8K的multi-step上
      都相对weak——model-specificity的pattern在task types之间有一致性。
      G_item跨benchmark从0.668到0.820变化较大（range=0.152），但这主要由
      residual差异驱动而非model×item差异。GSM8K和HellaSwag的G_item低
      （0.668-0.682）是因为higher residual（22.6%和17.4%+更高的prompt×item），
      不是因为model×item更大。
      IRT ratio在GSM8K（1.7×）和HellaSwag（1.6×）上collapse到<2×，原因是
      这些benchmark的IRT也需要更多items（item discrimination更uniform，
      2PL model的efficiency advantage减弱），所以分母增大、ratio压缩。
      MMLU上IRT仍然只需~120 items因为items有strong discrimination gradients
      （从trivial到impossible跨57 subjects），2PL拟合效率高。
      Cross-benchmark separability failure（max=4.8% on HellaSwag binary）
      原因：HellaSwag的sentence completion任务对precision和temperature的
      交互更敏感——不同precision下temperature>0生成的completions有更多
      divergence，且binary scoring的粒度在这类任务上captures了更多差异。
      D-study cross-bench Δ=0.032-0.058意味着MMLU-derived budgets在其他
      benchmark上systematically overestimate reliability by 3-6pp。这是因为
      MMLU的residual较低（19.5%）相对于GSM8K（22.6%）——更多unexplained
      variance意味着需要更多observations来stabilize。
    tables:
      - name: "Table 6: Cross-model variance decomposition by benchmark (4 models, bf16)"
        data:
          columns: [source, mmlu_pct, gsm8k_pct, arc_pct, hellaswag_pct, range_pp]
          rows:
            - [item_id, 42.1, 38.4, 44.1, 41.8, 5.7]
            - [model_x_item, 33.6, 31.8, 30.5, 35.2, 4.7]
            - [residual, 19.5, 22.6, 18.8, 17.4, 5.2]
            - [prompt_x_item, 4.6, 8.4, 5.2, 3.8, 4.6]
            - [seed_x_item, 4.7, 5.8, 4.6, 4.2, 1.6]
            - [temperature, 1.2, 3.2, 1.4, 0.8, 2.4]
            - [model, 0.8, 1.2, 0.9, 0.6, 0.6]
            - [precision, 0.0006, 0.3, 0.1, 0.2, 0.3]
      - name: "Table 7: G_item and IRT comparison by benchmark"
        data:
          columns: [benchmark, G_item_4model, G_binary_200items, irt_items_needed, gtheory_items_G80, ratio]
          rows:
            - [MMLU, 0.820, 0.611, 118, 510, 4.1]
            - [GSM8K, 0.682, 0.438, 286, 486, 1.7]
            - [ARC-Challenge, 0.718, 0.521, 178, 448, 2.5]
            - [HellaSwag, 0.668, 0.492, 312, 502, 1.6]
      - name: "Table 8: Cross-benchmark separability (binary, precision×methodology interaction)"
        data:
          columns: [benchmark, prec_x_prompt_pct, prec_x_seed_pct, prec_x_temp_pct, total_infra_x_method_pct]
          rows:
            - [MMLU, 0.02, 0.01, 0.05, 0.08]
            - [GSM8K, 1.2, 0.8, 1.6, 3.6]
            - [ARC-Challenge, 0.9, 0.5, 1.0, 2.4]
            - [HellaSwag, 1.6, 1.1, 2.1, 4.8]
      - name: "Table 9: D-study cross-benchmark transfer error"
        data:
          columns: [benchmark, mmlu_derived_G_at_510items, actual_G_at_510items, delta]
          rows:
            - [MMLU, 0.800, 0.800, 0.000]
            - [GSM8K, 0.800, 0.753, 0.047]
            - [ARC-Challenge, 0.800, 0.768, 0.032]
            - [HellaSwag, 0.800, 0.742, 0.058]
    figures_description:
      - >
        Fig 4: 4-benchmark stacked-bar variance decomposition。所有bars几乎等高的
        item_id（38-44%）和model×item（30-35%），视觉上immediately conveys"flat"。
        与原计划的"gradient reveals"图截然不同——现在是"uniformity reveals"。
        标注range=5.7pp和"no systematic gradient"。
      - >
        Fig 5: Scatter plot of IRT items vs G-theory items per benchmark。MMLU在
        右上角（IRT 118, G-theory 510, ratio 4.1×），GSM8K和HellaSwag在左下
        （ratio ~1.6-1.7×）。1:1 line和2× line标注。显示ratio的benchmark-dependence。
    analysis: >
      exp-002是worst档叙事转向的关键实验。gradient死亡意味着原planned的
      "cross-benchmark variance gradient — the primary novel finding"完全不可用。
      但flat structure本身可以reframe：
      (1) Positive spin："variance structure is approximately benchmark-invariant"
      → practitioners可以用MMLU结果cautiously extrapolate to other benchmarks。
      这解决了一个practical question。
      (2) D-study transfer error（Δ=0.03-0.06）限定了"cautiously"的程度——
      MMLU-derived budgets会在其他benchmark上overestimate G by 3-6pp，
      需要add 10-15% safety margin。
      (3) IRT ratio的benchmark-dependence（1.6×-4.1×）是一个publishable finding
      本身——解释了为什么field对"IRT够不够"的争论不收敛：答案是benchmark-dependent。
      Separability failure across benchmarks（MMLU 0.08% vs HellaSwag 4.8%）
      means separability完全不能作为general claim，降为"observed on MMLU under
      binary scoring; does not hold generally"。
      Net assessment: exp-002的data是有价值的，只是不支撑原叙事。reframe后
      可以支撑contribution (3)（benchmark-insensitivity as positive）但forcing
      function是writing quality——flat results需要更skillful framing。

  - name: "exp-003: Multi-hardware G-study (partial)"
    plan_id: "exp-003"
    description: >
      原计划4 models × 2+ GPU types × 2 precisions × full crossing。
      在worst档中，第二种GPU（RTX A6000 48GB）在deadline前4周获得，
      仅完成2 models（Llama + Mistral）× 2 precisions（bf16/fp16）× 6 prompts
      × 6 seeds × 3 temps × 4 orderings × 200 items = 2 × 576 × 200 = 230,400 records。
      Hardware × methodology interaction = 4.2% binary average，separability claim破裂。
    expected_results:
      status: PARTIAL
      gpu_types: ["RTX_PRO_6000_96GB", "RTX_A6000_48GB"]
      models_completed: 2
      models: ["Llama-3.1-8B-Instruct", "Mistral-7B-Instruct-v0.3"]
      total_records: 230400
      conditions_per_model: 576
      # --- Hardware variance decomposition (2-model, binary) ---
      hardware_main_effect_pct: 1.8
      hardware_x_precision_pct: 0.9
      hardware_x_prompt_pct: 0.6
      hardware_x_seed_pct: 0.3
      hardware_x_temperature_pct: 1.4
      hardware_x_item_pct: 2.8
      total_hardware_x_methodology_pct: 4.2
      hardware_x_methodology_llama_pct: 3.8
      hardware_x_methodology_mistral_pct: 4.6
      # --- Comparison with single-GPU ---
      single_gpu_infra_x_method_pct: 0.08
      multi_gpu_infra_x_method_pct: 4.2
      delta_pp: 4.12
      # --- Accuracy gaps ---
      llama_pro6000_accuracy: 0.6814
      llama_a6000_accuracy: 0.6791
      llama_hardware_gap_pp: 0.23
      mistral_pro6000_accuracy: 0.6124
      mistral_a6000_accuracy: 0.6083
      mistral_hardware_gap_pp: 0.41
      # --- Binary G comparison ---
      G_binary_single_gpu: 0.611
      G_binary_two_gpu: 0.582
      G_delta: 0.029
    result_rationale: >
      Hardware×methodology interaction从single-GPU的0.08%跳至multi-GPU的4.2%，
      原因是两种GPU有不同的CUDA kernel implementations（RTX PRO 6000使用
      sm_89 Ada Lovelace kernels，A6000使用sm_86 Ampere kernels）。
      BF16 matrix multiply的rounding behavior在两种架构上不同——不是precision
      本身的问题（bf16 spec相同），而是kernel-level implementation差异导致
      少量items在一个GPU上答对、另一个上答错。
      hardware×temperature=1.4%是最大sub-interaction，因为temperature>0时的
      sampling受CUDA RNG implementation影响，不同GPU的cuRAND版本产生
      不同的pseudo-random sequences（即使seed相同）。
      hardware×item=2.8%反映了~5-8个items在两GPU间有consistently不同的
      答案——这些items恰好在model的decision boundary上，kernel-level numerical
      differences足以flip prediction。
      Mistral（4.6%）比Llama（3.8%）的hardware interaction更大，因为Mistral
      accuracy更低（61.2%），更多items在decision boundary附近。
      这个结果对separability是definitive negative："infrastructure×methodology
      ≈0%"只在single-GPU上成立。跨GPU，interaction是non-negligible的。
      但4.2%仍然是minor relative to item_id（42.1%）和model×item（33.6%），
      所以the hierarchy is preserved——hardware interaction doesn't dominate。
    tables:
      - name: "Table 10: Hardware × methodology interaction breakdown (2 models, binary)"
        data:
          columns: [interaction_term, llama_pct, mistral_pct, average_pct]
          rows:
            - [hardware_x_temperature, 1.1, 1.7, 1.4]
            - [hardware_x_precision, 0.7, 1.1, 0.9]
            - [hardware_x_prompt, 0.5, 0.7, 0.6]
            - [hardware_x_seed, 0.2, 0.4, 0.3]
            - [hardware_x_item, 2.4, 3.2, 2.8]
            - [hardware_main, 1.3, 2.3, 1.8]
            - [total_hardware_related, 6.2, 9.4, 7.8]
            - [total_hardware_x_methodology, 3.8, 4.6, 4.2]
    figures_description:
      - >
        Fig (appendix): 双GPU variance decomposition stacked-bar。item_id仍dominant
        （~40%），但hardware-related components合计7.8%，以橙色系标注。
        hardware×methodology=4.2%用红色标注并与single-GPU的0.08%对比。
    analysis: >
      exp-003的partial completion足以kill separability claim但不够做full hardware
      G-study。只有2个模型意味着hardware×model interaction无法properly estimate。
      但data is sufficient to downgrade separability from "claim" to "observation
      limited to single-GPU environments"。
      论文framing：在Methods中honest报告"hardware crossing was partially completed
      (2 of 4 models)"，在Results中报告4.2% interaction as "preliminary evidence
      that separability does not hold across GPU architectures"，在Discussion中
      qualify all prior separability statements to "single-GPU, single-architecture"。
      这不fatal——separability在worst档叙事中已经不是contribution了。

  - name: "exp-004: Comprehensive analysis"
    plan_id: "exp-004"
    description: >
      基于exp-001/001b/002/003数据的全面分析。Worst档中exp-003仅有partial data，
      但exp-001和exp-002完整。可执行13/17 planned analyses。
      核心输出：IRT vs G-theory对比（benchmark-dependent ratio），D-study
      cross-benchmark transfer analysis，完整robustness package。
    expected_results:
      planned_analyses: 17
      executable_analyses: 13
      blocked_analyses: 4
      blocked_list: ["full hardware G-study", "hardware ranking stability",
                     "hardware logprob analysis", "hardware cost optimization"]
      # --- (a) Model-as-facet: locked from exp-001 ---
      model_as_facet_item_id_pct: 42.1
      model_as_facet_model_x_item_pct: 33.6
      model_as_facet_G_item: 0.820
      # --- (b) Bootstrap CIs (MMLU) ---
      bootstrap_n: 1000
      item_id_CI_95: [36.0, 48.8]
      model_x_item_CI_95: [28.4, 37.9]
      residual_CI_95: [16.2, 23.1]
      G_item_CI_95: [0.782, 0.861]
      G_binary_CI_95: [0.571, 0.652]
      # --- (c) D-study projections ---
      d_study_practical_items_G80_mmlu: 510
      d_study_practical_items_G80_gsm8k: 624
      d_study_practical_items_G80_arc: 538
      d_study_practical_items_G80_hellaswag: 652
      d_study_cross_bench_delta_range: [0.032, 0.058]
      d_study_14k_mmlu_G: 0.972
      # --- (d) REML vs Henderson I ---
      reml_henderson_max_diff_pp: 0.4
      reml_convergence_iterations: 500
      reml_practical_convergence_delta: 0.003
      # --- (h) IRT vs G-theory per benchmark ---
      irt_gtheory_ratio_mmlu: 4.1
      irt_gtheory_ratio_gsm8k: 1.7
      irt_gtheory_ratio_arc: 2.5
      irt_gtheory_ratio_hellaswag: 1.6
      irt_gtheory_ratio_mean: 2.5
      irt_gtheory_ratio_sd: 1.14
      # --- (i) Power analysis ---
      min_detectable_interaction_pct: 0.8
      power_at_1pct_interaction: 0.94
      power_at_5pct_interaction: 0.99
      # --- (k) Fixed vs random sensitivity ---
      G_all_random: 0.611
      G_temp_fixed: 0.634
      G_ordering_fixed: 0.645
      G_both_fixed: 0.664
      fixed_random_max_delta: 0.053
      # --- (l) Binary data analysis ---
      bernoulli_obs_variance_corr: 0.91
      null_sim_item_id_pct: 0.08
      obs_to_bernoulli_ratio: 1.0008
      # --- (m) Bootstrap vs jackknife ---
      bootstrap_jackknife_CI_ratio_mean: 1.02
      bootstrap_jackknife_CI_ratio_range: [0.96, 1.04]
      # --- (n) Matched 2×2 MMLU ---
      mmlu_2x2_vs_3x3_max_delta_pp: 1.7
      # --- (o) Full benchmark projection ---
      mmlu_14k_items_G_projected: 0.972
      # --- (p) Logprob across benchmarks ---
      logprob_mmlu_item_id_pct: 48.3
      logprob_gsm8k_item_id_pct: 44.8
      logprob_arc_item_id_pct: 46.1
      logprob_hellaswag_item_id_pct: 45.9
      logprob_cross_bench_range_pp: 3.5
      # --- (q) GPU cost ---
      gpu_hours_G80_mmlu: 340
      gpu_hours_G80_gsm8k: 415
      gpu_hours_G80_hellaswag: 430
      gpu_hours_G90_mmlu: 890
    result_rationale: >
      exp-004的analysis在worst档中产出两类结果：
      (1) Robust surviving findings（不受数据缺失影响）：IRT vs G-theory对比
      在MMLU上4.1×（locked），但cross-benchmark显示ratio从1.6×到4.1×——
      reviewer会说"so the 3-4× claim is only valid for MMLU"。ratio collapse的
      原因：在reasoning benchmarks上，IRT的2PL model fit效率降低（items have
      更uniform discrimination，lower slope parameters），IRT自己也需要更多items
      （GSM8K: 286 items vs MMLU: 118 items），所以G-theory的extra cost
      相对缩小。论文可以claim "3.6-4.4× on MMLU" and "1.6-4.1× benchmark-
      dependent range"——后者本身是informative finding。
      (2) Weakened findings：D-study cross-benchmark transfer Δ=0.03-0.06
      意味着MMLU budgets不能直接apply to other benchmarks（会high by 3-6pp G）。
      这undercuts contribution (3)的"practitioners can extrapolate"——需要加
      significant caveat "with 10-15% safety margin"。
      Robustness package全部基于exp-001 Llama数据，fully intact：binary not
      artifact（null sim 0.08%），fixed vs random insensitive（Δ<0.053），
      bootstrap=jackknife（ratio 0.96-1.04），REML confirms Henderson I（<0.4pp）。
      这些是论文的guaranteed floor——无论worst scenario多bad，robustness is there。
      Logprob analysis跨benchmarks显示更tight的range（3.5pp vs binary的5.7pp），
      suggesting logprob-based scoring reduces benchmark-dependence。This is a
      minor but novel observation that can go in Discussion。
    tables:
      - name: "Table 11: IRT vs G-theory item requirements by benchmark"
        data:
          columns: [benchmark, irt_2pl_items, gtheory_practical_items, ratio, gtheory_accounts_for]
          rows:
            - [MMLU, 118, 510, 4.1, "prompt + seed + ordering + temp + prec"]
            - [GSM8K, 286, 486, 1.7, "same facets; IRT also needs more items"]
            - [ARC-Challenge, 178, 448, 2.5, "same"]
            - [HellaSwag, 312, 502, 1.6, "same; IRT needs most items here"]
      - name: "Table 12: D-study budget recommendations by benchmark (G≥0.80, practical)"
        data:
          columns: [benchmark, items, prompts, seeds, G_projected, CI_95]
          rows:
            - [MMLU, 510, 2, 3, 0.800, "[0.782, 0.825]"]
            - [GSM8K, 624, 3, 4, 0.801, "[0.774, 0.831]"]
            - [ARC-Challenge, 538, 2, 3, 0.800, "[0.778, 0.826]"]
            - [HellaSwag, 652, 3, 4, 0.802, "[0.771, 0.838]"]
      - name: "Table 13: Methodological robustness summary"
        data:
          columns: [analysis, result, status]
          rows:
            - ["Binary not artifact (null sim)", "item_id=0.08% vs obs 61.1% (737×)", "PASS"]
            - ["Fixed vs random sensitivity", "max Δ(G)=0.053", "PASS"]
            - ["Bootstrap = Jackknife CIs", "ratio range [0.96, 1.04]", "PASS"]
            - ["REML vs Henderson I", "max diff < 0.4pp", "PASS"]
            - ["Temperature stratification", "binary G: 0.760→0.549 (T=0→0.7)", "PASS"]
            - ["Bernoulli variance correlation", "r=0.91 (item variance partly mechanical)", "NOTED"]
            - ["D-study cross-benchmark transfer", "Δ=0.032-0.058", "CAVEAT"]
            - ["Leave-one-model-out matched", "spread=0.058", "CAVEAT"]
    figures_description:
      - >
        Fig 6: D-study projection curves per benchmark。4条curves（MMLU/GSM8K/ARC/
        HellaSwag），x轴item count，y轴G coefficient。G≥0.80 threshold line。
        MMLU curve最陡（510 items达标），HellaSwag最缓（652 items）。
        IRT curves叠加显示（虚线），MMLU上gap大（4.1×），HellaSwag上gap小（1.6×）。
      - >
        Fig 7: Temperature-stratified G heatmap。4 benchmarks × 3 temperatures
        （T=0.0/0.3/0.7）× 2 metrics（binary/text-exact）。Binary从上到下
        degradation monotonic。Text-exact全黑（<0.01）。Cross-benchmark pattern
        similar（supporting "structure is approximately invariant"）。
    analysis: >
      exp-004在worst档中的关键产出是benchmark-conditional IRT ratio——这是
      新发现，解释了field对"IRT够不够"的长期争论。可以claim："The IRT-G-theory
      gap is benchmark-dependent, ranging from 1.6× (HellaSwag) to 4.1× (MMLU),
      because IRT item parameters (discrimination, difficulty) vary across task
      types"。这不需要gradient叙事，是self-contained的。
      D-study cross-benchmark transfer analysis（Δ=0.03-0.06）is nuanced：
      正面解读是MMLU budgets are "approximately right" (within 6pp G)；
      负面解读是they're "not directly transferable"。论文adopt中间立场：
      "MMLU-derived budgets provide a lower bound; benchmark-specific calibration
      improves precision by 3-6pp G"。
      Robustness package的6个PASS + 2个CAVEAT provides methodological credibility。
      CAVEAT items (D-study transfer, LOMO) are discussed honestly rather than hidden。

  - name: "exp-005: 14B model extension"
    plan_id: "exp-005"
    description: >
      Qwen3-14B和DeepSeek-R1-Distill-14B在datacenter GPU上的BF16/FP16测试。
      Worst档中未执行——deps on exp-003 timeline + 无可用48GB+ GPU时间。
    expected_results:
      status: NOT_COMPLETED
      records_collected: 0
      blocking_reason: >
        exp-003在deadline前4周才partially完成，exp-005的protocol
        依赖exp-003确定的multi-hardware procedure。同时14B模型需要
        ~24GB VRAM（bf16），PRO 6000可以跑但被P0实验占满。
        无法在AAAI deadline前执行。
    result_rationale: >
      exp-005的timeline依赖链：exp-003 partial completion → protocol finalization
      → 14B model runs。exp-003在T-4周才完成，来不及做exp-005的full crossing。
      此外，14B模型的inference latency比8B高~1.8×，即使有GPU也难在deadline内
      完成576 conditions × 2 models × 200 items = 230,400 records。
      对论文的影响：所有结论限于7-9B模型规模。reviewer concern "scale validation"
      只能在Limitations中acknowledge，argue "7-9B是最commonly used open-weight
      model class"。
    tables: []
    figures_description: []
    analysis: >
      不fatal。论文scope明确为"7-9B open-weight models"。14B extension
      适合ACL ARR camera-ready或后续独立paper。

  - name: "exp-006: Fine-tuning G-study"
    plan_id: "exp-006"
    description: >
      RoBERTa-large在SST-2/MNLI/RTE/COPA上的fine-tuning方差分解。
      Worst档中未执行——P1优先级，GPU budget被P0消耗。
    expected_results:
      status: NOT_COMPLETED
      records_collected: 0
      blocking_reason: >
        P1 priority。P0实验（exp-001 ~100h + exp-002 ~200h + exp-003 ~60h partial）
        消耗了大部分GPU budget。1,728次fine-tuning runs × ~15min ≈ 430 GPU-hours
        无法accommodate。
    result_rationale: >
      Per D006 framing directive #5，fine-tuning已降级为Discussion-section
      preliminary observation，不是numbered contribution。即使完成，encoder-only
      RoBERTa的fine-tuning与decoder LLM inference的methodological gap也会被
      reviewer指出。在worst档reframed narrative（MMLU case study + IRT comparison）
      中，fine-tuning完全outside scope。
    tables: []
    figures_description: []
    analysis: >
      零影响。在Discussion中mention "extending G-theory to fine-tuning variance
      is natural future work; Dodge et al. (2020) and Bui et al. (2025) provide
      preliminary evidence that seed/LR dominate fine-tuning variance"。

  - name: "exp-007: LayerCast precision mitigation"
    plan_id: "exp-007"
    description: >
      LayerCast（FP16 storage + FP32 compute）作为额外precision条件。
      P2优先级，worst档中未执行。
    expected_results:
      status: NOT_COMPLETED
      records_collected: 0
      blocking_reason: P2 priority, not attempted within AAAI timeline
    result_rationale: >
      LayerCast是mitigation strategy evaluation，不是core finding。
      BF16-vs-FP16 sensitivity已显示precision effect=0.0006%（接近zero），
      LayerCast的additional data point价值marginal——precision已经不是
      variance source。可以在Discussion中cite Yuan et al. (2025)的
      LayerCast results as "practitioners can further reduce precision variance
      via mixed-precision strategies"。
    tables: []
    figures_description: []
    analysis: >
      零影响。Precision在bf16/fp16上已经是non-issue（0.0006%），
      LayerCast实验变得moot。

  - name: "exp-008: MATH benchmark extension"
    plan_id: "exp-008"
    description: >
      MATH benchmark（200 items）测试reasoning-heavy任务的variance structure。
      P2优先级且deps on exp-002，worst档中未执行。
    expected_results:
      status: NOT_COMPLETED
      records_collected: 0
      blocking_reason: >
        P2 priority。Deps on exp-002 pipeline（已完成但consumed timeline）。
        MATH的chain-of-thought generation需要significantly longer inference time
        （avg ~45 tokens vs MMLU ~1 token），200h GPU budget已用尽。
    result_rationale: >
      exp-002已经覆盖了GSM8K（math reasoning）、ARC（science reasoning）、
      HellaSwag（commonsense），增加MATH的marginal value在worst档flat gradient
      下更低——不会出现新pattern，只会是another data point在38-44% item_id区间内。
      如果需要bolster "benchmark-insensitivity" claim，现有4个benchmarks
      （MMLU + 3 from exp-002）已经sufficient。
    tables: []
    figures_description: []
    analysis: >
      Marginal impact。4个benchmarks showing flat structure已经支撑
      "benchmark-insensitivity" reframe。MATH would be 5th data point
      but not change the conclusion。适合ACL ARR补充。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8754eb8f-2a03-489e-a6ca-d185fc61da73",
  "isSidechain": false,
  "requestId": "req_011CbFNU8WBzSSrEn4r8PVMs",
  "type": "assistant",
  "uuid": "fc8826c5-67fe-4ad8-91bb-7deca0209684",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoSxLdguzZL5byskwDGgLy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14829,
      "cache_read_input_tokens": 40030,
      "output_tokens": 27357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 27357,
          "cache_read_input_tokens": 40030,
          "cache_creation_input_tokens": 14829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14829
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

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Gradient flat or reversed; item resampling unstable; core story reduces to single-benchmark (MMLU) model×item finding — must reframe angle 核心假设：['exp-002:…",
  "leafUuid": "fc8826c5-67fe-4ad8-91bb-7deca0209684",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Model×item interaction in LLM evaluation variance",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Gradient flat or reversed; item resampling unstable; core story reduces to single-benchmark (MMLU) model×item finding — must reframe angle 核心假设：['exp-002:…",
  "leafUuid": "fc8826c5-67fe-4ad8-91bb-7deca0209684",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Model×item interaction in LLM evaluation variance",
  "sessionId": "434afb6d-4140-450b-b4ba-5f06ef1dacab"
}
```

---
