# exp_005_stage0_h1_operator_repair proposal

Date: 2026-05-31
Project: ec_hte_codex_a
Status target: PREPARING only
Parent: `exp_002_gpu_dgp_grid`

This is a proposal/spec only. Do not run a formal experiment, do not launch `submit_training_job`, do not use `tmux` or `nohup`, do not occupy GPU, and do not modify `findings.md`.

## Decision context

Director D003 accepted `art_20260531_6a9e94` as the decision basis for `exp_002_gpu_dgp_grid`: exp002 is a grid-level operational hypothesis failure, not an execution failure, and it does not overturn `exp_001_bias_bound_mvp` single-DGP worst-case success. Stage1 formal launch remains blocked by C002 until the Stage0 correction operator and H1 grid diagnostic are repaired or explicitly waived by Director.

`art_20260531_0e5bc8` is advisory design guidance only under C003. It must not be cited as empirical support for H1/H2.

## Registry proposal

- Proposed exp_id: `exp_005_stage0_h1_operator_repair`
- Registry status, if created: `PREPARING` only
- Parent: `exp_002_gpu_dgp_grid`
- Hypothesis:
  `A repaired Stage0 H1 grid that uses a posterior-normalized P(G|Z) correction operator aligned to the estimand subgroup prior, explicitly varies subgroup-prior imbalance, and evaluates signed plus magnitude diagnostics will recover positive-vs-negative mechanism separation only when the original exp001-style prior-weighted posterior distortion is present.`

No `PENDING`, `RUNNING`, `DONE`, metric completion, or claim update should be recorded before Director approval and a later formal run.

## H1a

Hypothesis H1a: posterior-normalized operator `P(G|Z)` must align with the estimand subgroup-prior weighting.

Mechanism: `exp_001_bias_bound_mvp` uses a posterior-normalized operator based on `P(G|Z)` and subgroup prior, while `exp_002_gpu_dgp_grid` directly solves `transition.T`. For subgroup-varying error rates, observed-label GATEs are posterior-weighted by noisy-label prevalence. Directly inverting `P(Z_hat|G).T` is only equivalent in special balanced cases.

Required design:

- Compute true subgroup prior `pi_g`.
- Compute row-stochastic confusion `C[g,h] = P(Z_hat=h | G=g)`.
- Compute observed-label prevalence `q_h = sum_g pi_g C[g,h]`.
- Compute posterior mixing `M[h,g] = pi_g C[g,h] / q_h`.
- Define the primary repaired global correction as `posterior_global_prior_weighted`, solving `observed_gate_by_Zhat = M true_gate_by_G`.
- Keep current `transition_transpose_inverse` as an explicit negative-control baseline, not as the repaired operator.
- Report oracle and estimated versions separately for both operators.

H1a metric keys:

- `h1a.posterior_global_minus_uncorrected_gate_rmse`
- `h1a.posterior_global_worse_rate`
- `h1a.posterior_minus_transition_inverse_gate_rmse`
- `h1a.posterior_operator_alignment_error`
- `h1a.estimated_posterior_minus_oracle_posterior_gate_rmse`

H1a success requires the repaired posterior operator to improve the intended mechanism separation relative to the current transition-transpose inverse, with bootstrap CI support defined below.

## H1b

Hypothesis H1b: the worst-case global-correction mechanism needs subgroup-prior imbalance, not only signed error-CATE coupling.

Mechanism: `exp_001_bias_bound_mvp` used imbalanced subgroup probabilities and created prior-weighted posterior distortion. `exp_002_gpu_dgp_grid` sampled true subgroups uniformly, weakening the pooled global correction's majority/minority leverage.

Required design:

- Add subgroup-prior axis: `uniform`, `moderate_imbalance`, `exp001_like_imbalance`.
- Use deterministic prior templates per `k` and record them in each condition row.
- Keep `uniform` cells as negative-control cells for the prior-leverage mechanism.
- For `k=3`, proposed prior templates:
  - `uniform`: `[0.3333, 0.3333, 0.3334]`
  - `moderate_imbalance`: `[0.50, 0.30, 0.20]`
  - `exp001_like_imbalance`: collapse/renormalize the exp001 shape to high-majority plus minority high-effect groups.
- For `k=6`, proposed prior templates:
  - `uniform`: six equal classes
  - `moderate_imbalance`: `[0.30, 0.22, 0.16, 0.13, 0.11, 0.08]`
  - `exp001_like_imbalance`: one large low-error/low-effect majority plus several smaller higher-error/higher-effect groups.

H1b metric keys:

- `h1b.prior_imbalance_interaction_positive_minus_negative_rate_diff`
- `h1b.uniform_prior_positive_minus_negative_rate_diff`
- `h1b.imbalanced_prior_positive_minus_negative_rate_diff`
- `h1b.posterior_distortion_norm_by_prior_axis`
- `h1b.prior_weighted_bias_delta`

H1b success requires positive-vs-negative separation to strengthen monotonically or at least materially from `uniform` to imbalanced prior settings, with `uniform` allowed to be weak or null.

## H1c

Hypothesis H1c: `bias_bound_score` must be signed or decomposed into signed and magnitude components.

Mechanism: exp002's magnitude-only diagnostic used absolute coupling and therefore could not distinguish positive and negative correlation controls. A repaired diagnostic must preserve the sign of error-CATE alignment while still reporting magnitude.

Required design:

- Replace single magnitude-only `bias_bound_score` with:
  - `signed_bias_alignment_score`
  - `bias_alignment_magnitude_score`
  - `signed_x_magnitude_decomposition`
- Define signed score against centered subgroup error and centered CATE contrast:
  `mean_g((error_g - weighted_mean_error) * (tau_g - weighted_mean_tau))`.
- Report an absolute/magnitude score separately:
  `mean_g(abs(error_g - weighted_mean_error) * abs(tau_g - weighted_mean_tau))`.
- Primary H1 diagnostic must use the signed score for directionality.
- Magnitude score is secondary and may explain severity but cannot decide positive-vs-negative direction.

H1c metric keys:

- `h1c.signed_bias_alignment_vs_global_worse_spearman`
- `h1c.signed_bias_alignment_auc`
- `h1c.magnitude_bias_alignment_vs_global_worse_spearman`
- `h1c.signed_minus_magnitude_rank_delta`
- `h1c.positive_negative_signed_score_separation`

H1c success requires the signed diagnostic to rank repaired posterior-global-worse conditions in the expected direction; the magnitude-only diagnostic is not sufficient.

## planned_conditions vs conditions

Use two names in the repaired spec:

- `matched_condition_pairs`: condition identities before expanding correlation direction.
- `observed_directional_conditions`: condition rows after expanding `correlation_direction in {positive, negative}`.

The original exp002 count is:

`3 n_values * 2 subgroup_counts * 4 expert_budgets * 2 misclassification_heterogeneity * 2 cate_heterogeneity * 2 correlation_directions = 192 observed conditions`.

Equivalently:

`3 * 2 * 4 * 2 * 2 = 96 matched condition pairs`, expanded by two directions to `192 observed_directional_conditions`.

For exp005, add `subgroup_prior_axis in {uniform, moderate_imbalance, exp001_like_imbalance}`. The proposed count becomes:

- `matched_condition_pairs = 96 * 3 = 288`
- `observed_directional_conditions = 288 * 2 = 576`
- `replications_per_observed_condition = 200`
- `planned_replications = 576 * 200 = 115200`

Each observed row must include:

- `condition_pair_id`
- `directional_condition_id`
- `correlation_direction`
- `subgroup_prior_axis`
- `subgroup_priors`
- `operator_family`
- `diagnostic_family`

## registry/matrix mapping

Initial registry and matrix status should be `planned`/`preparing` only. No new metric should be marked complete.

Recommended new plan entry:

- `plan_005_stage0_h1_operator_repair`
- claim: `C_H1_GLOBAL_CORRECTION_WORSE`
- registry_id: `exp_005_stage0_h1_operator_repair`
- role: `repair`
- priority: `P0`
- deps: `plan_002_h1_gpu_dgp_grid`

Recommended matrix cells:

| target_id | row | col | metric_key | exp_id | source | initial_status |
|---|---|---|---|---|---|---|
| `C_H1_GLOBAL_CORRECTION_WORSE` | `exp_005_stage0_h1_operator_repair` | `posterior_operator_vs_transition_inverse` | `h1a.posterior_minus_transition_inverse_gate_rmse` | `exp_005_stage0_h1_operator_repair` | `artifacts/exp_005_stage0_h1_operator_repair/formal/condition_metrics.jsonl` | `planned` |
| `C_H1_GLOBAL_CORRECTION_WORSE` | `exp_005_stage0_h1_operator_repair` | `prior_imbalance_mechanism` | `h1b.prior_imbalance_interaction_positive_minus_negative_rate_diff` | `exp_005_stage0_h1_operator_repair` | `artifacts/exp_005_stage0_h1_operator_repair/formal/summary.json` | `planned` |
| `T_STAGE0_DGP_GRID` | `operator_repair_grid_all_conditions` | `signed_bias_alignment_rank_corr` | `h1c.signed_bias_alignment_vs_global_worse_spearman` | `exp_005_stage0_h1_operator_repair` | `artifacts/exp_005_stage0_h1_operator_repair/formal/condition_metrics.jsonl` | `planned` |
| `T_STAGE0_DGP_GRID` | `operator_repair_grid_all_conditions` | `magnitude_diagnostic_control` | `h1c.magnitude_bias_alignment_vs_global_worse_spearman` | `exp_005_stage0_h1_operator_repair` | `artifacts/exp_005_stage0_h1_operator_repair/formal/condition_metrics.jsonl` | `planned` |
| `T_STAGE0_DGP_GRID` | `operator_repair_grid_all_conditions` | `oracle_estimated_gap_repaired_operator` | `h1a.estimated_posterior_minus_oracle_posterior_gate_rmse` | `exp_005_stage0_h1_operator_repair` | `artifacts/exp_005_stage0_h1_operator_repair/formal/summary.json` | `planned` |

Do not overwrite exp002 matrix semantics. In `C_H1_GLOBAL_CORRECTION_WORSE`, `exp_002_gpu_dgp_grid` remains hypothesis/plan negative.

## success rules

All success rules require `minimum_replications_per_observed_condition >= 200` and bootstrap 95% CIs with `bootstrap_iterations >= 1000`.

H1a success:

- `h1a.posterior_minus_transition_inverse_gate_rmse < 0`, with bootstrap 95% CI upper bound `< 0`.
- `h1a.posterior_operator_alignment_error` must be near numerical tolerance under oracle priors/confusion; otherwise the operator implementation is invalid.
- Repaired posterior-global results must be reported separately for oracle and estimated confusion/prior inputs.

H1b success:

- `h1b.imbalanced_prior_positive_minus_negative_rate_diff - h1b.uniform_prior_positive_minus_negative_rate_diff > 0`, with bootstrap 95% CI lower bound `> 0`.
- `h1b.posterior_distortion_norm_by_prior_axis` should increase from `uniform` to imbalanced axes.
- If only `exp001_like_imbalance` succeeds, the claim must be narrowed to prior-leveraged worst-case settings.

H1c success:

- `h1c.signed_bias_alignment_vs_global_worse_spearman >= 0.50`, with bootstrap 95% CI lower bound `> 0`.
- `h1c.positive_negative_signed_score_separation > 0`, with bootstrap 95% CI lower bound `> 0`.
- Magnitude-only diagnostics may be reported as severity diagnostics but cannot alone support H1.

Overall exp005 success:

- H1a, H1b, and H1c all pass.
- Positive-vs-negative repaired posterior-global worse-rate difference is at least 20 percentage points in the imbalanced-prior axes, with bootstrap 95% CI lower bound `> 0`.
- Estimated-global noise remains separately quantified and does not explain the effect: `h1a.estimated_posterior_minus_oracle_posterior_gate_rmse` is reported with CI.

## negative rules

H1a negative:

- Posterior-normalized correction does not beat the current `transition_transpose_inverse`, or operator alignment checks fail.
- If alignment checks fail, classify as implementation/spec failure and do not interpret as substantive H1 evidence.

H1b negative:

- Prior imbalance does not increase positive-vs-negative separation versus uniform prior.
- If uniform and imbalanced priors both fail with a valid posterior operator, the exp001 mechanism should be treated as narrower than the proposed grid claim.

H1c negative:

- Signed diagnostic does not rank global-worse conditions in the expected direction, or its CI includes nonpositive rank/separation.
- If signed and magnitude diagnostics disagree, signed directionality controls claim status; Director review is required before Stage1.

Overall negative:

- If any of H1a/H1b/H1c is negative, do not unblock Stage1 formal automatically.
- Preserve `exp_001_bias_bound_mvp` as single-DGP worst-case evidence and `exp_002_gpu_dgp_grid` as grid-level negative.

## stop conditions

Stop before formal launch if:

- Director has not approved `exp_005_stage0_h1_operator_repair`.
- Registry status would need to move beyond `PREPARING`.
- Any command would use `submit_training_job`, `tmux`, `nohup`, or GPU allocation before approval.
- Required code paths cannot emit `condition_pair_id`, `directional_condition_id`, and provenance fields.
- The operator identity test fails on a deterministic toy case.
- Bootstrap or replication settings fall below the minimum formal thresholds.

Continue Stage1 only if:

- exp005 formal run is approved, executed later, and marked `DONE/success`.
- H1a/H1b/H1c pass together.
- Director explicitly updates C002 or records an equivalent waiver.

Continue blocked if:

- exp005 is not run.
- exp005 is negative or mixed.
- exp005 outputs are missing matrix provenance or bootstrap CIs.

Director manual decision required if:

- H1a passes but H1b or H1c is mixed.
- Only `exp001_like_imbalance` cells pass and uniform/moderate cells fail.
- Estimated correction differs materially from oracle correction, implying expert-budget noise may dominate after repair.
- Stage1 is requested before exp005 formal evidence exists.

## commands (not executed)

Formal command draft only:

```bash
cd /home/root/ec_hte
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
CUDA_VISIBLE_DEVICES=0 python repro/exp_005_stage0_h1_operator_repair/run_operator_repair_grid.py \
  --config configs/exp_005_stage0_h1_operator_repair.json \
  --output-dir artifacts/exp_005_stage0_h1_operator_repair/formal \
  --device cuda
```

CPU-only smoke command draft only:

```bash
cd /home/root/ec_hte
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
python repro/exp_005_stage0_h1_operator_repair/run_operator_repair_grid.py \
  --config configs/exp_005_stage0_h1_operator_repair.json \
  --output-dir artifacts/exp_005_stage0_h1_operator_repair/smoke \
  --device cpu \
  --limit-condition-pairs 4 \
  --replications-per-condition 2 \
  --smoke
```

These commands must remain text in this proposal until Director approval. They were not executed by this worker.

## provenance fields

Formal spec provenance draft:

- server: `seetacloud-38274`
- account: `root`
- project_root: `/home/root/ec_hte`
- data_path: `synthetic DGP generated in-run; outputs under /home/root/ec_hte/artifacts/exp_005_stage0_h1_operator_repair/formal`
- output_path: `/home/root/ec_hte/artifacts/exp_005_stage0_h1_operator_repair/formal`
- log_path: `/home/root/ec_hte/artifacts/exp_005_stage0_h1_operator_repair/logs/exp_005_stage0_h1_operator_repair_<timestamp>.log`
- checkpoint_path: `/home/root/ec_hte/artifacts/exp_005_stage0_h1_operator_repair/checkpoints/no_model_checkpoint_required.txt`
- seed: `20260605`
- bootstrap_seed: `20260606`
- model_name: `synthetic_stage0_operator_repair_no_trained_model`
- matched_condition_pairs: `288`
- observed_directional_conditions: `576`
- replications_per_observed_condition: `200`
- planned_replications: `115200`
- expected_runtime: `proposal estimate <= 4 GPU-hours on seetacloud-38274/root/cuda:0; CPU smoke < 2 minutes`
- disk_estimate: `proposal estimate < 750 MB JSON/JSONL/CSV; no model checkpoint or external dataset`

## minimal code changes

Do not implement formal code in this proposal step. If Director approves implementation, the minimal change list is:

- Add `configs/exp_005_stage0_h1_operator_repair.json` with grid axes, operator families, prior axes, diagnostic families, and matrix mappings.
- Add `repro/exp_005_stage0_h1_operator_repair/run_operator_repair_grid.py` as a new script rather than mutating exp002 formal code in place.
- Add a shared correction utility, preferably `repro/common/misclassification_operators.py`, containing:
  - `posterior_mixing_from_confusion(C, pi)`
  - `solve_posterior_gate(observed_gate_by_zhat, posterior_mixing, ridge)`
  - `solve_transition_transpose_inverse(...)` as a named negative-control baseline
- Add a diagnostic utility, preferably `repro/common/bias_alignment.py`, containing signed and magnitude diagnostic functions.
- Add deterministic unit tests or smoke assertions for:
  - posterior rows sum to 1,
  - observed-label prevalence normalization handles small `q_h`,
  - posterior operator equals direct solve only in documented balanced special cases,
  - signed diagnostic changes sign under positive vs negative correlation while magnitude remains similar.

File header requirement: every new script/config should state `Proposal-only Stage0/H1 repair for exp_005; do not use as completed evidence until formal Director-approved run exists.`

Docstring requirement: every non-obvious operator/diagnostic function must state the estimand, matrix orientation, expected input shapes, and whether subgroup priors are required.

Pseudo-code sketch:

```python
def posterior_mixing_from_confusion(confusion_g_to_h, subgroup_prior, eps=1e-12):
    """Return M[h, g] = P(G=g | Z_hat=h) for observed-label GATE correction."""
    q_h = subgroup_prior @ confusion_g_to_h
    return (subgroup_prior[None, :] * confusion_g_to_h.T) / q_h[:, None].clip(min=eps)

def signed_bias_alignment(error_rate_g, tau_g, weight_g):
    """Signed prior-weighted alignment between subgroup error and CATE contrast."""
    err_c = error_rate_g - (weight_g * error_rate_g).sum()
    tau_c = tau_g - (weight_g * tau_g).sum()
    return (weight_g * err_c * tau_c).sum()
```

## findings/report boundary

Before exp005 formal execution:

- `exp_001_bias_bound_mvp` remains single-DGP worst-case evidence.
- `exp_002_gpu_dgp_grid` remains grid-level negative for the previous operational criterion.
- exp005 proposal/spec does not support any new H1/H2 empirical claim.
- `art_20260531_0e5bc8` remains advisory only.
- `findings.md` must not be modified.

After a future approved exp005 run, any report must still separate:

- posterior operator repair evidence,
- prior imbalance mechanism evidence,
- signed diagnostic evidence,
- estimated-vs-oracle finite-sample noise,
- Stage1 unblock decision.
