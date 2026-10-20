# fix exp 075 keyerror emergency

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_fix_exp-075-keyerror-emergency_20260519T174019.log`
- **Structured JSON:** [`fceded03deefcc8dad7b.json`](../../sessions/fc/fceded03deefcc8dad7b.json)

## Before a recorded user message

20 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
    "mcp__agent-ml-research__submit_training_job",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "e2258ecb-c7fd-4526-a4f5-417cc60aa232",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus/memory/"
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
    "resetsAt": 1779215400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f59900df-443f-4d29-bfca-20b2cf0be961",
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down the task:

1. Kill exp-075 process (run_contrastive.py) on westd-25068
2. Fix KeyError in run_contrastive.py (key name mismatch between contrastive_score_candidate() return dict and process_single() at line 379)
3. Also check/fix normalization at line 212
4. Dry-run 3 problems to verify
5. Redeploy with submit_training_job

Let me start by:
- Killing the process on the server
- Reading the source code to understand the bug


- Handling these steps in parallel
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "fed4ec27-d982-4fee-866e-49441adb19be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXpVXQzueqQaeLj638ewZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12594,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12594
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

_source line 5_

开始执行。先并行：kill 进程 + 读源码定位 bug。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "9cbc7c3c-902d-4551-96d9-076d2b5c2ee1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXpVXQzueqQaeLj638ewZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12594,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12594
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WhXRa9frw8mafbSaErP7jU`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__kill_job",
  "max_results": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "450e2b53-8db9-4586-8c1a-3838bb2f2f47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXpVXQzueqQaeLj638ewZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12594,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12594
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

_source line 7 · 2026-05-19T17:40:34.679Z_

<details><summary>↩ Tool result · `toolu_01WhXRa9frw8mafbSaErP7jU`</summary>

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
  "tool_name": "mcp__agent-ml-research__submit_training_job"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__kill_job"
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
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "5b462d0a-80ef-4a07-bb1c-8139352900b9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__kill_job"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__kill_job",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Let me start by doing things in parallel:
1. Find the run_contrastive.py process to kill
2. Read the source code to understand the bug
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "4e559783-17f0-4b48-8050-05f20bf69b0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmrBquFPrbVMc83NZMvJvy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 24435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2559
      },
      "output_tokens": 31,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JJqmiuR3G2HVA7sU4LfAjh`</summary>

```json
{
  "server": "westd-25068",
  "command": "ps aux | grep run_contrastive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "786c5634-e2b2-443a-8acd-b3739c275594",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmrBquFPrbVMc83NZMvJvy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 24435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2559
      },
      "output_tokens": 31,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T17:40:38.913Z_

<details><summary>↩ Tool result · `toolu_01JJqmiuR3G2HVA7sU4LfAjh`</summary>

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
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "14f6eeee-a30c-4194-8cbd-3106ecc7f39e",
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PCZTdxGeovr64ToS6bQHjV`</summary>

```json
{
  "server": "westd-25068",
  "command": "cat /root/symb_invariant_consensus/run_contrastive.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "7263c328-26c0-4f2f-971e-4d2acd269910",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmrBquFPrbVMc83NZMvJvy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2559,
      "cache_read_input_tokens": 24435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2559
      },
      "output_tokens": 31,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T17:40:40.352Z_

<details><summary>↩ Tool result · `toolu_01PCZTdxGeovr64ToS6bQHjV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nContrastive Constraint Generation Pipeline for FOLIO.\\n\\nInstead of extracting constraints from same-source SC traces (which lack\\nindependence), this pipeline generates PRO and CON constraints for each\\ncandidate answer independently via targeted LLM prompts, then uses\\ncontrastive MAX-SAT scoring to select the best answer.\\n\\nThree phases:\\n  Phase 1 — SC voting: generate K traces, majority-vote to get candidate set\\n  Phase 2 — Contrastive constraint generation: for each candidate, prompt the\\n            LLM K_contrast times to produce supporting (pro) and refuting (con)\\n            FOL constraints\\n  Phase 3 — Contrastive MAX-SAT scoring: score = MAX-SAT(pro) - α·MAX-SAT(con)\\n\\nUsage:\\n  python run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 \\\\\\n    --api-base http://localhost:8000/v1 --model auto \\\\\\n    --data data/folio_full.json \\\\\\n    --output results/exp075_contrastive/results.json \\\\\\n    --save-intermediates\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom collections import Counter\\n\\nfrom sica.trace_generator import VLLMGenerator, MockGenerator, extract_boxed_answer\\nfrom sica.constraint_extractor import VLLMBackend, MockLLM, ConstraintExtractor\\nfrom sica.z3_maxsat import (\\n    ConstraintDeduplicator, MaxSATSolver, parse_z3_formula, UniqueConstraint,\\n)\\nfrom sica.pipeline import normalize_logic_answer, _group_logic_answers\\nfrom baselines.self_consistency import SelfConsistency\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s %(levelname)s %(message)s\\\",\\n    handlers=[logging.StreamHandler(sys.stdout)],\\n)\\nlogger = logging.getLogger(__name__)\\n\\n# ---------------------------------------------------------------------------\\n# Contrastive constraint generation prompt\\n# ---------------------------------------------------------------------------\\n\\nCONTRASTIVE_PROMPT = '''\\\\\\nYou are a formal logic expert. Given a logic problem and a candidate answer, \\\\\\ngenerate logical constraints that must hold if the answer is CORRECT (pro) \\\\\\nand constraints that must hold if the answer is WRONG (con).\\n\\nProblem:\\n{problem_text}\\n\\nCandidate answer: {candidate_answer}\\n\\nInstructions:\\n1. List FOL constraints that SUPPORT this answer being correct (pro_constraints).\\n2. List FOL constraints that would hold if this answer is WRONG (con_constraints).\\n3. Express each constraint as a Z3-compatible boolean formula.\\n\\nVariable naming:\\n- Unary property: property_entity (e.g., kind_anne, red_charlie)\\n- Binary relation: relation_subject_object (e.g., eats_bear_squirrel)\\n- Use lowercase with underscores only\\n\\nZ3 operators: Implies(a, b), And(a, b, ...), Or(a, b, ...), Not(a), == True, == False\\n\\nOutput ONLY valid JSON:\\n{{\\\"pro_constraints\\\": [{{\\\"expression\\\": \\\"human-readable\\\", \\\"z3_formula\\\": \\\"Z3 syntax\\\"}}], \\\\\\n\\\"con_constraints\\\": [{{\\\"expression\\\": \\\"human-readable\\\", \\\"z3_formula\\\": \\\"Z3 syntax\\\"}}]}}'''\\n\\n# ---------------------------------------------------------------------------\\n# Contrastive constraint generator\\n# ---------------------------------------------------------------------------\\n\\ndef _strip_thinking(text: str) -> str:\\n    return re.sub(r'&lt;think>.*?&lt;/think>', '', text, flags=re.DOTALL).strip()\\n\\n\\ndef _extract_json_str(text: str) -> str | None:\\n    # Try to find JSON object\\n    for m in re.finditer(r'\\\\{[\\\\s\\\\S]*\\\\}', text):\\n        candidate = m.group()\\n        try:\\n            json.loads(candidate)\\n            return candidate\\n        except json.JSONDecodeError:\\n            continue\\n    return None\\n\\n\\ndef _repair_json(s: str) -> str:\\n    # Fix trailing commas before } or ]\\n    s = re.sub(r',\\\\s*([}\\\\]])', r'\\\\1', s)\\n    # Fix single quotes to double quotes\\n    s = s.replace(\\\"'\\\", '\\\"')\\n    return s\\n\\n\\ndef parse_contrastive_response(raw: str) -> tuple[list[dict], list[dict]]:\\n    \\\"\\\"\\\"Parse LLM response into (pro_constraints, con_constraints).\\n    Each constraint dict has 'expression' and 'z3_formula' keys.\\n    Returns empty lists on parse failure.\\n    \\\"\\\"\\\"\\n \\n\\n... [截断: 输出过长，省略 14789 字符] ...\\n\\nesults for size)\\n        result_entry = {\\n            \\\"problem_idx\\\": idx,\\n            \\\"problem_id\\\": prob_id,\\n            \\\"problem\\\": problem[\\\"problem\\\"],\\n            \\\"dataset\\\": \\\"folio\\\",\\n            \\\"ground_truth\\\": normalize_logic_answer(problem[\\\"answer\\\"]),\\n            \\\"contrastive_answer\\\": contrastive_answer,\\n            \\\"contrastive_correct\\\": contrastive_correct,\\n            \\\"sc_answer\\\": sc_answer,\\n            \\\"sc_correct\\\": sc_correct,\\n            \\\"candidates\\\": result.get(\\\"candidates\\\", []),\\n            \\\"answer_counts\\\": result.get(\\\"answer_counts\\\", {}),\\n            \\\"contrastive_scores\\\": result.get(\\\"contrastive_scores\\\", {}),\\n            \\\"pro_constraints_count\\\": result.get(\\\"pro_constraints_count\\\", 0),\\n            \\\"con_constraints_count\\\": result.get(\\\"con_constraints_count\\\", 0),\\n            \\\"per_candidate_details\\\": result.get(\\\"per_candidate_details\\\", {}),\\n            \\\"degenerate\\\": result.get(\\\"degenerate\\\", False),\\n            \\\"timing\\\": result.get(\\\"timing\\\", {}),\\n        }\\n        all_results.append(result_entry)\\n\\n        # Save intermediates (full constraints + traces per problem)\\n        if args.save_intermediates:\\n            intermed_dir = os.path.join(\\n                os.path.dirname(args.output) or \\\".\\\", \\\"intermediates\\\"\\n            )\\n            os.makedirs(intermed_dir, exist_ok=True)\\n            intermed_data = {\\n                \\\"problem\\\": problem,\\n                \\\"traces\\\": result.get(\\\"traces\\\", []),\\n                \\\"per_candidate_constraints\\\": result.get(\\\"per_candidate_constraints\\\", {}),\\n                \\\"contrastive_scores\\\": result.get(\\\"contrastive_scores\\\", {}),\\n                \\\"per_candidate_details\\\": result.get(\\\"per_candidate_details\\\", {}),\\n            }\\n            with open(os.path.join(intermed_dir, f\\\"{prob_id}.json\\\"), \\\"w\\\") as f:\\n                json.dump(intermed_data, f, indent=2, default=str)\\n\\n        # Checkpoint\\n        n = len(all_results)\\n        c_acc = sum(1 for r in all_results if r[\\\"contrastive_correct\\\"]) / n\\n        sc_acc = sum(1 for r in all_results if r[\\\"sc_correct\\\"]) / n\\n        summary = {\\n            \\\"n\\\": n,\\n            \\\"contrastive_accuracy\\\": round(c_acc, 4),\\n            \\\"sc_accuracy\\\": round(sc_acc, 4),\\n            \\\"delta\\\": round(c_acc - sc_acc, 4),\\n            \\\"k\\\": args.k,\\n            \\\"k_contrast\\\": args.k_contrast,\\n            \\\"temperature\\\": args.temperature,\\n            \\\"mode\\\": args.mode,\\n            \\\"seed\\\": args.seed,\\n            \\\"total_wall_time_s\\\": round(time.time() - total_start, 1),\\n            \\\"total_pro_constraints\\\": sum(\\n                r[\\\"pro_constraints_count\\\"] for r in all_results\\n            ),\\n            \\\"total_con_constraints\\\": sum(\\n                r[\\\"con_constraints_count\\\"] for r in all_results\\n            ),\\n            \\\"degenerate_count\\\": sum(1 for r in all_results if r.get(\\\"degenerate\\\")),\\n        }\\n        output = {\\\"summary\\\": summary, \\\"results\\\": all_results}\\n        with open(args.output, \\\"w\\\") as f:\\n            json.dump(output, f, indent=2, default=str)\\n\\n    # Final summary\\n    n = len(all_results)\\n    if n > 0:\\n        c_acc = sum(1 for r in all_results if r[\\\"contrastive_correct\\\"]) / n\\n        sc_acc = sum(1 for r in all_results if r[\\\"sc_correct\\\"]) / n\\n        total_wall = time.time() - total_start\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"FINAL RESULTS ({n} problems)\\\")\\n        print(f\\\"  Contrastive: {c_acc:.4f} ({sum(1 for r in all_results if r['contrastive_correct'])}/{n})\\\")\\n        print(f\\\"  SC baseline:  {sc_acc:.4f} ({sum(1 for r in all_results if r['sc_correct'])}/{n})\\\")\\n        print(f\\\"  Delta:        {c_acc - sc_acc:+.4f}\\\")\\n        print(f\\\"  Degenerate:   {sum(1 for r in all_results if r.get('degenerate'))}/{n}\\\")\\n        print(f\\\"  Pro total:    {sum(r['pro_constraints_count'] for r in all_results)}\\\")\\n        print(f\\\"  Con total:    {sum(r['con_constraints_count'] for r in all_results)}\\\")\\n        print(f\\\"  Wall time:    {total_wall/60:.1f} min\\\")\\n        print(f\\\"Results saved to {args.output}\\\")\\n\\n    print(\\\"CONTRASTIVE_PIPELINE_DONE\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.29}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "a58d2a0b-ad60-428d-9b0c-8f93e8b89103",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nContrastive Constraint Generation Pipeline for FOLIO.\\\\n\\\\nInstead of extracting constraints from same-source SC traces (which lack\\\\nindependence), this pipeline generates PRO and CON constraints for each\\\\ncandidate answer independently via targeted LLM prompts, then uses\\\\ncontrastive MAX-SAT scoring to select the best answer.\\\\n\\\\nThree phases:\\\\n  Phase 1 — SC voting: generate K traces, majority-vote to get candidate set\\\\n  Phase 2 — Contrastive constraint generation: for each candidate, prompt the\\\\n            LLM K_contrast times to produce supporting (pro) and refuting (con)\\\\n            FOL constraints\\\\n  Phase 3 — Contrastive MAX-SAT scoring: score = MAX-SAT(pro) - α·MAX-SAT(con)\\\\n\\\\nUsage:\\\\n  python run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 \\\\\\\\\\\\n    --api-base http://localhost:8000/v1 --model auto \\\\\\\\\\\\n    --data data/folio_full.json \\\\\\\\\\\\n    --output results/exp075_contrastive/results.json \\\\\\\\\\\\n    --save-intermediates\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport re\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter\\\\n\\\\nfrom sica.trace_generator import VLLMGenerator, MockGenerator, extract_boxed_answer\\\\nfrom sica.constraint_extractor import VLLMBackend, MockLLM, ConstraintExtractor\\\\nfrom sica.z3_maxsat import (\\\\n    ConstraintDeduplicator, MaxSATSolver, parse_z3_formula, UniqueConstraint,\\\\n)\\\\nfrom sica.pipeline import normalize_logic_answer, _group_logic_answers\\\\nfrom baselines.self_consistency import SelfConsistency\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s %(levelname)s %(message)s\\\\\\\",\\\\n    handlers=[logging.StreamHandler(sys.stdout)],\\\\n)\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n# ---------------------------------------------------------------------------\\\\n# Contrastive constraint generation prompt\\\\n# ---------------------------------------------------------------------------\\\\n\\\\nCONTRASTIVE_PROMPT = '''\\\\\\\\\\\\nYou are a formal logic expert. Given a logic problem and a candidate answer, \\\\\\\\\\\\ngenerate logical constraints that must hold if the answer is CORRECT (pro) \\\\\\\\\\\\nand constraints that must hold if the answer is WRONG (con).\\\\n\\\\nProblem:\\\\n{problem_text}\\\\n\\\\nCandidate answer: {candidate_answer}\\\\n\\\\nInstructions:\\\\n1. List FOL constraints that SUPPORT this answer being correct (pro_constraints).\\\\n2. List FOL constraints that would hold if this answer is WRONG (con_constraints).\\\\n3. Express each constraint as a Z3-compatible boolean formula.\\\\n\\\\nVariable naming:\\\\n- Unary property: property_entity (e.g., kind_anne, red_charlie)\\\\n- Binary relation: relation_subject_object (e.g., eats_bear_squirrel)\\\\n- Use lowercase with underscores only\\\\n\\\\nZ3 operators: Implies(a, b), And(a, b, ...), Or(a, b, ...), Not(a), == True, == False\\\\n\\\\nOutput ONLY valid JSON:\\\\n{{\\\\\\\"pro_constraints\\\\\\\": [{{\\\\\\\"expression\\\\\\\": \\\\\\\"human-readable\\\\\\\", \\\\\\\"z3_formula\\\\\\\": \\\\\\\"Z3 syntax\\\\\\\"}}], \\\\\\\\\\\\n\\\\\\\"con_constraints\\\\\\\": [{{\\\\\\\"expression\\\\\\\": \\\\\\\"human-readable\\\\\\\", \\\\\\\"z3_formula\\\\\\\": \\\\\\\"Z3 syntax\\\\\\\"}}]}}'''\\\\n\\\\n# ---------------------------------------------------------------------------\\\\n# Contrastive constraint generator\\\\n# ---------------------------------------------------------------------------\\\\n\\\\ndef _strip_thinking(text: str) -> str:\\\\n    return re.sub(r'&lt;think>.*?&lt;/think>', '', text, flags=re.DOTALL).strip()\\\\n\\\\n\\\\ndef _extract_json_str(text: str) -> str | None:\\\\n    # Try to find JSON object\\\\n    for m in re.finditer(r'\\\\\\\\{[\\\\\\\\s\\\\\\\\S]*\\\\\\\\}', text):\\\\n        candidate = m.group()\\\\n        try:\\\\n            json.loads(candidate)\\\\n            return candidate\\\\n        except json.JSONDecodeError:\\\\n            continue\\\\n    return None\\\\n\\\\n\\\\ndef _repair_json(s: str) -> str:\\\\n    # Fix trailing commas before } or ]\\\\n    s = re.sub(r',\\\\\\\\s*([}\\\\\\\\]])', r'\\\\\\\\1', s)\\\\n    # Fix single quotes to double quotes\\\\n    s = s.replace(\\\\\\\"'\\\\\\\", '\\\\\\\"')\\\\n    return s\\\\n\\\\n\\\\ndef parse_contrastive_response(raw: str) -> tuple[list[dict], list[dict]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Parse LLM response into (pro_constraints, con_constraints).\\\\n    Each constraint dict has 'expression' and 'z3_formula' keys.\\\\n    Returns empty lists on parse failure.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n \\\\n\\\\n... [截断: 输出过长，省略 14789 字符] ...\\\\n\\\\nesults for size)\\\\n        result_entry = {\\\\n            \\\\\\\"problem_idx\\\\\\\": idx,\\\\n            \\\\\\\"problem_id\\\\\\\": prob_id,\\\\n            \\\\\\\"problem\\\\\\\": problem[\\\\\\\"problem\\\\\\\"],\\\\n            \\\\\\\"dataset\\\\\\\": \\\\\\\"folio\\\\\\\",\\\\n            \\\\\\\"ground_truth\\\\\\\": normalize_logic_answer(problem[\\\\\\\"answer\\\\\\\"]),\\\\n            \\\\\\\"contrastive_answer\\\\\\\": contrastive_answer,\\\\n            \\\\\\\"contrastive_correct\\\\\\\": contrastive_correct,\\\\n            \\\\\\\"sc_answer\\\\\\\": sc_answer,\\\\n            \\\\\\\"sc_correct\\\\\\\": sc_correct,\\\\n            \\\\\\\"candidates\\\\\\\": result.get(\\\\\\\"candidates\\\\\\\", []),\\\\n            \\\\\\\"answer_counts\\\\\\\": result.get(\\\\\\\"answer_counts\\\\\\\", {}),\\\\n            \\\\\\\"contrastive_scores\\\\\\\": result.get(\\\\\\\"contrastive_scores\\\\\\\", {}),\\\\n            \\\\\\\"pro_constraints_count\\\\\\\": result.get(\\\\\\\"pro_constraints_count\\\\\\\", 0),\\\\n            \\\\\\\"con_constraints_count\\\\\\\": result.get(\\\\\\\"con_constraints_count\\\\\\\", 0),\\\\n            \\\\\\\"per_candidate_details\\\\\\\": result.get(\\\\\\\"per_candidate_details\\\\\\\", {}),\\\\n            \\\\\\\"degenerate\\\\\\\": result.get(\\\\\\\"degenerate\\\\\\\", False),\\\\n            \\\\\\\"timing\\\\\\\": result.get(\\\\\\\"timing\\\\\\\", {}),\\\\n        }\\\\n        all_results.append(result_entry)\\\\n\\\\n        # Save intermediates (full constraints + traces per problem)\\\\n        if args.save_intermediates:\\\\n            intermed_dir = os.path.join(\\\\n                os.path.dirname(args.output) or \\\\\\\".\\\\\\\", \\\\\\\"intermediates\\\\\\\"\\\\n            )\\\\n            os.makedirs(intermed_dir, exist_ok=True)\\\\n            intermed_data = {\\\\n                \\\\\\\"problem\\\\\\\": problem,\\\\n                \\\\\\\"traces\\\\\\\": result.get(\\\\\\\"traces\\\\\\\", []),\\\\n                \\\\\\\"per_candidate_constraints\\\\\\\": result.get(\\\\\\\"per_candidate_constraints\\\\\\\", {}),\\\\n                \\\\\\\"contrastive_scores\\\\\\\": result.get(\\\\\\\"contrastive_scores\\\\\\\", {}),\\\\n                \\\\\\\"per_candidate_details\\\\\\\": result.get(\\\\\\\"per_candidate_details\\\\\\\", {}),\\\\n            }\\\\n            with open(os.path.join(intermed_dir, f\\\\\\\"{prob_id}.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n                json.dump(intermed_data, f, indent=2, default=str)\\\\n\\\\n        # Checkpoint\\\\n        n = len(all_results)\\\\n        c_acc = sum(1 for r in all_results if r[\\\\\\\"contrastive_correct\\\\\\\"]) / n\\\\n        sc_acc = sum(1 for r in all_results if r[\\\\\\\"sc_correct\\\\\\\"]) / n\\\\n        summary = {\\\\n            \\\\\\\"n\\\\\\\": n,\\\\n            \\\\\\\"contrastive_accuracy\\\\\\\": round(c_acc, 4),\\\\n            \\\\\\\"sc_accuracy\\\\\\\": round(sc_acc, 4),\\\\n            \\\\\\\"delta\\\\\\\": round(c_acc - sc_acc, 4),\\\\n            \\\\\\\"k\\\\\\\": args.k,\\\\n            \\\\\\\"k_contrast\\\\\\\": args.k_contrast,\\\\n            \\\\\\\"temperature\\\\\\\": args.temperature,\\\\n            \\\\\\\"mode\\\\\\\": args.mode,\\\\n            \\\\\\\"seed\\\\\\\": args.seed,\\\\n            \\\\\\\"total_wall_time_s\\\\\\\": round(time.time() - total_start, 1),\\\\n            \\\\\\\"total_pro_constraints\\\\\\\": sum(\\\\n                r[\\\\\\\"pro_constraints_count\\\\\\\"] for r in all_results\\\\n            ),\\\\n            \\\\\\\"total_con_constraints\\\\\\\": sum(\\\\n                r[\\\\\\\"con_constraints_count\\\\\\\"] for r in all_results\\\\n            ),\\\\n            \\\\\\\"degenerate_count\\\\\\\": sum(1 for r in all_results if r.get(\\\\\\\"degenerate\\\\\\\")),\\\\n        }\\\\n        output = {\\\\\\\"summary\\\\\\\": summary, \\\\\\\"results\\\\\\\": all_results}\\\\n        with open(args.output, \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(output, f, indent=2, default=str)\\\\n\\\\n    # Final summary\\\\n    n = len(all_results)\\\\n    if n > 0:\\\\n        c_acc = sum(1 for r in all_results if r[\\\\\\\"contrastive_correct\\\\\\\"]) / n\\\\n        sc_acc = sum(1 for r in all_results if r[\\\\\\\"sc_correct\\\\\\\"]) / n\\\\n        total_wall = time.time() - total_start\\\\n        print(f\\\\\\\"\\\\\\\\n{'='*60}\\\\\\\")\\\\n        print(f\\\\\\\"FINAL RESULTS ({n} problems)\\\\\\\")\\\\n        print(f\\\\\\\"  Contrastive: {c_acc:.4f} ({sum(1 for r in all_results if r['contrastive_correct'])}/{n})\\\\\\\")\\\\n        print(f\\\\\\\"  SC baseline:  {sc_acc:.4f} ({sum(1 for r in all_results if r['sc_correct'])}/{n})\\\\\\\")\\\\n        print(f\\\\\\\"  Delta:        {c_acc - sc_acc:+.4f}\\\\\\\")\\\\n        print(f\\\\\\\"  Degenerate:   {sum(1 for r in all_results if r.get('degenerate'))}/{n}\\\\\\\")\\\\n        print(f\\\\\\\"  Pro total:    {sum(r['pro_constraints_count'] for r in all_results)}\\\\\\\")\\\\n        print(f\\\\\\\"  Con total:    {sum(r['con_constraints_count'] for r in all_results)}\\\\\\\")\\\\n        print(f\\\\\\\"  Wall time:    {total_wall/60:.1f} min\\\\\\\")\\\\n        print(f\\\\\\\"Results saved to {args.output}\\\\\\\")\\\\n\\\\n    print(\\\\\\\"CONTRASTIVE_PIPELINE_DONE\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.29}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nContrastive Constraint Generation Pipeline for FOLIO.\\n\\nInstead of extracting constraints from same-source SC traces (which lack\\nindependence), this pipeline generates PRO and CON constraints for each\\ncandidate answer independently via targeted LLM prompts, then uses\\ncontrastive MAX-SAT scoring to select the best answer.\\n\\nThree phases:\\n  Phase 1 — SC voting: generate K traces, majority-vote to get candidate set\\n  Phase 2 — Contrastive constraint generation: for each candidate, prompt the\\n            LLM K_contrast times to produce supporting (pro) and refuting (con)\\n            FOL constraints\\n  Phase 3 — Contrastive MAX-SAT scoring: score = MAX-SAT(pro) - α·MAX-SAT(con)\\n\\nUsage:\\n  python run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 \\\\\\n    --api-base http://localhost:8000/v1 --model auto \\\\\\n    --data data/folio_full.json \\\\\\n    --output results/exp075_contrastive/results.json \\\\\\n    --save-intermediates\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom collections import Counter\\n\\nfrom sica.trace_generator import VLLMGenerator, MockGenerator, extract_boxed_answer\\nfrom sica.constraint_extractor import VLLMBackend, MockLLM, ConstraintExtractor\\nfrom sica.z3_maxsat import (\\n    ConstraintDeduplicator, MaxSATSolver, parse_z3_formula, UniqueConstraint,\\n)\\nfrom sica.pipeline import normalize_logic_answer, _group_logic_answers\\nfrom baselines.self_consistency import SelfConsistency\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s %(levelname)s %(message)s\\\",\\n    handlers=[logging.StreamHandler(sys.stdout)],\\n)\\nlogger = logging.getLogger(__name__)\\n\\n# ---------------------------------------------------------------------------\\n# Contrastive constraint generation prompt\\n# ---------------------------------------------------------------------------\\n\\nCONTRASTIVE_PROMPT = '''\\\\\\nYou are a formal logic expert. Given a logic problem and a candidate answer, \\\\\\ngenerate logical constraints that must hold if the answer is CORRECT (pro) \\\\\\nand constraints that must hold if the answer is WRONG (con).\\n\\nProblem:\\n{problem_text}\\n\\nCandidate answer: {candidate_answer}\\n\\nInstructions:\\n1. List FOL constraints that SUPPORT this answer being correct (pro_constraints).\\n2. List FOL constraints that would hold if this answer is WRONG (con_constraints).\\n3. Express each constraint as a Z3-compatible boolean formula.\\n\\nVariable naming:\\n- Unary property: property_entity (e.g., kind_anne, red_charlie)\\n- Binary relation: relation_subject_object (e.g., eats_bear_squirrel)\\n- Use lowercase with underscores only\\n\\nZ3 operators: Implies(a, b), And(a, b, ...), Or(a, b, ...), Not(a), == True, == False\\n\\nOutput ONLY valid JSON:\\n{{\\\"pro_constraints\\\": [{{\\\"expression\\\": \\\"human-readable\\\", \\\"z3_formula\\\": \\\"Z3 syntax\\\"}}], \\\\\\n\\\"con_constraints\\\": [{{\\\"expression\\\": \\\"human-readable\\\", \\\"z3_formula\\\": \\\"Z3 syntax\\\"}}]}}'''\\n\\n# ---------------------------------------------------------------------------\\n# Contrastive constraint generator\\n# ---------------------------------------------------------------------------\\n\\ndef _strip_thinking(text: str) -> str:\\n    return re.sub(r'&lt;think>.*?&lt;/think>', '', text, flags=re.DOTALL).strip()\\n\\n\\ndef _extract_json_str(text: str) -> str | None:\\n    # Try to find JSON object\\n    for m in re.finditer(r'\\\\{[\\\\s\\\\S]*\\\\}', text):\\n        candidate = m.group()\\n        try:\\n            json.loads(candidate)\\n            return candidate\\n        except json.JSONDecodeError:\\n            continue\\n    return None\\n\\n\\ndef _repair_json(s: str) -> str:\\n    # Fix trailing commas before } or ]\\n    s = re.sub(r',\\\\s*([}\\\\]])', r'\\\\1', s)\\n    # Fix single quotes to double quotes\\n    s = s.replace(\\\"'\\\", '\\\"')\\n    return s\\n\\n\\ndef parse_contrastive_response(raw: str) -> tuple[list[dict], list[dict]]:\\n    \\\"\\\"\\\"Parse LLM response into (pro_constraints, con_constraints).\\n    Each constraint dict has 'expression' and 'z3_formula' keys.\\n    Returns empty lists on parse failure.\\n    \\\"\\\"\\\"\\n \\n\\n... [截断: 输出过长，省略 14789 字符] ...\\n\\nesults for size)\\n        result_entry = {\\n            \\\"problem_idx\\\": idx,\\n            \\\"problem_id\\\": prob_id,\\n            \\\"problem\\\": problem[\\\"problem\\\"],\\n            \\\"dataset\\\": \\\"folio\\\",\\n            \\\"ground_truth\\\": normalize_logic_answer(problem[\\\"answer\\\"]),\\n            \\\"contrastive_answer\\\": contrastive_answer,\\n            \\\"contrastive_correct\\\": contrastive_correct,\\n            \\\"sc_answer\\\": sc_answer,\\n            \\\"sc_correct\\\": sc_correct,\\n            \\\"candidates\\\": result.get(\\\"candidates\\\", []),\\n            \\\"answer_counts\\\": result.get(\\\"answer_counts\\\", {}),\\n            \\\"contrastive_scores\\\": result.get(\\\"contrastive_scores\\\", {}),\\n            \\\"pro_constraints_count\\\": result.get(\\\"pro_constraints_count\\\", 0),\\n            \\\"con_constraints_count\\\": result.get(\\\"con_constraints_count\\\", 0),\\n            \\\"per_candidate_details\\\": result.get(\\\"per_candidate_details\\\", {}),\\n            \\\"degenerate\\\": result.get(\\\"degenerate\\\", False),\\n            \\\"timing\\\": result.get(\\\"timing\\\", {}),\\n        }\\n        all_results.append(result_entry)\\n\\n        # Save intermediates (full constraints + traces per problem)\\n        if args.save_intermediates:\\n            intermed_dir = os.path.join(\\n                os.path.dirname(args.output) or \\\".\\\", \\\"intermediates\\\"\\n            )\\n            os.makedirs(intermed_dir, exist_ok=True)\\n            intermed_data = {\\n                \\\"problem\\\": problem,\\n                \\\"traces\\\": result.get(\\\"traces\\\", []),\\n                \\\"per_candidate_constraints\\\": result.get(\\\"per_candidate_constraints\\\", {}),\\n                \\\"contrastive_scores\\\": result.get(\\\"contrastive_scores\\\", {}),\\n                \\\"per_candidate_details\\\": result.get(\\\"per_candidate_details\\\", {}),\\n            }\\n            with open(os.path.join(intermed_dir, f\\\"{prob_id}.json\\\"), \\\"w\\\") as f:\\n                json.dump(intermed_data, f, indent=2, default=str)\\n\\n        # Checkpoint\\n        n = len(all_results)\\n        c_acc = sum(1 for r in all_results if r[\\\"contrastive_correct\\\"]) / n\\n        sc_acc = sum(1 for r in all_results if r[\\\"sc_correct\\\"]) / n\\n        summary = {\\n            \\\"n\\\": n,\\n            \\\"contrastive_accuracy\\\": round(c_acc, 4),\\n            \\\"sc_accuracy\\\": round(sc_acc, 4),\\n            \\\"delta\\\": round(c_acc - sc_acc, 4),\\n            \\\"k\\\": args.k,\\n            \\\"k_contrast\\\": args.k_contrast,\\n            \\\"temperature\\\": args.temperature,\\n            \\\"mode\\\": args.mode,\\n            \\\"seed\\\": args.seed,\\n            \\\"total_wall_time_s\\\": round(time.time() - total_start, 1),\\n            \\\"total_pro_constraints\\\": sum(\\n                r[\\\"pro_constraints_count\\\"] for r in all_results\\n            ),\\n            \\\"total_con_constraints\\\": sum(\\n                r[\\\"con_constraints_count\\\"] for r in all_results\\n            ),\\n            \\\"degenerate_count\\\": sum(1 for r in all_results if r.get(\\\"degenerate\\\")),\\n        }\\n        output = {\\\"summary\\\": summary, \\\"results\\\": all_results}\\n        with open(args.output, \\\"w\\\") as f:\\n            json.dump(output, f, indent=2, default=str)\\n\\n    # Final summary\\n    n = len(all_results)\\n    if n > 0:\\n        c_acc = sum(1 for r in all_results if r[\\\"contrastive_correct\\\"]) / n\\n        sc_acc = sum(1 for r in all_results if r[\\\"sc_correct\\\"]) / n\\n        total_wall = time.time() - total_start\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"FINAL RESULTS ({n} problems)\\\")\\n        print(f\\\"  Contrastive: {c_acc:.4f} ({sum(1 for r in all_results if r['contrastive_correct'])}/{n})\\\")\\n        print(f\\\"  SC baseline:  {sc_acc:.4f} ({sum(1 for r in all_results if r['sc_correct'])}/{n})\\\")\\n        print(f\\\"  Delta:        {c_acc - sc_acc:+.4f}\\\")\\n        print(f\\\"  Degenerate:   {sum(1 for r in all_results if r.get('degenerate'))}/{n}\\\")\\n        print(f\\\"  Pro total:    {sum(r['pro_constraints_count'] for r in all_results)}\\\")\\n        print(f\\\"  Con total:    {sum(r['con_constraints_count'] for r in all_results)}\\\")\\n        print(f\\\"  Wall time:    {total_wall/60:.1f} min\\\")\\n        print(f\\\"Results saved to {args.output}\\\")\\n\\n    print(\\\"CONTRASTIVE_PIPELINE_DONE\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.29}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
The output was truncated. I need to see the critical parts - around line 212 (normalization) and line 379 (KeyError). Let me also find the process to kill. Let me use grep to find the specific functions and the key references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "db2e0554-db2e-4f1d-9b91-2ee4876b67e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVogU2W5szog7Cm5eWY6q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6029,
      "cache_read_input_tokens": 24435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6029
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 14_

输出被截断了。需要看关键代码段。先找进程，同时读取关键行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "151544a9-7e64-44d8-ae35-7070413f3d53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVogU2W5szog7Cm5eWY6q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6029,
      "cache_read_input_tokens": 24435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6029
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_019dtQ6ehkyYB9FmTphUbkLx`</summary>

```json
{
  "server": "westd-25068",
  "command": "ps aux | grep run_contrastive | grep -v grep"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "b95c9c01-6a72-4355-87b8-5044a52ae148",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVogU2W5szog7Cm5eWY6q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6029,
      "cache_read_input_tokens": 24435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6029
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T17:40:46.082Z_

<details><summary>↩ Tool result · `toolu_019dtQ6ehkyYB9FmTphUbkLx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"root     257721  0.0  0.0   4364  3168 pts/1    Ss+  01:31   0:00 bash -c cd /root/symb_invariant_consensus && python -u run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 --api-base http://localhost:8002/v1 --model auto --data data/folio_full.json --output results/exp075_contrastive_mistral_folio/results.json --save-intermediates 2>&1 | tee results/exp075_contrastive_mistral_folio/run.log\\nroot     257723  0.2  0.0 724840 140620 pts/1   Sl+  01:31   0:01 python -u run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 --api-base http://localhost:8002/v1 --model auto --data data/folio_full.json --output results/exp075_contrastive_mistral_folio/results.json --save-intermediates\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "b5bfc53b-6be4-4975-a643-39f4c767dc8f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"root     257721  0.0  0.0   4364  3168 pts/1    Ss+  01:31   0:00 bash -c cd /root/symb_invariant_consensus && python -u run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 --api-base http://localhost:8002/v1 --model auto --data data/folio_full.json --output results/exp075_contrastive_mistral_folio/results.json --save-intermediates 2>&1 | tee results/exp075_contrastive_mistral_folio/run.log\\\\nroot     257723  0.2  0.0 724840 140620 pts/1   Sl+  01:31   0:01 python -u run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 --api-base http://localhost:8002/v1 --model auto --data data/folio_full.json --output results/exp075_contrastive_mistral_folio/results.json --save-intermediates\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"root     257721  0.0  0.0   4364  3168 pts/1    Ss+  01:31   0:00 bash -c cd /root/symb_invariant_consensus && python -u run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 --api-base http://localhost:8002/v1 --model auto --data data/folio_full.json --output results/exp075_contrastive_mistral_folio/results.json --save-intermediates 2>&1 | tee results/exp075_contrastive_mistral_folio/run.log\\nroot     257723  0.2  0.0 724840 140620 pts/1   Sl+  01:31   0:01 python -u run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 --api-base http://localhost:8002/v1 --model auto --data data/folio_full.json --output results/exp075_contrastive_mistral_folio/results.json --save-intermediates\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HptBptu3f9WHh1azhER8RP`</summary>

```json
{
  "server": "westd-25068",
  "command": "head -250 /root/symb_invariant_consensus/run_contrastive.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "755507e7-494e-4c92-bcfe-e20675a6c013",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVogU2W5szog7Cm5eWY6q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6029,
      "cache_read_input_tokens": 24435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6029
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DzKfajNGPpV3zgwMiuLhpb`</summary>

```json
{
  "server": "westd-25068",
  "command": "tail -n +250 /root/symb_invariant_consensus/run_contrastive.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "be02c774-c36b-4efe-b02d-86f7ce97f66f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVogU2W5szog7Cm5eWY6q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6029,
      "cache_read_input_tokens": 24435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6029
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T17:40:47.078Z_

<details><summary>↩ Tool result · `toolu_01HptBptu3f9WHh1azhER8RP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nContrastive Constraint Generation Pipeline for FOLIO.\\n\\nInstead of extracting constraints from same-source SC traces (which lack\\nindependence), this pipeline generates PRO and CON constraints for each\\ncandidate answer independently via targeted LLM prompts, then uses\\ncontrastive MAX-SAT scoring to select the best answer.\\n\\nThree phases:\\n  Phase 1 — SC voting: generate K traces, majority-vote to get candidate set\\n  Phase 2 — Contrastive constraint generation: for each candidate, prompt the\\n            LLM K_contrast times to produce supporting (pro) and refuting (con)\\n            FOL constraints\\n  Phase 3 — Contrastive MAX-SAT scoring: score = MAX-SAT(pro) - α·MAX-SAT(con)\\n\\nUsage:\\n  python run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 \\\\\\n    --api-base http://localhost:8000/v1 --model auto \\\\\\n    --data data/folio_full.json \\\\\\n    --output results/exp075_contrastive/results.json \\\\\\n    --save-intermediates\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom collections import Counter\\n\\nfrom sica.trace_generator import VLLMGenerator, MockGenerator, extract_boxed_answer\\nfrom sica.constraint_extractor import VLLMBackend, MockLLM, ConstraintExtractor\\nfrom sica.z3_maxsat import (\\n    ConstraintDeduplicator, MaxSATSolver, parse_z3_formula, UniqueConstraint,\\n)\\nfrom sica.pipeline import normalize_logic_answer, _group_logic_answers\\nfrom baselines.self_consistency import SelfConsistency\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s %(levelname)s %(message)s\\\",\\n    handlers=[logging.StreamHandler(sys.stdout)],\\n)\\nlogger = logging.getLogger(__name__)\\n\\n# ---------------------------------------------------------------------------\\n# Contrastive constraint generation prompt\\n# ---------------------------------------------------------------------------\\n\\nCONTRASTIVE_PROMPT = '''\\\\\\nYou are a formal logic expert. Given a logic problem and a candidate answer, \\\\\\ngenerate logical constraints that must hold if the answer is CORRECT (pro) \\\\\\nand constraints that must hold if the answer is WRONG (con).\\n\\nProblem:\\n{problem_text}\\n\\nCandidate answer: {candidate_answer}\\n\\nInstructions:\\n1. List FOL constraints that SUPPORT this answer being correct (pro_constraints).\\n2. List FOL constraints that would hold if this answer is WRONG (con_constraints).\\n3. Express each constraint as a Z3-compatible boolean formula.\\n\\nVariable naming:\\n- Unary property: property_entity (e.g., kind_anne, red_charlie)\\n- Binary relation: relation_subject_object (e.g., eats_bear_squirrel)\\n- Use lowercase with underscores only\\n\\nZ3 operators: Implies(a, b), And(a, b, ...), Or(a, b, ...), Not(a), == True, == False\\n\\nOutput ONLY valid JSON:\\n{{\\\"pro_constraints\\\": [{{\\\"expression\\\": \\\"human-readable\\\", \\\"z3_formula\\\": \\\"Z3 syntax\\\"}}], \\\\\\n\\\"con_constraints\\\": [{{\\\"expression\\\": \\\"human-readable\\\", \\\"z3_formula\\\": \\\"Z3 syntax\\\"}}]}}'''\\n\\n# ---------------------------------------------------------------------------\\n# Contrastive constraint generator\\n# ---------------------------------------------------------------------------\\n\\ndef _strip_thinking(text: str) -> str:\\n    return re.sub(r'&lt;think>.*?&lt;/think>', '', text, flags=re.DOTALL).strip()\\n\\n\\ndef _extract_json_str(text: str) -> str | None:\\n    # Try to find JSON object\\n    for m in re.finditer(r'\\\\{[\\\\s\\\\S]*\\\\}', text):\\n        candidate = m.group()\\n        try:\\n            json.loads(candidate)\\n            return candidate\\n        except json.JSONDecodeError:\\n            continue\\n    return None\\n\\n\\ndef _repair_json(s: str) -> str:\\n    # Fix trailing commas before } or ]\\n    s = re.sub(r',\\\\s*([}\\\\]])', r'\\\\1', s)\\n    # Fix single quotes to double quotes\\n    s = s.replace(\\\"'\\\", '\\\"')\\n    return s\\n\\n\\ndef parse_contrastive_response(raw: str) -> tuple[list[dict], list[dict]]:\\n    \\\"\\\"\\\"Parse LLM response into (pro_constraints, con_constraints).\\n    Each constraint dict has 'expression' and 'z3_formula' keys.\\n    Returns empty lists on parse failure.\\n    \\\"\\\"\\\"\\n \\n\\n... [截断: 输出过长，省略 439 字符] ...\\n\\nw = data.get(\\\"con_constraints\\\", [])\\n\\n    def _validate(constraints: list) -> list[dict]:\\n        valid = []\\n        for c in constraints:\\n            if not isinstance(c, dict):\\n                continue\\n            z3f = c.get(\\\"z3_formula\\\", \\\"\\\")\\n            if not z3f:\\n                continue\\n            # Verify parseable by z3\\n            parsed = parse_z3_formula(z3f)\\n            if parsed is None:\\n                continue\\n            valid.append({\\n                \\\"expression\\\": c.get(\\\"expression\\\", z3f),\\n                \\\"z3_formula\\\": z3f,\\n            })\\n        return valid\\n\\n    return _validate(pro_raw), _validate(con_raw)\\n\\n\\ndef generate_contrastive_constraints(\\n    llm, problem_text: str, candidate: str, k_contrast: int = 3,\\n) -> tuple[list[dict], list[dict]]:\\n    \\\"\\\"\\\"Call LLM k_contrast times for a candidate, aggregate pro/con constraints.\\\"\\\"\\\"\\n    all_pro, all_con = [], []\\n    prompt = CONTRASTIVE_PROMPT.format(\\n        problem_text=problem_text,\\n        candidate_answer=candidate,\\n    )\\n    for _ in range(k_contrast):\\n        raw = llm.call(prompt)\\n        pro, con = parse_contrastive_response(raw)\\n        all_pro.extend(pro)\\n        all_con.extend(con)\\n    return all_pro, all_con\\n\\n\\n# ---------------------------------------------------------------------------\\n# Contrastive MAX-SAT scoring\\n# ---------------------------------------------------------------------------\\n\\ndef _build_unique_constraints(constraints: list[dict]) -> list[UniqueConstraint]:\\n    \\\"\\\"\\\"Convert raw constraint dicts to UniqueConstraint list via deduplication.\\\"\\\"\\\"\\n    dedup = ConstraintDeduplicator()\\n    # Wrap as single-trace batch for the deduplicator\\n    return dedup.deduplicate([constraints])\\n\\n\\ndef contrastive_score_candidate(\\n    pro_constraints: list[dict],\\n    con_constraints: list[dict],\\n    solver: MaxSATSolver,\\n    maxsat_timeout_ms: int = 10000,\\n) -> dict:\\n    \\\"\\\"\\\"Score a single candidate: score = MAX-SAT(pro) - MAX-SAT(con).\\n\\n    Returns dict with score, pro_satisfied, con_satisfied, and details.\\n    \\\"\\\"\\\"\\n    # Deduplicate and solve pro constraints\\n    pro_unique = _build_unique_constraints(pro_constraints)\\n    if pro_unique:\\n        pro_result = solver.solve(pro_unique, timeout_ms=maxsat_timeout_ms)\\n        pro_sat_weight = pro_result.total_weight\\n        pro_n_sat = len(pro_result.satisfied)\\n    else:\\n        pro_sat_weight = 0.0\\n        pro_n_sat = 0\\n\\n    # Deduplicate and solve con constraints\\n    con_unique = _build_unique_constraints(con_constraints)\\n    if con_unique:\\n        con_result = solver.solve(con_unique, timeout_ms=maxsat_timeout_ms)\\n        con_sat_weight = con_result.total_weight\\n        con_n_sat = len(con_result.satisfied)\\n    else:\\n        con_sat_weight = 0.0\\n        con_n_sat = 0\\n\\n    n_pro = len(pro_unique)\\n    n_con = len(con_unique)\\n    raw_score = pro_sat_weight - con_sat_weight\\n    norm_pro = pro_sat_weight / max(n_pro, 1)\\n    norm_con = con_sat_weight / max(n_con, 1)\\n    score = norm_pro - norm_con\\n\\n    return {\\n        \\\"score\\\": score,\\n        \\\"raw_score\\\": raw_score,\\n        \\\"normalized_pro\\\": norm_pro,\\n        \\\"normalized_con\\\": norm_con,\\n        \\\"pro_satisfied_weight\\\": pro_sat_weight,\\n        \\\"con_satisfied_weight\\\": con_sat_weight,\\n        \\\"pro_n_satisfied\\\": pro_n_sat,\\n        \\\"con_n_satisfied\\\": con_n_sat,\\n        \\\"n_pro\\\": n_pro,\\n        \\\"n_con\\\": n_con,\\n        \\\"pro_n_raw\\\": len(pro_constraints),\\n        \\\"con_n_raw\\\": len(con_constraints),\\n    }\\n\\n\\n# ---------------------------------------------------------------------------\\n# Pipeline\\n# ---------------------------------------------------------------------------\\n\\ndef build_generator(args):\\n    if args.mode == \\\"mock\\\":\\n        gen = MockGenerator()\\n        gen.domain = \\\"math\\\"\\n        return gen\\n    elif args.mode == \\\"vllm\\\":\\n        gen = VLLMGenerator(\\n            base_url=args.api_base,\\n            api_key=[REDACTED],\\n            model=args.model if args.model != \\\"auto\\\" else None,\\n            temperature=args.temperature,\\n            max_tokens=args.max_tokens,\\n        )\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "e19e3aae-f1b8-48d6-84a9-60dfaa5e99d9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\nContrastive Constraint Generation Pipeline for FOLIO.\\\\n\\\\nInstead of extracting constraints from same-source SC traces (which lack\\\\nindependence), this pipeline generates PRO and CON constraints for each\\\\ncandidate answer independently via targeted LLM prompts, then uses\\\\ncontrastive MAX-SAT scoring to select the best answer.\\\\n\\\\nThree phases:\\\\n  Phase 1 — SC voting: generate K traces, majority-vote to get candidate set\\\\n  Phase 2 — Contrastive constraint generation: for each candidate, prompt the\\\\n            LLM K_contrast times to produce supporting (pro) and refuting (con)\\\\n            FOL constraints\\\\n  Phase 3 — Contrastive MAX-SAT scoring: score = MAX-SAT(pro) - α·MAX-SAT(con)\\\\n\\\\nUsage:\\\\n  python run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 \\\\\\\\\\\\n    --api-base http://localhost:8000/v1 --model auto \\\\\\\\\\\\n    --data data/folio_full.json \\\\\\\\\\\\n    --output results/exp075_contrastive/results.json \\\\\\\\\\\\n    --save-intermediates\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\nfrom __future__ import annotations\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport os\\\\nimport re\\\\nimport sys\\\\nimport time\\\\nfrom collections import Counter\\\\n\\\\nfrom sica.trace_generator import VLLMGenerator, MockGenerator, extract_boxed_answer\\\\nfrom sica.constraint_extractor import VLLMBackend, MockLLM, ConstraintExtractor\\\\nfrom sica.z3_maxsat import (\\\\n    ConstraintDeduplicator, MaxSATSolver, parse_z3_formula, UniqueConstraint,\\\\n)\\\\nfrom sica.pipeline import normalize_logic_answer, _group_logic_answers\\\\nfrom baselines.self_consistency import SelfConsistency\\\\n\\\\nlogging.basicConfig(\\\\n    level=logging.INFO,\\\\n    format=\\\\\\\"%(asctime)s %(levelname)s %(message)s\\\\\\\",\\\\n    handlers=[logging.StreamHandler(sys.stdout)],\\\\n)\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n# ---------------------------------------------------------------------------\\\\n# Contrastive constraint generation prompt\\\\n# ---------------------------------------------------------------------------\\\\n\\\\nCONTRASTIVE_PROMPT = '''\\\\\\\\\\\\nYou are a formal logic expert. Given a logic problem and a candidate answer, \\\\\\\\\\\\ngenerate logical constraints that must hold if the answer is CORRECT (pro) \\\\\\\\\\\\nand constraints that must hold if the answer is WRONG (con).\\\\n\\\\nProblem:\\\\n{problem_text}\\\\n\\\\nCandidate answer: {candidate_answer}\\\\n\\\\nInstructions:\\\\n1. List FOL constraints that SUPPORT this answer being correct (pro_constraints).\\\\n2. List FOL constraints that would hold if this answer is WRONG (con_constraints).\\\\n3. Express each constraint as a Z3-compatible boolean formula.\\\\n\\\\nVariable naming:\\\\n- Unary property: property_entity (e.g., kind_anne, red_charlie)\\\\n- Binary relation: relation_subject_object (e.g., eats_bear_squirrel)\\\\n- Use lowercase with underscores only\\\\n\\\\nZ3 operators: Implies(a, b), And(a, b, ...), Or(a, b, ...), Not(a), == True, == False\\\\n\\\\nOutput ONLY valid JSON:\\\\n{{\\\\\\\"pro_constraints\\\\\\\": [{{\\\\\\\"expression\\\\\\\": \\\\\\\"human-readable\\\\\\\", \\\\\\\"z3_formula\\\\\\\": \\\\\\\"Z3 syntax\\\\\\\"}}], \\\\\\\\\\\\n\\\\\\\"con_constraints\\\\\\\": [{{\\\\\\\"expression\\\\\\\": \\\\\\\"human-readable\\\\\\\", \\\\\\\"z3_formula\\\\\\\": \\\\\\\"Z3 syntax\\\\\\\"}}]}}'''\\\\n\\\\n# ---------------------------------------------------------------------------\\\\n# Contrastive constraint generator\\\\n# ---------------------------------------------------------------------------\\\\n\\\\ndef _strip_thinking(text: str) -> str:\\\\n    return re.sub(r'&lt;think>.*?&lt;/think>', '', text, flags=re.DOTALL).strip()\\\\n\\\\n\\\\ndef _extract_json_str(text: str) -> str | None:\\\\n    # Try to find JSON object\\\\n    for m in re.finditer(r'\\\\\\\\{[\\\\\\\\s\\\\\\\\S]*\\\\\\\\}', text):\\\\n        candidate = m.group()\\\\n        try:\\\\n            json.loads(candidate)\\\\n            return candidate\\\\n        except json.JSONDecodeError:\\\\n            continue\\\\n    return None\\\\n\\\\n\\\\ndef _repair_json(s: str) -> str:\\\\n    # Fix trailing commas before } or ]\\\\n    s = re.sub(r',\\\\\\\\s*([}\\\\\\\\]])', r'\\\\\\\\1', s)\\\\n    # Fix single quotes to double quotes\\\\n    s = s.replace(\\\\\\\"'\\\\\\\", '\\\\\\\"')\\\\n    return s\\\\n\\\\n\\\\ndef parse_contrastive_response(raw: str) -> tuple[list[dict], list[dict]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Parse LLM response into (pro_constraints, con_constraints).\\\\n    Each constraint dict has 'expression' and 'z3_formula' keys.\\\\n    Returns empty lists on parse failure.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n \\\\n\\\\n... [截断: 输出过长，省略 439 字符] ...\\\\n\\\\nw = data.get(\\\\\\\"con_constraints\\\\\\\", [])\\\\n\\\\n    def _validate(constraints: list) -> list[dict]:\\\\n        valid = []\\\\n        for c in constraints:\\\\n            if not isinstance(c, dict):\\\\n                continue\\\\n            z3f = c.get(\\\\\\\"z3_formula\\\\\\\", \\\\\\\"\\\\\\\")\\\\n            if not z3f:\\\\n                continue\\\\n            # Verify parseable by z3\\\\n            parsed = parse_z3_formula(z3f)\\\\n            if parsed is None:\\\\n                continue\\\\n            valid.append({\\\\n                \\\\\\\"expression\\\\\\\": c.get(\\\\\\\"expression\\\\\\\", z3f),\\\\n                \\\\\\\"z3_formula\\\\\\\": z3f,\\\\n            })\\\\n        return valid\\\\n\\\\n    return _validate(pro_raw), _validate(con_raw)\\\\n\\\\n\\\\ndef generate_contrastive_constraints(\\\\n    llm, problem_text: str, candidate: str, k_contrast: int = 3,\\\\n) -> tuple[list[dict], list[dict]]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Call LLM k_contrast times for a candidate, aggregate pro/con constraints.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    all_pro, all_con = [], []\\\\n    prompt = CONTRASTIVE_PROMPT.format(\\\\n        problem_text=problem_text,\\\\n        candidate_answer=candidate,\\\\n    )\\\\n    for _ in range(k_contrast):\\\\n        raw = llm.call(prompt)\\\\n        pro, con = parse_contrastive_response(raw)\\\\n        all_pro.extend(pro)\\\\n        all_con.extend(con)\\\\n    return all_pro, all_con\\\\n\\\\n\\\\n# ---------------------------------------------------------------------------\\\\n# Contrastive MAX-SAT scoring\\\\n# ---------------------------------------------------------------------------\\\\n\\\\ndef _build_unique_constraints(constraints: list[dict]) -> list[UniqueConstraint]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Convert raw constraint dicts to UniqueConstraint list via deduplication.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    dedup = ConstraintDeduplicator()\\\\n    # Wrap as single-trace batch for the deduplicator\\\\n    return dedup.deduplicate([constraints])\\\\n\\\\n\\\\ndef contrastive_score_candidate(\\\\n    pro_constraints: list[dict],\\\\n    con_constraints: list[dict],\\\\n    solver: MaxSATSolver,\\\\n    maxsat_timeout_ms: int = 10000,\\\\n) -> dict:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Score a single candidate: score = MAX-SAT(pro) - MAX-SAT(con).\\\\n\\\\n    Returns dict with score, pro_satisfied, con_satisfied, and details.\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    # Deduplicate and solve pro constraints\\\\n    pro_unique = _build_unique_constraints(pro_constraints)\\\\n    if pro_unique:\\\\n        pro_result = solver.solve(pro_unique, timeout_ms=maxsat_timeout_ms)\\\\n        pro_sat_weight = pro_result.total_weight\\\\n        pro_n_sat = len(pro_result.satisfied)\\\\n    else:\\\\n        pro_sat_weight = 0.0\\\\n        pro_n_sat = 0\\\\n\\\\n    # Deduplicate and solve con constraints\\\\n    con_unique = _build_unique_constraints(con_constraints)\\\\n    if con_unique:\\\\n        con_result = solver.solve(con_unique, timeout_ms=maxsat_timeout_ms)\\\\n        con_sat_weight = con_result.total_weight\\\\n        con_n_sat = len(con_result.satisfied)\\\\n    else:\\\\n        con_sat_weight = 0.0\\\\n        con_n_sat = 0\\\\n\\\\n    n_pro = len(pro_unique)\\\\n    n_con = len(con_unique)\\\\n    raw_score = pro_sat_weight - con_sat_weight\\\\n    norm_pro = pro_sat_weight / max(n_pro, 1)\\\\n    norm_con = con_sat_weight / max(n_con, 1)\\\\n    score = norm_pro - norm_con\\\\n\\\\n    return {\\\\n        \\\\\\\"score\\\\\\\": score,\\\\n        \\\\\\\"raw_score\\\\\\\": raw_score,\\\\n        \\\\\\\"normalized_pro\\\\\\\": norm_pro,\\\\n        \\\\\\\"normalized_con\\\\\\\": norm_con,\\\\n        \\\\\\\"pro_satisfied_weight\\\\\\\": pro_sat_weight,\\\\n        \\\\\\\"con_satisfied_weight\\\\\\\": con_sat_weight,\\\\n        \\\\\\\"pro_n_satisfied\\\\\\\": pro_n_sat,\\\\n        \\\\\\\"con_n_satisfied\\\\\\\": con_n_sat,\\\\n        \\\\\\\"n_pro\\\\\\\": n_pro,\\\\n        \\\\\\\"n_con\\\\\\\": n_con,\\\\n        \\\\\\\"pro_n_raw\\\\\\\": len(pro_constraints),\\\\n        \\\\\\\"con_n_raw\\\\\\\": len(con_constraints),\\\\n    }\\\\n\\\\n\\\\n# ---------------------------------------------------------------------------\\\\n# Pipeline\\\\n# ---------------------------------------------------------------------------\\\\n\\\\ndef build_generator(args):\\\\n    if args.mode == \\\\\\\"mock\\\\\\\":\\\\n        gen = MockGenerator()\\\\n        gen.domain = \\\\\\\"math\\\\\\\"\\\\n        return gen\\\\n    elif args.mode == \\\\\\\"vllm\\\\\\\":\\\\n        gen = VLLMGenerator(\\\\n            base_url=args.api_base,\\\\n            api_key=[REDACTED],\\\\n            model=args.model if args.model != \\\\\\\"auto\\\\\\\" else None,\\\\n            temperature=args.temperature,\\\\n            max_tokens=args.max_tokens,\\\\n        )\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nContrastive Constraint Generation Pipeline for FOLIO.\\n\\nInstead of extracting constraints from same-source SC traces (which lack\\nindependence), this pipeline generates PRO and CON constraints for each\\ncandidate answer independently via targeted LLM prompts, then uses\\ncontrastive MAX-SAT scoring to select the best answer.\\n\\nThree phases:\\n  Phase 1 — SC voting: generate K traces, majority-vote to get candidate set\\n  Phase 2 — Contrastive constraint generation: for each candidate, prompt the\\n            LLM K_contrast times to produce supporting (pro) and refuting (con)\\n            FOL constraints\\n  Phase 3 — Contrastive MAX-SAT scoring: score = MAX-SAT(pro) - α·MAX-SAT(con)\\n\\nUsage:\\n  python run_contrastive.py --mode vllm --k 12 --k-contrast 3 --temperature 0.7 --seed 42 \\\\\\n    --api-base http://localhost:8000/v1 --model auto \\\\\\n    --data data/folio_full.json \\\\\\n    --output results/exp075_contrastive/results.json \\\\\\n    --save-intermediates\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport re\\nimport sys\\nimport time\\nfrom collections import Counter\\n\\nfrom sica.trace_generator import VLLMGenerator, MockGenerator, extract_boxed_answer\\nfrom sica.constraint_extractor import VLLMBackend, MockLLM, ConstraintExtractor\\nfrom sica.z3_maxsat import (\\n    ConstraintDeduplicator, MaxSATSolver, parse_z3_formula, UniqueConstraint,\\n)\\nfrom sica.pipeline import normalize_logic_answer, _group_logic_answers\\nfrom baselines.self_consistency import SelfConsistency\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s %(levelname)s %(message)s\\\",\\n    handlers=[logging.StreamHandler(sys.stdout)],\\n)\\nlogger = logging.getLogger(__name__)\\n\\n# ---------------------------------------------------------------------------\\n# Contrastive constraint generation prompt\\n# ---------------------------------------------------------------------------\\n\\nCONTRASTIVE_PROMPT = '''\\\\\\nYou are a formal logic expert. Given a logic problem and a candidate answer, \\\\\\ngenerate logical constraints that must hold if the answer is CORRECT (pro) \\\\\\nand constraints that must hold if the answer is WRONG (con).\\n\\nProblem:\\n{problem_text}\\n\\nCandidate answer: {candidate_answer}\\n\\nInstructions:\\n1. List FOL constraints that SUPPORT this answer being correct (pro_constraints).\\n2. List FOL constraints that would hold if this answer is WRONG (con_constraints).\\n3. Express each constraint as a Z3-compatible boolean formula.\\n\\nVariable naming:\\n- Unary property: property_entity (e.g., kind_anne, red_charlie)\\n- Binary relation: relation_subject_object (e.g., eats_bear_squirrel)\\n- Use lowercase with underscores only\\n\\nZ3 operators: Implies(a, b), And(a, b, ...), Or(a, b, ...), Not(a), == True, == False\\n\\nOutput ONLY valid JSON:\\n{{\\\"pro_constraints\\\": [{{\\\"expression\\\": \\\"human-readable\\\", \\\"z3_formula\\\": \\\"Z3 syntax\\\"}}], \\\\\\n\\\"con_constraints\\\": [{{\\\"expression\\\": \\\"human-readable\\\", \\\"z3_formula\\\": \\\"Z3 syntax\\\"}}]}}'''\\n\\n# ---------------------------------------------------------------------------\\n# Contrastive constraint generator\\n# ---------------------------------------------------------------------------\\n\\ndef _strip_thinking(text: str) -> str:\\n    return re.sub(r'&lt;think>.*?&lt;/think>', '', text, flags=re.DOTALL).strip()\\n\\n\\ndef _extract_json_str(text: str) -> str | None:\\n    # Try to find JSON object\\n    for m in re.finditer(r'\\\\{[\\\\s\\\\S]*\\\\}', text):\\n        candidate = m.group()\\n        try:\\n            json.loads(candidate)\\n            return candidate\\n        except json.JSONDecodeError:\\n            continue\\n    return None\\n\\n\\ndef _repair_json(s: str) -> str:\\n    # Fix trailing commas before } or ]\\n    s = re.sub(r',\\\\s*([}\\\\]])', r'\\\\1', s)\\n    # Fix single quotes to double quotes\\n    s = s.replace(\\\"'\\\", '\\\"')\\n    return s\\n\\n\\ndef parse_contrastive_response(raw: str) -> tuple[list[dict], list[dict]]:\\n    \\\"\\\"\\\"Parse LLM response into (pro_constraints, con_constraints).\\n    Each constraint dict has 'expression' and 'z3_formula' keys.\\n    Returns empty lists on parse failure.\\n    \\\"\\\"\\\"\\n \\n\\n... [截断: 输出过长，省略 439 字符] ...\\n\\nw = data.get(\\\"con_constraints\\\", [])\\n\\n    def _validate(constraints: list) -> list[dict]:\\n        valid = []\\n        for c in constraints:\\n            if not isinstance(c, dict):\\n                continue\\n            z3f = c.get(\\\"z3_formula\\\", \\\"\\\")\\n            if not z3f:\\n                continue\\n            # Verify parseable by z3\\n            parsed = parse_z3_formula(z3f)\\n            if parsed is None:\\n                continue\\n            valid.append({\\n                \\\"expression\\\": c.get(\\\"expression\\\", z3f),\\n                \\\"z3_formula\\\": z3f,\\n            })\\n        return valid\\n\\n    return _validate(pro_raw), _validate(con_raw)\\n\\n\\ndef generate_contrastive_constraints(\\n    llm, problem_text: str, candidate: str, k_contrast: int = 3,\\n) -> tuple[list[dict], list[dict]]:\\n    \\\"\\\"\\\"Call LLM k_contrast times for a candidate, aggregate pro/con constraints.\\\"\\\"\\\"\\n    all_pro, all_con = [], []\\n    prompt = CONTRASTIVE_PROMPT.format(\\n        problem_text=problem_text,\\n        candidate_answer=candidate,\\n    )\\n    for _ in range(k_contrast):\\n        raw = llm.call(prompt)\\n        pro, con = parse_contrastive_response(raw)\\n        all_pro.extend(pro)\\n        all_con.extend(con)\\n    return all_pro, all_con\\n\\n\\n# ---------------------------------------------------------------------------\\n# Contrastive MAX-SAT scoring\\n# ---------------------------------------------------------------------------\\n\\ndef _build_unique_constraints(constraints: list[dict]) -> list[UniqueConstraint]:\\n    \\\"\\\"\\\"Convert raw constraint dicts to UniqueConstraint list via deduplication.\\\"\\\"\\\"\\n    dedup = ConstraintDeduplicator()\\n    # Wrap as single-trace batch for the deduplicator\\n    return dedup.deduplicate([constraints])\\n\\n\\ndef contrastive_score_candidate(\\n    pro_constraints: list[dict],\\n    con_constraints: list[dict],\\n    solver: MaxSATSolver,\\n    maxsat_timeout_ms: int = 10000,\\n) -> dict:\\n    \\\"\\\"\\\"Score a single candidate: score = MAX-SAT(pro) - MAX-SAT(con).\\n\\n    Returns dict with score, pro_satisfied, con_satisfied, and details.\\n    \\\"\\\"\\\"\\n    # Deduplicate and solve pro constraints\\n    pro_unique = _build_unique_constraints(pro_constraints)\\n    if pro_unique:\\n        pro_result = solver.solve(pro_unique, timeout_ms=maxsat_timeout_ms)\\n        pro_sat_weight = pro_result.total_weight\\n        pro_n_sat = len(pro_result.satisfied)\\n    else:\\n        pro_sat_weight = 0.0\\n        pro_n_sat = 0\\n\\n    # Deduplicate and solve con constraints\\n    con_unique = _build_unique_constraints(con_constraints)\\n    if con_unique:\\n        con_result = solver.solve(con_unique, timeout_ms=maxsat_timeout_ms)\\n        con_sat_weight = con_result.total_weight\\n        con_n_sat = len(con_result.satisfied)\\n    else:\\n        con_sat_weight = 0.0\\n        con_n_sat = 0\\n\\n    n_pro = len(pro_unique)\\n    n_con = len(con_unique)\\n    raw_score = pro_sat_weight - con_sat_weight\\n    norm_pro = pro_sat_weight / max(n_pro, 1)\\n    norm_con = con_sat_weight / max(n_con, 1)\\n    score = norm_pro - norm_con\\n\\n    return {\\n        \\\"score\\\": score,\\n        \\\"raw_score\\\": raw_score,\\n        \\\"normalized_pro\\\": norm_pro,\\n        \\\"normalized_con\\\": norm_con,\\n        \\\"pro_satisfied_weight\\\": pro_sat_weight,\\n        \\\"con_satisfied_weight\\\": con_sat_weight,\\n        \\\"pro_n_satisfied\\\": pro_n_sat,\\n        \\\"con_n_satisfied\\\": con_n_sat,\\n        \\\"n_pro\\\": n_pro,\\n        \\\"n_con\\\": n_con,\\n        \\\"pro_n_raw\\\": len(pro_constraints),\\n        \\\"con_n_raw\\\": len(con_constraints),\\n    }\\n\\n\\n# ---------------------------------------------------------------------------\\n# Pipeline\\n# ---------------------------------------------------------------------------\\n\\ndef build_generator(args):\\n    if args.mode == \\\"mock\\\":\\n        gen = MockGenerator()\\n        gen.domain = \\\"math\\\"\\n        return gen\\n    elif args.mode == \\\"vllm\\\":\\n        gen = VLLMGenerator(\\n            base_url=args.api_base,\\n            api_key=[REDACTED],\\n            model=args.model if args.model != \\\"auto\\\" else None,\\n            temperature=args.temperature,\\n            max_tokens=args.max_tokens,\\n        )\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T17:40:47.597Z_

<details><summary>↩ Tool result · `toolu_01DzKfajNGPpV3zgwMiuLhpb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"        )\\n        # FOLIO uses standard solve prompt — the generator extracts boxed answers\\n        gen.domain = \\\"math\\\"\\n        return gen\\n    raise ValueError(f\\\"Unknown mode: {args.mode}\\\")\\n\\n\\ndef build_llm(args):\\n    \\\"\\\"\\\"Build LLM backend for contrastive constraint generation.\\\"\\\"\\\"\\n    if args.mode == \\\"mock\\\":\\n        return MockLLM(domain=\\\"logic\\\")\\n    elif args.mode == \\\"vllm\\\":\\n        return VLLMBackend(\\n            base_url=args.api_base,\\n            model=args.model if args.model != \\\"auto\\\" else None,\\n            max_tokens=args.max_tokens,\\n        )\\n    raise ValueError(f\\\"Unknown mode: {args.mode}\\\")\\n\\n\\ndef sc_vote(problem: dict, traces: list[dict]) -> dict:\\n    \\\"\\\"\\\"Run SC majority voting on traces.\\\"\\\"\\\"\\n    sc = SelfConsistency()\\n    answers = [t.get(\\\"answer\\\", \\\"\\\") for t in traces]\\n    trace_texts = [t.get(\\\"trace\\\", \\\"\\\") for t in traces]\\n    return sc.run(problem, trace_texts, answers)\\n\\n\\ndef process_single(\\n    problem: dict,\\n    generator,\\n    llm,\\n    solver: MaxSATSolver,\\n    args,\\n) -> dict:\\n    \\\"\\\"\\\"Process a single problem through the full contrastive pipeline.\\\"\\\"\\\"\\n    t_start = time.perf_counter()\\n    problem_text = problem[\\\"problem\\\"]\\n\\n    # --- Phase 1: Generate K traces + SC vote ---\\n    t0 = time.perf_counter()\\n    traces = generator.generate(problem_text, k=args.k)\\n    trace_time = time.perf_counter() - t0\\n\\n    # Normalize logic answers (FOLIO: True/False/Unknown)\\n    for t in traces:\\n        if t.get(\\\"answer\\\"):\\n            t[\\\"answer\\\"] = normalize_logic_answer(t[\\\"answer\\\"])\\n\\n    sc_result = sc_vote(problem, traces)\\n    sc_answer = sc_result[\\\"answer\\\"]\\n    answer_counts = Counter(t[\\\"answer\\\"] for t in traces if t.get(\\\"answer\\\"))\\n\\n    # Determine candidate set: all answers that got at least 1 vote\\n    candidates = sorted(set(t[\\\"answer\\\"] for t in traces if t.get(\\\"answer\\\")))\\n\\n    # --- Degenerate case: single candidate ---\\n    if len(candidates) <= 1:\\n        total_time = time.perf_counter() - t_start\\n        only_answer = candidates[0] if candidates else \\\"\\\"\\n        return {\\n            \\\"answer\\\": only_answer,\\n            \\\"sc_answer\\\": sc_answer,\\n            \\\"candidates\\\": candidates,\\n            \\\"answer_counts\\\": dict(answer_counts),\\n            \\\"contrastive_scores\\\": {only_answer: 0.0} if only_answer else {},\\n            \\\"pro_constraints_count\\\": 0,\\n            \\\"con_constraints_count\\\": 0,\\n            \\\"per_candidate_details\\\": {},\\n            \\\"degenerate\\\": True,\\n            \\\"timing\\\": {\\n                \\\"trace_gen_s\\\": round(trace_time, 3),\\n                \\\"contrastive_s\\\": 0.0,\\n                \\\"total_s\\\": round(total_time, 3),\\n            },\\n            \\\"traces\\\": traces,\\n        }\\n\\n    # --- Phase 2: Contrastive constraint generation per candidate ---\\n    t0 = time.perf_counter()\\n    per_candidate = {}  # candidate -> {pro: [...], con: [...], score_details: {...}}\\n    total_pro = 0\\n    total_con = 0\\n\\n    for cand in candidates:\\n        pro, con = generate_contrastive_constraints(\\n            llm, problem_text, cand, k_contrast=args.k_contrast,\\n        )\\n        per_candidate[cand] = {\\\"pro\\\": pro, \\\"con\\\": con}\\n        total_pro += len(pro)\\n        total_con += len(con)\\n\\n    contrastive_time = time.perf_counter() - t0\\n\\n    # --- Phase 3: Contrastive MAX-SAT scoring ---\\n    t0 = time.perf_counter()\\n    contrastive_scores = {}\\n    for cand in candidates:\\n        details = contrastive_score_candidate(\\n            per_candidate[cand][\\\"pro\\\"],\\n            per_candidate[cand][\\\"con\\\"],\\n            solver,\\n            maxsat_timeout_ms=args.maxsat_timeout,\\n        )\\n        per_candidate[cand][\\\"score_details\\\"] = details\\n        contrastive_scores[cand] = details[\\\"score\\\"]\\n\\n    scoring_time = time.perf_counter() - t0\\n\\n    # Select answer: highest contrastive score, tie-break by SC vote count\\n    max_score = max(contrastive_scores.values())\\n    top = [a for a, s in contrastive_scores.items() if s == max_score]\\n    if len(top) == 1:\\n        contrastive_answer = top[0]\\n    else:\\n        contrastive_answer = max(top, key=lambda a: answer_counts.get(a, 0))\\n\\n    tot\\n\\n... [截断: 输出过长，省略 6360 字符] ...\\n\\nesults for size)\\n        result_entry = {\\n            \\\"problem_idx\\\": idx,\\n            \\\"problem_id\\\": prob_id,\\n            \\\"problem\\\": problem[\\\"problem\\\"],\\n            \\\"dataset\\\": \\\"folio\\\",\\n            \\\"ground_truth\\\": normalize_logic_answer(problem[\\\"answer\\\"]),\\n            \\\"contrastive_answer\\\": contrastive_answer,\\n            \\\"contrastive_correct\\\": contrastive_correct,\\n            \\\"sc_answer\\\": sc_answer,\\n            \\\"sc_correct\\\": sc_correct,\\n            \\\"candidates\\\": result.get(\\\"candidates\\\", []),\\n            \\\"answer_counts\\\": result.get(\\\"answer_counts\\\", {}),\\n            \\\"contrastive_scores\\\": result.get(\\\"contrastive_scores\\\", {}),\\n            \\\"pro_constraints_count\\\": result.get(\\\"pro_constraints_count\\\", 0),\\n            \\\"con_constraints_count\\\": result.get(\\\"con_constraints_count\\\", 0),\\n            \\\"per_candidate_details\\\": result.get(\\\"per_candidate_details\\\", {}),\\n            \\\"degenerate\\\": result.get(\\\"degenerate\\\", False),\\n            \\\"timing\\\": result.get(\\\"timing\\\", {}),\\n        }\\n        all_results.append(result_entry)\\n\\n        # Save intermediates (full constraints + traces per problem)\\n        if args.save_intermediates:\\n            intermed_dir = os.path.join(\\n                os.path.dirname(args.output) or \\\".\\\", \\\"intermediates\\\"\\n            )\\n            os.makedirs(intermed_dir, exist_ok=True)\\n            intermed_data = {\\n                \\\"problem\\\": problem,\\n                \\\"traces\\\": result.get(\\\"traces\\\", []),\\n                \\\"per_candidate_constraints\\\": result.get(\\\"per_candidate_constraints\\\", {}),\\n                \\\"contrastive_scores\\\": result.get(\\\"contrastive_scores\\\", {}),\\n                \\\"per_candidate_details\\\": result.get(\\\"per_candidate_details\\\", {}),\\n            }\\n            with open(os.path.join(intermed_dir, f\\\"{prob_id}.json\\\"), \\\"w\\\") as f:\\n                json.dump(intermed_data, f, indent=2, default=str)\\n\\n        # Checkpoint\\n        n = len(all_results)\\n        c_acc = sum(1 for r in all_results if r[\\\"contrastive_correct\\\"]) / n\\n        sc_acc = sum(1 for r in all_results if r[\\\"sc_correct\\\"]) / n\\n        summary = {\\n            \\\"n\\\": n,\\n            \\\"contrastive_accuracy\\\": round(c_acc, 4),\\n            \\\"sc_accuracy\\\": round(sc_acc, 4),\\n            \\\"delta\\\": round(c_acc - sc_acc, 4),\\n            \\\"k\\\": args.k,\\n            \\\"k_contrast\\\": args.k_contrast,\\n            \\\"temperature\\\": args.temperature,\\n            \\\"mode\\\": args.mode,\\n            \\\"seed\\\": args.seed,\\n            \\\"total_wall_time_s\\\": round(time.time() - total_start, 1),\\n            \\\"total_pro_constraints\\\": sum(\\n                r[\\\"pro_constraints_count\\\"] for r in all_results\\n            ),\\n            \\\"total_con_constraints\\\": sum(\\n                r[\\\"con_constraints_count\\\"] for r in all_results\\n            ),\\n            \\\"degenerate_count\\\": sum(1 for r in all_results if r.get(\\\"degenerate\\\")),\\n        }\\n        output = {\\\"summary\\\": summary, \\\"results\\\": all_results}\\n        with open(args.output, \\\"w\\\") as f:\\n            json.dump(output, f, indent=2, default=str)\\n\\n    # Final summary\\n    n = len(all_results)\\n    if n > 0:\\n        c_acc = sum(1 for r in all_results if r[\\\"contrastive_correct\\\"]) / n\\n        sc_acc = sum(1 for r in all_results if r[\\\"sc_correct\\\"]) / n\\n        total_wall = time.time() - total_start\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"FINAL RESULTS ({n} problems)\\\")\\n        print(f\\\"  Contrastive: {c_acc:.4f} ({sum(1 for r in all_results if r['contrastive_correct'])}/{n})\\\")\\n        print(f\\\"  SC baseline:  {sc_acc:.4f} ({sum(1 for r in all_results if r['sc_correct'])}/{n})\\\")\\n        print(f\\\"  Delta:        {c_acc - sc_acc:+.4f}\\\")\\n        print(f\\\"  Degenerate:   {sum(1 for r in all_results if r.get('degenerate'))}/{n}\\\")\\n        print(f\\\"  Pro total:    {sum(r['pro_constraints_count'] for r in all_results)}\\\")\\n        print(f\\\"  Con total:    {sum(r['con_constraints_count'] for r in all_results)}\\\")\\n        print(f\\\"  Wall time:    {total_wall/60:.1f} min\\\")\\n        print(f\\\"Results saved to {args.output}\\\")\\n\\n    print(\\\"CONTRASTIVE_PIPELINE_DONE\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bfd88c45-d65d-49b9-97b1-58cf46686ba8",
  "uuid": "dbb8baf0-f247-4bde-82e4-6729a878b059",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"        )\\\\n        # FOLIO uses standard solve prompt — the generator extracts boxed answers\\\\n        gen.domain = \\\\\\\"math\\\\\\\"\\\\n        return gen\\\\n    raise ValueError(f\\\\\\\"Unknown mode: {args.mode}\\\\\\\")\\\\n\\\\n\\\\ndef build_llm(args):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Build LLM backend for contrastive constraint generation.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    if args.mode == \\\\\\\"mock\\\\\\\":\\\\n        return MockLLM(domain=\\\\\\\"logic\\\\\\\")\\\\n    elif args.mode == \\\\\\\"vllm\\\\\\\":\\\\n        return VLLMBackend(\\\\n            base_url=args.api_base,\\\\n            model=args.model if args.model != \\\\\\\"auto\\\\\\\" else None,\\\\n            max_tokens=args.max_tokens,\\\\n        )\\\\n    raise ValueError(f\\\\\\\"Unknown mode: {args.mode}\\\\\\\")\\\\n\\\\n\\\\ndef sc_vote(problem: dict, traces: list[dict]) -> dict:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Run SC majority voting on traces.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    sc = SelfConsistency()\\\\n    answers = [t.get(\\\\\\\"answer\\\\\\\", \\\\\\\"\\\\\\\") for t in traces]\\\\n    trace_texts = [t.get(\\\\\\\"trace\\\\\\\", \\\\\\\"\\\\\\\") for t in traces]\\\\n    return sc.run(problem, trace_texts, answers)\\\\n\\\\n\\\\ndef process_single(\\\\n    problem: dict,\\\\n    generator,\\\\n    llm,\\\\n    solver: MaxSATSolver,\\\\n    args,\\\\n) -> dict:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Process a single problem through the full contrastive pipeline.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    t_start = time.perf_counter()\\\\n    problem_text = problem[\\\\\\\"problem\\\\\\\"]\\\\n\\\\n    # --- Phase 1: Generate K traces + SC vote ---\\\\n    t0 = time.perf_counter()\\\\n    traces = generator.generate(problem_text, k=args.k)\\\\n    trace_time = time.perf_counter() - t0\\\\n\\\\n    # Normalize logic answers (FOLIO: True/False/Unknown)\\\\n    for t in traces:\\\\n        if t.get(\\\\\\\"answer\\\\\\\"):\\\\n            t[\\\\\\\"answer\\\\\\\"] = normalize_logic_answer(t[\\\\\\\"answer\\\\\\\"])\\\\n\\\\n    sc_result = sc_vote(problem, traces)\\\\n    sc_answer = sc_result[\\\\\\\"answer\\\\\\\"]\\\\n    answer_counts = Counter(t[\\\\\\\"answer\\\\\\\"] for t in traces if t.get(\\\\\\\"answer\\\\\\\"))\\\\n\\\\n    # Determine candidate set: all answers that got at least 1 vote\\\\n    candidates = sorted(set(t[\\\\\\\"answer\\\\\\\"] for t in traces if t.get(\\\\\\\"answer\\\\\\\")))\\\\n\\\\n    # --- Degenerate case: single candidate ---\\\\n    if len(candidates) <= 1:\\\\n        total_time = time.perf_counter() - t_start\\\\n        only_answer = candidates[0] if candidates else \\\\\\\"\\\\\\\"\\\\n        return {\\\\n            \\\\\\\"answer\\\\\\\": only_answer,\\\\n            \\\\\\\"sc_answer\\\\\\\": sc_answer,\\\\n            \\\\\\\"candidates\\\\\\\": candidates,\\\\n            \\\\\\\"answer_counts\\\\\\\": dict(answer_counts),\\\\n            \\\\\\\"contrastive_scores\\\\\\\": {only_answer: 0.0} if only_answer else {},\\\\n            \\\\\\\"pro_constraints_count\\\\\\\": 0,\\\\n            \\\\\\\"con_constraints_count\\\\\\\": 0,\\\\n            \\\\\\\"per_candidate_details\\\\\\\": {},\\\\n            \\\\\\\"degenerate\\\\\\\": True,\\\\n            \\\\\\\"timing\\\\\\\": {\\\\n                \\\\\\\"trace_gen_s\\\\\\\": round(trace_time, 3),\\\\n                \\\\\\\"contrastive_s\\\\\\\": 0.0,\\\\n                \\\\\\\"total_s\\\\\\\": round(total_time, 3),\\\\n            },\\\\n            \\\\\\\"traces\\\\\\\": traces,\\\\n        }\\\\n\\\\n    # --- Phase 2: Contrastive constraint generation per candidate ---\\\\n    t0 = time.perf_counter()\\\\n    per_candidate = {}  # candidate -> {pro: [...], con: [...], score_details: {...}}\\\\n    total_pro = 0\\\\n    total_con = 0\\\\n\\\\n    for cand in candidates:\\\\n        pro, con = generate_contrastive_constraints(\\\\n            llm, problem_text, cand, k_contrast=args.k_contrast,\\\\n        )\\\\n        per_candidate[cand] = {\\\\\\\"pro\\\\\\\": pro, \\\\\\\"con\\\\\\\": con}\\\\n        total_pro += len(pro)\\\\n        total_con += len(con)\\\\n\\\\n    contrastive_time = time.perf_counter() - t0\\\\n\\\\n    # --- Phase 3: Contrastive MAX-SAT scoring ---\\\\n    t0 = time.perf_counter()\\\\n    contrastive_scores = {}\\\\n    for cand in candidates:\\\\n        details = contrastive_score_candidate(\\\\n            per_candidate[cand][\\\\\\\"pro\\\\\\\"],\\\\n            per_candidate[cand][\\\\\\\"con\\\\\\\"],\\\\n            solver,\\\\n            maxsat_timeout_ms=args.maxsat_timeout,\\\\n        )\\\\n        per_candidate[cand][\\\\\\\"score_details\\\\\\\"] = details\\\\n        contrastive_scores[cand] = details[\\\\\\\"score\\\\\\\"]\\\\n\\\\n    scoring_time = time.perf_counter() - t0\\\\n\\\\n    # Select answer: highest contrastive score, tie-break by SC vote count\\\\n    max_score = max(contrastive_scores.values())\\\\n    top = [a for a, s in contrastive_scores.items() if s == max_score]\\\\n    if len(top) == 1:\\\\n        contrastive_answer = top[0]\\\\n    else:\\\\n        contrastive_answer = max(top, key=lambda a: answer_counts.get(a, 0))\\\\n\\\\n    tot\\\\n\\\\n... [截断: 输出过长，省略 6360 字符] ...\\\\n\\\\nesults for size)\\\\n        result_entry = {\\\\n            \\\\\\\"problem_idx\\\\\\\": idx,\\\\n            \\\\\\\"problem_id\\\\\\\": prob_id,\\\\n            \\\\\\\"problem\\\\\\\": problem[\\\\\\\"problem\\\\\\\"],\\\\n            \\\\\\\"dataset\\\\\\\": \\\\\\\"folio\\\\\\\",\\\\n            \\\\\\\"ground_truth\\\\\\\": normalize_logic_answer(problem[\\\\\\\"answer\\\\\\\"]),\\\\n            \\\\\\\"contrastive_answer\\\\\\\": contrastive_answer,\\\\n            \\\\\\\"contrastive_correct\\\\\\\": contrastive_correct,\\\\n            \\\\\\\"sc_answer\\\\\\\": sc_answer,\\\\n            \\\\\\\"sc_correct\\\\\\\": sc_correct,\\\\n            \\\\\\\"candidates\\\\\\\": result.get(\\\\\\\"candidates\\\\\\\", []),\\\\n            \\\\\\\"answer_counts\\\\\\\": result.get(\\\\\\\"answer_counts\\\\\\\", {}),\\\\n            \\\\\\\"contrastive_scores\\\\\\\": result.get(\\\\\\\"contrastive_scores\\\\\\\", {}),\\\\n            \\\\\\\"pro_constraints_count\\\\\\\": result.get(\\\\\\\"pro_constraints_count\\\\\\\", 0),\\\\n            \\\\\\\"con_constraints_count\\\\\\\": result.get(\\\\\\\"con_constraints_count\\\\\\\", 0),\\\\n            \\\\\\\"per_candidate_details\\\\\\\": result.get(\\\\\\\"per_candidate_details\\\\\\\", {}),\\\\n            \\\\\\\"degenerate\\\\\\\": result.get(\\\\\\\"degenerate\\\\\\\", False),\\\\n            \\\\\\\"timing\\\\\\\": result.get(\\\\\\\"timing\\\\\\\", {}),\\\\n        }\\\\n        all_results.append(result_entry)\\\\n\\\\n        # Save intermediates (full constraints + traces per problem)\\\\n        if args.save_intermediates:\\\\n            intermed_dir = os.path.join(\\\\n                os.path.dirname(args.output) or \\\\\\\".\\\\\\\", \\\\\\\"intermediates\\\\\\\"\\\\n            )\\\\n            os.makedirs(intermed_dir, exist_ok=True)\\\\n            intermed_data = {\\\\n                \\\\\\\"problem\\\\\\\": problem,\\\\n                \\\\\\\"traces\\\\\\\": result.get(\\\\\\\"traces\\\\\\\", []),\\\\n                \\\\\\\"per_candidate_constraints\\\\\\\": result.get(\\\\\\\"per_candidate_constraints\\\\\\\", {}),\\\\n                \\\\\\\"contrastive_scores\\\\\\\": result.get(\\\\\\\"contrastive_scores\\\\\\\", {}),\\\\n                \\\\\\\"per_candidate_details\\\\\\\": result.get(\\\\\\\"per_candidate_details\\\\\\\", {}),\\\\n            }\\\\n            with open(os.path.join(intermed_dir, f\\\\\\\"{prob_id}.json\\\\\\\"), \\\\\\\"w\\\\\\\") as f:\\\\n                json.dump(intermed_data, f, indent=2, default=str)\\\\n\\\\n        # Checkpoint\\\\n        n = len(all_results)\\\\n        c_acc = sum(1 for r in all_results if r[\\\\\\\"contrastive_correct\\\\\\\"]) / n\\\\n        sc_acc = sum(1 for r in all_results if r[\\\\\\\"sc_correct\\\\\\\"]) / n\\\\n        summary = {\\\\n            \\\\\\\"n\\\\\\\": n,\\\\n            \\\\\\\"contrastive_accuracy\\\\\\\": round(c_acc, 4),\\\\n            \\\\\\\"sc_accuracy\\\\\\\": round(sc_acc, 4),\\\\n            \\\\\\\"delta\\\\\\\": round(c_acc - sc_acc, 4),\\\\n            \\\\\\\"k\\\\\\\": args.k,\\\\n            \\\\\\\"k_contrast\\\\\\\": args.k_contrast,\\\\n            \\\\\\\"temperature\\\\\\\": args.temperature,\\\\n            \\\\\\\"mode\\\\\\\": args.mode,\\\\n            \\\\\\\"seed\\\\\\\": args.seed,\\\\n            \\\\\\\"total_wall_time_s\\\\\\\": round(time.time() - total_start, 1),\\\\n            \\\\\\\"total_pro_constraints\\\\\\\": sum(\\\\n                r[\\\\\\\"pro_constraints_count\\\\\\\"] for r in all_results\\\\n            ),\\\\n            \\\\\\\"total_con_constraints\\\\\\\": sum(\\\\n                r[\\\\\\\"con_constraints_count\\\\\\\"] for r in all_results\\\\n            ),\\\\n            \\\\\\\"degenerate_count\\\\\\\": sum(1 for r in all_results if r.get(\\\\\\\"degenerate\\\\\\\")),\\\\n        }\\\\n        output = {\\\\\\\"summary\\\\\\\": summary, \\\\\\\"results\\\\\\\": all_results}\\\\n        with open(args.output, \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(output, f, indent=2, default=str)\\\\n\\\\n    # Final summary\\\\n    n = len(all_results)\\\\n    if n > 0:\\\\n        c_acc = sum(1 for r in all_results if r[\\\\\\\"contrastive_correct\\\\\\\"]) / n\\\\n        sc_acc = sum(1 for r in all_results if r[\\\\\\\"sc_correct\\\\\\\"]) / n\\\\n        total_wall = time.time() - total_start\\\\n        print(f\\\\\\\"\\\\\\\\n{'='*60}\\\\\\\")\\\\n        print(f\\\\\\\"FINAL RESULTS ({n} problems)\\\\\\\")\\\\n        print(f\\\\\\\"  Contrastive: {c_acc:.4f} ({sum(1 for r in all_results if r['contrastive_correct'])}/{n})\\\\\\\")\\\\n        print(f\\\\\\\"  SC baseline:  {sc_acc:.4f} ({sum(1 for r in all_results if r['sc_correct'])}/{n})\\\\\\\")\\\\n        print(f\\\\\\\"  Delta:        {c_acc - sc_acc:+.4f}\\\\\\\")\\\\n        print(f\\\\\\\"  Degenerate:   {sum(1 for r in all_results if r.get('degenerate'))}/{n}\\\\\\\")\\\\n        print(f\\\\\\\"  Pro total:    {sum(r['pro_constraints_count'] for r in all_results)}\\\\\\\")\\\\n        print(f\\\\\\\"  Con total:    {sum(r['con_constraints_count'] for r in all_results)}\\\\\\\")\\\\n        print(f\\\\\\\"  Wall time:    {total_wall/60:.1f} min\\\\\\\")\\\\n        print(f\\\\\\\"Results saved to {args.output}\\\\\\\")\\\\n\\\\n    print(\\\\\\\"CONTRASTIVE_PIPELINE_DONE\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"        )\\n        # FOLIO uses standard solve prompt — the generator extracts boxed answers\\n        gen.domain = \\\"math\\\"\\n        return gen\\n    raise ValueError(f\\\"Unknown mode: {args.mode}\\\")\\n\\n\\ndef build_llm(args):\\n    \\\"\\\"\\\"Build LLM backend for contrastive constraint generation.\\\"\\\"\\\"\\n    if args.mode == \\\"mock\\\":\\n        return MockLLM(domain=\\\"logic\\\")\\n    elif args.mode == \\\"vllm\\\":\\n        return VLLMBackend(\\n            base_url=args.api_base,\\n            model=args.model if args.model != \\\"auto\\\" else None,\\n            max_tokens=args.max_tokens,\\n        )\\n    raise ValueError(f\\\"Unknown mode: {args.mode}\\\")\\n\\n\\ndef sc_vote(problem: dict, traces: list[dict]) -> dict:\\n    \\\"\\\"\\\"Run SC majority voting on traces.\\\"\\\"\\\"\\n    sc = SelfConsistency()\\n    answers = [t.get(\\\"answer\\\", \\\"\\\") for t in traces]\\n    trace_texts = [t.get(\\\"trace\\\", \\\"\\\") for t in traces]\\n    return sc.run(problem, trace_texts, answers)\\n\\n\\ndef process_single(\\n    problem: dict,\\n    generator,\\n    llm,\\n    solver: MaxSATSolver,\\n    args,\\n) -> dict:\\n    \\\"\\\"\\\"Process a single problem through the full contrastive pipeline.\\\"\\\"\\\"\\n    t_start = time.perf_counter()\\n    problem_text = problem[\\\"problem\\\"]\\n\\n    # --- Phase 1: Generate K traces + SC vote ---\\n    t0 = time.perf_counter()\\n    traces = generator.generate(problem_text, k=args.k)\\n    trace_time = time.perf_counter() - t0\\n\\n    # Normalize logic answers (FOLIO: True/False/Unknown)\\n    for t in traces:\\n        if t.get(\\\"answer\\\"):\\n            t[\\\"answer\\\"] = normalize_logic_answer(t[\\\"answer\\\"])\\n\\n    sc_result = sc_vote(problem, traces)\\n    sc_answer = sc_result[\\\"answer\\\"]\\n    answer_counts = Counter(t[\\\"answer\\\"] for t in traces if t.get(\\\"answer\\\"))\\n\\n    # Determine candidate set: all answers that got at least 1 vote\\n    candidates = sorted(set(t[\\\"answer\\\"] for t in traces if t.get(\\\"answer\\\")))\\n\\n    # --- Degenerate case: single candidate ---\\n    if len(candidates) <= 1:\\n        total_time = time.perf_counter() - t_start\\n        only_answer = candidates[0] if candidates else \\\"\\\"\\n        return {\\n            \\\"answer\\\": only_answer,\\n            \\\"sc_answer\\\": sc_answer,\\n            \\\"candidates\\\": candidates,\\n            \\\"answer_counts\\\": dict(answer_counts),\\n            \\\"contrastive_scores\\\": {only_answer: 0.0} if only_answer else {},\\n            \\\"pro_constraints_count\\\": 0,\\n            \\\"con_constraints_count\\\": 0,\\n            \\\"per_candidate_details\\\": {},\\n            \\\"degenerate\\\": True,\\n            \\\"timing\\\": {\\n                \\\"trace_gen_s\\\": round(trace_time, 3),\\n                \\\"contrastive_s\\\": 0.0,\\n                \\\"total_s\\\": round(total_time, 3),\\n            },\\n            \\\"traces\\\": traces,\\n        }\\n\\n    # --- Phase 2: Contrastive constraint generation per candidate ---\\n    t0 = time.perf_counter()\\n    per_candidate = {}  # candidate -> {pro: [...], con: [...], score_details: {...}}\\n    total_pro = 0\\n    total_con = 0\\n\\n    for cand in candidates:\\n        pro, con = generate_contrastive_constraints(\\n            llm, problem_text, cand, k_contrast=args.k_contrast,\\n        )\\n        per_candidate[cand] = {\\\"pro\\\": pro, \\\"con\\\": con}\\n        total_pro += len(pro)\\n        total_con += len(con)\\n\\n    contrastive_time = time.perf_counter() - t0\\n\\n    # --- Phase 3: Contrastive MAX-SAT scoring ---\\n    t0 = time.perf_counter()\\n    contrastive_scores = {}\\n    for cand in candidates:\\n        details = contrastive_score_candidate(\\n            per_candidate[cand][\\\"pro\\\"],\\n            per_candidate[cand][\\\"con\\\"],\\n            solver,\\n            maxsat_timeout_ms=args.maxsat_timeout,\\n        )\\n        per_candidate[cand][\\\"score_details\\\"] = details\\n        contrastive_scores[cand] = details[\\\"score\\\"]\\n\\n    scoring_time = time.perf_counter() - t0\\n\\n    # Select answer: highest contrastive score, tie-break by SC vote count\\n    max_score = max(contrastive_scores.values())\\n    top = [a for a, s in contrastive_scores.items() if s == max_score]\\n    if len(top) == 1:\\n        contrastive_answer = top[0]\\n    else:\\n        contrastive_answer = max(top, key=lambda a: answer_counts.get(a, 0))\\n\\n    tot\\n\\n... [截断: 输出过长，省略 6360 字符] ...\\n\\nesults for size)\\n        result_entry = {\\n            \\\"problem_idx\\\": idx,\\n            \\\"problem_id\\\": prob_id,\\n            \\\"problem\\\": problem[\\\"problem\\\"],\\n            \\\"dataset\\\": \\\"folio\\\",\\n            \\\"ground_truth\\\": normalize_logic_answer(problem[\\\"answer\\\"]),\\n            \\\"contrastive_answer\\\": contrastive_answer,\\n            \\\"contrastive_correct\\\": contrastive_correct,\\n            \\\"sc_answer\\\": sc_answer,\\n            \\\"sc_correct\\\": sc_correct,\\n            \\\"candidates\\\": result.get(\\\"candidates\\\", []),\\n            \\\"answer_counts\\\": result.get(\\\"answer_counts\\\", {}),\\n            \\\"contrastive_scores\\\": result.get(\\\"contrastive_scores\\\", {}),\\n            \\\"pro_constraints_count\\\": result.get(\\\"pro_constraints_count\\\", 0),\\n            \\\"con_constraints_count\\\": result.get(\\\"con_constraints_count\\\", 0),\\n            \\\"per_candidate_details\\\": result.get(\\\"per_candidate_details\\\", {}),\\n            \\\"degenerate\\\": result.get(\\\"degenerate\\\", False),\\n            \\\"timing\\\": result.get(\\\"timing\\\", {}),\\n        }\\n        all_results.append(result_entry)\\n\\n        # Save intermediates (full constraints + traces per problem)\\n        if args.save_intermediates:\\n            intermed_dir = os.path.join(\\n                os.path.dirname(args.output) or \\\".\\\", \\\"intermediates\\\"\\n            )\\n            os.makedirs(intermed_dir, exist_ok=True)\\n            intermed_data = {\\n                \\\"problem\\\": problem,\\n                \\\"traces\\\": result.get(\\\"traces\\\", []),\\n                \\\"per_candidate_constraints\\\": result.get(\\\"per_candidate_constraints\\\", {}),\\n                \\\"contrastive_scores\\\": result.get(\\\"contrastive_scores\\\", {}),\\n                \\\"per_candidate_details\\\": result.get(\\\"per_candidate_details\\\", {}),\\n            }\\n            with open(os.path.join(intermed_dir, f\\\"{prob_id}.json\\\"), \\\"w\\\") as f:\\n                json.dump(intermed_data, f, indent=2, default=str)\\n\\n        # Checkpoint\\n        n = len(all_results)\\n        c_acc = sum(1 for r in all_results if r[\\\"contrastive_correct\\\"]) / n\\n        sc_acc = sum(1 for r in all_results if r[\\\"sc_correct\\\"]) / n\\n        summary = {\\n            \\\"n\\\": n,\\n            \\\"contrastive_accuracy\\\": round(c_acc, 4),\\n            \\\"sc_accuracy\\\": round(sc_acc, 4),\\n            \\\"delta\\\": round(c_acc - sc_acc, 4),\\n            \\\"k\\\": args.k,\\n            \\\"k_contrast\\\": args.k_contrast,\\n            \\\"temperature\\\": args.temperature,\\n            \\\"mode\\\": args.mode,\\n            \\\"seed\\\": args.seed,\\n            \\\"total_wall_time_s\\\": round(time.time() - total_start, 1),\\n            \\\"total_pro_constraints\\\": sum(\\n                r[\\\"pro_constraints_count\\\"] for r in all_results\\n            ),\\n            \\\"total_con_constraints\\\": sum(\\n                r[\\\"con_constraints_count\\\"] for r in all_results\\n            ),\\n            \\\"degenerate_count\\\": sum(1 for r in all_results if r.get(\\\"degenerate\\\")),\\n        }\\n        output = {\\\"summary\\\": summary, \\\"results\\\": all_results}\\n        with open(args.output, \\\"w\\\") as f:\\n            json.dump(output, f, indent=2, default=str)\\n\\n    # Final summary\\n    n = len(all_results)\\n    if n > 0:\\n        c_acc = sum(1 for r in all_results if r[\\\"contrastive_correct\\\"]) / n\\n        sc_acc = sum(1 for r in all_results if r[\\\"sc_correct\\\"]) / n\\n        total_wall = time.time() - total_start\\n        print(f\\\"\\\\n{'='*60}\\\")\\n        print(f\\\"FINAL RESULTS ({n} problems)\\\")\\n        print(f\\\"  Contrastive: {c_acc:.4f} ({sum(1 for r in all_results if r['contrastive_correct'])}/{n})\\\")\\n        print(f\\\"  SC baseline:  {sc_acc:.4f} ({sum(1 for r in all_results if r['sc_correct'])}/{n})\\\")\\n        print(f\\\"  Delta:        {c_acc - sc_acc:+.4f}\\\")\\n        print(f\\\"  Degenerate:   {sum(1 for r in all_results if r.get('degenerate'))}/{n}\\\")\\n        print(f\\\"  Pro total:    {sum(r['pro_constraints_count'] for r in all_results)}\\\")\\n        print(f\\\"  Con total:    {sum(r['con_constraints_count'] for r in all_results)}\\\")\\n        print(f\\\"  Wall time:    {total_wall/60:.1f} min\\\")\\n        print(f\\\"Results saved to {args.output}\\\")\\n\\n    print(\\\"CONTRASTIVE_PIPELINE_DONE\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---
