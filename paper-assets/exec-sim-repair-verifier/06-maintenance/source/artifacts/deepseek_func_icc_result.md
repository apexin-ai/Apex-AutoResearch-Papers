# DeepSeek Function-Level CLS: Inter-Seed ICC(3,1)

## Result

| Metric | Value |
|--------|-------|
| ICC(3,1) | **0.6530** |
| 95% CI | [0.6263, 0.6781] |
| n_test_cases | 1890 |
| n_seeds | 2 (s42, s123) |

## Per-Seed Accuracy

| Seed | Accuracy | Correct |
|------|----------|---------|
| s42 | 86.93% | 1643/1890 |
| s123 | 87.14% | 1647/1890 |

## Agreement Breakdown

| Category | Count | Pct |
|----------|-------|-----|
| Total agreement | 1742/1890 | 92.2% |
| Both correct | 1571 | 83.1% |
| Both wrong | 171 | 9.0% |
| Disagree | 148 | 7.8% |

## Comparison with Qwen3-4B

| Model | Function-Level ICC(3,1) | Interpretation |
|-------|------------------------|----------------|
| Qwen3-4B | 0.191 | Slight agreement |
| DeepSeek-Coder-6.7B | **0.653** | Substantial agreement |

## Interpretation

DeepSeek-Coder-6.7B shows substantially higher inter-seed consistency (ICC=0.653) than Qwen3-4B (ICC=0.191). This means DeepSeek's prediction errors are more systematic, driven by inherent test-case difficulty rather than training randomness. The 92.2% raw agreement rate and narrow 95% CI [0.626, 0.678] confirm this is a robust finding.

Higher ICC implies stronger within-block correlation of errors, which further supports the paper's argument that per-test scoring exploits block structure more effectively than trajectory-level scoring.

## Technical Details

- ICC type: ICC(3,1), two-way mixed, single measures
- MS_between (rows) = 0.1866
- MS_error = 0.0392
- F = 4.7635
- Checkpoints: `/root/autodl-tmp/checkpoints_deepseek_cls_func/best/` (s42), `/root/autodl-tmp/checkpoints_deepseek_cls_func_seed123/best/` (s123)
- Test data: `/root/exec-sim-repair-verifier/data/func_cls/swebench_test.jsonl`
- s123 predictions re-evaluated on 2026-05-19 (original predictions_func.jsonl was overwritten with repo-level data)
