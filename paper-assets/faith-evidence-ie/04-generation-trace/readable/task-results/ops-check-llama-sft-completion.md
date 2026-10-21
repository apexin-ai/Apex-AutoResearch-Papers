# ops check llama sft completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_llama_sft_completion_20260516T113955_result.json`
- **Structured JSON:** [`947158d1b9abe649e75f.json`](../../sessions/94/947158d1b9abe649e75f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

**训练状态：成功完成。**

- `max_steps: 570`，最终 step 570，epoch 3.0，`should_training_stop: true` — 训练正常跑完全部 3 个 epoch。
- 最终 checkpoint 保存在 `/root/autodl-tmp/sft_output_llama_3_1_8b/checkpoint-570/`，顶层也有完整的 adapter 输出。

**最终指标：**

| 指标 | Train (step 570) | Eval |
|------|-----------------|------|
| loss | 0.409 | 0.736 |
| mean_token_accuracy | 89.2% | 83.6% |
| entropy | 0.468 | 0.549 |

**LoRA 配置：** r=64, alpha=128, dropout=0.05, 目标模块: q/k/v/o/gate/up/down_proj

**Checkpoints：** checkpoint-190, checkpoint-570 + 顶层最终 adapter（adapter_model.safetensors, 671MB）

**GPU 状态：**

| GPU | 显存占用 | 状态 |
|-----|---------|------|
| cuda:0 | 0 MiB | 空闲 ✓ |
| cuda:1 | 11,415 MiB | 占用 |
| cuda:2 | 18,421 MiB | 占用 |
| cuda:3 | 23,737 MiB | 占用 |

cuda:0 已完全释放，可用于下一个任务。

---
