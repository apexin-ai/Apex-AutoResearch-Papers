# infra collect all running eval results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_collect_all_running_eval_results_20260517T204113_result.json`
- **Structured JSON:** [`ab3d981d721cb70c3187.json`](../../sessions/ab/ab3d981d721cb70c3187.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验均存活且正在运行 GSM8K generate_until（最后一个 task），结果在 GSM8K 跑完后统一输出。

## 状态汇总

| 实验ID | 服务器 | 状态 | PPL | ARC | WG | MMLU | GSM8K | 备注 |
|--------|--------|------|-----|-----|----|----- |-------|------|
| qwen14b_teal30_eval | westd-41718 | RUNNING | 8.7332 | 待出 | 待出 | 待出 | 67% (881/1319) | ETA ~2h, 17s/it |
| qwen14b_dense_baseline | westd-41718 | RUNNING | 5.1854 | 待出 | 待出 | 待出 | 34% (449/1319) | ETA ~1-3h, 速率波动大 |
| qwen14b_bce30_s42_eval | westd-34887 | RUNNING | 8.7634 | 待出 | 待出 | 待出 | 61% (809/1319) | ETA ~2h, 14.7s/it |
| bce_isocompute_v3_s456_eval | westd-34887 | RUNNING | 28.3503 | 待出 | 待出 | 待出 | 90% (1193/1319) | ETA ~2min, 1.1s/it |

说明：脚本使用 lm-evaluation-harness 批量评估，ARC/WG/MMLU/GSM8K 结果在全部 task 跑完后统一写入 log 和 results JSON。当前都卡在 GSM8K generate_until（最慢的 task）。

## GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| westd-41718 cuda:0 | 96% | 59,285 MiB |
| westd-41718 cuda:1 | 94% | 61,665 MiB |
| westd-34887 cuda:0 | 78% | 93,989 MiB |
| westd-34887 cuda:1 | 64% | 66,997 MiB |

全部 GPU 繁忙，无空闲卡。`bce_isocompute_v3_s456_eval` 预计最快完成（~2分钟内）。

---
