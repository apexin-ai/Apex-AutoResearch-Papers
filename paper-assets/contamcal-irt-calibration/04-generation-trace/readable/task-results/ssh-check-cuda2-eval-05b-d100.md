# ssh check cuda2 eval 05B d100

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh-check_cuda2_eval_05B_d100_20260514T150447_result.json`
- **Structured JSON:** [`b78c0643129c3533094a.json`](../../sessions/b7/b78c0643129c3533094a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| 项目 | 结果 |
|------|------|
| **进程 PID 389866** | **存活** — 状态 `Rl`（运行中），已运行 17 分 35 秒 |
| **GPU 2** | 占用中 — PID 389866 使用 3686 MiB，GPU 利用率 37% |
| **输出目录** | 目录已创建但**为空** — 尚无 benchmark 结果写入 |
| **Sentinel/日志** | 无 sentinel 文件，无日志文件 |

**结论**：Cron 误报。进程仍在正常运行，正在执行 eval（mmlu, gsm8k, arc_challenge, humaneval，aligned 格式）。输出目录为空说明还没有 benchmark 完成写出结果。

**建议**：不需要操作，等待运行完成。预计 4 个 benchmark 的 0.5B 模型 eval 总时长约 30-60 分钟，当前才跑了 ~18 分钟。后续可再检查输出完整性。

---
