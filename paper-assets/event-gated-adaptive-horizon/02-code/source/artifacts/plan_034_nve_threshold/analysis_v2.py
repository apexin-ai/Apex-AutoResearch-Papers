#!/usr/bin/env python3
"""NVE Threshold Sensitivity Analysis V2 — with combined diagnostic criteria and dual methods."""

import json
import math
from collections import OrderedDict

# ============================================================
# Walker baseline VE ratio per step (from exp_001_baseline s1)
# ============================================================
WALKER_BASELINE_VE = {
    15: 0.02, 25: 0.087, 35: 0.241, 45: 0.331, 55: 0.404,
    65: 0.563, 75: 0.719, 85: 0.701, 95: 0.632, 105: 0.656,
}
CHEETAH_BASELINE_VE = {
    15: 0.02, 25: 0.1, 35: 0.2, 45: 0.3, 55: 0.4,
    65: 0.5, 75: 0.55, 85: 0.6, 95: 0.65, 105: 0.65,
}

WALKER_BASELINE_EVAL = 915.67
CHEETAH_BASELINE_EVAL = 446.1

# ============================================================
# Dataset: 61 experiments from V1 with ground truth labels
# ============================================================
# Format: (exp_id, env, config, ground_truth_civo, nve_peak_methodA,
#          ve_ratio_peak_methodB, nve_trajectory_dict, eval_trajectory_dict)
# nve_trajectory: {step_K: nve_value} or None
# ve_ratio_trajectory: {step_K: raw_ve_ratio} or None

experiments = [
    # --- CIVO positive (25) ---
    {"id": "exp_006_fixed_dt2", "env": "walker", "gt": 1, "nve_peak": 4.835,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008d_civo_trigger_s3", "env": "walker", "gt": 1, "nve_peak": 1.530,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008d_civo_trigger_s4", "env": "walker", "gt": 1, "nve_peak": 4.620,
     "ve_ratio_peak": 3.0294, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008d_subsample_on_h8", "env": "walker", "gt": 1, "nve_peak": 4.124,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008e_v3_s3", "env": "walker", "gt": 1, "nve_peak": 4.020,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008e_v3_walker_s2", "env": "walker", "gt": 1, "nve_peak": 3.780,
     "ve_ratio_peak": 2.481,
     "nve_traj": {25: 1.64, 35: 1.03, 45: 1.06, 55: 1.02, 65: 0.90, 75: 0.66, 85: 0.68, 95: 1.34, 105: 3.78},
     "ve_traj": {25: 0.143, 35: 0.249, 45: 0.351, 55: 0.413, 65: 0.507, 75: 0.473, 85: 0.474, 95: 0.85, 105: 2.481},
     "eval_traj": None},
    {"id": "exp_009b_008d_walker_s2", "env": "walker", "gt": 1, "nve_peak": 1.620,
     "ve_ratio_peak": 0.5703, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_009e_008d_walker_s1", "env": "walker", "gt": 1, "nve_peak": 4.130,
     "ve_ratio_peak": 1.6663, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_010b_cheetah_civo_trigger", "env": "cheetah", "gt": 1, "nve_peak": 8.270,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_010b_cheetah_civo_trigger_s0", "env": "cheetah", "gt": 1, "nve_peak": 70.640,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_021_full_sgs_cheetah_s1", "env": "cheetah", "gt": 1, "nve_peak": 9.940,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_027_tcn_walker_s0", "env": "walker", "gt": 1, "nve_peak": 3.965,
     "ve_ratio_peak": 3.965,
     "nve_traj": None,
     "ve_traj": {15: 0.02, 25: 0.11, 35: 0.235, 45: 0.86, 55: 1.679, 65: 1.544, 75: 0.831, 85: 3.965, 95: 0.675, 105: 0.916},
     "eval_traj": None},
    {"id": "exp_027_tcn_walker_s1", "env": "walker", "gt": 1, "nve_peak": 1.637,
     "ve_ratio_peak": 1.6367,
     "nve_traj": None,
     "ve_traj": {15: 0.0246, 25: 0.1416, 35: 0.3585, 45: 0.6101, 55: 0.7092, 65: 0.4875, 75: 0.4902, 85: 1.4104, 95: 1.6367, 105: 0.6444},
     "eval_traj": None},
    {"id": "exp_029b_tcn_walker_s2_sigma02", "env": "walker", "gt": 1, "nve_peak": 2.765,
     "ve_ratio_peak": 2.765,
     "nve_traj": None,
     "ve_traj": {15: 0.03, 25: 0.174, 35: 0.335, 45: 0.477, 55: 0.583, 65: 1.014, 75: 1.65, 85: 1.623, 95: 2.109, 105: 2.765},
     "eval_traj": None},
    {"id": "exp_029d_tcn_walker_s3_sigma02", "env": "walker", "gt": 1, "nve_peak": 3.000,
     "ve_ratio_peak": 3.0,
     "nve_traj": None,
     "ve_traj": {45: 0.695, 55: 0.598, 65: 0.863, 75: 0.791, 85: 0.9, 95: 0.7, 105: 3.0},
     "eval_traj": None},
    {"id": "exp_030b_tcn_cheetah_s0_sigma05", "env": "cheetah", "gt": 1, "nve_peak": 10.666,
     "ve_ratio_peak": 10.6657,
     "nve_traj": None,
     "ve_traj": {15: 0.0202, 25: 0.0636, 35: 0.1238, 45: 1.9141, 55: 10.6657, 65: 0.8371, 75: 1.9823, 85: 1.0946, 95: 0.2253, 105: 0.2686},
     "eval_traj": None},
    {"id": "exp_031b_tcn_pickcube_s0_sigma05", "env": "pickcube", "gt": 1, "nve_peak": 3.300,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_034_dual_critic_cheetah", "env": "cheetah", "gt": 1, "nve_peak": 4.500,
     "ve_ratio_peak": 1.8, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_036_dual_critic_pickcube", "env": "pickcube", "gt": 1, "nve_peak": 2.300,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_037_wide_critic_cheetah", "env": "cheetah", "gt": 1, "nve_peak": 3.600,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_045_treatment_extension_008d_s3", "env": "walker", "gt": 1, "nve_peak": 4.910,
     "ve_ratio_peak": 4.91,
     "nve_traj": None,
     "ve_traj": {122: 4.77, 132: 4.91, 142: 0.43, 152: 0.21, 162: 0.25, 172: 0.18, 182: 0.16, 192: 0.13, 202: 0.12, 212: 0.1, 222: 0.1, 232: 0.09, 242: 0.07, 252: 0.08, 262: 0.07, 272: 0.08, 282: 0.07, 292: 0.06, 302: 0.05},
     "eval_traj": {112: 58.5, 122: 41.8, 132: 35.1, 142: 350.2, 152: 646.4, 162: 482.3, 172: 600.4, 182: 600.5, 192: 699.5, 202: 684.3, 212: 758.6, 222: 744.6, 232: 745.4, 242: 869.7, 252: 721.6, 262: 820.6, 272: 716.2, 282: 755.6, 292: 843, 302: 867.6}},
    {"id": "exp_048_cheetah_civo_extension", "env": "cheetah", "gt": 1, "nve_peak": 2.750,
     "ve_ratio_peak": 24.112, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_059_walker_trained_s5", "env": "walker", "gt": 1, "nve_peak": 4.720,
     "ve_ratio_peak": 3.3075, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_068_008d_walker_repro_s1", "env": "walker", "gt": 1, "nve_peak": 4.120,
     "ve_ratio_peak": 4.6,
     "nve_traj": None,
     "ve_traj": {15: 0, 25: 0.2, 35: 0.3, 45: 0.6, 55: 0.6, 65: 1.3, 75: 1.6, 85: 4.6, 95: 4.6, 105: 2.7},
     "eval_traj": None},
    {"id": "exp_078_cheetah_008d_s0", "env": "cheetah", "gt": 1, "nve_peak": 4.100,
     "ve_ratio_peak": 2.318,
     "nve_traj": {35: 1.24, 45: 1.7, 55: 3.66, 65: 3.55, 75: 4.1, 85: 2.74, 95: 2.26, 105: 0.48},
     "ve_traj": {15: 0.039, 25: 0.056, 35: 0.11, 45: 0.295, 55: 0.908, 65: 1.72, 75: 2.318, 85: 2.022, 95: 1.366, 105: 0.291},
     "eval_traj": {5: 8.3, 15: 41.3, 25: 170, 35: 213.7, 45: 148.9, 55: 64.5, 65: 36.8, 75: 26.1, 85: 26.7, 95: 32.5, 105: 119.5}},

    # --- Healthy (36) ---
    {"id": "exp_008a_cheetah_unexposed_s0", "env": "cheetah", "gt": 0, "nve_peak": 0.490,
     "ve_ratio_peak": 0.3193, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008a_cheetah_unexposed_s1", "env": "cheetah", "gt": 0, "nve_peak": 0.478,
     "ve_ratio_peak": 0.3112, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008a_no_subsample_dt2", "env": "walker", "gt": 0, "nve_peak": 0.930,
     "ve_ratio_peak": 0.93,  # max of normalized_ve series
     "nve_traj": None,
     "ve_traj": {55: 0.93, 65: 0.66, 75: 0.75, 85: 0.68, 95: 0.79, 105: 0.59},
     "eval_traj": None},
    {"id": "exp_008a_unexposed_s1", "env": "walker", "gt": 0, "nve_peak": 0.598,
     "ve_ratio_peak": 0.43, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008a_unexposed_s2", "env": "walker", "gt": 0, "nve_peak": 0.463,
     "ve_ratio_peak": 0.333, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008e_v3_s4", "env": "walker", "gt": 0, "nve_peak": 0.990,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008e_v3_subsample_on_dt1_h15", "env": "walker", "gt": 0, "nve_peak": 1.930,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008e_v3_walker_s1", "env": "walker", "gt": 0, "nve_peak": 0.803,
     "ve_ratio_peak": 0.527, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008f_no_dt_embed_subsample_on_h8", "env": "walker", "gt": 0, "nve_peak": 1.020,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008f_s3_no_dt_embed_walker", "env": "walker", "gt": 0, "nve_peak": 1.490,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_008f_s4", "env": "walker", "gt": 0, "nve_peak": 1.410,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_009c_s3", "env": "walker", "gt": 0, "nve_peak": 0.520,
     "ve_ratio_peak": 0.386, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_015b_frozen_dt_emb", "env": "walker", "gt": 0, "nve_peak": 0.467,
     "ve_ratio_peak": None,
     "nve_traj": {85: 0.467, 95: 0.394, 105: 0.42},
     "ve_traj": None, "eval_traj": None},
    {"id": "exp_020_vanilla_dreamerv3_s2", "env": "walker", "gt": 0, "nve_peak": 0.983,
     "ve_ratio_peak": 0.645, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_024b_cheetah_no_dt_emb_s0", "env": "cheetah", "gt": 0, "nve_peak": 0.200,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_024b_cheetah_no_dt_emb_s1", "env": "cheetah", "gt": 0, "nve_peak": 0.100,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_027_tcn_walker_s0_sigma02", "env": "walker", "gt": 0, "nve_peak": 0.908,
     "ve_ratio_peak": 0.9081,
     "nve_traj": None,
     "ve_traj": {15: 0.0192, 25: 0.0961, 35: 0.1875, 45: 0.3009, 55: 0.5231, 65: 0.5654, 75: 0.611, 85: 0.4665, 95: 0.9081, 105: 0.5625},
     "eval_traj": None},
    {"id": "exp_029a_tcn_walker_s1_sigma02", "env": "walker", "gt": 0, "nve_peak": 0.643,
     "ve_ratio_peak": 0.6428,
     "nve_traj": None,
     "ve_traj": {15: 0.0248, 25: 0.1165, 35: 0.3574, 45: 0.5147, 55: 0.6428, 65: 0.4777, 75: 0.398, 85: 0.4033, 95: 0.3007, 105: 0.1554},
     "eval_traj": None},
    {"id": "exp_032_dual_critic_walker", "env": "walker", "gt": 0, "nve_peak": 1.100,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_032b_dual_critic_walker_s1", "env": "walker", "gt": 0, "nve_peak": 1.400,
     "ve_ratio_peak": None,
     "nve_traj": {15: 0.0, 25: 0.2, 35: 0.4, 45: 0.8, 55: 0.7, 65: 0.7, 75: 0.7, 85: 1.4, 95: 0.7, 105: 0.5},
     "ve_traj": None, "eval_traj": None},
    {"id": "exp_042_frozen_dt_emb_walker", "env": "walker", "gt": 0, "nve_peak": 0.194,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_043_008f_walker_s1", "env": "walker", "gt": 0, "nve_peak": 0.808,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_046_frozen_dt_emb_cheetah", "env": "cheetah", "gt": 0, "nve_peak": 1.350,
     "ve_ratio_peak": 0.4, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_047_frozen_dt_emb_walker_s1", "env": "walker", "gt": 0, "nve_peak": 1.710,
     "ve_ratio_peak": 1.099, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_057_frozen_dt_emb_walker_s2", "env": "walker", "gt": 0, "nve_peak": 1.880,
     "ve_ratio_peak": 1.283, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_058_frozen_dt_emb_cheetah_s1", "env": "cheetah", "gt": 0, "nve_peak": 0.780,
     "ve_ratio_peak": 0.231, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_067_frozen_dt_emb_walker_plan015", "env": "walker", "gt": 0, "nve_peak": 0.400,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_069_008f_walker_repro_s1", "env": "walker", "gt": 0, "nve_peak": 0.660,
     "ve_ratio_peak": 0.4,
     "nve_traj": None,
     "ve_traj": {15: 0, 25: 0.1, 35: 0.2, 45: 0.2, 55: 0.3, 65: 0.3, 75: 0.4, 85: 0.3, 95: 0.3, 105: 0.4},
     "eval_traj": {5: 30.5, 15: 158.7, 25: 180.8, 35: 250.3, 45: 293.6, 55: 272.2, 65: 328.1, 75: 244.8, 85: 382.5, 95: 390.1, 105: 237.8}},
    {"id": "exp_070_008e_v3_walker_s0", "env": "walker", "gt": 0, "nve_peak": 0.800,
     "ve_ratio_peak": 0.8,
     "nve_traj": None,
     "ve_traj": {15: 0, 25: 0.1, 35: 0.2, 45: 0.3, 55: 0.4, 65: 0.5, 75: 0.6, 85: 0.5, 95: 0.8, 105: 0.8},
     "eval_traj": {5: 37.4, 15: 93.2, 25: 178.8, 35: 221.6, 45: 230.9, 55: 232.5, 65: 194, 75: 175.2, 85: 218.6, 95: 139.6, 105: 148}},
    {"id": "exp_071_008f_walker_s3", "env": "walker", "gt": 0, "nve_peak": 0.974,
     "ve_ratio_peak": 0.7, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_072_008e_v3_walker_s5", "env": "walker", "gt": 0, "nve_peak": 0.610,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_073_008f_walker_s4", "env": "walker", "gt": 0, "nve_peak": 0.760,
     "ve_ratio_peak": 0.5, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_082_cheetah_no_dt_emb_s0", "env": "cheetah", "gt": 0, "nve_peak": 1.580,
     "ve_ratio_peak": 0.955,
     "nve_traj": {35: 1.49, 45: 0.59, 55: 0.96, 65: 0.55, 75: 0.55, 85: 0.98, 95: 1.58, 105: 1.02},
     "ve_traj": {15: 0.038, 25: 0.069, 35: 0.132, 45: 0.103, 55: 0.237, 65: 0.268, 75: 0.311, 85: 0.724, 95: 0.955, 105: 0.616},
     "eval_traj": {5: 6.8, 15: 32.2, 25: 108.4, 35: 119.4, 45: 239.3, 55: 157, 65: 180.1, 75: 178.6, 85: 84.2, 95: 57.7, 105: 83.2}},
    {"id": "exp_084_frozen_dt_emb_walker_s0", "env": "walker", "gt": 0, "nve_peak": 0.370,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_085_frozen_dt_emb_walker_s1", "env": "walker", "gt": 0, "nve_peak": 0.310,
     "ve_ratio_peak": None, "nve_traj": None, "ve_traj": None, "eval_traj": None},
    {"id": "exp_087_frozen_dt_emb_cheetah_s1", "env": "cheetah", "gt": 0, "nve_peak": 0.299,
     "ve_ratio_peak": 0.2, "nve_traj": None, "ve_traj": None, "eval_traj": None},
]


def compute_nve_from_ve(ve_traj, env):
    """Compute NVE trajectory from raw ve_ratio trajectory."""
    baseline = WALKER_BASELINE_VE if env == "walker" else CHEETAH_BASELINE_VE
    nve = {}
    for step_k, ve in sorted(ve_traj.items()):
        bl = baseline.get(step_k)
        if bl and bl > 0.05:  # skip very early steps where baseline near 0
            nve[step_k] = ve / bl
    return nve


def check_condition_b(nve_series, threshold):
    """Check if NVE > threshold for >= 2 consecutive eval points."""
    sorted_steps = sorted(nve_series.keys())
    consecutive = 0
    for step in sorted_steps:
        if nve_series[step] > threshold:
            consecutive += 1
            if consecutive >= 2:
                return True
        else:
            consecutive = 0
    return False


def check_condition_c_from_nve(nve_series):
    """Check if NVE shows upward trend.
    Simplified: check if there's a window where NVE increases for >= 2 consecutive steps.
    """
    sorted_steps = sorted(nve_series.keys())
    vals = [nve_series[s] for s in sorted_steps]
    for i in range(len(vals) - 1):
        if vals[i + 1] > vals[i] * 1.1:  # 10% increase
            return True
    return False


def check_condition_c_with_eval(nve_series, eval_series):
    """Check if NVE uptrend accompanies eval decline."""
    nve_steps = sorted(nve_series.keys())
    eval_steps = sorted(eval_series.keys())
    common_steps = sorted(set(nve_steps) & set(eval_steps))
    if len(common_steps) < 3:
        return check_condition_c_from_nve(nve_series)

    for i in range(len(common_steps) - 1):
        s1, s2 = common_steps[i], common_steps[i + 1]
        nve_up = nve_series[s2] > nve_series[s1] * 1.05
        eval_down = eval_series[s2] < eval_series[s1] * 0.9
        if nve_up and eval_down:
            return True
    return False


def compute_auroc(scores, labels):
    """Compute AUROC using trapezoidal rule."""
    pairs = sorted(zip(scores, labels), key=lambda x: -x[0])
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    if n_pos == 0 or n_neg == 0:
        return float('nan')
    tp, fp = 0, 0
    prev_tp, prev_fp = 0, 0
    auc = 0.0
    prev_score = None
    for score, label in pairs:
        if score != prev_score and prev_score is not None:
            auc += (fp - prev_fp) * (tp + prev_tp) / 2.0
            prev_tp, prev_fp = tp, fp
        if label == 1:
            tp += 1
        else:
            fp += 1
        prev_score = score
    auc += (fp - prev_fp) * (tp + prev_tp) / 2.0
    return auc / (n_pos * n_neg)


def threshold_analysis(scores_labels, thresholds):
    """Run threshold analysis for given scores and labels."""
    results = {}
    for t in thresholds:
        tp = fp = tn = fn = 0
        fp_list = []
        fn_list = []
        for exp_id, score, label in scores_labels:
            pred = 1 if score >= t else 0
            if pred == 1 and label == 1:
                tp += 1
            elif pred == 1 and label == 0:
                fp += 1
                fp_list.append((exp_id, score))
            elif pred == 0 and label == 0:
                tn += 1
            else:
                fn += 1
                fn_list.append((exp_id, score))
        total = tp + fp + tn + fn
        acc = (tp + tn) / total if total > 0 else 0
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
        results[t] = {
            "acc": acc, "prec": prec, "rec": rec, "f1": f1,
            "tp": tp, "fp": fp, "tn": tn, "fn": fn,
            "fp_list": fp_list, "fn_list": fn_list,
        }
    return results


def combined_diagnostic(exp, threshold):
    """Apply combined A+B+C diagnostic. Returns (positive, reasons)."""
    nve_peak = exp["nve_peak"]

    # Condition A: NVE_peak > threshold
    cond_a = nve_peak >= threshold

    # Get NVE trajectory
    nve_traj = exp.get("nve_traj")
    ve_traj = exp.get("ve_traj")
    eval_traj = exp.get("eval_traj")

    if nve_traj is None and ve_traj is not None:
        nve_traj = compute_nve_from_ve(ve_traj, exp["env"])

    has_traj = nve_traj is not None and len(nve_traj) >= 3

    if not has_traj:
        # Without trajectory, can only apply condition A
        # Return A-only result with note
        return cond_a, "A_only (no trajectory data)"

    # Condition B: NVE > threshold for >= 2 consecutive eval points
    cond_b = check_condition_b(nve_traj, threshold)

    # Condition C: NVE uptrend precedes/accompanies eval decline
    if eval_traj is not None:
        cond_c = check_condition_c_with_eval(nve_traj, eval_traj)
    else:
        cond_c = check_condition_c_from_nve(nve_traj)

    positive = cond_a and cond_b and cond_c
    reasons = f"A={'Y' if cond_a else 'N'} B={'Y' if cond_b else 'N'} C={'Y' if cond_c else 'N'}"
    return positive, reasons


def compute_median_last5(nve_traj):
    """Compute median of last 5 NVE values."""
    if nve_traj is None or len(nve_traj) == 0:
        return None
    sorted_vals = [nve_traj[k] for k in sorted(nve_traj.keys())]
    last5 = sorted_vals[-5:] if len(sorted_vals) >= 5 else sorted_vals
    last5_sorted = sorted(last5)
    n = len(last5_sorted)
    if n % 2 == 1:
        return last5_sorted[n // 2]
    return (last5_sorted[n // 2 - 1] + last5_sorted[n // 2]) / 2


# ============================================================
# Main Analysis
# ============================================================

print("=" * 80)
print("NVE Threshold Sensitivity Analysis V2")
print("=" * 80)

# --- Dataset summary ---
n_total = len(experiments)
n_civo = sum(1 for e in experiments if e["gt"] == 1)
n_healthy = sum(1 for e in experiments if e["gt"] == 0)
n_with_ve_peak = sum(1 for e in experiments if e["ve_ratio_peak"] is not None)
n_with_traj = sum(1 for e in experiments if e.get("ve_traj") or e.get("nve_traj"))

print(f"\nDataset: N={n_total} (CIVO={n_civo}, Healthy={n_healthy})")
print(f"Method B coverage: {n_with_ve_peak}/{n_total} have ve_ratio_peak")
print(f"Trajectory coverage: {n_with_traj}/{n_total} have time series data")

# --- Method A: Step-matched NVE ---
print("\n" + "=" * 80)
print("METHOD A: Step-matched NVE (nve_peak)")
print("=" * 80)

method_a_data = [(e["id"], e["nve_peak"], e["gt"]) for e in experiments]
thresholds = [1.3, 1.5, 1.7, 2.0]

print("\n### Single Threshold")
results_a = threshold_analysis(method_a_data, thresholds)
for t in thresholds:
    r = results_a[t]
    print(f"\nθ = {t:.1f}×:")
    print(f"  Acc={r['acc']:.1%} Prec={r['prec']:.1%} Rec={r['rec']:.1%} F1={r['f1']:.3f}")
    print(f"  TP={r['tp']} FP={r['fp']} TN={r['tn']} FN={r['fn']}")
    if r['fp_list']:
        print(f"  FP: {', '.join(f'{x[0]}({x[1]:.2f})' for x in r['fp_list'])}")
    if r['fn_list']:
        print(f"  FN: {', '.join(f'{x[0]}({x[1]:.2f})' for x in r['fn_list'])}")

scores_a = [e["nve_peak"] for e in experiments]
labels = [e["gt"] for e in experiments]
auroc_a = compute_auroc(scores_a, labels)
print(f"\nAUROC (Method A): {auroc_a:.4f}")

# --- Method A combined diagnostic ---
print("\n### Combined Diagnostic (A+B+C)")
for t in thresholds:
    tp = fp = tn = fn = 0
    a_only_count = 0
    fp_list = []
    fn_list = []
    for e in experiments:
        positive, reasons = combined_diagnostic(e, t)
        if "A_only" in reasons:
            a_only_count += 1
        if positive and e["gt"] == 1:
            tp += 1
        elif positive and e["gt"] == 0:
            fp += 1
            fp_list.append((e["id"], e["nve_peak"], reasons))
        elif not positive and e["gt"] == 0:
            tn += 1
        else:
            fn += 1
            fn_list.append((e["id"], e["nve_peak"], reasons))
    total = tp + fp + tn + fn
    acc = (tp + tn) / total if total > 0 else 0
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
    print(f"\nθ = {t:.1f}× (A_only fallback: {a_only_count}/{n_total}):")
    print(f"  Acc={acc:.1%} Prec={prec:.1%} Rec={rec:.1%} F1={f1:.3f}")
    print(f"  TP={tp} FP={fp} TN={tn} FN={fn}")
    if fp_list:
        print(f"  FP: {', '.join(f'{x[0]}({x[1]:.2f}, {x[2]})' for x in fp_list)}")
    if fn_list:
        print(f"  FN: {', '.join(f'{x[0]}({x[1]:.2f}, {x[2]})' for x in fn_list)}")


# --- Method B: Raw ve_ratio_peak ---
print("\n" + "=" * 80)
print("METHOD B: Raw ve_ratio_peak")
print("=" * 80)

method_b_exps = [e for e in experiments if e["ve_ratio_peak"] is not None]
n_b = len(method_b_exps)
n_b_civo = sum(1 for e in method_b_exps if e["gt"] == 1)
n_b_healthy = sum(1 for e in method_b_exps if e["gt"] == 0)
print(f"\nSubset with ve_ratio_peak: N={n_b} (CIVO={n_b_civo}, Healthy={n_b_healthy})")

method_b_data = [(e["id"], e["ve_ratio_peak"], e["gt"]) for e in method_b_exps]
thresholds_b = [0.8, 1.0, 1.3, 1.5, 2.0]

print("\n### Single Threshold")
results_b = threshold_analysis(method_b_data, thresholds_b)
for t in thresholds_b:
    r = results_b[t]
    print(f"\nθ = {t:.1f}×:")
    print(f"  Acc={r['acc']:.1%} Prec={r['prec']:.1%} Rec={r['rec']:.1%} F1={r['f1']:.3f}")
    print(f"  TP={r['tp']} FP={r['fp']} TN={r['tn']} FN={r['fn']}")
    if r['fp_list']:
        print(f"  FP: {', '.join(f'{x[0]}({x[1]:.3f})' for x in r['fp_list'])}")
    if r['fn_list']:
        print(f"  FN: {', '.join(f'{x[0]}({x[1]:.3f})' for x in r['fn_list'])}")

scores_b = [e["ve_ratio_peak"] for e in method_b_exps]
labels_b = [e["gt"] for e in method_b_exps]
auroc_b = compute_auroc(scores_b, labels_b)
print(f"\nAUROC (Method B): {auroc_b:.4f}")

# --- Method B combined diagnostic ---
print("\n### Combined Diagnostic (A+B+C) — using ve_ratio_peak as threshold basis")
for t in thresholds_b:
    tp = fp = tn = fn = 0
    for e in method_b_exps:
        # For method B combined, we use ve_ratio_peak for condition A
        # and ve_ratio trajectory for conditions B and C
        ve_peak = e["ve_ratio_peak"]
        cond_a = ve_peak >= t

        ve_traj = e.get("ve_traj")
        has_traj = ve_traj is not None and len(ve_traj) >= 3

        if not has_traj:
            positive = cond_a
        else:
            sorted_steps = sorted(ve_traj.keys())
            vals = [ve_traj[s] for s in sorted_steps]
            # Condition B: ve_ratio > threshold for >= 2 consecutive
            consec = 0
            cond_b = False
            for v in vals:
                if v >= t:
                    consec += 1
                    if consec >= 2:
                        cond_b = True
                        break
                else:
                    consec = 0
            # Condition C: uptrend
            cond_c = False
            for i in range(len(vals) - 1):
                if vals[i + 1] > vals[i] * 1.1:
                    cond_c = True
                    break
            positive = cond_a and cond_b and cond_c

        if positive and e["gt"] == 1:
            tp += 1
        elif positive and e["gt"] == 0:
            fp += 1
        elif not positive and e["gt"] == 0:
            tn += 1
        else:
            fn += 1
    total = tp + fp + tn + fn
    acc = (tp + tn) / total if total > 0 else 0
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
    print(f"\nθ = {t:.1f}×:")
    print(f"  Acc={acc:.1%} Prec={prec:.1%} Rec={rec:.1%} F1={f1:.3f}")
    print(f"  TP={tp} FP={fp} TN={tn} FN={fn}")


# --- NVE_median_last5 ---
print("\n" + "=" * 80)
print("NVE_median_last5 Auxiliary Metric")
print("=" * 80)

median_results = []
for e in experiments:
    nve_traj = e.get("nve_traj")
    ve_traj = e.get("ve_traj")
    if nve_traj is None and ve_traj is not None:
        nve_traj = compute_nve_from_ve(ve_traj, e["env"])
    if nve_traj is not None and len(nve_traj) >= 3:
        med = compute_median_last5(nve_traj)
        label = "CIVO" if e["gt"] == 1 else "Healthy"
        correct = (med > 1.0 and e["gt"] == 1) or (med <= 1.0 and e["gt"] == 0)
        median_results.append((e["id"], label, med, correct))

print(f"\nExperiments with sufficient trajectory data: {len(median_results)}")
print(f"\n{'exp_id':<45} {'type':<8} {'median_last5':>12} {'correct':>8}")
print("-" * 75)
for eid, label, med, correct in median_results:
    print(f"{eid:<45} {label:<8} {med:>12.3f} {'✓' if correct else '✗':>8}")

# Summary stats
civo_meds = [m for _, l, m, _ in median_results if l == "CIVO"]
healthy_meds = [m for _, l, m, _ in median_results if l == "Healthy"]
if civo_meds:
    print(f"\nCIVO median_last5: min={min(civo_meds):.3f}, median={sorted(civo_meds)[len(civo_meds)//2]:.3f}, max={max(civo_meds):.3f}")
if healthy_meds:
    print(f"Healthy median_last5: min={min(healthy_meds):.3f}, median={sorted(healthy_meds)[len(healthy_meds)//2]:.3f}, max={max(healthy_meds):.3f}")
correct_count = sum(1 for _, _, _, c in median_results if c)
print(f"Accuracy: {correct_count}/{len(median_results)} = {correct_count/len(median_results):.1%}")


# --- Distribution analysis ---
print("\n" + "=" * 80)
print("Distribution Analysis")
print("=" * 80)

civo_nve = sorted([e["nve_peak"] for e in experiments if e["gt"] == 1])
healthy_nve = sorted([e["nve_peak"] for e in experiments if e["gt"] == 0])

print(f"\nMethod A NVE_peak distribution:")
print(f"  CIVO (N={len(civo_nve)}): min={min(civo_nve):.3f}, median={civo_nve[len(civo_nve)//2]:.3f}, max={max(civo_nve):.3f}, mean={sum(civo_nve)/len(civo_nve):.3f}")
print(f"  Healthy (N={len(healthy_nve)}): min={min(healthy_nve):.3f}, median={healthy_nve[len(healthy_nve)//2]:.3f}, max={max(healthy_nve):.3f}, mean={sum(healthy_nve)/len(healthy_nve):.3f}")

civo_ve = sorted([e["ve_ratio_peak"] for e in experiments if e["gt"] == 1 and e["ve_ratio_peak"] is not None])
healthy_ve = sorted([e["ve_ratio_peak"] for e in experiments if e["gt"] == 0 and e["ve_ratio_peak"] is not None])

if civo_ve and healthy_ve:
    print(f"\nMethod B ve_ratio_peak distribution:")
    print(f"  CIVO (N={len(civo_ve)}): min={min(civo_ve):.3f}, median={civo_ve[len(civo_ve)//2]:.3f}, max={max(civo_ve):.3f}, mean={sum(civo_ve)/len(civo_ve):.3f}")
    print(f"  Healthy (N={len(healthy_ve)}): min={min(healthy_ve):.3f}, median={healthy_ve[len(healthy_ve)//2]:.3f}, max={max(healthy_ve):.3f}, mean={sum(healthy_ve)/len(healthy_ve):.3f}")
