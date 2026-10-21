# ssh wait restart llama qwen judges v2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_wait_restart_llama_qwen_judges_v2_20260522T084304_result.json`
- **Structured JSON:** [`2abab89cd614e59ada67.json`](../../sessions/2a/2abab89cd614e59ada67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

自动重启脚本已部署并运行中。

当前状态：
- llama: 488/500（约 1-2 轮检查后触发 judge）
- qwen: 403/500（约 2-3 轮检查后触发 judge）
- 脚本每 3 分钟检查一次，response 到 500 行时自动在独立 tmux session 启动 `collect.py --workers 8 --generate-judge-responses`
- 日志：`/tmp/auto_restart_judges.log`（总控）、`/tmp/judge_llama_collect.log`、`/tmp/judge_qwen_collect.log`

---
