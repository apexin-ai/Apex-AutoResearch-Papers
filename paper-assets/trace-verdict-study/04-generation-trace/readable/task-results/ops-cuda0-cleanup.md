# ops cuda0 cleanup

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0_cleanup_20260515T102102_result.json`
- **Structured JSON:** [`5f4415353cf995c6060d.json`](../../sessions/5f/5f4415353cf995c6060d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到原因：**PID 87061 (ae_only) 同时持有 `/dev/nvidia1` (GPU 0 的设备文件)**。49GB 是 ae_only 进程初始化时在 GPU 0 上分配的显存（可能是模型加载时先到了 GPU 0 再转移到 GPU 1，但显存未释放）。

**无法在不 kill ae_only 的情况下释放 GPU 0 上的 49GB。**

## 清理结果

### 任务 1: GPU 0 显存
- **无法清理**。49GB 由 ae_only 进程 (PID 87061) 持有，该进程同时打开了 `/dev/nvidia1`(GPU 0) 和 `/dev/nvidia3`(GPU 1)
- GPU reset 不支持，且内存绑定在运行中的进程上
- GPU 0 剩余可用：**~48.7GB**（97.9GB - 49.2GB）

### 任务 2: 下载进程 ✓
- 已 kill：PID 89975, 89991, 90120, 90404, 90409（旧 v1 Worker 的 modelscope/huggingface 下载）
- 保留：PID 90582/90587（v2 Worker 的 ModelScope 下载）

### 任务 3: 当前状态
| GPU | 已用 | 可用 | 进程 |
|-----|------|------|------|
| cuda:0 | 49.2GB | **48.7GB** | 无计算进程（ae_only 持有上下文） |
| cuda:1 | 41.3GB | 56.6GB | PID 87061 ae_only (100% util) |

**DeepSeek-Coder-6.7B 训练可行性**：48.7GB 可用空间足够用 QLoRA 训练 6.7B 模型（4-bit 量化约需 ~15-20GB）。如果需要完整 97GB，则必须等 ae_only 结束或手动 kill 它。

---
