# prep exp012 model check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp012_model_check_20260515T153754_result.json`
- **Structured JSON:** [`585076483a02d9749474.json`](../../sessions/58/585076483a02d9749474.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

AWQ 下载 5.0GB/~35GB，速率约 ~1GB/min。48GB 剩余空间。

---

## 状态报告

### 模型可用性

| 模型 | 状态 | 路径 |
|------|------|------|
| Llama-3.3-70B-Instruct-FP8 (主模型) | **exists** ✓ | `/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/` (15 shards, 完整) |
| Meta-Llama-3.1-70B-Instruct-AWQ-INT4 (fallback) | **downloading** | PID 285069, 5.0GB/~35GB, ~30min 剩余 |
| Llama-3.1-8B-Instruct | **missing** | 未缓存，磁盘空间受限（48GB），不建议同时下载 |

### flashinfer / CUDA

| 组件 | 版本 | 状态 |
|------|------|------|
| flashinfer-python | 0.6.11.post2 | ⚠️ 与 cubin 版本不匹配 |
| flashinfer-cubin | 0.6.8.post1 | ⚠️ 升级失败（镜像 hash 错误 + pypi.org 过慢） |
| **workaround** | `FLASHINFER_DISABLE_VERSION_CHECK=1` | **已加入脚本** ✓ |
| vLLM | 0.20.2 | OK |
| PyTorch | 2.11.0+cu130 | OK, CUDA=True, 1 GPU |
| CUDA_HOME | `/root/miniconda3/.../nvidia/cu13` | 路径存在 ✓ |
| nvidia-cuda-nvcc | 13.2.78 | OK |

### 磁盘

- `/root/autodl-tmp/`: 250GB total, 203GB used, **48GB free** (81%)
- AWQ 下载完成后预计剩余 ~13GB

### 修改

- `scripts/run_exp012_llama.sh`：本地和服务器均已添加 `export FLASHINFER_DISABLE_VERSION_CHECK=1`

### 待监控

- AWQ 下载进程 PID 285069，可用以下命令检查：
  ```bash
  du -sh /root/autodl-tmp/.hf_cache/llama-3.1-70b-instruct-awq-int4/.cache/
  ls /root/autodl-tmp/.hf_cache/llama-3.1-70b-instruct-awq-int4/*.safetensors 2>/dev/null | wc -l
  ```

---
