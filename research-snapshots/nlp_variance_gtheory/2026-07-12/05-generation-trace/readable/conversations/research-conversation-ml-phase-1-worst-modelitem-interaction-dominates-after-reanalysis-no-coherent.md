# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Model×item interaction dominates after reanalysis; no coherent benchmark gr

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/292233c5-030e-414e-8dcf-2522550c6441.jsonl`
- **Structured JSON:** [`f565d2a529b5645d94b1.json`](../../sessions/f5/f565d2a529b5645d94b1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:59:34.707Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:59:34.707Z",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Model×item interaction dominates after reanalysis; no coherent benchmark gradient; separability fails broadly\n核心假设：['Model×item interaction becomes largest or co-largest source after model-as-facet reanalysis (item_id <28%, model×item >25%)', 'No systematic cross-benchmark gradient — variance structure is idiosyncratic per benchmark, not predictable from task type', 'Separability fails on 2+ benchmarks under binary scoring (infra×method >3%), undermining the confirmatory null', 'Gemma fully excluded; potential issues with second model reduce effective coverage to 2-3 models', \"exp-003 hardware unavailable or results show GPU×method interaction >2%, breaking the 'precision only' scoping\", 'Bootstrap CIs are wide (>12pp), making it impossible to rank-order variance sources with confidence on several benchmarks', 'D-study budgets are implausibly large (>1000 items) or vary so much across benchmarks that no actionable recommendation emerges']\n关键指标范围：{'item_id_pct_mmlu_model_as_facet': [15, 28], 'model_x_item_pct_mmlu': [25, 40], 'item_id_pct_gsm8k': [8, 18], 'cross_benchmark_gradient_pp': [0, 8], 'direct_infra_x_method_binary_max': [2.0, 8.0], 'direct_infra_x_method_text_match_max': [4.0, 12.0], 'g_coeff_binary_mmlu_200item': [0.15, 0.28], 'g_coeff_text_match_mmlu_200item': [0.82, 0.93], 'd_study_items_for_g90_mmlu_binary': [800, 2000], 'benchmarks_with_complete_data': [2, 3], 'models_with_complete_data': [2, 3], 'bootstrap_ci_width_item_id_pp': [10, 20]}\n叙事方向：Core framing (\"item dominance + benchmark gradient\") collapses. Reframe around: \"Model×item interaction is the hidden dominant variance source in LLM evaluation — items that are easy for one model are hard for another, and this interaction, not item difficulty alone, drives irreproducibility.\" This is actually a STRONGER and more surprising finding than item dominance (which reviewers flagged as psychometrically obvious). New headline: \"The model×item interaction problem — why benchmark scores are not commensurable across models without accounting for differential item functioning.\" Separability failure becomes a positive finding: \"isolated-factor studies are insufficient; infrastructure and methodology interact in ways that single-factor designs cannot detect.\" D-study contribution pivots to: \"current evaluation practices are even more inadequate than prior work suggests — reliability requires joint optimization across more facets than any existing recommendation accounts for.\" Drop the gradient narrative entirely; replace with \"variance structure is benchmark-specific and unpredictable from task taxonomy alone, requiring per-benchmark calibration.\" The paper becomes more iconoclastic (nothing is simple, everything interacts) which can work at AAAI if the empirical evidence is clean. Risk: the story is harder to sell without a tidy gradient, so writing must be exceptionally clear. ACL ARR (October) becomes the realistic primary target to allow time for the reframing.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: nlp_variance_gtheory\n\n## paper_framing.md\n\n# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation (MVP: 58.4% on MMLU single-model; expected to decrease with model-as-facet reanalysis). Its magnitude is hypothesized to be benchmark-dependent — weakening on reasoning tasks where temperature/seed interactions increase — but this gradient requires exp-002 confirmation. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating whether a systematic benchmark-dependent gradient exists, and (c) deriving D-study implications specific to LLM evaluation.\n**Fallback narratives**: (A) If gradient confirmed → \"benchmark-conditional variance structure\"; (B) If gradient not significant → \"item dominance is universal but magnitude varies\"; (C) If model-as-facet reduces item_id below 30% → pivot to \"model×item interaction is the dominant source\" — narrative direction changes substantially.\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.\n\n## Contributions (3 条，明确区分)\n\n1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\n\n2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.\n\n3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (X-Y%, benchmark-dependent [placeholder: fill after exp-001/002]), while direct infrastructure×methodology interactions are negligible. Variance structure [is/is not] benchmark-conditional [pending exp-002]. D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (4 figures minimum):\n  1. Problem illustration: same model, different benchmark → different dominant variance source\n  2. G-theory facet diagram showing crossed design\n  3. Stacked-bar variance decomposition across benchmarks (signature figure)\n  4. D-study projection curves: G vs item count for different benchmarks\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).\n\n## Methodological Defenses (Dream #2 审稿问题逐条应对)\n\n### MD1. Binary Data in G-theory\n**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).\n**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is \"mechanical\" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.\n\n### MD2. Fixed vs Random Facet Sensitivity\n**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.\n**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.\n\n### MD3. Separability Claim Scope\n**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).\n**Defense**: Qualify all separability claims as \"under binary scoring on knowledge-retrieval benchmarks.\" Present benchmark-conditional separability as a finding (not a limitation): \"separability itself varies across task types.\"\n\n### MD4. D-study Optimization Documentation\n**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).\n**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).\n\n### MD5. G-coefficient Interpretation\n**Issue**: G=0.22 for 200 items ≠ \"MMLU is unreliable\" (standard MMLU uses ~14K items).\n**Defense**: (a) Clearly distinguish \"G for our 200-item subsample design\" from \"reliability of full MMLU\"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as \"cost of subsampling\" rather than \"MMLU is broken.\"\n\n### MD6. Bootstrap Independence\n**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.\n**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.\n\n### MD7. IRT vs G-theory Comparison\n**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.\n**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the \"cost of multi-facet reliability\" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.\n\n### MD8. Cross-benchmark Design Asymmetry\n**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.\n**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.\n\n### MD9. Title-Content Alignment\n**Issue**: Title promises \"Evaluation Metrics\" but logprob analysis is minimal.\n**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to \"...Across Benchmarks and Models.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Full-scale precision study: 4 models (Qwen3-8B, Llama-3.1-8B-Instruct,\n    Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3) × 3 precisions (FP32, BF16, FP16) × 6\n    prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified).\n    All precisions use consistent vLLM engine (V0 enforce_eager) to eliminate the\n    float32 engine confound found in MVP. Validates item dominance finding at scale\n    and with multiple models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 100\n  hardware: westd-32570 (RTX PRO 6000 96GB)\n  deps: []\n  status: planned\n- id: exp-001b\n  claim: 1\n  description: 'Item resampling stability test: 3 independent stratified samples of\n    200 MMLU items (seeds 0, 7, 99) × 1 model (Llama-3.1-8B-Instruct) × 3 precisions\n    × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether\n    the 58% item dominance finding is stable across different item draws from MMLU,\n    not an artifact of the specific 200-item sample. Critical for defending the headline\n    claim.\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Multi-benchmark replication: same 4 models × BF16/FP16 × 6 prompts\n    × 6 seeds × 2 temperatures × 4 orderings on GSM8K (200 items), ARC-Challenge (200\n    items), HellaSwag (200 items). Tests whether item dominance and separability hold\n    across task types (math reasoning, science reasoning, commonsense).\n\n    '\n  priority: P0\n  gpu_budget_hours: 200\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-003\n  claim: 2\n  description: 'Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16,\n    FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. Tests\n    hardware × methodology interaction — the core separability question that MVP couldn''t\n    address with only 1 GPU type.\n\n    '\n  priority: P0\n  gpu_budget_hours: 120\n  hardware: westd-32570 + TBD (second GPU type from Manager)\n  deps: []\n  status: planned\n- id: exp-004\n  claim: 3\n  description: 'Comprehensive analysis of combined exp-001/001b/002/003 data. Includes:\n    (a) Model-as-facet G-theory reanalysis — treat model as crossed random facet to\n    properly attribute model×item interaction and reduce inflated item_id/residual\n    (Dream critical); (b) Bootstrap CIs (1000 resamples) on ALL variance components\n    in ALL tables, especially direct infra×method interaction term (Dream critical);\n    (c) D-study projections with CIs for optimal allocation across facets for G≥0.90/0.95/0.99,\n    with benchmark-specific budgets and comparison to IRT-based subsampling (tinyBenchmarks);\n    (d) REML vs Henderson Method I comparison as sensitivity analysis; (e) Logprob-based\n    scoring as third response variable; (f) Ranking stability analysis — does precision×temperature\n    interaction alter model rankings? (g) Higher-order interaction estimation to decompose\n    the residual component; (h) G-theory vs IRT direct comparison — same MMLU data,\n    D-study vs tinyBenchmarks IRT subsampling, compare recommended item counts and\n    discuss why G-theory is more conservative (accounts for prompt/seed dimensions\n    IRT ignores). First direct comparison in the literature; (i) Power analysis —\n    verify statistical power to detect ≥X% interaction effects given 5184×200 design\n    scale, preempt \"underpowered\" reviewer concern; (j) Practitioner evaluation protocol\n    guide (Discussion/Appendix); (k) Fixed vs random sensitivity — rerun G-study with\n    temperature/ordering as fixed facets, compare variance decomposition (MD2 defense);\n    (l) Binary data limitation analysis — correlate Bernoulli p(1-p) with observed\n    item variance, parallel binary vs text_exact_match analysis (MD1 defense); (m)\n    Bootstrap vs jackknife CI comparison — delete-1 jackknife as independence-safe\n    alternative, compare CI widths (MD6 defense); (n) Cross-benchmark design asymmetry\n    sensitivity — re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7),\n    compare with full 3×3 (MD8 defense); (o) G-coefficient at full benchmark size\n    — D-study projection to 14K MMLU items (MD5 defense); (p) Logprob-based scoring\n    across all benchmarks — expand from MMLU-only to all 5 benchmarks, support \"Evaluation\n    Metrics\" in title (MD9 defense); (q) GPU cost analysis — estimate compute cost\n    for recommended D-study budgets.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  hardware: none\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  status: planned\n- id: exp-005\n  claim: 2\n  description: '14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter\n    GPUs at BF16/FP16. Tests whether variance attribution patterns change with model\n    scale and architecture (dense vs reasoning-distilled).\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  hardware: TBD (needs ≥48GB VRAM per GPU)\n  deps:\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA. Fully crossed:\n    6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task\n    × 4 tasks = 1,728 total fine-tuning runs. Validates whether variance hierarchy\n    differs between inference and fine-tuning.\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  hardware: westd-32570 (RoBERTa-large fits easily on 96GB)\n  deps: []\n  status: planned\n- id: exp-007\n  claim: 2\n  description: 'Test LayerCast (FP16 storage + FP32 compute) as additional precision\n    condition on MMLU. Quantifies variance reduction from this mitigation strategy.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 1\n  description: 'MATH benchmark (200 items) — tests whether item dominance pattern\n    differs for reasoning-heavy tasks where chain-of-thought introduces additional\n    variance.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  hardware: westd-32570\n  deps:\n  - exp-002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase_a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 5400\n    conditions: 108\n    overall_accuracy: 0.6557\n    accuracy_bfloat16: 0.6844\n    accuracy_float16: 0.6833\n    accuracy_float32: 0.5994\n    g_coefficient_correct: 0.357\n    top_variance_correct:\n      item_id: 0.5844\n      residual: 0.1759\n      precision:item_id: 0.0724\n      temperature:item_id: 0.0685\n      prompt_template:item_id: 0.0573\n    top_variance_text_match:\n      residual: 0.407\n      prompt_template:item_id: 0.375\n      temperature: 0.169\n      temperature:item_id: 0.025\n      precision:temperature: 0.013\n    pass_criteria_a_pipeline: true\n    pass_criteria_b_components: true\n    pass_criteria_c_interaction: true\n    pass_criteria_c_detail: precision:temperature 1.3% CI not containing zero (text_exact_match)\n- exp_id: bf16_eager_disentangle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bf16_v1_accuracy: 0.6844\n    bf16_eager_accuracy: 0.6822\n    fp32_v0_accuracy: 0.5994\n    engine_effect_pct: 2.6\n    precision_effect_pct: 97.4\n    engine_gap_pp: 0.22\n    precision_gap_pp: 8.28\n    total_gap_pp: 8.5\n- exp_id: exp001_pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 20000\n    expected_records: 20000\n    overall_accuracy: 0.616\n    gpu0_acc: 0.605\n    gpu1_acc: 0.622\n    gpu2_acc: 0.627\n    gpu3_acc: 0.61\n    avg_latency_ms: 180.9\n    output_size_mb: 13\n    precision_coverage: float32 only (100 conditions)\n    temperature_coverage: T=0.0 only (100 conditions)\n    fields_complete: true\n- exp_id: exp001_llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 239200\n    expected_records: 239200\n    conditions: 1196\n    items_per_condition: 200\n    overall_accuracy: 0.6814\n    accuracy_bfloat16: 0.7108\n    accuracy_float16: 0.7114\n    accuracy_float32: 0.604\n    accuracy_T0.0: 0.6987\n    accuracy_T0.3: 0.6795\n    accuracy_T0.7: 0.6699\n    null_predictions: 42\n    null_pct: 0\n- exp_id: exp001_gemma\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T03:59:34.711Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:59:34.711Z",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T03:59:34.766Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Model×item interaction dominates after reanalysis; no coherent benchmark gradient; separability fails broadly
核心假设：['Model×item interaction becomes largest or co-largest source after model-as-facet reanalysis (item_id <28%, model×item >25%)', 'No systematic cross-benchmark gradient — variance structure is idiosyncratic per benchmark, not predictable from task type', 'Separability fails on 2+ benchmarks under binary scoring (infra×method >3%), undermining the confirmatory null', 'Gemma fully excluded; potential issues with second model reduce effective coverage to 2-3 models', "exp-003 hardware unavailable or results show GPU×method interaction >2%, breaking the 'precision only' scoping", 'Bootstrap CIs are wide (>12pp), making it impossible to rank-order variance sources with confidence on several benchmarks', 'D-study budgets are implausibly large (>1000 items) or vary so much across benchmarks that no actionable recommendation emerges']
关键指标范围：{'item_id_pct_mmlu_model_as_facet': [15, 28], 'model_x_item_pct_mmlu': [25, 40], 'item_id_pct_gsm8k': [8, 18], 'cross_benchmark_gradient_pp': [0, 8], 'direct_infra_x_method_binary_max': [2.0, 8.0], 'direct_infra_x_method_text_match_max': [4.0, 12.0], 'g_coeff_binary_mmlu_200item': [0.15, 0.28], 'g_coeff_text_match_mmlu_200item': [0.82, 0.93], 'd_study_items_for_g90_mmlu_binary': [800, 2000], 'benchmarks_with_complete_data': [2, 3], 'models_with_complete_data': [2, 3], 'bootstrap_ci_width_item_id_pp': [10, 20]}
叙事方向：Core framing ("item dominance + benchmark gradient") collapses. Reframe around: "Model×item interaction is the hidden dominant variance source in LLM evaluation — items that are easy for one model are hard for another, and this interaction, not item difficulty alone, drives irreproducibility." This is actually a STRONGER and more surprising finding than item dominance (which reviewers flagged as psychometrically obvious). New headline: "The model×item interaction problem — why benchmark scores are not commensurable across models without accounting for differential item functioning." Separability failure becomes a positive finding: "isolated-factor studies are insufficient; infrastructure and methodology interact in ways that single-factor designs cannot detect." D-study contribution pivots to: "current evaluation practices are even more inadequate than prior work suggests — reliability requires joint optimization across more facets than any existing recommendation accounts for." Drop the gradient narrative entirely; replace with "variance structure is benchmark-specific and unpredictable from task taxonomy alone, requiring per-benchmark calibration." The paper becomes more iconoclastic (nothing is simple, everything interacts) which can work at AAAI if the empirical evidence is clean. Risk: the story is harder to sell without a tidy gradient, so writing must be exceptionally clear. ACL ARR (October) becomes the realistic primary target to allow time for the reframing.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

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

**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation (MVP: 58.4% on MMLU single-model; expected to decrease with model-as-facet reanalysis). Its magnitude is hypothesized to be benchmark-dependent — weakening on reasoning tasks where temperature/seed interactions increase — but this gradient requires exp-002 confirmation. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating whether a systematic benchmark-dependent gradient exists, and (c) deriving D-study implications specific to LLM evaluation.
**Fallback narratives**: (A) If gradient confirmed → "benchmark-conditional variance structure"; (B) If gradient not significant → "item dominance is universal but magnitude varies"; (C) If model-as-facet reduces item_id below 30% → pivot to "model×item interaction is the dominant source" — narrative direction changes substantially.

**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), "infrastructure" is currently limited to the precision facet.

**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.

## Contributions (3 条，明确区分)

1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.

2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.

3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).

## Story Spine

**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.

**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.

**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.

**Headline result template**: "In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (X-Y%, benchmark-dependent [placeholder: fill after exp-001/002]), while direct infrastructure×methodology interactions are negligible. Variance structure [is/is not] benchmark-conditional [pending exp-002]. D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional."

## Hook (Counter-Intuitive Quantified Claim)
"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory."

## Narrative Strategy
- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)
- **Tension**: "No universal recipe" — the field seeks standardization but variance structure varies qualitatively across task types
- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)
- **Figure plan** (4 figures minimum):
  1. Problem illustration: same model, different benchmark → different dominant variance source
  2. G-theory facet diagram showing crossed design
  3. Stacked-bar variance decomposition across benchmarks (signature figure)
  4. D-study projection curves: G vs item count for different benchmarks
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
- Brennan (2001) — G-theory textbook (canonical)
- Lu et al. (2022) — Option ordering effects in MC evaluation
- Pezeshkpour & Hruschka (2024) — Option ordering effects
- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)
- Sellam et al. (2022) — MultiBERTs, multi-seed training
- Dehghani et al. (2021) — Benchmark Lottery
- Biderman et al. (2024) — Evaluation reproducibility lessons
- Vania et al. (2021) — IRT item properties in NLP


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
  conclusion: failed
  metrics: {}

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
  "promptId": "bdba9cf9-9251-417b-9543-5c0bd74fb35c",
  "type": "user",
  "uuid": "ee6ffc6f-26ed-447a-bb13-581b727e50df",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:59:34.764Z_

```json
{
  "parentUuid": "ee6ffc6f-26ed-447a-bb13-581b727e50df",
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
  "uuid": "af4338f4-11a2-47c8-a92a-15abab37c0cb",
  "timestamp": "2026-05-21T03:59:34.764Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:59:34.764Z_

```json
{
  "parentUuid": "af4338f4-11a2-47c8-a92a-15abab37c0cb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d2309023-399d-47e6-9aa3-8c69db5bb9ac",
  "timestamp": "2026-05-21T03:59:34.764Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Model×item interaction dominates after reanalysis; no coherent benchmark gradient; separability fails broadly 核心假设：['Model×item interaction becomes larges…",
  "leafUuid": "d2309023-399d-47e6-9aa3-8c69db5bb9ac",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Model×item interaction dominance with benchmark-specific variance structures",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441"
}
```

---

### Assistant

_source line 8 · 2026-05-21T04:00:05.696Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, under the "worst" tier scenario. Let me carefully analyze the worst tier definition and generate predictions for each experiment.

Let me re-read the worst tier definition:

**Worst tier meaning**: Model×item interaction dominates after reanalysis; no coherent benchmark gradient; separability fails broadly

**Core assumptions**:
1. Model×item interaction becomes largest or co-largest source after model-as-facet reanalysis (item_id <28%, model×item >25%)
2. No systematic cross-benchmark gradient — variance structure is idiosyncratic per benchmark


3. Separability breaks down on 2+ benchmarks with binary scoring (infra×method >3%)
4. Gemma gets fully excluded; second model issues reduce effective coverage to 2-3 models
5. exp-003 hardware constraints or GPU×method interactions >2% emerge
6. Bootstrap confidence intervals widen substantially (>12pp), preventing reliable ranking of variance sources
7. D-study budgets become unrealistic (>1000 items) or show extreme cross-benchmark variation

I'm now looking at the specific metric ranges that define this worst scenario across the benchmarks. I'm seeing the parameter ranges continue, and now the narrative is shifting—the model-by-item interaction is actually the real driver of variance, not the gradient effects I was tracking. The separability failure turns into something more interesting: it suggests the measurement problem is even worse than prior work indicated. For exp-001, I'm running a full precision study across MMLU with multiple models, prompts, seeds, and temperatures, but when I reanalyze treating model as a facet rather than a nuisance factor, the item dominance effect drops sharply, which changes the whole story. The remaining experiments show similar patterns of instability—the 14B model variant reveals different variance structures at scale, fine-tuning experiments lack a consistent hierarchy, LayerCast provides minimal variance reduction as a mitigation strategy, and the MATH benchmark introduces yet another idiosyncratic pattern. Now I'm constructing the detailed YAML output for each experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2309023-399d-47e6-9aa3-8c69db5bb9ac",
  "isSidechain": false,
  "requestId": "req_011CbF3ZyhKNU7iVuiAtGLCr",
  "type": "assistant",
  "uuid": "34a23d74-9501-41ed-98af-c37d6490a0a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMfXnfgXGtjQK5BmaTcgNY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13762,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14610,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14610,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13762
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

_source line 9 · 2026-05-21T04:04:51.976Z_

```yaml
tier: worst
narrative_guidance: >
  Core framing ("item dominance + benchmark gradient") collapses. Reframe around:
  "Model×item interaction is the hidden dominant variance source in LLM evaluation —
  items that are easy for one model are hard for another, and this interaction, not
  item difficulty alone, drives irreproducibility." Separability failure becomes a
  positive finding: isolated-factor studies are insufficient. D-study pivots to
  "current evaluation practices are even more inadequate than prior work suggests."
  Drop the gradient narrative entirely; replace with "variance structure is
  benchmark-specific and unpredictable from task taxonomy alone." The paper becomes
  more iconoclastic. ACL ARR October becomes realistic primary target.

imagined_experiments:
  - name: "exp-001 Full-Scale Precision Study (MMLU)"
    plan_id: "exp-001"
    description: >
      4 models × 3 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items.
      Gemma-2-9B-IT fails during FP16 runs (known from registry: exp001_gemma FAILED).
      Qwen3-8B produces sporadic decoding anomalies under FP32 at T=0.7, requiring
      partial reruns. Final dataset covers 3 models (Llama, Mistral, Qwen) with Gemma
      fully excluded, yielding 3 × 1296 = 3888 conditions × 200 items = 777,600 records.
    expected_results:
      total_records: 777600
      models_completed: 3
      models_excluded: 1  # Gemma
      conditions_per_model: 1296
      items_per_condition: 200
      overall_accuracy_llama: 0.681
      overall_accuracy_mistral: 0.623
      overall_accuracy_qwen: 0.704
      accuracy_bfloat16_pooled: 0.680
      accuracy_float16_pooled: 0.678
      accuracy_float32_pooled: 0.611
      float32_degradation_pp: 6.8
      null_predictions_pct: 0.03
      # Single-model G-study (per-model, pre-reanalysis)
      item_id_pct_llama_single: 0.561
      item_id_pct_mistral_single: 0.534
      item_id_pct_qwen_single: 0.589
      residual_pct_llama_single: 0.182
      residual_pct_mistral_single: 0.197
      residual_pct_qwen_single: 0.168
      g_coeff_binary_llama_200item: 0.362
      g_coeff_binary_mistral_200item: 0.338
      g_coeff_binary_qwen_200item: 0.371
      g_coeff_text_match_llama_200item: 0.968
      precision_x_temperature_text_match_llama_pct: 1.5
      precision_x_temperature_text_match_mistral_pct: 1.8
    result_rationale: >
      Single-model analyses replicate MVP findings: item_id dominates at 53-59% per model,
      consistent with Bernoulli variance spread across 200 items of heterogeneous difficulty.
      FP32 degradation (~6.8pp) replicates the V0 enforce_eager-controlled pattern from
      bf16_eager_disentangle. These per-model results look encouraging — item dominance
      appears stable. But this is misleading: the residual component (17-20%) is inflated
      because model×item interaction is confounded with residual when model is not a facet.
      The true picture emerges only in exp-004 reanalysis. Gemma exclusion reduces the
      model universe from 4 to 3, weakening generalizability claims and inviting reviewer
      criticism about restricted model coverage. Qwen FP32 anomalies at T=0.7 suggest
      architecture-specific precision sensitivity, foreshadowing the idiosyncratic
      variance patterns that dominate the worst-tier narrative.
    tables:
      - name: "Table 1: Single-Model Variance Decomposition (MMLU, 200 items, binary scoring)"
        description: >
          Rows: variance sources (item_id, prompt, seed, temperature, ordering, precision,
          all 2-way interactions, residual). Columns: Llama, Mistral, Qwen, Pooled.
          Shows item_id dominant at 53-59% across all 3 models. Residual inflated at 17-20%.
          Precision×temperature interaction 0.3-0.5% under binary, 1.5-1.8% under text_match.
      - name: "Table 2: Accuracy Summary by Precision × Temperature × Model"
        description: >
          3×3×3 table. FP32 degradation visible across all models (5.5-8.5pp). Temperature
          effect modest (T=0.0 vs T=0.7: 2-3pp). Cross-model accuracy spread: 8pp.
    figures_description:
      - "Accuracy heatmap (3 models × 3 precisions × 3 temperatures). FP32 row visibly darker. Model ranking preserved across conditions but gap varies."
      - "Item-level accuracy distributions per model: overlapping but offset histograms showing each model has distinct difficulty profile for the same 200 items."
    analysis: >
      Data collection succeeds for 3/4 models. Per-model G-studies replicate MVP item
      dominance finding. However, item-level correlation between models is only r=0.71-0.78
      (not r=0.90+), foreshadowing large model×item interaction in the facet reanalysis.
      The single-model framing looks solid at this stage but will collapse in exp-004.

  - name: "exp-001b Item Resampling Stability"
    plan_id: "exp-001b"
    description: >
      3 independent stratified 200-item MMLU samples (seeds 0, 7, 99) × Llama × 3
      precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample.
      Tests whether item_id dominance percentage is stable across item draws.
    expected_results:
      total_records_per_sample: 10800
      total_records: 32400
      item_id_pct_sample_seed0: 0.541
      item_id_pct_sample_seed7: 0.612
      item_id_pct_sample_seed99: 0.487
      item_id_range_pp: 12.5
      residual_pct_range: [0.155, 0.221]
      g_coeff_binary_seed0: 0.341
      g_coeff_binary_seed7: 0.389
      g_coeff_binary_seed99: 0.312
      g_coeff_range_pp: 7.7
      item_difficulty_mean_seed0: 0.683
      item_difficulty_mean_seed7: 0.671
      item_difficulty_mean_seed99: 0.698
      item_difficulty_sd_seed0: 0.284
      item_difficulty_sd_seed7: 0.301
      item_difficulty_sd_seed99: 0.262
    result_rationale: >
      The 12.5pp range in item_id percentage across three samples (48.7-61.2%) is
      uncomfortably wide. This is driven by differential item difficulty variance:
      sample seed99 has lower difficulty SD (0.262 vs 0.301), mechanically reducing
      Bernoulli p(1-p) spread and thus item_id's share. This directly validates the
      MD1 concern — item_id percentage is partly a mechanical artifact of the item
      difficulty distribution in the sample, not a stable psychometric property. The
      instability makes it impossible to report a single "item_id = X%" headline number
      with confidence. In the worst tier, this is compounded by the fact that model×item
      interaction (not measurable in single-model exp-001b) will further erode whatever
      item_id estimate survives. Bootstrap CIs on item_id will be wide (±6-8pp per sample),
      and the cross-sample range exceeds the within-sample CI, indicating genuine
      instability rather than sampling noise alone.
    tables:
      - name: "Table 3: Variance Decomposition Stability Across Item Samples"
        description: >
          Rows: variance sources. Columns: Sample A (seed0), Sample B (seed7), Sample C
          (seed99), Range. Item_id ranges 48.7-61.2%. Residual ranges 15.5-22.1%.
          Prompt×item ranges 4.8-7.2%. Instability is systematic, not random.
    figures_description:
      - "Three-panel stacked bar chart showing variance decomposition for each item sample. Visible structural differences despite identical design and model."
      - "Scatter plot: item difficulty SD vs item_id percentage across samples, showing positive correlation (mechanical Bernoulli link)."
    analysis: >
      Item dominance magnitude is sample-dependent, with a 12.5pp range across three
      draws. This is a serious threat to the headline claim. The Bernoulli variance
      mechanism (MD1) explains ~60% of the cross-sample variation. Combined with the
      model×item interaction finding from exp-004, the "item dominance" narrative becomes
      untenable as a clean headline. The paper must reframe: item_id is large but its
      magnitude is unstable and partly mechanical; the more interesting finding is what
      happens when model is added as a facet.

  - name: "exp-002 Multi-Benchmark Replication"
    plan_id: "exp-002"
    description: >
      3 models (Gemma excluded) × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds ×
      2 temperatures × 4 orderings × 200 items each on GSM8K, ARC-Challenge, HellaSwag.
      Reduced crossing (2×2 vs 3×3). Tests cross-benchmark gradient hypothesis.
    expected_results:
      total_records_gsm8k: 172800
      total_records_arc: 172800
      total_records_hellaswag: 172800
      models_completed_gsm8k: 3
      models_completed_arc: 2  # Mistral near-chance on ARC, data suspect
      models_completed_hellaswag: 3
      benchmarks_with_complete_data: 3
      # GSM8K variance decomposition (single-model pooled)
      item_id_pct_gsm8k_pooled: 0.143
      seed_pct_gsm8k: 0.089
      temperature_pct_gsm8k: 0.112
      prompt_pct_gsm8k: 0.067
      seed_x_item_pct_gsm8k: 0.138
      temperature_x_item_pct_gsm8k: 0.124
      residual_pct_gsm8k: 0.247
      precision_x_temperature_gsm8k_binary_pct: 3.2
      g_coeff_binary_gsm8k_200item: 0.198
      # ARC variance decomposition
      item_id_pct_arc_pooled: 0.472
      seed_pct_arc: 0.018
      temperature_pct_arc: 0.031
      prompt_pct_arc: 0.093
      residual_pct_arc: 0.196
      precision_x_temperature_arc_binary_pct: 0.4
      g_coeff_binary_arc_200item: 0.311
      # HellaSwag variance decomposition
      item_id_pct_hellaswag_pooled: 0.387
      seed_pct_hellaswag: 0.042
      temperature_pct_hellaswag: 0.058
      prompt_pct_hellaswag: 0.121
      precision_x_prompt_hellaswag_binary_pct: 3.8
      residual_pct_hellaswag: 0.203
      g_coeff_binary_hellaswag_200item: 0.274
      # Cross-benchmark gradient
      cross_benchmark_gradient_pp: 5.1  # not systematic
      item_id_ordering_by_benchmark: "ARC(47.2%) > HellaSwag(38.7%) > MMLU(~55%) > GSM8K(14.3%)"
      gradient_correlation_with_task_type: -0.12  # near zero
      # Separability failures
      direct_infra_x_method_binary_gsm8k: 3.2
      direct_infra_x_method_binary_hellaswag: 3.8
      direct_infra_x_method_binary_arc: 0.4
      direct_infra_x_method_text_match_gsm8k: 7.4
      direct_infra_x_method_text_match_hellaswag: 5.9
      benchmarks_separability_fails_binary: 2  # GSM8K, HellaSwag
    result_rationale: >
      The cross-benchmark gradient hypothesis collapses. The item_id ordering is
      MMLU(55%) > ARC(47%) > HellaSwag(39%) > GSM8K(14%), which does not follow any
      coherent task taxonomy. ARC (science reasoning) has higher item_id than HellaSwag
      (commonsense), despite commonsense items being more "knowledge-like." GSM8K's low
      item_id (14.3%) is expected — math reasoning items have high seed×item and
      temperature×item interactions because chain-of-thought generation introduces
      stochastic branching at each reasoning step. But HellaSwag's intermediate position
      and ARC's high position are not predicted by any task-type theory. The correlation
      between task-type ranking and item_id ranking is near zero (r=-0.12), destroying
      the "knowledge→reasoning gradient" narrative.

      Separability fails on GSM8K (precision×temperature = 3.2% under binary) and
      HellaSwag (precision×prompt = 3.8%). The GSM8K failure is interpretable: at T=0.7,
      floating-point non-associativity in the softmax creates different token selection
      paths across precisions, and for multi-step reasoning, these divergences compound.
      The HellaSwag failure is less interpretable — precision×prompt interaction suggests
      that certain prompt framings expose precision-dependent attention patterns in the
      commonsense completion task. Neither failure was predicted by the MVP data (which
      showed separability under binary scoring on MMLU). This means the Claim 2 separability
      result is benchmark-conditional in a way that undermines confident generalization.

      The residual components are large everywhere (19.6-24.7%), foreshadowing the
      model×item interaction that will emerge when model is treated as a facet in exp-004.
    tables:
      - name: "Table 4: Variance Decomposition Across Benchmarks (Single-Model Pooled, Binary Scoring)"
        description: >
          Rows: 10 variance sources. Columns: MMLU, GSM8K, ARC-Challenge, HellaSwag.
          No systematic gradient visible. Item_id ranges from 14.3% (GSM8K) to 55%+ (MMLU).
          Residual uniformly large (19-25%). Interaction terms vary idiosyncratically.
      - name: "Table 5: Infrastructure × Methodology Interactions (Binary + Text Match)"
        description: >
          All 2-way infra×method interactions per benchmark under both scoring metrics.
          Binary: GSM8K 3.2%, HellaSwag 3.8%, ARC 0.4%, MMLU 0.3%. Text match:
          GSM8K 7.4%, HellaSwag 5.9%. Separability fails on 2/4 benchmarks under binary.
      - name: "Table 6: G-coefficients by Benchmark and Metric"
        description: >
          Binary G: MMLU 0.36, ARC 0.31, HellaSwag 0.27, GSM8K 0.20. Text match G:
          MMLU 0.97, GSM8K 0.88, ARC 0.91, HellaSwag 0.93. Binary G is poor everywhere;
          text match is acceptable but variable.
    figures_description:
      - "Stacked-bar variance decomposition across 4 benchmarks. The signature figure — visually demonstrates NO gradient. Each benchmark has a unique 'fingerprint' of variance sources."
      - "Radar chart of top-5 variance sources per benchmark, showing non-overlapping patterns. MMLU is item-dominated, GSM8K is interaction-dominated, ARC is item+prompt, HellaSwag is prompt+residual."
      - "Separability violation heatmap: benchmarks × interaction terms, with cells colored by magnitude. Clear that separability is benchmark-conditional."
    analysis: >
      The gradient narrative is dead. Variance structure is idiosyncratic per benchmark
      and not predictable from task type alone. This is actually a finding — "variance
      structure is benchmark-specific" — but it is a negative finding relative to the
      original framing. Separability fails on 2 benchmarks under binary scoring,
      undermining the confirmatory null that was supposed to validate isolated-factor
      studies. The paper must pivot: instead of "here's a gradient that explains
      everything," the message becomes "nothing is simple, everything interacts, and
      you cannot generalize reproducibility findings across benchmarks."

  - name: "exp-003 Multi-Hardware G-Study"
    plan_id: "exp-003"
    description: >
      Multi-GPU type crossing to test hardware × methodology interaction. In the worst
      tier, second GPU type is unavailable (Manager cannot allocate datacenter GPU within
      timeline). Fallback: run on westd-32570 only with 2 GPU instances (same architecture)
      as pseudo-replication. Limited to same RTX PRO 6000 hardware.
    expected_results:
      hardware_types_obtained: 1
      second_gpu_available: false
      fallback_design: "2 instances of RTX PRO 6000 (same arch, different physical units)"
      gpu_instance_x_method_interaction_pct: 0.08
      gpu_instance_x_item_pct: 0.03
      # OR alternative: second GPU obtained but shows problems
      alt_second_gpu_type: "A100-80GB (if obtained)"
      alt_gpu_x_method_binary_pct: 2.4
      alt_gpu_x_prompt_pct: 1.8
      alt_gpu_x_temperature_pct: 0.9
      alt_gpu_x_item_pct: 3.1
      total_records_fallback: 777600
      experiment_status: "degraded — same-architecture pseudo-replication only"
    result_rationale: >
      In the worst tier, exp-003 fails its primary objective. Two scenarios:
      (A) Hardware unavailable: Manager cannot allocate a second GPU architecture within
      the AAAI timeline. The fallback pseudo-replication (two physical units of RTX PRO
      6000) shows near-zero cross-unit variance (0.08%), which is expected — same
      architecture, same drivers, same CUDA version. This tells us nothing about true
      hardware×methodology interaction. The "infrastructure" facet remains limited to
      "numerical precision on a single GPU architecture," severely weakening Claim 2.
      (B) Hardware obtained but interaction is large: if an A100 is obtained, the
      GPU×method interaction reaches 2.4% under binary scoring (driven by different
      CUDA kernel implementations for attention between Ampere and Ada Lovelace).
      GPU×item interaction is even larger (3.1%), meaning hardware affects items
      differentially — some items are hardware-sensitive while others are not. This
      breaks the "precision only" scoping assumption and means the paper must either
      include hardware as a full facet (requiring much more analysis) or explicitly
      scope the study to single-architecture inference. Either outcome damages the paper.
    tables:
      - name: "Table 7a (fallback): Same-Architecture GPU Pseudo-Replication"
        description: >
          Variance decomposition showing gpu_instance contributes <0.1% across all
          interactions. Demonstrates within-architecture reproducibility is high but
          says nothing about cross-architecture effects. Footnote: "True hardware crossing
          requires heterogeneous GPU architectures; this analysis uses same-architecture
          replication only."
      - name: "Table 7b (alt): Cross-Architecture Variance Decomposition (if A100 obtained)"
        description: >
          GPU type as additional facet. GPU×prompt 1.8%, GPU×temperature 0.9%, GPU×item
          3.1%. All exceed the 1% threshold used in MVP. Separability assumption for
          hardware is violated.
    figures_description:
      - "If fallback: simple bar chart showing negligible cross-unit variance. Visually uninteresting but methodologically important as a negative result."
      - "If alt: item-level accuracy difference (A100 minus RTX PRO) distribution, showing a fat-tailed distribution where ~15% of items differ by >5pp across GPU types."
    analysis: >
      exp-003 either provides no useful data (fallback) or actively harmful data (alt).
      The fallback forces explicit scoping to single-architecture, which reviewers will
      flag. The alt scenario compounds the worst-tier narrative by adding yet another
      interacting facet. Either way, Claim 2 (separability) is damaged. The paper must
      reframe "infrastructure" as "numerical precision" only and acknowledge hardware
      as an uncontrolled confound.

  - name: "exp-004 Comprehensive Analysis"
    plan_id: "exp-004"
    description: >
      Combined analysis of exp-001/001b/002/003 data. This is where the worst-tier
      narrative crystallizes. Model-as-facet reanalysis, bootstrap CIs, D-study
      projections, and all methodological defense analyses.
    expected_results:
      # (a) Model-as-facet reanalysis — THE key worst-tier result
      item_id_pct_mmlu_model_as_facet: 0.224
      model_pct_mmlu: 0.068
      model_x_item_pct_mmlu: 0.312
      prompt_x_item_pct_mmlu_model_facet: 0.048
      temperature_x_item_pct_mmlu_model_facet: 0.052
      residual_pct_mmlu_model_facet: 0.119
      item_id_drop_from_single_to_facet_pp: 33.6  # from ~55.8% to 22.4%
      model_x_item_is_largest_source: true
      # GSM8K model-as-facet
      item_id_pct_gsm8k_model_as_facet: 0.091
      model_x_item_pct_gsm8k: 0.287
      seed_x_item_pct_gsm8k_model_facet: 0.112
      # (b) Bootstrap CIs — wide, preventing rank-ordering
      bootstrap_ci_item_id_mmlu_model_facet: [0.148, 0.301]  # 15.3pp width
      bootstrap_ci_model_x_item_mmlu: [0.238, 0.387]  # 14.9pp width
      bootstrap_ci_width_item_id_pp: 15.3
      bootstrap_ci_width_model_x_item_pp: 14.9
      bootstrap_ci_overlap_item_id_model_x_item: true  # CIs overlap!
      bootstrap_ci_item_id_gsm8k: [0.041, 0.142]  # 10.1pp
      bootstrap_ci_model_x_item_gsm8k: [0.209, 0.364]  # 15.5pp
      # (c) D-study projections
      d_study_items_for_g90_mmlu_binary: 1400
      d_study_items_for_g90_gsm8k_binary: 2000  # unreachable practically
      d_study_items_for_g90_arc_binary: 980
      d_study_items_for_g90_hellaswag_binary: 1200
      d_study_items_for_g90_mmlu_text_match: 45
      d_study_range_across_benchmarks: "45–2000 items"
      d_study_prompts_for_g90_mmlu_binary: 8
      d_study_seeds_for_g90_mmlu_binary: 4
      d_study_budget_mmlu_total_conditions: 44800  # 1400 × 8 × 4
      # (d) REML vs Henderson
      reml_vs_henderson_max_diff_pp: 3.8
      reml_vs_henderson_rank_order_preserved: false  # rank changes on HellaSwag
      # (e) Logprob scoring
      g_coeff_logprob_mmlu: 0.412
      logprob_item_id_pct: 0.483
      logprob_model_x_item_pct: 0.198
      # (f) Ranking stability
      precision_x_temp_alters_rankings: true  # Qwen and Llama swap on 2/9 conditions
      ranking_instability_fraction: 0.22  # 22% of conditions show at least one rank swap
      # (g) Higher-order interactions
      three_way_interactions_total_pct: 0.042
      # (h) G-theory vs IRT comparison
      irt_recommended_items_mmlu: 110
      gtheory_recommended_items_mmlu: 1400
      ratio_gtheory_to_irt: 12.7
      # (i) Power analysis
      min_detectable_interaction_pct: 1.2  # can detect ≥1.2% interactions
      power_for_2pct_interaction: 0.89
      # (j) Fixed vs random sensitivity (MD2)
      fixed_vs_random_max_diff_pp: 7.2  # substantial
      temperature_fixed_changes_item_id_by_pp: 4.1
      # (k) Binary data limitation (MD1)
      bernoulli_variance_correlation_with_item_id: 0.83
      mechanical_share_of_item_id: 0.61  # 61% of item_id is Bernoulli-mechanical
      # (l) Bootstrap vs jackknife (MD6)
      bootstrap_jackknife_ci_ratio: 1.34  # bootstrap 34% wider
      jackknife_ci_width_item_id_pp: 11.4
      # (m) Design asymmetry sensitivity (MD8)
      mmlu_3x3_vs_2x2_item_id_diff_pp: 4.7
      mmlu_3x3_vs_2x2_changes_rank_order: false
      # (n) Full benchmark projection (MD5)
      g_coeff_binary_mmlu_14k_items_projected: 0.891  # still below 0.90
      g_coeff_binary_mmlu_14k_items_ci: [0.847, 0.934]
      # (o) GPU cost analysis
      compute_cost_recommended_budget_mmlu_usd: 4200
      compute_cost_recommended_budget_gsm8k_usd: 11500
    result_rationale: >
      The model-as-facet reanalysis is the earthquake. When model is added as a crossed
      facet to the MMLU G-study, item_id drops from ~55.8% (single-model) to 22.4%,
      while model×item interaction emerges at 31.2% — the LARGEST single variance source.
      This happens because different models find different items difficult: an item that
      Llama gets right 95% of the time, Mistral may get right only 40% of the time.
      This differential item functioning (DIF) was hidden in single-model analyses where
      it was confounded with the residual. The 33.6pp drop in item_id is dramatic and
      changes the entire paper narrative.

      Bootstrap CIs are wide (15.3pp for item_id, 14.9pp for model×item) and the two
      CIs overlap, meaning we cannot even definitively say which is larger. This is
      driven by item-level resampling with only 200 items — each bootstrap resample
      has ~127 unique items (Euler's formula), and the item×model interaction is sensitive
      to which items are included. The width exceeds 12pp on all benchmarks, making
      confident rank-ordering of variance sources impossible on most benchmarks.

      D-study projections are dire: achieving G≥0.90 under binary scoring requires
      1400 items on MMLU, 2000 on GSM8K (practically unreachable — GSM8K only has 1319
      test items), and 980-1200 on ARC/HellaSwag. These budgets are 3-10× larger than
      MVP estimates because model×item interaction adds a variance source that cannot
      be reduced by prompt/seed averaging — only item expansion helps. The cross-benchmark
      range (45-2000 items) is so large that no single recommendation is actionable.

      The G-theory vs IRT comparison reveals a 12.7× discrepancy (tinyBenchmarks: 110
      items; G-theory: 1400 items). This is because IRT ignores prompt/seed/temperature/
      ordering facets entirely — it assumes a single fixed evaluation protocol. The
      G-theory budget accounts for reproducibility across ALL facets, making it much
      larger. This is actually a strong finding: IRT-based subsampling produces reliable
      rankings only within a fixed protocol, not across protocols.

      Fixed vs random sensitivity analysis (MD2) shows a 7.2pp maximum change when
      temperature is treated as fixed vs random. Temperature has only 2-3 design points,
      making the random assumption dubious. But the fixed treatment changes item_id by
      4.1pp, which is large enough to affect conclusions. This is a genuine methodological
      vulnerability with no clean resolution.

      The Bernoulli correlation analysis (MD1) confirms that 61% of item_id's magnitude
      is mechanically driven by item difficulty spread through p(1-p). This is damning:
      more than half of the "headline finding" (item dominance) is a statistical artifact
      of using binary scoring on items with heterogeneous difficulty. The text_match
      metric does not suffer from this, but text_match has different (and less dramatic)
      variance structure.

      Even projecting to 14K items (full MMLU), binary G reaches only 0.891 [0.847, 0.934],
      still below 0.90 with a CI that includes values as low as 0.847. This means even
      full MMLU may not provide reliable binary-scored evaluation when considering all
      facets — a provocative but hard-to-communicate finding.
    tables:
      - name: "Table 8: Model-as-Facet Variance Decomposition (MMLU, binary scoring)"
        description: >
          The central table of the paper. Rows: item_id (22.4%), model (6.8%),
          model×item (31.2%), prompt×item (4.8%), temp×item (5.2%), precision×item (2.1%),
          seed (0.4%), prompt (1.2%), temperature (2.8%), precision (4.3%),
          3-way+ interactions (4.2%), residual (11.9%). Model×item is largest. Bold.
          Adjacent column: bootstrap 95% CI for each. CIs on item_id and model×item overlap.
      - name: "Table 9: Model-as-Facet Variance Decomposition Across Benchmarks"
        description: >
          Same format as Table 8 but columns = MMLU, GSM8K, ARC, HellaSwag. Model×item
          is largest or co-largest on MMLU (31.2%) and GSM8K (28.7%). On ARC, item_id
          remains largest (34.1%) with model×item at 22.3%. HellaSwag: prompt×item (18.9%)
          competes with model×item (21.7%). No consistent pattern across benchmarks.
      - name: "Table 10: D-Study Projections for G≥0.90 (Binary Scoring)"
        description: >
          Rows: MMLU, GSM8K, ARC, HellaSwag. Columns: required items, prompts, seeds,
          total conditions, estimated GPU-hours, USD cost. Items range 980-2000.
          GSM8K marked "exceeds available test items." Total costs: $4.2K-$11.5K per benchmark.
      - name: "Table 11: G-theory vs IRT Item Recommendations"
        description: >
          Comparison table. IRT (tinyBenchmarks): 110 items. G-theory: 1400 items.
          Ratio: 12.7×. Explanation: IRT assumes fixed protocol; G-theory targets
          cross-protocol reliability. Both are "correct" for different reliability definitions.
      - name: "Table 12: Bootstrap CI Widths by Variance Source and Benchmark"
        description: >
          All variance sources × all benchmarks. CI widths range 3-16pp. Sources with
          CI >12pp highlighted. Item_id and model×item exceed 12pp on all benchmarks.
          Precision main effect CIs are tighter (3-5pp). Message: only main effects
          can be estimated precisely; interactions and item-dependent sources are noisy.
      - name: "Table 13: Methodological Sensitivity Analyses Summary"
        description: >
          Rows: REML vs Henderson, Fixed vs Random, Binary vs TextMatch, 3×3 vs 2×2,
          Bootstrap vs Jackknife. Columns: max difference (pp), rank order preserved (Y/N),
          conclusion. Two of five analyses show >5pp sensitivity. Overall: results are
          moderately robust but not insensitive to analytic choices.
    figures_description:
      - "Figure 3 (SIGNATURE): Stacked-bar variance decomposition, single-model vs model-as-facet, side by side for MMLU. Dramatic visual: item_id shrinks, model×item emerges as largest block. The 'before and after' is the paper's most striking visual."
      - "Figure 4: Stacked-bar variance decomposition across all 4 benchmarks (model-as-facet). Each bar has a unique 'fingerprint.' No gradient visible."
      - "Figure 5: D-study projection curves — G vs item count for 4 benchmarks. Curves diverge wildly. GSM8K never reaches G=0.90 within available items. MMLU reaches 0.90 at ~1400 items."
      - "Figure 6: Bootstrap CI forest plot for top-5 variance sources on MMLU. Wide, overlapping CIs for item_id and model×item. Tight CIs for precision main effect."
      - "Figure 7: Bernoulli p(1-p) vs observed item variance scatter plot. r=0.83 correlation. Regression line shows 61% of item_id is mechanical."
    analysis: >
      exp-004 reveals that the entire single-model analysis framework was misleading.
      Model×item interaction (31.2%) — not item difficulty — is the dominant variance
      source when models are properly crossed. This is the worst-tier's central finding
      and it is genuinely novel and surprising. However, the wide bootstrap CIs, the
      Bernoulli mechanical artifact, and the benchmark-idiosyncratic patterns make the
      paper very hard to write cleanly. Every claim requires heavy qualification.
      The D-study budgets are impractically large and benchmark-specific, providing no
      actionable "recipe." The G-theory vs IRT comparison is the strongest standalone
      contribution but is a methods comparison, not an empirical finding. The narrative
      must shift to: "evaluation is harder than you think, and here's exactly why."

  - name: "exp-005 14B Model Extension"
    plan_id: "exp-005"
    description: >
      Qwen3-14B and DeepSeek-R1-Distill-14B at BF16/FP16. Tests scale effects.
      Depends on exp-003 (hardware). In worst tier, hardware issues cascade.
    expected_results:
      hardware_obtained: false  # cascading from exp-003
      experiment_status: "blocked — requires ≥48GB VRAM datacenter GPU not available"
      alt_single_gpu_status: "attempted on westd-32570 (96GB) with reduced design"
      alt_total_records: 28800  # minimal 2 models × 2 prec × 3 prompts × 3 seeds × 1 temp × 2 orderings × 200 items
      alt_qwen14b_accuracy: 0.738
      alt_deepseek_r1_distill_accuracy: 0.712
      alt_item_id_pct_qwen14b: 0.501
      alt_item_id_pct_deepseek_r1: 0.423
      alt_cross_scale_item_correlation: 0.64  # 14B vs 8B item difficulty correlation
      alt_model_x_item_estimated: "not estimable with 2-model design"
    result_rationale: >
      exp-005 is either blocked entirely (no datacenter GPU) or runs on the single
      available GPU with a severely reduced design. Even if it runs, 2 models is
      insufficient to estimate model×item interaction as a random effect — you need ≥3
      for meaningful variance component estimation. The cross-scale item difficulty
      correlation (r=0.64 between 8B and 14B models) is lower than within-scale
      correlation (r=0.71-0.78 among 8B models), suggesting that scale increases
      model×item interaction further. This is consistent with the worst-tier narrative
      (larger models have more distinct item-level competence profiles) but the evidence
      is too thin to make claims. The experiment contributes almost nothing to the paper
      in the worst tier.
    tables:
      - name: "Table A1 (Appendix): 14B Model Accuracy Summary"
        description: >
          Minimal 2×2 table (2 models × 2 precisions). Qwen3-14B: 73.8%, DeepSeek-R1-Distill:
          71.2%. Noted as "reduced design, insufficient for G-theory analysis."
    figures_description:
      - "Scatter plot: 8B vs 14B item-level accuracy. r=0.64. Points dispersed more than within-scale comparisons. Suggestive but underpowered."
    analysis: >
      exp-005 is the clearest casualty of the worst tier. It either doesn't run or
      produces too little data to support claims. Relegated to a brief appendix mention
      or dropped entirely. The cross-scale correlation finding (r=0.64) is interesting
      but requires follow-up work with more models and a full crossing design.

  - name: "exp-006 Fine-Tuning G-Study"
    plan_id: "exp-006"
    description: >
      RoBERTa-large on SST-2/MNLI/RTE/COPA. 6 seeds × 3 learning rates × 4 data
      shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 total runs.
      Independent of inference experiments. Tests fine-tuning variance hierarchy.
    expected_results:
      total_runs_completed: 1614  # 114 failed (NaN loss, OOM on some lr×precision combos)
      total_runs_planned: 1728
      failure_rate: 0.066
      failed_config: "lr=5e-4 × fp16 on RTE/COPA (small datasets, unstable)"
      # SST-2 variance decomposition
      item_id_pct_sst2: 0.312
      seed_pct_sst2: 0.089
      lr_pct_sst2: 0.143
      data_shuffle_pct_sst2: 0.034
      gpu_pct_sst2: 0.002
      precision_pct_sst2: 0.018
      seed_x_lr_pct_sst2: 0.112
      residual_pct_sst2: 0.178
      g_coeff_sst2: 0.487
      # MNLI variance decomposition
      item_id_pct_mnli: 0.401
      lr_pct_mnli: 0.098
      seed_pct_mnli: 0.067
      seed_x_item_pct_mnli: 0.134
      residual_pct_mnli: 0.156
      g_coeff_mnli: 0.534
      # RTE (small dataset — high variance)
      item_id_pct_rte: 0.187
      seed_pct_rte: 0.203
      lr_pct_rte: 0.178
      seed_x_lr_pct_rte: 0.156
      residual_pct_rte: 0.214
      g_coeff_rte: 0.298
      # COPA (small dataset — very high variance)
      item_id_pct_copa: 0.134
      seed_pct_copa: 0.241
      lr_pct_copa: 0.198
      residual_pct_copa: 0.267
      g_coeff_copa: 0.213
      # Cross-paradigm comparison
      inference_vs_finetuning_rank_correlation: 0.31
      dominant_source_inference: "item_id (or model×item)"
      dominant_source_finetuning: "item_id on large datasets; seed on small datasets"
    result_rationale: >
      Fine-tuning variance hierarchy differs substantially from inference. On large
      datasets (SST-2, MNLI), item_id is still the largest source (31-40%) but learning
      rate and seed×learning_rate interactions are substantial (10-14%), which have no
      analogue in inference. On small datasets (RTE: 277 items; COPA: 100 items), seed
      becomes dominant (20-24%) because the training dynamics are chaotic with few
      examples — small perturbations in initialization cascade through training.

      GPU and precision contribute negligibly to fine-tuning variance (<2% combined),
      which contrasts with the 4-7% precision contribution in inference. This is because
      fine-tuning aggregates over many gradient steps, averaging out per-forward-pass
      precision effects.

      The cross-paradigm rank correlation (r=0.31) between inference and fine-tuning
      variance hierarchies means the findings do NOT transfer. A reviewer cannot
      extrapolate from our inference G-study to fine-tuning practice, and we cannot
      extrapolate from exp-006 back to inference. This supports the worst-tier narrative
      ("nothing generalizes") but also means exp-006 is somewhat disconnected from the
      paper's main story. It becomes an appendix-level extension rather than a core
      contribution.

      The 6.6% run failure rate (NaN loss on high-lr×fp16 combinations with small
      datasets) is a methodological nuisance. These failures are informative (they
      show that some precision×hyperparameter combinations are unstable) but create
      missing cells in the G-theory design, requiring imputation or reduced analysis.
    tables:
      - name: "Table 14: Fine-Tuning Variance Decomposition Across Tasks"
        description: >
          Rows: seed, learning_rate, data_shuffle, gpu, precision, item_id, seed×lr,
          seed×item, residual. Columns: SST-2, MNLI, RTE, COPA. Clear split between
          large-dataset (item-dominated) and small-dataset (seed-dominated) patterns.
      - name: "Table 15: Inference vs Fine-Tuning Variance Hierarchy Comparison"
        description: >
          Side-by-side ranking of variance sources. Inference: item_id > model×item >
          residual > temperature×item > prompt×item. Fine-tuning: item_id > seed×lr >
          seed > lr > residual. Different hierarchies, different implications.
    figures_description:
      - "Paired stacked-bar: inference (MMLU) vs fine-tuning (SST-2) variance decomposition. Visually distinct patterns — different colors dominate each bar."
      - "G-coefficient comparison: inference tasks vs fine-tuning tasks. Fine-tuning G is generally higher on large datasets but lower on small datasets."
    analysis: >
      exp-006 produces a valid standalone result (fine-tuning variance hierarchy differs
      from inference) but its contribution to the main paper is ambiguous. It supports
      the worst-tier message ("nothing generalizes across paradigms") but also weakens
      coherence — the paper is already struggling to find a unifying narrative, and
      adding a disconnected fine-tuning analysis makes it more scattered. Recommend
      relegating to a 1-page appendix or splitting into a separate short paper.

  - name: "exp-007 LayerCast Precision Mitigation"
    plan_id: "exp-007"
    description: >
      LayerCast (FP16 storage + FP32 compute) as additional precision condition on MMLU.
      Tests whether this mixed-precision strategy reduces variance from the precision facet.
    expected_results:
      total_records: 43200  # 1 model × 216 method conditions × 200 items
      layercast_accuracy: 0.6482
      layercast_vs_fp32_gap_pp: 4.88  # better than pure FP32 but worse than BF16/FP16
      layercast_vs_bf16_gap_pp: -3.62  # worse than BF16
      precision_variance_with_layercast_pct: 5.1  # higher than without, because LayerCast adds a 4th heterogeneous level
      layercast_item_level_correlation_with_bf16: 0.87
      layercast_item_level_correlation_with_fp32: 0.72
      variance_reduction_from_layercast: "none — adds variance rather than reducing it"
    result_rationale: >
      LayerCast does not cleanly reduce variance because it creates a hybrid precision
      regime that behaves differently from both pure FP32 and pure FP16/BF16. The
      storage-in-FP16, compute-in-FP32 approach means attention computations use FP32
      but weight quantization noise from FP16 storage propagates through. The result is
      an accuracy level between FP32 and BF16 (64.8%), but with item-level patterns that
      don't correlate perfectly with either pure precision. Adding LayerCast as a 4th
      precision level actually INCREASES precision facet variance (from 4.3% to 5.1%)
      because it adds another distinct level rather than collapsing precision differences.
      This is a negative result for the mitigation narrative but a positive result for
      the worst-tier message: precision effects are complex and non-monotonic, and simple
      mitigation strategies don't work as advertised.
    tables:
      - name: "Table A2 (Appendix): LayerCast Variance Impact"
        description: >
          4-row precision comparison (FP32, FP16, BF16, LayerCast) with accuracy,
          item-level correlation with BF16, and precision facet variance contribution.
          LayerCast is intermediate but not a clean fix.
    figures_description:
      - "Item-level accuracy scatter: LayerCast vs BF16 (r=0.87) and LayerCast vs FP32 (r=0.72). Two panels showing LayerCast is closer to BF16 but not a drop-in replacement."
    analysis: >
      exp-007 is a minor negative result. LayerCast doesn't serve as a precision
      mitigation strategy in this context. Useful as a 1-paragraph appendix note
      showing that mixed-precision approaches don't simplify the variance picture.
      Low priority for inclusion in the worst-tier paper.

  - name: "exp-008 MATH Benchmark Extension"
    plan_id: "exp-008"
    description: >
      MATH benchmark (200 items) with chain-of-thought reasoning. Tests whether
      reasoning-heavy tasks with long generation have qualitatively different variance
      structure.
    expected_results:
      total_records: 115200  # 3 models × 2 prec × 6 prompts × 6 seeds × 2 temp × ~2.67 orderings × 200 items (reduced)
      models_completed: 2  # Mistral fails on MATH (accuracy <10%, data unusable)
      overall_accuracy_llama: 0.341
      overall_accuracy_qwen: 0.428
      accuracy_range_across_conditions: 0.187  # 18.7pp — massive
      # Variance decomposition
      item_id_pct_math: 0.118
      seed_pct_math: 0.134
      temperature_pct_math: 0.156
      prompt_pct_math: 0.087
      seed_x_item_pct_math: 0.168
      temperature_x_item_pct_math: 0.143
      precision_x_temperature_pct_math_binary: 4.7
      residual_pct_math: 0.194
      g_coeff_binary_math_200item: 0.152
      d_study_items_for_g90_math_binary: "not achievable within MATH test set size"
      # Chain-of-thought specific
      avg_generation_length_tokens: 487
      generation_length_cv: 0.68  # high coefficient of variation
      accuracy_conditional_on_cot_length: "non-monotonic — medium length CoT has highest accuracy"
    result_rationale: >
      MATH represents the extreme end of the worst-tier pattern. Item_id is only 11.8%
      — the lowest of any benchmark — because chain-of-thought generation introduces
      massive stochastic branching. Each reasoning step is a decision point where
      temperature and seed can send the model down different solution paths. The
      seed×item (16.8%) and temperature×item (14.3%) interactions are the dominant
      sources, meaning the same item can be solved or not depending on the random seed
      and temperature — an extreme form of the model×item interaction pattern.

      The 18.7pp accuracy range across conditions for the same model on the same items
      is striking: the "same" evaluation can produce 34.1% or 52.8% accuracy for Llama
      on MATH depending on prompt/seed/temperature. This makes any single-run MATH
      evaluation essentially meaningless for fine-grained model comparison.

      Separability fails catastrophically: precision×temperature interaction is 4.7%
      under binary scoring, the highest of any benchmark. This is because FP16/BF16
      rounding in the softmax creates different token selections at each reasoning step,
      and at higher temperatures these divergences compound over 400+ tokens of
      chain-of-thought.

      G=0.152 for 200 items under binary scoring is the lowest across all benchmarks.
      D-study projections show G≥0.90 is not achievable within MATH's test set (5000
      items) because the dominant variance sources (seed×item, temperature×item) cannot
      be reduced by adding items — they require averaging over many seeds and temperatures
      per item, which is computationally expensive.

      Mistral's exclusion (accuracy <10%, effectively random guessing on MATH) further
      reduces model coverage to 2, making model-as-facet analysis impossible on this
      benchmark.
    tables:
      - name: "Table A3 (Appendix): MATH Variance Decomposition"
        description: >
          Seed×item (16.8%) and temperature×item (14.3%) dominate. Item_id is only 11.8%.
          Precision×temperature is 4.7%. G=0.152. The most extreme interaction-dominated
          pattern in the study.
      - name: "Table A4: Accuracy Range by Model Across Conditions (MATH)"
        description: >
          2 models × min/max/range across all conditions. Llama: 22.5-52.8% (range 30.3pp).
          Qwen: 31.2-58.4% (range 27.2pp). Demonstrates that single-run MATH evaluation
          is unreliable.
    figures_description:
      - "Heatmap: seed × temperature accuracy grid for Llama on MATH. High variance visible — hot spots and cold spots across the grid with no smooth pattern."
      - "Chain-of-thought length distribution by accuracy outcome (correct vs incorrect). Bimodal: very short (gave up) and very long (went in circles) both predict failure."
    analysis: >
      MATH is the poster child for the worst-tier narrative: everything interacts,
      nothing is stable, and single-run evaluation is meaningless. But with only 2
      models and a reduced design, the evidence is thin. The extreme interaction
      dominance is compelling but also predictable (CoT reasoning is inherently
      stochastic). The finding reinforces the "no gradient" message — MATH is not
      simply "one step further" on a knowledge→reasoning continuum; it has a
      qualitatively different variance structure that shares nothing with MMLU or ARC.
      Best used as a dramatic closing example in the paper rather than a core analysis.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34a23d74-9501-41ed-98af-c37d6490a0a7",
  "isSidechain": false,
  "requestId": "req_011CbF3ZyhKNU7iVuiAtGLCr",
  "type": "assistant",
  "uuid": "c16266fb-cbdd-4518-bb89-3e707c0c65d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KMfXnfgXGtjQK5BmaTcgNY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13762,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14610,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14610,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13762
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Model×item interaction dominates after reanalysis; no coherent benchmark gradient; separability fails broadly 核心假设：['Model×item interaction becomes larges…",
  "leafUuid": "c16266fb-cbdd-4518-bb89-3e707c0c65d0",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Model×item interaction dominance with benchmark-specific variance structures",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Model×item interaction dominates after reanalysis; no coherent benchmark gradient; separability fails broadly 核心假设：['Model×item interaction becomes larges…",
  "leafUuid": "c16266fb-cbdd-4518-bb89-3e707c0c65d0",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Model×item interaction dominance with benchmark-specific variance structures",
  "sessionId": "292233c5-030e-414e-8dcf-2522550c6441"
}
```

---
