# Code Reusability Assessment

## Code Structure

### Core Pipeline (`src/`)

| Script | Function | Input → Output |
|--------|----------|----------------|
| `src/config.py` | Central config: paths, model params, layers, splits | Constants |
| `src/data_loader.py` | Load HarmThoughts from HF, group by trace, compute CP | HF dataset → trace dicts with `sentences`, `labels`, `commitment_point`, `step_labels` |
| `src/extract_hidden_states.py` | Forward pass → extract HS at sentence boundary positions | trace dicts + model → `.pt` files |
| `src/baselines/linear_probe.py` | MLP static probe (per-step classification) | HS features → trained probe |
| `src/crta/temporal_probe.py` | Temporal probe (sequence-level) | Windowed HS → trained probe |
| `src/eval/evaluate.py` | Evaluate probes (accuracy, F1, detection delay) | Probes + test data → metrics |
| `src/diagnostics/layer_sweep.py` | Per-layer LogReg sweep | All-layer HS → per-layer accuracy |
| `src/run_pipeline.py` | CLI entry point: `--step extract/train/eval/all` | Orchestrates above |

### Key Experiment Scripts

| Script | Function | Relevance to Table 2 |
|--------|----------|---------------------|
| `run_bootstrap_10k.py` | **Main Table 2 script**: 4 models × 3 metrics, 10k bootstrap, Holm-Bonferroni | **Critical** — the canonical metric-bias pipeline |
| `src/experiments/exp_r14_a1_ba_layer.py` | BA-optimal layer selection + HS vs Text comparison | **High** — latest canonical layer sweep + comparison |
| `src/experiments/text_baseline.py` | Text embedding baseline (MiniLM) | **High** — text probe training/eval |
| `src/experiments/r1_8b_bootstrap_hs_text.py` | Single-model HS vs Text bootstrap | Medium — R1-8B specific version |
| `src/experiments/exp_r5_auroc_layer_sweep.py` | AUROC layer sweep across all models | Medium — layer selection |
| `src/experiments/exp_split_half_v2.py` | Split-half replication (internal validity) | Medium — robustness check |

### IAA / CP Annotation (`src/iaa/`)

| Script | Function |
|--------|----------|
| `src/iaa/sample_traces.py` | Sample traces for annotation (25 per model) |
| `src/iaa/prompt_template.py` | Generic LLM prompt for CP annotation |
| `src/iaa/annotate.py` | Multi-backend LLM annotation (Groq/Anthropic/Google) |
| `src/iaa/compute_kappa.py` | Inter-annotator agreement (Cohen's κ) |

## Data Format Specification

### Hidden States (`.pt` files)

```
artifacts/hidden_states/{trace_id}.pt  (R1-8B)
artifacts/hidden_states_ot7b/{trace_id}.pt  (OT-7B)
artifacts/hidden_states_r1_32b/{trace_id}.pt  (R1-32B)
artifacts/hidden_states_qwq_32b/{trace_id}.pt  (QwQ-32B)
```

Format: `torch.save(dict)` with keys:
```python
{
    "hidden_states": Tensor[T, L, D],  # T=num_sentences, L=num_layers, D=hidden_dim
    "trace_id": str,                    # UUID-like hash
    "num_sentences": int,
    "commitment_point": int or None,    # step index where CP occurs
    "step_labels": List[int] or None,   # 0=pre-CP, 1=post-CP
    "query": str,                       # (OT-7B only, optional)
}
```

Model-specific dimensions:
| Model | hidden_dim (D) | num_layers stored (L) | layer_offset | Total layers |
|-------|------------|----------------------|-------------|-------------|
| R1-8B | 4096 | 13 (layers 12–24) | 12 | 25 |
| OT-7B | 3584 | 28 (all layers) | 1 | 28 |
| R1-32B | 5120 | 64 (all layers) | 0 | 64 |
| QwQ-32B | 5120 | 64 (all layers) | 0 | 64 |

Trace counts: R1-8B=268, OT-7B=228, R1-32B=100, QwQ-32B=95

### Text Embeddings (`.pkl` files)

```python
# dict[trace_id] → numpy.ndarray(T, 384)  # MiniLM L6 v2 output
# e.g. artifacts/r12_5seed_hb/r1_8b_text_emb.pkl
```

### CP Labels

From HarmThoughts: `llm_annotation` field with safety labels {RA, AL, CC, ED, IA}.
CP = index after last safety label in sequence.
For new dataset: either ground-truth labels or LLM annotation via `src/iaa/annotate.py`.

### Trace Metadata (in HarmThoughts)

```python
{
    "sentence_id": "trace_uuid-step_number",  # 1-indexed
    "model_name": "r1-8b" | "ot-7b" | "r1-32b" | "QwQ",
    "sentence": str,
    "llm_annotation": str,  # label code
    "query": str,
    "final_judgment": float,  # 1.0 = jailbreak
}
```

## Reusability Matrix

| Component | Script | Reusable? | Modifications needed |
|-----------|--------|-----------|---------------------|
| Config | `src/config.py` | ✓ partial | Add new model paths, layers, hidden_dim; new dataset name |
| Data loading | `src/data_loader.py` | ✗ | **Complete rewrite** — field names, trace_id parsing, safety labels, CP logic are all HarmThoughts-specific |
| HS extraction | `src/extract_hidden_states.py` | ✓ | Change model path + layer config; `find_sentence_boundaries()` and `extract_trace_hidden_states()` are generic |
| Text embedding | inline in `run_bootstrap_10k.py` | ✓ | Zero modifications — `SentenceTransformer.encode()` is dataset-agnostic |
| Window features | `build_window_features()` | ✓ | Zero modifications — pure numpy sliding window |
| Layer sweep | `exp_r5_auroc_layer_sweep.py` | ✓ partial | Add new `MODEL_CONFIGS` entry; core logic generic |
| Bootstrap test | `paired_bootstrap()` in `run_bootstrap_10k.py` | ✓ | Zero modifications — takes metric arrays, returns p-values |
| Holm-Bonferroni | `holm_bonferroni()` | ✓ | Zero modifications |
| Probe training | `train_probe()` in `run_bootstrap_10k.py` | ✓ | Zero modifications — LogReg on feature arrays |
| Full pipeline | `run_bootstrap_10k.py` | ✓ partial | Add new model entry to `MODEL_CONFIGS`; data loading interface change |
| CP annotation | `src/iaa/annotate.py` | ✓ | Prompt template is generic; need to convert new dataset to sampled_traces format |
| Split-half | `exp_split_half_v2.py` | ✓ partial | Config changes only |

### Summary

- **Directly reusable** (zero changes): Text embedding, window features, bootstrap test, Holm-Bonferroni, probe training = **core statistical pipeline**
- **Config-only changes**: Layer sweep, split-half, HS extraction = model-specific params
- **Must rewrite**: `data_loader.py` = the only deeply HarmThoughts-coupled component

**Overall: ~80% code reuse. The only major work is writing a new `data_loader.py` adapter for the new dataset.**

## Execution Plan: Second Dataset Sprint

Assumptions:
- Using R1-8B (same model, already cached on server)
- New dataset has prompts but NOT pre-existing reasoning traces
- No ground-truth CP labels → use LLM annotation
- RTX 6000 (24GB VRAM) available

| Step | Task | Time (wall) | GPU? | Dependencies | Details |
|------|------|-------------|------|-------------|---------|
| 0 | Data loader adapter | 1–2h | No | Dataset format spec | Write new `data_loader_v2.py` matching HS .pt format |
| 1 | Download prompt dataset | 10–30min | No | Internet | `datasets.load_dataset()` or manual download |
| 2 | Trace generation (R1-8B inference) | 4–8h | **Yes** | Step 1 | Generate reasoning traces from prompts. ~1–2 min/trace × ~200 traces. Need to run model with `<think>` tag parsing |
| 3 | Hidden state extraction | 2–4h | **Yes** | Step 2 | Re-run model, save HS at sentence boundaries. Can combine with Step 2 into single pass |
| 4 | CP annotation (LLM-based) | 1–2h | No | Step 2 | Use `src/iaa/annotate.py` with Groq/Anthropic. ~200 traces × 3 backends. API cost ~$2–5 |
| 5 | Text embedding (MiniLM) | 5–10min | No | Step 2 | `SentenceTransformer.encode()` on all sentences. CPU-only |
| 6 | Layer sweep (BA-optimal layer) | 30–60min | No | Steps 3,4 | Run `exp_r14_a1_ba_layer.py` with new config to find best layer |
| 7 | Bootstrap HS vs Text (10k) | 1–2h | No | Steps 3,4,5,6 | Run `run_bootstrap_10k.py` with new model entry |
| 8 | Results analysis + table | 30min | No | Step 7 | Format for Table 2, compare with HarmThoughts pattern |
| **Total** | | **10–18h** | **6–12h GPU** | | |

### Optimized Pipeline (Steps 2+3 merged)

Steps 2 and 3 can be a single forward pass: generate trace + extract HS simultaneously. This cuts GPU time to **4–8h total**.

| Phase | Steps | Wall clock | Parallelizable? |
|-------|-------|-----------|-----------------|
| A: Prep | 0, 1 | 2h | Yes (independent) |
| B: GPU | 2+3 (merged) | 4–8h | No (sequential, GPU-bound) |
| C: Annotation | 4 | 1–2h | Yes (with Phase B if traces from Phase A are available) |
| D: Analysis | 5, 6, 7, 8 | 2–4h | Mostly sequential |
| **Critical path** | A → B → D (C parallel with B) | **8–14h** | |

## Risk Assessment

### High Risk

1. **No existing traces for new dataset** — If the dataset only has prompts (no pre-generated reasoning), we must run R1-8B inference to generate traces. This is the most expensive step (4–8h GPU). If the dataset already has reasoning traces, this drops to 0.
   - *Mitigation*: Choose a dataset that already has CoT/reasoning traces (e.g., from an existing reasoning benchmark).

2. **CP definition may not transfer** — HarmThoughts' CP is defined by safety labels (RA/AL/CC/ED/IA). A new dataset may have different transition semantics.
   - *Mitigation*: Use LLM annotation (src/iaa/) which uses a generic "commitment to harmful output" prompt. Verify with IAA κ before proceeding.

3. **Metric-bias pattern may not replicate** — The HS > Text advantage may be HarmThoughts-specific (e.g., driven by its particular prompt distribution or annotation quality).
   - *Mitigation*: This IS the research question. Either outcome (replicate/fail) is informative.

### Medium Risk

4. **Dataset size mismatch** — HarmThoughts has 209 jailbreak traces (R1-8B). If new dataset is much smaller (<50), bootstrap tests lose power.
   - *Mitigation*: Target ≥100 traces. Check power analysis (`src/experiments/exp_power_analysis.py`).

5. **Layer selection instability** — BA-optimal layer may differ from HarmThoughts' layer 14. Need full layer sweep before bootstrap.
   - *Mitigation*: Already handled by `exp_r14_a1_ba_layer.py` pipeline.

6. **AutoDL disk space** — HS extraction for 200 traces × 25 layers × 4096 dim ≈ 3GB. Root partition is 30GB.
   - *Mitigation*: Store in `/root/autodl-tmp/`.

### Low Risk

7. **Model already cached** — R1-8B is at `/root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Llama-8B`. No download needed.

8. **Dependencies installed** — PyTorch, transformers, sentence-transformers, scikit-learn all present in conda base env.
