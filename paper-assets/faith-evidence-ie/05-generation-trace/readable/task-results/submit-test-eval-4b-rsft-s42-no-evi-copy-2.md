# submit test eval 4b rsft s42 no evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_test_eval_4b_rsft_s42_no_evi_20260522T185509_result.json`
- **Structured JSON:** [`9594c9c6831e2aea53c7.json`](../../sessions/95/9594c9c6831e2aea53c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 上已经在运行**完全相同的实验** (PID 194600, 已运行 ~39 分钟)：

```
python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/rsft_output_ced_s42_v2 \
  --base_model /root/autodl-tmp/models/Qwen3-4B \
  --sft_adapter /root/autodl-tmp/sft_output \
  --split test_revised --no_evidence --no-quantize \
  --output_dir /root/autodl-tmp/eval_results/test_eval_4b_rsft_s42_no_evi \
  --batch_size 1 --seed 42
```

唯一差异：正在运行的用 `--max_new_tokens 2048`，Director 指定的是 `1024`。

**不提交。** 原因：
1. C001 违反 — GPU 0 显存占用 9584 MiB >> 2GB
2. 同 exp_id、同 output_dir 的任务已在运行，重复提交会冲突

需要 Director 决定：等当前任务完成（max_new_tokens=2048 版本），还是 kill 后用 1024 重跑？

---
