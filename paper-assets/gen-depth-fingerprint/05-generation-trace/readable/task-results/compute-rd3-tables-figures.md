# compute rd3 tables figures

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_rd3-tables-figures_20260516T050158_result.json`
- **Structured JSON:** [`35870ea6994c0a8b3c76.json`](../../sessions/35/35870ea6994c0a8b3c76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Summary:

**Modified files:**
1. `results.tex` — W3 caveat added at L73; W2 Table 3 caption reworded at L138
2. `appendix_downstream.tex` — N2a bootstrap analysis paragraph added
3. `appendix_dataset_stats.tex` — M6 new file with per-generator × per-depth sample counts
4. `main.tex` — added `\input{appendix_dataset_stats}`
5. `fig1_differential_response.pdf` — M4 strip plot (downloaded from server)

**Task 1 (N3)**: Already done in prior commit — Table 1 binary F1 average = 0.723 ✓

**Task 2 (N2a)**: Bootstrap CI for size-matched vs depth 0–1: Δ=0.020, CI [0.019, 0.020], permutation p=0.25 (exact minimum with n=3), Cohen's d=34.8.

**Task 3 (M4)**: Strip plot shows 6 generators × 7 features; blue = drifting, red = stationary; black dash = mean. Saved as PDF on server (`/root/gen-depth-fingerprint/fig1_differential_response.pdf`) and locally.

**Task 4 (M6)**: Dataset stats table created. Attrition visible (e.g. Qwen3-8B: 995→755 from gen-0 to gen-4).

**Task 5 (W2)**: Caption now reads "…matches the multi-detector ensemble on binary F1 (0.723 vs. 0.724); the contribution is simplicity…rather than performance superiority."

**Task 6 (W3)**: Prompt-type caveat added referencing Appendix app:prompt-type.

---
