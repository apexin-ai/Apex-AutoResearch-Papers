# `<think>` Token Phase Validation (R9-C1)

## Key Results
- **Effective n = 48** (2 problems skipped; 4 sparsity conditions share identical dense-model phase boundaries → n=48 not n=192)
- Median Cohen's κ = **0.887** (almost perfect agreement)
- Thinking tokens in low-sparsity phase: **57.8%**
- Answer tokens in high-sparsity phase: **62.7%**
- Conclusion: **PASS** — sparsity tercile segmentation meaningfully captures CoT phase structure

## Server paths
- Analysis script: `/root/autodl-tmp/pacs/analyze_think_phase_validation.py`
- Output JSON: `/root/autodl-tmp/pacs/analysis_output/think_phase_validation.json`

## Note on effective sample size
Phase segmentation is computed on the dense model's attention sparsity distribution. Since all 4 sparsity conditions (s015/s020/s025/s030) use the same dense model, they produce identical phase boundaries. Therefore effective n = 48 unique problems, not 48 × 4 = 192.
