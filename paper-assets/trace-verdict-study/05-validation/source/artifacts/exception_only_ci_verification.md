# Exception Only CI Verification

Paired bootstrap resampling (N=10000, seed=42) on exception_only (vota_exception_only_seed42_v2).

- N samples: 1190
- Accuracy: 99.8319%
- Misclassified: 2
- **95% CI: [99.58, 100.00]**

## Discrepancy

| Source | CI Lower | CI Upper |
|--------|----------|----------|
| Table 1 (paper) | 99.50 | 100.00 |
| Registry | 99.58 | 100.00 |
| This verification | 99.58 | 100.00 |

**Conclusion**: Table 1 lower bound 99.50 is incorrect. Correct value is **99.58**.
