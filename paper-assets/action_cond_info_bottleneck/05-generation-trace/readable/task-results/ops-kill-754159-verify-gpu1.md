# ops kill 754159 verify gpu1

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-754159-verify-gpu1_20260516T034558_result.json`
- **Structured JSON:** [`a83cb9e8f916a3b19ef7.json`](../../sessions/a8/a83cb9e8f916a3b19ef7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 产出

**Step 1: PID 754159 kill 状态**
- kill 成功 → `KILLED_OK`
- 进程命令确认为旧 seed2 训练（`acib_v5_div_reg_seed2`, etime 14:14），不是误杀

**Step 2: GPU 1 最终进程列表**
- PID 733616: `/root/miniconda3/bin/python` (6601 MiB) — baseline_std libero_10 eval ✓
- PID 755664: `python3` (16216 MiB) — seed2 训练 ✓
- 无其他 train_acib 残留进程

**Step 3: 全局 nvidia-smi**
- GPU 0 (21573 MiB / 97887 MiB, 62% util): PID 675231 (eval, 5331 MiB) + PID 682233 (seed1 训练, 16214 MiB)
- GPU 1 (22845 MiB / 97887 MiB, 100% util): PID 733616 (eval, 6601 MiB) + PID 755664 (seed2 训练, 16216 MiB)

GPU 1 已清理干净，无重复进程。

---
