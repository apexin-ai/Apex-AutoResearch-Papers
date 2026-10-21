# ops urgent full status check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-full-status-check_20260518T163420_result.json`
- **Structured JSON:** [`f9295698e17b20821374.json`](../../sessions/f9/f9295698e17b20821374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

| 实验名 | 服务器 GPU | 状态 | 关键数字 |
|--------|-----------|------|---------|
| c1_ablation_eval_uniform | westd-41718 GPU0 | 运行中 | MMLU loglikelihood 73% (43269/58702), 预计还需~1.5min |
| kl_sparsity25_s123 | westd-41718 GPU1 | 运行中 | step 60/1000, kl=0.406, sparsity=0.391 |
| kl_sparsity25_s42 | westd-41718 (已释放) | **完成** | kl=0.1582, sparsity=0.230, lambda=5000, exit_code=0 |
| kl_sparsity35_s42 | westd-34887 GPU0 | 运行中 | step 560/1000, kl=0.194, sparsity=0.336 |
| kl_sparsity45_s42 | westd-34887 GPU1 | 运行中 | step 570/1000, kl=0.264, sparsity=0.457 |

kl_sparsity25_s42 registry 已更新为 DONE。其余 4 个实验全部存活正常运行中。

---
