# Wave 2 Eval Commands & Training Commands

Generated: 2026-05-18

## 磁盘状态

- **westd-41312 /root**: 30G total, 21G available (32% used)

---

## Priority 1: 41312 Eval (GPT-2 experiments)

### gpt2_adaptive_seed42
Checkpoints: checkpoint-3000, checkpoint-3500, checkpoint-4000
```bash
cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed42/checkpoint-3000 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048

cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed42/checkpoint-3500 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048

cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/gpt2_adaptive_seed42/checkpoint-4000 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048
```

### gpt2_uniform_seed42
Checkpoints: checkpoint-3500, checkpoint-4000, checkpoint-4500
```bash
cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/gpt2_uniform_seed42/checkpoint-3500 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048

cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/gpt2_uniform_seed42/checkpoint-4000 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048

cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/gpt2_uniform_seed42/checkpoint-4500 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048
```

---

## Priority 2: 41312 Eval (N-gram experiments)

### ngram_adaptive_seed42
```bash
cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/ngram_adaptive_seed42/final \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048
```

### ngram_uniform_seed42
```bash
cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/ngram_uniform_seed42/final \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048
```

---

## Priority 3: 41312 Eval (detect_remove_q08)

### detect_remove_q08_seed42
Checkpoints: checkpoint-3000, checkpoint-3500, checkpoint-4000
```bash
cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q08_seed42/checkpoint-3000 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048

cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q08_seed42/checkpoint-3500 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048

cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q08_seed42/checkpoint-4000 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048
```

---

## Priority 4: 30476 Eval (detect_remove_q02)

### detect_remove_q02_seed42 (on westd-30476)
Checkpoints: checkpoint-3000, checkpoint-3500, checkpoint-4000
```bash
cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/output/models/detect_remove_q02_seed42/checkpoint-3000 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048

cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/output/models/detect_remove_q02_seed42/checkpoint-3500 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048

cd /root/provenance_weight_training && python eval_perplexity.py \
  --checkpoints /root/autodl-tmp/output/models/detect_remove_q02_seed42/checkpoint-4000 \
  --data_path data/human/eval_holdout.jsonl --max_docs 5000 --max_length 2048
```

---

## Training: uniform_1_7b_seed123 (on westd-41312)

GPT-2 完成后在释放的 GPU 上启动。用 `nvidia-smi` 确认空闲 GPU 编号后设置 `CUDA_VISIBLE_DEVICES`。

```bash
cd /root/provenance_weight_training && CUDA_VISIBLE_DEVICES=0 WANDB_MODE=disabled python training/pretrain_weighted.py \
  --model_name models/Qwen/Qwen3-1.7B \
  --data_path data/scored_data.jsonl \
  --output_dir /root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed123 \
  --weighting_method uniform \
  --batch_size 4 --gradient_accumulation_steps 4 \
  --num_train_tokens 200000000 \
  --seed 123 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3
```

> 如果 cuda:0 被占用，改为 `CUDA_VISIBLE_DEVICES=1`。
