# infra check all evals status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_all_evals_status_20260517T171213_result.json`
- **Structured JSON:** [`6e3bfb8dc95ad809cf47.json`](../../sessions/6e/6e3bfb8dc95ad809cf47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个任务全部在运行中，无结果文件产出。汇总：

```
exp_id                      | status  | progress
─────────────────────────────┼─────────┼──────────────────────────────────────────────
qwen14b_kl30_s42            | running | PPL=7.6232 ✓; arc ✓; wino+mmlu ✓; gsm8k 49% (641/1319, ~2h left)
qwen14b_bce30_s42_eval      | running | PPL=8.7634 ✓; arc ✓; wino+mmlu 70% (41125/58702, ~3min left); gsm8k 未开始 (~3.5h)
qwen14b_teal30              | running | PPL=8.7332 ✓; arc ✓; wino+mmlu ✓; gsm8k 13% (169/1319, ~5.8h left)
downstream_teal30_baseline  | running | hellaswag 5% (1865/40168, ~35min left); piqa+boolq 未开始 (~30min)
```

备注：
- **KL30 s42** (westd-34887 cuda:1): 最快，预计 ~2h 完成
- **BCE30 s42** (westd-34887 cuda:0): MMLU 快完成，但 GSM8K 还要 ~3.5h
- **teal30** (westd-41718 cuda:1): GSM8K 生成速度慢 (~18.4s/item vs 34887 的 ~10s/item)，预计 ~6h
- **downstream baseline** (westd-41718 cuda:0): LLaMA-8B 上的 hellaswag/piqa/boolq，预计 ~1h 完成

---
