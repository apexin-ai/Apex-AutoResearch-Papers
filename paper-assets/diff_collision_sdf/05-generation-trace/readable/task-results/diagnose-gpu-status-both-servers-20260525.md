# diagnose gpu status both servers 20260525

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu_status_both_servers_20260525_20260525T203224_result.json`
- **Structured JSON:** [`0628132310bdfb223bdc.json`](../../sessions/06/0628132310bdfb223bdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### westd-35807（4× RTX PRO 6000 96GB）

| GPU | 显存占用 | 利用率 | 进程 | PID |
|-----|---------|--------|------|-----|
| cuda:0 | 27045/97887 MiB | 100% | train_pi05_a1_spatial_bowl_s0_l005 | 3717 |
| cuda:1 | 9010/97887 MiB | 1% | eval_30k_s1_l005_disp | 142394 |
| cuda:2 | 9010/97887 MiB | 14% | eval_best_s1_l005_16k | 134344 |
| cuda:3 | 9016/97887 MiB | 51% | eval_s0_l005_30k_r4 | 151915 |

**Tmux sessions**: train_pi05_a1_spatial_bowl_s0_l005, eval_pi05_a1_30k_s1_l005_disp, eval_pi05_a1_30k_s0_l005_r4

**磁盘**: root 23/30G (75%), autodl-tmp 210/350G (60%)

---

### westd-45947（2× RTX PRO 6000 96GB）

| GPU | 显存占用 | 利用率 | 进程 | PID |
|-----|---------|--------|------|-----|
| cuda:0 | 27089/97887 MiB | 100% | train_pi05_lora_baseline_s0 | 3634 |
| cuda:1 | 27089/97887 MiB | 100% | train_pi05_lora_baseline_s1 | 3724 |

**Tmux sessions**: train_pi05_lora_baseline_s0, train_pi05_lora_baseline_s1

**磁盘**: root 19/30G (61%)

---

### 空闲 GPU

**无**。6 张 GPU 全部占用。

---

### 3 个训练实验进度

| 实验 | 当前 step | 进度 | 速度 | 预估剩余 | 预计完成 (UTC) |
|------|----------|------|------|---------|---------------|
| spatial_bowl_s0_l005 | 9917/30000 | 33% | 4.63 s/it | ~25.8h | ~May 27 06:30 |
| lora_baseline_s0 | 26116/30000 | 87% | 4.62 s/it | ~5.0h | ~May 26 09:30 |
| lora_baseline_s1 | 26117/30000 | 87% | 4.63 s/it | ~5.0h | ~May 26 09:30 |

---

### 2 个 Eval 实验状态

**eval_pi05_a1_best_s1_l005_16k** — 在跑，即将完成
- GPU 2, PID 134344, via submit_training_job
- 进度：Task 3/4（最后一个 task），episode 40/50
- 预计 ~5 分钟内完成
- 输出：`/root/autodl-tmp/eval_results/eval_s1_l005_best_16k.json`（尚未生成）

**eval_pi05_a1_30k_s1_l005_disp** — 在跑
- GPU 1, PID 142394, tmux session
- 进度：Task 3/4（最后一个 task），episode 10/50
- 预计 ~10-15 分钟内完成
- 输出：`/root/autodl-tmp/eval_results/eval_s1_l005_30k_disp.json`（尚未生成）

**额外发现**：GPU 3 还跑着一个 eval_s0_l005_30k_r4（PID 151915, tmux session `eval_pi05_a1_30k_s0_l005_r4`），输出到 `eval_s0_l005_30k_r4.json`，04:08 启动。

---
