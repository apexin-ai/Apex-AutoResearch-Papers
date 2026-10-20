# Subsample Curriculum Patch
# -------------------------
# Problem: subsample_variable_dt applies variable-dt subsampling in Phase 1
# (gate frozen, 0-50K steps), forcing RSSM to train on variable-dt data while
# imagination only uses dt=1. This train/imagine mismatch hurts return (~40% of baseline).
#
# Fix: tie subsampling range to gate_scale curriculum.
#   Phase 1 (gate_scale=0):    effective_max_dt=1 -> no subsampling (vanilla DreamerV3)
#   Phase 2 (0<gate_scale<1):  effective_max_dt linearly ramps from 1 to K
#   Phase 3 (gate_scale=1):    effective_max_dt=K -> full log-uniform subsampling
#
# Deployment:
#   1. Replace subsample_variable_dt in tools.py (around line 763)
#   2. Replace the subsample call block in WorldModel._train in models.py (around line 169)

import math
import torch


# =============================================================================
# Part 1: Replace tools.subsample_variable_dt (tools.py ~line 763-810)
# =============================================================================

def subsample_variable_dt(data, max_dt, discount, effective_max_dt=None):
    """Variable-dt sub-sampling of replay trajectories.

    Samples per-element dt from log-uniform over [1, effective_max_dt].
    Computes cumulative discounted reward and minimum continuation for each gap.

    Args:
        data: dict of tensors, each (B, T, ...).
        max_dt: config maximum dt (used as upper bound clamp).
        discount: scalar discount factor for cumulative reward.
        effective_max_dt: curriculum-controlled max dt.
            None or <=1 means no subsampling (pure dt=1, vanilla DreamerV3).
    """
    B, T = data["action"].shape[:2]
    device = data["action"].device

    if effective_max_dt is None:
        effective_max_dt = max_dt

    effective_max_dt = max(1, min(int(round(effective_max_dt)), max_dt))

    if effective_max_dt <= 1:
        dt_labels = torch.ones(B, T, dtype=torch.long, device=device)
        return data, dt_labels

    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(effective_max_dt))
    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, effective_max_dt)

    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()
    T_sub = sub_len.max().item()

    data_sub = {}
    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)
    reward_cum = torch.zeros(B, T_sub, *data["reward"].shape[2:], device=device)
    cont_min = torch.ones(B, T_sub, *data["cont"].shape[2:], device=device)

    for b in range(B):
        dt_b = dt_per_elem[b].item()
        indices = list(range(0, T, dt_b))
        L = len(indices)

        for key in data:
            if key not in data_sub:
                data_sub[key] = torch.zeros(
                    B, T_sub, *data[key].shape[2:],
                    dtype=data[key].dtype, device=device,
                )
            data_sub[key][b, :L] = data[key][b, indices]

        for i, t_start in enumerate(indices[:-1]):
            t_end = min(t_start + dt_b, T)
            span = t_end - t_start
            gamma_powers = discount ** torch.arange(
                span, dtype=torch.float, device=device
            )
            r_slice = data["reward"][b, t_start:t_end]
            reward_cum[b, i] = (gamma_powers * r_slice).sum(dim=0)
            cont_min[b, i] = data["cont"][b, t_start:t_end].min(dim=0).values

        dt_labels[b, :L] = dt_b

    data_sub["reward"] = reward_cum
    data_sub["cont"] = cont_min
    return data_sub, dt_labels


# =============================================================================
# Part 2: Replace subsample call in WorldModel._train (models.py ~line 169-173)
# =============================================================================
# Original code:
#
#     if self._config.gate_enabled:
#         self.gate_step += 1
#         data, dt_labels = tools.subsample_variable_dt(
#             data, self._config.gate_max_dt, self._config.discount,
#         )
#     else:
#         dt_labels = None
#
# Replace with:
#
#     if self._config.gate_enabled:
#         self.gate_step += 1
#         step = self.gate_step.item()
#         if step < self._config.gate_curriculum_phase1:
#             gate_scale = 0.0
#         elif step < self._config.gate_curriculum_phase2:
#             progress = (step - self._config.gate_curriculum_phase1) / (
#                 self._config.gate_curriculum_phase2
#                 - self._config.gate_curriculum_phase1
#             )
#             gate_scale = progress
#         else:
#             gate_scale = 1.0
#
#         effective_max_dt = 1 + gate_scale * (self._config.gate_max_dt - 1)
#         data, dt_labels = tools.subsample_variable_dt(
#             data, self._config.gate_max_dt, self._config.discount,
#             effective_max_dt=effective_max_dt,
#         )
#     else:
#         dt_labels = None
#
# NOTE: The gate_scale computation later in _train (around line 242) already
# duplicates the same curriculum logic for scaling the gate loss. After this
# patch, both blocks use the same gate_scale value. You can optionally refactor
# to compute gate_scale once and reuse it, but it is not required — the
# duplicated computation is trivially cheap and keeps the patch minimal.
