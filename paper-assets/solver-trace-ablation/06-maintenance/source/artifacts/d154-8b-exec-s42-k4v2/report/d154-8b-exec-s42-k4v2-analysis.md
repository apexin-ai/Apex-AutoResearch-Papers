# D154: Qwen3-8B Exec-Only GRPO Analysis

## Experiment Config
- **Model**: Qwen3-8B (from /root/autodl-tmp/models/Qwen3-8B)
- **Mode**: execution_only (exec-only reward)
- **Data**: train_500_seed42.jsonl (500 examples)
- **Steps**: 500, K=4, bf16, seed=42
- **Server**: westd-39279
- **Training time**: 2h36m (9395s)
- **Output**: /root/autodl-tmp/outputs/d154_8b_exec_s42_k4_v2/

## Training Status: COMPLETED (EXIT_CODE=0)
No errors or traceback. Model saved at checkpoint-500.

## Key Metrics

### Reward Trajectory (milestone steps)

| Step | Reward | Prove Rate | ISR | Loss |
|------|--------|------------|-----|------|
| 1 | 0.250 | 0.250 | 0.200 | 0.0 |
| 50 | 0.250 | 0.250 | 0.066 | — |
| 100 | 0.438 | 0.438 | 0.162 | -0.034 |
| 250 | 0.000 | 0.000 | 0.000 | 0.0 |
| 300 | 0.063 | 0.063 | 0.042 | -0.088 |
| 400 | — | — | — | — |
| 500 | 0.313 | 0.312 | 0.184 | 0.062 |

### Overall Summary (from training log)
- **Average prove_rate**: 0.1551 (across all 500 steps)
- **Average ISR**: 0.0820
- **parse_rate**: 1.000 (perfect throughout)
- **Train loss**: 0.0149
- **Entropy**: dropped from ~0.05-0.07 (early) to ~0.04-0.05 (late) — moderate collapse

### Training Dynamics
- **Extremely noisy reward**: no clear upward trend across 500 steps
- **High zero-reward fraction**: many steps have reward=0 with all K=4 samples failing
- **frac_reward_zero_std = 1.0** at most steps → all 4 samples get identical reward → zero GRPO gradient
- **Sparse gradient signal**: loss=0 and grad_norm=0 at majority of steps
- Occasional spikes (e.g., step 99: reward=0.688, step 498: reward=0.75) but no sustained improvement

## Comparison with 4B Exec-Only (d146-pf series)

| Metric | 4B-s42 | 4B-s43 | 4B-s44 | **8B (this)** |
|--------|--------|--------|--------|---------------|
| Final prove_rate | 1.00 | 1.00 | 1.00 | **0.155** |
| Converges? | Yes | Yes | Yes | **No** |
| Hacking mode | 99 TS (100%) | 31 CE (49%) | 71 CE (99%) | N/A |
| Genuine rate | 0% | 50.8% | 1.4% | N/A |
| Goodhart collapse | **Yes** | **Yes** | **Yes** | **No** |

**4B pattern**: Reward converges to ~1.0 within 500 steps, but achieved primarily through hacking (TS=template shortcut, CE=conclusion echo). Classic Goodhart effect — reward optimized without genuine reasoning.

**8B pattern**: Reward stays flat at ~0.15 average. Model fails to learn from exec-only reward at all. No convergence, no hacking — just stagnation.

## Diagnosis

The 8B model exhibits a **qualitatively different failure mode** from 4B:

1. **Not Goodhart collapse** — the model never achieves high reward to begin with
2. **Entropy collapse without reward improvement** — output diversity drops (entropy 0.07→0.04) but the narrow distribution the model converges to mostly produces failing proofs
3. **K=4 insufficient for 8B** — with a larger model, K=4 generates near-identical samples (frac_reward_zero_std≈1.0), providing no contrastive signal for GRPO. The 4B model has lower entropy from the start, making K=4 adequate to find at least some reward-varying samples
4. **Possible LR mismatch** — cosine decay from 1e-6 to near-zero may be suboptimal for 8B's larger parameter space

## Conclusion: **NEGATIVE**

The hypothesis that "larger model (8B) exhibits same Goodhart collapse under exec-only reward" is **not confirmed**. Instead of reward gaming, 8B shows training stagnation — the GRPO training signal is too weak (K=4 too low) for the larger model to learn at all.

### Caveats
- This negative result may be a **config issue** (K too low) rather than a genuine model-size effect. Rerunning with K=8 or K=16 would disambiguate.
- The 4B experiments used Qwen2.5-4B; this uses Qwen3-8B. Architecture differences (not just scale) may contribute.
- No STA/hacking classification was run on the 8B outputs because prove_rate is too low to produce meaningful classification results.

### Suggested Next Steps
1. **K=8 or K=16 rerun** to test whether higher sampling restores learning
2. **Higher LR** (e.g., 2e-6 or 5e-6) to test whether 8B needs stronger gradients
3. If reward does converge with adjusted config, then run STA classification to check for Goodhart collapse
