# infra westd disk cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd_disk_cleanup_20260521T211049_result.json`
- **Structured JSON:** [`eeedc585006490e5b3dc.json`](../../sessions/ee/eeedc585006490e5b3dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

---

## 报告

### 1. 磁盘使用量

| 分区 | 清理前 | 清理后 | 释放 |
|------|--------|--------|------|
| Root (/) | 14G/30G (46%) | 14G/30G (46%) | 0 |
| Data (/root/autodl-tmp) | 142G/250G (57%) | 124G/250G (50%) | **~18GB** |

可用空间：Root 17GB + Data **127GB**，完全足够 Intervention C（5-10GB）和 OOD eval（3-5GB）。

### 2. 清理内容

| 已删除 | 大小 |
|--------|------|
| `exp029-seed8/global_step_10/` (FSDP shards) | ~20GB |

### 3. Seeds 4/7/8 Checkpoint 状态

| Seed | 路径 | Step | 格式 | 状态 |
|------|------|------|------|------|
| Seed 4 | `exp029-seed4/global_step_15_hf/` | 15 | HF | 3.8GB，完好。symlink `qwen_exp029_seed4_step15_hf` 指向它 |
| Seed 7 | — | — | — | **不存在**，此服务器无任何 seed7 checkpoint |
| Seed 8 | `exp029-seed8/global_step_5/` | 5 | FSDP shards (`actor/`) | 21GB，已保留。step 10 已删除 |

注：Seed 8 step 5 是 FSDP shards 格式，若要用于 OOD eval 需先转换为 HF 格式。

### 4. 进程状态

- **活跃任务**：`exp029_seed4_ood_eval_v2`（PID 779412）正在 CUDA:2 上运行，Ray 集群活跃（含 wandb 日志）。未 kill。
- **系统进程**：jupyter-lab (PID 934)、tensorboard (PID 940) — 正常基础设施，未动。
- **无僵死进程**。

### 5. 空间充足性

127GB 数据盘可用 + 17GB 根分区可用。Intervention C 和 OOD eval 可同时启动，无空间瓶颈。

---
