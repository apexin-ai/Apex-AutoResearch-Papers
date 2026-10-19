# analysis plan 005 stratified — Part 39 of 39

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Worker execution logs

[← Part 38](part-038.md) · [Transcript overview](../analysis-plan-005-stratified.md) · [Structured JSON](../../../sessions/ca/cacae794176b02f848f1.json)

## Before a recorded user message

### Tool result

_source line 168 · 2026-05-14T20:22:31.106Z_

<details><summary>↩ Tool result · `toolu_01FCX89VD4FdwGofuukzpzdo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    return results\\n\\n\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\n    for r in results:\\n        groups[r[key]].append(r)\\n    return dict(groups)\\n\\n\\n# ── Analysis core ────────────────────────────────────────────────────\\n\\ndef run_stratified_analysis(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    strata_key: str,\\n    bin_order: List[str],\\n    n_bootstrap: int = 1000,\\n) -> Dict:\\n    analysis = {}\\n    for bin_name in bin_order:\\n        analysis[bin_name] = {}\\n        for strategy in STRATEGIES:\\n            seed_results = []\\n            for seed, results in all_results.get(strategy, {}).items():\\n                grouped = group_by(results, strata_key)\\n                seed_results.extend(grouped.get(bin_name, []))\\n\\n            metrics = compute_metrics(seed_results)\\n            ci_r1 = bootstrap_ci(seed_results, \\\"R@1\\\", n_bootstrap)\\n            ci_r5 = bootstrap_ci(seed_results, \\\"R@5\\\", n_bootstrap)\\n            ci_mrr = bootstrap_ci(seed_results, \\\"MRR\\\", n_bootstrap)\\n\\n            analysis[bin_name][strategy] = {\\n                \\\"R@1\\\": ci_r1[0],\\n                \\\"R@1_ci\\\": [ci_r1[1], ci_r1[2]],\\n                \\\"R@5\\\": ci_r5[0],\\n                \\\"R@5_ci\\\": [ci_r5[1], ci_r5[2]],\\n                \\\"MRR\\\": ci_mrr[0],\\n                \\\"MRR_ci\\\": [ci_mrr[1], ci_mrr[2]],\\n                \\\"count\\\": metrics[\\\"count\\\"],\\n            }\\n\\n        # Compute deltas (embedding - random)\\n        rand_m = analysis[bin_name].get(\\\"random\\\", {})\\n        for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n            other_m = analysis[bin_name].get(other, {})\\n            delta_key = f\\\"{other}_vs_random\\\"\\n            if rand_m and other_m:\\n                for metric in [\\\"R@1\\\", \\\"R@5\\\", \\\"MRR\\\"]:\\n                    rv = rand_m.get(metric, 0)\\n                    ov = other_m.get(metric, 0)\\n                    analysis[bin_name].setdefault(delta_key, {})[f\\\"{metric}_delta\\\"] = ov - rv\\n                    analysis[bin_name][delta_key][f\\\"{metric}_rel_pct\\\"] = (\\n                        (ov - rv) / rv * 100 if rv > 0 else 0.0\\n                    )\\n\\n    return analysis\\n\\n\\n# ── Visualization ────────────────────────────────────────────────────\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "027f89e3-3e47-4165-808f-c1be008e7024",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    return results\\\\n\\\\n\\\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\\\n    for r in results:\\\\n        groups[r[key]].append(r)\\\\n    return dict(groups)\\\\n\\\\n\\\\n# ── Analysis core ────────────────────────────────────────────────────\\\\n\\\\ndef run_stratified_analysis(\\\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\\\n    strata_key: str,\\\\n    bin_order: List[str],\\\\n    n_bootstrap: int = 1000,\\\\n) -> Dict:\\\\n    analysis = {}\\\\n    for bin_name in bin_order:\\\\n        analysis[bin_name] = {}\\\\n        for strategy in STRATEGIES:\\\\n            seed_results = []\\\\n            for seed, results in all_results.get(strategy, {}).items():\\\\n                grouped = group_by(results, strata_key)\\\\n                seed_results.extend(grouped.get(bin_name, []))\\\\n\\\\n            metrics = compute_metrics(seed_results)\\\\n            ci_r1 = bootstrap_ci(seed_results, \\\\\\\"R@1\\\\\\\", n_bootstrap)\\\\n            ci_r5 = bootstrap_ci(seed_results, \\\\\\\"R@5\\\\\\\", n_bootstrap)\\\\n            ci_mrr = bootstrap_ci(seed_results, \\\\\\\"MRR\\\\\\\", n_bootstrap)\\\\n\\\\n            analysis[bin_name][strategy] = {\\\\n                \\\\\\\"R@1\\\\\\\": ci_r1[0],\\\\n                \\\\\\\"R@1_ci\\\\\\\": [ci_r1[1], ci_r1[2]],\\\\n                \\\\\\\"R@5\\\\\\\": ci_r5[0],\\\\n                \\\\\\\"R@5_ci\\\\\\\": [ci_r5[1], ci_r5[2]],\\\\n                \\\\\\\"MRR\\\\\\\": ci_mrr[0],\\\\n                \\\\\\\"MRR_ci\\\\\\\": [ci_mrr[1], ci_mrr[2]],\\\\n                \\\\\\\"count\\\\\\\": metrics[\\\\\\\"count\\\\\\\"],\\\\n            }\\\\n\\\\n        # Compute deltas (embedding - random)\\\\n        rand_m = analysis[bin_name].get(\\\\\\\"random\\\\\\\", {})\\\\n        for other in [\\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]:\\\\n            other_m = analysis[bin_name].get(other, {})\\\\n            delta_key = f\\\\\\\"{other}_vs_random\\\\\\\"\\\\n            if rand_m and other_m:\\\\n                for metric in [\\\\\\\"R@1\\\\\\\", \\\\\\\"R@5\\\\\\\", \\\\\\\"MRR\\\\\\\"]:\\\\n                    rv = rand_m.get(metric, 0)\\\\n                    ov = other_m.get(metric, 0)\\\\n                    analysis[bin_name].setdefault(delta_key, {})[f\\\\\\\"{metric}_delta\\\\\\\"] = ov - rv\\\\n                    analysis[bin_name][delta_key][f\\\\\\\"{metric}_rel_pct\\\\\\\"] = (\\\\n                        (ov - rv) / rv * 100 if rv > 0 else 0.0\\\\n                    )\\\\n\\\\n    return analysis\\\\n\\\\n\\\\n# ── Visualization ────────────────────────────────────────────────────\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    return results\\n\\n\\ndef group_by(results: List[Dict], key: str) -> Dict[str, List[Dict]]:\\n    groups: Dict[str, List[Dict]] = defaultdict(list)\\n    for r in results:\\n        groups[r[key]].append(r)\\n    return dict(groups)\\n\\n\\n# ── Analysis core ────────────────────────────────────────────────────\\n\\ndef run_stratified_analysis(\\n    all_results: Dict[str, Dict[int, List[Dict]]],\\n    strata_key: str,\\n    bin_order: List[str],\\n    n_bootstrap: int = 1000,\\n) -> Dict:\\n    analysis = {}\\n    for bin_name in bin_order:\\n        analysis[bin_name] = {}\\n        for strategy in STRATEGIES:\\n            seed_results = []\\n            for seed, results in all_results.get(strategy, {}).items():\\n                grouped = group_by(results, strata_key)\\n                seed_results.extend(grouped.get(bin_name, []))\\n\\n            metrics = compute_metrics(seed_results)\\n            ci_r1 = bootstrap_ci(seed_results, \\\"R@1\\\", n_bootstrap)\\n            ci_r5 = bootstrap_ci(seed_results, \\\"R@5\\\", n_bootstrap)\\n            ci_mrr = bootstrap_ci(seed_results, \\\"MRR\\\", n_bootstrap)\\n\\n            analysis[bin_name][strategy] = {\\n                \\\"R@1\\\": ci_r1[0],\\n                \\\"R@1_ci\\\": [ci_r1[1], ci_r1[2]],\\n                \\\"R@5\\\": ci_r5[0],\\n                \\\"R@5_ci\\\": [ci_r5[1], ci_r5[2]],\\n                \\\"MRR\\\": ci_mrr[0],\\n                \\\"MRR_ci\\\": [ci_mrr[1], ci_mrr[2]],\\n                \\\"count\\\": metrics[\\\"count\\\"],\\n            }\\n\\n        # Compute deltas (embedding - random)\\n        rand_m = analysis[bin_name].get(\\\"random\\\", {})\\n        for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n            other_m = analysis[bin_name].get(other, {})\\n            delta_key = f\\\"{other}_vs_random\\\"\\n            if rand_m and other_m:\\n                for metric in [\\\"R@1\\\", \\\"R@5\\\", \\\"MRR\\\"]:\\n                    rv = rand_m.get(metric, 0)\\n                    ov = other_m.get(metric, 0)\\n                    analysis[bin_name].setdefault(delta_key, {})[f\\\"{metric}_delta\\\"] = ov - rv\\n                    analysis[bin_name][delta_key][f\\\"{metric}_rel_pct\\\"] = (\\n                        (ov - rv) / rv * 100 if rv > 0 else 0.0\\n                    )\\n\\n    return analysis\\n\\n\\n# ── Visualization ────────────────────────────────────────────────────\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-14T20:22:31.530Z_

<details><summary>↩ Tool result · `toolu_014f47BB4BZ2ghbgYvMyffBL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    repo_analysis: Dict,\\n    pool_analysis: Dict,\\n    sim_analysis: Dict,\\n    output_path: str,\\n):\\n    rows = []\\n    for dim_name, analysis, bin_order in [\\n        (\\\"repo_size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n        (\\\"pool_size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n        (\\\"similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n    ]:\\n        for b in bin_order:\\n            if b not in analysis:\\n                continue\\n            for strategy in STRATEGIES:\\n                m = analysis[b].get(strategy, {})\\n                ci_r1 = m.get(\\\"R@1_ci\\\", [0, 0])\\n                row = {\\n                    \\\"dimension\\\": dim_name,\\n                    \\\"stratum\\\": b,\\n                    \\\"strategy\\\": strategy,\\n                    \\\"R@1\\\": f\\\"{m.get('R@1', 0):.4f}\\\",\\n                    \\\"R@1_ci95\\\": f\\\"[{ci_r1[0]:.4f}, {ci_r1[1]:.4f}]\\\",\\n                    \\\"R@5\\\": f\\\"{m.get('R@5', 0):.4f}\\\",\\n                    \\\"MRR\\\": f\\\"{m.get('MRR', 0):.4f}\\\",\\n                    \\\"count\\\": m.get(\\\"count\\\", 0),\\n                }\\n                rows.append(row)\\n\\n            # Deltas\\n            for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n                dk = f\\\"{other}_vs_random\\\"\\n                d = analysis[b].get(dk, {})\\n                if d:\\n                    row = {\\n                        \\\"dimension\\\": dim_name,\\n                        \\\"stratum\\\": b,\\n                        \\\"strategy\\\": f\\\"DELTA({STRATEGY_LABELS[other]}-Random)\\\",\\n                        \\\"R@1\\\": f\\\"{d.get('R@1_delta', 0):+.4f}\\\",\\n                        \\\"R@1_ci95\\\": f\\\"({d.get('R@1_rel_pct', 0):+.1f}%)\\\",\\n                        \\\"R@5\\\": f\\\"{d.get('R@5_delta', 0):+.4f}\\\",\\n                        \\\"MRR\\\": f\\\"{d.get('MRR_delta', 0):+.4f}\\\",\\n                        \\\"count\\\": \\\"\\\",\\n                    }\\n                    rows.append(row)\\n\\n    fieldnames = [\\\"dimension\\\", \\\"stratum\\\", \\\"strategy\\\", \\\"R@1\\\", \\\"R@1_ci95\\\", \\\"R@5\\\", \\\"MRR\\\", \\\"count\\\"]\\n    with open(output_path, \\\"w\\\", newline=\\\"\\\") as f:\\n        writer = csv.DictWriter(f, fieldnames=fieldnames)\\n        writer.writeheader()\\n        writer.writerows(rows)\\n    print(f\\\"  Summary CSV saved to {output_path}\\\", flush=True)\\n\\n\\n# ── Main ─────────────────────────────────────────────────────────────\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Stratified analysis of M2 strategies by data strata\\\"\\n    )\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "32f0f87f-e37e-4b07-ada0-9c6e3de12067",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    repo_analysis: Dict,\\\\n    pool_analysis: Dict,\\\\n    sim_analysis: Dict,\\\\n    output_path: str,\\\\n):\\\\n    rows = []\\\\n    for dim_name, analysis, bin_order in [\\\\n        (\\\\\\\"repo_size\\\\\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\\\n        (\\\\\\\"pool_size\\\\\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\\\n        (\\\\\\\"similarity\\\\\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\\\n    ]:\\\\n        for b in bin_order:\\\\n            if b not in analysis:\\\\n                continue\\\\n            for strategy in STRATEGIES:\\\\n                m = analysis[b].get(strategy, {})\\\\n                ci_r1 = m.get(\\\\\\\"R@1_ci\\\\\\\", [0, 0])\\\\n                row = {\\\\n                    \\\\\\\"dimension\\\\\\\": dim_name,\\\\n                    \\\\\\\"stratum\\\\\\\": b,\\\\n                    \\\\\\\"strategy\\\\\\\": strategy,\\\\n                    \\\\\\\"R@1\\\\\\\": f\\\\\\\"{m.get('R@1', 0):.4f}\\\\\\\",\\\\n                    \\\\\\\"R@1_ci95\\\\\\\": f\\\\\\\"[{ci_r1[0]:.4f}, {ci_r1[1]:.4f}]\\\\\\\",\\\\n                    \\\\\\\"R@5\\\\\\\": f\\\\\\\"{m.get('R@5', 0):.4f}\\\\\\\",\\\\n                    \\\\\\\"MRR\\\\\\\": f\\\\\\\"{m.get('MRR', 0):.4f}\\\\\\\",\\\\n                    \\\\\\\"count\\\\\\\": m.get(\\\\\\\"count\\\\\\\", 0),\\\\n                }\\\\n                rows.append(row)\\\\n\\\\n            # Deltas\\\\n            for other in [\\\\\\\"embedding_distance\\\\\\\", \\\\\\\"dataflow_aware\\\\\\\"]:\\\\n                dk = f\\\\\\\"{other}_vs_random\\\\\\\"\\\\n                d = analysis[b].get(dk, {})\\\\n                if d:\\\\n                    row = {\\\\n                        \\\\\\\"dimension\\\\\\\": dim_name,\\\\n                        \\\\\\\"stratum\\\\\\\": b,\\\\n                        \\\\\\\"strategy\\\\\\\": f\\\\\\\"DELTA({STRATEGY_LABELS[other]}-Random)\\\\\\\",\\\\n                        \\\\\\\"R@1\\\\\\\": f\\\\\\\"{d.get('R@1_delta', 0):+.4f}\\\\\\\",\\\\n                        \\\\\\\"R@1_ci95\\\\\\\": f\\\\\\\"({d.get('R@1_rel_pct', 0):+.1f}%)\\\\\\\",\\\\n                        \\\\\\\"R@5\\\\\\\": f\\\\\\\"{d.get('R@5_delta', 0):+.4f}\\\\\\\",\\\\n                        \\\\\\\"MRR\\\\\\\": f\\\\\\\"{d.get('MRR_delta', 0):+.4f}\\\\\\\",\\\\n                        \\\\\\\"count\\\\\\\": \\\\\\\"\\\\\\\",\\\\n                    }\\\\n                    rows.append(row)\\\\n\\\\n    fieldnames = [\\\\\\\"dimension\\\\\\\", \\\\\\\"stratum\\\\\\\", \\\\\\\"strategy\\\\\\\", \\\\\\\"R@1\\\\\\\", \\\\\\\"R@1_ci95\\\\\\\", \\\\\\\"R@5\\\\\\\", \\\\\\\"MRR\\\\\\\", \\\\\\\"count\\\\\\\"]\\\\n    with open(output_path, \\\\\\\"w\\\\\\\", newline=\\\\\\\"\\\\\\\") as f:\\\\n        writer = csv.DictWriter(f, fieldnames=fieldnames)\\\\n        writer.writeheader()\\\\n        writer.writerows(rows)\\\\n    print(f\\\\\\\"  Summary CSV saved to {output_path}\\\\\\\", flush=True)\\\\n\\\\n\\\\n# ── Main ─────────────────────────────────────────────────────────────\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(\\\\n        description=\\\\\\\"Stratified analysis of M2 strategies by data strata\\\\\\\"\\\\n    )\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.42}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    repo_analysis: Dict,\\n    pool_analysis: Dict,\\n    sim_analysis: Dict,\\n    output_path: str,\\n):\\n    rows = []\\n    for dim_name, analysis, bin_order in [\\n        (\\\"repo_size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n        (\\\"pool_size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n        (\\\"similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n    ]:\\n        for b in bin_order:\\n            if b not in analysis:\\n                continue\\n            for strategy in STRATEGIES:\\n                m = analysis[b].get(strategy, {})\\n                ci_r1 = m.get(\\\"R@1_ci\\\", [0, 0])\\n                row = {\\n                    \\\"dimension\\\": dim_name,\\n                    \\\"stratum\\\": b,\\n                    \\\"strategy\\\": strategy,\\n                    \\\"R@1\\\": f\\\"{m.get('R@1', 0):.4f}\\\",\\n                    \\\"R@1_ci95\\\": f\\\"[{ci_r1[0]:.4f}, {ci_r1[1]:.4f}]\\\",\\n                    \\\"R@5\\\": f\\\"{m.get('R@5', 0):.4f}\\\",\\n                    \\\"MRR\\\": f\\\"{m.get('MRR', 0):.4f}\\\",\\n                    \\\"count\\\": m.get(\\\"count\\\", 0),\\n                }\\n                rows.append(row)\\n\\n            # Deltas\\n            for other in [\\\"embedding_distance\\\", \\\"dataflow_aware\\\"]:\\n                dk = f\\\"{other}_vs_random\\\"\\n                d = analysis[b].get(dk, {})\\n                if d:\\n                    row = {\\n                        \\\"dimension\\\": dim_name,\\n                        \\\"stratum\\\": b,\\n                        \\\"strategy\\\": f\\\"DELTA({STRATEGY_LABELS[other]}-Random)\\\",\\n                        \\\"R@1\\\": f\\\"{d.get('R@1_delta', 0):+.4f}\\\",\\n                        \\\"R@1_ci95\\\": f\\\"({d.get('R@1_rel_pct', 0):+.1f}%)\\\",\\n                        \\\"R@5\\\": f\\\"{d.get('R@5_delta', 0):+.4f}\\\",\\n                        \\\"MRR\\\": f\\\"{d.get('MRR_delta', 0):+.4f}\\\",\\n                        \\\"count\\\": \\\"\\\",\\n                    }\\n                    rows.append(row)\\n\\n    fieldnames = [\\\"dimension\\\", \\\"stratum\\\", \\\"strategy\\\", \\\"R@1\\\", \\\"R@1_ci95\\\", \\\"R@5\\\", \\\"MRR\\\", \\\"count\\\"]\\n    with open(output_path, \\\"w\\\", newline=\\\"\\\") as f:\\n        writer = csv.DictWriter(f, fieldnames=fieldnames)\\n        writer.writeheader()\\n        writer.writerows(rows)\\n    print(f\\\"  Summary CSV saved to {output_path}\\\", flush=True)\\n\\n\\n# ── Main ─────────────────────────────────────────────────────────────\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Stratified analysis of M2 strategies by data strata\\\"\\n    )\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 170_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_0149725jXfnMDUYxFiasM7dk`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "head -n 560 /root/structfuse/evaluation/analyze_stratified.py | tail -n 60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "45c1e232-deda-476f-a330-320389fb2e89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETcxaH3iKFLvCTBmpyWdcF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 81536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2526
      },
      "output_tokens": 68,
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

_source line 171 · 2026-05-14T20:22:35.956Z_

<details><summary>↩ Tool result · `toolu_0149725jXfnMDUYxFiasM7dk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"            ax.set_yticklabels(bins_present)\\n            ax.set_title(f\\\"R@1 Heatmap — {title}\\\", fontweight=\\\"bold\\\")\\n\\n            for i in range(len(bins_present)):\\n                for j in range(len(STRATEGIES)):\\n                    val = data_matrix[i, j]\\n                    color = \\\"white\\\" if val > data_matrix.max() * 0.6 else \\\"black\\\"\\n                    ax.text(j, i, f\\\"{val:.3f}\\\", ha=\\\"center\\\", va=\\\"center\\\",\\n                            color=color, fontsize=10, fontweight=\\\"bold\\\")\\n\\n            fig.colorbar(im, ax=ax, shrink=0.8)\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n        # ── Plot 3: Delta trends ──\\n        for title, analysis, bin_order in [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            fig, ax = plt.subplots(figsize=(8, 5))\\n            x = np.arange(len(bins_present))\\n\\n            for other, color, marker in [\\n                (\\\"embedding_distance\\\", \\\"#DD8452\\\", \\\"o\\\"),\\n                (\\\"dataflow_aware\\\", \\\"#55A868\\\", \\\"s\\\"),\\n            ]:\\n                delta_key = f\\\"{other}_vs_random\\\"\\n                deltas = []\\n                for b in bins_present:\\n                    d = analysis[b].get(delta_key, {}).get(\\\"R@1_delta\\\", 0)\\n                    deltas.append(d)\\n\\n                ax.plot(x, deltas, marker=marker, linewidth=2, markersize=8,\\n                        color=color, label=f\\\"{STRATEGY_LABELS[other]} - Random\\\")\\n\\n            ax.axhline(y=0, color=\\\"gray\\\", linestyle=\\\"--\\\", linewidth=0.8)\\n            ax.set_xlabel(title)\\n            ax.set_ylabel(\\\"R@1 Delta (vs Random)\\\")\\n            ax.set_title(f\\\"R@1 Delta Trend — {title}\\\", fontweight=\\\"bold\\\")\\n            ax.set_xticks(x)\\n            ax.set_xticklabels(bins_present)\\n            ax.legend(loc=\\\"best\\\")\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n    # Also save individual PNGs\\n    print(f\\\"  Plots saved to {pdf_path}\\\", flush=True)\\n    return pdf_path\\n\\n\\n# ── CSV output ───────────────────────────────────────────────────────\\n\\ndef write_summary_csv(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "09b93f3c-551d-46d2-9c58-41337fbeca87",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"            ax.set_yticklabels(bins_present)\\\\n            ax.set_title(f\\\\\\\"R@1 Heatmap — {title}\\\\\\\", fontweight=\\\\\\\"bold\\\\\\\")\\\\n\\\\n            for i in range(len(bins_present)):\\\\n                for j in range(len(STRATEGIES)):\\\\n                    val = data_matrix[i, j]\\\\n                    color = \\\\\\\"white\\\\\\\" if val > data_matrix.max() * 0.6 else \\\\\\\"black\\\\\\\"\\\\n                    ax.text(j, i, f\\\\\\\"{val:.3f}\\\\\\\", ha=\\\\\\\"center\\\\\\\", va=\\\\\\\"center\\\\\\\",\\\\n                            color=color, fontsize=10, fontweight=\\\\\\\"bold\\\\\\\")\\\\n\\\\n            fig.colorbar(im, ax=ax, shrink=0.8)\\\\n            plt.tight_layout()\\\\n            pdf.savefig(fig, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n            plt.close(fig)\\\\n\\\\n        # ── Plot 3: Delta trends ──\\\\n        for title, analysis, bin_order in [\\\\n            (\\\\\\\"Repo Size\\\\\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Pool Size\\\\\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Similarity\\\\\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\\\n        ]:\\\\n            bins_present = [b for b in bin_order if b in analysis]\\\\n            if not bins_present:\\\\n                continue\\\\n\\\\n            fig, ax = plt.subplots(figsize=(8, 5))\\\\n            x = np.arange(len(bins_present))\\\\n\\\\n            for other, color, marker in [\\\\n                (\\\\\\\"embedding_distance\\\\\\\", \\\\\\\"#DD8452\\\\\\\", \\\\\\\"o\\\\\\\"),\\\\n                (\\\\\\\"dataflow_aware\\\\\\\", \\\\\\\"#55A868\\\\\\\", \\\\\\\"s\\\\\\\"),\\\\n            ]:\\\\n                delta_key = f\\\\\\\"{other}_vs_random\\\\\\\"\\\\n                deltas = []\\\\n                for b in bins_present:\\\\n                    d = analysis[b].get(delta_key, {}).get(\\\\\\\"R@1_delta\\\\\\\", 0)\\\\n                    deltas.append(d)\\\\n\\\\n                ax.plot(x, deltas, marker=marker, linewidth=2, markersize=8,\\\\n                        color=color, label=f\\\\\\\"{STRATEGY_LABELS[other]} - Random\\\\\\\")\\\\n\\\\n            ax.axhline(y=0, color=\\\\\\\"gray\\\\\\\", linestyle=\\\\\\\"--\\\\\\\", linewidth=0.8)\\\\n            ax.set_xlabel(title)\\\\n            ax.set_ylabel(\\\\\\\"R@1 Delta (vs Random)\\\\\\\")\\\\n            ax.set_title(f\\\\\\\"R@1 Delta Trend — {title}\\\\\\\", fontweight=\\\\\\\"bold\\\\\\\")\\\\n            ax.set_xticks(x)\\\\n            ax.set_xticklabels(bins_present)\\\\n            ax.legend(loc=\\\\\\\"best\\\\\\\")\\\\n            plt.tight_layout()\\\\n            pdf.savefig(fig, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n            plt.close(fig)\\\\n\\\\n    # Also save individual PNGs\\\\n    print(f\\\\\\\"  Plots saved to {pdf_path}\\\\\\\", flush=True)\\\\n    return pdf_path\\\\n\\\\n\\\\n# ── CSV output ───────────────────────────────────────────────────────\\\\n\\\\ndef write_summary_csv(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"            ax.set_yticklabels(bins_present)\\n            ax.set_title(f\\\"R@1 Heatmap — {title}\\\", fontweight=\\\"bold\\\")\\n\\n            for i in range(len(bins_present)):\\n                for j in range(len(STRATEGIES)):\\n                    val = data_matrix[i, j]\\n                    color = \\\"white\\\" if val > data_matrix.max() * 0.6 else \\\"black\\\"\\n                    ax.text(j, i, f\\\"{val:.3f}\\\", ha=\\\"center\\\", va=\\\"center\\\",\\n                            color=color, fontsize=10, fontweight=\\\"bold\\\")\\n\\n            fig.colorbar(im, ax=ax, shrink=0.8)\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n        # ── Plot 3: Delta trends ──\\n        for title, analysis, bin_order in [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            fig, ax = plt.subplots(figsize=(8, 5))\\n            x = np.arange(len(bins_present))\\n\\n            for other, color, marker in [\\n                (\\\"embedding_distance\\\", \\\"#DD8452\\\", \\\"o\\\"),\\n                (\\\"dataflow_aware\\\", \\\"#55A868\\\", \\\"s\\\"),\\n            ]:\\n                delta_key = f\\\"{other}_vs_random\\\"\\n                deltas = []\\n                for b in bins_present:\\n                    d = analysis[b].get(delta_key, {}).get(\\\"R@1_delta\\\", 0)\\n                    deltas.append(d)\\n\\n                ax.plot(x, deltas, marker=marker, linewidth=2, markersize=8,\\n                        color=color, label=f\\\"{STRATEGY_LABELS[other]} - Random\\\")\\n\\n            ax.axhline(y=0, color=\\\"gray\\\", linestyle=\\\"--\\\", linewidth=0.8)\\n            ax.set_xlabel(title)\\n            ax.set_ylabel(\\\"R@1 Delta (vs Random)\\\")\\n            ax.set_title(f\\\"R@1 Delta Trend — {title}\\\", fontweight=\\\"bold\\\")\\n            ax.set_xticks(x)\\n            ax.set_xticklabels(bins_present)\\n            ax.legend(loc=\\\"best\\\")\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n    # Also save individual PNGs\\n    print(f\\\"  Plots saved to {pdf_path}\\\", flush=True)\\n    return pdf_path\\n\\n\\n# ── CSV output ───────────────────────────────────────────────────────\\n\\ndef write_summary_csv(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 172_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01EnLj2H9WYco5mjYjVBxcBt`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "head -n 500 /root/structfuse/evaluation/analyze_stratified.py | tail -n 100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "b18aca15-da99-4e8c-8433-b79f32275321",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETcxaH3iKFLvCTBmpyWdcF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 81536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2526
      },
      "output_tokens": 68,
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

_source line 173 · 2026-05-14T20:22:36.439Z_

<details><summary>↩ Tool result · `toolu_01EnLj2H9WYco5mjYjVBxcBt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\ndef make_plots(\\n    repo_analysis: Dict,\\n    pool_analysis: Dict,\\n    sim_analysis: Dict,\\n    output_dir: str,\\n):\\n    import matplotlib\\n    matplotlib.use(\\\"Agg\\\")\\n    import matplotlib.pyplot as plt\\n    from matplotlib.backends.backend_pdf import PdfPages\\n\\n    plt.rcParams.update({\\n        \\\"font.size\\\": 11,\\n        \\\"axes.titlesize\\\": 13,\\n        \\\"axes.labelsize\\\": 12,\\n        \\\"xtick.labelsize\\\": 10,\\n        \\\"ytick.labelsize\\\": 10,\\n        \\\"legend.fontsize\\\": 10,\\n        \\\"figure.dpi\\\": 150,\\n        \\\"savefig.dpi\\\": 300,\\n        \\\"font.family\\\": \\\"sans-serif\\\",\\n    })\\n\\n    pdf_path = os.path.join(output_dir, \\\"stratified_plots.pdf\\\")\\n    with PdfPages(pdf_path) as pdf:\\n        # ── Plot 1: Grouped bar chart per stratum dimension ──\\n        for title, analysis, bin_order in [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Candidate Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Query-Positive Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            fig, axes = plt.subplots(1, 3, figsize=(15, 5))\\n            fig.suptitle(f\\\"Stratified by {title}\\\", fontweight=\\\"bold\\\", y=1.02)\\n\\n            for ax_idx, metric in enumerate([\\\"R@1\\\", \\\"R@5\\\", \\\"MRR\\\"]):\\n                ax = axes[ax_idx]\\n                x = np.arange(len(bins_present))\\n                width = 0.25\\n\\n                for i, strategy in enumerate(STRATEGIES):\\n                    vals = []\\n                    errs_lo = []\\n                    errs_hi = []\\n                    for b in bins_present:\\n                        m = analysis[b].get(strategy, {})\\n                        v = m.get(metric, 0)\\n                        ci = m.get(f\\\"{metric}_ci\\\", [v, v])\\n                        vals.append(v)\\n                        errs_lo.append(v - ci[0])\\n                        errs_hi.append(ci[1] - v)\\n\\n                    offset = (i - 1) * width\\n                    bars = ax.bar(\\n                        x + offset, vals, width,\\n                        label=STRATEGY_LABELS[strategy],\\n                        color=STRATEGY_COLORS[strategy],\\n                        yerr=[errs_lo, errs_hi],\\n                        capsize=3, alpha=0.85,\\n                    )\\n\\n                ax.set_xlabel(title)\\n                ax.set_ylabel(metric)\\n                ax.set_title(metric)\\n                ax.set_xticks(x)\\n                ax.set_xticklabels(bins_present, rotation=0)\\n                ax.legend(loc=\\\"best\\\")\\n                ax.set_ylim(bottom=0)\\n\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n        # ── Plot 2: Heatmap — stratum × strategy for R@1 ──\\n        for title, analysis, bin_order in [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            data_matrix = []\\n            for b in bins_present:\\n                row = []\\n                for s in STRATEGIES:\\n                    row.append(analysis[b].get(s, {}).get(\\\"R@1\\\", 0))\\n                data_matrix.append(row)\\n            data_matrix = np.array(data_matrix)\\n\\n            fig, ax = plt.subplots(figsize=(6, max(3, len(bins_present) * 0.8 + 1)))\\n            im = ax.imshow(data_matrix, cmap=\\\"YlOrRd\\\", aspect=\\\"auto\\\", vmin=0)\\n            ax.set_xticks(range(len(STRATEGIES)))\\n            ax.set_xticklabels([STRATEGY_LABELS[s] for s in STRATEGIES])\\n            ax.set_yticks(range(len(bins_present)))\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "d89af922-fc94-40ed-83fe-27968677a3b4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\ndef make_plots(\\\\n    repo_analysis: Dict,\\\\n    pool_analysis: Dict,\\\\n    sim_analysis: Dict,\\\\n    output_dir: str,\\\\n):\\\\n    import matplotlib\\\\n    matplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\n    import matplotlib.pyplot as plt\\\\n    from matplotlib.backends.backend_pdf import PdfPages\\\\n\\\\n    plt.rcParams.update({\\\\n        \\\\\\\"font.size\\\\\\\": 11,\\\\n        \\\\\\\"axes.titlesize\\\\\\\": 13,\\\\n        \\\\\\\"axes.labelsize\\\\\\\": 12,\\\\n        \\\\\\\"xtick.labelsize\\\\\\\": 10,\\\\n        \\\\\\\"ytick.labelsize\\\\\\\": 10,\\\\n        \\\\\\\"legend.fontsize\\\\\\\": 10,\\\\n        \\\\\\\"figure.dpi\\\\\\\": 150,\\\\n        \\\\\\\"savefig.dpi\\\\\\\": 300,\\\\n        \\\\\\\"font.family\\\\\\\": \\\\\\\"sans-serif\\\\\\\",\\\\n    })\\\\n\\\\n    pdf_path = os.path.join(output_dir, \\\\\\\"stratified_plots.pdf\\\\\\\")\\\\n    with PdfPages(pdf_path) as pdf:\\\\n        # ── Plot 1: Grouped bar chart per stratum dimension ──\\\\n        for title, analysis, bin_order in [\\\\n            (\\\\\\\"Repo Size\\\\\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Candidate Pool Size\\\\\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Query-Positive Similarity\\\\\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\\\n        ]:\\\\n            bins_present = [b for b in bin_order if b in analysis]\\\\n            if not bins_present:\\\\n                continue\\\\n\\\\n            fig, axes = plt.subplots(1, 3, figsize=(15, 5))\\\\n            fig.suptitle(f\\\\\\\"Stratified by {title}\\\\\\\", fontweight=\\\\\\\"bold\\\\\\\", y=1.02)\\\\n\\\\n            for ax_idx, metric in enumerate([\\\\\\\"R@1\\\\\\\", \\\\\\\"R@5\\\\\\\", \\\\\\\"MRR\\\\\\\"]):\\\\n                ax = axes[ax_idx]\\\\n                x = np.arange(len(bins_present))\\\\n                width = 0.25\\\\n\\\\n                for i, strategy in enumerate(STRATEGIES):\\\\n                    vals = []\\\\n                    errs_lo = []\\\\n                    errs_hi = []\\\\n                    for b in bins_present:\\\\n                        m = analysis[b].get(strategy, {})\\\\n                        v = m.get(metric, 0)\\\\n                        ci = m.get(f\\\\\\\"{metric}_ci\\\\\\\", [v, v])\\\\n                        vals.append(v)\\\\n                        errs_lo.append(v - ci[0])\\\\n                        errs_hi.append(ci[1] - v)\\\\n\\\\n                    offset = (i - 1) * width\\\\n                    bars = ax.bar(\\\\n                        x + offset, vals, width,\\\\n                        label=STRATEGY_LABELS[strategy],\\\\n                        color=STRATEGY_COLORS[strategy],\\\\n                        yerr=[errs_lo, errs_hi],\\\\n                        capsize=3, alpha=0.85,\\\\n                    )\\\\n\\\\n                ax.set_xlabel(title)\\\\n                ax.set_ylabel(metric)\\\\n                ax.set_title(metric)\\\\n                ax.set_xticks(x)\\\\n                ax.set_xticklabels(bins_present, rotation=0)\\\\n                ax.legend(loc=\\\\\\\"best\\\\\\\")\\\\n                ax.set_ylim(bottom=0)\\\\n\\\\n            plt.tight_layout()\\\\n            pdf.savefig(fig, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n            plt.close(fig)\\\\n\\\\n        # ── Plot 2: Heatmap — stratum × strategy for R@1 ──\\\\n        for title, analysis, bin_order in [\\\\n            (\\\\\\\"Repo Size\\\\\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Pool Size\\\\\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\\\n            (\\\\\\\"Similarity\\\\\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\\\n        ]:\\\\n            bins_present = [b for b in bin_order if b in analysis]\\\\n            if not bins_present:\\\\n                continue\\\\n\\\\n            data_matrix = []\\\\n            for b in bins_present:\\\\n                row = []\\\\n                for s in STRATEGIES:\\\\n                    row.append(analysis[b].get(s, {}).get(\\\\\\\"R@1\\\\\\\", 0))\\\\n                data_matrix.append(row)\\\\n            data_matrix = np.array(data_matrix)\\\\n\\\\n            fig, ax = plt.subplots(figsize=(6, max(3, len(bins_present) * 0.8 + 1)))\\\\n            im = ax.imshow(data_matrix, cmap=\\\\\\\"YlOrRd\\\\\\\", aspect=\\\\\\\"auto\\\\\\\", vmin=0)\\\\n            ax.set_xticks(range(len(STRATEGIES)))\\\\n            ax.set_xticklabels([STRATEGY_LABELS[s] for s in STRATEGIES])\\\\n            ax.set_yticks(range(len(bins_present)))\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\ndef make_plots(\\n    repo_analysis: Dict,\\n    pool_analysis: Dict,\\n    sim_analysis: Dict,\\n    output_dir: str,\\n):\\n    import matplotlib\\n    matplotlib.use(\\\"Agg\\\")\\n    import matplotlib.pyplot as plt\\n    from matplotlib.backends.backend_pdf import PdfPages\\n\\n    plt.rcParams.update({\\n        \\\"font.size\\\": 11,\\n        \\\"axes.titlesize\\\": 13,\\n        \\\"axes.labelsize\\\": 12,\\n        \\\"xtick.labelsize\\\": 10,\\n        \\\"ytick.labelsize\\\": 10,\\n        \\\"legend.fontsize\\\": 10,\\n        \\\"figure.dpi\\\": 150,\\n        \\\"savefig.dpi\\\": 300,\\n        \\\"font.family\\\": \\\"sans-serif\\\",\\n    })\\n\\n    pdf_path = os.path.join(output_dir, \\\"stratified_plots.pdf\\\")\\n    with PdfPages(pdf_path) as pdf:\\n        # ── Plot 1: Grouped bar chart per stratum dimension ──\\n        for title, analysis, bin_order in [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Candidate Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Query-Positive Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            fig, axes = plt.subplots(1, 3, figsize=(15, 5))\\n            fig.suptitle(f\\\"Stratified by {title}\\\", fontweight=\\\"bold\\\", y=1.02)\\n\\n            for ax_idx, metric in enumerate([\\\"R@1\\\", \\\"R@5\\\", \\\"MRR\\\"]):\\n                ax = axes[ax_idx]\\n                x = np.arange(len(bins_present))\\n                width = 0.25\\n\\n                for i, strategy in enumerate(STRATEGIES):\\n                    vals = []\\n                    errs_lo = []\\n                    errs_hi = []\\n                    for b in bins_present:\\n                        m = analysis[b].get(strategy, {})\\n                        v = m.get(metric, 0)\\n                        ci = m.get(f\\\"{metric}_ci\\\", [v, v])\\n                        vals.append(v)\\n                        errs_lo.append(v - ci[0])\\n                        errs_hi.append(ci[1] - v)\\n\\n                    offset = (i - 1) * width\\n                    bars = ax.bar(\\n                        x + offset, vals, width,\\n                        label=STRATEGY_LABELS[strategy],\\n                        color=STRATEGY_COLORS[strategy],\\n                        yerr=[errs_lo, errs_hi],\\n                        capsize=3, alpha=0.85,\\n                    )\\n\\n                ax.set_xlabel(title)\\n                ax.set_ylabel(metric)\\n                ax.set_title(metric)\\n                ax.set_xticks(x)\\n                ax.set_xticklabels(bins_present, rotation=0)\\n                ax.legend(loc=\\\"best\\\")\\n                ax.set_ylim(bottom=0)\\n\\n            plt.tight_layout()\\n            pdf.savefig(fig, bbox_inches=\\\"tight\\\")\\n            plt.close(fig)\\n\\n        # ── Plot 2: Heatmap — stratum × strategy for R@1 ──\\n        for title, analysis, bin_order in [\\n            (\\\"Repo Size\\\", repo_analysis, list(REPO_SIZE_BINS.keys())),\\n            (\\\"Pool Size\\\", pool_analysis, list(POOL_SIZE_BINS.keys())),\\n            (\\\"Similarity\\\", sim_analysis, list(SIMILARITY_BINS.keys())),\\n        ]:\\n            bins_present = [b for b in bin_order if b in analysis]\\n            if not bins_present:\\n                continue\\n\\n            data_matrix = []\\n            for b in bins_present:\\n                row = []\\n                for s in STRATEGIES:\\n                    row.append(analysis[b].get(s, {}).get(\\\"R@1\\\", 0))\\n                data_matrix.append(row)\\n            data_matrix = np.array(data_matrix)\\n\\n            fig, ax = plt.subplots(figsize=(6, max(3, len(bins_present) * 0.8 + 1)))\\n            im = ax.imshow(data_matrix, cmap=\\\"YlOrRd\\\", aspect=\\\"auto\\\", vmin=0)\\n            ax.set_xticks(range(len(STRATEGIES)))\\n            ax.set_xticklabels([STRATEGY_LABELS[s] for s in STRATEGIES])\\n            ax.set_yticks(range(len(bins_present)))\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 174_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01T75MPcUPm9yfiJWPFrzpdE`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "head -n 781 /root/structfuse/evaluation/analyze_stratified.py | tail -n 170"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "8df386bc-15fa-4a56-889a-8c0f0bd999ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5XU9Rg1WLKUkDBB1UH43T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2751,
      "cache_read_input_tokens": 84062,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2751
      },
      "output_tokens": 68,
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

_source line 175 · 2026-05-14T20:22:39.779Z_

<details><summary>↩ Tool result · `toolu_01T75MPcUPm9yfiJWPFrzpdE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    print(f\\\"  Summary CSV saved to {output_path}\\\", flush=True)\\n\\n\\n# ── Main ─────────────────────────────────────────────────────────────\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Stratified analysis of M2 strategies by data strata\\\"\\n    )\\n    parser.add_argument(\\\"--predictions-dir\\\", default=None,\\n                        help=\\\"Dir with per-strategy prediction JSONs (from eval_retrieval.py)\\\")\\n    parser.add_argument(\\\"--checkpoints-dir\\\", default=None,\\n                        help=\\\"Dir containing strategy/seed checkpoint subdirs\\\")\\n    parser.add_argument(\\\"--val-data-dir\\\", default=None,\\n                        help=\\\"Dir with val_&lt;strategy>_s&lt;seed>.jsonl files\\\")\\n    parser.add_argument(\\\"--m1-data\\\", required=True,\\n                        help=\\\"Path to M1 all.jsonl\\\")\\n    parser.add_argument(\\\"--output-dir\\\", required=True)\\n    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\",\\n                        help=\\\"Use mock predictions to validate pipeline\\\")\\n    parser.add_argument(\\\"--seeds\\\", default=\\\"42,43,44\\\",\\n                        help=\\\"Comma-separated seed list\\\")\\n    parser.add_argument(\\\"--device\\\", default=\\\"cuda\\\")\\n    parser.add_argument(\\\"--max-seq-length\\\", type=int, default=2048)\\n    parser.add_argument(\\\"--n-bootstrap\\\", type=int, default=1000)\\n    parser.add_argument(\\\"--repo-size-bins\\\", default=None,\\n                        help='JSON dict: {\\\"small\\\": [0,50], \\\"medium\\\": [50,200], ...}')\\n    parser.add_argument(\\\"--pool-size-bins\\\", default=None,\\n                        help='JSON dict for pool size bins')\\n    parser.add_argument(\\\"--sim-bins\\\", default=None,\\n                        help='JSON dict for similarity bins')\\n    args = parser.parse_args()\\n\\n    seeds = [int(s) for s in args.seeds.split(\\\",\\\")]\\n    os.makedirs(args.output_dir, exist_ok=True)\\n\\n    # Custom bins\\n    if args.repo_size_bins:\\n        custom = json.loads(args.repo_size_bins)\\n        REPO_SIZE_BINS.clear()\\n        REPO_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\n    if args.pool_size_bins:\\n        custom = json.loads(args.pool_size_bins)\\n        POOL_SIZE_BINS.clear()\\n        POOL_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\n    if args.sim_bins:\\n        custom = json.loads(args.sim_bins)\\n        SIMILARITY_BINS.clear()\\n        SIMILARITY_BINS.update({k: tuple(v) for k, v in custom.items()})\\n\\n    # Load M1 metadata\\n    print(f\\\"Loading M1 metadata from {args.m1_data}...\\\", flush=True)\\n    inst_to_repo, repo_counts = load_m1_metadata(args.m1_data)\\n    print(f\\\"  {len(inst_to_repo)} instances, {len(repo_counts)} repos\\\", flush=True)\\n\\n    # Determine val data directory\\n    val_dir = args.val_data_dir\\n    if val_dir is None and args.predictions_dir is None and not args.dry_run:\\n        val_dir = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\n    if val_dir is None and args.dry_run:\\n        val_dir = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\n\\n    # Collect per-instance results: {strategy: {seed: [results]}}\\n    all_results: Dict[str, Dict[int, List[Dict]]] = defaultdict(dict)\\n\\n    for strategy in STRATEGIES:\\n        for seed in seeds:\\n            val_file = os.path.join(val_dir, f\\\"val_{strategy}_s{seed}.jsonl\\\") if val_dir else None\\n\\n            if val_file and os.path.exists(val_file):\\n                print(f\\\"Loading val data: {strategy} seed={seed}...\\\", flush=True)\\n                lite = args.dry_run or (args.predictions_dir is not None)\\n                val_samples = load_val_samples(val_file, lite=lite)\\n            else:\\n                print(f\\\"  [WARN] Val file not found: {val_file}, skipping\\\", flush=True)\\n                continue\\n\\n            if args.dry_run:\\n                print(f\\\"  Generating mock predictions: {strategy} seed={seed}\\\", flush=True)\\n                results = mock_predictions(val_samples, strategy, seed)\\n            elif args.predictions_dir:\\n                pred_pattern = os.path.join(\\n                    args.predictions_dir, f\\\"*{strategy}*s{seed}*.json\\\"\\n                )\\n                import glob\\n                pred_files = glob.glob(pred_pattern)\\n                if pred_files:\\n                    print(f\\\"  Loading predictions: {pred_files[0]}\\\", flush=True)\\n                    results = load_predictions(pred_files[0], val_samples)\\n                else:\\n                    print(f\\\"  [WARN] No prediction file matching {pred_pattern}\\\", flush=True)\\n                    continue\\n            elif args.checkpoints_dir:\\n                ckpt_dir = os.path.join(\\n                    args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\", \\\"best\\\"\\n                )\\n                if not os.path.exists(ckpt_dir):\\n                    ckpt_dir = os.path.join(args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\")\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "4b3a5e36-5904-426a-b166-8c24044fb6ac",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    print(f\\\\\\\"  Summary CSV saved to {output_path}\\\\\\\", flush=True)\\\\n\\\\n\\\\n# ── Main ─────────────────────────────────────────────────────────────\\\\n\\\\ndef main():\\\\n    parser = argparse.ArgumentParser(\\\\n        description=\\\\\\\"Stratified analysis of M2 strategies by data strata\\\\\\\"\\\\n    )\\\\n    parser.add_argument(\\\\\\\"--predictions-dir\\\\\\\", default=None,\\\\n                        help=\\\\\\\"Dir with per-strategy prediction JSONs (from eval_retrieval.py)\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--checkpoints-dir\\\\\\\", default=None,\\\\n                        help=\\\\\\\"Dir containing strategy/seed checkpoint subdirs\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--val-data-dir\\\\\\\", default=None,\\\\n                        help=\\\\\\\"Dir with val_&lt;strategy>_s&lt;seed>.jsonl files\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--m1-data\\\\\\\", required=True,\\\\n                        help=\\\\\\\"Path to M1 all.jsonl\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--output-dir\\\\\\\", required=True)\\\\n    parser.add_argument(\\\\\\\"--dry-run\\\\\\\", action=\\\\\\\"store_true\\\\\\\",\\\\n                        help=\\\\\\\"Use mock predictions to validate pipeline\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--seeds\\\\\\\", default=\\\\\\\"42,43,44\\\\\\\",\\\\n                        help=\\\\\\\"Comma-separated seed list\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--device\\\\\\\", default=\\\\\\\"cuda\\\\\\\")\\\\n    parser.add_argument(\\\\\\\"--max-seq-length\\\\\\\", type=int, default=2048)\\\\n    parser.add_argument(\\\\\\\"--n-bootstrap\\\\\\\", type=int, default=1000)\\\\n    parser.add_argument(\\\\\\\"--repo-size-bins\\\\\\\", default=None,\\\\n                        help='JSON dict: {\\\\\\\"small\\\\\\\": [0,50], \\\\\\\"medium\\\\\\\": [50,200], ...}')\\\\n    parser.add_argument(\\\\\\\"--pool-size-bins\\\\\\\", default=None,\\\\n                        help='JSON dict for pool size bins')\\\\n    parser.add_argument(\\\\\\\"--sim-bins\\\\\\\", default=None,\\\\n                        help='JSON dict for similarity bins')\\\\n    args = parser.parse_args()\\\\n\\\\n    seeds = [int(s) for s in args.seeds.split(\\\\\\\",\\\\\\\")]\\\\n    os.makedirs(args.output_dir, exist_ok=True)\\\\n\\\\n    # Custom bins\\\\n    if args.repo_size_bins:\\\\n        custom = json.loads(args.repo_size_bins)\\\\n        REPO_SIZE_BINS.clear()\\\\n        REPO_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\\\n    if args.pool_size_bins:\\\\n        custom = json.loads(args.pool_size_bins)\\\\n        POOL_SIZE_BINS.clear()\\\\n        POOL_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\\\n    if args.sim_bins:\\\\n        custom = json.loads(args.sim_bins)\\\\n        SIMILARITY_BINS.clear()\\\\n        SIMILARITY_BINS.update({k: tuple(v) for k, v in custom.items()})\\\\n\\\\n    # Load M1 metadata\\\\n    print(f\\\\\\\"Loading M1 metadata from {args.m1_data}...\\\\\\\", flush=True)\\\\n    inst_to_repo, repo_counts = load_m1_metadata(args.m1_data)\\\\n    print(f\\\\\\\"  {len(inst_to_repo)} instances, {len(repo_counts)} repos\\\\\\\", flush=True)\\\\n\\\\n    # Determine val data directory\\\\n    val_dir = args.val_data_dir\\\\n    if val_dir is None and args.predictions_dir is None and not args.dry_run:\\\\n        val_dir = \\\\\\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\\\\\"\\\\n    if val_dir is None and args.dry_run:\\\\n        val_dir = \\\\\\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\\\\\"\\\\n\\\\n    # Collect per-instance results: {strategy: {seed: [results]}}\\\\n    all_results: Dict[str, Dict[int, List[Dict]]] = defaultdict(dict)\\\\n\\\\n    for strategy in STRATEGIES:\\\\n        for seed in seeds:\\\\n            val_file = os.path.join(val_dir, f\\\\\\\"val_{strategy}_s{seed}.jsonl\\\\\\\") if val_dir else None\\\\n\\\\n            if val_file and os.path.exists(val_file):\\\\n                print(f\\\\\\\"Loading val data: {strategy} seed={seed}...\\\\\\\", flush=True)\\\\n                lite = args.dry_run or (args.predictions_dir is not None)\\\\n                val_samples = load_val_samples(val_file, lite=lite)\\\\n            else:\\\\n                print(f\\\\\\\"  [WARN] Val file not found: {val_file}, skipping\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            if args.dry_run:\\\\n                print(f\\\\\\\"  Generating mock predictions: {strategy} seed={seed}\\\\\\\", flush=True)\\\\n                results = mock_predictions(val_samples, strategy, seed)\\\\n            elif args.predictions_dir:\\\\n                pred_pattern = os.path.join(\\\\n                    args.predictions_dir, f\\\\\\\"*{strategy}*s{seed}*.json\\\\\\\"\\\\n                )\\\\n                import glob\\\\n                pred_files = glob.glob(pred_pattern)\\\\n                if pred_files:\\\\n                    print(f\\\\\\\"  Loading predictions: {pred_files[0]}\\\\\\\", flush=True)\\\\n                    results = load_predictions(pred_files[0], val_samples)\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] No prediction file matching {pred_pattern}\\\\\\\", flush=True)\\\\n                    continue\\\\n            elif args.checkpoints_dir:\\\\n                ckpt_dir = os.path.join(\\\\n                    args.checkpoints_dir, f\\\\\\\"{strategy}_s{seed}\\\\\\\", \\\\\\\"best\\\\\\\"\\\\n                )\\\\n                if not os.path.exists(ckpt_dir):\\\\n                    ckpt_dir = os.path.join(args.checkpoints_dir, f\\\\\\\"{strategy}_s{seed}\\\\\\\")\\\\n                if os.path.exists(ckpt_dir):\\\\n                    print(f\\\\\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    results = reeval_checkpoint(\\\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\\\n                    )\\\\n                else:\\\\n                    print(f\\\\\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\\\\\", flush=True)\\\\n                    continue\\\\n            else:\\\\n                print(\\\\\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\\\\\", flush=True)\\\\n                continue\\\\n\\\\n            # Assign strata\\\\n            results = assign_strata(results, inst_to_repo, repo_counts)\\\\n\\\\n            # For dry-run or model-based: compute text similarity for sim_bin\\\\n            if args.dry_run:\\\\n                for r, s in zip(results, val_samples):\\\\n                    tsim = text_similarity(s[\\\\\\\"query_tokens\\\\\\\"][:500], s[\\\\\\\"pos_tokens\\\\\\\"][:500])\\\\n                    r[\\\\\\\"sim_bin\\\\\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\\\n\\\\n            all_results[strategy][seed] = results\\\\n            print(f\\\\\\\"  -> {len(results)} instances\\\\\\\", flush=True)\\\\n\\\\n    # Run stratified analysis\\\\n    print(\\\\\\\"\\\\\\\\nRunning stratified analysis...\\\\\\\", flush=True)\\\\n    repo_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"repo_size_bin\\\\\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    pool_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"pool_size_bin\\\\\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n    sim_analysis = run_stratified_analysis(\\\\n        all_results, \\\\\\\"sim_bin\\\\\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\\\n    )\\\\n\\\\n    # Save JSON\\\\n    full_results = {\\\\n        \\\\\\\"config\\\\\\\": {\\\\n            \\\\\\\"strategies\\\\\\\": STRATEGIES,\\\\n            \\\\\\\"seeds\\\\\\\": seeds,\\\\n            \\\\\\\"repo_size_bins\\\\\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\\\n            \\\\\\\"pool_size_bins\\\\\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\\\n            \\\\\\\"similarity_bins\\\\\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\\\n            \\\\\\\"n_bootstrap\\\\\\\": args.n_bootstrap,\\\\n            \\\\\\\"dry_run\\\\\\\": args.dry_run,\\\\n        },\\\\n        \\\\\\\"by_repo_size\\\\\\\": repo_analysis,\\\\n        \\\\\\\"by_pool_size\\\\\\\": pool_analysis,\\\\n        \\\\\\\"by_similarity\\\\\\\": sim_analysis,\\\\n    }\\\\n\\\\n    json_path = os.path.join(args.output_dir, \\\\\\\"stratified_results.json\\\\\\\")\\\\n    with open(json_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\\\n    print(f\\\\\\\"  Results JSON saved to {json_path}\\\\\\\", flush=True)\\\\n\\\\n    # CSV summary\\\\n    csv_path = os.path.join(args.output_dir, \\\\\\\"stratified_summary.csv\\\\\\\")\\\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path)\\\\n\\\\n    # Plots\\\\n    try:\\\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir)\\\\n    except Exception as e:\\\\n        print(f\\\\\\\"  [WARN] Plot generation failed: {e}\\\\\\\", flush=True)\\\\n\\\\n    print(\\\\\\\"\\\\\\\\nDone.\\\\\\\", flush=True)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    print(f\\\"  Summary CSV saved to {output_path}\\\", flush=True)\\n\\n\\n# ── Main ─────────────────────────────────────────────────────────────\\n\\ndef main():\\n    parser = argparse.ArgumentParser(\\n        description=\\\"Stratified analysis of M2 strategies by data strata\\\"\\n    )\\n    parser.add_argument(\\\"--predictions-dir\\\", default=None,\\n                        help=\\\"Dir with per-strategy prediction JSONs (from eval_retrieval.py)\\\")\\n    parser.add_argument(\\\"--checkpoints-dir\\\", default=None,\\n                        help=\\\"Dir containing strategy/seed checkpoint subdirs\\\")\\n    parser.add_argument(\\\"--val-data-dir\\\", default=None,\\n                        help=\\\"Dir with val_&lt;strategy>_s&lt;seed>.jsonl files\\\")\\n    parser.add_argument(\\\"--m1-data\\\", required=True,\\n                        help=\\\"Path to M1 all.jsonl\\\")\\n    parser.add_argument(\\\"--output-dir\\\", required=True)\\n    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\",\\n                        help=\\\"Use mock predictions to validate pipeline\\\")\\n    parser.add_argument(\\\"--seeds\\\", default=\\\"42,43,44\\\",\\n                        help=\\\"Comma-separated seed list\\\")\\n    parser.add_argument(\\\"--device\\\", default=\\\"cuda\\\")\\n    parser.add_argument(\\\"--max-seq-length\\\", type=int, default=2048)\\n    parser.add_argument(\\\"--n-bootstrap\\\", type=int, default=1000)\\n    parser.add_argument(\\\"--repo-size-bins\\\", default=None,\\n                        help='JSON dict: {\\\"small\\\": [0,50], \\\"medium\\\": [50,200], ...}')\\n    parser.add_argument(\\\"--pool-size-bins\\\", default=None,\\n                        help='JSON dict for pool size bins')\\n    parser.add_argument(\\\"--sim-bins\\\", default=None,\\n                        help='JSON dict for similarity bins')\\n    args = parser.parse_args()\\n\\n    seeds = [int(s) for s in args.seeds.split(\\\",\\\")]\\n    os.makedirs(args.output_dir, exist_ok=True)\\n\\n    # Custom bins\\n    if args.repo_size_bins:\\n        custom = json.loads(args.repo_size_bins)\\n        REPO_SIZE_BINS.clear()\\n        REPO_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\n    if args.pool_size_bins:\\n        custom = json.loads(args.pool_size_bins)\\n        POOL_SIZE_BINS.clear()\\n        POOL_SIZE_BINS.update({k: tuple(v) for k, v in custom.items()})\\n    if args.sim_bins:\\n        custom = json.loads(args.sim_bins)\\n        SIMILARITY_BINS.clear()\\n        SIMILARITY_BINS.update({k: tuple(v) for k, v in custom.items()})\\n\\n    # Load M1 metadata\\n    print(f\\\"Loading M1 metadata from {args.m1_data}...\\\", flush=True)\\n    inst_to_repo, repo_counts = load_m1_metadata(args.m1_data)\\n    print(f\\\"  {len(inst_to_repo)} instances, {len(repo_counts)} repos\\\", flush=True)\\n\\n    # Determine val data directory\\n    val_dir = args.val_data_dir\\n    if val_dir is None and args.predictions_dir is None and not args.dry_run:\\n        val_dir = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\n    if val_dir is None and args.dry_run:\\n        val_dir = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\n\\n    # Collect per-instance results: {strategy: {seed: [results]}}\\n    all_results: Dict[str, Dict[int, List[Dict]]] = defaultdict(dict)\\n\\n    for strategy in STRATEGIES:\\n        for seed in seeds:\\n            val_file = os.path.join(val_dir, f\\\"val_{strategy}_s{seed}.jsonl\\\") if val_dir else None\\n\\n            if val_file and os.path.exists(val_file):\\n                print(f\\\"Loading val data: {strategy} seed={seed}...\\\", flush=True)\\n                lite = args.dry_run or (args.predictions_dir is not None)\\n                val_samples = load_val_samples(val_file, lite=lite)\\n            else:\\n                print(f\\\"  [WARN] Val file not found: {val_file}, skipping\\\", flush=True)\\n                continue\\n\\n            if args.dry_run:\\n                print(f\\\"  Generating mock predictions: {strategy} seed={seed}\\\", flush=True)\\n                results = mock_predictions(val_samples, strategy, seed)\\n            elif args.predictions_dir:\\n                pred_pattern = os.path.join(\\n                    args.predictions_dir, f\\\"*{strategy}*s{seed}*.json\\\"\\n                )\\n                import glob\\n                pred_files = glob.glob(pred_pattern)\\n                if pred_files:\\n                    print(f\\\"  Loading predictions: {pred_files[0]}\\\", flush=True)\\n                    results = load_predictions(pred_files[0], val_samples)\\n                else:\\n                    print(f\\\"  [WARN] No prediction file matching {pred_pattern}\\\", flush=True)\\n                    continue\\n            elif args.checkpoints_dir:\\n                ckpt_dir = os.path.join(\\n                    args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\", \\\"best\\\"\\n                )\\n                if not os.path.exists(ckpt_dir):\\n                    ckpt_dir = os.path.join(args.checkpoints_dir, f\\\"{strategy}_s{seed}\\\")\\n                if os.path.exists(ckpt_dir):\\n                    print(f\\\"  Re-evaluating checkpoint: {ckpt_dir}\\\", flush=True)\\n                    results = reeval_checkpoint(\\n                        ckpt_dir, val_samples, args.device, args.max_seq_length\\n                    )\\n                else:\\n                    print(f\\\"  [WARN] Checkpoint not found: {ckpt_dir}\\\", flush=True)\\n                    continue\\n            else:\\n                print(\\\"  [ERROR] No --dry-run, --predictions-dir, or --checkpoints-dir\\\", flush=True)\\n                continue\\n\\n            # Assign strata\\n            results = assign_strata(results, inst_to_repo, repo_counts)\\n\\n            # For dry-run or model-based: compute text similarity for sim_bin\\n            if args.dry_run:\\n                for r, s in zip(results, val_samples):\\n                    tsim = text_similarity(s[\\\"query_tokens\\\"][:500], s[\\\"pos_tokens\\\"][:500])\\n                    r[\\\"sim_bin\\\"] = _bin_value(tsim, SIMILARITY_BINS)\\n\\n            all_results[strategy][seed] = results\\n            print(f\\\"  -> {len(results)} instances\\\", flush=True)\\n\\n    # Run stratified analysis\\n    print(\\\"\\\\nRunning stratified analysis...\\\", flush=True)\\n    repo_analysis = run_stratified_analysis(\\n        all_results, \\\"repo_size_bin\\\", list(REPO_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    pool_analysis = run_stratified_analysis(\\n        all_results, \\\"pool_size_bin\\\", list(POOL_SIZE_BINS.keys()), args.n_bootstrap\\n    )\\n    sim_analysis = run_stratified_analysis(\\n        all_results, \\\"sim_bin\\\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\\n    )\\n\\n    # Save JSON\\n    full_results = {\\n        \\\"config\\\": {\\n            \\\"strategies\\\": STRATEGIES,\\n            \\\"seeds\\\": seeds,\\n            \\\"repo_size_bins\\\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\\n            \\\"pool_size_bins\\\": {k: list(v) for k, v in POOL_SIZE_BINS.items()},\\n            \\\"similarity_bins\\\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\\n            \\\"n_bootstrap\\\": args.n_bootstrap,\\n            \\\"dry_run\\\": args.dry_run,\\n        },\\n        \\\"by_repo_size\\\": repo_analysis,\\n        \\\"by_pool_size\\\": pool_analysis,\\n        \\\"by_similarity\\\": sim_analysis,\\n    }\\n\\n    json_path = os.path.join(args.output_dir, \\\"stratified_results.json\\\")\\n    with open(json_path, \\\"w\\\") as f:\\n        json.dump(full_results, f, indent=2, ensure_ascii=False)\\n    print(f\\\"  Results JSON saved to {json_path}\\\", flush=True)\\n\\n    # CSV summary\\n    csv_path = os.path.join(args.output_dir, \\\"stratified_summary.csv\\\")\\n    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path)\\n\\n    # Plots\\n    try:\\n        make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir)\\n    except Exception as e:\\n        print(f\\\"  [WARN] Plot generation failed: {e}\\\", flush=True)\\n\\n    print(\\\"\\\\nDone.\\\", flush=True)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 176_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture of the script. I need to create a patch that:

1. Adds `DATAFLOW_BINS` and `NEG_DIFFICULTY_BINS` constants
2. Adds `--dataflow-graph` argument
3. Fixes checkpoint path resolution to handle `best_by_recall_at_1` / `best_by_val_loss`
4. Adds dataflow edge counting and neg_difficulty proxy computation in `assign_strata()` or a new function
5. Adds the two new analysis runs in `main()`


6. Updates `write_summary_csv()` and `make_plots()` to include the new dimensions
7. Updates the JSON output to include the new dimensions

I'm thinking through the best approach to apply these changes—I could write a Python patch script using string replacements, or generate the full modified file directly. Since the file is quite large with mostly unchanged sections, I'll go with a targeted patch script that makes surgical modifications to the specific functions and sections that need updating.

Writing comprehensive patch script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "7568c4f0-e71d-4d57-aa1d-73b873f56ee0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfqZrteUyBkqk7rCNX9yVB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2938,
      "cache_read_input_tokens": 86813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2938
      },
      "output_tokens": 8,
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


### Assistant

_source line 177_

Now I'll write a patch script to add the two missing dimensions and fix the checkpoint path. I'll apply it via ssh_execute.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "4716d6fa-25b4-4002-a9a6-25b5498f621f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfqZrteUyBkqk7rCNX9yVB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2938,
      "cache_read_input_tokens": 86813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2938
      },
      "output_tokens": 8,
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

_source line 178_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_018yrSAzQkYSS1fGG3W1cWPk`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "cat > /tmp/patch_stratified.py << 'PATCHEOF'\nimport re\n\nfilepath = \"/root/structfuse/evaluation/analyze_stratified.py\"\nwith open(filepath) as f:\n    content = f.read()\n\n# 1. Add DATAFLOW_BINS and NEG_DIFFICULTY_QUARTILES after SIMILARITY_BINS block\nold_after_sim = '''SIMILARITY_BINS = {\n    \"low\": (0.0, 0.3),\n    \"medium\": (0.3, 0.6),\n    \"high\": (0.6, 1.01),\n}'''\n\nnew_after_sim = '''SIMILARITY_BINS = {\n    \"low\": (0.0, 0.3),\n    \"medium\": (0.3, 0.6),\n    \"high\": (0.6, 1.01),\n}\n\nDATAFLOW_BINS = {\n    \"sparse\": (0, 2),\n    \"moderate\": (2, 10),\n    \"rich\": (10, float(\"inf\")),\n}\n\nNEG_DIFFICULTY_QUARTILE_LABELS = [\"Q1_easy\", \"Q2\", \"Q3\", \"Q4_hard\"]'''\n\ncontent = content.replace(old_after_sim, new_after_sim)\n\n# 2. Add load_dataflow_edges function after load_m1_metadata\nold_val_loading = \"# ── Val data loading\"\nnew_val_loading = '''# ── Dataflow graph loading ────────────────────────────────────────────\n\ndef load_dataflow_edges(graph_path: str) -> Dict[str, int]:\n    \"\"\"Load dataflow graph and return {file_key: edge_count}.\"\"\"\n    with open(graph_path) as f:\n        graph = json.load(f)\n    return {k: len(v) for k, v in graph.items()}\n\n\n# ── Val data loading'''\n\ncontent = content.replace(old_val_loading, new_val_loading)\n\n# 3. Update assign_strata to accept dataflow_edges\nold_assign = '''def assign_strata(\n    results: List[Dict],\n    inst_to_repo: Dict[str, str],\n    repo_counts: Dict[str, int],\n) -> List[Dict]:\n    for r in results:\n        repo = inst_to_repo.get(r[\"instance_id\"], \"\")\n        rc = repo_counts.get(repo, 0)\n        r[\"repo\"] = repo\n        r[\"repo_size\"] = rc\n        r[\"repo_size_bin\"] = _bin_value(rc, REPO_SIZE_BINS)\n        r[\"pool_size_bin\"] = _bin_value(r[\"pool_size\"], POOL_SIZE_BINS)\n        r[\"sim_bin\"] = _bin_value(r[\"pos_sim\"], SIMILARITY_BINS)\n    return results'''\n\nnew_assign = '''def assign_strata(\n    results: List[Dict],\n    inst_to_repo: Dict[str, str],\n    repo_counts: Dict[str, int],\n    dataflow_edges: Optional[Dict[str, int]] = None,\n) -> List[Dict]:\n    for r in results:\n        repo = inst_to_repo.get(r[\"instance_id\"], \"\")\n        rc = repo_counts.get(repo, 0)\n        r[\"repo\"] = repo\n        r[\"repo_size\"] = rc\n        r[\"repo_size_bin\"] = _bin_value(rc, REPO_SIZE_BINS)\n        r[\"pool_size_bin\"] = _bin_value(r[\"pool_size\"], POOL_SIZE_BINS)\n        r[\"sim_bin\"] = _bin_value(r[\"pos_sim\"], SIMILARITY_BINS)\n        if dataflow_edges is not None:\n            ec = dataflow_edges.get(r[\"query_id\"], 0)\n            r[\"dataflow_edge_count\"] = ec\n            r[\"dataflow_bin\"] = _bin_value(ec, DATAFLOW_BINS)\n        else:\n            r[\"dataflow_bin\"] = \"unknown\"\n    return results\n\n\ndef assign_neg_difficulty_quartiles(\n    all_results: Dict[str, Dict[int, List[Dict]]],\n    val_samples_cache: Dict[str, List[Dict]],\n):\n    \"\"\"Compute text-overlap-based neg difficulty proxy and assign quartiles.\"\"\"\n    for strategy in list(all_results.keys()):\n        for seed in list(all_results[strategy].keys()):\n            results = all_results[strategy][seed]\n            cache_key = f\"{strategy}_s{seed}\"\n            samples = val_samples_cache.get(cache_key, [])\n            sample_map = {s[\"query_id\"]: s for s in samples}\n\n            margins = []\n            for r in results:\n                s = sample_map.get(r[\"query_id\"])\n                if s is None:\n                    margins.append(0.0)\n                    continue\n                q_toks = set(s.get(\"query_tokens\", \"\")[:1000].split())\n                p_toks = set(s.get(\"pos_tokens\", \"\")[:1000].split())\n                pos_overlap = len(q_toks & p_toks) / max(len(q_toks | p_toks), 1)\n                max_neg_overlap = 0.0\n                neg_cands = s.get(\"neg_candidates\", [])[:7]\n                cand_tokens = s.get(\"candidate_tokens\", {})\n                for neg_id in neg_cands:\n                    neg_text = cand_tokens.get(neg_id, \"\")\n                    if neg_text:\n                        n_toks = set(neg_text[:1000].split())\n                        ov = len(q_toks & n_toks) / max(len(q_toks | n_toks), 1)\n                        max_neg_overlap = max(max_neg_overlap, ov)\n                margin = pos_overlap - max_neg_overlap\n                margins.append(margin)\n                r[\"neg_difficulty_margin\"] = margin\n\n            if margins:\n                arr = np.array(margins)\n                q25, q50, q75 = np.percentile(arr, [25, 50, 75])\n                for r, m in zip(results, margins):\n                    if m <= q25:\n                        r[\"neg_difficulty_bin\"] = \"Q4_hard\"\n                    elif m <= q50:\n                        r[\"neg_difficulty_bin\"] = \"Q3\"\n                    elif m <= q75:\n                        r[\"neg_difficulty_bin\"] = \"Q2\"\n                    else:\n                        r[\"neg_difficulty_bin\"] = \"Q1_easy\"'''\n\ncontent = content.replace(old_assign, new_assign)\n\n# 4. Add --dataflow-graph argument\nold_sim_bins_arg = '''    parser.add_argument(\"--sim-bins\", default=None,\n                        help='JSON dict for similarity bins')'''\n\nnew_sim_bins_arg = '''    parser.add_argument(\"--sim-bins\", default=None,\n                        help='JSON dict for similarity bins')\n    parser.add_argument(\"--dataflow-graph\", default=None,\n                        help=\"Path to dataflow_graph.json for structural data availability dimension\")'''\n\ncontent = content.replace(old_sim_bins_arg, new_sim_bins_arg)\n\n# 5. Fix checkpoint path resolution — add best_by_recall_at_1 / best_by_val_loss\nold_ckpt = '''            elif args.checkpoints_dir:\n                ckpt_dir = os.path.join(\n                    args.checkpoints_dir, f\"{strategy}_s{seed}\", \"best\"\n                )\n                if not os.path.exists(ckpt_dir):\n                    ckpt_dir = os.path.join(args.checkpoints_dir, f\"{strategy}_s{seed}\")'''\n\nnew_ckpt = '''            elif args.checkpoints_dir:\n                base = os.path.join(args.checkpoints_dir, f\"{strategy}_s{seed}\")\n                ckpt_dir = None\n                for subdir in [\"best\", \"best_by_recall_at_1\", \"best_by_val_loss\"]:\n                    candidate = os.path.join(base, subdir)\n                    if os.path.exists(os.path.join(candidate, \"model.pt\")):\n                        ckpt_dir = candidate\n                        break\n                if ckpt_dir is None and os.path.exists(os.path.join(base, \"model.pt\")):\n                    ckpt_dir = base'''\n\ncontent = content.replace(old_ckpt, new_ckpt)\n\n# 6. Load dataflow graph in main, before the loop\nold_load_m1 = '''    # Load M1 metadata\n    print(f\"Loading M1 metadata from {args.m1_data}...\", flush=True)\n    inst_to_repo, repo_counts = load_m1_metadata(args.m1_data)\n    print(f\"  {len(inst_to_repo)} instances, {len(repo_counts)} repos\", flush=True)'''\n\nnew_load_m1 = '''    # Load M1 metadata\n    print(f\"Loading M1 metadata from {args.m1_data}...\", flush=True)\n    inst_to_repo, repo_counts = load_m1_metadata(args.m1_data)\n    print(f\"  {len(inst_to_repo)} instances, {len(repo_counts)} repos\", flush=True)\n\n    # Load dataflow graph if provided\n    dataflow_edges = None\n    if args.dataflow_graph and os.path.exists(args.dataflow_graph):\n        print(f\"Loading dataflow graph from {args.dataflow_graph}...\", flush=True)\n        dataflow_edges = load_dataflow_edges(args.dataflow_graph)\n        print(f\"  {len(dataflow_edges)} file entries\", flush=True)'''\n\ncontent = content.replace(old_load_m1, new_load_m1)\n\n# 7. Update assign_strata call to pass dataflow_edges + keep val_samples for neg_difficulty\nold_assign_call = '''            # Assign strata\n            results = assign_strata(results, inst_to_repo, repo_counts)'''\n\nnew_assign_call = '''            # Assign strata\n            results = assign_strata(results, inst_to_repo, repo_counts, dataflow_edges)'''\n\ncontent = content.replace(old_assign_call, new_assign_call)\n\n# 8. Add val_samples_cache and neg_difficulty computation before analysis runs\n# Also add new analysis dimensions\nold_all_results_line = '''            all_results[strategy][seed] = results\n            print(f\"  -> {len(results)} instances\", flush=True)\n\n    # Run stratified analysis'''\n\nnew_all_results_line = '''            all_results[strategy][seed] = results\n            val_samples_cache[f\"{strategy}_s{seed}\"] = val_samples\n            print(f\"  -> {len(results)} instances\", flush=True)\n\n    # Compute neg_difficulty quartiles (text-overlap proxy, CPU-safe)\n    print(\"Computing neg difficulty quartiles...\", flush=True)\n    assign_neg_difficulty_quartiles(all_results, val_samples_cache)\n\n    # Run stratified analysis'''\n\ncontent = content.replace(old_all_results_line, new_all_results_line)\n\n# 9. Add val_samples_cache initialization\nold_collect = '''    # Collect per-instance results: {strategy: {seed: [results]}}\n    all_results: Dict[str, Dict[int, List[Dict]]] = defaultdict(dict)'''\n\nnew_collect = '''    # Collect per-instance results: {strategy: {seed: [results]}}\n    all_results: Dict[str, Dict[int, List[Dict]]] = defaultdict(dict)\n    val_samples_cache: Dict[str, List[Dict]] = {}'''\n\ncontent = content.replace(old_collect, new_collect)\n\n# 10. Add new analysis runs after sim_analysis\nold_analysis_runs = '''    sim_analysis = run_stratified_analysis(\n        all_results, \"sim_bin\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\n    )\n\n    # Save JSON'''\n\nnew_analysis_runs = '''    sim_analysis = run_stratified_analysis(\n        all_results, \"sim_bin\", list(SIMILARITY_BINS.keys()), args.n_bootstrap\n    )\n\n    dataflow_analysis = {}\n    if dataflow_edges is not None:\n        dataflow_analysis = run_stratified_analysis(\n            all_results, \"dataflow_bin\", list(DATAFLOW_BINS.keys()), args.n_bootstrap\n        )\n\n    neg_diff_analysis = run_stratified_analysis(\n        all_results, \"neg_difficulty_bin\", NEG_DIFFICULTY_QUARTILE_LABELS, args.n_bootstrap\n    )\n\n    # Save JSON'''\n\ncontent = content.replace(old_analysis_runs, new_analysis_runs)\n\n# 11. Update JSON output to include new dimensions\nold_json_save = '''    full_results = {\n        \"config\": {\n            \"strategies\": STRATEGIES,\n            \"seeds\": seeds,\n            \"repo_size_bins\": {k: list(v) for k, v in REPO_SIZE_BINS.items()},\n            \"pool_size_bins\": {k: list(v) for k, v POOL_SIZE_BINS.items()},\n            \"similarity_bins\": {k: list(v) for k, v in SIMILARITY_BINS.items()},\n            \"n_bootstrap\": args.n_bootstrap,\n            \"dry_run\": args.dry_run,\n        },\n        \"by_repo_size\": repo_analysis,\n        \"by_pool_size\": pool_analysis,\n        \"by_similarity\": sim_analysis,\n    }'''\n\n# The above might not match exactly due to spacing. Let me try a more precise match.\nold_json_save = '''    full_results = {\n        \"config\": {'''\n\n# Actually let me do this differently - replace the full_results block more carefully\nold_full_results = '''        \"by_repo_size\": repo_analysis,\n        \"by_pool_size\": pool_analysis,\n        \"by_similarity\": sim_analysis,\n    }'''\n\nnew_full_results = '''        \"by_repo_size\": repo_analysis,\n        \"by_pool_size\": pool_analysis,\n        \"by_similarity\": sim_analysis,\n        \"by_dataflow\": dataflow_analysis,\n        \"by_neg_difficulty\": neg_diff_analysis,\n    }'''\n\ncontent = content.replace(old_full_results, new_full_results)\n\n# 12. Add dataflow_bins and neg_difficulty to config\nold_config_end = '''            \"n_bootstrap\": args.n_bootstrap,\n            \"dry_run\": args.dry_run,'''\n\nnew_config_end = '''            \"dataflow_bins\": {k: list(v) for k, v in DATAFLOW_BINS.items()},\n            \"neg_difficulty_quartiles\": NEG_DIFFICULTY_QUARTILE_LABELS,\n            \"n_bootstrap\": args.n_bootstrap,\n            \"dry_run\": args.dry_run,'''\n\ncontent = content.replace(old_config_end, new_config_end)\n\n# 13. Update write_summary_csv call\nold_csv_call = '    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path)'\nnew_csv_call = '    write_summary_csv(repo_analysis, pool_analysis, sim_analysis, csv_path, dataflow_analysis, neg_diff_analysis)'\ncontent = content.replace(old_csv_call, new_csv_call)\n\n# 14. Update write_summary_csv function signature and body\nold_csv_func = '''def write_summary_csv(\n    repo_analysis: Dict,\n    pool_analysis: Dict,\n    sim_analysis: Dict,\n    output_path: str,\n):\n    rows = []\n    for dim_name, analysis, bin_order in [\n        (\"repo_size\", repo_analysis, list(REPO_SIZE_BINS.keys())),\n        (\"pool_size\", pool_analysis, list(POOL_SIZE_BINS.keys())),\n        (\"similarity\", sim_analysis, list(SIMILARITY_BINS.keys())),\n    ]:'''\n\nnew_csv_func = '''def write_summary_csv(\n    repo_analysis: Dict,\n    pool_analysis: Dict,\n    sim_analysis: Dict,\n    output_path: str,\n    dataflow_analysis: Optional[Dict] = None,\n    neg_diff_analysis: Optional[Dict] = None,\n):\n    rows = []\n    dimensions = [\n        (\"repo_size\", repo_analysis, list(REPO_SIZE_BINS.keys())),\n        (\"pool_size\", pool_analysis, list(POOL_SIZE_BINS.keys())),\n        (\"similarity\", sim_analysis, list(SIMILARITY_BINS.keys())),\n    ]\n    if dataflow_analysis:\n        dimensions.append((\"dataflow\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\n    if neg_diff_analysis:\n        dimensions.append((\"neg_difficulty\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\n    for dim_name, analysis, bin_order in dimensions:'''\n\ncontent = content.replace(old_csv_func, new_csv_func)\n\n# 15. Update make_plots call\nold_plots_call = '    make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir)'\nnew_plots_call = '    make_plots(repo_analysis, pool_analysis, sim_analysis, args.output_dir, dataflow_analysis, neg_diff_analysis)'\ncontent = content.replace(old_plots_call, new_plots_call)\n\n# 16. Update make_plots function signature and add new dimensions to plot lists\nold_plots_func = '''def make_plots(\n    repo_analysis: Dict,\n    pool_analysis: Dict,\n    sim_analysis: Dict,\n    output_dir: str,\n):'''\n\nnew_plots_func = '''def make_plots(\n    repo_analysis: Dict,\n    pool_analysis: Dict,\n    sim_analysis: Dict,\n    output_dir: str,\n    dataflow_analysis: Optional[Dict] = None,\n    neg_diff_analysis: Optional[Dict] = None,\n):'''\n\ncontent = content.replace(old_plots_func, new_plots_func)\n\n# 17. Add new dimensions to the plot loops (grouped bar, heatmap, delta)\n# For Plot 1 (grouped bar)\nold_plot1_list = '''        for title, analysis, bin_order in [\n            (\"Repo Size\", repo_analysis, list(REPO_SIZE_BINS.keys())),\n            (\"Candidate Pool Size\", pool_analysis, list(POOL_SIZE_BINS.keys())),\n            (\"Query-Positive Similarity\", sim_analysis, list(SIMILARITY_BINS.keys())),\n        ]:'''\n\nnew_plot1_list = '''        plot_dims = [\n            (\"Repo Size\", repo_analysis, list(REPO_SIZE_BINS.keys())),\n            (\"Candidate Pool Size\", pool_analysis, list(POOL_SIZE_BINS.keys())),\n            (\"Query-Positive Similarity\", sim_analysis, list(SIMILARITY_BINS.keys())),\n        ]\n        if dataflow_analysis:\n            plot_dims.append((\"Dataflow Availability\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\n        if neg_diff_analysis:\n            plot_dims.append((\"Neg Difficulty Quartile\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\n        for title, analysis, bin_order in plot_dims:'''\n\ncontent = content.replace(old_plot1_list, new_plot1_list)\n\n# For Plot 2 (heatmap) and Plot 3 (delta), replace the hardcoded lists\nold_plot2_list = '''        for title, analysis, bin_order in [\n            (\"Repo Size\", repo_analysis, list(REPO_SIZE_BINS.keys())),\n            (\"Pool Size\", pool_analysis, list(POOL_SIZE_BINS.keys())),\n            (\"Similarity\", sim_analysis, list(SIMILARITY_BINS.keys())),\n        ]:\n            bins_present = [b for b in bin_order if b in analysis]\n            if not bins_present:\n                continue\n\n            data_matrix = []'''\n\nnew_plot2_list = '''        heatmap_dims = [\n            (\"Repo Size\", repo_analysis, list(REPO_SIZE_BINS.keys())),\n            (\"Pool Size\", pool_analysis, list(POOL_SIZE_BINS.keys())),\n            (\"Similarity\", sim_analysis, list(SIMILARITY_BINS.keys())),\n        ]\n        if dataflow_analysis:\n            heatmap_dims.append((\"Dataflow\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\n        if neg_diff_analysis:\n            heatmap_dims.append((\"Neg Difficulty\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\n        for title, analysis, bin_order in heatmap_dims:\n            bins_present = [b for b in bin_order if b in analysis]\n            if not bins_present:\n                continue\n\n            data_matrix = []'''\n\ncontent = content.replace(old_plot2_list, new_plot2_list)\n\n# Plot 3 (delta trends)\nold_plot3_list = '''        for title, analysis, bin_order in [\n            (\"Repo Size\", repo_analysis, list(REPO_SIZE_BINS.keys())),\n            (\"Pool Size\", pool_analysis, list(POOL_SIZE_BINS.keys())),\n            (\"Similarity\", sim_analysis, list(SIMILARITY_BINS.keys())),\n        ]:\n            bins_present = [b for b in bin_order if b in analysis]\n            if not bins_present:\n                continue\n\n            fig, ax = plt.subplots(figsize=(8, 5))'''\n\nnew_plot3_list = '''        delta_dims = [\n            (\"Repo Size\", repo_analysis, list(REPO_SIZE_BINS.keys())),\n            (\"Pool Size\", pool_analysis, list(POOL_SIZE_BINS.keys())),\n            (\"Similarity\", sim_analysis, list(SIMILARITY_BINS.keys())),\n        ]\n        if dataflow_analysis:\n            delta_dims.append((\"Dataflow\", dataflow_analysis, list(DATAFLOW_BINS.keys())))\n        if neg_diff_analysis:\n            delta_dims.append((\"Neg Difficulty\", neg_diff_analysis, NEG_DIFFICULTY_QUARTILE_LABELS))\n        for title, analysis, bin_order in delta_dims:\n            bins_present = [b for b in bin_order if b in analysis]\n            if not bins_present:\n                continue\n\n            fig, ax = plt.subplots(figsize=(8, 5))'''\n\ncontent = content.replace(old_plot3_list, new_plot3_list)\n\n# 18. Also need to load val data with full candidate_tokens for neg_difficulty (not lite)\n# Change the lite condition: if we need neg_difficulty, we need full data\nold_lite = '''                lite = args.dry_run or (args.predictions_dir is not None)'''\nnew_lite = '''                lite = args.predictions_dir is not None'''\ncontent = content.replace(old_lite, new_lite)\n\nwith open(filepath, \"w\") as f:\n    f.write(content)\n\nprint(\"Patch applied successfully\")\n\n# Verify line count\nwith open(filepath) as f:\n    lines = f.readlines()\nprint(f\"New line count: {len(lines)}\")\nPATCHEOF\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 /tmp/patch_stratified.py\n",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "c5683358-0b27-4cf8-b721-c85ed513f666",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KfqZrteUyBkqk7rCNX9yVB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2938,
      "cache_read_input_tokens": 86813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2938
      },
      "output_tokens": 8,
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

_source line 179 · 2026-05-14T20:23:54.683Z_

<details><summary>↩ Tool result · `toolu_018yrSAzQkYSS1fGG3W1cWPk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Patch applied successfully\\nNew line count: 910\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "8bb24591-d719-40a0-9a6e-19dbce40053d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Patch applied successfully\\\\nNew line count: 910\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Patch applied successfully\\nNew line count: 910\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 180_

补丁应用成功 (781→910 行)。现在验证修改后的脚本能否通过 dry-run 加上 dataflow graph。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "49793954-8b0f-43d4-b9c1-44d8dfa6edf2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196a4w9YuKfnXePnNhjfwch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6595,
      "cache_read_input_tokens": 89751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6595
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

_source line 181_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_013jZg4QdJ4shV2EJankQaaV`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/structfuse && python3 evaluation/analyze_stratified.py \\\n  --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \\\n  --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data \\\n  --dataflow-graph /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json \\\n  --output-dir /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2 \\\n  --dry-run \\\n  --seeds 42 \\\n  --n-bootstrap 200\n",
  "warn": true,
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "21ba5fd2-0911-4d21-b7cc-2adb03ea957b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196a4w9YuKfnXePnNhjfwch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6595,
      "cache_read_input_tokens": 89751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6595
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

_source line 182 · 2026-05-14T20:24:20.500Z_

<details><summary>↩ Tool result · `toolu_013jZg4QdJ4shV2EJankQaaV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading M1 metadata from /root/autodl-tmp/structfuse/full_m1_data/all.jsonl...\\n  44173 instances, 123 repos\\nLoading dataflow graph from /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json...\\n  376069 file entries\\nLoading val data: random seed=42...\\n  Generating mock predictions: random seed=42\\n  -> 2980 instances\\nLoading val data: embedding_distance seed=42...\\n  Generating mock predictions: embedding_distance seed=42\\n  -> 2980 instances\\nLoading val data: dataflow_aware seed=42...\\n  Generating mock predictions: dataflow_aware seed=42\\n  -> 2980 instances\\nComputing neg difficulty quartiles...\\n\\nRunning stratified analysis...\\n  Results JSON saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_results.json\\n  Summary CSV saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_summary.csv\\n  Plots saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_plots.pdf\\n\\nDone.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 17.77}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "9af3bb21-3ca8-41a0-a781-c66e3734355f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Loading M1 metadata from /root/autodl-tmp/structfuse/full_m1_data/all.jsonl...\\\\n  44173 instances, 123 repos\\\\nLoading dataflow graph from /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json...\\\\n  376069 file entries\\\\nLoading val data: random seed=42...\\\\n  Generating mock predictions: random seed=42\\\\n  -> 2980 instances\\\\nLoading val data: embedding_distance seed=42...\\\\n  Generating mock predictions: embedding_distance seed=42\\\\n  -> 2980 instances\\\\nLoading val data: dataflow_aware seed=42...\\\\n  Generating mock predictions: dataflow_aware seed=42\\\\n  -> 2980 instances\\\\nComputing neg difficulty quartiles...\\\\n\\\\nRunning stratified analysis...\\\\n  Results JSON saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_results.json\\\\n  Summary CSV saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_summary.csv\\\\n  Plots saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_plots.pdf\\\\n\\\\nDone.\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 17.77}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Loading M1 metadata from /root/autodl-tmp/structfuse/full_m1_data/all.jsonl...\\n  44173 instances, 123 repos\\nLoading dataflow graph from /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json...\\n  376069 file entries\\nLoading val data: random seed=42...\\n  Generating mock predictions: random seed=42\\n  -> 2980 instances\\nLoading val data: embedding_distance seed=42...\\n  Generating mock predictions: embedding_distance seed=42\\n  -> 2980 instances\\nLoading val data: dataflow_aware seed=42...\\n  Generating mock predictions: dataflow_aware seed=42\\n  -> 2980 instances\\nComputing neg difficulty quartiles...\\n\\nRunning stratified analysis...\\n  Results JSON saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_results.json\\n  Summary CSV saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_summary.csv\\n  Plots saved to /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_plots.pdf\\n\\nDone.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 17.77}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 183_

5 维度全部通过。检查输出确认新维度数据正确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "0a5b06bf-fe34-4f92-847d-95ad0036d3d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRf6mSVisKJ29ieKTbsCkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 882,
      "cache_read_input_tokens": 96346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 882
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

_source line 184_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01AxWYm3M7Pw2ZUxzg7W2DV6`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_results.json') as f:\n    data = json.load(f)\nprint('Top-level keys:', list(data.keys()))\nprint()\nfor dim in ['by_dataflow', 'by_neg_difficulty']:\n    strata = list(data[dim].keys())\n    print(f'{dim}: strata = {strata}')\n    for s in strata:\n        strategies = list(data[dim][s].keys())\n        for st in ['random', 'embedding_distance']:\n            m = data[dim][s].get(st, {})\n            if m:\n                print(f'  {s}/{st}: R@1={m[\\\"R@1\\\"]:.4f} R@5={m[\\\"R@5\\\"]:.4f} MRR={m[\\\"MRR\\\"]:.4f} n={m[\\\"count\\\"]}')\n    print()\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "269bb6a6-a898-4142-8b3d-6f62e741f0e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRf6mSVisKJ29ieKTbsCkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 882,
      "cache_read_input_tokens": 96346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 882
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

_source line 185 · 2026-05-14T20:24:29.071Z_

<details><summary>↩ Tool result · `toolu_01AxWYm3M7Pw2ZUxzg7W2DV6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Top-level keys: ['config', 'by_repo_size', 'by_pool_size', 'by_similarity', 'by_dataflow', 'by_neg_difficulty']\\n\\nby_dataflow: strata = ['sparse', 'moderate', 'rich']\\n  sparse/random: R@1=0.0336 R@5=0.1624 MRR=0.1234 n=1546\\n  sparse/embedding_distance: R@1=0.0880 R@5=0.3325 MRR=0.2176 n=1546\\n  moderate/random: R@1=0.0361 R@5=0.1687 MRR=0.1343 n=498\\n  moderate/embedding_distance: R@1=0.0964 R@5=0.3916 MRR=0.2456 n=498\\n  rich/random: R@1=0.0128 R@5=0.1047 MRR=0.0868 n=936\\n  rich/embedding_distance: R@1=0.0502 R@5=0.2500 MRR=0.1667 n=936\\n\\nby_neg_difficulty: strata = ['Q1_easy', 'Q2', 'Q3', 'Q4_hard']\\n  Q1_easy/random: R@1=0.0377 R@5=0.1604 MRR=0.1241 n=742\\n  Q1_easy/embedding_distance: R@1=0.0822 R@5=0.3275 MRR=0.2101 n=742\\n  Q2/random: R@1=0.0308 R@5=0.1325 MRR=0.1120 n=747\\n  Q2/embedding_distance: R@1=0.0763 R@5=0.3240 MRR=0.2069 n=747\\n  Q3/random: R@1=0.0242 R@5=0.1248 MRR=0.1057 n=745\\n  Q3/embedding_distance: R@1=0.0765 R@5=0.3128 MRR=0.2074 n=745\\n  Q4_hard/random: R@1=0.0174 R@5=0.1635 MRR=0.1131 n=746\\n  Q4_hard/embedding_distance: R@1=0.0751 R@5=0.3016 MRR=0.2009 n=746\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "3180f0c9-5251-4a4e-81f4-85112f04e13a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Top-level keys: ['config', 'by_repo_size', 'by_pool_size', 'by_similarity', 'by_dataflow', 'by_neg_difficulty']\\\\n\\\\nby_dataflow: strata = ['sparse', 'moderate', 'rich']\\\\n  sparse/random: R@1=0.0336 R@5=0.1624 MRR=0.1234 n=1546\\\\n  sparse/embedding_distance: R@1=0.0880 R@5=0.3325 MRR=0.2176 n=1546\\\\n  moderate/random: R@1=0.0361 R@5=0.1687 MRR=0.1343 n=498\\\\n  moderate/embedding_distance: R@1=0.0964 R@5=0.3916 MRR=0.2456 n=498\\\\n  rich/random: R@1=0.0128 R@5=0.1047 MRR=0.0868 n=936\\\\n  rich/embedding_distance: R@1=0.0502 R@5=0.2500 MRR=0.1667 n=936\\\\n\\\\nby_neg_difficulty: strata = ['Q1_easy', 'Q2', 'Q3', 'Q4_hard']\\\\n  Q1_easy/random: R@1=0.0377 R@5=0.1604 MRR=0.1241 n=742\\\\n  Q1_easy/embedding_distance: R@1=0.0822 R@5=0.3275 MRR=0.2101 n=742\\\\n  Q2/random: R@1=0.0308 R@5=0.1325 MRR=0.1120 n=747\\\\n  Q2/embedding_distance: R@1=0.0763 R@5=0.3240 MRR=0.2069 n=747\\\\n  Q3/random: R@1=0.0242 R@5=0.1248 MRR=0.1057 n=745\\\\n  Q3/embedding_distance: R@1=0.0765 R@5=0.3128 MRR=0.2074 n=745\\\\n  Q4_hard/random: R@1=0.0174 R@5=0.1635 MRR=0.1131 n=746\\\\n  Q4_hard/embedding_distance: R@1=0.0751 R@5=0.3016 MRR=0.2009 n=746\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Top-level keys: ['config', 'by_repo_size', 'by_pool_size', 'by_similarity', 'by_dataflow', 'by_neg_difficulty']\\n\\nby_dataflow: strata = ['sparse', 'moderate', 'rich']\\n  sparse/random: R@1=0.0336 R@5=0.1624 MRR=0.1234 n=1546\\n  sparse/embedding_distance: R@1=0.0880 R@5=0.3325 MRR=0.2176 n=1546\\n  moderate/random: R@1=0.0361 R@5=0.1687 MRR=0.1343 n=498\\n  moderate/embedding_distance: R@1=0.0964 R@5=0.3916 MRR=0.2456 n=498\\n  rich/random: R@1=0.0128 R@5=0.1047 MRR=0.0868 n=936\\n  rich/embedding_distance: R@1=0.0502 R@5=0.2500 MRR=0.1667 n=936\\n\\nby_neg_difficulty: strata = ['Q1_easy', 'Q2', 'Q3', 'Q4_hard']\\n  Q1_easy/random: R@1=0.0377 R@5=0.1604 MRR=0.1241 n=742\\n  Q1_easy/embedding_distance: R@1=0.0822 R@5=0.3275 MRR=0.2101 n=742\\n  Q2/random: R@1=0.0308 R@5=0.1325 MRR=0.1120 n=747\\n  Q2/embedding_distance: R@1=0.0763 R@5=0.3240 MRR=0.2069 n=747\\n  Q3/random: R@1=0.0242 R@5=0.1248 MRR=0.1057 n=745\\n  Q3/embedding_distance: R@1=0.0765 R@5=0.3128 MRR=0.2074 n=745\\n  Q4_hard/random: R@1=0.0174 R@5=0.1635 MRR=0.1131 n=746\\n  Q4_hard/embedding_distance: R@1=0.0751 R@5=0.3016 MRR=0.2009 n=746\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 186_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01TZWMaunzS1yddNASrTcd1K`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "grep \"dataflow\\|neg_difficulty\" /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "48c50f2b-93f5-49f4-b047-45b3af3fb05c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRf6mSVisKJ29ieKTbsCkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 882,
      "cache_read_input_tokens": 96346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 882
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

_source line 187 · 2026-05-14T20:24:29.564Z_

<details><summary>↩ Tool result · `toolu_01TZWMaunzS1yddNASrTcd1K`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"repo_size,small,dataflow_aware,0.4000,\\\"[0.3152, 0.4694]\\\",0.9000,0.6000,130\\r\\nrepo_size,medium,dataflow_aware,0.2399,\\\"[0.2022, 0.2776]\\\",0.7370,0.4508,346\\r\\nrepo_size,large,dataflow_aware,0.0962,\\\"[0.0807, 0.1126]\\\",0.4103,0.2548,1226\\r\\nrepo_size,xlarge,dataflow_aware,0.1072,\\\"[0.0907, 0.1244]\\\",0.4210,0.2619,1278\\r\\npool_size,small,dataflow_aware,0.3551,\\\"[0.3043, 0.4240]\\\",0.8768,0.5628,276\\r\\npool_size,medium,dataflow_aware,0.1421,\\\"[0.1174, 0.1653]\\\",0.5636,0.3332,605\\r\\npool_size,large,dataflow_aware,0.0981,\\\"[0.0867, 0.1115]\\\",0.3954,0.2497,2099\\r\\nsimilarity,low,dataflow_aware,0.1285,\\\"[0.1143, 0.1416]\\\",0.4731,0.2939,2606\\r\\nsimilarity,medium,dataflow_aware,0.1514,\\\"[0.1114, 0.1944]\\\",0.4829,0.3097,350\\r\\nsimilarity,high,dataflow_aware,0.0833,\\\"[0.0000, 0.2083]\\\",0.4583,0.2834,24\\r\\ndataflow,sparse,random,0.0336,\\\"[0.0246, 0.0427]\\\",0.1624,0.1234,1546\\r\\ndataflow,sparse,embedding_distance,0.0880,\\\"[0.0750, 0.1009]\\\",0.3325,0.2176,1546\\r\\ndataflow,sparse,dataflow_aware,0.1378,\\\"[0.1216, 0.1552]\\\",0.5013,0.3071,1546\\r\\ndataflow,sparse,DELTA(Embedding-Random),+0.0543,(+161.5%),+0.1701,+0.0942,\\r\\ndataflow,sparse,DELTA(Dataflow-Random),+0.1041,(+309.6%),+0.3389,+0.1836,\\r\\ndataflow,moderate,random,0.0361,\\\"[0.0221, 0.0542]\\\",0.1687,0.1343,498\\r\\ndataflow,moderate,embedding_distance,0.0964,\\\"[0.0683, 0.1265]\\\",0.3916,0.2456,498\\r\\ndataflow,moderate,dataflow_aware,0.1627,\\\"[0.1305, 0.1908]\\\",0.5622,0.3469,498\\r\\ndataflow,moderate,DELTA(Embedding-Random),+0.0602,(+166.7%),+0.2229,+0.1113,\\r\\ndataflow,moderate,DELTA(Dataflow-Random),+0.1265,(+350.0%),+0.3936,+0.2126,\\r\\ndataflow,rich,random,0.0128,\\\"[0.0053, 0.0214]\\\",0.1047,0.0868,936\\r\\ndataflow,rich,embedding_distance,0.0502,\\\"[0.0342, 0.0641]\\\",0.2500,0.1667,936\\r\\ndataflow,rich,dataflow_aware,0.1026,\\\"[0.0855, 0.1197]\\\",0.3825,0.2496,936\\r\\ndataflow,rich,DELTA(Embedding-Random),+0.0374,(+291.7%),+0.1453,+0.0799,\\r\\ndataflow,rich,DELTA(Dataflow-Random),+0.0897,(+700.0%),+0.2778,+0.1629,\\r\\nneg_difficulty,Q1_easy,random,0.0377,\\\"[0.0243, 0.0512]\\\",0.1604,0.1241,742\\r\\nneg_difficulty,Q1_easy,embedding_distance,0.0822,\\\"[0.0633, 0.1024]\\\",0.3275,0.2101,742\\r\\nneg_difficulty,Q1_easy,dataflow_aware,0.1415,\\\"[0.1132, 0.1698]\\\",0.4596,0.2998,742\\r\\nneg_difficulty,Q1_easy,DELTA(Embedding-Random),+0.0445,(+117.9%),+0.1671,+0.0860,\\r\\nneg_difficulty,Q1_easy,DELTA(Dataflow-Random),+0.1038,(+275.0%),+0.2992,+0.1757,\\r\\nneg_difficulty,Q2,random,0.0308,\\\"[0.0187, 0.0442]\\\",0.1325,0.1120,747\\r\\nneg_difficulty,Q2,embedding_distance,0.0763,\\\"[0.0602, 0.0964]\\\",0.3240,0.2069,747\\r\\nneg_difficulty,Q2,dataflow_aware,0.1218,\\\"[0.0991, 0.1459]\\\",0.4859,0.2935,747\\r\\nneg_difficulty,Q2,DELTA(Embedding-Random),+0.0455,(+147.8%),+0.1914,+0.0949,\\r\\nneg_difficulty,Q2,DELTA(Dataflow-Random),+0.0910,(+295.7%),+0.3534,+0.1815,\\r\\nneg_difficulty,Q3,random,0.0242,\\\"[0.0148, 0.0349]\\\",0.1248,0.1057,745\\r\\nneg_difficulty,Q3,embedding_distance,0.0765,\\\"[0.0591, 0.0926]\\\",0.3128,0.2074,745\\r\\nneg_difficulty,Q3,dataflow_aware,0.1248,\\\"[0.0993, 0.1463]\\\",0.4832,0.2926,745\\r\\nneg_difficulty,Q3,DELTA(Embedding-Random),+0.0523,(+216.7%),+0.1879,+0.1016,\\r\\nneg_difficulty,Q3,DELTA(Dataflow-Random),+0.1007,(+416.7%),+0.3584,+0.1868,\\r\\nneg_difficulty,Q4_hard,random,0.0174,\\\"[0.0094, 0.0282]\\\",0.1635,0.1131,746\\r\\nneg_difficulty,Q4_hard,embedding_distance,0.0751,\\\"[0.0576, 0.0952]\\\",0.3016,0.2009,746\\r\\nneg_difficulty,Q4_hard,dataflow_aware,0.1354,\\\"[0.1113, 0.1622]\\\",0.4678,0.2968,746\\r\\nneg_difficulty,Q4_hard,DELTA(Embedding-Random),+0.0576,(+330.8%),+0.1381,+0.0878,\\r\\nneg_difficulty,Q4_hard,DELTA(Dataflow-Random),+0.1180,(+676.9%),+0.3043,+0.1837,\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "94f6c920-89f7-4c5f-bc96-c170696bbf80",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"repo_size,small,dataflow_aware,0.4000,\\\\\\\"[0.3152, 0.4694]\\\\\\\",0.9000,0.6000,130\\\\r\\\\nrepo_size,medium,dataflow_aware,0.2399,\\\\\\\"[0.2022, 0.2776]\\\\\\\",0.7370,0.4508,346\\\\r\\\\nrepo_size,large,dataflow_aware,0.0962,\\\\\\\"[0.0807, 0.1126]\\\\\\\",0.4103,0.2548,1226\\\\r\\\\nrepo_size,xlarge,dataflow_aware,0.1072,\\\\\\\"[0.0907, 0.1244]\\\\\\\",0.4210,0.2619,1278\\\\r\\\\npool_size,small,dataflow_aware,0.3551,\\\\\\\"[0.3043, 0.4240]\\\\\\\",0.8768,0.5628,276\\\\r\\\\npool_size,medium,dataflow_aware,0.1421,\\\\\\\"[0.1174, 0.1653]\\\\\\\",0.5636,0.3332,605\\\\r\\\\npool_size,large,dataflow_aware,0.0981,\\\\\\\"[0.0867, 0.1115]\\\\\\\",0.3954,0.2497,2099\\\\r\\\\nsimilarity,low,dataflow_aware,0.1285,\\\\\\\"[0.1143, 0.1416]\\\\\\\",0.4731,0.2939,2606\\\\r\\\\nsimilarity,medium,dataflow_aware,0.1514,\\\\\\\"[0.1114, 0.1944]\\\\\\\",0.4829,0.3097,350\\\\r\\\\nsimilarity,high,dataflow_aware,0.0833,\\\\\\\"[0.0000, 0.2083]\\\\\\\",0.4583,0.2834,24\\\\r\\\\ndataflow,sparse,random,0.0336,\\\\\\\"[0.0246, 0.0427]\\\\\\\",0.1624,0.1234,1546\\\\r\\\\ndataflow,sparse,embedding_distance,0.0880,\\\\\\\"[0.0750, 0.1009]\\\\\\\",0.3325,0.2176,1546\\\\r\\\\ndataflow,sparse,dataflow_aware,0.1378,\\\\\\\"[0.1216, 0.1552]\\\\\\\",0.5013,0.3071,1546\\\\r\\\\ndataflow,sparse,DELTA(Embedding-Random),+0.0543,(+161.5%),+0.1701,+0.0942,\\\\r\\\\ndataflow,sparse,DELTA(Dataflow-Random),+0.1041,(+309.6%),+0.3389,+0.1836,\\\\r\\\\ndataflow,moderate,random,0.0361,\\\\\\\"[0.0221, 0.0542]\\\\\\\",0.1687,0.1343,498\\\\r\\\\ndataflow,moderate,embedding_distance,0.0964,\\\\\\\"[0.0683, 0.1265]\\\\\\\",0.3916,0.2456,498\\\\r\\\\ndataflow,moderate,dataflow_aware,0.1627,\\\\\\\"[0.1305, 0.1908]\\\\\\\",0.5622,0.3469,498\\\\r\\\\ndataflow,moderate,DELTA(Embedding-Random),+0.0602,(+166.7%),+0.2229,+0.1113,\\\\r\\\\ndataflow,moderate,DELTA(Dataflow-Random),+0.1265,(+350.0%),+0.3936,+0.2126,\\\\r\\\\ndataflow,rich,random,0.0128,\\\\\\\"[0.0053, 0.0214]\\\\\\\",0.1047,0.0868,936\\\\r\\\\ndataflow,rich,embedding_distance,0.0502,\\\\\\\"[0.0342, 0.0641]\\\\\\\",0.2500,0.1667,936\\\\r\\\\ndataflow,rich,dataflow_aware,0.1026,\\\\\\\"[0.0855, 0.1197]\\\\\\\",0.3825,0.2496,936\\\\r\\\\ndataflow,rich,DELTA(Embedding-Random),+0.0374,(+291.7%),+0.1453,+0.0799,\\\\r\\\\ndataflow,rich,DELTA(Dataflow-Random),+0.0897,(+700.0%),+0.2778,+0.1629,\\\\r\\\\nneg_difficulty,Q1_easy,random,0.0377,\\\\\\\"[0.0243, 0.0512]\\\\\\\",0.1604,0.1241,742\\\\r\\\\nneg_difficulty,Q1_easy,embedding_distance,0.0822,\\\\\\\"[0.0633, 0.1024]\\\\\\\",0.3275,0.2101,742\\\\r\\\\nneg_difficulty,Q1_easy,dataflow_aware,0.1415,\\\\\\\"[0.1132, 0.1698]\\\\\\\",0.4596,0.2998,742\\\\r\\\\nneg_difficulty,Q1_easy,DELTA(Embedding-Random),+0.0445,(+117.9%),+0.1671,+0.0860,\\\\r\\\\nneg_difficulty,Q1_easy,DELTA(Dataflow-Random),+0.1038,(+275.0%),+0.2992,+0.1757,\\\\r\\\\nneg_difficulty,Q2,random,0.0308,\\\\\\\"[0.0187, 0.0442]\\\\\\\",0.1325,0.1120,747\\\\r\\\\nneg_difficulty,Q2,embedding_distance,0.0763,\\\\\\\"[0.0602, 0.0964]\\\\\\\",0.3240,0.2069,747\\\\r\\\\nneg_difficulty,Q2,dataflow_aware,0.1218,\\\\\\\"[0.0991, 0.1459]\\\\\\\",0.4859,0.2935,747\\\\r\\\\nneg_difficulty,Q2,DELTA(Embedding-Random),+0.0455,(+147.8%),+0.1914,+0.0949,\\\\r\\\\nneg_difficulty,Q2,DELTA(Dataflow-Random),+0.0910,(+295.7%),+0.3534,+0.1815,\\\\r\\\\nneg_difficulty,Q3,random,0.0242,\\\\\\\"[0.0148, 0.0349]\\\\\\\",0.1248,0.1057,745\\\\r\\\\nneg_difficulty,Q3,embedding_distance,0.0765,\\\\\\\"[0.0591, 0.0926]\\\\\\\",0.3128,0.2074,745\\\\r\\\\nneg_difficulty,Q3,dataflow_aware,0.1248,\\\\\\\"[0.0993, 0.1463]\\\\\\\",0.4832,0.2926,745\\\\r\\\\nneg_difficulty,Q3,DELTA(Embedding-Random),+0.0523,(+216.7%),+0.1879,+0.1016,\\\\r\\\\nneg_difficulty,Q3,DELTA(Dataflow-Random),+0.1007,(+416.7%),+0.3584,+0.1868,\\\\r\\\\nneg_difficulty,Q4_hard,random,0.0174,\\\\\\\"[0.0094, 0.0282]\\\\\\\",0.1635,0.1131,746\\\\r\\\\nneg_difficulty,Q4_hard,embedding_distance,0.0751,\\\\\\\"[0.0576, 0.0952]\\\\\\\",0.3016,0.2009,746\\\\r\\\\nneg_difficulty,Q4_hard,dataflow_aware,0.1354,\\\\\\\"[0.1113, 0.1622]\\\\\\\",0.4678,0.2968,746\\\\r\\\\nneg_difficulty,Q4_hard,DELTA(Embedding-Random),+0.0576,(+330.8%),+0.1381,+0.0878,\\\\r\\\\nneg_difficulty,Q4_hard,DELTA(Dataflow-Random),+0.1180,(+676.9%),+0.3043,+0.1837,\\\\r\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"repo_size,small,dataflow_aware,0.4000,\\\"[0.3152, 0.4694]\\\",0.9000,0.6000,130\\r\\nrepo_size,medium,dataflow_aware,0.2399,\\\"[0.2022, 0.2776]\\\",0.7370,0.4508,346\\r\\nrepo_size,large,dataflow_aware,0.0962,\\\"[0.0807, 0.1126]\\\",0.4103,0.2548,1226\\r\\nrepo_size,xlarge,dataflow_aware,0.1072,\\\"[0.0907, 0.1244]\\\",0.4210,0.2619,1278\\r\\npool_size,small,dataflow_aware,0.3551,\\\"[0.3043, 0.4240]\\\",0.8768,0.5628,276\\r\\npool_size,medium,dataflow_aware,0.1421,\\\"[0.1174, 0.1653]\\\",0.5636,0.3332,605\\r\\npool_size,large,dataflow_aware,0.0981,\\\"[0.0867, 0.1115]\\\",0.3954,0.2497,2099\\r\\nsimilarity,low,dataflow_aware,0.1285,\\\"[0.1143, 0.1416]\\\",0.4731,0.2939,2606\\r\\nsimilarity,medium,dataflow_aware,0.1514,\\\"[0.1114, 0.1944]\\\",0.4829,0.3097,350\\r\\nsimilarity,high,dataflow_aware,0.0833,\\\"[0.0000, 0.2083]\\\",0.4583,0.2834,24\\r\\ndataflow,sparse,random,0.0336,\\\"[0.0246, 0.0427]\\\",0.1624,0.1234,1546\\r\\ndataflow,sparse,embedding_distance,0.0880,\\\"[0.0750, 0.1009]\\\",0.3325,0.2176,1546\\r\\ndataflow,sparse,dataflow_aware,0.1378,\\\"[0.1216, 0.1552]\\\",0.5013,0.3071,1546\\r\\ndataflow,sparse,DELTA(Embedding-Random),+0.0543,(+161.5%),+0.1701,+0.0942,\\r\\ndataflow,sparse,DELTA(Dataflow-Random),+0.1041,(+309.6%),+0.3389,+0.1836,\\r\\ndataflow,moderate,random,0.0361,\\\"[0.0221, 0.0542]\\\",0.1687,0.1343,498\\r\\ndataflow,moderate,embedding_distance,0.0964,\\\"[0.0683, 0.1265]\\\",0.3916,0.2456,498\\r\\ndataflow,moderate,dataflow_aware,0.1627,\\\"[0.1305, 0.1908]\\\",0.5622,0.3469,498\\r\\ndataflow,moderate,DELTA(Embedding-Random),+0.0602,(+166.7%),+0.2229,+0.1113,\\r\\ndataflow,moderate,DELTA(Dataflow-Random),+0.1265,(+350.0%),+0.3936,+0.2126,\\r\\ndataflow,rich,random,0.0128,\\\"[0.0053, 0.0214]\\\",0.1047,0.0868,936\\r\\ndataflow,rich,embedding_distance,0.0502,\\\"[0.0342, 0.0641]\\\",0.2500,0.1667,936\\r\\ndataflow,rich,dataflow_aware,0.1026,\\\"[0.0855, 0.1197]\\\",0.3825,0.2496,936\\r\\ndataflow,rich,DELTA(Embedding-Random),+0.0374,(+291.7%),+0.1453,+0.0799,\\r\\ndataflow,rich,DELTA(Dataflow-Random),+0.0897,(+700.0%),+0.2778,+0.1629,\\r\\nneg_difficulty,Q1_easy,random,0.0377,\\\"[0.0243, 0.0512]\\\",0.1604,0.1241,742\\r\\nneg_difficulty,Q1_easy,embedding_distance,0.0822,\\\"[0.0633, 0.1024]\\\",0.3275,0.2101,742\\r\\nneg_difficulty,Q1_easy,dataflow_aware,0.1415,\\\"[0.1132, 0.1698]\\\",0.4596,0.2998,742\\r\\nneg_difficulty,Q1_easy,DELTA(Embedding-Random),+0.0445,(+117.9%),+0.1671,+0.0860,\\r\\nneg_difficulty,Q1_easy,DELTA(Dataflow-Random),+0.1038,(+275.0%),+0.2992,+0.1757,\\r\\nneg_difficulty,Q2,random,0.0308,\\\"[0.0187, 0.0442]\\\",0.1325,0.1120,747\\r\\nneg_difficulty,Q2,embedding_distance,0.0763,\\\"[0.0602, 0.0964]\\\",0.3240,0.2069,747\\r\\nneg_difficulty,Q2,dataflow_aware,0.1218,\\\"[0.0991, 0.1459]\\\",0.4859,0.2935,747\\r\\nneg_difficulty,Q2,DELTA(Embedding-Random),+0.0455,(+147.8%),+0.1914,+0.0949,\\r\\nneg_difficulty,Q2,DELTA(Dataflow-Random),+0.0910,(+295.7%),+0.3534,+0.1815,\\r\\nneg_difficulty,Q3,random,0.0242,\\\"[0.0148, 0.0349]\\\",0.1248,0.1057,745\\r\\nneg_difficulty,Q3,embedding_distance,0.0765,\\\"[0.0591, 0.0926]\\\",0.3128,0.2074,745\\r\\nneg_difficulty,Q3,dataflow_aware,0.1248,\\\"[0.0993, 0.1463]\\\",0.4832,0.2926,745\\r\\nneg_difficulty,Q3,DELTA(Embedding-Random),+0.0523,(+216.7%),+0.1879,+0.1016,\\r\\nneg_difficulty,Q3,DELTA(Dataflow-Random),+0.1007,(+416.7%),+0.3584,+0.1868,\\r\\nneg_difficulty,Q4_hard,random,0.0174,\\\"[0.0094, 0.0282]\\\",0.1635,0.1131,746\\r\\nneg_difficulty,Q4_hard,embedding_distance,0.0751,\\\"[0.0576, 0.0952]\\\",0.3016,0.2009,746\\r\\nneg_difficulty,Q4_hard,dataflow_aware,0.1354,\\\"[0.1113, 0.1622]\\\",0.4678,0.2968,746\\r\\nneg_difficulty,Q4_hard,DELTA(Embedding-Random),+0.0576,(+330.8%),+0.1381,+0.0878,\\r\\nneg_difficulty,Q4_hard,DELTA(Dataflow-Random),+0.1180,(+676.9%),+0.3043,+0.1837,\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 188_

全部 5 个维度输出正确。数据分布合理：
- **dataflow**: sparse 1546, moderate 498, rich 936 
- **neg_difficulty**: 每个 quartile ~745 个实例（均匀分布）

现在确认 plots PDF 也包含了新维度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "3a852e2a-6812-4b11-b72c-7b0f58cd9bd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134rnpzfcWwBncsaqXNMsjC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3461,
      "cache_read_input_tokens": 97228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3461
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

_source line 189_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Eu8qrpiKxbCYU45Xf62vA5`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nfrom PyPDF2 import PdfReader\nr = PdfReader('/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_plots.pdf')\nprint(f'PDF pages: {len(r.pages)}')\n\"\n",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "830cc988-bc3f-4934-9ade-9701dba8fe99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134rnpzfcWwBncsaqXNMsjC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3461,
      "cache_read_input_tokens": 97228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3461
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

_source line 190 · 2026-05-14T20:24:40.905Z_

<details><summary>↩ Tool result · `toolu_01Eu8qrpiKxbCYU45Xf62vA5`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"Traceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 2, in &lt;module>\\nModuleNotFoundError: No module named 'PyPDF2'\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "8b9c27de-dae2-4ba9-96b8-ab20ec39acce",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"Traceback (most recent call last):\\\\n  File \\\\\\\"&lt;string>\\\\\\\", line 2, in &lt;module>\\\\nModuleNotFoundError: No module named 'PyPDF2'\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"Traceback (most recent call last):\\n  File \\\"&lt;string>\\\", line 2, in &lt;module>\\nModuleNotFoundError: No module named 'PyPDF2'\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 191_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015EZUC5D3TSw9pt6BUGYk9v`</summary>

```json
{
  "server": "bjb1-42106",
  "account": "root",
  "command": "stat /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_plots.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "fe5d7653-f5a5-4cdf-83c7-bd8588373780",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N37aGvSxwbsobCkTjSccZP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 423,
      "cache_read_input_tokens": 100689,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 423
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

_source line 192 · 2026-05-14T20:24:45.157Z_

<details><summary>↩ Tool result · `toolu_015EZUC5D3TSw9pt6BUGYk9v`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  File: /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_plots.pdf\\n  Size: 113134    \\tBlocks: 224        IO Block: 4096   regular file\\nDevice: 900h/2304d\\tInode: 13965484586  Links: 1\\nAccess: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)\\nAccess: 2026-05-15 04:24:17.895672841 +0800\\nModify: 2026-05-15 04:24:20.071684655 +0800\\nChange: 2026-05-15 04:24:20.071684655 +0800\\n Birth: 2026-05-15 04:24:17.895672841 +0800\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "83d35d98-1d74-4388-a162-b2ab1488f950",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  File: /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_plots.pdf\\\\n  Size: 113134    \\\\tBlocks: 224        IO Block: 4096   regular file\\\\nDevice: 900h/2304d\\\\tInode: 13965484586  Links: 1\\\\nAccess: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)\\\\nAccess: 2026-05-15 04:24:17.895672841 +0800\\\\nModify: 2026-05-15 04:24:20.071684655 +0800\\\\nChange: 2026-05-15 04:24:20.071684655 +0800\\\\n Birth: 2026-05-15 04:24:17.895672841 +0800\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  File: /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/stratified_plots.pdf\\n  Size: 113134    \\tBlocks: 224        IO Block: 4096   regular file\\nDevice: 900h/2304d\\tInode: 13965484586  Links: 1\\nAccess: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)\\nAccess: 2026-05-15 04:24:17.895672841 +0800\\nModify: 2026-05-15 04:24:20.071684655 +0800\\nChange: 2026-05-15 04:24:20.071684655 +0800\\n Birth: 2026-05-15 04:24:17.895672841 +0800\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 193_

PDF 113KB，dry-run 前是 40-50KB 级别，说明新维度的图已加入。

现在更新报告，记录最终状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "a619f781-50b2-4ecf-bc35-9ab7be5dafef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnGEkrBi2KrX817YanAJis",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 101112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
      },
      "output_tokens": 3,
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

_source line 194_

<details open><summary>🔧 Tool call — Read · `toolu_01JEUkvFwKkT1t4KgBmksoh2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratified_analysis_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "d86ee6bf-65ad-4a19-9661-d2b9f8ae32ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnGEkrBi2KrX817YanAJis",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 101112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
      },
      "output_tokens": 3,
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

_source line 195 · 2026-05-14T20:24:51.946Z_

<details><summary>↩ Tool result · `toolu_01JEUkvFwKkT1t4KgBmksoh2`</summary>

````text
1	# Plan 005: 分层分析报告
2	
3	**日期**: 2026-05-14
4	**状态**: 部分完成 — 管道验证通过，真实分析有阻塞
5	
6	## 1. 脚本路径与参数
7	
8	**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (781 行)
9	
10	### 参数
11	
12	| 参数 | 说明 | 默认值 |
13	|------|------|--------|
14	| `--m1-data` | M1 all.jsonl 路径 (必须) | — |
15	| `--val-data-dir` | val_*.jsonl 目录 | — |
16	| `--output-dir` | 输出目录 (必须) | — |
17	| `--predictions-dir` | 预计算预测 JSON 目录 (CPU) | None |
18	| `--checkpoints-dir` | Checkpoint 目录 (需 GPU) | None |
19	| `--dry-run` | Mock 预测，用于测试管道 (CPU) | False |
20	| `--seeds` | 逗号分隔的种子 | 42,43,44 |
21	| `--device` | 推理设备 | cuda |
22	| `--n-bootstrap` | Bootstrap 迭代数 | 1000 |
23	| `--repo-size-bins` | 自定义 repo size 分组 | None |
24	| `--pool-size-bins` | 自定义 pool size 分组 | None |
25	| `--sim-bins` | 自定义 similarity 分组 | None |
26	
27	### 输入模式 (三选一)
28	1. `--dry-run`: Mock 数据，CPU，用于管道验证 ✅ 已验证通过
29	2. `--predictions-dir`: 加载已有预测结果，CPU ⛔ 无数据
30	3. `--checkpoints-dir`: 从 checkpoint 做 forward pass，GPU ⛔ GPU 占用中
31	
32	### 输出
33	- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI
34	- `stratified_summary.csv`: 紧凑表格
35	- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势
36	
37	## 2. 维度覆盖
38	
39	| # | 维度 | 状态 | 说明 |
40	|---|------|------|------|
41	| 1 | **Repo size** | ✅ 已实现 | small(<50), medium(50-200), large(200-500), xlarge(500+) — M1 instance count per repo |
42	| 2 | **Pool size** | ✅ 已实现 | small(<20), medium(20-40), large(40-51) — neg_candidates 数量 |
43	| 3 | **Query-positive similarity** | ✅ 已实现 | low(0-0.3), medium(0.3-0.6), high(0.6-1.0) — cosine sim 或 text overlap |
44	| 4 | **Structural data availability** | ❌ 未实现 | 需新增：按 dataflow graph 边数分层 |
45	| 5 | **neg_difficulty quartile** | ❌ 未实现 | 需新增：按 negative difficulty (margin) 分四等分 |
46	
47	## 3. 阻塞点
48	
49	### 3.1 Checkpoint 路径不匹配
50	脚本查找 `{strategy}_s{seed}/best/`，但实际路径是 `{strategy}_s{seed}/best_by_recall_at_1/`。
51	
52	**修复方案**: 在 `main()` 中 checkpoint 路径解析处增加对 `best_by_recall_at_1` 和 `best_by_val_loss` 的查找逻辑。
53	
54	### 3.2 缺少 embedding_distance / dataflow_aware checkpoints
55	`/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/` 只有 `random_s42/43/44`，无 `embedding_distance` 和 `dataflow_aware` checkpoint。
56	
57	跨策略对比需要等这些策略的训练完成。
58	
59	### 3.3 GPU 占用
60	两块 GPU 正在训练，无法用 `--checkpoints-dir` 做 model inference。
61	
62	### 3.4 无预计算预测文件
63	没有 `eval_retrieval.py` 产出的 per-instance prediction JSON，`--predictions-dir` 模式无法使用。
64	
65	## 4. 缺失维度的实现方案
66	
67	### 4.1 Structural data availability
68	
69	**数据源**: `/root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json`
70	- 376,069 条 file→edges 映射，覆盖 11,205 个 instance
71	- Val 数据中所有 2,980 个 query 都有 graph 条目
72	- 但 51.9% (1,546/2,980) 的 query 仅有 1 条边
73	
74	**分层方案**:
75	```python
76	DATAFLOW_BINS = {
77	    "sparse": (0, 2),      # 0-1 条边 — 无/极少 dataflow 信息
78	    "moderate": (2, 10),    # 2-9 条边
79	    "rich": (10, float("inf")),  # 10+ 条边 — 丰富 dataflow 信息
80	}
81	```
82	
83	**实现**: 在 `assign_strata()` 中加载 graph，统计每个 query_id 的边数，分配 `dataflow_bin`。在 `main()` 中增加 `run_stratified_analysis(all_results, "dataflow_bin", ...)`。
84	
85	### 4.2 neg_difficulty quartile
86	
87	**定义**: margin = pos_sim - max(neg_sims)。margin 越小，negative 越难。
88	
89	**问题**: 需要 model forward pass 计算 embedding 相似度 → 需 GPU。
90	
91	**替代方案 (CPU)**:
92	- 用 text overlap (Jaccard token similarity) 代替 embedding similarity 作为 proxy
93	- 从 val data 中计算 query-neg 的 text overlap，取 max，得到 proxy margin
94	- 按 quartile 分四等分
95	
96	**实现**:
97	```python
98	def compute_neg_difficulty_proxy(sample):
99	    q_tokens = set(sample["query_tokens"][:1000].split())
100	    p_tokens = set(sample["pos_tokens"][:1000].split())
101	    pos_overlap = len(q_tokens & p_tokens) / max(len(q_tokens | p_tokens), 1)
102	    max_neg_overlap = 0
103	    for neg_id in sample["neg_candidates"][:7]:
104	        neg_text = sample["candidate_tokens"].get(neg_id, "")
105	        if neg_text:
106	            n_tokens = set(neg_text[:1000].split())
107	            overlap = len(q_tokens & n_tokens) / max(len(q_tokens | n_tokens), 1)
108	            max_neg_overlap = max(max_neg_overlap, overlap)
109	    return pos_overlap - max_neg_overlap  # margin proxy
110	```
111	
112	然后按 quartile 分成 Q1(easiest) - Q4(hardest)。
113	
114	## 5. Dry-run 验证结果
115	
116	成功运行 `--dry-run --seeds 42 --n-bootstrap 200`，产出:
117	- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_results.json` ✅
118	- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_summary.csv` ✅
119	- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_plots.pdf` ✅
120	
121	数据规模: 2,980 val instances, 123 repos, 44,173 M1 instances。
122	
123	## 6. 下一步行动
124	
125	| 优先级 | 任务 | 依赖 |
126	|--------|------|------|
127	| P0 | 修复 checkpoint 路径解析 (best_by_recall_at_1) | 无 |
128	| P0 | 添加 structural data availability 维度 | 无 (CPU) |
129	| P0 | 添加 neg_difficulty quartile 维度 (text proxy) | 无 (CPU) |
130	| P1 | 用现有 random checkpoints 生成 per-instance predictions | GPU 空闲后 |
131	| P1 | 用 predictions 跑真实 3 维度分层分析 | P1 上一步 |
132	| P2 | 训练 embedding_distance / dataflow_aware checkpoints | GPU + 训练时间 |
133	| P2 | 跨策略全 5 维度完整分析 | P2 上一步 |
134	
135	## 7. 相关文件清单
136	
137	```
138	脚本:
139	  /root/structfuse/evaluation/analyze_stratified.py        # 主分析脚本
140	  /root/structfuse/scripts/analyze_bm25_overlap_stratified.py  # BM25 overlap 分层 (独立)
141	
142	数据:
143	  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl       # M1 元数据 (44,173 instances)
144	  /root/autodl-tmp/structfuse/full_m2_training_data/       # Val/Train JSONL (3 strategies × 3 seeds)
145	  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json  # Dataflow 图 (376K edges)
146	
147	Checkpoints (仅 random):
148	  /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s{42,43,44}/best_by_recall_at_1/
149	  /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/
150	
151	Dry-run 输出:
152	  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun/
153	```
154	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "6ad31a08-2cab-4cc3-895c-ce264d05081c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratified_analysis_report.md",
      "content": "# Plan 005: 分层分析报告\n\n**日期**: 2026-05-14\n**状态**: 部分完成 — 管道验证通过，真实分析有阻塞\n\n## 1. 脚本路径与参数\n\n**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (781 行)\n\n### 参数\n\n| 参数 | 说明 | 默认值 |\n|------|------|--------|\n| `--m1-data` | M1 all.jsonl 路径 (必须) | — |\n| `--val-data-dir` | val_*.jsonl 目录 | — |\n| `--output-dir` | 输出目录 (必须) | — |\n| `--predictions-dir` | 预计算预测 JSON 目录 (CPU) | None |\n| `--checkpoints-dir` | Checkpoint 目录 (需 GPU) | None |\n| `--dry-run` | Mock 预测，用于测试管道 (CPU) | False |\n| `--seeds` | 逗号分隔的种子 | 42,43,44 |\n| `--device` | 推理设备 | cuda |\n| `--n-bootstrap` | Bootstrap 迭代数 | 1000 |\n| `--repo-size-bins` | 自定义 repo size 分组 | None |\n| `--pool-size-bins` | 自定义 pool size 分组 | None |\n| `--sim-bins` | 自定义 similarity 分组 | None |\n\n### 输入模式 (三选一)\n1. `--dry-run`: Mock 数据，CPU，用于管道验证 ✅ 已验证通过\n2. `--predictions-dir`: 加载已有预测结果，CPU ⛔ 无数据\n3. `--checkpoints-dir`: 从 checkpoint 做 forward pass，GPU ⛔ GPU 占用中\n\n### 输出\n- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI\n- `stratified_summary.csv`: 紧凑表格\n- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势\n\n## 2. 维度覆盖\n\n| # | 维度 | 状态 | 说明 |\n|---|------|------|------|\n| 1 | **Repo size** | ✅ 已实现 | small(<50), medium(50-200), large(200-500), xlarge(500+) — M1 instance count per repo |\n| 2 | **Pool size** | ✅ 已实现 | small(<20), medium(20-40), large(40-51) — neg_candidates 数量 |\n| 3 | **Query-positive similarity** | ✅ 已实现 | low(0-0.3), medium(0.3-0.6), high(0.6-1.0) — cosine sim 或 text overlap |\n| 4 | **Structural data availability** | ❌ 未实现 | 需新增：按 dataflow graph 边数分层 |\n| 5 | **neg_difficulty quartile** | ❌ 未实现 | 需新增：按 negative difficulty (margin) 分四等分 |\n\n## 3. 阻塞点\n\n### 3.1 Checkpoint 路径不匹配\n脚本查找 `{strategy}_s{seed}/best/`，但实际路径是 `{strategy}_s{seed}/best_by_recall_at_1/`。\n\n**修复方案**: 在 `main()` 中 checkpoint 路径解析处增加对 `best_by_recall_at_1` 和 `best_by_val_loss` 的查找逻辑。\n\n### 3.2 缺少 embedding_distance / dataflow_aware checkpoints\n`/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/` 只有 `random_s42/43/44`，无 `embedding_distance` 和 `dataflow_aware` checkpoint。\n\n跨策略对比需要等这些策略的训练完成。\n\n### 3.3 GPU 占用\n两块 GPU 正在训练，无法用 `--checkpoints-dir` 做 model inference。\n\n### 3.4 无预计算预测文件\n没有 `eval_retrieval.py` 产出的 per-instance prediction JSON，`--predictions-dir` 模式无法使用。\n\n## 4. 缺失维度的实现方案\n\n### 4.1 Structural data availability\n\n**数据源**: `/root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json`\n- 376,069 条 file→edges 映射，覆盖 11,205 个 instance\n- Val 数据中所有 2,980 个 query 都有 graph 条目\n- 但 51.9% (1,546/2,980) 的 query 仅有 1 条边\n\n**分层方案**:\n```python\nDATAFLOW_BINS = {\n    \"sparse\": (0, 2),      # 0-1 条边 — 无/极少 dataflow 信息\n    \"moderate\": (2, 10),    # 2-9 条边\n    \"rich\": (10, float(\"inf\")),  # 10+ 条边 — 丰富 dataflow 信息\n}\n```\n\n**实现**: 在 `assign_strata()` 中加载 graph，统计每个 query_id 的边数，分配 `dataflow_bin`。在 `main()` 中增加 `run_stratified_analysis(all_results, \"dataflow_bin\", ...)`。\n\n### 4.2 neg_difficulty quartile\n\n**定义**: margin = pos_sim - max(neg_sims)。margin 越小，negative 越难。\n\n**问题**: 需要 model forward pass 计算 embedding 相似度 → 需 GPU。\n\n**替代方案 (CPU)**:\n- 用 text overlap (Jaccard token similarity) 代替 embedding similarity 作为 proxy\n- 从 val data 中计算 query-neg 的 text overlap，取 max，得到 proxy margin\n- 按 quartile 分四等分\n\n**实现**:\n```python\ndef compute_neg_difficulty_proxy(sample):\n    q_tokens = set(sample[\"query_tokens\"][:1000].split())\n    p_tokens = set(sample[\"pos_tokens\"][:1000].split())\n    pos_overlap = len(q_tokens & p_tokens) / max(len(q_tokens | p_tokens), 1)\n    max_neg_overlap = 0\n    for neg_id in sample[\"neg_candidates\"][:7]:\n        neg_text = sample[\"candidate_tokens\"].get(neg_id, \"\")\n        if neg_text:\n            n_tokens = set(neg_text[:1000].split())\n            overlap = len(q_tokens & n_tokens) / max(len(q_tokens | n_tokens), 1)\n            max_neg_overlap = max(max_neg_overlap, overlap)\n    return pos_overlap - max_neg_overlap  # margin proxy\n```\n\n然后按 quartile 分成 Q1(easiest) - Q4(hardest)。\n\n## 5. Dry-run 验证结果\n\n成功运行 `--dry-run --seeds 42 --n-bootstrap 200`，产出:\n- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_results.json` ✅\n- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_summary.csv` ✅\n- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_plots.pdf` ✅\n\n数据规模: 2,980 val instances, 123 repos, 44,173 M1 instances。\n\n## 6. 下一步行动\n\n| 优先级 | 任务 | 依赖 |\n|--------|------|------|\n| P0 | 修复 checkpoint 路径解析 (best_by_recall_at_1) | 无 |\n| P0 | 添加 structural data availability 维度 | 无 (CPU) |\n| P0 | 添加 neg_difficulty quartile 维度 (text proxy) | 无 (CPU) |\n| P1 | 用现有 random checkpoints 生成 per-instance predictions | GPU 空闲后 |\n| P1 | 用 predictions 跑真实 3 维度分层分析 | P1 上一步 |\n| P2 | 训练 embedding_distance / dataflow_aware checkpoints | GPU + 训练时间 |\n| P2 | 跨策略全 5 维度完整分析 | P2 上一步 |\n\n## 7. 相关文件清单\n\n```\n脚本:\n  /root/structfuse/evaluation/analyze_stratified.py        # 主分析脚本\n  /root/structfuse/scripts/analyze_bm25_overlap_stratified.py  # BM25 overlap 分层 (独立)\n\n数据:\n  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl       # M1 元数据 (44,173 instances)\n  /root/autodl-tmp/structfuse/full_m2_training_data/       # Val/Train JSONL (3 strategies × 3 seeds)\n  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json  # Dataflow 图 (376K edges)\n\nCheckpoints (仅 random):\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s{42,43,44}/best_by_recall_at_1/\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/\n\nDry-run 输出:\n  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun/\n```\n",
      "numLines": 154,
      "startLine": 1,
      "totalLines": 154
    }
  }
}
````

</details>

---


### Tool call

_source line 196_

<details open><summary>🔧 Tool call — Write · `toolu_01SNfMLywNd4ryiNBKjnbF4Z`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratified_analysis_report.md",
  "content": "# Plan 005: 分层分析报告\n\n**日期**: 2026-05-14\n**状态**: 脚本已完成全部 5 维度，dry-run 通过。真实数据分析受阻于 GPU 占用和缺少跨策略 checkpoint。\n\n## 1. 脚本路径与参数\n\n**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (910 行，已修改)\n\n### 参数\n\n| 参数 | 说明 | 默认值 |\n|------|------|--------|\n| `--m1-data` | M1 all.jsonl 路径 (必须) | — |\n| `--val-data-dir` | val_*.jsonl 目录 | — |\n| `--output-dir` | 输出目录 (必须) | — |\n| `--predictions-dir` | 预计算预测 JSON 目录 (CPU) | None |\n| `--checkpoints-dir` | Checkpoint 目录 (需 GPU) | None |\n| `--dry-run` | Mock 预测，用于测试管道 (CPU) | False |\n| `--seeds` | 逗号分隔的种子 | 42,43,44 |\n| `--device` | 推理设备 | cuda |\n| `--n-bootstrap` | Bootstrap 迭代数 | 1000 |\n| `--dataflow-graph` | dataflow_graph.json 路径 (新增) | None |\n| `--repo-size-bins` | 自定义 repo size 分组 | None |\n| `--pool-size-bins` | 自定义 pool size 分组 | None |\n| `--sim-bins` | 自定义 similarity 分组 | None |\n\n### 运行命令 (完整)\n\n```bash\ncd /root/structfuse && python3 evaluation/analyze_stratified.py \\\n  --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \\\n  --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data \\\n  --dataflow-graph /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json \\\n  --output-dir /root/autodl-tmp/structfuse/artifacts/stratified_analysis \\\n  --predictions-dir &lt;predictions_dir> \\  # 或 --checkpoints-dir 或 --dry-run\n  --seeds 42,43,44 \\\n  --n-bootstrap 1000\n```\n\n### 输出\n- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI (5 维度)\n- `stratified_summary.csv`: 紧凑表格\n- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势 (5 维度)\n\n## 2. 维度覆盖 — 全部 5/5 ✅\n\n| # | 维度 | 状态 | 分层 | 说明 |\n|---|------|------|------|------|\n| 1 | **Repo size** | ✅ | small/medium/large/xlarge | M1 instance count per repo |\n| 2 | **Pool size** | ✅ | small/medium/large | neg_candidates 数量 |\n| 3 | **Query-positive similarity** | ✅ | low/medium/high | cosine sim 或 text overlap |\n| 4 | **Structural data availability** | ✅ 新增 | sparse/moderate/rich | dataflow graph 边数 |\n| 5 | **neg_difficulty quartile** | ✅ 新增 | Q1_easy/Q2/Q3/Q4_hard | text overlap proxy margin |\n\n### 新增维度实现细节\n\n**Structural data availability**: 从 `dataflow_graph.json` 统计每个 query_id 的边数，按 DATAFLOW_BINS 分层：\n- sparse (0-1 边): 1546 instances (51.9%)\n- moderate (2-9 边): 498 instances (16.7%)\n- rich (10+ 边): 936 instances (31.4%)\n\n**neg_difficulty quartile**: CPU 友好的 text-overlap proxy。计算 margin = (query-pos Jaccard overlap) - max(query-neg Jaccard overlap)，按 quartile 分四等分，margin 越小 → negative 越难。每个 quartile ~745 instances。\n\n## 3. 已完成的修改\n\n1. **新增 `DATAFLOW_BINS` 和 `NEG_DIFFICULTY_QUARTILE_LABELS` 常量**\n2. **新增 `load_dataflow_edges()` 函数** — 加载 dataflow graph 并返回 {file_key: edge_count}\n3. **新增 `assign_neg_difficulty_quartiles()` 函数** — 基于 text overlap proxy 计算 margin 并按 quartile 分配\n4. **扩展 `assign_strata()`** — 增加 `dataflow_edges` 参数，分配 `dataflow_bin`\n5. **新增 `--dataflow-graph` 参数**\n6. **修复 checkpoint 路径解析** — 依次查找 `best/`, `best_by_recall_at_1/`, `best_by_val_loss/`，需 model.pt 存在\n7. **扩展 `write_summary_csv()` 和 `make_plots()`** — 接受新维度数据，自动生成对应图表\n\n## 4. 阻塞点（真实数据分析）\n\n### 4.1 缺少 embedding_distance / dataflow_aware checkpoints\n`m2_full_qwen/` 只有 `random_s42/43/44`。跨策略对比需要这些策略的训练 checkpoint。\n\n### 4.2 无预计算预测文件\n`--predictions-dir` 模式需要 `eval_retrieval.py` 产出的 per-instance JSON。\n\n### 4.3 GPU 占用\nmodel inference 需要 GPU，当前被训练占用。\n\n## 5. Dry-run 验证\n\n运行 `--dry-run --seeds 42 --n-bootstrap 200 --dataflow-graph ...`，全部 5 维度成功产出：\n\n```\n/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/\n├── stratified_results.json  (5 维度，含 by_dataflow + by_neg_difficulty)\n├── stratified_summary.csv   (dataflow + neg_difficulty 行已加入)\n└── stratified_plots.pdf     (113KB，含新维度的 bar chart + heatmap + delta)\n```\n\n## 6. 下一步行动\n\n| 优先级 | 任务 | 依赖 |\n|--------|------|------|\n| P1 | 用现有 random checkpoints 生成 per-instance predictions (eval_retrieval.py) | GPU 空闲后 |\n| P1 | 用 predictions 跑 5 维度分层分析 (random only) | P1 上一步 |\n| P2 | 训练 embedding_distance / dataflow_aware checkpoints | GPU + 训练时间 |\n| P2 | 跨策略全 5 维度完整分析 | P2 上一步 |\n\n## 7. 相关文件清单\n\n```\n脚本 (已修改):\n  /root/structfuse/evaluation/analyze_stratified.py        # 910 行，5 维度完整\n\n数据:\n  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\n  /root/autodl-tmp/structfuse/full_m2_training_data/val_*.jsonl\n  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json\n\nCheckpoints (仅 random):\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s{42,43,44}/best_by_recall_at_1/\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/\n\nDry-run 输出:\n  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "0e3a2853-ff69-4b3f-afce-5a355d7a5677",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MugAkzjaZc8bNPGngjwT9B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3195,
      "cache_read_input_tokens": 101548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3195
      },
      "output_tokens": 65,
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

_source line 197 · 2026-05-14T20:25:25.311Z_

<details><summary>↩ Tool result · `toolu_01SNfMLywNd4ryiNBKjnbF4Z`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratified_analysis_report.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "35865531-75a4-482d-a498-82ae5a08ff4f",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan005_stratified_analysis_report.md",
    "content": "# Plan 005: 分层分析报告\n\n**日期**: 2026-05-14\n**状态**: 脚本已完成全部 5 维度，dry-run 通过。真实数据分析受阻于 GPU 占用和缺少跨策略 checkpoint。\n\n## 1. 脚本路径与参数\n\n**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (910 行，已修改)\n\n### 参数\n\n| 参数 | 说明 | 默认值 |\n|------|------|--------|\n| `--m1-data` | M1 all.jsonl 路径 (必须) | — |\n| `--val-data-dir` | val_*.jsonl 目录 | — |\n| `--output-dir` | 输出目录 (必须) | — |\n| `--predictions-dir` | 预计算预测 JSON 目录 (CPU) | None |\n| `--checkpoints-dir` | Checkpoint 目录 (需 GPU) | None |\n| `--dry-run` | Mock 预测，用于测试管道 (CPU) | False |\n| `--seeds` | 逗号分隔的种子 | 42,43,44 |\n| `--device` | 推理设备 | cuda |\n| `--n-bootstrap` | Bootstrap 迭代数 | 1000 |\n| `--dataflow-graph` | dataflow_graph.json 路径 (新增) | None |\n| `--repo-size-bins` | 自定义 repo size 分组 | None |\n| `--pool-size-bins` | 自定义 pool size 分组 | None |\n| `--sim-bins` | 自定义 similarity 分组 | None |\n\n### 运行命令 (完整)\n\n```bash\ncd /root/structfuse && python3 evaluation/analyze_stratified.py \\\n  --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \\\n  --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data \\\n  --dataflow-graph /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json \\\n  --output-dir /root/autodl-tmp/structfuse/artifacts/stratified_analysis \\\n  --predictions-dir &lt;predictions_dir> \\  # 或 --checkpoints-dir 或 --dry-run\n  --seeds 42,43,44 \\\n  --n-bootstrap 1000\n```\n\n### 输出\n- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI (5 维度)\n- `stratified_summary.csv`: 紧凑表格\n- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势 (5 维度)\n\n## 2. 维度覆盖 — 全部 5/5 ✅\n\n| # | 维度 | 状态 | 分层 | 说明 |\n|---|------|------|------|------|\n| 1 | **Repo size** | ✅ | small/medium/large/xlarge | M1 instance count per repo |\n| 2 | **Pool size** | ✅ | small/medium/large | neg_candidates 数量 |\n| 3 | **Query-positive similarity** | ✅ | low/medium/high | cosine sim 或 text overlap |\n| 4 | **Structural data availability** | ✅ 新增 | sparse/moderate/rich | dataflow graph 边数 |\n| 5 | **neg_difficulty quartile** | ✅ 新增 | Q1_easy/Q2/Q3/Q4_hard | text overlap proxy margin |\n\n### 新增维度实现细节\n\n**Structural data availability**: 从 `dataflow_graph.json` 统计每个 query_id 的边数，按 DATAFLOW_BINS 分层：\n- sparse (0-1 边): 1546 instances (51.9%)\n- moderate (2-9 边): 498 instances (16.7%)\n- rich (10+ 边): 936 instances (31.4%)\n\n**neg_difficulty quartile**: CPU 友好的 text-overlap proxy。计算 margin = (query-pos Jaccard overlap) - max(query-neg Jaccard overlap)，按 quartile 分四等分，margin 越小 → negative 越难。每个 quartile ~745 instances。\n\n## 3. 已完成的修改\n\n1. **新增 `DATAFLOW_BINS` 和 `NEG_DIFFICULTY_QUARTILE_LABELS` 常量**\n2. **新增 `load_dataflow_edges()` 函数** — 加载 dataflow graph 并返回 {file_key: edge_count}\n3. **新增 `assign_neg_difficulty_quartiles()` 函数** — 基于 text overlap proxy 计算 margin 并按 quartile 分配\n4. **扩展 `assign_strata()`** — 增加 `dataflow_edges` 参数，分配 `dataflow_bin`\n5. **新增 `--dataflow-graph` 参数**\n6. **修复 checkpoint 路径解析** — 依次查找 `best/`, `best_by_recall_at_1/`, `best_by_val_loss/`，需 model.pt 存在\n7. **扩展 `write_summary_csv()` 和 `make_plots()`** — 接受新维度数据，自动生成对应图表\n\n## 4. 阻塞点（真实数据分析）\n\n### 4.1 缺少 embedding_distance / dataflow_aware checkpoints\n`m2_full_qwen/` 只有 `random_s42/43/44`。跨策略对比需要这些策略的训练 checkpoint。\n\n### 4.2 无预计算预测文件\n`--predictions-dir` 模式需要 `eval_retrieval.py` 产出的 per-instance JSON。\n\n### 4.3 GPU 占用\nmodel inference 需要 GPU，当前被训练占用。\n\n## 5. Dry-run 验证\n\n运行 `--dry-run --seeds 42 --n-bootstrap 200 --dataflow-graph ...`，全部 5 维度成功产出：\n\n```\n/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/\n├── stratified_results.json  (5 维度，含 by_dataflow + by_neg_difficulty)\n├── stratified_summary.csv   (dataflow + neg_difficulty 行已加入)\n└── stratified_plots.pdf     (113KB，含新维度的 bar chart + heatmap + delta)\n```\n\n## 6. 下一步行动\n\n| 优先级 | 任务 | 依赖 |\n|--------|------|------|\n| P1 | 用现有 random checkpoints 生成 per-instance predictions (eval_retrieval.py) | GPU 空闲后 |\n| P1 | 用 predictions 跑 5 维度分层分析 (random only) | P1 上一步 |\n| P2 | 训练 embedding_distance / dataflow_aware checkpoints | GPU + 训练时间 |\n| P2 | 跨策略全 5 维度完整分析 | P2 上一步 |\n\n## 7. 相关文件清单\n\n```\n脚本 (已修改):\n  /root/structfuse/evaluation/analyze_stratified.py        # 910 行，5 维度完整\n\n数据:\n  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl\n  /root/autodl-tmp/structfuse/full_m2_training_data/val_*.jsonl\n  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json\n\nCheckpoints (仅 random):\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s{42,43,44}/best_by_recall_at_1/\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/\n\nDry-run 输出:\n  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/\n```\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 11,
        "newStart": 1,
        "newLines": 11,
        "lines": [
          " # Plan 005: 分层分析报告",
          " ",
          " **日期**: 2026-05-14",
          "-**状态**: 部分完成 — 管道验证通过，真实分析有阻塞",
          "+**状态**: 脚本已完成全部 5 维度，dry-run 通过。真实数据分析受阻于 GPU 占用和缺少跨策略 checkpoint。",
          " ",
          " ## 1. 脚本路径与参数",
          " ",
          "-**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (781 行)",
          "+**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (910 行，已修改)",
          " ",
          " ### 参数",
          " "
        ]
      },
      {
        "oldStart": 20,
        "oldLines": 134,
        "newStart": 20,
        "newLines": 104,
        "lines": [
          " | `--seeds` | 逗号分隔的种子 | 42,43,44 |",
          " | `--device` | 推理设备 | cuda |",
          " | `--n-bootstrap` | Bootstrap 迭代数 | 1000 |",
          "+| `--dataflow-graph` | dataflow_graph.json 路径 (新增) | None |",
          " | `--repo-size-bins` | 自定义 repo size 分组 | None |",
          " | `--pool-size-bins` | 自定义 pool size 分组 | None |",
          " | `--sim-bins` | 自定义 similarity 分组 | None |",
          " ",
          "-### 输入模式 (三选一)",
          "-1. `--dry-run`: Mock 数据，CPU，用于管道验证 ✅ 已验证通过",
          "-2. `--predictions-dir`: 加载已有预测结果，CPU ⛔ 无数据",
          "-3. `--checkpoints-dir`: 从 checkpoint 做 forward pass，GPU ⛔ GPU 占用中",
          "+### 运行命令 (完整)",
          " ",
          "+```bash",
          "+cd /root/structfuse && python3 evaluation/analyze_stratified.py \\",
          "+  --m1-data /root/autodl-tmp/structfuse/full_m1_data/all.jsonl \\",
          "+  --val-data-dir /root/autodl-tmp/structfuse/full_m2_training_data \\",
          "+  --dataflow-graph /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json \\",
          "+  --output-dir /root/autodl-tmp/structfuse/artifacts/stratified_analysis \\",
          "+  --predictions-dir &lt;predictions_dir> \\  # 或 --checkpoints-dir 或 --dry-run",
          "+  --seeds 42,43,44 \\",
          "+  --n-bootstrap 1000",
          "+```",
          "+",
          " ### 输出",
          "-- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI",
          "+- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI (5 维度)",
          " - `stratified_summary.csv`: 紧凑表格",
          "-- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势",
          "+- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势 (5 维度)",
          " ",
          "-## 2. 维度覆盖",
          "+## 2. 维度覆盖 — 全部 5/5 ✅",
          " ",
          "-| # | 维度 | 状态 | 说明 |",
          "-|---|------|------|------|",
          "-| 1 | **Repo size** | ✅ 已实现 | small(<50), medium(50-200), large(200-500), xlarge(500+) — M1 instance count per repo |",
          "-| 2 | **Pool size** | ✅ 已实现 | small(<20), medium(20-40), large(40-51) — neg_candidates 数量 |",
          "-| 3 | **Query-positive similarity** | ✅ 已实现 | low(0-0.3), medium(0.3-0.6), high(0.6-1.0) — cosine sim 或 text overlap |",
          "-| 4 | **Structural data availability** | ❌ 未实现 | 需新增：按 dataflow graph 边数分层 |",
          "-| 5 | **neg_difficulty quartile** | ❌ 未实现 | 需新增：按 negative difficulty (margin) 分四等分 |",
          "+| # | 维度 | 状态 | 分层 | 说明 |",
          "+|---|------|------|------|------|",
          "+| 1 | **Repo size** | ✅ | small/medium/large/xlarge | M1 instance count per repo |",
          "+| 2 | **Pool size** | ✅ | small/medium/large | neg_candidates 数量 |",
          "+| 3 | **Query-positive similarity** | ✅ | low/medium/high | cosine sim 或 text overlap |",
          "+| 4 | **Structural data availability** | ✅ 新增 | sparse/moderate/rich | dataflow graph 边数 |",
          "+| 5 | **neg_difficulty quartile** | ✅ 新增 | Q1_easy/Q2/Q3/Q4_hard | text overlap proxy margin |",
          " ",
          "-## 3. 阻塞点",
          "+### 新增维度实现细节",
          " ",
          "-### 3.1 Checkpoint 路径不匹配",
          "-脚本查找 `{strategy}_s{seed}/best/`，但实际路径是 `{strategy}_s{seed}/best_by_recall_at_1/`。",
          "+**Structural data availability**: 从 `dataflow_graph.json` 统计每个 query_id 的边数，按 DATAFLOW_BINS 分层：",
          "+- sparse (0-1 边): 1546 instances (51.9%)",
          "+- moderate (2-9 边): 498 instances (16.7%)",
          "+- rich (10+ 边): 936 instances (31.4%)",
          " ",
          "-**修复方案**: 在 `main()` 中 checkpoint 路径解析处增加对 `best_by_recall_at_1` 和 `best_by_val_loss` 的查找逻辑。",
          "+**neg_difficulty quartile**: CPU 友好的 text-overlap proxy。计算 margin = (query-pos Jaccard overlap) - max(query-neg Jaccard overlap)，按 quartile 分四等分，margin 越小 → negative 越难。每个 quartile ~745 instances。",
          " ",
          "-### 3.2 缺少 embedding_distance / dataflow_aware checkpoints",
          "-`/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/` 只有 `random_s42/43/44`，无 `embedding_distance` 和 `dataflow_aware` checkpoint。",
          "+## 3. 已完成的修改",
          " ",
          "-跨策略对比需要等这些策略的训练完成。",
          "+1. **新增 `DATAFLOW_BINS` 和 `NEG_DIFFICULTY_QUARTILE_LABELS` 常量**",
          "+2. **新增 `load_dataflow_edges()` 函数** — 加载 dataflow graph 并返回 {file_key: edge_count}",
          "+3. **新增 `assign_neg_difficulty_quartiles()` 函数** — 基于 text overlap proxy 计算 margin 并按 quartile 分配",
          "+4. **扩展 `assign_strata()`** — 增加 `dataflow_edges` 参数，分配 `dataflow_bin`",
          "+5. **新增 `--dataflow-graph` 参数**",
          "+6. **修复 checkpoint 路径解析** — 依次查找 `best/`, `best_by_recall_at_1/`, `best_by_val_loss/`，需 model.pt 存在",
          "+7. **扩展 `write_summary_csv()` 和 `make_plots()`** — 接受新维度数据，自动生成对应图表",
          " ",
          "-### 3.3 GPU 占用",
          "-两块 GPU 正在训练，无法用 `--checkpoints-dir` 做 model inference。",
          "+## 4. 阻塞点（真实数据分析）",
          " ",
          "-### 3.4 无预计算预测文件",
          "-没有 `eval_retrieval.py` 产出的 per-instance prediction JSON，`--predictions-dir` 模式无法使用。",
          "+### 4.1 缺少 embedding_distance / dataflow_aware checkpoints",
          "+`m2_full_qwen/` 只有 `random_s42/43/44`。跨策略对比需要这些策略的训练 checkpoint。",
          " ",
          "-## 4. 缺失维度的实现方案",
          "+### 4.2 无预计算预测文件",
          "+`--predictions-dir` 模式需要 `eval_retrieval.py` 产出的 per-instance JSON。",
          " ",
          "-### 4.1 Structural data availability",
          "+### 4.3 GPU 占用",
          "+model inference 需要 GPU，当前被训练占用。",
          " ",
          "-**数据源**: `/root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json`",
          "-- 376,069 条 file→edges 映射，覆盖 11,205 个 instance",
          "-- Val 数据中所有 2,980 个 query 都有 graph 条目",
          "-- 但 51.9% (1,546/2,980) 的 query 仅有 1 条边",
          "+## 5. Dry-run 验证",
          " ",
          "-**分层方案**:",
          "-```python",
          "-DATAFLOW_BINS = {",
          "-    \"sparse\": (0, 2),      # 0-1 条边 — 无/极少 dataflow 信息",
          "-    \"moderate\": (2, 10),    # 2-9 条边",
          "-    \"rich\": (10, float(\"inf\")),  # 10+ 条边 — 丰富 dataflow 信息",
          "-}",
          "-```",
          "+运行 `--dry-run --seeds 42 --n-bootstrap 200 --dataflow-graph ...`，全部 5 维度成功产出：",
          " ",
          "-**实现**: 在 `assign_strata()` 中加载 graph，统计每个 query_id 的边数，分配 `dataflow_bin`。在 `main()` 中增加 `run_stratified_analysis(all_results, \"dataflow_bin\", ...)`。",
          "-",
          "-### 4.2 neg_difficulty quartile",
          "-",
          "-**定义**: margin = pos_sim - max(neg_sims)。margin 越小，negative 越难。",
          "-",
          "-**问题**: 需要 model forward pass 计算 embedding 相似度 → 需 GPU。",
          "-",
          "-**替代方案 (CPU)**:",
          "-- 用 text overlap (Jaccard token similarity) 代替 embedding similarity 作为 proxy",
          "-- 从 val data 中计算 query-neg 的 text overlap，取 max，得到 proxy margin",
          "-- 按 quartile 分四等分",
          "-",
          "-**实现**:",
          "-```python",
          "-def compute_neg_difficulty_proxy(sample):",
          "-    q_tokens = set(sample[\"query_tokens\"][:1000].split())",
          "-    p_tokens = set(sample[\"pos_tokens\"][:1000].split())",
          "-    pos_overlap = len(q_tokens & p_tokens) / max(len(q_tokens | p_tokens), 1)",
          "-    max_neg_overlap = 0",
          "-    for neg_id in sample[\"neg_candidates\"][:7]:",
          "-        neg_text = sample[\"candidate_tokens\"].get(neg_id, \"\")",
          "-        if neg_text:",
          "-            n_tokens = set(neg_text[:1000].split())",
          "-            overlap = len(q_tokens & n_tokens) / max(len(q_tokens | n_tokens), 1)",
          "-            max_neg_overlap = max(max_neg_overlap, overlap)",
          "-    return pos_overlap - max_neg_overlap  # margin proxy",
          " ```",
          "+/root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/",
          "+├── stratified_results.json  (5 维度，含 by_dataflow + by_neg_difficulty)",
          "+├── stratified_summary.csv   (dataflow + neg_difficulty 行已加入)",
          "+└── stratified_plots.pdf     (113KB，含新维度的 bar chart + heatmap + delta)",
          "+```",
          " ",
          "-然后按 quartile 分成 Q1(easiest) - Q4(hardest)。",
          "-",
          "-## 5. Dry-run 验证结果",
          "-",
          "-成功运行 `--dry-run --seeds 42 --n-bootstrap 200`，产出:",
          "-- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_results.json` ✅",
          "-- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_summary.csv` ✅",
          "-- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_plots.pdf` ✅",
          "-",
          "-数据规模: 2,980 val instances, 123 repos, 44,173 M1 instances。",
          "-",
          " ## 6. 下一步行动",
          " ",
          " | 优先级 | 任务 | 依赖 |",
          " |--------|------|------|",
          "-| P0 | 修复 checkpoint 路径解析 (best_by_recall_at_1) | 无 |",
          "-| P0 | 添加 structural data availability 维度 | 无 (CPU) |",
          "-| P0 | 添加 neg_difficulty quartile 维度 (text proxy) | 无 (CPU) |",
          "-| P1 | 用现有 random checkpoints 生成 per-instance predictions | GPU 空闲后 |",
          "-| P1 | 用 predictions 跑真实 3 维度分层分析 | P1 上一步 |",
          "+| P1 | 用现有 random checkpoints 生成 per-instance predictions (eval_retrieval.py) | GPU 空闲后 |",
          "+| P1 | 用 predictions 跑 5 维度分层分析 (random only) | P1 上一步 |",
          " | P2 | 训练 embedding_distance / dataflow_aware checkpoints | GPU + 训练时间 |",
          " | P2 | 跨策略全 5 维度完整分析 | P2 上一步 |",
          " ",
          " ## 7. 相关文件清单",
          " ",
          " ```",
          "-脚本:",
          "-  /root/structfuse/evaluation/analyze_stratified.py        # 主分析脚本",
          "-  /root/structfuse/scripts/analyze_bm25_overlap_stratified.py  # BM25 overlap 分层 (独立)",
          "+脚本 (已修改):",
          "+  /root/structfuse/evaluation/analyze_stratified.py        # 910 行，5 维度完整",
          " ",
          " 数据:",
          "-  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl       # M1 元数据 (44,173 instances)",
          "-  /root/autodl-tmp/structfuse/full_m2_training_data/       # Val/Train JSONL (3 strategies × 3 seeds)",
          "-  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json  # Dataflow 图 (376K edges)",
          "+  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl",
          "+  /root/autodl-tmp/structfuse/full_m2_training_data/val_*.jsonl",
          "+  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json",
          " ",
          " Checkpoints (仅 random):",
          "   /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s{42,43,44}/best_by_recall_at_1/",
          "   /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/",
          " ",
          " Dry-run 输出:",
          "-  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun/",
          "+  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun_v2/",
          " ```"
        ]
      }
    ],
    "originalFile": "# Plan 005: 分层分析报告\n\n**日期**: 2026-05-14\n**状态**: 部分完成 — 管道验证通过，真实分析有阻塞\n\n## 1. 脚本路径与参数\n\n**脚本**: `/root/structfuse/evaluation/analyze_stratified.py` (781 行)\n\n### 参数\n\n| 参数 | 说明 | 默认值 |\n|------|------|--------|\n| `--m1-data` | M1 all.jsonl 路径 (必须) | — |\n| `--val-data-dir` | val_*.jsonl 目录 | — |\n| `--output-dir` | 输出目录 (必须) | — |\n| `--predictions-dir` | 预计算预测 JSON 目录 (CPU) | None |\n| `--checkpoints-dir` | Checkpoint 目录 (需 GPU) | None |\n| `--dry-run` | Mock 预测，用于测试管道 (CPU) | False |\n| `--seeds` | 逗号分隔的种子 | 42,43,44 |\n| `--device` | 推理设备 | cuda |\n| `--n-bootstrap` | Bootstrap 迭代数 | 1000 |\n| `--repo-size-bins` | 自定义 repo size 分组 | None |\n| `--pool-size-bins` | 自定义 pool size 分组 | None |\n| `--sim-bins` | 自定义 similarity 分组 | None |\n\n### 输入模式 (三选一)\n1. `--dry-run`: Mock 数据，CPU，用于管道验证 ✅ 已验证通过\n2. `--predictions-dir`: 加载已有预测结果，CPU ⛔ 无数据\n3. `--checkpoints-dir`: 从 checkpoint 做 forward pass，GPU ⛔ GPU 占用中\n\n### 输出\n- `stratified_results.json`: 完整 per-stratum 指标 + bootstrap CI\n- `stratified_summary.csv`: 紧凑表格\n- `stratified_plots.pdf`: 分组柱状图 + heatmap + delta 趋势\n\n## 2. 维度覆盖\n\n| # | 维度 | 状态 | 说明 |\n|---|------|------|------|\n| 1 | **Repo size** | ✅ 已实现 | small(<50), medium(50-200), large(200-500), xlarge(500+) — M1 instance count per repo |\n| 2 | **Pool size** | ✅ 已实现 | small(<20), medium(20-40), large(40-51) — neg_candidates 数量 |\n| 3 | **Query-positive similarity** | ✅ 已实现 | low(0-0.3), medium(0.3-0.6), high(0.6-1.0) — cosine sim 或 text overlap |\n| 4 | **Structural data availability** | ❌ 未实现 | 需新增：按 dataflow graph 边数分层 |\n| 5 | **neg_difficulty quartile** | ❌ 未实现 | 需新增：按 negative difficulty (margin) 分四等分 |\n\n## 3. 阻塞点\n\n### 3.1 Checkpoint 路径不匹配\n脚本查找 `{strategy}_s{seed}/best/`，但实际路径是 `{strategy}_s{seed}/best_by_recall_at_1/`。\n\n**修复方案**: 在 `main()` 中 checkpoint 路径解析处增加对 `best_by_recall_at_1` 和 `best_by_val_loss` 的查找逻辑。\n\n### 3.2 缺少 embedding_distance / dataflow_aware checkpoints\n`/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/` 只有 `random_s42/43/44`，无 `embedding_distance` 和 `dataflow_aware` checkpoint。\n\n跨策略对比需要等这些策略的训练完成。\n\n### 3.3 GPU 占用\n两块 GPU 正在训练，无法用 `--checkpoints-dir` 做 model inference。\n\n### 3.4 无预计算预测文件\n没有 `eval_retrieval.py` 产出的 per-instance prediction JSON，`--predictions-dir` 模式无法使用。\n\n## 4. 缺失维度的实现方案\n\n### 4.1 Structural data availability\n\n**数据源**: `/root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json`\n- 376,069 条 file→edges 映射，覆盖 11,205 个 instance\n- Val 数据中所有 2,980 个 query 都有 graph 条目\n- 但 51.9% (1,546/2,980) 的 query 仅有 1 条边\n\n**分层方案**:\n```python\nDATAFLOW_BINS = {\n    \"sparse\": (0, 2),      # 0-1 条边 — 无/极少 dataflow 信息\n    \"moderate\": (2, 10),    # 2-9 条边\n    \"rich\": (10, float(\"inf\")),  # 10+ 条边 — 丰富 dataflow 信息\n}\n```\n\n**实现**: 在 `assign_strata()` 中加载 graph，统计每个 query_id 的边数，分配 `dataflow_bin`。在 `main()` 中增加 `run_stratified_analysis(all_results, \"dataflow_bin\", ...)`。\n\n### 4.2 neg_difficulty quartile\n\n**定义**: margin = pos_sim - max(neg_sims)。margin 越小，negative 越难。\n\n**问题**: 需要 model forward pass 计算 embedding 相似度 → 需 GPU。\n\n**替代方案 (CPU)**:\n- 用 text overlap (Jaccard token similarity) 代替 embedding similarity 作为 proxy\n- 从 val data 中计算 query-neg 的 text overlap，取 max，得到 proxy margin\n- 按 quartile 分四等分\n\n**实现**:\n```python\ndef compute_neg_difficulty_proxy(sample):\n    q_tokens = set(sample[\"query_tokens\"][:1000].split())\n    p_tokens = set(sample[\"pos_tokens\"][:1000].split())\n    pos_overlap = len(q_tokens & p_tokens) / max(len(q_tokens | p_tokens), 1)\n    max_neg_overlap = 0\n    for neg_id in sample[\"neg_candidates\"][:7]:\n        neg_text = sample[\"candidate_tokens\"].get(neg_id, \"\")\n        if neg_text:\n            n_tokens = set(neg_text[:1000].split())\n            overlap = len(q_tokens & n_tokens) / max(len(q_tokens | n_tokens), 1)\n            max_neg_overlap = max(max_neg_overlap, overlap)\n    return pos_overlap - max_neg_overlap  # margin proxy\n```\n\n然后按 quartile 分成 Q1(easiest) - Q4(hardest)。\n\n## 5. Dry-run 验证结果\n\n成功运行 `--dry-run --seeds 42 --n-bootstrap 200`，产出:\n- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_results.json` ✅\n- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_summary.csv` ✅\n- `/root/autodl-tmp/structfuse/artifacts/stratified_dryrun/stratified_plots.pdf` ✅\n\n数据规模: 2,980 val instances, 123 repos, 44,173 M1 instances。\n\n## 6. 下一步行动\n\n| 优先级 | 任务 | 依赖 |\n|--------|------|------|\n| P0 | 修复 checkpoint 路径解析 (best_by_recall_at_1) | 无 |\n| P0 | 添加 structural data availability 维度 | 无 (CPU) |\n| P0 | 添加 neg_difficulty quartile 维度 (text proxy) | 无 (CPU) |\n| P1 | 用现有 random checkpoints 生成 per-instance predictions | GPU 空闲后 |\n| P1 | 用 predictions 跑真实 3 维度分层分析 | P1 上一步 |\n| P2 | 训练 embedding_distance / dataflow_aware checkpoints | GPU + 训练时间 |\n| P2 | 跨策略全 5 维度完整分析 | P2 上一步 |\n\n## 7. 相关文件清单\n\n```\n脚本:\n  /root/structfuse/evaluation/analyze_stratified.py        # 主分析脚本\n  /root/structfuse/scripts/analyze_bm25_overlap_stratified.py  # BM25 overlap 分层 (独立)\n\n数据:\n  /root/autodl-tmp/structfuse/full_m1_data/all.jsonl       # M1 元数据 (44,173 instances)\n  /root/autodl-tmp/structfuse/full_m2_training_data/       # Val/Train JSONL (3 strategies × 3 seeds)\n  /root/autodl-tmp/structfuse/full_m2_training_data/dataflow_graph.json  # Dataflow 图 (376K edges)\n\nCheckpoints (仅 random):\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s{42,43,44}/best_by_recall_at_1/\n  /root/autodl-tmp/structfuse/checkpoints/m2_full_starcoder/random_s42/best_by_recall_at_1/\n\nDry-run 输出:\n  /root/autodl-tmp/structfuse/artifacts/stratified_dryrun/\n```\n",
    "userModified": false
  }
}
````

</details>

---


### Assistant

_source line 198_

Now let me register this artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "ba537026-258a-402b-ab7b-13bab25fd3af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGEvejxnyfM8Xh5Edj96m1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2418,
      "cache_read_input_tokens": 104743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2418
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

_source line 199_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qzt48ccZANXTihRibJKX16`</summary>

```json
{
  "query": "register_artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "0fec26a2-35b5-4656-8cf5-531fa97fc40d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FGEvejxnyfM8Xh5Edj96m1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2418,
      "cache_read_input_tokens": 104743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2418
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

_source line 200 · 2026-05-14T20:25:28.443Z_

<details><summary>↩ Tool result · `toolu_01Qzt48ccZANXTihRibJKX16`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "645bfebb-730c-4b01-9c4a-c2a24a03c397",
  "tool_use_result": {
    "matches": [],
    "query": "register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---


### Assistant

_source line 201_

完成。总结：

## 结果

**`analyze_stratified.py` 已修改 (781→910 行)，全部 5 个分层维度实现完毕，dry-run 验证通过。**

### 已完成
1. **找到脚本** — `/root/structfuse/evaluation/analyze_stratified.py`
2. **补齐 2 个缺失维度**：
   - **Structural data availability** — 基于 dataflow_graph.json 边数分 sparse/moderate/rich (分布: 52%/17%/31%)
   - **neg_difficulty quartile** — CPU 友好的 text-overlap proxy，按 margin 分 Q1-Q4
3. **修复 checkpoint 路径** — 支持 `best_by_recall_at_1/` 和 `best_by_val_loss/`
4. **新增 `--dataflow-graph` 参数**
5. **CSV 和 PDF 图表** 均已扩展覆盖 5 个维度

### 阻塞（真实数据分析）
- **只有 random 策略 checkpoint**，无 embedding_distance / dataflow_aware → 无法做跨策略对比
- **无 per-instance prediction JSON** → `--predictions-dir` 模式不可用
- **GPU 被训练占用** → `--checkpoints-dir` 模式不可用

### 下一步
GPU 空闲后用 `eval_retrieval.py` 对现有 random checkpoint 生成 per-instance predictions，再用 `--predictions-dir` 跑真实分析。完整跨策略分析需等 embedding/dataflow checkpoint 训练完成。

报告已写入 `artifacts/plan005_stratified_analysis_report.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "uuid": "d80bc453-8ea0-4da4-bc91-533eae775c55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wYBKj1R1stERKSkEBPZiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 107161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 203
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

_source line 202_

完成。总结：

## 结果

**`analyze_stratified.py` 已修改 (781→910 行)，全部 5 个分层维度实现完毕，dry-run 验证通过。**

### 已完成
1. **找到脚本** — `/root/structfuse/evaluation/analyze_stratified.py`
2. **补齐 2 个缺失维度**：
   - **Structural data availability** — 基于 dataflow_graph.json 边数分 sparse/moderate/rich (分布: 52%/17%/31%)
   - **neg_difficulty quartile** — CPU 友好的 text-overlap proxy，按 margin 分 Q1-Q4
3. **修复 checkpoint 路径** — 支持 `best_by_recall_at_1/` 和 `best_by_val_loss/`
4. **新增 `--dataflow-graph` 参数**
5. **CSV 和 PDF 图表** 均已扩展覆盖 5 个维度

### 阻塞（真实数据分析）
- **只有 random 策略 checkpoint**，无 embedding_distance / dataflow_aware → 无法做跨策略对比
- **无 per-instance prediction JSON** → `--predictions-dir` 模式不可用
- **GPU 被训练占用** → `--checkpoints-dir` 模式不可用

### 下一步
GPU 空闲后用 `eval_retrieval.py` 对现有 random checkpoint 生成 per-instance predictions，再用 `--predictions-dir` 跑真实分析。完整跨策略分析需等 embedding/dataflow checkpoint 训练完成。

报告已写入 `artifacts/plan005_stratified_analysis_report.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 646925,
  "duration_api_ms": 526712,
  "num_turns": 81,
  "stop_reason": "end_turn",
  "session_id": "cd11087d-991b-47e1-b3c6-f81e960f8388",
  "total_cost_usd": 2.843896749999999,
  "usage": {
    "input_tokens": 53,
    "cache_creation_input_tokens": 95917,
    "cache_read_input_tokens": 2891621,
    "output_tokens": 31866,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 95917,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 479,
        "cache_read_input_tokens": 107161,
        "cache_creation_input_tokens": 203,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 203
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1610,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00169,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 53,
      "outputTokens": 31866,
      "cacheReadInputTokens": 2891621,
      "cacheCreationInputTokens": 95917,
      "webSearchRequests": 0,
      "costUSD": 2.842206749999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "178916f4-bb96-44aa-baa2-afc53090e7fe"
}
```

</details>

---
