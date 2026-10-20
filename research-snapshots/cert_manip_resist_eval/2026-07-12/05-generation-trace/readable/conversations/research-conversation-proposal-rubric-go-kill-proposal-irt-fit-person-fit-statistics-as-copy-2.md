# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # IRT-FIT: Person-Fit Statistics as

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/995d5f7d-0337-4bc7-84dd-9975da23f404.jsonl`
- **Structured JSON:** [`db8c5cab7d7dd135934a.json`](../../sessions/db/db8c5cab7d7dd135934a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:35:26.437Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:35:26.437Z",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs\n\n## Description\nWe propose IRT-FIT, the first method that transfers person-fit statistics from educational psychometrics to detect LLM benchmark contamination in a fully black-box setting. The core insight is that a partially contaminated model, like a test-taker with item preknowledge, produces aberrant response patterns: it answers memorized hard items correctly while performance on non-memorized items reflects true ability, violating the monotonic difficulty gradient predicted by IRT. Using calibrated 4PL item parameters (discrimination, difficulty, guessing, and feasibility) from PSN-IRT (41,871 items, 11 benchmarks), we compute lz*, infit, outfit, and the multiscale lzm statistic for each model at two levels: per-benchmark (respecting unidimensionality via EFA-validated subscales) and aggregated (via the Hong-Lin-Cheng multiscale correction). We validate via controlled fine-tuning of three current open-source models — Llama 4 Scout 17B-16E (109B MoE), Qwen 3.5-9B (dense), and Gemma 4 31B (dense) — at seven contamination levels (0-100%) to empirically map the inverted-U detection power curve. We expect peak detection at 10-30% contamination, with explicit acknowledgment that 100% contamination is undetectable by person-fit (uniform high performance is consistent, not aberrant) and <3% contamination falls below statistical sensitivity. We benchmark against ConStat, PaCoST, CoDeC, Min-K%++, and Self-Critique, with a dedicated experiment testing the hypothesis (not assumption) that person-fit statistics maintain detection power on post-RL reasoning models where Wang et al. (2025) showed MIA-based methods fail. A 4PL-vs-3PL ablation quantifies how the feasibility parameter d affects sensitivity. We release an open-source toolkit with per-benchmark contamination flags and calibrated p-values inheriting Type-I error guarantees from decades of educational measurement theory.\n\n## Core Problem\nCan we detect benchmark contamination in LLMs without any access to training data or model internals, using only the pattern of correct/incorrect responses across benchmark items? Specifically, can psychometric person-fit statistics identify the 'sweet spot' of partial contamination (5-30% of items) where scores are meaningfully inflated but existing detectors fail?\n\n## Opportunity\nAll existing contamination detection methods require either training data access (n-gram overlap), model internals (Min-K% Probability, MIA, Self-Critique entropy sequences), or special probing prompts (Time Travel). Yet psychometrics has long used person-fit statistics like lz* to detect cheating examinees from response patterns alone — a contaminated LLM is functionally analogous to a test-taker with item preknowledge. This cross-domain transfer is newly feasible because IRT infrastructure for LLM evaluation has matured: PSN-IRT (AAAI 2026 Oral) calibrates 4PL item parameters (a, b, c, d) across 11 benchmarks and 41,871 items, providing the calibrated item bank needed to compute person-fit statistics at scale. The 4PL feasibility parameter d is particularly relevant — it accounts for item ambiguity that could otherwise be confused with contamination-induced aberrance, reducing false alarms. Meanwhile, Wang et al. (2025) demonstrate that all existing MIA-based detectors are fragile under reasoning-model contamination where RL post-training conceals SFT contamination signals, creating urgent demand for detection methods operating at a different level of abstraction.\n\n## Landscape\nContamination detection circa 2026 relies on five established families: (1) time-based partition, (2) Min-K%/Min-K%++ membership inference (ICLR 2024), (3) Time Travel probing (ICLR 2024 Spotlight), (4) ConStat performance-based testing (NeurIPS 2024), and (5) canary GUIDs. Newer approaches include CoDeC (ICLR 2026), which measures in-context learning effects on memorized vs. unseen data; Cross-Context Verification (arXiv 2603.21454), which uses session-isolated solution diversity; Self-Critique (arXiv 2510.09259, ICLR 2026), which detects post-RL contamination via policy collapse in entropy sequences with ~30% AUC improvement over baselines that perform near chance on RL-contaminated data; and Silicon Bureaucracy (arXiv 2603.21636), which audits score credibility through perturbation sensitivity analysis. Critically, Wang et al. (arXiv 2025) show all MIA-based methods fail under reasoning-model contamination where RL conceals SFT signals. On the IRT side, PSN-IRT (AAAI 2026 Oral) calibrates 4PL parameters (discrimination a, difficulty b, guessing c, feasibility d) across 11 benchmarks and 41,871 items but uses them for measurement quality, not contamination. ATLAS (arXiv 2025) uses IRT for adaptive testing efficiency. Han et al. (EACL 2026 Findings) quantify contamination in psychometric personality inventories but do not employ person-fit statistics. PaCoST (EMNLP 2024 Findings) uses paired confidence for contamination but is not IRT-based. In educational testing, lz* and outfit/infit statistics reliably flag cheating with known Type-I error control, with peak detection power at 10-30% item preknowledge (Sinharay, 2017; Karabatsos, 2003). No published or concurrent work connects IRT person-fit statistics to LLM benchmark contamination detection — an extensive search of arXiv 2025-2026, OpenReview, and GitHub confirms this gap remains open.\n\n## Approach\nWe compute four IRT person-fit statistics — lz, lz*, outfit, and infit — for each LLM using calibrated 4PL item parameters (a, b, c, d) from PSN-IRT's public release (41,871 items across 11 benchmarks). The analysis proceeds at two levels:\n\n**Level 1: Per-benchmark person-fit.** To respect the unidimensionality assumption, we compute person-fit statistics separately within each benchmark. Before fitting, we run an exploratory factor analysis (EFA) screen within each benchmark to validate approximate unidimensionality, following psychometric best practice (Crisan, Tendeiro & Meijer, 2017) and recent LLM evaluation precedent (arXiv:2509.24186). We focus on 6 benchmarks spanning diverse capabilities: MMLU (knowledge), GSM8K (math), HumanEval (coding), ARC-Challenge (science reasoning), HellaSwag (commonsense), and TruthfulQA (factuality).\n\n**Level 2: Aggregated contamination score.** We compute the multiscale lzm statistic (Hong, Lin & Cheng, 2021) — the standardized sum of per-benchmark lz* values — providing an overall contamination indicator that respects the multidimensional ability structure.\n\n**Controlled contamination experiment.** We establish ground truth by fine-tuning three open-source models (Llama 4 Scout 17B-16E, Qwen 3.5-9B, Gemma 4 31B) on varying fractions of benchmark items. We use seven contamination levels (0%, 5%, 10%, 15%, 25%, 50%, 100%) to map the detection power curve. Fine-tuning uses QLoRA to manage memory costs, particularly for the MoE-architecture Scout (109B total parameters, 17B active). For each contaminated variant, we compare person-fit signatures against clean baselines.\n\n**Power analysis and simulation.** We conduct a formal power analysis varying contamination fraction, number of contaminated items, and item difficulty distribution. Based on the educational testing literature, we expect an inverted-U detection power curve: undetectable below ~3% contamination (signal drowned in noise), peak detection at 10-30% (clear item-response aberrance), declining above 50% (inflated ability estimate absorbs contamination), and zero power at 100% (uniform high performance is consistent, not aberrant under IRT). We explicitly characterize this operating range and argue that 5-30% is the most policy-relevant detection window — where contamination meaningfully inflates scores but evades simple methods.\n\n**4PL ablation.** We compare person-fit statistics computed under the full 4PL model vs. a 3PL reduction (fixing d=1) to quantify how the feasibility parameter affects contamination detection sensitivity. The 4PL d parameter absorbs some item-level aberrance (Liao et al., 2012), which reduces false alarms from item ambiguity but may also reduce sensitivity to genuine contamination.\n\n**Post-RL hypothesis test.** As a key hypothesis (not a claimed advantage), we test whether person-fit statistics maintain detection power on post-RL reasoning models where Wang et al. (2025) showed existing MIA-based detectors fail. We create post-RL variants by applying GRPO fine-tuning after SFT-based contamination on Qwen 3.5-9B, specifically testing whether RL smooths out response-level aberrance or preserves it.\n\n**Baselines.** We evaluate detection performance (AUROC, Type-I error at fixed thresholds) against ConStat, PaCoST, CoDeC, Min-K%++, and Self-Critique across all contamination levels and training stages (SFT-only, SFT+RL).\n\n**Toolkit.** We release an open-source Python toolkit (built on py-irt and the R mirt package via rpy2, which natively supports 4PL person-fit computation) that takes any binary response matrix and calibrated 4PL item parameters and outputs per-model, per-benchmark contamination flags with calibrated p-values.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '300-400', 'timeline': '12 weeks', 'estimated_gpu_cost': '$750-1000 (H100 at ~$2.50/hr)'}, 'human_in_loop': {'gpu_hours': '280-350', 'timeline': '8-9 weeks', 'claude_api_cost': '$200-300', 'estimated_gpu_cost': '$700-875'}, 'auto_research': {'gpu_hours': '320-420', 'timeline': '5-6 weeks', 'claude_api_cost': '$400-600', 'estimated_gpu_cost': '$800-1050', 'speed_bottleneck': 'Sequential fine-tuning of contaminated model variants (3 base models × 7 contamination levels = 21 fine-tuning runs, plus 3 post-RL GRPO runs). Llama 4 Scout requires 4× H100 for QLoRA due to 109B total MoE parameters in memory; Gemma 4 31B needs 2× H100. Full-benchmark inference for 30+ models is parallelizable but each large model requires multi-GPU inference.'}, 'cost_breakdown': {'fine_tuning': 'Qwen 3.5-9B: ~15 GPU-hrs (7 levels × ~2 hrs); Gemma 4 31B: ~50 GPU-hrs (7 levels × ~7 hrs on 2× H100); Llama 4 Scout: ~70 GPU-hrs (7 levels × ~10 hrs on 4× H100). Post-RL GRPO variants: ~30 GPU-hrs. Total fine-tuning: ~165 GPU-hrs.', 'inference': '30+ models × 6 benchmarks × ~1-3 hrs/model depending on size: ~100-150 GPU-hrs.', 'simulation': 'Power analysis simulation (synthetic response matrices, 1000 replications × 7 contamination levels × 6 benchmarks): ~20 GPU-hrs on CPU/light GPU.', 'note': \"Costs increased ~50% vs. original estimate due to: (a) 7 contamination levels instead of 4, (b) Gemma 4 31B is 2.5× larger than originally assumed '12B', (c) explicit MoE memory overhead for Scout, (d) added simulation study and post-RL GRPO variants.\"}}\n\n## Inspired By\nField guide gap: 'MIA methods fail under single-epoch pre-training and post-RL concealment'; untried combination of IRT person-fit statistics (from psychometrics) with LLM contamination detection; the analogy between item preknowledge in educational cheating detection and benchmark memorization in LLM contamination; cross-domain transfer pattern from educational measurement to NLP evaluation; maturation of 4PL IRT infrastructure for LLMs (PSN-IRT) providing the calibrated item bank prerequisite.\n\n## Target Venues\n- AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026) — primary target: PSN-IRT was AAAI 2026 Oral, strong psychometrics+AI audience, 10 weeks from today is feasible with focused scope on 6 benchmarks\n- ICLR 2027 (abstract: ~Sep 19, 2026; full paper: ~Sep 24, 2026) — backup allowing fullest experimental scope including post-RL hypothesis test and expanded baseline comparisons\n\n## Key References\n- Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory (AAAI 2026 Oral, arXiv 2505.15055) — calibrates 4PL item parameters for 41,871 items across 11 benchmarks\n- Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks (arXiv 2511.04689) — ATLAS, IRT for adaptive testing efficiency\n- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024)\n- PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection (EMNLP 2024 Findings)\n- Detecting Pretraining Data from Large Language Models / Min-K% Probability (ICLR 2024)\n- Time Travel in LLMs: Tracing Data Contamination in Large Language Models (ICLR 2024 Spotlight)\n- On The Fragility of Benchmark Contamination Detection in Reasoning Models (arXiv 2510.02386) — Wang et al., shows MIA-based detectors fail under post-RL contamination\n- Detecting Data Contamination in LLMs via In-Context Learning / CoDeC (ICLR 2026)\n- Detecting Data Contamination from Reinforcement Learning Post-training / Self-Critique (arXiv 2510.09259, ICLR 2026) — post-RL contamination detection via entropy-sequence policy collapse\n- Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence (arXiv 2603.21636) — perturbation-based score credibility audit\n- Quantifying Data Contamination in Psychometric Evaluations of LLMs (EACL 2026 Findings) — Han et al.\n- Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis (arXiv 2603.21454)\n- Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types (Hong, Lin & Cheng, Psychometrika 2021) — lzm multiscale aggregation\n- Investigating the Practical Consequences of Model Misfit in Unidimensional IRT Models (Crisan, Tendeiro & Meijer, Applied Psychological Measurement 2017) — effects of unidimensionality violations on person-fit\n- The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses (Liao et al., 2012) — 4PL absorbs some aberrance via d parameter\n- Which Statistic Should Be Used to Detect Item Preknowledge? (Sinharay, JEBS 2017) — power analysis for preknowledge detection\n- Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics (Karabatsos, Applied Measurement in Education 2003)\n- PerFit: An R Package for Person-Fit Analysis in IRT (Journal of Statistical Software 2016)\n- py-irt: A Scalable Item Response Theory Library for Python (INFORMS Journal on Computing 2023)\n- mirt: A Multidimensional Item Response Theory Package for the R Environment (Journal of Statistical Software 2012) — supports 4PL person-fit natively\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:35:26.440Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:35:26.440Z",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-20T03:35:26.452Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs

## Description
We propose IRT-FIT, the first method that transfers person-fit statistics from educational psychometrics to detect LLM benchmark contamination in a fully black-box setting. The core insight is that a partially contaminated model, like a test-taker with item preknowledge, produces aberrant response patterns: it answers memorized hard items correctly while performance on non-memorized items reflects true ability, violating the monotonic difficulty gradient predicted by IRT. Using calibrated 4PL item parameters (discrimination, difficulty, guessing, and feasibility) from PSN-IRT (41,871 items, 11 benchmarks), we compute lz*, infit, outfit, and the multiscale lzm statistic for each model at two levels: per-benchmark (respecting unidimensionality via EFA-validated subscales) and aggregated (via the Hong-Lin-Cheng multiscale correction). We validate via controlled fine-tuning of three current open-source models — Llama 4 Scout 17B-16E (109B MoE), Qwen 3.5-9B (dense), and Gemma 4 31B (dense) — at seven contamination levels (0-100%) to empirically map the inverted-U detection power curve. We expect peak detection at 10-30% contamination, with explicit acknowledgment that 100% contamination is undetectable by person-fit (uniform high performance is consistent, not aberrant) and <3% contamination falls below statistical sensitivity. We benchmark against ConStat, PaCoST, CoDeC, Min-K%++, and Self-Critique, with a dedicated experiment testing the hypothesis (not assumption) that person-fit statistics maintain detection power on post-RL reasoning models where Wang et al. (2025) showed MIA-based methods fail. A 4PL-vs-3PL ablation quantifies how the feasibility parameter d affects sensitivity. We release an open-source toolkit with per-benchmark contamination flags and calibrated p-values inheriting Type-I error guarantees from decades of educational measurement theory.

## Core Problem
Can we detect benchmark contamination in LLMs without any access to training data or model internals, using only the pattern of correct/incorrect responses across benchmark items? Specifically, can psychometric person-fit statistics identify the 'sweet spot' of partial contamination (5-30% of items) where scores are meaningfully inflated but existing detectors fail?

## Opportunity
All existing contamination detection methods require either training data access (n-gram overlap), model internals (Min-K% Probability, MIA, Self-Critique entropy sequences), or special probing prompts (Time Travel). Yet psychometrics has long used person-fit statistics like lz* to detect cheating examinees from response patterns alone — a contaminated LLM is functionally analogous to a test-taker with item preknowledge. This cross-domain transfer is newly feasible because IRT infrastructure for LLM evaluation has matured: PSN-IRT (AAAI 2026 Oral) calibrates 4PL item parameters (a, b, c, d) across 11 benchmarks and 41,871 items, providing the calibrated item bank needed to compute person-fit statistics at scale. The 4PL feasibility parameter d is particularly relevant — it accounts for item ambiguity that could otherwise be confused with contamination-induced aberrance, reducing false alarms. Meanwhile, Wang et al. (2025) demonstrate that all existing MIA-based detectors are fragile under reasoning-model contamination where RL post-training conceals SFT contamination signals, creating urgent demand for detection methods operating at a different level of abstraction.

## Landscape
Contamination detection circa 2026 relies on five established families: (1) time-based partition, (2) Min-K%/Min-K%++ membership inference (ICLR 2024), (3) Time Travel probing (ICLR 2024 Spotlight), (4) ConStat performance-based testing (NeurIPS 2024), and (5) canary GUIDs. Newer approaches include CoDeC (ICLR 2026), which measures in-context learning effects on memorized vs. unseen data; Cross-Context Verification (arXiv 2603.21454), which uses session-isolated solution diversity; Self-Critique (arXiv 2510.09259, ICLR 2026), which detects post-RL contamination via policy collapse in entropy sequences with ~30% AUC improvement over baselines that perform near chance on RL-contaminated data; and Silicon Bureaucracy (arXiv 2603.21636), which audits score credibility through perturbation sensitivity analysis. Critically, Wang et al. (arXiv 2025) show all MIA-based methods fail under reasoning-model contamination where RL conceals SFT signals. On the IRT side, PSN-IRT (AAAI 2026 Oral) calibrates 4PL parameters (discrimination a, difficulty b, guessing c, feasibility d) across 11 benchmarks and 41,871 items but uses them for measurement quality, not contamination. ATLAS (arXiv 2025) uses IRT for adaptive testing efficiency. Han et al. (EACL 2026 Findings) quantify contamination in psychometric personality inventories but do not employ person-fit statistics. PaCoST (EMNLP 2024 Findings) uses paired confidence for contamination but is not IRT-based. In educational testing, lz* and outfit/infit statistics reliably flag cheating with known Type-I error control, with peak detection power at 10-30% item preknowledge (Sinharay, 2017; Karabatsos, 2003). No published or concurrent work connects IRT person-fit statistics to LLM benchmark contamination detection — an extensive search of arXiv 2025-2026, OpenReview, and GitHub confirms this gap remains open.

## Approach
We compute four IRT person-fit statistics — lz, lz*, outfit, and infit — for each LLM using calibrated 4PL item parameters (a, b, c, d) from PSN-IRT's public release (41,871 items across 11 benchmarks). The analysis proceeds at two levels:

**Level 1: Per-benchmark person-fit.** To respect the unidimensionality assumption, we compute person-fit statistics separately within each benchmark. Before fitting, we run an exploratory factor analysis (EFA) screen within each benchmark to validate approximate unidimensionality, following psychometric best practice (Crisan, Tendeiro & Meijer, 2017) and recent LLM evaluation precedent (arXiv:2509.24186). We focus on 6 benchmarks spanning diverse capabilities: MMLU (knowledge), GSM8K (math), HumanEval (coding), ARC-Challenge (science reasoning), HellaSwag (commonsense), and TruthfulQA (factuality).

**Level 2: Aggregated contamination score.** We compute the multiscale lzm statistic (Hong, Lin & Cheng, 2021) — the standardized sum of per-benchmark lz* values — providing an overall contamination indicator that respects the multidimensional ability structure.

**Controlled contamination experiment.** We establish ground truth by fine-tuning three open-source models (Llama 4 Scout 17B-16E, Qwen 3.5-9B, Gemma 4 31B) on varying fractions of benchmark items. We use seven contamination levels (0%, 5%, 10%, 15%, 25%, 50%, 100%) to map the detection power curve. Fine-tuning uses QLoRA to manage memory costs, particularly for the MoE-architecture Scout (109B total parameters, 17B active). For each contaminated variant, we compare person-fit signatures against clean baselines.

**Power analysis and simulation.** We conduct a formal power analysis varying contamination fraction, number of contaminated items, and item difficulty distribution. Based on the educational testing literature, we expect an inverted-U detection power curve: undetectable below ~3% contamination (signal drowned in noise), peak detection at 10-30% (clear item-response aberrance), declining above 50% (inflated ability estimate absorbs contamination), and zero power at 100% (uniform high performance is consistent, not aberrant under IRT). We explicitly characterize this operating range and argue that 5-30% is the most policy-relevant detection window — where contamination meaningfully inflates scores but evades simple methods.

**4PL ablation.** We compare person-fit statistics computed under the full 4PL model vs. a 3PL reduction (fixing d=1) to quantify how the feasibility parameter affects contamination detection sensitivity. The 4PL d parameter absorbs some item-level aberrance (Liao et al., 2012), which reduces false alarms from item ambiguity but may also reduce sensitivity to genuine contamination.

**Post-RL hypothesis test.** As a key hypothesis (not a claimed advantage), we test whether person-fit statistics maintain detection power on post-RL reasoning models where Wang et al. (2025) showed existing MIA-based detectors fail. We create post-RL variants by applying GRPO fine-tuning after SFT-based contamination on Qwen 3.5-9B, specifically testing whether RL smooths out response-level aberrance or preserves it.

**Baselines.** We evaluate detection performance (AUROC, Type-I error at fixed thresholds) against ConStat, PaCoST, CoDeC, Min-K%++, and Self-Critique across all contamination levels and training stages (SFT-only, SFT+RL).

**Toolkit.** We release an open-source Python toolkit (built on py-irt and the R mirt package via rpy2, which natively supports 4PL person-fit computation) that takes any binary response matrix and calibrated 4PL item parameters and outputs per-model, per-benchmark contamination flags with calibrated p-values.

## Resource Estimate
{'manual': {'gpu_hours': '300-400', 'timeline': '12 weeks', 'estimated_gpu_cost': '$750-1000 (H100 at ~$2.50/hr)'}, 'human_in_loop': {'gpu_hours': '280-350', 'timeline': '8-9 weeks', 'claude_api_cost': '$200-300', 'estimated_gpu_cost': '$700-875'}, 'auto_research': {'gpu_hours': '320-420', 'timeline': '5-6 weeks', 'claude_api_cost': '$400-600', 'estimated_gpu_cost': '$800-1050', 'speed_bottleneck': 'Sequential fine-tuning of contaminated model variants (3 base models × 7 contamination levels = 21 fine-tuning runs, plus 3 post-RL GRPO runs). Llama 4 Scout requires 4× H100 for QLoRA due to 109B total MoE parameters in memory; Gemma 4 31B needs 2× H100. Full-benchmark inference for 30+ models is parallelizable but each large model requires multi-GPU inference.'}, 'cost_breakdown': {'fine_tuning': 'Qwen 3.5-9B: ~15 GPU-hrs (7 levels × ~2 hrs); Gemma 4 31B: ~50 GPU-hrs (7 levels × ~7 hrs on 2× H100); Llama 4 Scout: ~70 GPU-hrs (7 levels × ~10 hrs on 4× H100). Post-RL GRPO variants: ~30 GPU-hrs. Total fine-tuning: ~165 GPU-hrs.', 'inference': '30+ models × 6 benchmarks × ~1-3 hrs/model depending on size: ~100-150 GPU-hrs.', 'simulation': 'Power analysis simulation (synthetic response matrices, 1000 replications × 7 contamination levels × 6 benchmarks): ~20 GPU-hrs on CPU/light GPU.', 'note': "Costs increased ~50% vs. original estimate due to: (a) 7 contamination levels instead of 4, (b) Gemma 4 31B is 2.5× larger than originally assumed '12B', (c) explicit MoE memory overhead for Scout, (d) added simulation study and post-RL GRPO variants."}}

## Inspired By
Field guide gap: 'MIA methods fail under single-epoch pre-training and post-RL concealment'; untried combination of IRT person-fit statistics (from psychometrics) with LLM contamination detection; the analogy between item preknowledge in educational cheating detection and benchmark memorization in LLM contamination; cross-domain transfer pattern from educational measurement to NLP evaluation; maturation of 4PL IRT infrastructure for LLMs (PSN-IRT) providing the calibrated item bank prerequisite.

## Target Venues
- AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026) — primary target: PSN-IRT was AAAI 2026 Oral, strong psychometrics+AI audience, 10 weeks from today is feasible with focused scope on 6 benchmarks
- ICLR 2027 (abstract: ~Sep 19, 2026; full paper: ~Sep 24, 2026) — backup allowing fullest experimental scope including post-RL hypothesis test and expanded baseline comparisons

## Key References
- Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory (AAAI 2026 Oral, arXiv 2505.15055) — calibrates 4PL item parameters for 41,871 items across 11 benchmarks
- Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks (arXiv 2511.04689) — ATLAS, IRT for adaptive testing efficiency
- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024)
- PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection (EMNLP 2024 Findings)
- Detecting Pretraining Data from Large Language Models / Min-K% Probability (ICLR 2024)
- Time Travel in LLMs: Tracing Data Contamination in Large Language Models (ICLR 2024 Spotlight)
- On The Fragility of Benchmark Contamination Detection in Reasoning Models (arXiv 2510.02386) — Wang et al., shows MIA-based detectors fail under post-RL contamination
- Detecting Data Contamination in LLMs via In-Context Learning / CoDeC (ICLR 2026)
- Detecting Data Contamination from Reinforcement Learning Post-training / Self-Critique (arXiv 2510.09259, ICLR 2026) — post-RL contamination detection via entropy-sequence policy collapse
- Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence (arXiv 2603.21636) — perturbation-based score credibility audit
- Quantifying Data Contamination in Psychometric Evaluations of LLMs (EACL 2026 Findings) — Han et al.
- Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis (arXiv 2603.21454)
- Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types (Hong, Lin & Cheng, Psychometrika 2021) — lzm multiscale aggregation
- Investigating the Practical Consequences of Model Misfit in Unidimensional IRT Models (Crisan, Tendeiro & Meijer, Applied Psychological Measurement 2017) — effects of unidimensionality violations on person-fit
- The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses (Liao et al., 2012) — 4PL absorbs some aberrance via d parameter
- Which Statistic Should Be Used to Detect Item Preknowledge? (Sinharay, JEBS 2017) — power analysis for preknowledge detection
- Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics (Karabatsos, Applied Measurement in Education 2003)
- PerFit: An R Package for Person-Fit Analysis in IRT (Journal of Statistical Software 2016)
- py-irt: A Scalable Item Response Theory Library for Python (INFORMS Journal on Computing 2023)
- mirt: A Multidimensional Item Response Theory Package for the R Environment (Journal of Statistical Software 2012) — supports 4PL person-fit natively


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "b0817405-f7ae-4abd-adf0-d018d44a69fa",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:35:26.451Z_

```json
{
  "parentUuid": "b0817405-f7ae-4abd-adf0-d018d44a69fa",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "57440709-27b1-437d-8aee-def461d4185a",
  "timestamp": "2026-05-20T03:35:26.451Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:35:26.451Z_

```json
{
  "parentUuid": "57440709-27b1-437d-8aee-def461d4185a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4af8e207-f4c7-47c9-a693-999a6103fac7",
  "timestamp": "2026-05-20T03:35:26.451Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs  ## Description We propos…",
  "leafUuid": "4af8e207-f4c7-47c9-a693-999a6103fac7",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT-based benchmark contamination detection for LLMs",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:35:31.313Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about using Item Response Theory (IRT) person-fit statistics from educational psychometrics to detect benchmark contamination in LLMs. Before I can give a proper assessment, I need to do thorough literature search to understand the current landscape.

Let me start by searching for the key related works and the novelty claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4af8e207-f4c7-47c9-a693-999a6103fac7",
  "isSidechain": false,
  "requestId": "req_011CbD7vJGHdRGLGxA874VdB",
  "type": "assistant",
  "uuid": "e3620d3a-a964-4780-a286-e878ed0376bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BFGrvJ8i1ibwG56NsNsKc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19477,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 193,
          "cache_read_input_tokens": 19477,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-20T03:35:32.312Z_

I'll start by conducting thorough literature research before making any assessment. Let me search for the key topics in this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3620d3a-a964-4780-a286-e878ed0376bf",
  "isSidechain": false,
  "requestId": "req_011CbD7vJGHdRGLGxA874VdB",
  "type": "assistant",
  "uuid": "d31e137c-e7a0-4d45-8242-1f916854cfdd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BFGrvJ8i1ibwG56NsNsKc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19477,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 193,
          "cache_read_input_tokens": 19477,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-20T03:35:32.751Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RkRtSFdpKNa3TnxZsjSMmW`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d31e137c-e7a0-4d45-8242-1f916854cfdd",
  "isSidechain": false,
  "requestId": "req_011CbD7vJGHdRGLGxA874VdB",
  "type": "assistant",
  "uuid": "2aca2ea0-9039-4540-8dcb-72e1c3a86267",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BFGrvJ8i1ibwG56NsNsKc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19477,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 193,
          "cache_read_input_tokens": 19477,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 11 · 2026-05-20T03:35:32.759Z_

<details><summary>↩ Tool result · `toolu_01RkRtSFdpKNa3TnxZsjSMmW`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2aca2ea0-9039-4540-8dcb-72e1c3a86267",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "5163f954-a13d-401e-af56-701084dc821a",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "2aca2ea0-9039-4540-8dcb-72e1c3a86267",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T03:35:35.420Z_

Now let me conduct the required literature searches. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5163f954-a13d-401e-af56-701084dc821a",
  "isSidechain": false,
  "requestId": "req_011CbD7vmNCdbdkYpwkyHStw",
  "type": "assistant",
  "uuid": "dc216792-8594-476e-9fea-7b52c491121e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KJ5GuPSWm38oUooC4kWdP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 19477,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 19477,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 720
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

_source line 13 · 2026-05-20T03:35:35.566Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019mQKGN8RW8fUpCdedBLyag`</summary>

```json
{
  "query": "IRT person-fit statistics LLM benchmark contamination detection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc216792-8594-476e-9fea-7b52c491121e",
  "isSidechain": false,
  "requestId": "req_011CbD7vmNCdbdkYpwkyHStw",
  "type": "assistant",
  "uuid": "5f041608-1bde-477c-a544-b5f16a61e339",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KJ5GuPSWm38oUooC4kWdP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 19477,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 19477,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 720
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

_source line 14 · 2026-05-20T03:35:43.145Z_

<details><summary>↩ Tool result · `toolu_019mQKGN8RW8fUpCdedBLyag`</summary>

```text
Web search results for query: "IRT person-fit statistics LLM benchmark contamination detection 2025 2026"

Links: [{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"Contamination Report for Multilingual Benchmarks","url":"https://arxiv.org/pdf/2410.16186"},{"title":"How Can I Publish My LLM Benchmark Without Giving the True Answers Away?","url":"https://arxiv.org/pdf/2505.18102"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark","url":"https://arxiv.org/pdf/2310.18018"},{"title":"Detecting Benchmark Contamination Through Watermarking","url":"https://arxiv.org/pdf/2502.17259"},{"title":"gies for llm benchmark data contamination - Gang Wang","url":"https://gangw.cs.illinois.edu/cvpr_Emperor25.pdf"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"}]

Based on the web search results, here's what I found regarding IRT person-fit statistics, LLM benchmark contamination detection in 2025-2026:

## Key Findings

**Recent Detection Methods (2025-2026):**
Five detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.

**Benchmark Contamination Definition:**
Benchmark contamination refers to the presence of test datasets in Large Language Model (LLM) pre-training or post-training data. Contamination can lead to inflated scores on benchmarks, compromising evaluation results and making it difficult to determine the capabilities of models.

**Novel Detection Approaches:**
A solution involves watermarking benchmarks before their release, with the embedding reformulating original questions with a watermarked LLM in a way that does not alter the benchmark utility. Additionally, CoDeC is a practical and accurate method to detect and quantify training data contamination in large language models.

**Challenges with Modern Models:**
Large Reasoning Models (LRMs) rely on chain-of-thought (CoT) reasoning to reach final answers, posing new challenges for contamination detection.

However, I did not find specific information about IRT (Item Response Theory) person-fit statistics being used as a contamination detection method in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f041608-1bde-477c-a544-b5f16a61e339",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "76191c9d-876f-43f0-9cc5-0f316e72750b",
  "toolUseResult": {
    "query": "IRT person-fit statistics LLM benchmark contamination detection 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LobAhHeJtqVuR7JqRdedgn",
        "content": [
          {
            "title": "What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide",
            "url": "https://llm-stats.com/blog/research/what-is-a-contaminated-llm"
          },
          {
            "title": "Contamination Report for Multilingual Benchmarks",
            "url": "https://arxiv.org/pdf/2410.16186"
          },
          {
            "title": "How Can I Publish My LLM Benchmark Without Giving the True Answers Away?",
            "url": "https://arxiv.org/pdf/2505.18102"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark",
            "url": "https://arxiv.org/pdf/2310.18018"
          },
          {
            "title": "Detecting Benchmark Contamination Through Watermarking",
            "url": "https://arxiv.org/pdf/2502.17259"
          },
          {
            "title": "gies for llm benchmark data contamination - Gang Wang",
            "url": "https://gangw.cs.illinois.edu/cvpr_Emperor25.pdf"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/html/2510.27055v1"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding IRT person-fit statistics, LLM benchmark contamination detection in 2025-2026:\n\n## Key Findings\n\n**Recent Detection Methods (2025-2026):**\nFive detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.\n\n**Benchmark Contamination Definition:**\nBenchmark contamination refers to the presence of test datasets in Large Language Model (LLM) pre-training or post-training data. Contamination can lead to inflated scores on benchmarks, compromising evaluation results and making it difficult to determine the capabilities of models.\n\n**Novel Detection Approaches:**\nA solution involves watermarking benchmarks before their release, with the embedding reformulating original questions with a watermarked LLM in a way that does not alter the benchmark utility. Additionally, CoDeC is a practical and accurate method to detect and quantify training data contamination in large language models.\n\n**Challenges with Modern Models:**\nLarge Reasoning Models (LRMs) rely on chain-of-thought (CoT) reasoning to reach final answers, posing new challenges for contamination detection.\n\nHowever, I did not find specific information about IRT (Item Response Theory) person-fit statistics being used as a contamination detection method in the search results."
    ],
    "durationSeconds": 7.572990291,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5f041608-1bde-477c-a544-b5f16a61e339",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T03:35:46.045Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kjt8BWzpfcvwHHPCse5mG3`</summary>

```json
{
  "query": "PSN-IRT \"Lost in Benchmarks\" AAAI 2026 4PL item response theory LLM evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76191c9d-876f-43f0-9cc5-0f316e72750b",
  "isSidechain": false,
  "requestId": "req_011CbD7wXb12k56m7xAHNS3t",
  "type": "assistant",
  "uuid": "75d2f766-0bec-41d3-861e-7e86fb12eaf6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019sJpmvGz7ugAqjdtDPspC4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 806,
      "cache_read_input_tokens": 20197,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 806,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 20197,
          "cache_creation_input_tokens": 806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 806
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

_source line 16 · 2026-05-20T03:35:52.215Z_

<details><summary>↩ Tool result · `toolu_01Kjt8BWzpfcvwHHPCse5mG3`</summary>

```text
Web search results for query: "PSN-IRT "Lost in Benchmarks" AAAI 2026 4PL item response theory LLM evaluation"

Links: [{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://chatpaper.com/paper/139423"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"},{"title":"Paper page - Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://huggingface.co/papers/2505.15055"},{"title":"[PDF] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Lost-in-Benchmarks-Rethinking-Large-Language-Model-Zhou-Huang/a43a21d3b8bcede381110da630421afca45c8e5d"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"}]

Based on the search results, here's what I found about this research:

## Overview

"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" proposes Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture.

## Research Focus

The paper addresses the fact that the evaluation of LLMs via benchmarks is widespread, yet inconsistencies between different leaderboards and poor separability among top models raise concerns about their ability to accurately reflect authentic model capabilities.

## Methodology

The core methodology involves two independent neural network pathways: a Model Network and an Item Network, with the Model Network taking a one-hot encoding of an LLM identifier as input and estimating a latent scalar representing the model's ability. The framework estimates item parameters including discriminability (a), difficulty (b), guessing-rate (c), and feasibility (d) parameters from the 4PL model.

## Scale of Analysis

The research conducts extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.

## Key Findings

LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, limiting their ability to challenge and accurately evaluate advanced models, and exhibit data contamination in numerous items, compromising their reliability.

The paper was accepted as an oral presentation at AAAI 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75d2f766-0bec-41d3-861e-7e86fb12eaf6",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "c321f2ab-be8f-4831-8bb6-1b8d7001ca65",
  "toolUseResult": {
    "query": "PSN-IRT \"Lost in Benchmarks\" AAAI 2026 4PL item response theory LLM evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_017zoeiPpQduWfUwkXgTRkdn",
        "content": [
          {
            "title": "GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub",
            "url": "https://github.com/Joe-Hall-Lee/PSN-IRT"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://chatpaper.com/paper/139423"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v2"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40814"
          },
          {
            "title": "[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/pdf/2505.15055"
          },
          {
            "title": "(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"
          },
          {
            "title": "Paper page - Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://huggingface.co/papers/2505.15055"
          },
          {
            "title": "[PDF] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Lost-in-Benchmarks-Rethinking-Large-Language-Model-Zhou-Huang/a43a21d3b8bcede381110da630421afca45c8e5d"
          },
          {
            "title": "[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/abs/2505.15055"
          }
        ]
      },
      "Based on the search results, here's what I found about this research:\n\n## Overview\n\n\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\" proposes Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture.\n\n## Research Focus\n\nThe paper addresses the fact that the evaluation of LLMs via benchmarks is widespread, yet inconsistencies between different leaderboards and poor separability among top models raise concerns about their ability to accurately reflect authentic model capabilities.\n\n## Methodology\n\nThe core methodology involves two independent neural network pathways: a Model Network and an Item Network, with the Model Network taking a one-hot encoding of an LLM identifier as input and estimating a latent scalar representing the model's ability. The framework estimates item parameters including discriminability (a), difficulty (b), guessing-rate (c), and feasibility (d) parameters from the 4PL model.\n\n## Scale of Analysis\n\nThe research conducts extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.\n\n## Key Findings\n\nLLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, limiting their ability to challenge and accurately evaluate advanced models, and exhibit data contamination in numerous items, compromising their reliability.\n\nThe paper was accepted as an oral presentation at AAAI 2026."
    ],
    "durationSeconds": 6.165355295000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "75d2f766-0bec-41d3-861e-7e86fb12eaf6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T03:36:06.889Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LqwCL8bv5Wm1U4qrUGGEgo`</summary>

```json
{
  "query": "Wang et al 2025 \"fragility benchmark contamination detection reasoning models\" MIA fail post-RL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c321f2ab-be8f-4831-8bb6-1b8d7001ca65",
  "isSidechain": false,
  "requestId": "req_011CbD7xCjDA51daZCuKEE9Y",
  "type": "assistant",
  "uuid": "842cd595-4097-4d91-8349-0019011534ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyxwKkpTkcGcTjfiwZA2u3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1104,
      "cache_read_input_tokens": 21003,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1104,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 21003,
          "cache_creation_input_tokens": 1104,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1104
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

_source line 18 · 2026-05-20T03:36:15.220Z_

<details><summary>↩ Tool result · `toolu_01LqwCL8bv5Wm1U4qrUGGEgo`</summary>

```text
Web search results for query: "Wang et al 2025 "fragility benchmark contamination detection reasoning models" MIA fail post-RL"

Links: [{"title":"[PDF] On The Fragility of Benchmark Contamination Detection in Reasoning Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-The-Fragility-of-Benchmark-Contamination-in-Wang-Li/9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3"},{"title":"[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/abs/2510.02386"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/html/2510.02386v1"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/pdf/2510.09259"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/html/2510.09259v1"}]

I found the paper you're looking for! Here are the key findings:

## Paper Overview

Wang et al. (2025) authored "On The Fragility of Benchmark Contamination Detection in Reasoning Models", which examines critical vulnerabilities in detecting benchmark contamination in Large Reasoning Models (LRMs).

## Key Findings

The work reveals that RL fine-tuning can conceal benchmark contamination when base models evolve into LRMs, and contamination with Chain-of-Thought (CoT) applied to advanced LRMs leaves little evidence detectable by existing memorization-based methods.

More specifically:

- When the base model evolves into LRM via Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), contamination during SFT can be originally identified by contamination detection methods, but even brief GRPO training can markedly conceal contamination signals that most detection methods rely on.

- In the post-LRM stage, extensive contamination with CoT on advanced LRMs barely leaves evidence for existing memorization-based detection methods.

The paper was published on arXiv on September 30, 2025 (arXiv:2510.02386).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "842cd595-4097-4d91-8349-0019011534ff",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "552e45a3-6379-4786-affe-7bf49f4d9db9",
  "toolUseResult": {
    "query": "Wang et al 2025 \"fragility benchmark contamination detection reasoning models\" MIA fail post-RL",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Uky17MrZELgt21BNx5K3dD",
        "content": [
          {
            "title": "[PDF] On The Fragility of Benchmark Contamination Detection in Reasoning Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/On-The-Fragility-of-Benchmark-Contamination-in-Wang-Li/9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3"
          },
          {
            "title": "[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/abs/2510.02386"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/html/2510.02386v1"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"
          },
          {
            "title": "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/pdf/2510.09259"
          },
          {
            "title": "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/html/2510.09259v1"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key findings:\n\n## Paper Overview\n\nWang et al. (2025) authored \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\", which examines critical vulnerabilities in detecting benchmark contamination in Large Reasoning Models (LRMs).\n\n## Key Findings\n\nThe work reveals that RL fine-tuning can conceal benchmark contamination when base models evolve into LRMs, and contamination with Chain-of-Thought (CoT) applied to advanced LRMs leaves little evidence detectable by existing memorization-based methods.\n\nMore specifically:\n\n- When the base model evolves into LRM via Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), contamination during SFT can be originally identified by contamination detection methods, but even brief GRPO training can markedly conceal contamination signals that most detection methods rely on.\n\n- In the post-LRM stage, extensive contamination with CoT on advanced LRMs barely leaves evidence for existing memorization-based detection methods.\n\nThe paper was published on arXiv on September 30, 2025 (arXiv:2510.02386)."
    ],
    "durationSeconds": 8.326779427000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "842cd595-4097-4d91-8349-0019011534ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T03:36:17.174Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GFepC8vwMRcGtSZrwcwRQc`</summary>

```json
{
  "query": "Self-Critique \"detecting data contamination reinforcement learning post-training\" ICLR 2026 entropy policy collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "552e45a3-6379-4786-affe-7bf49f4d9db9",
  "isSidechain": false,
  "requestId": "req_011CbD7ytgp1VLztramiQ6eY",
  "type": "assistant",
  "uuid": "f770bd28-3dd5-4d2a-84b4-063b54f711a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GHZP6SeZZ7ekZziPMGmcfN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 774,
      "cache_read_input_tokens": 22107,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 774,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 22107,
          "cache_creation_input_tokens": 774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 774
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

_source line 20 · 2026-05-20T03:36:23.794Z_

<details><summary>↩ Tool result · `toolu_01GFepC8vwMRcGtSZrwcwRQc`</summary>

```text
Web search results for query: "Self-Critique "detecting data contamination reinforcement learning post-training" ICLR 2026 entropy policy collapse"

Links: [{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/html/2510.09259v1"},{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"},{"title":"detecting data contamination from reinforcement learning ...","url":"https://arxiv.org/pdf/2510.09259"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2505.19590"},{"title":"The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models | OpenReview","url":"https://openreview.net/forum?id=vXoksdcfqC"},{"title":"ICLR Poster Entropy-preserving reinforcement learning","url":"https://iclr.cc/virtual/2026/poster/10010707"},{"title":"Published as a conference paper at ICLR 2026 EXPLORATION VS EXPLOITATION:","url":"https://arxiv.org/pdf/2512.16912"},{"title":"The Impact of Post-training on Data Contamination","url":"https://arxiv.org/pdf/2601.06103"}]

Based on the search results, I found relevant information about this research:

The paper presents the first systematic study of data contamination in the overlooked RL post-training stage, proposing Self-Critique, a novel method that identifies RL-induced policy collapse by actively probing the model's reasoning path dependencies using token-level entropy.

The method is motivated by a key observation that after the RL phase, the output entropy distribution of LLMs tends to collapse into highly specific and sparse modes, and Self-Critique probes for the underlying policy collapse—the model's convergence to a narrow reasoning path, which causes this entropy reduction.

Experiments show that Self-Critique consistently outperforms baselines, improving the average AUC by up to 30%, and its ability to isolate RL-specific signals is further highlighted in dual-contamination scenarios, where performance improves by up to 55%.

The research paper appears to be available on arXiv (paper ID: 2510.09259) and addresses a critical gap in detecting data contamination specifically within the reinforcement learning post-training phase of large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f770bd28-3dd5-4d2a-84b4-063b54f711a2",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "4779c714-b973-453b-abeb-3e572beb41e1",
  "toolUseResult": {
    "query": "Self-Critique \"detecting data contamination reinforcement learning post-training\" ICLR 2026 entropy policy collapse",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VTYegtcETHJ8XRJ6GoNW84",
        "content": [
          {
            "title": "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/html/2510.09259v1"
          },
          {
            "title": "[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/abs/2510.09259"
          },
          {
            "title": "detecting data contamination from reinforcement learning ...",
            "url": "https://arxiv.org/pdf/2510.09259"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2505.19590"
          },
          {
            "title": "The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=vXoksdcfqC"
          },
          {
            "title": "ICLR Poster Entropy-preserving reinforcement learning",
            "url": "https://iclr.cc/virtual/2026/poster/10010707"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 EXPLORATION VS EXPLOITATION:",
            "url": "https://arxiv.org/pdf/2512.16912"
          },
          {
            "title": "The Impact of Post-training on Data Contamination",
            "url": "https://arxiv.org/pdf/2601.06103"
          }
        ]
      },
      "Based on the search results, I found relevant information about this research:\n\nThe paper presents the first systematic study of data contamination in the overlooked RL post-training stage, proposing Self-Critique, a novel method that identifies RL-induced policy collapse by actively probing the model's reasoning path dependencies using token-level entropy.\n\nThe method is motivated by a key observation that after the RL phase, the output entropy distribution of LLMs tends to collapse into highly specific and sparse modes, and Self-Critique probes for the underlying policy collapse—the model's convergence to a narrow reasoning path, which causes this entropy reduction.\n\nExperiments show that Self-Critique consistently outperforms baselines, improving the average AUC by up to 30%, and its ability to isolate RL-specific signals is further highlighted in dual-contamination scenarios, where performance improves by up to 55%.\n\nThe research paper appears to be available on arXiv (paper ID: 2510.09259) and addresses a critical gap in detecting data contamination specifically within the reinforcement learning post-training phase of large language models."
    ],
    "durationSeconds": 6.616885416000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f770bd28-3dd5-4d2a-84b4-063b54f711a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs  ## Description We propos…",
  "leafUuid": "4779c714-b973-453b-abeb-3e572beb41e1",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT-based benchmark contamination detection for LLMs",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404"
}
```

---

### Tool call

_source line 23 · 2026-05-20T03:36:26.150Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CohACUMkmE73FbB4hRLXLh`</summary>

```json
{
  "query": "CoDeC \"detecting data contamination in-context learning\" ICLR 2026 LLM benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4779c714-b973-453b-abeb-3e572beb41e1",
  "isSidechain": false,
  "requestId": "req_011CbD7zXMCg8Pfp22Y7Kash",
  "type": "assistant",
  "uuid": "33661224-8bf2-4c94-891d-07bf355575fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkwqbAytyWjrJD6a3Zj8Rb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 22881,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 22881,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 24 · 2026-05-20T03:36:31.335Z_

<details><summary>↩ Tool result · `toolu_01CohACUMkmE73FbB4hRLXLh`</summary>

```text
Web search results for query: "CoDeC "detecting data contamination in-context learning" ICLR 2026 LLM benchmark"

Links: [{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://openreview.net/pdf/fbfd3e4f09f698fff38f0024c147e2e942876160.pdf"},{"title":"Detecting Data Contamination in LLMs via In-Context ...","url":"https://openreview.net/pdf/ff30b4c6160ac241bb4827febefd6353e52dbd32.pdf"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/pdf/2510.27055"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning - AI Research Papers Daily","url":"https://ai-blogs.co.in/paper/2510.27055v1"},{"title":"[2510.27055] Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/abs/2510.27055"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning | OpenReview","url":"https://openreview.net/forum?id=YlpaaYxx4t"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning Michał Zawalski†","url":"https://openreview.net/pdf/753f569951799d9078f4db2d0e9debd74ad5b692.pdf"}]

I found the research paper you're looking for! Here's what I found:

CoDeC is a paper under review at ICLR 2026 titled "Detecting Data Contamination in LLMs via In-Context Learning."

**Key Details:**

The paper presents Contamination Detection via Context (CoDeC), a method to detect and quantify training data contamination in large language models that distinguishes between data memorized during training and data outside the training distribution by measuring how in-context learning affects model performance.

**How CoDeC Works:**

In-context examples typically boost confidence for unseen datasets but may reduce it when the dataset was part of training, due to disrupted memorization patterns. The percentage of samples in a dataset for which added context reduces confidence quantifies contamination.

**Key Advantages:**

- CoDeC is computationally efficient, needing just two forward passes per sample.
- It requires only gray-box access to token probabilities, works with any dataset, and needs no prior knowledge of the model's training corpus.
- The method is simple, automated, and both model- and dataset-agnostic, making it easy to integrate with benchmark evaluations.

**Results:**

Experiments show that CoDeC produces interpretable contamination scores that clearly separate seen and unseen datasets, and reveals strong evidence of memorization in open-weight models with undisclosed training corpora.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33661224-8bf2-4c94-891d-07bf355575fc",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "bcaa153f-5886-491a-99d4-e66bb6dac811",
  "toolUseResult": {
    "query": "CoDeC \"detecting data contamination in-context learning\" ICLR 2026 LLM benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NyHSwLWdaPDPBHfgiNKxSF",
        "content": [
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://openreview.net/pdf/fbfd3e4f09f698fff38f0024c147e2e942876160.pdf"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context ...",
            "url": "https://openreview.net/pdf/ff30b4c6160ac241bb4827febefd6353e52dbd32.pdf"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/pdf/2510.27055"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/html/2510.27055v1"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning - AI Research Papers Daily",
            "url": "https://ai-blogs.co.in/paper/2510.27055v1"
          },
          {
            "title": "[2510.27055] Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/abs/2510.27055"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning | OpenReview",
            "url": "https://openreview.net/forum?id=YlpaaYxx4t"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning Michał Zawalski†",
            "url": "https://openreview.net/pdf/753f569951799d9078f4db2d0e9debd74ad5b692.pdf"
          }
        ]
      },
      "I found the research paper you're looking for! Here's what I found:\n\nCoDeC is a paper under review at ICLR 2026 titled \"Detecting Data Contamination in LLMs via In-Context Learning.\"\n\n**Key Details:**\n\nThe paper presents Contamination Detection via Context (CoDeC), a method to detect and quantify training data contamination in large language models that distinguishes between data memorized during training and data outside the training distribution by measuring how in-context learning affects model performance.\n\n**How CoDeC Works:**\n\nIn-context examples typically boost confidence for unseen datasets but may reduce it when the dataset was part of training, due to disrupted memorization patterns. The percentage of samples in a dataset for which added context reduces confidence quantifies contamination.\n\n**Key Advantages:**\n\n- CoDeC is computationally efficient, needing just two forward passes per sample.\n- It requires only gray-box access to token probabilities, works with any dataset, and needs no prior knowledge of the model's training corpus.\n- The method is simple, automated, and both model- and dataset-agnostic, making it easy to integrate with benchmark evaluations.\n\n**Results:**\n\nExperiments show that CoDeC produces interpretable contamination scores that clearly separate seen and unseen datasets, and reveals strong evidence of memorization in open-weight models with undisclosed training corpora."
    ],
    "durationSeconds": 5.181023996999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "33661224-8bf2-4c94-891d-07bf355575fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T03:36:33.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013F4iwyiaP72jWe5BHo6zLG`</summary>

```json
{
  "query": "IRT item response theory LLM evaluation contamination cheating detection person fit 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcaa153f-5886-491a-99d4-e66bb6dac811",
  "isSidechain": false,
  "requestId": "req_011CbD815sYN6DsntYeL5GEd",
  "type": "assistant",
  "uuid": "514b4c6f-632c-4e35-a7cb-f56349aea2ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012WcuZhppnr8tGfWoEZzYpZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 839,
      "cache_read_input_tokens": 23584,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 23584,
          "cache_creation_input_tokens": 839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 839
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

_source line 26 · 2026-05-20T03:36:41.343Z_

<details><summary>↩ Tool result · `toolu_013F4iwyiaP72jWe5BHo6zLG`</summary>

```text
Web search results for query: "IRT item response theory LLM evaluation contamination cheating detection person fit 2025 2026 arXiv"

Links: [{"title":"Applying Item Response Theory to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments","url":"https://arxiv.org/html/2412.02713v1"},{"title":"Leveraging LLM-Respondents for Item Evaluation: a Psychometric Analysis","url":"https://arxiv.org/html/2407.10899v1"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"[2602.00521] Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/abs/2602.00521"},{"title":"A Short Note on Aberrant Responses Bias in Item Response Theory","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6365413/"},{"title":"JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory","url":"https://arxiv.org/pdf/2509.22888"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"},{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"}]

Based on the web search results, I found several highly relevant papers from arXiv that address the intersection of Item Response Theory (IRT), LLM evaluation, contamination, and cheating detection:

## Key Papers Found:

**1. Distinguishing Human from AI Responses (2025)**
A paper accepted to the 15th International Learning Analytics & Knowledge Conference focuses on using cheating with AI, separating AI from humans, and item-response theory person-fit statistics. IRT is described as a psychometric framework used to model the relationship between individuals' responses to assessment items and their underlying traits or abilities.

**2. Data Contamination in LLM Benchmarking (2025)**
The PSN-IRT framework combines psychometrics with neural networks to analyze LLM benchmarks, demonstrating that current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination.

**3. Quantifying Data Contamination in Psychometric Evaluations (2025)**
LLMs may have encountered psychometric items during pretraining, creating a risk of data contamination where test results may reflect prior exposure rather than genuine characteristics.

**4. LLM-as-a-Judge Reliability Assessment (2026)**
A framework grounded in Item Response Theory assesses the reliability of LLM judges using the Graded Response Model, examining intrinsic consistency and human alignment.

**5. Adaptive Testing for LLM Evaluation (2026)**
Static benchmarks are vulnerable to data contamination, and computerized adaptive testing (CAT) frameworks grounded in IRT offer an alternative for efficient assessment of LLMs.

These papers collectively address your search terms, focusing on using IRT for detecting anomalous response patterns, evaluating LLMs reliably, and identifying data contamination issues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "514b4c6f-632c-4e35-a7cb-f56349aea2ef",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "8a653546-6618-4bf7-929f-df034c089d12",
  "toolUseResult": {
    "query": "IRT item response theory LLM evaluation contamination cheating detection person fit 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D6HMYRLdqT2zChnHiEThHJ",
        "content": [
          {
            "title": "Applying Item Response Theory to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments",
            "url": "https://arxiv.org/html/2412.02713v1"
          },
          {
            "title": "Leveraging LLM-Respondents for Item Evaluation: a Psychometric Analysis",
            "url": "https://arxiv.org/html/2407.10899v1"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v2"
          },
          {
            "title": "[2602.00521] Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory",
            "url": "https://arxiv.org/abs/2602.00521"
          },
          {
            "title": "A Short Note on Aberrant Responses Bias in Item Response Theory",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6365413/"
          },
          {
            "title": "JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory",
            "url": "https://arxiv.org/pdf/2509.22888"
          },
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/pdf/2510.07175"
          },
          {
            "title": "Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking",
            "url": "https://arxiv.org/pdf/2603.23506"
          }
        ]
      },
      "Based on the web search results, I found several highly relevant papers from arXiv that address the intersection of Item Response Theory (IRT), LLM evaluation, contamination, and cheating detection:\n\n## Key Papers Found:\n\n**1. Distinguishing Human from AI Responses (2025)**\nA paper accepted to the 15th International Learning Analytics & Knowledge Conference focuses on using cheating with AI, separating AI from humans, and item-response theory person-fit statistics. IRT is described as a psychometric framework used to model the relationship between individuals' responses to assessment items and their underlying traits or abilities.\n\n**2. Data Contamination in LLM Benchmarking (2025)**\nThe PSN-IRT framework combines psychometrics with neural networks to analyze LLM benchmarks, demonstrating that current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination.\n\n**3. Quantifying Data Contamination in Psychometric Evaluations (2025)**\nLLMs may have encountered psychometric items during pretraining, creating a risk of data contamination where test results may reflect prior exposure rather than genuine characteristics.\n\n**4. LLM-as-a-Judge Reliability Assessment (2026)**\nA framework grounded in Item Response Theory assesses the reliability of LLM judges using the Graded Response Model, examining intrinsic consistency and human alignment.\n\n**5. Adaptive Testing for LLM Evaluation (2026)**\nStatic benchmarks are vulnerable to data contamination, and computerized adaptive testing (CAT) frameworks grounded in IRT offer an alternative for efficient assessment of LLMs.\n\nThese papers collectively address your search terms, focusing on using IRT for detecting anomalous response patterns, evaluating LLMs reliably, and identifying data contamination issues."
    ],
    "durationSeconds": 7.424004136000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "514b4c6f-632c-4e35-a7cb-f56349aea2ef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T03:36:43.526Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016afFGeCGeFixQuUhWZwUQe`</summary>

```json
{
  "query": "\"person-fit\" \"lz\" aberrant response pattern LLM contamination benchmark cheating detection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a653546-6618-4bf7-929f-df034c089d12",
  "isSidechain": false,
  "requestId": "req_011CbD81pNuw5TQoYg8PwAaf",
  "type": "assistant",
  "uuid": "02419fdc-25f3-461c-8947-e2007dfc3865",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmuZSwmyGGangpFaUGLjyf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 24423,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 24423,
          "cache_creation_input_tokens": 916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 916
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

_source line 28 · 2026-05-20T03:36:58.245Z_

<details><summary>↩ Tool result · `toolu_016afFGeCGeFixQuUhWZwUQe`</summary>

```text
Web search results for query: ""person-fit" "lz" aberrant response pattern LLM contamination benchmark cheating detection 2025 2026"

Links: [{"title":"Full article: An Iterative Scale Purification Procedure on lz for the Detection of Aberrant Responses","url":"https://www.tandfonline.com/doi/full/10.1080/00273171.2023.2211564"},{"title":"An Iterative Scale Purification Procedure on lz for the Detection of Aberrant Responses - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/37261427/"},{"title":"Rise of the Machine: Detecting Aberrant Response Patterns in Survey Instruments Using Autoencoder - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12904810/"},{"title":"Evaluating LLM-Contaminated Crowdsourcing Data Without Ground Truth","url":"https://arxiv.org/pdf/2506.06991"},{"title":"Benchmark Data Contamination of Large Language Models: A Survey","url":"https://arxiv.org/html/2406.04244v1"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/pdf/2408.14352"}]

I found relevant search results on your query. Here's what I found:

## Person-Fit Statistics and Aberrant Response Detection

Person-fit statistics have been proposed to detect aberrant response behaviors like cheating and guessing, with lz being one of the most widely used indices. An lz value smaller than −1.645 (at 0.05 one-tailed significance) indicates rejection of the null hypothesis, marking the response pattern as aberrant.

When aberrant behaviors occur, person and item parameter estimations become inaccurate, degrading lz performance, so iterative procedures have been developed to attain more accurate person parameter estimates.

## Recent Work on Aberrant Response Patterns

Person-fit analysis, grounded in item response theory (IRT), evaluates how well an individual's response pattern conforms to model expectations through person-fit statistics including likelihood-based measures such as Lz.

## LLM Contamination and Benchmark Cheating Detection

The search results also retrieved recent papers on related topics: Large Language Models like GPT-4, Claude-3, and Gemini have resulted in a significant issue known as Benchmark Data Contamination (BDC), which occurs when models inadvertently incorporate evaluation benchmark information from their training data.

Model developers could contaminate LRMs to achieve inflated leaderboard performance while leaving minimal traces, underlining the need for advanced contamination detection methods and trustworthy evaluation protocols.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02419fdc-25f3-461c-8947-e2007dfc3865",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "f137ea83-e81e-4681-8bce-c1a3b13c5dd6",
  "toolUseResult": {
    "query": "\"person-fit\" \"lz\" aberrant response pattern LLM contamination benchmark cheating detection 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QQgA1AoQnPa1aRXcML6Dzq",
        "content": [
          {
            "title": "Full article: An Iterative Scale Purification Procedure on lz for the Detection of Aberrant Responses",
            "url": "https://www.tandfonline.com/doi/full/10.1080/00273171.2023.2211564"
          },
          {
            "title": "An Iterative Scale Purification Procedure on lz for the Detection of Aberrant Responses - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/37261427/"
          },
          {
            "title": "Rise of the Machine: Detecting Aberrant Response Patterns in Survey Instruments Using Autoencoder - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12904810/"
          },
          {
            "title": "Evaluating LLM-Contaminated Crowdsourcing Data Without Ground Truth",
            "url": "https://arxiv.org/pdf/2506.06991"
          },
          {
            "title": "Benchmark Data Contamination of Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2406.04244v1"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "LogProber: Disentangling confidence from contamination in LLM responses",
            "url": "https://arxiv.org/pdf/2408.14352"
          }
        ]
      },
      "I found relevant search results on your query. Here's what I found:\n\n## Person-Fit Statistics and Aberrant Response Detection\n\nPerson-fit statistics have been proposed to detect aberrant response behaviors like cheating and guessing, with lz being one of the most widely used indices. An lz value smaller than −1.645 (at 0.05 one-tailed significance) indicates rejection of the null hypothesis, marking the response pattern as aberrant.\n\nWhen aberrant behaviors occur, person and item parameter estimations become inaccurate, degrading lz performance, so iterative procedures have been developed to attain more accurate person parameter estimates.\n\n## Recent Work on Aberrant Response Patterns\n\nPerson-fit analysis, grounded in item response theory (IRT), evaluates how well an individual's response pattern conforms to model expectations through person-fit statistics including likelihood-based measures such as Lz.\n\n## LLM Contamination and Benchmark Cheating Detection\n\nThe search results also retrieved recent papers on related topics: Large Language Models like GPT-4, Claude-3, and Gemini have resulted in a significant issue known as Benchmark Data Contamination (BDC), which occurs when models inadvertently incorporate evaluation benchmark information from their training data.\n\nModel developers could contaminate LRMs to achieve inflated leaderboard performance while leaving minimal traces, underlining the need for advanced contamination detection methods and trustworthy evaluation protocols."
    ],
    "durationSeconds": 14.715177276999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "02419fdc-25f3-461c-8947-e2007dfc3865",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T03:36:58.250Z_

```json
{
  "parentUuid": "f137ea83-e81e-4681-8bce-c1a3b13c5dd6",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7ef6cf74-ff61-4b5a-a087-d49587574789",
  "timestamp": "2026-05-20T03:36:58.250Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T03:37:00.453Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QhXGMop1RdFU9ekvJEJjPA`</summary>

```json
{
  "query": "ConStat NeurIPS 2024 contamination detection performance-based LLM benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ef6cf74-ff61-4b5a-a087-d49587574789",
  "isSidechain": false,
  "requestId": "req_011CbD834gQsrz2taZ63ngg2",
  "type": "assistant",
  "uuid": "3d6a82d4-c96d-4ce7-af3d-3dcfaf918911",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEXCNJGUnzZPDCwFXrBynk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 891,
      "cache_read_input_tokens": 25339,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 891,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 25339,
          "cache_creation_input_tokens": 891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 891
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

_source line 31 · 2026-05-20T03:37:05.862Z_

<details><summary>↩ Tool result · `toolu_01QhXGMop1RdFU9ekvJEJjPA`</summary>

```text
Web search results for query: "ConStat NeurIPS 2024 contamination detection performance-based LLM benchmark"

Links: [{"title":"[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://openreview.net/pdf?id=ALISPmDPCq"},{"title":"NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://neurips.cc/virtual/2024/poster/96266"},{"title":"NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://nips.cc/virtual/2024/poster/96266"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/html/2405.16281v1"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language   Models","url":"https://arxiv.org/pdf/2405.16281"},{"title":"[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/abs/2405.16281"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models | SRI Lab","url":"https://www.sri.inf.ethz.ch/publications/dekoninck2024constat"}]

Based on the search results, here's what I found about ConStat:

## Overview

ConStat is a statistical test presented at NeurIPS 2024 that detects and quantifies benchmark contamination in LLMs. It works by comparing primary and reference benchmark performance relative to reference models to reliably detect and quantify contamination.

## Performance-Based Definition

ConStat defines contamination as artificially inflated, non-generalizing performance—a model is contaminated if its performance relative to other models is significantly higher on the original benchmark than on a similar reference benchmark. This enables detection of any model with inflated performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.

## Performance Results

ConStat detects 89.1% of syntax-specifically contaminated models (surpassing the best baseline's 85%) and identifies 98.4% of sample-specifically contaminated models (significantly higher than the best baseline's 71%).

## Key Findings

The research found high levels of contamination in multiple popular models including Mistral, Llama, Yi, and the top-3 Open LLM Leaderboard models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d6a82d4-c96d-4ce7-af3d-3dcfaf918911",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "21317695-606d-415f-86f8-6bf63ab36cb5",
  "toolUseResult": {
    "query": "ConStat NeurIPS 2024 contamination detection performance-based LLM benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_017B576Gy63KWEd3ZTdkzx9Q",
        "content": [
          {
            "title": "[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://openreview.net/pdf?id=ALISPmDPCq"
          },
          {
            "title": "NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://neurips.cc/virtual/2024/poster/96266"
          },
          {
            "title": "NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://nips.cc/virtual/2024/poster/96266"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://arxiv.org/html/2405.16281v1"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language   Models",
            "url": "https://arxiv.org/pdf/2405.16281"
          },
          {
            "title": "[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://arxiv.org/abs/2405.16281"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models | SRI Lab",
            "url": "https://www.sri.inf.ethz.ch/publications/dekoninck2024constat"
          }
        ]
      },
      "Based on the search results, here's what I found about ConStat:\n\n## Overview\n\nConStat is a statistical test presented at NeurIPS 2024 that detects and quantifies benchmark contamination in LLMs. It works by comparing primary and reference benchmark performance relative to reference models to reliably detect and quantify contamination.\n\n## Performance-Based Definition\n\nConStat defines contamination as artificially inflated, non-generalizing performance—a model is contaminated if its performance relative to other models is significantly higher on the original benchmark than on a similar reference benchmark. This enables detection of any model with inflated performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.\n\n## Performance Results\n\nConStat detects 89.1% of syntax-specifically contaminated models (surpassing the best baseline's 85%) and identifies 98.4% of sample-specifically contaminated models (significantly higher than the best baseline's 71%).\n\n## Key Findings\n\nThe research found high levels of contamination in multiple popular models including Mistral, Llama, Yi, and the top-3 Open LLM Leaderboard models."
    ],
    "durationSeconds": 5.405448763999986,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3d6a82d4-c96d-4ce7-af3d-3dcfaf918911",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T03:37:09.140Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MYyqoZfmLv98cEq81wxfTz`</summary>

```json
{
  "query": "\"Silicon Bureaucracy\" contamination sensitivity score confidence perturbation 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21317695-606d-415f-86f8-6bf63ab36cb5",
  "isSidechain": false,
  "requestId": "req_011CbD83dZazkeqVbRubyXE1",
  "type": "assistant",
  "uuid": "a22ca9b2-e01b-412b-afcb-a717da65e7e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVWcMiNERzhbRH6RD71rcV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 26230,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 26230,
          "cache_creation_input_tokens": 881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 881
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs  ## Description We propos…",
  "leafUuid": "a22ca9b2-e01b-412b-afcb-a717da65e7e2",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT-based benchmark contamination detection for LLMs",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404"
}
```

---

### Tool result

_source line 35 · 2026-05-20T03:37:15.266Z_

<details><summary>↩ Tool result · `toolu_01MYyqoZfmLv98cEq81wxfTz`</summary>

```text
Web search results for query: ""Silicon Bureaucracy" contamination sensitivity score confidence perturbation 2026 arXiv"

Links: [{"title":"[2603.21636] Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/abs/2603.21636"},{"title":"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/html/2603.21636"},{"title":"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/pdf/2603.21636"},{"title":"[2604.08974] Confident in a Confidence Score: Investigating the Sensitivity of Confidence Scores to Supervised Fine-Tuning","url":"https://arxiv.org/abs/2604.08974"},{"title":"[2604.17771] SPENCE: A Syntactic Probe for Detecting Contamination in NL2SQL Benchmarks","url":"https://arxiv.org/abs/2604.17771"}]

Based on the search results, I found the paper you're looking for:

**"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks"** is an arXiv paper published March 23, 2026, which frames the benchmark-centered regime as "Silicon Bureaucracy and AI Test-Oriented Education".

**Key Details:**

The paper proposes an audit framework for analyzing contamination sensitivity and score confidence in LLM benchmarks. 

The researchers use a router-worker setup to compare a clean-control condition with noisy conditions in which benchmark problems are systematically deleted, rewritten, and perturbed before being passed downstream.

Across multiple models, they find widespread but heterogeneous above-baseline gains under noisy conditions, indicating that benchmark-related cues may be reassembled and can reactivate contamination-related memory.

Rather than rejecting benchmarks altogether, the authors argue that benchmark-based evaluation should be supplemented with explicit audits of contamination sensitivity and score confidence.

The paper is available at: https://arxiv.org/abs/2603.21636


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a22ca9b2-e01b-412b-afcb-a717da65e7e2",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "e070121d-47ae-4ded-b7c4-4471ddfe7257",
  "toolUseResult": {
    "query": "\"Silicon Bureaucracy\" contamination sensitivity score confidence perturbation 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AwPZ7HZxZXuEsFGM2FM6um",
        "content": [
          {
            "title": "[2603.21636] Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks",
            "url": "https://arxiv.org/abs/2603.21636"
          },
          {
            "title": "Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks",
            "url": "https://arxiv.org/html/2603.21636"
          },
          {
            "title": "Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks",
            "url": "https://arxiv.org/pdf/2603.21636"
          },
          {
            "title": "[2604.08974] Confident in a Confidence Score: Investigating the Sensitivity of Confidence Scores to Supervised Fine-Tuning",
            "url": "https://arxiv.org/abs/2604.08974"
          },
          {
            "title": "[2604.17771] SPENCE: A Syntactic Probe for Detecting Contamination in NL2SQL Benchmarks",
            "url": "https://arxiv.org/abs/2604.17771"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**\"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks\"** is an arXiv paper published March 23, 2026, which frames the benchmark-centered regime as \"Silicon Bureaucracy and AI Test-Oriented Education\".\n\n**Key Details:**\n\nThe paper proposes an audit framework for analyzing contamination sensitivity and score confidence in LLM benchmarks. \n\nThe researchers use a router-worker setup to compare a clean-control condition with noisy conditions in which benchmark problems are systematically deleted, rewritten, and perturbed before being passed downstream.\n\nAcross multiple models, they find widespread but heterogeneous above-baseline gains under noisy conditions, indicating that benchmark-related cues may be reassembled and can reactivate contamination-related memory.\n\nRather than rejecting benchmarks altogether, the authors argue that benchmark-based evaluation should be supplemented with explicit audits of contamination sensitivity and score confidence.\n\nThe paper is available at: https://arxiv.org/abs/2603.21636"
    ],
    "durationSeconds": 6.121335426999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a22ca9b2-e01b-412b-afcb-a717da65e7e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T03:37:17.959Z_

Now let me do one more critical search — checking if anyone has already connected IRT person-fit to LLM contamination detection:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e070121d-47ae-4ded-b7c4-4471ddfe7257",
  "isSidechain": false,
  "requestId": "req_011CbD84KXQa893DCRs2c8tk",
  "type": "assistant",
  "uuid": "ba2be859-9ea4-4dac-aac5-e2478371af7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QAFixc1GG6wafu8pEyCJp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 27111,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 27111,
          "cache_creation_input_tokens": 652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 652
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

_source line 37 · 2026-05-20T03:37:18.820Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MLYEL7kMtHYTxxK8F5tJ6z`</summary>

```json
{
  "query": "item response theory person fit statistics aberrant response LLM artificial intelligence benchmark evaluation cheating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba2be859-9ea4-4dac-aac5-e2478371af7f",
  "isSidechain": false,
  "requestId": "req_011CbD84KXQa893DCRs2c8tk",
  "type": "assistant",
  "uuid": "c97beadf-aa8a-4602-9f19-dcacfd57570e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019QAFixc1GG6wafu8pEyCJp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 27111,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 98,
          "cache_read_input_tokens": 27111,
          "cache_creation_input_tokens": 652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 652
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

_source line 38 · 2026-05-20T03:37:25.931Z_

<details><summary>↩ Tool result · `toolu_01MLYEL7kMtHYTxxK8F5tJ6z`</summary>

```text
Web search results for query: "item response theory person fit statistics aberrant response LLM artificial intelligence benchmark evaluation cheating"

Links: [{"title":"Applying Item Response Theory to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments","url":"https://arxiv.org/html/2412.02713v1"},{"title":"Using Benchmarking Infrastructure to Evaluate LLM Performance on CS Concept Inventories: Challenges, Opportunities, and Critiques","url":"https://dl.acm.org/doi/fullHtml/10.1145/3632620.3671097"},{"title":"A Short Note on Aberrant Responses Bias in Item Response Theory","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6365413/"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689v2"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/pdf/2602.00521"}]

I found several highly relevant research papers and articles on this topic. Here's what the search results show:

## Key Findings:

**Item Response Theory and AI Cheating Detection:**
A recent approach applies Item Response Theory (IRT) to detect AI cheating in multiple-choice assessments by modeling deviations from expected human response patterns using Person-Fit Statistics (PFS). This method operates on the assumption that artificial and human intelligence exhibit different response patterns, with AI cheating manifesting as deviations from the expected patterns of human responses.

**Aberrant Responses in IRT:**
Item response models often cannot calculate true individual response probabilities because of the existence of response disturbances such as guessing and cheating. Aberrant responses are often strange and different than expected, with a response inconsistent with expectation said to be aberrant.

**IRT Applied to LLM Benchmarking:**
Item Response Theory is a psychometric framework widely used in educational assessment that analyzes item properties such as difficulty by modeling item response against examinee ability. Recent work introduces adaptive testing frameworks based on IRT that estimate model ability using Fisher information-guided item selection, reducing the number of required items by up to 90% while maintaining measurement precision.

**Benchmark Quality Issues:**
Inconsistencies between different leaderboards and poor separability among top models raise concerns about the ability of benchmarks to accurately reflect authentic model capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c97beadf-aa8a-4602-9f19-dcacfd57570e",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "9f2445c1-b5fe-4c5a-9900-7648f0835481",
  "toolUseResult": {
    "query": "item response theory person fit statistics aberrant response LLM artificial intelligence benchmark evaluation cheating",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HyE96p9LxEV7z7TYEh9U3d",
        "content": [
          {
            "title": "Applying Item Response Theory to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments",
            "url": "https://arxiv.org/html/2412.02713v1"
          },
          {
            "title": "Using Benchmarking Infrastructure to Evaluate LLM Performance on CS Concept Inventories: Challenges, Opportunities, and Critiques",
            "url": "https://dl.acm.org/doi/fullHtml/10.1145/3632620.3671097"
          },
          {
            "title": "A Short Note on Aberrant Responses Bias in Item Response Theory",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6365413/"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/pdf/2505.15055"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/html/2511.04689v2"
          },
          {
            "title": "[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/abs/2505.15055"
          },
          {
            "title": "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory",
            "url": "https://arxiv.org/pdf/2602.00521"
          }
        ]
      },
      "I found several highly relevant research papers and articles on this topic. Here's what the search results show:\n\n## Key Findings:\n\n**Item Response Theory and AI Cheating Detection:**\nA recent approach applies Item Response Theory (IRT) to detect AI cheating in multiple-choice assessments by modeling deviations from expected human response patterns using Person-Fit Statistics (PFS). This method operates on the assumption that artificial and human intelligence exhibit different response patterns, with AI cheating manifesting as deviations from the expected patterns of human responses.\n\n**Aberrant Responses in IRT:**\nItem response models often cannot calculate true individual response probabilities because of the existence of response disturbances such as guessing and cheating. Aberrant responses are often strange and different than expected, with a response inconsistent with expectation said to be aberrant.\n\n**IRT Applied to LLM Benchmarking:**\nItem Response Theory is a psychometric framework widely used in educational assessment that analyzes item properties such as difficulty by modeling item response against examinee ability. Recent work introduces adaptive testing frameworks based on IRT that estimate model ability using Fisher information-guided item selection, reducing the number of required items by up to 90% while maintaining measurement precision.\n\n**Benchmark Quality Issues:**\nInconsistencies between different leaderboards and poor separability among top models raise concerns about the ability of benchmarks to accurately reflect authentic model capabilities."
    ],
    "durationSeconds": 7.107386816999991,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c97beadf-aa8a-4602-9f19-dcacfd57570e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T03:37:28.598Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now also check the specific paper about using IRT person-fit to distinguish AI from human responses, since that's very close to this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f2445c1-b5fe-4c5a-9900-7648f0835481",
  "isSidechain": false,
  "requestId": "req_011CbD8574LvrMyV7yYPeoHx",
  "type": "assistant",
  "uuid": "e4c206c6-58c8-4454-8022-ce420c0f37a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHo1Xh1y9kixYQXVJCZna2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 27763,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 27763,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
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

_source line 40 · 2026-05-20T03:37:29.114Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Piwj5c8bjcmf7dSMP5hw7k`</summary>

```json
{
  "query": "arXiv 2412.02713 \"person-fit statistics\" AI cheating detection multiple choice IRT distinguish human generative AI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4c206c6-58c8-4454-8022-ce420c0f37a4",
  "isSidechain": false,
  "requestId": "req_011CbD8574LvrMyV7yYPeoHx",
  "type": "assistant",
  "uuid": "913e1657-5234-4768-a753-5e2c96539ab0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHo1Xh1y9kixYQXVJCZna2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 27763,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 27763,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
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

_source line 41 · 2026-05-20T03:37:34.841Z_

<details><summary>↩ Tool result · `toolu_01Piwj5c8bjcmf7dSMP5hw7k`</summary>

```text
Web search results for query: "arXiv 2412.02713 "person-fit statistics" AI cheating detection multiple choice IRT distinguish human generative AI"

Links: [{"title":"[2412.02713] Applying IRT to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments","url":"https://arxiv.org/abs/2412.02713"},{"title":"Appraising Traditional and Purpose-built Person Fit Statistics’ Power to Detect Cheating","url":"https://www.ce-jeme.org/journal/vol3/iss1/3/"},{"title":"Applying Item Response Theory to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments","url":"https://arxiv.org/html/2412.02713"},{"title":"A new method for cheating detection during computerized adaptive testing | Computational Statistics | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00180-026-01739-1"},{"title":"Applying Item Response Theory to Distinguish Between Human and Generative","url":"https://arxiv.org/pdf/2412.02713"},{"title":"Using Person Fit Statistics to Detect Outliers in Survey Research","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5445123/"},{"title":"The Detection of Cheating on E-Exams in Higher Education—The Performance of Several Old and Some New Indicators","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7573546/"},{"title":"Reducing Calibration Bias for Person Fit Assessment by Mixture Model Expansion","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12413990/"}]

I found the paper you were looking for! Here are the key details about arXiv 2412.02713:

## Paper Summary

The paper addresses AI cheating in educational assessments, focusing on multiple-choice questions (MCQs), which has been largely unexplored compared to detecting AI-cheating on text-rich outputs. The authors propose a method based on Item Response Theory (IRT) to address this gap.

## Methodology

The approach operates on the assumption that artificial and human intelligence exhibit different response patterns, with AI cheating manifesting as deviations from expected human response patterns. These deviations are modeled using Person-Fit Statistics.

## Key Findings

The method effectively highlights the differences between human responses and those generated by premium versions of leading chatbots (ChatGPT, Claude, and Gemini), but is also sensitive to the amount of AI cheating in the data.

The paper was accepted to The 15th International Learning Analytics and Knowledge Conference (LAK'25) and was published to arXiv in December 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "913e1657-5234-4768-a753-5e2c96539ab0",
  "isSidechain": false,
  "promptId": "24d78e4e-49b7-46a9-a324-1e7b99546d2d",
  "type": "user",
  "uuid": "ce77f779-73f7-4221-a286-8ba33288fd3c",
  "toolUseResult": {
    "query": "arXiv 2412.02713 \"person-fit statistics\" AI cheating detection multiple choice IRT distinguish human generative AI",
    "results": [
      {
        "tool_use_id": "srvtoolu_015afyzDWERMvkVUKMM39xmC",
        "content": [
          {
            "title": "[2412.02713] Applying IRT to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments",
            "url": "https://arxiv.org/abs/2412.02713"
          },
          {
            "title": "Appraising Traditional and Purpose-built Person Fit Statistics’ Power to Detect Cheating",
            "url": "https://www.ce-jeme.org/journal/vol3/iss1/3/"
          },
          {
            "title": "Applying Item Response Theory to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments",
            "url": "https://arxiv.org/html/2412.02713"
          },
          {
            "title": "A new method for cheating detection during computerized adaptive testing | Computational Statistics | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s00180-026-01739-1"
          },
          {
            "title": "Applying Item Response Theory to Distinguish Between Human and Generative",
            "url": "https://arxiv.org/pdf/2412.02713"
          },
          {
            "title": "Using Person Fit Statistics to Detect Outliers in Survey Research",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5445123/"
          },
          {
            "title": "The Detection of Cheating on E-Exams in Higher Education—The Performance of Several Old and Some New Indicators",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7573546/"
          },
          {
            "title": "Reducing Calibration Bias for Person Fit Assessment by Mixture Model Expansion",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12413990/"
          }
        ]
      },
      "I found the paper you were looking for! Here are the key details about arXiv 2412.02713:\n\n## Paper Summary\n\nThe paper addresses AI cheating in educational assessments, focusing on multiple-choice questions (MCQs), which has been largely unexplored compared to detecting AI-cheating on text-rich outputs. The authors propose a method based on Item Response Theory (IRT) to address this gap.\n\n## Methodology\n\nThe approach operates on the assumption that artificial and human intelligence exhibit different response patterns, with AI cheating manifesting as deviations from expected human response patterns. These deviations are modeled using Person-Fit Statistics.\n\n## Key Findings\n\nThe method effectively highlights the differences between human responses and those generated by premium versions of leading chatbots (ChatGPT, Claude, and Gemini), but is also sensitive to the amount of AI cheating in the data.\n\nThe paper was accepted to The 15th International Learning Analytics and Knowledge Conference (LAK'25) and was published to arXiv in December 2024."
    ],
    "durationSeconds": 5.722704060999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "913e1657-5234-4768-a753-5e2c96539ab0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-20T03:38:50.726Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important! There is a paper (arXiv 2412.02713) from December 2024 that uses IRT person-fit statistics to distinguish between human and AI responses. This is related but different from the proposal — that paper uses person-fit to detect when a human used AI to cheat on assessments, whereas the proposal uses person-fit to detect when an LLM has been contaminated with benchmark data.

The analogy is similar but the direction is different:
- 2412.02713: Human cheats using AI → person-fit detects aberrant response pattern
- IRT-FIT proposal: LLM contaminated with benchmark data → person-fit detects aberrant response pattern


Both approaches leverage person-fit statistics to identify unusual response patterns, but they're targeting different contamination scenarios. I should check whether there are other concurrent works specifically connecting IRT person-fit to LLM contamination detection beyond the human cheating angle, and I need to review the Cross-Context Verification and Han et al. EACL 2026 papers to complete my landscape analysis before synthesizing my findings.

Looking at what I've confirmed so far: PSN-IRT calibrates parameters across thousands of benchmark items and provides the foundational infrastructure needed; Wang et al. demonstrates that existing MIA detectors break down under RL post-training; Self-Critique offers a competing approach using entropy-sequence patterns to catch post-RL contamination; CoDeC and ConStat provide alternative detection methods; and the LAK 2025 paper using IRT person-fit statistics to distinguish human from AI responses is conceptually closest to what the proposal is attempting.

The gap I'm identifying is that while person-fit statistics could theoretically detect contamination by flagging models that perform anomalously on benchmark items, ConStat already uses performance-based detection through original versus rephrased comparisons. The real question becomes whether formalizing this through IRT adds meaningful value beyond what's already established.

I'm considering whether a simpler approach—just measuring the correlation between item difficulty and model accuracy and flagging anomalously low correlations—would capture the same signal without the full IRT machinery. The proposal's strength would rest on person-fit's Type-I error control, the 4PL model's handling of guessing and feasibility, and its ability to detect partial contamination at lower percentages.

But I'm also recognizing a key vulnerability: the analogy between benchmark contamination and educational item preknowledge isn't perfect. Models might show non-monotonic difficulty curves for reasons entirely unrelated to contamination—like being exceptionally strong in mathematics but weak in communication tasks.

There's also the issue of local independence. IRT assumes item responses are independent given ability, but LLM outputs across items likely correlate through shared knowledge and prompt sensitivity. Within a single benchmark like MMLU, the diversity of subtopics means a single latent trait probably doesn't capture the full picture, even with EFA screening. And there's the blind spot with complete dataset memorization—the proposal acknowledges it, but it's still a significant limitation. The core assumption that contaminated items produce a specific, detectable response pattern may not hold as cleanly in LLMs as it does in educational testing scenarios.

The novelty here is really about applying person-fit statistics from psychometrics to LLM contamination detection—that cross-domain transfer hasn't been done before. The person-fit statistics themselves are established, and the IRT framework comes from existing work, but recognizing this analogy and implementing it for contamination detection is genuinely novel, even if it's more of a novel application than a novel method.

On significance, the research tackles an important problem—benchmark contamination is a real concern, and black-box detection matters as models become more closed. But the practical value hinges on whether person-fit actually outperforms existing methods in real scenarios. The 5-30% detection range is useful but narrow, and I should note that Self-Critique and ConStat already address similar gaps with reasonable effectiveness. Also, I'm noticing the system prompt mentions CoRL 2026, but this proposal targets AAAI 2027 and ICLR 2027—CoRL is robotics, which doesn't fit here at all. I'm noticing the system prompt mentions CoRL 2026, but the actual proposal targets AAAI 2027 and ICLR 2027 — this seems like a template mismatch. Regardless, I should evaluate the idea itself based on the rubric provided. Looking at novelty, the cross-domain application of IRT person-fit statistics to LLM contamination detection is genuinely novel in its connection, though the underlying methodologies are established. The core contribution is recognizing this analogy and implementing it, though similar person-fit approaches for human-vs-AI detection have already appeared in recent work. The core issue is that while the analogy is elegant, it's fundamentally a methodological application rather than a conceptual breakthrough—once you make the person-fit connection, the execution path becomes fairly predictable. The inverted-U detection curve itself isn't surprising given what we know from educational testing, so even positive results would likely feel confirmatory rather than revelatory to reviewers. Weighing the clean motivation and solid experimental infrastructure against the moderate novelty, I'm settling on around 30% for AAAI 2027, though I should reconsider the positive factors more carefully for top-tier venues. I'm factoring in that AAAI has shown interest in this cross-domain psychometrics-to-NLP approach—PSN-IRT got an oral there—while ICLR might demand more technical novelty. Accounting for venue variation, I'd estimate 23-33% acceptance probability, with 28% as the midpoint.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce77f779-73f7-4221-a286-8ba33288fd3c",
  "isSidechain": false,
  "requestId": "req_011CbD85m5LWTE4bVxmrDktc",
  "type": "assistant",
  "uuid": "1717c3c5-b691-499c-9bff-cfb02b22ce7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARFv9kGUoPb6Bre9jyUrM3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 824,
      "cache_read_input_tokens": 28568,
      "output_tokens": 6871,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6871,
          "cache_read_input_tokens": 28568,
          "cache_creation_input_tokens": 824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 824
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

_source line 43 · 2026-05-20T03:40:14.145Z_

Now I have enough research to make an informed assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:

1. PSN-IRT / "Lost in Benchmarks?" (AAAI 2026 Oral, arXiv 2505.15055):
   确认存在且描述准确。该工作使用 4PL IRT 模型对 41,871 个 items 进行参数校准，但其目的是评估 benchmark 测量质量，而非检测 contamination。为本 proposal 提供了关键基础设施。

2. Wang et al. "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (arXiv 2510.02386):
   确认存在且描述准确。实验表明 GRPO 训练可以显著遮蔽 SFT 阶段的 contamination 信号，使所有基于 MIA 的检测方法失效。这为本 proposal 提供了动机。

3. Self-Critique (arXiv 2510.09259, ICLR 2026):
   确认存在。通过 token-level entropy 探测 RL-induced policy collapse 来检测 post-RL 污染。AUC 比 baseline 提升约 30%。注意：这是本 proposal 在 post-RL 场景下的直接竞争者，且已证明有效——不是 gray-box 但需要 token probability 访问。

4. CoDeC (arXiv 2510.27055, ICLR 2026):
   确认存在。通过 in-context learning 对 memorized vs. unseen data 的差异效应检测 contamination。需要 gray-box（token probability）访问。

5. ConStat (NeurIPS 2024):
   确认存在。Performance-based 方法，比较原始 benchmark 与 rephrased/reference benchmark 的表现差异。这是当前最接近 "黑盒" 的方法之一，但需要构建 reference benchmark。

6. arXiv 2412.02713 "Applying IRT to Distinguish Between Human and Generative AI Responses" (LAK 2025):
   ⚠️ 本 proposal 未引用。这篇论文已经使用 IRT person-fit statistics 区分人类和 AI 的作答模式。虽然应用场景不同（学术诚信 vs. LLM contamination），但概念桥梁已被建立——person-fit 用于 AI 相关的异常检测并非全新。

7. Silicon Bureaucracy (arXiv 2603.21636, 2026):
   确认存在。通过 perturbation sensitivity analysis 审计 benchmark 分数可信度。与本 proposal 在精神上相近（都从测量学角度质疑分数可信度），但方法不同。

8. Han et al. "Quantifying Data Contamination in Psychometric Evaluations of LLMs" (EACL 2026 Findings, arXiv 2510.07175):
   确认存在。量化 LLM 在心理测量量表上的 contamination，但未使用 person-fit statistics。

- 调研总结: LLM benchmark contamination 检测是一个快速发展的领域，2024-2026 涌现了多个方法族。IRT 在 LLM 评估中的应用日趋成熟（PSN-IRT、ATLAS、JE-IRT 等），但 person-fit statistics 尚未被正式应用于 LLM contamination 检测。不过，person-fit 用于 AI 相关异常检测的概念已在 LAK 2025 中出现，说明"psychometric person-fit → AI 异常检测"这一桥梁正在被逐步搭建。本 proposal 的定位是一个有实质空白但非完全无人触及的交叉领域。


【Trivial Alternative 检验】:

存在一个成本显著更低的 trivial baseline：直接计算每个模型在 easy/hard items 上的 accuracy 偏差。具体来说，用 PSN-IRT 的 difficulty 参数 b 将 items 按难度排序，计算模型的"难度-正确率梯度"——如果模型在高难度 items 上的 accuracy 异常高于其整体能力预测值，就标记为可疑。这本质上是 person-fit statistics 要捕捉的核心信号（response pattern 偏离单调难度梯度），但不需要完整的 IRT 拟合和 lz* 计算。

此外，ConStat 已经是一个 performance-based 黑盒方法——虽然它需要 reference benchmark，但在实际应用中这个成本并不高。

IRT-FIT 相对于这些 trivial alternatives 的增量价值在于：
(a) person-fit statistics 有经过数十年验证的 Type-I error 控制；
(b) 4PL 模型的 d 参数可以区分 item ambiguity 和 contamination；
(c) lzm 多尺度聚合尊重多维能力结构。
这些增量价值是真实的，但属于"精细化改进"而非"质的跨越"。审稿人可能会认为简单的 difficulty-accuracy anomaly score 已经能捕捉大部分信号。


【前提假设检验】:

核心 claim 的逻辑链有以下未经验证的环节：

1. **"污染 LLM ≈ 考试作弊者" 类比的保真度**：教育测试中，作弊者拥有特定 item 的答案，导致在这些 items 上正确率为 1，而在其他 items 上反映真实能力。LLM contamination 的表现可能更复杂——memorization 不一定导致 100% 正确（可能只是更高的 confidence），且 SFT/RL 过程可能将 contamination 信号扩散到相邻知识区域，而非局限于特定 items。这意味着 LLM 的 aberrant pattern 可能与教育作弊者的 pattern 结构上不同，person-fit 的检测力可能因此打折。

2. **Local independence 假设**：IRT 和 person-fit statistics 都假设在给定 ability 的条件下，item responses 相互独立。LLM 的 responses 可能违反这一假设——同一 prompt template、相邻的 knowledge domain、甚至 context window 内的 items 都可能产生相关性。虽然 proposal 用 per-benchmark 分析和 EFA screening 来缓解这一问题，但 LLM-specific 的 local dependence 结构是否会系统性偏移 person-fit statistics 的分布是未知的。

3. **Stochastic response 假设**：IRT 要求 examinees 的 responses 具有概率性（即同一个人面对同一个 item 有时对有时错）。而 LLM 在 temperature=0 下是确定性的，同一 item 永远给出相同答案。这在技术上违反了 IRT 的概率模型基础。PSN-IRT 通过将多个模型作为"考生池"来校准 item 参数，回避了这个问题，但 person-fit statistics 在确定性 response 上的理论行为值得检验。

4. **Post-RL contamination 保留假设**：proposal 将 post-RL 场景作为"hypothesis test"而非"claimed advantage"，这是好的。但 Wang et al. 展示 RL 遮蔽了 MIA 信号，Self-Critique 发现 RL 导致 entropy collapse——如果 RL 同时平滑了 response-level aberrance（使得 contaminated items 上的优势被泛化到 uncontaminated items），那么 person-fit 同样会失效，而且失效的原因与 MIA 不同。


【3 维度打分】:

1. Novelty: 【中】
   — "IRT person-fit → LLM contamination 检测" 的跨领域迁移在字面上确实未发表（经调研确认无直接先例）。
   — 但 novelty 的本质是 application/connection，不是 methodology。Person-fit statistics（lz*, infit, outfit, lzm）全部来自现有文献；IRT 基础设施完全来自 PSN-IRT；实验设计是标准的 controlled contamination。核心贡献在于识别类比并实施，一旦类比被说出（contaminated LLM ≈ 作弊考生），后续技术路径基本是直接的。
   — arXiv 2412.02713 (LAK 2025) 已经在 AI 上下文中使用了 person-fit statistics（区分人类和 AI 作答），表明 "psychometric person-fit → AI 异常检测" 的桥梁已在被搭建，虽然具体场景不同。
   — 审稿人可能的反应："这是一个 neat application，但一旦有了 PSN-IRT 的 item parameters，计算 person-fit 是 obvious next step。"

2. Significance: 【中】
   — 研究问题重要且时效性强：benchmark contamination 是 LLM 评估的核心痛点，黑盒检测需求真实存在，post-RL 场景下现有方法失效（Wang et al.）创造了真实需求缺口。
   — 但实际影响力受限于 detection window 的狭窄性：5-30% contamination 是 policy-relevant，但 proposal 自身承认 <3% 和 >50% 无法检测，尤其 100% contamination（完整 benchmark 泄露）完全不可检测——这恰恰是实践中最常见和最受关注的场景。
   — Self-Critique (ICLR 2026) 已经为 post-RL 检测提供了有效方案（AUC 提升 30%），降低了本 proposal 在该场景上的边际贡献。
   — 如果核心实验结果是 positive（person-fit 在 10-30% 污染下检测力优于 baselines），审稿人更可能的反应是 "makes sense, nice to confirm"（因为这直接从教育测量文献预测），而非 "surprising, didn't expect that"。反过来，如果 negative，则有 "negative result + application paper" 的困境。

3. Related Work: 【强】
   — 对 contamination detection 五大方法族（time-based, MIA, Time Travel, ConStat, canary）的覆盖非常全面。
   — 对 2025-2026 年的新进展（CoDeC, Self-Critique, Silicon Bureaucracy, Cross-Context Verification）的覆盖及时。
   — IRT 侧的覆盖（PSN-IRT, ATLAS, Han et al.）充分。
   — 所有引用的论文经调研确认真实存在且描述基本准确。
   — 唯一缺漏：arXiv 2412.02713 (LAK 2025) 使用 person-fit 进行 AI-human 区分，概念上是最近的"邻居"，应被讨论和差异化。


【概率估计】: 23% - 33%，中位 28%

【估计理由】:
三个维度中 Novelty 和 Significance 均为"中"，Related Work 为"强"。Related Work 的强只保证了形式质量和定位清晰，但不能拉高 idea 本身的上限。

概率上界被 Novelty 和 Significance 共同限制：
- Novelty 是 application-level 而非 methodology-level，核心贡献是识别类比+实施（一旦 PSN-IRT 存在，person-fit 计算是 "obvious next step"的风险）。
- Significance 受限于 detection window 的狭窄性（5-30%）和 Self-Critique 已占位 post-RL 检测。
- 核心结果的 "surprise factor" 偏低——无论 positive 还是 negative，都可以从教育测量文献中大致预测。

概率下界被以下因素支撑：
- 跨领域迁移故事整洁、动机清晰。
- 真实存在的 gap（经调研确认无直接先例）。
- AAAI 对 psychometrics+AI 交叉工作有接受度（PSN-IRT 是 Oral）。
- Type-I error 理论保证是相对于 heuristic baselines 的真实优势。

【主要风险】:
1. **"Obvious next step" 质疑**：审稿人可能认为一旦 PSN-IRT 提供了校准的 item parameters，计算 person-fit 是自然延伸，novelty delta 不足以构成独立贡献。
2. **Detection window 实用性质疑**：5-30% partial contamination 是 proposal 自定义的"most policy-relevant window"，但审稿人可能反驳：实践中最常见的场景是 full benchmark leakage（训练数据中包含完整 benchmark），而 person-fit 在这种场景下完全失效（100% contamination = consistent high performance = 不 aberrant），严重削弱实际应用价值。
```

Sources:
- [PSN-IRT: Lost in Benchmarks? (AAAI 2026)](https://arxiv.org/abs/2505.15055)
- [Wang et al. On The Fragility of Benchmark Contamination Detection in Reasoning Models](https://arxiv.org/abs/2510.02386)
- [Self-Critique: Detecting Data Contamination from RL Post-training (ICLR 2026)](https://arxiv.org/abs/2510.09259)
- [CoDeC: Detecting Data Contamination via In-Context Learning (ICLR 2026)](https://arxiv.org/abs/2510.27055)
- [ConStat: Performance-Based Contamination Detection (NeurIPS 2024)](https://arxiv.org/abs/2405.16281)
- [Applying IRT to Distinguish Human and AI Responses (LAK 2025)](https://arxiv.org/abs/2412.02713)
- [Silicon Bureaucracy: Contamination Sensitivity and Score Confidence](https://arxiv.org/abs/2603.21636)
- [Han et al. Quantifying Data Contamination in Psychometric Evaluations of LLMs](https://arxiv.org/abs/2510.07175)
- [PSN-IRT GitHub Repository](https://github.com/Joe-Hall-Lee/PSN-IRT)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1717c3c5-b691-499c-9bff-cfb02b22ce7e",
  "isSidechain": false,
  "requestId": "req_011CbD85m5LWTE4bVxmrDktc",
  "type": "assistant",
  "uuid": "3734056f-53fe-4230-a43c-1db21fbea2bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARFv9kGUoPb6Bre9jyUrM3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 824,
      "cache_read_input_tokens": 28568,
      "output_tokens": 6871,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6871,
          "cache_read_input_tokens": 28568,
          "cache_creation_input_tokens": 824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 824
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs  ## Description We propos…",
  "leafUuid": "3734056f-53fe-4230-a43c-1db21fbea2bf",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT-based benchmark contamination detection for LLMs",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs  ## Description We propos…",
  "leafUuid": "3734056f-53fe-4230-a43c-1db21fbea2bf",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "IRT-based benchmark contamination detection for LLMs",
  "sessionId": "995d5f7d-0337-4bc7-84dd-9975da23f404"
}
```

---
