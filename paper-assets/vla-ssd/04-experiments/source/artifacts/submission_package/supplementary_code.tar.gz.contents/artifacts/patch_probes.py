"""Patch train_probes.py and analyze_goal_probes.py to add trajectory-level accuracy."""
# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---

import sys

# ===================== Patch train_probes.py =====================
with open(f"{PROJECT_ROOT}/scripts/train_probes.py", 'r') as f:
    content = f.read()

patches_applied = 0

# --- Patch 1: train_goal_classification_probe — return val_preds ---
old1 = """    return dict(
        accuracy=acc,
        macro_f1=macro_f1,
        per_class_accuracy={str(k): v for k, v in per_class_acc.items()},
        confusion_matrix=cm.tolist(),
        epochs_trained=final_ep,
    )


# ============================================================
# Runners"""

new1 = """    return dict(
        accuracy=acc,
        macro_f1=macro_f1,
        per_class_accuracy={str(k): v for k, v in per_class_acc.items()},
        confusion_matrix=cm.tolist(),
        epochs_trained=final_ep,
        val_preds=preds,
    )


# ============================================================
# Runners"""

if old1 in content:
    content = content.replace(old1, new1)
    patches_applied += 1
    print("Patch 1 applied: val_preds added to return dict")
else:
    print("ERROR: Patch 1 failed — old text not found", file=sys.stderr)

# --- Patch 2: flatten function — add traj_ids tracking ---
old2 = '''        # Flatten: each timestep is one sample, label = task index
        def flatten(feats, ids):
            Xs, Ys = [], []
            for feat, idx in zip(feats, ids):
                label = task_to_idx[traj_metas[idx]["task"]]
                T = feat.shape[0]
                Xs.append(torch.from_numpy(feat))
                Ys.append(torch.full((T,), label, dtype=torch.long))
            return torch.cat(Xs), torch.cat(Ys)

        X_tr, y_tr = flatten(train_feats, train_ids)
        X_val, y_val = flatten(val_feats, val_ids)
        del train_feats, val_feats'''

new2 = '''        # Flatten: each timestep is one sample, label = task index
        def flatten(feats, ids, return_traj_ids=False):
            Xs, Ys, Ts = [], [], []
            for feat, idx in zip(feats, ids):
                label = task_to_idx[traj_metas[idx]["task"]]
                T = feat.shape[0]
                Xs.append(torch.from_numpy(feat))
                Ys.append(torch.full((T,), label, dtype=torch.long))
                if return_traj_ids:
                    Ts.append(torch.full((T,), idx, dtype=torch.long))
            if return_traj_ids:
                return torch.cat(Xs), torch.cat(Ys), torch.cat(Ts)
            return torch.cat(Xs), torch.cat(Ys)

        X_tr, y_tr = flatten(train_feats, train_ids)
        X_val, y_val, val_traj_ids = flatten(val_feats, val_ids, return_traj_ids=True)
        del train_feats, val_feats'''

if old2 in content:
    content = content.replace(old2, new2)
    patches_applied += 1
    print("Patch 2 applied: flatten returns traj_ids for val")
else:
    print("ERROR: Patch 2 failed — old text not found", file=sys.stderr)

# --- Patch 3: After probe training, compute traj-level accuracy ---
old3 = '''        met = train_goal_classification_probe(
            X_tr, y_tr, X_val, y_val, probe_dim, n_classes, args, device
        )
        met["layer"] = layer'''

new3 = '''        met = train_goal_classification_probe(
            X_tr, y_tr, X_val, y_val, probe_dim, n_classes, args, device
        )
        val_preds = met.pop("val_preds")
        val_traj_np = val_traj_ids.numpy()
        val_y_np = y_val.cpu().numpy()
        traj_correct, traj_total = 0, 0
        for tidx in np.unique(val_traj_np):
            mask = val_traj_np == tidx
            majority_pred = np.bincount(val_preds[mask], minlength=n_classes).argmax()
            traj_correct += int(majority_pred == val_y_np[mask][0])
            traj_total += 1
        met["traj_accuracy"] = traj_correct / traj_total if traj_total > 0 else 0.0
        met["layer"] = layer'''

if old3 in content:
    content = content.replace(old3, new3)
    patches_applied += 1
    print("Patch 3 applied: traj-level majority vote accuracy")
else:
    print("ERROR: Patch 3 failed — old text not found", file=sys.stderr)

# --- Patch 4: Update print to include traj_accuracy ---
old4 = '''        print(f"  acc={met['accuracy']:.4f}  F1={met['macro_f1']:.4f}  "
              f"ep={met['epochs_trained']}  {time.time()-t0:.1f}s")

    return results


# ============================================================
# Results I/O
# ============================================================'''

new4 = '''        print(f"  acc={met['accuracy']:.4f}  traj_acc={met['traj_accuracy']:.4f}  "
              f"F1={met['macro_f1']:.4f}  ep={met['epochs_trained']}  {time.time()-t0:.1f}s")

    return results


# ============================================================
# Results I/O
# ============================================================'''

if old4 in content:
    content = content.replace(old4, new4)
    patches_applied += 1
    print("Patch 4 applied: print includes traj_accuracy")
else:
    print("ERROR: Patch 4 failed — old text not found", file=sys.stderr)

# --- Patch 5: save_results — CSV fields ---
old5 = '''    elif probe_type == "goal_classification":
        fields = ["layer", "accuracy", "macro_f1", "epochs_trained"]'''

new5 = '''    elif probe_type == "goal_classification":
        fields = ["layer", "accuracy", "traj_accuracy", "macro_f1", "epochs_trained"]'''

if old5 in content:
    content = content.replace(old5, new5)
    patches_applied += 1
    print("Patch 5 applied: CSV fields include traj_accuracy")
else:
    print("ERROR: Patch 5 failed — old text not found", file=sys.stderr)

# --- Patch 6: save_results — summary JSON ---
old6 = '''    if probe_type == "goal_classification" and results:
        best = max(results, key=lambda k: results[k]["accuracy"])
        summary["best_layer"] = best
        summary["best_accuracy"] = results[best]["accuracy"]
        summary["best_macro_f1"] = results[best]["macro_f1"]
        # Per-layer accuracy curve
        summary["accuracy_by_layer"] = {
            str(k): results[k]["accuracy"] for k in sorted(results.keys())
        }'''

new6 = '''    if probe_type == "goal_classification" and results:
        best = max(results, key=lambda k: results[k]["accuracy"])
        summary["best_layer"] = best
        summary["best_accuracy"] = results[best]["accuracy"]
        summary["best_macro_f1"] = results[best]["macro_f1"]
        summary["best_traj_accuracy"] = max(
            results[k].get("traj_accuracy", 0) for k in results
        )
        # Per-layer accuracy curve
        summary["accuracy_by_layer"] = {
            str(k): results[k]["accuracy"] for k in sorted(results.keys())
        }
        summary["traj_accuracy_by_layer"] = {
            str(k): results[k].get("traj_accuracy") for k in sorted(results.keys())
        }'''

if old6 in content:
    content = content.replace(old6, new6)
    patches_applied += 1
    print("Patch 6 applied: summary JSON includes traj_accuracy fields")
else:
    print("ERROR: Patch 6 failed — old text not found", file=sys.stderr)

with open(f"{PROJECT_ROOT}/scripts/train_probes.py", 'w') as f:
    f.write(content)

print(f"\ntrain_probes.py: {patches_applied}/6 patches applied")

# ===================== Patch analyze_goal_probes.py =====================
with open(f"{PROJECT_ROOT}/scripts/analyze_goal_probes.py", 'r') as f:
    content2 = f.read()

patches2 = 0

# --- Patch A: Add traj_accuracy helper ---
old_a = '''    def get_acc(summary, layer_key):
        abl = summary.get("accuracy_by_layer", {})
        if layer_key in abl:
            return abl[layer_key]
        res = summary.get("results", {})
        if layer_key in res:
            return res[layer_key].get("accuracy")
        return None'''

new_a = '''    def get_acc(summary, layer_key):
        abl = summary.get("accuracy_by_layer", {})
        if layer_key in abl:
            return abl[layer_key]
        res = summary.get("results", {})
        if layer_key in res:
            return res[layer_key].get("accuracy")
        return None

    def get_traj_acc(summary, layer_key):
        tabl = summary.get("traj_accuracy_by_layer", {})
        if layer_key in tabl:
            return tabl[layer_key]
        res = summary.get("results", {})
        if layer_key in res:
            return res[layer_key].get("traj_accuracy")
        return None'''

if old_a in content2:
    content2 = content2.replace(old_a, new_a)
    patches2 += 1
    print("\nPatch A applied: get_traj_acc helper added")
else:
    print("\nERROR: Patch A failed", file=sys.stderr)

# --- Patch B: Table header + rows include traj_accuracy ---
old_b = '''    header = f"{'Layer':>6}" + "".join(f"  {n:>12}" for n in model_names)
    print(header)
    print("-" * len(header))
    for layer in sorted_layers:
        row = f"{layer:>6}"
        for name in model_names:
            acc = get_acc(summaries[name], layer)
            if acc is not None:
                row += f"  {acc:>11.4f}"
            else:
                row += f"  {'—':>11}"
        print(row)'''

new_b = '''    # Build column headers: acc and traj_acc per model
    col_headers = []
    for n in model_names:
        col_headers.append(f"{n}_acc")
        col_headers.append(f"{n}_traj")
    header = f"{'Layer':>6}" + "".join(f"  {h:>12}" for h in col_headers)
    print(header)
    print("-" * len(header))
    for layer in sorted_layers:
        row = f"{layer:>6}"
        for name in model_names:
            acc = get_acc(summaries[name], layer)
            if acc is not None:
                row += f"  {acc:>11.4f}"
            else:
                row += f"  {'—':>11}"
            tacc = get_traj_acc(summaries[name], layer)
            if tacc is not None:
                row += f"  {tacc:>11.4f}"
            else:
                row += f"  {'—':>11}"
        print(row)'''

if old_b in content2:
    content2 = content2.replace(old_b, new_b)
    patches2 += 1
    print("Patch B applied: table includes traj_accuracy columns")
else:
    print("ERROR: Patch B failed", file=sys.stderr)

# --- Patch C: Best layer summary includes traj_accuracy ---
old_c = '''    for name in model_names:
        s = summaries[name]
        best_layer = s.get("best_layer", "?")
        best_acc = s.get("best_accuracy", 0)
        best_f1 = s.get("best_macro_f1", 0)
        print(f"  {name:>10}: layer {best_layer}  acc={best_acc:.4f}  F1={best_f1:.4f}")'''

new_c = '''    for name in model_names:
        s = summaries[name]
        best_layer = s.get("best_layer", "?")
        best_acc = s.get("best_accuracy", 0)
        best_f1 = s.get("best_macro_f1", 0)
        best_tacc = s.get("best_traj_accuracy", 0) or 0
        print(f"  {name:>10}: layer {best_layer}  acc={best_acc:.4f}  traj_acc={best_tacc:.4f}  F1={best_f1:.4f}")'''

if old_c in content2:
    content2 = content2.replace(old_c, new_c)
    patches2 += 1
    print("Patch C applied: best summary includes traj_accuracy")
else:
    print("ERROR: Patch C failed", file=sys.stderr)

# --- Patch D: Gate judgment uses traj_accuracy too ---
old_d = '''    trained_acc = summaries.get("trained", {}).get("best_accuracy", 0)
    dino_acc = summaries.get("dinov2", {}).get("best_accuracy", 0) if "dinov2" in summaries else 0
    gap = trained_acc - dino_acc

    print(f"  Trained best accuracy:  {trained_acc:.4f}")
    print(f"  DINO best accuracy:     {dino_acc:.4f}")
    print(f"  Gap:                    {gap:.4f}")
    print(f"  Threshold:              acc > {args.acc_gate:.2f} AND gap > {args.gap_gate:.2f}")'''

new_d = '''    trained_acc = summaries.get("trained", {}).get("best_accuracy", 0)
    trained_tacc = summaries.get("trained", {}).get("best_traj_accuracy", 0) or 0
    dino_acc = summaries.get("dinov2", {}).get("best_accuracy", 0) if "dinov2" in summaries else 0
    dino_tacc = (summaries.get("dinov2", {}).get("best_traj_accuracy", 0) or 0) if "dinov2" in summaries else 0
    gap = trained_acc - dino_acc
    traj_gap = trained_tacc - dino_tacc

    print(f"  Trained best accuracy:       {trained_acc:.4f}")
    print(f"  Trained best traj_accuracy:  {trained_tacc:.4f}")
    print(f"  DINO best accuracy:          {dino_acc:.4f}")
    print(f"  DINO best traj_accuracy:     {dino_tacc:.4f}")
    print(f"  Gap (per-frame):             {gap:.4f}")
    print(f"  Gap (trajectory):            {traj_gap:.4f}")
    print(f"  Threshold:                   acc > {args.acc_gate:.2f} AND gap > {args.gap_gate:.2f}")'''

if old_d in content2:
    content2 = content2.replace(old_d, new_d)
    patches2 += 1
    print("Patch D applied: gate judgment shows traj_accuracy")
else:
    print("ERROR: Patch D failed", file=sys.stderr)

with open(f"{PROJECT_ROOT}/scripts/analyze_goal_probes.py", 'w') as f:
    f.write(content2)

print(f"\nanalyze_goal_probes.py: {patches2}/4 patches applied")

if patches_applied < 6 or patches2 < 4:
    sys.exit(1)
print("\nAll patches applied successfully.")
