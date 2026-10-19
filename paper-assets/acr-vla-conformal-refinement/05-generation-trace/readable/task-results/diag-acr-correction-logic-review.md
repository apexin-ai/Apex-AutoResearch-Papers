# diag acr correction logic review

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_acr-correction-logic-review_20260514T072631_result.json`
- **Structured JSON:** [`cc918dd17b949004f8d0.json`](../../sessions/cc/cc918dd17b949004f8d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture. Here's the audit report.

---

# ACR-VLA CRM Bug Audit Report

## CRITICAL

### C1: Train/eval state dimension mismatch (6D vs 8D)

**Files:** `smolvla_wrapper.py:180` vs `smolvla_wrapper.py:142-145`

During CRM training precompute, `preprocess_obs_batch` feeds SmolVLA the robot state from `s["ee_states"]` — **6D** (eef_pos + axisangle, no gripper):

```python
# smolvla_wrapper.py:180 (precompute path)
es = torch.tensor(s["ee_states"], ...)  # 6D
es = self._normalize_state(es)
state[i, :es.shape[0]] = es  # state[0:6] filled, state[6:31] = 0
```

During evaluation, `preprocess_obs` feeds SmolVLA the full **8D** state (eef_pos + axisangle + gripper_qpos):

```python
# smolvla_wrapper.py:142 (eval path), via get_robot_state (evaluate.py:80)
state_t = torch.tensor(robot_state, ...)  # 8D
state_t = self._normalize_state(state_t)
state[0, :state_t.shape[0]] = state_t  # state[0:8] filled
```

Root cause: `build_training_samples` (utils.py:75) stores `ee_states` (6D) but `get_robot_state` (evaluate.py:80) computes 8D by including `gripper_qpos`.

**Impact:** SmolVLA was trained with 8D state input. During CRM precompute, positions 6-7 (gripper_qpos) are zeroed → SmolVLA produces differently-conditioned `obs_feat` (960D) and K samples. The CRM trains on this corrupted distribution, then at eval receives correctly-conditioned inputs it has never seen. This is a systematic train/eval distribution shift on **both** of CRM's primary inputs.

---

## WARNING

### W1: ACI module dead code — conformal alpha never adapts online

**File:** `evaluate.py:287,303`

```python
aci = AdaptiveConformalInference()  # line ~287
...
aci.reset()  # line ~303, per task
```

`aci` is instantiated and reset per task but never passed to any action selection function. CGS always uses the static default `alpha=0.1`. The online alpha adaptation described in `aci.py` (Gibbs & Candès 2021 update rule, COC signal) is completely disconnected from the pipeline.

### W2: CRM uses sample mean as base action — bad for multimodal distributions

**File:** `evaluate.py:174`, `cgs.py:38`

ACR-VLA computes `ma = K_samples.mean(dim=0)` and CRM output = `ma + delta`. For multimodal action distributions (common in spatial manipulation — e.g., reach around left vs right), the mean falls in an invalid no-man's-land between modes. ReconVLA avoids this by selecting a concrete sample via argmin, which is always a valid action.

This is likely a key contributor to the 42.9% (reconvla) vs 23.3% (acr_vla) gap.

### W3: Conformal radius always equals max distance (K=10, alpha=0.1)

**File:** `cgs.py:61-64`

```python
q_idx = int(np.ceil((1 - 0.1) * (10 + 1))) - 1  # = ceil(9.9) - 1 = 9
q_idx = min(9, 9)  # 9 → last element = maximum
```

With K=10 and alpha=0.1, the conformal quantile index is always 9 (the max). All 5 `conformal_radius` features in the 40D CGS are just `max(Mahalanobis_distances)` — a single noisy outlier statistic with near-zero discriminative power.

### W4: No correction magnitude constraint

**File:** `crm.py:44`

```python
delta = self.net(x)
return mean_action + delta  # no clamping/scaling
```

CRM can output arbitrarily large corrections at eval. A well-performing base prediction can be catastrophically corrupted. No tanh squashing, learned temperature, or norm constraint is applied.

---

## OK (verified correct)

| # | Check | Verdict |
|---|-------|---------|
| O1 | CRM output is absolute (mean+delta), consistent in train & eval | ✓ |
| O2 | Gripper excluded from CRM, mean-aggregated separately (`evaluate.py:183-185`) | ✓ |
| O3 | 30D = 5×6 dimension mapping, consistent H_EFF/CORRECTION_DIM | ✓ |
| O4 | Both train & eval operate in unnormalized action space, no double denorm | ✓ |
| O5 | CGS math correct (Ledoit-Wolf cov, regularized inverse, Mahalanobis) | ✓ |
| O6 | CRM input concat order `[ma(30), uf(40), obs(960)]` same in train & eval | ✓ |
| O7 | chunk_size=50 → H_EFF=5 truncation consistent | ✓ |
| O8 | Expert actions in same space (raw LIBERO) as unnormalized SmolVLA output | ✓ |

---

## Summary

The most actionable bug is **C1** — the 6D/8D state mismatch in training precompute. Fix: change `build_training_samples` to include `gripper_qpos` in the cached state, or augment `ee_states` to 8D in `preprocess_obs_batch`. This requires re-running precompute + retraining CRM.

Beyond the code bug, two design issues (W2: mean as base action, W3: degenerate conformal quantile) structurally limit ACR-VLA's ability to outperform the simpler reconvla baseline. Consider switching to a "select then refine" approach: use reconvla-style argmin to pick the best sample, then apply CRM correction to that concrete sample instead of the mean.

---
