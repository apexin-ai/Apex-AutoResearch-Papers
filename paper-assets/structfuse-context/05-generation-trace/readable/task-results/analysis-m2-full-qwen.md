# analysis m2 full qwen

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m2_full_qwen_20260514T112525_result.json`
- **Structured JSON:** [`8a78002c19b6c9786919.json`](../../sessions/8a/8a78002c19b6c9786919.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心发现：

**实验未完成 — 9 runs 中只有 random_s42 跑完了。**

### random_s42 结果
- Best R@1 = **0.5527** (step 1000, epoch 1 中期)，best val_loss 也在同一步
- 之后持续 overfit，val_loss 从 0.465 升到 0.560
- 比 pilot random (0.5357) 高 **+1.7pp**，full data 有帮助

### 未完成原因
- random_s43 在 19:24:14 启动，模型加载完成后无任何训练步输出（疑似 OOM/crash）
- 其余 7 个 run（embedding_distance × 3, dataflow_aware × 3, random_s44）均未启动
- **核心假设（embedding > random）无法验证**

### 需要行动
1. 诊断 random_s43 停止原因（查 dmesg / GPU 内存）
2. 修复后重启剩余 8 runs
3. 3 epochs 过多，建议保持 2 epochs + early_stopping_patience=2

---
