# code fix async extraction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-async-extraction_20260515T111651_result.json`
- **Structured JSON:** [`aac86c0fd9935e332083.json`](../../sessions/aa/aac86c0fd9935e332083.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

测试完成。结果：

**修改内容：**
1. `VLLMBackend` 和 `APIBasedLLM` 的 `batch_call` 从 asyncio 改为 `ThreadPoolExecutor`（无 event loop 错误）
2. 删除了 `import asyncio`、`AsyncOpenAI`、`async_call`、`nest_asyncio` 依赖
3. `VLLMBackend.max_tokens` 默认 2048 → 1024
4. `APIBasedLLM.max_tokens` 默认 8192 → 1024
5. 两个类的 `__init__` 都接受 `max_tokens` 参数

**测试结果：**
- Backend: VLLMBackend, Model: QwQ-32B, max_tokens: 1024
- `batch_call` 3 个 prompt 并发执行，**45.0s** 完成（无 RuntimeError）
- 每个结果 3551-3896 chars（QwQ 仍有思考内容，但被 1024 token 限制截断，远比之前 ~700s/题快）
- 3 个请求并发而非串行，总时间约等于单次请求时间

---
