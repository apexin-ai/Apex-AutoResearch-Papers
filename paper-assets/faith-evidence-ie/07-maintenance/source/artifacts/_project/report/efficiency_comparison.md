# Inference Efficiency Comparison

All experiments run on RTX 5090 (single GPU). Times are wall-clock seconds.

**Important caveats**:
- `batch_size` and `max_new_tokens` vary across evals — only compare within matched-setting groups
- No-evidence mode sometimes generates MORE tokens (more predictions, higher truncation), which can make it slower than with-evidence for smaller models
- GPU contention from concurrent jobs may affect some timings

---

## 1. Evidence Tax — SFT Dev (batch=4, max_tokens=2048, 985 docs)

d140 series: cleanest matched comparison for evidence overhead.

| Scale | With-Evi (s) | s/doc | No-Evi (s) | s/doc | Δ% | #Pred (w/) | #Pred (no) |
|-------|-------------|-------|-----------|-------|-----|-----------|-----------|
| Qwen3-1.7B | 6,424 | 6.52 | 7,438 | 7.55 | **−13.6%** | 25,534 | 44,566 |
| Qwen3-4B | 8,887 | 9.02 | 7,606 | 7.72 | **+16.8%** | 24,682 | 25,638 |
| Qwen3-8B | 10,486 | 10.65 | 10,901 | 11.07 | **−3.8%** | 25,007 | 31,119 |

Sources: `d140_{scale}_sft_s42_with_evi_2048` / `d140_{scale}_sft_s42_no_evi_2048_fix`

**Finding**: Evidence tax is NOT a straightforward overhead. For 1.7B, no-evidence mode generates 1.75× more predictions (44,566 vs 25,534) and is actually 13.6% slower. For 4B, with-evidence is 16.8% slower. For 8B, roughly equal. The evidence field acts as a structural constraint that reduces output verbosity for smaller models.

## 2. Evidence Tax — 14B Dev (batch=1, max_tokens=2048, 985 docs)

| Model | Paradigm | With-Evi (s) | s/doc | No-Evi (s) | s/doc | Δ% |
|-------|----------|-------------|-------|-----------|-------|-----|
| Qwen3-14B | SFT | 18,011 | 18.29 | 14,498 | 14.72 | +24.2% |
| Qwen3-14B | RSFT s43 | 20,676 | 20.99 | 17,799 | 18.07 | +16.2% |

Sources: registry (plan_019 14B SFT), `plan017_14b_rsft_s43_eval` / `plan017_14b_rsft_s43_no_evi_eval`

**Finding**: At 14B scale, evidence generation adds 16–24% overhead — the expected "evidence tax" pattern. Larger models don't over-generate in no-evidence mode.

## 3. Evidence Tax — LLaMA-3.1-8B Dev (batch=1, max_tokens=2048, 985 docs)

| Paradigm | With-Evi (s) | s/doc | No-Evi (s) | s/doc | Δ% |
|----------|-------------|-------|-----------|-------|-----|
| SFT | 10,492 | 10.65 | 12,529* | 12.72 | −16.3% |
| RSFT | 15,375 | 15.61 | 15,710 | 15.95 | −2.1% |

*SFT no-evi uses batch=4 (others batch=1), so this comparison is confounded.

Sources: `eval_llama_sft_s42_with_evidence_2048`, `eval_llama_sft_s42_no_evidence_2048`, `eval_llama_rsft_s42_with_evidence_2048`, `eval_llama_rsft_s42_no_evi_2048`

## 4. Model Scaling — SFT with-Evidence Dev (batch=4, max_tokens=2048)

| Scale | Time (s) | s/doc | Relative to 1.7B |
|-------|---------|-------|-------------------|
| Qwen3-1.7B | 6,424 | 6.52 | 1.00× |
| Qwen3-4B | 8,887 | 9.02 | 1.38× |
| Qwen3-8B | 10,486 | 10.65 | 1.63× |

14B and LLaMA use batch=1, not directly comparable:

| Scale | Time (s) | s/doc | Batch |
|-------|---------|-------|-------|
| LLaMA-3.1-8B | 10,492 | 10.65 | 1 |
| Qwen3-14B | 18,011 | 18.29 | 1 |

**Finding**: Inference time scales sub-linearly with model size (1.7B→8B is 4.7× params but only 1.63× time at batch=4).

## 5. SFT vs RSFT — Dev with-Evidence

### Matched batch=1, max_tokens=2048

| Scale | SFT (s) | RSFT (s) | Δ% |
|-------|---------|---------|-----|
| LLaMA-3.1-8B | 10,492 | 15,375 | +46.5% |
| Qwen3-14B | 18,011 | 20,676 | +14.8% |

### Matched batch=4, max_tokens=1024

| Scale | SFT* (s) | RSFT (s) | Source |
|-------|----------|---------|--------|
| Qwen3-1.7B | N/A | 8,836 | d102_1_7b_k1_s42 |
| Qwen3-4B | ~6,139† | 10,816–13,078 | reeval series |
| Qwen3-8B | N/A | 11,700 | d102_8b_k1_s42 |

*No SFT eval at batch=4 / max_tokens=1024 for 1.7B/8B. †SFT 4B reeval baseline: 6,138.5s.

**Finding**: RSFT is 15–47% slower than SFT (with evidence), likely because RSFT generates more structured, higher-quality evidence output.

## 6. Test Set (500 docs, max_tokens=2048)

### batch=1 evals (comparable)

| Scale | Paradigm | Evidence | Time (s) | s/doc |
|-------|----------|----------|---------|-------|
| Qwen3-1.7B | SFT | ✓ | 12,179 | 24.36 |
| Qwen3-1.7B | SFT | ✗ | 13,010 | 26.02 |
| Qwen3-1.7B | RSFT | ✓ | 21,129 | 42.26 |
| Qwen3-1.7B | RSFT | ✗ | 24,157 | 48.31 |
| Qwen3-4B | SFT | ✓ | 15,019 | 30.04 |
| Qwen3-4B | SFT | ✗ | 11,801 | 23.60 |
| Qwen3-4B | RSFT | ✗ | 20,789 | 41.58 |
| Qwen3-8B | SFT | ✓ | 16,165 | 32.33 |
| Qwen3-8B | SFT | ✗ | 15,655 | 31.31 |
| Qwen3-8B | RSFT | ✗ | 16,425 | 32.85 |
| LLaMA-3.1-8B | SFT | ✓ | 12,493 | 24.99 |
| LLaMA-3.1-8B | SFT | ✗ | 12,679 | 25.36 |
| LLaMA-3.1-8B | RSFT | ✓ | 19,571 | 39.14 |
| Qwen3-14B | SFT | ✓ | 20,463 | 40.93 |
| Qwen3-14B | SFT | ✗ | 19,010 | 38.02 |
| Qwen3-14B | RSFT | ✓ | 19,086 | 38.17 |
| Qwen3-14B | RSFT | ✗ | 20,126 | 40.25 |

### batch=16 evals (NOT comparable to batch=1)

| Scale | Paradigm | Evidence | Time (s) | s/doc |
|-------|----------|----------|---------|-------|
| Qwen3-4B | RSFT | ✓ | 4,124 | 8.25 |
| Qwen3-8B | RSFT | ✓ | 2,711 | 5.42 |
| LLaMA-3.1-8B | RSFT | ✗ | 4,089 | 8.18 |

## 7. Summary of Key Findings

1. **Evidence tax is scale-dependent**: Small models (1.7B) generate MORE output without evidence constraints, making no-evidence mode slower. At 14B, evidence adds 16–24% overhead. The crossover occurs around 4B–8B scale.

2. **Sub-linear scaling**: 1.7B→8B (4.7× params) only increases inference time 1.63× at batch=4, thanks to memory-bound generation.

3. **RSFT overhead**: RSFT adds 15–47% inference time over SFT due to more structured output generation.

4. **Test vs dev**: Test set is ~2–3× slower per document than dev (24–42 s/doc test vs 7–18 s/doc dev), reflecting larger/more complex test documents.

5. **Batching impact**: batch=16 gives ~4–6× speedup over batch=1 (e.g., 4B RSFT test: 8.25 s/doc at batch=16 vs ~41 s/doc at batch=1).
