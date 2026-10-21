# harvest eval pi05 random k05 spatial seed42 postfix v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_pi05_random_k05_spatial_seed42_postfix_v2_20260524T010502_result.json`
- **Structured JSON:** [`46dc4355040d6550d000.json`](../../sessions/46/46dc4355040d6550d000.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

**eval_pi05_random_k05_spatial_seed42_postfix_v2**: 再次崩溃（连续第2次）

- **崩溃原因**: `httpx.ConnectError: [Errno 101] Network is unreachable` — tokenizer `google/paligemma-3b-pt-224` 加载时尝试联网。`TRANSFORMERS_OFFLINE=1` 无效，因为调用链经过 `lerobot → huggingface_hub`，需要 `HF_HUB_OFFLINE=1`
- **与 pre-fix 对比**: 无法对比，seed42 spatial 未产出结果
- **参考**: seed43 已有结果 72.4%（May 23），与 pre-fix 71.6% 接近
- **Registry**: 已更新为 DONE/failed

**下一步**: 如需重试（v3），启动命令需加 `HF_HUB_OFFLINE=1`（参考同服务器上 `eval_pi05_random_k085_spatial_seed42_postfix` 的命令格式，该实验已正确设置此变量）

**westd-41074 GPU 状态**: GPU 0/1/2 空闲（0% utilization），GPU 3 在用（39%）。GPU 2 可用。

---
