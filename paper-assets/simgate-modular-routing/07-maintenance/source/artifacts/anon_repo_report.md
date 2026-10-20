# Anonymous GitHub Repository Report

## Repository URL
https://github.com/anonymous-nlp-2026/simgate-modular-routing

## Commit
- Hash: `91bcdb444fa84b2e5354c1d5e27c982965056aca`
- Author: `Anonymous <anonymous@example.com>`
- Message: `Anonymous submission for EMNLP 2026 ARR`

## Summary
- Total files: **211**
- Repo size: ~2.6MB (down from 11GB original)
- Branch: `main`

## Anonymization Verification

| Check | Result |
|-------|--------|
| `caoxiaoyu` / `caoxiaoyuyuyuyuyu` | PASS — not found |
| `1844118046@qq.com` | PASS — not found |
| `周俊伟` / `贾骁涵` / `曹晓玉` | PASS — not found |
| `ghp_` tokens | PASS — not found |
| `sk-` API keys | PASS — no real keys (only `task-type` substrings) |
| `hf_` tokens | PASS — only variable name `hf_cache_dirs` |
| University/lab names | PASS — not found |
| Server paths (`/root/autodl-tmp/`) | PASS — replaced with relative paths |
| `wandb entity` | PASS — no entity set in code |
| Files > 10MB | PASS — none |
| Paper `\author{}` | PASS — set to `Anonymous` |
| `.git/config` token | PASS — removed after push |

## Deleted Content
- `wandb/` — experiment tracking logs
- `data/` — collected trajectory data
- `results/` — experiment outputs and checkpoints
- `checkpoints/` — model weights (LoRA adapters)
- `outputs/`, `logs/` — runtime outputs
- `artifacts/` — analysis outputs
- `notes/`, `docs/` — personal notes, duplicate paper source
- `figures/` — intermediate figure files
- All `__pycache__/`, `*.pyc`, `*.pt`, `*.bin`, `*.safetensors`, `*.log`, `*.bak` files
- `.git/` — original history

## Retained Content
- `src/` — core source code (counterfactual labeling, training, evaluation)
- `scripts/` — experiment scripts and analyses
- `guided_router/` — decomposition-guided router module
- `paper/` — LaTeX source (already anonymized with `\author{Anonymous}`)
- `crafter_pilot/` — Crafter environment pilot code
- `analysis/` — dose-response analysis scripts
- Root-level `*.py` and `*.sh` experiment scripts

## File List

```
.gitignore
README.md
analysis/dose_response_figure.py
analysis/per_task_dose_response.py
analysis/retry_determinism_audit.py
analysis/unify_dose_response_metrics.py
analyze_retry_dose_response.py
auto_start_vllm.sh
auto_start_vllm2.sh
corrected_eval.py
crafter_pilot/config.py
crafter_pilot/episode_runner.py
crafter_pilot/heuristic_agent.py
crafter_pilot/heuristic_agent_v8.py
crafter_pilot/heuristic_agent_v9.py
crafter_pilot/llm_agent.py
crafter_pilot/seed_patch.py
crafter_pilot/test_agent.py
crafter_pilot/text_wrapper.py
eval_ablation_b_gen.py
eval_classification.py
eval_multiseed_gen.py
eval_v4_router.py
guided_router/README.md
guided_router/__init__.py
guided_router/cluster_bootstrap.py
guided_router/cluster_bootstrap_full.py
guided_router/compute_sci.py
guided_router/config.py
guided_router/cross_model_eval.py
guided_router/daf_bootstrap.py
guided_router/eval_episode.py
guided_router/framework_draft.md
guided_router/loto_eval.py
guided_router/math_power_analysis.py
guided_router/partial_corr.py
guided_router/router.py
guided_router/run_guided_router.py
guided_router/task_type_classifier.py
paper/abstract.tex
paper/acl.sty
paper/acl_natbib.bst
paper/conclusion.tex
paper/discussion.tex
paper/experiments.tex
paper/figures/fig1_daf_scatter.pdf
paper/figures/gen_fig1.py
paper/figures/gen_pipeline.py
paper/figures/gen_signal_reversal.py
paper/figures/pipeline_overview.pdf
paper/figures/signal_reversal.pdf
paper/introduction.tex
paper/main.pdf
paper/main.tex
paper/method.tex
paper/references.bib
paper/related_work.tex
run_1_7b_reeval.py
run_corrected_eval_gpu0.sh
run_corrected_eval_gpu1.sh
run_death_rate_0_5b.py
run_dose_response_full.sh
run_gpu0_v3.sh
run_grounding_filter_ablation.py
run_grounding_filter_wrapper.sh
run_pilot50.sh
run_plan001b_gpu0.sh
run_plan001b_gpu1.sh
run_prescreening_gpu0.sh
run_prescreening_gpu1.sh
run_reflexion_dose_response.py
run_reflexion_dr_wrapper.sh
run_reflexion_n345_wrapper.sh
run_remaining.sh
run_retry_dose_response.py
run_seed44_45.sh
scripts/ (48 files — analysis, experiment launchers, bootstrap)
src/ (50 files — core pipeline, training, evaluation)
w3_confusion_analysis.py
```

## Items for Director Review

1. **`paper/` directory included** — Contains full LaTeX source + compiled PDF. Author is already set to `Anonymous`. Including paper source in code repo is common for ARR, but flagging in case you prefer to exclude it.
2. **`guided_router/framework_draft.md`** — Contains formal mathematical framework draft. No identifying info, but is a detailed research document.
3. **No `requirements.txt`** — The original project did not have a root-level `requirements.txt`. Key dependencies are listed in README instead. Consider adding one if reviewers need it.
