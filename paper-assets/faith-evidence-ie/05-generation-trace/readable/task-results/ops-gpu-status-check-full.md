# ops gpu status check full

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check-full_20260515T215429_result.json`
- **Structured JSON:** [`f12664ff8994da05be7c.json`](../../sessions/f1/f12664ff8994da05be7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总览

| GPU | 显存占用 | 利用率 | PID | 实验 |
|-----|---------|--------|-----|------|
| **0** | 14,597 / 32,607 MiB (45%) | 33% | 258508 | plan_001_flat_nli_seed44 (训练) |
| **1** | 18,817 / 32,607 MiB (58%) | 87% | 254077 | plan_011_bf16_g8_step_eval (推理) |
| **2** | 15,167 / 32,607 MiB (47%) | 34% | 257192 | plan_001_flat_nli_seed45 (训练) |
| **3** | **0 / 32,607 MiB** | 0% | — | **空闲** |

## 各实验状态

### plan_011_bf16_g8_step_eval (GPU 1)
- 对 `grpo_ced_g8_bf16/checkpoint-50` 跑 eval inference
- 进度：**60/62 batches (97%)**，预计 ~2 分钟内完成

### plan_001_flat_nli_seed45 (GPU 2)
- RSFT 训练，seed=45
- 进度：**169/507 steps (33%)**，epoch ≈ 0.95
- 最近 loss=0.6376，token_accuracy=0.845
- 刚触发 step eval（inference 已启动），eval 完成后继续训练
- 预计剩余训练时间 ~30 min

### plan_001_flat_nli_seed44 (GPU 0)
- RSFT 训练，seed=44
- 进度：**169/507 steps (33%)**，epoch ≈ 0.95
- 最近 loss=0.6444，token_accuracy=0.839
- 同样刚触发 step eval
- 预计剩余训练时间 ~30 min

### eval_plan_008_rsft_topk3
- **无残留**，tmux session 不存在

### 其他
- `mvp2_eval_rsft_s43_r2` 有一个僵尸 tmux session（PID 194836），但无活跃 python 进程，可清理

---
