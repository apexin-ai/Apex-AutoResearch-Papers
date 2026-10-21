# analysis uniform epoch matched indep lr seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_uniform_epoch_matched_indep_lr_seed42_20260521T134509_result.json`
- **Structured JSON:** [`e0a5e6ab1cdec98d1e6d.json`](../../sessions/e0/e0a5e6ab1cdec98d1e6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果如下：

```
lr_scheduler:        linear  ✓ (日志配置确认，非 cosine)
total_steps:         2533
train_loss_final:    8.058   (Trainer 报告值，含 batch_size=4 累加；per-sample ≈ 2.01)
holdout_loss:        2.89381
holdout_ppl:         18.06206
ood_owt_loss:        ⚠️ 未评估
ood_owt_ppl:         ⚠️ 未评估
ood_wiki_loss:       ⚠️ 未评估
ood_wiki_ppl:        ⚠️ 未评估
checkpoint_path:     /root/autodl-tmp/provenance_weight_training/output/models/uniform_epoch_matched_indep_lr_seed42/final
completed_normally:  yes (EXIT_CODE=0, "Training complete" 确认)
```

**Checkpoint 内容**：final/ 含 model.safetensors (1.1GB)、config.json、tokenizer 等完整文件。另有 checkpoint-2000、checkpoint-2500、checkpoint-2533 三个中间 checkpoint。

### 与配对实验 delta

| 指标 | uniform | dr | delta | 方向 |
|------|---------|-----|-------|------|
| holdout_loss | 2.89381 | 2.93288 | **-0.03907** | uniform 更优 |
| holdout_ppl | 18.06206 | 18.78174 | **-0.71968** | uniform 更优 |
| ood_owt_ppl | N/A | 19.23533 | — | |
| ood_wiki_ppl | N/A | 15.95958 | — | |

**注意**：OOD eval (owt, wiki) 未执行，只有 holdout eval 结果。需要单独跑 OOD eval 才能完成完整对比。

---
