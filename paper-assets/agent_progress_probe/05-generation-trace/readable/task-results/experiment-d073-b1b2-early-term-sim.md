# experiment d073 b1b2 early term sim

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_d073-b1b2-early-term-sim_20260516T022819_result.json`
- **Structured JSON:** [`c519c3b89afd4cdf6c28.json`](../../sessions/c5/c519c3b89afd4cdf6c28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Both tasks done. Here's the summary:

---

## D073-B1: Early Termination Simulation

**Setup**: Train on SWE conf≥2, cross-agent eval on OH (4969 trajectories, 43376 windows, 19.9% stag prevalence). 3 seeds.

| Model | k | Precision | Recall | Compute Saved |
|-------|---|-----------|--------|---------------|
| **3lf_gb** | 1 | 0.995±0.000 | 1.000±0.000 | **40.4%** |
| **3lf_gb** | 2 | 0.998±0.000 | 0.772±0.000 | 29.7% |
| **3lf_gb** | 3 | 1.000±0.000 | 0.451±0.000 | 16.3% |
| 2lf_rf | 1 | 0.848±0.142 | 1.000±0.000 | 40.6% |
| 2lf_rf | 3 | 0.972±0.035 | 0.451±0.000 | 16.3% |
| oracle | 1 | 1.000 | 1.000 | 40.4% |
| random | 1 | 0.261 | 0.814 | 38.1% |

**Key finding**: 3-LF GB is near-oracle — at k=1 it saves 40.4% compute with 99.5% precision. At k≥3 it achieves perfect precision (zero false terminations that matter).

---

## D073-B2: Compute Waste Audit

| Metric | All | SWE-Agent | OpenHands |
|--------|-----|-----------|-----------|
| Total trajectories | 10,000 | 5,000 | 5,000 |
| With stagnation tail | 1,096 (11%) | 863 (17.3%) | 233 (4.7%) |
| Mean tail ratio | 35.1% | 38.5% | 22.5% |
| Median tail ratio | 19.3% | 22.0% | 12.2% |

**Key finding**: SWE-Agent wastes significantly more compute on stagnation tails than OpenHands (17.3% vs 4.7% affected, and 38.5% vs 22.5% wasted per affected trajectory).

---

Output files on server: `/root/autodl-tmp/agent_progress_probe/artifacts/d072/{early_termination_sim,compute_waste_audit}.json`

---
