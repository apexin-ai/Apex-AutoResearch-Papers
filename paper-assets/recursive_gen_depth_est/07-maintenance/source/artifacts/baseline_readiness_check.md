# Baseline Readiness Check — gpu-6000pro-2
**Date**: 2026-05-19

## 1. 9-Cell Atlas Data

**Status: COMPLETE**

All 9 cells have depth_0–depth_3.jsonl on the server:

| Model | Strategy | Dir | Files |
|-------|----------|-----|-------|
| pythia | nucleus | `data/` (root) | depth_0–3.jsonl (5000 lines each) |
| pythia | temp09 | `data/pythia_temp09/` | depth_0–3.jsonl |
| pythia | topk50 | `data/pythia_topk50/` | depth_1–3.jsonl (depth_0 shared from nucleus) |
| olmo | nucleus | `data/olmo/` | depth_0–5.jsonl |
| olmo | temp09 | `data/olmo_temp09/` | depth_1–3.jsonl |
| olmo | topk50 | `data/olmo_topk50/` | depth_1–3.jsonl |
| gpt2xl | nucleus | `data/gpt2xl/` | depth_0–5.jsonl |
| gpt2xl | temp09 | `data/gpt2xl_temp09/` | depth_1–3.jsonl |
| gpt2xl | topk50 | `data/gpt2xl_topk50/` | depth_1–3.jsonl |

Note: temp09/topk50 variants share depth_0 from nucleus directory (depth_0 = human seed text, same across strategies).

## 2. Baseline Scripts & Results

### Min-K% Prob
- **Script**: `mink_prob_baseline.py` (project root) — PRESENT
- **Results**: `results/mink_prob_baseline/mink_prob_results.json` — **COMPLETE (9/9 cells)**
- **Status**: Already finished. No action needed.

### DetectGPT
- **Script on server**: `scripts/detection_baselines.py` (covers Fast-DetectGPT + Binoculars combined)
- **Standalone script on server**: NOT present
- **Results**: `results/detectgpt_baseline/detectgpt_results.json` — **8/9 cells (missing pythia_nucleus)**
- **Status**: Mostly done; pythia_nucleus cell needs re-run or standalone script deployment.

### Binoculars
- **Script on server**: `scripts/detection_baselines.py` includes Binoculars scoring, but no standalone binoculars script
- **Results on server**: **NONE** — no binoculars results found anywhere
- **Status**: Needs script deployment + full run.

## 3. Local Artifacts Available for Deployment

| Artifact | Local Path |
|----------|-----------|
| Min-K% | `artifacts/mink_prob_baseline.py` |
| DetectGPT | `artifacts/detectgpt_baseline.py` |
| Binoculars | `artifacts/binoculars_baseline/binoculars_ordinal_eval.py` |
| Binoculars (intermediate) | `artifacts/_project/intermediate/binoculars_ordinal_eval.py` |

All three standalone baseline scripts are available locally.

## 4. Disk Space

```
Filesystem  Size  Used  Avail  Use%
/dev/md0    250G  168G  83G    68%
```

**Sufficient** — baseline scripts require model loading (GPT-2 Large ~1.5GB, T5-large ~3GB, Pythia models ~1-3GB) but no large data writes. 83GB headroom is adequate.

## 5. Python Environment

Not explicitly verified in this check, but:
- Min-K% and DetectGPT already ran successfully on this server (results exist)
- Required packages (torch, transformers, sklearn, numpy) are pre-installed (conda env)
- Binoculars uses same dependencies (torch, transformers, sklearn)

## Summary

| Baseline | Data | Script | Results | Action Needed |
|----------|------|--------|---------|---------------|
| Min-K% | ✓ | ✓ | ✓ 9/9 | None — already complete |
| DetectGPT | ✓ | Partial | 8/9 | Deploy `detectgpt_baseline.py` for pythia_nucleus, or re-run `detection_baselines.py` for that cell |
| Binoculars | ✓ | Missing | 0/9 | Deploy `binoculars_ordinal_eval.py` from local artifacts + run |

**Required deployments:**
1. `artifacts/detectgpt_baseline.py` → server (if pythia_nucleus re-run needed)
2. `artifacts/binoculars_baseline/binoculars_ordinal_eval.py` → server (mandatory)
