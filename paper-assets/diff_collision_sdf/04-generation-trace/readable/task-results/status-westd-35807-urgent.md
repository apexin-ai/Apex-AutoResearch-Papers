# status westd 35807 urgent

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westd-35807-urgent_20260527T092042_result.json`
- **Structured JSON:** [`c92b3cbf0d576b1fa8dc.json`](../../sessions/c9/c92b3cbf0d576b1fa8dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-35807 状态

### nvidia-smi
```
GPU 0: RTX PRO 6000,  9012/97887 MiB, 46%  — PID 722752 (eval)
GPU 1: RTX PRO 6000,     1/97887 MiB,  0%  — 空闲
GPU 2: RTX PRO 6000, 27045/97887 MiB, 100% — PID 274407 (s1 训练)
GPU 3: RTX PRO 6000, 27037/97887 MiB, 100% — PID 341425 (spatial_bowl)
```

### eval s0 30K (cuda:0)
状态: **STILL_RUNNING** (PID 722752)
已完成 3/10 tasks（~9min/task，预计还需 ~63min）:

| Task | TSR | CAR | avg_max_disp |
|------|-----|-----|-------------|
| 0 | 30.0% | 60.0% | 0.0677m |
| 1 | 70.0% | 74.0% | 0.0555m |
| 2 | 24.0% | 68.0% | 0.0313m |

部分均值: TSR=41.3%, CAR=67.3%
frozen_rate/dfCAR 待 eval 完成后出。

### s1 训练 (cuda:2)
当前步数: **20178/30000** (67%)
ETA: ~12h34m
速度: 4.61s/it, loss=0.0114

### spatial_bowl LoRA ctrl (cuda:3)
当前步数: **20187/30000** (67%)
ETA: ~12h39m
速度: 4.64s/it, loss=0.0168

---

## westd-45947 状态

### nvidia-smi
```
GPU 0: RTX PRO 6000, 27089/97887 MiB, 100% — PID 460442 (LoRA baseline s2)
GPU 1: RTX PRO 6000, 27097/97887 MiB, 100% — PID 425058 (λ=0.1 s2)
```

### LoRA baseline s2 (cuda:0)
当前步数: **25817/30000** (86%)
ETA: ~5h23m
速度: 4.63s/it, loss=0.0091

### λ=0.1 s2 训练 (cuda:1)
当前步数: **18203/30000** (61%)
ETA: ~15h05m
速度: 4.61s/it
Loss 分解: action=0.0111, sdf=0.0358, ee=0.0060

---

**注意**: westd-45947 cuda:0 实际 PID 是 460442（非预期的 460433），可能是 resume 后新进程。

---
