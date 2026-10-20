# analysis variance statistics — Part 2 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-variance-statistics.md) · [Structured JSON](../../../sessions/88/887993f7e63d0a8f5b7d.json)

## Before a recorded user message

### Tool result

_source line 101 · 2026-05-23T01:27:52.270Z_

<details><summary>↩ Tool result · `toolu_019QmA2PKJ9TaKW9pNb2jDCs`</summary>

```text
## Sign test

4/4 scales: SFT_std > RSFT_std
Binomial p-value (one-sided, H0: p≤0.5): 0.0625
Binomial p-value (two-sided): 0.1250
Note: 14B excluded (n=1 for both SFT/RSFT, std undefined)

## χ² 95% CI for standard deviations

| Scale     | n_SFT | SFT_std (pp) | SFT_std 95% CI (pp)    | n_RSFT | RSFT_std (pp) | RSFT_std 95% CI (pp)   |
|-----------|-------|--------------|------------------------|--------|---------------|------------------------|
| 1.7B      |     3 |         2.79 | [    1.45,    17.55] |      3 |          0.09 | [    0.04,     0.54] |
| 4B        |     3 |         3.80 | [    1.98,    23.89] |      3 |          0.51 | [    0.27,     3.21] |
| 8B        |     3 |         3.23 | [    1.68,    20.31] |      3 |          0.50 | [    0.26,     3.15] |
| LLaMA-8B  |     3 |         2.92 | [    1.52,    18.37] |      3 |          0.64 | [    0.33,     4.01] |

Compression ratios:
  1.7B      : 32.6×
  4B        : 7.5×
  8B        : 6.5×
  LLaMA-8B  : 4.6×

## Cohen's d (SFT mean vs RSFT mean)

| Scale     | SFT_mean (pp) | RSFT_mean (pp) | Δ (pp) | pooled_std (pp) | Cohen's d | Effect      |
|-----------|---------------|----------------|--------|-----------------|-----------|-------------|
| 1.7B      |         44.64 |          51.19 | +6.54 |            1.98 |     +3.31 | large       |
| 4B        |         43.58 |          44.82 | +1.24 |            2.71 |     +0.46 | small       |
| 8B        |         50.19 |          54.33 | +4.14 |            2.31 |     +1.79 | large       |
| LLaMA-8B  |         51.09 |          56.54 | +5.45 |            2.12 |     +2.58 | large       |

## Raw per-seed data

| Scale     | SFT s42  | SFT s43  | SFT s44  | RSFT s42 | RSFT s43 | RSFT s44 |
|-----------|----------|----------|----------|----------|----------|----------|
| 1.7B      | 0.4786 | 0.4286 | 0.4321 | 0.5122 | 0.5109 | 0.5125 |
| 4B        | 0.3974 | 0.4365 | 0.4734 | 0.4423 | 0.4512 | 0.4511 |
| 8B        | 0.5051 | 0.5324 | 0.4681 | 0.5376 | 0.5471 | 0.5451 |
| LLaMA-8B  | 0.5384 | 0.5142 | 0.4802 | 0.5714 | 0.5662 | 0.5587 |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4af931fe-946a-4832-a5aa-ef15be99c0ed",
  "uuid": "7b501789-1294-4d73-b677-b6fd7e30864a",
  "tool_use_result": {
    "stdout": "## Sign test\n\n4/4 scales: SFT_std > RSFT_std\nBinomial p-value (one-sided, H0: p≤0.5): 0.0625\nBinomial p-value (two-sided): 0.1250\nNote: 14B excluded (n=1 for both SFT/RSFT, std undefined)\n\n## χ² 95% CI for standard deviations\n\n| Scale     | n_SFT | SFT_std (pp) | SFT_std 95% CI (pp)    | n_RSFT | RSFT_std (pp) | RSFT_std 95% CI (pp)   |\n|-----------|-------|--------------|------------------------|--------|---------------|------------------------|\n| 1.7B      |     3 |         2.79 | [    1.45,    17.55] |      3 |          0.09 | [    0.04,     0.54] |\n| 4B        |     3 |         3.80 | [    1.98,    23.89] |      3 |          0.51 | [    0.27,     3.21] |\n| 8B        |     3 |         3.23 | [    1.68,    20.31] |      3 |          0.50 | [    0.26,     3.15] |\n| LLaMA-8B  |     3 |         2.92 | [    1.52,    18.37] |      3 |          0.64 | [    0.33,     4.01] |\n\nCompression ratios:\n  1.7B      : 32.6×\n  4B        : 7.5×\n  8B        : 6.5×\n  LLaMA-8B  : 4.6×\n\n## Cohen's d (SFT mean vs RSFT mean)\n\n| Scale     | SFT_mean (pp) | RSFT_mean (pp) | Δ (pp) | pooled_std (pp) | Cohen's d | Effect      |\n|-----------|---------------|----------------|--------|-----------------|-----------|-------------|\n| 1.7B      |         44.64 |          51.19 | +6.54 |            1.98 |     +3.31 | large       |\n| 4B        |         43.58 |          44.82 | +1.24 |            2.71 |     +0.46 | small       |\n| 8B        |         50.19 |          54.33 | +4.14 |            2.31 |     +1.79 | large       |\n| LLaMA-8B  |         51.09 |          56.54 | +5.45 |            2.12 |     +2.58 | large       |\n\n## Raw per-seed data\n\n| Scale     | SFT s42  | SFT s43  | SFT s44  | RSFT s42 | RSFT s43 | RSFT s44 |\n|-----------|----------|----------|----------|----------|----------|----------|\n| 1.7B      | 0.4786 | 0.4286 | 0.4321 | 0.5122 | 0.5109 | 0.5125 |\n| 4B        | 0.3974 | 0.4365 | 0.4734 | 0.4423 | 0.4512 | 0.4511 |\n| 8B        | 0.5051 | 0.5324 | 0.4681 | 0.5376 | 0.5471 | 0.5451 |\n| LLaMA-8B  | 0.5384 | 0.5142 | 0.4802 | 0.5714 | 0.5662 | 0.5587 |",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 102_

<details><summary>Logged reasoning block</summary>

```text
The results are complete. Let me check if the task mentioned "5/5 scales" - it did. But 14B only has 1 seed, so std is undefined. The task description was probably written before verifying the actual data availability.

However, there's one thing I can note: if we consider the claim that "SFT std > RSFT std" and we include 14B as "vacuously true" because with n=1 both stds are undefined and we can't compute, we might still want to mention 4/4. Or alternately, if we include 14B with some caveat, 5/5.
 
Looking at the statistical evidence more carefully: the sign test across the four scales with sufficient data shows SFT has higher standard deviation than RSFT, though the p-value of 0.0625 (one-sided) falls just short of significance. The confidence intervals for SFT are wider due to smaller sample sizes, but they consistently exceed RSFT's bounds, with no overlap for the 1.7B model. Most scales also show large effect sizes by Cohen's d.

Now I'm checking the compression ratios against the paper's reported values—the 1.7B model shows 32.6× compared to the paper's 31×, which could stem from rounding differences or slight variations in the exact ignore_f1 values used in the calculations. The standard deviation I calculated is 0.086pp, which matches the paper's reported 0.09pp when rounded. This gives a compression ratio of about 32.5× for the 1.7B model, though the paper reports 31× due to using rounded intermediate values. I should present the precise calculation rather than the rounded version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4af931fe-946a-4832-a5aa-ef15be99c0ed",
  "uuid": "cf32ba8f-15c0-4270-9470-916344425daf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015w9YU4f5U7fttPGt3KsA7b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3009,
      "cache_read_input_tokens": 118303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3009
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 103_

Results computed. Here's the final output:

---

## Sign test

4/4 scales: SFT_std > RSFT_std
- Binomial p-value (one-sided, H0: p≤0.5): **0.0625**
- Binomial p-value (two-sided): **0.1250**
- 14B excluded: n=1 for both SFT and RSFT, sample std undefined (ddof=1)
- Note: p=0.0625 is marginal. With 4 scales, even 4/4 cannot reach α=0.05 (minimum achievable = 2^{-4} = 0.0625). This is a power limitation of the sign test with small N, not evidence against the claim.

## χ² 95% CI for standard deviations

| Scale | n_SFT | SFT_std (pp) | SFT_std 95% CI (pp) | n_RSFT | RSFT_std (pp) | RSFT_std 95% CI (pp) | Compression |
|-------|-------|-------------|---------------------|--------|--------------|---------------------|-------------|
| 1.7B | 3 | 2.79 | [1.45, 17.55] | 3 | 0.09 | [0.04, 0.54] | 32.6× |
| 4B | 3 | 3.80 | [1.98, 23.89] | 3 | 0.51 | [0.27, 3.21] | 7.5× |
| 8B | 3 | 3.23 | [1.68, 20.31] | 3 | 0.50 | [0.26, 3.15] | 6.5× |
| LLaMA-8B | 3 | 2.92 | [1.52, 18.37] | 3 | 0.64 | [0.33, 4.01] | 4.6× |

CIs are wide (df=2 gives broad chi-squared tails), but 1.7B CIs are fully non-overlapping (SFT lower=1.45 > RSFT upper=0.54). For 4B/8B/LLaMA, SFT lower bound exceeds RSFT point estimate by 3-4×, though CIs technically overlap at the tails.

## Cohen's d (SFT mean vs RSFT mean)

| Scale | SFT_mean (pp) | RSFT_mean (pp) | Δ (pp) | pooled_std (pp) | Cohen's d | Effect |
|-------|--------------|----------------|--------|----------------|-----------|--------|
| 1.7B | 44.64 | 51.19 | +6.54 | 1.98 | +3.31 | large |
| 4B | 43.58 | 44.82 | +1.24 | 2.71 | +0.46 | small |
| 8B | 50.19 | 54.33 | +4.14 | 2.31 | +1.79 | large |
| LLaMA-8B | 51.09 | 56.54 | +5.45 | 2.12 | +2.58 | large |

Direction: positive d = RSFT mean > SFT mean. 3/4 scales show **large** effect (d>0.8), 4B shows **small** effect (d=0.46). All positive — RSFT consistently improves mean while compressing variance.

---

**Key caveat**: n=3 seeds per condition makes chi-squared CIs very wide and individual-scale significance tests underpowered. The strongest statistical argument is the **consistency across 4 independent scales** (sign test direction) combined with the **magnitude of compression** (4.6-32.6×), rather than any single-scale test.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4af931fe-946a-4832-a5aa-ef15be99c0ed",
  "uuid": "fb78b541-fb2e-463f-83d5-16f8943933f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015w9YU4f5U7fttPGt3KsA7b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3009,
      "cache_read_input_tokens": 118303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3009
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 104_

Results computed. Here's the final output:

---

## Sign test

4/4 scales: SFT_std > RSFT_std
- Binomial p-value (one-sided, H0: p≤0.5): **0.0625**
- Binomial p-value (two-sided): **0.1250**
- 14B excluded: n=1 for both SFT and RSFT, sample std undefined (ddof=1)
- Note: p=0.0625 is marginal. With 4 scales, even 4/4 cannot reach α=0.05 (minimum achievable = 2^{-4} = 0.0625). This is a power limitation of the sign test with small N, not evidence against the claim.

## χ² 95% CI for standard deviations

| Scale | n_SFT | SFT_std (pp) | SFT_std 95% CI (pp) | n_RSFT | RSFT_std (pp) | RSFT_std 95% CI (pp) | Compression |
|-------|-------|-------------|---------------------|--------|--------------|---------------------|-------------|
| 1.7B | 3 | 2.79 | [1.45, 17.55] | 3 | 0.09 | [0.04, 0.54] | 32.6× |
| 4B | 3 | 3.80 | [1.98, 23.89] | 3 | 0.51 | [0.27, 3.21] | 7.5× |
| 8B | 3 | 3.23 | [1.68, 20.31] | 3 | 0.50 | [0.26, 3.15] | 6.5× |
| LLaMA-8B | 3 | 2.92 | [1.52, 18.37] | 3 | 0.64 | [0.33, 4.01] | 4.6× |

CIs are wide (df=2 gives broad chi-squared tails), but 1.7B CIs are fully non-overlapping (SFT lower=1.45 > RSFT upper=0.54). For 4B/8B/LLaMA, SFT lower bound exceeds RSFT point estimate by 3-4×, though CIs technically overlap at the tails.

## Cohen's d (SFT mean vs RSFT mean)

| Scale | SFT_mean (pp) | RSFT_mean (pp) | Δ (pp) | pooled_std (pp) | Cohen's d | Effect |
|-------|--------------|----------------|--------|----------------|-----------|--------|
| 1.7B | 44.64 | 51.19 | +6.54 | 1.98 | +3.31 | large |
| 4B | 43.58 | 44.82 | +1.24 | 2.71 | +0.46 | small |
| 8B | 50.19 | 54.33 | +4.14 | 2.31 | +1.79 | large |
| LLaMA-8B | 51.09 | 56.54 | +5.45 | 2.12 | +2.58 | large |

Direction: positive d = RSFT mean > SFT mean. 3/4 scales show **large** effect (d>0.8), 4B shows **small** effect (d=0.46). All positive — RSFT consistently improves mean while compressing variance.

---

**Key caveat**: n=3 seeds per condition makes chi-squared CIs very wide and individual-scale significance tests underpowered. The strongest statistical argument is the **consistency across 4 independent scales** (sign test direction) combined with the **magnitude of compression** (4.6-32.6×), rather than any single-scale test.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 379977,
  "duration_api_ms": 373287,
  "num_turns": 39,
  "stop_reason": "end_turn",
  "session_id": "4af931fe-946a-4832-a5aa-ef15be99c0ed",
  "total_cost_usd": 2.00059875,
  "usage": {
    "input_tokens": 24,
    "cache_creation_input_tokens": 109471,
    "cache_read_input_tokens": 1572672,
    "output_tokens": 21098,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 109471,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1943,
        "cache_read_input_tokens": 118303,
        "cache_creation_input_tokens": 3009,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3009
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2424,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002499,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 24,
      "outputTokens": 21098,
      "cacheReadInputTokens": 1572672,
      "cacheCreationInputTokens": 109471,
      "webSearchRequests": 0,
      "costUSD": 1.99809975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2ae60ac2-6437-4a87-9635-c6e58059e751"
}
```

</details>

---
