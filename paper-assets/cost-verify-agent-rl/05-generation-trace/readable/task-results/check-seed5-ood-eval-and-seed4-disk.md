# check seed5 ood eval and seed4 disk

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed5_ood_eval_and_seed4_disk_20260521T144232_result.json`
- **Structured JSON:** [`e40a7c773ec66ec55fed.json`](../../sessions/e4/e40a7c773ec66ec55fed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Seed 5 OOD Eval (westd-47453): **已完成**

PID 375913/383150 已退出，GPU 3 内存已释放（0 MiB）。

**关键指标**（134 OOD episodes）：

| 指标 | 值 |
|------|-----|
| success_rate | **29.10%** |
| pass@1 | **29.10%** |
| num_actions | 38.54 |
| action_is_effective | 99.99% |
| action_is_valid | 72.66% |
| response_length | 6632.0 |
| tasks_evaluated | 134 |
| eval 耗时 | 1218s (~20.3 min) |

westd GPU 状态：GPU 0/1 各占 ~45GB（Seed 3/5 训练），GPU 2/3 已空闲。

---

### bjb1 磁盘 + Seed 4 训练

**磁盘**：
- 根分区：30G 总量，8.4G 已用，**22G 可用**（28%）
- 数据盘 `/root/autodl-tmp/`：170G（其中 checkpoints 126G）
- Checkpoint 存储在数据盘，不占根分区 → **安全**

**Seed 4 训练进度**：
- 最新完成 step 的 ID eval：**success=40.63%, pass@1=40.63%**（32 episodes）
- 训练累计 ~16457s，每 step ~2010s（~33.5 min）→ 约完成 **9 个训练 step**
- 当前正在进行 step 10 的 eval（日志 22:41 仍在输出 AlfworldSG warnings）
- 预计还需 ~5 steps × 33.5 min ≈ **~2.8 小时**完成

---
