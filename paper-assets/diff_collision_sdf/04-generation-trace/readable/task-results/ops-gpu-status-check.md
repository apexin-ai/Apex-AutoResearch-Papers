# ops gpu status check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260525T185246_result.json`
- **Structured JSON:** [`d7a53e6a817cfbd8feac.json`](../../sessions/d7/d7a53e6a817cfbd8feac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 占用汇总

| 服务器 | GPU | 显存占用 | util% | 进程 | 对应实验 |
|--------|-----|----------|-------|------|----------|
| **westd-35807** | cuda:0 | 27045/97887 MiB | 100% | PID 3717 | `train_a1_sdf_aux_pi05.py --scene spatial_bowl --seed 0 --resume` |
| **westd-35807** | cuda:1 | 8483/97887 MiB | 0% | PID 6667 | `eval_safelibero.py` s0_l005_30k_final (object_pudding) |
| **westd-35807** | cuda:2 | 9142/97887 MiB | 11% | PID 7094 | `eval_safelibero.py` s0_l01_30k_final (object_pudding) |
| **westd-35807** | cuda:3 | 1 MiB | 0% | — | **空闲** |
| **westd-45947** | cuda:0 | 27089/97887 MiB | 100% | PID 3634 | `train_pi05_lora_baseline.py --scene object_pudding --seed 0 --resume` |
| **westd-45947** | cuda:1 | 27089/97887 MiB | 100% | PID 3724 | `train_pi05_lora_baseline.py --scene object_pudding --seed 1 --resume` |

**空闲卡：westd-35807:cuda:3**（完全空闲），cuda:1 和 cuda:2 在跑 eval 但显存占用不大，eval 结束后也会释放。

**westd-45947 满载**，两张卡都在跑 lora baseline 训练。

---
