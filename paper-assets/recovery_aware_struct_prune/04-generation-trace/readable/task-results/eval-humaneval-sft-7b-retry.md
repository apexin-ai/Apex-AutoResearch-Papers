# eval humaneval sft 7b retry

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_humaneval_sft_7b_retry_20260519T135704_result.json`
- **Structured JSON:** [`7705a46f9311e0033dbb.json`](../../sessions/77/7705a46f9311e0033dbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行中。

## 诊断与执行总结

### 诊断结果
| 问题 | 发现 |
|------|------|
| 日志不存在 | westd-29022 是克隆机，原 v3/v2 日志未迁移 |
| SFT RASP 模型路径 | `sft_rasp_20` 不存在，实际为 `sft_rasp_20_westd` |
| `sft_standard_20_westd` | 不完整（无 model.safetensors），正确模型在 `sft_standard_20` |
| eval 脚本参数 | `--max_new_tokens`（非 `--max_tokens`） |
| GPU 占用 | 0/1/2 均有进程，仅 GPU 3 空闲 |
| RASP v3 | 另一 agent 已提交，PID 109506 加载模型后死亡 |
| RASP v2 | tmux 进程 PID 107932 在 GPU 1 上正常运行中 |

### 执行结果
| 实验 | 状态 | GPU | 进度 |
|------|------|-----|------|
| `eval_humaneval_sft_standard_20_2048_v4` | RUNNING, GPU 3 (26390 MiB, 97%) | cuda:3 | 已开始推理 (0/164) |
| `eval_humaneval_sft_rasp_20_2048_v3` | RUNNING, GPU 1 (复用 v2 进程 PID 107932) | cuda:1 | 53/164 (32%), Pass@1: 20% |

预计 Standard ~1h, RASP ~30min 完成。

---
