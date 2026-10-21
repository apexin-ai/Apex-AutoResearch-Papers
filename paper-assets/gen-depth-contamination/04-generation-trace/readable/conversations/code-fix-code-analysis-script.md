# code fix code analysis script

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_code_fix-code-analysis-script_20260519T025536.jsonl`
- **Structured JSON:** [`f070233d3ef2e85d5820.json`](../../sessions/f0/f070233d3ef2e85d5820.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-19T02:58:25.767856+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-code-analysis-script_20260519T025536",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T02:58:25.768227+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-code-analysis-script_20260519T025536",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T02:58:25.768647+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/analyze_code_crossmodel.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-code-analysis-script_20260519T025536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/analyze_code_crossmodel.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T02:58:25.769060+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Analyze code-domain cross-model pairwise AUC results and generate LaTeX table + JSON.\\\"\\\"\\\"\\n\\nimport json\\nimport math\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nPROJ_ROOT = Path(\\\"/root/autodl-tmp/gen-depth-contamination\\\")\\nRESULTS_DIR = PROJ_ROOT / \\\"results\\\"\\nARTIFACTS_DIR = PROJ_ROOT / \\\"artifacts\\\"\\nTHETA = 0.60\\n\\nEXPERIMENTS = {\\n    \\\"Qwen2.5-1.5B\\\": \\\"exp_code_qwen1b5\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"exp_code_qwen7b\\\",\\n    \\\"Llama-3.1-8B\\\": \\\"exp_code_llama8b\\\",\\n    \\\"Mistral-7B-v0.3\\\": \\\"exp_code_mistral7b\\\",\\n}\\n\\nPAIRS = [\\\"0v1\\\", \\\"1v2\\\", \\\"2v3\\\", \\\"3v4\\\", \\\"4v5\\\"]\\n\\n\\ndef load_experiment(exp_dir: Path) -> dict | None:\\n    auc_file = exp_dir / \\\"pairwise_auc.json\\\"\\n    if not auc_file.exists():\\n        return None\\n    with open(auc_file) as f:\\n        data = json.load(f)\\n    return data\\n\\n\\ndef compute_ci(fold_values: list[float]) -> tuple[float, float, float]:\\n    n = len(fold_values)\\n    mean = sum(fold_values) / n\\n    std = math.sqrt(sum((x - mean) ** 2 for x in fold_values) / (n - 1))\\n    ci = 1.96 * std / math.sqrt(n)\\n    return mean, std, ci\\n\\n\\ndef determine_kstar(mean_aucs: dict[str, float], theta: float = THETA) -> int:\\n    kstar = 0\\n    for pair in PAIRS:\\n        k = int(pair.split(\\\"v\\\")[1])\\n        if mean_aucs.get(pair, 0) > theta:\\n            kstar = max(kstar, k)\\n        else:\\n            break\\n    return kstar\\n\\n\\ndef build_results(experiments: dict[str, str]) -> dict:\\n    all_results = {}\\n    for model_name, exp_name in experiments.items():\\n        exp_dir = RESULTS_DIR / exp_name\\n        data = load_experiment(exp_dir)\\n        if data is None:\\n            print(f\\\"[WARN] {exp_name} not found or incomplete, skipping\\\", file=sys.stderr)\\n            all_results[model_name] 
…[truncated 4928 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-code-analysis-script_20260519T025536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T02:58:25.769375+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_code_pythia1b4/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-code-analysis-script_20260519T025536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/autodl-tmp/gen-depth-contamination/results/exp_code_pythia1b4/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T02:58:25.769577+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"feature_importance.json\\njsd.json\\nordinal_results.json\\npairwise_auc.json\\nsummary.txt\\ntrain.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-code-analysis-script_20260519T025536",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T02:58:25.769833+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat > /root/autodl-tmp/gen-depth-contamination/scripts/analyze_code_crossmodel.py << 'SCRIPTEOF'\n#!/usr/bin/env python3\n\"\"\"Analyze code-domain cross-model pairwise AUC results and generate LaTeX table + JSON.\"\"\"\n\nimport json\nimport math\nimport os\nimport sys\nfrom pathlib import Path\n\nPROJ_ROOT = Path(\"/root/autodl-tmp/gen-depth-contamination\")\nRESULTS_DIR = PROJ_ROOT / \"results\"\nARTIFACTS_DIR = PROJ_ROOT / \"artifacts\"\nTHETA = 0.60\n\nEXPERIMENTS = {\n    \"Qwen2.5-1.5B\": \"exp_code_qwen1b5\",\n    \"Pythia-1.4B\": \"exp_code_pythia1b4\",\n    \"Qwen2.5-7B\": \"exp_code_qwen7b\",\n    \"Llama-3.1-8B\": \"exp_code_llama8b\",\n    \"Mistral-7B-v0.3\": \"exp_code_mistral7b\",\n}\n\nPAIRS = [\"0v1\", \"1v2\", \"2v3\", \"3v4\", \"4v5\"]\n\n\ndef load_experiment(exp_dir: Path) -> dict | None:\n    auc_file = exp_dir / \"pairwise_auc.json\"\n    if not auc_file.exists():\n        return None\n    with open(auc_file) as f:\n        data = json.load(f)\n    return data\n\n\ndef compute_ci(fold_values: list[float]) -> tuple[float, float, float]:\n    n = len(fold_values)\n    mean = sum(fold_values) / n\n    std = math.sqrt(sum((x - mean) ** 2 for x in fold_values) / (n - 1))\n    ci = 1.96 * std / math.sqrt(n)\n    return mean, std, ci\n\n\ndef determine_kstar(mean_aucs: dict[str, float], theta: float = THETA) -> int:\n    kstar = 0\n    for pair in PAIRS:\n        k = int(pair.split(\"v\")[1])\n        if mean_aucs.get(pair, 0) > theta:\n            kstar = max(kstar, k)\n        else:\n            break\n    return kstar\n\n\ndef build_results(experiments: dict[str, str]) -> dict:\n    all_results = {}\n    for model_name, exp_name in experiments.items():\n        exp_dir = RESULTS_DIR / exp_name\n        data = load_experiment(exp_dir)\n        if data is None:\n            print(f\"[WARN] {exp_name} not found or incomplete, skipping\", file=sys.stderr)\n            all_results[model_name] = None\n            continue\n\n        model_result = {\"pairs\": {}}\n        for pair in PAIRS:\n            folds = data[\"per_fold\"][pair]\n            mean, std, ci = compute_ci(folds)\n            model_result[\"pairs\"][pair] = {\n                \"mean\": round(mean, 4),\n                \"std\": round(std, 4),\n                \"ci\": round(ci, 4),\n                \"folds\": folds,\n            }\n\n        mean_aucs = {p: model_result[\"pairs\"][p][\"mean\"] for p in PAIRS}\n        model_result[\"kstar\"] = determine_kstar(mean_aucs)\n        all_results[model_name] = model_result\n\n    return all_results\n\n\ndef generate_latex(all_results: dict) -> str:\n    model_names = list(EXPERIMENTS.keys())\n    n_models = len(model_names)\n\n    lines = []\n    lines.append(\"% Code Domain Cross-Model Pairwise AUC Results\")\n    lines.append(f\"% Generated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}\")\n    lines.append(f\"% Threshold theta = {THETA}\")\n    lines.append(\"\")\n    lines.append(\"\\\\begin{table}[t]\")\n    lines.append(\"\\\\centering\")\n    lines.append(\n        \"\\\\caption{Pairwise AUC ($k$ vs $k{+}1$) for code-domain contamination detection \"\n        \"across five generator models trained on the CodeSearchNet Python subset \"\n        \"\\\\citep{husain2019codesearchnet}. \"\n        \"CI columns show 95\\\\% confidence intervals from 5-fold CV. \"\n        \"Underlined values mark the $K^*$ boundary (last pair with AUC $> \\\\theta$).}\"\n    )\n    lines.append(\"\\\\label{tab:code_crossmodel_auc}\")\n    lines.append(\"\\\\resizebox{\\\\columnwidth}{!}{%\")\n\n    col_spec = \"l\" + \" cc\" * n_models\n    lines.append(f\"\\\\begin{{tabular}}{{{col_spec}}}\")\n    lines.append(\"\\\\toprule\")\n\n    header1_parts = [\"\"]\n    for name in model_names:\n        header1_parts.append(f\"\\\\multicolumn{{2}}{{c}}{{{name}}}\")\n    lines.append(\" & \".join(header1_parts) + \" \\\\\\\\\")\n\n    cmidrules = []\n    for i in range(n_models):\n        start = 2 + i * 2\n        end = start + 1\n        cmidrules.append(f\"\\\\cmidrule(lr){{{start}-{end}}}\")\n    lines.append(\" \".join(cmidrules))\n\n    header2 = \"Pair\"\n    for _ in model_names:\n        header2 += \" & AUC & CI\"\n    lines.append(header2 + \" \\\\\\\\\")\n    lines.append(\"\\\\midrule\")\n\n    for pair in PAIRS:\n        k_from, k_to = pair.split(\"v\")\n        row_label = f\"${k_from}{{\\\\to}}{k_to}$\"\n        row_parts = [row_label]\n\n        for model_name in model_names:\n            result = all_results.get(model_name)\n            if result is None:\n                row_parts.extend([\"TBD\", \"\"])\n            else:\n                pair_data = result[\"pairs\"][pair]\n                kstar = result[\"kstar\"]\n                k = int(k_from)\n                is_boundary = (k + 1 == kstar) and (pair_data[\"mean\"] > THETA)\n\n                auc_str = f\"{pair_data['mean']:.4f}\"\n                ci_str = f\"$\\\\pm${pair_data['ci']:.4f}\"\n\n                if is_boundary:\n                    auc_str = f\"\\\\underline{{{auc_str}}}\"\n                    ci_str = f\"\\\\underline{{{ci_str}}}\"\n\n                row_parts.extend([auc_str, ci_str])\n\n        lines.append(\" & \".join(row_parts) + \" \\\\\\\\\")\n\n    lines.append(\"\\\\midrule\")\n\n    kstar_parts = [\"$K^*$\"]\n    for model_name in model_names:\n        result = all_results.get(model_name)\n        if result is None:\n            kstar_parts.extend([\"TBD\", \"\"])\n        else:\n            kstar_parts.extend([str(result[\"kstar\"]), \"\"])\n    lines.append(\" & \".join(kstar_parts) + \" \\\\\\\\\")\n\n    lines.append(\"\\\\bottomrule\")\n    lines.append(\"\\\\end{tabular}}\")\n    lines.append(\"\")\n    lines.append(\"\\\\vspace{2pt}\")\n    lines.append(\n        f\"{{\\\\footnotesize $\\\\theta = {THETA}$; $K^*$ = max $k$ s.t.\\\\ \"\n        f\"AUC($k{{-}}1, k$) $> \\\\theta$. Domain: Code (CodeSearchNet Python subset). 5-fold CV.}}\"\n    )\n    lines.append(\"\\\\end{table}\")\n\n    return \"\\n\".join(lines)\n\n\ndef main():\n    all_results = build_results(EXPERIMENTS)\n\n    latex = generate_latex(all_results)\n    print(latex)\n    print()\n\n    json_out = {}\n    for model_name, result in all_results.items():\n        if result is None:\n            json_out[model_name] = None\n        else:\n            json_out[model_name] = {\n                \"kstar\": result[\"kstar\"],\n                \"pairs\": {\n                    p: {\"mean\": v[\"mean\"], \"ci\": v[\"ci\"]}\n                    for p, v in result[\"pairs\"].items()\n                },\n            }\n\n    os.makedirs(ARTIFACTS_DIR, exist_ok=True)\n    tex_path = ARTIFACTS_DIR / \"code_crossmodel_table.tex\"\n    json_path = ARTIFACTS_DIR / \"code_crossmodel_results.json\"\n\n    with open(tex_path, \"w\") as f:\n        f.write(latex + \"\\n\")\n    with open(json_path, \"w\") as f:\n        json.dump(json_out, f, indent=2)\n\n    print(f\"[INFO] LaTeX table written to {tex_path}\", file=sys.stderr)\n    print(f\"[INFO] JSON results written to {json_path}\", file=sys.stderr)\n\n    for model_name, result in all_results.items():\n        if result is not None:\n            print(f\"[CHECK] {model_name}: K*={result['kstar']}, 0v1 AUC={result['pairs']['0v1']['mean']:.4f}\", file=sys.stderr)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPTEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-code-analysis-script_20260519T025536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat > /root/autodl-tmp/gen-depth-contamination/scripts/analyze_code_crossmodel.py << 'SCRIPTEOF'\n#!/usr/bin/env python3\n\"\"\"Analyze code-domain cross-model pairwise AUC results and generate LaTeX table + JSON.\"\"\"\n\nimport json\nimport math\nimport os\nimport sys\nfrom pathlib import Path\n\nPROJ_ROOT = Path(\"/root/autodl-tmp/gen-depth-contamination\")\nRESULTS_DIR = PROJ_ROOT / \"results\"\nARTIFACTS_DIR = PROJ_ROOT / \"artifacts\"\nTHETA = 0.60\n\nEXPERIMENTS = {\n    \"Qwen2.5-1.5B\": \"exp_code_qwen1b5\",\n    \"Pythia-1.4B\": \"exp_code_pythia1b4\",\n    \"Qwen2.5-7B\": \"exp_code_qwen7b\",\n    \"Llama-3.1-8B\": \"exp_code_llama8b\",\n    \"Mistral-7B-v0.3\": \"exp_code_mistral7b\",\n}\n\nPAIRS = [\"0v1\", \"1v2\", \"2v3\", \"3v4\", \"4v5\"]\n\n\ndef load_experiment(exp_dir: Path) -> dict | None:\n    auc_file = exp_dir / \"pairwise_auc.json\"\n    if not auc_file.exists():\n        return None\n    with open(auc_file) as f:\n        data = json.load(f)\n    return data\n\n\ndef compute_ci(fold_values: list[float]) -> tuple[float, float, float]:\n    n = len(fold_values)\n    mean = sum(fold_values) / n\n    std = math.sqrt(sum((x - mean) ** 2 for x in fold_values) / (n - 1))\n    ci = 1.96 * std / math.sqrt(n)\n    return mean, std, ci\n\n\ndef determine_kstar(mean_aucs: dict[str, float], theta: float = THETA) -> int:\n    kstar = 0\n    for pair in PAIRS:\n        k = int(pair.split(\"v\")[1])\n        if mean_aucs.get(pair, 0) > theta:\n            kstar = max(kstar, k)\n        else:\n            break\n    return kstar\n\n\ndef build_results(experiments: dict[str, str]) -> dict:\n    all_results = {}\n    for model_name, exp_name in experiments.items():\n        exp_dir = RESULTS_DIR / exp_name\n        data = load_experiment(exp_dir)\n        if data is None:\n            print(f\"[WARN] {exp_name} not found or incomplete, skipping\", file=sys.stderr)\n            all_results[model_name] = None\n            continue\n\n        model_result = {\"pairs\": {}}\n        for pair in PAIRS:\n            folds = data[\"per_fold\"][pair]\n            mean, std, ci = compute_ci(folds)\n            model_result[\"pairs\"][pair] = {\n                \"mean\": round(mean, 4),\n                \"std\": round(std, 4),\n                \"ci\": round(ci, 4),\n                \"folds\": folds,\n            }\n\n        mean_aucs = {p: model_result[\"pairs\"][p][\"mean\"] for p in PAIRS}\n        model_result[\"kstar\"] = determine_kstar(mean_aucs)\n        all_results[model_name] = model_result\n\n    return all_results\n\n\ndef generate_latex(all_results: dict) -> str:\n    model_names = list(EXPERIMENTS.keys())\n    n_models = len(model_names)\n\n    lines = []\n    lines.append(\"% Code Domain Cross-Model Pairwise AUC Results\")\n    lines.append(f\"% Generated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}\")\n    lines.append(f\"% Threshold theta = {THETA}\")\n    lines.append(\"\")\n    lines.append(\"\\\\begin{table}[t]\")\n    lines.append(\"\\\\centering\")\n    lines.append(\n        \"\\\\caption{Pairwise AUC ($k$ vs $k{+}1$) for code-domain contamination detection \"\n        \"across five generator models trained on the CodeSearchNet Python subset \"\n        \"\\\\citep{husain2019codesearchnet}. \"\n        \"CI columns show 95\\\\% confidence intervals from 5-fold CV. \"\n        \"Underlined values mark the $K^*$ boundary (last pair with AUC $> \\\\theta$).}\"\n    )\n    lines.append(\"\\\\label{tab:code_crossmodel_auc}\")\n    lines.append(\"\\\\resizebox{\\\\columnwidth}{!}{%\")\n\n    col_spec = \"l\" + \" cc\" * n_models\n    lines.append(f\"\\\\begin{{tabular}}{{{col_spec}}}\")\n    lines.append(\"\\\\toprule\")\n\n    header1_parts = [\"\"]\n    for name in model_names:\n        header1_parts.append(f\"\\\\multicolumn{{2}}{{c}}{{{name}}}\")\n    lines.append(\" & \".join(header1_parts) + \" \\\\\\\\\")\n\n    cmidrules = []\n    for i in range(n_models):\n        start = 2 + i * 2\n        end = start + 1\n        cmidrules.append(f\"\\\\cmidrule(lr){{{start}-{end}}}\")\n    lines.append(\" \".join(cmidrules))\n\n    header2 = \"Pair\"\n    for _ in model_names:\n        header2 += \" & AUC & CI\"\n    lines.append(header2 + \" \\\\\\\\\")\n    lines.append(\"\\\\midrule\")\n\n    for pair in PAIRS:\n        k_from, k_to = pair.split(\"v\")\n        row_label = f\"${k_from}{{\\\\to}}{k_to}$\"\n        row_parts = [row_label]\n\n        for model_name in model_names:\n            result = all_results.get(model_name)\n            if result is None:\n                row_parts.extend([\"TBD\", \"\"])\n            else:\n                pair_data = result[\"pairs\"][pair]\n                kstar = result[\"kstar\"]\n                k = int(k_from)\n                is_boundary = (k + 1 == kstar) and (pair_data[\"mean\"] > THETA)\n\n                auc_str = f\"{pair_data['mean']:.4f}\"\n                ci_str = f\"$\\\\pm${pair_data['ci']:.4f}\"\n\n                if is_boundary:\n                    auc_str = f\"\\\\underline{{{auc_str}}}\"\n                    ci_str = f\"\\\\underline{{{ci_str}}}\"\n\n                row_parts.extend([auc_str, ci_str])\n\n        lines.append(\" & \".join(row_parts) + \" \\\\\\\\\")\n\n    lines.append(\"\\\\midrule\")\n\n    kstar_parts = [\"$K^*$\"]\n    for model_name in model_names:\n        result = all_results.get(model_name)\n        if result is None:\n            kstar_parts.extend([\"TBD\", \"\"])\n        else:\n            kstar_parts.extend([str(result[\"kstar\"]), \"\"])\n    lines.append(\" & \".join(kstar_parts) + \" \\\\\\\\\")\n\n    lines.append(\"\\\\bottomrule\")\n    lines.append(\"\\\\end{tabular}}\")\n    lines.append(\"\")\n    lines.append(\"\\\\vspace{2pt}\")\n    lines.append(\n        f\"{{\\\\footnotesize $\\\\theta = {THETA}$; $K^*$ = max $k$ s.t.\\\\ \"\n        f\"AUC($k{{-}}1, k$) $> \\\\theta$. Domain: Code (CodeSearchNet Python subset). 5-fold CV.}}\"\n    )\n    lines.append(\"\\\\end{table}\")\n\n    return \"\\n\".join(lines)\n\n\ndef main():\n    all_results = build_results(EXPERIMENTS)\n\n    latex = generate_latex(all_results)\n    print(latex)\n    print()\n\n    json_out = {}\n    for model_name, result in all_results.items():\n        if result is None:\n            json_out[model_name] = None\n        else:\n            json_out[model_name] = {\n                \"kstar\": result[\"kstar\"],\n                \"pairs\": {\n                    p: {\"mean\": v[\"mean\"], \"ci\": v[\"ci\"]}\n                    for p, v in result[\"pairs\"].items()\n                },\n            }\n\n    os.makedirs(ARTIFACTS_DIR, exist_ok=True)\n    tex_path = ARTIFACTS_DIR / \"code_crossmodel_table.tex\"\n    json_path = ARTIFACTS_DIR / \"code_crossmodel_results.json\"\n\n    with open(tex_path, \"w\") as f:\n        f.write(latex + \"\\n\")\n    with open(json_path, \"w\") as f:\n        json.dump(json_out, f, indent=2)\n\n    print(f\"[INFO] LaTeX table written to {tex_path}\", file=sys.stderr)\n    print(f\"[INFO] JSON results written to {json_path}\", file=sys.stderr)\n\n    for model_name, result in all_results.items():\n        if result is not None:\n            print(f\"[CHECK] {model_name}: K*={result['kstar']}, 0v1 AUC={result['pairs']['0v1']['mean']:.4f}\", file=sys.stderr)\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPTEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T02:58:25.770069+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-code-analysis-script_20260519T025536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T02:58:25.770244+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cd /root/autodl-tmp/gen-depth-contamination && python3 scripts/analyze_code_crossmodel.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_fix-code-analysis-script_20260519T025536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cd /root/autodl-tmp/gen-depth-contamination && python3 scripts/analyze_code_crossmodel.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T02:58:25.770427+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"% Code Domain Cross-Model Pairwise AUC Results\\n% Generated: 2026-05-19 10:58\\n% Threshold theta = 0.6\\n\\n\\\\begin{table}[t]\\n\\\\centering\\n\\\\caption{Pairwise AUC ($k$ vs $k{+}1$) for code-domain contamination detection across five generator models trained on the CodeSearchNet Python subset \\\\citep{husain2019codesearchnet}. CI columns show 95\\\\% confidence intervals from 5-fold CV. Underlined values mark the $K^*$ boundary (last pair with AUC $> \\\\theta$).}\\n\\\\label{tab:code_crossmodel_auc}\\n\\\\resizebox{\\\\columnwidth}{!}{%\\n\\\\begin{tabular}{l cc cc cc cc cc}\\n\\\\toprule\\n & \\\\multicolumn{2}{c}{Qwen2.5-1.5B} & \\\\multicolumn{2}{c}{Pythia-1.4B} & \\\\multicolumn{2}{c}{Qwen2.5-7B} & \\\\multicolumn{2}{c}{Llama-3.1-8B} & \\\\multicolumn{2}{c}{Mistral-7B-v0.3} \\\\\\\\\\n\\\\cmidrule(lr){2-3} \\\\cmidrule(lr){4-5} \\\\cmidrule(lr){6-7} \\\\cmidrule(lr){8-9} \\\\cmidrule(lr){10-11}\\nPair & AUC & CI & AUC & CI & AUC & CI & AUC & CI & AUC & CI \\\\\\\\\\n\\\\midrule\\n$0{\\\\to}1$ & 0.9388 & $\\\\pm$0.0046 & \\\\underline{0.9592} & \\\\underline{$\\\\pm$0.0035} & TBD &  & TBD &  & TBD &  \\\\\\\\\\n$1{\\\\to}2$ & \\\\underline{0.7382} & \\\\underline{$\\\\pm$0.0130} & 0.5983 & $\\\\pm$0.0049 & TBD &  & TBD &  & TBD &  \\\\\\\\\\n$2{\\\\to}3$ & 0.5300 & $\\\\pm$0.0072 & 0.5215 & $\\\\pm$0.0125 & TBD &  & TBD &  & TBD &  \\\\\\\\\\n$3{\\\\to}4$ & 0.5022 & $\\\\pm$0.0072 & 0.5152 & $\\\\pm$0.0117 & TBD &  & TBD &  & TBD &  \\\\\\\\\\n$4{\\\\to}5$ & 0.5219 & $\\\\pm$0.0055 & 0.5046 & $\\\\pm$0.0134 & TBD &  & TBD &  & TBD &  \\\\\\\\\\n\\\\midrule\\n$K^*$ & 2 &  & 1 &  & TBD &  & TBD &  & TBD &  \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}}\\n\\n\\\\vspace{2pt}\\n{\\\\footnotesize $\\\\theta = 0.6$; $K^*$ = max $k$ s.t.\\\\ AUC($k{-}1, k$) $> \\\\theta$. Domain: Code (CodeSearchNet Python subset). 5-fold CV.}\\n\\\\end{table}\\n\\n\", \"stderr\": \"[WARN] exp_code_qwen7b not found or incom
…[truncated 537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_fix-code-analysis-script_20260519T025536",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T02:58:25.770673+00:00_

验证结果：

| 检查项 | 结果 |
|--------|------|
| Qwen-1.5B: K\*=2, 0v1 AUC | K\*=2, AUC=0.9388 |
| Pythia-1.4B: K\*=1, 0v1 AUC | K\*=1, AUC=0.9592 |
| 其他 3 模型 | TBD |
| Caption 含 "CodeSearchNet Python" | 有 |
| Caption 含 "TheStack" | 无 |
| 表格列数 | `l cc cc cc cc cc` = 11 列 |
| cmidrule 分组 | `{2-3} {4-5} {6-7} {8-9} {10-11}` |

Pythia-1.4B 的 K\*=1 与预期一致，但 0v1 AUC 实际值为 0.9592（高于预估的 0.8952）。这是从 `exp_code_pythia1b4/pairwise_auc.json` 读出的真实数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_fix-code-analysis-script_20260519T025536"
}
```

</details>

---
