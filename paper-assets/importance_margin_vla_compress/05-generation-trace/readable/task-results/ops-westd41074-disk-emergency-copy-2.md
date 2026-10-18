# ops westd41074 disk emergency

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-disk-emergency_20260521T082244_result.json`
- **Structured JSON:** [`d8ff49cfb34f9a8dfd5f.json`](../../sessions/d8/d8ff49cfb34f9a8dfd5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型已加载完成，正在计算 action statistics（~10 分钟）。训练即将开始。

---

## 执行报告

### 1. 空间释放 (westd-41074)

| 操作 | 释放空间 |
|------|----------|
| 删除 M128 stale checkpoints (`openvla_sc_m128/`) | **38G** |
| 删除 M96 冗余副本 (`checkpoint_step50000.pt`) | **19G** |
| **总计** | **57G** |

磁盘: **93% → 71%** (19G → 75G 可用)

### 2. M64v5 重启状态

- **PID**: 996937
- **GPU**: cuda:3
- **Resume**: 无（v1-v4 均因磁盘满崩溃，无有效 checkpoint，**从头训练**）
- **修改**: `save_every` 从 10000 改为 50000（每个 checkpoint ~19G，原频率会再次撑爆磁盘）
- **当前**: 模型已加载，正在计算 action statistics，预计 ~10 分钟后正式训练
- **日志**: `logs/train_openvla_sc_m64_seed42_v5.log`
- **预计完成**: ~46 小时（100K steps @ 0.6 sps）

### 3. 各服务器磁盘状态

| 服务器 | 容量 | 已用 | 可用 | 使用率 | 大型 Checkpoint |
|--------|------|------|------|--------|-----------------|
| **westd-41074** | 250G | 176G | **75G** | 71% | M96: 19G (1个) |
| **westd-27271** | 250G | 207G | **44G** | 83% | M128 stale 19G, M128_seed42 35G, M32_seed42 38G |
| **westd-38929** | 250G | 210G | **41G** | 84% | M128 stale 19G |
| **cqa1-33015** | 250G | 195G | **56G** | 78% | M128 stale 19G |

### 4. Checkpoint 清理总结

- **已清理**: westd-41074 释放 57G
- **未清理（需确认）**: 其他 3 个服务器各有 `openvla_sc_m128/checkpoint_step20000.pt` (19G)，均为已 kill 的 M128 实验残留，可安全删除
- westd-27271 额外有 `openvla_sc_m128_seed42/` (35G, 含 checkpoint.pt + checkpoint_merged.pt) 和 `openvla_sc_m32_seed42/` (38G, 活跃训练中) 需要单独评估

### 风险提醒

westd-41074 当 M64 和 M96 同时完成 100K steps 时，checkpoint 峰值占用: M96 38G + M64 57G = **95G**，接近可用上限（93G）。建议在 M96 完成后（~27h）及时清理其旧 checkpoint，或对 `save_checkpoint` 增加自动清理逻辑。

---
