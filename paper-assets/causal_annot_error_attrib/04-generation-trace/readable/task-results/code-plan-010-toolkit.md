# code plan 010 toolkit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_010_toolkit_20260520T232412_result.json`
- **Structured JSON:** [`edca30072d919fc0cd43.json`](../../sessions/ed/edca30072d919fc0cd43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three verification steps pass:

1. **Import** — works
2. **35/35 pytest tests** — all pass (14s)
3. **Worked example** — runs correctly, shows confounding bias of +10.2% with symmetric_high C, ASV at δ=0.967, recommends PPI++ with gold / DSL without

Package structure created:

```
annot_sensitivity/
├── __init__.py          # Public API: compute_bias, compute_asv, recommend_correction, ...
├── utils.py             # softmax_sample, misclassify, make_dummies, ols, ols_with_se
├── confusion.py         # validate, random, interpolate, predefined matrices
├── dgp.py               # 7 topology DGPs with DEFAULT_PARAMS
├── bias.py              # compute_bias via precomputed plim (2M samples, cached)
├── asv.py               # compute_asv with magnitude/significance/sign_flip thresholds
├── correction.py        # 5 correction methods + recommend_correction
├── examples/
│   └── confounding_k3.py   # Full workflow demo
└── tests/
    ├── __init__.py
    └── test_core.py     # 35 tests across all modules
```

---
