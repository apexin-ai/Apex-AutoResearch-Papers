# ops check plan 008

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_plan_008_20260515T190634_result.json`
- **Structured JSON:** [`202ef2467e7f70b0f736.json`](../../sessions/20/202ef2467e7f70b0f736.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### plan_008_rsft_topk3 进程状态：**正在运行**

- **PID**: 234494，启动于 2026-05-16 02:03:03 (CST)
- **GPU**: GPU 3，占用 15512 MiB，利用率 38%
- **命令**: `python -m freige.training.rsft_trainer --rsft_data_path rsft_filtered_topk3/rsft_train.jsonl --output_dir rsft_topk3_output --wandb_run_name plan_008_rsft_topk3`
- **训练进度**: step 500 / 1509 (33%)，3 epochs，loss=0.6289，token_accuracy=0.846
- **最新 checkpoint**: checkpoint-500（02:49 写入），每 50 step 保存一次

### 全部 4 块 GPU 占用情况

| GPU | 显存占用 | 利用率 | PID | 任务 |
|-----|---------|--------|-----|------|
| 0 | 16281 MiB | 76% | 236779 | plan_001_flat_nli_seed43 (rsft training) |
| 1 | 17143 MiB | 90% | 237917 | sft_baseline_noquant (eval inference) |
| 2 | 13255 MiB | 72% | 232312 | plan_012_dpo_ced (eval inference) |
| 3 | 15521 MiB | 38% | 234494 | **plan_008_rsft_topk3** (rsft training) |

### 结论

plan_008_rsft_topk3 确实在跑，进度约 1/3。按当前速度（~50 step 每 4-5 分钟），剩余 ~1009 step 预计还需 **约 1.5-2 小时**完成。4 块 GPU 全部被占用，无空闲 GPU。

---
