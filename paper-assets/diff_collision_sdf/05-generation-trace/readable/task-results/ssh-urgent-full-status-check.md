# ssh urgent full status check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_full_status_check_20260521T165714_result.json`
- **Structured JSON:** [`35b7729247bcdac53772.json`](../../sessions/35/35b7729247bcdac53772.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已采集。

## 状态总览

### westd-35807（4 卡全满载）

| GPU | 实验 | PID | alive/dead | Step/30K | Loss | GPU util |
|-----|------|-----|-----------|----------|------|----------|
| 0 | A1 LoRA spatial_bowl | 299910 | **alive** (10h09m) | **9,645** (32%) | 0.042 | 100% |
| 1 | Baseline LoRA spatial_bowl | 281554 | **alive** (14h46m) | **13,175** (44%) | 0.020 | 100% |
| 2 | A1 LoRA object_pudding | 292258 | **alive** (12h15m) | **13,130** (44%) | 0.019 | 100% |
| 3 | Baseline LoRA object_pudding | 281629 | **alive** (14h46m) | **13,148** (44%) | 0.021 | 100% |

### westd-45947（2 卡全满载）

| GPU | 实验 | PID | alive/dead | Step/30K | Loss | GPU util |
|-----|------|-----|-----------|----------|------|----------|
| 0 | A3 spatial_bowl | 164430 | **alive** (7h54m) | **7,697** (26%) | 0.062 | 100% |
| 1 | A3 object_pudding | 165990 | **alive** (7h53m) | **28,971** (97%) | 0.015 | 100% |

---

### 关键判断

1. **A3 object_pudding 是否完成？** — **未完成**，当前 28,971/30,000 (97%)。按 ~4s/step 估算，剩余 ~1,029 步 ≈ **约 1.1 小时后完成**。

2. **A1 Phase 2 LoRA 解冻是否触发？** — **未触发**。两个 A1 实验的 train.log 中均无 "phase 2" / "unfreeze" / "Phase2" 相关日志。

3. **异常：**
   - **A1 spatial_bowl 进度明显落后**：仅 32%（9,645 步），比同机其他实验慢。原因是它比 baseline 晚启动 ~4.6 小时（uptime 10h vs 14.75h）。
   - **A3 spatial_bowl 日志路径变更**：实际写入 `/tmp/spatial_bowl.log`（非预期的 `train_fresh.log`）。`train_resume3.log` 记录了一次 SyntaxError 启动失败（`train_a3_hook.py:243`），但当前进程正常运行。
   - **Baseline 两个实验进度几乎同步**（13,175 vs 13,148），loss 也接近（0.020 vs 0.021），运行正常。

---
