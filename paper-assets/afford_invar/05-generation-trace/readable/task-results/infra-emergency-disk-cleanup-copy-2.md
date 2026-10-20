# infra emergency disk cleanup

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_emergency-disk-cleanup_20260520T001417_result.json`
- **Structured JSON:** [`2600e1db8a3ebab2ba18.json`](../../sessions/26/2600e1db8a3ebab2ba18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**transfer_v2 也正常运行中**，Step 1241/20000。之前看到的 SIGTERM 是旧进程 (PID 124528) 的残留日志。

---

## 汇报

### 磁盘状态

| 分区 | 清理前 | 清理后 |
|------|--------|--------|
| 根分区 `/` | 9.7G / 30G (33%) | 9.7G / 30G (33%) — 无变化 |
| 数据盘 `/root/autodl-tmp/` | 172G / 350G (49%) | 156G / 350G (45%) |

**根分区从未处于危险状态。** `/root/afford_invar/runs` 是指向 `/root/autodl-tmp/afford_invar/runs` 的 symlink，所有 checkpoint 都在数据盘上。根分区无 >500MB 大文件。

### 清理内容

| 删除目录 | 大小 | 原因 |
|----------|------|------|
| `libero_goal_no_noops+afford+b2+lr0.0005+a0.1/` (lconsist_v1) | 1.5G | DONE negative，不重试 |
| `openvla-7b+...--500_chkpt/` | 15G | 旧 checkpoint，有更新的 |
| `openvla-7b+...--1000_chkpt/` | 15G | 旧 checkpoint，有更新的 |

释放 ~31.5G（净 ~16G，因 oft_baseline 期间新写了 2000_chkpt）。

**未删除 `libero_goal_no_noops+transfer+b2+lr0.0005+beta0.1/`** — 这是 transfer_v2 的活跃输出目录，删除会杀死正在跑的实验。

### 实验状态

| 实验 | PID | GPU | 进度 | 状态 |
|------|-----|-----|------|------|
| phase1_oft_baseline | 123110 (python) | GPU 2 (24340MiB) | Step 2510/20000 (13%) | **正常运行** |
| phase1_transfer_v2 | 125863 (python) | GPU 0 (24720MiB) | Step 1241/20000 (6%) | **正常运行** |

### Checkpoint 路径确认

全部在数据盘 (`/root/autodl-tmp/afford_invar/runs/`)：
- `openvla-7b+...--1500_chkpt/` (15G) — 保留
- `openvla-7b+...--2000_chkpt/` (15G) — oft_baseline 新写入
- `openvla-7b+...--2500_chkpt/` — oft_baseline 刚在 step 2500 保存
- `libero_goal_no_noops+transfer+...` (1.5G) — transfer_v2 活跃目录

根分区上零 checkpoint。

---
