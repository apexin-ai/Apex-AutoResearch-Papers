# analysis exp004 ckpt5000 ckpt7000 eval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004-ckpt5000-ckpt7000-eval_20260520T150909_result.json`
- **Structured JSON:** [`7f54cb46be367e2dfe05.json`](../../sessions/7f/7f54cb46be367e2dfe05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-004 ACT Baseline — ckpt5000 & ckpt7000 Unified Eval Results

```json
{
  "exp004_ckpt5000": {
    "ToF": 0.1547,
    "NoF": 0.8785,
    "SYCONScore": 0.2631,
    "n_valid": 181,
    "n_invalid": 181,
    "n_total": 362,
    "eval_time_seconds": 1305
  },
  "exp004_ckpt7000": {
    "ToF": 0.1713,
    "NoF": 0.8619,
    "SYCONScore": 0.2858,
    "n_valid": 181,
    "n_invalid": 181,
    "n_total": 362,
    "eval_time_seconds": 1254
  }
}
```

### vs Vanilla Baseline (SYCONScore=0.1335, ToF=0.072, NoF=0.945)

| Checkpoint | SYCONScore | Δ vs Vanilla | % Change | ToF | NoF |
|---|---|---|---|---|---|
| ckpt-5000 | 0.2631 | +0.1296 | +97.1% | 0.1547 | 0.8785 |
| ckpt-7000 | 0.2858 | +0.1523 | +114.1% | 0.1713 | 0.8619 |

### 完整 ACT Trajectory（更新后）

| Steps | SYCONScore | ToF | NoF |
|---|---|---|---|
| 500 | 0.1699 | — | — |
| 1000 | 0.2048 | 0.116 | 0.8729 |
| 2000 | 0.2550 | 0.1492 | 0.8785 |
| 4000 | 0.2140 | 0.1215 | 0.8950 |
| **5000** | **0.2631** | **0.1547** | **0.8785** |
| 6000 | 0.2618 | 0.1547 | 0.8508 |
| **7000** | **0.2858** | **0.1713** | **0.8619** |
| 8000 | 0.3013 | 0.1823 | 0.8674 |

ckpt-5000 和 ckpt-7000 填补了 trajectory 中的空缺。整体趋势：SYCONScore 从 ckpt-4000 的低谷（0.214）回升，经 5000→6000→7000→8000 持续上升至 0.3013，NoF 同步下降（模型越来越愿意 flip）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp004_ckpt5000": {
      "ToF": 0.1547,
      "NoF": 0.8785,
      "SYCONScore": 0.2631,
      "n_valid": 181,
      "n_invalid": 181,
      "n_total": 362,
      "eval_time_seconds": 1305
    },
    "exp004_ckpt7000": {
      "ToF": 0.1713,
      "NoF": 0.8619,
      "SYCONScore": 0.2858,
      "n_valid": 181,
      "n_invalid": 181,
      "n_total": 362,
      "eval_time_seconds": 1254
    }
  }
}
```

</details>

---
