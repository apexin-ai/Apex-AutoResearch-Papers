# analyze eval pi05 l2norm k09 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k09_spatial_seed42_20260522T010321_result.json`
- **Structured JSON:** [`8353b51235dde6c45ebc.json`](../../sessions/83/8353b51235dde6c45ebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No W&B run ID in the log.

```
RESULT_SUMMARY:
overall_sr: 95.0
total_successes: 475
total_episodes: 500
elapsed_min: 60.3
per_task_sr: {
  T0 "pick up the black bowl between the plate": 98.0,
  T1 "pick up the black bowl next to the ramekin": 98.0,
  T2 "pick up the black bowl from table center": 98.0,
  T3 "pick up the black bowl on the cookie box": 92.0,
  T4 "pick up the black bowl in the top drawer": 88.0,
  T5 "pick up the black bowl on the ramekin": 90.0,
  T6 "pick up the black bowl next to the cookie box": 100.0,
  T7 "pick up the black bowl on the stove": 94.0,
  T8 "pick up the black bowl next to the plate": 100.0,
  T9 "pick up the black bowl on the wooden cabinet": 92.0
}
log_path: ~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k09_spatial_seed42.log
checkpoint_path: /root/autodl-tmp/pi05_libero_finetuned
result_json_path: /root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.90_libero_spatial_seed42.json
wandb_run_id: N/A
status: success
notes: 正常完成，EXIT_CODE=0。Overall SR=95.0% vs baseline 97.2%，差距仅 2.2pp，符合预期（k=0.9 只移除 10% token）。最弱 task 是 T4 "top drawer"（88%），最强 T6/T8（100%）。
```

---
