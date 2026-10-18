# exp step1 scoring restart

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_step1-scoring-restart_20260522T130523_result.json`
- **Structured JSON:** [`6f28f63fc5d40390bf50.json`](../../sessions/6f/6f28f63fc5d40390bf50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程活跃（PID 105698，运行 2:54，有 1 个 socket 连接）。

**汇报：**

- **启动成功**：PID 105698，tmux session `step1_scoring`
- **Checkpoint 数量**：23/126（103 remaining）
- **前 30 秒日志**：无 503 错误，代理已恢复正常工作。脚本在逐条 scoring `claude-sonnet-4 / mmlu / clean`（300 pairs），完成后才输出日志行
- **预估完成时间**：
  - Claude batch: 28 conditions × 300 pairs × ~17s/pair ÷ 1 worker ≈ **39.7 小时**（仅 Claude 部分）
  - 如果其他 provider（GPT-4o 等）的条件已完成，总剩余主要是 Claude 的 28 conditions
  - 单 worker 非常慢。若需加速可考虑增加 `max_workers` 或提高 `rps`

---
