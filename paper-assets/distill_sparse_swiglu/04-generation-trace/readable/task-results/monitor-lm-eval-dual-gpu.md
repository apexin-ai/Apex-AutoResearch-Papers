# monitor lm eval dual gpu

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_lm_eval_dual_gpu_20260515T231931_result.json`
- **Structured JSON:** [`aa9655a4014534394f67.json`](../../sessions/aa/aa9655a4014534394f67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 监控报告

### 进程状态

| 任务 | PID | GPU | 运行时间 | 状态 | GPU 利用率 | 显存 |
|------|-----|-----|---------|------|-----------|------|
| kl_s42 | 171565 | cuda:0 | 16h13m | Running | 97% | 29.9/97.9 GB |
| dense | 163723 | cuda:1 | 31h01m | Running | 85% | 29.8/97.9 GB |

### 进度详情

**kl_s42 (cuda:0)**:
- 正在运行 **MMLU loglikelihood**: 79% (44525/56168), ~178 it/s, 剩余 ~1 分钟
- ARC-c、WinoGrande 应已完成推理（结果在所有任务跑完后统一输出）
- **剩余**: GSM8K（generate_until 模式，比 loglikelihood 慢很多）
- **预估剩余时间**: 1-3 小时（取决于 GSM8K 生成速度）

**dense (cuda:1)**:
- 花了 ~30 小时在 tokenizing 阶段（MMLU 57 个子任务 tokenize 耗时极长）
- 刚进入推理阶段，当前跑 **ARC-c loglikelihood**: 11% (506/4687), ~6 it/s, ARC-c 剩余 ~12 分钟
- **剩余**: WinoGrande (~2534 requests) + MMLU (~56168 requests) + GSM8K (generation)
- MMLU loglikelihood 按 6 it/s 估需 ~2.6 小时；GSM8K 额外数小时
- **预估剩余时间**: 4-6+ 小时

### 结果产出
- `/root/distill_sparse_swiglu/results/lm_eval/` 目录为空，两个任务均未完成
- 两个 log 中均无 accuracy 输出（lm_eval 在所有 task 跑完后才统一打印结果）

### 注意
dense 推理速度 (6 it/s) 远低于 kl_s42 (178 it/s)，部分原因是 ARC-c 用 25-shot（长上下文），但差距仍较大。kl_s42 可能因为是稀疏模型，推理更快。

---
