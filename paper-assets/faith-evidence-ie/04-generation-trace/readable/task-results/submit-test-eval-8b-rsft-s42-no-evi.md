# submit test eval 8b rsft s42 no evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_test_eval_8b_rsft_s42_no_evi_20260522T115950_result.json`
- **Structured JSON:** [`00f40eb008f23dc8c4f8.json`](../../sessions/00/00f40eb008f23dc8c4f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并运行中。

- **RSFT adapter**: `/root/autodl-tmp/rsft_output_qwen3_8b_k1`
- **GPU**: cuda:3，当前占用 ~16GB（模型加载中）
- **tmux session**: `test_eval_8b_rsft_s42_no_evi`
- **日志**: `~/runs/faith-evidence-ie/test_eval_8b_rsft_s42_no_evi.log`
- **输出目录**: `/root/autodl-tmp/eval_results/test_eval_8b_rsft_s42_no_evi`

注意：第一次提交因缺少 `--no-quantize` 参数失败（`quantize` 默认 `True`），已补上重新提交。with-evi eval 的 batch_size=16，这里用了 batch_size=1（按任务要求），预计耗时会更长。参考 with-evi eval 用时 ~45min（batch_size=16），batch_size=1 可能需要数小时。

---
