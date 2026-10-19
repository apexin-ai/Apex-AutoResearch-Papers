# infra llama full probe

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_llama_full_probe_20260521T190238_result.json`
- **Structured JSON:** [`5a57a95b3c16476b4aab.json`](../../sessions/5a/5a57a95b3c16476b4aab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

```
[Llama-3.1-8B MVP Gate Verdict]

=== EN→EN (within-language baseline) ===
Peak: 77.6% (layer 28)
Binomial p: 7.99e-21
Permutation p: 0.000

=== ZH→ZH (within-language Chinese) ===
Peak: 72.1% (layer 13)
Binomial p: 1.09e-13
Permutation p: 0.000

=== EN→ZH (cross-lingual transfer) ===
Peak: 59.6% (layer 5)
Binomial p: 9.66e-04
Permutation p: 0.001

=== ZH→EN (cross-lingual transfer) ===
Peak: 71.3% (layer 15)
Binomial p: 7.11e-13
Permutation p: 0.000

Gate Criteria:
- EN acc ≥ 80%: FAIL (77.6%)
- ZH transfer binomial p < 0.01: PASS (EN→ZH: 9.66e-04, ZH→EN: 7.11e-13)
- ZH transfer point > 60%: CONDITIONAL (EN→ZH: 59.6% FAIL, ZH→EN: 71.3% PASS)
- Layer-wise structure (≥1 layer ≥ 65%, perm p < 0.01): PASS (ZH→EN has 5 layers ≥ 65%, best layer 15 perm p=0.000)

Overall: CONDITIONAL

Notes:
- EN→EN baseline narrowly misses 80% gate (77.6%), but is highly significant
- Cross-lingual transfer is asymmetric: ZH→EN (71.3%) is strong, EN→ZH (59.6%) is weak
- ZH→EN shows robust layer-wise structure with 5 layers ≥ 65% (layers 9, 15, 25, 27, 28)
- EN→ZH transfer only barely exceeds chance at its peak (59.6%), suggesting the EN probe doesn't generalize well to ZH test data

输出文件:
- data/llama31/probe_results.json
- data/llama31/probe_accuracy_by_layer.png
```

---
