# ssh setup 30476 full

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_setup_30476_full_20260517T101827_result.json`
- **Structured JSON:** [`1306a6b145bcfe4e8c22.json`](../../sessions/13/1306a6b145bcfe4e8c22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks passed. Here's the summary:

---

## Setup Complete: westd-30476

| Item | Status |
|------|--------|
| **Python** | 3.12.3 (miniconda3) |
| **PyTorch** | 2.8.0+cu128 |
| **CUDA** | 12.8 (Driver 580.82.09) |
| **transformers** | 5.8.1 |
| **All imports** | OK (torch, transformers, datasets, accelerate, peft, safetensors) |
| **Code sync** | 32 .py files + all .sh scripts synced from 41312 |
| **Data sync** | 7.1G transferred (scored_data, mixed_data, filtered, hybrid, synthetic) |
| **Model** | Qwen3-0.6B loaded (596M params, vocab=151643) |
| **Output dir** | `/dev/shm/output/models` (220G tmpfs RAM disk) |
| **GPUs** | 4x NVIDIA RTX PRO 6000 Blackwell (102GB each), all free (0 MiB used) |
| **Disk** | 9.5G free on root overlay; checkpoints go to /dev/shm (220G) |

**Blockers:** None. Training can start immediately.

**Note:** Root disk is 69% full (9.5G free). All checkpoint output must use `/dev/shm/output/models` to avoid filling the root filesystem. The `/dev/shm` is RAM-backed (220G), so checkpoints are lost on reboot. Important results should be pulled off-server promptly.

---
