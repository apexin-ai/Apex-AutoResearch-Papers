# ops c4ext eval migrate cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c4ext-eval-migrate-cqa1_20260520T081109_result.json`
- **Structured JSON:** [`cae208d473f203091eda.json`](../../sessions/ca/cae208d473f203091eda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full eval is running on westd-38929.

**Summary:**
- **Server**: westd-38929, GPU 0 (RTX PRO 6000 Blackwell, 98GB)
- **PID**: 89467 (python process), 89459 (wrapper)
- **Config**: `openvla_sc_m128` checkpoint step 20000, LIBERO-Object, 10 tasks × 50 episodes, seed 42
- **Log**: `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_sc_m128_vtconly_20k_seed42.log`
- **Output**: `eval_results/eval_openvla_sc_m128_vtconly_20k_seed42.json`
- **Speed**: ~8.4 min/episode (280 steps × ~1.8s/step worst case), ~500 episodes total
- **ETA**: ~50-70 hours (~May 22-23)
- **Registry**: `eval_openvla_sc_m128_20k_seed42` → RUNNING

2-episode test confirmed pipeline works end-to-end (both episodes ran to 280 steps, logged correctly, JSON output valid). The full eval is now running autonomously via nohup.

---
