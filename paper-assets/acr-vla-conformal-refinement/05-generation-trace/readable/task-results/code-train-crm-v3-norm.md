# code train crm v3 norm

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_train-crm-v3-norm_20260514T184613_result.json`
- **Structured JSON:** [`fe0f19a0939b66c5b054.json`](../../sessions/fe/fe0f19a0939b66c5b054.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 RUNNING。训练状态总结：

- **实验**: crm-train-v3-norm (RUNNING)
- **服务器**: bjb1-18228, GPU 1
- **数据**: crm_cache_v5/spatial, 12167 samples
- **模型**: CRM-MLP-337K-Normalized (337,438 params)
- **配置**: epochs=50, batch_size=512, lr=0.016, input_mode=full, seed=42
- **Normalization**: 已自动计算 norm stats (mean [-26.94, 5.54], std [0.004, 2.22])
- **Epoch 1**: train_loss=0.1166, val_loss=0.0726 (已保存 best)
- **tmux session**: `crm_v3_norm`
- **tee log 失败**（目录竞争），输出在 tmux pane 中可用

---
