# exp plan 015 wild data design — Part 2 of 2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../exp-plan-015-wild-data-design.md) · [Structured JSON](../../../sessions/16/1672294bb29e3515ff99.json)

## Round 2

### Tool result

_source line 287 · 2026-05-15T19:48:03.543Z_

<details><summary>↩ Tool result · `toolu_01PUJ73hMY1Knd3APvUos8jF`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/src/wild_data_calibration.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "9c2f45b3-08a8-46e3-a4e3-dde6adee7be8",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/src/wild_data_calibration.py",
    "content": "\"\"\"\nWild-data calibration experiment (plan_015).\n\nValidates RF classifier calibration on real-world web text (RedPajama)\nto test external validity of depth classification findings.\n\nThree tests:\n  A. d0 False Positive Rate: wild text should be classified as d0\n  B. Mixed-domain 4-class accuracy: wild d0 + controlled d1-d3\n  C. Feature distribution shift: KS test + MMD between wild d0 and controlled d0\n\nUsage:\n  python src/wild_data_calibration.py --mode download --n_samples 10000\n  python src/wild_data_calibration.py --mode extract --gpu 0\n  python src/wild_data_calibration.py --mode evaluate --controlled_features_dir results/pythia_nucleus095/\n  python src/wild_data_calibration.py --mode all --gpu 0 --controlled_features_dir results/pythia_nucleus095/\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport sys\nimport numpy as np\nfrom collections import Counter\nfrom scipy.stats import skew, kurtosis, entropy, ks_2samp\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n\nFEATURE_NAMES = [\n    \"mean_ppl\", \"var_ppl\", \"skewness_ppl\", \"kurtosis_ppl\",\n    \"p10_ppl\", \"p25_ppl\", \"p50_ppl\", \"p75_ppl\", \"p90_ppl\",\n    \"mean_surprisal\", \"var_surprisal\", \"entropy_of_surprisal\",\n    \"type_token_ratio\", \"hapax_ratio\", \"bigram_entropy\", \"trigram_entropy\",\n    \"rep_2gram\", \"rep_3gram\", \"rep_4gram\",\n]\nNUM_FEATURES = len(FEATURE_NAMES)\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Wild-data calibration for depth classifier (plan_015)\")\n    p.add_argument(\"--mode\", choices=[\"download\", \"extract\", \"evaluate\", \"all\"], default=\"all\")\n    p.add_argument(\"--data_source\", choices=[\"redpajama\", \"dolma\"], default=\"redpajama\")\n    p.add_argument(\"--n_samples\", type=int, default=10000)\n    p.add_argument(\"--min_tokens\", type=int, default=512)\n    p.add_argument(\"--truncate_tokens\", type=int, default=512)\n    p.add_argument(\"--reference_model\", default=\"gpt2\",\n                   help=\"Reference LM for perplexity/surprisal features\")\n    p.add_argument(\"--gpu\", type=int, default=0)\n    p.add_argument(\"--batch_size\", type=int, default=32)\n    p.add_argument(\"--wild_data_dir\", default=\"data/wild_calibration\")\n    p.add_argument(\"--controlled_features_dir\", nargs=\"+\",\n                   default=[\"data/features\"],\n                   help=\"Directories containing per-cell feature JSONL files\")\n    p.add_argument(\"--output_dir\", default=\"results/wild_calibration\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    return p.parse_args()\n\n\n# ── Data Download ──\n\ndef download_redpajama(output_path, n_samples, min_tokens, tokenizer, seed=42):\n    from datasets import load_dataset\n\n    print(f\"Loading RedPajama-Data-1T-Sample (streaming)...\")\n    ds = load_dataset(\n        \"togethercomputer/RedPajama-Data-1T-Sample\",\n        split=\"train\",\n        streaming=True,\n    )\n\n    rng = np.random.RandomState(seed)\n    collected = []\n    skipped_short = 0\n    skipped_wiki = 0\n\n    for example in ds:\n        meta = example.get(\"meta\", \"{}\")\n        if isinstance(meta, str):\n            try:\n                meta = json.loads(meta)\n            except (json.JSONDecodeError, TypeError):\n                meta = {}\n        source = meta.get(\"redpajama_set_name\", \"\")\n        if \"wikipedia\" in source.lower():\n            skipped_wiki += 1\n            continue\n\n        text = example.get(\"text\", \"\")\n        if not text or len(text) < 100:\n            continue\n        tokens = tokenizer.encode(text, add_special_tokens=False)\n        if len(tokens) < min_tokens:\n            skipped_short += 1\n            continue\n\n        tokens_trunc = tokens[:min_tokens]\n        text_truncated = tokenizer.decode(tokens_trunc)\n\n        collected.append({\n            \"text\": text_truncated,\n            \"depth\": 0,\n            \"source\": \"redpajama\",\n            \"token_count\": len(tokens_trunc),\n            \"original_source\": source,\n        })\n\n        if len(collected) >= n_samples * 2:\n            break\n\n        if len(collected) % 5000 == 0 and len(collected) > 0:\n            print(f\"  Collected {len(collected)} candidates \"\n                  f\"(skipped: {skipped_short} short, {skipped_wiki} wiki)...\")\n\n    if len(collected) > n_samples:\n        idx = rng.choice(len(collected), n_samples, replace=False)\n        collected = [collected[i] for i in sorted(idx)]\n\n    os.makedirs(os.path.dirname(output_path), exist_ok=True)\n    with open(output_path, \"w\") as f:\n        for rec in collected:\n            f.write(json.dumps(rec, ensure_ascii=False) + \"\\n\")\n\n    source_dist = Counter(r[\"original_source\"] for r in collected)\n    print(f\"Saved {len(collected)} samples to {output_path}\")\n    print(f\"Source distribution: {dict(source_dist)}\")\n    return collected\n\n\ndef download_dolma(output_path, n_samples, min_tokens, tokenizer, seed=42):\n    from datasets import load_dataset\n\n    print(\"Loading Dolma v1.7 sample (streaming)...\")\n    ds = load_dataset(\n        \"allenai/dolma\",\n        name=\"v1_7-sample\",\n        split=\"train\",\n        streaming=True,\n    )\n\n    collected = []\n    skipped = 0\n\n    for example in ds:\n        text = example.get(\"text\", \"\")\n        if not text or len(text) < 100:\n            continue\n        tokens = tokenizer.encode(text, add_special_tokens=False)\n        if len(tokens) < min_tokens:\n            skipped += 1\n            continue\n\n        tokens_trunc = tokens[:min_tokens]\n        text_truncated = tokenizer.decode(tokens_trunc)\n\n        collected.append({\n            \"text\": text_truncated,\n            \"depth\": 0,\n            \"source\": \"dolma\",\n            \"token_count\": len(tokens_trunc),\n        })\n\n        if len(collected) >= n_samples:\n            break\n\n    os.makedirs(os.path.dirname(output_path), exist_ok=True)\n    with open(output_path, \"w\") as f:\n        for rec in collected:\n            f.write(json.dumps(rec, ensure_ascii=False) + \"\\n\")\n\n    print(f\"Saved {len(collected)} samples to {output_path}\")\n    return collected\n\n\n# ── Feature Extraction ──\n\ndef compute_repetition_rates(token_ids):\n    def _rep_rate(ids, n):\n        if len(ids) < n:\n            return 0.0\n        ngrams = [tuple(ids[i:i+n]) for i in range(len(ids) - n + 1)]\n        if not ngrams:\n            return 0.0\n        counts = Counter(ngrams)\n        repeated = sum(c - 1 for c in counts.values() if c > 1)\n        return repeated / len(ngrams)\n\n    return _rep_rate(token_ids, 2), _rep_rate(token_ids, 3), _rep_rate(token_ids, 4)\n\n\ndef compute_lexical_features(token_ids):\n    total = len(token_ids)\n    if total == 0:\n        return 0.0, 0.0, 0.0, 0.0\n\n    counts = Counter(token_ids)\n    unique = len(counts)\n    ttr = unique / total\n    hapax = sum(1 for c in counts.values() if c == 1)\n    hapax_ratio = hapax / unique if unique > 0 else 0.0\n\n    bigrams = [tuple(token_ids[i:i+2]) for i in range(len(token_ids) - 1)]\n    if bigrams:\n        bg_counts = Counter(bigrams)\n        bg_freq = np.array(list(bg_counts.values()), dtype=np.float64)\n        bg_freq /= bg_freq.sum()\n        bg_ent = float(entropy(bg_freq))\n    else:\n        bg_ent = 0.0\n\n    trigrams = [tuple(token_ids[i:i+3]) for i in range(len(token_ids) - 2)]\n    if trigrams:\n        tg_counts = Counter(trigrams)\n        tg_freq = np.array(list(tg_counts.values()), dtype=np.float64)\n        tg_freq /= tg_freq.sum()\n        tg_ent = float(entropy(tg_freq))\n    else:\n        tg_ent = 0.0\n\n    return ttr, hapax_ratio, bg_ent, tg_ent\n\n\ndef surprisal_entropy_hist(surprisals, n_bins=50):\n    if len(surprisals) < 2:\n        return 0.0\n    hist, _ = np.histogram(surprisals, bins=n_bins, density=True)\n    hist = hist[hist > 0]\n    if len(hist) == 0:\n        return 0.0\n    hist = hist / hist.sum()\n    return float(entropy(hist))\n\n\ndef extract_features_batch(model, tokenizer, texts, trunc_len, device):\n    import torch\n\n    encoded = [tokenizer.encode(t, add_special_tokens=False)[:trunc_len] for t in texts]\n    max_len = max(len(e) for e in encoded)\n    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id\n\n    input_ids_list, attn_mask_list = [], []\n    for e in encoded:\n        pad_len = max_len - len(e)\n        input_ids_list.append(e + [pad_id] * pad_len)\n        attn_mask_list.append([1] * len(e) + [0] * pad_len)\n\n    input_ids_t = torch.tensor(input_ids_list, dtype=torch.long, device=device)\n    attn_mask_t = torch.tensor(attn_mask_list, dtype=torch.long, device=device)\n\n    with torch.no_grad():\n        logits = model(input_ids=input_ids_t, attention_mask=attn_mask_t).logits\n\n    shift_logits = logits[:, :-1, :].contiguous()\n    shift_labels = input_ids_t[:, 1:].contiguous()\n    loss_fn = torch.nn.CrossEntropyLoss(reduction=\"none\")\n    per_token_loss = loss_fn(\n        shift_logits.view(-1, shift_logits.size(-1)),\n        shift_labels.view(-1),\n    ).view(shift_logits.size(0), shift_logits.size(1))\n\n    results = []\n    for i in range(len(texts)):\n        seq_len = len(encoded[i])\n        if seq_len <= 1:\n            surprisals = np.array([0.0])\n        else:\n            surprisals = per_token_loss[i, :seq_len - 1].cpu().numpy().astype(np.float64)\n\n        ppl_per_token = np.exp(np.clip(surprisals, 0, 20))\n\n        ttr, hapax_r, bg_ent, tg_ent = compute_lexical_features(encoded[i])\n        rep2, rep3, rep4 = compute_repetition_rates(encoded[i])\n\n        results.append({\n            \"mean_ppl\": float(np.mean(ppl_per_token)),\n            \"var_ppl\": float(np.var(ppl_per_token)),\n            \"skewness_ppl\": float(skew(ppl_per_token)) if len(ppl_per_token) > 2 else 0.0,\n            \"kurtosis_ppl\": float(kurtosis(ppl_per_token)) if len(ppl_per_token) > 3 else 0.0,\n            \"p10_ppl\": float(np.percentile(ppl_per_token, 10)),\n            \"p25_ppl\": float(np.percentile(ppl_per_token, 25)),\n            \"p50_ppl\": float(np.percentile(ppl_per_token, 50)),\n            \"p75_ppl\": float(np.percentile(ppl_per_token, 75)),\n            \"p90_ppl\": float(np.percentile(ppl_per_token, 90)),\n            \"mean_surprisal\": float(np.mean(surprisals)),\n            \"var_surprisal\": float(np.var(surprisals)),\n            \"entropy_of_surprisal\": surprisal_entropy_hist(surprisals),\n            \"type_token_ratio\": ttr,\n            \"hapax_ratio\": hapax_r,\n            \"bigram_entropy\": bg_ent,\n            \"trigram_entropy\": tg_ent,\n            \"rep_2gram\": rep2,\n            \"rep_3gram\": rep3,\n            \"rep_4gram\": rep4,\n            \"depth\": 0,\n        })\n    return results\n\n\ndef run_feature_extraction(args):\n    import torch\n    from transformers import AutoTokenizer, AutoModelForCausalLM\n\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    print(f\"Device: {device}\")\n\n    wild_path = os.path.join(args.wild_data_dir, \"wild_d0.jsonl\")\n    records = []\n    with open(wild_path) as f:\n        for line in f:\n            if line.strip():\n                records.append(json.loads(line))\n    print(f\"Loaded {len(records)} wild samples\")\n\n    print(f\"Loading reference model: {args.reference_model}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.reference_model)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n    model = AutoModelForCausalLM.from_pretrained(\n        args.reference_model, torch_dtype=torch.float16,\n    ).to(device)\n    model.eval()\n\n    texts = [r[\"text\"] for r in records]\n    all_features = []\n    bs = args.batch_size\n\n    for start in range(0, len(texts), bs):\n        end = min(start + bs, len(texts))\n        batch_feats = extract_features_batch(\n            model, tokenizer, texts[start:end], args.truncate_tokens, device,\n        )\n        all_features.extend(batch_feats)\n        if (start // bs) % 50 == 0 or end == len(texts):\n            print(f\"  Extracted features: {end}/{len(texts)}\")\n\n    output_path = os.path.join(args.wild_data_dir, \"wild_d0_features.jsonl\")\n    os.makedirs(os.path.dirname(output_path), exist_ok=True)\n    with open(output_path, \"w\") as f:\n        for feat in all_features:\n            f.write(json.dumps(feat) + \"\\n\")\n    print(f\"Features saved to {output_path} ({len(all_features)} samples)\")\n    return all_features\n\n\n# ── Feature Loading ──\n\ndef load_features(path):\n    records = []\n    with open(path) as f:\n        for line in f:\n            if line.strip():\n                records.append(json.loads(line))\n    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)\n    y = np.array([r[\"depth\"] for r in records], dtype=np.int64)\n    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)\n    return X, y\n\n\ndef find_feature_files(dirs):\n    found = {}\n    for d in dirs:\n        if not os.path.isdir(d):\n            if os.path.isfile(d) and d.endswith(\".jsonl\"):\n                name = os.path.splitext(os.path.basename(d))[0]\n                found[name] = d\n            continue\n        for root, _, files in os.walk(d):\n            for f in files:\n                if f.endswith(\".jsonl\") and \"feature\" in f.lower():\n                    cell = os.path.basename(root)\n                    if cell in (\".\", \"data\", \"features\"):\n                        cell = os.path.splitext(f)[0]\n                    found[cell] = os.path.join(root, f)\n    return found\n\n\n# ── Test A: d0 False Positive Rate ──\n\ndef test_a_d0_fpr(wild_X, ctrl_X, ctrl_y, output_dir, seed=42):\n    print(\"\\n\" + \"=\" * 60)\n    print(\"TEST A: d0 False Positive Rate on Wild Data\")\n    print(\"=\" * 60)\n\n    scaler = StandardScaler()\n    X_train = scaler.fit_transform(ctrl_X)\n    rf = RandomForestClassifier(n_estimators=100, random_state=seed, n_jobs=-1)\n    rf.fit(X_train, ctrl_y)\n\n    X_wild = scaler.transform(wild_X)\n    y_pred = rf.predict(X_wild)\n    y_prob = rf.predict_proba(X_wild)\n\n    pred_dist = Counter(int(x) for x in y_pred)\n    n_total = len(y_pred)\n    d0_rate = pred_dist.get(0, 0) / n_total\n    fpr = 1.0 - d0_rate\n\n    d0_col = list(rf.classes_).index(0)\n    mean_p_d0 = float(np.mean(y_prob[:, d0_col]))\n    std_p_d0 = float(np.std(y_prob[:, d0_col]))\n\n    results = {\n        \"n_wild_samples\": n_total,\n        \"d0_rate\": round(d0_rate, 4),\n        \"fpr_d_gt_0\": round(fpr, 4),\n        \"prediction_distribution\": {str(k): v for k, v in sorted(pred_dist.items())},\n        \"mean_P_d0\": round(mean_p_d0, 4),\n        \"std_P_d0\": round(std_p_d0, 4),\n    }\n\n    print(f\"  d0 classification rate: {d0_rate:.1%}\")\n    print(f\"  False positive rate (d>0): {fpr:.1%}\")\n    print(f\"  Prediction distribution: {dict(pred_dist)}\")\n    print(f\"  Mean P(d0): {mean_p_d0:.4f} ± {std_p_d0:.4f}\")\n\n    os.makedirs(output_dir, exist_ok=True)\n    with open(os.path.join(output_dir, \"test_a_d0_fpr.json\"), \"w\") as f:\n        json.dump(results, f, indent=2)\n    return results\n\n\n# ── Test B: Mixed-domain 4-class Accuracy ──\n\ndef test_b_mixed_accuracy(wild_X, ctrl_X, ctrl_y, output_dir, seed=42):\n    print(\"\\n\" + \"=\" * 60)\n    print(\"TEST B: Mixed-domain 4-class Accuracy\")\n    print(\"=\" * 60)\n\n    ctrl_X_train, ctrl_X_test, ctrl_y_train, ctrl_y_test = train_test_split(\n        ctrl_X, ctrl_y, test_size=0.2, random_state=seed, stratify=ctrl_y,\n    )\n\n    scaler = StandardScaler()\n    X_train = scaler.fit_transform(ctrl_X_train)\n    rf = RandomForestClassifier(n_estimators=100, random_state=seed, n_jobs=-1)\n    rf.fit(X_train, ctrl_y_train)\n\n    # In-distribution baseline\n    y_pred_ctrl = rf.predict(scaler.transform(ctrl_X_test))\n    acc_indist = accuracy_score(ctrl_y_test, y_pred_ctrl)\n\n    # Mixed test set: wild d0 + controlled d1-d3 (from test split)\n    n_per_class = min(\n        len(wild_X),\n        *[int(np.sum(ctrl_y_test == d)) for d in [1, 2, 3]],\n    )\n    n_per_class = min(n_per_class, 2500)\n\n    rng = np.random.RandomState(seed)\n    mixed_parts_X, mixed_parts_y = [], []\n\n    wild_idx = rng.choice(len(wild_X), min(n_per_class, len(wild_X)), replace=False)\n    mixed_parts_X.append(wild_X[wild_idx])\n    mixed_parts_y.append(np.zeros(len(wild_idx), dtype=np.int64))\n\n    for d in [1, 2, 3]:\n        d_idx = np.where(ctrl_y_test == d)[0]\n        if len(d_idx) > n_per_class:\n            d_idx = rng.choice(d_idx, n_per_class, replace=False)\n        mixed_parts_X.append(ctrl_X_test[d_idx])\n        mixed_parts_y.append(np.full(len(d_idx), d, dtype=np.int64))\n\n    mixed_X = np.vstack(mixed_parts_X)\n    mixed_y = np.concatenate(mixed_parts_y)\n\n    y_pred_mixed = rf.predict(scaler.transform(mixed_X))\n    acc_mixed = accuracy_score(mixed_y, y_pred_mixed)\n\n    labels = [f\"d{d}\" for d in range(4)]\n    report = classification_report(\n        mixed_y, y_pred_mixed, output_dict=True, target_names=labels,\n    )\n\n    results = {\n        \"in_distribution_accuracy\": round(acc_indist, 4),\n        \"mixed_domain_accuracy\": round(acc_mixed, 4),\n        \"accuracy_gap_pp\": round((acc_indist - acc_mixed) * 100, 1),\n        \"n_per_class\": n_per_class,\n        \"per_class_recall\": {\n            f\"d{d}\": round(report[f\"d{d}\"][\"recall\"], 4) for d in range(4)\n        },\n        \"confusion_matrix\": confusion_matrix(mixed_y, y_pred_mixed).tolist(),\n    }\n\n    print(f\"  In-distribution accuracy: {acc_indist:.1%}\")\n    print(f\"  Mixed-domain accuracy:    {acc_mixed:.1%}\")\n    print(f\"  Gap: {results['accuracy_gap_pp']:.1f} pp\")\n    print(f\"  Per-class recall: {results['per_class_recall']}\")\n\n    with open(os.path.join(output_dir, \"test_b_mixed_accuracy.json\"), \"w\") as f:\n        json.dump(results, f, indent=2)\n    return results\n\n\n# ── Test C: Feature Distribution Shift ──\n\ndef compute_mmd_rbf(X, Y, n_subsample=2000, seed=42):\n    from sklearn.metrics.pairwise import rbf_kernel\n    from scipy.spatial.distance import cdist\n\n    rng = np.random.RandomState(seed)\n    n = min(n_subsample, len(X), len(Y))\n    Xs = X[rng.choice(len(X), n, replace=False)]\n    Ys = Y[rng.choice(len(Y), n, replace=False)]\n\n    scaler = StandardScaler()\n    combined = np.vstack([Xs, Ys])\n    scaler.fit(combined)\n    Xs = scaler.transform(Xs)\n    Ys = scaler.transform(Ys)\n\n    dists = cdist(combined[:min(500, len(combined))],\n                  combined[:min(500, len(combined))], \"sqeuclidean\")\n    gamma = 1.0 / max(np.median(dists[dists > 0]), 1e-8)\n\n    XX = rbf_kernel(Xs, Xs, gamma=gamma)\n    YY = rbf_kernel(Ys, Ys, gamma=gamma)\n    XY = rbf_kernel(Xs, Ys, gamma=gamma)\n    mmd2 = XX.mean() + YY.mean() - 2 * XY.mean()\n    return float(np.sqrt(max(mmd2, 0)))\n\n\ndef test_c_distribution_shift(wild_X, ctrl_X, ctrl_y, output_dir):\n    print(\"\\n\" + \"=\" * 60)\n    print(\"TEST C: Feature Distribution Shift (wild d0 vs controlled d0)\")\n    print(\"=\" * 60)\n\n    d0_mask = ctrl_y == 0\n    ctrl_d0_X = ctrl_X[d0_mask]\n    print(f\"  Wild d0: {len(wild_X)} samples\")\n    print(f\"  Controlled d0: {len(ctrl_d0_X)} samples\")\n\n    alpha = 0.05\n    bonferroni_alpha = alpha / NUM_FEATURES\n    ks_results = {}\n\n    for i, fname in enumerate(FEATURE_NAMES):\n        stat, pval = ks_2samp(wild_X[:, i], ctrl_d0_X[:, i])\n        ks_results[fname] = {\n            \"ks_statistic\": round(float(stat), 4),\n            \"p_value\": float(pval),\n            \"significant\": pval < bonferroni_alpha,\n            \"wild_mean\": round(float(np.mean(wild_X[:, i])), 4),\n            \"wild_std\": round(float(np.std(wild_X[:, i])), 4),\n            \"ctrl_mean\": round(float(np.mean(ctrl_d0_X[:, i])), 4),\n            \"ctrl_std\": round(float(np.std(ctrl_d0_X[:, i])), 4),\n        }\n\n    sorted_feats = sorted(ks_results.items(), key=lambda x: -x[1][\"ks_statistic\"])\n\n    print(f\"\\n  KS test (Bonferroni alpha={bonferroni_alpha:.4f}):\")\n    for fname, res in sorted_feats[:10]:\n        sig = \"***\" if res[\"significant\"] else \"   \"\n        print(f\"    {fname:25s}: KS={res['ks_statistic']:.4f}, \"\n              f\"p={res['p_value']:.2e} {sig}\")\n\n    n_sig = sum(1 for r in ks_results.values() if r[\"significant\"])\n    print(f\"\\n  {n_sig}/{NUM_FEATURES} features significantly shifted\")\n\n    mmd_val = compute_mmd_rbf(wild_X, ctrl_d0_X)\n    print(f\"  MMD (RBF): {mmd_val:.4f}\")\n\n    results = {\n        \"ks_tests\": ks_results,\n        \"n_significant_bonferroni\": n_sig,\n        \"bonferroni_alpha\": bonferroni_alpha,\n        \"mmd_rbf\": round(mmd_val, 4),\n        \"top_5_shifted\": [f for f, _ in sorted_feats[:5]],\n    }\n\n    os.makedirs(output_dir, exist_ok=True)\n    with open(os.path.join(output_dir, \"test_c_distribution_shift.json\"), \"w\") as f:\n        json.dump(results, f, indent=2)\n    return results\n\n\n# ── Evaluation Runner ──\n\ndef run_evaluation(args):\n    wild_features_path = os.path.join(args.wild_data_dir, \"wild_d0_features.jsonl\")\n    print(f\"Loading wild features from {wild_features_path}\")\n    wild_X, wild_y = load_features(wild_features_path)\n    print(f\"  Wild: {wild_X.shape[0]} samples, {wild_X.shape[1]} dims\")\n\n    feat_files = find_feature_files(args.controlled_features_dir)\n    if not feat_files:\n        print(f\"ERROR: No feature JSONL files found in {args.controlled_features_dir}\")\n        sys.exit(1)\n\n    print(f\"Found {len(feat_files)} controlled feature file(s): {list(feat_files.keys())}\")\n    os.makedirs(args.output_dir, exist_ok=True)\n    all_results = {}\n\n    for cell_name, fpath in sorted(feat_files.items()):\n        print(f\"\\n{'#' * 70}\")\n        print(f\"# Cell: {cell_name}\")\n        print(f\"# File: {fpath}\")\n        print(f\"{'#' * 70}\")\n\n        ctrl_X, ctrl_y = load_features(fpath)\n        depth_dist = dict(Counter(int(x) for x in ctrl_y))\n        print(f\"  Controlled: {ctrl_X.shape[0]} samples, depths: {depth_dist}\")\n\n        if len(set(ctrl_y)) < 4:\n            print(f\"  SKIP: fewer than 4 depth classes\")\n            continue\n\n        cell_dir = os.path.join(args.output_dir, cell_name)\n\n        res_a = test_a_d0_fpr(wild_X, ctrl_X, ctrl_y, cell_dir, args.seed)\n        res_b = test_b_mixed_accuracy(wild_X, ctrl_X, ctrl_y, cell_dir, args.seed)\n        res_c = test_c_distribution_shift(wild_X, ctrl_X, ctrl_y, cell_dir)\n\n        all_results[cell_name] = {\n            \"test_a\": res_a,\n            \"test_b\": res_b,\n            \"test_c\": {\n                \"mmd_rbf\": res_c[\"mmd_rbf\"],\n                \"n_significant_ks\": res_c[\"n_significant_bonferroni\"],\n                \"top_5_shifted\": res_c[\"top_5_shifted\"],\n            },\n        }\n\n    # Summary\n    print(f\"\\n{'=' * 80}\")\n    print(\"SUMMARY\")\n    print(f\"{'=' * 80}\")\n    print(f\"{'Cell':30s} {'d0%':>6s} {'FPR':>6s} {'Mix':>6s} {'InD':>6s} \"\n          f\"{'Gap':>6s} {'MMD':>6s} {'#KS':>4s}\")\n    print(\"-\" * 80)\n\n    summary = {}\n    for cell, res in sorted(all_results.items()):\n        row = {\n            \"d0_rate\": res[\"test_a\"][\"d0_rate\"],\n            \"fpr\": res[\"test_a\"][\"fpr_d_gt_0\"],\n            \"mixed_acc\": res[\"test_b\"][\"mixed_domain_accuracy\"],\n            \"indist_acc\": res[\"test_b\"][\"in_distribution_accuracy\"],\n            \"gap_pp\": res[\"test_b\"][\"accuracy_gap_pp\"],\n            \"mmd\": res[\"test_c\"][\"mmd_rbf\"],\n            \"n_sig_ks\": res[\"test_c\"][\"n_significant_ks\"],\n        }\n        summary[cell] = row\n        print(f\"{cell:30s} {row['d0_rate']:6.1%} {row['fpr']:6.1%} \"\n              f\"{row['mixed_acc']:6.1%} {row['indist_acc']:6.1%} \"\n              f\"{row['gap_pp']:5.1f}pp {row['mmd']:6.4f} {row['n_sig_ks']:4d}\")\n\n    with open(os.path.join(args.output_dir, \"summary.json\"), \"w\") as f:\n        json.dump(summary, f, indent=2)\n\n    print(f\"\\nAll results saved to {args.output_dir}/\")\n    return all_results\n\n\n# ── Main ──\n\ndef main():\n    args = parse_args()\n\n    if args.mode in (\"download\", \"all\"):\n        from transformers import AutoTokenizer\n        tokenizer = AutoTokenizer.from_pretrained(args.reference_model)\n        output_path = os.path.join(args.wild_data_dir, \"wild_d0.jsonl\")\n        if args.data_source == \"redpajama\":\n            download_redpajama(output_path, args.n_samples, args.min_tokens,\n                               tokenizer, args.seed)\n        else:\n            download_dolma(output_path, args.n_samples, args.min_tokens,\n                           tokenizer, args.seed)\n\n    if args.mode in (\"extract\", \"all\"):\n        run_feature_extraction(args)\n\n    if args.mode in (\"evaluate\", \"all\"):\n        run_evaluation(args)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 288_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_012LwgXCgwVCh3DtGu1jZSsa`</summary>

```json
{
  "todos": [
    {
      "content": "Write wild_data_calibration.py script",
      "status": "completed",
      "activeForm": "Writing wild_data_calibration.py script"
    },
    {
      "content": "Dry-run verify script syntax and argparse",
      "status": "in_progress",
      "activeForm": "Verifying script syntax and argparse"
    },
    {
      "content": "Output plan_015 design document for Director approval",
      "status": "pending",
      "activeForm": "Outputting plan_015 design document"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "9437fad7-88ef-4de2-ab84-ef3157c74365",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTtJvJzfHwoKJ9bac7ehz3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8831,
      "cache_read_input_tokens": 85913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8831
      },
      "output_tokens": 35,
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

_source line 289 · 2026-05-15T19:48:07.792Z_

<details><summary>↩ Tool result · `toolu_012LwgXCgwVCh3DtGu1jZSsa`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "bbf1cfab-4eb0-42fe-b910-a4bd612c96d9",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Write wild_data_calibration.py script",
        "status": "in_progress",
        "activeForm": "Writing wild_data_calibration.py script"
      },
      {
        "content": "Dry-run verify script syntax and argparse",
        "status": "pending",
        "activeForm": "Verifying script syntax and argparse"
      },
      {
        "content": "Output plan_015 design document for Director approval",
        "status": "pending",
        "activeForm": "Outputting plan_015 design document"
      }
    ],
    "newTodos": [
      {
        "content": "Write wild_data_calibration.py script",
        "status": "completed",
        "activeForm": "Writing wild_data_calibration.py script"
      },
      {
        "content": "Dry-run verify script syntax and argparse",
        "status": "in_progress",
        "activeForm": "Verifying script syntax and argparse"
      },
      {
        "content": "Output plan_015 design document for Director approval",
        "status": "pending",
        "activeForm": "Outputting plan_015 design document"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 290_

<details open><summary>🔧 Tool call — Bash · `toolu_01RqgGaGHd27Q1EkdtaSbQS6`</summary>

```json
{
  "command": "python3 -c \"import ast; ast.parse(open('src/wild_data_calibration.py').read()); print('SYNTAX OK')\"",
  "description": "Verify Python syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "b89b9660-6586-4a75-aa45-7b0bce2392ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TF1mJT9b7AwxZthDuQWegj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 207,
      "cache_read_input_tokens": 94744,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 207
      },
      "output_tokens": 62,
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

_source line 291 · 2026-05-15T19:48:10.880Z_

<details><summary>↩ Tool result · `toolu_01RqgGaGHd27Q1EkdtaSbQS6`</summary>

```text
SYNTAX OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "85635db1-45d1-4509-9046-4384622d049f",
  "tool_use_result": {
    "stdout": "SYNTAX OK",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 292_

<details open><summary>🔧 Tool call — Bash · `toolu_0142AfB29YhUL9DaXvNMA2QV`</summary>

```json
{
  "command": "python3 src/wild_data_calibration.py --help",
  "description": "Dry-run argparse verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "7956e198-aaf9-4563-af51-291b9de85c94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Knu1PDbfDrrCxyjkssWiXz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 122,
      "cache_read_input_tokens": 94951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 122
      },
      "output_tokens": 64,
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

_source line 293 · 2026-05-15T19:48:27.780Z_

<details><summary>↩ Tool result · reported error · `toolu_0142AfB29YhUL9DaXvNMA2QV`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/src/wild_data_calibration.py", line 26, in &lt;module>
    from sklearn.ensemble import RandomForestClassifier
ModuleNotFoundError: No module named 'sklearn'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "09c1f85b-8458-474d-a248-05472c6ca504",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/src/wild_data_calibration.py\", line 26, in &lt;module>\n    from sklearn.ensemble import RandomForestClassifier\nModuleNotFoundError: No module named 'sklearn'"
}
```

</details>

---


### Tool call

_source line 294_

<details open><summary>🔧 Tool call — Bash · `toolu_01U8S4fxfQ7LRujytKCJJqyr`</summary>

```json
{
  "command": "python3 -c \"\nimport ast, sys, re\n\nwith open('src/wild_data_calibration.py') as f:\n    source = f.read()\n\ntree = ast.parse(source)\n\n# Find parse_args function and extract argparse arguments\nfor node in ast.walk(tree):\n    if isinstance(node, ast.FunctionDef) and node.name == 'parse_args':\n        for child in ast.walk(node):\n            if isinstance(child, ast.Call):\n                if hasattr(child.func, 'attr') and child.func.attr == 'add_argument':\n                    args_strs = [ast.literal_eval(a) for a in child.args if isinstance(a, ast.Constant)]\n                    print(f'  {args_strs}')\nprint('Argparse structure OK')\n\"",
  "description": "Verify argparse structure without imports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "af5afb12-95ab-4d39-8d52-8caecb9a656b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKxjp6TkX88Qc5fARLhzAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 201,
      "cache_read_input_tokens": 95073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 201
      },
      "output_tokens": 51,
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

_source line 295 · 2026-05-15T19:48:33.142Z_

<details><summary>↩ Tool result · `toolu_01U8S4fxfQ7LRujytKCJJqyr`</summary>

```text
  ['--mode']
  ['--data_source']
  ['--n_samples']
  ['--min_tokens']
  ['--truncate_tokens']
  ['--reference_model']
  ['--gpu']
  ['--batch_size']
  ['--wild_data_dir']
  ['--controlled_features_dir']
  ['--output_dir']
  ['--seed']
Argparse structure OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "ddab2812-1a99-4d98-bdd5-15a526d738d1",
  "tool_use_result": {
    "stdout": "  ['--mode']\n  ['--data_source']\n  ['--n_samples']\n  ['--min_tokens']\n  ['--truncate_tokens']\n  ['--reference_model']\n  ['--gpu']\n  ['--batch_size']\n  ['--wild_data_dir']\n  ['--controlled_features_dir']\n  ['--output_dir']\n  ['--seed']\nArgparse structure OK",
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

_source line 296_

语法和参数解析均正常（sklearn 在本机未安装，服务器上有）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "122a86b2-68cf-4abf-b2ef-2a4ceccb5b39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnLsMiaY53Ly3fUUpZwZaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 95274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 389
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

_source line 297_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Fmdm7vneje1HrqPGac7hPB`</summary>

```json
{
  "todos": [
    {
      "content": "Write wild_data_calibration.py script",
      "status": "completed",
      "activeForm": "Writing wild_data_calibration.py script"
    },
    {
      "content": "Dry-run verify script syntax and argparse",
      "status": "completed",
      "activeForm": "Verifying script syntax and argparse"
    },
    {
      "content": "Output plan_015 design document for Director approval",
      "status": "in_progress",
      "activeForm": "Outputting plan_015 design document"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "8eee1b6b-c148-49ae-b422-74d82300e7a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnLsMiaY53Ly3fUUpZwZaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 95274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 389
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

_source line 298 · 2026-05-15T19:48:37.017Z_

<details><summary>↩ Tool result · `toolu_01Fmdm7vneje1HrqPGac7hPB`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "54fe2453-0611-4190-8b50-d31f630b06c7",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Write wild_data_calibration.py script",
        "status": "completed",
        "activeForm": "Writing wild_data_calibration.py script"
      },
      {
        "content": "Dry-run verify script syntax and argparse",
        "status": "in_progress",
        "activeForm": "Verifying script syntax and argparse"
      },
      {
        "content": "Output plan_015 design document for Director approval",
        "status": "pending",
        "activeForm": "Outputting plan_015 design document"
      }
    ],
    "newTodos": [
      {
        "content": "Write wild_data_calibration.py script",
        "status": "completed",
        "activeForm": "Writing wild_data_calibration.py script"
      },
      {
        "content": "Dry-run verify script syntax and argparse",
        "status": "completed",
        "activeForm": "Verifying script syntax and argparse"
      },
      {
        "content": "Output plan_015 design document for Director approval",
        "status": "in_progress",
        "activeForm": "Outputting plan_015 design document"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 299_

---

## plan_015: Wild-data Calibration 实验方案

### 目标

验证 RF depth classifier 在 wild web text 上的 calibration——确认分类器不会对真实人类文本产生虚假的 depth signal (false positive)。增强论文 Claim 2 (Atlas findings 的 external validity)。

### 数据

| 数据集 | 来源 | 数量 | 处理 |
|--------|------|------|------|
| Wild d0 | `togethercomputer/RedPajama-Data-1T-Sample` (Common Crawl 子集，**排除 Wikipedia** 避免与 controlled d0 重叠) | 10,000 passages | GPT-2 tokenizer 过滤 ≥512 tokens，截断至 512 tokens |
| Controlled d0-d3 | 已有 9-cell 数据（服务器上已提取特征） | 每 cell ~5K×4=20K | 复用已有 feature JSONL |

数据路径：`/root/autodl-tmp/recursive_gen_depth_est/data/wild_calibration/`

### Reference Model

**GPT-2 base** (`gpt2`, 124M params) — 用于提取 wild data 的 19 维特征（PPL 统计 9 + surprisal 3 + lexical 4 + repetition 3），与 controlled experiments 保持一致。

### 三个实验

**Test A: d0 False Positive Rate (FPR)**
- 用每个 cell 的 RF（全量 controlled data 训练），对 10K wild passages 预测
- 指标：d0 分类率（期望 ≥85%）、FPR_{d>0}、mean P(d0)
- 覆盖 9 cells，报告跨 cell 一致性
- 成功标准：所有 cell 的 d0 分类率 ≥85%

**Test B: Mixed-domain 4-class Accuracy**
- 混合测试集：wild d0 (2500) + controlled d1/d2/d3 (各 2500)
- RF 在 controlled train split 训练，在混合集上测试
- 对比 in-distribution accuracy，报告 gap
- 成功标准：accuracy gap ≤5 pp

**Test C: Feature Distribution Shift**
- Wild d0 vs controlled d0 的 19 维特征逐维 KS test（Bonferroni 校正 α=0.05/19）
- MMD (RBF kernel, median heuristic) 作为聚合 domain gap 指标
- 识别 top-5 shifted features，分析哪些特征对 domain 最敏感
- 用于解释 Test A/B 结果

### 预期结果

| 场景 | 预期 | 论文价值 |
|------|------|----------|
| d0 rate ≥90%, gap ≤3pp | **强阳性**：RF 特征具备 domain invariance，直接写入 §5 | 高 |
| d0 rate 85-90%, gap 3-5pp | **弱阳性**：有轻微 domain shift 但不影响 depth signal 检测 | 中 |
| d0 rate <85% | **阴性**：需分析哪些特征泄漏 domain 信息，可能需 domain adaptation | 低（但有信息量） |

### GPU 分配

| 阶段 | 设备 | 预估时间 |
|------|------|----------|
| 数据下载 (RedPajama streaming) | CPU | ~10 min |
| GPT-2 base 特征提取 (10K × 512 tokens) | cuda:0 | ~1.5 GPU·h |
| RF 训练/推理 × 9 cells | CPU | ~5 min |
| KS test + MMD × 9 cells | CPU | ~2 min |
| **Total** | | **~2 GPU·h** (预算 5 GPU·h) |

### 执行步骤

```bash
# 1. 环境准备
source /etc/network_turbo
export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# 2. 下载 GPT-2 base (if not cached)
python -c "from transformers import AutoTokenizer, AutoModelForCausalLM; AutoTokenizer.from_pretrained('gpt2'); AutoModelForCausalLM.from_pretrained('gpt2')"

# 3. 运行全流程
cd /root/autodl-tmp/recursive_gen_depth_est
python src/wild_data_calibration.py --mode all \
  --gpu 0 \
  --n_samples 10000 \
  --reference_model gpt2 \
  --controlled_features_dir results/pythia_nucleus095/ results/gpt2xl_nucleus095/ results/olmo_nucleus095/ \
  --output_dir results/wild_calibration/
```

### 产出

| 文件 | 说明 |
|------|------|
| `data/wild_calibration/wild_d0.jsonl` | 10K wild passages |
| `data/wild_calibration/wild_d0_features.jsonl` | 19-dim 特征 |
| `results/wild_calibration/summary.json` | 9-cell 汇总 |
| `results/wild_calibration/{cell}/test_a_d0_fpr.json` | 每 cell FPR |
| `results/wild_calibration/{cell}/test_b_mixed_accuracy.json` | 混合准确率 |
| `results/wild_calibration/{cell}/test_c_distribution_shift.json` | KS/MMD |
| `src/wild_data_calibration.py` | 实验脚本（已写入） |

### 风险

1. **Reference model 不一致**：如果 controlled features 的提取用的不是 GPT-2 base，Test A/B 会受影响 → 执行前先确认 controlled features 的 reference model，不一致则需用 `--mode extract` 重新提取 controlled features
2. **RedPajama 下载失败**：AutoDL 代理不稳定 → fallback `--data_source dolma`
3. **FPR 偏高**：如果 wild text 的 perplexity 分布与 controlled d0 差异大 → 分析 Test C 结果确定原因，考虑 z-score domain normalization

### 注意事项

- 脚本已通过本地 syntax + argparse 验证
- 服务器部署前需 `source /etc/network_turbo` + SSL 环境变量
- GPT-2 base 仅 ~500MB，下载快，不占根分区（HF_HOME 指向数据盘）
- 预留 cuda:1 空闲，可同时跑其他任务

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "141dddc4-f9e2-43d2-80d5-8fd738c792b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrS2AEeinAohJTwpxNXyLY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 95663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
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

_source line 300_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01GhZ9zSdBS8ATrNtHLHoCKT`</summary>

```json
{
  "todos": [
    {
      "content": "Write wild_data_calibration.py script",
      "status": "completed",
      "activeForm": "Writing wild_data_calibration.py script"
    },
    {
      "content": "Dry-run verify script syntax and argparse",
      "status": "completed",
      "activeForm": "Verifying script syntax and argparse"
    },
    {
      "content": "Output plan_015 design document for Director approval",
      "status": "completed",
      "activeForm": "Outputting plan_015 design document"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "4707d5b6-23d5-4f7c-a9c8-cc3de227c09f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrS2AEeinAohJTwpxNXyLY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 235,
      "cache_read_input_tokens": 95663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 235
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

_source line 301 · 2026-05-15T19:49:34.631Z_

<details><summary>↩ Tool result · `toolu_01GhZ9zSdBS8ATrNtHLHoCKT`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "48571a2e-738b-4d2e-b902-d5b64ebc2c6b",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Write wild_data_calibration.py script",
        "status": "completed",
        "activeForm": "Writing wild_data_calibration.py script"
      },
      {
        "content": "Dry-run verify script syntax and argparse",
        "status": "completed",
        "activeForm": "Verifying script syntax and argparse"
      },
      {
        "content": "Output plan_015 design document for Director approval",
        "status": "in_progress",
        "activeForm": "Outputting plan_015 design document"
      }
    ],
    "newTodos": [
      {
        "content": "Write wild_data_calibration.py script",
        "status": "completed",
        "activeForm": "Writing wild_data_calibration.py script"
      },
      {
        "content": "Dry-run verify script syntax and argparse",
        "status": "completed",
        "activeForm": "Verifying script syntax and argparse"
      },
      {
        "content": "Output plan_015 design document for Director approval",
        "status": "completed",
        "activeForm": "Outputting plan_015 design document"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 302_

plan_015 设计完成。脚本 `src/wild_data_calibration.py` 已写入，支持 `--mode download|extract|evaluate|all` 四种运行模式。核心设计：10K RedPajama (排除 Wikipedia) 作为 wild d0，三个测试 (FPR / 混合准确率 / KS+MMD 分布偏移)，覆盖 9 cells，预估 ~2 GPU·h。待审批。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "uuid": "c58ded93-40b2-408d-b5a6-df4e17a56591",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SHheogiKdSrp66Lzae8n9y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2136,
      "cache_read_input_tokens": 95898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2136
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

_source line 303_

plan_015 设计完成。脚本 `src/wild_data_calibration.py` 已写入，支持 `--mode download|extract|evaluate|all` 四种运行模式。核心设计：10K RedPajama (排除 Wikipedia) 作为 wild d0，三个测试 (FPR / 混合准确率 / KS+MMD 分布偏移)，覆盖 9 cells，预估 ~2 GPU·h。待审批。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 765413,
  "duration_api_ms": 767051,
  "num_turns": 31,
  "stop_reason": "end_turn",
  "session_id": "adc05a57-a71c-4f49-97c1-a1559984d6a5",
  "total_cost_usd": 2.4534756499999997,
  "usage": {
    "input_tokens": 28,
    "cache_creation_input_tokens": 86193,
    "cache_read_input_tokens": 1300230,
    "output_tokens": 33465,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 86193,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 134,
        "cache_read_input_tokens": 95898,
        "cache_creation_input_tokens": 2136,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2136
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1955,
      "outputTokens": 13551,
      "cacheReadInputTokens": 2120219,
      "cacheCreationInputTokens": 116926,
      "webSearchRequests": 0,
      "costUSD": 0.42788940000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 28,
      "outputTokens": 33465,
      "cacheReadInputTokens": 1300230,
      "cacheCreationInputTokens": 86193,
      "webSearchRequests": 0,
      "costUSD": 2.02558625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0df75ae0-adbe-4793-9046-553d204da39f"
}
```

</details>

---
