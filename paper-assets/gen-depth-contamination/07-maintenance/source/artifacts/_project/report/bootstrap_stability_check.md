Files on cqa1-22115:
- results/bootstrap_stability/stability_results.json
- artifacts/bootstrap_stability_table.tex

Key findings:
- B=1K→5K: CI width shrinks ~1-3%
- B=5K→10K: <1% change, fully converged
- 13/14 verdicts stable across all B values
- Only instability: Mistral-7B 1v2 (AUC=0.590, CI upper at exactly θ=0.60)
- Borderline cases (LLaMA-8B, Gemma-2B) CI lower bounds stable to 4th decimal