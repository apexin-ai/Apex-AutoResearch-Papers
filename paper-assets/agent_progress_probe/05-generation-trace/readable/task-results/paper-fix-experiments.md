# paper fix experiments

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-experiments_20260515T010600_result.json`
- **Structured JSON:** [`157a62c34d49afafc03f.json`](../../sessions/15/157a62c34d49afafc03f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied correctly. Summary of changes:

**§5.1** — OH stagnation ratio: 6.6% → 21.4% (text line 20 + Table 1 line 32)

**§5.2 Table 2** — ProgressProbe OH Transfer: 0.530/0.528 → 0.598/0.598; fine-tune: 0.7510 → 0.9763

**§5.3** — Rewrote cross-agent narrative: removed the false 21.6pp claim, reframed as stage-dependent asymmetry (zero-shot gap 36.9pp closes to 2.2pp after FT), added deployment trade-off framing

**§5.5** — Complete rewrite as "Label Quality and cmd\_rep Coverage":
- Label audit discovery (stag rate 6.56%→21.45%, 21,898 labels flipped)
- Label quality as transfer bottleneck (FT 0.751→0.9763, 5% FT now beats old 50%)
- New Table 3: prevalence-matched ablation (3-LF 0.9763 vs 2-LF 0.6822, Δ=-29.4pp, McNemar p≈0)
- Coverage explanation (cmd\_rep fires 5.39%, precision 97.91%, 100% agreement on intersection, 4K→43K training data expansion)
- WS implications paragraph on coverage vs label refinement

---
