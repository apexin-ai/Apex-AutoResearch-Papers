# paper d044 framing rewrite

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d044_framing_rewrite_20260516T093329_result.json`
- **Structured JSON:** [`0d772aa548b69ff07f43.json`](../../sessions/0d/0d772aa548b69ff07f43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete:

1. **Title**: "Drive" → "Shape" in `main.tex:16`
2. **Abstract**: Fully rewritten (~195 words). Leads with quartile Δ=-5.3pp and typical-batch 2.2pp; 31.2pp demoted to "under extreme-batch construction"; includes all required phrasings verbatim (cross-model, prompt robustness, MAVEN, decomposition, RE closed-set).
3. **Introduction**:
   - Finding (1) now leads with typical magnitudes (quartile -5.3pp, typical 2.2pp) before extreme -49pp count effect
   - Finding (3) changed from "robust across ... prompt designs" to "directionally consistent across prompt designs, with attenuated magnitude under improved prompts"
   - Contribution #4 rewritten with oracle routing +29.8pp, inconclusive grouping +1.4pp p≈0.19, merge amplification
   - RQ1 doesn't use "Drive" (already phrased differently), so no change needed there
4. **Prompt robustness (S12)**: `main.tex:245` updated from "robust to prompt design" to "directionally consistent across prompt designs, with attenuated magnitude"

---
