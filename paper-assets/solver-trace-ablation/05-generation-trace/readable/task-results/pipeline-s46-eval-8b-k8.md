# pipeline s46 eval 8b k8

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_s46-eval-8b-k8_20260522T033553_result.json`
- **Structured JSON:** [`77b0dfd1ff3d3f8a4cdb.json`](../../sessions/77/77b0dfd1ff3d3f8a4cdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

准备工作全部完成。关键信息已记录：

- **eval**: `python scripts/eval_sta.py --model_path &lt;path> --data_path data/proofwriter_fol_100.jsonl --output_path &lt;path>`
- **classify**: `python scripts/classify_h7.py --eval_path &lt;path>`
- **8B dry-run 配置**: 需改 `num_generations: 4 → 8`
- **s45 已完成**: PR=15%, ISR=0.592(proved-only), genuine=86.7%, TS=6.7%, CE=6.7%

等待 s46 完成，轮询已设置。

---
