# verify model downloads

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_model-downloads_20260516T112704_result.json`
- **Structured JSON:** [`5196b94e450a34837118.json`](../../sessions/51/5196b94e450a34837118.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

| 模型 | 状态 | 详情 |
|------|------|------|
| **DeepSeek-R1-Distill-Llama-8B** | ✅ COMPLETE | 2 shards (15GB), tokenizer OK (vocab=128000) |
| **LLaMA-3.1-8B-Instruct** | ✅ COMPLETE | 4 shards (14.9GB), tokenizer OK (vocab=128000) |
| **Mistral-7B-Instruct-v0.3** | ⏳ INCOMPLETE | safetensors 在 `._____temp/` 中，正在下载 (~78%, ETA ~40min) |

### 已执行修复

1. **杀死重复下载进程** — 之前有 3 个 Mistral + 2 个 LLaMA 下载进程同时跑，互相竞争带宽（~400KB/s）。已 kill 5 个重复进程，保留 PID 197995 继续 Mistral 下载。
2. **清理 LLaMA temp 残留** — 删除了 `._____temp/` 下 3.3GB 的无用临时文件。

### vLLM 脚本路径检查

- `start_vllm_mistral_7b.sh` (port 8001): 路径 `…/mistralai/Mistral-7B-Instruct-v0___3` ✓（下载完成后 ModelScope 会自动从 temp 移入）
- `start_vllm_llama_8b.sh` (port 8002): 路径 `…/LLM-Research/Meta-Llama-3___1-8B-Instruct` ✓
- `start_vllm_deepseek_r1_8b.sh` (port 8003): 路径 `/root/autodl-tmp/models/DeepSeek-R1-Distill-Llama-8B` ✓

### 待办

- Mistral 下载完成后验证：safetensors 是否从 `._____temp` 移至最终路径，tokenizer 是否可加载。预计 ~40 分钟后完成（去掉竞争进程后速度应提升）。

---
