# check spatial bowl lora alive

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_spatial_bowl_lora_alive_20260527T142003_result.json`
- **Structured JSON:** [`2c7bd863d303a77ebfa8.json`](../../sessions/2c/2c7bd863d303a77ebfa8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程存活：

- **PID**: 341425
- **运行时间**: 1天1小时52分27秒
- **命令**: `python scripts/train_pi05_lora_baseline.py --scene spatial_bowl --seed 0 --gpu 3 --batch_size 32 --num_train_steps 30000 --lr 2.5e-5 --save_interval 2000 --log_interval 100`
- **GPU**: cuda:3，显存占用 27028 MiB

进程正常运行中，不受 lerobot 版本问题影响（走的是 `train_pi05_lora_baseline.py` 脚本）。

---
