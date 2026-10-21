# eval_rsft_ced_s45 Results

## Key Metrics
| Metric | Value |
|--------|-------|
| F1 | 0.4514 |
| Ign-F1 | 0.4416 |
| Precision | 0.4718 |
| Recall | 0.4326 |
| Evi-F1 | 0.8174 |
| Evi-Precision | 0.8210 |
| Evi-Recall | 0.8139 |
| Evi-F1 (joint) | 0.3558 |
| EDCR | 0.6550 |
| Format OK | 985/985 (100%) |
| Truncated | 206/985 |
| Predictions | 15307 |

## Config
- Model: Qwen3-4B + SFT adapter + CED RSFT LoRA (seed=45, checkpoint-510)
- Split: dev (985 docs, 12275 gold triples)
- batch_size=4, max_new_tokens=1024, no quantize
- Inference time: 10211.6s (~2h50m)

## CED RSFT Cross-Seed Comparison (rel_f1)
| Seed | F1 | Status |
|------|------|--------|
| s42 | TBD (from mvp2_eval_rsft_r2b_maxtok1536_r2) | needs confirmation |
| s43 | TBD | eval running |
| s44 | TBD | needs confirmation |
| s45 | **0.4514** | ✓ done |

## Flat-NLI RSFT Comparison (rel_f1)
| Seed | F1 |
|------|------|
| s42 | 0.4539 |
| s43 | rerunning |
| s44 | rerunning |
| s45 | TBD |

## Conclusion
CED RSFT s45 F1=0.4514 > 0.40 threshold → success. Comparable to flat-NLI s42 (0.4539). Awaiting remaining seeds for paired t-test.
