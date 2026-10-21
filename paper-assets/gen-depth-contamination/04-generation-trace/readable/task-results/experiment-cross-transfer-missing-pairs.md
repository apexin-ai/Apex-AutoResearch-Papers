# experiment cross transfer missing pairs

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_cross-transfer-missing-pairs_20260520T005455_result.json`
- **Structured JSON:** [`3d05a9d862009c157cc3.json`](../../sessions/3d/3d05a9d862009c157cc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均已启动并运行中。

| 实验 | exp_id | PID | GPU | 命令 |
|------|--------|-----|-----|------|
| qwen7b→llama8b | `exp_cross_transfer_qwen7b_to_llama8b` | 270054 | cuda:0 | `python scripts/run_deberta_cross_transfer.py --train_model wiki_qwen7b --test_model wiki_llama8b --gpu 0` |
| llama8b→qwen7b | `exp_cross_transfer_llama8b_to_qwen7b` | 270133 | cuda:1 | `python scripts/run_deberta_cross_transfer.py --train_model wiki_llama8b --test_model wiki_qwen7b --gpu 1` |

日志文件：
- `~/runs/gen-depth-contamination/exp_cross_transfer_qwen7b_to_llama8b.log`
- `~/runs/gen-depth-contamination/exp_cross_transfer_llama8b_to_qwen7b.log`

预计约 25 分钟完成，结果会写入 `results/deberta_cross_transfer/wiki_qwen7b__to__wiki_llama8b.json` 和 `wiki_llama8b__to__wiki_qwen7b.json`。

---
