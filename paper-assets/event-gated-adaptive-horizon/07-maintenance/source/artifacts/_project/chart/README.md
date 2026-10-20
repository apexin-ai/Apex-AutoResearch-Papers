# Paper Figures — CoRL 2026

Diagnostic Analysis of Temporal Abstraction in World-Model RL.

## Figures

| File | Figure | Paper Section | Description |
|------|--------|---------------|-------------|
| `fig1_nve_diagnostic.py` | Fig 1 | Results (C2) | Normalized v/e ratio over training. >1.5× threshold separates trained vs untrained dt_emb (4/4). Diagnostic marker for delusional critic. |
| `fig2_eval_curves.py` | Fig 2 | Results (C1, C3, C6) | Eval return learning curves for all key configurations. Shows degradation (C1), untrained dt_emb protection (C3), and mitigation (C6). |
| `fig3_causal_chain.py` | Fig 3 | Discussion | Causal chain diagram: trained dt_emb → precise dt prediction → RSSM fidelity gap → pathological value overestimation → collapse. Includes feedback loop and mitigation point. |
| `fig4_multiseed.py` | Fig 4 | Results (C2) | Multi-seed robustness: 2×2 grid (trained/no dt_emb × eval/nve) across seeds 1-2. Shows stochastic collapse vs deterministic nve>1.5× threshold. |
| `fig5_rssm_fidelity.py` | Fig 5 + Table 1 | Discussion | RSSM prediction fidelity bar chart (obs_MSE, reward_MAE at dt=1 vs dt=2) and LaTeX table. |
| `fig6_mitigation.py` | Fig 6 | Results (C6) | Mitigation comparison: 008e_v3 (dt=1 imag, 95% baseline) vs 006 (dt=2 imag, collapse). Dual-panel with eval + nve. |

## Shared Style

- `fig_style.py` — Academic figure style (serif font, no grid, Nature/ICML convention). All figures import from here.

## Generated Artifacts

Each script produces `.pdf` + `.png`. Run: `python3 fig<N>_*.py`
- `fig5_rssm_fidelity.py` additionally produces `tab_rssm_fidelity.tex` (LaTeX table).

## Data Notes

- All data hardcoded from experiment registry as of 2026-05-15.
- 008e_v3 has 1 independent seed (seed=1); s2 (seed=2) RUNNING at 72K/105K.
- Baseline representative trajectory interpolated from sparse early checkpoints.
- Replace placeholder data with live W&B/registry pulls for final submission.
