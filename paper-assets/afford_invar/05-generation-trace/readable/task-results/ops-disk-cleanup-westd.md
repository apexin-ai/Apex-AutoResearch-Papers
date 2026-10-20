# ops disk cleanup westd

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-westd_20260520T001220_result.json`
- **Structured JSON:** [`c5f20def7743cfc37dcb.json`](../../sessions/c5/c5f20def7743cfc37dcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 磁盘检查与清理报告

### 清理前/后对比

| 分区 | 清理前 Used/Avail | 清理后 Used/Avail | 变化 |
|------|------|------|------|
| 根分区 (overlay, 30G) | 9.7G / 21G | 7.2G / 23G | **释放 2.5G** |
| 数据盘 (/dev/md0, 350G) | 156G / 195G | 166G / 185G | 反增 10G（2000_chkpt 写入） |

### 已清理项

- pip cache: ~1.6G（根分区）
- conda pkgs cache: ~107MB（根分区）
- __pycache__: 26 个目录（可忽略）
- 合计释放 ~2.5G（均在根分区，不影响数据盘）

### phase1_lconsist_v1_cont 崩溃原因更正

**不是磁盘满。** 实际崩溃原因是 `--resume` 参数解析错误（exitcode 2），脚本启动即失败，从未开始训练。没有 checkpoint-2000+ 可删。afford 目录下的 checkpoint-500 和 checkpoint-1000 均属于原始 phase1_lconsist_v1。

### phase1_oft_baseline 状态

- PID 123033 运行正常（已运行 ~11 分钟）
- 当前 step ~2143/20000，正在保存/合并 checkpoint
- 速度 ~4.5 it/s

### 严重警告：磁盘空间不足以跑完

**phase1_oft_baseline 每 500 步保存一个 15G merged checkpoint 且不删旧的。**

- 已有 4 个 checkpoint（500/1000/1500/2000）= 60G
- 剩余空间 185G，最多再存 **12 个** checkpoint
- 预计到 **step ~8500** 数据盘就会满
- 跑完 20000 步总共需要 40 个 checkpoint = **600G**，远超数据盘容量

### 建议（需你决定）

1. **最关键**：修改保存策略 — 开启 `save_latest_checkpoint_only` 只保留最新 checkpoint，或增大 `save_freq`（如 2000 或 5000 步）
2. 手动删除早期的 merged checkpoint（--500_chkpt, --1000_chkpt）可腾出 30G，但只多撑 ~1000 步
3. 需要立即行动，否则 ~1 小时后训练就会因磁盘满而崩溃

---
