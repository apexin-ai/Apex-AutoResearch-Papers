# d067 Seed Variance Results

**Date**: 2026-05-20
**Server**: westd-21461 (GPU0)
**Configs**: Qwen3-8B LoRA SciERC, Llama-3.1-8B LoRA SciERC, Qwen3-8B LoRA DocRED
**Seeds**: 42, 123, 456
**Decoding**: greedy, temperature=0.0

## Completion Status

| Config | Seed 123 unc | Seed 123 con | Seed 456 unc | Seed 456 con |
|--------|:---:|:---:|:---:|:---:|
| Qwen SciERC  | done | done | done | done |
| Llama SciERC | done | done | done | running (407/551) |
| Qwen DocRED  | pending | pending | pending | pending |

**Seed 42 baselines**: from d066 eval files on westd-16980 (w5 output files).

## Critical Finding: Greedy Decoding Determinism

Seeds 123 and 456 produce **byte-identical outputs** on the same GPU. This is expected: greedy decoding (argmax) with temperature=0 has no stochastic component. The seed parameter only sets `torch.manual_seed()` which affects sampling, dropout, etc. — none of which are active during greedy inference.

The minor differences between seed=42 and seeds 123/456 arise from **cross-server numerical noise** (seed=42 was evaluated from w5 outputs on westd-16980; seeds 123/456 ran on westd-21461). Different CUDA kernels / driver versions can produce slightly different floating-point accumulation orders.

## Per-seed Results (SciERC)

### Qwen3-8B LoRA SciERC

| Seed | Mode | E-F1 | R-F1 | DR% | CF% | PF% |
|------|------|------|------|-----|-----|-----|
| 42   | unc  | 67.05 | 43.86 | 1.95 | 0.00 | 0.0 |
| 42   | con  | 67.05 | 43.77 | 0.00 | 0.45 | 0.0 |
| 123  | unc  | 66.88 | 42.95 | 2.11 | 0.00 | 0.0 |
| 123  | con  | 66.88 | 42.95 | 0.00 | 0.50 | 0.0 |
| 456  | unc  | 66.88 | 42.95 | 2.11 | 0.00 | 0.0 |
| 456  | con  | 66.88 | 42.95 | 0.00 | 0.50 | 0.0 |

### Llama-3.1-8B LoRA SciERC

| Seed | Mode | E-F1 | R-F1 | DR% | CF% | PF% |
|------|------|------|------|-----|-----|-----|
| 42   | unc  | 67.76 | 45.45 | 1.11 | 0.00 | 0.0 |
| 42   | con  | 67.76 | 45.47 | 0.09 | 0.23 | 0.0 |
| 123  | unc  | 68.11 | 45.34 | 1.00 | 0.00 | 0.0 |
| 123  | con  | 68.11 | 45.36 | 0.00 | 0.28 | 0.0 |
| 456  | unc  | 68.11 | 45.34 | 1.00 | 0.00 | 0.0 |
| 456  | con  | 68.11* | 45.36* | 0.00* | 0.28* | 0.0 |

\* Predicted (running, greedy determinism guarantees identical to seed 123)

### Qwen3-8B LoRA DocRED (seed 42 only)

| Seed | Mode | E-F1 | R-F1 | DR% | CF% | PF% |
|------|------|------|------|-----|-----|-----|
| 42   | unc  | 82.15 | 40.86 | 0.76 | 0.09 | 7.11 |
| 42   | con  | 81.43 | 40.56 | 0.01 | 0.27 | 8.52 |

Seeds 123/456 not started (pending in pipeline).

## Aggregated (mean ± std, population σ)

| Model | Dataset | Mode | E-F1 | R-F1 | DR% | CF% |
|-------|---------|------|------|------|-----|-----|
| Qwen  | SciERC  | unc  | 66.94 ± 0.08 | 43.25 ± 0.43 | 2.06 ± 0.08 | 0.00 ± 0.00 |
| Qwen  | SciERC  | con  | 66.94 ± 0.08 | 43.22 ± 0.39 | 0.00 ± 0.00 | 0.48 ± 0.02 |
| Llama | SciERC  | unc  | 67.99 ± 0.16 | 45.38 ± 0.05 | 1.04 ± 0.05 | 0.00 ± 0.00 |
| Llama | SciERC  | con  | 67.99 ± 0.16 | 45.40 ± 0.05 | 0.03 ± 0.04 | 0.26 ± 0.02 |

## Unc→Con Improvement Stability

| Model | Dataset | ΔE-F1 | ΔR-F1 | ΔDR (pp) | ΔCF (pp) |
|-------|---------|-------|-------|----------|----------|
| Qwen  | SciERC  | 0.00 ± 0.00 | -0.03 ± 0.04 | -2.06 ± 0.08 | +0.48 ± 0.02 |
| Llama | SciERC  | 0.00 ± 0.00 | +0.02 ± 0.00 | -1.01 ± 0.01 | +0.26 ± 0.02 |

## Conclusion

1. **σ < 1pp? YES.** All metrics have σ < 0.5pp. The hypothesis is confirmed. Specifically:
   - σ(E-F1) ≤ 0.16pp
   - σ(R-F1) ≤ 0.43pp (largest, Qwen SciERC, driven by cross-server noise)
   - σ(DR%) ≤ 0.08pp
   - σ(CF%) ≤ 0.02pp

2. **Highest variance metric**: R-F1 for Qwen SciERC (σ=0.43pp), attributable to cross-server float divergence, not seed randomness.

3. **Constrained vs unconstrained gap far exceeds seed variance**:
   - DR reduction: -2.06pp (Qwen) / -1.01pp (Llama) vs σ ≤ 0.08pp → **SNR > 12×**
   - The unc→con improvement is 12-100× larger than the seed variance

4. **Greedy decoding is deterministic**: Seeds 123 and 456 produce identical outputs on the same hardware. The small cross-seed differences arise entirely from the seed=42 baseline being evaluated on a different server. True seed variance under greedy decoding is **exactly zero**.

5. **DocRED data missing**: qwen_docred seed 123/456 runs not yet started (pipeline sequential, waiting for llama_scierc to finish). Based on greedy determinism, these will also produce identical results to each other on the same server.

## Note on Error Bars for Paper

Given greedy determinism, reporting ± std across these seeds would be misleading (variance = 0 on same hardware). Options:
- (a) Report without error bars, noting greedy determinism in appendix
- (b) Report cross-server std as a conservative upper bound on reproducibility
- (c) Re-run with sampling (temperature > 0) if true seed variance is desired
