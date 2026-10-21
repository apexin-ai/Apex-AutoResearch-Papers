# verify westd35807 gpu state

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_westd35807_gpu_state_20260527T144902_result.json`
- **Structured JSON:** [`da4fd3eef3ecfca247a5.json`](../../sessions/da/da4fd3eef3ecfca247a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

与期望状态**完全一致**：

| GPU | 显存占用 | GPU利用率 | PID | 运行时长 | 任务 |
|-----|---------|----------|-----|---------|------|
| cuda:0 | 0 MiB / 97887 MiB | 0% | — | — | 空闲 ✓ |
| cuda:1 | 19055 MiB / 97887 MiB | 100% | 856552 | 23h49m | Stage 1 seed0 λ=0.005 ✓ |
| cuda:2 | 27045 MiB / 97887 MiB | 100% | 856471 | 23h52m | Stage 2 seed2 λ=0 (resume) ✓ |
| cuda:3 | 27037 MiB / 97887 MiB | 92% | 341425 | 1d 2h21m | LoRA baseline seed0 ✓ |

三个训练进程均在正常运行，cuda:0 已释放。

---
