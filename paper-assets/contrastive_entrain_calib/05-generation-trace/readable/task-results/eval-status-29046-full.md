# eval status 29046 full

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_status-29046-full_20260522T185152_result.json`
- **Structured JSON:** [`c4fa50035e21bd46295c.json`](../../sessions/c4/c4fa50035e21bd46295c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-29046 Status ===
GPU0: 占用 38197MiB/97887MiB, 95% util, PID 516696 (python) — exp-003-gs8
GPU1: 占用 23279MiB/97887MiB, 40% util, PID 494017 (python) — exp-004-s2-v2

exp-003-gs8 (exp003_gs8_r3only): step 38/8000, ~66s/step
  最新日志时间: 2026-05-23 00:37:53 (约2h前)
  注意: WARNING "d_syc not loaded; returning R3-only rewards" 每步都在报
  ckpt-500: NOT_YET — 还需 ~462 steps × 66s ≈ 8.5h (预计 ~11:20)
  已 SCP 到 28034: NO (ckpt 未生成)

exp-004-s2-v2: step 5160/8000, step_time=9.1s, ETA ≈ 7.2h (~10:05)
  total_loss=0.000109, l2_loss=0.00106, sft_loss=3e-06
  ckpt-5000: EXISTS (2026-05-23 02:26, adapter_model.safetensors 666MB)
```

两个要注意的点：

1. **exp-003-gs8 才跑到 step 38**，看起来是刚启动不久，ckpt-500 最快要 ~8.5h 后才有。日志里 WARNING `d_syc not loaded` 每步都出现——不确定这是否符合预期（R3-only 模式）。

2. **exp-004-s2-v2 的 ckpt-5000 已就绪**，需要 SCP 到别处吗？

---
