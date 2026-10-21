# diagnose kl30 8b multiseed fail

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_kl30_8b_multiseed_fail_20260518T010952_result.json`
- **Structured JSON:** [`83bb6fe2aa2f446535b1.json`](../../sessions/83/83bb6fe2aa2f446535b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：实验没有失败，正在正常运行

两个实验的状态报告有误。实际情况：

### 训练（Phase 1）已成功完成
| | s123 | s456 |
|---|---|---|
| 训练步数 | 1000/1000 | 1000/1000 |
| 最终 sparsity | 0.300 | 0.300 |
| WikiText-2 PPL | 8.9267 | 8.9614 |

### 评估（Phase 2）正在进行
两个 `benchmark_eval.py` 进程均在活跃运行：
- GPU 0 (s123): PID 37184, 100% GPU util, 49GB VRAM
- GPU 1 (s456): PID 37480, 100% GPU util, 49GB VRAM
- 当前都在跑 MMLU loglikelihood（s123 进度约 75%，s456 约 64%）

### 根因
EXIT_CODE=1 的报告是**误报**。可能是监控系统在实验仍在运行时超时判定为失败（wall_clock ~46-47 min 时检查，但实验还没完成）。实际的 nohup 启动命令是 train + eval 两阶段串联，训练约 30 分钟完成后进入评估阶段，评估包含 4 个 benchmark（arc_challenge, winogrande, mmlu, gsm8k），MMLU 本身就很耗时。

**无需任何修复，等评估自然跑完即可。** 日志末尾会输出 `ALL_DONE_OK` 表示成功。

---
