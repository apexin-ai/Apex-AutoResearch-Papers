# TaxEI-RP Training Analysis (3 seeds)

**Date**: 2026-05-16
**Model**: Qwen3-8B (ms-swift SFT, LoRA rank=16)
**Data**: sft_taxei_rp.jsonl (14437 samples)
**Config**: 3 epochs, bs=4, ga=2, lr=1e-4, max_length=4096, bf16, gradient_checkpointing

## Summary Table

| exp_id | seed | final_train_loss | final_eval_loss | duration | checkpoint_path | wandb_run_id | status |
|--------|------|-----------------|-----------------|----------|-----------------|--------------|--------|
| v4-taxei-rp-s42 | 42 | 0.3847 | N/A (no eval split) | 3h 46m 40s (226.7 min) | `.../v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415` | N/A (not configured) | SUCCESS |
| v4-taxei-rp-s123 | 123 | 0.3852 | N/A (no eval split) | 3h 46m 30s (226.5 min) | `.../v4-taxei-rp-s123/v0-20260516-101708/checkpoint-5415` | N/A (not configured) | SUCCESS |
| v4-taxei-rp-s1 | 1 | 0.3853 | N/A (no eval split) | 3h 46m 18s (226.3 min) | `.../v4-taxei-rp-s1/v0-20260516-101834/checkpoint-5415` | N/A (not configured) | SUCCESS |

**Cross-seed consistency**: train_loss std = 0.0003, highly stable across seeds.

### Additional Metrics (final summary)

| exp_id | train_samples/s | train_steps/s | final_token_acc | peak_memory_GiB |
|--------|----------------|---------------|-----------------|-----------------|
| v4-taxei-rp-s42 | 3.185 | 0.398 | 0.9249 | 30.68 |
| v4-taxei-rp-s123 | 3.187 | 0.398 | 0.9137 | 30.66 |
| v4-taxei-rp-s1 | 3.190 | 0.399 | 0.9176 | 30.17 |

## Per-Experiment Details

### v4-taxei-rp-s42 (seed=42, cuda:0)

**Timing**: Started 2026-05-16 10:17:03, ended 14:04:07
**Checkpoints** (save_strategy=epoch):
- `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-1805` (epoch 1)
- `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-3610` (epoch 2)
- `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s42/v0-20260516-101703/checkpoint-5415` (epoch 3, final)

**Log tail (last steps)**:
```
step 5400: loss=0.2575, token_acc=0.9108, lr=0.0
step 5410: loss=0.2257, token_acc=0.9183, lr=0.0
Final: train_loss=0.38469276, token_acc=0.92487562, runtime=13600.1s
EXIT_CODE=0
```

**Warnings**: bitsandbytes libnvJitLink.so.13 load warning (non-critical, bnb not used in this run)
**Errors**: None

---

### v4-taxei-rp-s123 (seed=123, cuda:2)

**Timing**: Started 2026-05-16 10:17:08, ended 14:04:02
**Checkpoints** (save_strategy=epoch):
- `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s123/v0-20260516-101708/checkpoint-1805` (epoch 1)
- `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s123/v0-20260516-101708/checkpoint-3610` (epoch 2)
- `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s123/v0-20260516-101708/checkpoint-5415` (epoch 3, final)

**Log tail (last steps)**:
```
step 5400: loss=0.2683, token_acc=0.9022, lr=0.0
step 5410: loss=0.2208, token_acc=0.9193, lr=0.0
Final: train_loss=0.38524182, token_acc=0.91372913, runtime=13589.8s
EXIT_CODE=0
```

**Warnings**: bitsandbytes libnvJitLink.so.13 load warning (non-critical)
**Errors**: None

---

### v4-taxei-rp-s1 (seed=1, cuda:3)

**Timing**: Started 2026-05-16 10:18:34, ended 14:05:16
**Checkpoints** (save_strategy=epoch):
- `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s1/v0-20260516-101834/checkpoint-1805` (epoch 1)
- `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s1/v0-20260516-101834/checkpoint-3610` (epoch 2)
- `/root/autodl-tmp/tax_error_inject_agent/output/v4-taxei-rp-s1/v0-20260516-101834/checkpoint-5415` (epoch 3, final)

**Log tail (last steps)**:
```
step 5400: loss=0.2377, token_acc=0.9117, lr=0.0
step 5410: loss=0.2427, token_acc=0.9093, lr=0.0
Final: train_loss=0.38530399, token_acc=0.91761223, runtime=13577.8s
EXIT_CODE=0
```

**Warnings**: bitsandbytes libnvJitLink.so.13 load warning (non-critical)
**Errors**: None