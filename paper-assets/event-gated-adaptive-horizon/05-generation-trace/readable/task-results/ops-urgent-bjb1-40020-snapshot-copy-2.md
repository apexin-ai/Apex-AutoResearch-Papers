# ops urgent bjb1 40020 snapshot

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_bjb1_40020_snapshot_20260520T165240_result.json`
- **Structured JSON:** [`958c69095d52acdca7da.json`](../../sessions/95/958c69095d52acdca7da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== exp_029a (σ=0.2 s1) ===
PID: EXITED (50924)
最新 step: 224K (target 210K ✓)
最新 eval_return:
  175K=159.0  185K=278.2  195K=301.2  205K=204.6  215K=161.3
最新 ve_ratio:
  175K=0.214  185K=0.121  195K=0.108  205K=0.150  215K=0.186
NVE max: 0.643 @55K — 全程 <1.0×, CIVO 抑制成功
Registry: 已是 DONE/success，checkpoint_path + log_path 已设置，无需更新

=== exp_029c (σ=0.1 s0) ===
PID: RUNNING (59395, 5h10m, Ss+)
最新 step: 152K / 210K target (72%)
最新 eval_return:
  105K=204.7  115K=296.4  125K=232.3  135K=247.4  145K=323.1
最新 ve_ratio:
  105K=0.80  115K=0.45  125K=0.49  135K=0.40  145K=0.27
⚠️ NVE max: 1.022 @95K（微超 1.0×），之后持续下降至 0.27
Registry: RUNNING, current_step 已更新至 152K

=== GPU ===
cuda:0: 17% util, 3043/24564 MiB — PID 59400 (python, 3025 MiB) ← exp_029c
cuda:1: 0% util, 1/24564 MiB — 空闲
```

---
