# train openvla vtc lora westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_openvla_vtc_lora_westd41074_20260519T182506_result.json`
- **Structured JSON:** [`23088a5a04b6c8802129.json`](../../sessions/23/23088a5a04b6c8802129.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Task complete. Training `train_openvla_sc_m128_lora_seed42` verified running on westd-41074:cuda:1.

**Status summary:**

| Check | Result |
|-------|--------|
| PID 30737 alive | Yes |
| GPU 1 utilization | 95%, 31.6GB VRAM |
| Log errors | None |
| Step 0 | loss=18.09, grad=887 |
| Step 50 | loss=4.98, grad=35.7, sps=0.6 |
| Registry | RUNNING, retry_count=1 |

At sps=0.6, 100K steps ≈ 46 hours. Both experiments (VTC-only on cuda:0, VTC+LoRA on cuda:1) running in parallel on westd-41074 with no resource contention issues.

---
