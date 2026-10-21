# analysis padding robustness a100 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_padding_robustness_a100_s42_fp32_20260519T141915_result.json`
- **Structured JSON:** [`8de0c1c65c224a9c1123.json`](../../sessions/8d/8de0c1c65c224a9c1123.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== STRUCTURED RESULT ===
conclusion: success
checkpoint_path: /root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/a100_s42_fp32
metrics:
  permg_fwd_fdr: 6/8
  permg_rev_fdr: 0/8
  consensus_ge4: 6/8
  mmct_uniform_fwd: 6/8 (simple K≥4 proxy, no null distribution on this server)
  d1_drift_pct: -18.97%
  d2_drift_pct: -21.72%
  d3_drift_pct: -18.31%
  entropy_drift_pct: -63.57%
  gen0_d1: 0.09796
  gen10_d1: 0.07938
  gen0_entropy: 3.2342
  gen10_entropy: 1.1782
  gen0_ppl: 26.95
  gen10_ppl: 941.94
padding_impact_summary: padding_side 对 gen0 无影响（d1 差异 <0.03%，D093 预测的 gen0_d1≈0.092 未确认）；right-padding 使 d1 collapse 加剧约 10pp（-28.3% vs -19.0%），但 lead-lag 因果信号完全稳健（PermG fwd 6/8, rev 0/8, K≥4 6/8），定性结论不变。
```

---
