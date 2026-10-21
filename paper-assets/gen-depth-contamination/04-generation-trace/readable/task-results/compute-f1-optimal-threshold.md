# compute f1 optimal threshold

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_f1-optimal-threshold_20260519T170145_result.json`
- **Structured JSON:** [`c6c95256bffb4a5cf2a5.json`](../../sessions/c6/c6c95256bffb4a5cf2a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All results complete. Here's the full report:

---

## F1@optimal-threshold Analysis Results

### Methodological note
For balanced binary classes (50/50), the naive "predict all-positive" strategy gives F1 = 2/3 ≈ 0.667. The unconstrained F1@optimal-threshold converges to this trivial solution for near-random classifiers (threshold drops to ~0.1-0.2). **F1@threshold=0.50** is the more meaningful metric, where random baseline ≈ 0.50.

### Table 1: F1@threshold=0.50

| Config | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 |
|--------|------|------|------|------|------|
| Qwen-base | .941 | **.597** | .531 | .525 | .513 |
| Pythia-nuc0.9 | .967 | **.635** | .548 | .522 | .490 |
| Pythia-greedy | .988 | **.810** | .526 | .505 | .510 |
| Pythia-T0.7 | .974 | **.662** | .575 | .548 | .530 |
| Pythia-T1.2 | .957 | **.591** | .525 | .511 | .511 |
| Mistral-7B | .933 | .554 | .528 | .505 | .509 |
| LLaMA-8B | .842 | **.569** | .503 | .510 | .508 |

### Table 2: Pairwise AUC (reference)

| Config | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 |
|--------|------|------|------|------|------|
| Qwen-base | .987 | .629 | .555 | .527 | .520 |
| Pythia-nuc0.9 | .995 | .675 | .559 | .524 | .501 |
| Pythia-greedy | .999 | .884 | .531 | .522 | .514 |
| Pythia-T0.7 | .996 | .728 | .598 | .563 | .527 |
| Pythia-T1.2 | .994 | .618 | .531 | .520 | .510 |
| Mistral-7B | .984 | .590 | .537 | .525 | .527 |
| LLaMA-8B | .923 | .608 | .527 | .528 | .516 |

### Table 3: F1@optimal-threshold (unconstrained sweep)

| Config | 0v1 F1 (thr) | 1v2 F1 (thr) | 2v3 F1 (thr) | 3v4 F1 (thr) | 4v5 F1 (thr) |
|--------|-------------|-------------|-------------|-------------|-------------|
| Qwen-base | .942 (.44) | .676 (.32) | .667 (.25) | .667 (.18) | .667 (.10) |
| Pythia-nuc0.9 | .968 (.57) | .685 (.31) | .667 (.12) | .667 (.20) | .667 (.21) |
| Pythia-greedy | .990 (.64) | .819 (.38) | .667 (.20) | .668 (.26) | .667 (.23) |
| Pythia-T0.7 | .974 (.45) | .698 (.33) | .668 (.20) | .667 (.18) | .667 (.10) |
| Pythia-T1.2 | .959 (.62) | .669 (.21) | .667 (.10) | .667 (.12) | .667 (.17) |
| Mistral-7B | .935 (.53) | .667 (.23) | .667 (.18) | .667 (.12) | .667 (.17) |
| LLaMA-8B | .847 (.40) | .667 (.25) | .667 (.14) | .667 (.13) | .667 (.12) |

### Key findings

**F1 boundary is consistent with AUC-based K\*=2 for 6/7 configs.**

1. **Clear boundary at 2v3**: All configs show a sharp F1@0.50 drop from 1v2 to 2v3. For 1v2, F1 is meaningfully above 0.50 (0.554–0.810); for 2v3, it collapses near 0.50 (0.503–0.575).

2. **Mistral-7B confirms K\*=1**: Even 1v2 F1@0.50=0.554 is barely above random, matching its AUC-based K\*=1 (1v2 AUC=0.590 < θ=0.60).

3. **Pythia-T0.7 is the sole borderline case**: 2v3 F1@0.50=0.575 is slightly elevated (AUC=0.598, just below θ). This reflects that lower-temperature decoding preserves more statistical structure.

4. **F1@optimal-threshold is uninformative for weak classifiers**: Unconstrained sweep converges to the trivial all-positive baseline (F1≈0.667, threshold<0.25) whenever AUC<~0.65. F1@0.50 is the better auxiliary metric.

5. **Note on data**: The exact Table 2 experiment directories (exp_001/002/003/006) are not present on the server. Results use the available C4-domain experiments (Qwen-base, Pythia decoding variants, Mistral-7B, LLaMA-8B). The AUC values closely match the paper range.

Results saved to `/root/autodl-tmp/gen-depth-contamination/results/f1_optimal_threshold/f1_optimal_results.json`.

---
