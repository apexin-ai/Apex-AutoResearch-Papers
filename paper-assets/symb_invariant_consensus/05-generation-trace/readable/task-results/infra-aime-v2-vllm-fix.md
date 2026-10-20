# infra aime v2 vllm fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_aime-v2-vllm-fix_20260515T154811_result.json`
- **Structured JSON:** [`45a9206ee3a75e3b72d9.json`](../../sessions/45/45a9206ee3a75e3b72d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功恢复。

**诊断结果：**
- **根因**：`VLLMGenerator` 的 OpenAI client 使用默认 600s 超时，k=12 用 `n=12` 批量请求时，12 个 trace（各 max 10240 tokens）共享 GPU 吞吐，总生成时间超过 600s → 客户端超时 → 重试发新请求 → 旧请求仍在跑 → KV cache 堆积到 99% → 恶性循环
- **vLLM 状态**：进程存活，GPU 100%，但被废弃的旧请求占满 KV cache

**修复操作：**
1. `sica/trace_generator.py`：OpenAI client timeout 从默认 600s → 1800s（sync + async 均已修改）
2. Kill 卡住的实验进程（PID 121144）和旧 vLLM（PID 102693）
3. 重启 vLLM（清除积压请求）
4. `--resume` 从 Problem 5 继续，跳过已完成的前 4 题

**当前状态**：实验 PID 129992 正在跑 Problem 5（aime2024_II_05），26 题剩余。

---
