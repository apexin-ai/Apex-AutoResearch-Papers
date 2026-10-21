# paper figure fig2 nve trajectory

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig2_nve_trajectory_20260515T102507_result.json`
- **Structured JSON:** [`2511c0e010ef5ce80c06.json`](../../sessions/25/2511c0e010ef5ce80c06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Done.** Generated `fig2_nve_trajectory` — top panel only.

**Outputs:**
- PDF: `artifacts/figures/paper/fig2_nve_trajectory.pdf`
- PNG: `artifacts/figures/paper/fig2_nve_trajectory.png`
- Script: `artifacts/figures/paper/fig2_nve_trajectory.py`
- Artifact: `art_20260515_993076` registered

**Bottom panel (actor_loss) skipped** — the SSH data extraction worker is stuck loading tools and couldn't connect to bjb1-45299. No data fabricated. The script is already wired to auto-detect `actor_loss_data.json` and render the two-panel layout when data becomes available — just drop the JSON file next to the script and re-run.

**Top panel shows the key result**: all 3 trained dt_emb experiments (008d, 009b, 009e — solid lines) cross the 1.5× threshold at some point, while both untrained controls (008f, 009c — dashed) stay below. 4/4 separating power. Mitigation experiments (008e_v3 — dash-dot) show mixed behavior.

---
