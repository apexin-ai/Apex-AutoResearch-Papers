# ops server cleanup

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-cleanup_20260515T084015_result.json`
- **Structured JSON:** [`ec41dd38fdbe91090de9.json`](../../sessions/ec/ec41dd38fdbe91090de9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Llama 模型下载状态：**未完成，碎片化**

模型文件散落在多个目录，不在预期路径 `meta-llama/Meta-Llama-3.1-8B-Instruct/`：

| 位置 | 内容 |
|------|------|
| `LLM-Research/Meta-Llama-3___1-8B-Instruct/` | shard 4/4 (1.1GB) + config/tokenizer |
| `._____temp/LLM-Research/Meta-Llama-3.1-8B-Instruct/` | shard 1-3 (共 ~13.5GB)，在 temp 目录 |
| `Meta-Llama-3.1-8B-Instruct/` | 仅 44MB，有 `tokenizer.json.aria2` 残留 |

4 个 safetensors 文件都存在但分散在不同目录。需要合并到一个目录并清理 temp 文件。

### 2. GPU 显存

| GPU | 清理前 | 清理后 |
|-----|--------|--------|
| cuda:0 | 0 MiB / 32607 MiB | 0 MiB / 32607 MiB |
| cuda:1 | 28283 MiB / 32607 MiB | **0 MiB / 32607 MiB** |

### 3. 已清理进程

- vLLM Qwen2.5-7B-Instruct (port 8001, CUDA_VISIBLE_DEVICES=1) — PID 359272, 359266 — 已 kill，cuda:1 显存已释放

### 4. Multi-model pilot 相关进程

- port 8000：无进程
- episode_level_collection.py：无进程

---
