# detect_remove_q05_v2_seed456 — Final Metrics

## Training Summary
- **Status**: Completed successfully (EXIT_CODE=0)
- **Total steps**: 6103/6103
- **Train loss** (HF Trainer avg): 11.01
- **Training time**: ~4h08m (14920s)
- **Epoch**: 0.6352
- **Training config**: uniform weighting, filtered data (q≤0.5, 153725 samples), bs=4×grad_accum=4, lr=5e-5 linear, seed=456

## Eval Metrics (seed456)
| Metric | Loss | Perplexity | Tokens |
|--------|------|------------|--------|
| Holdout | 2.8493 | **17.277** | 4,077,068 |
| OWT | 2.8913 | **18.017** | 6,767,242 |
| Wiki | — | **pending** (fp32 eval running) | — |

**Note**: Wiki eval with fp16+autocast (eval_perplexity.py) produced NaN. Re-running with fp32 (eval_perplexity_fp32.py) on GPU 2, PID 779491. Holdout/OWT used same fp16 eval without issues.

## 3-Seed Comparison: detect_remove_q05_v2

| Seed | Holdout PPL | OWT PPL | Wiki PPL |
|------|-------------|---------|----------|
| seed42 | 17.285 | 18.014 | 15.053 |
| seed123_r2 | 17.272 | 18.008 | 15.047 |
| seed456 | 17.277 | 18.017 | pending |

### Aggregated (mean ± std)
- **Holdout PPL**: 17.278 ± 0.007
- **OWT PPL**: 18.013 ± 0.005
- **Wiki PPL**: 15.050 ± 0.004 (2-seed only, seed456 pending)

## Checkpoint Paths
- Final model: `/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed456/final`
- Checkpoints: checkpoint-5500, checkpoint-6000, checkpoint-6103
- Log: `~/runs/provenance_weight_training/detect_remove_q05_v2_seed456.log`
- Eval results: `/root/autodl-tmp/provenance_weight_training/output/eval_results/detect_remove_q05_v2_seed456/`

## Observations
- 3-seed holdout PPL 极其一致（std=0.007），确认 D&R hard filtering 结果稳定
- OWT PPL 同样高度一致（std=0.005）
- Wiki eval fp16+autocast 出现 NaN，可能是长文档数值溢出，其他两个 seed 未出现此问题。fp32 eval 正在运行中
