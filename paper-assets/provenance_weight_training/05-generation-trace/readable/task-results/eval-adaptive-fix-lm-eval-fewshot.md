# eval adaptive fix lm eval fewshot

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_adaptive_fix_lm_eval_fewshot_20260517T150643_result.json`
- **Structured JSON:** [`b1d6ecb4e55e3df8dcd6.json`](../../sessions/b1/b1d6ecb4e55e3df8dcd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个评估任务完成。汇总结果：

## adaptive_fix_seed42 (Qwen3-0.6B) 评估结果

| Task | num_fewshot | acc | acc_norm |
|------|-------------|-----|----------|
| **HellaSwag** | 10 | 0.3818 | **0.4863** |
| **ARC-Easy** | 25 | **0.7100** | **0.7121** |
| **PIQA** | 5 | **0.6866** | **0.6839** |
| **WinoGrande** | 5 | **0.5635** | - |

每个 task 的 num_fewshot 已从 JSON 中确认一致：HellaSwag=10, ARC-Easy=25, PIQA=5, WinoGrande=5。

结果保存在 `westd-41312:/root/autodl-tmp/provenance_weight_training/output/eval/adaptive_fix_fewshot/`。

---
