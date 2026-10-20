# audit bgem3 multiseed

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bgem3-multiseed_20260516T042333_result.json`
- **Structured JSON:** [`1b03c057161df610efa5.json`](../../sessions/1b/1b03c057161df610efa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计信息收集完毕。以下是完整报告：

---

## BGE-M3 Multiseed Audit Report

### Seed 42:
```
Log source: /checkpoints_ablation_bgem3/train_history.json (10 epochs)
Best val_macro_f1: 0.9578594622558281 (epoch 5)
Independent verification: artifacts/d073/probe_bge_m3/results.json
  d073 swe_indomain_test.macro_f1 = 0.9413404301928796
  d073 swe_indomain_test.f1_stagnation = 0.9147442326980942
  d073 swe_indomain_test.f1_progress = 0.9679366276876651
  d073 best_val_f1 = 0.9578594622558281 (exact match with train history)
Registry metrics: macro_f1=0.9413, f1_stag=0.9147, f1_prog=0.9679
Match: ✅ VERIFIED (full-precision match via d073 independent evaluation)
```

### Seed 123:
```
Log source: /checkpoints_ablation_bgem3_s123/train_history.json (7 epochs, early stop)
Best val_macro_f1: 0.9178535065951313 (epoch 2)
Val→Test gap: -7.0pp (0.9179 → 0.8474) — large but plausible with different instance splits
Registry metrics: macro_f1=0.8474, f1_stag=0.8173, f1_prog=0.8775
Independent verification: ❌ NONE — metrics exist ONLY in bgem3_multiseed_test_results.json
Match: ⚠️ UNVERIFIABLE — no independent source confirms these test metrics
```

### Seed 456:
```
Log source: /checkpoints_ablation_bgem3_s456/train_history.json (10 epochs)
Best val_macro_f1: 0.9479577246180328 (epoch 5)
Val→Test gap: -1.2pp (0.9480 → 0.9364) — plausible
Registry metrics: macro_f1=0.9364, f1_stag=0.9183, f1_prog=0.9545
Independent verification: ❌ NONE — metrics exist ONLY in bgem3_multiseed_test_results.json
Match: ⚠️ UNVERIFIABLE — no independent source confirms these test metrics
```

### Checkpoint Integrity:
```
Seed 42:  ✅ best_model.pt (5,521,660B, mtime 2026-05-14 21:42)
Seed 123: ✅ best_model.pt (5,521,660B, mtime 2026-05-15 05:58)
Seed 456: ✅ best_model.pt (5,521,660B, mtime 2026-05-15 06:01)
Results JSON: mtime 2026-05-15 06:15 (14 min after last training — consistent)
File sizes identical: EXPECTED (same architecture, weights dominate size)
```

### Split Integrity:
```
train_indices: ✅ DIFFERENT across all 3 seeds (verified first 300 bytes)
test_indices:  ✅ DIFFERENT across all 3 seeds (verified first 200 chars)
Split structure: 3 arrays only (no keep_indices → min_confidence=0 training)
```

### Test Size Verification:
```
Registry claims: s42=1824, s123=2216, s456=2343
Verification: ❌ CANNOT COUNT — python3 blocked in read-only mode
Note: Full test split is ~15% of 54,809 = ~8000+ windows
      Registry "test_size" likely refers to conf>=2 subset evaluation
```

### Red Flags:
1. **No evaluation script** generates or references `bgem3_multiseed_test_results.json` — was created ad-hoc
2. **Seed 123 has unusually large val→test gap** (7pp) compared to seeds 42/456 (~1-2pp)
3. **Seeds 123/456 have zero independent corroboration** — their metrics exist in one file only

### Mitigating Evidence:
1. Seed 42 is fully confirmed by d073 evaluation (different file, different date)
2. Training histories show realistic patterns (different convergence, early stopping)
3. Timestamps are sequential and internally consistent
4. Splits are genuinely different (not just relabeled copies)

---

## Overall: PARTIAL PASS

- **Seed 42: PASS** — independently verified
- **Seeds 123 & 456: INCONCLUSIVE** — structurally consistent with real training, but test metrics have no independent verification source

**Recommendation:** Re-run evaluation on seeds 123 and 456 using `eval_probe_only.py` to independently confirm test metrics. This requires `ssh_execute` access to the server.

---
