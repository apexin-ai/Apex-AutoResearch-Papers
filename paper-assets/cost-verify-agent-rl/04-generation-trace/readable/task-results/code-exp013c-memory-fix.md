# code exp013c memory fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp013c-memory-fix_20260514T083238_result.json`
- **Structured JSON:** [`68f7174e9068bb74e87b.json`](../../sessions/68/68f7174e9068bb74e87b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成。

## 产出

### 1. env_groups 修改前后

| 参数 | 修改前 | 修改后 |
|------|--------|--------|
| train.env_groups | 8 | **4** |
| train.group_size | 16 | 16（不变） |
| train.n_groups | [8] | **[4]** |
| val.env_groups | 16 | 16（不变） |
| val.group_size | 1 | 1（不变） |

### 2. 内存估算
- 修改后并发：4 × 16 = **64 个 ALFWorld 游戏**
- 每游戏估算 ~2GB 内存 → 峰值 ~128GB
- Ray object store 将限制为 30GB（启动时设 `RAY_object_store_memory=30000000000`）
- 总计 ~158GB，在 220GB cgroup 限制内安全

### 3. GPU 和进程清理
- 4 个残留 `ray::WorkerDict` 进程已 kill（PID: 267666, 271458, 267667, 271459）
- `/tmp/ray*` 已清除
- GPU 0: 3 MiB / 97887 MiB ✓
- GPU 1: 3 MiB / 97887 MiB ✓

启动时记得加 `export RAY_object_store_memory=30000000000`。

---
