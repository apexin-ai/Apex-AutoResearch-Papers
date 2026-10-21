# Free-form vs Constrained Decoding: Deep Ablation Analysis

**Setup**: 551 instances × 8 samples, Qwen3-8B, SciERC, seed=42, T=1.0, max_tokens=1024.
- Constrained: `exp_012_rerun_1024/samples.jsonl`
- Free-form: `exp_freeform_ablation/samples.jsonl`

---

## 1. RE LP Selection Flip

**Phenomenon**: LP selection gap for RE flips from -0.68pp (constrained) to +1.69pp (free-form).

### 1.1 Per Relation Type Breakdown

| Relation Type | N instances | Constrained Gap | Free-form Gap | Δ (flip) |
|:---|---:|---:|---:|---:|
| USED-FOR | 299 | -1.41% | +2.42% | +3.83% |
| CONJUNCTION | 86 | -0.81% | +1.65% | +2.46% |
| EVALUATE-FOR | 62 | -1.61% | +0.07% | +1.68% |
| FEATURE-OF | 50 | -0.86% | +0.50% | +1.36% |
| PART-OF | 44 | -4.51% | +2.01% | **+6.52%** |
| HYPONYM-OF | 36 | -3.12% | +1.34% | +4.45% |
| COMPARE | 35 | -1.36% | +0.12% | +1.48% |

**Interpretation**: The flip is **universal** — all 7 relation types show negative constrained gap and positive (or neutral) free-form gap. This rules out the hypothesis that a single dominant relation type drives the effect. The largest flips occur on PART-OF (+6.52pp) and HYPONYM-OF (+4.45pp), both of which are semantically subtle types requiring precise entity boundary identification. USED-FOR, the most frequent type (54% of instances with relations), contributes the largest absolute mass (+3.83pp × 299 instances).

### 1.2 LP–F1 Correlation by Subtask

| Condition | NER ρ | NER p | RE ρ | RE p |
|:---|---:|---:|---:|---:|
| Constrained | 0.171 | 5.24e-05 | 0.318 | 1.88e-14 |
| Free-form | 0.189 | 8.09e-06 | 0.301 | 4.83e-13 |

**Interpretation**: The Spearman ρ between LP-selected sample's mean logprob and F1 is actually slightly *lower* for RE in free-form (0.301 vs 0.318). This means the flip is **not** due to improved LP–quality correlation overall, but rather to a change in the *distribution* of errors: in constrained mode LP selection is systematically biased toward wrong RE answers, while in free-form this bias disappears.

### 1.3 LP Variance Structure

| Metric | Constrained | Free-form |
|:---|---:|---:|
| Mean LP std | 0.0206 | 0.0199 |
| Mean LP range | 0.0623 | 0.0599 |
| LP_std ↔ NER F1 range (ρ) | +0.329 | +0.337 |
| LP_std ↔ RE F1 range (ρ) | **-0.131** | **-0.152** |

**Interpretation**: A critical asymmetry: LP variance positively correlates with NER F1 range (when LP varies more, NER quality varies more — so LP can select) but **negatively** correlates with RE F1 range. This means instances where RE quality varies most across samples tend to have *compressed* LP variance, making LP selection near-random for RE. Free-form slightly amplifies this negative correlation (-0.152 vs -0.131), but the key difference lies in *where* the variance is allocated (see §1.5).

### 1.4 Instance-Level Flip Analysis

31 instances flip from "constrained LP wrong" to "free-form LP right" (5.6% of 551).

| Characteristic | Flip Instances (N=31) | Other Instances (N=520) | Baseline (N=551) |
|:---|---:|---:|---:|
| Mean gold relations | **3.3** | 1.7 | 1.8 |
| Mean gold entities | **4.6** | 3.0 | 3.1 |
| Mean LP std (constrained) | 0.0162 | 0.0209 | 0.0206 |
| Mean LP std (free-form) | 0.0182 | 0.0200 | 0.0199 |
| Mean LP range (constrained) | 0.0496 | 0.0631 | 0.0623 |
| Mean LP range (free-form) | 0.0564 | 0.0601 | 0.0599 |
| NER F1 of LP-sel (constrained) | 0.662 | — | — |
| NER F1 of LP-sel (free-form) | **0.763** | — | — |

Relation type distribution among flip instances: USED-FOR (25), PART-OF (8), CONJUNCTION (7), FEATURE-OF (6), EVALUATE-FOR (6), COMPARE (4), HYPONYM-OF (4).

**Interpretation**: Flip instances are **relation-dense** (3.3 gold rels, nearly 2× baseline) but have **low LP variance** in constrained mode (0.0162 vs 0.0209 for others). The constrained format forces structurally similar outputs on these complex instances, compressing LP spread and making selection near-random. Free-form relaxes this constraint: LP variance increases from 0.0162 to 0.0182 (+12%), and more importantly, the NER F1 of the LP-selected sample jumps from 0.662 to 0.763, suggesting free-form LP preferentially selects samples with better entity boundaries, which cascades into better RE.

### 1.5 Hypothesis Test: LP Variance × RE Difficulty

Instances split at median greedy RE F1 (0.400).

| Group | N | Constrained LP std | Free-form LP std | F/C Ratio |
|:---|---:|---:|---:|---:|
| RE-difficult (F1 < 0.40) | 194 | 0.0185 | 0.0196 | **1.06** |
| RE-easy (F1 ≥ 0.40) | 203 | 0.0159 | 0.0136 | **0.86** |

Mann-Whitney U tests (one-sided: difficult > easy):
- Free-form: U = 24269, **p < 0.0001**
- Constrained: U = 22720, p = 0.0040

**Interpretation**: Free-form decoding **selectively amplifies** LP variance on RE-difficult instances (ratio 1.06) while **dampening** it on RE-easy instances (ratio 0.86). Constrained decoding also shows this pattern but less pronounced (both groups have moderately different variance, p = 0.004). The selective amplification in free-form means difficult instances get more LP spread — and thus more discriminative power for LP selection — exactly where it matters most.

### 1.6 LP Selection Win/Loss Balance

| Condition | Correct (LP > greedy) | Wrong (LP < greedy) | Tied | Net |
|:---|---:|---:|---:|---:|
| Constrained | 36 (9.1%) | 59 (14.9%) | 302 | **-23** |
| Free-form | 45 (11.3%) | 45 (11.3%) | 307 | **0** |

(Only instances with ≥1 gold relation, N=397)

**Interpretation**: The asymmetry in constrained mode (23 more wrong than correct) is the direct cause of the -0.68pp gap. Free-form brings the win/loss ratio to parity (45:45), which — combined with the fact that correct instances tend to have larger F1 deltas than wrong instances — produces the +1.69pp gap. The mechanism: constrained decoding creates a systematic bias where higher-LP samples tend to be ones that copied more entity tokens verbatim (higher NER logprob) but failed at relation typing; free-form breaks this coupling.

---

## 2. Non-Tied Subset Overlap

**Phenomenon**: Constrained tied fraction = 59.7%, free-form = 57.7% (only -2pp). But does the non-tied set composition change?

### 2.1 Set Overlap Statistics

| Metric | Value |
|:---|---:|
| Constrained non-tied | 222 (40.3%) |
| Free-form non-tied | 233 (42.3%) |
| Intersection (both non-tied) | 146 |
| Union (either non-tied) | 309 |
| **Jaccard similarity** | **0.472** |
| New non-tied in free-form | 87 |
| Lost non-tied in free-form | 76 |

**Interpretation**: Despite near-identical tied fractions, the Jaccard similarity is only 0.472 — meaning the non-tied sets share less than half their members. 87 instances become non-tied in free-form (were tied in constrained), and 76 go the other way. This is a **substantial reshuffling**: ~38% of the union consists of instances that are non-tied in only one condition.

### 2.2 New Non-Tied Instances (Free-form Non-Tied, Constrained Tied)

N = 87 instances that gain LP discrimination under free-form.

| Characteristic | New Non-Tied (N=87) | Lost Non-Tied (N=76) | Baseline (N=551) |
|:---|---:|---:|---:|
| Mean gold relations | 1.7 | 1.3 | 1.8 |
| Mean gold entities | 2.8 | 2.6 | 3.1 |
| % with relations | 71.3% | 64.5% | 72.1% |
| Mean LP range (constrained) | 0.0321 | 0.1108 | 0.0623 |
| Mean LP range (free-form) | **0.0978** | 0.0314 | 0.0599 |
| Mean greedy NER F1 | 0.631 | 0.607 | 0.618 |
| Mean greedy RE F1 | 0.417 | 0.406 | — |
| Mean output tokens (constrained) | 186 | 164 | — |
| Mean output tokens (free-form) | 168 | 175 | — |
| Mean input text length | 146 | 137 | — |

**Interpretation**: New non-tied instances had very tight LP ranges under constrained decoding (0.0321, barely above the 0.05 threshold — actually below it, hence tied). Free-form triples their LP range to 0.0978. These tend to be moderate-complexity instances (1.7 rels, 2.8 ents) that are slightly longer than lost instances. The constrained format apparently homogenized their outputs, but free-form allows enough structural variation to create LP discrimination.

### 2.3 Lost Non-Tied Instances (Constrained Non-Tied, Free-form Tied)

N = 76 instances that lose LP discrimination under free-form.

These instances had the **highest** LP ranges in constrained mode (0.1108, nearly 2× baseline). In free-form, their LP range collapses to 0.0314. They tend to be simpler instances (1.3 rels, 2.6 ents, shorter text). The constrained format's structural rigidity apparently amplified small differences in these simple cases (e.g., missing/adding a single entity changes token count significantly), but free-form's flexibility allows the model to express the same content with different phrasings that have similar logprobs.

### 2.4 LP Range Cross-Condition Correlation

| Metric | Value |
|:---|---:|
| Spearman ρ (per-instance LP range) | 0.488 |
| p-value | 2.95e-34 |
| Mean LP range (constrained) | 0.0623 |
| Mean LP range (free-form) | 0.0599 |

**Interpretation**: Moderate positive correlation (ρ = 0.488) — instances with high LP range in one condition tend to have high range in the other, but with substantial scatter. The 0.488 is consistent with roughly 24% shared variance in LP range, meaning ~76% of the variance in which instances are "discriminable" is condition-specific. This confirms the reshuffling finding: the two decoding modes expose different aspects of instance difficulty.

---

## Summary: Key Takeaways

1. **The RE LP selection flip is universal across all 7 SciERC relation types**, with the largest flips on semantically subtle types (PART-OF +6.52pp, HYPONYM-OF +4.45pp). No single type drives the effect.

2. **Free-form decoding selectively reallocates LP variance**: it amplifies variance on RE-difficult instances (ratio 1.06, p < 0.0001) and dampens it on RE-easy instances (ratio 0.86). This gives LP selection more discriminative power exactly where RE quality varies most.

3. **The constrained format creates a systematic LP selection bias for RE**: in constrained mode, LP selection is wrong more often than right (14.9% vs 9.1%), producing a net -23 instances. Free-form equalizes this to 45:45, flipping the aggregate gap from -0.68pp to +1.69pp. The mechanism is likely that constrained decoding rewards verbatim entity token copying (boosting logprobs) while penalizing relation-type experimentation.

4. **Despite near-identical tied fractions (59.7% vs 57.7%), free-form fundamentally reshuffles which instances are discriminable** (Jaccard = 0.472). 87 instances gain LP discrimination (LP range triples from 0.032 to 0.098) while 76 lose it (range collapses from 0.111 to 0.031). Only 24% of LP range variance is shared between conditions.

5. **The flip instances are relation-dense** (3.3 gold rels, 2× baseline) with suppressed LP variance in constrained mode. Free-form relaxes structural constraints, allowing these complex instances to produce more varied — and more informatively varied — outputs, enabling LP to select samples with better entity boundaries that cascade into better RE.
