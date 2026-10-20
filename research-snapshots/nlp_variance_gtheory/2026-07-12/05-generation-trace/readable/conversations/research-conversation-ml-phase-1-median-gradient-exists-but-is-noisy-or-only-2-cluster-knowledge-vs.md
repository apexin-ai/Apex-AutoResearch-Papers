# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Gradient exists but is noisy or only 2-cluster (knowledge vs reasoning); s

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/b4125e70-e297-410c-afc9-d3cc6ac9f2e3.jsonl`
- **Structured JSON:** [`bfb0facaee4964858a3f.json`](../../sessions/bf/bfb0facaee4964858a3f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T22:42:38.098Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T22:42:38.098Z",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Gradient exists but is noisy or only 2-cluster (knowledge vs reasoning); some claims need softening; paper is publishable with adjusted framing\n核心假设：['Item dominance on MMLU replicates but with wider spread across resamples (exp-001b CV 15-25%)', 'Cross-benchmark gradient exists but is 2-cluster rather than monotonic: {MMLU, ARC} high item dominance vs {GSM8K, HellaSwag} lower — not a clean 4-point gradient', 'GSM8K item dominance is 30-40% rather than the hypothesized 20-30% — gradient exists but is shallower than claimed', 'Separability holds on knowledge benchmarks but one reasoning benchmark shows infra×method 2-5% (binary), requiring metric+benchmark qualification', \"Model-as-facet absorbs 15-25% from item_id on some benchmarks, making 'item dominance' claim benchmark-conditional rather than universal\", 'Bootstrap CIs on gradient endpoints overlap partially — gradient direction is clear but magnitude is imprecise', 'Multi-hardware (exp-003) shows hardware main effect 1-3% on one precision, manageable but requires discussion', 'D-study projections differentiate benchmarks but optimal allocations are closer than expected (less dramatic practical implication)']\n关键指标范围：{'item_id_variance_mmlu_binary': [0.42, 0.55], 'item_id_variance_gsm8k_binary': [0.3, 0.42], 'item_id_variance_arc_binary': [0.38, 0.52], 'item_id_variance_hellaswag_binary': [0.25, 0.38], 'cross_benchmark_gradient_spread_pp': [10, 24], 'infra_x_method_binary_all_benchmarks': [0.0, 0.05], 'infra_x_method_textmatch_max': [0.015, 0.045], 'hardware_x_methodology_exp003': [0.005, 0.03], 'model_x_item_mmlu': [0.15, 0.28], 'g_correct_mmlu': [0.3, 0.42], 'g_correct_gsm8k': [0.35, 0.55], 'bootstrap_ci_width_item_id': [0.08, 0.15], 'item_resample_cv_exp001b': [0.15, 0.25], 'dstudy_items_for_g90_mmlu': [300, 500], 'dstudy_items_for_g90_gsm8k': [200, 350]}\n叙事方向：Soften \"gradient\" to \"benchmark-conditional variance structure\" — emphasize the existence of benchmark dependence rather than a clean monotonic ordering. Claim 1 weakens from \"systematic gradient\" to \"task-type clustering\": knowledge-retrieval benchmarks show higher item dominance than reasoning benchmarks, but within-cluster ordering is not reliable. Claim 2 adds qualification: separability is benchmark-conditional, not universal. Claim 3 survives but with wider CIs and less dramatic differentiation between benchmark-specific budgets. Reframe hook as \"even the question of WHAT dominates variance depends on your benchmark\" rather than \"gradient across benchmarks.\" Model-as-facet absorption becomes a feature: \"prior single-model studies overestimated item dominance by confounding item difficulty with model-item interaction.\" Still targets AAAI but may need one more experiment (e.g., additional benchmark) to strengthen the clustering story. If AAAI timeline is tight, ACL ARR October is a comfortable fallback.\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: nlp_variance_gtheory\nfocus: Re-dream after major framing revision addressing all 9 structural issues from first dream. Key changes: (1) infrastructure crossing reframed as confirmatory null, not primary novelty; (2) cross-benchmark variance gradient is now the primary finding; (3) item dominance acknowledged as psychometrically expected, contribution is quantification+gradient; (4) model treated as crossed facet in analysis; (5) bibliography expanded to 25+ refs; (6) 4 figures planned; (7) \"fully crossed\" qualified; (8) \"diagnostic tool\" either substantiated with code release or reframed. Verify whether these framing changes address the weak reject scores from first dream.\n\n## paper_framing.md\n\n# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation, but its magnitude is benchmark-dependent: from ~45% on knowledge-retrieval tasks (MMLU) down to ~25% on reasoning tasks (GSM8K/MATH) where temperature and seed interactions increase. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating the systematic benchmark-dependent gradient, and (c) deriving D-study implications specific to LLM evaluation.\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.\n\n## Contributions (3 条，明确区分)\n\n1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\n\n2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.\n\n3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (25-55%, benchmark-dependent), while direct infrastructure×methodology interactions are negligible (<0.5% binary, ≤1.3% text-match). Variance structure shifts systematically from item-dominated (knowledge benchmarks) to interaction-dominated (reasoning benchmarks). D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional: MMLU needs more items, GSM8K needs more seeds.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (4 figures minimum):\n  1. Problem illustration: same model, different benchmark → different dominant variance source\n  2. G-theory facet diagram showing crossed design\n  3. Stacked-bar variance decomposition across benchmarks (signature figure)\n  4. D-study projection curves: G vs item count for different benchmarks\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (25-55%), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Full-scale precision study: 4 models (Qwen3-8B-Instruct, Llama-3.1-8B-Instruct,\n    Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3) × 3 precisions (FP32, BF16, FP16) × 6\n    prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified).\n    All precisions use consistent vLLM engine (V0 enforce_eager) to eliminate the\n    float32 engine confound found in MVP. Validates item dominance finding at scale\n    and with multiple models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 100\n  hardware: westd-32570 (RTX PRO 6000 96GB)\n  deps: []\n  status: planned\n- id: exp-001b\n  claim: 1\n  description: 'Item resampling stability test: 3 independent stratified samples of\n    200 MMLU items (seeds 0, 7, 99) × 1 model (Llama-3.1-8B-Instruct) × 3 precisions\n    × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether\n    the 58% item dominance finding is stable across different item draws from MMLU,\n    not an artifact of the specific 200-item sample. Critical for defending the headline\n    claim.\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Multi-benchmark replication: same 4 models × BF16/FP16 × 6 prompts\n    × 6 seeds × 2 temperatures × 4 orderings on GSM8K (200 items), ARC-Challenge (200\n    items), HellaSwag (200 items). Tests whether item dominance and separability hold\n    across task types (math reasoning, science reasoning, commonsense).\n\n    '\n  priority: P0\n  gpu_budget_hours: 200\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-003\n  claim: 2\n  description: 'Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16,\n    FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. Tests\n    hardware × methodology interaction — the core separability question that MVP couldn''t\n    address with only 1 GPU type.\n\n    '\n  priority: P0\n  gpu_budget_hours: 120\n  hardware: westd-32570 + TBD (second GPU type from Manager)\n  deps: []\n  status: planned\n- id: exp-004\n  claim: 3\n  description: 'Comprehensive analysis of combined exp-001/001b/002/003 data. Includes:\n    (a) Model-as-facet G-theory reanalysis — treat model as crossed random facet to\n    properly attribute model×item interaction and reduce inflated item_id/residual\n    (Dream critical); (b) Bootstrap CIs (1000 resamples) on ALL variance components\n    in ALL tables, especially direct infra×method interaction term (Dream critical);\n    (c) D-study projections with CIs for optimal allocation across facets for G≥0.90/0.95/0.99,\n    with benchmark-specific budgets and comparison to IRT-based subsampling (tinyBenchmarks);\n    (d) REML vs Henderson Method I comparison as sensitivity analysis; (e) Logprob-based\n    scoring as third response variable; (f) Ranking stability analysis — does precision×temperature\n    interaction alter model rankings? (g) Higher-order interaction estimation to decompose\n    the residual component.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  hardware: none\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  status: planned\n- id: exp-005\n  claim: 2\n  description: '14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter\n    GPUs at BF16/FP16. Tests whether variance attribution patterns change with model\n    scale and architecture (dense vs reasoning-distilled).\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  hardware: TBD (needs ≥48GB VRAM per GPU)\n  deps:\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA. Fully crossed:\n    6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task\n    × 4 tasks = 1,728 total fine-tuning runs. Validates whether variance hierarchy\n    differs between inference and fine-tuning.\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  hardware: westd-32570 (RoBERTa-large fits easily on 96GB)\n  deps: []\n  status: planned\n- id: exp-007\n  claim: 2\n  description: 'Test LayerCast (FP16 storage + FP32 compute) as additional precision\n    condition on MMLU. Quantifies variance reduction from this mitigation strategy.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 1\n  description: 'MATH benchmark (200 items) — tests whether item dominance pattern\n    differs for reasoning-heavy tasks where chain-of-thought introduces additional\n    variance.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  hardware: westd-32570\n  deps:\n  - exp-002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase_a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 5400\n    conditions: 108\n    overall_accuracy: 0.6557\n    accuracy_bfloat16: 0.6844\n    accuracy_float16: 0.6833\n    accuracy_float32: 0.5994\n    g_coefficient_correct: 0.357\n    top_variance_correct:\n      item_id: 0.5844\n      residual: 0.1759\n      precision:item_id: 0.0724\n      temperature:item_id: 0.0685\n      prompt_template:item_id: 0.0573\n    top_variance_text_match:\n      residual: 0.407\n      prompt_template:item_id: 0.375\n      temperature: 0.169\n      temperature:item_id: 0.025\n      precision:temperature: 0.013\n    pass_criteria_a_pipeline: true\n    pass_criteria_b_components: true\n    pass_criteria_c_interaction: true\n    pass_criteria_c_detail: precision:temperature 1.3% CI not containing zero (text_exact_match)\n- exp_id: bf16_eager_disentangle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bf16_v1_accuracy: 0.6844\n    bf16_eager_accuracy: 0.6822\n    fp32_v0_accuracy: 0.5994\n    engine_effect_pct: 2.6\n    precision_effect_pct: 97.4\n    engine_gap_pp: 0.22\n    precision_gap_pp: 8.28\n    total_gap_pp: 8.5\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T22:42:38.101Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T22:42:38.101Z",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T22:42:38.126Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Gradient exists but is noisy or only 2-cluster (knowledge vs reasoning); some claims need softening; paper is publishable with adjusted framing
核心假设：['Item dominance on MMLU replicates but with wider spread across resamples (exp-001b CV 15-25%)', 'Cross-benchmark gradient exists but is 2-cluster rather than monotonic: {MMLU, ARC} high item dominance vs {GSM8K, HellaSwag} lower — not a clean 4-point gradient', 'GSM8K item dominance is 30-40% rather than the hypothesized 20-30% — gradient exists but is shallower than claimed', 'Separability holds on knowledge benchmarks but one reasoning benchmark shows infra×method 2-5% (binary), requiring metric+benchmark qualification', "Model-as-facet absorbs 15-25% from item_id on some benchmarks, making 'item dominance' claim benchmark-conditional rather than universal", 'Bootstrap CIs on gradient endpoints overlap partially — gradient direction is clear but magnitude is imprecise', 'Multi-hardware (exp-003) shows hardware main effect 1-3% on one precision, manageable but requires discussion', 'D-study projections differentiate benchmarks but optimal allocations are closer than expected (less dramatic practical implication)']
关键指标范围：{'item_id_variance_mmlu_binary': [0.42, 0.55], 'item_id_variance_gsm8k_binary': [0.3, 0.42], 'item_id_variance_arc_binary': [0.38, 0.52], 'item_id_variance_hellaswag_binary': [0.25, 0.38], 'cross_benchmark_gradient_spread_pp': [10, 24], 'infra_x_method_binary_all_benchmarks': [0.0, 0.05], 'infra_x_method_textmatch_max': [0.015, 0.045], 'hardware_x_methodology_exp003': [0.005, 0.03], 'model_x_item_mmlu': [0.15, 0.28], 'g_correct_mmlu': [0.3, 0.42], 'g_correct_gsm8k': [0.35, 0.55], 'bootstrap_ci_width_item_id': [0.08, 0.15], 'item_resample_cv_exp001b': [0.15, 0.25], 'dstudy_items_for_g90_mmlu': [300, 500], 'dstudy_items_for_g90_gsm8k': [200, 350]}
叙事方向：Soften "gradient" to "benchmark-conditional variance structure" — emphasize the existence of benchmark dependence rather than a clean monotonic ordering. Claim 1 weakens from "systematic gradient" to "task-type clustering": knowledge-retrieval benchmarks show higher item dominance than reasoning benchmarks, but within-cluster ordering is not reliable. Claim 2 adds qualification: separability is benchmark-conditional, not universal. Claim 3 survives but with wider CIs and less dramatic differentiation between benchmark-specific budgets. Reframe hook as "even the question of WHAT dominates variance depends on your benchmark" rather than "gradient across benchmarks." Model-as-facet absorption becomes a feature: "prior single-model studies overestimated item dominance by confounding item difficulty with model-item interaction." Still targets AAAI but may need one more experiment (e.g., additional benchmark) to strengthen the clustering story. If AAAI timeline is tight, ACL ARR October is a comfortable fallback.


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: nlp_variance_gtheory
focus: Re-dream after major framing revision addressing all 9 structural issues from first dream. Key changes: (1) infrastructure crossing reframed as confirmatory null, not primary novelty; (2) cross-benchmark variance gradient is now the primary finding; (3) item dominance acknowledged as psychometrically expected, contribution is quantification+gradient; (4) model treated as crossed facet in analysis; (5) bibliography expanded to 25+ refs; (6) 4 figures planned; (7) "fully crossed" qualified; (8) "diagnostic tool" either substantiated with code release or reframed. Verify whether these framing changes address the weak reject scores from first dream.

## paper_framing.md

# Paper Framing — nlp_variance_gtheory

## Target Venue
- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
- Extended: TACL (rolling)

## Title
Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics

## Core Claims (3 条，可证伪)

**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation, but its magnitude is benchmark-dependent: from ~45% on knowledge-retrieval tasks (MMLU) down to ~25% on reasoning tasks (GSM8K/MATH) where temperature and seed interactions increase. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating the systematic benchmark-dependent gradient, and (c) deriving D-study implications specific to LLM evaluation.

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

**Headline result template**: "In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (25-55%, benchmark-dependent), while direct infrastructure×methodology interactions are negligible (<0.5% binary, ≤1.3% text-match). Variance structure shifts systematically from item-dominated (knowledge benchmarks) to interaction-dominated (reasoning benchmarks). D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional: MMLU needs more items, GSM8K needs more seeds."

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
- Reviewer concern 3: "Item dominance is obvious from measurement theory" — Acknowledge explicitly. Contribution is quantification (25-55%), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.

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
  description: 'Full-scale precision study: 4 models (Qwen3-8B-Instruct, Llama-3.1-8B-Instruct,
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
    the residual component.

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

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: median
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
  "promptId": "31e420b1-6550-40f9-ab75-0e6113d15f14",
  "type": "user",
  "uuid": "ba8499f3-94ec-4ab9-8077-a7239a97ca5b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T22:42:38.125Z_

```json
{
  "parentUuid": "ba8499f3-94ec-4ab9-8077-a7239a97ca5b",
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
  "uuid": "43536103-ff4e-46ab-b9b0-1de8f1cc7913",
  "timestamp": "2026-05-20T22:42:38.125Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T22:42:38.125Z_

```json
{
  "parentUuid": "43536103-ff4e-46ab-b9b0-1de8f1cc7913",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "172469c9-f8fc-497b-82e9-26e92951b258",
  "timestamp": "2026-05-20T22:42:38.125Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Gradient exists but is noisy or only 2-cluster (knowledge vs reasoning); some claims need softening; paper is publishable with adjusted framing 核心假设：['It…",
  "leafUuid": "172469c9-f8fc-497b-82e9-26e92951b258",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define median-tier experiment predictions for nlp_variance_gtheory",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3"
}
```

---

### Assistant

_source line 8 · 2026-05-20T22:52:53.106Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined data for each planned experiment in the experiment_plan, under the "median" tier scenario. Each prediction needs a result_rationale explaining why this outcome occurs under the median tier.

Let me go through each planned experiment and generate detailed expected results consistent with the median tier definition.

Let me review the median tier key metric ranges:
- item_id_variance_mmlu_binary: [0.42, 0.55]
- item_id_variance_gsm8k_binary: [0.3, 0.42]


- item_id_variance_arc_binary: [0.38, 0.52]
- item_id_variance_hellaswag_binary: [0.25, 0.38]
- cross_benchmark_gradient_spread_pp: [10, 24]
- infra_x_method_binary_all_benchmarks: [0.0, 0.05]
- infra_x_method_textmatch_max: [0.015, 0.045]
- hardware_x_methodology_exp003: [0.005, 0.03]
- model_x_item_mmlu: [0.15, 0.28]

Now I'm looking at the remaining metric ranges to complete the median tier definition.

The narrative is shifting away from describing a clean gradient structure toward emphasizing benchmark-conditional variance instead — there's a two-cluster pattern rather than monotonic ordering. GSM8K items are showing stronger effects than expected, and the model-as-facet interaction is absorbing a larger share of variance from item effects than I initially thought. I need to refine the bootstrap confidence intervals and sample size requirements for the generalizability study.

Now looking at the experimental results more closely. The hardware effect is minimal, only accounting for 1-3% of precision variance. In the full MMLU study, item dominance is lower than the earlier MVP estimate of 58.4% — coming in around 48% when I account for the wider item sample and multiple models — with a G coefficient around 0.36. The item resampling experiment shows notable instability across the three independent samples, with cross-validation ranging from 15-25%, which suggests item effects aren't as stable as I'd hoped.

The multi-benchmark results reveal an interesting split: MMLU and ARC cluster together with high item dominance, while GSM8K and HellaSwag show much lower item effects. GSM8K came in higher than expected at 30-40%. When I treat the model as a separate facet rather than nesting it, it absorbs 15-25% of what I'd attributed to items. Bootstrap confidence intervals are fairly wide at 0.08-0.15, and I still need to work through the D-study projections to see what this means for generalizability. The 14B model extension and fine-tuning G-study should help clarify whether these patterns hold at different scales.

Now I'm setting up the detailed YAML structure for each experiment with specific metrics and variance components. For exp-001, the item variance sits around 0.48, and since I've fixed the precision confound by enforcing eager execution across all conditions, the main effect of precision should nearly disappear—the interaction with items will still be there but much smaller. The G coefficient should land around 0.36, and I'm working through what the residual variance looks like once everything else is accounted for.

I'm realizing I need to clarify how exp-001 treats model as a factor in its analysis. The description mentions validating the item dominance finding across multiple models, but the full model-as-facet reanalysis happens in exp-004. So exp-001 probably includes model in the variance decomposition but doesn't fully explore it as a separate dimension—model variance would either be pooled across conditions or absorbed into the residual depending on how the analysis is structured. I'm checking whether these variance proportions actually sum to one—item_id at 0.48 and model×item at 0.20 already account for 0.68 of the total, leaving only 0.32 for residual, precision, prompt, and other effects combined, which seems tight given the experimental design.

With model as a crossed facet, the original 58.4% item variance decomposes into pure item difficulty around 0.48, model-specific item interactions at 0.20, and the remaining 0.32 split across prompt:item, temperature:item, and residual noise—that allocation feels more plausible. The total item-related variance would be quite substantial, but the main item effect alone sits at roughly 48%.

Now I need to lay this out clearly and concisely, then figure out how to present the variance tables.

For exp-001, fixing the confound means FP32 accuracy should align with BF16/FP16 now, the precision main effect shrinks to near zero, and item_id stays dominant—though without the full model-as-facet decomposition, the basic analysis might still show item_id looking inflated. Since exp-001 includes four models, the basic variance breakdown will capture model effects anyway, but exp-004 is where I do the comprehensive reanalysis with bootstrap confidence intervals. So the split is: exp-001 reports the foundational variance decomposition including model, and exp-004 digs deeper with the crossed-facet structure and uncertainty quantification.

Writing YAML output... ~0.48 for item dominance once the model-as-facet separation is properly accounted for. I'm overcomplicating the narrative here—let me just lock in concrete numbers and write clear justifications. I'm setting up the median tier with a YAML structure that reframes the "systematic gradient" as a benchmark-conditional pattern: two clusters where knowledge tasks like MMLU and ARC show high item dominance, while reasoning tasks like GSM8K and HellaSwag are lower. Item effects remain dominant on knowledge benchmarks, but the earlier MVP estimate was inflated before properly disentangling model and item interactions. The separability finding holds at the aggregate level, though one reasoning benchmark shows a small infra×method interaction under binary scoring that needs flagging.

I'm also noting that bootstrap confidence intervals on the gradient endpoints overlap somewhat, so I need to soften magnitude claims while keeping directional ones intact. The paper hook should pivot to "variance structure depends on what you're benchmarking" rather than claiming a clean monotonic ordering. I'm targeting AAAI with this adjusted framing, with ACL ARR October as a fallback if I add another benchmark like MATH to strengthen the clustering story.

Now I'm sketching out the imagined experiments, starting with a full-scale MMLU precision study that fixes confounds by running 4 models across 3 precision levels with consistent eager execution, 6 different prompts, 6 random seeds, 3 temperature settings, 4 orderings, and 200 MMLU items to get precise estimates.

Looking at the expected results from this experiment—over a million observations across thousands of conditions—I'm seeing the accuracy patterns across precisions and the variance decomposition breakdown, where item difficulty dominates the variance structure, followed by residual noise, then various interaction effects. Looking at the cross-model consistency metric of 0.82, then examining how removing the FP32 engine confound dramatically shrinks the accuracy gap from 8.5 percentage points down to 0.6 percentage points — this confirms the MVP's FP32 degradation was almost entirely engine-related rather than precision-related. With that confound eliminated, precision's contribution to overall variance drops to just 0.3%, while item difficulty remains the dominant factor at 52%, though slightly lower than the MVP's 58.4% because the larger stratified sample captures more mid-range items that compress between-item variance.

The text-match results follow the same pattern as before with prompt and item interactions dominating, and the G-coefficient of 0.37 for binary scoring aligns with the MVP's 0.357, confirming that item difficulty variance is the fundamental constraint preventing higher reliability without substantially expanding the item pool. The residual variance at 19% is inflated because this basic analysis hasn't yet separated model effects from other sources — the next experiment will decompose this further using a model-as-facet approach.

Generating variance decomposition table... Generating variance decomposition tables... Now I'm looking at the visualizations I'm creating to support the analysis—stacked bar charts comparing variance decomposition across scoring methods, a heatmap showing how precision and temperature interact differently depending on item difficulty, and a scatter plot examining the relationship between item-level accuracy variance and difficulty across subject categories. The key insight is that the FP32 engine confound was driving the anomalous precision effect in the original analysis, and once corrected, precision contributes less than half a percent to total variance. Item dominance still accounts for about 52% of variance across the broader sample, slightly lower than the original 58% due to more diverse item selection, while text-match scoring continues to show a distinctly different variance structure. The precision gap between models maxes out around 0.6 percentage points, which falls within expected noise margins.

Now I'm planning a resampling stability test using three independent stratified samples of 200 MMLU items with different random seeds, running each through a single model across multiple precision levels, prompt variations, and orderings to verify that the item dominance effect remains stable regardless of which items are selected. The variation across samples shows that while item difficulty distribution shifts meaningfully—Sample 7 skews toward harder items (42% variance) and Sample 99 toward easier ones (44%)—the fundamental ranking of variance sources stays consistent, confirming item dominance is robust. This instability actually strengthens the paper's argument: the headline estimate of ~50% item contribution should be reported as a range (42-54%) with confidence intervals, which directly supports why D-study recommendations need uncertainty quantification rather than single point estimates.

Generating markdown table... Generating markdown table...

I'm visualizing the variance component distributions across the resamples with a forest plot and overlaying the item difficulty histograms to show how the stratification seed influences coverage. The 19% coefficient of variation sits right where I'd expect for this tier, and it's actually revealing—it demonstrates the item-sampling uncertainty that undermines single-draw studies. The variance hierarchy stays consistent with item_id dominating, though the exact percentages shift depending on the sample, which reinforces the D-study point: 200 items with a 19% CV on the primary component means practitioners shouldn't rely on one-off evaluations.

This also explains the discrepancy between Mesting (2026) and Brittlebench (2026)—they drew different item subsets from the same benchmark, leading to different variance structures. For the paper, I should report the mean and range rather than treating any single estimate as definitive.

Now I'm setting up the multi-benchmark replication across GSM8K, ARC, and HellaSwag with 4 models, two precision formats, multiple prompts, seeds, temperatures, and orderings—each benchmark gets 200 items. The expected variance components are already populated for GSM8K, and I'm continuing to fill in the projections for the other benchmarks. Compiling performance metrics across the remaining benchmarks... Looking at the interaction effects across benchmarks, the cross-benchmark pattern shows a clear 2-cluster structure: knowledge-retrieval tasks like MMLU and ARC cluster around 46-52% with item difficulty as the dominant factor, while reasoning tasks like GSM8K and HellaSwag cluster lower around 31-36% where temperature and seed variations have more influence on outcomes. sensitive to sampling randomness, so temperature×item and seed×item absorb variance that would otherwise be pure item difficulty. GSM8K's item dominance at 36% is higher than the hypothesized 20-30% because even in math reasoning, some items are trivially easy or impossibly hard for 8B models, creating a floor of item-driven variance. The 2-cluster pattern arises because ARC, despite being "science reasoning," is effectively knowledge retrieval — most items test factual recall rather than multi-step reasoning. Within-cluster ordering is unreliable across models, and the gradient spread of ~21pp is real but imprecise. Bootstrap confidence intervals on the endpoints will overlap partially, though infrastructure×method interactions remain negligible across all benchmarks under binary scoring. Under text-match scoring, GSM8K shows the largest precision×temperature interaction at 3.2% because exact-match scoring of multi-step math outputs is especially sensitive to token-level differences from floating-point precision.

Generating variance decomposition table... Generating benchmark comparison table... The core finding is a clear 2-cluster pattern — knowledge benchmarks (MMLU, ARC) versus reasoning benchmarks (GSM8K, HellaSwag) — rather than the hypothesized 4-point gradient, which means I need to reframe this as task-type-dependent variance structure instead of a systematic gradient. ARC clustering with MMLU rather than between them actually strengthens the finding since it shows variance tracks cognitive demands regardless of benchmark labels. The ~21 percentage point spread between clusters is meaningful though confidence intervals overlap at the edges, and GSM8K's 36% item dominance exceeds my initial 20-30% hypothesis, suggesting the gradient is steeper than expected.

For the second claim, separability holds across all benchmarks under binary scoring with negligible infrastructure-by-method interaction everywhere, which is stronger than the median tier prediction that anticipated one benchmark might show 2-5% interaction. Now I'm planning a multi-hardware generalization study across 4 models, 2 GPU types, multiple precisions and random seeds to quantify hardware effects on these findings. The FP16 precision gap of 0.8 percentage points is notably larger than BF16's 0.15 percentage points because FP16's narrower dynamic range makes it more sensitive to hardware-specific timing and memory subsystem variations, which aligns with recent research showing FP16's greater hardware dependency. The hardware×precision interaction effect at 0.8% for binary and 2.2% for text-match metrics represents the most significant finding, while the main hardware effect itself remains negligible since both GPUs execute the same IEEE 754 operations. Generating variance decomposition tables... The hardware effects are modest overall, but there's a critical interaction between precision and hardware—FP16 shows much greater sensitivity than BF16, which aligns with known limitations in floating-point range. When I look at the variance breakdown, hardware accounts for 3.6% under binary scoring but jumps to 7.2% with text-match evaluation, suggesting the metric choice significantly amplifies hardware sensitivity. For the separability claim, the hardware×methodology interaction is small but present, so I should frame it as approximately separable while noting the FP16 caveat.

Now I'm planning a comprehensive reanalysis across all experiments that treats the model as a facet in the generalizability theory framework, adds bootstrap confidence intervals, projects D-study estimates, compares REML and Henderson methods, incorporates logprob scoring, examines ranking stability, and estimates higher-order interactions. Now I'm looking at the confidence intervals for the gradient endpoints across different benchmarks, and they show a small overlap zone which suggests the direction is statistically significant. I'm also calculating the D-study projections to determine how many items would be needed to achieve 90% and 95% generalizability across MMLU, GSM8K, ARC, and HellaSwag. Looking at the variance decomposition results, the model-by-item interaction is absorbing a meaningful chunk of what initially appeared as pure item difficulty—about 21% on MMLU—which suggests that items don't have universal difficulty across models but rather model-specific challenges reflecting different knowledge gaps. The remaining 48% item variance is still the dominant factor, but now more accurately attributed, and the bootstrap confidence intervals around 0.14 width align well with the expected range, indicating stable estimates even with the resampling variability.

The gradient comparison between MMLU and HellaSwag shows they do overlap at the boundaries (0.38 to 0.41), confirming the direction is clear but the magnitude is uncertain—I can say MMLU is higher but only estimate a 10-30 percentage point range rather than claiming a precise 21 point difference. The generalizability study reveals MMLU requires 420 items to reach G≥0.90 while GSM8K needs just 280, showing a real difference in item requirements but less dramatic than initially expected.

The practical takeaway is that MMLU needs roughly 1.5 times more items than GSM8K, not the 3 times I'd hoped for. REML and Henderson methods agree within 2.1 points, so the choice of estimation approach doesn't shift the conclusions. Logprob scoring pushes the item_id variance component to 55% because it captures continuous difficulty gradations better than binary right/wrong scoring. Model rankings flip about 12% of the time across different condition pairs, primarily due to temperature variations—this matters for leaderboards that lock in specific evaluation conditions.

Generating markdown table... Generating markdown table... Generating markdown table...

The model-as-facet reanalysis is the key finding here — it shows that treating model as a random factor rather than fixed reveals a substantial 21% model×item interaction that prior work missed by conflating item difficulty with model-specific performance patterns. The bootstrap confidence intervals suggest the 2-cluster pattern is directionally stable but the magnitude should be reported as a 10-30pp range rather than a point estimate. D-study projections show benchmarks converge at different rates (MMLU needs ~420 items versus HellaSwag's ~240 for adequate generalization), though the actual ratio is less extreme than a simple gradient would predict, which still supports benchmark-specific evaluation budgets but with more nuance needed.

Now I'm planning an extension to 14B-scale models using Qwen3 and DeepSeek-R1-Distill across multiple experimental conditions to test whether the interaction patterns hold at this model size, with expected accuracy and variance estimates already projected. The 14B models show a modest 4 percentage point reduction in item_id variance compared to 8B, since higher capacity means fewer items are answered incorrectly, though item difficulty still dominates the variance structure. DeepSeek-R1-Distill-14B exhibits heightened sensitivity to temperature in its reasoning chains—about 8% compared to 5% for standard dense models—reflecting how distilled reasoning architectures respond differently to sampling variation. The model×item interaction grows to 25% because the architectural difference between reasoning-distilled and dense models creates distinct item-specific strengths: DeepSeek performs better on reasoning tasks while Qwen excels on knowledge-based items. The overall variance hierarchy remains stable across the 8-14B range, with item_id still dominating, and the precision gap stays negligible at 0.3 percentage points. Looking at the variance decomposition results, the 14B models show item difficulty becoming less dominant while model-by-item interactions grow stronger—likely because the larger models have more architectural diversity. This pattern validates that the variance structure holds across the scale range, though the magnitude of item effects does shift with model size. I should frame this as supporting evidence for the scope rather than a primary finding.

Now I'm moving into the fine-tuning analysis with RoBERTa on text classification tasks.  I'm running a large factorial experiment across SST-2, RTE, COPA, and MNLI with multiple seeds, learning rates, data shuffles, and hardware configurations to decompose variance sources. The expected results show distinct patterns: SST-2 with its large dataset exhibits dominant learning rate effects and seed variance, while RTE's smaller dataset shows data shuffle variance becoming nearly as important as learning rate, with much higher overall accuracy variability. Generating variance table... Generating markdown table...

The fine-tuning results reveal a striking contrast with inference—hyperparameters dominate rather than item properties, which aligns with the hypothesis that variance structure depends on the task type. The learning rate effect scales with dataset size while shuffle matters more for smaller datasets, mirroring how inference variance shifts between knowledge-based and reasoning tasks. Hardware and precision effects remain negligible across both settings, making this a key discussion point: reproducibility budgets from inference don't transfer to fine-tuning evaluations. One limitation is that these findings come from encoder-only models like RoBERTa, so decoder fine-tuning might behave differently.

Now I'm planning an experiment to test LayerCast—a mixed-precision approach using FP16 storage with FP32 computation—as an additional condition on MMLU. I'm expecting it to achieve around 68.3% accuracy with roughly a 0.1 percentage point gap versus BF16 and 0.2 points versus FP16, while reducing the precision-by-item interaction by about 45% compared to pure FP16. The inference overhead should stay around 18%.

The rationale is that LayerCast's FP32 compute path eliminates the accumulation errors that make items near decision boundaries sensitive to precision loss, so items stop flipping answers due to reduced-precision arithmetic. This puts accuracy between BF16 and FP32 since it preserves compute precision while using FP16 storage. The item-level variance stays high at 51% because LayerCast addresses precision sensitivity rather than item difficulty itself, and the g-coefficient remains unchanged since the dominant source of variance comes from item differences rather than precision effects.

Generating comparison table... Now I'm planning the MATH benchmark extension with 200 items across multiple models, precisions, prompts, seeds, temperatures, and orderings to measure chain-of-thought reasoning variance. The expected results show item effects dominating at 28%, with residual variance at 22%, while precision has negligible impact at 0.2%.

Looking at the cross-benchmark patterns, MATH clusters at the lower end with the lowest item dominance compared to MMLU and ARC, likely because multi-step proofs create substantial variance through different reasoning paths—temperature and seed interactions with items are particularly strong at 15% and 12% respectively, since sampling randomness determines which solution approach the model takes. are more clearly separated with MATH added. If the timeline permits, including MATH shifts the narrative from a "2-cluster" pattern to a "task-complexity gradient," which is a much stronger empirical claim. Now I'm looking at the variance decomposition across these benchmarks to see how MATH compares to GSM8K and MMLU in terms of what's driving the performance differences. Generating markdown table...

The MATH benchmark completes the 5-benchmark set and pushes toward a compelling 3-tier gradient narrative—moving from knowledge-based tasks through reasoning to proof-based problems. Adding this fifth benchmark strengthens the story about how task complexity drives variance structure, though there's still some noise in the within-tier ordering that I need to address.

Now I'm reconsidering the median-tier results. The infra×method interaction for binary classification was 0.3%, which falls well within the 0-5% range specified in the guidance, so that actually supports the separability claim on knowledge benchmarks rather than contradicting it. I need to adjust GSM8K to show the infra×method interaction at around 3% under binary scoring, keeping the other reasoning benchmarks near 0%, which aligns with the narrative requirement. I'm also reconsidering what "infra×method" means—it's likely the direct infrastructure and methodology interaction without item-level factors, so I'll increase the precision×temperature and precision×seed contributions accordingly.

Now I'm verifying that all my numbers across experiments are internally consistent and checking that the key metrics fall within their specified ranges. Looking at the rest of the validation metrics, all the remaining parameters are checking out within their expected ranges too. The MMLU and GSM8K correctness scores are solid, the bootstrap confidence intervals are tight, and the resampling variability is reasonable. The generalizability study suggests I need around 420 items for MMLU and 280 for GSM8K to hit the 90% confidence threshold.

Now I'm refining experiment 002 to properly capture the GSM8K infrastructure-by-method interaction effect at roughly 3% — breaking down the precision×temperature, precision×prompt, and precision×seed components. This represents the median-tier scenario where one reasoning benchmark shows that interaction effect in the 2-5% range.

I'm ready to synthesize all this into the final YAML output, making sure the narrative reflects these findings across all four experiments and how the model-as-facet adjustment progressively clarifies the variance decomposition.

One thing I need to reconcile: the item_id variance numbers in the key metrics likely represent the final model-as-facet versions from experiment 004, so I should use those as the authoritative figures while noting that the basic analysis in experiment 002 would show slightly inflated item_id effects due to model not being properly factored out.

Looking at the workflow more carefully, it seems experiments 001 and 002 collected data across multiple models but their basic analyses probably didn't treat model as a proper random facet—they might have pooled across models or fixed model effects. Then experiment 004 comes in and redoes the analysis with model properly crossed as a random factor, which is why those numbers would be lower and more accurate.

So the reported item_id values would be inflated in the basic analyses, then corrected downward in experiment 004 once model is properly decomposed. Rather than trying to track two sets of numbers, I should just use the final model-as-facet values throughout and note that the earlier experiments used a simpler pooled approach.

Let me restructure this: report the basic pooled numbers for experiments 001 and 002, then show how experiment 004's model-as-facet reanalysis brings those down to the final values that appear in the paper. For experiment 002 specifically, the basic analysis would show GSM8K around 40% and ARC around 50%, which then get adjusted down to 36% and 46% respectively once the model effect is properly accounted for.

The interesting pattern is that the spread between benchmarks stays constant at 17 percentage points whether we're looking at the basic pooled numbers or the model-as-facet adjusted ones—it's just shifted downward. This makes sense because the model-by-item interaction absorbs roughly the same amount across all benchmarks, though I'm wondering if that's actually true or if knowledge benchmarks like MMLU and ARC might show different patterns than reasoning benchmarks where models have more varied strategies.

Looking at the specific numbers I have, MMLU's model-by-item interaction is around 21%, and I'm estimating similar ranges for the others—ARC at 18%, GSM8K at 25%, HellaSwag at 22%. But when I try to work through how the transition from basic to model-as-facet actually happens, the math gets messier than I expected, because the variance absorption isn't a simple linear relationship.

Rather than get stuck on the exact mechanics, I should focus on making sure the final analysis hits the target ranges I'm aiming for. For the basic experiment, I can report slightly higher numbers and then note that the refined analysis tightens them up. The GSM8K finding is particularly important to highlight—the infrastructure and method interactions there (totaling 3%) show that separability actually breaks down on reasoning tasks, which is a key part of the narrative.

Let me write out the YAML with all these considerations in mind. I'm verifying the metric interpretation—the `infra_x_method_binary_all_benchmarks` range of 0-5% means individual benchmarks can fall anywhere within that, so GSM8K at 3% fits perfectly. Now I'm structuring the final YAML output with the tier, narrative guidance, and eight imagined experiments, each containing the plan ID, description, expected results, rationale, tables, figures, and analysis sections. Writing the YAML output... observed score variance). With less item variance, the person/model being measured is more reliably distinguished across conditions. Actually wait, G-theory's G coefficient for decisions about persons (models) would depend on model variance relative to error. But in this study, we're interested in the reproducibility of the benchmark score for a given model across conditions (not the reliability of distinguishing between models).

The G coefficient here is about generalizability of a model's score across items and conditions. With high item_id variance, the score is very item-dependent, making it less generalizable → lower G. With lower item_id variance (GSM8K), the score is less item-dependent → higher G. This makes sense: GSM8K G=0.42 > MMLU G=0.37.

And HellaSwag with even lower item_id (31%) would have even higher G: I set it at 0.48. MATH at item_id=28% gets G=0.52. ARC at item_id=46% gets G=0.35. This inverse relationship between item_id and G makes sense in this context.

Now I'm ready to write the YAML. But I need to account for GSM8K's infra×method interaction that breaks separability—the result rationale should explain why this happens specifically for math tasks. Math generation produces longer multi-step chains-of-thought where FP16 versus BF16 precision differences accumulate, and when precision interacts with temperature's sampling randomness, it can shift probability distributions past decision boundaries differently for mathematical reasoning, which binary scoring captures through the final numerical answer.

This differs from MMLU where answers are single tokens and precision effects in a single forward pass are negligible. So my analysis should note that GSM8K's ~3% infra×method interaction under binary scoring breaks the universal separability claim and requires metric and benchmark qualification. Now I need to finalize the write-up and reconsider the cross_benchmark_gradient_spread_pp metric—my spread is 17pp (MMLU 48% minus HellaSwag 31% with model-as-facet), but I should verify what the basic analysis spread would be.

Checking the numbers: MMLU 52% minus HellaSwag 35% gives 17pp, and with model-as-facet it's also 17pp, both within the [10, 24] range. Adding MATH in exp-008 pushes the spread to 20pp (48% minus 28%), which is still within range. The 4-benchmark spread without MATH is 17pp, and with MATH it becomes 20pp. Now I'm writing the YAML and making sure all percentages are precise and consistent across benchmarks.

Generating variance decomposition table... I'm seeing the variance breakdown for GSM8K continues with several smaller factors, and the percentages add up correctly. This is getting quite granular with all these interaction terms, so I should simplify by grouping the minor contributors together for cleaner presentation. Continuing with the variance breakdown for the remaining benchmarks, showing how item difficulty dominates across ARC and HellaSwag as well, with residual variance and various interaction effects accounting for smaller portions. The numbers check out perfectly at 100%, so this decomposition works as-is. Though I'd normally expect to see more granular factors like precision and prompt effects, I can redistribute these percentages to capture those additional dimensions while keeping the total intact.

Now I'm looking at how the model-as-facet approach reshapes the variance breakdown compared to the basic model—the key shift is that treating model as its own factor plus its interaction with items accounts for 26 percentage points of variance that was previously absorbed into the residual and item effects. Looking at the variance breakdown after adding the model-facet interaction, the model×item term is capturing about 21 percentage points—mostly pulled from the residual variance that was previously unexplained, along with some of the item_id effect that was actually model-specific item difficulty. The smaller prompt:item and temp:item effects also shifted slightly as the model interaction absorbed their variance, while the new between-model effect accounts for 5 percentage points of the total. The "other" category shrinking from 6.7% to 0.4% makes sense because those cross-terms involving the model are now being explicitly attributed in the model-as-facet analysis. Now I need to write out the YAML configuration, but I should be careful to distinguish between the basic pooled-model analysis from exp-002 and the model-as-facet corrections from exp-004. Let me verify the model-as-facet results are hitting the target ranges: MMLU item_id at 48% is within [42%, 55%], GSM8K at ~36% is within [30%, 42%] (down from the basic 40%), and ARC at ~46% is within [38%, 52%] (down from 50%).

For the GSM8K infra×method interaction of 3%, that should remain stable in the model-as-facet analysis since infrastructure and methodology interactions are orthogonal to model effects. Now I'm ready to construct the comprehensive YAML, though I need to think through the exp-003 numbers more carefully for the multi-hardware G-study on MMLU.

Looking at the hardware×methodology breakdown, the total comes to 1.4% across precision, prompt, seed, and temperature interactions, which fits within the 0.5% to 3% range. The hardware main effect is 0.4%, and hardware×item accounts for 1.8%, bringing the total hardware-related variance to 3.6%. Under text-match scoring, the hardware main effect increases to 1.2% with different interaction patterns across the methodology components.

The narrative about hardware effects being 1-3% on specific precisions makes sense when I look at the FP16 gap—there's roughly a 2% effect across GPUs—while BF16 shows only about 0.3%, so the significant variance is really precision-dependent rather than uniform across all configurations.

Writing the YAML output...

Actually, I need to verify something about the bf16_eager_disentangle results—the precision effect was 97.4% of the total gap while engine contributed 2.6%, which means the raw precision difference between FP32 and BF16 using the same engine is around 8.28 percentage points. That's substantial, but I'm second-guessing whether exp-001 actually uses the same engine configuration to make this comparison valid. Looking at the disentangle results more carefully, the precision effect is actually 8.28 percentage points while the engine effect is only 0.22 percentage points — so FP32 really is substantially worse than BF16, and the engine confound was minimal. This directly contradicts the paper's framing that fixing the FP32 engine would make precision negligible. is that variance components measure proportions of total variance, not absolute effect sizes — so an 8.5 percentage point accuracy gap from precision can still represent a small fraction of overall variance if item differences span a much wider range. Looking back at the MVP results, precision's main effect didn't even crack the top 5 variance sources, sitting below 5%, while item effects dominated at 58.4%.

The precision:item interaction (7.2%) is what actually shows up in the decomposition because precision affects different items differently, whereas the main effect is just a constant shift across 3 levels. Even if fixing the V0 confound in exp-001 only accounts for 2.6% of the gap, the precision main effect would still be around 8 percentage points in absolute terms, but its variance component contribution would remain small relative to item variance.

Now I'm realizing my imagined data for exp-001 doesn't match up—I had the FP32-BF16 gap at only 0.6 percentage points, but the disentangle showed the real precision gap is 8.28 percentage points, so exp-001 with V0 enforce_eager should show a similar gap. The issue is that the disentangle only used one model and 50 items, so there's a question of whether that gap generalizes.

Actually, the more fundamental problem is that FP32 should theoretically be better than or equal to BF16 since it has more precision, so an 8pp deficit doesn't make sense unless vLLM's FP32 computation path is doing something different—maybe the enforce_eager mode is introducing some rounding behavior that hurts accuracy.

Given that the disentangle experiment concluded the confound wasn't the main cause, the 8pp gap is probably real, which means the paper would need to explain why FP32 underperforms BF16 in vLLM specifically rather than as a general precision issue.

But looking back at the paper's framing around "conditional separability" and infrastructure factors being approximately separable from methodology factors, if the fix doesn't actually change the result much, then the fix validates the methodology but confirms the precision effect is genuine. The reviewer concern about FP32 degradation being known from prior work could be reframed as a supporting finding with a novel item-level breakdown rather than a novel discovery.

For my experiment design, I need to revise the imagined data: FP32 should show notably lower accuracy than BF16/FP16, the precision main effect might account for 3-5% of variance, but the key insight is that precision and methodology interactions should remain near zero—it's the precision-by-item interaction that will be substantial. Looking at the median tier metrics though, I don't see a specific metric capturing the precision main effect directly.

Now I'm realizing there's a puzzle here: in the MVP under binary scoring, the precision main effect wasn't even in the top 5 sources of variance (all below 5%), yet there was an 8.5 percentage point accuracy gap between FP32 and the other precisions. I need to work through the G-theory calculation to understand how that's possible—the variance of the precision level means should explain this discrepancy. The precision effect is small relative to overall variance since items vary so dramatically more than precision levels do, so even an 8 percentage point shift is proportionally minor. For my synthetic data, I'll set FP32 noticeably lower than BF16 and FP16, account for precision contributing around 3% of total variance with a 4-5% interaction effect between precision and items, then adjust the exp-001 accuracy values downward slightly since 200 items might include harder ones.

With 4 models across 200 stratified MMLU items, the baseline BF16 accuracy would likely sit around 0.68-0.70, making FP32 around 0.60-0.62 after the 8 percentage point penalty—though that seems low given these models typically score 70%+ on MMLU, so I need to account for the fact that the MVP's 0.5994 was specific to Llama-3.1-8B-Instruct on just 50 items, and averaging across 4 models with a larger sample would shift the baseline differently.

The FP32 degradation appears to be model-dependent rather than uniform, so I'm estimating individual FP32 accuracies for each model based on their likely sensitivity to precision loss, then averaging them to get a more realistic aggregate picture. I'm setting the precision:item interaction at around 5% of variance, which captures how different items respond differently to precision changes. This keeps the story coherent—the confound fix in exp-001 reveals that FP32's lower accuracy is genuinely a precision effect, not just an artifact of the experimental setup, even though the overall precision gap is modest at roughly 3 percentage points on average. Looking at the variance decomposition totaling 100%, I'm realizing that when models are pooled together in the basic analysis, their variance gets absorbed into the item_id and residual components, which is why item_id sits at 48% here. Once I factor in model as a separate dimension, that 48% should decrease as model variance gets extracted out, bringing item_id down to somewhere in the target range of 42-55%. single-model because some between-model disagreement reduces the "consensus" item difficulty. So I'm settling on pooled item_id around 52% and model-as-facet at 48% with model×item at 21%, meaning the facet approach absorbs about 4 percentage points from item variance while the remaining 17 comes from residual and other sources. For precision, the real FP32 gap of 3 percentage points should push it higher than the initial 0.3% estimate, though it'll still be dwarfed by item variance.

Now I'm laying out the full variance decomposition for the basic exp-001 setup with precision properly accounted for at 3%, showing how all the components—item interactions, residual, and main effects—sum to 100%.

For the text-match task, I'm adapting the MVP's decomposition pattern to the larger exp-001 scale, where residual and prompt-item interactions still dominate but temperature effects are somewhat reduced, and I'm adding in the precision and item_id contributions that weren't explicitly broken out before.

The variance components sum to 100%, confirming the allocation is balanced. Since text-match relies on exact string matching, precision differences show up more clearly here than in other metrics.

Now I'm ready to write out the final YAML structure, formatting the tables as lists of dictionaries with columns and rows as specified in the template. I need to ensure all the numbers stay internally consistent across experiments and align with the GSM8K infrastructure-by-method interaction baseline of around 3%.

For GSM8K specifically, the precision-temperature interaction compounds to about 2.2%, precision-seed adds 0.5%, and precision-prompt contributes 0.3%, totaling roughly 3% under binary scoring—this makes sense because longer reasoning chains amplify how temperature and precision interact, potentially shifting which reasoning path the model takes. The other benchmarks show smaller interactions: MMLU around 0.4% due to short single-token answers, ARC at 0.3%, and HellaSwag at 0.2% since it already achieves high accuracy.

Writing the YAML configuration...

Now I'm clarifying the interaction structure: precision is an infrastructure factor, while prompt, seed, temperature, and ordering are methodology factors. The infra×method interactions I need to report are between precision and each of those methodology variables, not between precision and individual items.

For GSM8K, the two-way interactions total around 3.0%, with temperature showing the strongest effect at 2.2%. MMLU shows much smaller interactions at 0.35% total. I should note that MMLU results come from exp-001 while the other benchmarks come from exp-002, so I need to keep those sources straight when building the cross-benchmark comparison table.

Let me finalize the key variance components I'll be reporting: MMLU shows item_id at 48%, model×item at 21%, with smaller contributions from precision, temperature, and prompt interactions. I'm ready to write this up now. Now I'm looking at the variance breakdown for ARC and HellaSwag, where item effects remain dominant but model interactions and temperature variations play meaningful roles across these benchmarks. Now I'm checking the cross-benchmark patterns—MMLU and ARC cluster together in the 46-48% range while GSM8K and HellaSwag fall lower at 31-36%, which matches the expected two-cluster structure. The generalizability coefficients look solid across all benchmarks, and the bootstrap confidence intervals are within target at 0.14 width. For the D-study analysis, I'm verifying that both MMLU and GSM8K would need 280-420 items to reach the 0.90 reliability threshold, which aligns with the specified ranges.

The item resampling cross-validation error of 0.19 is acceptable, and the hardware interaction effect from experiment-003 is minimal at 1.4%, confirming the methodology is robust. All validation checks pass, so I'm ready to construct the full YAML output with comprehensive data for all eight planned experiments, making sure each one includes detailed result rationales as requested.

For the basic MMLU analysis in exp-001, I need to be clear that the 52% item dominance figure reflects pooling effects before the model-as-facet approach is introduced in exp-004. My structure will organize the experiments sequentially: starting with the foundational MMLU analysis, moving through resampling validation, multi-benchmark patterns, hardware interactions, and culminating in the combined analysis with bootstrap confidence intervals and generalizability studies.

Continuing with the remaining experiments—exp-005 covers 14B model scaling validation, exp-006 examines fine-tuning with a different variance structure, exp-007 tests LayerCast as a minor mitigation strategy, and exp-008 explores MATH performance with potential three-tier gradient patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "172469c9-f8fc-497b-82e9-26e92951b258",
  "isSidechain": false,
  "requestId": "req_011CbEdQBG1rK7Tjzmhe68Y8",
  "type": "assistant",
  "uuid": "23bb16bc-8444-433e-8339-e59084ddebb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pm13He2zchUaGL4kZg4VJV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12069,
      "cache_read_input_tokens": 11841,
      "output_tokens": 51219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 51219,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12069
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

_source line 9 · 2026-05-20T22:58:31.499Z_

```yaml
tier: median
narrative_guidance: >
  Soften "systematic gradient" to "benchmark-conditional variance structure" or "task-type clustering."
  Cross-benchmark pattern is 2-cluster ({MMLU, ARC} high item dominance vs {GSM8K, HellaSwag} lower),
  not a clean monotonic 4-point gradient. Item dominance remains dominant on knowledge benchmarks but
  magnitude is less precise than MVP suggested once model-as-facet is handled and bootstrap CIs computed.
  Separability holds on knowledge benchmarks but GSM8K shows infra×method ~3% under binary scoring,
  requiring benchmark+metric qualification on Claim 2. Bootstrap CIs on gradient endpoints overlap
  partially — directional claims hold, magnitude claims are imprecise. Reframe hook: "the variance
  structure itself depends on what you're benchmarking" rather than a clean ordering. FP32 degradation
  is real (not engine confound), position as known finding (Yuan 2025) with novel item-level G-theory
  breakdown. Model-as-facet absorption (21% on MMLU) reframes prior single-model studies as having
  overestimated pure item dominance — turn this into a feature, not a weakness. Target AAAI with
  adjusted framing; if exp-008 (MATH) is feasible and strengthens the clustering to 3-tier, include it;
  otherwise ACL ARR October is a comfortable fallback.

imagined_experiments:
  - name: "Full-scale MMLU precision study (confound-fixed)"
    plan_id: "exp-001"
    description: >
      4 models × 3 precisions (FP32/BF16/FP16, all V0 enforce_eager) × 6 prompts × 6 seeds ×
      3 temperatures × 4 orderings × 200 MMLU items (stratified). 1,036,800 total observations.
    expected_results:
      total_observations: 1036800
      total_conditions: 5184
      accuracy_fp32: 0.655
      accuracy_bf16: 0.684
      accuracy_fp16: 0.681
      accuracy_gap_fp32_bf16_pp: 2.9
      accuracy_gap_bf16_fp16_pp: 0.3
      accuracy_by_model:
        qwen3_8b:  { fp32: 0.695, bf16: 0.710, fp16: 0.706 }
        llama31_8b: { fp32: 0.600, bf16: 0.672, fp16: 0.669 }
        gemma2_9b:  { fp32: 0.638, bf16: 0.660, fp16: 0.658 }
        mistral_7b: { fp32: 0.688, bf16: 0.694, fp16: 0.691 }
      # Basic G-theory decomposition (model pooled, not yet facet-separated)
      item_id_variance_binary: 0.52
      residual_variance_binary: 0.14
      precision_x_item_binary: 0.050
      prompt_x_item_binary: 0.058
      temperature_x_item_binary: 0.055
      seed_x_item_binary: 0.028
      precision_main_binary: 0.030
      temperature_main_binary: 0.015
      prompt_main_binary: 0.008
      ordering_main_binary: 0.002
      precision_x_temperature_binary: 0.002
      precision_x_prompt_binary: 0.001
      precision_x_seed_binary: 0.001
      other_binary: 0.090
      # Text-exact-match decomposition
      residual_textmatch: 0.36
      prompt_x_item_textmatch: 0.33
      temperature_main_textmatch: 0.14
      precision_x_item_textmatch: 0.04
      precision_x_temperature_textmatch: 0.022
      temperature_x_item_textmatch: 0.03
      item_id_textmatch: 0.03
      precision_main_textmatch: 0.025
      other_textmatch: 0.023
      # G coefficients
      g_correct_binary: 0.37
      g_correct_textmatch: 0.97
      # Cross-model consistency
      item_id_rank_corr_across_models: 0.82
      fp32_gap_model_range_pp: [1.5, 7.2]
    result_rationale: >
      V0 enforce_eager for all precisions eliminates the 0.22pp engine confound (bf16_eager_disentangle)
      but the FP32 accuracy gap PERSISTS at ~2.9pp average — confirming the disentangle conclusion that
      97.4% of the gap was genuine precision effect. FP32 degradation is strongly model-dependent:
      Llama-3.1-8B shows 7.2pp gap (consistent with MVP's 8.5pp on this model) while Qwen3-8B shows
      only 1.5pp, likely because Qwen's training used mixed-precision strategies that are more robust to
      FP32 inference rounding. Precision main effect at 3% is real but dwarfed by item_id at 52%.
      Precision:item at 5% means certain items (those near decision boundaries) are disproportionately
      affected — this is the novel item-level breakdown that extends Yuan et al. (2025). Item_id at 52%
      is lower than MVP's 58.4% because 200 stratified items (vs 50) include more mid-difficulty items
      that reduce between-item variance, and pooling across 4 models absorbs some item-specific variance
      into residual. Residual at 14% is inflated because model effects are pooled — exp-004 will
      decompose this. G=0.37 replicates MVP's 0.357, confirming item dominance makes G≥0.90 unreachable
      without massive item expansion. Text-match scoring replicates the qualitative shift: prompt:item
      dominates (33%), precision×temperature at 2.2% (consistent with MVP's 1.3% but larger due to
      more conditions), driven by floating-point non-associativity in generation.
    tables:
      - name: "Table 1: MMLU Variance Decomposition — Binary Correct (Basic, Model Pooled)"
        columns: ["Source", "% Total Variance"]
        rows:
          - ["item_id", "52.0%"]
          - ["residual (includes model effects)", "14.0%"]
          - ["prompt:item", "5.8%"]
          - ["temperature:item", "5.5%"]
          - ["precision:item", "5.0%"]
          - ["precision (main)", "3.0%"]
          - ["seed:item", "2.8%"]
          - ["temperature (main)", "1.5%"]
          - ["prompt (main)", "0.8%"]
          - ["infra×method (all)", "0.4%"]
          - ["ordering", "0.2%"]
          - ["other 2-way / 3-way", "9.0%"]
      - name: "Table 2: MMLU Variance Decomposition — Text Exact Match (Basic)"
        columns: ["Source", "% Total Variance"]
        rows:
          - ["residual", "36.0%"]
          - ["prompt:item", "33.0%"]
          - ["temperature (main)", "14.0%"]
          - ["precision:item", "4.0%"]
          - ["temperature:item", "3.0%"]
          - ["item_id", "3.0%"]
          - ["precision (main)", "2.5%"]
          - ["precision×temperature", "2.2%"]
          - ["other", "2.3%"]
      - name: "Table 3: Per-Model Accuracy by Precision (V0 enforce_eager)"
        columns: ["Model", "FP32", "BF16", "FP16", "FP32-BF16 Gap"]
        rows:
          - ["Qwen3-8B-Instruct", "0.695", "0.710", "0.706", "1.5pp"]
          - ["Llama-3.1-8B-Instruct", "0.600", "0.672", "0.669", "7.2pp"]
          - ["Gemma-2-9B-IT", "0.638", "0.660", "0.658", "2.2pp"]
          - ["Mistral-7B-v0.3", "0.688", "0.694", "0.691", "0.6pp"]
          - ["Average", "0.655", "0.684", "0.681", "2.9pp"]
    figures_description:
      - "Stacked bar: binary vs text-match variance decomposition side by side, showing metric-conditional
        shift from item-dominated (binary) to prompt-dominated (text-match)."
      - "Heatmap: FP32 degradation (pp) by model × item difficulty quartile, showing model-dependent
        and difficulty-dependent precision sensitivity."
      - "Scatter: item-level accuracy variance vs item difficulty, colored by MMLU subject category."
    analysis: >
      Key finding: FP32 degradation is REAL, not an engine confound. The bf16_eager_disentangle result
      is confirmed at scale — V0 enforce_eager changes nothing substantial. This reframes the
      contribution: we provide the first item-level G-theory decomposition of precision effects,
      showing that precision:item (5%) exceeds precision main (3%). The model-dependence of FP32
      degradation (1.5-7.2pp) is novel and suggests training-time precision choices affect inference
      robustness. For the paper: position FP32 degradation as supporting Yuan et al. (2025) with
      novel item×model granularity, NOT as a primary finding. Separability on MMLU is confirmed:
      infra×method = 0.4% binary, 2.2% text-match (precision×temperature only). CIs deferred to
      exp-004.

  - name: "Item resampling stability test"
    plan_id: "exp-001b"
    description: >
      3 independent stratified samples of 200 MMLU items (seeds 0, 7, 99) × Llama-3.1-8B ×
      3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions/sample, 32,400 obs/sample.
    expected_results:
      item_id_sample_0: 0.49
      item_id_sample_7: 0.55
      item_id_sample_99: 0.44
      item_id_mean: 0.493
      item_id_sd: 0.055
      item_id_cv: 0.19
      g_coeff_sample_0: 0.36
      g_coeff_sample_7: 0.32
      g_coeff_sample_99: 0.39
      accuracy_sample_0: 0.668
      accuracy_sample_7: 0.641
      accuracy_sample_99: 0.679
      mean_item_difficulty_sample_0: 0.50
      mean_item_difficulty_sample_7: 0.42
      mean_item_difficulty_sample_99: 0.54
      sd_item_difficulty_sample_0: 0.28
      sd_item_difficulty_sample_7: 0.32
      sd_item_difficulty_sample_99: 0.25
      rank_order_top3_sources_preserved: true
      residual_cv: 0.11
      prompt_item_cv: 0.09
    result_rationale: >
      CV of 19% reflects meaningful item-sampling uncertainty. MMLU has 14,042 items across 57 subjects
      with heterogeneous difficulty; stratified sampling with 200 items (1.4%) leaves substantial
      sampling variance especially in the tails. Sample 7 draws more hard items (mean difficulty 0.42),
      inflating between-item variance to 55% because the difficulty spread is wider (SD 0.32). Sample 99
      draws more mid-difficulty items (mean 0.54, SD 0.25), compressing item_id to 44% because items
      cluster around the center. Despite magnitude variation, the qualitative hierarchy is preserved:
      item_id ranks #1 in all 3 samples, residual #2, prompt:item #3. This stability-in-rank with
      instability-in-magnitude is the key finding: the headline claim "item dominance ~50%" needs error
      bars, reported as "44-55% across independent 200-item stratified draws." The G-coefficient varies
      inversely (0.32-0.39) because higher item variance = lower generalizability of the benchmark score.
      This directly motivates D-study item-count recommendations with CIs, not point estimates — if your
      headline variance component shifts ±5pp with a different item draw, your optimal resource allocation
      shifts too.
    tables:
      - name: "Table 4: Resampling Stability of Variance Components"
        columns: ["Source", "Sample 0", "Sample 7", "Sample 99", "Mean", "CV"]
        rows:
          - ["item_id", "49.0%", "55.0%", "44.0%", "49.3%", "0.19"]
          - ["residual", "17.5%", "15.0%", "19.5%", "17.3%", "0.11"]
          - ["prompt:item", "6.5%", "6.0%", "7.0%", "6.5%", "0.09"]
          - ["temp:item", "5.8%", "5.2%", "6.5%", "5.8%", "0.10"]
          - ["prec:item", "5.0%", "5.5%", "4.2%", "4.9%", "0.12"]
          - ["precision", "3.0%", "3.5%", "2.8%", "3.1%", "0.10"]
          - ["other", "13.2%", "9.8%", "16.0%", "13.0%", "—"]
      - name: "Table 5: Per-Sample Summary Statistics"
        columns: ["Metric", "Sample 0", "Sample 7", "Sample 99"]
        rows:
          - ["N items", "200", "200", "200"]
          - ["Mean item difficulty", "0.50", "0.42", "0.54"]
          - ["SD item difficulty", "0.28", "0.32", "0.25"]
          - ["Overall accuracy", "0.668", "0.641", "0.679"]
          - ["G (binary)", "0.36", "0.32", "0.39"]
          - ["item_id %", "49.0%", "55.0%", "44.0%"]
    figures_description:
      - "Forest plot: item_id % with bootstrap 95% CIs across 3 resamples, showing overlapping but
        distinct intervals. Horizontal shaded band marks the MVP point estimate (58.4%) for comparison."
      - "Histogram overlay: item difficulty distribution for each sample, showing how stratification seed
        shifts the difficulty profile despite identical stratification ratios."
    analysis: >
      The 19% CV is the paper's best defense against "you just got lucky with your items." It quantifies
      the item-sampling uncertainty that plagues every single-draw benchmark study. Rank ordering is
      robust (item_id always #1) but precise magnitude depends on which items you drew — explaining why
      Mesting (2026) and Brittlebench (2026) reached different headline numbers on different item sets.
      For the paper: always report item_id as a range (44-55%) not a point. D-study projections from
      exp-004 should include CIs that account for this resampling instability.

  - name: "Multi-benchmark replication (GSM8K, ARC, HellaSwag)"
    plan_id: "exp-002"
    description: >
      4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings ×
      200 items on GSM8K, ARC-Challenge, HellaSwag. Reduced crossing vs exp-001.
    expected_results:
      total_observations_per_benchmark: 384000
      # GSM8K — basic analysis (model pooled)
      gsm8k_accuracy: 0.575
      gsm8k_item_id_binary: 0.40
      gsm8k_residual_binary: 0.15
      gsm8k_temp_x_item_binary: 0.10
      gsm8k_seed_x_item_binary: 0.07
      gsm8k_prompt_x_item_binary: 0.065
      gsm8k_temperature_binary: 0.04
      gsm8k_prec_x_temp_binary: 0.022
      gsm8k_prec_x_seed_binary: 0.005
      gsm8k_prec_x_prompt_binary: 0.003
      gsm8k_infra_x_method_total_binary: 0.030
      gsm8k_precision_main_binary: 0.010
      gsm8k_prec_x_item_binary: 0.015
      gsm8k_other_binary: 0.093
      gsm8k_g_correct_binary: 0.42
      # ARC-Challenge — basic analysis
      arc_accuracy: 0.625
      arc_item_id_binary: 0.50
      arc_residual_binary: 0.12
      arc_prompt_x_item_binary: 0.085
      arc_temp_x_item_binary: 0.055
      arc_seed_x_item_binary: 0.04
      arc_prec_x_item_binary: 0.025
      arc_temperature_binary: 0.025
      arc_precision_binary: 0.010
      arc_infra_x_method_total_binary: 0.005
      arc_other_binary: 0.115
      arc_g_correct_binary: 0.35
      # HellaSwag — basic analysis
      hellaswag_accuracy: 0.712
      hellaswag_item_id_binary: 0.35
      hellaswag_residual_binary: 0.18
      hellaswag_temp_x_item_binary: 0.095
      hellaswag_seed_x_item_binary: 0.085
      hellaswag_prompt_x_item_binary: 0.075
      hellaswag_temperature_binary: 0.045
      hellaswag_prec_x_item_binary: 0.015
      hellaswag_precision_binary: 0.005
      hellaswag_infra_x_method_total_binary: 0.003
      hellaswag_other_binary: 0.127
      hellaswag_g_correct_binary: 0.48
      # Cross-benchmark summary (basic, pre-model-facet)
      gradient_pattern: "2-cluster: {MMLU 52%, ARC 50%} vs {GSM8K 40%, HellaSwag 35%}"
      gradient_spread_pp: 17
      within_cluster_ordering_reliable: false
      # Text-match
      gsm8k_prec_x_temp_textmatch: 0.035
      arc_prec_x_temp_textmatch: 0.022
      hellaswag_prec_x_temp_textmatch: 0.016
      infra_x_method_textmatch_max: 0.035
    result_rationale: >
      The 2-cluster pattern emerges because variance structure tracks cognitive demand, not benchmark
      labels. Knowledge-retrieval benchmarks (MMLU, ARC) show high item dominance (50-52% basic) because
      item difficulty is the primary driver — items test factual knowledge that is either present or
      absent in the model, and this binary state dominates across conditions. ARC clusters with MMLU
      despite being labeled "science reasoning" because most ARC items are effectively factual recall
      (what happens when ice melts?) rather than multi-step inference. Reasoning benchmarks (GSM8K,
      HellaSwag) show lower item dominance (35-40%) because temperature and seed interact strongly with
      items: multi-step reasoning and commonsense inference have multiple valid processing paths, and
      sampling randomness determines which path is taken, shifting variance from item_id to interaction
      terms. GSM8K item dominance at 40% is above the hypothesized 20-30% because even math reasoning
      has trivially easy items (single-step arithmetic) and impossible items (complex multi-step for 8B
      models), creating a floor of item-driven variance. The critical median-tier finding: GSM8K shows
      infra×method = 3.0% under binary scoring (precision×temperature 2.2% + precision×seed 0.5% +
      precision×prompt 0.3%). This breaks universal separability. The mechanism: math generation produces
      longer chains-of-thought where BF16 vs FP16 accumulation differences compound; temperature controls
      how aggressively alternative reasoning paths are explored; the precision×temperature combination
      can push probability distributions past decision boundaries, flipping the final numerical answer.
      Binary scoring captures this because the extracted number differs. Other benchmarks show
      infra×method <0.5% binary — the effect is GSM8K-specific. Under text-match, GSM8K prec×temp
      reaches 3.5% because exact-string comparison of multi-step outputs amplifies floating-point
      divergence. The gradient spread of 17pp (MMLU 52% vs HellaSwag 35%, basic) is within the target
      range [10-24pp]; after model-as-facet correction in exp-004 it will be similar (48% vs 31% = 17pp).
    tables:
      - name: "Table 6: Cross-Benchmark Variance Decomposition — Binary (Basic, Model Pooled)"
        columns: ["Source", "MMLU", "GSM8K", "ARC", "HellaSwag"]
        rows:
          - ["item_id", "52.0%", "40.0%", "50.0%", "35.0%"]
          - ["residual", "14.0%", "15.0%", "12.0%", "18.0%"]
          - ["temp:item", "5.5%", "10.0%", "5.5%", "9.5%"]
          - ["seed:item", "2.8%", "7.0%", "4.0%", "8.5%"]
          - ["prompt:item", "5.8%", "6.5%", "8.5%", "7.5%"]
          - ["prec:item", "5.0%", "1.5%", "2.5%", "1.5%"]
          - ["precision (main)", "3.0%", "1.0%", "1.0%", "0.5%"]
          - ["temperature (main)", "1.5%", "4.0%", "2.5%", "4.5%"]
          - ["infra×method (total)", "0.4%", "3.0%", "0.5%", "0.3%"]
          - ["other", "10.0%", "12.0%", "13.5%", "14.7%"]
      - name: "Table 7: Cross-Benchmark Summary (Basic)"
        columns: ["Benchmark", "Task Type", "item_id %", "G (binary)", "infra×method", "Cluster"]
        rows:
          - ["MMLU", "Knowledge", "52.0%", "0.37", "0.4%", "High"]
          - ["ARC-Challenge", "Knowledge/Science", "50.0%", "0.35", "0.5%", "High"]
          - ["GSM8K", "Math reasoning", "40.0%", "0.42", "3.0%", "Low"]
          - ["HellaSwag", "Commonsense", "35.0%", "0.48", "0.3%", "Low"]
      - name: "Table 8: GSM8K Infra×Method Interaction Breakdown (Binary)"
        columns: ["Interaction", "% Total Variance", "95% CI (bootstrap, exp-004)"]
        rows:
          - ["precision×temperature", "2.2%", "deferred"]
          - ["precision×seed", "0.5%", "deferred"]
          - ["precision×prompt", "0.3%", "deferred"]
          - ["Total infra×method", "3.0%", "deferred"]
        note: "Only GSM8K exceeds 1% threshold. MMLU 0.4%, ARC 0.5%, HellaSwag 0.3%."
    figures_description:
      - "Stacked bar (signature figure): 4-benchmark variance decomposition, bars sorted by item_id
        descending, showing 2-cluster visual. Item_id bars in dark blue, interaction terms in lighter
        shades, precision/temperature main in warm tones."
      - "Scatter: item_id % vs benchmark task-type ordinal (knowledge → reasoning), with error bars from
        exp-001b resampling on MMLU. Shows cluster structure, not monotonic trend."
      - "Heatmap: pairwise Spearman correlation of per-item variance profiles across 4 benchmarks,
        showing r>0.7 within clusters and r<0.3 between clusters."
    analysis: >
      This is the core finding. The 2-cluster pattern is clear and the direction is robust, but it is
      NOT the clean monotonic gradient originally hypothesized. ARC clusters with MMLU (not intermediate)
      — this is actually a stronger finding than a gradient: variance structure tracks cognitive demand,
      and ARC's "science reasoning" label is misleading. The GSM8K infra×method at 3% binary is the
      median tier's key complication for Claim 2: separability is benchmark-conditional, not universal.
      The paper must add "on knowledge-retrieval benchmarks" or "when math reasoning is excluded" to the
      separability claim. Under text-match, GSM8K reaches 3.5% (within target [1.5%, 4.5%]). Practical
      implication: practitioners evaluating math reasoning on GSM8K should fix both precision AND
      temperature to minimize infra×method confounding.

  - name: "Multi-hardware G-study"
    plan_id: "exp-003"
    description: >
      4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions (BF16/FP16) ×
      6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items.
    expected_results:
      total_observations: 1152000
      # Variance components — hardware-related
      hardware_main_binary: 0.004
      hardware_x_precision_binary: 0.008
      hardware_x_temperature_binary: 0.003
      hardware_x_seed_binary: 0.002
      hardware_x_prompt_binary: 0.001
      hardware_x_methodology_total_binary: 0.014
      hardware_x_item_binary: 0.018
      total_hardware_related_binary: 0.036
      # Text-match
      hardware_main_textmatch: 0.012
      hardware_x_precision_textmatch: 0.022
      hardware_x_methodology_total_textmatch: 0.032
      hardware_x_item_textmatch: 0.028
      total_hardware_related_textmatch: 0.072
      # Non-hardware components (consistent with exp-001)
      item_id_with_hardware_binary: 0.50
      g_correct_binary_gpu1: 0.37
      g_correct_binary_gpu2: 0.36
      # Accuracy gaps by precision
      cross_gpu_gap_bf16_mean_pp: 0.12
      cross_gpu_gap_fp16_mean_pp: 0.75
      cross_gpu_gap_bf16_max_pp: 0.2
      cross_gpu_gap_fp16_max_pp: 1.1
      model_ranking_preserved_across_gpus: true
      # FP16-conditioned hardware effect
      hardware_variance_fp16_subset: 0.022
      hardware_variance_bf16_subset: 0.003
    result_rationale: >
      Hardware main effect at 0.4% binary is negligible because both GPUs implement the same IEEE 754
      operations; differences arise only from CUDA kernel scheduling nondeterminism and memory subsystem
      timing. The critical finding is hardware×precision at 0.8% binary: FP16 is more hardware-sensitive
      than BF16 (cross-GPU gap 0.75pp vs 0.12pp), because FP16's narrower dynamic range (5-bit exponent
      vs BF16's 8-bit) makes accumulation order hardware-dependent — consistent with Yuan et al. (2025).
      When subsetting to FP16-only data, hardware explains 2.2% of variance (within median narrative's
      "1-3% on one precision"). Under text-match, hardware effects roughly double (total 7.2%) because
      different GPU kernel orderings produce different final tokens in long generations, amplified by
      exact-match scoring. Hardware×item at 1.8% binary means certain items near decision boundaries are
      hardware-sensitive — the same items that are precision-sensitive (prec:item) are also
      hardware-sensitive, consistent with a shared mechanism of logit perturbation near thresholds.
      Model rankings are fully preserved across GPUs (Kendall tau = 1.0 at all condition combinations)
      — hardware effects are far too small to alter comparative model evaluation. Total hardware-related
      variance at 3.6% binary is manageable but nonzero, requiring "approximately separable" language.
    tables:
      - name: "Table 9: Hardware Facet Variance Components"
        columns: ["Source", "Binary %", "Text-match %"]
        rows:
          - ["hardware (main)", "0.4%", "1.2%"]
          - ["hardware×precision", "0.8%", "2.2%"]
          - ["hardware×temperature", "0.3%", "0.6%"]
          - ["hardware×seed", "0.2%", "0.4%"]
          - ["hardware×prompt", "0.1%", "0.3%"]
          - ["hardware×item", "1.8%", "2.8%"]
          - ["Total hardware-related", "3.6%", "7.5%"]
      - name: "Table 10: Cross-GPU Accuracy by Model and Precision"
        columns: ["Model", "GPU1-BF16", "GPU2-BF16", "Δ(pp)", "GPU1-FP16", "GPU2-FP16", "Δ(pp)"]
        rows:
          - ["Qwen3-8B", "0.710", "0.709", "0.1", "0.706", "0.700", "0.6"]
          - ["Llama-3.1-8B", "0.672", "0.672", "0.0", "0.669", "0.661", "0.8"]
          - ["Gemma-2-9B", "0.660", "0.659", "0.1", "0.658", "0.649", "0.9"]
          - ["Mistral-7B", "0.694", "0.693", "0.1", "0.691", "0.680", "1.1"]
      - name: "Table 11: Hardware Effect Conditioned on Precision"
        columns: ["Metric", "BF16 Only", "FP16 Only"]
        rows:
          - ["Hardware % total variance", "0.3%", "2.2%"]
          - ["Mean cross-GPU gap (pp)", "0.12", "0.75"]
          - ["Max cross-GPU gap (pp)", "0.2", "1.1"]
    figures_description:
      - "Paired dot plot: per-model accuracy on GPU1 vs GPU2, BF16 (nearly overlapping) vs FP16
        (visible gap), connected by lines to show model-specific hardware sensitivity."
      - "Bar chart: hardware-related variance by scoring metric, showing binary→text-match doubling."
    analysis: >
      Hardware is a manageable confound, not a showstopper. Separability claim (Claim 2) survives with
      qualification: "hardware×methodology is ≤1.4% under binary scoring" — but the FP16 hardware
      sensitivity (2.2% when conditioned on FP16) warrants a Discussion paragraph. Practical
      recommendation: prefer BF16 for hardware-independent reproducibility; if FP16 is necessary for
      memory, acknowledge ~1pp cross-GPU uncertainty. The hardware×item overlap with precision×item
      suggests a unified "logit perturbation" mechanism — items near decision boundaries are vulnerable
      to both precision and hardware nondeterminism. This is a potential Discussion point but not a
      formal claim.

  - name: "Comprehensive combined analysis"
    plan_id: "exp-004"
    description: >
      Reanalysis of all exp-001/001b/002/003 data: (a) model-as-facet G-theory, (b) bootstrap CIs
      (1000 resamples), (c) D-study projections, (d) REML vs Henderson, (e) logprob scoring,
      (f) ranking stability, (g) higher-order interactions.
    expected_results:
      # (a) Model-as-facet — MMLU
      mmlu_item_id_model_facet: 0.48
      mmlu_model_main: 0.05
      mmlu_model_x_item: 0.21
      mmlu_residual_model_facet: 0.08
      mmlu_prompt_item_model_facet: 0.053
      mmlu_temp_item_model_facet: 0.048
      mmlu_prec_item_model_facet: 0.028
      mmlu_precision_main_model_facet: 0.025
      mmlu_temperature_main_model_facet: 0.012
      # Model-as-facet — other benchmarks
      gsm8k_item_id_model_facet: 0.36
      gsm8k_model_x_item: 0.18
      gsm8k_model_main: 0.04
      arc_item_id_model_facet: 0.46
      arc_model_x_item: 0.16
      arc_model_main: 0.04
      hellaswag_item_id_model_facet: 0.31
      hellaswag_model_x_item: 0.19
      hellaswag_model_main: 0.05
      # Item dominance reduction from model-facet
      item_id_reduction_mmlu_pp: 4.0
      item_id_reduction_gsm8k_pp: 4.0
      item_id_reduction_arc_pp: 4.0
      item_id_reduction_hellaswag_pp: 4.0
      # (b) Bootstrap CIs (1000 resamples) on item_id
      mmlu_item_id_ci: [0.41, 0.55]
      mmlu_item_id_ci_width: 0.14
      gsm8k_item_id_ci: [0.29, 0.43]
      gsm8k_item_id_ci_width: 0.14
      arc_item_id_ci: [0.39, 0.53]
      arc_item_id_ci_width: 0.14
      hellaswag_item_id_ci: [0.24, 0.38]
      hellaswag_item_id_ci_width: 0.14
      # Gradient endpoint CI overlap
      gradient_high_endpoint_ci: [0.41, 0.55]    # MMLU
      gradient_low_endpoint_ci: [0.24, 0.38]      # HellaSwag
      gradient_endpoint_overlap: true
      gradient_overlap_range: [0.38, 0.41]         # 3pp overlap zone
      gradient_direction_p_value: 0.003
      # Bootstrap CIs on infra×method
      gsm8k_infra_x_method_ci: [0.012, 0.048]
      mmlu_infra_x_method_ci: [0.0, 0.012]
      # Bootstrap CIs on model×item
      mmlu_model_x_item_ci: [0.16, 0.27]
      # (c) D-study projections
      dstudy_items_g80_mmlu: 220
      dstudy_items_g90_mmlu: 420
      dstudy_items_g95_mmlu: 680
      dstudy_items_g80_gsm8k: 150
      dstudy_items_g90_gsm8k: 280
      dstudy_items_g95_gsm8k: 450
      dstudy_items_g80_arc: 200
      dstudy_items_g90_arc: 380
      dstudy_items_g95_arc: 620
      dstudy_items_g80_hellaswag: 130
      dstudy_items_g90_hellaswag: 240
      dstudy_items_g95_hellaswag: 400
      dstudy_optimal_prompts_mmlu: 3
      dstudy_optimal_seeds_mmlu: 4
      dstudy_optimal_prompts_gsm8k: 4
      dstudy_optimal_seeds_gsm8k: 6
      dstudy_items_g90_ci_mmlu: [350, 510]
      dstudy_items_g90_ci_gsm8k: [220, 360]
      dstudy_ratio_mmlu_vs_hellaswag: 1.75
      dstudy_ratio_mmlu_vs_gsm8k: 1.50
      # (d) REML vs Henderson
      reml_henderson_max_diff_pp: 2.1
      reml_henderson_rank_preserved: true
      # (e) Logprob scoring
      mmlu_item_id_logprob: 0.55
      mmlu_g_logprob: 0.32
      gsm8k_item_id_logprob: 0.42
      # (f) Ranking stability
      model_rank_flip_pct_across_conditions: 0.12
      rank_flip_driver: "temperature=1.0"
      precision_causes_rank_flip: false
      # (g) Higher-order interactions
      three_way_interactions_total_mmlu: 0.03
      three_way_interactions_total_gsm8k: 0.05
    result_rationale: >
      Model-as-facet is the most consequential reanalysis. On MMLU, 21% of total variance is model×item
      — this is not "model difficulty" but model-SPECIFIC item difficulty: items that are hard for
      Llama but easy for Qwen due to model-specific knowledge gaps and training data overlap. Absorbing
      this from item_id (52%→48%) and residual (14%→8%) properly attributes variance that prior
      single-model studies would have assigned to "item difficulty." The 4pp reduction is consistent
      across all benchmarks, suggesting the model-facet correction is systematic rather than
      benchmark-specific. Bootstrap CI width of 0.14 on item_id reflects both item-resampling
      instability (exp-001b CV=19%) and condition-resampling instability. The gradient endpoint CIs
      overlap narrowly: MMLU lower CI (0.41) exceeds HellaSwag upper CI (0.38) by only 3pp, so the
      gradient direction is statistically significant (p=0.003 by permutation test) but the magnitude
      is imprecise — the paper should say "10-30pp spread" not "17pp." D-study projections differentiate
      benchmarks: MMLU needs 420 items for G≥0.90 vs HellaSwag 240, a 1.75× ratio. This is directionally
      useful but less dramatic than a clean gradient would predict — the practical message is "50-75%
      more items for knowledge vs reasoning benchmarks," not "3× more items." D-study CIs on MMLU
      G≥0.90 ([350, 510]) show that even the recommended item count is imprecise. REML and Henderson
      agree to within 2.1pp — methodological choice doesn't affect qualitative conclusions. Logprob
      scoring increases item_id to 55% on MMLU because continuous logprobs capture fine-grained difficulty
      more sensitively than binary 0/1. Model rank flips occur in 12% of condition pairs, driven
      entirely by temperature=1.0 (high-temperature conditions produce enough noise to flip rankings of
      close models); precision never causes rank flips. Three-way interactions total 3-5% — most
      variance is captured by main effects and 2-way terms.
    tables:
      - name: "Table 12: Model-as-Facet Reanalysis — All Benchmarks (Binary)"
        columns: ["Source", "MMLU", "GSM8K", "ARC", "HellaSwag"]
        rows:
          - ["item_id", "48.0%", "36.0%", "46.0%", "31.0%"]
          - ["model×item", "21.0%", "18.0%", "16.0%", "19.0%"]
          - ["model (main)", "5.0%", "4.0%", "4.0%", "5.0%"]
          - ["residual", "8.0%", "10.0%", "8.0%", "10.0%"]
          - ["temp:item", "4.8%", "9.0%", "5.0%", "8.5%"]
          - ["seed:item", "2.0%", "5.5%", "3.0%", "7.0%"]
          - ["prompt:item", "5.3%", "5.5%", "7.5%", "6.5%"]
          - ["prec:item", "2.8%", "1.2%", "2.0%", "1.2%"]
          - ["precision (main)", "2.5%", "0.8%", "0.8%", "0.3%"]
          - ["temperature (main)", "1.2%", "3.5%", "2.2%", "4.0%"]
          - ["infra×method", "0.4%", "3.0%", "0.5%", "0.3%"]
          - ["other", "0.0%", "3.5%", "5.0%", "7.2%"]
        note: "Rows may not sum to 100% due to rounding and higher-order terms in 'other.'"
      - name: "Table 13: Bootstrap 95% CIs on Key Variance Components"
        columns: ["Component", "MMLU", "GSM8K", "ARC", "HellaSwag"]
        rows:
          - ["item_id", "[0.41, 0.55]", "[0.29, 0.43]", "[0.39, 0.53]", "[0.24, 0.38]"]
          - ["model×item", "[0.16, 0.27]", "[0.13, 0.24]", "[0.11, 0.22]", "[0.14, 0.25]"]
          - ["infra×method", "[0.00, 0.012]", "[0.012, 0.048]", "[0.00, 0.014]", "[0.00, 0.010]"]
        note: "1000 bootstrap resamples (items × conditions). GSM8K infra×method CI excludes 0."
      - name: "Table 14: D-Study — Items Needed for Target G (BF16, optimal prompt/seed)"
        columns: ["Benchmark", "G≥0.80", "G≥0.90", "G≥0.90 CI", "G≥0.95", "Prompts", "Seeds"]
        rows:
          - ["MMLU", "220", "420", "[350, 510]", "680", "3", "4"]
          - ["ARC", "200", "380", "[310, 470]", "620", "3", "4"]
          - ["GSM8K", "150", "280", "[220, 360]", "450", "4", "6"]
          - ["HellaSwag", "130", "240", "[190, 310]", "400", "4", "6"]
      - name: "Table 15: Scoring Metric Comparison (MMLU, Model-as-Facet)"
        columns: ["Source", "Binary", "Text-match", "Logprob"]
        rows:
          - ["item_id", "48.0%", "3.0%", "55.0%"]
          - ["model×item", "21.0%", "1.5%", "18.0%"]
          - ["prompt:item", "5.3%", "33.0%", "4.0%"]
          - ["residual", "8.0%", "36.0%", "6.0%"]
          - ["G coefficient", "0.37", "0.97", "0.32"]
      - name: "Table 16: REML vs Henderson Method I (MMLU, Binary)"
        columns: ["Source", "Henderson %", "REML %", "Diff (pp)"]
        rows:
          - ["item_id", "48.0%", "49.2%", "+1.2"]
          - ["model×item", "21.0%", "22.4%", "+1.4"]
          - ["residual", "8.0%", "6.1%", "-1.9"]
          - ["other sources", "23.0%", "22.3%", "—"]
    figures_description:
      - "Forest plot (key figure): bootstrap 95% CIs on item_id across 4 benchmarks, ordered by point
        estimate. 2-cluster visual: high-cluster (MMLU, ARC) separated from low-cluster (GSM8K,
        HellaSwag) but with narrow endpoint overlap. Dashed line at 50%."
      - "D-study projection curves: G coefficient vs item count for each benchmark, with shaded CI
        bands from bootstrap. Horizontal dashed lines at G=0.80, 0.90, 0.95. Shows benchmark-specific
        convergence rates with CIs on the crossing points."
      - "Side-by-side stacked bars: basic (model-pooled) vs model-as-facet decomposition for MMLU,
        showing 21% model×item extracted from residual (11pp) and item_id (4pp). Annotation arrows."
      - "Heatmap: model×item interaction strength for 4 models × 200 MMLU items, biclustered. Shows
        Llama vs Qwen knowledge gap pattern (Llama weak on STEM, Qwen weak on humanities)."
    analysis: >
      Five key takeaways for the paper. (1) Model-as-facet reduces item_id by ~4pp on ALL benchmarks —
      prior single-model studies systematically overestimated pure item dominance. Frame as: "even
      within the 7-9B parameter range, model-specific knowledge gaps account for 16-21% of variance,
      meaning item difficulty estimates from single-model studies are inflated." (2) Gradient direction is
      significant (p=0.003) but magnitude CIs overlap at endpoints — use "10-30pp spread" in claims.
      (3) GSM8K infra×method CI [1.2%, 4.8%] excludes zero — this is a statistically robust departure
      from separability, requiring benchmark qualification on Claim 2. (4) D-study budgets differentiate
      benchmarks but the ratio (1.5-1.75×, not 3×) means the practical implication is real but less
      dramatic than hoped. (5) Logprob scoring amplifies item_id to 55% — a third metric perspective
      that strengthens the metric-conditional narrative.

  - name: "14B model scale extension"
    plan_id: "exp-005"
    description: >
      Qwen3-14B + DeepSeek-R1-Distill-14B at BF16/FP16 × 6 prompts × 6 seeds × 2 temperatures ×
      4 orderings × 200 MMLU items on datacenter GPUs (≥48GB VRAM).
    expected_results:
      qwen3_14b_accuracy_bf16: 0.745
      deepseek_r1_14b_accuracy_bf16: 0.728
      item_id_14b_model_facet: 0.44
      model_x_item_14b: 0.25
      model_main_14b: 0.07
      residual_14b: 0.06
      temp_x_item_14b: 0.06
      prompt_x_item_14b: 0.045
      precision_main_14b: 0.003
      g_correct_14b_binary: 0.40
      deepseek_r1_temp_x_item: 0.085
      qwen3_14b_temp_x_item: 0.042
      cross_gpu_gap_14b_bf16_pp: 0.1
      item_id_8b_vs_14b_diff_pp: 4.0
      model_x_item_8b_vs_14b_diff_pp: 4.0
      variance_hierarchy_qualitatively_preserved: true
    result_rationale: >
      14B models show 44% item_id (vs 48% at 8B) because higher capacity reduces floor effects — items
      that were impossible for 8B models become solvable at 14B, compressing between-item variance. The
      4pp reduction is modest, suggesting item difficulty saturation is far from reached even at 14B.
      Model×item interaction rises to 25% (from 21%) because the dense-vs-reasoning-distilled
      architecture difference creates larger model-specific item profiles: DeepSeek-R1-Distill-14B
      excels on multi-step reasoning items (distilled from R1's reasoning traces) while Qwen3-14B excels
      on factual knowledge items (larger pre-training corpus). This architecture-driven specialization
      is larger than the Llama-vs-Qwen difference at 8B. DeepSeek shows elevated temperature×item (8.5%
      vs Qwen's 4.2%) because reasoning-distilled models produce chain-of-thought that branches more at
      sampling time — consistent with exp-002's finding that reasoning tasks show higher temperature
      sensitivity. Model main effect at 7% (vs 5% at 8B) reflects the larger accuracy spread between
      dense and reasoning-distilled architectures. Precision effect remains negligible (0.3pp) —
      precision sensitivity does not increase with scale in this range. G-coefficient of 0.40 is slightly
      higher than 8B (0.37) because reduced item variance improves relative reliability.
    tables:
      - name: "Table 17: 8B vs 14B Variance Decomposition (MMLU, Model-as-Facet)"
        columns: ["Source", "8B (4 models)", "14B (2 models)", "Δ"]
        rows:
          - ["item_id", "48.0%", "44.0%", "-4.0pp"]
          - ["model×item", "21.0%", "25.0%", "+4.0pp"]
          - ["model (main)", "5.0%", "7.0%", "+2.0pp"]
          - ["residual", "8.0%", "6.0%", "-2.0pp"]
          - ["temp:item", "4.8%", "6.0%", "+1.2pp"]
          - ["prompt:item", "5.3%", "4.5%", "-0.8pp"]
          - ["precision (main)", "2.5%", "0.3%", "-2.2pp"]
          - ["other", "5.4%", "7.2%", "—"]
      - name: "Table 18: Per-Architecture Temperature Sensitivity (14B)"
        columns: ["Model", "Type", "temp:item", "temp=0.0 Acc", "temp=1.0 Acc", "Spread"]
        rows:
          - ["Qwen3-14B", "Dense", "4.2%", "0.752", "0.738", "1.4pp"]
          - ["DeepSeek-R1-14B", "Reasoning-distilled", "8.5%", "0.740", "0.715", "2.5pp"]
    figures_description:
      - "Paired stacked bars: 8B vs 14B decomposition showing item_id compression and model×item
        expansion. Annotation highlighting the 'scale compresses item dominance' pattern."
    analysis: >
      Scale extension confirms qualitative stability: item_id > model×item > residual hierarchy
      holds at 14B. The 4pp item_id reduction per scale doubling (8B→14B) suggests that at current
      model sizes, item difficulty remains the dominant variance source — much larger models (70B+)
      would be needed to substantively alter the hierarchy. The dense-vs-reasoning architecture
      finding is a useful Discussion point: model×item increases not from more models but from
      more architecturally diverse models. For the paper: "variance structure is qualitatively stable
      across 7-14B but item dominance magnitude is scale- and architecture-dependent." Frame as scope
      validation, not a primary finding. The precision reduction from 2.5% to 0.3% at 14B (both at
      BF16/FP16 only, no FP32) is because the FP32 degradation source is absent from this experiment.

  - name: "Fine-tuning G-study (RoBERTa)"
    plan_id: "exp-006"
    description: >
      RoBERTa-large fine-tuning on SST-2/MNLI/RTE/COPA. 6 seeds × 3 LRs × 4 data shuffles ×
      3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 total runs.
    expected_results:
      # SST-2 (large dataset, saturated task)
      sst2_accuracy_mean: 0.942
      sst2_accuracy_sd: 0.005
      sst2_lr_variance: 0.35
      sst2_seed_variance: 0.25
      sst2_data_shuffle_variance: 0.12
      sst2_seed_x_lr_variance: 0.10
      sst2_gpu_variance: 0.003
      sst2_precision_variance: 0.008
      sst2_residual: 0.159
      # MNLI (large dataset, harder task)
      mnli_accuracy_mean: 0.875
      mnli_accuracy_sd: 0.008
      mnli_lr_variance: 0.30
      mnli_seed_variance: 0.22
      mnli_data_shuffle_variance: 0.15
      mnli_seed_x_lr_variance: 0.12
      mnli_gpu_variance: 0.004
      mnli_precision_variance: 0.009
      mnli_residual: 0.177
      # RTE (small dataset, high variance)
      rte_accuracy_mean: 0.716
      rte_accuracy_sd: 0.032
      rte_lr_variance: 0.20
      rte_seed_variance: 0.16
      rte_data_shuffle_variance: 0.28
      rte_seed_x_lr_variance: 0.16
      rte_gpu_variance: 0.005
      rte_precision_variance: 0.010
      rte_residual: 0.175
      # COPA (small dataset, binary choice)
      copa_accuracy_mean: 0.672
      copa_accuracy_sd: 0.038
      copa_lr_variance: 0.18
      copa_seed_variance: 0.20
      copa_data_shuffle_variance: 0.30
      copa_seed_x_lr_variance: 0.14
      copa_gpu_variance: 0.004
      copa_precision_variance: 0.012
      copa_residual: 0.134
      # Cross-task patterns
      dominant_source_large_data: "learning_rate"
      dominant_source_small_data: "data_shuffle"
      gpu_all_tasks_max: 0.005
      precision_all_tasks_max: 0.012
      hierarchy_differs_from_inference: true
      rte_bimodal_seed_lr: true
    result_rationale: >
      Fine-tuning variance structure is qualitatively different from inference: hyperparameters (LR,
      seed, data shuffle) dominate instead of items. On large datasets (SST-2, MNLI), learning rate
      dominates (30-35%) because the optimization landscape is well-defined and LR determines the
      convergence basin — too high overshoots, too low underfits, and the sensitivity is amplified by
      RoBERTa's sharp loss surface near the optimum (Dodge et al., 2020). On small datasets (RTE, COPA),
      data shuffle dominates (28-30%) because mini-batch composition has outsized influence with fewer
      training examples — a single misplaced hard example in early batches can steer the model into a
      different loss basin. Seed is substantial everywhere (16-25%) because weight initialization and
      dropout mask jointly determine the optimization trajectory. The seed×LR interaction (10-16%) is
      the fine-tuning analog of item×temperature in inference: certain seed-LR combinations land in
      qualitatively different loss basins, producing bimodal accuracy distributions on RTE (two clusters
      separated by ~4pp accuracy, one basin near 72% and one near 68%). GPU and precision effects remain
      negligible (<1.2%) across all tasks — the variance hierarchy for infrastructure factors is
      consistent between fine-tuning and inference, even though the methodology-factor hierarchy differs
      completely. This validates the G-theory framework's generality while showing that reproducibility
      budgets cannot be transferred between evaluation modes.
    tables:
      - name: "Table 19: Fine-Tuning Variance Decomposition Across Tasks"
        columns: ["Source", "SST-2", "MNLI", "RTE", "COPA"]
        rows:
          - ["learning_rate", "35.0%", "30.0%", "20.0%", "18.0%"]
          - ["seed", "25.0%", "22.0%", "16.0%", "20.0%"]
          - ["data_shuffle", "12.0%", "15.0%", "28.0%", "30.0%"]
          - ["seed×lr", "10.0%", "12.0%", "16.0%", "14.0%"]
          - ["gpu", "0.3%", "0.4%", "0.5%", "0.4%"]
          - ["precision", "0.8%", "0.9%", "1.0%", "1.2%"]
          - ["residual", "16.9%", "19.7%", "18.5%", "16.4%"]
      - name: "Table 20: Inference vs Fine-Tuning Variance Hierarchy"
        columns: ["Rank", "Inference (MMLU)", "FT — Large (SST-2)", "FT — Small (RTE)"]
        rows:
          - ["#1", "item_id (48%)", "learning_rate (35%)", "data_shuffle (28%)"]
          - ["#2", "model×item (21%)", "seed (25%)", "learning_rate (20%)"]
          - ["#3", "residual (8%)", "residual (17%)", "seed×lr (16%)"]
          - ["#4", "prompt:item (5%)", "data_shuffle (12%)", "seed (16%)"]
          - ["Infra", "precision 2.5%", "gpu+prec 1.1%", "gpu+prec 1.5%"]
    figures_description:
      - "Side-by-side stacked bars: inference (MMLU) vs fine-tuning (4 tasks), highlighting the
        qualitative hierarchy shift from item-dominated to hyperparameter-dominated."
      - "Scatter: per-run accuracy vs learning rate for RTE, colored by seed, showing bimodal clustering
        at seed×LR interaction. Two loss basins annotated."
    analysis: >
      Fine-tuning results support the paper's broader thesis at a meta-level: variance structure is
      task-conditional, and this extends beyond benchmarks to evaluation MODES. The LR-dominated
      (large data) vs shuffle-dominated (small data) pattern in fine-tuning parallels the
      knowledge-item-dominated vs reasoning-interaction-dominated pattern in inference — in both cases,
      the dominant source shifts as the task's "difficulty structure" changes. Infrastructure effects
      remain negligible in both settings, providing cross-mode evidence for separability (with the
      caveat that fine-tuning doesn't test the temperature/seed × precision interactions that drive
      GSM8K's infra×method departure). For the paper: position as Discussion material showing G-theory
      generality. Explicit caveat: encoder-only fine-tuning (RoBERTa) may not generalize to decoder
      fine-tuning where generation-related variance sources (temperature, seed) would re-enter.

  - name: "LayerCast precision mitigation"
    plan_id: "exp-007"
    description: >
      LayerCast (FP16 storage + FP32 compute) as additional precision condition on MMLU.
      Same 4 models × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 items.
    expected_results:
      layercast_accuracy_mean: 0.682
      layercast_vs_bf16_gap_pp: 0.2
      layercast_vs_fp16_gap_pp: 0.1
      layercast_vs_fp32_gap_pp: 2.7
      layercast_item_id_binary: 0.515
      layercast_prec_x_item_reduction_vs_fp16_pct: 40
      layercast_g_correct_binary: 0.37
      layercast_inference_overhead_pct: 18
      layercast_prec_x_temp_binary: 0.001
      layercast_prec_x_temp_textmatch: 0.008
    result_rationale: >
      LayerCast reduces precision:item interaction by ~40% vs FP16 because the FP32 compute path
      eliminates mid-layer accumulation errors that flip items near decision boundaries. However, the
      practical benefit is marginal: FP16 precision:item was already only 5% of total variance, so a
      40% reduction brings it to ~3% — still dwarfed by item_id at 51.5%. Accuracy (0.682) falls between
      BF16 (0.684) and FP16 (0.681), essentially equivalent to both. The precision×temperature
      interaction drops to 0.1% binary (from FP16's ~0.2%) because FP32 compute stabilizes the logit
      computation at each sampling step. The 18% inference overhead comes from FP16→FP32 upcasting at
      each transformer layer. G-coefficient is unchanged (0.37) because the dominant item_id component
      is unaffected by precision mitigation. Given that BF16 already shows negligible precision effects
      and has no inference overhead, LayerCast is only relevant for the specific case where FP16 memory
      savings are required AND cross-hardware reproducibility matters.
    tables:
      - name: "Table 21: LayerCast Comparison Across Precision Modes"
        columns: ["Metric", "FP32", "BF16", "FP16", "LayerCast"]
        rows:
          - ["Accuracy", "0.655", "0.684", "0.681", "0.682"]
          - ["item_id %", "50.5%", "52.0%", "51.8%", "51.5%"]
          - ["prec:item %", "5.8%", "4.5%", "5.0%", "3.0%"]
          - ["prec×temp (binary)", "0.3%", "0.1%", "0.2%", "0.1%"]
          - ["prec×temp (text)", "2.5%", "1.8%", "2.2%", "0.8%"]
          - ["G (binary)", "0.36", "0.37", "0.37", "0.37"]
          - ["Inference cost (rel.)", "1.35×", "1.00×", "1.00×", "1.18×"]
    figures_description:
      - "Bar chart: precision:item interaction by precision mode, showing LayerCast intermediate between
        BF16 and FP16 but closer to BF16."
    analysis: >
      LayerCast is a footnote finding. Precision effects are already small post-confound analysis
      (precision main 2.5-3% of total, infra×method <0.5% on knowledge benchmarks). Mitigating them
      further with LayerCast provides diminishing returns at 18% inference cost. Include as 1-2
      paragraphs in Discussion or as appendix material. Practical recommendation: use BF16 — it has
      no overhead and minimal precision artifacts. LayerCast is only worth mentioning to preempt
      reviewer questions about mitigation strategies.

  - name: "MATH benchmark extension"
    plan_id: "exp-008"
    description: >
      MATH (200 items) with 4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds ×
      2 temperatures × 4 orderings. Tests chain-of-thought reasoning variance.
    expected_results:
      math_accuracy_mean: 0.38
      math_accuracy_sd_across_conditions: 0.045
      # Basic analysis (model pooled)
      math_item_id_basic: 0.32
      math_residual_basic: 0.17
      math_temp_x_item_basic: 0.14
      math_seed_x_item_basic: 0.11
      math_prompt_x_item_basic: 0.08
      math_temperature_main_basic: 0.06
      math_precision_main_basic: 0.005
      math_infra_x_method_binary: 0.025
      math_other_basic: 0.09
      # Model-as-facet (via exp-004 reanalysis)
      math_item_id_model_facet: 0.28
      math_model_x_item: 0.22
      math_model_main: 0.06
      math_residual_model_facet: 0.07
      math_g_correct_binary: 0.52
      # Updated 5-benchmark gradient
      five_benchmark_item_id_range: [0.28, 0.48]
      five_benchmark_spread_pp: 20
      five_benchmark_pattern: "{MMLU 48%, ARC 46%} > {GSM8K 36%, HellaSwag 31%} ≥ {MATH 28%}"
      three_tier_structure: true
      math_infra_x_method_textmatch: 0.042
    result_rationale: >
      MATH shows the lowest item dominance (28% model-as-facet) because multi-step mathematical proofs
      introduce maximal chain-of-thought variance. Unlike GSM8K's mostly arithmetic word problems, MATH
      items require proof strategies (induction, construction, algebraic manipulation) with multiple valid
      approaches — temperature and seed determine which strategy the model attempts, making temp:item
      (14%) and seed:item (11%) jointly exceed item_id. The 38% overall accuracy (8B models on MATH)
      creates strong floor effects: ~40% of items are never solved regardless of conditions (zero
      variance), ~20% are always solved (zero variance), and the remaining ~40% of "mid-difficulty" items
      carry nearly all the variance — and on these items, condition sensitivity is extreme. G-coefficient
      at 0.52 (highest of all benchmarks) is counterintuitive but correct: the items that 8B models CAN
      solve are consistently solved (low relative error), so the universe score is reliable despite high
      absolute variance. Model×item at 22% is the highest across benchmarks because dense vs
      reasoning-distilled architectures diverge most on proof items: DeepSeek-R1-Distill can solve
      certain proof items that no other 8B model touches, creating large model-specific item effects.
      Adding MATH extends the 2-cluster gradient to a potential 3-tier structure with 20pp total spread
      (48-28%), strengthening the cognitive-complexity narrative. Infra×method at 2.5% binary confirms
      the GSM8K pattern: math-heavy generation shows detectable precision×methodology interaction. Under
      text-match, MATH prec×temp reaches 4.2% (the highest single infra×method interaction) because
      proof-format outputs are extremely sensitive to token-level differences.
    tables:
      - name: "Table 22: MATH Variance Decomposition (Binary, Model-as-Facet)"
        columns: ["Source", "MATH", "GSM8K (ref)", "MMLU (ref)"]
        rows:
          - ["item_id", "28.0%", "36.0%", "48.0%"]
          - ["model×item", "22.0%", "18.0%", "21.0%"]
          - ["temp:item", "14.0%", "9.0%", "4.8%"]
          - ["seed:item", "11.0%", "5.5%", "2.0%"]
          - ["prompt:item", "6.5%", "5.5%", "5.3%"]
          - ["model (main)", "6.0%", "4.0%", "5.0%"]
          - ["residual", "7.0%", "10.0%", "8.0%"]
          - ["temperature", "4.5%", "3.5%", "1.2%"]
          - ["infra×method", "2.5%", "3.0%", "0.4%"]
          - ["other", "-1.5%", "5.5%", "4.3%"]
        note: "Negative 'other' due to rounding and minor negative Henderson estimates on near-zero terms."
      - name: "Table 23: Updated 5-Benchmark Summary (Model-as-Facet)"
        columns: ["Benchmark", "Type", "item_id", "G (binary)", "infra×method", "Tier"]
        rows:
          - ["MMLU", "Knowledge", "48.0%", "0.37", "0.4%", "High"]
          - ["ARC", "Knowledge", "46.0%", "0.35", "0.5%", "High"]
          - ["GSM8K", "Arithmetic reasoning", "36.0%", "0.42", "3.0%", "Mid"]
          - ["HellaSwag", "Commonsense", "31.0%", "0.48", "0.3%", "Mid"]
          - ["MATH", "Proof reasoning", "28.0%", "0.52", "2.5%", "Low"]
    figures_description:
      - "Updated stacked bar (5 benchmarks): variance decomposition showing the 3-tier gradient.
        Item_id bars decrease monotonically from left (MMLU) to right (MATH); interaction bars grow."
      - "Line plot: item_id % vs cognitive complexity ordinal (knowledge → arithmetic → commonsense →
        proof), with bootstrap CI bands. Stepped pattern visible despite within-tier noise."
    analysis: >
      MATH is the median tier's upgrade path. With 5 benchmarks and 20pp spread, the narrative
      strengthens from "2-cluster" to "task-complexity gradient with 3 tiers": knowledge benchmarks
      (MMLU, ARC) → arithmetic/commonsense reasoning (GSM8K, HellaSwag) → proof reasoning (MATH).
      HellaSwag's position (31%, in "mid" tier despite being commonsense rather than math) adds nuance
      — the gradient tracks multi-step reasoning demand more than domain. MATH also reinforces the
      GSM8K infra×method finding: both math-heavy benchmarks show 2.5-3% infra×method binary, while
      knowledge and commonsense benchmarks show <0.5%. This transforms the separability exception from
      "one benchmark" to "math-generation benchmarks" — a more principled category that strengthens the
      paper. If AAAI timeline permits exp-008 (50 GPU hours, dependent on exp-002), include it and
      claim the 3-tier gradient. If not, the 4-benchmark 2-cluster story is publishable with softened
      framing, and MATH can be added for camera-ready or the ACL submission.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23bb16bc-8444-433e-8339-e59084ddebb0",
  "isSidechain": false,
  "requestId": "req_011CbEdQBG1rK7Tjzmhe68Y8",
  "type": "assistant",
  "uuid": "ba5ece7d-e070-4f9b-a2d3-92bac7d75176",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pm13He2zchUaGL4kZg4VJV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12069,
      "cache_read_input_tokens": 11841,
      "output_tokens": 51219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 51219,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12069
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Gradient exists but is noisy or only 2-cluster (knowledge vs reasoning); some claims need softening; paper is publishable with adjusted framing 核心假设：['It…",
  "leafUuid": "ba5ece7d-e070-4f9b-a2d3-92bac7d75176",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define median-tier experiment predictions for nlp_variance_gtheory",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Gradient exists but is noisy or only 2-cluster (knowledge vs reasoning); some claims need softening; paper is publishable with adjusted framing 核心假设：['It…",
  "leafUuid": "ba5ece7d-e070-4f9b-a2d3-92bac7d75176",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Define median-tier experiment predictions for nlp_variance_gtheory",
  "sessionId": "b4125e70-e297-410c-afc9-d3cc6ac9f2e3"
}
```

---
