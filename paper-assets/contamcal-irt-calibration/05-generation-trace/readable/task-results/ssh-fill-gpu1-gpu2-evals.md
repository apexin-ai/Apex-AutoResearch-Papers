# ssh fill gpu1 gpu2 evals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fill-gpu1-gpu2-evals_20260513T222916_result.json`
- **Structured JSON:** [`50fbd178d05821c9a94c.json`](../../sessions/50/50fbd178d05821c9a94c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均启动成功，bitsandbytes 警告无影响（和之前 1.5B s42 eval 一样）。

---

## 汇报

### 训练结果

| 模型 | Seed | 最终 loss (step 3120) | 平均 train_loss | mean_token_acc | 训练时长 | Checkpoint 路径 |
|------|------|-----------------------|-----------------|----------------|----------|----------------|
| 0.5B | s123 | 1.4735 | 1.5393 | 0.6757 | 54.4 min | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter/` |
| 1.5B | s123 | 1.2235 | 1.2602 | 0.7310 | 101.5 min | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter/` |

两个训练均正常完成（EXIT_CODE=0），3125 steps / 1 epoch。

### Eval 提交状态

| Eval | GPU | PID | 状态 | 日志 |
|------|-----|-----|------|------|
| 0.5B s42 | GPU 1 (CUDA_VISIBLE_DEVICES=1) | 227160 | 运行中，正在加载模型 | `eval_05B_d000_s42.log` |
| 1.5B s123 | GPU 2 (CUDA_VISIBLE_DEVICES=2) | 227572 | 运行中，正在加载模型 | `eval_15B_d000_s123.log` |

Benchmarks: mmlu, gsm8k, arc_challenge（无 humaneval）。

### 当前 GPU 占用总览
- GPU 0: 1.5B s42 eval（已在跑）
- GPU 1: 0.5B s42 eval（刚启动）
- GPU 2: 1.5B s123 eval（刚启动）
- GPU 3: 3B s123 训练
- GPU 4-5: 3B s42 训练

0.5B s42 eval 跑完后 GPU 1 可接着跑 0.5B s123 eval。

---
