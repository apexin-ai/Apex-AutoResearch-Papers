# research check logprobs

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check-logprobs_20260517T120129_result.json`
- **Structured JSON:** [`9c987092dfc7fa542f1b.json`](../../sessions/9c/9c987092dfc7fa542f1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**数据中是否有 logprobs：否**

Episode 数据（`episodes.jsonl`、`labeled_steps.jsonl`、`episode_details.jsonl`）只记录了 step-level 的 action、score、observation 等信息，没有任何 logprobs/token_probs 相关字段。LLM 的原始输出文本（raw ReAct output）也未被保存到数据中。

**代码中 vLLM API 调用是否请求了 logprobs：否**

`src/llm_agent.py:268-272`，`SamplingParams` 只传了三个参数：
```python
params = SamplingParams(
    temperature=max(temperature, 0.01),
    max_tokens=self.max_new_tokens,
    stop=["Observation:", "\nObservation"],
)
```
没有设置 `logprobs` 参数。且 `_generate` 方法（L274）只提取了 `outputs[0].outputs[0].text`，丢弃了其他所有返回信息。

**加 logprobs 的改动量**

很小，两处修改即可：
1. `SamplingParams` 加 `logprobs=5`（或需要的 top-k 数量）
2. `_generate` 返回值从纯 text 改为同时返回 `outputs[0].outputs[0].logprobs`

但需要**重新跑 245 episodes**才能拿到带 logprobs 的数据，现有数据无法追溯。

---
