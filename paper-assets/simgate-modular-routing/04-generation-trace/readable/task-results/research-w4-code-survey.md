# research w4 code survey

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_w4-code-survey_20260521T205845_result.json`
- **Structured JSON:** [`84b609ffed5dfc081a27.json`](../../sessions/84/84b609ffed5dfc081a27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/w4_code_survey.md`。

核心发现：

1. **Router 训练代码**在 `src/router_sft_train.py`，用 Qwen3 LoRA + `AutoModelForSequenceClassification`，2-class (internal/deterministic)，输入只有 observation + action_history，**prompt 中不含 task_type**。

2. **训练数据**（2040 steps）中每条记录都已包含 `task_type` 字段，无需额外数据采集。Label 分布严重不平衡：1830 deterministic / 210 internal。

3. **已有 `task_type_classifier.py`** 但用的是 3-class episode-level 设置，不能直接与 2-class step-level router 对比。

4. **推荐 Plan C**：新建一个 ~120 行的 sklearn 脚本 `src/task_type_positive_control.py`，用 task_type one-hot 作为唯一输入预测 routing label。运行 <1 秒，预期 balanced accuracy ~90%+，直接证明 routing signal 是 task-type level property。如果 reviewer 需要 same-architecture 对比，再补做 Plan A（在 LLM prompt 中加一行 task_type）。

---
