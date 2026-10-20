# code update jsd figure 14b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update-jsd-figure-14b_20260518T084358_result.json`
- **Structured JSON:** [`a111ba2ec6041f13f7ed.json`](../../sessions/a1/a111ba2ec6041f13f7ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Summary:

**What changed:**
- Created reproducible script `scripts/plot_fig_jsd_decay.py` with all JSD data hardcoded
- Regenerated `docs/paper/figures/fig_jsd_decay.{pdf,png}` with Qwen2.5-14B added to the C4 band
- Updated figure caption in `discussion.tex` and appendix text in `appendix_extended.tex` from "7 models" to "8 models (1B--14B)"

**Figure now contains:**
- **C4 band (8 models, K\*=2):** Qwen-1.5B, Qwen-1.5B-cont, LLaMA-8B, Pythia-greedy, Pythia-nuc0.9, Pythia-T0.7, Pythia-T1.2, **Qwen-14B** (new)
- **Mistral-7B** (K\*=1, dashed purple)
- **arXiv Pythia** (K\*=3, green)
- **Retrain-chain** (K\*>=4, dotted red)

14B JSD values (0v1=0.1097, 1v2=0.0112, 2v3=0.0062, 3v4=0.0044, 4v5=0.0036) fall squarely within the existing C4 band, consistent with scale invariance of the K\*=2 pattern.

---
