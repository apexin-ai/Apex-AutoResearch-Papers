# diagnose dying experiments 20260524

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_dying_experiments_20260524_20260524T050620_result.json`
- **Structured JSON:** [`65322cbb496b13670e31.json`](../../sessions/65/65322cbb496b13670e31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

```
exp_id: eval_openvla_random_k05_goal_seed42
status: completed_normally
last_log_lines: Overall SR: 0.5220 (261/500) | Time: 230.7 min | Saved: openvla_random_prune_k05_goal_seed42.json
result: SR = 52.2%
action_taken: registry updated → conclusion=success, metrics recorded

exp_id: eval_pi05_l2norm_k05_spatial_seed43_v2
status: completed_normally
last_log_lines: RESULT: libero_spatial prune=l2norm keep=0.5 SR=55.4% | EXIT_CODE=0 | Saved: pi05_l2norm_k0.50_libero_spatial_seed43.json
result: SR = 55.4%
action_taken: registry updated → conclusion=success, metrics recorded
```

两个实验都是正常完成后进程退出，被 cron 误判为 failed。已将 registry 从 failed 修正为 success 并录入 metrics。

---
