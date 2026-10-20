# code c3 layer effect test

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_code_c3_layer_effect_test_20260520T162759.jsonl`
- **Structured JSON:** [`4143af8872be80527072.json`](../../sessions/41/4143af8872be80527072.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-20T16:28:55.413970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
  "offset": "1080",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
    "offset": "1080",
    "limit": "120"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T16:28:55.414374+00:00_

1080	        interp = "moderate agreement"
1081	    elif kappa < 0.80:
1082	        interp = "substantial agreement"
1083	    else:
1084	        interp = "almost perfect agreement"
1085	
1086	    result = {
1087	        "n_clauses": N,
1088	        "n_models": n_models,
1089	        "models": models,
1090	        "n_raters_per_clause": {
1091	            "min": int(n_arr.min()),
1092	            "max": int(n_arr.max()),
1093	            "mean": round(float(n_arr.mean()), 1),
1094	        },
1095	        "category_proportions": {
1096	            "violated": round(float(p_j[0]), 4),
1097	            "not_violated": round(float(p_j[1]), 4),
1098	        },
1099	        "fleiss_kappa": round(float(kappa), 4),
1100	        "se": round(float(se), 4) if np.isfinite(se) else None,
1101	        "z": round(float(z_val), 4) if np.isfinite(z_val) else None,
1102	        "p": round(float(p_val), 6) if np.isfinite(p_val) else None,
1103	        "interpretation": interp,
1104	    }
1105	
1106	    out = ANALYSIS_DIR / "fleiss_kappa.json"
1107	    with open(out, "w") as f:
1108	        json.dump(result, f, indent=2, default=str)
1109	    print(f"  -> {out.name}")
1110	    return result
1111	
1112	
1113	def run_phase3(models: list[str]):
1114	    """Load all judgments and run the full analysis suite."""
1115	    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)
1116	
1117	    df = _load_all_judgments(models)
1118	    if df.empty:
1119	        print("No judgments found. Run Phase 2 first.")
1120	        return
1121	
1122	    print(f"Loaded {len(df)} judgments ({df['model'].nunique()} models, "
1123	          f"{df['ambiguity_type'].nunique()} types)")
1124	
1125	    binary = _binary_effect(df)
1126	    type_eff = _type_effect(df)
1127	    model_eff = _model_effect(df)
1128	    interact = _interaction(df)
1129	
1130	    # JSON report
1131	    report = {
1132	        "binary_effect": binary,
1133	        "type_effect": type_eff,
1134	        "model_effect": model_eff,
1135	        "model
…[truncated 2662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T16:28:55.414632+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
  "old_string": "    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):",
  "new_string": "    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_layer_effect_test(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"C3: Formal test of specification-layer vs linguistic-layer violation rates.\"\"\"\n    SPEC_TYPES = {\"incompleteness\", \"conditional_precedence\", \"authorization_scope\"}\n    LING_TYPES = {\"scopal\", \"lexical\", \"coreferential\"}\n\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n\n    # Filter to ambiguous condition only\n    amb = dfc[dfc[\"condition\"] == \"ambiguous\"].copy()\n    amb[\"layer\"] = amb[\"ambiguity_type\"].map(\n        lambda t: \"specification\" if t in SPEC_TYPES else \"linguistic\" if t in LING_TYPES else \"unknown\"\n    )\n    amb = amb[amb[\"layer\"] != \"unknown\"]\n\n    spec = amb[amb[\"layer\"] == \"specification\"]\n    ling = amb[amb[\"layer\"] == \"linguistic\"]\n\n    spec_n = len(spec)\n    spec_v = int(spec[\"violated\"].sum())\n    ling_n = len(ling)\n    ling_v = int(ling[\"violated\"].sum())\n\n    spec_rate = spec_v / spec_n if spec_n > 0 else 0\n    ling_rate = ling_v / ling_n if ling_n > 0 else 0\n    delta_pp = (spec_rate - ling_rate) * 100\n\n    from scipy.stats import chi2_contingency\n    table = np.array([\n        [spec_v, spec_n - spec_v],\n        [ling_v, ling_n - ling_v],\n    ])\n    chi2, p_val, dof, expected = chi2_contingency(table, correction=False)\n\n    n_total = spec_n + ling_n\n    cramers_v = np.sqrt(chi2 / n_total) if n_total > 0 else 0\n\n    a, b = spec_v, spec_n - spec_v\n    c, d = ling_v, ling_n - ling_v\n    if b > 0 and c > 0 and d > 0 and a > 0:\n        or_val = (a * d) / (b * c)\n        log_or = np.log(or_val)\n        se_log = np.sqrt(1/a + 1/b + 1/c + 1/d)\n        or_lo = float(np.exp(log_or - 1.96 * se_log))\n        or_hi = float(np.exp(log_or + 1.96 * se_log))\n    else:\n        or_val = or_lo = or_hi = float(\"nan\")\n\n    np.random.seed(42)\n    n_boot = 10000\n    spec_arr = spec[\"violated\"].values.astype(float)\n    ling_arr = ling[\"violated\"].values.astype(float)\n    boot_deltas = []\n    for _ in range(n_boot):\n        s_idx = np.random.randint(0, len(spec_arr), len(spec_arr))\n        l_idx = np.random.randint(0, len(ling_arr), len(ling_arr))\n        boot_deltas.append((spec_arr[s_idx].mean() - ling_arr[l_idx].mean()) * 100)\n    boot_deltas = np.array(boot_deltas)\n    ci_lo = float(np.percentile(boot_deltas, 2.5))\n    ci_hi = float(np.percentile(boot_deltas, 97.5))\n\n    per_type = {}\n    for atype in list(SPEC_TYPES) + list(LING_TYPES):\n        subset = amb[amb[\"ambiguity_type\"] == atype]\n        if len(subset) > 0:\n            rate = float(subset[\"violated\"].mean())\n            per_type[atype] = {\n                \"n\": len(subset),\n                \"violations\": int(subset[\"violated\"].sum()),\n                \"rate\": round(rate * 100, 2),\n                \"layer\": \"specification\" if atype in SPEC_TYPES else \"linguistic\",\n            }\n\n    result = {\n        \"test\": \"layer_effect (C3)\",\n        \"specification_layer\": {\n            \"types\": sorted(SPEC_TYPES),\n            \"n\": spec_n,\n            \"violations\": spec_v,\n            \"rate_pct\": round(spec_rate * 100, 2),\n        },\n        \"linguistic_layer\": {\n            \"types\": sorted(LING_TYPES),\n            \"n\": ling_n,\n            \"violations\": ling_v,\n            \"rate_pct\": round(ling_rate * 100, 2),\n        },\n        \"delta_pp\": round(delta_pp, 2),\n        \"bootstrap_ci_95\": [round(ci_lo, 2), round(ci_hi, 2)],\n        \"chi_squared\": {\n            \"statistic\": round(float(chi2), 4),\n            \"df\": int(dof),\n            \"p\": round(float(p_val), 6),\n        },\n        \"cramers_v\": round(float(cramers_v), 4),\n        \"odds_ratio\": {\n            \"or\": round(float(or_val), 4) if np.isfinite(or_val) else str(or_val),\n            \"ci_95\": [round(or_lo, 4) if np.isfinite(or_lo) else str(or_lo),\n                       round(or_hi, 4) if np.isfinite(or_hi) else str(or_hi)],\n        },\n        \"per_type_detail\": per_type,\n    }\n\n    out = ANALYSIS_DIR / \"layer_effect_test.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
    "old_string": "    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):",
    "new_string": "    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_layer_effect_test(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"C3: Formal test of specification-layer vs linguistic-layer violation rates.\"\"\"\n    SPEC_TYPES = {\"incompleteness\", \"conditional_precedence\", \"authorization_scope\"}\n    LING_TYPES = {\"scopal\", \"lexical\", \"coreferential\"}\n\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n\n    # Filter to ambiguous condition only\n    amb = dfc[dfc[\"condition\"] == \"ambiguous\"].copy()\n    amb[\"layer\"] = amb[\"ambiguity_type\"].map(\n        lambda t: \"specification\" if t in SPEC_TYPES else \"linguistic\" if t in LING_TYPES else \"unknown\"\n    )\n    amb = amb[amb[\"layer\"] != \"unknown\"]\n\n    spec = amb[amb[\"layer\"] == \"specification\"]\n    ling = amb[amb[\"layer\"] == \"linguistic\"]\n\n    spec_n = len(spec)\n    spec_v = int(spec[\"violated\"].sum())\n    ling_n = len(ling)\n    ling_v = int(ling[\"violated\"].sum())\n\n    spec_rate = spec_v / spec_n if spec_n > 0 else 0\n    ling_rate = ling_v / ling_n if ling_n > 0 else 0\n    delta_pp = (spec_rate - ling_rate) * 100\n\n    from scipy.stats import chi2_contingency\n    table = np.array([\n        [spec_v, spec_n - spec_v],\n        [ling_v, ling_n - ling_v],\n    ])\n    chi2, p_val, dof, expected = chi2_contingency(table, correction=False)\n\n    n_total = spec_n + ling_n\n    cramers_v = np.sqrt(chi2 / n_total) if n_total > 0 else 0\n\n    a, b = spec_v, spec_n - spec_v\n    c, d = ling_v, ling_n - ling_v\n    if b > 0 and c > 0 and d > 0 and a > 0:\n        or_val = (a * d) / (b * c)\n        log_or = np.log(or_val)\n        se_log = np.sqrt(1/a + 1/b + 1/c + 1/d)\n        or_lo = float(np.exp(log_or - 1.96 * se_log))\n        or_hi = float(np.exp(log_or + 1.96 * se_log))\n    else:\n        or_val = or_lo = or_hi = float(\"nan\")\n\n    np.random.seed(42)\n    n_boot = 10000\n    spec_arr = spec[\"violated\"].values.astype(float)\n    ling_arr = ling[\"violated\"].values.astype(float)\n    boot_deltas = []\n    for _ in range(n_boot):\n        s_idx = np.random.randint(0, len(spec_arr), len(spec_arr))\n        l_idx = np.random.randint(0, len(ling_arr), len(ling_arr))\n        boot_deltas.append((spec_arr[s_idx].mean() - ling_arr[l_idx].mean()) * 100)\n    boot_deltas = np.array(boot_deltas)\n    ci_lo = float(np.percentile(boot_deltas, 2.5))\n    ci_hi = float(np.percentile(boot_deltas, 97.5))\n\n    per_type = {}\n    for atype in list(SPEC_TYPES) + list(LING_TYPES):\n        subset = amb[amb[\"ambiguity_type\"] == atype]\n        if len(subset) > 0:\n            rate = float(subset[\"violated\"].mean())\n            per_type[atype] = {\n                \"n\": len(subset),\n                \"violations\": int(subset[\"violated\"].sum()),\n                \"rate\": round(rate * 100, 2),\n                \"layer\": \"specification\" if atype in SPEC_TYPES else \"linguistic\",\n            }\n\n    result = {\n        \"test\": \"layer_effect (C3)\",\n        \"specification_layer\": {\n            \"types\": sorted(SPEC_TYPES),\n            \"n\": spec_n,\n            \"violations\": spec_v,\n            \"rate_pct\": round(spec_rate * 100, 2),\n        },\n        \"linguistic_layer\": {\n            \"types\": sorted(LING_TYPES),\n            \"n\": ling_n,\n            \"violations\": ling_v,\n            \"rate_pct\": round(ling_rate * 100, 2),\n        },\n        \"delta_pp\": round(delta_pp, 2),\n        \"bootstrap_ci_95\": [round(ci_lo, 2), round(ci_hi, 2)],\n        \"chi_squared\": {\n            \"statistic\": round(float(chi2), 4),\n            \"df\": int(dof),\n            \"p\": round(float(p_val), 6),\n        },\n        \"cramers_v\": round(float(cramers_v), 4),\n        \"odds_ratio\": {\n            \"or\": round(float(or_val), 4) if np.isfinite(or_val) else str(or_val),\n            \"ci_95\": [round(or_lo, 4) if np.isfinite(or_lo) else str(or_lo),\n                       round(or_hi, 4) if np.isfinite(or_hi) else str(or_hi)],\n        },\n        \"per_type_detail\": per_type,\n    }\n\n    out = ANALYSIS_DIR / \"layer_effect_test.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T16:28:55.415077+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T16:28:55.415291+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
  "old_string": "    run_fleiss_kappa(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")",
  "new_string": "    run_fleiss_kappa(df, clauses_data)\n    run_layer_effect_test(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
    "old_string": "    run_fleiss_kappa(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")",
    "new_string": "    run_fleiss_kappa(df, clauses_data)\n    run_layer_effect_test(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T16:28:55.415669+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T16:28:55.415828+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
  "old_string": "    print(\"  - fleiss_kappa.json\")\n\n\n# ---------------------------------------------------------------------------",
  "new_string": "    print(\"  - fleiss_kappa.json\")\n    print(\"  - layer_effect_test.json\")\n\n\n# ---------------------------------------------------------------------------"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
    "old_string": "    print(\"  - fleiss_kappa.json\")\n\n\n# ---------------------------------------------------------------------------",
    "new_string": "    print(\"  - fleiss_kappa.json\")\n    print(\"  - layer_effect_test.json\")\n\n\n# ---------------------------------------------------------------------------"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T16:28:55.416188+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T16:28:55.416359+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts && source .venv/bin/activate && python run_full_study.py --phase 3 2>&1",
  "description": "Run Phase 3 analysis with new layer effect test",
  "timeout": "300000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts && source .venv/bin/activate && python run_full_study.py --phase 3 2>&1",
    "description": "Run Phase 3 analysis with new layer effect test",
    "timeout": "300000"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T16:28:55.416525+00:00_

======================================== Phase 3 ========================================

Loaded 1200 judgments (2 models, 6 types)

========================================================================
FULL STUDY — STATISTICAL ANALYSIS REPORT
========================================================================

-- (a) Binary Effect: Ambiguous vs Unambiguous --

  Global: amb=40.8%  unamb=4.3%  D=+36.5%  chi2 p=0.0000

  Type                          Amb   Unamb       D  Fisher p
  ------------------------- ------- ------- ------- ---------
  authorization_scope        55.0%   2.0% +53.0%    0.0000
  conditional_precedence     35.0%   0.0% +35.0%    0.0000
  coreferential              25.0%   9.0% +16.0%    0.0042
  incompleteness             52.0%   3.0% +49.0%    0.0000
  lexical                    38.0%   8.0% +30.0%    0.0000
  scopal                     40.0%   4.0% +36.0%    0.0000

  Model               Amb   Unamb       D  Fisher p
  --------------- ------- ------- ------- ---------
  gpt-4.1          40.7%   6.0% +34.7%    0.0000
  gpt-5.4          41.0%   2.7% +38.3%    0.0000

-- (b) Type Effect: 6-way chi-square (ambiguous only) --

  Type                            Rate      N
  ------------------------- ---------- ------
  authorization_scope           55.0%    100
  conditional_precedence        35.0%    100
  coreferential                 25.0%    100
  incompleteness                52.0%    100
  lexical                       38.0%    100
  scopal                        40.0%    100

  chi2=25.614  p=0.0001  dof=5  Cramer's V=0.207

-- (c) Model Effect --

  Model               Rate  N_viol      N
  --------------- -------- ------- ------
  gpt-4.1           23.3%     140    600
  gpt-5.4           21.8%     131    600

  Overall: chi2 p=0.5807  V=0.016
  Ambiguous-only: chi2 p=1.0000

-- (d) Model x Type Interaction --

  [gpt-4.1] type chi2=9.891  p=0.0784  V=0.182
  [gpt-5.4] type chi2=23.439  p=0.0003  V=0.280

  gpt-4.1: incompleteness 
…[truncated 864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T16:28:55.416689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/full_study/analysis/layer_effect_test.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/full_study/analysis/layer_effect_test.json"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T16:28:55.416838+00:00_

1	{
2	  "test": "layer_effect (C3)",
3	  "specification_layer": {
4	    "types": [
5	      "authorization_scope",
6	      "conditional_precedence",
7	      "incompleteness"
8	    ],
9	    "n": 300,
10	    "violations": 142,
11	    "rate_pct": 47.33
12	  },
13	  "linguistic_layer": {
14	    "types": [
15	      "coreferential",
16	      "lexical",
17	      "scopal"
18	    ],
19	    "n": 300,
20	    "violations": 103,
21	    "rate_pct": 34.33
22	  },
23	  "delta_pp": 13.0,
24	  "bootstrap_ci_95": [
25	    5.33,
26	    20.67
27	  ],
28	  "chi_squared": {
29	    "statistic": 10.4927,
30	    "df": 1,
31	    "p": 0.001198
32	  },
33	  "cramers_v": 0.1322,
34	  "odds_ratio": {
35	    "or": 1.7189,
36	    "ci_95": [
37	      1.2372,
38	      2.3883
39	    ]
40	  },
41	  "per_type_detail": {
42	    "conditional_precedence": {
43	      "n": 100,
44	      "violations": 35,
45	      "rate": 35.0,
46	      "layer": "specification"
47	    },
48	    "incompleteness": {
49	      "n": 100,
50	      "violations": 52,
51	      "rate": 52.0,
52	      "layer": "specification"
53	    },
54	    "authorization_scope": {
55	      "n": 100,
56	      "violations": 55,
57	      "rate": 55.0,
58	      "layer": "specification"
59	    },
60	    "scopal": {
61	      "n": 100,
62	      "violations": 40,
63	      "rate": 40.0,
64	      "layer": "linguistic"
65	    },
66	    "lexical": {
67	      "n": 100,
68	      "violations": 38,
69	      "rate": 38.0,
70	      "layer": "linguistic"
71	    },
72	    "coreferential": {
73	      "n": 100,
74	      "violations": 25,
75	      "rate": 25.0,
76	      "layer": "linguistic"
77	    }
78	  }
79	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_c3_layer_effect_test_20260520T162759",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T16:28:55.417010+00:00_

结果符合预期：

| 指标 | 值 |
|---|---|
| spec_rate | 47.33% |
| ling_rate | 34.33% |
| delta_pp | +13.0 pp |
| chi2 | 10.49, p = 0.0012 |
| Cramér's V | 0.132 |
| OR | 1.72 [1.24, 2.39] |
| Bootstrap 95% CI | [5.33, 20.67] |

Specification-layer ambiguity 的违规率显著高于 linguistic-layer（p < 0.01），效应中等偏小。所有其他 analysis 文件均正常重新生成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_c3_layer_effect_test_20260520T162759"
}
```

</details>

---
