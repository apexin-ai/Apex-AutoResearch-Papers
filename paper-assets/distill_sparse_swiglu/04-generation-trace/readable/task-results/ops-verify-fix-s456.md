# ops verify fix s456

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-fix-s456_20260516T145721_result.json`
- **Structured JSON:** [`d377145b3aa07b69f3ef.json`](../../sessions/d3/d377145b3aa07b69f3ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行，无需重提交。

## 状态报告

### nvidia-smi
| GPU | 进程 PID | 显存占用 | GPU 利用率 |
|-----|---------|---------|-----------|
| cuda:0 | 244554 | 66986 MiB / 97887 MiB | 100% |
| cuda:1 | 245032 | 49090 MiB / 97887 MiB | 0% (CPU tokenizing 阶段) |

### cuda:0 — bench_kl50_uniform_s123
- **状态**: 正常运行
- **当前阶段**: MMLU loglikelihood evaluation，865/58702 (~1.5%)，速度 ~32 it/s
- 预计 MMLU 还需 ~30 分钟

### cuda:1 — bench_kl50_uniform_s456
- **状态**: 正常运行（PID 245022 存活）
- **当前阶段**: MMLU tokenizing inputs，56275/58702 (~96%)
- GPU util 为 0% 是因为 tokenization 是 CPU-bound，tokenizing 完成后会进入 loglikelihood 推理阶段，GPU 利用率将上升
- **无需重提交**

---
