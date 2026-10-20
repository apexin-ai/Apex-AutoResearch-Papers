# diagnose eval 05B hang

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_05B_hang_20260514T004837_result.json`
- **Structured JSON:** [`62d0df9a38904815d299.json`](../../sessions/62/62d0df9a38904815d299.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：正常运行，未挂死。**

两个 eval 进程都在正常运行：

| 实验 | PID | GPU | GPU Util | 显存 | 当前任务 | 进度 | 速度 | GSM8K 剩余 |
|------|-----|-----|----------|------|---------|------|------|-----------|
| s42 | 229370→229375 | GPU 1 | 36% | 3658 MiB | GSM8K | 1215/1319 (92%) | ~5.1s/it | ~9 min |
| s123 | 229516→229521 | GPU 2 | 35% | 3658 MiB | GSM8K | 1167/1319 (88%) | ~5.3s/it | ~13 min |

**运行时间**：进程启动约 2 小时（非 10 小时），日志在持续更新（08:49 最后修改）。

**早期异常**：06:59-07:00 期间有大量 HuggingFace 连接超时（下载 GSM8K 数据集），但最终自动恢复，已过渡到正常 eval 阶段。

**待完成 benchmark**：当前在 GSM8K，之后还有 arc_challenge 和 humaneval。命令行参数为 `--benchmarks mmlu gsm8k arc_challenge humaneval`，MMLU 应已完成。GSM8K 完成后预计还需运行 arc_challenge + humaneval，总剩余时间估计 30-60 分钟。

**结论**：不需要 kill，不需要重提交。让它们继续跑完即可。

---
