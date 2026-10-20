# analysis check object pipeline gpu

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_object_pipeline_gpu_20260521T011932_result.json`
- **Structured JSON:** [`44d62f9b45a46abad1a4.json`](../../sessions/44/44d62f9b45a46abad1a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 任务 1: LIBERO-Object Pipeline

| 项目 | 状态 |
|------|------|
| GPU 0 | RTX PRO 6000 (98GB), 15.1GB 显存占用, 0% util |
| GPU 1 | RTX PRO 6000 (98GB), 空闲 |
| tmux session | `libero_object_full_pipeline` 运行中 |
| PID | 513523, CPU 4041% (多线程 probing) |

**Pipeline 进度：**
- **Phase 1 (数据收集)**: 已完成，10/10 tasks，5000 samples，耗时 249.1s
- **Phase 2 (action R2 probing)**: 进行中，已输出第一层结果：
  - `L0: img_mean R2=0.6952  last_pre R2=0.5710`
  - 最后输出时间 09:14:49，当前 09:20，正在计算后续层，**正常运行中**

### 任务 2: NORA 下载

**NORA 环境:** venv 已创建 (`/root/autodl-tmp/vla-ssd/envs/nora/`)，PyTorch 仍在安装中（PID 508806，`pip install torch --index-url .../cu128`，已运行 ~53min）

**NORA 模型 (nora-libero-goal):** 4.8GB 已下载
- `model-00001-of-00002.safetensors`: 4.62GB — **完成**
- `model-00002-of-00002.safetensors`: 仅 60MB — **仍在下载**
- 有多个并发下载进程（HF direct + hf-mirror + wget），其中一个遇到 `ChunkedEncodingError`（连接中断）
- hf-mirror 进程 (PID 513278, 53% 8/15 files) 仍在继续

### 任务 3: LIBERO-Long (openvla-7b-oft-finetuned-libero-10)

| 项目 | 状态 |
|------|------|
| PID 513449 | **存活** |
| 已下载 | 817MB |
| 进度 | 12% (3/25 files) |
| 预计剩余 | ~1h37m |
| **问题** | `model-00002-of-00004.safetensors` 下载遇到 **ReadTimeoutError**（xethub cas-bridge 超时），正在自动重试 (1/5) |

### 需要关注的问题

1. **NORA PyTorch 安装耗时异常**（53min），可能卡住或网络极慢，建议检查
2. **NORA 模型下载有 3 个并发进程**在抢同一个文件，可能互相干扰
3. **LIBERO-Long 下载遇到 xethub 超时**，自动重试中，但 AutoDL 上 xethub 连接不稳定，若持续失败需要改用 `HF_HUB_DISABLE_XET=1` 或 hf-mirror

---
