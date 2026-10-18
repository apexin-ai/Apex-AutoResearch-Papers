# ops westd41074 kill spatial download pi05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-kill-spatial-download-pi05_20260521T022232_result.json`
- **Structured JSON:** [`7ca3d18d2581072b8302.json`](../../sessions/7c/7ca3d18d2581072b8302.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 结果

1. **Kill**: PID 724539 (cuda:1, 16477 MiB) 已 force kill。GPU 1 现已空闲。其他 GPU 未受影响（GPU 0: PID 659206, GPU 2: PID 68539, GPU 3: PID 68852 正常运行）。

2. **π0.5 checkpoint**: 已下载完成（可能之前的 Worker 已完成），路径 `/root/autodl-tmp/pi05_libero_finetuned/`。

3. **验证**:
   - 总大小: **8.0GB**
   - 无 `.aria2` 残留文件
   - 核心文件: `model.safetensors` (6.0GB), `config.json`, `train_config.json`, preprocessor/postprocessor 文件齐全

---
