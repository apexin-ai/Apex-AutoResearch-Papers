# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Cross-benchmark gradient clear and monotonic; all three claims hold as frame

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/23357e26-9b8d-4d36-9720-249b9bfdef30.jsonl`
- **Structured JSON:** [`3aae9f14bcfd5c76f267.json`](../../sessions/3a/3aae9f14bcfd5c76f267.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T22:22:44.310Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T22:22:44.310Z",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Cross-benchmark gradient clear and monotonic; all three claims hold as framed; AAAI submission proceeds without claim weakening\n核心假设：['Item dominance on MMLU replicates at 50-60% (binary) across 3 independent 200-item samples (exp-001b CV<15%)', 'Cross-benchmark gradient is monotonic: MMLU > ARC-Challenge > HellaSwag > GSM8K in item_id variance share', 'GSM8K/MATH item dominance drops to 20-30%, with seed×item and temperature×item rising to 15-25%', 'Infrastructure×methodology interaction remains <1% (binary) across all benchmarks in exp-002/003', 'Multi-hardware crossing (exp-003) confirms single-GPU separability: hardware×methodology <1%', 'Model-as-facet (exp-004) reveals model×item 5-15%, reduces residual, but item_id remains largest single component on knowledge benchmarks', \"Bootstrap CIs (1000 resamples) on item_id share exclude zero and don't overlap across benchmark clusters\", 'D-study projections show clearly differentiated optimal allocations: MMLU needs 400+ items, GSM8K needs 10+ seeds']\n关键指标范围：{'item_id_variance_mmlu_binary': [0.48, 0.62], 'item_id_variance_gsm8k_binary': [0.18, 0.3], 'item_id_variance_arc_binary': [0.35, 0.48], 'item_id_variance_hellaswag_binary': [0.28, 0.4], 'cross_benchmark_gradient_spread_pp': [25, 40], 'infra_x_method_binary_all_benchmarks': [0.0, 0.008], 'infra_x_method_textmatch_max': [0.005, 0.02], 'hardware_x_methodology_exp003': [0.0, 0.01], 'model_x_item_mmlu': [0.05, 0.15], 'g_correct_mmlu': [0.3, 0.4], 'g_correct_gsm8k': [0.45, 0.65], 'bootstrap_ci_width_item_id': [0.03, 0.08], 'item_resample_cv_exp001b': [0.03, 0.12], 'dstudy_items_for_g90_mmlu': [350, 500], 'dstudy_items_for_g90_gsm8k': [100, 200]}\n叙事方向：Original framing holds intact. Title: \"Reproducibility Budgets\" with cross-benchmark gradient as headline. Lead with the gradient figure (stacked bars clearly shifting across benchmarks). Separability is a clean confirmatory result. D-study budgets are benchmark-specific and actionable. Intro hook: \"universal reproducibility recipe is illusory\" is fully supported by data. All 3 claims survive without qualification. Paper lands as empirical contribution + practical tool, with psychometric framing validated by benchmark-conditional quantification. AAAI \"evaluation methodology\" track is a natural fit; no need for backup venue.\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: nlp_variance_gtheory\nfocus: Re-dream after major framing revision addressing all 9 structural issues from first dream. Key changes: (1) infrastructure crossing reframed as confirmatory null, not primary novelty; (2) cross-benchmark variance gradient is now the primary finding; (3) item dominance acknowledged as psychometrically expected, contribution is quantification+gradient; (4) model treated as crossed facet in analysis; (5) bibliography expanded to 25+ refs; (6) 4 figures planned; (7) \"fully crossed\" qualified; (8) \"diagnostic tool\" either substantiated with code release or reframed. Verify whether these framing changes address the weak reject scores from first dream.\n\n## paper_framing.md\n\n# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Item Dominance (benchmark-conditional)**: Item selection is the single largest variance source in multiple-choice LLM evaluation, but its magnitude is benchmark-dependent: from ~45% on knowledge-retrieval tasks (MMLU) down to ~25% on reasoning tasks (GSM8K/MATH) where temperature and seed interactions increase. Item dominance is expected from measurement theory when item difficulty varies widely (Brennan, 2001); our contribution is in (a) quantifying the precise magnitude across benchmarks and models, (b) demonstrating the systematic benchmark-dependent gradient, and (c) deriving D-study implications specific to LLM evaluation.\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent: binary correct scoring yields G=0.357 (item dominance makes G≥0.90 unreachable without massive item expansion), while text-exact-match scoring yields G=0.975 (already adequate). D-study projections show that increasing item sampling is more cost-effective than increasing prompt/seed replication, but the optimal allocation depends critically on both the evaluation metric and the benchmark. Current common practices (1 prompt, 1 seed, ≤200 items, single metric) produce misleading reliability estimates.\n\n## Contributions (3 条，明确区分)\n\n1. **Cross-benchmark variance gradient**: The first multi-benchmark G-theory analysis showing that variance structure systematically shifts from item-dominated (knowledge retrieval) to interaction-dominated (reasoning tasks), explaining why prior single-benchmark studies reached seemingly contradictory conclusions.\n\n2. **Confirmatory separability test**: Infrastructure×methodology interactions are negligible at the aggregate level (<0.5% under binary scoring), providing empirical support for isolated-factor studies — with the caveat that both factors interact with items and the finding is metric-conditional.\n\n3. **Task-specific reproducibility budgets**: D-study projections with bootstrap CIs yield actionable, benchmark-specific item/prompt/seed allocations for achieving target reliability (G≥0.90), contextualized against IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite).\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of K conditions across M models and N benchmarks, item selection is the largest single variance source on multiple-choice benchmarks (25-55%, benchmark-dependent), while direct infrastructure×methodology interactions are negligible (<0.5% binary, ≤1.3% text-match). Variance structure shifts systematically from item-dominated (knowledge benchmarks) to interaction-dominated (reasoning benchmarks). D-study reproducibility budgets show that optimal facet allocation is both benchmark-specific and metric-conditional: MMLU needs more items, GSM8K needs more seeds.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (4 figures minimum):\n  1. Problem illustration: same model, different benchmark → different dominant variance source\n  2. G-theory facet diagram showing crossed design\n  3. Stacked-bar variance decomposition across benchmarks (signature figure)\n  4. D-study projection curves: G vs item count for different benchmarks\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (25-55%), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Full-scale precision study: 4 models (Qwen3-8B-Instruct, Llama-3.1-8B-Instruct,\n    Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3) × 3 precisions (FP32, BF16, FP16) × 6\n    prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified).\n    All precisions use consistent vLLM engine (V0 enforce_eager) to eliminate the\n    float32 engine confound found in MVP. Validates item dominance finding at scale\n    and with multiple models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 100\n  hardware: westd-32570 (RTX PRO 6000 96GB)\n  deps: []\n  status: planned\n- id: exp-001b\n  claim: 1\n  description: 'Item resampling stability test: 3 independent stratified samples of\n    200 MMLU items (seeds 0, 7, 99) × 1 model (Llama-3.1-8B-Instruct) × 3 precisions\n    × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether\n    the 58% item dominance finding is stable across different item draws from MMLU,\n    not an artifact of the specific 200-item sample. Critical for defending the headline\n    claim.\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Multi-benchmark replication: same 4 models × BF16/FP16 × 6 prompts\n    × 6 seeds × 2 temperatures × 4 orderings on GSM8K (200 items), ARC-Challenge (200\n    items), HellaSwag (200 items). Tests whether item dominance and separability hold\n    across task types (math reasoning, science reasoning, commonsense).\n\n    '\n  priority: P0\n  gpu_budget_hours: 200\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-003\n  claim: 2\n  description: 'Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16,\n    FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. Tests\n    hardware × methodology interaction — the core separability question that MVP couldn''t\n    address with only 1 GPU type.\n\n    '\n  priority: P0\n  gpu_budget_hours: 120\n  hardware: westd-32570 + TBD (second GPU type from Manager)\n  deps: []\n  status: planned\n- id: exp-004\n  claim: 3\n  description: 'Comprehensive analysis of combined exp-001/001b/002/003 data. Includes:\n    (a) Model-as-facet G-theory reanalysis — treat model as crossed random facet to\n    properly attribute model×item interaction and reduce inflated item_id/residual\n    (Dream critical); (b) Bootstrap CIs (1000 resamples) on ALL variance components\n    in ALL tables, especially direct infra×method interaction term (Dream critical);\n    (c) D-study projections with CIs for optimal allocation across facets for G≥0.90/0.95/0.99,\n    with benchmark-specific budgets and comparison to IRT-based subsampling (tinyBenchmarks);\n    (d) REML vs Henderson Method I comparison as sensitivity analysis; (e) Logprob-based\n    scoring as third response variable; (f) Ranking stability analysis — does precision×temperature\n    interaction alter model rankings? (g) Higher-order interaction estimation to decompose\n    the residual component.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  hardware: none\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  status: planned\n- id: exp-005\n  claim: 2\n  description: '14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter\n    GPUs at BF16/FP16. Tests whether variance attribution patterns change with model\n    scale and architecture (dense vs reasoning-distilled).\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  hardware: TBD (needs ≥48GB VRAM per GPU)\n  deps:\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA. Fully crossed:\n    6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task\n    × 4 tasks = 1,728 total fine-tuning runs. Validates whether variance hierarchy\n    differs between inference and fine-tuning.\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  hardware: westd-32570 (RoBERTa-large fits easily on 96GB)\n  deps: []\n  status: planned\n- id: exp-007\n  claim: 2\n  description: 'Test LayerCast (FP16 storage + FP32 compute) as additional precision\n    condition on MMLU. Quantifies variance reduction from this mitigation strategy.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 1\n  description: 'MATH benchmark (200 items) — tests whether item dominance pattern\n    differs for reasoning-heavy tasks where chain-of-thought introduces additional\n    variance.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  hardware: westd-32570\n  deps:\n  - exp-002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase_a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 5400\n    conditions: 108\n    overall_accuracy: 0.6557\n    accuracy_bfloat16: 0.6844\n    accuracy_float16: 0.6833\n    accuracy_float32: 0.5994\n    g_coefficient_correct: 0.357\n    top_variance_correct:\n      item_id: 0.5844\n      residual: 0.1759\n      precision:item_id: 0.0724\n      temperature:item_id: 0.0685\n      prompt_template:item_id: 0.0573\n    top_variance_text_match:\n      residual: 0.407\n      prompt_template:item_id: 0.375\n      temperature: 0.169\n      temperature:item_id: 0.025\n      precision:temperature: 0.013\n    pass_criteria_a_pipeline: true\n    pass_criteria_b_components: true\n    pass_criteria_c_interaction: true\n    pass_criteria_c_detail: precision:temperature 1.3% CI not containing zero (text_exact_match)\n- exp_id: bf16_eager_disentangle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bf16_v1_accuracy: 0.6844\n    bf16_eager_accuracy: 0.6822\n    fp32_v0_accuracy: 0.5994\n    engine_effect_pct: 2.6\n    precision_effect_pct: 97.4\n    engine_gap_pp: 0.22\n    precision_gap_pp: 8.28\n    total_gap_pp: 8.5\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T22:22:44.313Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T22:22:44.313Z",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-20T22:22:44.343Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Cross-benchmark gradient clear and monotonic; all three claims hold as framed; AAAI submission proceeds without claim weakening
核心假设：['Item dominance on MMLU replicates at 50-60% (binary) across 3 independent 200-item samples (exp-001b CV<15%)', 'Cross-benchmark gradient is monotonic: MMLU > ARC-Challenge > HellaSwag > GSM8K in item_id variance share', 'GSM8K/MATH item dominance drops to 20-30%, with seed×item and temperature×item rising to 15-25%', 'Infrastructure×methodology interaction remains <1% (binary) across all benchmarks in exp-002/003', 'Multi-hardware crossing (exp-003) confirms single-GPU separability: hardware×methodology <1%', 'Model-as-facet (exp-004) reveals model×item 5-15%, reduces residual, but item_id remains largest single component on knowledge benchmarks', "Bootstrap CIs (1000 resamples) on item_id share exclude zero and don't overlap across benchmark clusters", 'D-study projections show clearly differentiated optimal allocations: MMLU needs 400+ items, GSM8K needs 10+ seeds']
关键指标范围：{'item_id_variance_mmlu_binary': [0.48, 0.62], 'item_id_variance_gsm8k_binary': [0.18, 0.3], 'item_id_variance_arc_binary': [0.35, 0.48], 'item_id_variance_hellaswag_binary': [0.28, 0.4], 'cross_benchmark_gradient_spread_pp': [25, 40], 'infra_x_method_binary_all_benchmarks': [0.0, 0.008], 'infra_x_method_textmatch_max': [0.005, 0.02], 'hardware_x_methodology_exp003': [0.0, 0.01], 'model_x_item_mmlu': [0.05, 0.15], 'g_correct_mmlu': [0.3, 0.4], 'g_correct_gsm8k': [0.45, 0.65], 'bootstrap_ci_width_item_id': [0.03, 0.08], 'item_resample_cv_exp001b': [0.03, 0.12], 'dstudy_items_for_g90_mmlu': [350, 500], 'dstudy_items_for_g90_gsm8k': [100, 200]}
叙事方向：Original framing holds intact. Title: "Reproducibility Budgets" with cross-benchmark gradient as headline. Lead with the gradient figure (stacked bars clearly shifting across benchmarks). Separability is a clean confirmatory result. D-study budgets are benchmark-specific and actionable. Intro hook: "universal reproducibility recipe is illusory" is fully supported by data. All 3 claims survive without qualification. Paper lands as empirical contribution + practical tool, with psychometric framing validated by benchmark-conditional quantification. AAAI "evaluation methodology" track is a natural fit; no need for backup venue.


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
tier: best
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
  "promptId": "c295c0c9-7475-4ab1-87e4-a49b6b5cf1ca",
  "type": "user",
  "uuid": "ff0a217c-2c18-4a79-8743-15fcff42e0d1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T22:22:44.342Z_

```json
{
  "parentUuid": "ff0a217c-2c18-4a79-8743-15fcff42e0d1",
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
  "uuid": "397353b9-94fc-410d-ab6c-e890c3945c47",
  "timestamp": "2026-05-20T22:22:44.342Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T22:22:44.342Z_

```json
{
  "parentUuid": "397353b9-94fc-410d-ab6c-e890c3945c47",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5ce1c29f-94c3-4cd3-9bbb-86e890c694b0",
  "timestamp": "2026-05-20T22:22:44.342Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Cross-benchmark gradient clear and monotonic; all three claims hold as framed; AAAI submission proceeds without claim weakening 核心假设：['Item dominance on MM…",
  "leafUuid": "5ce1c29f-94c3-4cd3-9bbb-86e890c694b0",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "G-theory variance decomposition across LLM benchmarks",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30"
}
```

---

### Assistant

_source line 8 · 2026-05-20T22:22:47.556Z_

I'll analyze the experiment plan and generate detailed predictions for the "best" tier. Let me first review the existing data and experiment definitions carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ce1c29f-94c3-4cd3-9bbb-86e890c694b0",
  "isSidechain": false,
  "requestId": "req_011CbEbtBJngvD35hafhPwt4",
  "type": "assistant",
  "uuid": "743fe67f-501e-4f3c-92c8-bcbd6710c061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TBG2HkTN62teRFye3VSC4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11961,
      "cache_read_input_tokens": 11841,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11961,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 227,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11961
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

_source line 9 · 2026-05-20T22:22:51.022Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019WLcmL3Hb4uAZgx3GWBo97`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore project structure",
  "prompt": "Search the directory /home/ubuntu/.agent-ml-research-idea_gen_0519 for any relevant files. Look for:\n1. Any existing YAML/JSON files with experiment results or predictions\n2. Any Python analysis scripts\n3. Any data files or notebooks\n4. The full project structure\n\nUse glob patterns like **/*.yaml, **/*.yml, **/*.py, **/*.json, **/*.ipynb, **/*.md to find everything. Report the full file listing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "743fe67f-501e-4f3c-92c8-bcbd6710c061",
  "isSidechain": false,
  "requestId": "req_011CbEbtBJngvD35hafhPwt4",
  "type": "assistant",
  "uuid": "7e971bd4-1005-41cb-a935-1a9b9c294ce7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019TBG2HkTN62teRFye3VSC4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11961,
      "cache_read_input_tokens": 11841,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11961,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 227,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11961
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

_source line 10 · 2026-05-20T22:24:01.049Z_

<details><summary>↩ Tool result · `toolu_019WLcmL3Hb4uAZgx3GWBo97`</summary>

````text
Perfect! Now I have a comprehensive understanding. Let me create the final report:

## Summary: Project Structure and File Inventory

I've completed a thorough exploration of `/home/ubuntu/.agent-ml-research-idea_gen_0519`. Here's the comprehensive inventory:

### PROJECT OVERVIEW

**Project**: `nlp_variance_gtheory` — An AI research project investigating variance sources in LLM (Large Language Model) evaluation using Generalizability Theory (G-theory).

**Status**: Research phase (MVP completed and validated, full-scale experiments pending approval after re-dream review)

**Target Venues**: AAAI 2027 (9-week timeline), ACL 2027 via ARR (21 weeks backup)

---

### DIRECTORY STRUCTURE

```
/home/ubuntu/.agent-ml-research-idea_gen_0519/
├── projects/
│   ├── nlp_variance_gtheory/          [MAIN PROJECT]
│   │   ├── artifacts/                 [Research outputs]
│   │   │   ├── code/                  [Analysis & inference code]
│   │   │   │   └── src/
│   │   │   │       ├── analysis/      [Variance decomposition, D-study, visualization]
│   │   │   │       ├── data/          [MMLU sampling, prompt templates, few-shot]
│   │   │   │       ├── design/        [Factorial design matrix generation]
│   │   │   │       ├── inference/     [vLLM inference pipeline]
│   │   │   │       └── config/        [Model paths, settings]
│   │   │   ├── dream_reports/         [AI review reports - best/median/worst scenarios]
│   │   │   ├── mvp_phase_a/           [MVP results & analysis]
│   │   │   ├── analysis/              [Dual-metric analysis]
│   │   │   └── manifest.yaml          [Artifact registry]
│   │   ├── logs/                      [Worker execution logs & chat history]
│   │   ├── checkpoints/               [Experiment state snapshots]
│   │   ├── distill_tmp/               [Literature distillation YAML files]
│   │   ├── docs/
│   │   │   └── IDEA_BRIEF.md          [Initial idea proposal + MVP results]
│   │   ├── .claude/                   [Claude sessions & documentation]
│   │   ├── experiment_plan.yaml       [Full experimental design P0-P2 phases]
│   │   ├── ROADMAP.md                 [Research progress dashboard]
│   │   ├── memory.md                  [Critical findings & constraints]
│   │   ├── decisions.yaml             [Decision log D001-D003]
│   │   ├── paper_framing.md           [Paper narrative & positioning]
│   │   ├── registry.yaml              [Experiment registry]
│   │   ├── dream_registry.yaml        [Dream review schedule]
│   │   └── mistakes.yaml              [Documented issues & learnings]
│   ├── __setup__/                     [Shared project setup]
│   └── idea_gen_0519/                 [Related idea generation project]
├── config/                            [Global configuration]
│   ├── projects/
│   ├── secrets/
│   ├── venue_rules/                   [CORL-2026, EMNLP-2026 rules]
│   ├── approvals.yaml
│   ├── backend.yaml
│   ├── mcp_config*.json               [Claude MCP tool configs]
│   └── session_state.json
├── global/
│   └── logs/                          [System logs, worker registry, usage tracking]
├── skills/
│   └── projects/nlp_variance_gtheory/
│       ├── distilled-research.skill.md [10 LLM eval variance papers summary]
│       └── distilled-writing.skill.md  [Writing patterns from 8 papers]
├── state/
│   └── pool_state_last.json           [Last system state snapshot]
├── idea_generator/
│   ├── ideas.yaml                     [Tracked research ideas]
│   ├── ideas.lock
│   └── ideas.yaml.bak
├── workspace.yaml                     [Workspace metadata]
├── AGENTS.md                          [Agent role definitions]
└── .claude/
    ├── CLAUDE.md                      [Global documentation]
    └── sessions/                      [Claude session records]
```

---

### KEY FILES BY CATEGORY

#### 1. **YAML/Configuration Files** (33 files)

**Core experiment & research planning:**
- `/projects/nlp_variance_gtheory/experiment_plan.yaml` — Full experimental design with 8 experiments (exp-001 through exp-008), GPU budgets, dependencies, status
- `/projects/nlp_variance_gtheory/decisions.yaml` — Decision log (D001: MVP PASS, D002: dual-metric adoption, D003: framing adjustments)
- `/projects/nlp_variance_gtheory/dream_registry.yaml` — Dream review scheduling
- `/projects/nlp_variance_gtheory/registry.yaml` — Experiment registry

**Literature & distillation:**
- `/projects/nlp_variance_gtheory/distill_tmp/*.yaml` (10 files) — Distilled paper summaries:
  - `hua2025flaw.yaml`, `mesting2026hidden.yaml`, `brittlebench2026.yaml`, `yuan2025layercast.yaml`, `kunievsky2025intent.yaml`, `thinkingmachines2025batch.yaml`, `messina2026background.yaml`, `generalizit2024.yaml`, `bui2025seeds.yaml`, `sameprompt2026.yaml`

**Dream reports (AI review results):**
- `/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/{best,median,worst}/` (3 directories × 3 files each):
  - `imagined_experiments.yaml`, `review_context.yaml`, `experiment_data.json`
- `/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/meta.yaml` — Dream metadata

**Venue configuration:**
- `config/venue_registry.yaml`, `config/venue_rules/corl-2026.yaml`, `config/venue_rules/emnlp-2026.yaml`

---

#### 2. **JSON Result Files** (30+ files)

**Experiment results & checkpoints:**
- `/projects/nlp_variance_gtheory/checkpoints/` (4 files):
  - `mvp_phase_a_{QUEUED,RUNNING,DONE}*.json` — MVP experiment state tracking

**Worker logs & results:**
- `/projects/nlp_variance_gtheory/logs/workers/*_result.json` (15+ files):
  - Worker execution results for: code_design_update, infra_code_deploy, infra_cpu_deps_and_datagen, infra_env_setup, research_related_work_notes, infra_diagnose_env, infra_install_vllm_and_sanity, exp_mvp_phase_a, code_post_mvp_updates, exp_text_exact_match_analysis, debug_fp32_accuracy_investigation, analysis_text_match_dstudy, exp_bf16_eager_disentangle, and more

**Dream report data:**
- `/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/{best,median,worst}/experiment_data.json` (3 files) — Structured experiment data

**MCP & session configs:**
- `config/mcp_config*.json` (10+ files) — Claude tool configurations for different roles (director, worker, distiller, reviewer, etc.)
- `config/session_state.json`, `config/pool.json`, `config/claude_sessions.json`

---

#### 3. **Markdown Documentation** (25+ files)

**Core research documentation:**
- `/projects/nlp_variance_gtheory/docs/IDEA_BRIEF.md` — **Core proposal**: 75-line research brief with idea ID, core problem, proposed approach, key references, MVP validation results (59.9-68.4% accuracy, item_id=58.4%, G=0.357)
- `/projects/nlp_variance_gtheory/paper_framing.md` — Paper narrative: title, 3 core claims (item dominance, separability, reproducibility budgets), story spine, hooks, venue risks
- `/projects/nlp_variance_gtheory/ROADMAP.md` — **Progress dashboard**: current phase (research, MVP PASS), P0/P1/P2 experiments status, GPU budget tracking, model download status
- `/projects/nlp_variance_gtheory/memory.md` — **Gated model constraints, dual-metric decision rationale, FP32 precision effects**
- `/projects/nlp_variance_gtheory/report.md` — Handover report with running tasks, recent conclusions, trends (1 success, 1 negative result)

**Analysis reports:**
- `/projects/nlp_variance_gtheory/artifacts/mvp_phase_a/report/dual_metric_analysis.md` — Deep analysis of binary_correct vs text_exact_match: item_id dominance (58.4%) vs prompt×item (37.5%), temperature effects, correlation analysis
- `/projects/nlp_variance_gtheory/artifacts/analysis/dual_metric_analysis.md` — Extended dual-metric analysis
- `/projects/nlp_variance_gtheory/artifacts/related_work_notes.md` — Literature review synthesis
- `/projects/nlp_variance_gtheory/artifacts/_project/report/related_work_notes.md`

**Dream review feedback:**
- `/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/{best,median,worst}/paper_framing.md` (3 files) — AI-generated framing suggestions for best/median/worst case scenarios
- `/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/{best,median,worst}/review_report.md` (3 files) — Detailed review critiques

**Infrastructure & environment:**
- `/projects/nlp_variance_gtheory/artifacts/env_setup_report.md` — Environment setup documentation
- `/projects/nlp_variance_gtheory/artifacts/code/README.md` — Code pipeline documentation with setup, quick start, design, analysis sections

**Session documentation:**
- `.claude/CLAUDE.md` — Critical session memory (gated model constraints, worker rules, SSH environment setup, Phase 1-5 setup protocols)
- `.claude/AGENTS.md` — Agent role definitions
- Session-specific: `CLAUDE.md` & `AGENTS.md` in distiller, director, agent, reviewer session directories

---

#### 4. **Python Analysis & Inference Code** (18 files)

**Data preparation:**
- `/artifacts/code/src/data/sample_mmlu.py` — MMLU dataset sampling (stratified by subject)
- `/artifacts/code/src/data/sample_benchmarks.py` — GSM8K, ARC, HellaSwag sampling
- `/artifacts/code/src/data/prompt_templates.py` — 6 Brittlebench-style prompt paraphrases
- `/artifacts/code/src/data/few_shot.py` — Few-shot example ordering (4 orderings)

**Experimental design:**
- `/artifacts/code/src/design/generate_design.py` — Factorial design matrix generation (5,184-10,368 conditions)

**Inference pipeline:**
- `/artifacts/code/src/inference/vllm_runner.py` — vLLM wrapper with seed control at 3 levels (engine, CUDA, sampling)
- `/artifacts/code/src/inference/run_experiment.py` — Experiment orchestration script
- `/artifacts/code/src/inference/sanity_check.py` — Model loading & inference validation

**Analysis:**
- `/artifacts/code/src/analysis/variance_decomposition.py` — G-theory variance component estimation (REML via lme4, Henderson Method I)
- `/artifacts/code/src/analysis/d_study.py` — D-study projections for reproducibility budgets
- `/artifacts/code/src/analysis/visualize.py` — Variance decomposition visualization (stacked bar charts)

**Configuration:**
- `/artifacts/code/src/config/model_paths.py` — Model path mapping for gated models (Llama-3.1, Gemma-2)

**Initialization files:**
- `__init__.py` in all subdirectories

**External analysis:**
- `/artifacts/analysis/dual_metric_analysis.py` — Detailed dual-metric variance analysis script

---

#### 5. **Experiment Logs & Chat Histories** (60+ files)

**Worker execution logs:**
- `/projects/nlp_variance_gtheory/logs/workers/*.log` (25+ files) — Step-by-step execution traces
- `/projects/nlp_variance_gtheory/logs/workers/*.json` (15+ files) — Structured results

**Chat/conversation history:**
- `/projects/nlp_variance_gtheory/logs/chats/*.jsonl` (8+ files) — Worker-to-Claude conversations
- `/projects/nlp_variance_gtheory/logs/chats/*.lock` — File locks for concurrent access

**System-level logs:**
- `global/logs/system.log` — Global system operations
- `global/logs/session_events.jsonl` — Session event timeline
- `global/logs/workers/registry.json` — Worker registry
- `global/logs/usage.jsonl` — API usage tracking
- `global/logs/skill_usage.jsonl` — Skill invocation log
- `global/logs/registry_audit.jsonl` — Audit trail
- `global/logs/manager_api.jsonl` — Manager API calls

---

### CORE RESEARCH FINDINGS

**MVP Phase A Results** (2026-05-20):
- **Accuracy**: 59.9% (FP32) to 68.4% (BF16)
- **Variance decomposition** (binary_correct metric):
  - Item selection: **58.4%** (dominant)
  - Residual: 17.6%
  - Precision × Item: 7.2%
  - Temperature × Item: 6.9%
  - Prompt × Item: 5.7%
  - Seed × Item: 2.7%
  - Direct precision-methodology interaction: <0.02% (separability holds)
  - Generalizability coefficient (G): 0.357
- **Key insight**: Dual-metric analysis reveals item dominance in accuracy (58.4%) but prompt sensitivity in text matching (37.5% prompt×item variance)

**Decision Log** (D001-D003):
- D001: MVP validates G-theory feasibility in LLM evaluation
- D002: Adopt dual-metric (binary_correct + text_exact_match) as core methodology
- D003: Dream review (Best 3/6, Median 4/6, Worst 3/6) → Adjust framing, expand exp-004 analysis with model-as-facet, bootstrap CIs, higher-order interactions

---

### EXPERIMENT ROADMAP

**P0 (Must-run for paper):**
- exp-001: 4 models × 3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings × 200 items (100 GPU-h)
- exp-001b: Item resampling stability test (15 GPU-h)
- exp-002: Multi-benchmark replication (GSM8K, ARC, HellaSwag) (200 GPU-h)
- exp-003: Multi-hardware G-study (blocked pending second GPU type) (120 GPU-h)
- exp-004: Comprehensive analysis (0 GPU-h, pure analysis)

**P1 (Important for strength):**
- exp-005: 14B model scale validation (100 GPU-h)
- exp-006: Fine-tuning G-study with RoBERTa (200 GPU-h)

**P2 (Nice-to-have):**
- exp-007: LayerCast mitigation testing (30 GPU-h)
- exp-008: MATH benchmark reasoning extension (50 GPU-h)

**Total P0 budget**: 435 GPU-hours (target: AAAI 2027 with 9-week timeline)

---

### CRITICAL CONSTRAINTS & DECISIONS

1. **Gated model issue**: Llama-3.1-8B and Gemma-2-9B must be loaded from local paths (ModelScope); direct repo ID fails without HF token
2. **FP32 engine confound**: MVP identified vLLM V0 (enforce_eager) vs V1 (CUDA graph) difference affecting FP32; exp-001 standardizes on V0
3. **vLLM version**: 0.9.2 required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support
4. **Dual-metric design**: binary_correct and text_exact_match measure orthogonal constructs (ρ = −0.21); both required in final paper
5. **Item-conditional effects**: Precision/temperature/prompt effects are item-specific, not universal

---

### DELIVERABLES SUMMARY

- **Code repository**: 18 Python analysis/inference modules with full pipeline (data → design → inference → G-theory analysis → D-study projections)
- **Experimental data**: MVP (5,400 inferences), Dream reports (3 scenarios), checkpoint system
- **Documentation**: 25+ markdown files covering research narrative, paper framing, roadmap, decisions, domain-specific skills
- **Configuration**: MCP configs for 10+ Claude tool roles, experiment tracking, worker orchestration
- **Logs**: 80+ log files tracking execution history, chat records, system operations

---

### FILE TOTALS BY TYPE

| File Type | Count | Key Locations |
|-----------|-------|---------------|
| YAML | 33 | experiment_plan, decisions, registry, dream_reports, distill_tmp, config/ |
| JSON | 30+ | artifacts/dream_reports, checkpoints, logs/workers, config/, state/ |
| Markdown | 25+ | docs/, artifacts/, analysis, paper_framing |
| Python | 18 | artifacts/code/src/{data,design,inference,analysis}, analysis/ |
| Log files | 60+ | logs/{workers,chats}, global/logs/ |
| Lock/backup | 10+ | *.lock, *.bak, .pyc/ |

**Total project size**: ~850 files (excluding .venv and __pycache__)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "7e971bd4-1005-41cb-a935-1a9b9c294ce7",
  "isSidechain": false,
  "promptId": "c295c0c9-7475-4ab1-87e4-a49b6b5cf1ca",
  "type": "user",
  "uuid": "9c1658eb-5bd9-41b7-b2ba-6a98d3798415",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the directory /home/ubuntu/.agent-ml-research-idea_gen_0519 for any relevant files. Look for:\n1. Any existing YAML/JSON files with experiment results or predictions\n2. Any Python analysis scripts\n3. Any data files or notebooks\n4. The full project structure\n\nUse glob patterns like **/*.yaml, **/*.yml, **/*.py, **/*.json, **/*.ipynb, **/*.md to find everything. Report the full file listing.",
    "agentId": "afec698511fc6719d",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have a comprehensive understanding. Let me create the final report:\n\n## Summary: Project Structure and File Inventory\n\nI've completed a thorough exploration of `/home/ubuntu/.agent-ml-research-idea_gen_0519`. Here's the comprehensive inventory:\n\n### PROJECT OVERVIEW\n\n**Project**: `nlp_variance_gtheory` — An AI research project investigating variance sources in LLM (Large Language Model) evaluation using Generalizability Theory (G-theory).\n\n**Status**: Research phase (MVP completed and validated, full-scale experiments pending approval after re-dream review)\n\n**Target Venues**: AAAI 2027 (9-week timeline), ACL 2027 via ARR (21 weeks backup)\n\n---\n\n### DIRECTORY STRUCTURE\n\n```\n/home/ubuntu/.agent-ml-research-idea_gen_0519/\n├── projects/\n│   ├── nlp_variance_gtheory/          [MAIN PROJECT]\n│   │   ├── artifacts/                 [Research outputs]\n│   │   │   ├── code/                  [Analysis & inference code]\n│   │   │   │   └── src/\n│   │   │   │       ├── analysis/      [Variance decomposition, D-study, visualization]\n│   │   │   │       ├── data/          [MMLU sampling, prompt templates, few-shot]\n│   │   │   │       ├── design/        [Factorial design matrix generation]\n│   │   │   │       ├── inference/     [vLLM inference pipeline]\n│   │   │   │       └── config/        [Model paths, settings]\n│   │   │   ├── dream_reports/         [AI review reports - best/median/worst scenarios]\n│   │   │   ├── mvp_phase_a/           [MVP results & analysis]\n│   │   │   ├── analysis/              [Dual-metric analysis]\n│   │   │   └── manifest.yaml          [Artifact registry]\n│   │   ├── logs/                      [Worker execution logs & chat history]\n│   │   ├── checkpoints/               [Experiment state snapshots]\n│   │   ├── distill_tmp/               [Literature distillation YAML files]\n│   │   ├── docs/\n│   │   │   └── IDEA_BRIEF.md          [Initial idea proposal + MVP results]\n│   │   ├── .claude/                   [Claude sessions & documentation]\n│   │   ├── experiment_plan.yaml       [Full experimental design P0-P2 phases]\n│   │   ├── ROADMAP.md                 [Research progress dashboard]\n│   │   ├── memory.md                  [Critical findings & constraints]\n│   │   ├── decisions.yaml             [Decision log D001-D003]\n│   │   ├── paper_framing.md           [Paper narrative & positioning]\n│   │   ├── registry.yaml              [Experiment registry]\n│   │   ├── dream_registry.yaml        [Dream review schedule]\n│   │   └── mistakes.yaml              [Documented issues & learnings]\n│   ├── __setup__/                     [Shared project setup]\n│   └── idea_gen_0519/                 [Related idea generation project]\n├── config/                            [Global configuration]\n│   ├── projects/\n│   ├── secrets/\n│   ├── venue_rules/                   [CORL-2026, EMNLP-2026 rules]\n│   ├── approvals.yaml\n│   ├── backend.yaml\n│   ├── mcp_config*.json               [Claude MCP tool configs]\n│   └── session_state.json\n├── global/\n│   └── logs/                          [System logs, worker registry, usage tracking]\n├── skills/\n│   └── projects/nlp_variance_gtheory/\n│       ├── distilled-research.skill.md [10 LLM eval variance papers summary]\n│       └── distilled-writing.skill.md  [Writing patterns from 8 papers]\n├── state/\n│   └── pool_state_last.json           [Last system state snapshot]\n├── idea_generator/\n│   ├── ideas.yaml                     [Tracked research ideas]\n│   ├── ideas.lock\n│   └── ideas.yaml.bak\n├── workspace.yaml                     [Workspace metadata]\n├── AGENTS.md                          [Agent role definitions]\n└── .claude/\n    ├── CLAUDE.md                      [Global documentation]\n    └── sessions/                      [Claude session records]\n```\n\n---\n\n### KEY FILES BY CATEGORY\n\n#### 1. **YAML/Configuration Files** (33 files)\n\n**Core experiment & research planning:**\n- `/projects/nlp_variance_gtheory/experiment_plan.yaml` — Full experimental design with 8 experiments (exp-001 through exp-008), GPU budgets, dependencies, status\n- `/projects/nlp_variance_gtheory/decisions.yaml` — Decision log (D001: MVP PASS, D002: dual-metric adoption, D003: framing adjustments)\n- `/projects/nlp_variance_gtheory/dream_registry.yaml` — Dream review scheduling\n- `/projects/nlp_variance_gtheory/registry.yaml` — Experiment registry\n\n**Literature & distillation:**\n- `/projects/nlp_variance_gtheory/distill_tmp/*.yaml` (10 files) — Distilled paper summaries:\n  - `hua2025flaw.yaml`, `mesting2026hidden.yaml`, `brittlebench2026.yaml`, `yuan2025layercast.yaml`, `kunievsky2025intent.yaml`, `thinkingmachines2025batch.yaml`, `messina2026background.yaml`, `generalizit2024.yaml`, `bui2025seeds.yaml`, `sameprompt2026.yaml`\n\n**Dream reports (AI review results):**\n- `/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/{best,median,worst}/` (3 directories × 3 files each):\n  - `imagined_experiments.yaml`, `review_context.yaml`, `experiment_data.json`\n- `/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/meta.yaml` — Dream metadata\n\n**Venue configuration:**\n- `config/venue_registry.yaml`, `config/venue_rules/corl-2026.yaml`, `config/venue_rules/emnlp-2026.yaml`\n\n---\n\n#### 2. **JSON Result Files** (30+ files)\n\n**Experiment results & checkpoints:**\n- `/projects/nlp_variance_gtheory/checkpoints/` (4 files):\n  - `mvp_phase_a_{QUEUED,RUNNING,DONE}*.json` — MVP experiment state tracking\n\n**Worker logs & results:**\n- `/projects/nlp_variance_gtheory/logs/workers/*_result.json` (15+ files):\n  - Worker execution results for: code_design_update, infra_code_deploy, infra_cpu_deps_and_datagen, infra_env_setup, research_related_work_notes, infra_diagnose_env, infra_install_vllm_and_sanity, exp_mvp_phase_a, code_post_mvp_updates, exp_text_exact_match_analysis, debug_fp32_accuracy_investigation, analysis_text_match_dstudy, exp_bf16_eager_disentangle, and more\n\n**Dream report data:**\n- `/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/{best,median,worst}/experiment_data.json` (3 files) — Structured experiment data\n\n**MCP & session configs:**\n- `config/mcp_config*.json` (10+ files) — Claude tool configurations for different roles (director, worker, distiller, reviewer, etc.)\n- `config/session_state.json`, `config/pool.json`, `config/claude_sessions.json`\n\n---\n\n#### 3. **Markdown Documentation** (25+ files)\n\n**Core research documentation:**\n- `/projects/nlp_variance_gtheory/docs/IDEA_BRIEF.md` — **Core proposal**: 75-line research brief with idea ID, core problem, proposed approach, key references, MVP validation results (59.9-68.4% accuracy, item_id=58.4%, G=0.357)\n- `/projects/nlp_variance_gtheory/paper_framing.md` — Paper narrative: title, 3 core claims (item dominance, separability, reproducibility budgets), story spine, hooks, venue risks\n- `/projects/nlp_variance_gtheory/ROADMAP.md` — **Progress dashboard**: current phase (research, MVP PASS), P0/P1/P2 experiments status, GPU budget tracking, model download status\n- `/projects/nlp_variance_gtheory/memory.md` — **Gated model constraints, dual-metric decision rationale, FP32 precision effects**\n- `/projects/nlp_variance_gtheory/report.md` — Handover report with running tasks, recent conclusions, trends (1 success, 1 negative result)\n\n**Analysis reports:**\n- `/projects/nlp_variance_gtheory/artifacts/mvp_phase_a/report/dual_metric_analysis.md` — Deep analysis of binary_correct vs text_exact_match: item_id dominance (58.4%) vs prompt×item (37.5%), temperature effects, correlation analysis\n- `/projects/nlp_variance_gtheory/artifacts/analysis/dual_metric_analysis.md` — Extended dual-metric analysis\n- `/projects/nlp_variance_gtheory/artifacts/related_work_notes.md` — Literature review synthesis\n- `/projects/nlp_variance_gtheory/artifacts/_project/report/related_work_notes.md`\n\n**Dream review feedback:**\n- `/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/{best,median,worst}/paper_framing.md` (3 files) — AI-generated framing suggestions for best/median/worst case scenarios\n- `/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/{best,median,worst}/review_report.md` (3 files) — Detailed review critiques\n\n**Infrastructure & environment:**\n- `/projects/nlp_variance_gtheory/artifacts/env_setup_report.md` — Environment setup documentation\n- `/projects/nlp_variance_gtheory/artifacts/code/README.md` — Code pipeline documentation with setup, quick start, design, analysis sections\n\n**Session documentation:**\n- `.claude/CLAUDE.md` — Critical session memory (gated model constraints, worker rules, SSH environment setup, Phase 1-5 setup protocols)\n- `.claude/AGENTS.md` — Agent role definitions\n- Session-specific: `CLAUDE.md` & `AGENTS.md` in distiller, director, agent, reviewer session directories\n\n---\n\n#### 4. **Python Analysis & Inference Code** (18 files)\n\n**Data preparation:**\n- `/artifacts/code/src/data/sample_mmlu.py` — MMLU dataset sampling (stratified by subject)\n- `/artifacts/code/src/data/sample_benchmarks.py` — GSM8K, ARC, HellaSwag sampling\n- `/artifacts/code/src/data/prompt_templates.py` — 6 Brittlebench-style prompt paraphrases\n- `/artifacts/code/src/data/few_shot.py` — Few-shot example ordering (4 orderings)\n\n**Experimental design:**\n- `/artifacts/code/src/design/generate_design.py` — Factorial design matrix generation (5,184-10,368 conditions)\n\n**Inference pipeline:**\n- `/artifacts/code/src/inference/vllm_runner.py` — vLLM wrapper with seed control at 3 levels (engine, CUDA, sampling)\n- `/artifacts/code/src/inference/run_experiment.py` — Experiment orchestration script\n- `/artifacts/code/src/inference/sanity_check.py` — Model loading & inference validation\n\n**Analysis:**\n- `/artifacts/code/src/analysis/variance_decomposition.py` — G-theory variance component estimation (REML via lme4, Henderson Method I)\n- `/artifacts/code/src/analysis/d_study.py` — D-study projections for reproducibility budgets\n- `/artifacts/code/src/analysis/visualize.py` — Variance decomposition visualization (stacked bar charts)\n\n**Configuration:**\n- `/artifacts/code/src/config/model_paths.py` — Model path mapping for gated models (Llama-3.1, Gemma-2)\n\n**Initialization files:**\n- `__init__.py` in all subdirectories\n\n**External analysis:**\n- `/artifacts/analysis/dual_metric_analysis.py` — Detailed dual-metric variance analysis script\n\n---\n\n#### 5. **Experiment Logs & Chat Histories** (60+ files)\n\n**Worker execution logs:**\n- `/projects/nlp_variance_gtheory/logs/workers/*.log` (25+ files) — Step-by-step execution traces\n- `/projects/nlp_variance_gtheory/logs/workers/*.json` (15+ files) — Structured results\n\n**Chat/conversation history:**\n- `/projects/nlp_variance_gtheory/logs/chats/*.jsonl` (8+ files) — Worker-to-Claude conversations\n- `/projects/nlp_variance_gtheory/logs/chats/*.lock` — File locks for concurrent access\n\n**System-level logs:**\n- `global/logs/system.log` — Global system operations\n- `global/logs/session_events.jsonl` — Session event timeline\n- `global/logs/workers/registry.json` — Worker registry\n- `global/logs/usage.jsonl` — API usage tracking\n- `global/logs/skill_usage.jsonl` — Skill invocation log\n- `global/logs/registry_audit.jsonl` — Audit trail\n- `global/logs/manager_api.jsonl` — Manager API calls\n\n---\n\n### CORE RESEARCH FINDINGS\n\n**MVP Phase A Results** (2026-05-20):\n- **Accuracy**: 59.9% (FP32) to 68.4% (BF16)\n- **Variance decomposition** (binary_correct metric):\n  - Item selection: **58.4%** (dominant)\n  - Residual: 17.6%\n  - Precision × Item: 7.2%\n  - Temperature × Item: 6.9%\n  - Prompt × Item: 5.7%\n  - Seed × Item: 2.7%\n  - Direct precision-methodology interaction: <0.02% (separability holds)\n  - Generalizability coefficient (G): 0.357\n- **Key insight**: Dual-metric analysis reveals item dominance in accuracy (58.4%) but prompt sensitivity in text matching (37.5% prompt×item variance)\n\n**Decision Log** (D001-D003):\n- D001: MVP validates G-theory feasibility in LLM evaluation\n- D002: Adopt dual-metric (binary_correct + text_exact_match) as core methodology\n- D003: Dream review (Best 3/6, Median 4/6, Worst 3/6) → Adjust framing, expand exp-004 analysis with model-as-facet, bootstrap CIs, higher-order interactions\n\n---\n\n### EXPERIMENT ROADMAP\n\n**P0 (Must-run for paper):**\n- exp-001: 4 models × 3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings × 200 items (100 GPU-h)\n- exp-001b: Item resampling stability test (15 GPU-h)\n- exp-002: Multi-benchmark replication (GSM8K, ARC, HellaSwag) (200 GPU-h)\n- exp-003: Multi-hardware G-study (blocked pending second GPU type) (120 GPU-h)\n- exp-004: Comprehensive analysis (0 GPU-h, pure analysis)\n\n**P1 (Important for strength):**\n- exp-005: 14B model scale validation (100 GPU-h)\n- exp-006: Fine-tuning G-study with RoBERTa (200 GPU-h)\n\n**P2 (Nice-to-have):**\n- exp-007: LayerCast mitigation testing (30 GPU-h)\n- exp-008: MATH benchmark reasoning extension (50 GPU-h)\n\n**Total P0 budget**: 435 GPU-hours (target: AAAI 2027 with 9-week timeline)\n\n---\n\n### CRITICAL CONSTRAINTS & DECISIONS\n\n1. **Gated model issue**: Llama-3.1-8B and Gemma-2-9B must be loaded from local paths (ModelScope); direct repo ID fails without HF token\n2. **FP32 engine confound**: MVP identified vLLM V0 (enforce_eager) vs V1 (CUDA graph) difference affecting FP32; exp-001 standardizes on V0\n3. **vLLM version**: 0.9.2 required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support\n4. **Dual-metric design**: binary_correct and text_exact_match measure orthogonal constructs (ρ = −0.21); both required in final paper\n5. **Item-conditional effects**: Precision/temperature/prompt effects are item-specific, not universal\n\n---\n\n### DELIVERABLES SUMMARY\n\n- **Code repository**: 18 Python analysis/inference modules with full pipeline (data → design → inference → G-theory analysis → D-study projections)\n- **Experimental data**: MVP (5,400 inferences), Dream reports (3 scenarios), checkpoint system\n- **Documentation**: 25+ markdown files covering research narrative, paper framing, roadmap, decisions, domain-specific skills\n- **Configuration**: MCP configs for 10+ Claude tool roles, experiment tracking, worker orchestration\n- **Logs**: 80+ log files tracking execution history, chat records, system operations\n\n---\n\n### FILE TOTALS BY TYPE\n\n| File Type | Count | Key Locations |\n|-----------|-------|---------------|\n| YAML | 33 | experiment_plan, decisions, registry, dream_reports, distill_tmp, config/ |\n| JSON | 30+ | artifacts/dream_reports, checkpoints, logs/workers, config/, state/ |\n| Markdown | 25+ | docs/, artifacts/, analysis, paper_framing |\n| Python | 18 | artifacts/code/src/{data,design,inference,analysis}, analysis/ |\n| Log files | 60+ | logs/{workers,chats}, global/logs/ |\n| Lock/backup | 10+ | *.lock, *.bak, .pyc/ |\n\n**Total project size**: ~850 files (excluding .venv and __pycache__)"
      }
    ],
    "totalDurationMs": 70022,
    "totalTokens": 62581,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1751,
      "cache_read_input_tokens": 56178,
      "output_tokens": 4645,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1751
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 4645,
          "cache_read_input_tokens": 56178,
          "cache_creation_input_tokens": 1751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1751,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 6,
      "bashCount": 8,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "7e971bd4-1005-41cb-a935-1a9b9c294ce7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Cross-benchmark gradient clear and monotonic; all three claims hold as framed; AAAI submission proceeds without claim weakening 核心假设：['Item dominance on MM…",
  "leafUuid": "9c1658eb-5bd9-41b7-b2ba-6a98d3798415",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "G-theory variance decomposition across LLM benchmarks",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30"
}
```

---

### Assistant

_source line 13 · 2026-05-20T22:24:05.116Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of the project. Let me read the key files I need to generate accurate predictions for the "best" tier:

1. The existing dream reports (especially the best tier) to understand the format
2. The MVP results in detail
3. The experiment plan details

Let me read the existing dream experiment data to understand the expected format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c1658eb-5bd9-41b7-b2ba-6a98d3798415",
  "isSidechain": false,
  "requestId": "req_011CbEbyqCycwvvzbxgP33t8",
  "type": "assistant",
  "uuid": "56aab84f-7555-48a0-9c57-4c2dc2d17fb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EiQFaxDbscb7ExyuU7rbVD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4881,
      "cache_read_input_tokens": 23802,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 23802,
          "cache_creation_input_tokens": 4881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4881
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

_source line 14 · 2026-05-20T22:24:05.609Z_

Let me read the existing dream reports and MVP data to calibrate predictions precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56aab84f-7555-48a0-9c57-4c2dc2d17fb2",
  "isSidechain": false,
  "requestId": "req_011CbEbyqCycwvvzbxgP33t8",
  "type": "assistant",
  "uuid": "63580f28-88ca-469a-ab86-a18089b145c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EiQFaxDbscb7ExyuU7rbVD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4881,
      "cache_read_input_tokens": 23802,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 23802,
          "cache_creation_input_tokens": 4881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4881
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

_source line 15 · 2026-05-20T22:24:06.590Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Pyr5WXPFVPN1MNFiNRmbw2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63580f28-88ca-469a-ab86-a18089b145c2",
  "isSidechain": false,
  "requestId": "req_011CbEbyqCycwvvzbxgP33t8",
  "type": "assistant",
  "uuid": "0c2686d6-0a9e-4401-b99f-2c9f12aca353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EiQFaxDbscb7ExyuU7rbVD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4881,
      "cache_read_input_tokens": 23802,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 23802,
          "cache_creation_input_tokens": 4881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4881
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

_source line 16 · 2026-05-20T22:24:07.869Z_

<details><summary>↩ Tool result · `toolu_01UCAtqmbYKYEBWgVmwkHvc8`</summary>

```text
1	[
2	  {
3	    "name": "Full-scale precision study with confound fix",
4	    "description": "4 models × 3 precisions (FP32/BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items, 全部使用vLLM V0 enforce_eager消除engine差异。总条件数 4×3×6×6×3×4=5184 per item, 总记录 5184×200=1,036,800。\n",
5	    "results": {
6	      "total_records": 1036800,
7	      "conditions_per_model": 1296,
8	      "overall_accuracy": 0.668,
9	      "accuracy_fp32": 0.666,
10	      "accuracy_bf16": 0.671,
11	      "accuracy_fp16": 0.669,
12	      "accuracy_spread_across_precisions": 0.005,
13	      "item_id": 0.584,
14	      "residual": 0.168,
15	      "prompt_template_x_item_id": 0.061,
16	      "temperature_x_item_id": 0.058,
17	      "seed_x_item_id": 0.029,
18	      "precision_x_item_id": 0.018,
19	      "ordering_x_item_id": 0.014,
20	      "prompt_template": 0.009,
21	      "temperature": 0.007,
22	      "ordering": 0.003,
23	      "precision": 0.003,
24	      "seed": 0.001,
25	      "models_with_item_id_rank1": 4,
26	      "item_id_range_across_models": [
27	        0.52,
28	        0.62
29	      ],
30	      "qwen3_8b_item_id": 0.598,
31	      "llama31_8b_item_id": 0.571,
32	      "gemma2_9b_item_id": 0.62,
33	      "mistral_7b_item_id": 0.547,
34	      "precision_main_effect_before_fix_mvp": 0.0087,
35	      "precision_main_effect_after_fix": 0.003,
36	      "precision_x_item_id_before_fix_mvp": 0.0724,
37	      "precision_x_item_id_after_fix": 0.018,
38	      "fp32_bf16_accuracy_gap_before_fix": 0.085,
39	      "fp32_bf16_accuracy_gap_after_fix": 0.005,
40	      "g_current_practice_1p1s200i": 0.34,
41	      "g_6p6s200i": 0.72,
42	      "g_6p6s200i_3t4o": 0.78
43	    },
44	    "tables": [
45	      {
46	        "name": "Table 1: Variance Component Estimates — MMLU 200 items, 4 models pooled",
47	        "columns": [
48	          "Component",
49	          "% Variance",
50	          "SE",
51	          "95% CI Lower",
52	          "95% CI Upper",
53	          "MVP (50 items)"
54	        ],
55	        "rows": [
56	          [
57	            "item_id",
58	            58.4,
59	            2.1,
60	            54.3,
61	            62.5,
62	            58.4
63	          ],
64	          [
65	            "residual",
66	            16.8,
67	            0.9,
68	            15.0,
69	            18.6,
70	            17.6
71	          ],
72	          [
73	            "prompt×item",
74	            6.1,
75	            0.7,
76	            4.7,
77	            7.5,
78	            5.7
79	          ],
80	          [
81	            "temp×item",
82	            5.8,
83	            0.6,
84	            4.6,
85	            7.0,
86	            6.9
87	          ],
88	          [
89	            "seed×item",
90	            2.9,
91	            0.4,
92	            2.1,
93	            3.7,
94	            2.7
95	          ],
96	          [
97	            "precision×item",
98	            1.8,
99	            0.3,
100	            1.2,
101	            2.4,
102	            "7.2*"
103	          ],
104	          [
105	            "ordering×item",
106	            1.4,
107	            0.3,
108	            0.8,
109	            2.0,
110	            "—"
111	          ],
112	          [
113	            "prompt",
114	            0.9,
115	            0.3,
116	            0.3,
117	            1.5,
118	            "—"
119	          ],
120	          [
121	            "temperature",
122	            0.7,
123	            0.2,
124	            0.3,
125	            1.1,
126	            "—"
127	          ],
128	          [
129	            "precision",
130	            0.3,
131	            0.1,
132	            0.1,
133	            0.5,
134	            "0.87*"
135	          ],
136	          [
137	            "ordering",
138	            0.3,
139	            0.1,
140	            0.1,
141	            0.5,
142	            "—"
143	          ],
144	          [
145	            "seed",
146	            0.1,
147	            0.05,
148	            0.0,
149	            0.2,
150	            "—"
151	          ]
152	        ]
153	      },
154	      {
155	        "name": "Table 2: Per-Model item_id Variance Share",
156	        "columns": [
157	          "Model",
158	          "item_id %",
159	          "Next Largest",
160	          "Next %"
161	        ],
162	        "rows": [
163	          [
164	            "Qwen3-8B",
165	            59.8,
166	            "residual",
167	            16.2
168	          ],
169	          [
170	            "Llama-3.1-8B",
171	            57.1,
172	            "residual",
173	            17.8
174	          ],
175	          [
176	            "Gemma-2-9B-IT",
177	            62.0,
178	            "residual",
179	            14.9
180	          ],
181	          [
182	            "Mistral-7B-v0.3",
183	            54.7,
184	            "residual",
185	            18.5
186	          ]
187	        ]
188	      }
189	    ],
190	    "figures": [],
191	    "analysis": "核心发现：engine confound修复后item dominance完全稳健，precision主效应从0.87%降至0.3%。 这同时验证了Claim 1（item dominance）和提供了方法论贡献（engine配置对variance attribution的影响）。 4个模型一致性消除了\"Qwen3特例\"的concern。200 items分层采样提供了足够的statistical power。 Ordering facet新增后占比很小（~1.7% total含interaction），说明item presentation order不是主要concern。\n\n\nMVP中precision主效应0.87%和precision×item交互7.24%主要来自float32使用不同vLLM engine路径（非V0时触发不同kernel）， 导致FP32准确率系统性偏低5.7pp。统一V0 enforce_eager后，三种精度走同一compute path， FP32/BF16/FP16准确率差收敛至0.5pp以内（纯numerical noise水平）。precision主效应从0.87%降至~0.3%， precision×item从7.24%降至~1.8%。这些被释放的方差份额主要回流到residual和item_id， 使item_id维持在~58%（与MVP一致，因为item difficulty本身是真实信号，不受engine confound影响）。 4个模型均以item_id为rank-1组分，因为MMLU的item difficulty分布（从trivial到expert-level） 在所有7-9B模型上产生类似的accuracy ceiling/floor效应。Gemma-2略高因其instruction-tuned特性 使其对easy items更稳定（floor更高），Mistral略低因其在部分domain上accuracy更平坦。 200 items（分层采样）比MVP的50 items提供更稳定的方差估计，置信区间收窄约50%。\n"
192	  },
193	  {
194	    "name": "Multi-benchmark replication",
195	    "description": "4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 items, 分别在GSM8K、ARC-Challenge、HellaSwag上运行。每benchmark总记录 4×2×6×6×2×4×200=230,400。\n",
196	    "results": {
197	      "gsm8k_overall_accuracy": 0.583,
198	      "gsm8k_item_id": 0.487,
199	      "gsm8k_residual": 0.214,
200	      "gsm8k_temperature_x_item_id": 0.089,
201	      "gsm8k_prompt_x_item_id": 0.072,
202	      "gsm8k_seed_x_item_id": 0.041,
203	      "gsm8k_precision_x_item_id": 0.012,
204	      "gsm8k_ordering_x_item_id": 0.018,
205	      "gsm8k_temperature": 0.024,
206	      "gsm8k_prompt": 0.015,
207	      "gsm8k_precision": 0.002,
208	      "gsm8k_g_current_practice": 0.29,
209	      "arc_overall_accuracy": 0.597,
210	      "arc_item_id": 0.551,
211	      "arc_residual": 0.182,
212	      "arc_prompt_x_item_id": 0.068,
213	      "arc_temperature_x_item_id": 0.054,
214	      "arc_seed_x_item_id": 0.031,
215	      "arc_precision_x_item_id": 0.014,
216	      "arc_ordering_x_item_id": 0.016,
217	      "arc_prompt": 0.011,
218	      "arc_temperature": 0.008,
219	      "arc_precision": 0.002,
220	      "arc_g_current_practice": 0.32,
221	      "hellaswag_overall_accuracy": 0.712,
222	      "hellaswag_item_id": 0.527,
223	      "hellaswag_residual": 0.195,
224	      "hellaswag_prompt_x_item_id": 0.058,
225	      "hellaswag_temperature_x_item_id": 0.062,
226	      "hellaswag_seed_x_item_id": 0.033,
227	      "hellaswag_precision_x_item_id": 0.011,
228	      "hellaswag_ordering_x_item_id": 0.019,
229	      "hellaswag_prompt": 0.008,
230	      "hellaswag_temperature": 0.006,
231	      "hellaswag_precision": 0.001,
232	      "hellaswag_g_current_practice": 0.36,
233	      "benchmarks_with_item_id_rank1": 4,
234	      "item_id_range_across_benchmarks": [
235	        0.487,
236	        0.584
237	      ],
238	      "cross_benchmark_replication_rate": 1.0,
239	      "models_showing_consistent_pattern": 4
240	    },
241	    "tables": [
242	      {
243	        "name": "Table 3: Cross-Benchmark Variance Decomposition Summary",
244	        "columns": [
245	          "Benchmark",
246	          "item_id %",
247	          "Residual %",
248	          "Item-Conditional Total %",
249	          "Precision Main %",
250	          "G (current)"
251	        ],
252	        "rows": [
253	          [
254	            "MMLU",
255	            58.4,
256	            16.8,
257	            16.1,
258	            0.3,
259	            0.34
260	          ],
261	          [
262	            "GSM8K",
263	            48.7,
264	            21.4,
265	            23.2,
266	            0.2,
267	            0.29
268	          ],
269	          [
270	            "ARC-Challenge",
271	            55.1,
272	            18.2,
273	            18.3,
274	            0.2,
275	            0.32
276	          ],
277	          [
278	            "HellaSwag",
279	            52.7,
280	            19.5,
281	            18.3,
282	            0.1,
283	            0.36
284	          ]
285	        ]
286	      },
287	      {
288	        "name": "Table 4: GSM8K Per-Model Breakdown",
289	        "columns": [
290	          "Model",
291	          "item_id %",
292	          "temp×item %",
293	          "prompt×item %",
294	          "residual %"
295	        ],
296	        "rows": [
297	          [
298	            "Qwen3-8B",
299	            51.2,
300	            8.1,
301	            6.8,
302	            19.8
303	          ],
304	          [
305	            "Llama-3.1-8B",
306	            47.3,
307	            9.4,
308	            7.6,
309	            22.1
310	          ],
311	          [
312	            "Gemma-2-9B-IT",
313	            50.8,
314	            8.5,
315	            6.9,
316	            20.3
317	          ],
318	          [
319	            "Mistral-7B-v0.3",
320	            43.4,
321	            10.5,
322	            8.3,
323	            23.5
324	          ]
325	        ]
326	      }
327	    ],
328	    "figures": [],
329	    "analysis": "Item dominance在4个benchmark上全部复现（range 48.7%-58.4%），但幅度因task type有系统性差异： generation-heavy tasks（GSM8K）因CoT随机性使residual膨胀，压缩item_id相对占比； classification-like tasks（MMLU, ARC）的item_id更高。这个gradient本身是有趣的发现， 可在Discussion中展开。关键是即使在\"worst case\"的GSM8K上，item_id仍是rank-1（48.7% > residual 21.4%）， headline claim成立。\n\n\nGSM8K的item_id占比略低于MMLU（48.7% vs 58.4%），因为数学推理任务引入更多chain-of-thought随机性， 使residual和temperature×item交互膨胀。GSM8K中温度效应更大（temperature×item 8.9%）， 因为CoT生成路径对sampling temperature更敏感——同一道数学题在不同温度下可能走完全不同的推理链。 但item_id仍然是rank-1组分，因为GSM8K的difficulty gradient极陡（从单步算术到多步word problem）， 这种item-level variance在所有条件下都主导。ARC-Challenge的item_id（55.1%）接近MMLU， 因为科学推理题的difficulty分布类似（从factual recall到multi-hop inference）。 HellaSwag的item_id（52.7%）也稳健，因为commonsense completion的item variance主要来自 distractor quality差异——有些items的wrong answers显而易见，有些几乎无法区分。 所有benchmark上precision主效应均<0.3%，确认engine confound fix的泛化性。 4/4 benchmark的item_id rank-1复现率为100%，支撑\"cross-benchmark replication rate = 1.0\"。\n"
330	  },
331	  {
332	    "name": "Multi-hardware G-study",
333	    "description": "4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。总记录 4×2×2×6×6×3×4×200=691,200。 核心目标：量化hardware主效应和hardware×methodology交互。\n",
334	    "results": {
335	      "total_records": 691200,
336	      "hardware_main_effect": 0.006,
337	      "hardware_x_precision": 0.002,
338	      "hardware_x_prompt": 0.001,
339	      "hardware_x_temperature": 0.001,
340	      "hardware_x_seed": 0.0005,
341	      "hardware_x_ordering": 0.0003,
342	      "hardware_x_item_id": 0.019,
343	      "precision_x_prompt": 0.0008,
344	      "precision_x_temperature": 0.0006,
345	      "precision_x_seed": 0.0003,
346	      "precision_x_ordering": 0.0002,
347	      "direct_infra_method_interaction_total": 0.005,
348	      "item_conditional_interactions_total": 0.142,
349	      "item_id": 0.561,
350	      "residual": 0.152,
351	      "prompt_x_item": 0.059,
352	      "temperature_x_item": 0.055,
353	      "seed_x_item": 0.028,
354	      "precision_x_item": 0.017,
355	      "ordering_x_item": 0.013,
356	      "hardware_x_item": 0.019,
357	      "separability_ratio": 0.035,
358	      "gpu1_gpu2_accuracy_correlation": 0.9987,
359	      "max_accuracy_difference_any_condition": 0.018,
360	      "mean_accuracy_difference": 0.004,
361	      "g_current_practice": 0.33,
362	      "g_full_design": 0.81
363	    },
364	    "tables": [
365	      {
366	        "name": "Table 5: Separability Test — Direct vs Item-Conditional Interactions",
367	        "columns": [
368	          "Interaction Type",
369	          "Components",
370	          "Total % Variance",
371	          "Interpretation"
372	        ],
373	        "rows": [
374	          [
375	            "Direct Infra×Method",
376	            "hw×prompt, hw×temp, hw×seed, hw×ord, prec×prompt, prec×temp, prec×seed, prec×ord",
377	            0.5,
378	            "Negligible — separability holds at aggregate"
379	          ],
380	          [
381	            "Infra×Item",
382	            "hw×item, prec×item",
383	            3.6,
384	            "Small but non-zero — hardware/precision effects are item-conditional"
385	          ],
386	          [
387	            "Method×Item",
388	            "prompt×item, temp×item, seed×item, ord×item",
389	            15.5,
390	            "Substantial — methodology effects are strongly item-conditional"
391	          ],
392	          [
393	            "Item Main",
394	            "item_id",
395	            56.1,
396	            "Dominant — item selection is the primary variance source"
397	          ]
398	        ]
399	      },
400	      {
401	        "name": "Table 6: Hardware Agreement Matrix (per-model mean accuracy)",
402	        "columns": [
403	          "Model",
404	          "GPU1",
405	          "GPU2",
406	          "Difference"
407	        ],
408	        "rows": [
409	          [
410	            "Qwen3-8B",
411	            0.671,
412	            0.668,
413	            0.003
414	          ],
415	          [
416	            "Llama-3.1-8B",
417	            0.654,
418	            0.65,
419	            0.004
420	          ],
421	          [
422	            "Gemma-2-9B-IT",
423	            0.689,
424	            0.684,
425	            0.005
426	          ],
427	          [
428	            "Mistral-7B-v0.3",
429	            0.638,
430	            0.634,
431	            0.004
432	          ]
433	        ]
434	      }
435	    ],
436	    "figures": [],
437	    "analysis": "Separability成立：direct infra×method交互总和0.5%，远低于1%阈值。但不是trivial null result—— item-conditional interactions（14.2%）提供了nuanced interpretation：infrastructure和methodology 不是完全独立的，而是通过item difficulty间接耦合。这比simple \"separable/not separable\"更有价值， 因为它解释了为什么isolated-factor studies的结论在某些items上不泛化。 这同时支撑了Claim 2的两半：\"empirical license for isolated-factor studies\"（direct <0.5%） 和 \"conclusions are conditional on item selection\"（item-conditional 14.2%）。\n\n\nHardware主效应0.6%反映两块GPU的微架构差异（不同SM count、memory bandwidth、kernel scheduling）， 但这些差异是系统性的（固定偏移），不是随机的，所以主效应很小。hardware×item交互1.9%比hardware主效应大， 因为特定items（如需要长sequence generation的items）在不同GPU上因kernel tiling差异产生不同的numerical path， 但这只影响边界case items。所有direct infra×method交互加总仅0.5%，因为infrastructure层（hardware type, precision） 和methodology层（prompt, seed, temperature, ordering）作用于不同的computation stages： precision/hardware影响numerical computation，prompt/seed/temperature影响token sampling， 两者的交叉点（sampling受precision影响的程度）在logit空间中被softmax压缩到negligible水平。 Item-conditional interactions总和14.2%远大于direct interactions 0.5%，验证了Claim 2的nuanced story： separability在aggregate成立，但两层都通过item difficulty调节其效应。 GPU间accuracy correlation 0.9987说明hardware几乎不改变model ranking，只在individual item level引入微小噪声。\n"
438	  },
439	  {
440	    "name": "D-study reproducibility budget projections",
441	    "description": "基于exp-001/002/003的合并variance component estimates，计算不同facet allocation下的G系数。 生成practitioner-facing budget tables和projection curves。纯计算，无GPU开销。\n",
442	    "results": {
443	      "g_1prompt_1seed_200items_mmlu": 0.34,
444	      "g_1prompt_1seed_200items_gsm8k": 0.29,
445	      "g_1prompt_1seed_200items_arc": 0.32,
446	      "g_1prompt_1seed_200items_hellaswag": 0.36,
447	      "g_1prompt_1seed_600items_mmlu": 0.71,
448	      "g_1prompt_1seed_1000items_mmlu": 0.82,
449	      "g_1prompt_1seed_2000items_mmlu": 0.9,
450	      "g_3prompt_1seed_200items_mmlu": 0.42,
451	      "g_6prompt_1seed_200items_mmlu": 0.49,
452	      "g_12prompt_1seed_200items_mmlu": 0.54,
453	      "g_1prompt_3seed_200items_mmlu": 0.36,
454	      "g_1prompt_6seed_200items_mmlu": 0.37,
455	      "optimal_g90_items": 600,
456	      "optimal_g90_prompts": 3,
457	      "optimal_g90_seeds": 2,
458	      "optimal_g90_total_conditions": 6,
459	      "optimal_g90_total_evaluations": 3600,
460	      "optimal_g95_items": 1200,
461	      "optimal_g95_prompts": 4,
462	      "optimal_g95_seeds": 3,
463	      "optimal_g95_total_conditions": 12,
464	      "optimal_g95_total_evaluations": 14400,
465	      "marginal_g_per_100_items": 0.038,
466	      "marginal_g_per_prompt": 0.025,
467	      "marginal_g_per_seed": 0.005,
468	      "items_vs_prompts_effectiveness_ratio": 10.2,
469	      "items_vs_seeds_effectiveness_ratio": 51.0,
470	      "gsm8k_optimal_g90_items": 800,
471	      "gsm8k_optimal_g90_prompts": 3,
472	      "gsm8k_optimal_g90_seeds": 2,
473	      "arc_optimal_g90_items": 650,
474	      "hellaswag_optimal_g90_items": 550
475	    },
476	    "tables": [
477	      {
478	        "name": "Table 7: Reproducibility Budget — MMLU (Items × Prompts × Seeds → G coefficient)",
479	        "columns": [
480	          "Items",
481	          "Prompts",
482	          "Seeds",
483	          "Total Evals",
484	          "G coeff",
485	          "Δ vs Current"
486	        ],
487	        "rows": [
488	          [
489	            200,
490	            1,
491	            1,
492	            200,
493	            0.34,
494	            "baseline"
495	          ],
496	          [
497	            200,
498	            3,
499	            1,
500	            600,
501	            0.42,
502	            "+0.08"
503	          ],
504	          [
505	            200,
506	            6,
507	            1,
508	            1200,
509	            0.49,
510	            "+0.15"
511	          ],
512	          [
513	            200,
514	            6,
515	            6,
516	            7200,
517	            0.54,
518	            "+0.20"
519	          ],
520	          [
521	            600,
522	            1,
523	            1,
524	            600,
525	            0.71,
526	            "+0.37"
527	          ],
528	          [
529	            600,
530	            3,
531	            1,
532	            1800,
533	            0.82,
534	            "+0.48"
535	          ],
536	          [
537	            600,
538	            3,
539	            2,
540	            3600,
541	            0.9,
542	            "+0.56"
543	          ],
544	          [
545	            1000,
546	            3,
547	            2,
548	            6000,
549	            0.93,
550	            "+0.59"
551	          ],
552	          [
553	            1200,
554	            4,
555	            3,
556	            14400,
557	            0.95,
558	            "+0.61"
559	          ],
560	          [
561	            2000,
562	            4,
563	            3,
564	            24000,
565	            0.97,
566	            "+0.63"
567	          ]
568	        ]
569	      },
570	      {
571	        "name": "Table 8: Cross-Benchmark Minimum Budget for G≥0.90",
572	        "columns": [
573	          "Benchmark",
574	          "Items",
575	          "Prompts",
576	          "Seeds",
577	          "Total Evals",
578	          "Cost Factor vs Current"
579	        ],
580	        "rows": [
581	          [
582	            "MMLU",
583	            600,
584	            3,
585	            2,
586	            3600,
587	            "18×"
588	          ],
589	          [
590	            "GSM8K",
591	            800,
592	            3,
593	            2,
594	            4800,
595	            "24×"
596	          ],
597	          [
598	            "ARC-Challenge",
599	            650,
600	            3,
601	            2,
602	            3900,
603	            "19.5×"
604	          ],
605	          [
606	            "HellaSwag",
607	            550,
608	            3,
609	            2,
610	            3300,
611	            "16.5×"
612	          ]
613	        ]
614	      }
615	    ],
616	    "figures": [],
617	    "analysis": "Claim 3的核心表格。Headline数字：\"tripling items is 10× more effective than tripling prompts\" 直接来自marginal effectiveness ratio 10.2:1。当前practice G<0.40的发现具有强policy implication—— 意味着现有leaderboard结果的measurement reliability低于社会科学中最低标准。 600 items + 3 prompts + 2 seeds的\"recommended minimum\"在计算成本上仅为full factorial的一小部分， 是actionable的建议。跨benchmark budget差异（550-800 items for G≥0.90）提供task-specific guidance。\n\n\nG系数由universe score variance与observed score variance的比值决定。因为item_id占总方差>50%， 增加item采样直接压缩最大的variance component，G提升最快。具体地，G ≈ σ²(τ) / [σ²(τ) + σ²(δ)/n_facets]， 当item_id是σ²(δ)的主要贡献者时，增加n_items的marginal return远超增加n_prompts或n_seeds。 数值上，从200到600 items（3×）使G从0.34升至0.71，而从1到3 prompts（3×）仅从0.34升至0.42。 这是因为prompt variance（含prompt×item）共计~7%，而item variance 58%。 Seed几乎无效（G从0.34到0.37 at 6 seeds），因为seed的总方差贡献<3%（主要通过seed×item）。 G≥0.90需要~600 items + 3 prompts + 2 seeds = 3,600 evaluations。 当前标准practice（1 prompt, 1 seed, 200 items）的G < 0.40意味着evaluation结果的reliability 低于社会科学中\"不可接受\"的阈值（通常G≥0.80）。 GSM8K需要更多items（800 vs 600）达到G≥0.90，因为其residual更大（CoT随机性）， 需要更多items来平均掉item-level noise。\n"
618	  },
619	  {
620	    "name": "14B model extension",
621	    "description": "Qwen3-14B和DeepSeek-R1-Distill-14B × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。每模型 2×6×6×3×4×200=172,800记录。\n",
622	    "results": {
623	      "qwen3_14b_accuracy": 0.728,
624	      "deepseek_r1_14b_accuracy": 0.714,
625	      "qwen3_14b_item_id": 0.574,
626	      "deepseek_r1_14b_item_id": 0.538,
627	      "qwen3_14b_residual": 0.162,
628	      "deepseek_r1_14b_residual": 0.198,
629	      "deepseek_r1_14b_temperature_x_item": 0.082,
630	      "scale_effect_on_item_id": "within 8B model range",
631	      "item_id_rank1_both_models": true,
632	      "variance_pattern_consistent_with_8b": true,
633	      "precision_main_effect_14b": 0.002
634	    },
635	    "tables": [
636	      {
637	        "name": "Table 9: 14B vs 8B Variance Pattern Comparison",
638	        "columns": [
639	          "Component",
640	          "8B Mean",
641	          "8B Range",
642	          "Qwen3-14B",
643	          "DS-R1-14B"
644	        ],
645	        "rows": [
646	          [
647	            "item_id",
648	            58.4,
649	            "54.7–62.0",
650	            57.4,
651	            53.8
652	          ],
653	          [
654	            "residual",
655	            16.8,
656	            "14.9–18.5",
657	            16.2,
658	            19.8
659	          ],
660	          [
661	            "temp×item",
662	            5.8,
663	            "4.6–7.0",
664	            5.3,
665	            8.2
666	          ],
667	          [
668	            "prompt×item",
669	            6.1,
670	            "4.7–7.5",
671	            5.8,
672	            5.4
673	          ],
674	          [
675	            "precision",
676	            0.3,
677	            "0.1–0.5",
678	            0.2,
679	            0.2
680	          ]
681	        ]
682	      }
683	    ],
684	    "figures": [],
685	    "analysis": "Scale invariance确认：item dominance不是小模型artifacts。DeepSeek-R1-Distill的slightly不同的profile （更高residual, 更高temp×item）提供了architecture effect的初步evidence， 但不改变core claim。这是P1实验，为paper增加robustness但非必需。\n\n\n14B模型的overall accuracy更高，但item difficulty的variance structure不会因scale改变—— easy items仍然easy，hard items仍然hard。Item_id占比略低于8B平均值（~55-57% vs ~58%）， 因为14B模型在medium-difficulty items上表现更一致（ceiling effect压缩了item variance的上端）， 但差异不大。DeepSeek-R1-Distill的reasoning-distilled特性使其在CoT-heavy items上产生更多 temperature×item交互（类似GSM8K的pattern），residual也略高，因为distillation引入的implicit CoT 增加了generation-level stochasticity。关键是item_id在两个14B模型上仍为rank-1， 确认pattern不随model scale改变。precision主效应在14B上同样negligible（0.2%）， 因为confound fix的原理（统一engine path）与model size无关。\n"
686	  },
687	  {
688	    "name": "Fine-tuning G-study",
689	    "description": "RoBERTa-large在SST-2/MNLI/RTE/COPA上fine-tuning。6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 total。\n",
690	    "results": {
691	      "sst2_accuracy_mean": 0.948,
692	      "sst2_item_id": 0.412,
693	      "sst2_seed": 0.087,
694	      "sst2_learning_rate": 0.063,
695	      "sst2_data_shuffle": 0.042,
696	      "sst2_seed_x_item": 0.098,
697	      "sst2_lr_x_item": 0.074,
698	      "sst2_residual": 0.131,
699	      "sst2_gpu": 0.003,
700	      "sst2_precision": 0.002,
701	      "mnli_accuracy_mean": 0.876,
702	      "mnli_item_id": 0.445,
703	      "mnli_seed": 0.072,
704	      "mnli_learning_rate": 0.081,
705	      "mnli_data_shuffle": 0.038,
706	      "mnli_seed_x_item": 0.091,
707	      "mnli_residual": 0.142,
708	      "rte_accuracy_mean": 0.743,
709	      "rte_item_id": 0.368,
710	      "rte_seed": 0.124,
711	      "rte_learning_rate": 0.098,
712	      "rte_data_shuffle": 0.067,
713	      "rte_seed_x_item": 0.112,
714	      "rte_residual": 0.158,
715	      "copa_accuracy_mean": 0.682,
716	      "copa_item_id": 0.382,
717	      "copa_seed": 0.118,
718	      "copa_learning_rate": 0.091,
719	      "copa_residual": 0.167,
720	      "item_id_rank1_all_tasks": true,
721	      "seed_more_important_than_inference": true,
722	      "infra_effects_negligible": true,
723	      "fine_tuning_g_current_practice": 0.28
724	    },
725	    "tables": [
726	      {
727	        "name": "Table 10: Fine-tuning vs Inference Variance Hierarchy",
728	        "columns": [
729	          "Rank",
730	          "Inference (MMLU)",
731	          "Fine-tuning (SST-2)"
732	        ],
733	        "rows": [
734	          [
735	            1,
736	            "item_id (58.4%)",
737	            "item_id (41.2%)"
738	          ],
739	          [
740	            2,
741	            "residual (16.8%)",
742	            "residual (13.1%)"
743	          ],
744	          [
745	            3,
746	            "prompt×item (6.1%)",
747	            "seed×item (9.8%)"
748	          ],
749	          [
750	            4,
751	            "temp×item (5.8%)",
752	            "seed (8.7%)"
753	          ],
754	          [
755	            5,
756	            "seed×item (2.9%)",
757	            "lr×item (7.4%)"
758	          ],
759	          [
760	            6,
761	            "precision×item (1.8%)",
762	            "lr (6.3%)"
763	          ]
764	        ]
765	      }
766	    ],
767	    "figures": [],
768	    "analysis": "Fine-tuning G-study将paper从\"inference evaluation reproducibility\"扩展到\"ML reproducibility broadly\"。 核心takeaway：item dominance是跨paradigm的（inference和fine-tuning），但second-tier factors不同。 这是P1实验，为paper增加generality但AAAI投稿时可作为supplementary。\n\n\nFine-tuning与inference的关键区别：training seed和learning rate成为substantial variance sources （combined 10-22%），因为它们影响optimization trajectory，不仅仅是sampling randomness。 但item_id仍然是rank-1（37-45%），因为NLU tasks的item difficulty gradient—— 从\"I love this movie\"(trivially positive)到需要subtle pragmatic inference的examples—— 在所有training configurations下都产生consistent accuracy variation。 RTE的item_id最低（36.8%），因为小数据集（2.5K training examples）使fine-tuning对seed更敏感， seed主效应膨胀到12.4%。这为paper提供了\"inference vs fine-tuning\"的对比dimension： 两者都是item-dominant，但fine-tuning中training hyperparameters（seed, LR）取代了 inference中的generation parameters（temperature, prompt）成为第二梯队的variance sources。 GPU和precision主效应在fine-tuning中同样negligible（<0.5%），因为RoBERTa-large 对numerical precision不敏感（unlike large generative models的autoregressive error accumulation）。\n"
769	  },
770	  {
771	    "name": "LayerCast precision study",
772	    "description": "在MMLU上测试LayerCast（FP16 storage + FP32 compute）作为额外precision condition。 4 models × 1 precision mode × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 items = 172,800记录。\n",
773	    "results": {
774	      "layercast_accuracy_mean": 0.67,
775	      "layercast_vs_fp32_accuracy_diff": 0.004,
776	      "layercast_vs_bf16_accuracy_diff": -0.001,
777	      "layercast_item_agreement_with_fp32": 0.9991,
778	      "layercast_item_agreement_with_bf16": 0.9994,
779	      "layercast_added_variance_to_precision": 0.0004,
780	      "layercast_throughput_vs_fp32": 1.38,
781	      "layercast_throughput_vs_bf16": 0.91,
782	      "layercast_precision_x_item_contribution": 0.009
783	    },
784	    "tables": [
785	      {
786	        "name": "Table 11: Precision Mode Comparison",
787	        "columns": [
788	          "Mode",
789	          "Accuracy",
790	          "item Agreement w/ FP32",
791	          "Throughput (tokens/s)",
792	          "VRAM (GB)"
793	        ],
794	        "rows": [
795	          [
796	            "FP32",
797	            0.666,
798	            1.0,
799	            1820,
800	            31.2
801	          ],
802	          [
803	            "BF16",
804	            0.671,
805	            0.9985,
806	            2760,
807	            15.8
808	          ],
809	          [
810	            "FP16",
811	            0.669,
812	            0.9982,
813	            2810,
814	            15.6
815	          ],
816	          [
817	            "LayerCast",
818	            0.67,
819	            0.9991,
820	            2510,
821	            16.1
822	          ]
823	        ]
824	      }
825	    ],
826	    "figures": [],
827	    "analysis": "P2实验。LayerCast结果进一步support precision不是major concern（在engine confound fix后）。 可作为paper中\"practical recommendation\"段落的一条：对于追求最高reproducibility的场景， LayerCast提供了memory-efficient的FP32-equivalent选项。\n\n\nLayerCast在存储时用FP16减少memory footprint，在compute时cast to FP32， 因此其numerical behavior几乎等同于纯FP32（computation path一致）， accuracy差异仅来自storage时的precision loss（FP16 mantissa 10 bits vs FP32 23 bits）， 这对大部分weights来说negligible（在训练时weights就是从FP16/BF16来的）。 与BF16的差异更小（0.1pp），因为BF16的dynamic range与FP32一致（8-bit exponent）， 而FP16的range更窄但mantissa更宽，两者accuracy接近。 LayerCast对precision variance几乎没有增量贡献（0.04%），因为它本质上是FP32 compute的cheaper variant。 Throughput方面，LayerCast比FP32快38%（memory bandwidth节省），比BF16慢9%（需要cast操作）。 这个实验为paper提供了一个\"practical mitigation\"故事：如果practitioner担心precision影响， LayerCast以minimal overhead提供FP32-level behavior。\n"
828	  },
829	  {
830	    "name": "MATH benchmark extension",
831	    "description": "4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 MATH items。 总记录 4×2×6×6×2×4×200=230,400。测试reasoning-heavy task的variance structure。\n",
832	    "results": {
833	      "math_overall_accuracy": 0.342,
834	      "math_item_id": 0.421,
835	      "math_residual": 0.248,
836	      "math_temperature_x_item": 0.104,
837	      "math_prompt_x_item": 0.068,
838	      "math_seed_x_item": 0.052,
839	      "math_temperature": 0.038,
840	      "math_prompt": 0.021,
841	      "math_precision": 0.002,
842	      "math_precision_x_item": 0.008,
843	      "math_ordering_x_item": 0.015,
844	      "math_g_current_practice": 0.24,
845	      "math_item_id_rank1": true,
846	      "math_optimal_g90_items": 1100,
847	      "math_optimal_g90_prompts": 4,
848	      "math_optimal_g90_seeds": 3
849	    },
850	    "tables": [
851	      {
852	        "name": "Table 12: Full Cross-Benchmark Variance Summary (5 benchmarks)",
853	        "columns": [
854	          "Benchmark",
855	          "Accuracy",
856	          "item_id %",
857	          "Residual %",
858	          "Temp×Item %",
859	          "G (current)",
860	          "Items for G≥0.90"
861	        ],
862	        "rows": [
863	          [
864	            "MMLU",
865	            0.668,
866	            58.4,
867	            16.8,
868	            5.8,
869	            0.34,
870	            600
871	          ],
872	          [
873	            "ARC-Challenge",
874	            0.597,
875	            55.1,
876	            18.2,
877	            5.4,
878	            0.32,
879	            650
880	          ],
881	          [
882	            "HellaSwag",
883	            0.712,
884	            52.7,
885	            19.5,
886	            6.2,
887	            0.36,
888	            550
889	          ],
890	          [
891	            "GSM8K",
892	            0.583,
893	            48.7,
894	            21.4,
895	            8.9,
896	            0.29,
897	            800
898	          ],
899	          [
900	            "MATH",
901	            0.342,
902	            42.1,
903	            24.8,
904	            10.4,
905	            0.24,
906	            1100
907	          ]
908	        ]
909	      }
910	    ],
911	    "figures": [],
912	    "analysis": "MATH提供了variance structure的\"stress test\"。Item_id在最extreme条件下仍为rank-1（42.1%）， 但task difficulty明显调节了variance decomposition的profile。5个benchmark展现了清晰的gradient： task difficulty ↑ → item_id share ↓, residual ↑, temperature×item ↑, G current practice ↓。 这个gradient本身是publishable finding：它量化了为什么reasoning benchmark的evaluation更不稳定， 并给出了task-specific的reproducibility budget。\n\nMATH是所有benchmark中最challenging的（accuracy ~34%），其item difficulty分布极端—— 从Level 1（algebra basics）到Level 5（competition math），跨越巨大的difficulty range。 Item_id仍为rank-1（42.1%）但低于MMLU，因为：(1) lower overall accuracy增加了random guessing的比例， 膨胀residual到24.8%；(2) MATH的CoT generation比GSM8K更长更复杂（多步proof-like reasoning）， 使temperature×item interaction达到10.4%——在高temperature下，长推理链的任何一步都可能diverge， 且这种sensitivity是item-specific的（Level 5 problems的长推理链比Level 1的短计算更sensitive）。 Temperature主效应也最高（3.8%），因为MATH的generation length使sampling temperature的cumulative effect更显著。 G current practice仅0.24——所有benchmark中最低——意味着MATH evaluation的reproducibility最差。 达到G≥0.90需要1100 items + 4 prompts + 3 seeds，是MMLU所需的~3倍evaluation budget。 这个发现有strong policy implication：reasoning benchmark的evaluation标准需要比classification benchmark更严格。\n"
913	  }
914	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "745ba392-db2a-4661-867e-a15b5f1e6c12",
  "isSidechain": false,
  "promptId": "c295c0c9-7475-4ab1-87e4-a49b6b5cf1ca",
  "type": "user",
  "uuid": "acd46e52-72a1-4587-a606-1cb48d42c0ed",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"Full-scale precision study with confound fix\",\n    \"description\": \"4 models × 3 precisions (FP32/BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items, 全部使用vLLM V0 enforce_eager消除engine差异。总条件数 4×3×6×6×3×4=5184 per item, 总记录 5184×200=1,036,800。\\n\",\n    \"results\": {\n      \"total_records\": 1036800,\n      \"conditions_per_model\": 1296,\n      \"overall_accuracy\": 0.668,\n      \"accuracy_fp32\": 0.666,\n      \"accuracy_bf16\": 0.671,\n      \"accuracy_fp16\": 0.669,\n      \"accuracy_spread_across_precisions\": 0.005,\n      \"item_id\": 0.584,\n      \"residual\": 0.168,\n      \"prompt_template_x_item_id\": 0.061,\n      \"temperature_x_item_id\": 0.058,\n      \"seed_x_item_id\": 0.029,\n      \"precision_x_item_id\": 0.018,\n      \"ordering_x_item_id\": 0.014,\n      \"prompt_template\": 0.009,\n      \"temperature\": 0.007,\n      \"ordering\": 0.003,\n      \"precision\": 0.003,\n      \"seed\": 0.001,\n      \"models_with_item_id_rank1\": 4,\n      \"item_id_range_across_models\": [\n        0.52,\n        0.62\n      ],\n      \"qwen3_8b_item_id\": 0.598,\n      \"llama31_8b_item_id\": 0.571,\n      \"gemma2_9b_item_id\": 0.62,\n      \"mistral_7b_item_id\": 0.547,\n      \"precision_main_effect_before_fix_mvp\": 0.0087,\n      \"precision_main_effect_after_fix\": 0.003,\n      \"precision_x_item_id_before_fix_mvp\": 0.0724,\n      \"precision_x_item_id_after_fix\": 0.018,\n      \"fp32_bf16_accuracy_gap_before_fix\": 0.085,\n      \"fp32_bf16_accuracy_gap_after_fix\": 0.005,\n      \"g_current_practice_1p1s200i\": 0.34,\n      \"g_6p6s200i\": 0.72,\n      \"g_6p6s200i_3t4o\": 0.78\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Variance Component Estimates — MMLU 200 items, 4 models pooled\",\n        \"columns\": [\n          \"Component\",\n          \"% Variance\",\n          \"SE\",\n          \"95% CI Lower\",\n          \"95% CI Upper\",\n          \"MVP (50 items)\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            58.4,\n            2.1,\n            54.3,\n            62.5,\n            58.4\n          ],\n          [\n            \"residual\",\n            16.8,\n            0.9,\n            15.0,\n            18.6,\n            17.6\n          ],\n          [\n            \"prompt×item\",\n            6.1,\n            0.7,\n            4.7,\n            7.5,\n            5.7\n          ],\n          [\n            \"temp×item\",\n            5.8,\n            0.6,\n            4.6,\n            7.0,\n            6.9\n          ],\n          [\n            \"seed×item\",\n            2.9,\n            0.4,\n            2.1,\n            3.7,\n            2.7\n          ],\n          [\n            \"precision×item\",\n            1.8,\n            0.3,\n            1.2,\n            2.4,\n            \"7.2*\"\n          ],\n          [\n            \"ordering×item\",\n            1.4,\n            0.3,\n            0.8,\n            2.0,\n            \"—\"\n          ],\n          [\n            \"prompt\",\n            0.9,\n            0.3,\n            0.3,\n            1.5,\n            \"—\"\n          ],\n          [\n            \"temperature\",\n            0.7,\n            0.2,\n            0.3,\n            1.1,\n            \"—\"\n          ],\n          [\n            \"precision\",\n            0.3,\n            0.1,\n            0.1,\n            0.5,\n            \"0.87*\"\n          ],\n          [\n            \"ordering\",\n            0.3,\n            0.1,\n            0.1,\n            0.5,\n            \"—\"\n          ],\n          [\n            \"seed\",\n            0.1,\n            0.05,\n            0.0,\n            0.2,\n            \"—\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 2: Per-Model item_id Variance Share\",\n        \"columns\": [\n          \"Model\",\n          \"item_id %\",\n          \"Next Largest\",\n          \"Next %\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            59.8,\n            \"residual\",\n            16.2\n          ],\n          [\n            \"Llama-3.1-8B\",\n            57.1,\n            \"residual\",\n            17.8\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            62.0,\n            \"residual\",\n            14.9\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            54.7,\n            \"residual\",\n            18.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现：engine confound修复后item dominance完全稳健，precision主效应从0.87%降至0.3%。 这同时验证了Claim 1（item dominance）和提供了方法论贡献（engine配置对variance attribution的影响）。 4个模型一致性消除了\\\"Qwen3特例\\\"的concern。200 items分层采样提供了足够的statistical power。 Ordering facet新增后占比很小（~1.7% total含interaction），说明item presentation order不是主要concern。\\n\\n\\nMVP中precision主效应0.87%和precision×item交互7.24%主要来自float32使用不同vLLM engine路径（非V0时触发不同kernel）， 导致FP32准确率系统性偏低5.7pp。统一V0 enforce_eager后，三种精度走同一compute path， FP32/BF16/FP16准确率差收敛至0.5pp以内（纯numerical noise水平）。precision主效应从0.87%降至~0.3%， precision×item从7.24%降至~1.8%。这些被释放的方差份额主要回流到residual和item_id， 使item_id维持在~58%（与MVP一致，因为item difficulty本身是真实信号，不受engine confound影响）。 4个模型均以item_id为rank-1组分，因为MMLU的item difficulty分布（从trivial到expert-level） 在所有7-9B模型上产生类似的accuracy ceiling/floor效应。Gemma-2略高因其instruction-tuned特性 使其对easy items更稳定（floor更高），Mistral略低因其在部分domain上accuracy更平坦。 200 items（分层采样）比MVP的50 items提供更稳定的方差估计，置信区间收窄约50%。\\n\"\n  },\n  {\n    \"name\": \"Multi-benchmark replication\",\n    \"description\": \"4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 items, 分别在GSM8K、ARC-Challenge、HellaSwag上运行。每benchmark总记录 4×2×6×6×2×4×200=230,400。\\n\",\n    \"results\": {\n      \"gsm8k_overall_accuracy\": 0.583,\n      \"gsm8k_item_id\": 0.487,\n      \"gsm8k_residual\": 0.214,\n      \"gsm8k_temperature_x_item_id\": 0.089,\n      \"gsm8k_prompt_x_item_id\": 0.072,\n      \"gsm8k_seed_x_item_id\": 0.041,\n      \"gsm8k_precision_x_item_id\": 0.012,\n      \"gsm8k_ordering_x_item_id\": 0.018,\n      \"gsm8k_temperature\": 0.024,\n      \"gsm8k_prompt\": 0.015,\n      \"gsm8k_precision\": 0.002,\n      \"gsm8k_g_current_practice\": 0.29,\n      \"arc_overall_accuracy\": 0.597,\n      \"arc_item_id\": 0.551,\n      \"arc_residual\": 0.182,\n      \"arc_prompt_x_item_id\": 0.068,\n      \"arc_temperature_x_item_id\": 0.054,\n      \"arc_seed_x_item_id\": 0.031,\n      \"arc_precision_x_item_id\": 0.014,\n      \"arc_ordering_x_item_id\": 0.016,\n      \"arc_prompt\": 0.011,\n      \"arc_temperature\": 0.008,\n      \"arc_precision\": 0.002,\n      \"arc_g_current_practice\": 0.32,\n      \"hellaswag_overall_accuracy\": 0.712,\n      \"hellaswag_item_id\": 0.527,\n      \"hellaswag_residual\": 0.195,\n      \"hellaswag_prompt_x_item_id\": 0.058,\n      \"hellaswag_temperature_x_item_id\": 0.062,\n      \"hellaswag_seed_x_item_id\": 0.033,\n      \"hellaswag_precision_x_item_id\": 0.011,\n      \"hellaswag_ordering_x_item_id\": 0.019,\n      \"hellaswag_prompt\": 0.008,\n      \"hellaswag_temperature\": 0.006,\n      \"hellaswag_precision\": 0.001,\n      \"hellaswag_g_current_practice\": 0.36,\n      \"benchmarks_with_item_id_rank1\": 4,\n      \"item_id_range_across_benchmarks\": [\n        0.487,\n        0.584\n      ],\n      \"cross_benchmark_replication_rate\": 1.0,\n      \"models_showing_consistent_pattern\": 4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: Cross-Benchmark Variance Decomposition Summary\",\n        \"columns\": [\n          \"Benchmark\",\n          \"item_id %\",\n          \"Residual %\",\n          \"Item-Conditional Total %\",\n          \"Precision Main %\",\n          \"G (current)\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            58.4,\n            16.8,\n            16.1,\n            0.3,\n            0.34\n          ],\n          [\n            \"GSM8K\",\n            48.7,\n            21.4,\n            23.2,\n            0.2,\n            0.29\n          ],\n          [\n            \"ARC-Challenge\",\n            55.1,\n            18.2,\n            18.3,\n            0.2,\n            0.32\n          ],\n          [\n            \"HellaSwag\",\n            52.7,\n            19.5,\n            18.3,\n            0.1,\n            0.36\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 4: GSM8K Per-Model Breakdown\",\n        \"columns\": [\n          \"Model\",\n          \"item_id %\",\n          \"temp×item %\",\n          \"prompt×item %\",\n          \"residual %\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            51.2,\n            8.1,\n            6.8,\n            19.8\n          ],\n          [\n            \"Llama-3.1-8B\",\n            47.3,\n            9.4,\n            7.6,\n            22.1\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            50.8,\n            8.5,\n            6.9,\n            20.3\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            43.4,\n            10.5,\n            8.3,\n            23.5\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Item dominance在4个benchmark上全部复现（range 48.7%-58.4%），但幅度因task type有系统性差异： generation-heavy tasks（GSM8K）因CoT随机性使residual膨胀，压缩item_id相对占比； classification-like tasks（MMLU, ARC）的item_id更高。这个gradient本身是有趣的发现， 可在Discussion中展开。关键是即使在\\\"worst case\\\"的GSM8K上，item_id仍是rank-1（48.7% > residual 21.4%）， headline claim成立。\\n\\n\\nGSM8K的item_id占比略低于MMLU（48.7% vs 58.4%），因为数学推理任务引入更多chain-of-thought随机性， 使residual和temperature×item交互膨胀。GSM8K中温度效应更大（temperature×item 8.9%）， 因为CoT生成路径对sampling temperature更敏感——同一道数学题在不同温度下可能走完全不同的推理链。 但item_id仍然是rank-1组分，因为GSM8K的difficulty gradient极陡（从单步算术到多步word problem）， 这种item-level variance在所有条件下都主导。ARC-Challenge的item_id（55.1%）接近MMLU， 因为科学推理题的difficulty分布类似（从factual recall到multi-hop inference）。 HellaSwag的item_id（52.7%）也稳健，因为commonsense completion的item variance主要来自 distractor quality差异——有些items的wrong answers显而易见，有些几乎无法区分。 所有benchmark上precision主效应均<0.3%，确认engine confound fix的泛化性。 4/4 benchmark的item_id rank-1复现率为100%，支撑\\\"cross-benchmark replication rate = 1.0\\\"。\\n\"\n  },\n  {\n    \"name\": \"Multi-hardware G-study\",\n    \"description\": \"4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。总记录 4×2×2×6×6×3×4×200=691,200。 核心目标：量化hardware主效应和hardware×methodology交互。\\n\",\n    \"results\": {\n      \"total_records\": 691200,\n      \"hardware_main_effect\": 0.006,\n      \"hardware_x_precision\": 0.002,\n      \"hardware_x_prompt\": 0.001,\n      \"hardware_x_temperature\": 0.001,\n      \"hardware_x_seed\": 0.0005,\n      \"hardware_x_ordering\": 0.0003,\n      \"hardware_x_item_id\": 0.019,\n      \"precision_x_prompt\": 0.0008,\n      \"precision_x_temperature\": 0.0006,\n      \"precision_x_seed\": 0.0003,\n      \"precision_x_ordering\": 0.0002,\n      \"direct_infra_method_interaction_total\": 0.005,\n      \"item_conditional_interactions_total\": 0.142,\n      \"item_id\": 0.561,\n      \"residual\": 0.152,\n      \"prompt_x_item\": 0.059,\n      \"temperature_x_item\": 0.055,\n      \"seed_x_item\": 0.028,\n      \"precision_x_item\": 0.017,\n      \"ordering_x_item\": 0.013,\n      \"hardware_x_item\": 0.019,\n      \"separability_ratio\": 0.035,\n      \"gpu1_gpu2_accuracy_correlation\": 0.9987,\n      \"max_accuracy_difference_any_condition\": 0.018,\n      \"mean_accuracy_difference\": 0.004,\n      \"g_current_practice\": 0.33,\n      \"g_full_design\": 0.81\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Separability Test — Direct vs Item-Conditional Interactions\",\n        \"columns\": [\n          \"Interaction Type\",\n          \"Components\",\n          \"Total % Variance\",\n          \"Interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Direct Infra×Method\",\n            \"hw×prompt, hw×temp, hw×seed, hw×ord, prec×prompt, prec×temp, prec×seed, prec×ord\",\n            0.5,\n            \"Negligible — separability holds at aggregate\"\n          ],\n          [\n            \"Infra×Item\",\n            \"hw×item, prec×item\",\n            3.6,\n            \"Small but non-zero — hardware/precision effects are item-conditional\"\n          ],\n          [\n            \"Method×Item\",\n            \"prompt×item, temp×item, seed×item, ord×item\",\n            15.5,\n            \"Substantial — methodology effects are strongly item-conditional\"\n          ],\n          [\n            \"Item Main\",\n            \"item_id\",\n            56.1,\n            \"Dominant — item selection is the primary variance source\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 6: Hardware Agreement Matrix (per-model mean accuracy)\",\n        \"columns\": [\n          \"Model\",\n          \"GPU1\",\n          \"GPU2\",\n          \"Difference\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            0.671,\n            0.668,\n            0.003\n          ],\n          [\n            \"Llama-3.1-8B\",\n            0.654,\n            0.65,\n            0.004\n          ],\n          [\n            \"Gemma-2-9B-IT\",\n            0.689,\n            0.684,\n            0.005\n          ],\n          [\n            \"Mistral-7B-v0.3\",\n            0.638,\n            0.634,\n            0.004\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Separability成立：direct infra×method交互总和0.5%，远低于1%阈值。但不是trivial null result—— item-conditional interactions（14.2%）提供了nuanced interpretation：infrastructure和methodology 不是完全独立的，而是通过item difficulty间接耦合。这比simple \\\"separable/not separable\\\"更有价值， 因为它解释了为什么isolated-factor studies的结论在某些items上不泛化。 这同时支撑了Claim 2的两半：\\\"empirical license for isolated-factor studies\\\"（direct <0.5%） 和 \\\"conclusions are conditional on item selection\\\"（item-conditional 14.2%）。\\n\\n\\nHardware主效应0.6%反映两块GPU的微架构差异（不同SM count、memory bandwidth、kernel scheduling）， 但这些差异是系统性的（固定偏移），不是随机的，所以主效应很小。hardware×item交互1.9%比hardware主效应大， 因为特定items（如需要长sequence generation的items）在不同GPU上因kernel tiling差异产生不同的numerical path， 但这只影响边界case items。所有direct infra×method交互加总仅0.5%，因为infrastructure层（hardware type, precision） 和methodology层（prompt, seed, temperature, ordering）作用于不同的computation stages： precision/hardware影响numerical computation，prompt/seed/temperature影响token sampling， 两者的交叉点（sampling受precision影响的程度）在logit空间中被softmax压缩到negligible水平。 Item-conditional interactions总和14.2%远大于direct interactions 0.5%，验证了Claim 2的nuanced story： separability在aggregate成立，但两层都通过item difficulty调节其效应。 GPU间accuracy correlation 0.9987说明hardware几乎不改变model ranking，只在individual item level引入微小噪声。\\n\"\n  },\n  {\n    \"name\": \"D-study reproducibility budget projections\",\n    \"description\": \"基于exp-001/002/003的合并variance component estimates，计算不同facet allocation下的G系数。 生成practitioner-facing budget tables和projection curves。纯计算，无GPU开销。\\n\",\n    \"results\": {\n      \"g_1prompt_1seed_200items_mmlu\": 0.34,\n      \"g_1prompt_1seed_200items_gsm8k\": 0.29,\n      \"g_1prompt_1seed_200items_arc\": 0.32,\n      \"g_1prompt_1seed_200items_hellaswag\": 0.36,\n      \"g_1prompt_1seed_600items_mmlu\": 0.71,\n      \"g_1prompt_1seed_1000items_mmlu\": 0.82,\n      \"g_1prompt_1seed_2000items_mmlu\": 0.9,\n      \"g_3prompt_1seed_200items_mmlu\": 0.42,\n      \"g_6prompt_1seed_200items_mmlu\": 0.49,\n      \"g_12prompt_1seed_200items_mmlu\": 0.54,\n      \"g_1prompt_3seed_200items_mmlu\": 0.36,\n      \"g_1prompt_6seed_200items_mmlu\": 0.37,\n      \"optimal_g90_items\": 600,\n      \"optimal_g90_prompts\": 3,\n      \"optimal_g90_seeds\": 2,\n      \"optimal_g90_total_conditions\": 6,\n      \"optimal_g90_total_evaluations\": 3600,\n      \"optimal_g95_items\": 1200,\n      \"optimal_g95_prompts\": 4,\n      \"optimal_g95_seeds\": 3,\n      \"optimal_g95_total_conditions\": 12,\n      \"optimal_g95_total_evaluations\": 14400,\n      \"marginal_g_per_100_items\": 0.038,\n      \"marginal_g_per_prompt\": 0.025,\n      \"marginal_g_per_seed\": 0.005,\n      \"items_vs_prompts_effectiveness_ratio\": 10.2,\n      \"items_vs_seeds_effectiveness_ratio\": 51.0,\n      \"gsm8k_optimal_g90_items\": 800,\n      \"gsm8k_optimal_g90_prompts\": 3,\n      \"gsm8k_optimal_g90_seeds\": 2,\n      \"arc_optimal_g90_items\": 650,\n      \"hellaswag_optimal_g90_items\": 550\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Reproducibility Budget — MMLU (Items × Prompts × Seeds → G coefficient)\",\n        \"columns\": [\n          \"Items\",\n          \"Prompts\",\n          \"Seeds\",\n          \"Total Evals\",\n          \"G coeff\",\n          \"Δ vs Current\"\n        ],\n        \"rows\": [\n          [\n            200,\n            1,\n            1,\n            200,\n            0.34,\n            \"baseline\"\n          ],\n          [\n            200,\n            3,\n            1,\n            600,\n            0.42,\n            \"+0.08\"\n          ],\n          [\n            200,\n            6,\n            1,\n            1200,\n            0.49,\n            \"+0.15\"\n          ],\n          [\n            200,\n            6,\n            6,\n            7200,\n            0.54,\n            \"+0.20\"\n          ],\n          [\n            600,\n            1,\n            1,\n            600,\n            0.71,\n            \"+0.37\"\n          ],\n          [\n            600,\n            3,\n            1,\n            1800,\n            0.82,\n            \"+0.48\"\n          ],\n          [\n            600,\n            3,\n            2,\n            3600,\n            0.9,\n            \"+0.56\"\n          ],\n          [\n            1000,\n            3,\n            2,\n            6000,\n            0.93,\n            \"+0.59\"\n          ],\n          [\n            1200,\n            4,\n            3,\n            14400,\n            0.95,\n            \"+0.61\"\n          ],\n          [\n            2000,\n            4,\n            3,\n            24000,\n            0.97,\n            \"+0.63\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Table 8: Cross-Benchmark Minimum Budget for G≥0.90\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Items\",\n          \"Prompts\",\n          \"Seeds\",\n          \"Total Evals\",\n          \"Cost Factor vs Current\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            600,\n            3,\n            2,\n            3600,\n            \"18×\"\n          ],\n          [\n            \"GSM8K\",\n            800,\n            3,\n            2,\n            4800,\n            \"24×\"\n          ],\n          [\n            \"ARC-Challenge\",\n            650,\n            3,\n            2,\n            3900,\n            \"19.5×\"\n          ],\n          [\n            \"HellaSwag\",\n            550,\n            3,\n            2,\n            3300,\n            \"16.5×\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 3的核心表格。Headline数字：\\\"tripling items is 10× more effective than tripling prompts\\\" 直接来自marginal effectiveness ratio 10.2:1。当前practice G<0.40的发现具有强policy implication—— 意味着现有leaderboard结果的measurement reliability低于社会科学中最低标准。 600 items + 3 prompts + 2 seeds的\\\"recommended minimum\\\"在计算成本上仅为full factorial的一小部分， 是actionable的建议。跨benchmark budget差异（550-800 items for G≥0.90）提供task-specific guidance。\\n\\n\\nG系数由universe score variance与observed score variance的比值决定。因为item_id占总方差>50%， 增加item采样直接压缩最大的variance component，G提升最快。具体地，G ≈ σ²(τ) / [σ²(τ) + σ²(δ)/n_facets]， 当item_id是σ²(δ)的主要贡献者时，增加n_items的marginal return远超增加n_prompts或n_seeds。 数值上，从200到600 items（3×）使G从0.34升至0.71，而从1到3 prompts（3×）仅从0.34升至0.42。 这是因为prompt variance（含prompt×item）共计~7%，而item variance 58%。 Seed几乎无效（G从0.34到0.37 at 6 seeds），因为seed的总方差贡献<3%（主要通过seed×item）。 G≥0.90需要~600 items + 3 prompts + 2 seeds = 3,600 evaluations。 当前标准practice（1 prompt, 1 seed, 200 items）的G < 0.40意味着evaluation结果的reliability 低于社会科学中\\\"不可接受\\\"的阈值（通常G≥0.80）。 GSM8K需要更多items（800 vs 600）达到G≥0.90，因为其residual更大（CoT随机性）， 需要更多items来平均掉item-level noise。\\n\"\n  },\n  {\n    \"name\": \"14B model extension\",\n    \"description\": \"Qwen3-14B和DeepSeek-R1-Distill-14B × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。每模型 2×6×6×3×4×200=172,800记录。\\n\",\n    \"results\": {\n      \"qwen3_14b_accuracy\": 0.728,\n      \"deepseek_r1_14b_accuracy\": 0.714,\n      \"qwen3_14b_item_id\": 0.574,\n      \"deepseek_r1_14b_item_id\": 0.538,\n      \"qwen3_14b_residual\": 0.162,\n      \"deepseek_r1_14b_residual\": 0.198,\n      \"deepseek_r1_14b_temperature_x_item\": 0.082,\n      \"scale_effect_on_item_id\": \"within 8B model range\",\n      \"item_id_rank1_both_models\": true,\n      \"variance_pattern_consistent_with_8b\": true,\n      \"precision_main_effect_14b\": 0.002\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: 14B vs 8B Variance Pattern Comparison\",\n        \"columns\": [\n          \"Component\",\n          \"8B Mean\",\n          \"8B Range\",\n          \"Qwen3-14B\",\n          \"DS-R1-14B\"\n        ],\n        \"rows\": [\n          [\n            \"item_id\",\n            58.4,\n            \"54.7–62.0\",\n            57.4,\n            53.8\n          ],\n          [\n            \"residual\",\n            16.8,\n            \"14.9–18.5\",\n            16.2,\n            19.8\n          ],\n          [\n            \"temp×item\",\n            5.8,\n            \"4.6–7.0\",\n            5.3,\n            8.2\n          ],\n          [\n            \"prompt×item\",\n            6.1,\n            \"4.7–7.5\",\n            5.8,\n            5.4\n          ],\n          [\n            \"precision\",\n            0.3,\n            \"0.1–0.5\",\n            0.2,\n            0.2\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scale invariance确认：item dominance不是小模型artifacts。DeepSeek-R1-Distill的slightly不同的profile （更高residual, 更高temp×item）提供了architecture effect的初步evidence， 但不改变core claim。这是P1实验，为paper增加robustness但非必需。\\n\\n\\n14B模型的overall accuracy更高，但item difficulty的variance structure不会因scale改变—— easy items仍然easy，hard items仍然hard。Item_id占比略低于8B平均值（~55-57% vs ~58%）， 因为14B模型在medium-difficulty items上表现更一致（ceiling effect压缩了item variance的上端）， 但差异不大。DeepSeek-R1-Distill的reasoning-distilled特性使其在CoT-heavy items上产生更多 temperature×item交互（类似GSM8K的pattern），residual也略高，因为distillation引入的implicit CoT 增加了generation-level stochasticity。关键是item_id在两个14B模型上仍为rank-1， 确认pattern不随model scale改变。precision主效应在14B上同样negligible（0.2%）， 因为confound fix的原理（统一engine path）与model size无关。\\n\"\n  },\n  {\n    \"name\": \"Fine-tuning G-study\",\n    \"description\": \"RoBERTa-large在SST-2/MNLI/RTE/COPA上fine-tuning。6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728 total。\\n\",\n    \"results\": {\n      \"sst2_accuracy_mean\": 0.948,\n      \"sst2_item_id\": 0.412,\n      \"sst2_seed\": 0.087,\n      \"sst2_learning_rate\": 0.063,\n      \"sst2_data_shuffle\": 0.042,\n      \"sst2_seed_x_item\": 0.098,\n      \"sst2_lr_x_item\": 0.074,\n      \"sst2_residual\": 0.131,\n      \"sst2_gpu\": 0.003,\n      \"sst2_precision\": 0.002,\n      \"mnli_accuracy_mean\": 0.876,\n      \"mnli_item_id\": 0.445,\n      \"mnli_seed\": 0.072,\n      \"mnli_learning_rate\": 0.081,\n      \"mnli_data_shuffle\": 0.038,\n      \"mnli_seed_x_item\": 0.091,\n      \"mnli_residual\": 0.142,\n      \"rte_accuracy_mean\": 0.743,\n      \"rte_item_id\": 0.368,\n      \"rte_seed\": 0.124,\n      \"rte_learning_rate\": 0.098,\n      \"rte_data_shuffle\": 0.067,\n      \"rte_seed_x_item\": 0.112,\n      \"rte_residual\": 0.158,\n      \"copa_accuracy_mean\": 0.682,\n      \"copa_item_id\": 0.382,\n      \"copa_seed\": 0.118,\n      \"copa_learning_rate\": 0.091,\n      \"copa_residual\": 0.167,\n      \"item_id_rank1_all_tasks\": true,\n      \"seed_more_important_than_inference\": true,\n      \"infra_effects_negligible\": true,\n      \"fine_tuning_g_current_practice\": 0.28\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Fine-tuning vs Inference Variance Hierarchy\",\n        \"columns\": [\n          \"Rank\",\n          \"Inference (MMLU)\",\n          \"Fine-tuning (SST-2)\"\n        ],\n        \"rows\": [\n          [\n            1,\n            \"item_id (58.4%)\",\n            \"item_id (41.2%)\"\n          ],\n          [\n            2,\n            \"residual (16.8%)\",\n            \"residual (13.1%)\"\n          ],\n          [\n            3,\n            \"prompt×item (6.1%)\",\n            \"seed×item (9.8%)\"\n          ],\n          [\n            4,\n            \"temp×item (5.8%)\",\n            \"seed (8.7%)\"\n          ],\n          [\n            5,\n            \"seed×item (2.9%)\",\n            \"lr×item (7.4%)\"\n          ],\n          [\n            6,\n            \"precision×item (1.8%)\",\n            \"lr (6.3%)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Fine-tuning G-study将paper从\\\"inference evaluation reproducibility\\\"扩展到\\\"ML reproducibility broadly\\\"。 核心takeaway：item dominance是跨paradigm的（inference和fine-tuning），但second-tier factors不同。 这是P1实验，为paper增加generality但AAAI投稿时可作为supplementary。\\n\\n\\nFine-tuning与inference的关键区别：training seed和learning rate成为substantial variance sources （combined 10-22%），因为它们影响optimization trajectory，不仅仅是sampling randomness。 但item_id仍然是rank-1（37-45%），因为NLU tasks的item difficulty gradient—— 从\\\"I love this movie\\\"(trivially positive)到需要subtle pragmatic inference的examples—— 在所有training configurations下都产生consistent accuracy variation。 RTE的item_id最低（36.8%），因为小数据集（2.5K training examples）使fine-tuning对seed更敏感， seed主效应膨胀到12.4%。这为paper提供了\\\"inference vs fine-tuning\\\"的对比dimension： 两者都是item-dominant，但fine-tuning中training hyperparameters（seed, LR）取代了 inference中的generation parameters（temperature, prompt）成为第二梯队的variance sources。 GPU和precision主效应在fine-tuning中同样negligible（<0.5%），因为RoBERTa-large 对numerical precision不敏感（unlike large generative models的autoregressive error accumulation）。\\n\"\n  },\n  {\n    \"name\": \"LayerCast precision study\",\n    \"description\": \"在MMLU上测试LayerCast（FP16 storage + FP32 compute）作为额外precision condition。 4 models × 1 precision mode × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 items = 172,800记录。\\n\",\n    \"results\": {\n      \"layercast_accuracy_mean\": 0.67,\n      \"layercast_vs_fp32_accuracy_diff\": 0.004,\n      \"layercast_vs_bf16_accuracy_diff\": -0.001,\n      \"layercast_item_agreement_with_fp32\": 0.9991,\n      \"layercast_item_agreement_with_bf16\": 0.9994,\n      \"layercast_added_variance_to_precision\": 0.0004,\n      \"layercast_throughput_vs_fp32\": 1.38,\n      \"layercast_throughput_vs_bf16\": 0.91,\n      \"layercast_precision_x_item_contribution\": 0.009\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Precision Mode Comparison\",\n        \"columns\": [\n          \"Mode\",\n          \"Accuracy\",\n          \"item Agreement w/ FP32\",\n          \"Throughput (tokens/s)\",\n          \"VRAM (GB)\"\n        ],\n        \"rows\": [\n          [\n            \"FP32\",\n            0.666,\n            1.0,\n            1820,\n            31.2\n          ],\n          [\n            \"BF16\",\n            0.671,\n            0.9985,\n            2760,\n            15.8\n          ],\n          [\n            \"FP16\",\n            0.669,\n            0.9982,\n            2810,\n            15.6\n          ],\n          [\n            \"LayerCast\",\n            0.67,\n            0.9991,\n            2510,\n            16.1\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"P2实验。LayerCast结果进一步support precision不是major concern（在engine confound fix后）。 可作为paper中\\\"practical recommendation\\\"段落的一条：对于追求最高reproducibility的场景， LayerCast提供了memory-efficient的FP32-equivalent选项。\\n\\n\\nLayerCast在存储时用FP16减少memory footprint，在compute时cast to FP32， 因此其numerical behavior几乎等同于纯FP32（computation path一致）， accuracy差异仅来自storage时的precision loss（FP16 mantissa 10 bits vs FP32 23 bits）， 这对大部分weights来说negligible（在训练时weights就是从FP16/BF16来的）。 与BF16的差异更小（0.1pp），因为BF16的dynamic range与FP32一致（8-bit exponent）， 而FP16的range更窄但mantissa更宽，两者accuracy接近。 LayerCast对precision variance几乎没有增量贡献（0.04%），因为它本质上是FP32 compute的cheaper variant。 Throughput方面，LayerCast比FP32快38%（memory bandwidth节省），比BF16慢9%（需要cast操作）。 这个实验为paper提供了一个\\\"practical mitigation\\\"故事：如果practitioner担心precision影响， LayerCast以minimal overhead提供FP32-level behavior。\\n\"\n  },\n  {\n    \"name\": \"MATH benchmark extension\",\n    \"description\": \"4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings × 200 MATH items。 总记录 4×2×6×6×2×4×200=230,400。测试reasoning-heavy task的variance structure。\\n\",\n    \"results\": {\n      \"math_overall_accuracy\": 0.342,\n      \"math_item_id\": 0.421,\n      \"math_residual\": 0.248,\n      \"math_temperature_x_item\": 0.104,\n      \"math_prompt_x_item\": 0.068,\n      \"math_seed_x_item\": 0.052,\n      \"math_temperature\": 0.038,\n      \"math_prompt\": 0.021,\n      \"math_precision\": 0.002,\n      \"math_precision_x_item\": 0.008,\n      \"math_ordering_x_item\": 0.015,\n      \"math_g_current_practice\": 0.24,\n      \"math_item_id_rank1\": true,\n      \"math_optimal_g90_items\": 1100,\n      \"math_optimal_g90_prompts\": 4,\n      \"math_optimal_g90_seeds\": 3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 12: Full Cross-Benchmark Variance Summary (5 benchmarks)\",\n        \"columns\": [\n          \"Benchmark\",\n          \"Accuracy\",\n          \"item_id %\",\n          \"Residual %\",\n          \"Temp×Item %\",\n          \"G (current)\",\n          \"Items for G≥0.90\"\n        ],\n        \"rows\": [\n          [\n            \"MMLU\",\n            0.668,\n            58.4,\n            16.8,\n            5.8,\n            0.34,\n            600\n          ],\n          [\n            \"ARC-Challenge\",\n            0.597,\n            55.1,\n            18.2,\n            5.4,\n            0.32,\n            650\n          ],\n          [\n            \"HellaSwag\",\n            0.712,\n            52.7,\n            19.5,\n            6.2,\n            0.36,\n            550\n          ],\n          [\n            \"GSM8K\",\n            0.583,\n            48.7,\n            21.4,\n            8.9,\n            0.29,\n            800\n          ],\n          [\n            \"MATH\",\n            0.342,\n            42.1,\n            24.8,\n            10.4,\n            0.24,\n            1100\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"MATH提供了variance structure的\\\"stress test\\\"。Item_id在最extreme条件下仍为rank-1（42.1%）， 但task difficulty明显调节了variance decomposition的profile。5个benchmark展现了清晰的gradient： task difficulty ↑ → item_id share ↓, residual ↑, temperature×item ↑, G current practice ↓。 这个gradient本身是publishable finding：它量化了为什么reasoning benchmark的evaluation更不稳定， 并给出了task-specific的reproducibility budget。\\n\\nMATH是所有benchmark中最challenging的（accuracy ~34%），其item difficulty分布极端—— 从Level 1（algebra basics）到Level 5（competition math），跨越巨大的difficulty range。 Item_id仍为rank-1（42.1%）但低于MMLU，因为：(1) lower overall accuracy增加了random guessing的比例， 膨胀residual到24.8%；(2) MATH的CoT generation比GSM8K更长更复杂（多步proof-like reasoning）， 使temperature×item interaction达到10.4%——在高temperature下，长推理链的任何一步都可能diverge， 且这种sensitivity是item-specific的（Level 5 problems的长推理链比Level 1的短计算更sensitive）。 Temperature主效应也最高（3.8%），因为MATH的generation length使sampling temperature的cumulative effect更显著。 G current practice仅0.24——所有benchmark中最低——意味着MATH evaluation的reproducibility最差。 达到G≥0.90需要1100 items + 4 prompts + 3 seeds，是MMLU所需的~3倍evaluation budget。 这个发现有strong policy implication：reasoning benchmark的evaluation标准需要比classification benchmark更严格。\\n\"\n  }\n]",
      "numLines": 914,
      "startLine": 1,
      "totalLines": 914
    }
  },
  "sourceToolAssistantUUID": "074394ac-f93c-4673-8c0e-16c37f482e1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T22:24:06.837Z_

<details><summary>↩ Tool result · `toolu_01Pyr5WXPFVPN1MNFiNRmbw2`</summary>

```text
1	tier: best
2	narrative_guidance: '原始framing完全成立。float32 confound修复后precision主效应坍缩至噪声水平，反而成为方法论贡献（展示engine配置对variance
3	  attribution的系统性影响）。 Item dominance在所有benchmark上复现为最大单一方差源，4个模型一致。Separability在aggregate
4	  level成立（direct interaction <0.5%）， 但item-conditional interactions提供nuanced story。D-study
5	  budget表给出clear actionable guidance，headline数字"item selection >50%"直接可用。 AAAI投稿节奏正常，三条claim原封不动。
6	
7	  '
8	imagined_experiments:
9	- name: Full-scale precision study with confound fix
10	  plan_id: exp-001
11	  description: '4 models × 3 precisions (FP32/BF16/FP16) × 6 prompts × 6 seeds × 3
12	    temperatures × 4 orderings × 200 MMLU items, 全部使用vLLM V0 enforce_eager消除engine差异。总条件数
13	    4×3×6×6×3×4=5184 per item, 总记录 5184×200=1,036,800。
14	
15	    '
16	  expected_results:
17	    total_records: 1036800
18	    conditions_per_model: 1296
19	    overall_accuracy: 0.668
20	    accuracy_fp32: 0.666
21	    accuracy_bf16: 0.671
22	    accuracy_fp16: 0.669
23	    accuracy_spread_across_precisions: 0.005
24	    item_id: 0.584
25	    residual: 0.168
26	    prompt_template_x_item_id: 0.061
27	    temperature_x_item_id: 0.058
28	    seed_x_item_id: 0.029
29	    precision_x_item_id: 0.018
30	    ordering_x_item_id: 0.014
31	    prompt_template: 0.009
32	    temperature: 0.007
33	    ordering: 0.003
34	    precision: 0.003
35	    seed: 0.001
36	    models_with_item_id_rank1: 4
37	    item_id_range_across_models:
38	    - 0.52
39	    - 0.62
40	    qwen3_8b_item_id: 0.598
41	    llama31_8b_item_id: 0.571
42	    gemma2_9b_item_id: 0.62
43	    mistral_7b_item_id: 0.547
44	    precision_main_effect_before_fix_mvp: 0.0087
45	    precision_main_effect_after_fix: 0.003
46	    precision_x_item_id_before_fix_mvp: 0.0724
47	    precision_x_item_id_after_fix: 0.018
48	    fp32_bf16_accuracy_gap_before_fix: 0.085
49	    fp32_bf16_accuracy_gap_after_fix: 0.005
50	    g_current_practice_1p1s200i: 0.34
51	    g_6p6s200i: 0.72
52	    g_6p6s200i_3t4o: 0.78
53	  result_rationale: 'MVP中precision主效应0.87%和precision×item交互7.24%主要来自float32使用不同vLLM
54	    engine路径（非V0时触发不同kernel）， 导致FP32准确率系统性偏低5.7pp。统一V0 enforce_eager后，三种精度走同一compute
55	    path， FP32/BF16/FP16准确率差收敛至0.5pp以内（纯numerical noise水平）。precision主效应从0.87%降至~0.3%，
56	    precision×item从7.24%降至~1.8%。这些被释放的方差份额主要回流到residual和item_id， 使item_id维持在~58%（与MVP一致，因为item
57	    difficulty本身是真实信号，不受engine confound影响）。 4个模型均以item_id为rank-1组分，因为MMLU的item difficulty分布（从trivial到expert-level）
58	    在所有7-9B模型上产生类似的accuracy ceiling/floor效应。Gemma-2略高因其instruction-tuned特性 使其对easy
59	    items更稳定（floor更高），Mistral略低因其在部分domain上accuracy更平坦。 200 items（分层采样）比MVP的50 items提供更稳定的方差估计，置信区间收窄约50%。
60	
61	    '
62	  tables:
63	  - name: 'Table 1: Variance Component Estimates — MMLU 200 items, 4 models pooled'
64	    columns:
65	    - Component
66	    - '% Variance'
67	    - SE
68	    - 95% CI Lower
69	    - 95% CI Upper
70	    - MVP (50 items)
71	    rows:
72	    - - item_id
73	      - 58.4
74	      - 2.1
75	      - 54.3
76	      - 62.5
77	      - 58.4
78	    - - residual
79	      - 16.8
80	      - 0.9
81	      - 15.0
82	      - 18.6
83	      - 17.6
84	    - - prompt×item
85	      - 6.1
86	      - 0.7
87	      - 4.7
88	      - 7.5
89	      - 5.7
90	    - - temp×item
91	      - 5.8
92	      - 0.6
93	      - 4.6
94	      - 7.0
95	      - 6.9
96	    - - seed×item
97	      - 2.9
98	      - 0.4
99	      - 2.1
100	      - 3.7
101	      - 2.7
102	    - - precision×item
103	      - 1.8
104	      - 0.3
105	      - 1.2
106	      - 2.4
107	      - 7.2*
108	    - - ordering×item
109	      - 1.4
110	      - 0.3
111	      - 0.8
112	      - 2.0
113	      - —
114	    - - prompt
115	      - 0.9
116	      - 0.3
117	      - 0.3
118	      - 1.5
119	      - —
120	    - - temperature
121	      - 0.7
122	      - 0.2
123	      - 0.3
124	      - 1.1
125	      - —
126	    - - precision
127	      - 0.3
128	      - 0.1
129	      - 0.1
130	      - 0.5
131	      - 0.87*
132	    - - ordering
133	      - 0.3
134	      - 0.1
135	      - 0.1
136	      - 0.5
137	      - —
138	    - - seed
139	      - 0.1
140	      - 0.05
141	      - 0.0
142	      - 0.2
143	      - —
144	  - name: 'Table 2: Per-Model item_id Variance Share'
145	    columns:
146	    - Model
147	    - item_id %
148	    - Next Largest
149	    - Next %
150	    rows:
151	    - - Qwen3-8B
152	      - 59.8
153	      - residual
154	      - 16.2
155	    - - Llama-3.1-8B
156	      - 57.1
157	      - residual
158	      - 17.8
159	    - - Gemma-2-9B-IT
160	      - 62.0
161	      - residual
162	      - 14.9
163	    - - Mistral-7B-v0.3
164	      - 54.7
165	      - residual
166	      - 18.5
167	  figures_description:
168	  - 'Fig 1: Stacked-bar variance decomposition — MVP (confounded) vs exp-001 (fixed),
169	    side-by-side。左栏显示precision和precision×item的膨胀，右栏显示修复后两者坍缩，item_id占比不变。'
170	  - 'Fig 2: 4-panel per-model stacked bars，展示item_id始终为rank-1的cross-model consistency。'
171	  - 'Fig 3: FP32 vs BF16 accuracy scatter (per-item)，MVP中slope偏离1.0，exp-001中回归到~1.0。'
172	  analysis: '核心发现：engine confound修复后item dominance完全稳健，precision主效应从0.87%降至0.3%。 这同时验证了Claim
173	    1（item dominance）和提供了方法论贡献（engine配置对variance attribution的影响）。 4个模型一致性消除了"Qwen3特例"的concern。200
174	    items分层采样提供了足够的statistical power。 Ordering facet新增后占比很小（~1.7% total含interaction），说明item
175	    presentation order不是主要concern。
176	
177	    '
178	- name: Multi-benchmark replication
179	  plan_id: exp-002
180	  description: '4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures
181	    × 4 orderings × 200 items, 分别在GSM8K、ARC-Challenge、HellaSwag上运行。每benchmark总记录 4×2×6×6×2×4×200=230,400。
182	
183	    '
184	  expected_results:
185	    gsm8k_overall_accuracy: 0.583
186	    gsm8k_item_id: 0.487
187	    gsm8k_residual: 0.214
188	    gsm8k_temperature_x_item_id: 0.089
189	    gsm8k_prompt_x_item_id: 0.072
190	    gsm8k_seed_x_item_id: 0.041
191	    gsm8k_precision_x_item_id: 0.012
192	    gsm8k_ordering_x_item_id: 0.018
193	    gsm8k_temperature: 0.024
194	    gsm8k_prompt: 0.015
195	    gsm8k_precision: 0.002
196	    gsm8k_g_current_practice: 0.29
197	    arc_overall_accuracy: 0.597
198	    arc_item_id: 0.551
199	    arc_residual: 0.182
200	    arc_prompt_x_item_id: 0.068
201	    arc_temperature_x_item_id: 0.054
202	    arc_seed_x_item_id: 0.031
203	    arc_precision_x_item_id: 0.014
204	    arc_ordering_x_item_id: 0.016
205	    arc_prompt: 0.011
206	    arc_temperature: 0.008
207	    arc_precision: 0.002
208	    arc_g_current_practice: 0.32
209	    hellaswag_overall_accuracy: 0.712
210	    hellaswag_item_id: 0.527
211	    hellaswag_residual: 0.195
212	    hellaswag_prompt_x_item_id: 0.058
213	    hellaswag_temperature_x_item_id: 0.062
214	    hellaswag_seed_x_item_id: 0.033
215	    hellaswag_precision_x_item_id: 0.011
216	    hellaswag_ordering_x_item_id: 0.019
217	    hellaswag_prompt: 0.008
218	    hellaswag_temperature: 0.006
219	    hellaswag_precision: 0.001
220	    hellaswag_g_current_practice: 0.36
221	    benchmarks_with_item_id_rank1: 4
222	    item_id_range_across_benchmarks:
223	    - 0.487
224	    - 0.584
225	    cross_benchmark_replication_rate: 1.0
226	    models_showing_consistent_pattern: 4
227	  result_rationale: 'GSM8K的item_id占比略低于MMLU（48.7% vs 58.4%），因为数学推理任务引入更多chain-of-thought随机性，
228	    使residual和temperature×item交互膨胀。GSM8K中温度效应更大（temperature×item 8.9%）， 因为CoT生成路径对sampling
229	    temperature更敏感——同一道数学题在不同温度下可能走完全不同的推理链。 但item_id仍然是rank-1组分，因为GSM8K的difficulty
230	    gradient极陡（从单步算术到多步word problem）， 这种item-level variance在所有条件下都主导。ARC-Challenge的item_id（55.1%）接近MMLU，
231	    因为科学推理题的difficulty分布类似（从factual recall到multi-hop inference）。 HellaSwag的item_id（52.7%）也稳健，因为commonsense
232	    completion的item variance主要来自 distractor quality差异——有些items的wrong answers显而易见，有些几乎无法区分。
233	    所有benchmark上precision主效应均<0.3%，确认engine confound fix的泛化性。 4/4 benchmark的item_id
234	    rank-1复现率为100%，支撑"cross-benchmark replication rate = 1.0"。
235	
236	    '
237	  tables:
238	  - name: 'Table 3: Cross-Benchmark Variance Decomposition Summary'
239	    columns:
240	    - Benchmark
241	    - item_id %
242	    - Residual %
243	    - Item-Conditional Total %
244	    - Precision Main %
245	    - G (current)
246	    rows:
247	    - - MMLU
248	      - 58.4
249	      - 16.8
250	      - 16.1
251	      - 0.3
252	      - 0.34
253	    - - GSM8K
254	      - 48.7
255	      - 21.4
256	      - 23.2
257	      - 0.2
258	      - 0.29
259	    - - ARC-Challenge
260	      - 55.1
261	      - 18.2
262	      - 18.3
263	      - 0.2
264	      - 0.32
265	    - - HellaSwag
266	      - 52.7
267	      - 19.5
268	      - 18.3
269	      - 0.1
270	      - 0.36
271	  - name: 'Table 4: GSM8K Per-Model Breakdown'
272	    columns:
273	    - Model
274	    - item_id %
275	    - temp×item %
276	    - prompt×item %
277	    - residual %
278	    rows:
279	    - - Qwen3-8B
280	      - 51.2
281	      - 8.1
282	      - 6.8
283	      - 19.8
284	    - - Llama-3.1-8B
285	      - 47.3
286	      - 9.4
287	      - 7.6
288	      - 22.1
289	    - - Gemma-2-9B-IT
290	      - 50.8
291	      - 8.5
292	      - 6.9
293	      - 20.3
294	    - - Mistral-7B-v0.3
295	      - 43.4
296	      - 10.5
297	      - 8.3
298	      - 23.5
299	  figures_description:
300	  - 'Fig 4: 4-benchmark stacked-bar variance decomposition并排对比。item_id始终为最大色块，但GSM8K的residual和temperature×item色块明显更大。'
301	  - 'Fig 5: Heatmap — benchmark × model × component，展示pattern consistency。色块深浅表示variance
302	    share，item_id行始终最深。'
303	  analysis: 'Item dominance在4个benchmark上全部复现（range 48.7%-58.4%），但幅度因task type有系统性差异：
304	    generation-heavy tasks（GSM8K）因CoT随机性使residual膨胀，压缩item_id相对占比； classification-like
305	    tasks（MMLU, ARC）的item_id更高。这个gradient本身是有趣的发现， 可在Discussion中展开。关键是即使在"worst case"的GSM8K上，item_id仍是rank-1（48.7%
306	    > residual 21.4%）， headline claim成立。
307	
308	    '
309	- name: Multi-hardware G-study
310	  plan_id: exp-003
311	  description: '4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions
312	    (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。总记录
313	    4×2×2×6×6×3×4×200=691,200。 核心目标：量化hardware主效应和hardware×methodology交互。
314	
315	    '
316	  expected_results:
317	    total_records: 691200
318	    hardware_main_effect: 0.006
319	    hardware_x_precision: 0.002
320	    hardware_x_prompt: 0.001
321	    hardware_x_temperature: 0.001
322	    hardware_x_seed: 0.0005
323	    hardware_x_ordering: 0.0003
324	    hardware_x_item_id: 0.019
325	    precision_x_prompt: 0.0008
326	    precision_x_temperature: 0.0006
327	    precision_x_seed: 0.0003
328	    precision_x_ordering: 0.0002
329	    direct_infra_method_interaction_total: 0.005
330	    item_conditional_interactions_total: 0.142
331	    item_id: 0.561
332	    residual: 0.152
333	    prompt_x_item: 0.059
334	    temperature_x_item: 0.055
335	    seed_x_item: 0.028
336	    precision_x_item: 0.017
337	    ordering_x_item: 0.013
338	    hardware_x_item: 0.019
339	    separability_ratio: 0.035
340	    gpu1_gpu2_accuracy_correlation: 0.9987
341	    max_accuracy_difference_any_condition: 0.018
342	    mean_accuracy_difference: 0.004
343	    g_current_practice: 0.33
344	    g_full_design: 0.81
345	  result_rationale: 'Hardware主效应0.6%反映两块GPU的微架构差异（不同SM count、memory bandwidth、kernel
346	    scheduling）， 但这些差异是系统性的（固定偏移），不是随机的，所以主效应很小。hardware×item交互1.9%比hardware主效应大，
347	    因为特定items（如需要长sequence generation的items）在不同GPU上因kernel tiling差异产生不同的numerical
348	    path， 但这只影响边界case items。所有direct infra×method交互加总仅0.5%，因为infrastructure层（hardware
349	    type, precision） 和methodology层（prompt, seed, temperature, ordering）作用于不同的computation
350	    stages： precision/hardware影响numerical computation，prompt/seed/temperature影响token
351	    sampling， 两者的交叉点（sampling受precision影响的程度）在logit空间中被softmax压缩到negligible水平。 Item-conditional
352	    interactions总和14.2%远大于direct interactions 0.5%，验证了Claim 2的nuanced story： separability在aggregate成立，但两层都通过item
353	    difficulty调节其效应。 GPU间accuracy correlation 0.9987说明hardware几乎不改变model ranking，只在individual
354	    item level引入微小噪声。
355	
356	    '
357	  tables:
358	  - name: 'Table 5: Separability Test — Direct vs Item-Conditional Interactions'
359	    columns:
360	    - Interaction Type
361	    - Components
362	    - Total % Variance
363	    - Interpretation
364	    rows:
365	    - - Direct Infra×Method
366	      - hw×prompt, hw×temp, hw×seed, hw×ord, prec×prompt, prec×temp, prec×seed, prec×ord
367	      - 0.5
368	      - Negligible — separability holds at aggregate
369	    - - Infra×Item
370	      - hw×item, prec×item
371	      - 3.6
372	      - Small but non-zero — hardware/precision effects are item-conditional
373	    - - Method×Item
374	      - prompt×item, temp×item, seed×item, ord×item
375	      - 15.5
376	      - Substantial — methodology effects are strongly item-conditional
377	    - - Item Main
378	      - item_id
379	      - 56.1
380	      - Dominant — item selection is the primary variance source
381	  - name: 'Table 6: Hardware Agreement Matrix (per-model mean accuracy)'
382	    columns:
383	    - Model
384	    - GPU1
385	    - GPU2
386	    - Difference
387	    rows:
388	    - - Qwen3-8B
389	      - 0.671
390	      - 0.668
391	      - 0.003
392	    - - Llama-3.1-8B
393	      - 0.654
394	      - 0.65
395	      - 0.004
396	    - - Gemma-2-9B-IT
397	      - 0.689
398	      - 0.684
399	      - 0.005
400	    - - Mistral-7B-v0.3
401	      - 0.638
402	      - 0.634
403	      - 0.004
404	  figures_description:
405	  - 'Fig 6: Separability diagram — 两层圆（infra layer, method layer）通过item difficulty连接，直接交互箭头用虚线（<0.5%），item-conditional箭头用实线。'
406	  - 'Fig 7: GPU1 vs GPU2 per-item accuracy scatter，近乎perfect diagonal，少数outlier items标注。'
407	  analysis: 'Separability成立：direct infra×method交互总和0.5%，远低于1%阈值。但不是trivial null result——
408	    item-conditional interactions（14.2%）提供了nuanced interpretation：infrastructure和methodology
409	    不是完全独立的，而是通过item difficulty间接耦合。这比simple "separable/not separable"更有价值， 因为它解释了为什么isolated-factor
410	    studies的结论在某些items上不泛化。 这同时支撑了Claim 2的两半："empirical license for isolated-factor
411	    studies"（direct <0.5%） 和 "conclusions are conditional on item selection"（item-conditional
412	    14.2%）。
413	
414	    '
415	- name: D-study reproducibility budget projections
416	  plan_id: exp-004
417	  description: '基于exp-001/002/003的合并variance component estimates，计算不同facet allocation下的G系数。
418	    生成practitioner-facing budget tables和projection curves。纯计算，无GPU开销。
419	
420	    '
421	  expected_results:
422	    g_1prompt_1seed_200items_mmlu: 0.34
423	    g_1prompt_1seed_200items_gsm8k: 0.29
424	    g_1prompt_1seed_200items_arc: 0.32
425	    g_1prompt_1seed_200items_hellaswag: 0.36
426	    g_1prompt_1seed_600items_mmlu: 0.71
427	    g_1prompt_1seed_1000items_mmlu: 0.82
428	    g_1prompt_1seed_2000items_mmlu: 0.9
429	    g_3prompt_1seed_200items_mmlu: 0.42
430	    g_6prompt_1seed_200items_mmlu: 0.49
431	    g_12prompt_1seed_200items_mmlu: 0.54
432	    g_1prompt_3seed_200items_mmlu: 0.36
433	    g_1prompt_6seed_200items_mmlu: 0.37
434	    optimal_g90_items: 600
435	    optimal_g90_prompts: 3
436	    optimal_g90_seeds: 2
437	    optimal_g90_total_conditions: 6
438	    optimal_g90_total_evaluations: 3600
439	    optimal_g95_items: 1200
440	    optimal_g95_prompts: 4
441	    optimal_g95_seeds: 3
442	    optimal_g95_total_conditions: 12
443	    optimal_g95_total_evaluations: 14400
444	    marginal_g_per_100_items: 0.038
445	    marginal_g_per_prompt: 0.025
446	    marginal_g_per_seed: 0.005
447	    items_vs_prompts_effectiveness_ratio: 10.2
448	    items_vs_seeds_effectiveness_ratio: 51.0
449	    gsm8k_optimal_g90_items: 800
450	    gsm8k_optimal_g90_prompts: 3
451	    gsm8k_optimal_g90_seeds: 2
452	    arc_optimal_g90_items: 650
453	    hellaswag_optimal_g90_items: 550
454	  result_rationale: 'G系数由universe score variance与observed score variance的比值决定。因为item_id占总方差>50%，
455	    增加item采样直接压缩最大的variance component，G提升最快。具体地，G ≈ σ²(τ) / [σ²(τ) + σ²(δ)/n_facets]，
456	    当item_id是σ²(δ)的主要贡献者时，增加n_items的marginal return远超增加n_prompts或n_seeds。 数值上，从200到600
457	    items（3×）使G从0.34升至0.71，而从1到3 prompts（3×）仅从0.34升至0.42。 这是因为prompt variance（含prompt×item）共计~7%，而item
458	    variance 58%。 Seed几乎无效（G从0.34到0.37 at 6 seeds），因为seed的总方差贡献<3%（主要通过seed×item）。
459	    G≥0.90需要~600 items + 3 prompts + 2 seeds = 3,600 evaluations。 当前标准practice（1 prompt,
460	    1 seed, 200 items）的G < 0.40意味着evaluation结果的reliability 低于社会科学中"不可接受"的阈值（通常G≥0.80）。
461	    GSM8K需要更多items（800 vs 600）达到G≥0.90，因为其residual更大（CoT随机性）， 需要更多items来平均掉item-level
462	    noise。
463	
464	    '
465	  tables:
466	  - name: 'Table 7: Reproducibility Budget — MMLU (Items × Prompts × Seeds → G coefficient)'
467	    columns:
468	    - Items
469	    - Prompts
470	    - Seeds
471	    - Total Evals
472	    - G coeff
473	    - Δ vs Current
474	    rows:
475	    - - 200
476	      - 1
477	      - 1
478	      - 200
479	      - 0.34
480	      - baseline
481	    - - 200
482	      - 3
483	      - 1
484	      - 600
485	      - 0.42
486	      - '+0.08'
487	    - - 200
488	      - 6
489	      - 1
490	      - 1200
491	      - 0.49
492	      - '+0.15'
493	    - - 200
494	      - 6
495	      - 6
496	      - 7200
497	      - 0.54
498	      - '+0.20'
499	    - - 600
500	      - 1
501	      - 1
502	      - 600
503	      - 0.71
504	      - '+0.37'
505	    - - 600
506	      - 3
507	      - 1
508	      - 1800
509	      - 0.82
510	      - '+0.48'
511	    - - 600
512	      - 3
513	      - 2
514	      - 3600
515	      - 0.9
516	      - '+0.56'
517	    - - 1000
518	      - 3
519	      - 2
520	      - 6000
521	      - 0.93
522	      - '+0.59'
523	    - - 1200
524	      - 4
525	      - 3
526	      - 14400
527	      - 0.95
528	      - '+0.61'
529	    - - 2000
530	      - 4
531	      - 3
532	      - 24000
533	      - 0.97
534	      - '+0.63'
535	  - name: 'Table 8: Cross-Benchmark Minimum Budget for G≥0.90'
536	    columns:
537	    - Benchmark
538	    - Items
539	    - Prompts
540	    - Seeds
541	    - Total Evals
542	    - Cost Factor vs Current
543	    rows:
544	    - - MMLU
545	      - 600
546	      - 3
547	      - 2
548	      - 3600
549	      - 18×
550	    - - GSM8K
551	      - 800
552	      - 3
553	      - 2
554	      - 4800
555	      - 24×
556	    - - ARC-Challenge
557	      - 650
558	      - 3
559	      - 2
560	      - 3900
561	      - 19.5×
562	    - - HellaSwag
563	      - 550
564	      - 3
565	      - 2
566	      - 3300
567	      - 16.5×
568	  figures_description:
569	  - 'Fig 8: D-study projection curves — G coefficient vs total evaluations，三条线分别对应
570	    scale items only / scale prompts only / scale seeds only。Items线陡峭上升，prompts线平缓，seeds线几乎flat。'
571	  - 'Fig 9: Iso-G contour plot（items × prompts平面，G值等高线），展示最优allocation路径沿items轴延伸。'
572	  - 'Fig 10: 4-benchmark overlay projection curves，展示GSM8K需要更多evaluations但pattern一致。'
573	  analysis: 'Claim 3的核心表格。Headline数字："tripling items is 10× more effective than tripling
574	    prompts" 直接来自marginal effectiveness ratio 10.2:1。当前practice G<0.40的发现具有强policy
575	    implication—— 意味着现有leaderboard结果的measurement reliability低于社会科学中最低标准。 600 items
576	    + 3 prompts + 2 seeds的"recommended minimum"在计算成本上仅为full factorial的一小部分， 是actionable的建议。跨benchmark
577	    budget差异（550-800 items for G≥0.90）提供task-specific guidance。
578	
579	    '
580	- name: 14B model extension
581	  plan_id: exp-005
582	  description: 'Qwen3-14B和DeepSeek-R1-Distill-14B × 2 precisions (BF16/FP16) × 6 prompts
583	    × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。每模型 2×6×6×3×4×200=172,800记录。
584	
585	    '
586	  expected_results:
587	    qwen3_14b_accuracy: 0.728
588	    deepseek_r1_14b_accuracy: 0.714
589	    qwen3_14b_item_id: 0.574
590	    deepseek_r1_14b_item_id: 0.538
591	    qwen3_14b_residual: 0.162
592	    deepseek_r1_14b_residual: 0.198
593	    deepseek_r1_14b_temperature_x_item: 0.082
594	    scale_effect_on_item_id: within 8B model range
595	    item_id_rank1_both_models: true
596	    variance_pattern_consistent_with_8b: true
597	    precision_main_effect_14b: 0.002
598	  result_rationale: '14B模型的overall accuracy更高，但item difficulty的variance structure不会因scale改变——
599	    easy items仍然easy，hard items仍然hard。Item_id占比略低于8B平均值（~55-57% vs ~58%）， 因为14B模型在medium-difficulty
600	    items上表现更一致（ceiling effect压缩了item variance的上端）， 但差异不大。DeepSeek-R1-Distill的reasoning-distilled特性使其在CoT-heavy
601	    items上产生更多 temperature×item交互（类似GSM8K的pattern），residual也略高，因为distillation引入的implicit
602	    CoT 增加了generation-level stochasticity。关键是item_id在两个14B模型上仍为rank-1， 确认pattern不随model
603	    scale改变。precision主效应在14B上同样negligible（0.2%）， 因为confound fix的原理（统一engine path）与model
604	    size无关。
605	
606	    '
607	  tables:
608	  - name: 'Table 9: 14B vs 8B Variance Pattern Comparison'
609	    columns:
610	    - Component
611	    - 8B Mean
612	    - 8B Range
613	    - Qwen3-14B
614	    - DS-R1-14B
615	    rows:
616	    - - item_id
617	      - 58.4
618	      - 54.7–62.0
619	      - 57.4
620	      - 53.8
621	    - - residual
622	      - 16.8
623	      - 14.9–18.5
624	      - 16.2
625	      - 19.8
626	    - - temp×item
627	      - 5.8
628	      - 4.6–7.0
629	      - 5.3
630	      - 8.2
631	    - - prompt×item
632	      - 6.1
633	      - 4.7–7.5
634	      - 5.8
635	      - 5.4
636	    - - precision
637	      - 0.3
638	      - 0.1–0.5
639	      - 0.2
640	      - 0.2
641	  figures_description:
642	  - 'Fig 11: 6-model panel（4×8B + 2×14B）stacked bars，展示scale不改变variance hierarchy。'
643	  analysis: 'Scale invariance确认：item dominance不是小模型artifacts。DeepSeek-R1-Distill的slightly不同的profile
644	    （更高residual, 更高temp×item）提供了architecture effect的初步evidence， 但不改变core claim。这是P1实验，为paper增加robustness但非必需。
645	
646	    '
647	- name: Fine-tuning G-study
648	  plan_id: exp-006
649	  description: 'RoBERTa-large在SST-2/MNLI/RTE/COPA上fine-tuning。6 seeds × 3 learning
650	    rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728
651	    total。
652	
653	    '
654	  expected_results:
655	    sst2_accuracy_mean: 0.948
656	    sst2_item_id: 0.412
657	    sst2_seed: 0.087
658	    sst2_learning_rate: 0.063
659	    sst2_data_shuffle: 0.042
660	    sst2_seed_x_item: 0.098
661	    sst2_lr_x_item: 0.074
662	    sst2_residual: 0.131
663	    sst2_gpu: 0.003
664	    sst2_precision: 0.002
665	    mnli_accuracy_mean: 0.876
666	    mnli_item_id: 0.445
667	    mnli_seed: 0.072
668	    mnli_learning_rate: 0.081
669	    mnli_data_shuffle: 0.038
670	    mnli_seed_x_item: 0.091
671	    mnli_residual: 0.142
672	    rte_accuracy_mean: 0.743
673	    rte_item_id: 0.368
674	    rte_seed: 0.124
675	    rte_learning_rate: 0.098
676	    rte_data_shuffle: 0.067
677	    rte_seed_x_item: 0.112
678	    rte_residual: 0.158
679	    copa_accuracy_mean: 0.682
680	    copa_item_id: 0.382
681	    copa_seed: 0.118
682	    copa_learning_rate: 0.091
683	    copa_residual: 0.167
684	    item_id_rank1_all_tasks: true
685	    seed_more_important_than_inference: true
686	    infra_effects_negligible: true
687	    fine_tuning_g_current_practice: 0.28
688	  result_rationale: 'Fine-tuning与inference的关键区别：training seed和learning rate成为substantial
689	    variance sources （combined 10-22%），因为它们影响optimization trajectory，不仅仅是sampling
690	    randomness。 但item_id仍然是rank-1（37-45%），因为NLU tasks的item difficulty gradient—— 从"I
691	    love this movie"(trivially positive)到需要subtle pragmatic inference的examples—— 在所有training
692	    configurations下都产生consistent accuracy variation。 RTE的item_id最低（36.8%），因为小数据集（2.5K
693	    training examples）使fine-tuning对seed更敏感， seed主效应膨胀到12.4%。这为paper提供了"inference vs
694	    fine-tuning"的对比dimension： 两者都是item-dominant，但fine-tuning中training hyperparameters（seed,
695	    LR）取代了 inference中的generation parameters（temperature, prompt）成为第二梯队的variance sources。
696	    GPU和precision主效应在fine-tuning中同样negligible（<0.5%），因为RoBERTa-large 对numerical precision不敏感（unlike
697	    large generative models的autoregressive error accumulation）。
698	
699	    '
700	  tables:
701	  - name: 'Table 10: Fine-tuning vs Inference Variance Hierarchy'
702	    columns:
703	    - Rank
704	    - Inference (MMLU)
705	    - Fine-tuning (SST-2)
706	    rows:
707	    - - 1
708	      - item_id (58.4%)
709	      - item_id (41.2%)
710	    - - 2
711	      - residual (16.8%)
712	      - residual (13.1%)
713	    - - 3
714	      - prompt×item (6.1%)
715	      - seed×item (9.8%)
716	    - - 4
717	      - temp×item (5.8%)
718	      - seed (8.7%)
719	    - - 5
720	      - seed×item (2.9%)
721	      - lr×item (7.4%)
722	    - - 6
723	      - precision×item (1.8%)
724	      - lr (6.3%)
725	  figures_description:
726	  - 'Fig 12: Inference vs Fine-tuning stacked bars并排，展示item_id在两个paradigm中均为rank-1但fine-tuning中seed/LR更prominent。'
727	  - 'Fig 13: 4-task fine-tuning panel，展示dataset size对variance structure的调节效应（RTE seed最大）。'
728	  analysis: 'Fine-tuning G-study将paper从"inference evaluation reproducibility"扩展到"ML
729	    reproducibility broadly"。 核心takeaway：item dominance是跨paradigm的（inference和fine-tuning），但second-tier
730	    factors不同。 这是P1实验，为paper增加generality但AAAI投稿时可作为supplementary。
731	
732	    '
733	- name: LayerCast precision study
734	  plan_id: exp-007
735	  description: '在MMLU上测试LayerCast（FP16 storage + FP32 compute）作为额外precision condition。
736	    4 models × 1 precision mode × 6 prompts × 6 seeds × 3 temperatures × 4 orderings
737	    × 200 items = 172,800记录。
738	
739	    '
740	  expected_results:
741	    layercast_accuracy_mean: 0.67
742	    layercast_vs_fp32_accuracy_diff: 0.004
743	    layercast_vs_bf16_accuracy_diff: -0.001
744	    layercast_item_agreement_with_fp32: 0.9991
745	    layercast_item_agreement_with_bf16: 0.9994
746	    layercast_added_variance_to_precision: 0.0004
747	    layercast_throughput_vs_fp32: 1.38
748	    layercast_throughput_vs_bf16: 0.91
749	    layercast_precision_x_item_contribution: 0.009
750	  result_rationale: 'LayerCast在存储时用FP16减少memory footprint，在compute时cast to FP32， 因此其numerical
751	    behavior几乎等同于纯FP32（computation path一致）， accuracy差异仅来自storage时的precision loss（FP16
752	    mantissa 10 bits vs FP32 23 bits）， 这对大部分weights来说negligible（在训练时weights就是从FP16/BF16来的）。
753	    与BF16的差异更小（0.1pp），因为BF16的dynamic range与FP32一致（8-bit exponent）， 而FP16的range更窄但mantissa更宽，两者accuracy接近。
754	    LayerCast对precision variance几乎没有增量贡献（0.04%），因为它本质上是FP32 compute的cheaper variant。
755	    Throughput方面，LayerCast比FP32快38%（memory bandwidth节省），比BF16慢9%（需要cast操作）。 这个实验为paper提供了一个"practical
756	    mitigation"故事：如果practitioner担心precision影响， LayerCast以minimal overhead提供FP32-level
757	    behavior。
758	
759	    '
760	  tables:
761	  - name: 'Table 11: Precision Mode Comparison'
762	    columns:
763	    - Mode
764	    - Accuracy
765	    - item Agreement w/ FP32
766	    - Throughput (tokens/s)
767	    - VRAM (GB)
768	    rows:
769	    - - FP32
770	      - 0.666
771	      - 1.0
772	      - 1820
773	      - 31.2
774	    - - BF16
775	      - 0.671
776	      - 0.9985
777	      - 2760
778	      - 15.8
779	    - - FP16
780	      - 0.669
781	      - 0.9982
782	      - 2810
783	      - 15.6
784	    - - LayerCast
785	      - 0.67
786	      - 0.9991
787	      - 2510
788	      - 16.1
789	  figures_description:
790	  - 'Fig 14: 4-precision mode accuracy distribution violin plots，展示LayerCast与FP32几乎identical
791	    spread。'
792	  analysis: 'P2实验。LayerCast结果进一步support precision不是major concern（在engine confound
793	    fix后）。 可作为paper中"practical recommendation"段落的一条：对于追求最高reproducibility的场景， LayerCast提供了memory-efficient的FP32-equivalent选项。
794	
795	    '
796	- name: MATH benchmark extension
797	  plan_id: exp-008
798	  description: '4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures
799	    × 4 orderings × 200 MATH items。 总记录 4×2×6×6×2×4×200=230,400。测试reasoning-heavy
800	    task的variance structure。
801	
802	    '
803	  expected_results:
804	    math_overall_accuracy: 0.342
805	    math_item_id: 0.421
806	    math_residual: 0.248
807	    math_temperature_x_item: 0.104
808	    math_prompt_x_item: 0.068
809	    math_seed_x_item: 0.052
810	    math_temperature: 0.038
811	    math_prompt: 0.021
812	    math_precision: 0.002
813	    math_precision_x_item: 0.008
814	    math_ordering_x_item: 0.015
815	    math_g_current_practice: 0.24
816	    math_item_id_rank1: true
817	    math_optimal_g90_items: 1100
818	    math_optimal_g90_prompts: 4
819	    math_optimal_g90_seeds: 3
820	  result_rationale: 'MATH是所有benchmark中最challenging的（accuracy ~34%），其item difficulty分布极端——
821	    从Level 1（algebra basics）到Level 5（competition math），跨越巨大的difficulty range。 Item_id仍为rank-1（42.1%）但低于MMLU，因为：(1)
822	    lower overall accuracy增加了random guessing的比例， 膨胀residual到24.8%；(2) MATH的CoT generation比GSM8K更长更复杂（多步proof-like
823	    reasoning）， 使temperature×item interaction达到10.4%——在高temperature下，长推理链的任何一步都可能diverge，
824	    且这种sensitivity是item-specific的（Level 5 problems的长推理链比Level 1的短计算更sensitive）。 Temperature主效应也最高（3.8%），因为MATH的generation
825	    length使sampling temperature的cumulative effect更显著。 G current practice仅0.24——所有benchmark中最低——意味着MATH
826	    evaluation的reproducibility最差。 达到G≥0.90需要1100 items + 4 prompts + 3 seeds，是MMLU所需的~3倍evaluation
827	    budget。 这个发现有strong policy implication：reasoning benchmark的evaluation标准需要比classification
828	    benchmark更严格。
829	
830	    '
831	  tables:
832	  - name: 'Table 12: Full Cross-Benchmark Variance Summary (5 benchmarks)'
833	    columns:
834	    - Benchmark
835	    - Accuracy
836	    - item_id %
837	    - Residual %
838	    - Temp×Item %
839	    - G (current)
840	    - Items for G≥0.90
841	    rows:
842	    - - MMLU
843	      - 0.668
844	      - 58.4
845	      - 16.8
846	      - 5.8
847	      - 0.34
848	      - 600
849	    - - ARC-Challenge
850	      - 0.597
851	      - 55.1
852	      - 18.2
853	      - 5.4
854	      - 0.32
855	      - 650
856	    - - HellaSwag
857	      - 0.712
858	      - 52.7
859	      - 19.5
860	      - 6.2
861	      - 0.36
862	      - 550
863	    - - GSM8K
864	      - 0.583
865	      - 48.7
866	      - 21.4
867	      - 8.9
868	      - 0.29
869	      - 800
870	    - - MATH
871	      - 0.342
872	      - 42.1
873	      - 24.8
874	      - 10.4
875	      - 0.24
876	      - 1100
877	  figures_description:
878	  - 'Fig 15: 5-benchmark stacked bars排序by task difficulty，展示清晰的gradient：task越难→item_id越低、residual和temp×item越高。'
879	  - 'Fig 16: D-study projection curves for 5 benchmarks overlay，MATH曲线最右（需最多evaluations达G≥0.90）。'
880	  analysis: MATH提供了variance structure的"stress test"。Item_id在最extreme条件下仍为rank-1（42.1%），
881	    但task difficulty明显调节了variance decomposition的profile。5个benchmark展现了清晰的gradient：
882	    task difficulty ↑ → item_id share ↓, residual ↑, temperature×item ↑, G current
883	    practice ↓。 这个gradient本身是publishable finding：它量化了为什么reasoning benchmark的evaluation更不稳定，
884	    并给出了task-specific的reproducibility budget。
885	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c2686d6-0a9e-4401-b99f-2c9f12aca353",
  "isSidechain": false,
  "promptId": "c295c0c9-7475-4ab1-87e4-a49b6b5cf1ca",
  "type": "user",
  "uuid": "374e8ab7-01a4-47d0-83d0-252ce74a56b2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/imagined_experiments.yaml",
      "content": "tier: best\nnarrative_guidance: '原始framing完全成立。float32 confound修复后precision主效应坍缩至噪声水平，反而成为方法论贡献（展示engine配置对variance\n  attribution的系统性影响）。 Item dominance在所有benchmark上复现为最大单一方差源，4个模型一致。Separability在aggregate\n  level成立（direct interaction <0.5%）， 但item-conditional interactions提供nuanced story。D-study\n  budget表给出clear actionable guidance，headline数字\"item selection >50%\"直接可用。 AAAI投稿节奏正常，三条claim原封不动。\n\n  '\nimagined_experiments:\n- name: Full-scale precision study with confound fix\n  plan_id: exp-001\n  description: '4 models × 3 precisions (FP32/BF16/FP16) × 6 prompts × 6 seeds × 3\n    temperatures × 4 orderings × 200 MMLU items, 全部使用vLLM V0 enforce_eager消除engine差异。总条件数\n    4×3×6×6×3×4=5184 per item, 总记录 5184×200=1,036,800。\n\n    '\n  expected_results:\n    total_records: 1036800\n    conditions_per_model: 1296\n    overall_accuracy: 0.668\n    accuracy_fp32: 0.666\n    accuracy_bf16: 0.671\n    accuracy_fp16: 0.669\n    accuracy_spread_across_precisions: 0.005\n    item_id: 0.584\n    residual: 0.168\n    prompt_template_x_item_id: 0.061\n    temperature_x_item_id: 0.058\n    seed_x_item_id: 0.029\n    precision_x_item_id: 0.018\n    ordering_x_item_id: 0.014\n    prompt_template: 0.009\n    temperature: 0.007\n    ordering: 0.003\n    precision: 0.003\n    seed: 0.001\n    models_with_item_id_rank1: 4\n    item_id_range_across_models:\n    - 0.52\n    - 0.62\n    qwen3_8b_item_id: 0.598\n    llama31_8b_item_id: 0.571\n    gemma2_9b_item_id: 0.62\n    mistral_7b_item_id: 0.547\n    precision_main_effect_before_fix_mvp: 0.0087\n    precision_main_effect_after_fix: 0.003\n    precision_x_item_id_before_fix_mvp: 0.0724\n    precision_x_item_id_after_fix: 0.018\n    fp32_bf16_accuracy_gap_before_fix: 0.085\n    fp32_bf16_accuracy_gap_after_fix: 0.005\n    g_current_practice_1p1s200i: 0.34\n    g_6p6s200i: 0.72\n    g_6p6s200i_3t4o: 0.78\n  result_rationale: 'MVP中precision主效应0.87%和precision×item交互7.24%主要来自float32使用不同vLLM\n    engine路径（非V0时触发不同kernel）， 导致FP32准确率系统性偏低5.7pp。统一V0 enforce_eager后，三种精度走同一compute\n    path， FP32/BF16/FP16准确率差收敛至0.5pp以内（纯numerical noise水平）。precision主效应从0.87%降至~0.3%，\n    precision×item从7.24%降至~1.8%。这些被释放的方差份额主要回流到residual和item_id， 使item_id维持在~58%（与MVP一致，因为item\n    difficulty本身是真实信号，不受engine confound影响）。 4个模型均以item_id为rank-1组分，因为MMLU的item difficulty分布（从trivial到expert-level）\n    在所有7-9B模型上产生类似的accuracy ceiling/floor效应。Gemma-2略高因其instruction-tuned特性 使其对easy\n    items更稳定（floor更高），Mistral略低因其在部分domain上accuracy更平坦。 200 items（分层采样）比MVP的50 items提供更稳定的方差估计，置信区间收窄约50%。\n\n    '\n  tables:\n  - name: 'Table 1: Variance Component Estimates — MMLU 200 items, 4 models pooled'\n    columns:\n    - Component\n    - '% Variance'\n    - SE\n    - 95% CI Lower\n    - 95% CI Upper\n    - MVP (50 items)\n    rows:\n    - - item_id\n      - 58.4\n      - 2.1\n      - 54.3\n      - 62.5\n      - 58.4\n    - - residual\n      - 16.8\n      - 0.9\n      - 15.0\n      - 18.6\n      - 17.6\n    - - prompt×item\n      - 6.1\n      - 0.7\n      - 4.7\n      - 7.5\n      - 5.7\n    - - temp×item\n      - 5.8\n      - 0.6\n      - 4.6\n      - 7.0\n      - 6.9\n    - - seed×item\n      - 2.9\n      - 0.4\n      - 2.1\n      - 3.7\n      - 2.7\n    - - precision×item\n      - 1.8\n      - 0.3\n      - 1.2\n      - 2.4\n      - 7.2*\n    - - ordering×item\n      - 1.4\n      - 0.3\n      - 0.8\n      - 2.0\n      - —\n    - - prompt\n      - 0.9\n      - 0.3\n      - 0.3\n      - 1.5\n      - —\n    - - temperature\n      - 0.7\n      - 0.2\n      - 0.3\n      - 1.1\n      - —\n    - - precision\n      - 0.3\n      - 0.1\n      - 0.1\n      - 0.5\n      - 0.87*\n    - - ordering\n      - 0.3\n      - 0.1\n      - 0.1\n      - 0.5\n      - —\n    - - seed\n      - 0.1\n      - 0.05\n      - 0.0\n      - 0.2\n      - —\n  - name: 'Table 2: Per-Model item_id Variance Share'\n    columns:\n    - Model\n    - item_id %\n    - Next Largest\n    - Next %\n    rows:\n    - - Qwen3-8B\n      - 59.8\n      - residual\n      - 16.2\n    - - Llama-3.1-8B\n      - 57.1\n      - residual\n      - 17.8\n    - - Gemma-2-9B-IT\n      - 62.0\n      - residual\n      - 14.9\n    - - Mistral-7B-v0.3\n      - 54.7\n      - residual\n      - 18.5\n  figures_description:\n  - 'Fig 1: Stacked-bar variance decomposition — MVP (confounded) vs exp-001 (fixed),\n    side-by-side。左栏显示precision和precision×item的膨胀，右栏显示修复后两者坍缩，item_id占比不变。'\n  - 'Fig 2: 4-panel per-model stacked bars，展示item_id始终为rank-1的cross-model consistency。'\n  - 'Fig 3: FP32 vs BF16 accuracy scatter (per-item)，MVP中slope偏离1.0，exp-001中回归到~1.0。'\n  analysis: '核心发现：engine confound修复后item dominance完全稳健，precision主效应从0.87%降至0.3%。 这同时验证了Claim\n    1（item dominance）和提供了方法论贡献（engine配置对variance attribution的影响）。 4个模型一致性消除了\"Qwen3特例\"的concern。200\n    items分层采样提供了足够的statistical power。 Ordering facet新增后占比很小（~1.7% total含interaction），说明item\n    presentation order不是主要concern。\n\n    '\n- name: Multi-benchmark replication\n  plan_id: exp-002\n  description: '4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures\n    × 4 orderings × 200 items, 分别在GSM8K、ARC-Challenge、HellaSwag上运行。每benchmark总记录 4×2×6×6×2×4×200=230,400。\n\n    '\n  expected_results:\n    gsm8k_overall_accuracy: 0.583\n    gsm8k_item_id: 0.487\n    gsm8k_residual: 0.214\n    gsm8k_temperature_x_item_id: 0.089\n    gsm8k_prompt_x_item_id: 0.072\n    gsm8k_seed_x_item_id: 0.041\n    gsm8k_precision_x_item_id: 0.012\n    gsm8k_ordering_x_item_id: 0.018\n    gsm8k_temperature: 0.024\n    gsm8k_prompt: 0.015\n    gsm8k_precision: 0.002\n    gsm8k_g_current_practice: 0.29\n    arc_overall_accuracy: 0.597\n    arc_item_id: 0.551\n    arc_residual: 0.182\n    arc_prompt_x_item_id: 0.068\n    arc_temperature_x_item_id: 0.054\n    arc_seed_x_item_id: 0.031\n    arc_precision_x_item_id: 0.014\n    arc_ordering_x_item_id: 0.016\n    arc_prompt: 0.011\n    arc_temperature: 0.008\n    arc_precision: 0.002\n    arc_g_current_practice: 0.32\n    hellaswag_overall_accuracy: 0.712\n    hellaswag_item_id: 0.527\n    hellaswag_residual: 0.195\n    hellaswag_prompt_x_item_id: 0.058\n    hellaswag_temperature_x_item_id: 0.062\n    hellaswag_seed_x_item_id: 0.033\n    hellaswag_precision_x_item_id: 0.011\n    hellaswag_ordering_x_item_id: 0.019\n    hellaswag_prompt: 0.008\n    hellaswag_temperature: 0.006\n    hellaswag_precision: 0.001\n    hellaswag_g_current_practice: 0.36\n    benchmarks_with_item_id_rank1: 4\n    item_id_range_across_benchmarks:\n    - 0.487\n    - 0.584\n    cross_benchmark_replication_rate: 1.0\n    models_showing_consistent_pattern: 4\n  result_rationale: 'GSM8K的item_id占比略低于MMLU（48.7% vs 58.4%），因为数学推理任务引入更多chain-of-thought随机性，\n    使residual和temperature×item交互膨胀。GSM8K中温度效应更大（temperature×item 8.9%）， 因为CoT生成路径对sampling\n    temperature更敏感——同一道数学题在不同温度下可能走完全不同的推理链。 但item_id仍然是rank-1组分，因为GSM8K的difficulty\n    gradient极陡（从单步算术到多步word problem）， 这种item-level variance在所有条件下都主导。ARC-Challenge的item_id（55.1%）接近MMLU，\n    因为科学推理题的difficulty分布类似（从factual recall到multi-hop inference）。 HellaSwag的item_id（52.7%）也稳健，因为commonsense\n    completion的item variance主要来自 distractor quality差异——有些items的wrong answers显而易见，有些几乎无法区分。\n    所有benchmark上precision主效应均<0.3%，确认engine confound fix的泛化性。 4/4 benchmark的item_id\n    rank-1复现率为100%，支撑\"cross-benchmark replication rate = 1.0\"。\n\n    '\n  tables:\n  - name: 'Table 3: Cross-Benchmark Variance Decomposition Summary'\n    columns:\n    - Benchmark\n    - item_id %\n    - Residual %\n    - Item-Conditional Total %\n    - Precision Main %\n    - G (current)\n    rows:\n    - - MMLU\n      - 58.4\n      - 16.8\n      - 16.1\n      - 0.3\n      - 0.34\n    - - GSM8K\n      - 48.7\n      - 21.4\n      - 23.2\n      - 0.2\n      - 0.29\n    - - ARC-Challenge\n      - 55.1\n      - 18.2\n      - 18.3\n      - 0.2\n      - 0.32\n    - - HellaSwag\n      - 52.7\n      - 19.5\n      - 18.3\n      - 0.1\n      - 0.36\n  - name: 'Table 4: GSM8K Per-Model Breakdown'\n    columns:\n    - Model\n    - item_id %\n    - temp×item %\n    - prompt×item %\n    - residual %\n    rows:\n    - - Qwen3-8B\n      - 51.2\n      - 8.1\n      - 6.8\n      - 19.8\n    - - Llama-3.1-8B\n      - 47.3\n      - 9.4\n      - 7.6\n      - 22.1\n    - - Gemma-2-9B-IT\n      - 50.8\n      - 8.5\n      - 6.9\n      - 20.3\n    - - Mistral-7B-v0.3\n      - 43.4\n      - 10.5\n      - 8.3\n      - 23.5\n  figures_description:\n  - 'Fig 4: 4-benchmark stacked-bar variance decomposition并排对比。item_id始终为最大色块，但GSM8K的residual和temperature×item色块明显更大。'\n  - 'Fig 5: Heatmap — benchmark × model × component，展示pattern consistency。色块深浅表示variance\n    share，item_id行始终最深。'\n  analysis: 'Item dominance在4个benchmark上全部复现（range 48.7%-58.4%），但幅度因task type有系统性差异：\n    generation-heavy tasks（GSM8K）因CoT随机性使residual膨胀，压缩item_id相对占比； classification-like\n    tasks（MMLU, ARC）的item_id更高。这个gradient本身是有趣的发现， 可在Discussion中展开。关键是即使在\"worst case\"的GSM8K上，item_id仍是rank-1（48.7%\n    > residual 21.4%）， headline claim成立。\n\n    '\n- name: Multi-hardware G-study\n  plan_id: exp-003\n  description: '4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions\n    (BF16/FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。总记录\n    4×2×2×6×6×3×4×200=691,200。 核心目标：量化hardware主效应和hardware×methodology交互。\n\n    '\n  expected_results:\n    total_records: 691200\n    hardware_main_effect: 0.006\n    hardware_x_precision: 0.002\n    hardware_x_prompt: 0.001\n    hardware_x_temperature: 0.001\n    hardware_x_seed: 0.0005\n    hardware_x_ordering: 0.0003\n    hardware_x_item_id: 0.019\n    precision_x_prompt: 0.0008\n    precision_x_temperature: 0.0006\n    precision_x_seed: 0.0003\n    precision_x_ordering: 0.0002\n    direct_infra_method_interaction_total: 0.005\n    item_conditional_interactions_total: 0.142\n    item_id: 0.561\n    residual: 0.152\n    prompt_x_item: 0.059\n    temperature_x_item: 0.055\n    seed_x_item: 0.028\n    precision_x_item: 0.017\n    ordering_x_item: 0.013\n    hardware_x_item: 0.019\n    separability_ratio: 0.035\n    gpu1_gpu2_accuracy_correlation: 0.9987\n    max_accuracy_difference_any_condition: 0.018\n    mean_accuracy_difference: 0.004\n    g_current_practice: 0.33\n    g_full_design: 0.81\n  result_rationale: 'Hardware主效应0.6%反映两块GPU的微架构差异（不同SM count、memory bandwidth、kernel\n    scheduling）， 但这些差异是系统性的（固定偏移），不是随机的，所以主效应很小。hardware×item交互1.9%比hardware主效应大，\n    因为特定items（如需要长sequence generation的items）在不同GPU上因kernel tiling差异产生不同的numerical\n    path， 但这只影响边界case items。所有direct infra×method交互加总仅0.5%，因为infrastructure层（hardware\n    type, precision） 和methodology层（prompt, seed, temperature, ordering）作用于不同的computation\n    stages： precision/hardware影响numerical computation，prompt/seed/temperature影响token\n    sampling， 两者的交叉点（sampling受precision影响的程度）在logit空间中被softmax压缩到negligible水平。 Item-conditional\n    interactions总和14.2%远大于direct interactions 0.5%，验证了Claim 2的nuanced story： separability在aggregate成立，但两层都通过item\n    difficulty调节其效应。 GPU间accuracy correlation 0.9987说明hardware几乎不改变model ranking，只在individual\n    item level引入微小噪声。\n\n    '\n  tables:\n  - name: 'Table 5: Separability Test — Direct vs Item-Conditional Interactions'\n    columns:\n    - Interaction Type\n    - Components\n    - Total % Variance\n    - Interpretation\n    rows:\n    - - Direct Infra×Method\n      - hw×prompt, hw×temp, hw×seed, hw×ord, prec×prompt, prec×temp, prec×seed, prec×ord\n      - 0.5\n      - Negligible — separability holds at aggregate\n    - - Infra×Item\n      - hw×item, prec×item\n      - 3.6\n      - Small but non-zero — hardware/precision effects are item-conditional\n    - - Method×Item\n      - prompt×item, temp×item, seed×item, ord×item\n      - 15.5\n      - Substantial — methodology effects are strongly item-conditional\n    - - Item Main\n      - item_id\n      - 56.1\n      - Dominant — item selection is the primary variance source\n  - name: 'Table 6: Hardware Agreement Matrix (per-model mean accuracy)'\n    columns:\n    - Model\n    - GPU1\n    - GPU2\n    - Difference\n    rows:\n    - - Qwen3-8B\n      - 0.671\n      - 0.668\n      - 0.003\n    - - Llama-3.1-8B\n      - 0.654\n      - 0.65\n      - 0.004\n    - - Gemma-2-9B-IT\n      - 0.689\n      - 0.684\n      - 0.005\n    - - Mistral-7B-v0.3\n      - 0.638\n      - 0.634\n      - 0.004\n  figures_description:\n  - 'Fig 6: Separability diagram — 两层圆（infra layer, method layer）通过item difficulty连接，直接交互箭头用虚线（<0.5%），item-conditional箭头用实线。'\n  - 'Fig 7: GPU1 vs GPU2 per-item accuracy scatter，近乎perfect diagonal，少数outlier items标注。'\n  analysis: 'Separability成立：direct infra×method交互总和0.5%，远低于1%阈值。但不是trivial null result——\n    item-conditional interactions（14.2%）提供了nuanced interpretation：infrastructure和methodology\n    不是完全独立的，而是通过item difficulty间接耦合。这比simple \"separable/not separable\"更有价值， 因为它解释了为什么isolated-factor\n    studies的结论在某些items上不泛化。 这同时支撑了Claim 2的两半：\"empirical license for isolated-factor\n    studies\"（direct <0.5%） 和 \"conclusions are conditional on item selection\"（item-conditional\n    14.2%）。\n\n    '\n- name: D-study reproducibility budget projections\n  plan_id: exp-004\n  description: '基于exp-001/002/003的合并variance component estimates，计算不同facet allocation下的G系数。\n    生成practitioner-facing budget tables和projection curves。纯计算，无GPU开销。\n\n    '\n  expected_results:\n    g_1prompt_1seed_200items_mmlu: 0.34\n    g_1prompt_1seed_200items_gsm8k: 0.29\n    g_1prompt_1seed_200items_arc: 0.32\n    g_1prompt_1seed_200items_hellaswag: 0.36\n    g_1prompt_1seed_600items_mmlu: 0.71\n    g_1prompt_1seed_1000items_mmlu: 0.82\n    g_1prompt_1seed_2000items_mmlu: 0.9\n    g_3prompt_1seed_200items_mmlu: 0.42\n    g_6prompt_1seed_200items_mmlu: 0.49\n    g_12prompt_1seed_200items_mmlu: 0.54\n    g_1prompt_3seed_200items_mmlu: 0.36\n    g_1prompt_6seed_200items_mmlu: 0.37\n    optimal_g90_items: 600\n    optimal_g90_prompts: 3\n    optimal_g90_seeds: 2\n    optimal_g90_total_conditions: 6\n    optimal_g90_total_evaluations: 3600\n    optimal_g95_items: 1200\n    optimal_g95_prompts: 4\n    optimal_g95_seeds: 3\n    optimal_g95_total_conditions: 12\n    optimal_g95_total_evaluations: 14400\n    marginal_g_per_100_items: 0.038\n    marginal_g_per_prompt: 0.025\n    marginal_g_per_seed: 0.005\n    items_vs_prompts_effectiveness_ratio: 10.2\n    items_vs_seeds_effectiveness_ratio: 51.0\n    gsm8k_optimal_g90_items: 800\n    gsm8k_optimal_g90_prompts: 3\n    gsm8k_optimal_g90_seeds: 2\n    arc_optimal_g90_items: 650\n    hellaswag_optimal_g90_items: 550\n  result_rationale: 'G系数由universe score variance与observed score variance的比值决定。因为item_id占总方差>50%，\n    增加item采样直接压缩最大的variance component，G提升最快。具体地，G ≈ σ²(τ) / [σ²(τ) + σ²(δ)/n_facets]，\n    当item_id是σ²(δ)的主要贡献者时，增加n_items的marginal return远超增加n_prompts或n_seeds。 数值上，从200到600\n    items（3×）使G从0.34升至0.71，而从1到3 prompts（3×）仅从0.34升至0.42。 这是因为prompt variance（含prompt×item）共计~7%，而item\n    variance 58%。 Seed几乎无效（G从0.34到0.37 at 6 seeds），因为seed的总方差贡献<3%（主要通过seed×item）。\n    G≥0.90需要~600 items + 3 prompts + 2 seeds = 3,600 evaluations。 当前标准practice（1 prompt,\n    1 seed, 200 items）的G < 0.40意味着evaluation结果的reliability 低于社会科学中\"不可接受\"的阈值（通常G≥0.80）。\n    GSM8K需要更多items（800 vs 600）达到G≥0.90，因为其residual更大（CoT随机性）， 需要更多items来平均掉item-level\n    noise。\n\n    '\n  tables:\n  - name: 'Table 7: Reproducibility Budget — MMLU (Items × Prompts × Seeds → G coefficient)'\n    columns:\n    - Items\n    - Prompts\n    - Seeds\n    - Total Evals\n    - G coeff\n    - Δ vs Current\n    rows:\n    - - 200\n      - 1\n      - 1\n      - 200\n      - 0.34\n      - baseline\n    - - 200\n      - 3\n      - 1\n      - 600\n      - 0.42\n      - '+0.08'\n    - - 200\n      - 6\n      - 1\n      - 1200\n      - 0.49\n      - '+0.15'\n    - - 200\n      - 6\n      - 6\n      - 7200\n      - 0.54\n      - '+0.20'\n    - - 600\n      - 1\n      - 1\n      - 600\n      - 0.71\n      - '+0.37'\n    - - 600\n      - 3\n      - 1\n      - 1800\n      - 0.82\n      - '+0.48'\n    - - 600\n      - 3\n      - 2\n      - 3600\n      - 0.9\n      - '+0.56'\n    - - 1000\n      - 3\n      - 2\n      - 6000\n      - 0.93\n      - '+0.59'\n    - - 1200\n      - 4\n      - 3\n      - 14400\n      - 0.95\n      - '+0.61'\n    - - 2000\n      - 4\n      - 3\n      - 24000\n      - 0.97\n      - '+0.63'\n  - name: 'Table 8: Cross-Benchmark Minimum Budget for G≥0.90'\n    columns:\n    - Benchmark\n    - Items\n    - Prompts\n    - Seeds\n    - Total Evals\n    - Cost Factor vs Current\n    rows:\n    - - MMLU\n      - 600\n      - 3\n      - 2\n      - 3600\n      - 18×\n    - - GSM8K\n      - 800\n      - 3\n      - 2\n      - 4800\n      - 24×\n    - - ARC-Challenge\n      - 650\n      - 3\n      - 2\n      - 3900\n      - 19.5×\n    - - HellaSwag\n      - 550\n      - 3\n      - 2\n      - 3300\n      - 16.5×\n  figures_description:\n  - 'Fig 8: D-study projection curves — G coefficient vs total evaluations，三条线分别对应\n    scale items only / scale prompts only / scale seeds only。Items线陡峭上升，prompts线平缓，seeds线几乎flat。'\n  - 'Fig 9: Iso-G contour plot（items × prompts平面，G值等高线），展示最优allocation路径沿items轴延伸。'\n  - 'Fig 10: 4-benchmark overlay projection curves，展示GSM8K需要更多evaluations但pattern一致。'\n  analysis: 'Claim 3的核心表格。Headline数字：\"tripling items is 10× more effective than tripling\n    prompts\" 直接来自marginal effectiveness ratio 10.2:1。当前practice G<0.40的发现具有强policy\n    implication—— 意味着现有leaderboard结果的measurement reliability低于社会科学中最低标准。 600 items\n    + 3 prompts + 2 seeds的\"recommended minimum\"在计算成本上仅为full factorial的一小部分， 是actionable的建议。跨benchmark\n    budget差异（550-800 items for G≥0.90）提供task-specific guidance。\n\n    '\n- name: 14B model extension\n  plan_id: exp-005\n  description: 'Qwen3-14B和DeepSeek-R1-Distill-14B × 2 precisions (BF16/FP16) × 6 prompts\n    × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。每模型 2×6×6×3×4×200=172,800记录。\n\n    '\n  expected_results:\n    qwen3_14b_accuracy: 0.728\n    deepseek_r1_14b_accuracy: 0.714\n    qwen3_14b_item_id: 0.574\n    deepseek_r1_14b_item_id: 0.538\n    qwen3_14b_residual: 0.162\n    deepseek_r1_14b_residual: 0.198\n    deepseek_r1_14b_temperature_x_item: 0.082\n    scale_effect_on_item_id: within 8B model range\n    item_id_rank1_both_models: true\n    variance_pattern_consistent_with_8b: true\n    precision_main_effect_14b: 0.002\n  result_rationale: '14B模型的overall accuracy更高，但item difficulty的variance structure不会因scale改变——\n    easy items仍然easy，hard items仍然hard。Item_id占比略低于8B平均值（~55-57% vs ~58%）， 因为14B模型在medium-difficulty\n    items上表现更一致（ceiling effect压缩了item variance的上端）， 但差异不大。DeepSeek-R1-Distill的reasoning-distilled特性使其在CoT-heavy\n    items上产生更多 temperature×item交互（类似GSM8K的pattern），residual也略高，因为distillation引入的implicit\n    CoT 增加了generation-level stochasticity。关键是item_id在两个14B模型上仍为rank-1， 确认pattern不随model\n    scale改变。precision主效应在14B上同样negligible（0.2%）， 因为confound fix的原理（统一engine path）与model\n    size无关。\n\n    '\n  tables:\n  - name: 'Table 9: 14B vs 8B Variance Pattern Comparison'\n    columns:\n    - Component\n    - 8B Mean\n    - 8B Range\n    - Qwen3-14B\n    - DS-R1-14B\n    rows:\n    - - item_id\n      - 58.4\n      - 54.7–62.0\n      - 57.4\n      - 53.8\n    - - residual\n      - 16.8\n      - 14.9–18.5\n      - 16.2\n      - 19.8\n    - - temp×item\n      - 5.8\n      - 4.6–7.0\n      - 5.3\n      - 8.2\n    - - prompt×item\n      - 6.1\n      - 4.7–7.5\n      - 5.8\n      - 5.4\n    - - precision\n      - 0.3\n      - 0.1–0.5\n      - 0.2\n      - 0.2\n  figures_description:\n  - 'Fig 11: 6-model panel（4×8B + 2×14B）stacked bars，展示scale不改变variance hierarchy。'\n  analysis: 'Scale invariance确认：item dominance不是小模型artifacts。DeepSeek-R1-Distill的slightly不同的profile\n    （更高residual, 更高temp×item）提供了architecture effect的初步evidence， 但不改变core claim。这是P1实验，为paper增加robustness但非必需。\n\n    '\n- name: Fine-tuning G-study\n  plan_id: exp-006\n  description: 'RoBERTa-large在SST-2/MNLI/RTE/COPA上fine-tuning。6 seeds × 3 learning\n    rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task × 4 tasks = 1,728\n    total。\n\n    '\n  expected_results:\n    sst2_accuracy_mean: 0.948\n    sst2_item_id: 0.412\n    sst2_seed: 0.087\n    sst2_learning_rate: 0.063\n    sst2_data_shuffle: 0.042\n    sst2_seed_x_item: 0.098\n    sst2_lr_x_item: 0.074\n    sst2_residual: 0.131\n    sst2_gpu: 0.003\n    sst2_precision: 0.002\n    mnli_accuracy_mean: 0.876\n    mnli_item_id: 0.445\n    mnli_seed: 0.072\n    mnli_learning_rate: 0.081\n    mnli_data_shuffle: 0.038\n    mnli_seed_x_item: 0.091\n    mnli_residual: 0.142\n    rte_accuracy_mean: 0.743\n    rte_item_id: 0.368\n    rte_seed: 0.124\n    rte_learning_rate: 0.098\n    rte_data_shuffle: 0.067\n    rte_seed_x_item: 0.112\n    rte_residual: 0.158\n    copa_accuracy_mean: 0.682\n    copa_item_id: 0.382\n    copa_seed: 0.118\n    copa_learning_rate: 0.091\n    copa_residual: 0.167\n    item_id_rank1_all_tasks: true\n    seed_more_important_than_inference: true\n    infra_effects_negligible: true\n    fine_tuning_g_current_practice: 0.28\n  result_rationale: 'Fine-tuning与inference的关键区别：training seed和learning rate成为substantial\n    variance sources （combined 10-22%），因为它们影响optimization trajectory，不仅仅是sampling\n    randomness。 但item_id仍然是rank-1（37-45%），因为NLU tasks的item difficulty gradient—— 从\"I\n    love this movie\"(trivially positive)到需要subtle pragmatic inference的examples—— 在所有training\n    configurations下都产生consistent accuracy variation。 RTE的item_id最低（36.8%），因为小数据集（2.5K\n    training examples）使fine-tuning对seed更敏感， seed主效应膨胀到12.4%。这为paper提供了\"inference vs\n    fine-tuning\"的对比dimension： 两者都是item-dominant，但fine-tuning中training hyperparameters（seed,\n    LR）取代了 inference中的generation parameters（temperature, prompt）成为第二梯队的variance sources。\n    GPU和precision主效应在fine-tuning中同样negligible（<0.5%），因为RoBERTa-large 对numerical precision不敏感（unlike\n    large generative models的autoregressive error accumulation）。\n\n    '\n  tables:\n  - name: 'Table 10: Fine-tuning vs Inference Variance Hierarchy'\n    columns:\n    - Rank\n    - Inference (MMLU)\n    - Fine-tuning (SST-2)\n    rows:\n    - - 1\n      - item_id (58.4%)\n      - item_id (41.2%)\n    - - 2\n      - residual (16.8%)\n      - residual (13.1%)\n    - - 3\n      - prompt×item (6.1%)\n      - seed×item (9.8%)\n    - - 4\n      - temp×item (5.8%)\n      - seed (8.7%)\n    - - 5\n      - seed×item (2.9%)\n      - lr×item (7.4%)\n    - - 6\n      - precision×item (1.8%)\n      - lr (6.3%)\n  figures_description:\n  - 'Fig 12: Inference vs Fine-tuning stacked bars并排，展示item_id在两个paradigm中均为rank-1但fine-tuning中seed/LR更prominent。'\n  - 'Fig 13: 4-task fine-tuning panel，展示dataset size对variance structure的调节效应（RTE seed最大）。'\n  analysis: 'Fine-tuning G-study将paper从\"inference evaluation reproducibility\"扩展到\"ML\n    reproducibility broadly\"。 核心takeaway：item dominance是跨paradigm的（inference和fine-tuning），但second-tier\n    factors不同。 这是P1实验，为paper增加generality但AAAI投稿时可作为supplementary。\n\n    '\n- name: LayerCast precision study\n  plan_id: exp-007\n  description: '在MMLU上测试LayerCast（FP16 storage + FP32 compute）作为额外precision condition。\n    4 models × 1 precision mode × 6 prompts × 6 seeds × 3 temperatures × 4 orderings\n    × 200 items = 172,800记录。\n\n    '\n  expected_results:\n    layercast_accuracy_mean: 0.67\n    layercast_vs_fp32_accuracy_diff: 0.004\n    layercast_vs_bf16_accuracy_diff: -0.001\n    layercast_item_agreement_with_fp32: 0.9991\n    layercast_item_agreement_with_bf16: 0.9994\n    layercast_added_variance_to_precision: 0.0004\n    layercast_throughput_vs_fp32: 1.38\n    layercast_throughput_vs_bf16: 0.91\n    layercast_precision_x_item_contribution: 0.009\n  result_rationale: 'LayerCast在存储时用FP16减少memory footprint，在compute时cast to FP32， 因此其numerical\n    behavior几乎等同于纯FP32（computation path一致）， accuracy差异仅来自storage时的precision loss（FP16\n    mantissa 10 bits vs FP32 23 bits）， 这对大部分weights来说negligible（在训练时weights就是从FP16/BF16来的）。\n    与BF16的差异更小（0.1pp），因为BF16的dynamic range与FP32一致（8-bit exponent）， 而FP16的range更窄但mantissa更宽，两者accuracy接近。\n    LayerCast对precision variance几乎没有增量贡献（0.04%），因为它本质上是FP32 compute的cheaper variant。\n    Throughput方面，LayerCast比FP32快38%（memory bandwidth节省），比BF16慢9%（需要cast操作）。 这个实验为paper提供了一个\"practical\n    mitigation\"故事：如果practitioner担心precision影响， LayerCast以minimal overhead提供FP32-level\n    behavior。\n\n    '\n  tables:\n  - name: 'Table 11: Precision Mode Comparison'\n    columns:\n    - Mode\n    - Accuracy\n    - item Agreement w/ FP32\n    - Throughput (tokens/s)\n    - VRAM (GB)\n    rows:\n    - - FP32\n      - 0.666\n      - 1.0\n      - 1820\n      - 31.2\n    - - BF16\n      - 0.671\n      - 0.9985\n      - 2760\n      - 15.8\n    - - FP16\n      - 0.669\n      - 0.9982\n      - 2810\n      - 15.6\n    - - LayerCast\n      - 0.67\n      - 0.9991\n      - 2510\n      - 16.1\n  figures_description:\n  - 'Fig 14: 4-precision mode accuracy distribution violin plots，展示LayerCast与FP32几乎identical\n    spread。'\n  analysis: 'P2实验。LayerCast结果进一步support precision不是major concern（在engine confound\n    fix后）。 可作为paper中\"practical recommendation\"段落的一条：对于追求最高reproducibility的场景， LayerCast提供了memory-efficient的FP32-equivalent选项。\n\n    '\n- name: MATH benchmark extension\n  plan_id: exp-008\n  description: '4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures\n    × 4 orderings × 200 MATH items。 总记录 4×2×6×6×2×4×200=230,400。测试reasoning-heavy\n    task的variance structure。\n\n    '\n  expected_results:\n    math_overall_accuracy: 0.342\n    math_item_id: 0.421\n    math_residual: 0.248\n    math_temperature_x_item: 0.104\n    math_prompt_x_item: 0.068\n    math_seed_x_item: 0.052\n    math_temperature: 0.038\n    math_prompt: 0.021\n    math_precision: 0.002\n    math_precision_x_item: 0.008\n    math_ordering_x_item: 0.015\n    math_g_current_practice: 0.24\n    math_item_id_rank1: true\n    math_optimal_g90_items: 1100\n    math_optimal_g90_prompts: 4\n    math_optimal_g90_seeds: 3\n  result_rationale: 'MATH是所有benchmark中最challenging的（accuracy ~34%），其item difficulty分布极端——\n    从Level 1（algebra basics）到Level 5（competition math），跨越巨大的difficulty range。 Item_id仍为rank-1（42.1%）但低于MMLU，因为：(1)\n    lower overall accuracy增加了random guessing的比例， 膨胀residual到24.8%；(2) MATH的CoT generation比GSM8K更长更复杂（多步proof-like\n    reasoning）， 使temperature×item interaction达到10.4%——在高temperature下，长推理链的任何一步都可能diverge，\n    且这种sensitivity是item-specific的（Level 5 problems的长推理链比Level 1的短计算更sensitive）。 Temperature主效应也最高（3.8%），因为MATH的generation\n    length使sampling temperature的cumulative effect更显著。 G current practice仅0.24——所有benchmark中最低——意味着MATH\n    evaluation的reproducibility最差。 达到G≥0.90需要1100 items + 4 prompts + 3 seeds，是MMLU所需的~3倍evaluation\n    budget。 这个发现有strong policy implication：reasoning benchmark的evaluation标准需要比classification\n    benchmark更严格。\n\n    '\n  tables:\n  - name: 'Table 12: Full Cross-Benchmark Variance Summary (5 benchmarks)'\n    columns:\n    - Benchmark\n    - Accuracy\n    - item_id %\n    - Residual %\n    - Temp×Item %\n    - G (current)\n    - Items for G≥0.90\n    rows:\n    - - MMLU\n      - 0.668\n      - 58.4\n      - 16.8\n      - 5.8\n      - 0.34\n      - 600\n    - - ARC-Challenge\n      - 0.597\n      - 55.1\n      - 18.2\n      - 5.4\n      - 0.32\n      - 650\n    - - HellaSwag\n      - 0.712\n      - 52.7\n      - 19.5\n      - 6.2\n      - 0.36\n      - 550\n    - - GSM8K\n      - 0.583\n      - 48.7\n      - 21.4\n      - 8.9\n      - 0.29\n      - 800\n    - - MATH\n      - 0.342\n      - 42.1\n      - 24.8\n      - 10.4\n      - 0.24\n      - 1100\n  figures_description:\n  - 'Fig 15: 5-benchmark stacked bars排序by task difficulty，展示清晰的gradient：task越难→item_id越低、residual和temp×item越高。'\n  - 'Fig 16: D-study projection curves for 5 benchmarks overlay，MATH曲线最右（需最多evaluations达G≥0.90）。'\n  analysis: MATH提供了variance structure的\"stress test\"。Item_id在最extreme条件下仍为rank-1（42.1%），\n    但task difficulty明显调节了variance decomposition的profile。5个benchmark展现了清晰的gradient：\n    task difficulty ↑ → item_id share ↓, residual ↑, temperature×item ↑, G current\n    practice ↓。 这个gradient本身是publishable finding：它量化了为什么reasoning benchmark的evaluation更不稳定，\n    并给出了task-specific的reproducibility budget。\n",
      "numLines": 885,
      "startLine": 1,
      "totalLines": 885
    }
  },
  "sourceToolAssistantUUID": "0c2686d6-0a9e-4401-b99f-2c9f12aca353",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T22:24:07.620Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UCAtqmbYKYEBWgVmwkHvc8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "374e8ab7-01a4-47d0-83d0-252ce74a56b2",
  "isSidechain": false,
  "requestId": "req_011CbEbyqCycwvvzbxgP33t8",
  "type": "assistant",
  "uuid": "074394ac-f93c-4673-8c0e-16c37f482e1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EiQFaxDbscb7ExyuU7rbVD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4881,
      "cache_read_input_tokens": 23802,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 23802,
          "cache_creation_input_tokens": 4881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4881
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

_source line 19 · 2026-05-20T22:24:07.840Z_

<details open><summary>🔧 Tool call — Read · `toolu_019BoRds8rxALHNmpuFh3SV3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260520T190053/meta.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "074394ac-f93c-4673-8c0e-16c37f482e1d",
  "isSidechain": false,
  "requestId": "req_011CbEbyqCycwvvzbxgP33t8",
  "type": "assistant",
  "uuid": "745ba392-db2a-4661-867e-a15b5f1e6c12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EiQFaxDbscb7ExyuU7rbVD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4881,
      "cache_read_input_tokens": 23802,
      "output_tokens": 380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 380,
          "cache_read_input_tokens": 23802,
          "cache_creation_input_tokens": 4881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4881
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Cross-benchmark gradient clear and monotonic; all three claims hold as framed; AAAI submission proceeds without claim weakening 核心假设：['Item dominance on MM…",
  "leafUuid": "acd46e52-72a1-4587-a606-1cb48d42c0ed",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "G-theory variance decomposition across LLM benchmarks",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30"
}
```

---

### Tool result

_source line 22 · 2026-05-20T22:24:08.196Z_

<details><summary>↩ Tool result · reported error · `toolu_019BoRds8rxALHNmpuFh3SV3`</summary>

```text
File content (44998 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "745ba392-db2a-4661-867e-a15b5f1e6c12",
  "isSidechain": false,
  "promptId": "c295c0c9-7475-4ab1-87e4-a49b6b5cf1ca",
  "type": "user",
  "uuid": "fcd6397b-8304-437f-990e-e778ff10c8f7",
  "toolUseResult": "Error: File content (44998 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "745ba392-db2a-4661-867e-a15b5f1e6c12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23 · 2026-05-20T22:24:08.236Z_

````json
{
  "parentUuid": "fcd6397b-8304-437f-990e-e778ff10c8f7",
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
  "uuid": "6da77325-fec3-4734-9274-1c8b95cc4149",
  "timestamp": "2026-05-20T22:24:08.236Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Assistant

_source line 24 · 2026-05-20T22:36:31.288Z_

<details><summary>Logged reasoning block</summary>

```text
I now have the complete first dream's "best" tier experiment data. The user wants me to generate a new, revised version based on the updated Phase 1 definitions for the "best" tier. Let me compare what's changed:

The key definitions for "best" tier:
- Cross-benchmark gradient clear and monotonic
- All three claims hold as framed
- AAAI submission proceeds without claim weakening

Core assumptions:
1. Item dominance on MMLU replicates at 50-60% (binary) across 3 independent 200-item samples (exp-001b CV<15%)


2. The cross-benchmark ordering should show MMLU with the highest item variance share, then ARC-Challenge, HellaSwag, and GSM8K in descending order
3. For GSM8K and MATH, item dominance drops significantly to 20-30%, while seed and temperature interactions rise to 15-25%
4. The infrastructure and methodology interaction stays below 1% across all benchmarks in the follow-up experiments
5. Multi-hardware validation confirms that hardware and methodology don't interact meaningfully, staying under 1%
6. When treating model as a factor in the analysis, the model-item interaction ranges from 5-15% and reduces the residual variance, though item_id still dominates on knowledge-focused benchmarks
7. Bootstrap confidence intervals with 1000 resamples show non-overlapping ranges across benchmark clusters, confirming the item_id effect is statistically robust
8. The D-study projections indicate distinct optimal designs: MMLU requires 400+ items while GSM8K needs 10+ seeds, and I'm seeing the metric ranges cluster distinctly by benchmark type and interaction pattern is fundamentally different from my earlier model—GSM8K's item variance drops dramatically to 18-30% instead of nearly 50%, while the cross-benchmark gradient becomes much steeper and monotonic across MMLU, ARC, HellaSwag, and GSM8K. The seed and temperature interactions with items are now much larger at 15-25%, model effects are explicitly factored in at 5-15%, and the D-study requirements shift significantly, needing fewer items for MMLU but the same range for GSM8K.

Now I'm noticing something counterintuitive—if GSM8K's item variance is so much lower, why does it need fewer items to reach G≥0.90? That suggests the lower item variance is actually working in my favor, reducing the generalization penalty. of the total variance — the G coefficient depends on what variance is "universe score variance" vs "error variance." If item dominance is low but seed×item and temp×item are high, then the error variance from items is relatively smaller, and the G coefficient from items alone might be higher (since less variance is attributable to items). 

Actually wait — G coefficient relates to the ratio of universe score variance to total variance. The universe score is the object of measurement. If we're measuring models, then:
- σ²(model) / [σ²(model) + σ²(error)]
- Where σ²(error) includes item, prompt, seed, temp, and their interactions

Actually in G-theory for LLM evaluation, items ARE the object of differentiation in many setups. Let me reconsider...

Actually, thinking about this more carefully: the G coefficient for binary correct scoring on GSM8K is higher than on MMLU, which makes sense because item variance is lower on GSM8K — less item variance means less error from item sampling, so the measurement generalizes better. That's why GSM8K needs fewer items to reach G=0.9 but more seeds instead, since seed and temperature interactions with items are driving more variance there. MMLU, on the other hand, has much higher item variance, so it needs more items to stabilize the measurement, but the seed and temperature effects are more contained. This is a completely different story from what I initially thought — the key insight is that MMLU demands more items while GSM8K demands more seeds.

Now I need to think through what experiments are actually planned. Looking at the list, none of these have been run yet beyond the MVP stage, so I'm predicting outcomes for:
- exp-001: Full-scale MMLU precision study
- exp-001b: Item resampling stability
- exp-002: Multi-benchmark (GSM8K, ARC, HellaSwag)
- exp-003: Multi-hardware
- exp-004: Comprehensive analysis (model-as-facet, bootstrap CIs, D-study)
- exp-005: 14B models
- exp-006: Fine-tuning G-study
- exp-007: LayerCast
- exp-008: MATH benchmark

The central finding I'm building toward is that a universal reproducibility recipe doesn't exist — the cross-benchmark gradient is steep and monotonic, and that's the real headline. Let me now work through each experiment's predicted outcomes systematically.

For exp-001, I need to be precise about the item_id variance on MMLU. The best-tier assumptions put it between 0.48 and 0.62, and the MVP found 0.584. But I need to distinguish between what exp-001 itself will show (pooled analysis across 4 models) versus what exp-004 will reveal when breaking down model-as-facet effects separately.

The key insight is that when model×item interaction is extracted in exp-004 (estimated at 5-15%), some of that variance was previously being absorbed into item_id in the pooled analysis. So exp-001's item_id estimate will be inflated compared to exp-004's. I should expect exp-001 to show item_id around 0.55, while exp-004 will show a lower item_id (0.48-0.50) once the model×item interaction is properly isolated.

Now looking at the metric range [0.48, 0.62] for item_id_variance_mmlu_binary—this likely spans from the lower bound after extracting model-as-facet effects up to the upper bound from single-model estimates. The assumption about 50-60% item dominance in exp-001b (single model) sits at the higher end of this range, while the multi-model decomposition in exp-004 brings it down toward 0.48-0.52.

Let me settle on consistent estimates: exp-001 pooled across 4 models gives item_id around 0.56, exp-001b with a single model across 3 samples lands near 0.54 with low variance, and exp-004 with model-as-facet yields item_id around 0.49 with model×item interaction at 0.10. For exp-002 across multiple benchmarks, the picture shifts significantly—GSM8K item_id drops to around 25%, while ARC and HellaSwag show different patterns than the earlier estimates of 48.7% and 55.1%.

Now I'm checking whether the new gradient across benchmarks makes sense: MMLU at 56%, ARC at 42%, HellaSwag at 34%, and GSM8K at 25% gives a spread of 31 percentage points, which fits the target range of 25-40pp. For GSM8K specifically, the item_id variance around 25% with seed×item and temp×item interactions each contributing 15-25% seems reasonable. Now I'm filling in the remaining components and making sure everything adds up to 100% — temperature contributes 3.8%, prompt 3.2%, seed 2.1%, with smaller contributions from precision interactions, ordering, and infrastructure effects.

Looking at the G coefficient values for GSM8K, I'm noticing the range [0.45, 0.65] is substantially higher than the previous estimate of 0.29 under current practice, which suggests the measurement conditions have changed significantly or the definition of what we're measuring has shifted. σ²(item) + Σ(error terms)/n_levels]

So the G coefficient represents how reliable a single score is given the variance decomposition and fixed conditions like 1 prompt and 1 seed. Since item_id accounts for about 58% of variance, even sampling 200 items leaves substantial error from item sampling, which is why G stays relatively low despite the large sample size.

For GSM8K, the situation flips — item variance is only 25%, but seed×item and temp×item interactions each contribute around 16-18% of variance. When I'm stuck with 1 seed and 1 temperature, these interaction terms become massive error sources that can't be reduced by sampling more items, which should actually push G lower than the MMLU case, not higher.

But wait, looking at the reference values again — g_correct_gsm8k is [0.45, 0.65], which is actually higher than g_correct_mmlu at [0.3, 0.4]. That suggests these might be measuring something different: the G coefficient under a full factorial design where all prompts, seeds, and temperatures are varied. Under that scenario, the interaction terms get averaged out across many conditions, so even though they're individually large, their contribution to overall error shrinks. That would explain why GSM8K's G is higher despite the larger interaction variance — the full design effectively neutralizes those interaction effects. The MVP's G coefficient of 0.357 for MMLU under the full factorial design aligns with the [0.3, 0.4] range, while GSM8K's higher [0.45, 0.65] range reflects its lower item variance making the universe score more reliably estimated. Now I can map out the D-study predictions: MMLU requires 350-500 items to reach G≥0.90, while GSM8K needs fewer items but more seeds to achieve the same reliability threshold.

Writing YAML output... Let me think through each experiment carefully:

### exp-001: Full-scale MMLU precision study
- 4 models × 3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings × 200 items
- item_id: ~0.56 (pooled, before model-as-facet)
- Engine confound fix: precision main → ~0.3%, precision×item → ~1.8%
- All 4 models show item_id as rank-1
- G (full design) ≈ 0.36

### exp-001b: Item resampling stability
- 3 independent 200-item samples, 1 model
- item_id replicates at 50-60% across all 3 samples
- CV < 15%, with mean around 0.55 and SD of 0.055, suggesting a range of roughly 0.51-0.59

### exp-002: Multi-benchmark
- GSM8K item_id: ~0.25
- ARC item_id: ~0.42
- HellaSwag item_id: ~0.34
- Clear gradient across benchmarks: MMLU(0.56) > ARC(0.42) > HellaSwag(0.34) > GSM8K(0.25), a 31-point spread

Looking at the variance components, GSM8K shows item_id at 25% with temperature interactions at 18.2% and seed interactions at 15.8%, while ARC's item_id dominates at 42% with prompt interactions contributing 12.5%.

HellaSwag falls in the middle with item_id at 34%, temperature interactions at 14.2%, and seed interactions at 12.6%.

### exp-003: Multi-hardware
- Hardware effects are minimal: hardware×methodology < 1%, hardware main ~0.5%, hardware×item ~1.5%
- Direct infrastructure×methodology interactions stay below 0.8%

### exp-004: Comprehensive analysis
- When treating model as a facet, model×item accounts for 5-15% of variance (~10% on average)
- After extracting model effects, item_id remains the dominant factor at ~0.49

### exp-005: 14B models
- The patterns hold across larger models, with item_id still the primary variance driver

### exp-006: Fine-tuning
- item_id drops to 37-45% but stays dominant
- Seed and learning rate become more influential factors

### exp-007: LayerCast
- This approach has minimal impact on precision variance

### exp-008: MATH
- item_id drops further to ~20% since MATH requires more reasoning
- Temperature and seed interactions become more prominent, aligning with the assumption that item dominance decreases to 20-30% on reasoning-heavy benchmarks

Now I'm working through the complete YAML construction, making sure all the variance components are internally consistent across the benchmark gradient. The ordering should flow from MMLU down through ARC-Challenge, HellaSwag, and GSM8K, with MATH extending even further as the most reasoning-intensive task. I need to recalculate the G coefficients carefully for the full factorial design across all conditions. prompts/seeds estimate the universe score? With G=0.357 in the MVP, that means my current sample only captures about 36% of the true variance, so the measurement isn't very reliable. For MMLU where items account for 56% of error, even sampling 200 items from ~14K introduces substantial error, and since I'm only using one prompt and one seed, all that variance flows directly into my measurement error — the G coefficient would be quite low, showing how much the observed score underestimates the true universe score.

For GSM8K where items are only 25% of the error, the full design with multiple prompts, seeds, and temperatures changes things significantly. Those interaction terms like prompt×item and seed×item get divided down by the number of levels in each factor, so the sampling error shrinks considerably. Since the item variance itself is smaller to begin with, the universe score variance becomes relatively larger compared to the reduced error, which should push G higher.

Now I'm working through the actual G-theory formula to make sure I'm applying it correctly to these experimental designs. In a crossed design like person×item×rater, the coefficient depends on how you partition the variance components and what you're dividing by. I need to be more careful about which variance components go in the numerator versus the denominator, especially when dealing with pooled analyses across multiple experimental factors. LLM evaluation, if "person" = model, "item" = test item, and we have multiple facets:
- σ²(model) / [σ²(model) + σ²(model×item)/n_items + σ²(model×prompt)/n_prompts + ...]

But in many of these experiments, model is POOLED (not a facet), so the G coefficient might be:
- σ²(universe_score) / σ²(observed_score)

Where the "object of measurement" is the score itself (not differentiating models).

I think for this paper, G represents: "if I repeat this evaluation with different items/prompts/seeds, how consistent will the score be?" This is a relative G coefficient.

Now I'm working through the actual variance components with the current experimental setup—one prompt, one seed, 200 items on MMLU—and factoring in all the interaction terms. The math is getting unwieldy, so let me just anchor to the concrete numbers from the spec and make sure everything's internally consistent. I've got G coefficients around 0.36 for MMLU and 0.55 for GSM8K under their respective full designs, and I can use those to figure out what sample sizes I'd need to hit G≥0.90. MMLU needs way more items (420) while GSM8K is more constrained by seeds and temperature variations. Now I'm ready to write out the full YAML configuration, making sure all the parameters align. amplifies interaction effects. The same item gives different results with different temperatures and seeds because the reasoning path can fork at many points. On knowledge tasks like MMLU, items are either known or not — less sensitivity to generation randomness.

Let me calibrate the metric ranges for ARC and HellaSwag to fit the monotonic gradient I'm targeting. ARC sits around 0.42 and HellaSwag around 0.34, which gives me the spread I need: MMLU at 0.56 down to GSM8K at 0.25 — a clean 31-point gap that stays within my target bounds.

Now I'm working through the variance decomposition for ARC to understand how the interaction effects shift across the benchmark difficulty spectrum. Looking at the variance patterns across these benchmarks, I'm seeing a clear gradient emerge—as tasks shift from factual recall to reasoning, item-level interactions with temperature and seed become increasingly important while the main item effect diminishes. Now I'm analyzing what happens when I add model as a crossed factor to the MMLU data, looking at how much variance comes from overall model differences versus which specific items each model struggles with. 3% (CI: 46-52%) on MMLU versus 25% ± 4% (CI: 21-29%) on GSM8K—these confidence intervals don't overlap, confirming the gradient is statistically significant. I'm double-checking whether the bootstrap CI widths represent full ranges or half-widths, and treating them as full widths: MMLU shows a 6 percentage point spread while GSM8K shows 8 percentage points. The non-overlapping ranges validate assumption 7 that bootstrap CIs on item_id exclude zero and remain distinct across knowledge benchmarks like MMLU and ARC.

Now I'm mapping out how the clusters might be organized—knowledge benchmarks (MMLU at 46-52%, ARC at 38-46%) versus reasoning benchmarks (GSM8K at 21-29%, HellaSwag at 30-38%), with ARC's lower bound just barely touching HellaSwag's upper bound at 38%. The inter-cluster separation suggests a clear pattern even if the exact grouping remains slightly ambiguous.

Let me refine the confidence intervals to get cleaner separation: MMLU around 56% with a tighter range, ARC at 42%, HellaSwag at 34%, and GSM8K at 25%, which creates two distinct clusters with minimal overlap between the knowledge and reasoning tiers. %, 44%] — width 4pp
- HellaSwag: 34% ± 2.5% = [31.5%, 36.5%] — width 5pp
- GSM8K: 25% ± 2% = [23%, 27%] — width 4pp

These maintain clean separation across all benchmarks, with MMLU's lower bound well above ARC's upper bound and that pattern continuing down the line. After applying the model-as-facet adjustment in exp-004, MMLU drops to 49% [46%, 52%] but still stays clear of ARC's range. Rather than keep refining these intervals, I should just move forward and write out the YAML configuration with these finalized numbers, then work through the D-study projections for exp-004.

For MMLU, the current practice setup yields a generalizability coefficient around 0.36, but reaching 0.90 would require roughly 420 items combined with 3 prompts and 2 seeds—showing that item count is the dominant factor. GSM8K performs better at 0.55 under current practice since it has lower item variance, though I need to clarify whether the g_coefficient values I'm seeing come from the full MVP design or just the current practice conditions.

Looking at the full experimental design for exp-002, GSM8K's g_correct range of 0.45-0.65 is notably higher than MMLU's 0.3-0.4 because the dataset has less inherent item variance and the interactions between seeds, temperatures, and items get averaged out across the broader sampling. For the D-study projections, MMLU needs 420 items to hit G≥0.90 since items are the bottleneck, while GSM8K only needs 150 items because the seed and temperature variance is more manageable there.

The key insight is that GSM8K is fundamentally seed-limited while MMLU is item-limited. Under current practice with just one prompt, one seed, around 200 items, and a single temperature, MMLU's generalizability is severely constrained by item sampling error, whereas GSM8K would benefit much more from additional seeds to stabilize performance estimates. I'm realizing the G coefficient would be quite low for GSM8K under current practice—probably below 0.3—which contradicts the expected range of 0.45-0.65 from the full design. Let me reconsider how these error components actually combine: with only one seed and one temperature setting, the interaction effects between seed×item, temp×item, and prompt×item all contribute their full variance to the error rather than being averaged out, whereas item variance gets diluted across 200 items. I need to think through the G-theory calculation more carefully to understand how these facets actually combine. G = 1 - (σ²(error) / σ²(observed))

Where the error variance encompasses all the components that shift when we resample—items, prompts, seeds, and their interactions—while the observed variance is the total. So under the current MMLU setup, G is really measuring how stable the score would be if we ran the evaluation again with a different sample of items and different random seeds.

Looking at the spec numbers, the full design gives us G = 0.36 for MMLU and G = 0.55 for GSM8K, but when we're only using one prompt and one seed with about 200 items, those numbers drop significantly—MMLU falls to around 0.22 and GSM8K even lower to 0.15 because the interaction effects become much larger. Let me check what the previous analysis had for these estimates to make sure I'm being consistent. i = 0.72
- g_6p6s200i_3t4o = 0.78

So the full design G is 0.78, not 0.34. And g_correct_mmlu in the spec is [0.3, 0.4] which matches the FULL design G of 0.357 from MVP... 

Wait, the MVP had G = 0.357 under what design? Let me re-check: the MVP used 108 conditions per item (6 prompts × 6 seeds × 3 temps × 3 precisions), with 50 items. 

Actually, in the MVP report it says g_coefficient_correct: 0.357. This was computed with 50 items × 108 conditions = 5400 total records. 

In the MVP analysis, the G coefficient might represent the reliability of the score for a single model under the full design with all facet levels. With 50 items and all the interaction terms, G = 0.357.

Now I'm realizing the confusion: "g_current_practice_1p1s200i" isn't the actual study G — it's a D-study projection showing what reliability would look like if a practitioner only used 1 prompt and 1 seed with 200 items. The actual study uses the full 6 prompts × 6 seeds × 3 temperatures × 4 observation types, but the D-study lets me ask what-if questions about simplified designs.

So the full study G should be higher than 0.357, and the D-study projection for minimal conditions (1p, 1s) would be lower. The GSM8K dataset shows even higher G values because averaging across 200 items reduces the relative contribution of seed and temperature variance.

For the current practice scenario with just 1 prompt, 1 seed, and 200 items, I'm getting much lower G coefficients — around 0.22 for MMLU and 0.18 for GSM8K — since interactions dominate without the averaging benefit of multiple seeds and temperatures. Rather than deriving these from first principles, I'll stick with the spec's ranges and pick values that form a coherent narrative across both datasets.

Now I'm settling on specific variance component values that stay within the specified ranges: item effects ranging from 0.56 down to 0.21 across the benchmarks, g-factors around 0.36-0.55 for the full design, model-by-item interactions at 0.10 for MMLU, and infrastructure/hardware effects staying below half a percent. I'm also noting the bootstrap confidence intervals should be 4-6 percentage points wide and the item resampling coefficient of variation sits at 8%.

For the generalizability study, I need 420 items for MMLU to reach a G coefficient of 0.90, and 150 items for GSM8K with 10 additional random seeds. The item_id variance across the three independent samples in exp-001b shows a coefficient of variation between 3-12%, which means if the mean item effect is 0.55, the standard deviation would be around 0.044, so individual samples might cluster around 0.52-0.58.

Writing the YAML configuration... ound fix
- Core: item_id ≈ 56%, precision collapses post-fix
- 4 models all show item_id rank-1
- G coefficient (full design): 0.36

**exp-001b**: Item resampling stability
- 3 × 200-item samples, CV = 8%
- item_id across samples: 0.53, 0.56, 0.58
- Confirms item dominance is not artifact of specific item sample

**exp-002**: Multi-benchmark → THE headline experiment
- GSM8K item_id: 25%, temp×item: 18%, seed×item: 16%
- ARC item_id: 42%
- HellaSwag item_id: 34%
- Clear monotonic gradient
- GSM8K's G (full design): 0.55

**exp-003**: Multi-hardware
- hardware×methodology total: 0.4%
- hardware×item: 1.5% (small but real)

**exp-004**: Comprehensive analysis
- When I treat model as a facet, model×item interaction jumps to 10% and item_id drops to 49%, but the bootstrap confidence intervals stay tight and non-overlapping across clusters. The D-study results show I'd need 420 items for MMLU but only 150 items plus 10 seeds for GSM8K—the optimal allocation really does depend on which benchmark I'm working with.

**exp-005**: 14B extension
- The pattern holds across larger models with item_id still dominant, though DeepSeek-R1 shows slightly different behavior given its reasoning-focused architecture.

**exp-006**: Fine-tuning G-study
- item_id remains rank-1 but weakens, with seed and learning rate becoming more influential than prompt and temperature.

**exp-007**: LayerCast
- Minimal impact.

**exp-008**: MATH benchmark
- item_id accounts for roughly 21%, with temperature×item and seed×item interactions even more pronounced, requiring the most evaluations to reach G≥0.90.

Now I'm writing out the full YAML specification with tables and figures. I need to go back and include exp-001b since it wasn't in the original plan, and I should double-check exp-002's design—the factorial is 4 models × 2 precisions × 6 prompts × 6 seeds × 2 temperatures × 4 orderings across three benchmarks, which gives 2304 conditions per benchmark.

Let me verify the total record count: 2304 conditions × 200 items per benchmark × 3 benchmarks = 1,382,400 total records. I'm confirming the calculation is correct at 460,800 per benchmark, and for exp-001 it's 1,036,800 which matches the previous reference. Now I'm ready to write out the YAML configuration.

For the narrative guidance in the "best" tier, I need to emphasize the cross-benchmark gradient as the primary finding—showing how reproducibility drops dramatically from MMLU to GSM8K—and highlight that the universal reproducibility recipe is actually illusory. I'll incorporate the model-as-facet framing as a clean analytical lens and note that D-study budgets need to be benchmark-specific since MMLU focuses on item variance while GSM8K's variance is driven more by seeds and temperature interactions.

Writing YAML configuration...

Now I'm thinking through whether the GSM8K variance decomposition makes conceptual sense. The 25% from item selection is much lower than MMLU's 56% because GSM8K's multi-step reasoning is heavily influenced by sampling at each step—different seeds produce different reasoning paths, and this effect varies dramatically across items depending on their difficulty. The 18% from temperature-by-item and 16% from seed-by-item interactions capture this sensitivity, while the residual (likely 12-16%) accounts for higher-order interactions and irreducible stochasticity from token sampling.

For the benchmark accuracy expectations, I'm settling on MMLU around 67%, ARC-Challenge at 60%, HellaSwag at 72%, GSM8K at 58%, and MATH at 34%—these feel right for 7-9B instruction-tuned models in this timeframe. Now I need to structure what goes into each experiment's expected results: total records, accuracy metrics, full variance decomposition, G coefficient, and key comparison metrics, along with specifying which tables and figures each experiment should include. I should stop overthinking and just start writing this out, though I want to clarify whether exp-002 should include text_exact_match analysis or if that's only for a later experiment.

Looking at the benchmark types in exp-002, GSM8K requires answer extraction and numerical comparison while ARC-Challenge and HellaSwag are multiple choice, but all three ultimately reduce to binary correct/incorrect scoring. I need to think through how exp-004 handles text-based evaluation as well. I need to work through the G coefficient calculation more carefully for GSM8K under the full experimental design. The universe score represents the model's true performance on the benchmark, while error encompasses all the variance from items, prompts, seeds, temperature, precision, ordering, and their interactions—each scaled by how many levels we're averaging across. For the exp-002 setup with 200 items, the item variance contribution drops to about 0.125%, and I'm calculating how the prompt variance factors in at the 6-level division.

Now I'm computing the remaining variance components: prompt contributes roughly 0.53%, seed about 0.35%, temperature 1.9%, precision 0.15%, and ordering 0.2%. The two-way interactions are much smaller—prompt×item interaction is negligible at 0.0086%, while temp×item is slightly larger at 0.046%.

Summing these up, the total error across all factors comes to about 3.3%, which would suggest a universe score around 96.7%—though that figure seems suspiciously high and might indicate an issue with how I'm aggregating the variance components.

Let me reconsider the G-theory framework here. The variance components I've estimated don't directly translate to percentages of total variance the way I was treating them. In generalizability theory, the G coefficient actually measures reliability by comparing the object of measurement's variance against the sum of error components weighted by their facet levels. Since we're evaluating a single model rather than comparing across multiple models, the universe score—what the model would achieve if we could average across all possible items, prompts, and seeds—needs to be computed differently, and I'm realizing the variance of the universe itself might actually be zero in this setup.

That can't be right though, since it would give G = 0. I think what's actually happening here is that the G coefficient in this context is measuring how much of the observed score variance comes from the facets we're deliberately varying (like items or prompts) versus random error. So it's really about whether the score differences we're seeing are reliable or just noise. In LLM evaluation specifically, the question becomes: if I evaluate on this particular set of items and prompts, how well will those results generalize to the broader universe of all possible evaluation items?

Rather than deriving this from first principles, I should just pull the actual values from the spec—MMLU's G coefficient is around 0.36 and GSM8K's is around 0.55 based on their full design analysis. I can use those as my baseline numbers and then work out the D-study projections from there.

Now I'm looking at what sample sizes would get me to G≥0.90: MMLU needs 420 items with 3 prompts and 2 seeds, while GSM8K requires 150 items with 3 prompts and 10 seeds. These are the concrete targets I need to include in the YAML.

I should also make sure I'm covering all the sub-analyses mentioned in exp-004—the model-as-facet reanalysis, bootstrap confidence intervals, D-study projections, REML versus Henderson method comparison, logprob-based scoring, ranking stability analysis, and higher-order interaction estimation. For the REML versus Henderson comparison, I expect them to be fairly similar with REML being slightly more conservative, so I'll note that in the predictions.

For logprob scoring, since it's continuous rather than binary, I'd expect different patterns to emerge—item effects might be lower because logprobs capture graded information instead of hitting a binary threshold. Ranking stability should hold up well in the best tier since model effects should dominate over precision and temperature effects. Higher-order interactions should stay small, under 3% of total variance, with the residual shrinking as I extract them.

Writing the YAML structure... Writing the YAML structure with variance decomposition tables... Looking at the variance breakdown from the MVP experiment with 50 items, I see item_id dominates at 58.4% with residual at 17.6%, but there's a confounding issue where precision×item accounts for 7.2% of variance that should be separated out. After fixing this confound in the larger 200-item experiment, that precision×item variance drops to around 1.8%, with the freed variance redistributing mostly back to residual and item_id, though the new ordering facet also claims some of that variance.

With the expanded dataset, the estimates stabilize considerably. Looking at the realistic numbers from the MMLU experiment with 4 pooled models, item_id remains the dominant source at 56%, residual sits at 17.1%, and the interaction effects are now properly separated—prompt×item at 6.2%, temp×item at 5.9%, seed×item at 3%, with precision×item and ordering×item each under 2%. The main effects are all quite small, with precision barely registering at 0.3%.

For the paper, I should focus on the largest components rather than trying to report all 22 possible variance sources. The key story is that item difficulty dominates, followed by the residual, then the critical interactions between items and the experimental manipulations. effects subtotal: 4.8%
- All direct infra×method: 0.4%
- Residual: 20.4%

That gives me 100% total, which checks out. Though 20.4% residual seems higher than the MVP's 17.6%, so let me think through whether that's actually expected. With more facets like ordering and a larger item set, I'd expect more variance to be captured, which should lower the residual rather than raise it. Let me recalculate the MMLU breakdown more carefully.

After working through the full variance decomposition with all six facets, I'm getting a residual of 20.7%, which is still elevated. That's reasonable for a complex design where higher-order interactions get absorbed into the residual term, but I should simplify this table to make the key patterns clearer.

Now I'm looking at the GSM8K results to see how the variance breakdown compares across datasets. Looking at the variance breakdown for ARC-Challenge, item identity dominates at 42%, which is much higher than GSM8K. The interaction effects are smaller here too, suggesting that on multiple-choice questions, the specific question matters far more than the hyperparameters, whereas reasoning tasks show more systematic sensitivity to prompt and temperature choices. I'm working through the variance decomposition more carefully now, making sure all the components add up to exactly 100%. Let me recalculate by listing out the main effects and interactions separately, then use a residual term to capture whatever's left unaccounted for. Now I'm adjusting the variance decomposition to shift some of the residual into item-conditional interactions, which gives a cleaner story for the paper while keeping the total variance accounted for reasonable at 78.3%. Generating comparison table...

The residual pattern across benchmarks isn't monotonic, which suggests I need to reconsider the decomposition. GSM8K's lower residual makes sense given the stronger interaction effects, while MMLU's higher residual indicates more scattered unexplained variance. Let me refine the HellaSwag breakdown to better account for the ordering and precision interactions. I'm refining the ARC breakdown with the interaction terms, and the residual at 21.7% seems reasonable given the higher-order effects at play. Rather than chasing perfect monotonicity, I should focus on the clearest story for the paper—highlighting item_id as the dominant factor across all benchmarks. Let me lock in the final variance explained numbers: MMLU shows the strongest item effect at 56% with a G_full of 0.36, while ARC sits at 42% with 0.42, HellaSwag at 34% with 0.48, and GSM8K starting at 25%.

Checking these G values against the specification ranges confirms they're solid—MMLU and GSM8K both fall within their target bands, and the intermediate benchmarks fit the expected gradient. The 31 percentage point spread across benchmarks is well within the acceptable range. Now I'm working through the D-study projections to determine how many items we'd need to reliably achieve a generalizability coefficient of 0.90 on MMLU, which points to around 420 items paired with 3 prompts and 2 seeds as the optimal configuration.

For GSM8K, reaching that same threshold requires fewer items—about 150—but demands substantially more seeds, suggesting that reasoning-heavy tasks benefit from greater prompt and seed variation rather than item quantity. I'm interpolating similar requirements for ARC and HellaSwag based on their position between MMLU and GSM8K in terms of reasoning demands. The pattern emerging is that as tasks shift toward reasoning-intensive evaluation, the allocation strategy should prioritize seed diversity over raw item count.

Moving into the model-as-facet analysis for exp-004, I'm examining what happens when we treat the model itself as a crossed facet in the combined MMLU dataset across four models, which shows a main effect of roughly 2.

8% variance. The model×item interaction captures about 10.2% of variance—this represents the portion where different models succeed on different items, which previously was distributed across the item_id and residual components. The remaining model interactions with prompt, temperature, and seed are much smaller, suggesting that model differences are primarily driven by item-level variation rather than sensitivity to these other factors. After accounting for the model facet, the item_id variance drops from 56% to about 49%, and residual shrinks from 20.7% to 14.5%, with the extracted variance now attributed to the model interactions.

Now I'm checking whether these estimates are reasonable. The item_id component at 49.2% falls within the expected range and remains the dominant source of variance. The model×item interaction at 10.2% is also within plausible bounds. Looking at the bootstrap confidence intervals, item_id shows consistent estimates across datasets—49.2% on MMLU and 25% on GSM8K—with non-overlapping intervals, which confirms the estimates are stable. Comparing different estimation methods like REML and Henderson shows only minor differences, all under 2 percentage points, suggesting the results are robust. The logprob scoring approach provides a continuous measure that's more sensitive than discrete accuracy metrics.

For ranking stability, the precision and temperature variations don't cause models to flip positions, with rankings remaining stable across over 95% of conditions. The higher-order interactions account for about 5% of variance total, with the largest three-way interaction around 2%, and extracting these reduces the residual from roughly 20.7% down to 15.7%. I have enough information now to construct the complete YAML configuration, and I want to make sure the narrative guidance captures the key conceptual shifts in how we're framing the variance decomposition.

The main findings I'm emphasizing are that the benchmark gradient is steeper than initially expected, MMLU is fundamentally item-limited while GSM8K is seed-limited, and treating model as a facet cleanly separates the model×item interaction while keeping item_id as the dominant effect. Bootstrap confidence intervals give us the statistical rigor we need, and the analysis doesn't require any claim weakening—the AAAI submission is on track. For the specific exp-001b setup, I'm using three independent 200-item samples from MMLU with stratified sampling across seeds 0, 7, and 99, testing one model across three precisions, three prompts, three seeds, and two orderings, which gives 54 conditions per sample, and the item_id variance across the three samples shows a consistent upward trend from 0.53 to 0.58.

The coefficient of variation is well within acceptable bounds at 4.5%, and the item resampling CV of 0.045 falls comfortably in the expected range. With 10,800 records per sample and 32,400 total across all three samples, I have solid statistical power. Now I'm moving to write the YAML configuration with a flat dictionary structure for expected results and structured tables for presentation. I'm reconsidering the exp-001 baseline numbers slightly—the MVP found 58.4% item_id with 50 items and one model, but scaling to four models and 200 items might shift the pooled item_id estimate since different models will have varying agreement patterns.

I'm settling on 56.0% for the MMLU pooled item_id, which sits comfortably within the expected range. The slight decrease from the MVP's 58.4% makes sense because pooling across four models introduces model-specific variance that wasn't present with a single model, and the larger item set provides a more precise estimate. But I need to think through the confounding here—when model isn't a facet in exp-001, the model×item variance gets absorbed into the item_id estimate, which would actually inflate it relative to exp-004 where model is explicitly modeled.

Looking at exp-004's breakdown: item_id at 49.2% plus model×item at 10.2% gives 59.4% total item-related variance. In the pooled analysis, some of that model×item variance redistributes between item_id and residual depending on the correlation structure. My estimate of roughly 6-7% flowing to item_id and 3-4% to residual would put pooled item_id around 55.7%, which rounds to 56.0%—so that's internally consistent.

Now for the G coefficients across datasets: the item sampling error dominates for MMLU (56%/200 = 0.28%), which explains its lower G around 0.36, while GSM8K's smaller item variance (25%/200 = 0.125%) contributes less error. But GSM8K's main limitation isn't items—it's the temperature and seed main effects, which are much larger contributors to measurement error. To reach G≥0.90 on GSM8K, I'd need more seeds and temperature levels rather than more items, since the item error is already minimal. I'm realizing I need to reconsider how the G coefficient actually works in this context—it's the ratio of universe score variance to observed variance, and I should be more careful about what constitutes the "true" score versus measurement error.

Rather than deriving everything from first principles, I'll use the ranges from the spec and write out the full YAML with all nine experiments now.

For the G coefficient, I'm realizing the spec gives me the full-design values (around 0.36 for MMLU, 0.55 for GSM8K), and I can project what happens under current practice conditions using a D-study approach. The key insight is that MMLU's G stays relatively stable when you add items, but GSM8K's G drops significantly under current practice because the seed and temperature interactions fully contribute as error with only one seed and one temperature sampled. I'll use these projected values to show the reversal: current practice favors neither benchmark, but the full design shows GSM8K becoming more reliable than MMLU. I'm trying to reverse-engineer the G coefficient formula from the variance components, but I keep getting values that don't match the reported 0.36 for MMLU and 0.55 for GSM8K. I've tried several interpretations—treating items as the object of measurement, treating conditions as the object, computing it as ICC or Cronbach's alpha—but none quite land on those numbers. Rather than continue chasing the exact formula, I should just work with the empirical G values as given and focus on the D-study projections: how many items, prompts, seeds, and temperatures are needed to reach G≥0.90 for each benchmark, since that's what the experiment is actually measuring.

Writing YAML structure... about why the item_id performance drops so sharply on GSM8K compared to the baseline of 56%.

The distinction comes down to the nature of the tasks themselves. MMLU tests pure knowledge retrieval—you either know the answer or you don't—so item difficulty is fixed regardless of temperature, seed, or prompt variations. That's why item_id explains so much of the variance there. GSM8K is different though; the items involve multi-step reasoning, which means the same problem can be solved or failed depending on how the model approaches it.

With GSM8K, temperature and seed have massive effects because they change the reasoning path itself. A complex math problem might fail at one temperature but succeed at another, depending on which tokens get sampled. The interaction between temperature and item (18.2%) and between seed and item (15.8%) is huge because different items have different sensitivity to these generation parameters—simple problems stay correct regardless, but harder ones are fragile. This makes item_id itself smaller (25%) since so much of the difficulty is conditional on how the model generates its reasoning.

This pattern cascades across the benchmarks: MMLU's knowledge-based tasks show the strongest item effects, while GSM8K's pure reasoning tasks show the strongest parameter interactions, with ARC and HellaSwag falling somewhere in between based on how much retrieval versus reasoning they require.

Looking at the residuals though, I'm noticing something odd—GSM8K has the lowest unexplained variance (12.4%), but I'd expect it to be higher since chain-of-thought generation introduces more stochasticity and harder-to-model interactions.

Let me revise the GSM8K breakdown to account for this. I'm recalculating the variance components with a higher residual of 15.9% to better capture the irreducible noise from CoT generation, and I'm working through the full decomposition to make sure the numbers add up correctly.

Now I need to construct the complete YAML specification with bootstrap confidence intervals for each benchmark. I'm starting with MMLU and ARC, defining the point estimates and their 95% CI bounds for the major variance components like item difficulty, model-by-item interactions, and prompt effects.

Filling in the remaining benchmarks—HellaSwag and GSM8K—with their respective variance decompositions and confidence intervals. Then I'm verifying that the confidence intervals don't overlap between consecutive benchmarks, which confirms they're statistically distinct, and checking that all lower bounds stay above zero to ensure positive variance estimates.

Now I need to compare the item_id variance estimates between the earlier experiment (before extracting model×item effects) and the current one (after extraction) to make sure they're consistent with what I'd expect when removing that interaction term. Now I'm checking whether the model×item variance aligns with the spec range of [0.05, 0.15]—all my values fall within bounds. But I notice the difference between pooled and model-as-facet item difficulty should roughly equal model×item, though not exactly since some variance leaks into the residual. For MMLU, the 6.8% gap between pooled (56.0%) and model-as-facet (49.2%) is smaller than the 10.2% model×item effect, which suggests the model main effect and residual are absorbing the rest. I need to reconsider how the variance shifts when introducing model as a facet—the model-related components are pulling variance away from both item_id and the residual term, so I should calculate what's left in the residual by subtracting all the model contributions from the original pooled residual.

Now I'm ready to move forward with writing out the YAML configuration, and I want to make sure exp-001b is clearly defined as an item resampling stability test with three independent runs.

For exp-001b, I'm using three stratified 200-item MMLU samples with different seeds, testing a single model across 54 conditions per sample (combining precision, prompt, seed, and ordering variations), which gives me 32,400 total records. Looking at how item_id variance breaks down across the three samples—ranging from 52.6% to 56.2% with a coefficient of variation around 3.3%—this shows reasonable consistency in the item effect across different sample compositions. I'm checking whether the CV values are expressed as fractions or percentages—the spec says CV<15% for the criterion, but the range [0.03, 0.12] suggests a tighter constraint of 3-12%. My current 3.4% fits within both, so I'm adjusting the sample values slightly to stay comfortably in that range. I'm recalibrating the values since the reduced design with just Llama-3.1-8B should center around its per-model performance of 57.1%, and my adjusted samples of 53.6%, 58.2%, and 56.1% give a mean of 56.0% with a coefficient of variation of 4.1%, which still fits the acceptable range and keeps all values within the 50-60% band. I'm applying the scaling factor to each model's values, which gives me a range from 52.5% to 59.5%, but I realize the pooled analysis doesn't work that way—it's a weighted combination dependent on covariance structure, not just an average. So I'll set reasonable per-model item_id values directly instead.

Now I'm checking the coefficient of variation for the Llama-3.1-8B samples in exp-001b, aiming to keep it within the target range of 0.03 to 0.12. My initial samples gave me a CV of 2.9%, which is just below the threshold, so I'm adjusting the sample values to push the standard deviation higher and hit the target range more precisely.

With the adjusted samples at 52.8%, 57.2%, and 55.6%, I'm getting a mean of 55.2% and a CV of 0.040, which sits comfortably within the acceptable range. All three values fall within the 50-60% band, and the coefficient of variation is well below 15%, so the data looks solid. Now I'm ready to write out the YAML configuration and start planning the figures for the experiment.

I'm mapping out eight experimental figures to build toward the paper: a ground truth comparison, resampling stability check, the main stacked-bar benchmark visualization, a separability diagram, model decomposition with bootstrap confidence intervals and D-study curves, a 14B model comparison, inference versus fine-tuning analysis, precision mode comparison, and an extended five-benchmark gradient. For the final paper, I need at least four figures covering the problem setup, the signature benchmark results, D-study projections, and the separability test.

Now I'm verifying my variance decomposition numbers against the key assumptions. The cross-benchmark gradient holds as expected with MMLU showing the highest item variance share, followed by ARC-Challenge, HellaSwag, and GSM8K in descending order. For GSM8K and MATH, the item dominance has dropped into the 20-30% range while seed-by-item and temperature-by-item interactions have risen to the 15-25% band, which matches the expected pattern. I'm checking the infrastructure and methodology assumptions next. interaction remains <1% (binary) across all benchmarks"

All benchmarks: infra×method < 0.5% ✓

Assumption 5: "Multi-hardware crossing (exp-003) confirms single-GPU separability: hardware×methodology <1%"

exp-003 hardware×methodology: 0.3% ✓

Assumption 6: "Model-as-facet (exp-004) reveals model×item 5-15%, reduces residual, but item_id remains largest single component on knowledge benchmarks"

model×item MMLU: 10.2% ✓ (within 5-15%)
item_id after extraction: 49.2% > model×item 10.2% → item_id still largest ✓
Residual reduced: 20.7% → 12.0% ✓

On GSM8K, item_id accounts for 22.6% after extraction, which still dominates over temp×item at 18.2% and seed×item at 15.8%, confirming it remains the largest component across both benchmarks.

Assumption 7: "Bootstrap CIs (1000 resamples) on item_id share exclude zero and don't overlap across benchmark clusters"

All CIs above zero ✓
CIs non-overlapping between benchmarks ✓

Assumption 8: "D-study projections show clearly differentiated optimal allocations: MMLU needs 400+ items, GSM8K needs 10+ seeds"

MMLU: 420 items ✓ (>400)
GSM8K: 10

+ seeds ✓

All checks pass. Now I'm compiling the variance components for MATH to verify the pattern holds there too—item_id dominates at 21.0%, followed by temp×item at 20.8% and seed×item at 17.4%, with smaller contributions from prompt, ordering, and precision interactions.

The gradient across benchmarks checks out as expected: MMLU performs best at 56.0%, then ARC at 42.0%, HellaSwag at 34.0%, GSM8K at 25.0%, and MATH at 21.0%.

Now I need to reconsider the full experimental design for exp-008 to make sure I'm capturing all the factors correctly. I'm calculating the variance contributions under the full experimental design for MATH, and they're actually quite substantial—the temperature effect alone contributes 2.4% error, which is notably larger than GSM8K's. When I add up all the main effects and consider how they interact, MATH's total error budget might actually be higher than GSM8K's, which would push its G coefficient lower despite the smaller item-level variance. The interaction effects are substantial—temperature by item, seed by item, and prompt by item together account for nearly half the total error, which compounds the main effects. For MATH specifically, a D-study shows I'd need a much larger design with 120 items, 4 prompts, and 12 seeds to achieve a generalizability coefficient of 0.90 or higher. Looking at the full picture across all datasets, MATH and HellaSwag both land around 0.48, though for different reasons—HellaSwag has moderate item variance balanced against moderate interactions, while MATH has lower item variance but higher main effects that partially offset each other. Now I'm verifying the total record counts for each experiment by multiplying out all the factors — exp-001 comes to just over a million records, exp-001b is around 32,400, and I'm working through exp-002's calculation across the different benchmarks. Now I'm working through exp-007, which gives 172,800 runs, but I need to clarify that LayerCast is an additional precision condition that gets combined with exp-001 data rather than being standalone. For exp-008, I'm calculating 460,800 runs with a slightly different configuration using only 2 temperature settings instead of 3.

Before I write out the YAML configuration, I should verify that all the variance metrics fall within the specified best-tier ranges—checking MMLU, GSM8K, ARC, and HellaSwag values across both the pooled and model-as-facet conditions to ensure everything qualifies. Looking at the remaining benchmarks, the text-match metric comes in at 1.3% which fits within the target range, and I'm verifying the hardware-methodology interaction for exp-003 at 0.3%. The MMLU performance across experiments hits 0.102, the correctness metrics for MMLU and GSM8K are tracking at 0.36 and 0.55 respectively, both within their expected bounds.

Now checking the bootstrap confidence intervals across all datasets—MMLU, ARC, HellaSwag, and GSM8K all fall within the 0.03-0.08 range, and the resampling coefficient for exp-001b validates at 0.040. The D-study item requirements look solid too: 420 items for MMLU's g=0.90 and 150 for GSM8K both pass their checks. Everything validates, so I'm ready to generate the full YAML configuration.

I need to account for how the evaluation metrics differ across tasks—GSM8K and ARC use answer extraction and multiple choice selection respectively, but both ultimately score as binary correct/incorrect. The text-match metric is really only meaningful for MMLU where exact letter matching matters, though GSM8K's answer string comparison is a related form of text matching. Looking at the dual-metric breakdown from the MVP, item_id dominates the binary_correct variance for MMLU at 56%, while prompt×item interaction becomes more prominent in text_exact_match at around 38%. GSM8K shows item_id at 25% for binary_correct with temperature and seed interactions playing larger roles, and the text-match variant likely amplifies the prompt×item sensitivity due to answer formatting differences. I'll structure the analysis to capture these metric-specific patterns.

Writing YAML experiment definitions...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6da77325-fec3-4734-9274-1c8b95cc4149",
  "isSidechain": false,
  "requestId": "req_011CbEbzMuSN9caiuCJY27HN",
  "type": "assistant",
  "uuid": "8439739c-1316-4c65-a636-665c6f416340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMUVGyQV7GG74d57fhCF2v",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33573,
      "cache_read_input_tokens": 28683,
      "output_tokens": 60425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 60425,
          "cache_read_input_tokens": 28683,
          "cache_creation_input_tokens": 33573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33573
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

_source line 25 · 2026-05-20T22:42:36.113Z_

Now I have all the context needed — the first dream's predictions, MVP data, and the new best-tier definition with significantly different assumptions (especially the much steeper cross-benchmark gradient and shifted D-study allocations). Let me generate the updated predictions.

```yaml
tier: best
narrative_guidance: >
  Cross-benchmark gradient是primary finding且远比第一版dream更陡峭：
  MMLU(56%) > ARC(42%) > HellaSwag(34%) > GSM8K(25%)，spread 31pp。
  reasoning tasks的CoT stochasticity将massive方差从item_id转移到seed×item和temp×item（各15-25%），
  这解释了为什么prior single-benchmark studies得出看似矛盾的结论。
  
  核心升级："optimal evaluation protocol reverses across task types"——
  MMLU是item-limited（需420 items for G≥0.90），GSM8K是seed-limited（需10+ seeds for G≥0.90）。
  "Universal reproducibility recipe is illusory"被数据完全支持，且比预期更强。
  
  Model-as-facet分析cleanly提取model×item（~10%），item_id降至49%但仍为最大单一组分。
  Bootstrap CIs tight（4-6pp宽度）且benchmark间不重叠——gradient具有full statistical significance。
  Separability是clean confirmatory null（hardware×methodology <0.3%）。
  
  三条claim全部成立无需弱化。AAAI "evaluation methodology" track投稿正常推进。
  Lead figure: 4-benchmark stacked bars展示variance structure的系统性迁移，
  signature visual直接支撑"no universal recipe"叙事。

imagined_experiments:
  - name: "Full-scale MMLU precision study with confound fix"
    plan_id: "exp-001"
    description: >
      4 models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT, Mistral-7B-v0.3) × 3 precisions (FP32/BF16/FP16)
      × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified),
      全部使用vLLM V0 enforce_eager消除engine confound。
      总条件数 4×3×6×6×3×4 = 5,184 per item，总记录 5,184×200 = 1,036,800。
    expected_results:
      total_records: 1036800
      conditions_per_model: 1296
      overall_accuracy: 0.667
      accuracy_fp32: 0.664
      accuracy_bf16: 0.669
      accuracy_fp16: 0.667
      accuracy_spread_across_precisions_pp: 0.5
      item_id: 0.560
      residual: 0.207
      prompt_template_x_item_id: 0.062
      temperature_x_item_id: 0.059
      seed_x_item_id: 0.030
      precision_x_item_id: 0.018
      ordering_x_item_id: 0.015
      prompt_template: 0.018
      temperature: 0.014
      ordering: 0.008
      precision: 0.003
      seed: 0.002
      direct_infra_x_method_total: 0.004
      models_with_item_id_rank1: 4
      item_id_range_across_models: [0.516, 0.602]
      qwen3_8b_item_id: 0.578
      llama31_8b_item_id: 0.554
      gemma2_9b_item_id: 0.602
      mistral_7b_item_id: 0.516
      precision_main_before_fix_mvp: 0.0087
      precision_main_after_fix: 0.003
      precision_x_item_before_fix_mvp: 0.0724
      precision_x_item_after_fix: 0.018
      fp32_bf16_gap_before_fix_pp: 8.5
      fp32_bf16_gap_after_fix_pp: 0.5
      g_coefficient_correct: 0.36
      g_text_exact_match: 0.94
      text_match_prompt_x_item: 0.362
      text_match_item_id: 0.218
      text_match_precision_x_temperature: 0.014
    result_rationale: >
      MVP的precision主效应(0.87%)和precision×item(7.24%)源于float32使用不同vLLM engine路径（V1 CUDA graph vs V0 eager），
      导致FP32准确率系统性偏低5.7pp。统一V0 enforce_eager后三种精度走同一compute path，
      FP32/BF16/FP16准确率差收敛至0.5pp内（纯numerical noise水平，符合IEEE 754 rounding差异预期）。
      
      Precision释放的~6%方差重新分配：precision×item从7.2%→1.8%（剩余为genuine numerical sensitivity on boundary items），
      precision主效应从0.87%→0.3%，释放的份额主要回流到residual（+3.1pp）和小量到item_id（+0.2pp），
      因为之前被precision confound扭曲的item-level patterns现在归入正确组分。
      
      4个模型均以item_id为rank-1（51.6%-60.2%），因为MMLU的item difficulty分布（从trivial factual recall到
      expert-level reasoning）在所有7-9B instruction-tuned模型上产生类似的accuracy ceiling/floor效应。
      Gemma-2最高(60.2%)因其instruction-tuning使easy items更稳定（floor更高），
      Mistral最低(51.6%)因其在部分domain上accuracy分布更平坦（difficulty gradient被压缩）。
      
      200 items分层采样比MVP的50 items提供更稳定的方差估计，SE减半，CI收窄~50%。
      
      Text-exact-match指标复现MVP pattern：prompt×item主导(36.2%)而非item_id(21.8%)，
      因为不同prompt template导致model生成不同格式的答案字符串（"A"/"(A)"/"The answer is A"），
      这种格式变异是item-specific的（有些items的答案format更鲁棒）。
      precision×temperature在text-match下仍检出1.4%（CI不含零），确认floating-point non-associativity效应。
    tables:
      - name: "Table 1: Variance Components — MMLU 200 items, 4 models pooled (binary_correct)"
        columns: ["Component", "% Variance", "SE", "95% CI Lower", "95% CI Upper", "MVP (50 items)"]
        rows:
          - ["item_id", 56.0, 1.8, 52.5, 59.5, "58.4"]
          - ["residual", 20.7, 0.8, 19.1, 22.3, "17.6"]
          - ["prompt×item", 6.2, 0.6, 5.0, 7.4, "5.7"]
          - ["temp×item", 5.9, 0.5, 4.9, 6.9, "6.9"]
          - ["seed×item", 3.0, 0.3, 2.4, 3.6, "2.7"]
          - ["precision×item", 1.8, 0.2, 1.4, 2.2, "7.2*"]
          - ["ordering×item", 1.5, 0.2, 1.1, 1.9, "—"]
          - ["prompt", 1.8, 0.3, 1.2, 2.4, "—"]
          - ["temperature", 1.4, 0.2, 1.0, 1.8, "—"]
          - ["ordering", 0.8, 0.2, 0.4, 1.2, "—"]
          - ["precision", 0.3, 0.1, 0.1, 0.5, "0.87*"]
          - ["seed", 0.2, 0.05, 0.1, 0.3, "—"]
          - ["infra×method (all)", 0.4, 0.1, 0.2, 0.6, "<0.02"]
      - name: "Table 2: Per-Model item_id Variance Share (MMLU)"
        columns: ["Model", "item_id %", "Next Largest", "Next %", "Accuracy"]
        rows:
          - ["Gemma-2-9B-IT", 60.2, "residual", 17.1, 0.691]
          - ["Qwen3-8B", 57.8, "residual", 18.3, 0.672]
          - ["Llama-3.1-8B", 55.4, "residual", 19.8, 0.658]
          - ["Mistral-7B-v0.3", 51.6, "residual", 22.4, 0.641]
    figures_description:
      - "Fig 1: Side-by-side stacked-bar — MVP (confounded, left) vs exp-001 (fixed, right)。
        precision和precision×item色块在右侧坍缩，item_id占比稳定，直观展示confound fix的效果。"
      - "Fig 2: 4-panel per-model stacked bars，each panel one model。item_id色块在所有panel中均为最大，
        展示cross-model consistency。Mistral panel中residual略大，Gemma panel中item_id略大。"
      - "Fig 3: Per-item accuracy scatter (FP32 vs BF16)。MVP中slope偏离1.0且intercept偏移（confound），
        exp-001中points紧贴diagonal（r>0.998），outlier items标注。"
    analysis: >
      核心发现：engine confound fix后item dominance完全稳健（56.0% vs MVP 58.4%，差异在SE范围内），
      precision主效应从0.87%坍缩至0.3%。这同时验证了Claim 1和提供了方法论贡献
      （vLLM engine配置对variance attribution的系统性影响）。
      4个模型一致性消除了"单模型特例"concern。text-match指标复现MVP的dual-metric pattern。
      Ordering facet新增后占比很小（~2.3% total），不是major concern。
      该实验为所有后续benchmark比较建立了MMLU baseline。

  - name: "Item resampling stability test"
    plan_id: "exp-001b"
    description: >
      3 independent stratified 200-item MMLU samples (stratification seeds 0, 7, 99)
      × 1 model (Llama-3.1-8B) × 3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample。
      每sample 54×200 = 10,800记录，总计 32,400记录。
      测试item_id dominance是否对specific item selection稳定。
    expected_results:
      total_records: 32400
      conditions_per_sample: 54
      sample_a_item_id: 0.528
      sample_b_item_id: 0.572
      sample_c_item_id: 0.561
      item_id_mean: 0.554
      item_id_sd: 0.023
      item_id_cv: 0.041
      item_id_rank1_all_samples: true
      sample_a_residual: 0.224
      sample_b_residual: 0.198
      sample_c_residual: 0.210
      sample_a_accuracy: 0.651
      sample_b_accuracy: 0.664
      sample_c_accuracy: 0.657
      prompt_x_item_range: [0.054, 0.072]
      temp_x_item_range: [0.048, 0.067]
      max_component_cv: 0.14
    result_rationale: >
      Item_id across 3 samples: 52.8%, 57.2%, 55.6%（mean=55.4%, CV=4.1%）。
      所有sample均在50-60%范围内，item_id均为rank-1。CV远低于15%阈值。
      
      Sample间变异源于MMLU 14K item pool中不同difficulty strata的adoption——
      不同随机种子抽到的items在difficulty distribution上略有差异（例如sample B可能
      包含更多extreme-difficulty items，拉大item variance）。但由于分层采样保证了
      subject-level比例一致，这种变异被有效控制。
      
      关键：即使是"worst"的sample A（52.8%），item_id仍远超第二名residual（22.4%），
      headline claim "item selection is the largest variance source"对任意200-item MMLU子集稳健。
      
      非item组分的CV也可控（max 14%），说明variance structure本身是item-robust的，
      不会因特定item选择而qualitatively改变。
    tables:
      - name: "Table 3: Item Resampling Stability (Llama-3.1-8B, MMLU)"
        columns: ["Component", "Sample A", "Sample B", "Sample C", "Mean", "CV"]
        rows:
          - ["item_id", 52.8, 57.2, 55.6, 55.2, "4.1%"]
          - ["residual", 22.4, 19.8, 21.0, 21.1, "6.2%"]
          - ["prompt×item", 5.4, 7.2, 6.1, 6.2, "14.5%"]
          - ["temp×item", 4.8, 6.7, 5.6, 5.7, "16.7%"]
          - ["seed×item", 2.8, 3.2, 3.0, 3.0, "6.7%"]
          - ["precision×item", 1.6, 2.0, 1.8, 1.8, "11.1%"]
          - ["Accuracy", 0.651, 0.664, 0.657, 0.657, "—"]
    figures_description:
      - "Fig 4: 3-sample stacked-bar comparison，side-by-side。item_id色块高度一致，
        minor variation在其他组分上。error bars显示bootstrap SE。"
      - "Fig 5: item_id % 的strip plot (3 points) + 95% CI bar，
        直观展示resampling stability和CI不含零。"
    analysis: >
      CV=4.1%的稳定性为headline claim提供了strong defense against "specific item selection artifact"。
      即使用不同的200-item子集，variance structure qualitatively不变。
      这为exp-002的cross-benchmark比较提供了基线——任何跨benchmark的item_id差异
      只要超过~5pp就不能归因于item sampling variability。

  - name: "Multi-benchmark variance gradient"
    plan_id: "exp-002"
    description: >
      4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures × 4 orderings
      × 200 items，在GSM8K、ARC-Challenge、HellaSwag上分别运行。
      每benchmark 4×2×6×6×2×4×200 = 460,800记录，3 benchmarks总计 1,382,400记录。
      核心目标：建立cross-benchmark variance gradient，验证item dominance的benchmark-dependence。
    expected_results:
      total_records_per_benchmark: 460800
      total_records_all: 1382400
      # GSM8K
      gsm8k_overall_accuracy: 0.574
      gsm8k_item_id: 0.250
      gsm8k_temperature_x_item: 0.182
      gsm8k_seed_x_item: 0.158
      gsm8k_prompt_x_item: 0.103
      gsm8k_residual: 0.159
      gsm8k_ordering_x_item: 0.032
      gsm8k_precision_x_item: 0.011
      gsm8k_temperature: 0.036
      gsm8k_prompt: 0.028
      gsm8k_seed: 0.024
      gsm8k_ordering: 0.012
      gsm8k_precision: 0.002
      gsm8k_infra_x_method: 0.003
      gsm8k_g_full_design: 0.55
      # ARC-Challenge
      arc_overall_accuracy: 0.592
      arc_item_id: 0.420
      arc_temperature_x_item: 0.086
      arc_seed_x_item: 0.062
      arc_prompt_x_item: 0.092
      arc_residual: 0.174
      arc_ordering_x_item: 0.034
      arc_precision_x_item: 0.015
      arc_temperature: 0.020
      arc_prompt: 0.022
      arc_seed: 0.014
      arc_ordering: 0.012
      arc_precision: 0.002
      arc_infra_x_method: 0.003
      arc_g_full_design: 0.42
      # HellaSwag
      hellaswag_overall_accuracy: 0.708
      hellaswag_item_id: 0.340
      hellaswag_temperature_x_item: 0.132
      hellaswag_seed_x_item: 0.108
      hellaswag_prompt_x_item: 0.094
      hellaswag_residual: 0.158
      hellaswag_ordering_x_item: 0.036
      hellaswag_precision_x_item: 0.013
      hellaswag_temperature: 0.028
      hellaswag_prompt: 0.024
      hellaswag_seed: 0.020
      hellaswag_ordering: 0.014
      hellaswag_precision: 0.002
      hellaswag_infra_x_method: 0.003
      hellaswag_g_full_design: 0.47
      # Cross-benchmark
      gradient_monotonic: true
      gradient_order: "MMLU > ARC > HellaSwag > GSM8K"
      gradient_spread_pp: 31.0
      all_benchmarks_item_id_rank1: true
      item_id_range_across_benchmarks: [0.250, 0.560]
      models_showing_consistent_gradient: 4
      precision_main_under_0_5pct_all_benchmarks: true
    result_rationale: >
      Cross-benchmark gradient的机制：MMLU(56%) > ARC(42%) > HellaSwag(34%) > GSM8K(25%)。
      
      MMLU是knowledge-retrieval：item difficulty是intrinsic属性——你要么知道，要么不知道。
      不同temperature/seed对答案选择的影响很小，因为在logit space中correct answer的probability
      要么远高于threshold（easy items）要么远低于（hard items）。只有narrow difficulty band
      内的items对generation parameters敏感。结果：item_id dominates at 56%。
      
      GSM8K是multi-step math reasoning：同一item在不同seeds/temperatures下产生qualitatively不同的
      推理链。具体地：(1) 每个推理步骤是independently sampled，温度直接影响每步的token distribution，
      多步累积效应使temperature×item达到18.2%——对比MMLU的5.9%，涨幅3×；
      (2) random seed决定了initial token choice，不同seed走不同reasoning path，
      某些items（multi-step word problems）对seed极度敏感而simple arithmetic几乎不受影响，
      故seed×item达到15.8%——对比MMLU的3.0%，涨幅5×；
      (3) item_id降至25%不是因为items不重要，而是因为"intrinsic difficulty"只是total difficulty的一部分——
      在reasoning tasks中，difficulty = intrinsic complexity + generation path stochasticity。
      
      ARC-Challenge混合了factual recall（类似MMLU）和multi-hop reasoning（类似GSM8K），
      所以item_id(42%)落在两者之间。具体来说，ARC的science questions中factual questions
      （"What is the boiling point of water?"）贡献高item_id，而multi-hop questions
      （"Which of these would happen if..."）贡献高interaction terms。
      
      HellaSwag是commonsense completion：需要生成continuation的判断涉及implicit reasoning
      但步骤较少（通常1-2步推理），介于knowledge和full reasoning之间。
      Distractor quality的item-level variation是item_id的主要贡献（有些items的wrong
      answers显而易见，有些极难区分），但generation sensitivity高于MMLU。
      
      所有benchmark上precision主效应均<0.3%（均为engine confound fix后的clean estimates），
      infra×method<0.3%，确认separability across benchmarks。
      
      4/4 models在每个benchmark上都展示相同的gradient pattern，排除了model-specific artifact。
    tables:
      - name: "Table 4: Cross-Benchmark Variance Gradient (binary_correct, 4 models pooled)"
        columns: ["Benchmark", "Task Type", "item_id %", "temp×item %", "seed×item %", "prompt×item %", "Residual %", "G (full)"]
        rows:
          - ["MMLU", "Knowledge", 56.0, 5.9, 3.0, 6.2, 20.7, 0.36]
          - ["ARC-Chal.", "Science", 42.0, 8.6, 6.2, 9.2, 17.4, 0.42]
          - ["HellaSwag", "Commonsense", 34.0, 13.2, 10.8, 9.4, 15.8, 0.47]
          - ["GSM8K", "Math", 25.0, 18.2, 15.8, 10.3, 15.9, 0.55]
      - name: "Table 5: GSM8K Per-Model Variance Breakdown"
        columns: ["Model", "item_id %", "temp×item %", "seed×item %", "prompt×item %", "Residual %"]
        rows:
          - ["Qwen3-8B", 28.4, 16.8, 14.2, 9.6, 14.8]
          - ["Llama-3.1-8B", 24.1, 19.4, 16.8, 10.8, 15.2]
          - ["Gemma-2-9B-IT", 27.6, 17.2, 14.8, 9.8, 14.6]
          - ["Mistral-7B-v0.3", 21.2, 20.6, 18.4, 11.6, 16.4]
      - name: "Table 6: Interaction Term Gradient (benchmark × interaction type)"
        columns: ["Benchmark", "temp×item", "seed×item", "Σ(interaction×item)", "Main Effects Σ"]
        rows:
          - ["MMLU", 5.9, 3.0, 18.4, 4.5]
          - ["ARC-Chal.", 8.6, 6.2, 28.9, 7.0]
          - ["HellaSwag", 13.2, 10.8, 38.3, 8.8]
          - ["GSM8K", 18.2, 15.8, 48.6, 10.2]
    figures_description:
      - "Fig 6 [SIGNATURE FIGURE]: 4-benchmark stacked-bar variance decomposition，
        benchmarks按task reasoning intensity排序（MMLU→ARC→HellaSwag→GSM8K）。
        item_id色块从左到右系统性缩小，temp×item和seed×item色块系统性扩大。
        视觉上清晰展示variance structure的cross-benchmark gradient。
        这是paper的lead figure，直接支撑'no universal recipe'叙事。"
      - "Fig 7: Heatmap — 4 benchmarks × 4 models × top-5 components。
        色深=variance share。item_id行从左到右渐变（深→浅），
        temp×item行反向渐变（浅→深）。Pattern在所有model行中一致。"
      - "Fig 8: Scatter plot — item_id % vs benchmark reasoning intensity (ordinal axis)，
        4 models × 4 benchmarks = 16 points。Clear monotonic trend with tight model-level clusters。"
    analysis: >
      这是paper的headline experiment。31pp的gradient spread（MMLU 56% → GSM8K 25%）
      是primary novel finding。比第一版dream预测的~10pp gradient（旧预测GSM8K在~49%）
      大3×，说明reasoning tasks的variance structure与knowledge tasks qualitatively不同。
      
      核心发现可总结为一句话：
      "On knowledge benchmarks, WHICH items you select determines your result;
       on reasoning benchmarks, HOW you generate answers matters equally."
      
      4/4 benchmarks的item_id仍为rank-1，但GSM8K的item_id(25%)仅微弱领先temp×item(18.2%)，
      说明在extreme reasoning tasks上，item dominance可能不再成立——
      这为MATH benchmark（exp-008）设置了预期。
      
      G coefficient的反直觉pattern：knowledge benchmarks的G更低（MMLU 0.36 vs GSM8K 0.55）。
      这是因为high item_id意味着item sampling是measurement reliability的bottleneck——
      在MMLU上即使用全部facet levels，200-item的item sampling error仍然dominant。
      GSM8K的low item_id意味着item sampling error小，多seed/temp averaging后G更高。

  - name: "Multi-hardware separability test"
    plan_id: "exp-003"
    description: >
      4 models × 2 GPU types (RTX PRO 6000 + second GPU) × 2 precisions (BF16/FP16)
      × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。
      总记录 4×2×2×6×6×3×4×200 = 691,200。
      核心目标：量化hardware主效应和hardware×methodology交互，验证single-GPU separability。
    expected_results:
      total_records: 691200
      hardware_main_effect: 0.004
      hardware_x_item: 0.016
      hardware_x_prompt: 0.0006
      hardware_x_temperature: 0.0005
      hardware_x_seed: 0.0004
      hardware_x_ordering: 0.0002
      hardware_x_methodology_total: 0.0017
      precision_x_prompt: 0.0006
      precision_x_temperature: 0.0005
      precision_x_seed: 0.0003
      precision_x_ordering: 0.0002
      direct_infra_x_method_total: 0.003
      item_id: 0.554
      residual: 0.164
      prompt_x_item: 0.060
      temperature_x_item: 0.057
      seed_x_item: 0.029
      precision_x_item: 0.017
      ordering_x_item: 0.014
      infra_x_item_total: 0.033
      method_x_item_total: 0.160
      gpu1_gpu2_accuracy_correlation: 0.9992
      max_accuracy_difference_any_condition: 0.014
      mean_accuracy_difference: 0.003
      model_rankings_preserved: true
      g_full_design: 0.35
    result_rationale: >
      Hardware主效应0.4%反映两块GPU的微架构差异（不同SM count、memory bandwidth、kernel scheduling），
      但这些差异是systematic fixed offset，不是random——同一model在GPU2上一致性地偏低0.3pp。
      
      hardware×methodology total仅0.17%，远低于1%阈值。原理：hardware层影响numerical computation
      （tensor core routing、memory alignment），methodology层影响token sampling
      （prompt→attention pattern、seed→RNG state、temperature→softmax scaling）。
      两者的交叉点（GPU微架构如何影响不同prompt下的sampling distribution）
      在logit space中被softmax压缩到negligible水平——除非logits在decision boundary附近
      （这是hardware×item交互的来源：boundary items对numerical precision敏感）。
      
      hardware×item(1.6%)比hardware主效应(0.4%)大4×，因为特定items
      （logit difference between correct and nearest distractor < 0.01）在不同GPU上
      因kernel tiling和memory access pattern差异产生不同numerical path。
      但这只影响~5%的boundary items。
      
      GPU间accuracy correlation 0.9992说明hardware几乎不改变measurement outcome。
      Model rankings across all conditions完全preserved——无ranking flip。
      
      这是clean confirmatory null：validates isolated-factor studies的implicit separability assumption，
      同时hardware×item的non-zero值提供了nuanced story。
    tables:
      - name: "Table 7: Separability Test — Direct vs Item-Conditional Interactions"
        columns: ["Interaction Type", "Components", "Total %", "Interpretation"]
        rows:
          - ["Direct Infra×Method", "hw×prompt, hw×temp, hw×seed, hw×ord, prec×prompt, prec×temp, prec×seed, prec×ord", 0.3, "Negligible — aggregate separability holds"]
          - ["Infra×Item", "hw×item, prec×item", 3.3, "Small — hardware/precision effects are item-conditional"]
          - ["Method×Item", "prompt×item, temp×item, seed×item, ord×item", 16.0, "Substantial — methodology effects are strongly item-conditional"]
          - ["Item Main", "item_id", 55.4, "Dominant — item selection is the primary variance source"]
      - name: "Table 8: Hardware Agreement (per-model mean accuracy)"
        columns: ["Model", "GPU1 (RTX PRO 6000)", "GPU2", "Δ (pp)", "Rank Preserved"]
        rows:
          - ["Qwen3-8B", 0.672, 0.669, 0.3, "Yes"]
          - ["Llama-3.1-8B", 0.658, 0.655, 0.3, "Yes"]
          - ["Gemma-2-9B-IT", 0.691, 0.687, 0.4, "Yes"]
          - ["Mistral-7B-v0.3", 0.641, 0.638, 0.3, "Yes"]
    figures_description:
      - "Fig 9: Separability diagram — 两同心层（inner=infra, outer=method）通过item连接。
        Direct interaction箭头用虚线标注<0.3%，item-conditional箭头用实线标注3.3%/16.0%。
        视觉上直观展示'separable at aggregate, coupled through items'。"
      - "Fig 10: GPU1 vs GPU2 per-item accuracy scatter (pooled across conditions)，
        near-perfect diagonal (r=0.9992)，5-8个outlier boundary items标注。"
    analysis: >
      Separability confirmed: direct infra×method total 0.3%，远低于1%阈值。
      这是Claim 2的核心evidence。但不是trivial null——
      item-conditional interactions提供了mechanistic insight：
      infra和method不是completely independent，而是通过item difficulty间接耦合。
      这解释了为什么prior isolated-factor studies在某些specific items上不generalize
      而在aggregate level是valid的。
      
      Note：当前"infrastructure"限于precision facet + 2 GPU types。
      更广泛的hardware diversity（datacenter GPU、不同CUDA versions）是future work。

  - name: "Comprehensive analysis with model-as-facet and D-study projections"
    plan_id: "exp-004"
    description: >
      基于exp-001/001b/002/003合并数据的comprehensive analysis suite。包含：
      (a) Model-as-facet G-theory reanalysis；(b) Bootstrap CIs (1000 resamples)；
      (c) D-study projections with benchmark-specific budgets；(d) REML vs Henderson比较；
      (e) Logprob-based scoring；(f) Ranking stability analysis；(g) Higher-order interaction estimation。
      纯计算，无GPU开销。
    expected_results:
      # (a) Model-as-facet — MMLU
      mmlu_item_id_model_as_facet: 0.492
      mmlu_model_x_item: 0.102
      mmlu_model_main: 0.028
      mmlu_model_x_prompt: 0.014
      mmlu_model_x_temp: 0.008
      mmlu_model_x_seed: 0.003
      mmlu_residual_model_as_facet: 0.120
      mmlu_item_id_still_largest: true
      # Model-as-facet — other benchmarks
      arc_item_id_model_as_facet: 0.384
      arc_model_x_item: 0.081
      hellaswag_item_id_model_as_facet: 0.308
      hellaswag_model_x_item: 0.074
      gsm8k_item_id_model_as_facet: 0.226
      gsm8k_model_x_item: 0.058
      model_x_item_gradient: "MMLU(10.2%) > ARC(8.1%) > HellaSwag(7.4%) > GSM8K(5.8%)"
      # (b) Bootstrap CIs
      mmlu_item_id_ci: [0.461, 0.523]
      mmlu_item_id_ci_width: 0.062
      arc_item_id_ci: [0.356, 0.412]
      arc_item_id_ci_width: 0.056
      hellaswag_item_id_ci: [0.282, 0.334]
      hellaswag_item_id_ci_width: 0.052
      gsm8k_item_id_ci: [0.198, 0.254]
      gsm8k_item_id_ci_width: 0.056
      cis_exclude_zero_all: true
      cis_non_overlapping_all_pairs: true
      # (c) D-study projections
      mmlu_g_current_practice_1p1s200i: 0.22
      gsm8k_g_current_practice_1p1s200i: 0.14
      arc_g_current_practice_1p1s200i: 0.20
      hellaswag_g_current_practice_1p1s200i: 0.18
      mmlu_dstudy_items_for_g90: 420
      mmlu_dstudy_prompts_for_g90: 3
      mmlu_dstudy_seeds_for_g90: 2
      mmlu_dstudy_total_evals_g90: 2520
      gsm8k_dstudy_items_for_g90: 150
      gsm8k_dstudy_prompts_for_g90: 3
      gsm8k_dstudy_seeds_for_g90: 10
      gsm8k_dstudy_total_evals_g90: 4500
      arc_dstudy_items_for_g90: 320
      arc_dstudy_seeds_for_g90: 4
      hellaswag_dstudy_items_for_g90: 240
      hellaswag_dstudy_seeds_for_g90: 6
      items_vs_seeds_effectiveness_mmlu: 14.2
      items_vs_seeds_effectiveness_gsm8k: 0.8
      # (d) REML vs Henderson
      reml_henderson_max_diff_pp: 1.4
      reml_henderson_rank_agreement: true
      # (e) Logprob scoring
      logprob_item_id_mmlu: 0.428
      logprob_prompt_main_mmlu: 0.068
      logprob_g_mmlu: 0.41
      # (f) Ranking stability
      ranking_stable_across_conditions_pct: 96.8
      ranking_flips_only_within_1pp: true
      # (g) Higher-order interactions
      three_way_total: 0.048
      largest_three_way_temp_x_seed_x_item: 0.018
      residual_after_3way_extraction: 0.072
    result_rationale: >
      (a) Model-as-facet：在MMLU数据中加入model作为crossed random facet后，model×item吸收10.2%方差。
      这10.2%来源：约6.8%从pooled item_id提取（因为model-specific item difficulty patterns
      在pooled分析中被归入item主效应），约3.4%从residual提取（因为model-specific noise
      在pooled分析中被归入unexplained error）。item_id从56.0%降至49.2%但仍为最大单一组分，
      residual从20.7%降至12.0%（大幅改善模型拟合）。
      
      Model×item gradient与主gradient同向：知识型benchmark上models更heterogeneous
      （MMLU 10.2% vs GSM8K 5.8%），因为models在knowledge domain coverage上差异大
      （Gemma在STEM强、Mistral在humanities强），而在reasoning ability上差异相对小。
      
      (b) Bootstrap CIs：1000次item-level resampling后，所有benchmark的item_id CI
      不含零（all lower bounds > 19%），且任意两个benchmark间CIs不重叠。
      MMLU [46.1%, 52.3%]、ARC [35.6%, 41.2%]、HellaSwag [28.2%, 33.4%]、GSM8K [19.8%, 25.4%]。
      CI宽度4-6pp（1000 resamples, 200 items each），
      证明31pp的gradient spread具有full statistical significance。
      
      (c) D-study核心发现——评估protocol的optimal allocation随benchmark qualitatively改变：
      - MMLU是item-limited：items vs seeds effectiveness ratio = 14.2:1。
        G≥0.90需要420 items + 3 prompts + 2 seeds = 2,520 evaluations。
        Scaling items是唯一高效路径。
      - GSM8K是seed-limited：items vs seeds effectiveness ratio = 0.8:1（反转！）。
        G≥0.90需要150 items + 3 prompts + 10 seeds = 4,500 evaluations。
        Scaling seeds比scaling items更有效，因为seed×item和temp×item是dominant error sources。
      
      这是"no universal recipe"的quantitative crystallization：
      同一evaluation budget在不同benchmark上的optimal allocation完全不同。
      
      Current practice G全部<0.25——低于社会科学中"不可接受"的阈值（通常G≥0.80），
      说明现有leaderboard结果的measurement reliability fundamentally inadequate。
      GSM8K current practice G最低(0.14)，因为seed×item和temp×item在1-seed/1-temp下
      完全contribute as error。
      
      (d) REML vs Henderson：差异<1.5pp在所有组分上，component ranking完全一致。
      REML在小方差组分上给出slightly lower estimates（consistent with REML的bias correction特性）。
      
      (e) Logprob scoring：continuous measure，item_id降至42.8%（因为logprobs capture
      graded confidence而非binary threshold），prompt主效应升至6.8%（不同prompts
      系统性shift logprob distribution）。G升至0.41（continuous scoring reduces measurement error）。
      
      (f) Ranking stability：96.8%的条件组合下4个model ranking不变。
      Flips仅发生在accuracy差<1pp的model pairs在extreme conditions下（high temp + specific items），
      且flip direction不systematic。
      
      (g) Higher-order interactions：3-way总计4.8%，最大的temp×seed×item(1.8%)
      反映了在特定items上temperature和seed的joint sensitivity。
      Residual从12.0%降至7.2%，表明3-way interactions是residual的主要组成。
    tables:
      - name: "Table 9: Model-as-Facet Reanalysis — Cross-Benchmark (binary_correct)"
        columns: ["Component", "MMLU", "ARC", "HellaSwag", "GSM8K"]
        rows:
          - ["item_id", 49.2, 38.4, 30.8, 22.6]
          - ["model×item", 10.2, 8.1, 7.4, 5.8]
          - ["temp×item", 5.9, 8.6, 13.2, 18.2]
          - ["seed×item", 3.0, 6.2, 10.8, 15.8]
          - ["prompt×item", 6.2, 9.2, 9.4, 10.3]
          - ["model", 2.8, 2.4, 2.2, 2.0]
          - ["residual", 12.0, 13.8, 14.4, 13.6]
          - ["other", 10.7, 13.3, 11.8, 11.7]
      - name: "Table 10: Bootstrap 95% CIs on item_id (model-as-facet, 1000 resamples)"
        columns: ["Benchmark", "item_id %", "95% CI", "Width (pp)", "Excludes 0"]
        rows:
          - ["MMLU", 49.2, "[46.1, 52.3]", 6.2, "Yes"]
          - ["ARC-Challenge", 38.4, "[35.6, 41.2]", 5.6, "Yes"]
          - ["HellaSwag", 30.8, "[28.2, 33.4]", 5.2, "Yes"]
          - ["GSM8K", 22.6, "[19.8, 25.4]", 5.6, "Yes"]
      - name: "Table 11: D-Study Optimal Allocation for G≥0.90"
        columns: ["Benchmark", "Items", "Prompts", "Seeds", "Total Evals", "Bottleneck"]
        rows:
          - ["MMLU", 420, 3, 2, 2520, "Items"]
          - ["ARC-Challenge", 320, 3, 4, 3840, "Items"]
          - ["HellaSwag", 240, 3, 6, 4320, "Mixed"]
          - ["GSM8K", 150, 3, 10, 4500, "Seeds"]
      - name: "Table 12: D-Study Projection Grid — MMLU (Items × Prompts × Seeds → G)"
        columns: ["Items", "Prompts", "Seeds", "Total Evals", "G coeff", "Δ vs Current"]
        rows:
          - [200, 1, 1, 200, 0.22, "baseline"]
          - [200, 3, 1, 600, 0.29, "+0.07"]
          - [200, 3, 3, 1800, 0.32, "+0.10"]
          - [400, 1, 1, 400, 0.41, "+0.19"]
          - [400, 3, 2, 2400, 0.82, "+0.60"]
          - [420, 3, 2, 2520, 0.90, "+0.68"]
          - [600, 3, 2, 3600, 0.94, "+0.72"]
          - [1000, 4, 3, 12000, 0.97, "+0.75"]
      - name: "Table 13: D-Study Projection Grid — GSM8K (Items × Prompts × Seeds → G)"
        columns: ["Items", "Prompts", "Seeds", "Total Evals", "G coeff", "Δ vs Current"]
        rows:
          - [200, 1, 1, 200, 0.14, "baseline"]
          - [200, 1, 6, 1200, 0.36, "+0.22"]
          - [200, 3, 6, 3600, 0.52, "+0.38"]
          - [200, 3, 10, 6000, 0.68, "+0.54"]
          - [150, 3, 10, 4500, 0.90, "+0.76"]
          - [200, 3, 10, 6000, 0.93, "+0.79"]
          - [300, 4, 12, 14400, 0.97, "+0.83"]
      - name: "Table 14: Facet Effectiveness Ratio by Benchmark"
        columns: ["Benchmark", "ΔG per 100 items", "ΔG per seed", "Items:Seeds ratio"]
        rows:
          - ["MMLU", 0.042, 0.003, "14.2:1"]
          - ["ARC-Challenge", 0.034, 0.008, "4.3:1"]
          - ["HellaSwag", 0.026, 0.014, "1.9:1"]
          - ["GSM8K", 0.015, 0.019, "0.8:1"]
    figures_description:
      - "Fig 11: Bootstrap CI forest plot — 4 benchmarks的item_id point estimates + 95% CIs，
        横轴0-60%。4个CIs clearly separated（无overlap），gradient visually obvious。"
      - "Fig 12: D-study projection curves — G vs total evaluations。
        两个panel：左panel scale items only，右panel scale seeds only。
        MMLU在左panel陡峭上升，GSM8K在右panel陡峭上升。交叉pattern直观展示
        'MMLU is item-limited, GSM8K is seed-limited'。"
      - "Fig 13: Facet effectiveness ratio bar chart — 4 benchmarks × 2 bars (items, seeds)。
        MMLU的items bar远高于seeds bar，GSM8K相反。从左到右ratio reverses。"
      - "Fig 14: Model-as-facet前后对比 — MMLU stacked bars side-by-side。
        左: pooled (item_id 56%), 右: model-as-facet (item_id 49%, model×item 10.2%)。
        residual显著减小。"
    analysis: >
      Exp-004是paper的analytical backbone。三个key takeaways：
      
      1. Model-as-facet cleanly reduces residual（20.7%→12.0%），model×item(10.2%)是有意义的组分，
         但item_id(49.2%)仍为最大。这回应了Dream review的"model not treated as facet"concern。
      
      2. Bootstrap CIs将gradient从descriptive观察提升为statistically significant finding。
         任意两benchmark间CIs不重叠，31pp spread的significance不容质疑。
      
      3. D-study的"allocation reversal"是paper最actionable的finding：
         practitioners在MMLU上应invest in more items（420 for G≥0.90），
         在GSM8K上应invest in more seeds（10 for G≥0.90）。
         This is the quantitative distillation of "no universal recipe"。
         
         Current practice G < 0.25 everywhere是strong policy implication——
         现有evaluation的measurement reliability低于任何scientific discipline的最低标准。

  - name: "14B model scale extension"
    plan_id: "exp-005"
    description: >
      Qwen3-14B和DeepSeek-R1-Distill-14B × 2 precisions (BF16/FP16)
      × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items。
      每模型 2×6×6×3×4×200 = 172,800记录，总计 345,600记录。
    expected_results:
      total_records: 345600
      qwen3_14b_accuracy: 0.724
      deepseek_r1_14b_accuracy: 0.708
      qwen3_14b_item_id: 0.548
      deepseek_r1_14b_item_id: 0.502
      qwen3_14b_residual: 0.172
      deepseek_r1_14b_residual: 0.208
      deepseek_r1_14b_temp_x_item: 0.088
      deepseek_r1_14b_seed_x_item: 0.052
      qwen3_14b_temp_x_item: 0.054
      item_id_rank1_both: true
      within_8b_model_range: true
      precision_main_14b: 0.002
    result_rationale: >
      14B模型的overall accuracy更高（72.4%/70.8% vs 8B平均66.7%），但variance structure不因scale改变。
      Item_id在两个14B上均为rank-1：Qwen3-14B(54.8%)落在8B range(51.6%-60.2%)内，
      DeepSeek-R1-Distill-14B(50.2%)也在range内但偏低端。
      
      Qwen3-14B的variance profile几乎identical to Qwen3-8B（scaled up但structure preserved），
      因为item difficulty的relative ordering不随model scale改变——easy items仍easy，hard items仍hard，
      只是accuracy ceiling整体上移。
      
      DeepSeek-R1-Distill-14B的profile略有不同：temp×item更高(8.8% vs 8B mean 5.9%)，
      seed×item更高(5.2% vs 3.0%)，residual更高(20.8%)。原因：reasoning distillation引入了
      implicit chain-of-thought倾向，即使在MMLU这种knowledge task上也会触发extended reasoning，
      增加了generation-level stochasticity。这个pattern类似于GSM8K在8B上的表现——
      suggesting that reasoning-tuned models在所有benchmarks上都shift toward更高的interaction terms。
      
      Precision主效应在14B上同样negligible(0.2%)，确认confound fix与model size无关。
    tables:
      - name: "Table 15: 14B vs 8B Variance Pattern Comparison"
        columns: ["Component", "8B Mean", "8B Range", "Qwen3-14B", "DS-R1-14B"]
        rows:
          - ["item_id", 56.0, "51.6–60.2", 54.8, 50.2]
          - ["residual", 20.7, "17.1–22.4", 17.2, 20.8]
          - ["temp×item", 5.9, "4.9–6.9", 5.4, 8.8]
          - ["prompt×item", 6.2, "5.0–7.4", 6.0, 5.6]
          - ["seed×item", 3.0, "2.4–3.6", 2.8, 5.2]
          - ["precision", 0.3, "0.1–0.5", 0.2, 0.2]
    figures_description:
      - "Fig 15: 6-model stacked bars (4×8B + 2×14B)，按model scale分组。
        14B组的variance structure在8B range内，DeepSeek-R1的temp×item和seed×item略大但不改变hierarchy。"
    analysis: >
      Scale invariance confirmed：item dominance不是小模型artifact。
      DeepSeek-R1-Distill的slightly shifted profile提供了有趣的secondary finding——
      reasoning distillation改变了model的generation characteristics，使其在knowledge tasks上
      也表现出类似reasoning tasks的更高interaction terms。
      这是P1实验，为paper增加robustness但不改变core claims。

  - name: "Fine-tuning G-study (RoBERTa)"
    plan_id: "exp-006"
    description: >
      RoBERTa-large在SST-2/MNLI/RTE/COPA上fine-tuning。
      6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task
      × 4 tasks = 1,728 total fine-tuning runs。
    expected_results:
      total_runs: 1728
      sst2_accuracy_mean: 0.946
      sst2_item_id: 0.406
      sst2_seed: 0.092
      sst2_learning_rate: 0.068
      sst2_data_shuffle: 0.038
      sst2_seed_x_item: 0.104
      sst2_lr_x_item: 0.078
      sst2_shuffle_x_item: 0.044
      sst2_residual: 0.118
      sst2_gpu: 0.003
      sst2_precision: 0.002
      mnli_accuracy_mean: 0.872
      mnli_item_id: 0.438
      mnli_seed: 0.076
      mnli_learning_rate: 0.084
      mnli_seed_x_item: 0.094
      mnli_residual: 0.136
      rte_accuracy_mean: 0.738
      rte_item_id: 0.358
      rte_seed: 0.132
      rte_learning_rate: 0.102
      rte_seed_x_item: 0.118
      rte_residual: 0.152
      copa_accuracy_mean: 0.678
      copa_item_id: 0.374
      copa_seed: 0.122
      copa_learning_rate: 0.096
      copa_residual: 0.164
      item_id_rank1_all_tasks: true
      seed_more_important_in_finetuning: true
      infra_effects_negligible: true
      finetuning_g_current_practice: 0.26
    result_rationale: >
      Fine-tuning vs inference的关键区别：training seed和learning rate成为substantial
      variance sources（combined 13-23%），因为它们影响optimization trajectory的全局geometry，
      不仅是sampling randomness。
      
      但item_id仍为rank-1（35.8%-43.8%），因为NLU tasks的item difficulty gradient——
      从"I love this movie"(trivially positive)到需要subtle pragmatic inference的examples——
      在所有training configurations下产生consistent accuracy variation。
      Item difficulty是task-intrinsic property，不随optimizer state改变。
      
      RTE的item_id最低(35.8%)，seed最高(13.2%)，因为小数据集(2.5K examples)使
      fine-tuning对seed极度敏感——不同random initializations导致qualitatively不同的
      loss landscape traversals，而小数据量意味着optimizer更容易overfit to specific
      data ordering。这是dataset size调节variance structure的evidence。
      
      GPU和precision主效应在fine-tuning中同样negligible(<0.5%)，因为RoBERTa-large
      对numerical precision不敏感（encoder-only architecture无autoregressive error accumulation）。
      
      Fine-tuning G current practice仅0.26（1 seed, 1 LR, full dataset），
      说明单次fine-tuning run的结果不具备adequate reliability。
    tables:
      - name: "Table 16: Fine-tuning vs Inference Variance Hierarchy"
        columns: ["Rank", "Inference (MMLU)", "Fine-tuning (SST-2)"]
        rows:
          - [1, "item_id (56.0%)", "item_id (40.6%)"]
          - [2, "residual (20.7%)", "residual (11.8%)"]
          - [3, "prompt×item (6.2%)", "seed×item (10.4%)"]
          - [4, "temp×item (5.9%)", "seed (9.2%)"]
          - [5, "seed×item (3.0%)", "lr×item (7.8%)"]
          - [6, "precision×item (1.8%)", "lr (6.8%)"]
      - name: "Table 17: Fine-tuning Variance Across Tasks"
        columns: ["Task", "N_train", "item_id %", "seed %", "LR %", "seed×item %"]
        rows:
          - ["SST-2", "67K", 40.6, 9.2, 6.8, 10.4]
          - ["MNLI", "393K", 43.8, 7.6, 8.4, 9.4]
          - ["RTE", "2.5K", 35.8, 13.2, 10.2, 11.8]
          - ["COPA", "400", 37.4, 12.2, 9.6, 10.8]
    figures_description:
      - "Fig 16: Inference vs Fine-tuning stacked bars并排，展示item_id在两个paradigm中均为rank-1
        但fine-tuning中seed/LR prominent。"
      - "Fig 17: Fine-tuning task panel — 4-task stacked bars按dataset size排序，
        展示dataset size对variance structure的调节（小dataset→seed更大）。"
    analysis: >
      Fine-tuning G-study将paper从inference evaluation扩展到ML reproducibility broadly。
      核心takeaway：item dominance是跨paradigm的，但second-tier factors不同——
      inference中是prompt和temperature，fine-tuning中是seed和learning rate。
      
      Dataset size作为moderator是interesting secondary finding：
      小数据(RTE, COPA)下seed dominance增强，类似reasoning benchmarks下temperature dominance增强。
      Both reflect increased stochasticity when the task is "harder"
      （either because data is scarce or because reasoning is complex）。
      
      P1实验，AAAI main paper中可condensed为1-2段+1 table，或放supplementary。

  - name: "LayerCast precision mitigation"
    plan_id: "exp-007"
    description: >
      4 models × LayerCast (FP16 storage + FP32 compute) × 6 prompts × 6 seeds
      × 3 temperatures × 4 orderings × 200 MMLU items = 172,800记录。
      作为第4种precision condition加入exp-001 analysis。
    expected_results:
      total_records: 172800
      layercast_accuracy_mean: 0.668
      layercast_vs_fp32_diff_pp: 0.4
      layercast_vs_bf16_diff_pp: -0.1
      layercast_item_agreement_fp32: 0.9993
      layercast_item_agreement_bf16: 0.9995
      layercast_added_precision_variance: 0.0003
      layercast_precision_x_item: 0.008
      layercast_throughput_vs_fp32: 1.42
      layercast_throughput_vs_bf16: 0.92
      layercast_vram_gb: 16.2
    result_rationale: >
      LayerCast在存储时用FP16减少memory footprint，compute时cast to FP32，
      因此numerical behavior几乎等同于纯FP32（same computation path，仅storage时有precision loss）。
      FP16 mantissa 10 bits vs FP32 23 bits的差异对大部分weights negligible
      （pre-trained weights本身就是从BF16/FP16训练来的）。
      
      Accuracy差异：vs FP32仅0.4pp（storage precision loss的residual effect），
      vs BF16仅0.1pp（BF16和LayerCast都是"FP32-adjacent"precision modes）。
      Item agreement > 99.93%确认LayerCast不改变per-item measurement outcome。
      
      对precision方差的增量贡献仅0.03%——essentially zero。
      Throughput比FP32快42%（memory bandwidth节省：16.2GB vs 31.2GB），
      比BF16慢8%（cast operation overhead）。
      
      这为paper提供了practical mitigation recommendation：如果practitioner
      担心precision影响（尽管engine confound fix后影响已minimal），
      LayerCast以acceptable overhead提供FP32-equivalent numerical behavior。
    tables:
      - name: "Table 18: 4-Precision Mode Comparison"
        columns: ["Mode", "Accuracy", "Agreement w/ FP32", "Throughput (tok/s)", "VRAM (GB)"]
        rows:
          - ["FP32 (V0 eager)", 0.664, "1.000", 1820, 31.2]
          - ["BF16", 0.669, "0.9987", 2760, 15.8]
          - ["FP16", 0.667, "0.9984", 2810, 15.6]
          - ["LayerCast", 0.668, "0.9993", 2580, 16.2]
    figures_description:
      - "Fig 18: 4-precision accuracy distribution violin plots + LayerCast overlay。
        LayerCast和FP32的distribution几乎identical。"
    analysis: >
      P2实验。LayerCast进一步confirms precision不是major concern（post confound-fix）。
      可作为paper中practical recommendation的一条data point。
      在engine confound已修复的前提下，precision choice是第二优先级的optimization。

  - name: "MATH benchmark extension"
    plan_id: "exp-008"
    description: >
      4 models × 2 precisions (BF16/FP16) × 6 prompts × 6 seeds × 2 temperatures
      × 4 orderings × 200 MATH items。总记录 460,800。
      测试extreme reasoning task的variance structure，延伸cross-benchmark gradient。
    expected_results:
      total_records: 460800
      math_overall_accuracy: 0.324
      math_item_id: 0.210
      math_temperature_x_item: 0.208
      math_seed_x_item: 0.174
      math_prompt_x_item: 0.112
      math_residual: 0.113
      math_ordering_x_item: 0.038
      math_temperature: 0.048
      math_prompt: 0.034
      math_seed: 0.032
      math_precision_x_item: 0.009
      math_ordering: 0.016
      math_precision: 0.002
      math_infra_x_method: 0.002
      math_item_id_rank1: true
      math_g_full_design: 0.50
      math_g_current_practice: 0.10
      math_dstudy_items_for_g90: 120
      math_dstudy_seeds_for_g90: 12
      math_gradient_extends_monotonically: true
    result_rationale: >
      MATH是cross-benchmark gradient的"stress test"。Item_id(21.0%)仅以微弱优势维持rank-1——
      temp×item(20.8%)几乎与之并列。这是5个benchmark中item dominance最弱的，
      因为MATH的multi-step proof-like reasoning生成了最长的CoT（平均4-8步 vs GSM8K的2-4步），
      使每一步的temperature sensitivity在item level cumulative。
      
      具体机制：Level 1 algebra（answer in 1-2 steps）几乎不受temp/seed影响，
      Level 5 competition math（answer in 6-10 steps）对temp/seed极度敏感。
      这种item-level heterogeneity产生了massive interaction terms（temp×item 20.8%, seed×item 17.4%）。
      
      Overall accuracy仅32.4%——接近random guessing baseline(25% for 4-choice)——
      增加了binary scoring下的floor effect，膨胀residual中的"guessing noise"成分。
      
      G current practice仅0.10——5个benchmark中最低。
      这意味着MATH evaluation在current practice下essentially unreliable。
      D-study：G≥0.90需要120 items + 4 prompts + 12 seeds = 5,760 evaluations——
      seed投入最大，是典型的seed-limited benchmark。
      
      5-benchmark gradient完整：MMLU(56%) > ARC(42%) > HellaSwag(34%) > GSM8K(25%) > MATH(21%)。
      Spread扩大到35pp（56-21），pattern perfectly monotonic。
      这quantitatively captures "reasoning intensity ↑ → item_id share ↓"。
    tables:
      - name: "Table 19: Complete 5-Benchmark Variance Gradient"
        columns: ["Benchmark", "Accuracy", "item_id %", "temp×item %", "seed×item %", "G (full)", "G (current)", "Items for G≥0.90", "Seeds for G≥0.90"]
        rows:
          - ["MMLU", 0.667, 56.0, 5.9, 3.0, 0.36, 0.22, 420, 2]
          - ["ARC-Chal.", 0.592, 42.0, 8.6, 6.2, 0.42, 0.20, 320, 4]
          - ["HellaSwag", 0.708, 34.0, 13.2, 10.8, 0.47, 0.18, 240, 6]
          - ["GSM8K", 0.574, 25.0, 18.2, 15.8, 0.55, 0.14, 150, 10]
          - ["MATH", 0.324, 21.0, 20.8, 17.4, 0.50, 0.10, 120, 12]
      - name: "Table 20: MATH Per-Model Breakdown"
        columns: ["Model", "item_id %", "temp×item %", "seed×item %", "Residual %"]
        rows:
          - ["Qwen3-8B", 24.2, 19.4, 16.2, 10.8]
          - ["Llama-3.1-8B", 20.6, 21.8, 18.4, 11.6]
          - ["Gemma-2-9B-IT", 23.4, 19.8, 16.4, 10.4]
          - ["Mistral-7B-v0.3", 17.8, 22.8, 19.4, 12.6]
    figures_description:
      - "Fig 19 [EXTENDED SIGNATURE]: 5-benchmark stacked bars按reasoning intensity排序。
        item_id色块从左到右monotonically shrinks，temp×item和seed×item monotonically grows。
        MATH panel中temp×item和item_id几乎等高——visual 'tipping point'。"
      - "Fig 20: D-study projection curves 5-benchmark overlay。
        X轴=total evaluations，Y轴=G。MATH曲线最右（需最多evaluations for G≥0.90），
        但通过seed-heavy allocation其slope与GSM8K comparable。"
      - "Fig 21: item_id % vs temp×item % scatter — 5 benchmarks × 4 models = 20 points。
        Near-perfect negative correlation (r≈-0.94)，直观展示tradeoff。"
    analysis: >
      MATH将gradient从4-benchmark延伸到5-benchmark，35pp spread进一步strengthens
      "no universal recipe"叙事。关键observation：MATH是item dominance的"near-collapse point"——
      item_id(21.0%)和temp×item(20.8%)几乎并列，suggesting that for tasks with even longer
      reasoning chains (e.g., formal proofs, multi-document QA), item_id可能不再是rank-1。
      
      这是P2实验但高度complementary：如果included，paper从4-benchmark gradient
      升级为5-benchmark gradient，trend更convincing，slope estimate更精确。
      
      Policy implication最强：MATH evaluation在current practice下G=0.10，
      essentially不能reproducibly differentiate models。
      推荐：至少12 seeds + 120 items + 4 prompts for minimal reliability。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8439739c-1316-4c65-a636-665c6f416340",
  "isSidechain": false,
  "requestId": "req_011CbEbzMuSN9caiuCJY27HN",
  "type": "assistant",
  "uuid": "04119d03-c79b-401b-88f7-6b85a910b209",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMUVGyQV7GG74d57fhCF2v",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 33573,
      "cache_read_input_tokens": 28683,
      "output_tokens": 60425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 60425,
          "cache_read_input_tokens": 28683,
          "cache_creation_input_tokens": 33573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33573
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Cross-benchmark gradient clear and monotonic; all three claims hold as framed; AAAI submission proceeds without claim weakening 核心假设：['Item dominance on MM…",
  "leafUuid": "04119d03-c79b-401b-88f7-6b85a910b209",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "G-theory variance decomposition across LLM benchmarks",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Cross-benchmark gradient clear and monotonic; all three claims hold as framed; AAAI submission proceeds without claim weakening 核心假设：['Item dominance on MM…",
  "leafUuid": "04119d03-c79b-401b-88f7-6b85a910b209",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "G-theory variance decomposition across LLM benchmarks",
  "sessionId": "23357e26-9b8d-4d36-9720-249b9bfdef30"
}
```

---
