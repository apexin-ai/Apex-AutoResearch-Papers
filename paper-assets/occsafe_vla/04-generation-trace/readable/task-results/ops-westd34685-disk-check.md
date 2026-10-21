# ops westd34685 disk check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd34685_disk_check_20260523T141006_result.json`
- **Structured JSON:** [`b7f68dbe49c80dce9615.json`](../../sessions/b7/b7f68dbe49c80dce9615.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 磁盘预警检查报告

### 1. 磁盘状态

| 总量 | 已用 | 可用 | 使用率 |
|------|------|------|--------|
| 350G | 289G | **62G** | 83% |

### 2. Checkpoint 目录占用

| 目录 | 大小 | 状态 |
|------|------|------|
| vanilla_retrain_s0 | 45G | **运行中** (4 子目录: latest + 10K/20K/30K) |
| full_occ_retrain_s0 | 45G | **运行中** (同上) |
| reverse_cutoff_s0 | 45G | **运行中** (同上) |
| cutoff_25k_s0 | 45G | **运行中** (同上) |
| cutoff_s0 | 15G | 旧实验 (eval 已完成) |
| cutoff_s1 | 15G | 旧实验 (eval 已完成) |
| depth_s0 | 15G | 旧实验 (eval 已完成) |
| depth_s1 | 15G | 旧实验 (eval 已完成) |
| ablation_occ_detach_s2 | 15G | 旧实验 |
| ablation_random_occ_s2 | 15G | 旧实验 |
| **总计** | **270G** | |

### 3. 训练进度 & 剩余 checkpoint 需求

| 实验 | 当前 step | 已保存 ckpt | 还需保存 | 额外空间需求 |
|------|-----------|------------|---------|-------------|
| vanilla_retrain_s0 | ~37,300 (75%) | 10K, 20K, 30K | 40K, 50K | **30G** |
| full_occ_retrain_s0 | ~37,180 (74%) | 10K, 20K, 30K | 40K, 50K | **30G** |
| reverse_cutoff_s0 | ~30,550 (61%) | 10K, 20K, 30K | 40K, 50K | **30G** |
| cutoff_25k_s0 | ~30,600 (61%) | 10K, 20K, 30K | 40K, 50K | **30G** |
| **合计** | | | **8 个** | **120G** |

### 4. 空间判断

**严重不足。** 可用 62G，需要 120G，缺口 **~58G**。

- vanilla_retrain_s0 和 full_occ_retrain_s0 最快到 40K step（约 2,700 步，~42 分钟），届时同时写两个 15G checkpoint 就需要 30G，勉强能过第一波
- 但 reverse_cutoff_s0 和 cutoff_25k_s0 到 40K 时再来 30G，磁盘必满
- 50K checkpoint 完全无空间

### 5. 推荐清理方案

**旧实验 checkpoint（eval 已完成，可安全删除）：**

| 可删目录 | 释放空间 |
|----------|---------|
| cutoff_s0 | 15G |
| cutoff_s1 | 15G |
| depth_s0 | 15G |
| depth_s1 | 15G |
| ablation_occ_detach_s2 | 15G |
| ablation_random_occ_s2 | 15G |
| **合计** | **90G** |

清理后可用空间 = 62G + 90G = **152G**，满足 120G 需求，余量 32G。

### 6. 建议

- **立即删除 6 个旧实验 checkpoint**，释放 90G，空间充裕
- 如果不愿全删，**至少删 4 个**（释放 60G），加上现有 62G = 122G，刚好够
- save_freq 不需要调整，清理后空间足够

**需要我执行删除吗？**

---
