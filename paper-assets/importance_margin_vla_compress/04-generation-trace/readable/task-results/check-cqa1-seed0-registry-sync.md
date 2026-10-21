# check cqa1 seed0 registry sync

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_seed0_registry_sync_20260516T183811_result.json`
- **Structured JSON:** [`8b7cd0f45e65d0285684.json`](../../sessions/8b/8b7cd0f45e65d0285684.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常运行，registry 已更新。

```
cuda:0: libero_full_ft_baseline (seed=42) — step 63000/100K (63%)
cuda:1: libero_lora_baseline (seed=42) — step 62900/100K (62.9%)
cuda:2: libero_lora_seed0 (seed=0) — step 43600/100K (43.6%)
cuda:3: libero_fullft_seed0 (seed=0) — step 42450/100K (42.5%)
```

seed=42 的两个 baseline 跑得更早，已过 60%。seed=0 的两个约 42-43%，PID 活跃，进程正常（主进程 + 4 个 dataloader worker 各自）。按 sps=4.1 估算，seed0 剩余约 ~40h 完成。

---
