# ops c4 data download

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c4_data_download_20260515T223821_result.json`
- **Structured JSON:** [`8ae970988bef434badcd.json`](../../sessions/8a/8ae970988bef434badcd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 报告

**1. C4 validation 数据状态**
- 路径：`/root/autodl-tmp/data/c4_val` (arrow 格式)
- 样本数：364,608
- 磁盘占用：783MB
- 原始 json.gz 也缓存在 hub cache：`/root/autodl-tmp/.hf_cache/hub/datasets--allenai--c4/`（~311MB，8 个文件）

**2. 离线验证结果**
- `load_from_disk` 离线加载：通过
- `data_utils.get_eval_dataset("c4", ...)` 离线加载：通过（200 samples → 132 packed sequences）
- 已 patch `data_utils.py`：C4 优先从本地 arrow 数据加载，不依赖网络

**3. 代码改动**
- `/root/distill_sparse_swiglu/src/data_utils.py`：
  - 添加 `import os`
  - `get_eval_dataset` 和 `get_calibration_loader` 的 C4 分支：优先检查 `/root/autodl-tmp/data/c4_val` 本地路径，存在则用 `load_from_disk`，否则回退到 streaming 模式

---
