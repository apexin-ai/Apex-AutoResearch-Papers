# exp d046 kl ablations

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_d046_kl_ablations_20260517T060059_result.json`
- **Structured JSON:** [`a3e023d9d343741d5652.json`](../../sessions/a3/a3e023d9d343741d5652.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡满载运行，训练状态正常。

**总结：**

| 项目 | Reverse KL (cuda:0) | JSD (cuda:1) |
|------|---------------------|--------------|
| PID | 2525 | 2867 |
| 显存 | 71.4 GB / 97.9 GB | 73.4 GB / 97.9 GB |
| GPU利用率 | 100% | 100% |
| 初始 loss | ~1.48 | ~0.19 |
| Lagrangian | 正常更新，推动 sparsity 从 0.406 → 0.5 | 正常更新 |

**代码修改摘要：**
- `src/losses.py`：新增 `ReverseKLDistillLoss`（KL(p_sparse||p_dense)）和 `JSDDistillLoss`（0.5*KL(p_dense||m) + 0.5*KL(p_sparse||m)）
- `src/train.py`：argparse 添加 `reverse_kl`/`jsd` choices，`train_kl_normalized` 接受可选 `loss_fn` 参数，main dispatch 路由新 loss type

超参与 baseline `mvp_kl_norm_v2_s42` 完全一致（batch_size=4, seq_len=2048, lr=1e-3, seed=42, tau 1.0→0.1, warmup 100, 1000 steps, wikitext-103）。预计每个实验约 40-60 分钟完成。

---
