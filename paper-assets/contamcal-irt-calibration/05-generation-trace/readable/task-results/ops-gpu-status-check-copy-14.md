# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260516T160350_result.json`
- **Structured JSON:** [`3cf4c64ddb39a6b15c38.json`](../../sessions/3c/3cf4c64ddb39a6b15c38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：全部 6 张 GPU 都在正常运行，没有任何任务结束。** 系统误报 idle 是 C002 已知问题（resource_usage 工具 PID/tmux 不匹配导致误判）。

| GPU | 实验 | 运行时间 | GPU利用率 |
|-----|------|---------|----------|
| cuda:0 | Llama d005 SFT | 32min | 86% |
| cuda:1 | Llama d000 eval (aligned) | 30min | 80% |
| cuda:2 | 0.5B-Instruct eval | 1h22min | 0% (CPU-bound phase) |
| cuda:3 | Llama d025 SFT | 56min | 100% |
| cuda:4 | 1.5B MMLU signals | 15min | 45% |
| cuda:5 | Llama d100 SFT | 32min | 84% |

cuda:2 的 0% GPU-util 不代表挂了——进程活着且已跑 1h22m，可能在 HumanEval 代码执行阶段（纯 CPU）。3 个 Llama SFT 都还在 LoRA 训练阶段，尚未到 merge 步骤。

报告已写入 `artifacts/report_gpu_status_check.md`。

---
