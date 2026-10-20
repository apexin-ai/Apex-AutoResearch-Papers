# ops check running progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_running_progress_20260515T195558_result.json`
- **Structured JSON:** [`a9796f628b2bcecaa30b.json`](../../sessions/a9/a9796f628b2bcecaa30b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU 状态
| GPU | 显存占用 | 利用率 | 占用进程 |
|-----|---------|--------|---------|
| 0 | 16287/32607 MiB | 1% | PID 236779 (plan_001) |
| 1 | 29260/32607 MiB | 93% | PID 246982 + 247244 (plan_011 eval) |
| 2 | 28825/32607 MiB | 99% | PID 245108 (plan_012 DPO) |
| 3 | 20093/32607 MiB | 40% | PID 234494 (plan_008) |

### 各实验进度

| 实验 | 状态 | 进度 | Loss | ETA |
|------|------|------|------|-----|
| **plan_001_flat_nli_seed43** | 运行中 (1h32m) | 503/507 (99.2%) | 0.625 (ep2.96) | **~20s，即将完成** |
| **plan_008_rsft_topk3** | 运行中 (1h53m) | 1006/1509 (66.7%) | 0.502 (ep1.99) | **~36 min** |
| **plan_011_bf16_g8_step_eval** | 运行中 (刚启动) | 1/62 batch (2%) | — (eval推理) | **~1h50m** |
| **plan_012_dpo_ced_1ep** | 运行中 (13m) | 64/167 (38%) | 0.668 (ep0.36) | **~21 min** |
| **plan_009_extract_reward_eval** | **OOM 失败** | — | — | CUDA out of memory on GPU 0 |

### 备注
- **plan_001** 马上完成，loss 在 0.60-0.63 波动，epoch 接近 3.0
- **plan_008** 刚过 epoch 2，loss 从 0.55 降到 0.50，训练正常
- **plan_012** DPO loss 从 0.693 稳步降至 0.668，rewards/accuracies 从 0.41 升到 0.68，训练趋势良好
- **plan_011** 加载了 `grpo_ced_g8_bf16/checkpoint-30` 的 LoRA，正在跑 dev set eval，111s/batch
- **plan_009** 因 GPU 0 显存被 plan_001 和 plan_011 eval 子进程占满导致 OOM 崩溃，需要等 plan_001 完成后重跑

---
