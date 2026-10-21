# check all gpu progress v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all-gpu-progress-v2_20260514T172314_result.json`
- **Structured JSON:** [`4a867f7f4405819f47e4.json`](../../sessions/4a/4a867f7f4405819f47e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

report.md 不可直接写入，直接输出：

## GPU Progress Check — 2026-05-15 01:25 (westd) / 2026-05-14 10:25 (home)

### westd cuda:0 — CWM seed123 eval (PID 195531)
- Status: **running** (16h20m)
- Progress: **9208/9784 (94.1%)**
- Running accuracy: **59.0%**
- ETA: **~62 min**

### westd cuda:1 — CWM v12 eval (PID 195668)
- Status: **running** (16h20m)
- Progress: **9320/9784 (95.3%)**
- Running accuracy: **57.9%**
- ETA: **~49 min**

### westd cuda:2 — CWM 8B training (PID 245775, tmux: repo_cwm_8b_restart)
- Status: **running** (2h55m)
- Step: **1659/6633 (25.0%)**, resumed from ckpt-1200
- Training loss: **0.2796**, eval_loss@1600: **0.3742**
- Latest checkpoint: **ckpt-1600** (saved 01:12)
- ETA: **~32.7h**
- eval_loss 趋势: 1400→1500→1600 = 0.364→0.369→0.374，持续微升

### westd cuda:3 — CLS 8B seed123 training (PID 248041)
- Status: **running** (2h36m)
- Step: **3200/6633 (48.2%)**, resumed from ckpt-2400
- Training loss: **0.180** (波动大: 0.53→0.37→0.58→0.18)
- eval_loss@2800: **0.3238**, eval_loss@3200: **0.4262**
- Latest checkpoint: **ckpt-3000** (saved 00:55)
- ETA: **~11.1h**
- **eval_loss 从 0.324 跳到 0.426 (+31%)，需关注过拟合**

### home cuda:0 — CLS 8B ckpt-3000 val@5120 eval (PID 3145070)
- Status: **running** (37min)
- Progress: **~6260/9335 (67.1%)**
- Running accuracy: **89.3%**
- ETA: **~33 min**

---

| GPU | Task | Progress | Key Metric | ETA |
|-----|------|----------|-----------|-----|
| westd:0 | CWM seed123 eval | 94.1% | acc=59.0% | ~62min |
| westd:1 | CWM v12 eval | 95.3% | acc=57.9% | ~49min |
| westd:2 | CWM 8B train | 25.0% | eval_loss=0.374 | ~32.7h |
| westd:3 | CLS 8B s123 train | 48.2% | eval_loss=0.426 | ~11.1h |
| home:0 | CLS 8B ckpt3000 val5120 | 67.1% | acc=89.3% | ~33min |

**关注点:**
1. CLS 8B seed123 的 eval_loss 从 step 2800 (0.324) 跳到 3200 (0.426)，训练 loss 波动也大，可能过拟合
2. CWM 8B 的 eval_loss 也在缓慢上升 (0.364→0.374)
3. 两个 CWM eval ~1h 内完成，seed123 (59.0%) 略优于 v12 (57.9%)

---
