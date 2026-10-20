# infra westd10894 disk cleanup and restart

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd10894_disk_cleanup_and_restart_20260520T163301_result.json`
- **Structured JSON:** [`55df351fb175a4119e62.json`](../../sessions/55/55df351fb175a4119e62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务完成。报告如下：

---

## 处理报告

### 1. 磁盘清理
| | 清理前 | 清理后 |
|---|---|---|
| 已用 | 250G (100%) | 81G (33%) |
| 可用 | 1.5M | 170G |
| 回收 | — | ~169G |

每 seed 删除了 4 个旧 checkpoint (5k/10k/15k/20k)，各保留 25000_chkpt。

### 2. 各 seed 保留 checkpoint
| Seed | 保留 checkpoint | 大小 |
|---|---|---|
| vanilla_s0 | 25000_chkpt | 15G |
| vanilla_s1 | 25000_chkpt | 15G |
| vanilla_s2 | 25000_chkpt (已修复) | 15G |

### 3. vanilla_s2 checkpoint 完整性
原始 25000_chkpt **损坏**——磁盘满时写入中断，model-00002 截断 (785MB vs 应有 4.9GB)，model-00003/00004 缺失。

但 LoRA adapter、action_head、proprio_projector 均完整。通过 base model + LoRA adapter merge 重建了完整的 safetensors（4 个 shard，和 s0 字节数完全一致）。

### 4. s0/s1 当前进度
| Seed | 当前 step | 速度 | 预计完成 (UTC) |
|---|---|---|---|
| s0 (PID 100203) | 26733/50005 | ~1.09 it/s | ~06:40 May 21 |
| s1 (PID 97847) | 26517/50005 | ~1.09 it/s | ~07:00 May 21 |

### 5. s2 恢复情况
- 崩溃原因：磁盘满 (exitcode 1, 2026-05-21 00:20:46)
- 恢复方式：`--resume True --resume_step 25000`，`--vla_path` 指向修复后的 25000_chkpt
- 新进程 PID: 149428 (worker), 149353 (bash wrapper)
- 从 log_step 25000 继续，预计 ~07:15 UTC 完成
- GPU 2，~1.09 it/s，运行正常

### 6. 最终状态
- **GPU**: 0/1/2 均 99% 利用率，GPU 3 空闲
- **磁盘**: 81G/250G (33%)

### ⚠️ 注意
每个 seed 后续还会保存 5 个 checkpoint (30k~50k)，共 15 × ~15G = ~225G。当前空闲 170G **不够**。建议在 step 30000 保存后删除 25000_chkpt，之后每次保存新 checkpoint 后删除上一个，避免再次磁盘满。

---
