# train plan015 mean pooling

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan015-mean-pooling_20260518T013615_result.json`
- **Structured JSON:** [`22db350082cf745b4b43.json`](../../sessions/22/22db350082cf745b4b43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果**：Mean Pooling 在所有 K 值（1,2,3,5,full）上 F1=1.0，与 GRU treatment 完全一致（delta=0.0）。

**结论**：BiGRU 时序建模对 treatment 条件下的分类性能没有贡献。Mean pooling（简单平均 turn embeddings）即可达到相同效果，说明方法的核心在于 per-turn DeBERTa 特征质量，而非序列建模。

产出：
- Checkpoint: `checkpoints/plan_015_meanpool/treatment/best.pt`
- 结果: `results/plan_015_mean_pooling_eval.json`
- 训练日志: `results/plan_015_nohup.log`

---
