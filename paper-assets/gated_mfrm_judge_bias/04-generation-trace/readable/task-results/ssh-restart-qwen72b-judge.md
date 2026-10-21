# ssh restart qwen72b judge

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_restart_qwen72b_judge_20260522T220730_result.json`
- **Structured JSON:** [`11d92898a7c67aa78f4a.json`](../../sessions/11/11d92898a7c67aa78f4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行正常。

**状态汇总：**
- vLLM server (port 8002, qwen2.5-72b-instruct): 正常运行
- collect.py 已在 tmux session `qwen72b-judge` 中启动
- 启动命令: `PYTHONUNBUFFERED=1 python collect.py --config config_qwen_arena.yaml --benchmark arena_hard --workers 8`
- 已完成: 8736/9000 (含 resume)
- 剩余: 264 条
- 速率: 0.2 items/s，预计 ~25 分钟完成
- 9 个 target models: gpt-3.5-turbo-0125, gpt-4-0314, gpt-4-0613, gpt-4o, gpt-4o-mini, llama-3.3-70b, qwen2.5-72b, gemma-2-9b, qwen3-8b

---
