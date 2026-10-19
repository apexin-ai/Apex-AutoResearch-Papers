# check lm eval status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_lm_eval_status_20260516T002511_result.json`
- **Structured JSON:** [`c162c8fe139c2752e7d9.json`](../../sessions/c1/c162c8fe139c2752e7d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**lm_eval_kl_s42 状态：已完成。**

结果摘要：

| Benchmark | Score |
|-----------|-------|
| arc_challenge | 0.3771 |
| winogrande | 0.6156 |
| mmlu | 0.2591 |
| gsm8k | 0.0121 |

- PID 179913/179918 技术上还活着（33 min），但日志显示评估全部跑完，结果已写入 `results/plan_007/`
- EXIT_CODE=129（SIGHUP），评估在信号前已正常完成并保存
- cuda:0 占 21GB（89%），cuda:1 占 74GB（95%）——两张卡均有其他进程在跑
- PID 179918 仍占 cuda:1 约 16GB 显存，是残留进程

状态报告已写入 `artifacts/lm_eval_status_check.md`。

---
