# W3 Related Work Gap Analysis
**Date:** 2026-05-15
**Purpose:** Address reviewer W3 — significant missing related work

---

## 1. R1-RE (arXiv 2507.04642) — GRPO for Sentence-Level RE

**Status:** direct-competitor

**Key facts:**
- First RLVR (GRPO + verifiable reward) framework for RE
- Sentence-level RE on SemEval-2010 Task 8 and MDKG
- Results: 91.8% in-domain, ~66-70% OOD accuracy (matches GPT-4o)
- Reward: format reward (+1/-3) + metric reward (+2/-1.5); triplet F1-based
- **No catastrophic forgetting** — GRPO training actually improved MATH-500/IFEval/GPQA
- No evidence generation component

**Why GRPO works for sentence-level but fails for document-level:**
Sentence-level RE is essentially binary classification (1 triple per sample), so reward variance within each GRPO group is naturally sufficient. Document-level RE has dozens of triples per sample; F1 as reward produces homogeneous scores across rollouts (frac_zero_std→0.8). This is exactly the zero-gradient problem DAPO's Dynamic Sampling and Dr. GRPO's difficulty bias analysis describe.

**How to cite:**
Position R1-RE as complementary evidence — it proves RLVR for RE is viable in principle, while FREIGE reveals that document-level RE requires CED to maintain reward variance. The sentence-vs-document complexity gap explains why GRPO alone succeeds at sentence level but needs CED at document level.

---

## 2. DAPO (arXiv 2503.14476) & Dr. GRPO (arXiv 2503.20783) — GRPO Failure Modes

**Status:** method-component (already in lit map, now enriched)

### DAPO — Entropy Collapse
- **Root cause:** Clipping asymmetry — prob 0.01 token can only grow to 0.012, prob 0.9 token to 1.08. Low-probability tokens can't explore.
- **Dynamic Sampling:** Filters prompts with accuracy=0 or 1 (zero gradient). This is functionally identical to our frac_zero_std observation.
- **Connection to CED:** DAPO filters zero-gradient prompts after the fact; CED prevents them from occurring by adding an orthogonal reward dimension.

### Dr. GRPO — Normalization Bias
- **Difficulty bias:** std(r) normalization gives disproportionate weight to low-variance groups (all-correct/all-wrong).
- **When std→0:** Advantage term explodes/undefined → numerically unstable gradients.
- **Connection to CED:** Our frac_zero_std→0.8 with extraction-only reward is the extreme version of Dr. GRPO's difficulty bias. CED maintains reward_std>0 by design.

**How to cite:**
Use DAPO and Dr. GRPO as independent theoretical validation of CED's stabilization mechanism. Frame it as: "DAPO and Dr. GRPO identify the failure modes; CED addresses them from the reward design level rather than algorithmic patches."

---

## 3. "A Minimalist Approach to LLM Reasoning" (arXiv 2504.11343)

**Status:** method-component (already in lit map, now enriched)

**Key insight:** RAFT (simple rejection sampling) matches GRPO/PPO on math reasoning. GRPO's advantage mainly comes from discarding all-wrong prompts, not reward normalization.

**Connection to FREIGE:**
- Directly supports RSFT choice over GRPO for DocRE
- GRPO's negative-sample mixing doesn't help (and may hurt for structured output)
- RSFT's offline nature avoids catastrophic forgetting on structured generation

**How to cite:**
"Xiao et al. (2025) show that rejection sampling is competitive with GRPO for math reasoning; we extend this finding to structured IE, where RSFT's stability advantage is even more pronounced due to the higher complexity of document-level output."

---

## 4. LLM-based DocRE Methods — Performance Landscape

### F1 Score Summary (Re-DocRED test, LLaMA3-8B backbone unless noted)

| Method | Re-DocRED Test F1 | DocRED Test F1 | Evidence? | Paradigm |
|--------|-------------------|----------------|-----------|----------|
| **FREIGE (ours)** | — | — | **Yes** | RSFT + CED |
| RelPrior | 54.80 | 48.34 | No | Inference filtering |
| AutoRE | 51.97 | 45.96 | No | QLoRA SFT (RHF) |
| LMRC | 74.63 | 60.52 | No | BERT filter + LLM (hybrid) |
| Ru-LLM | >AutoRE (paywall) | >AutoRE (paywall) | No | Rule prompt + CoT verify |
| GLiDRE | 77.83 (encoder) | — | No | Dual-encoder (not LLM) |

### Key observations:
1. **No existing LLM-based DocRE method generates evidence.** FREIGE is unique in jointly extracting relations + evidence.
2. Among pure LLM generative methods, RelPrior (54.80) is current SOTA on Re-DocRED.
3. LMRC (74.63) and GLiDRE (77.83) achieve much higher F1 but aren't comparable — LMRC uses BERT classifier, GLiDRE is encoder-based.
4. All methods use SFT/QLoRA training. FREIGE is the first to apply RL-based training (RSFT) to LLM DocRE.

### Per-method notes:

**RelPrior** — Inference-time two-stage filtering (binary relation prior → predefined relation matching). Orthogonal to FREIGE: RelPrior improves inference, FREIGE improves training. Could potentially combine.

**AutoRE** — RHF paradigm (Relation→Head→Facts) with QLoRA. Our SFT baseline is similar; RSFT adds reward-guided sample selection on top.

**LMRC** — Not directly comparable (hybrid BERT+LLM). Shows that reducing candidate space via external classifier helps LLMs, but requires task-specific classifier training.

**Ru-LLM** — Most conceptually related to CED: both inject external knowledge constraints. But Ru-LLM uses dataset-level frequent patterns at inference time (MCTS+CoT), while CED uses instance-level evidence faithfulness at training time.

**GLiDRE** — Different paradigm entirely (encoder-based). Shows DocRE field is still actively innovating across paradigms.

---

## 5. Contrastive Reward Methods

### arXiv 2403.07708 — Contrastive Rewards for RLHF
- Two-step: offline sampling baseline → contrastive penalty in PPO
- Domain-agnostic, penalizes reward uncertainty

### EMNLP 2024 — Contrastive Learning for RM
- Trains reward model with contrastive loss for better discrimination
- Leads to more stable PPO training

**CED vs. these methods:**

| Aspect | Contrastive Rewards (2403.07708) | EMNLP 2024 Contrastive RM | CED |
|--------|----------------------------------|---------------------------|-----|
| What's contrastive | RM output vs. baseline | RM training pairs | Evidence vs. corrupted evidence |
| Where applied | PPO | PPO | GRPO / RSFT |
| Domain | General RLHF | General RLHF | Task-specific (DocRE) |
| Mechanism | Post-hoc penalty | Training-time RM | Reward function design |
| Stabilization | Variance reduction | Better RM discrimination | Reward diversity + faithfulness |

**How to cite:**
"Prior contrastive reward approaches (Shen et al., 2024; EMNLP 2024) operate at the reward model or optimization level. CED introduces contrastive structure directly into the task reward function — evidence vs. corrupted evidence — providing both training stabilization (via reward diversity) and task-relevant faithfulness signal."

---

## 6. Recommended Citation Strategy for Paper

### In Related Work section:

**RL for IE (new subsection):**
- R1-RE as key concurrent work: "R1-RE demonstrates GRPO success for sentence-level RE; our work reveals document-level RE requires additional reward design (CED) due to reward homogenization."
- REAR, MORE-R1 as broader RL-for-IE trend

**GRPO Instability Analysis (expand existing):**
- DAPO: "identifies entropy collapse from clipping asymmetry and zero-gradient prompts"
- Dr. GRPO: "identifies difficulty bias from std normalization when reward variance→0"
- Frame: "These independently-discovered failure modes precisely describe what we observe with extraction-only reward (frac_zero_std→0.8)"

**LLM-based DocRE (new subsection):**
- RelPrior, AutoRE, LMRC, Ru-LLM as baselines
- Note: "None generate evidence; FREIGE is unique in evidence-grounded extraction"
- GLiDRE as different paradigm (encoder-based)

**RSFT Theory (expand existing):**
- Xiao et al. 2025: "RAFT competitive with GRPO in math; we extend to structured IE where RSFT's stability advantage is more critical"

**Contrastive Rewards (expand existing):**
- Distinguish CED from prior contrastive approaches
- CED is task-specific reward design, not generic penalty/training trick
