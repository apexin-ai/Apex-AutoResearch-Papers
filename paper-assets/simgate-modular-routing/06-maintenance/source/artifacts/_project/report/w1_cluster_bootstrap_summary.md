# W1: Wild Cluster Bootstrap — Death Asymmetry Soundness Check

**Source**: westd-18266:/root/autodl-tmp/simgate-modular-routing/artifacts/w1_cluster_bootstrap.md

## Data
- K=7 task clusters (not K=11; some plan_c directories empty)
- N=240 episodes (20-40 per task)
- Death rate differential grand mean = **29.6%**, range [20%, 40%]
- 7/7 tasks: internal DR > deterministic DR

## Results

| Method | p-value | 95% CI |
|--------|---------|--------|
| Cluster-robust t-test (df=6) | **0.0001** | [0.213, 0.380] |
| Wild cluster bootstrap (B=9999) | **0.0142** | [0.239, 0.361] |
| Exact permutation (128 perms) | **0.0156** | — |
| Sign test | **0.0156** | — |
| Wilcoxon signed-rank | **0.0156** | — |

**Cohen's d = 3.27** (massive effect size)

## Interpretation
- p=0.0156 is the **theoretical minimum** for two-sided K=7 (all 7 signs must align → 2/128 = 1/64)
- Death asymmetry survives cluster-robust inference with wide margin
- The result is "as strong as possible given the cluster count"

## Paper Narrative
"Even accounting for task-level clustering (K=7), death asymmetry remains highly significant (wild cluster bootstrap p=0.014, exact permutation p=0.016). The effect size (Cohen's d=3.27) is massive, and the 95% CI [0.21, 0.38] excludes zero by a wide margin."