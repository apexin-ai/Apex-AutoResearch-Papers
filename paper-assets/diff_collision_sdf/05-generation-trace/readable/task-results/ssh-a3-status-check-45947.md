# ssh a3 status check 45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a3_status_check_45947_20260520T092216_result.json`
- **Structured JSON:** [`3b90cd125dc43928762d.json`](../../sessions/3b/3b90cd125dc43928762d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 实验 | PID | Step/30000 | Loss | Speed(s/it) | VRAM | 状态 |
|-----|------|-----|------------|------|-------------|------|------|
| 0 | spatial_bowl | 71494 | 1012/30000 (3%) | 0.2671 | ~3.1s | 16.9/95.6 GB | 运行中 (1h23m) |
| 1 | object_pudding | 73165 | 3461/30000 (12%) | 0.2275 | ~3.3s | 16.9/95.6 GB | 运行中 (1h22m) |

- object_pudding 从 step 2500 恢复（checkpoint resume），实际已跑 ~961 步新 step
- GPU utilization 瞬时显示 0%（查询间隙），但训练速度正常
- 磁盘：/root/autodl-tmp 22G/250G (9%)，充裕

---
