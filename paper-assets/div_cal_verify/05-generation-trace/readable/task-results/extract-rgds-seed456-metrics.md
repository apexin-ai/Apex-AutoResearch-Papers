# extract rgds seed456 metrics

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_rgds_seed456_metrics_20260513T232223_result.json`
- **Structured JSON:** [`ae6816ce236e0bb139ed.json`](../../sessions/ae/ae6816ce236e0bb139ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已包含 rgds_seed456 的完整数据（metrics、conclusion、checkpoint_path、log_path 全部已设置），无需再次更新。

```
=== rgds_seed456 Metrics ===
Gen 0: ppl=36.70, rankme=274.06, knn=0.988, rare=0.0284, corr=-0.0138, ratio=0.9114
Gen 1: ppl=44.59, rankme=291.76, knn=0.988, rare=0.0189, corr=-0.0418, ratio=0.8895
Gen 2: ppl=45.30, rankme=290.79, knn=0.988, rare=0.0139, corr=-0.0356, ratio=0.9071
Gen 3: ppl=49.13, rankme=289.92, knn=0.988, rare=0.0111, corr=-0.0403, ratio=0.8774
Gen 4: ppl=47.40, rankme=287.04, knn=0.988, rare=0.0098, corr=-0.0342, ratio=0.8292
Gen 5: ppl=55.99, rankme=290.71, knn=0.988, rare=0.0078, corr=-0.0269, ratio=0.7065
Gen 6: ppl=55.99, rankme=287.52, knn=0.988, rare=0.0065, corr=-0.0247, ratio=0.6447
Gen 7: ppl=66.22, rankme=286.54, knn=0.988, rare=0.0069, corr=-0.0228, ratio=0.8682

Verification:
  Gen 7 PPL = 66.22 ✓ (ref: 66.22, delta=0%)
  Gen 7 ratio = 0.8682 ✓ (ref: 0.868, delta=0.02%)

Registry status: ALL FIELDS ALREADY SET (metrics, conclusion="success",
  checkpoint_path="/root/autodl-tmp/div_cal_verify/results_seed456/rgds/rgds/gen_7/checkpoint/",
  log_path="/root/autodl-tmp/div_cal_verify/rgds_seed456.log")

=== medium_rgds_seed42 Progress ===
Current: Gen 6/7, step 3/5 (training), method=rgds

=== medium_external Status ===
Running: yes (tmux session: chain_cuda1)
Log: /root/autodl-tmp/div_cal_verify/medium_external.log
Current: Gen 0/7, step 3/5 (training), method=external_only
```

---
