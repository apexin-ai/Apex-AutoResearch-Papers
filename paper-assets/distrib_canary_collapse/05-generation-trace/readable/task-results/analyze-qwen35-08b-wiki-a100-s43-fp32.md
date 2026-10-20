# analyze qwen35 08b wiki a100 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen35_08b_wiki_a100_s43_fp32_20260520T080029_result.json`
- **Structured JSON:** [`d4b0e7656212c49d9bb1.json`](../../sessions/d4/d4b0e7656212c49d9bb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "PermG_fwd": "6/8",
  "PermG_rev": "0/8",
  "diff_xcorr_fdr": "6/8",
  "naive_xcorr": "6/8",
  "threshold_onset": "8/8",
  "TY_granger": "6/8",
  "K_ge3": "6/8",
  "K_ge4": "6/8",
  "d120_canonical": true,
  "notes": "mauve pairs weak: token_entropy->mauve K=1, ece->mauve K=1 (xcorr peak_lag=+1, direction filter correctly excluded). 6 distinct_* pairs all K=5/5. vs s42 (8/8 full sweep), s43 mauve non-monotonic (+6.42% drift) likely explains drop.",
  "checkpoint_path": "/root/autodl-tmp/distrib_canary_collapse/results/generalize/qwen35_08b_wiki_a100_s43_fp32/gen_10/checkpoint"
}
```

**Consensus detail per pair:**

| Pair | K | Methods |
|------|---|---------|
| token_entropy→distinct_1 | 5/5 | naive, diff, thresh, pg_fwd, ty |
| token_entropy→distinct_2 | 5/5 | naive, diff, thresh, pg_fwd, ty |
| token_entropy→distinct_3 | 5/5 | naive, diff, thresh, pg_fwd, ty |
| token_entropy→mauve | 1/5 | thresh |
| ece→distinct_1 | 5/5 | naive, diff, thresh, pg_fwd, ty |
| ece→distinct_2 | 5/5 | naive, diff, thresh, pg_fwd, ty |
| ece→distinct_3 | 5/5 | naive, diff, thresh, pg_fwd, ty |
| ece→mauve | 1/5 | thresh |

s43 vs s42 差异：mauve drift 仅 +6.42%（非单调），xcorr peak_lag=+1（反向），导致 mauve 两对被方向过滤器正确排除，K 从 s42 的 8/8 降至 6/8。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "PermG_fwd": "6/8",
    "PermG_rev": "0/8",
    "diff_xcorr_fdr": "6/8",
    "naive_xcorr": "6/8",
    "threshold_onset": "8/8",
    "TY_granger": "6/8",
    "K_ge3": "6/8",
    "K_ge4": "6/8",
    "d120_canonical": true,
    "notes": "mauve pairs weak: token_entropy->mauve K=1, ece->mauve K=1 (xcorr peak_lag=+1, direction filter correctly excluded). 6 distinct_* pairs all K=5/5. vs s42 (8/8 full sweep), s43 mauve non-monotonic (+6.42% drift) likely explains drop.",
    "checkpoint_path": "/root/autodl-tmp/distrib_canary_collapse/results/generalize/qwen35_08b_wiki_a100_s43_fp32/gen_10/checkpoint"
  }
}
```

</details>

---
