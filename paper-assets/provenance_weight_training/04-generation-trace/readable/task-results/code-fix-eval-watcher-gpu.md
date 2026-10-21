# code fix eval watcher gpu

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_eval_watcher_gpu_20260514T123507_result.json`
- **Structured JSON:** [`8d874fe11fd86d2ee235.json`](../../sessions/8d/8d874fe11fd86d2ee235.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

新 watcher 运行正常，日志不再重复。

## 结果

**1. 修改内容：**
- 删除硬编码 `EVAL_GPU = "3"`，新增 `MIN_FREE_MB = 15000`
- 新增 `get_least_loaded_gpu()` 函数：优先读环境变量 `EVAL_GPU`，否则调 `nvidia-smi` 选显存占用最低的 GPU，异常时 fallback GPU 0
- GPU 选择从模块级移到 `run_eval()` 内每次 eval 前动态调用，确保总是选当前最空闲的 GPU
- 启动日志更新为显示动态选择策略

**2. 新进程 PID：** `99503`

**3. GPU 选择逻辑验证：**
- 日志确认 `GPU select: dynamic (least loaded) | env EVAL_GPU overrides`
- 每次 eval 执行时会打印 `Selected GPU X (used=YMB, free=ZMB)`
- 无异常显存占用（所有 GPU 均 ~46.5GB/97.9GB，各有 ~51GB 空余，远超 15GB 阈值）

---
