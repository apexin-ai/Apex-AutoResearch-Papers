# infra exp052 053 manual deploy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp052-053-manual-deploy_20260518T234259_result.json`
- **Structured JSON:** [`873058c65b4cc5c4f214.json`](../../sessions/87/873058c65b4cc5c4f214.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现关键问题：

- **cuda:2 (port 8002)**: 已有 Mistral-7B vLLM 在运行，且似乎空闲（`exp-046-mistral-pw600` session 内容为空）。可直接复用给 exp-052。
- **cuda:3 (port 8003)**: 运行 Qwen3-14B vLLM，`exp028b` 正在活跃使用（持续发请求）。

**需要你确认**：
1. cuda:2 的 Mistral-7B vLLM (port 8002) 可以直接复用给 exp-052？
2. cuda:3 的 exp028b + Qwen3-14B 可以 kill 掉来腾出给 exp-053？还是需要等 exp028b 完成？

另外 `exp033_run` 和 `exp035_run` 已完成（显示 FULL_MVP_DONE），可以清理。`exp034_run` 看起来还在跑。

---
