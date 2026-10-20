# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/b609ec7e-7843-4d55-82de-38f83ed68c88.jsonl`
- **Structured JSON:** [`f426337bd00fdabfb149.json`](../../sessions/f4/f426337bd00fdabfb149.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:24:56.848Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:24:56.848Z",
  "sessionId": "b609ec7e-7843-4d55-82de-38f83ed68c88",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: nlp_variance_gtheory\n\n## paper_framing.md\n\n# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Model-Conditional Item Dominance**: Item selection is the single largest variance source in single-model LLM evaluation (61.1% on MMLU), but model×item interaction (26.2%) emerges as the second-largest source when model is treated as a crossed facet. Item difficulty rankings are model-specific: two models with similar aggregate accuracy (Llama 66.4% vs Gemma 73.2%) disagree dramatically at the item level — item_id drops from 61% (single-model) to 38% (cross-model) as model×item absorbs the model-conditional portion. This means single-model variance decompositions overestimate item dominance by conflating universal and model-specific item difficulty. Cross-benchmark gradient (pending exp-002) is hypothesized to further modulate this structure.\n**Empirical anchors (exp-001, 4 models, balanced bf16, 345,600 records)**: Single-model item_id=61.1%, cross-model item_id=42.1% [36.0-48.8%] (↓19pp), model×item=33.6% [28.4-37.9%] (second-largest source, increased from 3-model 31.7%). G_item=0.820 [0.782-0.861]. D-study prediction validated out-of-sample: 3-model predicted G=0.816 for n=4, actual=0.820 (Δ=0.004). Forward projection: 5 models → G=0.848, 8→0.893, 10→0.910 (G≥0.90 requires ~10 models). Residual dropped 24%→19.5% as 4th model split residual into model×item. Per-model interaction: Mistral 29.25% (lowest accuracy 63.8%) > Qwen 27.11% > Gemma 23.95% > Llama 19.69%.\n**REML robustness**: REML-EM (500 iter, practical convergence Δ<0.003pp) confirms Henderson I: all components differ <0.5pp. Henderson I unbiased for balanced designs. Dataset B differences (item_id 38→52%, model×item 26→12%) due to design differences (factor selection), not estimator bias — measurement design choices themselves affect observed variance structure.\n**Completed robustness**: BF16-vs-FP16 sensitivity confirms precision→0.0006% without FP32 (FP32 is sole source of precision variance); leave-one-model-out (matched-spec) shows G_item range 0.747-0.793 across 3-model subsets (spread=0.046) — all below 0.80, confirming 4 models is the minimum for reliable cross-model measurement. LOMO also confirms item_id dominance and model×item as second-largest source are stable across all subsets.\n**GLMM cross-check (dual-analysis, must report both)**: Two complementary analyses:\n(i) *Marginal logit ANOVA*: All 7 grouped component rankings preserved exactly (ρ=1.0), consistent with MQL-1 prediction that logit-scaling is approximately constant at p̄=0.70.\n(ii) *VB GLMM (25-item subsample)*: Ranking reversal on top-2 — model:item_id=47.3% > item_id=22.8% on logit scale (ρ=0.571, p=0.18). Attributable to model underspecification (missing 4 item-interaction terms in VB model) + subsample.\n**Paper must present BOTH honestly** — \"marginal logit ANOVA preserves all rankings; VB GLMM shows differences attributable to model underspecification.\" Do NOT overwrite ρ=0.571 with ρ=1.0. Implication: model×item interaction may be even more important than Henderson I indicates on logit scale — strengthens Claim 1's core message.\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent and temperature-conditional. Binary correct: G=0.611 (200 items), G≥0.80 requires ~510 items (all facets random) or ~414 items (practical: precision+temperature fixed). Text-exact-match: G=0.007 (temperature dominates at 79.7%), unreliable at any temperature >0. Temperature-stratified analysis reveals binary G degrades monotonically (T=0.0: 0.760 → T=0.7: 0.549). G-theory requires 3.6-4.4× more items than IRT (510 vs 116) because it accounts for prompt×item (4.6%), seed×item (4.7%), and residual (21.6%) dimensions that IRT ignores. Current practices (1 prompt, 1 seed, ≤200 items) yield G=0.611 — below the 0.80 threshold for dependable measurement.\n\n## Contributions (4 条，明确区分)\n\n1. **Model×item interaction as the hidden dominant source**: In a balanced 4-model design (345,600 records), model×item interaction (33.6%, CI [28.4-37.9%]) is the second-largest variance source, while item_id drops from 61% (single-model) to 42%. Item difficulty rankings are model-specific — single-model G-studies overestimate item dominance by conflating universal and model-specific difficulty. G_item=0.820 [0.782-0.861] with 4 models; D-study prediction validated out-of-sample (3-model predicted 0.816, actual 0.820, Δ=0.004). Reaching G≥0.90 requires ~10 models. [Note: position as quantification of a phenomenon expected from measurement theory, not as a surprising discovery. The novelty is the magnitude, the out-of-sample D-study validation, and the cross-model generalizability implications.]\n\n2. **Precision separability with metric qualification**: Precision×methodology interactions are negligible under binary scoring (<0.1%), providing empirical support for isolated-factor studies. Under text-exact-match scoring, precision×temperature reaches 4.15%, consistent with floating-point non-associativity. Separability is confirmed as metric-conditional. [Note: scope to \"numerical precision on single GPU architecture\" — not \"infrastructure\" broadly. This is a confirmatory secondary finding, not a primary contribution. Pending BF16-vs-FP16 sensitivity to isolate FP32/vLLM confound.]\n\n3. **IRT vs G-theory: the cost of multi-facet reliability**: The first empirical quantification of the multi-facet reliability cost for LLM evaluation: G-theory requires 3.6-4.4× more items than IRT (510 vs 116 for MMLU) because it accounts for prompt, seed, and ordering dimensions that IRT ignores. At IRT's recommended 116 items, G-theory G is only 0.529. This quantifies the \"hidden cost\" of evaluation dimensions invisible to IRT. [Note: keep as numbered contribution — Dream + Reviewer consensus this is one of the paper's strongest findings. Wording adjusted from \"first direct comparison\" to \"first empirical quantification\" per SF6 resolution.]\n\n4. **Practitioner toolkit**: Open-source G-theory variance decomposition pipeline + D-study budget calculator for LLM evaluation. Includes: (a) benchmark-specific reproducibility budget tables (items × prompts × seeds for target G), (b) temperature-stratified reliability guide, (c) model-as-facet analysis template. Addresses \"purely diagnostic\" criticism — provides actionable tools, not just warnings.\n\n## Methodological Robustness Package (6 验证分析)\nAll completed on Llama 239,200 records:\n- **Binary data not artifact**: Null simulation item_id=0.08% vs observed 61.1% (737.5×); obs/Bernoulli ratio=1.0008\n- **Fixed vs random insensitive**: Binary G ranges 0.611-0.664 across all facet classification choices\n- **Bootstrap = jackknife**: CI width ratio 0.96-1.04, independence violation negligible\n- **Temperature stratification**: Binary G degrades T=0.0 (0.760) → T=0.7 (0.549); text metric unreliable at all T>0\n- **D-study formula verified**: Monotonicity assertion added; min_items_G80=414 (practical) / 510 (all random)\n- **IRT comparison**: G-theory 3.6-4.4× more conservative than IRT; difference attributable to prompt/seed/ordering dimensions\n- **REML vs Henderson I**: REML-EM (500 iter) confirms all components within <0.5pp of Henderson I; Henderson I unbiased for balanced designs\n- **BF16-vs-FP16 sensitivity**: Excluding FP32, precision effect drops from 0.4% to 0.0006% (precision×item: 1.3%→0.04%). FP32 anomaly is entirely a vLLM enforce_eager artifact, not a fundamental precision effect. BF16≈FP16 (Δ=0.23pp accuracy)\n- **Leave-one-model-out stability**: All 3-model subsets preserve item_id dominance (39-45%) and model×item as second-largest (32-37%). G_item range 0.747-0.793 (spread=0.046), all below 0.80 — confirming 4 models is the minimum configuration for G≥0.80. This strengthens the D-study \"need ~10 models for G≥0.90\" prediction.\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of 345,600 evaluation records across 4 models on MMLU (200 items × 6 prompts × 6 seeds × 3 temperatures × 4 orderings), item selection accounts for 42% of variance when model is treated as a crossed facet — but model×item interaction (34%) emerges as the second-largest source, revealing that item difficulty rankings are substantially model-specific (G_item=0.82, requiring ~10 models for G≥0.90). A D-study from 3 models predicted the 4-model G coefficient within 0.004 — out-of-sample validation of the D-study methodology. G-theory requires 3.6-4.4× more items than IRT for reliable measurement because it accounts for prompt, seed, and ordering dimensions that IRT ignores. Numerical precision×methodology interactions are negligible under binary scoring (<0.1%). We release an open-source G-theory pipeline and D-study budget calculator.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (5 figures):\n  1. **Stacked-bar: single-model vs cross-model variance decomposition** — item_id shrinks from 61% to 42%, model×item appears at 34%, residual drops 24%→20%. The \"reveal\" figure.\n  2. **G-theory crossed design diagram** — facets, levels, crossing structure\n  3. **D-study projection curves** — G vs item count for binary (practical vs all-random) and text metric. Shows G≥0.80 threshold at ~414/510 items.\n  4. **IRT vs G-theory item requirement comparison** — bar chart showing 116 (IRT) vs 510 (G-theory) items, with breakdown of where the extra items go (prompt×item, seed×item, residual)\n  5. **Temperature-stratified G coefficient heatmap** — binary vs text metric × 3 temperatures, showing metric×temperature interaction\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed quasi-random facet**: In exp-001 analysis, model is treated as a crossed quasi-random facet — purposive sample from 4 major architecture families (Llama, Gemma, Mistral, Qwen), not a random draw from all LLMs. Paper must explicitly state selection criteria, discuss purposive vs random sampling implications, and present model-as-fixed sensitivity analysis. D-study Δ=0.004 out-of-sample prediction supports exchangeability assumption. Plan to add 2-3 models (Yi-1.5-9B, OLMo-2-7B, etc.) to strengthen to 6-7 models per MF2 resolution.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).\n\n## Methodological Defenses (Dream #2 审稿问题逐条应对)\n\n### MD1. Binary Data in G-theory\n**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).\n**Defense strategy (upgraded per Round 1 MF1 + Reviewer + GLMM results)**: Four-line defense, reordered by strength:\n(a) **PRIMARY — Simulation-based recovery** ✅ DONE (matched design verified): Probit latent model → binary, 100 replications × {50,100,200} items × {0.5-0.8} accuracy. **Strongest finding (matched 1,296-condition design): binary ρ=0.732 ≈ continuous ρ=0.741 at n=200 (Δ=0.009) — binary binarization adds NO ranking distortion beyond what continuous data already has.** Henderson I identifies item_id as #1 systematic source in 99-100% of runs. Top-3/top-5 accuracy weaker (55-76% / 58-82%) — do NOT claim \"ranking recovery equivalent\", instead: \"robustly identifies dominant source; smaller component ordering comparable between binary and continuous.\" **Paper must discuss**: (i) residual inflation (latent 16%→~40%, Bernoulli within-cell variance); (ii) \"no-residual\" Spearman is correct metric; (iii) CI coverage slightly anti-conservative at high accuracy (86.4% at p=0.8).\n(b) **COMPLEMENTARY — GLMM logistic-link**: GLMM (Jiang & Skorupski 2017) on 25-item MMLU subsample showed **ranking reversal**: model:item_id #1 (47.3%) > item_id #2 (22.8%) on logit scale, vs Henderson I item_id #1 (42.1%) > model:item_id #2 (33.6%). Spearman ρ=0.571, p=0.18 — rankings NOT statistically consistent. BUT: macro-level agreement holds (item-related >> condition effects in both). Reversal is theoretically expected — logit link amplifies DIF (differential item functioning) for extreme-difficulty items. **Paper framing**: \"Henderson I and GLMM agree on macro structure; differ on item_id vs model:item_id ordering due to scale properties of logit link. This is a complementary perspective, not a contradiction. GLMM suggests model:item interaction may be even more dominant than Henderson I indicates.\" Do NOT claim GLMM \"validates\" Henderson I.\n(c) **Bernoulli-adjusted decomposition**: ✅ DONE. Percentage decomposition inherently normalized by p(1-p) ceiling. Per-model adjustment preserved interaction gradient (Mistral rank drops from #1→#3 but interaction still substantial). Cross-accuracy resampling (0.62-0.72) shows item_id% stable (r=-0.048 with accuracy).\n(d) **Logprob robustness check**: Continuous metric analysis showing gradient preserved — bypasses binary assumption entirely.\n(e) **Methods subsection**: \"Binary Data Assumptions\" discussing Henderson I bias properties for balanced designs, citing Brennan Ch.12, Shavelson et al. 1989, Mushquash & O'Connor 2006, Lalor et al. 2019 (IRT on binary NLP data). Must note GLMM residual drops to 0.004% as Bernoulli variance absorbed by link function.\n\n### MD2. Fixed vs Random Facet Sensitivity\n**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.\n**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.\n\n### MD3. Separability Claim Scope\n**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).\n**Defense**: Qualify all separability claims as \"under binary scoring on knowledge-retrieval benchmarks.\" Present benchmark-conditional separability as a finding (not a limitation): \"separability itself varies across task types.\"\n\n### MD4. D-study Optimization Documentation\n**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).\n**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).\n\n### MD5. G-coefficient Interpretation\n**Issue**: G=0.22 for 200 items ≠ \"MMLU is unreliable\" (standard MMLU uses ~14K items).\n**Defense**: (a) Clearly distinguish \"G for our 200-item subsample design\" from \"reliability of full MMLU\"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as \"cost of subsampling\" rather than \"MMLU is broken.\"\n\n### MD6. Bootstrap Independence\n**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.\n**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.\n\n### MD7. IRT vs G-theory Comparison\n**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.\n**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the \"cost of multi-facet reliability\" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.\n\n### MD8. Cross-benchmark Design Asymmetry\n**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.\n**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.\n\n### MD9. Title-Content Alignment\n**Issue**: Title promises \"Evaluation Metrics\" but logprob analysis is minimal.\n**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to \"...Across Benchmarks and Models.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical, Ch.12 on binary data)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n- **Sclar et al. (2024, ICLR)** — Up to 76% accuracy swing from prompt formatting; directly relevant to prompt×item variance [Dream #3: all 3 tiers flagged as missing]\n- **Kunievsky & Evans (2025)** — Alternative decomposition: intent/articulation/model uncertainty; competing framework to G-theory [Dream #3: all 3 tiers flagged]\n- **Bui et al. (2025)** — Extreme seed sensitivity in fine-tuning (RTES variance=18.22 for RoBERTa on COPA) [Dream #3: relevant to exp-006]\n- **Jiang & Skorupski (2017)** — Logistic-link generalized G-theory for binary data [Dream #3 worst: methodological defense for REML on binary]\n- **Mushquash & O'Connor (2006)** — Binary-data G-theory [Dream #3: classical psychometrics gap]\n- **Shavelson et al. (1989)** — Binary response G-theory treatment [Dream #3: classical psychometrics]\n\n## Dream #3 Framing Directives (2026-05-21, D006)\nPost-analysis framing adjustments based on three-tier consistent feedback:\n1. **Center gradient + model×item as primary contributions** — infrastructure crossing is confirmatory secondary\n2. **Position explicitly as empirical extension of Mesting (2026)** with novel findings (model×item quantification, D-study out-of-sample validation, IRT comparison), not a new framework. Remove \"first\" claims where not defensible.\n3. **Scope Claim 2 to \"precision separability\"** — not \"infrastructure\" broadly. Single GPU architecture.\n4. **Item dominance is psychometrically expected** — contribution is quantification of magnitude, metric-conditionality, and D-study implications\n5. **Fine-tuning (exp-006) downgraded** to Discussion-section preliminary observation, not a numbered contribution\n6. **Add explicit judge-facet exclusion discussion** vs Mesting: we fix judge to isolate other factors; Mesting's 43.8% judge variance would dominate\n7. **Practitioner toolkit must be concrete**: specify released scripts, D-study calculator, budget lookup tables\n8. **Figures are non-negotiable**: 5 planned figures address all-tier \"zero figures\" criticism\n\n## Dream #4 Framing Directives (2026-05-21, D008)\nPost-analysis adjustments based on Dream #4 (best 7, median 6, worst 5):\n1. **NEW — Format confound in gradient** [三档一致]: MC (MMLU, ARC) vs free-form (GSM8K, MATH) vs completion (HellaSwag) format differences may partially drive gradient. Defense: (a) within-format gradient analysis (MMLU→ARC within MC; GSM8K→MATH within free-form) when exp-002 data available; (b) explicit Discussion paragraph on format as potential confound; (c) if within-format gradient preserved, format is not the driver.\n2. **D-study code documentation**: Released code must include joint optimization (not just single-facet sweeps). Fix before submission.\n3. **Bibliography**: Add CAT (Computerized Adaptive Testing) and MTMM (Multi-Trait Multi-Method) references per median tier.\n4. **Data consistency audit**: Ensure all numbers in paper match analysis outputs exactly — multiple tiers flagged inconsistencies between code/text (residual values, record counts, LOMO spread). Pre-submission checklist item.\n5. **Sclar et al. discrepancy**: Our prompt×item is 3.8-4.6% vs Sclar's 76% accuracy swing. Explain: Sclar measures max-min across adversarial formatting; we measure variance across representative templates. Different questions, compatible answers.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  registry_id: exp001_llama\n  description: 'Full-scale precision study: 4 models (Qwen3-8B, Llama-3.1-8B-Instruct,\n    Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3) × 3 precisions (FP32, BF16, FP16) × 6\n    prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified).\n    All precisions use consistent vLLM engine (V0 enforce_eager) to eliminate the\n    float32 engine confound found in MVP. Validates item dominance finding at scale\n    and with multiple models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 100\n  hardware: westd-32570 (RTX PRO 6000 96GB)\n  deps: []\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 239200\n    expected_records: 239200\n    conditions: 1196\n    items_per_condition: 200\n    overall_accuracy: 0.6814\n    accuracy_bfloat16: 0.7108\n    accuracy_float16: 0.7114\n    accuracy_float32: 0.604\n    accuracy_T0.0: 0.6987\n    accuracy_T0.3: 0.6795\n    accuracy_T0.7: 0.6699\n    null_predictions: 42\n    null_pct: 0\n- id: exp-001b\n  claim: 1\n  registry_id: exp001b_resampling\n  description: 'Item resampling stability test: 3 independent stratified samples of\n    200 MMLU items (seeds 0, 7, 99) × 1 model (Llama-3.1-8B-Instruct) × 3 precisions\n    × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether\n    the 58% item dominance finding is stable across different item draws from MMLU,\n    not an artifact of the specific 200-item sample. Critical for defending the headline\n    claim.\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 259200\n    samples: 3\n    records_per_sample: 86400\n    accuracy_sample1: 0.7207\n    accuracy_sample2: 0.6212\n    accuracy_sample3: 0.686\n    item_id_pct_mean: 74.48\n    item_id_pct_cv: 2.7\n    g_item_mean: 0.96\n    g_item_cv: 0.5\n    g_item_sample1: 0.9637\n    g_item_sample2: 0.962\n    g_item_sample3: 0.9548\n    min_items_g80_range: 31-38\n    seed_item_cv: 5.5\n    prompt_item_cv: 12.2\n    hypothesis_confirmed: true\n    g_item_corrected: 2026-05-21, ICC→Henderson I G coefficient\n- id: exp-002\n  claim: 1\n  registry_id: exp002_multi_benchmark\n  description: 'Multi-benchmark replication (D009 expanded): 8 models × 5 benchmarks\n    × BF16 × 2 temps × 6 prompts × 6 seeds × 4 orderings × 200 items each. Phase 1\n    (RUNNING): 4 original models × 4 benchmarks (MMLU/ARC/HellaSwag/GSM8K) on westd-32570.\n    Phase 2: + MATH as 5th benchmark (all models). Phase 3: + Yi-1.5-9B, OLMo-2-7B\n    on all 5 benchmarks (westd-15695). Phase 4: + InternLM2.5-7B, DeepSeek-7B on all\n    5 benchmarks. Validates cross-benchmark variance gradient, permutation test for\n    monotonicity, and benchmark-conditional D-study budgets.\n\n    '\n  priority: P0\n  gpu_budget_hours: 300\n  hardware: westd-32570 + westd-15695\n  deps:\n  - exp-001\n  status: RUNNING\n- id: exp-003\n  claim: 2\n  description: 'Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16,\n    FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. Tests\n    hardware × methodology interaction. Descoped from current priority — infrastructure\n    claim narrowed to \"precision separability\" per D003/D007. Would strengthen paper\n    if second GPU type becomes available.\n\n    '\n  priority: P1\n  gpu_budget_hours: 120\n  hardware: TBD (needs different GPU type)\n  deps: []\n  status: planned\n- id: exp-004\n  claim: 3\n  description: 'Comprehensive analysis of combined exp-001/001b/002/003 data. Includes:\n    (a) Model-as-facet G-theory reanalysis — treat model as crossed random facet to\n    properly attribute model×item interaction and reduce inflated item_id/residual\n    (Dream critical); (b) Bootstrap CIs (1000 resamples) on ALL variance components\n    in ALL tables, especially direct infra×method interaction term (Dream critical);\n    (c) D-study projections with CIs for optimal allocation across facets for G≥0.90/0.95/0.99,\n    with benchmark-specific budgets and comparison to IRT-based subsampling (tinyBenchmarks);\n    (d) REML vs Henderson Method I comparison as sensitivity analysis; (e) Logprob-based\n    scoring as third response variable; (f) Ranking stability analysis — does precision×temperature\n    interaction alter model rankings? (g) Higher-order interaction estimation to decompose\n    the residual component; (h) G-theory vs IRT direct comparison — same MMLU data,\n    D-study vs tinyBenchmarks IRT subsampling, compare recommended item counts and\n    discuss why G-theory is more conservative (accounts for prompt/seed dimensions\n    IRT ignores). First direct comparison in the literature; (i) Power analysis —\n    verify statistical power to detect ≥X% interaction effects given 5184×200 design\n    scale, preempt \"underpowered\" reviewer concern; (j) Practitioner evaluation protocol\n    guide (Discussion/Appendix); (k) Fixed vs random sensitivity — rerun G-study with\n    temperature/ordering as fixed facets, compare variance decomposition (MD2 defense);\n    (l) Binary data limitation analysis — correlate Bernoulli p(1-p) with observed\n    item variance, parallel binary vs text_exact_match analysis (MD1 defense); (m)\n    Bootstrap vs jackknife CI comparison — delete-1 jackknife as independence-safe\n    alternative, compare CI widths (MD6 defense); (n) Cross-benchmark design asymmetry\n    sensitivity — re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7),\n    compare with full 3×3 (MD8 defense); (o) G-coefficient at full benchmark size\n    — D-study projection to 14K MMLU items (MD5 defense); (p) Logprob-based scoring\n    across all benchmarks — expand from MMLU-only to all 5 benchmarks, support \"Evaluation\n    Metrics\" in title (MD9 defense); (q) GPU cost analysis — estimate compute cost\n    for recommended D-study budgets.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  hardware: none\n  deps:\n  - exp-001\n  - exp-002\n  status: planned\n- id: exp-005\n  claim: 2\n  description: '14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter\n    GPUs at BF16/FP16. Tests whether variance attribution patterns change with model\n    scale and architecture (dense vs reasoning-distilled).\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  hardware: TBD (needs ≥48GB VRAM per GPU)\n  deps:\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA. Fully crossed:\n    6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task\n    × 4 tasks = 1,728 total fine-tuning runs. Validates whether variance hierarchy\n    differs between inference and fine-tuning.\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  hardware: westd-32570 (RoBERTa-large fits easily on 96GB)\n  deps: []\n  status: planned\n- id: exp-007\n  claim: 2\n  description: 'Test LayerCast (FP16 storage + FP32 compute) as additional precision\n    condition on MMLU. Quantifies variance reduction from this mitigation strategy.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 1\n  description: 'MATH benchmark (200 items). Merged into exp-002 D009 expansion as\n    5th benchmark. No longer a standalone experiment.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  hardware: westd-32570\n  deps:\n  - exp-002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase_a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 5400\n    conditions: 108\n    overall_accuracy: 0.6557\n    accuracy_bfloat16: 0.6844\n    accuracy_float16: 0.6833\n    accuracy_float32: 0.5994\n    g_coefficient_correct: 0.357\n    top_variance_correct:\n      item_id: 0.5844\n      residual: 0.1759\n      precision:item_id: 0.0724\n      temperature:item_id: 0.0685\n      prompt_template:item_id: 0.0573\n    top_variance_text_match:\n      residual: 0.407\n      prompt_template:item_id: 0.375\n      temperature: 0.169\n      temperature:item_id: 0.025\n      precision:temperature: 0.013\n    pass_criteria_a_pipeline: true\n    pass_criteria_b_components: true\n    pass_criteria_c_interaction: true\n    pass_criteria_c_detail: precision:temperature 1.3% CI not containing zero (text_exact_match)\n- exp_id: bf16_eager_disentangle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bf16_v1_accuracy: 0.6844\n    bf16_eager_accuracy: 0.6822\n    fp32_v0_accuracy: 0.5994\n    engine_effect_pct: 2.6\n    precision_effect_pct: 97.4\n    engine_gap_pp: 0.22\n    precision_gap_pp: 8.28\n    total_gap_pp: 8.5\n- exp_id: exp001_pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 20000\n    expected_records: 20000\n    overall_accuracy: 0.616\n    gpu0_acc: 0.605\n    gpu1_acc: 0.622\n    gpu2_acc: 0.627\n    gpu3_acc: 0.61\n    avg_latency_ms: 180.9\n    output_size_mb: 13\n    precision_coverage: float32 only (100 conditions)\n    temperature_coverage: T=0.0 only (100 conditions)\n    fields_complete: true\n- exp_id: exp001_llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 239200\n    expected_records: 239200\n    conditions: 1196\n    items_per_condition: 200\n    overall_accuracy: 0.6814\n    accuracy_bfloat16: 0.7108\n    accuracy_float16: 0.7114\n    accuracy_float32: 0.604\n    accuracy_T0.0: 0.6987\n    accuracy_T0.3: 0.6795\n    accuracy_T0.7: 0.6699\n    null_predictions: 42\n    null_pct: 0\n- exp_id: exp001_gemma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 172800\n    bf16_records: 86400\n    fp32_records: 86400\n    fp16_records: 0\n    precisions_available:\n    - bfloat16\n    - float32\n    fp16_note: Gemma2 does not support float16 (vLLM numerical instability)\n    conditions_bf16: 432\n    conditions_fp32: 432\n    total_conditions: 864\n    items_per_condition: 200\n- exp_id: exp001_mistral\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 259200\n    expected_records: 259200\n    conditions: 1296\n    items_per_condition: 200\n    overall_accuracy: 0.6124\n    accuracy_bfloat16: null\n    accuracy_float16: null\n    accuracy_float32: null\n    precisions_available:\n    - bfloat16\n    - float16\n    - float32\n    per_precision_records: 86400\n    per_temperature_records: 86400\n- exp_id: exp001_qwen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 259200\n    overall_accuracy: 0.7252\n    accuracy_bf16: 0.726\n    accuracy_fp16: 0.7257\n    accuracy_fp32: 0.7235\n    unique_conditions: 1227\n    temperatures:\n    - 0\n    - 0.3\n    - 0.7\n- exp_id: exp001b_resampling\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 259200\n    samples: 3\n    records_per_sample: 86400\n    accuracy_sample1: 0.7207\n    accuracy_sample2: 0.6212\n    accuracy_sample3: 0.686\n    item_id_pct_mean: 74.48\n    item_id_pct_cv: 2.7\n    g_item_mean: 0.96\n    g_item_cv: 0.5\n    g_item_sample1: 0.9637\n    g_item_sample2: 0.962\n    g_item_sample3: 0.9548\n    min_items_g80_range: 31-38\n    seed_item_cv: 5.5\n    prompt_item_cv: 12.2\n    hypothesis_confirmed: true\n    g_item_corrected: 2026-05-21, ICC→Henderson I G coefficient\n- exp_id: exp002_multi_benchmark\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T12:24:56.851Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:24:56.851Z",
  "sessionId": "b609ec7e-7843-4d55-82de-38f83ed68c88"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-21T12:24:56.870Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

# Project context
project: nlp_variance_gtheory

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
**Completed robustness**: BF16-vs-FP16 sensitivity confirms precision→0.0006% without FP32 (FP32 is sole source of precision variance); leave-one-model-out (matched-spec) shows G_item range 0.747-0.793 across 3-model subsets (spread=0.046) — all below 0.80, confirming 4 models is the minimum for reliable cross-model measurement. LOMO also confirms item_id dominance and model×item as second-largest source are stable across all subsets.
**GLMM cross-check (dual-analysis, must report both)**: Two complementary analyses:
(i) *Marginal logit ANOVA*: All 7 grouped component rankings preserved exactly (ρ=1.0), consistent with MQL-1 prediction that logit-scaling is approximately constant at p̄=0.70.
(ii) *VB GLMM (25-item subsample)*: Ranking reversal on top-2 — model:item_id=47.3% > item_id=22.8% on logit scale (ρ=0.571, p=0.18). Attributable to model underspecification (missing 4 item-interaction terms in VB model) + subsample.
**Paper must present BOTH honestly** — "marginal logit ANOVA preserves all rankings; VB GLMM shows differences attributable to model underspecification." Do NOT overwrite ρ=0.571 with ρ=1.0. Implication: model×item interaction may be even more important than Henderson I indicates on logit scale — strengthens Claim 1's core message.

**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), "infrastructure" is currently limited to the precision facet.

**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent and temperature-conditional. Binary correct: G=0.611 (200 items), G≥0.80 requires ~510 items (all facets random) or ~414 items (practical: precision+temperature fixed). Text-exact-match: G=0.007 (temperature dominates at 79.7%), unreliable at any temperature >0. Temperature-stratified analysis reveals binary G degrades monotonically (T=0.0: 0.760 → T=0.7: 0.549). G-theory requires 3.6-4.4× more items than IRT (510 vs 116) because it accounts for prompt×item (4.6%), seed×item (4.7%), and residual (21.6%) dimensions that IRT ignores. Current practices (1 prompt, 1 seed, ≤200 items) yield G=0.611 — below the 0.80 threshold for dependable measurement.

## Contributions (4 条，明确区分)

1. **Model×item interaction as the hidden dominant source**: In a balanced 4-model design (345,600 records), model×item interaction (33.6%, CI [28.4-37.9%]) is the second-largest variance source, while item_id drops from 61% (single-model) to 42%. Item difficulty rankings are model-specific — single-model G-studies overestimate item dominance by conflating universal and model-specific difficulty. G_item=0.820 [0.782-0.861] with 4 models; D-study prediction validated out-of-sample (3-model predicted 0.816, actual 0.820, Δ=0.004). Reaching G≥0.90 requires ~10 models. [Note: position as quantification of a phenomenon expected from measurement theory, not as a surprising discovery. The novelty is the magnitude, the out-of-sample D-study validation, and the cross-model generalizability implications.]

2. **Precision separability with metric qualification**: Precision×methodology interactions are negligible under binary scoring (<0.1%), providing empirical support for isolated-factor studies. Under text-exact-match scoring, precision×temperature reaches 4.15%, consistent with floating-point non-associativity. Separability is confirmed as metric-conditional. [Note: scope to "numerical precision on single GPU architecture" — not "infrastructure" broadly. This is a confirmatory secondary finding, not a primary contribution. Pending BF16-vs-FP16 sensitivity to isolate FP32/vLLM confound.]

3. **IRT vs G-theory: the cost of multi-facet reliability**: The first empirical quantification of the multi-facet reliability cost for LLM evaluation: G-theory requires 3.6-4.4× more items than IRT (510 vs 116 for MMLU) because it accounts for prompt, seed, and ordering dimensions that IRT ignores. At IRT's recommended 116 items, G-theory G is only 0.529. This quantifies the "hidden cost" of evaluation dimensions invisible to IRT. [Note: keep as numbered contribution — Dream + Reviewer consensus this is one of the paper's strongest findings. Wording adjusted from "first direct comparison" to "first empirical quantification" per SF6 resolution.]

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
- **Leave-one-model-out stability**: All 3-model subsets preserve item_id dominance (39-45%) and model×item as second-largest (32-37%). G_item range 0.747-0.793 (spread=0.046), all below 0.80 — confirming 4 models is the minimum configuration for G≥0.80. This strengthens the D-study "need ~10 models for G≥0.90" prediction.

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
- **Model as crossed quasi-random facet**: In exp-001 analysis, model is treated as a crossed quasi-random facet — purposive sample from 4 major architecture families (Llama, Gemma, Mistral, Qwen), not a random draw from all LLMs. Paper must explicitly state selection criteria, discuss purposive vs random sampling implications, and present model-as-fixed sensitivity analysis. D-study Δ=0.004 out-of-sample prediction supports exchangeability assumption. Plan to add 2-3 models (Yi-1.5-9B, OLMo-2-7B, etc.) to strengthen to 6-7 models per MF2 resolution.
- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as "reduced crossing" rather than "fully crossed."
- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).

## Methodological Defenses (Dream #2 审稿问题逐条应对)

### MD1. Binary Data in G-theory
**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).
**Defense strategy (upgraded per Round 1 MF1 + Reviewer + GLMM results)**: Four-line defense, reordered by strength:
(a) **PRIMARY — Simulation-based recovery** ✅ DONE (matched design verified): Probit latent model → binary, 100 replications × {50,100,200} items × {0.5-0.8} accuracy. **Strongest finding (matched 1,296-condition design): binary ρ=0.732 ≈ continuous ρ=0.741 at n=200 (Δ=0.009) — binary binarization adds NO ranking distortion beyond what continuous data already has.** Henderson I identifies item_id as #1 systematic source in 99-100% of runs. Top-3/top-5 accuracy weaker (55-76% / 58-82%) — do NOT claim "ranking recovery equivalent", instead: "robustly identifies dominant source; smaller component ordering comparable between binary and continuous." **Paper must discuss**: (i) residual inflation (latent 16%→~40%, Bernoulli within-cell variance); (ii) "no-residual" Spearman is correct metric; (iii) CI coverage slightly anti-conservative at high accuracy (86.4% at p=0.8).
(b) **COMPLEMENTARY — GLMM logistic-link**: GLMM (Jiang & Skorupski 2017) on 25-item MMLU subsample showed **ranking reversal**: model:item_id #1 (47.3%) > item_id #2 (22.8%) on logit scale, vs Henderson I item_id #1 (42.1%) > model:item_id #2 (33.6%). Spearman ρ=0.571, p=0.18 — rankings NOT statistically consistent. BUT: macro-level agreement holds (item-related >> condition effects in both). Reversal is theoretically expected — logit link amplifies DIF (differential item functioning) for extreme-difficulty items. **Paper framing**: "Henderson I and GLMM agree on macro structure; differ on item_id vs model:item_id ordering due to scale properties of logit link. This is a complementary perspective, not a contradiction. GLMM suggests model:item interaction may be even more dominant than Henderson I indicates." Do NOT claim GLMM "validates" Henderson I.
(c) **Bernoulli-adjusted decomposition**: ✅ DONE. Percentage decomposition inherently normalized by p(1-p) ceiling. Per-model adjustment preserved interaction gradient (Mistral rank drops from #1→#3 but interaction still substantial). Cross-accuracy resampling (0.62-0.72) shows item_id% stable (r=-0.048 with accuracy).
(d) **Logprob robustness check**: Continuous metric analysis showing gradient preserved — bypasses binary assumption entirely.
(e) **Methods subsection**: "Binary Data Assumptions" discussing Henderson I bias properties for balanced designs, citing Brennan Ch.12, Shavelson et al. 1989, Mushquash & O'Connor 2006, Lalor et al. 2019 (IRT on binary NLP data). Must note GLMM residual drops to 0.004% as Bernoulli variance absorbed by link function.

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

## Dream #4 Framing Directives (2026-05-21, D008)
Post-analysis adjustments based on Dream #4 (best 7, median 6, worst 5):
1. **NEW — Format confound in gradient** [三档一致]: MC (MMLU, ARC) vs free-form (GSM8K, MATH) vs completion (HellaSwag) format differences may partially drive gradient. Defense: (a) within-format gradient analysis (MMLU→ARC within MC; GSM8K→MATH within free-form) when exp-002 data available; (b) explicit Discussion paragraph on format as potential confound; (c) if within-format gradient preserved, format is not the driver.
2. **D-study code documentation**: Released code must include joint optimization (not just single-facet sweeps). Fix before submission.
3. **Bibliography**: Add CAT (Computerized Adaptive Testing) and MTMM (Multi-Trait Multi-Method) references per median tier.
4. **Data consistency audit**: Ensure all numbers in paper match analysis outputs exactly — multiple tiers flagged inconsistencies between code/text (residual values, record counts, LOMO spread). Pre-submission checklist item.
5. **Sclar et al. discrepancy**: Our prompt×item is 3.8-4.6% vs Sclar's 76% accuracy swing. Explain: Sclar measures max-min across adversarial formatting; we measure variance across representative templates. Different questions, compatible answers.


## experiment_plan (with registry status)

- id: exp-001
  claim: 1
  registry_id: exp001_llama
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
- id: exp-001b
  claim: 1
  registry_id: exp001b_resampling
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
  status: DONE
  conclusion: success
  metrics:
    total_records: 259200
    samples: 3
    records_per_sample: 86400
    accuracy_sample1: 0.7207
    accuracy_sample2: 0.6212
    accuracy_sample3: 0.686
    item_id_pct_mean: 74.48
    item_id_pct_cv: 2.7
    g_item_mean: 0.96
    g_item_cv: 0.5
    g_item_sample1: 0.9637
    g_item_sample2: 0.962
    g_item_sample3: 0.9548
    min_items_g80_range: 31-38
    seed_item_cv: 5.5
    prompt_item_cv: 12.2
    hypothesis_confirmed: true
    g_item_corrected: 2026-05-21, ICC→Henderson I G coefficient
- id: exp-002
  claim: 1
  registry_id: exp002_multi_benchmark
  description: 'Multi-benchmark replication (D009 expanded): 8 models × 5 benchmarks
    × BF16 × 2 temps × 6 prompts × 6 seeds × 4 orderings × 200 items each. Phase 1
    (RUNNING): 4 original models × 4 benchmarks (MMLU/ARC/HellaSwag/GSM8K) on westd-32570.
    Phase 2: + MATH as 5th benchmark (all models). Phase 3: + Yi-1.5-9B, OLMo-2-7B
    on all 5 benchmarks (westd-15695). Phase 4: + InternLM2.5-7B, DeepSeek-7B on all
    5 benchmarks. Validates cross-benchmark variance gradient, permutation test for
    monotonicity, and benchmark-conditional D-study budgets.

    '
  priority: P0
  gpu_budget_hours: 300
  hardware: westd-32570 + westd-15695
  deps:
  - exp-001
  status: RUNNING
- id: exp-003
  claim: 2
  description: 'Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16,
    FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. Tests
    hardware × methodology interaction. Descoped from current priority — infrastructure
    claim narrowed to "precision separability" per D003/D007. Would strengthen paper
    if second GPU type becomes available.

    '
  priority: P1
  gpu_budget_hours: 120
  hardware: TBD (needs different GPU type)
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
  description: 'MATH benchmark (200 items). Merged into exp-002 D009 expansion as
    5th benchmark. No longer a standalone experiment.

    '
  priority: P0
  gpu_budget_hours: 0
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
- exp_id: exp001b_resampling
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_records: 259200
    samples: 3
    records_per_sample: 86400
    accuracy_sample1: 0.7207
    accuracy_sample2: 0.6212
    accuracy_sample3: 0.686
    item_id_pct_mean: 74.48
    item_id_pct_cv: 2.7
    g_item_mean: 0.96
    g_item_cv: 0.5
    g_item_sample1: 0.9637
    g_item_sample2: 0.962
    g_item_sample3: 0.9548
    min_items_g80_range: 31-38
    seed_item_cv: 5.5
    prompt_item_cv: 12.2
    hypothesis_confirmed: true
    g_item_corrected: 2026-05-21, ICC→Henderson I G coefficient
- exp_id: exp002_multi_benchmark
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-002
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "314690db-7ae2-4309-a558-5fa34aec647d",
  "type": "user",
  "uuid": "a1e64f36-31ed-414f-b635-3aa02ad30b24",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "b609ec7e-7843-4d55-82de-38f83ed68c88",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:24:56.869Z_

```json
{
  "parentUuid": "a1e64f36-31ed-414f-b635-3aa02ad30b24",
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
  "uuid": "c4e267b4-452a-4bfa-915d-631dbec44876",
  "timestamp": "2026-05-21T12:24:56.869Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "b609ec7e-7843-4d55-82de-38f83ed68c88",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:24:56.869Z_

```json
{
  "parentUuid": "c4e267b4-452a-4bfa-915d-631dbec44876",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f0ce5a49-7c40-4006-9b29-176fa3f2ab01",
  "timestamp": "2026-05-21T12:24:56.869Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "b609ec7e-7843-4d55-82de-38f83ed68c88",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "f0ce5a49-7c40-4006-9b29-176fa3f2ab01",
  "sessionId": "b609ec7e-7843-4d55-82de-38f83ed68c88"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for Dream LLM variance study",
  "sessionId": "b609ec7e-7843-4d55-82de-38f83ed68c88"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:25:28.855Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to define three tiers (best/median/worst) for a Dream simulation based on their research project on G-theory variance decomposition for LLM evaluation. Let me carefully analyze the project context to define meaningful, data-grounded tiers.

Key things to consider:
1. exp-001 is DONE with solid results (4 models, MMLU, 345,600 records)
2. exp-002 (multi-benchmark) is RUNNING - this is the critical unknown
3. The paper's primary novel contribution is the cross-benchmark variance gradient


4. Secondary contributions include quantifying model×item interactions, comparing against IRT approaches, and examining precision separability
5. I'm targeting AAAI 2027 in 9 weeks with ACL 2027 ARR as a backup at 21 weeks

The real differentiator between tiers hinges on what exp-002 reveals. I already have exp-001 locked down with item_id explaining 61.1% of variance in single-model contexts, dropping to 42.1% cross-model with model×item accounting for 33.6%, plus validated D-study predictions and precision separability findings under binary scoring.

For exp-002, the critical unknowns are whether cross-benchmark variance follows a clear monotonic pattern as difficulty increases, whether item_id dominance genuinely weakens moving from knowledge-focused benchmarks toward reasoning tasks, and whether format differences between multiple-choice and free-form responses can be isolated from the underlying effects. The best-case scenario would show exactly this pattern—a systematic decrease in item_id dominance across benchmarks while preserving within-format gradients, which would rule out format confounds entirely.

The median outcome involves a noisier gradient that doesn't cleanly monotonic, with format effects partially explaining the variance and potentially fewer models completing the full experiment. The worst case would show no meaningful cross-benchmark structure at all, forcing a reframe toward single-benchmark depth rather than the multi-benchmark narrative. I need to establish concrete metrics to distinguish between these scenarios: tracking the range of item_id percentages across benchmarks, testing gradient monotonicity statistically, and measuring how consistently model×item patterns replicate.

Looking at the exp-001 anchors from MMLU, I have solid baseline numbers—item_id sits around 42% in the cross-model case with a tight generalizability coefficient around 0.82. The core hypothesis is that item_id should decline as we move from knowledge-heavy tasks like MMLU toward reasoning-intensive ones like GSM8K and MATH, since reasoning problems tend to show more model-specific difficulty variation. Now I'm checking what the actual item_id ranges look like across the five benchmarks to see if that predicted gradient holds.

For the best-case tier, I'm looking for item_id dropping from roughly 42% at MMLU down to 15-25% at GSM8K, with a spread of at least 20 percentage points and a statistically significant monotonic trend. For the median tier, the gradient is weaker—maybe 42% down to 25-35%—with a 10-20 point spread and only a marginal trend. The worst tier shows overlapping item_id values across benchmarks with minimal gradient and no detectable monotonicity.

Now I'm thinking through D-study budgets and other metrics before I write out the YAML configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0ce5a49-7c40-4006-9b29-176fa3f2ab01",
  "isSidechain": false,
  "requestId": "req_011CbFi79avSRFEUBoLFYqFN",
  "type": "assistant",
  "uuid": "c94ccbc9-d6de-4391-9a61-ca6d2f99706e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "b609ec7e-7843-4d55-82de-38f83ed68c88",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNUn88Z7HKUWzqqP1zQZWt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18141,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18141,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3352,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18141
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

_source line 9 · 2026-05-21T12:26:08.839Z_

```yaml
tiers:
  best:
    meaning: "Cross-benchmark gradient clear and monotonic; all three claims validated with multi-benchmark + multi-model evidence; AAAI timeline feasible"
    key_assumptions:
      - "exp-002 completes Phase 1-3 (6+ models × 5 benchmarks) within 4 weeks"
      - "Item_id% decreases monotonically from knowledge-retrieval (MMLU/ARC) to multi-step reasoning (GSM8K/MATH), with ≥20pp spread"
      - "Within-format gradient preserved (MMLU > ARC within MC format; GSM8K shows lower item_id than HellaSwag), ruling out format confound as primary driver"
      - "Model×item interaction increases correspondingly on reasoning benchmarks, confirming model-conditional difficulty is task-type dependent"
      - "Precision separability holds across all benchmarks under binary scoring (<1%)"
      - "D-study budgets vary meaningfully across benchmarks (knowledge needs fewer items than reasoning), enabling benchmark-specific practitioner guidance"
    number_ranges:
      cross_benchmark_item_id_pct: ["MMLU ~42 → ARC ~35 → HellaSwag ~28 → GSM8K ~20 → MATH ~15"]
      gradient_spread_item_id_pp: [20, 30]
      gradient_monotonicity_perm_p: [0.001, 0.05]
      model_x_item_range_pct: ["MMLU ~34 → MATH ~45-55"]
      G_item_cross_model_range: ["MMLU 0.82 → MATH 0.60-0.70"]
      n_models_completed: [6, 8]
      n_benchmarks_completed: [5, 5]
      within_format_gradient_preserved: [true]
      precision_separability_all_benchmarks_binary: [0, 1.0]
      D_study_items_G80_range_across_benchmarks: [300, 800]
      exp002_phase_completion: ["Phase 1-3 done, Phase 4 partial"]
    narrative_direction: "Original framing holds — 'variance structure is benchmark-conditional, no universal reproducibility recipe.' Cross-benchmark gradient is the headline finding with permutation-tested monotonicity. Three numbered claims intact. Hook validated: single-benchmark G-studies (including our own exp-001) miss the task-type dependence. Figures 1-5 all populated with multi-benchmark data. AAAI submission on schedule."

  median:
    meaning: "Gradient exists but noisy/non-monotonic; format confound partially explanatory; claims require softened language and additional qualification"
    key_assumptions:
      - "exp-002 completes Phase 1-2 (4-5 models × 4-5 benchmarks) but Phase 3-4 delayed or incomplete"
      - "Item_id% varies across benchmarks (10-20pp spread) but ordering is not cleanly monotonic — e.g., HellaSwag breaks the knowledge→reasoning gradient"
      - "Format confound partially explains gradient: MC benchmarks cluster together vs free-form, but within-format gradient is weak or absent"
      - "Model×item interaction increases on some reasoning benchmarks but not consistently"
      - "Precision separability holds on 3-4 benchmarks but one benchmark shows unexpected interaction (2-5%)"
      - "D-study budgets vary but the variation is partially attributable to benchmark design differences (item count, difficulty distribution) rather than task type"
    number_ranges:
      cross_benchmark_item_id_pct: ["MMLU ~42 → ARC ~38 → HellaSwag ~30 → GSM8K ~25-32"]
      gradient_spread_item_id_pp: [10, 20]
      gradient_monotonicity_perm_p: [0.05, 0.25]
      model_x_item_range_pct: ["MMLU ~34 → GSM8K ~35-42"]
      G_item_cross_model_range: ["MMLU 0.82 → GSM8K 0.70-0.78"]
      n_models_completed: [4, 6]
      n_benchmarks_completed: [4, 5]
      within_format_gradient_preserved: ["weak or inconclusive"]
      precision_separability_all_benchmarks_binary: [0, 5.0]
      D_study_items_G80_range_across_benchmarks: [350, 650]
      exp002_phase_completion: ["Phase 1-2 done, Phase 3 partial"]
    narrative_direction: "Reframe gradient from 'monotonic task-type dependence' to 'benchmark-conditional variance structure with task-type as a partial predictor.' Claim 1 softened: 'item_id dominance and model×item interaction magnitudes vary across benchmarks, with task complexity as one moderating factor alongside format and difficulty distribution.' Add explicit analysis disentangling format vs task-type. Claim 2 adds caveat for anomalous benchmark. Claim 3 strengthened — budget variation across benchmarks makes benchmark-specific budgets even more necessary. Hook adjusted to 'variance structure varies across benchmarks, but the gradient is partially confounded with evaluation format.' Contribution 1 reweighted toward model×item quantification (already validated in exp-001) + benchmark variation (even if not monotonic). May need supplementary experiments or extended analysis → consider ACL ARR October cycle as insurance if AAAI writing timeline too tight."

  worst:
    meaning: "No systematic gradient; cross-benchmark variance structures are idiosyncratic; must reframe paper around single-benchmark depth + taxonomy of benchmark-specific structures"
    key_assumptions:
      - "exp-002 completes Phase 1 only (4 models × 3-4 benchmarks), Phase 2-4 blocked by compute or data issues"
      - "Item_id% does not vary systematically across benchmarks (<10pp spread), OR gradient is entirely explained by format confound (MC vs free-form)"
      - "Some benchmarks show pathological variance structures — e.g., GSM8K dominated by residual (>40%) due to stochastic generation, or model×item interaction negligible on ARC"
      - "Model×item interaction magnitude is benchmark-specific but unpredictable from task taxonomy"
      - "One or more benchmarks show convergence issues with Henderson I (near-zero components, negative REML estimates)"
      - "D-study budgets are wildly different across benchmarks but without interpretable pattern"
    number_ranges:
      cross_benchmark_item_id_pct: ["MMLU ~42 → others scattered 30-45, no clear ordering"]
      gradient_spread_item_id_pp: [0, 10]
      gradient_monotonicity_perm_p: [0.25, 1.0]
      model_x_item_range_pct: ["inconsistent, 15-40% across benchmarks without pattern"]
      G_item_cross_model_range: ["MMLU 0.82 → others 0.50-0.85 without trend"]
      n_models_completed: [4, 5]
      n_benchmarks_completed: [3, 4]
      within_format_gradient_preserved: [false]
      precision_separability_all_benchmarks_binary: [0, 8.0]
      D_study_items_G80_range_across_benchmarks: [200, 1200]
      exp002_phase_completion: ["Phase 1 done only"]
    narrative_direction: "Abandon gradient as headline. Reframe paper around two axes: (A) deep single-benchmark analysis (MMLU, exp-001 — already strong: model×item quantification, D-study validation, IRT comparison, full robustness package) + (B) 'benchmark-specific variance fingerprints' — each benchmark has a unique variance structure that cannot be predicted from task taxonomy alone, making benchmark-specific G-studies mandatory rather than optional. Hook flipped: 'not only is there no universal reproducibility recipe — there is no universal variance structure, and even task-type taxonomy fails to predict it.' This is still a publishable finding (arguably more surprising than a clean gradient), but requires rewriting intro and restructuring figures. Claim 1 narrowed to MMLU with exploratory multi-benchmark extension. Claim 2 unchanged (precision separability on MMLU). Claim 3 strengthened — benchmark-specific budgets are the ONLY viable approach. Primary contribution shifts from gradient discovery to: (i) model×item interaction quantification with D-study validation, (ii) IRT vs G-theory comparison, (iii) demonstration that variance structure is irreducibly benchmark-specific. Same venue target (AAAI), but likely needs ACL ARR timeline for rewriting."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c94ccbc9-d6de-4391-9a61-ca6d2f99706e",
  "isSidechain": false,
  "requestId": "req_011CbFi79avSRFEUBoLFYqFN",
  "type": "assistant",
  "uuid": "42075186-1d89-4a76-951f-0023ca90a1d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "b609ec7e-7843-4d55-82de-38f83ed68c88",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VNUn88Z7HKUWzqqP1zQZWt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18141,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18141,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3352,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18141
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "42075186-1d89-4a76-951f-0023ca90a1d0",
  "sessionId": "b609ec7e-7843-4d55-82de-38f83ed68c88"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for Dream LLM variance study",
  "sessionId": "b609ec7e-7843-4d55-82de-38f83ed68c88"
}
```

---
