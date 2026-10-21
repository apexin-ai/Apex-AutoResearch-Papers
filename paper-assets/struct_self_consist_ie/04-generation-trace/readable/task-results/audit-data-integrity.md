# audit data integrity

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data_integrity_20260523T102309_result.json`
- **Structured JSON:** [`00edb2447caab6c1ca66.json`](../../sessions/00/00edb2447caab6c1ca66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证完成。编写最终报告。

```
=== DATA INTEGRITY VERIFICATION ===

[2a] FewNERD entity construction +1.40±0.51pp
  Paper: +1.40±0.51pp (experiments_main.tex:107, "3-seed mean")
  Recomputed: +1.40±0.51pp (4-seed ddof=0: seeds 42,123,456,789)
  Per-seed: s42=+0.88, s123=+2.18, s456=+1.51, s789=+1.02pp
  Cross-check: exact match with cached multiseed_results.json
  Status: MATCH (numbers correct)
  ⚠ TEXT ISSUE: Paper says "3-seed mean" but value requires 4 seeds.
    3-seed (42,123,456) gives +1.52±0.53pp, not +1.40±0.51pp.
    Also uses population std (ddof=0); sample std (ddof=1) = ±0.59pp.

[2b] FewNERD LP 5-epoch +0.12±0.04pp
  Paper: +0.12±0.04pp (appendix.tex:2084, "2-seed, full test set micro-F1")
  Recomputed: +0.12±0.04pp (all 37,648 instances, corpus micro-F1, ddof=1)
    s42: +0.15pp, s123: +0.09pp → mean=+0.12pp, std(ddof=1)=0.04pp
  Status: MATCH
  ⚠ NOTE: Table caption says "gold-filtered, n=32,565" but LP Δ was computed
    on ALL instances (n=37,648) including gold-empty. Gold-filtered gives
    +0.21pp (different number). The appendix text "full test set micro-F1"
    clarifies, but table caption is misleading.

[2c] CoNLL degeneracy 61.7%
  Paper: 61.7% (experiments_main.tex:69, 3-seed mean)
  Definition: "constant-F1 degeneracy" = all N samples yield identical F1
    (NOT identical entity sets — method.tex:61)
  Recomputed: 61.7% (exp002 3-seed mean: s42=59.1%, s123=63.0%, s456=62.9%)
    Mean = (59.1+63.0+62.9)/3 = 61.67% → 61.7%
  Status: MATCH

[2d] AUROC 0.82
  Paper: 0.82 (abstract) / 0.816 (Table 1, CoNLL Qwen EM AUROC)
  NOTE: Task says "SciERC AUROC" but 0.82 is actually CoNLL (Qwen) EM.
  Recomputed: 0.8156 (CoNLL seed42, EM signal, binarized at median F1=1.0)
  Cross-check: exact match with unified_auroc.json (0.8156)
  Status: MATCH (0.8156 → 0.816 in table → 0.82 in abstract)

[3] Q4 Fisher exact test
  Report: OR=0.109, p<1e-300
  Recomputed: OR=0.1086, p=0.0 (scipy returns exact 0.0)
  Status: MATCH

=== SUMMARY ===
All 5 numerical claims verified ✓
Two text-level issues flagged:
  1. [2a] "3-seed mean" should be "4-seed mean" (affects reproducibility description)
  2. [2b] Table caption "gold-filtered" is misleading for LP Δ row (computed on all instances)
```

---
