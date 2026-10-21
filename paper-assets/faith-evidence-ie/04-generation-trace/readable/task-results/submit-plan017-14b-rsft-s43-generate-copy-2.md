# submit plan017 14b rsft s43 generate

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_plan017_14b_rsft_s43_generate_20260522T183558_result.json`
- **Structured JSON:** [`7640854852bb3ee2eebb.json`](../../sessions/76/7640854852bb3ee2eebb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已经在运行，无需重复提交。

**当前状态：**
- **exp_id**: `plan017_14b_rsft_s43_generate`
- **PID**: 194682，cuda:1
- **进度**: 62/3027 docs (~2%)，平均 ~14-20s/doc
- **预估总时长**: 按 ~17s/doc 计算，3027 docs ≈ 14.3 小时，已跑约 19 分钟
- **预计完成时间**: 约 5/23 16:30（UTC）

命令：
```
CUDA_VISIBLE_DEVICES=1 python -m freige.training.rsft_generate \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B \
    --sft_adapter /root/autodl-tmp/sft_output_14b_s43 \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/rsft_generations_14b_s43 \
    --num_generations 8 --max_new_tokens 1024 --seed 43
```

---
