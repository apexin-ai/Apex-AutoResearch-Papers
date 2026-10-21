# ssh w1 cluster bootstrap

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_w1-cluster-bootstrap_20260518T070541_result.json`
- **Structured JSON:** [`4e5c03daca3ab976c78f.json`](../../sessions/4e/4e5c03daca3ab976c78f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `/root/autodl-tmp/simgate-modular-routing/artifacts/w1_cluster_bootstrap.md`.

## Results Summary

**Data**: K=7 task clusters, N=240 episodes (actual data has 7 tasks with 20-40 episodes each, not K=11 as originally estimated; `plan_c` directories were empty).

**Death rate differential**: Grand mean = 0.2964, range [0.20, 0.40]. All 7/7 tasks show internal agent dying more than deterministic.

| Method | p-value | 95% CI |
|---|---|---|
| Cluster-robust t-test (df=6) | 0.0001 | [0.2126, 0.3802] |
| Wild cluster bootstrap (B=9999) | 0.0142 | [0.2393, 0.3607] |
| Exact permutation test (128 perms) | 0.0156 | — |
| Sign test | 0.0156 | — |
| Wilcoxon signed-rank | 0.0156 | — |

**Cohen's d = 3.27** (massive effect size).

**Conclusion**: Death asymmetry is significant (p < 0.05) across all three primary methods, even at K=7. The exact permutation p-value of 1/64 = 0.0156 is the theoretical minimum for a two-sided test with K=7 (all signs must align), confirming the finding is as strong as possible given the cluster count. The CI excludes zero by a wide margin.

Note: The 2/128 extreme permutations correspond to the two cases where all 7 signs flip to +1 or all to -1, producing the maximal |mean|. This is the strongest possible result for K=7.

---
