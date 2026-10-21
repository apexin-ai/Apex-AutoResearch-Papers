# analyze kl30 s456 uniform eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_kl30_s456_uniform_eval_20260517T150532_result.json`
- **Structured JSON:** [`809042735153000d2237.json`](../../sessions/80/809042735153000d2237.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE/success. Here's the analysis:

```json
{
  "metrics": {
    "wikitext2_ppl": 8.7947,
    "arc_challenge_acc_norm": 0.4505,
    "winogrande_acc": 0.6875,
    "mmlu_acc": 0.4198,
    "gsm8k_exact_match": 0.0758,
    "actual_sparsity": 0.300,
    "allocation": "uniform"
  },
  "conclusion": "success",
  "analysis": "s456 uniform MMLU=0.4198 is slightly above s42/s123 range but uniform 3-seed std=0.013, far tighter than global allocation's observed 0.25-0.44 spread, confirming uniform allocation provides consistent cross-seed MMLU",
  "comparison": {
    "uniform_seeds": {
      "s42_mmlu": 0.4061,
      "s123_mmlu": 0.3944,
      "s456_mmlu": 0.4198,
      "uniform_mmlu_mean": 0.4068,
      "uniform_mmlu_std": 0.0127
    },
    "global_s456_mmlu": 0.4382,
    "uniform_ppl": {
      "s42": 8.8157,
      "s123": 8.8308,
      "s456": 8.7947,
      "mean": 8.8137,
      "std": 0.0181
    },
    "uniform_arc": {
      "s42": 0.4078,
      "s123": 0.4531,
      "s456": 0.4505
    },
    "uniform_winogrande": {
      "s42": 0.6859,
      "s123": 0.6938,
      "s456": 0.6875
    }
  }
}
```

Key findings:
- MMLU 0.4198 is marginally above the predicted 0.38-0.42 range but close enough to confirm consistency. Uniform 3-seed MMLU std = **0.013**, very tight.
- PPL is the **best** across all 3 uniform seeds (8.7947 vs 8.8157/8.8308), with near-zero variance (std=0.018).
- ARC and WinoGrande also consistent across seeds.
- Compared to global allocation s456 (MMLU=0.4382), uniform is ~2pp lower on MMLU but dramatically more stable across seeds, which is the core claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "metrics": {
      "wikitext2_ppl": 8.7947,
      "arc_challenge_acc_norm": 0.4505,
      "winogrande_acc": 0.6875,
      "mmlu_acc": 0.4198,
      "gsm8k_exact_match": 0.0758,
      "actual_sparsity": 0.3,
      "allocation": "uniform"
    },
    "conclusion": "success",
    "analysis": "s456 uniform MMLU=0.4198 is slightly above s42/s123 range but uniform 3-seed std=0.013, far tighter than global allocation's observed 0.25-0.44 spread, confirming uniform allocation provides consistent cross-seed MMLU",
    "comparison": {
      "uniform_seeds": {
        "s42_mmlu": 0.4061,
        "s123_mmlu": 0.3944,
        "s456_mmlu": 0.4198,
        "uniform_mmlu_mean": 0.4068,
        "uniform_mmlu_std": 0.0127
      },
      "global_s456_mmlu": 0.4382,
      "uniform_ppl": {
        "s42": 8.8157,
        "s123": 8.8308,
        "s456": 8.7947,
        "mean": 8.8137,
        "std": 0.0181
      },
      "uniform_arc": {
        "s42": 0.4078,
        "s123": 0.4531,
        "s456": 0.4505
      },
      "uniform_winogrande": {
        "s42": 0.6859,
        "s123": 0.6938,
        "s456": 0.6875
      }
    }
  }
}
```

</details>

---
