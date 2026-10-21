# ops disk cleanup and scp

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_and_scp_20260523T140332_result.json`
- **Structured JSON:** [`53f8c44a1ab98af2f828.json`](../../sessions/53/53f8c44a1ab98af2f828.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

### 阶段 1：清理结果

| 删除项 | 释放空间 |
|--------|---------|
| cutoff_s2 (旧实验) | ~74G |
| depth_s2 + depth_s3 (eval 已完成) | ~30G |
| detach_ln_s0/step-030000 (损坏) | 少量 |
| detach_ln_s2/step-020000 (损坏) | 少量 |
| cutoff_s2_v2 (损坏) | ~540K |
| **阶段 1 合计释放** | **~103G** |

### 阶段 2：SCP 迁移结果

| Checkpoint | 大小 | safetensors 文件数 | 状态 |
|-----------|------|-------------------|------|
| ablation_occ_detach_s2 50K | 15G | 5 (4 shard + 1 lora) | 完整 |
| ablation_random_occ_s2 50K | 15G | 5 (4 shard + 1 lora) | 完整 |

源文件已从 westd-10894 删除，额外释放 30G。

### 最终磁盘状态

| 服务器 | 总容量 | 已用 | 可用 | 使用率 |
|--------|-------|------|------|--------|
| **westd-10894** | 250G | 117G | 134G | **47%** (从 100% 降) |
| **westd-34685** | 350G | 289G | 62G | 83% (从 74% 升) |

westd-10894 剩余 checkpoint 80G（detach_ln_s0/s1/s2）。

---
