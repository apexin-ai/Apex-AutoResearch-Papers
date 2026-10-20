# ops urgent bjb1 45299 snapshot deploy

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_bjb1_45299_snapshot_deploy_20260520T162648_result.json`
- **Structured JSON:** [`5dd7ab0ec43c7983295b.json`](../../sessions/5d/5dd7ab0ec43c7983295b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

```
=== exp_030b (Cheetah σ=0.5) ===
PID: exited（已 kill，超 220K 未自退）
最新 step: 215K（eval）/ 220K+（training metrics）
最新 eval: step=215K → 77.6
最新 NVE: step=215K → 0.1394
Registry: DONE/negative ✓

=== exp_031 (PickCube σ=0.2) ===
PID 908459: running（03:44:47+）
最新 step: 72.5K
eval_return 全量:
  2.5K=2.4, 12.5K=19.2, 22.5K=17.7, 32.5K=11.5,
  42.5K=7.8, 52.5K=4.8, 62.5K=10.4, 72.5K=16.2
NVE 全量:
  12.5K=0.20, 22.5K=1.01, 32.5K=2.29, 42.5K=3.06,
  52.5K=3.71, 62.5K=1.20, 72.5K=0.55

=== exp_030c (Cheetah σ=1.0) ===
部署状态: 成功 ✓
PID: 920973（tmux session: exp_030c_tcn_cheetah_s0_sigma10）
Registry: RUNNING

=== GPU ===
cuda:0: 28% util, 3942/97887 MiB（exp_030c PID 920973, 3255 MiB）
cuda:1: 18% util, 2767/97887 MiB（exp_031 PID 908464, 2758 MiB）
```

---
