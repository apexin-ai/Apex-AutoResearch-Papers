# research eval lost in conversation

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_eval-lost-in-conversation_20260518T055049_result.json`
- **Structured JSON:** [`251dcf0969b0fc0f76df.json`](../../sessions/25/251dcf0969b0fc0f76df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/eval_lost_in_conversation_report.md` 并注册。核心发现：

**数据集**: 627 样本，6 种任务，shard 数 3-12。shard >= 5 子集 509 条（code 91, math 81）。

**指标**: P̄/A⁹⁰/U₁₀⁹⁰ **不在仓库代码中**，是论文级 post-hoc 指标，需从 JSONL trace 自行计算。仓库只记录 per-conversation 的 `is_correct` 和 `score`。

**评估方法**:
- Code: **pass@1 执行评估**，forked subprocess（非安全沙盒），AST 提取代码
- Math: **字符串精确匹配**（GSM8K 风格 normalize 后），无数值容差

**对话模拟**: 3-agent 架构（User Agent LLM 逐轮透露 shard + Assistant 被测模型 + System Agent LLM 判断/提取答案）。不是固定模板，User Agent 是 LLM 驱动的。

**本地适配**: 最小改动路径只需改 `model_openai.py`（~50-100 行），assistant 本地推理 + system/user agent 保持 API。3 GPU 并行 + vLLM，7B 模型全量评估（600 x N=10）预计 10-20 小时。

---
