# diagnose grpo v2 step50 eval

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_v2_step50_eval_20260513T103847_result.json`
- **Structured JSON:** [`2a0c277f3f13a7f14aae.json`](../../sessions/2a/2a0c277f3f13a7f14aae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部拿到。

```json
{
  "step50_eval_metrics": {
    "RE_F1": 0.4384,
    "Evidence_F1": 0.3705,
    "Attribution_Precision": 0.9424,
    "samples": 985
  },
  "eval_output_file": "/root/autodl-tmp/prov_grounded_uie/outputs/grpo_v2_step50/eval_results.json",
  "step100_checkpoint_exists": true,
  "final_checkpoint_exists": true,
  "eval_script_content": "eval_grpo_v2.sh 做两步: (A) 将 LoRA adapter 合并到 SFT base model (outputs/sft/merged), 保存到 outputs/&lt;name>/merged; (B) 用 evaluate.py 在合并模型上跑评估, 输出 outputs/&lt;name>/eval_results.json"
}
```

关键发现：
- **训练已跑完 100 步**，checkpoint-50、checkpoint-100、final 三个 checkpoint 都在（final 时间戳与 checkpoint-100 相同，说明 100 步就是最终步）
- step50 eval 指标：RE-F1=43.8%, Evi-F1=37.1%, AP=94.2%
- checkpoint-100 尚未 eval

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "step50_eval_metrics": {
      "RE_F1": 0.4384,
      "Evidence_F1": 0.3705,
      "Attribution_Precision": 0.9424,
      "samples": 985
    },
    "eval_output_file": "/root/autodl-tmp/prov_grounded_uie/outputs/grpo_v2_step50/eval_results.json",
    "step100_checkpoint_exists": true,
    "final_checkpoint_exists": true,
    "eval_script_content": "eval_grpo_v2.sh 做两步: (A) 将 LoRA adapter 合并到 SFT base model (outputs/sft/merged), 保存到 outputs/&lt;name>/merged; (B) 用 evaluate.py 在合并模型上跑评估, 输出 outputs/&lt;name>/eval_results.json"
  }
}
```

</details>

---
