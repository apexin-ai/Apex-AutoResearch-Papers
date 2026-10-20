# analysis bootstrap ci crossagent

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-ci-crossagent_20260515T042535_result.json`
- **Structured JSON:** [`f4b4eb9c27d027c306a9.json`](../../sessions/f4/f4b4eb9c27d027c306a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary:

```
=== Paired Bootstrap: 11 LF-overlap vs 30 Full (OH Cross-Agent) ===

All-windows (N=150,652):
  F1_11 = 0.977, F1_30 = 0.9674
  Delta = +0.0096
  95% CI: [0.0085, 0.0107]
  p-value: <0.001 (significant)

Conf>=2 (N=43,376):
  F1_11 = 0.9848, F1_30 = 0.9919
  Delta = -0.0071
  95% CI: [-0.0088, -0.0054]
  p-value: 1.0 (NOT significant; direction reverses)
```

Key findings:
- **All-windows**: 11 LF-overlap features significantly outperform 30 full features (+0.96pp, p<0.001, CI entirely positive). The pruned model generalizes better cross-agent.
- **Conf>=2**: Direction **reverses** — full 30 features outperform 11 LF-overlap by 0.71pp. On high-confidence labels, the extra 19 residual features help.
- HPs used: full_30 lr=0.05, lf_overlap_11 lr=0.01 (matching original ablation).

Outputs:
- JSON: `/root/autodl-tmp/agent_progress_probe/artifacts/feature-overlap-ablation/bootstrap_ci_crossagent.json`
- Script: `/root/autodl-tmp/agent_progress_probe/src/analysis/bootstrap_ci_crossagent.py`
- Registry: `feature-overlap-ablation` metrics updated with `bootstrap_ci_crossagent` field

---
