# diagnose llama31 s123 eval failures

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama31-s123-eval-failures_20260516T152117_result.json`
- **Structured JSON:** [`9c24d6c7971c4e1efb9c.json`](../../sessions/9c/9c24d6c7971c4e1efb9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。结果如下：

```json
{
  "exp_id": "llama31-random-s123-clean",
  "actually_completed": true,
  "metrics": {"success_rate": 0.766},
  "output_file": "eval_results/llama31_random_s123_clean.json",
  "error_if_any": null
}
```

```json
{
  "exp_id": "llama31-taxei-s123-clean",
  "actually_completed": true,
  "metrics": {"success_rate": 0.617},
  "output_file": "eval_results/llama31_taxei_s123_clean.json",
  "error_if_any": null
}
```

```json
{
  "exp_id": "llama31-taxei-s123-eval",
  "actually_completed": false,
  "metrics": null,
  "output_file": null,
  "error_if_any": "仍在运行中 (PID 293496, 进度 35/47 episodes)，预计还需 ~5 分钟完成。输出将写入 eval_results/llama31_taxei_s123_injected.json"
}
```

**总结：**
- 实验 1 和 2（recovery.py clean eval）已正常完成，cron 误报 confirmed。
- 实验 3（injected_eval.py）正在运行，35/47 已完成，未出错。另外还有一个排队的 `llama31_random_s123_injected` eval 也在跑（PID 294869）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp_id": "llama31-taxei-s123-eval",
    "actually_completed": false,
    "metrics": null,
    "output_file": null,
    "error_if_any": "仍在运行中 (PID 293496, 进度 35/47 episodes)，预计还需 ~5 分钟完成。输出将写入 eval_results/llama31_taxei_s123_injected.json"
  }
}
```

</details>

---
