# analysis exp wiki scorer confound

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_wiki_scorer_confound_20260517T231531_result.json`
- **Structured JSON:** [`2158d1ff08597283a922.json`](../../sessions/21/2158d1ff08597283a922.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report saved. The experiment isn't in the registry (likely wasn't registered), but the analysis is complete.

---

**Verdict: Scorer confound confirmed. Qwen-7B Wikipedia K\*=1 (not 2).**

The critical depth pair 1v2 AUC drops from 0.6108 (Qwen scorer, barely above 0.60) to 0.5870 (Pythia scorer, below threshold). Qwen-1.5B scorer inflates AUC uniformly across all depth pairs by 0.005-0.027, with the largest bias at shallow depths. This aligns Qwen-7B with all other models on Wikipedia (K\*=1).

```json
{
  "k_star": 1,
  "confound_verdict": "confirmed",
  "depth_pairs": {
    "0v1": {"ordinal_accuracy": null, "auc": 0.9404, "auc_std": 0.0043, "jsd": 0.068909},
    "1v2": {"ordinal_accuracy": null, "auc": 0.5870, "auc_std": 0.0088, "jsd": 0.008241},
    "2v3": {"ordinal_accuracy": null, "auc": 0.5456, "auc_std": 0.0049, "jsd": 0.005474},
    "3v4": {"ordinal_accuracy": null, "auc": 0.5250, "auc_std": 0.0134, "jsd": 0.004037},
    "4v5": {"ordinal_accuracy": null, "auc": 0.5172, "auc_std": 0.0082, "jsd": 0.003646}
  },
  "ordinal_mae": 1.3559,
  "ordinal_accuracy": 0.331,
  "comparison_with_qwen_scorer": {
    "qwen_scorer_k_star": 2,
    "pythia_scorer_k_star": 1,
    "critical_pair_1v2_auc_delta": -0.0238
  },
  "wandb_run_id": null
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "k_star": 1,
    "confound_verdict": "confirmed",
    "depth_pairs": {
      "0v1": {
        "ordinal_accuracy": null,
        "auc": 0.9404,
        "auc_std": 0.0043,
        "jsd": 0.068909
      },
      "1v2": {
        "ordinal_accuracy": null,
        "auc": 0.587,
        "auc_std": 0.0088,
        "jsd": 0.008241
      },
      "2v3": {
        "ordinal_accuracy": null,
        "auc": 0.5456,
        "auc_std": 0.0049,
        "jsd": 0.005474
      },
      "3v4": {
        "ordinal_accuracy": null,
        "auc": 0.525,
        "auc_std": 0.0134,
        "jsd": 0.004037
      },
      "4v5": {
        "ordinal_accuracy": null,
        "auc": 0.5172,
        "auc_std": 0.0082,
        "jsd": 0.003646
      }
    },
    "ordinal_mae": 1.3559,
    "ordinal_accuracy": 0.331,
    "comparison_with_qwen_scorer": {
      "qwen_scorer_k_star": 2,
      "pythia_scorer_k_star": 1,
      "critical_pair_1v2_auc_delta": -0.0238
    },
    "wandb_run_id": null
  }
}
```

</details>

---
