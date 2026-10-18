# code mvp impl

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-impl_20260513T173830_result.json`
- **Structured JSON:** [`bc01e8ea32a03f88c460.json`](../../sessions/bc/bc01e8ea32a03f88c460.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All imports verified. Here's a summary of the 6 files written to `/root/ratekv/`:

| File | Lines | Purpose |
|------|-------|---------|
| `utils.py` | ~80 | Quantization (per-channel, per-token), attention with GQA, Expected Attention scoring, `repeat_kv` |
| `profiler.py` | ~160 | Captures hidden states via hooks, computes Q/K/V + rotary manually, profiles eviction (4 ratios) and quantization (3 bit-widths) distortion per KV head |
| `solver.py` | ~130 | Greedy MCKP downgrade solver with Pareto front filtering, uniform quantization baseline |
| `eval_ppl.py` | ~150 | Monkey-patches `LlamaAttention.forward` to apply per-head quant/eviction, evaluates WikiText-2 PPL |
| `visualize.py` | ~140 | Crossover scatter (evict vs quant distortion), PPL bar chart, allocation heatmap (32×8 grid) |
| `run_mvp.py` | ~180 | Orchestrates: profile → solve (3 budgets × 2 modes + uniform) → eval PPL → crossover analysis → visualize → save JSON |

Key design points:
- Matches transformers 4.57.6 API exactly (position_embeddings tuple, `apply_rotary_pos_emb`, eager attention path)
- Profiler uses `register_forward_pre_hook(with_kwargs=True)` to capture post-layernorm hidden states, then manually computes Q/K/V + rotary
- Eval uses factory-function closures for monkey-patching to avoid stale variable capture
- Eviction during eval uses two-pass approach: initial softmax for importance → mask → re-softmax
- Model loaded with `attn_implementation="eager"` and `torch.bfloat16`

---
