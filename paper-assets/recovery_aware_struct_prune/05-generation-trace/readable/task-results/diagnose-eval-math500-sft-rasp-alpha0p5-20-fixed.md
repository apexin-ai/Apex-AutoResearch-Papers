# diagnose eval math500 sft rasp alpha0p5 20 fixed

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_rasp_alpha0p5_20_fixed_20260523T224722_result.json`
- **Structured JSON:** [`a324cd36ff7893080d51.json`](../../sessions/a3/a324cd36ff7893080d51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```json
{
  "result_file_exists": false,
  "accuracy": null,
  "root_cause": "批量 SIGTERM 杀进程。同批至少 4 个 _fixed eval 在 21:15-22:24 UTC 被外部 SIGTERM/SIGHUP 终止（sft_standard_20_fixed @ 21:15:04 exit=143, sft_standard_25_fixed @ 21:15:03 exit=129, sft_standard_20_fixed_v3 @ 22:18:51 exit=143, sft_rasp_alpha0p5_20 @ 22:24:26 exit=143）。两个 job 在同一秒被杀证明是 scheduler/batch kill 操作，非 OOM（OOM 是 SIGKILL=137）。",
  "model_path_exists": true,
  "gpu_status": "cuda:3 被 PID 168451 占用 (eval_math500_grpo_cka_only_25_fixed, 已跑 1h18m, 16846MiB/97887MiB, 94% util)",
  "old_eval_exists": true,
  "old_eval_accuracy": "25.4% (127/500, non-fixed eval script)",
  "fix_steps": [
    "等 cuda:3 当前 job (grpo_cka_only_25_fixed) 完成",
    "重跑: CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha0p5_20_fixed.json",
    "同样需要重跑的被杀 jobs: sft_standard_20_fixed, sft_standard_25_fixed"
  ],
  "can_auto_fix": true
}
```

**关键发现**：不是单个 job 的问题，而是 5月23日 21:15-22:24 UTC 时段内发生了一次批量进程清理，至少 4 个 _fixed eval 被 SIGTERM。已完成的 _fixed eval（如 sft_rasp_alpha1p0、grpo_rasp_alpha1p0、grpo_standard_20）都正常生成了结果文件，被杀的都没有结果文件。cuda:3 当前有任务在跑，完成后可以重跑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "result_file_exists": false,
    "accuracy": null,
    "root_cause": "批量 SIGTERM 杀进程。同批至少 4 个 _fixed eval 在 21:15-22:24 UTC 被外部 SIGTERM/SIGHUP 终止（sft_standard_20_fixed @ 21:15:04 exit=143, sft_standard_25_fixed @ 21:15:03 exit=129, sft_standard_20_fixed_v3 @ 22:18:51 exit=143, sft_rasp_alpha0p5_20 @ 22:24:26 exit=143）。两个 job 在同一秒被杀证明是 scheduler/batch kill 操作，非 OOM（OOM 是 SIGKILL=137）。",
    "model_path_exists": true,
    "gpu_status": "cuda:3 被 PID 168451 占用 (eval_math500_grpo_cka_only_25_fixed, 已跑 1h18m, 16846MiB/97887MiB, 94% util)",
    "old_eval_exists": true,
    "old_eval_accuracy": "25.4% (127/500, non-fixed eval script)",
    "fix_steps": [
      "等 cuda:3 当前 job (grpo_cka_only_25_fixed) 完成",
      "重跑: CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha0p5_20_fixed.json",
      "同样需要重跑的被杀 jobs: sft_standard_20_fixed, sft_standard_25_fixed"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
