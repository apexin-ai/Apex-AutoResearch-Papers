# diag grpo stage2 gpu check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_grpo-stage2-gpu-check_20260515T025732_result.json`
- **Structured JSON:** [`9ad7f5c5091c2dde67c8.json`](../../sessions/9a/9ad7f5c5091c2dde67c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### GPU 状态
| GPU | 利用率 | 显存 | 温度 |
|-----|--------|------|------|
| cuda:0 (rasp_20) | **100%** | 30.4 / 97.9 GB | 79°C |
| cuda:1 (standard_20) | **100%** | 86.1 / 97.9 GB | 82°C |

### 进程状态
- PID 263893 (rasp_20 的实际 python 进程): **运行中**, CPU 109%, 已累积 116 分钟 CPU 时间
- PID 263971 (standard_20 的实际 python 进程): **运行中**, CPU 109%, 已累积 115 分钟 CPU 时间
- wandb-core 进程也都在运行

### 日志 & Checkpoint
- 两个日志最后修改时间：**09:15** (约 1h43m 前)，之后无更新
- 进度条停在 `0/500 [00:00<?, ?it/s]`
- 输出目录只有空的 `completions/` 文件夹，无 checkpoint

### 结论：**正常——卡在 GRPO 首步 generation phase**

两个进程并未卡死。GPU 100% 利用率 + 持续累积 CPU 时间证明它们在积极计算。原因：

1. **GRPO 首步需要为整个 batch 生成所有 completions 后才更新进度条**——TRL 的 GRPO 每个 prompt 生成多条 completion（默认 8 条），每条最长 `max_completion_length=4096` tokens
2. 单 GPU 逐条 autoregressive 生成 4096 tokens 非常慢，整个 batch 的 generation 需要数小时
3. wandb 零指标也是因为首步未完成，metrics 只在 training step 完成后才上报

### 建议

**不需要 kill，继续等待。** 首步 generation 完成后进度条会跳到 1/500 并开始正常推进。

如果未来想加速 GRPO：
- 减小 `max_completion_length`（如 1024 或 2048）
- 减少 `num_generations`（如 4）
- 使用 vLLM 后端加速 generation（TRL 支持但需要 vLLM 兼容版本）

---
