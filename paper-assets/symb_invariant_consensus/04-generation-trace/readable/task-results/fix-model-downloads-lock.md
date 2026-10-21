# fix model downloads lock

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_model-downloads-lock_20260516T082128_result.json`
- **Structured JSON:** [`916fe2f5a84a3dfe5e0c.json`](../../sessions/91/916fe2f5a84a3dfe5e0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-001 (PID 181491) 正常运行，未受影响。

---

**完成。结果汇总：**

| 模型 | 最终路径 | 大小 | 验证 |
|------|----------|------|------|
| Mistral-7B-Instruct-v0.3 | `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/mistralai/Mistral-7B-Instruct-v0___3/` | 5.75 GB (3 shards) | vocab=32768, hidden=4096, 32 layers |
| LLaMA-3.1-8B-Instruct | `/root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct/` | 5.83 GB (4 shards) | vocab=128000, hidden=4096, 32 layers |

**操作：**
- 进程已死，safetensors 完整但卡在 `._____temp` → 直接移到最终目录
- 清除 `.lock` 目录和 `._____temp` 残留
- Tokenizer + config 加载验证通过
- 创建 `scripts/start_vllm_mistral_7b.sh` (port 8001)
- `scripts/start_vllm_llama_8b.sh` (port 8002) 路径已正确，无需修改
- exp-001 (PID 181491) 未受影响

exp-010 和 exp-011 可以启动了。

---
