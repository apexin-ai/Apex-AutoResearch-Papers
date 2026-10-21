# paper expand method section

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_expand_method_section_20260528T174644_result.json`
- **Structured JSON:** [`3016a12c750fe0a85692.json`](../../sessions/30/3016a12c750fe0a85692.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Zero em-dashes. The `ing,` matches are all nouns (scoring, pruning, folding) in normal sentence structure, not dangling participial phrases.

Expansion complete. Summary of changes to `method.tex`:

**§3.2 Pruning Protocol** (was 1 paragraph, now 4 `\paragraph` blocks + 2 equations):
- Formal pruning operation definition with $\lfloor kN \rfloor$ notation
- **L2-norm scoring**: formula (Eq. 3), information density justification, spatial bias analysis
- **Random subsampling**: formula (Eq. 4), null hypothesis framing, spatial preservation property
- **Importance margin**: formal definition $\Delta(k)$, interpretation of positive/negative margins
- **Attention-based alternatives**: column-sum, cross-layer mean, attention rollout with intuitions; why we use L2/random instead
- **Retention ratio design space**: $k$ range rationale, cliff zone concept, per-architecture cliff locations

**§3.3 Compressibility Diagnostic** (was 1 equation + 1 paragraph, now 1 equation + spectrum equation + 4 `\paragraph` blocks):
- **CV spectrum** (Eq. 6): all 6 models ordered with connector-family grouping via `\underbrace`
- **CV as tolerance predictor**: high CV = dispensable tokens exist, low CV = uniform criticality; CV also predicts optimal strategy (L2 vs random)
- **Entropy comparison**: entropy clusters π0.5/X-VLA/OpenVLA (0.61--0.67) despite different pruning behaviors; "reading pattern" vs "writing pattern" distinction

---
