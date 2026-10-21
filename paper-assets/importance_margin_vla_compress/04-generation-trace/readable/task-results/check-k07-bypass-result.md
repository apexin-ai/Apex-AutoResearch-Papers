# check k07 bypass result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_k07_bypass_result_20260517T035909_result.json`
- **Structured JSON:** [`c285192069b91ae638d6.json`](../../sessions/c2/c285192069b91ae638d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**k=0.7 bypass eval 失败了。**

- **错误**: `torch.AcceleratorError: CUDA error: invalid device ordinal`
- **原因**: 启动时设了 `CUDA_VISIBLE_DEVICES=1`（进程内只可见 1 块 GPU 映射为 `cuda:0`），但脚本又指定 `--device cuda:1`，导致找不到设备
- **修复**: 重跑时用 `CUDA_VISIBLE_DEVICES=1 python eval_... --device cuda:0`，或去掉 `CUDA_VISIBLE_DEVICES` 直接用 `--device cuda:1`

Registry 已更新为 `conclusion: failed`。需要我现在重新提交 eval 吗？

---
