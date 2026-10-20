# 7B Pilot Validation Plan

## Objective

Validate LoRA SFT hyperparameters on Qwen2.5-7B before committing to full dosage matrix (8 runs, ~16h GPU). One d000 run + eval to confirm training stability and no capability regression.

## D018 Lesson Summary

3B GSM8K collapsed from 60.5% to 11.7% with original config (r=16, alpha=32, **lr=2e-4**, effective scale=4e-4). Root cause: excessive learning rate for LoRA scale. After standardizing to **lr=5e-5** (effective scale=1e-4, D076), all 3B runs stable. The 4x lr reduction fixed the issue completely.

For 7B: relative perturbation ||delta_W||/||W|| is *smaller* at 7B than 3B for same LoRA config (same rank, more base params). Theoretically 3B config should be *more conservative* on 7B, not less. But empirical validation is required given D018 history.

---

## Pilot Run Configuration

### Hardware
- 1x A100 80GB
- Memory estimate: ~14GB model (bf16) + ~2GB LoRA + ~25GB activations (bs=4, seq=2048) = ~41GB (fits)

### Config A (Recommended First: 3B-identical)

```bash
CUDA_VISIBLE_DEVICES=0 python3 train_sft.py \
    --model-name Qwen/Qwen2.5-7B \
    --data-path <d000_sft_data.jsonl> \
    --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42 \
    --seed 42 \
    --gpu 0 \
    --lr 5e-5 \
    --lora-r 16 \
    --lora-alpha 32 \
    --batch-size 4 \
    --grad-accum 4 \
    --epochs 1 \
    --max-seq-length 2048 \
    --cache-dir /root/autodl-tmp/.hf_cache
```

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| r | 16 | Match 3B (7 target modules, rank per module) |
| alpha | 32 | Match 3B (alpha/r = 2.0) |
| lr | 5e-5 | Match 3B standardized (D076) |
| effective scale | 1e-4 | Same as 3B; relative perturbation smaller on 7B |
| batch_size | 4 | Match 3B |
| grad_accum | 4 | Effective batch = 16, match 3B |
| epochs | 1 | Match 3B |
| warmup | 0.05 | Match 3B |
| scheduler | cosine | Match 3B |
| dropout | 0.05 | Match 3B |
| target_modules | q,k,v,o,gate,up,down | Match 3B (all linear projections) |

### Config B (Fallback: lr halved)

Only if Config A fails success criteria.

| Parameter | Value | Change from A |
|-----------|-------|---------------|
| lr | 2e-5 | Halved (effective scale = 4e-5) |
| All others | Same | -- |

### Config C (Emergency: reduced everything)

Only if Config B also fails.

| Parameter | Value | Change from A |
|-----------|-------|---------------|
| r | 8 | Halved |
| alpha | 16 | Halved (alpha/r still 2.0) |
| lr | 1e-5 | 5x reduction (effective scale = 2e-5) |

---

## Evaluation Protocol

Post-training eval on 3 benchmarks (same pipeline as exp-001):

1. **MMLU** (MCQ, 5-shot): core MC benchmark
2. **GSM8K** (generative, 8-shot CoT): the D018 failure indicator
3. **ARC-Challenge** (MCQ, 25-shot): secondary MC benchmark

Pre-SFT baseline: eval Qwen2.5-7B base model on same benchmarks before SFT (one-time, reusable).

---

## Success / Failure Criteria

### Pass (proceed to full matrix)

| Metric | Threshold | Rationale |
|--------|-----------|-----------|
| MMLU | >= baseline - 2pp | MC tasks should not degrade from d000 SFT |
| GSM8K | >= baseline - 5pp | Primary failure mode from D018; generous margin |
| ARC | >= baseline - 2pp | MC tasks should not degrade from d000 SFT |
| Training loss | Final < 1.5, no NaN/Inf | 3B final loss was ~1.07-1.21 |
| Loss curve | Monotonic decrease, no spikes > 2x | Stability check |

### Fail (try next config)

Any of:
- GSM8K drops > 5pp from baseline (D018 pattern)
- MMLU or ARC drops > 3pp
- Training loss diverges, NaN, or fails to decrease
- OOM (adjust batch_size first before switching config)

### Abort (escalate)

All 3 configs fail, or unexpected behaviors (e.g., model generates gibberish).

---

## Decision Tree

```
Config A (3B-identical, lr=5e-5)
|-- PASS --> Use Config A for full 7B matrix
|-- FAIL
    |-- GSM8K collapse / eval degradation --> Config B (lr=2e-5)
    |   |-- PASS --> Use Config B for full 7B matrix
    |   |-- FAIL --> Config C (r=8, alpha=16, lr=1e-5)
    |       |-- PASS --> Use Config C for full 7B matrix
    |       |-- FAIL --> Abort, escalate to Director
    |-- OOM --> Reduce batch_size to 2 (grad_accum to 8), retry same config
```

---

## GPU Time Estimates

| Step | Estimated Time |
|------|---------------|
| Download Qwen2.5-7B | ~15 min (if not cached) |
| Pre-SFT baseline eval (3 benchmarks) | ~1h |
| Pilot SFT training (1 epoch, d000) | ~2-3h |
| Post-SFT eval (3 benchmarks) | ~1h |
| **Total pilot (Config A)** | **~4-5h** |
| Each additional config attempt | +3-4h |

---

## Post-Pilot: Full Matrix Launch

Once pilot config validated:

### 7B Full Matrix (Qwen2.5-7B)
- Dosages: d000, d005, d025, d100
- Seeds: 42, 123
- Total: 4 x 2 = 8 SFT runs
- Parallelism: 2 A100s, 4 runs each, ~8h wall time
- Then: eval (aligned + para_aligned) + signal computation

### 14B Extension (if GPU budget allows)
- Same pilot-first protocol
- Additional concern: A100 80GB may need gradient checkpointing for 14B
- Config A for 14B: same as validated 7B config (if 7B used Config A)
- If 7B required lr reduction, apply proportional further reduction for 14B

### Llama-3.1-8B Cross-Family
- Same pilot protocol, Config A first
- Note: Llama uses different tokenizer/chat template; ensure eval pipeline handles it
- Dosages: d000, d005, d025, d100 x 1 seed

### Launch Sequence
1. 7B pilot (this plan): 1 A100, ~4h
2. 7B full matrix: 2 A100s, ~8h
3. 14B pilot: 1 A100, ~6h (larger model)
4. 8B Llama pilot: 1 A100, ~4h
5. 14B + 8B full matrix: 2 A100s, ~16-32h

Total: ~4 days with 4x A100 80GB (matches ROADMAP estimate).

---

## Pre-flight Checklist (before submitting pilot)

- [ ] `nvidia-smi` confirm target GPU idle (C001, C002)
- [ ] `ps aux | grep train` confirm no residual processes (C003)
- [ ] `CUDA_VISIBLE_DEVICES=N` explicitly set in command (C004)
- [ ] d000 SFT data file exists and is correct format
- [ ] Qwen2.5-7B weights downloaded or accessible
- [ ] Disk space sufficient (~30GB for model + checkpoints)
- [ ] Pre-SFT baseline eval completed first
- [ ] `cat adapter_config.json | grep lora_alpha` post-training confirms alpha=32 (C006)

---

## Script Modification Note

`train_sft.py` default lr is 2e-4 (the D018-era value). The standardized lr=5e-5 must ALWAYS be passed via `--lr 5e-5` flag. Consider updating the script default to 5e-5 to prevent future accidents. The `run_exp001.sh` orchestrator does NOT pass `--lr`, so it would use the dangerous default if run as-is.
