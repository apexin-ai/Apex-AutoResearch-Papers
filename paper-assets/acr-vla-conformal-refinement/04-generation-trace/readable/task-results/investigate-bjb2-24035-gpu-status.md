# investigate bjb2 24035 gpu status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_bjb2-24035-gpu-status_20260526T101410_result.json`
- **Structured JSON:** [`2832b7d5bd7878be3e70.json`](../../sessions/28/2832b7d5bd7878be3e70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 占用排查结果

**GPU 0 (RTX 4090D)：10303 MiB，PID 3035**

| 字段 | 值 |
|---|---|
| PID | 3035 |
| 用户 | root |
| 运行时间 | 05:57:06（约 6 小时）|
| 启动时间 | 2026-05-26 12:17:52 |
| CWD | /root/acr-vla-conformal-refinement |
| stdout/stderr | /tmp/westd-pi05-adaptive-object-s43.log |

**命令行：**
```
python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm \
  --K 2 --max_correction_norm 0.2 --conformal_threshold 0.25 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt \
  --obs_dim 2048 --unified_obs_dim 2088 \
  --benchmark object --seed 43 --n_rollouts 20 \
  --output_file logs/eval_object_adaptive_pi05_seed43.json
```

**对应实验：** pi05 模型 adaptive_conformal_crm 评测，object benchmark，seed 43，K=2，max_correction_norm=0.2，conformal_threshold=0.25。

**进度：** 已完成 5/10 任务（goal benchmark 名称的任务对应 object suite），正在第 6 个任务 `pick_up_the_chocolate_pudding_and_place_it_in_the_basket`（15/20 rollout）。当前未完成，输出文件 `logs/eval_object_adaptive_pi05_seed43.json` 还未生成。

**注意：** 该进程不是从 tmux 启动（log 路径在 /tmp，且 registry 未登记）——可能是用户在 ssh 会话里用 `nohup` 或后台 `&` 启动的"野进程"，没有走 submit_training_job，所以 registry 没有记录。`tmux ls` 在 ssh_read_only 白名单外无法验证。

---
