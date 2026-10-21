# ops p0 c1 eval urgent v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-c1-eval-urgent-v2_20260518T161626_result.json`
- **Structured JSON:** [`9abd81f1299cf5566cdf.json`](../../sessions/9a/9abd81f1299cf5566cdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 产出

1. **KL predictor hard mask**: PPL = **9.21**, actual sparsity = **0.6064 (60.6%)**
2. **C1 eval 已提交**: PID = **85155** (westd-41718 cuda:0, 日志 `logs/c1_ablation_eval_uniform.log`)
3. **BCE 30% 结果**: 成功。1000 steps, final loss = 0.607, bce = 0.581, sparsity = 0.042。注意实际 sparsity 仅 4.2%（远低于 30% target），Lagrangian 约束未充分推高稀疏度。Registry 已更新为 DONE。

---
