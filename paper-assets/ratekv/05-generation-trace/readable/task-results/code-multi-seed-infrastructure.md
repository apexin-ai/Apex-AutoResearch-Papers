# code multi seed infrastructure

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi_seed_infrastructure_20260516T032334_result.json`
- **Structured JSON:** [`212a94cb14a10664b613.json`](../../sessions/21/212a94cb14a10664b613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Everything verified. Here's the summary:

---

**Script created:** `/root/ratekv/run_multi_seed_ppl.py`

**What it does:** For each seed (42, 123, 456), re-profiles all attention heads with a different WikiText-103 calibration subset, solves constrained MCKP, and evaluates WikiText-2 PPL. Reports mean±std and allocation agreement across seeds.

**4 models supported:**
| Model | Path | max_2bit | Special handling |
|---|---|---|---|
| `llama` | `.../Meta-Llama-3___1-8B` | 2 | standard |
| `mistral` | `.../Mistral-7B-v0.3` | 2 | standard |
| `yi` | `.../Yi-1___5-9B` | 2 | standard |
| `gemma2` | `.../gemma-2-9b` | 8 | custom patch + BOS eval |

**Usage:**
```bash
python run_multi_seed_ppl.py --model llama --gpu 0
python run_multi_seed_ppl.py --model gemma2 --gpu 1
python run_multi_seed_ppl.py --model llama --dry-run  # verify only
```

**Key findings on profiling & seed:**
- Profiling **does** depend on calibration data. Different seeds → different calibration subsets → different per-head deltas → potentially different MCKP allocations.
- The script re-profiles from scratch per seed (same approach as existing `run_multi_seed.py` for Qwen).
- Baseline and uniform 4-bit PPL are evaluated once (seed-independent).

**Dry-run verified:** Seeds 42/123/456 produce distinct calibration subsets (0.8% token overlap), same seed is deterministic.

**Outputs:** `artifacts/{model}_multi_seed_ppl_results.json` with per-seed profiles saved as intermediate checkpoints.

---
