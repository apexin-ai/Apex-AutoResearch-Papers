# Experiments and Results

## 4.1 GRPO Reward-Accuracy Decoupling is Universal (Claim 1)

We evaluate whether GRPO training improves reasoning accuracy beyond the SFT baseline. Table 1 reports GSM8K accuracy for all three pruning conditions under both recovery paradigms.

**Table 1: GRPO reward-accuracy decoupling across pruning conditions.** $N = 1{,}319$ GSM8K test problems, greedy decoding, seed 42.

| Model | SFT Acc (%) | GRPO Acc (%) | $\Delta$ (pp) | Peak Reward | Collapse |
|-------|-------------|--------------|---------------|-------------|----------|
| Unpruned | 81.27 | 81.27 | 0.00 | 0.661 | None |
| Standard 20% | 59.29 | 58.91 | -0.38 | 0.096 | Transient |
| RASP 20% | 61.49 | 60.65 | -0.84 | 0.039 | Permanent |

*Sources: eval\_sft\_unpruned\_full, eval\_grpo\_unpruned\_v2\_step100, eval\_sft\_standard\_full\_westd, eval\_grpo\_standard\_step50\_full, eval\_sft\_rasp\_full\_westd, eval\_grpo\_rasp\_v9\_step5.*

The unpruned model provides the strongest evidence for universal decoupling. GRPO drives reward from 0 to 0.661 over 100 steps, yet GSM8K accuracy remains exactly 81.27% (1,072/1,319 correct answers, identical to SFT). The model produces 1,072 of the same correct answers under both conditions. Reward improvement reflects changes in output format and length distribution, not genuine reasoning gains. This result holds despite stable training with no collapse and sustained gradient flow throughout all 100 steps (final grad\_norm = 6.97, final entropy = 0.194).

For pruned models, the pattern is consistent: Standard achieves its best GRPO accuracy at step 50 (58.91%), 0.38pp below SFT. RASP achieves 60.65% at step 5, 0.84pp below SFT. Neither pruning condition shows any accuracy benefit from GRPO. The GRPO accuracy for RASP at step 10 is 61.87% ($p = 0.52$ vs step 5), confirming that early collapse onset does not reduce accuracy below the SFT baseline either.

We additionally verify this decoupling on a second checkpoint: the unpruned model at step 90 achieves 80.59% (1,063/1,319), confirming accuracy stability across the final 10 steps of training despite continued reward fluctuation.

**Cross-model validation.** On Qwen2.5-Math-7B at 20% sparsity ($N = 200$), the same pattern holds: RASP post-SFT 72.5% vs post-GRPO 72.5% ($\Delta = 0.0$pp); Standard post-SFT 71.0% vs post-GRPO 70.5% ($\Delta = -0.5$pp). Reward-accuracy decoupling is not model-specific.

*Sources: eval\_sft\_rasp\_qwen\_math\_n200, eval\_grpo\_rasp\_20\_qwen\_math, eval\_sft\_standard\_qwen\_math\_n200, eval\_grpo\_standard\_20\_qwen\_math.*

## 4.2 Collapse Severity Gradient Diagnoses Structural Damage (Claim 2)

Beyond the universal accuracy plateau, pruned models exhibit a qualitatively different failure mode: GRPO training collapse. The severity and onset timing form a clean gradient that tracks the aggressiveness of redundancy removal.

**Table 2: GRPO collapse dynamics by pruning condition.**

| Model | Collapse Onset | Peak Reward | Final frac\_zero\_std | Final grad\_norm | Recovery? |
|-------|---------------|-------------|----------------------|-----------------|-----------|
| Unpruned | N/A | 0.669 (step 80) | 0.275 | 6.97 | N/A |
| Standard 20% | Step ~60 | 0.096 | 0.65 | 0.42 | Yes (transient) |
| RASP 20% | Step ~10 | 0.039 (step 20) | 0.95 | 0.007 | No (permanent) |

*Sources: grpo\_unpruned\_v2, grpo\_stage2\_standard\_20\_v8, grpo\_stage2\_rasp\_20\_v9.*

The three-model comparison reveals a severity gradient aligned with redundancy removal intensity. The unpruned model trains stably for 100 steps, with frac\_zero\_std never exceeding 0.275 and reward climbing monotonically from 0.425 to 0.669. The model maintains exploration diversity throughout training.

Standard pruning (importance-only, $\alpha = 0$) shows a transient collapse at step 60: frac\_zero\_std spikes above 0.8, reward dips, and gradient norm drops temporarily. The model recovers by step 90 as reward signal re-emerges from the remaining viable completions. This transient pattern indicates partial loss of exploration capacity that the model can compensate for given sufficient training steps.

RASP pruning ($\alpha = 1.0$) collapses permanently at step 10. By step 30, frac\_zero\_std reaches 0.95, gradient norm drops to 0.007, and reward peaks at only 0.039 before declining. The model converges to a degenerate policy where nearly all completions within each group receive identical rewards, eliminating the relative advantage signal that GRPO requires. Mean terminated completion length drops sharply, indicating the model produces minimal outputs rather than reasoning chains.

**Mechanism.** RASP preferentially removes groups with high functional overlap (high $F(h)$), preserving functionally unique structures. Under SFT, this is beneficial because unique structures contribute non-redundant gradient directions for supervised recovery. Under GRPO, the removed redundant structures would have provided backup exploration paths: alternative generation strategies that maintain reward variance across the completion group. Without these paths, the policy quickly converges to a single mode, collapsing the reward distribution and eliminating GRPO's learning signal.

The 6$\times$ speedup from Standard collapse (step 60) to RASP collapse (step 10) directly corresponds to the difference in redundancy removal. Standard pruning removes groups by importance alone, incidentally preserving some redundant structures. RASP explicitly targets redundant structures for preservation avoidance, leaving fewer backup paths.

**Higher sparsity confirmation.** At 25% sparsity, both methods exhibit near-total collapse: RASP reaches frac\_zero\_std = 0.875 with reward 0.009, Standard reaches near-complete collapse with reward 0.0075. The collapse gradient compresses at higher sparsity, consistent with reduced overall capacity leaving minimal room for either method to sustain RL exploration.

*Sources: grpo\_rasp\_25 (wandb: bc4ojqie), grpo\_standard\_25 (wandb: 16vqw4e6).*

## 4.3 Recovery Method Conditions Optimal Pruning (Claim 3)

The preceding sections establish that RASP and Standard pruning interact differently with GRPO. We now examine the SFT recovery direction, where RASP's design rationale predicts an advantage.

**SFT Recovery Comparison (N = 1,319, greedy, seed 42):**
- RASP 20%: 61.49% (811/1,319)
- Standard 20%: 59.29% (782/1,319)
- Difference: +2.20pp in favor of RASP
- McNemar's test: $p = 0.25$ (not statistically significant)

*Sources: eval\_sft\_rasp\_full\_westd, eval\_sft\_standard\_full\_westd.*

RASP achieves a marginal SFT advantage of 2.2 percentage points. While this difference does not reach statistical significance at the current sample size, the direction is consistent with RASP's design: preserving functionally unique structures provides non-redundant gradient directions during supervised learning, enabling slightly more efficient recovery.

**The Redundancy-Stability Tradeoff.** Combining the SFT and GRPO results reveals a fundamental tension:

| Recovery Paradigm | RASP vs Standard | Interpretation |
|-------------------|-----------------|----------------|
| SFT | +2.2pp (marginal advantage) | Redundancy removal helps: unique structures provide efficient gradient directions |
| GRPO | 6$\times$ faster collapse | Redundancy removal harms: backup paths needed for exploration stability |

The structures that RASP identifies as optimal to remove (high-overlap, redundant groups) play opposite roles under the two recovery paradigms. For supervised learning, redundancy is expendable because gradient-based optimization can redistribute function across remaining structures. For reinforcement learning, redundancy provides the exploration stability that prevents policy collapse.

This tradeoff implies that no single pruning strategy is universally optimal. The choice of which structures to preserve must be conditioned on the intended recovery paradigm. A practitioner who plans SFT-only recovery can safely (even preferably) remove redundant structures. A practitioner who plans RLVR alignment must preserve them.

**Cross-model evidence.** On Qwen2.5-Math-7B ($N = 200$), the SFT direction shows RASP 72.5% vs Standard 71.0% (+1.5pp), while GRPO dynamics show entropy collapse from step 1 for RASP (frac\_zero\_std\_final = 0.675) versus milder collapse for Standard. The tradeoff pattern reproduces across model families.

*Sources: eval\_sft\_rasp\_qwen\_math\_n200, eval\_sft\_standard\_qwen\_math\_n200, grpo\_rasp\_qwen\_math\_v3.*

## 4.4 Alpha Ablation

We verify that the CKA weight $\alpha$ systematically controls the redundancy-accuracy tradeoff. Table 3 reports post-prune accuracy across $\alpha$ values (20% sparsity, $N = 100$, calibration = 512).

**Table 3: Effect of $\alpha$ on post-prune accuracy.**

| $\alpha$ | Post-prune Acc (%) | EOS Rate (%) | Avg Response Length |
|----------|-------------------|--------------|---------------------|
| 0.0 (Standard) | 27 | 80 | 1,192 |
| 0.25 | 23 | 63 | 1,834 |
| 0.5 | 22 | 81 | 1,141 |
| 1.0 (RASP default) | 31 | 92 | 733 |
| 2.0 | 36 | 59 | 2,130 |

*Source: alpha\_ablation\_sweep (calibration = 512, N = 100).*

The relationship between $\alpha$ and post-prune accuracy is non-monotonic, with a U-shape: moderate $\alpha$ values (0.25, 0.5) slightly decrease accuracy relative to $\alpha = 0$, while $\alpha \geq 1.0$ improves it. This pattern arises because low non-zero $\alpha$ partially disrupts importance ranking without providing sufficient functional-uniqueness benefit, while higher $\alpha$ values create a clear bias toward preserving unique structures that carry irreplaceable function.

Post-SFT results ($N = 100$) show the gap narrows: $\alpha = 0.0$ achieves 64%, $\alpha = 1.0$ achieves 57%, $\alpha = 2.0$ achieves 62%, and $\alpha = 4.0$ achieves 62%. SFT recovery partially equalizes scoring differences, consistent with supervised learning's ability to redistribute function across remaining structures.

*Sources: eval-sft-alpha-0p0, eval-sft-alpha-1p0, eval\_sft\_alpha\_2p0, sft\_alpha4\_0\_westd\_retry.*

The tradeoff implication is clear: higher $\alpha$ removes more redundancy, which benefits post-prune and post-SFT accuracy modestly but accelerates GRPO collapse. The $\alpha$ parameter directly controls position along the Redundancy-Stability Tradeoff curve.
