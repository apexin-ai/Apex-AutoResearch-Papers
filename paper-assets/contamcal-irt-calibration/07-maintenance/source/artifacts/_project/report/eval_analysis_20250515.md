# Eval Analysis: 3 Experiments (2026-05-15)

## 1. exp_001_eval_3B_d025_v2_para_aligned ✅
- .done marker present, fully complete
- Paraphrased benchmarks, aligned format

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| MMLU | 0.6210 | 4096/6596 |
| GSM8K | 0.5482 | ~125/228 |
| ARC | 0.8106 | ~565/697 |
| HumanEval | 0.1154 (pass@1) | 3/26 |

## 2. exp_001_eval_3B_d100_v2_aligned_v2 ✅
- No .done but JSON output complete and valid
- Non-paraphrased, aligned format

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| MMLU | 0.6320 | 8874/14042 |
| GSM8K | 0.7415 | ~978/1319 |
| ARC | 0.8242 | ~966/1172 |
| HumanEval | 0.1707 (pass@1) | 28/164 |

## 3. exp_008_instruct_05B_eval ✅
- No .done but JSON output complete and valid
- 0.5B-Instruct (SFT+RL), aligned format

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| MMLU | 0.2462 | 3457/14042 |
| GSM8K | 0.3882 | ~512/1319 |
| ARC | 0.2816 | ~330/1172 |
| HumanEval | 0.0 (pass@1) | 0/164 |

---

## Contamination Effect at 3B Scale (d100 vs d000 aligned)

| Benchmark | d000 | d100 | Delta |
|-----------|------|------|-------|
| MMLU | 0.6295 | 0.6320 | +0.0025 |
| GSM8K | 0.3525 | **0.7415** | **+0.3890** |
| ARC | 0.8183 | 0.8242 | +0.0059 |
| HumanEval | 0.0976 | 0.1707 | +0.0731 |

**Key finding**: GSM8K shows massive 39pp contamination effect at 3B scale. MMLU and ARC unaffected.

## S4 Paraphrase Gap (3B, aligned - para)

| Benchmark | d000 gap | d100 gap | Net (d100-d000) |
|-----------|----------|----------|-----------------|
| MMLU | -0.017 | -0.027 | -0.010 |
| GSM8K | +0.063 | **+0.158** | **+0.095** |
| ARC | +0.006 | +0.015 | +0.009 |
| HumanEval | +0.059 | +0.055 | -0.004 |

**Key finding**: Net paraphrase gap for GSM8K = +9.5pp, confirming contamination is detectable through paraphrase-based signal.

## 0.5B Three-Regime Comparison (d000 → d100 → Instruct)

| Benchmark | d000 (SFT clean) | d100 (SFT contam) | Instruct (SFT+RL) |
|-----------|-------------------|--------------------|--------------------|
| MMLU | 0.3979 | 0.2334 | 0.2462 |
| GSM8K | 0.3692 | 0.3654 | 0.3882 |
| ARC | 0.4693 | 0.2944 | 0.2816 |
| HumanEval | 0.1098 | 0.0 | 0.0 |

**Key findings**:
1. At 0.5B, d100 contamination HURTS MMLU (-16.5pp) and ARC (-17.5pp) but barely changes GSM8K
2. Instruct ≈ d100: RL post-training doesn't recover from SFT-induced degradation
3. Both d100 and Instruct lose HumanEval capability entirely
4. Contrast with 3B: at 3B scale, d100 boosts GSM8K +39pp while keeping MMLU/ARC stable → model capacity determines whether contamination helps or hurts

## Missing Data
- 3B d025 v2 aligned (non-paraphrased): only eval.log, no JSON output. Eval incomplete/failed. Needed for d025 paraphrase gap computation.
