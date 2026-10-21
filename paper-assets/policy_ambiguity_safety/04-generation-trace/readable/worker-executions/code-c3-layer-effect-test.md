# code c3 layer effect test

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_code_c3_layer_effect_test_20260520T162759.log`
- **Structured JSON:** [`9761dad425467ba5ca38.json`](../../sessions/97/9761dad425467ba5ca38.json)

## Before a recorded user message

23 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "20700285-ddcd-44a2-8083-b39d85a75d0f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0519-4-projects-policy-ambiguity-safety/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779301800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a63e2544-e15f-4c69-8918-19898ab1db08",
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25"
}
```

---

### Assistant

_source line 4_

Looking at the target file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "746b370b-b9d3-4c8d-8c69-bbdda597c31b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6yLWCRJYNtoW9FtSfHypN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13326,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13326
      },
      "output_tokens": 2,
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01KBhGXWvyzS6tVJPAEvEot7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
  "offset": 1080,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "65b2cf1e-8de7-49ee-b02a-45f3fb2c3281",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q6yLWCRJYNtoW9FtSfHypN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13326,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13326
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-20T16:28:12.165Z_

<details><summary>↩ Tool result · `toolu_01KBhGXWvyzS6tVJPAEvEot7`</summary>

```text
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
1135	        "model_type_interaction": interact,
1136	        "n_judgments": len(df),
1137	    }
1138	    with open(ANALYSIS_DIR / "full_statistics.json", "w") as f:
1139	        json.dump(report, f, indent=2, default=str)
1140	
1141	    # Per-clause summary CSV
1142	    summary = analyze.per_clause_summary(df)
1143	    summary.to_csv(ANALYSIS_DIR / "per_clause_summary.csv", index=False)
1144	
1145	    # Aggregated rates CSV
1146	    dfc = df.copy()
1147	    dfc["violated"] = analyze.binarize_violations(dfc)
1148	    agg = dfc.groupby(
1149	        ["model", "ambiguity_type", "condition"]
1150	    )["violated"].agg(
1151	        violation_rate="mean", n_violations="sum", n_total="count",
1152	    ).reset_index()
1153	    agg.to_csv(ANALYSIS_DIR / "aggregated_rates.csv", index=False)
1154	
1155	    _print_full_report(binary, type_eff, model_eff, interact)
1156	
1157	    # Extended analyses (Dream reviewer)
1158	    clauses_path = config.ARTIFACTS_DIR / "clause_templates_full.json"
1159	    if clauses_path.exists():
1160	        with open(clauses_path) as f:
1161	            raw = json.load(f)
1162	        clauses_data = raw if isinstance(raw, list) else raw.get("clauses", raw)
1163	    else:
1164	        clauses_data = []
1165	
1166	    print("\n-- Extended analyses (Dream reviewer) --\n")
1167	    run_power_analysis(df, clauses_data)
1168	    run_tost_equivalence(df, clauses_data)
1169	    run_bootstrap_ci(df, clauses_data)
1170	    run_mcnemar_matched(df, clauses_data)
1171	    if clauses_data:
1172	        run_information_delta(df, clauses_data)
1173	    else:
1174	        print("  (skipped information_delta -- no clauses file)")
1175	    run_fleiss_kappa(df, clauses_data)
1176	
1177	    print(f"\nOutputs in {ANALYSIS_DIR}/:")
1178	    print("  - full_statistics.json")
1179	    print("  - per_clause_summary.csv")
1180	    print("  - aggregated_rates.csv")
1181	    print("  - power_analysis.json")
1182	    print("  - tost_equivalence.json")
1183	    print("  - bootstrap_ci.json")
1184	    print("  - mcnemar_matched.json")
1185	    if clauses_data:
1186	        print("  - information_delta.json")
1187	    print("  - fleiss_kappa.json")
1188	
1189	
1190	# ---------------------------------------------------------------------------
1191	# CLI
1192	# ---------------------------------------------------------------------------
1193	
1194	def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
1195	    parser = argparse.ArgumentParser(
1196	        description="Full study execution for policy ambiguity safety experiment.",
1197	        formatter_class=argparse.RawDescriptionHelpFormatter,
1198	        epilog="""\
1199	Examples:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "c06ef642-f04b-44c3-9f3c-83b0a31c5ea7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
      "content": "        interp = \"moderate agreement\"\n    elif kappa < 0.80:\n        interp = \"substantial agreement\"\n    else:\n        interp = \"almost perfect agreement\"\n\n    result = {\n        \"n_clauses\": N,\n        \"n_models\": n_models,\n        \"models\": models,\n        \"n_raters_per_clause\": {\n            \"min\": int(n_arr.min()),\n            \"max\": int(n_arr.max()),\n            \"mean\": round(float(n_arr.mean()), 1),\n        },\n        \"category_proportions\": {\n            \"violated\": round(float(p_j[0]), 4),\n            \"not_violated\": round(float(p_j[1]), 4),\n        },\n        \"fleiss_kappa\": round(float(kappa), 4),\n        \"se\": round(float(se), 4) if np.isfinite(se) else None,\n        \"z\": round(float(z_val), 4) if np.isfinite(z_val) else None,\n        \"p\": round(float(p_val), 6) if np.isfinite(p_val) else None,\n        \"interpretation\": interp,\n    }\n\n    out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):\n    \"\"\"Load all judgments and run the full analysis suite.\"\"\"\n    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)\n\n    df = _load_all_judgments(models)\n    if df.empty:\n        print(\"No judgments found. Run Phase 2 first.\")\n        return\n\n    print(f\"Loaded {len(df)} judgments ({df['model'].nunique()} models, \"\n          f\"{df['ambiguity_type'].nunique()} types)\")\n\n    binary = _binary_effect(df)\n    type_eff = _type_effect(df)\n    model_eff = _model_effect(df)\n    interact = _interaction(df)\n\n    # JSON report\n    report = {\n        \"binary_effect\": binary,\n        \"type_effect\": type_eff,\n        \"model_effect\": model_eff,\n        \"model_type_interaction\": interact,\n        \"n_judgments\": len(df),\n    }\n    with open(ANALYSIS_DIR / \"full_statistics.json\", \"w\") as f:\n        json.dump(report, f, indent=2, default=str)\n\n    # Per-clause summary CSV\n    summary = analyze.per_clause_summary(df)\n    summary.to_csv(ANALYSIS_DIR / \"per_clause_summary.csv\", index=False)\n\n    # Aggregated rates CSV\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n    agg = dfc.groupby(\n        [\"model\", \"ambiguity_type\", \"condition\"]\n    )[\"violated\"].agg(\n        violation_rate=\"mean\", n_violations=\"sum\", n_total=\"count\",\n    ).reset_index()\n    agg.to_csv(ANALYSIS_DIR / \"aggregated_rates.csv\", index=False)\n\n    _print_full_report(binary, type_eff, model_eff, interact)\n\n    # Extended analyses (Dream reviewer)\n    clauses_path = config.ARTIFACTS_DIR / \"clause_templates_full.json\"\n    if clauses_path.exists():\n        with open(clauses_path) as f:\n            raw = json.load(f)\n        clauses_data = raw if isinstance(raw, list) else raw.get(\"clauses\", raw)\n    else:\n        clauses_data = []\n\n    print(\"\\n-- Extended analyses (Dream reviewer) --\\n\")\n    run_power_analysis(df, clauses_data)\n    run_tost_equivalence(df, clauses_data)\n    run_bootstrap_ci(df, clauses_data)\n    run_mcnemar_matched(df, clauses_data)\n    if clauses_data:\n        run_information_delta(df, clauses_data)\n    else:\n        print(\"  (skipped information_delta -- no clauses file)\")\n    run_fleiss_kappa(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")\n    print(\"  - full_statistics.json\")\n    print(\"  - per_clause_summary.csv\")\n    print(\"  - aggregated_rates.csv\")\n    print(\"  - power_analysis.json\")\n    print(\"  - tost_equivalence.json\")\n    print(\"  - bootstrap_ci.json\")\n    print(\"  - mcnemar_matched.json\")\n    if clauses_data:\n        print(\"  - information_delta.json\")\n    print(\"  - fleiss_kappa.json\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args(argv: list[str] | None = None) -> argparse.Namespace:\n    parser = argparse.ArgumentParser(\n        description=\"Full study execution for policy ambiguity safety experiment.\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n        epilog=\"\"\"\\\nExamples:",
      "numLines": 120,
      "startLine": 1080,
      "totalLines": 1262
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. I need to:

1. Add `run_layer_effect_test()` function after `run_fleiss_kappa()` (after line 1110) and before `run_phase3()` (line 1113)
2. Call it in `run_phase3()` after `run_fleiss_kappa(df, clauses_data)` (line 1175)
3. Add the output line after `print("  - fleiss_kappa.json")` (line 1187)

Let me also check what imports are available at the top.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "e77a0068-b9d7-4caa-abd9-53f034fbcd0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D46ETLKebETqq2H27p3sU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1848,
      "cache_read_input_tokens": 25167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1848
      },
      "output_tokens": 10,
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

_source line 8_

Now I'll make the three edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "c5001cf0-189c-4659-a523-3078aa72bad7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D46ETLKebETqq2H27p3sU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1848,
      "cache_read_input_tokens": 25167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1848
      },
      "output_tokens": 10,
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01B2pQ7VFwCbvGXmzMTJ8NXw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
  "old_string": "    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):",
  "new_string": "    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_layer_effect_test(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"C3: Formal test of specification-layer vs linguistic-layer violation rates.\"\"\"\n    SPEC_TYPES = {\"incompleteness\", \"conditional_precedence\", \"authorization_scope\"}\n    LING_TYPES = {\"scopal\", \"lexical\", \"coreferential\"}\n\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n\n    # Filter to ambiguous condition only\n    amb = dfc[dfc[\"condition\"] == \"ambiguous\"].copy()\n    amb[\"layer\"] = amb[\"ambiguity_type\"].map(\n        lambda t: \"specification\" if t in SPEC_TYPES else \"linguistic\" if t in LING_TYPES else \"unknown\"\n    )\n    amb = amb[amb[\"layer\"] != \"unknown\"]\n\n    spec = amb[amb[\"layer\"] == \"specification\"]\n    ling = amb[amb[\"layer\"] == \"linguistic\"]\n\n    spec_n = len(spec)\n    spec_v = int(spec[\"violated\"].sum())\n    ling_n = len(ling)\n    ling_v = int(ling[\"violated\"].sum())\n\n    spec_rate = spec_v / spec_n if spec_n > 0 else 0\n    ling_rate = ling_v / ling_n if ling_n > 0 else 0\n    delta_pp = (spec_rate - ling_rate) * 100\n\n    from scipy.stats import chi2_contingency\n    table = np.array([\n        [spec_v, spec_n - spec_v],\n        [ling_v, ling_n - ling_v],\n    ])\n    chi2, p_val, dof, expected = chi2_contingency(table, correction=False)\n\n    n_total = spec_n + ling_n\n    cramers_v = np.sqrt(chi2 / n_total) if n_total > 0 else 0\n\n    a, b = spec_v, spec_n - spec_v\n    c, d = ling_v, ling_n - ling_v\n    if b > 0 and c > 0 and d > 0 and a > 0:\n        or_val = (a * d) / (b * c)\n        log_or = np.log(or_val)\n        se_log = np.sqrt(1/a + 1/b + 1/c + 1/d)\n        or_lo = float(np.exp(log_or - 1.96 * se_log))\n        or_hi = float(np.exp(log_or + 1.96 * se_log))\n    else:\n        or_val = or_lo = or_hi = float(\"nan\")\n\n    np.random.seed(42)\n    n_boot = 10000\n    spec_arr = spec[\"violated\"].values.astype(float)\n    ling_arr = ling[\"violated\"].values.astype(float)\n    boot_deltas = []\n    for _ in range(n_boot):\n        s_idx = np.random.randint(0, len(spec_arr), len(spec_arr))\n        l_idx = np.random.randint(0, len(ling_arr), len(ling_arr))\n        boot_deltas.append((spec_arr[s_idx].mean() - ling_arr[l_idx].mean()) * 100)\n    boot_deltas = np.array(boot_deltas)\n    ci_lo = float(np.percentile(boot_deltas, 2.5))\n    ci_hi = float(np.percentile(boot_deltas, 97.5))\n\n    per_type = {}\n    for atype in list(SPEC_TYPES) + list(LING_TYPES):\n        subset = amb[amb[\"ambiguity_type\"] == atype]\n        if len(subset) > 0:\n            rate = float(subset[\"violated\"].mean())\n            per_type[atype] = {\n                \"n\": len(subset),\n                \"violations\": int(subset[\"violated\"].sum()),\n                \"rate\": round(rate * 100, 2),\n                \"layer\": \"specification\" if atype in SPEC_TYPES else \"linguistic\",\n            }\n\n    result = {\n        \"test\": \"layer_effect (C3)\",\n        \"specification_layer\": {\n            \"types\": sorted(SPEC_TYPES),\n            \"n\": spec_n,\n            \"violations\": spec_v,\n            \"rate_pct\": round(spec_rate * 100, 2),\n        },\n        \"linguistic_layer\": {\n            \"types\": sorted(LING_TYPES),\n            \"n\": ling_n,\n            \"violations\": ling_v,\n            \"rate_pct\": round(ling_rate * 100, 2),\n        },\n        \"delta_pp\": round(delta_pp, 2),\n        \"bootstrap_ci_95\": [round(ci_lo, 2), round(ci_hi, 2)],\n        \"chi_squared\": {\n            \"statistic\": round(float(chi2), 4),\n            \"df\": int(dof),\n            \"p\": round(float(p_val), 6),\n        },\n        \"cramers_v\": round(float(cramers_v), 4),\n        \"odds_ratio\": {\n            \"or\": round(float(or_val), 4) if np.isfinite(or_val) else str(or_val),\n            \"ci_95\": [round(or_lo, 4) if np.isfinite(or_lo) else str(or_lo),\n                       round(or_hi, 4) if np.isfinite(or_hi) else str(or_hi)],\n        },\n        \"per_type_detail\": per_type,\n    }\n\n    out = ANALYSIS_DIR / \"layer_effect_test.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "272d45f5-d162-4909-a3da-c93563472b6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D46ETLKebETqq2H27p3sU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1848,
      "cache_read_input_tokens": 25167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1848
      },
      "output_tokens": 10,
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

_source line 10 · 2026-05-20T16:28:29.497Z_

<details><summary>↩ Tool result · `toolu_01B2pQ7VFwCbvGXmzMTJ8NXw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "cfc18a95-280a-45c9-a956-1810c4d6a4d4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
    "oldString": "    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):",
    "newString": "    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_layer_effect_test(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"C3: Formal test of specification-layer vs linguistic-layer violation rates.\"\"\"\n    SPEC_TYPES = {\"incompleteness\", \"conditional_precedence\", \"authorization_scope\"}\n    LING_TYPES = {\"scopal\", \"lexical\", \"coreferential\"}\n\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n\n    # Filter to ambiguous condition only\n    amb = dfc[dfc[\"condition\"] == \"ambiguous\"].copy()\n    amb[\"layer\"] = amb[\"ambiguity_type\"].map(\n        lambda t: \"specification\" if t in SPEC_TYPES else \"linguistic\" if t in LING_TYPES else \"unknown\"\n    )\n    amb = amb[amb[\"layer\"] != \"unknown\"]\n\n    spec = amb[amb[\"layer\"] == \"specification\"]\n    ling = amb[amb[\"layer\"] == \"linguistic\"]\n\n    spec_n = len(spec)\n    spec_v = int(spec[\"violated\"].sum())\n    ling_n = len(ling)\n    ling_v = int(ling[\"violated\"].sum())\n\n    spec_rate = spec_v / spec_n if spec_n > 0 else 0\n    ling_rate = ling_v / ling_n if ling_n > 0 else 0\n    delta_pp = (spec_rate - ling_rate) * 100\n\n    from scipy.stats import chi2_contingency\n    table = np.array([\n        [spec_v, spec_n - spec_v],\n        [ling_v, ling_n - ling_v],\n    ])\n    chi2, p_val, dof, expected = chi2_contingency(table, correction=False)\n\n    n_total = spec_n + ling_n\n    cramers_v = np.sqrt(chi2 / n_total) if n_total > 0 else 0\n\n    a, b = spec_v, spec_n - spec_v\n    c, d = ling_v, ling_n - ling_v\n    if b > 0 and c > 0 and d > 0 and a > 0:\n        or_val = (a * d) / (b * c)\n        log_or = np.log(or_val)\n        se_log = np.sqrt(1/a + 1/b + 1/c + 1/d)\n        or_lo = float(np.exp(log_or - 1.96 * se_log))\n        or_hi = float(np.exp(log_or + 1.96 * se_log))\n    else:\n        or_val = or_lo = or_hi = float(\"nan\")\n\n    np.random.seed(42)\n    n_boot = 10000\n    spec_arr = spec[\"violated\"].values.astype(float)\n    ling_arr = ling[\"violated\"].values.astype(float)\n    boot_deltas = []\n    for _ in range(n_boot):\n        s_idx = np.random.randint(0, len(spec_arr), len(spec_arr))\n        l_idx = np.random.randint(0, len(ling_arr), len(ling_arr))\n        boot_deltas.append((spec_arr[s_idx].mean() - ling_arr[l_idx].mean()) * 100)\n    boot_deltas = np.array(boot_deltas)\n    ci_lo = float(np.percentile(boot_deltas, 2.5))\n    ci_hi = float(np.percentile(boot_deltas, 97.5))\n\n    per_type = {}\n    for atype in list(SPEC_TYPES) + list(LING_TYPES):\n        subset = amb[amb[\"ambiguity_type\"] == atype]\n        if len(subset) > 0:\n            rate = float(subset[\"violated\"].mean())\n            per_type[atype] = {\n                \"n\": len(subset),\n                \"violations\": int(subset[\"violated\"].sum()),\n                \"rate\": round(rate * 100, 2),\n                \"layer\": \"specification\" if atype in SPEC_TYPES else \"linguistic\",\n            }\n\n    result = {\n        \"test\": \"layer_effect (C3)\",\n        \"specification_layer\": {\n            \"types\": sorted(SPEC_TYPES),\n            \"n\": spec_n,\n            \"violations\": spec_v,\n            \"rate_pct\": round(spec_rate * 100, 2),\n        },\n        \"linguistic_layer\": {\n            \"types\": sorted(LING_TYPES),\n            \"n\": ling_n,\n            \"violations\": ling_v,\n            \"rate_pct\": round(ling_rate * 100, 2),\n        },\n        \"delta_pp\": round(delta_pp, 2),\n        \"bootstrap_ci_95\": [round(ci_lo, 2), round(ci_hi, 2)],\n        \"chi_squared\": {\n            \"statistic\": round(float(chi2), 4),\n            \"df\": int(dof),\n            \"p\": round(float(p_val), 6),\n        },\n        \"cramers_v\": round(float(cramers_v), 4),\n        \"odds_ratio\": {\n            \"or\": round(float(or_val), 4) if np.isfinite(or_val) else str(or_val),\n            \"ci_95\": [round(or_lo, 4) if np.isfinite(or_lo) else str(or_lo),\n                       round(or_hi, 4) if np.isfinite(or_hi) else str(or_hi)],\n        },\n        \"per_type_detail\": per_type,\n    }\n\n    out = ANALYSIS_DIR / \"layer_effect_test.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Full study execution script for policy ambiguity safety experiments.\n\nOrchestrates the complete experiment pipeline:\n  Phase 1: Episode generation (300 clauses x 2 conditions x 2 models = 1,200 episodes)\n  Phase 2: Cross-judge evaluation (gpt-5.4 episodes judged by gpt-4.1, vice versa)\n  Phase 3: Statistical analysis (binary/type/model effects + interactions)\n\nInput:  artifacts/clause_templates_full.json (300 clauses, 6 types x 50)\nOutput: artifacts/full_study/{episodes,judgments,analysis}/\n\nDependencies: harness.py, judge.py, analyze.py, config.py\n\"\"\"\n\nimport argparse\nimport asyncio\nimport json\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport config\nimport harness\nimport judge\nimport analyze\n\n# ---------------------------------------------------------------------------\n# Paths\n# ---------------------------------------------------------------------------\n\nFULL_STUDY_DIR = config.ARTIFACTS_DIR / \"full_study\"\nEPISODES_DIR = FULL_STUDY_DIR / \"episodes\"\nJUDGMENTS_DIR = FULL_STUDY_DIR / \"judgments\"\nANALYSIS_DIR = FULL_STUDY_DIR / \"analysis\"\nERRORS_FILE = FULL_STUDY_DIR / \"errors.jsonl\"\n\nDEFAULT_MODELS = [\"gpt-5.4\", \"gpt-4.1\", \"claude-sonnet-4-6\"]\n\n\n# ---------------------------------------------------------------------------\n# Phase 1: Episode Generation\n# ---------------------------------------------------------------------------\n\ndef _load_completed_episodes(model_dir: Path) -> set[str]:\n    \"\"\"Return set of 'clause_id|condition' keys already completed.\"\"\"\n    completed = set()\n    episodes_file = model_dir / \"episodes.jsonl\"\n    if episodes_file.exists():\n        with open(episodes_file) as f:\n            for line in f:\n                if line.strip():\n                    rec = json.loads(line)\n                    completed.add(f\"{rec['clause_id']}|{rec['condition']}\")\n    return completed\n\n\nasync def run_phase1(\n    clauses: list[dict],\n    models: list[str],\n    concurrency: int,\n    resume: bool,\n):\n    \"\"\"Generate episodes for all model x clause x condition combinations.\"\"\"\n    FULL_STUDY_DIR.mkdir(parents=True, exist_ok=True)\n\n    print(\"Preflight API check...\")\n    for m in models:\n        try:\n            await harness.preflight_check(m)\n            print(f\"  {m}: OK\")\n        except Exception as e:\n            print(f\"  {m}: FAILED — {e}\")\n            raise SystemExit(f\"Preflight failed for {m}. Fix API key/endpoint before running.\")\n\n    total_done = 0\n    total_errors = 0\n    total_skipped = 0\n\n    for model_name in models:\n        model_dir = EPISODES_DIR / model_name\n        model_dir.mkdir(parents=True, exist_ok=True)\n\n        completed = _load_completed_episodes(model_dir) if resume else set()\n        tasks = []\n        for clause in clauses:\n            for condition in (\"ambiguous\", \"unambiguous\"):\n                key = f\"{clause['clause_id']}|{condition}\"\n                if key in completed:\n                    total_skipped += 1\n                    continue\n                tasks.append((clause, condition))\n\n        if not tasks:\n            print(f\"[{model_name}] All {len(completed)} episodes complete.\")\n            continue\n\n        print(f\"[{model_name}] {len(tasks)} episodes to run \"\n              f\"(skipping {len(completed)}, concurrency={concurrency})\")\n\n        semaphore = asyncio.Semaphore(concurrency)\n        output_file = model_dir / \"episodes.jsonl\"\n        lock = asyncio.Lock()\n        done = 0\n        errors = 0\n\n        async def _run_one(clause, condition, _model=model_name):\n            nonlocal done, errors\n            async with semaphore:\n                try:\n                    result = await harness.run_episode(clause, condition, _model)\n                    validity = harness.validate_episode(result)\n                    if validity != \"ok\":\n                        raise RuntimeError(\n                            f\"Episode {validity}: {result.get('error', 'no assistant response')}\"\n                        )\n                    async with lock:\n                        with open(output_file, \"a\") as f:\n                            f.write(json.dumps(result, ensure_ascii=False) + \"\\n\")\n                        done += 1\n                        if done % 50 == 0:\n                            print(f\"  [{_model}] {done}/{len(tasks)}\")\n                except Exception as e:\n                    async with lock:\n                        errors += 1\n                        with open(ERRORS_FILE, \"a\") as f:\n                            f.write(json.dumps({\n                                \"phase\": 1, \"model\": _model,\n                                \"clause_id\": clause[\"clause_id\"],\n                                \"condition\": condition,\n                                \"error\": str(e),\n                                \"timestamp\": time.time(),\n                            }, ensure_ascii=False) + \"\\n\")\n\n        await asyncio.gather(*[_run_one(c, cond) for c, cond in tasks])\n        print(f\"  [{model_name}] {done} done, {errors} errors\")\n        total_done += done\n        total_errors += errors\n\n    print(f\"\\nPhase 1 summary: {total_done} done / {total_errors} errors / \"\n          f\"{total_skipped} skipped\")\n\n\n# ---------------------------------------------------------------------------\n# Phase 2: Cross-Judge Evaluation\n# ---------------------------------------------------------------------------\n\ndef _load_judged_ids(model_dir: Path) -> set[str]:\n    \"\"\"Return set of episode_ids already judged.\"\"\"\n    judged = set()\n    judgments_file = model_dir / \"judgments.jsonl\"\n    if judgments_file.exists():\n        with open(judgments_file) as f:\n            for line in f:\n                if line.strip():\n                    judged.add(json.loads(line)[\"episode_id\"])\n    return judged\n\n\nasync def run_phase2(\n    clauses: list[dict],\n    models: list[str],\n    concurrency: int,\n    resume: bool,\n):\n    \"\"\"Cross-judge all episodes (each model's episodes judged by the other).\"\"\"\n    clause_index = judge.build_clause_index(clauses)\n    total_done = 0\n    total_errors = 0\n    total_skipped = 0\n\n    for model_name in models:\n        ep_dir = EPISODES_DIR / model_name\n        if not ep_dir.exists():\n            print(f\"[{model_name}] No episodes found — run Phase 1 first.\")\n            continue\n\n        episodes = judge.load_episodes(ep_dir)\n        if not episodes:\n            print(f\"[{model_name}] No episode files found.\")\n            continue\n\n        judge_model = config.CROSS_JUDGE_MAP[model_name]\n        jdg_dir = JUDGMENTS_DIR / model_name\n        jdg_dir.mkdir(parents=True, exist_ok=True)\n\n        judged_ids = _load_judged_ids(jdg_dir) if resume else set()\n        pending = [ep for ep in episodes if ep[\"episode_id\"] not in judged_ids]\n        total_skipped += len(episodes) - len(pending)\n\n        if not pending:\n            print(f\"[{model_name}] All {len(episodes)} episodes already judged.\")\n            continue\n\n        print(f\"[{model_name}] Judging {len(pending)} episodes \"\n              f\"(judge={judge_model}, concurrency={concurrency})\")\n\n        semaphore = asyncio.Semaphore(concurrency)\n        output_file = jdg_dir / \"judgments.jsonl\"\n        lock = asyncio.Lock()\n        done = 0\n        errors = 0\n\n        async def _judge_one(episode, _model=model_name):\n            nonlocal done, errors\n            async with semaphore:\n                try:\n                    result = await judge.judge_episode(episode, clause_index)\n                    async with lock:\n                        with open(output_file, \"a\") as f:\n                            f.write(json.dumps(result, ensure_ascii=False) + \"\\n\")\n                        done += 1\n                        if done % 50 == 0:\n                            print(f\"  [{_model}] {done}/{len(pending)} judged\")\n                except Exception as e:\n                    async with lock:\n                        errors += 1\n                        with open(ERRORS_FILE, \"a\") as f:\n                            f.write(json.dumps({\n                                \"phase\": 2, \"model\": _model,\n                                \"episode_id\": episode.get(\"episode_id\", \"?\"),\n                                \"error\": str(e),\n                                \"timestamp\": time.time(),\n                            }, ensure_ascii=False) + \"\\n\")\n\n        await asyncio.gather(*[_judge_one(ep) for ep in pending])\n        print(f\"  [{model_name}] {done} judged, {errors} errors\")\n        total_done += done\n        total_errors += errors\n\n    print(f\"\\nPhase 2 summary: {total_done} done / {total_errors} errors / \"\n          f\"{total_skipped} skipped\")\n\n\n# ---------------------------------------------------------------------------\n# Phase 3: Analysis\n# ---------------------------------------------------------------------------\n\ndef _load_all_judgments(models: list[str]) -> pd.DataFrame:\n    \"\"\"Load judgments from all model subdirectories into one DataFrame.\"\"\"\n    records = []\n    for model_name in models:\n        jdg_dir = JUDGMENTS_DIR / model_name\n        if not jdg_dir.exists():\n            continue\n        for jsonl_file in jdg_dir.glob(\"*.jsonl\"):\n            with open(jsonl_file) as f:\n                for line in f:\n                    if not line.strip():\n                        continue\n                    rec = json.loads(line)\n                    records.append({\n                        \"episode_id\": rec[\"episode_id\"],\n                        \"clause_id\": rec[\"clause_id\"],\n                        \"ambiguity_type\": rec[\"ambiguity_type\"],\n                        \"condition\": rec[\"condition\"],\n                        \"model\": rec[\"model\"],\n                        \"violation_level\": rec[\"judgment\"][\"violation_level\"],\n                        \"confidence\": rec[\"judgment\"][\"confidence\"],\n                        \"judge_model\": rec[\"judge_model\"],\n                    })\n    df = pd.DataFrame(records)\n    if df.empty:\n        return df\n    level_order = pd.CategoricalDtype(\n        categories=config.VIOLATION_LEVELS, ordered=True\n    )\n    df[\"violation_level\"] = df[\"violation_level\"].astype(level_order)\n    return df\n\n\ndef _binary_effect(df: pd.DataFrame) -> dict:\n    \"\"\"(a) Ambiguous vs unambiguous violation rates: global, per-type, per-model.\"\"\"\n    df = df.copy()\n    df[\"violated\"] = analyze.binarize_violations(df)\n\n    # Global\n    cond_rates = df.groupby(\"condition\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    amb_r = float(cond_rates.loc[\"ambiguous\", \"mean\"]) if \"ambiguous\" in cond_rates.index else float(\"nan\")\n    una_r = float(cond_rates.loc[\"unambiguous\", \"mean\"]) if \"unambiguous\" in cond_rates.index else float(\"nan\")\n    ct = pd.crosstab(df[\"condition\"], df[\"violated\"])\n    if ct.shape == (2, 2):\n        chi2, p, _, _ = stats.chi2_contingency(ct.values)\n    else:\n        chi2, p = float(\"nan\"), float(\"nan\")\n    glob = {\n        \"ambiguous_rate\": amb_r, \"unambiguous_rate\": una_r,\n        \"difference\": amb_r - una_r if not (np.isnan(amb_r) or np.isnan(una_r)) else None,\n        \"chi2\": float(chi2), \"p\": float(p),\n    }\n\n    # Per-type\n    per_type = {}\n    for atype, tdf in df.groupby(\"ambiguity_type\"):\n        tr = tdf.groupby(\"condition\")[\"violated\"].mean()\n        a, u = tr.get(\"ambiguous\", np.nan), tr.get(\"unambiguous\", np.nan)\n        ct_t = pd.crosstab(tdf[\"condition\"], tdf[\"violated\"])\n        fp = float(stats.fisher_exact(ct_t.values)[1]) if ct_t.shape == (2, 2) else float(\"nan\")\n        per_type[atype] = {\n            \"ambiguous_rate\": float(a), \"unambiguous_rate\": float(u),\n            \"difference\": float(a - u) if not (np.isnan(a) or np.isnan(u)) else None,\n            \"fisher_p\": fp,\n        }\n\n    # Per-model\n    per_model = {}\n    for mname, mdf in df.groupby(\"model\"):\n        mr = mdf.groupby(\"condition\")[\"violated\"].mean()\n        a, u = mr.get(\"ambiguous\", np.nan), mr.get(\"unambiguous\", np.nan)\n        ct_m = pd.crosstab(mdf[\"condition\"], mdf[\"violated\"])\n        fp = float(stats.fisher_exact(ct_m.values)[1]) if ct_m.shape == (2, 2) else float(\"nan\")\n        per_model[mname] = {\n            \"ambiguous_rate\": float(a), \"unambiguous_rate\": float(u),\n            \"difference\": float(a - u) if not (np.isnan(a) or np.isnan(u)) else None,\n            \"fisher_p\": fp,\n        }\n\n    return {\"global\": glob, \"per_type\": per_type, \"per_model\": per_model}\n\n\ndef _type_effect(df: pd.DataFrame) -> dict:\n    \"\"\"(b) 6-way chi-square across ambiguity types (ambiguous episodes only).\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    type_rates = amb.groupby(\"ambiguity_type\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    type_rates.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n\n    ct = pd.crosstab(amb[\"ambiguity_type\"], amb[\"violated\"])\n    if ct.shape[0] >= 2 and ct.shape[1] >= 2:\n        chi2, p, dof, _ = stats.chi2_contingency(ct.values)\n        v = analyze.cramers_v(ct.values)\n    else:\n        chi2, p, dof, v = float(\"nan\"), float(\"nan\"), 0, 0.0\n\n    return {\n        \"rates\": type_rates.to_dict(orient=\"index\"),\n        \"chi2\": float(chi2), \"p\": float(p), \"dof\": int(dof),\n        \"cramers_v\": float(v),\n    }\n\n\ndef _model_effect(df: pd.DataFrame) -> dict:\n    \"\"\"(c) Model comparison: gpt-5.4 vs gpt-4.1 violation rates.\"\"\"\n    df = df.copy()\n    df[\"violated\"] = analyze.binarize_violations(df)\n\n    model_rates = df.groupby(\"model\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    model_rates.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n\n    ct = pd.crosstab(df[\"model\"], df[\"violated\"])\n    if ct.shape == (2, 2):\n        chi2, p, _, _ = stats.chi2_contingency(ct.values)\n        v = analyze.cramers_v(ct.values)\n    else:\n        chi2, p, v = float(\"nan\"), float(\"nan\"), 0.0\n\n    # Ambiguous-only subset\n    amb = df[df[\"condition\"] == \"ambiguous\"]\n    amb_rates = amb.groupby(\"model\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    amb_rates.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n    ct_a = pd.crosstab(amb[\"model\"], amb[\"violated\"])\n    if ct_a.shape == (2, 2):\n        chi2_a, p_a, _, _ = stats.chi2_contingency(ct_a.values)\n    else:\n        chi2_a, p_a = float(\"nan\"), float(\"nan\")\n\n    return {\n        \"overall\": model_rates.to_dict(orient=\"index\"),\n        \"overall_chi2\": float(chi2), \"overall_p\": float(p),\n        \"cramers_v\": float(v),\n        \"ambiguous_only\": amb_rates.to_dict(orient=\"index\"),\n        \"ambiguous_chi2\": float(chi2_a), \"ambiguous_p\": float(p_a),\n    }\n\n\ndef _interaction(df: pd.DataFrame) -> dict:\n    \"\"\"(d) Model x Type interaction (ambiguous episodes only).\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    per_model_rates = {}\n    per_model_chi2 = {}\n    rankings = {}\n\n    for mname, mdf in amb.groupby(\"model\"):\n        tr = mdf.groupby(\"ambiguity_type\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n        tr.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n        per_model_rates[mname] = tr.to_dict(orient=\"index\")\n\n        ct = pd.crosstab(mdf[\"ambiguity_type\"], mdf[\"violated\"])\n        if ct.shape[0] >= 2 and ct.shape[1] >= 2:\n            chi2, p, dof, _ = stats.chi2_contingency(ct.values)\n            v = analyze.cramers_v(ct.values)\n        else:\n            chi2, p, dof, v = float(\"nan\"), float(\"nan\"), 0, 0.0\n        per_model_chi2[mname] = {\n            \"chi2\": float(chi2), \"p\": float(p),\n            \"dof\": int(dof), \"cramers_v\": float(v),\n        }\n\n        sorted_types = sorted(\n            per_model_rates[mname].items(),\n            key=lambda x: x[1][\"violation_rate\"], reverse=True,\n        )\n        rankings[mname] = [t[0] for t in sorted_types]\n\n    return {\n        \"per_model_type_rates\": per_model_rates,\n        \"per_model_chi2\": per_model_chi2,\n        \"type_rankings\": rankings,\n    }\n\n\ndef _print_full_report(binary: dict, type_eff: dict,\n                       model_eff: dict, interact: dict):\n    \"\"\"Print formatted analysis report to console.\"\"\"\n    print(\"\\n\" + \"=\" * 72)\n    print(\"FULL STUDY — STATISTICAL ANALYSIS REPORT\")\n    print(\"=\" * 72)\n\n    # (a) Binary effect\n    print(\"\\n-- (a) Binary Effect: Ambiguous vs Unambiguous --\\n\")\n    g = binary[\"global\"]\n    diff_str = f\"{g['difference']:+.1%}\" if g[\"difference\"] is not None else \"N/A\"\n    print(f\"  Global: amb={g['ambiguous_rate']:.1%}  unamb={g['unambiguous_rate']:.1%}\"\n          f\"  D={diff_str}  chi2 p={g['p']:.4f}\")\n\n    print(f\"\\n  {'Type':<25} {'Amb':>7} {'Unamb':>7} {'D':>7} {'Fisher p':>9}\")\n    print(f\"  {'-'*25} {'-'*7} {'-'*7} {'-'*7} {'-'*9}\")\n    for atype in sorted(binary[\"per_type\"]):\n        r = binary[\"per_type\"][atype]\n        d = r[\"difference\"]\n        if d is not None:\n            print(f\"  {atype:<25} {r['ambiguous_rate']:>6.1%} {r['unambiguous_rate']:>6.1%}\"\n                  f\" {d:>+6.1%} {r['fisher_p']:>9.4f}\")\n        else:\n            print(f\"  {atype:<25}  insufficient data\")\n\n    print(f\"\\n  {'Model':<15} {'Amb':>7} {'Unamb':>7} {'D':>7} {'Fisher p':>9}\")\n    print(f\"  {'-'*15} {'-'*7} {'-'*7} {'-'*7} {'-'*9}\")\n    for mname in sorted(binary[\"per_model\"]):\n        r = binary[\"per_model\"][mname]\n        d = r[\"difference\"]\n        if d is not None:\n            print(f\"  {mname:<15} {r['ambiguous_rate']:>6.1%} {r['unambiguous_rate']:>6.1%}\"\n                  f\" {d:>+6.1%} {r['fisher_p']:>9.4f}\")\n\n    # (b) Type effect\n    print(\"\\n-- (b) Type Effect: 6-way chi-square (ambiguous only) --\\n\")\n    rates = type_eff.get(\"rates\", {})\n    print(f\"  {'Type':<25} {'Rate':>10} {'N':>6}\")\n    print(f\"  {'-'*25} {'-'*10} {'-'*6}\")\n    for atype in sorted(rates):\n        r = rates[atype]\n        print(f\"  {atype:<25} {r['violation_rate']:>9.1%} {r['n_total']:>6.0f}\")\n    print(f\"\\n  chi2={type_eff['chi2']:.3f}  p={type_eff['p']:.4f}\"\n          f\"  dof={type_eff['dof']}  Cramer's V={type_eff['cramers_v']:.3f}\")\n\n    # (c) Model effect\n    print(\"\\n-- (c) Model Effect --\\n\")\n    ov = model_eff.get(\"overall\", {})\n    print(f\"  {'Model':<15} {'Rate':>8} {'N_viol':>7} {'N':>6}\")\n    print(f\"  {'-'*15} {'-'*8} {'-'*7} {'-'*6}\")\n    for mname in sorted(ov):\n        r = ov[mname]\n        print(f\"  {mname:<15} {r['violation_rate']:>7.1%} {r['n_violations']:>7.0f}\"\n              f\" {r['n_total']:>6.0f}\")\n    print(f\"\\n  Overall: chi2 p={model_eff['overall_p']:.4f}  V={model_eff['cramers_v']:.3f}\")\n    print(f\"  Ambiguous-only: chi2 p={model_eff['ambiguous_p']:.4f}\")\n\n    # (d) Interaction\n    print(\"\\n-- (d) Model x Type Interaction --\\n\")\n    for mname in sorted(interact.get(\"per_model_chi2\", {})):\n        c = interact[\"per_model_chi2\"][mname]\n        print(f\"  [{mname}] type chi2={c['chi2']:.3f}  p={c['p']:.4f}\"\n              f\"  V={c['cramers_v']:.3f}\")\n    print()\n    for mname in sorted(interact.get(\"type_rankings\", {})):\n        ranking = interact[\"type_rankings\"][mname]\n        print(f\"  {mname}: {' > '.join(ranking)}\")\n\n    print(\"\\n\" + \"=\" * 72)\n\n\n# ---------------------------------------------------------------------------\n# Phase 3 Extended: Dream reviewer analyses (A3, A4, A10 + bootstrap/McNemar/Fleiss)\n# ---------------------------------------------------------------------------\n\ndef run_power_analysis(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Dream A3: Power analysis for C2 (type uniformity) and C3 (per-type).\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    types = sorted(amb[\"ambiguity_type\"].unique())\n    n_types = len(types)\n    alpha = 0.05\n    target_power = 0.80\n\n    def _find_mde(n_total, df_val):\n        crit = stats.chi2.ppf(1 - alpha, df_val)\n        lo, hi = 1e-4, 1.0\n        for _ in range(200):\n            mid = (lo + hi) / 2\n            pwr = 1 - stats.ncx2.cdf(crit, df_val, n_total * mid ** 2)\n            if pwr < target_power:\n                lo = mid\n            else:\n                hi = mid\n        return (lo + hi) / 2\n\n    def _compute_power(w, n_total, df_val):\n        crit = stats.chi2.ppf(1 - alpha, df_val)\n        return float(1 - stats.ncx2.cdf(crit, df_val, n_total * w ** 2))\n\n    c2_n_per_type = 200\n    c2_n_total = c2_n_per_type * n_types\n    c2_df = max(n_types - 1, 1)\n    c2_mde = _find_mde(c2_n_total, c2_df)\n\n    c3_n = 200\n    c3_df = 1\n    c3_mde = _find_mde(c3_n, c3_df)\n\n    ct = pd.crosstab(amb[\"ambiguity_type\"], amb[\"violated\"])\n    observed_v = (\n        analyze.cramers_v(ct.values)\n        if ct.shape[0] >= 2 and ct.shape[1] >= 2\n        else 0.0\n    )\n\n    actual_n = len(amb)\n    mde_actual = _find_mde(actual_n, c2_df)\n    power_at_observed = (\n        _compute_power(observed_v, actual_n, c2_df) if observed_v > 0 else 0.0\n    )\n\n    underpowered = observed_v < 0.20 and c2_mde > observed_v\n\n    result = {\n        \"c2_type_uniformity\": {\n            \"design_N_per_type\": c2_n_per_type,\n            \"design_N_total\": c2_n_total,\n            \"n_types\": n_types,\n            \"df\": c2_df,\n            \"alpha\": alpha,\n            \"target_power\": target_power,\n            \"mde_cramers_v\": round(c2_mde, 4),\n        },\n        \"c3_per_type_comparison\": {\n            \"design_N\": c3_n,\n            \"df\": c3_df,\n            \"alpha\": alpha,\n            \"target_power\": target_power,\n            \"mde_cramers_v\": round(c3_mde, 4),\n        },\n        \"observed_cramers_v\": round(float(observed_v), 4),\n        \"actual_sample\": {\n            \"N_total\": actual_n,\n            \"per_type\": {\n                t: int(v)\n                for t, v in amb.groupby(\"ambiguity_type\").size().items()\n            },\n            \"mde_cramers_v\": round(mde_actual, 4),\n            \"power_at_observed\": round(power_at_observed, 4),\n        },\n        \"underpowered_warning\": underpowered,\n    }\n\n    out = ANALYSIS_DIR / \"power_analysis.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_tost_equivalence(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Dream A4: TOST equivalence test for C2 type uniformity.\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    types = sorted(amb[\"ambiguity_type\"].unique())\n    margins = [0.15, 0.10]\n\n    results_by_margin = {}\n    for margin in margins:\n        pairwise = []\n        for i in range(len(types)):\n            for j in range(i + 1, len(types)):\n                t1, t2 = types[i], types[j]\n                d1 = amb[amb[\"ambiguity_type\"] == t1][\"violated\"]\n                d2 = amb[amb[\"ambiguity_type\"] == t2][\"violated\"]\n                p1, n1 = float(d1.mean()), len(d1)\n                p2, n2 = float(d2.mean()), len(d2)\n                diff = p1 - p2\n\n                if n1 > 0 and n2 > 0:\n                    se = np.sqrt(\n                        p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2\n                    )\n                else:\n                    se = float(\"inf\")\n\n                if se > 0 and np.isfinite(se):\n                    z_lower = (diff + margin) / se\n                    p_lower = float(1 - stats.norm.cdf(z_lower))\n                    z_upper = (diff - margin) / se\n                    p_upper = float(stats.norm.cdf(z_upper))\n                    tost_p = max(p_lower, p_upper)\n                    equivalent = tost_p < 0.05\n                else:\n                    z_lower = z_upper = tost_p = float(\"nan\")\n                    p_lower = p_upper = float(\"nan\")\n                    equivalent = False\n\n                pairwise.append({\n                    \"type_1\": t1,\n                    \"type_2\": t2,\n                    \"rate_1\": round(p1, 4),\n                    \"rate_2\": round(p2, 4),\n                    \"difference\": round(diff, 4),\n                    \"se\": round(float(se), 4),\n                    \"z_lower\": round(float(z_lower), 4),\n                    \"p_lower\": round(float(p_lower), 4),\n                    \"z_upper\": round(float(z_upper), 4),\n                    \"p_upper\": round(float(p_upper), 4),\n                    \"tost_p\": round(float(tost_p), 4),\n                    \"equivalent\": equivalent,\n                })\n\n        all_equiv = all(p[\"equivalent\"] for p in pairwise) if pairwise else False\n        results_by_margin[f\"margin_{int(margin * 100)}pp\"] = {\n            \"margin\": margin,\n            \"pairwise\": pairwise,\n            \"all_pairs_equivalent\": all_equiv,\n        }\n\n    result = {\n        \"test\": \"TOST two one-sided z-tests for proportions\",\n        \"margin_justification\": (\n            \"15pp = practical significance threshold for policy remediation \"\n            \"cost; 10pp = stricter robustness check\"\n        ),\n        **results_by_margin,\n    }\n\n    out = ANALYSIS_DIR / \"tost_equivalence.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef _bca_ci(g1: np.ndarray, g2: np.ndarray, rng, B: int = 10000,\n            alpha: float = 0.05) -> dict:\n    \"\"\"BCa bootstrap CI for difference in means (g1 - g2).\"\"\"\n    n1, n2 = len(g1), len(g2)\n    if n1 == 0 or n2 == 0:\n        return {\"observed_diff\": None, \"ci_lower\": None, \"ci_upper\": None}\n\n    observed = float(g1.mean() - g2.mean())\n\n    idx1 = rng.integers(0, n1, size=(B, n1))\n    idx2 = rng.integers(0, n2, size=(B, n2))\n    boot_stats = g1[idx1].mean(axis=1) - g2[idx2].mean(axis=1)\n\n    prop_below = np.mean(boot_stats < observed)\n    prop_below = np.clip(prop_below, 1 / (B + 1), B / (B + 1))\n    z0 = stats.norm.ppf(prop_below)\n\n    if n1 >= 2 and n2 >= 2:\n        jack = np.empty(n1 + n2)\n        g1_sum, g2_mean = g1.sum(), g2.mean()\n        g1_mean, g2_sum = g1.mean(), g2.sum()\n        for i in range(n1):\n            jack[i] = (g1_sum - g1[i]) / (n1 - 1) - g2_mean\n        for j in range(n2):\n            jack[n1 + j] = g1_mean - (g2_sum - g2[j]) / (n2 - 1)\n        jm = jack.mean()\n        d = jm - jack\n        denom = 6 * np.sum(d ** 2) ** 1.5\n        a = float(np.sum(d ** 3) / denom) if denom > 0 else 0.0\n    else:\n        a = 0.0\n\n    z_lo = stats.norm.ppf(alpha / 2)\n    z_hi = stats.norm.ppf(1 - alpha / 2)\n\n    def _adj(z):\n        num = z0 + z\n        den = 1 - a * num\n        if abs(den) < 1e-12:\n            return 0.5\n        return stats.norm.cdf(z0 + num / den)\n\n    a1 = np.clip(_adj(z_lo), 0.5 / B, 1 - 0.5 / B)\n    a2 = np.clip(_adj(z_hi), 0.5 / B, 1 - 0.5 / B)\n\n    return {\n        \"observed_diff\": round(observed, 4),\n        \"ci_lower\": round(float(np.percentile(boot_stats, 100 * a1)), 4),\n        \"ci_upper\": round(float(np.percentile(boot_stats, 100 * a2)), 4),\n        \"z0\": round(float(z0), 4),\n        \"acceleration\": round(a, 6),\n    }\n\n\ndef run_bootstrap_ci(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"BCa bootstrap 95% CIs for all pairwise comparisons.\"\"\"\n    B = 10000\n    rng = np.random.default_rng(42)\n\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc).astype(float)\n\n    results: dict = {\"n_resamples\": B}\n\n    # Global ambig vs unambig\n    amb_v = dfc.loc[dfc[\"condition\"] == \"ambiguous\", \"violated\"].values\n    una_v = dfc.loc[dfc[\"condition\"] == \"unambiguous\", \"violated\"].values\n    results[\"ambig_vs_unambig_global\"] = _bca_ci(amb_v, una_v, rng, B)\n\n    # Per-type ambig vs unambig\n    per_type = {}\n    for atype in sorted(dfc[\"ambiguity_type\"].unique()):\n        tdf = dfc[dfc[\"ambiguity_type\"] == atype]\n        a = tdf.loc[tdf[\"condition\"] == \"ambiguous\", \"violated\"].values\n        u = tdf.loc[tdf[\"condition\"] == \"unambiguous\", \"violated\"].values\n        per_type[atype] = _bca_ci(a, u, rng, B)\n    results[\"ambig_vs_unambig_per_type\"] = per_type\n\n    # Type pairs (ambiguous only)\n    amb_df = dfc[dfc[\"condition\"] == \"ambiguous\"]\n    types = sorted(amb_df[\"ambiguity_type\"].unique())\n    type_pairs = {}\n    for i in range(len(types)):\n        for j in range(i + 1, len(types)):\n            t1, t2 = types[i], types[j]\n            v1 = amb_df.loc[amb_df[\"ambiguity_type\"] == t1, \"violated\"].values\n            v2 = amb_df.loc[amb_df[\"ambiguity_type\"] == t2, \"violated\"].values\n            type_pairs[f\"{t1}_vs_{t2}\"] = _bca_ci(v1, v2, rng, B)\n    results[\"type_pairs_ambiguous\"] = type_pairs\n\n    # Model pairs\n    models = sorted(dfc[\"model\"].unique())\n    model_pairs = {}\n    for i in range(len(models)):\n        for j in range(i + 1, len(models)):\n            m1, m2 = models[i], models[j]\n            v1 = dfc.loc[dfc[\"model\"] == m1, \"violated\"].values\n            v2 = dfc.loc[dfc[\"model\"] == m2, \"violated\"].values\n            model_pairs[f\"{m1}_vs_{m2}\"] = _bca_ci(v1, v2, rng, B)\n    results[\"model_pairs\"] = model_pairs\n\n    out = ANALYSIS_DIR / \"bootstrap_ci.json\"\n    with open(out, \"w\") as f:\n        json.dump(results, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return results\n\n\ndef run_mcnemar_matched(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Matched-pair McNemar test for C1 (binary effect).\"\"\"\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n\n    amb = dfc.loc[dfc[\"condition\"] == \"ambiguous\", [\"clause_id\", \"model\", \"violated\"]]\n    una = dfc.loc[dfc[\"condition\"] == \"unambiguous\", [\"clause_id\", \"model\", \"violated\"]]\n    merged = pd.merge(amb, una, on=[\"clause_id\", \"model\"], suffixes=(\"_amb\", \"_una\"))\n\n    if merged.empty:\n        return {\"error\": \"No matched pairs found\"}\n\n    merged[\"amb_only\"] = merged[\"violated_amb\"] & ~merged[\"violated_una\"]\n    merged[\"una_only\"] = ~merged[\"violated_amb\"] & merged[\"violated_una\"]\n    merged[\"both\"] = merged[\"violated_amb\"] & merged[\"violated_una\"]\n    merged[\"neither\"] = ~merged[\"violated_amb\"] & ~merged[\"violated_una\"]\n\n    b_total = int(merged[\"amb_only\"].sum())\n    c_total = int(merged[\"una_only\"].sum())\n    n_pairs = len(merged)\n    n_disc = b_total + c_total\n\n    # Overall McNemar\n    if n_disc > 0:\n        if n_disc >= 25:\n            mcn_chi2 = float((abs(b_total - c_total) - 1) ** 2 / n_disc)\n            mcn_p = float(1 - stats.chi2.cdf(mcn_chi2, 1))\n            method = \"chi-square (continuity corrected)\"\n        else:\n            mcn_p = float(stats.binomtest(b_total, n_disc, 0.5).pvalue)\n            mcn_chi2 = None\n            method = \"exact binomial\"\n    else:\n        mcn_chi2 = 0.0\n        mcn_p = 1.0\n        method = \"no discordant pairs\"\n\n    # Odds ratio b/c with Wald 95% CI\n    if b_total > 0 and c_total > 0:\n        or_val = b_total / c_total\n        log_or = np.log(or_val)\n        se_log = np.sqrt(1 / b_total + 1 / c_total)\n        or_lo = float(np.exp(log_or - 1.96 * se_log))\n        or_hi = float(np.exp(log_or + 1.96 * se_log))\n    elif c_total == 0 and b_total > 0:\n        or_val, or_lo, or_hi = float(\"inf\"), float(\"nan\"), float(\"nan\")\n    elif b_total == 0 and c_total > 0:\n        or_val, or_lo, or_hi = 0.0, float(\"nan\"), float(\"nan\")\n    else:\n        or_val = or_lo = or_hi = float(\"nan\")\n\n    # Per-model McNemar\n    per_model = {}\n    for model_name, mdf in merged.groupby(\"model\"):\n        b_m = int(mdf[\"amb_only\"].sum())\n        c_m = int(mdf[\"una_only\"].sum())\n        disc_m = b_m + c_m\n        if disc_m > 0:\n            p_m = float(stats.binomtest(b_m, disc_m, 0.5).pvalue)\n        else:\n            p_m = 1.0\n        per_model[model_name] = {\n            \"n_pairs\": len(mdf),\n            \"b_amb_only\": b_m,\n            \"c_una_only\": c_m,\n            \"mcnemar_p\": round(p_m, 6),\n        }\n\n    # Mantel-Haenszel OR stratified by ambiguity_type\n    mh_strata = []\n    for atype, sdf in merged.groupby(\n        merged[\"clause_id\"].map(\n            lambda cid: dfc.loc[dfc[\"clause_id\"] == cid, \"ambiguity_type\"].iloc[0]\n            if cid in dfc[\"clause_id\"].values else \"unknown\"\n        )\n    ):\n        b_s = int(sdf[\"amb_only\"].sum())\n        c_s = int(sdf[\"una_only\"].sum())\n        a_s = int(sdf[\"both\"].sum())\n        d_s = int(sdf[\"neither\"].sum())\n        n_s = len(sdf)\n        mh_strata.append({\n            \"stratum\": atype, \"n\": n_s,\n            \"a\": a_s, \"b\": b_s, \"c\": c_s, \"d\": d_s,\n        })\n\n    # Haldane 0.5 correction for strata with zero cells\n    mh_num = 0.0\n    mh_den = 0.0\n    for s in mh_strata:\n        if s[\"n\"] == 0:\n            continue\n        a, b, c, d, n = s[\"a\"], s[\"b\"], s[\"c\"], s[\"d\"], s[\"n\"]\n        if a == 0 or b == 0 or c == 0 or d == 0:\n            a, b, c, d, n = a + 0.5, b + 0.5, c + 0.5, d + 0.5, n + 2\n        mh_num += b * d / n\n        mh_den += c * a / n\n    mh_or = mh_num / mh_den if mh_den > 0 else float(\"inf\") if mh_num > 0 else float(\"nan\")\n\n    def _safe_round(v, n=4):\n        if isinstance(v, float) and (np.isnan(v) or np.isinf(v)):\n            return str(v)\n        return round(float(v), n)\n\n    result = {\n        \"n_pairs\": n_pairs,\n        \"n_concordant\": int(merged[\"both\"].sum() + merged[\"neither\"].sum()),\n        \"n_discordant\": n_disc,\n        \"b_amb_only\": b_total,\n        \"c_una_only\": c_total,\n        \"mcnemar\": {\n            \"method\": method,\n            \"statistic\": _safe_round(mcn_chi2) if mcn_chi2 is not None else None,\n            \"p\": round(mcn_p, 6),\n        },\n        \"odds_ratio\": {\n            \"or\": _safe_round(or_val),\n            \"ci_95_lower\": _safe_round(or_lo),\n            \"ci_95_upper\": _safe_round(or_hi),\n        },\n        \"mantel_haenszel\": {\n            \"or\": _safe_round(mh_or),\n            \"correction\": \"haldane_0.5\",\n            \"note\": \"Primary OR=44.8 (non-stratified); MH OR is supplementary\",\n            \"strata\": mh_strata,\n        },\n        \"per_model\": per_model,\n    }\n\n    out = ANALYSIS_DIR / \"mcnemar_matched.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_information_delta(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Dream A10: Per-type information (token count) delta + logistic regression.\"\"\"\n    import statsmodels.api as sm\n\n    clause_map = {}\n    for c in clauses:\n        cid = c[\"clause_id\"]\n        amb_tok = len(c.get(\"ambiguous_clause\", \"\").split())\n        una_tok = len(c.get(\"unambiguous_clause\", \"\").split())\n        clause_map[cid] = {\n            \"ambiguity_type\": c.get(\"ambiguity_type\", \"unknown\"),\n            \"amb_tokens\": amb_tok,\n            \"una_tokens\": una_tok,\n            \"token_delta\": una_tok - amb_tok,\n        }\n\n    # Per-type token delta stats\n    type_groups: dict[str, list[int]] = {}\n    for info in clause_map.values():\n        atype = info[\"ambiguity_type\"]\n        type_groups.setdefault(atype, []).append(info[\"token_delta\"])\n\n    type_deltas = {}\n    for atype, deltas in sorted(type_groups.items()):\n        arr = np.array(deltas)\n        type_deltas[atype] = {\n            \"mean\": round(float(arr.mean()), 2),\n            \"median\": round(float(np.median(arr)), 2),\n            \"std\": round(float(arr.std(ddof=1)), 2) if len(arr) > 1 else 0.0,\n            \"min\": int(arr.min()),\n            \"max\": int(arr.max()),\n            \"n_clauses\": len(arr),\n        }\n\n    # Merge into judgments\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc).astype(int)\n    dfc[\"token_delta\"] = dfc[\"clause_id\"].map(\n        lambda cid: clause_map.get(cid, {}).get(\"token_delta\", 0)\n    )\n    dfc[\"condition_amb\"] = (dfc[\"condition\"] == \"ambiguous\").astype(int)\n\n    # Logistic regression: violation ~ condition + type + token_delta + model\n    type_dummies = pd.get_dummies(\n        dfc[\"ambiguity_type\"], prefix=\"type\", drop_first=True, dtype=float\n    )\n    model_dummies = pd.get_dummies(\n        dfc[\"model\"], prefix=\"model\", drop_first=True, dtype=float\n    )\n    X = pd.concat(\n        [dfc[[\"condition_amb\", \"token_delta\"]].astype(float), type_dummies, model_dummies],\n        axis=1,\n    )\n    X = sm.add_constant(X)\n    y = dfc[\"violated\"]\n\n    logit_result: dict = {}\n    try:\n        fit = sm.Logit(y, X).fit(disp=0, maxiter=100)\n        coefficients = {}\n        ci = fit.conf_int()\n        for var in fit.params.index:\n            coefficients[var] = {\n                \"coef\": round(float(fit.params[var]), 4),\n                \"se\": round(float(fit.bse[var]), 4),\n                \"z\": round(float(fit.tvalues[var]), 4),\n                \"p\": round(float(fit.pvalues[var]), 6),\n                \"ci_lower\": round(float(ci.loc[var, 0]), 4),\n                \"ci_upper\": round(float(ci.loc[var, 1]), 4),\n            }\n        logit_result = {\n            \"converged\": bool(fit.mle_retvals.get(\"converged\", False)),\n            \"n_obs\": int(fit.nobs),\n            \"pseudo_r2\": round(float(fit.prsquared), 4),\n            \"llr_p\": round(float(fit.llr_pvalue), 6),\n            \"coefficients\": coefficients,\n        }\n    except Exception as e:\n        logit_result = {\"error\": str(e)}\n\n    result = {\n        \"per_type_token_delta\": type_deltas,\n        \"logistic_regression\": logit_result,\n    }\n\n    out = ANALYSIS_DIR / \"information_delta.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_fleiss_kappa(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Fleiss' kappa for inter-model agreement on violation judgment.\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        result = {\"error\": \"No ambiguous episodes\"}\n        out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n        with open(out, \"w\") as f:\n            json.dump(result, f, indent=2)\n        print(f\"  -> {out.name}\")\n        return result\n\n    amb[\"violated\"] = analyze.binarize_violations(amb).astype(int)\n    models = sorted(amb[\"model\"].unique())\n    n_models = len(models)\n\n    if n_models < 2:\n        result = {\"error\": f\"Need >= 2 models, found {n_models}\", \"models\": models}\n        out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n        with open(out, \"w\") as f:\n            json.dump(result, f, indent=2)\n        print(f\"  -> {out.name}\")\n        return result\n\n    ratings = amb.groupby(\"clause_id\").agg(\n        n_violated=(\"violated\", \"sum\"),\n        n_raters=(\"violated\", \"count\"),\n    ).reset_index()\n    ratings = ratings[ratings[\"n_raters\"] >= 2]\n\n    if ratings.empty:\n        result = {\"error\": \"No clauses with >= 2 model ratings\"}\n        out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n        with open(out, \"w\") as f:\n            json.dump(result, f, indent=2)\n        print(f\"  -> {out.name}\")\n        return result\n\n    ratings[\"n_not\"] = ratings[\"n_raters\"] - ratings[\"n_violated\"]\n    N = len(ratings)\n    mat = ratings[[\"n_violated\", \"n_not\"]].values  # (N, 2)\n    n_arr = ratings[\"n_raters\"].values\n\n    # Per-subject agreement P_i\n    P_i = np.zeros(N)\n    for i in range(N):\n        ni = n_arr[i]\n        if ni >= 2:\n            P_i[i] = (np.sum(mat[i] ** 2) - ni) / (ni * (ni - 1))\n    P_bar = float(P_i.mean())\n\n    total_ratings = n_arr.sum()\n    p_j = mat.sum(axis=0) / total_ratings  # (2,)\n    P_e = float(np.sum(p_j ** 2))\n\n    kappa = (P_bar - P_e) / (1 - P_e) if P_e < 1.0 else 0.0\n\n    # SE (large sample, Fleiss 1971)\n    n_fixed = int(np.median(n_arr))\n    if N > 1 and P_e < 1.0 and n_fixed >= 2:\n        inner = (\n            P_e\n            - (2 * n_fixed - 3) * P_e ** 2\n            + 2 * (n_fixed - 2) * np.sum(p_j ** 3)\n        )\n        se = float(np.sqrt(2 / (N * n_fixed * (n_fixed - 1))) * np.sqrt(\n            abs(inner) / (1 - P_e) ** 2\n        ))\n        z_val = kappa / se if se > 0 else float(\"nan\")\n        p_val = float(2 * (1 - stats.norm.cdf(abs(z_val)))) if np.isfinite(z_val) else float(\"nan\")\n    else:\n        se = z_val = p_val = float(\"nan\")\n\n    if kappa < 0:\n        interp = \"less than chance agreement\"\n    elif kappa < 0.20:\n        interp = \"slight agreement\"\n    elif kappa < 0.40:\n        interp = \"fair agreement\"\n    elif kappa < 0.60:\n        interp = \"moderate agreement\"\n    elif kappa < 0.80:\n        interp = \"substantial agreement\"\n    else:\n        interp = \"almost perfect agreement\"\n\n    result = {\n        \"n_clauses\": N,\n        \"n_models\": n_models,\n        \"models\": models,\n        \"n_raters_per_clause\": {\n            \"min\": int(n_arr.min()),\n            \"max\": int(n_arr.max()),\n            \"mean\": round(float(n_arr.mean()), 1),\n        },\n        \"category_proportions\": {\n            \"violated\": round(float(p_j[0]), 4),\n            \"not_violated\": round(float(p_j[1]), 4),\n        },\n        \"fleiss_kappa\": round(float(kappa), 4),\n        \"se\": round(float(se), 4) if np.isfinite(se) else None,\n        \"z\": round(float(z_val), 4) if np.isfinite(z_val) else None,\n        \"p\": round(float(p_val), 6) if np.isfinite(p_val) else None,\n        \"interpretation\": interp,\n    }\n\n    out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):\n    \"\"\"Load all judgments and run the full analysis suite.\"\"\"\n    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)\n\n    df = _load_all_judgments(models)\n    if df.empty:\n        print(\"No judgments found. Run Phase 2 first.\")\n        return\n\n    print(f\"Loaded {len(df)} judgments ({df['model'].nunique()} models, \"\n          f\"{df['ambiguity_type'].nunique()} types)\")\n\n    binary = _binary_effect(df)\n    type_eff = _type_effect(df)\n    model_eff = _model_effect(df)\n    interact = _interaction(df)\n\n    # JSON report\n    report = {\n        \"binary_effect\": binary,\n        \"type_effect\": type_eff,\n        \"model_effect\": model_eff,\n        \"model_type_interaction\": interact,\n        \"n_judgments\": len(df),\n    }\n    with open(ANALYSIS_DIR / \"full_statistics.json\", \"w\") as f:\n        json.dump(report, f, indent=2, default=str)\n\n    # Per-clause summary CSV\n    summary = analyze.per_clause_summary(df)\n    summary.to_csv(ANALYSIS_DIR / \"per_clause_summary.csv\", index=False)\n\n    # Aggregated rates CSV\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n    agg = dfc.groupby(\n        [\"model\", \"ambiguity_type\", \"condition\"]\n    )[\"violated\"].agg(\n        violation_rate=\"mean\", n_violations=\"sum\", n_total=\"count\",\n    ).reset_index()\n    agg.to_csv(ANALYSIS_DIR / \"aggregated_rates.csv\", index=False)\n\n    _print_full_report(binary, type_eff, model_eff, interact)\n\n    # Extended analyses (Dream reviewer)\n    clauses_path = config.ARTIFACTS_DIR / \"clause_templates_full.json\"\n    if clauses_path.exists():\n        with open(clauses_path) as f:\n            raw = json.load(f)\n        clauses_data = raw if isinstance(raw, list) else raw.get(\"clauses\", raw)\n    else:\n        clauses_data = []\n\n    print(\"\\n-- Extended analyses (Dream reviewer) --\\n\")\n    run_power_analysis(df, clauses_data)\n    run_tost_equivalence(df, clauses_data)\n    run_bootstrap_ci(df, clauses_data)\n    run_mcnemar_matched(df, clauses_data)\n    if clauses_data:\n        run_information_delta(df, clauses_data)\n    else:\n        print(\"  (skipped information_delta -- no clauses file)\")\n    run_fleiss_kappa(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")\n    print(\"  - full_statistics.json\")\n    print(\"  - per_clause_summary.csv\")\n    print(\"  - aggregated_rates.csv\")\n    print(\"  - power_analysis.json\")\n    print(\"  - tost_equivalence.json\")\n    print(\"  - bootstrap_ci.json\")\n    print(\"  - mcnemar_matched.json\")\n    if clauses_data:\n        print(\"  - information_delta.json\")\n    print(\"  - fleiss_kappa.json\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args(argv: list[str] | None = None) -> argparse.Namespace:\n    parser = argparse.ArgumentParser(\n        description=\"Full study execution for policy ambiguity safety experiment.\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n        epilog=\"\"\"\\\nExamples:\n  python run_full_study.py --phase 1 --clauses clause_templates_full.json\n  python run_full_study.py --phase 2 --resume\n  python run_full_study.py --phase 3\n  python run_full_study.py --all --clauses clause_templates_full.json\n\"\"\",\n    )\n    group = parser.add_mutually_exclusive_group(required=True)\n    group.add_argument(\n        \"--phase\", type=int, choices=[1, 2, 3],\n        help=\"Run a specific phase (1=episodes, 2=judge, 3=analysis).\",\n    )\n    group.add_argument(\n        \"--all\", action=\"store_true\",\n        help=\"Run all 3 phases sequentially.\",\n    )\n    parser.add_argument(\n        \"--clauses\",\n        default=str(config.ARTIFACTS_DIR / \"clause_templates_full.json\"),\n        help=\"Path to clauses JSON (default: clause_templates_full.json).\",\n    )\n    parser.add_argument(\n        \"--models\", default=\",\".join(DEFAULT_MODELS),\n        help=f\"Comma-separated model names (default: {','.join(DEFAULT_MODELS)}).\",\n    )\n    parser.add_argument(\n        \"--concurrency\", type=int, default=config.DEFAULT_CONCURRENCY,\n        help=f\"Max concurrent API calls (default: {config.DEFAULT_CONCURRENCY}).\",\n    )\n    parser.add_argument(\n        \"--resume\", action=\"store_true\", default=True,\n        help=\"Skip completed episodes/judgments (default: True).\",\n    )\n    parser.add_argument(\n        \"--no-resume\", action=\"store_false\", dest=\"resume\",\n        help=\"Re-run everything from scratch.\",\n    )\n    return parser.parse_args(argv)\n\n\ndef main(argv: list[str] | None = None):\n    args = parse_args(argv)\n    models = [m.strip() for m in args.models.split(\",\")]\n    for m in models:\n        if m not in config.MODELS:\n            print(f\"Error: unknown model '{m}'. Available: {list(config.MODELS.keys())}\")\n            sys.exit(1)\n\n    clauses = harness.load_clauses(args.clauses)\n    phases = [1, 2, 3] if args.all else [args.phase]\n\n    for phase in phases:\n        print(f\"\\n{'=' * 40} Phase {phase} {'=' * 40}\\n\")\n        if phase == 1:\n            asyncio.run(run_phase1(clauses, models, args.concurrency, args.resume))\n        elif phase == 2:\n            asyncio.run(run_phase2(clauses, models, args.concurrency, args.resume))\n        elif phase == 3:\n            run_phase3(models)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 1110,
        "oldLines": 6,
        "newStart": 1110,
        "newLines": 116,
        "lines": [
          "     return result",
          " ",
          " ",
          "+def run_layer_effect_test(df: pd.DataFrame, clauses: list[dict]) -> dict:",
          "+    \"\"\"C3: Formal test of specification-layer vs linguistic-layer violation rates.\"\"\"",
          "+    SPEC_TYPES = {\"incompleteness\", \"conditional_precedence\", \"authorization_scope\"}",
          "+    LING_TYPES = {\"scopal\", \"lexical\", \"coreferential\"}",
          "+",
          "+    dfc = df.copy()",
          "+    dfc[\"violated\"] = analyze.binarize_violations(dfc)",
          "+",
          "+    # Filter to ambiguous condition only",
          "+    amb = dfc[dfc[\"condition\"] == \"ambiguous\"].copy()",
          "+    amb[\"layer\"] = amb[\"ambiguity_type\"].map(",
          "+        lambda t: \"specification\" if t in SPEC_TYPES else \"linguistic\" if t in LING_TYPES else \"unknown\"",
          "+    )",
          "+    amb = amb[amb[\"layer\"] != \"unknown\"]",
          "+",
          "+    spec = amb[amb[\"layer\"] == \"specification\"]",
          "+    ling = amb[amb[\"layer\"] == \"linguistic\"]",
          "+",
          "+    spec_n = len(spec)",
          "+    spec_v = int(spec[\"violated\"].sum())",
          "+    ling_n = len(ling)",
          "+    ling_v = int(ling[\"violated\"].sum())",
          "+",
          "+    spec_rate = spec_v / spec_n if spec_n > 0 else 0",
          "+    ling_rate = ling_v / ling_n if ling_n > 0 else 0",
          "+    delta_pp = (spec_rate - ling_rate) * 100",
          "+",
          "+    from scipy.stats import chi2_contingency",
          "+    table = np.array([",
          "+        [spec_v, spec_n - spec_v],",
          "+        [ling_v, ling_n - ling_v],",
          "+    ])",
          "+    chi2, p_val, dof, expected = chi2_contingency(table, correction=False)",
          "+",
          "+    n_total = spec_n + ling_n",
          "+    cramers_v = np.sqrt(chi2 / n_total) if n_total > 0 else 0",
          "+",
          "+    a, b = spec_v, spec_n - spec_v",
          "+    c, d = ling_v, ling_n - ling_v",
          "+    if b > 0 and c > 0 and d > 0 and a > 0:",
          "+        or_val = (a * d) / (b * c)",
          "+        log_or = np.log(or_val)",
          "+        se_log = np.sqrt(1/a + 1/b + 1/c + 1/d)",
          "+        or_lo = float(np.exp(log_or - 1.96 * se_log))",
          "+        or_hi = float(np.exp(log_or + 1.96 * se_log))",
          "+    else:",
          "+        or_val = or_lo = or_hi = float(\"nan\")",
          "+",
          "+    np.random.seed(42)",
          "+    n_boot = 10000",
          "+    spec_arr = spec[\"violated\"].values.astype(float)",
          "+    ling_arr = ling[\"violated\"].values.astype(float)",
          "+    boot_deltas = []",
          "+    for _ in range(n_boot):",
          "+        s_idx = np.random.randint(0, len(spec_arr), len(spec_arr))",
          "+        l_idx = np.random.randint(0, len(ling_arr), len(ling_arr))",
          "+        boot_deltas.append((spec_arr[s_idx].mean() - ling_arr[l_idx].mean()) * 100)",
          "+    boot_deltas = np.array(boot_deltas)",
          "+    ci_lo = float(np.percentile(boot_deltas, 2.5))",
          "+    ci_hi = float(np.percentile(boot_deltas, 97.5))",
          "+",
          "+    per_type = {}",
          "+    for atype in list(SPEC_TYPES) + list(LING_TYPES):",
          "+        subset = amb[amb[\"ambiguity_type\"] == atype]",
          "+        if len(subset) > 0:",
          "+            rate = float(subset[\"violated\"].mean())",
          "+            per_type[atype] = {",
          "+                \"n\": len(subset),",
          "+                \"violations\": int(subset[\"violated\"].sum()),",
          "+                \"rate\": round(rate * 100, 2),",
          "+                \"layer\": \"specification\" if atype in SPEC_TYPES else \"linguistic\",",
          "+            }",
          "+",
          "+    result = {",
          "+        \"test\": \"layer_effect (C3)\",",
          "+        \"specification_layer\": {",
          "+            \"types\": sorted(SPEC_TYPES),",
          "+            \"n\": spec_n,",
          "+            \"violations\": spec_v,",
          "+            \"rate_pct\": round(spec_rate * 100, 2),",
          "+        },",
          "+        \"linguistic_layer\": {",
          "+            \"types\": sorted(LING_TYPES),",
          "+            \"n\": ling_n,",
          "+            \"violations\": ling_v,",
          "+            \"rate_pct\": round(ling_rate * 100, 2),",
          "+        },",
          "+        \"delta_pp\": round(delta_pp, 2),",
          "+        \"bootstrap_ci_95\": [round(ci_lo, 2), round(ci_hi, 2)],",
          "+        \"chi_squared\": {",
          "+            \"statistic\": round(float(chi2), 4),",
          "+            \"df\": int(dof),",
          "+            \"p\": round(float(p_val), 6),",
          "+        },",
          "+        \"cramers_v\": round(float(cramers_v), 4),",
          "+        \"odds_ratio\": {",
          "+            \"or\": round(float(or_val), 4) if np.isfinite(or_val) else str(or_val),",
          "+            \"ci_95\": [round(or_lo, 4) if np.isfinite(or_lo) else str(or_lo),",
          "+                       round(or_hi, 4) if np.isfinite(or_hi) else str(or_hi)],",
          "+        },",
          "+        \"per_type_detail\": per_type,",
          "+    }",
          "+",
          "+    out = ANALYSIS_DIR / \"layer_effect_test.json\"",
          "+    with open(out, \"w\") as f:",
          "+        json.dump(result, f, indent=2, default=str)",
          "+    print(f\"  -> {out.name}\")",
          "+    return result",
          "+",
          "+",
          " def run_phase3(models: list[str]):",
          "     \"\"\"Load all judgments and run the full analysis suite.\"\"\"",
          "     ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01TVQ4B8Ux4G4AwpyRwQLCEq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
  "old_string": "    run_fleiss_kappa(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")",
  "new_string": "    run_fleiss_kappa(df, clauses_data)\n    run_layer_effect_test(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "2b5ba5a7-50f7-4588-991b-a3824d55c170",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARSuJkDmcQoSwC8PWAd549",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1945,
      "cache_read_input_tokens": 27015,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1945
      },
      "output_tokens": 67,
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

_source line 12 · 2026-05-20T16:28:33.336Z_

<details><summary>↩ Tool result · `toolu_01TVQ4B8Ux4G4AwpyRwQLCEq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "d0cc6266-8886-4216-b117-f61155ae3052",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
    "oldString": "    run_fleiss_kappa(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")",
    "newString": "    run_fleiss_kappa(df, clauses_data)\n    run_layer_effect_test(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Full study execution script for policy ambiguity safety experiments.\n\nOrchestrates the complete experiment pipeline:\n  Phase 1: Episode generation (300 clauses x 2 conditions x 2 models = 1,200 episodes)\n  Phase 2: Cross-judge evaluation (gpt-5.4 episodes judged by gpt-4.1, vice versa)\n  Phase 3: Statistical analysis (binary/type/model effects + interactions)\n\nInput:  artifacts/clause_templates_full.json (300 clauses, 6 types x 50)\nOutput: artifacts/full_study/{episodes,judgments,analysis}/\n\nDependencies: harness.py, judge.py, analyze.py, config.py\n\"\"\"\n\nimport argparse\nimport asyncio\nimport json\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport config\nimport harness\nimport judge\nimport analyze\n\n# ---------------------------------------------------------------------------\n# Paths\n# ---------------------------------------------------------------------------\n\nFULL_STUDY_DIR = config.ARTIFACTS_DIR / \"full_study\"\nEPISODES_DIR = FULL_STUDY_DIR / \"episodes\"\nJUDGMENTS_DIR = FULL_STUDY_DIR / \"judgments\"\nANALYSIS_DIR = FULL_STUDY_DIR / \"analysis\"\nERRORS_FILE = FULL_STUDY_DIR / \"errors.jsonl\"\n\nDEFAULT_MODELS = [\"gpt-5.4\", \"gpt-4.1\", \"claude-sonnet-4-6\"]\n\n\n# ---------------------------------------------------------------------------\n# Phase 1: Episode Generation\n# ---------------------------------------------------------------------------\n\ndef _load_completed_episodes(model_dir: Path) -> set[str]:\n    \"\"\"Return set of 'clause_id|condition' keys already completed.\"\"\"\n    completed = set()\n    episodes_file = model_dir / \"episodes.jsonl\"\n    if episodes_file.exists():\n        with open(episodes_file) as f:\n            for line in f:\n                if line.strip():\n                    rec = json.loads(line)\n                    completed.add(f\"{rec['clause_id']}|{rec['condition']}\")\n    return completed\n\n\nasync def run_phase1(\n    clauses: list[dict],\n    models: list[str],\n    concurrency: int,\n    resume: bool,\n):\n    \"\"\"Generate episodes for all model x clause x condition combinations.\"\"\"\n    FULL_STUDY_DIR.mkdir(parents=True, exist_ok=True)\n\n    print(\"Preflight API check...\")\n    for m in models:\n        try:\n            await harness.preflight_check(m)\n            print(f\"  {m}: OK\")\n        except Exception as e:\n            print(f\"  {m}: FAILED — {e}\")\n            raise SystemExit(f\"Preflight failed for {m}. Fix API key/endpoint before running.\")\n\n    total_done = 0\n    total_errors = 0\n    total_skipped = 0\n\n    for model_name in models:\n        model_dir = EPISODES_DIR / model_name\n        model_dir.mkdir(parents=True, exist_ok=True)\n\n        completed = _load_completed_episodes(model_dir) if resume else set()\n        tasks = []\n        for clause in clauses:\n            for condition in (\"ambiguous\", \"unambiguous\"):\n                key = f\"{clause['clause_id']}|{condition}\"\n                if key in completed:\n                    total_skipped += 1\n                    continue\n                tasks.append((clause, condition))\n\n        if not tasks:\n            print(f\"[{model_name}] All {len(completed)} episodes complete.\")\n            continue\n\n        print(f\"[{model_name}] {len(tasks)} episodes to run \"\n              f\"(skipping {len(completed)}, concurrency={concurrency})\")\n\n        semaphore = asyncio.Semaphore(concurrency)\n        output_file = model_dir / \"episodes.jsonl\"\n        lock = asyncio.Lock()\n        done = 0\n        errors = 0\n\n        async def _run_one(clause, condition, _model=model_name):\n            nonlocal done, errors\n            async with semaphore:\n                try:\n                    result = await harness.run_episode(clause, condition, _model)\n                    validity = harness.validate_episode(result)\n                    if validity != \"ok\":\n                        raise RuntimeError(\n                            f\"Episode {validity}: {result.get('error', 'no assistant response')}\"\n                        )\n                    async with lock:\n                        with open(output_file, \"a\") as f:\n                            f.write(json.dumps(result, ensure_ascii=False) + \"\\n\")\n                        done += 1\n                        if done % 50 == 0:\n                            print(f\"  [{_model}] {done}/{len(tasks)}\")\n                except Exception as e:\n                    async with lock:\n                        errors += 1\n                        with open(ERRORS_FILE, \"a\") as f:\n                            f.write(json.dumps({\n                                \"phase\": 1, \"model\": _model,\n                                \"clause_id\": clause[\"clause_id\"],\n                                \"condition\": condition,\n                                \"error\": str(e),\n                                \"timestamp\": time.time(),\n                            }, ensure_ascii=False) + \"\\n\")\n\n        await asyncio.gather(*[_run_one(c, cond) for c, cond in tasks])\n        print(f\"  [{model_name}] {done} done, {errors} errors\")\n        total_done += done\n        total_errors += errors\n\n    print(f\"\\nPhase 1 summary: {total_done} done / {total_errors} errors / \"\n          f\"{total_skipped} skipped\")\n\n\n# ---------------------------------------------------------------------------\n# Phase 2: Cross-Judge Evaluation\n# ---------------------------------------------------------------------------\n\ndef _load_judged_ids(model_dir: Path) -> set[str]:\n    \"\"\"Return set of episode_ids already judged.\"\"\"\n    judged = set()\n    judgments_file = model_dir / \"judgments.jsonl\"\n    if judgments_file.exists():\n        with open(judgments_file) as f:\n            for line in f:\n                if line.strip():\n                    judged.add(json.loads(line)[\"episode_id\"])\n    return judged\n\n\nasync def run_phase2(\n    clauses: list[dict],\n    models: list[str],\n    concurrency: int,\n    resume: bool,\n):\n    \"\"\"Cross-judge all episodes (each model's episodes judged by the other).\"\"\"\n    clause_index = judge.build_clause_index(clauses)\n    total_done = 0\n    total_errors = 0\n    total_skipped = 0\n\n    for model_name in models:\n        ep_dir = EPISODES_DIR / model_name\n        if not ep_dir.exists():\n            print(f\"[{model_name}] No episodes found — run Phase 1 first.\")\n            continue\n\n        episodes = judge.load_episodes(ep_dir)\n        if not episodes:\n            print(f\"[{model_name}] No episode files found.\")\n            continue\n\n        judge_model = config.CROSS_JUDGE_MAP[model_name]\n        jdg_dir = JUDGMENTS_DIR / model_name\n        jdg_dir.mkdir(parents=True, exist_ok=True)\n\n        judged_ids = _load_judged_ids(jdg_dir) if resume else set()\n        pending = [ep for ep in episodes if ep[\"episode_id\"] not in judged_ids]\n        total_skipped += len(episodes) - len(pending)\n\n        if not pending:\n            print(f\"[{model_name}] All {len(episodes)} episodes already judged.\")\n            continue\n\n        print(f\"[{model_name}] Judging {len(pending)} episodes \"\n              f\"(judge={judge_model}, concurrency={concurrency})\")\n\n        semaphore = asyncio.Semaphore(concurrency)\n        output_file = jdg_dir / \"judgments.jsonl\"\n        lock = asyncio.Lock()\n        done = 0\n        errors = 0\n\n        async def _judge_one(episode, _model=model_name):\n            nonlocal done, errors\n            async with semaphore:\n                try:\n                    result = await judge.judge_episode(episode, clause_index)\n                    async with lock:\n                        with open(output_file, \"a\") as f:\n                            f.write(json.dumps(result, ensure_ascii=False) + \"\\n\")\n                        done += 1\n                        if done % 50 == 0:\n                            print(f\"  [{_model}] {done}/{len(pending)} judged\")\n                except Exception as e:\n                    async with lock:\n                        errors += 1\n                        with open(ERRORS_FILE, \"a\") as f:\n                            f.write(json.dumps({\n                                \"phase\": 2, \"model\": _model,\n                                \"episode_id\": episode.get(\"episode_id\", \"?\"),\n                                \"error\": str(e),\n                                \"timestamp\": time.time(),\n                            }, ensure_ascii=False) + \"\\n\")\n\n        await asyncio.gather(*[_judge_one(ep) for ep in pending])\n        print(f\"  [{model_name}] {done} judged, {errors} errors\")\n        total_done += done\n        total_errors += errors\n\n    print(f\"\\nPhase 2 summary: {total_done} done / {total_errors} errors / \"\n          f\"{total_skipped} skipped\")\n\n\n# ---------------------------------------------------------------------------\n# Phase 3: Analysis\n# ---------------------------------------------------------------------------\n\ndef _load_all_judgments(models: list[str]) -> pd.DataFrame:\n    \"\"\"Load judgments from all model subdirectories into one DataFrame.\"\"\"\n    records = []\n    for model_name in models:\n        jdg_dir = JUDGMENTS_DIR / model_name\n        if not jdg_dir.exists():\n            continue\n        for jsonl_file in jdg_dir.glob(\"*.jsonl\"):\n            with open(jsonl_file) as f:\n                for line in f:\n                    if not line.strip():\n                        continue\n                    rec = json.loads(line)\n                    records.append({\n                        \"episode_id\": rec[\"episode_id\"],\n                        \"clause_id\": rec[\"clause_id\"],\n                        \"ambiguity_type\": rec[\"ambiguity_type\"],\n                        \"condition\": rec[\"condition\"],\n                        \"model\": rec[\"model\"],\n                        \"violation_level\": rec[\"judgment\"][\"violation_level\"],\n                        \"confidence\": rec[\"judgment\"][\"confidence\"],\n                        \"judge_model\": rec[\"judge_model\"],\n                    })\n    df = pd.DataFrame(records)\n    if df.empty:\n        return df\n    level_order = pd.CategoricalDtype(\n        categories=config.VIOLATION_LEVELS, ordered=True\n    )\n    df[\"violation_level\"] = df[\"violation_level\"].astype(level_order)\n    return df\n\n\ndef _binary_effect(df: pd.DataFrame) -> dict:\n    \"\"\"(a) Ambiguous vs unambiguous violation rates: global, per-type, per-model.\"\"\"\n    df = df.copy()\n    df[\"violated\"] = analyze.binarize_violations(df)\n\n    # Global\n    cond_rates = df.groupby(\"condition\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    amb_r = float(cond_rates.loc[\"ambiguous\", \"mean\"]) if \"ambiguous\" in cond_rates.index else float(\"nan\")\n    una_r = float(cond_rates.loc[\"unambiguous\", \"mean\"]) if \"unambiguous\" in cond_rates.index else float(\"nan\")\n    ct = pd.crosstab(df[\"condition\"], df[\"violated\"])\n    if ct.shape == (2, 2):\n        chi2, p, _, _ = stats.chi2_contingency(ct.values)\n    else:\n        chi2, p = float(\"nan\"), float(\"nan\")\n    glob = {\n        \"ambiguous_rate\": amb_r, \"unambiguous_rate\": una_r,\n        \"difference\": amb_r - una_r if not (np.isnan(amb_r) or np.isnan(una_r)) else None,\n        \"chi2\": float(chi2), \"p\": float(p),\n    }\n\n    # Per-type\n    per_type = {}\n    for atype, tdf in df.groupby(\"ambiguity_type\"):\n        tr = tdf.groupby(\"condition\")[\"violated\"].mean()\n        a, u = tr.get(\"ambiguous\", np.nan), tr.get(\"unambiguous\", np.nan)\n        ct_t = pd.crosstab(tdf[\"condition\"], tdf[\"violated\"])\n        fp = float(stats.fisher_exact(ct_t.values)[1]) if ct_t.shape == (2, 2) else float(\"nan\")\n        per_type[atype] = {\n            \"ambiguous_rate\": float(a), \"unambiguous_rate\": float(u),\n            \"difference\": float(a - u) if not (np.isnan(a) or np.isnan(u)) else None,\n            \"fisher_p\": fp,\n        }\n\n    # Per-model\n    per_model = {}\n    for mname, mdf in df.groupby(\"model\"):\n        mr = mdf.groupby(\"condition\")[\"violated\"].mean()\n        a, u = mr.get(\"ambiguous\", np.nan), mr.get(\"unambiguous\", np.nan)\n        ct_m = pd.crosstab(mdf[\"condition\"], mdf[\"violated\"])\n        fp = float(stats.fisher_exact(ct_m.values)[1]) if ct_m.shape == (2, 2) else float(\"nan\")\n        per_model[mname] = {\n            \"ambiguous_rate\": float(a), \"unambiguous_rate\": float(u),\n            \"difference\": float(a - u) if not (np.isnan(a) or np.isnan(u)) else None,\n            \"fisher_p\": fp,\n        }\n\n    return {\"global\": glob, \"per_type\": per_type, \"per_model\": per_model}\n\n\ndef _type_effect(df: pd.DataFrame) -> dict:\n    \"\"\"(b) 6-way chi-square across ambiguity types (ambiguous episodes only).\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    type_rates = amb.groupby(\"ambiguity_type\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    type_rates.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n\n    ct = pd.crosstab(amb[\"ambiguity_type\"], amb[\"violated\"])\n    if ct.shape[0] >= 2 and ct.shape[1] >= 2:\n        chi2, p, dof, _ = stats.chi2_contingency(ct.values)\n        v = analyze.cramers_v(ct.values)\n    else:\n        chi2, p, dof, v = float(\"nan\"), float(\"nan\"), 0, 0.0\n\n    return {\n        \"rates\": type_rates.to_dict(orient=\"index\"),\n        \"chi2\": float(chi2), \"p\": float(p), \"dof\": int(dof),\n        \"cramers_v\": float(v),\n    }\n\n\ndef _model_effect(df: pd.DataFrame) -> dict:\n    \"\"\"(c) Model comparison: gpt-5.4 vs gpt-4.1 violation rates.\"\"\"\n    df = df.copy()\n    df[\"violated\"] = analyze.binarize_violations(df)\n\n    model_rates = df.groupby(\"model\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    model_rates.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n\n    ct = pd.crosstab(df[\"model\"], df[\"violated\"])\n    if ct.shape == (2, 2):\n        chi2, p, _, _ = stats.chi2_contingency(ct.values)\n        v = analyze.cramers_v(ct.values)\n    else:\n        chi2, p, v = float(\"nan\"), float(\"nan\"), 0.0\n\n    # Ambiguous-only subset\n    amb = df[df[\"condition\"] == \"ambiguous\"]\n    amb_rates = amb.groupby(\"model\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    amb_rates.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n    ct_a = pd.crosstab(amb[\"model\"], amb[\"violated\"])\n    if ct_a.shape == (2, 2):\n        chi2_a, p_a, _, _ = stats.chi2_contingency(ct_a.values)\n    else:\n        chi2_a, p_a = float(\"nan\"), float(\"nan\")\n\n    return {\n        \"overall\": model_rates.to_dict(orient=\"index\"),\n        \"overall_chi2\": float(chi2), \"overall_p\": float(p),\n        \"cramers_v\": float(v),\n        \"ambiguous_only\": amb_rates.to_dict(orient=\"index\"),\n        \"ambiguous_chi2\": float(chi2_a), \"ambiguous_p\": float(p_a),\n    }\n\n\ndef _interaction(df: pd.DataFrame) -> dict:\n    \"\"\"(d) Model x Type interaction (ambiguous episodes only).\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    per_model_rates = {}\n    per_model_chi2 = {}\n    rankings = {}\n\n    for mname, mdf in amb.groupby(\"model\"):\n        tr = mdf.groupby(\"ambiguity_type\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n        tr.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n        per_model_rates[mname] = tr.to_dict(orient=\"index\")\n\n        ct = pd.crosstab(mdf[\"ambiguity_type\"], mdf[\"violated\"])\n        if ct.shape[0] >= 2 and ct.shape[1] >= 2:\n            chi2, p, dof, _ = stats.chi2_contingency(ct.values)\n            v = analyze.cramers_v(ct.values)\n        else:\n            chi2, p, dof, v = float(\"nan\"), float(\"nan\"), 0, 0.0\n        per_model_chi2[mname] = {\n            \"chi2\": float(chi2), \"p\": float(p),\n            \"dof\": int(dof), \"cramers_v\": float(v),\n        }\n\n        sorted_types = sorted(\n            per_model_rates[mname].items(),\n            key=lambda x: x[1][\"violation_rate\"], reverse=True,\n        )\n        rankings[mname] = [t[0] for t in sorted_types]\n\n    return {\n        \"per_model_type_rates\": per_model_rates,\n        \"per_model_chi2\": per_model_chi2,\n        \"type_rankings\": rankings,\n    }\n\n\ndef _print_full_report(binary: dict, type_eff: dict,\n                       model_eff: dict, interact: dict):\n    \"\"\"Print formatted analysis report to console.\"\"\"\n    print(\"\\n\" + \"=\" * 72)\n    print(\"FULL STUDY — STATISTICAL ANALYSIS REPORT\")\n    print(\"=\" * 72)\n\n    # (a) Binary effect\n    print(\"\\n-- (a) Binary Effect: Ambiguous vs Unambiguous --\\n\")\n    g = binary[\"global\"]\n    diff_str = f\"{g['difference']:+.1%}\" if g[\"difference\"] is not None else \"N/A\"\n    print(f\"  Global: amb={g['ambiguous_rate']:.1%}  unamb={g['unambiguous_rate']:.1%}\"\n          f\"  D={diff_str}  chi2 p={g['p']:.4f}\")\n\n    print(f\"\\n  {'Type':<25} {'Amb':>7} {'Unamb':>7} {'D':>7} {'Fisher p':>9}\")\n    print(f\"  {'-'*25} {'-'*7} {'-'*7} {'-'*7} {'-'*9}\")\n    for atype in sorted(binary[\"per_type\"]):\n        r = binary[\"per_type\"][atype]\n        d = r[\"difference\"]\n        if d is not None:\n            print(f\"  {atype:<25} {r['ambiguous_rate']:>6.1%} {r['unambiguous_rate']:>6.1%}\"\n                  f\" {d:>+6.1%} {r['fisher_p']:>9.4f}\")\n        else:\n            print(f\"  {atype:<25}  insufficient data\")\n\n    print(f\"\\n  {'Model':<15} {'Amb':>7} {'Unamb':>7} {'D':>7} {'Fisher p':>9}\")\n    print(f\"  {'-'*15} {'-'*7} {'-'*7} {'-'*7} {'-'*9}\")\n    for mname in sorted(binary[\"per_model\"]):\n        r = binary[\"per_model\"][mname]\n        d = r[\"difference\"]\n        if d is not None:\n            print(f\"  {mname:<15} {r['ambiguous_rate']:>6.1%} {r['unambiguous_rate']:>6.1%}\"\n                  f\" {d:>+6.1%} {r['fisher_p']:>9.4f}\")\n\n    # (b) Type effect\n    print(\"\\n-- (b) Type Effect: 6-way chi-square (ambiguous only) --\\n\")\n    rates = type_eff.get(\"rates\", {})\n    print(f\"  {'Type':<25} {'Rate':>10} {'N':>6}\")\n    print(f\"  {'-'*25} {'-'*10} {'-'*6}\")\n    for atype in sorted(rates):\n        r = rates[atype]\n        print(f\"  {atype:<25} {r['violation_rate']:>9.1%} {r['n_total']:>6.0f}\")\n    print(f\"\\n  chi2={type_eff['chi2']:.3f}  p={type_eff['p']:.4f}\"\n          f\"  dof={type_eff['dof']}  Cramer's V={type_eff['cramers_v']:.3f}\")\n\n    # (c) Model effect\n    print(\"\\n-- (c) Model Effect --\\n\")\n    ov = model_eff.get(\"overall\", {})\n    print(f\"  {'Model':<15} {'Rate':>8} {'N_viol':>7} {'N':>6}\")\n    print(f\"  {'-'*15} {'-'*8} {'-'*7} {'-'*6}\")\n    for mname in sorted(ov):\n        r = ov[mname]\n        print(f\"  {mname:<15} {r['violation_rate']:>7.1%} {r['n_violations']:>7.0f}\"\n              f\" {r['n_total']:>6.0f}\")\n    print(f\"\\n  Overall: chi2 p={model_eff['overall_p']:.4f}  V={model_eff['cramers_v']:.3f}\")\n    print(f\"  Ambiguous-only: chi2 p={model_eff['ambiguous_p']:.4f}\")\n\n    # (d) Interaction\n    print(\"\\n-- (d) Model x Type Interaction --\\n\")\n    for mname in sorted(interact.get(\"per_model_chi2\", {})):\n        c = interact[\"per_model_chi2\"][mname]\n        print(f\"  [{mname}] type chi2={c['chi2']:.3f}  p={c['p']:.4f}\"\n              f\"  V={c['cramers_v']:.3f}\")\n    print()\n    for mname in sorted(interact.get(\"type_rankings\", {})):\n        ranking = interact[\"type_rankings\"][mname]\n        print(f\"  {mname}: {' > '.join(ranking)}\")\n\n    print(\"\\n\" + \"=\" * 72)\n\n\n# ---------------------------------------------------------------------------\n# Phase 3 Extended: Dream reviewer analyses (A3, A4, A10 + bootstrap/McNemar/Fleiss)\n# ---------------------------------------------------------------------------\n\ndef run_power_analysis(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Dream A3: Power analysis for C2 (type uniformity) and C3 (per-type).\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    types = sorted(amb[\"ambiguity_type\"].unique())\n    n_types = len(types)\n    alpha = 0.05\n    target_power = 0.80\n\n    def _find_mde(n_total, df_val):\n        crit = stats.chi2.ppf(1 - alpha, df_val)\n        lo, hi = 1e-4, 1.0\n        for _ in range(200):\n            mid = (lo + hi) / 2\n            pwr = 1 - stats.ncx2.cdf(crit, df_val, n_total * mid ** 2)\n            if pwr < target_power:\n                lo = mid\n            else:\n                hi = mid\n        return (lo + hi) / 2\n\n    def _compute_power(w, n_total, df_val):\n        crit = stats.chi2.ppf(1 - alpha, df_val)\n        return float(1 - stats.ncx2.cdf(crit, df_val, n_total * w ** 2))\n\n    c2_n_per_type = 200\n    c2_n_total = c2_n_per_type * n_types\n    c2_df = max(n_types - 1, 1)\n    c2_mde = _find_mde(c2_n_total, c2_df)\n\n    c3_n = 200\n    c3_df = 1\n    c3_mde = _find_mde(c3_n, c3_df)\n\n    ct = pd.crosstab(amb[\"ambiguity_type\"], amb[\"violated\"])\n    observed_v = (\n        analyze.cramers_v(ct.values)\n        if ct.shape[0] >= 2 and ct.shape[1] >= 2\n        else 0.0\n    )\n\n    actual_n = len(amb)\n    mde_actual = _find_mde(actual_n, c2_df)\n    power_at_observed = (\n        _compute_power(observed_v, actual_n, c2_df) if observed_v > 0 else 0.0\n    )\n\n    underpowered = observed_v < 0.20 and c2_mde > observed_v\n\n    result = {\n        \"c2_type_uniformity\": {\n            \"design_N_per_type\": c2_n_per_type,\n            \"design_N_total\": c2_n_total,\n            \"n_types\": n_types,\n            \"df\": c2_df,\n            \"alpha\": alpha,\n            \"target_power\": target_power,\n            \"mde_cramers_v\": round(c2_mde, 4),\n        },\n        \"c3_per_type_comparison\": {\n            \"design_N\": c3_n,\n            \"df\": c3_df,\n            \"alpha\": alpha,\n            \"target_power\": target_power,\n            \"mde_cramers_v\": round(c3_mde, 4),\n        },\n        \"observed_cramers_v\": round(float(observed_v), 4),\n        \"actual_sample\": {\n            \"N_total\": actual_n,\n            \"per_type\": {\n                t: int(v)\n                for t, v in amb.groupby(\"ambiguity_type\").size().items()\n            },\n            \"mde_cramers_v\": round(mde_actual, 4),\n            \"power_at_observed\": round(power_at_observed, 4),\n        },\n        \"underpowered_warning\": underpowered,\n    }\n\n    out = ANALYSIS_DIR / \"power_analysis.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_tost_equivalence(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Dream A4: TOST equivalence test for C2 type uniformity.\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    types = sorted(amb[\"ambiguity_type\"].unique())\n    margins = [0.15, 0.10]\n\n    results_by_margin = {}\n    for margin in margins:\n        pairwise = []\n        for i in range(len(types)):\n            for j in range(i + 1, len(types)):\n                t1, t2 = types[i], types[j]\n                d1 = amb[amb[\"ambiguity_type\"] == t1][\"violated\"]\n                d2 = amb[amb[\"ambiguity_type\"] == t2][\"violated\"]\n                p1, n1 = float(d1.mean()), len(d1)\n                p2, n2 = float(d2.mean()), len(d2)\n                diff = p1 - p2\n\n                if n1 > 0 and n2 > 0:\n                    se = np.sqrt(\n                        p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2\n                    )\n                else:\n                    se = float(\"inf\")\n\n                if se > 0 and np.isfinite(se):\n                    z_lower = (diff + margin) / se\n                    p_lower = float(1 - stats.norm.cdf(z_lower))\n                    z_upper = (diff - margin) / se\n                    p_upper = float(stats.norm.cdf(z_upper))\n                    tost_p = max(p_lower, p_upper)\n                    equivalent = tost_p < 0.05\n                else:\n                    z_lower = z_upper = tost_p = float(\"nan\")\n                    p_lower = p_upper = float(\"nan\")\n                    equivalent = False\n\n                pairwise.append({\n                    \"type_1\": t1,\n                    \"type_2\": t2,\n                    \"rate_1\": round(p1, 4),\n                    \"rate_2\": round(p2, 4),\n                    \"difference\": round(diff, 4),\n                    \"se\": round(float(se), 4),\n                    \"z_lower\": round(float(z_lower), 4),\n                    \"p_lower\": round(float(p_lower), 4),\n                    \"z_upper\": round(float(z_upper), 4),\n                    \"p_upper\": round(float(p_upper), 4),\n                    \"tost_p\": round(float(tost_p), 4),\n                    \"equivalent\": equivalent,\n                })\n\n        all_equiv = all(p[\"equivalent\"] for p in pairwise) if pairwise else False\n        results_by_margin[f\"margin_{int(margin * 100)}pp\"] = {\n            \"margin\": margin,\n            \"pairwise\": pairwise,\n            \"all_pairs_equivalent\": all_equiv,\n        }\n\n    result = {\n        \"test\": \"TOST two one-sided z-tests for proportions\",\n        \"margin_justification\": (\n            \"15pp = practical significance threshold for policy remediation \"\n            \"cost; 10pp = stricter robustness check\"\n        ),\n        **results_by_margin,\n    }\n\n    out = ANALYSIS_DIR / \"tost_equivalence.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef _bca_ci(g1: np.ndarray, g2: np.ndarray, rng, B: int = 10000,\n            alpha: float = 0.05) -> dict:\n    \"\"\"BCa bootstrap CI for difference in means (g1 - g2).\"\"\"\n    n1, n2 = len(g1), len(g2)\n    if n1 == 0 or n2 == 0:\n        return {\"observed_diff\": None, \"ci_lower\": None, \"ci_upper\": None}\n\n    observed = float(g1.mean() - g2.mean())\n\n    idx1 = rng.integers(0, n1, size=(B, n1))\n    idx2 = rng.integers(0, n2, size=(B, n2))\n    boot_stats = g1[idx1].mean(axis=1) - g2[idx2].mean(axis=1)\n\n    prop_below = np.mean(boot_stats < observed)\n    prop_below = np.clip(prop_below, 1 / (B + 1), B / (B + 1))\n    z0 = stats.norm.ppf(prop_below)\n\n    if n1 >= 2 and n2 >= 2:\n        jack = np.empty(n1 + n2)\n        g1_sum, g2_mean = g1.sum(), g2.mean()\n        g1_mean, g2_sum = g1.mean(), g2.sum()\n        for i in range(n1):\n            jack[i] = (g1_sum - g1[i]) / (n1 - 1) - g2_mean\n        for j in range(n2):\n            jack[n1 + j] = g1_mean - (g2_sum - g2[j]) / (n2 - 1)\n        jm = jack.mean()\n        d = jm - jack\n        denom = 6 * np.sum(d ** 2) ** 1.5\n        a = float(np.sum(d ** 3) / denom) if denom > 0 else 0.0\n    else:\n        a = 0.0\n\n    z_lo = stats.norm.ppf(alpha / 2)\n    z_hi = stats.norm.ppf(1 - alpha / 2)\n\n    def _adj(z):\n        num = z0 + z\n        den = 1 - a * num\n        if abs(den) < 1e-12:\n            return 0.5\n        return stats.norm.cdf(z0 + num / den)\n\n    a1 = np.clip(_adj(z_lo), 0.5 / B, 1 - 0.5 / B)\n    a2 = np.clip(_adj(z_hi), 0.5 / B, 1 - 0.5 / B)\n\n    return {\n        \"observed_diff\": round(observed, 4),\n        \"ci_lower\": round(float(np.percentile(boot_stats, 100 * a1)), 4),\n        \"ci_upper\": round(float(np.percentile(boot_stats, 100 * a2)), 4),\n        \"z0\": round(float(z0), 4),\n        \"acceleration\": round(a, 6),\n    }\n\n\ndef run_bootstrap_ci(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"BCa bootstrap 95% CIs for all pairwise comparisons.\"\"\"\n    B = 10000\n    rng = np.random.default_rng(42)\n\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc).astype(float)\n\n    results: dict = {\"n_resamples\": B}\n\n    # Global ambig vs unambig\n    amb_v = dfc.loc[dfc[\"condition\"] == \"ambiguous\", \"violated\"].values\n    una_v = dfc.loc[dfc[\"condition\"] == \"unambiguous\", \"violated\"].values\n    results[\"ambig_vs_unambig_global\"] = _bca_ci(amb_v, una_v, rng, B)\n\n    # Per-type ambig vs unambig\n    per_type = {}\n    for atype in sorted(dfc[\"ambiguity_type\"].unique()):\n        tdf = dfc[dfc[\"ambiguity_type\"] == atype]\n        a = tdf.loc[tdf[\"condition\"] == \"ambiguous\", \"violated\"].values\n        u = tdf.loc[tdf[\"condition\"] == \"unambiguous\", \"violated\"].values\n        per_type[atype] = _bca_ci(a, u, rng, B)\n    results[\"ambig_vs_unambig_per_type\"] = per_type\n\n    # Type pairs (ambiguous only)\n    amb_df = dfc[dfc[\"condition\"] == \"ambiguous\"]\n    types = sorted(amb_df[\"ambiguity_type\"].unique())\n    type_pairs = {}\n    for i in range(len(types)):\n        for j in range(i + 1, len(types)):\n            t1, t2 = types[i], types[j]\n            v1 = amb_df.loc[amb_df[\"ambiguity_type\"] == t1, \"violated\"].values\n            v2 = amb_df.loc[amb_df[\"ambiguity_type\"] == t2, \"violated\"].values\n            type_pairs[f\"{t1}_vs_{t2}\"] = _bca_ci(v1, v2, rng, B)\n    results[\"type_pairs_ambiguous\"] = type_pairs\n\n    # Model pairs\n    models = sorted(dfc[\"model\"].unique())\n    model_pairs = {}\n    for i in range(len(models)):\n        for j in range(i + 1, len(models)):\n            m1, m2 = models[i], models[j]\n            v1 = dfc.loc[dfc[\"model\"] == m1, \"violated\"].values\n            v2 = dfc.loc[dfc[\"model\"] == m2, \"violated\"].values\n            model_pairs[f\"{m1}_vs_{m2}\"] = _bca_ci(v1, v2, rng, B)\n    results[\"model_pairs\"] = model_pairs\n\n    out = ANALYSIS_DIR / \"bootstrap_ci.json\"\n    with open(out, \"w\") as f:\n        json.dump(results, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return results\n\n\ndef run_mcnemar_matched(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Matched-pair McNemar test for C1 (binary effect).\"\"\"\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n\n    amb = dfc.loc[dfc[\"condition\"] == \"ambiguous\", [\"clause_id\", \"model\", \"violated\"]]\n    una = dfc.loc[dfc[\"condition\"] == \"unambiguous\", [\"clause_id\", \"model\", \"violated\"]]\n    merged = pd.merge(amb, una, on=[\"clause_id\", \"model\"], suffixes=(\"_amb\", \"_una\"))\n\n    if merged.empty:\n        return {\"error\": \"No matched pairs found\"}\n\n    merged[\"amb_only\"] = merged[\"violated_amb\"] & ~merged[\"violated_una\"]\n    merged[\"una_only\"] = ~merged[\"violated_amb\"] & merged[\"violated_una\"]\n    merged[\"both\"] = merged[\"violated_amb\"] & merged[\"violated_una\"]\n    merged[\"neither\"] = ~merged[\"violated_amb\"] & ~merged[\"violated_una\"]\n\n    b_total = int(merged[\"amb_only\"].sum())\n    c_total = int(merged[\"una_only\"].sum())\n    n_pairs = len(merged)\n    n_disc = b_total + c_total\n\n    # Overall McNemar\n    if n_disc > 0:\n        if n_disc >= 25:\n            mcn_chi2 = float((abs(b_total - c_total) - 1) ** 2 / n_disc)\n            mcn_p = float(1 - stats.chi2.cdf(mcn_chi2, 1))\n            method = \"chi-square (continuity corrected)\"\n        else:\n            mcn_p = float(stats.binomtest(b_total, n_disc, 0.5).pvalue)\n            mcn_chi2 = None\n            method = \"exact binomial\"\n    else:\n        mcn_chi2 = 0.0\n        mcn_p = 1.0\n        method = \"no discordant pairs\"\n\n    # Odds ratio b/c with Wald 95% CI\n    if b_total > 0 and c_total > 0:\n        or_val = b_total / c_total\n        log_or = np.log(or_val)\n        se_log = np.sqrt(1 / b_total + 1 / c_total)\n        or_lo = float(np.exp(log_or - 1.96 * se_log))\n        or_hi = float(np.exp(log_or + 1.96 * se_log))\n    elif c_total == 0 and b_total > 0:\n        or_val, or_lo, or_hi = float(\"inf\"), float(\"nan\"), float(\"nan\")\n    elif b_total == 0 and c_total > 0:\n        or_val, or_lo, or_hi = 0.0, float(\"nan\"), float(\"nan\")\n    else:\n        or_val = or_lo = or_hi = float(\"nan\")\n\n    # Per-model McNemar\n    per_model = {}\n    for model_name, mdf in merged.groupby(\"model\"):\n        b_m = int(mdf[\"amb_only\"].sum())\n        c_m = int(mdf[\"una_only\"].sum())\n        disc_m = b_m + c_m\n        if disc_m > 0:\n            p_m = float(stats.binomtest(b_m, disc_m, 0.5).pvalue)\n        else:\n            p_m = 1.0\n        per_model[model_name] = {\n            \"n_pairs\": len(mdf),\n            \"b_amb_only\": b_m,\n            \"c_una_only\": c_m,\n            \"mcnemar_p\": round(p_m, 6),\n        }\n\n    # Mantel-Haenszel OR stratified by ambiguity_type\n    mh_strata = []\n    for atype, sdf in merged.groupby(\n        merged[\"clause_id\"].map(\n            lambda cid: dfc.loc[dfc[\"clause_id\"] == cid, \"ambiguity_type\"].iloc[0]\n            if cid in dfc[\"clause_id\"].values else \"unknown\"\n        )\n    ):\n        b_s = int(sdf[\"amb_only\"].sum())\n        c_s = int(sdf[\"una_only\"].sum())\n        a_s = int(sdf[\"both\"].sum())\n        d_s = int(sdf[\"neither\"].sum())\n        n_s = len(sdf)\n        mh_strata.append({\n            \"stratum\": atype, \"n\": n_s,\n            \"a\": a_s, \"b\": b_s, \"c\": c_s, \"d\": d_s,\n        })\n\n    # Haldane 0.5 correction for strata with zero cells\n    mh_num = 0.0\n    mh_den = 0.0\n    for s in mh_strata:\n        if s[\"n\"] == 0:\n            continue\n        a, b, c, d, n = s[\"a\"], s[\"b\"], s[\"c\"], s[\"d\"], s[\"n\"]\n        if a == 0 or b == 0 or c == 0 or d == 0:\n            a, b, c, d, n = a + 0.5, b + 0.5, c + 0.5, d + 0.5, n + 2\n        mh_num += b * d / n\n        mh_den += c * a / n\n    mh_or = mh_num / mh_den if mh_den > 0 else float(\"inf\") if mh_num > 0 else float(\"nan\")\n\n    def _safe_round(v, n=4):\n        if isinstance(v, float) and (np.isnan(v) or np.isinf(v)):\n            return str(v)\n        return round(float(v), n)\n\n    result = {\n        \"n_pairs\": n_pairs,\n        \"n_concordant\": int(merged[\"both\"].sum() + merged[\"neither\"].sum()),\n        \"n_discordant\": n_disc,\n        \"b_amb_only\": b_total,\n        \"c_una_only\": c_total,\n        \"mcnemar\": {\n            \"method\": method,\n            \"statistic\": _safe_round(mcn_chi2) if mcn_chi2 is not None else None,\n            \"p\": round(mcn_p, 6),\n        },\n        \"odds_ratio\": {\n            \"or\": _safe_round(or_val),\n            \"ci_95_lower\": _safe_round(or_lo),\n            \"ci_95_upper\": _safe_round(or_hi),\n        },\n        \"mantel_haenszel\": {\n            \"or\": _safe_round(mh_or),\n            \"correction\": \"haldane_0.5\",\n            \"note\": \"Primary OR=44.8 (non-stratified); MH OR is supplementary\",\n            \"strata\": mh_strata,\n        },\n        \"per_model\": per_model,\n    }\n\n    out = ANALYSIS_DIR / \"mcnemar_matched.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_information_delta(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Dream A10: Per-type information (token count) delta + logistic regression.\"\"\"\n    import statsmodels.api as sm\n\n    clause_map = {}\n    for c in clauses:\n        cid = c[\"clause_id\"]\n        amb_tok = len(c.get(\"ambiguous_clause\", \"\").split())\n        una_tok = len(c.get(\"unambiguous_clause\", \"\").split())\n        clause_map[cid] = {\n            \"ambiguity_type\": c.get(\"ambiguity_type\", \"unknown\"),\n            \"amb_tokens\": amb_tok,\n            \"una_tokens\": una_tok,\n            \"token_delta\": una_tok - amb_tok,\n        }\n\n    # Per-type token delta stats\n    type_groups: dict[str, list[int]] = {}\n    for info in clause_map.values():\n        atype = info[\"ambiguity_type\"]\n        type_groups.setdefault(atype, []).append(info[\"token_delta\"])\n\n    type_deltas = {}\n    for atype, deltas in sorted(type_groups.items()):\n        arr = np.array(deltas)\n        type_deltas[atype] = {\n            \"mean\": round(float(arr.mean()), 2),\n            \"median\": round(float(np.median(arr)), 2),\n            \"std\": round(float(arr.std(ddof=1)), 2) if len(arr) > 1 else 0.0,\n            \"min\": int(arr.min()),\n            \"max\": int(arr.max()),\n            \"n_clauses\": len(arr),\n        }\n\n    # Merge into judgments\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc).astype(int)\n    dfc[\"token_delta\"] = dfc[\"clause_id\"].map(\n        lambda cid: clause_map.get(cid, {}).get(\"token_delta\", 0)\n    )\n    dfc[\"condition_amb\"] = (dfc[\"condition\"] == \"ambiguous\").astype(int)\n\n    # Logistic regression: violation ~ condition + type + token_delta + model\n    type_dummies = pd.get_dummies(\n        dfc[\"ambiguity_type\"], prefix=\"type\", drop_first=True, dtype=float\n    )\n    model_dummies = pd.get_dummies(\n        dfc[\"model\"], prefix=\"model\", drop_first=True, dtype=float\n    )\n    X = pd.concat(\n        [dfc[[\"condition_amb\", \"token_delta\"]].astype(float), type_dummies, model_dummies],\n        axis=1,\n    )\n    X = sm.add_constant(X)\n    y = dfc[\"violated\"]\n\n    logit_result: dict = {}\n    try:\n        fit = sm.Logit(y, X).fit(disp=0, maxiter=100)\n        coefficients = {}\n        ci = fit.conf_int()\n        for var in fit.params.index:\n            coefficients[var] = {\n                \"coef\": round(float(fit.params[var]), 4),\n                \"se\": round(float(fit.bse[var]), 4),\n                \"z\": round(float(fit.tvalues[var]), 4),\n                \"p\": round(float(fit.pvalues[var]), 6),\n                \"ci_lower\": round(float(ci.loc[var, 0]), 4),\n                \"ci_upper\": round(float(ci.loc[var, 1]), 4),\n            }\n        logit_result = {\n            \"converged\": bool(fit.mle_retvals.get(\"converged\", False)),\n            \"n_obs\": int(fit.nobs),\n            \"pseudo_r2\": round(float(fit.prsquared), 4),\n            \"llr_p\": round(float(fit.llr_pvalue), 6),\n            \"coefficients\": coefficients,\n        }\n    except Exception as e:\n        logit_result = {\"error\": str(e)}\n\n    result = {\n        \"per_type_token_delta\": type_deltas,\n        \"logistic_regression\": logit_result,\n    }\n\n    out = ANALYSIS_DIR / \"information_delta.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_fleiss_kappa(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Fleiss' kappa for inter-model agreement on violation judgment.\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        result = {\"error\": \"No ambiguous episodes\"}\n        out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n        with open(out, \"w\") as f:\n            json.dump(result, f, indent=2)\n        print(f\"  -> {out.name}\")\n        return result\n\n    amb[\"violated\"] = analyze.binarize_violations(amb).astype(int)\n    models = sorted(amb[\"model\"].unique())\n    n_models = len(models)\n\n    if n_models < 2:\n        result = {\"error\": f\"Need >= 2 models, found {n_models}\", \"models\": models}\n        out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n        with open(out, \"w\") as f:\n            json.dump(result, f, indent=2)\n        print(f\"  -> {out.name}\")\n        return result\n\n    ratings = amb.groupby(\"clause_id\").agg(\n        n_violated=(\"violated\", \"sum\"),\n        n_raters=(\"violated\", \"count\"),\n    ).reset_index()\n    ratings = ratings[ratings[\"n_raters\"] >= 2]\n\n    if ratings.empty:\n        result = {\"error\": \"No clauses with >= 2 model ratings\"}\n        out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n        with open(out, \"w\") as f:\n            json.dump(result, f, indent=2)\n        print(f\"  -> {out.name}\")\n        return result\n\n    ratings[\"n_not\"] = ratings[\"n_raters\"] - ratings[\"n_violated\"]\n    N = len(ratings)\n    mat = ratings[[\"n_violated\", \"n_not\"]].values  # (N, 2)\n    n_arr = ratings[\"n_raters\"].values\n\n    # Per-subject agreement P_i\n    P_i = np.zeros(N)\n    for i in range(N):\n        ni = n_arr[i]\n        if ni >= 2:\n            P_i[i] = (np.sum(mat[i] ** 2) - ni) / (ni * (ni - 1))\n    P_bar = float(P_i.mean())\n\n    total_ratings = n_arr.sum()\n    p_j = mat.sum(axis=0) / total_ratings  # (2,)\n    P_e = float(np.sum(p_j ** 2))\n\n    kappa = (P_bar - P_e) / (1 - P_e) if P_e < 1.0 else 0.0\n\n    # SE (large sample, Fleiss 1971)\n    n_fixed = int(np.median(n_arr))\n    if N > 1 and P_e < 1.0 and n_fixed >= 2:\n        inner = (\n            P_e\n            - (2 * n_fixed - 3) * P_e ** 2\n            + 2 * (n_fixed - 2) * np.sum(p_j ** 3)\n        )\n        se = float(np.sqrt(2 / (N * n_fixed * (n_fixed - 1))) * np.sqrt(\n            abs(inner) / (1 - P_e) ** 2\n        ))\n        z_val = kappa / se if se > 0 else float(\"nan\")\n        p_val = float(2 * (1 - stats.norm.cdf(abs(z_val)))) if np.isfinite(z_val) else float(\"nan\")\n    else:\n        se = z_val = p_val = float(\"nan\")\n\n    if kappa < 0:\n        interp = \"less than chance agreement\"\n    elif kappa < 0.20:\n        interp = \"slight agreement\"\n    elif kappa < 0.40:\n        interp = \"fair agreement\"\n    elif kappa < 0.60:\n        interp = \"moderate agreement\"\n    elif kappa < 0.80:\n        interp = \"substantial agreement\"\n    else:\n        interp = \"almost perfect agreement\"\n\n    result = {\n        \"n_clauses\": N,\n        \"n_models\": n_models,\n        \"models\": models,\n        \"n_raters_per_clause\": {\n            \"min\": int(n_arr.min()),\n            \"max\": int(n_arr.max()),\n            \"mean\": round(float(n_arr.mean()), 1),\n        },\n        \"category_proportions\": {\n            \"violated\": round(float(p_j[0]), 4),\n            \"not_violated\": round(float(p_j[1]), 4),\n        },\n        \"fleiss_kappa\": round(float(kappa), 4),\n        \"se\": round(float(se), 4) if np.isfinite(se) else None,\n        \"z\": round(float(z_val), 4) if np.isfinite(z_val) else None,\n        \"p\": round(float(p_val), 6) if np.isfinite(p_val) else None,\n        \"interpretation\": interp,\n    }\n\n    out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_layer_effect_test(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"C3: Formal test of specification-layer vs linguistic-layer violation rates.\"\"\"\n    SPEC_TYPES = {\"incompleteness\", \"conditional_precedence\", \"authorization_scope\"}\n    LING_TYPES = {\"scopal\", \"lexical\", \"coreferential\"}\n\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n\n    # Filter to ambiguous condition only\n    amb = dfc[dfc[\"condition\"] == \"ambiguous\"].copy()\n    amb[\"layer\"] = amb[\"ambiguity_type\"].map(\n        lambda t: \"specification\" if t in SPEC_TYPES else \"linguistic\" if t in LING_TYPES else \"unknown\"\n    )\n    amb = amb[amb[\"layer\"] != \"unknown\"]\n\n    spec = amb[amb[\"layer\"] == \"specification\"]\n    ling = amb[amb[\"layer\"] == \"linguistic\"]\n\n    spec_n = len(spec)\n    spec_v = int(spec[\"violated\"].sum())\n    ling_n = len(ling)\n    ling_v = int(ling[\"violated\"].sum())\n\n    spec_rate = spec_v / spec_n if spec_n > 0 else 0\n    ling_rate = ling_v / ling_n if ling_n > 0 else 0\n    delta_pp = (spec_rate - ling_rate) * 100\n\n    from scipy.stats import chi2_contingency\n    table = np.array([\n        [spec_v, spec_n - spec_v],\n        [ling_v, ling_n - ling_v],\n    ])\n    chi2, p_val, dof, expected = chi2_contingency(table, correction=False)\n\n    n_total = spec_n + ling_n\n    cramers_v = np.sqrt(chi2 / n_total) if n_total > 0 else 0\n\n    a, b = spec_v, spec_n - spec_v\n    c, d = ling_v, ling_n - ling_v\n    if b > 0 and c > 0 and d > 0 and a > 0:\n        or_val = (a * d) / (b * c)\n        log_or = np.log(or_val)\n        se_log = np.sqrt(1/a + 1/b + 1/c + 1/d)\n        or_lo = float(np.exp(log_or - 1.96 * se_log))\n        or_hi = float(np.exp(log_or + 1.96 * se_log))\n    else:\n        or_val = or_lo = or_hi = float(\"nan\")\n\n    np.random.seed(42)\n    n_boot = 10000\n    spec_arr = spec[\"violated\"].values.astype(float)\n    ling_arr = ling[\"violated\"].values.astype(float)\n    boot_deltas = []\n    for _ in range(n_boot):\n        s_idx = np.random.randint(0, len(spec_arr), len(spec_arr))\n        l_idx = np.random.randint(0, len(ling_arr), len(ling_arr))\n        boot_deltas.append((spec_arr[s_idx].mean() - ling_arr[l_idx].mean()) * 100)\n    boot_deltas = np.array(boot_deltas)\n    ci_lo = float(np.percentile(boot_deltas, 2.5))\n    ci_hi = float(np.percentile(boot_deltas, 97.5))\n\n    per_type = {}\n    for atype in list(SPEC_TYPES) + list(LING_TYPES):\n        subset = amb[amb[\"ambiguity_type\"] == atype]\n        if len(subset) > 0:\n            rate = float(subset[\"violated\"].mean())\n            per_type[atype] = {\n                \"n\": len(subset),\n                \"violations\": int(subset[\"violated\"].sum()),\n                \"rate\": round(rate * 100, 2),\n                \"layer\": \"specification\" if atype in SPEC_TYPES else \"linguistic\",\n            }\n\n    result = {\n        \"test\": \"layer_effect (C3)\",\n        \"specification_layer\": {\n            \"types\": sorted(SPEC_TYPES),\n            \"n\": spec_n,\n            \"violations\": spec_v,\n            \"rate_pct\": round(spec_rate * 100, 2),\n        },\n        \"linguistic_layer\": {\n            \"types\": sorted(LING_TYPES),\n            \"n\": ling_n,\n            \"violations\": ling_v,\n            \"rate_pct\": round(ling_rate * 100, 2),\n        },\n        \"delta_pp\": round(delta_pp, 2),\n        \"bootstrap_ci_95\": [round(ci_lo, 2), round(ci_hi, 2)],\n        \"chi_squared\": {\n            \"statistic\": round(float(chi2), 4),\n            \"df\": int(dof),\n            \"p\": round(float(p_val), 6),\n        },\n        \"cramers_v\": round(float(cramers_v), 4),\n        \"odds_ratio\": {\n            \"or\": round(float(or_val), 4) if np.isfinite(or_val) else str(or_val),\n            \"ci_95\": [round(or_lo, 4) if np.isfinite(or_lo) else str(or_lo),\n                       round(or_hi, 4) if np.isfinite(or_hi) else str(or_hi)],\n        },\n        \"per_type_detail\": per_type,\n    }\n\n    out = ANALYSIS_DIR / \"layer_effect_test.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):\n    \"\"\"Load all judgments and run the full analysis suite.\"\"\"\n    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)\n\n    df = _load_all_judgments(models)\n    if df.empty:\n        print(\"No judgments found. Run Phase 2 first.\")\n        return\n\n    print(f\"Loaded {len(df)} judgments ({df['model'].nunique()} models, \"\n          f\"{df['ambiguity_type'].nunique()} types)\")\n\n    binary = _binary_effect(df)\n    type_eff = _type_effect(df)\n    model_eff = _model_effect(df)\n    interact = _interaction(df)\n\n    # JSON report\n    report = {\n        \"binary_effect\": binary,\n        \"type_effect\": type_eff,\n        \"model_effect\": model_eff,\n        \"model_type_interaction\": interact,\n        \"n_judgments\": len(df),\n    }\n    with open(ANALYSIS_DIR / \"full_statistics.json\", \"w\") as f:\n        json.dump(report, f, indent=2, default=str)\n\n    # Per-clause summary CSV\n    summary = analyze.per_clause_summary(df)\n    summary.to_csv(ANALYSIS_DIR / \"per_clause_summary.csv\", index=False)\n\n    # Aggregated rates CSV\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n    agg = dfc.groupby(\n        [\"model\", \"ambiguity_type\", \"condition\"]\n    )[\"violated\"].agg(\n        violation_rate=\"mean\", n_violations=\"sum\", n_total=\"count\",\n    ).reset_index()\n    agg.to_csv(ANALYSIS_DIR / \"aggregated_rates.csv\", index=False)\n\n    _print_full_report(binary, type_eff, model_eff, interact)\n\n    # Extended analyses (Dream reviewer)\n    clauses_path = config.ARTIFACTS_DIR / \"clause_templates_full.json\"\n    if clauses_path.exists():\n        with open(clauses_path) as f:\n            raw = json.load(f)\n        clauses_data = raw if isinstance(raw, list) else raw.get(\"clauses\", raw)\n    else:\n        clauses_data = []\n\n    print(\"\\n-- Extended analyses (Dream reviewer) --\\n\")\n    run_power_analysis(df, clauses_data)\n    run_tost_equivalence(df, clauses_data)\n    run_bootstrap_ci(df, clauses_data)\n    run_mcnemar_matched(df, clauses_data)\n    if clauses_data:\n        run_information_delta(df, clauses_data)\n    else:\n        print(\"  (skipped information_delta -- no clauses file)\")\n    run_fleiss_kappa(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")\n    print(\"  - full_statistics.json\")\n    print(\"  - per_clause_summary.csv\")\n    print(\"  - aggregated_rates.csv\")\n    print(\"  - power_analysis.json\")\n    print(\"  - tost_equivalence.json\")\n    print(\"  - bootstrap_ci.json\")\n    print(\"  - mcnemar_matched.json\")\n    if clauses_data:\n        print(\"  - information_delta.json\")\n    print(\"  - fleiss_kappa.json\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args(argv: list[str] | None = None) -> argparse.Namespace:\n    parser = argparse.ArgumentParser(\n        description=\"Full study execution for policy ambiguity safety experiment.\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n        epilog=\"\"\"\\\nExamples:\n  python run_full_study.py --phase 1 --clauses clause_templates_full.json\n  python run_full_study.py --phase 2 --resume\n  python run_full_study.py --phase 3\n  python run_full_study.py --all --clauses clause_templates_full.json\n\"\"\",\n    )\n    group = parser.add_mutually_exclusive_group(required=True)\n    group.add_argument(\n        \"--phase\", type=int, choices=[1, 2, 3],\n        help=\"Run a specific phase (1=episodes, 2=judge, 3=analysis).\",\n    )\n    group.add_argument(\n        \"--all\", action=\"store_true\",\n        help=\"Run all 3 phases sequentially.\",\n    )\n    parser.add_argument(\n        \"--clauses\",\n        default=str(config.ARTIFACTS_DIR / \"clause_templates_full.json\"),\n        help=\"Path to clauses JSON (default: clause_templates_full.json).\",\n    )\n    parser.add_argument(\n        \"--models\", default=\",\".join(DEFAULT_MODELS),\n        help=f\"Comma-separated model names (default: {','.join(DEFAULT_MODELS)}).\",\n    )\n    parser.add_argument(\n        \"--concurrency\", type=int, default=config.DEFAULT_CONCURRENCY,\n        help=f\"Max concurrent API calls (default: {config.DEFAULT_CONCURRENCY}).\",\n    )\n    parser.add_argument(\n        \"--resume\", action=\"store_true\", default=True,\n        help=\"Skip completed episodes/judgments (default: True).\",\n    )\n    parser.add_argument(\n        \"--no-resume\", action=\"store_false\", dest=\"resume\",\n        help=\"Re-run everything from scratch.\",\n    )\n    return parser.parse_args(argv)\n\n\ndef main(argv: list[str] | None = None):\n    args = parse_args(argv)\n    models = [m.strip() for m in args.models.split(\",\")]\n    for m in models:\n        if m not in config.MODELS:\n            print(f\"Error: unknown model '{m}'. Available: {list(config.MODELS.keys())}\")\n            sys.exit(1)\n\n    clauses = harness.load_clauses(args.clauses)\n    phases = [1, 2, 3] if args.all else [args.phase]\n\n    for phase in phases:\n        print(f\"\\n{'=' * 40} Phase {phase} {'=' * 40}\\n\")\n        if phase == 1:\n            asyncio.run(run_phase1(clauses, models, args.concurrency, args.resume))\n        elif phase == 2:\n            asyncio.run(run_phase2(clauses, models, args.concurrency, args.resume))\n        elif phase == 3:\n            run_phase3(models)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 1283,
        "oldLines": 6,
        "newStart": 1283,
        "newLines": 7,
        "lines": [
          "     else:",
          "         print(\"  (skipped information_delta -- no clauses file)\")",
          "     run_fleiss_kappa(df, clauses_data)",
          "+    run_layer_effect_test(df, clauses_data)",
          " ",
          "     print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")",
          "     print(\"  - full_statistics.json\")"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_014rYuzfVf7s84rH8edW9kLW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
  "old_string": "    print(\"  - fleiss_kappa.json\")\n\n\n# ---------------------------------------------------------------------------",
  "new_string": "    print(\"  - fleiss_kappa.json\")\n    print(\"  - layer_effect_test.json\")\n\n\n# ---------------------------------------------------------------------------"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "1df3fe40-45bf-4afb-8428-620888599444",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xww4NEqwjVwxw47oW4bmcc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 290,
      "cache_read_input_tokens": 28960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 290
      },
      "output_tokens": 69,
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

_source line 14 · 2026-05-20T16:28:37.142Z_

<details><summary>↩ Tool result · `toolu_014rYuzfVf7s84rH8edW9kLW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "a9abe32a-4932-4d85-a0c7-81fcd8c6b38f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/run_full_study.py",
    "oldString": "    print(\"  - fleiss_kappa.json\")\n\n\n# ---------------------------------------------------------------------------",
    "newString": "    print(\"  - fleiss_kappa.json\")\n    print(\"  - layer_effect_test.json\")\n\n\n# ---------------------------------------------------------------------------",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Full study execution script for policy ambiguity safety experiments.\n\nOrchestrates the complete experiment pipeline:\n  Phase 1: Episode generation (300 clauses x 2 conditions x 2 models = 1,200 episodes)\n  Phase 2: Cross-judge evaluation (gpt-5.4 episodes judged by gpt-4.1, vice versa)\n  Phase 3: Statistical analysis (binary/type/model effects + interactions)\n\nInput:  artifacts/clause_templates_full.json (300 clauses, 6 types x 50)\nOutput: artifacts/full_study/{episodes,judgments,analysis}/\n\nDependencies: harness.py, judge.py, analyze.py, config.py\n\"\"\"\n\nimport argparse\nimport asyncio\nimport json\nimport sys\nimport time\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport config\nimport harness\nimport judge\nimport analyze\n\n# ---------------------------------------------------------------------------\n# Paths\n# ---------------------------------------------------------------------------\n\nFULL_STUDY_DIR = config.ARTIFACTS_DIR / \"full_study\"\nEPISODES_DIR = FULL_STUDY_DIR / \"episodes\"\nJUDGMENTS_DIR = FULL_STUDY_DIR / \"judgments\"\nANALYSIS_DIR = FULL_STUDY_DIR / \"analysis\"\nERRORS_FILE = FULL_STUDY_DIR / \"errors.jsonl\"\n\nDEFAULT_MODELS = [\"gpt-5.4\", \"gpt-4.1\", \"claude-sonnet-4-6\"]\n\n\n# ---------------------------------------------------------------------------\n# Phase 1: Episode Generation\n# ---------------------------------------------------------------------------\n\ndef _load_completed_episodes(model_dir: Path) -> set[str]:\n    \"\"\"Return set of 'clause_id|condition' keys already completed.\"\"\"\n    completed = set()\n    episodes_file = model_dir / \"episodes.jsonl\"\n    if episodes_file.exists():\n        with open(episodes_file) as f:\n            for line in f:\n                if line.strip():\n                    rec = json.loads(line)\n                    completed.add(f\"{rec['clause_id']}|{rec['condition']}\")\n    return completed\n\n\nasync def run_phase1(\n    clauses: list[dict],\n    models: list[str],\n    concurrency: int,\n    resume: bool,\n):\n    \"\"\"Generate episodes for all model x clause x condition combinations.\"\"\"\n    FULL_STUDY_DIR.mkdir(parents=True, exist_ok=True)\n\n    print(\"Preflight API check...\")\n    for m in models:\n        try:\n            await harness.preflight_check(m)\n            print(f\"  {m}: OK\")\n        except Exception as e:\n            print(f\"  {m}: FAILED — {e}\")\n            raise SystemExit(f\"Preflight failed for {m}. Fix API key/endpoint before running.\")\n\n    total_done = 0\n    total_errors = 0\n    total_skipped = 0\n\n    for model_name in models:\n        model_dir = EPISODES_DIR / model_name\n        model_dir.mkdir(parents=True, exist_ok=True)\n\n        completed = _load_completed_episodes(model_dir) if resume else set()\n        tasks = []\n        for clause in clauses:\n            for condition in (\"ambiguous\", \"unambiguous\"):\n                key = f\"{clause['clause_id']}|{condition}\"\n                if key in completed:\n                    total_skipped += 1\n                    continue\n                tasks.append((clause, condition))\n\n        if not tasks:\n            print(f\"[{model_name}] All {len(completed)} episodes complete.\")\n            continue\n\n        print(f\"[{model_name}] {len(tasks)} episodes to run \"\n              f\"(skipping {len(completed)}, concurrency={concurrency})\")\n\n        semaphore = asyncio.Semaphore(concurrency)\n        output_file = model_dir / \"episodes.jsonl\"\n        lock = asyncio.Lock()\n        done = 0\n        errors = 0\n\n        async def _run_one(clause, condition, _model=model_name):\n            nonlocal done, errors\n            async with semaphore:\n                try:\n                    result = await harness.run_episode(clause, condition, _model)\n                    validity = harness.validate_episode(result)\n                    if validity != \"ok\":\n                        raise RuntimeError(\n                            f\"Episode {validity}: {result.get('error', 'no assistant response')}\"\n                        )\n                    async with lock:\n                        with open(output_file, \"a\") as f:\n                            f.write(json.dumps(result, ensure_ascii=False) + \"\\n\")\n                        done += 1\n                        if done % 50 == 0:\n                            print(f\"  [{_model}] {done}/{len(tasks)}\")\n                except Exception as e:\n                    async with lock:\n                        errors += 1\n                        with open(ERRORS_FILE, \"a\") as f:\n                            f.write(json.dumps({\n                                \"phase\": 1, \"model\": _model,\n                                \"clause_id\": clause[\"clause_id\"],\n                                \"condition\": condition,\n                                \"error\": str(e),\n                                \"timestamp\": time.time(),\n                            }, ensure_ascii=False) + \"\\n\")\n\n        await asyncio.gather(*[_run_one(c, cond) for c, cond in tasks])\n        print(f\"  [{model_name}] {done} done, {errors} errors\")\n        total_done += done\n        total_errors += errors\n\n    print(f\"\\nPhase 1 summary: {total_done} done / {total_errors} errors / \"\n          f\"{total_skipped} skipped\")\n\n\n# ---------------------------------------------------------------------------\n# Phase 2: Cross-Judge Evaluation\n# ---------------------------------------------------------------------------\n\ndef _load_judged_ids(model_dir: Path) -> set[str]:\n    \"\"\"Return set of episode_ids already judged.\"\"\"\n    judged = set()\n    judgments_file = model_dir / \"judgments.jsonl\"\n    if judgments_file.exists():\n        with open(judgments_file) as f:\n            for line in f:\n                if line.strip():\n                    judged.add(json.loads(line)[\"episode_id\"])\n    return judged\n\n\nasync def run_phase2(\n    clauses: list[dict],\n    models: list[str],\n    concurrency: int,\n    resume: bool,\n):\n    \"\"\"Cross-judge all episodes (each model's episodes judged by the other).\"\"\"\n    clause_index = judge.build_clause_index(clauses)\n    total_done = 0\n    total_errors = 0\n    total_skipped = 0\n\n    for model_name in models:\n        ep_dir = EPISODES_DIR / model_name\n        if not ep_dir.exists():\n            print(f\"[{model_name}] No episodes found — run Phase 1 first.\")\n            continue\n\n        episodes = judge.load_episodes(ep_dir)\n        if not episodes:\n            print(f\"[{model_name}] No episode files found.\")\n            continue\n\n        judge_model = config.CROSS_JUDGE_MAP[model_name]\n        jdg_dir = JUDGMENTS_DIR / model_name\n        jdg_dir.mkdir(parents=True, exist_ok=True)\n\n        judged_ids = _load_judged_ids(jdg_dir) if resume else set()\n        pending = [ep for ep in episodes if ep[\"episode_id\"] not in judged_ids]\n        total_skipped += len(episodes) - len(pending)\n\n        if not pending:\n            print(f\"[{model_name}] All {len(episodes)} episodes already judged.\")\n            continue\n\n        print(f\"[{model_name}] Judging {len(pending)} episodes \"\n              f\"(judge={judge_model}, concurrency={concurrency})\")\n\n        semaphore = asyncio.Semaphore(concurrency)\n        output_file = jdg_dir / \"judgments.jsonl\"\n        lock = asyncio.Lock()\n        done = 0\n        errors = 0\n\n        async def _judge_one(episode, _model=model_name):\n            nonlocal done, errors\n            async with semaphore:\n                try:\n                    result = await judge.judge_episode(episode, clause_index)\n                    async with lock:\n                        with open(output_file, \"a\") as f:\n                            f.write(json.dumps(result, ensure_ascii=False) + \"\\n\")\n                        done += 1\n                        if done % 50 == 0:\n                            print(f\"  [{_model}] {done}/{len(pending)} judged\")\n                except Exception as e:\n                    async with lock:\n                        errors += 1\n                        with open(ERRORS_FILE, \"a\") as f:\n                            f.write(json.dumps({\n                                \"phase\": 2, \"model\": _model,\n                                \"episode_id\": episode.get(\"episode_id\", \"?\"),\n                                \"error\": str(e),\n                                \"timestamp\": time.time(),\n                            }, ensure_ascii=False) + \"\\n\")\n\n        await asyncio.gather(*[_judge_one(ep) for ep in pending])\n        print(f\"  [{model_name}] {done} judged, {errors} errors\")\n        total_done += done\n        total_errors += errors\n\n    print(f\"\\nPhase 2 summary: {total_done} done / {total_errors} errors / \"\n          f\"{total_skipped} skipped\")\n\n\n# ---------------------------------------------------------------------------\n# Phase 3: Analysis\n# ---------------------------------------------------------------------------\n\ndef _load_all_judgments(models: list[str]) -> pd.DataFrame:\n    \"\"\"Load judgments from all model subdirectories into one DataFrame.\"\"\"\n    records = []\n    for model_name in models:\n        jdg_dir = JUDGMENTS_DIR / model_name\n        if not jdg_dir.exists():\n            continue\n        for jsonl_file in jdg_dir.glob(\"*.jsonl\"):\n            with open(jsonl_file) as f:\n                for line in f:\n                    if not line.strip():\n                        continue\n                    rec = json.loads(line)\n                    records.append({\n                        \"episode_id\": rec[\"episode_id\"],\n                        \"clause_id\": rec[\"clause_id\"],\n                        \"ambiguity_type\": rec[\"ambiguity_type\"],\n                        \"condition\": rec[\"condition\"],\n                        \"model\": rec[\"model\"],\n                        \"violation_level\": rec[\"judgment\"][\"violation_level\"],\n                        \"confidence\": rec[\"judgment\"][\"confidence\"],\n                        \"judge_model\": rec[\"judge_model\"],\n                    })\n    df = pd.DataFrame(records)\n    if df.empty:\n        return df\n    level_order = pd.CategoricalDtype(\n        categories=config.VIOLATION_LEVELS, ordered=True\n    )\n    df[\"violation_level\"] = df[\"violation_level\"].astype(level_order)\n    return df\n\n\ndef _binary_effect(df: pd.DataFrame) -> dict:\n    \"\"\"(a) Ambiguous vs unambiguous violation rates: global, per-type, per-model.\"\"\"\n    df = df.copy()\n    df[\"violated\"] = analyze.binarize_violations(df)\n\n    # Global\n    cond_rates = df.groupby(\"condition\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    amb_r = float(cond_rates.loc[\"ambiguous\", \"mean\"]) if \"ambiguous\" in cond_rates.index else float(\"nan\")\n    una_r = float(cond_rates.loc[\"unambiguous\", \"mean\"]) if \"unambiguous\" in cond_rates.index else float(\"nan\")\n    ct = pd.crosstab(df[\"condition\"], df[\"violated\"])\n    if ct.shape == (2, 2):\n        chi2, p, _, _ = stats.chi2_contingency(ct.values)\n    else:\n        chi2, p = float(\"nan\"), float(\"nan\")\n    glob = {\n        \"ambiguous_rate\": amb_r, \"unambiguous_rate\": una_r,\n        \"difference\": amb_r - una_r if not (np.isnan(amb_r) or np.isnan(una_r)) else None,\n        \"chi2\": float(chi2), \"p\": float(p),\n    }\n\n    # Per-type\n    per_type = {}\n    for atype, tdf in df.groupby(\"ambiguity_type\"):\n        tr = tdf.groupby(\"condition\")[\"violated\"].mean()\n        a, u = tr.get(\"ambiguous\", np.nan), tr.get(\"unambiguous\", np.nan)\n        ct_t = pd.crosstab(tdf[\"condition\"], tdf[\"violated\"])\n        fp = float(stats.fisher_exact(ct_t.values)[1]) if ct_t.shape == (2, 2) else float(\"nan\")\n        per_type[atype] = {\n            \"ambiguous_rate\": float(a), \"unambiguous_rate\": float(u),\n            \"difference\": float(a - u) if not (np.isnan(a) or np.isnan(u)) else None,\n            \"fisher_p\": fp,\n        }\n\n    # Per-model\n    per_model = {}\n    for mname, mdf in df.groupby(\"model\"):\n        mr = mdf.groupby(\"condition\")[\"violated\"].mean()\n        a, u = mr.get(\"ambiguous\", np.nan), mr.get(\"unambiguous\", np.nan)\n        ct_m = pd.crosstab(mdf[\"condition\"], mdf[\"violated\"])\n        fp = float(stats.fisher_exact(ct_m.values)[1]) if ct_m.shape == (2, 2) else float(\"nan\")\n        per_model[mname] = {\n            \"ambiguous_rate\": float(a), \"unambiguous_rate\": float(u),\n            \"difference\": float(a - u) if not (np.isnan(a) or np.isnan(u)) else None,\n            \"fisher_p\": fp,\n        }\n\n    return {\"global\": glob, \"per_type\": per_type, \"per_model\": per_model}\n\n\ndef _type_effect(df: pd.DataFrame) -> dict:\n    \"\"\"(b) 6-way chi-square across ambiguity types (ambiguous episodes only).\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    type_rates = amb.groupby(\"ambiguity_type\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    type_rates.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n\n    ct = pd.crosstab(amb[\"ambiguity_type\"], amb[\"violated\"])\n    if ct.shape[0] >= 2 and ct.shape[1] >= 2:\n        chi2, p, dof, _ = stats.chi2_contingency(ct.values)\n        v = analyze.cramers_v(ct.values)\n    else:\n        chi2, p, dof, v = float(\"nan\"), float(\"nan\"), 0, 0.0\n\n    return {\n        \"rates\": type_rates.to_dict(orient=\"index\"),\n        \"chi2\": float(chi2), \"p\": float(p), \"dof\": int(dof),\n        \"cramers_v\": float(v),\n    }\n\n\ndef _model_effect(df: pd.DataFrame) -> dict:\n    \"\"\"(c) Model comparison: gpt-5.4 vs gpt-4.1 violation rates.\"\"\"\n    df = df.copy()\n    df[\"violated\"] = analyze.binarize_violations(df)\n\n    model_rates = df.groupby(\"model\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    model_rates.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n\n    ct = pd.crosstab(df[\"model\"], df[\"violated\"])\n    if ct.shape == (2, 2):\n        chi2, p, _, _ = stats.chi2_contingency(ct.values)\n        v = analyze.cramers_v(ct.values)\n    else:\n        chi2, p, v = float(\"nan\"), float(\"nan\"), 0.0\n\n    # Ambiguous-only subset\n    amb = df[df[\"condition\"] == \"ambiguous\"]\n    amb_rates = amb.groupby(\"model\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n    amb_rates.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n    ct_a = pd.crosstab(amb[\"model\"], amb[\"violated\"])\n    if ct_a.shape == (2, 2):\n        chi2_a, p_a, _, _ = stats.chi2_contingency(ct_a.values)\n    else:\n        chi2_a, p_a = float(\"nan\"), float(\"nan\")\n\n    return {\n        \"overall\": model_rates.to_dict(orient=\"index\"),\n        \"overall_chi2\": float(chi2), \"overall_p\": float(p),\n        \"cramers_v\": float(v),\n        \"ambiguous_only\": amb_rates.to_dict(orient=\"index\"),\n        \"ambiguous_chi2\": float(chi2_a), \"ambiguous_p\": float(p_a),\n    }\n\n\ndef _interaction(df: pd.DataFrame) -> dict:\n    \"\"\"(d) Model x Type interaction (ambiguous episodes only).\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    per_model_rates = {}\n    per_model_chi2 = {}\n    rankings = {}\n\n    for mname, mdf in amb.groupby(\"model\"):\n        tr = mdf.groupby(\"ambiguity_type\")[\"violated\"].agg([\"mean\", \"sum\", \"count\"])\n        tr.columns = [\"violation_rate\", \"n_violations\", \"n_total\"]\n        per_model_rates[mname] = tr.to_dict(orient=\"index\")\n\n        ct = pd.crosstab(mdf[\"ambiguity_type\"], mdf[\"violated\"])\n        if ct.shape[0] >= 2 and ct.shape[1] >= 2:\n            chi2, p, dof, _ = stats.chi2_contingency(ct.values)\n            v = analyze.cramers_v(ct.values)\n        else:\n            chi2, p, dof, v = float(\"nan\"), float(\"nan\"), 0, 0.0\n        per_model_chi2[mname] = {\n            \"chi2\": float(chi2), \"p\": float(p),\n            \"dof\": int(dof), \"cramers_v\": float(v),\n        }\n\n        sorted_types = sorted(\n            per_model_rates[mname].items(),\n            key=lambda x: x[1][\"violation_rate\"], reverse=True,\n        )\n        rankings[mname] = [t[0] for t in sorted_types]\n\n    return {\n        \"per_model_type_rates\": per_model_rates,\n        \"per_model_chi2\": per_model_chi2,\n        \"type_rankings\": rankings,\n    }\n\n\ndef _print_full_report(binary: dict, type_eff: dict,\n                       model_eff: dict, interact: dict):\n    \"\"\"Print formatted analysis report to console.\"\"\"\n    print(\"\\n\" + \"=\" * 72)\n    print(\"FULL STUDY — STATISTICAL ANALYSIS REPORT\")\n    print(\"=\" * 72)\n\n    # (a) Binary effect\n    print(\"\\n-- (a) Binary Effect: Ambiguous vs Unambiguous --\\n\")\n    g = binary[\"global\"]\n    diff_str = f\"{g['difference']:+.1%}\" if g[\"difference\"] is not None else \"N/A\"\n    print(f\"  Global: amb={g['ambiguous_rate']:.1%}  unamb={g['unambiguous_rate']:.1%}\"\n          f\"  D={diff_str}  chi2 p={g['p']:.4f}\")\n\n    print(f\"\\n  {'Type':<25} {'Amb':>7} {'Unamb':>7} {'D':>7} {'Fisher p':>9}\")\n    print(f\"  {'-'*25} {'-'*7} {'-'*7} {'-'*7} {'-'*9}\")\n    for atype in sorted(binary[\"per_type\"]):\n        r = binary[\"per_type\"][atype]\n        d = r[\"difference\"]\n        if d is not None:\n            print(f\"  {atype:<25} {r['ambiguous_rate']:>6.1%} {r['unambiguous_rate']:>6.1%}\"\n                  f\" {d:>+6.1%} {r['fisher_p']:>9.4f}\")\n        else:\n            print(f\"  {atype:<25}  insufficient data\")\n\n    print(f\"\\n  {'Model':<15} {'Amb':>7} {'Unamb':>7} {'D':>7} {'Fisher p':>9}\")\n    print(f\"  {'-'*15} {'-'*7} {'-'*7} {'-'*7} {'-'*9}\")\n    for mname in sorted(binary[\"per_model\"]):\n        r = binary[\"per_model\"][mname]\n        d = r[\"difference\"]\n        if d is not None:\n            print(f\"  {mname:<15} {r['ambiguous_rate']:>6.1%} {r['unambiguous_rate']:>6.1%}\"\n                  f\" {d:>+6.1%} {r['fisher_p']:>9.4f}\")\n\n    # (b) Type effect\n    print(\"\\n-- (b) Type Effect: 6-way chi-square (ambiguous only) --\\n\")\n    rates = type_eff.get(\"rates\", {})\n    print(f\"  {'Type':<25} {'Rate':>10} {'N':>6}\")\n    print(f\"  {'-'*25} {'-'*10} {'-'*6}\")\n    for atype in sorted(rates):\n        r = rates[atype]\n        print(f\"  {atype:<25} {r['violation_rate']:>9.1%} {r['n_total']:>6.0f}\")\n    print(f\"\\n  chi2={type_eff['chi2']:.3f}  p={type_eff['p']:.4f}\"\n          f\"  dof={type_eff['dof']}  Cramer's V={type_eff['cramers_v']:.3f}\")\n\n    # (c) Model effect\n    print(\"\\n-- (c) Model Effect --\\n\")\n    ov = model_eff.get(\"overall\", {})\n    print(f\"  {'Model':<15} {'Rate':>8} {'N_viol':>7} {'N':>6}\")\n    print(f\"  {'-'*15} {'-'*8} {'-'*7} {'-'*6}\")\n    for mname in sorted(ov):\n        r = ov[mname]\n        print(f\"  {mname:<15} {r['violation_rate']:>7.1%} {r['n_violations']:>7.0f}\"\n              f\" {r['n_total']:>6.0f}\")\n    print(f\"\\n  Overall: chi2 p={model_eff['overall_p']:.4f}  V={model_eff['cramers_v']:.3f}\")\n    print(f\"  Ambiguous-only: chi2 p={model_eff['ambiguous_p']:.4f}\")\n\n    # (d) Interaction\n    print(\"\\n-- (d) Model x Type Interaction --\\n\")\n    for mname in sorted(interact.get(\"per_model_chi2\", {})):\n        c = interact[\"per_model_chi2\"][mname]\n        print(f\"  [{mname}] type chi2={c['chi2']:.3f}  p={c['p']:.4f}\"\n              f\"  V={c['cramers_v']:.3f}\")\n    print()\n    for mname in sorted(interact.get(\"type_rankings\", {})):\n        ranking = interact[\"type_rankings\"][mname]\n        print(f\"  {mname}: {' > '.join(ranking)}\")\n\n    print(\"\\n\" + \"=\" * 72)\n\n\n# ---------------------------------------------------------------------------\n# Phase 3 Extended: Dream reviewer analyses (A3, A4, A10 + bootstrap/McNemar/Fleiss)\n# ---------------------------------------------------------------------------\n\ndef run_power_analysis(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Dream A3: Power analysis for C2 (type uniformity) and C3 (per-type).\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    types = sorted(amb[\"ambiguity_type\"].unique())\n    n_types = len(types)\n    alpha = 0.05\n    target_power = 0.80\n\n    def _find_mde(n_total, df_val):\n        crit = stats.chi2.ppf(1 - alpha, df_val)\n        lo, hi = 1e-4, 1.0\n        for _ in range(200):\n            mid = (lo + hi) / 2\n            pwr = 1 - stats.ncx2.cdf(crit, df_val, n_total * mid ** 2)\n            if pwr < target_power:\n                lo = mid\n            else:\n                hi = mid\n        return (lo + hi) / 2\n\n    def _compute_power(w, n_total, df_val):\n        crit = stats.chi2.ppf(1 - alpha, df_val)\n        return float(1 - stats.ncx2.cdf(crit, df_val, n_total * w ** 2))\n\n    c2_n_per_type = 200\n    c2_n_total = c2_n_per_type * n_types\n    c2_df = max(n_types - 1, 1)\n    c2_mde = _find_mde(c2_n_total, c2_df)\n\n    c3_n = 200\n    c3_df = 1\n    c3_mde = _find_mde(c3_n, c3_df)\n\n    ct = pd.crosstab(amb[\"ambiguity_type\"], amb[\"violated\"])\n    observed_v = (\n        analyze.cramers_v(ct.values)\n        if ct.shape[0] >= 2 and ct.shape[1] >= 2\n        else 0.0\n    )\n\n    actual_n = len(amb)\n    mde_actual = _find_mde(actual_n, c2_df)\n    power_at_observed = (\n        _compute_power(observed_v, actual_n, c2_df) if observed_v > 0 else 0.0\n    )\n\n    underpowered = observed_v < 0.20 and c2_mde > observed_v\n\n    result = {\n        \"c2_type_uniformity\": {\n            \"design_N_per_type\": c2_n_per_type,\n            \"design_N_total\": c2_n_total,\n            \"n_types\": n_types,\n            \"df\": c2_df,\n            \"alpha\": alpha,\n            \"target_power\": target_power,\n            \"mde_cramers_v\": round(c2_mde, 4),\n        },\n        \"c3_per_type_comparison\": {\n            \"design_N\": c3_n,\n            \"df\": c3_df,\n            \"alpha\": alpha,\n            \"target_power\": target_power,\n            \"mde_cramers_v\": round(c3_mde, 4),\n        },\n        \"observed_cramers_v\": round(float(observed_v), 4),\n        \"actual_sample\": {\n            \"N_total\": actual_n,\n            \"per_type\": {\n                t: int(v)\n                for t, v in amb.groupby(\"ambiguity_type\").size().items()\n            },\n            \"mde_cramers_v\": round(mde_actual, 4),\n            \"power_at_observed\": round(power_at_observed, 4),\n        },\n        \"underpowered_warning\": underpowered,\n    }\n\n    out = ANALYSIS_DIR / \"power_analysis.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_tost_equivalence(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Dream A4: TOST equivalence test for C2 type uniformity.\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        return {\"error\": \"No ambiguous episodes\"}\n    amb[\"violated\"] = analyze.binarize_violations(amb)\n\n    types = sorted(amb[\"ambiguity_type\"].unique())\n    margins = [0.15, 0.10]\n\n    results_by_margin = {}\n    for margin in margins:\n        pairwise = []\n        for i in range(len(types)):\n            for j in range(i + 1, len(types)):\n                t1, t2 = types[i], types[j]\n                d1 = amb[amb[\"ambiguity_type\"] == t1][\"violated\"]\n                d2 = amb[amb[\"ambiguity_type\"] == t2][\"violated\"]\n                p1, n1 = float(d1.mean()), len(d1)\n                p2, n2 = float(d2.mean()), len(d2)\n                diff = p1 - p2\n\n                if n1 > 0 and n2 > 0:\n                    se = np.sqrt(\n                        p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2\n                    )\n                else:\n                    se = float(\"inf\")\n\n                if se > 0 and np.isfinite(se):\n                    z_lower = (diff + margin) / se\n                    p_lower = float(1 - stats.norm.cdf(z_lower))\n                    z_upper = (diff - margin) / se\n                    p_upper = float(stats.norm.cdf(z_upper))\n                    tost_p = max(p_lower, p_upper)\n                    equivalent = tost_p < 0.05\n                else:\n                    z_lower = z_upper = tost_p = float(\"nan\")\n                    p_lower = p_upper = float(\"nan\")\n                    equivalent = False\n\n                pairwise.append({\n                    \"type_1\": t1,\n                    \"type_2\": t2,\n                    \"rate_1\": round(p1, 4),\n                    \"rate_2\": round(p2, 4),\n                    \"difference\": round(diff, 4),\n                    \"se\": round(float(se), 4),\n                    \"z_lower\": round(float(z_lower), 4),\n                    \"p_lower\": round(float(p_lower), 4),\n                    \"z_upper\": round(float(z_upper), 4),\n                    \"p_upper\": round(float(p_upper), 4),\n                    \"tost_p\": round(float(tost_p), 4),\n                    \"equivalent\": equivalent,\n                })\n\n        all_equiv = all(p[\"equivalent\"] for p in pairwise) if pairwise else False\n        results_by_margin[f\"margin_{int(margin * 100)}pp\"] = {\n            \"margin\": margin,\n            \"pairwise\": pairwise,\n            \"all_pairs_equivalent\": all_equiv,\n        }\n\n    result = {\n        \"test\": \"TOST two one-sided z-tests for proportions\",\n        \"margin_justification\": (\n            \"15pp = practical significance threshold for policy remediation \"\n            \"cost; 10pp = stricter robustness check\"\n        ),\n        **results_by_margin,\n    }\n\n    out = ANALYSIS_DIR / \"tost_equivalence.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef _bca_ci(g1: np.ndarray, g2: np.ndarray, rng, B: int = 10000,\n            alpha: float = 0.05) -> dict:\n    \"\"\"BCa bootstrap CI for difference in means (g1 - g2).\"\"\"\n    n1, n2 = len(g1), len(g2)\n    if n1 == 0 or n2 == 0:\n        return {\"observed_diff\": None, \"ci_lower\": None, \"ci_upper\": None}\n\n    observed = float(g1.mean() - g2.mean())\n\n    idx1 = rng.integers(0, n1, size=(B, n1))\n    idx2 = rng.integers(0, n2, size=(B, n2))\n    boot_stats = g1[idx1].mean(axis=1) - g2[idx2].mean(axis=1)\n\n    prop_below = np.mean(boot_stats < observed)\n    prop_below = np.clip(prop_below, 1 / (B + 1), B / (B + 1))\n    z0 = stats.norm.ppf(prop_below)\n\n    if n1 >= 2 and n2 >= 2:\n        jack = np.empty(n1 + n2)\n        g1_sum, g2_mean = g1.sum(), g2.mean()\n        g1_mean, g2_sum = g1.mean(), g2.sum()\n        for i in range(n1):\n            jack[i] = (g1_sum - g1[i]) / (n1 - 1) - g2_mean\n        for j in range(n2):\n            jack[n1 + j] = g1_mean - (g2_sum - g2[j]) / (n2 - 1)\n        jm = jack.mean()\n        d = jm - jack\n        denom = 6 * np.sum(d ** 2) ** 1.5\n        a = float(np.sum(d ** 3) / denom) if denom > 0 else 0.0\n    else:\n        a = 0.0\n\n    z_lo = stats.norm.ppf(alpha / 2)\n    z_hi = stats.norm.ppf(1 - alpha / 2)\n\n    def _adj(z):\n        num = z0 + z\n        den = 1 - a * num\n        if abs(den) < 1e-12:\n            return 0.5\n        return stats.norm.cdf(z0 + num / den)\n\n    a1 = np.clip(_adj(z_lo), 0.5 / B, 1 - 0.5 / B)\n    a2 = np.clip(_adj(z_hi), 0.5 / B, 1 - 0.5 / B)\n\n    return {\n        \"observed_diff\": round(observed, 4),\n        \"ci_lower\": round(float(np.percentile(boot_stats, 100 * a1)), 4),\n        \"ci_upper\": round(float(np.percentile(boot_stats, 100 * a2)), 4),\n        \"z0\": round(float(z0), 4),\n        \"acceleration\": round(a, 6),\n    }\n\n\ndef run_bootstrap_ci(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"BCa bootstrap 95% CIs for all pairwise comparisons.\"\"\"\n    B = 10000\n    rng = np.random.default_rng(42)\n\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc).astype(float)\n\n    results: dict = {\"n_resamples\": B}\n\n    # Global ambig vs unambig\n    amb_v = dfc.loc[dfc[\"condition\"] == \"ambiguous\", \"violated\"].values\n    una_v = dfc.loc[dfc[\"condition\"] == \"unambiguous\", \"violated\"].values\n    results[\"ambig_vs_unambig_global\"] = _bca_ci(amb_v, una_v, rng, B)\n\n    # Per-type ambig vs unambig\n    per_type = {}\n    for atype in sorted(dfc[\"ambiguity_type\"].unique()):\n        tdf = dfc[dfc[\"ambiguity_type\"] == atype]\n        a = tdf.loc[tdf[\"condition\"] == \"ambiguous\", \"violated\"].values\n        u = tdf.loc[tdf[\"condition\"] == \"unambiguous\", \"violated\"].values\n        per_type[atype] = _bca_ci(a, u, rng, B)\n    results[\"ambig_vs_unambig_per_type\"] = per_type\n\n    # Type pairs (ambiguous only)\n    amb_df = dfc[dfc[\"condition\"] == \"ambiguous\"]\n    types = sorted(amb_df[\"ambiguity_type\"].unique())\n    type_pairs = {}\n    for i in range(len(types)):\n        for j in range(i + 1, len(types)):\n            t1, t2 = types[i], types[j]\n            v1 = amb_df.loc[amb_df[\"ambiguity_type\"] == t1, \"violated\"].values\n            v2 = amb_df.loc[amb_df[\"ambiguity_type\"] == t2, \"violated\"].values\n            type_pairs[f\"{t1}_vs_{t2}\"] = _bca_ci(v1, v2, rng, B)\n    results[\"type_pairs_ambiguous\"] = type_pairs\n\n    # Model pairs\n    models = sorted(dfc[\"model\"].unique())\n    model_pairs = {}\n    for i in range(len(models)):\n        for j in range(i + 1, len(models)):\n            m1, m2 = models[i], models[j]\n            v1 = dfc.loc[dfc[\"model\"] == m1, \"violated\"].values\n            v2 = dfc.loc[dfc[\"model\"] == m2, \"violated\"].values\n            model_pairs[f\"{m1}_vs_{m2}\"] = _bca_ci(v1, v2, rng, B)\n    results[\"model_pairs\"] = model_pairs\n\n    out = ANALYSIS_DIR / \"bootstrap_ci.json\"\n    with open(out, \"w\") as f:\n        json.dump(results, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return results\n\n\ndef run_mcnemar_matched(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Matched-pair McNemar test for C1 (binary effect).\"\"\"\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n\n    amb = dfc.loc[dfc[\"condition\"] == \"ambiguous\", [\"clause_id\", \"model\", \"violated\"]]\n    una = dfc.loc[dfc[\"condition\"] == \"unambiguous\", [\"clause_id\", \"model\", \"violated\"]]\n    merged = pd.merge(amb, una, on=[\"clause_id\", \"model\"], suffixes=(\"_amb\", \"_una\"))\n\n    if merged.empty:\n        return {\"error\": \"No matched pairs found\"}\n\n    merged[\"amb_only\"] = merged[\"violated_amb\"] & ~merged[\"violated_una\"]\n    merged[\"una_only\"] = ~merged[\"violated_amb\"] & merged[\"violated_una\"]\n    merged[\"both\"] = merged[\"violated_amb\"] & merged[\"violated_una\"]\n    merged[\"neither\"] = ~merged[\"violated_amb\"] & ~merged[\"violated_una\"]\n\n    b_total = int(merged[\"amb_only\"].sum())\n    c_total = int(merged[\"una_only\"].sum())\n    n_pairs = len(merged)\n    n_disc = b_total + c_total\n\n    # Overall McNemar\n    if n_disc > 0:\n        if n_disc >= 25:\n            mcn_chi2 = float((abs(b_total - c_total) - 1) ** 2 / n_disc)\n            mcn_p = float(1 - stats.chi2.cdf(mcn_chi2, 1))\n            method = \"chi-square (continuity corrected)\"\n        else:\n            mcn_p = float(stats.binomtest(b_total, n_disc, 0.5).pvalue)\n            mcn_chi2 = None\n            method = \"exact binomial\"\n    else:\n        mcn_chi2 = 0.0\n        mcn_p = 1.0\n        method = \"no discordant pairs\"\n\n    # Odds ratio b/c with Wald 95% CI\n    if b_total > 0 and c_total > 0:\n        or_val = b_total / c_total\n        log_or = np.log(or_val)\n        se_log = np.sqrt(1 / b_total + 1 / c_total)\n        or_lo = float(np.exp(log_or - 1.96 * se_log))\n        or_hi = float(np.exp(log_or + 1.96 * se_log))\n    elif c_total == 0 and b_total > 0:\n        or_val, or_lo, or_hi = float(\"inf\"), float(\"nan\"), float(\"nan\")\n    elif b_total == 0 and c_total > 0:\n        or_val, or_lo, or_hi = 0.0, float(\"nan\"), float(\"nan\")\n    else:\n        or_val = or_lo = or_hi = float(\"nan\")\n\n    # Per-model McNemar\n    per_model = {}\n    for model_name, mdf in merged.groupby(\"model\"):\n        b_m = int(mdf[\"amb_only\"].sum())\n        c_m = int(mdf[\"una_only\"].sum())\n        disc_m = b_m + c_m\n        if disc_m > 0:\n            p_m = float(stats.binomtest(b_m, disc_m, 0.5).pvalue)\n        else:\n            p_m = 1.0\n        per_model[model_name] = {\n            \"n_pairs\": len(mdf),\n            \"b_amb_only\": b_m,\n            \"c_una_only\": c_m,\n            \"mcnemar_p\": round(p_m, 6),\n        }\n\n    # Mantel-Haenszel OR stratified by ambiguity_type\n    mh_strata = []\n    for atype, sdf in merged.groupby(\n        merged[\"clause_id\"].map(\n            lambda cid: dfc.loc[dfc[\"clause_id\"] == cid, \"ambiguity_type\"].iloc[0]\n            if cid in dfc[\"clause_id\"].values else \"unknown\"\n        )\n    ):\n        b_s = int(sdf[\"amb_only\"].sum())\n        c_s = int(sdf[\"una_only\"].sum())\n        a_s = int(sdf[\"both\"].sum())\n        d_s = int(sdf[\"neither\"].sum())\n        n_s = len(sdf)\n        mh_strata.append({\n            \"stratum\": atype, \"n\": n_s,\n            \"a\": a_s, \"b\": b_s, \"c\": c_s, \"d\": d_s,\n        })\n\n    # Haldane 0.5 correction for strata with zero cells\n    mh_num = 0.0\n    mh_den = 0.0\n    for s in mh_strata:\n        if s[\"n\"] == 0:\n            continue\n        a, b, c, d, n = s[\"a\"], s[\"b\"], s[\"c\"], s[\"d\"], s[\"n\"]\n        if a == 0 or b == 0 or c == 0 or d == 0:\n            a, b, c, d, n = a + 0.5, b + 0.5, c + 0.5, d + 0.5, n + 2\n        mh_num += b * d / n\n        mh_den += c * a / n\n    mh_or = mh_num / mh_den if mh_den > 0 else float(\"inf\") if mh_num > 0 else float(\"nan\")\n\n    def _safe_round(v, n=4):\n        if isinstance(v, float) and (np.isnan(v) or np.isinf(v)):\n            return str(v)\n        return round(float(v), n)\n\n    result = {\n        \"n_pairs\": n_pairs,\n        \"n_concordant\": int(merged[\"both\"].sum() + merged[\"neither\"].sum()),\n        \"n_discordant\": n_disc,\n        \"b_amb_only\": b_total,\n        \"c_una_only\": c_total,\n        \"mcnemar\": {\n            \"method\": method,\n            \"statistic\": _safe_round(mcn_chi2) if mcn_chi2 is not None else None,\n            \"p\": round(mcn_p, 6),\n        },\n        \"odds_ratio\": {\n            \"or\": _safe_round(or_val),\n            \"ci_95_lower\": _safe_round(or_lo),\n            \"ci_95_upper\": _safe_round(or_hi),\n        },\n        \"mantel_haenszel\": {\n            \"or\": _safe_round(mh_or),\n            \"correction\": \"haldane_0.5\",\n            \"note\": \"Primary OR=44.8 (non-stratified); MH OR is supplementary\",\n            \"strata\": mh_strata,\n        },\n        \"per_model\": per_model,\n    }\n\n    out = ANALYSIS_DIR / \"mcnemar_matched.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_information_delta(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Dream A10: Per-type information (token count) delta + logistic regression.\"\"\"\n    import statsmodels.api as sm\n\n    clause_map = {}\n    for c in clauses:\n        cid = c[\"clause_id\"]\n        amb_tok = len(c.get(\"ambiguous_clause\", \"\").split())\n        una_tok = len(c.get(\"unambiguous_clause\", \"\").split())\n        clause_map[cid] = {\n            \"ambiguity_type\": c.get(\"ambiguity_type\", \"unknown\"),\n            \"amb_tokens\": amb_tok,\n            \"una_tokens\": una_tok,\n            \"token_delta\": una_tok - amb_tok,\n        }\n\n    # Per-type token delta stats\n    type_groups: dict[str, list[int]] = {}\n    for info in clause_map.values():\n        atype = info[\"ambiguity_type\"]\n        type_groups.setdefault(atype, []).append(info[\"token_delta\"])\n\n    type_deltas = {}\n    for atype, deltas in sorted(type_groups.items()):\n        arr = np.array(deltas)\n        type_deltas[atype] = {\n            \"mean\": round(float(arr.mean()), 2),\n            \"median\": round(float(np.median(arr)), 2),\n            \"std\": round(float(arr.std(ddof=1)), 2) if len(arr) > 1 else 0.0,\n            \"min\": int(arr.min()),\n            \"max\": int(arr.max()),\n            \"n_clauses\": len(arr),\n        }\n\n    # Merge into judgments\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc).astype(int)\n    dfc[\"token_delta\"] = dfc[\"clause_id\"].map(\n        lambda cid: clause_map.get(cid, {}).get(\"token_delta\", 0)\n    )\n    dfc[\"condition_amb\"] = (dfc[\"condition\"] == \"ambiguous\").astype(int)\n\n    # Logistic regression: violation ~ condition + type + token_delta + model\n    type_dummies = pd.get_dummies(\n        dfc[\"ambiguity_type\"], prefix=\"type\", drop_first=True, dtype=float\n    )\n    model_dummies = pd.get_dummies(\n        dfc[\"model\"], prefix=\"model\", drop_first=True, dtype=float\n    )\n    X = pd.concat(\n        [dfc[[\"condition_amb\", \"token_delta\"]].astype(float), type_dummies, model_dummies],\n        axis=1,\n    )\n    X = sm.add_constant(X)\n    y = dfc[\"violated\"]\n\n    logit_result: dict = {}\n    try:\n        fit = sm.Logit(y, X).fit(disp=0, maxiter=100)\n        coefficients = {}\n        ci = fit.conf_int()\n        for var in fit.params.index:\n            coefficients[var] = {\n                \"coef\": round(float(fit.params[var]), 4),\n                \"se\": round(float(fit.bse[var]), 4),\n                \"z\": round(float(fit.tvalues[var]), 4),\n                \"p\": round(float(fit.pvalues[var]), 6),\n                \"ci_lower\": round(float(ci.loc[var, 0]), 4),\n                \"ci_upper\": round(float(ci.loc[var, 1]), 4),\n            }\n        logit_result = {\n            \"converged\": bool(fit.mle_retvals.get(\"converged\", False)),\n            \"n_obs\": int(fit.nobs),\n            \"pseudo_r2\": round(float(fit.prsquared), 4),\n            \"llr_p\": round(float(fit.llr_pvalue), 6),\n            \"coefficients\": coefficients,\n        }\n    except Exception as e:\n        logit_result = {\"error\": str(e)}\n\n    result = {\n        \"per_type_token_delta\": type_deltas,\n        \"logistic_regression\": logit_result,\n    }\n\n    out = ANALYSIS_DIR / \"information_delta.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_fleiss_kappa(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"Fleiss' kappa for inter-model agreement on violation judgment.\"\"\"\n    amb = df[df[\"condition\"] == \"ambiguous\"].copy()\n    if amb.empty:\n        result = {\"error\": \"No ambiguous episodes\"}\n        out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n        with open(out, \"w\") as f:\n            json.dump(result, f, indent=2)\n        print(f\"  -> {out.name}\")\n        return result\n\n    amb[\"violated\"] = analyze.binarize_violations(amb).astype(int)\n    models = sorted(amb[\"model\"].unique())\n    n_models = len(models)\n\n    if n_models < 2:\n        result = {\"error\": f\"Need >= 2 models, found {n_models}\", \"models\": models}\n        out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n        with open(out, \"w\") as f:\n            json.dump(result, f, indent=2)\n        print(f\"  -> {out.name}\")\n        return result\n\n    ratings = amb.groupby(\"clause_id\").agg(\n        n_violated=(\"violated\", \"sum\"),\n        n_raters=(\"violated\", \"count\"),\n    ).reset_index()\n    ratings = ratings[ratings[\"n_raters\"] >= 2]\n\n    if ratings.empty:\n        result = {\"error\": \"No clauses with >= 2 model ratings\"}\n        out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n        with open(out, \"w\") as f:\n            json.dump(result, f, indent=2)\n        print(f\"  -> {out.name}\")\n        return result\n\n    ratings[\"n_not\"] = ratings[\"n_raters\"] - ratings[\"n_violated\"]\n    N = len(ratings)\n    mat = ratings[[\"n_violated\", \"n_not\"]].values  # (N, 2)\n    n_arr = ratings[\"n_raters\"].values\n\n    # Per-subject agreement P_i\n    P_i = np.zeros(N)\n    for i in range(N):\n        ni = n_arr[i]\n        if ni >= 2:\n            P_i[i] = (np.sum(mat[i] ** 2) - ni) / (ni * (ni - 1))\n    P_bar = float(P_i.mean())\n\n    total_ratings = n_arr.sum()\n    p_j = mat.sum(axis=0) / total_ratings  # (2,)\n    P_e = float(np.sum(p_j ** 2))\n\n    kappa = (P_bar - P_e) / (1 - P_e) if P_e < 1.0 else 0.0\n\n    # SE (large sample, Fleiss 1971)\n    n_fixed = int(np.median(n_arr))\n    if N > 1 and P_e < 1.0 and n_fixed >= 2:\n        inner = (\n            P_e\n            - (2 * n_fixed - 3) * P_e ** 2\n            + 2 * (n_fixed - 2) * np.sum(p_j ** 3)\n        )\n        se = float(np.sqrt(2 / (N * n_fixed * (n_fixed - 1))) * np.sqrt(\n            abs(inner) / (1 - P_e) ** 2\n        ))\n        z_val = kappa / se if se > 0 else float(\"nan\")\n        p_val = float(2 * (1 - stats.norm.cdf(abs(z_val)))) if np.isfinite(z_val) else float(\"nan\")\n    else:\n        se = z_val = p_val = float(\"nan\")\n\n    if kappa < 0:\n        interp = \"less than chance agreement\"\n    elif kappa < 0.20:\n        interp = \"slight agreement\"\n    elif kappa < 0.40:\n        interp = \"fair agreement\"\n    elif kappa < 0.60:\n        interp = \"moderate agreement\"\n    elif kappa < 0.80:\n        interp = \"substantial agreement\"\n    else:\n        interp = \"almost perfect agreement\"\n\n    result = {\n        \"n_clauses\": N,\n        \"n_models\": n_models,\n        \"models\": models,\n        \"n_raters_per_clause\": {\n            \"min\": int(n_arr.min()),\n            \"max\": int(n_arr.max()),\n            \"mean\": round(float(n_arr.mean()), 1),\n        },\n        \"category_proportions\": {\n            \"violated\": round(float(p_j[0]), 4),\n            \"not_violated\": round(float(p_j[1]), 4),\n        },\n        \"fleiss_kappa\": round(float(kappa), 4),\n        \"se\": round(float(se), 4) if np.isfinite(se) else None,\n        \"z\": round(float(z_val), 4) if np.isfinite(z_val) else None,\n        \"p\": round(float(p_val), 6) if np.isfinite(p_val) else None,\n        \"interpretation\": interp,\n    }\n\n    out = ANALYSIS_DIR / \"fleiss_kappa.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_layer_effect_test(df: pd.DataFrame, clauses: list[dict]) -> dict:\n    \"\"\"C3: Formal test of specification-layer vs linguistic-layer violation rates.\"\"\"\n    SPEC_TYPES = {\"incompleteness\", \"conditional_precedence\", \"authorization_scope\"}\n    LING_TYPES = {\"scopal\", \"lexical\", \"coreferential\"}\n\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n\n    # Filter to ambiguous condition only\n    amb = dfc[dfc[\"condition\"] == \"ambiguous\"].copy()\n    amb[\"layer\"] = amb[\"ambiguity_type\"].map(\n        lambda t: \"specification\" if t in SPEC_TYPES else \"linguistic\" if t in LING_TYPES else \"unknown\"\n    )\n    amb = amb[amb[\"layer\"] != \"unknown\"]\n\n    spec = amb[amb[\"layer\"] == \"specification\"]\n    ling = amb[amb[\"layer\"] == \"linguistic\"]\n\n    spec_n = len(spec)\n    spec_v = int(spec[\"violated\"].sum())\n    ling_n = len(ling)\n    ling_v = int(ling[\"violated\"].sum())\n\n    spec_rate = spec_v / spec_n if spec_n > 0 else 0\n    ling_rate = ling_v / ling_n if ling_n > 0 else 0\n    delta_pp = (spec_rate - ling_rate) * 100\n\n    from scipy.stats import chi2_contingency\n    table = np.array([\n        [spec_v, spec_n - spec_v],\n        [ling_v, ling_n - ling_v],\n    ])\n    chi2, p_val, dof, expected = chi2_contingency(table, correction=False)\n\n    n_total = spec_n + ling_n\n    cramers_v = np.sqrt(chi2 / n_total) if n_total > 0 else 0\n\n    a, b = spec_v, spec_n - spec_v\n    c, d = ling_v, ling_n - ling_v\n    if b > 0 and c > 0 and d > 0 and a > 0:\n        or_val = (a * d) / (b * c)\n        log_or = np.log(or_val)\n        se_log = np.sqrt(1/a + 1/b + 1/c + 1/d)\n        or_lo = float(np.exp(log_or - 1.96 * se_log))\n        or_hi = float(np.exp(log_or + 1.96 * se_log))\n    else:\n        or_val = or_lo = or_hi = float(\"nan\")\n\n    np.random.seed(42)\n    n_boot = 10000\n    spec_arr = spec[\"violated\"].values.astype(float)\n    ling_arr = ling[\"violated\"].values.astype(float)\n    boot_deltas = []\n    for _ in range(n_boot):\n        s_idx = np.random.randint(0, len(spec_arr), len(spec_arr))\n        l_idx = np.random.randint(0, len(ling_arr), len(ling_arr))\n        boot_deltas.append((spec_arr[s_idx].mean() - ling_arr[l_idx].mean()) * 100)\n    boot_deltas = np.array(boot_deltas)\n    ci_lo = float(np.percentile(boot_deltas, 2.5))\n    ci_hi = float(np.percentile(boot_deltas, 97.5))\n\n    per_type = {}\n    for atype in list(SPEC_TYPES) + list(LING_TYPES):\n        subset = amb[amb[\"ambiguity_type\"] == atype]\n        if len(subset) > 0:\n            rate = float(subset[\"violated\"].mean())\n            per_type[atype] = {\n                \"n\": len(subset),\n                \"violations\": int(subset[\"violated\"].sum()),\n                \"rate\": round(rate * 100, 2),\n                \"layer\": \"specification\" if atype in SPEC_TYPES else \"linguistic\",\n            }\n\n    result = {\n        \"test\": \"layer_effect (C3)\",\n        \"specification_layer\": {\n            \"types\": sorted(SPEC_TYPES),\n            \"n\": spec_n,\n            \"violations\": spec_v,\n            \"rate_pct\": round(spec_rate * 100, 2),\n        },\n        \"linguistic_layer\": {\n            \"types\": sorted(LING_TYPES),\n            \"n\": ling_n,\n            \"violations\": ling_v,\n            \"rate_pct\": round(ling_rate * 100, 2),\n        },\n        \"delta_pp\": round(delta_pp, 2),\n        \"bootstrap_ci_95\": [round(ci_lo, 2), round(ci_hi, 2)],\n        \"chi_squared\": {\n            \"statistic\": round(float(chi2), 4),\n            \"df\": int(dof),\n            \"p\": round(float(p_val), 6),\n        },\n        \"cramers_v\": round(float(cramers_v), 4),\n        \"odds_ratio\": {\n            \"or\": round(float(or_val), 4) if np.isfinite(or_val) else str(or_val),\n            \"ci_95\": [round(or_lo, 4) if np.isfinite(or_lo) else str(or_lo),\n                       round(or_hi, 4) if np.isfinite(or_hi) else str(or_hi)],\n        },\n        \"per_type_detail\": per_type,\n    }\n\n    out = ANALYSIS_DIR / \"layer_effect_test.json\"\n    with open(out, \"w\") as f:\n        json.dump(result, f, indent=2, default=str)\n    print(f\"  -> {out.name}\")\n    return result\n\n\ndef run_phase3(models: list[str]):\n    \"\"\"Load all judgments and run the full analysis suite.\"\"\"\n    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)\n\n    df = _load_all_judgments(models)\n    if df.empty:\n        print(\"No judgments found. Run Phase 2 first.\")\n        return\n\n    print(f\"Loaded {len(df)} judgments ({df['model'].nunique()} models, \"\n          f\"{df['ambiguity_type'].nunique()} types)\")\n\n    binary = _binary_effect(df)\n    type_eff = _type_effect(df)\n    model_eff = _model_effect(df)\n    interact = _interaction(df)\n\n    # JSON report\n    report = {\n        \"binary_effect\": binary,\n        \"type_effect\": type_eff,\n        \"model_effect\": model_eff,\n        \"model_type_interaction\": interact,\n        \"n_judgments\": len(df),\n    }\n    with open(ANALYSIS_DIR / \"full_statistics.json\", \"w\") as f:\n        json.dump(report, f, indent=2, default=str)\n\n    # Per-clause summary CSV\n    summary = analyze.per_clause_summary(df)\n    summary.to_csv(ANALYSIS_DIR / \"per_clause_summary.csv\", index=False)\n\n    # Aggregated rates CSV\n    dfc = df.copy()\n    dfc[\"violated\"] = analyze.binarize_violations(dfc)\n    agg = dfc.groupby(\n        [\"model\", \"ambiguity_type\", \"condition\"]\n    )[\"violated\"].agg(\n        violation_rate=\"mean\", n_violations=\"sum\", n_total=\"count\",\n    ).reset_index()\n    agg.to_csv(ANALYSIS_DIR / \"aggregated_rates.csv\", index=False)\n\n    _print_full_report(binary, type_eff, model_eff, interact)\n\n    # Extended analyses (Dream reviewer)\n    clauses_path = config.ARTIFACTS_DIR / \"clause_templates_full.json\"\n    if clauses_path.exists():\n        with open(clauses_path) as f:\n            raw = json.load(f)\n        clauses_data = raw if isinstance(raw, list) else raw.get(\"clauses\", raw)\n    else:\n        clauses_data = []\n\n    print(\"\\n-- Extended analyses (Dream reviewer) --\\n\")\n    run_power_analysis(df, clauses_data)\n    run_tost_equivalence(df, clauses_data)\n    run_bootstrap_ci(df, clauses_data)\n    run_mcnemar_matched(df, clauses_data)\n    if clauses_data:\n        run_information_delta(df, clauses_data)\n    else:\n        print(\"  (skipped information_delta -- no clauses file)\")\n    run_fleiss_kappa(df, clauses_data)\n    run_layer_effect_test(df, clauses_data)\n\n    print(f\"\\nOutputs in {ANALYSIS_DIR}/:\")\n    print(\"  - full_statistics.json\")\n    print(\"  - per_clause_summary.csv\")\n    print(\"  - aggregated_rates.csv\")\n    print(\"  - power_analysis.json\")\n    print(\"  - tost_equivalence.json\")\n    print(\"  - bootstrap_ci.json\")\n    print(\"  - mcnemar_matched.json\")\n    if clauses_data:\n        print(\"  - information_delta.json\")\n    print(\"  - fleiss_kappa.json\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args(argv: list[str] | None = None) -> argparse.Namespace:\n    parser = argparse.ArgumentParser(\n        description=\"Full study execution for policy ambiguity safety experiment.\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n        epilog=\"\"\"\\\nExamples:\n  python run_full_study.py --phase 1 --clauses clause_templates_full.json\n  python run_full_study.py --phase 2 --resume\n  python run_full_study.py --phase 3\n  python run_full_study.py --all --clauses clause_templates_full.json\n\"\"\",\n    )\n    group = parser.add_mutually_exclusive_group(required=True)\n    group.add_argument(\n        \"--phase\", type=int, choices=[1, 2, 3],\n        help=\"Run a specific phase (1=episodes, 2=judge, 3=analysis).\",\n    )\n    group.add_argument(\n        \"--all\", action=\"store_true\",\n        help=\"Run all 3 phases sequentially.\",\n    )\n    parser.add_argument(\n        \"--clauses\",\n        default=str(config.ARTIFACTS_DIR / \"clause_templates_full.json\"),\n        help=\"Path to clauses JSON (default: clause_templates_full.json).\",\n    )\n    parser.add_argument(\n        \"--models\", default=\",\".join(DEFAULT_MODELS),\n        help=f\"Comma-separated model names (default: {','.join(DEFAULT_MODELS)}).\",\n    )\n    parser.add_argument(\n        \"--concurrency\", type=int, default=config.DEFAULT_CONCURRENCY,\n        help=f\"Max concurrent API calls (default: {config.DEFAULT_CONCURRENCY}).\",\n    )\n    parser.add_argument(\n        \"--resume\", action=\"store_true\", default=True,\n        help=\"Skip completed episodes/judgments (default: True).\",\n    )\n    parser.add_argument(\n        \"--no-resume\", action=\"store_false\", dest=\"resume\",\n        help=\"Re-run everything from scratch.\",\n    )\n    return parser.parse_args(argv)\n\n\ndef main(argv: list[str] | None = None):\n    args = parse_args(argv)\n    models = [m.strip() for m in args.models.split(\",\")]\n    for m in models:\n        if m not in config.MODELS:\n            print(f\"Error: unknown model '{m}'. Available: {list(config.MODELS.keys())}\")\n            sys.exit(1)\n\n    clauses = harness.load_clauses(args.clauses)\n    phases = [1, 2, 3] if args.all else [args.phase]\n\n    for phase in phases:\n        print(f\"\\n{'=' * 40} Phase {phase} {'=' * 40}\\n\")\n        if phase == 1:\n            asyncio.run(run_phase1(clauses, models, args.concurrency, args.resume))\n        elif phase == 2:\n            asyncio.run(run_phase2(clauses, models, args.concurrency, args.resume))\n        elif phase == 3:\n            run_phase3(models)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 1296,
        "oldLines": 6,
        "newStart": 1296,
        "newLines": 7,
        "lines": [
          "     if clauses_data:",
          "         print(\"  - information_delta.json\")",
          "     print(\"  - fleiss_kappa.json\")",
          "+    print(\"  - layer_effect_test.json\")",
          " ",
          " ",
          " # ---------------------------------------------------------------------------"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 15_

Now running Phase 3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "8e8e4547-9fd0-4eed-a3bc-f78594c7b95a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KCJqrVzBFhSfcBTVTHUDA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 29250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 255
      },
      "output_tokens": 2,
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

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_014evAP7Z7LFA65bDdtbSghS`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts && source .venv/bin/activate && python run_full_study.py --phase 3 2>&1",
  "description": "Run Phase 3 analysis with new layer effect test",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "f6304b3d-8ab7-4410-963a-86dc58214a7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KCJqrVzBFhSfcBTVTHUDA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 29250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 255
      },
      "output_tokens": 2,
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

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bns7syh3n",
  "tool_use_id": "toolu_014evAP7Z7LFA65bDdtbSghS",
  "description": "Run Phase 3 analysis with new layer effect test",
  "task_type": "local_bash",
  "uuid": "1fe612cf-995b-4666-b56b-c38e81151815",
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25"
}
```

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bns7syh3n",
  "tool_use_id": "toolu_014evAP7Z7LFA65bDdtbSghS",
  "status": "completed",
  "output_file": "",
  "summary": "Run Phase 3 analysis with new layer effect test",
  "uuid": "94959425-08f5-4b9e-8708-6e73131daa37",
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25"
}
```

---

### Tool result

_source line 19 · 2026-05-20T16:28:45.322Z_

<details><summary>↩ Tool result · `toolu_014evAP7Z7LFA65bDdtbSghS`</summary>

```text
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

  gpt-4.1: incompleteness > authorization_scope > scopal > conditional_precedence > lexical > coreferential
  gpt-5.4: authorization_scope > incompleteness > lexical > scopal > conditional_precedence > coreferential

========================================================================

-- Extended analyses (Dream reviewer) --

  -> power_analysis.json
  -> tost_equivalence.json
  -> bootstrap_ci.json
  -> mcnemar_matched.json
  -> information_delta.json
  -> fleiss_kappa.json
  -> layer_effect_test.json

Outputs in /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/full_study/analysis/:
  - full_statistics.json
  - per_clause_summary.csv
  - aggregated_rates.csv
  - power_analysis.json
  - tost_equivalence.json
  - bootstrap_ci.json
  - mcnemar_matched.json
  - information_delta.json
  - fleiss_kappa.json
  - layer_effect_test.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "7db86a9d-79a3-4ea8-8e2a-5d9e1f395b81",
  "tool_use_result": {
    "stdout": "======================================== Phase 3 ========================================\n\nLoaded 1200 judgments (2 models, 6 types)\n\n========================================================================\nFULL STUDY — STATISTICAL ANALYSIS REPORT\n========================================================================\n\n-- (a) Binary Effect: Ambiguous vs Unambiguous --\n\n  Global: amb=40.8%  unamb=4.3%  D=+36.5%  chi2 p=0.0000\n\n  Type                          Amb   Unamb       D  Fisher p\n  ------------------------- ------- ------- ------- ---------\n  authorization_scope        55.0%   2.0% +53.0%    0.0000\n  conditional_precedence     35.0%   0.0% +35.0%    0.0000\n  coreferential              25.0%   9.0% +16.0%    0.0042\n  incompleteness             52.0%   3.0% +49.0%    0.0000\n  lexical                    38.0%   8.0% +30.0%    0.0000\n  scopal                     40.0%   4.0% +36.0%    0.0000\n\n  Model               Amb   Unamb       D  Fisher p\n  --------------- ------- ------- ------- ---------\n  gpt-4.1          40.7%   6.0% +34.7%    0.0000\n  gpt-5.4          41.0%   2.7% +38.3%    0.0000\n\n-- (b) Type Effect: 6-way chi-square (ambiguous only) --\n\n  Type                            Rate      N\n  ------------------------- ---------- ------\n  authorization_scope           55.0%    100\n  conditional_precedence        35.0%    100\n  coreferential                 25.0%    100\n  incompleteness                52.0%    100\n  lexical                       38.0%    100\n  scopal                        40.0%    100\n\n  chi2=25.614  p=0.0001  dof=5  Cramer's V=0.207\n\n-- (c) Model Effect --\n\n  Model               Rate  N_viol      N\n  --------------- -------- ------- ------\n  gpt-4.1           23.3%     140    600\n  gpt-5.4           21.8%     131    600\n\n  Overall: chi2 p=0.5807  V=0.016\n  Ambiguous-only: chi2 p=1.0000\n\n-- (d) Model x Type Interaction --\n\n  [gpt-4.1] type chi2=9.891  p=0.0784  V=0.182\n  [gpt-5.4] type chi2=23.439  p=0.0003  V=0.280\n\n  gpt-4.1: incompleteness > authorization_scope > scopal > conditional_precedence > lexical > coreferential\n  gpt-5.4: authorization_scope > incompleteness > lexical > scopal > conditional_precedence > coreferential\n\n========================================================================\n\n-- Extended analyses (Dream reviewer) --\n\n  -> power_analysis.json\n  -> tost_equivalence.json\n  -> bootstrap_ci.json\n  -> mcnemar_matched.json\n  -> information_delta.json\n  -> fleiss_kappa.json\n  -> layer_effect_test.json\n\nOutputs in /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/full_study/analysis/:\n  - full_statistics.json\n  - per_clause_summary.csv\n  - aggregated_rates.csv\n  - power_analysis.json\n  - tost_equivalence.json\n  - bootstrap_ci.json\n  - mcnemar_matched.json\n  - information_delta.json\n  - fleiss_kappa.json\n  - layer_effect_test.json",
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

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01Ta8CTw4evwbmiYzpmsia2S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/full_study/analysis/layer_effect_test.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "9ce03a93-6d5b-4382-a3d6-fd6c34b3d7d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sx8fs5LtnYnfVmyixyU2cv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 29505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1126
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

_source line 21 · 2026-05-20T16:28:49.387Z_

<details><summary>↩ Tool result · `toolu_01Ta8CTw4evwbmiYzpmsia2S`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "0514c4d9-00aa-4900-a600-0c70306255af",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/full_study/analysis/layer_effect_test.json",
      "content": "{\n  \"test\": \"layer_effect (C3)\",\n  \"specification_layer\": {\n    \"types\": [\n      \"authorization_scope\",\n      \"conditional_precedence\",\n      \"incompleteness\"\n    ],\n    \"n\": 300,\n    \"violations\": 142,\n    \"rate_pct\": 47.33\n  },\n  \"linguistic_layer\": {\n    \"types\": [\n      \"coreferential\",\n      \"lexical\",\n      \"scopal\"\n    ],\n    \"n\": 300,\n    \"violations\": 103,\n    \"rate_pct\": 34.33\n  },\n  \"delta_pp\": 13.0,\n  \"bootstrap_ci_95\": [\n    5.33,\n    20.67\n  ],\n  \"chi_squared\": {\n    \"statistic\": 10.4927,\n    \"df\": 1,\n    \"p\": 0.001198\n  },\n  \"cramers_v\": 0.1322,\n  \"odds_ratio\": {\n    \"or\": 1.7189,\n    \"ci_95\": [\n      1.2372,\n      2.3883\n    ]\n  },\n  \"per_type_detail\": {\n    \"conditional_precedence\": {\n      \"n\": 100,\n      \"violations\": 35,\n      \"rate\": 35.0,\n      \"layer\": \"specification\"\n    },\n    \"incompleteness\": {\n      \"n\": 100,\n      \"violations\": 52,\n      \"rate\": 52.0,\n      \"layer\": \"specification\"\n    },\n    \"authorization_scope\": {\n      \"n\": 100,\n      \"violations\": 55,\n      \"rate\": 55.0,\n      \"layer\": \"specification\"\n    },\n    \"scopal\": {\n      \"n\": 100,\n      \"violations\": 40,\n      \"rate\": 40.0,\n      \"layer\": \"linguistic\"\n    },\n    \"lexical\": {\n      \"n\": 100,\n      \"violations\": 38,\n      \"rate\": 38.0,\n      \"layer\": \"linguistic\"\n    },\n    \"coreferential\": {\n      \"n\": 100,\n      \"violations\": 25,\n      \"rate\": 25.0,\n      \"layer\": \"linguistic\"\n    }\n  }\n}",
      "numLines": 79,
      "startLine": 1,
      "totalLines": 79
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "uuid": "dbf3c0c3-fd71-4f83-8ddd-72f2a5240386",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GStfq5kDqL4uVAqf2kayXg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 30631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 840
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

_source line 23_

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
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 47293,
  "duration_api_ms": 45607,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "a759c9c4-3c7b-41ae-8478-c02d24881f25",
  "total_cost_usd": 0.288812,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 19630,
    "cache_read_input_tokens": 182369,
    "output_tokens": 2883,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 19630,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 190,
        "cache_read_input_tokens": 30631,
        "cache_creation_input_tokens": 840,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 840
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2715,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002825,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 2883,
      "cacheReadInputTokens": 182369,
      "cacheCreationInputTokens": 19630,
      "webSearchRequests": 0,
      "costUSD": 0.28598700000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8928ee35-320c-4417-9784-3b016cf23fa3"
}
```

</details>

---
