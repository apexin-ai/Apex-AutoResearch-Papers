# analysis surprisal vs binary

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_surprisal-vs-binary_20260515T060559_result.json`
- **Structured JSON:** [`a8f024ec272152e244e4.json`](../../sessions/a8/a8f024ec272152e244e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

### Summary (mean±std, 5 seeds)

| Strategy | n | MMLU | HellaSwag |
|---|---|---|---|
| **base_model** | 1 | 0.6018 | 0.6821 |
| no-filter | 5 | 0.5865±0.0010 | 0.6638±0.0008 |
| **binary-ours** | 5 | **0.5941±0.0008** | **0.6701±0.0006** |
| binary-drayson | 5 | 0.5913±0.0009 | 0.6691±0.0004 |
| **surprisal** | 5 | 0.5894±0.0009 | 0.6641±0.0006 |
| graduated_a0.1 | 5 | 0.5873±0.0019 | 0.6640±0.0009 |
| graduated_a0.3 | 5 | 0.5877±0.0013 | 0.6669±0.0005 |
| graduated_a0.5 | 5 | 0.5880±0.0013 | 0.6687±0.0008 |
| graduated_a0.7 | 5 | 0.5892±0.0014 | 0.6695±0.0004 |
| graduated_a0.9 | 5 | 0.5892±0.0008 | 0.6701±0.0007 |

### Delta: surprisal - binary-ours

| Metric | binary-ours | surprisal | Δ |
|---|---|---|---|
| MMLU | 0.5941 | 0.5894 | **-0.0047** |
| HellaSwag | 0.6701 | 0.6641 | **-0.0061** |

### Per-seed detail

| Run | MMLU | HellaSwag |
|---|---|---|
| binary-ours_s42 | 0.5945 | 0.6701 |
| binary-ours_s123 | 0.5929 | 0.6699 |
| binary-ours_s456 | 0.5937 | 0.6709 |
| binary-ours_s789 | 0.5942 | 0.6692 |
| binary-ours_s1024 | 0.5953 | 0.6706 |
| surprisal_s42 | 0.5898 | 0.6646 |
| surprisal_s123 | 0.5889 | 0.6637 |
| surprisal_s456 | 0.5895 | 0.6632 |
| surprisal_s789 | 0.5908 | 0.6641 |
| surprisal_s1024 | 0.5880 | 0.6647 |

**binary-ours 在 MMLU 和 HellaSwag 上均优于 surprisal**，差距分别为 +0.47pp 和 +0.61pp。binary-ours 在所有 5 个 seed 上均一致领先，且是所有策略中最接近 base_model 的（能力保留最好）。graduated_a0.9 的 HellaSwag 与 binary-ours 持平（0.6701），但 MMLU 仍低 0.5pp。

---
