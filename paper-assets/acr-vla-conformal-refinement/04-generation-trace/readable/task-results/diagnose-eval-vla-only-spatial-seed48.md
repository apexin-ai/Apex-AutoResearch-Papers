# diagnose eval vla only spatial seed48

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-vla-only-spatial-seed48_20260519T210122_result.json`
- **Structured JSON:** [`7706fba52cbeebfe2430.json`](../../sessions/77/7706fba52cbeebfe2430.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论清楚了。这 **不是** cron false positive——实验实际在第 4 个 task 执行中途被终止。

关键证据：
- 日志 `/root/acr-vla-conformal-refinement/logs/eval_spatial_vla_only_seed48.log` 在 04:31 创建，05:00 停止写入
- 只完成 3/10 个 task，在第 4 个 task 的 rollout 5/10 处截断
- 无 Python traceback → 进程被外部信号 SIGKILL 终止（非 Python 异常）
- 无输出 JSON 文件
- runs/ 目录无对应 cron 日志（cron 系统未正常捕获此任务）
- 磁盘正常（33% used），无法读 dmesg（容器限制）
- 同时段有多个实验在跑（seed46/47 spatial、seed46/47 long、goal evals），可能存在 GPU 争抢

```json
{"completed": false, "overall_success_rate": null, "per_task": {"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate": 0.7, "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate": 1.0, "pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate": 0.0}, "root_cause": "Process killed by external signal (SIGKILL) during task 4/10 rollout 5/10. No Python traceback in log. Most likely GPU OOM or resource contention — multiple eval jobs (spatial seed46/47, long seed46/47, goal evals) were running concurrently around 04:30-05:00 on May 20. No cron log in runs/ suggests cron management may not have tracked this job properly.", "fix_steps": ["Rerun with dedicated GPU: CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 48 --K 1 --output_file logs/eval_spatial_vla_only_seed48.json", "Ensure no other experiment is scheduled on GPU 5 concurrently", "Redirect stderr to capture potential OOM messages: 2>&1 | tee logs/eval_spatial_vla_only_seed48.log"]}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "completed": false,
    "overall_success_rate": null,
    "per_task": {
      "pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate": 0.7,
      "pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate": 1.0,
      "pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate": 0.0
    },
    "root_cause": "Process killed by external signal (SIGKILL) during task 4/10 rollout 5/10. No Python traceback in log. Most likely GPU OOM or resource contention — multiple eval jobs (spatial seed46/47, long seed46/47, goal evals) were running concurrently around 04:30-05:00 on May 20. No cron log in runs/ suggests cron management may not have tracked this job properly.",
    "fix_steps": [
      "Rerun with dedicated GPU: CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python -u src/evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 48 --K 1 --output_file logs/eval_spatial_vla_only_seed48.json",
      "Ensure no other experiment is scheduled on GPU 5 concurrently",
      "Redirect stderr to capture potential OOM messages: 2>&1 | tee logs/eval_spatial_vla_only_seed48.log"
    ]
  }
}
```

</details>

---
