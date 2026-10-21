# fix grid b2 0 seed123 eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_grid_b2_0_seed123_eval_20260514T142411_result.json`
- **Structured JSON:** [`4df742acef1f52d1a5c1.json`](../../sessions/4d/4df742acef1f52d1a5c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### 问题根因

Eval 没有在训练结束后立即执行，是因为训练脚本 (`run_grid_b_seed123.sh`) 本身**不包含 eval 逻辑**——它只做训练。Eval 由独立的后台进程 `auto_eval_watcher.py` 负责，每 60 秒扫描一次 `output/models/grid_b*/final/` 目录，发现有 `model.safetensors` 但没有对应 `{exp_id}_eval.json` 时自动触发 eval。

从 watcher 日志看，`grid_b2_0_seed123` 训练在 22:13 完成，watcher 在同一时刻检测到并在 22:15 完成了 eval。之前 metrics 标注 `should_evaluate=false` 大概率是因为查询时 eval 还没跑完。

### Eval 已完成

**不需要补跑。** `auto_eval_watcher` 已于 `2026-05-14 22:15:45` 完成 eval：

| 实验 | Loss | PPL | Tokens |
|------|------|-----|--------|
| grid_b0_5_seed123 | 2.8701 | 17.64 | 4,077,068 |
| grid_b1_0_seed123 | (需查) | (需查) | - |
| grid_b1_5_seed123 | (需查) | (需查) | - |
| **grid_b2_0_seed123** | **2.8750** | **17.73** | **4,077,068** |

### Checkpoint 完整性

已确认完整：`model.safetensors` (1.1GB) + config.json + tokenizer 文件齐全。

### 如果需要手动重跑 eval

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/provenance_weight_training
CUDA_VISIBLE_DEVICES=<空闲GPU> python eval_perplexity.py \
    --checkpoints output/models/grid_b2_0_seed123/final \
    --data_path data/human/eval_holdout.jsonl \
    --output_path output/eval_results/grid_b2_0_seed123_eval.json
```

但目前已有结果，**PPL=17.73**，可直接用于 seed123 的 b-value 对比。

---
