# diagnose eval gsm8k grpo standard 20 step50

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_gsm8k_grpo_standard_20_step50_20260520T024845_result.json`
- **Structured JSON:** [`56ab841f111a94b2ad57.json`](../../sessions/56/56ab841f111a94b2ad57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息汇总完毕。

**诊断结论：**

- `grpo_stage2_standard_20_fair/checkpoint-50` 被训练过程的 `save_total_limit=3` 自动清理（只保留了 80/90/100）
- 旧版 `grpo_standard_v8_step50` checkpoint 也已删除
- `grpo_standard_20_extended_300` 目录也已清理
- 服务器上**不存在任何 step-50 checkpoint**
- D080 已决定用 E2 300 步 GSM8K 59.29% (782/1319) 替代 step-50 重跑
- 旧版 v8 run 的结果文件仍在：`/root/recovery_aware_struct_prune/results/eval_grpo_standard_step50_full.json`（58.91%, 777/1319）
- 最早可用的同训练 run checkpoint 是 checkpoint-80

```json
{"root_cause":"checkpoint-50 被 save_total_limit=3 自动清理，仅保留 80/90/100。旧版 v8 step-50 checkpoint 也已删除。服务器无任何 step-50 checkpoint。","correct_path":"不存在","error_type":"infrastructure","fix_steps":["方案A：用已有 v8 结果文件 eval_grpo_standard_step50_full.json (58.91%, 777/1319) 作为 provenance","方案B：用 D080 决定的 E2 300步结果 eval_gsm8k_grpo_standard_20_extended_300.json (59.29%, 782/1319) 替代","方案C：用最早可用的 checkpoint-80 重跑 eval（同 training run，非 step-50）"],"can_auto_fix":false,"available_checkpoints":["grpo_stage2_standard_20_fair/checkpoint-80","grpo_stage2_standard_20_fair/checkpoint-90","grpo_stage2_standard_20_fair/checkpoint-100"],"existing_results":{"v8_step50":"results/eval_grpo_standard_step50_full.json (58.91%)","extended_300":"results/eval_gsm8k_grpo_standard_20_extended_300.json (59.29%)"}}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "checkpoint-50 被 save_total_limit=3 自动清理，仅保留 80/90/100。旧版 v8 step-50 checkpoint 也已删除。服务器无任何 step-50 checkpoint。",
    "correct_path": "不存在",
    "error_type": "infrastructure",
    "fix_steps": [
      "方案A：用已有 v8 结果文件 eval_grpo_standard_step50_full.json (58.91%, 777/1319) 作为 provenance",
      "方案B：用 D080 决定的 E2 300步结果 eval_gsm8k_grpo_standard_20_extended_300.json (59.29%, 782/1319) 替代",
      "方案C：用最早可用的 checkpoint-80 重跑 eval（同 training run，非 step-50）"
    ],
    "can_auto_fix": false,
    "available_checkpoints": [
      "grpo_stage2_standard_20_fair/checkpoint-80",
      "grpo_stage2_standard_20_fair/checkpoint-90",
      "grpo_stage2_standard_20_fair/checkpoint-100"
    ],
    "existing_results": {
      "v8_step50": "results/eval_grpo_standard_step50_full.json (58.91%)",
      "extended_300": "results/eval_gsm8k_grpo_standard_20_extended_300.json (59.29%)"
    }
  }
}
```

</details>

---
