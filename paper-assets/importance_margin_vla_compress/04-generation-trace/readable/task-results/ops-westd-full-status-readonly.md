# ops westd full status readonly

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_full_status_readonly_20260520T012546_result.json`
- **Structured JSON:** [`d10094ab24b4e95e176c.json`](../../sessions/d1/d10094ab24b4e95e176c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-41074 ===
C4-ext: PID=26118 [ALIVE] step=14500/100K loss=3.22 sps=0.6 运行6h53m
  cmdline: python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m128.yaml
  log_path: /root/runs/importance_margin_vla_compress/train_openvla_sc_m128_seed42.log
磁盘: 85G/250G free (67% used), C5 checkpoint [DELETED], LoRA [DELETED]
GPU 0: C4-ext 30108 MiB, 53°C, 176W
GPU 1: 空闲 (0 MiB)
GPU 2: 空闲 (0 MiB)
GPU 3: 空闲 (0 MiB)

=== westd-27271 ===
M=32 VTC-only: PID=855140 [ALIVE] step=2250/100K loss=3.26 sps=0.5 运行1h10m
VTC+LoRA M=128: PID=841334 [ALIVE] step=12900/100K loss=3.17 sps=0.5 运行6h48m
磁盘: 91G/250G free (64% used)
GPU 0: VTC+LoRA 32276 MiB, 38°C, 182W
GPU 1: M=32 VTC-only 25942 MiB, 37°C, 187W, util 96%
```

---
