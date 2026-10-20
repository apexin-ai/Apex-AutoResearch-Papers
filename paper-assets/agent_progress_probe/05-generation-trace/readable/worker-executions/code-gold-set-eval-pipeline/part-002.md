# code gold set eval pipeline — Part 2 of 2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-gold-set-eval-pipeline.md) · [Structured JSON](../../../sessions/26/266d5fbc7dd9ab6ff921.json)

## Round 1

### Tool result

_source line 167 · 2026-05-14T22:46:04.472Z_

<details><summary>↩ Tool result · `toolu_016RtuzBpQYYwBsixAZxJGYV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "3bc0d542-8d20-4765-bcd3-1be9fab26ab2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "        if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:",
    "newString": "        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if not emb_path.exists():\n                missing.append(f\"embeddings ({emb_path})\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 858,
        "oldLines": 7,
        "newStart": 858,
        "newLines": 7,
        "lines": [
          "                 break",
          " ",
          "         print(f\"\\nEvaluating: GRU Probe ...\")",
          "-        if HAS_TORCH and HAS_PROBE and emb_path.exists() and ckpt_path is not None:",
          "+        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:",
          "             emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)",
          "             embeddings = emb_data[\"embeddings\"]",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Assistant

_source line 168_

Also update the missing message for emb_path:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "b9807f0b-7c57-478f-8138-d3a354c40241",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136f2yjx2SJQvxuXnyxnsNk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 74783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 278
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 169_

<details open><summary>🔧 Tool call — Edit · `toolu_01EWFgNz38WMATBSeNqEvjS9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "            if not emb_path.exists():\n                missing.append(f\"embeddings ({emb_path})\")",
  "new_string": "            if emb_path is None:\n                missing.append(\"embeddings.pt\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "9191e364-06bf-457e-9386-cd5fa6cff85a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136f2yjx2SJQvxuXnyxnsNk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 74783,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 278
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 170 · 2026-05-14T22:46:10.181Z_

<details><summary>↩ Tool result · `toolu_01EWFgNz38WMATBSeNqEvjS9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "94cda0df-625a-4490-b15e-b1fe287f9f72",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "            if not emb_path.exists():\n                missing.append(f\"embeddings ({emb_path})\")",
    "newString": "            if emb_path is None:\n                missing.append(\"embeddings.pt\")",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if not emb_path.exists():\n                missing.append(f\"embeddings ({emb_path})\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 884,
        "oldLines": 8,
        "newStart": 884,
        "newLines": 8,
        "lines": [
          "                 missing.append(\"torch\")",
          "             if not HAS_PROBE:",
          "                 missing.append(\"probe_model\")",
          "-            if not emb_path.exists():",
          "-                missing.append(f\"embeddings ({emb_path})\")",
          "+            if emb_path is None:",
          "+                missing.append(\"embeddings.pt\")",
          "             if ckpt_path is None:",
          "                 missing.append(\"checkpoint\")",
          "             print(f\"  SKIPPED: {', '.join(missing)} not available\")"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Assistant

_source line 171_

Also fix LLM judge path resolution:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "df46c42d-7b1f-4b78-bbd0-75f86df5385b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAeHx7fgKCNcTb7vkMuht9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 75061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 258
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 172_

<details open><summary>🔧 Tool call — Edit · `toolu_01AX49sZMJJXYCJZJWXbG4Gt`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
  "old_string": "            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:",
  "new_string": "            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "0bb3b714-0839-457a-aed9-1c365cef9bbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAeHx7fgKCNcTb7vkMuht9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 75061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 258
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-14T22:46:14.841Z_

<details><summary>↩ Tool result · `toolu_01AX49sZMJJXYCJZJWXbG4Gt`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "6354fa4f-b71c-4bb2-bad5-f1d3a2ac5f7b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/src/evaluation/gold_set_eval.py",
    "oldString": "            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:",
    "newString": "            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Gold-set evaluation pipeline for agent_progress_probe.\n\nEvaluates multiple stagnation detectors against human-annotated gold labels:\n  - Structural classifiers (RF / GB / LR) trained on 30-dim hand-crafted features\n  - GRU probe (ProgressProbe) on pre-computed embeddings\n  - LLM-as-judge (from cached prediction JSONL)\n  - Silver labels (majority-vote from labeling functions)\n\nInputs:\n  --gold-file       CSV or JSONL with fields: window_id, gold_label (0/1),\n                    optional annotator_id, confidence\n  --predictions-dir Directory with model artifacts (checkpoints, embeddings,\n                    windows_labeled.jsonl, trajectories, cached LLM predictions)\n  --output-dir      Where to write results JSON and reliability diagram PDF\n\nOutputs:\n  {output-dir}/gold_set_results.json   — full metrics for every model\n  {output-dir}/gold_set_reliability.pdf — calibration curves\n\nDependencies: torch, scikit-learn, numpy, matplotlib\n\"\"\"\n\nimport argparse\nimport csv\nimport json\nimport re\nimport sys\nimport time\nimport warnings\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nfrom sklearn.calibration import calibration_curve\nfrom sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    accuracy_score,\n    cohen_kappa_score,\n    f1_score,\n    precision_score,\n    recall_score,\n)\nfrom sklearn.preprocessing import StandardScaler\n\nwarnings.filterwarnings(\"ignore\", category=UserWarning)\n\n# ---------------------------------------------------------------------------\n# Optional: torch (only needed for GRU probe)\n# ---------------------------------------------------------------------------\ntry:\n    import torch\n    import torch.nn as nn\n    from torch.utils.data import DataLoader\n\n    HAS_TORCH = True\nexcept ImportError:\n    HAS_TORCH = False\n\n# ---------------------------------------------------------------------------\n# Try importing probe model from project artifacts\n# ---------------------------------------------------------------------------\n_ARTIFACTS_DIR = Path(__file__).resolve().parent.parent.parent / \"artifacts\"\nif _ARTIFACTS_DIR.exists():\n    sys.path.insert(0, str(_ARTIFACTS_DIR))\ntry:\n    from probe_model import ProgressProbe, WindowDataset, collate_fn\n    HAS_PROBE = True\nexcept ImportError:\n    HAS_PROBE = False\n\n\n# ===========================================================================\n# Metrics\n# ===========================================================================\n\ndef compute_metrics(y_true, y_pred):\n    \"\"\"Per-model metrics: macro-F1, accuracy, per-class P/R/F1, Cohen's kappa.\"\"\"\n    return {\n        \"macro_f1\": f1_score(y_true, y_pred, average=\"macro\", zero_division=0),\n        \"accuracy\": accuracy_score(y_true, y_pred),\n        \"precision_stag\": precision_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"recall_stag\": recall_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"f1_stag\": f1_score(y_true, y_pred, pos_label=0, zero_division=0),\n        \"precision_prog\": precision_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"recall_prog\": recall_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"f1_prog\": f1_score(y_true, y_pred, pos_label=1, zero_division=0),\n        \"cohens_kappa\": cohen_kappa_score(y_true, y_pred),\n    }\n\n\n# ===========================================================================\n# Structural feature extraction (mirrors non_nlp_baseline.py)\n# ===========================================================================\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef _extract_command(text):\n    match = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return match.group(1).strip() if match else None\n\n\ndef _cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_structural_features(steps, is_short):\n    \"\"\"Extract 30-dim structural feature vector from a list of step dicts.\"\"\"\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30, dtype=np.float32)\n\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (\n            n * np.dot(x, x) - x.sum() ** 2 + 1e-9\n        )\n    else:\n        slope = 0.0\n\n    commands = []\n    for _, t in actions:\n        cmd = _extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        max_repeat = cmd_counter.most_common(1)[0][1]\n        repeat_ratio = max_repeat / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        first_word = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if first_word in EDIT_CMDS:\n            n_edit += 1\n        elif first_word in SEARCH_CMDS:\n            n_search += 1\n        elif first_word in NAV_CMDS:\n            n_nav += 1\n        elif first_word == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n\n    if n_cmds >= 2:\n        sims = [_cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run, cur_run = 1, 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = max_adj_sim = 0.0\n        max_run = 0\n\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(\n        1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower()\n    )\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1\n        for _, t in observations\n        if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n\n    return np.array(\n        [\n            n, n_actions, n_obs, n_actions / max(n, 1),\n            mean_tlen, std_tlen, max_tlen, min_tlen,\n            mean_action_len, mean_obs_len, slope,\n            n_cmds, mean_cmd_len, max_cmd_len,\n            unique_cmd_ratio, repeat_ratio,\n            n_edit, n_search, n_nav, n_submit,\n            edit_ratio, search_ratio,\n            avg_adj_sim, max_adj_sim, max_run,\n            n_errors, n_test_output, n_file_display, n_nonzero_exit,\n            float(is_short),\n        ],\n        dtype=np.float32,\n    )\n\n\n# ===========================================================================\n# Data loading helpers\n# ===========================================================================\n\ndef load_gold_labels(path):\n    \"\"\"Load gold labels from CSV or JSONL.\n\n    Returns list of dicts: [{window_id, gold_label, annotator_id?, confidence?}]\n    \"\"\"\n    path = Path(path)\n    records = []\n    if path.suffix == \".csv\":\n        with open(path) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                rec = {\n                    \"window_id\": row[\"window_id\"],\n                    \"gold_label\": int(row[\"gold_label\"]),\n                }\n                if \"annotator_id\" in row:\n                    rec[\"annotator_id\"] = row[\"annotator_id\"]\n                if \"confidence\" in row:\n                    rec[\"confidence\"] = int(row[\"confidence\"]) if row[\"confidence\"] else None\n                records.append(rec)\n    else:\n        with open(path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                rec = {\n                    \"window_id\": obj[\"window_id\"],\n                    \"gold_label\": int(obj[\"gold_label\"]),\n                }\n                if \"annotator_id\" in obj:\n                    rec[\"annotator_id\"] = obj[\"annotator_id\"]\n                if \"confidence\" in obj:\n                    rec[\"confidence\"] = obj.get(\"confidence\")\n                records.append(rec)\n    return records\n\n\ndef load_windows_jsonl(path):\n    windows = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                windows.append(json.loads(line))\n    return windows\n\n\ndef build_trajectory_index(traj_path):\n    index = {}\n    with open(traj_path) as f:\n        for row_idx, line in enumerate(f):\n            line = line.strip()\n            if not line:\n                continue\n            raw = json.loads(line)\n            steps = []\n            for s in raw.get(\"trajectory\") or []:\n                steps.append(\n                    {\n                        \"role\": s.get(\"role\", \"unknown\"),\n                        \"text\": s.get(\"text\") or s.get(\"system_prompt\") or \"\",\n                    }\n                )\n            index[row_idx] = steps\n    return index\n\n\ndef window_id_from_window(w):\n    return f\"{w['trajectory_id']}__w{w['window_idx']}\"\n\n\ndef parse_row_index(trajectory_id):\n    return int(trajectory_id.rsplit(\"__r\", 1)[1])\n\n\n# ===========================================================================\n# Model evaluators\n# ===========================================================================\n\ndef _align(gold_wids, gold_labels, prediction_map):\n    \"\"\"Align gold labels with predictions by window_id.\n\n    Returns (aligned_gold, aligned_preds, n_missing).\n    \"\"\"\n    aligned_gold, aligned_preds = [], []\n    n_missing = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        pred = prediction_map.get(wid)\n        if pred is None:\n            n_missing += 1\n            continue\n        aligned_gold.append(gl)\n        aligned_preds.append(pred)\n    return aligned_gold, aligned_preds, n_missing\n\n\ndef evaluate_silver(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Silver majority-vote labels vs gold.\"\"\"\n    pred_map = {}\n    prob_map = {}\n    conf_map = {}\n    for wid in gold_wids:\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        pred_map[wid] = w[\"majority_label\"]\n        prob_map[wid] = float(w[\"majority_label\"])\n        conf_map[wid] = w.get(\"confidence\", 0)\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, {}, {}, {}\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map, conf_map\n\n\ndef evaluate_structural_clf(\n    gold_wids,\n    gold_labels,\n    wid_to_noabs_idx,\n    all_features,\n    all_mv_labels,\n    split_info,\n    model_cls,\n    model_kwargs,\n    use_scaler=False,\n):\n    \"\"\"Train structural classifier on silver train split, predict on gold windows.\"\"\"\n    keep_indices = split_info.get(\"keep_indices\")\n    if keep_indices is not None:\n        feat_subset = all_features[keep_indices]\n        label_subset = np.array(all_mv_labels)[keep_indices]\n    else:\n        feat_subset = all_features\n        label_subset = np.array(all_mv_labels)\n\n    train_idx = split_info[\"train_indices\"]\n    X_train = feat_subset[train_idx]\n    y_train = label_subset[train_idx]\n\n    scaler = None\n    if use_scaler:\n        scaler = StandardScaler()\n        X_train = scaler.fit_transform(X_train)\n\n    clf = model_cls(**model_kwargs)\n    clf.fit(X_train, y_train)\n\n    pred_map = {}\n    prob_map = {}\n    for wid in gold_wids:\n        idx = wid_to_noabs_idx.get(wid)\n        if idx is None:\n            continue\n        feat = all_features[idx].reshape(1, -1)\n        if scaler is not None:\n            feat = scaler.transform(feat)\n        pred_map[wid] = int(clf.predict(feat)[0])\n        if hasattr(clf, \"predict_proba\"):\n            prob_map[wid] = float(clf.predict_proba(feat)[0, 1])\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\ndef evaluate_gru_probe(gold_wids, gold_labels, wid_to_emb_idx, embeddings, ckpt_path, device):\n    \"\"\"GRU probe evaluation on gold windows.\"\"\"\n    if not HAS_TORCH or not HAS_PROBE:\n        return None, 0, len(gold_wids), {}\n\n    ckpt_path = Path(ckpt_path)\n    if not ckpt_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n    ).to(device)\n    model.load_state_dict(ckpt[\"model_state_dict\"])\n    model.eval()\n\n    ordered_wids = []\n    gold_embs = []\n    valid_gold = []\n    n_miss = 0\n    for wid, gl in zip(gold_wids, gold_labels):\n        idx = wid_to_emb_idx.get(wid)\n        if idx is None:\n            n_miss += 1\n            continue\n        ordered_wids.append(wid)\n        gold_embs.append(embeddings[idx])\n        valid_gold.append(gl)\n\n    if not gold_embs:\n        return None, 0, n_miss, {}\n\n    ds = WindowDataset(gold_embs, valid_gold)\n    loader = DataLoader(ds, batch_size=64, collate_fn=collate_fn)\n\n    all_preds = []\n    all_probs = []\n    all_labels = []\n    with torch.no_grad():\n        for padded, labels, lengths in loader:\n            logits = model(padded.to(device), lengths)\n            probs = torch.sigmoid(logits).cpu()\n            preds = (probs >= 0.5).long()\n            all_preds.extend(preds.tolist())\n            all_probs.extend(probs.tolist())\n            all_labels.extend(labels.long().tolist())\n\n    prob_map = {wid: p for wid, p in zip(ordered_wids, all_probs)}\n    return compute_metrics(all_labels, all_preds), len(all_preds), n_miss, prob_map\n\n\ndef evaluate_llm_judge(gold_wids, gold_labels, predictions_path):\n    \"\"\"LLM-as-judge from cached predictions JSONL/JSON.\"\"\"\n    predictions_path = Path(predictions_path)\n    if not predictions_path.exists():\n        return None, 0, len(gold_wids), {}\n\n    pred_index = {}\n    if predictions_path.suffix == \".jsonl\":\n        with open(predictions_path) as f:\n            for line in f:\n                line = line.strip()\n                if not line:\n                    continue\n                obj = json.loads(line)\n                wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n                if obj.get(\"predicted_label\", -1) != -1:\n                    pred_index[wid] = obj\n    else:\n        with open(predictions_path) as f:\n            data = json.load(f)\n        for obj in data.get(\"results\", []):\n            wid = f\"{obj['trajectory_id']}__w{obj['window_idx']}\"\n            if obj.get(\"predicted_label\", -1) != -1:\n                pred_index[wid] = obj\n\n    pred_map = {wid: obj[\"predicted_label\"] for wid, obj in pred_index.items()}\n    prob_map = {}\n    for wid, obj in pred_index.items():\n        conf = obj.get(\"llm_confidence\", 3)\n        label = obj[\"predicted_label\"]\n        prob_map[wid] = label * (0.5 + conf / 10.0) + (1 - label) * (0.5 - conf / 10.0)\n\n    gold_al, pred_al, n_miss = _align(gold_wids, gold_labels, pred_map)\n    if not gold_al:\n        return None, 0, n_miss, prob_map\n    return compute_metrics(gold_al, pred_al), len(gold_al), n_miss, prob_map\n\n\n# ===========================================================================\n# Confidence stratification (silver label confidence vs gold agreement)\n# ===========================================================================\n\ndef confidence_stratification(gold_wids, gold_labels, wid_to_window):\n    \"\"\"Agreement between silver and gold stratified by silver confidence (1/2/3).\"\"\"\n    strata = {1: {\"agree\": 0, \"total\": 0}, 2: {\"agree\": 0, \"total\": 0}, 3: {\"agree\": 0, \"total\": 0}}\n    for wid, gl in zip(gold_wids, gold_labels):\n        w = wid_to_window.get(wid)\n        if w is None:\n            continue\n        conf = w.get(\"confidence\", 0)\n        if conf not in strata:\n            continue\n        strata[conf][\"total\"] += 1\n        if w[\"majority_label\"] == gl:\n            strata[conf][\"agree\"] += 1\n\n    result = {}\n    for conf in [1, 2, 3]:\n        total = strata[conf][\"total\"]\n        agree = strata[conf][\"agree\"]\n        result[f\"conf_{conf}\"] = {\n            \"total\": total,\n            \"agree\": agree,\n            \"agreement_rate\": agree / total if total > 0 else None,\n        }\n    return result\n\n\n# ===========================================================================\n# Reliability diagram\n# ===========================================================================\n\ndef plot_reliability_diagram(model_probs, gold_wids, gold_labels, output_path, n_bins=10):\n    \"\"\"Plot calibration curves for all models with predicted probabilities.\"\"\"\n    import matplotlib\n\n    matplotlib.use(\"Agg\")\n    import matplotlib.pyplot as plt\n\n    plt.rcParams.update(\n        {\n            \"font.family\": \"serif\",\n            \"font.size\": 10,\n            \"axes.labelsize\": 11,\n            \"axes.titlesize\": 12,\n            \"legend.fontsize\": 9,\n            \"figure.dpi\": 150,\n        }\n    )\n\n    gold_map = dict(zip(gold_wids, gold_labels))\n\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), gridspec_kw={\"width_ratios\": [2, 1]})\n\n    ax1.plot([0, 1], [0, 1], \"k--\", lw=1, label=\"Perfect calibration\")\n\n    colors = [\"#1f77b4\", \"#ff7f0e\", \"#2ca02c\", \"#d62728\", \"#9467bd\", \"#8c564b\"]\n    for i, (model_name, prob_map) in enumerate(model_probs.items()):\n        y_true, y_prob = [], []\n        for wid, prob in prob_map.items():\n            gl = gold_map.get(wid)\n            if gl is not None:\n                y_true.append(gl)\n                y_prob.append(prob)\n        if len(y_true) < 10:\n            continue\n\n        y_true = np.array(y_true)\n        y_prob = np.array(y_prob)\n\n        fraction_pos, mean_predicted = calibration_curve(\n            y_true, y_prob, n_bins=n_bins, strategy=\"uniform\"\n        )\n        ax1.plot(\n            mean_predicted, fraction_pos,\n            \"o-\", color=colors[i % len(colors)], label=model_name, markersize=4,\n        )\n\n        ax2.hist(\n            y_prob, bins=n_bins, range=(0, 1),\n            alpha=0.5, color=colors[i % len(colors)], label=model_name,\n        )\n\n    ax1.set_xlabel(\"Mean predicted probability\")\n    ax1.set_ylabel(\"Fraction of positives (progress)\")\n    ax1.set_title(\"Reliability Diagram\")\n    ax1.legend(loc=\"lower right\")\n    ax1.set_xlim(-0.02, 1.02)\n    ax1.set_ylim(-0.02, 1.02)\n    ax1.set_aspect(\"equal\")\n\n    ax2.set_xlabel(\"Predicted probability\")\n    ax2.set_ylabel(\"Count\")\n    ax2.set_title(\"Prediction Distribution\")\n    ax2.legend(loc=\"upper right\")\n\n    fig.tight_layout()\n    fig.savefig(output_path, bbox_inches=\"tight\")\n    plt.close(fig)\n\n\n# ===========================================================================\n# Console summary\n# ===========================================================================\n\ndef print_summary_table(results):\n    \"\"\"Print markdown-formatted summary to console.\"\"\"\n    header = (\n        \"| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) \"\n        \"| F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\"\n    )\n    sep = \"|\" + \"|\".join([\"---\"] * 11) + \"|\"\n    print(header)\n    print(sep)\n    for name, metrics, n, n_miss in results:\n        if metrics is None:\n            print(f\"| {name:19s} | {'—':>5s} | SKIPPED (missing={n_miss}) |{'|' * 8}\")\n            continue\n        print(\n            f\"| {name:19s} \"\n            f\"| {n:5d} \"\n            f\"| {metrics['macro_f1']:.4f}   \"\n            f\"| {metrics['accuracy']:.4f}   \"\n            f\"| {metrics['precision_stag']:.4f}  \"\n            f\"| {metrics['recall_stag']:.4f}  \"\n            f\"| {metrics['f1_stag']:.4f}   \"\n            f\"| {metrics['precision_prog']:.4f}  \"\n            f\"| {metrics['recall_prog']:.4f}  \"\n            f\"| {metrics['f1_prog']:.4f}   \"\n            f\"| {metrics['cohens_kappa']:.4f}  |\"\n        )\n\n\n# ===========================================================================\n# Main\n# ===========================================================================\n\nALL_MODELS = [\"silver\", \"rf\", \"gb\", \"lr\", \"gru_probe\", \"llm_judge\"]\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Gold-set evaluation pipeline for agent_progress_probe\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n    )\n    parser.add_argument(\n        \"--gold-file\", required=True,\n        help=\"Path to gold label file (CSV or JSONL). \"\n             \"Required fields: window_id, gold_label (0=stagnation, 1=progress). \"\n             \"Optional: annotator_id, confidence.\",\n    )\n    parser.add_argument(\n        \"--predictions-dir\", required=True,\n        help=\"Directory containing model artifacts: \"\n             \"data/windows_labeled.jsonl, data/embeddings.pt, \"\n             \"checkpoints/best_model.pt, checkpoints/split_info.json, \"\n             \"data/swe_agent_trajectories_5000.jsonl, \"\n             \"results/llm_judge_results.json\",\n    )\n    parser.add_argument(\n        \"--output-dir\", default=\"artifacts\",\n        help=\"Output directory for results JSON and reliability PDF (default: artifacts)\",\n    )\n    parser.add_argument(\n        \"--models\", nargs=\"+\", default=ALL_MODELS, choices=ALL_MODELS,\n        help=\"Which models to evaluate (default: all). \"\n             \"Choices: silver, rf, gb, lr, gru_probe, llm_judge\",\n    )\n    parser.add_argument(\"--device\", default=None, help=\"Torch device (default: auto)\")\n    parser.add_argument(\n        \"--llm-predictions\", default=None,\n        help=\"Override path to LLM-as-judge cached predictions (JSON or JSONL)\",\n    )\n    parser.add_argument(\n        \"--checkpoint\", default=None,\n        help=\"Override path to GRU probe checkpoint (default: {predictions-dir}/checkpoints/best_model.pt)\",\n    )\n    parser.add_argument(\n        \"--trajectories\", default=None,\n        help=\"Override path to raw trajectories JSONL\",\n    )\n    parser.add_argument(\"--n-bins\", type=int, default=10, help=\"Calibration curve bins\")\n    args = parser.parse_args()\n\n    t_start = time.time()\n    pdir = Path(args.predictions_dir)\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    device = args.device\n    if device is None and HAS_TORCH:\n        device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    elif device is None:\n        device = \"cpu\"\n\n    selected_models = set(args.models)\n\n    # ------------------------------------------------------------------\n    # 1. Load gold labels\n    # ------------------------------------------------------------------\n    print(f\"Loading gold labels: {args.gold_file}\")\n    gold_records = load_gold_labels(args.gold_file)\n    gold_wids = [r[\"window_id\"] for r in gold_records]\n    gold_labels = [r[\"gold_label\"] for r in gold_records]\n    gold_dist = Counter(gold_labels)\n    print(f\"  Total: {len(gold_labels)}, stag={gold_dist.get(0, 0)}, prog={gold_dist.get(1, 0)}\")\n\n    # ------------------------------------------------------------------\n    # 2. Load windows_labeled.jsonl\n    # ------------------------------------------------------------------\n    windows_path = None\n    for candidate in [\n        pdir / \"data\" / \"windows_labeled.jsonl\",\n        pdir / \"windows_labeled.jsonl\",\n        pdir / \"artifacts\" / \"data\" / \"windows_labeled.jsonl\",\n    ]:\n        if candidate.exists():\n            windows_path = candidate\n            break\n    if windows_path is None:\n        print(\"ERROR: windows_labeled.jsonl not found under predictions-dir\")\n        sys.exit(1)\n    print(f\"Loading windows: {windows_path}\")\n    all_windows = load_windows_jsonl(str(windows_path))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n    print(f\"  Total: {len(all_windows)}, non-abstain: {len(non_abstain)}\")\n\n    wid_to_window = {window_id_from_window(w): w for w in non_abstain}\n    wid_to_noabs_idx = {window_id_from_window(w): i for i, w in enumerate(non_abstain)}\n\n    # ------------------------------------------------------------------\n    # 3. Load split info\n    # ------------------------------------------------------------------\n    split_info_path = None\n    for candidate in [\n        pdir / \"checkpoints\" / \"split_info.json\",\n        pdir / \"split_info.json\",\n        pdir / \"artifacts\" / \"split_info.json\",\n    ]:\n        if candidate.exists():\n            split_info_path = candidate\n            break\n    split_info = None\n    if split_info_path is not None:\n        print(f\"Loading split info: {split_info_path}\")\n        with open(split_info_path) as f:\n            split_info = json.load(f)\n\n    # ------------------------------------------------------------------\n    # 4. Evaluate models\n    # ------------------------------------------------------------------\n    results = []\n    model_probs = {}\n\n    # --- Silver labels ---\n    if \"silver\" in selected_models:\n        print(\"\\nEvaluating: Silver (MV) Labels vs Gold ...\")\n        m, n, n_miss, prob_map, conf_map = evaluate_silver(\n            gold_wids, gold_labels, wid_to_window\n        )\n        if m:\n            print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n        results.append((\"Silver (MV)\", m, n, n_miss))\n        if prob_map:\n            model_probs[\"Silver (MV)\"] = prob_map\n\n    # --- Structural classifiers (RF, GB, LR) ---\n    need_structural = selected_models & {\"rf\", \"gb\", \"lr\"}\n    if need_structural:\n        traj_path = Path(args.trajectories) if args.trajectories else None\n        if traj_path is None:\n            for candidate in [\n                pdir / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_5000.jsonl\",\n                pdir / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n                pdir / \"artifacts\" / \"data\" / \"swe_agent_trajectories_1000.jsonl\",\n            ]:\n                if candidate.exists():\n                    traj_path = candidate\n                    break\n\n        if traj_path is not None and traj_path.exists() and split_info is not None:\n            print(f\"\\nBuilding structural features (trajectories: {traj_path}) ...\")\n            traj_index = build_trajectory_index(str(traj_path))\n            print(f\"  Indexed {len(traj_index)} trajectories\")\n\n            all_features = []\n            all_mv_labels = []\n            for w in non_abstain:\n                row_idx = w.get(\"row_index\", 0)\n                step_indices = w[\"step_indices\"]\n                traj_steps = traj_index.get(row_idx, [])\n                window_steps = []\n                for si in step_indices:\n                    if si < len(traj_steps):\n                        window_steps.append(traj_steps[si])\n                    else:\n                        window_steps.append({\"role\": \"unknown\", \"text\": \"\"})\n                feat = extract_structural_features(window_steps, w.get(\"short_trajectory\", False))\n                all_features.append(feat)\n                all_mv_labels.append(w[\"majority_label\"])\n\n            all_features = np.stack(all_features)\n            print(f\"  Feature matrix: {all_features.shape}\")\n\n            struct_configs = {\n                \"rf\": (\n                    \"Structural RF\",\n                    RandomForestClassifier,\n                    {\"n_estimators\": 200, \"max_depth\": 10, \"random_state\": 42, \"n_jobs\": -1},\n                    False,\n                ),\n                \"gb\": (\n                    \"Structural GB\",\n                    GradientBoostingClassifier,\n                    {\"n_estimators\": 200, \"learning_rate\": 0.1, \"max_depth\": 5, \"random_state\": 42},\n                    False,\n                ),\n                \"lr\": (\n                    \"Structural LR\",\n                    LogisticRegression,\n                    {\"max_iter\": 2000, \"C\": 1.0, \"solver\": \"lbfgs\"},\n                    True,\n                ),\n            }\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key not in selected_models:\n                    continue\n                name, cls, kwargs, scaler = struct_configs[key]\n                print(f\"  Evaluating {name} ...\")\n                m, n, n_miss, prob_map = evaluate_structural_clf(\n                    gold_wids, gold_labels, wid_to_noabs_idx,\n                    all_features, all_mv_labels, split_info,\n                    cls, kwargs, use_scaler=scaler,\n                )\n                if m:\n                    print(f\"    macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n                results.append((name, m, n, n_miss))\n                if prob_map:\n                    model_probs[name] = prob_map\n        else:\n            reason = \"trajectories not found\" if traj_path is None else \"split_info not found\"\n            print(f\"\\nSkipping structural classifiers: {reason}\")\n            for key in [\"rf\", \"gb\", \"lr\"]:\n                if key in selected_models:\n                    name = {\"rf\": \"Structural RF\", \"gb\": \"Structural GB\", \"lr\": \"Structural LR\"}[key]\n                    results.append((name, None, 0, len(gold_wids)))\n\n    # --- GRU Probe ---\n    if \"gru_probe\" in selected_models:\n        ckpt_path = Path(args.checkpoint) if args.checkpoint else None\n        if ckpt_path is None:\n            for candidate in [\n                pdir / \"checkpoints\" / \"best_model.pt\",\n                pdir / \"best_model.pt\",\n                pdir / \"artifacts\" / \"best_model.pt\",\n            ]:\n                if candidate.exists():\n                    ckpt_path = candidate\n                    break\n\n        emb_path = None\n        for candidate in [\n            pdir / \"data\" / \"embeddings.pt\",\n            pdir / \"embeddings.pt\",\n            pdir / \"artifacts\" / \"data\" / \"embeddings.pt\",\n        ]:\n            if candidate.exists():\n                emb_path = candidate\n                break\n\n        print(f\"\\nEvaluating: GRU Probe ...\")\n        if HAS_TORCH and HAS_PROBE and emb_path is not None and ckpt_path is not None:\n            emb_data = torch.load(emb_path, map_location=\"cpu\", weights_only=False)\n            embeddings = emb_data[\"embeddings\"]\n\n            wid_to_emb_idx = {}\n            if len(embeddings) == len(non_abstain):\n                for i, w in enumerate(non_abstain):\n                    wid_to_emb_idx[window_id_from_window(w)] = i\n            else:\n                for i in range(min(len(embeddings), len(non_abstain))):\n                    wid_to_emb_idx[window_id_from_window(non_abstain[i])] = i\n\n            m, n, n_miss, prob_map = evaluate_gru_probe(\n                gold_wids, gold_labels, wid_to_emb_idx, embeddings, str(ckpt_path), device\n            )\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"GRU Probe\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"GRU Probe\"] = prob_map\n        else:\n            missing = []\n            if not HAS_TORCH:\n                missing.append(\"torch\")\n            if not HAS_PROBE:\n                missing.append(\"probe_model\")\n            if emb_path is None:\n                missing.append(\"embeddings.pt\")\n            if ckpt_path is None:\n                missing.append(\"checkpoint\")\n            print(f\"  SKIPPED: {', '.join(missing)} not available\")\n            results.append((\"GRU Probe\", None, 0, len(gold_wids)))\n\n    # --- LLM-as-judge ---\n    if \"llm_judge\" in selected_models:\n        llm_path = Path(args.llm_predictions) if args.llm_predictions else None\n        if llm_path is None:\n            for candidate in [\n                pdir / \"results\" / \"llm_judge_results.json\",\n                pdir / \"llm_judge_results.json\",\n                pdir / \"results\" / \"llm_judge_results.jsonl\",\n            ]:\n                if candidate.exists():\n                    llm_path = candidate\n                    break\n\n        print(f\"\\nEvaluating: LLM-as-Judge ...\")\n        if llm_path is not None and llm_path.exists():\n            m, n, n_miss, prob_map = evaluate_llm_judge(gold_wids, gold_labels, llm_path)\n            if m:\n                print(f\"  macro_f1={m['macro_f1']:.4f}, kappa={m['cohens_kappa']:.4f}, n={n}\")\n            results.append((\"LLM-as-Judge\", m, n, n_miss))\n            if prob_map:\n                model_probs[\"LLM-as-Judge\"] = prob_map\n        else:\n            print(f\"  SKIPPED: no cached predictions found\")\n            results.append((\"LLM-as-Judge\", None, 0, len(gold_wids)))\n\n    # ------------------------------------------------------------------\n    # 5. Confidence stratification\n    # ------------------------------------------------------------------\n    print(\"\\nConfidence stratification (silver conf vs gold agreement):\")\n    conf_strat = confidence_stratification(gold_wids, gold_labels, wid_to_window)\n    for conf_key in [\"conf_1\", \"conf_2\", \"conf_3\"]:\n        s = conf_strat[conf_key]\n        rate = f\"{s['agreement_rate']:.4f}\" if s[\"agreement_rate\"] is not None else \"N/A\"\n        print(f\"  {conf_key}: {s['agree']}/{s['total']} = {rate}\")\n\n    # ------------------------------------------------------------------\n    # 6. Console summary\n    # ------------------------------------------------------------------\n    print(\"\\n\" + \"=\" * 120)\n    print(\"GOLD SET EVALUATION RESULTS\")\n    print(\"=\" * 120)\n    print_summary_table(results)\n\n    # ------------------------------------------------------------------\n    # 7. Reliability diagram\n    # ------------------------------------------------------------------\n    pdf_path = output_dir / \"gold_set_reliability.pdf\"\n    if model_probs:\n        try:\n            plot_reliability_diagram(\n                model_probs, gold_wids, gold_labels, str(pdf_path), n_bins=args.n_bins\n            )\n            print(f\"\\nReliability diagram: {pdf_path}\")\n        except Exception as e:\n            print(f\"\\nFailed to generate reliability diagram: {e}\")\n    else:\n        print(\"\\nNo probability estimates available; skipping reliability diagram.\")\n\n    # ------------------------------------------------------------------\n    # 8. JSON output\n    # ------------------------------------------------------------------\n    elapsed = time.time() - t_start\n    output = {\n        \"gold_file\": str(args.gold_file),\n        \"gold_distribution\": {\"total\": len(gold_labels), \"stagnation\": gold_dist.get(0, 0), \"progress\": gold_dist.get(1, 0)},\n        \"confidence_stratification\": conf_strat,\n        \"models\": {},\n        \"elapsed_seconds\": round(elapsed, 2),\n    }\n    for name, metrics, n, n_miss in results:\n        output[\"models\"][name] = {\n            \"n_evaluated\": n,\n            \"n_missing\": n_miss,\n            \"metrics\": {k: round(v, 6) for k, v in metrics.items()} if metrics else None,\n        }\n\n    json_path = output_dir / \"gold_set_results.json\"\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"Results JSON: {json_path}\")\n    print(f\"Elapsed: {elapsed:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 898,
        "oldLines": 6,
        "newStart": 898,
        "newLines": 7,
        "lines": [
          "             for candidate in [",
          "                 pdir / \"results\" / \"llm_judge_results.json\",",
          "                 pdir / \"llm_judge_results.json\",",
          "+                pdir / \"artifacts\" / \"results\" / \"llm_judge_results.json\",",
          "                 pdir / \"results\" / \"llm_judge_results.jsonl\",",
          "             ]:",
          "                 if candidate.exists():"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
````

</details>

---


### Assistant

_source line 174_

Now retry the dry-run with just `silver` model (no trajectories needed):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "85077cea-d3ed-4164-9d14-6bc1714e533c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReDdiHiBYGZmEMaujrUsv3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 75319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 356
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 175_

<details open><summary>🔧 Tool call — Bash · `toolu_01BNqiLawNnise8KefQkA32c`</summary>

```json
{
  "command": "source .venv/bin/activate && python3 src/evaluation/gold_set_eval.py --gold-file /tmp/pseudo_gold.csv --predictions-dir . --output-dir /tmp/gold_eval_test --models silver 2>&1",
  "description": "Dry-run silver-only test"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "0d30edac-9ecc-498c-b758-4de48eb85b4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReDdiHiBYGZmEMaujrUsv3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 75319,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 356
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 176_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b3iv1a9h3",
  "tool_use_id": "toolu_01BNqiLawNnise8KefQkA32c",
  "description": "Dry-run silver-only test",
  "task_type": "local_bash",
  "uuid": "239ba25a-2b75-410b-92a7-019029a8c511",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### System

_source line 177_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b3iv1a9h3",
  "tool_use_id": "toolu_01BNqiLawNnise8KefQkA32c",
  "status": "completed",
  "output_file": "",
  "summary": "Dry-run silver-only test",
  "uuid": "69e817ce-dcdc-4e67-b1ff-d7d8cdeb9db6",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0"
}
```

---


### Tool result

_source line 178 · 2026-05-14T22:46:25.644Z_

<details><summary>↩ Tool result · `toolu_01BNqiLawNnise8KefQkA32c`</summary>

```text
Loading gold labels: /tmp/pseudo_gold.csv
  Total: 200, stag=70, prog=130
Loading windows: artifacts/data/windows_labeled.jsonl
  Total: 59496, non-abstain: 54809

Evaluating: Silver (MV) Labels vs Gold ...
  macro_f1=1.0000, kappa=1.0000, n=200

Confidence stratification (silver conf vs gold agreement):
  conf_1: 0/0 = N/A
  conf_2: 187/187 = 1.0000
  conf_3: 13/13 = 1.0000

========================================================================================================================
GOLD SET EVALUATION RESULTS
========================================================================================================================
| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) | F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |
|---|---|---|---|---|---|---|---|---|---|---|
| Silver (MV)         |   200 | 1.0000   | 1.0000   | 1.0000  | 1.0000  | 1.0000   | 1.0000  | 1.0000  | 1.0000   | 1.0000  |

Reliability diagram: /tmp/gold_eval_test/gold_set_reliability.pdf
Results JSON: /tmp/gold_eval_test/gold_set_results.json
Elapsed: 2.6s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "549e5555-8edb-49dc-923d-d88e8d365e37",
  "tool_use_result": {
    "stdout": "Loading gold labels: /tmp/pseudo_gold.csv\n  Total: 200, stag=70, prog=130\nLoading windows: artifacts/data/windows_labeled.jsonl\n  Total: 59496, non-abstain: 54809\n\nEvaluating: Silver (MV) Labels vs Gold ...\n  macro_f1=1.0000, kappa=1.0000, n=200\n\nConfidence stratification (silver conf vs gold agreement):\n  conf_1: 0/0 = N/A\n  conf_2: 187/187 = 1.0000\n  conf_3: 13/13 = 1.0000\n\n========================================================================================================================\nGOLD SET EVALUATION RESULTS\n========================================================================================================================\n| Model               | N     | Macro-F1 | Accuracy | P(stag) | R(stag) | F1(stag) | P(prog) | R(prog) | F1(prog) | Cohen κ |\n|---|---|---|---|---|---|---|---|---|---|---|\n| Silver (MV)         |   200 | 1.0000   | 1.0000   | 1.0000  | 1.0000  | 1.0000   | 1.0000  | 1.0000  | 1.0000   | 1.0000  |\n\nReliability diagram: /tmp/gold_eval_test/gold_set_reliability.pdf\nResults JSON: /tmp/gold_eval_test/gold_set_results.json\nElapsed: 2.6s",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 179_

Perfect agreement expected (gold = silver in dry-run). Let me verify the output files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "57ed24e5-15b2-46fc-8189-58f8a048ceb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DRRAoFTPJSJrBENecfkqZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 532,
      "cache_read_input_tokens": 75675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 532
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 180_

<details open><summary>🔧 Tool call — Read · `toolu_01D8b1ensX67JR1eYyR1wWxL`</summary>

```json
{
  "file_path": "/tmp/gold_eval_test/gold_set_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "1244ba11-6600-4fa9-a118-0ac8cb3e41a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DRRAoFTPJSJrBENecfkqZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 532,
      "cache_read_input_tokens": 75675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 532
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-14T22:46:30.168Z_

<details><summary>↩ Tool result · `toolu_01D8b1ensX67JR1eYyR1wWxL`</summary>

```text
1	{
2	  "gold_file": "/tmp/pseudo_gold.csv",
3	  "gold_distribution": {
4	    "total": 200,
5	    "stagnation": 70,
6	    "progress": 130
7	  },
8	  "confidence_stratification": {
9	    "conf_1": {
10	      "total": 0,
11	      "agree": 0,
12	      "agreement_rate": null
13	    },
14	    "conf_2": {
15	      "total": 187,
16	      "agree": 187,
17	      "agreement_rate": 1.0
18	    },
19	    "conf_3": {
20	      "total": 13,
21	      "agree": 13,
22	      "agreement_rate": 1.0
23	    }
24	  },
25	  "models": {
26	    "Silver (MV)": {
27	      "n_evaluated": 200,
28	      "n_missing": 0,
29	      "metrics": {
30	        "macro_f1": 1.0,
31	        "accuracy": 1.0,
32	        "precision_stag": 1.0,
33	        "recall_stag": 1.0,
34	        "f1_stag": 1.0,
35	        "precision_prog": 1.0,
36	        "recall_prog": 1.0,
37	        "f1_prog": 1.0,
38	        "cohens_kappa": 1.0
39	      }
40	    }
41	  },
42	  "elapsed_seconds": 2.62
43	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "2c7d9655-caf9-49aa-9f7f-949aae494a82",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/gold_eval_test/gold_set_results.json",
      "content": "{\n  \"gold_file\": \"/tmp/pseudo_gold.csv\",\n  \"gold_distribution\": {\n    \"total\": 200,\n    \"stagnation\": 70,\n    \"progress\": 130\n  },\n  \"confidence_stratification\": {\n    \"conf_1\": {\n      \"total\": 0,\n      \"agree\": 0,\n      \"agreement_rate\": null\n    },\n    \"conf_2\": {\n      \"total\": 187,\n      \"agree\": 187,\n      \"agreement_rate\": 1.0\n    },\n    \"conf_3\": {\n      \"total\": 13,\n      \"agree\": 13,\n      \"agreement_rate\": 1.0\n    }\n  },\n  \"models\": {\n    \"Silver (MV)\": {\n      \"n_evaluated\": 200,\n      \"n_missing\": 0,\n      \"metrics\": {\n        \"macro_f1\": 1.0,\n        \"accuracy\": 1.0,\n        \"precision_stag\": 1.0,\n        \"recall_stag\": 1.0,\n        \"f1_stag\": 1.0,\n        \"precision_prog\": 1.0,\n        \"recall_prog\": 1.0,\n        \"f1_prog\": 1.0,\n        \"cohens_kappa\": 1.0\n      }\n    }\n  },\n  \"elapsed_seconds\": 2.62\n}",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---


### Tool call

_source line 182_

<details open><summary>🔧 Tool call — Bash · `toolu_01CYbh3TTqMeszHckNnA8LU4`</summary>

```json
{
  "command": "ls -la /tmp/gold_eval_test/",
  "description": "Check output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "bf2df2de-240c-4cd2-970d-125c5e220b48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011DRRAoFTPJSJrBENecfkqZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 532,
      "cache_read_input_tokens": 75675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 532
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-14T22:46:30.611Z_

<details><summary>↩ Tool result · `toolu_01CYbh3TTqMeszHckNnA8LU4`</summary>

```text
total 24
drwxr-xr-x  2 ubuntu ubuntu    80 May 14 22:46 .
drwxrwxrwt 21 root   root     740 May 14 22:46 ..
-rw-r--r--  1 ubuntu ubuntu 16958 May 14 22:46 gold_set_reliability.pdf
-rw-r--r--  1 ubuntu ubuntu   828 May 14 22:46 gold_set_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "f2a3ac40-4941-4952-9b31-e29f69d46fb4",
  "tool_use_result": {
    "stdout": "total 24\ndrwxr-xr-x  2 ubuntu ubuntu    80 May 14 22:46 .\ndrwxrwxrwt 21 root   root     740 May 14 22:46 ..\n-rw-r--r--  1 ubuntu ubuntu 16958 May 14 22:46 gold_set_reliability.pdf\n-rw-r--r--  1 ubuntu ubuntu   828 May 14 22:46 gold_set_results.json",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 184_

Pipeline 端到端验证通过。三个产出全部生成：
- `gold_set_results.json` — 完整指标 JSON
- `gold_set_reliability.pdf` — 校准曲线图
- Console markdown 表格

**文件**: `src/evaluation/gold_set_eval.py`

**已实现功能**:
1. 加载 CSV/JSONL gold 标注（支持 `annotator_id`, `confidence` 可选字段）
2. 六个评估对象：Silver MV、RF、GB、LR、GRU Probe、LLM-as-Judge
3. 按 `window_id` 对齐，报告未匹配数量
4. 指标：macro-F1、accuracy、per-class P/R/F1、Cohen's κ
5. 按 silver confidence (1/2/3) 分层统计 gold-silver agreement
6. Reliability diagram (calibration curve + prediction distribution)
7. `--models` 选择器可单独跑某些模型
8. 路径自动探测，兼容 `artifacts/data/`、`data/`、`checkpoints/` 等多种目录布局

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "uuid": "1b29727c-f73c-441c-9f99-6fcdc39f60d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LcTrkjytL4UxYeC3E4wbqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 76207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 877
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 185_

Pipeline 端到端验证通过。三个产出全部生成：
- `gold_set_results.json` — 完整指标 JSON
- `gold_set_reliability.pdf` — 校准曲线图
- Console markdown 表格

**文件**: `src/evaluation/gold_set_eval.py`

**已实现功能**:
1. 加载 CSV/JSONL gold 标注（支持 `annotator_id`, `confidence` 可选字段）
2. 六个评估对象：Silver MV、RF、GB、LR、GRU Probe、LLM-as-Judge
3. 按 `window_id` 对齐，报告未匹配数量
4. 指标：macro-F1、accuracy、per-class P/R/F1、Cohen's κ
5. 按 silver confidence (1/2/3) 分层统计 gold-silver agreement
6. Reliability diagram (calibration curve + prediction distribution)
7. `--models` 选择器可单独跑某些模型
8. 路径自动探测，兼容 `artifacts/data/`、`data/`、`checkpoints/` 等多种目录布局

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 395469,
  "duration_api_ms": 358776,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "8ef45f83-2af7-4abc-8b9d-cfa9ae51dde0",
  "total_cost_usd": 1.9083139499999995,
  "usage": {
    "input_tokens": 26,
    "cache_creation_input_tokens": 65243,
    "cache_read_input_tokens": 1521943,
    "output_tokens": 16507,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 65243,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 315,
        "cache_read_input_tokens": 76207,
        "cache_creation_input_tokens": 877,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 877
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1665,
      "outputTokens": 8291,
      "cacheReadInputTokens": 1753237,
      "cacheCreationInputTokens": 86660,
      "webSearchRequests": 0,
      "costUSD": 0.3267687,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 26,
      "outputTokens": 16507,
      "cacheReadInputTokens": 1521943,
      "cacheCreationInputTokens": 65243,
      "webSearchRequests": 0,
      "costUSD": 1.5815452499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5b277b25-3300-4972-9f6c-8814c00cbc25"
}
```

</details>

---
