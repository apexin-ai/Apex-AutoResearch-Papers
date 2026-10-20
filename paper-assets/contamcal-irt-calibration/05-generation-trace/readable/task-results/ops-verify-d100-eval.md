# ops verify d100 eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-d100-eval_20260516T050145_result.json`
- **Structured JSON:** [`3121baf6116739f790a8.json`](../../sessions/31/3121baf6116739f790a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：

**进程存活，正常运行中。** 另一个 Worker 的报告有误。

| 项目 | 状态 |
|------|------|
| PID 687347 | **存活**，运行 1h56m，状态 `Rl+`（running） |
| GPU 3 | PID 687347 占用 8976 MiB，利用率 71% |
| 命令 | `evaluate.py --adapter-path .../Qwen2.5-3B_d100_a32_s42_v3/lora_adapter --output-dir .../Qwen2.5-3B_d100_a32_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned` |
| 输出目录 | `Qwen2.5-3B_d100_a32_s42_aligned/` 存在但**为空** — 说明 eval 还在跑第一个 benchmark，尚未写出结果文件 |
| 日志 | `exp_001_eval_3B_d100_s42_a32_batch.log` 不存在（但有 `exp_001_eval_3B_d100_s123_a32_batch.log`，命名差异可能是日志写到 tmux 而非文件） |

**判断**：进程健康，4 个 benchmark 的 3B eval 预计总共需要 2-3 小时，当前 ~2h 进度正常。输出为空是因为 evaluate.py 在所有 benchmark 跑完后才统一写结果，不是异常。不需要干预。

---
