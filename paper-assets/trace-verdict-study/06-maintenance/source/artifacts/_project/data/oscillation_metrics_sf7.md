Remote files on westd-11235:
- /root/autodl-tmp/trace-verdict-study-checkpoints/oscillation_metrics/oscillation_metrics.json
- /root/autodl-tmp/trace-verdict-study-checkpoints/oscillation_metrics/oscillation_summary.txt

Key metrics:
| Metric | exception_only | full_trace | Ratio |
|--------|---------------|------------|-------|
| Loss rolling variance (w=5) | 0.0036 | 0.1658 | 46x |
| Eval accuracy CV (full) | 0.0024 | 0.0222 | 9.4x |
| Eval accuracy CV (2nd half) | 0.0000 | 0.0172 | ∞ |
| Last 3 checkpoint std | 0.0000 | 0.0135 | — |
| Max drop | 0pp | 5.29pp | — |
| Recovery time | N/A | 150 steps | — |
| Direction changes | 2/8 | 5/8 | 2.5x |
| First stable (ε=0.005) | step 200 | never | — |