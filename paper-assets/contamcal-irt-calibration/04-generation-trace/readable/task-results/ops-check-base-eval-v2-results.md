# ops check base eval v2 results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-base-eval-v2-results_20260515T113152_result.json`
- **Structured JSON:** [`a0f795bca31c014a77fb.json`](../../sessions/a0/a0f795bca31c014a77fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Cron 报告是误报，进程仍在正常运行。**

状态：
- **PID 553256** 在 GPU 2 上活跃（3600 MiB，46% util），已运行 ~1.5 分钟
- MMLU 评估进度 **39%**（5428/14042），速度 ~79 it/s，预计 MMLU 还需 ~2 分钟
- MMLU 之后还要跑 gsm8k、arc_challenge、humaneval
- 命令：`evaluate.py --model-path Qwen2.5-0.5B --output-dir Qwen2.5-0.5B_base_pretrained_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned`

输出目录 `Qwen2.5-0.5B_base_pretrained_aligned/` 当前为空（结果应在全部 benchmark 完成后写入）。

不更新 registry，等进程真正完成后再检查。预计总运行时间约 5-10 分钟。

---
