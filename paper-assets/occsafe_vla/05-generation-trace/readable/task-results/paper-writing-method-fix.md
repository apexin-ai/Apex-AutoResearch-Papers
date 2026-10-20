# paper writing method fix

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_fix_20260520T210126_result.json`
- **Structured JSON:** [`785bfb8936c6baa69e17.json`](../../sessions/78/785bfb8936c6baa69e17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The -ing matches are nouns ("pretraining", "training"), not banned participial phrase endings. All clean.

---

## Report

### 5 Corrections (code-verified via SSH)

| # | Location | Old (wrong) | New (correct) | Code source |
|---|----------|-------------|---------------|-------------|
| 1 | §3.2 L24: architecture | "lightweight two-layer MLP with 256 hidden units" | Convolutional decoder: Linear→256ch, reshape 16×16, two ConvTranspose2d (256→128→64, k4s2) + BN + GELU, 1×1 Conv output | `occ_head.py` L20-30 |
| 2 | §3.2 L28: focal alpha | α = 0.75 | α = 0.25 | `occ_head.py` L56 `FocalLoss(alpha=0.25)` |
| 3 | §3.2 L28: loss weight | λ = 0.1 (static) | λ\_occ = 0.01 with exponential decay τ=50K | `finetune.py` L92-93 |
| 4 | §3.3 L39: total loss | λ = 0.1 (static formula) | λ\_occ(t) = 0.01 · exp(-t/τ), τ=50K (formula updated with decay term) | `finetune.py` L92-93 |
| 5 | §3.3 L41: lr + GPU | "cosine decay" + "17h on A100" | fixed lr 5e-4 + ~13h on NVIDIA RTX PRO 6000 | `finetune.py` L100,102 (MultiStepLR milestone 100K, never triggers at 50K) |

### §3.4 OCC-CBF

- **Removed** from `method.tex` (entire subsection + intro paragraph reference)
- **Created** `discussion.tex` with OCC-CBF as future direction: covers (1) limitations of implicit safety, (2) OCC-CBF concept (learned barrier on encoder features), (3) distinction from AEGIS/OGM-CBF/DCBF (operates in learned feature space, no explicit geometry), (4) marked as future work

### Self-check

- No §3.4 in method.tex
- All 5 values match experiments.tex §4.4 exactly
- Zero em-dashes (—) or explanatory en-dashes (–)
- `discussion.tex` needs `\input{discussion}` added to `main.tex` (not done, since the task scope was method.tex rewrite + discussion.tex creation)

---
