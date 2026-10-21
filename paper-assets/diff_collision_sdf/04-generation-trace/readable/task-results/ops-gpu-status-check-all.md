# ops gpu status check all

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_all_20260525T191845_result.json`
- **Structured JSON:** [`843159905f5a0a57462a.json`](../../sessions/84/843159905f5a0a57462a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-35807

| GPU | 显存占用 | 利用率 | 进程/实验 |
|-----|---------|--------|----------|
| 0   | 27045/97887 MiB | 100% | PID 3717 — `train_a1_sdf_aux_pi05.py --scene spatial_bowl --seed 0 --resume` |
| 1   | 9128/97887 MiB | 14% | PID 6667 — `eval_safelibero.py` s0_l005 30k final |
| 2   | 9142/97887 MiB | 37% | PID 7094 — `eval_safelibero.py` s0_l01 30k final |
| 3   | 27011/97887 MiB | 69% | PID 35423+72605+75123 — 3 个 `eval_safelibero.py` s2_l005 best 10k（n_episodes=200 + 2个默认） |

## westd-45947

| GPU | 显存占用 | 利用率 | 进程/实验 | 当前 step |
|-----|---------|--------|----------|-----------|
| 0   | 27089/97887 MiB | 100% | LoRA baseline s0 resume2 | 25158/30000 (84%), ~4.62s/it |
| 1   | 27089/97887 MiB | 100% | LoRA baseline s1 resume2 | 25158/30000 (84%), ~4.62s/it |

**状态总结：**
- 6 张卡全部在工作，GPU 利用率正常
- westd-45947 两个 LoRA baseline 稳步推进中，step 已到 25158，预计剩余 ~6h13m
- westd-35807 GPU 0 spatial_bowl 训练继续；GPU 1-3 在跑 eval，其中 GPU 3 同时跑了 3 个 eval 进程（都是 s2_l005 best checkpoint，可能有重复提交）

---
