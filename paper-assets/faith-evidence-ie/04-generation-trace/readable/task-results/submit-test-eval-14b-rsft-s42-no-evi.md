# submit test eval 14b rsft s42 no evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_test_eval_14b_rsft_s42_no_evi_20260522T115936_result.json`
- **Structured JSON:** [`2a8fa26b577fdad83c77.json`](../../sessions/2a/2a8fa26b577fdad83c77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并注册。汇报：

- **RSFT adapter**: `/root/autodl-tmp/rsft_output_14b`
- **GPU**: cuda:0，bf16 加载占用 ~28.7GB / 96GB
- **tmux session**: `test_eval_14b_rsft_s42_no_evi`
- **日志**: `~/runs/faith-evidence-ie/test_eval_14b_rsft_s42_no_evi.log`
- **输出**: `/root/autodl-tmp/eval_results/test_eval_14b_rsft_s42_no_evi/`
- **修复**: 原始命令缺少 `--no-quantize`，默认 quantize=True 触发缺失 bitsandbytes 报错，已加上

模型权重加载中，预计推理约 5 小时（参考 with-evi 的 19086s）。

---
