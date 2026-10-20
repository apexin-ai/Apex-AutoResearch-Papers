# eval plan 008 rsft topk3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_008_rsft_topk3_20260515T211207_result.json`
- **Structured JSON:** [`714d8809d533347d69ee.json`](../../sessions/71/714d8809d533347d69ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:3 上已经在运行完全相同的评测命令（PID 255528）：

```
python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_topk3_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/rsft_topk3 --no-quantize
```

这个任务已经在跑了，无需重复提交。是否需要我检查它的运行进度或 registry 状态？

---
