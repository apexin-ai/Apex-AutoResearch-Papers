# R3 .tex Verification Report

Date: 2026-05-16

## Summary

All 6 R3 items have been implemented in `docs/paper/*.tex`.

| Item | Status | Evidence |
|------|--------|----------|
| R3-N2 feature ablation text | ✅ Done | `atlas.tex:56` — full ablation paragraph: top-2 features reach 91.1%, top-5 reach 97.6% (76.5% vs 78.4%), with per-category breakdown (perplexity 76.6%, surprisal 73.2%, others ≤47%). Also referenced in `method.tex:45`. |
| R3-N3 SHAP replaces attention | ✅ Done | SHAP referenced 15+ times across `atlas.tex`, `discussion.tex`, `generalization.tex`, `introduction.tex`, `section_appendix.tex`. TreeExplainer analysis cited (`generalization.tex:118`). Three-way concordance (SHAP/Gini/permutation, Kendall's W=0.90) reported. No "attention weight" or "attention-based importance" found anywhere. |
| R3-N4 scope 界定 | ✅ Done | `introduction.tex:25` — contribution bullet explicitly states "Task formalization" as ordinal classification + EDD metric. `method.tex:26` — explicit scope limitation: "Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established." Paper is framed as task formalization + empirical study throughout. |
| R3-W1 d0 inflation headline | ✅ Done | Abstract line 5: reports 58.8–82.6% "when excluding the near-perfectly separable d0 class". Dedicated `\paragraph{d0 inflation of headline metrics.}` in `conclusion.tex:8-10`. Transfer tables explicitly note "d0 recall ≥89% inflates headline; d1–d3 mean: 45.9%". d0 accuracy is never presented as the headline claim — always qualified. |
| R3-W2 Discussion 扩展 | ✅ Done | `discussion.tex` is 47 lines with 7 substantive paragraphs: depth-graduated data curation (with LoRA PoC stats), provenance toolkit positioning, mixed-depth documents, adversarial robustness, scaling predictions, limitations/future directions. Significantly expanded beyond a typical 1-paragraph discussion. |
| R3-W4 exp ID 清理 | ✅ Done | grep for `mvp_pipeline`, `exp_id`, `run_` returns zero matches in all .tex files. All experiments referenced by descriptive names (e.g., "Pythia-1.4B nucleus", "cross-model leave-one-out") rather than raw IDs. |

## Notes

- .tex files exist only in local `docs/paper/`, not on remote server (no `paper/` dir in `/root/autodl-tmp/recursive_gen_depth_est/`)
- All R3 modifications appear well-integrated with supporting quantitative evidence
