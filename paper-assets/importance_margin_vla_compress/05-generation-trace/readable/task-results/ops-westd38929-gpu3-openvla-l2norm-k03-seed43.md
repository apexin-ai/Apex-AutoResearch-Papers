# ops westd38929 gpu3 openvla l2norm k03 seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-gpu3-openvla-l2norm-k03-seed43_20260521T121236_result.json`
- **Structured JSON:** [`9fb64cc0465cdd9c4349.json`](../../sessions/9f/9fb64cc0465cdd9c4349.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

- **PID**: 195275（运行中）
- **GPU**: westd-38929 GPU3, `CUDA_VISIBLE_DEVICES=3`
- **状态**: 正在执行 libero_object task 1/10，L2 pruning 256→76 vision tokens (k=0.3)
- **日志**: `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_l2norm_k03_object_seed43.log`
- **Registry**: `eval_openvla_l2norm_k03_object_seed43` → RUNNING

注意：脚本不接受 `--device` 参数，已去掉，仅用 `CUDA_VISIBLE_DEVICES=3` 控制 GPU。

---
