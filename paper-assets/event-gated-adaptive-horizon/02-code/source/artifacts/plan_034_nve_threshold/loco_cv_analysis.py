#!/usr/bin/env python3
"""Leave-One-Config-Out (LOCO) Cross-Validation for NVE threshold robustness."""

import numpy as np
from collections import defaultdict

DATA = [
    ("exp_006_fixed_dt2", "006_fixed_dt2", 1, 4.835),
    ("exp_008a_cheetah_unexposed_s0", "008a_unexposed", 0, 0.490),
    ("exp_008a_cheetah_unexposed_s1", "008a_unexposed", 0, 0.478),
    ("exp_008a_no_subsample_dt2", "008a_unexposed", 0, 0.930),
    ("exp_008a_unexposed_s1", "008a_unexposed", 0, 0.598),
    ("exp_008a_unexposed_s2", "008a_unexposed", 0, 0.463),
    ("exp_008d_civo_trigger_s3", "008d_civo_trigger", 1, 1.530),
    ("exp_008d_civo_trigger_s4", "008d_civo_trigger", 1, 4.620),
    ("exp_008d_subsample_on_h8", "008d_civo_trigger", 1, 4.124),
    ("exp_008e_v3_s3", "008e_v3_mitigation", 1, 4.020),
    ("exp_008e_v3_s4", "008e_v3_mitigation", 0, 0.990),
    ("exp_008e_v3_subsample_on_dt1_h15", "008e_v3_mitigation", 0, 1.930),
    ("exp_008e_v3_walker_s1", "008e_v3_mitigation", 0, 0.803),
    ("exp_008e_v3_walker_s2", "008e_v3_mitigation", 1, 3.780),
    ("exp_008f_no_dt_embed_subsample_on_h8", "008f_no_dt_emb", 0, 1.020),
    ("exp_008f_s3_no_dt_embed_walker", "008f_no_dt_emb", 0, 1.490),
    ("exp_008f_s4", "008f_no_dt_emb", 0, 1.410),
    ("exp_009b_008d_walker_s2", "008d_civo_trigger", 1, 1.620),
    ("exp_009c_s3", "other", 0, 0.520),
    ("exp_009e_008d_walker_s1", "008d_civo_trigger", 1, 4.130),
    ("exp_010b_cheetah_civo_trigger", "008d_civo_trigger", 1, 8.270),
    ("exp_010b_cheetah_civo_trigger_s0", "008d_civo_trigger", 1, 70.640),
    ("exp_015b_frozen_dt_emb", "frozen_dt_emb", 0, 0.467),
    ("exp_020_vanilla_dreamerv3_s2", "baseline", 0, 0.983),
    ("exp_021_full_sgs_cheetah_s1", "sgs", 1, 9.940),
    ("exp_024b_cheetah_no_dt_emb_s0", "008f_no_dt_emb", 0, 0.200),
    ("exp_024b_cheetah_no_dt_emb_s1", "008f_no_dt_emb", 0, 0.100),
    ("exp_027_tcn_walker_s0", "tcn", 1, 3.965),
    ("exp_027_tcn_walker_s0_sigma02", "tcn", 0, 0.908),
    ("exp_027_tcn_walker_s1", "tcn", 1, 1.637),
    ("exp_029a_tcn_walker_s1_sigma02", "tcn", 0, 0.643),
    ("exp_029b_tcn_walker_s2_sigma02", "tcn", 1, 2.765),
    ("exp_029d_tcn_walker_s3_sigma02", "tcn", 1, 3.000),
    ("exp_030b_tcn_cheetah_s0_sigma05", "tcn", 1, 10.666),
    ("exp_031b_tcn_pickcube_s0_sigma05", "tcn", 1, 3.300),
    ("exp_032_dual_critic_walker", "dual_critic", 0, 1.100),
    ("exp_032b_dual_critic_walker_s1", "dual_critic", 0, 1.400),
    ("exp_034_dual_critic_cheetah", "dual_critic", 1, 4.500),
    ("exp_036_dual_critic_pickcube", "dual_critic", 1, 2.300),
    ("exp_037_wide_critic_cheetah", "other", 1, 3.600),
    ("exp_042_frozen_dt_emb_walker", "frozen_dt_emb", 0, 0.194),
    ("exp_043_008f_walker_s1", "008f_no_dt_emb", 0, 0.808),
    ("exp_045_treatment_extension_008d_s3", "008d_civo_trigger", 1, 4.910),
    ("exp_046_frozen_dt_emb_cheetah", "frozen_dt_emb", 0, 1.350),
    ("exp_047_frozen_dt_emb_walker_s1", "frozen_dt_emb", 0, 1.710),
    ("exp_048_cheetah_civo_extension", "other", 1, 2.750),
    ("exp_057_frozen_dt_emb_walker_s2", "frozen_dt_emb", 0, 1.880),
    ("exp_058_frozen_dt_emb_cheetah_s1", "frozen_dt_emb", 0, 0.780),
    ("exp_059_walker_trained_s5", "trained_dt_emb", 1, 4.720),
    ("exp_067_frozen_dt_emb_walker_plan015", "frozen_dt_emb", 0, 0.400),
    ("exp_068_008d_walker_repro_s1", "008d_civo_trigger", 1, 4.120),
    ("exp_069_008f_walker_repro_s1", "008f_no_dt_emb", 0, 0.660),
    ("exp_070_008e_v3_walker_s0", "008e_v3_mitigation", 0, 0.800),
    ("exp_071_008f_walker_s3", "008f_no_dt_emb", 0, 0.974),
    ("exp_072_008e_v3_walker_s5", "008e_v3_mitigation", 0, 0.610),
    ("exp_073_008f_walker_s4", "008f_no_dt_emb", 0, 0.760),
]

def compute_auroc(labels, scores):
    pos = sorted([s for s, l in zip(scores, labels) if l == 1])
    neg = sorted([s for s, l in zip(scores, labels) if l == 0])
    n_pos, n_neg = len(pos), len(neg)
    if n_pos == 0 or n_neg == 0:
        return float('nan')
    concordant = 0
    tied = 0
    for p in pos:
        for n in neg:
            if p > n:
                concordant += 1
            elif p == n:
                tied += 0.5
    return (concordant + tied) / (n_pos * n_neg)

def classify(nve_values, labels, threshold):
    tp = fp = tn = fn = 0
    for nve, label in zip(nve_values, labels):
        pred = 1 if nve >= threshold else 0
        if pred == 1 and label == 1: tp += 1
        elif pred == 1 and label == 0: fp += 1
        elif pred == 0 and label == 0: tn += 1
        else: fn += 1
    return tp, fp, tn, fn

def f1_score(tp, fp, tn, fn):
    if tp + fp == 0 or tp + fn == 0:
        return 0.0
    prec = tp / (tp + fp)
    rec = tp / (tp + fn)
    if prec + rec == 0:
        return 0.0
    return 2 * prec * rec / (prec + rec)

def find_optimal_threshold(nve_values, labels):
    all_nve = sorted(set(nve_values))
    candidates = [0.0]
    for i in range(len(all_nve)):
        candidates.append(all_nve[i])
        if i + 1 < len(all_nve):
            candidates.append((all_nve[i] + all_nve[i + 1]) / 2)
    candidates.append(all_nve[-1] + 0.1)

    best_f1 = -1
    best_thresh = 0
    for t in candidates:
        tp, fp, tn, fn = classify(nve_values, labels, t)
        f = f1_score(tp, fp, tn, fn)
        if f > best_f1:
            best_f1 = f
            best_thresh = t
    return best_thresh, best_f1

def main():
    configs = defaultdict(list)
    for exp_id, config, label, nve in DATA:
        configs[config].append((exp_id, label, nve))

    config_names = sorted(configs.keys())
    K = len(config_names)

    print(f"Total samples: {len(DATA)}")
    print(f"Configs: {K}")
    print(f"CIVO: {sum(1 for _, _, l, _ in DATA if l == 1)}, Healthy: {sum(1 for _, _, l, _ in DATA if l == 0)}")
    print()

    for c in config_names:
        n_c = len(configs[c])
        n_pos = sum(1 for _, l, _ in configs[c] if l == 1)
        n_neg = sum(1 for _, l, _ in configs[c] if l == 0)
        print(f"  {c}: n={n_c} (pos={n_pos}, neg={n_neg})")
    print()

    results = []
    for held_out in config_names:
        test_data = configs[held_out]
        train_data = []
        for c in config_names:
            if c != held_out:
                train_data.extend(configs[c])

        train_nve = [nve for _, _, nve in train_data]
        train_labels = [l for _, l, _ in train_data]
        test_nve = [nve for _, _, nve in test_data]
        test_labels = [l for _, l, _ in test_data]

        opt_thresh, train_f1 = find_optimal_threshold(train_nve, train_labels)
        train_auroc = compute_auroc(train_labels, train_nve)

        tp, fp, tn, fn = classify(test_nve, test_labels, opt_thresh)
        test_acc = (tp + tn) / len(test_data) if len(test_data) > 0 else float('nan')
        test_f1 = f1_score(tp, fp, tn, fn)

        tp15, fp15, tn15, fn15 = classify(test_nve, test_labels, 1.5)
        test_acc_15 = (tp15 + tn15) / len(test_data) if len(test_data) > 0 else float('nan')
        test_f1_15 = f1_score(tp15, fp15, tn15, fn15)

        results.append({
            'config': held_out,
            'n_test': len(test_data),
            'n_train': len(train_data),
            'opt_threshold': opt_thresh,
            'train_f1': train_f1,
            'train_auroc': train_auroc,
            'test_acc': test_acc,
            'test_f1': test_f1,
            'test_acc_15': test_acc_15,
            'test_f1_15': test_f1_15,
            'tp': tp, 'fp': fp, 'tn': tn, 'fn': fn,
            'tp15': tp15, 'fp15': fp15, 'tn15': tn15, 'fn15': fn15,
        })

    print("=" * 120)
    print(f"{'Fold (config excluded)':<28} {'n_test':>6} {'n_train':>7} {'opt_thresh':>10} {'train_F1':>8} {'train_AUROC':>11} {'test_acc':>8} {'test_F1':>7} {'acc@1.5':>7} {'F1@1.5':>6}")
    print("-" * 120)
    for r in results:
        print(f"{r['config']:<28} {r['n_test']:>6} {r['n_train']:>7} {r['opt_threshold']:>10.3f} {r['train_f1']:>8.3f} {r['train_auroc']:>11.3f} {r['test_acc']:>8.3f} {r['test_f1']:>7.3f} {r['test_acc_15']:>7.3f} {r['test_f1_15']:>6.3f}")
    print("=" * 120)

    thresholds = [r['opt_threshold'] for r in results]
    aurocs = [r['train_auroc'] for r in results]
    test_accs = [r['test_acc'] for r in results]
    test_f1s = [r['test_f1'] for r in results]
    test_accs_15 = [r['test_acc_15'] for r in results]
    test_f1s_15 = [r['test_f1_15'] for r in results]

    print(f"\nOptimal threshold across folds: {np.mean(thresholds):.3f} ± {np.std(thresholds):.3f} (range: [{min(thresholds):.3f}, {max(thresholds):.3f}])")
    print(f"Train AUROC across folds: {np.mean(aurocs):.3f} ± {np.std(aurocs):.3f}")
    print(f"Test accuracy (opt thresh): {np.mean(test_accs):.3f} ± {np.std(test_accs):.3f}")
    print(f"Test F1 (opt thresh): {np.mean(test_f1s):.3f} ± {np.std(test_f1s):.3f}")
    print(f"Test accuracy (@1.5): {np.mean(test_accs_15):.3f} ± {np.std(test_accs_15):.3f}")
    print(f"Test F1 (@1.5): {np.mean(test_f1s_15):.3f} ± {np.std(test_f1s_15):.3f}")

    thresh_is_15 = sum(1 for t in thresholds if abs(t - 1.5) < 0.05)
    thresh_near_15 = sum(1 for t in thresholds if 1.0 <= t <= 2.0)
    print(f"\nFolds where optimal threshold ≈ 1.5 (±0.05): {thresh_is_15}/{K}")
    print(f"Folds where optimal threshold in [1.0, 2.0]: {thresh_near_15}/{K}")

    perfect_folds = sum(1 for r in results if r['test_acc_15'] == 1.0)
    print(f"Folds with perfect test accuracy at θ=1.5: {perfect_folds}/{K}")

    misclassified = []
    for r in results:
        if r['test_acc_15'] < 1.0:
            test_data = configs[r['config']]
            for exp_id, label, nve in test_data:
                pred = 1 if nve >= 1.5 else 0
                if pred != label:
                    misclassified.append((r['config'], exp_id, label, nve, pred))

    if misclassified:
        print(f"\nMisclassifications at θ=1.5:")
        for config, exp_id, label, nve, pred in misclassified:
            label_str = "CIVO" if label == 1 else "Healthy"
            pred_str = "CIVO" if pred == 1 else "Healthy"
            print(f"  Fold={config}: {exp_id} (true={label_str}, pred={pred_str}, NVE={nve:.3f})")

if __name__ == "__main__":
    main()
