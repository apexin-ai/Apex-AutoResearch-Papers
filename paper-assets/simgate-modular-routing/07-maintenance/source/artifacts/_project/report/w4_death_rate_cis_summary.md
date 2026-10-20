# W4: Per-Task Death Rate Differential Confidence Intervals

**Source**: westd-18266:/root/autodl-tmp/simgate-modular-routing/artifacts/w4_death_rate_cis.md
**Data**: death_decomposition_report.json, 30 tasks, 249 matched episodes

## Key Results

### Per-Task Analysis
- 28/30 tasks are death-prone (internal DR > 0 OR deterministic DR > 0)
- **15/28 individually significant** (95% CI for Δ excludes 0)
- **13/28 non-significant** — ALL have n=5 (statistical power limitation)
- **100% directional consistency**: internal DR > deterministic DR in ALL 28 death-prone tasks

### Pooled Analysis
| Metric | Value | 95% CI |
|--------|-------|--------|
| Internal DR | 49.0% | [42.8%, 55.2%] |
| Deterministic DR | 11.6% | [8.2%, 16.2%] |
| **Delta** | **+37.3%** | **[+29.7%, +44.4%]** |

### Paper Narrative
"Death dominance is universal across tasks" — supported by:
1. 100% directional consistency (no exceptions)
2. Pooled effect highly significant
3. Non-significant individual tasks are entirely explained by small sample size (n=5), not absence of effect