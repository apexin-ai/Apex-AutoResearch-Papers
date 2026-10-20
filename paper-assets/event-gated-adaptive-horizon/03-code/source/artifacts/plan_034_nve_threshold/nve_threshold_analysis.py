#!/usr/bin/env python3
"""
NVE (Normalized Value-Eval ratio) Threshold Sensitivity Analysis

Reads the experiment registry, extracts NVE metrics, labels ground truth,
and computes classification performance at various NVE thresholds.
"""

import json
import re
from collections import OrderedDict

REGISTRY_PATH = "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/738d1ad5-83b9-408a-b880-7de8f3ac7af9/tool-results/mcp-agent-ml-research-read_registry-1779710700766.txt"
OUTPUT_PATH = "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis.md"

# =============================================================================
# 1. Load and parse registry
# =============================================================================
with open(REGISTRY_PATH) as f:
    raw = json.load(f)
inner = json.loads(raw['result'])
exps = inner['data']['experiments']

print(f"Total experiments in registry: {len(exps)}")

# =============================================================================
# 2. Define baseline VE ratios at each step
# =============================================================================
# Walker Walk baseline (exp_001_baseline, seed 1): ve_ratio at each step
WALKER_BASELINE_VE = {
    '25K': 0.087, '35K': 0.241, '45K': 0.331, '55K': 0.404,
    '65K': 0.563, '75K': 0.719, '85K': 0.701, '95K': 0.632, '105K': 0.656
}

# Cheetah baseline: approximate from exp_023a/023b (ve_ratio ~ 0.5-0.7 range)
CHEETAH_BASELINE_VE = {
    '25K': 0.10, '35K': 0.20, '45K': 0.30, '55K': 0.40,
    '65K': 0.50, '75K': 0.55, '85K': 0.60, '95K': 0.65, '105K': 0.65
}

# Manipulation envs (pickcube, stackcube, peginsertion) have no reliable baselines
# for NVE normalization - raw ve_ratio must be used with caution
# exp_019a_v2_pickcube_baseline has ve_ratio_range 1.05-3.56 which is already high
# So we EXCLUDE manipulation envs from NVE threshold analysis (no proper baseline)

CARTPOLE_BASELINE_VE = {
    '105K': 0.05  # approximate, too low for reliable normalization
}


def parse_step_key(k):
    """Parse step keys like '105K', '55000', '105k', '85K' to integer steps."""
    k = k.strip().upper().replace(',', '')
    if k.endswith('K'):
        return int(float(k[:-1]) * 1000)
    return int(float(k))


def detect_env(exp_id, exp_data):
    """Detect environment from experiment id and data."""
    eid_lower = exp_id.lower()
    hyp = str(exp_data.get('hypothesis', '')).lower()
    spec_cmd = str(exp_data.get('spec', {}).get('command', '')).lower()
    text = eid_lower + ' ' + hyp + ' ' + spec_cmd

    if 'cheetah' in text:
        return 'cheetah'
    if 'cartpole' in text:
        return 'cartpole'
    if 'pickcube' in text:
        return 'pickcube'
    if 'stackcube' in text:
        return 'stackcube'
    if 'peginsertion' in text or 'peg_insertion' in text:
        return 'peginsertion'
    if 'walker' in text:
        return 'walker'
    # Default: infer from parent or notes
    parent = str(exp_data.get('parent', '')).lower()
    if 'cheetah' in parent:
        return 'cheetah'
    return 'walker'  # default


def detect_config(exp_id, exp_data):
    """Detect configuration type."""
    eid = exp_id.lower()
    hyp = str(exp_data.get('hypothesis', '')).lower()

    if 'baseline' in eid or 'vanilla' in eid:
        return 'baseline'
    if 'frozen' in eid or 'frozen' in hyp or 'freeze' in hyp:
        return 'frozen_dt_emb'
    if '008f' in eid or 'no_dt_embed' in eid or 'no_dt_emb' in eid:
        return '008f_no_dt_emb'
    if '008e_v3' in eid or '008e_v3' in hyp:
        return '008e_v3_mitigation'
    if '008a' in eid:
        return '008a_unexposed'
    if '008d' in eid or 'civo_trigger' in eid:
        return '008d_civo_trigger'
    if '006' in eid:
        return '006_fixed_dt2'
    if 'dual_critic' in eid:
        return 'dual_critic'
    if 'sgs' in eid:
        return 'sgs'
    if 'tcn' in eid:
        return 'tcn'
    if 'rave' in eid:
        return 'rave'
    if 'gradient_stop' in eid:
        return 'gradient_stop'
    if 'trained' in eid:
        return 'trained_dt_emb'
    return 'other'


def detect_seed(exp_id, exp_data):
    """Extract seed from experiment id or spec."""
    eid = exp_id.lower()
    m = re.search(r'_s(\d+)(?:_|$)', eid)
    if m:
        return int(m.group(1))
    spec_cmd = str(exp_data.get('spec', {}).get('command', ''))
    m = re.search(r'--seed\s+(\d+)', spec_cmd)
    if m:
        return int(m.group(1))
    return None


def get_baseline_ve(env):
    """Get baseline VE dict for an environment."""
    if env == 'cheetah':
        return CHEETAH_BASELINE_VE
    elif env == 'cartpole':
        return CARTPOLE_BASELINE_VE
    else:
        return WALKER_BASELINE_VE


def extract_peak_nve(exp_id, exp_data, env):
    """
    Extract peak NVE from experiment data.
    Returns (peak_nve, source_description) or (None, reason).

    Priority:
    1. Direct nve_peak field (numeric)
    2. nve_max field (numeric, used in TCN experiments)
    3. Compute from normalized_ve dict/fields
    4. Compute from value_eval_ratio / baseline_ve at matched steps
    5. Compute from ve_ratio / baseline_ve at matched steps
    """
    metrics = exp_data.get('metrics', {})
    if not isinstance(metrics, dict):
        return None, "no metrics dict"

    baseline_ve = get_baseline_ve(env)

    # Manipulation envs have no reliable baseline for normalization
    is_manip_env = env in ('pickcube', 'stackcube', 'peginsertion')

    # --- Priority 1: Direct nve_peak or peak_nve field ---
    for field_name in ['nve_peak', 'peak_nve']:
        if field_name in metrics:
            val = metrics[field_name]
            if isinstance(val, (int, float)) and not isinstance(val, bool):
                return float(val), f"metrics.{field_name}"
            if isinstance(val, str):
                val_clean = val.strip().replace('x', '').replace('×', '')
                if val_clean.startswith('<'):
                    try:
                        return float(val_clean[1:].strip()) - 0.01, f"metrics.{field_name} (parsed '{val}')"
                    except:
                        pass
                try:
                    return float(val_clean), f"metrics.{field_name} (parsed '{val}')"
                except:
                    pass

    # --- Priority 2: nve_max field (used in TCN experiments) ---
    if 'nve_max' in metrics:
        val = metrics['nve_max']
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            return float(val), "metrics.nve_max"

    # --- Priority 3: normalized_ve dict or fields ---
    if 'normalized_ve' in metrics:
        nve_data = metrics['normalized_ve']
        if isinstance(nve_data, dict):
            max_nve = 0
            max_step = None
            for step_key, val in nve_data.items():
                if isinstance(val, (int, float)):
                    if float(val) > max_nve:
                        max_nve = float(val)
                        max_step = step_key
            if max_nve > 0:
                return max_nve, f"max(metrics.normalized_ve) at {max_step}"

    # Check normalized_ve_XXK fields
    nve_from_fields = {}
    for k, v in metrics.items():
        if k.startswith('normalized_ve_') and isinstance(v, (int, float)) and not isinstance(v, bool):
            nve_from_fields[k] = float(v)
    if nve_from_fields:
        max_k = max(nve_from_fields, key=nve_from_fields.get)
        return nve_from_fields[max_k], f"max({max_k})"

    # Check individual nve_XXK fields (not nve_peak, nve_classification, etc.)
    nve_step_vals = {}
    for k, v in metrics.items():
        if re.match(r'nve_\d+[kK]?$', k) and isinstance(v, (int, float)) and not isinstance(v, bool):
            nve_step_vals[k] = float(v)
    # Also nve_final, nve_final_105k, final_nve, final_NVE
    for fld in ['nve_final', 'nve_final_105k', 'final_nve', 'final_NVE']:
        if fld in metrics and isinstance(metrics[fld], (int, float)) and not isinstance(metrics[fld], bool):
            nve_step_vals[fld] = float(metrics[fld])
    if nve_step_vals:
        max_k = max(nve_step_vals, key=nve_step_vals.get)
        return nve_step_vals[max_k], f"max({max_k})"

    # Check eval_checkpoints structure (like 008f)
    nve_from_checkpoints = {}
    if 'eval_checkpoints' in metrics and isinstance(metrics['eval_checkpoints'], dict):
        for step_key, checkpoint in metrics['eval_checkpoints'].items():
            if isinstance(checkpoint, dict) and 'normalized_ve' in checkpoint:
                nve_from_checkpoints[step_key] = float(checkpoint['normalized_ve'])
        if nve_from_checkpoints:
            max_k = max(nve_from_checkpoints, key=nve_from_checkpoints.get)
            return nve_from_checkpoints[max_k], f"max(eval_checkpoints.normalized_ve) at {max_k}"

    # --- Priority 4/5: Compute NVE from ve_ratio / baseline ---
    # Skip for manipulation envs (no reliable baseline)
    if is_manip_env:
        return None, f"no pre-computed NVE and no reliable baseline for {env}"

    ve_ratios = {}

    # value_eval_ratio dict
    if 'value_eval_ratio' in metrics and isinstance(metrics['value_eval_ratio'], dict):
        for step_key, val in metrics['value_eval_ratio'].items():
            if isinstance(val, (int, float)):
                ve_ratios[step_key] = float(val)

    # value_eval_ratio_XXK fields
    for k, v in metrics.items():
        if k.startswith('value_eval_ratio_') and not k.endswith('stable'):
            if isinstance(v, (int, float)):
                step_key = k.replace('value_eval_ratio_', '')
                ve_ratios[step_key] = float(v)
            elif isinstance(v, str):
                try:
                    v_clean = v.strip().replace('%', '')
                    fv = float(v_clean)
                    if fv > 1 and '%' in v:
                        fv /= 100.0
                    step_key = k.replace('value_eval_ratio_', '')
                    ve_ratios[step_key] = fv
                except:
                    pass

    # ve_ratio_trajectory dict or list
    if 've_ratio_trajectory' in metrics:
        traj = metrics['ve_ratio_trajectory']
        if isinstance(traj, dict):
            for step_key, val in traj.items():
                if isinstance(val, (int, float)):
                    ve_ratios[step_key] = float(val)
        elif isinstance(traj, list):
            for item in traj:
                if isinstance(item, dict) and 'step' in item and 've' in item:
                    ve_ratios[str(item['step'])] = float(item['ve'])

    # ve_ratio_XXK fields
    for k, v in metrics.items():
        if re.match(r've_ratio_\d+[kK]?$', k) and isinstance(v, (int, float)):
            step_key = k.replace('ve_ratio_', '')
            ve_ratios[step_key] = float(v)

    # ve_ratio dict (TCN experiments store raw ve_ratio as dict)
    if 've_ratio' in metrics and isinstance(metrics['ve_ratio'], dict):
        for step_key, val in metrics['ve_ratio'].items():
            if isinstance(val, (int, float)):
                ve_ratios[step_key] = float(val)

    # eval_checkpoints ve_ratio
    if 'eval_checkpoints' in metrics and isinstance(metrics['eval_checkpoints'], dict):
        for step_key, checkpoint in metrics['eval_checkpoints'].items():
            if isinstance(checkpoint, dict) and 've_ratio' in checkpoint:
                ve_ratios[step_key] = float(checkpoint['ve_ratio'])

    # Compute NVE = ve_ratio / baseline_ve for each matched step
    if ve_ratios:
        max_nve = 0
        max_step = None
        for step_key, ve in ve_ratios.items():
            try:
                step_val = parse_step_key(step_key)
            except:
                continue
            normalized_key = f"{step_val // 1000}K"
            if normalized_key in baseline_ve and baseline_ve[normalized_key] > 0.05:
                nve = ve / baseline_ve[normalized_key]
                if nve > max_nve:
                    max_nve = nve
                    max_step = normalized_key
        if max_nve > 0:
            return max_nve, f"computed ve_ratio/baseline at {max_step}"

    # --- Fallback: use ve_ratio_peak / max_baseline ---
    if 've_ratio_peak' in metrics and isinstance(metrics['ve_ratio_peak'], (int, float)):
        ve_peak = float(metrics['ve_ratio_peak'])
        peak_step = metrics.get('ve_ratio_peak_step', None)
        if peak_step:
            try:
                step_val = parse_step_key(str(peak_step))
                normalized_key = f"{step_val // 1000}K"
                if normalized_key in baseline_ve and baseline_ve[normalized_key] > 0.05:
                    return ve_peak / baseline_ve[normalized_key], f"computed ve_ratio_peak/baseline at {normalized_key}"
            except:
                pass
        max_baseline = max(baseline_ve.values())
        if max_baseline > 0:
            return ve_peak / max_baseline, f"computed ve_ratio_peak/max_baseline_ve"

    # Fallback for civo_ve_ratio_final
    if 'civo_ve_ratio_final' in metrics:
        ve = float(metrics['civo_ve_ratio_final'])
        max_baseline = max(baseline_ve.values())
        if max_baseline > 0:
            return ve / max_baseline, f"computed civo_ve_ratio_final/max_baseline_ve"

    # Check ve_ratio_105k or ve_ratio_final
    for fld in ['ve_ratio_105k', 've_ratio_final']:
        if fld in metrics and isinstance(metrics[fld], (int, float)):
            ve = float(metrics[fld])
            if '105K' in baseline_ve and baseline_ve['105K'] > 0.05:
                return ve / baseline_ve['105K'], f"computed {fld}/baseline_105K"

    return None, "no VE/NVE data found"


# =============================================================================
# 3. Ground truth labeling
# =============================================================================

# Explicit manual labels based on thorough registry review
# 1 = CIVO collapsed, 0 = Healthy
MANUAL_LABELS = {
    # --- CIVO COLLAPSED (1) ---
    # 006: fixed dt=2, VE accelerating to 2.722, eval crashing
    'exp_006_fixed_dt2': 1,
    # 008d: trained dt_emb + subsample ON + H=8 = CIVO trigger
    'exp_008d_subsample_on_h8': 1,
    'exp_008d_civo_trigger_s3': 1,
    'exp_008d_civo_trigger_s4': 1,
    'exp_009e_008d_walker_s1': 1,
    'exp_068_008d_walker_repro_s1': 1,
    'exp_009b_008d_walker_s2': 1,   # onset_self_correcting BUT peak nve=1.62, eval poor
    # trained dt_emb walker - CIVO positive
    'exp_059_walker_trained_s5': 1,
    # 008e_v3 mitigation FAILURES (trained dt_emb + dt=1 imag, but still collapsed)
    'exp_008e_v3_walker_s2': 1,     # nve=3.78, eval 715->137
    'exp_008e_v3_s3': 1,            # nve=4.02, eval 520->93
    # 008d extension (reached nve=4.91 before treatment)
    'exp_045_treatment_extension_008d_s3': 1,
    # Cheetah CIVO trigger
    'exp_010b_cheetah_civo_trigger_s0': 1,   # nve_105K=70.64
    'exp_010b_cheetah_civo_trigger': 1,      # nve_peak=8.27
    'exp_048_cheetah_civo_extension': 1,     # cheetah CIVO extension
    # SGS cheetah collapsed
    'exp_021_full_sgs_cheetah_s1': 1,   # nve_peak=9.94
    # Dual critic still collapsed
    'exp_034_dual_critic_cheetah': 1,   # ve_ratio_peak=1.8 at 55K -> nve=4.5
    'exp_036_dual_critic_pickcube': 1,  # nve_peak=2.3
    'exp_037_wide_critic_cheetah': 1,   # nve_peak=3.6
    # TCN experiments that collapsed
    'exp_027_tcn_walker_s0': 1,         # nve_peak=3.965
    'exp_027_tcn_walker_s1': 1,         # nve_max=1.637 (from ve_ratio), conclusion=negative
    'exp_029b_tcn_walker_s2_sigma02': 1,  # nve_peak=2.765
    'exp_029d_tcn_walker_s3_sigma02': 1,  # nve_peak=3.0
    'exp_030b_tcn_cheetah_s0_sigma05': 1,  # nve_max=10.666
    'exp_031_tcn_pickcube_s0_sigma02': 1,  # CIVO in pickcube
    'exp_031b_tcn_pickcube_s0_sigma05': 1,  # nve_peak=3.3

    # --- HEALTHY (0) ---
    # 008a: unexposed trained dt_emb, no CIVO
    'exp_008a_no_subsample_dt2': 0,
    'exp_008a_unexposed_s1': 0,
    'exp_008a_unexposed_s2': 0,
    'exp_008a_cheetah_unexposed_s0': 0,
    'exp_008a_cheetah_unexposed_s1': 0,
    # 008e_v3 mitigation SUCCESSES
    'exp_008e_v3_subsample_on_dt1_h15': 0,
    'exp_008e_v3_walker_s1': 0,
    'exp_008e_v3_s4': 0,
    'exp_072_008e_v3_walker_s5': 0,
    'exp_070_008e_v3_walker_s0': 0,  # negative but NOT via CIVO per notes
    # 008f: no dt_emb, no CIVO
    'exp_008f_no_dt_embed_subsample_on_h8': 0,
    'exp_008f_s3_no_dt_embed_walker': 0,
    'exp_008f_s4': 0,
    'exp_043_008f_walker_s1': 0,
    'exp_069_008f_walker_repro_s1': 0,
    'exp_071_008f_walker_s3': 0,
    'exp_073_008f_walker_s4': 0,
    # Frozen dt_emb: no CIVO (frozen prevents CIVO)
    'exp_042_frozen_dt_emb_walker': 0,
    'exp_015b_frozen_dt_emb': 0,
    'exp_046_frozen_dt_emb_cheetah': 0,
    'exp_047_frozen_dt_emb_walker_s1': 0,
    'exp_057_frozen_dt_emb_walker_s2': 0,
    'exp_058_frozen_dt_emb_cheetah_s1': 0,
    'exp_067_frozen_dt_emb_walker_plan015': 0,
    # Vanilla DreamerV3
    'exp_020_vanilla_dreamerv3_s2': 0,
    # Cheetah no_dt_emb
    'exp_024b_cheetah_no_dt_emb_s0': 0,
    'exp_024b_cheetah_no_dt_emb_s1': 0,
    # TCN healthy seeds
    'exp_027_tcn_walker_s0_sigma02': 0,
    'exp_029a_tcn_walker_s1_sigma02': 0,
    # Dual critic healthy
    'exp_032_dual_critic_walker': 0,
    'exp_032b_dual_critic_walker_s1': 0,
    # 009c_s3 (008f config seed 3, healthy)
    'exp_009c_s3': 0,
    # 009c_008f_walker_s2 negative but no CIVO per verdict
    'exp_009c_008f_walker_s2': 0,
}


# =============================================================================
# 4. Build dataset
# =============================================================================
dataset = []
excluded = []

for exp_id, exp_data in exps.items():
    env = detect_env(exp_id, exp_data)
    config = detect_config(exp_id, exp_data)
    seed = detect_seed(exp_id, exp_data)
    conclusion = exp_data.get('conclusion', 'N/A')
    status = exp_data.get('status', '')

    peak_nve, nve_source = extract_peak_nve(exp_id, exp_data, env)

    # Determine ground truth
    if exp_id in MANUAL_LABELS:
        label = MANUAL_LABELS[exp_id]
        label_reason = "manual label"
    elif conclusion in ('killed', 'failed'):
        label = None
        label_reason = "technical failure"
    elif status in ('ALLOCATED', 'RUNNING', 'SUBMITTED') and conclusion == 'N/A':
        label = None
        label_reason = "not completed"
    elif config == 'baseline':
        label = None
        label_reason = "baseline (reference)"
    elif peak_nve is None:
        label = None
        label_reason = "no NVE data"
    elif env in ('pickcube', 'stackcube', 'peginsertion', 'cartpole'):
        # Manipulation envs and cartpole excluded unless manually labeled
        label = None
        label_reason = f"excluded {env} env (no reliable baseline for NVE)"
    else:
        label = None
        label_reason = "ambiguous (not manually labeled)"

    entry = {
        'exp_id': exp_id,
        'env': env,
        'config': config,
        'seed': seed,
        'conclusion': conclusion,
        'peak_nve': peak_nve,
        'nve_source': nve_source,
        'ground_truth': label,
        'label_reason': label_reason,
    }

    if label is not None:
        dataset.append(entry)
    else:
        excluded.append(entry)

# Sort dataset by exp_id
dataset.sort(key=lambda x: x['exp_id'])
excluded.sort(key=lambda x: x['exp_id'])

n_collapsed = sum(1 for d in dataset if d['ground_truth'] == 1)
n_healthy = sum(1 for d in dataset if d['ground_truth'] == 0)

print(f"\nDataset: {len(dataset)} samples")
print(f"  Collapsed (1): {n_collapsed}")
print(f"  Healthy (0): {n_healthy}")
print(f"Excluded: {len(excluded)} experiments")

# Validate NVE extraction
print("\nDataset entries:")
for d in dataset:
    nve_str = f"{d['peak_nve']:.3f}" if d['peak_nve'] is not None else "N/A"
    gt_str = "CIVO" if d['ground_truth'] == 1 else "OK"
    print(f"  {d['exp_id']:50s} {gt_str:5s} nve={nve_str:>10s}  src={d['nve_source']}")


# =============================================================================
# 5. Classification at various NVE thresholds
# =============================================================================
thresholds = [1.0, 1.1, 1.2, 1.3, 1.5, 1.7, 2.0]

# Filter out entries without NVE for classification
classifiable = [d for d in dataset if d['peak_nve'] is not None]
print(f"\nClassifiable (have NVE): {len(classifiable)}")

results = []
for thresh in thresholds:
    tp = fp = tn = fn = 0
    for d in classifiable:
        predicted = 1 if d['peak_nve'] >= thresh else 0
        actual = d['ground_truth']
        if predicted == 1 and actual == 1:
            tp += 1
        elif predicted == 1 and actual == 0:
            fp += 1
        elif predicted == 0 and actual == 0:
            tn += 1
        elif predicted == 0 and actual == 1:
            fn += 1

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    accuracy = (tp + tn) / len(classifiable) if len(classifiable) > 0 else 0.0

    results.append({
        'threshold': thresh,
        'TP': tp, 'FP': fp, 'TN': tn, 'FN': fn,
        'Precision': precision, 'Recall': recall, 'F1': f1, 'Accuracy': accuracy,
    })

# =============================================================================
# 6. AUROC computation (trapezoidal rule)
# =============================================================================
auroc = None
auroc_note = ""

positives = sorted([d['peak_nve'] for d in classifiable if d['ground_truth'] == 1])
negatives = sorted([d['peak_nve'] for d in classifiable if d['ground_truth'] == 0])

if len(classifiable) >= 10 and len(positives) > 0 and len(negatives) > 0:
    # Generate ROC curve points at many thresholds
    all_nve = sorted(set([d['peak_nve'] for d in classifiable]), reverse=True)
    roc_thresholds = [max(all_nve) + 1.0] + all_nve + [min(all_nve) - 1.0]

    roc_points = []
    for t in roc_thresholds:
        tp = sum(1 for v in positives if v >= t)
        fp = sum(1 for v in negatives if v >= t)
        tpr = tp / len(positives)
        fpr = fp / len(negatives)
        roc_points.append((fpr, tpr))

    roc_points.sort(key=lambda x: (x[0], x[1]))

    # Remove duplicates keeping max TPR for each FPR
    unique_fpr = OrderedDict()
    for fpr, tpr in roc_points:
        if fpr not in unique_fpr or tpr > unique_fpr[fpr]:
            unique_fpr[fpr] = tpr
    roc_points = [(fpr, tpr) for fpr, tpr in unique_fpr.items()]

    # Trapezoidal AUC
    auroc = 0.0
    for i in range(1, len(roc_points)):
        x0, y0 = roc_points[i-1]
        x1, y1 = roc_points[i]
        auroc += (x1 - x0) * (y0 + y1) / 2.0

    auroc_note = f"Computed from {len(positives)} positive + {len(negatives)} negative samples using {len(roc_points)} ROC points"
else:
    auroc_note = f"Sample size {len(classifiable)} (pos={len(positives)}, neg={len(negatives)}), AUROC not computed"

# =============================================================================
# 7. Find best threshold
# =============================================================================
best_result = max(results, key=lambda r: r['F1'])
best_threshold = best_result['threshold']

# Also check: at 1.5 (paper commonly used) what's the performance?
result_15 = [r for r in results if r['threshold'] == 1.5][0]

# =============================================================================
# 8. Generate markdown report
# =============================================================================
lines = []
lines.append("# NVE Threshold Sensitivity Analysis\n")

# Dataset table
lines.append("## 数据集\n")
lines.append(f"样本总数: {len(classifiable)} (Collapsed: {sum(1 for d in classifiable if d['ground_truth'] == 1)}, "
             f"Healthy: {sum(1 for d in classifiable if d['ground_truth'] == 0)})\n")
lines.append("| exp_id | env | config | seed | ground_truth | peak_nve | nve_source |")
lines.append("|--------|-----|--------|------|-------------|----------|------------|")
for d in classifiable:
    gt_str = "CIVO(1)" if d['ground_truth'] == 1 else "Healthy(0)"
    seed_str = str(d['seed']) if d['seed'] is not None else "?"
    nve_str = f"{d['peak_nve']:.3f}"
    lines.append(f"| {d['exp_id']} | {d['env']} | {d['config']} | {seed_str} | {gt_str} | {nve_str} | {d['nve_source']} |")

lines.append("")

# Classification results
lines.append("## 分类结果\n")
lines.append("| threshold | TP | FP | TN | FN | Precision | Recall | F1 | Accuracy |")
lines.append("|-----------|----|----|----|----|-----------|--------|-----|----------|")
for r in results:
    marker = " **" if r['threshold'] == best_threshold else ""
    lines.append(f"| {r['threshold']:.1f}{marker} | {r['TP']} | {r['FP']} | {r['TN']} | {r['FN']} | "
                 f"{r['Precision']:.3f} | {r['Recall']:.3f} | {r['F1']:.3f} | {r['Accuracy']:.3f} |")

lines.append("")

# AUROC
lines.append("## AUROC\n")
if auroc is not None:
    lines.append(f"**AUROC = {auroc:.4f}**\n")
    lines.append(f"{auroc_note}\n")

    lines.append("ROC 关键点 (FPR, TPR):\n")
    lines.append("| Threshold | FPR | TPR |")
    lines.append("|-----------|-----|-----|")
    n_pos = sum(1 for d in classifiable if d['ground_truth'] == 1)
    n_neg = sum(1 for d in classifiable if d['ground_truth'] == 0)
    for t in thresholds:
        tp = sum(1 for d in classifiable if d['ground_truth'] == 1 and d['peak_nve'] >= t)
        fp = sum(1 for d in classifiable if d['ground_truth'] == 0 and d['peak_nve'] >= t)
        tpr = tp / n_pos if n_pos > 0 else 0
        fpr = fp / n_neg if n_neg > 0 else 0
        lines.append(f"| {t:.1f} | {fpr:.3f} | {tpr:.3f} |")
    lines.append("")
else:
    lines.append(f"{auroc_note}\n")

# Recommended threshold
lines.append("## 推荐阈值\n")
lines.append(f"**推荐阈值: NVE >= {best_threshold:.1f}** (基于最高 F1 = {best_result['F1']:.3f})\n")
lines.append(f"- Precision = {best_result['Precision']:.3f}, Recall = {best_result['Recall']:.3f}, Accuracy = {best_result['Accuracy']:.3f}")
lines.append(f"- TP={best_result['TP']}, FP={best_result['FP']}, TN={best_result['TN']}, FN={best_result['FN']}\n")

if result_15['F1'] != best_result['F1']:
    lines.append(f"论文常用阈值 1.5 的性能: F1={result_15['F1']:.3f}, Precision={result_15['Precision']:.3f}, Recall={result_15['Recall']:.3f}\n")

lines.append("### 阈值选择权衡\n")
lines.append("- **低阈值 (1.0-1.2)**: 高 Recall (少漏报) 但多误报。适用于安全优先场景 (宁可误报不可漏报)。")
lines.append("- **中阈值 (1.3-1.5)**: Recall/Precision 平衡。1.5 是 CIVO 论文推荐的 onset 检测阈值。")
lines.append("- **高阈值 (1.7-2.0)**: 高 Precision (少误报) 但可能漏报早期 CIVO。适用于减少不必要干预。\n")

# Misclassification details at best threshold
lines.append(f"### 最佳阈值 ({best_threshold:.1f}) 下的分类细节\n")
fp_list = [d for d in classifiable if d['ground_truth'] == 0 and d['peak_nve'] >= best_threshold]
fn_list = [d for d in classifiable if d['ground_truth'] == 1 and d['peak_nve'] < best_threshold]

if fp_list:
    lines.append("**False Positives (误报为CIVO):**\n")
    for d in fp_list:
        lines.append(f"- `{d['exp_id']}`: peak_nve={d['peak_nve']:.3f}, config={d['config']}, env={d['env']}")
    lines.append("")

if fn_list:
    lines.append("**False Negatives (漏报CIVO):**\n")
    for d in fn_list:
        lines.append(f"- `{d['exp_id']}`: peak_nve={d['peak_nve']:.3f}, config={d['config']}, env={d['env']}")
    lines.append("")

if not fp_list and not fn_list:
    lines.append("无误分类。\n")

# Also show misclassification at 1.5 threshold
lines.append(f"### 阈值 1.5 下的分类细节\n")
fp_15 = [d for d in classifiable if d['ground_truth'] == 0 and d['peak_nve'] >= 1.5]
fn_15 = [d for d in classifiable if d['ground_truth'] == 1 and d['peak_nve'] < 1.5]

if fp_15:
    lines.append("**False Positives (误报为CIVO):**\n")
    for d in fp_15:
        lines.append(f"- `{d['exp_id']}`: peak_nve={d['peak_nve']:.3f}, config={d['config']}, env={d['env']}")
    lines.append("")

if fn_15:
    lines.append("**False Negatives (漏报CIVO):**\n")
    for d in fn_15:
        lines.append(f"- `{d['exp_id']}`: peak_nve={d['peak_nve']:.3f}, config={d['config']}, env={d['env']}")
    lines.append("")

# Methodology
lines.append("## 方法论说明\n")
lines.append("### NVE 计算方法\n")
lines.append("NVE (Normalized Value-Eval ratio) = experiment_ve_ratio / baseline_ve_ratio_at_same_step\n")
lines.append("- Walker Walk baseline: exp_001_baseline (seed 1) per-step VE ratios: " +
             ", ".join(f"{k}={v}" for k, v in sorted(WALKER_BASELINE_VE.items(), key=lambda x: parse_step_key(x[0]))))
lines.append("- Cheetah Run baseline: approximate VE trajectory from exp_023a/023b: " +
             ", ".join(f"{k}={v}" for k, v in sorted(CHEETAH_BASELINE_VE.items(), key=lambda x: parse_step_key(x[0]))))
lines.append("- 取 peak NVE (训练过程中最大 NVE) 作为分类特征")
lines.append("- NVE 数据提取优先级: nve_peak > nve_max > normalized_ve > ve_ratio/baseline")
lines.append("- 操控环境 (pickcube/stackcube/peginsertion) 和 cartpole 因缺乏可靠 baseline 而排除\n")

lines.append("### Ground Truth 标注\n")
lines.append(f"- **CIVO(1)** ({n_collapsed} 个): conclusion=negative/success + 明确 CIVO collapse 证据 (VE 持续加速, eval 显著下降, nve_classification=onset_collapse)")
lines.append(f"- **Healthy(0)** ({n_healthy} 个): conclusion=success + 无 CIVO 迹象 (VE 稳定, eval 保持或增长)")
lines.append("- **EXCLUDE**: conclusion=killed/failed (技术故障), 无 NVE 数据, baseline 实验, 操控环境, 分类模糊\n")

lines.append(f"### 排除实验 ({len(excluded)} 个)\n")
exclude_reasons = {}
for e in excluded:
    reason = e['label_reason']
    if reason not in exclude_reasons:
        exclude_reasons[reason] = []
    exclude_reasons[reason].append(e['exp_id'])

for reason, ids in sorted(exclude_reasons.items()):
    lines.append(f"- **{reason}** ({len(ids)}): {', '.join(sorted(ids)[:5])}" +
                 (f" ...+{len(ids)-5} more" if len(ids) > 5 else ""))

lines.append("")

# NVE distribution summary
lines.append("### NVE 分布\n")
collapsed_nves = sorted([d['peak_nve'] for d in classifiable if d['ground_truth'] == 1])
healthy_nves = sorted([d['peak_nve'] for d in classifiable if d['ground_truth'] == 0])

if collapsed_nves:
    lines.append(f"- CIVO collapsed ({len(collapsed_nves)}): min={min(collapsed_nves):.3f}, "
                 f"median={collapsed_nves[len(collapsed_nves)//2]:.3f}, "
                 f"max={max(collapsed_nves):.3f}, mean={sum(collapsed_nves)/len(collapsed_nves):.3f}")
if healthy_nves:
    lines.append(f"- Healthy ({len(healthy_nves)}): min={min(healthy_nves):.3f}, "
                 f"median={healthy_nves[len(healthy_nves)//2]:.3f}, "
                 f"max={max(healthy_nves):.3f}, mean={sum(healthy_nves)/len(healthy_nves):.3f}")

if collapsed_nves and healthy_nves:
    gap = min(collapsed_nves) - max(healthy_nves)
    lines.append(f"- 类间间距 (min_collapsed - max_healthy): {gap:.3f}")
    if gap > 0:
        lines.append(f"  - 两类完全可分（无重叠），任何 [{max(healthy_nves):.3f}, {min(collapsed_nves):.3f}] 范围内的阈值均可达到 100% 准确率")
    else:
        overlap_collapsed = [v for v in collapsed_nves if v <= max(healthy_nves)]
        overlap_healthy = [v for v in healthy_nves if v >= min(collapsed_nves)]
        lines.append(f"  - 重叠区域: {len(overlap_collapsed)} collapsed 样本 + {len(overlap_healthy)} healthy 样本在 "
                     f"[{min(collapsed_nves):.3f}, {max(healthy_nves):.3f}] 重叠范围内")
        if overlap_collapsed:
            lines.append(f"  - 重叠 collapsed: " + ", ".join(
                f"{d['exp_id']}(nve={d['peak_nve']:.3f})"
                for d in classifiable if d['ground_truth'] == 1 and d['peak_nve'] <= max(healthy_nves)
            ))
        if overlap_healthy:
            lines.append(f"  - 重叠 healthy: " + ", ".join(
                f"{d['exp_id']}(nve={d['peak_nve']:.3f})"
                for d in classifiable if d['ground_truth'] == 0 and d['peak_nve'] >= min(collapsed_nves)
            ))

lines.append("")

# Write report
report = "\n".join(lines)
with open(OUTPUT_PATH, 'w') as f:
    f.write(report)

print(f"\nReport written to: {OUTPUT_PATH}")
print(f"\n{'='*60}")
print("SUMMARY")
print(f"{'='*60}")
print(f"Best threshold (F1): {best_threshold} (F1={best_result['F1']:.3f})")
if auroc is not None:
    print(f"AUROC: {auroc:.4f}")
print(f"Dataset: {len(classifiable)} samples ({sum(1 for d in classifiable if d['ground_truth']==1)} CIVO, "
      f"{sum(1 for d in classifiable if d['ground_truth']==0)} healthy)")
