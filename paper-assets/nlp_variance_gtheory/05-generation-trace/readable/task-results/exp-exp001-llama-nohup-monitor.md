# exp exp001 llama nohup monitor

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_exp001_llama_nohup_monitor_20260521T010837_result.json`
- **Structured JSON:** [`736d7c277f8191c77e94.json`](../../sessions/73/736d7c277f8191c77e94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

nohup 收集脚本已启动，确认运行中。

- **PID**: 63972
- **脚本**: `/tmp/collect_exp001_llama.sh`（后台轮询 `pgrep -f run_experiment`，每 30s 一次）
- **结果文件**: 推理结束后写入 `/tmp/exp001_llama_results.txt`
- **日志**: `/tmp/collect_exp001_llama.log`
- **预计完成**: ~20 分钟后（推理结束即自动收集）

---
