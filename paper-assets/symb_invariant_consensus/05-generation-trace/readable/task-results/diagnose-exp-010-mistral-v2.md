# diagnose exp 010 mistral v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-010-mistral-v2_20260517T055243_result.json`
- **Structured JSON:** [`d26eca7e90f83d604d50.json`](../../sessions/d2/d26eca7e90f83d604d50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。产出已写入 `artifacts/exp-010-mistral-v2/diagnosis.md`。

**总结：**

| | v2 | v1 |
|---|---|---|
| 死因 | 外部 SIGTERM（GPU 被 Qwen2.5-14B 占用，13:51 提交时 pilot-constraint-filtering 仍在跑） | vLLM 忽略 `--max-model-len 8192`，实际用 4096，所有请求 400 |
| 可用结果 | 无 | 26 条空壳记录（0% accuracy），不可用 |

**重跑需要修两处：**
1. 确保 GPU 空闲再提交
2. 降 `--max-tokens` 为 2048（或换 `python -m vllm.serve` 新入口确保 8192 生效）

---
