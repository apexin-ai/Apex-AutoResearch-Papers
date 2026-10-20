# ops full gpu status check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_gpu_status_check_20260518T071527_result.json`
- **Structured JSON:** [`93f222f8fe744f7761a3.json`](../../sessions/93/93f222f8fe744f7761a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-30476 ===
cuda:0 — detect_remove_q05_seed123: [RUNNING] step 2439/8477 (29%) ETA ~27min
cuda:1 — detect_remove_q05_seed456: [RUNNING] step 2280/8477 (27%) ETA ~28min
cuda:2 — contamination_60_grid_b0_3_seed42: [RUNNING] step 1837/6103 (30%) ETA ~2h29m
cuda:3 — contamination_60_random_seed42: [RUNNING] step 1185/6103 (19%) ETA ~2h52m

=== westd-41312 ===
cuda:0 — contamination_60_ess_only_seed123: [RUNNING] step 1612/6103 (26%) ETA ~2h38m
cuda:1 — contamination_60_ess_only_seed456: [RUNNING] step 1611/6103 (26%) ETA ~2h38m
cuda:2 — contamination_60_random_seed123: [RUNNING] step 1089/6103 (18%) ETA ~2h56m
cuda:3 — contamination_60_random_seed456: [RUNNING] step 1089/6103 (18%) ETA ~2h56m
```

**注意**: detect_remove_q05 实验总步数是 **8477**（不是 6103），因为用的是 `scored_data_filtered_q05.jsonl` + `contamination_ratio=0.4`，数据集不同。这两个实验速度也快得多（~3.66 it/s vs ~2.10 s/it），约 30 分钟内完成。

所有 8 个实验均在正常运行，无异常。

---
