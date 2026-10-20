# analysis prepare ess only eval command

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prepare_ess_only_eval_command_20260516T025302_result.json`
- **Structured JSON:** [`68b0ad15cf7ea1fe3515.json`](../../sessions/68/68b0ad15cf7ea1fe3515.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

参数确认完毕。以下是训练完成后可直接执行的 eval 命令：

---

**Eval on holdout (ρ=0.4)**:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/provenance_weight_training

CUDA_VISIBLE_DEVICES=2 python eval_perplexity.py \
    --checkpoints output/models/contamination_60_ess_only_seed42/final \
    --data_path data/human/eval_holdout.jsonl \
    --output_path output/eval_results/contamination_60_ess_only_seed42_eval.json
```

**Eval on full ρ=0.6 data**:
```bash
CUDA_VISIBLE_DEVICES=2 python eval_perplexity.py \
    --checkpoints output/models/contamination_60_ess_only_seed42/final \
    --data_path data/scored_data_60.jsonl \
    --output_path output/eval_results/contamination_60_ess_only_seed42_trainset_eval.json
```

---

注意：当前 checkpoint 目录里还没有 `final/`，需等训练完成后生成。如果训练只保存 numbered checkpoint 不生成 `final/`，改用最后一个 checkpoint 路径（如 `checkpoint-6000`）。

对比基准：
- adaptive PPL = 17.74
- grid b=0.5 PPL = 17.704
- ρ=0.4 ess_only PPL = 17.728（已有结果）

---
