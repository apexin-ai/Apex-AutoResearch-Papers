# registry sync grid b seed42 batch

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_registry-sync_grid_b_seed42_batch_20260514T202935_result.json`
- **Structured JSON:** [`d5d3c37fb3a29ab99a0f.json`](../../sessions/d5/d5d3c37fb3a29ab99a0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 做了 merge 而非 replace，旧字段仍在但不影响。新指标已添加。

eval_ppl 检查——日志中没有 eval 相关内容（batch 脚本未配置 inline eval），确认需要 post-hoc eval。

结果汇总：

1. **b=2.0 train_loss = 10.6206**（Trainer summary average, train_runtime=13034s）
2. **b=3.0 train_loss = 10.7537**（Trainer summary average, train_runtime=13036s）
3. **eval_ppl 不可用** — batch 脚本未配置 `--eval_data_path`/`--eval_steps`，需要对 b=2.0 和 b=3.0 的 checkpoints 补跑 post-hoc eval
4. **Checkpoint 路径**：
   - b=2.0: `/root/provenance_weight_training/output/models/grid_b2_0_seed42/final/`（model.safetensors 1.19GB）
   - b=3.0: `/root/provenance_weight_training/output/models/grid_b3_0_seed42/final/`（model.safetensors 1.19GB）

备注：registry 中 b0_5_train_loss=2.531 与 Trainer summary（9.598）不一致，可能是用 step_metrics 最后一步的 loss 而非 epoch 平均值。b=2.0/3.0 的值按 Trainer summary 记录，与 seed123 系列实验一致。

---
