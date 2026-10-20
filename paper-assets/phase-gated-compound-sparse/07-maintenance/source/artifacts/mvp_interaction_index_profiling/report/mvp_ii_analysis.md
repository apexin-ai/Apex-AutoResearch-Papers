# MVP Interaction Index Profiling — Analysis Report

**Date**: 2026-05-13
**Experiment**: `mvp_interaction_index_profiling`
**Server**: westd-22162
**Runtime**: ~0.54h
**Verdict**: **FAIL (code bug, NOT hypothesis failure)**

---

## 1. Summary

All 6 Interaction Index values are NaN due to a bug in KV cache eviction mask flattening. The `kv` and `both` perplexity conditions produce NaN because the attention mask is effectively all-zeros after flattening. The `dense` and `attn` conditions produce valid, reasonable values. Phase segmentation is healthy. **The hypothesis remains untested.**

---

## 2. Raw Results

### 2.1 Phase Statistics

| Phase | Tokens | Segments | ≥ 20 Segments? |
|-------|--------|----------|----------------|
| execution | 1,022 | 25 | YES |
| reasoning | 7,007 | 96 | YES |
| transition | 78,178 | 192 | YES |

### 2.2 Perplexity (mean across segments)

| Phase | Sparsity | dense | attn | kv | both |
|-------|----------|-------|------|----|------|
| execution | 0.3 | 2.2485 | 1065.8501 | NaN | NaN |
| execution | 0.5 | 2.2485 | Inf | NaN | NaN |
| reasoning | 0.3 | 1.1798 | 16.6822 | NaN | NaN |
| reasoning | 0.5 | 1.1798 | 692.5218 | NaN | NaN |
| transition | 0.3 | 1.0997 | 66.9653 | NaN | NaN |
| transition | 0.5 | 1.0997 | 808.5626 | NaN | NaN |

### 2.3 Interaction Index (all NaN)

| Phase | Sparsity | II mean | CI_low | CI_high |
|-------|----------|---------|--------|---------|
| execution | 0.3 | NaN | NaN | NaN |
| execution | 0.5 | NaN | NaN | NaN |
| reasoning | 0.3 | NaN | NaN | NaN |
| reasoning | 0.5 | NaN | NaN | NaN |
| transition | 0.3 | NaN | NaN | NaN |
| transition | 0.5 | NaN | NaN | NaN |

### 2.4 Pass/Fail Tests

- CI overlap test: **FAIL** (no valid CIs to compare)
- Sign reversal test: **FAIL** (no valid II values)
- Overall: **FAIL**

---

## 3. Root Cause Analysis

### Bug Location

`pacs/profiling/interaction_index.py`, method `forward_with_sparse_config`, line ~210:

```python
flat_kv_mask = kv_mask.min(dim=0).values  # (seq_len,)
model_attention_mask = attention_mask * flat_kv_mask.unsqueeze(0)
```

### Mechanism

`_select_kv_to_evict` creates a `(num_layers, seq_len)` binary mask where each of the 28 layers **independently** and **randomly** selects positions to evict. `min(dim=0)` computes the element-wise minimum across all layers — a position is kept only if it survives in **every** layer.

With 28 layers and sparsity ratio `s`:

| Sparsity | P(kept per layer) | P(kept in ALL 28 layers) | Expected kept positions (seq_len=500) |
|----------|-------------------|--------------------------|---------------------------------------|
| 0.3 | 0.70 | 0.7^28 = 7.25e-4 | ~0.36 |
| 0.5 | 0.50 | 0.5^28 = 3.73e-9 | ~0.00 |

Result: the attention mask becomes all-zeros → softmax over empty set → NaN logits → NaN perplexity.

### Evidence

- `dense` (no masking) and `attn` (hook-based head masking, no KV mask) produce valid values
- Only `kv` and `both` (which use KV mask → attention mask path) are NaN
- The code comment says "apply the *union* (min across layers)" but `min` computes the **intersection**, not the union

### Existing Correct Code (Unused)

`_build_kv_attention_mask()` (line ~141) correctly constructs a `(num_layers, batch, seq_len)` per-layer mask, but `forward_with_sparse_config` does not use it.

---

## 4. Data Quality Checks

### 4.1 Segment counts
All phases have ≥ 20 segments. Sufficient for bootstrap.

### 4.2 NaN/Inf in valid conditions
- `dense`: no NaN/Inf across all phases ✓
- `attn` at s=0.5 execution: Inf (expected — 50% head pruning on short execution phase is extreme)
- `kv` and `both`: all NaN (bug)

### 4.3 Phase segmentation
- Working correctly: 50/50 problems processed
- Bandwidth halving warnings are normal (KDE fallback for simpler traces)
- Phase distribution is heavily skewed toward `transition` (78K tokens vs 1K execution) — expected for long CoT traces

### 4.4 Dense PPL pattern
Reasonable ordering: execution (2.25) > reasoning (1.18) > transition (1.10). Execution phase has highest perplexity (computational steps are harder to predict); transition is lowest (long predictable reasoning chains).

### 4.5 Attn-only observations (s=0.3)
- execution: 1065.85 (474× dense) — extreme sensitivity to head pruning
- transition: 66.97 (61× dense) — moderate sensitivity
- reasoning: 16.68 (14× dense) — least sensitive

This already shows phase-dependent sensitivity to attention head pruning. If KV eviction shows a different ordering, the interaction hypothesis is plausible.

---

## 5. Fix Recommendations

### Option A: Layer-uniform KV eviction (recommended for MVP)

Make `_select_kv_to_evict` select the same positions across all layers. Then `min == max == the single mask`, and the flattening is correct.

```python
# In _select_kv_to_evict: generate one mask, broadcast to all layers
base_mask = torch.ones(seq_len)
indices = torch.randperm(seq_len - 1)[:num_to_evict] + 1  # skip BOS
base_mask[indices] = 0.0
mask = base_mask.unsqueeze(0).expand(num_layers, -1).clone()
```

### Option B: Per-layer masking via hooks

Use `_build_kv_attention_mask` and apply per-layer masks through forward hooks on each attention layer, similar to `_HeadMaskHook`.

### Option C: Fix the flattening

If per-layer random eviction is desired, change `min` to something semantically correct. But this requires custom model code since HF models accept only a flat attention mask.

**Recommendation**: Option A for the MVP rerun. It's the simplest fix, semantically valid (uniform KV eviction is standard in the literature), and doesn't require model surgery.

---

## 6. Conclusion

**MVP status**: FAIL due to code bug. The hypothesis is **untested**.

**What works**:
- Phase segmentation pipeline (KDE + sparsity trace)
- Attention head pruning (hook-based masking)
- Dense perplexity computation
- Bootstrap CI infrastructure
- Data loading and stratified sampling

**What's broken**:
- KV cache eviction masking (single-line fix)

**Next step**: Fix `_select_kv_to_evict` or `forward_with_sparse_config`, rerun. Expected wall time: ~0.5h.

---

## 7. Output Files

| File | Path | Status |
|------|------|--------|
| Results JSON | `/root/autodl-tmp/pacs/profiling_output/profiling_results.json` | Valid (contains NaN) |
| Run log | `~/runs/phase-gated-compound-sparse/mvp_interaction_index_profiling.log` | Clean (no tracebacks) |
| Figures | None generated | N/A |
