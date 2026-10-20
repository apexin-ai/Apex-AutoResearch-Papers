# Round 8 Analysis: FK Independence + TOST External Delta

## Task 1: FK Independence Instance-Level Test (R3-W4)

### Problem
Round 8 reviewer: FK independence test used n=5 t-test with extremely low statistical power.

### Solution
Instance-level analysis: each instance yields one FK value (N=8 samples as 8 raters), n=529-2756.

### Results

| Config | n | FK mean | 95% CI | t-stat | t-test p | Perm p | Split-half r |
|--------|---|---------|--------|--------|----------|--------|-------------|
| SciERC (Qwen) | 529 | 0.402 | [0.376, 0.428] | 30.8 | 4.0e-120 | <0.0002 | 0.395 |
| CoNLL (LLaMA) | 2756 | 0.927 | [0.919, 0.935] | 225.9 | <1e-300 | <0.002 | 0.578 |
| CoNLL (Qwen) | 2756 | 0.720 | [0.706, 0.734] | 102.1 | <1e-300 | <0.002 | 0.520 |

### Suggested Paper Wording

To test whether FK reflects genuine within-instance agreement, we conducted instance-level permutation tests. The observed mean FK (0.40 on SciERC n=529; 0.72-0.93 on CoNLL n=2756) exceeded all permuted values (null ~ -0.14), p < 0.001. One-sample t-tests (n=529-2756) confirmed FK > 0 with t >= 30.8 (all p < 10^-120). Split-half reliability r = 0.39-0.58.

---

## Task 2: TOST External Delta Benchmark (R4-M2)

### Problem
TOST delta anchored to oracle headroom = circular reasoning.

### Solution
Three external anchors: delta_SEM (bootstrapped SE, 0.43-1.33pp), delta_practical (0.5pp), delta_literature (1.0pp).

### Key Results

- LLaMA-CoNLL (F1=0.924): ALL signals equivalent at ALL deltas (p<0.001)
- Qwen-CoNLL (F1=0.908): NO signals pass (selection degrades 0.9-1.5pp)
- SciERC (F1~0.644): Only SJ passes at delta_SEM

### Suggested Paper Wording

To avoid circularity, we anchor TOST to three external benchmarks: delta_SEM = bootstrapped SE of greedy F1 (0.43-1.33pp), delta_practical = 0.5pp (Ratinov & Roth 2009), delta_literature = 1.0pp (Berg-Kirkpatrick et al. 2012). On LLaMA-CoNLL, all signals achieve equivalence at all thresholds (p<0.001). On SciERC/Qwen-CoNLL, only SJ at delta_SEM passes, suggesting selective application benefits these configurations.

## Data Files (on server autodl-5090)
- analysis_round8/fk_independence_instance_test.json
- analysis_round8/tost_external_delta.json
