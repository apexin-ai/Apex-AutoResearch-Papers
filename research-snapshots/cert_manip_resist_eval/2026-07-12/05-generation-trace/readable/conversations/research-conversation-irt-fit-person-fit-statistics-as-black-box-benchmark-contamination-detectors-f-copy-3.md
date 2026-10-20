# Research conversation: IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs ## Description We propose IRT-FIT

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/4c224f93-82cc-4676-966b-092e5c76d381.jsonl`
- **Structured JSON:** [`755495130f39d001d643.json`](../../sessions/75/755495130f39d001d643.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:46:36.602Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:46:36.602Z",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "content": "# IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs\n\n## Description\nWe propose IRT-FIT, the first method that transfers person-fit statistics from educational psychometrics to detect LLM benchmark contamination in a fully black-box setting. The core insight is that a partially contaminated model, like a test-taker with item preknowledge, produces aberrant response patterns: it answers memorized hard items correctly while performance on non-memorized items reflects true ability, violating the monotonic difficulty gradient predicted by IRT. Using calibrated 4PL item parameters (discrimination, difficulty, guessing, and feasibility) from PSN-IRT (41,871 items, 11 benchmarks), we compute lz*, infit, outfit, and the multiscale lzm statistic for each model at two levels: per-benchmark (respecting unidimensionality via EFA-validated subscales) and aggregated (via the Hong-Lin-Cheng multiscale correction). We validate via controlled fine-tuning of three current open-source models — Llama 4 Scout 17B-16E (109B MoE), Qwen 3.5-9B (dense), and Gemma 4 31B (dense) — at seven contamination levels (0-100%) to empirically map the inverted-U detection power curve. We expect peak detection at 10-30% contamination, with explicit acknowledgment that 100% contamination is undetectable by person-fit (uniform high performance is consistent, not aberrant) and <3% contamination falls below statistical sensitivity. We benchmark against ConStat, PaCoST, CoDeC, Min-K%++, and Self-Critique, with a dedicated experiment testing the hypothesis (not assumption) that person-fit statistics maintain detection power on post-RL reasoning models where Wang et al. (2025) showed MIA-based methods fail. A 4PL-vs-3PL ablation quantifies how the feasibility parameter d affects sensitivity. We release an open-source toolkit with per-benchmark contamination flags and calibrated p-values inheriting Type-I error guarantees from decades of educational measurement theory.\n\n## Core Problem\nCan we detect benchmark contamination in LLMs without any access to training data or model internals, using only the pattern of correct/incorrect responses across benchmark items? Specifically, can psychometric person-fit statistics identify the 'sweet spot' of partial contamination (5-30% of items) where scores are meaningfully inflated but existing detectors fail?\n\n## Opportunity\nAll existing contamination detection methods require either training data access (n-gram overlap), model internals (Min-K% Probability, MIA, Self-Critique entropy sequences), or special probing prompts (Time Travel). Yet psychometrics has long used person-fit statistics like lz* to detect cheating examinees from response patterns alone — a contaminated LLM is functionally analogous to a test-taker with item preknowledge. This cross-domain transfer is newly feasible because IRT infrastructure for LLM evaluation has matured: PSN-IRT (AAAI 2026 Oral) calibrates 4PL item parameters (a, b, c, d) across 11 benchmarks and 41,871 items, providing the calibrated item bank needed to compute person-fit statistics at scale. The 4PL feasibility parameter d is particularly relevant — it accounts for item ambiguity that could otherwise be confused with contamination-induced aberrance, reducing false alarms. Meanwhile, Wang et al. (2025) demonstrate that all existing MIA-based detectors are fragile under reasoning-model contamination where RL post-training conceals SFT contamination signals, creating urgent demand for detection methods operating at a different level of abstraction.\n\n## Landscape\nContamination detection circa 2026 relies on five established families: (1) time-based partition, (2) Min-K%/Min-K%++ membership inference (ICLR 2024), (3) Time Travel probing (ICLR 2024 Spotlight), (4) ConStat performance-based testing (NeurIPS 2024), and (5) canary GUIDs. Newer approaches include CoDeC (ICLR 2026), which measures in-context learning effects on memorized vs. unseen data; Cross-Context Verification (arXiv 2603.21454), which uses session-isolated solution diversity; Self-Critique (arXiv 2510.09259, ICLR 2026), which detects post-RL contamination via policy collapse in entropy sequences with ~30% AUC improvement over baselines that perform near chance on RL-contaminated data; and Silicon Bureaucracy (arXiv 2603.21636), which audits score credibility through perturbation sensitivity analysis. Critically, Wang et al. (arXiv 2025) show all MIA-based methods fail under reasoning-model contamination where RL conceals SFT signals. On the IRT side, PSN-IRT (AAAI 2026 Oral) calibrates 4PL parameters (discrimination a, difficulty b, guessing c, feasibility d) across 11 benchmarks and 41,871 items but uses them for measurement quality, not contamination. ATLAS (arXiv 2025) uses IRT for adaptive testing efficiency. Han et al. (EACL 2026 Findings) quantify contamination in psychometric personality inventories but do not employ person-fit statistics. PaCoST (EMNLP 2024 Findings) uses paired confidence for contamination but is not IRT-based. In educational testing, lz* and outfit/infit statistics reliably flag cheating with known Type-I error control, with peak detection power at 10-30% item preknowledge (Sinharay, 2017; Karabatsos, 2003). No published or concurrent work connects IRT person-fit statistics to LLM benchmark contamination detection — an extensive search of arXiv 2025-2026, OpenReview, and GitHub confirms this gap remains open.\n\n## Approach\nWe compute four IRT person-fit statistics — lz, lz*, outfit, and infit — for each LLM using calibrated 4PL item parameters (a, b, c, d) from PSN-IRT's public release (41,871 items across 11 benchmarks). The analysis proceeds at two levels:\n\n**Level 1: Per-benchmark person-fit.** To respect the unidimensionality assumption, we compute person-fit statistics separately within each benchmark. Before fitting, we run an exploratory factor analysis (EFA) screen within each benchmark to validate approximate unidimensionality, following psychometric best practice (Crisan, Tendeiro & Meijer, 2017) and recent LLM evaluation precedent (arXiv:2509.24186). We focus on 6 benchmarks spanning diverse capabilities: MMLU (knowledge), GSM8K (math), HumanEval (coding), ARC-Challenge (science reasoning), HellaSwag (commonsense), and TruthfulQA (factuality).\n\n**Level 2: Aggregated contamination score.** We compute the multiscale lzm statistic (Hong, Lin & Cheng, 2021) — the standardized sum of per-benchmark lz* values — providing an overall contamination indicator that respects the multidimensional ability structure.\n\n**Controlled contamination experiment.** We establish ground truth by fine-tuning three open-source models (Llama 4 Scout 17B-16E, Qwen 3.5-9B, Gemma 4 31B) on varying fractions of benchmark items. We use seven contamination levels (0%, 5%, 10%, 15%, 25%, 50%, 100%) to map the detection power curve. Fine-tuning uses QLoRA to manage memory costs, particularly for the MoE-architecture Scout (109B total parameters, 17B active). For each contaminated variant, we compare person-fit signatures against clean baselines.\n\n**Power analysis and simulation.** We conduct a formal power analysis varying contamination fraction, number of contaminated items, and item difficulty distribution. Based on the educational testing literature, we expect an inverted-U detection power curve: undetectable below ~3% contamination (signal drowned in noise), peak detection at 10-30% (clear item-response aberrance), declining above 50% (inflated ability estimate absorbs contamination), and zero power at 100% (uniform high performance is consistent, not aberrant under IRT). We explicitly characterize this operating range and argue that 5-30% is the most policy-relevant detection window — where contamination meaningfully inflates scores but evades simple methods.\n\n**4PL ablation.** We compare person-fit statistics computed under the full 4PL model vs. a 3PL reduction (fixing d=1) to quantify how the feasibility parameter affects contamination detection sensitivity. The 4PL d parameter absorbs some item-level aberrance (Liao et al., 2012), which reduces false alarms from item ambiguity but may also reduce sensitivity to genuine contamination.\n\n**Post-RL hypothesis test.** As a key hypothesis (not a claimed advantage), we test whether person-fit statistics maintain detection power on post-RL reasoning models where Wang et al. (2025) showed existing MIA-based detectors fail. We create post-RL variants by applying GRPO fine-tuning after SFT-based contamination on Qwen 3.5-9B, specifically testing whether RL smooths out response-level aberrance or preserves it.\n\n**Baselines.** We evaluate detection performance (AUROC, Type-I error at fixed thresholds) against ConStat, PaCoST, CoDeC, Min-K%++, and Self-Critique across all contamination levels and training stages (SFT-only, SFT+RL).\n\n**Toolkit.** We release an open-source Python toolkit (built on py-irt and the R mirt package via rpy2, which natively supports 4PL person-fit computation) that takes any binary response matrix and calibrated 4PL item parameters and outputs per-model, per-benchmark contamination flags with calibrated p-values.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '300-400', 'timeline': '12 weeks', 'estimated_gpu_cost': '$750-1000 (H100 at ~$2.50/hr)'}, 'human_in_loop': {'gpu_hours': '280-350', 'timeline': '8-9 weeks', 'claude_api_cost': '$200-300', 'estimated_gpu_cost': '$700-875'}, 'auto_research': {'gpu_hours': '320-420', 'timeline': '5-6 weeks', 'claude_api_cost': '$400-600', 'estimated_gpu_cost': '$800-1050', 'speed_bottleneck': 'Sequential fine-tuning of contaminated model variants (3 base models × 7 contamination levels = 21 fine-tuning runs, plus 3 post-RL GRPO runs). Llama 4 Scout requires 4× H100 for QLoRA due to 109B total MoE parameters in memory; Gemma 4 31B needs 2× H100. Full-benchmark inference for 30+ models is parallelizable but each large model requires multi-GPU inference.'}, 'cost_breakdown': {'fine_tuning': 'Qwen 3.5-9B: ~15 GPU-hrs (7 levels × ~2 hrs); Gemma 4 31B: ~50 GPU-hrs (7 levels × ~7 hrs on 2× H100); Llama 4 Scout: ~70 GPU-hrs (7 levels × ~10 hrs on 4× H100). Post-RL GRPO variants: ~30 GPU-hrs. Total fine-tuning: ~165 GPU-hrs.', 'inference': '30+ models × 6 benchmarks × ~1-3 hrs/model depending on size: ~100-150 GPU-hrs.', 'simulation': 'Power analysis simulation (synthetic response matrices, 1000 replications × 7 contamination levels × 6 benchmarks): ~20 GPU-hrs on CPU/light GPU.', 'note': \"Costs increased ~50% vs. original estimate due to: (a) 7 contamination levels instead of 4, (b) Gemma 4 31B is 2.5× larger than originally assumed '12B', (c) explicit MoE memory overhead for Scout, (d) added simulation study and post-RL GRPO variants.\"}}\n\n## Inspired By\nField guide gap: 'MIA methods fail under single-epoch pre-training and post-RL concealment'; untried combination of IRT person-fit statistics (from psychometrics) with LLM contamination detection; the analogy between item preknowledge in educational cheating detection and benchmark memorization in LLM contamination; cross-domain transfer pattern from educational measurement to NLP evaluation; maturation of 4PL IRT infrastructure for LLMs (PSN-IRT) providing the calibrated item bank prerequisite.\n\n## Target Venues\n- AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026) — primary target: PSN-IRT was AAAI 2026 Oral, strong psychometrics+AI audience, 10 weeks from today is feasible with focused scope on 6 benchmarks\n- ICLR 2027 (abstract: ~Sep 19, 2026; full paper: ~Sep 24, 2026) — backup allowing fullest experimental scope including post-RL hypothesis test and expanded baseline comparisons\n\n## Key References\n- Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory (AAAI 2026 Oral, arXiv 2505.15055) — calibrates 4PL item parameters for 41,871 items across 11 benchmarks\n- Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks (arXiv 2511.04689) — ATLAS, IRT for adaptive testing efficiency\n- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024)\n- PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection (EMNLP 2024 Findings)\n- Detecting Pretraining Data from Large Language Models / Min-K% Probability (ICLR 2024)\n- Time Travel in LLMs: Tracing Data Contamination in Large Language Models (ICLR 2024 Spotlight)\n- On The Fragility of Benchmark Contamination Detection in Reasoning Models (arXiv 2510.02386) — Wang et al., shows MIA-based detectors fail under post-RL contamination\n- Detecting Data Contamination in LLMs via In-Context Learning / CoDeC (ICLR 2026)\n- Detecting Data Contamination from Reinforcement Learning Post-training / Self-Critique (arXiv 2510.09259, ICLR 2026) — post-RL contamination detection via entropy-sequence policy collapse\n- Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence (arXiv 2603.21636) — perturbation-based score credibility audit\n- Quantifying Data Contamination in Psychometric Evaluations of LLMs (EACL 2026 Findings) — Han et al.\n- Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis (arXiv 2603.21454)\n- Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types (Hong, Lin & Cheng, Psychometrika 2021) — lzm multiscale aggregation\n- Investigating the Practical Consequences of Model Misfit in Unidimensional IRT Models (Crisan, Tendeiro & Meijer, Applied Psychological Measurement 2017) — effects of unidimensionality violations on person-fit\n- The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses (Liao et al., 2012) — 4PL absorbs some aberrance via d parameter\n- Which Statistic Should Be Used to Detect Item Preknowledge? (Sinharay, JEBS 2017) — power analysis for preknowledge detection\n- Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics (Karabatsos, Applied Measurement in Education 2003)\n- PerFit: An R Package for Person-Fit Analysis in IRT (Journal of Statistical Software 2016)\n- py-irt: A Scalable Item Response Theory Library for Python (INFORMS Journal on Computing 2023)\n- mirt: A Multidimensional Item Response Theory Package for the R Environment (Journal of Statistical Software 2012) — supports 4PL person-fit natively\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:46:36.609Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:46:36.609Z",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-20T04:46:36.628Z_

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
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "5843b88a-be7e-49bb-b4eb-8bba6acdad41",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:46:36.626Z_

```json
{
  "parentUuid": "5843b88a-be7e-49bb-b4eb-8bba6acdad41",
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
  "uuid": "ce880aa1-75d2-4b7c-9678-19615847a941",
  "timestamp": "2026-05-20T04:46:36.626Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:46:36.626Z_

```json
{
  "parentUuid": "ce880aa1-75d2-4b7c-9678-19615847a941",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "61192288-fa1e-4cd5-b877-685edf986c7d",
  "timestamp": "2026-05-20T04:46:36.626Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
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
  "lastPrompt": "# IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs  ## Description We propose IRT-FIT, the first method that transfers person-fit statistics from educational psyc…",
  "leafUuid": "61192288-fa1e-4cd5-b877-685edf986c7d",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Detect LLM benchmark contamination using IRT person-fit statistics",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:46:40.612Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about using Item Response Theory (IRT) person-fit statistics from educational psychometrics to detect benchmark contamination in LLMs. Let me first do some web searches to understand the current landscape before giving my assessment.

Let me search for:
1. Recent work on IRT person-fit statistics for LLM evaluation
2. Recent benchmark contamination detection methods (2025-2026)
3. PSN-IRT and related work
4. Any work connecting person-fit to LLM contamination
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61192288-fa1e-4cd5-b877-685edf986c7d",
  "isSidechain": false,
  "requestId": "req_011CbDDM5B1hyAvjzyzUSptb",
  "type": "assistant",
  "uuid": "431ec141-3b36-4ddf-84f6-ff5b3bde0723",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yCx5L8nhdXu5BhYwnf8Y7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5427,
      "cache_read_input_tokens": 14549,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 239,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 5427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5427
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

_source line 9 · 2026-05-20T04:46:42.159Z_

I need to do thorough front-end research before evaluating this proposal. Let me search for the key related works and recent developments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "431ec141-3b36-4ddf-84f6-ff5b3bde0723",
  "isSidechain": false,
  "requestId": "req_011CbDDM5B1hyAvjzyzUSptb",
  "type": "assistant",
  "uuid": "285f1849-adde-42ff-8653-d28357636d73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yCx5L8nhdXu5BhYwnf8Y7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5427,
      "cache_read_input_tokens": 14549,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 239,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 5427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5427
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

_source line 10 · 2026-05-20T04:46:42.506Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MWSkA7NvWPBm7S5ye7eyjU`</summary>

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
  "parentUuid": "285f1849-adde-42ff-8653-d28357636d73",
  "isSidechain": false,
  "requestId": "req_011CbDDM5B1hyAvjzyzUSptb",
  "type": "assistant",
  "uuid": "35822d68-2cb2-4f89-91a6-833a73b8b173",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yCx5L8nhdXu5BhYwnf8Y7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5427,
      "cache_read_input_tokens": 14549,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 239,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 5427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5427
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

_source line 11 · 2026-05-20T04:46:42.512Z_

<details><summary>↩ Tool result · `toolu_01MWSkA7NvWPBm7S5ye7eyjU`</summary>

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
  "parentUuid": "35822d68-2cb2-4f89-91a6-833a73b8b173",
  "isSidechain": false,
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "9acc65cf-e1d9-4074-a34e-c36e6491ba08",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "35822d68-2cb2-4f89-91a6-833a73b8b173",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T04:46:44.966Z_

Now let me run multiple searches in parallel to understand the landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9acc65cf-e1d9-4074-a34e-c36e6491ba08",
  "isSidechain": false,
  "requestId": "req_011CbDDMWXzvT3TZ8DAA9VqM",
  "type": "assistant",
  "uuid": "0a5fb564-8427-4ca7-975f-59eb71b22c46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZW64rF2CnXfo61o5akbcs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 19976,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 766,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 19976,
          "cache_creation_input_tokens": 766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 766
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

_source line 13 · 2026-05-20T04:46:45.028Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HXCw9UNBsGt88GzyTvPDRj`</summary>

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
  "parentUuid": "0a5fb564-8427-4ca7-975f-59eb71b22c46",
  "isSidechain": false,
  "requestId": "req_011CbDDMWXzvT3TZ8DAA9VqM",
  "type": "assistant",
  "uuid": "4ec3e445-42d6-4fd2-ab79-379923c464e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ZW64rF2CnXfo61o5akbcs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 19976,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 766,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 19976,
          "cache_creation_input_tokens": 766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 766
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

_source line 14 · 2026-05-20T04:46:52.464Z_

<details><summary>↩ Tool result · `toolu_01HXCw9UNBsGt88GzyTvPDRj`</summary>

```text
Web search results for query: "IRT person-fit statistics LLM benchmark contamination detection 2025 2026"

Links: [{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"Contamination Report for Multilingual Benchmarks","url":"https://arxiv.org/pdf/2410.16186"},{"title":"How Can I Publish My LLM Benchmark Without Giving the True Answers Away?","url":"https://arxiv.org/pdf/2505.18102"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"Detecting Benchmark Contamination Through Watermarking","url":"https://arxiv.org/pdf/2502.17259"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark","url":"https://arxiv.org/pdf/2310.18018"},{"title":"gies for llm benchmark data contamination - Gang Wang","url":"https://gangw.cs.illinois.edu/cvpr_Emperor25.pdf"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"}]

Based on the web search results, here's what I found regarding IRT person-fit statistics and LLM benchmark contamination detection for 2025-2026:

## Key Findings on LLM Benchmark Contamination Detection (2025-2026)

Five detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.

For most of 2024 and 2025, the field had two contradictory findings - detection work showed clear contamination signal, while Bordt et al. (2025) ran controlled studies on overtrained models and found that even known test-set inclusion had little measurable effect on benchmark accuracy.

The 2026 paper "Quantifying the Effect of Test Set Contamination on Generative Evaluations" resolved this contradiction by training dozens of models and fitting a clean dose-response curve.

## Notable Recent Detection Methods

CoDeC (Contamination Detection via Context) is a practical and accurate method to detect and quantify training data contamination in large language models.

Watermarking approaches have been introduced to address benchmark contamination by watermarking benchmarks before their release.

However, I should note that the search results do not specifically mention **IRT (Item Response Theory) person-fit statistics** in the context of LLM contamination detection. The results focus on other detection methodologies but don't directly address IRT-based approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ec3e445-42d6-4fd2-ab79-379923c464e2",
  "isSidechain": false,
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "f63dea80-3643-4226-9d06-647f0fa68c40",
  "toolUseResult": {
    "query": "IRT person-fit statistics LLM benchmark contamination detection 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ht9ABtfXrfGJY37pXfbrfr",
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
            "title": "Detecting Benchmark Contamination Through Watermarking",
            "url": "https://arxiv.org/pdf/2502.17259"
          },
          {
            "title": "NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark",
            "url": "https://arxiv.org/pdf/2310.18018"
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
      "Based on the web search results, here's what I found regarding IRT person-fit statistics and LLM benchmark contamination detection for 2025-2026:\n\n## Key Findings on LLM Benchmark Contamination Detection (2025-2026)\n\nFive detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.\n\nFor most of 2024 and 2025, the field had two contradictory findings - detection work showed clear contamination signal, while Bordt et al. (2025) ran controlled studies on overtrained models and found that even known test-set inclusion had little measurable effect on benchmark accuracy.\n\nThe 2026 paper \"Quantifying the Effect of Test Set Contamination on Generative Evaluations\" resolved this contradiction by training dozens of models and fitting a clean dose-response curve.\n\n## Notable Recent Detection Methods\n\nCoDeC (Contamination Detection via Context) is a practical and accurate method to detect and quantify training data contamination in large language models.\n\nWatermarking approaches have been introduced to address benchmark contamination by watermarking benchmarks before their release.\n\nHowever, I should note that the search results do not specifically mention **IRT (Item Response Theory) person-fit statistics** in the context of LLM contamination detection. The results focus on other detection methodologies but don't directly address IRT-based approaches."
    ],
    "durationSeconds": 7.429770788,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4ec3e445-42d6-4fd2-ab79-379923c464e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:46:55.196Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BcoBKkDx2ZjLPMAtcSZwrJ`</summary>

```json
{
  "query": "PSN-IRT \"Lost in Benchmarks\" 4PL item response theory LLM evaluation AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f63dea80-3643-4226-9d06-647f0fa68c40",
  "isSidechain": false,
  "requestId": "req_011CbDDNEmzYkvvgd4BFqa7t",
  "type": "assistant",
  "uuid": "d1e5e044-07cd-4157-a9c1-5b462928b132",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJqLuQzWachQuWCtqPnbE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 20742,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 20742,
          "cache_creation_input_tokens": 814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 814
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

_source line 16 · 2026-05-20T04:47:02.248Z_

<details><summary>↩ Tool result · `toolu_01BcoBKkDx2ZjLPMAtcSZwrJ`</summary>

```text
Web search results for query: "PSN-IRT "Lost in Benchmarks" 4PL item response theory LLM evaluation AAAI 2026"

Links: [{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://chatpaper.com/paper/139423"},{"title":"[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"},{"title":"(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Paper page - Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://huggingface.co/papers/2505.15055"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://ojs.aaai.org/index.php/AAAI/article/download/40814/44775"}]

I found comprehensive information about the paper you searched for. Here's what I found:

## Overview

"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" provides a critical analysis of benchmark effectiveness, examining mainstream prominent LLM benchmarks, and proposes Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture.

## Key Details

**Framework Architecture:**
PSN-IRT consists of two independent pathways: a model network and an item network, each processing one-hot encoded identifiers of LLMs and benchmark items, respectively. The model network estimates latent ability (θ), while the item network infers four psychometric parameters: discriminability (a), difficulty (b), guessing-rate (c), and feasibility (d).

**4PL Model:**
The framework uses the Four-Parameter Logistic (4PL) model, an advanced IRT formulation that extends simpler models like the 1PL to capture nuanced behaviors. PSN-IRT performs best with 4PL configuration.

**Analysis Results:**
The analysis covers 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. Key findings show that LLM benchmarks fail to achieve simultaneous excellence across multiple measurements, suffer from widespread saturation and insufficient difficulty ceilings, and exhibit data contamination in numerous items.

**Publication:**
The paper has been accepted to AAAI 2026 as an oral presentation, with code available on GitHub at https://github.com/Joe-Hall-Lee/PSN-IRT.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1e5e044-07cd-4157-a9c1-5b462928b132",
  "isSidechain": false,
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "5c40dc89-79b3-45c9-b0ba-6a742a364b7b",
  "toolUseResult": {
    "query": "PSN-IRT \"Lost in Benchmarks\" 4PL item response theory LLM evaluation AAAI 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WfS7u2bW9yzVFvCuZxeFu6",
        "content": [
          {
            "title": "GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub",
            "url": "https://github.com/Joe-Hall-Lee/PSN-IRT"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40814"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v2"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://chatpaper.com/paper/139423"
          },
          {
            "title": "[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"
          },
          {
            "title": "(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/pdf/2505.15055"
          },
          {
            "title": "Paper page - Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://huggingface.co/papers/2505.15055"
          },
          {
            "title": "[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/abs/2505.15055"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/download/40814/44775"
          }
        ]
      },
      "I found comprehensive information about the paper you searched for. Here's what I found:\n\n## Overview\n\n\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\" provides a critical analysis of benchmark effectiveness, examining mainstream prominent LLM benchmarks, and proposes Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture.\n\n## Key Details\n\n**Framework Architecture:**\nPSN-IRT consists of two independent pathways: a model network and an item network, each processing one-hot encoded identifiers of LLMs and benchmark items, respectively. The model network estimates latent ability (θ), while the item network infers four psychometric parameters: discriminability (a), difficulty (b), guessing-rate (c), and feasibility (d).\n\n**4PL Model:**\nThe framework uses the Four-Parameter Logistic (4PL) model, an advanced IRT formulation that extends simpler models like the 1PL to capture nuanced behaviors. PSN-IRT performs best with 4PL configuration.\n\n**Analysis Results:**\nThe analysis covers 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. Key findings show that LLM benchmarks fail to achieve simultaneous excellence across multiple measurements, suffer from widespread saturation and insufficient difficulty ceilings, and exhibit data contamination in numerous items.\n\n**Publication:**\nThe paper has been accepted to AAAI 2026 as an oral presentation, with code available on GitHub at https://github.com/Joe-Hall-Lee/PSN-IRT."
    ],
    "durationSeconds": 7.047734367999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d1e5e044-07cd-4157-a9c1-5b462928b132",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T04:47:06.311Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T9sZnGyxvTe6e7jKN3iiXB`</summary>

```json
{
  "query": "Wang et al 2025 \"fragility benchmark contamination detection reasoning models\" MIA failure post-RL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c40dc89-79b3-45c9-b0ba-6a742a364b7b",
  "isSidechain": false,
  "requestId": "req_011CbDDNxeuhPS2VpiTxcqgM",
  "type": "assistant",
  "uuid": "3ca7ad49-cff4-4f3e-a62a-fd67d60929ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSwJBEYi9rgcXuGeJt5XFW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1112,
      "cache_read_input_tokens": 21556,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 21556,
          "cache_creation_input_tokens": 1112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1112
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

_source line 18 · 2026-05-20T04:47:14.258Z_

<details><summary>↩ Tool result · `toolu_01T9sZnGyxvTe6e7jKN3iiXB`</summary>

```text
Web search results for query: "Wang et al 2025 "fragility benchmark contamination detection reasoning models" MIA failure post-RL"

Links: [{"title":"[PDF] On The Fragility of Benchmark Contamination Detection in Reasoning Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-The-Fragility-of-Benchmark-Contamination-in-Wang-Li/9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/abs/2510.02386"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/html/2510.02386v1"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/pdf/2510.09259"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/html/2510.09259v1"}]

Based on the search results, I found the paper you're looking for:

## "On The Fragility of Benchmark Contamination Detection in Reasoning Models" - Wang et al., 2025

The paper by Han Wang, Haoyu Li, Brian Ko, and Huan Zhang (published on arXiv in 2025) addresses how model developers could easily contaminate Large Reasoning Models (LRMs) to achieve inflated leaderboard performance while leaving minimal traces of contamination.

### Key Findings:

The paper identifies two critical scenarios: In Stage I (pre-LRM), while SFT contamination to the base model is initially detectable, contamination evidence can be concealed through subsequent RL training. In Stage II (post-LRM), extensive contamination with CoT on advanced LRMs barely leaves evidence for existing memorization-based detection methods.

The researchers found that when a base model evolves into an LRM via SFT and RL, contamination during SFT can be originally identified by detection methods, yet even a brief GRPO training can markedly conceal contamination signals that most detection methods rely on.

### Main Vulnerabilities Revealed:

The work reveals critical vulnerabilities: RL fine-tuning can conceal benchmark contamination when base models evolve into LRMs; contamination with CoT applied to advanced LRMs leaves little evidence detectable by existing memorization-based methods.

The paper is available on arXiv (ID: 2510.02386) and was submitted on September 30, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ca7ad49-cff4-4f3e-a62a-fd67d60929ce",
  "isSidechain": false,
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "44b717f0-a933-427b-a31c-6ace29aa65b4",
  "toolUseResult": {
    "query": "Wang et al 2025 \"fragility benchmark contamination detection reasoning models\" MIA failure post-RL",
    "results": [
      {
        "tool_use_id": "srvtoolu_012D1MBsQCdUVUyXKe8qiJVR",
        "content": [
          {
            "title": "[PDF] On The Fragility of Benchmark Contamination Detection in Reasoning Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/On-The-Fragility-of-Benchmark-Contamination-in-Wang-Li/9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/abs/2510.02386"
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
      "Based on the search results, I found the paper you're looking for:\n\n## \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" - Wang et al., 2025\n\nThe paper by Han Wang, Haoyu Li, Brian Ko, and Huan Zhang (published on arXiv in 2025) addresses how model developers could easily contaminate Large Reasoning Models (LRMs) to achieve inflated leaderboard performance while leaving minimal traces of contamination.\n\n### Key Findings:\n\nThe paper identifies two critical scenarios: In Stage I (pre-LRM), while SFT contamination to the base model is initially detectable, contamination evidence can be concealed through subsequent RL training. In Stage II (post-LRM), extensive contamination with CoT on advanced LRMs barely leaves evidence for existing memorization-based detection methods.\n\nThe researchers found that when a base model evolves into an LRM via SFT and RL, contamination during SFT can be originally identified by detection methods, yet even a brief GRPO training can markedly conceal contamination signals that most detection methods rely on.\n\n### Main Vulnerabilities Revealed:\n\nThe work reveals critical vulnerabilities: RL fine-tuning can conceal benchmark contamination when base models evolve into LRMs; contamination with CoT applied to advanced LRMs leaves little evidence detectable by existing memorization-based methods.\n\nThe paper is available on arXiv (ID: 2510.02386) and was submitted on September 30, 2025."
    ],
    "durationSeconds": 7.9442903110000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3ca7ad49-cff4-4f3e-a62a-fd67d60929ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T04:47:16.298Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SbWNzvMkmm6H6C1xLf4rVS`</summary>

```json
{
  "query": "Self-Critique contamination detection post-RL \"entropy sequence\" \"policy collapse\" ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44b717f0-a933-427b-a31c-6ace29aa65b4",
  "isSidechain": false,
  "requestId": "req_011CbDDPqvdEJgG9cjjsmwPF",
  "type": "assistant",
  "uuid": "fa19a934-2062-4977-9f19-4b3cc4805fbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011KmYdhKWzjvB2uaC1TD9sJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 22668,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 22668,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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
  "lastPrompt": "# IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs  ## Description We propose IRT-FIT, the first method that transfers person-fit statistics from educational psyc…",
  "leafUuid": "fa19a934-2062-4977-9f19-4b3cc4805fbb",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Detect LLM benchmark contamination using IRT person-fit statistics",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381"
}
```

---

### Tool result

_source line 22 · 2026-05-20T04:47:23.109Z_

<details><summary>↩ Tool result · `toolu_01SbWNzvMkmm6H6C1xLf4rVS`</summary>

```text
Web search results for query: "Self-Critique contamination detection post-RL "entropy sequence" "policy collapse" ICLR 2026"

Links: [{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/pdf/2510.09259"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2603.11682"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=YlpaaYxx4t"},{"title":"Rethinking Entropy Interventions in RLVR: An Entropy Change Perspective","url":"https://arxiv.org/pdf/2510.10150"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"OBSCURING DATA CONTAMINATION THROUGH TRANSLATION","url":"https://openreview.net/pdf?id=omg9K6lI93"},{"title":"Entropy-Reservoir Bregman Projection: An Information-Geometric Unification of Model Collapse","url":"https://arxiv.org/pdf/2512.14879"}]

I found relevant research on this topic. Here are the key findings:

The Self-Critique method was proposed to detect data contamination within reinforcement learning post-training scenarios. The method is motivated by the observation that after the RL phase, LLM output entropy distribution tends to collapse into highly specific and sparse modes, and Self-Critique probes for the underlying policy collapse—the model's convergence to a narrow reasoning path—which causes this entropy reduction.

To facilitate this research, the authors also introduced RL-MIA, a benchmark constructed to simulate this specific contamination scenario. Extensive experiments show that Self-Critique significantly outperforms baseline methods across multiple models and contamination tasks, achieving an AUC improvement of up to 30%.

The search results also show complementary ICLR 2026 research on entropy in RL post-training. One work argues that entropy should be actively monitored and controlled throughout RL training, analyzing entropy preservation as a unifying lens for understanding recent algorithms and proposing explicit mechanisms for entropy control. For example, GRPO reduces entropy by nearly 90% over training, while other methods like RLOO lose considerably less.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa19a934-2062-4977-9f19-4b3cc4805fbb",
  "isSidechain": false,
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "ca3ff40c-f869-483c-b105-d2dc462770eb",
  "toolUseResult": {
    "query": "Self-Critique contamination detection post-RL \"entropy sequence\" \"policy collapse\" ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NJbpRV17YRLLdqRNxZvbcP",
        "content": [
          {
            "title": "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/pdf/2510.09259"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2603.11682"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf?id=YlpaaYxx4t"
          },
          {
            "title": "Rethinking Entropy Interventions in RLVR: An Entropy Change Perspective",
            "url": "https://arxiv.org/pdf/2510.10150"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "OBSCURING DATA CONTAMINATION THROUGH TRANSLATION",
            "url": "https://openreview.net/pdf?id=omg9K6lI93"
          },
          {
            "title": "Entropy-Reservoir Bregman Projection: An Information-Geometric Unification of Model Collapse",
            "url": "https://arxiv.org/pdf/2512.14879"
          }
        ]
      },
      "I found relevant research on this topic. Here are the key findings:\n\nThe Self-Critique method was proposed to detect data contamination within reinforcement learning post-training scenarios. The method is motivated by the observation that after the RL phase, LLM output entropy distribution tends to collapse into highly specific and sparse modes, and Self-Critique probes for the underlying policy collapse—the model's convergence to a narrow reasoning path—which causes this entropy reduction.\n\nTo facilitate this research, the authors also introduced RL-MIA, a benchmark constructed to simulate this specific contamination scenario. Extensive experiments show that Self-Critique significantly outperforms baseline methods across multiple models and contamination tasks, achieving an AUC improvement of up to 30%.\n\nThe search results also show complementary ICLR 2026 research on entropy in RL post-training. One work argues that entropy should be actively monitored and controlled throughout RL training, analyzing entropy preservation as a unifying lens for understanding recent algorithms and proposing explicit mechanisms for entropy control. For example, GRPO reduces entropy by nearly 90% over training, while other methods like RLOO lose considerably less."
    ],
    "durationSeconds": 6.807952335000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fa19a934-2062-4977-9f19-4b3cc4805fbb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T04:47:26.063Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DV5yjr9mtTRbsL2jDsnYas`</summary>

```json
{
  "query": "\"person-fit\" \"lz\" statistic LLM evaluation contamination cheating detection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca3ff40c-f869-483c-b105-d2dc462770eb",
  "isSidechain": false,
  "requestId": "req_011CbDDQVngn1H9pBjVjRdib",
  "type": "assistant",
  "uuid": "12126b29-d20c-446a-9680-3a96c37909cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rw61F4CXrzHQtuouN3A9vY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 23517,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 23517,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 24 · 2026-05-20T04:47:33.968Z_

<details><summary>↩ Tool result · `toolu_01DV5yjr9mtTRbsL2jDsnYas`</summary>

```text
Web search results for query: ""person-fit" "lz" statistic LLM evaluation contamination cheating detection 2025 2026"

Links: [{"title":"On the Performance of the lZ Person-Fit Statistic","url":"https://www.researchgate.net/publication/287008632_On_the_Performance_of_the_lZ_Person-Fit_Statistic"},{"title":"Suggestions for combining psychometric-based and supervised classification methods to detect cheating in online exams | Behaviormetrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s41237-023-00216-z"},{"title":"Evaluating LLM-Contaminated Crowdsourcing Data Without Ground Truth","url":"https://arxiv.org/pdf/2506.06991"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/pdf/2510.27055"},{"title":"Appraising Traditional and Purpose-built Person Fit Statistics’ Power to Detect Cheating","url":"https://www.ce-jeme.org/journal/vol3/iss1/3/"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"}]

Based on the search results, I found information about person-fit statistics and LLM contamination detection, though the specific combination of "person-fit" "lz" statistic with LLM evaluation appears to be an emerging intersection of research areas.

## Key Findings:

**Person-Fit Statistics (lz Statistic):**

The lz person-fit statistic is a well-established tool in educational testing. Person-fit statistics (PFSs) have been suggested as a tool to detect cheating in large-scale testing, and integrating person-fit and distribution-based methods enhances the reliability of cheating detection in unsupervised testing environments.

**LLM Data Contamination Detection (2025-2026):**

Recent research has focused on detecting data contamination in LLM evaluations. Detecting contamination is essential for the integrity of LLM evaluation. Several approaches have emerged:

- CoDeC produces interpretable contamination scores that clearly separate seen and unseen datasets, and the method is simple, automated, and both model- and dataset-agnostic.

- The 2026 paper "Quantifying the Effect of Test Set Contamination on Generative Evaluations" trained dozens of models on Qwen 3 architectures from 34M to 344M parameters, sweeping the number of test set replicas in the pretraining corpus.

- PaCoST (Paired Confidence Significance Testing) was proposed to detect benchmark contamination in LLMs, addressing how data from benchmarks can lead to cheatingly high scores on model leaderboards.

However, the search results don't show direct application of the lz person-fit statistic specifically to LLM contamination detection as of 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12126b29-d20c-446a-9680-3a96c37909cd",
  "isSidechain": false,
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "2ec8c649-8959-4eeb-b1ea-49f5e3e70bb8",
  "toolUseResult": {
    "query": "\"person-fit\" \"lz\" statistic LLM evaluation contamination cheating detection 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U7qQMauaXs97v7NYzY1x6D",
        "content": [
          {
            "title": "On the Performance of the lZ Person-Fit Statistic",
            "url": "https://www.researchgate.net/publication/287008632_On_the_Performance_of_the_lZ_Person-Fit_Statistic"
          },
          {
            "title": "Suggestions for combining psychometric-based and supervised classification methods to detect cheating in online exams | Behaviormetrika | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s41237-023-00216-z"
          },
          {
            "title": "Evaluating LLM-Contaminated Crowdsourcing Data Without Ground Truth",
            "url": "https://arxiv.org/pdf/2506.06991"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/pdf/2510.27055"
          },
          {
            "title": "Appraising Traditional and Purpose-built Person Fit Statistics’ Power to Detect Cheating",
            "url": "https://www.ce-jeme.org/journal/vol3/iss1/3/"
          },
          {
            "title": "What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide",
            "url": "https://llm-stats.com/blog/research/what-is-a-contaminated-llm"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          }
        ]
      },
      "Based on the search results, I found information about person-fit statistics and LLM contamination detection, though the specific combination of \"person-fit\" \"lz\" statistic with LLM evaluation appears to be an emerging intersection of research areas.\n\n## Key Findings:\n\n**Person-Fit Statistics (lz Statistic):**\n\nThe lz person-fit statistic is a well-established tool in educational testing. Person-fit statistics (PFSs) have been suggested as a tool to detect cheating in large-scale testing, and integrating person-fit and distribution-based methods enhances the reliability of cheating detection in unsupervised testing environments.\n\n**LLM Data Contamination Detection (2025-2026):**\n\nRecent research has focused on detecting data contamination in LLM evaluations. Detecting contamination is essential for the integrity of LLM evaluation. Several approaches have emerged:\n\n- CoDeC produces interpretable contamination scores that clearly separate seen and unseen datasets, and the method is simple, automated, and both model- and dataset-agnostic.\n\n- The 2026 paper \"Quantifying the Effect of Test Set Contamination on Generative Evaluations\" trained dozens of models on Qwen 3 architectures from 34M to 344M parameters, sweeping the number of test set replicas in the pretraining corpus.\n\n- PaCoST (Paired Confidence Significance Testing) was proposed to detect benchmark contamination in LLMs, addressing how data from benchmarks can lead to cheatingly high scores on model leaderboards.\n\nHowever, the search results don't show direct application of the lz person-fit statistic specifically to LLM contamination detection as of 2025-2026."
    ],
    "durationSeconds": 7.901007597000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "12126b29-d20c-446a-9680-3a96c37909cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T04:47:35.960Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J2HjbPn28Eg16dS45YA7E2`</summary>

```json
{
  "query": "CoDeC \"in-context learning\" contamination detection ICLR 2026 method details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ec8c649-8959-4eeb-b1ea-49f5e3e70bb8",
  "isSidechain": false,
  "requestId": "req_011CbDDRJEggzoFdnnsYo3cx",
  "type": "assistant",
  "uuid": "9ae8ee62-0631-403e-a6bf-b3af3994fca9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U6oj4kczX7ZsDXVoiSYYTc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 24193,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 24193,
          "cache_creation_input_tokens": 894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 894
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

_source line 26 · 2026-05-20T04:47:41.733Z_

<details><summary>↩ Tool result · `toolu_01J2HjbPn28Eg16dS45YA7E2`</summary>

```text
Web search results for query: "CoDeC "in-context learning" contamination detection ICLR 2026 method details"

Links: [{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/pdf/2510.27055"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/html/2510.27055v1"},{"title":"[2510.27055] Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/abs/2510.27055"},{"title":"Detecting Data Contamination in LLMs via In-Context ...","url":"https://openreview.net/pdf?id=YlpaaYxx4t"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning | OpenReview","url":"https://openreview.net/forum?id=YlpaaYxx4t"}]

Based on the search results, here's what I found about CoDeC:

## Overview
CoDeC (Contamination Detection via Context) is a practical and accurate method to detect and quantify training data contamination in large language models.

## Core Method
CoDeC distinguishes between data memorized during training and data outside the training distribution by measuring how in-context learning affects model performance. The method builds on the observation that context sampled from a dataset seen during training provides no new information to the model, while unseen data can improve predictions, with the percentage of samples in a dataset for which added context reduces confidence quantifying contamination.

## Key Findings
In-context examples typically boost confidence for unseen datasets but may reduce it when the dataset was part of training, due to disrupted memorization patterns.

## Advantages
CoDeC produces interpretable contamination scores that clearly separate seen and unseen datasets, and reveals strong evidence of memorization in open-weight models with undisclosed training corpora. The method is simple, automated, and both model- and dataset-agnostic, making it easy to integrate with benchmark evaluations.

## Technical Requirements
CoDeC requires only gray-box access to token probabilities, works with any dataset, and needs no prior knowledge of the model's training corpus.

The paper appears to be a recent submission to ICLR 2026 (posted on arXiv in October 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ae8ee62-0631-403e-a6bf-b3af3994fca9",
  "isSidechain": false,
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "45cc1cbd-e8b9-440d-87da-59d0b487c903",
  "toolUseResult": {
    "query": "CoDeC \"in-context learning\" contamination detection ICLR 2026 method details",
    "results": [
      {
        "tool_use_id": "srvtoolu_019E2GNTuYzmHfc8Xvv9jtAE",
        "content": [
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/pdf/2510.27055"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/html/2510.27055v1"
          },
          {
            "title": "[2510.27055] Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/abs/2510.27055"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context ...",
            "url": "https://openreview.net/pdf?id=YlpaaYxx4t"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning | OpenReview",
            "url": "https://openreview.net/forum?id=YlpaaYxx4t"
          }
        ]
      },
      "Based on the search results, here's what I found about CoDeC:\n\n## Overview\nCoDeC (Contamination Detection via Context) is a practical and accurate method to detect and quantify training data contamination in large language models.\n\n## Core Method\nCoDeC distinguishes between data memorized during training and data outside the training distribution by measuring how in-context learning affects model performance. The method builds on the observation that context sampled from a dataset seen during training provides no new information to the model, while unseen data can improve predictions, with the percentage of samples in a dataset for which added context reduces confidence quantifying contamination.\n\n## Key Findings\nIn-context examples typically boost confidence for unseen datasets but may reduce it when the dataset was part of training, due to disrupted memorization patterns.\n\n## Advantages\nCoDeC produces interpretable contamination scores that clearly separate seen and unseen datasets, and reveals strong evidence of memorization in open-weight models with undisclosed training corpora. The method is simple, automated, and both model- and dataset-agnostic, making it easy to integrate with benchmark evaluations.\n\n## Technical Requirements\nCoDeC requires only gray-box access to token probabilities, works with any dataset, and needs no prior knowledge of the model's training corpus.\n\nThe paper appears to be a recent submission to ICLR 2026 (posted on arXiv in October 2025)."
    ],
    "durationSeconds": 5.766957490000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9ae8ee62-0631-403e-a6bf-b3af3994fca9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T04:47:44.058Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Je3qgQtSdhErFh4PppvPB5`</summary>

```json
{
  "query": "\"Silicon Bureaucracy\" contamination perturbation sensitivity arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45cc1cbd-e8b9-440d-87da-59d0b487c903",
  "isSidechain": false,
  "requestId": "req_011CbDDRsRU6w1Yunhv45TY7",
  "type": "assistant",
  "uuid": "a3064201-1fd1-4de8-a769-58a795dfc557",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JJ9eo4bDx1NmuTmqUfZ4Lu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 25087,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 25087,
          "cache_creation_input_tokens": 656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 656
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

_source line 28 · 2026-05-20T04:47:51.688Z_

<details><summary>↩ Tool result · `toolu_01Je3qgQtSdhErFh4PppvPB5`</summary>

```text
Web search results for query: ""Silicon Bureaucracy" contamination perturbation sensitivity arXiv 2603"

Links: [{"title":"[2603.21636] Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/abs/2603.21636"},{"title":"Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks","url":"https://arxiv.org/html/2603.21636"},{"title":"Can AI Scientist Agents Learn from Lab-in-the-Loop Feedback? Evidence from Iterative Perturbation Discovery","url":"https://arxiv.org/html/2603.26177"},{"title":"Influence of water contamination on the sputtering of silicon with low-energy argon ions investigated by molecular dynamics simulations","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9520830/"},{"title":"Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis","url":"https://arxiv.org/html/2603.21454v1"},{"title":"SENSITIVITY ANALYSIS USING PERTURBED-LAW ...","url":"https://arxiv.org/pdf/1707.01296"},{"title":"Single-photon emitters and spin-photon interfaces in silicon","url":"https://arxiv.org/html/2603.02201v1"},{"title":"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity","url":"https://arxiv.org/pdf/2603.13285"},{"title":"Correctness Attraction: A Study of Stability of Software Behavior Under   Runtime Perturbation","url":"https://arxiv.org/pdf/1611.09187"}]

Based on the search results, I found the paper you're looking for:

**Title:** Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks

**ArXiv ID:** 2603.21636

**Summary:**
Public benchmarks increasingly govern how large language models (LLMs) are ranked, selected, and deployed, framed as "Silicon Bureaucracy and AI Test-Oriented Education," and this regime rests on a fragile assumption: that benchmark scores directly reflect genuine generalization. In practice, such scores may conflate exam-oriented competence with principled capability, especially when contamination and semantic leakage are difficult to exclude from modern training pipelines.

**Methodology:**
The paper proposes an audit framework for analyzing contamination sensitivity and score confidence in LLM benchmarks, using a router-worker setup to compare a clean-control condition with noisy conditions in which benchmark problems are systematically deleted, rewritten, and perturbed before being passed downstream.

The paper was published on March 23, 2026, and is available at https://arxiv.org/abs/2603.21636.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3064201-1fd1-4de8-a769-58a795dfc557",
  "isSidechain": false,
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "0bbbfd65-86d5-4b90-9caf-e498f1930cff",
  "toolUseResult": {
    "query": "\"Silicon Bureaucracy\" contamination perturbation sensitivity arXiv 2603",
    "results": [
      {
        "tool_use_id": "srvtoolu_013MNZQJn7FEeKViL7GdKUYd",
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
            "title": "Can AI Scientist Agents Learn from Lab-in-the-Loop Feedback? Evidence from Iterative Perturbation Discovery",
            "url": "https://arxiv.org/html/2603.26177"
          },
          {
            "title": "Influence of water contamination on the sputtering of silicon with low-energy argon ions investigated by molecular dynamics simulations",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9520830/"
          },
          {
            "title": "Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis",
            "url": "https://arxiv.org/html/2603.21454v1"
          },
          {
            "title": "SENSITIVITY ANALYSIS USING PERTURBED-LAW ...",
            "url": "https://arxiv.org/pdf/1707.01296"
          },
          {
            "title": "Single-photon emitters and spin-photon interfaces in silicon",
            "url": "https://arxiv.org/html/2603.02201v1"
          },
          {
            "title": "Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity",
            "url": "https://arxiv.org/pdf/2603.13285"
          },
          {
            "title": "Correctness Attraction: A Study of Stability of Software Behavior Under   Runtime Perturbation",
            "url": "https://arxiv.org/pdf/1611.09187"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks\n\n**ArXiv ID:** 2603.21636\n\n**Summary:**\nPublic benchmarks increasingly govern how large language models (LLMs) are ranked, selected, and deployed, framed as \"Silicon Bureaucracy and AI Test-Oriented Education,\" and this regime rests on a fragile assumption: that benchmark scores directly reflect genuine generalization. In practice, such scores may conflate exam-oriented competence with principled capability, especially when contamination and semantic leakage are difficult to exclude from modern training pipelines.\n\n**Methodology:**\nThe paper proposes an audit framework for analyzing contamination sensitivity and score confidence in LLM benchmarks, using a router-worker setup to compare a clean-control condition with noisy conditions in which benchmark problems are systematically deleted, rewritten, and perturbed before being passed downstream.\n\nThe paper was published on March 23, 2026, and is available at https://arxiv.org/abs/2603.21636."
    ],
    "durationSeconds": 7.6250963009999975,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a3064201-1fd1-4de8-a769-58a795dfc557",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T04:47:51.694Z_

```json
{
  "parentUuid": "0bbbfd65-86d5-4b90-9caf-e498f1930cff",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0c43aefd-5db9-444d-ae45-728acfb72cdc",
  "timestamp": "2026-05-20T04:47:51.694Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T04:47:56.441Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MsDsbtVLASCJuuss4TvuAn`</summary>

```json
{
  "query": "IRT item response theory LLM evaluation aberrant response pattern black-box 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c43aefd-5db9-444d-ae45-728acfb72cdc",
  "isSidechain": false,
  "requestId": "req_011CbDDSc2ngBDpb7BwnMHJb",
  "type": "assistant",
  "uuid": "a51e674a-fd14-4644-9484-6e613a873648",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kog1ZS5jn6njfUP64RkMyJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 25743,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 25743,
          "cache_creation_input_tokens": 905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 905
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

_source line 31 · 2026-05-20T04:48:14.648Z_

<details><summary>↩ Tool result · `toolu_01MsDsbtVLASCJuuss4TvuAn`</summary>

```text
Web search results for query: "IRT item response theory LLM evaluation aberrant response pattern black-box 2025 2026 arXiv"

Links: [{"title":"[2605.00238] Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory","url":"https://arxiv.org/abs/2605.00238"},{"title":"Correcting Human Labels for Rater Effects in AI Evaluation: An Item Response Theory Approach","url":"https://arxiv.org/html/2602.22585"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/pdf/2602.00521"},{"title":"A Short Note on Aberrant Responses Bias in Item Response Theory","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6365413/"},{"title":"[2510.00844] Learning Compact Representations of LLM Abilities via Item Response Theory","url":"https://arxiv.org/abs/2510.00844"},{"title":"[2512.07019] Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length","url":"https://arxiv.org/abs/2512.07019"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"}]

Based on the search results, here are the key findings related to IRT (Item Response Theory) and LLM evaluation:

## Recent IRT-Based LLM Evaluation Research (2025-2026)

Several recent papers on arXiv have explored the intersection of Item Response Theory and LLM evaluation:

1. **Grading Ability and Response Difficulty**: An evaluation framework for LLM-based automated short answer grading based on item response theory models grading correctness as a function of latent grader ability and response grading difficulty. This formulation enables response-level analysis of where LLM graders succeed or fail and reveals robustness differences that are not visible from aggregate scores alone.

2. **LLM Judge Reliability**: Item Response Theory is leveraged as a measurement framework to analyze latent traits from observed responses to examine LLM judging behavior. The framework examines intrinsic consistency by applying prompt perturbations and evaluates human alignment by comparing latent evaluation signals inferred from LLM judges with those of human annotators.

3. **Rater Effects Correction**: Item response theory can be used to adjust for rater aberrance after-the-fact via psychometric modeling.

4. **Model Ability Representations**: IRT models the probability of correct answers as a function of the model's multi-skill ability vector, the query's discrimination vector that separates models of differing skills, and the query's difficulty scalar.

5. **Benchmark Analysis**: Pseudo-Siamese Network for Item Response Theory incorporates a rich set of item parameters within an IRT-grounded architecture for accurate estimations of item characteristics and model abilities.

Regarding **aberrant response patterns**, the search results reference the concept in the context of traditional IRT theory, but the specific recent research on black-box LLM detection of aberrant patterns appears limited in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a51e674a-fd14-4644-9484-6e613a873648",
  "isSidechain": false,
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "62d78d94-00cc-4336-983d-d5cc293f6472",
  "toolUseResult": {
    "query": "IRT item response theory LLM evaluation aberrant response pattern black-box 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_017ExifX1gVjhzBN5iohNh8N",
        "content": [
          {
            "title": "[2605.00238] Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory",
            "url": "https://arxiv.org/abs/2605.00238"
          },
          {
            "title": "Correcting Human Labels for Rater Effects in AI Evaluation: An Item Response Theory Approach",
            "url": "https://arxiv.org/html/2602.22585"
          },
          {
            "title": "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory",
            "url": "https://arxiv.org/pdf/2602.00521"
          },
          {
            "title": "A Short Note on Aberrant Responses Bias in Item Response Theory",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6365413/"
          },
          {
            "title": "[2510.00844] Learning Compact Representations of LLM Abilities via Item Response Theory",
            "url": "https://arxiv.org/abs/2510.00844"
          },
          {
            "title": "[2512.07019] Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length",
            "url": "https://arxiv.org/abs/2512.07019"
          },
          {
            "title": "[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/abs/2505.15055"
          }
        ]
      },
      "Based on the search results, here are the key findings related to IRT (Item Response Theory) and LLM evaluation:\n\n## Recent IRT-Based LLM Evaluation Research (2025-2026)\n\nSeveral recent papers on arXiv have explored the intersection of Item Response Theory and LLM evaluation:\n\n1. **Grading Ability and Response Difficulty**: An evaluation framework for LLM-based automated short answer grading based on item response theory models grading correctness as a function of latent grader ability and response grading difficulty. This formulation enables response-level analysis of where LLM graders succeed or fail and reveals robustness differences that are not visible from aggregate scores alone.\n\n2. **LLM Judge Reliability**: Item Response Theory is leveraged as a measurement framework to analyze latent traits from observed responses to examine LLM judging behavior. The framework examines intrinsic consistency by applying prompt perturbations and evaluates human alignment by comparing latent evaluation signals inferred from LLM judges with those of human annotators.\n\n3. **Rater Effects Correction**: Item response theory can be used to adjust for rater aberrance after-the-fact via psychometric modeling.\n\n4. **Model Ability Representations**: IRT models the probability of correct answers as a function of the model's multi-skill ability vector, the query's discrimination vector that separates models of differing skills, and the query's difficulty scalar.\n\n5. **Benchmark Analysis**: Pseudo-Siamese Network for Item Response Theory incorporates a rich set of item parameters within an IRT-grounded architecture for accurate estimations of item characteristics and model abilities.\n\nRegarding **aberrant response patterns**, the search results reference the concept in the context of traditional IRT theory, but the specific recent research on black-box LLM detection of aberrant patterns appears limited in these results."
    ],
    "durationSeconds": 18.2010791,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a51e674a-fd14-4644-9484-6e613a873648",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs  ## Description We propose IRT-FIT, the first method that transfers person-fit statistics from educational psyc…",
  "leafUuid": "62d78d94-00cc-4336-983d-d5cc293f6472",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Detect LLM benchmark contamination using IRT person-fit statistics",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381"
}
```

---

### Tool call

_source line 34 · 2026-05-20T04:48:16.794Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EGqopUSNx1xUmwkpyd1Twa`</summary>

```json
{
  "query": "\"Cross-Context Verification\" benchmark contamination \"session-isolated\" arXiv 2603.21454"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62d78d94-00cc-4336-983d-d5cc293f6472",
  "isSidechain": false,
  "requestId": "req_011CbDDUJ9K8iT8X7xuv77oG",
  "type": "assistant",
  "uuid": "05816c39-7fa2-4ecb-9352-af1c3159b35c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0114mNqZEAeryyc3EcZRVbgt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 893,
      "cache_read_input_tokens": 26648,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 893,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 26648,
          "cache_creation_input_tokens": 893,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 893
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

_source line 35 · 2026-05-20T04:48:30.821Z_

<details><summary>↩ Tool result · `toolu_01EGqopUSNx1xUmwkpyd1Twa`</summary>

```text
Web search results for query: ""Cross-Context Verification" benchmark contamination "session-isolated" arXiv 2603.21454"

Links: [{"title":"[2603.21454] Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis","url":"https://arxiv.org/abs/2603.21454"},{"title":"Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis","url":"https://arxiv.org/html/2603.21454v1"},{"title":"Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis","url":"https://arxiv.org/pdf/2603.21454"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/pdf/2510.27055"},{"title":"Data Contamination Can Cross Language Barriers","url":"https://arxiv.org/pdf/2406.13236"}]

Based on the search results, I found the paper you're looking for:

Cross-Context Verification (CCV) is a black-box method that solves the same benchmark problem in N independent sessions and measures solution diversity, combined with the Hierarchical Cross-Context Architecture (HCCA), a multi-agent analysis framework that prevents confirmation bias through intentional information restriction across specialized analytical roles.

The paper addresses a credibility crisis in LLM coding benchmarks due to widespread solution leakage and test quality issues that undermine SWE-bench Verified, noting that existing detection methods—paraphrase consistency, n-gram overlap, perplexity analysis—never directly observe whether a model reasons or recalls.

On 9 SWE-bench Verified problems (45 trials, Claude Opus 4.6, temperature 0), CCV achieves perfect separation between contaminated and genuine reasoning. Key findings include that contamination is binary (models either recall perfectly or not at all), reasoning absence is a perfect discriminator, and 33% of prior contamination labels are false positives.

The paper was authored by Tae-Eun Song and submitted to arXiv on March 23, 2026, with a revised version on April 1, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05816c39-7fa2-4ecb-9352-af1c3159b35c",
  "isSidechain": false,
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "f6d0b848-f89c-4bdf-af37-3743b7365ce7",
  "toolUseResult": {
    "query": "\"Cross-Context Verification\" benchmark contamination \"session-isolated\" arXiv 2603.21454",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NywR7ohuJ9atuALzLvox3h",
        "content": [
          {
            "title": "[2603.21454] Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis",
            "url": "https://arxiv.org/abs/2603.21454"
          },
          {
            "title": "Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis",
            "url": "https://arxiv.org/html/2603.21454v1"
          },
          {
            "title": "Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis",
            "url": "https://arxiv.org/pdf/2603.21454"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/pdf/2510.27055"
          },
          {
            "title": "Data Contamination Can Cross Language Barriers",
            "url": "https://arxiv.org/pdf/2406.13236"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nCross-Context Verification (CCV) is a black-box method that solves the same benchmark problem in N independent sessions and measures solution diversity, combined with the Hierarchical Cross-Context Architecture (HCCA), a multi-agent analysis framework that prevents confirmation bias through intentional information restriction across specialized analytical roles.\n\nThe paper addresses a credibility crisis in LLM coding benchmarks due to widespread solution leakage and test quality issues that undermine SWE-bench Verified, noting that existing detection methods—paraphrase consistency, n-gram overlap, perplexity analysis—never directly observe whether a model reasons or recalls.\n\nOn 9 SWE-bench Verified problems (45 trials, Claude Opus 4.6, temperature 0), CCV achieves perfect separation between contaminated and genuine reasoning. Key findings include that contamination is binary (models either recall perfectly or not at all), reasoning absence is a perfect discriminator, and 33% of prior contamination labels are false positives.\n\nThe paper was authored by Tae-Eun Song and submitted to arXiv on March 23, 2026, with a revised version on April 1, 2026."
    ],
    "durationSeconds": 14.022658943999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "05816c39-7fa2-4ecb-9352-af1c3159b35c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T04:48:33.569Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KcWYzEsoEJF5vQGpySFtht`</summary>

```json
{
  "query": "Han et al EACL 2026 \"psychometric\" \"personality\" LLM contamination quantifying"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6d0b848-f89c-4bdf-af37-3743b7365ce7",
  "isSidechain": false,
  "requestId": "req_011CbDDVVFqFvNBJoXqScWpo",
  "type": "assistant",
  "uuid": "b5522f49-b9b7-4091-a7cc-b46d2f5e6e47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014FBRTo8BbeHiWhRyG61SnX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 27541,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 626,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 27541,
          "cache_creation_input_tokens": 626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 626
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

_source line 37 · 2026-05-20T04:48:40.848Z_

<details><summary>↩ Tool result · `toolu_01KcWYzEsoEJF5vQGpySFtht`</summary>

```text
Web search results for query: "Han et al EACL 2026 "psychometric" "personality" LLM contamination quantifying"

Links: [{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.319/"},{"title":"Human Psychometric Questionnaires Mischaracterize LLM Psychology: Evidence from Generation Behavior","url":"https://arxiv.org/html/2509.10078"},{"title":"LLM Psychometric Personality Assessment","url":"https://www.emergentmind.com/topics/psychometric-personality-assessment-in-llms"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/html/2510.07175v2"},{"title":"[2510.07175] Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/abs/2510.07175"},{"title":"Quantifying Data Contamination in Psychometric ...","url":"https://aclanthology.org/2026.findings-eacl.319.pdf"}]

I found the paper! Here are the search results for the Han et al. EACL 2026 paper on quantifying data contamination in psychometric evaluations of LLMs:

**Paper Details:**

Jongwook Han, Woojung Song, Jonggeun Lee, and Yohan Jo published "Quantifying Data Contamination in Psychometric Evaluations of LLMs" in Findings of the Association for Computational Linguistics: EACL 2026, pages 6070–6088, Rabat, Morocco.

**Key Contributions:**

The paper addresses recent studies that apply psychometric questionnaires to Large Language Models (LLMs) to assess high-level psychological constructs such as values, personality, moral foundations, and dark traits.

Although prior work has raised concerns about possible data contamination from psychometric inventories, which may threaten the reliability of such evaluations, the authors propose a framework to systematically measure data contamination in psychometric evaluations of LLMs, evaluating three aspects: (1) item memorization, (2) evaluation memorization, and (3) target score matching.

**Key Findings:**

Applying this framework to 21 models from major families and four widely used psychometric inventories, the authors provide evidence that popular inventories such as the Big Five Inventory (BFI-44) and Portrait Values Questionnaire (PVQ-40) exhibit strong contamination, where models not only memorize items but can also adjust their responses to achieve specific target scores.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5522f49-b9b7-4091-a7cc-b46d2f5e6e47",
  "isSidechain": false,
  "promptId": "3c1d9893-b55e-49e1-b616-e480fa0f3d16",
  "type": "user",
  "uuid": "19458715-13ed-4579-acc0-3fe7b4d904c4",
  "toolUseResult": {
    "query": "Han et al EACL 2026 \"psychometric\" \"personality\" LLM contamination quantifying",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DVsQCH2RFWaofxdZCWzVTi",
        "content": [
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2026.findings-eacl.319/"
          },
          {
            "title": "Human Psychometric Questionnaires Mischaracterize LLM Psychology: Evidence from Generation Behavior",
            "url": "https://arxiv.org/html/2509.10078"
          },
          {
            "title": "LLM Psychometric Personality Assessment",
            "url": "https://www.emergentmind.com/topics/psychometric-personality-assessment-in-llms"
          },
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/pdf/2510.07175"
          },
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/html/2510.07175v2"
          },
          {
            "title": "[2510.07175] Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/abs/2510.07175"
          },
          {
            "title": "Quantifying Data Contamination in Psychometric ...",
            "url": "https://aclanthology.org/2026.findings-eacl.319.pdf"
          }
        ]
      },
      "I found the paper! Here are the search results for the Han et al. EACL 2026 paper on quantifying data contamination in psychometric evaluations of LLMs:\n\n**Paper Details:**\n\nJongwook Han, Woojung Song, Jonggeun Lee, and Yohan Jo published \"Quantifying Data Contamination in Psychometric Evaluations of LLMs\" in Findings of the Association for Computational Linguistics: EACL 2026, pages 6070–6088, Rabat, Morocco.\n\n**Key Contributions:**\n\nThe paper addresses recent studies that apply psychometric questionnaires to Large Language Models (LLMs) to assess high-level psychological constructs such as values, personality, moral foundations, and dark traits.\n\nAlthough prior work has raised concerns about possible data contamination from psychometric inventories, which may threaten the reliability of such evaluations, the authors propose a framework to systematically measure data contamination in psychometric evaluations of LLMs, evaluating three aspects: (1) item memorization, (2) evaluation memorization, and (3) target score matching.\n\n**Key Findings:**\n\nApplying this framework to 21 models from major families and four widely used psychometric inventories, the authors provide evidence that popular inventories such as the Big Five Inventory (BFI-44) and Portrait Values Questionnaire (PVQ-40) exhibit strong contamination, where models not only memorize items but can also adjust their responses to achieve specific target scores."
    ],
    "durationSeconds": 7.273320665000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b5522f49-b9b7-4091-a7cc-b46d2f5e6e47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T04:49:52.330Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the landscape. Let me synthesize my findings and evaluate this proposal.

Key observations from my research:

1. **PSN-IRT (AAAI 2026 Oral)** is real and provides the 4PL calibrated item parameters across 41,871 items and 11 benchmarks. This infrastructure is publicly available.

2. **The gap is real**: No existing work connects IRT person-fit statistics (lz*, infit, outfit) to LLM benchmark contamination detection. The analogy to educational cheating detection is well-motivated.


3. Wang et al. (2025) shows that MIA-based detection breaks down after post-RL contamination, which is a genuine problem in the field. Self-Critique from ICLR 2026 tackles this with entropy sequences and achieves meaningful improvements, making it a strong competitor for post-RL detection. CoDeC also addresses this space but requires token-level access, whereas the IRT approach would work entirely black-box. The most recent work like Silicon Bureaucracy and Cross-Context Verification are still emerging.

7. Han et al. (EACL 2026) explores psychometric contamination but doesn't leverage person-fit statistics the way this proposal does. Looking at the strengths here: the core insight of borrowing person-fit detection from educational testing is genuinely novel and well-motivated—contaminated models behave like test-takers with item preknowledge. The timing works because PSN-IRT's calibrated parameters are now available, and the fully black-box nature is a real advantage. The honest framing around detection limits—acknowledging that complete contamination is undetectable and there's a detection power curve—shows thoughtful consideration of the method's boundaries.

But I should push back on whether person-fit statistics are actually necessary here. Could a much simpler approach work just as well—like checking whether a model gets disproportionately many hard items correct relative to easy ones, or computing Guttman error counts? The mathematical sophistication of lz* and similar statistics is appealing, but the underlying signal might be capturable through cruder difficulty-based comparisons without needing full IRT calibration.

That said, the IRT framework does offer real advantages: it accounts for the full item characteristic curve including discrimination and guessing parameters, has established null distributions for proper statistical testing, and the 4PL model specifically handles ambiguity and false positives better than simple heuristics. So while a trivial alternative exists in principle, there's genuine statistical rigor in the IRT approach that justifies the added complexity.

Now I'm questioning whether the core analogy even holds—does contamination in an LLM actually manifest like cheating on an exam? The assumption is that a partially contaminated model would show aberrant patterns (correct on memorized hard items, normal elsewhere), but pretraining contamination might not work that way at all.

Pretraining on benchmark data likely improves general performance on similar items rather than memorizing specific answers, and the "item preknowledge" analogy really only applies cleanly to SFT contamination where exact Q-A pairs are memorized. The proposal handles this by using controlled SFT-based contamination, which is the right move. The unidimensionality assumption is also well-addressed through per-benchmark computation, exploratory factor analysis screening, and multiscale aggregation. But I need to examine the "fully black-box" claim more carefully—the method requires calibrated 4PL parameters from PSN-IRT, and I'm not sure how those were originally established.

There's a potential circularity issue here: if the target model was part of PSN-IRT's calibration sample, that's problematic. Though one additional model shouldn't dominate the collective response patterns, there's a deeper concern—if many of the models used in PSN-IRT's calibration were already contaminated on certain items, the difficulty parameters for those items would be artificially deflated, making them appear easier than they actually are. This would then undermine the person-fit detection, since contaminated items wouldn't stand out as surprisingly difficult anymore. It's a legitimate concern, though the severity depends on how widespread contamination was in the original calibration sample.

The controlled fine-tuning experiment with known contamination status helps sidestep this issue entirely. The post-RL hypothesis is compelling—if person-fit statistics maintain their power after reinforcement learning, that's a major strength for the approach, and framing it as a genuine hypothesis test rather than an assumption is the right move.

The core idea is genuinely novel and well-timed given PSN-IRT's recent availability. The cross-domain transfer aspect is non-trivial. I'm thinking about what could strengthen the proposal further, particularly around sharpening the "black-box advantage" narrative and how it positions this work relative to existing contamination detection methods like CoDeC and Self-Critique.

The real differentiator here is that IRT-FIT operates on just binary correct/incorrect patterns—the absolute minimum information needed—whereas those baselines require token probabilities or gray-box access that API-only models like GPT-4 or Claude can't provide. That's the central selling point and should be emphasized more prominently. Beyond contamination detection, this also addresses a governance problem: as benchmarks increasingly influence funding and regulatory decisions, the ability to audit scores without any model cooperation becomes critical infrastructure. I should also check how this relates to Silicon Bureaucracy, which uses perturbation-based auditing for similar credibility assessment purposes. but requires the ability to modify and re-administer test items. IRT-FIT works on existing response data without re-testing. This distinction should be made explicit.

4. **The inverted-U curve as a contribution in its own right**: The characterization of the detection power curve (inverted-U, peak at 10-30%, zero at 100%) is itself a conceptual contribution. It provides a framework for understanding the fundamental limits of ANY response-pattern-based detection method. This could be elevated to a standalone contribution rather than just a property of the method.

Actually, let me reconsider. The proposal is already quite mature and well-articulated. Most of the points I'm thinking of are already somewhat addressed. Let me focus on what genuinely could raise the ceiling.

The strongest point I see is the information-theoretic minimality argument: since IRT-FIT only needs binary response patterns without logits, token probabilities, training data, or re-testing capabilities, it operates at the absolute minimal information threshold for detecting contamination. This frames the work not just as a working method but as establishing a new point on the fundamental tradeoff frontier between information access and detection power, which connects to deeper questions about the information-theoretic lower bounds for this problem.

Beyond that, there's real value in emphasizing the deployability angle—because the method only requires binary response data, it can be applied retroactively to any existing benchmark evaluations without needing to re-run anything.

The core assumptions hold up well when contamination is partial and the model's true ability differs measurably from its contaminated performance, though the method could struggle if contamination generalizes beyond exact memorization or if the model is sufficiently capable that it performs well regardless.

The proposal handles these edge cases through the inverted-U curve analysis and the 4PL feasibility parameter, and the controlled fine-tuning setup partially addresses generalization concerns. The work is solid and novel, with the main opportunities being to refine the information-theoretic framing, highlight that it works retroactively on existing leaderboards, and elevate the inverted-U power curve as its own conceptual insight.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19458715-13ed-4579-acc0-3fe7b4d904c4",
  "isSidechain": false,
  "requestId": "req_011CbDDWEA1VaagKBq3dkSYE",
  "type": "assistant",
  "uuid": "a3c66d03-f3c7-4894-8f12-662412bfb9c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBcyhEnBLnKEiqYVmPfLXj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 28167,
      "output_tokens": 6591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6591,
          "cache_read_input_tokens": 28167,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 790
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

_source line 39 · 2026-05-20T04:51:18.592Z_

Now I have enough research to provide a thorough assessment. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- **PSN-IRT / "Lost in Benchmarks?" (AAAI 2026 Oral, arXiv 2505.15055)**: 确认公开了 4PL 参数（a, b, c, d）涵盖 41,871 items × 11 benchmarks，GitHub 代码可用。该工作聚焦 measurement quality（item 层面的 discrimination/difficulty 分析），未涉及 person-fit 统计量，也未连接到 contamination detection。IRT-FIT 提出的 person-fit 应用与 PSN-IRT 的 item-level 分析正交。
- **Wang et al., "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (arXiv 2510.02386, 2025)**: 确认了两阶段脆弱性：(1) SFT contamination 被 RL 后训练掩盖；(2) 直接对 LRM 的 CoT contamination 对现有 memorization-based 方法近乎不可见。核心发现：即使短暂的 GRPO 训练就能显著消除 MIA 检测信号。
- **Self-Critique (arXiv 2510.09259, ICLR 2026)**: 检测 post-RL contamination 的 entropy-sequence policy collapse 方法，AUC 提升 ~30%。但仍需 **token-level probability access**（gray-box），不是纯 black-box。
- **CoDeC (arXiv 2510.27055, ICLR 2026)**: 通过 in-context learning 对比 seen/unseen data 的 confidence 变化检测 contamination，需要 **token probability access**（gray-box）。
- **Silicon Bureaucracy (arXiv 2603.21636, 2026)**: perturbation-based score credibility audit，需要能对 items 进行 **修改和重新施测**，非 fully black-box。
- **Cross-Context Verification (arXiv 2603.21454, 2026)**: 通过 session-isolated solution diversity 检测 contamination，9 problems 上达到 perfect separation，但需要 **多次独立 session 施测**（无法用于已有数据）。
- **Han et al., "Quantifying Data Contamination in Psychometric Evaluations of LLMs" (EACL 2026 Findings)**: 量化心理测量问卷（BFI-44, PVQ-40 等）中的 contamination，提出 item memorization / evaluation memorization / target score matching 框架，但 **未使用 person-fit 统计量**，且聚焦心理测量而非能力基准。
- **Educational testing literature on person-fit (Sinharay 2017; Karabatsos 2003)**: 确认 lz* 在 10-30% item preknowledge 时检测力最强，inverted-U 曲线是 well-established 的理论预测。

- **调研总结**: 当前 contamination detection 领域的研究者主要沿两条路线突破：(1) 利用 model internals（logits/entropy）设计更鲁棒的检测器（Self-Critique, CoDeC）；(2) 利用 external probing（perturbation, session diversity）绕过 internal signal 的脆弱性（Silicon Bureaucracy, CCV）。**没有任何已发表或 concurrent 工作从 response pattern 层面利用 psychometric person-fit 统计量进行 contamination detection**，这个 gap 经调研确认为真实的。所有现有方法都需要超出 binary response pattern 的额外信息——这是 IRT-FIT 的根本性差异化。

---

【发掘点 1】
- **维度**: significance 提升 / 核心 claim 强化
- **内容**: 当前 proposal 将 IRT-FIT 的 black-box 特性作为众多优势之一平铺叙述，但调研发现这实际上是一个**信息论层面的根本性定位差异**，应提升为核心 framing。具体来说：IRT-FIT 使用的是**所有可能检测信号中信息量最小的**——纯 binary（correct/incorrect）response pattern。CoDeC 和 Self-Critique 需要 token-level probability（gray-box），Min-K%++ 需要 logits，Silicon Bureaucracy 需要 re-administration 能力，CCV 需要多 session 施测。IRT-FIT 处于 information access hierarchy 的**最底层**。建议将论文核心 framing 从 "cross-domain transfer from psychometrics" 调整为 **"establishing the detection frontier at the minimal-information operating point"**——即：仅凭 binary response pattern 这一最弱信号，contamination detection 的 power envelope 是什么？这不仅是一个 method contribution，更是一个**理论性贡献**，因为它回答了一个基础问题：contamination detection 的信息下界在哪里？
- **价值**: 显著提升 Significance 和 Novelty。将论文从 "一种新检测方法" 提升到 "建立信息接入-检测能力 tradeoff frontier 上的新操作点"。审稿人看到的不是 yet another detector，而是对 detection problem 本身的 information-theoretic understanding 的推进。
- **调研依据**: 系统对比了 CoDeC (gray-box, token prob), Self-Critique (gray-box, entropy sequence), Silicon Bureaucracy (re-administration), CCV (multi-session), Min-K%++ (logits) 的 information access requirement。IRT-FIT 是唯一仅需 binary response pattern 的方法，这个 positioning 在现有文献中无人明确阐述。

【发掘点 2】
- **维度**: significance 提升
- **内容**: Proposal 未充分强调 IRT-FIT 的一个独特实践优势：**retroactive applicability**（追溯性适用）。因为方法仅需 binary response pattern + 已校准的 item parameters，它可以**立即应用于所有已有的 leaderboard 历史数据**，无需对模型进行任何额外施测。这意味着：(1) 可以回溯审计 Open LLM Leaderboard 上所有已提交模型的 contamination 风险；(2) 可以对已关闭 API 或不再公开的历史模型版本进行分析；(3) 不依赖模型提供方的配合。这是其他所有检测方法都做不到的——CoDeC 需要对模型做新的 inference with context, Self-Critique 需要新的 entropy probing, CCV 需要多 session 施测。建议在 Significance 论述中加入 "leaderboard audit at scale" 的应用场景，将 contribution 从 "检测方法" 扩展到 "评估基础设施工具"。
- **价值**: 提升 Significance——解决了一个高度实际的问题（leaderboard integrity 追溯审计），且有明确的 deployment scenario，让审稿人看到 beyond-paper impact。
- **调研依据**: 基于对所有 baseline 方法 information access requirement 的对比分析。特别是 Silicon Bureaucracy 明确需要 re-test，CCV 需要 multi-session，CoDeC/Self-Critique 需要 token-level access——均无法做追溯审计。

【发掘点 3】
- **维度**: novelty 锐化
- **内容**: Proposal 描述的 inverted-U detection power curve（<3% 无信号，10-30% 峰值，50%+ 下降，100% 零检测力）目前被呈现为方法的一个 property/limitation。但这实际上可以被提升为**一个独立的概念性贡献**：它刻画了**所有 response-pattern-based detection 方法的基本检测极限**（不仅限于 person-fit）。理由：100% contamination 不可检测的根本原因不是 person-fit 统计量的局限，而是信息论层面的——uniform high performance 与 genuine high ability 在 response pattern 中不可区分。同理，<3% contamination 信号被 noise 淹没也是 response-level detection 的普遍极限。建议将 inverted-U curve 从 "empirical finding about our method" 重新定位为 "a fundamental characterization of the detection landscape for response-pattern methods"，并讨论其对 contamination detection research agenda 的 implication（例如：future detection methods 需要在哪个 contamination regime 提供增量价值）。
- **价值**: 将一个潜在的 "limitation" 转化为 "contribution"，同时为 paper 增加一个理论层面的 insight，增强 Novelty。审稿人不再只是看到一个 detection tool，还看到了对 detection problem 结构的理解。
- **调研依据**: Sinharay (2017) 和 Karabatsos (2003) 在 educational testing 中已建立 person-fit 的 power curve 理论。但将其从 "单一方法的 power analysis" 推广到 "response-pattern detection 的 fundamental limit" 是 proposal 自身可以做的理论贡献。现有 LLM contamination 文献中无人做过这种系统的 detection limit characterization。

【发掘点 4】
- **维度**: 前提假设质疑
- **内容**: IRT-FIT 的核心假设是 "contaminated LLM ≈ cheating examinee with item preknowledge"，这个类比在 **SFT-based contamination**（直接在 Q-A pair 上 fine-tune）场景下成立。但需要注意一个 assumption gap：**pretraining contamination** 的行为模式可能不同。Pretraining 中的 benchmark data 出现在海量其他数据中，可能产生的不是 "item-specific memorization"（即在特定难题上答对），而是 "generalized ability improvement"（在相关 items 上普遍提升）。后者不会产生 aberrant response pattern（因为是 smooth ability 提升，符合 IRT 模型），person-fit 统计量将无法检测。这不是 proposal 的致命问题（因为 controlled experiment 用的是 SFT，最现实的 contamination concern 也是 SFT-based），但 **需要在论文中明确界定 detection scope**：IRT-FIT 检测的是 "item-level memorization contamination"（SFT/data leakage），不是 "distributional exposure during pretraining"。这个 scoping 如果做得好，反而会增强 paper 的可信度（honest about what we can and cannot detect），避免审稿人以此为攻击点。
- **价值**: 预防审稿人的 predictable attack（"what about pretraining contamination?"）。通过主动界定 scope，将潜在 weakness 转化为论证的 precision，增强整体 claim 的 soundness。
- **调研依据**: Wang et al. (2025) 区分了 Stage I (pretraining/SFT contamination) 和 Stage II (post-RL contamination)，但未进一步区分 pretraining exposure vs. SFT memorization。CoDeC 的 in-context learning approach 同样主要检测 memorization 而非 distributional exposure。这个 scope limitation 是领域共性问题，但 IRT-FIT 需要显式声明。

【发掘点 5】
- **维度**: related work 差异化
- **内容**: Proposal 的 related work 覆盖已相当全面，但存在一个需要显式对比的维度：**与 ConStat (NeurIPS 2024) 的差异化可以更锐利**。ConStat 也是 performance-based detection（不需要 model internals），通过比较模型在 original vs. rephrased benchmark items 上的表现差异来检测 contamination。表面上 ConStat 和 IRT-FIT 都是 "从 performance pattern 检测"，审稿人很可能将两者混淆。关键差异需要锐化：(1) ConStat 需要 **生成 rephrased items 并重新施测**，IRT-FIT 完全不需要；(2) ConStat 的 rephrasing quality 直接影响检测 validity（rephrase 改变了 item semantics 怎么办？），IRT-FIT 使用 calibrated item parameters 不受此影响；(3) ConStat 只能做 binary detection（contaminated or not），IRT-FIT 通过 person-fit p-value 提供连续的 contamination severity 量化。建议在 Related Work 中专门用一段 head-to-head 对比 ConStat，强调 "no re-testing required" 和 "continuous severity quantification" 两个维度。
- **价值**: 防止审稿人将 IRT-FIT 误判为 ConStat 的 incremental improvement。锐化差异化直接影响 Novelty 评分。
- **调研依据**: ConStat (NeurIPS 2024) 是目前最接近 IRT-FIT operating point 的方法（都是 performance-based），因此是最可能被审稿人用来质疑 novelty 的 comparator。

---

Sources:
- [PSN-IRT GitHub](https://github.com/Joe-Hall-Lee/PSN-IRT)
- [Lost in Benchmarks? (AAAI 2026 Oral)](https://arxiv.org/abs/2505.15055)
- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](https://arxiv.org/abs/2510.02386)
- [Self-Critique: Detecting Data Contamination from RL Post-training](https://arxiv.org/abs/2510.09259)
- [CoDeC: Detecting Data Contamination via In-Context Learning](https://arxiv.org/abs/2510.27055)
- [Silicon Bureaucracy: Contamination Sensitivity and Score Confidence](https://arxiv.org/abs/2603.21636)
- [Cross-Context Verification](https://arxiv.org/abs/2603.21454)
- [Han et al., Quantifying Data Contamination in Psychometric Evaluations (EACL 2026)](https://aclanthology.org/2026.findings-eacl.319/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3c66d03-f3c7-4894-8f12-662412bfb9c6",
  "isSidechain": false,
  "requestId": "req_011CbDDWEA1VaagKBq3dkSYE",
  "type": "assistant",
  "uuid": "f3ac6ceb-5ae3-4170-ac71-e6325c340cc8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBcyhEnBLnKEiqYVmPfLXj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 28167,
      "output_tokens": 6591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6591,
          "cache_read_input_tokens": 28167,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 790
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs  ## Description We propose IRT-FIT, the first method that transfers person-fit statistics from educational psyc…",
  "leafUuid": "f3ac6ceb-5ae3-4170-ac71-e6325c340cc8",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Detect LLM benchmark contamination using IRT person-fit statistics",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs  ## Description We propose IRT-FIT, the first method that transfers person-fit statistics from educational psyc…",
  "leafUuid": "f3ac6ceb-5ae3-4170-ac71-e6325c340cc8",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Detect LLM benchmark contamination using IRT person-fit statistics",
  "sessionId": "4c224f93-82cc-4676-966b-092e5c76d381"
}
```

---
