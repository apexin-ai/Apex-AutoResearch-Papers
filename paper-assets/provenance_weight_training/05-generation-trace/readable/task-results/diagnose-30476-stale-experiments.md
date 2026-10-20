# diagnose 30476 stale experiments

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_30476-stale-experiments_20260518T171344_result.json`
- **Structured JSON:** [`23a6b44b2c4801a93648.json`](../../sessions/23/23a6b44b2c4801a93648.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都完成了。汇总：

---

```
实验: grid_b0_1_seed42
Final checkpoint: 无（被 SIGTERM kill，EXIT_CODE=143）
训练进度: step 1999/8477（~24%），最后 checkpoint: checkpoint-1500
Train loss: 无最终值（训练未完成）
Eval PPL: 未执行（无 final）

实验: rho02_adaptive_tau08_seed42
Final checkpoint: 有 (/root/autodl-tmp/output/models/rho02_adaptive_tau08_seed42/final)
Train loss: 11.6800（注：weighted loss，epoch=0.47，6103 steps）
Eval loss: 2.8555
Eval PPL: 17.38

实验: batchsize16_nmin8_r2
Final checkpoint: 有 (/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_r2/final)
Train loss: 2.6308（epoch=0.26，6103 steps）
Eval loss: 2.8709
Eval PPL: 17.65

实验: detect_remove_q01_seed42（q01）
状态: 正在训练（GPU 3, PID 47640, 100% utilization）
进度: step ~4172/6103（~68%）
最新 checkpoint: checkpoint-4000
预计剩余: ~1900 steps
```

**关键发现：**
- `grid_b0_1_seed42` 被外部 kill 了（SIGTERM），只跑了 24%，需要重新启动或放弃
- `rho02` 的 train_loss（11.68）异常高，但 eval PPL（17.38）与 `batchsize16`（17.65）接近，说明 train_loss 高是因为 adaptive weighting 对高 contamination 样本施加了大权重放大了 loss 值
- q01 大约还需 ~45 分钟完成

---
