# fix disk cleanup step1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_disk_cleanup_step1_20260514T191344_result.json`
- **Structured JSON:** [`d05cdc7686613ee05f48.json`](../../sessions/d0/d05cdc7686613ee05f48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理完成汇总

| 步骤 | 删除目录 | 释放空间 |
|------|---------|---------|
| 1 | `m2_embed_verify_output/` | **35 GB** |
| 2 | `m2_starcoder_output/` | **28 GB** |
| 3 | `m2_pilot_data/` + `m2_embed_verify_data/` | **2 GB** |
| ~~4~~ | ~~s42/s43 final~~ | 跳过（目录不存在） |
| **合计** | | **65 GB** |

**最终磁盘**: 250G 总量，已用 143G，**可用 108G** (57%)，从 43G → 108G。

**训练状态**: 2 个 run 正在运行，双 GPU 100% 利用率
- GPU 0: `m2_full_random_s44` (Qwen, seed 44)
- GPU 1: `m2_full_sc2_random_s43` (StarCoder2, seed 43)

**剩余大目录可进一步清理**:

| 目录 | 大小 | 建议 |
|------|------|------|
| `checkpoints/` | 47 GB | 含当前训练 checkpoint，**不可删** |
| `full_m1_data/` | 46 GB | M1 阶段数据，若 M1 已完结可考虑删除 |
| `full_m2_training_data/` | 19 GB | 当前训练在用，**不可删** |
| `full_m2_starcoder_data/` | 13 GB | 当前训练在用，**不可删** |
| `swebench_repos/` | 623 MB | 评估用，后续需要则保留 |

108G 可用空间已足够覆盖 ~249GB 需求的前几个 run。如果需要更多空间，`full_m1_data/`（46GB）是最大的可清理候选。

---
