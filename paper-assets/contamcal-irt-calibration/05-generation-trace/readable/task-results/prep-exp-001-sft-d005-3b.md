# prep exp 001 sft d005 3B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp_001_sft_d005_3B_20260514T085409_result.json`
- **Structured JSON:** [`94bb0b9bfb13c24eaff2.json`](../../sessions/94/94bb0b9bfb13c24eaff2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`exp_001_sft_d005_3B` 准备完毕，状态 QUEUED。

**验证摘要：**
| 项目 | 状态 |
|------|------|
| 模型 Qwen2.5-3B | ✓ 存在 |
| 数据 sft_dosage_005.jsonl | ✓ 50,826 行 |
| 训练脚本 train_sft.py | ✓ 存在 |
| 输出目录 | ✓ 不存在（干净） |
| Registry 条目 | ✓ QUEUED，hypothesis + 提交命令已记录 |

GPU 空闲时按 notes 中的命令提交即可（提交前需 `nvidia-smi` 确认目标 GPU 无同类进程，遵守 C001）。

---
