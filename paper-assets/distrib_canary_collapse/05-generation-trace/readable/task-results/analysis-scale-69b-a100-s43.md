# analysis scale 69b a100 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scale_69b_a100_s43_20260520T075602_result.json`
- **Structured JSON:** [`4eed2c6ba7d656b0dac9.json`](../../sessions/4e/4eed2c6ba7d656b0dac9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果如下：

## scale_69b_a100_s43 — D120 Canonical 5-Method Analysis

```json
{
  "experiment": "scale_69b_a100_s43",
  "model": "EleutherAI/pythia-6.9b",
  "dataset": "wikitext-103-v1",
  "alpha": 1.0,
  "seed": 43,
  "generations": 11,
  "bf16": true,
  "gradient_checkpointing": true,

  "metrics": {
    "PermG_fwd": "6/8",
    "PermG_rev": "0/8",
    "diff_xcorr_fdr": "6/8",
    "naive_xcorr": "6/8",
    "threshold_onset": "0/8",
    "TY_granger": "0/8",
    "K_ge3": "6/8",
    "K_ge4": "0/8"
  },

  "consensus_detail": {
    "token_entropy<distinct_1": "3/5 [naive, diff, perm]",
    "token_entropy<distinct_2": "3/5 [naive, diff, perm]",
    "token_entropy<distinct_3": "3/5 [naive, diff, perm]",
    "token_entropy<mauve":      "0/5",
    "ece<distinct_1":           "3/5 [naive, diff, perm]",
    "ece<distinct_2":           "3/5 [naive, diff, perm]",
    "ece<distinct_3":           "3/5 [naive, diff, perm]",
    "ece<mauve":                "0/5"
  },

  "checkpoint_path": "/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia69b_wiki_a100_s43/gen_10/checkpoint/",
  "analysis_path": "/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia69b_wiki_a100_s43/analysis/5method_leadlag.json",
  "server": "westd-17855"
}
```

## s42 vs s43 对比

| Metric | s42 (parent) | s43 | Delta |
|--------|:---:|:---:|:---:|
| PermG_fwd | 7/8 | 6/8 | -1 |
| PermG_rev | 0/8 | 0/8 | = |
| diff_xcorr_fdr | 6/8 | 6/8 | = |
| naive_xcorr | 5/8 | 6/8 | +1 |
| threshold_onset | 2/8 | 0/8 | -2 |
| TY_granger | 1/8 | 0/8 | -1 |
| **K≥3** | **5/8** | **6/8** | **+1** |
| K≥4 | 0/8 | 0/8 | = |

**要点**：
- 核心三方法（PermG + diff_xcorr + naive_xcorr）在 6 个 distinct_* pair 上高度一致，跨 seed 稳定
- mauve pair 两个 seed 均 0/5，信号弱
- threshold_onset 从 2→0：s43 的 downstream 指标未触发 true 3σ 阈值（canary onset 在 gen_2 但 downstream onset 为 null）
- TY 继续不稳定（1→0），符合 C003 预期
- K≥3 从 5→6 提升，s43 的 naive_xcorr 在更多 pair 上与 diff/perm 一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "scale_69b_a100_s43",
    "model": "EleutherAI/pythia-6.9b",
    "dataset": "wikitext-103-v1",
    "alpha": 1.0,
    "seed": 43,
    "generations": 11,
    "bf16": true,
    "gradient_checkpointing": true,
    "metrics": {
      "PermG_fwd": "6/8",
      "PermG_rev": "0/8",
      "diff_xcorr_fdr": "6/8",
      "naive_xcorr": "6/8",
      "threshold_onset": "0/8",
      "TY_granger": "0/8",
      "K_ge3": "6/8",
      "K_ge4": "0/8"
    },
    "consensus_detail": {
      "token_entropy<distinct_1": "3/5 [naive, diff, perm]",
      "token_entropy<distinct_2": "3/5 [naive, diff, perm]",
      "token_entropy<distinct_3": "3/5 [naive, diff, perm]",
      "token_entropy<mauve": "0/5",
      "ece<distinct_1": "3/5 [naive, diff, perm]",
      "ece<distinct_2": "3/5 [naive, diff, perm]",
      "ece<distinct_3": "3/5 [naive, diff, perm]",
      "ece<mauve": "0/5"
    },
    "checkpoint_path": "/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia69b_wiki_a100_s43/gen_10/checkpoint/",
    "analysis_path": "/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia69b_wiki_a100_s43/analysis/5method_leadlag.json",
    "server": "westd-17855"
  }
}
```

</details>

---
