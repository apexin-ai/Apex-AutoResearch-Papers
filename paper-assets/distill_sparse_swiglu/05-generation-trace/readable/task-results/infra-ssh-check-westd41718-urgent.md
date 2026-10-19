# infra ssh check westd41718 urgent

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_ssh_check_westd41718_urgent_20260517T215634_result.json`
- **Structured JSON:** [`fb662f7a3c2f18c516bd.json`](../../sessions/fb/fb662f7a3c2f18c516bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都正常运行，不是挂了或异常：

| 实验 | GPU | PPL | GSM8K 进度 | 预计剩余 |
|------|-----|-----|-----------|---------|
| qwen14b_teal30_eval | cuda:1 94% | 8.7332 | 87% (1153/1319) | ~46 min |
| qwen14b_dense_baseline | cuda:0 97% | 5.1854 | 81% (1065/1319) | ~9 min |

两个都已完成 wikitext2 PPL + ARC-c + WinoGrande + MMLU 评估，正在跑最后的 GSM8K generate_until。完整指标会在 GSM8K 跑完后由脚本统一输出。无任何错误。Cron 回调失效不影响实验本身。

报告已写入 `artifacts/westd41718_check_results.md`。

---
