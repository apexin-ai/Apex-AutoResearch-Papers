# diagnose westb evals status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westb_evals_status_20260518T181031_result.json`
- **Structured JSON:** [`0b325c682fd328e0f9c5.json`](../../sessions/0b/0b325c682fd328e0f9c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都活着且在跑。结果 JSON 尚未生成（只有之前的 quick 版本）。

```json
{
  "eval_gsm8k_grpo_cka_only_20_1p5b": {
    "alive": true,
    "progress": "828/1319 (63%)",
    "accuracy": "0.3538 @ 800",
    "eos_rate": "95.25%",
    "avg_len": 327,
    "log_tail": "正常推进中，无错误"
  },
  "eval_gsm8k_grpo_standard_20_1p5b": {
    "alive": true,
    "progress": "509/1319 (39%)",
    "accuracy": "0.2320 @ 500",
    "eos_rate": "91.40%",
    "avg_len": 476,
    "log_tail": "正常推进中，无错误"
  },
  "gpu_status": "cuda:0 = 99% util, 6537MiB/97887MiB (PID 823050, standard eval); cuda:1 = 96% util, 6555MiB/97887MiB (PID 822503, cka_only eval)"
}
```

两个 eval 都从 00:36~00:39 启动，已跑约 1.5 小时。CKA-only 进度更快（63% vs 39%），Standard 的 avg_len 更长（476 vs 327）导致推理更慢。按当前速度预估 CKA-only 还需约 50 分钟，Standard 还需约 2.5 小时完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "eval_gsm8k_grpo_cka_only_20_1p5b": {
      "alive": true,
      "progress": "828/1319 (63%)",
      "accuracy": "0.3538 @ 800",
      "eos_rate": "95.25%",
      "avg_len": 327,
      "log_tail": "正常推进中，无错误"
    },
    "eval_gsm8k_grpo_standard_20_1p5b": {
      "alive": true,
      "progress": "509/1319 (39%)",
      "accuracy": "0.2320 @ 500",
      "eos_rate": "91.40%",
      "avg_len": 476,
      "log_tail": "正常推进中，无错误"
    },
    "gpu_status": "cuda:0 = 99% util, 6537MiB/97887MiB (PID 823050, standard eval); cuda:1 = 96% util, 6555MiB/97887MiB (PID 822503, cka_only eval)"
  }
}
```

</details>

---
