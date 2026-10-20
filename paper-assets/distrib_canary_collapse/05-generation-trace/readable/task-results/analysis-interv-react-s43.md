# analysis interv react s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_interv_react_s43_20260521T003501_result.json`
- **Structured JSON:** [`8d1fe62c7a471abf0a0f.json`](../../sessions/8d/8d1fe62c7a471abf0a0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== METRICS ===
trigger_gen: 2
trigger_distinct1_drop_pct: -15.83
gen0_distinct_1: 0.0983
gen0_ppl: 26.95
gen0_entropy: 3.234
gen_last_distinct_1: 0.0834
gen_last_ppl: 21.39
gen_last_entropy: 3.088
gen_last_ece: 0.0147
gen_last_mauve: 0.0276
recovery_complete_by_gen: 3
converges_to_alpha0_baseline: true
checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/intervention/reactive_d1_s43_fp32

=== COMPARISON vs s42 ===
trigger_gen: match (both Gen 2)
trigger_drop: match (-15.83% vs -15.58%)
gen2_ppl: match (158.22 vs 157.09)
recovery: match (Gen 3 vs Gen 4, s43 slightly faster)
final_metrics: match (ppl 21.39 vs 21.24, d1 0.0834 vs 0.0844)

=== CONCLUSION ===
conclusion: success
reason: s43 reproduces s42 — identical trigger point (Gen 2, ~-15.8% distinct_1 drop), PPL spike to ~158, recovery within 1 gen post-intervention (Gen 3), and convergence to α=0 baseline (~21.4 ppl). Cross-seed consistency confirmed.
```

注意：此次运行与已有 interv_react_s43_fp32 共享 output_dir 且数值完全一致（trigger_drop -15.83%、gen2_ppl 158.22、recovery_ppl 21.98），是同一组实验数据。

---
