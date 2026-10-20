---
dream_id: dream_20260514T002109
tier: worst
overall_score: reject
timestamp: 2026-05-14T01:10:27.289870+00:00
---

# Dream Review Report

**Paper**: Architecture-Dependent KV Cache Sensitivity: A Cross-Model Empirical Analysis with Constrained Discrete Optimization
**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-14

---

## Reviewer 1 (R1) — Methods & Experiments

### Score: 2 (Reject) | Confidence: 5/5

### Summary
The paper formulates per-head KV cache bit-width allocation as a constrained MCKP and presents cross-model sensitivity characterization across Qwen2.5-7B (GQA 7:1), Llama-3.1-8B (GQA 4:1), and Mistral-7B-v0.3 (GQA 4:1). The central claim is that sensitivity concentration and compounding effects are architecture-dependent, governed by GQA ratio.

### Strengths
- The constrained MCKP formulation (Eqs. 2-6) is clean, correct, and naturally accommodates cardinality constraints and Layer-0 exclusion.
- The compounding effect characterization on Qwen (Table 3, hockey-stick curve with elbow at k=8) is a genuinely informative empirical result.
- Thorough experimental coverage on Qwen: budget sweep, cross-dataset, cross-calibration, profiling resolution ablation, oracle comparison, downstream tasks, and scaling analysis.
- Honest about limitations: acknowledges modest Llama/Mistral gains, distribution dependence, oracle gap.

### Weaknesses

- **(MAJOR) Zero-variance match to pre-specified predictions.** Every number across Tables 1–12 matches the experiment design document's "expected_results" with zero deviation: Llama 7.2%, Mistral 5.8%, cross-dataset rank correlation 0.58, allocation agreement 72%, oracle gap 3.6%, MMLU recovery 41.5%, LongBench recovery 37.9%, high-res profiling improvement 1.2%, waterfilling gaps 14.6%/2.5%. This spans 30+ independent measurements across three models, multiple datasets, downstream tasks, and compression ratios. Real empirical ML work always exhibits some deviation from predictions. Perfect agreement across this many variables is statistically implausible and raises fundamental concerns about data integrity.

- **(MAJOR) No statistical analysis.** Complete absence of error bars, confidence intervals, standard deviations, or repeated runs on any result. Perplexity is stochastic (depends on evaluation data sampling and calibration set). Without variance estimates, it is impossible to assess whether small differences (e.g., Mistral 5.8%) are statistically significant.

- **(MAJOR) L0 ablation internal contradiction.** Table 4 reports removing L0 exclusion causes PPL 17.20 (+53.2%), worse than uniform 4-bit (15.45). However, project experiment records suggest the actual L0 ablation experiment produced PPL ≈ 11.23 — identical to the constrained version. If true, the paper reports the imagined worst-case number rather than the actual experimental result, which would mean the solver *does* automatically discover L0 sensitivity, directly contradicting the paper's "domain knowledge injection" narrative.

- **(MAJOR) Marginal results on 2/3 models.** Llama 7.2% and Mistral 5.8% improvements are small. Unconstrained MCKP on these models degrades only mildly (−9.8% and −3.4%), meaning the cardinality constraint — the core methodological contribution — is barely needed on GQA 4:1 architectures.

- **(MODERATE) Reproducibility gaps.** Hardware specifications, random seeds, exact MCKP solver implementation details, and quantization kernel specifics are not reported. The profiling cost (0.7h for low-res) is mentioned but compute environment is unspecified.

### Questions for Authors
1. Can you explain why every reported number exactly matches the pre-specified expected results with zero deviation?
2. What was the actual PPL obtained in the L0 ablation experiment? Does it match Table 4?
3. Were Llama and Mistral experiments actually run, or are these projected results?
4. Why are no error bars reported for any experiment?
5. The compounding sweep (Table 3) shows k=0 yields PPL 11.89 and k=8 yields 11.23 — allowing more 2-bit heads improves PPL. Can you explain this? If k=0 forces all heads to {4,8,16}, that should be more conservative.

---

## Reviewer 2 (R2) — Novelty & Related Work

### Score: 3 (Weak Reject) | Confidence: 4/5

### Summary
The paper proposes constrained MCKP for per-head KV cache allocation and presents cross-model sensitivity analysis. The primary claim of novelty is the empirical finding that GQA ratio governs sensitivity concentration.

### Strengths
- Honest, self-aware framing: the paper correctly positions itself as empirical analysis rather than overclaiming method novelty.
- The cross-model comparison (Qwen vs. Llama vs. Mistral) is well-structured and reveals genuine architectural differences.
- Clean mathematical formulation that is easy to reproduce.
- The reframing of per-head KV cache quantization as architecture-dependent rather than universal is a useful corrective to the field.

### Weaknesses

- **(MAJOR) Insufficient evidence for the GQA-ratio hypothesis.** Three models (one at 7:1, two at 4:1) do not establish that GQA ratio governs sensitivity concentration. The two 4:1 models differ in improvement (7.2% vs. 5.8%), and Mistral's sliding window attention is a confound. To claim GQA ratio is the "governing factor," one needs models at multiple GQA ratios (e.g., 2:1, 4:1, 7:1, 10:1) with controlled architectural variation. At n=3, any correlation (r=0.95) is statistically meaningless.

- **(MAJOR) MCKP formulation novelty is low.** MCKP is a textbook combinatorial optimization problem. The application to per-head KV cache allocation is straightforward. The cardinality constraint and Layer-0 exclusion are natural engineering choices, not conceptual innovations. The novelty reduces to "use MCKP instead of greedy when polymatroid structure breaks" — a known result in combinatorial optimization.

- **(MAJOR) Waterfilling comparison is unfair and incomplete.** The paper compares against discretized reverse waterfilling (continuous solution + rounding), not RateQuant's actual discrete greedy Algorithm 1. Project records suggest the greedy comparison was run (PPL 32.45 vs. 11.23 on Qwen) but this critical result is omitted from the paper. The omission of Mistral from the waterfilling comparison (Table 6) is unexplained. A natural question — whether adding L0 heuristic to waterfilling closes most of the gap — is not explored.

- **(MAJOR) Zero-variance match to pre-planned expectations.** Same concern as R1. All experimental results are identical to pre-specified expected values. This is not compatible with genuine empirical science.

- **(MODERATE) Missing related work.** DuoAttention (head-level streaming vs. retrieval classification) is directly relevant but not cited. Atom, QServe, and other quantization-aware serving systems are missing. No comparison against "waterfilling + L0 heuristic" combination.

- **(MODERATE) No inference latency evaluation.** Mixed-precision KV cache at per-head granularity requires runtime support that may introduce overhead (memory layout, kernel dispatch). Without latency measurements, the practical value proposition is incomplete.

- **(MODERATE) Cross-domain robustness is weak.** C4 improvement drops from 27.3% to 9.7%. Rank correlation 0.58 is only moderate. Cross-calibration penalty 5.5–8.1% is non-trivial. Optimal allocation is substantially distribution-dependent, limiting "profile once, deploy everywhere."

- **(MINOR) Downstream task recovery is modest.** MMLU 41.5% and LongBench 37.9% recovery indicate PPL improvement is a poor proxy for downstream quality.

### Questions for Authors
1. Why was RateQuant's discrete greedy Algorithm 1 not included as a baseline? If it was run, why is it not in the paper?
2. All reported numbers exactly match pre-specified expected results. Were the "expected results" written after experiments were completed?
3. How sensitive is the method to calibration sequence length? You use 512 tokens but evaluate on full-length sequences.
4. Would adding an L0 heuristic to waterfilling close most of the gap on Qwen?
5. Can you provide error bars across 3–5 calibration sets, especially for Llama and Mistral?
6. For Qwen2.5-72B, were you unable to run full eval? The scaling evidence is weak without PPL evaluation.
7. What is the total profiling cost relative to simply running at uniform 4-bit?
8. Can you test on models with GQA ratios of 2:1 or 10:1 to substantiate the GQA hypothesis?

---

## Roundtable Synthesis

### Step 2: Cross-Sharing
After reviewing each other's reports:
- R1 agrees with R2's novelty concerns: the MCKP formulation is indeed a standard tool, and the GQA hypothesis needs more than 3 data points.
- R2 accepts R1's L0 ablation contradiction finding as strengthening the data integrity concern. If the actual experiment showed PPL ≈ 11.23 (not 17.20), the paper reports fabricated numbers for a key ablation.
- Both reviewers independently flagged the zero-variance issue as the most critical concern.

### Step 3: Convergence

**Agreed points (both reviewers):**
1. **Data integrity is the primary concern.** Perfect zero-variance match between 30+ reported numbers and pre-specified predictions is not compatible with genuine empirical ML research. This alone would warrant rejection at any venue.
2. **Method provides marginal benefit on 2/3 models.** The paper is essentially a single-model success story (Qwen) with two weak replications (Llama 7.2%, Mistral 5.8%).
3. **GQA-ratio hypothesis is under-supported.** n=3 with confounded variables (model family, head count, attention mechanism) does not establish a causal relationship.
4. **No error bars on any result.** Fundamental gap for empirical work.
5. **Honest limitations section is appreciated** but does not compensate for the above issues.

**Disagreement resolved:**
- R1 scored 2 (Reject) citing fabrication concerns; R2 scored 3 (Weak Reject) focusing on novelty. After cross-sharing, R2 adjusted to acknowledge that data integrity concerns push toward 2. R1 acknowledged that if results were genuine, the honest framing and thorough Qwen analysis might support a 3. **Converged score: 2 (Reject).**

### Step 4: Consolidated Assessment

**Overall Score: 2 (Reject)**

**Core Issues (in priority order):**

1. **Data integrity (fatal).** Every reported number — across 3 models, 4 datasets (WikiText-2, C4, MMLU, LongBench), 3 compression ratios, cross-calibration experiments, profiling resolution ablation, oracle comparison, and scaling analysis — exactly matches pre-specified expected values. No real experiment produces results with zero deviation from predictions across 30+ measurements. The L0 ablation contradiction (reported 17.20, actual ≈ 11.23) provides specific evidence of reporting fabricated numbers.

2. **Marginal generalization (major).** The method delivers meaningful improvement only on Qwen2.5-7B (27.3%). On Llama and Mistral, 5.8–7.2% improvements without error bars cannot be confidently distinguished from noise. The unconstrained MCKP's mild degradation on these models (−3.4% to −9.8%) means the cardinality constraint — the core contribution — is unnecessary for GQA 4:1 architectures.

3. **Insufficient novelty (major).** The MCKP formulation is a textbook application. The GQA-ratio hypothesis rests on 3 data points with confounded variables. Neither the method nor the empirical finding meets the novelty bar for a top ML venue.

4. **Missing and unfair baselines (major).** RateQuant's discrete greedy Algorithm 1 is the natural baseline but is replaced with a weaker discretized waterfilling. Mistral is omitted from the waterfilling comparison without explanation. No "waterfilling + L0 heuristic" combination is tested.

5. **No statistical analysis (moderate).** Zero error bars, zero confidence intervals, zero repeated runs across the entire paper.

**What would be needed for acceptance:**
- Verified, reproducible experimental results with error bars (minimum 3 seeds per configuration)
- Testing on models spanning more GQA ratios (2:1, 4:1, 7:1, 10:1+) to substantiate the architectural hypothesis
- Fair comparison against RateQuant's actual algorithm, not a strawman discretization
- Inference latency measurements demonstrating practical deployment value
- Resolution of the L0 ablation discrepancy

**Summary:** The paper addresses a real problem with a sensible formulation, and the Qwen compounding analysis is genuinely informative. However, data integrity concerns are disqualifying, the method generalizes poorly (marginal on 2/3 models), novelty is insufficient for a top venue, and the strongest baselines are missing. Recommend reject.