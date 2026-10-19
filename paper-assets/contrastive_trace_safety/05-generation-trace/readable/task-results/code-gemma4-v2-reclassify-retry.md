# code gemma4 v2 reclassify retry

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma4_v2_reclassify_retry_20260522T162702_result.json`
- **Structured JSON:** [`dda556e2d226bf6f9499.json`](../../sessions/dd/dda556e2d226bf6f9499.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Gemma-4 v2 Reclassify Results

### v1 → v2 Label Distribution Change

| | v1 | v2 | Delta |
|---|---|---|---|
| Jailbreak | 295 | 14 | -281 |
| Safe | 225 | 506 | +281 |
| Total | 520 | 520 | — |

**285/520 labels changed** (54.8%). The v2 classifier (final-response-only + threshold>=1 + 5 new phrases) massively reclassified: most v1 "jailbreaks" were caught by refusal phrases in the thinking block that v1 counted but v2 ignores (it only checks after `&lt;channel|>`).

### Best Layer Table (v2)

| Metric | Layer | Depth% | Window | Value |
|---|---|---|---|---|
| Bal. accuracy | L1 | 2.4% | W15 | 0.748 |
| Precision | L7 | 17.1% | W15 | 0.500 |
| Inv. FPR | L13 | 31.7% | W15 | 0.007 |
| CR-composite | L1 | 2.4% | W5 | 0.014 |
| AUROC | L1 | 2.4% | W15 | 0.966 |
| Crossing rate | L0 | 0.0% | W5 | 0.019 |

### Divergence

**14.7pp** (composite L1 @ 2.4% vs precision L7 @ 17.1%) — **NOT replicated** (threshold >15pp).

### Analysis

The extreme class imbalance (14 JB / 506 safe = 2.7% JB rate) makes this result unreliable — with only ~3 JB traces in the test split, crossing rates collapse to near-zero and precision is noisy. The AUROC (0.966) is high at L1 suggesting the model signals are there, but there's simply not enough jailbreak data to produce stable metric-level layer divergence. The 14.7pp divergence misses the >15pp replication threshold by 0.3pp, but with N_JB=14 the confidence interval is wide.

The v1 classifier was counting refusal phrases in the thinking block (inflating JB count to 295), making the v1 results misleading. The v2 result is methodologically correct but statistically underpowered for Gemma-4 on AdvBench — it nearly universally refuses.

---
