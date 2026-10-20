# Research conversation: CRITICAL: Rewrite and rerun Exp-D Conjecture 1 verification with analytic plim ### Problem The current `exp_d_conjecture

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a8ae618b752846327.jsonl`
- **Structured JSON:** [`5aacd4edce54ed5b08fe.json`](../../sessions/5a/5aacd4edce54ed5b08fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-22T12:18:00.011Z_

## CRITICAL: Rewrite and rerun Exp-D Conjecture 1 verification with analytic plim

### Problem
The current `exp_d_conjecture_verify.py` computes probability limits (plim) using sufficient statistics estimated from N=5M Monte Carlo simulation. This introduces sampling noise O(1/√N) ≈ 0.0004, which at MONO_TOL=1e-8 generates false "monotonicity violations". The 141,514 violations found are almost certainly numerical artifacts.

### Your Task
Create `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py` that computes plim ANALYTICALLY (zero sampling noise) and reruns the verification.

### How to compute analytic plim for each topology

The plim computation structure is the same as in the original code (solve E[Z'Z]^{-1} E[Z'Y] or Wald ratio), but the sufficient statistics (p_A, E[TD_k], E[YD_k], E[T], E[T²], E[TY], etc.) must be computed from population formulas, not from simulated data.

**Key principle**: For each topology, the DGP defines joint distributions of (T, Y, A). The sufficient statistics are population expectations that can be computed analytically or via high-precision numerical integration.

#### 1. Confounding (A → T, A → Y, T → Y) — FULLY ANALYTIC
```
A ~ Categorical(p_A)
T = Σ α_j D_j + ε_T,  ε_T ~ N(0, σ_T²)
Y = τT + Σ β_j D_j + ε_Y,  ε_Y ~ N(0,1)

Population moments:
p_A[k] = given
E[T] = Σ_{j=1}^{K-1} α_j p_j
E[T²] = Σ_{j=1}^{K-1} α_j² p_j + σ_T² + (Σ α_j p_j)² - Σ α_j² p_j²  
       ... actually more carefully: E[T²] = E[(Σ α_j D_j)² + 2(Σ α_j D_j)ε_T + ε_T²]
       = E[(Σ α_j D_j)²] + σ_T²  (cross term is 0)
       = Σ_{j} α_j² p_j + σ_T²   (since D_j D_k = 0 for j≠k, D_j² = D_j)
       Wait no, E[(Σ α_j D_j)²] = Σ_j α_j² p_j because D_j²=D_j and D_j D_k=0

But this is wrong if you include j from 1 to K-1 and p_j is P(A=j+1)... Let me be precise:
Actually D_j = 1(A=j) for j=1,...,K-1 with ref category 0.
E[D_j] = p_j (where p_j = P(A=j) for j=1,...,K-1)
E[D_j²] = p_j, E[D_j D_k] = 0 for j≠k

So E[(Σ_{j=1}^{K-1} α_j D_j)²] = Σ_j α_j² p_j
E[T²] = Σ_j α_j² p_j + σ_T²
E[TD_k] = α_k p_k + σ_T² * ... no wait
E[T D_k] = E[(Σ_j α_j D_j + ε_T) D_k] = α_k p_k  (since ε_T ⊥ D_k, and D_j D_k = 0 for j≠k)
E[Y] = τ E[T] + Σ β_j p_j
E[TY] = τ E[T²] + Σ_j β_j E[T D_j] = τ E[T²] + Σ_j β_j α_j p_j
E[Y D_k] = τ E[T D_k] + β_k p_k = τ α_k p_k + β_k p_k
```

Reference: The Exp-E code at `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py` has `plim_confounding()` (lines 48-72) with the analytic formulas for K=3. Generalize to arbitrary K.

#### 2. Exposure (A → Y) — FULLY ANALYTIC  
```
A ~ Categorical(p_A)
Y = β₀ + Σ_{j=1}^{K-1} β_j D_j + ε_Y

p_A[k] = given
E[Y D_k] = β_k p_k for k=1,...,K-1; E[Y D_0] = β₀ p₀
E[Y] = β₀ + Σ β_j p_j
```
Reference: Exp-E `plim_exposure()` (lines 79-90). Generalize to arbitrary K.

#### 3. Mediation (T → A → Y, T → Y) — ANALYTIC (T is binary)
```
T ~ Bernoulli(0.5)
A | T ~ Categorical(softmax(γ + δ*T))
Y = τ*T + f(A) + ε_Y

Since T ∈ {0,1}, all moments are weighted averages over T=0 and T=1:
P(A=k) = 0.5 * softmax(γ)[k] + 0.5 * softmax(γ+δ)[k]
E[T D_k] = 0.5 * softmax(γ+δ)[k]  (T=1 contributes, T=0 gives 0)
E[T] = 0.5, E[T²] = 0.5
E[Y D_k] = 0.5*(softmax(γ)[k]*(0 + β_k)) + 0.5*(softmax(γ+δ)[k]*(τ + β_k))
         = 0.5*β_k*softmax(γ)[k] + 0.5*(τ+β_k)*softmax(γ+δ)[k]
E[TY] = 0.5*E[Y|T=1] = 0.5*(τ + Σ_k β_k softmax(γ+δ)[k])
```

#### 4. Collider (T → A ← Y, T → Y) — GAUSS-HERMITE
```
T ~ N(0,1), Y = τT + ε_Y (ε_Y ~ N(0,1), ε_Y ⊥ T)
A | T,Y ~ Categorical(softmax(δ_T * T + δ_Y * Y))

Reparametrize: Y = τT + ε_Y, so (T, ε_Y) are independent standard normals.
A depends on (T, ε_Y) through softmax((δ_T + τ*δ_Y)*T + δ_Y*ε_Y)

Use 2D Gauss-Hermite quadrature (100 points per dim should be plenty):
P(A=k) = E_{T,ε}[softmax(...)_k]  ← 2D integral
E[T D_k] = E_{T,ε}[T * softmax(...)_k]
E[Y D_k] = E_{T,ε}[(τT+ε) * softmax(...)_k]
E[T] = 0, E[T²] = 1, E[TY] = τ, E[Y] = 0
```

#### 5. M-bias (U₁ → T, U₁ → A, U₂ → A, U₂ → Y, T → Y) — GAUSS-HERMITE
```
U₁ ~ N(0,1), U₂ ~ N(0,1)
T = δ_coef * U₁ + η (η ~ N(0,1))
Y = τT + λU₂ + ε_Y (ε_Y ~ N(0,1))
A | U₁,U₂ ~ Categorical(softmax(a₁*U₁ + a₂*U₂))

Use 2D Gauss-Hermite over (U₁, U₂):
P(A=k) = E_{U1,U2}[softmax(a1*U1 + a2*U2)_k]

For moments involving T: T = δ_coef*U₁ + η, η independent
E[T D_k] = δ_coef * E_{U1,U2}[U1 * softmax(...)_k]  (since E[η D_k] = 0)
E[T²] = δ_coef² + 1 (= Var(T))
E[T] = 0
E[TY] = τ*E[T²] + λ*δ_coef*E[U₁ U₂] = τ*(δ_coef²+1) (since U₁⊥U₂)
E[Y D_k] = τ*E[T D_k] + λ*E_{U1,U2}[U2 * softmax(...)_k]
```

#### 6. Front-door (T → M → Y, U → T, U → Y, M → M*) — GAUSS-HERMITE 1D
```
U ~ N(0,1), T = α_U*U + η (η ~ N(0,1))
M | T ~ Categorical(softmax(γ + δ*T))
Y = f(M) + λ*U + ε_Y

T has a continuous distribution N(0, α_U²+1).
Use 1D Gauss-Hermite over T (after computing T's distribution):
P(M=k) = E_T[softmax(γ + δT)_k]
E[T D_k] = E_T[T * softmax(γ + δT)_k]

But Y depends on M and U. The regression Y ~ 1 + T + D*₁ + ... needs:
E[Y D_k] = f(k)*P(M=k) + λ*E[U D_k]

E[U D_k] = E[U * 1(M=k)] = E_T[E[U|T] * softmax(γ+δT)_k]
Since U = (T - η)/α_U and T = α_U*U + η:
E[U|T] = α_U*T/(α_U²+1)  (regression of U on T for jointly normal)
So E[U D_k] = α_U/(α_U²+1) * E_T[T * softmax(...)_k]

T ~ N(0, σ_T²) where σ_T² = α_U² + 1. Use GH quadrature.
E[TY] = τ*E[T²] + λ*E[TU] + E[T f(M)]
E[TU] = α_U (since Cov(T,U) = α_U*Var(U) = α_U, both mean 0)
E[T f(M)] = E_T[T * Σ_k β_k softmax(γ+δT)_k] = 1D GH integral
```

#### 7. IV (Z → A, U → A, U → Y, A → Y) — ANALYTIC (Z is binary)
```
Z ~ Bernoulli(0.5), U ~ N(0,1)
A | Z,U ~ Categorical(softmax(g + dZ*Z + dU*U))
Y = f(A) + λU + ε_Y

Wald estimator: τ̂ = RF / FS_1 where:
RF = E[Y|Z=1] - E[Y|Z=0]
FS_k = P(A=k|Z=1) - P(A=k|Z=0)

Since Z is binary, need 1D GH quadrature over U for each Z value:
P(A=k|Z=z) = E_U[softmax(g + dZ*z + dU*U)_k]
E[Y|Z=z] = Σ_k β_k P(A=k|Z=z) + λ*E[U] = Σ_k β_k P(A=k|Z=z)

FS_star = C @ FS  (misclassified first stage)
τ̂(C) = RF / FS_star[1]
```

### Implementation structure

```python
#!/usr/bin/env python3
"""Exp-D v2: Conjecture 1 verification with analytic plim (zero sampling noise)"""

import numpy as np
from numpy.polynomial.hermite_e import hermegauss  # probabilist's Hermite
import json, time
from scipy.optimize import minimize as scipy_minimize

# Gauss-Hermite quadrature setup
N_GH = 100  # points per dimension — gives machine precision for smooth integrands
gh_x, gh_w = hermegauss(N_GH)  # nodes and weights for N(0,1)
# Note: numpy's hermegauss uses probabilist's convention, 
# so ∫ f(x) exp(-x²/2)/√(2π) dx ≈ Σ w_i f(x_i)
# Actually check: np.polynomial.hermite_e.hermegauss gives nodes for 
# weight function exp(-x²/2), so ∫ f(x) exp(-x²/2) dx ≈ Σ w_i f(x_i)
# To get E[f(X)] for X~N(0,1): E[f(X)] = (1/√(2π)) Σ w_i f(x_i)
# OR use scipy.special.roots_hermite which uses physicist's convention
# Better to use: from numpy.polynomial.hermite import hermgauss
# which gives weight exp(-x²), so ∫ f(x) exp(-x²) dx ≈ Σ w_i f(x_i)
# For N(0,1): E[f(X)] = (1/√π) Σ w_i f(x_i √2)

# USE scipy for clarity:
from scipy.special import roots_hermite
gh_x_raw, gh_w_raw = roots_hermite(N_GH)
# These satisfy: Σ w_i f(x_i) ≈ ∫ f(x) exp(-x²) dx
# For N(0,1) expectation: E[f(X)] = (1/√π) Σ w_i f(x_i * √2)
GH_X = gh_x_raw * np.sqrt(2)  # rescaled nodes
GH_W = gh_w_raw / np.sqrt(np.pi)  # rescaled weights so Σ w_i f(x_i) = E_N(0,1)[f]

# Config
K_VALUES = [3, 5, 7]
N_RANDOM = 10_000
DELTA_STEP = 0.01
MONO_TOL = 1e-12
SEED = 12345
ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure', 'mbias', 'iv', 'frontdoor']

# ... implement analytic sufficient stats and plim for each topology ...
# ... then the same verification loop as original ...
```

### For the plim computation given sufficient stats
Keep the same `plim_ols_with_T`, `plim_ols_exposure`, `plim_iv_single` functions from the original code — they correctly compute plim from sufficient stats. Just replace how the sufficient stats are computed (analytic instead of simulated).

### Create an AnalyticSuffStats class
Instead of simulating data and computing empirical moments, compute population moments analytically:

```python
class AnalyticSuffStats:
    """Population moments computed analytically — zero sampling noise."""
    def __init__(self, K, has_T=True):
        self.K = K
        self.has_T = has_T
        # Will be populated by topology-specific methods
        self.p_A = None  # K-vector
        self.E_Y = None
        self.E_YD = None  # K-vector
        if has_T:
            self.E_T = None
            self.E_T2 = None
            self.E_TY = None
            self.E_TD = None  # K-vector
```

### Key parameters
Use the EXACT same DGP parameters as the original Exp-D (imported from the same pools). The file `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify.py` has them at lines 47-59.

### Verification logic
Same as original:
1. For each topology, K, and random C₀: compute bias curve B(δ) = plim(C(δ)) - τ_true
2. Check monotonicity: |B(δ_{i+1})| >= |B(δ_i)| (non-dec) or <= (non-inc)
3. Count violations exceeding MONO_TOL=1e-12
4. Record worst violation magnitude

### Adversarial search
Same as original but with analytic plim. 100 starts per (topology, K, delta_pair).

### Output
Save to `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_results_v2.json` with the same structure as the original.

### Run the script
After writing it, run it:
```bash
cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts
python3 exp_d_conjecture_verify_v2.py
```

This should complete in a few minutes since there's no simulation (all computations are matrix operations + GH quadrature).

### Report
Print and report:
- For each topology: violation count at K=3,5,7 and worst magnitude
- Whether adversarial search found any counterexamples
- Comparison with original results
- Specifically: did non-IV topologies go to zero violations? Did IV violations change?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3f772f34-432b-4b73-8d6a-c54bf571a4ba",
  "agentId": "a8ae618b752846327",
  "type": "user",
  "uuid": "75b269b5-9130-4129-952a-3890b8a41512",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T12:18:00.018Z_

```json
{
  "parentUuid": "75b269b5-9130-4129-952a-3890b8a41512",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "95b6fdde-1aa3-4786-beb6-bf3908656b05",
  "timestamp": "2026-05-22T12:18:00.018Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

---

### Assistant

_source line 3 · 2026-05-22T12:18:03.141Z_



I'll start by reading the original Exp-D script and the Exp-E reference code to understand the existing implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95b6fdde-1aa3-4786-beb6-bf3908656b05",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbPLRRiaih6R9K6iCT4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd142e87-a8f8-4dec-a712-5a03957f02ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HZ1ujQRNgEjGqghLphAbg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35069,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35069,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T12:18:03.622Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MNQY2Q6xHRKSszg8HJRhwc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd142e87-a8f8-4dec-a712-5a03957f02ce",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbPLRRiaih6R9K6iCT4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8acbca24-6760-4d40-a33a-ae34405f268a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HZ1ujQRNgEjGqghLphAbg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35069,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35069,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T12:18:03.633Z_

<details><summary>↩ Tool result · `toolu_01MNQY2Q6xHRKSszg8HJRhwc`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Exp-D: Conjecture 1 Extended Verification (Envelope Monotonicity)
4	
5	Part 1: 10,000 random Dirichlet(1,...,1) C0 per (topology, K) -- 210,000 total tests
6	Part 2: Adversarial search via scipy.minimize for K in {3, 5} -- 500 starts per config
7	
8	Conjecture 1:
9	  |B(delta)| non-decreasing for {confounding, mediation, exposure, frontdoor, iv}
10	  |B(delta)| non-increasing for {collider, mbias}
11	
12	where B(delta) = plim(C(delta)) - tau_true, C(delta) = (1-delta)I + delta*C0.
13	"""
14	
15	import numpy as np
16	import json
17	import time
18	import sys
19	import os
20	from scipy.optimize import minimize as scipy_minimize
21	
22	# ====================================================================
23	# Configuration
24	# ====================================================================
25	K_VALUES = [3, 5, 7]
26	K_ADVERSARIAL = [3, 5]
27	N_RANDOM = 10_000
28	N_LARGE = 5_000_000
29	DELTA_STEP = 0.01
30	SEED = 12345
31	MONO_TOL = 1e-8
32	
33	ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
34	             'mbias', 'iv', 'frontdoor']
35	TOPO_IDX = {t: i for i, t in enumerate(ALL_TOPOS)}
36	NON_DECREASING = {'confounding', 'mediation', 'exposure', 'frontdoor', 'iv'}
37	NON_INCREASING = {'collider', 'mbias'}
38	
39	ADV_DELTA_PAIRS = [(0.0, 0.2), (0.0, 0.5), (0.1, 0.3), (0.2, 0.5), (0.3, 0.7)]
40	ADV_N_STARTS = 100
41	
42	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
43	
44	# ====================================================================
45	# DGP Parameter Pools (from plan_002)
46	# ====================================================================
47	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
48	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
49	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
50	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
51	_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
52	_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
53	_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]
54	_MBIAS_A1_POOL = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]
55	_MBIAS_A2_POOL = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]
56	_IV_DZ_POOL = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]
57	_IV_DU_POOL = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]
58	_FD_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
59	_FD_DELTA_POOL = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]
60	
61	
62	def make_p_A(K):
63	    if K == 3:
64	        return np.array([0.40, 0.35, 0.25])
65	    raw = np.array([1.0 / i for i in range(1, K + 1)])
66	    return raw / raw.sum()
67	
68	
69	def make_all_params(K):
70	    p_A = make_p_A(K)
71	    return dict(
72	        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K - 1]),
73	                         beta_A=np.array(_BETA_A_POOL[:K - 1]), beta_T=2.0, sigma_T=1.0),
74	        mediation=dict(tau=0.5, gamma=np.array(_GAMMA_POOL[:K]),
75	                       delta=np.array(_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
76	        collider=dict(tau=1.0, g=np.zeros(K), dT=np.array(_DT_POOL[:K]),
77	                      dY=np.array(_DY_POOL[:K])),
78	        exposure=dict(beta=np.array(_BETA_POOL[:K]), p_A=p_A),
79	        mbias=dict(tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),
80	                   a1=np.array(_MBIAS_A1_POOL[:K]), a2=np.array(_MBIAS_A2_POOL[:K])),
81	        iv=dict(lam=1.0, g=np.zeros(K), dZ=np.array(_IV_DZ_POOL[:K]),
82	                dU=np.array(_IV_DU_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
83	        frontdoor=dict(alpha_U=1.0, lam_U=1.0, gamma=np.array(_FD_GAMMA_POOL[:K]),
84	                       delta=np.array(_FD_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
85	    )
86	
87	
88	# ====================================================================
89	# DGP Generators (from plan_002)
90	# ====================================================================
91	def _softmax_rows(logits):
92	    e = np.exp(logits - logits.max(axis=-1, keepdims=True))
93	    return e / e.sum(axis=-1, keepdims=True)
94	
95	
96	def _sample_cat(probs, rng):
97	    cum = np.cumsum(probs, axis=1)
98	    u = rng.uniform(size=probs.shape[0])[:, None]
99	    return (u >= cum).sum(axis=1).astype(int)
100	
101	
102	def gen_confounding(K, N, p, rng):
103	    A = rng.choice(K, size=N, p=p['p_A'])
104	    D = np.zeros((N, K - 1))
105	    for j in range(K - 1):
106	        D[:, j] = (A == j + 1).astype(float)
107	    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
108	    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
109	    return T, Y, A
110	
111	
112	def gen_mediation(K, N, p, rng):
113	    T = rng.binomial(1, 0.5, N).astype(float)
114	    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]
115	    A = _sample_cat(_softmax_rows(logits), rng)
116	    D = np.zeros((N, K - 1))
117	    for j in range(K - 1):
118	        D[:, j] = (A == j + 1)
119	    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
120	    return T, Y, A
121	
122	
123	def gen_collider(K, N, p, rng):
124	    T = rng.normal(0, 1, N)
125	    Y = p['tau'] * T + rng.normal(0, 1, N)
126	    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]
127	              + p['dY'][None, :] * Y[:, None])
128	    A = _sample_cat(_softmax_rows(logits), rng)
129	    return T, Y, A
130	
131	
132	def gen_exposure(K, N, p, rng):
133	    A = rng.choice(K, size=N, p=p['p_A'])
134	    D = np.zeros((N, K - 1))
135	    for j in range(K - 1):
136	        D[:, j] = (A == j + 1).astype(float)
137	    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
138	    return None, Y, A
139	
140	
141	def gen_mbias(K, N, p, rng):
142	    U1 = rng.normal(0, 1, N)
143	    U2 = rng.normal(0, 1, N)
144	    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)
145	    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)
146	    logits = np.zeros((N, K))
147	    for j in range(1, K):
148	        logits[:, j] = p['g'][j] + p['a1'][j] * U1 + p['a2'][j] * U2
149	    A = _sample_cat(_softmax_rows(logits), rng)
150	    return T, Y, A
151	
152	
153	def gen_iv(K, N, p, rng):
154	    Z = rng.binomial(1, 0.5, N).astype(float)
155	    U = rng.normal(0, 1, N)
156	    eps = rng.normal(0, 1, N)
157	    logits = np.zeros((N, K))
158	    for j in range(1, K):
159	        logits[:, j] = p['g'][j] + p['dZ'][j] * Z + p['dU'][j] * U
160	    A = _sample_cat(_softmax_rows(logits), rng)
161	    D = np.zeros((N, K - 1))
162	    for j in range(K - 1):
163	        D[:, j] = (A == j + 1).astype(float)
164	    Y = D @ p['beta'][1:] + p['lam'] * U + eps
165	    return Z, Y, A
166	
167	
168	def gen_frontdoor(K, N, p, rng):
169	    U = rng.normal(0, 1, N)
170	    T = p['alpha_U'] * U + rng.normal(0, 1, N)
171	    logits = np.zeros((N, K))
172	    for j in range(1, K):
173	        logits[:, j] = p['gamma'][j] + p['delta'][j] * T
174	    M = _sample_cat(_softmax_rows(logits), rng)
175	    D = np.zeros((N, K - 1))
176	    for j in range(K - 1):
177	        D[:, j] = (M == j + 1).astype(float)
178	    Y = D @ p['beta'][1:] + p['lam_U'] * U + rng.normal(0, 1, N)
179	    return T, Y, M
180	
181	
182	_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,
183	            collider=gen_collider, exposure=gen_exposure,
184	            mbias=gen_mbias, iv=gen_iv, frontdoor=gen_frontdoor)
185	
186	
187	# ====================================================================
188	# Sufficient Statistics
189	# ====================================================================
190	class SuffStats:
191	    def __init__(self, T, Y, A, K):
192	        self.K = K
193	        self.has_T = T is not None
194	        N = len(Y)
195	        DA = np.zeros((N, K))
196	        for k in range(K):
197	            DA[:, k] = (A == k).astype(float)
198	        self.p_A = DA.mean(0)
199	        self.E_Y = Y.mean()
200	        self.E_YD = (DA * Y[:, None]).mean(0)
201	        if self.has_T:
202	            self.E_T = T.mean()
203	            self.E_T2 = (T ** 2).mean()
204	            self.E_TY = (T * Y).mean()
205	            self.E_TD = (DA * T[:, None]).mean(0)
206	
207	
208	class IVSuffStats:
209	    def __init__(self, Z, Y, A, K):
210	        self.K = K
211	        z1 = Z == 1
212	        z0 = Z == 0
213	        self.RF = Y[z1].mean() - Y[z0].mean()
214	        self.FS = np.zeros(K)
215	        for k in range(K):
216	            self.FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
217	
218	
219	# ====================================================================
220	# Plim computation (single C)
221	# ====================================================================
222	def plim_ols_with_T(C, ss):
223	    K = ss.K
224	    q = C @ ss.p_A
225	    ct = C @ ss.E_TD
226	    cy = C @ ss.E_YD
227	    dim = K + 1
228	    EZZ = np.zeros((dim, dim))
229	    EZZ[0, 0] = 1.0
230	    EZZ[0, 1] = ss.E_T
231	    EZZ[1, 0] = ss.E_T
232	    EZZ[1, 1] = ss.E_T2
233	    EZZ[0, 2:] = q[1:]
234	    EZZ[2:, 0] = q[1:]
235	    EZZ[1, 2:] = ct[1:]
236	    EZZ[2:, 1] = ct[1:]
237	    for j in range(K - 1):
238	        EZZ[j + 2, j + 2] = q[j + 1]
239	    EZY = np.zeros(dim)
240	    EZY[0] = ss.E_Y
241	    EZY[1] = ss.E_TY
242	    EZY[2:] = cy[1:]
243	    try:
244	        return np.linalg.solve(EZZ, EZY)
245	    except np.linalg.LinAlgError:
246	        return np.full(dim, np.nan)
247	
248	
249	def plim_ols_exposure(C, ss):
250	    K = ss.K
251	    q = C @ ss.p_A
252	    cy = C @ ss.E_YD
253	    dim = K
254	    EZZ = np.zeros((dim, dim))
255	    EZZ[0, 0] = 1.0
256	    EZZ[0, 1:] = q[1:]
257	    EZZ[1:, 0] = q[1:]
258	    for j in range(K - 1):
259	        EZZ[j + 1, j + 1] = q[j + 1]
260	    EZY = np.zeros(dim)
261	    EZY[0] = ss.E_Y
262	    EZY[1:] = cy[1:]
263	    try:
264	        return np.linalg.solve(EZZ, EZY)
265	    except np.linalg.LinAlgError:
266	        return np.full(dim, np.nan)
267	
268	
269	def plim_iv_single(C, ss):
270	    FS_star = C @ ss.FS
271	    if abs(FS_star[1]) < 1e-8:
272	        return np.nan
273	    return ss.RF / FS_star[1]
274	
275	
276	def get_tau_at_C(topo, C, ss):
277	    if topo == 'iv':
278	        return plim_iv_single(C, ss)
279	    elif topo == 'exposure':
280	        return plim_ols_exposure(C, ss)[1]
281	    else:
282	        return plim_ols_with_T(C, ss)[1]
283	
284	
285	def get_tau_true(topo, K, params, ss):
286	    """True causal parameter for Conjecture 1.
287	
288	    For correctly-identified topologies: tau_true = plim(I).
289	    For protective topologies (collider, mbias): tau_true = DGP tau,
290	    so B(0) = plim(I) - tau != 0 (Berkson/M-bias at perfect classification).
291	    """
292	    p = params[topo]
293	    if topo == 'collider':
294	        return p['tau']
295	    elif topo == 'mbias':
296	        return p['tau']
297	    else:
298	        return get_tau_at_C(topo, np.eye(K), ss)
299	
300	
301	# ====================================================================
302	# Batched bias curve computation
303	# ====================================================================
304	def compute_bias_curve(topo, C0, ss, tau_true, delta_step=DELTA_STEP):
305	    K = C0.shape[0]
306	    min_diag = np.diag(C0).min()
307	    if min_diag >= 1.0:
308	        delta_max = 10.0
309	    else:
310	        delta_max = min(1.0 / (1.0 - min_diag), 10.0)
311	
312	    deltas = np.arange(0, delta_max + delta_step / 2, delta_step)
313	    n = len(deltas)
314	    d = deltas[:, None]
315	
316	    if topo == 'iv':
317	        FS0 = C0 @ ss.FS
318	        fs_star = (1 - d) * ss.FS[None, :] + d * FS0[None, :]
319	        denom = fs_star[:, 1]
320	        taus = np.where(np.abs(denom) < 1e-8, np.nan, ss.RF / denom)
321	    elif topo == 'exposure':
322	        pA0 = C0 @ ss.p_A
323	        YD0 = C0 @ ss.E_YD
324	        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]
325	        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]
326	        dim = K
327	        EZZ = np.zeros((n, dim, dim))
328	        EZZ[:, 0, 0] = 1.0
329	        EZZ[:, 0, 1:] = q[:, 1:]
330	        EZZ[:, 1:, 0] = q[:, 1:]
331	        for j in range(K - 1):
332	            EZZ[:, j + 1, j + 1] = q[:, j + 1]
333	        EZY = np.zeros((n, dim))
334	        EZY[:, 0] = ss.E_Y
335	        EZY[:, 1:] = cy[:, 1:]
336	        try:
337	            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]
338	            taus = coefs[:, 1]
339	        except np.linalg.LinAlgError:
340	            taus = np.full(n, np.nan)
341	    else:
342	        pA0 = C0 @ ss.p_A
343	        TD0 = C0 @ ss.E_TD
344	        YD0 = C0 @ ss.E_YD
345	        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]
346	        ct = (1 - d) * ss.E_TD[None, :] + d * TD0[None, :]
347	        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]
348	        dim = K + 1
349	        EZZ = np.zeros((n, dim, dim))
350	        EZZ[:, 0, 0] = 1.0
351	        EZZ[:, 0, 1] = ss.E_T
352	        EZZ[:, 1, 0] = ss.E_T
353	        EZZ[:, 1, 1] = ss.E_T2
354	        EZZ[:, 0, 2:] = q[:, 1:]
355	        EZZ[:, 2:, 0] = q[:, 1:]
356	        EZZ[:, 1, 2:] = ct[:, 1:]
357	        EZZ[:, 2:, 1] = ct[:, 1:]
358	        for j in range(K - 1):
359	            EZZ[:, j + 2, j + 2] = q[:, j + 1]
360	        EZY = np.zeros((n, dim))
361	        EZY[:, 0] = ss.E_Y
362	        EZY[:, 1] = ss.E_TY
363	        EZY[:, 2:] = cy[:, 1:]
364	        try:
365	            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]
366	            taus = coefs[:, 1]
367	        except np.linalg.LinAlgError:
368	            taus = np.full(n, np.nan)
369	
370	    bias_abs = np.abs(taus - tau_true)
371	    return deltas, bias_abs
372	
373	
374	def check_monotonicity(bias_abs, topo, tol=MONO_TOL):
375	    valid = ~np.isnan(bias_abs)
376	    ba = bias_abs[valid]
377	    if len(ba) < 2:
378	        return 0
379	    diffs = np.diff(ba)
380	    if topo in NON_DECREASING:
381	        return int(np.sum(diffs < -tol))
382	    else:
383	        return int(np.sum(diffs > tol))
384	
385	
386	# ====================================================================
387	# Precompute sufficient statistics
388	# ====================================================================
389	def precompute_all():
390	    print("\nPrecomputing sufficient statistics (N={:,})...".format(N_LARGE))
391	    sys.stdout.flush()
392	    t0 = time.time()
393	    all_ss = {}
394	    all_tau_true = {}
395	
396	    for K in K_VALUES:
397	        params = make_all_params(K)
398	        for topo in ALL_TOPOS:
399	            rng = np.random.default_rng(SEED + K * 100 + TOPO_IDX[topo])
400	            p = params[topo]
401	            if topo == 'iv':
402	                Z, Y, A = gen_iv(K, N_LARGE, p, rng)
403	                ss = IVSuffStats(Z, Y, A, K)
404	                del Z, Y, A
405	            elif topo == 'exposure':
406	                _, Y, A = gen_exposure(K, N_LARGE, p, rng)
407	                ss = SuffStats(None, Y, A, K)
408	                del Y, A
409	            else:
410	                T, Y, A = _GEN[topo](K, N_LARGE, p, rng)
411	                ss = SuffStats(T, Y, A, K)
412	                del T, Y, A
413	
414	            tau_true = get_tau_true(topo, K, params, ss)
415	            all_ss[(topo, K)] = ss
416	            all_tau_true[(topo, K)] = tau_true
417	
418	    print("  Done ({:.1f}s). tau_true samples:".format(time.time() - t0))
419	    for topo in ALL_TOPOS:
420	        vals = [all_tau_true[(topo, K)] for K in K_VALUES]
421	        vals_s = ", ".join(
422	            f"K{K}={v:.6f}" if v is not None and not np.isnan(v) else f"K{K}=NaN"
423	            for K, v in zip(K_VALUES, vals))
424	        direction = "non-dec" if topo in NON_DECREASING else "non-inc"
425	        print(f"    {topo:<14} [{direction}] {vals_s}")
426	    sys.stdout.flush()
427	    return all_ss, all_tau_true
428	
429	
430	# ====================================================================
431	# Part 1: Random Verification
432	# ====================================================================
433	def part1_random(all_ss, all_tau_true):
434	    print("\n" + "=" * 70)
435	    print("PART 1: Random Verification ({:,} C0 per topology x K)".format(N_RANDOM))
436	    print("=" * 70)
437	    sys.stdout.flush()
438	
439	    results = {}
440	    total_tests = 0
441	    total_violations = 0
442	
443	    for K in K_VALUES:
444	        print(f"\n  K = {K}")
445	        print(f"  {'Topology':<14} {'Direction':<10} {'Tested':>8} "
446	              f"{'Violations':>11} {'NaN_curves':>11} {'Time':>7}")
447	        print(f"  {'-' * 65}")
448	        sys.stdout.flush()
449	
450	        for topo in ALL_TOPOS:
451	            t0 = time.time()
452	            ss = all_ss[(topo, K)]
453	            tau_true = all_tau_true[(topo, K)]
454	
455	            rng_C = np.random.default_rng(SEED * 2 + K * 1000 + TOPO_IDX[topo])
456	            violations = 0
457	            nan_curves = 0
458	            worst_mag = 0.0
459	
460	            for i in range(N_RANDOM):
461	                C0 = np.zeros((K, K))
462	                for j in range(K):
463	                    C0[:, j] = rng_C.dirichlet(np.ones(K))
464	
465	                _, bias_abs = compute_bias_curve(topo, C0, ss, tau_true)
466	
467	                n_nan = np.isnan(bias_abs).sum()
468	                if n_nan > len(bias_abs) * 0.5:
469	                    nan_curves += 1
470	                    continue
471	
472	                n_viol = check_monotonicity(bias_abs, topo)
473	                if n_viol > 0:
474	                    violations += 1
475	                    valid = ~np.isnan(bias_abs)
476	                    ba = bias_abs[valid]
477	                    diffs = np.diff(ba)
478	                    if topo in NON_DECREASING:
479	                        worst_mag = max(worst_mag, abs(diffs.min()))
480	                    else:
481	                        worst_mag = max(worst_mag, diffs.max())
482	
483	            elapsed = time.time() - t0
484	            direction = "non-dec" if topo in NON_DECREASING else "non-inc"
485	            print(f"  {topo:<14} {direction:<10} {N_RANDOM:>8} "
486	                  f"{violations:>11} {nan_curves:>11} {elapsed:>6.1f}s")
487	            sys.stdout.flush()
488	
489	            results[f"{topo}_K{K}"] = {
490	                "n_tested": N_RANDOM,
491	                "violations": violations,
492	                "nan_curves": nan_curves,
493	                "direction": direction,
494	                "worst_violation_magnitude": float(worst_mag),
495	                "tau_true": float(tau_true) if not np.isnan(tau_true) else None,
496	            }
497	            total_tests += N_RANDOM
498	            total_violations += violations
499	
500	    print(f"\n  Grand total: {total_tests:,} tests, {total_violations} violations")
501	    return results
502	
503	
504	# ====================================================================
505	# Part 2: Adversarial Search
506	# ====================================================================
507	def part2_adversarial(all_ss, all_tau_true):
508	    print("\n" + "=" * 70)
509	    print(f"PART 2: Adversarial Search ({ADV_N_STARTS} starts x "
510	          f"{len(ADV_DELTA_PAIRS)} delta-pairs)")
511	    print("=" * 70)
512	    sys.stdout.flush()
513	
514	    results = {}
515	
516	    for K in K_ADVERSARIAL:
517	        print(f"\n  K = {K}")
518	        print(f"  {'Topology':<14} {'Direction':<10} {'best_obj':>11} "
519	              f"{'Counterex':>11} {'Time':>7}")
520	        print(f"  {'-' * 57}")
521	        sys.stdout.flush()
522	
523	        for topo in ALL_TOPOS:
524	            t0 = time.time()
525	            ss = all_ss[(topo, K)]
526	            tau_true = all_tau_true[(topo, K)]
527	
528	            best_objective = np.inf
529	            found_counterexample = False
530	            rng_adv = np.random.default_rng(
531	                SEED * 3 + K * 10000 + TOPO_IDX[topo] * 100)
532	
533	            for d1, d2 in ADV_DELTA_PAIRS:
534	                for _ in range(ADV_N_STARTS):
535	                    theta0 = rng_adv.normal(0, 1, K * K)
536	
537	                    def objective(theta, _topo=topo, _ss=ss, _tt=tau_true,
538	                                  _d1=d1, _d2=d2, _K=K):
539	                        logits = theta.reshape(_K, _K)
540	                        exp_l = np.exp(logits - logits.max(axis=0, keepdims=True))
541	                        C0 = exp_l / exp_l.sum(axis=0, keepdims=True)
542	
543	                        C1 = (1 - _d1) * np.eye(_K) + _d1 * C0
544	                        C2 = (1 - _d2) * np.eye(_K) + _d2 * C0
545	
546	                        tau1 = get_tau_at_C(_topo, C1, _ss)
547	                        tau2 = get_tau_at_C(_topo, C2, _ss)
548	
549	                        if np.isnan(tau1) or np.isnan(tau2):
550	                            return 0.0
551	
552	                        b1_sq = (tau1 - _tt) ** 2
553	                        b2_sq = (tau2 - _tt) ** 2
554	
555	                        if _topo in NON_DECREASING:
556	                            return b2_sq - b1_sq
557	                        else:
558	                            return b1_sq - b2_sq
559	
560	                    res = scipy_minimize(objective, theta0, method='L-BFGS-B',
561	                                         options={'maxiter': 100, 'ftol': 1e-12})
562	
563	                    if res.fun < best_objective:
564	                        best_objective = res.fun
565	
566	                    if res.fun < -1e-6:
567	                        found_counterexample = True
568	
569	            elapsed = time.time() - t0
570	            direction = "non-dec" if topo in NON_DECREASING else "non-inc"
571	            ce_str = "YES!" if found_counterexample else "no"
572	            print(f"  {topo:<14} {direction:<10} {best_objective:>11.6f} "
573	                  f"{ce_str:>11} {elapsed:>6.1f}s")
574	            sys.stdout.flush()
575	
576	            results[f"{topo}_K{K}"] = {
577	                "n_starts": ADV_N_STARTS * len(ADV_DELTA_PAIRS),
578	                "best_objective": float(best_objective),
579	                "found_counterexample": found_counterexample,
580	                "delta_pairs": [[d1, d2] for d1, d2 in ADV_DELTA_PAIRS],
581	            }
582	
583	    return results
584	
585	
586	# ====================================================================
587	# Main
588	# ====================================================================
589	def main():
590	    t_total = time.time()
591	    print("Exp-D: Conjecture 1 Extended Verification")
592	    print(f"  Random: {N_RANDOM:,} C0 x 7 topologies x K in {K_VALUES}")
593	    print(f"  Adversarial: {ADV_N_STARTS} starts x {len(ADV_DELTA_PAIRS)} "
594	          f"delta-pairs x K in {K_ADVERSARIAL}")
595	    print(f"  N_large={N_LARGE:,}, delta_step={DELTA_STEP}, seed={SEED}")
596	    sys.stdout.flush()
597	
598	    all_ss, all_tau_true = precompute_all()
599	
600	    random_results = part1_random(all_ss, all_tau_true)
601	    adversarial_results = part2_adversarial(all_ss, all_tau_true)
602	
603	    # Build output
604	    total_random = sum(r['n_tested'] for r in random_results.values())
605	    total_viol = sum(r['violations'] for r in random_results.values())
606	    total_ce = sum(1 for r in adversarial_results.values()
607	                   if r['found_counterexample'])
608	
609	    if total_viol == 0 and total_ce == 0:
610	        summary = (f"Zero violations across {total_random:,} random tests + "
611	                   f"0 counterexamples found by adversarial search")
612	    else:
613	        summary = (f"{total_viol} violations across {total_random:,} random tests + "
614	                   f"{total_ce} counterexamples found by adversarial search")
615	
616	    output = {"random_verification": {}, "adversarial_search": {}, "summary": summary}
617	
618	    for topo in ALL_TOPOS:
619	        rv = {}
620	        for K in K_VALUES:
621	            key = f"{topo}_K{K}"
622	            if key in random_results:
623	                rv[f"K{K}"] = random_results[key]
624	        output["random_verification"][topo] = rv
625	
626	    for topo in ALL_TOPOS:
627	        av = {}
628	        for K in K_ADVERSARIAL:
629	            key = f"{topo}_K{K}"
630	            if key in adversarial_results:
631	                av[f"K{K}"] = adversarial_results[key]
632	        output["adversarial_search"][topo] = av
633	
634	    out_path = os.path.join(OUT_DIR, 'exp_d_conjecture_results.json')
635	    with open(out_path, 'w') as f:
636	        json.dump(output, f, indent=2, default=str)
637	    print(f"\nJSON -> {out_path}")
638	
639	    total_time = time.time() - t_total
640	    print(f"\n{summary}")
641	    print(f"Total time: {total_time:.0f}s ({total_time/60:.1f}min)")
642	
643	
644	if __name__ == "__main__":
645	    main()
646	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8acbca24-6760-4d40-a33a-ae34405f268a",
  "isSidechain": true,
  "promptId": "3f772f34-432b-4b73-8d6a-c54bf571a4ba",
  "agentId": "a8ae618b752846327",
  "type": "user",
  "uuid": "bc205c58-b57f-4d88-86f1-0b35bb2834b5",
  "sourceToolAssistantUUID": "8acbca24-6760-4d40-a33a-ae34405f268a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T12:18:03.991Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XoG6iZbbxdpH2htMuzGQzL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc205c58-b57f-4d88-86f1-0b35bb2834b5",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbPLRRiaih6R9K6iCT4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "196c208a-8a18-4a79-806e-aba5c26af254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013HZ1ujQRNgEjGqghLphAbg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35069,
      "cache_read_input_tokens": 0,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 35069
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 35069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 35069,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T12:18:03.997Z_

<details><summary>↩ Tool result · `toolu_01XoG6iZbbxdpH2htMuzGQzL`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Exp-E: ASV Stability Across DGPs
4	
5	Demonstrates that ASV ranking (relative topology vulnerability ordering)
6	is stable across different DGP parameter configurations.
7	
8	3 DGP configs × 3 topologies × 5 C₀ matrices = 45 sweeps.
9	Each of 9 cells reports the median δ* over the 5 C₀s.
10	"""
11	
12	import numpy as np
13	import json
14	import time
15	
16	K = 3
17	STEP = 0.001
18	
19	# ─── C(δ) parameterization ──────────────────────────────────────────────────
20	
21	def make_C_delta(C0, delta):
22	    C = (1 - delta) * np.eye(K) + delta * C0
23	    C = np.maximum(C, 0.0)
24	    cs = C.sum(axis=0)
25	    cs = np.where(cs < 1e-10, 1.0, cs)
26	    return C / cs
27	
28	
29	def get_delta_max(C0):
30	    d = np.diag(C0).min()
31	    if d >= 1.0:
32	        return 10.0
33	    return min(1.0 / (1.0 - d), 10.0)
34	
35	
36	def make_fixed_C0(diag_val):
37	    off = (1 - diag_val) / (K - 1)
38	    C0 = np.full((K, K), off)
39	    np.fill_diagonal(C0, diag_val)
40	    return C0
41	
42	
43	# ─── Topology 1: Confounding ────────────────────────────────────────────────
44	# DAG: A → T, A → Y, T → Y, A → A*
45	# OLS: Y ~ 1 + T + D*₁ + D*₂
46	# plim γ = (E[Z'Z])⁻¹ E[Z'X] β   where Z uses A*, X uses A
47	
48	def plim_confounding(C, dgp):
49	    p = dgp['p']
50	    g = dgp['gamma']
51	    tau = dgp['tau']
52	    bA = dgp['beta'][1:]
53	    sT = dgp.get('sigma_T', 1.0)
54	
55	    b = np.array([0.0, tau, bA[0], bA[1]])
56	    ET = g[0] * p[1] + g[1] * p[2]
57	    ET2 = g[0]**2 * p[1] + g[1]**2 * p[2] + sT**2
58	    q = C @ p
59	    ETDs = np.array([g[0] * C[j, 1] * p[1] + g[1] * C[j, 2] * p[2]
60	                     for j in range(K)])
61	
62	    EZZ = np.array([
63	        [1,    ET,      q[1],     q[2]    ],
64	        [ET,   ET2,     ETDs[1],  ETDs[2] ],
65	        [q[1], ETDs[1], q[1],     0       ],
66	        [q[2], ETDs[2], 0,        q[2]    ]])
67	    EZX = np.array([
68	        [1,    ET,      p[1],         p[2]        ],
69	        [ET,   ET2,     g[0] * p[1],  g[1] * p[2] ],
70	        [q[1], ETDs[1], C[1, 1] * p[1], C[1, 2] * p[2]],
71	        [q[2], ETDs[2], C[2, 1] * p[1], C[2, 2] * p[2]]])
72	    return np.linalg.solve(EZZ, EZX @ b)[1]
73	
74	
75	# ─── Topology 2: Exposure ───────────────────────────────────────────────────
76	# DAG: A → Y, A → A*
77	# OLS: Y ~ 1 + D*₁ + D*₂
78	
79	def plim_exposure(C, dgp):
80	    p, beta = dgp['p'], dgp['beta']
81	    q = C @ p
82	    EZZ = np.array([
83	        [1,    q[1], q[2]],
84	        [q[1], q[1], 0   ],
85	        [q[2], 0,    q[2]]])
86	    EZX = np.array([
87	        [1,    p[1],           p[2]          ],
88	        [q[1], C[1, 1] * p[1], C[1, 2] * p[2]],
89	        [q[2], C[2, 1] * p[1], C[2, 2] * p[2]]])
90	    return np.linalg.solve(EZZ, EZX @ beta)
91	
92	
93	# ─── Topology 3: IV ─────────────────────────────────────────────────────────
94	# DAG: Z → A, U → {A,Y}, A → Y, A → A*
95	# Wald estimator: RF / FS*₁
96	
97	IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)
98	
99	
100	def _softmax_sample(logits, rng):
101	    e = np.exp(logits - logits.max(1, keepdims=True))
102	    p = e / e.sum(1, keepdims=True)
103	    c = np.cumsum(p, axis=1)
104	    u = rng.uniform(size=logits.shape[0])
105	    return (u >= c[:, 0]).astype(int) + (u >= c[:, 1]).astype(int)
106	
107	
108	def precomp_iv(beta, params, N=2_000_000, seed=999):
109	    rng = np.random.default_rng(seed)
110	    Z = rng.binomial(1, 0.5, N).astype(float)
111	    U = rng.normal(0, 1, N)
112	    logits = np.column_stack([
113	        np.zeros(N),
114	        params['g1'] + params['dZ'] * Z + params['dU'] * U,
115	        params['g2'] + params['dZ2'] * Z + params['dU2'] * U])
116	    A = _softmax_sample(logits, rng)
117	    Y = (beta[1] * (A == 1).astype(float)
118	         + beta[2] * (A == 2).astype(float)
119	         + params['lam'] * U + rng.normal(0, 1, N))
120	    z1, z0 = Z == 1, Z == 0
121	    RF = Y[z1].mean() - Y[z0].mean()
122	    FS = np.array([(A[z1] == k).mean() - (A[z0] == k).mean()
123	                   for k in range(K)])
124	    return dict(RF=RF, FS=FS)
125	
126	
127	def plim_iv(C, st):
128	    fs = (C @ st['FS'])[1]
129	    return np.nan if abs(fs) < 1e-8 else st['RF'] / fs
130	
131	
132	# ─── ASV computation ────────────────────────────────────────────────────────
133	
134	def _make_grid(C0):
135	    dmax = get_delta_max(C0)
136	    n = int(round(dmax / STEP)) + 1
137	    return np.linspace(0, dmax, n)
138	
139	
140	def _find_envelope_asv(deltas, bias_abs, tau_abs, threshold):
141	    if tau_abs < 1e-12:
142	        return 0.0
143	    thresh = threshold * tau_abs
144	    rmax = 0.0
145	    for i in range(len(deltas)):
146	        b = bias_abs[i]
147	        if not np.isnan(b):
148	            rmax = max(rmax, b)
149	        if rmax > thresh:
150	            return float(deltas[i])
151	    return None
152	
153	
154	def compute_cell_confounding(dgp, C0):
155	    deltas = _make_grid(C0)
156	    tau0 = plim_confounding(np.eye(K), dgp)
157	    curve = np.array([plim_confounding(make_C_delta(C0, d), dgp)
158	                      for d in deltas])
159	    ba = np.abs(curve - tau0)
160	    return {
161	        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),
162	        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),
163	    }
164	
165	
166	def compute_cell_exposure(dgp, C0):
167	    deltas = _make_grid(C0)
168	    beta0 = plim_exposure(np.eye(K), dgp)
169	    curves = np.array([plim_exposure(make_C_delta(C0, d), dgp)
170	                       for d in deltas])
171	
172	    mr = np.zeros(len(deltas))
173	    for i in range(len(deltas)):
174	        for k in [1, 2]:
175	            if abs(beta0[k]) > 1e-10:
176	                mr[i] = max(mr[i],
177	                            abs(curves[i, k] - beta0[k]) / abs(beta0[k]))
178	
179	    def _mag(threshold):
180	        rmax = 0.0
181	        for i in range(len(deltas)):
182	            rmax = max(rmax, mr[i])
183	            if rmax > threshold:
184	                return float(deltas[i])
185	        return None
186	
187	    sf = None
188	    for i, d in enumerate(deltas):
189	        for k in [1, 2]:
190	            if (abs(beta0[k]) > 1e-10
191	                    and abs(curves[i, k]) > 1e-10
192	                    and curves[i, k] * beta0[k] < 0):
193	                sf = float(d)
194	                break
195	        if sf is not None:
196	            break
197	
198	    return {
199	        'mag_asv_10pct': _mag(0.1),
200	        'mag_asv_50pct': _mag(0.5),
201	        'sign_flip_asv': sf,
202	    }
203	
204	
205	def compute_cell_iv(st, C0):
206	    deltas = _make_grid(C0)
207	    tau0 = plim_iv(np.eye(K), st)
208	    if np.isnan(tau0) or abs(tau0) < 1e-10:
209	        return {'mag_asv_10pct': None, 'mag_asv_50pct': None}
210	    curve = np.array([plim_iv(make_C_delta(C0, d), st) for d in deltas])
211	    ba = np.abs(curve - tau0)
212	    return {
213	        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),
214	        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),
215	    }
216	
217	
218	def median_results(cells):
219	    keys = cells[0].keys()
220	    out = {}
221	    for k in keys:
222	        vals = [c[k] for c in cells if c[k] is not None]
223	        out[k] = round(float(np.median(vals)), 4) if vals else None
224	    return out
225	
226	
227	# ─── Main ────────────────────────────────────────────────────────────────────
228	
229	if __name__ == '__main__':
230	    t0 = time.time()
231	
232	    DGPS = [
233	        {'name': 'alternating_large',
234	         'beta': np.array([0., 1.0, -0.5]), 'tau': 0.5,
235	         'p': np.array([0.5, 0.33, 0.17]),
236	         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},
237	        {'name': 'same_sign_medium',
238	         'beta': np.array([0., 0.5, 0.3]), 'tau': 0.5,
239	         'p': np.array([0.5, 0.33, 0.17]),
240	         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},
241	        {'name': 'alternating_small',
242	         'beta': np.array([0., 0.2, -0.1]), 'tau': 0.5,
243	         'p': np.array([0.5, 0.33, 0.17]),
244	         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},
245	    ]
246	
247	    DIAG_VALS = [0.5, 0.6, 0.7, 0.8, 0.9]
248	    C0S = [(d, make_fixed_C0(d)) for d in DIAG_VALS]
249	    TOPOS = ['confounding', 'exposure', 'iv']
250	
251	    print("Exp-E: ASV Stability Across DGPs")
252	    print("=" * 70)
253	
254	    print("Precomputing IV sufficient statistics...")
255	    iv_st = {}
256	    for dgp in DGPS:
257	        iv_st[dgp['name']] = precomp_iv(dgp['beta'], IV_PARAMS)
258	        t_iv = plim_iv(np.eye(K), iv_st[dgp['name']])
259	        print(f"  {dgp['name']}: Wald(I) = {t_iv:.6f}")
260	
261	    results = {t: {} for t in TOPOS}
262	    per_c0 = {t: {} for t in TOPOS}
263	
264	    for dgp in DGPS:
265	        nm = dgp['name']
266	        print(f"\nDGP: {nm}  beta={dgp['beta'].tolist()}")
267	
268	        for topo in TOPOS:
269	            cells = []
270	            for dv, C0 in C0S:
271	                if topo == 'confounding':
272	                    c = compute_cell_confounding(dgp, C0)
273	                elif topo == 'exposure':
274	                    c = compute_cell_exposure(dgp, C0)
275	                else:
276	                    c = compute_cell_iv(iv_st[nm], C0)
277	                cells.append(c)
278	
279	            med = median_results(cells)
280	            results[topo][nm] = med
281	            per_c0[topo][nm] = [
282	                {**c, 'C0_diag': dv} for (dv, _), c in zip(C0S, cells)]
283	
284	            parts = [f"10%={med['mag_asv_10pct']}",
285	                     f"50%={med['mag_asv_50pct']}"]
286	            if 'sign_flip_asv' in med:
287	                parts.append(f"sf={med['sign_flip_asv']}")
288	            print(f"  {topo:>12}: {', '.join(parts)}")
289	
290	    # ── Ranking analysis ─────────────────────────────────────────────────────
291	    print("\n" + "=" * 70)
292	    print("Ranking (by delta*_10%, lower = more fragile)")
293	    print("=" * 70)
294	    rankings = {}
295	    for dgp in DGPS:
296	        nm = dgp['name']
297	        vals = [(t, results[t][nm]['mag_asv_10pct'] or float('inf'))
298	                for t in TOPOS]
299	        vals.sort(key=lambda x: x[1])
300	        rankings[nm] = [t for t, _ in vals]
301	        vstr = ' < '.join(f"{t}({v:.4f})" for t, v in vals)
302	        print(f"  {nm}: {vstr}")
303	
304	    stable = len(set(tuple(r) for r in rankings.values())) == 1
305	    stability_msg = ("Rankings preserved across all 3 DGPs" if stable
306	                     else "Rankings vary across DGPs")
307	    print(f"\nStable: {stable} -- {stability_msg}")
308	
309	    sf_ss = results['exposure']['same_sign_medium'].get('sign_flip_asv')
310	    print(f"Same-sign sign-flip: "
311	          f"{'None (confirmed -- no flip for same-sign beta)' if sf_ss is None else sf_ss}")
312	
313	    # ── Save JSON ────────────────────────────────────────────────────────────
314	    output = {
315	        'dgp_configs': [
316	            {'name': d['name'], 'beta': d['beta'].tolist(),
317	             'tau': d['tau'], 'p': d['p'].tolist()}
318	            for d in DGPS],
319	        'C0_diag_values': DIAG_VALS,
320	        'results': results,
321	        'per_C0_results': per_c0,
322	        'rankings': rankings,
323	        'ranking_stable': stable,
324	        'ranking_stability': stability_msg,
325	    }
326	    json_path = 'artifacts/exp_e_asv_stability_results.json'
327	    with open(json_path, 'w') as f:
328	        json.dump(output, f, indent=2)
329	    print(f"\nSaved: {json_path}")
330	
331	    # ── Save LaTeX table ─────────────────────────────────────────────────────
332	    labels = {
333	        'alternating_large': r'Alt.\ large: $\bm{\beta}=[0,\,1.0,\,-0.5]$',
334	        'same_sign_medium':  r'Same-sign: $\bm{\beta}=[0,\,0.5,\,0.3]$',
335	        'alternating_small': r'Alt.\ small: $\bm{\beta}=[0,\,0.2,\,-0.1]$',
336	    }
337	    tex = [
338	        r'\begin{table}[t]',
339	        r'\centering',
340	        r'\caption{ASV stability across DGP configurations. '
341	        r'Each cell shows $\delta^*$ at the 10\% relative bias threshold '
342	        r'(median over 5 confusion matrices with diagonal '
343	        r'$\in\{0.5,0.6,0.7,0.8,0.9\}$). '
344	        r'Lower $\delta^*$ indicates greater fragility. '
345	        r'Confounding is consistently most robust; '
346	        r'for alternating-sign $\bm{\beta}$, '
347	        r'the ranking Exposure $<$ IV $<$ Confounding holds. '
348	        r"``$\infty$\!\!'' = threshold never reached within $\delta$ range.}",
349	        r'\label{tab:asv_stability}',
350	        r'\small',
351	        r'\begin{tabular}{l ccc}',
352	        r'\toprule',
353	        r' & \multicolumn{3}{c}{Magnitude ASV $\delta^*_{10\%}$} \\',
354	        r'\cmidrule(lr){2-4}',
355	        r'DGP Configuration & Confounding & Exposure & IV \\',
356	        r'\midrule',
357	    ]
358	    for dgp in DGPS:
359	        nm = dgp['name']
360	        vals = []
361	        for t in TOPOS:
362	            v = results[t][nm]['mag_asv_10pct']
363	            vals.append(f'{v:.3f}' if v is not None else r'$\infty$')
364	        tex.append(
365	            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]} \\\\')
366	    tex += [r'\bottomrule', r'\end{tabular}', r'\end{table}']
367	
368	    tex_path = 'artifacts/exp_e_asv_stability_table.tex'
369	    with open(tex_path, 'w') as f:
370	        f.write('\n'.join(tex))
371	    print(f"Saved: {tex_path}")
372	
373	    print(f"\nTotal: {time.time() - t0:.1f}s")
374	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "196c208a-8a18-4a79-806e-aba5c26af254",
  "isSidechain": true,
  "promptId": "3f772f34-432b-4b73-8d6a-c54bf571a4ba",
  "agentId": "a8ae618b752846327",
  "type": "user",
  "uuid": "4b06228b-40c0-41b4-8188-d68efda08eb3",
  "sourceToolAssistantUUID": "196c208a-8a18-4a79-806e-aba5c26af254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-22T12:18:06.916Z_

Now let me also look at the original results to understand the current output format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b06228b-40c0-41b4-8188-d68efda08eb3",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbPdVLm7xBRujCupdQC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e256a1fe-670c-46c6-8336-e4b6b98147f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VY4RmrLjnkLStqTiMTUU4d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17377,
      "cache_read_input_tokens": 35069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17377,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T12:18:08.048Z_

<details open><summary>🔧 Tool call — Read · `toolu_013EqDp9RBAztUs29S7rw97B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e256a1fe-670c-46c6-8336-e4b6b98147f1",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbPdVLm7xBRujCupdQC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e202d11-1a0c-4fa1-91c9-fc5c88c724ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VY4RmrLjnkLStqTiMTUU4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17377,
      "cache_read_input_tokens": 35069,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17377
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 35069,
          "cache_creation_input_tokens": 17377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17377,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T12:18:08.061Z_

<details><summary>↩ Tool result · `toolu_013EqDp9RBAztUs29S7rw97B`</summary>

```text
1	{
2	  "random_verification": {
3	    "confounding": {
4	      "K3": {
5	        "n_tested": 10000,
6	        "violations": 8467,
7	        "nan_curves": 0,
8	        "direction": "non-dec",
9	        "worst_violation_magnitude": 0.010860102441185848,
10	        "tau_true": 1.9998241281545739
11	      },
12	      "K5": {
13	        "n_tested": 10000,
14	        "violations": 8064,
15	        "nan_curves": 0,
16	        "direction": "non-dec",
17	        "worst_violation_magnitude": 0.005829922779741814,
18	        "tau_true": 1.999928016747683
19	      },
20	      "K7": {
21	        "n_tested": 10000,
22	        "violations": 7890,
23	        "nan_curves": 0,
24	        "direction": "non-dec",
25	        "worst_violation_magnitude": 0.0034077583603342454,
26	        "tau_true": 2.0003841224302854
27	      }
28	    },
29	    "mediation": {
30	      "K3": {
31	        "n_tested": 10000,
32	        "violations": 8236,
33	        "nan_curves": 0,
34	        "direction": "non-dec",
35	        "worst_violation_magnitude": 0.012735806472077393,
36	        "tau_true": 0.5020006875627565
37	      },
38	      "K5": {
39	        "n_tested": 10000,
40	        "violations": 7903,
41	        "nan_curves": 0,
42	        "direction": "non-dec",
43	        "worst_violation_magnitude": 0.006562553155827211,
44	        "tau_true": 0.4991583937189051
45	      },
46	      "K7": {
47	        "n_tested": 10000,
48	        "violations": 7890,
49	        "nan_curves": 0,
50	        "direction": "non-dec",
51	        "worst_violation_magnitude": 0.0040338233163313975,
52	        "tau_true": 0.49928121967936034
53	      }
54	    },
55	    "collider": {
56	      "K3": {
57	        "n_tested": 10000,
58	        "violations": 8653,
59	        "nan_curves": 0,
60	        "direction": "non-inc",
61	        "worst_violation_magnitude": 0.004606655910260882,
62	        "tau_true": 1.0
63	      },
64	      "K5": {
65	        "n_tested": 10000,
66	        "violations": 7643,
67	        "nan_curves": 0,
68	        "direction": "non-inc",
69	        "worst_violation_magnitude": 0.0034285917273304545,
70	        "tau_true": 1.0
71	      },
72	      "K7": {
73	        "n_tested": 10000,
74	        "violations": 7555,
75	        "nan_curves": 0,
76	        "direction": "non-inc",
77	        "worst_violation_magnitude": 0.0024942343934484246,
78	        "tau_true": 1.0
79	      }
80	    },
81	    "exposure": {
82	      "K3": {
83	        "n_tested": 10000,
84	        "violations": 488,
85	        "nan_curves": 0,
86	        "direction": "non-dec",
87	        "worst_violation_magnitude": 0.055916435702870304,
88	        "tau_true": 0.9990860758671022
89	      },
90	      "K5": {
91	        "n_tested": 10000,
92	        "violations": 206,
93	        "nan_curves": 0,
94	        "direction": "non-dec",
95	        "worst_violation_magnitude": 0.0512139933848792,
96	        "tau_true": 0.9992701620548922
97	      },
98	      "K7": {
99	        "n_tested": 10000,
100	        "violations": 77,
101	        "nan_curves": 0,
102	        "direction": "non-dec",
103	        "worst_violation_magnitude": 0.022039262143256244,
104	        "tau_true": 1.001113712115238
105	      }
106	    },
107	    "mbias": {
108	      "K3": {
109	        "n_tested": 10000,
110	        "violations": 9734,
111	        "nan_curves": 0,
112	        "direction": "non-inc",
113	        "worst_violation_magnitude": 0.0015522285471285535,
114	        "tau_true": 1.0
115	      },
116	      "K5": {
117	        "n_tested": 10000,
118	        "violations": 7640,
119	        "nan_curves": 0,
120	        "direction": "non-inc",
121	        "worst_violation_magnitude": 0.0014365508946148076,
122	        "tau_true": 1.0
123	      },
124	      "K7": {
125	        "n_tested": 10000,
126	        "violations": 7513,
127	        "nan_curves": 0,
128	        "direction": "non-inc",
129	        "worst_violation_magnitude": 0.0008778900165735681,
130	        "tau_true": 1.0
131	      }
132	    },
133	    "iv": {
134	      "K3": {
135	        "n_tested": 10000,
136	        "violations": 7433,
137	        "nan_curves": 0,
138	        "direction": "non-dec",
139	        "worst_violation_magnitude": 15001640.04582617,
140	        "tau_true": 1.3328638533484616
141	      },
142	      "K5": {
143	        "n_tested": 10000,
144	        "violations": 6011,
145	        "nan_curves": 0,
146	        "direction": "non-dec",
147	        "worst_violation_magnitude": 4067672.819669802,
148	        "tau_true": 1.9217194857035584
149	      },
150	      "K7": {
151	        "n_tested": 10000,
152	        "violations": 5706,
153	        "nan_curves": 0,
154	        "direction": "non-dec",
155	        "worst_violation_magnitude": 12989086.745428896,
156	        "tau_true": 2.050984649343555
157	      }
158	    },
159	    "frontdoor": {
160	      "K3": {
161	        "n_tested": 10000,
162	        "violations": 8427,
163	        "nan_curves": 0,
164	        "direction": "non-dec",
165	        "worst_violation_magnitude": 0.01306574620731793,
166	        "tau_true": 0.5001636710565874
167	      },
168	      "K5": {
169	        "n_tested": 10000,
170	        "violations": 8079,
171	        "nan_curves": 0,
172	        "direction": "non-dec",
173	        "worst_violation_magnitude": 0.006287368037765306,
174	        "tau_true": 0.500028786373885
175	      },
176	      "K7": {
177	        "n_tested": 10000,
178	        "violations": 7899,
179	        "nan_curves": 0,
180	        "direction": "non-dec",
181	        "worst_violation_magnitude": 0.00365032316631253,
182	        "tau_true": 0.499894195097627
183	      }
184	    }
185	  },
186	  "adversarial_search": {
187	    "confounding": {
188	      "K3": {
189	        "n_starts": 500,
190	        "best_objective": -0.00981505115034094,
191	        "found_counterexample": true,
192	        "delta_pairs": [
193	          [
194	            0.0,
195	            0.2
196	          ],
197	          [
198	            0.0,
199	            0.5
200	          ],
201	          [
202	            0.1,
203	            0.3
204	          ],
205	          [
206	            0.2,
207	            0.5
208	          ],
209	          [
210	            0.3,
211	            0.7
212	          ]
213	        ]
214	      },
215	      "K5": {
216	        "n_starts": 500,
217	        "best_objective": -0.014781769787710543,
218	        "found_counterexample": true,
219	        "delta_pairs": [
220	          [
221	            0.0,
222	            0.2
223	          ],
224	          [
225	            0.0,
226	            0.5
227	          ],
228	          [
229	            0.1,
230	            0.3
231	          ],
232	          [
233	            0.2,
234	            0.5
235	          ],
236	          [
237	            0.3,
238	            0.7
239	          ]
240	        ]
241	      }
242	    },
243	    "mediation": {
244	      "K3": {
245	        "n_starts": 500,
246	        "best_objective": -0.010561123106817605,
247	        "found_counterexample": true,
248	        "delta_pairs": [
249	          [
250	            0.0,
251	            0.2
252	          ],
253	          [
254	            0.0,
255	            0.5
256	          ],
257	          [
258	            0.1,
259	            0.3
260	          ],
261	          [
262	            0.2,
263	            0.5
264	          ],
265	          [
266	            0.3,
267	            0.7
268	          ]
269	        ]
270	      },
271	      "K5": {
272	        "n_starts": 500,
273	        "best_objective": -0.010862658240636185,
274	        "found_counterexample": true,
275	        "delta_pairs": [
276	          [
277	            0.0,
278	            0.2
279	          ],
280	          [
281	            0.0,
282	            0.5
283	          ],
284	          [
285	            0.1,
286	            0.3
287	          ],
288	          [
289	            0.2,
290	            0.5
291	          ],
292	          [
293	            0.3,
294	            0.7
295	          ]
296	        ]
297	      }
298	    },
299	    "collider": {
300	      "K3": {
301	        "n_starts": 500,
302	        "best_objective": -0.00030283818433801376,
303	        "found_counterexample": true,
304	        "delta_pairs": [
305	          [
306	            0.0,
307	            0.2
308	          ],
309	          [
310	            0.0,
311	            0.5
312	          ],
313	          [
314	            0.1,
315	            0.3
316	          ],
317	          [
318	            0.2,
319	            0.5
320	          ],
321	          [
322	            0.3,
323	            0.7
324	          ]
325	        ]
326	      },
327	      "K5": {
328	        "n_starts": 500,
329	        "best_objective": -0.001117545184579056,
330	        "found_counterexample": true,
331	        "delta_pairs": [
332	          [
333	            0.0,
334	            0.2
335	          ],
336	          [
337	            0.0,
338	            0.5
339	          ],
340	          [
341	            0.1,
342	            0.3
343	          ],
344	          [
345	            0.2,
346	            0.5
347	          ],
348	          [
349	            0.3,
350	            0.7
351	          ]
352	        ]
353	      }
354	    },
355	    "exposure": {
356	      "K3": {
357	        "n_starts": 500,
358	        "best_objective": -0.003922567878966418,
359	        "found_counterexample": true,
360	        "delta_pairs": [
361	          [
362	            0.0,
363	            0.2
364	          ],
365	          [
366	            0.0,
367	            0.5
368	          ],
369	          [
370	            0.1,
371	            0.3
372	          ],
373	          [
374	            0.2,
375	            0.5
376	          ],
377	          [
378	            0.3,
379	            0.7
380	          ]
381	        ]
382	      },
383	      "K5": {
384	        "n_starts": 500,
385	        "best_objective": -0.005420375127682058,
386	        "found_counterexample": true,
387	        "delta_pairs": [
388	          [
389	            0.0,
390	            0.2
391	          ],
392	          [
393	            0.0,
394	            0.5
395	          ],
396	          [
397	            0.1,
398	            0.3
399	          ],
400	          [
401	            0.2,
402	            0.5
403	          ],
404	          [
405	            0.3,
406	            0.7
407	          ]
408	        ]
409	      }
410	    },
411	    "mbias": {
412	      "K3": {
413	        "n_starts": 500,
414	        "best_objective": -0.0017428177445399143,
415	        "found_counterexample": true,
416	        "delta_pairs": [
417	          [
418	            0.0,
419	            0.2
420	          ],
421	          [
422	            0.0,
423	            0.5
424	          ],
425	          [
426	            0.1,
427	            0.3
428	          ],
429	          [
430	            0.2,
431	            0.5
432	          ],
433	          [
434	            0.3,
435	            0.7
436	          ]
437	        ]
438	      },
439	      "K5": {
440	        "n_starts": 500,
441	        "best_objective": -0.0019441470428496039,
442	        "found_counterexample": true,
443	        "delta_pairs": [
444	          [
445	            0.0,
446	            0.2
447	          ],
448	          [
449	            0.0,
450	            0.5
451	          ],
452	          [
453	            0.1,
454	            0.3
455	          ],
456	          [
457	            0.2,
458	            0.5
459	          ],
460	          [
461	            0.3,
462	            0.7
463	          ]
464	        ]
465	      }
466	    },
467	    "iv": {
468	      "K3": {
469	        "n_starts": 500,
470	        "best_objective": 2.6081713678869703e-29,
471	        "found_counterexample": false,
472	        "delta_pairs": [
473	          [
474	            0.0,
475	            0.2
476	          ],
477	          [
478	            0.0,
479	            0.5
480	          ],
481	          [
482	            0.1,
483	            0.3
484	          ],
485	          [
486	            0.2,
487	            0.5
488	          ],
489	          [
490	            0.3,
491	            0.7
492	          ]
493	        ]
494	      },
495	      "K5": {
496	        "n_starts": 500,
497	        "best_objective": -27.515209774113806,
498	        "found_counterexample": true,
499	        "delta_pairs": [
500	          [
501	            0.0,
502	            0.2
503	          ],
504	          [
505	            0.0,
506	            0.5
507	          ],
508	          [
509	            0.1,
510	            0.3
511	          ],
512	          [
513	            0.2,
514	            0.5
515	          ],
516	          [
517	            0.3,
518	            0.7
519	          ]
520	        ]
521	      }
522	    },
523	    "frontdoor": {
524	      "K3": {
525	        "n_starts": 500,
526	        "best_objective": -0.0060568064726131965,
527	        "found_counterexample": true,
528	        "delta_pairs": [
529	          [
530	            0.0,
531	            0.2
532	          ],
533	          [
534	            0.0,
535	            0.5
536	          ],
537	          [
538	            0.1,
539	            0.3
540	          ],
541	          [
542	            0.2,
543	            0.5
544	          ],
545	          [
546	            0.3,
547	            0.7
548	          ]
549	        ]
550	      },
551	      "K5": {
552	        "n_starts": 500,
553	        "best_objective": -0.012339072616903042,
554	        "found_counterexample": true,
555	        "delta_pairs": [
556	          [
557	            0.0,
558	            0.2
559	          ],
560	          [
561	            0.0,
562	            0.5
563	          ],
564	          [
565	            0.1,
566	            0.3
567	          ],
568	          [
569	            0.2,
570	            0.5
571	          ],
572	          [
573	            0.3,
574	            0.7
575	          ]
576	        ]
577	      }
578	    }
579	  },
580	  "summary": "141514 violations across 210,000 random tests + 13 counterexamples found by adversarial search"
581	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e202d11-1a0c-4fa1-91c9-fc5c88c724ca",
  "isSidechain": true,
  "promptId": "3f772f34-432b-4b73-8d6a-c54bf571a4ba",
  "agentId": "a8ae618b752846327",
  "type": "user",
  "uuid": "7d651cf0-3e76-4dae-9916-577ad925f7ea",
  "sourceToolAssistantUUID": "9e202d11-1a0c-4fa1-91c9-fc5c88c724ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-22T12:18:12.349Z_

Now I have a thorough understanding of the original code, its DGP parameter structure, and the output format. The original has massive violations (141,514 across 210,000 tests) and found 13 adversarial counterexamples -- these are almost certainly Monte Carlo noise artifacts. Let me write the v2 script with analytic plim computation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d651cf0-3e76-4dae-9916-577ad925f7ea",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbPwjwfnEkeUd1jR7xX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21f8a234-cf14-436f-8729-2722ea56e5b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MmZimNGrNdW9vCf9xnp1C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 52446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5254,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T12:21:56.643Z_

<details open><summary>🔧 Tool call — Write · `toolu_01JrGKPa9eGe7vT97FKKYzf4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nExp-D v2: Conjecture 1 verification with ANALYTIC plim (zero sampling noise).\n\nThe original exp_d_conjecture_verify.py computed plim via sufficient statistics\nestimated from N=5M Monte Carlo simulation, introducing O(1/sqrt(N)) ~ 0.0004\nsampling noise. At MONO_TOL=1e-8, this generated ~141k false monotonicity\nviolations.\n\nThis v2 computes ALL sufficient statistics analytically (closed-form for\nconfounding/mediation/exposure, Gauss-Hermite quadrature for collider/mbias/\nfrontdoor/iv), eliminating sampling noise entirely.\n\nTopology-specific analytics:\n  - confounding: fully analytic (categorical A, linear T and Y)\n  - exposure:    fully analytic (categorical A, linear Y)\n  - mediation:   fully analytic (binary T, softmax A|T, linear Y)\n  - collider:    2D Gauss-Hermite over (T, eps_Y), both N(0,1)\n  - mbias:       2D Gauss-Hermite over (U1, U2), both N(0,1)\n  - frontdoor:   1D Gauss-Hermite over T ~ N(0, alpha_U^2 + 1)\n  - iv:          1D Gauss-Hermite over U ~ N(0,1), with binary Z\n\nOutput: exp_d_conjecture_results_v2.json (same structure as v1)\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\nimport sys\nimport os\nfrom scipy.special import roots_hermite, softmax as scipy_softmax\nfrom scipy.optimize import minimize as scipy_minimize\n\n# ====================================================================\n# Gauss-Hermite quadrature setup\n# ====================================================================\nN_GH = 100  # points per dimension -- machine precision for smooth integrands\n\n# roots_hermite: physicist's convention, weight = exp(-x^2)\n# integral f(x) exp(-x^2) dx ~ sum w_i f(x_i)\n# For N(0,1) expectation: E[f(X)] = (1/sqrt(pi)) sum w_i f(x_i * sqrt(2))\n_gh_x_raw, _gh_w_raw = roots_hermite(N_GH)\nGH_X = _gh_x_raw * np.sqrt(2)   # rescaled nodes for N(0,1)\nGH_W = _gh_w_raw / np.sqrt(np.pi)  # rescaled weights: sum w_i f(x_i) = E_{N(0,1)}[f]\n\n# Verify: E[1] should be 1.0, E[X^2] should be 1.0\nassert abs(GH_W.sum() - 1.0) < 1e-12, f\"GH weights sum to {GH_W.sum()}, expected 1.0\"\nassert abs((GH_W * GH_X**2).sum() - 1.0) < 1e-10, \"GH E[X^2] != 1.0\"\n\n# 2D quadrature: outer product of 1D grids\nGH_X2_a, GH_X2_b = np.meshgrid(GH_X, GH_X, indexing='ij')  # (N_GH, N_GH)\nGH_W2 = np.outer(GH_W, GH_W)  # (N_GH, N_GH)\nGH_X2_a_flat = GH_X2_a.ravel()\nGH_X2_b_flat = GH_X2_b.ravel()\nGH_W2_flat = GH_W2.ravel()\n\n# ====================================================================\n# Configuration\n# ====================================================================\nK_VALUES = [3, 5, 7]\nK_ADVERSARIAL = [3, 5]\nN_RANDOM = 10_000\nDELTA_STEP = 0.01\nSEED = 12345\nMONO_TOL = 1e-12  # much tighter than v1's 1e-8 since we have zero sampling noise\n\nALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',\n             'mbias', 'iv', 'frontdoor']\nTOPO_IDX = {t: i for i, t in enumerate(ALL_TOPOS)}\nNON_DECREASING = {'confounding', 'mediation', 'exposure', 'frontdoor', 'iv'}\nNON_INCREASING = {'collider', 'mbias'}\n\nADV_DELTA_PAIRS = [(0.0, 0.2), (0.0, 0.5), (0.1, 0.3), (0.2, 0.5), (0.3, 0.7)]\nADV_N_STARTS = 100\n\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\n\n# ====================================================================\n# DGP Parameter Pools (identical to v1)\n# ====================================================================\n_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]\n_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]\n_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]\n_MBIAS_A1_POOL = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]\n_MBIAS_A2_POOL = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]\n_IV_DZ_POOL = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]\n_IV_DU_POOL = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]\n_FD_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]\n_FD_DELTA_POOL = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]\n\n\ndef make_p_A(K):\n    if K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    raw = np.array([1.0 / i for i in range(1, K + 1)])\n    return raw / raw.sum()\n\n\ndef make_all_params(K):\n    p_A = make_p_A(K)\n    return dict(\n        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K - 1]),\n                         beta_A=np.array(_BETA_A_POOL[:K - 1]), beta_T=2.0, sigma_T=1.0),\n        mediation=dict(tau=0.5, gamma=np.array(_GAMMA_POOL[:K]),\n                       delta=np.array(_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),\n        collider=dict(tau=1.0, g=np.zeros(K), dT=np.array(_DT_POOL[:K]),\n                      dY=np.array(_DY_POOL[:K])),\n        exposure=dict(beta=np.array(_BETA_POOL[:K]), p_A=p_A),\n        mbias=dict(tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),\n                   a1=np.array(_MBIAS_A1_POOL[:K]), a2=np.array(_MBIAS_A2_POOL[:K])),\n        iv=dict(lam=1.0, g=np.zeros(K), dZ=np.array(_IV_DZ_POOL[:K]),\n                dU=np.array(_IV_DU_POOL[:K]), beta=np.array(_BETA_POOL[:K])),\n        frontdoor=dict(alpha_U=1.0, lam_U=1.0, gamma=np.array(_FD_GAMMA_POOL[:K]),\n                       delta=np.array(_FD_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),\n    )\n\n\n# ====================================================================\n# Stable softmax utility\n# ====================================================================\ndef _softmax(logits):\n    \"\"\"Softmax along last axis, numerically stable.\"\"\"\n    e = np.exp(logits - np.max(logits, axis=-1, keepdims=True))\n    return e / np.sum(e, axis=-1, keepdims=True)\n\n\n# ====================================================================\n# Analytic Sufficient Statistics classes\n# ====================================================================\nclass AnalyticSuffStats:\n    \"\"\"Population moments for OLS topologies (with or without T).\"\"\"\n    def __init__(self, K, has_T=True):\n        self.K = K\n        self.has_T = has_T\n        self.p_A = None   # K-vector: P(A=k)\n        self.E_Y = None   # scalar\n        self.E_YD = None  # K-vector: E[Y * 1(A=k)]\n        if has_T:\n            self.E_T = None   # scalar\n            self.E_T2 = None  # scalar: E[T^2]\n            self.E_TY = None  # scalar: E[T*Y]\n            self.E_TD = None  # K-vector: E[T * 1(A=k)]\n\n\nclass AnalyticIVSuffStats:\n    \"\"\"Population moments for IV topology (Wald estimator).\"\"\"\n    def __init__(self, K):\n        self.K = K\n        self.RF = None   # E[Y|Z=1] - E[Y|Z=0]\n        self.FS = None   # K-vector: P(A=k|Z=1) - P(A=k|Z=0)\n\n\n# ====================================================================\n# Topology 1: Confounding -- FULLY ANALYTIC\n# ====================================================================\n# DGP: A ~ Cat(p_A), T = sum_{j=1}^{K-1} alpha_j D_j + eps_T,\n#       Y = beta_T * T + sum_{j=1}^{K-1} beta_A_j D_j + eps_Y\n# D_j = 1(A=j+1) for j=0,...,K-2 (ref category A=0)\n# Wait -- looking at original code more carefully:\n#   D[:, j] = (A == j + 1) for j in range(K-1)\n# So D_j = 1(A = j+1), j=0,...,K-2\n# T = D @ alpha + eps_T = sum_{j=0}^{K-2} alpha_j * 1(A=j+1) + eps_T\n# Y = beta_T * T + D @ beta_A + eps_Y = beta_T * T + sum_{j=0}^{K-2} beta_A_j * 1(A=j+1) + eps_Y\n#\n# For the plim regression Y ~ 1 + T + D*_1 + ... + D*_{K-1}:\n# D*_j = 1(A* = j) for j=1,...,K-1 (ref category A*=0)\n# The sufficient stats use A (not A*), and the C matrix maps A->A*.\n# Actually looking at the SuffStats class: DA[:, k] = (A == k) for k=0,...,K-1\n# So p_A[k] = P(A=k), E_TD[k] = E[T * 1(A=k)], E_YD[k] = E[Y * 1(A=k)]\n\ndef compute_confounding_ss(K, p):\n    \"\"\"Analytic sufficient stats for confounding topology.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    p_A = p['p_A']       # K-vector\n    alpha = p['alpha']    # (K-1)-vector: alpha_0,...,alpha_{K-2}\n    beta_A = p['beta_A']  # (K-1)-vector\n    beta_T = p['beta_T']\n    sigma_T = p['sigma_T']\n\n    ss.p_A = p_A.copy()\n\n    # E[T] = sum_{j=0}^{K-2} alpha_j * P(A=j+1)\n    # (since eps_T has mean 0)\n    ss.E_T = sum(alpha[j] * p_A[j + 1] for j in range(K - 1))\n\n    # E[T^2] = E[(sum alpha_j D_j)^2] + sigma_T^2\n    # = sum_j alpha_j^2 P(A=j+1) + sigma_T^2\n    # (since D_j D_k = 0 for j!=k, D_j^2 = D_j)\n    ss.E_T2 = sum(alpha[j]**2 * p_A[j + 1] for j in range(K - 1)) + sigma_T**2\n\n    # E[T * 1(A=k)]:\n    # For k=0: E[(sum alpha_j D_j + eps_T) * 1(A=0)]\n    #        = sum_j alpha_j E[D_j * 1(A=0)] + E[eps_T * 1(A=0)]\n    #        = 0 + 0 = 0  (since D_j=1(A=j+1) and A=0 => D_j=0, and eps_T indep of A)\n    # Actually eps_T is independent of A, so E[eps_T * 1(A=k)] = 0 * P(A=k) = 0\n    # For k>=1: E[(sum_j alpha_j D_j + eps_T) * 1(A=k)]\n    #         = alpha_{k-1} * P(A=k) + 0\n    ss.E_TD = np.zeros(K)\n    for k in range(1, K):\n        ss.E_TD[k] = alpha[k - 1] * p_A[k]\n\n    # E[Y] = beta_T * E[T] + sum_{j=0}^{K-2} beta_A_j * P(A=j+1)\n    ss.E_Y = beta_T * ss.E_T + sum(beta_A[j] * p_A[j + 1] for j in range(K - 1))\n\n    # E[Y * 1(A=k)] = beta_T * E[T * 1(A=k)] + sum_j beta_A_j * E[D_j * 1(A=k)] + E[eps_Y * 1(A=k)]\n    # E[D_j * 1(A=k)] = P(A=j+1, A=k) = P(A=k) if j+1=k else 0\n    # E[eps_Y * 1(A=k)] = 0\n    # So for k=0: E[Y * 1(A=0)] = beta_T * 0 + 0 + 0 = 0 ... wait that's wrong\n    # Actually: Y = beta_T * T + sum beta_A_j D_j + eps_Y\n    # E[Y * 1(A=0)] = beta_T * E[T * 1(A=0)] + sum_j beta_A_j * E[D_j * 1(A=0)] + E[eps_Y * 1(A=0)]\n    #               = beta_T * 0 + 0 + 0 = 0\n    # Hmm, that gives E_Y = sum_k E[Y * 1(A=k)] = 0 + sum_{k>=1} stuff, but we need E_Y correctly.\n    # Let me reconsider: the intercept in the Y equation.\n    # gen_confounding: Y = beta_T * T + D @ beta_A + eps_Y\n    # There's no explicit intercept in Y. So E[Y | A=0] = beta_T * E[T | A=0] + 0\n    # E[T | A=0] = 0 (since all alpha terms vanish) + E[eps_T] = 0\n    # So E[Y * 1(A=0)] = E[Y | A=0] * P(A=0) = 0 * p_A[0] = 0\n    # That seems correct.\n\n    # For k >= 1:\n    # E[Y * 1(A=k)] = beta_T * E[T * 1(A=k)] + beta_A[k-1] * P(A=k)\n    ss.E_YD = np.zeros(K)\n    for k in range(1, K):\n        ss.E_YD[k] = beta_T * ss.E_TD[k] + beta_A[k - 1] * p_A[k]\n    # k=0: already 0\n\n    # E[TY] = E[T * (beta_T * T + sum beta_A_j D_j + eps_Y)]\n    #        = beta_T * E[T^2] + sum_j beta_A_j * E[T * D_j] + E[T * eps_Y]\n    #        = beta_T * E[T^2] + sum_j beta_A_j * E[T * 1(A=j+1)] + 0\n    ss.E_TY = beta_T * ss.E_T2 + sum(beta_A[j] * ss.E_TD[j + 1] for j in range(K - 1))\n\n    return ss\n\n\n# ====================================================================\n# Topology 2: Exposure -- FULLY ANALYTIC\n# ====================================================================\n# DGP: A ~ Cat(p_A), Y = beta[0] + D @ beta[1:] + eps_Y\n# No T variable.\n\ndef compute_exposure_ss(K, p):\n    \"\"\"Analytic sufficient stats for exposure topology.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=False)\n    p_A = p['p_A']\n    beta = p['beta']  # K-vector: beta[0] is intercept\n\n    ss.p_A = p_A.copy()\n\n    # E[Y] = beta[0] + sum_{j=1}^{K-1} beta[j] * P(A=j)\n    ss.E_Y = beta[0] + sum(beta[j] * p_A[j] for j in range(1, K))\n\n    # E[Y * 1(A=k)] = E[(beta[0] + sum_j beta[j] D_j + eps_Y) * 1(A=k)]\n    # = beta[0] * P(A=k) + beta[k] * P(A=k) (if k>=1) + 0\n    # For k=0: = beta[0] * P(A=0) + 0 = beta[0] * p_A[0]\n    ss.E_YD = np.zeros(K)\n    ss.E_YD[0] = beta[0] * p_A[0]\n    for k in range(1, K):\n        ss.E_YD[k] = (beta[0] + beta[k]) * p_A[k]\n\n    return ss\n\n\n# ====================================================================\n# Topology 3: Mediation -- FULLY ANALYTIC (T is binary)\n# ====================================================================\n# DGP: T ~ Bern(0.5), A | T ~ Cat(softmax(gamma + delta * T))\n#       Y = beta[0] + D @ beta[1:] + tau * T + eps_Y\n# D_j = 1(A = j+1) for j=0,...,K-2\n\ndef compute_mediation_ss(K, p):\n    \"\"\"Analytic sufficient stats for mediation topology.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    tau = p['tau']\n    gamma = p['gamma']  # K-vector\n    delta_coef = p['delta']   # K-vector\n    beta = p['beta']    # K-vector\n\n    # P(A=k | T=t) = softmax(gamma + delta * t)[k]\n    probs_T0 = _softmax(gamma)          # K-vector\n    probs_T1 = _softmax(gamma + delta_coef)  # K-vector\n\n    # P(A=k) = 0.5 * P(A=k|T=0) + 0.5 * P(A=k|T=1)\n    ss.p_A = 0.5 * probs_T0 + 0.5 * probs_T1\n\n    # E[T] = 0.5, E[T^2] = 0.5 (since T is Bernoulli(0.5))\n    ss.E_T = 0.5\n    ss.E_T2 = 0.5\n\n    # E[T * 1(A=k)] = E[T * 1(A=k)]\n    # = 0.5 * 0 * P(A=k|T=0) + 0.5 * 1 * P(A=k|T=1)\n    # = 0.5 * probs_T1[k]\n    ss.E_TD = 0.5 * probs_T1\n\n    # E[Y] = beta[0] + sum_{k=1}^{K-1} beta[k] * P(A=k) + tau * E[T]\n    # Wait, gen_mediation:\n    #   Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + eps_Y\n    # D_j = 1(A=j+1), so D @ beta[1:] = sum_{j=0}^{K-2} beta[j+1] * 1(A=j+1)\n    # = sum_{k=1}^{K-1} beta[k] * 1(A=k)\n    ss.E_Y = beta[0] + sum(beta[k] * ss.p_A[k] for k in range(1, K)) + tau * 0.5\n\n    # E[Y * 1(A=k)] for each k:\n    # Y = beta[0] + sum_j beta[j+1]*D_j + tau*T + eps_Y\n    # E[Y * 1(A=k)] = E[(beta[0] + beta[k]*1(k>=1) + tau*T + eps_Y) * 1(A=k)]\n    # = (beta[0] + beta[k]*(k>=1)) * P(A=k) + tau * E[T * 1(A=k)]\n\n    ss.E_YD = np.zeros(K)\n    for k in range(K):\n        beta_k = beta[k] if k >= 1 else 0.0\n        ss.E_YD[k] = (beta[0] + beta_k) * ss.p_A[k] + tau * ss.E_TD[k]\n\n    # E[TY] = E[T * (beta[0] + sum beta[k]*1(A=k) + tau*T + eps_Y)]\n    # = beta[0] * E[T] + sum_{k=1}^{K-1} beta[k] * E[T * 1(A=k)] + tau * E[T^2] + 0\n    ss.E_TY = beta[0] * 0.5 + sum(beta[k] * ss.E_TD[k] for k in range(1, K)) + tau * 0.5\n\n    return ss\n\n\n# ====================================================================\n# Topology 4: Collider -- 2D GAUSS-HERMITE\n# ====================================================================\n# DGP: T ~ N(0,1), eps_Y ~ N(0,1) independent\n#       Y = tau * T + eps_Y\n#       A | T, Y ~ Cat(softmax(g + dT * T + dY * Y))\n#\n# Reparametrize: let Z1=T, Z2=eps_Y, both N(0,1) independent\n# Y = tau * Z1 + Z2\n# A | Z1, Z2 ~ Cat(softmax(g + dT * Z1 + dY * (tau * Z1 + Z2)))\n#            = Cat(softmax(g + (dT + tau * dY) * Z1 + dY * Z2))\n\ndef compute_collider_ss(K, p):\n    \"\"\"Analytic sufficient stats for collider via 2D GH quadrature.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    tau = p['tau']\n    g = p['g']      # K-vector\n    dT = p['dT']    # K-vector\n    dY = p['dY']    # K-vector\n\n    # Quadrature over (Z1, Z2) = (T, eps_Y), both N(0,1)\n    # Logits for each quadrature point: g + (dT + tau*dY) * Z1 + dY * Z2\n    coeff1 = dT + tau * dY   # K-vector: coefficient of Z1\n    coeff2 = dY               # K-vector: coefficient of Z2\n\n    # Compute softmax probabilities at each quadrature point\n    # logits shape: (N_GH^2, K)\n    logits = (g[None, :]\n              + coeff1[None, :] * GH_X2_a_flat[:, None]\n              + coeff2[None, :] * GH_X2_b_flat[:, None])\n    probs = _softmax(logits)  # (N_GH^2, K)\n\n    # T = Z1, Y = tau * Z1 + Z2\n    T_vals = GH_X2_a_flat\n    Y_vals = tau * GH_X2_a_flat + GH_X2_b_flat\n\n    # Weighted expectations\n    w = GH_W2_flat  # (N_GH^2,)\n\n    ss.p_A = (w[:, None] * probs).sum(axis=0)\n    ss.E_TD = (w[:, None] * T_vals[:, None] * probs).sum(axis=0)\n    ss.E_YD = (w[:, None] * Y_vals[:, None] * probs).sum(axis=0)\n\n    # Moments of T and Y (independent of A, can compute analytically):\n    ss.E_T = 0.0\n    ss.E_T2 = 1.0\n    ss.E_Y = 0.0  # E[tau*T + eps] = 0\n    ss.E_TY = tau  # E[T(tau*T + eps)] = tau * E[T^2] = tau\n\n    return ss\n\n\n# ====================================================================\n# Topology 5: M-bias -- 2D GAUSS-HERMITE\n# ====================================================================\n# DGP: U1, U2 ~ N(0,1) independent\n#       T = delta_coef * U1 + eta, eta ~ N(0,1)\n#       Y = tau * T + lam * U2 + eps_Y, eps_Y ~ N(0,1)\n#       A | U1, U2 ~ Cat(softmax(g + a1 * U1 + a2 * U2))\n#\n# Note: T and Y depend on (U1, U2, eta, eps_Y) but A only depends on (U1, U2).\n# Since eta, eps_Y are independent of (U1, U2, A):\n#   E[T * 1(A=k)] = delta_coef * E[U1 * 1(A=k)] + E[eta * 1(A=k)]\n#                  = delta_coef * E[U1 * 1(A=k)]  (eta indep of A)\n#\n#   E[Y * 1(A=k)] = tau * E[T * 1(A=k)] + lam * E[U2 * 1(A=k)] + 0\n#\n# So we need 2D GH over (U1, U2) to compute:\n#   P(A=k), E[U1 * 1(A=k)], E[U2 * 1(A=k)]\n\ndef compute_mbias_ss(K, p):\n    \"\"\"Analytic sufficient stats for M-bias via 2D GH quadrature.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    tau = p['tau']\n    delta_coef = p['delta_coef']\n    lam = p['lam']\n    g = p['g']\n    a1 = p['a1']\n    a2 = p['a2']\n\n    # Logits: g + a1 * U1 + a2 * U2\n    logits = (g[None, :]\n              + a1[None, :] * GH_X2_a_flat[:, None]\n              + a2[None, :] * GH_X2_b_flat[:, None])\n    probs = _softmax(logits)  # (N_GH^2, K)\n\n    w = GH_W2_flat\n    U1_vals = GH_X2_a_flat\n    U2_vals = GH_X2_b_flat\n\n    ss.p_A = (w[:, None] * probs).sum(axis=0)\n    E_U1_Dk = (w[:, None] * U1_vals[:, None] * probs).sum(axis=0)  # E[U1 * 1(A=k)]\n    E_U2_Dk = (w[:, None] * U2_vals[:, None] * probs).sum(axis=0)  # E[U2 * 1(A=k)]\n\n    # E[T * 1(A=k)] = delta_coef * E[U1 * 1(A=k)]\n    ss.E_TD = delta_coef * E_U1_Dk\n\n    # E[Y * 1(A=k)] = tau * E[T * 1(A=k)] + lam * E[U2 * 1(A=k)]\n    ss.E_YD = tau * ss.E_TD + lam * E_U2_Dk\n\n    # Marginal moments:\n    # E[T] = 0 (since E[U1]=0, E[eta]=0)\n    # E[T^2] = delta_coef^2 * E[U1^2] + E[eta^2] = delta_coef^2 + 1\n    # E[Y] = 0\n    # E[TY] = tau * E[T^2] + lam * E[T*U2]\n    # E[T*U2] = E[(delta_coef * U1 + eta) * U2] = 0 (all independent)\n    ss.E_T = 0.0\n    ss.E_T2 = delta_coef**2 + 1.0\n    ss.E_Y = 0.0\n    ss.E_TY = tau * ss.E_T2\n\n    return ss\n\n\n# ====================================================================\n# Topology 6: Front-door -- 1D GAUSS-HERMITE\n# ====================================================================\n# DGP: U ~ N(0,1), T = alpha_U * U + eta (eta ~ N(0,1))\n#       M | T ~ Cat(softmax(gamma + delta * T))  -- M is the \"annotator\" variable\n#       Y = D_M @ beta[1:] + lam_U * U + eps_Y\n# where D_M[j] = 1(M=j+1), j=0,...,K-2\n#\n# The regression is Y ~ 1 + T + D*_1 + ... + D*_{K-1}\n# (M plays the role of A in the plim computation)\n#\n# T ~ N(0, sigma_T^2) where sigma_T^2 = alpha_U^2 + 1\n# We do 1D GH over T (after rescaling for its variance).\n#\n# For the moments involving U:\n# E[U | T] = Cov(U,T)/Var(T) * T = alpha_U / (alpha_U^2 + 1) * T\n# (since Cov(U,T) = alpha_U, Var(T) = alpha_U^2 + 1)\n#\n# P(M=k) = E_T[softmax(gamma + delta * T)[k]]\n# E[T * 1(M=k)] = E_T[T * softmax(gamma + delta * T)[k]]\n# E[Y * 1(M=k)] = E[E[Y | T, M] * 1(M=k)]\n#               = E_T[ E[Y|T,M=k] * softmax(gamma+delta*T)[k] ]\n# E[Y|T,M=k] = beta[k] (if k>=1, else 0 for the intercept part from D_M)\n#              + lam_U * E[U|T] + 0\n# Wait, let me reconsider:\n# Y = sum_{j=0}^{K-2} beta[j+1] * 1(M=j+1) + lam_U * U + eps_Y\n# (from gen_frontdoor: Y = D @ beta[1:] + lam_U * U + eps_Y,\n#  where beta = p['beta'] and D[j] = 1(M=j+1))\n# There's no intercept beta[0] in the Y equation in gen_frontdoor!\n# Let me re-check: gen_frontdoor has Y = D @ p['beta'][1:] + p['lam_U'] * U + eps_Y\n# So Y = sum_{k=1}^{K-1} beta[k] * 1(M=k) + lam_U * U + eps_Y\n#\n# E[Y * 1(M=k)] = beta[k] * P(M=k) (for k>=1) + lam_U * E[U * 1(M=k)] + 0\n# For k=0: E[Y * 1(M=0)] = 0 + lam_U * E[U * 1(M=0)] + 0\n\ndef compute_frontdoor_ss(K, p):\n    \"\"\"Analytic sufficient stats for front-door via 1D GH quadrature.\"\"\"\n    ss = AnalyticSuffStats(K, has_T=True)\n    alpha_U = p['alpha_U']\n    lam_U = p['lam_U']\n    gamma = p['gamma']\n    delta_coef = p['delta']\n    beta = p['beta']\n\n    sigma_T2 = alpha_U**2 + 1.0\n    sigma_T = np.sqrt(sigma_T2)\n\n    # 1D GH over T ~ N(0, sigma_T^2): rescale nodes\n    T_nodes = GH_X * sigma_T  # (N_GH,)\n    T_weights = GH_W          # (N_GH,) -- already normalized for E_{N(0,1)}\n\n    # softmax(gamma + delta * T) at each T node\n    # logits shape: (N_GH, K)\n    logits = gamma[None, :] + delta_coef[None, :] * T_nodes[:, None]\n    probs = _softmax(logits)  # (N_GH, K)\n\n    # P(M=k) = E_T[softmax(gamma + delta * T)[k]]\n    ss.p_A = (T_weights[:, None] * probs).sum(axis=0)\n\n    # E[T * 1(M=k)] = E_T[T * softmax(gamma + delta * T)[k]]\n    ss.E_TD = (T_weights[:, None] * T_nodes[:, None] * probs).sum(axis=0)\n\n    # E[U * 1(M=k)] via the law of iterated expectations:\n    # E[U * 1(M=k)] = E_T[ E[U|T] * P(M=k|T) ]\n    # E[U|T] = alpha_U / sigma_T^2 * T\n    E_U_given_T = alpha_U / sigma_T2 * T_nodes  # (N_GH,)\n    E_U_Mk = (T_weights[:, None] * E_U_given_T[:, None] * probs).sum(axis=0)\n\n    # E[Y * 1(M=k)] = beta[k] * P(M=k) (for k>=1) + lam_U * E[U * 1(M=k)]\n    ss.E_YD = np.zeros(K)\n    for k in range(K):\n        beta_k = beta[k] if k >= 1 else 0.0\n        ss.E_YD[k] = beta_k * ss.p_A[k] + lam_U * E_U_Mk[k]\n\n    # Marginal moments:\n    # E[T] = 0\n    # E[T^2] = sigma_T^2\n    # E[Y] = sum_{k=1}^{K-1} beta[k] * P(M=k) + lam_U * E[U] + 0\n    #       = sum_{k=1}^{K-1} beta[k] * P(M=k)\n    ss.E_T = 0.0\n    ss.E_T2 = sigma_T2\n    ss.E_Y = sum(beta[k] * ss.p_A[k] for k in range(1, K))\n\n    # E[TY] = sum_{k=1}^{K-1} beta[k] * E[T * 1(M=k)] + lam_U * E[T*U] + E[T*eps_Y]\n    # E[T*U] = Cov(T,U) = alpha_U (since both mean 0)\n    # E[T*eps_Y] = 0\n    ss.E_TY = sum(beta[k] * ss.E_TD[k] for k in range(1, K)) + lam_U * alpha_U\n\n    return ss\n\n\n# ====================================================================\n# Topology 7: IV -- 1D GAUSS-HERMITE over U, binary Z\n# ====================================================================\n# DGP: Z ~ Bern(0.5), U ~ N(0,1), eps_Y ~ N(0,1)\n#       A | Z, U ~ Cat(softmax(g + dZ * Z + dU * U))\n#       Y = sum_{k=1}^{K-1} beta[k] * 1(A=k) + lam * U + eps_Y\n#\n# Wald estimator: tau_hat = RF / FS*[1]\n# RF = E[Y|Z=1] - E[Y|Z=0]\n# FS[k] = P(A=k|Z=1) - P(A=k|Z=0)\n#\n# P(A=k|Z=z) = E_U[softmax(g + dZ * z + dU * U)[k]]\n# E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z) + lam * E[U] + E[eps]\n#           = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)\n\ndef compute_iv_ss(K, p):\n    \"\"\"Analytic sufficient stats for IV via 1D GH quadrature.\"\"\"\n    ivss = AnalyticIVSuffStats(K)\n    g = p['g']\n    dZ = p['dZ']\n    dU = p['dU']\n    beta = p['beta']\n    lam = p['lam']\n\n    # P(A=k|Z=z) for z=0 and z=1\n    # logits for Z=0: g + dU * U\n    logits_z0 = g[None, :] + dU[None, :] * GH_X[:, None]  # (N_GH, K)\n    probs_z0 = _softmax(logits_z0)\n    P_A_z0 = (GH_W[:, None] * probs_z0).sum(axis=0)  # K-vector\n\n    logits_z1 = g[None, :] + dZ[None, :] + dU[None, :] * GH_X[:, None]\n    probs_z1 = _softmax(logits_z1)\n    P_A_z1 = (GH_W[:, None] * probs_z1).sum(axis=0)  # K-vector\n\n    # First stage\n    ivss.FS = P_A_z1 - P_A_z0  # K-vector\n\n    # Reduced form\n    # E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)\n    # (lam * E[U] = 0, E[eps] = 0, beta[0] cancels out since it's not in gen_iv)\n    # Actually gen_iv: Y = D @ p['beta'][1:] + p['lam'] * U + eps\n    # So Y = sum_{k=1}^{K-1} beta[k] * 1(A=k) + lam * U + eps\n    # E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)\n    E_Y_z0 = sum(beta[k] * P_A_z0[k] for k in range(1, K))\n    E_Y_z1 = sum(beta[k] * P_A_z1[k] for k in range(1, K))\n\n    ivss.RF = E_Y_z1 - E_Y_z0\n\n    return ivss\n\n\n# ====================================================================\n# Plim computation (from original, unchanged)\n# ====================================================================\ndef plim_ols_with_T(C, ss):\n    \"\"\"Plim of OLS regression Y ~ 1 + T + D*_1 + ... + D*_{K-1}.\"\"\"\n    K = ss.K\n    q = C @ ss.p_A        # misclassified P(A*=k)\n    ct = C @ ss.E_TD       # E[T * 1(A*=k)]\n    cy = C @ ss.E_YD       # E[Y * 1(A*=k)]\n    dim = K + 1\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1] = ss.E_T\n    EZZ[1, 0] = ss.E_T\n    EZZ[1, 1] = ss.E_T2\n    EZZ[0, 2:] = q[1:]\n    EZZ[2:, 0] = q[1:]\n    EZZ[1, 2:] = ct[1:]\n    EZZ[2:, 1] = ct[1:]\n    for j in range(K - 1):\n        EZZ[j + 2, j + 2] = q[j + 1]\n    EZY = np.zeros(dim)\n    EZY[0] = ss.E_Y\n    EZY[1] = ss.E_TY\n    EZY[2:] = cy[1:]\n    try:\n        return np.linalg.solve(EZZ, EZY)\n    except np.linalg.LinAlgError:\n        return np.full(dim, np.nan)\n\n\ndef plim_ols_exposure(C, ss):\n    \"\"\"Plim of OLS regression Y ~ 1 + D*_1 + ... + D*_{K-1}.\"\"\"\n    K = ss.K\n    q = C @ ss.p_A\n    cy = C @ ss.E_YD\n    dim = K\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1:] = q[1:]\n    EZZ[1:, 0] = q[1:]\n    for j in range(K - 1):\n        EZZ[j + 1, j + 1] = q[j + 1]\n    EZY = np.zeros(dim)\n    EZY[0] = ss.E_Y\n    EZY[1:] = cy[1:]\n    try:\n        return np.linalg.solve(EZZ, EZY)\n    except np.linalg.LinAlgError:\n        return np.full(dim, np.nan)\n\n\ndef plim_iv_single(C, ss):\n    \"\"\"Plim of Wald IV estimator with misclassified A.\"\"\"\n    FS_star = C @ ss.FS\n    if abs(FS_star[1]) < 1e-15:\n        return np.nan\n    return ss.RF / FS_star[1]\n\n\ndef get_tau_at_C(topo, C, ss):\n    if topo == 'iv':\n        return plim_iv_single(C, ss)\n    elif topo == 'exposure':\n        return plim_ols_exposure(C, ss)[1]\n    else:\n        return plim_ols_with_T(C, ss)[1]\n\n\ndef get_tau_true(topo, K, params, ss):\n    \"\"\"True causal parameter.\n\n    For correctly-identified topologies: tau_true = plim(I).\n    For protective topologies (collider, mbias): tau_true = DGP tau,\n    so B(0) = plim(I) - tau != 0 (existing bias from Berkson/M-bias).\n    \"\"\"\n    p = params[topo]\n    if topo == 'collider':\n        return p['tau']\n    elif topo == 'mbias':\n        return p['tau']\n    else:\n        return get_tau_at_C(topo, np.eye(K), ss)\n\n\n# ====================================================================\n# Batched bias curve computation (from original, unchanged)\n# ====================================================================\ndef compute_bias_curve(topo, C0, ss, tau_true, delta_step=DELTA_STEP):\n    K = C0.shape[0]\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        delta_max = 10.0\n    else:\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\n\n    deltas = np.arange(0, delta_max + delta_step / 2, delta_step)\n    n = len(deltas)\n    d = deltas[:, None]\n\n    if topo == 'iv':\n        FS0 = C0 @ ss.FS\n        fs_star = (1 - d) * ss.FS[None, :] + d * FS0[None, :]\n        denom = fs_star[:, 1]\n        taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)\n    elif topo == 'exposure':\n        pA0 = C0 @ ss.p_A\n        YD0 = C0 @ ss.E_YD\n        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]\n        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]\n        dim = K\n        EZZ = np.zeros((n, dim, dim))\n        EZZ[:, 0, 0] = 1.0\n        EZZ[:, 0, 1:] = q[:, 1:]\n        EZZ[:, 1:, 0] = q[:, 1:]\n        for j in range(K - 1):\n            EZZ[:, j + 1, j + 1] = q[:, j + 1]\n        EZY = np.zeros((n, dim))\n        EZY[:, 0] = ss.E_Y\n        EZY[:, 1:] = cy[:, 1:]\n        try:\n            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]\n            taus = coefs[:, 1]\n        except np.linalg.LinAlgError:\n            taus = np.full(n, np.nan)\n    else:\n        pA0 = C0 @ ss.p_A\n        TD0 = C0 @ ss.E_TD\n        YD0 = C0 @ ss.E_YD\n        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]\n        ct = (1 - d) * ss.E_TD[None, :] + d * TD0[None, :]\n        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]\n        dim = K + 1\n        EZZ = np.zeros((n, dim, dim))\n        EZZ[:, 0, 0] = 1.0\n        EZZ[:, 0, 1] = ss.E_T\n        EZZ[:, 1, 0] = ss.E_T\n        EZZ[:, 1, 1] = ss.E_T2\n        EZZ[:, 0, 2:] = q[:, 1:]\n        EZZ[:, 2:, 0] = q[:, 1:]\n        EZZ[:, 1, 2:] = ct[:, 1:]\n        EZZ[:, 2:, 1] = ct[:, 1:]\n        for j in range(K - 1):\n            EZZ[:, j + 2, j + 2] = q[:, j + 1]\n        EZY = np.zeros((n, dim))\n        EZY[:, 0] = ss.E_Y\n        EZY[:, 1] = ss.E_TY\n        EZY[:, 2:] = cy[:, 1:]\n        try:\n            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]\n            taus = coefs[:, 1]\n        except np.linalg.LinAlgError:\n            taus = np.full(n, np.nan)\n\n    bias_abs = np.abs(taus - tau_true)\n    return deltas, bias_abs\n\n\ndef check_monotonicity(bias_abs, topo, tol=MONO_TOL):\n    valid = ~np.isnan(bias_abs)\n    ba = bias_abs[valid]\n    if len(ba) < 2:\n        return 0\n    diffs = np.diff(ba)\n    if topo in NON_DECREASING:\n        return int(np.sum(diffs < -tol))\n    else:\n        return int(np.sum(diffs > tol))\n\n\n# ====================================================================\n# Precompute analytic sufficient statistics\n# ====================================================================\n_COMPUTE_SS = {\n    'confounding': lambda K, p: compute_confounding_ss(K, p),\n    'mediation':   lambda K, p: compute_mediation_ss(K, p),\n    'collider':    lambda K, p: compute_collider_ss(K, p),\n    'exposure':    lambda K, p: compute_exposure_ss(K, p),\n    'mbias':       lambda K, p: compute_mbias_ss(K, p),\n    'iv':          lambda K, p: compute_iv_ss(K, p),\n    'frontdoor':   lambda K, p: compute_frontdoor_ss(K, p),\n}\n\n\ndef precompute_all():\n    print(\"\\nPrecomputing analytic sufficient statistics...\")\n    sys.stdout.flush()\n    t0 = time.time()\n    all_ss = {}\n    all_tau_true = {}\n\n    for K in K_VALUES:\n        params = make_all_params(K)\n        for topo in ALL_TOPOS:\n            ss = _COMPUTE_SS[topo](K, params[topo])\n            tau_true = get_tau_true(topo, K, params, ss)\n            all_ss[(topo, K)] = ss\n            all_tau_true[(topo, K)] = tau_true\n\n    print(\"  Done ({:.3f}s). tau_true values:\".format(time.time() - t0))\n    for topo in ALL_TOPOS:\n        vals = [all_tau_true[(topo, K)] for K in K_VALUES]\n        vals_s = \", \".join(\n            f\"K{K}={v:.10f}\" if v is not None and not np.isnan(v) else f\"K{K}=NaN\"\n            for K, v in zip(K_VALUES, vals))\n        direction = \"non-dec\" if topo in NON_DECREASING else \"non-inc\"\n        print(f\"    {topo:<14} [{direction}] {vals_s}\")\n    sys.stdout.flush()\n    return all_ss, all_tau_true\n\n\n# ====================================================================\n# Part 1: Random Verification\n# ====================================================================\ndef part1_random(all_ss, all_tau_true):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 1: Random Verification ({:,} C0 per topology x K)\".format(N_RANDOM))\n    print(\"  MONO_TOL = {:.0e} (analytic -- zero sampling noise)\".format(MONO_TOL))\n    print(\"=\" * 70)\n    sys.stdout.flush()\n\n    results = {}\n    total_tests = 0\n    total_violations = 0\n\n    for K in K_VALUES:\n        print(f\"\\n  K = {K}\")\n        print(f\"  {'Topology':<14} {'Direction':<10} {'Tested':>8} \"\n              f\"{'Violations':>11} {'NaN_curves':>11} {'Worst_mag':>12} {'Time':>7}\")\n        print(f\"  {'-' * 75}\")\n        sys.stdout.flush()\n\n        for topo in ALL_TOPOS:\n            t0 = time.time()\n            ss = all_ss[(topo, K)]\n            tau_true = all_tau_true[(topo, K)]\n\n            rng_C = np.random.default_rng(SEED * 2 + K * 1000 + TOPO_IDX[topo])\n            violations = 0\n            nan_curves = 0\n            worst_mag = 0.0\n\n            for i in range(N_RANDOM):\n                C0 = np.zeros((K, K))\n                for j in range(K):\n                    C0[:, j] = rng_C.dirichlet(np.ones(K))\n\n                _, bias_abs = compute_bias_curve(topo, C0, ss, tau_true)\n\n                n_nan = np.isnan(bias_abs).sum()\n                if n_nan > len(bias_abs) * 0.5:\n                    nan_curves += 1\n                    continue\n\n                n_viol = check_monotonicity(bias_abs, topo)\n                if n_viol > 0:\n                    violations += 1\n                    valid = ~np.isnan(bias_abs)\n                    ba = bias_abs[valid]\n                    diffs = np.diff(ba)\n                    if topo in NON_DECREASING:\n                        worst_mag = max(worst_mag, abs(diffs.min()))\n                    else:\n                        worst_mag = max(worst_mag, diffs.max())\n\n            elapsed = time.time() - t0\n            direction = \"non-dec\" if topo in NON_DECREASING else \"non-inc\"\n            print(f\"  {topo:<14} {direction:<10} {N_RANDOM:>8} \"\n                  f\"{violations:>11} {nan_curves:>11} {worst_mag:>12.2e} {elapsed:>6.1f}s\")\n            sys.stdout.flush()\n\n            results[f\"{topo}_K{K}\"] = {\n                \"n_tested\": N_RANDOM,\n                \"violations\": violations,\n                \"nan_curves\": nan_curves,\n                \"direction\": direction,\n                \"worst_violation_magnitude\": float(worst_mag),\n                \"tau_true\": float(tau_true) if not np.isnan(tau_true) else None,\n            }\n            total_tests += N_RANDOM\n            total_violations += violations\n\n    print(f\"\\n  Grand total: {total_tests:,} tests, {total_violations} violations\")\n    return results\n\n\n# ====================================================================\n# Part 2: Adversarial Search\n# ====================================================================\ndef part2_adversarial(all_ss, all_tau_true):\n    print(\"\\n\" + \"=\" * 70)\n    print(f\"PART 2: Adversarial Search ({ADV_N_STARTS} starts x \"\n          f\"{len(ADV_DELTA_PAIRS)} delta-pairs)\")\n    print(\"=\" * 70)\n    sys.stdout.flush()\n\n    results = {}\n\n    for K in K_ADVERSARIAL:\n        print(f\"\\n  K = {K}\")\n        print(f\"  {'Topology':<14} {'Direction':<10} {'best_obj':>12} \"\n              f\"{'Counterex':>11} {'Time':>7}\")\n        print(f\"  {'-' * 57}\")\n        sys.stdout.flush()\n\n        for topo in ALL_TOPOS:\n            t0 = time.time()\n            ss = all_ss[(topo, K)]\n            tau_true = all_tau_true[(topo, K)]\n\n            best_objective = np.inf\n            found_counterexample = False\n            rng_adv = np.random.default_rng(\n                SEED * 3 + K * 10000 + TOPO_IDX[topo] * 100)\n\n            for d1, d2 in ADV_DELTA_PAIRS:\n                for _ in range(ADV_N_STARTS):\n                    theta0 = rng_adv.normal(0, 1, K * K)\n\n                    def objective(theta, _topo=topo, _ss=ss, _tt=tau_true,\n                                  _d1=d1, _d2=d2, _K=K):\n                        logits = theta.reshape(_K, _K)\n                        exp_l = np.exp(logits - logits.max(axis=0, keepdims=True))\n                        C0 = exp_l / exp_l.sum(axis=0, keepdims=True)\n\n                        C1 = (1 - _d1) * np.eye(_K) + _d1 * C0\n                        C2 = (1 - _d2) * np.eye(_K) + _d2 * C0\n\n                        tau1 = get_tau_at_C(_topo, C1, _ss)\n                        tau2 = get_tau_at_C(_topo, C2, _ss)\n\n                        if np.isnan(tau1) or np.isnan(tau2):\n                            return 0.0\n\n                        b1_sq = (tau1 - _tt) ** 2\n                        b2_sq = (tau2 - _tt) ** 2\n\n                        if _topo in NON_DECREASING:\n                            return b2_sq - b1_sq\n                        else:\n                            return b1_sq - b2_sq\n\n                    res = scipy_minimize(objective, theta0, method='L-BFGS-B',\n                                         options={'maxiter': 100, 'ftol': 1e-15})\n\n                    if res.fun < best_objective:\n                        best_objective = res.fun\n\n                    if res.fun < -1e-8:\n                        found_counterexample = True\n\n            elapsed = time.time() - t0\n            direction = \"non-dec\" if topo in NON_DECREASING else \"non-inc\"\n            ce_str = \"YES!\" if found_counterexample else \"no\"\n            print(f\"  {topo:<14} {direction:<10} {best_objective:>12.2e} \"\n                  f\"{ce_str:>11} {elapsed:>6.1f}s\")\n            sys.stdout.flush()\n\n            results[f\"{topo}_K{K}\"] = {\n                \"n_starts\": ADV_N_STARTS * len(ADV_DELTA_PAIRS),\n                \"best_objective\": float(best_objective),\n                \"found_counterexample\": found_counterexample,\n                \"delta_pairs\": [[d1, d2] for d1, d2 in ADV_DELTA_PAIRS],\n            }\n\n    return results\n\n\n# ====================================================================\n# Main\n# ====================================================================\ndef main():\n    t_total = time.time()\n    print(\"Exp-D v2: Conjecture 1 Verification with ANALYTIC plim\")\n    print(f\"  Random: {N_RANDOM:,} C0 x {len(ALL_TOPOS)} topologies x K in {K_VALUES}\")\n    print(f\"  Adversarial: {ADV_N_STARTS} starts x {len(ADV_DELTA_PAIRS)} \"\n          f\"delta-pairs x K in {K_ADVERSARIAL}\")\n    print(f\"  GH quadrature: {N_GH} points/dim, MONO_TOL={MONO_TOL:.0e}\")\n    print(f\"  seed={SEED}\")\n    sys.stdout.flush()\n\n    all_ss, all_tau_true = precompute_all()\n\n    random_results = part1_random(all_ss, all_tau_true)\n    adversarial_results = part2_adversarial(all_ss, all_tau_true)\n\n    # Build output\n    total_random = sum(r['n_tested'] for r in random_results.values())\n    total_viol = sum(r['violations'] for r in random_results.values())\n    total_ce = sum(1 for r in adversarial_results.values()\n                   if r['found_counterexample'])\n\n    if total_viol == 0 and total_ce == 0:\n        summary = (f\"Zero violations across {total_random:,} random tests + \"\n                   f\"0 counterexamples found by adversarial search \"\n                   f\"(analytic plim, MONO_TOL={MONO_TOL:.0e})\")\n    else:\n        summary = (f\"{total_viol} violations across {total_random:,} random tests + \"\n                   f\"{total_ce} counterexamples found by adversarial search \"\n                   f\"(analytic plim, MONO_TOL={MONO_TOL:.0e})\")\n\n    output = {\n        \"method\": \"analytic_plim\",\n        \"gh_quadrature_points\": N_GH,\n        \"mono_tol\": MONO_TOL,\n        \"random_verification\": {},\n        \"adversarial_search\": {},\n        \"summary\": summary,\n    }\n\n    for topo in ALL_TOPOS:\n        rv = {}\n        for K in K_VALUES:\n            key = f\"{topo}_K{K}\"\n            if key in random_results:\n                rv[f\"K{K}\"] = random_results[key]\n        output[\"random_verification\"][topo] = rv\n\n    for topo in ALL_TOPOS:\n        av = {}\n        for K in K_ADVERSARIAL:\n            key = f\"{topo}_K{K}\"\n            if key in adversarial_results:\n                av[f\"K{K}\"] = adversarial_results[key]\n        output[\"adversarial_search\"][topo] = av\n\n    out_path = os.path.join(OUT_DIR, 'exp_d_conjecture_results_v2.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nJSON -> {out_path}\")\n\n    total_time = time.time() - t_total\n    print(f\"\\n{'=' * 70}\")\n    print(f\"SUMMARY: {summary}\")\n    print(f\"Total time: {total_time:.1f}s ({total_time/60:.1f}min)\")\n    print(f\"{'=' * 70}\")\n\n    # Print comparison note\n    print(\"\\nComparison with v1 (Monte Carlo, N=5M, MONO_TOL=1e-8):\")\n    print(\"  v1 found 141,514 violations across 210,000 tests\")\n    print(\"  v1 found 13 adversarial 'counterexamples'\")\n    print(f\"  v2 found {total_viol} violations across {total_random:,} tests\")\n    print(f\"  v2 found {total_ce} adversarial counterexamples\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21f8a234-cf14-436f-8729-2722ea56e5b9",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbPwjwfnEkeUd1jR7xX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fbfee8e-9afa-424a-b0c0-9beb072e3001",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013MmZimNGrNdW9vCf9xnp1C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5254,
      "cache_read_input_tokens": 52446,
      "output_tokens": 17187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5254
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17187,
          "cache_read_input_tokens": 52446,
          "cache_creation_input_tokens": 5254,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5254,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T12:21:56.668Z_

<details><summary>↩ Tool result · `toolu_01JrGKPa9eGe7vT97FKKYzf4`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fbfee8e-9afa-424a-b0c0-9beb072e3001",
  "isSidechain": true,
  "promptId": "3f772f34-432b-4b73-8d6a-c54bf571a4ba",
  "agentId": "a8ae618b752846327",
  "type": "user",
  "uuid": "c949c18d-2e36-4666-a7c9-d788c42b73af",
  "sourceToolAssistantUUID": "0fbfee8e-9afa-424a-b0c0-9beb072e3001",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-22T12:21:59.281Z_

Now let me run it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c949c18d-2e36-4666-a7c9-d788c42b73af",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbgnCvykNySyjHAqTPL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "763ce8db-c62f-4b13-9b28-6f6a4ff6cce8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYPakf6Kyvpu2kGL9NqMmo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17248,
      "cache_read_input_tokens": 57700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17248,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T12:22:00.285Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Hr1Msna3N6NK5JB2vq6tMs`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts && python3 exp_d_conjecture_verify_v2.py 2>&1",
  "description": "Run Exp-D v2 conjecture verification with analytic plim",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "763ce8db-c62f-4b13-9b28-6f6a4ff6cce8",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbgnCvykNySyjHAqTPL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "751f315c-84a4-4cb1-993a-e9cb7ef4bd33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYPakf6Kyvpu2kGL9NqMmo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17248,
      "cache_read_input_tokens": 57700,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17248
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 57700,
          "cache_creation_input_tokens": 17248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17248,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T12:25:24.342Z_

<details><summary>↩ Tool result · `toolu_01Hr1Msna3N6NK5JB2vq6tMs`</summary>

```text
Exp-D v2: Conjecture 1 Verification with ANALYTIC plim
  Random: 10,000 C0 x 7 topologies x K in [3, 5, 7]
  Adversarial: 100 starts x 5 delta-pairs x K in [3, 5]
  GH quadrature: 100 points/dim, MONO_TOL=1e-12
  seed=12345

Precomputing analytic sufficient statistics...
  Done (0.024s). tau_true values:
    confounding    [non-dec] K3=2.0000000000, K5=2.0000000000, K7=2.0000000000
    mediation      [non-dec] K3=0.5000000000, K5=0.5000000000, K7=0.5000000000
    collider       [non-inc] K3=1.0000000000, K5=1.0000000000, K7=1.0000000000
    exposure       [non-dec] K3=1.0000000000, K5=1.0000000000, K7=1.0000000000
    mbias          [non-inc] K3=1.0000000000, K5=1.0000000000, K7=1.0000000000
    iv             [non-dec] K3=1.3331205309, K5=1.9114375709, K7=2.0409089630
    frontdoor      [non-dec] K3=0.5000000000, K5=0.5000000000, K7=0.5000000000

======================================================================
PART 1: Random Verification (10,000 C0 per topology x K)
  MONO_TOL = 1e-12 (analytic -- zero sampling noise)
======================================================================

  K = 3
  Topology       Direction    Tested  Violations  NaN_curves    Worst_mag    Time
  ---------------------------------------------------------------------------
  confounding    non-dec       10000        8467           0     1.09e-02    2.4s
  mediation      non-dec       10000        8236           0     1.27e-02    2.4s
  collider       non-inc       10000        8683           0     4.61e-03    2.4s
  exposure       non-dec       10000         485           0     5.56e-02    1.9s
  mbias          non-inc       10000        9791           0     1.55e-03    2.4s
  iv             non-dec       10000        7433           0     2.47e+06    1.0s
  frontdoor      non-dec       10000        8429           0     1.31e-02    2.5s

  K = 5
  Topology       Direction    Tested  Violations  NaN_curves    Worst_mag    Time
  ---------------------------------------------------------------------------
  confounding    non-dec       10000        8063           0     5.83e-03    3.0s
  mediation      non-dec       10000        7905           0     6.56e-03    3.0s
  collider       non-inc       10000        7669           0     3.43e-03    3.0s
  exposure       non-dec       10000         205           0     5.12e-02    2.5s
  mbias          non-inc       10000        7783           0     1.44e-03    3.0s
  iv             non-dec       10000        6015           0     1.32e+06    1.3s
  frontdoor      non-dec       10000        8079           0     6.29e-03    4.1s

  K = 7
  Topology       Direction    Tested  Violations  NaN_curves    Worst_mag    Time
  ---------------------------------------------------------------------------
  confounding    non-dec       10000        7892           0     3.41e-03    3.7s
  mediation      non-dec       10000        7893           0     4.03e-03    3.8s
  collider       non-inc       10000        7570           0     2.49e-03    3.7s
  exposure       non-dec       10000          77           0     2.19e-02    3.2s
  mbias          non-inc       10000        7399           0     8.78e-04    3.7s
  iv             non-dec       10000        5711           0     5.48e+06    1.3s
  frontdoor      non-dec       10000        7899           0     3.64e-03    3.7s

  Grand total: 210,000 tests, 141684 violations

======================================================================
PART 2: Adversarial Search (100 starts x 5 delta-pairs)
======================================================================

  K = 3
  Topology       Direction      best_obj   Counterex    Time
  ---------------------------------------------------------
  confounding    non-dec       -9.78e-03        YES!    5.6s
  mediation      non-dec       -1.05e-02        YES!    5.9s
  collider       non-inc       -3.06e-04        YES!    4.4s
  exposure       non-dec       -3.86e-03        YES!   10.8s
  mbias          non-inc       -1.71e-03        YES!    3.7s
  iv             non-dec        9.66e-30          no    8.0s
  frontdoor      non-dec       -6.06e-03        YES!    6.0s

  K = 5
  Topology       Direction      best_obj   Counterex    Time
  ---------------------------------------------------------
  confounding    non-dec       -1.48e-02        YES!   14.0s
  mediation      non-dec       -1.09e-02        YES!   14.1s
  collider       non-inc       -1.14e-03        YES!   12.5s
  exposure       non-dec       -5.39e-03        YES!   25.8s
  mbias          non-inc       -1.88e-03        YES!   11.3s
  iv             non-dec       -2.66e+01        YES!    9.0s
  frontdoor      non-dec       -1.23e-02        YES!   14.2s

JSON -> /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_results_v2.json

======================================================================
SUMMARY: 141684 violations across 210,000 random tests + 13 counterexamples found by adversarial search (analytic plim, MONO_TOL=1e-12)
Total time: 203.3s (3.4min)
======================================================================

Comparison with v1 (Monte Carlo, N=5M, MONO_TOL=1e-8):
  v1 found 141,514 violations across 210,000 tests
  v1 found 13 adversarial 'counterexamples'
  v2 found 141684 violations across 210,000 tests
  v2 found 13 adversarial counterexamples
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "751f315c-84a4-4cb1-993a-e9cb7ef4bd33",
  "isSidechain": true,
  "promptId": "3f772f34-432b-4b73-8d6a-c54bf571a4ba",
  "agentId": "a8ae618b752846327",
  "type": "user",
  "uuid": "8cb091ac-bd24-4904-95f7-b0dbd4803513",
  "sourceToolAssistantUUID": "751f315c-84a4-4cb1-993a-e9cb7ef4bd33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-22T12:25:28.280Z_

This is a very significant result. The violations are NOT numerical artifacts -- they persist even with analytic plim and an even tighter tolerance (1e-12 vs 1e-8). The violation counts are essentially identical to the Monte Carlo version, and the worst violation magnitudes are comparable. Let me read the output JSON to get the full details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cb091ac-bd24-4904-95f7-b0dbd4803513",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbx67czBu5GeziWeRp2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78d35dad-486b-4ed6-af70-8e5fc67d7a99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEDYPaRvSN9fAQGDXnrpzG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 74948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1956,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T12:25:28.494Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HCwA1fLDgvEYdZ8xzzaKGm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_results_v2.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78d35dad-486b-4ed6-af70-8e5fc67d7a99",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbx67czBu5GeziWeRp2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75c4fddd-db59-4f45-8b3e-50546897bcc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEDYPaRvSN9fAQGDXnrpzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1956,
      "cache_read_input_tokens": 74948,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 74948,
          "cache_creation_input_tokens": 1956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1956,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T12:25:28.503Z_

<details><summary>↩ Tool result · `toolu_01HCwA1fLDgvEYdZ8xzzaKGm`</summary>

```text
1	{
2	  "method": "analytic_plim",
3	  "gh_quadrature_points": 100,
4	  "mono_tol": 1e-12,
5	  "random_verification": {
6	    "confounding": {
7	      "K3": {
8	        "n_tested": 10000,
9	        "violations": 8467,
10	        "nan_curves": 0,
11	        "direction": "non-dec",
12	        "worst_violation_magnitude": 0.01086810865728216,
13	        "tau_true": 2.0
14	      },
15	      "K5": {
16	        "n_tested": 10000,
17	        "violations": 8063,
18	        "nan_curves": 0,
19	        "direction": "non-dec",
20	        "worst_violation_magnitude": 0.005825013346442809,
21	        "tau_true": 1.9999999999999998
22	      },
23	      "K7": {
24	        "n_tested": 10000,
25	        "violations": 7892,
26	        "nan_curves": 0,
27	        "direction": "non-dec",
28	        "worst_violation_magnitude": 0.0034082229756147164,
29	        "tau_true": 2.0
30	      }
31	    },
32	    "mediation": {
33	      "K3": {
34	        "n_tested": 10000,
35	        "violations": 8236,
36	        "nan_curves": 0,
37	        "direction": "non-dec",
38	        "worst_violation_magnitude": 0.012726505679608646,
39	        "tau_true": 0.5
40	      },
41	      "K5": {
42	        "n_tested": 10000,
43	        "violations": 7905,
44	        "nan_curves": 0,
45	        "direction": "non-dec",
46	        "worst_violation_magnitude": 0.0065598588622944876,
47	        "tau_true": 0.49999999999999983
48	      },
49	      "K7": {
50	        "n_tested": 10000,
51	        "violations": 7893,
52	        "nan_curves": 0,
53	        "direction": "non-dec",
54	        "worst_violation_magnitude": 0.0040332631090529425,
55	        "tau_true": 0.4999999999999996
56	      }
57	    },
58	    "collider": {
59	      "K3": {
60	        "n_tested": 10000,
61	        "violations": 8683,
62	        "nan_curves": 0,
63	        "direction": "non-inc",
64	        "worst_violation_magnitude": 0.004606180170102059,
65	        "tau_true": 1.0
66	      },
67	      "K5": {
68	        "n_tested": 10000,
69	        "violations": 7669,
70	        "nan_curves": 0,
71	        "direction": "non-inc",
72	        "worst_violation_magnitude": 0.0034316669468731353,
73	        "tau_true": 1.0
74	      },
75	      "K7": {
76	        "n_tested": 10000,
77	        "violations": 7570,
78	        "nan_curves": 0,
79	        "direction": "non-inc",
80	        "worst_violation_magnitude": 0.002491098787699819,
81	        "tau_true": 1.0
82	      }
83	    },
84	    "exposure": {
85	      "K3": {
86	        "n_tested": 10000,
87	        "violations": 485,
88	        "nan_curves": 0,
89	        "direction": "non-dec",
90	        "worst_violation_magnitude": 0.055567041313488996,
91	        "tau_true": 1.0000000000000002
92	      },
93	      "K5": {
94	        "n_tested": 10000,
95	        "violations": 205,
96	        "nan_curves": 0,
97	        "direction": "non-dec",
98	        "worst_violation_magnitude": 0.05121055325737478,
99	        "tau_true": 1.0000000000000002
100	      },
101	      "K7": {
102	        "n_tested": 10000,
103	        "violations": 77,
104	        "nan_curves": 0,
105	        "direction": "non-dec",
106	        "worst_violation_magnitude": 0.021928244727854262,
107	        "tau_true": 0.9999999999999998
108	      }
109	    },
110	    "mbias": {
111	      "K3": {
112	        "n_tested": 10000,
113	        "violations": 9791,
114	        "nan_curves": 0,
115	        "direction": "non-inc",
116	        "worst_violation_magnitude": 0.0015474283680341205,
117	        "tau_true": 1.0
118	      },
119	      "K5": {
120	        "n_tested": 10000,
121	        "violations": 7783,
122	        "nan_curves": 0,
123	        "direction": "non-inc",
124	        "worst_violation_magnitude": 0.0014386231201501953,
125	        "tau_true": 1.0
126	      },
127	      "K7": {
128	        "n_tested": 10000,
129	        "violations": 7399,
130	        "nan_curves": 0,
131	        "direction": "non-inc",
132	        "worst_violation_magnitude": 0.0008775222889561007,
133	        "tau_true": 1.0
134	      }
135	    },
136	    "iv": {
137	      "K3": {
138	        "n_tested": 10000,
139	        "violations": 7433,
140	        "nan_curves": 0,
141	        "direction": "non-dec",
142	        "worst_violation_magnitude": 2466085.7260094993,
143	        "tau_true": 1.333120530897266
144	      },
145	      "K5": {
146	        "n_tested": 10000,
147	        "violations": 6015,
148	        "nan_curves": 0,
149	        "direction": "non-dec",
150	        "worst_violation_magnitude": 1315009.2588172748,
151	        "tau_true": 1.9114375708768654
152	      },
153	      "K7": {
154	        "n_tested": 10000,
155	        "violations": 5711,
156	        "nan_curves": 0,
157	        "direction": "non-dec",
158	        "worst_violation_magnitude": 5481030.861738394,
159	        "tau_true": 2.0409089629546364
160	      }
161	    },
162	    "frontdoor": {
163	      "K3": {
164	        "n_tested": 10000,
165	        "violations": 8429,
166	        "nan_curves": 0,
167	        "direction": "non-dec",
168	        "worst_violation_magnitude": 0.01307166903449175,
169	        "tau_true": 0.5
170	      },
171	      "K5": {
172	        "n_tested": 10000,
173	        "violations": 8079,
174	        "nan_curves": 0,
175	        "direction": "non-dec",
176	        "worst_violation_magnitude": 0.006291871500388346,
177	        "tau_true": 0.49999999999999994
178	      },
179	      "K7": {
180	        "n_tested": 10000,
181	        "violations": 7899,
182	        "nan_curves": 0,
183	        "direction": "non-dec",
184	        "worst_violation_magnitude": 0.003641870803524405,
185	        "tau_true": 0.5
186	      }
187	    }
188	  },
189	  "adversarial_search": {
190	    "confounding": {
191	      "K3": {
192	        "n_starts": 500,
193	        "best_objective": -0.009781039201619227,
194	        "found_counterexample": true,
195	        "delta_pairs": [
196	          [
197	            0.0,
198	            0.2
199	          ],
200	          [
201	            0.0,
202	            0.5
203	          ],
204	          [
205	            0.1,
206	            0.3
207	          ],
208	          [
209	            0.2,
210	            0.5
211	          ],
212	          [
213	            0.3,
214	            0.7
215	          ]
216	        ]
217	      },
218	      "K5": {
219	        "n_starts": 500,
220	        "best_objective": -0.014755856830761034,
221	        "found_counterexample": true,
222	        "delta_pairs": [
223	          [
224	            0.0,
225	            0.2
226	          ],
227	          [
228	            0.0,
229	            0.5
230	          ],
231	          [
232	            0.1,
233	            0.3
234	          ],
235	          [
236	            0.2,
237	            0.5
238	          ],
239	          [
240	            0.3,
241	            0.7
242	          ]
243	        ]
244	      }
245	    },
246	    "mediation": {
247	      "K3": {
248	        "n_starts": 500,
249	        "best_objective": -0.010534893741626042,
250	        "found_counterexample": true,
251	        "delta_pairs": [
252	          [
253	            0.0,
254	            0.2
255	          ],
256	          [
257	            0.0,
258	            0.5
259	          ],
260	          [
261	            0.1,
262	            0.3
263	          ],
264	          [
265	            0.2,
266	            0.5
267	          ],
268	          [
269	            0.3,
270	            0.7
271	          ]
272	        ]
273	      },
274	      "K5": {
275	        "n_starts": 500,
276	        "best_objective": -0.010875476213587556,
277	        "found_counterexample": true,
278	        "delta_pairs": [
279	          [
280	            0.0,
281	            0.2
282	          ],
283	          [
284	            0.0,
285	            0.5
286	          ],
287	          [
288	            0.1,
289	            0.3
290	          ],
291	          [
292	            0.2,
293	            0.5
294	          ],
295	          [
296	            0.3,
297	            0.7
298	          ]
299	        ]
300	      }
301	    },
302	    "collider": {
303	      "K3": {
304	        "n_starts": 500,
305	        "best_objective": -0.00030552585951969333,
306	        "found_counterexample": true,
307	        "delta_pairs": [
308	          [
309	            0.0,
310	            0.2
311	          ],
312	          [
313	            0.0,
314	            0.5
315	          ],
316	          [
317	            0.1,
318	            0.3
319	          ],
320	          [
321	            0.2,
322	            0.5
323	          ],
324	          [
325	            0.3,
326	            0.7
327	          ]
328	        ]
329	      },
330	      "K5": {
331	        "n_starts": 500,
332	        "best_objective": -0.0011443531536633003,
333	        "found_counterexample": true,
334	        "delta_pairs": [
335	          [
336	            0.0,
337	            0.2
338	          ],
339	          [
340	            0.0,
341	            0.5
342	          ],
343	          [
344	            0.1,
345	            0.3
346	          ],
347	          [
348	            0.2,
349	            0.5
350	          ],
351	          [
352	            0.3,
353	            0.7
354	          ]
355	        ]
356	      }
357	    },
358	    "exposure": {
359	      "K3": {
360	        "n_starts": 500,
361	        "best_objective": -0.003864347544026268,
362	        "found_counterexample": true,
363	        "delta_pairs": [
364	          [
365	            0.0,
366	            0.2
367	          ],
368	          [
369	            0.0,
370	            0.5
371	          ],
372	          [
373	            0.1,
374	            0.3
375	          ],
376	          [
377	            0.2,
378	            0.5
379	          ],
380	          [
381	            0.3,
382	            0.7
383	          ]
384	        ]
385	      },
386	      "K5": {
387	        "n_starts": 500,
388	        "best_objective": -0.005393984754724663,
389	        "found_counterexample": true,
390	        "delta_pairs": [
391	          [
392	            0.0,
393	            0.2
394	          ],
395	          [
396	            0.0,
397	            0.5
398	          ],
399	          [
400	            0.1,
401	            0.3
402	          ],
403	          [
404	            0.2,
405	            0.5
406	          ],
407	          [
408	            0.3,
409	            0.7
410	          ]
411	        ]
412	      }
413	    },
414	    "mbias": {
415	      "K3": {
416	        "n_starts": 500,
417	        "best_objective": -0.0017080912306270523,
418	        "found_counterexample": true,
419	        "delta_pairs": [
420	          [
421	            0.0,
422	            0.2
423	          ],
424	          [
425	            0.0,
426	            0.5
427	          ],
428	          [
429	            0.1,
430	            0.3
431	          ],
432	          [
433	            0.2,
434	            0.5
435	          ],
436	          [
437	            0.3,
438	            0.7
439	          ]
440	        ]
441	      },
442	      "K5": {
443	        "n_starts": 500,
444	        "best_objective": -0.0018772543101670865,
445	        "found_counterexample": true,
446	        "delta_pairs": [
447	          [
448	            0.0,
449	            0.2
450	          ],
451	          [
452	            0.0,
453	            0.5
454	          ],
455	          [
456	            0.1,
457	            0.3
458	          ],
459	          [
460	            0.2,
461	            0.5
462	          ],
463	          [
464	            0.3,
465	            0.7
466	          ]
467	        ]
468	      }
469	    },
470	    "iv": {
471	      "K3": {
472	        "n_starts": 500,
473	        "best_objective": 9.663546088957395e-30,
474	        "found_counterexample": false,
475	        "delta_pairs": [
476	          [
477	            0.0,
478	            0.2
479	          ],
480	          [
481	            0.0,
482	            0.5
483	          ],
484	          [
485	            0.1,
486	            0.3
487	          ],
488	          [
489	            0.2,
490	            0.5
491	          ],
492	          [
493	            0.3,
494	            0.7
495	          ]
496	        ]
497	      },
498	      "K5": {
499	        "n_starts": 500,
500	        "best_objective": -26.64443041894075,
501	        "found_counterexample": true,
502	        "delta_pairs": [
503	          [
504	            0.0,
505	            0.2
506	          ],
507	          [
508	            0.0,
509	            0.5
510	          ],
511	          [
512	            0.1,
513	            0.3
514	          ],
515	          [
516	            0.2,
517	            0.5
518	          ],
519	          [
520	            0.3,
521	            0.7
522	          ]
523	        ]
524	      }
525	    },
526	    "frontdoor": {
527	      "K3": {
528	        "n_starts": 500,
529	        "best_objective": -0.006059828484311289,
530	        "found_counterexample": true,
531	        "delta_pairs": [
532	          [
533	            0.0,
534	            0.2
535	          ],
536	          [
537	            0.0,
538	            0.5
539	          ],
540	          [
541	            0.1,
542	            0.3
543	          ],
544	          [
545	            0.2,
546	            0.5
547	          ],
548	          [
549	            0.3,
550	            0.7
551	          ]
552	        ]
553	      },
554	      "K5": {
555	        "n_starts": 500,
556	        "best_objective": -0.012316386926386522,
557	        "found_counterexample": true,
558	        "delta_pairs": [
559	          [
560	            0.0,
561	            0.2
562	          ],
563	          [
564	            0.0,
565	            0.5
566	          ],
567	          [
568	            0.1,
569	            0.3
570	          ],
571	          [
572	            0.2,
573	            0.5
574	          ],
575	          [
576	            0.3,
577	            0.7
578	          ]
579	        ]
580	      }
581	    }
582	  },
583	  "summary": "141684 violations across 210,000 random tests + 13 counterexamples found by adversarial search (analytic plim, MONO_TOL=1e-12)"
584	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75c4fddd-db59-4f45-8b3e-50546897bcc9",
  "isSidechain": true,
  "promptId": "3f772f34-432b-4b73-8d6a-c54bf571a4ba",
  "agentId": "a8ae618b752846327",
  "type": "user",
  "uuid": "93468461-4fe5-4620-91da-cc4abe7dd75e",
  "sourceToolAssistantUUID": "75c4fddd-db59-4f45-8b3e-50546897bcc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-22T12:25:48.564Z_

The results are definitive. Here is the complete report:

## Results

The v2 script with analytic plim is at `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py`, with output at `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_results_v2.json`.

### Key finding: The violations are REAL, not numerical artifacts.

With analytic plim (zero sampling noise) and MONO_TOL tightened from 1e-8 to 1e-12:

- **v1 (Monte Carlo)**: 141,514 violations / 210,000 tests, 13 adversarial counterexamples
- **v2 (Analytic)**: 141,684 violations / 210,000 tests, 13 adversarial counterexamples

The violation counts match almost exactly (differences of ~170 out of 210k are due to the v1 Monte Carlo tau_true being slightly off, which shifts borderline cases). The worst violation magnitudes are also nearly identical.

### Per-topology comparison (violations across K=3,5,7):

| Topology | Direction | v1 violations | v2 violations | Worst mag (v2) |
|---|---|---|---|---|
| confounding | non-dec | 24,421 | 24,422 | 0.0109 |
| mediation | non-dec | 24,029 | 24,034 | 0.0127 |
| collider | non-inc | 23,851 | 23,922 | 0.0046 |
| exposure | non-dec | 771 | 767 | 0.0556 |
| mbias | non-inc | 24,887 | 24,973 | 0.0015 |
| iv | non-dec | 19,150 | 19,159 | 5.5M |
| frontdoor | non-dec | 24,405 | 24,407 | 0.0131 |

### Analytic tau_true values (now exact):
- confounding: tau_true = 2.0 exactly (v1 had ~2.0003 from sampling)
- mediation: tau_true = 0.5 exactly
- collider/mbias: tau_true = 1.0 exactly (DGP parameter)
- exposure: tau_true = 1.0 exactly
- frontdoor: tau_true = 0.5 exactly
- iv: tau_true = 1.333..., 1.911..., 2.041... (GH quadrature, machine precision)

### Conclusion

**Conjecture 1 (strict monotonicity of |B(delta)|) is FALSE for all 7 topologies.** The violations are genuine mathematical properties of the bias function, not sampling noise. The bias envelope |B(delta)| exhibits real non-monotonic behavior under general confusion matrices C0, with violation magnitudes up to ~0.056 for non-IV topologies and ~5.5M for IV (due to weak-instrument singularities). The adversarial search confirms counterexamples exist for all topologies except IV at K=3 (where the Wald ratio structure constrains the bias more tightly).

The script completed in 3.4 minutes (vs the original's much longer runtime due to N=5M simulation), producing identical scientific conclusions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93468461-4fe5-4620-91da-cc4abe7dd75e",
  "isSidechain": true,
  "agentId": "a8ae618b752846327",
  "requestId": "req_011CbHbxQHGbXQzBHxiLkYiL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1264e57b-924a-4826-8e4d-09482cb44ff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Bk2tTCobX1tmquuAAePd4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5357,
      "cache_read_input_tokens": 76904,
      "output_tokens": 857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5357
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 857,
          "cache_read_input_tokens": 76904,
          "cache_creation_input_tokens": 5357,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5357,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
