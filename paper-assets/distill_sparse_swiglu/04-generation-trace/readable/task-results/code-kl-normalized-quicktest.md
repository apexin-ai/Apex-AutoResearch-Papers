# code kl normalized quicktest

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kl_normalized_quicktest_20260515T140431_result.json`
- **Structured JSON:** [`332b19053d5fdd32377e.json`](../../sessions/33/332b19053d5fdd32377e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING。汇总：

**代码修改**：
1. `train.py` 新增 `--loss_type kl_normalized` 选项
2. 新增 `train_kl_normalized()` 函数（~100 行），核心改动：
   - **KL 归一化**：`kl_norm = kl_raw / vocab_size`，将 KL 从 ~418 降到 ~0.003 量级
   - **激进 Lagrangian**：每步更新 lambda，×2.0 增长/×0.5 衰减，cap=1000，margin=0.02
   - **Soft constraint**：`clamp(|sparsity - target| - margin, 0)²` 替代 hard clamp，确保梯度不被截断
   - 日志打印 raw_kl、normalized_kl、lambda、constraint、sparsity
3. `main()` 路由增加 `kl_normalized` 分支，自动启用 gradient checkpointing

**训练状态**：
- PID=65772，正在 westd-34887 cuda:0 上运行
- 早期数据：kl_norm ~0.000009，sparsity ~0.40，lambda 在 10 步内就涨到 cap=1000
- lambda 涨得很快是因为 sparsity (0.40) 一直 < target-margin (0.48)，符合预期——接下来看 constraint 能否推动 sparsity 上升

---
