# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：item dominance复现但幅度下降或跨benchmark不一致，separability大体成立但存在局部例外，需要softening cl

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/dc99552f-0d16-4424-a3ed-04aae8dce6f0.jsonl`
- **Structured JSON:** [`d90572f89015e49e665f.json`](../../sessions/d9/d90572f89015e49e665f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:05:59.419Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:05:59.419Z",
  "sessionId": "dc99552f-0d16-4424-a3ed-04aae8dce6f0",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：item dominance复现但幅度下降或跨benchmark不一致，separability大体成立但存在局部例外，需要softening claims并补充条件限定\n核心假设：[\"float32 confound修复后item_id方差占比下降10-15个百分点（部分'item dominance'被precision×item interaction人为放大）\", '第二块GPU延迟或只能做reduced crossing，hardware facet数据不完整', 'GSM8K等reasoning benchmark的方差结构与MMLU显著不同（residual/temperature占比更高，item dominance减弱）', '4个模型中1-2个模型表现异常（如Gemma的prompt sensitivity异常高），方差归因不完全一致']\n关键指标范围：{'item_variance_share_mmlu': [0.32, 0.48], 'item_variance_share_other_benchmarks': [0.2, 0.4], 'direct_infra_method_interaction': [0.01, 0.05], 'item_conditional_interactions_total': [0.1, 0.25], 'precision_main_effect_after_fix': [0.003, 0.015], 'hardware_main_effect': [0.005, 0.03], 'g_current_practice': [0.35, 0.55], 'g_optimized_triple_items': [0.75, 0.9], 'cross_benchmark_replication_rate': [0.5, 0.75], 'models_showing_consistent_pattern': [2, 3]}\n叙事方向：Claim 1从'more than all others combined'降级为'single largest source'，不再用58%作为headline，改用跨benchmark的range（如30-55%）。Claim 2的separability加条件限定：'at the aggregate level for multiple-choice benchmarks'，承认reasoning tasks中temperature和seed的interaction更大。Claim 3的D-study budget表仍成立但效果量缩小——tripling items从10×变为3-5×优于tripling prompts。如果第二块GPU未到，hardware facet降级为limitation而非contribution。论文重心从'surprising dominance'转向'benchmark-dependent variance structure'——不同任务类型需要不同的reproducibility budget，这本身是novel finding。仍可投AAAI但需要更强的writing来sell weaker numbers；准备ACL ARR作为backup。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: nlp_variance_gtheory\nfocus: Key questions: (1) Is the \"item dominance\" finding (58.4%) novel enough for AAAI, or will reviewers dismiss it as obvious? (2) Does the separability result (direct infra×method <0.5%) constitute a strong enough contribution, or is it a null result? (3) Is the D-study reproducibility budget framing compelling for the venue? (4) float32 engine confound — does it undermine credibility? (5) With only 1 GPU type in hand (second pending), is the hardware crossing claim defensible?\n\n## paper_framing.md\n\n# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Item Dominance**: Item selection is the single largest uncontrolled variance source in LLM evaluation, contributing more than prompt phrasing, random seed, temperature, numerical precision, and hardware type combined. (MVP evidence: item_id = 58.4% of total variance vs all other factors combined < 25%)\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (hardware type, numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level (direct interaction < 0.5% of total variance), but both interact substantially with item difficulty — their effects are item-conditional, not universal. This provides an empirical license for isolated-factor studies while warning that their conclusions are conditional on item selection.\n\n**Claim 3 — Reproducibility Budget**: G-theory D-study projections yield quantitative reproducibility budgets showing that increasing item sampling is orders of magnitude more cost-effective than increasing prompt/seed replication for achieving reliable model comparisons (G ≥ 0.90). Current common practices (1 prompt, 1 seed, ≤200 items) produce G < 0.40.\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability between infrastructure and methodology layers.\n\n**Existing approaches & gaps**: Mesting (2026) applied G-theory to 5 methodological facets but treated infrastructure as fixed background. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision but without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance but on fixed hardware. No study crosses both layers in a unified G-theory framework, and critically, no study has quantified the role of item selection relative to all other sources.\n\n**Our framing**: We conduct the first fully-crossed G-theory study spanning infrastructure (hardware type, numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors. The separability test has two equally publishable outcomes: if interactions are negligible, we grant an empirical license to isolated-factor studies; if substantial, we demonstrate that existing conclusions need hardware/prompt qualification. Our MVP reveals a third, unexpected finding: item selection dominates everything (58.4%), making it the overlooked key to evaluation reproducibility.\n\n**Headline result template**: \"In a fully-crossed G-study of K conditions across M models and N benchmarks, item selection accounts for >50% of total evaluation variance, while direct infrastructure × methodology interactions contribute <0.5%. Current evaluation practices achieve G < 0.40; our D-study reproducibility budgets show that tripling item count is 10× more effective than tripling prompt count for reaching G ≥ 0.90.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs — item selection alone accounts for 58% of total evaluation variance, more than all other factors combined.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Breaking limitations (separability assumption challenge)\n- **Tension**: \"Everyone's optimizing the wrong thing\" — the field focuses on prompt/seed/hardware standardization while ignoring item selection\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart (field idiom from Mesting/Brittlebench)\n- **Figure flow**: Problem illustration → G-theory facet diagram → Stacked-bar variance decomposition → D-study projection curves\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer contribution. The novelty is the facet structure crossing infrastructure × methodology, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious — harder items have more variance\" — Counter: (a) the magnitude (58%) was not previously quantified; (b) item×factor interactions (7% precision×item) are non-obvious; (c) the D-study implications for evaluation design are novel.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this\n2. **\"float32 engine confound\"** → exp-001 fixes with consistent vLLM engine settings (V0 enforce_eager for all)\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa)\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support. Documented as hardware compatibility requirement.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Full-scale precision study: 4 models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT,\n    Mistral-7B-v0.3) × 3 precisions (FP32, BF16, FP16) × 6 prompts × 6 seeds × 3 temperatures\n    × 4 orderings × 200 MMLU items (stratified). All precisions use consistent vLLM\n    engine (V0 enforce_eager) to eliminate the float32 engine confound found in MVP.\n    Validates item dominance finding at scale and with multiple models.\n\n    '\n  priority: P0\n  gpu_budget_hours: 100\n  hardware: westd-32570 (RTX PRO 6000 96GB)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Multi-benchmark replication: same 4 models × BF16/FP16 × 6 prompts\n    × 6 seeds × 2 temperatures × 4 orderings on GSM8K (200 items), ARC-Challenge (200\n    items), HellaSwag (200 items). Tests whether item dominance and separability hold\n    across task types (math reasoning, science reasoning, commonsense).\n\n    '\n  priority: P0\n  gpu_budget_hours: 200\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-003\n  claim: 2\n  description: 'Multi-hardware G-study: 4 models × 2+ GPU types × 2 precisions (BF16,\n    FP16) × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 MMLU items. Tests\n    hardware × methodology interaction — the core separability question that MVP couldn''t\n    address with only 1 GPU type.\n\n    '\n  priority: P0\n  gpu_budget_hours: 120\n  hardware: westd-32570 + TBD (second GPU type from Manager)\n  deps: []\n  status: planned\n- id: exp-004\n  claim: 3\n  description: 'D-study projections from combined exp-001/002/003 data. Compute optimal\n    allocation across facets (items, prompts, seeds, orderings) for G≥0.90/0.95/0.99.\n    Generate practitioner-facing reproducibility budget tables.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  hardware: none\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  status: planned\n- id: exp-005\n  claim: 2\n  description: '14B model extension: Qwen3-14B and DeepSeek-R1-Distill-14B on datacenter\n    GPUs at BF16/FP16. Tests whether variance attribution patterns change with model\n    scale and architecture (dense vs reasoning-distilled).\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  hardware: TBD (needs ≥48GB VRAM per GPU)\n  deps:\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Fine-tuning G-study: RoBERTa-large on SST-2/MNLI/RTE/COPA. Fully crossed:\n    6 seeds × 3 learning rates × 4 data shuffles × 3 GPUs × 2 precisions = 432 runs/task\n    × 4 tasks = 1,728 total fine-tuning runs. Validates whether variance hierarchy\n    differs between inference and fine-tuning.\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  hardware: westd-32570 (RoBERTa-large fits easily on 96GB)\n  deps: []\n  status: planned\n- id: exp-007\n  claim: 2\n  description: 'Test LayerCast (FP16 storage + FP32 compute) as additional precision\n    condition on MMLU. Quantifies variance reduction from this mitigation strategy.\n\n    '\n  priority: P2\n  gpu_budget_hours: 30\n  hardware: westd-32570\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 1\n  description: 'MATH benchmark (200 items) — tests whether item dominance pattern\n    differs for reasoning-heavy tasks where chain-of-thought introduces additional\n    variance.\n\n    '\n  priority: P2\n  gpu_budget_hours: 50\n  hardware: westd-32570\n  deps:\n  - exp-002\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_phase_a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_records: 5400\n    conditions: 108\n    overall_accuracy: 0.6557\n    accuracy_bfloat16: 0.6844\n    accuracy_float16: 0.6833\n    accuracy_float32: 0.5994\n    g_coefficient: 0.357\n    top_variance_components:\n      item_id: 0.5844\n      residual: 0.1759\n      precision:item_id: 0.0724\n      temperature:item_id: 0.0685\n      prompt_template:item_id: 0.0573\n      seed:item_id: 0.027\n      precision: 0.0087\n    pass_criteria_a_pipeline: true\n    pass_criteria_b_components: true\n    pass_criteria_c_interaction: partial\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:05:59.422Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:05:59.422Z",
  "sessionId": "dc99552f-0d16-4424-a3ed-04aae8dce6f0"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T19:05:59.450Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：item dominance复现但幅度下降或跨benchmark不一致，separability大体成立但存在局部例外，需要softening claims并补充条件限定
核心假设：["float32 confound修复后item_id方差占比下降10-15个百分点（部分'item dominance'被precision×item interaction人为放大）", '第二块GPU延迟或只能做reduced crossing，hardware facet数据不完整', 'GSM8K等reasoning benchmark的方差结构与MMLU显著不同（residual/temperature占比更高，item dominance减弱）', '4个模型中1-2个模型表现异常（如Gemma的prompt sensitivity异常高），方差归因不完全一致']
关键指标范围：{'item_variance_share_mmlu': [0.32, 0.48], 'item_variance_share_other_benchmarks': [0.2, 0.4], 'direct_infra_method_interaction': [0.01, 0.05], 'item_conditional_interactions_total': [0.1, 0.25], 'precision_main_effect_after_fix': [0.003, 0.015], 'hardware_main_effect': [0.005, 0.03], 'g_current_practice': [0.35, 0.55], 'g_optimized_triple_items': [0.75, 0.9], 'cross_benchmark_replication_rate': [0.5, 0.75], 'models_showing_consistent_pattern': [2, 3]}
叙事方向：Claim 1从'more than all others combined'降级为'single largest source'，不再用58%作为headline，改用跨benchmark的range（如30-55%）。Claim 2的separability加条件限定：'at the aggregate level for multiple-choice benchmarks'，承认reasoning tasks中temperature和seed的interaction更大。Claim 3的D-study budget表仍成立但效果量缩小——tripling items从10×变为3-5×优于tripling prompts。如果第二块GPU未到，hardware facet降级为limitation而非contribution。论文重心从'surprising dominance'转向'benchmark-dependent variance structure'——不同任务类型需要不同的reproducibility budget，这本身是novel finding。仍可投AAAI但需要更强的writing来sell weaker numbers；准备ACL ARR作为backup。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: nlp_variance_gtheory
focus: Key questions: (1) Is the "item dominance" finding (58.4%) novel enough for AAAI, or will reviewers dismiss it as obvious? (2) Does the separability result (direct infra×method <0.5%) constitute a strong enough contribution, or is it a null result? (3) Is the D-study reproducibility budget framing compelling for the venue? (4) float32 engine confound — does it undermine credibility? (5) With only 1 GPU type in hand (second pending), is the hardware crossing claim defensible?

## paper_framing.md

# Paper Framing — nlp_variance_gtheory

## Target Venue
- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
- Extended: TACL (rolling)

## Title
Reproducibility Budgets for LLM Evaluation: Testing the Separability Assumption Between Infrastructure and Methodological Variance Sources via Generalizability Theory

## Core Claims (3 条，可证伪)

**Claim 1 — Item Dominance**: Item selection is the single largest uncontrolled variance source in LLM evaluation, contributing more than prompt phrasing, random seed, temperature, numerical precision, and hardware type combined. (MVP evidence: item_id = 58.4% of total variance vs all other factors combined < 25%)

**Claim 2 — Conditional Separability**: Infrastructure factors (hardware type, numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level (direct interaction < 0.5% of total variance), but both interact substantially with item difficulty — their effects are item-conditional, not universal. This provides an empirical license for isolated-factor studies while warning that their conclusions are conditional on item selection.

**Claim 3 — Reproducibility Budget**: G-theory D-study projections yield quantitative reproducibility budgets showing that increasing item sampling is orders of magnitude more cost-effective than increasing prompt/seed replication for achieving reliable model comparisons (G ≥ 0.90). Current common practices (1 prompt, 1 seed, ≤200 items) produce G < 0.40.

## Story Spine

**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability between infrastructure and methodology layers.

**Existing approaches & gaps**: Mesting (2026) applied G-theory to 5 methodological facets but treated infrastructure as fixed background. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision but without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance but on fixed hardware. No study crosses both layers in a unified G-theory framework, and critically, no study has quantified the role of item selection relative to all other sources.

**Our framing**: We conduct the first fully-crossed G-theory study spanning infrastructure (hardware type, numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors. The separability test has two equally publishable outcomes: if interactions are negligible, we grant an empirical license to isolated-factor studies; if substantial, we demonstrate that existing conclusions need hardware/prompt qualification. Our MVP reveals a third, unexpected finding: item selection dominates everything (58.4%), making it the overlooked key to evaluation reproducibility.

**Headline result template**: "In a fully-crossed G-study of K conditions across M models and N benchmarks, item selection accounts for >50% of total evaluation variance, while direct infrastructure × methodology interactions contribute <0.5%. Current evaluation practices achieve G < 0.40; our D-study reproducibility budgets show that tripling item count is 10× more effective than tripling prompt count for reaching G ≥ 0.90."

## Hook (Counter-Intuitive Quantified Claim)
"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs — item selection alone accounts for 58% of total evaluation variance, more than all other factors combined."

## Narrative Strategy
- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Breaking limitations (separability assumption challenge)
- **Tension**: "Everyone's optimizing the wrong thing" — the field focuses on prompt/seed/hardware standardization while ignoring item selection
- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
- **Signature visual**: Stacked-bar variance decomposition chart (field idiom from Mesting/Brittlebench)
- **Figure flow**: Problem illustration → G-theory facet diagram → Stacked-bar variance decomposition → D-study projection curves

## Venue Fit Risks
- AAAI: Strong fit for "evaluation methodology" track. Risk: tight 9-week timeline requires overlapping experiments with writing.
- Reviewer concern 1: "Only open-weight models, not API models" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.
- Reviewer concern 2: "G-theory is borrowed methodology, not novel" — Frame as cross-domain transfer contribution. The novelty is the facet structure crossing infrastructure × methodology, not G-theory itself.
- Reviewer concern 3: "Item dominance is obvious — harder items have more variance" — Counter: (a) the magnitude (58%) was not previously quantified; (b) item×factor interactions (7% precision×item) are non-obvious; (c) the D-study implications for evaluation design are novel.

## Anticipated Reviewer Concerns & Planned Responses
1. **"Only N GPU types"** → exp-003 (multi-hardware crossing) addresses this
2. **"float32 engine confound"** → exp-001 fixes with consistent vLLM engine settings (V0 enforce_eager for all)
3. **"Only MMLU"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag
4. **"Small item sample"** → exp-001 expands from 50 to 200 items
5. **"No training-time analysis"** → exp-006 (fine-tuning G-study with RoBERTa)
6. **"Missing scale validation"** → exp-005 (14B models)
7. **"G-theory may not be right framework"** → Compare with ANOVA and regression decomposition as sensitivity analysis

## Design Decisions
- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.
- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.
- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.
- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support. Documented as hardware compatibility requirement.


## experiment_plan (with registry status)

- id: exp-001
  claim: 1
  description: 'Full-scale precision study: 4 models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B-IT,
    Mistral-7B-v0.3) × 3 precisions (FP32, BF16, FP16) × 6 prompts × 6 seeds × 3 temperatures
    × 4 orderings × 200 MMLU items (stratified). All precisions use consistent vLLM
    engine (V0 enforce_eager) to eliminate the float32 engine confound found in MVP.
    Validates item dominance finding at scale and with multiple models.

    '
  priority: P0
  gpu_budget_hours: 100
  hardware: westd-32570 (RTX PRO 6000 96GB)
  deps: []
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
  description: 'D-study projections from combined exp-001/002/003 data. Compute optimal
    allocation across facets (items, prompts, seeds, orderings) for G≥0.90/0.95/0.99.
    Generate practitioner-facing reproducibility budget tables.

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
    g_coefficient: 0.357
    top_variance_components:
      item_id: 0.5844
      residual: 0.1759
      precision:item_id: 0.0724
      temperature:item_id: 0.0685
      prompt_template:item_id: 0.0573
      seed:item_id: 0.027
      precision: 0.0087
    pass_criteria_a_pipeline: true
    pass_criteria_b_components: true
    pass_criteria_c_interaction: partial

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
  "promptId": "0b3e45f6-81af-4bf4-aa42-1777b35e51fe",
  "type": "user",
  "uuid": "ffd858ac-a946-4a5b-839a-7a8137c14c60",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "dc99552f-0d16-4424-a3ed-04aae8dce6f0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:05:59.449Z_

```json
{
  "parentUuid": "ffd858ac-a946-4a5b-839a-7a8137c14c60",
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
  "uuid": "408b3741-faf6-4a09-915e-1298c248533f",
  "timestamp": "2026-05-20T19:05:59.449Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "dc99552f-0d16-4424-a3ed-04aae8dce6f0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:05:59.449Z_

```json
{
  "parentUuid": "408b3741-faf6-4a09-915e-1298c248533f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5519835c-d10b-4cd3-822e-79c11fa32d54",
  "timestamp": "2026-05-20T19:05:59.449Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "dc99552f-0d16-4424-a3ed-04aae8dce6f0",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：item dominance复现但幅度下降或跨benchmark不一致，separability大体成立但存在局部例外，需要softening claims并补充条件限定 核心假设：[\"float32 confound修复后item_id方差占比下降10-15个百分点（部分'item dominance'…",
  "leafUuid": "5519835c-d10b-4cd3-822e-79c11fa32d54",
  "sessionId": "dc99552f-0d16-4424-a3ed-04aae8dce6f0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "LLM evaluation variance decomposition and reproducibility budgets",
  "sessionId": "dc99552f-0d16-4424-a3ed-04aae8dce6f0"
}
```

---

### Assistant

_source line 8 · 2026-05-20T19:06:24.553Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment plan, assuming the "median" tier outcome. I need to provide specific expected metrics, rationales for why those results would occur under the median scenario, and descriptions of tables/figures/analysis for each experiment.

Let me carefully think through each experiment under the median tier assumptions:

**Median tier key assumptions:**
- float32 confound fix causes item_id variance share to drop 10-15 percentage points
- Second GPU delayed or only reduced crossing possible
- GSM8K/reasoning benchmarks have different variance structure (more residual/temperature, less item dominance)


- About 1-2 models show unexpected behavior patterns like Gemma's prompt sensitivity
- MMLU item variance should settle between 32-48%, while other benchmarks range from 20-40%
- Direct infrastructure-method interactions remain minimal at 1-5%, but conditional item interactions account for 10-25% of variance
- The precision improvement from the float32 fix shows modest gains of 0.3-1.5%, while hardware effects contribute 0.5-3%
- Generalization metrics show current practice achieving 35-55% while optimized triple-item approaches reach 75-90%
- Cross-benchmark replication rates hover around 50%

For the first experiment, I'm expecting the confound fix to substantially reduce item dominance from 58.4% down to around 42%, since some of that variance was artificially inflated by the precision-item interaction under the float32 confound. The precision main effect should drop to roughly 0.8%, the precision-item interaction should fall from 7.2% to about 3%, and the G coefficient might see slight improvement as the confound is removed.

For the second experiment across multiple benchmarks, I'm anticipating that item dominance will vary considerably—GSM8K should show weaker item effects around 25-35% since reasoning tasks are more sensitive to temperature and seed, while HellaSwag and ARC-Challenge will likely fall somewhere between 35-45%, though the pattern of item dominance being the single largest source won't hold uniformly across all benchmarks.

For the hardware study, if the second GPU data comes through, I'm expecting hardware effects to be minimal around 1-2% with small but detectable hardware-method interactions, though the incomplete crossing from the delayed GPU might limit what I can conclude.

The D-study projections show that tripling items could push generalizability from 0.45 to 0.82, though this is more modest than the original MVP estimate, and I'll need to flag the hardware limitations as a caveat in the final report.

The 14B model extension and fine-tuning studies should reveal different patterns—larger models might behave differently, and fine-tuning will likely show seed and learning rate dominating over hardware effects. LayerCast is lower priority but could offer modest improvements, while the MATH benchmark with chain-of-thought reasoning will probably show weaker item dominance due to increased variance from the reasoning process itself.

Now I'm ready to structure all of this into the YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5519835c-d10b-4cd3-822e-79c11fa32d54",
  "isSidechain": false,
  "requestId": "req_011CbELszKkKyD7vSTXeTMWj",
  "type": "assistant",
  "uuid": "03599311-40d3-4a27-b9c7-234ac4a03dfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "dc99552f-0d16-4424-a3ed-04aae8dce6f0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DngnAxHexpewcYNLGdEdeJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9480,
      "cache_read_input_tokens": 11841,
      "output_tokens": 7441,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 7441,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9480
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

_source line 9 · 2026-05-20T19:08:47.376Z_

```yaml
tier: median
narrative_guidance: "Claim 1从'more than all others combined'降级为'single largest source'，headline用跨benchmark range（30-55%）。Claim 2 separability加条件限定'at aggregate level for MC benchmarks'，承认reasoning tasks中temperature/seed interaction更大。Claim 3 D-study budget效果量缩小（tripling items从10×变为3-5×优于tripling prompts）。Hardware facet若数据不完整则降级为limitation。论文重心转向'benchmark-dependent variance structure'。"

imagined_experiments:
  - name: "Full-scale Precision Study (Confound Fixed)"
    plan_id: "exp-001"
    description: "4 models × 3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings × 200 MMLU items, all using V0 enforce_eager"
    expected_results:
      total_conditions: 1296_per_model
      total_records: 1036800
      item_id_variance_share: 0.43
      residual: 0.21
      precision_main_effect: 0.008
      precision_x_item: 0.032
      temperature_x_item: 0.058
      prompt_x_item: 0.062
      seed_x_item: 0.024
      ordering_main_effect: 0.004
      prompt_main_effect: 0.012
      temperature_main_effect: 0.015
      item_conditional_interactions_total: 0.176
      direct_infra_method_interaction: 0.003
      g_coefficient_current_practice: 0.42
      accuracy_bf16: 0.681
      accuracy_fp16: 0.679
      accuracy_fp32: 0.674
      model_agreement: "3 of 4 models show item_id as largest; Gemma-2 shows elevated prompt_x_item (~0.09) pulling item_id share to 0.36"
    result_rationale: "修复float32 confound后，MVP中precision=0.0087的main effect基本维持（因为BF16/FP16本身仍有差异），但precision×item从0.072骤降至0.032——MVP中float32使用了不同engine路径导致特定难题上的accuracy骤降，这部分interaction被消除。item_id纯方差从0.584降至0.43：原来的0.584中约有10-12pp是precision×item和temperature×item interaction在单一precision条件下被吸收进item主效应（50 items时估计不稳定）。200 items的stratified sampling提供更稳定估计，residual从0.176升至0.21反映了更大item pool中的unmodeled item×condition microvariance。Gemma-2-9B-IT因其instruction-tuning风格对prompt wording异常敏感（已知其system prompt格式要求严格），prompt×item interaction偏高，拉低了该模型的item_id相对份额。整体G=0.42仍然很低，验证了current practice不可靠的核心论点。"
    tables:
      - "Table 1: Variance component estimates (% of total) by model — 4×12 matrix showing each component per model plus pooled"
      - "Table 2: Accuracy means by precision level per model — confirms confound fix (三者差异<1pp vs MVP的8.5pp)"
      - "Table 3: Model-level G coefficients under current practice conditions"
    figures_description:
      - "Fig 1: Stacked bar chart of variance components, 4 models side-by-side + pooled, showing item_id consistently largest but varying 36-48%"
      - "Fig 2: Heatmap of item×precision interaction — showing which item difficulty bins still show precision sensitivity after fix"
    analysis: "Two-way ANOVA确认precision main effect在fix后从显著(p<0.001, η²=0.009)降为边际(p=0.03, η²=0.008)。Bootstrap CI for item_id share: [0.38, 0.48]。Gemma异常通过leave-one-model-out sensitivity analysis量化——移除Gemma后pooled item_id升至0.46。"

  - name: "Multi-Benchmark Replication"
    plan_id: "exp-002"
    description: "4 models × 2 precisions × 6 prompts × 6 seeds × 2 temps × 4 orderings on GSM8K/ARC-C/HellaSwag (200 items each)"
    expected_results:
      total_records_per_benchmark: 230400
      gsm8k_item_id_share: 0.28
      gsm8k_temperature_x_item: 0.12
      gsm8k_seed_x_item: 0.08
      gsm8k_residual: 0.27
      gsm8k_prompt_main: 0.03
      arc_challenge_item_id_share: 0.38
      arc_challenge_residual: 0.22
      arc_challenge_temperature_x_item: 0.07
      hellaswag_item_id_share: 0.45
      hellaswag_residual: 0.19
      hellaswag_prompt_x_item: 0.05
      cross_benchmark_item_dominance_as_largest: "3/4 benchmarks (GSM8K exception — residual+temp×item jointly exceed item_id)"
      cross_benchmark_separability_holds: "3/4 benchmarks (direct infra×method < 0.02 everywhere)"
      g_gsm8k_current: 0.35
      g_arc_current: 0.40
      g_hellaswag_current: 0.48
      replication_rate_item_as_single_largest: 0.625
    result_rationale: "GSM8K是reasoning task，CoT generation引入大量stochastic variance——temperature直接影响推理链的分支选择，且不同seed下同一难题可能走完全不同的推理路径，导致temperature×item和seed×item interaction显著放大（合计0.20 vs MMLU的0.08）。residual也更高（0.27）因为generation过程本质上比MC selection更noisy。item_id仍有0.28但不再是单一最大源——residual(0.27)+temperature×item(0.12)合并后超过它。ARC-Challenge是science MC，结构更接近MMLU但题目难度分布更极端（容易题ceiling effect），item_id=0.38。HellaSwag最接近MMLU pattern（都是MC、都是knowledge/commonsense），item_id=0.45。跨benchmark的核心发现：MC benchmarks中item dominance稳健成立，但reasoning/generation benchmarks中variance structure根本不同——这本身成为novel finding。Separability在所有benchmark都成立（direct interaction<0.02），因为hardware/precision effects是low-level numerical的，与task type无关。"
    tables:
      - "Table 4: Cross-benchmark variance decomposition comparison — 4 benchmarks × top-8 components matrix"
      - "Table 5: Benchmark characteristics (task type, answer format, difficulty distribution) vs variance structure mapping"
    figures_description:
      - "Fig 3: Grouped stacked bars — 4 benchmarks side-by-side showing how variance structure shifts from MC (item-dominated) to reasoning (residual/interaction-dominated)"
      - "Fig 4: Scatter plot of item difficulty vs item-level variance contribution across benchmarks — showing ceiling/floor effects"
    analysis: "Kruskal-Wallis test on per-item variance contributions across benchmarks confirms significant structural difference (H=47.3, p<0.001)。Permutation test for 'item_id is single largest component' yields replication probability 0.63 across random benchmark subsets。Key narrative shift: item dominance is benchmark-type-dependent, strongest for knowledge MC tasks, weaker for reasoning generation tasks。"

  - name: "Multi-Hardware G-Study"
    plan_id: "exp-003"
    description: "4 models × 2 GPU types × 2 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings × 200 MMLU items"
    expected_results:
      hardware_status: "second GPU arrived late — only 2 models × reduced seeds(3) completed on GPU-2"
      hardware_main_effect: 0.012
      hardware_x_precision: 0.006
      hardware_x_prompt: 0.002
      hardware_x_item: 0.018
      hardware_x_temperature: 0.003
      total_hardware_related_variance: 0.041
      direct_hardware_x_methodology_interaction: 0.005
      separability_conclusion: "holds at aggregate level — direct hardware×method < 1%"
      item_id_with_hardware_facet: 0.41
      g_with_hardware_generalization: 0.38
      completeness: "partial — 2/4 models fully crossed, 2/4 models only on primary GPU"
    result_rationale: "第二块GPU延迟到达，只能对Qwen3-8B和Llama-3.1-8B做完整crossing（reduced seeds=3以控制时间）。Hardware main effect=0.012来自GPU间的kernel implementation差异（不同SM架构的floating-point rounding path不同），但远小于item_id。hardware×item=0.018表明特定难题在不同GPU上表现不同——这是因为numerical edge cases（接近decision boundary的logits）在不同GPU architecture上round differently。Direct hardware×methodology interaction仅0.005，验证separability——但这个结论基于incomplete crossing需要谨慎表述。数据不完整意味着hardware facet的估计CI较宽，论文中需作为limitation明确说明，但核心separability finding的方向性仍可支持。"
    tables:
      - "Table 6: Hardware facet variance components (with CI) — noting which estimates are based on reduced crossing"
      - "Table 7: Separability test — direct interaction terms between hardware and each methodology facet"
    figures_description:
      - "Fig 5: Forest plot of hardware-related variance components with 95% bootstrap CIs — showing most CIs include zero except hardware×item"
    analysis: "Mixed-effects model with GPU as random effect confirms hardware contributes <2% unique variance。Acknowledge limitation: only 2 GPU types × partial model crossing — separability conclusion is directional, not definitive。Frame as 'consistent with separability' rather than 'proves separability'。计划在camera-ready前补充完整数据。"

  - name: "D-Study Projections"
    plan_id: "exp-004"
    description: "Compute optimal measurement allocation from combined exp-001/002/003 variance components"
    expected_results:
      g_current_practice_mmlu: 0.42
      g_current_practice_gsm8k: 0.35
      g_current_practice_pooled: 0.39
      g_triple_items_mmlu: 0.82
      g_triple_prompts_mmlu: 0.51
      g_triple_seeds_mmlu: 0.44
      g_optimal_600items_mmlu: 0.87
      g_optimal_600items_3prompts_mmlu: 0.91
      items_needed_for_g90_mmlu: 520
      items_needed_for_g90_gsm8k: 780
      items_needed_for_g90_hellaswag: 380
      cost_ratio_items_vs_prompts_for_g90: 3.8
      cost_ratio_items_vs_seeds_for_g90: 7.2
      budget_table_achievable_g90: "600 items × 3 prompts × 2 seeds — feasible but 3× current practice"
    result_rationale: "item_id占比从MVP的58%降至MMLU的43%、跨benchmark均值约35%，导致D-study中tripling items的marginal gain缩小——从MVP预测的G提升0.35降至约0.25。具体来看：G(current)=0.42因为200 items在43% item variance下仍然欠采样（需要~520 items才能让item sampling error降到可接受水平）。Triple items(600)→G=0.82而非MVP外推的0.90+，因为residual(0.21)设定了ceiling——即使无限items，residual variance仍限制G上界约0.93。Triple prompts仅从0.42→0.51因为prompt-related variance(main+interactions)合计才~0.08，三倍prompt只压缩这小部分。Cost ratio从MVP的'10×'降至3.8×：items仍是最cost-effective lever但优势缩小。GSM8K需要更多items(780)因为其residual更高且item variance share更低——每增加一个item压缩的variance比例更小。这个'benchmark-dependent budget'本身成为实用贡献。"
    tables:
      - "Table 8: D-study projection matrix — rows=facet allocation scenarios, columns=benchmarks, cells=projected G"
      - "Table 9: Practitioner budget table — 'to achieve G≥X on benchmark Y, sample at least Z items with W prompts'"
      - "Table 10: Cost-effectiveness ratios — marginal G gain per additional level of each facet"
    figures_description:
      - "Fig 6: D-study curves — G vs number of items, with separate lines per benchmark, horizontal reference at G=0.90"
      - "Fig 7: Allocation efficiency surface — 3D plot of items × prompts × projected G, showing diminishing returns"
    analysis: "Sensitivity analysis: bootstrap resample variance components 1000×, compute D-study projections for each → 95% CI on 'items needed for G≥0.90' is [420, 680] for MMLU。Key message shift: 'tripling items is 3-5× more effective than tripling prompts' (down from '10×' in MVP)。仍然是strong practical recommendation但headline数字需要honest reporting。"

  - name: "14B Model Extension"
    plan_id: "exp-005"
    description: "Qwen3-14B and DeepSeek-R1-Distill-14B at BF16/FP16 on MMLU 200 items"
    expected_results:
      qwen3_14b_item_id_share: 0.46
      deepseek_r1_14b_item_id_share: 0.34
      qwen3_14b_precision_main: 0.005
      deepseek_r1_precision_main: 0.009
      deepseek_r1_temperature_x_item: 0.11
      scale_effect_on_variance_structure: "mixed — dense 14B similar to 8B; reasoning-distilled shows more temperature sensitivity"
      g_qwen3_14b_current: 0.47
      g_deepseek_r1_14b_current: 0.38
    result_rationale: "Qwen3-14B作为dense model的scale-up版本，variance structure与8B系列相似但item_id略高(0.46)——更大模型对easy items更consistently correct，使item difficulty gradient更极端，增加item方差贡献。DeepSeek-R1-Distill-14B是reasoning-distilled模型，其CoT倾向使temperature sensitivity大幅升高（temperature×item=0.11），类似GSM8K的pattern——即使在MC task(MMLU)上，该模型也倾向于'思考'，引入generation-like variance。这导致其item_id share仅0.34。这个发现支持'variance structure depends on model architecture, not just task type'的扩展论点。Precision main effect在两个14B模型上都很小（dense model更稳定），验证separability在larger scale也成立。"
    tables:
      - "Table 11: 8B vs 14B variance component comparison — paired by architecture family"
    figures_description:
      - "Fig 8: Paired bar chart — 8B vs 14B models showing variance structure shift with scale"
    analysis: "Key finding: variance structure is jointly determined by task type AND model architecture (specifically, reasoning-distilled models behave like 'reasoning tasks' even on MC benchmarks)。This adds nuance to the benchmark-dependent story。"

  - name: "Fine-Tuning G-Study"
    plan_id: "exp-006"
    description: "RoBERTa-large on SST-2/MNLI/RTE/COPA: 6 seeds × 3 LR × 4 shuffles × 3 GPUs × 2 precisions = 432 runs/task"
    expected_results:
      total_runs: 1728
      sst2_seed_variance_share: 0.18
      sst2_lr_variance_share: 0.31
      sst2_item_id_variance_share: 0.22
      sst2_shuffle_variance_share: 0.04
      sst2_gpu_variance_share: 0.003
      sst2_precision_variance_share: 0.006
      sst2_residual: 0.15
      sst2_seed_x_item: 0.05
      rte_seed_variance_share: 0.28
      rte_lr_variance_share: 0.22
      rte_item_id_variance_share: 0.19
      rte_seed_x_lr: 0.08
      copa_instability: "high residual (0.32) due to small dataset size"
      g_finetuning_current_practice: 0.52
      g_finetuning_5seeds_3lr: 0.78
      infra_method_separability_finetuning: "holds — GPU×seed interaction < 0.5%"
    result_rationale: "Fine-tuning的variance hierarchy与inference根本不同：learning rate成为dominant factor(SST-2上0.31)因为它决定了optimization trajectory的convergence point——不同LR到达不同local minima。Seed是第二大因素(0.18-0.28)因为weight initialization和data ordering jointly决定optimization path。Item_id仍significant(0.19-0.22)但不再dominant——fine-tuning使模型适配了task distribution，减少了item difficulty的极端效应。RTE上seed更重要(0.28)因为小数据集(2.5k training)使optimization对initialization更敏感。GPU variance几乎为零(0.003)因为fine-tuning的随机性远大于hardware-level numerical差异。Data shuffle仅0.04——远低于预期，因为在足够epochs后shuffle的影响被averaged out。核心对比：inference中item dominates(43%)，fine-tuning中LR+seed dominates(~50%)——practitioners需要不同的reproducibility strategies for不同scenarios。"
    tables:
      - "Table 12: Fine-tuning variance decomposition — 4 tasks × top-8 components"
      - "Table 13: Inference vs fine-tuning variance hierarchy comparison"
      - "Table 14: Fine-tuning D-study — seeds and LR needed for G≥0.90"
    figures_description:
      - "Fig 9: Side-by-side stacked bars — inference (MMLU) vs fine-tuning (SST-2) variance decomposition showing inverted hierarchy"
      - "Fig 10: Fine-tuning D-study curves — G vs number of seeds, with LR as parameter"
    analysis: "The inverted hierarchy (item→LR+seed) between inference and fine-tuning is a clean novel finding。It explains why the 'run 5 seeds and report mean±std' convention exists for fine-tuning but not for inference evaluation。Separability still holds in fine-tuning (GPU×methodology < 0.5%)，strengthening the cross-scenario generalization of Claim 2。"

  - name: "LayerCast Precision Study"
    plan_id: "exp-007"
    description: "LayerCast (FP16 storage + FP32 compute) as 4th precision condition on MMLU"
    expected_results:
      layercast_accuracy: 0.680
      layercast_vs_fp32_accuracy_diff: 0.006
      layercast_vs_bf16_accuracy_diff: -0.001
      layercast_item_level_agreement_with_bf16: 0.94
      precision_variance_with_layercast: 0.005
      precision_x_item_with_layercast: 0.022
      variance_reduction_vs_mixed_precision: "15-20% reduction in precision-related variance components"
    result_rationale: "LayerCast在FP16存储但FP32计算，理论上获得FP32的numerical stability同时保持FP16的memory efficiency。实测accuracy接近BF16/FP16（差异<0.1pp）而非接近pure FP32——这是因为在confound-fixed设置下FP32本身的accuracy已与BF16接近（差异<1pp），LayerCast的'storage in FP16'引入的quantization noise在compute阶段被FP32 accumulation部分补偿。Precision×item interaction从0.032降至0.022——LayerCast减少了precision-sensitive items上的variance但未完全消除（weight quantization仍在）。整体precision-related variance减少约18%，是有意义但非revolutionary的改进。作为mitigation strategy，值得在discussion中推荐但不足以成为standalone contribution。"
    tables:
      - "Table 15: 4-level precision comparison (FP32/BF16/FP16/LayerCast) — accuracy and variance metrics"
    figures_description:
      - "Fig 11: Item-level accuracy correlation matrix across 4 precision conditions — showing LayerCast clusters with BF16/FP16"
    analysis: "LayerCast provides modest variance reduction but does not fundamentally change the story。Best framed as a practical recommendation in discussion: 'for practitioners concerned about precision effects, LayerCast offers ~18% reduction in precision-related variance at minimal memory cost'。"

  - name: "MATH Benchmark Extension"
    plan_id: "exp-008"
    description: "MATH 200 items — reasoning-heavy with CoT, testing item dominance in extended generation"
    expected_results:
      math_item_id_share: 0.22
      math_temperature_main: 0.04
      math_temperature_x_item: 0.15
      math_seed_x_item: 0.11
      math_residual: 0.30
      math_prompt_x_item: 0.06
      math_precision_main: 0.005
      math_g_current: 0.30
      math_items_for_g90: 950
      item_dominance_holds: false
      separability_holds: true
    result_rationale: "MATH是最极端的reasoning benchmark——每题需要多步推导，CoT generation在每一步都受temperature和seed影响。Temperature×item=0.15因为难题（Level 4-5）的solution path高度branching——temperature=0.7时可能走对路径，temperature=0.3时可能卡在suboptimal path。Seed×item=0.11同理——不同seed改变了sampling trajectory。Residual高达0.30反映了即使fixed所有facets，generation的intrinsic stochasticity（vLLM default设置下的CUDA nondeterminism在long generation中累积）。Item_id仅0.22——仍然是single largest individual component但margin很小（vs residual 0.30如果将residual视为'unexplained'则item不是最大）。这是median档下GSM8K pattern的加强版，确认了'reasoning tasks have fundamentally different variance structure'。Separability仍成立（precision/hardware与methodology无direct interaction>1%）——numerical precision不影响推理策略选择，只影响individual token probabilities。G=0.30极低，需要~950 items才能达到G≥0.90——对MATH这样仅500题的benchmark来说实质上不可达，这本身是对当前evaluation practice的strong critique。"
    tables:
      - "Table 16: MATH vs GSM8K vs MMLU variance structure comparison — progression from MC to light-reasoning to heavy-reasoning"
    figures_description:
      - "Fig 12: Variance structure gradient plot — x-axis = 'reasoning intensity' (MMLU→ARC→GSM8K→MATH), y-axis = component shares, showing smooth transition from item-dominated to residual/interaction-dominated"
    analysis: "MATH completes the picture: variance structure is a continuous function of task reasoning demands。For MC knowledge tasks, item selection is the key lever; for reasoning tasks, temperature control and massive item sampling are both needed。The 'one-size-fits-all' reproducibility budget is insufficient — practitioners need task-type-specific guidance。This benchmark-dependency finding becomes the paper's central novel contribution under the median tier narrative。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03599311-40d3-4a27-b9c7-234ac4a03dfc",
  "isSidechain": false,
  "requestId": "req_011CbELszKkKyD7vSTXeTMWj",
  "type": "assistant",
  "uuid": "6e0da9c4-585a-48a4-8178-381370541af9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519",
  "sessionId": "dc99552f-0d16-4424-a3ed-04aae8dce6f0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DngnAxHexpewcYNLGdEdeJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9480,
      "cache_read_input_tokens": 11841,
      "output_tokens": 7441,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 7441,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9480
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：item dominance复现但幅度下降或跨benchmark不一致，separability大体成立但存在局部例外，需要softening claims并补充条件限定 核心假设：[\"float32 confound修复后item_id方差占比下降10-15个百分点（部分'item dominance'…",
  "leafUuid": "6e0da9c4-585a-48a4-8178-381370541af9",
  "sessionId": "dc99552f-0d16-4424-a3ed-04aae8dce6f0"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "LLM evaluation variance decomposition and reproducibility budgets",
  "sessionId": "dc99552f-0d16-4424-a3ed-04aae8dce6f0"
}
```

---
