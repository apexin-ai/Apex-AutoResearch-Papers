# ops submission precheck

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submission-precheck_20260516T202001_result.json`
- **Structured JSON:** [`2fd65c360d925d01f48e.json`](../../sessions/2f/2fd65c360d925d01f48e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed for the checklist. Let me compile the final report.

```
=== SUBMISSION CHECKLIST ===

[1] Citation Integrity
    Status: PASS
    Missing bib entries: none
    Unused bib entries: gemma2

[2] Figure/Table References
    Status: PASS
    Missing labels: none
    Unused labels: fig:baseline-ci, tab:5class-logo, tab:5class-perclass,
                   tab:feature-ablation, tab:lofo, tab:qlora
    (All unused labels are in appendix files — defined but only internally
     referenced via \ref within their own appendix sections or unreferenced
     standalone tables.)

[3] Data-Paper Consistency
    Status: PASS
    Checked: Table 1 per-gen F1, Baselines table
    
    Table 1 (8gen_logo_unfiltered.json → results.tex tab:logo-results):
      Binary F1: all 8 generators match (0.633–0.724) ✓
      3-class F1: all 8 generators match (0.682–0.806) ✓
      Pooled: 3-class 0.762, binary 0.694, CI [0.688, 0.700] ✓
    
    Baselines (8gen_logo_baselines.json → results.tex tab:baselines):
      Avg-LogProb: 0.683/0.641 ✓
      FastDetectGPT: 0.655/0.564 ✓
      Binoculars: 0.395/0.520 ✓
      LD-Score: 0.619/0.657 ✓
      4-det ensemble: 0.770/0.686 ✓
      4-det + surface: 0.787/0.699 ✓
    
    Mismatches: none

[4] Compilation & Page Count
    Status: FAIL
    Compilation: SUCCESS (no errors, no undefined references)
    Total pages: 17
    Main body (through Conclusion): ~9 pages (overflows onto page 9)
    Limitations starts: page 9 right column
    References: pages 10–12
    Appendix: pages 13–17
    
    EMNLP limit: 8 pages main body (excl. Limitations/Ethics/References/Appendix)
    OVER LIMIT by ~0.7 page — Discussion + Conclusion spill onto page 9.

=== SUMMARY: 3/4 PASS ===

Action needed: Cut ~0.7 page from main body (Discussion is the most compressible
section — "Paraphrastic chains", "Instruct tuning", and "Negative downstream
finding" paragraphs on pages 8–9 are candidates for trimming or moving to appendix).
```

---
