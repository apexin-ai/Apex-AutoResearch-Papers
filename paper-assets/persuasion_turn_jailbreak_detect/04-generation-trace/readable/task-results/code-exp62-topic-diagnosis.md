# code exp62 topic diagnosis

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp62_topic_diagnosis_20260522T170212_result.json`
- **Structured JSON:** [`af2fcf8b7bfbc2161044.json`](../../sessions/af/af2fcf8b7bfbc2161044.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Now let me analyze the findings.

The results **do not** straightforwardly support the original hypothesis. Here's the summary table:

| Model | Dataset | Fisher(mean) | Fisher(top10) | Silhouette | Centroid(L2) | Centroid(norm) |
|-------|---------|:---:|:---:|:---:|:---:|:---:|
| **vanilla** | iid_test | 0.1180 | 0.4478 | 0.0342 | 0.93 | 0.5938 |
| **vanilla** | dd_ood | 0.4014 | 2.9746 | 0.4113 | 1.11 | 1.0615 |
| **vanilla** | aa_ood | 0.4082 | 3.0273 | 0.3300 | 1.04 | 1.0303 |
| **9class_dapt** | iid_test | 0.0733 | 0.4251 | 0.0484 | 7.55 | 0.3662 |
| **9class_dapt** | dd_ood | 0.1995 | 1.4646 | 0.0786 | 12.33 | 0.5568 |
| **9class_dapt** | aa_ood | 0.8323 | 4.8773 | 0.3014 | 27.63 | 1.3767 |
| **topic_dapt** | iid_test | 0.1080 | 0.5830 | 0.0756 | 10.73 | 0.6221 |
| **topic_dapt** | dd_ood | 0.6527 | 3.2567 | 0.2743 | 25.39 | 1.3982 |
| **topic_dapt** | aa_ood | 0.3113 | 1.7473 | 0.1407 | 18.26 | 0.9214 |

Key observations:

1. **9-class DAPT has LOWER Fisher/silhouette on IID & DD OOD** compared to vanilla — the opposite of what the hypothesis predicted. This suggests the 9-class DAPT doesn't simply improve jailbreak/benign separability in the embedding space; instead, it reorganizes the space around persuasion strategy structure, which the downstream GRU leverages.

2. **Topic DAPT has HIGHER separability than 9-class on IID & DD OOD** (Fisher 0.108 vs 0.073; silhouette 0.076 vs 0.048). This contradicts the "topic DAPT blurs the boundary" hypothesis.

3. **The real pattern**: The 9-class model has much larger centroid L2 distances (7.5→27.6) but much lower normalized distances and silhouette scores. This means the 9-class DAPT greatly expands the embedding space while distributing both classes broadly — it creates a richer representation geometry that the GRU classifier can exploit over the sequence of turns, even though single-turn separability is lower.

The original hypothesis (topic DAPT blurs jailbreak/benign boundary) **is not supported** by the embedding-level evidence. The failure mechanism must be different — likely topic DAPT fails not because it merges jailbreak/benign, but because topic classification doesn't teach the encoder features useful for the downstream temporal detection task (persuasion strategy progression patterns are what matter).

---
