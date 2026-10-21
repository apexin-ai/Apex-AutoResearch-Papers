# code r5 bootstrap method audit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_code_r5_bootstrap_method_audit_20260517T141145.log`
- **Structured JSON:** [`66c96d31caf7953b1b0f.json`](../../sessions/66/66c96d31caf7953b1b0f.json)

## Before a recorded user message

56 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "d2cd0303-df57-4e53-b38b-973ee9c6771a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/memory/"
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
    "resetsAt": 1779036600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "11f9dd06-1694-45e3-a9ab-a353a687e04a",
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091"
}
```

---

### Assistant

_source line 4_

I'll start by reading the bootstrap scripts on the server to check the F1 calculation method.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "07bec200-88f5-4a97-9bbd-631baacfdd2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJ2Mh5F3zuh4rNXtqy27fA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12628,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12628
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UFaxrho5Rst6QUjSgMw2Go`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "8d41c391-cd10-4d4b-be33-d2cc1384ed6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJ2Mh5F3zuh4rNXtqy27fA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12628,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12628
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

_source line 6 · 2026-05-17T14:11:55.646Z_

<details><summary>↩ Tool result · `toolu_01UFaxrho5Rst6QUjSgMw2Go`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "6009e301-49dd-4640-9769-2b1977e3c6eb",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the bootstrap scripts on the server to check the F1 calculation method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "7db3b89a-8d18-4a07-a53d-dc00c348e360",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcqqZMXiapajW1TpmfdCgd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 24469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1903
      },
      "output_tokens": 41,
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

Let me read the FT and ZS bootstrap scripts on the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "d0eda83d-2a07-4875-bf5e-e3bcf5f4e32f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcqqZMXiapajW1TpmfdCgd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 24469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1903
      },
      "output_tokens": 41,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ECqp6C4ovZ12VZ7H48UK5L`</summary>

```json
{
  "server": "westd-16980",
  "command": "find /root/schema_semantic_constrained_ie -name \"*bootstrap*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "d765d033-27ef-4c2f-9d2d-b4f4aa71d439",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WcqqZMXiapajW1TpmfdCgd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 24469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1903
      },
      "output_tokens": 41,
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

_source line 10 · 2026-05-17T14:12:00.433Z_

<details><summary>↩ Tool result · `toolu_01ECqp6C4ovZ12VZ7H48UK5L`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results.json\\n/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results_v2.json\\n/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results_llama.json\\n/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_ft_composability.json\\n/root/schema_semantic_constrained_ie/__pycache__/compute_bootstrap_ci.cpython-312.pyc\\n/root/schema_semantic_constrained_ie/compute_bootstrap_ci.py\\n/root/schema_semantic_constrained_ie/run_bootstrap_llama.py\\n/root/schema_semantic_constrained_ie/compute_bootstrap_ci_llama.py\\n/root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "411e3810-08ac-459f-8470-df48f0ffcf37",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results.json\\\\n/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results_v2.json\\\\n/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results_llama.json\\\\n/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_ft_composability.json\\\\n/root/schema_semantic_constrained_ie/__pycache__/compute_bootstrap_ci.cpython-312.pyc\\\\n/root/schema_semantic_constrained_ie/compute_bootstrap_ci.py\\\\n/root/schema_semantic_constrained_ie/run_bootstrap_llama.py\\\\n/root/schema_semantic_constrained_ie/compute_bootstrap_ci_llama.py\\\\n/root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.3}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results.json\\n/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results_v2.json\\n/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results_llama.json\\n/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_ft_composability.json\\n/root/schema_semantic_constrained_ie/__pycache__/compute_bootstrap_ci.cpython-312.pyc\\n/root/schema_semantic_constrained_ie/compute_bootstrap_ci.py\\n/root/schema_semantic_constrained_ie/run_bootstrap_llama.py\\n/root/schema_semantic_constrained_ie/compute_bootstrap_ci_llama.py\\n/root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CPs9xHX29qf2U1SbQSLgcK`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "d0fea461-a210-4489-bd25-ce6f605bb5ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CtnimN6txt9wX8GVcUDAN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 26372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
      },
      "output_tokens": 60,
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

_source line 12 · 2026-05-17T14:12:03.534Z_

<details><summary>↩ Tool result · `toolu_01CPs9xHX29qf2U1SbQSLgcK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Bootstrap CI for FT (LoRA) composability: constrained vs unconstrained.\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\nfrom pathlib import Path\\n\\n# --- Normalization (reuse from ZS script) ---\\n\\nSCIERC_TYPE_MAP = {\\n    \\\"otherscientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other-scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other_scientific_term\\\": \\\"OtherScientificTerm\\\",\\n    \\\"scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other\\\": \\\"OtherScientificTerm\\\",\\n}\\n\\ndef scierc_normalize_type(t, valid_types):\\n    t_lower = t.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vt in valid_types:\\n        if t_lower == vt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vt\\n    if t_lower in SCIERC_TYPE_MAP:\\n        return SCIERC_TYPE_MAP[t_lower]\\n    return None\\n\\nDOCRED_VALID_ENTITY_TYPES = {\\\"PER\\\", \\\"ORG\\\", \\\"LOC\\\", \\\"TIME\\\", \\\"NUM\\\", \\\"MISC\\\"}\\nDOCRED_ENTITY_TYPE_ALIASES = {\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC',\\n    'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\ndef docred_normalize_entity_type(raw_type):\\n    t = raw_type.strip().upper()\\n    return DOCRED_ENTITY_TYPE_ALIASES.get(t, t)\\n\\ndef _levenshtein(s1, s2):\\n    if len(s1) < len(s2):\\n        return _levenshtein(s2, s1)\\n    if len(s2) == 0:\\n        return len(s1)\\n    prev_row = list(range(len(s2) + 1))\\n    for i, c1 in enumerate(s1):\\n        curr_row = [i + 1]\\n        for j, c2 in enumerate(s2):\\n            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (c1 != c2)))\\n        prev_row = curr_row\\n    return prev_row[-1]\\n\\ndef build_name_to_id(rel_types):\\n    name_to_id = {}\\n    for rid, rname in rel_types.items():\\n        name_to_id[rname.lower().strip()] = rid\\n        name_to_id[rid.lower()] = rid\\n    return name_to_id\\n\\ndef docred_normalize_relation(rel_name, rel_types, name_to_id):\\n    rel_key = name_to_id.get(rel_name.lower().strip())\\n    if rel_key:\\n        return rel_key\\n    rel_tokens = set(rel_name.strip().lower().split())\\n    best_pid, best_overlap = None, 0.0\\n    for rid, rname in rel_types.items():\\n        rname_tokens = set(rname.lower().split())\\n        if rel_tokens and rname_tokens:\\n            ratio = len(rel_tokens & rname_tokens) / len(rel_tokens | rname_tokens)\\n            if ratio > 0.8 and ratio > best_overlap:\\n                best_overlap = ratio\\n                best_pid = rid\\n    if best_pid:\\n        return best_pid\\n    for rid, rname in rel_types.items():\\n        if _levenshtein(rel_name.strip().lower(), rname.lower()) <= 2:\\n            return rid\\n    return None\\n\\n# --- Per-sample stats ---\\n\\ndef scierc_sample_stats(rec, valid_entity_types):\\n    parsed = rec.get(\\\"parsed_output\\\")\\n    gold_ents = rec.get(\\\"gold_entities\\\", [])\\n    gold_rels = rec.get(\\\"gold_relations\\\", [])\\n\\n    gold_ent_set = set((e[\\\"text\\\"].lower().strip(), e[\\\"type\\\"]) for e in gold_ents)\\n    gold_rel_set = set((r[\\\"head\\\"].lower().strip(), r[\\\"tail\\\"].lower().strip(), r[\\\"type\\\"]) for r in gold_rels)\\n\\n    if parsed is None:\\n        return {\\\"ent_tp\\\": 0, \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": 0,\\n                \\\"rel_tp\\\": 0, \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": 0}\\n\\n    entities = parsed.get(\\\"entities\\\", [])\\n    relations = parsed.get(\\\"relations\\\", [])\\n\\n    pred_ent_set = set()\\n    for e in entities:\\n        nt = scierc_normalize_type(e.get(\\\"type\\\", \\\"\\\"), valid_entity_types)\\n        if nt:\\n            pred_ent_set.add((e.get(\\\"text\\\", \\\"\\\").lower().strip(), nt))\\n\\n    pred_rel_set = set((r.get(\\\"head\\\", \\\"\\\").lower().strip(), r.get(\\\"tail\\\", \\\"\\\").lower().strip(), r.get(\\\"type\\\", \\\"\\\")) for r in relations)\\n\\n    return {\\n        \\\"ent_tp\\\": len(gold_ent_set & pred_ent_set), \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": len(pred_ent_set),\\n        \\\"rel_tp\\\": len(gold_rel_set & pred_rel_set), \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": len(pred_rel_set),\\n    }\\n\\ndef docred_sample_stats(rec, rel_types, name_to_id):\\n    parsed = rec.get(\\\"parsed_output\\\")\\n    gold_ents = rec.get(\\\"gold_entities\\\", [])\\n    g\\n\\n... [截断: 输出过长，省略 7163 字符] ...\\n\\nids, f\\\"Doc ID mismatch in {setting_name}!\\\"\\n\\n        # Compute per-sample stats\\n        if cfg[\\\"dataset\\\"] == \\\"scierc\\\":\\n            unc_stats = [scierc_sample_stats(r, scierc_valid_types) for r in unc_records]\\n            con_stats = [scierc_sample_stats(r, scierc_valid_types) for r in con_records]\\n        else:\\n            unc_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in unc_records]\\n            con_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in con_records]\\n\\n        # Bootstrap CI for each config\\n        for label, stats in [(\\\"unconstrained\\\", unc_stats), (\\\"constrained\\\", con_stats)]:\\n            ent_ci = bootstrap_f1(extract_stats(stats, \\\"entity\\\"))\\n            rel_ci = bootstrap_f1(extract_stats(stats, \\\"relation\\\"))\\n            print(f\\\"  {label}: E-F1={100*ent_ci['point_estimate']:.2f}% [{100*ent_ci['ci_lower']:.2f}, {100*ent_ci['ci_upper']:.2f}], \\\"\\n                  f\\\"R-F1={100*rel_ci['point_estimate']:.2f}% [{100*rel_ci['ci_lower']:.2f}, {100*rel_ci['ci_upper']:.2f}]\\\")\\n\\n        # Paired test: constrained - unconstrained\\n        ent_test = paired_bootstrap_test(\\n            extract_stats(unc_stats, \\\"entity\\\"),\\n            extract_stats(con_stats, \\\"entity\\\"))\\n        rel_test = paired_bootstrap_test(\\n            extract_stats(unc_stats, \\\"relation\\\"),\\n            extract_stats(con_stats, \\\"relation\\\"))\\n\\n        print(f\\\"\\\\n  Paired test (constrained - unconstrained):\\\")\\n        print(f\\\"    ΔE-F1 = {100*ent_test['delta_point']:+.2f}pp  95%CI [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}]  p={ent_test['p_value']:.4f}\\\")\\n        print(f\\\"    ΔR-F1 = {100*rel_test['delta_point']:+.2f}pp  95%CI [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}]  p={rel_test['p_value']:.4f}\\\")\\n\\n        sig_rel = \\\"***\\\" if rel_test['p_value'] < 0.001 else \\\"**\\\" if rel_test['p_value'] < 0.01 else \\\"*\\\" if rel_test['p_value'] < 0.05 else \\\"n.s.\\\"\\n        sig_ent = \\\"***\\\" if ent_test['p_value'] < 0.001 else \\\"**\\\" if ent_test['p_value'] < 0.01 else \\\"*\\\" if ent_test['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"    Significance: E-F1 {sig_ent}, R-F1 {sig_rel}\\\")\\n\\n        all_results[setting_name] = {\\n            \\\"n_samples\\\": len(unc_records),\\n            \\\"ent_test\\\": ent_test,\\n            \\\"rel_test\\\": rel_test,\\n        }\\n\\n    # Summary table\\n    print(f\\\"\\\\n\\\\n{'='*70}\\\")\\n    print(\\\"  SUMMARY TABLE\\\")\\n    print(f\\\"{'='*70}\\\")\\n    print(f\\\"{'Setting':<22} {'ΔR-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\")\\n    print(f\\\"{'─'*70}\\\")\\n    for name, res in all_results.items():\\n        rt = res[\\\"rel_test\\\"]\\n        sig = \\\"***\\\" if rt['p_value'] < 0.001 else \\\"**\\\" if rt['p_value'] < 0.01 else \\\"*\\\" if rt['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"{name:<22} {100*rt['delta_point']:+.2f}        [{100*rt['ci_lower']:+.2f}, {100*rt['ci_upper']:+.2f}]    {rt['p_value']:.4f}     {sig}\\\")\\n\\n    print(f\\\"\\\\n{'Setting':<22} {'ΔE-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\")\\n    print(f\\\"{'─'*70}\\\")\\n    for name, res in all_results.items():\\n        et = res[\\\"ent_test\\\"]\\n        sig = \\\"***\\\" if et['p_value'] < 0.001 else \\\"**\\\" if et['p_value'] < 0.01 else \\\"*\\\" if et['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"{name:<22} {100*et['delta_point']:+.2f}        [{100*et['ci_lower']:+.2f}, {100*et['ci_upper']:+.2f}]    {et['p_value']:.4f}     {sig}\\\")\\n\\n    # Save JSON\\n    output = {\\n        \\\"settings\\\": {k: {\\n            \\\"n_samples\\\": v[\\\"n_samples\\\"],\\n            \\\"rel_f1\\\": v[\\\"rel_test\\\"],\\n            \\\"ent_f1\\\": v[\\\"ent_test\\\"],\\n        } for k, v in all_results.items()},\\n        \\\"metadata\\\": {\\n            \\\"n_bootstrap\\\": 10000,\\n            \\\"ci_method\\\": \\\"percentile\\\",\\n            \\\"ci_level\\\": 0.95,\\n            \\\"seed\\\": 42,\\n            \\\"test_type\\\": \\\"paired_bootstrap\\\",\\n            \\\"comparison\\\": \\\"constrained - unconstrained\\\",\\n        }\\n    }\\n    with open(\\\"outputs/bootstrap_ci_ft_composability.json\\\", \\\"w\\\") as f:\\n        json.dump(output, f, indent=2)\\n    print(f\\\"\\\\nJSON saved to outputs/bootstrap_ci_ft_composability.json\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "fa65c448-2cb1-4821-8b0b-edac8e3d09f0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Bootstrap CI for FT (LoRA) composability: constrained vs unconstrained.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport json\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\n\\\\n# --- Normalization (reuse from ZS script) ---\\\\n\\\\nSCIERC_TYPE_MAP = {\\\\n    \\\\\\\"otherscientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"other-scientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"other_scientific_term\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"scientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"other\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n}\\\\n\\\\ndef scierc_normalize_type(t, valid_types):\\\\n    t_lower = t.strip().lower().replace(\\\\\\\" \\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"-\\\\\\\", \\\\\\\"\\\\\\\")\\\\n    for vt in valid_types:\\\\n        if t_lower == vt.lower().replace(\\\\\\\" \\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"-\\\\\\\", \\\\\\\"\\\\\\\"):\\\\n            return vt\\\\n    if t_lower in SCIERC_TYPE_MAP:\\\\n        return SCIERC_TYPE_MAP[t_lower]\\\\n    return None\\\\n\\\\nDOCRED_VALID_ENTITY_TYPES = {\\\\\\\"PER\\\\\\\", \\\\\\\"ORG\\\\\\\", \\\\\\\"LOC\\\\\\\", \\\\\\\"TIME\\\\\\\", \\\\\\\"NUM\\\\\\\", \\\\\\\"MISC\\\\\\\"}\\\\nDOCRED_ENTITY_TYPE_ALIASES = {\\\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\\\n    'LOCATION': 'LOC',\\\\n    'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\\\n    'MISCELLANEOUS': 'MISC',\\\\n}\\\\n\\\\ndef docred_normalize_entity_type(raw_type):\\\\n    t = raw_type.strip().upper()\\\\n    return DOCRED_ENTITY_TYPE_ALIASES.get(t, t)\\\\n\\\\ndef _levenshtein(s1, s2):\\\\n    if len(s1) < len(s2):\\\\n        return _levenshtein(s2, s1)\\\\n    if len(s2) == 0:\\\\n        return len(s1)\\\\n    prev_row = list(range(len(s2) + 1))\\\\n    for i, c1 in enumerate(s1):\\\\n        curr_row = [i + 1]\\\\n        for j, c2 in enumerate(s2):\\\\n            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (c1 != c2)))\\\\n        prev_row = curr_row\\\\n    return prev_row[-1]\\\\n\\\\ndef build_name_to_id(rel_types):\\\\n    name_to_id = {}\\\\n    for rid, rname in rel_types.items():\\\\n        name_to_id[rname.lower().strip()] = rid\\\\n        name_to_id[rid.lower()] = rid\\\\n    return name_to_id\\\\n\\\\ndef docred_normalize_relation(rel_name, rel_types, name_to_id):\\\\n    rel_key = name_to_id.get(rel_name.lower().strip())\\\\n    if rel_key:\\\\n        return rel_key\\\\n    rel_tokens = set(rel_name.strip().lower().split())\\\\n    best_pid, best_overlap = None, 0.0\\\\n    for rid, rname in rel_types.items():\\\\n        rname_tokens = set(rname.lower().split())\\\\n        if rel_tokens and rname_tokens:\\\\n            ratio = len(rel_tokens & rname_tokens) / len(rel_tokens | rname_tokens)\\\\n            if ratio > 0.8 and ratio > best_overlap:\\\\n                best_overlap = ratio\\\\n                best_pid = rid\\\\n    if best_pid:\\\\n        return best_pid\\\\n    for rid, rname in rel_types.items():\\\\n        if _levenshtein(rel_name.strip().lower(), rname.lower()) <= 2:\\\\n            return rid\\\\n    return None\\\\n\\\\n# --- Per-sample stats ---\\\\n\\\\ndef scierc_sample_stats(rec, valid_entity_types):\\\\n    parsed = rec.get(\\\\\\\"parsed_output\\\\\\\")\\\\n    gold_ents = rec.get(\\\\\\\"gold_entities\\\\\\\", [])\\\\n    gold_rels = rec.get(\\\\\\\"gold_relations\\\\\\\", [])\\\\n\\\\n    gold_ent_set = set((e[\\\\\\\"text\\\\\\\"].lower().strip(), e[\\\\\\\"type\\\\\\\"]) for e in gold_ents)\\\\n    gold_rel_set = set((r[\\\\\\\"head\\\\\\\"].lower().strip(), r[\\\\\\\"tail\\\\\\\"].lower().strip(), r[\\\\\\\"type\\\\\\\"]) for r in gold_rels)\\\\n\\\\n    if parsed is None:\\\\n        return {\\\\\\\"ent_tp\\\\\\\": 0, \\\\\\\"ent_gold\\\\\\\": len(gold_ent_set), \\\\\\\"ent_pred\\\\\\\": 0,\\\\n                \\\\\\\"rel_tp\\\\\\\": 0, \\\\\\\"rel_gold\\\\\\\": len(gold_rel_set), \\\\\\\"rel_pred\\\\\\\": 0}\\\\n\\\\n    entities = parsed.get(\\\\\\\"entities\\\\\\\", [])\\\\n    relations = parsed.get(\\\\\\\"relations\\\\\\\", [])\\\\n\\\\n    pred_ent_set = set()\\\\n    for e in entities:\\\\n        nt = scierc_normalize_type(e.get(\\\\\\\"type\\\\\\\", \\\\\\\"\\\\\\\"), valid_entity_types)\\\\n        if nt:\\\\n            pred_ent_set.add((e.get(\\\\\\\"text\\\\\\\", \\\\\\\"\\\\\\\").lower().strip(), nt))\\\\n\\\\n    pred_rel_set = set((r.get(\\\\\\\"head\\\\\\\", \\\\\\\"\\\\\\\").lower().strip(), r.get(\\\\\\\"tail\\\\\\\", \\\\\\\"\\\\\\\").lower().strip(), r.get(\\\\\\\"type\\\\\\\", \\\\\\\"\\\\\\\")) for r in relations)\\\\n\\\\n    return {\\\\n        \\\\\\\"ent_tp\\\\\\\": len(gold_ent_set & pred_ent_set), \\\\\\\"ent_gold\\\\\\\": len(gold_ent_set), \\\\\\\"ent_pred\\\\\\\": len(pred_ent_set),\\\\n        \\\\\\\"rel_tp\\\\\\\": len(gold_rel_set & pred_rel_set), \\\\\\\"rel_gold\\\\\\\": len(gold_rel_set), \\\\\\\"rel_pred\\\\\\\": len(pred_rel_set),\\\\n    }\\\\n\\\\ndef docred_sample_stats(rec, rel_types, name_to_id):\\\\n    parsed = rec.get(\\\\\\\"parsed_output\\\\\\\")\\\\n    gold_ents = rec.get(\\\\\\\"gold_entities\\\\\\\", [])\\\\n    g\\\\n\\\\n... [截断: 输出过长，省略 7163 字符] ...\\\\n\\\\nids, f\\\\\\\"Doc ID mismatch in {setting_name}!\\\\\\\"\\\\n\\\\n        # Compute per-sample stats\\\\n        if cfg[\\\\\\\"dataset\\\\\\\"] == \\\\\\\"scierc\\\\\\\":\\\\n            unc_stats = [scierc_sample_stats(r, scierc_valid_types) for r in unc_records]\\\\n            con_stats = [scierc_sample_stats(r, scierc_valid_types) for r in con_records]\\\\n        else:\\\\n            unc_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in unc_records]\\\\n            con_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in con_records]\\\\n\\\\n        # Bootstrap CI for each config\\\\n        for label, stats in [(\\\\\\\"unconstrained\\\\\\\", unc_stats), (\\\\\\\"constrained\\\\\\\", con_stats)]:\\\\n            ent_ci = bootstrap_f1(extract_stats(stats, \\\\\\\"entity\\\\\\\"))\\\\n            rel_ci = bootstrap_f1(extract_stats(stats, \\\\\\\"relation\\\\\\\"))\\\\n            print(f\\\\\\\"  {label}: E-F1={100*ent_ci['point_estimate']:.2f}% [{100*ent_ci['ci_lower']:.2f}, {100*ent_ci['ci_upper']:.2f}], \\\\\\\"\\\\n                  f\\\\\\\"R-F1={100*rel_ci['point_estimate']:.2f}% [{100*rel_ci['ci_lower']:.2f}, {100*rel_ci['ci_upper']:.2f}]\\\\\\\")\\\\n\\\\n        # Paired test: constrained - unconstrained\\\\n        ent_test = paired_bootstrap_test(\\\\n            extract_stats(unc_stats, \\\\\\\"entity\\\\\\\"),\\\\n            extract_stats(con_stats, \\\\\\\"entity\\\\\\\"))\\\\n        rel_test = paired_bootstrap_test(\\\\n            extract_stats(unc_stats, \\\\\\\"relation\\\\\\\"),\\\\n            extract_stats(con_stats, \\\\\\\"relation\\\\\\\"))\\\\n\\\\n        print(f\\\\\\\"\\\\\\\\n  Paired test (constrained - unconstrained):\\\\\\\")\\\\n        print(f\\\\\\\"    ΔE-F1 = {100*ent_test['delta_point']:+.2f}pp  95%CI [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}]  p={ent_test['p_value']:.4f}\\\\\\\")\\\\n        print(f\\\\\\\"    ΔR-F1 = {100*rel_test['delta_point']:+.2f}pp  95%CI [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}]  p={rel_test['p_value']:.4f}\\\\\\\")\\\\n\\\\n        sig_rel = \\\\\\\"***\\\\\\\" if rel_test['p_value'] < 0.001 else \\\\\\\"**\\\\\\\" if rel_test['p_value'] < 0.01 else \\\\\\\"*\\\\\\\" if rel_test['p_value'] < 0.05 else \\\\\\\"n.s.\\\\\\\"\\\\n        sig_ent = \\\\\\\"***\\\\\\\" if ent_test['p_value'] < 0.001 else \\\\\\\"**\\\\\\\" if ent_test['p_value'] < 0.01 else \\\\\\\"*\\\\\\\" if ent_test['p_value'] < 0.05 else \\\\\\\"n.s.\\\\\\\"\\\\n        print(f\\\\\\\"    Significance: E-F1 {sig_ent}, R-F1 {sig_rel}\\\\\\\")\\\\n\\\\n        all_results[setting_name] = {\\\\n            \\\\\\\"n_samples\\\\\\\": len(unc_records),\\\\n            \\\\\\\"ent_test\\\\\\\": ent_test,\\\\n            \\\\\\\"rel_test\\\\\\\": rel_test,\\\\n        }\\\\n\\\\n    # Summary table\\\\n    print(f\\\\\\\"\\\\\\\\n\\\\\\\\n{'='*70}\\\\\\\")\\\\n    print(\\\\\\\"  SUMMARY TABLE\\\\\\\")\\\\n    print(f\\\\\\\"{'='*70}\\\\\\\")\\\\n    print(f\\\\\\\"{'Setting':<22} {'ΔR-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\\\\\")\\\\n    print(f\\\\\\\"{'─'*70}\\\\\\\")\\\\n    for name, res in all_results.items():\\\\n        rt = res[\\\\\\\"rel_test\\\\\\\"]\\\\n        sig = \\\\\\\"***\\\\\\\" if rt['p_value'] < 0.001 else \\\\\\\"**\\\\\\\" if rt['p_value'] < 0.01 else \\\\\\\"*\\\\\\\" if rt['p_value'] < 0.05 else \\\\\\\"n.s.\\\\\\\"\\\\n        print(f\\\\\\\"{name:<22} {100*rt['delta_point']:+.2f}        [{100*rt['ci_lower']:+.2f}, {100*rt['ci_upper']:+.2f}]    {rt['p_value']:.4f}     {sig}\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"\\\\\\\\n{'Setting':<22} {'ΔE-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\\\\\")\\\\n    print(f\\\\\\\"{'─'*70}\\\\\\\")\\\\n    for name, res in all_results.items():\\\\n        et = res[\\\\\\\"ent_test\\\\\\\"]\\\\n        sig = \\\\\\\"***\\\\\\\" if et['p_value'] < 0.001 else \\\\\\\"**\\\\\\\" if et['p_value'] < 0.01 else \\\\\\\"*\\\\\\\" if et['p_value'] < 0.05 else \\\\\\\"n.s.\\\\\\\"\\\\n        print(f\\\\\\\"{name:<22} {100*et['delta_point']:+.2f}        [{100*et['ci_lower']:+.2f}, {100*et['ci_upper']:+.2f}]    {et['p_value']:.4f}     {sig}\\\\\\\")\\\\n\\\\n    # Save JSON\\\\n    output = {\\\\n        \\\\\\\"settings\\\\\\\": {k: {\\\\n            \\\\\\\"n_samples\\\\\\\": v[\\\\\\\"n_samples\\\\\\\"],\\\\n            \\\\\\\"rel_f1\\\\\\\": v[\\\\\\\"rel_test\\\\\\\"],\\\\n            \\\\\\\"ent_f1\\\\\\\": v[\\\\\\\"ent_test\\\\\\\"],\\\\n        } for k, v in all_results.items()},\\\\n        \\\\\\\"metadata\\\\\\\": {\\\\n            \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n            \\\\\\\"ci_method\\\\\\\": \\\\\\\"percentile\\\\\\\",\\\\n            \\\\\\\"ci_level\\\\\\\": 0.95,\\\\n            \\\\\\\"seed\\\\\\\": 42,\\\\n            \\\\\\\"test_type\\\\\\\": \\\\\\\"paired_bootstrap\\\\\\\",\\\\n            \\\\\\\"comparison\\\\\\\": \\\\\\\"constrained - unconstrained\\\\\\\",\\\\n        }\\\\n    }\\\\n    with open(\\\\\\\"outputs/bootstrap_ci_ft_composability.json\\\\\\\", \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(output, f, indent=2)\\\\n    print(f\\\\\\\"\\\\\\\\nJSON saved to outputs/bootstrap_ci_ft_composability.json\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Bootstrap CI for FT (LoRA) composability: constrained vs unconstrained.\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\nfrom pathlib import Path\\n\\n# --- Normalization (reuse from ZS script) ---\\n\\nSCIERC_TYPE_MAP = {\\n    \\\"otherscientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other-scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other_scientific_term\\\": \\\"OtherScientificTerm\\\",\\n    \\\"scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other\\\": \\\"OtherScientificTerm\\\",\\n}\\n\\ndef scierc_normalize_type(t, valid_types):\\n    t_lower = t.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vt in valid_types:\\n        if t_lower == vt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vt\\n    if t_lower in SCIERC_TYPE_MAP:\\n        return SCIERC_TYPE_MAP[t_lower]\\n    return None\\n\\nDOCRED_VALID_ENTITY_TYPES = {\\\"PER\\\", \\\"ORG\\\", \\\"LOC\\\", \\\"TIME\\\", \\\"NUM\\\", \\\"MISC\\\"}\\nDOCRED_ENTITY_TYPE_ALIASES = {\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC',\\n    'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\ndef docred_normalize_entity_type(raw_type):\\n    t = raw_type.strip().upper()\\n    return DOCRED_ENTITY_TYPE_ALIASES.get(t, t)\\n\\ndef _levenshtein(s1, s2):\\n    if len(s1) < len(s2):\\n        return _levenshtein(s2, s1)\\n    if len(s2) == 0:\\n        return len(s1)\\n    prev_row = list(range(len(s2) + 1))\\n    for i, c1 in enumerate(s1):\\n        curr_row = [i + 1]\\n        for j, c2 in enumerate(s2):\\n            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (c1 != c2)))\\n        prev_row = curr_row\\n    return prev_row[-1]\\n\\ndef build_name_to_id(rel_types):\\n    name_to_id = {}\\n    for rid, rname in rel_types.items():\\n        name_to_id[rname.lower().strip()] = rid\\n        name_to_id[rid.lower()] = rid\\n    return name_to_id\\n\\ndef docred_normalize_relation(rel_name, rel_types, name_to_id):\\n    rel_key = name_to_id.get(rel_name.lower().strip())\\n    if rel_key:\\n        return rel_key\\n    rel_tokens = set(rel_name.strip().lower().split())\\n    best_pid, best_overlap = None, 0.0\\n    for rid, rname in rel_types.items():\\n        rname_tokens = set(rname.lower().split())\\n        if rel_tokens and rname_tokens:\\n            ratio = len(rel_tokens & rname_tokens) / len(rel_tokens | rname_tokens)\\n            if ratio > 0.8 and ratio > best_overlap:\\n                best_overlap = ratio\\n                best_pid = rid\\n    if best_pid:\\n        return best_pid\\n    for rid, rname in rel_types.items():\\n        if _levenshtein(rel_name.strip().lower(), rname.lower()) <= 2:\\n            return rid\\n    return None\\n\\n# --- Per-sample stats ---\\n\\ndef scierc_sample_stats(rec, valid_entity_types):\\n    parsed = rec.get(\\\"parsed_output\\\")\\n    gold_ents = rec.get(\\\"gold_entities\\\", [])\\n    gold_rels = rec.get(\\\"gold_relations\\\", [])\\n\\n    gold_ent_set = set((e[\\\"text\\\"].lower().strip(), e[\\\"type\\\"]) for e in gold_ents)\\n    gold_rel_set = set((r[\\\"head\\\"].lower().strip(), r[\\\"tail\\\"].lower().strip(), r[\\\"type\\\"]) for r in gold_rels)\\n\\n    if parsed is None:\\n        return {\\\"ent_tp\\\": 0, \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": 0,\\n                \\\"rel_tp\\\": 0, \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": 0}\\n\\n    entities = parsed.get(\\\"entities\\\", [])\\n    relations = parsed.get(\\\"relations\\\", [])\\n\\n    pred_ent_set = set()\\n    for e in entities:\\n        nt = scierc_normalize_type(e.get(\\\"type\\\", \\\"\\\"), valid_entity_types)\\n        if nt:\\n            pred_ent_set.add((e.get(\\\"text\\\", \\\"\\\").lower().strip(), nt))\\n\\n    pred_rel_set = set((r.get(\\\"head\\\", \\\"\\\").lower().strip(), r.get(\\\"tail\\\", \\\"\\\").lower().strip(), r.get(\\\"type\\\", \\\"\\\")) for r in relations)\\n\\n    return {\\n        \\\"ent_tp\\\": len(gold_ent_set & pred_ent_set), \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": len(pred_ent_set),\\n        \\\"rel_tp\\\": len(gold_rel_set & pred_rel_set), \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": len(pred_rel_set),\\n    }\\n\\ndef docred_sample_stats(rec, rel_types, name_to_id):\\n    parsed = rec.get(\\\"parsed_output\\\")\\n    gold_ents = rec.get(\\\"gold_entities\\\", [])\\n    g\\n\\n... [截断: 输出过长，省略 7163 字符] ...\\n\\nids, f\\\"Doc ID mismatch in {setting_name}!\\\"\\n\\n        # Compute per-sample stats\\n        if cfg[\\\"dataset\\\"] == \\\"scierc\\\":\\n            unc_stats = [scierc_sample_stats(r, scierc_valid_types) for r in unc_records]\\n            con_stats = [scierc_sample_stats(r, scierc_valid_types) for r in con_records]\\n        else:\\n            unc_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in unc_records]\\n            con_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in con_records]\\n\\n        # Bootstrap CI for each config\\n        for label, stats in [(\\\"unconstrained\\\", unc_stats), (\\\"constrained\\\", con_stats)]:\\n            ent_ci = bootstrap_f1(extract_stats(stats, \\\"entity\\\"))\\n            rel_ci = bootstrap_f1(extract_stats(stats, \\\"relation\\\"))\\n            print(f\\\"  {label}: E-F1={100*ent_ci['point_estimate']:.2f}% [{100*ent_ci['ci_lower']:.2f}, {100*ent_ci['ci_upper']:.2f}], \\\"\\n                  f\\\"R-F1={100*rel_ci['point_estimate']:.2f}% [{100*rel_ci['ci_lower']:.2f}, {100*rel_ci['ci_upper']:.2f}]\\\")\\n\\n        # Paired test: constrained - unconstrained\\n        ent_test = paired_bootstrap_test(\\n            extract_stats(unc_stats, \\\"entity\\\"),\\n            extract_stats(con_stats, \\\"entity\\\"))\\n        rel_test = paired_bootstrap_test(\\n            extract_stats(unc_stats, \\\"relation\\\"),\\n            extract_stats(con_stats, \\\"relation\\\"))\\n\\n        print(f\\\"\\\\n  Paired test (constrained - unconstrained):\\\")\\n        print(f\\\"    ΔE-F1 = {100*ent_test['delta_point']:+.2f}pp  95%CI [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}]  p={ent_test['p_value']:.4f}\\\")\\n        print(f\\\"    ΔR-F1 = {100*rel_test['delta_point']:+.2f}pp  95%CI [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}]  p={rel_test['p_value']:.4f}\\\")\\n\\n        sig_rel = \\\"***\\\" if rel_test['p_value'] < 0.001 else \\\"**\\\" if rel_test['p_value'] < 0.01 else \\\"*\\\" if rel_test['p_value'] < 0.05 else \\\"n.s.\\\"\\n        sig_ent = \\\"***\\\" if ent_test['p_value'] < 0.001 else \\\"**\\\" if ent_test['p_value'] < 0.01 else \\\"*\\\" if ent_test['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"    Significance: E-F1 {sig_ent}, R-F1 {sig_rel}\\\")\\n\\n        all_results[setting_name] = {\\n            \\\"n_samples\\\": len(unc_records),\\n            \\\"ent_test\\\": ent_test,\\n            \\\"rel_test\\\": rel_test,\\n        }\\n\\n    # Summary table\\n    print(f\\\"\\\\n\\\\n{'='*70}\\\")\\n    print(\\\"  SUMMARY TABLE\\\")\\n    print(f\\\"{'='*70}\\\")\\n    print(f\\\"{'Setting':<22} {'ΔR-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\")\\n    print(f\\\"{'─'*70}\\\")\\n    for name, res in all_results.items():\\n        rt = res[\\\"rel_test\\\"]\\n        sig = \\\"***\\\" if rt['p_value'] < 0.001 else \\\"**\\\" if rt['p_value'] < 0.01 else \\\"*\\\" if rt['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"{name:<22} {100*rt['delta_point']:+.2f}        [{100*rt['ci_lower']:+.2f}, {100*rt['ci_upper']:+.2f}]    {rt['p_value']:.4f}     {sig}\\\")\\n\\n    print(f\\\"\\\\n{'Setting':<22} {'ΔE-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\")\\n    print(f\\\"{'─'*70}\\\")\\n    for name, res in all_results.items():\\n        et = res[\\\"ent_test\\\"]\\n        sig = \\\"***\\\" if et['p_value'] < 0.001 else \\\"**\\\" if et['p_value'] < 0.01 else \\\"*\\\" if et['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"{name:<22} {100*et['delta_point']:+.2f}        [{100*et['ci_lower']:+.2f}, {100*et['ci_upper']:+.2f}]    {et['p_value']:.4f}     {sig}\\\")\\n\\n    # Save JSON\\n    output = {\\n        \\\"settings\\\": {k: {\\n            \\\"n_samples\\\": v[\\\"n_samples\\\"],\\n            \\\"rel_f1\\\": v[\\\"rel_test\\\"],\\n            \\\"ent_f1\\\": v[\\\"ent_test\\\"],\\n        } for k, v in all_results.items()},\\n        \\\"metadata\\\": {\\n            \\\"n_bootstrap\\\": 10000,\\n            \\\"ci_method\\\": \\\"percentile\\\",\\n            \\\"ci_level\\\": 0.95,\\n            \\\"seed\\\": 42,\\n            \\\"test_type\\\": \\\"paired_bootstrap\\\",\\n            \\\"comparison\\\": \\\"constrained - unconstrained\\\",\\n        }\\n    }\\n    with open(\\\"outputs/bootstrap_ci_ft_composability.json\\\", \\\"w\\\") as f:\\n        json.dump(output, f, indent=2)\\n    print(f\\\"\\\\nJSON saved to outputs/bootstrap_ci_ft_composability.json\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01FVJditHWZRKsyrn4mmiRjH`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/compute_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "6404fe22-6401-46d3-a301-3ef85cf46fb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CtnimN6txt9wX8GVcUDAN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 26372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
      },
      "output_tokens": 60,
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SAUUXm48ZDcmf29XzJg563`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/compute_bootstrap_ci_llama.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "a17a7493-4f9c-475c-aab0-6cd1541a0477",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CtnimN6txt9wX8GVcUDAN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 26372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
      },
      "output_tokens": 60,
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

_source line 15 · 2026-05-17T14:12:04.596Z_

<details><summary>↩ Tool result · `toolu_01FVJditHWZRKsyrn4mmiRjH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Compute bootstrap confidence intervals for SciERC and DocRED experiments.\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\nfrom pathlib import Path\\n\\n# --- SciERC normalization (from violation_checker.py) ---\\n\\nSCIERC_TYPE_MAP = {\\n    \\\"otherscientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other-scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other_scientific_term\\\": \\\"OtherScientificTerm\\\",\\n    \\\"scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other\\\": \\\"OtherScientificTerm\\\",\\n}\\n\\ndef scierc_normalize_type(t, valid_types):\\n    t_lower = t.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vt in valid_types:\\n        if t_lower == vt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vt\\n    if t_lower in SCIERC_TYPE_MAP:\\n        return SCIERC_TYPE_MAP[t_lower]\\n    return None\\n\\n# --- DocRED normalization (from violation_checker_docred.py) ---\\n\\nDOCRED_VALID_ENTITY_TYPES = {\\\"PER\\\", \\\"ORG\\\", \\\"LOC\\\", \\\"TIME\\\", \\\"NUM\\\", \\\"MISC\\\"}\\n\\nDOCRED_ENTITY_TYPE_ALIASES = {\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC',\\n    'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\ndef docred_normalize_entity_type(raw_type):\\n    t = raw_type.strip().upper()\\n    return DOCRED_ENTITY_TYPE_ALIASES.get(t, t)\\n\\ndef _levenshtein(s1, s2):\\n    if len(s1) < len(s2):\\n        return _levenshtein(s2, s1)\\n    if len(s2) == 0:\\n        return len(s1)\\n    prev_row = list(range(len(s2) + 1))\\n    for i, c1 in enumerate(s1):\\n        curr_row = [i + 1]\\n        for j, c2 in enumerate(s2):\\n            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (c1 != c2)))\\n        prev_row = curr_row\\n    return prev_row[-1]\\n\\ndef build_name_to_id(rel_types):\\n    name_to_id = {}\\n    for rid, rname in rel_types.items():\\n        name_to_id[rname.lower().strip()] = rid\\n        name_to_id[rid.lower()] = rid\\n    return name_to_id\\n\\ndef docred_normalize_relation(rel_name, rel_types, name_to_id):\\n    rel_key = name_to_id.get(rel_name.lower().strip())\\n    if rel_key:\\n        return rel_key\\n    rel_tokens = set(rel_name.strip().lower().split())\\n    best_pid, best_overlap = None, 0.0\\n    for rid, rname in rel_types.items():\\n        rname_tokens = set(rname.lower().split())\\n        if rel_tokens and rname_tokens:\\n            ratio = len(rel_tokens & rname_tokens) / len(rel_tokens | rname_tokens)\\n            if ratio > 0.8 and ratio > best_overlap:\\n                best_overlap = ratio\\n                best_pid = rid\\n    if best_pid:\\n        return best_pid\\n    for rid, rname in rel_types.items():\\n        if _levenshtein(rel_name.strip().lower(), rname.lower()) <= 2:\\n            return rid\\n    return None\\n\\n# --- Per-sample stats ---\\n\\ndef scierc_sample_stats(rec, valid_entity_types):\\n    parsed = rec.get(\\\"parsed_output\\\")\\n    gold_ents = rec.get(\\\"gold_entities\\\", [])\\n    gold_rels = rec.get(\\\"gold_relations\\\", [])\\n\\n    gold_ent_set = set((e[\\\"text\\\"].lower().strip(), e[\\\"type\\\"]) for e in gold_ents)\\n    gold_rel_set = set((r[\\\"head\\\"].lower().strip(), r[\\\"tail\\\"].lower().strip(), r[\\\"type\\\"]) for r in gold_rels)\\n\\n    if parsed is None:\\n        return {\\\"ent_tp\\\": 0, \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": 0,\\n                \\\"rel_tp\\\": 0, \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": 0}\\n\\n    entities = parsed.get(\\\"entities\\\", [])\\n    relations = parsed.get(\\\"relations\\\", [])\\n\\n    pred_ent_set = set()\\n    for e in entities:\\n        nt = scierc_normalize_type(e.get(\\\"type\\\", \\\"\\\"), valid_entity_types)\\n        if nt:\\n            pred_ent_set.add((e.get(\\\"text\\\", \\\"\\\").lower().strip(), nt))\\n\\n    pred_rel_set = set((r.get(\\\"head\\\", \\\"\\\").lower().strip(), r.get(\\\"tail\\\", \\\"\\\").lower().strip(), r.get(\\\"type\\\", \\\"\\\")) for r in relations)\\n\\n    return {\\n        \\\"ent_tp\\\": len(gold_ent_set & pred_ent_set), \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": len(pred_ent_set),\\n        \\\"rel_tp\\\": len(gold_rel_set & pred_rel_set), \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": len(pred_rel_set),\\n    }\\n\\ndef docred_sample_stats(rec, rel_types, name_to_id):\\n    pa\\n\\n... [截断: 输出过长，省略 6326 字符] ...\\n\\ne)\\n\\n    per_config = {}\\n    for name, stats in all_stats.items():\\n        ent_ci = bootstrap_f1(extract_stats(stats, \\\"entity\\\"))\\n        rel_ci = bootstrap_f1(extract_stats(stats, \\\"relation\\\"))\\n        per_config[name] = {\\\"ent_f1\\\": ent_ci, \\\"rel_f1\\\": rel_ci}\\n        print(f\\\"  {name} CI: Ent F1={100*ent_ci['point_estimate']:.2f}% [{100*ent_ci['ci_lower']:.2f}, {100*ent_ci['ci_upper']:.2f}], \\\"\\n              f\\\"Rel F1={100*rel_ci['point_estimate']:.2f}% [{100*rel_ci['ci_lower']:.2f}, {100*rel_ci['ci_upper']:.2f}]\\\")\\n\\n    comparisons = {}\\n    pairs = [\\n        (\\\"unconstrained\\\", \\\"grammar_only\\\"),\\n        (\\\"unconstrained\\\", \\\"semantic_only\\\"),\\n        (\\\"unconstrained\\\", \\\"full_s1\\\"),\\n        (\\\"grammar_only\\\", \\\"full_s1\\\"),\\n        (\\\"semantic_only\\\", \\\"full_s1\\\"),\\n    ]\\n    print(f\\\"\\\\n  Paired bootstrap tests (B - A):\\\")\\n    for cfg_a, cfg_b in pairs:\\n        if cfg_a not in all_stats or cfg_b not in all_stats:\\n            continue\\n        ent_test = paired_bootstrap_test(extract_stats(all_stats[cfg_a], \\\"entity\\\"),\\n                                          extract_stats(all_stats[cfg_b], \\\"entity\\\"))\\n        rel_test = paired_bootstrap_test(extract_stats(all_stats[cfg_a], \\\"relation\\\"),\\n                                          extract_stats(all_stats[cfg_b], \\\"relation\\\"))\\n        key = f\\\"{cfg_a}_vs_{cfg_b}\\\"\\n        comparisons[key] = {\\\"ent_f1_delta\\\": ent_test, \\\"rel_f1_delta\\\": rel_test}\\n        print(f\\\"  {key}:\\\")\\n        print(f\\\"    Ent ΔF1={100*ent_test['delta_point']:+.2f}pp [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}] p={ent_test['p_value']:.4f}\\\")\\n        print(f\\\"    Rel ΔF1={100*rel_test['delta_point']:+.2f}pp [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}] p={rel_test['p_value']:.4f}\\\")\\n\\n    return {\\\"per_config\\\": per_config, \\\"comparisons\\\": comparisons}\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    import os\\n    os.chdir(\\\"/root/schema_semantic_constrained_ie\\\")\\n\\n    # SciERC\\n    with open(\\\"ontology_constraints.json\\\") as f:\\n        scierc_constraints = json.load(f)\\n    scierc_valid_types = scierc_constraints[\\\"entity_types\\\"]\\n\\n    scierc_configs = {\\n        \\\"unconstrained\\\": \\\"outputs/phase2_scierc_unconstrained.jsonl\\\",\\n        \\\"grammar_only\\\": \\\"outputs/phase2_scierc_grammar_only.jsonl\\\",\\n        \\\"semantic_only\\\": \\\"outputs/phase2_scierc_semantic_only_v2.jsonl\\\",\\n        \\\"full_s1\\\": \\\"outputs/phase2_scierc_full_s1_v2.jsonl\\\",\\n    }\\n    scierc_results = run_dataset(\\\"SciERC\\\", scierc_configs, scierc_sample_stats, (scierc_valid_types,))\\n\\n    # DocRED\\n    with open(\\\"data/docred/ontology_constraints_docred.json\\\") as f:\\n        docred_constraints = json.load(f)\\n    docred_rel_types = docred_constraints.get(\\\"relation_types\\\", {})\\n    docred_name_to_id = build_name_to_id(docred_rel_types)\\n\\n    docred_configs = {\\n        \\\"unconstrained\\\": \\\"outputs/docred_unconstrained.jsonl\\\",\\n        \\\"grammar_only\\\": \\\"outputs/docred_grammar_only.jsonl\\\",\\n        \\\"semantic_only\\\": \\\"outputs/docred_semantic_only.jsonl\\\",\\n        \\\"full_s1\\\": \\\"outputs/docred_full_s1.jsonl\\\",\\n    }\\n    docred_results = run_dataset(\\\"DocRED\\\", docred_configs, docred_sample_stats, (docred_rel_types, docred_name_to_id))\\n\\n    # Save results\\n    def round_recursive(obj, decimals=6):\\n        if isinstance(obj, float):\\n            return round(obj, decimals)\\n        if isinstance(obj, dict):\\n            return {k: round_recursive(v, decimals) for k, v in obj.items()}\\n        if isinstance(obj, list):\\n            return [round_recursive(v, decimals) for v in obj]\\n        return obj\\n\\n    results = {\\n        \\\"scierc\\\": round_recursive(scierc_results),\\n        \\\"docred\\\": round_recursive(docred_results),\\n        \\\"metadata\\\": {\\n            \\\"n_bootstrap\\\": 10000,\\n            \\\"ci_method\\\": \\\"percentile\\\",\\n            \\\"ci_level\\\": 0.95,\\n            \\\"seed\\\": 42,\\n            \\\"resample_unit\\\": \\\"sentence (SciERC) / document (DocRED)\\\",\\n        }\\n    }\\n\\n    output_path = \\\"outputs/bootstrap_ci_results_v2.json\\\"\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(results, f, indent=2)\\n    print(f\\\"\\\\nResults saved to {output_path}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "db714c2b-426c-4880-955e-d9f7f9c5360f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Compute bootstrap confidence intervals for SciERC and DocRED experiments.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport json\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\n\\\\n# --- SciERC normalization (from violation_checker.py) ---\\\\n\\\\nSCIERC_TYPE_MAP = {\\\\n    \\\\\\\"otherscientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"other-scientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"other_scientific_term\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"scientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"other\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n}\\\\n\\\\ndef scierc_normalize_type(t, valid_types):\\\\n    t_lower = t.strip().lower().replace(\\\\\\\" \\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"-\\\\\\\", \\\\\\\"\\\\\\\")\\\\n    for vt in valid_types:\\\\n        if t_lower == vt.lower().replace(\\\\\\\" \\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"-\\\\\\\", \\\\\\\"\\\\\\\"):\\\\n            return vt\\\\n    if t_lower in SCIERC_TYPE_MAP:\\\\n        return SCIERC_TYPE_MAP[t_lower]\\\\n    return None\\\\n\\\\n# --- DocRED normalization (from violation_checker_docred.py) ---\\\\n\\\\nDOCRED_VALID_ENTITY_TYPES = {\\\\\\\"PER\\\\\\\", \\\\\\\"ORG\\\\\\\", \\\\\\\"LOC\\\\\\\", \\\\\\\"TIME\\\\\\\", \\\\\\\"NUM\\\\\\\", \\\\\\\"MISC\\\\\\\"}\\\\n\\\\nDOCRED_ENTITY_TYPE_ALIASES = {\\\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\\\n    'LOCATION': 'LOC',\\\\n    'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\\\n    'MISCELLANEOUS': 'MISC',\\\\n}\\\\n\\\\ndef docred_normalize_entity_type(raw_type):\\\\n    t = raw_type.strip().upper()\\\\n    return DOCRED_ENTITY_TYPE_ALIASES.get(t, t)\\\\n\\\\ndef _levenshtein(s1, s2):\\\\n    if len(s1) < len(s2):\\\\n        return _levenshtein(s2, s1)\\\\n    if len(s2) == 0:\\\\n        return len(s1)\\\\n    prev_row = list(range(len(s2) + 1))\\\\n    for i, c1 in enumerate(s1):\\\\n        curr_row = [i + 1]\\\\n        for j, c2 in enumerate(s2):\\\\n            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (c1 != c2)))\\\\n        prev_row = curr_row\\\\n    return prev_row[-1]\\\\n\\\\ndef build_name_to_id(rel_types):\\\\n    name_to_id = {}\\\\n    for rid, rname in rel_types.items():\\\\n        name_to_id[rname.lower().strip()] = rid\\\\n        name_to_id[rid.lower()] = rid\\\\n    return name_to_id\\\\n\\\\ndef docred_normalize_relation(rel_name, rel_types, name_to_id):\\\\n    rel_key = name_to_id.get(rel_name.lower().strip())\\\\n    if rel_key:\\\\n        return rel_key\\\\n    rel_tokens = set(rel_name.strip().lower().split())\\\\n    best_pid, best_overlap = None, 0.0\\\\n    for rid, rname in rel_types.items():\\\\n        rname_tokens = set(rname.lower().split())\\\\n        if rel_tokens and rname_tokens:\\\\n            ratio = len(rel_tokens & rname_tokens) / len(rel_tokens | rname_tokens)\\\\n            if ratio > 0.8 and ratio > best_overlap:\\\\n                best_overlap = ratio\\\\n                best_pid = rid\\\\n    if best_pid:\\\\n        return best_pid\\\\n    for rid, rname in rel_types.items():\\\\n        if _levenshtein(rel_name.strip().lower(), rname.lower()) <= 2:\\\\n            return rid\\\\n    return None\\\\n\\\\n# --- Per-sample stats ---\\\\n\\\\ndef scierc_sample_stats(rec, valid_entity_types):\\\\n    parsed = rec.get(\\\\\\\"parsed_output\\\\\\\")\\\\n    gold_ents = rec.get(\\\\\\\"gold_entities\\\\\\\", [])\\\\n    gold_rels = rec.get(\\\\\\\"gold_relations\\\\\\\", [])\\\\n\\\\n    gold_ent_set = set((e[\\\\\\\"text\\\\\\\"].lower().strip(), e[\\\\\\\"type\\\\\\\"]) for e in gold_ents)\\\\n    gold_rel_set = set((r[\\\\\\\"head\\\\\\\"].lower().strip(), r[\\\\\\\"tail\\\\\\\"].lower().strip(), r[\\\\\\\"type\\\\\\\"]) for r in gold_rels)\\\\n\\\\n    if parsed is None:\\\\n        return {\\\\\\\"ent_tp\\\\\\\": 0, \\\\\\\"ent_gold\\\\\\\": len(gold_ent_set), \\\\\\\"ent_pred\\\\\\\": 0,\\\\n                \\\\\\\"rel_tp\\\\\\\": 0, \\\\\\\"rel_gold\\\\\\\": len(gold_rel_set), \\\\\\\"rel_pred\\\\\\\": 0}\\\\n\\\\n    entities = parsed.get(\\\\\\\"entities\\\\\\\", [])\\\\n    relations = parsed.get(\\\\\\\"relations\\\\\\\", [])\\\\n\\\\n    pred_ent_set = set()\\\\n    for e in entities:\\\\n        nt = scierc_normalize_type(e.get(\\\\\\\"type\\\\\\\", \\\\\\\"\\\\\\\"), valid_entity_types)\\\\n        if nt:\\\\n            pred_ent_set.add((e.get(\\\\\\\"text\\\\\\\", \\\\\\\"\\\\\\\").lower().strip(), nt))\\\\n\\\\n    pred_rel_set = set((r.get(\\\\\\\"head\\\\\\\", \\\\\\\"\\\\\\\").lower().strip(), r.get(\\\\\\\"tail\\\\\\\", \\\\\\\"\\\\\\\").lower().strip(), r.get(\\\\\\\"type\\\\\\\", \\\\\\\"\\\\\\\")) for r in relations)\\\\n\\\\n    return {\\\\n        \\\\\\\"ent_tp\\\\\\\": len(gold_ent_set & pred_ent_set), \\\\\\\"ent_gold\\\\\\\": len(gold_ent_set), \\\\\\\"ent_pred\\\\\\\": len(pred_ent_set),\\\\n        \\\\\\\"rel_tp\\\\\\\": len(gold_rel_set & pred_rel_set), \\\\\\\"rel_gold\\\\\\\": len(gold_rel_set), \\\\\\\"rel_pred\\\\\\\": len(pred_rel_set),\\\\n    }\\\\n\\\\ndef docred_sample_stats(rec, rel_types, name_to_id):\\\\n    pa\\\\n\\\\n... [截断: 输出过长，省略 6326 字符] ...\\\\n\\\\ne)\\\\n\\\\n    per_config = {}\\\\n    for name, stats in all_stats.items():\\\\n        ent_ci = bootstrap_f1(extract_stats(stats, \\\\\\\"entity\\\\\\\"))\\\\n        rel_ci = bootstrap_f1(extract_stats(stats, \\\\\\\"relation\\\\\\\"))\\\\n        per_config[name] = {\\\\\\\"ent_f1\\\\\\\": ent_ci, \\\\\\\"rel_f1\\\\\\\": rel_ci}\\\\n        print(f\\\\\\\"  {name} CI: Ent F1={100*ent_ci['point_estimate']:.2f}% [{100*ent_ci['ci_lower']:.2f}, {100*ent_ci['ci_upper']:.2f}], \\\\\\\"\\\\n              f\\\\\\\"Rel F1={100*rel_ci['point_estimate']:.2f}% [{100*rel_ci['ci_lower']:.2f}, {100*rel_ci['ci_upper']:.2f}]\\\\\\\")\\\\n\\\\n    comparisons = {}\\\\n    pairs = [\\\\n        (\\\\\\\"unconstrained\\\\\\\", \\\\\\\"grammar_only\\\\\\\"),\\\\n        (\\\\\\\"unconstrained\\\\\\\", \\\\\\\"semantic_only\\\\\\\"),\\\\n        (\\\\\\\"unconstrained\\\\\\\", \\\\\\\"full_s1\\\\\\\"),\\\\n        (\\\\\\\"grammar_only\\\\\\\", \\\\\\\"full_s1\\\\\\\"),\\\\n        (\\\\\\\"semantic_only\\\\\\\", \\\\\\\"full_s1\\\\\\\"),\\\\n    ]\\\\n    print(f\\\\\\\"\\\\\\\\n  Paired bootstrap tests (B - A):\\\\\\\")\\\\n    for cfg_a, cfg_b in pairs:\\\\n        if cfg_a not in all_stats or cfg_b not in all_stats:\\\\n            continue\\\\n        ent_test = paired_bootstrap_test(extract_stats(all_stats[cfg_a], \\\\\\\"entity\\\\\\\"),\\\\n                                          extract_stats(all_stats[cfg_b], \\\\\\\"entity\\\\\\\"))\\\\n        rel_test = paired_bootstrap_test(extract_stats(all_stats[cfg_a], \\\\\\\"relation\\\\\\\"),\\\\n                                          extract_stats(all_stats[cfg_b], \\\\\\\"relation\\\\\\\"))\\\\n        key = f\\\\\\\"{cfg_a}_vs_{cfg_b}\\\\\\\"\\\\n        comparisons[key] = {\\\\\\\"ent_f1_delta\\\\\\\": ent_test, \\\\\\\"rel_f1_delta\\\\\\\": rel_test}\\\\n        print(f\\\\\\\"  {key}:\\\\\\\")\\\\n        print(f\\\\\\\"    Ent ΔF1={100*ent_test['delta_point']:+.2f}pp [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}] p={ent_test['p_value']:.4f}\\\\\\\")\\\\n        print(f\\\\\\\"    Rel ΔF1={100*rel_test['delta_point']:+.2f}pp [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}] p={rel_test['p_value']:.4f}\\\\\\\")\\\\n\\\\n    return {\\\\\\\"per_config\\\\\\\": per_config, \\\\\\\"comparisons\\\\\\\": comparisons}\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    import os\\\\n    os.chdir(\\\\\\\"/root/schema_semantic_constrained_ie\\\\\\\")\\\\n\\\\n    # SciERC\\\\n    with open(\\\\\\\"ontology_constraints.json\\\\\\\") as f:\\\\n        scierc_constraints = json.load(f)\\\\n    scierc_valid_types = scierc_constraints[\\\\\\\"entity_types\\\\\\\"]\\\\n\\\\n    scierc_configs = {\\\\n        \\\\\\\"unconstrained\\\\\\\": \\\\\\\"outputs/phase2_scierc_unconstrained.jsonl\\\\\\\",\\\\n        \\\\\\\"grammar_only\\\\\\\": \\\\\\\"outputs/phase2_scierc_grammar_only.jsonl\\\\\\\",\\\\n        \\\\\\\"semantic_only\\\\\\\": \\\\\\\"outputs/phase2_scierc_semantic_only_v2.jsonl\\\\\\\",\\\\n        \\\\\\\"full_s1\\\\\\\": \\\\\\\"outputs/phase2_scierc_full_s1_v2.jsonl\\\\\\\",\\\\n    }\\\\n    scierc_results = run_dataset(\\\\\\\"SciERC\\\\\\\", scierc_configs, scierc_sample_stats, (scierc_valid_types,))\\\\n\\\\n    # DocRED\\\\n    with open(\\\\\\\"data/docred/ontology_constraints_docred.json\\\\\\\") as f:\\\\n        docred_constraints = json.load(f)\\\\n    docred_rel_types = docred_constraints.get(\\\\\\\"relation_types\\\\\\\", {})\\\\n    docred_name_to_id = build_name_to_id(docred_rel_types)\\\\n\\\\n    docred_configs = {\\\\n        \\\\\\\"unconstrained\\\\\\\": \\\\\\\"outputs/docred_unconstrained.jsonl\\\\\\\",\\\\n        \\\\\\\"grammar_only\\\\\\\": \\\\\\\"outputs/docred_grammar_only.jsonl\\\\\\\",\\\\n        \\\\\\\"semantic_only\\\\\\\": \\\\\\\"outputs/docred_semantic_only.jsonl\\\\\\\",\\\\n        \\\\\\\"full_s1\\\\\\\": \\\\\\\"outputs/docred_full_s1.jsonl\\\\\\\",\\\\n    }\\\\n    docred_results = run_dataset(\\\\\\\"DocRED\\\\\\\", docred_configs, docred_sample_stats, (docred_rel_types, docred_name_to_id))\\\\n\\\\n    # Save results\\\\n    def round_recursive(obj, decimals=6):\\\\n        if isinstance(obj, float):\\\\n            return round(obj, decimals)\\\\n        if isinstance(obj, dict):\\\\n            return {k: round_recursive(v, decimals) for k, v in obj.items()}\\\\n        if isinstance(obj, list):\\\\n            return [round_recursive(v, decimals) for v in obj]\\\\n        return obj\\\\n\\\\n    results = {\\\\n        \\\\\\\"scierc\\\\\\\": round_recursive(scierc_results),\\\\n        \\\\\\\"docred\\\\\\\": round_recursive(docred_results),\\\\n        \\\\\\\"metadata\\\\\\\": {\\\\n            \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n            \\\\\\\"ci_method\\\\\\\": \\\\\\\"percentile\\\\\\\",\\\\n            \\\\\\\"ci_level\\\\\\\": 0.95,\\\\n            \\\\\\\"seed\\\\\\\": 42,\\\\n            \\\\\\\"resample_unit\\\\\\\": \\\\\\\"sentence (SciERC) / document (DocRED)\\\\\\\",\\\\n        }\\\\n    }\\\\n\\\\n    output_path = \\\\\\\"outputs/bootstrap_ci_results_v2.json\\\\\\\"\\\\n    with open(output_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(results, f, indent=2)\\\\n    print(f\\\\\\\"\\\\\\\\nResults saved to {output_path}\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Compute bootstrap confidence intervals for SciERC and DocRED experiments.\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\nfrom pathlib import Path\\n\\n# --- SciERC normalization (from violation_checker.py) ---\\n\\nSCIERC_TYPE_MAP = {\\n    \\\"otherscientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other-scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other_scientific_term\\\": \\\"OtherScientificTerm\\\",\\n    \\\"scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other\\\": \\\"OtherScientificTerm\\\",\\n}\\n\\ndef scierc_normalize_type(t, valid_types):\\n    t_lower = t.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vt in valid_types:\\n        if t_lower == vt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vt\\n    if t_lower in SCIERC_TYPE_MAP:\\n        return SCIERC_TYPE_MAP[t_lower]\\n    return None\\n\\n# --- DocRED normalization (from violation_checker_docred.py) ---\\n\\nDOCRED_VALID_ENTITY_TYPES = {\\\"PER\\\", \\\"ORG\\\", \\\"LOC\\\", \\\"TIME\\\", \\\"NUM\\\", \\\"MISC\\\"}\\n\\nDOCRED_ENTITY_TYPE_ALIASES = {\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC',\\n    'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\ndef docred_normalize_entity_type(raw_type):\\n    t = raw_type.strip().upper()\\n    return DOCRED_ENTITY_TYPE_ALIASES.get(t, t)\\n\\ndef _levenshtein(s1, s2):\\n    if len(s1) < len(s2):\\n        return _levenshtein(s2, s1)\\n    if len(s2) == 0:\\n        return len(s1)\\n    prev_row = list(range(len(s2) + 1))\\n    for i, c1 in enumerate(s1):\\n        curr_row = [i + 1]\\n        for j, c2 in enumerate(s2):\\n            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (c1 != c2)))\\n        prev_row = curr_row\\n    return prev_row[-1]\\n\\ndef build_name_to_id(rel_types):\\n    name_to_id = {}\\n    for rid, rname in rel_types.items():\\n        name_to_id[rname.lower().strip()] = rid\\n        name_to_id[rid.lower()] = rid\\n    return name_to_id\\n\\ndef docred_normalize_relation(rel_name, rel_types, name_to_id):\\n    rel_key = name_to_id.get(rel_name.lower().strip())\\n    if rel_key:\\n        return rel_key\\n    rel_tokens = set(rel_name.strip().lower().split())\\n    best_pid, best_overlap = None, 0.0\\n    for rid, rname in rel_types.items():\\n        rname_tokens = set(rname.lower().split())\\n        if rel_tokens and rname_tokens:\\n            ratio = len(rel_tokens & rname_tokens) / len(rel_tokens | rname_tokens)\\n            if ratio > 0.8 and ratio > best_overlap:\\n                best_overlap = ratio\\n                best_pid = rid\\n    if best_pid:\\n        return best_pid\\n    for rid, rname in rel_types.items():\\n        if _levenshtein(rel_name.strip().lower(), rname.lower()) <= 2:\\n            return rid\\n    return None\\n\\n# --- Per-sample stats ---\\n\\ndef scierc_sample_stats(rec, valid_entity_types):\\n    parsed = rec.get(\\\"parsed_output\\\")\\n    gold_ents = rec.get(\\\"gold_entities\\\", [])\\n    gold_rels = rec.get(\\\"gold_relations\\\", [])\\n\\n    gold_ent_set = set((e[\\\"text\\\"].lower().strip(), e[\\\"type\\\"]) for e in gold_ents)\\n    gold_rel_set = set((r[\\\"head\\\"].lower().strip(), r[\\\"tail\\\"].lower().strip(), r[\\\"type\\\"]) for r in gold_rels)\\n\\n    if parsed is None:\\n        return {\\\"ent_tp\\\": 0, \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": 0,\\n                \\\"rel_tp\\\": 0, \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": 0}\\n\\n    entities = parsed.get(\\\"entities\\\", [])\\n    relations = parsed.get(\\\"relations\\\", [])\\n\\n    pred_ent_set = set()\\n    for e in entities:\\n        nt = scierc_normalize_type(e.get(\\\"type\\\", \\\"\\\"), valid_entity_types)\\n        if nt:\\n            pred_ent_set.add((e.get(\\\"text\\\", \\\"\\\").lower().strip(), nt))\\n\\n    pred_rel_set = set((r.get(\\\"head\\\", \\\"\\\").lower().strip(), r.get(\\\"tail\\\", \\\"\\\").lower().strip(), r.get(\\\"type\\\", \\\"\\\")) for r in relations)\\n\\n    return {\\n        \\\"ent_tp\\\": len(gold_ent_set & pred_ent_set), \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": len(pred_ent_set),\\n        \\\"rel_tp\\\": len(gold_rel_set & pred_rel_set), \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": len(pred_rel_set),\\n    }\\n\\ndef docred_sample_stats(rec, rel_types, name_to_id):\\n    pa\\n\\n... [截断: 输出过长，省略 6326 字符] ...\\n\\ne)\\n\\n    per_config = {}\\n    for name, stats in all_stats.items():\\n        ent_ci = bootstrap_f1(extract_stats(stats, \\\"entity\\\"))\\n        rel_ci = bootstrap_f1(extract_stats(stats, \\\"relation\\\"))\\n        per_config[name] = {\\\"ent_f1\\\": ent_ci, \\\"rel_f1\\\": rel_ci}\\n        print(f\\\"  {name} CI: Ent F1={100*ent_ci['point_estimate']:.2f}% [{100*ent_ci['ci_lower']:.2f}, {100*ent_ci['ci_upper']:.2f}], \\\"\\n              f\\\"Rel F1={100*rel_ci['point_estimate']:.2f}% [{100*rel_ci['ci_lower']:.2f}, {100*rel_ci['ci_upper']:.2f}]\\\")\\n\\n    comparisons = {}\\n    pairs = [\\n        (\\\"unconstrained\\\", \\\"grammar_only\\\"),\\n        (\\\"unconstrained\\\", \\\"semantic_only\\\"),\\n        (\\\"unconstrained\\\", \\\"full_s1\\\"),\\n        (\\\"grammar_only\\\", \\\"full_s1\\\"),\\n        (\\\"semantic_only\\\", \\\"full_s1\\\"),\\n    ]\\n    print(f\\\"\\\\n  Paired bootstrap tests (B - A):\\\")\\n    for cfg_a, cfg_b in pairs:\\n        if cfg_a not in all_stats or cfg_b not in all_stats:\\n            continue\\n        ent_test = paired_bootstrap_test(extract_stats(all_stats[cfg_a], \\\"entity\\\"),\\n                                          extract_stats(all_stats[cfg_b], \\\"entity\\\"))\\n        rel_test = paired_bootstrap_test(extract_stats(all_stats[cfg_a], \\\"relation\\\"),\\n                                          extract_stats(all_stats[cfg_b], \\\"relation\\\"))\\n        key = f\\\"{cfg_a}_vs_{cfg_b}\\\"\\n        comparisons[key] = {\\\"ent_f1_delta\\\": ent_test, \\\"rel_f1_delta\\\": rel_test}\\n        print(f\\\"  {key}:\\\")\\n        print(f\\\"    Ent ΔF1={100*ent_test['delta_point']:+.2f}pp [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}] p={ent_test['p_value']:.4f}\\\")\\n        print(f\\\"    Rel ΔF1={100*rel_test['delta_point']:+.2f}pp [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}] p={rel_test['p_value']:.4f}\\\")\\n\\n    return {\\\"per_config\\\": per_config, \\\"comparisons\\\": comparisons}\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    import os\\n    os.chdir(\\\"/root/schema_semantic_constrained_ie\\\")\\n\\n    # SciERC\\n    with open(\\\"ontology_constraints.json\\\") as f:\\n        scierc_constraints = json.load(f)\\n    scierc_valid_types = scierc_constraints[\\\"entity_types\\\"]\\n\\n    scierc_configs = {\\n        \\\"unconstrained\\\": \\\"outputs/phase2_scierc_unconstrained.jsonl\\\",\\n        \\\"grammar_only\\\": \\\"outputs/phase2_scierc_grammar_only.jsonl\\\",\\n        \\\"semantic_only\\\": \\\"outputs/phase2_scierc_semantic_only_v2.jsonl\\\",\\n        \\\"full_s1\\\": \\\"outputs/phase2_scierc_full_s1_v2.jsonl\\\",\\n    }\\n    scierc_results = run_dataset(\\\"SciERC\\\", scierc_configs, scierc_sample_stats, (scierc_valid_types,))\\n\\n    # DocRED\\n    with open(\\\"data/docred/ontology_constraints_docred.json\\\") as f:\\n        docred_constraints = json.load(f)\\n    docred_rel_types = docred_constraints.get(\\\"relation_types\\\", {})\\n    docred_name_to_id = build_name_to_id(docred_rel_types)\\n\\n    docred_configs = {\\n        \\\"unconstrained\\\": \\\"outputs/docred_unconstrained.jsonl\\\",\\n        \\\"grammar_only\\\": \\\"outputs/docred_grammar_only.jsonl\\\",\\n        \\\"semantic_only\\\": \\\"outputs/docred_semantic_only.jsonl\\\",\\n        \\\"full_s1\\\": \\\"outputs/docred_full_s1.jsonl\\\",\\n    }\\n    docred_results = run_dataset(\\\"DocRED\\\", docred_configs, docred_sample_stats, (docred_rel_types, docred_name_to_id))\\n\\n    # Save results\\n    def round_recursive(obj, decimals=6):\\n        if isinstance(obj, float):\\n            return round(obj, decimals)\\n        if isinstance(obj, dict):\\n            return {k: round_recursive(v, decimals) for k, v in obj.items()}\\n        if isinstance(obj, list):\\n            return [round_recursive(v, decimals) for v in obj]\\n        return obj\\n\\n    results = {\\n        \\\"scierc\\\": round_recursive(scierc_results),\\n        \\\"docred\\\": round_recursive(docred_results),\\n        \\\"metadata\\\": {\\n            \\\"n_bootstrap\\\": 10000,\\n            \\\"ci_method\\\": \\\"percentile\\\",\\n            \\\"ci_level\\\": 0.95,\\n            \\\"seed\\\": 42,\\n            \\\"resample_unit\\\": \\\"sentence (SciERC) / document (DocRED)\\\",\\n        }\\n    }\\n\\n    output_path = \\\"outputs/bootstrap_ci_results_v2.json\\\"\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(results, f, indent=2)\\n    print(f\\\"\\\\nResults saved to {output_path}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T14:12:05.144Z_

<details><summary>↩ Tool result · `toolu_01SAUUXm48ZDcmf29XzJg563`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Compute bootstrap confidence intervals for Llama SciERC and DocRED experiments.\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport numpy as np\\nfrom pathlib import Path\\n\\nsys.path.insert(0, \\\"/root/schema_semantic_constrained_ie\\\")\\nfrom compute_bootstrap_ci import (\\n    scierc_sample_stats,\\n    bootstrap_f1, paired_bootstrap_test,\\n    load_jsonl, extract_stats,\\n    build_name_to_id, docred_normalize_relation,\\n)\\n\\nREGISTRY = {\\n    \\\"llama_scierc_unconstrained\\\": {\\\"rel_f1\\\": 2.68, \\\"ent_f1\\\": 23.56},\\n    \\\"llama_scierc_full_s1\\\":      {\\\"rel_f1\\\": 2.54, \\\"ent_f1\\\": 23.49},\\n    \\\"llama_docred_unconstrained\\\": {\\\"rel_f1\\\": 5.98, \\\"ent_f1\\\": 55.65},\\n    \\\"llama_docred_full_s1\\\":      {\\\"rel_f1\\\": 6.27, \\\"ent_f1\\\": 55.01},\\n}\\n\\n# Tolerance 0.05pp: registry values were rounded at storage time, causing\\n# up to ~0.03pp rounding discrepancy (e.g. SciERC E-F1 23.5294 vs 23.56).\\n# 0.05pp is still far below any meaningful statistical difference.\\nREGISTRY_TOL_PP = 0.05\\n\\ndef check_registry_alignment(config_name, ent_f1, rel_f1):\\n    reg = REGISTRY[config_name]\\n    ent_delta = abs(ent_f1 * 100 - reg[\\\"ent_f1\\\"])\\n    rel_delta = abs(rel_f1 * 100 - reg[\\\"rel_f1\\\"])\\n    ent_pass = ent_delta <= REGISTRY_TOL_PP\\n    rel_pass = rel_delta <= REGISTRY_TOL_PP\\n    print(f\\\"  Registry check {config_name}:\\\")\\n    print(f\\\"    E-F1: computed={ent_f1*100:.4f} registry={reg['ent_f1']:.2f} delta={ent_delta:.4f}pp {'PASS' if ent_pass else 'FAIL'}\\\")\\n    print(f\\\"    R-F1: computed={rel_f1*100:.4f} registry={reg['rel_f1']:.2f} delta={rel_delta:.4f}pp {'PASS' if rel_pass else 'FAIL'}\\\")\\n    return ent_pass and rel_pass\\n\\n\\ndef docred_sample_stats_llama(rec, rel_types, name_to_id):\\n    \\\"\\\"\\\"Like docred_sample_stats but with two Llama-specific fixes:\\n    1. str() wrapping for int-typed entity text (e.g. years like 1945)\\n    2. Correct gold counting when parsed_output is None\\n    \\\"\\\"\\\"\\n    parsed = rec.get(\\\"parsed_output\\\")\\n    gold_ents = rec.get(\\\"gold_entities\\\", [])\\n    gold_rels = rec.get(\\\"gold_relations\\\", [])\\n\\n    gold_ent_set = set((str(e[\\\"text\\\"]).lower().strip(), e[\\\"type\\\"]) for e in gold_ents)\\n    gold_rel_set = set((str(r[\\\"head\\\"]).lower().strip(), str(r[\\\"tail\\\"]).lower().strip(), r[\\\"type\\\"]) for r in gold_rels)\\n\\n    if parsed is None:\\n        return {\\\"ent_tp\\\": 0, \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": 0,\\n                \\\"rel_tp\\\": 0, \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": 0}\\n\\n    entities = parsed.get(\\\"entities\\\", [])\\n    relations = parsed.get(\\\"relations\\\", [])\\n\\n    pred_ent_set = set((str(e.get(\\\"text\\\", \\\"\\\")).lower().strip(), e.get(\\\"type\\\", \\\"\\\")) for e in entities)\\n\\n    pred_rel_set = set()\\n    for r in relations:\\n        pid = docred_normalize_relation(str(r.get(\\\"type\\\", \\\"\\\")), rel_types, name_to_id)\\n        if pid:\\n            pred_rel_set.add((str(r.get(\\\"head\\\", \\\"\\\")).lower().strip(), str(r.get(\\\"tail\\\", \\\"\\\")).lower().strip(), pid))\\n        else:\\n            pred_rel_set.add((str(r.get(\\\"head\\\", \\\"\\\")).lower().strip(), str(r.get(\\\"tail\\\", \\\"\\\")).lower().strip(), f\\\"__OOV__{r.get('type', '')}\\\"))\\n\\n    return {\\n        \\\"ent_tp\\\": len(gold_ent_set & pred_ent_set), \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": len(pred_ent_set),\\n        \\\"rel_tp\\\": len(gold_rel_set & pred_rel_set), \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": len(pred_rel_set),\\n    }\\n\\n\\ndef compute_point_f1(stats_list, metric):\\n    extracted = extract_stats(stats_list, metric)\\n    tp = sum(s[\\\"tp\\\"] for s in extracted)\\n    gold = sum(s[\\\"gold\\\"] for s in extracted)\\n    pred = sum(s[\\\"pred\\\"] for s in extracted)\\n    if gold + pred == 0:\\n        return 0.0\\n    return 2 * tp / (gold + pred)\\n\\ndef run_llama_dataset(dataset_name, config_paths, stats_fn, stats_fn_args, registry_keys):\\n    print(f\\\"\\\\n{'='*50}\\\")\\n    print(f\\\"  Llama {dataset_name}\\\")\\n    print(f\\\"{'='*50}\\\")\\n\\n    all_raw = {}\\n    all_stats = {}\\n    for name, path in config_paths.items():\\n        records = load_jsonl(path)\\n        raw_with_id = [{\\\"doc_id\\\": r.get(\\\"doc_id\\\", i), **stats_fn(r, *stats_fn_args)} for i, r in enumerate(records)]\\n        all_raw[name] = {r[\\\"doc_id\\\"]: r for r in raw_with_id}\\n        all_stats[name] = [{k: v\\n\\n... [截断: 输出过长，省略 1682 字符] ...\\n\\nmon_ids)} (from {[len(all_raw[c]) for c in configs]})\\\")\\n\\n    aligned_stats = {}\\n    for name in configs:\\n        aligned_stats[name] = [{k: v for k, v in all_raw[name][did].items() if k != \\\"doc_id\\\"} for did in common_ids]\\n\\n    comparisons = {}\\n    pairs = [(\\\"unconstrained\\\", \\\"full_s1\\\")]\\n    print(f\\\"\\\\n  Paired bootstrap tests (full_s1 - unconstrained):\\\")\\n    for cfg_a, cfg_b in pairs:\\n        if cfg_a not in aligned_stats or cfg_b not in aligned_stats:\\n            continue\\n        ent_test = paired_bootstrap_test(extract_stats(aligned_stats[cfg_a], \\\"entity\\\"),\\n                                          extract_stats(aligned_stats[cfg_b], \\\"entity\\\"))\\n        rel_test = paired_bootstrap_test(extract_stats(aligned_stats[cfg_a], \\\"relation\\\"),\\n                                          extract_stats(aligned_stats[cfg_b], \\\"relation\\\"))\\n        key = f\\\"{cfg_a}_vs_{cfg_b}\\\"\\n        comparisons[key] = {\\\"ent_f1_delta\\\": ent_test, \\\"rel_f1_delta\\\": rel_test}\\n        print(f\\\"  {key}:\\\")\\n        print(f\\\"    Ent ΔF1={100*ent_test['delta_point']:+.2f}pp [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}] p={ent_test['p_value']:.4f}\\\")\\n        print(f\\\"    Rel ΔF1={100*rel_test['delta_point']:+.2f}pp [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}] p={rel_test['p_value']:.4f}\\\")\\n\\n    return {\\\"per_config\\\": per_config, \\\"comparisons\\\": comparisons}\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    import os\\n    os.chdir(\\\"/root/schema_semantic_constrained_ie\\\")\\n\\n    # SciERC\\n    with open(\\\"ontology_constraints.json\\\") as f:\\n        scierc_constraints = json.load(f)\\n    scierc_valid_types = scierc_constraints[\\\"entity_types\\\"]\\n\\n    scierc_configs = {\\n        \\\"unconstrained\\\": \\\"outputs/llama_scierc_unconstrained.jsonl\\\",\\n        \\\"full_s1\\\": \\\"outputs/llama_scierc_full_s1.jsonl\\\",\\n    }\\n    scierc_registry_keys = {\\n        \\\"unconstrained\\\": \\\"llama_scierc_unconstrained\\\",\\n        \\\"full_s1\\\": \\\"llama_scierc_full_s1\\\",\\n    }\\n    scierc_results = run_llama_dataset(\\\"SciERC\\\", scierc_configs, scierc_sample_stats,\\n                                        (scierc_valid_types,), scierc_registry_keys)\\n\\n    # DocRED — use Llama-safe version with str() wrapping + correct gold counting\\n    with open(\\\"data/docred/ontology_constraints_docred.json\\\") as f:\\n        docred_constraints = json.load(f)\\n    docred_rel_types = docred_constraints.get(\\\"relation_types\\\", {})\\n    docred_name_to_id = build_name_to_id(docred_rel_types)\\n\\n    docred_configs = {\\n        \\\"unconstrained\\\": \\\"outputs/llama_docred_unconstrained.jsonl\\\",\\n        \\\"full_s1\\\": \\\"outputs/llama_docred_full_s1.jsonl\\\",\\n    }\\n    docred_registry_keys = {\\n        \\\"unconstrained\\\": \\\"llama_docred_unconstrained\\\",\\n        \\\"full_s1\\\": \\\"llama_docred_full_s1\\\",\\n    }\\n    docred_results = run_llama_dataset(\\\"DocRED\\\", docred_configs, docred_sample_stats_llama,\\n                                        (docred_rel_types, docred_name_to_id), docred_registry_keys)\\n\\n    if scierc_results is None or docred_results is None:\\n        print(\\\"\\\\nABORTED due to registry alignment failure.\\\")\\n        sys.exit(1)\\n\\n    def round_recursive(obj, decimals=6):\\n        if isinstance(obj, float):\\n            return round(obj, decimals)\\n        if isinstance(obj, dict):\\n            return {k: round_recursive(v, decimals) for k, v in obj.items()}\\n        if isinstance(obj, list):\\n            return [round_recursive(v, decimals) for v in obj]\\n        return obj\\n\\n    results = {\\n        \\\"scierc\\\": round_recursive(scierc_results),\\n        \\\"docred\\\": round_recursive(docred_results),\\n        \\\"metadata\\\": {\\n            \\\"model\\\": \\\"llama\\\",\\n            \\\"n_bootstrap\\\": 10000,\\n            \\\"ci_method\\\": \\\"percentile\\\",\\n            \\\"ci_level\\\": 0.95,\\n            \\\"seed\\\": 42,\\n            \\\"resample_unit\\\": \\\"sentence (SciERC) / document (DocRED)\\\",\\n            \\\"registry_tolerance_pp\\\": REGISTRY_TOL_PP,\\n        }\\n    }\\n\\n    output_path = \\\"outputs/bootstrap_ci_results_llama.json\\\"\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(results, f, indent=2)\\n    print(f\\\"\\\\nResults saved to {output_path}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "c2b6b66a-8b9e-4d5a-997c-938dcdb2c7f2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Compute bootstrap confidence intervals for Llama SciERC and DocRED experiments.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport json\\\\nimport sys\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\n\\\\nsys.path.insert(0, \\\\\\\"/root/schema_semantic_constrained_ie\\\\\\\")\\\\nfrom compute_bootstrap_ci import (\\\\n    scierc_sample_stats,\\\\n    bootstrap_f1, paired_bootstrap_test,\\\\n    load_jsonl, extract_stats,\\\\n    build_name_to_id, docred_normalize_relation,\\\\n)\\\\n\\\\nREGISTRY = {\\\\n    \\\\\\\"llama_scierc_unconstrained\\\\\\\": {\\\\\\\"rel_f1\\\\\\\": 2.68, \\\\\\\"ent_f1\\\\\\\": 23.56},\\\\n    \\\\\\\"llama_scierc_full_s1\\\\\\\":      {\\\\\\\"rel_f1\\\\\\\": 2.54, \\\\\\\"ent_f1\\\\\\\": 23.49},\\\\n    \\\\\\\"llama_docred_unconstrained\\\\\\\": {\\\\\\\"rel_f1\\\\\\\": 5.98, \\\\\\\"ent_f1\\\\\\\": 55.65},\\\\n    \\\\\\\"llama_docred_full_s1\\\\\\\":      {\\\\\\\"rel_f1\\\\\\\": 6.27, \\\\\\\"ent_f1\\\\\\\": 55.01},\\\\n}\\\\n\\\\n# Tolerance 0.05pp: registry values were rounded at storage time, causing\\\\n# up to ~0.03pp rounding discrepancy (e.g. SciERC E-F1 23.5294 vs 23.56).\\\\n# 0.05pp is still far below any meaningful statistical difference.\\\\nREGISTRY_TOL_PP = 0.05\\\\n\\\\ndef check_registry_alignment(config_name, ent_f1, rel_f1):\\\\n    reg = REGISTRY[config_name]\\\\n    ent_delta = abs(ent_f1 * 100 - reg[\\\\\\\"ent_f1\\\\\\\"])\\\\n    rel_delta = abs(rel_f1 * 100 - reg[\\\\\\\"rel_f1\\\\\\\"])\\\\n    ent_pass = ent_delta <= REGISTRY_TOL_PP\\\\n    rel_pass = rel_delta <= REGISTRY_TOL_PP\\\\n    print(f\\\\\\\"  Registry check {config_name}:\\\\\\\")\\\\n    print(f\\\\\\\"    E-F1: computed={ent_f1*100:.4f} registry={reg['ent_f1']:.2f} delta={ent_delta:.4f}pp {'PASS' if ent_pass else 'FAIL'}\\\\\\\")\\\\n    print(f\\\\\\\"    R-F1: computed={rel_f1*100:.4f} registry={reg['rel_f1']:.2f} delta={rel_delta:.4f}pp {'PASS' if rel_pass else 'FAIL'}\\\\\\\")\\\\n    return ent_pass and rel_pass\\\\n\\\\n\\\\ndef docred_sample_stats_llama(rec, rel_types, name_to_id):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Like docred_sample_stats but with two Llama-specific fixes:\\\\n    1. str() wrapping for int-typed entity text (e.g. years like 1945)\\\\n    2. Correct gold counting when parsed_output is None\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    parsed = rec.get(\\\\\\\"parsed_output\\\\\\\")\\\\n    gold_ents = rec.get(\\\\\\\"gold_entities\\\\\\\", [])\\\\n    gold_rels = rec.get(\\\\\\\"gold_relations\\\\\\\", [])\\\\n\\\\n    gold_ent_set = set((str(e[\\\\\\\"text\\\\\\\"]).lower().strip(), e[\\\\\\\"type\\\\\\\"]) for e in gold_ents)\\\\n    gold_rel_set = set((str(r[\\\\\\\"head\\\\\\\"]).lower().strip(), str(r[\\\\\\\"tail\\\\\\\"]).lower().strip(), r[\\\\\\\"type\\\\\\\"]) for r in gold_rels)\\\\n\\\\n    if parsed is None:\\\\n        return {\\\\\\\"ent_tp\\\\\\\": 0, \\\\\\\"ent_gold\\\\\\\": len(gold_ent_set), \\\\\\\"ent_pred\\\\\\\": 0,\\\\n                \\\\\\\"rel_tp\\\\\\\": 0, \\\\\\\"rel_gold\\\\\\\": len(gold_rel_set), \\\\\\\"rel_pred\\\\\\\": 0}\\\\n\\\\n    entities = parsed.get(\\\\\\\"entities\\\\\\\", [])\\\\n    relations = parsed.get(\\\\\\\"relations\\\\\\\", [])\\\\n\\\\n    pred_ent_set = set((str(e.get(\\\\\\\"text\\\\\\\", \\\\\\\"\\\\\\\")).lower().strip(), e.get(\\\\\\\"type\\\\\\\", \\\\\\\"\\\\\\\")) for e in entities)\\\\n\\\\n    pred_rel_set = set()\\\\n    for r in relations:\\\\n        pid = docred_normalize_relation(str(r.get(\\\\\\\"type\\\\\\\", \\\\\\\"\\\\\\\")), rel_types, name_to_id)\\\\n        if pid:\\\\n            pred_rel_set.add((str(r.get(\\\\\\\"head\\\\\\\", \\\\\\\"\\\\\\\")).lower().strip(), str(r.get(\\\\\\\"tail\\\\\\\", \\\\\\\"\\\\\\\")).lower().strip(), pid))\\\\n        else:\\\\n            pred_rel_set.add((str(r.get(\\\\\\\"head\\\\\\\", \\\\\\\"\\\\\\\")).lower().strip(), str(r.get(\\\\\\\"tail\\\\\\\", \\\\\\\"\\\\\\\")).lower().strip(), f\\\\\\\"__OOV__{r.get('type', '')}\\\\\\\"))\\\\n\\\\n    return {\\\\n        \\\\\\\"ent_tp\\\\\\\": len(gold_ent_set & pred_ent_set), \\\\\\\"ent_gold\\\\\\\": len(gold_ent_set), \\\\\\\"ent_pred\\\\\\\": len(pred_ent_set),\\\\n        \\\\\\\"rel_tp\\\\\\\": len(gold_rel_set & pred_rel_set), \\\\\\\"rel_gold\\\\\\\": len(gold_rel_set), \\\\\\\"rel_pred\\\\\\\": len(pred_rel_set),\\\\n    }\\\\n\\\\n\\\\ndef compute_point_f1(stats_list, metric):\\\\n    extracted = extract_stats(stats_list, metric)\\\\n    tp = sum(s[\\\\\\\"tp\\\\\\\"] for s in extracted)\\\\n    gold = sum(s[\\\\\\\"gold\\\\\\\"] for s in extracted)\\\\n    pred = sum(s[\\\\\\\"pred\\\\\\\"] for s in extracted)\\\\n    if gold + pred == 0:\\\\n        return 0.0\\\\n    return 2 * tp / (gold + pred)\\\\n\\\\ndef run_llama_dataset(dataset_name, config_paths, stats_fn, stats_fn_args, registry_keys):\\\\n    print(f\\\\\\\"\\\\\\\\n{'='*50}\\\\\\\")\\\\n    print(f\\\\\\\"  Llama {dataset_name}\\\\\\\")\\\\n    print(f\\\\\\\"{'='*50}\\\\\\\")\\\\n\\\\n    all_raw = {}\\\\n    all_stats = {}\\\\n    for name, path in config_paths.items():\\\\n        records = load_jsonl(path)\\\\n        raw_with_id = [{\\\\\\\"doc_id\\\\\\\": r.get(\\\\\\\"doc_id\\\\\\\", i), **stats_fn(r, *stats_fn_args)} for i, r in enumerate(records)]\\\\n        all_raw[name] = {r[\\\\\\\"doc_id\\\\\\\"]: r for r in raw_with_id}\\\\n        all_stats[name] = [{k: v\\\\n\\\\n... [截断: 输出过长，省略 1682 字符] ...\\\\n\\\\nmon_ids)} (from {[len(all_raw[c]) for c in configs]})\\\\\\\")\\\\n\\\\n    aligned_stats = {}\\\\n    for name in configs:\\\\n        aligned_stats[name] = [{k: v for k, v in all_raw[name][did].items() if k != \\\\\\\"doc_id\\\\\\\"} for did in common_ids]\\\\n\\\\n    comparisons = {}\\\\n    pairs = [(\\\\\\\"unconstrained\\\\\\\", \\\\\\\"full_s1\\\\\\\")]\\\\n    print(f\\\\\\\"\\\\\\\\n  Paired bootstrap tests (full_s1 - unconstrained):\\\\\\\")\\\\n    for cfg_a, cfg_b in pairs:\\\\n        if cfg_a not in aligned_stats or cfg_b not in aligned_stats:\\\\n            continue\\\\n        ent_test = paired_bootstrap_test(extract_stats(aligned_stats[cfg_a], \\\\\\\"entity\\\\\\\"),\\\\n                                          extract_stats(aligned_stats[cfg_b], \\\\\\\"entity\\\\\\\"))\\\\n        rel_test = paired_bootstrap_test(extract_stats(aligned_stats[cfg_a], \\\\\\\"relation\\\\\\\"),\\\\n                                          extract_stats(aligned_stats[cfg_b], \\\\\\\"relation\\\\\\\"))\\\\n        key = f\\\\\\\"{cfg_a}_vs_{cfg_b}\\\\\\\"\\\\n        comparisons[key] = {\\\\\\\"ent_f1_delta\\\\\\\": ent_test, \\\\\\\"rel_f1_delta\\\\\\\": rel_test}\\\\n        print(f\\\\\\\"  {key}:\\\\\\\")\\\\n        print(f\\\\\\\"    Ent ΔF1={100*ent_test['delta_point']:+.2f}pp [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}] p={ent_test['p_value']:.4f}\\\\\\\")\\\\n        print(f\\\\\\\"    Rel ΔF1={100*rel_test['delta_point']:+.2f}pp [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}] p={rel_test['p_value']:.4f}\\\\\\\")\\\\n\\\\n    return {\\\\\\\"per_config\\\\\\\": per_config, \\\\\\\"comparisons\\\\\\\": comparisons}\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    import os\\\\n    os.chdir(\\\\\\\"/root/schema_semantic_constrained_ie\\\\\\\")\\\\n\\\\n    # SciERC\\\\n    with open(\\\\\\\"ontology_constraints.json\\\\\\\") as f:\\\\n        scierc_constraints = json.load(f)\\\\n    scierc_valid_types = scierc_constraints[\\\\\\\"entity_types\\\\\\\"]\\\\n\\\\n    scierc_configs = {\\\\n        \\\\\\\"unconstrained\\\\\\\": \\\\\\\"outputs/llama_scierc_unconstrained.jsonl\\\\\\\",\\\\n        \\\\\\\"full_s1\\\\\\\": \\\\\\\"outputs/llama_scierc_full_s1.jsonl\\\\\\\",\\\\n    }\\\\n    scierc_registry_keys = {\\\\n        \\\\\\\"unconstrained\\\\\\\": \\\\\\\"llama_scierc_unconstrained\\\\\\\",\\\\n        \\\\\\\"full_s1\\\\\\\": \\\\\\\"llama_scierc_full_s1\\\\\\\",\\\\n    }\\\\n    scierc_results = run_llama_dataset(\\\\\\\"SciERC\\\\\\\", scierc_configs, scierc_sample_stats,\\\\n                                        (scierc_valid_types,), scierc_registry_keys)\\\\n\\\\n    # DocRED — use Llama-safe version with str() wrapping + correct gold counting\\\\n    with open(\\\\\\\"data/docred/ontology_constraints_docred.json\\\\\\\") as f:\\\\n        docred_constraints = json.load(f)\\\\n    docred_rel_types = docred_constraints.get(\\\\\\\"relation_types\\\\\\\", {})\\\\n    docred_name_to_id = build_name_to_id(docred_rel_types)\\\\n\\\\n    docred_configs = {\\\\n        \\\\\\\"unconstrained\\\\\\\": \\\\\\\"outputs/llama_docred_unconstrained.jsonl\\\\\\\",\\\\n        \\\\\\\"full_s1\\\\\\\": \\\\\\\"outputs/llama_docred_full_s1.jsonl\\\\\\\",\\\\n    }\\\\n    docred_registry_keys = {\\\\n        \\\\\\\"unconstrained\\\\\\\": \\\\\\\"llama_docred_unconstrained\\\\\\\",\\\\n        \\\\\\\"full_s1\\\\\\\": \\\\\\\"llama_docred_full_s1\\\\\\\",\\\\n    }\\\\n    docred_results = run_llama_dataset(\\\\\\\"DocRED\\\\\\\", docred_configs, docred_sample_stats_llama,\\\\n                                        (docred_rel_types, docred_name_to_id), docred_registry_keys)\\\\n\\\\n    if scierc_results is None or docred_results is None:\\\\n        print(\\\\\\\"\\\\\\\\nABORTED due to registry alignment failure.\\\\\\\")\\\\n        sys.exit(1)\\\\n\\\\n    def round_recursive(obj, decimals=6):\\\\n        if isinstance(obj, float):\\\\n            return round(obj, decimals)\\\\n        if isinstance(obj, dict):\\\\n            return {k: round_recursive(v, decimals) for k, v in obj.items()}\\\\n        if isinstance(obj, list):\\\\n            return [round_recursive(v, decimals) for v in obj]\\\\n        return obj\\\\n\\\\n    results = {\\\\n        \\\\\\\"scierc\\\\\\\": round_recursive(scierc_results),\\\\n        \\\\\\\"docred\\\\\\\": round_recursive(docred_results),\\\\n        \\\\\\\"metadata\\\\\\\": {\\\\n            \\\\\\\"model\\\\\\\": \\\\\\\"llama\\\\\\\",\\\\n            \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n            \\\\\\\"ci_method\\\\\\\": \\\\\\\"percentile\\\\\\\",\\\\n            \\\\\\\"ci_level\\\\\\\": 0.95,\\\\n            \\\\\\\"seed\\\\\\\": 42,\\\\n            \\\\\\\"resample_unit\\\\\\\": \\\\\\\"sentence (SciERC) / document (DocRED)\\\\\\\",\\\\n            \\\\\\\"registry_tolerance_pp\\\\\\\": REGISTRY_TOL_PP,\\\\n        }\\\\n    }\\\\n\\\\n    output_path = \\\\\\\"outputs/bootstrap_ci_results_llama.json\\\\\\\"\\\\n    with open(output_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(results, f, indent=2)\\\\n    print(f\\\\\\\"\\\\\\\\nResults saved to {output_path}\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Compute bootstrap confidence intervals for Llama SciERC and DocRED experiments.\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport numpy as np\\nfrom pathlib import Path\\n\\nsys.path.insert(0, \\\"/root/schema_semantic_constrained_ie\\\")\\nfrom compute_bootstrap_ci import (\\n    scierc_sample_stats,\\n    bootstrap_f1, paired_bootstrap_test,\\n    load_jsonl, extract_stats,\\n    build_name_to_id, docred_normalize_relation,\\n)\\n\\nREGISTRY = {\\n    \\\"llama_scierc_unconstrained\\\": {\\\"rel_f1\\\": 2.68, \\\"ent_f1\\\": 23.56},\\n    \\\"llama_scierc_full_s1\\\":      {\\\"rel_f1\\\": 2.54, \\\"ent_f1\\\": 23.49},\\n    \\\"llama_docred_unconstrained\\\": {\\\"rel_f1\\\": 5.98, \\\"ent_f1\\\": 55.65},\\n    \\\"llama_docred_full_s1\\\":      {\\\"rel_f1\\\": 6.27, \\\"ent_f1\\\": 55.01},\\n}\\n\\n# Tolerance 0.05pp: registry values were rounded at storage time, causing\\n# up to ~0.03pp rounding discrepancy (e.g. SciERC E-F1 23.5294 vs 23.56).\\n# 0.05pp is still far below any meaningful statistical difference.\\nREGISTRY_TOL_PP = 0.05\\n\\ndef check_registry_alignment(config_name, ent_f1, rel_f1):\\n    reg = REGISTRY[config_name]\\n    ent_delta = abs(ent_f1 * 100 - reg[\\\"ent_f1\\\"])\\n    rel_delta = abs(rel_f1 * 100 - reg[\\\"rel_f1\\\"])\\n    ent_pass = ent_delta <= REGISTRY_TOL_PP\\n    rel_pass = rel_delta <= REGISTRY_TOL_PP\\n    print(f\\\"  Registry check {config_name}:\\\")\\n    print(f\\\"    E-F1: computed={ent_f1*100:.4f} registry={reg['ent_f1']:.2f} delta={ent_delta:.4f}pp {'PASS' if ent_pass else 'FAIL'}\\\")\\n    print(f\\\"    R-F1: computed={rel_f1*100:.4f} registry={reg['rel_f1']:.2f} delta={rel_delta:.4f}pp {'PASS' if rel_pass else 'FAIL'}\\\")\\n    return ent_pass and rel_pass\\n\\n\\ndef docred_sample_stats_llama(rec, rel_types, name_to_id):\\n    \\\"\\\"\\\"Like docred_sample_stats but with two Llama-specific fixes:\\n    1. str() wrapping for int-typed entity text (e.g. years like 1945)\\n    2. Correct gold counting when parsed_output is None\\n    \\\"\\\"\\\"\\n    parsed = rec.get(\\\"parsed_output\\\")\\n    gold_ents = rec.get(\\\"gold_entities\\\", [])\\n    gold_rels = rec.get(\\\"gold_relations\\\", [])\\n\\n    gold_ent_set = set((str(e[\\\"text\\\"]).lower().strip(), e[\\\"type\\\"]) for e in gold_ents)\\n    gold_rel_set = set((str(r[\\\"head\\\"]).lower().strip(), str(r[\\\"tail\\\"]).lower().strip(), r[\\\"type\\\"]) for r in gold_rels)\\n\\n    if parsed is None:\\n        return {\\\"ent_tp\\\": 0, \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": 0,\\n                \\\"rel_tp\\\": 0, \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": 0}\\n\\n    entities = parsed.get(\\\"entities\\\", [])\\n    relations = parsed.get(\\\"relations\\\", [])\\n\\n    pred_ent_set = set((str(e.get(\\\"text\\\", \\\"\\\")).lower().strip(), e.get(\\\"type\\\", \\\"\\\")) for e in entities)\\n\\n    pred_rel_set = set()\\n    for r in relations:\\n        pid = docred_normalize_relation(str(r.get(\\\"type\\\", \\\"\\\")), rel_types, name_to_id)\\n        if pid:\\n            pred_rel_set.add((str(r.get(\\\"head\\\", \\\"\\\")).lower().strip(), str(r.get(\\\"tail\\\", \\\"\\\")).lower().strip(), pid))\\n        else:\\n            pred_rel_set.add((str(r.get(\\\"head\\\", \\\"\\\")).lower().strip(), str(r.get(\\\"tail\\\", \\\"\\\")).lower().strip(), f\\\"__OOV__{r.get('type', '')}\\\"))\\n\\n    return {\\n        \\\"ent_tp\\\": len(gold_ent_set & pred_ent_set), \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": len(pred_ent_set),\\n        \\\"rel_tp\\\": len(gold_rel_set & pred_rel_set), \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": len(pred_rel_set),\\n    }\\n\\n\\ndef compute_point_f1(stats_list, metric):\\n    extracted = extract_stats(stats_list, metric)\\n    tp = sum(s[\\\"tp\\\"] for s in extracted)\\n    gold = sum(s[\\\"gold\\\"] for s in extracted)\\n    pred = sum(s[\\\"pred\\\"] for s in extracted)\\n    if gold + pred == 0:\\n        return 0.0\\n    return 2 * tp / (gold + pred)\\n\\ndef run_llama_dataset(dataset_name, config_paths, stats_fn, stats_fn_args, registry_keys):\\n    print(f\\\"\\\\n{'='*50}\\\")\\n    print(f\\\"  Llama {dataset_name}\\\")\\n    print(f\\\"{'='*50}\\\")\\n\\n    all_raw = {}\\n    all_stats = {}\\n    for name, path in config_paths.items():\\n        records = load_jsonl(path)\\n        raw_with_id = [{\\\"doc_id\\\": r.get(\\\"doc_id\\\", i), **stats_fn(r, *stats_fn_args)} for i, r in enumerate(records)]\\n        all_raw[name] = {r[\\\"doc_id\\\"]: r for r in raw_with_id}\\n        all_stats[name] = [{k: v\\n\\n... [截断: 输出过长，省略 1682 字符] ...\\n\\nmon_ids)} (from {[len(all_raw[c]) for c in configs]})\\\")\\n\\n    aligned_stats = {}\\n    for name in configs:\\n        aligned_stats[name] = [{k: v for k, v in all_raw[name][did].items() if k != \\\"doc_id\\\"} for did in common_ids]\\n\\n    comparisons = {}\\n    pairs = [(\\\"unconstrained\\\", \\\"full_s1\\\")]\\n    print(f\\\"\\\\n  Paired bootstrap tests (full_s1 - unconstrained):\\\")\\n    for cfg_a, cfg_b in pairs:\\n        if cfg_a not in aligned_stats or cfg_b not in aligned_stats:\\n            continue\\n        ent_test = paired_bootstrap_test(extract_stats(aligned_stats[cfg_a], \\\"entity\\\"),\\n                                          extract_stats(aligned_stats[cfg_b], \\\"entity\\\"))\\n        rel_test = paired_bootstrap_test(extract_stats(aligned_stats[cfg_a], \\\"relation\\\"),\\n                                          extract_stats(aligned_stats[cfg_b], \\\"relation\\\"))\\n        key = f\\\"{cfg_a}_vs_{cfg_b}\\\"\\n        comparisons[key] = {\\\"ent_f1_delta\\\": ent_test, \\\"rel_f1_delta\\\": rel_test}\\n        print(f\\\"  {key}:\\\")\\n        print(f\\\"    Ent ΔF1={100*ent_test['delta_point']:+.2f}pp [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}] p={ent_test['p_value']:.4f}\\\")\\n        print(f\\\"    Rel ΔF1={100*rel_test['delta_point']:+.2f}pp [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}] p={rel_test['p_value']:.4f}\\\")\\n\\n    return {\\\"per_config\\\": per_config, \\\"comparisons\\\": comparisons}\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    import os\\n    os.chdir(\\\"/root/schema_semantic_constrained_ie\\\")\\n\\n    # SciERC\\n    with open(\\\"ontology_constraints.json\\\") as f:\\n        scierc_constraints = json.load(f)\\n    scierc_valid_types = scierc_constraints[\\\"entity_types\\\"]\\n\\n    scierc_configs = {\\n        \\\"unconstrained\\\": \\\"outputs/llama_scierc_unconstrained.jsonl\\\",\\n        \\\"full_s1\\\": \\\"outputs/llama_scierc_full_s1.jsonl\\\",\\n    }\\n    scierc_registry_keys = {\\n        \\\"unconstrained\\\": \\\"llama_scierc_unconstrained\\\",\\n        \\\"full_s1\\\": \\\"llama_scierc_full_s1\\\",\\n    }\\n    scierc_results = run_llama_dataset(\\\"SciERC\\\", scierc_configs, scierc_sample_stats,\\n                                        (scierc_valid_types,), scierc_registry_keys)\\n\\n    # DocRED — use Llama-safe version with str() wrapping + correct gold counting\\n    with open(\\\"data/docred/ontology_constraints_docred.json\\\") as f:\\n        docred_constraints = json.load(f)\\n    docred_rel_types = docred_constraints.get(\\\"relation_types\\\", {})\\n    docred_name_to_id = build_name_to_id(docred_rel_types)\\n\\n    docred_configs = {\\n        \\\"unconstrained\\\": \\\"outputs/llama_docred_unconstrained.jsonl\\\",\\n        \\\"full_s1\\\": \\\"outputs/llama_docred_full_s1.jsonl\\\",\\n    }\\n    docred_registry_keys = {\\n        \\\"unconstrained\\\": \\\"llama_docred_unconstrained\\\",\\n        \\\"full_s1\\\": \\\"llama_docred_full_s1\\\",\\n    }\\n    docred_results = run_llama_dataset(\\\"DocRED\\\", docred_configs, docred_sample_stats_llama,\\n                                        (docred_rel_types, docred_name_to_id), docred_registry_keys)\\n\\n    if scierc_results is None or docred_results is None:\\n        print(\\\"\\\\nABORTED due to registry alignment failure.\\\")\\n        sys.exit(1)\\n\\n    def round_recursive(obj, decimals=6):\\n        if isinstance(obj, float):\\n            return round(obj, decimals)\\n        if isinstance(obj, dict):\\n            return {k: round_recursive(v, decimals) for k, v in obj.items()}\\n        if isinstance(obj, list):\\n            return [round_recursive(v, decimals) for v in obj]\\n        return obj\\n\\n    results = {\\n        \\\"scierc\\\": round_recursive(scierc_results),\\n        \\\"docred\\\": round_recursive(docred_results),\\n        \\\"metadata\\\": {\\n            \\\"model\\\": \\\"llama\\\",\\n            \\\"n_bootstrap\\\": 10000,\\n            \\\"ci_method\\\": \\\"percentile\\\",\\n            \\\"ci_level\\\": 0.95,\\n            \\\"seed\\\": 42,\\n            \\\"resample_unit\\\": \\\"sentence (SciERC) / document (DocRED)\\\",\\n            \\\"registry_tolerance_pp\\\": REGISTRY_TOL_PP,\\n        }\\n    }\\n\\n    output_path = \\\"outputs/bootstrap_ci_results_llama.json\\\"\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(results, f, indent=2)\\n    print(f\\\"\\\\nResults saved to {output_path}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
The output was truncated for `compute_bootstrap_ci_ft.py` and `compute_bootstrap_ci.py`. I need to see the critical `bootstrap_f1` and `paired_bootstrap_test` functions to determine whether they use corpus micro-F1 or document-level macro-F1. Let me read those specific functions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "d6adb60b-9f28-4f6f-a79c-817f1a74a84e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011U8cFGVJa3wQJNAYgCjmSK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11751,
      "cache_read_input_tokens": 26826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11751
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

_source line 18_

The key functions `bootstrap_f1` and `paired_bootstrap_test` were truncated. Let me read those specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "fae736cf-f785-49b6-b85d-0f7a207c6ef4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011U8cFGVJa3wQJNAYgCjmSK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11751,
      "cache_read_input_tokens": 26826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11751
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

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0172i7fhvgMDz9rZ7Z4y4B8J`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"def bootstrap_f1\\|def paired_bootstrap_test\\|def extract_stats\" /root/schema_semantic_constrained_ie/compute_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "d9f0a7bd-b70b-4ea8-a0ba-330a8e5f9159",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011U8cFGVJa3wQJNAYgCjmSK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11751,
      "cache_read_input_tokens": 26826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11751
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

_source line 20 · 2026-05-17T14:12:10.556Z_

<details><summary>↩ Tool result · `toolu_0172i7fhvgMDz9rZ7Z4y4B8J`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "1cfbefe1-5820-4eed-9e5d-4c1755a0d71b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CBLJX6HWMbvrDAmGT1ihfi`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"def bootstrap_f1\\|def paired_bootstrap_test\\|def extract_stats\" /root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "3a65760e-eb29-47cc-a3e6-8ba152bd627e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011U8cFGVJa3wQJNAYgCjmSK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11751,
      "cache_read_input_tokens": 26826,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11751
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

_source line 22 · 2026-05-17T14:12:11.168Z_

<details><summary>↩ Tool result · `toolu_01CBLJX6HWMbvrDAmGT1ihfi`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "3eeec971-7cdf-4d9d-bd4a-787f78592459",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PcY1KYgtuDMCqSajZwXJVk`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"def bootstrap_f1\" /root/schema_semantic_constrained_ie/compute_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "ce77b60e-9668-4a83-bfc2-aaea88d60bbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEECu9uYjsjcgLh1HTnMep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 38577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 24 · 2026-05-17T14:12:14.555Z_

<details><summary>↩ Tool result · `toolu_01PcY1KYgtuDMCqSajZwXJVk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"150:def bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "26725de8-abd0-48c0-8028-3d3c44160055",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"150:def bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"150:def bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KDrhNdWSAAgGoCaQMjN2iS`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"def paired_bootstrap_test\" /root/schema_semantic_constrained_ie/compute_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "f2573928-6f01-40c5-a7e0-ac2e2bcbc0a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEECu9uYjsjcgLh1HTnMep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 38577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BBdugHUzh9GhPsfo1wBe69`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"def extract_stats\" /root/schema_semantic_constrained_ie/compute_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "90ddd1ea-5a54-4ab3-a084-7ed7272e9228",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEECu9uYjsjcgLh1HTnMep",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 708,
      "cache_read_input_tokens": 38577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 708
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

_source line 27 · 2026-05-17T14:12:15.422Z_

<details><summary>↩ Tool result · `toolu_01KDrhNdWSAAgGoCaQMjN2iS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"176:def paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "569201c2-9d64-4a53-8a7d-5ee627139f32",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"176:def paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"176:def paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T14:12:15.950Z_

<details><summary>↩ Tool result · `toolu_01BBdugHUzh9GhPsfo1wBe69`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"227:def extract_stats(sample_stats, metric):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "25f5af8d-255e-4a03-abfc-cc7a62f2bc4b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"227:def extract_stats(sample_stats, metric):\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"227:def extract_stats(sample_stats, metric):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01554QdQ6rq6AdMAM9tZMG5E`</summary>

```json
{
  "server": "westd-16980",
  "command": "head -n 245 /root/schema_semantic_constrained_ie/compute_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "c81a93a6-8907-4e78-8b0a-a640676fbe9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015G7pr6ZsPHSXV6YMpBLmrT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 39285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 679
      },
      "output_tokens": 63,
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

_source line 30 · 2026-05-17T14:12:20.072Z_

<details><summary>↩ Tool result · `toolu_01554QdQ6rq6AdMAM9tZMG5E`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Compute bootstrap confidence intervals for SciERC and DocRED experiments.\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\nfrom pathlib import Path\\n\\n# --- SciERC normalization (from violation_checker.py) ---\\n\\nSCIERC_TYPE_MAP = {\\n    \\\"otherscientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other-scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other_scientific_term\\\": \\\"OtherScientificTerm\\\",\\n    \\\"scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other\\\": \\\"OtherScientificTerm\\\",\\n}\\n\\ndef scierc_normalize_type(t, valid_types):\\n    t_lower = t.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vt in valid_types:\\n        if t_lower == vt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vt\\n    if t_lower in SCIERC_TYPE_MAP:\\n        return SCIERC_TYPE_MAP[t_lower]\\n    return None\\n\\n# --- DocRED normalization (from violation_checker_docred.py) ---\\n\\nDOCRED_VALID_ENTITY_TYPES = {\\\"PER\\\", \\\"ORG\\\", \\\"LOC\\\", \\\"TIME\\\", \\\"NUM\\\", \\\"MISC\\\"}\\n\\nDOCRED_ENTITY_TYPE_ALIASES = {\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC',\\n    'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\ndef docred_normalize_entity_type(raw_type):\\n    t = raw_type.strip().upper()\\n    return DOCRED_ENTITY_TYPE_ALIASES.get(t, t)\\n\\ndef _levenshtein(s1, s2):\\n    if len(s1) < len(s2):\\n        return _levenshtein(s2, s1)\\n    if len(s2) == 0:\\n        return len(s1)\\n    prev_row = list(range(len(s2) + 1))\\n    for i, c1 in enumerate(s1):\\n        curr_row = [i + 1]\\n        for j, c2 in enumerate(s2):\\n            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (c1 != c2)))\\n        prev_row = curr_row\\n    return prev_row[-1]\\n\\ndef build_name_to_id(rel_types):\\n    name_to_id = {}\\n    for rid, rname in rel_types.items():\\n        name_to_id[rname.lower().strip()] = rid\\n        name_to_id[rid.lower()] = rid\\n    return name_to_id\\n\\ndef docred_normalize_relation(rel_name, rel_types, name_to_id):\\n    rel_key = name_to_id.get(rel_name.lower().strip())\\n    if rel_key:\\n        return rel_key\\n    rel_tokens = set(rel_name.strip().lower().split())\\n    best_pid, best_overlap = None, 0.0\\n    for rid, rname in rel_types.items():\\n        rname_tokens = set(rname.lower().split())\\n        if rel_tokens and rname_tokens:\\n            ratio = len(rel_tokens & rname_tokens) / len(rel_tokens | rname_tokens)\\n            if ratio > 0.8 and ratio > best_overlap:\\n                best_overlap = ratio\\n                best_pid = rid\\n    if best_pid:\\n        return best_pid\\n    for rid, rname in rel_types.items():\\n        if _levenshtein(rel_name.strip().lower(), rname.lower()) <= 2:\\n            return rid\\n    return None\\n\\n# --- Per-sample stats ---\\n\\ndef scierc_sample_stats(rec, valid_entity_types):\\n    parsed = rec.get(\\\"parsed_output\\\")\\n    gold_ents = rec.get(\\\"gold_entities\\\", [])\\n    gold_rels = rec.get(\\\"gold_relations\\\", [])\\n\\n    gold_ent_set = set((e[\\\"text\\\"].lower().strip(), e[\\\"type\\\"]) for e in gold_ents)\\n    gold_rel_set = set((r[\\\"head\\\"].lower().strip(), r[\\\"tail\\\"].lower().strip(), r[\\\"type\\\"]) for r in gold_rels)\\n\\n    if parsed is None:\\n        return {\\\"ent_tp\\\": 0, \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": 0,\\n                \\\"rel_tp\\\": 0, \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": 0}\\n\\n    entities = parsed.get(\\\"entities\\\", [])\\n    relations = parsed.get(\\\"relations\\\", [])\\n\\n    pred_ent_set = set()\\n    for e in entities:\\n        nt = scierc_normalize_type(e.get(\\\"type\\\", \\\"\\\"), valid_entity_types)\\n        if nt:\\n            pred_ent_set.add((e.get(\\\"text\\\", \\\"\\\").lower().strip(), nt))\\n\\n    pred_rel_set = set((r.get(\\\"head\\\", \\\"\\\").lower().strip(), r.get(\\\"tail\\\", \\\"\\\").lower().strip(), r.get(\\\"type\\\", \\\"\\\")) for r in relations)\\n\\n    return {\\n        \\\"ent_tp\\\": len(gold_ent_set & pred_ent_set), \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": len(pred_ent_set),\\n        \\\"rel_tp\\\": len(gold_rel_set & pred_rel_set), \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": len(pred_rel_set),\\n    }\\n\\ndef docred_sample_stats(rec, rel_types, name_to_id):\\n    pa\\n\\n... [截断: 输出过长，省略 1333 字符] ...\\n\\np, gold, pred):\\n    p = np.where(pred > 0, tp / pred, 0.0)\\n    r = np.where(gold > 0, tp / gold, 0.0)\\n    denom = p + r\\n    return np.where(denom > 0, 2 * p * r / denom, 0.0)\\n\\ndef bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    n = len(sample_stats)\\n    tps = np.array([s[\\\"tp\\\"] for s in sample_stats])\\n    golds = np.array([s[\\\"gold\\\"] for s in sample_stats])\\n    preds = np.array([s[\\\"pred\\\"] for s in sample_stats])\\n\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\n    tp_sums = tps[indices].sum(axis=1).astype(float)\\n    gold_sums = golds[indices].sum(axis=1).astype(float)\\n    pred_sums = preds[indices].sum(axis=1).astype(float)\\n\\n    f1_samples = _f1_from_arrays(tp_sums, gold_sums, pred_sums)\\n\\n    point_p = tps.sum() / preds.sum() if preds.sum() > 0 else 0.0\\n    point_r = tps.sum() / golds.sum() if golds.sum() > 0 else 0.0\\n    point_f1 = 2 * point_p * point_r / (point_p + point_r) if (point_p + point_r) > 0 else 0.0\\n\\n    return {\\n        \\\"point_estimate\\\": float(point_f1),\\n        \\\"bootstrap_mean\\\": float(np.mean(f1_samples)),\\n        \\\"ci_lower\\\": float(np.percentile(f1_samples, 2.5)),\\n        \\\"ci_upper\\\": float(np.percentile(f1_samples, 97.5)),\\n        \\\"std\\\": float(np.std(f1_samples)),\\n    }\\n\\ndef paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    n = len(stats_a)\\n    assert n == len(stats_b)\\n\\n    tps_a = np.array([s[\\\"tp\\\"] for s in stats_a])\\n    golds_a = np.array([s[\\\"gold\\\"] for s in stats_a])\\n    preds_a = np.array([s[\\\"pred\\\"] for s in stats_a])\\n    tps_b = np.array([s[\\\"tp\\\"] for s in stats_b])\\n    golds_b = np.array([s[\\\"gold\\\"] for s in stats_b])\\n    preds_b = np.array([s[\\\"pred\\\"] for s in stats_b])\\n\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\n\\n    f1_a = _f1_from_arrays(tps_a[indices].sum(axis=1).astype(float),\\n                           golds_a[indices].sum(axis=1).astype(float),\\n                           preds_a[indices].sum(axis=1).astype(float))\\n    f1_b = _f1_from_arrays(tps_b[indices].sum(axis=1).astype(float),\\n                           golds_b[indices].sum(axis=1).astype(float),\\n                           preds_b[indices].sum(axis=1).astype(float))\\n\\n    delta = f1_b - f1_a\\n    p_value = float(min(2 * min(np.mean(delta <= 0), np.mean(delta >= 0)), 1.0))\\n\\n    # Point estimates\\n    pa_p = tps_a.sum() / preds_a.sum() if preds_a.sum() > 0 else 0.0\\n    pa_r = tps_a.sum() / golds_a.sum() if golds_a.sum() > 0 else 0.0\\n    f1_a_point = 2 * pa_p * pa_r / (pa_p + pa_r) if (pa_p + pa_r) > 0 else 0.0\\n    pb_p = tps_b.sum() / preds_b.sum() if preds_b.sum() > 0 else 0.0\\n    pb_r = tps_b.sum() / golds_b.sum() if golds_b.sum() > 0 else 0.0\\n    f1_b_point = 2 * pb_p * pb_r / (pb_p + pb_r) if (pb_p + pb_r) > 0 else 0.0\\n\\n    return {\\n        \\\"delta_point\\\": float(f1_b_point - f1_a_point),\\n        \\\"delta_mean\\\": float(np.mean(delta)),\\n        \\\"ci_lower\\\": float(np.percentile(delta, 2.5)),\\n        \\\"ci_upper\\\": float(np.percentile(delta, 97.5)),\\n        \\\"p_value\\\": p_value,\\n    }\\n\\n# --- Main ---\\n\\ndef load_jsonl(path):\\n    records = []\\n    with open(path) as f:\\n        for line in f:\\n            line = line.strip()\\n            if line:\\n                records.append(json.loads(line))\\n    return records\\n\\ndef extract_stats(sample_stats, metric):\\n    prefix = \\\"ent\\\" if metric == \\\"entity\\\" else \\\"rel\\\"\\n    return [{\\\"tp\\\": s[f\\\"{prefix}_tp\\\"], \\\"gold\\\": s[f\\\"{prefix}_gold\\\"], \\\"pred\\\": s[f\\\"{prefix}_pred\\\"]} for s in sample_stats]\\n\\ndef verify_alignment(all_stats, dataset_name):\\n    configs = list(all_stats.keys())\\n    ref_ids = [s[\\\"doc_id\\\"] for s in all_stats[configs[0]]]\\n    for cfg in configs[1:]:\\n        ids = [s[\\\"doc_id\\\"] for s in all_stats[cfg]]\\n        if ids != ref_ids:\\n            print(f\\\"  WARNING: {dataset_name} {cfg} doc_ids differ from {configs[0]}!\\\")\\n            return False\\n    return True\\n\\ndef run_dataset(dataset_name, config_paths, stats_fn, stats_fn_args):\\n    print(f\\\"\\\\n{'='*50}\\\")\\n    print(f\\\"  {dataset_name}\\\")\\n    print(f\\\"{'='*50}\\\")\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "c98fb024-5207-4c2a-a657-ac01dcd37b19",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"Compute bootstrap confidence intervals for SciERC and DocRED experiments.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport json\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\n\\\\n# --- SciERC normalization (from violation_checker.py) ---\\\\n\\\\nSCIERC_TYPE_MAP = {\\\\n    \\\\\\\"otherscientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"other-scientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"other_scientific_term\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"scientificterm\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n    \\\\\\\"other\\\\\\\": \\\\\\\"OtherScientificTerm\\\\\\\",\\\\n}\\\\n\\\\ndef scierc_normalize_type(t, valid_types):\\\\n    t_lower = t.strip().lower().replace(\\\\\\\" \\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"-\\\\\\\", \\\\\\\"\\\\\\\")\\\\n    for vt in valid_types:\\\\n        if t_lower == vt.lower().replace(\\\\\\\" \\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"_\\\\\\\", \\\\\\\"\\\\\\\").replace(\\\\\\\"-\\\\\\\", \\\\\\\"\\\\\\\"):\\\\n            return vt\\\\n    if t_lower in SCIERC_TYPE_MAP:\\\\n        return SCIERC_TYPE_MAP[t_lower]\\\\n    return None\\\\n\\\\n# --- DocRED normalization (from violation_checker_docred.py) ---\\\\n\\\\nDOCRED_VALID_ENTITY_TYPES = {\\\\\\\"PER\\\\\\\", \\\\\\\"ORG\\\\\\\", \\\\\\\"LOC\\\\\\\", \\\\\\\"TIME\\\\\\\", \\\\\\\"NUM\\\\\\\", \\\\\\\"MISC\\\\\\\"}\\\\n\\\\nDOCRED_ENTITY_TYPE_ALIASES = {\\\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\\\n    'LOCATION': 'LOC',\\\\n    'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\\\n    'MISCELLANEOUS': 'MISC',\\\\n}\\\\n\\\\ndef docred_normalize_entity_type(raw_type):\\\\n    t = raw_type.strip().upper()\\\\n    return DOCRED_ENTITY_TYPE_ALIASES.get(t, t)\\\\n\\\\ndef _levenshtein(s1, s2):\\\\n    if len(s1) < len(s2):\\\\n        return _levenshtein(s2, s1)\\\\n    if len(s2) == 0:\\\\n        return len(s1)\\\\n    prev_row = list(range(len(s2) + 1))\\\\n    for i, c1 in enumerate(s1):\\\\n        curr_row = [i + 1]\\\\n        for j, c2 in enumerate(s2):\\\\n            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (c1 != c2)))\\\\n        prev_row = curr_row\\\\n    return prev_row[-1]\\\\n\\\\ndef build_name_to_id(rel_types):\\\\n    name_to_id = {}\\\\n    for rid, rname in rel_types.items():\\\\n        name_to_id[rname.lower().strip()] = rid\\\\n        name_to_id[rid.lower()] = rid\\\\n    return name_to_id\\\\n\\\\ndef docred_normalize_relation(rel_name, rel_types, name_to_id):\\\\n    rel_key = name_to_id.get(rel_name.lower().strip())\\\\n    if rel_key:\\\\n        return rel_key\\\\n    rel_tokens = set(rel_name.strip().lower().split())\\\\n    best_pid, best_overlap = None, 0.0\\\\n    for rid, rname in rel_types.items():\\\\n        rname_tokens = set(rname.lower().split())\\\\n        if rel_tokens and rname_tokens:\\\\n            ratio = len(rel_tokens & rname_tokens) / len(rel_tokens | rname_tokens)\\\\n            if ratio > 0.8 and ratio > best_overlap:\\\\n                best_overlap = ratio\\\\n                best_pid = rid\\\\n    if best_pid:\\\\n        return best_pid\\\\n    for rid, rname in rel_types.items():\\\\n        if _levenshtein(rel_name.strip().lower(), rname.lower()) <= 2:\\\\n            return rid\\\\n    return None\\\\n\\\\n# --- Per-sample stats ---\\\\n\\\\ndef scierc_sample_stats(rec, valid_entity_types):\\\\n    parsed = rec.get(\\\\\\\"parsed_output\\\\\\\")\\\\n    gold_ents = rec.get(\\\\\\\"gold_entities\\\\\\\", [])\\\\n    gold_rels = rec.get(\\\\\\\"gold_relations\\\\\\\", [])\\\\n\\\\n    gold_ent_set = set((e[\\\\\\\"text\\\\\\\"].lower().strip(), e[\\\\\\\"type\\\\\\\"]) for e in gold_ents)\\\\n    gold_rel_set = set((r[\\\\\\\"head\\\\\\\"].lower().strip(), r[\\\\\\\"tail\\\\\\\"].lower().strip(), r[\\\\\\\"type\\\\\\\"]) for r in gold_rels)\\\\n\\\\n    if parsed is None:\\\\n        return {\\\\\\\"ent_tp\\\\\\\": 0, \\\\\\\"ent_gold\\\\\\\": len(gold_ent_set), \\\\\\\"ent_pred\\\\\\\": 0,\\\\n                \\\\\\\"rel_tp\\\\\\\": 0, \\\\\\\"rel_gold\\\\\\\": len(gold_rel_set), \\\\\\\"rel_pred\\\\\\\": 0}\\\\n\\\\n    entities = parsed.get(\\\\\\\"entities\\\\\\\", [])\\\\n    relations = parsed.get(\\\\\\\"relations\\\\\\\", [])\\\\n\\\\n    pred_ent_set = set()\\\\n    for e in entities:\\\\n        nt = scierc_normalize_type(e.get(\\\\\\\"type\\\\\\\", \\\\\\\"\\\\\\\"), valid_entity_types)\\\\n        if nt:\\\\n            pred_ent_set.add((e.get(\\\\\\\"text\\\\\\\", \\\\\\\"\\\\\\\").lower().strip(), nt))\\\\n\\\\n    pred_rel_set = set((r.get(\\\\\\\"head\\\\\\\", \\\\\\\"\\\\\\\").lower().strip(), r.get(\\\\\\\"tail\\\\\\\", \\\\\\\"\\\\\\\").lower().strip(), r.get(\\\\\\\"type\\\\\\\", \\\\\\\"\\\\\\\")) for r in relations)\\\\n\\\\n    return {\\\\n        \\\\\\\"ent_tp\\\\\\\": len(gold_ent_set & pred_ent_set), \\\\\\\"ent_gold\\\\\\\": len(gold_ent_set), \\\\\\\"ent_pred\\\\\\\": len(pred_ent_set),\\\\n        \\\\\\\"rel_tp\\\\\\\": len(gold_rel_set & pred_rel_set), \\\\\\\"rel_gold\\\\\\\": len(gold_rel_set), \\\\\\\"rel_pred\\\\\\\": len(pred_rel_set),\\\\n    }\\\\n\\\\ndef docred_sample_stats(rec, rel_types, name_to_id):\\\\n    pa\\\\n\\\\n... [截断: 输出过长，省略 1333 字符] ...\\\\n\\\\np, gold, pred):\\\\n    p = np.where(pred > 0, tp / pred, 0.0)\\\\n    r = np.where(gold > 0, tp / gold, 0.0)\\\\n    denom = p + r\\\\n    return np.where(denom > 0, 2 * p * r / denom, 0.0)\\\\n\\\\ndef bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\\\n    rng = np.random.RandomState(seed)\\\\n    n = len(sample_stats)\\\\n    tps = np.array([s[\\\\\\\"tp\\\\\\\"] for s in sample_stats])\\\\n    golds = np.array([s[\\\\\\\"gold\\\\\\\"] for s in sample_stats])\\\\n    preds = np.array([s[\\\\\\\"pred\\\\\\\"] for s in sample_stats])\\\\n\\\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\\\n    tp_sums = tps[indices].sum(axis=1).astype(float)\\\\n    gold_sums = golds[indices].sum(axis=1).astype(float)\\\\n    pred_sums = preds[indices].sum(axis=1).astype(float)\\\\n\\\\n    f1_samples = _f1_from_arrays(tp_sums, gold_sums, pred_sums)\\\\n\\\\n    point_p = tps.sum() / preds.sum() if preds.sum() > 0 else 0.0\\\\n    point_r = tps.sum() / golds.sum() if golds.sum() > 0 else 0.0\\\\n    point_f1 = 2 * point_p * point_r / (point_p + point_r) if (point_p + point_r) > 0 else 0.0\\\\n\\\\n    return {\\\\n        \\\\\\\"point_estimate\\\\\\\": float(point_f1),\\\\n        \\\\\\\"bootstrap_mean\\\\\\\": float(np.mean(f1_samples)),\\\\n        \\\\\\\"ci_lower\\\\\\\": float(np.percentile(f1_samples, 2.5)),\\\\n        \\\\\\\"ci_upper\\\\\\\": float(np.percentile(f1_samples, 97.5)),\\\\n        \\\\\\\"std\\\\\\\": float(np.std(f1_samples)),\\\\n    }\\\\n\\\\ndef paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\\\n    rng = np.random.RandomState(seed)\\\\n    n = len(stats_a)\\\\n    assert n == len(stats_b)\\\\n\\\\n    tps_a = np.array([s[\\\\\\\"tp\\\\\\\"] for s in stats_a])\\\\n    golds_a = np.array([s[\\\\\\\"gold\\\\\\\"] for s in stats_a])\\\\n    preds_a = np.array([s[\\\\\\\"pred\\\\\\\"] for s in stats_a])\\\\n    tps_b = np.array([s[\\\\\\\"tp\\\\\\\"] for s in stats_b])\\\\n    golds_b = np.array([s[\\\\\\\"gold\\\\\\\"] for s in stats_b])\\\\n    preds_b = np.array([s[\\\\\\\"pred\\\\\\\"] for s in stats_b])\\\\n\\\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\\\n\\\\n    f1_a = _f1_from_arrays(tps_a[indices].sum(axis=1).astype(float),\\\\n                           golds_a[indices].sum(axis=1).astype(float),\\\\n                           preds_a[indices].sum(axis=1).astype(float))\\\\n    f1_b = _f1_from_arrays(tps_b[indices].sum(axis=1).astype(float),\\\\n                           golds_b[indices].sum(axis=1).astype(float),\\\\n                           preds_b[indices].sum(axis=1).astype(float))\\\\n\\\\n    delta = f1_b - f1_a\\\\n    p_value = float(min(2 * min(np.mean(delta <= 0), np.mean(delta >= 0)), 1.0))\\\\n\\\\n    # Point estimates\\\\n    pa_p = tps_a.sum() / preds_a.sum() if preds_a.sum() > 0 else 0.0\\\\n    pa_r = tps_a.sum() / golds_a.sum() if golds_a.sum() > 0 else 0.0\\\\n    f1_a_point = 2 * pa_p * pa_r / (pa_p + pa_r) if (pa_p + pa_r) > 0 else 0.0\\\\n    pb_p = tps_b.sum() / preds_b.sum() if preds_b.sum() > 0 else 0.0\\\\n    pb_r = tps_b.sum() / golds_b.sum() if golds_b.sum() > 0 else 0.0\\\\n    f1_b_point = 2 * pb_p * pb_r / (pb_p + pb_r) if (pb_p + pb_r) > 0 else 0.0\\\\n\\\\n    return {\\\\n        \\\\\\\"delta_point\\\\\\\": float(f1_b_point - f1_a_point),\\\\n        \\\\\\\"delta_mean\\\\\\\": float(np.mean(delta)),\\\\n        \\\\\\\"ci_lower\\\\\\\": float(np.percentile(delta, 2.5)),\\\\n        \\\\\\\"ci_upper\\\\\\\": float(np.percentile(delta, 97.5)),\\\\n        \\\\\\\"p_value\\\\\\\": p_value,\\\\n    }\\\\n\\\\n# --- Main ---\\\\n\\\\ndef load_jsonl(path):\\\\n    records = []\\\\n    with open(path) as f:\\\\n        for line in f:\\\\n            line = line.strip()\\\\n            if line:\\\\n                records.append(json.loads(line))\\\\n    return records\\\\n\\\\ndef extract_stats(sample_stats, metric):\\\\n    prefix = \\\\\\\"ent\\\\\\\" if metric == \\\\\\\"entity\\\\\\\" else \\\\\\\"rel\\\\\\\"\\\\n    return [{\\\\\\\"tp\\\\\\\": s[f\\\\\\\"{prefix}_tp\\\\\\\"], \\\\\\\"gold\\\\\\\": s[f\\\\\\\"{prefix}_gold\\\\\\\"], \\\\\\\"pred\\\\\\\": s[f\\\\\\\"{prefix}_pred\\\\\\\"]} for s in sample_stats]\\\\n\\\\ndef verify_alignment(all_stats, dataset_name):\\\\n    configs = list(all_stats.keys())\\\\n    ref_ids = [s[\\\\\\\"doc_id\\\\\\\"] for s in all_stats[configs[0]]]\\\\n    for cfg in configs[1:]:\\\\n        ids = [s[\\\\\\\"doc_id\\\\\\\"] for s in all_stats[cfg]]\\\\n        if ids != ref_ids:\\\\n            print(f\\\\\\\"  WARNING: {dataset_name} {cfg} doc_ids differ from {configs[0]}!\\\\\\\")\\\\n            return False\\\\n    return True\\\\n\\\\ndef run_dataset(dataset_name, config_paths, stats_fn, stats_fn_args):\\\\n    print(f\\\\\\\"\\\\\\\\n{'='*50}\\\\\\\")\\\\n    print(f\\\\\\\"  {dataset_name}\\\\\\\")\\\\n    print(f\\\\\\\"{'='*50}\\\\\\\")\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Compute bootstrap confidence intervals for SciERC and DocRED experiments.\\\"\\\"\\\"\\n\\nimport json\\nimport numpy as np\\nfrom pathlib import Path\\n\\n# --- SciERC normalization (from violation_checker.py) ---\\n\\nSCIERC_TYPE_MAP = {\\n    \\\"otherscientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other-scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other_scientific_term\\\": \\\"OtherScientificTerm\\\",\\n    \\\"scientificterm\\\": \\\"OtherScientificTerm\\\",\\n    \\\"other\\\": \\\"OtherScientificTerm\\\",\\n}\\n\\ndef scierc_normalize_type(t, valid_types):\\n    t_lower = t.strip().lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\")\\n    for vt in valid_types:\\n        if t_lower == vt.lower().replace(\\\" \\\", \\\"\\\").replace(\\\"_\\\", \\\"\\\").replace(\\\"-\\\", \\\"\\\"):\\n            return vt\\n    if t_lower in SCIERC_TYPE_MAP:\\n        return SCIERC_TYPE_MAP[t_lower]\\n    return None\\n\\n# --- DocRED normalization (from violation_checker_docred.py) ---\\n\\nDOCRED_VALID_ENTITY_TYPES = {\\\"PER\\\", \\\"ORG\\\", \\\"LOC\\\", \\\"TIME\\\", \\\"NUM\\\", \\\"MISC\\\"}\\n\\nDOCRED_ENTITY_TYPE_ALIASES = {\\n    'PERSON': 'PER', 'PEOPLE': 'PER',\\n    'ORGANIZATION': 'ORG', 'ORGANISATION': 'ORG',\\n    'LOCATION': 'LOC',\\n    'NUMBER': 'NUM', 'NUMERICAL': 'NUM',\\n    'MISCELLANEOUS': 'MISC',\\n}\\n\\ndef docred_normalize_entity_type(raw_type):\\n    t = raw_type.strip().upper()\\n    return DOCRED_ENTITY_TYPE_ALIASES.get(t, t)\\n\\ndef _levenshtein(s1, s2):\\n    if len(s1) < len(s2):\\n        return _levenshtein(s2, s1)\\n    if len(s2) == 0:\\n        return len(s1)\\n    prev_row = list(range(len(s2) + 1))\\n    for i, c1 in enumerate(s1):\\n        curr_row = [i + 1]\\n        for j, c2 in enumerate(s2):\\n            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (c1 != c2)))\\n        prev_row = curr_row\\n    return prev_row[-1]\\n\\ndef build_name_to_id(rel_types):\\n    name_to_id = {}\\n    for rid, rname in rel_types.items():\\n        name_to_id[rname.lower().strip()] = rid\\n        name_to_id[rid.lower()] = rid\\n    return name_to_id\\n\\ndef docred_normalize_relation(rel_name, rel_types, name_to_id):\\n    rel_key = name_to_id.get(rel_name.lower().strip())\\n    if rel_key:\\n        return rel_key\\n    rel_tokens = set(rel_name.strip().lower().split())\\n    best_pid, best_overlap = None, 0.0\\n    for rid, rname in rel_types.items():\\n        rname_tokens = set(rname.lower().split())\\n        if rel_tokens and rname_tokens:\\n            ratio = len(rel_tokens & rname_tokens) / len(rel_tokens | rname_tokens)\\n            if ratio > 0.8 and ratio > best_overlap:\\n                best_overlap = ratio\\n                best_pid = rid\\n    if best_pid:\\n        return best_pid\\n    for rid, rname in rel_types.items():\\n        if _levenshtein(rel_name.strip().lower(), rname.lower()) <= 2:\\n            return rid\\n    return None\\n\\n# --- Per-sample stats ---\\n\\ndef scierc_sample_stats(rec, valid_entity_types):\\n    parsed = rec.get(\\\"parsed_output\\\")\\n    gold_ents = rec.get(\\\"gold_entities\\\", [])\\n    gold_rels = rec.get(\\\"gold_relations\\\", [])\\n\\n    gold_ent_set = set((e[\\\"text\\\"].lower().strip(), e[\\\"type\\\"]) for e in gold_ents)\\n    gold_rel_set = set((r[\\\"head\\\"].lower().strip(), r[\\\"tail\\\"].lower().strip(), r[\\\"type\\\"]) for r in gold_rels)\\n\\n    if parsed is None:\\n        return {\\\"ent_tp\\\": 0, \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": 0,\\n                \\\"rel_tp\\\": 0, \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": 0}\\n\\n    entities = parsed.get(\\\"entities\\\", [])\\n    relations = parsed.get(\\\"relations\\\", [])\\n\\n    pred_ent_set = set()\\n    for e in entities:\\n        nt = scierc_normalize_type(e.get(\\\"type\\\", \\\"\\\"), valid_entity_types)\\n        if nt:\\n            pred_ent_set.add((e.get(\\\"text\\\", \\\"\\\").lower().strip(), nt))\\n\\n    pred_rel_set = set((r.get(\\\"head\\\", \\\"\\\").lower().strip(), r.get(\\\"tail\\\", \\\"\\\").lower().strip(), r.get(\\\"type\\\", \\\"\\\")) for r in relations)\\n\\n    return {\\n        \\\"ent_tp\\\": len(gold_ent_set & pred_ent_set), \\\"ent_gold\\\": len(gold_ent_set), \\\"ent_pred\\\": len(pred_ent_set),\\n        \\\"rel_tp\\\": len(gold_rel_set & pred_rel_set), \\\"rel_gold\\\": len(gold_rel_set), \\\"rel_pred\\\": len(pred_rel_set),\\n    }\\n\\ndef docred_sample_stats(rec, rel_types, name_to_id):\\n    pa\\n\\n... [截断: 输出过长，省略 1333 字符] ...\\n\\np, gold, pred):\\n    p = np.where(pred > 0, tp / pred, 0.0)\\n    r = np.where(gold > 0, tp / gold, 0.0)\\n    denom = p + r\\n    return np.where(denom > 0, 2 * p * r / denom, 0.0)\\n\\ndef bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    n = len(sample_stats)\\n    tps = np.array([s[\\\"tp\\\"] for s in sample_stats])\\n    golds = np.array([s[\\\"gold\\\"] for s in sample_stats])\\n    preds = np.array([s[\\\"pred\\\"] for s in sample_stats])\\n\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\n    tp_sums = tps[indices].sum(axis=1).astype(float)\\n    gold_sums = golds[indices].sum(axis=1).astype(float)\\n    pred_sums = preds[indices].sum(axis=1).astype(float)\\n\\n    f1_samples = _f1_from_arrays(tp_sums, gold_sums, pred_sums)\\n\\n    point_p = tps.sum() / preds.sum() if preds.sum() > 0 else 0.0\\n    point_r = tps.sum() / golds.sum() if golds.sum() > 0 else 0.0\\n    point_f1 = 2 * point_p * point_r / (point_p + point_r) if (point_p + point_r) > 0 else 0.0\\n\\n    return {\\n        \\\"point_estimate\\\": float(point_f1),\\n        \\\"bootstrap_mean\\\": float(np.mean(f1_samples)),\\n        \\\"ci_lower\\\": float(np.percentile(f1_samples, 2.5)),\\n        \\\"ci_upper\\\": float(np.percentile(f1_samples, 97.5)),\\n        \\\"std\\\": float(np.std(f1_samples)),\\n    }\\n\\ndef paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    n = len(stats_a)\\n    assert n == len(stats_b)\\n\\n    tps_a = np.array([s[\\\"tp\\\"] for s in stats_a])\\n    golds_a = np.array([s[\\\"gold\\\"] for s in stats_a])\\n    preds_a = np.array([s[\\\"pred\\\"] for s in stats_a])\\n    tps_b = np.array([s[\\\"tp\\\"] for s in stats_b])\\n    golds_b = np.array([s[\\\"gold\\\"] for s in stats_b])\\n    preds_b = np.array([s[\\\"pred\\\"] for s in stats_b])\\n\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\n\\n    f1_a = _f1_from_arrays(tps_a[indices].sum(axis=1).astype(float),\\n                           golds_a[indices].sum(axis=1).astype(float),\\n                           preds_a[indices].sum(axis=1).astype(float))\\n    f1_b = _f1_from_arrays(tps_b[indices].sum(axis=1).astype(float),\\n                           golds_b[indices].sum(axis=1).astype(float),\\n                           preds_b[indices].sum(axis=1).astype(float))\\n\\n    delta = f1_b - f1_a\\n    p_value = float(min(2 * min(np.mean(delta <= 0), np.mean(delta >= 0)), 1.0))\\n\\n    # Point estimates\\n    pa_p = tps_a.sum() / preds_a.sum() if preds_a.sum() > 0 else 0.0\\n    pa_r = tps_a.sum() / golds_a.sum() if golds_a.sum() > 0 else 0.0\\n    f1_a_point = 2 * pa_p * pa_r / (pa_p + pa_r) if (pa_p + pa_r) > 0 else 0.0\\n    pb_p = tps_b.sum() / preds_b.sum() if preds_b.sum() > 0 else 0.0\\n    pb_r = tps_b.sum() / golds_b.sum() if golds_b.sum() > 0 else 0.0\\n    f1_b_point = 2 * pb_p * pb_r / (pb_p + pb_r) if (pb_p + pb_r) > 0 else 0.0\\n\\n    return {\\n        \\\"delta_point\\\": float(f1_b_point - f1_a_point),\\n        \\\"delta_mean\\\": float(np.mean(delta)),\\n        \\\"ci_lower\\\": float(np.percentile(delta, 2.5)),\\n        \\\"ci_upper\\\": float(np.percentile(delta, 97.5)),\\n        \\\"p_value\\\": p_value,\\n    }\\n\\n# --- Main ---\\n\\ndef load_jsonl(path):\\n    records = []\\n    with open(path) as f:\\n        for line in f:\\n            line = line.strip()\\n            if line:\\n                records.append(json.loads(line))\\n    return records\\n\\ndef extract_stats(sample_stats, metric):\\n    prefix = \\\"ent\\\" if metric == \\\"entity\\\" else \\\"rel\\\"\\n    return [{\\\"tp\\\": s[f\\\"{prefix}_tp\\\"], \\\"gold\\\": s[f\\\"{prefix}_gold\\\"], \\\"pred\\\": s[f\\\"{prefix}_pred\\\"]} for s in sample_stats]\\n\\ndef verify_alignment(all_stats, dataset_name):\\n    configs = list(all_stats.keys())\\n    ref_ids = [s[\\\"doc_id\\\"] for s in all_stats[configs[0]]]\\n    for cfg in configs[1:]:\\n        ids = [s[\\\"doc_id\\\"] for s in all_stats[cfg]]\\n        if ids != ref_ids:\\n            print(f\\\"  WARNING: {dataset_name} {cfg} doc_ids differ from {configs[0]}!\\\")\\n            return False\\n    return True\\n\\ndef run_dataset(dataset_name, config_paths, stats_fn, stats_fn_args):\\n    print(f\\\"\\\\n{'='*50}\\\")\\n    print(f\\\"  {dataset_name}\\\")\\n    print(f\\\"{'='*50}\\\")\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

````text
Now I can see the critical functions. Let me analyze:

**`bootstrap_f1` function (line 150)**:
```python
def bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(sample_stats)
    tps = np.array([s["tp"] for s in sample_stats])
    golds = np.array([s["gold"] for s in sample_stats])


```

Extracting predictions and computing bootstrap samples...

```

The key insight is that this computes corpus-level micro-F1 by aggregating TP, gold, and pred counts across resampled batches before calculating F1, rather than computing F1 per sample first. The `paired_bootstrap_test` function applies the same logic to compare two systems.

Now I need to check whether the FT script uses these same functions or implements its own version.

```

python
def _f1_from_arrays(tp, gold, pred):
    p = np.where(pred > 0, tp / pred, 0.0)
    r = np.where(gold > 0, tp / gold, 0.0)
    denom = p + r
    return np.where(denom > 0, 2 * p * r / denom, 0.0)
```

Checking FT script implementation...
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "7254effa-8a17-4860-b40c-6cb869e862f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpEcV1WRjK7jXeshcAHZks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3942,
      "cache_read_input_tokens": 39964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3942
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

_source line 32_

Now I can see the critical functions clearly. Let me also check if the FT script has its own `bootstrap_f1` or imports from the ZS script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "7f16e585-5078-4f5c-8305-4a1ee78c0af3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpEcV1WRjK7jXeshcAHZks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3942,
      "cache_read_input_tokens": 39964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3942
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

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014BG9r61uXv1aNBvnVLoHg2`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"def bootstrap_f1\\|def paired_bootstrap_test\\|def _f1_from_arrays\\|import.*bootstrap\" /root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "251fcfc7-513d-4056-8f7f-f929e564287f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpEcV1WRjK7jXeshcAHZks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3942,
      "cache_read_input_tokens": 39964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3942
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

_source line 34 · 2026-05-17T14:12:34.707Z_

<details><summary>↩ Tool result · `toolu_014BG9r61uXv1aNBvnVLoHg2`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "57091791-fcb4-459d-a0ad-2a9105cf36d8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DZU1JNXJSv5zoRK1C1c2G8`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"def bootstrap_f1\" /root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "3f5b44d8-900d-4b83-969a-be21d9554516",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fa4jKbxM4Lxbaoy2qtDKa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 43906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
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

_source line 36 · 2026-05-17T14:12:38.297Z_

<details><summary>↩ Tool result · `toolu_01DZU1JNXJSv5zoRK1C1c2G8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"153:def bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "45a3e588-d357-469f-81d1-dd161816a0ff",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"153:def bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"153:def bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NhPsDdspM68L6X3SWrVfdD`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"def _f1_from_arrays\" /root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "cdf82733-c509-4065-8e2f-010e4823cded",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fa4jKbxM4Lxbaoy2qtDKa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 43906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
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

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015FYPgDzxt3AdQyefcQTpvE`</summary>

```json
{
  "server": "westd-16980",
  "command": "grep -n \"def paired_bootstrap_test\" /root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "936776bf-69e2-4be2-b079-164e5cacfb88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fa4jKbxM4Lxbaoy2qtDKa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 993,
      "cache_read_input_tokens": 43906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 993
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

_source line 39 · 2026-05-17T14:12:38.910Z_

<details><summary>↩ Tool result · `toolu_01NhPsDdspM68L6X3SWrVfdD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"148:def _f1_from_arrays(tp, gold, pred):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "eb7c6a89-4aaf-463a-8546-8678b71afd18",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"148:def _f1_from_arrays(tp, gold, pred):\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"148:def _f1_from_arrays(tp, gold, pred):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T14:12:39.444Z_

<details><summary>↩ Tool result · `toolu_015FYPgDzxt3AdQyefcQTpvE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"179:def paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "6778524a-f664-4692-93de-0f2f83b9149d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"179:def paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.53}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"179:def paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LDViVKffm4iGutrrHbX58s`</summary>

```json
{
  "server": "westd-16980",
  "command": "tail -n +148 /root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "8684a4e2-29e8-411c-8181-e1f20bfc8788",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAwB7FjhC346P2Znnzf3ta",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 44899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
      },
      "output_tokens": 63,
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

_source line 42 · 2026-05-17T14:12:43.364Z_

<details><summary>↩ Tool result · `toolu_01LDViVKffm4iGutrrHbX58s`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"def _f1_from_arrays(tp, gold, pred):\\n    p = np.where(pred > 0, tp / pred, 0.0)\\n    r = np.where(gold > 0, tp / gold, 0.0)\\n    return np.where((p + r) > 0, 2 * p * r / (p + r), 0.0)\\n\\ndef bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    n = len(sample_stats)\\n    tps = np.array([s[\\\"tp\\\"] for s in sample_stats])\\n    golds = np.array([s[\\\"gold\\\"] for s in sample_stats])\\n    preds = np.array([s[\\\"pred\\\"] for s in sample_stats])\\n\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\n    tp_sums = tps[indices].sum(axis=1).astype(float)\\n    gold_sums = golds[indices].sum(axis=1).astype(float)\\n    pred_sums = preds[indices].sum(axis=1).astype(float)\\n\\n    f1_samples = _f1_from_arrays(tp_sums, gold_sums, pred_sums)\\n\\n    point_p = tps.sum() / preds.sum() if preds.sum() > 0 else 0.0\\n    point_r = tps.sum() / golds.sum() if golds.sum() > 0 else 0.0\\n    point_f1 = 2 * point_p * point_r / (point_p + point_r) if (point_p + point_r) > 0 else 0.0\\n\\n    return {\\n        \\\"point_estimate\\\": float(point_f1),\\n        \\\"bootstrap_mean\\\": float(np.mean(f1_samples)),\\n        \\\"ci_lower\\\": float(np.percentile(f1_samples, 2.5)),\\n        \\\"ci_upper\\\": float(np.percentile(f1_samples, 97.5)),\\n        \\\"std\\\": float(np.std(f1_samples)),\\n    }\\n\\ndef paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    n = len(stats_a)\\n    assert n == len(stats_b), f\\\"Mismatched lengths: {n} vs {len(stats_b)}\\\"\\n\\n    tps_a = np.array([s[\\\"tp\\\"] for s in stats_a])\\n    golds_a = np.array([s[\\\"gold\\\"] for s in stats_a])\\n    preds_a = np.array([s[\\\"pred\\\"] for s in stats_a])\\n    tps_b = np.array([s[\\\"tp\\\"] for s in stats_b])\\n    golds_b = np.array([s[\\\"gold\\\"] for s in stats_b])\\n    preds_b = np.array([s[\\\"pred\\\"] for s in stats_b])\\n\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\n\\n    f1_a = _f1_from_arrays(tps_a[indices].sum(axis=1).astype(float),\\n                           golds_a[indices].sum(axis=1).astype(float),\\n                           preds_a[indices].sum(axis=1).astype(float))\\n    f1_b = _f1_from_arrays(tps_b[indices].sum(axis=1).astype(float),\\n                           golds_b[indices].sum(axis=1).astype(float),\\n                           preds_b[indices].sum(axis=1).astype(float))\\n\\n    delta = f1_b - f1_a\\n    p_value = float(min(2 * min(np.mean(delta <= 0), np.mean(delta >= 0)), 1.0))\\n\\n    pa_p = tps_a.sum() / preds_a.sum() if preds_a.sum() > 0 else 0.0\\n    pa_r = tps_a.sum() / golds_a.sum() if golds_a.sum() > 0 else 0.0\\n    f1_a_point = 2 * pa_p * pa_r / (pa_p + pa_r) if (pa_p + pa_r) > 0 else 0.0\\n    pb_p = tps_b.sum() / preds_b.sum() if preds_b.sum() > 0 else 0.0\\n    pb_r = tps_b.sum() / golds_b.sum() if golds_b.sum() > 0 else 0.0\\n    f1_b_point = 2 * pb_p * pb_r / (pb_p + pb_r) if (pb_p + pb_r) > 0 else 0.0\\n\\n    return {\\n        \\\"f1_a\\\": float(f1_a_point),\\n        \\\"f1_b\\\": float(f1_b_point),\\n        \\\"delta_point\\\": float(f1_b_point - f1_a_point),\\n        \\\"delta_mean\\\": float(np.mean(delta)),\\n        \\\"ci_lower\\\": float(np.percentile(delta, 2.5)),\\n        \\\"ci_upper\\\": float(np.percentile(delta, 97.5)),\\n        \\\"p_value\\\": p_value,\\n    }\\n\\n# --- Main ---\\n\\ndef load_jsonl(path):\\n    records = []\\n    with open(path) as f:\\n        for line in f:\\n            line = line.strip()\\n            if line:\\n                records.append(json.loads(line))\\n    return records\\n\\ndef extract_stats(sample_stats, metric):\\n    prefix = \\\"ent\\\" if metric == \\\"entity\\\" else \\\"rel\\\"\\n    return [{\\\"tp\\\": s[f\\\"{prefix}_tp\\\"], \\\"gold\\\": s[f\\\"{prefix}_gold\\\"], \\\"pred\\\": s[f\\\"{prefix}_pred\\\"]} for s in sample_stats]\\n\\nif __name__ == \\\"__main__\\\":\\n    import os\\n    os.chdir(\\\"/root/schema_semantic_constrained_ie\\\")\\n\\n    # Load ontologies\\n    with open(\\\"ontology_constraints.json\\\") as f:\\n        scierc_constraints = json.load(f)\\n    scierc_valid_types = scierc_constraints[\\\"entity_types\\\"]\\n\\n    with open(\\\"data/docred/ontology_constraints_docred.json\\\") as f:\\n        docred_constraints = json.load(f)\\n    docred_rel_types = docred_constraints.get(\\\"rel\\n\\n... [截断: 输出过长，省略 1831 字符] ...\\n\\nids, f\\\"Doc ID mismatch in {setting_name}!\\\"\\n\\n        # Compute per-sample stats\\n        if cfg[\\\"dataset\\\"] == \\\"scierc\\\":\\n            unc_stats = [scierc_sample_stats(r, scierc_valid_types) for r in unc_records]\\n            con_stats = [scierc_sample_stats(r, scierc_valid_types) for r in con_records]\\n        else:\\n            unc_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in unc_records]\\n            con_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in con_records]\\n\\n        # Bootstrap CI for each config\\n        for label, stats in [(\\\"unconstrained\\\", unc_stats), (\\\"constrained\\\", con_stats)]:\\n            ent_ci = bootstrap_f1(extract_stats(stats, \\\"entity\\\"))\\n            rel_ci = bootstrap_f1(extract_stats(stats, \\\"relation\\\"))\\n            print(f\\\"  {label}: E-F1={100*ent_ci['point_estimate']:.2f}% [{100*ent_ci['ci_lower']:.2f}, {100*ent_ci['ci_upper']:.2f}], \\\"\\n                  f\\\"R-F1={100*rel_ci['point_estimate']:.2f}% [{100*rel_ci['ci_lower']:.2f}, {100*rel_ci['ci_upper']:.2f}]\\\")\\n\\n        # Paired test: constrained - unconstrained\\n        ent_test = paired_bootstrap_test(\\n            extract_stats(unc_stats, \\\"entity\\\"),\\n            extract_stats(con_stats, \\\"entity\\\"))\\n        rel_test = paired_bootstrap_test(\\n            extract_stats(unc_stats, \\\"relation\\\"),\\n            extract_stats(con_stats, \\\"relation\\\"))\\n\\n        print(f\\\"\\\\n  Paired test (constrained - unconstrained):\\\")\\n        print(f\\\"    ΔE-F1 = {100*ent_test['delta_point']:+.2f}pp  95%CI [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}]  p={ent_test['p_value']:.4f}\\\")\\n        print(f\\\"    ΔR-F1 = {100*rel_test['delta_point']:+.2f}pp  95%CI [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}]  p={rel_test['p_value']:.4f}\\\")\\n\\n        sig_rel = \\\"***\\\" if rel_test['p_value'] < 0.001 else \\\"**\\\" if rel_test['p_value'] < 0.01 else \\\"*\\\" if rel_test['p_value'] < 0.05 else \\\"n.s.\\\"\\n        sig_ent = \\\"***\\\" if ent_test['p_value'] < 0.001 else \\\"**\\\" if ent_test['p_value'] < 0.01 else \\\"*\\\" if ent_test['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"    Significance: E-F1 {sig_ent}, R-F1 {sig_rel}\\\")\\n\\n        all_results[setting_name] = {\\n            \\\"n_samples\\\": len(unc_records),\\n            \\\"ent_test\\\": ent_test,\\n            \\\"rel_test\\\": rel_test,\\n        }\\n\\n    # Summary table\\n    print(f\\\"\\\\n\\\\n{'='*70}\\\")\\n    print(\\\"  SUMMARY TABLE\\\")\\n    print(f\\\"{'='*70}\\\")\\n    print(f\\\"{'Setting':<22} {'ΔR-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\")\\n    print(f\\\"{'─'*70}\\\")\\n    for name, res in all_results.items():\\n        rt = res[\\\"rel_test\\\"]\\n        sig = \\\"***\\\" if rt['p_value'] < 0.001 else \\\"**\\\" if rt['p_value'] < 0.01 else \\\"*\\\" if rt['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"{name:<22} {100*rt['delta_point']:+.2f}        [{100*rt['ci_lower']:+.2f}, {100*rt['ci_upper']:+.2f}]    {rt['p_value']:.4f}     {sig}\\\")\\n\\n    print(f\\\"\\\\n{'Setting':<22} {'ΔE-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\")\\n    print(f\\\"{'─'*70}\\\")\\n    for name, res in all_results.items():\\n        et = res[\\\"ent_test\\\"]\\n        sig = \\\"***\\\" if et['p_value'] < 0.001 else \\\"**\\\" if et['p_value'] < 0.01 else \\\"*\\\" if et['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"{name:<22} {100*et['delta_point']:+.2f}        [{100*et['ci_lower']:+.2f}, {100*et['ci_upper']:+.2f}]    {et['p_value']:.4f}     {sig}\\\")\\n\\n    # Save JSON\\n    output = {\\n        \\\"settings\\\": {k: {\\n            \\\"n_samples\\\": v[\\\"n_samples\\\"],\\n            \\\"rel_f1\\\": v[\\\"rel_test\\\"],\\n            \\\"ent_f1\\\": v[\\\"ent_test\\\"],\\n        } for k, v in all_results.items()},\\n        \\\"metadata\\\": {\\n            \\\"n_bootstrap\\\": 10000,\\n            \\\"ci_method\\\": \\\"percentile\\\",\\n            \\\"ci_level\\\": 0.95,\\n            \\\"seed\\\": 42,\\n            \\\"test_type\\\": \\\"paired_bootstrap\\\",\\n            \\\"comparison\\\": \\\"constrained - unconstrained\\\",\\n        }\\n    }\\n    with open(\\\"outputs/bootstrap_ci_ft_composability.json\\\", \\\"w\\\") as f:\\n        json.dump(output, f, indent=2)\\n    print(f\\\"\\\\nJSON saved to outputs/bootstrap_ci_ft_composability.json\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "61602727-cea9-4ceb-b057-12c4e47863ce",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"def _f1_from_arrays(tp, gold, pred):\\\\n    p = np.where(pred > 0, tp / pred, 0.0)\\\\n    r = np.where(gold > 0, tp / gold, 0.0)\\\\n    return np.where((p + r) > 0, 2 * p * r / (p + r), 0.0)\\\\n\\\\ndef bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\\\n    rng = np.random.RandomState(seed)\\\\n    n = len(sample_stats)\\\\n    tps = np.array([s[\\\\\\\"tp\\\\\\\"] for s in sample_stats])\\\\n    golds = np.array([s[\\\\\\\"gold\\\\\\\"] for s in sample_stats])\\\\n    preds = np.array([s[\\\\\\\"pred\\\\\\\"] for s in sample_stats])\\\\n\\\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\\\n    tp_sums = tps[indices].sum(axis=1).astype(float)\\\\n    gold_sums = golds[indices].sum(axis=1).astype(float)\\\\n    pred_sums = preds[indices].sum(axis=1).astype(float)\\\\n\\\\n    f1_samples = _f1_from_arrays(tp_sums, gold_sums, pred_sums)\\\\n\\\\n    point_p = tps.sum() / preds.sum() if preds.sum() > 0 else 0.0\\\\n    point_r = tps.sum() / golds.sum() if golds.sum() > 0 else 0.0\\\\n    point_f1 = 2 * point_p * point_r / (point_p + point_r) if (point_p + point_r) > 0 else 0.0\\\\n\\\\n    return {\\\\n        \\\\\\\"point_estimate\\\\\\\": float(point_f1),\\\\n        \\\\\\\"bootstrap_mean\\\\\\\": float(np.mean(f1_samples)),\\\\n        \\\\\\\"ci_lower\\\\\\\": float(np.percentile(f1_samples, 2.5)),\\\\n        \\\\\\\"ci_upper\\\\\\\": float(np.percentile(f1_samples, 97.5)),\\\\n        \\\\\\\"std\\\\\\\": float(np.std(f1_samples)),\\\\n    }\\\\n\\\\ndef paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\\\n    rng = np.random.RandomState(seed)\\\\n    n = len(stats_a)\\\\n    assert n == len(stats_b), f\\\\\\\"Mismatched lengths: {n} vs {len(stats_b)}\\\\\\\"\\\\n\\\\n    tps_a = np.array([s[\\\\\\\"tp\\\\\\\"] for s in stats_a])\\\\n    golds_a = np.array([s[\\\\\\\"gold\\\\\\\"] for s in stats_a])\\\\n    preds_a = np.array([s[\\\\\\\"pred\\\\\\\"] for s in stats_a])\\\\n    tps_b = np.array([s[\\\\\\\"tp\\\\\\\"] for s in stats_b])\\\\n    golds_b = np.array([s[\\\\\\\"gold\\\\\\\"] for s in stats_b])\\\\n    preds_b = np.array([s[\\\\\\\"pred\\\\\\\"] for s in stats_b])\\\\n\\\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\\\n\\\\n    f1_a = _f1_from_arrays(tps_a[indices].sum(axis=1).astype(float),\\\\n                           golds_a[indices].sum(axis=1).astype(float),\\\\n                           preds_a[indices].sum(axis=1).astype(float))\\\\n    f1_b = _f1_from_arrays(tps_b[indices].sum(axis=1).astype(float),\\\\n                           golds_b[indices].sum(axis=1).astype(float),\\\\n                           preds_b[indices].sum(axis=1).astype(float))\\\\n\\\\n    delta = f1_b - f1_a\\\\n    p_value = float(min(2 * min(np.mean(delta <= 0), np.mean(delta >= 0)), 1.0))\\\\n\\\\n    pa_p = tps_a.sum() / preds_a.sum() if preds_a.sum() > 0 else 0.0\\\\n    pa_r = tps_a.sum() / golds_a.sum() if golds_a.sum() > 0 else 0.0\\\\n    f1_a_point = 2 * pa_p * pa_r / (pa_p + pa_r) if (pa_p + pa_r) > 0 else 0.0\\\\n    pb_p = tps_b.sum() / preds_b.sum() if preds_b.sum() > 0 else 0.0\\\\n    pb_r = tps_b.sum() / golds_b.sum() if golds_b.sum() > 0 else 0.0\\\\n    f1_b_point = 2 * pb_p * pb_r / (pb_p + pb_r) if (pb_p + pb_r) > 0 else 0.0\\\\n\\\\n    return {\\\\n        \\\\\\\"f1_a\\\\\\\": float(f1_a_point),\\\\n        \\\\\\\"f1_b\\\\\\\": float(f1_b_point),\\\\n        \\\\\\\"delta_point\\\\\\\": float(f1_b_point - f1_a_point),\\\\n        \\\\\\\"delta_mean\\\\\\\": float(np.mean(delta)),\\\\n        \\\\\\\"ci_lower\\\\\\\": float(np.percentile(delta, 2.5)),\\\\n        \\\\\\\"ci_upper\\\\\\\": float(np.percentile(delta, 97.5)),\\\\n        \\\\\\\"p_value\\\\\\\": p_value,\\\\n    }\\\\n\\\\n# --- Main ---\\\\n\\\\ndef load_jsonl(path):\\\\n    records = []\\\\n    with open(path) as f:\\\\n        for line in f:\\\\n            line = line.strip()\\\\n            if line:\\\\n                records.append(json.loads(line))\\\\n    return records\\\\n\\\\ndef extract_stats(sample_stats, metric):\\\\n    prefix = \\\\\\\"ent\\\\\\\" if metric == \\\\\\\"entity\\\\\\\" else \\\\\\\"rel\\\\\\\"\\\\n    return [{\\\\\\\"tp\\\\\\\": s[f\\\\\\\"{prefix}_tp\\\\\\\"], \\\\\\\"gold\\\\\\\": s[f\\\\\\\"{prefix}_gold\\\\\\\"], \\\\\\\"pred\\\\\\\": s[f\\\\\\\"{prefix}_pred\\\\\\\"]} for s in sample_stats]\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    import os\\\\n    os.chdir(\\\\\\\"/root/schema_semantic_constrained_ie\\\\\\\")\\\\n\\\\n    # Load ontologies\\\\n    with open(\\\\\\\"ontology_constraints.json\\\\\\\") as f:\\\\n        scierc_constraints = json.load(f)\\\\n    scierc_valid_types = scierc_constraints[\\\\\\\"entity_types\\\\\\\"]\\\\n\\\\n    with open(\\\\\\\"data/docred/ontology_constraints_docred.json\\\\\\\") as f:\\\\n        docred_constraints = json.load(f)\\\\n    docred_rel_types = docred_constraints.get(\\\\\\\"rel\\\\n\\\\n... [截断: 输出过长，省略 1831 字符] ...\\\\n\\\\nids, f\\\\\\\"Doc ID mismatch in {setting_name}!\\\\\\\"\\\\n\\\\n        # Compute per-sample stats\\\\n        if cfg[\\\\\\\"dataset\\\\\\\"] == \\\\\\\"scierc\\\\\\\":\\\\n            unc_stats = [scierc_sample_stats(r, scierc_valid_types) for r in unc_records]\\\\n            con_stats = [scierc_sample_stats(r, scierc_valid_types) for r in con_records]\\\\n        else:\\\\n            unc_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in unc_records]\\\\n            con_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in con_records]\\\\n\\\\n        # Bootstrap CI for each config\\\\n        for label, stats in [(\\\\\\\"unconstrained\\\\\\\", unc_stats), (\\\\\\\"constrained\\\\\\\", con_stats)]:\\\\n            ent_ci = bootstrap_f1(extract_stats(stats, \\\\\\\"entity\\\\\\\"))\\\\n            rel_ci = bootstrap_f1(extract_stats(stats, \\\\\\\"relation\\\\\\\"))\\\\n            print(f\\\\\\\"  {label}: E-F1={100*ent_ci['point_estimate']:.2f}% [{100*ent_ci['ci_lower']:.2f}, {100*ent_ci['ci_upper']:.2f}], \\\\\\\"\\\\n                  f\\\\\\\"R-F1={100*rel_ci['point_estimate']:.2f}% [{100*rel_ci['ci_lower']:.2f}, {100*rel_ci['ci_upper']:.2f}]\\\\\\\")\\\\n\\\\n        # Paired test: constrained - unconstrained\\\\n        ent_test = paired_bootstrap_test(\\\\n            extract_stats(unc_stats, \\\\\\\"entity\\\\\\\"),\\\\n            extract_stats(con_stats, \\\\\\\"entity\\\\\\\"))\\\\n        rel_test = paired_bootstrap_test(\\\\n            extract_stats(unc_stats, \\\\\\\"relation\\\\\\\"),\\\\n            extract_stats(con_stats, \\\\\\\"relation\\\\\\\"))\\\\n\\\\n        print(f\\\\\\\"\\\\\\\\n  Paired test (constrained - unconstrained):\\\\\\\")\\\\n        print(f\\\\\\\"    ΔE-F1 = {100*ent_test['delta_point']:+.2f}pp  95%CI [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}]  p={ent_test['p_value']:.4f}\\\\\\\")\\\\n        print(f\\\\\\\"    ΔR-F1 = {100*rel_test['delta_point']:+.2f}pp  95%CI [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}]  p={rel_test['p_value']:.4f}\\\\\\\")\\\\n\\\\n        sig_rel = \\\\\\\"***\\\\\\\" if rel_test['p_value'] < 0.001 else \\\\\\\"**\\\\\\\" if rel_test['p_value'] < 0.01 else \\\\\\\"*\\\\\\\" if rel_test['p_value'] < 0.05 else \\\\\\\"n.s.\\\\\\\"\\\\n        sig_ent = \\\\\\\"***\\\\\\\" if ent_test['p_value'] < 0.001 else \\\\\\\"**\\\\\\\" if ent_test['p_value'] < 0.01 else \\\\\\\"*\\\\\\\" if ent_test['p_value'] < 0.05 else \\\\\\\"n.s.\\\\\\\"\\\\n        print(f\\\\\\\"    Significance: E-F1 {sig_ent}, R-F1 {sig_rel}\\\\\\\")\\\\n\\\\n        all_results[setting_name] = {\\\\n            \\\\\\\"n_samples\\\\\\\": len(unc_records),\\\\n            \\\\\\\"ent_test\\\\\\\": ent_test,\\\\n            \\\\\\\"rel_test\\\\\\\": rel_test,\\\\n        }\\\\n\\\\n    # Summary table\\\\n    print(f\\\\\\\"\\\\\\\\n\\\\\\\\n{'='*70}\\\\\\\")\\\\n    print(\\\\\\\"  SUMMARY TABLE\\\\\\\")\\\\n    print(f\\\\\\\"{'='*70}\\\\\\\")\\\\n    print(f\\\\\\\"{'Setting':<22} {'ΔR-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\\\\\")\\\\n    print(f\\\\\\\"{'─'*70}\\\\\\\")\\\\n    for name, res in all_results.items():\\\\n        rt = res[\\\\\\\"rel_test\\\\\\\"]\\\\n        sig = \\\\\\\"***\\\\\\\" if rt['p_value'] < 0.001 else \\\\\\\"**\\\\\\\" if rt['p_value'] < 0.01 else \\\\\\\"*\\\\\\\" if rt['p_value'] < 0.05 else \\\\\\\"n.s.\\\\\\\"\\\\n        print(f\\\\\\\"{name:<22} {100*rt['delta_point']:+.2f}        [{100*rt['ci_lower']:+.2f}, {100*rt['ci_upper']:+.2f}]    {rt['p_value']:.4f}     {sig}\\\\\\\")\\\\n\\\\n    print(f\\\\\\\"\\\\\\\\n{'Setting':<22} {'ΔE-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\\\\\")\\\\n    print(f\\\\\\\"{'─'*70}\\\\\\\")\\\\n    for name, res in all_results.items():\\\\n        et = res[\\\\\\\"ent_test\\\\\\\"]\\\\n        sig = \\\\\\\"***\\\\\\\" if et['p_value'] < 0.001 else \\\\\\\"**\\\\\\\" if et['p_value'] < 0.01 else \\\\\\\"*\\\\\\\" if et['p_value'] < 0.05 else \\\\\\\"n.s.\\\\\\\"\\\\n        print(f\\\\\\\"{name:<22} {100*et['delta_point']:+.2f}        [{100*et['ci_lower']:+.2f}, {100*et['ci_upper']:+.2f}]    {et['p_value']:.4f}     {sig}\\\\\\\")\\\\n\\\\n    # Save JSON\\\\n    output = {\\\\n        \\\\\\\"settings\\\\\\\": {k: {\\\\n            \\\\\\\"n_samples\\\\\\\": v[\\\\\\\"n_samples\\\\\\\"],\\\\n            \\\\\\\"rel_f1\\\\\\\": v[\\\\\\\"rel_test\\\\\\\"],\\\\n            \\\\\\\"ent_f1\\\\\\\": v[\\\\\\\"ent_test\\\\\\\"],\\\\n        } for k, v in all_results.items()},\\\\n        \\\\\\\"metadata\\\\\\\": {\\\\n            \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n            \\\\\\\"ci_method\\\\\\\": \\\\\\\"percentile\\\\\\\",\\\\n            \\\\\\\"ci_level\\\\\\\": 0.95,\\\\n            \\\\\\\"seed\\\\\\\": 42,\\\\n            \\\\\\\"test_type\\\\\\\": \\\\\\\"paired_bootstrap\\\\\\\",\\\\n            \\\\\\\"comparison\\\\\\\": \\\\\\\"constrained - unconstrained\\\\\\\",\\\\n        }\\\\n    }\\\\n    with open(\\\\\\\"outputs/bootstrap_ci_ft_composability.json\\\\\\\", \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(output, f, indent=2)\\\\n    print(f\\\\\\\"\\\\\\\\nJSON saved to outputs/bootstrap_ci_ft_composability.json\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"def _f1_from_arrays(tp, gold, pred):\\n    p = np.where(pred > 0, tp / pred, 0.0)\\n    r = np.where(gold > 0, tp / gold, 0.0)\\n    return np.where((p + r) > 0, 2 * p * r / (p + r), 0.0)\\n\\ndef bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    n = len(sample_stats)\\n    tps = np.array([s[\\\"tp\\\"] for s in sample_stats])\\n    golds = np.array([s[\\\"gold\\\"] for s in sample_stats])\\n    preds = np.array([s[\\\"pred\\\"] for s in sample_stats])\\n\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\n    tp_sums = tps[indices].sum(axis=1).astype(float)\\n    gold_sums = golds[indices].sum(axis=1).astype(float)\\n    pred_sums = preds[indices].sum(axis=1).astype(float)\\n\\n    f1_samples = _f1_from_arrays(tp_sums, gold_sums, pred_sums)\\n\\n    point_p = tps.sum() / preds.sum() if preds.sum() > 0 else 0.0\\n    point_r = tps.sum() / golds.sum() if golds.sum() > 0 else 0.0\\n    point_f1 = 2 * point_p * point_r / (point_p + point_r) if (point_p + point_r) > 0 else 0.0\\n\\n    return {\\n        \\\"point_estimate\\\": float(point_f1),\\n        \\\"bootstrap_mean\\\": float(np.mean(f1_samples)),\\n        \\\"ci_lower\\\": float(np.percentile(f1_samples, 2.5)),\\n        \\\"ci_upper\\\": float(np.percentile(f1_samples, 97.5)),\\n        \\\"std\\\": float(np.std(f1_samples)),\\n    }\\n\\ndef paired_bootstrap_test(stats_a, stats_b, n_bootstrap=10000, seed=42):\\n    rng = np.random.RandomState(seed)\\n    n = len(stats_a)\\n    assert n == len(stats_b), f\\\"Mismatched lengths: {n} vs {len(stats_b)}\\\"\\n\\n    tps_a = np.array([s[\\\"tp\\\"] for s in stats_a])\\n    golds_a = np.array([s[\\\"gold\\\"] for s in stats_a])\\n    preds_a = np.array([s[\\\"pred\\\"] for s in stats_a])\\n    tps_b = np.array([s[\\\"tp\\\"] for s in stats_b])\\n    golds_b = np.array([s[\\\"gold\\\"] for s in stats_b])\\n    preds_b = np.array([s[\\\"pred\\\"] for s in stats_b])\\n\\n    indices = rng.randint(0, n, size=(n_bootstrap, n))\\n\\n    f1_a = _f1_from_arrays(tps_a[indices].sum(axis=1).astype(float),\\n                           golds_a[indices].sum(axis=1).astype(float),\\n                           preds_a[indices].sum(axis=1).astype(float))\\n    f1_b = _f1_from_arrays(tps_b[indices].sum(axis=1).astype(float),\\n                           golds_b[indices].sum(axis=1).astype(float),\\n                           preds_b[indices].sum(axis=1).astype(float))\\n\\n    delta = f1_b - f1_a\\n    p_value = float(min(2 * min(np.mean(delta <= 0), np.mean(delta >= 0)), 1.0))\\n\\n    pa_p = tps_a.sum() / preds_a.sum() if preds_a.sum() > 0 else 0.0\\n    pa_r = tps_a.sum() / golds_a.sum() if golds_a.sum() > 0 else 0.0\\n    f1_a_point = 2 * pa_p * pa_r / (pa_p + pa_r) if (pa_p + pa_r) > 0 else 0.0\\n    pb_p = tps_b.sum() / preds_b.sum() if preds_b.sum() > 0 else 0.0\\n    pb_r = tps_b.sum() / golds_b.sum() if golds_b.sum() > 0 else 0.0\\n    f1_b_point = 2 * pb_p * pb_r / (pb_p + pb_r) if (pb_p + pb_r) > 0 else 0.0\\n\\n    return {\\n        \\\"f1_a\\\": float(f1_a_point),\\n        \\\"f1_b\\\": float(f1_b_point),\\n        \\\"delta_point\\\": float(f1_b_point - f1_a_point),\\n        \\\"delta_mean\\\": float(np.mean(delta)),\\n        \\\"ci_lower\\\": float(np.percentile(delta, 2.5)),\\n        \\\"ci_upper\\\": float(np.percentile(delta, 97.5)),\\n        \\\"p_value\\\": p_value,\\n    }\\n\\n# --- Main ---\\n\\ndef load_jsonl(path):\\n    records = []\\n    with open(path) as f:\\n        for line in f:\\n            line = line.strip()\\n            if line:\\n                records.append(json.loads(line))\\n    return records\\n\\ndef extract_stats(sample_stats, metric):\\n    prefix = \\\"ent\\\" if metric == \\\"entity\\\" else \\\"rel\\\"\\n    return [{\\\"tp\\\": s[f\\\"{prefix}_tp\\\"], \\\"gold\\\": s[f\\\"{prefix}_gold\\\"], \\\"pred\\\": s[f\\\"{prefix}_pred\\\"]} for s in sample_stats]\\n\\nif __name__ == \\\"__main__\\\":\\n    import os\\n    os.chdir(\\\"/root/schema_semantic_constrained_ie\\\")\\n\\n    # Load ontologies\\n    with open(\\\"ontology_constraints.json\\\") as f:\\n        scierc_constraints = json.load(f)\\n    scierc_valid_types = scierc_constraints[\\\"entity_types\\\"]\\n\\n    with open(\\\"data/docred/ontology_constraints_docred.json\\\") as f:\\n        docred_constraints = json.load(f)\\n    docred_rel_types = docred_constraints.get(\\\"rel\\n\\n... [截断: 输出过长，省略 1831 字符] ...\\n\\nids, f\\\"Doc ID mismatch in {setting_name}!\\\"\\n\\n        # Compute per-sample stats\\n        if cfg[\\\"dataset\\\"] == \\\"scierc\\\":\\n            unc_stats = [scierc_sample_stats(r, scierc_valid_types) for r in unc_records]\\n            con_stats = [scierc_sample_stats(r, scierc_valid_types) for r in con_records]\\n        else:\\n            unc_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in unc_records]\\n            con_stats = [docred_sample_stats(r, docred_rel_types, docred_name_to_id) for r in con_records]\\n\\n        # Bootstrap CI for each config\\n        for label, stats in [(\\\"unconstrained\\\", unc_stats), (\\\"constrained\\\", con_stats)]:\\n            ent_ci = bootstrap_f1(extract_stats(stats, \\\"entity\\\"))\\n            rel_ci = bootstrap_f1(extract_stats(stats, \\\"relation\\\"))\\n            print(f\\\"  {label}: E-F1={100*ent_ci['point_estimate']:.2f}% [{100*ent_ci['ci_lower']:.2f}, {100*ent_ci['ci_upper']:.2f}], \\\"\\n                  f\\\"R-F1={100*rel_ci['point_estimate']:.2f}% [{100*rel_ci['ci_lower']:.2f}, {100*rel_ci['ci_upper']:.2f}]\\\")\\n\\n        # Paired test: constrained - unconstrained\\n        ent_test = paired_bootstrap_test(\\n            extract_stats(unc_stats, \\\"entity\\\"),\\n            extract_stats(con_stats, \\\"entity\\\"))\\n        rel_test = paired_bootstrap_test(\\n            extract_stats(unc_stats, \\\"relation\\\"),\\n            extract_stats(con_stats, \\\"relation\\\"))\\n\\n        print(f\\\"\\\\n  Paired test (constrained - unconstrained):\\\")\\n        print(f\\\"    ΔE-F1 = {100*ent_test['delta_point']:+.2f}pp  95%CI [{100*ent_test['ci_lower']:+.2f}, {100*ent_test['ci_upper']:+.2f}]  p={ent_test['p_value']:.4f}\\\")\\n        print(f\\\"    ΔR-F1 = {100*rel_test['delta_point']:+.2f}pp  95%CI [{100*rel_test['ci_lower']:+.2f}, {100*rel_test['ci_upper']:+.2f}]  p={rel_test['p_value']:.4f}\\\")\\n\\n        sig_rel = \\\"***\\\" if rel_test['p_value'] < 0.001 else \\\"**\\\" if rel_test['p_value'] < 0.01 else \\\"*\\\" if rel_test['p_value'] < 0.05 else \\\"n.s.\\\"\\n        sig_ent = \\\"***\\\" if ent_test['p_value'] < 0.001 else \\\"**\\\" if ent_test['p_value'] < 0.01 else \\\"*\\\" if ent_test['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"    Significance: E-F1 {sig_ent}, R-F1 {sig_rel}\\\")\\n\\n        all_results[setting_name] = {\\n            \\\"n_samples\\\": len(unc_records),\\n            \\\"ent_test\\\": ent_test,\\n            \\\"rel_test\\\": rel_test,\\n        }\\n\\n    # Summary table\\n    print(f\\\"\\\\n\\\\n{'='*70}\\\")\\n    print(\\\"  SUMMARY TABLE\\\")\\n    print(f\\\"{'='*70}\\\")\\n    print(f\\\"{'Setting':<22} {'ΔR-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\")\\n    print(f\\\"{'─'*70}\\\")\\n    for name, res in all_results.items():\\n        rt = res[\\\"rel_test\\\"]\\n        sig = \\\"***\\\" if rt['p_value'] < 0.001 else \\\"**\\\" if rt['p_value'] < 0.01 else \\\"*\\\" if rt['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"{name:<22} {100*rt['delta_point']:+.2f}        [{100*rt['ci_lower']:+.2f}, {100*rt['ci_upper']:+.2f}]    {rt['p_value']:.4f}     {sig}\\\")\\n\\n    print(f\\\"\\\\n{'Setting':<22} {'ΔE-F1 (pp)':<12} {'95% CI':<22} {'p-value':<10} {'Sig':<5}\\\")\\n    print(f\\\"{'─'*70}\\\")\\n    for name, res in all_results.items():\\n        et = res[\\\"ent_test\\\"]\\n        sig = \\\"***\\\" if et['p_value'] < 0.001 else \\\"**\\\" if et['p_value'] < 0.01 else \\\"*\\\" if et['p_value'] < 0.05 else \\\"n.s.\\\"\\n        print(f\\\"{name:<22} {100*et['delta_point']:+.2f}        [{100*et['ci_lower']:+.2f}, {100*et['ci_upper']:+.2f}]    {et['p_value']:.4f}     {sig}\\\")\\n\\n    # Save JSON\\n    output = {\\n        \\\"settings\\\": {k: {\\n            \\\"n_samples\\\": v[\\\"n_samples\\\"],\\n            \\\"rel_f1\\\": v[\\\"rel_test\\\"],\\n            \\\"ent_f1\\\": v[\\\"ent_test\\\"],\\n        } for k, v in all_results.items()},\\n        \\\"metadata\\\": {\\n            \\\"n_bootstrap\\\": 10000,\\n            \\\"ci_method\\\": \\\"percentile\\\",\\n            \\\"ci_level\\\": 0.95,\\n            \\\"seed\\\": 42,\\n            \\\"test_type\\\": \\\"paired_bootstrap\\\",\\n            \\\"comparison\\\": \\\"constrained - unconstrained\\\",\\n        }\\n    }\\n    with open(\\\"outputs/bootstrap_ci_ft_composability.json\\\", \\\"w\\\") as f:\\n        json.dump(output, f, indent=2)\\n    print(f\\\"\\\\nJSON saved to outputs/bootstrap_ci_ft_composability.json\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

````text
Now I have the complete picture. Let me analyze all three bootstrap scripts:

## Analysis

### `bootstrap_f1` function (identical in all scripts):
```python
def bootstrap_f1(sample_stats, n_bootstrap=10000, seed=42):
    tps = np.array([s["tp"] for s in sample_stats])
    golds = np.array([s["gold"] for s in sample_stats])


```

Extracting bootstrap samples...

So this is computing corpus-level micro-F1 by resampling documents with replacement, then aggregating the TP, gold, and predicted counts across all resampled documents before calculating F1. That's different from macro-F1, which would compute F1 per document first and then average them. The `paired_bootstrap_test` function uses the same approach to compare two systems.

I've now confirmed that all three bootstrap scripts—the one for zero-shot GPT-4o, fine-tuned LoRA, and zero-shot Llama—are already computing corpus micro-F1 correctly. They all follow the same pattern of summing counts globally before computing F1, so no changes are needed there. Now I should check the existing bootstrap results to make sure they align with the main results table.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "72eca971-465d-4843-adc3-4b0ccdda5c0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018a1DqpzB4ScVCF8nHES3B6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4114,
      "cache_read_input_tokens": 45592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4114
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

_source line 44_

All three scripts are confirmed to use **corpus micro-F1**. The `bootstrap_f1` and `paired_bootstrap_test` functions all:
1. Collect per-sample TP/gold/pred counts
2. Bootstrap resample documents
3. **Sum** TP/gold/pred across resampled documents (`.sum(axis=1)`)
4. Compute F1 from global sums → micro-F1

No document-level macro-F1 is used anywhere. Let me verify the existing results are consistent by checking the output files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "ccf7c453-d47a-4c64-b788-eb8334cd5768",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018a1DqpzB4ScVCF8nHES3B6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4114,
      "cache_read_input_tokens": 45592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4114
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

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KwZgAYY4eVqSDg8e3JshxM`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/outputs/bootstrap_ci_ft_composability.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "1e6d9545-f6a9-4155-baf5-3f4997839233",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018a1DqpzB4ScVCF8nHES3B6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4114,
      "cache_read_input_tokens": 45592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4114
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

_source line 46 · 2026-05-17T14:12:59.435Z_

<details><summary>↩ Tool result · `toolu_01KwZgAYY4eVqSDg8e3JshxM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"settings\\\": {\\n    \\\"Qwen-LoRA-SciERC\\\": {\\n      \\\"n_samples\\\": 551,\\n      \\\"rel_f1\\\": {\\n        \\\"f1_a\\\": 0.4386298763082778,\\n        \\\"f1_b\\\": 0.43767840152235965,\\n        \\\"delta_point\\\": -0.0009514747859181716,\\n        \\\"delta_mean\\\": -0.0009561921675813286,\\n        \\\"ci_lower\\\": -0.002967359050445098,\\n        \\\"ci_upper\\\": 0.0,\\n        \\\"p_value\\\": 0.726\\n      },\\n      \\\"ent_f1\\\": {\\n        \\\"f1_a\\\": 0.6705403834979663,\\n        \\\"f1_b\\\": 0.6705403834979663,\\n        \\\"delta_point\\\": 0.0,\\n        \\\"delta_mean\\\": 0.0,\\n        \\\"ci_lower\\\": 0.0,\\n        \\\"ci_upper\\\": 0.0,\\n        \\\"p_value\\\": 1.0\\n      }\\n    },\\n    \\\"Qwen-LoRA-DocRED\\\": {\\n      \\\"n_samples\\\": 998,\\n      \\\"rel_f1\\\": {\\n        \\\"f1_a\\\": 0.40967427063374423,\\n        \\\"f1_b\\\": 0.4059783992145169,\\n        \\\"delta_point\\\": -0.0036958714192273368,\\n        \\\"delta_mean\\\": -0.0037055378165787153,\\n        \\\"ci_lower\\\": -0.007592290105293843,\\n        \\\"ci_upper\\\": -0.0005354787439645679,\\n        \\\"p_value\\\": 0.014\\n      },\\n      \\\"ent_f1\\\": {\\n        \\\"f1_a\\\": 0.8222435487310727,\\n        \\\"f1_b\\\": 0.8149601010236707,\\n        \\\"delta_point\\\": -0.00728344770740208,\\n        \\\"delta_mean\\\": -0.007301595654623452,\\n        \\\"ci_lower\\\": -0.012111950558267803,\\n        \\\"ci_upper\\\": -0.003041898819680814,\\n        \\\"p_value\\\": 0.0004\\n      }\\n    },\\n    \\\"Llama-LoRA-SciERC\\\": {\\n      \\\"n_samples\\\": 551,\\n      \\\"rel_f1\\\": {\\n        \\\"f1_a\\\": 0.4545012165450121,\\n        \\\"f1_b\\\": 0.45472249269717624,\\n        \\\"delta_point\\\": 0.00022127615216416263,\\n        \\\"delta_mean\\\": 0.00022208035589220865,\\n        \\\"ci_lower\\\": 0.0,\\n        \\\"ci_upper\\\": 0.000705289319757152,\\n        \\\"p_value\\\": 0.7364\\n      },\\n      \\\"ent_f1\\\": {\\n        \\\"f1_a\\\": 0.6776084407971864,\\n        \\\"f1_b\\\": 0.6776084407971864,\\n        \\\"delta_point\\\": 0.0,\\n        \\\"delta_mean\\\": 0.0,\\n        \\\"ci_lower\\\": 0.0,\\n        \\\"ci_upper\\\": 0.0,\\n        \\\"p_value\\\": 1.0\\n      }\\n    },\\n    \\\"Llama-LoRA-DocRED\\\": {\\n      \\\"n_samples\\\": 998,\\n      \\\"rel_f1\\\": {\\n        \\\"f1_a\\\": 0.43806668094524165,\\n        \\\"f1_b\\\": 0.4382884174311926,\\n        \\\"delta_point\\\": 0.00022173648595097406,\\n        \\\"delta_mean\\\": 0.00021390097127442823,\\n        \\\"ci_lower\\\": -0.0014921138208722497,\\n        \\\"ci_upper\\\": 0.002155864233342271,\\n        \\\"p_value\\\": 0.8506\\n      },\\n      \\\"ent_f1\\\": {\\n        \\\"f1_a\\\": 0.840090382567592,\\n        \\\"f1_b\\\": 0.8400998076623174,\\n        \\\"delta_point\\\": 9.425094725346028e-06,\\n        \\\"delta_mean\\\": 2.7109307882730494e-05,\\n        \\\"ci_lower\\\": -0.0015434694575261615,\\n        \\\"ci_upper\\\": 0.0017849557158172837,\\n        \\\"p_value\\\": 0.9844\\n      }\\n    }\\n  },\\n  \\\"metadata\\\": {\\n    \\\"n_bootstrap\\\": 10000,\\n    \\\"ci_method\\\": \\\"percentile\\\",\\n    \\\"ci_level\\\": 0.95,\\n    \\\"seed\\\": 42,\\n    \\\"test_type\\\": \\\"paired_bootstrap\\\",\\n    \\\"comparison\\\": \\\"constrained - unconstrained\\\"\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "cf3bc02e-4b80-44ec-b443-eaf26928332c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"settings\\\\\\\": {\\\\n    \\\\\\\"Qwen-LoRA-SciERC\\\\\\\": {\\\\n      \\\\\\\"n_samples\\\\\\\": 551,\\\\n      \\\\\\\"rel_f1\\\\\\\": {\\\\n        \\\\\\\"f1_a\\\\\\\": 0.4386298763082778,\\\\n        \\\\\\\"f1_b\\\\\\\": 0.43767840152235965,\\\\n        \\\\\\\"delta_point\\\\\\\": -0.0009514747859181716,\\\\n        \\\\\\\"delta_mean\\\\\\\": -0.0009561921675813286,\\\\n        \\\\\\\"ci_lower\\\\\\\": -0.002967359050445098,\\\\n        \\\\\\\"ci_upper\\\\\\\": 0.0,\\\\n        \\\\\\\"p_value\\\\\\\": 0.726\\\\n      },\\\\n      \\\\\\\"ent_f1\\\\\\\": {\\\\n        \\\\\\\"f1_a\\\\\\\": 0.6705403834979663,\\\\n        \\\\\\\"f1_b\\\\\\\": 0.6705403834979663,\\\\n        \\\\\\\"delta_point\\\\\\\": 0.0,\\\\n        \\\\\\\"delta_mean\\\\\\\": 0.0,\\\\n        \\\\\\\"ci_lower\\\\\\\": 0.0,\\\\n        \\\\\\\"ci_upper\\\\\\\": 0.0,\\\\n        \\\\\\\"p_value\\\\\\\": 1.0\\\\n      }\\\\n    },\\\\n    \\\\\\\"Qwen-LoRA-DocRED\\\\\\\": {\\\\n      \\\\\\\"n_samples\\\\\\\": 998,\\\\n      \\\\\\\"rel_f1\\\\\\\": {\\\\n        \\\\\\\"f1_a\\\\\\\": 0.40967427063374423,\\\\n        \\\\\\\"f1_b\\\\\\\": 0.4059783992145169,\\\\n        \\\\\\\"delta_point\\\\\\\": -0.0036958714192273368,\\\\n        \\\\\\\"delta_mean\\\\\\\": -0.0037055378165787153,\\\\n        \\\\\\\"ci_lower\\\\\\\": -0.007592290105293843,\\\\n        \\\\\\\"ci_upper\\\\\\\": -0.0005354787439645679,\\\\n        \\\\\\\"p_value\\\\\\\": 0.014\\\\n      },\\\\n      \\\\\\\"ent_f1\\\\\\\": {\\\\n        \\\\\\\"f1_a\\\\\\\": 0.8222435487310727,\\\\n        \\\\\\\"f1_b\\\\\\\": 0.8149601010236707,\\\\n        \\\\\\\"delta_point\\\\\\\": -0.00728344770740208,\\\\n        \\\\\\\"delta_mean\\\\\\\": -0.007301595654623452,\\\\n        \\\\\\\"ci_lower\\\\\\\": -0.012111950558267803,\\\\n        \\\\\\\"ci_upper\\\\\\\": -0.003041898819680814,\\\\n        \\\\\\\"p_value\\\\\\\": 0.0004\\\\n      }\\\\n    },\\\\n    \\\\\\\"Llama-LoRA-SciERC\\\\\\\": {\\\\n      \\\\\\\"n_samples\\\\\\\": 551,\\\\n      \\\\\\\"rel_f1\\\\\\\": {\\\\n        \\\\\\\"f1_a\\\\\\\": 0.4545012165450121,\\\\n        \\\\\\\"f1_b\\\\\\\": 0.45472249269717624,\\\\n        \\\\\\\"delta_point\\\\\\\": 0.00022127615216416263,\\\\n        \\\\\\\"delta_mean\\\\\\\": 0.00022208035589220865,\\\\n        \\\\\\\"ci_lower\\\\\\\": 0.0,\\\\n        \\\\\\\"ci_upper\\\\\\\": 0.000705289319757152,\\\\n        \\\\\\\"p_value\\\\\\\": 0.7364\\\\n      },\\\\n      \\\\\\\"ent_f1\\\\\\\": {\\\\n        \\\\\\\"f1_a\\\\\\\": 0.6776084407971864,\\\\n        \\\\\\\"f1_b\\\\\\\": 0.6776084407971864,\\\\n        \\\\\\\"delta_point\\\\\\\": 0.0,\\\\n        \\\\\\\"delta_mean\\\\\\\": 0.0,\\\\n        \\\\\\\"ci_lower\\\\\\\": 0.0,\\\\n        \\\\\\\"ci_upper\\\\\\\": 0.0,\\\\n        \\\\\\\"p_value\\\\\\\": 1.0\\\\n      }\\\\n    },\\\\n    \\\\\\\"Llama-LoRA-DocRED\\\\\\\": {\\\\n      \\\\\\\"n_samples\\\\\\\": 998,\\\\n      \\\\\\\"rel_f1\\\\\\\": {\\\\n        \\\\\\\"f1_a\\\\\\\": 0.43806668094524165,\\\\n        \\\\\\\"f1_b\\\\\\\": 0.4382884174311926,\\\\n        \\\\\\\"delta_point\\\\\\\": 0.00022173648595097406,\\\\n        \\\\\\\"delta_mean\\\\\\\": 0.00021390097127442823,\\\\n        \\\\\\\"ci_lower\\\\\\\": -0.0014921138208722497,\\\\n        \\\\\\\"ci_upper\\\\\\\": 0.002155864233342271,\\\\n        \\\\\\\"p_value\\\\\\\": 0.8506\\\\n      },\\\\n      \\\\\\\"ent_f1\\\\\\\": {\\\\n        \\\\\\\"f1_a\\\\\\\": 0.840090382567592,\\\\n        \\\\\\\"f1_b\\\\\\\": 0.8400998076623174,\\\\n        \\\\\\\"delta_point\\\\\\\": 9.425094725346028e-06,\\\\n        \\\\\\\"delta_mean\\\\\\\": 2.7109307882730494e-05,\\\\n        \\\\\\\"ci_lower\\\\\\\": -0.0015434694575261615,\\\\n        \\\\\\\"ci_upper\\\\\\\": 0.0017849557158172837,\\\\n        \\\\\\\"p_value\\\\\\\": 0.9844\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\\\\"metadata\\\\\\\": {\\\\n    \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n    \\\\\\\"ci_method\\\\\\\": \\\\\\\"percentile\\\\\\\",\\\\n    \\\\\\\"ci_level\\\\\\\": 0.95,\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"test_type\\\\\\\": \\\\\\\"paired_bootstrap\\\\\\\",\\\\n    \\\\\\\"comparison\\\\\\\": \\\\\\\"constrained - unconstrained\\\\\\\"\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"settings\\\": {\\n    \\\"Qwen-LoRA-SciERC\\\": {\\n      \\\"n_samples\\\": 551,\\n      \\\"rel_f1\\\": {\\n        \\\"f1_a\\\": 0.4386298763082778,\\n        \\\"f1_b\\\": 0.43767840152235965,\\n        \\\"delta_point\\\": -0.0009514747859181716,\\n        \\\"delta_mean\\\": -0.0009561921675813286,\\n        \\\"ci_lower\\\": -0.002967359050445098,\\n        \\\"ci_upper\\\": 0.0,\\n        \\\"p_value\\\": 0.726\\n      },\\n      \\\"ent_f1\\\": {\\n        \\\"f1_a\\\": 0.6705403834979663,\\n        \\\"f1_b\\\": 0.6705403834979663,\\n        \\\"delta_point\\\": 0.0,\\n        \\\"delta_mean\\\": 0.0,\\n        \\\"ci_lower\\\": 0.0,\\n        \\\"ci_upper\\\": 0.0,\\n        \\\"p_value\\\": 1.0\\n      }\\n    },\\n    \\\"Qwen-LoRA-DocRED\\\": {\\n      \\\"n_samples\\\": 998,\\n      \\\"rel_f1\\\": {\\n        \\\"f1_a\\\": 0.40967427063374423,\\n        \\\"f1_b\\\": 0.4059783992145169,\\n        \\\"delta_point\\\": -0.0036958714192273368,\\n        \\\"delta_mean\\\": -0.0037055378165787153,\\n        \\\"ci_lower\\\": -0.007592290105293843,\\n        \\\"ci_upper\\\": -0.0005354787439645679,\\n        \\\"p_value\\\": 0.014\\n      },\\n      \\\"ent_f1\\\": {\\n        \\\"f1_a\\\": 0.8222435487310727,\\n        \\\"f1_b\\\": 0.8149601010236707,\\n        \\\"delta_point\\\": -0.00728344770740208,\\n        \\\"delta_mean\\\": -0.007301595654623452,\\n        \\\"ci_lower\\\": -0.012111950558267803,\\n        \\\"ci_upper\\\": -0.003041898819680814,\\n        \\\"p_value\\\": 0.0004\\n      }\\n    },\\n    \\\"Llama-LoRA-SciERC\\\": {\\n      \\\"n_samples\\\": 551,\\n      \\\"rel_f1\\\": {\\n        \\\"f1_a\\\": 0.4545012165450121,\\n        \\\"f1_b\\\": 0.45472249269717624,\\n        \\\"delta_point\\\": 0.00022127615216416263,\\n        \\\"delta_mean\\\": 0.00022208035589220865,\\n        \\\"ci_lower\\\": 0.0,\\n        \\\"ci_upper\\\": 0.000705289319757152,\\n        \\\"p_value\\\": 0.7364\\n      },\\n      \\\"ent_f1\\\": {\\n        \\\"f1_a\\\": 0.6776084407971864,\\n        \\\"f1_b\\\": 0.6776084407971864,\\n        \\\"delta_point\\\": 0.0,\\n        \\\"delta_mean\\\": 0.0,\\n        \\\"ci_lower\\\": 0.0,\\n        \\\"ci_upper\\\": 0.0,\\n        \\\"p_value\\\": 1.0\\n      }\\n    },\\n    \\\"Llama-LoRA-DocRED\\\": {\\n      \\\"n_samples\\\": 998,\\n      \\\"rel_f1\\\": {\\n        \\\"f1_a\\\": 0.43806668094524165,\\n        \\\"f1_b\\\": 0.4382884174311926,\\n        \\\"delta_point\\\": 0.00022173648595097406,\\n        \\\"delta_mean\\\": 0.00021390097127442823,\\n        \\\"ci_lower\\\": -0.0014921138208722497,\\n        \\\"ci_upper\\\": 0.002155864233342271,\\n        \\\"p_value\\\": 0.8506\\n      },\\n      \\\"ent_f1\\\": {\\n        \\\"f1_a\\\": 0.840090382567592,\\n        \\\"f1_b\\\": 0.8400998076623174,\\n        \\\"delta_point\\\": 9.425094725346028e-06,\\n        \\\"delta_mean\\\": 2.7109307882730494e-05,\\n        \\\"ci_lower\\\": -0.0015434694575261615,\\n        \\\"ci_upper\\\": 0.0017849557158172837,\\n        \\\"p_value\\\": 0.9844\\n      }\\n    }\\n  },\\n  \\\"metadata\\\": {\\n    \\\"n_bootstrap\\\": 10000,\\n    \\\"ci_method\\\": \\\"percentile\\\",\\n    \\\"ci_level\\\": 0.95,\\n    \\\"seed\\\": 42,\\n    \\\"test_type\\\": \\\"paired_bootstrap\\\",\\n    \\\"comparison\\\": \\\"constrained - unconstrained\\\"\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NBFYKdQGnv8PZczEoEaqiq`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results_v2.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "de61ab75-dbb0-43cb-a9b2-ec30b935a9a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018a1DqpzB4ScVCF8nHES3B6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4114,
      "cache_read_input_tokens": 45592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4114
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

_source line 48 · 2026-05-17T14:12:59.971Z_

<details><summary>↩ Tool result · `toolu_01NBFYKdQGnv8PZczEoEaqiq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"per_config\\\": {\\n      \\\"unconstrained\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.310111,\\n          \\\"bootstrap_mean\\\": 0.310169,\\n          \\\"ci_lower\\\": 0.288275,\\n          \\\"ci_upper\\\": 0.332452,\\n          \\\"std\\\": 0.011217\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.082283,\\n          \\\"bootstrap_mean\\\": 0.082357,\\n          \\\"ci_lower\\\": 0.064876,\\n          \\\"ci_upper\\\": 0.10089,\\n          \\\"std\\\": 0.009112\\n        }\\n      },\\n      \\\"grammar_only\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.309846,\\n          \\\"bootstrap_mean\\\": 0.309905,\\n          \\\"ci_lower\\\": 0.288045,\\n          \\\"ci_upper\\\": 0.332121,\\n          \\\"std\\\": 0.011184\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.082253,\\n          \\\"bootstrap_mean\\\": 0.082321,\\n          \\\"ci_lower\\\": 0.064896,\\n          \\\"ci_upper\\\": 0.10087,\\n          \\\"std\\\": 0.009103\\n        }\\n      },\\n      \\\"semantic_only\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.310111,\\n          \\\"bootstrap_mean\\\": 0.310169,\\n          \\\"ci_lower\\\": 0.288275,\\n          \\\"ci_upper\\\": 0.332452,\\n          \\\"std\\\": 0.011217\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.081481,\\n          \\\"bootstrap_mean\\\": 0.081547,\\n          \\\"ci_lower\\\": 0.064367,\\n          \\\"ci_upper\\\": 0.100038,\\n          \\\"std\\\": 0.009066\\n        }\\n      },\\n      \\\"full_s1\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.309846,\\n          \\\"bootstrap_mean\\\": 0.309905,\\n          \\\"ci_lower\\\": 0.288045,\\n          \\\"ci_upper\\\": 0.332121,\\n          \\\"std\\\": 0.011184\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.083611,\\n          \\\"bootstrap_mean\\\": 0.083708,\\n          \\\"ci_lower\\\": 0.065828,\\n          \\\"ci_upper\\\": 0.102677,\\n          \\\"std\\\": 0.009354\\n        }\\n      }\\n    },\\n    \\\"comparisons\\\": {\\n      \\\"unconstrained_vs_grammar_only\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000266,\\n          \\\"delta_mean\\\": -0.000264,\\n          \\\"ci_lower\\\": -0.001065,\\n          \\\"ci_upper\\\": 0.000823,\\n          \\\"p_value\\\": 0.5266\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": -3e-05,\\n          \\\"delta_mean\\\": -3.6e-05,\\n          \\\"ci_lower\\\": -0.002234,\\n          \\\"ci_upper\\\": 0.002185,\\n          \\\"p_value\\\": 0.9798\\n        }\\n      },\\n      \\\"unconstrained_vs_semantic_only\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.0,\\n          \\\"delta_mean\\\": 0.0,\\n          \\\"ci_lower\\\": 0.0,\\n          \\\"ci_upper\\\": 0.0,\\n          \\\"p_value\\\": 1.0\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000802,\\n          \\\"delta_mean\\\": -0.000811,\\n          \\\"ci_lower\\\": -0.003592,\\n          \\\"ci_upper\\\": 0.001478,\\n          \\\"p_value\\\": 0.4236\\n        }\\n      },\\n      \\\"unconstrained_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000266,\\n          \\\"delta_mean\\\": -0.000264,\\n          \\\"ci_lower\\\": -0.001065,\\n          \\\"ci_upper\\\": 0.000823,\\n          \\\"p_value\\\": 0.5266\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.001328,\\n          \\\"delta_mean\\\": 0.001351,\\n          \\\"ci_lower\\\": -0.00235,\\n          \\\"ci_upper\\\": 0.005828,\\n          \\\"p_value\\\": 0.5824\\n        }\\n      },\\n      \\\"grammar_only_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.0,\\n          \\\"delta_mean\\\": 0.0,\\n          \\\"ci_lower\\\": 0.0,\\n          \\\"ci_upper\\\": 0.0,\\n          \\\"p_value\\\": 1.0\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.001358,\\n          \\\"delta_mean\\\": 0.001387,\\n          \\\"ci_lower\\\": -0.0016,\\n          \\\"ci_upper\\\": 0.00536,\\n          \\\"p_value\\\": 0.5108\\n        }\\n      },\\n      \\\"semantic_only_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000266,\\n          \\\"delta_mean\\\": -0.000264,\\n          \\\"ci_lower\\\": -0.001065,\\n          \\\"ci_upper\\\": 0.000823,\\n          \\\"p_value\\\": 0.5266\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.002129,\\n          \\\"delta_mean\\\": 0.002162,\\n          \\\"ci_lower\\\": -0.002094,\\n          \\\"ci_upper\\\": 0.00727,\\n          \\\"p_value\\\": 0.393\\n        }\\n      }\\n    }\\n  },\\n  \\\"docred\\\": {\\n    \\\"per_config\\\": {\\n      \\\"unconstrained\\\":\\n\\n... [截断: 输出过长，省略 1809 字符] ...\\n\\n   \\\"delta_mean\\\": 0.01228,\\n          \\\"ci_lower\\\": 0.009322,\\n          \\\"ci_upper\\\": 0.015463,\\n          \\\"p_value\\\": 0.0\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.005718,\\n          \\\"delta_mean\\\": 0.005738,\\n          \\\"ci_lower\\\": 0.003157,\\n          \\\"ci_upper\\\": 0.008757,\\n          \\\"p_value\\\": 0.0\\n        }\\n      },\\n      \\\"unconstrained_vs_semantic_only\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 2.9e-05,\\n          \\\"delta_mean\\\": 2.9e-05,\\n          \\\"ci_lower\\\": 0.0,\\n          \\\"ci_upper\\\": 0.0001,\\n          \\\"p_value\\\": 0.7378\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": -7.9e-05,\\n          \\\"delta_mean\\\": -7.9e-05,\\n          \\\"ci_lower\\\": -0.001015,\\n          \\\"ci_upper\\\": 0.000873,\\n          \\\"p_value\\\": 0.8546\\n        }\\n      },\\n      \\\"unconstrained_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.012309,\\n          \\\"delta_mean\\\": 0.012317,\\n          \\\"ci_lower\\\": 0.009362,\\n          \\\"ci_upper\\\": 0.015503,\\n          \\\"p_value\\\": 0.0\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.004961,\\n          \\\"delta_mean\\\": 0.00498,\\n          \\\"ci_lower\\\": 0.002276,\\n          \\\"ci_upper\\\": 0.00812,\\n          \\\"p_value\\\": 0.0\\n        }\\n      },\\n      \\\"grammar_only_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 3.7e-05,\\n          \\\"delta_mean\\\": 3.7e-05,\\n          \\\"ci_lower\\\": -7.4e-05,\\n          \\\"ci_upper\\\": 0.000187,\\n          \\\"p_value\\\": 0.6556\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000757,\\n          \\\"delta_mean\\\": -0.000758,\\n          \\\"ci_lower\\\": -0.001706,\\n          \\\"ci_upper\\\": 0.000189,\\n          \\\"p_value\\\": 0.115\\n        }\\n      },\\n      \\\"semantic_only_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.01228,\\n          \\\"delta_mean\\\": 0.012288,\\n          \\\"ci_lower\\\": 0.009322,\\n          \\\"ci_upper\\\": 0.015469,\\n          \\\"p_value\\\": 0.0\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.00504,\\n          \\\"delta_mean\\\": 0.005058,\\n          \\\"ci_lower\\\": 0.002408,\\n          \\\"ci_upper\\\": 0.008147,\\n          \\\"p_value\\\": 0.0\\n        }\\n      }\\n    }\\n  },\\n  \\\"metadata\\\": {\\n    \\\"n_bootstrap\\\": 10000,\\n    \\\"ci_method\\\": \\\"percentile\\\",\\n    \\\"ci_level\\\": 0.95,\\n    \\\"seed\\\": 42,\\n    \\\"resample_unit\\\": \\\"sentence (SciERC) / document (DocRED)\\\",\\n    \\\"fix_applied\\\": \\\"Removed entity type filter (DOCRED_VALID_ENTITY_TYPES) and entity type normalization from docred_sample_stats pred_ent_set. Parse-failure documents now return all zeros (matching registry posthoc_filter.py behavior).\\\",\\n    \\\"fix_lines\\\": \\\"compute_bootstrap_ci.py:117 (gold_ent_set), 127 (pred_ent_set), 119-120 (parse failure return)\\\"\\n  },\\n  \\\"registry_alignment\\\": {\\n    \\\"docred\\\": {\\n      \\\"unconstrained\\\": {\\n        \\\"registry_ent_f1\\\": 58.15,\\n        \\\"bootstrap_ent_f1\\\": 58.15,\\n        \\\"delta\\\": 0.0,\\n        \\\"registry_rel_f1\\\": 7.74,\\n        \\\"bootstrap_rel_f1\\\": 7.74,\\n        \\\"delta_rel\\\": 0.0\\n      },\\n      \\\"full_s1\\\": {\\n        \\\"registry_ent_f1\\\": 59.37,\\n        \\\"bootstrap_ent_f1\\\": 59.38,\\n        \\\"delta\\\": 0.01,\\n        \\\"registry_rel_f1\\\": 8.23,\\n        \\\"bootstrap_rel_f1\\\": 8.24,\\n        \\\"delta_rel\\\": 0.01\\n      }\\n    },\\n    \\\"scierc\\\": {\\n      \\\"unconstrained\\\": {\\n        \\\"registry_ent_f1\\\": 31.01,\\n        \\\"bootstrap_ent_f1\\\": 31.01,\\n        \\\"delta\\\": 0.0,\\n        \\\"registry_rel_f1\\\": 8.23,\\n        \\\"bootstrap_rel_f1\\\": 8.23,\\n        \\\"delta_rel\\\": 0.0\\n      },\\n      \\\"full_s1\\\": {\\n        \\\"registry_ent_f1\\\": 30.98,\\n        \\\"bootstrap_ent_f1\\\": 30.98,\\n        \\\"delta\\\": 0.0,\\n        \\\"registry_rel_f1\\\": 8.36,\\n        \\\"bootstrap_rel_f1\\\": 8.36,\\n        \\\"delta_rel\\\": 0.0\\n      }\\n    },\\n    \\\"note\\\": \\\"All deltas <= 0.01pp (rounding). Registry alignment verified.\\\"\\n  },\\n  \\\"grammar_only_entity_f1\\\": {\\n    \\\"docred\\\": {\\n      \\\"entity_f1\\\": 59.38,\\n      \\\"entity_precision\\\": 58.47,\\n      \\\"entity_recall\\\": 60.32,\\n      \\\"tp\\\": 11590,\\n      \\\"gold\\\": 19215,\\n      \\\"pred\\\": 19823,\\n      \\\"note\\\": \\\"Previously null in registry. Grammar constraint (JSON schema enum) enforces valid entity types, improving entity F1 by +1.23pp over unconstrained (p<0.001).\\\"\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "42b5f0a0-ff6c-4999-b77d-f6b3f4b0c705",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"scierc\\\\\\\": {\\\\n    \\\\\\\"per_config\\\\\\\": {\\\\n      \\\\\\\"unconstrained\\\\\\\": {\\\\n        \\\\\\\"ent_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.310111,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.310169,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.288275,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.332452,\\\\n          \\\\\\\"std\\\\\\\": 0.011217\\\\n        },\\\\n        \\\\\\\"rel_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.082283,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.082357,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.064876,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.10089,\\\\n          \\\\\\\"std\\\\\\\": 0.009112\\\\n        }\\\\n      },\\\\n      \\\\\\\"grammar_only\\\\\\\": {\\\\n        \\\\\\\"ent_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.309846,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.309905,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.288045,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.332121,\\\\n          \\\\\\\"std\\\\\\\": 0.011184\\\\n        },\\\\n        \\\\\\\"rel_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.082253,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.082321,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.064896,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.10087,\\\\n          \\\\\\\"std\\\\\\\": 0.009103\\\\n        }\\\\n      },\\\\n      \\\\\\\"semantic_only\\\\\\\": {\\\\n        \\\\\\\"ent_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.310111,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.310169,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.288275,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.332452,\\\\n          \\\\\\\"std\\\\\\\": 0.011217\\\\n        },\\\\n        \\\\\\\"rel_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.081481,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.081547,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.064367,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.100038,\\\\n          \\\\\\\"std\\\\\\\": 0.009066\\\\n        }\\\\n      },\\\\n      \\\\\\\"full_s1\\\\\\\": {\\\\n        \\\\\\\"ent_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.309846,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.309905,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.288045,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.332121,\\\\n          \\\\\\\"std\\\\\\\": 0.011184\\\\n        },\\\\n        \\\\\\\"rel_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.083611,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.083708,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.065828,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.102677,\\\\n          \\\\\\\"std\\\\\\\": 0.009354\\\\n        }\\\\n      }\\\\n    },\\\\n    \\\\\\\"comparisons\\\\\\\": {\\\\n      \\\\\\\"unconstrained_vs_grammar_only\\\\\\\": {\\\\n        \\\\\\\"ent_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": -0.000266,\\\\n          \\\\\\\"delta_mean\\\\\\\": -0.000264,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.001065,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.000823,\\\\n          \\\\\\\"p_value\\\\\\\": 0.5266\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": -3e-05,\\\\n          \\\\\\\"delta_mean\\\\\\\": -3.6e-05,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.002234,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.002185,\\\\n          \\\\\\\"p_value\\\\\\\": 0.9798\\\\n        }\\\\n      },\\\\n      \\\\\\\"unconstrained_vs_semantic_only\\\\\\\": {\\\\n        \\\\\\\"ent_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.0,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.0,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.0,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.0,\\\\n          \\\\\\\"p_value\\\\\\\": 1.0\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": -0.000802,\\\\n          \\\\\\\"delta_mean\\\\\\\": -0.000811,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.003592,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.001478,\\\\n          \\\\\\\"p_value\\\\\\\": 0.4236\\\\n        }\\\\n      },\\\\n      \\\\\\\"unconstrained_vs_full_s1\\\\\\\": {\\\\n        \\\\\\\"ent_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": -0.000266,\\\\n          \\\\\\\"delta_mean\\\\\\\": -0.000264,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.001065,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.000823,\\\\n          \\\\\\\"p_value\\\\\\\": 0.5266\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.001328,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.001351,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.00235,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.005828,\\\\n          \\\\\\\"p_value\\\\\\\": 0.5824\\\\n        }\\\\n      },\\\\n      \\\\\\\"grammar_only_vs_full_s1\\\\\\\": {\\\\n        \\\\\\\"ent_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.0,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.0,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.0,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.0,\\\\n          \\\\\\\"p_value\\\\\\\": 1.0\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.001358,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.001387,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.0016,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.00536,\\\\n          \\\\\\\"p_value\\\\\\\": 0.5108\\\\n        }\\\\n      },\\\\n      \\\\\\\"semantic_only_vs_full_s1\\\\\\\": {\\\\n        \\\\\\\"ent_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": -0.000266,\\\\n          \\\\\\\"delta_mean\\\\\\\": -0.000264,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.001065,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.000823,\\\\n          \\\\\\\"p_value\\\\\\\": 0.5266\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.002129,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.002162,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.002094,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.00727,\\\\n          \\\\\\\"p_value\\\\\\\": 0.393\\\\n        }\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\\\\"docred\\\\\\\": {\\\\n    \\\\\\\"per_config\\\\\\\": {\\\\n      \\\\\\\"unconstrained\\\\\\\":\\\\n\\\\n... [截断: 输出过长，省略 1809 字符] ...\\\\n\\\\n   \\\\\\\"delta_mean\\\\\\\": 0.01228,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.009322,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.015463,\\\\n          \\\\\\\"p_value\\\\\\\": 0.0\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.005718,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.005738,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.003157,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.008757,\\\\n          \\\\\\\"p_value\\\\\\\": 0.0\\\\n        }\\\\n      },\\\\n      \\\\\\\"unconstrained_vs_semantic_only\\\\\\\": {\\\\n        \\\\\\\"ent_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 2.9e-05,\\\\n          \\\\\\\"delta_mean\\\\\\\": 2.9e-05,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.0,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.0001,\\\\n          \\\\\\\"p_value\\\\\\\": 0.7378\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": -7.9e-05,\\\\n          \\\\\\\"delta_mean\\\\\\\": -7.9e-05,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.001015,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.000873,\\\\n          \\\\\\\"p_value\\\\\\\": 0.8546\\\\n        }\\\\n      },\\\\n      \\\\\\\"unconstrained_vs_full_s1\\\\\\\": {\\\\n        \\\\\\\"ent_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.012309,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.012317,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.009362,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.015503,\\\\n          \\\\\\\"p_value\\\\\\\": 0.0\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.004961,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.00498,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.002276,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.00812,\\\\n          \\\\\\\"p_value\\\\\\\": 0.0\\\\n        }\\\\n      },\\\\n      \\\\\\\"grammar_only_vs_full_s1\\\\\\\": {\\\\n        \\\\\\\"ent_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 3.7e-05,\\\\n          \\\\\\\"delta_mean\\\\\\\": 3.7e-05,\\\\n          \\\\\\\"ci_lower\\\\\\\": -7.4e-05,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.000187,\\\\n          \\\\\\\"p_value\\\\\\\": 0.6556\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": -0.000757,\\\\n          \\\\\\\"delta_mean\\\\\\\": -0.000758,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.001706,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.000189,\\\\n          \\\\\\\"p_value\\\\\\\": 0.115\\\\n        }\\\\n      },\\\\n      \\\\\\\"semantic_only_vs_full_s1\\\\\\\": {\\\\n        \\\\\\\"ent_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.01228,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.012288,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.009322,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.015469,\\\\n          \\\\\\\"p_value\\\\\\\": 0.0\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.00504,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.005058,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.002408,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.008147,\\\\n          \\\\\\\"p_value\\\\\\\": 0.0\\\\n        }\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\\\\"metadata\\\\\\\": {\\\\n    \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n    \\\\\\\"ci_method\\\\\\\": \\\\\\\"percentile\\\\\\\",\\\\n    \\\\\\\"ci_level\\\\\\\": 0.95,\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"resample_unit\\\\\\\": \\\\\\\"sentence (SciERC) / document (DocRED)\\\\\\\",\\\\n    \\\\\\\"fix_applied\\\\\\\": \\\\\\\"Removed entity type filter (DOCRED_VALID_ENTITY_TYPES) and entity type normalization from docred_sample_stats pred_ent_set. Parse-failure documents now return all zeros (matching registry posthoc_filter.py behavior).\\\\\\\",\\\\n    \\\\\\\"fix_lines\\\\\\\": \\\\\\\"compute_bootstrap_ci.py:117 (gold_ent_set), 127 (pred_ent_set), 119-120 (parse failure return)\\\\\\\"\\\\n  },\\\\n  \\\\\\\"registry_alignment\\\\\\\": {\\\\n    \\\\\\\"docred\\\\\\\": {\\\\n      \\\\\\\"unconstrained\\\\\\\": {\\\\n        \\\\\\\"registry_ent_f1\\\\\\\": 58.15,\\\\n        \\\\\\\"bootstrap_ent_f1\\\\\\\": 58.15,\\\\n        \\\\\\\"delta\\\\\\\": 0.0,\\\\n        \\\\\\\"registry_rel_f1\\\\\\\": 7.74,\\\\n        \\\\\\\"bootstrap_rel_f1\\\\\\\": 7.74,\\\\n        \\\\\\\"delta_rel\\\\\\\": 0.0\\\\n      },\\\\n      \\\\\\\"full_s1\\\\\\\": {\\\\n        \\\\\\\"registry_ent_f1\\\\\\\": 59.37,\\\\n        \\\\\\\"bootstrap_ent_f1\\\\\\\": 59.38,\\\\n        \\\\\\\"delta\\\\\\\": 0.01,\\\\n        \\\\\\\"registry_rel_f1\\\\\\\": 8.23,\\\\n        \\\\\\\"bootstrap_rel_f1\\\\\\\": 8.24,\\\\n        \\\\\\\"delta_rel\\\\\\\": 0.01\\\\n      }\\\\n    },\\\\n    \\\\\\\"scierc\\\\\\\": {\\\\n      \\\\\\\"unconstrained\\\\\\\": {\\\\n        \\\\\\\"registry_ent_f1\\\\\\\": 31.01,\\\\n        \\\\\\\"bootstrap_ent_f1\\\\\\\": 31.01,\\\\n        \\\\\\\"delta\\\\\\\": 0.0,\\\\n        \\\\\\\"registry_rel_f1\\\\\\\": 8.23,\\\\n        \\\\\\\"bootstrap_rel_f1\\\\\\\": 8.23,\\\\n        \\\\\\\"delta_rel\\\\\\\": 0.0\\\\n      },\\\\n      \\\\\\\"full_s1\\\\\\\": {\\\\n        \\\\\\\"registry_ent_f1\\\\\\\": 30.98,\\\\n        \\\\\\\"bootstrap_ent_f1\\\\\\\": 30.98,\\\\n        \\\\\\\"delta\\\\\\\": 0.0,\\\\n        \\\\\\\"registry_rel_f1\\\\\\\": 8.36,\\\\n        \\\\\\\"bootstrap_rel_f1\\\\\\\": 8.36,\\\\n        \\\\\\\"delta_rel\\\\\\\": 0.0\\\\n      }\\\\n    },\\\\n    \\\\\\\"note\\\\\\\": \\\\\\\"All deltas <= 0.01pp (rounding). Registry alignment verified.\\\\\\\"\\\\n  },\\\\n  \\\\\\\"grammar_only_entity_f1\\\\\\\": {\\\\n    \\\\\\\"docred\\\\\\\": {\\\\n      \\\\\\\"entity_f1\\\\\\\": 59.38,\\\\n      \\\\\\\"entity_precision\\\\\\\": 58.47,\\\\n      \\\\\\\"entity_recall\\\\\\\": 60.32,\\\\n      \\\\\\\"tp\\\\\\\": 11590,\\\\n      \\\\\\\"gold\\\\\\\": 19215,\\\\n      \\\\\\\"pred\\\\\\\": 19823,\\\\n      \\\\\\\"note\\\\\\\": \\\\\\\"Previously null in registry. Grammar constraint (JSON schema enum) enforces valid entity types, improving entity F1 by +1.23pp over unconstrained (p<0.001).\\\\\\\"\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"per_config\\\": {\\n      \\\"unconstrained\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.310111,\\n          \\\"bootstrap_mean\\\": 0.310169,\\n          \\\"ci_lower\\\": 0.288275,\\n          \\\"ci_upper\\\": 0.332452,\\n          \\\"std\\\": 0.011217\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.082283,\\n          \\\"bootstrap_mean\\\": 0.082357,\\n          \\\"ci_lower\\\": 0.064876,\\n          \\\"ci_upper\\\": 0.10089,\\n          \\\"std\\\": 0.009112\\n        }\\n      },\\n      \\\"grammar_only\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.309846,\\n          \\\"bootstrap_mean\\\": 0.309905,\\n          \\\"ci_lower\\\": 0.288045,\\n          \\\"ci_upper\\\": 0.332121,\\n          \\\"std\\\": 0.011184\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.082253,\\n          \\\"bootstrap_mean\\\": 0.082321,\\n          \\\"ci_lower\\\": 0.064896,\\n          \\\"ci_upper\\\": 0.10087,\\n          \\\"std\\\": 0.009103\\n        }\\n      },\\n      \\\"semantic_only\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.310111,\\n          \\\"bootstrap_mean\\\": 0.310169,\\n          \\\"ci_lower\\\": 0.288275,\\n          \\\"ci_upper\\\": 0.332452,\\n          \\\"std\\\": 0.011217\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.081481,\\n          \\\"bootstrap_mean\\\": 0.081547,\\n          \\\"ci_lower\\\": 0.064367,\\n          \\\"ci_upper\\\": 0.100038,\\n          \\\"std\\\": 0.009066\\n        }\\n      },\\n      \\\"full_s1\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.309846,\\n          \\\"bootstrap_mean\\\": 0.309905,\\n          \\\"ci_lower\\\": 0.288045,\\n          \\\"ci_upper\\\": 0.332121,\\n          \\\"std\\\": 0.011184\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.083611,\\n          \\\"bootstrap_mean\\\": 0.083708,\\n          \\\"ci_lower\\\": 0.065828,\\n          \\\"ci_upper\\\": 0.102677,\\n          \\\"std\\\": 0.009354\\n        }\\n      }\\n    },\\n    \\\"comparisons\\\": {\\n      \\\"unconstrained_vs_grammar_only\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000266,\\n          \\\"delta_mean\\\": -0.000264,\\n          \\\"ci_lower\\\": -0.001065,\\n          \\\"ci_upper\\\": 0.000823,\\n          \\\"p_value\\\": 0.5266\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": -3e-05,\\n          \\\"delta_mean\\\": -3.6e-05,\\n          \\\"ci_lower\\\": -0.002234,\\n          \\\"ci_upper\\\": 0.002185,\\n          \\\"p_value\\\": 0.9798\\n        }\\n      },\\n      \\\"unconstrained_vs_semantic_only\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.0,\\n          \\\"delta_mean\\\": 0.0,\\n          \\\"ci_lower\\\": 0.0,\\n          \\\"ci_upper\\\": 0.0,\\n          \\\"p_value\\\": 1.0\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000802,\\n          \\\"delta_mean\\\": -0.000811,\\n          \\\"ci_lower\\\": -0.003592,\\n          \\\"ci_upper\\\": 0.001478,\\n          \\\"p_value\\\": 0.4236\\n        }\\n      },\\n      \\\"unconstrained_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000266,\\n          \\\"delta_mean\\\": -0.000264,\\n          \\\"ci_lower\\\": -0.001065,\\n          \\\"ci_upper\\\": 0.000823,\\n          \\\"p_value\\\": 0.5266\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.001328,\\n          \\\"delta_mean\\\": 0.001351,\\n          \\\"ci_lower\\\": -0.00235,\\n          \\\"ci_upper\\\": 0.005828,\\n          \\\"p_value\\\": 0.5824\\n        }\\n      },\\n      \\\"grammar_only_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.0,\\n          \\\"delta_mean\\\": 0.0,\\n          \\\"ci_lower\\\": 0.0,\\n          \\\"ci_upper\\\": 0.0,\\n          \\\"p_value\\\": 1.0\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.001358,\\n          \\\"delta_mean\\\": 0.001387,\\n          \\\"ci_lower\\\": -0.0016,\\n          \\\"ci_upper\\\": 0.00536,\\n          \\\"p_value\\\": 0.5108\\n        }\\n      },\\n      \\\"semantic_only_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000266,\\n          \\\"delta_mean\\\": -0.000264,\\n          \\\"ci_lower\\\": -0.001065,\\n          \\\"ci_upper\\\": 0.000823,\\n          \\\"p_value\\\": 0.5266\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.002129,\\n          \\\"delta_mean\\\": 0.002162,\\n          \\\"ci_lower\\\": -0.002094,\\n          \\\"ci_upper\\\": 0.00727,\\n          \\\"p_value\\\": 0.393\\n        }\\n      }\\n    }\\n  },\\n  \\\"docred\\\": {\\n    \\\"per_config\\\": {\\n      \\\"unconstrained\\\":\\n\\n... [截断: 输出过长，省略 1809 字符] ...\\n\\n   \\\"delta_mean\\\": 0.01228,\\n          \\\"ci_lower\\\": 0.009322,\\n          \\\"ci_upper\\\": 0.015463,\\n          \\\"p_value\\\": 0.0\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.005718,\\n          \\\"delta_mean\\\": 0.005738,\\n          \\\"ci_lower\\\": 0.003157,\\n          \\\"ci_upper\\\": 0.008757,\\n          \\\"p_value\\\": 0.0\\n        }\\n      },\\n      \\\"unconstrained_vs_semantic_only\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 2.9e-05,\\n          \\\"delta_mean\\\": 2.9e-05,\\n          \\\"ci_lower\\\": 0.0,\\n          \\\"ci_upper\\\": 0.0001,\\n          \\\"p_value\\\": 0.7378\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": -7.9e-05,\\n          \\\"delta_mean\\\": -7.9e-05,\\n          \\\"ci_lower\\\": -0.001015,\\n          \\\"ci_upper\\\": 0.000873,\\n          \\\"p_value\\\": 0.8546\\n        }\\n      },\\n      \\\"unconstrained_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.012309,\\n          \\\"delta_mean\\\": 0.012317,\\n          \\\"ci_lower\\\": 0.009362,\\n          \\\"ci_upper\\\": 0.015503,\\n          \\\"p_value\\\": 0.0\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.004961,\\n          \\\"delta_mean\\\": 0.00498,\\n          \\\"ci_lower\\\": 0.002276,\\n          \\\"ci_upper\\\": 0.00812,\\n          \\\"p_value\\\": 0.0\\n        }\\n      },\\n      \\\"grammar_only_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 3.7e-05,\\n          \\\"delta_mean\\\": 3.7e-05,\\n          \\\"ci_lower\\\": -7.4e-05,\\n          \\\"ci_upper\\\": 0.000187,\\n          \\\"p_value\\\": 0.6556\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000757,\\n          \\\"delta_mean\\\": -0.000758,\\n          \\\"ci_lower\\\": -0.001706,\\n          \\\"ci_upper\\\": 0.000189,\\n          \\\"p_value\\\": 0.115\\n        }\\n      },\\n      \\\"semantic_only_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.01228,\\n          \\\"delta_mean\\\": 0.012288,\\n          \\\"ci_lower\\\": 0.009322,\\n          \\\"ci_upper\\\": 0.015469,\\n          \\\"p_value\\\": 0.0\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.00504,\\n          \\\"delta_mean\\\": 0.005058,\\n          \\\"ci_lower\\\": 0.002408,\\n          \\\"ci_upper\\\": 0.008147,\\n          \\\"p_value\\\": 0.0\\n        }\\n      }\\n    }\\n  },\\n  \\\"metadata\\\": {\\n    \\\"n_bootstrap\\\": 10000,\\n    \\\"ci_method\\\": \\\"percentile\\\",\\n    \\\"ci_level\\\": 0.95,\\n    \\\"seed\\\": 42,\\n    \\\"resample_unit\\\": \\\"sentence (SciERC) / document (DocRED)\\\",\\n    \\\"fix_applied\\\": \\\"Removed entity type filter (DOCRED_VALID_ENTITY_TYPES) and entity type normalization from docred_sample_stats pred_ent_set. Parse-failure documents now return all zeros (matching registry posthoc_filter.py behavior).\\\",\\n    \\\"fix_lines\\\": \\\"compute_bootstrap_ci.py:117 (gold_ent_set), 127 (pred_ent_set), 119-120 (parse failure return)\\\"\\n  },\\n  \\\"registry_alignment\\\": {\\n    \\\"docred\\\": {\\n      \\\"unconstrained\\\": {\\n        \\\"registry_ent_f1\\\": 58.15,\\n        \\\"bootstrap_ent_f1\\\": 58.15,\\n        \\\"delta\\\": 0.0,\\n        \\\"registry_rel_f1\\\": 7.74,\\n        \\\"bootstrap_rel_f1\\\": 7.74,\\n        \\\"delta_rel\\\": 0.0\\n      },\\n      \\\"full_s1\\\": {\\n        \\\"registry_ent_f1\\\": 59.37,\\n        \\\"bootstrap_ent_f1\\\": 59.38,\\n        \\\"delta\\\": 0.01,\\n        \\\"registry_rel_f1\\\": 8.23,\\n        \\\"bootstrap_rel_f1\\\": 8.24,\\n        \\\"delta_rel\\\": 0.01\\n      }\\n    },\\n    \\\"scierc\\\": {\\n      \\\"unconstrained\\\": {\\n        \\\"registry_ent_f1\\\": 31.01,\\n        \\\"bootstrap_ent_f1\\\": 31.01,\\n        \\\"delta\\\": 0.0,\\n        \\\"registry_rel_f1\\\": 8.23,\\n        \\\"bootstrap_rel_f1\\\": 8.23,\\n        \\\"delta_rel\\\": 0.0\\n      },\\n      \\\"full_s1\\\": {\\n        \\\"registry_ent_f1\\\": 30.98,\\n        \\\"bootstrap_ent_f1\\\": 30.98,\\n        \\\"delta\\\": 0.0,\\n        \\\"registry_rel_f1\\\": 8.36,\\n        \\\"bootstrap_rel_f1\\\": 8.36,\\n        \\\"delta_rel\\\": 0.0\\n      }\\n    },\\n    \\\"note\\\": \\\"All deltas <= 0.01pp (rounding). Registry alignment verified.\\\"\\n  },\\n  \\\"grammar_only_entity_f1\\\": {\\n    \\\"docred\\\": {\\n      \\\"entity_f1\\\": 59.38,\\n      \\\"entity_precision\\\": 58.47,\\n      \\\"entity_recall\\\": 60.32,\\n      \\\"tp\\\": 11590,\\n      \\\"gold\\\": 19215,\\n      \\\"pred\\\": 19823,\\n      \\\"note\\\": \\\"Previously null in registry. Grammar constraint (JSON schema enum) enforces valid entity types, improving entity F1 by +1.23pp over unconstrained (p<0.001).\\\"\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WqgkQ3Ynz73YeF9utpJV2r`</summary>

```json
{
  "server": "westd-16980",
  "command": "cat /root/schema_semantic_constrained_ie/outputs/bootstrap_ci_results_llama.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "e6882d39-2f4a-45be-9043-7154770eeb30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018a1DqpzB4ScVCF8nHES3B6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4114,
      "cache_read_input_tokens": 45592,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4114
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

_source line 50 · 2026-05-17T14:13:00.571Z_

<details><summary>↩ Tool result · `toolu_01WqgkQ3Ynz73YeF9utpJV2r`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"per_config\\\": {\\n      \\\"unconstrained\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.235294,\\n          \\\"bootstrap_mean\\\": 0.235528,\\n          \\\"ci_lower\\\": 0.21466,\\n          \\\"ci_upper\\\": 0.256498,\\n          \\\"std\\\": 0.010899\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.026714,\\n          \\\"bootstrap_mean\\\": 0.026775,\\n          \\\"ci_lower\\\": 0.016464,\\n          \\\"ci_upper\\\": 0.038443,\\n          \\\"std\\\": 0.005622\\n        }\\n      },\\n      \\\"full_s1\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.234867,\\n          \\\"bootstrap_mean\\\": 0.234796,\\n          \\\"ci_lower\\\": 0.213549,\\n          \\\"ci_upper\\\": 0.256148,\\n          \\\"std\\\": 0.010908\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.025405,\\n          \\\"bootstrap_mean\\\": 0.025391,\\n          \\\"ci_lower\\\": 0.015321,\\n          \\\"ci_upper\\\": 0.036586,\\n          \\\"std\\\": 0.005426\\n        }\\n      }\\n    },\\n    \\\"comparisons\\\": {\\n      \\\"unconstrained_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.000317,\\n          \\\"delta_mean\\\": 0.000302,\\n          \\\"ci_lower\\\": -0.001756,\\n          \\\"ci_upper\\\": 0.002192,\\n          \\\"p_value\\\": 0.7618\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000442,\\n          \\\"delta_mean\\\": -0.000439,\\n          \\\"ci_lower\\\": -0.000992,\\n          \\\"ci_upper\\\": -7.7e-05,\\n          \\\"p_value\\\": 0.0106\\n        }\\n      }\\n    }\\n  },\\n  \\\"docred\\\": {\\n    \\\"per_config\\\": {\\n      \\\"unconstrained\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.556542,\\n          \\\"bootstrap_mean\\\": 0.556564,\\n          \\\"ci_lower\\\": 0.544593,\\n          \\\"ci_upper\\\": 0.568411,\\n          \\\"std\\\": 0.006054\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.059779,\\n          \\\"bootstrap_mean\\\": 0.059832,\\n          \\\"ci_lower\\\": 0.053295,\\n          \\\"ci_upper\\\": 0.066744,\\n          \\\"std\\\": 0.003476\\n        }\\n      },\\n      \\\"full_s1\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.550089,\\n          \\\"bootstrap_mean\\\": 0.550115,\\n          \\\"ci_lower\\\": 0.537481,\\n          \\\"ci_upper\\\": 0.562624,\\n          \\\"std\\\": 0.006379\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.062749,\\n          \\\"bootstrap_mean\\\": 0.062798,\\n          \\\"ci_lower\\\": 0.055976,\\n          \\\"ci_upper\\\": 0.070014,\\n          \\\"std\\\": 0.003577\\n        }\\n      }\\n    },\\n    \\\"comparisons\\\": {\\n      \\\"unconstrained_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.006453,\\n          \\\"delta_mean\\\": -0.006442,\\n          \\\"ci_lower\\\": -0.012298,\\n          \\\"ci_upper\\\": -0.000893,\\n          \\\"p_value\\\": 0.022\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.00297,\\n          \\\"delta_mean\\\": 0.002964,\\n          \\\"ci_lower\\\": 0.000618,\\n          \\\"ci_upper\\\": 0.005354,\\n          \\\"p_value\\\": 0.0128\\n        }\\n      }\\n    }\\n  },\\n  \\\"metadata\\\": {\\n    \\\"model\\\": \\\"llama\\\",\\n    \\\"n_bootstrap\\\": 10000,\\n    \\\"ci_method\\\": \\\"percentile\\\",\\n    \\\"ci_level\\\": 0.95,\\n    \\\"seed\\\": 42,\\n    \\\"resample_unit\\\": \\\"sentence (SciERC) / document (DocRED)\\\",\\n    \\\"registry_tolerance_pp\\\": 0.05\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "526c3e4a-0702-4767-a018-41ac793c8792",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"scierc\\\\\\\": {\\\\n    \\\\\\\"per_config\\\\\\\": {\\\\n      \\\\\\\"unconstrained\\\\\\\": {\\\\n        \\\\\\\"ent_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.235294,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.235528,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.21466,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.256498,\\\\n          \\\\\\\"std\\\\\\\": 0.010899\\\\n        },\\\\n        \\\\\\\"rel_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.026714,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.026775,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.016464,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.038443,\\\\n          \\\\\\\"std\\\\\\\": 0.005622\\\\n        }\\\\n      },\\\\n      \\\\\\\"full_s1\\\\\\\": {\\\\n        \\\\\\\"ent_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.234867,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.234796,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.213549,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.256148,\\\\n          \\\\\\\"std\\\\\\\": 0.010908\\\\n        },\\\\n        \\\\\\\"rel_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.025405,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.025391,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.015321,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.036586,\\\\n          \\\\\\\"std\\\\\\\": 0.005426\\\\n        }\\\\n      }\\\\n    },\\\\n    \\\\\\\"comparisons\\\\\\\": {\\\\n      \\\\\\\"unconstrained_vs_full_s1\\\\\\\": {\\\\n        \\\\\\\"ent_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.000317,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.000302,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.001756,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.002192,\\\\n          \\\\\\\"p_value\\\\\\\": 0.7618\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": -0.000442,\\\\n          \\\\\\\"delta_mean\\\\\\\": -0.000439,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.000992,\\\\n          \\\\\\\"ci_upper\\\\\\\": -7.7e-05,\\\\n          \\\\\\\"p_value\\\\\\\": 0.0106\\\\n        }\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\\\\"docred\\\\\\\": {\\\\n    \\\\\\\"per_config\\\\\\\": {\\\\n      \\\\\\\"unconstrained\\\\\\\": {\\\\n        \\\\\\\"ent_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.556542,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.556564,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.544593,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.568411,\\\\n          \\\\\\\"std\\\\\\\": 0.006054\\\\n        },\\\\n        \\\\\\\"rel_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.059779,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.059832,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.053295,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.066744,\\\\n          \\\\\\\"std\\\\\\\": 0.003476\\\\n        }\\\\n      },\\\\n      \\\\\\\"full_s1\\\\\\\": {\\\\n        \\\\\\\"ent_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.550089,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.550115,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.537481,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.562624,\\\\n          \\\\\\\"std\\\\\\\": 0.006379\\\\n        },\\\\n        \\\\\\\"rel_f1\\\\\\\": {\\\\n          \\\\\\\"point_estimate\\\\\\\": 0.062749,\\\\n          \\\\\\\"bootstrap_mean\\\\\\\": 0.062798,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.055976,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.070014,\\\\n          \\\\\\\"std\\\\\\\": 0.003577\\\\n        }\\\\n      }\\\\n    },\\\\n    \\\\\\\"comparisons\\\\\\\": {\\\\n      \\\\\\\"unconstrained_vs_full_s1\\\\\\\": {\\\\n        \\\\\\\"ent_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": -0.006453,\\\\n          \\\\\\\"delta_mean\\\\\\\": -0.006442,\\\\n          \\\\\\\"ci_lower\\\\\\\": -0.012298,\\\\n          \\\\\\\"ci_upper\\\\\\\": -0.000893,\\\\n          \\\\\\\"p_value\\\\\\\": 0.022\\\\n        },\\\\n        \\\\\\\"rel_f1_delta\\\\\\\": {\\\\n          \\\\\\\"delta_point\\\\\\\": 0.00297,\\\\n          \\\\\\\"delta_mean\\\\\\\": 0.002964,\\\\n          \\\\\\\"ci_lower\\\\\\\": 0.000618,\\\\n          \\\\\\\"ci_upper\\\\\\\": 0.005354,\\\\n          \\\\\\\"p_value\\\\\\\": 0.0128\\\\n        }\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\\\\"metadata\\\\\\\": {\\\\n    \\\\\\\"model\\\\\\\": \\\\\\\"llama\\\\\\\",\\\\n    \\\\\\\"n_bootstrap\\\\\\\": 10000,\\\\n    \\\\\\\"ci_method\\\\\\\": \\\\\\\"percentile\\\\\\\",\\\\n    \\\\\\\"ci_level\\\\\\\": 0.95,\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"resample_unit\\\\\\\": \\\\\\\"sentence (SciERC) / document (DocRED)\\\\\\\",\\\\n    \\\\\\\"registry_tolerance_pp\\\\\\\": 0.05\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.47}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"scierc\\\": {\\n    \\\"per_config\\\": {\\n      \\\"unconstrained\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.235294,\\n          \\\"bootstrap_mean\\\": 0.235528,\\n          \\\"ci_lower\\\": 0.21466,\\n          \\\"ci_upper\\\": 0.256498,\\n          \\\"std\\\": 0.010899\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.026714,\\n          \\\"bootstrap_mean\\\": 0.026775,\\n          \\\"ci_lower\\\": 0.016464,\\n          \\\"ci_upper\\\": 0.038443,\\n          \\\"std\\\": 0.005622\\n        }\\n      },\\n      \\\"full_s1\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.234867,\\n          \\\"bootstrap_mean\\\": 0.234796,\\n          \\\"ci_lower\\\": 0.213549,\\n          \\\"ci_upper\\\": 0.256148,\\n          \\\"std\\\": 0.010908\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.025405,\\n          \\\"bootstrap_mean\\\": 0.025391,\\n          \\\"ci_lower\\\": 0.015321,\\n          \\\"ci_upper\\\": 0.036586,\\n          \\\"std\\\": 0.005426\\n        }\\n      }\\n    },\\n    \\\"comparisons\\\": {\\n      \\\"unconstrained_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.000317,\\n          \\\"delta_mean\\\": 0.000302,\\n          \\\"ci_lower\\\": -0.001756,\\n          \\\"ci_upper\\\": 0.002192,\\n          \\\"p_value\\\": 0.7618\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.000442,\\n          \\\"delta_mean\\\": -0.000439,\\n          \\\"ci_lower\\\": -0.000992,\\n          \\\"ci_upper\\\": -7.7e-05,\\n          \\\"p_value\\\": 0.0106\\n        }\\n      }\\n    }\\n  },\\n  \\\"docred\\\": {\\n    \\\"per_config\\\": {\\n      \\\"unconstrained\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.556542,\\n          \\\"bootstrap_mean\\\": 0.556564,\\n          \\\"ci_lower\\\": 0.544593,\\n          \\\"ci_upper\\\": 0.568411,\\n          \\\"std\\\": 0.006054\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.059779,\\n          \\\"bootstrap_mean\\\": 0.059832,\\n          \\\"ci_lower\\\": 0.053295,\\n          \\\"ci_upper\\\": 0.066744,\\n          \\\"std\\\": 0.003476\\n        }\\n      },\\n      \\\"full_s1\\\": {\\n        \\\"ent_f1\\\": {\\n          \\\"point_estimate\\\": 0.550089,\\n          \\\"bootstrap_mean\\\": 0.550115,\\n          \\\"ci_lower\\\": 0.537481,\\n          \\\"ci_upper\\\": 0.562624,\\n          \\\"std\\\": 0.006379\\n        },\\n        \\\"rel_f1\\\": {\\n          \\\"point_estimate\\\": 0.062749,\\n          \\\"bootstrap_mean\\\": 0.062798,\\n          \\\"ci_lower\\\": 0.055976,\\n          \\\"ci_upper\\\": 0.070014,\\n          \\\"std\\\": 0.003577\\n        }\\n      }\\n    },\\n    \\\"comparisons\\\": {\\n      \\\"unconstrained_vs_full_s1\\\": {\\n        \\\"ent_f1_delta\\\": {\\n          \\\"delta_point\\\": -0.006453,\\n          \\\"delta_mean\\\": -0.006442,\\n          \\\"ci_lower\\\": -0.012298,\\n          \\\"ci_upper\\\": -0.000893,\\n          \\\"p_value\\\": 0.022\\n        },\\n        \\\"rel_f1_delta\\\": {\\n          \\\"delta_point\\\": 0.00297,\\n          \\\"delta_mean\\\": 0.002964,\\n          \\\"ci_lower\\\": 0.000618,\\n          \\\"ci_upper\\\": 0.005354,\\n          \\\"p_value\\\": 0.0128\\n        }\\n      }\\n    }\\n  },\\n  \\\"metadata\\\": {\\n    \\\"model\\\": \\\"llama\\\",\\n    \\\"n_bootstrap\\\": 10000,\\n    \\\"ci_method\\\": \\\"percentile\\\",\\n    \\\"ci_level\\\": 0.95,\\n    \\\"seed\\\": 42,\\n    \\\"resample_unit\\\": \\\"sentence (SciERC) / document (DocRED)\\\",\\n    \\\"registry_tolerance_pp\\\": 0.05\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to write the audit report.

Summary of findings:

## All three bootstrap scripts use corpus micro-F1

### Mechanism (identical across all scripts):
1. Per-sample (document/sentence) TP/gold/pred counts are collected
2. Bootstrap resampling draws N samples with replacement
3. TP/gold/pred are **summed** across all resampled samples (`.sum(axis=1)`)
4. F1 is computed from global sums: `P = TP_sum / pred_sum`, `R = TP_sum / gold_sum`, `F1 = 2PR/(P+R)`


5. This is **corpus micro-F1**, consistent with the main tables — not document-level macro-F1, which would compute F1 per document first then average.

I've audited three scripts: `compute_bootstrap_ci.py` for zero-shot GPT-4o on SciERC and DocRED, `compute_bootstrap_ci_ft.py` for fine-tuned LoRA composability, and a third script that all use the same micro-F1 logic.

Registry alignment checks show negligible discrepancies (≤0.01pp for zero-shot v2, 0.05pp tolerance for Llama), so everything's consistent and ready for the audit report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "5e1e521f-7c20-4013-98d0-d10824fdd0c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMs6c6kcwadZPbVV4bUvBu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9092,
      "cache_read_input_tokens": 49706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9092
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

_source line 52_

Audit complete. All three scripts use corpus micro-F1. Now writing the report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "f699a3a7-d084-4eaf-a69c-6148c884cbb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMs6c6kcwadZPbVV4bUvBu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9092,
      "cache_read_input_tokens": 49706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9092
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

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01TJNfU9r1FM4heEmXiBxZEA`</summary>

````json
{
  "name": "r5_bootstrap_method_audit",
  "type": "report",
  "description": "Bootstrap F1 计算方式核查：确认所有脚本使用 corpus micro-F1，与主表一致",
  "project": "schema_semantic_constrained_ie",
  "content_filename": "r5_bootstrap_method_audit.md",
  "content": "# Bootstrap F1 计算方式核查报告\n\n## 结论\n\n**所有 bootstrap 脚本已使用 corpus micro-F1，与主表 (Table 2/4) 一致。无需修改。**\n\n## 审计范围\n\n| 脚本 | 用途 | F1 类型 |\n|------|------|---------|\n| `compute_bootstrap_ci.py` | ZS GPT-4o (SciERC + DocRED) | corpus micro-F1 ✓ |\n| `compute_bootstrap_ci_ft.py` | FT LoRA composability (4 settings) | corpus micro-F1 ✓ |\n| `compute_bootstrap_ci_llama.py` | ZS Llama (SciERC + DocRED) | corpus micro-F1 ✓ |\n\n## 关键代码逻辑 (三个脚本均相同)\n\n`bootstrap_f1` 函数 (以 `compute_bootstrap_ci.py:150` 为例):\n\n```python\n# 收集每个 sample 的 TP/gold/pred\ntps = np.array([s[\"tp\"] for s in sample_stats])\ngolds = np.array([s[\"gold\"] for s in sample_stats])\npreds = np.array([s[\"pred\"] for s in sample_stats])\n\n# Bootstrap: resample → SUM across resampled samples → compute F1\nindices = rng.randint(0, n, size=(n_bootstrap, n))\ntp_sums = tps[indices].sum(axis=1)      # 全局汇总\ngold_sums = golds[indices].sum(axis=1)\npred_sums = preds[indices].sum(axis=1)\nf1_samples = _f1_from_arrays(tp_sums, gold_sums, pred_sums)  # micro-F1\n```\n\n**这是 corpus micro-F1**：先对 bootstrap sample 内所有 document 的 TP/gold/pred 求和，再从全局计数计算 P/R/F1。\n\n如果是 document-level macro-F1，则会先对每个 document 独立算 F1，再取平均。代码中没有这种逻辑。\n\n`paired_bootstrap_test` 使用同样的 sum-then-F1 逻辑。\n\n## Registry Alignment\n\nZS v2 结果文件包含 registry alignment 校验：\n- SciERC: delta ≤ 0.00pp (unconstrained, full_s1)\n- DocRED: delta ≤ 0.01pp (rounding)\n\nLlama 结果文件有 explicit tolerance check (0.05pp)。\n\nFT composability 结果的 point estimate 直接从相同的 micro-F1 逻辑计算。\n\n## ZS Bootstrap 一致性确认\n\n- `compute_bootstrap_ci.py` (GPT-4o ZS): corpus micro-F1 ✓\n- `compute_bootstrap_ci_llama.py` (Llama ZS): imports `bootstrap_f1` 和 `paired_bootstrap_test` from `compute_bootstrap_ci.py`,同一套代码 ✓\n- DocRED p<0.001 (unconstrained vs full_s1): 基于 corpus micro-F1 的 paired bootstrap test，`p_value: 0.0` ✓\n\n## 现有结果汇总 (无变化)\n\n### ZS GPT-4o (compute_bootstrap_ci_results_v2.json)\n| 对比 | Dataset | ΔR-F1 (pp) | 95% CI | p-value |\n|------|---------|------------|--------|---------|\n| unc vs full_s1 | SciERC | +0.13 | [-0.24, +0.58] | 0.582 |\n| unc vs full_s1 | DocRED | +0.50 | [+0.23, +0.81] | <0.001 |\n\n### ZS Llama (bootstrap_ci_results_llama.json)\n| 对比 | Dataset | ΔR-F1 (pp) | 95% CI | p-value |\n|------|---------|------------|--------|---------|\n| unc vs full_s1 | SciERC | -0.04 | [-0.10, -0.01] | 0.011 |\n| unc vs full_s1 | DocRED | +0.30 | [+0.06, +0.54] | 0.013 |\n\n### FT LoRA (bootstrap_ci_ft_composability.json)\n| Setting | ΔR-F1 (pp) | 95% CI | p-value |\n|---------|------------|--------|---------|\n| Qwen-LoRA-SciERC | -0.10 | [-0.30, 0.00] | 0.726 |\n| Qwen-LoRA-DocRED | -0.37 | [-0.76, -0.05] | 0.014 |\n| Llama-LoRA-SciERC | +0.02 | [0.00, +0.07] | 0.736 |\n| Llama-LoRA-DocRED | +0.02 | [-0.15, +0.22] | 0.851 |\n\n## 结论\n\n无需修改任何脚本或重新运行实验。所有 bootstrap 统计量与主表的 corpus micro-F1 计算方式一致。\n",
  "tags": [
    "bootstrap",
    "audit",
    "micro-f1",
    "statistical-testing"
  ]
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "f7059636-c6c9-413b-b9d6-68ac786fe67a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMs6c6kcwadZPbVV4bUvBu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9092,
      "cache_read_input_tokens": 49706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9092
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

_source line 54 · 2026-05-17T14:13:37.102Z_

<details><summary>↩ Tool result · `toolu_01TJNfU9r1FM4heEmXiBxZEA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260517_8b7fcd\", \"name\": \"r5_bootstrap_method_audit\", \"type\": \"report\", \"description\": \"Bootstrap F1 计算方式核查：确认所有脚本使用 corpus micro-F1，与主表一致\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/r5_bootstrap_method_audit.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-17T14:13:36.911801+00:00\", \"tags\": [\"bootstrap\", \"audit\", \"micro-f1\", \"statistical-testing\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "fb6d77de-acbd-4fed-9ead-0bdbf0b4fb2f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260517_8b7fcd\\\", \\\"name\\\": \\\"r5_bootstrap_method_audit\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Bootstrap F1 计算方式核查：确认所有脚本使用 corpus micro-F1，与主表一致\\\", \\\"path\\\": \\\"projects/schema_semantic_constrained_ie/artifacts/_project/report/r5_bootstrap_method_audit.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"schema_semantic_constrained_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-17T14:13:36.911801+00:00\\\", \\\"tags\\\": [\\\"bootstrap\\\", \\\"audit\\\", \\\"micro-f1\\\", \\\"statistical-testing\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260517_8b7fcd\", \"name\": \"r5_bootstrap_method_audit\", \"type\": \"report\", \"description\": \"Bootstrap F1 计算方式核查：确认所有脚本使用 corpus micro-F1，与主表一致\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/report/r5_bootstrap_method_audit.md\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-17T14:13:36.911801+00:00\", \"tags\": [\"bootstrap\", \"audit\", \"micro-f1\", \"statistical-testing\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 55_

**审计结论：所有 bootstrap 脚本已使用 corpus micro-F1，无需修改。**

三个脚本 (`compute_bootstrap_ci.py`, `compute_bootstrap_ci_ft.py`, `compute_bootstrap_ci_llama.py`) 均采用相同逻辑：bootstrap resample 后对 TP/gold/pred 全局求和再算 F1（即 micro-F1），与主表计算方式一致。ZS 和 FT 的所有 p-value 和 CI 均无需更新。

报告已注册：`r5_bootstrap_method_audit`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "uuid": "f0b815f2-2821-4d4b-92c6-b3741a97bd6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195sWnckvZ3vWhgMAJjWVom",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2395,
      "cache_read_input_tokens": 58798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2395
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

_source line 56_

**审计结论：所有 bootstrap 脚本已使用 corpus micro-F1，无需修改。**

三个脚本 (`compute_bootstrap_ci.py`, `compute_bootstrap_ci_ft.py`, `compute_bootstrap_ci_llama.py`) 均采用相同逻辑：bootstrap resample 后对 TP/gold/pred 全局求和再算 F1（即 micro-F1），与主表计算方式一致。ZS 和 FT 的所有 p-value 和 CI 均无需更新。

报告已注册：`r5_bootstrap_method_audit`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 114052,
  "duration_api_ms": 110917,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "4de90974-122f-4fd9-95fb-37d2dff4f091",
  "total_cost_usd": 0.6862104999999998,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 49352,
    "cache_read_input_tokens": 450235,
    "output_tokens": 6053,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 49352,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 168,
        "cache_read_input_tokens": 58798,
        "cache_creation_input_tokens": 2395,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2395
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1158,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001238,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 6053,
      "cacheReadInputTokens": 450235,
      "cacheCreationInputTokens": 49352,
      "webSearchRequests": 0,
      "costUSD": 0.6849725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8737f027-c1c7-45b6-9448-4df3d25d7009"
}
```

</details>

---
