# diagnose 34685 dead process

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_34685-dead-process_20260527T103909_result.json`
- **Structured JSON:** [`06aed19e9b3f80e09a24.json`](../../sessions/06/06aed19e9b3f80e09a24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### detach_ln_v2_s1 (GPU 0): **正常运行中**
- 当前 step: **40986/50005 (82%)**，速度 ~1.07 it/s
- ETA: **~2h18m**
- Checkpoint: 30000 和 40000 已保存，50000 尚未到达
- tmux session 消失但进程仍在（GPU 0 占用 98%/62GB）

### 其他 3 个实验状态

| 实验 | GPU | Step | 进度 | ETA |
|------|-----|------|------|-----|
| detach_ln_s4 | 1 (99%, 62GB) | 41034/50005 | 82% | ~2h19m |
| ablation_occ_detach_s4 | 2 (99%, 62GB) | 38193/50005 | 76% | ~3h06m |
| mvp_occ_s4 | 3 (76%, 63GB) | 38132/50005 | 76% | ~3h12m |

### 结论
- **4 个实验全部正常运行**，无需干预
- GPU 0 **不空闲**
- 所有实验预计在 deadline (2026-05-28 12:00 UTC) 前完成

---
