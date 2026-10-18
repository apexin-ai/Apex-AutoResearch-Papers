# code d015 g4 absolute threshold

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_code_d015-g4-absolute-threshold_20260515T203457.jsonl`
- **Structured JSON:** [`965169f2b9db319de27b.json`](../../sessions/96/965169f2b9db319de27b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-15T20:37:13.355117+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T20:37:13.355496+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T20:37:13.355668+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T20:37:13.355950+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"D014 Gate Evaluation for IMM MVP.\\n\\nCompares baseline and IMM evaluation JSONs against 4 gate criteria:\\n  G1: Δ_k median improvement ≥ 2x\\n  G2: Top-k preservation rate improvement ≥ 10pp\\n  G3: Clean action loss ratio ≤ 1.10\\n  G4: L·ε·k/Δ_k ratio decrease ≥ 30%\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\n\\ndef load_results(path: str) -> dict:\\n    with open(path) as f:\\n        return json.load(f)\\n\\n\\ndef get_condition_keys(results: dict) -> list[str]:\\n    return sorted(k for k in results if not k.startswith(\\\"_\\\"))\\n\\n\\ndef get_perturbed_keys(results: dict, prune: bool = False) -> list[str]:\\n    prune_str = \\\"True\\\" if prune else \\\"False\\\"\\n    return sorted(\\n        k for k in results\\n        if not k.startswith(\\\"_\\\")\\n        and k.startswith(\\\"eps\\\")\\n        and not k.startswith(\\\"eps0.0_\\\")\\n        and k.endswith(f\\\"prune{prune_str}\\\")\\n    )\\n\\n\\ndef mean(values: list[float]) -> float:\\n    return sum(values) / len(values) if values else float(\\\"nan\\\")\\n\\n\\ndef evaluate_gate(baseline: dict, imm: dict, condition: str | None = None) -> dict:\\n    \\\"\\\"\\\"Evaluate gate criteria.\\n\\n    If condition is None, aggregates across all perturbed non-pruned conditions.\\n    \\\"\\\"\\\"\\n    clean_key = \\\"eps0.0_pruneFalse\\\"\\n\\n    # G3: Clean action loss ratio\\n    bl_clean_loss = baseline.get(clean_key, {}).get(\\\"action_loss\\\")\\n    imm_clean_loss = imm.get(clean_key, {}).get(\\\"action_loss\\\")\\n\\n    g3_ratio = None\\n    if bl_clean_loss and imm_clean_loss and bl_clean_loss > 0:\\n        g3_ratio = imm_clean_loss / bl_clean_loss\\n\\n    if condition is not None:\\n        conditions = [condition]\\n    else:\\n        bl_perturbed = set(get_perturbed_keys(baseline))\\n        imm_perturbed = set(get_perturbed_k
…[truncated 7286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T20:37:13.356176+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "wc -l /root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "wc -l /root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T20:37:13.356373+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"284 /root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T20:37:13.356522+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "head -145 /root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "head -145 /root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T20:37:13.356727+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"D014 Gate Evaluation for IMM MVP.\\n\\nCompares baseline and IMM evaluation JSONs against 4 gate criteria:\\n  G1: Δ_k median improvement ≥ 2x\\n  G2: Top-k preservation rate improvement ≥ 10pp\\n  G3: Clean action loss ratio ≤ 1.10\\n  G4: L·ε·k/Δ_k ratio decrease ≥ 30%\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport sys\\nfrom pathlib import Path\\n\\n\\ndef load_results(path: str) -> dict:\\n    with open(path) as f:\\n        return json.load(f)\\n\\n\\ndef get_condition_keys(results: dict) -> list[str]:\\n    return sorted(k for k in results if not k.startswith(\\\"_\\\"))\\n\\n\\ndef get_perturbed_keys(results: dict, prune: bool = False) -> list[str]:\\n    prune_str = \\\"True\\\" if prune else \\\"False\\\"\\n    return sorted(\\n        k for k in results\\n        if not k.startswith(\\\"_\\\")\\n        and k.startswith(\\\"eps\\\")\\n        and not k.startswith(\\\"eps0.0_\\\")\\n        and k.endswith(f\\\"prune{prune_str}\\\")\\n    )\\n\\n\\ndef mean(values: list[float]) -> float:\\n    return sum(values) / len(values) if values else float(\\\"nan\\\")\\n\\n\\ndef evaluate_gate(baseline: dict, imm: dict, condition: str | None = None) -> dict:\\n    \\\"\\\"\\\"Evaluate gate criteria.\\n\\n    If condition is None, aggregates across all perturbed non-pruned conditions.\\n    \\\"\\\"\\\"\\n    clean_key = \\\"eps0.0_pruneFalse\\\"\\n\\n    # G3: Clean action loss ratio\\n    bl_clean_loss = baseline.get(clean_key, {}).get(\\\"action_loss\\\")\\n    imm_clean_loss = imm.get(clean_key, {}).get(\\\"action_loss\\\")\\n\\n    g3_ratio = None\\n    if bl_clean_loss and imm_clean_loss and bl_clean_loss > 0:\\n        g3_ratio = imm_clean_loss / bl_clean_loss\\n\\n    if condition is not None:\\n        conditions = [condition]\\n    else:\\n        bl_perturbed = set(get_perturbed_keys(baseline))\\n        imm_perturbed = set(get_perturbed_k
…[truncated 3350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T20:37:13.356881+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -n +140 /root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "tail -n +140 /root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T20:37:13.357114+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n    return {\\n        \\\"conditions_evaluated\\\": conditions,\\n        \\\"per_condition\\\": per_condition,\\n        \\\"gate\\\": {\\n            \\\"G1_margin_median_ratio\\\": {\\n                \\\"value\\\": g1_value,\\n                \\\"threshold\\\": \\\"≥ 2.0\\\",\\n                \\\"pass\\\": g1_pass,\\n            },\\n            \\\"G2_preservation_rate_diff\\\": {\\n                \\\"value\\\": g2_value,\\n                \\\"threshold\\\": \\\"≥ 0.10\\\",\\n                \\\"pass\\\": g2_pass,\\n            },\\n            \\\"G3_clean_action_loss_ratio\\\": {\\n                \\\"value\\\": g3_ratio,\\n                \\\"threshold\\\": \\\"≤ 1.10\\\",\\n                \\\"bl_loss\\\": bl_clean_loss,\\n                \\\"imm_loss\\\": imm_clean_loss,\\n                \\\"pass\\\": g3_pass,\\n            },\\n            \\\"G4_led_ratio_decrease\\\": {\\n                \\\"value\\\": g4_value,\\n                \\\"threshold\\\": \\\"≥ 0.30\\\",\\n                \\\"bl_led_avg\\\": bl_led_avg,\\n                \\\"imm_led_avg\\\": imm_led_avg,\\n                \\\"pass\\\": g4_pass,\\n                \\\"baseline_degenerate\\\": g4_baseline_degenerate,\\n            },\\n        },\\n        \\\"overall_pass\\\": overall,\\n    }\\n\\n\\ndef format_val(v, fmt=\\\".4f\\\"):\\n    if v is None:\\n        return \\\"N/A\\\"\\n    return f\\\"{v:{fmt}}\\\"\\n\\n\\ndef print_report(result: dict, output_json: str | None = None):\\n    if \\\"error\\\" in result:\\n        print(f\\\"ERROR: {result['error']}\\\")\\n        print(f\\\"  Baseline keys: {result.get('baseline_keys')}\\\")\\n        print(f\\\"  IMM keys:      {result.get('imm_keys')}\\\")\\n        sys.exit(1)\\n\\n    gate = result[\\\"gate\\\"]\\n    conditions = result[\\\"conditions_evaluated\\\"]\\n\\n    print(\\\"=\\\" * 64)\\n    print(\\\"  D014 GATE EVALUATION REPORT\\\")\\n    print(\\\"=\\\" * 64)\\n  
…[truncated 4353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T20:37:13.357386+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress -name \"*.json\" -path \"*/results/*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress -name \"*.json\" -path \"*/results/*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T20:37:13.357537+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/results/eval_step_005000.json\\n/root/autodl-tmp/importance_margin_vla_compress/results/eval_imm_v7_dryrun.json\\n/root/autodl-tmp/importance_margin_vla_compress/results/eval_baseline_v5.json\\n/root/autodl-tmp/importance_margin_vla_compress/results/eval_imm_v7_step004000.json\\n/root/autodl-tmp/importance_margin_vla_compress/results/eval_imm_v7_step006000.json\\n/root/autodl-tmp/importance_margin_vla_compress/results/eval_baseline_v5_d011.json\\n/root/autodl-tmp/importance_margin_vla_compress/results/eval_imm_v7_step008000.json\\n/root/autodl-tmp/importance_margin_vla_compress/results/eval_imm_v7_step020000_quick.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T20:37:13.357722+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cat > /root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py << 'ENDOFFILE'\n\"\"\"D015 Gate Evaluation for IMM MVP.\n\nCompares baseline and IMM evaluation JSONs against 4 gate criteria:\n  G1: Δ_k median improvement ≥ 2x\n  G2: Top-k preservation rate improvement ≥ 10pp\n  G3: Clean action loss ratio ≤ 1.10\n  G4: L·ε·k/Δ_k ratio median < 1.0 (certified bound)\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport statistics\nimport sys\nfrom pathlib import Path\n\n\ndef load_results(path: str) -> dict:\n    with open(path) as f:\n        return json.load(f)\n\n\ndef get_condition_keys(results: dict) -> list[str]:\n    return sorted(k for k in results if not k.startswith(\"_\"))\n\n\ndef get_perturbed_keys(results: dict, prune: bool = False) -> list[str]:\n    prune_str = \"True\" if prune else \"False\"\n    return sorted(\n        k for k in results\n        if not k.startswith(\"_\")\n        and k.startswith(\"eps\")\n        and not k.startswith(\"eps0.0_\")\n        and k.endswith(f\"prune{prune_str}\")\n    )\n\n\ndef mean(values: list[float]) -> float:\n    return sum(values) / len(values) if values else float(\"nan\")\n\n\ndef evaluate_gate(baseline: dict, imm: dict, condition: str | None = None) -> dict:\n    \"\"\"Evaluate gate criteria.\n\n    If condition is None, aggregates across all perturbed non-pruned conditions.\n    \"\"\"\n    clean_key = \"eps0.0_pruneFalse\"\n\n    # G3: Clean action loss ratio\n    bl_clean_loss = baseline.get(clean_key, {}).get(\"action_loss\")\n    imm_clean_loss = imm.get(clean_key, {}).get(\"action_loss\")\n\n    g3_ratio = None\n    if bl_clean_loss and imm_clean_loss and bl_clean_loss > 0:\n        g3_ratio = imm_clean_loss / bl_clean_loss\n\n    if condition is not None:\n        conditions = [condition]\n    else:\n        bl_perturbed = set(get_perturbed_keys(baseline))\n        imm_perturbed = set(get_perturbed_keys(imm))\n        conditions = sorted(bl_perturbed & imm_perturbed)\n\n    if not conditions:\n        return {\n            \"error\": \"No matching perturbed conditions found\",\n            \"baseline_keys\": get_condition_keys(baseline),\n            \"imm_keys\": get_condition_keys(imm),\n        }\n\n    # Collect per-condition values\n    margin_ratios = []\n    pres_diffs = []\n    led_ratios_imm = []\n\n    per_condition = {}\n    for cond in conditions:\n        bl_data = baseline.get(cond, {})\n        imm_data = imm.get(cond, {})\n\n        bl_margin = bl_data.get(\"margin_median\")\n        imm_margin = imm_data.get(\"margin_median\")\n        bl_pres = bl_data.get(\"preservation_rate\")\n        imm_pres = imm_data.get(\"preservation_rate\")\n        imm_led = imm_data.get(\"l_eps_delta_ratio_median\")\n\n        cond_info = {}\n\n        if bl_margin and imm_margin and bl_margin > 0:\n            ratio = imm_margin / bl_margin\n            margin_ratios.append(ratio)\n            cond_info[\"margin_ratio\"] = ratio\n            cond_info[\"bl_margin_median\"] = bl_margin\n            cond_info[\"imm_margin_median\"] = imm_margin\n\n        if bl_pres is not None and imm_pres is not None:\n            diff = imm_pres - bl_pres\n            pres_diffs.append(diff)\n            cond_info[\"pres_diff\"] = diff\n            cond_info[\"bl_preservation\"] = bl_pres\n            cond_info[\"imm_preservation\"] = imm_pres\n\n        if imm_led is not None:\n            led_ratios_imm.append(imm_led)\n            cond_info[\"imm_led_median\"] = imm_led\n\n        per_condition[cond] = cond_info\n\n    # Aggregate\n    g1_value = mean(margin_ratios) if margin_ratios else None\n    g2_value = mean(pres_diffs) if pres_diffs else None\n\n    g4_value = statistics.median(led_ratios_imm) if led_ratios_imm else None\n\n    # Gate judgments\n    g1_pass = g1_value is not None and g1_value >= 2.0\n    g2_pass = g2_value is not None and g2_value >= 0.10\n    g3_pass = g3_ratio is not None and g3_ratio <= 1.10\n    g4_pass = g4_value is not None and g4_value < 1.0\n\n    overall = g1_pass and g2_pass and g3_pass and g4_pass\n\n    return {\n        \"conditions_evaluated\": conditions,\n        \"per_condition\": per_condition,\n        \"gate\": {\n            \"G1_margin_median_ratio\": {\n                \"value\": g1_value,\n                \"threshold\": \"≥ 2.0\",\n                \"pass\": g1_pass,\n            },\n            \"G2_preservation_rate_diff\": {\n                \"value\": g2_value,\n                \"threshold\": \"≥ 0.10\",\n                \"pass\": g2_pass,\n            },\n            \"G3_clean_action_loss_ratio\": {\n                \"value\": g3_ratio,\n                \"threshold\": \"≤ 1.10\",\n                \"bl_loss\": bl_clean_loss,\n                \"imm_loss\": imm_clean_loss,\n                \"pass\": g3_pass,\n            },\n            \"G4_led_ratio_median\": {\n                \"value\": g4_value,\n                \"threshold\": \"< 1.0\",\n                \"pass\": g4_pass,\n            },\n        },\n        \"overall_pass\": overall,\n    }\n\n\ndef format_val(v, fmt=\".4f\"):\n    if v is None:\n        return \"N/A\"\n    return f\"{v:{fmt}}\"\n\n\ndef print_report(result: dict, output_json: str | None = None):\n    if \"error\" in result:\n        print(f\"ERROR: {result['error']}\")\n        print(f\"  Baseline keys: {result.get('baseline_keys')}\")\n        print(f\"  IMM keys:      {result.get('imm_keys')}\")\n        sys.exit(1)\n\n    gate = result[\"gate\"]\n    conditions = result[\"conditions_evaluated\"]\n\n    print(\"=\" * 64)\n    print(\"  D015 GATE EVALUATION REPORT\")\n    print(\"=\" * 64)\n    print()\n    print(f\"Conditions evaluated: {', '.join(conditions)}\")\n    print()\n\n    # Per-condition detail\n    print(\"--- Per-Condition Detail ---\")\n    for cond, info in result[\"per_condition\"].items():\n        print(f\"\\n  [{cond}]\")\n        if \"margin_ratio\" in info:\n            print(f\"    Δ_k median:  BL={format_val(info['bl_margin_median'])}  IMM={format_val(info['imm_margin_median'])}  ratio={format_val(info['margin_ratio'], '.2f')}x\")\n        if \"pres_diff\" in info:\n            print(f\"    Preservation: BL={format_val(info['bl_preservation'])}  IMM={format_val(info['imm_preservation'])}  diff={format_val(info['pres_diff'], '+.4f')}\")\n        if \"imm_led_median\" in info:\n            print(f\"    L·ε·k/Δ_k:  IMM={format_val(info['imm_led_median'])}\")\n\n    # Gate summary\n    print()\n    print(\"--- Gate Criteria (aggregated) ---\")\n    print()\n\n    criteria = [\n        (\"G1\", \"Δ_k median improvement ≥ 2x\", gate[\"G1_margin_median_ratio\"]),\n        (\"G2\", \"Top-k preservation ≥ +10pp\", gate[\"G2_preservation_rate_diff\"]),\n        (\"G3\", \"Clean action loss ratio ≤ 1.10\", gate[\"G3_clean_action_loss_ratio\"]),\n        (\"G4\", \"LED ratio median < 1.0 (certified bound)\", gate[\"G4_led_ratio_median\"]),\n    ]\n\n    for tag, desc, info in criteria:\n        status = \"PASS\" if info[\"pass\"] else \"FAIL\"\n        val = info[\"value\"]\n        thr = info[\"threshold\"]\n        if tag == \"G1\":\n            val_str = f\"{format_val(val, '.2f')}x\"\n        elif tag == \"G2\":\n            val_str = format_val(val, \"+.4f\")\n        elif tag == \"G3\":\n            val_str = format_val(val, \".4f\")\n        elif tag == \"G4\":\n            val_str = format_val(val, \".4f\")\n        else:\n            val_str = format_val(val)\n        print(f\"  [{status}] {tag}: {desc}\")\n        print(f\"         value={val_str}  threshold={thr}\")\n\n    print()\n    print(\"=\" * 64)\n    overall = result[\"overall_pass\"]\n    verdict = \"PASS\" if overall else \"FAIL\"\n    print(f\"  OVERALL VERDICT: {verdict}\")\n    print(\"=\" * 64)\n\n    if output_json:\n        out_path = Path(output_json)\n        out_path.parent.mkdir(parents=True, exist_ok=True)\n        with open(out_path, \"w\") as f:\n            json.dump(result, f, indent=2, default=str)\n        print(f\"\\nDetailed results saved to {out_path}\")\n\n    return 0 if overall else 1\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"D015 Gate Evaluation: compare baseline vs IMM eval results\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n        epilog=\"\"\"\\\nexamples:\n  python analyze_gate.py --baseline results/baseline.json --imm results/imm.json\n  python analyze_gate.py --baseline bl.json --imm imm.json --condition eps0.01_pruneFalse\n  python analyze_gate.py --baseline bl.json --imm imm.json --output gate_report.json\n\"\"\",\n    )\n    parser.add_argument(\"--baseline\", required=True, help=\"Path to baseline eval JSON\")\n    parser.add_argument(\"--imm\", required=True, help=\"Path to IMM eval JSON\")\n    parser.add_argument(\"--condition\", default=None, help=\"Evaluate a single condition (default: aggregate all perturbed non-pruned)\")\n    parser.add_argument(\"--output\", default=None, help=\"Save detailed results to JSON\")\n    args = parser.parse_args()\n\n    baseline = load_results(args.baseline)\n    imm = load_results(args.imm)\n\n    result = evaluate_gate(baseline, imm, condition=args.condition)\n    exit_code = print_report(result, output_json=args.output)\n    sys.exit(exit_code)\n\n\nif __name__ == \"__main__\":\n    main()\nENDOFFILE",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat > /root/autodl-tmp/importance_margin_vla_compress/analyze_gate.py << 'ENDOFFILE'\n\"\"\"D015 Gate Evaluation for IMM MVP.\n\nCompares baseline and IMM evaluation JSONs against 4 gate criteria:\n  G1: Δ_k median improvement ≥ 2x\n  G2: Top-k preservation rate improvement ≥ 10pp\n  G3: Clean action loss ratio ≤ 1.10\n  G4: L·ε·k/Δ_k ratio median < 1.0 (certified bound)\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport statistics\nimport sys\nfrom pathlib import Path\n\n\ndef load_results(path: str) -> dict:\n    with open(path) as f:\n        return json.load(f)\n\n\ndef get_condition_keys(results: dict) -> list[str]:\n    return sorted(k for k in results if not k.startswith(\"_\"))\n\n\ndef get_perturbed_keys(results: dict, prune: bool = False) -> list[str]:\n    prune_str = \"True\" if prune else \"False\"\n    return sorted(\n        k for k in results\n        if not k.startswith(\"_\")\n        and k.startswith(\"eps\")\n        and not k.startswith(\"eps0.0_\")\n        and k.endswith(f\"prune{prune_str}\")\n    )\n\n\ndef mean(values: list[float]) -> float:\n    return sum(values) / len(values) if values else float(\"nan\")\n\n\ndef evaluate_gate(baseline: dict, imm: dict, condition: str | None = None) -> dict:\n    \"\"\"Evaluate gate criteria.\n\n    If condition is None, aggregates across all perturbed non-pruned conditions.\n    \"\"\"\n    clean_key = \"eps0.0_pruneFalse\"\n\n    # G3: Clean action loss ratio\n    bl_clean_loss = baseline.get(clean_key, {}).get(\"action_loss\")\n    imm_clean_loss = imm.get(clean_key, {}).get(\"action_loss\")\n\n    g3_ratio = None\n    if bl_clean_loss and imm_clean_loss and bl_clean_loss > 0:\n        g3_ratio = imm_clean_loss / bl_clean_loss\n\n    if condition is not None:\n        conditions = [condition]\n    else:\n        bl_perturbed = set(get_perturbed_keys(baseline))\n        imm_perturbed = set(get_perturbed_keys(imm))\n        conditions = sorted(bl_perturbed & imm_perturbed)\n\n    if not conditions:\n        return {\n            \"error\": \"No matching perturbed conditions found\",\n            \"baseline_keys\": get_condition_keys(baseline),\n            \"imm_keys\": get_condition_keys(imm),\n        }\n\n    # Collect per-condition values\n    margin_ratios = []\n    pres_diffs = []\n    led_ratios_imm = []\n\n    per_condition = {}\n    for cond in conditions:\n        bl_data = baseline.get(cond, {})\n        imm_data = imm.get(cond, {})\n\n        bl_margin = bl_data.get(\"margin_median\")\n        imm_margin = imm_data.get(\"margin_median\")\n        bl_pres = bl_data.get(\"preservation_rate\")\n        imm_pres = imm_data.get(\"preservation_rate\")\n        imm_led = imm_data.get(\"l_eps_delta_ratio_median\")\n\n        cond_info = {}\n\n        if bl_margin and imm_margin and bl_margin > 0:\n            ratio = imm_margin / bl_margin\n            margin_ratios.append(ratio)\n            cond_info[\"margin_ratio\"] = ratio\n            cond_info[\"bl_margin_median\"] = bl_margin\n            cond_info[\"imm_margin_median\"] = imm_margin\n\n        if bl_pres is not None and imm_pres is not None:\n            diff = imm_pres - bl_pres\n            pres_diffs.append(diff)\n            cond_info[\"pres_diff\"] = diff\n            cond_info[\"bl_preservation\"] = bl_pres\n            cond_info[\"imm_preservation\"] = imm_pres\n\n        if imm_led is not None:\n            led_ratios_imm.append(imm_led)\n            cond_info[\"imm_led_median\"] = imm_led\n\n        per_condition[cond] = cond_info\n\n    # Aggregate\n    g1_value = mean(margin_ratios) if margin_ratios else None\n    g2_value = mean(pres_diffs) if pres_diffs else None\n\n    g4_value = statistics.median(led_ratios_imm) if led_ratios_imm else None\n\n    # Gate judgments\n    g1_pass = g1_value is not None and g1_value >= 2.0\n    g2_pass = g2_value is not None and g2_value >= 0.10\n    g3_pass = g3_ratio is not None and g3_ratio <= 1.10\n    g4_pass = g4_value is not None and g4_value < 1.0\n\n    overall = g1_pass and g2_pass and g3_pass and g4_pass\n\n    return {\n        \"conditions_evaluated\": conditions,\n        \"per_condition\": per_condition,\n        \"gate\": {\n            \"G1_margin_median_ratio\": {\n                \"value\": g1_value,\n                \"threshold\": \"≥ 2.0\",\n                \"pass\": g1_pass,\n            },\n            \"G2_preservation_rate_diff\": {\n                \"value\": g2_value,\n                \"threshold\": \"≥ 0.10\",\n                \"pass\": g2_pass,\n            },\n            \"G3_clean_action_loss_ratio\": {\n                \"value\": g3_ratio,\n                \"threshold\": \"≤ 1.10\",\n                \"bl_loss\": bl_clean_loss,\n                \"imm_loss\": imm_clean_loss,\n                \"pass\": g3_pass,\n            },\n            \"G4_led_ratio_median\": {\n                \"value\": g4_value,\n                \"threshold\": \"< 1.0\",\n                \"pass\": g4_pass,\n            },\n        },\n        \"overall_pass\": overall,\n    }\n\n\ndef format_val(v, fmt=\".4f\"):\n    if v is None:\n        return \"N/A\"\n    return f\"{v:{fmt}}\"\n\n\ndef print_report(result: dict, output_json: str | None = None):\n    if \"error\" in result:\n        print(f\"ERROR: {result['error']}\")\n        print(f\"  Baseline keys: {result.get('baseline_keys')}\")\n        print(f\"  IMM keys:      {result.get('imm_keys')}\")\n        sys.exit(1)\n\n    gate = result[\"gate\"]\n    conditions = result[\"conditions_evaluated\"]\n\n    print(\"=\" * 64)\n    print(\"  D015 GATE EVALUATION REPORT\")\n    print(\"=\" * 64)\n    print()\n    print(f\"Conditions evaluated: {', '.join(conditions)}\")\n    print()\n\n    # Per-condition detail\n    print(\"--- Per-Condition Detail ---\")\n    for cond, info in result[\"per_condition\"].items():\n        print(f\"\\n  [{cond}]\")\n        if \"margin_ratio\" in info:\n            print(f\"    Δ_k median:  BL={format_val(info['bl_margin_median'])}  IMM={format_val(info['imm_margin_median'])}  ratio={format_val(info['margin_ratio'], '.2f')}x\")\n        if \"pres_diff\" in info:\n            print(f\"    Preservation: BL={format_val(info['bl_preservation'])}  IMM={format_val(info['imm_preservation'])}  diff={format_val(info['pres_diff'], '+.4f')}\")\n        if \"imm_led_median\" in info:\n            print(f\"    L·ε·k/Δ_k:  IMM={format_val(info['imm_led_median'])}\")\n\n    # Gate summary\n    print()\n    print(\"--- Gate Criteria (aggregated) ---\")\n    print()\n\n    criteria = [\n        (\"G1\", \"Δ_k median improvement ≥ 2x\", gate[\"G1_margin_median_ratio\"]),\n        (\"G2\", \"Top-k preservation ≥ +10pp\", gate[\"G2_preservation_rate_diff\"]),\n        (\"G3\", \"Clean action loss ratio ≤ 1.10\", gate[\"G3_clean_action_loss_ratio\"]),\n        (\"G4\", \"LED ratio median < 1.0 (certified bound)\", gate[\"G4_led_ratio_median\"]),\n    ]\n\n    for tag, desc, info in criteria:\n        status = \"PASS\" if info[\"pass\"] else \"FAIL\"\n        val = info[\"value\"]\n        thr = info[\"threshold\"]\n        if tag == \"G1\":\n            val_str = f\"{format_val(val, '.2f')}x\"\n        elif tag == \"G2\":\n            val_str = format_val(val, \"+.4f\")\n        elif tag == \"G3\":\n            val_str = format_val(val, \".4f\")\n        elif tag == \"G4\":\n            val_str = format_val(val, \".4f\")\n        else:\n            val_str = format_val(val)\n        print(f\"  [{status}] {tag}: {desc}\")\n        print(f\"         value={val_str}  threshold={thr}\")\n\n    print()\n    print(\"=\" * 64)\n    overall = result[\"overall_pass\"]\n    verdict = \"PASS\" if overall else \"FAIL\"\n    print(f\"  OVERALL VERDICT: {verdict}\")\n    print(\"=\" * 64)\n\n    if output_json:\n        out_path = Path(output_json)\n        out_path.parent.mkdir(parents=True, exist_ok=True)\n        with open(out_path, \"w\") as f:\n            json.dump(result, f, indent=2, default=str)\n        print(f\"\\nDetailed results saved to {out_path}\")\n\n    return 0 if overall else 1\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"D015 Gate Evaluation: compare baseline vs IMM eval results\",\n        formatter_class=argparse.RawDescriptionHelpFormatter,\n        epilog=\"\"\"\\\nexamples:\n  python analyze_gate.py --baseline results/baseline.json --imm results/imm.json\n  python analyze_gate.py --baseline bl.json --imm imm.json --condition eps0.01_pruneFalse\n  python analyze_gate.py --baseline bl.json --imm imm.json --output gate_report.json\n\"\"\",\n    )\n    parser.add_argument(\"--baseline\", required=True, help=\"Path to baseline eval JSON\")\n    parser.add_argument(\"--imm\", required=True, help=\"Path to IMM eval JSON\")\n    parser.add_argument(\"--condition\", default=None, help=\"Evaluate a single condition (default: aggregate all perturbed non-pruned)\")\n    parser.add_argument(\"--output\", default=None, help=\"Save detailed results to JSON\")\n    args = parser.parse_args()\n\n    baseline = load_results(args.baseline)\n    imm = load_results(args.imm)\n\n    result = evaluate_gate(baseline, imm, condition=args.condition)\n    exit_code = print_report(result, output_json=args.output)\n    sys.exit(exit_code)\n\n\nif __name__ == \"__main__\":\n    main()\nENDOFFILE",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T20:37:13.357956+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T20:37:13.358097+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_gate.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_gate.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T20:37:13.358269+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: analyze_gate.py [-h] --baseline BASELINE --imm IMM\\n                       [--condition CONDITION] [--output OUTPUT]\\n\\nD015 Gate Evaluation: compare baseline vs IMM eval results\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --baseline BASELINE   Path to baseline eval JSON\\n  --imm IMM             Path to IMM eval JSON\\n  --condition CONDITION\\n                        Evaluate a single condition (default: aggregate all\\n                        perturbed non-pruned)\\n  --output OUTPUT       Save detailed results to JSON\\n\\nexamples:\\n  python analyze_gate.py --baseline results/baseline.json --imm results/imm.json\\n  python analyze_gate.py --baseline bl.json --imm imm.json --condition eps0.01_pruneFalse\\n  python analyze_gate.py --baseline bl.json --imm imm.json --output gate_report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T20:37:13.358412+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-27271",
  "command": "cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_gate.py --baseline results/eval_baseline_v5.json --imm results/eval_imm_v7_step008000.json 2>&1; echo \"EXIT_CODE=$?\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-27271",
    "command": "cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_gate.py --baseline results/eval_baseline_v5.json --imm results/eval_imm_v7_step008000.json 2>&1; echo \"EXIT_CODE=$?\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T20:37:13.358557+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"================================================================\\n  D015 GATE EVALUATION REPORT\\n================================================================\\n\\nConditions evaluated: eps0.01_pruneFalse, eps0.02_pruneFalse, eps0.05_pruneFalse\\n\\n--- Per-Condition Detail ---\\n\\n  [eps0.01_pruneFalse]\\n    L·ε·k/Δ_k:  IMM=0.1070\\n\\n  [eps0.02_pruneFalse]\\n    L·ε·k/Δ_k:  IMM=0.2176\\n\\n  [eps0.05_pruneFalse]\\n    L·ε·k/Δ_k:  IMM=0.5479\\n\\n--- Gate Criteria (aggregated) ---\\n\\n  [FAIL] G1: Δ_k median improvement ≥ 2x\\n         value=N/Ax  threshold=≥ 2.0\\n  [FAIL] G2: Top-k preservation ≥ +10pp\\n         value=N/A  threshold=≥ 0.10\\n  [FAIL] G3: Clean action loss ratio ≤ 1.10\\n         value=7.1707  threshold=≤ 1.10\\n  [PASS] G4: LED ratio median < 1.0 (certified bound)\\n         value=0.2176  threshold=< 1.0\\n\\n================================================================\\n  OVERALL VERDICT: FAIL\\n================================================================\\nEXIT_CODE=1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T20:37:13.358732+00:00_

G4 works correctly — median of `[0.1070, 0.2176, 0.5479]` = `0.2176` < 1.0 → PASS.

### 修改前 vs 修改后对比

| 方面 | D014 (旧) | D015 (新) |
|------|-----------|-----------|
| **G4 指标** | `1 - mean(imm_led)/mean(bl_led)` (relative decrease) | `median(imm_led_ratios)` (absolute value) |
| **G4 阈值** | ≥ 30% decrease | < 1.0 |
| **G4 依赖** | 需要 baseline + IMM 的 LED ratio | 只需 IMM 的 LED ratio |
| **Fallback** | baseline L=0 时 auto-PASS | 无 fallback；IMM 没有 LED 字段则 FAIL |
| **聚合方式** | mean | median |
| **Gate dict key** | `G4_led_ratio_decrease` | `G4_led_ratio_median` |

### 验证结果
- `--help` 参数接口不变（`--baseline`, `--imm`, `--condition`, `--output`）
- dry-run 输出格式正确：`G4 PASS: LED ratio median = 0.2176 < 1.0 (certified bound)`
- G1/G2/G3 逻辑完全未动——从输出可见它们仍独立判定（G1 N/A→FAIL, G2 N/A→FAIL, G3 7.17→FAIL，与旧逻辑一致）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_d015-g4-absolute-threshold_20260515T203457"
}
```

</details>

---
