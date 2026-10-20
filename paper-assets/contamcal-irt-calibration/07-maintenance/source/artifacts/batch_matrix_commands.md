# D141 Model Matrix Batch Commands

Server: westd-29999 | GPUs 0-3
Total: 29 runs (bf16 LoRA, lr=5e-5, r=16, alpha=32, epochs=1)

## Model Matrix

| Model | Path | Runs | GPU | bs | ga | Seeds |
|-------|------|------|-----|----|----|-------|
| Qwen2.5-7B | Qwen2.5-7B | 9 (5d×s42+4d×s123) | cuda:0 | 2 | 8 | 42,123 |
| Qwen2.5-14B | Qwen2.5-14B | 5 (5d×1s) | cuda:2 | 1 | 16 | 42 |
| Phi-4 | phi-4 | 5 (5d×1s) | cuda:1 | 1 | 16 | 42 |
| OLMo-2-7B | OLMo-2-1124-7B | 5 (5d×1s) | cuda:1 (Batch 2) | 2 | 8 | 42 |
| Gemma-2-9B | gemma-2-9b | 5 (5d×1s) | cuda:3 | 1 | 16 | 42 |

## Pre-launch Checklist (per C001-C006)

```bash
# 1. Check all GPUs idle
nvidia-smi

# 2. Check no residual processes
ps aux | grep train_sft | grep -v grep
```

---

## Batch 1: cuda:0 (Qwen2.5-7B d000/d005 s42,s123), cuda:1 (Phi-4), cuda:2 (14B), cuda:3 (Gemma)

### cuda:0 — Qwen2.5-7B d000 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:0 — Qwen2.5-7B d005 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:0 — Qwen2.5-7B d000 s123

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s123 --seed 123 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:0 — Qwen2.5-7B d005 s123

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d005_s123 --seed 123 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:1 — Phi-4 d000 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:1 — Phi-4 d005 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:1 — Phi-4 d025 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:1 — Phi-4 d050 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d050_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:1 — Phi-4 d100 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d100_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:2 — Qwen2.5-14B d000 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=2 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:2 — Qwen2.5-14B d005 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=2 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:2 — Qwen2.5-14B d025 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=2 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:2 — Qwen2.5-14B d050 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=2 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:2 — Qwen2.5-14B d100 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=2 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:3 — Gemma-2-9B d000 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=3 python exp001/train_sft.py --model-name /root/autodl-tmp/models/gemma-2-9b --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:3 — Gemma-2-9B d005 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=3 python exp001/train_sft.py --model-name /root/autodl-tmp/models/gemma-2-9b --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:3 — Gemma-2-9B d025 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=3 python exp001/train_sft.py --model-name /root/autodl-tmp/models/gemma-2-9b --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:3 — Gemma-2-9B d050 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=3 python exp001/train_sft.py --model-name /root/autodl-tmp/models/gemma-2-9b --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d050_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

### cuda:3 — Gemma-2-9B d100 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=3 python exp001/train_sft.py --model-name /root/autodl-tmp/models/gemma-2-9b --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048"
```

---

## Batch 2: cuda:0 (Qwen7B d025/d050/d100 s42,s123), cuda:1 (OLMo-2)

### cuda:0 — Qwen2.5-7B d025 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:0 — Qwen2.5-7B d050 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d050_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:0 — Qwen2.5-7B d100 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d100_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:0 — Qwen2.5-7B d025 s123

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d025_s123 --seed 123 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:0 — Qwen2.5-7B d100 s123

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=0 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d100_s123 --seed 123 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:1 — OLMo-2-7B d000 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/OLMo-2-1124-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-1124-7B_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:1 — OLMo-2-7B d005 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/OLMo-2-1124-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-1124-7B_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:1 — OLMo-2-7B d025 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/OLMo-2-1124-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-1124-7B_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:1 — OLMo-2-7B d050 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/OLMo-2-1124-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d050_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

### cuda:1 — OLMo-2-7B d100 s42

```bash
bash -c "cd /root/contamcal-irt-calibration && source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/OLMo-2-1124-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-1124-7B_d100_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048"
```

---

## Summary Table

| # | Batch | GPU | Model | Dosage | Seed | bs | ga |
|---|-------|-----|-------|--------|------|----|----|
| 1 | 1 | 0 | Qwen2.5-7B | d000 | 42 | 2 | 8 |
| 2 | 1 | 0 | Qwen2.5-7B | d005 | 42 | 2 | 8 |
| 3 | 1 | 0 | Qwen2.5-7B | d000 | 123 | 2 | 8 |
| 4 | 1 | 0 | Qwen2.5-7B | d005 | 123 | 2 | 8 |
| 5 | 1 | 1 | Phi-4 | d000 | 42 | 1 | 16 |
| 6 | 1 | 1 | Phi-4 | d005 | 42 | 1 | 16 |
| 7 | 1 | 1 | Phi-4 | d025 | 42 | 1 | 16 |
| 8 | 1 | 1 | Phi-4 | d050 | 42 | 1 | 16 |
| 9 | 1 | 1 | Phi-4 | d100 | 42 | 1 | 16 |
| 10 | 1 | 2 | Qwen2.5-14B | d000 | 42 | 1 | 16 |
| 11 | 1 | 2 | Qwen2.5-14B | d005 | 42 | 1 | 16 |
| 12 | 1 | 2 | Qwen2.5-14B | d025 | 42 | 1 | 16 |
| 13 | 1 | 2 | Qwen2.5-14B | d050 | 42 | 1 | 16 |
| 14 | 1 | 2 | Qwen2.5-14B | d100 | 42 | 1 | 16 |
| 15 | 1 | 3 | Gemma-2-9B | d000 | 42 | 1 | 16 |
| 16 | 1 | 3 | Gemma-2-9B | d005 | 42 | 1 | 16 |
| 17 | 1 | 3 | Gemma-2-9B | d025 | 42 | 1 | 16 |
| 18 | 1 | 3 | Gemma-2-9B | d050 | 42 | 1 | 16 |
| 19 | 1 | 3 | Gemma-2-9B | d100 | 42 | 1 | 16 |
| 20 | 2 | 0 | Qwen2.5-7B | d025 | 42 | 2 | 8 |
| 21 | 2 | 0 | Qwen2.5-7B | d050 | 42 | 2 | 8 |
| 22 | 2 | 0 | Qwen2.5-7B | d100 | 42 | 2 | 8 |
| 23 | 2 | 0 | Qwen2.5-7B | d025 | 123 | 2 | 8 |
| 24 | 2 | 0 | Qwen2.5-7B | d100 | 123 | 2 | 8 |
| 25 | 2 | 1 | OLMo-2-7B | d000 | 42 | 2 | 8 |
| 26 | 2 | 1 | OLMo-2-7B | d005 | 42 | 2 | 8 |
| 27 | 2 | 1 | OLMo-2-7B | d025 | 42 | 2 | 8 |
| 28 | 2 | 1 | OLMo-2-7B | d050 | 42 | 2 | 8 |
| 29 | 2 | 1 | OLMo-2-7B | d100 | 42 | 2 | 8 |
