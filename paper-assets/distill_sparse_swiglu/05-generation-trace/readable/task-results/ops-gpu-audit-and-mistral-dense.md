# ops gpu audit and mistral dense

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_audit_and_mistral_dense_20260516T000157_result.json`
- **Structured JSON:** [`2e170322fb1bab6e9966.json`](../../sessions/2e/2e170322fb1bab6e9966.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Mistral dense 已启动并在加载模型。

## 汇总

### 1. GPU 状态

| GPU | PID | 任务 | 显存 | 状态 |
|-----|-----|------|------|------|
| cuda:0 | 181121 | **mistral_dense lm_eval** (新提交) | 14378 MiB (加载中) | 启动中 |
| cuda:1 | 174850 | mistral_kl_s42 lm_eval | 21280 MiB | GSM8K generate 13%, ~68min 剩余 |
| cuda:1 | 179918 | sparse lm_eval (kl_s42 predictor) | 16364 MiB | 运行中 |

### 2. 清理操作
- **PID 177270**: 不存在，无需处理
- GPU 1 上的两个进程是**不同任务**，非重复，均保留
- PID 174840 链式命令的第二步（mistral_dense on GPU 1）后续会变成冗余——因为 GPU 0 上的 mistral_dense 会先完成。建议链式任务完成 kl_s42 后手动 kill 避免重复跑 dense

### 3. Mistral dense 提交
- **已提交**: `lm_eval_mistral_dense` on cuda:0, PID 181121
- tmux session: `lm_eval_mistral_dense`
- log: `~/runs/distill_sparse_swiglu/lm_eval_mistral_dense.log`
- plan_id: plan_009

---
