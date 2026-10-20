# exp alfworld llama cross model

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_alfworld-llama-cross-model_20260520T055857_result.json`
- **Structured JSON:** [`c6e11deb036c71d00ee4.json`](../../sessions/c6/c6e11deb036c71d00ee4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并注册完成。

**总结：**
- tmux session `alfworld-llama-cross-model` 在 westb-13313 上运行
- 模型：Meta-Llama-3.1-8B-Instruct (vLLM, GPU 0)
- 135 games，每 task 约 105s，预计 ~4 小时完成
- 第一个 task 已完成 (no-preference)，输出写入 `results/alfworld_llama_counterfactual/episodes.jsonl`
- Registry 已更新为 RUNNING

**修复过程**：tokenizer.json 截断 + 模型权重缺失，从 ModelScope 缓存目录硬链接恢复。

---
