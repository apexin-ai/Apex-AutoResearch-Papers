# ops fp16 download setup

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fp16-download-setup_20260525T103533_result.json`
- **Structured JSON:** [`d65d82b709df1f8c1114.json`](../../sessions/d6/d65d82b709df1f8c1114.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 模型下载状态

| 模型 | FP16 状态 | AWQ 状态 | FP16 路径 | AWQ 路径 |
|------|----------|---------|----------|---------|
| Qwen2.5-7B | ❌缺失→⏳下载中 | ❌缺失→⏳下载中 | (下载到 modelscope_cache) | (下载到 modelscope_cache) |
| Qwen2.5-14B | ⚠️不完整(6/8 shards)→⏳补全中 | ✅完整 9.4GB | `.../Qwen2___5-14B-Instruct` | `.../Qwen2___5-14B-Instruct-AWQ` |
| Qwen2.5-32B | ⚠️不完整(15/17 shards)→⏳补全中 | ✅完整 19GB | `.../Qwen2___5-32B-Instruct` | `.../Qwen2___5-32B-Instruct-AWQ` |
| Qwen2.5-72B | ❌缺失，**磁盘不足(需~140GB)** | ❌缺失→⏳下载中 | 无法下载 | (下载到 modelscope_cache) |
| Llama-3.1-8B | ✅完整 30GB | ⚠️不完整(1/2 in temp)→⏳补全中 | `.../Meta-Llama-3___1-8B-Instruct` | `.../Meta-Llama-3___1-8B-Instruct-AWQ-INT4` |
| Mistral-7B-v0.3 | ❌缺失→⏳下载中 | ❌缺失→⏳下载中 | `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3` | `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3-AWQ` |

> 所有 ModelScope 路径前缀: `/root/autodl-tmp/modelscope_cache/`

## 启动的 nohup 下载

| 模型 | PID | 日志路径 | 来源 |
|------|-----|---------|------|
| Qwen2.5-14B FP16 补全 | 80512 | `/tmp/download_qwen14b_fp16.log` | ModelScope |
| Qwen2.5-32B FP16 补全 | 80606 | `/tmp/download_qwen32b_fp16.log` | ModelScope |
| Llama-3.1-8B AWQ 补全 | 80699 | `/tmp/download_llama8b_awq.log` | ModelScope |
| Qwen2.5-7B FP16 | 80806 | `/tmp/download_qwen7b_fp16.log` | ModelScope |
| Qwen2.5-7B AWQ | 80909 | `/tmp/download_qwen7b_awq.log` | ModelScope |
| Qwen2.5-72B AWQ | 81023 | `/tmp/download_qwen72b_awq.log` | ModelScope |
| Mistral-7B FP16 | 81175 | `/tmp/download_mistral7b_fp16.log` | HuggingFace |
| Mistral-7B AWQ | 81214 | `/tmp/download_mistral7b_awq.log` | HuggingFace |

## 磁盘状态

- **数据盘** `/root/autodl-tmp`: 167GB / 250GB 已用，**84GB 可用**
- **系统盘** `/root`: 9.2GB / 30GB 已用，21GB 可用

## 风险提醒

1. **Qwen2.5-72B FP16 (~140GB) 无法下载**——磁盘空间不足，需清理或换更大磁盘
2. 8 个并发下载预计总新增 ~93GB，与可用 84GB 接近。72B AWQ (~40GB) 可能导致磁盘满——如果空间不足会自动失败，不会损坏已有模型
3. **Mistral-7B AWQ repo `TheBloke/Mistral-7B-Instruct-v0.3-AWQ` 可能不存在**，需检查日志确认。备选: `solidrust/Mistral-7B-Instruct-v0.3-AWQ`
4. HF cache 中的旧残余文件 (~130MB) 已部分清理 .incomplete 文件，目录结构保留

---
