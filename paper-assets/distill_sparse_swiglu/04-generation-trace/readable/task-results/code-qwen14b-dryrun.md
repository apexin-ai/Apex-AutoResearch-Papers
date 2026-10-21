# code qwen14b dryrun

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen14b_dryrun_20260517T124814_result.json`
- **Structured JSON:** [`b078ce2408054a5f85c7.json`](../../sessions/b0/b078ce2408054a5f85c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen-2.5-14B Dry-run 结果

**状态：成功**

| 项目 | 结果 |
|------|------|
| 模型加载 | 成功，8 shard / 28GB |
| Predictor 维度 | 正确：5120 → 128 → 13824（48 层，每层 4 个参数） |
| 可训练参数 | 117,061,632 / 14,770,033,664 (0.793%) |
| 峰值显存（allocated） | **45.33 GiB** |
| 峰值显存（reserved） | **47.47 GiB**（单卡 98GB，余量充足） |
| 单步时间 | **~1.9s**（batch_size=1, gradient_checkpointing, seq_len=2048） |
| Loss 趋势（20步） | step1: 0.598 → step10: 2.047 → step20: 1.141 |
| Sparsity | 0.402 → 0.383 → 0.371（向 target 0.3 收敛中） |

**备注：**
- Loss 先升后降是正常的：tau 从 0.955 退火到 0.1，mask 从软变硬，中间 KL 会先恶化再恢复
- 随机数据不会有真正的 loss 收敛，仅验证训练流程正常
- 单卡 47.5 GiB 占用，双卡并行或 batch_size=2 均可行

---
