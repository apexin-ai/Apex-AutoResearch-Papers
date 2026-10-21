# gpu expand generators

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_expand_generators_20260521T093312_result.json`
- **Structured JSON:** [`bf280fa4aaf1307df3e9.json`](../../sessions/bf/bf280fa4aaf1307df3e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

### 当前 GPU 状态

| GPU | 占用 | 进程 |
|-----|------|------|
| cuda:0 | 13046 MiB / 32607 MiB | Pythia topk (PID 283041, 6186 MiB) + **Llama greedy (PID 347968, 6846 MiB)** |
| cuda:1 | 7594 MiB / 32607 MiB | OLMo topk (PID 283607, 3616 MiB) + Qwen greedy (PID 344399, 3964 MiB) |
| cuda:2 | 空闲 | — |
| cuda:3 | 空闲 | — |

### 新启动进程

| 模型 | PID | 日志 | 状态 |
|------|-----|------|------|
| **Llama-3.2-3B** | 347968 | `/tmp/gen_llama_decoding.log` | 已在 cuda:0 运行 greedy，~16s/it |
| **Mistral watcher** | 348289 | `/tmp/start_mistral_watcher.log` | 等待 OLMo (PID 283607) 结束后自动在 cuda:1 启动 Mistral-7B-v0.3 |

Mistral 日志将写入 `/tmp/gen_mistral_decoding.log`。脚本 `generate_chain_decoding.py` 已更新 MODEL_PATHS，新增 `llama-3.2-3b` 和 `mistral-7b-v0.3`。cuda:2/3 未使用。

---
