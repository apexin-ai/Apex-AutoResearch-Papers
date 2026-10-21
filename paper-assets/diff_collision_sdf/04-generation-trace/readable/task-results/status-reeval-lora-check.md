# status reeval lora check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_reeval_lora_check_20260527T100436_result.json`
- **Structured JSON:** [`a6ec661e1f6dab9dccac.json`](../../sessions/a6/a6ec661e1f6dab9dccac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. reeval_lora_s0_30k_v2 (cuda:1, PID 747037)
**ALIVE** — 运行 15 分 44 秒

当前日志：正在 eval Task 1 `pick_up_the_chocolate_pudding_and_place_it_in_the_basket` (Safety Level II)，已完成 30/50 episodes。上一个 task (Task 0) 结果：TSR=18.0% (9/50), CAR=68.0% (34/50)。

### 2. eval s1 (cuda:2)
**有新 eval 进程** — PID 760035，启动于 ~18:03，运行在 GPU-2 (8995 MiB)。从 ps 输出中可以看到其 compile workers (parent=760035)，确认是 eval 进程。

另外 PID 751737 也在 GPU-0 上 (8995 MiB)，加上 tmux 里的 `train_pi05_a1_spatial_bowl_s0_l005` 训练也挂在 GPU-0。

### 3. nvidia-smi 快照

| GPU | 利用率 | 显存占用 | 进程 |
|-----|--------|----------|------|
| 0 | 51% | 9014 MiB | PID 751737 (eval/其他) |
| 1 | 0% | 8365 MiB | PID 747037 (reeval_lora_s0_30k_v2) — GPU idle，正在跑 episode |
| 2 | 23% | 9014 MiB | PID 760035 (eval s1) |
| 3 | 100% | 27037 MiB | PID 341425 (train lora_baseline spatial_bowl s0) |

4 张卡全在用。

---
