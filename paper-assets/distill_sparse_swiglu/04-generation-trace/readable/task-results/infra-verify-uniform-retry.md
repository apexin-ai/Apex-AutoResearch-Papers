# infra verify uniform retry

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_uniform_retry_20260517T231032_result.json`
- **Structured JSON:** [`ce721b149514d21de9b6.json`](../../sessions/ce/ce721b149514d21de9b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 状态：两个实验均正常运行

**原 PID 81217/81296 已不存在**，当前实际运行的是重新启动的进程：

| 实验 | PID | GPU | 显存占用 | GPU利用率 | 运行时间 | 进度 |
|------|-----|-----|---------|----------|---------|------|
| qwen14b_kl30_uniform | 79839 | cuda:0 | 93.9G/97.9G | 100% | 15m46s | 9% (5473/58702) |
| qwen14b_teal30_uniform | 80810 | cuda:1 | 40.3G/97.9G | 98% | 5m40s | 59% (2774/4687) |

### 关键确认

- **KL uniform**: 命令行明确含 `--allocation uniform`，确认 uniform 模式
- **TEAL uniform**: 命令行明确含 `--allocation uniform`
- 两个日志中有早期失败的 traceback（模型路径 `Qwen2.5-14B` 大小写不匹配 `qwen2.5-14b/`），但当前运行已跳过该错误，loglikelihood 推理正常推进
- TEAL 进度明显快于 KL（4687 vs 58702 总请求数），TEAL 预计再 ~3 分钟完成，KL 预计再 ~36 分钟

---
