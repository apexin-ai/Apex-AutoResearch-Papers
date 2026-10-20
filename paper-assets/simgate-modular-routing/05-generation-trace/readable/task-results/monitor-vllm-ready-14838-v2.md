# monitor vllm ready 14838 v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_vllm-ready-14838-v2_20260517T131651_result.json`
- **Structured JSON:** [`f029ee41f2d31766675c.json`](../../sessions/f0/f029ee41f2d31766675c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**READY**

两个 vLLM 端口均已就绪：

| 端口 | 状态 | 模型 | max_model_len |
|------|------|------|---------------|
| 8000 (cuda:2) | OK | Qwen2.5-7B-Instruct | 32768 |
| 8001 (cuda:3) | OK | Qwen2.5-7B-Instruct | 32768 |

解决过程中的问题：
1. 原始 safetensors 文件损坏（ModelScope 下载不完整，文件大小与 index 不符）→ 用 ModelScope 重新下载
2. FlashInfer 不支持 Blackwell GPU (SM 12.0) → 设置 `VLLM_USE_FLASHINFER_SAMPLER=0` 绕过
3. vLLM 版本：0.21.0，torch：2.11.0+cu130

---
