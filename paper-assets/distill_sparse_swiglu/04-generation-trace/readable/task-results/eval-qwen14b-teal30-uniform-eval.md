# eval qwen14b teal30 uniform eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen14b_teal30_uniform_eval_20260517T230401_result.json`
- **Structured JSON:** [`5fdcc7512caab97f3f3f.json`](../../sessions/5f/5fdcc7512caab97f3f3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **任务已提交**: `qwen14b_teal30_uniform_eval` 在 westd-34887:cuda:1 上运行 (PID 80808)
- **命令**: `--baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.3`（无需 checkpoint，TEAL vanilla 是 training-free baseline）
- **与 KL uniform 的区别**: KL uniform 用 `--sparsity_mode teal_global --checkpoint ...` + `--allocation uniform`（用训练过的 KL predictor 预测重要性再 uniform 分配）；TEAL uniform 用 `--baseline_mode teal_vanilla --allocation uniform`（直接用激活幅度作为重要性指标再 uniform 分配）
- **日志**: `/root/runs/distill_sparse_swiglu/qwen14b_teal30_uniform_eval.log`
- **Registry**: 状态已更新为 RUNNING，spec 已填写完整
- **当前进度**: 模型已加载，uniform mask 已计算（model-level sparsity 0.293），WikiText-2 PPL 评估进行中

---
