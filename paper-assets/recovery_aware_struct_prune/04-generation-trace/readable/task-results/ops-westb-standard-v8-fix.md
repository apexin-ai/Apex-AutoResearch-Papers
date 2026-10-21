# ops westb standard v8 fix

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-standard-v8-fix_20260515T144217_result.json`
- **Structured JSON:** [`c4d945df7cd6b53d4f9d.json`](../../sessions/c4/c4d945df7cd6b53d4f9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪，双卡训练正常运行。

### 最终状态

| GPU | 进程 | PID | 显存 | 状态 |
|-----|------|-----|------|------|
| cuda:0 | RASP v8 | 532861 | 71.7GB | 训练中 (1/100) |
| cuda:1 | **Standard v8** | **534667** | 33.5GB | 训练中 (0/100，刚启动) |

- **Standard v8 新 PID**: 534662 (bash wrapper) / 534667 (python)
- **wandb run**: `grpo_stage2_standard_20_v8` → `runs/q34vz8j2`
- **RASP v8 wandb**: `grpo_stage2_rasp_20_v8` → `runs/0wz7xpd5`（已跑到 1/100）
- **异常**: 网络不通（HuggingFace HEAD 请求失败），但已 fallback 到本地缓存的 GSM8K 数据集，不影响训练

---
