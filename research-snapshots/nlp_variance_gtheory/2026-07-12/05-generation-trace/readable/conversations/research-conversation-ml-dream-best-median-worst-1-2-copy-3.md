# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/d5e31096-55f1-47ed-b249-5208c5c4996e.jsonl`
- **Structured JSON:** [`4e3e6d133902cfbecac4.json`](../../sessions/4e/4e3e6d133902cfbecac4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:47:48.240Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:47:48.240Z",
  "sessionId": "d5e31096-55f1-47ed-b249-5208c5c4996e",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: nlp_variance_gtheory\nfocus: Re-dream #3 after major improvements: (1) Cross-model G-study reveals model×item=26.2% as second-largest source, G collapses 0.611→0.073 — strongest finding so far; (2) 6 methodological robustness analyses completed (Bernoulli non-artifact, fixed/random insensitive, bootstrap=jackknife, temperature stratification, D-study verified, IRT vs G-theory 4× gap); (3) Added 4th contribution: practitioner toolkit (open-source G-theory pipeline + D-study calculator); (4) 5 concrete figures planned; (5) 9 Methodological Defenses (MD1-MD9) explicitly addressing every Dream #2 reviewer concern; (6) Claim 1 upgraded from \"item dominance\" to \"model-conditional item dominance\" based on actual 2-model data; (7) IRT vs G-theory comparison as standalone contribution. Key question: do these changes push median above weak accept and worst above borderline?\n\n## paper_framing.md\n\n# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Model-Conditional Item Dominance**: Item selection is the single largest variance source in single-model LLM evaluation (61.1% on MMLU), but model×item interaction (26.2%) emerges as the second-largest source when model is treated as a crossed facet — collapsing cross-model generalizability (G: 0.611→0.073). Item difficulty rankings are model-specific: two models with similar aggregate accuracy (Llama 66.4% vs Gemma 73.2%) disagree dramatically at the item level. This means single-model variance decompositions provide a false sense of reliability. Cross-benchmark gradient (pending exp-002) is hypothesized to further modulate this structure.\n**Empirical anchors (exp-001, 2 models, 325,600 records)**: Single-model item_id=61.1%, cross-model item_id=37.9% (↓23pp), model×item=26.2%, cross-model G=0.073. D-study: even 10 models yield G=0.179 — model×item interaction is irreducible by adding models.\n**Fallback narratives**: (A) If 4-model analysis confirms 2-model trend → \"model×item interaction is a fundamental barrier to cross-model generalizability\"; (B) If 4-model analysis shows stabilization (item_id rebounds) → \"2-model analysis overestimates model-specificity\"; (C) Cross-benchmark gradient confirmed → additional dimension of conditionality.\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent and temperature-conditional. Binary correct: G=0.611 (200 items), G≥0.80 requires ~510 items (all facets random) or ~414 items (practical: precision+temperature fixed). Text-exact-match: G=0.007 (temperature dominates at 79.7%), unreliable at any temperature >0. Temperature-stratified analysis reveals binary G degrades monotonically (T=0.0: 0.760 → T=0.7: 0.549). G-theory requires 3.6-4.4× more items than IRT (510 vs 116) because it accounts for prompt×item (4.6%), seed×item (4.7%), and residual (21.6%) dimensions that IRT ignores. Current practices (1 prompt, 1 seed, ≤200 items) yield G=0.611 — below the 0.80 threshold for dependable measurement.\n\n## Contributions (4 条，明确区分)\n\n1. **Model×item interaction as the hidden dominant source**: When model is treated as a crossed facet, model×item interaction (26.2%) emerges as the second-largest variance source, collapsing cross-model G from 0.611 to 0.073. Item difficulty rankings are model-specific — single-model G-studies provide false confidence. This is the first quantification of cross-model item-level disagreement in LLM evaluation via G-theory.\n\n2. **Confirmatory separability with metric qualification**: Infrastructure×methodology interactions are negligible under binary scoring (<0.1%), providing empirical support for isolated-factor studies. Under text-exact-match scoring, precision×temperature reaches 4.15%, consistent with floating-point non-associativity. Separability is confirmed as metric-conditional and benchmark-conditional (knowledge benchmarks only).\n\n3. **IRT vs G-theory: the cost of multi-facet reliability**: The first direct comparison showing G-theory requires 3.6-4.4× more items than IRT (510 vs 116 for MMLU) because it accounts for prompt, seed, and ordering dimensions that IRT ignores. At IRT's recommended 116 items, G-theory G is only 0.529. This quantifies the \"hidden cost\" of evaluation dimensions invisible to IRT.\n\n4. **Practitioner toolkit**: Open-source G-theory variance decomposition pipeline + D-study budget calculator for LLM evaluation. Includes: (a) benchmark-specific reproducibility budget tables (items × prompts × seeds for target G), (b) temperature-stratified reliability guide, (c) model-as-facet analysis template. Addresses \"purely diagnostic\" criticism — provides actionable tools, not just warnings.\n\n## Methodological Robustness Package (6 验证分析)\nAll completed on Llama 239,200 records:\n- **Binary data not artifact**: Null simulation item_id=0.08% vs observed 61.1% (737.5×); obs/Bernoulli ratio=1.0008\n- **Fixed vs random insensitive**: Binary G ranges 0.611-0.664 across all facet classification choices\n- **Bootstrap = jackknife**: CI width ratio 0.96-1.04, independence violation negligible\n- **Temperature stratification**: Binary G degrades T=0.0 (0.760) → T=0.7 (0.549); text metric unreliable at all T>0\n- **D-study formula verified**: Monotonicity assertion added; min_items_G80=414 (practical) / 510 (all random)\n- **IRT comparison**: G-theory 3.6-4.4× more conservative than IRT; difference attributable to prompt/seed/ordering dimensions\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of 5,184 conditions across 4 models on MMLU (200 items), item selection accounts for 61% of variance in single-model evaluation but only 38% when model is treated as a crossed facet — with model×item interaction (26%) emerging as the second-largest source. Cross-model generalizability collapses from G=0.61 to G=0.07, revealing that item difficulty rankings are model-specific. G-theory requires 4× more items than IRT to achieve reliable measurement because it accounts for prompt, seed, and ordering dimensions that IRT ignores. Direct infrastructure×methodology interactions are negligible (<0.1% under binary scoring). We release an open-source G-theory toolkit for practitioners to compute benchmark-specific reproducibility budgets.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (5 figures):\n  1. **Stacked-bar: single-model vs cross-model variance decomposition** — item_id shrinks from 61% to 38%, model×item appears at 26%. The \"reveal\" figure.\n  2. **G-theory crossed design diagram** — facets, levels, crossing structure\n  3. **D-study projection curves** — G vs item count for binary (practical vs all-random) and text metric. Shows G≥0.80 threshold at ~414/510 items.\n  4. **IRT vs G-theory item requirement comparison** — bar chart showing 116 (IRT) vs 510 (G-theory) items, with breakdown of where the extra items go (prompt×item, seed×item, residual)\n  5. **Temperature-stratified G coefficient heatmap** — binary vs text metric × 3 temperatures, showing metric×temperature interaction\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).\n\n## Methodological Defenses (Dream #2 审稿问题逐条应对)\n\n### MD1. Binary Data in G-theory\n**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).\n**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is \"mechanical\" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.\n\n### MD2. Fixed vs Random Facet Sensitivity\n**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.\n**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.\n\n### MD3. Separability Claim Scope\n**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).\n**Defense**: Qualify all separability claims as \"under binary scoring on knowledge-retrieval benchmarks.\" Present benchmark-conditional separability as a finding (not a limitation): \"separability itself varies across task types.\"\n\n### MD4. D-study Optimization Documentation\n**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).\n**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).\n\n### MD5. G-coefficient Interpretation\n**Issue**: G=0.22 for 200 items ≠ \"MMLU is unreliable\" (standard MMLU uses ~14K items).\n**Defense**: (a) Clearly distinguish \"G for our 200-item subsample design\" from \"reliability of full MMLU\"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as \"cost of subsampling\" rather than \"MMLU is broken.\"\n\n### MD6. Bootstrap Independence\n**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.\n**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.\n\n### MD7. IRT vs G-theory Comparison\n**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.\n**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the \"cost of multi-facet reliability\" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.\n\n### MD8. Cross-benchmark Design Asymmetry\n**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.\n**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.\n\n### MD9. Title-Content Alignment\n**Issue**: Title promises \"Evaluation Metrics\" but logprob analysis is minimal.\n**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to \"...Across Benchmarks and Models.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Full-scale precision study: 4 models (Qwen3-8B, Llama-3.1-8B-Instruct,\n    Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3) × 3 precisions (FP32, BF16, FP16) × 6\n    prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items (stratified).\n    All precisions use consistent vLLM engine (V0 enforce_eager) to eliminate the\n    float32 engine confound found in MVP. Validates item dominance finding at scale\n    and with multiple models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 100\n  hardware: westd-32570 (RTX PRO 6000 96GB)\n  deps: []\n  status: planned\n- id: exp-001b\n  claim: 1\n  description: 'Item resampling stability test: 3 independent stratified samples of\n    200 MMLU items (seeds 0, 7, 99) × 1 model (Llama-3.1-8B-Instruct) × 3 precisions\n    × 3 prompts × 3 seeds × 2 orderings = 54 conditions per sample. Tests whether\n    the 58% item dominance finding is stable across different item draws from MMLU,\n    not an artifact of the specific 200-item sample. Critical for defending the headline\n    claim.\n\n    '\n  priority: P0\n  gpu_budget_hours: 15\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Multi-benchmark replication: same 4 models × BF16/FP16 × 6 prompts\n    × 6 seeds × 2 temperatures × 4 orderings on GSM8K (200 items), ARC-Challenge (200\n    items), HellaSwag (200 items). Tests whether item dominance and separability hold\n    across task types (math reasoning, science reasoning, commonsense).\n\n    '\n  priority: P0\n  gpu_budget_hours: 200\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-003\n  claim: 2\n  description: 'Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16,\n    FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. Tests\n    hardware × methodology interaction — the core separability question that MVP couldn''t\n    address with only 1 GPU type.\n\n    '\n  priority: P0\n  gpu_budget_hours: 120\n  hardware: westd-32570 + TBD (second GPU type from Manager)\n  deps: []\n  status: planned\n- id: exp-004\n  claim: 3\n  description: 'Comprehensive analysis of combined exp-001/001b/002/003 data. Includes:\n    (a) Model-as-facet G-theory reanalysis — treat model as crossed random facet to\n    properly attribute model×item interaction and reduce inflated item_id/residual\n    (Dream critical); (b) Bootstrap CIs (1000 resamples) on ALL variance components\n    in ALL tables, especially direct infra×method interaction term (Dream critical);\n    (c) D-study projections with CIs for optimal allocation across facets for G≥0.90/0.95/0.99,\n    with benchmark-specific budgets and comparison to IRT-based subsampling (tinyBenchmarks);\n    (d) REML vs Henderson Method I comparison as sensitivity analysis; (e) Logprob-based\n    scoring as third response variable; (f) Ranking stability analysis — does precision×temperature\n    interaction alter model rankings? (g) Higher-order interaction estimation to decompose\n    the residual component; (h) G-theory vs IRT direct comparison — same MMLU data,\n    D-study vs tinyBenchmarks IRT subsampling, compare recommended item counts and\n    discuss why G-theory is more conservative (accounts for prompt/seed dimensions\n    IRT ignores). First direct comparison in the literature; (i) Power analysis —\n    verify statistical power to detect ≥X% interaction effects given 5184×200 design\n    scale, preempt \"underpowered\" reviewer concern; (j) Practitioner evaluation protocol\n    guide (Discussion/Appendix); (k) Fixed vs random sensitivity — rerun G-study with\n    temperature/ordering as fixed facets, compare variance decomposition (MD2 defense);\n    (l) Binary data limitation analysis — correlate Bernoulli p(1-p) with observed\n    item variance, parallel binary vs text_exact_match analysis (MD1 defense); (m)\n    Bootstrap vs jackknife CI comparison — delete-1 jackknife as independence-safe\n    alternative, compare CI widths (MD6 defense); (n) Cross-benchmark design asymmetry\n    sensitivity — re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7),\n    compare with full 3×3 (MD8 defense); (o) G-coefficient at full benchmark size\n    — D-study projection to 14K MMLU items (MD5 defense); (p) Logprob-based scoring\n    across all benchmarks — expand from MMLU-only to all 5 benchmarks, support \"Evaluation\n    Metrics\" in title (MD9 defense); (q) GPU cost analysis — estimate compute cost\n    for recommended D-study budgets.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  hardware: none\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  status: planned\n- id: exp-005\n  claim: 2\n  description: '14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter\n    GPUs at BF16/FP16. Tests whether variance attribution patterns change with model\n    scale and architecture (dense vs reasoning-distilled).\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  hardware: TBD (needs ≥48GB VRAM per GPU)\n  deps:\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA. Fully crossed:\n    6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task\n    × 4 tasks = 1,728 total fine-tuning runs. Validates whether variance hierarchy\n    differs between inference and fine-tuning.\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  hardware: westd-32570 (RoBERTa-large fits easily on 96GB)\n  deps: []\n  status: planned\n- id: exp-007\n  claim: 2\n  description: 'Test LayerCast (FP16 storage + FP32 compute) as additional precision\n    condition on MMLU. Quantifies variance reduction from this mitigation strategy.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 1\n  description: 'MATH benchmark (200 items) — tests whether item dominance pattern\n    differs for reasoning-heavy tasks where chain-of-thought introduces additional\n    variance.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  hardware: westd-32570\n  deps:\n  - exp-002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase_a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 5400\n    conditions: 108\n    overall_accuracy: 0.6557\n    accuracy_bfloat16: 0.6844\n    accuracy_float16: 0.6833\n    accuracy_float32: 0.5994\n    g_coefficient_correct: 0.357\n    top_variance_correct:\n      item_id: 0.5844\n      residual: 0.1759\n      precision:item_id: 0.0724\n      temperature:item_id: 0.0685\n      prompt_template:item_id: 0.0573\n    top_variance_text_match:\n      residual: 0.407\n      prompt_template:item_id: 0.375\n      temperature: 0.169\n      temperature:item_id: 0.025\n      precision:temperature: 0.013\n    pass_criteria_a_pipeline: true\n    pass_criteria_b_components: true\n    pass_criteria_c_interaction: true\n    pass_criteria_c_detail: precision:temperature 1.3% CI not containing zero (text_exact_match)\n- exp_id: bf16_eager_disentangle\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bf16_v1_accuracy: 0.6844\n    bf16_eager_accuracy: 0.6822\n    fp32_v0_accuracy: 0.5994\n    engine_effect_pct: 2.6\n    precision_effect_pct: 97.4\n    engine_gap_pp: 0.22\n    precision_gap_pp: 8.28\n    total_gap_pp: 8.5\n- exp_id: exp001_pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 20000\n    expected_records: 20000\n    overall_accuracy: 0.616\n    gpu0_acc: 0.605\n    gpu1_acc: 0.622\n    gpu2_acc: 0.627\n    gpu3_acc: 0.61\n    avg_latency_ms: 180.9\n    output_size_mb: 13\n    precision_coverage: float32 only (100 conditions)\n    temperature_coverage: T=0.0 only (100 conditions)\n    fields_complete: true\n- exp_id: exp001_llama\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 239200\n    expected_records: 239200\n    conditions: 1196\n    items_per_condition: 200\n    overall_accuracy: 0.6814\n    accuracy_bfloat16: 0.7108\n    accuracy_float16: 0.7114\n    accuracy_float32: 0.604\n    accuracy_T0.0: 0.6987\n    accuracy_T0.3: 0.6795\n    accuracy_T0.7: 0.6699\n    null_predictions: 42\n    null_pct: 0\n- exp_id: exp001_gemma\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 172800\n    bf16_records: 86400\n    fp32_records: 86400\n    fp16_records: 0\n    precisions_available:\n    - bfloat16\n    - float32\n    fp16_note: Gemma2 does not support float16 (vLLM numerical instability)\n    conditions_bf16: 432\n    conditions_fp32: 432\n    total_conditions: 864\n    items_per_condition: 200\n- exp_id: exp001_mistral\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T04:47:48.244Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:47:48.244Z",
  "sessionId": "d5e31096-55f1-47ed-b249-5208c5c4996e"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-21T04:47:48.277Z_

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
focus: Re-dream #3 after major improvements: (1) Cross-model G-study reveals model×item=26.2% as second-largest source, G collapses 0.611→0.073 — strongest finding so far; (2) 6 methodological robustness analyses completed (Bernoulli non-artifact, fixed/random insensitive, bootstrap=jackknife, temperature stratification, D-study verified, IRT vs G-theory 4× gap); (3) Added 4th contribution: practitioner toolkit (open-source G-theory pipeline + D-study calculator); (4) 5 concrete figures planned; (5) 9 Methodological Defenses (MD1-MD9) explicitly addressing every Dream #2 reviewer concern; (6) Claim 1 upgraded from "item dominance" to "model-conditional item dominance" based on actual 2-model data; (7) IRT vs G-theory comparison as standalone contribution. Key question: do these changes push median above weak accept and worst above borderline?

## paper_framing.md

# Paper Framing — nlp_variance_gtheory

## Target Venue
- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
- Extended: TACL (rolling)

## Title
Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics

## Core Claims (3 条，可证伪)

**Claim 1 — Model-Conditional Item Dominance**: Item selection is the single largest variance source in single-model LLM evaluation (61.1% on MMLU), but model×item interaction (26.2%) emerges as the second-largest source when model is treated as a crossed facet — collapsing cross-model generalizability (G: 0.611→0.073). Item difficulty rankings are model-specific: two models with similar aggregate accuracy (Llama 66.4% vs Gemma 73.2%) disagree dramatically at the item level. This means single-model variance decompositions provide a false sense of reliability. Cross-benchmark gradient (pending exp-002) is hypothesized to further modulate this structure.
**Empirical anchors (exp-001, 2 models, 325,600 records)**: Single-model item_id=61.1%, cross-model item_id=37.9% (↓23pp), model×item=26.2%, cross-model G=0.073. D-study: even 10 models yield G=0.179 — model×item interaction is irreducible by adding models.
**Fallback narratives**: (A) If 4-model analysis confirms 2-model trend → "model×item interaction is a fundamental barrier to cross-model generalizability"; (B) If 4-model analysis shows stabilization (item_id rebounds) → "2-model analysis overestimates model-specificity"; (C) Cross-benchmark gradient confirmed → additional dimension of conditionality.

**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), "infrastructure" is currently limited to the precision facet.

**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent and temperature-conditional. Binary correct: G=0.611 (200 items), G≥0.80 requires ~510 items (all facets random) or ~414 items (practical: precision+temperature fixed). Text-exact-match: G=0.007 (temperature dominates at 79.7%), unreliable at any temperature >0. Temperature-stratified analysis reveals binary G degrades monotonically (T=0.0: 0.760 → T=0.7: 0.549). G-theory requires 3.6-4.4× more items than IRT (510 vs 116) because it accounts for prompt×item (4.6%), seed×item (4.7%), and residual (21.6%) dimensions that IRT ignores. Current practices (1 prompt, 1 seed, ≤200 items) yield G=0.611 — below the 0.80 threshold for dependable measurement.

## Contributions (4 条，明确区分)

1. **Model×item interaction as the hidden dominant source**: When model is treated as a crossed facet, model×item interaction (26.2%) emerges as the second-largest variance source, collapsing cross-model G from 0.611 to 0.073. Item difficulty rankings are model-specific — single-model G-studies provide false confidence. This is the first quantification of cross-model item-level disagreement in LLM evaluation via G-theory.

2. **Confirmatory separability with metric qualification**: Infrastructure×methodology interactions are negligible under binary scoring (<0.1%), providing empirical support for isolated-factor studies. Under text-exact-match scoring, precision×temperature reaches 4.15%, consistent with floating-point non-associativity. Separability is confirmed as metric-conditional and benchmark-conditional (knowledge benchmarks only).

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

## Story Spine

**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.

**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.

**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.

**Headline result template**: "In a G-study of 5,184 conditions across 4 models on MMLU (200 items), item selection accounts for 61% of variance in single-model evaluation but only 38% when model is treated as a crossed facet — with model×item interaction (26%) emerging as the second-largest source. Cross-model generalizability collapses from G=0.61 to G=0.07, revealing that item difficulty rankings are model-specific. G-theory requires 4× more items than IRT to achieve reliable measurement because it accounts for prompt, seed, and ordering dimensions that IRT ignores. Direct infrastructure×methodology interactions are negligible (<0.1% under binary scoring). We release an open-source G-theory toolkit for practitioners to compute benchmark-specific reproducibility budgets."

## Hook (Counter-Intuitive Quantified Claim)
"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory."

## Narrative Strategy
- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)
- **Tension**: "No universal recipe" — the field seeks standardization but variance structure varies qualitatively across task types
- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)
- **Figure plan** (5 figures):
  1. **Stacked-bar: single-model vs cross-model variance decomposition** — item_id shrinks from 61% to 38%, model×item appears at 26%. The "reveal" figure.
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
  status: RUNNING
  conclusion: ''
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
  "promptId": "88f2ba13-9ed3-4e4a-aef8-26d367f0631f",
  "type": "user",
  "uuid": "6132ec4e-955d-436c-aee0-37bacf5d50ef",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "d5e31096-55f1-47ed-b249-5208c5c4996e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:47:48.275Z_

```json
{
  "parentUuid": "6132ec4e-955d-436c-aee0-37bacf5d50ef",
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
  "uuid": "6d54ffd6-60e5-4bde-93d8-39063ebb7d84",
  "timestamp": "2026-05-21T04:47:48.275Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "d5e31096-55f1-47ed-b249-5208c5c4996e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:47:48.275Z_

```json
{
  "parentUuid": "6d54ffd6-60e5-4bde-93d8-39063ebb7d84",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7cb4d6f0-cb5a-4d74-b3cc-8a04427461f0",
  "timestamp": "2026-05-21T04:47:48.275Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "d5e31096-55f1-47ed-b249-5208c5c4996e",
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
  "leafUuid": "7cb4d6f0-cb5a-4d74-b3cc-8a04427461f0",
  "sessionId": "d5e31096-55f1-47ed-b249-5208c5c4996e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for Dream LLM evaluation variance G-theory study",
  "sessionId": "d5e31096-55f1-47ed-b249-5208c5c4996e"
}
```

---

### Assistant

_source line 8 · 2026-05-21T04:49:11.385Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to define three tiers (best/median/worst) for a Dream simulation based on the research context provided. Let me analyze the research carefully.

Key findings so far (from exp-001 with 2 models: Llama + Gemma):
- Single-model item_id = 61.1%
- Cross-model item_id = 37.9%
- model×item = 26.2%
- Single-model G = 0.611
- Cross-model G = 0.073
- D-study: 10 models → G = 0.179
- Infrastructure×methodology < 0.1% (binary)


- Precision×temperature accounts for 1.3% of variance in exact match scoring
- IRT and G-theory show a substantial gap in item counts (510 vs 116)
- Temperature has a notable effect on reliability, dropping from 0.760 at T=0.0 to 0.549 at T=0.7
- I've completed six methodological robustness checks

I'm waiting on Mistral results to complete the four-model analysis, with Qwen still queued. Beyond that, I need to run experiments across multiple benchmarks and different hardware configurations.

The critical questions are whether the four-model setup will hold the model×item interaction I found with two models, whether reasoning tasks show a different pattern than other benchmarks, and whether hardware differences matter for the separability claim. I have nine weeks until the AAAI deadline, so timing is tight. The best outcome would be all three experiments confirming the core findings with a clean narrative, though realistically the four-model analysis might show some attenuation of the original effect.

Now I'm defining what success looks like across different scenarios. In the median case, the model×item effect persists but weakens somewhat, the cross-benchmark gradient exists but with noise, and I'd need to dial back some claims. The worst case would be if the four-model analysis reveals the two-model finding was an artifact—item_id rebounds and the model×item interaction collapses, forcing a complete reframe. I'm tracking specific metrics: the cross-model item_id percentage, the model×item percentage, the cross-model G coefficient, and how item dominance varies across MMLU, GSM8K, ARC, and HellaSwag to see if reasoning tasks behave differently. Writing YAML output...

Actually, I need to think through the worst-case reframing more carefully. Even if the model×item interaction collapses with the 4-model analysis and no systematic gradient emerges across benchmarks, I can still anchor the narrative around the robustness of Claim 3 since it's grounded in the data I've already collected, pivot to comparing IRT and G-theory as the methodological contribution, or emphasize the framework validation across all six analyses. The practitioner toolkit remains viable regardless.

For a venue like AAAI, the worst-case positioning would lead with metric-conditional reproducibility budgets and the IRT versus G-theory comparison as the main story, treating the model×item findings as an interesting secondary result rather than the headline, while positioning cross-benchmark evidence as preliminary. The single-model findings are solid anchors—the 61.1% item variance, G-coefficient of 0.611 for 200 items, D-study projections, and temperature stratification all hold up independently.

Now I need to define the metric ranges properly to maintain best ≥ median ≥ worst consistency. Defining the key metrics... I need to clarify the directionality issue—some metrics improve the paper when they're lower (like cross_model_G and infra×method interaction), while others improve it when they're higher. The user's constraint about "best ≥ median ≥ worst" consistency means the tiers should be logically ordered, not that every number must literally be greater than the previous one. I'll define clear ranges for each metric and note which direction indicates better performance.

Now looking at the critical path: exp-001 is about 70% complete across the four models, and it's blocking both the stability analysis and the multi-benchmark work. With nine weeks until AAAI, I need to prioritize ruthlessly—getting all P0 experiments done would be ideal, but realistically I should aim for exp-001 fully finished plus at least partial results from the multi-hardware experiment, with the analysis-only work filling in gaps if time allows.

For the metrics themselves, I'm refining the expected ranges based on what the 2-model baseline shows. The model-by-item interaction effect should either hold steady or slightly decrease as I add more models, while the cross-model G statistic should remain very low if the "collapse" hypothesis is correct. Writing out the YAML configuration now with these constraints in mind. I'm settling on a cleaner set of metrics for the YAML output: the headline percentage for model×item effects, the cross-model collapse metric, the range of item performance across benchmarks, whether a clear gradient is evident, whether multi-hardware experiments validate separability, and the fraction of P0 work completed by deadline. Now I'm defining what constitutes best, median, and worst performance for each tier—best tier needs the 4-model analysis to show strong item effects with minimal collapse, clear cross-benchmark gradients, multi-hardware validation, all P0s done, and stability from resampling. remains significant. Cross-benchmark gradient exists but is noisy with only 2-3 of 4 benchmarks aligning. Multi-hardware testing is blocked or incomplete, limited to precision analysis. The first two experiments are complete while the third is partial. Item resampling demonstrates moderate stability with variance under 30% across samples.

In the worst case, the 4-model result drops below 10%, suggesting the 2-model finding was overstated. There's no clear cross-benchmark gradient, multi-hardware testing remains blocked, and only the first experiment is fully done. Item resampling could show instability with inconsistent variance patterns across different 200-item samples.

Looking at how these scenarios play out narratively: if results hold, the model×item barrier finding is confirmed across 4 models and benchmarks, validating all three claims and supporting all contributions—positioning the paper strongly for AAAI. In a median scenario, I'd need to soften the first claim to acknowledge that model-conditional item difficulty varies by benchmark, scope the infrastructure work to precision only, and lean more heavily on the toolkit contribution to strengthen the novelty pitch. In the worst case, the headline finding doesn't survive at 4-model scale, so I'd pivot to leading with metric-conditional reproducibility budgets and the IRT versus G-theory comparison as primary contributions, treating model×item as a preliminary observation rather than the main story.

Now I'm ready to write out the YAML configuration. But first, let me double-check the numeric ranges to make sure they're properly ordered and realistic. For the model×item percentage across 4 models, the best case should be higher than the median, which should be higher than the worst. I need to verify there's no overlap or gaps that would make the ranges unrealistic. Same check for the cross-model G coefficient—making sure the ranges reflect the expected ordering where best shows stronger generalization than worst.

Writing YAML config... I should include the single-model baseline metrics too, though those are already locked in. Let me focus on the uncertain metrics and write out the YAML configuration now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cb4d6f0-cb5a-4d74-b3cc-8a04427461f0",
  "isSidechain": false,
  "requestId": "req_011CbF7FGaW7rsgKVSr99AdC",
  "type": "assistant",
  "uuid": "16d81d69-21a8-45e3-9c31-612faf0adefa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "d5e31096-55f1-47ed-b249-5208c5c4996e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014fHQRdo6gT1exReZKq5vvV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14427,
      "cache_read_input_tokens": 11841,
      "output_tokens": 5925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 5925,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14427
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

_source line 9 · 2026-05-21T04:49:59.621Z_

```yaml
tiers:
  best:
    meaning: "4-model交叉分析完全验证2-model趋势，跨benchmark梯度清晰可解释，所有P0实验按时完成"
    key_assumptions:
      - "4-model G-study中 model×item 交互维持≥20%，确认为不可约的第二大方差来源"
      - "跨模型G系数保持极低(<0.10)，'G崩塌'叙事成立"
      - "跨benchmark梯度单调：知识检索(MMLU)→常识(HellaSwag)→推理(GSM8K)，item dominance系统性递减"
      - "exp-001b item重采样显示方差结构稳定（三组200-item样本间item_id变异<15%）"
      - "exp-003多硬件确认separability（hardware×methodology <1% binary）"
      - "所有5个P0实验在AAAI截稿前完成"
    number_ranges:
      model_x_item_pct_4model: [20, 30]
      cross_model_G_4model: [0.03, 0.10]
      single_model_item_id_pct: [55, 65]
      benchmark_item_id_spread_pp: [25, 40]
      benchmark_gradient_rank_corr: [0.80, 1.00]
      infra_x_method_binary_pct: [0.0, 0.5]
      irt_vs_gtheory_item_ratio: [3.5, 5.0]
      resampling_item_id_cv: [0.02, 0.08]
      p0_experiments_completed: [5, 5]
    narrative_direction: >
      原始framing完全成立。标题不变。三条Claims均有充分实证支撑。
      Claim 1升级为"model-conditional item dominance is a fundamental barrier to cross-model generalizability"，
      4模型+4benchmark数据链完整。Claim 2从"precision-only"扩展为"infrastructure separability"，
      多硬件数据补齐。Claim 3的D-study预算表覆盖4个benchmark，IRT vs G-theory对比作为独立贡献成立。
      Contribution 4工具包附带benchmark-specific budget表。
      Hook改为量化版："跨4个benchmark和4个模型，方差结构本身是benchmark-conditional的"。
      投稿AAAI，目标weak accept以上（6.0+/10）。

  median:
    meaning: "4-model分析部分确认但model×item有所衰减，跨benchmark梯度存在但有噪声，exp-003未完成"
    key_assumptions:
      - "4-model G-study中 model×item 衰减至12-20%——仍为显著方差来源但非'dominant'"
      - "跨模型G系数上升至0.10-0.22——仍远低于0.80阈值，但'崩塌'措辞需弱化"
      - "跨benchmark梯度方向正确但非单调（4个benchmark中3个符合预期，1个异常）"
      - "exp-001b重采样稳定性中等（item_id变异15-30%）"
      - "exp-003因第二块GPU未到位而缺失或仅有部分数据；separability仅限precision维度"
      - "P0实验完成4/5（exp-003缺失或不完整）"
    number_ranges:
      model_x_item_pct_4model: [12, 20]
      cross_model_G_4model: [0.10, 0.22]
      single_model_item_id_pct: [55, 65]
      benchmark_item_id_spread_pp: [10, 25]
      benchmark_gradient_rank_corr: [0.40, 0.80]
      infra_x_method_binary_pct: [0.0, 1.0]
      irt_vs_gtheory_item_ratio: [3.0, 4.5]
      resampling_item_id_cv: [0.08, 0.18]
      p0_experiments_completed: [3, 4]
    narrative_direction: >
      Claims需要校准强度。Claim 1降级："model×item interaction is a substantial but not dominant
      variance source that significantly degrades cross-model reliability"——去掉"hidden dominant"措辞，
      改为"non-negligible and previously unquantified"。标题中"Variance Sources"保留但摘要措辞软化。
      跨benchmark梯度从"primary novel finding"降为"suggestive evidence of benchmark-conditional
      variance structure"，需补充讨论异常benchmark的原因。Claim 2将"infrastructure"限定为
      "numerical precision on single hardware"，明确标注hardware crossing为future work。
      Claim 3和IRT对比不受影响，可能需要提升为论文第一贡献以补偿Claim 1弱化。
      Contribution 4工具包的实用价值需要强化论证。
      补充实验：增加exp-001b第二轮验证item稳定性；或将exp-006(fine-tuning)部分结果
      作为额外贡献拉入。投稿AAAI仍可行但需精心打磨framing，目标borderline accept（5.5-6.0/10）。

  worst:
    meaning: "4-model分析显示2-model结果被放大，无可解释的跨benchmark梯度，多个P0实验缺失"
    key_assumptions:
      - "4-model G-study中 model×item 降至<10%——2-model结果因Llama/Gemma架构差异被夸大"
      - "跨模型G系数回升至0.22-0.40——仍非'高可靠'但'崩塌'叙事不成立"
      - "跨benchmark方差结构无系统性规律——各benchmark表现idiosyncratic，无可解释梯度"
      - "exp-001b重采样显示item_id不稳定（变异>30%），200-item子集方差结构依赖具体抽样"
      - "exp-003完全缺失；exp-002仅完成1-2个benchmark"
      - "P0实验仅完成2-3个"
    number_ranges:
      model_x_item_pct_4model: [2, 10]
      cross_model_G_4model: [0.22, 0.40]
      single_model_item_id_pct: [50, 65]
      benchmark_item_id_spread_pp: [0, 10]
      benchmark_gradient_rank_corr: [0.00, 0.40]
      infra_x_method_binary_pct: [0.0, 2.0]
      irt_vs_gtheory_item_ratio: [2.5, 4.0]
      resampling_item_id_cv: [0.18, 0.40]
      p0_experiments_completed: [2, 3]
    narrative_direction: >
      核心reframe：放弃model×item作为headline finding，整篇论文重心从"variance source discovery"
      转向"G-theory as a framework for metric-conditional evaluation reliability"。
      新Claim 1：Metric-conditional reproducibility budgets——binary vs text-exact-match的G系数
      差异(0.611 vs 0.007)作为headline数字，这基于已完成的Llama数据，不依赖4-model结果。
      新Claim 2：IRT vs G-theory直接对比——3.6-4.4×的item需求差异作为standalone finding，
      论证G-theory捕获了IRT忽略的prompt/seed/ordering维度，这是文献中首个此类对比。
      新Claim 3：原Claim 1降为"preliminary evidence"——model×item在2-model设计中显著(26%)
      但随模型数增加衰减，讨论可能原因并标注为需更大规模验证。
      标题调整为"Reproducibility Budgets for LLM Evaluation: Why G-theory Demands 4× More
      Items Than IRT"——突出IRT对比而非方差分解。
      Contribution 4工具包升级为主要卖点之一——"不仅是诊断，是可操作的评估设计工具"。
      温度分层分析(已完成)和6项方法学鲁棒性验证(已完成)成为论文方法学贡献的核心。
      仍投AAAI同一track，目标borderline（5.0-5.5/10），但有清晰的rebuttal策略。
      若时间允许，将exp-002剩余benchmark数据作为camera-ready补充。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16d81d69-21a8-45e3-9c31-612faf0adefa",
  "isSidechain": false,
  "requestId": "req_011CbF7FGaW7rsgKVSr99AdC",
  "type": "assistant",
  "uuid": "f75770f5-6003-4e5e-abf8-bcf2764b5fb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "d5e31096-55f1-47ed-b249-5208c5c4996e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014fHQRdo6gT1exReZKq5vvV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14427,
      "cache_read_input_tokens": 11841,
      "output_tokens": 5925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 5925,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14427
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
  "leafUuid": "f75770f5-6003-4e5e-abf8-bcf2764b5fb4",
  "sessionId": "d5e31096-55f1-47ed-b249-5208c5c4996e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for Dream LLM evaluation variance G-theory study",
  "sessionId": "d5e31096-55f1-47ed-b249-5208c5c4996e"
}
```

---
