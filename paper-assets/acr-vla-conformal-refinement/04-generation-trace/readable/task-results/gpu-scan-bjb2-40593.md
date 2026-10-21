# gpu scan bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu-scan_bjb2-40593_20260520T103616_result.json`
- **Structured JSON:** [`1b9a4c52e74d43a5f35e.json`](../../sessions/1b/1b9a4c52e74d43a5f35e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
SERVER: bjb2-40593
GPU_STATUS: RTX 4090 D | 2267MiB/24564MiB | 18% util | 37°C | PID 681823 占用 2249MiB
PID 681823: ALIVE | stat=Rl+ | etime=03:22:00 | python -u src/evaluate.py --mode adaptive_k --benchmark spatial --seed 42
OUTPUT_JSON: NOT_FOUND（尚未生成，实验仍在运行）
LOG: /root/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p50-seed42.log (2362B, last modified 15:10)
  - 已完成 3/10 tasks:
    - pick_up_the_black_bowl_between_the_plate_and_the_ramekin: 70.0% (7/10)
    - pick_up_the_black_bowl_next_to_the_ramekin: 100.0% (10/10)
    - pick_up_the_black_bowl_from_table_center: 0.0% (0/10)
  - 当前正在运行第 4 个 task: pick_up_the_black_bowl_on_the_cookie_box (5/10 rollouts, 1 success)
TMUX: eval-adaptive-k-spatial-p50-seed42 session 存在（tmux ls 被 read_only 拦截，但 ps 显示 tmux PID 681816）
EXIT_FILE: NOT_FOUND（无 spatial-p50-seed42 的 exit file）
CONCLUSION: STILL_RUNNING — 已运行 3h22m，完成 3/10 tasks，预计还需约 7 小时完成剩余 7 个 tasks。
```

---
