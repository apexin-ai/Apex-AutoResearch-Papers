# ops urgent bjb1 40020 snapshot finalize

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_bjb1_40020_snapshot_finalize_20260520T164716_result.json`
- **Structured JSON:** [`c007eacd816a39f98a61.json`](../../sessions/c0/c007eacd816a39f98a61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== exp_029a (σ=0.2 s1) ===
进程: EXITED (PID 50924)
最终步数: 224K (train), 最后 eval @215K
checkpoint_path: /root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt
log_path: /root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/metrics.jsonl
日志最后（@215K eval）: eval_return=161.3, ve_ratio=0.1864, fps=7.3
eval 峰值: 401.0@125K | NVE max: 0.6428@55K | NVE final: 0.1864@215K — 全程 <1.0×
Registry: DONE/success ✓
Cron: 已不存在（此前已删除）

=== exp_029c (σ=0.1 s0) ===
PID 59395: RUNNING (Ss+, uptime 5h04m)
当前 step: ~148K (train), 最后 eval @145K

eval_return 完整:
  5K=35.6  15K=99.1  25K=140.7  35K=155.7  45K=160.9
  55K=254.8  65K=268.7  75K=295.5  85K=220.8  95K=188.6
  105K=204.7  115K=296.4  125K=232.3  135K=247.4  145K=323.1

ve_ratio 完整:
  15K=0.0306  25K=0.1606  35K=0.3162  45K=0.4807  55K=0.4368
  65K=0.5432  75K=0.6211  85K=0.9533  95K=1.0218  105K=0.7610
  115K=0.4514  125K=0.4899  135K=0.3995  145K=0.2667

⚠️ NVE 在 95K 短暂超 1.0 (1.0218)，之后回落，当前 0.2667@145K

=== GPU ===
cuda:0: 14% util, 3043/24564 MiB — PID 59400 (python, 3025 MiB) [exp_029c]
cuda:1: 0% util, 1/24564 MiB — 空闲
```

---
