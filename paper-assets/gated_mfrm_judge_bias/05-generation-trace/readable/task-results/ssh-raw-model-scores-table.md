# ssh raw model scores table

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_raw_model_scores_table_20260523T015054_result.json`
- **Structured JSON:** [`9f6e9fb8393165c7f4af.json`](../../sessions/9f/9f6e9fb8393165c7f4af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here are the results.

---

### Raw Model Scores Table

All values on logit scale, sorted by Arena ELO descending. Sources: RawAvg/Cyclic/CycDisc/DCR/PrefLk from exp-004; MFRM/Sequential from exp-003; G-MFRM from exp-003b (HalfNormal prior).

```
Model                  Arena   RawAvg     MFRM      Seq   G-MFRM   Cyclic  CycDisc      DCR   PrefLk
----------------------------------------------------------------------------------------------------
gpt-4o                  1286   1.3046   1.5916   1.6381   1.9865   1.2741   1.2912   1.3508   1.3046
gpt-4o-mini             1272   0.8897   1.0640   1.1262   1.4317   0.8574   0.8909   0.9336   0.8897
qwen2.5-72b             1187   0.9839   1.2124   1.1953   1.1793   0.9537   0.9502   0.9742   0.9839
llama-3.3-70b           1208   0.4230   0.5176   0.5253   0.5397   0.4081   0.4669   0.4326   0.4230
qwen3-8b                1170   0.1403   0.2067   0.2675   0.5164   0.2009   0.2661   0.1779   0.1403
gemma-2-9b              1130  -0.5013  -0.6598  -0.6447  -0.5038  -0.5072  -0.4702  -0.4641  -0.5013
gpt-4-0613              1163  -1.2013  -1.4445  -1.5183  -1.8764  -1.1789  -1.2774  -1.2539  -1.2013
gpt-3.5-turbo-0125      1105  -2.0390  -2.4880  -2.5892  -3.2733  -2.0080  -2.1178  -2.1511  -2.0390
```

### Score Identity Check

```
raw_avg vs mfrm_only            : NO  (max diff: 0.449), ranking: SAME
raw_avg vs sequential           : NO  (max diff: 0.550), ranking: SAME
raw_avg vs joint_gmfrm          : NO  (max diff: 1.234), ranking: DIFFERENT
raw_avg vs cyclic_judge         : NO  (max diff: 0.061), ranking: SAME
raw_avg vs cyclic_judge_discard : NO  (max diff: 0.126), ranking: SAME
raw_avg vs dcr_factor           : NO  (max diff: 0.112), ranking: SAME
raw_avg vs preference_leakage   : YES (max diff: 0.000001), ranking: SAME
```

### Conclusion

**Scores differ across all methods, but 7 of 8 methods produce the identical ranking.** Only Joint G-MFRM swaps qwen2.5-72b (rank 2→3) and gpt-4o-mini (rank 3→2), which is the ranking change that improves τ from 0.786 to 0.857.

Key observations:
- **Preference Leakage ≈ Raw Average**: virtually identical scores (max diff ~1e-6), meaning the judge-bias correction in PrefLeak has negligible effect on this dataset
- **G-MFRM stretches the scale**: it amplifies score differences (especially for bottom models like gpt-3.5-turbo: -2.04 → -3.27), reflecting the contamination correction separating genuine ability from exposure-inflated scores
- **Non-contamination baselines cluster**: RawAvg, Cyclic, CycDisc, DCR, PrefLk all produce similar scores (within ~0.13 of each other)
- **MFRM and Sequential are between**: they use IRT modeling but without joint contamination correction, producing moderate score stretching

---
