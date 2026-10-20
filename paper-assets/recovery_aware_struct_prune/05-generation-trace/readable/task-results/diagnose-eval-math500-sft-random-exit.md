# diagnose eval math500 sft random exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_random_exit_20260522T140838_result.json`
- **Structured JSON:** [`365878f98851980e9f00.json`](../../sessions/36/365878f98851980e9f00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

```
=== LOG ===
(logs/eval_math500_sft_random_20_v3.log — 末尾)
...
MATH-500 eval: 100%|██████████| 500/500 [9:54:42<00:00, 71.37s/it]
2026-05-22 22:08:06,287 [INFO] MATH-500 Accuracy: 0.1440 +/- 0.0157 (72/500)
2026-05-22 22:08:06,288 [INFO] EOS Stats: {
  "natural_eos": 171,
  "truncated": 329,
  "avg_response_length": 1470.44
}
2026-05-22 22:08:06,290 [INFO] Results saved to /root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json

(results/eval_math500_sft_random_20_v3.log — NO_LOG_AT_RESULTS)

=== RESULT FILE ===
-rw-r--r-- 1 root root 165884 May 22 22:08 /root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json

(autodl-tmp 下无同名文件)

=== RESULT CONTENT ===
eval_math500_sft_random_20_v3.json: accuracy=0.144, stderr=0.0157

=== PID CHECK ===
PID 5236: EXITED
PID 5241: EXITED

=== GPU ===
0, 29599 MiB, 99 %
1, 0 MiB, 0 %
2, 26219 MiB, 99 %
3, 0 MiB, 0 %
```

**结论**：eval_math500_sft_random_20_v3 已正常完成退出。500 题全部跑完，accuracy = 14.4% (72/500)，结果已写入 JSON。进程已退出。GPU 0 和 2 被其他任务占用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "natural_eos": 171,
    "truncated": 329,
    "avg_response_length": 1470.44
  }
}
```

</details>

---
