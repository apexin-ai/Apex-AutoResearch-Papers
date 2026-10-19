# v9d (8B Cell C Episode-level GRPO) Step 7-8 Analysis

**Date**: 2026-05-20
**W&B Run**: 4x8hludk (`8b-cell-c-v9-fsdp2-offload`)
**Progress**: Step ~7-8 / 30 | ETA ~8h | ~22 min/step

## 1. Current Metrics

| Metric | Step 6 | Step 7 | W&B Latest | Trend |
|--------|--------|--------|------------|-------|
| train/success_rate | 0.852 | 0.914 | — | POSITIVE |
| pass_at_8 | — | 1.000 | — | saturated |
| actor/entropy | — | 0.0473 | 0.0597 | very low |
| kl | — | -0.034 | — | near zero |
| actor/pg_loss | — | 0.00096 | 0.000604 | near zero |
| actor/pg_clipfrac | — | — | 0.00243 | near zero |
| actor/grad_norm | — | 0.573 | 0.382 | low, stable |
| GPU util | 75-100% | — | — | healthy |
| GPU mem | 24/98 GB | — | — | OK |

**Config highlights**: GRPO (kl_coef=0, use_kl_loss=false), lr=5e-7, clip_ratio=0.2, entropy_coeff=0.001, FSDP2+CPUOffload, 4x GPU, train_batch=128 (16 groups x 8 rollouts)

## 2. Comparison with 1.7B Experiments

### 2.1 Training Success Rate Progression

| Experiment | Model | Step 1 | Step 5 | Step 7 | Step 15 | Best Train |
|-----------|-------|--------|--------|--------|---------|------------|
| **v9d** | **8B** | **—** | **—** | **91.4%** | **TBD** | **91.4% (step 7)** |
| Cell A seed1 | 1.7B | 20.3% | — | 4.7% | 0% | 20.3% (step 1) |
| Cell A seed2 | 1.7B | — | — | — | 55.5% | 55.5% (step 15) |
| Cell B seed1 | 1.7B | 18.75% | 1.56% | 4.7% | 0% | 18.75% (step 1) |
| Cell B seed2 | 1.7B | — | — | — | 28.12% | 28.12% (step 15) |
| hsweep h=20 | 1.7B | 20.3% | — | — | — | 28.1% (step 4) |

### 2.2 OOD / Eval Results

| Experiment | Model | OOD Success | action_is_valid | Dataset |
|-----------|-------|-------------|-----------------|---------|
| exp029 Cell C | 1.7B | 23.88% | 56.83% | AlfworldSG_OOD 134 tasks |
| exp029 per-task t=0.4 | 1.7B | 19.4% | — | 134 tasks |
| Cell A seed1 best | 1.7B | 5.97% | — | AlfworldOOD 134 tasks |
| Cell B seed2 | 1.7B | 9.375% | 99.4% | 16 in-dist tasks |
| **v9d** | **8B** | **TBD** | **TBD** | **pending step 10 eval** |

### 2.3 SFT Baselines (before GRPO)

| Model | In-dist Success | OOD Success |
|-------|----------------|-------------|
| 8B SFT (clean v2) | 71.875% | — |
| 8B SFT (det eval) | 68.75% | — |
| 1.7B SFT (OOD) | — | 80.6% |

**v9d GRPO gain over 8B SFT**: 91.4% vs 71.875% = **+19.5pp** at step 7 (in-dist training set).

### 2.4 Key Scaling Observations

- **8B >> 1.7B on train success**: 91.4% at step 7 vs best 1.7B of 55.5% at step 15. Scaling works.
- **8B converges much faster**: Near-saturation by step 7. All 1.7B runs needed 15 steps and still fell far short.
- **No collapse**: 1.7B Cell B seed1 collapsed by step 4 (invalid_action → 97%). 8B shows zero signs of instability.
- **Critical unknown**: OOD generalization. 1.7B Cell C achieved 23.88% OOD despite lower train success. 8B's OOD test is pending (test_freq=5, next eval at step 10).

## 3. Training Dynamics Analysis

### 3.1 Entropy: CONCERNING (watch closely)

- **v9d step 7**: 0.047-0.060
- **1.7B Cell B seed2 step 15**: 0.401
- **1.7B Cell B seed1 step 15** (collapsed): 0.342

v9d's entropy is **~7x lower** than 1.7B experiments at their endpoints. The policy is extremely deterministic. This is consistent with the high success rate (the model "knows" what to do), but leaves almost no exploration margin. If the policy has found a local optimum that works for training tasks but not OOD tasks, low entropy means it cannot escape.

**Mitigating factor**: entropy_coeff=0.001 provides a small entropy bonus. The 8B model's larger capacity may mean it has legitimately learned robust policies rather than memorizing patterns. pass_at_8=1.0 suggests some remaining diversity.

**Verdict**: Not mode collapse (too high success rate), but approaching **premature convergence**. Remaining 23 steps may yield minimal further improvement.

### 3.2 KL Divergence: POSITIVE

- **v9d step 7**: -0.034 (effectively zero)
- **1.7B Cell A seed1 step 15**: 2.845 (severe drift)
- **1.7B Cell A seed1 step 5**: 0.735

KL is extremely well controlled. Two reasons:
1. Config sets kl_coef=0 and use_kl_loss=false (no KL penalty in loss)
2. Despite no explicit KL control, the policy hasn't drifted far from the reference — the conservative lr=5e-7 and clip_ratio=0.2 act as implicit constraints

This is excellent. The 1.7B experiments suffered from KL drift (Cell A seed1 degraded from 5.97% to 0.75% OOD as KL rose to 2.845). No such risk here.

### 3.3 Gradient Norm: POSITIVE

- **v9d step 7**: 0.382-0.573
- **1.7B Cell B seed1 step 15**: 1.611

Stable and low. No gradient explosion. FSDP2 + gradient checkpointing + grad_clip=1 keeping things smooth.

### 3.4 Policy Gradient Loss & Clipfrac: NEUTRAL (saturating)

- pg_loss: 0.0006 (near zero)
- clipfrac: 0.0024 (near zero, only 0.24% of tokens clipped)

The policy is barely updating. This means:
- The model already generates near-optimal actions for the training distribution
- GRPO advantages are small (most rollouts succeed, so the advantage contrast is low)
- Remaining 23 steps will likely see diminishing returns on training set metrics

## 4. Predictions for Remaining Steps

| Metric | Prediction | Confidence |
|--------|-----------|------------|
| train/success_rate step 15 | 93-96% | HIGH (near ceiling) |
| train/success_rate step 30 | 95-98% | MEDIUM |
| entropy step 15 | 0.02-0.04 | MEDIUM (continued slow decline) |
| entropy step 30 | 0.01-0.03 | LOW |
| OOD success step 10 eval | 30-50% | LOW (high uncertainty) |
| Mode collapse risk | LOW | HIGH confidence |
| Diminishing returns | YES | HIGH |

## 5. Risks & Recommendations

### Disk Risk (ACTIVE)
Registry notes: "step 5 ckpt still 92GB (pre-config-change). step 10 ckpt must be ~33GB or disk crash." With save_freq=5 and max_actor_ckpt_to_keep=2, verify step 10 checkpoint size. 91GB available but two 92GB checkpoints would overflow.

### Premature Convergence
Training success is nearly saturated. The real question is whether step 5-10 val/OOD numbers show generalization. If OOD success is low despite 91% train success, this indicates **overfitting to the training task distribution**.

### Entropy Floor
entropy_coeff=0.001 provides minimal entropy bonus. If entropy drops below 0.01, consider whether the model can still explore novel OOD scenarios.

### Recommendation
1. **Priority 1**: Wait for step 10 val/eval results (test_freq=5). This is the most informative signal.
2. **Priority 2**: Verify disk — confirm step 10 checkpoint will be ~33GB, not 92GB.
3. **Do NOT stop early** based on training metrics alone. The train/OOD gap is the key research question.
4. If step 10 OOD eval shows < 30%, consider whether continuing to step 30 adds value vs. pivoting to curriculum/exploration strategies.

## 6. Summary

| Dimension | Assessment |
|-----------|-----------|
| Training success | POSITIVE — 91.4%, massive 8B vs 1.7B scaling gain |
| Training stability | POSITIVE — no collapse, low grad_norm, controlled KL |
| Convergence speed | POSITIVE — near-saturation in 7 steps |
| Entropy / exploration | CONCERNING — very low (0.05), risk of premature convergence |
| OOD generalization | UNKNOWN — critical pending step 10 eval |
| Disk safety | AT RISK — needs checkpoint size verification |
| Remaining training value | UNCERTAIN — may have diminishing returns |

**Bottom line**: v9d demonstrates that 8B episode-level GRPO works dramatically better than 1.7B on in-distribution training (91.4% vs best 55.5%). Training dynamics are healthy. The open question — and the one that matters for the paper — is OOD generalization. Step 10 eval will be decisive.
