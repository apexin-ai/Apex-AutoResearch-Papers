# submit bce isocompute v3 retry

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_bce_isocompute_v3_retry_20260516T043330_result.json`
- **Structured JSON:** [`592e769005389315dc27.json`](../../sessions/59/592e769005389315dc27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:1 上有残留进程，无法启动 v3 训练。**

PID 204280 是 `bench_kl70_s42` 评估任务：
```
python -u src/benchmark_eval.py --exp_id bench_kl70_s42 --checkpoint checkpoints/kl_sparsity70_s42/predictor_kl_normalized.pt --sparsity_mode per_token --sparsity_target 0.7 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --gpu 0
```

它通过 `CUDA_VISIBLE_DEVICES=1` 映射到 cuda:1，占用 37008 MiB。

需要你决定：是否 kill PID 204280 以释放 cuda:1？还是等它跑完？

---
