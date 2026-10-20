# code prep exp011 llama script

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp011-llama-script_20260517T064352_result.json`
- **Structured JSON:** [`5ce44fa586f75b24864d.json`](../../sessions/5c/5ce44fa586f75b24864d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改摘要：

1. **vLLM 清理逻辑**：将原来只杀 port 8002 的 `pkill -f "vllm.entrypoints.*--port 8002"` 替换为通杀所有 vLLM 进程的 `pkill -9 -f "vllm.entrypoints"`，加 `sleep 5` 等待释放，并打印 GPU 显存状态。
2. **max-tokens**：从 8192 降为 4096（LLaMA-8B 生成不需要那么长）。
3. **max-model-len**：保持 8192（LLaMA-3.1 原生支持）。
4. **模型路径**：已确认 4 shards 完整存在。
5. **`bash -n` dry-run**：通过，无语法错误。

---
