# ssh prepare eval pipeline

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare_eval_pipeline_20260515T185134_result.json`
- **Structured JSON:** [`9eaebf2d927fcff089ab.json`](../../sessions/9e/9eaebf2d927fcff089ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇总如下：

---

## 实验进度

| 实验 | 当前 step | 总 step | 进度 | loss | 速度 | 预计剩余 |
|------|----------|---------|------|------|------|---------|
| ess_only_seed123 (cuda:0) | 1339/6103 | 6103 | 22% | 10.44 | 2.12s/step | ~2h48m |
| ess_only_seed456 (cuda:3) | 1340/6103 | 6103 | 22% | 9.97 | 2.12s/step | ~2h48m |
| nmin4_seed42 (cuda:1) | 2036/6103 | 6103 | 33% | 7.47 | 2.11s/step | ~2h23m |

**nmin4_seed42 符合预期**：`b=0.0`, `ess=4.0`(=n_min), `weighted_loss == unweighted_loss`，确认 b*=0 退化为 uniform weighting。

---

## Eval 脚本说明

脚本：`evaluation/eval_pipeline.py`

主要参数：
- `--model_path`：HF 模型目录（训练完成后在 `output/models/{exp_id}/final/`）
- `--output_dir`：结果保存目录
- `--eval_data_path`：本地 eval JSONL（`data/human/eval_holdout.jsonl`，67823 条）
- `--num_eval_tokens`：默认 5M tokens
- `--max_length`：默认 2048
- `--batch_size`：默认 4
- `--run_perplexity`：默认 true
- `--run_lm_eval`：是否跑 HellaSwag/MMLU（之前的 eval 未跑）
- `--run_generation`：是否跑 Self-BLEU/Distinct-n（之前的 eval 未跑）
- `--seed`：随机种子

之前已完成的 eval（grid_b1_0_seed456、grid_b1_5_seed456）只跑了 perplexity，结果为 ~17.70。

---

## 3 个 Eval 命令

**1. ess_only_seed123**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=0 python evaluation/eval_pipeline.py \
  --model_path output/models/ess_only_seed123/final \
  --output_dir output/eval/ess_only_seed123 \
  --eval_data_path data/human/eval_holdout.jsonl \
  --run_lm_eval false \
  --run_generation false \
  --seed 123
```

**2. ess_only_seed456**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=3 python evaluation/eval_pipeline.py \
  --model_path output/models/ess_only_seed456/final \
  --output_dir output/eval/ess_only_seed456 \
  --eval_data_path data/human/eval_holdout.jsonl \
  --run_lm_eval false \
  --run_generation false \
  --seed 456
```

**3. nmin4_seed42**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=1 python evaluation/eval_pipeline.py \
  --model_path output/models/nmin4_seed42/final \
  --output_dir output/eval/nmin4_seed42 \
  --eval_data_path data/human/eval_holdout.jsonl \
  --run_lm_eval false \
  --run_generation false \
  --seed 42
```

---

**注意**：训练完成后 `final/` 目录才会生成。nmin4_seed42 预计最先完成（~2h23m 后），两个 ess_only 约 2h48m 后完成。CUDA_VISIBLE_DEVICES 与训练 GPU 匹配，避免 OOM 冲突——如果训练完成后 GPU 已释放，也可以用其他空闲 GPU。

---
