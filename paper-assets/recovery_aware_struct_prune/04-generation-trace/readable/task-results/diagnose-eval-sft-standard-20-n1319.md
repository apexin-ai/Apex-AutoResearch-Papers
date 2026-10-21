# diagnose eval sft standard 20 n1319

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_sft_standard_20_n1319_20260517T012508_result.json`
- **Structured JSON:** [`22077234c00f5a681671.json`](../../sessions/22/22077234c00f5a681671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：实验正常完成，应改为 success

**日志路径**: `/root/runs/recovery_aware_struct_prune/eval_sft_standard_20_n1319.log`

**关键尾部日志**:
```
2026-05-17 09:01:52,484 [INFO] GSM8K Accuracy: 0.5929 ± 0.0135 (782/1319)
2026-05-17 09:01:52,484 [INFO] EOS Stats: {
  "natural_eos": 1293,
  "truncated": 26,
  "eos_rate": 0.9802880970432145,
  "avg_response_length": 226.73692191053829,
  "max_response_length": 4096,
  "min_response_length": 32
}
2026-05-17 09:01:52,496 [INFO] Results saved to /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_20_full_westd.json
```

**确认**:
- 1319/1319 样本全部完成，进度条 100%
- accuracy = 0.5929 (782/1319)，与 registry 完全匹配
- eos_rate = 0.9803，匹配
- 无 error/traceback
- 结果 JSON 已正常写出

评估完全正常完成。Cron 标记 failed 是误判（缺少 W&B sentinel 但实际任务已成功结束）。应改为 success。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "natural_eos": 1293,
    "truncated": 26,
    "eos_rate": 0.9802880970432145,
    "avg_response_length": 226.73692191053829,
    "max_response_length": 4096,
    "min_response_length": 32
  }
}
```

</details>

---
