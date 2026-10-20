# CompressLink MVP

Joint compression-restoration optimization for RAG KV cache reuse.

## Components

| Module | Description |
|--------|-------------|
| `rope_utils.py` | RoPE apply/remove/restore utilities |
| `nope_attention.py` | NoPE KV storage + Q-only RoPE attention (MEPIC) |
| `boundary_recomp.py` | Fixed, query-independent boundary recomputation |
| `budget_manager.py` | Total budget → boundary (fixed) → CEGR (variable) |
| `raba.py` | Restoration-Aware Bit Allocation + DP/greedy allocators |
| `cegr.py` | Compression-Error-Guided Restoration (r_q × ε^β) |
| `query_probe.py` | ProphetKV-style query relevance probe |
| `pipeline.py` | End-to-end pipeline integrating all components |
| `eval_runner.py` | MVP evaluation on SQuAD/NQ |

## Configurations

| Config | Compression | Restoration | Description |
|--------|-------------|-------------|-------------|
| A | Standard KVTC | ProphetKV | Independent baseline |
| B | RABA | ProphetKV | Restoration-aware allocation |
| C | Standard KVTC | CEGR-MSE | Error-guided restoration |
| D | RABA | CEGR-MSE | Full joint optimization |
| E | None | Boundary only | Uncompressed MEPIC baseline |

## Usage

```bash
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Run evaluation
python -m compresslink.eval_runner --config configs/mvp_config.yaml --gpu cuda:0
```

## Budget Allocation (default 20%)

1. **Boundary** (~6%): Fixed. First block (32 tokens) of each chunk (512 tokens).
2. **CEGR/ProphetKV** (~14%): Variable, query-dependent. Non-boundary tokens only.
