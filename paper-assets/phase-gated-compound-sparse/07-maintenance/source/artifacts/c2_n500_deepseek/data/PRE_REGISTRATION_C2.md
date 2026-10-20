# C2 Pre-registration: n=500 Statistical Power Boost
Date: 2026-05-14
Pre-registered before experiments begin.

## Hypothesis
Expanding from n=50 to n=500 (full MATH-500) will tighten confidence intervals and confirm existing findings about phase-modulated compound sparsity severity.

## Decision rule
If QW s015 CI still crosses zero at n=500:
→ Paper narrative changes to: "compound effect emerges above a threshold sparsity level (~s020)"
This is not a failure but a more precise claim.

## Conditions
8 conditions: DeepSeek-R1-Distill-Qwen-7B (bfloat16)
- importance × {s=0.15, 0.20, 0.25, 0.30}
- random × {s=0.15, 0.20, 0.25, 0.30}

## Analysis plan
Per-problem Interaction Index (II), then:
- Median II per phase per condition
- Bootstrap 95% CI (B=1000)
- Cohen's d (paired, importance vs random)
- Permutation test (10000 permutations)