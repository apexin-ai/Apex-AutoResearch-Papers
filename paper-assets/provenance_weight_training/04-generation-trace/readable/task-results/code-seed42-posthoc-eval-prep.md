# code seed42 posthoc eval prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed42_posthoc_eval_prep_20260514T211436_result.json`
- **Structured JSON:** [`60f64a3e6c79d547be1c.json`](../../sessions/60/60f64a3e6c79d547be1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功。结果：

**b=0.5 seed42 dry-run (100 docs)**
- eval_loss = 3.0532
- eval_ppl = 21.18
- tokens = 77,302
- 耗时 = 5s

**脚本位置**: `/root/provenance_weight_training/run_posthoc_eval_seed42.sh`

**使用方法**:
```bash
# 默认 5000 docs
bash run_posthoc_eval_seed42.sh

# 自定义 doc 数
bash run_posthoc_eval_seed42.sh 10000
```

**预估全量 eval 耗时**:
- 100 docs → 5s/checkpoint
- 5000 docs → ~250s (~4min)/checkpoint
- 6 checkpoints × 4min = **~24 min 总计**
- 加载/卸载模型开销 → 实际约 **25-30 min**

**当前状态**:
- 5/6 checkpoint 已就绪（b=0.5/1.0/1.5/2.0/3.0）
- b=5.0 seed42 仍在训练（无 `final/` 目录）
- 脚本会自动跳过缺失的 checkpoint 并打印 WARNING

**输出路径**: `output/eval/posthoc_eval_seed42.json`

不需要写新的 `eval_checkpoint.py`——已有的 `eval_perplexity.py` 完全满足需求。

---
