# paper compounding curves integration

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compounding-curves-integration_20260516T015523_result.json`
- **Structured JSON:** [`8d3447301264c0bfb79f.json`](../../sessions/8d/8d3447301264c0bfb79f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Summary:

**Fixed and regenerated `fig_compounding_curves`**:
- Corrected Llama concentration from 0.85 → **0.57** (matching paper text)
- Updated colors: Qwen=orange-red `#D55E00`, Llama=blue `#0072B2`, Mistral=green `#009E73` (colorblind-safe palette)
- Full model names (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3)
- PDF+PNG saved to `docs/paper/figures/`

**experiments.tex** — Section 5.3 "Cross-Architecture Compounding" was already integrated with the correct `\label{fig:compounding_cross}` reference and matching caption data. No tex changes needed.

---
