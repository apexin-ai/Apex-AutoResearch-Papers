# train smart compress m128 seed44 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_smart_compress_m128_seed44_v2_20260519T042644_result.json`
- **Structured JSON:** [`f268c217cfa48bf138e3.json`](../../sessions/f2/f268c217cfa48bf138e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并注册为 RUNNING。

**总结：**
- **环境**：PyTorch 2.8.0+cu128，依赖完整，无需修复
- **Config**：`smart_compress_m128_seed44.yaml` 已存在（M=128, seed=44）
- **训练**：已在 tmux session `train_m128_s44` 中启动，使用 cuda:1
  - step=0 loss=1.7947, grad=62.05
  - 目标 100K steps
- **Registry**：`train_smart_compress_m128_seed44` 状态已更新为 RUNNING

---
