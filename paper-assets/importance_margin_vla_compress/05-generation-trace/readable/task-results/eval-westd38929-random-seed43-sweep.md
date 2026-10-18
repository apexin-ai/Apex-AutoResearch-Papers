# eval westd38929 random seed43 sweep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_westd38929-random-seed43-sweep_20260520T181819_result.json`
- **Structured JSON:** [`78644668b1f9bd9a6e7b.json`](../../sessions/78/78644668b1f9bd9a6e7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`eval_openvla_libero.py` 不存在，服务器和本地都没有。

服务器上的 OpenVLA eval 脚本只有 3 个：
- `eval_openvla_acis_prune.py` — ACIS pruning
- `eval_openvla_smart_compress.py` — smart compress  
- `eval_openvla_l2norm_libero.py` — L2 norm pruning

Random pruning 脚本只有 SmolVLA 版本（`eval_random_prune_smolvla.py`），没有 OpenVLA 版本。

需要先创建 `eval_openvla_libero.py`（OpenVLA random pruning），还是用现有脚本替代？

---
