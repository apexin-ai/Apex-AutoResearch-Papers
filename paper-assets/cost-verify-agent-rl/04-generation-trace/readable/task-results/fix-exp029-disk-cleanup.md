# fix exp029 disk cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp029_disk_cleanup_20260516T230921_result.json`
- **Structured JSON:** [`565cddf48184ae74390b.json`](../../sessions/56/565cddf48184ae74390b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。结果：

**已删除（共 ~130G）：**
- exp028c: 41G
- exp019b_expert_sft_v3: 23G
- exp029_dryrun2: 21G ⚠️（误删，为 dry run，实际 exp029 已保留）
- exp024: 21G
- exp023c: 21G
- exp008_sft: 3.3G
- exp026, exp026_dryrun, exp027, exp028_prereq, exp028_prereq_nothink, exp028a: 空目录

**保留：**
- exp021_ragen_sft_v4: 23G
- exp029: 21G

**磁盘状态：**
- 清理前：242G/250G (97%), 8.4G 可用
- 清理后：115G/250G (46%), **136G 可用**

**训练状态：**
- PID 902342: **ALIVE**，已运行 2h57m
- 进度：6/100 steps (6%)，`Training Progress: 6%`
- GPU：2× 21387 MiB 已用，utilization 0%（可能在 step 间等待/数据加载）
- Ray 之前报的磁盘满警告已不再是问题（现在 136G 可用）

训练进程存活且在推进中，磁盘瓶颈已解除。

---
