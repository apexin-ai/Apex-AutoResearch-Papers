# analyze eval pi05 random k085 spatial seed42 postfix v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k085_spatial_seed42_postfix_v2_20260524T050603_result.json`
- **Structured JSON:** [`aef5e30e818b75342885.json`](../../sessions/ae/aef5e30e818b75342885.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE. 

```
RESULT:
- overall_sr: 60.8%
- per_task: T0=84%, T1=68%, T2=92%, T3=16%, T4=66%, T5=28%, T6=44%, T7=76%, T8=82%, T9=52%
- total_episodes: 500 (10 tasks × 50 eps, all complete)
- anomalies: 无
- comparison: baseline(k=1.0)=78%, this(k=0.85)=60.8%, delta=-17.2pp
- disruption_peak_in_spatial: NO
```

**结论 (success)**：Spatial suite 无 disruption peak。Random k=0.85 从 78% 降至 60.8%（-17.2pp），属中度退化，远非 Object suite 的灾难性崩塌（82% → 5.6%，-76pp）。

值得注意：T3(16%) 和 T5(28%) 退化严重，说明 random pruning 对某些需要精细空间定位的 task 仍有显著影响，但整体不构成 disruption peak 现象。

---
