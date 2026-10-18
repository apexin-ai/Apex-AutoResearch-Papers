# infra proxy restore and test

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_proxy-restore-and-test_20260522T130206_result.json`
- **Structured JSON:** [`e4f499865e29d50c425b.json`](../../sessions/e4/e4f499865e29d50c425b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 旧 API key
找到了：`tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8`（多个旧脚本中一致）

### 2. 脚本回滚
完成。修改内容：
- `API_KEY` → 硬编码旧 key（原为 `os.environ["OPENROUTER_API_KEY"]`）
- `API_BASE` → `http://47.94.22.126/v1`（原为 `https://openrouter.ai/api/v1`）
- 三个 BATCHES 的 `max_workers` → 1，`max_rps` → 1.0（原为 3 / 3.0）
- `api_judge_service.py` 未改动（脚本传参覆盖）

### 3. 代理测试结果

| Provider | Model | HTTP Code | Latency |
|----------|-------|-----------|---------|
| Claude | claude-3-haiku | 200 | 11.7s |
| OpenAI | gpt-4o-mini | 200 | 18.4s |
| Gemini | gemini-2.5-flash | 200 | 16.1s |

**PROXY RECOVERED，可以启动 scoring。**

注意：代理延迟偏高（11-18s），实际 scoring 中 timeout=120s 应该足够，但 max_workers=1 + max_rps=1.0 意味着吞吐量很低，300 samples × 7 conditions × 9 models 会比较耗时。

---
