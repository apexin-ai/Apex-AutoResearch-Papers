# eval_rsft_ced_s43 Results

**Model**: Qwen3-4B + SFT (merged) + CED RSFT LoRA (checkpoint-510, seed=43)
**Eval**: Full dev set (985 docs, 12275 gold triples), batch_size=4, max_new_tokens=1024, no-quantize
**Date**: 2026-05-16 | **Inference time**: 10768s (2h59m, 10.93 s/doc)

## Metrics

| Metric | Value |
|--------|-------|
| **rel_f1** | **0.4601** |
| ign_f1 | 0.4512 |
| precision | 0.4696 |
| recall | 0.4509 |
| evi_f1 | 0.8063 |
| evi_precision | 0.8025 |
| evi_recall | 0.8101 |
| edcr | 0.6542 |
| evi_f1_joint | 0.3605 |
| format_ok_rate | 1.000 (985/985) |
| n_truncated | 184/985 |
| n_predictions | 15051 |

## CED Seed Comparison (current eval protocol)

| Seed | rel_f1 | ign_f1 | evi_f1 | edcr | evi_f1_joint | n_truncated |
|------|--------|--------|--------|------|-------------|-------------|
| s43 | 0.4601 | 0.4512 | 0.8063 | 0.6542 | 0.3605 | 184 |
| s45 | 0.4514 | 0.4416 | 0.8174 | 0.6550 | 0.3558 | 206 |
| **2-seed mean** | **0.4558** | **0.4464** | **0.8119** | **0.6546** | **0.3582** | **195** |
| 2-seed std | 0.0062 | 0.0068 | 0.0078 | 0.0006 | 0.0033 | 16 |

**Note**: CED s42 and s44 re-evals (`reeval_ced_s42`, `reeval_ced_s44`) are currently RUNNING. The 4-seed CED statistics below use mvp2-era reference values for s42/s44 and should be updated when re-evals complete.

### CED 4-seed estimate (2 current + 2 mvp2-era reference)

| Seed | rel_f1 | evi_f1 | edcr | Protocol |
|------|--------|--------|------|----------|
| s42 | 0.4449* | 0.8187* | 0.6565* | mvp2 |
| s43 | 0.4601 | 0.8063 | 0.6542 | current |
| s44 | 0.4655* | 0.8087* | 0.6350* | mvp2 |
| s45 | 0.4514 | 0.8174 | 0.6550 | current |
| **4-seed mean** | **0.4555** | **0.8128** | **0.6502** | mixed |
| 4-seed std | 0.0090 | 0.0060 | 0.0099 | mixed |

*\* mvp2-era values, pending re-evaluation*

## flat-NLI Seed Comparison (all current eval protocol)

| Seed | rel_f1 | ign_f1 | evi_f1 | edcr | evi_f1_joint |
|------|--------|--------|--------|------|-------------|
| s42 | 0.4539 | 0.4539 | 0.8043 | 0.6431 | — |
| s43 | 0.4523 | 0.4523 | 0.8158 | 0.6505 | — |
| s44 | 0.4615 | 0.4521 | 0.8131 | 0.6458 | 0.3597 |
| s45 | 0.4551 | 0.4462 | 0.8154 | 0.6521 | 0.3556 |
| **4-seed mean** | **0.4557** | **0.4511** | **0.8122** | **0.6479** | — |
| 4-seed std | 0.0040 | 0.0034 | 0.0054 | 0.0042 | — |

## CED vs flat-NLI (preliminary)

| Metric | CED (2-seed) | flat-NLI (4-seed) | Δ |
|--------|-------------|-------------------|------|
| rel_f1 | 0.4558 | 0.4557 | +0.0001 |
| ign_f1 | 0.4464 | 0.4511 | −0.0047 |
| evi_f1 | 0.8119 | 0.8122 | −0.0003 |
| edcr | 0.6546 | 0.6479 | +0.0067 |

**Preliminary conclusion**: With only 2 CED seeds completed under the current eval protocol, CED and flat-NLI are virtually indistinguishable on rel_f1 (Δ < 0.001). EDCR slightly higher for CED (+0.007), suggesting marginally less distractor citation. Statistical significance testing requires all 4 CED seeds.

## Conclusion

- **rel_f1 = 0.4601** is within the expected 0.43–0.47 range → **success**
- s43 is the highest CED rel_f1 so far (vs s45's 0.4514), consistent with normal seed variance
- Format compliance 100%, truncation 18.7% (184/985) — typical for this model
- All metrics nominal; no anomalies detected
- **Action**: await reeval_ced_s42 and reeval_ced_s44 completion for final 4-seed CED statistics and proper CED vs flat-NLI paired comparison
