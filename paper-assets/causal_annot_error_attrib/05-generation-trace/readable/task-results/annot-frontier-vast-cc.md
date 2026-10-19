# annot frontier vast cc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_annot_frontier_vast_cc_20260521T095547_result.json`
- **Structured JSON:** [`49b414271f7bfc683e60.json`](../../sessions/49/49b414271f7bfc683e60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I've prepared everything except the live API calls — the provided API key fails auth on every endpoint I can reach. Reporting status:

## Status: BLOCKED on auth (HTTP 401)

The provided key `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8` is rejected by every endpoint I tried:

| Endpoint | Result |
|---|---|
| `https://openrouter.ai/api/v1/chat/completions` | 401 "Missing Authentication header" |
| `https://gpu.aet.cit.tum.de/api/v1/chat/completions` (Open WebUI, TUM-AET) | 401 Unauthorized |
| `https://gpu.aet.cit.tum.de/openai/v1/...`, `/ollama/v1/...` | 401 Unauthorized |
| `http://47.94.22.126/v1/...` (previous project endpoint) | timeout/unreachable |

OpenRouter requires `sk-or-v1-*` keys (not `tum_*`). The TUM gateway recognises the request format but rejects this bearer token — likely expired or revoked. I stopped before running 6000 API calls that would all 401.

## What's ready (so this can resume once auth is fixed)

```
artifacts/plan011_frontier_annotations/
├── STATUS.md                              # this report, with resume instructions
├── data/
│   ├── vast/test.jsonl                    # 1000 dedup VAST test (HF blocked, used GitHub CSV)
│   └── civil_comments/test.jsonl          # 1000 balanced 500/500 from HF google/civil_comments
└── scripts/
    ├── prepare_data.py                    # reproducible data prep (already run)
    ├── annotate_frontier.py               # zero-shot pipeline, streaming JSONL + resume
    │                                      # supports OPENROUTER_API_BASE/KEY env override
    │                                      # 30s × 5 retries on 402/429/5xx
    │                                      # `--smoke` for 1-call auth check
    │                                      # aborts after 20 consecutive failures
    └── compute_results.py                 # CMs + macro F1 + bias + magnitude-ASV across
                                           # 7 topologies, imports plan_006 K-general pipeline
```

VAST data: HF `QCRI/VAST` is gone — fell back to `emilyallaway/zero-shot-stance` raw CSV (3006 rows, 2928 after dedup, sampled 1000 with seed 42). Labels mapped to canonical `["Con", "Pro", "Neutral"]` matching plan_006 conventions.

## What I need from you

Either a working key against `gpu.aet.cit.tum.de/api/v1` (or whichever Open WebUI URL is current), **or** a real OpenRouter `sk-or-v1-*` key. Once auth works:

```bash
cd artifacts/plan011_frontier_annotations
OPENROUTER_API_BASE=&lt;URL> OPENROUTER_API_KEY=[REDACTED] /tmp/hf_venv/bin/python scripts/annotate_frontier.py --smoke
OPENROUTER_API_BASE=&lt;URL> OPENROUTER_API_KEY=[REDACTED] /tmp/hf_venv/bin/python scripts/annotate_frontier.py
/tmp/hf_venv/bin/python scripts/compute_results.py
```

Then I'll register the artifact.

---
