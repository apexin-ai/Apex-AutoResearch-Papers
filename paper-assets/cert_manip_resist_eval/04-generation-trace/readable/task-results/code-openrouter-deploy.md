# code openrouter deploy

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openrouter-deploy_20260522T125604_result.json`
- **Structured JSON:** [`3d49b4faf00524625b84.json`](../../sessions/3d/3d49b4faf00524625b84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

import 验证通过。汇报：

**api_judge_service.py 修改：**
- L35: 新增 `_OPENROUTER_MODEL_MAP` 映射表（9 个模型）
- L93: 默认 `api_base` → `https://openrouter.ai/api/v1`
- L111-112: session headers 新增 `HTTP-Referer` 和 `X-Title`
- L125: `_call_api` 中 model 字段改用 `_OPENROUTER_MODEL_MAP.get(self.model_id, self.model_id)`，`self.model_id` 本身不变

**run_plan001_step1_batched.py 修改：**
- L31: `API_KEY` → `os.environ["OPENROUTER_API_KEY"]`（删除硬编码 key）
- L32: `API_BASE` → `https://openrouter.ai/api/v1`
- L38-51: 三个 batch 的 `max_workers` 全部改为 3，`max_rps` 全部改为 3.0

**import 验证：通过**

设置 `OPENROUTER_API_KEY` 环境变量后即可启动 scoring。

---
