# diag mvp 001 download check

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mvp_001_download_check_20260520T143045_result.json`
- **Structured JSON:** [`1d65479817453872bcbe.json`](../../sessions/1d/1d65479817453872bcbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验已崩溃，进程不存在。** 以下是完整诊断：

### 1. 日志（最后 100 行）
实验以 `EXIT_CODE=1` 终止。崩溃栈：
- `extract_activations.py:126` → `AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")` 
- 根因：`RuntimeError: Cannot send a request, as the client has been closed.`（httpx 客户端断连）
- 最终报错：`OSError: Can't load the configuration of 'Qwen/Qwen2.5-7B-Instruct'`

**模型连 config.json 都没下到，在 tokenizer 加载阶段就挂了。**

### 2. HF cache
- `/root/.cache/huggingface/` — **不存在**
- `/root/autodl-tmp/.hf_cache/` — **不存在**
- `find /root -name "config.json" -path "*Qwen*"` — **无结果**

模型从未成功下载过任何文件。

### 3. GPU
4× NVIDIA RTX PRO 6000 Blackwell (98GB each)，全部空闲：0MiB 显存，0% 利用率，无 GPU 进程。

### 4. 进程
无 `run_mvp` 或 `extract_act` 相关进程。只有系统守护进程（supervisord、tensorboard、jupyter、sshd）。实验进程已退出。

### 5. network_turbo
`/etc/network_turbo` **存在但很可能未被 source**。这是 AutoDL 上访问 HuggingFace 的关键——不激活代理加速，HTTP 连接会失败。

### 6. 模型 blobs 目录
不存在。下载从未开始。

---

**结论**：mvp_001 在第一步（加载 tokenizer）就失败了，原因是 HuggingFace Hub 网络不通。最可能的原因是实验脚本启动前未执行 `source /etc/network_turbo`。模型从未下载，GPU 从未使用。需要修复启动脚本，在运行前激活网络加速，并设置 `HF_HOME=/root/autodl-tmp/.hf_cache` 避免根分区空间不足。

---
