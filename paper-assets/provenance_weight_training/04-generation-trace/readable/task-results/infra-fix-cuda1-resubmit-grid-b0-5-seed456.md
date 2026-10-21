# infra fix cuda1 resubmit grid b0 5 seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_cuda1_resubmit_grid_b0_5_seed456_20260514T211606_result.json`
- **Structured JSON:** [`354536cd1d37fe216c34.json`](../../sessions/35/354536cd1d37fe216c34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。四块 GPU 全部正常运行：

| GPU | 实验 | PID | 显存 |
|-----|------|-----|------|
| cuda:0 | grid_b_seed42_batch | 129259 | 46514 MiB |
| cuda:1 | **grid_b0_5_seed456** (重提交) | **144400** | 46514 MiB |
| cuda:2 | grid_b1_0_seed456 | 142907 | 46514 MiB |
| cuda:3 | grid_b1_5_seed456 | 142990 | 46514 MiB |

残留进程已清理，grid_b0_5_seed456 已在 cuda:1 上正常启动（6103 steps, GPU-Util 99%）。

---
