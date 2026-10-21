# check westb gpu1 and westd progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westb_gpu1_and_westd_progress_20260521T225945_result.json`
- **Structured JSON:** [`87f169f7affeea745b4b.json`](../../sessions/87/87f169f7affeea745b4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1. westb-23072 GPU 1

两个 eval 进程共享 GPU 1：

| PID | 模型 | VRAM | 运行时间 |
|-----|------|------|---------|
| 104592 | `sft_standard_25/checkpoint-1870` | 19186 MiB | 7h40m |
| 118095 | `sft_cka_only_20` | 17044 MiB | 3h27m |

两个都是 `eval_math500.py`。sft_cka_only_20 的日志显示进度 **206/500**，elapsed 3h25m。sft_standard_25 的日志路径 `eval_math500_sft_standard_25/eval.log` 不存在（可能用了其他日志文件名）。

## 2. westd-29022 MATH-500 eval 进度

| GPU | 任务 | 进度 | Accuracy | 平均速度 | 预计剩余 |
|-----|------|------|----------|---------|---------|
| GPU 1 | eval_math500_grpo_random_20_v2 | **452/500** | 0.1244 (at 450) | ~72s/it | **~60 min** |
| GPU 3 | eval_math500_sft_random_20 | **206/500** | 未报告 | ~60s/it（高度波动） | **~5h** |

**grpo_random_20_v2 先完成**，大约还需 1 小时。sft_random_20 还差约 5 小时。

注意：sft_random_20 的进度条显示 elapsed 仅 3h25m，但进程从 22:48 启动至今已 ~8h，存在不一致——可能中途有重启或脚本内部计时逻辑不同。

---
