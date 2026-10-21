# research table2 seed audit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_table2_seed_audit_20260517T171934_result.json`
- **Structured JSON:** [`3b81f63a4336162b8d78.json`](../../sessions/3b/3b81f63a4336162b8d78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the complete audit:

## Table 2 (tab:main) Multi-Seed Audit

Paper caption says: *"MMLU for 30% KL reports 3-seed mean±std; 50% uniform PPL is 3-seed (11.92±0.07); all other entries use seed 42."*

| # | Sparsity | Method | Alloc | Seeds Done | Seeds Missing | Action Needed | Est. GPU Time |
|---|----------|--------|-------|------------|---------------|---------------|---------------|
| 1 | 0% | Dense | — | N/A (deterministic) | — | None | — |
| 2 | 30% | TEAL vanilla | global | 1 (s42), deterministic | — | None | — |
| 3 | 30% | KL global (Ours) | global | **3** (s42, s123, s456) | None | None | — |
| 4 | 30% | KL uniform | uniform | **3** (s42, s123, s456) | None | None | — |
| 5 | 50% | TEAL vanilla | global | 1 (s42), deterministic | — | None | — |
| 6 | 50% | KL global (Ours) | global | **3** (s42, s123, s456) | None* | See note below | ~1.5h |
| 7 | 50% | KL uniform | uniform | **3** (s42, s123, s456) | None | None | — |
| 8 | 50% | BCE (2700 steps) | per-token | **1** (s42) | s123, s456 | Train + Eval | ~5h |

### Detailed Seed Inventory

**Row 3 — 30% KL global** (3 seeds complete):
| Seed | Benchmark Dir | Checkpoint | PPL | MMLU |
|------|--------------|------------|-----|------|
| s42 | `bench_kl30_global` | `kl_sparsity30_s42_v3` | 8.977 | 25.27% |
| s123 | `kl_30pct_s123` | `kl_30pct_s123` | 8.975 | 38.07% |
| s456 | `kl30_s456_global` | `kl_30pct_s456` | 8.933 | 43.82% |
| | | **3-seed mean±std** | — | **35.7±9.5%** ✓ |

**Row 4 — 30% KL uniform** (3 seeds complete):
| Seed | Benchmark Dir | Checkpoint | PPL | MMLU |
|------|--------------|------------|-----|------|
| s42 | `bench_kl30_uniform` | `kl_sparsity30_s42_v3` | 8.816 | 40.61% |
| s123 | `kl30_s123_uniform` | `kl_30pct_s123` | 8.831 | 39.44% |
| s456 | `kl30_s456_uniform` | `kl_30pct_s456` | 8.795 | 41.98% |
| | | **3-seed mean±std** | — | **40.7±1.3%** ✓ |

**Row 6 — 50% KL global** (3 seeds exist, but consistency issue):
| Seed | Benchmark Dir | Checkpoint | PPL | MMLU |
|------|--------------|------------|-----|------|
| s42 | `bench_kl50_global` | `mvp_kl_norm_v2_s42` | 11.790 | 27.89% |
| s123 | `kl_50pct_s123_global` | **`kl_50pct_s123`** ⚠️ | 11.745 | 27.52% |
| s456 | `kl50_s456_global` | `mvp_kl_norm_v2_s456` | 11.806 | 27.94% |

⚠️ **s123 uses `kl_50pct_s123` checkpoint instead of `mvp_kl_norm_v2_s123`** (different training config from s42/s456). The `mvp_kl_norm_v2_s123` checkpoint exists but has not been benchmarked with global allocation. Re-eval needed for consistency (~1.5h).

**Row 7 — 50% KL uniform** (3 seeds complete, consistent checkpoints):
| Seed | Benchmark Dir | Checkpoint | PPL | MMLU |
|------|--------------|------------|-----|------|
| s42 | `bench_kl50_uniform` | `mvp_kl_norm_v2_s42` | 11.963 | 27.77% |
| s123 | `bench_kl50_uniform_s123` | `mvp_kl_norm_v2_s123` | 11.833 | 27.51% |
| s456 | `bench_kl50_uniform_s456` | `mvp_kl_norm_v2_s456` | 11.960 | 28.74% |
| | | **3-seed mean±std** | **11.92±0.07** ✓ | — |

**Row 8 — 50% BCE (2700 steps)** (1 seed only):
- s42: `bce_isocompute_v3_s42` checkpoint + benchmark exist
- s123: no checkpoint, no benchmark → **train (~46min) + eval (~1.5h) = ~2.3h**
- s456: no checkpoint, no benchmark → **train (~46min) + eval (~1.5h) = ~2.3h**

### Summary of Gaps

| Priority | Action | Est. GPU Time |
|----------|--------|---------------|
| 1. Row 6 s123 consistency | Re-eval `mvp_kl_norm_v2_s123` with global alloc | ~1.5h |
| 2. Row 8 BCE s123 | Train BCE 2700 steps + eval 5 tasks | ~2.3h |
| 3. Row 8 BCE s456 | Train BCE 2700 steps + eval 5 tasks | ~2.3h |
| **Total** | | **~6.1h** |

Rows 1-5 and 7 are fully covered. The only actionable gaps are the 50% KL global s123 checkpoint mismatch and the missing BCE multi-seed runs.

---
