# plan011 Frontier Annotations — Status

## Blocker
API key `tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8` returns **HTTP 401 "Missing
Authentication header" / "401 Unauthorized"** on every endpoint probed:

| Endpoint                                         | Result               |
|--------------------------------------------------|----------------------|
| `https://openrouter.ai/api/v1/chat/completions`  | 401 (Missing Auth)   |
| `https://gpu.aet.cit.tum.de/api/v1/chat/completions` | 401 Unauthorized |
| `https://gpu.aet.cit.tum.de/openai/v1/chat/completions` | 401            |
| `https://gpu.aet.cit.tum.de/ollama/v1/chat/completions` | 401            |
| `http://47.94.22.126/v1/chat/completions` (old)  | timeout / unreachable |

The TUM gateway (`gpu.aet.cit.tum.de` runs Open WebUI v0.9.4) recognises the
request format but rejects the bearer token. OpenRouter rejects the `tum_*`
prefix outright (real OR keys are `sk-or-v1-...`).

The key is either expired, malformed, or intended for a different gateway URL.

## What is ready
- `data/vast/test.jsonl` — 1000 deduped samples from VAST test (333 Con / 333 Pro / 333 Neutral roughly), each with `text`, `topic`, `label`, `label_name`.
- `data/civil_comments/test.jsonl` — 1000 samples balanced 500 toxic / 500 non-toxic from `google/civil_comments` test split.
- `scripts/prepare_data.py` — reproducible data prep (HF + GitHub fallback for VAST).
- `scripts/annotate_frontier.py` — annotation pipeline. Supports:
  - `--smoke` (1 API call to verify auth)
  - `--dataset {vast,civil_comments,all} --model {llama4,qwen3,deepseek,all}`
  - Streaming JSONL write + resume by `idx`
  - 30-s wait × 5 retries on 402/429/5xx
  - Aborts after 20 consecutive failures (avoids burning credit on auth errors)
- `scripts/compute_results.py` — confusion matrix + macro F1 + bias + magnitude-ASV
  across 7 topologies for K=2 / K=3. Imports the K-general pipeline from
  `plan_006_asv_empirical.py`. Flags zero-matrices (trace(C) < 0.01).

## To resume after auth is fixed
Set `OPENROUTER_API_BASE` and `OPENROUTER_API_KEY` env vars (or edit the
constants in `annotate_frontier.py`) and run:

```
cd artifacts/plan011_frontier_annotations
/tmp/hf_venv/bin/python scripts/annotate_frontier.py --smoke   # verify auth
/tmp/hf_venv/bin/python scripts/annotate_frontier.py           # all 6 configs
/tmp/hf_venv/bin/python scripts/compute_results.py             # ASV + bias
```

Then `register_artifact(name="plan011_frontier_annotation_results", ...)`.
