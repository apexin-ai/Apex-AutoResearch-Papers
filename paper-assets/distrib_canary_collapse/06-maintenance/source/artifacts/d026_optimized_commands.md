# D026 Multi-seed Optimized Commands

## Current vs Recommended Parameters

| Parameter | Current | Recommended | Rationale |
|-----------|---------|-------------|-----------|
| `batch_size` | 4 | **32** | 14.4GB / 96GB VRAM used (15%). bs=32 ~30-35GB, well within budget |
| `gen_batch_size` | 16 | **32** | Generation phase also underutilized; 2x speeds up synthetic data creation |
| `steps_per_gen` | 5000 | 5000 | Unchanged — keeps experiment comparable to existing α-sweep |
| `lr` | 5e-5 | 5e-5 | Unchanged — larger batch smooths gradients but 5e-5 is already conservative |

### Memory Budget (Pythia-410M fp16, seq_len=512, 96GB VRAM)

- Model weights + optimizer + gradients: ~6.5GB
- CUDA context + HF overhead: ~3-4GB
- Activations at bs=32: ~16-20GB (24 layers × attention scores + FFN intermediates)
- **Estimated peak at bs=32: ~30-35GB** (36% of 96GB)
- Generation KV cache at gen_bs=32: ~1.6GB additional
- Headroom: ~60GB — no OOM risk

### Parameters NOT available as CLI args

`dataloader_num_workers` and `pin_memory` are not exposed in `iterative_train.py` argparse. HF Trainer defaults: `num_workers=0`, `pin_memory=True`. Adding these would require code changes — not worth it since the bottleneck is GPU compute utilization, not data loading.

## Experiment Commands

All 4 experiments use the same format as existing α-sweep queue. Run at most **2 simultaneously** (one per GPU).

### D026-1: α=0.25, seed=43 (priority)

```bash
CUDA_VISIBLE_DEVICES=0 nohup python iterative_train.py \
  --seed 43 --synthetic_ratio 0.25 \
  --data_dir data/wikitext103_5k \
  --steps_per_gen 5000 --num_generations 10 \
  --batch_size 32 --gen_batch_size 32 \
  --output_dir results/alpha_sweep/a025_s43 \
  > /tmp/a025_s43.log 2>&1 &
```

### D026-2: α=0.50, seed=43

```bash
CUDA_VISIBLE_DEVICES=1 nohup python iterative_train.py \
  --seed 43 --synthetic_ratio 0.50 \
  --data_dir data/wikitext103_5k \
  --steps_per_gen 5000 --num_generations 10 \
  --batch_size 32 --gen_batch_size 32 \
  --output_dir results/alpha_sweep/a050_s43 \
  > /tmp/a050_s43.log 2>&1 &
```

### D026-3: α=0.25, seed=44

```bash
CUDA_VISIBLE_DEVICES=0 nohup python iterative_train.py \
  --seed 44 --synthetic_ratio 0.25 \
  --data_dir data/wikitext103_5k \
  --steps_per_gen 5000 --num_generations 10 \
  --batch_size 32 --gen_batch_size 32 \
  --output_dir results/alpha_sweep/a025_s44 \
  > /tmp/a025_s44.log 2>&1 &
```

### D026-4: α=0.50, seed=44

```bash
CUDA_VISIBLE_DEVICES=1 nohup python iterative_train.py \
  --seed 44 --synthetic_ratio 0.50 \
  --data_dir data/wikitext103_5k \
  --steps_per_gen 5000 --num_generations 10 \
  --batch_size 32 --gen_batch_size 32 \
  --output_dir results/alpha_sweep/a050_s44 \
  > /tmp/a050_s44.log 2>&1 &
```

## Submission Plan

1. Wait for current a000_s42 (GPU 0) and a025_s42 (GPU 1) to finish
2. Launch **D026-1** on GPU 0 + **D026-2** on GPU 1 simultaneously
3. When those finish, launch **D026-3** on GPU 0 + **D026-4** on GPU 1

## Training Time Estimate

| Phase | bs=4 (old) | bs=32 (new) |
|-------|-----------|-------------|
| Training per gen (5000 steps) | ~12 min | ~20-25 min |
| Generation per gen (gen_bs 16→32) | ~8 min | ~5 min |
| Metrics per gen | ~3 min | ~3 min |
| **Per generation total** | **~23 min** | **~28-33 min** |
| **10 generations total** | **~3.8 h** | **~4.7-5.5 h** |
| **GPU utilization** | **~37%** | **~75-85%** |

Per-step time increases ~2x at bs=32 (not 8x — GPU parallelism absorbs most of the increase). Each step processes 8x more data, so the effective throughput (samples/sec) roughly quadruples. Total wall time per experiment increases ~25-40%, but GPU utilization doubles and each training step sees 8x more data.

### Note on Comparability

Changing batch_size from 4 to 32 means each of the 5000 steps sees 32 instead of 4 samples. This changes effective data exposure per generation from 20K to 160K sample-steps. For model collapse dynamics, this should be noted in analysis — the model sees more data per generation, which may dampen collapse rate. If strict comparability with the seed=42 runs (bs=4) is required, consider either:
- Keeping bs=4 and accepting low utilization
- Reducing steps_per_gen to 625 (= 5000 × 4/32) to match total data exposure — but this changes the gradient update count

Recommendation: **use bs=32** and note it in the experimental log. The α-sweep comparison is across seeds within the same batch_size, not across different batch sizes.
