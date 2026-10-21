# ops check 10894 urgent

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_10894_urgent_20260524T174906_result.json`
- **Structured JSON:** [`6827e50800a90fcdf09c.json`](../../sessions/68/6827e50800a90fcdf09c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| GPU | exp_id | PID | 状态 | Step/Total | ETA |
|-----|--------|-----|------|------------|-----|
| cuda:0 | ablation_occ_detach_s0_retrain | 746696 | **CRASHED** | 30000/50005 | - |
| cuda:1 | full_occ_ln_s0 | 742821 | **RUNNING** | ~30755/50005 (61%) | ~5h |
| cuda:2 | full_occ_ln_s1 | 743031 | **CRASHED** | 30000/50005 | - |
| cuda:3 | full_occ_ln_s2 | 743375 | **CRASHED** | 30000/50005 | - |

**空闲 GPU：cuda:0, cuda:2, cuda:3**

### 崩溃原因

**全部相同：`No space left on device (os error 28)`**

三个实验都在 step 30000 保存 checkpoint 时因磁盘满而崩溃（01:38~01:44 UTC）。

磁盘状态：
- `/root/autodl-tmp`：**250G / 250G (100% 已满，仅剩 740K)**
- `/root`（系统盘）：30G 用了 21G，还有 9.1G

### 紧急风险

`full_occ_ln_s0`（cuda:1）当前仍在运行，但下一个 checkpoint 保存点是 step 40000。**如果不清理磁盘空间，它也会在 ~5h 后崩溃。**

### 需要立即行动

1. **清理 `/root/autodl-tmp/` 磁盘空间**（删除旧 checkpoint、清理 HF cache 等）
2. 清理后重启 cuda:0/2/3 上的三个实验（可从 step 30000 checkpoint 恢复，如果保存成功的话）
3. 确保 `full_occ_ln_s0` 在 step 40000 前有足够空间

Registry 已更新：三个崩溃实验状态设为 DONE(failed)。

---
