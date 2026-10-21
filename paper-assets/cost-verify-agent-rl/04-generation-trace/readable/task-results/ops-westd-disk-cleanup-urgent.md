# ops westd disk cleanup urgent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_disk_cleanup_urgent_20260520T050441_result.json`
- **Structured JSON:** [`af2c7cc5f9e4d121f43a.json`](../../sessions/af/af2c7cc5f9e4d121f43a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

释放了 30GB（22→52GB），**未达到目标的 ≥50GB 释放量**。

最大的可清理目标：
| 目录 | 大小 | 状态 |
|------|------|------|
| `checkpoints/8b-cell-c-v9/` | 92GB | **禁删** (v9d 训练中) |
| `checkpoints/scienceworld_sft/` | 27GB | 可清理候选 |
| `cost-verify-agent-rl/` | 21GB | 项目代码 |
| `models/` | 20GB | 基础模型 |

`scienceworld_sft` (27GB) 是唯一能安全释放大量空间的目标。删掉后总释放 57GB，磁盘可用 79GB。确认可以删吗？

**不删的风险**：当前 52GB 可用，写 step 10 checkpoint (37GB) 时临时降至 15GB，如果框架是先写后删旧 checkpoint，15GB 缓冲偏紧。

---
