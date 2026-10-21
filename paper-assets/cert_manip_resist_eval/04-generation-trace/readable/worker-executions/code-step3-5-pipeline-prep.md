# code step3 5 pipeline prep

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 92
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/workers/worker_code_step3-5-pipeline-prep_20260522T145553.log`
- **Structured JSON:** [`fca053addc40a8fe3a5c.json`](../../sessions/fc/fca053addc40a8fe3a5c.json)

## Before a recorded user message

92 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
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
  "uuid": "434fced5-4a01-43f4-a0a0-71737041c38c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-cert-manip-resist-eval/memory/"
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
    "resetsAt": 1779466800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1ad778d2-8ed4-4ef8-b574-7a9e4314aeef",
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the 4 scripts on the remote server to understand their current data loading logic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "bec570c5-6983-4422-8426-5711a7c14bbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017eYMV5T1g5yXmRxj67eWrQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13388,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13388
      },
      "output_tokens": 29,
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

先读取 4 个脚本，了解现有数据加载逻辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "e8adca49-6012-4b17-b72c-3b80d4618aa0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017eYMV5T1g5yXmRxj67eWrQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13388,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13388
      },
      "output_tokens": 29,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PY7eRz8h5QySg5cqxfH5Zv`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
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
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "d41ff4ac-cf16-4e96-a202-015e30061223",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017eYMV5T1g5yXmRxj67eWrQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13388,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13388
      },
      "output_tokens": 29,
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

_source line 7 · 2026-05-22T14:56:06.402Z_

<details><summary>↩ Tool result · `toolu_01PY7eRz8h5QySg5cqxfH5Zv`</summary>

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
  "tool_name": "mcp__agent-ml-research__detect_image"
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
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "a5ab60b2-1124-42cc-8a43-c5a53159c041",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all 4 scripts in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "6445bbd7-b9e1-4097-86cc-1e6ca52d0338",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gnr9tuWwdVbM3PtFVZEq14",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 934,
      "cache_read_input_tokens": 24835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 934
      },
      "output_tokens": 52,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018rSXhvucRUStT6cuLtpvuF`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "83f27241-bb1f-4ebd-8fa9-9100df63e6c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gnr9tuWwdVbM3PtFVZEq14",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 934,
      "cache_read_input_tokens": 24835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 934
      },
      "output_tokens": 52,
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01BZ6U5dYZDWf4yrspZ9VhLD`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/scripts/run_plan001_confound_diagnosis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "2aaa2ccb-4186-41f4-8731-0f859da42d0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gnr9tuWwdVbM3PtFVZEq14",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 934,
      "cache_read_input_tokens": 24835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 934
      },
      "output_tokens": 52,
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

_source line 11 · 2026-05-22T14:56:10.896Z_

<details><summary>↩ Tool result · `toolu_018rSXhvucRUStT6cuLtpvuF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Plan 001 Step 3: Compute 15-model pairwise MI matrix and K_eff for all C(15,3) panels.\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport itertools\\nimport numpy as np\\nfrom pathlib import Path\\nfrom collections import Counter\\nfrom sklearn.metrics import mutual_info_score\\n\\nfrom src.utils import setup_logging\\n\\nlogger = setup_logging(\\\"plan001_step3_mi\\\")\\n\\n# ── Model lists ──────────────────────────────────────────────────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4\\\", \\\"gpt-5.5\\\", \\\"gemini-2.5-pro\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4\\\", \\\"gpt-4o\\\", \\\"gemini-2.5-flash\\\",\\n    \\\"gpt-4o-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\n\\n# ── Paths ────────────────────────────────────────────────────────────\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_DIR = PLAN001_DIR / \\\"mi_matrix\\\"\\n\\nSTEP2V3_CKPT = RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\"\\nTAXONOMY_CKPT = RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\"\\n\\n\\ndef load_local_clean_scores():\\n    \\\"\\\"\\\"Load clean scores for 6 local models from checkpoint files.\\\"\\\"\\\"\\n    scores = {}\\n    for ckpt_path in [STEP2V3_CKPT, TAXONOMY_CKPT]:\\n        if not ckpt_path.exists():\\n            logger.warning(f\\\"Checkpoint not found: {ckpt_path}\\\")\\n            continue\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        cs = data.get(\\\"clean_scores\\\", {})\\n        for ds in DATASETS:\\n            if ds not in cs:\\n                continue\\n            if ds not in scores:\\n                scores[ds] = {}\\n            for model_id, model_scores in cs[ds].items():\\n                if model_id in LOCAL_MODELS and model_id not in scores[ds]:\\n                    scores[ds][model_id] = model_scores\\n    return scores\\n\\n\\ndef load_api_clean_scores():\\n    \\\"\\\"\\\"Load clean scores for 9 API models from individual score files.\\\"\\\"\\\"\\n    scores = {}\\n    for model_id in API_MODELS:\\n        for ds in DATASETS:\\n            fname = f\\\"{model_id}__{ds}__clean.json\\\"\\n            fpath = SCORES_DIR / fname\\n            if not fpath.exists():\\n                logger.warning(f\\\"API score file not found: {fpath}\\\")\\n                continue\\n            with open(fpath) as f:\\n                data = json.load(f)\\n            if ds not in scores:\\n                scores[ds] = {}\\n            scores[ds][model_id] = data.get(\\\"scores\\\", [])\\n    return scores\\n\\n\\ndef merge_clean_scores(local_scores, api_scores):\\n    \\\"\\\"\\\"Merge local and API clean scores into unified dict.\\\"\\\"\\\"\\n    merged = {}\\n    for ds in DATASETS:\\n        merged[ds] = {}\\n        for src in [local_scores, api_scores]:\\n            if ds in src:\\n                merged[ds].update(src[ds])\\n    return merged\\n\\n\\ndef extract_winner_vector(score_list):\\n    \\\"\\\"\\\"Extract winner labels from score list, normalizing to A/B/C/tie.\\\"\\\"\\\"\\n    winners = []\\n    for s in score_list:\\n        w = s.get(\\\"winner\\\", \\\"tie\\\") if isinstance(s, dict) else \\\"tie\\\"\\n        winners.append(w)\\n    return winners\\n\\n\\ndef compute_pairwise_mi(winners_i, winners_j):\\n    \\\"\\\"\\\"Compute mutual information between two winner vectors.\\\"\\\"\\\"\\n    n = min(len(winners_i), len(winners_j))\\n    if n == 0:\\n        return 0.0\\n    return mutual_info_score(winners_i[:n], winners_j[:n])\\n\\n\\ndef build_mi_matrix(clean_scores, dataset):\\n    \\\"\\\"\\\"Build 15x15 MI matrix for a dataset.\\\"\\\"\\\"\\n    ds_scores = clean_scores.get(dataset, {})\\n    n_models = len(ALL_MODELS)\\n    mi_mat = np.zeros((n_models, n_models))\\n\\n    winner_vectors = {}\\n    for i, model_id in enumerate(ALL_MODELS):\\n        if model_id in ds_scores:\\n            winner_vectors[i] = extract_winner_vector(ds_scores[model_id])\\n        else:\\n            logger.warning(f\\\"No clean scores for {model_id} on {dataset}\\\")\\n\\n    for i in range(n_m\\n\\n... [截断: 输出过长，省略 666 字符] ...\\n\\n return keff / K\\n\\n\\ndef compute_all_panel_keffs(mi_matrix, dataset):\\n    \\\"\\\"\\\"Compute K_eff for all C(15,3)=455 panels.\\\"\\\"\\\"\\n    n_models = len(ALL_MODELS)\\n    idx_to_model = {i: m for i, m in enumerate(ALL_MODELS)}\\n    panels = {}\\n\\n    for combo in itertools.combinations(range(n_models), 3):\\n        model_ids = [idx_to_model[i] for i in combo]\\n        panel_key = \\\"|\\\".join(model_ids)\\n        keff = mi_based_keff(mi_matrix, list(combo))\\n\\n        mi_pairs = {}\\n        for a, b in itertools.combinations(combo, 2):\\n            pair_key = f\\\"{idx_to_model[a]}|{idx_to_model[b]}\\\"\\n            mi_pairs[pair_key] = float(mi_matrix[a, b])\\n\\n        panels[panel_key] = {\\n            \\\"models\\\": model_ids,\\n            \\\"keff\\\": float(keff),\\n            \\\"mi_pairs\\\": mi_pairs,\\n        }\\n\\n    return panels\\n\\n\\ndef main():\\n    logger.info(\\\"=== Plan 001 Step 3: MI Matrix Computation ===\\\")\\n\\n    local_scores = load_local_clean_scores()\\n    api_scores = load_api_clean_scores()\\n    clean_scores = merge_clean_scores(local_scores, api_scores)\\n\\n    for ds in DATASETS:\\n        available = list(clean_scores.get(ds, {}).keys())\\n        missing = [m for m in ALL_MODELS if m not in available]\\n        logger.info(f\\\"  {ds}: {len(available)}/{len(ALL_MODELS)} models available\\\")\\n        if missing:\\n            logger.warning(f\\\"  {ds}: missing models: {missing}\\\")\\n\\n    available_count = sum(\\n        1 for ds in DATASETS\\n        for m in ALL_MODELS\\n        if m in clean_scores.get(ds, {})\\n    )\\n    total_needed = len(DATASETS) * len(ALL_MODELS)\\n    if available_count < total_needed:\\n        logger.warning(\\n            f\\\"Only {available_count}/{total_needed} model×dataset combos available. \\\"\\n            f\\\"MI matrix will have zeros for missing pairs.\\\"\\n        )\\n\\n    mi_matrices = {}\\n    keff_per_panel = {}\\n\\n    for ds in DATASETS:\\n        logger.info(f\\\"\\\\n--- Computing MI matrix for {ds} ---\\\")\\n        mi_mat = build_mi_matrix(clean_scores, ds)\\n        mi_matrices[ds] = mi_mat.tolist()\\n\\n        nonzero = np.count_nonzero(mi_mat)\\n        max_possible = len(ALL_MODELS) * (len(ALL_MODELS) - 1)\\n        logger.info(f\\\"  MI matrix: {nonzero}/{max_possible} non-zero entries\\\")\\n        if nonzero > 0:\\n            upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\\n            upper_nz = upper[upper > 0]\\n            if len(upper_nz) > 0:\\n                logger.info(\\n                    f\\\"  MI range: [{upper_nz.min():.4f}, {upper_nz.max():.4f}], \\\"\\n                    f\\\"mean={upper_nz.mean():.4f}\\\"\\n                )\\n\\n        logger.info(f\\\"  Computing K_eff for all C(15,3)=455 panels on {ds}...\\\")\\n        panels = compute_all_panel_keffs(mi_mat, ds)\\n        keff_per_panel[ds] = panels\\n\\n        keff_values = [p[\\\"keff\\\"] for p in panels.values()]\\n        logger.info(\\n            f\\\"  K_eff range: [{min(keff_values):.3f}, {max(keff_values):.3f}], \\\"\\n            f\\\"mean={np.mean(keff_values):.3f}\\\"\\n        )\\n\\n    MI_DIR.mkdir(parents=True, exist_ok=True)\\n    output = {\\n        \\\"models\\\": ALL_MODELS,\\n        \\\"mi_matrix\\\": mi_matrices,\\n        \\\"keff_per_panel\\\": keff_per_panel,\\n    }\\n    output_path = MI_DIR / \\\"mi_matrix_15models.json\\\"\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2, ensure_ascii=False)\\n    logger.info(f\\\"\\\\nSaved MI matrix to {output_path}\\\")\\n\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(\\\"MI MATRIX SUMMARY\\\")\\n    print(\\\"=\\\" * 70)\\n    for ds in DATASETS:\\n        mi_mat = np.array(mi_matrices[ds])\\n        upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\\n        n_computed = np.count_nonzero(upper)\\n        print(f\\\"\\\\n{ds}:\\\")\\n        print(f\\\"  Pairwise MI computed: {n_computed}/105\\\")\\n        if n_computed > 0:\\n            nz = upper[upper > 0]\\n            print(f\\\"  MI range: [{nz.min():.4f}, {nz.max():.4f}]\\\")\\n            print(f\\\"  MI mean:  {nz.mean():.4f}\\\")\\n        keffs = [p[\\\"keff\\\"] for p in keff_per_panel[ds].values()]\\n        print(f\\\"  K_eff (455 panels): [{min(keffs):.3f}, {max(keffs):.3f}], mean={np.mean(keffs):.3f}\\\")\\n    print(\\\"=\\\" * 70)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.98}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "5db2e243-ef95-4b2a-a76f-602969a6a843",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Plan 001 Step 3: Compute 15-model pairwise MI matrix and K_eff for all C(15,3) panels.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport os\\\\nos.environ[\\\\\\\"HF_HOME\\\\\\\"] = \\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"\\\\n\\\\nimport sys\\\\nsys.path.insert(0, \\\\\\\"/root/cert_manip_resist_eval\\\\\\\")\\\\n\\\\nimport json\\\\nimport itertools\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\nfrom collections import Counter\\\\nfrom sklearn.metrics import mutual_info_score\\\\n\\\\nfrom src.utils import setup_logging\\\\n\\\\nlogger = setup_logging(\\\\\\\"plan001_step3_mi\\\\\\\")\\\\n\\\\n# ── Model lists ──────────────────────────────────────────────────────\\\\nLOCAL_MODELS = [\\\\n    \\\\\\\"qwen2.5-72b\\\\\\\", \\\\\\\"llama3.1-70b\\\\\\\", \\\\\\\"mistral-large\\\\\\\",\\\\n    \\\\\\\"qwen2.5-32b\\\\\\\", \\\\\\\"qwen2.5-14b\\\\\\\", \\\\\\\"llama3.1-8b\\\\\\\",\\\\n]\\\\nAPI_MODELS = [\\\\n    \\\\\\\"claude-opus-4\\\\\\\", \\\\\\\"gpt-5.5\\\\\\\", \\\\\\\"gemini-2.5-pro\\\\\\\", \\\\\\\"gpt-4.1\\\\\\\",\\\\n    \\\\\\\"claude-sonnet-4\\\\\\\", \\\\\\\"gpt-4o\\\\\\\", \\\\\\\"gemini-2.5-flash\\\\\\\",\\\\n    \\\\\\\"gpt-4o-mini\\\\\\\", \\\\\\\"claude-3-haiku\\\\\\\",\\\\n]\\\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\\\nDATASETS = [\\\\\\\"mmlu\\\\\\\", \\\\\\\"arc_challenge\\\\\\\"]\\\\n\\\\n# ── Paths ────────────────────────────────────────────────────────────\\\\nRESULTS_DIR = Path(\\\\\\\"/root/cert_manip_resist_eval/artifacts/results\\\\\\\")\\\\nPLAN001_DIR = RESULTS_DIR / \\\\\\\"plan001\\\\\\\"\\\\nSCORES_DIR = PLAN001_DIR / \\\\\\\"individual_scores\\\\\\\"\\\\nMI_DIR = PLAN001_DIR / \\\\\\\"mi_matrix\\\\\\\"\\\\n\\\\nSTEP2V3_CKPT = RESULTS_DIR / \\\\\\\"_step2v3_checkpoint.json\\\\\\\"\\\\nTAXONOMY_CKPT = RESULTS_DIR / \\\\\\\"_taxonomy_checkpoint.json\\\\\\\"\\\\n\\\\n\\\\ndef load_local_clean_scores():\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load clean scores for 6 local models from checkpoint files.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    scores = {}\\\\n    for ckpt_path in [STEP2V3_CKPT, TAXONOMY_CKPT]:\\\\n        if not ckpt_path.exists():\\\\n            logger.warning(f\\\\\\\"Checkpoint not found: {ckpt_path}\\\\\\\")\\\\n            continue\\\\n        with open(ckpt_path) as f:\\\\n            data = json.load(f)\\\\n        cs = data.get(\\\\\\\"clean_scores\\\\\\\", {})\\\\n        for ds in DATASETS:\\\\n            if ds not in cs:\\\\n                continue\\\\n            if ds not in scores:\\\\n                scores[ds] = {}\\\\n            for model_id, model_scores in cs[ds].items():\\\\n                if model_id in LOCAL_MODELS and model_id not in scores[ds]:\\\\n                    scores[ds][model_id] = model_scores\\\\n    return scores\\\\n\\\\n\\\\ndef load_api_clean_scores():\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load clean scores for 9 API models from individual score files.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    scores = {}\\\\n    for model_id in API_MODELS:\\\\n        for ds in DATASETS:\\\\n            fname = f\\\\\\\"{model_id}__{ds}__clean.json\\\\\\\"\\\\n            fpath = SCORES_DIR / fname\\\\n            if not fpath.exists():\\\\n                logger.warning(f\\\\\\\"API score file not found: {fpath}\\\\\\\")\\\\n                continue\\\\n            with open(fpath) as f:\\\\n                data = json.load(f)\\\\n            if ds not in scores:\\\\n                scores[ds] = {}\\\\n            scores[ds][model_id] = data.get(\\\\\\\"scores\\\\\\\", [])\\\\n    return scores\\\\n\\\\n\\\\ndef merge_clean_scores(local_scores, api_scores):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Merge local and API clean scores into unified dict.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    merged = {}\\\\n    for ds in DATASETS:\\\\n        merged[ds] = {}\\\\n        for src in [local_scores, api_scores]:\\\\n            if ds in src:\\\\n                merged[ds].update(src[ds])\\\\n    return merged\\\\n\\\\n\\\\ndef extract_winner_vector(score_list):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Extract winner labels from score list, normalizing to A/B/C/tie.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    winners = []\\\\n    for s in score_list:\\\\n        w = s.get(\\\\\\\"winner\\\\\\\", \\\\\\\"tie\\\\\\\") if isinstance(s, dict) else \\\\\\\"tie\\\\\\\"\\\\n        winners.append(w)\\\\n    return winners\\\\n\\\\n\\\\ndef compute_pairwise_mi(winners_i, winners_j):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute mutual information between two winner vectors.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    n = min(len(winners_i), len(winners_j))\\\\n    if n == 0:\\\\n        return 0.0\\\\n    return mutual_info_score(winners_i[:n], winners_j[:n])\\\\n\\\\n\\\\ndef build_mi_matrix(clean_scores, dataset):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Build 15x15 MI matrix for a dataset.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    ds_scores = clean_scores.get(dataset, {})\\\\n    n_models = len(ALL_MODELS)\\\\n    mi_mat = np.zeros((n_models, n_models))\\\\n\\\\n    winner_vectors = {}\\\\n    for i, model_id in enumerate(ALL_MODELS):\\\\n        if model_id in ds_scores:\\\\n            winner_vectors[i] = extract_winner_vector(ds_scores[model_id])\\\\n        else:\\\\n            logger.warning(f\\\\\\\"No clean scores for {model_id} on {dataset}\\\\\\\")\\\\n\\\\n    for i in range(n_m\\\\n\\\\n... [截断: 输出过长，省略 666 字符] ...\\\\n\\\\n return keff / K\\\\n\\\\n\\\\ndef compute_all_panel_keffs(mi_matrix, dataset):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute K_eff for all C(15,3)=455 panels.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    n_models = len(ALL_MODELS)\\\\n    idx_to_model = {i: m for i, m in enumerate(ALL_MODELS)}\\\\n    panels = {}\\\\n\\\\n    for combo in itertools.combinations(range(n_models), 3):\\\\n        model_ids = [idx_to_model[i] for i in combo]\\\\n        panel_key = \\\\\\\"|\\\\\\\".join(model_ids)\\\\n        keff = mi_based_keff(mi_matrix, list(combo))\\\\n\\\\n        mi_pairs = {}\\\\n        for a, b in itertools.combinations(combo, 2):\\\\n            pair_key = f\\\\\\\"{idx_to_model[a]}|{idx_to_model[b]}\\\\\\\"\\\\n            mi_pairs[pair_key] = float(mi_matrix[a, b])\\\\n\\\\n        panels[panel_key] = {\\\\n            \\\\\\\"models\\\\\\\": model_ids,\\\\n            \\\\\\\"keff\\\\\\\": float(keff),\\\\n            \\\\\\\"mi_pairs\\\\\\\": mi_pairs,\\\\n        }\\\\n\\\\n    return panels\\\\n\\\\n\\\\ndef main():\\\\n    logger.info(\\\\\\\"=== Plan 001 Step 3: MI Matrix Computation ===\\\\\\\")\\\\n\\\\n    local_scores = load_local_clean_scores()\\\\n    api_scores = load_api_clean_scores()\\\\n    clean_scores = merge_clean_scores(local_scores, api_scores)\\\\n\\\\n    for ds in DATASETS:\\\\n        available = list(clean_scores.get(ds, {}).keys())\\\\n        missing = [m for m in ALL_MODELS if m not in available]\\\\n        logger.info(f\\\\\\\"  {ds}: {len(available)}/{len(ALL_MODELS)} models available\\\\\\\")\\\\n        if missing:\\\\n            logger.warning(f\\\\\\\"  {ds}: missing models: {missing}\\\\\\\")\\\\n\\\\n    available_count = sum(\\\\n        1 for ds in DATASETS\\\\n        for m in ALL_MODELS\\\\n        if m in clean_scores.get(ds, {})\\\\n    )\\\\n    total_needed = len(DATASETS) * len(ALL_MODELS)\\\\n    if available_count < total_needed:\\\\n        logger.warning(\\\\n            f\\\\\\\"Only {available_count}/{total_needed} model×dataset combos available. \\\\\\\"\\\\n            f\\\\\\\"MI matrix will have zeros for missing pairs.\\\\\\\"\\\\n        )\\\\n\\\\n    mi_matrices = {}\\\\n    keff_per_panel = {}\\\\n\\\\n    for ds in DATASETS:\\\\n        logger.info(f\\\\\\\"\\\\\\\\n--- Computing MI matrix for {ds} ---\\\\\\\")\\\\n        mi_mat = build_mi_matrix(clean_scores, ds)\\\\n        mi_matrices[ds] = mi_mat.tolist()\\\\n\\\\n        nonzero = np.count_nonzero(mi_mat)\\\\n        max_possible = len(ALL_MODELS) * (len(ALL_MODELS) - 1)\\\\n        logger.info(f\\\\\\\"  MI matrix: {nonzero}/{max_possible} non-zero entries\\\\\\\")\\\\n        if nonzero > 0:\\\\n            upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\\\\n            upper_nz = upper[upper > 0]\\\\n            if len(upper_nz) > 0:\\\\n                logger.info(\\\\n                    f\\\\\\\"  MI range: [{upper_nz.min():.4f}, {upper_nz.max():.4f}], \\\\\\\"\\\\n                    f\\\\\\\"mean={upper_nz.mean():.4f}\\\\\\\"\\\\n                )\\\\n\\\\n        logger.info(f\\\\\\\"  Computing K_eff for all C(15,3)=455 panels on {ds}...\\\\\\\")\\\\n        panels = compute_all_panel_keffs(mi_mat, ds)\\\\n        keff_per_panel[ds] = panels\\\\n\\\\n        keff_values = [p[\\\\\\\"keff\\\\\\\"] for p in panels.values()]\\\\n        logger.info(\\\\n            f\\\\\\\"  K_eff range: [{min(keff_values):.3f}, {max(keff_values):.3f}], \\\\\\\"\\\\n            f\\\\\\\"mean={np.mean(keff_values):.3f}\\\\\\\"\\\\n        )\\\\n\\\\n    MI_DIR.mkdir(parents=True, exist_ok=True)\\\\n    output = {\\\\n        \\\\\\\"models\\\\\\\": ALL_MODELS,\\\\n        \\\\\\\"mi_matrix\\\\\\\": mi_matrices,\\\\n        \\\\\\\"keff_per_panel\\\\\\\": keff_per_panel,\\\\n    }\\\\n    output_path = MI_DIR / \\\\\\\"mi_matrix_15models.json\\\\\\\"\\\\n    with open(output_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(output, f, indent=2, ensure_ascii=False)\\\\n    logger.info(f\\\\\\\"\\\\\\\\nSaved MI matrix to {output_path}\\\\\\\")\\\\n\\\\n    print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 70)\\\\n    print(\\\\\\\"MI MATRIX SUMMARY\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n    for ds in DATASETS:\\\\n        mi_mat = np.array(mi_matrices[ds])\\\\n        upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\\\\n        n_computed = np.count_nonzero(upper)\\\\n        print(f\\\\\\\"\\\\\\\\n{ds}:\\\\\\\")\\\\n        print(f\\\\\\\"  Pairwise MI computed: {n_computed}/105\\\\\\\")\\\\n        if n_computed > 0:\\\\n            nz = upper[upper > 0]\\\\n            print(f\\\\\\\"  MI range: [{nz.min():.4f}, {nz.max():.4f}]\\\\\\\")\\\\n            print(f\\\\\\\"  MI mean:  {nz.mean():.4f}\\\\\\\")\\\\n        keffs = [p[\\\\\\\"keff\\\\\\\"] for p in keff_per_panel[ds].values()]\\\\n        print(f\\\\\\\"  K_eff (455 panels): [{min(keffs):.3f}, {max(keffs):.3f}], mean={np.mean(keffs):.3f}\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.98}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Plan 001 Step 3: Compute 15-model pairwise MI matrix and K_eff for all C(15,3) panels.\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport itertools\\nimport numpy as np\\nfrom pathlib import Path\\nfrom collections import Counter\\nfrom sklearn.metrics import mutual_info_score\\n\\nfrom src.utils import setup_logging\\n\\nlogger = setup_logging(\\\"plan001_step3_mi\\\")\\n\\n# ── Model lists ──────────────────────────────────────────────────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4\\\", \\\"gpt-5.5\\\", \\\"gemini-2.5-pro\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4\\\", \\\"gpt-4o\\\", \\\"gemini-2.5-flash\\\",\\n    \\\"gpt-4o-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\n\\n# ── Paths ────────────────────────────────────────────────────────────\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_DIR = PLAN001_DIR / \\\"mi_matrix\\\"\\n\\nSTEP2V3_CKPT = RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\"\\nTAXONOMY_CKPT = RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\"\\n\\n\\ndef load_local_clean_scores():\\n    \\\"\\\"\\\"Load clean scores for 6 local models from checkpoint files.\\\"\\\"\\\"\\n    scores = {}\\n    for ckpt_path in [STEP2V3_CKPT, TAXONOMY_CKPT]:\\n        if not ckpt_path.exists():\\n            logger.warning(f\\\"Checkpoint not found: {ckpt_path}\\\")\\n            continue\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        cs = data.get(\\\"clean_scores\\\", {})\\n        for ds in DATASETS:\\n            if ds not in cs:\\n                continue\\n            if ds not in scores:\\n                scores[ds] = {}\\n            for model_id, model_scores in cs[ds].items():\\n                if model_id in LOCAL_MODELS and model_id not in scores[ds]:\\n                    scores[ds][model_id] = model_scores\\n    return scores\\n\\n\\ndef load_api_clean_scores():\\n    \\\"\\\"\\\"Load clean scores for 9 API models from individual score files.\\\"\\\"\\\"\\n    scores = {}\\n    for model_id in API_MODELS:\\n        for ds in DATASETS:\\n            fname = f\\\"{model_id}__{ds}__clean.json\\\"\\n            fpath = SCORES_DIR / fname\\n            if not fpath.exists():\\n                logger.warning(f\\\"API score file not found: {fpath}\\\")\\n                continue\\n            with open(fpath) as f:\\n                data = json.load(f)\\n            if ds not in scores:\\n                scores[ds] = {}\\n            scores[ds][model_id] = data.get(\\\"scores\\\", [])\\n    return scores\\n\\n\\ndef merge_clean_scores(local_scores, api_scores):\\n    \\\"\\\"\\\"Merge local and API clean scores into unified dict.\\\"\\\"\\\"\\n    merged = {}\\n    for ds in DATASETS:\\n        merged[ds] = {}\\n        for src in [local_scores, api_scores]:\\n            if ds in src:\\n                merged[ds].update(src[ds])\\n    return merged\\n\\n\\ndef extract_winner_vector(score_list):\\n    \\\"\\\"\\\"Extract winner labels from score list, normalizing to A/B/C/tie.\\\"\\\"\\\"\\n    winners = []\\n    for s in score_list:\\n        w = s.get(\\\"winner\\\", \\\"tie\\\") if isinstance(s, dict) else \\\"tie\\\"\\n        winners.append(w)\\n    return winners\\n\\n\\ndef compute_pairwise_mi(winners_i, winners_j):\\n    \\\"\\\"\\\"Compute mutual information between two winner vectors.\\\"\\\"\\\"\\n    n = min(len(winners_i), len(winners_j))\\n    if n == 0:\\n        return 0.0\\n    return mutual_info_score(winners_i[:n], winners_j[:n])\\n\\n\\ndef build_mi_matrix(clean_scores, dataset):\\n    \\\"\\\"\\\"Build 15x15 MI matrix for a dataset.\\\"\\\"\\\"\\n    ds_scores = clean_scores.get(dataset, {})\\n    n_models = len(ALL_MODELS)\\n    mi_mat = np.zeros((n_models, n_models))\\n\\n    winner_vectors = {}\\n    for i, model_id in enumerate(ALL_MODELS):\\n        if model_id in ds_scores:\\n            winner_vectors[i] = extract_winner_vector(ds_scores[model_id])\\n        else:\\n            logger.warning(f\\\"No clean scores for {model_id} on {dataset}\\\")\\n\\n    for i in range(n_m\\n\\n... [截断: 输出过长，省略 666 字符] ...\\n\\n return keff / K\\n\\n\\ndef compute_all_panel_keffs(mi_matrix, dataset):\\n    \\\"\\\"\\\"Compute K_eff for all C(15,3)=455 panels.\\\"\\\"\\\"\\n    n_models = len(ALL_MODELS)\\n    idx_to_model = {i: m for i, m in enumerate(ALL_MODELS)}\\n    panels = {}\\n\\n    for combo in itertools.combinations(range(n_models), 3):\\n        model_ids = [idx_to_model[i] for i in combo]\\n        panel_key = \\\"|\\\".join(model_ids)\\n        keff = mi_based_keff(mi_matrix, list(combo))\\n\\n        mi_pairs = {}\\n        for a, b in itertools.combinations(combo, 2):\\n            pair_key = f\\\"{idx_to_model[a]}|{idx_to_model[b]}\\\"\\n            mi_pairs[pair_key] = float(mi_matrix[a, b])\\n\\n        panels[panel_key] = {\\n            \\\"models\\\": model_ids,\\n            \\\"keff\\\": float(keff),\\n            \\\"mi_pairs\\\": mi_pairs,\\n        }\\n\\n    return panels\\n\\n\\ndef main():\\n    logger.info(\\\"=== Plan 001 Step 3: MI Matrix Computation ===\\\")\\n\\n    local_scores = load_local_clean_scores()\\n    api_scores = load_api_clean_scores()\\n    clean_scores = merge_clean_scores(local_scores, api_scores)\\n\\n    for ds in DATASETS:\\n        available = list(clean_scores.get(ds, {}).keys())\\n        missing = [m for m in ALL_MODELS if m not in available]\\n        logger.info(f\\\"  {ds}: {len(available)}/{len(ALL_MODELS)} models available\\\")\\n        if missing:\\n            logger.warning(f\\\"  {ds}: missing models: {missing}\\\")\\n\\n    available_count = sum(\\n        1 for ds in DATASETS\\n        for m in ALL_MODELS\\n        if m in clean_scores.get(ds, {})\\n    )\\n    total_needed = len(DATASETS) * len(ALL_MODELS)\\n    if available_count < total_needed:\\n        logger.warning(\\n            f\\\"Only {available_count}/{total_needed} model×dataset combos available. \\\"\\n            f\\\"MI matrix will have zeros for missing pairs.\\\"\\n        )\\n\\n    mi_matrices = {}\\n    keff_per_panel = {}\\n\\n    for ds in DATASETS:\\n        logger.info(f\\\"\\\\n--- Computing MI matrix for {ds} ---\\\")\\n        mi_mat = build_mi_matrix(clean_scores, ds)\\n        mi_matrices[ds] = mi_mat.tolist()\\n\\n        nonzero = np.count_nonzero(mi_mat)\\n        max_possible = len(ALL_MODELS) * (len(ALL_MODELS) - 1)\\n        logger.info(f\\\"  MI matrix: {nonzero}/{max_possible} non-zero entries\\\")\\n        if nonzero > 0:\\n            upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\\n            upper_nz = upper[upper > 0]\\n            if len(upper_nz) > 0:\\n                logger.info(\\n                    f\\\"  MI range: [{upper_nz.min():.4f}, {upper_nz.max():.4f}], \\\"\\n                    f\\\"mean={upper_nz.mean():.4f}\\\"\\n                )\\n\\n        logger.info(f\\\"  Computing K_eff for all C(15,3)=455 panels on {ds}...\\\")\\n        panels = compute_all_panel_keffs(mi_mat, ds)\\n        keff_per_panel[ds] = panels\\n\\n        keff_values = [p[\\\"keff\\\"] for p in panels.values()]\\n        logger.info(\\n            f\\\"  K_eff range: [{min(keff_values):.3f}, {max(keff_values):.3f}], \\\"\\n            f\\\"mean={np.mean(keff_values):.3f}\\\"\\n        )\\n\\n    MI_DIR.mkdir(parents=True, exist_ok=True)\\n    output = {\\n        \\\"models\\\": ALL_MODELS,\\n        \\\"mi_matrix\\\": mi_matrices,\\n        \\\"keff_per_panel\\\": keff_per_panel,\\n    }\\n    output_path = MI_DIR / \\\"mi_matrix_15models.json\\\"\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2, ensure_ascii=False)\\n    logger.info(f\\\"\\\\nSaved MI matrix to {output_path}\\\")\\n\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(\\\"MI MATRIX SUMMARY\\\")\\n    print(\\\"=\\\" * 70)\\n    for ds in DATASETS:\\n        mi_mat = np.array(mi_matrices[ds])\\n        upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\\n        n_computed = np.count_nonzero(upper)\\n        print(f\\\"\\\\n{ds}:\\\")\\n        print(f\\\"  Pairwise MI computed: {n_computed}/105\\\")\\n        if n_computed > 0:\\n            nz = upper[upper > 0]\\n            print(f\\\"  MI range: [{nz.min():.4f}, {nz.max():.4f}]\\\")\\n            print(f\\\"  MI mean:  {nz.mean():.4f}\\\")\\n        keffs = [p[\\\"keff\\\"] for p in keff_per_panel[ds].values()]\\n        print(f\\\"  K_eff (455 panels): [{min(keffs):.3f}, {max(keffs):.3f}], mean={np.mean(keffs):.3f}\\\")\\n    print(\\\"=\\\" * 70)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.98}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UoWAxAZ3jmFnv2gWKKtCJd`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "a51902ef-0be0-4430-9247-443d4f3cef1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gnr9tuWwdVbM3PtFVZEq14",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 934,
      "cache_read_input_tokens": 24835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 934
      },
      "output_tokens": 52,
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

_source line 13 · 2026-05-22T14:56:11.419Z_

<details><summary>↩ Tool result · `toolu_01BZ6U5dYZDWf4yrspZ9VhLD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Plan 001: K_eff vs eta_max confound diagnosis across all C(15,3) panels.\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport itertools\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nfrom pathlib import Path\\nfrom scipy import stats\\n\\nfrom src.utils import setup_logging\\n\\nlogger = setup_logging(\\\"plan001_confound\\\")\\n\\n# ── Model lists ──────────────────────────────────────────────────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4\\\", \\\"gpt-5.5\\\", \\\"gemini-2.5-pro\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4\\\", \\\"gpt-4o\\\", \\\"gemini-2.5-flash\\\",\\n    \\\"gpt-4o-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\nATTACKS = [\\n    \\\"prompt_injection\\\", \\\"sycophancy\\\", \\\"score_manipulation\\\",\\n    \\\"verbosity_bias\\\", \\\"position_bias\\\", \\\"authority_bias\\\",\\n]\\n\\n# ── Paths ────────────────────────────────────────────────────────────\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_MATRIX_PATH = PLAN001_DIR / \\\"mi_matrix\\\" / \\\"mi_matrix_15models.json\\\"\\n\\nSTEP2V3_CKPT = RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\"\\nTAXONOMY_CKPT = RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\"\\n\\nLOCAL_ATTACK_CKPT = {\\n    \\\"prompt_injection\\\": STEP2V3_CKPT,\\n    \\\"sycophancy\\\": STEP2V3_CKPT,\\n    \\\"score_manipulation\\\": STEP2V3_CKPT,\\n    \\\"verbosity_bias\\\": TAXONOMY_CKPT,\\n    \\\"position_bias\\\": TAXONOMY_CKPT,\\n    \\\"authority_bias\\\": TAXONOMY_CKPT,\\n}\\n\\n\\ndef _invert_winners(scores):\\n    \\\"\\\"\\\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\\\"\\\"\\\"\\n    swap = {\\\"A\\\": \\\"B\\\", \\\"B\\\": \\\"A\\\", \\\"tie\\\": \\\"tie\\\"}\\n    return [{**s, \\\"winner\\\": swap.get(s.get(\\\"winner\\\", \\\"tie\\\"), \\\"tie\\\")} for s in scores]\\n\\n\\ndef compute_asr_from_scores(clean_scores, attacked_scores, pairs):\\n    \\\"\\\"\\\"Compute individual judge ASR: fraction of clean-correct flipped by attack.\\\"\\\"\\\"\\n    n_flips = 0\\n    n_total = 0\\n    for clean, attacked, pair in zip(clean_scores, attacked_scores, pairs):\\n        gt = pair.get(\\\"ground_truth_winner\\\")\\n        cw = clean.get(\\\"winner\\\") if isinstance(clean, dict) else None\\n        aw = attacked.get(\\\"winner\\\") if isinstance(attacked, dict) else None\\n        if cw == gt:\\n            n_total += 1\\n            if aw != gt:\\n                n_flips += 1\\n    return n_flips / max(n_total, 1)\\n\\n\\ndef load_local_individual_asr():\\n    \\\"\\\"\\\"Load per-model ASR for local models from checkpoint files.\\n\\n    Returns: {dataset: {attack: {model_id: asr}}}\\n    \\\"\\\"\\\"\\n    asr_data = {}\\n    ckpt_cache = {}\\n\\n    for attack in ATTACKS:\\n        ckpt_path = LOCAL_ATTACK_CKPT[attack]\\n        if str(ckpt_path) not in ckpt_cache:\\n            if not ckpt_path.exists():\\n                logger.warning(f\\\"Checkpoint not found: {ckpt_path}\\\")\\n                continue\\n            with open(ckpt_path) as f:\\n                ckpt_cache[str(ckpt_path)] = json.load(f)\\n        data = ckpt_cache[str(ckpt_path)]\\n\\n        for ds in DATASETS:\\n            if ds not in asr_data:\\n                asr_data[ds] = {}\\n            if attack not in asr_data[ds]:\\n                asr_data[ds][attack] = {}\\n\\n            clean_all = data.get(\\\"clean_scores\\\", {}).get(ds, {})\\n            atk_all = data.get(\\\"attacked_scores\\\", {}).get(ds, {}).get(attack, {})\\n            pairs = data.get(\\\"pairs\\\", {}).get(ds, [])\\n\\n            if not pairs:\\n                logger.warning(f\\\"No pairs for {ds} in {ckpt_path.name}\\\")\\n                continue\\n\\n            for model_id in LOCAL_MODELS:\\n                if model_id not in clean_all or model_id not in atk_all:\\n                    continue\\n                atk_scores = atk_all[model_id]\\n                if attack == \\\"position_bias\\\":\\n                    atk_scores = _invert_winners(atk_scores)\\n                asr = compute_asr_from_scores(\\n      \\n\\n... [截断: 输出过长，省略 6681 字符] ...\\n\\nfs[mask]\\n            e_sub = eta_maxs[mask]\\n            label = PANEL_LABELS[pt] if pt not in plotted_labels else None\\n            ax.scatter(\\n                k_sub, e_sub,\\n                c=PANEL_COLORS[pt],\\n                alpha=0.4, s=12, label=label,\\n                edgecolors=\\\"none\\\",\\n            )\\n            plotted_labels.add(pt)\\n\\n        verdict_color = {\\n            \\\"CONFOUND_SEVERE\\\": \\\"#e74c3c\\\",\\n            \\\"CONFOUND_MODERATE\\\": \\\"#e67e22\\\",\\n            \\\"CONFOUND_BROKEN\\\": \\\"#27ae60\\\",\\n        }.get(verdict, \\\"#333\\\")\\n\\n        ax.set_title(\\n            f\\\"{cond_key}\\\\nr = {r:.3f}  [{verdict}]\\\",\\n            fontsize=9,\\n            color=verdict_color,\\n        )\\n        ax.set_xlabel(\\\"K_eff\\\", fontsize=8)\\n        ax.set_ylabel(\\\"eta_max (individual ASR)\\\", fontsize=8)\\n        ax.tick_params(labelsize=7)\\n\\n        if len(keffs) >= 3 and np.std(keffs) > 1e-10:\\n            z = np.polyfit(keffs, eta_maxs, 1)\\n            x_line = np.linspace(keffs.min(), keffs.max(), 50)\\n            ax.plot(x_line, np.polyval(z, x_line), \\\"k--\\\", alpha=0.3, linewidth=1)\\n\\n        if idx == 0:\\n            ax.legend(fontsize=6, loc=\\\"best\\\", framealpha=0.7)\\n\\n    for idx in range(len(valid_conds), nrows * ncols):\\n        row, col = divmod(idx, ncols)\\n        axes[row][col].set_visible(False)\\n\\n    fig.suptitle(\\n        \\\"K_eff vs eta_max Confound Diagnosis (15 models, K=3 panels)\\\",\\n        fontsize=12, y=1.02,\\n    )\\n    plt.tight_layout()\\n    plt.savefig(output_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    logger.info(f\\\"Scatter plot saved to {output_path}\\\")\\n\\n\\ndef main():\\n    logger.info(\\\"=== Plan 001: K_eff vs eta_max Confound Diagnosis ===\\\")\\n\\n    logger.info(\\\"Loading MI matrix...\\\")\\n    mi_data = load_mi_matrix()\\n\\n    logger.info(\\\"Loading individual ASR data...\\\")\\n    local_asr = load_local_individual_asr()\\n    api_asr = load_api_individual_asr()\\n    asr_data = merge_asr(local_asr, api_asr)\\n\\n    for ds in DATASETS:\\n        for attack in ATTACKS:\\n            models_with_asr = list(asr_data.get(ds, {}).get(attack, {}).keys())\\n            logger.info(f\\\"  {ds}__{attack}: {len(models_with_asr)} models\\\")\\n\\n    logger.info(\\\"\\\\nRunning confound analysis...\\\")\\n    conditions = run_confound_analysis(mi_data, asr_data)\\n\\n    scatter_path = PLAN001_DIR / \\\"confound_scatter.png\\\"\\n    plot_scatter_grid(conditions, scatter_path)\\n\\n    r_values = [\\n        v[\\\"pearson_r\\\"] for v in conditions.values()\\n        if v.get(\\\"pearson_r\\\") is not None\\n    ]\\n    if r_values:\\n        mean_r = float(np.mean(r_values))\\n        if mean_r < -0.7:\\n            overall = \\\"CONFOUND_SEVERE\\\"\\n        elif mean_r <= -0.5:\\n            overall = \\\"CONFOUND_MODERATE\\\"\\n        else:\\n            overall = \\\"CONFOUND_BROKEN\\\"\\n    else:\\n        mean_r = None\\n        overall = \\\"INSUFFICIENT_DATA\\\"\\n\\n    output_conditions = {}\\n    for k, v in conditions.items():\\n        output_conditions[k] = {\\n            \\\"pearson_r\\\": v.get(\\\"pearson_r\\\"),\\n            \\\"p_value\\\": v.get(\\\"p_value\\\"),\\n            \\\"verdict\\\": v.get(\\\"verdict\\\"),\\n            \\\"n_panels\\\": v.get(\\\"n_panels\\\"),\\n            \\\"n_models_with_asr\\\": v.get(\\\"n_models_with_asr\\\"),\\n        }\\n\\n    output = {\\n        \\\"conditions\\\": output_conditions,\\n        \\\"scatter_plots\\\": str(scatter_path),\\n        \\\"overall_verdict\\\": overall,\\n        \\\"mean_r\\\": mean_r,\\n    }\\n\\n    output_path = PLAN001_DIR / \\\"confound_diagnosis.json\\\"\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2, ensure_ascii=False)\\n    logger.info(f\\\"\\\\nDiagnosis saved to {output_path}\\\")\\n\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(\\\"CONFOUND DIAGNOSIS SUMMARY\\\")\\n    print(\\\"=\\\" * 70)\\n    for cond_key, cond in sorted(output_conditions.items()):\\n        r = cond[\\\"pearson_r\\\"]\\n        v = cond[\\\"verdict\\\"]\\n        n = cond[\\\"n_panels\\\"]\\n        r_str = f\\\"{r:.3f}\\\" if r is not None else \\\"N/A\\\"\\n        print(f\\\"  {cond_key:40s}  r={r_str:>7s}  {v:20s}  ({n} panels)\\\")\\n    print(f\\\"\\\\n  Overall: mean_r={'N/A' if mean_r is None else f'{mean_r:.3f}'}, verdict={overall}\\\")\\n    print(\\\"=\\\" * 70)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "034a5d57-624f-44f6-aeb4-7dcd7184b251",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Plan 001: K_eff vs eta_max confound diagnosis across all C(15,3) panels.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport os\\\\nos.environ[\\\\\\\"HF_HOME\\\\\\\"] = \\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"\\\\n\\\\nimport sys\\\\nsys.path.insert(0, \\\\\\\"/root/cert_manip_resist_eval\\\\\\\")\\\\n\\\\nimport json\\\\nimport itertools\\\\nimport numpy as np\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\nimport matplotlib.pyplot as plt\\\\nfrom pathlib import Path\\\\nfrom scipy import stats\\\\n\\\\nfrom src.utils import setup_logging\\\\n\\\\nlogger = setup_logging(\\\\\\\"plan001_confound\\\\\\\")\\\\n\\\\n# ── Model lists ──────────────────────────────────────────────────────\\\\nLOCAL_MODELS = [\\\\n    \\\\\\\"qwen2.5-72b\\\\\\\", \\\\\\\"llama3.1-70b\\\\\\\", \\\\\\\"mistral-large\\\\\\\",\\\\n    \\\\\\\"qwen2.5-32b\\\\\\\", \\\\\\\"qwen2.5-14b\\\\\\\", \\\\\\\"llama3.1-8b\\\\\\\",\\\\n]\\\\nAPI_MODELS = [\\\\n    \\\\\\\"claude-opus-4\\\\\\\", \\\\\\\"gpt-5.5\\\\\\\", \\\\\\\"gemini-2.5-pro\\\\\\\", \\\\\\\"gpt-4.1\\\\\\\",\\\\n    \\\\\\\"claude-sonnet-4\\\\\\\", \\\\\\\"gpt-4o\\\\\\\", \\\\\\\"gemini-2.5-flash\\\\\\\",\\\\n    \\\\\\\"gpt-4o-mini\\\\\\\", \\\\\\\"claude-3-haiku\\\\\\\",\\\\n]\\\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\\\nDATASETS = [\\\\\\\"mmlu\\\\\\\", \\\\\\\"arc_challenge\\\\\\\"]\\\\nATTACKS = [\\\\n    \\\\\\\"prompt_injection\\\\\\\", \\\\\\\"sycophancy\\\\\\\", \\\\\\\"score_manipulation\\\\\\\",\\\\n    \\\\\\\"verbosity_bias\\\\\\\", \\\\\\\"position_bias\\\\\\\", \\\\\\\"authority_bias\\\\\\\",\\\\n]\\\\n\\\\n# ── Paths ────────────────────────────────────────────────────────────\\\\nRESULTS_DIR = Path(\\\\\\\"/root/cert_manip_resist_eval/artifacts/results\\\\\\\")\\\\nPLAN001_DIR = RESULTS_DIR / \\\\\\\"plan001\\\\\\\"\\\\nSCORES_DIR = PLAN001_DIR / \\\\\\\"individual_scores\\\\\\\"\\\\nMI_MATRIX_PATH = PLAN001_DIR / \\\\\\\"mi_matrix\\\\\\\" / \\\\\\\"mi_matrix_15models.json\\\\\\\"\\\\n\\\\nSTEP2V3_CKPT = RESULTS_DIR / \\\\\\\"_step2v3_checkpoint.json\\\\\\\"\\\\nTAXONOMY_CKPT = RESULTS_DIR / \\\\\\\"_taxonomy_checkpoint.json\\\\\\\"\\\\n\\\\nLOCAL_ATTACK_CKPT = {\\\\n    \\\\\\\"prompt_injection\\\\\\\": STEP2V3_CKPT,\\\\n    \\\\\\\"sycophancy\\\\\\\": STEP2V3_CKPT,\\\\n    \\\\\\\"score_manipulation\\\\\\\": STEP2V3_CKPT,\\\\n    \\\\\\\"verbosity_bias\\\\\\\": TAXONOMY_CKPT,\\\\n    \\\\\\\"position_bias\\\\\\\": TAXONOMY_CKPT,\\\\n    \\\\\\\"authority_bias\\\\\\\": TAXONOMY_CKPT,\\\\n}\\\\n\\\\n\\\\ndef _invert_winners(scores):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    swap = {\\\\\\\"A\\\\\\\": \\\\\\\"B\\\\\\\", \\\\\\\"B\\\\\\\": \\\\\\\"A\\\\\\\", \\\\\\\"tie\\\\\\\": \\\\\\\"tie\\\\\\\"}\\\\n    return [{**s, \\\\\\\"winner\\\\\\\": swap.get(s.get(\\\\\\\"winner\\\\\\\", \\\\\\\"tie\\\\\\\"), \\\\\\\"tie\\\\\\\")} for s in scores]\\\\n\\\\n\\\\ndef compute_asr_from_scores(clean_scores, attacked_scores, pairs):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Compute individual judge ASR: fraction of clean-correct flipped by attack.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    n_flips = 0\\\\n    n_total = 0\\\\n    for clean, attacked, pair in zip(clean_scores, attacked_scores, pairs):\\\\n        gt = pair.get(\\\\\\\"ground_truth_winner\\\\\\\")\\\\n        cw = clean.get(\\\\\\\"winner\\\\\\\") if isinstance(clean, dict) else None\\\\n        aw = attacked.get(\\\\\\\"winner\\\\\\\") if isinstance(attacked, dict) else None\\\\n        if cw == gt:\\\\n            n_total += 1\\\\n            if aw != gt:\\\\n                n_flips += 1\\\\n    return n_flips / max(n_total, 1)\\\\n\\\\n\\\\ndef load_local_individual_asr():\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load per-model ASR for local models from checkpoint files.\\\\n\\\\n    Returns: {dataset: {attack: {model_id: asr}}}\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    asr_data = {}\\\\n    ckpt_cache = {}\\\\n\\\\n    for attack in ATTACKS:\\\\n        ckpt_path = LOCAL_ATTACK_CKPT[attack]\\\\n        if str(ckpt_path) not in ckpt_cache:\\\\n            if not ckpt_path.exists():\\\\n                logger.warning(f\\\\\\\"Checkpoint not found: {ckpt_path}\\\\\\\")\\\\n                continue\\\\n            with open(ckpt_path) as f:\\\\n                ckpt_cache[str(ckpt_path)] = json.load(f)\\\\n        data = ckpt_cache[str(ckpt_path)]\\\\n\\\\n        for ds in DATASETS:\\\\n            if ds not in asr_data:\\\\n                asr_data[ds] = {}\\\\n            if attack not in asr_data[ds]:\\\\n                asr_data[ds][attack] = {}\\\\n\\\\n            clean_all = data.get(\\\\\\\"clean_scores\\\\\\\", {}).get(ds, {})\\\\n            atk_all = data.get(\\\\\\\"attacked_scores\\\\\\\", {}).get(ds, {}).get(attack, {})\\\\n            pairs = data.get(\\\\\\\"pairs\\\\\\\", {}).get(ds, [])\\\\n\\\\n            if not pairs:\\\\n                logger.warning(f\\\\\\\"No pairs for {ds} in {ckpt_path.name}\\\\\\\")\\\\n                continue\\\\n\\\\n            for model_id in LOCAL_MODELS:\\\\n                if model_id not in clean_all or model_id not in atk_all:\\\\n                    continue\\\\n                atk_scores = atk_all[model_id]\\\\n                if attack == \\\\\\\"position_bias\\\\\\\":\\\\n                    atk_scores = _invert_winners(atk_scores)\\\\n                asr = compute_asr_from_scores(\\\\n      \\\\n\\\\n... [截断: 输出过长，省略 6681 字符] ...\\\\n\\\\nfs[mask]\\\\n            e_sub = eta_maxs[mask]\\\\n            label = PANEL_LABELS[pt] if pt not in plotted_labels else None\\\\n            ax.scatter(\\\\n                k_sub, e_sub,\\\\n                c=PANEL_COLORS[pt],\\\\n                alpha=0.4, s=12, label=label,\\\\n                edgecolors=\\\\\\\"none\\\\\\\",\\\\n            )\\\\n            plotted_labels.add(pt)\\\\n\\\\n        verdict_color = {\\\\n            \\\\\\\"CONFOUND_SEVERE\\\\\\\": \\\\\\\"#e74c3c\\\\\\\",\\\\n            \\\\\\\"CONFOUND_MODERATE\\\\\\\": \\\\\\\"#e67e22\\\\\\\",\\\\n            \\\\\\\"CONFOUND_BROKEN\\\\\\\": \\\\\\\"#27ae60\\\\\\\",\\\\n        }.get(verdict, \\\\\\\"#333\\\\\\\")\\\\n\\\\n        ax.set_title(\\\\n            f\\\\\\\"{cond_key}\\\\\\\\nr = {r:.3f}  [{verdict}]\\\\\\\",\\\\n            fontsize=9,\\\\n            color=verdict_color,\\\\n        )\\\\n        ax.set_xlabel(\\\\\\\"K_eff\\\\\\\", fontsize=8)\\\\n        ax.set_ylabel(\\\\\\\"eta_max (individual ASR)\\\\\\\", fontsize=8)\\\\n        ax.tick_params(labelsize=7)\\\\n\\\\n        if len(keffs) >= 3 and np.std(keffs) > 1e-10:\\\\n            z = np.polyfit(keffs, eta_maxs, 1)\\\\n            x_line = np.linspace(keffs.min(), keffs.max(), 50)\\\\n            ax.plot(x_line, np.polyval(z, x_line), \\\\\\\"k--\\\\\\\", alpha=0.3, linewidth=1)\\\\n\\\\n        if idx == 0:\\\\n            ax.legend(fontsize=6, loc=\\\\\\\"best\\\\\\\", framealpha=0.7)\\\\n\\\\n    for idx in range(len(valid_conds), nrows * ncols):\\\\n        row, col = divmod(idx, ncols)\\\\n        axes[row][col].set_visible(False)\\\\n\\\\n    fig.suptitle(\\\\n        \\\\\\\"K_eff vs eta_max Confound Diagnosis (15 models, K=3 panels)\\\\\\\",\\\\n        fontsize=12, y=1.02,\\\\n    )\\\\n    plt.tight_layout()\\\\n    plt.savefig(output_path, dpi=150, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close()\\\\n    logger.info(f\\\\\\\"Scatter plot saved to {output_path}\\\\\\\")\\\\n\\\\n\\\\ndef main():\\\\n    logger.info(\\\\\\\"=== Plan 001: K_eff vs eta_max Confound Diagnosis ===\\\\\\\")\\\\n\\\\n    logger.info(\\\\\\\"Loading MI matrix...\\\\\\\")\\\\n    mi_data = load_mi_matrix()\\\\n\\\\n    logger.info(\\\\\\\"Loading individual ASR data...\\\\\\\")\\\\n    local_asr = load_local_individual_asr()\\\\n    api_asr = load_api_individual_asr()\\\\n    asr_data = merge_asr(local_asr, api_asr)\\\\n\\\\n    for ds in DATASETS:\\\\n        for attack in ATTACKS:\\\\n            models_with_asr = list(asr_data.get(ds, {}).get(attack, {}).keys())\\\\n            logger.info(f\\\\\\\"  {ds}__{attack}: {len(models_with_asr)} models\\\\\\\")\\\\n\\\\n    logger.info(\\\\\\\"\\\\\\\\nRunning confound analysis...\\\\\\\")\\\\n    conditions = run_confound_analysis(mi_data, asr_data)\\\\n\\\\n    scatter_path = PLAN001_DIR / \\\\\\\"confound_scatter.png\\\\\\\"\\\\n    plot_scatter_grid(conditions, scatter_path)\\\\n\\\\n    r_values = [\\\\n        v[\\\\\\\"pearson_r\\\\\\\"] for v in conditions.values()\\\\n        if v.get(\\\\\\\"pearson_r\\\\\\\") is not None\\\\n    ]\\\\n    if r_values:\\\\n        mean_r = float(np.mean(r_values))\\\\n        if mean_r < -0.7:\\\\n            overall = \\\\\\\"CONFOUND_SEVERE\\\\\\\"\\\\n        elif mean_r <= -0.5:\\\\n            overall = \\\\\\\"CONFOUND_MODERATE\\\\\\\"\\\\n        else:\\\\n            overall = \\\\\\\"CONFOUND_BROKEN\\\\\\\"\\\\n    else:\\\\n        mean_r = None\\\\n        overall = \\\\\\\"INSUFFICIENT_DATA\\\\\\\"\\\\n\\\\n    output_conditions = {}\\\\n    for k, v in conditions.items():\\\\n        output_conditions[k] = {\\\\n            \\\\\\\"pearson_r\\\\\\\": v.get(\\\\\\\"pearson_r\\\\\\\"),\\\\n            \\\\\\\"p_value\\\\\\\": v.get(\\\\\\\"p_value\\\\\\\"),\\\\n            \\\\\\\"verdict\\\\\\\": v.get(\\\\\\\"verdict\\\\\\\"),\\\\n            \\\\\\\"n_panels\\\\\\\": v.get(\\\\\\\"n_panels\\\\\\\"),\\\\n            \\\\\\\"n_models_with_asr\\\\\\\": v.get(\\\\\\\"n_models_with_asr\\\\\\\"),\\\\n        }\\\\n\\\\n    output = {\\\\n        \\\\\\\"conditions\\\\\\\": output_conditions,\\\\n        \\\\\\\"scatter_plots\\\\\\\": str(scatter_path),\\\\n        \\\\\\\"overall_verdict\\\\\\\": overall,\\\\n        \\\\\\\"mean_r\\\\\\\": mean_r,\\\\n    }\\\\n\\\\n    output_path = PLAN001_DIR / \\\\\\\"confound_diagnosis.json\\\\\\\"\\\\n    with open(output_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(output, f, indent=2, ensure_ascii=False)\\\\n    logger.info(f\\\\\\\"\\\\\\\\nDiagnosis saved to {output_path}\\\\\\\")\\\\n\\\\n    print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 70)\\\\n    print(\\\\\\\"CONFOUND DIAGNOSIS SUMMARY\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n    for cond_key, cond in sorted(output_conditions.items()):\\\\n        r = cond[\\\\\\\"pearson_r\\\\\\\"]\\\\n        v = cond[\\\\\\\"verdict\\\\\\\"]\\\\n        n = cond[\\\\\\\"n_panels\\\\\\\"]\\\\n        r_str = f\\\\\\\"{r:.3f}\\\\\\\" if r is not None else \\\\\\\"N/A\\\\\\\"\\\\n        print(f\\\\\\\"  {cond_key:40s}  r={r_str:>7s}  {v:20s}  ({n} panels)\\\\\\\")\\\\n    print(f\\\\\\\"\\\\\\\\n  Overall: mean_r={'N/A' if mean_r is None else f'{mean_r:.3f}'}, verdict={overall}\\\\\\\")\\\\n    print(\\\\\\\"=\\\\\\\" * 70)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Plan 001: K_eff vs eta_max confound diagnosis across all C(15,3) panels.\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport itertools\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nfrom pathlib import Path\\nfrom scipy import stats\\n\\nfrom src.utils import setup_logging\\n\\nlogger = setup_logging(\\\"plan001_confound\\\")\\n\\n# ── Model lists ──────────────────────────────────────────────────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4\\\", \\\"gpt-5.5\\\", \\\"gemini-2.5-pro\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4\\\", \\\"gpt-4o\\\", \\\"gemini-2.5-flash\\\",\\n    \\\"gpt-4o-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\nATTACKS = [\\n    \\\"prompt_injection\\\", \\\"sycophancy\\\", \\\"score_manipulation\\\",\\n    \\\"verbosity_bias\\\", \\\"position_bias\\\", \\\"authority_bias\\\",\\n]\\n\\n# ── Paths ────────────────────────────────────────────────────────────\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_MATRIX_PATH = PLAN001_DIR / \\\"mi_matrix\\\" / \\\"mi_matrix_15models.json\\\"\\n\\nSTEP2V3_CKPT = RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\"\\nTAXONOMY_CKPT = RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\"\\n\\nLOCAL_ATTACK_CKPT = {\\n    \\\"prompt_injection\\\": STEP2V3_CKPT,\\n    \\\"sycophancy\\\": STEP2V3_CKPT,\\n    \\\"score_manipulation\\\": STEP2V3_CKPT,\\n    \\\"verbosity_bias\\\": TAXONOMY_CKPT,\\n    \\\"position_bias\\\": TAXONOMY_CKPT,\\n    \\\"authority_bias\\\": TAXONOMY_CKPT,\\n}\\n\\n\\ndef _invert_winners(scores):\\n    \\\"\\\"\\\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\\\"\\\"\\\"\\n    swap = {\\\"A\\\": \\\"B\\\", \\\"B\\\": \\\"A\\\", \\\"tie\\\": \\\"tie\\\"}\\n    return [{**s, \\\"winner\\\": swap.get(s.get(\\\"winner\\\", \\\"tie\\\"), \\\"tie\\\")} for s in scores]\\n\\n\\ndef compute_asr_from_scores(clean_scores, attacked_scores, pairs):\\n    \\\"\\\"\\\"Compute individual judge ASR: fraction of clean-correct flipped by attack.\\\"\\\"\\\"\\n    n_flips = 0\\n    n_total = 0\\n    for clean, attacked, pair in zip(clean_scores, attacked_scores, pairs):\\n        gt = pair.get(\\\"ground_truth_winner\\\")\\n        cw = clean.get(\\\"winner\\\") if isinstance(clean, dict) else None\\n        aw = attacked.get(\\\"winner\\\") if isinstance(attacked, dict) else None\\n        if cw == gt:\\n            n_total += 1\\n            if aw != gt:\\n                n_flips += 1\\n    return n_flips / max(n_total, 1)\\n\\n\\ndef load_local_individual_asr():\\n    \\\"\\\"\\\"Load per-model ASR for local models from checkpoint files.\\n\\n    Returns: {dataset: {attack: {model_id: asr}}}\\n    \\\"\\\"\\\"\\n    asr_data = {}\\n    ckpt_cache = {}\\n\\n    for attack in ATTACKS:\\n        ckpt_path = LOCAL_ATTACK_CKPT[attack]\\n        if str(ckpt_path) not in ckpt_cache:\\n            if not ckpt_path.exists():\\n                logger.warning(f\\\"Checkpoint not found: {ckpt_path}\\\")\\n                continue\\n            with open(ckpt_path) as f:\\n                ckpt_cache[str(ckpt_path)] = json.load(f)\\n        data = ckpt_cache[str(ckpt_path)]\\n\\n        for ds in DATASETS:\\n            if ds not in asr_data:\\n                asr_data[ds] = {}\\n            if attack not in asr_data[ds]:\\n                asr_data[ds][attack] = {}\\n\\n            clean_all = data.get(\\\"clean_scores\\\", {}).get(ds, {})\\n            atk_all = data.get(\\\"attacked_scores\\\", {}).get(ds, {}).get(attack, {})\\n            pairs = data.get(\\\"pairs\\\", {}).get(ds, [])\\n\\n            if not pairs:\\n                logger.warning(f\\\"No pairs for {ds} in {ckpt_path.name}\\\")\\n                continue\\n\\n            for model_id in LOCAL_MODELS:\\n                if model_id not in clean_all or model_id not in atk_all:\\n                    continue\\n                atk_scores = atk_all[model_id]\\n                if attack == \\\"position_bias\\\":\\n                    atk_scores = _invert_winners(atk_scores)\\n                asr = compute_asr_from_scores(\\n      \\n\\n... [截断: 输出过长，省略 6681 字符] ...\\n\\nfs[mask]\\n            e_sub = eta_maxs[mask]\\n            label = PANEL_LABELS[pt] if pt not in plotted_labels else None\\n            ax.scatter(\\n                k_sub, e_sub,\\n                c=PANEL_COLORS[pt],\\n                alpha=0.4, s=12, label=label,\\n                edgecolors=\\\"none\\\",\\n            )\\n            plotted_labels.add(pt)\\n\\n        verdict_color = {\\n            \\\"CONFOUND_SEVERE\\\": \\\"#e74c3c\\\",\\n            \\\"CONFOUND_MODERATE\\\": \\\"#e67e22\\\",\\n            \\\"CONFOUND_BROKEN\\\": \\\"#27ae60\\\",\\n        }.get(verdict, \\\"#333\\\")\\n\\n        ax.set_title(\\n            f\\\"{cond_key}\\\\nr = {r:.3f}  [{verdict}]\\\",\\n            fontsize=9,\\n            color=verdict_color,\\n        )\\n        ax.set_xlabel(\\\"K_eff\\\", fontsize=8)\\n        ax.set_ylabel(\\\"eta_max (individual ASR)\\\", fontsize=8)\\n        ax.tick_params(labelsize=7)\\n\\n        if len(keffs) >= 3 and np.std(keffs) > 1e-10:\\n            z = np.polyfit(keffs, eta_maxs, 1)\\n            x_line = np.linspace(keffs.min(), keffs.max(), 50)\\n            ax.plot(x_line, np.polyval(z, x_line), \\\"k--\\\", alpha=0.3, linewidth=1)\\n\\n        if idx == 0:\\n            ax.legend(fontsize=6, loc=\\\"best\\\", framealpha=0.7)\\n\\n    for idx in range(len(valid_conds), nrows * ncols):\\n        row, col = divmod(idx, ncols)\\n        axes[row][col].set_visible(False)\\n\\n    fig.suptitle(\\n        \\\"K_eff vs eta_max Confound Diagnosis (15 models, K=3 panels)\\\",\\n        fontsize=12, y=1.02,\\n    )\\n    plt.tight_layout()\\n    plt.savefig(output_path, dpi=150, bbox_inches=\\\"tight\\\")\\n    plt.close()\\n    logger.info(f\\\"Scatter plot saved to {output_path}\\\")\\n\\n\\ndef main():\\n    logger.info(\\\"=== Plan 001: K_eff vs eta_max Confound Diagnosis ===\\\")\\n\\n    logger.info(\\\"Loading MI matrix...\\\")\\n    mi_data = load_mi_matrix()\\n\\n    logger.info(\\\"Loading individual ASR data...\\\")\\n    local_asr = load_local_individual_asr()\\n    api_asr = load_api_individual_asr()\\n    asr_data = merge_asr(local_asr, api_asr)\\n\\n    for ds in DATASETS:\\n        for attack in ATTACKS:\\n            models_with_asr = list(asr_data.get(ds, {}).get(attack, {}).keys())\\n            logger.info(f\\\"  {ds}__{attack}: {len(models_with_asr)} models\\\")\\n\\n    logger.info(\\\"\\\\nRunning confound analysis...\\\")\\n    conditions = run_confound_analysis(mi_data, asr_data)\\n\\n    scatter_path = PLAN001_DIR / \\\"confound_scatter.png\\\"\\n    plot_scatter_grid(conditions, scatter_path)\\n\\n    r_values = [\\n        v[\\\"pearson_r\\\"] for v in conditions.values()\\n        if v.get(\\\"pearson_r\\\") is not None\\n    ]\\n    if r_values:\\n        mean_r = float(np.mean(r_values))\\n        if mean_r < -0.7:\\n            overall = \\\"CONFOUND_SEVERE\\\"\\n        elif mean_r <= -0.5:\\n            overall = \\\"CONFOUND_MODERATE\\\"\\n        else:\\n            overall = \\\"CONFOUND_BROKEN\\\"\\n    else:\\n        mean_r = None\\n        overall = \\\"INSUFFICIENT_DATA\\\"\\n\\n    output_conditions = {}\\n    for k, v in conditions.items():\\n        output_conditions[k] = {\\n            \\\"pearson_r\\\": v.get(\\\"pearson_r\\\"),\\n            \\\"p_value\\\": v.get(\\\"p_value\\\"),\\n            \\\"verdict\\\": v.get(\\\"verdict\\\"),\\n            \\\"n_panels\\\": v.get(\\\"n_panels\\\"),\\n            \\\"n_models_with_asr\\\": v.get(\\\"n_models_with_asr\\\"),\\n        }\\n\\n    output = {\\n        \\\"conditions\\\": output_conditions,\\n        \\\"scatter_plots\\\": str(scatter_path),\\n        \\\"overall_verdict\\\": overall,\\n        \\\"mean_r\\\": mean_r,\\n    }\\n\\n    output_path = PLAN001_DIR / \\\"confound_diagnosis.json\\\"\\n    with open(output_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2, ensure_ascii=False)\\n    logger.info(f\\\"\\\\nDiagnosis saved to {output_path}\\\")\\n\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 70)\\n    print(\\\"CONFOUND DIAGNOSIS SUMMARY\\\")\\n    print(\\\"=\\\" * 70)\\n    for cond_key, cond in sorted(output_conditions.items()):\\n        r = cond[\\\"pearson_r\\\"]\\n        v = cond[\\\"verdict\\\"]\\n        n = cond[\\\"n_panels\\\"]\\n        r_str = f\\\"{r:.3f}\\\" if r is not None else \\\"N/A\\\"\\n        print(f\\\"  {cond_key:40s}  r={r_str:>7s}  {v:20s}  ({n} panels)\\\")\\n    print(f\\\"\\\\n  Overall: mean_r={'N/A' if mean_r is None else f'{mean_r:.3f}'}, verdict={overall}\\\")\\n    print(\\\"=\\\" * 70)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017Z34BFjee51BxRLNWQr6rp`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/scripts/run_plan001_step5_random_fault.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "b630ecdf-5e9c-4a4c-b4cc-6a9ebd22017b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gnr9tuWwdVbM3PtFVZEq14",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 934,
      "cache_read_input_tokens": 24835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 934
      },
      "output_tokens": 52,
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

_source line 15 · 2026-05-22T14:56:12.267Z_

<details><summary>↩ Tool result · `toolu_01UoWAxAZ3jmFnv2gWKKtCJd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Plan 001 Step 4: Panel regression — 455 panels × 12 conditions.\\n\\nInput:\\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\\n\\nOutput:\\n  - artifacts/results/plan001/panel_regression/step4_regression_results.json\\n\\nDependencies: numpy, scipy, statsmodels\\nOptional: pingouin (for partial_corr; manual fallback included)\\n\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport warnings\\nimport itertools\\nimport numpy as np\\nimport statsmodels.api as sm\\nfrom pathlib import Path\\nfrom scipy import optimize, stats, special\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\nfrom statsmodels.stats.multitest import multipletests\\n\\nfrom src.utils import setup_logging\\n\\nlogger = setup_logging(\\\"plan001_step4\\\")\\n\\n# ── Constants ────────────────────────────────────────────────────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4\\\", \\\"gpt-5.5\\\", \\\"gemini-2.5-pro\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4\\\", \\\"gpt-4o\\\", \\\"gemini-2.5-flash\\\",\\n    \\\"gpt-4o-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\nATTACKS = [\\n    \\\"prompt_injection\\\", \\\"sycophancy\\\", \\\"score_manipulation\\\",\\n    \\\"verbosity_bias\\\", \\\"position_bias\\\", \\\"authority_bias\\\",\\n]\\nEPS = 0.001\\n\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_PATH = PLAN001_DIR / \\\"mi_matrix\\\" / \\\"mi_matrix_15models.json\\\"\\nCKPT_FILES = [\\n    RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\",\\n    RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\",\\n]\\nOUTPUT_DIR = PLAN001_DIR / \\\"panel_regression\\\"\\n\\n\\n# ── JSON Helper ──────────────────────────────────────────────────────\\n\\ndef _json_default(obj):\\n    if isinstance(obj, np.floating):\\n        v = float(obj)\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\n    if isinstance(obj, np.integer):\\n        return int(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    if isinstance(obj, np.bool_):\\n        return bool(obj)\\n    raise TypeError(f\\\"Not JSON serializable: {type(obj)}\\\")\\n\\n\\n# ── Data Loading ─────────────────────────────────────────────────────\\n\\ndef load_mi_data():\\n    if not MI_PATH.exists():\\n        logger.error(f\\\"MI matrix not found: {MI_PATH}\\\")\\n        logger.error(\\\"Run Step 3 first: scripts/run_plan001_step3_mi_matrix.py\\\")\\n        sys.exit(1)\\n    with open(MI_PATH) as f:\\n        data = json.load(f)\\n    logger.info(f\\\"Loaded MI matrix: {len(data['models'])} models\\\")\\n    return data\\n\\n\\ndef load_pairs():\\n    for ckpt_path in CKPT_FILES:\\n        if not ckpt_path.exists():\\n            continue\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        if \\\"pairs\\\" not in data:\\n            continue\\n        pairs = {}\\n        for ds in DATASETS:\\n            if ds in data[\\\"pairs\\\"]:\\n                pairs[ds] = data[\\\"pairs\\\"][ds][:300]\\n                logger.info(f\\\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\\\")\\n        if pairs:\\n            return pairs\\n    logger.error(\\\"No pairs found in any checkpoint file\\\")\\n    sys.exit(1)\\n\\n\\ndef _invert_winners(scores):\\n    \\\"\\\"\\\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\\\"\\\"\\\"\\n    swap = {\\\"A\\\": \\\"B\\\", \\\"B\\\": \\\"A\\\", \\\"tie\\\": \\\"tie\\\"}\\n    return [{**s, \\\"winner\\\": swap.get(s.get(\\\"winner\\\", \\\"tie\\\"), \\\"tie\\\")} for s in scores]\\n\\n\\ndef load_all_scores():\\n    \\\"\\\"\\\"Load sample-level clean + attacked scores for all 15 models.\\n\\n    Returns:\\n        clean[ds][model_id] = [{\\\"winner\\\": ..., ...}, ...]\\n        attacked[ds][atk][model_id] = [{\\\"winner\\\": ..., ...}, ...]\\n    \\\"\\\"\\\"\\n    clean = {ds: {} for ds in DATASETS}\\n    attacked = {ds: {a: {} fo\\n\\n... [截断: 输出过长，省略 11673 字符] ...\\n\\n raw_eta_ps.append(cond_res[\\\"ols\\\"][\\\"eta_max_p\\\"])\\n            raw_keff_ps.append(cond_res[\\\"ols\\\"][\\\"keff_p\\\"])\\n            valid_cond_keys.append(cond)\\n\\n            ols = cond_res[\\\"ols\\\"]\\n            sig_k = \\\"***\\\" if ols[\\\"keff_p\\\"] < 0.001 else \\\"**\\\" if ols[\\\"keff_p\\\"] < 0.01 else \\\"*\\\" if ols[\\\"keff_p\\\"] < 0.05 else \\\"ns\\\"\\n            sig_e = \\\"***\\\" if ols[\\\"eta_max_p\\\"] < 0.001 else \\\"**\\\" if ols[\\\"eta_max_p\\\"] < 0.01 else \\\"*\\\" if ols[\\\"eta_max_p\\\"] < 0.05 else \\\"ns\\\"\\n            logger.info(\\n                f\\\"  OLS R2={ols['R2']:.4f}  \\\"\\n                f\\\"K_eff: B={ols['keff_beta']:+.4f} p={ols['keff_p']:.4f} {sig_k}  \\\"\\n                f\\\"eta_max: B={ols['eta_max_beta']:+.4f} p={ols['eta_max_p']:.4f} {sig_e}\\\"\\n            )\\n            logger.info(\\n                f\\\"  VIF: K_eff={cond_res['vif_keff']:.2f}, eta_max={cond_res['vif_eta_max']:.2f}\\\"\\n            )\\n            logger.info(\\n                f\\\"  Partial r(K_eff|eta_max)={cond_res['partial_r_keff']:.4f} \\\"\\n                f\\\"p={cond_res['partial_r_keff_p']:.4f}\\\"\\n            )\\n            logger.info(\\n                f\\\"  Residualized K_eff: B={cond_res['residualized_keff_beta']:+.4f} \\\"\\n                f\\\"p={cond_res['residualized_keff_p']:.4f}\\\"\\n            )\\n\\n    # ── Multiple testing corrections ──\\n    if raw_eta_ps:\\n        _, bonf_eta, _, _ = multipletests(raw_eta_ps, method=\\\"bonferroni\\\")\\n        _, fdr_eta, _, _ = multipletests(raw_eta_ps, method=\\\"fdr_bh\\\")\\n        _, bonf_keff, _, _ = multipletests(raw_keff_ps, method=\\\"bonferroni\\\")\\n        _, fdr_keff, _, _ = multipletests(raw_keff_ps, method=\\\"fdr_bh\\\")\\n\\n        for i, ck in enumerate(valid_cond_keys):\\n            condition_results[ck][\\\"eta_max_bonferroni_p\\\"] = float(bonf_eta[i])\\n            condition_results[ck][\\\"eta_max_fdr_p\\\"] = float(fdr_eta[i])\\n            condition_results[ck][\\\"keff_bonferroni_p\\\"] = float(bonf_keff[i])\\n            condition_results[ck][\\\"keff_fdr_p\\\"] = float(fdr_keff[i])\\n\\n    # ── Summary ──\\n    valid = [condition_results[k] for k in valid_cond_keys]\\n    nv = len(valid)\\n    summary = {}\\n    if nv > 0:\\n        summary = {\\n            \\\"keff_sig_negative_count\\\": (\\n                f\\\"{sum(1 for r in valid if r['ols']['keff_beta'] < 0 and r['ols']['keff_p'] < 0.05)}/{nv}\\\"\\n            ),\\n            \\\"keff_residualized_sig_count\\\": (\\n                f\\\"{sum(1 for r in valid if r.get('residualized_keff_p', 1) < 0.05)}/{nv}\\\"\\n            ),\\n            \\\"eta_max_bonferroni_sig_count\\\": (\\n                f\\\"{sum(1 for r in valid if r.get('eta_max_bonferroni_p', 1) < 0.05)}/{nv}\\\"\\n            ),\\n            \\\"eta_max_fdr_sig_count\\\": (\\n                f\\\"{sum(1 for r in valid if r.get('eta_max_fdr_p', 1) < 0.05)}/{nv}\\\"\\n            ),\\n            \\\"mean_vif_keff\\\": float(np.mean([r[\\\"vif_keff\\\"] for r in valid])),\\n            \\\"mean_R2\\\": float(np.mean([r[\\\"ols\\\"][\\\"R2\\\"] for r in valid])),\\n        }\\n\\n    output = {\\n        \\\"n_panels\\\": 455,\\n        \\\"n_models\\\": len(ALL_MODELS),\\n        \\\"models\\\": ALL_MODELS,\\n        \\\"datasets\\\": DATASETS,\\n        \\\"attacks\\\": ATTACKS,\\n        \\\"conditions\\\": condition_results,\\n        \\\"summary\\\": summary,\\n    }\\n\\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\\n    out_path = OUTPUT_DIR / \\\"step4_regression_results.json\\\"\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\\n    logger.info(f\\\"\\\\nResults saved: {out_path}\\\")\\n\\n    logger.info(\\\"\\\\n\\\" + \\\"=\\\" * 60)\\n    logger.info(\\\"SUMMARY\\\")\\n    logger.info(\\\"=\\\" * 60)\\n    for k, v in summary.items():\\n        logger.info(f\\\"  {k}: {v}\\\")\\n\\n    # Per-condition table\\n    logger.info(f\\\"\\\\n{'Condition':<35} {'R2':>6} {'K_eff B':>9} {'K_eff p':>9} {'eta_max B':>9} {'eta_max p':>9} {'VIF':>5}\\\")\\n    logger.info(\\\"-\\\" * 90)\\n    for ck in valid_cond_keys:\\n        r = condition_results[ck]\\n        o = r[\\\"ols\\\"]\\n        logger.info(\\n            f\\\"  {ck:<33} {o['R2']:>6.3f} {o['keff_beta']:>+9.4f} {o['keff_p']:>9.4f} \\\"\\n            f\\\"{o['eta_max_beta']:>+9.4f} {o['eta_max_p']:>9.4f} {r['vif_keff']:>5.1f}\\\"\\n        )\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "d85997f8-a96c-44bd-957a-835d22e65f68",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Plan 001 Step 4: Panel regression — 455 panels × 12 conditions.\\\\n\\\\nInput:\\\\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\\\\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\\\\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\\\\n\\\\nOutput:\\\\n  - artifacts/results/plan001/panel_regression/step4_regression_results.json\\\\n\\\\nDependencies: numpy, scipy, statsmodels\\\\nOptional: pingouin (for partial_corr; manual fallback included)\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport os\\\\nos.environ[\\\\\\\"HF_HOME\\\\\\\"] = \\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"\\\\n\\\\nimport sys\\\\nsys.path.insert(0, \\\\\\\"/root/cert_manip_resist_eval\\\\\\\")\\\\n\\\\nimport json\\\\nimport warnings\\\\nimport itertools\\\\nimport numpy as np\\\\nimport statsmodels.api as sm\\\\nfrom pathlib import Path\\\\nfrom scipy import optimize, stats, special\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\nfrom statsmodels.stats.multitest import multipletests\\\\n\\\\nfrom src.utils import setup_logging\\\\n\\\\nlogger = setup_logging(\\\\\\\"plan001_step4\\\\\\\")\\\\n\\\\n# ── Constants ────────────────────────────────────────────────────────\\\\nLOCAL_MODELS = [\\\\n    \\\\\\\"qwen2.5-72b\\\\\\\", \\\\\\\"llama3.1-70b\\\\\\\", \\\\\\\"mistral-large\\\\\\\",\\\\n    \\\\\\\"qwen2.5-32b\\\\\\\", \\\\\\\"qwen2.5-14b\\\\\\\", \\\\\\\"llama3.1-8b\\\\\\\",\\\\n]\\\\nAPI_MODELS = [\\\\n    \\\\\\\"claude-opus-4\\\\\\\", \\\\\\\"gpt-5.5\\\\\\\", \\\\\\\"gemini-2.5-pro\\\\\\\", \\\\\\\"gpt-4.1\\\\\\\",\\\\n    \\\\\\\"claude-sonnet-4\\\\\\\", \\\\\\\"gpt-4o\\\\\\\", \\\\\\\"gemini-2.5-flash\\\\\\\",\\\\n    \\\\\\\"gpt-4o-mini\\\\\\\", \\\\\\\"claude-3-haiku\\\\\\\",\\\\n]\\\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\\\nDATASETS = [\\\\\\\"mmlu\\\\\\\", \\\\\\\"arc_challenge\\\\\\\"]\\\\nATTACKS = [\\\\n    \\\\\\\"prompt_injection\\\\\\\", \\\\\\\"sycophancy\\\\\\\", \\\\\\\"score_manipulation\\\\\\\",\\\\n    \\\\\\\"verbosity_bias\\\\\\\", \\\\\\\"position_bias\\\\\\\", \\\\\\\"authority_bias\\\\\\\",\\\\n]\\\\nEPS = 0.001\\\\n\\\\nRESULTS_DIR = Path(\\\\\\\"/root/cert_manip_resist_eval/artifacts/results\\\\\\\")\\\\nPLAN001_DIR = RESULTS_DIR / \\\\\\\"plan001\\\\\\\"\\\\nSCORES_DIR = PLAN001_DIR / \\\\\\\"individual_scores\\\\\\\"\\\\nMI_PATH = PLAN001_DIR / \\\\\\\"mi_matrix\\\\\\\" / \\\\\\\"mi_matrix_15models.json\\\\\\\"\\\\nCKPT_FILES = [\\\\n    RESULTS_DIR / \\\\\\\"_taxonomy_checkpoint.json\\\\\\\",\\\\n    RESULTS_DIR / \\\\\\\"_step2v3_checkpoint.json\\\\\\\",\\\\n]\\\\nOUTPUT_DIR = PLAN001_DIR / \\\\\\\"panel_regression\\\\\\\"\\\\n\\\\n\\\\n# ── JSON Helper ──────────────────────────────────────────────────────\\\\n\\\\ndef _json_default(obj):\\\\n    if isinstance(obj, np.floating):\\\\n        v = float(obj)\\\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\\\n    if isinstance(obj, np.integer):\\\\n        return int(obj)\\\\n    if isinstance(obj, np.ndarray):\\\\n        return obj.tolist()\\\\n    if isinstance(obj, np.bool_):\\\\n        return bool(obj)\\\\n    raise TypeError(f\\\\\\\"Not JSON serializable: {type(obj)}\\\\\\\")\\\\n\\\\n\\\\n# ── Data Loading ─────────────────────────────────────────────────────\\\\n\\\\ndef load_mi_data():\\\\n    if not MI_PATH.exists():\\\\n        logger.error(f\\\\\\\"MI matrix not found: {MI_PATH}\\\\\\\")\\\\n        logger.error(\\\\\\\"Run Step 3 first: scripts/run_plan001_step3_mi_matrix.py\\\\\\\")\\\\n        sys.exit(1)\\\\n    with open(MI_PATH) as f:\\\\n        data = json.load(f)\\\\n    logger.info(f\\\\\\\"Loaded MI matrix: {len(data['models'])} models\\\\\\\")\\\\n    return data\\\\n\\\\n\\\\ndef load_pairs():\\\\n    for ckpt_path in CKPT_FILES:\\\\n        if not ckpt_path.exists():\\\\n            continue\\\\n        with open(ckpt_path) as f:\\\\n            data = json.load(f)\\\\n        if \\\\\\\"pairs\\\\\\\" not in data:\\\\n            continue\\\\n        pairs = {}\\\\n        for ds in DATASETS:\\\\n            if ds in data[\\\\\\\"pairs\\\\\\\"]:\\\\n                pairs[ds] = data[\\\\\\\"pairs\\\\\\\"][ds][:300]\\\\n                logger.info(f\\\\\\\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\\\\\\\")\\\\n        if pairs:\\\\n            return pairs\\\\n    logger.error(\\\\\\\"No pairs found in any checkpoint file\\\\\\\")\\\\n    sys.exit(1)\\\\n\\\\n\\\\ndef _invert_winners(scores):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    swap = {\\\\\\\"A\\\\\\\": \\\\\\\"B\\\\\\\", \\\\\\\"B\\\\\\\": \\\\\\\"A\\\\\\\", \\\\\\\"tie\\\\\\\": \\\\\\\"tie\\\\\\\"}\\\\n    return [{**s, \\\\\\\"winner\\\\\\\": swap.get(s.get(\\\\\\\"winner\\\\\\\", \\\\\\\"tie\\\\\\\"), \\\\\\\"tie\\\\\\\")} for s in scores]\\\\n\\\\n\\\\ndef load_all_scores():\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load sample-level clean + attacked scores for all 15 models.\\\\n\\\\n    Returns:\\\\n        clean[ds][model_id] = [{\\\\\\\"winner\\\\\\\": ..., ...}, ...]\\\\n        attacked[ds][atk][model_id] = [{\\\\\\\"winner\\\\\\\": ..., ...}, ...]\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    clean = {ds: {} for ds in DATASETS}\\\\n    attacked = {ds: {a: {} fo\\\\n\\\\n... [截断: 输出过长，省略 11673 字符] ...\\\\n\\\\n raw_eta_ps.append(cond_res[\\\\\\\"ols\\\\\\\"][\\\\\\\"eta_max_p\\\\\\\"])\\\\n            raw_keff_ps.append(cond_res[\\\\\\\"ols\\\\\\\"][\\\\\\\"keff_p\\\\\\\"])\\\\n            valid_cond_keys.append(cond)\\\\n\\\\n            ols = cond_res[\\\\\\\"ols\\\\\\\"]\\\\n            sig_k = \\\\\\\"***\\\\\\\" if ols[\\\\\\\"keff_p\\\\\\\"] < 0.001 else \\\\\\\"**\\\\\\\" if ols[\\\\\\\"keff_p\\\\\\\"] < 0.01 else \\\\\\\"*\\\\\\\" if ols[\\\\\\\"keff_p\\\\\\\"] < 0.05 else \\\\\\\"ns\\\\\\\"\\\\n            sig_e = \\\\\\\"***\\\\\\\" if ols[\\\\\\\"eta_max_p\\\\\\\"] < 0.001 else \\\\\\\"**\\\\\\\" if ols[\\\\\\\"eta_max_p\\\\\\\"] < 0.01 else \\\\\\\"*\\\\\\\" if ols[\\\\\\\"eta_max_p\\\\\\\"] < 0.05 else \\\\\\\"ns\\\\\\\"\\\\n            logger.info(\\\\n                f\\\\\\\"  OLS R2={ols['R2']:.4f}  \\\\\\\"\\\\n                f\\\\\\\"K_eff: B={ols['keff_beta']:+.4f} p={ols['keff_p']:.4f} {sig_k}  \\\\\\\"\\\\n                f\\\\\\\"eta_max: B={ols['eta_max_beta']:+.4f} p={ols['eta_max_p']:.4f} {sig_e}\\\\\\\"\\\\n            )\\\\n            logger.info(\\\\n                f\\\\\\\"  VIF: K_eff={cond_res['vif_keff']:.2f}, eta_max={cond_res['vif_eta_max']:.2f}\\\\\\\"\\\\n            )\\\\n            logger.info(\\\\n                f\\\\\\\"  Partial r(K_eff|eta_max)={cond_res['partial_r_keff']:.4f} \\\\\\\"\\\\n                f\\\\\\\"p={cond_res['partial_r_keff_p']:.4f}\\\\\\\"\\\\n            )\\\\n            logger.info(\\\\n                f\\\\\\\"  Residualized K_eff: B={cond_res['residualized_keff_beta']:+.4f} \\\\\\\"\\\\n                f\\\\\\\"p={cond_res['residualized_keff_p']:.4f}\\\\\\\"\\\\n            )\\\\n\\\\n    # ── Multiple testing corrections ──\\\\n    if raw_eta_ps:\\\\n        _, bonf_eta, _, _ = multipletests(raw_eta_ps, method=\\\\\\\"bonferroni\\\\\\\")\\\\n        _, fdr_eta, _, _ = multipletests(raw_eta_ps, method=\\\\\\\"fdr_bh\\\\\\\")\\\\n        _, bonf_keff, _, _ = multipletests(raw_keff_ps, method=\\\\\\\"bonferroni\\\\\\\")\\\\n        _, fdr_keff, _, _ = multipletests(raw_keff_ps, method=\\\\\\\"fdr_bh\\\\\\\")\\\\n\\\\n        for i, ck in enumerate(valid_cond_keys):\\\\n            condition_results[ck][\\\\\\\"eta_max_bonferroni_p\\\\\\\"] = float(bonf_eta[i])\\\\n            condition_results[ck][\\\\\\\"eta_max_fdr_p\\\\\\\"] = float(fdr_eta[i])\\\\n            condition_results[ck][\\\\\\\"keff_bonferroni_p\\\\\\\"] = float(bonf_keff[i])\\\\n            condition_results[ck][\\\\\\\"keff_fdr_p\\\\\\\"] = float(fdr_keff[i])\\\\n\\\\n    # ── Summary ──\\\\n    valid = [condition_results[k] for k in valid_cond_keys]\\\\n    nv = len(valid)\\\\n    summary = {}\\\\n    if nv > 0:\\\\n        summary = {\\\\n            \\\\\\\"keff_sig_negative_count\\\\\\\": (\\\\n                f\\\\\\\"{sum(1 for r in valid if r['ols']['keff_beta'] < 0 and r['ols']['keff_p'] < 0.05)}/{nv}\\\\\\\"\\\\n            ),\\\\n            \\\\\\\"keff_residualized_sig_count\\\\\\\": (\\\\n                f\\\\\\\"{sum(1 for r in valid if r.get('residualized_keff_p', 1) < 0.05)}/{nv}\\\\\\\"\\\\n            ),\\\\n            \\\\\\\"eta_max_bonferroni_sig_count\\\\\\\": (\\\\n                f\\\\\\\"{sum(1 for r in valid if r.get('eta_max_bonferroni_p', 1) < 0.05)}/{nv}\\\\\\\"\\\\n            ),\\\\n            \\\\\\\"eta_max_fdr_sig_count\\\\\\\": (\\\\n                f\\\\\\\"{sum(1 for r in valid if r.get('eta_max_fdr_p', 1) < 0.05)}/{nv}\\\\\\\"\\\\n            ),\\\\n            \\\\\\\"mean_vif_keff\\\\\\\": float(np.mean([r[\\\\\\\"vif_keff\\\\\\\"] for r in valid])),\\\\n            \\\\\\\"mean_R2\\\\\\\": float(np.mean([r[\\\\\\\"ols\\\\\\\"][\\\\\\\"R2\\\\\\\"] for r in valid])),\\\\n        }\\\\n\\\\n    output = {\\\\n        \\\\\\\"n_panels\\\\\\\": 455,\\\\n        \\\\\\\"n_models\\\\\\\": len(ALL_MODELS),\\\\n        \\\\\\\"models\\\\\\\": ALL_MODELS,\\\\n        \\\\\\\"datasets\\\\\\\": DATASETS,\\\\n        \\\\\\\"attacks\\\\\\\": ATTACKS,\\\\n        \\\\\\\"conditions\\\\\\\": condition_results,\\\\n        \\\\\\\"summary\\\\\\\": summary,\\\\n    }\\\\n\\\\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\\\\n    out_path = OUTPUT_DIR / \\\\\\\"step4_regression_results.json\\\\\\\"\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\\\\n    logger.info(f\\\\\\\"\\\\\\\\nResults saved: {out_path}\\\\\\\")\\\\n\\\\n    logger.info(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 60)\\\\n    logger.info(\\\\\\\"SUMMARY\\\\\\\")\\\\n    logger.info(\\\\\\\"=\\\\\\\" * 60)\\\\n    for k, v in summary.items():\\\\n        logger.info(f\\\\\\\"  {k}: {v}\\\\\\\")\\\\n\\\\n    # Per-condition table\\\\n    logger.info(f\\\\\\\"\\\\\\\\n{'Condition':<35} {'R2':>6} {'K_eff B':>9} {'K_eff p':>9} {'eta_max B':>9} {'eta_max p':>9} {'VIF':>5}\\\\\\\")\\\\n    logger.info(\\\\\\\"-\\\\\\\" * 90)\\\\n    for ck in valid_cond_keys:\\\\n        r = condition_results[ck]\\\\n        o = r[\\\\\\\"ols\\\\\\\"]\\\\n        logger.info(\\\\n            f\\\\\\\"  {ck:<33} {o['R2']:>6.3f} {o['keff_beta']:>+9.4f} {o['keff_p']:>9.4f} \\\\\\\"\\\\n            f\\\\\\\"{o['eta_max_beta']:>+9.4f} {o['eta_max_p']:>9.4f} {r['vif_keff']:>5.1f}\\\\\\\"\\\\n        )\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.84}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Plan 001 Step 4: Panel regression — 455 panels × 12 conditions.\\n\\nInput:\\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\\n\\nOutput:\\n  - artifacts/results/plan001/panel_regression/step4_regression_results.json\\n\\nDependencies: numpy, scipy, statsmodels\\nOptional: pingouin (for partial_corr; manual fallback included)\\n\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport warnings\\nimport itertools\\nimport numpy as np\\nimport statsmodels.api as sm\\nfrom pathlib import Path\\nfrom scipy import optimize, stats, special\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\nfrom statsmodels.stats.multitest import multipletests\\n\\nfrom src.utils import setup_logging\\n\\nlogger = setup_logging(\\\"plan001_step4\\\")\\n\\n# ── Constants ────────────────────────────────────────────────────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4\\\", \\\"gpt-5.5\\\", \\\"gemini-2.5-pro\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4\\\", \\\"gpt-4o\\\", \\\"gemini-2.5-flash\\\",\\n    \\\"gpt-4o-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\nATTACKS = [\\n    \\\"prompt_injection\\\", \\\"sycophancy\\\", \\\"score_manipulation\\\",\\n    \\\"verbosity_bias\\\", \\\"position_bias\\\", \\\"authority_bias\\\",\\n]\\nEPS = 0.001\\n\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_PATH = PLAN001_DIR / \\\"mi_matrix\\\" / \\\"mi_matrix_15models.json\\\"\\nCKPT_FILES = [\\n    RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\",\\n    RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\",\\n]\\nOUTPUT_DIR = PLAN001_DIR / \\\"panel_regression\\\"\\n\\n\\n# ── JSON Helper ──────────────────────────────────────────────────────\\n\\ndef _json_default(obj):\\n    if isinstance(obj, np.floating):\\n        v = float(obj)\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\n    if isinstance(obj, np.integer):\\n        return int(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    if isinstance(obj, np.bool_):\\n        return bool(obj)\\n    raise TypeError(f\\\"Not JSON serializable: {type(obj)}\\\")\\n\\n\\n# ── Data Loading ─────────────────────────────────────────────────────\\n\\ndef load_mi_data():\\n    if not MI_PATH.exists():\\n        logger.error(f\\\"MI matrix not found: {MI_PATH}\\\")\\n        logger.error(\\\"Run Step 3 first: scripts/run_plan001_step3_mi_matrix.py\\\")\\n        sys.exit(1)\\n    with open(MI_PATH) as f:\\n        data = json.load(f)\\n    logger.info(f\\\"Loaded MI matrix: {len(data['models'])} models\\\")\\n    return data\\n\\n\\ndef load_pairs():\\n    for ckpt_path in CKPT_FILES:\\n        if not ckpt_path.exists():\\n            continue\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        if \\\"pairs\\\" not in data:\\n            continue\\n        pairs = {}\\n        for ds in DATASETS:\\n            if ds in data[\\\"pairs\\\"]:\\n                pairs[ds] = data[\\\"pairs\\\"][ds][:300]\\n                logger.info(f\\\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\\\")\\n        if pairs:\\n            return pairs\\n    logger.error(\\\"No pairs found in any checkpoint file\\\")\\n    sys.exit(1)\\n\\n\\ndef _invert_winners(scores):\\n    \\\"\\\"\\\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\\\"\\\"\\\"\\n    swap = {\\\"A\\\": \\\"B\\\", \\\"B\\\": \\\"A\\\", \\\"tie\\\": \\\"tie\\\"}\\n    return [{**s, \\\"winner\\\": swap.get(s.get(\\\"winner\\\", \\\"tie\\\"), \\\"tie\\\")} for s in scores]\\n\\n\\ndef load_all_scores():\\n    \\\"\\\"\\\"Load sample-level clean + attacked scores for all 15 models.\\n\\n    Returns:\\n        clean[ds][model_id] = [{\\\"winner\\\": ..., ...}, ...]\\n        attacked[ds][atk][model_id] = [{\\\"winner\\\": ..., ...}, ...]\\n    \\\"\\\"\\\"\\n    clean = {ds: {} for ds in DATASETS}\\n    attacked = {ds: {a: {} fo\\n\\n... [截断: 输出过长，省略 11673 字符] ...\\n\\n raw_eta_ps.append(cond_res[\\\"ols\\\"][\\\"eta_max_p\\\"])\\n            raw_keff_ps.append(cond_res[\\\"ols\\\"][\\\"keff_p\\\"])\\n            valid_cond_keys.append(cond)\\n\\n            ols = cond_res[\\\"ols\\\"]\\n            sig_k = \\\"***\\\" if ols[\\\"keff_p\\\"] < 0.001 else \\\"**\\\" if ols[\\\"keff_p\\\"] < 0.01 else \\\"*\\\" if ols[\\\"keff_p\\\"] < 0.05 else \\\"ns\\\"\\n            sig_e = \\\"***\\\" if ols[\\\"eta_max_p\\\"] < 0.001 else \\\"**\\\" if ols[\\\"eta_max_p\\\"] < 0.01 else \\\"*\\\" if ols[\\\"eta_max_p\\\"] < 0.05 else \\\"ns\\\"\\n            logger.info(\\n                f\\\"  OLS R2={ols['R2']:.4f}  \\\"\\n                f\\\"K_eff: B={ols['keff_beta']:+.4f} p={ols['keff_p']:.4f} {sig_k}  \\\"\\n                f\\\"eta_max: B={ols['eta_max_beta']:+.4f} p={ols['eta_max_p']:.4f} {sig_e}\\\"\\n            )\\n            logger.info(\\n                f\\\"  VIF: K_eff={cond_res['vif_keff']:.2f}, eta_max={cond_res['vif_eta_max']:.2f}\\\"\\n            )\\n            logger.info(\\n                f\\\"  Partial r(K_eff|eta_max)={cond_res['partial_r_keff']:.4f} \\\"\\n                f\\\"p={cond_res['partial_r_keff_p']:.4f}\\\"\\n            )\\n            logger.info(\\n                f\\\"  Residualized K_eff: B={cond_res['residualized_keff_beta']:+.4f} \\\"\\n                f\\\"p={cond_res['residualized_keff_p']:.4f}\\\"\\n            )\\n\\n    # ── Multiple testing corrections ──\\n    if raw_eta_ps:\\n        _, bonf_eta, _, _ = multipletests(raw_eta_ps, method=\\\"bonferroni\\\")\\n        _, fdr_eta, _, _ = multipletests(raw_eta_ps, method=\\\"fdr_bh\\\")\\n        _, bonf_keff, _, _ = multipletests(raw_keff_ps, method=\\\"bonferroni\\\")\\n        _, fdr_keff, _, _ = multipletests(raw_keff_ps, method=\\\"fdr_bh\\\")\\n\\n        for i, ck in enumerate(valid_cond_keys):\\n            condition_results[ck][\\\"eta_max_bonferroni_p\\\"] = float(bonf_eta[i])\\n            condition_results[ck][\\\"eta_max_fdr_p\\\"] = float(fdr_eta[i])\\n            condition_results[ck][\\\"keff_bonferroni_p\\\"] = float(bonf_keff[i])\\n            condition_results[ck][\\\"keff_fdr_p\\\"] = float(fdr_keff[i])\\n\\n    # ── Summary ──\\n    valid = [condition_results[k] for k in valid_cond_keys]\\n    nv = len(valid)\\n    summary = {}\\n    if nv > 0:\\n        summary = {\\n            \\\"keff_sig_negative_count\\\": (\\n                f\\\"{sum(1 for r in valid if r['ols']['keff_beta'] < 0 and r['ols']['keff_p'] < 0.05)}/{nv}\\\"\\n            ),\\n            \\\"keff_residualized_sig_count\\\": (\\n                f\\\"{sum(1 for r in valid if r.get('residualized_keff_p', 1) < 0.05)}/{nv}\\\"\\n            ),\\n            \\\"eta_max_bonferroni_sig_count\\\": (\\n                f\\\"{sum(1 for r in valid if r.get('eta_max_bonferroni_p', 1) < 0.05)}/{nv}\\\"\\n            ),\\n            \\\"eta_max_fdr_sig_count\\\": (\\n                f\\\"{sum(1 for r in valid if r.get('eta_max_fdr_p', 1) < 0.05)}/{nv}\\\"\\n            ),\\n            \\\"mean_vif_keff\\\": float(np.mean([r[\\\"vif_keff\\\"] for r in valid])),\\n            \\\"mean_R2\\\": float(np.mean([r[\\\"ols\\\"][\\\"R2\\\"] for r in valid])),\\n        }\\n\\n    output = {\\n        \\\"n_panels\\\": 455,\\n        \\\"n_models\\\": len(ALL_MODELS),\\n        \\\"models\\\": ALL_MODELS,\\n        \\\"datasets\\\": DATASETS,\\n        \\\"attacks\\\": ATTACKS,\\n        \\\"conditions\\\": condition_results,\\n        \\\"summary\\\": summary,\\n    }\\n\\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\\n    out_path = OUTPUT_DIR / \\\"step4_regression_results.json\\\"\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\\n    logger.info(f\\\"\\\\nResults saved: {out_path}\\\")\\n\\n    logger.info(\\\"\\\\n\\\" + \\\"=\\\" * 60)\\n    logger.info(\\\"SUMMARY\\\")\\n    logger.info(\\\"=\\\" * 60)\\n    for k, v in summary.items():\\n        logger.info(f\\\"  {k}: {v}\\\")\\n\\n    # Per-condition table\\n    logger.info(f\\\"\\\\n{'Condition':<35} {'R2':>6} {'K_eff B':>9} {'K_eff p':>9} {'eta_max B':>9} {'eta_max p':>9} {'VIF':>5}\\\")\\n    logger.info(\\\"-\\\" * 90)\\n    for ck in valid_cond_keys:\\n        r = condition_results[ck]\\n        o = r[\\\"ols\\\"]\\n        logger.info(\\n            f\\\"  {ck:<33} {o['R2']:>6.3f} {o['keff_beta']:>+9.4f} {o['keff_p']:>9.4f} \\\"\\n            f\\\"{o['eta_max_beta']:>+9.4f} {o['eta_max_p']:>9.4f} {r['vif_keff']:>5.1f}\\\"\\n        )\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.84}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T14:56:12.804Z_

<details><summary>↩ Tool result · `toolu_017Z34BFjee51BxRLNWQr6rp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Plan 001 Step 5: Random-fault simulation — 455 panels × 12 conditions.\\n\\nInput:\\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\\n\\nOutput:\\n  - artifacts/results/plan001/panel_regression/step5_random_fault_results.json\\n\\nDependencies: numpy, scipy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport warnings\\nimport itertools\\nimport numpy as np\\nimport statsmodels.api as sm\\nfrom pathlib import Path\\nfrom scipy import stats\\n\\nfrom src.utils import setup_logging\\n\\nlogger = setup_logging(\\\"plan001_step5\\\")\\n\\n# ── Constants ───────────────────────────────────────────────��────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4\\\", \\\"gpt-5.5\\\", \\\"gemini-2.5-pro\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4\\\", \\\"gpt-4o\\\", \\\"gemini-2.5-flash\\\",\\n    \\\"gpt-4o-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\nATTACKS = [\\n    \\\"prompt_injection\\\", \\\"sycophancy\\\", \\\"score_manipulation\\\",\\n    \\\"verbosity_bias\\\", \\\"position_bias\\\", \\\"authority_bias\\\",\\n]\\nEPS = 0.001\\nN_SIMS = 1000\\nN_SAMPLES = 300\\nSIM_BATCH = 100\\n\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_PATH = PLAN001_DIR / \\\"mi_matrix\\\" / \\\"mi_matrix_15models.json\\\"\\nCKPT_FILES = [\\n    RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\",\\n    RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\",\\n]\\nOUTPUT_DIR = PLAN001_DIR / \\\"panel_regression\\\"\\n\\n\\n# ── JSON Helper ───────��──────────────────────────────────────────────\\n\\ndef _json_default(obj):\\n    if isinstance(obj, np.floating):\\n        v = float(obj)\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\n    if isinstance(obj, np.integer):\\n        return int(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    if isinstance(obj, np.bool_):\\n        return bool(obj)\\n    raise TypeError(f\\\"Not JSON serializable: {type(obj)}\\\")\\n\\n\\n# ── Data Loading (shared with Step 4) ────────────────────────────────\\n\\ndef load_mi_data():\\n    if not MI_PATH.exists():\\n        logger.error(f\\\"MI matrix not found: {MI_PATH}\\\")\\n        sys.exit(1)\\n    with open(MI_PATH) as f:\\n        data = json.load(f)\\n    logger.info(f\\\"Loaded MI matrix: {len(data['models'])} models\\\")\\n    return data\\n\\n\\ndef load_pairs():\\n    for ckpt_path in CKPT_FILES:\\n        if not ckpt_path.exists():\\n            continue\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        if \\\"pairs\\\" not in data:\\n            continue\\n        pairs = {}\\n        for ds in DATASETS:\\n            if ds in data[\\\"pairs\\\"]:\\n                pairs[ds] = data[\\\"pairs\\\"][ds][:300]\\n                logger.info(f\\\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\\\")\\n        if pairs:\\n            return pairs\\n    logger.error(\\\"No pairs found in any checkpoint file\\\")\\n    sys.exit(1)\\n\\n\\ndef _invert_winners(scores):\\n    swap = {\\\"A\\\": \\\"B\\\", \\\"B\\\": \\\"A\\\", \\\"tie\\\": \\\"tie\\\"}\\n    return [{**s, \\\"winner\\\": swap.get(s.get(\\\"winner\\\", \\\"tie\\\"), \\\"tie\\\")} for s in scores]\\n\\n\\ndef load_all_scores():\\n    clean = {ds: {} for ds in DATASETS}\\n    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}\\n\\n    for ckpt_path in CKPT_FILES:\\n        if not ckpt_path.exists():\\n            continue\\n        logger.info(f\\\"Loading checkpoint: {ckpt_path.name}\\\")\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        for ds in DATASETS:\\n            for mid, scores in data.get(\\\"clean_scores\\\", {}).get(ds, {}).items():\\n                if mid not in clean[ds]:\\n                    clean[ds][mid] = scores\\n            for atk in ATTACKS:\\n                for mid, scores in data.get(\\\"attacked_scores\\n\\n... [截断: 输出过长，省略 10848 字符] ...\\n\\ngger.info(\\n                f\\\"  Adaptive: K_eff B={adaptive_ols.get('keff_beta', 0):+.4f} \\\"\\n                f\\\"p={adaptive_ols.get('keff_p', 1):.4f} R2={adaptive_ols.get('R2', 0):.4f}\\\"\\n            )\\n            logger.info(\\n                f\\\"  RF:       K_eff B={rf_ols.get('keff_beta', 0):+.4f} \\\"\\n                f\\\"p={rf_ols.get('keff_p', 1):.4f} R2={rf_ols.get('R2', 0):.4f}\\\"\\n            )\\n            logger.info(f\\\"  dR2={delta_R2:+.4f}  K_eff gains significance: {keff_gains}\\\")\\n            if n_hk_le >= 5:\\n                logger.info(\\n                    f\\\"  High-K/Low-eta panels ({n_hk_le}): \\\"\\n                    f\\\"mean benefit={hk_le_benefit:+.4f} p={hk_le_pval}\\\"\\n                )\\n\\n    # ── Summary ──\\n    valid = {k: v for k, v in condition_results.items() if not v.get(\\\"skipped\\\")}\\n    nv = len(valid)\\n\\n    if nv > 0:\\n        n_adapt_sig = sum(\\n            1 for v in valid.values()\\n            if v[\\\"adaptive\\\"].get(\\\"keff_p\\\", 1) < 0.05 and v[\\\"adaptive\\\"].get(\\\"keff_beta\\\", 0) < 0\\n        )\\n        n_rf_sig = sum(\\n            1 for v in valid.values()\\n            if v[\\\"random_fault\\\"].get(\\\"keff_p\\\", 1) < 0.05 and v[\\\"random_fault\\\"].get(\\\"keff_beta\\\", 0) < 0\\n        )\\n        mean_dR2 = float(np.mean([v[\\\"delta_R2\\\"] for v in valid.values()]))\\n        n_gains = sum(1 for v in valid.values() if v[\\\"keff_gains_significance\\\"])\\n\\n        parts = []\\n        parts.append(\\n            f\\\"K_eff significantly negative in {n_rf_sig}/{nv} conditions under RF \\\"\\n            f\\\"vs {n_adapt_sig}/{nv} under adaptive.\\\"\\n        )\\n        if mean_dR2 > 0:\\n            parts.append(\\n                f\\\"RF model explains more variance (mean dR2={mean_dR2:+.3f}), \\\"\\n                \\\"consistent with independent-error majority vote theory.\\\"\\n            )\\n        else:\\n            parts.append(\\n                f\\\"Adaptive model explains more variance (mean dR2={mean_dR2:+.3f}).\\\"\\n            )\\n        if n_gains > nv // 2:\\n            parts.append(\\n                f\\\"K_eff gains significance in {n_gains}/{nv} conditions under RF, \\\"\\n                \\\"suggesting diversity benefit is undermined by adaptive attacks.\\\"\\n            )\\n        interpretation = \\\" \\\".join(parts)\\n\\n        summary = {\\n            \\\"adaptive_keff_sig_negative\\\": f\\\"{n_adapt_sig}/{nv}\\\",\\n            \\\"random_fault_keff_sig_negative\\\": f\\\"{n_rf_sig}/{nv}\\\",\\n            \\\"mean_delta_R2\\\": mean_dR2,\\n            \\\"keff_gains_significance_count\\\": f\\\"{n_gains}/{nv}\\\",\\n            \\\"interpretation\\\": interpretation,\\n        }\\n    else:\\n        summary = {\\\"note\\\": \\\"No valid conditions to summarize\\\"}\\n\\n    output = {\\n        \\\"n_panels\\\": 455,\\n        \\\"n_simulations\\\": N_SIMS,\\n        \\\"n_samples_per_sim\\\": N_SAMPLES,\\n        \\\"models\\\": ALL_MODELS,\\n        \\\"conditions\\\": condition_results,\\n        \\\"summary\\\": summary,\\n    }\\n\\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\\n    out_path = OUTPUT_DIR / \\\"step5_random_fault_results.json\\\"\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\\n    logger.info(f\\\"\\\\nResults saved: {out_path}\\\")\\n\\n    logger.info(\\\"\\\\n\\\" + \\\"=\\\" * 60)\\n    logger.info(\\\"SUMMARY\\\")\\n    logger.info(\\\"=\\\" * 60)\\n    for k, v in summary.items():\\n        if k != \\\"interpretation\\\":\\n            logger.info(f\\\"  {k}: {v}\\\")\\n    if \\\"interpretation\\\" in summary:\\n        logger.info(f\\\"\\\\n  {summary['interpretation']}\\\")\\n\\n    # Comparison table\\n    valid_keys = [k for k in condition_results if not condition_results[k].get(\\\"skipped\\\")]\\n    logger.info(f\\\"\\\\n{'Condition':<35} {'Adap R2':>8} {'RF R2':>8} {'dR2':>7} {'Adap Kp':>8} {'RF Kp':>8} {'Gains':>5}\\\")\\n    logger.info(\\\"-\\\" * 85)\\n    for ck in valid_keys:\\n        r = condition_results[ck]\\n        a = r[\\\"adaptive\\\"]\\n        rf = r[\\\"random_fault\\\"]\\n        logger.info(\\n            f\\\"  {ck:<33} {a.get('R2', 0):>8.4f} {rf.get('R2', 0):>8.4f} \\\"\\n            f\\\"{r['delta_R2']:>+7.3f} {a.get('keff_p', 1):>8.4f} {rf.get('keff_p', 1):>8.4f} \\\"\\n            f\\\"{'Y' if r['keff_gains_significance'] else 'N':>5}\\\"\\n        )\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "20d53baa-f2ef-4021-9875-a23928e265f5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Plan 001 Step 5: Random-fault simulation — 455 panels × 12 conditions.\\\\n\\\\nInput:\\\\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\\\\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\\\\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\\\\n\\\\nOutput:\\\\n  - artifacts/results/plan001/panel_regression/step5_random_fault_results.json\\\\n\\\\nDependencies: numpy, scipy, statsmodels\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport os\\\\nos.environ[\\\\\\\"HF_HOME\\\\\\\"] = \\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"\\\\n\\\\nimport sys\\\\nsys.path.insert(0, \\\\\\\"/root/cert_manip_resist_eval\\\\\\\")\\\\n\\\\nimport json\\\\nimport warnings\\\\nimport itertools\\\\nimport numpy as np\\\\nimport statsmodels.api as sm\\\\nfrom pathlib import Path\\\\nfrom scipy import stats\\\\n\\\\nfrom src.utils import setup_logging\\\\n\\\\nlogger = setup_logging(\\\\\\\"plan001_step5\\\\\\\")\\\\n\\\\n# ── Constants ───────────────────────────────────────────────��────────\\\\nLOCAL_MODELS = [\\\\n    \\\\\\\"qwen2.5-72b\\\\\\\", \\\\\\\"llama3.1-70b\\\\\\\", \\\\\\\"mistral-large\\\\\\\",\\\\n    \\\\\\\"qwen2.5-32b\\\\\\\", \\\\\\\"qwen2.5-14b\\\\\\\", \\\\\\\"llama3.1-8b\\\\\\\",\\\\n]\\\\nAPI_MODELS = [\\\\n    \\\\\\\"claude-opus-4\\\\\\\", \\\\\\\"gpt-5.5\\\\\\\", \\\\\\\"gemini-2.5-pro\\\\\\\", \\\\\\\"gpt-4.1\\\\\\\",\\\\n    \\\\\\\"claude-sonnet-4\\\\\\\", \\\\\\\"gpt-4o\\\\\\\", \\\\\\\"gemini-2.5-flash\\\\\\\",\\\\n    \\\\\\\"gpt-4o-mini\\\\\\\", \\\\\\\"claude-3-haiku\\\\\\\",\\\\n]\\\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\\\nDATASETS = [\\\\\\\"mmlu\\\\\\\", \\\\\\\"arc_challenge\\\\\\\"]\\\\nATTACKS = [\\\\n    \\\\\\\"prompt_injection\\\\\\\", \\\\\\\"sycophancy\\\\\\\", \\\\\\\"score_manipulation\\\\\\\",\\\\n    \\\\\\\"verbosity_bias\\\\\\\", \\\\\\\"position_bias\\\\\\\", \\\\\\\"authority_bias\\\\\\\",\\\\n]\\\\nEPS = 0.001\\\\nN_SIMS = 1000\\\\nN_SAMPLES = 300\\\\nSIM_BATCH = 100\\\\n\\\\nRESULTS_DIR = Path(\\\\\\\"/root/cert_manip_resist_eval/artifacts/results\\\\\\\")\\\\nPLAN001_DIR = RESULTS_DIR / \\\\\\\"plan001\\\\\\\"\\\\nSCORES_DIR = PLAN001_DIR / \\\\\\\"individual_scores\\\\\\\"\\\\nMI_PATH = PLAN001_DIR / \\\\\\\"mi_matrix\\\\\\\" / \\\\\\\"mi_matrix_15models.json\\\\\\\"\\\\nCKPT_FILES = [\\\\n    RESULTS_DIR / \\\\\\\"_taxonomy_checkpoint.json\\\\\\\",\\\\n    RESULTS_DIR / \\\\\\\"_step2v3_checkpoint.json\\\\\\\",\\\\n]\\\\nOUTPUT_DIR = PLAN001_DIR / \\\\\\\"panel_regression\\\\\\\"\\\\n\\\\n\\\\n# ── JSON Helper ───────��──────────────────────────────────────────────\\\\n\\\\ndef _json_default(obj):\\\\n    if isinstance(obj, np.floating):\\\\n        v = float(obj)\\\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\\\n    if isinstance(obj, np.integer):\\\\n        return int(obj)\\\\n    if isinstance(obj, np.ndarray):\\\\n        return obj.tolist()\\\\n    if isinstance(obj, np.bool_):\\\\n        return bool(obj)\\\\n    raise TypeError(f\\\\\\\"Not JSON serializable: {type(obj)}\\\\\\\")\\\\n\\\\n\\\\n# ── Data Loading (shared with Step 4) ────────────────────────────────\\\\n\\\\ndef load_mi_data():\\\\n    if not MI_PATH.exists():\\\\n        logger.error(f\\\\\\\"MI matrix not found: {MI_PATH}\\\\\\\")\\\\n        sys.exit(1)\\\\n    with open(MI_PATH) as f:\\\\n        data = json.load(f)\\\\n    logger.info(f\\\\\\\"Loaded MI matrix: {len(data['models'])} models\\\\\\\")\\\\n    return data\\\\n\\\\n\\\\ndef load_pairs():\\\\n    for ckpt_path in CKPT_FILES:\\\\n        if not ckpt_path.exists():\\\\n            continue\\\\n        with open(ckpt_path) as f:\\\\n            data = json.load(f)\\\\n        if \\\\\\\"pairs\\\\\\\" not in data:\\\\n            continue\\\\n        pairs = {}\\\\n        for ds in DATASETS:\\\\n            if ds in data[\\\\\\\"pairs\\\\\\\"]:\\\\n                pairs[ds] = data[\\\\\\\"pairs\\\\\\\"][ds][:300]\\\\n                logger.info(f\\\\\\\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\\\\\\\")\\\\n        if pairs:\\\\n            return pairs\\\\n    logger.error(\\\\\\\"No pairs found in any checkpoint file\\\\\\\")\\\\n    sys.exit(1)\\\\n\\\\n\\\\ndef _invert_winners(scores):\\\\n    swap = {\\\\\\\"A\\\\\\\": \\\\\\\"B\\\\\\\", \\\\\\\"B\\\\\\\": \\\\\\\"A\\\\\\\", \\\\\\\"tie\\\\\\\": \\\\\\\"tie\\\\\\\"}\\\\n    return [{**s, \\\\\\\"winner\\\\\\\": swap.get(s.get(\\\\\\\"winner\\\\\\\", \\\\\\\"tie\\\\\\\"), \\\\\\\"tie\\\\\\\")} for s in scores]\\\\n\\\\n\\\\ndef load_all_scores():\\\\n    clean = {ds: {} for ds in DATASETS}\\\\n    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}\\\\n\\\\n    for ckpt_path in CKPT_FILES:\\\\n        if not ckpt_path.exists():\\\\n            continue\\\\n        logger.info(f\\\\\\\"Loading checkpoint: {ckpt_path.name}\\\\\\\")\\\\n        with open(ckpt_path) as f:\\\\n            data = json.load(f)\\\\n        for ds in DATASETS:\\\\n            for mid, scores in data.get(\\\\\\\"clean_scores\\\\\\\", {}).get(ds, {}).items():\\\\n                if mid not in clean[ds]:\\\\n                    clean[ds][mid] = scores\\\\n            for atk in ATTACKS:\\\\n                for mid, scores in data.get(\\\\\\\"attacked_scores\\\\n\\\\n... [截断: 输出过长，省略 10848 字符] ...\\\\n\\\\ngger.info(\\\\n                f\\\\\\\"  Adaptive: K_eff B={adaptive_ols.get('keff_beta', 0):+.4f} \\\\\\\"\\\\n                f\\\\\\\"p={adaptive_ols.get('keff_p', 1):.4f} R2={adaptive_ols.get('R2', 0):.4f}\\\\\\\"\\\\n            )\\\\n            logger.info(\\\\n                f\\\\\\\"  RF:       K_eff B={rf_ols.get('keff_beta', 0):+.4f} \\\\\\\"\\\\n                f\\\\\\\"p={rf_ols.get('keff_p', 1):.4f} R2={rf_ols.get('R2', 0):.4f}\\\\\\\"\\\\n            )\\\\n            logger.info(f\\\\\\\"  dR2={delta_R2:+.4f}  K_eff gains significance: {keff_gains}\\\\\\\")\\\\n            if n_hk_le >= 5:\\\\n                logger.info(\\\\n                    f\\\\\\\"  High-K/Low-eta panels ({n_hk_le}): \\\\\\\"\\\\n                    f\\\\\\\"mean benefit={hk_le_benefit:+.4f} p={hk_le_pval}\\\\\\\"\\\\n                )\\\\n\\\\n    # ── Summary ──\\\\n    valid = {k: v for k, v in condition_results.items() if not v.get(\\\\\\\"skipped\\\\\\\")}\\\\n    nv = len(valid)\\\\n\\\\n    if nv > 0:\\\\n        n_adapt_sig = sum(\\\\n            1 for v in valid.values()\\\\n            if v[\\\\\\\"adaptive\\\\\\\"].get(\\\\\\\"keff_p\\\\\\\", 1) < 0.05 and v[\\\\\\\"adaptive\\\\\\\"].get(\\\\\\\"keff_beta\\\\\\\", 0) < 0\\\\n        )\\\\n        n_rf_sig = sum(\\\\n            1 for v in valid.values()\\\\n            if v[\\\\\\\"random_fault\\\\\\\"].get(\\\\\\\"keff_p\\\\\\\", 1) < 0.05 and v[\\\\\\\"random_fault\\\\\\\"].get(\\\\\\\"keff_beta\\\\\\\", 0) < 0\\\\n        )\\\\n        mean_dR2 = float(np.mean([v[\\\\\\\"delta_R2\\\\\\\"] for v in valid.values()]))\\\\n        n_gains = sum(1 for v in valid.values() if v[\\\\\\\"keff_gains_significance\\\\\\\"])\\\\n\\\\n        parts = []\\\\n        parts.append(\\\\n            f\\\\\\\"K_eff significantly negative in {n_rf_sig}/{nv} conditions under RF \\\\\\\"\\\\n            f\\\\\\\"vs {n_adapt_sig}/{nv} under adaptive.\\\\\\\"\\\\n        )\\\\n        if mean_dR2 > 0:\\\\n            parts.append(\\\\n                f\\\\\\\"RF model explains more variance (mean dR2={mean_dR2:+.3f}), \\\\\\\"\\\\n                \\\\\\\"consistent with independent-error majority vote theory.\\\\\\\"\\\\n            )\\\\n        else:\\\\n            parts.append(\\\\n                f\\\\\\\"Adaptive model explains more variance (mean dR2={mean_dR2:+.3f}).\\\\\\\"\\\\n            )\\\\n        if n_gains > nv // 2:\\\\n            parts.append(\\\\n                f\\\\\\\"K_eff gains significance in {n_gains}/{nv} conditions under RF, \\\\\\\"\\\\n                \\\\\\\"suggesting diversity benefit is undermined by adaptive attacks.\\\\\\\"\\\\n            )\\\\n        interpretation = \\\\\\\" \\\\\\\".join(parts)\\\\n\\\\n        summary = {\\\\n            \\\\\\\"adaptive_keff_sig_negative\\\\\\\": f\\\\\\\"{n_adapt_sig}/{nv}\\\\\\\",\\\\n            \\\\\\\"random_fault_keff_sig_negative\\\\\\\": f\\\\\\\"{n_rf_sig}/{nv}\\\\\\\",\\\\n            \\\\\\\"mean_delta_R2\\\\\\\": mean_dR2,\\\\n            \\\\\\\"keff_gains_significance_count\\\\\\\": f\\\\\\\"{n_gains}/{nv}\\\\\\\",\\\\n            \\\\\\\"interpretation\\\\\\\": interpretation,\\\\n        }\\\\n    else:\\\\n        summary = {\\\\\\\"note\\\\\\\": \\\\\\\"No valid conditions to summarize\\\\\\\"}\\\\n\\\\n    output = {\\\\n        \\\\\\\"n_panels\\\\\\\": 455,\\\\n        \\\\\\\"n_simulations\\\\\\\": N_SIMS,\\\\n        \\\\\\\"n_samples_per_sim\\\\\\\": N_SAMPLES,\\\\n        \\\\\\\"models\\\\\\\": ALL_MODELS,\\\\n        \\\\\\\"conditions\\\\\\\": condition_results,\\\\n        \\\\\\\"summary\\\\\\\": summary,\\\\n    }\\\\n\\\\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\\\\n    out_path = OUTPUT_DIR / \\\\\\\"step5_random_fault_results.json\\\\\\\"\\\\n    with open(out_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\\\\n    logger.info(f\\\\\\\"\\\\\\\\nResults saved: {out_path}\\\\\\\")\\\\n\\\\n    logger.info(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 60)\\\\n    logger.info(\\\\\\\"SUMMARY\\\\\\\")\\\\n    logger.info(\\\\\\\"=\\\\\\\" * 60)\\\\n    for k, v in summary.items():\\\\n        if k != \\\\\\\"interpretation\\\\\\\":\\\\n            logger.info(f\\\\\\\"  {k}: {v}\\\\\\\")\\\\n    if \\\\\\\"interpretation\\\\\\\" in summary:\\\\n        logger.info(f\\\\\\\"\\\\\\\\n  {summary['interpretation']}\\\\\\\")\\\\n\\\\n    # Comparison table\\\\n    valid_keys = [k for k in condition_results if not condition_results[k].get(\\\\\\\"skipped\\\\\\\")]\\\\n    logger.info(f\\\\\\\"\\\\\\\\n{'Condition':<35} {'Adap R2':>8} {'RF R2':>8} {'dR2':>7} {'Adap Kp':>8} {'RF Kp':>8} {'Gains':>5}\\\\\\\")\\\\n    logger.info(\\\\\\\"-\\\\\\\" * 85)\\\\n    for ck in valid_keys:\\\\n        r = condition_results[ck]\\\\n        a = r[\\\\\\\"adaptive\\\\\\\"]\\\\n        rf = r[\\\\\\\"random_fault\\\\\\\"]\\\\n        logger.info(\\\\n            f\\\\\\\"  {ck:<33} {a.get('R2', 0):>8.4f} {rf.get('R2', 0):>8.4f} \\\\\\\"\\\\n            f\\\\\\\"{r['delta_R2']:>+7.3f} {a.get('keff_p', 1):>8.4f} {rf.get('keff_p', 1):>8.4f} \\\\\\\"\\\\n            f\\\\\\\"{'Y' if r['keff_gains_significance'] else 'N':>5}\\\\\\\"\\\\n        )\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Plan 001 Step 5: Random-fault simulation — 455 panels × 12 conditions.\\n\\nInput:\\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\\n\\nOutput:\\n  - artifacts/results/plan001/panel_regression/step5_random_fault_results.json\\n\\nDependencies: numpy, scipy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport warnings\\nimport itertools\\nimport numpy as np\\nimport statsmodels.api as sm\\nfrom pathlib import Path\\nfrom scipy import stats\\n\\nfrom src.utils import setup_logging\\n\\nlogger = setup_logging(\\\"plan001_step5\\\")\\n\\n# ── Constants ───────────────────────────────────────────────��────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4\\\", \\\"gpt-5.5\\\", \\\"gemini-2.5-pro\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4\\\", \\\"gpt-4o\\\", \\\"gemini-2.5-flash\\\",\\n    \\\"gpt-4o-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\nATTACKS = [\\n    \\\"prompt_injection\\\", \\\"sycophancy\\\", \\\"score_manipulation\\\",\\n    \\\"verbosity_bias\\\", \\\"position_bias\\\", \\\"authority_bias\\\",\\n]\\nEPS = 0.001\\nN_SIMS = 1000\\nN_SAMPLES = 300\\nSIM_BATCH = 100\\n\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_PATH = PLAN001_DIR / \\\"mi_matrix\\\" / \\\"mi_matrix_15models.json\\\"\\nCKPT_FILES = [\\n    RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\",\\n    RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\",\\n]\\nOUTPUT_DIR = PLAN001_DIR / \\\"panel_regression\\\"\\n\\n\\n# ── JSON Helper ───────��──────────────────────────────────────────────\\n\\ndef _json_default(obj):\\n    if isinstance(obj, np.floating):\\n        v = float(obj)\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\n    if isinstance(obj, np.integer):\\n        return int(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    if isinstance(obj, np.bool_):\\n        return bool(obj)\\n    raise TypeError(f\\\"Not JSON serializable: {type(obj)}\\\")\\n\\n\\n# ── Data Loading (shared with Step 4) ────────────────────────────────\\n\\ndef load_mi_data():\\n    if not MI_PATH.exists():\\n        logger.error(f\\\"MI matrix not found: {MI_PATH}\\\")\\n        sys.exit(1)\\n    with open(MI_PATH) as f:\\n        data = json.load(f)\\n    logger.info(f\\\"Loaded MI matrix: {len(data['models'])} models\\\")\\n    return data\\n\\n\\ndef load_pairs():\\n    for ckpt_path in CKPT_FILES:\\n        if not ckpt_path.exists():\\n            continue\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        if \\\"pairs\\\" not in data:\\n            continue\\n        pairs = {}\\n        for ds in DATASETS:\\n            if ds in data[\\\"pairs\\\"]:\\n                pairs[ds] = data[\\\"pairs\\\"][ds][:300]\\n                logger.info(f\\\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\\\")\\n        if pairs:\\n            return pairs\\n    logger.error(\\\"No pairs found in any checkpoint file\\\")\\n    sys.exit(1)\\n\\n\\ndef _invert_winners(scores):\\n    swap = {\\\"A\\\": \\\"B\\\", \\\"B\\\": \\\"A\\\", \\\"tie\\\": \\\"tie\\\"}\\n    return [{**s, \\\"winner\\\": swap.get(s.get(\\\"winner\\\", \\\"tie\\\"), \\\"tie\\\")} for s in scores]\\n\\n\\ndef load_all_scores():\\n    clean = {ds: {} for ds in DATASETS}\\n    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}\\n\\n    for ckpt_path in CKPT_FILES:\\n        if not ckpt_path.exists():\\n            continue\\n        logger.info(f\\\"Loading checkpoint: {ckpt_path.name}\\\")\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        for ds in DATASETS:\\n            for mid, scores in data.get(\\\"clean_scores\\\", {}).get(ds, {}).items():\\n                if mid not in clean[ds]:\\n                    clean[ds][mid] = scores\\n            for atk in ATTACKS:\\n                for mid, scores in data.get(\\\"attacked_scores\\n\\n... [截断: 输出过长，省略 10848 字符] ...\\n\\ngger.info(\\n                f\\\"  Adaptive: K_eff B={adaptive_ols.get('keff_beta', 0):+.4f} \\\"\\n                f\\\"p={adaptive_ols.get('keff_p', 1):.4f} R2={adaptive_ols.get('R2', 0):.4f}\\\"\\n            )\\n            logger.info(\\n                f\\\"  RF:       K_eff B={rf_ols.get('keff_beta', 0):+.4f} \\\"\\n                f\\\"p={rf_ols.get('keff_p', 1):.4f} R2={rf_ols.get('R2', 0):.4f}\\\"\\n            )\\n            logger.info(f\\\"  dR2={delta_R2:+.4f}  K_eff gains significance: {keff_gains}\\\")\\n            if n_hk_le >= 5:\\n                logger.info(\\n                    f\\\"  High-K/Low-eta panels ({n_hk_le}): \\\"\\n                    f\\\"mean benefit={hk_le_benefit:+.4f} p={hk_le_pval}\\\"\\n                )\\n\\n    # ── Summary ──\\n    valid = {k: v for k, v in condition_results.items() if not v.get(\\\"skipped\\\")}\\n    nv = len(valid)\\n\\n    if nv > 0:\\n        n_adapt_sig = sum(\\n            1 for v in valid.values()\\n            if v[\\\"adaptive\\\"].get(\\\"keff_p\\\", 1) < 0.05 and v[\\\"adaptive\\\"].get(\\\"keff_beta\\\", 0) < 0\\n        )\\n        n_rf_sig = sum(\\n            1 for v in valid.values()\\n            if v[\\\"random_fault\\\"].get(\\\"keff_p\\\", 1) < 0.05 and v[\\\"random_fault\\\"].get(\\\"keff_beta\\\", 0) < 0\\n        )\\n        mean_dR2 = float(np.mean([v[\\\"delta_R2\\\"] for v in valid.values()]))\\n        n_gains = sum(1 for v in valid.values() if v[\\\"keff_gains_significance\\\"])\\n\\n        parts = []\\n        parts.append(\\n            f\\\"K_eff significantly negative in {n_rf_sig}/{nv} conditions under RF \\\"\\n            f\\\"vs {n_adapt_sig}/{nv} under adaptive.\\\"\\n        )\\n        if mean_dR2 > 0:\\n            parts.append(\\n                f\\\"RF model explains more variance (mean dR2={mean_dR2:+.3f}), \\\"\\n                \\\"consistent with independent-error majority vote theory.\\\"\\n            )\\n        else:\\n            parts.append(\\n                f\\\"Adaptive model explains more variance (mean dR2={mean_dR2:+.3f}).\\\"\\n            )\\n        if n_gains > nv // 2:\\n            parts.append(\\n                f\\\"K_eff gains significance in {n_gains}/{nv} conditions under RF, \\\"\\n                \\\"suggesting diversity benefit is undermined by adaptive attacks.\\\"\\n            )\\n        interpretation = \\\" \\\".join(parts)\\n\\n        summary = {\\n            \\\"adaptive_keff_sig_negative\\\": f\\\"{n_adapt_sig}/{nv}\\\",\\n            \\\"random_fault_keff_sig_negative\\\": f\\\"{n_rf_sig}/{nv}\\\",\\n            \\\"mean_delta_R2\\\": mean_dR2,\\n            \\\"keff_gains_significance_count\\\": f\\\"{n_gains}/{nv}\\\",\\n            \\\"interpretation\\\": interpretation,\\n        }\\n    else:\\n        summary = {\\\"note\\\": \\\"No valid conditions to summarize\\\"}\\n\\n    output = {\\n        \\\"n_panels\\\": 455,\\n        \\\"n_simulations\\\": N_SIMS,\\n        \\\"n_samples_per_sim\\\": N_SAMPLES,\\n        \\\"models\\\": ALL_MODELS,\\n        \\\"conditions\\\": condition_results,\\n        \\\"summary\\\": summary,\\n    }\\n\\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\\n    out_path = OUTPUT_DIR / \\\"step5_random_fault_results.json\\\"\\n    with open(out_path, \\\"w\\\") as f:\\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\\n    logger.info(f\\\"\\\\nResults saved: {out_path}\\\")\\n\\n    logger.info(\\\"\\\\n\\\" + \\\"=\\\" * 60)\\n    logger.info(\\\"SUMMARY\\\")\\n    logger.info(\\\"=\\\" * 60)\\n    for k, v in summary.items():\\n        if k != \\\"interpretation\\\":\\n            logger.info(f\\\"  {k}: {v}\\\")\\n    if \\\"interpretation\\\" in summary:\\n        logger.info(f\\\"\\\\n  {summary['interpretation']}\\\")\\n\\n    # Comparison table\\n    valid_keys = [k for k in condition_results if not condition_results[k].get(\\\"skipped\\\")]\\n    logger.info(f\\\"\\\\n{'Condition':<35} {'Adap R2':>8} {'RF R2':>8} {'dR2':>7} {'Adap Kp':>8} {'RF Kp':>8} {'Gains':>5}\\\")\\n    logger.info(\\\"-\\\" * 85)\\n    for ck in valid_keys:\\n        r = condition_results[ck]\\n        a = r[\\\"adaptive\\\"]\\n        rf = r[\\\"random_fault\\\"]\\n        logger.info(\\n            f\\\"  {ck:<33} {a.get('R2', 0):>8.4f} {rf.get('R2', 0):>8.4f} \\\"\\n            f\\\"{r['delta_R2']:>+7.3f} {a.get('keff_p', 1):>8.4f} {rf.get('keff_p', 1):>8.4f} \\\"\\n            f\\\"{'Y' if r['keff_gains_significance'] else 'N':>5}\\\"\\n        )\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
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
Now I have a thorough understanding of all 4 scripts. Let me analyze the data loading patterns:

**Step 3 (MI Matrix):**
- `load_local_clean_scores()`: Loads clean scores from 2 checkpoint files (`_step2v3_checkpoint.json`, `_taxonomy_checkpoint.json`), nested `{clean_scores: {dataset: {model: [...]}}}`
- `load_api_clean_scores()`: Loads from individual files `{model}__{ds}__clean.json` in SCORES_DIR
- `merge_clean_scores()`: Merges both


- Only needs clean scores with hardcoded model lists

**Confound Diagnosis:**
- `load_local_individual_asr()` and `load_api_individual_asr()` compute ASR from checkpoint files and individual score files respectively, requiring clean scores, attacked scores, and pairs
- `merge_asr()` combines both sources
- Also loads the MI matrix from Step 3 output with hardcoded model lists

**Step 4 (Panel Regression):**
- `load_all_scores()` pulls clean and attacked scores from checkpoints for local models and individual files for API models, plus MI data

**Step 5 (Random Fault):**
- Uses the same `load_all_scores()` pattern with MI data and pairs loading

Looking back at the actual requirements, I realize the scripts already have the dual loading logic built in for both checkpoint and individual file formats. The 15-model lists are hardcoded throughout, and each script handles the appropriate data types—Step 3 only needs clean scores while the confound, panel regression, and random fault steps all need clean plus attacked scores and pairs.

But re-reading the task more carefully, I see the real goal isn't just to verify the scripts work—it's to refactor them. The task wants me to extract all this duplicated loading logic into a shared `unified_data_loader.py` module and then modify each script to use it instead. This is a DRY refactoring exercise. Let me check what's currently in the `src/` directory and whether this module already exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "47c41470-68e0-412c-bd2b-c55e2e719fdb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9hDh84vLkwAbNvUJ2a2vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15319,
      "cache_read_input_tokens": 25769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15319
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

4 个脚本已读完。检查现有目录结构和数据文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "1831a7c6-07b8-400b-8e4c-6d56c0d11c5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9hDh84vLkwAbNvUJ2a2vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15319,
      "cache_read_input_tokens": 25769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15319
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01CA4Uow3uH1vE8N8UkZAtSf`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "ls /root/cert_manip_resist_eval/src/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "8d6eb6fb-64c3-49bb-afcc-086c6ff6d9ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9hDh84vLkwAbNvUJ2a2vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15319,
      "cache_read_input_tokens": 25769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15319
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

_source line 20 · 2026-05-22T14:56:36.651Z_

<details><summary>↩ Tool result · `toolu_01CA4Uow3uH1vE8N8UkZAtSf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"__init__.py\\n__pycache__\\napi_judge_service.py\\nattacks.py\\nconfig.py\\ncorrelation.py\\neval_pipeline.py\\njudge_service.py\\nkeff.py\\npanel_selection.py\\npanels.py\\nscaling.py\\nutils.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "e2f47753-27b5-4846-a385-0a8ad17ec9b5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"__init__.py\\\\n__pycache__\\\\napi_judge_service.py\\\\nattacks.py\\\\nconfig.py\\\\ncorrelation.py\\\\neval_pipeline.py\\\\njudge_service.py\\\\nkeff.py\\\\npanel_selection.py\\\\npanels.py\\\\nscaling.py\\\\nutils.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"__init__.py\\n__pycache__\\napi_judge_service.py\\nattacks.py\\nconfig.py\\ncorrelation.py\\neval_pipeline.py\\njudge_service.py\\nkeff.py\\npanel_selection.py\\npanels.py\\nscaling.py\\nutils.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PsUGEzSeD11e7hXc6DbsWF`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "ls /root/cert_manip_resist_eval/artifacts/results/plan001/individual_scores/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "3a19c723-6ccb-45de-844a-9845841eb618",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9hDh84vLkwAbNvUJ2a2vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15319,
      "cache_read_input_tokens": 25769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15319
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

_source line 22 · 2026-05-22T14:56:43.167Z_

<details><summary>↩ Tool result · `toolu_01PsUGEzSeD11e7hXc6DbsWF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"claude-3-haiku__arc_challenge__authority_bias.json\\nclaude-3-haiku__arc_challenge__clean.json\\nclaude-3-haiku__arc_challenge__position_bias.json\\nclaude-3-haiku__arc_challenge__prompt_injection.json\\nclaude-3-haiku__arc_challenge__score_manipulation.json\\nclaude-3-haiku__arc_challenge__sycophancy.json\\nclaude-3-haiku__arc_challenge__verbosity_bias.json\\nclaude-3-haiku__mmlu__authority_bias.json\\nclaude-3-haiku__mmlu__clean.json\\nclaude-3-haiku__mmlu__position_bias.json\\nclaude-3-haiku__mmlu__prompt_injection.json\\nclaude-3-haiku__mmlu__score_manipulation.json\\nclaude-3-haiku__mmlu__sycophancy.json\\nclaude-3-haiku__mmlu__verbosity_bias.json\\ngpt-4o__arc_challenge__clean.json\\ngpt-4o__arc_challenge__prompt_injection.json\\ngpt-4o__mmlu__authority_bias.json\\ngpt-4o__mmlu__clean.json\\ngpt-4o__mmlu__position_bias.json\\ngpt-4o__mmlu__prompt_injection.json\\ngpt-4o__mmlu__score_manipulation.json\\ngpt-4o__mmlu__sycophancy.json\\ngpt-4o__mmlu__verbosity_bias.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "3771ed80-b37a-41eb-9f22-319f1c54f235",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"claude-3-haiku__arc_challenge__authority_bias.json\\\\nclaude-3-haiku__arc_challenge__clean.json\\\\nclaude-3-haiku__arc_challenge__position_bias.json\\\\nclaude-3-haiku__arc_challenge__prompt_injection.json\\\\nclaude-3-haiku__arc_challenge__score_manipulation.json\\\\nclaude-3-haiku__arc_challenge__sycophancy.json\\\\nclaude-3-haiku__arc_challenge__verbosity_bias.json\\\\nclaude-3-haiku__mmlu__authority_bias.json\\\\nclaude-3-haiku__mmlu__clean.json\\\\nclaude-3-haiku__mmlu__position_bias.json\\\\nclaude-3-haiku__mmlu__prompt_injection.json\\\\nclaude-3-haiku__mmlu__score_manipulation.json\\\\nclaude-3-haiku__mmlu__sycophancy.json\\\\nclaude-3-haiku__mmlu__verbosity_bias.json\\\\ngpt-4o__arc_challenge__clean.json\\\\ngpt-4o__arc_challenge__prompt_injection.json\\\\ngpt-4o__mmlu__authority_bias.json\\\\ngpt-4o__mmlu__clean.json\\\\ngpt-4o__mmlu__position_bias.json\\\\ngpt-4o__mmlu__prompt_injection.json\\\\ngpt-4o__mmlu__score_manipulation.json\\\\ngpt-4o__mmlu__sycophancy.json\\\\ngpt-4o__mmlu__verbosity_bias.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"claude-3-haiku__arc_challenge__authority_bias.json\\nclaude-3-haiku__arc_challenge__clean.json\\nclaude-3-haiku__arc_challenge__position_bias.json\\nclaude-3-haiku__arc_challenge__prompt_injection.json\\nclaude-3-haiku__arc_challenge__score_manipulation.json\\nclaude-3-haiku__arc_challenge__sycophancy.json\\nclaude-3-haiku__arc_challenge__verbosity_bias.json\\nclaude-3-haiku__mmlu__authority_bias.json\\nclaude-3-haiku__mmlu__clean.json\\nclaude-3-haiku__mmlu__position_bias.json\\nclaude-3-haiku__mmlu__prompt_injection.json\\nclaude-3-haiku__mmlu__score_manipulation.json\\nclaude-3-haiku__mmlu__sycophancy.json\\nclaude-3-haiku__mmlu__verbosity_bias.json\\ngpt-4o__arc_challenge__clean.json\\ngpt-4o__arc_challenge__prompt_injection.json\\ngpt-4o__mmlu__authority_bias.json\\ngpt-4o__mmlu__clean.json\\ngpt-4o__mmlu__position_bias.json\\ngpt-4o__mmlu__prompt_injection.json\\ngpt-4o__mmlu__score_manipulation.json\\ngpt-4o__mmlu__sycophancy.json\\ngpt-4o__mmlu__verbosity_bias.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Mcyry4UW11JcXbWnBtzhW7`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "ls /root/cert_manip_resist_eval/artifacts/results/_step2v3_checkpoint.json /root/cert_manip_resist_eval/artifacts/results/_taxonomy_checkpoint.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "7df78e28-1880-468e-b726-5922c47ffad6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9hDh84vLkwAbNvUJ2a2vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15319,
      "cache_read_input_tokens": 25769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15319
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

_source line 24 · 2026-05-22T14:56:44.417Z_

<details><summary>↩ Tool result · `toolu_01Mcyry4UW11JcXbWnBtzhW7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/cert_manip_resist_eval/artifacts/results/_step2v3_checkpoint.json\\n/root/cert_manip_resist_eval/artifacts/results/_taxonomy_checkpoint.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "c32c2a53-a1bd-49d8-b0d4-2918aad5397d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/cert_manip_resist_eval/artifacts/results/_step2v3_checkpoint.json\\\\n/root/cert_manip_resist_eval/artifacts/results/_taxonomy_checkpoint.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/cert_manip_resist_eval/artifacts/results/_step2v3_checkpoint.json\\n/root/cert_manip_resist_eval/artifacts/results/_taxonomy_checkpoint.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture:

**Current state:**
- 4 scripts already have 15-model lists hardcoded and dual loading logic
- Individual scores dir has: claude-3-haiku (all 14 conditions) + gpt-4o (partial - 8 conditions)
- Both checkpoint files exist
- `src/` has various modules but no `unified_data_loader.py`

**Analysis of the 4 scripts' data loading:**

1. **Step 3 (MI Matrix):** Only needs clean scores. 

2. **Confound Diagnosis:** Needs clean + attacked scores + pairs. Has functions to load individual ASR data locally and from API, then merges them and computes ASR internally.

3. **Step 4 (Panel Regression):** Needs clean + attacked scores + pairs + MI data. Has its own function that loads all scores and returns them organized by dataset, attack type, and model.

4. **Step 5 (Random Fault):** Uses the same pattern as Step 4 with an identical score-loading function.

The unified loader should consolidate this by providing a single function that loads clean and attacked scores from both checkpoint and individual file formats, returning a consistent dictionary structure. Steps 4 and 5 already have nearly identical implementations, and the confound script computes ASR from the scores it loads separately, so I really just need to centralize the clean and attacked score loading logic.

My plan is to create a unified data loader module, update all four scripts to use it, build the pipeline launcher, and then run a dry test to verify everything works together.

Let me examine Step 4's score-loading function more closely since I need the complete version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "7bbad26f-3997-49ff-b267-168399e05488",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsJdWA7B81mX4xVQ3DSxDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 41088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2093
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

_source line 26_

Step 4 的 `load_all_scores()` 被截断了，需要看完整版。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "e3f502af-cc4f-4b81-8ce5-5acb3dadb735",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsJdWA7B81mX4xVQ3DSxDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 41088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2093
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

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PYibvU4JjGnTodmzYHbZs5`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "grep -n \"def load_all_scores\" /root/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "861de78f-f413-4826-aa6e-9f9f6bce4a01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsJdWA7B81mX4xVQ3DSxDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 41088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2093
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

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01N8UN45PeuhTsese7kK5cxT`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "head -200 /root/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "7edf603d-5d70-46d4-a86b-53ca157dfe28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsJdWA7B81mX4xVQ3DSxDg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 41088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2093
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

_source line 29 · 2026-05-22T14:57:00.782Z_

<details><summary>↩ Tool result · `toolu_01PYibvU4JjGnTodmzYHbZs5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"118:def load_all_scores():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "f6b4bc10-bcc0-49c4-8fd7-a492b60babf3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"118:def load_all_scores():\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"118:def load_all_scores():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T14:57:01.305Z_

<details><summary>↩ Tool result · `toolu_01N8UN45PeuhTsese7kK5cxT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Plan 001 Step 4: Panel regression — 455 panels × 12 conditions.\\n\\nInput:\\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\\n\\nOutput:\\n  - artifacts/results/plan001/panel_regression/step4_regression_results.json\\n\\nDependencies: numpy, scipy, statsmodels\\nOptional: pingouin (for partial_corr; manual fallback included)\\n\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport warnings\\nimport itertools\\nimport numpy as np\\nimport statsmodels.api as sm\\nfrom pathlib import Path\\nfrom scipy import optimize, stats, special\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\nfrom statsmodels.stats.multitest import multipletests\\n\\nfrom src.utils import setup_logging\\n\\nlogger = setup_logging(\\\"plan001_step4\\\")\\n\\n# ── Constants ────────────────────────────────────────────────────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4\\\", \\\"gpt-5.5\\\", \\\"gemini-2.5-pro\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4\\\", \\\"gpt-4o\\\", \\\"gemini-2.5-flash\\\",\\n    \\\"gpt-4o-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\nATTACKS = [\\n    \\\"prompt_injection\\\", \\\"sycophancy\\\", \\\"score_manipulation\\\",\\n    \\\"verbosity_bias\\\", \\\"position_bias\\\", \\\"authority_bias\\\",\\n]\\nEPS = 0.001\\n\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_PATH = PLAN001_DIR / \\\"mi_matrix\\\" / \\\"mi_matrix_15models.json\\\"\\nCKPT_FILES = [\\n    RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\",\\n    RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\",\\n]\\nOUTPUT_DIR = PLAN001_DIR / \\\"panel_regression\\\"\\n\\n\\n# ── JSON Helper ──────────────────────────────────────────────────────\\n\\ndef _json_default(obj):\\n    if isinstance(obj, np.floating):\\n        v = float(obj)\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\n    if isinstance(obj, np.integer):\\n        return int(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    if isinstance(obj, np.bool_):\\n        return bool(obj)\\n    raise TypeError(f\\\"Not JSON serializable: {type(obj)}\\\")\\n\\n\\n# ── Data Loading ─────────────────────────────────────────────────────\\n\\ndef load_mi_data():\\n    if not MI_PATH.exists():\\n        logger.error(f\\\"MI matrix not found: {MI_PATH}\\\")\\n        logger.error(\\\"Run Step 3 first: scripts/run_plan001_step3_mi_matrix.py\\\")\\n        sys.exit(1)\\n    with open(MI_PATH) as f:\\n        data = json.load(f)\\n    logger.info(f\\\"Loaded MI matrix: {len(data['models'])} models\\\")\\n    return data\\n\\n\\ndef load_pairs():\\n    for ckpt_path in CKPT_FILES:\\n        if not ckpt_path.exists():\\n            continue\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        if \\\"pairs\\\" not in data:\\n            continue\\n        pairs = {}\\n        for ds in DATASETS:\\n            if ds in data[\\\"pairs\\\"]:\\n                pairs[ds] = data[\\\"pairs\\\"][ds][:300]\\n                logger.info(f\\\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\\\")\\n        if pairs:\\n            return pairs\\n    logger.error(\\\"No pairs found in any checkpoint file\\\")\\n    sys.exit(1)\\n\\n\\ndef _invert_winners(scores):\\n    \\\"\\\"\\\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\\\"\\\"\\\"\\n    swap = {\\\"A\\\": \\\"B\\\", \\\"B\\\": \\\"A\\\", \\\"tie\\\": \\\"tie\\\"}\\n    return [{**s, \\\"winner\\\": swap.get(s.get(\\\"winner\\\", \\\"tie\\\"), \\\"tie\\\")} for s in scores]\\n\\n\\ndef load_all_scores():\\n    \\\"\\\"\\\"Load sample-level clean + attacked scores for all 15 models.\\n\\n    Returns:\\n        clean[ds][model_id] = [{\\\"winner\\\": ..., ...}, ...]\\n        attacked[ds][atk][model_id] = [{\\\"winner\\\": ..., ...}, ...]\\n    \\\"\\\"\\\"\\n    clean = {ds: {} for ds in DATASETS}\\n    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}\\n\\n    for ckpt_path in CKPT_FILES:\\n        if not ckpt_path.exists():\\n            continue\\n        logger.info(f\\\"Loading checkpoint: {ckpt_path.name}\\\")\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        for ds in DATASETS:\\n            for mid, scores in data.get(\\\"clean_scores\\\", {}).get(ds, {}).items():\\n                if mid not in clean[ds]:\\n                    clean[ds][mid] = scores\\n            for atk in ATTACKS:\\n                for mid, scores in data.get(\\\"attacked_scores\\\", {}).get(ds, {}).get(atk, {}).items():\\n                    if mid not in attacked[ds][atk]:\\n                        if atk == \\\"position_bias\\\":\\n                            scores = _invert_winners(scores)\\n                        attacked[ds][atk][mid] = scores\\n\\n    if SCORES_DIR.exists():\\n        logger.info(f\\\"Loading individual scores from {SCORES_DIR}\\\")\\n        for mid in ALL_MODELS:\\n            for ds in DATASETS:\\n                fp = SCORES_DIR / f\\\"{mid}__{ds}__clean.json\\\"\\n                if fp.exists() and mid not in clean[ds]:\\n                    with open(fp) as f:\\n                        clean[ds][mid] = json.load(f).get(\\\"scores\\\", [])\\n                for atk in ATTACKS:\\n                    fp = SCORES_DIR / f\\\"{mid}__{ds}__{atk}.json\\\"\\n                    if fp.exists() and mid not in attacked[ds][atk]:\\n                        with open(fp) as f:\\n                            scores = json.load(f).get(\\\"scores\\\", [])\\n                        if atk == \\\"position_bias\\\":\\n                            scores = _invert_winners(scores)\\n                        attacked[ds][atk][mid] = scores\\n\\n    for ds in DATASETS:\\n        nc = len(clean[ds])\\n        logger.info(f\\\"  {ds} clean: {nc}/{len(ALL_MODELS)}\\\")\\n        for atk in ATTACKS:\\n            na = len(attacked[ds][atk])\\n            if na > 0:\\n                logger.info(f\\\"  {ds} {atk}: {na}/{len(ALL_MODELS)}\\\")\\n\\n    return clean, attacked\\n\\n\\n# ── ASR Computation ──────────────────────────────────────────────────\\n\\ndef majority_vote(votes):\\n    counts = {\\\"A\\\": 0, \\\"B\\\": 0, \\\"tie\\\": 0}\\n    for v in votes:\\n        counts[v] = counts.get(v, 0) + 1\\n    mc = max(counts.values())\\n    winners = [k for k, c in counts.items() if c == mc]\\n    if len(winners) == 1:\\n        return winners[0]\\n    for w in winners:\\n        if w != \\\"tie\\\":\\n            return w\\n    return \\\"tie\\\"\\n\\n\\ndef compute_individual_asr(clean_list, attacked_list, pairs):\\n    n = min(len(clean_list), len(attacked_list), len(pairs))\\n    n_flips = n_correct = 0\\n    for i in range(n):\\n        gt = pairs[i][\\\"ground_truth_winner\\\"]\\n        if clean_list[i].get(\\\"winner\\\", \\\"tie\\\") == gt:\\n            n_correct += 1\\n            if attacked_list[i].get(\\\"winner\\\", \\\"tie\\\") != gt:\\n                n_flips += 1\\n    return n_flips / max(n_correct, 1)\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "4104ad36-dd0a-446b-9c7f-2c91ac47875f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Plan 001 Step 4: Panel regression — 455 panels × 12 conditions.\\\\n\\\\nInput:\\\\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\\\\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\\\\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\\\\n\\\\nOutput:\\\\n  - artifacts/results/plan001/panel_regression/step4_regression_results.json\\\\n\\\\nDependencies: numpy, scipy, statsmodels\\\\nOptional: pingouin (for partial_corr; manual fallback included)\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport os\\\\nos.environ[\\\\\\\"HF_HOME\\\\\\\"] = \\\\\\\"/root/autodl-tmp/.hf_cache\\\\\\\"\\\\n\\\\nimport sys\\\\nsys.path.insert(0, \\\\\\\"/root/cert_manip_resist_eval\\\\\\\")\\\\n\\\\nimport json\\\\nimport warnings\\\\nimport itertools\\\\nimport numpy as np\\\\nimport statsmodels.api as sm\\\\nfrom pathlib import Path\\\\nfrom scipy import optimize, stats, special\\\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\\\nfrom statsmodels.stats.multitest import multipletests\\\\n\\\\nfrom src.utils import setup_logging\\\\n\\\\nlogger = setup_logging(\\\\\\\"plan001_step4\\\\\\\")\\\\n\\\\n# ── Constants ────────────────────────────────────────────────────────\\\\nLOCAL_MODELS = [\\\\n    \\\\\\\"qwen2.5-72b\\\\\\\", \\\\\\\"llama3.1-70b\\\\\\\", \\\\\\\"mistral-large\\\\\\\",\\\\n    \\\\\\\"qwen2.5-32b\\\\\\\", \\\\\\\"qwen2.5-14b\\\\\\\", \\\\\\\"llama3.1-8b\\\\\\\",\\\\n]\\\\nAPI_MODELS = [\\\\n    \\\\\\\"claude-opus-4\\\\\\\", \\\\\\\"gpt-5.5\\\\\\\", \\\\\\\"gemini-2.5-pro\\\\\\\", \\\\\\\"gpt-4.1\\\\\\\",\\\\n    \\\\\\\"claude-sonnet-4\\\\\\\", \\\\\\\"gpt-4o\\\\\\\", \\\\\\\"gemini-2.5-flash\\\\\\\",\\\\n    \\\\\\\"gpt-4o-mini\\\\\\\", \\\\\\\"claude-3-haiku\\\\\\\",\\\\n]\\\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\\\nDATASETS = [\\\\\\\"mmlu\\\\\\\", \\\\\\\"arc_challenge\\\\\\\"]\\\\nATTACKS = [\\\\n    \\\\\\\"prompt_injection\\\\\\\", \\\\\\\"sycophancy\\\\\\\", \\\\\\\"score_manipulation\\\\\\\",\\\\n    \\\\\\\"verbosity_bias\\\\\\\", \\\\\\\"position_bias\\\\\\\", \\\\\\\"authority_bias\\\\\\\",\\\\n]\\\\nEPS = 0.001\\\\n\\\\nRESULTS_DIR = Path(\\\\\\\"/root/cert_manip_resist_eval/artifacts/results\\\\\\\")\\\\nPLAN001_DIR = RESULTS_DIR / \\\\\\\"plan001\\\\\\\"\\\\nSCORES_DIR = PLAN001_DIR / \\\\\\\"individual_scores\\\\\\\"\\\\nMI_PATH = PLAN001_DIR / \\\\\\\"mi_matrix\\\\\\\" / \\\\\\\"mi_matrix_15models.json\\\\\\\"\\\\nCKPT_FILES = [\\\\n    RESULTS_DIR / \\\\\\\"_taxonomy_checkpoint.json\\\\\\\",\\\\n    RESULTS_DIR / \\\\\\\"_step2v3_checkpoint.json\\\\\\\",\\\\n]\\\\nOUTPUT_DIR = PLAN001_DIR / \\\\\\\"panel_regression\\\\\\\"\\\\n\\\\n\\\\n# ── JSON Helper ──────────────────────────────────────────────────────\\\\n\\\\ndef _json_default(obj):\\\\n    if isinstance(obj, np.floating):\\\\n        v = float(obj)\\\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\\\n    if isinstance(obj, np.integer):\\\\n        return int(obj)\\\\n    if isinstance(obj, np.ndarray):\\\\n        return obj.tolist()\\\\n    if isinstance(obj, np.bool_):\\\\n        return bool(obj)\\\\n    raise TypeError(f\\\\\\\"Not JSON serializable: {type(obj)}\\\\\\\")\\\\n\\\\n\\\\n# ── Data Loading ─────────────────────────────────────────────────────\\\\n\\\\ndef load_mi_data():\\\\n    if not MI_PATH.exists():\\\\n        logger.error(f\\\\\\\"MI matrix not found: {MI_PATH}\\\\\\\")\\\\n        logger.error(\\\\\\\"Run Step 3 first: scripts/run_plan001_step3_mi_matrix.py\\\\\\\")\\\\n        sys.exit(1)\\\\n    with open(MI_PATH) as f:\\\\n        data = json.load(f)\\\\n    logger.info(f\\\\\\\"Loaded MI matrix: {len(data['models'])} models\\\\\\\")\\\\n    return data\\\\n\\\\n\\\\ndef load_pairs():\\\\n    for ckpt_path in CKPT_FILES:\\\\n        if not ckpt_path.exists():\\\\n            continue\\\\n        with open(ckpt_path) as f:\\\\n            data = json.load(f)\\\\n        if \\\\\\\"pairs\\\\\\\" not in data:\\\\n            continue\\\\n        pairs = {}\\\\n        for ds in DATASETS:\\\\n            if ds in data[\\\\\\\"pairs\\\\\\\"]:\\\\n                pairs[ds] = data[\\\\\\\"pairs\\\\\\\"][ds][:300]\\\\n                logger.info(f\\\\\\\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\\\\\\\")\\\\n        if pairs:\\\\n            return pairs\\\\n    logger.error(\\\\\\\"No pairs found in any checkpoint file\\\\\\\")\\\\n    sys.exit(1)\\\\n\\\\n\\\\ndef _invert_winners(scores):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    swap = {\\\\\\\"A\\\\\\\": \\\\\\\"B\\\\\\\", \\\\\\\"B\\\\\\\": \\\\\\\"A\\\\\\\", \\\\\\\"tie\\\\\\\": \\\\\\\"tie\\\\\\\"}\\\\n    return [{**s, \\\\\\\"winner\\\\\\\": swap.get(s.get(\\\\\\\"winner\\\\\\\", \\\\\\\"tie\\\\\\\"), \\\\\\\"tie\\\\\\\")} for s in scores]\\\\n\\\\n\\\\ndef load_all_scores():\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Load sample-level clean + attacked scores for all 15 models.\\\\n\\\\n    Returns:\\\\n        clean[ds][model_id] = [{\\\\\\\"winner\\\\\\\": ..., ...}, ...]\\\\n        attacked[ds][atk][model_id] = [{\\\\\\\"winner\\\\\\\": ..., ...}, ...]\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    clean = {ds: {} for ds in DATASETS}\\\\n    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}\\\\n\\\\n    for ckpt_path in CKPT_FILES:\\\\n        if not ckpt_path.exists():\\\\n            continue\\\\n        logger.info(f\\\\\\\"Loading checkpoint: {ckpt_path.name}\\\\\\\")\\\\n        with open(ckpt_path) as f:\\\\n            data = json.load(f)\\\\n        for ds in DATASETS:\\\\n            for mid, scores in data.get(\\\\\\\"clean_scores\\\\\\\", {}).get(ds, {}).items():\\\\n                if mid not in clean[ds]:\\\\n                    clean[ds][mid] = scores\\\\n            for atk in ATTACKS:\\\\n                for mid, scores in data.get(\\\\\\\"attacked_scores\\\\\\\", {}).get(ds, {}).get(atk, {}).items():\\\\n                    if mid not in attacked[ds][atk]:\\\\n                        if atk == \\\\\\\"position_bias\\\\\\\":\\\\n                            scores = _invert_winners(scores)\\\\n                        attacked[ds][atk][mid] = scores\\\\n\\\\n    if SCORES_DIR.exists():\\\\n        logger.info(f\\\\\\\"Loading individual scores from {SCORES_DIR}\\\\\\\")\\\\n        for mid in ALL_MODELS:\\\\n            for ds in DATASETS:\\\\n                fp = SCORES_DIR / f\\\\\\\"{mid}__{ds}__clean.json\\\\\\\"\\\\n                if fp.exists() and mid not in clean[ds]:\\\\n                    with open(fp) as f:\\\\n                        clean[ds][mid] = json.load(f).get(\\\\\\\"scores\\\\\\\", [])\\\\n                for atk in ATTACKS:\\\\n                    fp = SCORES_DIR / f\\\\\\\"{mid}__{ds}__{atk}.json\\\\\\\"\\\\n                    if fp.exists() and mid not in attacked[ds][atk]:\\\\n                        with open(fp) as f:\\\\n                            scores = json.load(f).get(\\\\\\\"scores\\\\\\\", [])\\\\n                        if atk == \\\\\\\"position_bias\\\\\\\":\\\\n                            scores = _invert_winners(scores)\\\\n                        attacked[ds][atk][mid] = scores\\\\n\\\\n    for ds in DATASETS:\\\\n        nc = len(clean[ds])\\\\n        logger.info(f\\\\\\\"  {ds} clean: {nc}/{len(ALL_MODELS)}\\\\\\\")\\\\n        for atk in ATTACKS:\\\\n            na = len(attacked[ds][atk])\\\\n            if na > 0:\\\\n                logger.info(f\\\\\\\"  {ds} {atk}: {na}/{len(ALL_MODELS)}\\\\\\\")\\\\n\\\\n    return clean, attacked\\\\n\\\\n\\\\n# ── ASR Computation ──────────────────────────────────────────────────\\\\n\\\\ndef majority_vote(votes):\\\\n    counts = {\\\\\\\"A\\\\\\\": 0, \\\\\\\"B\\\\\\\": 0, \\\\\\\"tie\\\\\\\": 0}\\\\n    for v in votes:\\\\n        counts[v] = counts.get(v, 0) + 1\\\\n    mc = max(counts.values())\\\\n    winners = [k for k, c in counts.items() if c == mc]\\\\n    if len(winners) == 1:\\\\n        return winners[0]\\\\n    for w in winners:\\\\n        if w != \\\\\\\"tie\\\\\\\":\\\\n            return w\\\\n    return \\\\\\\"tie\\\\\\\"\\\\n\\\\n\\\\ndef compute_individual_asr(clean_list, attacked_list, pairs):\\\\n    n = min(len(clean_list), len(attacked_list), len(pairs))\\\\n    n_flips = n_correct = 0\\\\n    for i in range(n):\\\\n        gt = pairs[i][\\\\\\\"ground_truth_winner\\\\\\\"]\\\\n        if clean_list[i].get(\\\\\\\"winner\\\\\\\", \\\\\\\"tie\\\\\\\") == gt:\\\\n            n_correct += 1\\\\n            if attacked_list[i].get(\\\\\\\"winner\\\\\\\", \\\\\\\"tie\\\\\\\") != gt:\\\\n                n_flips += 1\\\\n    return n_flips / max(n_correct, 1)\\\\n\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Plan 001 Step 4: Panel regression — 455 panels × 12 conditions.\\n\\nInput:\\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\\n\\nOutput:\\n  - artifacts/results/plan001/panel_regression/step4_regression_results.json\\n\\nDependencies: numpy, scipy, statsmodels\\nOptional: pingouin (for partial_corr; manual fallback included)\\n\\\"\\\"\\\"\\n\\nimport os\\nos.environ[\\\"HF_HOME\\\"] = \\\"/root/autodl-tmp/.hf_cache\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport warnings\\nimport itertools\\nimport numpy as np\\nimport statsmodels.api as sm\\nfrom pathlib import Path\\nfrom scipy import optimize, stats, special\\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\\nfrom statsmodels.stats.multitest import multipletests\\n\\nfrom src.utils import setup_logging\\n\\nlogger = setup_logging(\\\"plan001_step4\\\")\\n\\n# ── Constants ────────────────────────────────────────────────────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4\\\", \\\"gpt-5.5\\\", \\\"gemini-2.5-pro\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4\\\", \\\"gpt-4o\\\", \\\"gemini-2.5-flash\\\",\\n    \\\"gpt-4o-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\nATTACKS = [\\n    \\\"prompt_injection\\\", \\\"sycophancy\\\", \\\"score_manipulation\\\",\\n    \\\"verbosity_bias\\\", \\\"position_bias\\\", \\\"authority_bias\\\",\\n]\\nEPS = 0.001\\n\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_PATH = PLAN001_DIR / \\\"mi_matrix\\\" / \\\"mi_matrix_15models.json\\\"\\nCKPT_FILES = [\\n    RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\",\\n    RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\",\\n]\\nOUTPUT_DIR = PLAN001_DIR / \\\"panel_regression\\\"\\n\\n\\n# ── JSON Helper ──────────────────────────────────────────────────────\\n\\ndef _json_default(obj):\\n    if isinstance(obj, np.floating):\\n        v = float(obj)\\n        return None if (np.isnan(v) or np.isinf(v)) else v\\n    if isinstance(obj, np.integer):\\n        return int(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    if isinstance(obj, np.bool_):\\n        return bool(obj)\\n    raise TypeError(f\\\"Not JSON serializable: {type(obj)}\\\")\\n\\n\\n# ── Data Loading ─────────────────────────────────────────────────────\\n\\ndef load_mi_data():\\n    if not MI_PATH.exists():\\n        logger.error(f\\\"MI matrix not found: {MI_PATH}\\\")\\n        logger.error(\\\"Run Step 3 first: scripts/run_plan001_step3_mi_matrix.py\\\")\\n        sys.exit(1)\\n    with open(MI_PATH) as f:\\n        data = json.load(f)\\n    logger.info(f\\\"Loaded MI matrix: {len(data['models'])} models\\\")\\n    return data\\n\\n\\ndef load_pairs():\\n    for ckpt_path in CKPT_FILES:\\n        if not ckpt_path.exists():\\n            continue\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        if \\\"pairs\\\" not in data:\\n            continue\\n        pairs = {}\\n        for ds in DATASETS:\\n            if ds in data[\\\"pairs\\\"]:\\n                pairs[ds] = data[\\\"pairs\\\"][ds][:300]\\n                logger.info(f\\\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\\\")\\n        if pairs:\\n            return pairs\\n    logger.error(\\\"No pairs found in any checkpoint file\\\")\\n    sys.exit(1)\\n\\n\\ndef _invert_winners(scores):\\n    \\\"\\\"\\\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\\\"\\\"\\\"\\n    swap = {\\\"A\\\": \\\"B\\\", \\\"B\\\": \\\"A\\\", \\\"tie\\\": \\\"tie\\\"}\\n    return [{**s, \\\"winner\\\": swap.get(s.get(\\\"winner\\\", \\\"tie\\\"), \\\"tie\\\")} for s in scores]\\n\\n\\ndef load_all_scores():\\n    \\\"\\\"\\\"Load sample-level clean + attacked scores for all 15 models.\\n\\n    Returns:\\n        clean[ds][model_id] = [{\\\"winner\\\": ..., ...}, ...]\\n        attacked[ds][atk][model_id] = [{\\\"winner\\\": ..., ...}, ...]\\n    \\\"\\\"\\\"\\n    clean = {ds: {} for ds in DATASETS}\\n    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}\\n\\n    for ckpt_path in CKPT_FILES:\\n        if not ckpt_path.exists():\\n            continue\\n        logger.info(f\\\"Loading checkpoint: {ckpt_path.name}\\\")\\n        with open(ckpt_path) as f:\\n            data = json.load(f)\\n        for ds in DATASETS:\\n            for mid, scores in data.get(\\\"clean_scores\\\", {}).get(ds, {}).items():\\n                if mid not in clean[ds]:\\n                    clean[ds][mid] = scores\\n            for atk in ATTACKS:\\n                for mid, scores in data.get(\\\"attacked_scores\\\", {}).get(ds, {}).get(atk, {}).items():\\n                    if mid not in attacked[ds][atk]:\\n                        if atk == \\\"position_bias\\\":\\n                            scores = _invert_winners(scores)\\n                        attacked[ds][atk][mid] = scores\\n\\n    if SCORES_DIR.exists():\\n        logger.info(f\\\"Loading individual scores from {SCORES_DIR}\\\")\\n        for mid in ALL_MODELS:\\n            for ds in DATASETS:\\n                fp = SCORES_DIR / f\\\"{mid}__{ds}__clean.json\\\"\\n                if fp.exists() and mid not in clean[ds]:\\n                    with open(fp) as f:\\n                        clean[ds][mid] = json.load(f).get(\\\"scores\\\", [])\\n                for atk in ATTACKS:\\n                    fp = SCORES_DIR / f\\\"{mid}__{ds}__{atk}.json\\\"\\n                    if fp.exists() and mid not in attacked[ds][atk]:\\n                        with open(fp) as f:\\n                            scores = json.load(f).get(\\\"scores\\\", [])\\n                        if atk == \\\"position_bias\\\":\\n                            scores = _invert_winners(scores)\\n                        attacked[ds][atk][mid] = scores\\n\\n    for ds in DATASETS:\\n        nc = len(clean[ds])\\n        logger.info(f\\\"  {ds} clean: {nc}/{len(ALL_MODELS)}\\\")\\n        for atk in ATTACKS:\\n            na = len(attacked[ds][atk])\\n            if na > 0:\\n                logger.info(f\\\"  {ds} {atk}: {na}/{len(ALL_MODELS)}\\\")\\n\\n    return clean, attacked\\n\\n\\n# ── ASR Computation ──────────────────────────────────────────────────\\n\\ndef majority_vote(votes):\\n    counts = {\\\"A\\\": 0, \\\"B\\\": 0, \\\"tie\\\": 0}\\n    for v in votes:\\n        counts[v] = counts.get(v, 0) + 1\\n    mc = max(counts.values())\\n    winners = [k for k, c in counts.items() if c == mc]\\n    if len(winners) == 1:\\n        return winners[0]\\n    for w in winners:\\n        if w != \\\"tie\\\":\\n            return w\\n    return \\\"tie\\\"\\n\\n\\ndef compute_individual_asr(clean_list, attacked_list, pairs):\\n    n = min(len(clean_list), len(attacked_list), len(pairs))\\n    n_flips = n_correct = 0\\n    for i in range(n):\\n        gt = pairs[i][\\\"ground_truth_winner\\\"]\\n        if clean_list[i].get(\\\"winner\\\", \\\"tie\\\") == gt:\\n            n_correct += 1\\n            if attacked_list[i].get(\\\"winner\\\", \\\"tie\\\") != gt:\\n                n_flips += 1\\n    return n_flips / max(n_correct, 1)\\n\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture. Let me also check Step 5's `load_all_scores()` to confirm it's the same pattern.

The key observations:
1. All 4 scripts already have hardcoded 15-model lists (identical across scripts)
2. All scripts already handle both checkpoint and individual file formats
3. Step 4 and Step 5 have nearly identical `load_all_scores()` functions
4. Step 3 only loads clean scores
5. Confound script loads separately for ASR computation

The duplicated code across scripts:


- Model lists, datasets, attacks, and path constants
- The `_invert_winners()` helper function
- Nearly identical `load_all_scores()` implementations in Step 4 and Step 5
- Clean score loading in Step 3 (a subset of the full pattern)
- Score loading with ASR computation in the Confound script

My plan is to create a unified data loader module that consolidates all these constants and functions, then build a `load_all_scores()` function that handles both clean and attacked scores, plus a `load_pairs()` function to replace the duplicated logic across scripts.

I'll also need a `load_mi_data()` function to read from the MI matrix file. Once that's done, I can modify each script to import from the unified loader and strip out the redundant code, then create a pipeline launcher and run a dry-test.

Let me start writing the unified data loader module with all the constants, helper functions, and data loading utilities. Setting up the attack types and directory structure...

Now I'm defining helper functions to load and process evaluation scores across different attack conditions and models. Loading individual score files... Writing file loading logic... Finishing the MI data loading function, then moving into a validation function that checks whether all models have the expected number of samples across datasets and attack types, flagging any missing data or count mismatches.

Now I'm thinking through what minimal changes need to be made to each script to swap out the data loading logic.

For the Step 3 script, I need to replace the separate local and API loading functions with a unified loader, remove the hardcoded model lists, and eliminate the path constants for checkpoints and scores directories.

For the Confound script, it's a bit trickier since it computes ASR internally from the loaded scores rather than loading pre-computed ASR values, so I need to figure out how to integrate the new loader while preserving that computation pattern.

Looking at Steps 4 and 5, they'll follow a similar pattern of replacing their local loading functions with imports from the unified loader and removing duplicated model lists and path helpers.

Actually, I'm realizing the scripts are already working fine for the 15 models we have. The real benefit of creating a unified loader is eliminating code duplication across all four scripts and having a single place to update if the data format changes. Let me start writing out the actual implementation.

The most straightforward approach is to write the unified loader directly to the server first, then systematically update each script to import from it rather than defining their own loading functions. Since these scripts are quite long with data loading logic scattered throughout, I'll need to carefully extract and consolidate those functions into the loader, then update the imports in each script.

For the step 3 scripts, I'm removing the duplicate model and dataset definitions, keeping only the directory paths they actually use, and replacing their individual load calls with a single call to the unified loader. For Confound, I need to import additional utilities like the attack definitions and helper functions it depends on.

The key insight is that both scripts ultimately need ASR computed from clean and attacked scores—the unified loader already handles the position bias inversion during loading, so I can simplify the confound script to load scores once and compute ASR directly from them rather than maintaining separate loading paths for local and API models. Writing the ASR computation function...

I'm realizing the cleanest approach is to create a unified loader that provides raw scores, then have each script handle its own ASR calculations. Rather than completely rewriting every script, I can make surgical changes—just swap out the data loading calls in main() and remove the duplicate constants and loading functions that are now handled by the unified loader. Let me write the unified loader first, then patch each script with those targeted modifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "b32c3adc-2668-4944-8266-87cb890add17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJWpbkvSJ32synMisqcX15",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3796,
      "cache_read_input_tokens": 43181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3796
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

检查本地是否有代码副本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "496e04a7-5333-46fc-9bd4-29f27340582f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJWpbkvSJ32synMisqcX15",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3796,
      "cache_read_input_tokens": 43181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3796
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

<details open><summary>🔧 Tool call — Bash · `toolu_01BYu8DqBsC2a98gxtJHeeR5`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/",
  "description": "List local project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "d4180267-20fc-432f-8630-8dc95fe06df6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJWpbkvSJ32synMisqcX15",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3796,
      "cache_read_input_tokens": 43181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3796
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

_source line 34 · 2026-05-22T14:58:10.889Z_

<details><summary>↩ Tool result · `toolu_01BYu8DqBsC2a98gxtJHeeR5`</summary>

```text
AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
decisions.lock
decisions.yaml
distill_tmp
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.yaml
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
paper_framing.md
registry.lock
registry.yaml
report.md
requirements.txt
scoring
scripts
src
study_status.lock
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "442689d8-c9a3-46d7-8b3a-fe03e528a0c6",
  "tool_use_result": {
    "stdout": "AGENTS.md\nROADMAP.lock\nROADMAP.md\nartifacts\ncheckpoints\ndecisions.lock\ndecisions.yaml\ndistill_tmp\ndocs\ndream_registry.lock\ndream_registry.yaml\ndream_registry.yaml.bak\nexperiment_plan.yaml\nliterature_map.yaml\nlogs\nmemory.md\nmistakes.lock\nmistakes.yaml\npaper_framing.md\nregistry.lock\nregistry.yaml\nreport.md\nrequirements.txt\nscoring\nscripts\nsrc\nstudy_status.lock",
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

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jr6GDxrEJBR4SCip7QVwsx`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/ 2>/dev/null || echo \"NO_SRC_DIR\"",
  "description": "Check local src directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "088358b6-9e35-4737-9988-ed02feb19c2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AJWpbkvSJ32synMisqcX15",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3796,
      "cache_read_input_tokens": 43181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3796
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

_source line 36 · 2026-05-22T14:58:11.365Z_

<details><summary>↩ Tool result · `toolu_01Jr6GDxrEJBR4SCip7QVwsx`</summary>

```text
__init__.py
__pycache__
attacks.py
config.py
correlation.py
eval_pipeline.py
judge_service.py
keff.py
panels.py
scaling.py
utils.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "2bf90260-59a1-4a86-a7c1-989fc8429247",
  "tool_use_result": {
    "stdout": "__init__.py\n__pycache__\nattacks.py\nconfig.py\ncorrelation.py\neval_pipeline.py\njudge_service.py\nkeff.py\npanels.py\nscaling.py\nutils.py",
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

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Good, there's a local src directory. Let me also check the local scripts directory. However, I notice the local src doesn't have `api_judge_service.py` and `panel_selection.py` that were on the server. The server might have a different version. Let me check the local scripts too.

Actually, the approach should be:
1. Write files locally
2. SCP them to the server
3. Test on the server

But wait, is this a git repo? Let me check. The system said "Is a git repository: false" for the working directory. But the server might have git.


I'll write the unified loader locally along with the modified scripts, then transfer everything to the server via SCP. First, let me see what scripts are already in the local directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "408bd3ff-e104-4b50-8f73-8e0ea2446efd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vt11oj86e51q22BgSL31no",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5227,
      "cache_read_input_tokens": 46977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5227
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

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01WRLpjCJ6uSkq5rMsc526Dp`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_*.py 2>/dev/null",
  "description": "List local plan001 scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "b2a5cefc-692b-43ad-b13a-1b79ce013eca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vt11oj86e51q22BgSL31no",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5227,
      "cache_read_input_tokens": 46977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5227
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

_source line 39 · 2026-05-22T14:58:19.273Z_

<details><summary>↩ Tool result · `toolu_01WRLpjCJ6uSkq5rMsc526Dp`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_confound_diagnosis.py
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step1_api_scoring.py
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step1_parallel_v2.py
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py
/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step5_random_fault.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "31d008f9-ba11-4634-816b-58e271fb053c",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_confound_diagnosis.py\n/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step1_api_scoring.py\n/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step1_parallel_v2.py\n/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py\n/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py\n/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step5_random_fault.py",
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

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
The local copy has all the scripts. Let me verify the local scripts match the server versions, then write locally and scp.

Actually, let me just proceed directly. I'll:
1. Write `src/unified_data_loader.py` locally
2. Modify the 4 scripts locally
3. Write the pipeline launcher script
4. SCP everything to the server
5. Dry-run test

Let me read the local versions of the scripts to make sure they're current.

Actually, the server versions are what I already read - let me just compare a few lines to confirm. But to save time, let me just trust the server versions are authoritative (I already read them) and write accordingly. I'll write locally then scp.


Now I'm starting to write the unified data loader module. I also need to check the full content of the Step 4 and Step 5 scripts locally since the server output was truncated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "95737a6a-45d5-404e-b44f-5d2c457d8df8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtxhqJbYPLcGhMDMXSfJQ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 52204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 41_

Let me read the local scripts to get full content (server output was truncated).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "e50b316e-8d3b-44fb-a212-317e44d4f280",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtxhqJbYPLcGhMDMXSfJQ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 52204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01JB8UCkvfx71SZorXKFQJKq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "07f90149-9ef4-41a2-afcc-214e98c62ae1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtxhqJbYPLcGhMDMXSfJQ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 52204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_0132VTuZzEWg52EG6htFx85M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_confound_diagnosis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "283f88f2-f834-4492-aee7-bea473f23739",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtxhqJbYPLcGhMDMXSfJQ2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 52204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 44 · 2026-05-22T14:58:28.582Z_

<details><summary>↩ Tool result · `toolu_0132VTuZzEWg52EG6htFx85M`</summary>

```text
1	#!/usr/bin/env python3
2	"""Plan 001: K_eff vs η_max confound diagnosis across all C(15,3) panels."""
3	
4	import os
5	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
6	
7	import sys
8	sys.path.insert(0, "/root/cert_manip_resist_eval")
9	
10	import json
11	import itertools
12	import numpy as np
13	import matplotlib
14	matplotlib.use("Agg")
15	import matplotlib.pyplot as plt
16	from pathlib import Path
17	from scipy import stats
18	
19	from src.utils import setup_logging
20	
21	logger = setup_logging("plan001_confound")
22	
23	# ── Model lists ──────────────────────────────────────────────────────
24	LOCAL_MODELS = [
25	    "qwen2.5-72b", "llama3.1-70b", "mistral-large",
26	    "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b",
27	]
28	API_MODELS = [
29	    "claude-opus-4", "gpt-5.5", "gemini-2.5-pro", "gpt-4.1",
30	    "claude-sonnet-4", "gpt-4o", "gemini-2.5-flash",
31	    "gpt-4o-mini", "claude-3-haiku",
32	]
33	ALL_MODELS = LOCAL_MODELS + API_MODELS
34	DATASETS = ["mmlu", "arc_challenge"]
35	ATTACKS = [
36	    "prompt_injection", "sycophancy", "score_manipulation",
37	    "verbosity_bias", "position_bias", "authority_bias",
38	]
39	
40	# ── Paths ────────────────────────────────────────────────────────────
41	RESULTS_DIR = Path("/root/cert_manip_resist_eval/artifacts/results")
42	PLAN001_DIR = RESULTS_DIR / "plan001"
43	SCORES_DIR = PLAN001_DIR / "individual_scores"
44	MI_MATRIX_PATH = PLAN001_DIR / "mi_matrix" / "mi_matrix_15models.json"
45	
46	STEP2V3_CKPT = RESULTS_DIR / "_step2v3_checkpoint.json"
47	TAXONOMY_CKPT = RESULTS_DIR / "_taxonomy_checkpoint.json"
48	
49	# Attack → checkpoint mapping for local models
50	LOCAL_ATTACK_CKPT = {
51	    "prompt_injection": STEP2V3_CKPT,
52	    "sycophancy": STEP2V3_CKPT,
53	    "score_manipulation": STEP2V3_CKPT,
54	    "verbosity_bias": TAXONOMY_CKPT,
55	    "position_bias": TAXONOMY_CKPT,
56	    "authority_bias": TAXONOMY_CKPT,
57	}
58	
59	
60	def _invert_winners(scores):
61	    """Invert A<->B winner labels for position bias scores (swapped pair orientation)."""
62	    swap = {"A": "B", "B": "A", "tie": "tie"}
63	    return [{**s, "winner": swap.get(s.get("winner", "tie"), "tie")} for s in scores]
64	
65	
66	def compute_asr_from_scores(clean_scores, attacked_scores, pairs):
67	    """Compute individual judge ASR: fraction of clean-correct flipped by attack."""
68	    n_flips = 0
69	    n_total = 0
70	    for clean, attacked, pair in zip(clean_scores, attacked_scores, pairs):
71	        gt = pair.get("ground_truth_winner")
72	        cw = clean.get("winner") if isinstance(clean, dict) else None
73	        aw = attacked.get("winner") if isinstance(attacked, dict) else None
74	        if cw == gt:
75	            n_total += 1
76	            if aw != gt:
77	                n_flips += 1
78	    return n_flips / max(n_total, 1)
79	
80	
81	def load_local_individual_asr():
82	    """Load per-model ASR for local models from checkpoint files.
83	
84	    Returns: {dataset: {attack: {model_id: asr}}}
85	    """
86	    asr_data = {}
87	    ckpt_cache = {}
88	
89	    for attack in ATTACKS:
90	        ckpt_path = LOCAL_ATTACK_CKPT[attack]
91	        if str(ckpt_path) not in ckpt_cache:
92	            if not ckpt_path.exists():
93	                logger.warning(f"Checkpoint not found: {ckpt_path}")
94	                continue
95	            with open(ckpt_path) as f:
96	                ckpt_cache[str(ckpt_path)] = json.load(f)
97	        data = ckpt_cache[str(ckpt_path)]
98	
99	        for ds in DATASETS:
100	            if ds not in asr_data:
101	                asr_data[ds] = {}
102	            if attack not in asr_data[ds]:
103	                asr_data[ds][attack] = {}
104	
105	            clean_all = data.get("clean_scores", {}).get(ds, {})
106	            atk_all = data.get("attacked_scores", {}).get(ds, {}).get(attack, {})
107	            pairs = data.get("pairs", {}).get(ds, [])
108	
109	            if not pairs:
110	                logger.warning(f"No pairs for {ds} in {ckpt_path.name}")
111	                continue
112	
113	            for model_id in LOCAL_MODELS:
114	                if model_id not in clean_all or model_id not in atk_all:
115	                    continue
116	                atk_scores = atk_all[model_id]
117	                if attack == "position_bias":
118	                    atk_scores = _invert_winners(atk_scores)
119	                asr = compute_asr_from_scores(
120	                    clean_all[model_id], atk_scores, pairs
121	                )
122	                asr_data[ds][attack][model_id] = asr
123	
124	    return asr_data
125	
126	
127	def load_api_individual_asr():
128	    """Load per-model ASR for API models from individual score files.
129	
130	    Returns: {dataset: {attack: {model_id: asr}}}
131	    """
132	    asr_data = {}
133	    for model_id in API_MODELS:
134	        for ds in DATASETS:
135	            if ds not in asr_data:
136	                asr_data[ds] = {}
137	
138	            clean_path = SCORES_DIR / f"{model_id}__{ds}__clean.json"
139	            if not clean_path.exists():
140	                continue
141	            with open(clean_path) as f:
142	                clean_data = json.load(f)
143	            clean_scores = clean_data.get("scores", [])
144	
145	            for attack in ATTACKS:
146	                if attack not in asr_data[ds]:
147	                    asr_data[ds][attack] = {}
148	
149	                atk_path = SCORES_DIR / f"{model_id}__{ds}__{attack}.json"
150	                if not atk_path.exists():
151	                    continue
152	                with open(atk_path) as f:
153	                    atk_data = json.load(f)
154	
155	                asr = atk_data.get("asr")
156	                if asr is not None:
157	                    asr_data[ds][attack][model_id] = asr
158	                else:
159	                    logger.warning(
160	                        f"No ASR in {atk_path.name}, skipping"
161	                    )
162	
163	    return asr_data
164	
165	
166	def merge_asr(local_asr, api_asr):
167	    """Merge local and API ASR data."""
168	    merged = {}
169	    for ds in DATASETS:
170	        merged[ds] = {}
171	        for attack in ATTACKS:
172	            merged[ds][attack] = {}
173	            for src in [local_asr, api_asr]:
174	                if ds in src and attack in src[ds]:
175	                    merged[ds][attack].update(src[ds][attack])
176	    return merged
177	
178	
179	def load_mi_matrix():
180	    """Load MI matrix from Step 3 output."""
181	    if not MI_MATRIX_PATH.exists():
182	        logger.error(f"MI matrix not found: {MI_MATRIX_PATH}")
183	        sys.exit(1)
184	    with open(MI_MATRIX_PATH) as f:
185	        data = json.load(f)
186	    return data
187	
188	
189	def mi_based_keff(mi_matrix_np, model_indices):
190	    """K_eff = (1/K) * sum_i [1 + sum_{j!=i} exp(-2 * MI_ij)]"""
191	    K = len(model_indices)
192	    if K <= 1:
193	        return 1.0
194	    keff = 0.0
195	    for i_idx in model_indices:
196	        term = 1.0
197	        for j_idx in model_indices:
198	            if i_idx != j_idx:
199	                term += np.exp(-2 * mi_matrix_np[i_idx, j_idx])
200	        keff += term
201	    return keff / K
202	
203	
204	def classify_panel(model_ids):
205	    """Classify panel by composition for scatter plot coloring."""
206	    n_api = sum(1 for m in model_ids if m in API_MODELS)
207	    if n_api == 3:
208	        return "all_api"
209	    elif n_api == 0:
210	        return "all_local"
211	    elif n_api == 2:
212	        return "2api_1local"
213	    else:
214	        return "1api_2local"
215	
216	
217	PANEL_COLORS = {
218	    "all_api": "#e74c3c",
219	    "all_local": "#2ecc71",
220	    "2api_1local": "#e67e22",
221	    "1api_2local": "#3498db",
222	}
223	
224	PANEL_LABELS = {
225	    "all_api": "3 API",
226	    "all_local": "3 Local",
227	    "2api_1local": "2 API + 1 Local",
228	    "1api_2local": "1 API + 2 Local",
229	}
230	
231	
232	def run_confound_analysis(mi_data, asr_data):
233	    """Run K_eff vs η_max analysis for all conditions."""
234	    models = mi_data["models"]
235	    model_to_idx = {m: i for i, m in enumerate(models)}
236	    conditions = {}
237	
238	    for ds in DATASETS:
239	        mi_mat = np.array(mi_data["mi_matrix"][ds])
240	
241	        for attack in ATTACKS:
242	            cond_key = f"{ds}×{attack}"
243	            model_asrs = asr_data.get(ds, {}).get(attack, {})
244	
245	            if len(model_asrs) < 3:
246	                logger.warning(
247	                    f"  {cond_key}: only {len(model_asrs)} models have ASR, "
248	                    f"need ≥3 for panel construction. Skipping."
249	                )
250	                conditions[cond_key] = {
251	                    "pearson_r": None,
252	                    "p_value": None,
253	                    "verdict": "INSUFFICIENT_DATA",
254	                    "n_panels": 0,
255	                    "n_models_with_asr": len(model_asrs),
256	                }
257	                continue
258	
259	            available_models = [
260	                m for m in models if m in model_asrs
261	            ]
262	
263	            keffs = []
264	            eta_maxs = []
265	            panel_types = []
266	
267	            for combo in itertools.combinations(available_models, 3):
268	                indices = [model_to_idx[m] for m in combo]
269	                keff = mi_based_keff(mi_mat, indices)
270	                eta_max = max(model_asrs[m] for m in combo)
271	
272	                keffs.append(keff)
273	                eta_maxs.append(eta_max)
274	                panel_types.append(classify_panel(combo))
275	
276	            keffs = np.array(keffs)
277	            eta_maxs = np.array(eta_maxs)
278	
279	            if len(keffs) < 3 or np.std(keffs) < 1e-10 or np.std(eta_maxs) < 1e-10:
280	                r, p = 0.0, 1.0
281	            else:
282	                r, p = stats.pearsonr(keffs, eta_maxs)
283	
284	            if r < -0.7:
285	                verdict = "CONFOUND_SEVERE"
286	            elif r <= -0.5:
287	                verdict = "CONFOUND_MODERATE"
288	            else:
289	                verdict = "CONFOUND_BROKEN"
290	
291	            conditions[cond_key] = {
292	                "pearson_r": float(r),
293	                "p_value": float(p),
294	                "verdict": verdict,
295	                "n_panels": len(keffs),
296	                "n_models_with_asr": len(available_models),
297	                "keffs": keffs.tolist(),
298	                "eta_maxs": eta_maxs.tolist(),
299	                "panel_types": panel_types,
300	            }
301	            logger.info(
302	                f"  {cond_key}: r={r:.3f}, p={p:.4f}, "
303	                f"verdict={verdict}, n_panels={len(keffs)}"
304	            )
305	
306	    return conditions
307	
308	
309	def plot_scatter_grid(conditions, output_path):
310	    """Plot K_eff vs η_max scatter grid."""
311	    valid_conds = {
312	        k: v for k, v in conditions.items()
313	        if v.get("pearson_r") is not None
314	    }
315	    n = len(valid_conds)
316	    if n == 0:
317	        logger.warning("No valid conditions to plot")
318	        return
319	
320	    if n <= 6:
321	        nrows, ncols = 2, 3
322	    elif n <= 9:
323	        nrows, ncols = 3, 3
324	    else:
325	        nrows, ncols = 3, 4
326	
327	    fig, axes = plt.subplots(
328	        nrows, ncols,
329	        figsize=(5 * ncols, 4 * nrows),
330	        squeeze=False,
331	    )
332	
333	    for idx, (cond_key, cond_data) in enumerate(sorted(valid_conds.items())):
334	        row, col = divmod(idx, ncols)
335	        ax = axes[row][col]
336	
337	        keffs = np.array(cond_data["keffs"])
338	        eta_maxs = np.array(cond_data["eta_maxs"])
339	        panel_types = cond_data["panel_types"]
340	        r = cond_data["pearson_r"]
341	        verdict = cond_data["verdict"]
342	
343	        plotted_labels = set()
344	        for pt in ["all_local", "1api_2local", "2api_1local", "all_api"]:
345	            mask = [t == pt for t in panel_types]
346	            if not any(mask):
347	                continue
348	            k_sub = keffs[mask]
349	            e_sub = eta_maxs[mask]
350	            label = PANEL_LABELS[pt] if pt not in plotted_labels else None
351	            ax.scatter(
352	                k_sub, e_sub,
353	                c=PANEL_COLORS[pt],
354	                alpha=0.4, s=12, label=label,
355	                edgecolors="none",
356	            )
357	            plotted_labels.add(pt)
358	
359	        verdict_color = {
360	            "CONFOUND_SEVERE": "#e74c3c",
361	            "CONFOUND_MODERATE": "#e67e22",
362	            "CONFOUND_BROKEN": "#27ae60",
363	        }.get(verdict, "#333")
364	
365	        ax.set_title(
366	            f"{cond_key}\nr = {r:.3f}  [{verdict}]",
367	            fontsize=9,
368	            color=verdict_color,
369	        )
370	        ax.set_xlabel("K_eff", fontsize=8)
371	        ax.set_ylabel("η_max (individual ASR)", fontsize=8)
372	        ax.tick_params(labelsize=7)
373	
374	        if len(keffs) >= 3 and np.std(keffs) > 1e-10:
375	            z = np.polyfit(keffs, eta_maxs, 1)
376	            x_line = np.linspace(keffs.min(), keffs.max(), 50)
377	            ax.plot(x_line, np.polyval(z, x_line), "k--", alpha=0.3, linewidth=1)
378	
379	        if idx == 0:
380	            ax.legend(fontsize=6, loc="best", framealpha=0.7)
381	
382	    for idx in range(len(valid_conds), nrows * ncols):
383	        row, col = divmod(idx, ncols)
384	        axes[row][col].set_visible(False)
385	
386	    fig.suptitle(
387	        "K_eff vs η_max Confound Diagnosis (15 models, K=3 panels)",
388	        fontsize=12, y=1.02,
389	    )
390	    plt.tight_layout()
391	    plt.savefig(output_path, dpi=150, bbox_inches="tight")
392	    plt.close()
393	    logger.info(f"Scatter plot saved to {output_path}")
394	
395	
396	def main():
397	    logger.info("=== Plan 001: K_eff vs η_max Confound Diagnosis ===")
398	
399	    logger.info("Loading MI matrix...")
400	    mi_data = load_mi_matrix()
401	
402	    logger.info("Loading individual ASR data...")
403	    local_asr = load_local_individual_asr()
404	    api_asr = load_api_individual_asr()
405	    asr_data = merge_asr(local_asr, api_asr)
406	
407	    for ds in DATASETS:
408	        for attack in ATTACKS:
409	            models_with_asr = list(asr_data.get(ds, {}).get(attack, {}).keys())
410	            logger.info(f"  {ds}×{attack}: {len(models_with_asr)} models")
411	
412	    logger.info("\nRunning confound analysis...")
413	    conditions = run_confound_analysis(mi_data, asr_data)
414	
415	    scatter_path = PLAN001_DIR / "confound_scatter.png"
416	    plot_scatter_grid(conditions, scatter_path)
417	
418	    r_values = [
419	        v["pearson_r"] for v in conditions.values()
420	        if v.get("pearson_r") is not None
421	    ]
422	    if r_values:
423	        mean_r = float(np.mean(r_values))
424	        if mean_r < -0.7:
425	            overall = "CONFOUND_SEVERE"
426	        elif mean_r <= -0.5:
427	            overall = "CONFOUND_MODERATE"
428	        else:
429	            overall = "CONFOUND_BROKEN"
430	    else:
431	        mean_r = None
432	        overall = "INSUFFICIENT_DATA"
433	
434	    output_conditions = {}
435	    for k, v in conditions.items():
436	        output_conditions[k] = {
437	            "pearson_r": v.get("pearson_r"),
438	            "p_value": v.get("p_value"),
439	            "verdict": v.get("verdict"),
440	            "n_panels": v.get("n_panels"),
441	            "n_models_with_asr": v.get("n_models_with_asr"),
442	        }
443	
444	    output = {
445	        "conditions": output_conditions,
446	        "scatter_plots": str(scatter_path),
447	        "overall_verdict": overall,
448	        "mean_r": mean_r,
449	    }
450	
451	    output_path = PLAN001_DIR / "confound_diagnosis.json"
452	    with open(output_path, "w") as f:
453	        json.dump(output, f, indent=2, ensure_ascii=False)
454	    logger.info(f"\nDiagnosis saved to {output_path}")
455	
456	    print("\n" + "=" * 70)
457	    print("CONFOUND DIAGNOSIS SUMMARY")
458	    print("=" * 70)
459	    for cond_key, cond in sorted(output_conditions.items()):
460	        r = cond["pearson_r"]
461	        v = cond["verdict"]
462	        n = cond["n_panels"]
463	        r_str = f"{r:.3f}" if r is not None else "N/A"
464	        print(f"  {cond_key:40s}  r={r_str:>7s}  {v:20s}  ({n} panels)")
465	    print(f"\n  Overall: mean_r={mean_r:.3f if mean_r else 'N/A'}, verdict={overall}")
466	    print("=" * 70)
467	
468	
469	if __name__ == "__main__":
470	    main()
471	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "87a4eb29-8599-4d0d-82b4-01c79015e873",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_confound_diagnosis.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Plan 001: K_eff vs η_max confound diagnosis across all C(15,3) panels.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nfrom pathlib import Path\nfrom scipy import stats\n\nfrom src.utils import setup_logging\n\nlogger = setup_logging(\"plan001_confound\")\n\n# ── Model lists ──────────────────────────────────────────────────────\nLOCAL_MODELS = [\n    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",\n    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",\n]\nAPI_MODELS = [\n    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",\n    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",\n    \"gpt-4o-mini\", \"claude-3-haiku\",\n]\nALL_MODELS = LOCAL_MODELS + API_MODELS\nDATASETS = [\"mmlu\", \"arc_challenge\"]\nATTACKS = [\n    \"prompt_injection\", \"sycophancy\", \"score_manipulation\",\n    \"verbosity_bias\", \"position_bias\", \"authority_bias\",\n]\n\n# ── Paths ────────────────────────────────────────────────────────────\nRESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")\nPLAN001_DIR = RESULTS_DIR / \"plan001\"\nSCORES_DIR = PLAN001_DIR / \"individual_scores\"\nMI_MATRIX_PATH = PLAN001_DIR / \"mi_matrix\" / \"mi_matrix_15models.json\"\n\nSTEP2V3_CKPT = RESULTS_DIR / \"_step2v3_checkpoint.json\"\nTAXONOMY_CKPT = RESULTS_DIR / \"_taxonomy_checkpoint.json\"\n\n# Attack → checkpoint mapping for local models\nLOCAL_ATTACK_CKPT = {\n    \"prompt_injection\": STEP2V3_CKPT,\n    \"sycophancy\": STEP2V3_CKPT,\n    \"score_manipulation\": STEP2V3_CKPT,\n    \"verbosity_bias\": TAXONOMY_CKPT,\n    \"position_bias\": TAXONOMY_CKPT,\n    \"authority_bias\": TAXONOMY_CKPT,\n}\n\n\ndef _invert_winners(scores):\n    \"\"\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\"\"\"\n    swap = {\"A\": \"B\", \"B\": \"A\", \"tie\": \"tie\"}\n    return [{**s, \"winner\": swap.get(s.get(\"winner\", \"tie\"), \"tie\")} for s in scores]\n\n\ndef compute_asr_from_scores(clean_scores, attacked_scores, pairs):\n    \"\"\"Compute individual judge ASR: fraction of clean-correct flipped by attack.\"\"\"\n    n_flips = 0\n    n_total = 0\n    for clean, attacked, pair in zip(clean_scores, attacked_scores, pairs):\n        gt = pair.get(\"ground_truth_winner\")\n        cw = clean.get(\"winner\") if isinstance(clean, dict) else None\n        aw = attacked.get(\"winner\") if isinstance(attacked, dict) else None\n        if cw == gt:\n            n_total += 1\n            if aw != gt:\n                n_flips += 1\n    return n_flips / max(n_total, 1)\n\n\ndef load_local_individual_asr():\n    \"\"\"Load per-model ASR for local models from checkpoint files.\n\n    Returns: {dataset: {attack: {model_id: asr}}}\n    \"\"\"\n    asr_data = {}\n    ckpt_cache = {}\n\n    for attack in ATTACKS:\n        ckpt_path = LOCAL_ATTACK_CKPT[attack]\n        if str(ckpt_path) not in ckpt_cache:\n            if not ckpt_path.exists():\n                logger.warning(f\"Checkpoint not found: {ckpt_path}\")\n                continue\n            with open(ckpt_path) as f:\n                ckpt_cache[str(ckpt_path)] = json.load(f)\n        data = ckpt_cache[str(ckpt_path)]\n\n        for ds in DATASETS:\n            if ds not in asr_data:\n                asr_data[ds] = {}\n            if attack not in asr_data[ds]:\n                asr_data[ds][attack] = {}\n\n            clean_all = data.get(\"clean_scores\", {}).get(ds, {})\n            atk_all = data.get(\"attacked_scores\", {}).get(ds, {}).get(attack, {})\n            pairs = data.get(\"pairs\", {}).get(ds, [])\n\n            if not pairs:\n                logger.warning(f\"No pairs for {ds} in {ckpt_path.name}\")\n                continue\n\n            for model_id in LOCAL_MODELS:\n                if model_id not in clean_all or model_id not in atk_all:\n                    continue\n                atk_scores = atk_all[model_id]\n                if attack == \"position_bias\":\n                    atk_scores = _invert_winners(atk_scores)\n                asr = compute_asr_from_scores(\n                    clean_all[model_id], atk_scores, pairs\n                )\n                asr_data[ds][attack][model_id] = asr\n\n    return asr_data\n\n\ndef load_api_individual_asr():\n    \"\"\"Load per-model ASR for API models from individual score files.\n\n    Returns: {dataset: {attack: {model_id: asr}}}\n    \"\"\"\n    asr_data = {}\n    for model_id in API_MODELS:\n        for ds in DATASETS:\n            if ds not in asr_data:\n                asr_data[ds] = {}\n\n            clean_path = SCORES_DIR / f\"{model_id}__{ds}__clean.json\"\n            if not clean_path.exists():\n                continue\n            with open(clean_path) as f:\n                clean_data = json.load(f)\n            clean_scores = clean_data.get(\"scores\", [])\n\n            for attack in ATTACKS:\n                if attack not in asr_data[ds]:\n                    asr_data[ds][attack] = {}\n\n                atk_path = SCORES_DIR / f\"{model_id}__{ds}__{attack}.json\"\n                if not atk_path.exists():\n                    continue\n                with open(atk_path) as f:\n                    atk_data = json.load(f)\n\n                asr = atk_data.get(\"asr\")\n                if asr is not None:\n                    asr_data[ds][attack][model_id] = asr\n                else:\n                    logger.warning(\n                        f\"No ASR in {atk_path.name}, skipping\"\n                    )\n\n    return asr_data\n\n\ndef merge_asr(local_asr, api_asr):\n    \"\"\"Merge local and API ASR data.\"\"\"\n    merged = {}\n    for ds in DATASETS:\n        merged[ds] = {}\n        for attack in ATTACKS:\n            merged[ds][attack] = {}\n            for src in [local_asr, api_asr]:\n                if ds in src and attack in src[ds]:\n                    merged[ds][attack].update(src[ds][attack])\n    return merged\n\n\ndef load_mi_matrix():\n    \"\"\"Load MI matrix from Step 3 output.\"\"\"\n    if not MI_MATRIX_PATH.exists():\n        logger.error(f\"MI matrix not found: {MI_MATRIX_PATH}\")\n        sys.exit(1)\n    with open(MI_MATRIX_PATH) as f:\n        data = json.load(f)\n    return data\n\n\ndef mi_based_keff(mi_matrix_np, model_indices):\n    \"\"\"K_eff = (1/K) * sum_i [1 + sum_{j!=i} exp(-2 * MI_ij)]\"\"\"\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix_np[i_idx, j_idx])\n        keff += term\n    return keff / K\n\n\ndef classify_panel(model_ids):\n    \"\"\"Classify panel by composition for scatter plot coloring.\"\"\"\n    n_api = sum(1 for m in model_ids if m in API_MODELS)\n    if n_api == 3:\n        return \"all_api\"\n    elif n_api == 0:\n        return \"all_local\"\n    elif n_api == 2:\n        return \"2api_1local\"\n    else:\n        return \"1api_2local\"\n\n\nPANEL_COLORS = {\n    \"all_api\": \"#e74c3c\",\n    \"all_local\": \"#2ecc71\",\n    \"2api_1local\": \"#e67e22\",\n    \"1api_2local\": \"#3498db\",\n}\n\nPANEL_LABELS = {\n    \"all_api\": \"3 API\",\n    \"all_local\": \"3 Local\",\n    \"2api_1local\": \"2 API + 1 Local\",\n    \"1api_2local\": \"1 API + 2 Local\",\n}\n\n\ndef run_confound_analysis(mi_data, asr_data):\n    \"\"\"Run K_eff vs η_max analysis for all conditions.\"\"\"\n    models = mi_data[\"models\"]\n    model_to_idx = {m: i for i, m in enumerate(models)}\n    conditions = {}\n\n    for ds in DATASETS:\n        mi_mat = np.array(mi_data[\"mi_matrix\"][ds])\n\n        for attack in ATTACKS:\n            cond_key = f\"{ds}×{attack}\"\n            model_asrs = asr_data.get(ds, {}).get(attack, {})\n\n            if len(model_asrs) < 3:\n                logger.warning(\n                    f\"  {cond_key}: only {len(model_asrs)} models have ASR, \"\n                    f\"need ≥3 for panel construction. Skipping.\"\n                )\n                conditions[cond_key] = {\n                    \"pearson_r\": None,\n                    \"p_value\": None,\n                    \"verdict\": \"INSUFFICIENT_DATA\",\n                    \"n_panels\": 0,\n                    \"n_models_with_asr\": len(model_asrs),\n                }\n                continue\n\n            available_models = [\n                m for m in models if m in model_asrs\n            ]\n\n            keffs = []\n            eta_maxs = []\n            panel_types = []\n\n            for combo in itertools.combinations(available_models, 3):\n                indices = [model_to_idx[m] for m in combo]\n                keff = mi_based_keff(mi_mat, indices)\n                eta_max = max(model_asrs[m] for m in combo)\n\n                keffs.append(keff)\n                eta_maxs.append(eta_max)\n                panel_types.append(classify_panel(combo))\n\n            keffs = np.array(keffs)\n            eta_maxs = np.array(eta_maxs)\n\n            if len(keffs) < 3 or np.std(keffs) < 1e-10 or np.std(eta_maxs) < 1e-10:\n                r, p = 0.0, 1.0\n            else:\n                r, p = stats.pearsonr(keffs, eta_maxs)\n\n            if r < -0.7:\n                verdict = \"CONFOUND_SEVERE\"\n            elif r <= -0.5:\n                verdict = \"CONFOUND_MODERATE\"\n            else:\n                verdict = \"CONFOUND_BROKEN\"\n\n            conditions[cond_key] = {\n                \"pearson_r\": float(r),\n                \"p_value\": float(p),\n                \"verdict\": verdict,\n                \"n_panels\": len(keffs),\n                \"n_models_with_asr\": len(available_models),\n                \"keffs\": keffs.tolist(),\n                \"eta_maxs\": eta_maxs.tolist(),\n                \"panel_types\": panel_types,\n            }\n            logger.info(\n                f\"  {cond_key}: r={r:.3f}, p={p:.4f}, \"\n                f\"verdict={verdict}, n_panels={len(keffs)}\"\n            )\n\n    return conditions\n\n\ndef plot_scatter_grid(conditions, output_path):\n    \"\"\"Plot K_eff vs η_max scatter grid.\"\"\"\n    valid_conds = {\n        k: v for k, v in conditions.items()\n        if v.get(\"pearson_r\") is not None\n    }\n    n = len(valid_conds)\n    if n == 0:\n        logger.warning(\"No valid conditions to plot\")\n        return\n\n    if n <= 6:\n        nrows, ncols = 2, 3\n    elif n <= 9:\n        nrows, ncols = 3, 3\n    else:\n        nrows, ncols = 3, 4\n\n    fig, axes = plt.subplots(\n        nrows, ncols,\n        figsize=(5 * ncols, 4 * nrows),\n        squeeze=False,\n    )\n\n    for idx, (cond_key, cond_data) in enumerate(sorted(valid_conds.items())):\n        row, col = divmod(idx, ncols)\n        ax = axes[row][col]\n\n        keffs = np.array(cond_data[\"keffs\"])\n        eta_maxs = np.array(cond_data[\"eta_maxs\"])\n        panel_types = cond_data[\"panel_types\"]\n        r = cond_data[\"pearson_r\"]\n        verdict = cond_data[\"verdict\"]\n\n        plotted_labels = set()\n        for pt in [\"all_local\", \"1api_2local\", \"2api_1local\", \"all_api\"]:\n            mask = [t == pt for t in panel_types]\n            if not any(mask):\n                continue\n            k_sub = keffs[mask]\n            e_sub = eta_maxs[mask]\n            label = PANEL_LABELS[pt] if pt not in plotted_labels else None\n            ax.scatter(\n                k_sub, e_sub,\n                c=PANEL_COLORS[pt],\n                alpha=0.4, s=12, label=label,\n                edgecolors=\"none\",\n            )\n            plotted_labels.add(pt)\n\n        verdict_color = {\n            \"CONFOUND_SEVERE\": \"#e74c3c\",\n            \"CONFOUND_MODERATE\": \"#e67e22\",\n            \"CONFOUND_BROKEN\": \"#27ae60\",\n        }.get(verdict, \"#333\")\n\n        ax.set_title(\n            f\"{cond_key}\\nr = {r:.3f}  [{verdict}]\",\n            fontsize=9,\n            color=verdict_color,\n        )\n        ax.set_xlabel(\"K_eff\", fontsize=8)\n        ax.set_ylabel(\"η_max (individual ASR)\", fontsize=8)\n        ax.tick_params(labelsize=7)\n\n        if len(keffs) >= 3 and np.std(keffs) > 1e-10:\n            z = np.polyfit(keffs, eta_maxs, 1)\n            x_line = np.linspace(keffs.min(), keffs.max(), 50)\n            ax.plot(x_line, np.polyval(z, x_line), \"k--\", alpha=0.3, linewidth=1)\n\n        if idx == 0:\n            ax.legend(fontsize=6, loc=\"best\", framealpha=0.7)\n\n    for idx in range(len(valid_conds), nrows * ncols):\n        row, col = divmod(idx, ncols)\n        axes[row][col].set_visible(False)\n\n    fig.suptitle(\n        \"K_eff vs η_max Confound Diagnosis (15 models, K=3 panels)\",\n        fontsize=12, y=1.02,\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    logger.info(\"=== Plan 001: K_eff vs η_max Confound Diagnosis ===\")\n\n    logger.info(\"Loading MI matrix...\")\n    mi_data = load_mi_matrix()\n\n    logger.info(\"Loading individual ASR data...\")\n    local_asr = load_local_individual_asr()\n    api_asr = load_api_individual_asr()\n    asr_data = merge_asr(local_asr, api_asr)\n\n    for ds in DATASETS:\n        for attack in ATTACKS:\n            models_with_asr = list(asr_data.get(ds, {}).get(attack, {}).keys())\n            logger.info(f\"  {ds}×{attack}: {len(models_with_asr)} models\")\n\n    logger.info(\"\\nRunning confound analysis...\")\n    conditions = run_confound_analysis(mi_data, asr_data)\n\n    scatter_path = PLAN001_DIR / \"confound_scatter.png\"\n    plot_scatter_grid(conditions, scatter_path)\n\n    r_values = [\n        v[\"pearson_r\"] for v in conditions.values()\n        if v.get(\"pearson_r\") is not None\n    ]\n    if r_values:\n        mean_r = float(np.mean(r_values))\n        if mean_r < -0.7:\n            overall = \"CONFOUND_SEVERE\"\n        elif mean_r <= -0.5:\n            overall = \"CONFOUND_MODERATE\"\n        else:\n            overall = \"CONFOUND_BROKEN\"\n    else:\n        mean_r = None\n        overall = \"INSUFFICIENT_DATA\"\n\n    output_conditions = {}\n    for k, v in conditions.items():\n        output_conditions[k] = {\n            \"pearson_r\": v.get(\"pearson_r\"),\n            \"p_value\": v.get(\"p_value\"),\n            \"verdict\": v.get(\"verdict\"),\n            \"n_panels\": v.get(\"n_panels\"),\n            \"n_models_with_asr\": v.get(\"n_models_with_asr\"),\n        }\n\n    output = {\n        \"conditions\": output_conditions,\n        \"scatter_plots\": str(scatter_path),\n        \"overall_verdict\": overall,\n        \"mean_r\": mean_r,\n    }\n\n    output_path = PLAN001_DIR / \"confound_diagnosis.json\"\n    with open(output_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n    logger.info(f\"\\nDiagnosis saved to {output_path}\")\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"CONFOUND DIAGNOSIS SUMMARY\")\n    print(\"=\" * 70)\n    for cond_key, cond in sorted(output_conditions.items()):\n        r = cond[\"pearson_r\"]\n        v = cond[\"verdict\"]\n        n = cond[\"n_panels\"]\n        r_str = f\"{r:.3f}\" if r is not None else \"N/A\"\n        print(f\"  {cond_key:40s}  r={r_str:>7s}  {v:20s}  ({n} panels)\")\n    print(f\"\\n  Overall: mean_r={mean_r:.3f if mean_r else 'N/A'}, verdict={overall}\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 471,
      "startLine": 1,
      "totalLines": 471
    }
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-22T14:58:28.586Z_

<details><summary>↩ Tool result · `toolu_01JB8UCkvfx71SZorXKFQJKq`</summary>

```text
1	#!/usr/bin/env python3
2	"""Plan 001 Step 3: Compute 15-model pairwise MI matrix and K_eff for all C(15,3) panels."""
3	
4	import os
5	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
6	
7	import sys
8	sys.path.insert(0, "/root/cert_manip_resist_eval")
9	
10	import json
11	import itertools
12	import numpy as np
13	from pathlib import Path
14	from collections import Counter
15	from sklearn.metrics import mutual_info_score
16	
17	from src.utils import setup_logging
18	
19	logger = setup_logging("plan001_step3_mi")
20	
21	# ── Model lists ──────────────────────────────────────────────────────
22	LOCAL_MODELS = [
23	    "qwen2.5-72b", "llama3.1-70b", "mistral-large",
24	    "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b",
25	]
26	API_MODELS = [
27	    "claude-opus-4", "gpt-5.5", "gemini-2.5-pro", "gpt-4.1",
28	    "claude-sonnet-4", "gpt-4o", "gemini-2.5-flash",
29	    "gpt-4o-mini", "claude-3-haiku",
30	]
31	ALL_MODELS = LOCAL_MODELS + API_MODELS
32	DATASETS = ["mmlu", "arc_challenge"]
33	
34	# ── Paths ────────────────────────────────────────────────────────────
35	RESULTS_DIR = Path("/root/cert_manip_resist_eval/artifacts/results")
36	PLAN001_DIR = RESULTS_DIR / "plan001"
37	SCORES_DIR = PLAN001_DIR / "individual_scores"
38	MI_DIR = PLAN001_DIR / "mi_matrix"
39	
40	STEP2V3_CKPT = RESULTS_DIR / "_step2v3_checkpoint.json"
41	TAXONOMY_CKPT = RESULTS_DIR / "_taxonomy_checkpoint.json"
42	
43	
44	def load_local_clean_scores():
45	    """Load clean scores for 6 local models from checkpoint files."""
46	    scores = {}
47	    for ckpt_path in [STEP2V3_CKPT, TAXONOMY_CKPT]:
48	        if not ckpt_path.exists():
49	            logger.warning(f"Checkpoint not found: {ckpt_path}")
50	            continue
51	        with open(ckpt_path) as f:
52	            data = json.load(f)
53	        cs = data.get("clean_scores", {})
54	        for ds in DATASETS:
55	            if ds not in cs:
56	                continue
57	            if ds not in scores:
58	                scores[ds] = {}
59	            for model_id, model_scores in cs[ds].items():
60	                if model_id in LOCAL_MODELS and model_id not in scores[ds]:
61	                    scores[ds][model_id] = model_scores
62	    return scores
63	
64	
65	def load_api_clean_scores():
66	    """Load clean scores for 9 API models from individual score files."""
67	    scores = {}
68	    for model_id in API_MODELS:
69	        for ds in DATASETS:
70	            fname = f"{model_id}__{ds}__clean.json"
71	            fpath = SCORES_DIR / fname
72	            if not fpath.exists():
73	                logger.warning(f"API score file not found: {fpath}")
74	                continue
75	            with open(fpath) as f:
76	                data = json.load(f)
77	            if ds not in scores:
78	                scores[ds] = {}
79	            scores[ds][model_id] = data.get("scores", [])
80	    return scores
81	
82	
83	def merge_clean_scores(local_scores, api_scores):
84	    """Merge local and API clean scores into unified dict."""
85	    merged = {}
86	    for ds in DATASETS:
87	        merged[ds] = {}
88	        for src in [local_scores, api_scores]:
89	            if ds in src:
90	                merged[ds].update(src[ds])
91	    return merged
92	
93	
94	def extract_winner_vector(score_list):
95	    """Extract winner labels from score list, normalizing to A/B/C/tie."""
96	    winners = []
97	    for s in score_list:
98	        w = s.get("winner", "tie") if isinstance(s, dict) else "tie"
99	        winners.append(w)
100	    return winners
101	
102	
103	def compute_pairwise_mi(winners_i, winners_j):
104	    """Compute mutual information between two winner vectors."""
105	    n = min(len(winners_i), len(winners_j))
106	    if n == 0:
107	        return 0.0
108	    return mutual_info_score(winners_i[:n], winners_j[:n])
109	
110	
111	def build_mi_matrix(clean_scores, dataset):
112	    """Build 15x15 MI matrix for a dataset."""
113	    ds_scores = clean_scores.get(dataset, {})
114	    n_models = len(ALL_MODELS)
115	    mi_mat = np.zeros((n_models, n_models))
116	
117	    winner_vectors = {}
118	    for i, model_id in enumerate(ALL_MODELS):
119	        if model_id in ds_scores:
120	            winner_vectors[i] = extract_winner_vector(ds_scores[model_id])
121	        else:
122	            logger.warning(f"No clean scores for {model_id} on {dataset}")
123	
124	    for i in range(n_models):
125	        for j in range(i + 1, n_models):
126	            if i in winner_vectors and j in winner_vectors:
127	                mi = compute_pairwise_mi(winner_vectors[i], winner_vectors[j])
128	                mi_mat[i, j] = mi
129	                mi_mat[j, i] = mi
130	
131	    return mi_mat
132	
133	
134	def mi_based_keff(mi_matrix, model_indices):
135	    """K_eff = (1/K) * sum_i [1 + sum_{j!=i} exp(-2 * MI_ij)]"""
136	    K = len(model_indices)
137	    if K <= 1:
138	        return 1.0
139	    keff = 0.0
140	    for i_idx in model_indices:
141	        term = 1.0
142	        for j_idx in model_indices:
143	            if i_idx != j_idx:
144	                term += np.exp(-2 * mi_matrix[i_idx, j_idx])
145	        keff += term
146	    return keff / K
147	
148	
149	def compute_all_panel_keffs(mi_matrix, dataset):
150	    """Compute K_eff for all C(15,3)=455 panels."""
151	    n_models = len(ALL_MODELS)
152	    idx_to_model = {i: m for i, m in enumerate(ALL_MODELS)}
153	    panels = {}
154	
155	    for combo in itertools.combinations(range(n_models), 3):
156	        model_ids = [idx_to_model[i] for i in combo]
157	        panel_key = "|".join(model_ids)
158	        keff = mi_based_keff(mi_matrix, list(combo))
159	
160	        mi_pairs = {}
161	        for a, b in itertools.combinations(combo, 2):
162	            pair_key = f"{idx_to_model[a]}|{idx_to_model[b]}"
163	            mi_pairs[pair_key] = float(mi_matrix[a, b])
164	
165	        panels[panel_key] = {
166	            "models": model_ids,
167	            "keff": float(keff),
168	            "mi_pairs": mi_pairs,
169	        }
170	
171	    return panels
172	
173	
174	def main():
175	    logger.info("=== Plan 001 Step 3: MI Matrix Computation ===")
176	
177	    local_scores = load_local_clean_scores()
178	    api_scores = load_api_clean_scores()
179	    clean_scores = merge_clean_scores(local_scores, api_scores)
180	
181	    for ds in DATASETS:
182	        available = list(clean_scores.get(ds, {}).keys())
183	        missing = [m for m in ALL_MODELS if m not in available]
184	        logger.info(f"  {ds}: {len(available)}/{len(ALL_MODELS)} models available")
185	        if missing:
186	            logger.warning(f"  {ds}: missing models: {missing}")
187	
188	    available_count = sum(
189	        1 for ds in DATASETS
190	        for m in ALL_MODELS
191	        if m in clean_scores.get(ds, {})
192	    )
193	    total_needed = len(DATASETS) * len(ALL_MODELS)
194	    if available_count < total_needed:
195	        logger.warning(
196	            f"Only {available_count}/{total_needed} model×dataset combos available. "
197	            f"MI matrix will have zeros for missing pairs."
198	        )
199	
200	    mi_matrices = {}
201	    keff_per_panel = {}
202	
203	    for ds in DATASETS:
204	        logger.info(f"\n--- Computing MI matrix for {ds} ---")
205	        mi_mat = build_mi_matrix(clean_scores, ds)
206	        mi_matrices[ds] = mi_mat.tolist()
207	
208	        nonzero = np.count_nonzero(mi_mat)
209	        max_possible = len(ALL_MODELS) * (len(ALL_MODELS) - 1)
210	        logger.info(f"  MI matrix: {nonzero}/{max_possible} non-zero entries")
211	        if nonzero > 0:
212	            upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]
213	            upper_nz = upper[upper > 0]
214	            if len(upper_nz) > 0:
215	                logger.info(
216	                    f"  MI range: [{upper_nz.min():.4f}, {upper_nz.max():.4f}], "
217	                    f"mean={upper_nz.mean():.4f}"
218	                )
219	
220	        logger.info(f"  Computing K_eff for all C(15,3)=455 panels on {ds}...")
221	        panels = compute_all_panel_keffs(mi_mat, ds)
222	        keff_per_panel[ds] = panels
223	
224	        keff_values = [p["keff"] for p in panels.values()]
225	        logger.info(
226	            f"  K_eff range: [{min(keff_values):.3f}, {max(keff_values):.3f}], "
227	            f"mean={np.mean(keff_values):.3f}"
228	        )
229	
230	    MI_DIR.mkdir(parents=True, exist_ok=True)
231	    output = {
232	        "models": ALL_MODELS,
233	        "mi_matrix": mi_matrices,
234	        "keff_per_panel": keff_per_panel,
235	    }
236	    output_path = MI_DIR / "mi_matrix_15models.json"
237	    with open(output_path, "w") as f:
238	        json.dump(output, f, indent=2, ensure_ascii=False)
239	    logger.info(f"\nSaved MI matrix to {output_path}")
240	
241	    print("\n" + "=" * 70)
242	    print("MI MATRIX SUMMARY")
243	    print("=" * 70)
244	    for ds in DATASETS:
245	        mi_mat = np.array(mi_matrices[ds])
246	        upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]
247	        n_computed = np.count_nonzero(upper)
248	        print(f"\n{ds}:")
249	        print(f"  Pairwise MI computed: {n_computed}/105")
250	        if n_computed > 0:
251	            nz = upper[upper > 0]
252	            print(f"  MI range: [{nz.min():.4f}, {nz.max():.4f}]")
253	            print(f"  MI mean:  {nz.mean():.4f}")
254	        keffs = [p["keff"] for p in keff_per_panel[ds].values()]
255	        print(f"  K_eff (455 panels): [{min(keffs):.3f}, {max(keffs):.3f}], mean={np.mean(keffs):.3f}")
256	    print("=" * 70)
257	
258	
259	if __name__ == "__main__":
260	    main()
261	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "56752590-e7ad-4c55-9760-ecfa69fbfbb2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 3: Compute 15-model pairwise MI matrix and K_eff for all C(15,3) panels.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\nfrom collections import Counter\nfrom sklearn.metrics import mutual_info_score\n\nfrom src.utils import setup_logging\n\nlogger = setup_logging(\"plan001_step3_mi\")\n\n# ── Model lists ──────────────────────────────────────────────────────\nLOCAL_MODELS = [\n    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",\n    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",\n]\nAPI_MODELS = [\n    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",\n    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",\n    \"gpt-4o-mini\", \"claude-3-haiku\",\n]\nALL_MODELS = LOCAL_MODELS + API_MODELS\nDATASETS = [\"mmlu\", \"arc_challenge\"]\n\n# ── Paths ────────────────────────────────────────────────────────────\nRESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")\nPLAN001_DIR = RESULTS_DIR / \"plan001\"\nSCORES_DIR = PLAN001_DIR / \"individual_scores\"\nMI_DIR = PLAN001_DIR / \"mi_matrix\"\n\nSTEP2V3_CKPT = RESULTS_DIR / \"_step2v3_checkpoint.json\"\nTAXONOMY_CKPT = RESULTS_DIR / \"_taxonomy_checkpoint.json\"\n\n\ndef load_local_clean_scores():\n    \"\"\"Load clean scores for 6 local models from checkpoint files.\"\"\"\n    scores = {}\n    for ckpt_path in [STEP2V3_CKPT, TAXONOMY_CKPT]:\n        if not ckpt_path.exists():\n            logger.warning(f\"Checkpoint not found: {ckpt_path}\")\n            continue\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        cs = data.get(\"clean_scores\", {})\n        for ds in DATASETS:\n            if ds not in cs:\n                continue\n            if ds not in scores:\n                scores[ds] = {}\n            for model_id, model_scores in cs[ds].items():\n                if model_id in LOCAL_MODELS and model_id not in scores[ds]:\n                    scores[ds][model_id] = model_scores\n    return scores\n\n\ndef load_api_clean_scores():\n    \"\"\"Load clean scores for 9 API models from individual score files.\"\"\"\n    scores = {}\n    for model_id in API_MODELS:\n        for ds in DATASETS:\n            fname = f\"{model_id}__{ds}__clean.json\"\n            fpath = SCORES_DIR / fname\n            if not fpath.exists():\n                logger.warning(f\"API score file not found: {fpath}\")\n                continue\n            with open(fpath) as f:\n                data = json.load(f)\n            if ds not in scores:\n                scores[ds] = {}\n            scores[ds][model_id] = data.get(\"scores\", [])\n    return scores\n\n\ndef merge_clean_scores(local_scores, api_scores):\n    \"\"\"Merge local and API clean scores into unified dict.\"\"\"\n    merged = {}\n    for ds in DATASETS:\n        merged[ds] = {}\n        for src in [local_scores, api_scores]:\n            if ds in src:\n                merged[ds].update(src[ds])\n    return merged\n\n\ndef extract_winner_vector(score_list):\n    \"\"\"Extract winner labels from score list, normalizing to A/B/C/tie.\"\"\"\n    winners = []\n    for s in score_list:\n        w = s.get(\"winner\", \"tie\") if isinstance(s, dict) else \"tie\"\n        winners.append(w)\n    return winners\n\n\ndef compute_pairwise_mi(winners_i, winners_j):\n    \"\"\"Compute mutual information between two winner vectors.\"\"\"\n    n = min(len(winners_i), len(winners_j))\n    if n == 0:\n        return 0.0\n    return mutual_info_score(winners_i[:n], winners_j[:n])\n\n\ndef build_mi_matrix(clean_scores, dataset):\n    \"\"\"Build 15x15 MI matrix for a dataset.\"\"\"\n    ds_scores = clean_scores.get(dataset, {})\n    n_models = len(ALL_MODELS)\n    mi_mat = np.zeros((n_models, n_models))\n\n    winner_vectors = {}\n    for i, model_id in enumerate(ALL_MODELS):\n        if model_id in ds_scores:\n            winner_vectors[i] = extract_winner_vector(ds_scores[model_id])\n        else:\n            logger.warning(f\"No clean scores for {model_id} on {dataset}\")\n\n    for i in range(n_models):\n        for j in range(i + 1, n_models):\n            if i in winner_vectors and j in winner_vectors:\n                mi = compute_pairwise_mi(winner_vectors[i], winner_vectors[j])\n                mi_mat[i, j] = mi\n                mi_mat[j, i] = mi\n\n    return mi_mat\n\n\ndef mi_based_keff(mi_matrix, model_indices):\n    \"\"\"K_eff = (1/K) * sum_i [1 + sum_{j!=i} exp(-2 * MI_ij)]\"\"\"\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx, j_idx])\n        keff += term\n    return keff / K\n\n\ndef compute_all_panel_keffs(mi_matrix, dataset):\n    \"\"\"Compute K_eff for all C(15,3)=455 panels.\"\"\"\n    n_models = len(ALL_MODELS)\n    idx_to_model = {i: m for i, m in enumerate(ALL_MODELS)}\n    panels = {}\n\n    for combo in itertools.combinations(range(n_models), 3):\n        model_ids = [idx_to_model[i] for i in combo]\n        panel_key = \"|\".join(model_ids)\n        keff = mi_based_keff(mi_matrix, list(combo))\n\n        mi_pairs = {}\n        for a, b in itertools.combinations(combo, 2):\n            pair_key = f\"{idx_to_model[a]}|{idx_to_model[b]}\"\n            mi_pairs[pair_key] = float(mi_matrix[a, b])\n\n        panels[panel_key] = {\n            \"models\": model_ids,\n            \"keff\": float(keff),\n            \"mi_pairs\": mi_pairs,\n        }\n\n    return panels\n\n\ndef main():\n    logger.info(\"=== Plan 001 Step 3: MI Matrix Computation ===\")\n\n    local_scores = load_local_clean_scores()\n    api_scores = load_api_clean_scores()\n    clean_scores = merge_clean_scores(local_scores, api_scores)\n\n    for ds in DATASETS:\n        available = list(clean_scores.get(ds, {}).keys())\n        missing = [m for m in ALL_MODELS if m not in available]\n        logger.info(f\"  {ds}: {len(available)}/{len(ALL_MODELS)} models available\")\n        if missing:\n            logger.warning(f\"  {ds}: missing models: {missing}\")\n\n    available_count = sum(\n        1 for ds in DATASETS\n        for m in ALL_MODELS\n        if m in clean_scores.get(ds, {})\n    )\n    total_needed = len(DATASETS) * len(ALL_MODELS)\n    if available_count < total_needed:\n        logger.warning(\n            f\"Only {available_count}/{total_needed} model×dataset combos available. \"\n            f\"MI matrix will have zeros for missing pairs.\"\n        )\n\n    mi_matrices = {}\n    keff_per_panel = {}\n\n    for ds in DATASETS:\n        logger.info(f\"\\n--- Computing MI matrix for {ds} ---\")\n        mi_mat = build_mi_matrix(clean_scores, ds)\n        mi_matrices[ds] = mi_mat.tolist()\n\n        nonzero = np.count_nonzero(mi_mat)\n        max_possible = len(ALL_MODELS) * (len(ALL_MODELS) - 1)\n        logger.info(f\"  MI matrix: {nonzero}/{max_possible} non-zero entries\")\n        if nonzero > 0:\n            upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\n            upper_nz = upper[upper > 0]\n            if len(upper_nz) > 0:\n                logger.info(\n                    f\"  MI range: [{upper_nz.min():.4f}, {upper_nz.max():.4f}], \"\n                    f\"mean={upper_nz.mean():.4f}\"\n                )\n\n        logger.info(f\"  Computing K_eff for all C(15,3)=455 panels on {ds}...\")\n        panels = compute_all_panel_keffs(mi_mat, ds)\n        keff_per_panel[ds] = panels\n\n        keff_values = [p[\"keff\"] for p in panels.values()]\n        logger.info(\n            f\"  K_eff range: [{min(keff_values):.3f}, {max(keff_values):.3f}], \"\n            f\"mean={np.mean(keff_values):.3f}\"\n        )\n\n    MI_DIR.mkdir(parents=True, exist_ok=True)\n    output = {\n        \"models\": ALL_MODELS,\n        \"mi_matrix\": mi_matrices,\n        \"keff_per_panel\": keff_per_panel,\n    }\n    output_path = MI_DIR / \"mi_matrix_15models.json\"\n    with open(output_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n    logger.info(f\"\\nSaved MI matrix to {output_path}\")\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"MI MATRIX SUMMARY\")\n    print(\"=\" * 70)\n    for ds in DATASETS:\n        mi_mat = np.array(mi_matrices[ds])\n        upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\n        n_computed = np.count_nonzero(upper)\n        print(f\"\\n{ds}:\")\n        print(f\"  Pairwise MI computed: {n_computed}/105\")\n        if n_computed > 0:\n            nz = upper[upper > 0]\n            print(f\"  MI range: [{nz.min():.4f}, {nz.max():.4f}]\")\n            print(f\"  MI mean:  {nz.mean():.4f}\")\n        keffs = [p[\"keff\"] for p in keff_per_panel[ds].values()]\n        print(f\"  K_eff (455 panels): [{min(keffs):.3f}, {max(keffs):.3f}], mean={np.mean(keffs):.3f}\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 261,
      "startLine": 1,
      "totalLines": 261
    }
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01RYu3nrchL4c45AiEGeyp2G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "571f3013-5ded-4d41-a938-847cd61bae95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgSLYGx6LvgdkELMs8G7Lu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6156,
      "cache_creation_input_tokens": 4123,
      "cache_read_input_tokens": 52808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4123
      },
      "output_tokens": 38,
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

_source line 47 · 2026-05-22T14:58:34.482Z_

<details><summary>↩ Tool result · `toolu_01RYu3nrchL4c45AiEGeyp2G`</summary>

```text
1	#!/usr/bin/env python3
2	"""Plan 001 Step 4: Panel regression — 455 panels × 12 conditions.
3	
4	Input:
5	  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json
6	  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/
7	  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json
8	
9	Output:
10	  - artifacts/results/plan001/panel_regression/step4_regression_results.json
11	
12	Dependencies: numpy, scipy, statsmodels
13	Optional: pingouin (for partial_corr; manual fallback included)
14	"""
15	
16	import os
17	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
18	
19	import sys
20	sys.path.insert(0, "/root/cert_manip_resist_eval")
21	
22	import json
23	import warnings
24	import itertools
25	import numpy as np
26	import statsmodels.api as sm
27	from pathlib import Path
28	from scipy import optimize, stats, special
29	from statsmodels.stats.outliers_influence import variance_inflation_factor
30	from statsmodels.stats.multitest import multipletests
31	
32	from src.utils import setup_logging
33	
34	logger = setup_logging("plan001_step4")
35	
36	# ── Constants ────────────────────────────────────────────────────────
37	LOCAL_MODELS = [
38	    "qwen2.5-72b", "llama3.1-70b", "mistral-large",
39	    "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b",
40	]
41	API_MODELS = [
42	    "claude-opus-4", "gpt-5.5", "gemini-2.5-pro", "gpt-4.1",
43	    "claude-sonnet-4", "gpt-4o", "gemini-2.5-flash",
44	    "gpt-4o-mini", "claude-3-haiku",
45	]
46	ALL_MODELS = LOCAL_MODELS + API_MODELS
47	DATASETS = ["mmlu", "arc_challenge"]
48	ATTACKS = [
49	    "prompt_injection", "sycophancy", "score_manipulation",
50	    "verbosity_bias", "position_bias", "authority_bias",
51	]
52	EPS = 0.001
53	
54	RESULTS_DIR = Path("/root/cert_manip_resist_eval/artifacts/results")
55	PLAN001_DIR = RESULTS_DIR / "plan001"
56	SCORES_DIR = PLAN001_DIR / "individual_scores"
57	MI_PATH = PLAN001_DIR / "mi_matrix" / "mi_matrix_15models.json"
58	CKPT_FILES = [
59	    RESULTS_DIR / "_taxonomy_checkpoint.json",
60	    RESULTS_DIR / "_step2v3_checkpoint.json",
61	]
62	OUTPUT_DIR = PLAN001_DIR / "panel_regression"
63	
64	
65	# ── JSON Helper ──────────────────────────────────────────────────────
66	
67	def _json_default(obj):
68	    if isinstance(obj, np.floating):
69	        v = float(obj)
70	        return None if (np.isnan(v) or np.isinf(v)) else v
71	    if isinstance(obj, np.integer):
72	        return int(obj)
73	    if isinstance(obj, np.ndarray):
74	        return obj.tolist()
75	    if isinstance(obj, np.bool_):
76	        return bool(obj)
77	    raise TypeError(f"Not JSON serializable: {type(obj)}")
78	
79	
80	# ── Data Loading ─────────────────────────────────────────────────────
81	
82	def load_mi_data():
83	    if not MI_PATH.exists():
84	        logger.error(f"MI matrix not found: {MI_PATH}")
85	        logger.error("Run Step 3 first: scripts/run_plan001_step3_mi_matrix.py")
86	        sys.exit(1)
87	    with open(MI_PATH) as f:
88	        data = json.load(f)
89	    logger.info(f"Loaded MI matrix: {len(data['models'])} models")
90	    return data
91	
92	
93	def load_pairs():
94	    for ckpt_path in CKPT_FILES:
95	        if not ckpt_path.exists():
96	            continue
97	        with open(ckpt_path) as f:
98	            data = json.load(f)
99	        if "pairs" not in data:
100	            continue
101	        pairs = {}
102	        for ds in DATASETS:
103	            if ds in data["pairs"]:
104	                pairs[ds] = data["pairs"][ds][:300]
105	                logger.info(f"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}")
106	        if pairs:
107	            return pairs
108	    logger.error("No pairs found in any checkpoint file")
109	    sys.exit(1)
110	
111	
112	def _invert_winners(scores):
113	    """Invert A<->B winner labels for position bias scores (swapped pair orientation)."""
114	    swap = {"A": "B", "B": "A", "tie": "tie"}
115	    return [{**s, "winner": swap.get(s.get("winner", "tie"), "tie")} for s in scores]
116	
117	
118	def load_all_scores():
119	    """Load sample-level clean + attacked scores for all 15 models.
120	
121	    Returns:
122	        clean[ds][model_id] = [{"winner": ..., ...}, ...]
123	        attacked[ds][atk][model_id] = [{"winner": ..., ...}, ...]
124	    """
125	    clean = {ds: {} for ds in DATASETS}
126	    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}
127	
128	    for ckpt_path in CKPT_FILES:
129	        if not ckpt_path.exists():
130	            continue
131	        logger.info(f"Loading checkpoint: {ckpt_path.name}")
132	        with open(ckpt_path) as f:
133	            data = json.load(f)
134	        for ds in DATASETS:
135	            for mid, scores in data.get("clean_scores", {}).get(ds, {}).items():
136	                if mid not in clean[ds]:
137	                    clean[ds][mid] = scores
138	            for atk in ATTACKS:
139	                for mid, scores in data.get("attacked_scores", {}).get(ds, {}).get(atk, {}).items():
140	                    if mid not in attacked[ds][atk]:
141	                        if atk == "position_bias":
142	                            scores = _invert_winners(scores)
143	                        attacked[ds][atk][mid] = scores
144	
145	    if SCORES_DIR.exists():
146	        logger.info(f"Loading individual scores from {SCORES_DIR}")
147	        for mid in ALL_MODELS:
148	            for ds in DATASETS:
149	                fp = SCORES_DIR / f"{mid}__{ds}__clean.json"
150	                if fp.exists() and mid not in clean[ds]:
151	                    with open(fp) as f:
152	                        clean[ds][mid] = json.load(f).get("scores", [])
153	                for atk in ATTACKS:
154	                    fp = SCORES_DIR / f"{mid}__{ds}__{atk}.json"
155	                    if fp.exists() and mid not in attacked[ds][atk]:
156	                        with open(fp) as f:
157	                            scores = json.load(f).get("scores", [])
158	                        if atk == "position_bias":
159	                            scores = _invert_winners(scores)
160	                        attacked[ds][atk][mid] = scores
161	
162	    for ds in DATASETS:
163	        nc = len(clean[ds])
164	        logger.info(f"  {ds} clean: {nc}/{len(ALL_MODELS)}")
165	        for atk in ATTACKS:
166	            na = len(attacked[ds][atk])
167	            if na > 0:
168	                logger.info(f"  {ds} {atk}: {na}/{len(ALL_MODELS)}")
169	
170	    return clean, attacked
171	
172	
173	# ── ASR Computation ──────────────────────────────────────────────────
174	
175	def majority_vote(votes):
176	    counts = {"A": 0, "B": 0, "tie": 0}
177	    for v in votes:
178	        counts[v] = counts.get(v, 0) + 1
179	    mc = max(counts.values())
180	    winners = [k for k, c in counts.items() if c == mc]
181	    if len(winners) == 1:
182	        return winners[0]
183	    for w in winners:
184	        if w != "tie":
185	            return w
186	    return "tie"
187	
188	
189	def compute_individual_asr(clean_list, attacked_list, pairs):
190	    n = min(len(clean_list), len(attacked_list), len(pairs))
191	    n_flips = n_correct = 0
192	    for i in range(n):
193	        gt = pairs[i]["ground_truth_winner"]
194	        if clean_list[i].get("winner", "tie") == gt:
195	            n_correct += 1
196	            if attacked_list[i].get("winner", "tie") != gt:
197	                n_flips += 1
198	    return n_flips / max(n_correct, 1)
199	
200	
201	def compute_panel_asr(jids, clean, attacked, pairs):
202	    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))
203	    n_flips = n_correct = 0
204	    for i in range(n):
205	        gt = pairs[i]["ground_truth_winner"]
206	        cv = majority_vote([clean[j][i].get("winner", "tie") for j in jids])
207	        if cv != gt:
208	            continue
209	        n_correct += 1
210	        av = majority_vote([attacked[j][i].get("winner", "tie") for j in jids])
211	        if av != gt:
212	            n_flips += 1
213	    return n_flips / max(n_correct, 1)
214	
215	
216	# ── Regression Helpers ───────────────────────────────────────────────
217	
218	def partial_corr_manual(x, y, covar):
219	    """Partial correlation of x and y, controlling for covar."""
220	    Xc = sm.add_constant(covar)
221	    rx = sm.OLS(x, Xc).fit().resid
222	    ry = sm.OLS(y, Xc).fit().resid
223	    r, p = stats.pearsonr(rx, ry)
224	    return float(r), float(p)
225	
226	
227	try:
228	    import pingouin as pg
229	    import pandas as pd
230	
231	    def partial_corr_fn(x, y, covar):
232	        df = pd.DataFrame({"x": x, "y": y, "z": covar})
233	        res = pg.partial_corr(data=df, x="x", y="y", covar="z")
234	        return float(res["r"].values[0]), float(res["p-val"].values[0])
235	    logger.info("Using pingouin for partial correlation")
236	except ImportError:
237	    partial_corr_fn = partial_corr_manual
238	    logger.info("pingouin not available, using manual partial correlation")
239	
240	
241	def beta_regression_mle(y_raw, X):
242	    """Beta regression via MLE. y in (0,1), logit link.
243	    X should include constant column.
244	    Returns dict with coefficients/p-values or None on failure."""
245	    y = np.clip(y_raw, 1e-6, 1 - 1e-6)
246	    n, k = X.shape
247	
248	    def neg_ll(params):
249	        beta = params[:k]
250	        phi = np.exp(params[k])
251	        mu = 1.0 / (1.0 + np.exp(-(X @ beta)))
252	        a = mu * phi
253	        b = (1.0 - mu) * phi
254	        return -np.sum(
255	            special.gammaln(phi) - special.gammaln(a) - special.gammaln(b)
256	            + (a - 1.0) * np.log(y) + (b - 1.0) * np.log(1.0 - y)
257	        )
258	
259	    # Initial values from OLS on logit(y)
260	    y_logit = np.log(y / (1.0 - y))
261	    x0 = np.zeros(k + 1)
262	    try:
263	        init_fit = sm.OLS(y_logit, X).fit()
264	        x0[:k] = init_fit.params
265	    except Exception:
266	        pass
267	    x0[k] = np.log(10.0)
268	
269	    with warnings.catch_warnings():
270	        warnings.simplefilter("ignore")
271	        res = optimize.minimize(neg_ll, x0, method="L-BFGS-B",
272	                                options={"maxiter": 5000, "ftol": 1e-12})
273	    if not res.success:
274	        return None
275	
276	    # Numerical Hessian for standard errors
277	    n_p = len(res.x)
278	    H = np.zeros((n_p, n_p))
279	    eps_h = 1e-5
280	    for i in range(n_p):
281	        for j in range(i, n_p):
282	            ei = np.zeros(n_p)
283	            ej = np.zeros(n_p)
284	            ei[i] = eps_h
285	            ej[j] = eps_h
286	            fpp = neg_ll(res.x + ei + ej)
287	            fpm = neg_ll(res.x + ei - ej)
288	            fmp = neg_ll(res.x - ei + ej)
289	            fmm = neg_ll(res.x - ei - ej)
290	            H[i, j] = H[j, i] = (fpp - fpm - fmp + fmm) / (4.0 * eps_h * eps_h)
291	
292	    try:
293	        cov = np.linalg.inv(H)
294	        se = np.sqrt(np.maximum(np.diag(cov), 0.0))
295	    except np.linalg.LinAlgError:
296	        return None
297	
298	    beta = res.x[:k]
299	    se_b = se[:k]
300	    z = beta / np.maximum(se_b, 1e-12)
301	    pvals = 2.0 * (1.0 - stats.norm.cdf(np.abs(z)))
302	    return {"beta": beta, "se": se_b, "z": z, "p": pvals}
303	
304	
305	def run_condition_analysis(panel_asrs, keffs, eta_maxs):
306	    """Full regression suite for one condition. All arrays shape (n,)."""
307	    n = len(panel_asrs)
308	    y = np.log(panel_asrs + EPS)
309	    x1 = np.log(keffs)
310	    x2 = np.log(eta_maxs + EPS)
311	    X = np.column_stack([x1, x2])
312	    Xc = sm.add_constant(X)
313	    results = {}
314	
315	    # ── OLS ──
316	    fit = sm.OLS(y, Xc).fit()
317	    results["ols"] = {
318	        "keff_beta": float(fit.params[1]),
319	        "keff_t": float(fit.tvalues[1]),
320	        "keff_p": float(fit.pvalues[1]),
321	        "eta_max_beta": float(fit.params[2]),
322	        "eta_max_t": float(fit.tvalues[2]),
323	        "eta_max_p": float(fit.pvalues[2]),
324	        "R2": float(fit.rsquared),
325	        "adj_R2": float(fit.rsquared_adj),
326	        "f_stat": float(fit.fvalue) if np.isfinite(fit.fvalue) else None,
327	        "f_pvalue": float(fit.f_pvalue) if np.isfinite(fit.f_pvalue) else None,
328	    }
329	
330	    # ── VIF ──
331	    results["vif_keff"] = float(variance_inflation_factor(Xc, 1))
332	    results["vif_eta_max"] = float(variance_inflation_factor(Xc, 2))
333	
334	    # ── Partial correlation (K_eff | η_max) ──
335	    pr, pp = partial_corr_fn(x1, y, x2)
336	    results["partial_r_keff"] = pr
337	    results["partial_r_keff_p"] = pp
338	
339	    # ── Residualized K_eff ──
340	    Xz = sm.add_constant(x2)
341	    resid_keff = sm.OLS(x1, Xz).fit().resid
342	    Xr = sm.add_constant(resid_keff)
343	    fit_r = sm.OLS(y, Xr).fit()
344	    results["residualized_keff_beta"] = float(fit_r.params[1])
345	    results["residualized_keff_t"] = float(fit_r.tvalues[1])
346	    results["residualized_keff_p"] = float(fit_r.pvalues[1])
347	
348	    # ── Beta regression ──
349	    y_raw = np.clip(panel_asrs, 0.0, 1.0)
350	    br = beta_regression_mle(y_raw, Xc)
351	    if br is not None:
352	        results["beta_reg_keff_beta"] = float(br["beta"][1])
353	        results["beta_reg_keff_p"] = float(br["p"][1])
354	        results["beta_reg_eta_max_beta"] = float(br["beta"][2])
355	        results["beta_reg_eta_max_p"] = float(br["p"][2])
356	    else:
357	        results["beta_reg_keff_p"] = None
358	        results["beta_reg_eta_max_p"] = None
359	
360	    return results
361	
362	
363	# ── Main ─────────────────────────────────────────────────────────────
364	
365	def main():
366	    logger.info("=" * 60)
367	    logger.info("Plan 001 Step 4: Panel Regression (455 panels × 12 conditions)")
368	    logger.info("=" * 60)
369	
370	    mi_data = load_mi_data()
371	    pairs = load_pairs()
372	    clean, attacked = load_all_scores()
373	
374	    # Precompute individual ASR for all model × condition
375	    logger.info("\nPrecomputing individual ASR...")
376	    ind_asr = {}
377	    for ds in DATASETS:
378	        for atk in ATTACKS:
379	            for mid in ALL_MODELS:
380	                if mid in clean[ds] and mid in attacked[ds][atk]:
381	                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
382	                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]
383	                    )
384	    logger.info(f"  Computed {len(ind_asr)} individual ASR values")
385	
386	    # Enumerate all C(15,3)=455 panels
387	    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))
388	    logger.info(f"  Total panels: {len(all_combos)}")
389	
390	    condition_results = {}
391	    raw_eta_ps = []
392	    raw_keff_ps = []
393	    valid_cond_keys = []
394	
395	    for ds in DATASETS:
396	        keff_data = mi_data["keff_per_panel"].get(ds, {})
397	        for atk in ATTACKS:
398	            cond = f"{ds}×{atk}"
399	            logger.info(f"\n--- {cond} ---")
400	
401	            p_asrs, p_keffs, p_etas = [], [], []
402	            skipped = 0
403	
404	            for combo in all_combos:
405	                jids = [ALL_MODELS[i] for i in combo]
406	
407	                if not all((ds, atk, j) in ind_asr for j in jids):
408	                    skipped += 1
409	                    continue
410	                pk = "|".join(jids)
411	                if pk not in keff_data:
412	                    skipped += 1
413	                    continue
414	
415	                keff = keff_data[pk]["keff"]
416	                etas = [ind_asr[(ds, atk, j)] for j in jids]
417	                eta_max = max(etas)
418	
419	                cs = {j: clean[ds][j] for j in jids}
420	                ats = {j: attacked[ds][atk][j] for j in jids}
421	                p_asr = compute_panel_asr(jids, cs, ats, pairs[ds])
422	
423	                p_asrs.append(p_asr)
424	                p_keffs.append(keff)
425	                p_etas.append(eta_max)
426	
427	            n_panels = len(p_asrs)
428	            logger.info(f"  {n_panels} panels with data, {skipped} skipped")
429	
430	            if n_panels < 10:
431	                logger.warning(f"  Too few panels ({n_panels}), skipping")
432	                condition_results[cond] = {"n_panels": n_panels, "skipped": True}
433	                continue
434	
435	            p_asrs = np.array(p_asrs)
436	            p_keffs = np.array(p_keffs)
437	            p_etas = np.array(p_etas)
438	
439	            if np.std(p_asrs) < 1e-10:
440	                logger.warning(f"  Constant ASR ({p_asrs[0]:.4f}), skipping regression")
441	                condition_results[cond] = {
442	                    "n_panels": n_panels, "skipped": True,
443	                    "reason": "constant_asr", "asr_value": float(p_asrs[0]),
444	                }
445	                continue
446	
447	            cond_res = run_condition_analysis(p_asrs, p_keffs, p_etas)
448	            cond_res["n_panels"] = n_panels
449	            cond_res["skipped"] = False
450	            cond_res["asr_stats"] = {
451	                "mean": float(np.mean(p_asrs)),
452	                "std": float(np.std(p_asrs)),
453	                "min": float(np.min(p_asrs)),
454	                "max": float(np.max(p_asrs)),
455	                "pct_zero": float(np.mean(p_asrs == 0)),
456	            }
457	            condition_results[cond] = cond_res
458	
459	            raw_eta_ps.append(cond_res["ols"]["eta_max_p"])
460	            raw_keff_ps.append(cond_res["ols"]["keff_p"])
461	            valid_cond_keys.append(cond)
462	
463	            ols = cond_res["ols"]
464	            sig_k = "***" if ols["keff_p"] < 0.001 else "**" if ols["keff_p"] < 0.01 else "*" if ols["keff_p"] < 0.05 else "ns"
465	            sig_e = "***" if ols["eta_max_p"] < 0.001 else "**" if ols["eta_max_p"] < 0.01 else "*" if ols["eta_max_p"] < 0.05 else "ns"
466	            logger.info(
467	                f"  OLS R²={ols['R2']:.4f}  "
468	                f"K_eff: β={ols['keff_beta']:+.4f} p={ols['keff_p']:.4f} {sig_k}  "
469	                f"η_max: β={ols['eta_max_beta']:+.4f} p={ols['eta_max_p']:.4f} {sig_e}"
470	            )
471	            logger.info(
472	                f"  VIF: K_eff={cond_res['vif_keff']:.2f}, η_max={cond_res['vif_eta_max']:.2f}"
473	            )
474	            logger.info(
475	                f"  Partial r(K_eff|η_max)={cond_res['partial_r_keff']:.4f} "
476	                f"p={cond_res['partial_r_keff_p']:.4f}"
477	            )
478	            logger.info(
479	                f"  Residualized K_eff: β={cond_res['residualized_keff_beta']:+.4f} "
480	                f"p={cond_res['residualized_keff_p']:.4f}"
481	            )
482	
483	    # ── Multiple testing corrections ──
484	    if raw_eta_ps:
485	        _, bonf_eta, _, _ = multipletests(raw_eta_ps, method="bonferroni")
486	        _, fdr_eta, _, _ = multipletests(raw_eta_ps, method="fdr_bh")
487	        _, bonf_keff, _, _ = multipletests(raw_keff_ps, method="bonferroni")
488	        _, fdr_keff, _, _ = multipletests(raw_keff_ps, method="fdr_bh")
489	
490	        for i, ck in enumerate(valid_cond_keys):
491	            condition_results[ck]["eta_max_bonferroni_p"] = float(bonf_eta[i])
492	            condition_results[ck]["eta_max_fdr_p"] = float(fdr_eta[i])
493	            condition_results[ck]["keff_bonferroni_p"] = float(bonf_keff[i])
494	            condition_results[ck]["keff_fdr_p"] = float(fdr_keff[i])
495	
496	    # ── Summary ──
497	    valid = [condition_results[k] for k in valid_cond_keys]
498	    nv = len(valid)
499	    summary = {}
500	    if nv > 0:
501	        summary = {
502	            "keff_sig_negative_count": (
503	                f"{sum(1 for r in valid if r['ols']['keff_beta'] < 0 and r['ols']['keff_p'] < 0.05)}/{nv}"
504	            ),
505	            "keff_residualized_sig_count": (
506	                f"{sum(1 for r in valid if r.get('residualized_keff_p', 1) < 0.05)}/{nv}"
507	            ),
508	            "eta_max_bonferroni_sig_count": (
509	                f"{sum(1 for r in valid if r.get('eta_max_bonferroni_p', 1) < 0.05)}/{nv}"
510	            ),
511	            "eta_max_fdr_sig_count": (
512	                f"{sum(1 for r in valid if r.get('eta_max_fdr_p', 1) < 0.05)}/{nv}"
513	            ),
514	            "mean_vif_keff": float(np.mean([r["vif_keff"] for r in valid])),
515	            "mean_R2": float(np.mean([r["ols"]["R2"] for r in valid])),
516	        }
517	
518	    output = {
519	        "n_panels": 455,
520	        "n_models": len(ALL_MODELS),
521	        "models": ALL_MODELS,
522	        "datasets": DATASETS,
523	        "attacks": ATTACKS,
524	        "conditions": condition_results,
525	        "summary": summary,
526	    }
527	
528	    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
529	    out_path = OUTPUT_DIR / "step4_regression_results.json"
530	    with open(out_path, "w") as f:
531	        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
532	    logger.info(f"\nResults saved: {out_path}")
533	
534	    logger.info("\n" + "=" * 60)
535	    logger.info("SUMMARY")
536	    logger.info("=" * 60)
537	    for k, v in summary.items():
538	        logger.info(f"  {k}: {v}")
539	
540	    # Per-condition table
541	    logger.info(f"\n{'Condition':<35} {'R²':>6} {'K_eff β':>9} {'K_eff p':>9} {'η_max β':>9} {'η_max p':>9} {'VIF':>5}")
542	    logger.info("-" * 90)
543	    for ck in valid_cond_keys:
544	        r = condition_results[ck]
545	        o = r["ols"]
546	        logger.info(
547	            f"  {ck:<33} {o['R2']:>6.3f} {o['keff_beta']:>+9.4f} {o['keff_p']:>9.4f} "
548	            f"{o['eta_max_beta']:>+9.4f} {o['eta_max_p']:>9.4f} {r['vif_keff']:>5.1f}"
549	        )
550	
551	
552	if __name__ == "__main__":
553	    main()
554	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "de276cd2-258c-4b62-b232-bdf0edbee37c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 4: Panel regression — 455 panels × 12 conditions.\n\nInput:\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\n\nOutput:\n  - artifacts/results/plan001/panel_regression/step4_regression_results.json\n\nDependencies: numpy, scipy, statsmodels\nOptional: pingouin (for partial_corr; manual fallback included)\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport warnings\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy import optimize, stats, special\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\nfrom statsmodels.stats.multitest import multipletests\n\nfrom src.utils import setup_logging\n\nlogger = setup_logging(\"plan001_step4\")\n\n# ── Constants ────────────────────────────────────────────────────────\nLOCAL_MODELS = [\n    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",\n    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",\n]\nAPI_MODELS = [\n    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",\n    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",\n    \"gpt-4o-mini\", \"claude-3-haiku\",\n]\nALL_MODELS = LOCAL_MODELS + API_MODELS\nDATASETS = [\"mmlu\", \"arc_challenge\"]\nATTACKS = [\n    \"prompt_injection\", \"sycophancy\", \"score_manipulation\",\n    \"verbosity_bias\", \"position_bias\", \"authority_bias\",\n]\nEPS = 0.001\n\nRESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")\nPLAN001_DIR = RESULTS_DIR / \"plan001\"\nSCORES_DIR = PLAN001_DIR / \"individual_scores\"\nMI_PATH = PLAN001_DIR / \"mi_matrix\" / \"mi_matrix_15models.json\"\nCKPT_FILES = [\n    RESULTS_DIR / \"_taxonomy_checkpoint.json\",\n    RESULTS_DIR / \"_step2v3_checkpoint.json\",\n]\nOUTPUT_DIR = PLAN001_DIR / \"panel_regression\"\n\n\n# ── JSON Helper ──────────────────────────────────────────────────────\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\n# ── Data Loading ─────────────────────────────────────────────────────\n\ndef load_mi_data():\n    if not MI_PATH.exists():\n        logger.error(f\"MI matrix not found: {MI_PATH}\")\n        logger.error(\"Run Step 3 first: scripts/run_plan001_step3_mi_matrix.py\")\n        sys.exit(1)\n    with open(MI_PATH) as f:\n        data = json.load(f)\n    logger.info(f\"Loaded MI matrix: {len(data['models'])} models\")\n    return data\n\n\ndef load_pairs():\n    for ckpt_path in CKPT_FILES:\n        if not ckpt_path.exists():\n            continue\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        if \"pairs\" not in data:\n            continue\n        pairs = {}\n        for ds in DATASETS:\n            if ds in data[\"pairs\"]:\n                pairs[ds] = data[\"pairs\"][ds][:300]\n                logger.info(f\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\")\n        if pairs:\n            return pairs\n    logger.error(\"No pairs found in any checkpoint file\")\n    sys.exit(1)\n\n\ndef _invert_winners(scores):\n    \"\"\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\"\"\"\n    swap = {\"A\": \"B\", \"B\": \"A\", \"tie\": \"tie\"}\n    return [{**s, \"winner\": swap.get(s.get(\"winner\", \"tie\"), \"tie\")} for s in scores]\n\n\ndef load_all_scores():\n    \"\"\"Load sample-level clean + attacked scores for all 15 models.\n\n    Returns:\n        clean[ds][model_id] = [{\"winner\": ..., ...}, ...]\n        attacked[ds][atk][model_id] = [{\"winner\": ..., ...}, ...]\n    \"\"\"\n    clean = {ds: {} for ds in DATASETS}\n    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}\n\n    for ckpt_path in CKPT_FILES:\n        if not ckpt_path.exists():\n            continue\n        logger.info(f\"Loading checkpoint: {ckpt_path.name}\")\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        for ds in DATASETS:\n            for mid, scores in data.get(\"clean_scores\", {}).get(ds, {}).items():\n                if mid not in clean[ds]:\n                    clean[ds][mid] = scores\n            for atk in ATTACKS:\n                for mid, scores in data.get(\"attacked_scores\", {}).get(ds, {}).get(atk, {}).items():\n                    if mid not in attacked[ds][atk]:\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    if SCORES_DIR.exists():\n        logger.info(f\"Loading individual scores from {SCORES_DIR}\")\n        for mid in ALL_MODELS:\n            for ds in DATASETS:\n                fp = SCORES_DIR / f\"{mid}__{ds}__clean.json\"\n                if fp.exists() and mid not in clean[ds]:\n                    with open(fp) as f:\n                        clean[ds][mid] = json.load(f).get(\"scores\", [])\n                for atk in ATTACKS:\n                    fp = SCORES_DIR / f\"{mid}__{ds}__{atk}.json\"\n                    if fp.exists() and mid not in attacked[ds][atk]:\n                        with open(fp) as f:\n                            scores = json.load(f).get(\"scores\", [])\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    for ds in DATASETS:\n        nc = len(clean[ds])\n        logger.info(f\"  {ds} clean: {nc}/{len(ALL_MODELS)}\")\n        for atk in ATTACKS:\n            na = len(attacked[ds][atk])\n            if na > 0:\n                logger.info(f\"  {ds} {atk}: {na}/{len(ALL_MODELS)}\")\n\n    return clean, attacked\n\n\n# ── ASR Computation ──────────────────────────────────────────────────\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\n# ── Regression Helpers ───────────────────────────────────────────────\n\ndef partial_corr_manual(x, y, covar):\n    \"\"\"Partial correlation of x and y, controlling for covar.\"\"\"\n    Xc = sm.add_constant(covar)\n    rx = sm.OLS(x, Xc).fit().resid\n    ry = sm.OLS(y, Xc).fit().resid\n    r, p = stats.pearsonr(rx, ry)\n    return float(r), float(p)\n\n\ntry:\n    import pingouin as pg\n    import pandas as pd\n\n    def partial_corr_fn(x, y, covar):\n        df = pd.DataFrame({\"x\": x, \"y\": y, \"z\": covar})\n        res = pg.partial_corr(data=df, x=\"x\", y=\"y\", covar=\"z\")\n        return float(res[\"r\"].values[0]), float(res[\"p-val\"].values[0])\n    logger.info(\"Using pingouin for partial correlation\")\nexcept ImportError:\n    partial_corr_fn = partial_corr_manual\n    logger.info(\"pingouin not available, using manual partial correlation\")\n\n\ndef beta_regression_mle(y_raw, X):\n    \"\"\"Beta regression via MLE. y in (0,1), logit link.\n    X should include constant column.\n    Returns dict with coefficients/p-values or None on failure.\"\"\"\n    y = np.clip(y_raw, 1e-6, 1 - 1e-6)\n    n, k = X.shape\n\n    def neg_ll(params):\n        beta = params[:k]\n        phi = np.exp(params[k])\n        mu = 1.0 / (1.0 + np.exp(-(X @ beta)))\n        a = mu * phi\n        b = (1.0 - mu) * phi\n        return -np.sum(\n            special.gammaln(phi) - special.gammaln(a) - special.gammaln(b)\n            + (a - 1.0) * np.log(y) + (b - 1.0) * np.log(1.0 - y)\n        )\n\n    # Initial values from OLS on logit(y)\n    y_logit = np.log(y / (1.0 - y))\n    x0 = np.zeros(k + 1)\n    try:\n        init_fit = sm.OLS(y_logit, X).fit()\n        x0[:k] = init_fit.params\n    except Exception:\n        pass\n    x0[k] = np.log(10.0)\n\n    with warnings.catch_warnings():\n        warnings.simplefilter(\"ignore\")\n        res = optimize.minimize(neg_ll, x0, method=\"L-BFGS-B\",\n                                options={\"maxiter\": 5000, \"ftol\": 1e-12})\n    if not res.success:\n        return None\n\n    # Numerical Hessian for standard errors\n    n_p = len(res.x)\n    H = np.zeros((n_p, n_p))\n    eps_h = 1e-5\n    for i in range(n_p):\n        for j in range(i, n_p):\n            ei = np.zeros(n_p)\n            ej = np.zeros(n_p)\n            ei[i] = eps_h\n            ej[j] = eps_h\n            fpp = neg_ll(res.x + ei + ej)\n            fpm = neg_ll(res.x + ei - ej)\n            fmp = neg_ll(res.x - ei + ej)\n            fmm = neg_ll(res.x - ei - ej)\n            H[i, j] = H[j, i] = (fpp - fpm - fmp + fmm) / (4.0 * eps_h * eps_h)\n\n    try:\n        cov = np.linalg.inv(H)\n        se = np.sqrt(np.maximum(np.diag(cov), 0.0))\n    except np.linalg.LinAlgError:\n        return None\n\n    beta = res.x[:k]\n    se_b = se[:k]\n    z = beta / np.maximum(se_b, 1e-12)\n    pvals = 2.0 * (1.0 - stats.norm.cdf(np.abs(z)))\n    return {\"beta\": beta, \"se\": se_b, \"z\": z, \"p\": pvals}\n\n\ndef run_condition_analysis(panel_asrs, keffs, eta_maxs):\n    \"\"\"Full regression suite for one condition. All arrays shape (n,).\"\"\"\n    n = len(panel_asrs)\n    y = np.log(panel_asrs + EPS)\n    x1 = np.log(keffs)\n    x2 = np.log(eta_maxs + EPS)\n    X = np.column_stack([x1, x2])\n    Xc = sm.add_constant(X)\n    results = {}\n\n    # ── OLS ──\n    fit = sm.OLS(y, Xc).fit()\n    results[\"ols\"] = {\n        \"keff_beta\": float(fit.params[1]),\n        \"keff_t\": float(fit.tvalues[1]),\n        \"keff_p\": float(fit.pvalues[1]),\n        \"eta_max_beta\": float(fit.params[2]),\n        \"eta_max_t\": float(fit.tvalues[2]),\n        \"eta_max_p\": float(fit.pvalues[2]),\n        \"R2\": float(fit.rsquared),\n        \"adj_R2\": float(fit.rsquared_adj),\n        \"f_stat\": float(fit.fvalue) if np.isfinite(fit.fvalue) else None,\n        \"f_pvalue\": float(fit.f_pvalue) if np.isfinite(fit.f_pvalue) else None,\n    }\n\n    # ── VIF ──\n    results[\"vif_keff\"] = float(variance_inflation_factor(Xc, 1))\n    results[\"vif_eta_max\"] = float(variance_inflation_factor(Xc, 2))\n\n    # ── Partial correlation (K_eff | η_max) ──\n    pr, pp = partial_corr_fn(x1, y, x2)\n    results[\"partial_r_keff\"] = pr\n    results[\"partial_r_keff_p\"] = pp\n\n    # ── Residualized K_eff ──\n    Xz = sm.add_constant(x2)\n    resid_keff = sm.OLS(x1, Xz).fit().resid\n    Xr = sm.add_constant(resid_keff)\n    fit_r = sm.OLS(y, Xr).fit()\n    results[\"residualized_keff_beta\"] = float(fit_r.params[1])\n    results[\"residualized_keff_t\"] = float(fit_r.tvalues[1])\n    results[\"residualized_keff_p\"] = float(fit_r.pvalues[1])\n\n    # ── Beta regression ──\n    y_raw = np.clip(panel_asrs, 0.0, 1.0)\n    br = beta_regression_mle(y_raw, Xc)\n    if br is not None:\n        results[\"beta_reg_keff_beta\"] = float(br[\"beta\"][1])\n        results[\"beta_reg_keff_p\"] = float(br[\"p\"][1])\n        results[\"beta_reg_eta_max_beta\"] = float(br[\"beta\"][2])\n        results[\"beta_reg_eta_max_p\"] = float(br[\"p\"][2])\n    else:\n        results[\"beta_reg_keff_p\"] = None\n        results[\"beta_reg_eta_max_p\"] = None\n\n    return results\n\n\n# ── Main ─────────────────────────────────────────────────────────────\n\ndef main():\n    logger.info(\"=\" * 60)\n    logger.info(\"Plan 001 Step 4: Panel Regression (455 panels × 12 conditions)\")\n    logger.info(\"=\" * 60)\n\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    # Precompute individual ASR for all model × condition\n    logger.info(\"\\nPrecomputing individual ASR...\")\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    logger.info(f\"  Computed {len(ind_asr)} individual ASR values\")\n\n    # Enumerate all C(15,3)=455 panels\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n    logger.info(f\"  Total panels: {len(all_combos)}\")\n\n    condition_results = {}\n    raw_eta_ps = []\n    raw_keff_ps = []\n    valid_cond_keys = []\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        for atk in ATTACKS:\n            cond = f\"{ds}×{atk}\"\n            logger.info(f\"\\n--- {cond} ---\")\n\n            p_asrs, p_keffs, p_etas = [], [], []\n            skipped = 0\n\n            for combo in all_combos:\n                jids = [ALL_MODELS[i] for i in combo]\n\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    skipped += 1\n                    continue\n                pk = \"|\".join(jids)\n                if pk not in keff_data:\n                    skipped += 1\n                    continue\n\n                keff = keff_data[pk][\"keff\"]\n                etas = [ind_asr[(ds, atk, j)] for j in jids]\n                eta_max = max(etas)\n\n                cs = {j: clean[ds][j] for j in jids}\n                ats = {j: attacked[ds][atk][j] for j in jids}\n                p_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n                p_asrs.append(p_asr)\n                p_keffs.append(keff)\n                p_etas.append(eta_max)\n\n            n_panels = len(p_asrs)\n            logger.info(f\"  {n_panels} panels with data, {skipped} skipped\")\n\n            if n_panels < 10:\n                logger.warning(f\"  Too few panels ({n_panels}), skipping\")\n                condition_results[cond] = {\"n_panels\": n_panels, \"skipped\": True}\n                continue\n\n            p_asrs = np.array(p_asrs)\n            p_keffs = np.array(p_keffs)\n            p_etas = np.array(p_etas)\n\n            if np.std(p_asrs) < 1e-10:\n                logger.warning(f\"  Constant ASR ({p_asrs[0]:.4f}), skipping regression\")\n                condition_results[cond] = {\n                    \"n_panels\": n_panels, \"skipped\": True,\n                    \"reason\": \"constant_asr\", \"asr_value\": float(p_asrs[0]),\n                }\n                continue\n\n            cond_res = run_condition_analysis(p_asrs, p_keffs, p_etas)\n            cond_res[\"n_panels\"] = n_panels\n            cond_res[\"skipped\"] = False\n            cond_res[\"asr_stats\"] = {\n                \"mean\": float(np.mean(p_asrs)),\n                \"std\": float(np.std(p_asrs)),\n                \"min\": float(np.min(p_asrs)),\n                \"max\": float(np.max(p_asrs)),\n                \"pct_zero\": float(np.mean(p_asrs == 0)),\n            }\n            condition_results[cond] = cond_res\n\n            raw_eta_ps.append(cond_res[\"ols\"][\"eta_max_p\"])\n            raw_keff_ps.append(cond_res[\"ols\"][\"keff_p\"])\n            valid_cond_keys.append(cond)\n\n            ols = cond_res[\"ols\"]\n            sig_k = \"***\" if ols[\"keff_p\"] < 0.001 else \"**\" if ols[\"keff_p\"] < 0.01 else \"*\" if ols[\"keff_p\"] < 0.05 else \"ns\"\n            sig_e = \"***\" if ols[\"eta_max_p\"] < 0.001 else \"**\" if ols[\"eta_max_p\"] < 0.01 else \"*\" if ols[\"eta_max_p\"] < 0.05 else \"ns\"\n            logger.info(\n                f\"  OLS R²={ols['R2']:.4f}  \"\n                f\"K_eff: β={ols['keff_beta']:+.4f} p={ols['keff_p']:.4f} {sig_k}  \"\n                f\"η_max: β={ols['eta_max_beta']:+.4f} p={ols['eta_max_p']:.4f} {sig_e}\"\n            )\n            logger.info(\n                f\"  VIF: K_eff={cond_res['vif_keff']:.2f}, η_max={cond_res['vif_eta_max']:.2f}\"\n            )\n            logger.info(\n                f\"  Partial r(K_eff|η_max)={cond_res['partial_r_keff']:.4f} \"\n                f\"p={cond_res['partial_r_keff_p']:.4f}\"\n            )\n            logger.info(\n                f\"  Residualized K_eff: β={cond_res['residualized_keff_beta']:+.4f} \"\n                f\"p={cond_res['residualized_keff_p']:.4f}\"\n            )\n\n    # ── Multiple testing corrections ──\n    if raw_eta_ps:\n        _, bonf_eta, _, _ = multipletests(raw_eta_ps, method=\"bonferroni\")\n        _, fdr_eta, _, _ = multipletests(raw_eta_ps, method=\"fdr_bh\")\n        _, bonf_keff, _, _ = multipletests(raw_keff_ps, method=\"bonferroni\")\n        _, fdr_keff, _, _ = multipletests(raw_keff_ps, method=\"fdr_bh\")\n\n        for i, ck in enumerate(valid_cond_keys):\n            condition_results[ck][\"eta_max_bonferroni_p\"] = float(bonf_eta[i])\n            condition_results[ck][\"eta_max_fdr_p\"] = float(fdr_eta[i])\n            condition_results[ck][\"keff_bonferroni_p\"] = float(bonf_keff[i])\n            condition_results[ck][\"keff_fdr_p\"] = float(fdr_keff[i])\n\n    # ── Summary ──\n    valid = [condition_results[k] for k in valid_cond_keys]\n    nv = len(valid)\n    summary = {}\n    if nv > 0:\n        summary = {\n            \"keff_sig_negative_count\": (\n                f\"{sum(1 for r in valid if r['ols']['keff_beta'] < 0 and r['ols']['keff_p'] < 0.05)}/{nv}\"\n            ),\n            \"keff_residualized_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('residualized_keff_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"eta_max_bonferroni_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('eta_max_bonferroni_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"eta_max_fdr_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('eta_max_fdr_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"mean_vif_keff\": float(np.mean([r[\"vif_keff\"] for r in valid])),\n            \"mean_R2\": float(np.mean([r[\"ols\"][\"R2\"] for r in valid])),\n        }\n\n    output = {\n        \"n_panels\": 455,\n        \"n_models\": len(ALL_MODELS),\n        \"models\": ALL_MODELS,\n        \"datasets\": DATASETS,\n        \"attacks\": ATTACKS,\n        \"conditions\": condition_results,\n        \"summary\": summary,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    out_path = OUTPUT_DIR / \"step4_regression_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    logger.info(f\"\\nResults saved: {out_path}\")\n\n    logger.info(\"\\n\" + \"=\" * 60)\n    logger.info(\"SUMMARY\")\n    logger.info(\"=\" * 60)\n    for k, v in summary.items():\n        logger.info(f\"  {k}: {v}\")\n\n    # Per-condition table\n    logger.info(f\"\\n{'Condition':<35} {'R²':>6} {'K_eff β':>9} {'K_eff p':>9} {'η_max β':>9} {'η_max p':>9} {'VIF':>5}\")\n    logger.info(\"-\" * 90)\n    for ck in valid_cond_keys:\n        r = condition_results[ck]\n        o = r[\"ols\"]\n        logger.info(\n            f\"  {ck:<33} {o['R2']:>6.3f} {o['keff_beta']:>+9.4f} {o['keff_p']:>9.4f} \"\n            f\"{o['eta_max_beta']:>+9.4f} {o['eta_max_p']:>9.4f} {r['vif_keff']:>5.1f}\"\n        )\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 554,
      "startLine": 1,
      "totalLines": 554
    }
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01DHK1QUqmpZjqHKogcdWyAs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step5_random_fault.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "9f0af250-9e00-43f9-aea4-83ca71988772",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgSLYGx6LvgdkELMs8G7Lu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6156,
      "cache_creation_input_tokens": 4123,
      "cache_read_input_tokens": 52808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4123
      },
      "output_tokens": 38,
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

_source line 49 · 2026-05-22T14:58:34.999Z_

<details><summary>↩ Tool result · `toolu_01DHK1QUqmpZjqHKogcdWyAs`</summary>

```text
1	#!/usr/bin/env python3
2	"""Plan 001 Step 5: Random-fault simulation — 455 panels × 12 conditions.
3	
4	Input:
5	  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json
6	  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/
7	  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json
8	
9	Output:
10	  - artifacts/results/plan001/panel_regression/step5_random_fault_results.json
11	
12	Dependencies: numpy, scipy, statsmodels
13	"""
14	
15	import os
16	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
17	
18	import sys
19	sys.path.insert(0, "/root/cert_manip_resist_eval")
20	
21	import json
22	import warnings
23	import itertools
24	import numpy as np
25	import statsmodels.api as sm
26	from pathlib import Path
27	from scipy import stats
28	
29	from src.utils import setup_logging
30	
31	logger = setup_logging("plan001_step5")
32	
33	# ── Constants ────────────────────────────────────────────────────────
34	LOCAL_MODELS = [
35	    "qwen2.5-72b", "llama3.1-70b", "mistral-large",
36	    "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b",
37	]
38	API_MODELS = [
39	    "claude-opus-4", "gpt-5.5", "gemini-2.5-pro", "gpt-4.1",
40	    "claude-sonnet-4", "gpt-4o", "gemini-2.5-flash",
41	    "gpt-4o-mini", "claude-3-haiku",
42	]
43	ALL_MODELS = LOCAL_MODELS + API_MODELS
44	DATASETS = ["mmlu", "arc_challenge"]
45	ATTACKS = [
46	    "prompt_injection", "sycophancy", "score_manipulation",
47	    "verbosity_bias", "position_bias", "authority_bias",
48	]
49	EPS = 0.001
50	N_SIMS = 1000
51	N_SAMPLES = 300
52	SIM_BATCH = 100
53	
54	RESULTS_DIR = Path("/root/cert_manip_resist_eval/artifacts/results")
55	PLAN001_DIR = RESULTS_DIR / "plan001"
56	SCORES_DIR = PLAN001_DIR / "individual_scores"
57	MI_PATH = PLAN001_DIR / "mi_matrix" / "mi_matrix_15models.json"
58	CKPT_FILES = [
59	    RESULTS_DIR / "_taxonomy_checkpoint.json",
60	    RESULTS_DIR / "_step2v3_checkpoint.json",
61	]
62	OUTPUT_DIR = PLAN001_DIR / "panel_regression"
63	
64	
65	# ── JSON Helper ──────────────────────────────────────────────────────
66	
67	def _json_default(obj):
68	    if isinstance(obj, np.floating):
69	        v = float(obj)
70	        return None if (np.isnan(v) or np.isinf(v)) else v
71	    if isinstance(obj, np.integer):
72	        return int(obj)
73	    if isinstance(obj, np.ndarray):
74	        return obj.tolist()
75	    if isinstance(obj, np.bool_):
76	        return bool(obj)
77	    raise TypeError(f"Not JSON serializable: {type(obj)}")
78	
79	
80	# ── Data Loading (shared with Step 4) ────────────────────────────────
81	
82	def load_mi_data():
83	    if not MI_PATH.exists():
84	        logger.error(f"MI matrix not found: {MI_PATH}")
85	        sys.exit(1)
86	    with open(MI_PATH) as f:
87	        data = json.load(f)
88	    logger.info(f"Loaded MI matrix: {len(data['models'])} models")
89	    return data
90	
91	
92	def load_pairs():
93	    for ckpt_path in CKPT_FILES:
94	        if not ckpt_path.exists():
95	            continue
96	        with open(ckpt_path) as f:
97	            data = json.load(f)
98	        if "pairs" not in data:
99	            continue
100	        pairs = {}
101	        for ds in DATASETS:
102	            if ds in data["pairs"]:
103	                pairs[ds] = data["pairs"][ds][:300]
104	                logger.info(f"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}")
105	        if pairs:
106	            return pairs
107	    logger.error("No pairs found in any checkpoint file")
108	    sys.exit(1)
109	
110	
111	def _invert_winners(scores):
112	    swap = {"A": "B", "B": "A", "tie": "tie"}
113	    return [{**s, "winner": swap.get(s.get("winner", "tie"), "tie")} for s in scores]
114	
115	
116	def load_all_scores():
117	    clean = {ds: {} for ds in DATASETS}
118	    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}
119	
120	    for ckpt_path in CKPT_FILES:
121	        if not ckpt_path.exists():
122	            continue
123	        logger.info(f"Loading checkpoint: {ckpt_path.name}")
124	        with open(ckpt_path) as f:
125	            data = json.load(f)
126	        for ds in DATASETS:
127	            for mid, scores in data.get("clean_scores", {}).get(ds, {}).items():
128	                if mid not in clean[ds]:
129	                    clean[ds][mid] = scores
130	            for atk in ATTACKS:
131	                for mid, scores in data.get("attacked_scores", {}).get(ds, {}).get(atk, {}).items():
132	                    if mid not in attacked[ds][atk]:
133	                        if atk == "position_bias":
134	                            scores = _invert_winners(scores)
135	                        attacked[ds][atk][mid] = scores
136	
137	    if SCORES_DIR.exists():
138	        logger.info(f"Loading individual scores from {SCORES_DIR}")
139	        for mid in ALL_MODELS:
140	            for ds in DATASETS:
141	                fp = SCORES_DIR / f"{mid}__{ds}__clean.json"
142	                if fp.exists() and mid not in clean[ds]:
143	                    with open(fp) as f:
144	                        clean[ds][mid] = json.load(f).get("scores", [])
145	                for atk in ATTACKS:
146	                    fp = SCORES_DIR / f"{mid}__{ds}__{atk}.json"
147	                    if fp.exists() and mid not in attacked[ds][atk]:
148	                        with open(fp) as f:
149	                            scores = json.load(f).get("scores", [])
150	                        if atk == "position_bias":
151	                            scores = _invert_winners(scores)
152	                        attacked[ds][atk][mid] = scores
153	
154	    for ds in DATASETS:
155	        nc = len(clean[ds])
156	        logger.info(f"  {ds} clean: {nc}/{len(ALL_MODELS)}")
157	        for atk in ATTACKS:
158	            na = len(attacked[ds][atk])
159	            if na > 0:
160	                logger.info(f"  {ds} {atk}: {na}/{len(ALL_MODELS)}")
161	
162	    return clean, attacked
163	
164	
165	# ── ASR Computation ──────────────────────────────────────────────────
166	
167	def majority_vote(votes):
168	    counts = {"A": 0, "B": 0, "tie": 0}
169	    for v in votes:
170	        counts[v] = counts.get(v, 0) + 1
171	    mc = max(counts.values())
172	    winners = [k for k, c in counts.items() if c == mc]
173	    if len(winners) == 1:
174	        return winners[0]
175	    for w in winners:
176	        if w != "tie":
177	            return w
178	    return "tie"
179	
180	
181	def compute_individual_asr(clean_list, attacked_list, pairs):
182	    n = min(len(clean_list), len(attacked_list), len(pairs))
183	    n_flips = n_correct = 0
184	    for i in range(n):
185	        gt = pairs[i]["ground_truth_winner"]
186	        if clean_list[i].get("winner", "tie") == gt:
187	            n_correct += 1
188	            if attacked_list[i].get("winner", "tie") != gt:
189	                n_flips += 1
190	    return n_flips / max(n_correct, 1)
191	
192	
193	def compute_panel_asr(jids, clean, attacked, pairs):
194	    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))
195	    n_flips = n_correct = 0
196	    for i in range(n):
197	        gt = pairs[i]["ground_truth_winner"]
198	        cv = majority_vote([clean[j][i].get("winner", "tie") for j in jids])
199	        if cv != gt:
200	            continue
201	        n_correct += 1
202	        av = majority_vote([attacked[j][i].get("winner", "tie") for j in jids])
203	        if av != gt:
204	            n_flips += 1
205	    return n_flips / max(n_correct, 1)
206	
207	
208	# ── Random-Fault Simulation ─────────────────────────────────────────
209	
210	def analytical_rf_asr(eta):
211	    """Analytical P(panel error) for majority vote with 3 independent judges.
212	    P(≥2 fail) = η₁η₂ + η₁η₃ + η₂η₃ - 2η₁η₂η₃"""
213	    e1, e2, e3 = eta
214	    return e1 * e2 + e1 * e3 + e2 * e3 - 2.0 * e1 * e2 * e3
215	
216	
217	def simulate_rf_vectorized(eta_all, rng):
218	    """Simulate random-fault ASR for all panels.
219	
220	    Args:
221	        eta_all: (n_panels, 3) array of individual judge error rates
222	        rng: numpy random generator
223	
224	    Returns:
225	        rf_mean: (n_panels,) mean RF ASR across simulations
226	        rf_std: (n_panels,) std RF ASR across simulations
227	    """
228	    n_panels = eta_all.shape[0]
229	    rf_sum = np.zeros(n_panels)
230	    rf_sq_sum = np.zeros(n_panels)
231	
232	    for sim_start in range(0, N_SIMS, SIM_BATCH):
233	        b = min(SIM_BATCH, N_SIMS - sim_start)
234	        # (n_panels, batch, n_samples, 3) random draws
235	        randoms = rng.random((n_panels, b, N_SAMPLES, 3))
236	        # Each judge errors independently with probability eta_j
237	        errors = randoms < eta_all[:, np.newaxis, np.newaxis, :]
238	        # Majority vote: panel errs if ≥2 judges err
239	        panel_err = errors.sum(axis=3) >= 2
240	        # Error rate per sim: (n_panels, batch)
241	        rates = panel_err.mean(axis=2).astype(np.float64)
242	        rf_sum += rates.sum(axis=1)
243	        rf_sq_sum += (rates ** 2).sum(axis=1)
244	
245	    rf_mean = rf_sum / N_SIMS
246	    rf_std = np.sqrt(np.maximum(rf_sq_sum / N_SIMS - rf_mean ** 2, 0.0))
247	    return rf_mean, rf_std
248	
249	
250	# ── Regression ───────────────────────────────────────────────────────
251	
252	def run_ols(y_raw, keffs, eta_maxs):
253	    """Simple OLS: log(y+ε) ~ log(K_eff) + log(η_max+ε)."""
254	    y = np.log(y_raw + EPS)
255	    X = np.column_stack([np.log(keffs), np.log(eta_maxs + EPS)])
256	    Xc = sm.add_constant(X)
257	    fit = sm.OLS(y, Xc).fit()
258	    return {
259	        "keff_beta": float(fit.params[1]),
260	        "keff_t": float(fit.tvalues[1]),
261	        "keff_p": float(fit.pvalues[1]),
262	        "eta_max_beta": float(fit.params[2]),
263	        "eta_max_t": float(fit.tvalues[2]),
264	        "eta_max_p": float(fit.pvalues[2]),
265	        "R2": float(fit.rsquared),
266	        "adj_R2": float(fit.rsquared_adj),
267	    }
268	
269	
270	# ── Main ─────────────────────────────────────────────────────────────
271	
272	def main():
273	    logger.info("=" * 60)
274	    logger.info("Plan 001 Step 5: Random-Fault Simulation")
275	    logger.info(f"  {N_SIMS} simulations × {N_SAMPLES} samples per panel")
276	    logger.info("=" * 60)
277	
278	    mi_data = load_mi_data()
279	    pairs = load_pairs()
280	    clean, attacked = load_all_scores()
281	
282	    # Precompute individual ASR
283	    logger.info("\nPrecomputing individual ASR...")
284	    ind_asr = {}
285	    for ds in DATASETS:
286	        for atk in ATTACKS:
287	            for mid in ALL_MODELS:
288	                if mid in clean[ds] and mid in attacked[ds][atk]:
289	                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
290	                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]
291	                    )
292	    logger.info(f"  Computed {len(ind_asr)} individual ASR values")
293	
294	    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))
295	    rng = np.random.default_rng(42)
296	
297	    condition_results = {}
298	
299	    for ds in DATASETS:
300	        keff_data = mi_data["keff_per_panel"].get(ds, {})
301	        for atk in ATTACKS:
302	            cond = f"{ds}×{atk}"
303	            logger.info(f"\n--- {cond} ---")
304	
305	            # Collect panel data
306	            panel_keffs = []
307	            panel_eta_maxs = []
308	            panel_eta_all = []  # (n_panels, 3) for simulation
309	            panel_adaptive_asrs = []
310	            panel_jids_list = []
311	            skipped = 0
312	
313	            for combo in all_combos:
314	                jids = [ALL_MODELS[i] for i in combo]
315	                if not all((ds, atk, j) in ind_asr for j in jids):
316	                    skipped += 1
317	                    continue
318	                pk = "|".join(jids)
319	                if pk not in keff_data:
320	                    skipped += 1
321	                    continue
322	
323	                keff = keff_data[pk]["keff"]
324	                etas = [ind_asr[(ds, atk, j)] for j in jids]
325	
326	                # Adaptive panel ASR (majority vote on actual scores)
327	                cs = {j: clean[ds][j] for j in jids}
328	                ats = {j: attacked[ds][atk][j] for j in jids}
329	                adaptive_asr = compute_panel_asr(jids, cs, ats, pairs[ds])
330	
331	                panel_keffs.append(keff)
332	                panel_eta_maxs.append(max(etas))
333	                panel_eta_all.append(etas)
334	                panel_adaptive_asrs.append(adaptive_asr)
335	                panel_jids_list.append(jids)
336	
337	            n_panels = len(panel_keffs)
338	            logger.info(f"  {n_panels} panels with data, {skipped} skipped")
339	
340	            if n_panels < 10:
341	                logger.warning(f"  Too few panels ({n_panels}), skipping")
342	                condition_results[cond] = {"n_panels": n_panels, "skipped": True}
343	                continue
344	
345	            keffs = np.array(panel_keffs)
346	            eta_maxs = np.array(panel_eta_maxs)
347	            eta_all = np.array(panel_eta_all)  # (n_panels, 3)
348	            adaptive_asrs = np.array(panel_adaptive_asrs)
349	
350	            # ── Random-fault simulation ──
351	            logger.info(f"  Simulating {N_SIMS} RF runs...")
352	            rf_mean, rf_std = simulate_rf_vectorized(eta_all, rng)
353	
354	            # Analytical validation
355	            analytical = np.array([analytical_rf_asr(e) for e in eta_all])
356	            max_dev = np.max(np.abs(rf_mean - analytical))
357	            logger.info(f"  RF simulation done. Max deviation from analytical: {max_dev:.6f}")
358	
359	            # ── Regressions ──
360	            # Adaptive
361	            if np.std(adaptive_asrs) < 1e-10:
362	                logger.warning(f"  Constant adaptive ASR, skipping regression")
363	                adaptive_ols = {"keff_beta": 0, "keff_p": 1, "R2": 0, "note": "constant_asr"}
364	            else:
365	                adaptive_ols = run_ols(adaptive_asrs, keffs, eta_maxs)
366	
367	            # Random-fault
368	            if np.std(rf_mean) < 1e-10:
369	                logger.warning(f"  Constant RF ASR, skipping regression")
370	                rf_ols = {"keff_beta": 0, "keff_p": 1, "R2": 0, "note": "constant_asr"}
371	            else:
372	                rf_ols = run_ols(rf_mean, keffs, eta_maxs)
373	
374	            delta_R2 = rf_ols.get("R2", 0) - adaptive_ols.get("R2", 0)
375	            keff_gains = (
376	                rf_ols.get("keff_p", 1) < 0.05
377	                and rf_ols.get("keff_p", 1) < adaptive_ols.get("keff_p", 1)
378	            )
379	
380	            # ── High-K_eff + Low-η_max benefit analysis ──
381	            keff_q75 = np.percentile(keffs, 75)
382	            eta_q25 = np.percentile(eta_maxs, 25)
383	            hk_le_mask = (keffs >= keff_q75) & (eta_maxs <= eta_q25)
384	            n_hk_le = int(hk_le_mask.sum())
385	            hk_le_benefit = None
386	            hk_le_pval = None
387	            if n_hk_le >= 5:
388	                diff = adaptive_asrs[hk_le_mask] - rf_mean[hk_le_mask]
389	                hk_le_benefit = float(np.mean(diff))
390	                if np.std(diff) > 1e-10:
391	                    _, hk_le_pval = stats.ttest_1samp(diff, 0)
392	                    hk_le_pval = float(hk_le_pval)
393	
394	            cond_res = {
395	                "n_panels": n_panels,
396	                "skipped": False,
397	                "adaptive": adaptive_ols,
398	                "random_fault": rf_ols,
399	                "delta_R2": float(delta_R2),
400	                "keff_gains_significance": bool(keff_gains),
401	                "rf_stats": {
402	                    "mean": float(np.mean(rf_mean)),
403	                    "std": float(np.mean(rf_std)),
404	                    "max_analytical_deviation": float(max_dev),
405	                },
406	                "adaptive_stats": {
407	                    "mean": float(np.mean(adaptive_asrs)),
408	                    "std": float(np.std(adaptive_asrs)),
409	                },
410	                "high_keff_low_eta": {
411	                    "n_panels": n_hk_le,
412	                    "keff_threshold": float(keff_q75),
413	                    "eta_threshold": float(eta_q25),
414	                    "mean_benefit_adaptive_minus_rf": hk_le_benefit,
415	                    "benefit_pval": hk_le_pval,
416	                },
417	            }
418	            condition_results[cond] = cond_res
419	
420	            logger.info(
421	                f"  Adaptive: K_eff β={adaptive_ols.get('keff_beta', 0):+.4f} "
422	                f"p={adaptive_ols.get('keff_p', 1):.4f} R²={adaptive_ols.get('R2', 0):.4f}"
423	            )
424	            logger.info(
425	                f"  RF:       K_eff β={rf_ols.get('keff_beta', 0):+.4f} "
426	                f"p={rf_ols.get('keff_p', 1):.4f} R²={rf_ols.get('R2', 0):.4f}"
427	            )
428	            logger.info(f"  ΔR²={delta_R2:+.4f}  K_eff gains significance: {keff_gains}")
429	            if n_hk_le >= 5:
430	                logger.info(
431	                    f"  High-K/Low-η panels ({n_hk_le}): "
432	                    f"mean benefit={hk_le_benefit:+.4f} p={hk_le_pval}"
433	                )
434	
435	    # ── Summary ──
436	    valid = {k: v for k, v in condition_results.items() if not v.get("skipped")}
437	    nv = len(valid)
438	
439	    if nv > 0:
440	        n_adapt_sig = sum(
441	            1 for v in valid.values()
442	            if v["adaptive"].get("keff_p", 1) < 0.05 and v["adaptive"].get("keff_beta", 0) < 0
443	        )
444	        n_rf_sig = sum(
445	            1 for v in valid.values()
446	            if v["random_fault"].get("keff_p", 1) < 0.05 and v["random_fault"].get("keff_beta", 0) < 0
447	        )
448	        mean_dR2 = float(np.mean([v["delta_R2"] for v in valid.values()]))
449	        n_gains = sum(1 for v in valid.values() if v["keff_gains_significance"])
450	
451	        # Build interpretation
452	        parts = []
453	        parts.append(
454	            f"K_eff significantly negative in {n_rf_sig}/{nv} conditions under RF "
455	            f"vs {n_adapt_sig}/{nv} under adaptive."
456	        )
457	        if mean_dR2 > 0:
458	            parts.append(
459	                f"RF model explains more variance (mean ΔR²={mean_dR2:+.3f}), "
460	                "consistent with independent-error majority vote theory."
461	            )
462	        else:
463	            parts.append(
464	                f"Adaptive model explains more variance (mean ΔR²={mean_dR2:+.3f})."
465	            )
466	        if n_gains > nv // 2:
467	            parts.append(
468	                f"K_eff gains significance in {n_gains}/{nv} conditions under RF, "
469	                "suggesting diversity benefit is undermined by adaptive attacks."
470	            )
471	        interpretation = " ".join(parts)
472	
473	        summary = {
474	            "adaptive_keff_sig_negative": f"{n_adapt_sig}/{nv}",
475	            "random_fault_keff_sig_negative": f"{n_rf_sig}/{nv}",
476	            "mean_delta_R2": mean_dR2,
477	            "keff_gains_significance_count": f"{n_gains}/{nv}",
478	            "interpretation": interpretation,
479	        }
480	    else:
481	        summary = {"note": "No valid conditions to summarize"}
482	
483	    output = {
484	        "n_panels": 455,
485	        "n_simulations": N_SIMS,
486	        "n_samples_per_sim": N_SAMPLES,
487	        "models": ALL_MODELS,
488	        "conditions": condition_results,
489	        "summary": summary,
490	    }
491	
492	    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
493	    out_path = OUTPUT_DIR / "step5_random_fault_results.json"
494	    with open(out_path, "w") as f:
495	        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
496	    logger.info(f"\nResults saved: {out_path}")
497	
498	    logger.info("\n" + "=" * 60)
499	    logger.info("SUMMARY")
500	    logger.info("=" * 60)
501	    for k, v in summary.items():
502	        if k != "interpretation":
503	            logger.info(f"  {k}: {v}")
504	    if "interpretation" in summary:
505	        logger.info(f"\n  {summary['interpretation']}")
506	
507	    # Comparison table
508	    valid_keys = [k for k in condition_results if not condition_results[k].get("skipped")]
509	    logger.info(f"\n{'Condition':<35} {'Adap R²':>8} {'RF R²':>8} {'ΔR²':>7} {'Adap Kp':>8} {'RF Kp':>8} {'Gains':>5}")
510	    logger.info("-" * 85)
511	    for ck in valid_keys:
512	        r = condition_results[ck]
513	        a = r["adaptive"]
514	        rf = r["random_fault"]
515	        logger.info(
516	            f"  {ck:<33} {a.get('R2', 0):>8.4f} {rf.get('R2', 0):>8.4f} "
517	            f"{r['delta_R2']:>+7.3f} {a.get('keff_p', 1):>8.4f} {rf.get('keff_p', 1):>8.4f} "
518	            f"{'Y' if r['keff_gains_significance'] else 'N':>5}"
519	        )
520	
521	
522	if __name__ == "__main__":
523	    main()
524	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "2c288529-74d1-48bf-bbec-5a5ca8c40608",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step5_random_fault.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 5: Random-fault simulation — 455 panels × 12 conditions.\n\nInput:\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\n\nOutput:\n  - artifacts/results/plan001/panel_regression/step5_random_fault_results.json\n\nDependencies: numpy, scipy, statsmodels\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport warnings\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy import stats\n\nfrom src.utils import setup_logging\n\nlogger = setup_logging(\"plan001_step5\")\n\n# ── Constants ────────────────────────────────────────────────────────\nLOCAL_MODELS = [\n    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",\n    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",\n]\nAPI_MODELS = [\n    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",\n    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",\n    \"gpt-4o-mini\", \"claude-3-haiku\",\n]\nALL_MODELS = LOCAL_MODELS + API_MODELS\nDATASETS = [\"mmlu\", \"arc_challenge\"]\nATTACKS = [\n    \"prompt_injection\", \"sycophancy\", \"score_manipulation\",\n    \"verbosity_bias\", \"position_bias\", \"authority_bias\",\n]\nEPS = 0.001\nN_SIMS = 1000\nN_SAMPLES = 300\nSIM_BATCH = 100\n\nRESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")\nPLAN001_DIR = RESULTS_DIR / \"plan001\"\nSCORES_DIR = PLAN001_DIR / \"individual_scores\"\nMI_PATH = PLAN001_DIR / \"mi_matrix\" / \"mi_matrix_15models.json\"\nCKPT_FILES = [\n    RESULTS_DIR / \"_taxonomy_checkpoint.json\",\n    RESULTS_DIR / \"_step2v3_checkpoint.json\",\n]\nOUTPUT_DIR = PLAN001_DIR / \"panel_regression\"\n\n\n# ── JSON Helper ──────────────────────────────────────────────────────\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\n# ── Data Loading (shared with Step 4) ────────────────────────────────\n\ndef load_mi_data():\n    if not MI_PATH.exists():\n        logger.error(f\"MI matrix not found: {MI_PATH}\")\n        sys.exit(1)\n    with open(MI_PATH) as f:\n        data = json.load(f)\n    logger.info(f\"Loaded MI matrix: {len(data['models'])} models\")\n    return data\n\n\ndef load_pairs():\n    for ckpt_path in CKPT_FILES:\n        if not ckpt_path.exists():\n            continue\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        if \"pairs\" not in data:\n            continue\n        pairs = {}\n        for ds in DATASETS:\n            if ds in data[\"pairs\"]:\n                pairs[ds] = data[\"pairs\"][ds][:300]\n                logger.info(f\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\")\n        if pairs:\n            return pairs\n    logger.error(\"No pairs found in any checkpoint file\")\n    sys.exit(1)\n\n\ndef _invert_winners(scores):\n    swap = {\"A\": \"B\", \"B\": \"A\", \"tie\": \"tie\"}\n    return [{**s, \"winner\": swap.get(s.get(\"winner\", \"tie\"), \"tie\")} for s in scores]\n\n\ndef load_all_scores():\n    clean = {ds: {} for ds in DATASETS}\n    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}\n\n    for ckpt_path in CKPT_FILES:\n        if not ckpt_path.exists():\n            continue\n        logger.info(f\"Loading checkpoint: {ckpt_path.name}\")\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        for ds in DATASETS:\n            for mid, scores in data.get(\"clean_scores\", {}).get(ds, {}).items():\n                if mid not in clean[ds]:\n                    clean[ds][mid] = scores\n            for atk in ATTACKS:\n                for mid, scores in data.get(\"attacked_scores\", {}).get(ds, {}).get(atk, {}).items():\n                    if mid not in attacked[ds][atk]:\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    if SCORES_DIR.exists():\n        logger.info(f\"Loading individual scores from {SCORES_DIR}\")\n        for mid in ALL_MODELS:\n            for ds in DATASETS:\n                fp = SCORES_DIR / f\"{mid}__{ds}__clean.json\"\n                if fp.exists() and mid not in clean[ds]:\n                    with open(fp) as f:\n                        clean[ds][mid] = json.load(f).get(\"scores\", [])\n                for atk in ATTACKS:\n                    fp = SCORES_DIR / f\"{mid}__{ds}__{atk}.json\"\n                    if fp.exists() and mid not in attacked[ds][atk]:\n                        with open(fp) as f:\n                            scores = json.load(f).get(\"scores\", [])\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    for ds in DATASETS:\n        nc = len(clean[ds])\n        logger.info(f\"  {ds} clean: {nc}/{len(ALL_MODELS)}\")\n        for atk in ATTACKS:\n            na = len(attacked[ds][atk])\n            if na > 0:\n                logger.info(f\"  {ds} {atk}: {na}/{len(ALL_MODELS)}\")\n\n    return clean, attacked\n\n\n# ── ASR Computation ──────────────────────────────────────────────────\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\n# ── Random-Fault Simulation ─────────────────────────────────────────\n\ndef analytical_rf_asr(eta):\n    \"\"\"Analytical P(panel error) for majority vote with 3 independent judges.\n    P(≥2 fail) = η₁η₂ + η₁η₃ + η₂η₃ - 2η₁η₂η₃\"\"\"\n    e1, e2, e3 = eta\n    return e1 * e2 + e1 * e3 + e2 * e3 - 2.0 * e1 * e2 * e3\n\n\ndef simulate_rf_vectorized(eta_all, rng):\n    \"\"\"Simulate random-fault ASR for all panels.\n\n    Args:\n        eta_all: (n_panels, 3) array of individual judge error rates\n        rng: numpy random generator\n\n    Returns:\n        rf_mean: (n_panels,) mean RF ASR across simulations\n        rf_std: (n_panels,) std RF ASR across simulations\n    \"\"\"\n    n_panels = eta_all.shape[0]\n    rf_sum = np.zeros(n_panels)\n    rf_sq_sum = np.zeros(n_panels)\n\n    for sim_start in range(0, N_SIMS, SIM_BATCH):\n        b = min(SIM_BATCH, N_SIMS - sim_start)\n        # (n_panels, batch, n_samples, 3) random draws\n        randoms = rng.random((n_panels, b, N_SAMPLES, 3))\n        # Each judge errors independently with probability eta_j\n        errors = randoms < eta_all[:, np.newaxis, np.newaxis, :]\n        # Majority vote: panel errs if ≥2 judges err\n        panel_err = errors.sum(axis=3) >= 2\n        # Error rate per sim: (n_panels, batch)\n        rates = panel_err.mean(axis=2).astype(np.float64)\n        rf_sum += rates.sum(axis=1)\n        rf_sq_sum += (rates ** 2).sum(axis=1)\n\n    rf_mean = rf_sum / N_SIMS\n    rf_std = np.sqrt(np.maximum(rf_sq_sum / N_SIMS - rf_mean ** 2, 0.0))\n    return rf_mean, rf_std\n\n\n# ── Regression ───────────────────────────────────────────────────────\n\ndef run_ols(y_raw, keffs, eta_maxs):\n    \"\"\"Simple OLS: log(y+ε) ~ log(K_eff) + log(η_max+ε).\"\"\"\n    y = np.log(y_raw + EPS)\n    X = np.column_stack([np.log(keffs), np.log(eta_maxs + EPS)])\n    Xc = sm.add_constant(X)\n    fit = sm.OLS(y, Xc).fit()\n    return {\n        \"keff_beta\": float(fit.params[1]),\n        \"keff_t\": float(fit.tvalues[1]),\n        \"keff_p\": float(fit.pvalues[1]),\n        \"eta_max_beta\": float(fit.params[2]),\n        \"eta_max_t\": float(fit.tvalues[2]),\n        \"eta_max_p\": float(fit.pvalues[2]),\n        \"R2\": float(fit.rsquared),\n        \"adj_R2\": float(fit.rsquared_adj),\n    }\n\n\n# ── Main ─────────────────────────────────────────────────────────────\n\ndef main():\n    logger.info(\"=\" * 60)\n    logger.info(\"Plan 001 Step 5: Random-Fault Simulation\")\n    logger.info(f\"  {N_SIMS} simulations × {N_SAMPLES} samples per panel\")\n    logger.info(\"=\" * 60)\n\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    # Precompute individual ASR\n    logger.info(\"\\nPrecomputing individual ASR...\")\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    logger.info(f\"  Computed {len(ind_asr)} individual ASR values\")\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n    rng = np.random.default_rng(42)\n\n    condition_results = {}\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        for atk in ATTACKS:\n            cond = f\"{ds}×{atk}\"\n            logger.info(f\"\\n--- {cond} ---\")\n\n            # Collect panel data\n            panel_keffs = []\n            panel_eta_maxs = []\n            panel_eta_all = []  # (n_panels, 3) for simulation\n            panel_adaptive_asrs = []\n            panel_jids_list = []\n            skipped = 0\n\n            for combo in all_combos:\n                jids = [ALL_MODELS[i] for i in combo]\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    skipped += 1\n                    continue\n                pk = \"|\".join(jids)\n                if pk not in keff_data:\n                    skipped += 1\n                    continue\n\n                keff = keff_data[pk][\"keff\"]\n                etas = [ind_asr[(ds, atk, j)] for j in jids]\n\n                # Adaptive panel ASR (majority vote on actual scores)\n                cs = {j: clean[ds][j] for j in jids}\n                ats = {j: attacked[ds][atk][j] for j in jids}\n                adaptive_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n                panel_keffs.append(keff)\n                panel_eta_maxs.append(max(etas))\n                panel_eta_all.append(etas)\n                panel_adaptive_asrs.append(adaptive_asr)\n                panel_jids_list.append(jids)\n\n            n_panels = len(panel_keffs)\n            logger.info(f\"  {n_panels} panels with data, {skipped} skipped\")\n\n            if n_panels < 10:\n                logger.warning(f\"  Too few panels ({n_panels}), skipping\")\n                condition_results[cond] = {\"n_panels\": n_panels, \"skipped\": True}\n                continue\n\n            keffs = np.array(panel_keffs)\n            eta_maxs = np.array(panel_eta_maxs)\n            eta_all = np.array(panel_eta_all)  # (n_panels, 3)\n            adaptive_asrs = np.array(panel_adaptive_asrs)\n\n            # ── Random-fault simulation ──\n            logger.info(f\"  Simulating {N_SIMS} RF runs...\")\n            rf_mean, rf_std = simulate_rf_vectorized(eta_all, rng)\n\n            # Analytical validation\n            analytical = np.array([analytical_rf_asr(e) for e in eta_all])\n            max_dev = np.max(np.abs(rf_mean - analytical))\n            logger.info(f\"  RF simulation done. Max deviation from analytical: {max_dev:.6f}\")\n\n            # ── Regressions ──\n            # Adaptive\n            if np.std(adaptive_asrs) < 1e-10:\n                logger.warning(f\"  Constant adaptive ASR, skipping regression\")\n                adaptive_ols = {\"keff_beta\": 0, \"keff_p\": 1, \"R2\": 0, \"note\": \"constant_asr\"}\n            else:\n                adaptive_ols = run_ols(adaptive_asrs, keffs, eta_maxs)\n\n            # Random-fault\n            if np.std(rf_mean) < 1e-10:\n                logger.warning(f\"  Constant RF ASR, skipping regression\")\n                rf_ols = {\"keff_beta\": 0, \"keff_p\": 1, \"R2\": 0, \"note\": \"constant_asr\"}\n            else:\n                rf_ols = run_ols(rf_mean, keffs, eta_maxs)\n\n            delta_R2 = rf_ols.get(\"R2\", 0) - adaptive_ols.get(\"R2\", 0)\n            keff_gains = (\n                rf_ols.get(\"keff_p\", 1) < 0.05\n                and rf_ols.get(\"keff_p\", 1) < adaptive_ols.get(\"keff_p\", 1)\n            )\n\n            # ── High-K_eff + Low-η_max benefit analysis ──\n            keff_q75 = np.percentile(keffs, 75)\n            eta_q25 = np.percentile(eta_maxs, 25)\n            hk_le_mask = (keffs >= keff_q75) & (eta_maxs <= eta_q25)\n            n_hk_le = int(hk_le_mask.sum())\n            hk_le_benefit = None\n            hk_le_pval = None\n            if n_hk_le >= 5:\n                diff = adaptive_asrs[hk_le_mask] - rf_mean[hk_le_mask]\n                hk_le_benefit = float(np.mean(diff))\n                if np.std(diff) > 1e-10:\n                    _, hk_le_pval = stats.ttest_1samp(diff, 0)\n                    hk_le_pval = float(hk_le_pval)\n\n            cond_res = {\n                \"n_panels\": n_panels,\n                \"skipped\": False,\n                \"adaptive\": adaptive_ols,\n                \"random_fault\": rf_ols,\n                \"delta_R2\": float(delta_R2),\n                \"keff_gains_significance\": bool(keff_gains),\n                \"rf_stats\": {\n                    \"mean\": float(np.mean(rf_mean)),\n                    \"std\": float(np.mean(rf_std)),\n                    \"max_analytical_deviation\": float(max_dev),\n                },\n                \"adaptive_stats\": {\n                    \"mean\": float(np.mean(adaptive_asrs)),\n                    \"std\": float(np.std(adaptive_asrs)),\n                },\n                \"high_keff_low_eta\": {\n                    \"n_panels\": n_hk_le,\n                    \"keff_threshold\": float(keff_q75),\n                    \"eta_threshold\": float(eta_q25),\n                    \"mean_benefit_adaptive_minus_rf\": hk_le_benefit,\n                    \"benefit_pval\": hk_le_pval,\n                },\n            }\n            condition_results[cond] = cond_res\n\n            logger.info(\n                f\"  Adaptive: K_eff β={adaptive_ols.get('keff_beta', 0):+.4f} \"\n                f\"p={adaptive_ols.get('keff_p', 1):.4f} R²={adaptive_ols.get('R2', 0):.4f}\"\n            )\n            logger.info(\n                f\"  RF:       K_eff β={rf_ols.get('keff_beta', 0):+.4f} \"\n                f\"p={rf_ols.get('keff_p', 1):.4f} R²={rf_ols.get('R2', 0):.4f}\"\n            )\n            logger.info(f\"  ΔR²={delta_R2:+.4f}  K_eff gains significance: {keff_gains}\")\n            if n_hk_le >= 5:\n                logger.info(\n                    f\"  High-K/Low-η panels ({n_hk_le}): \"\n                    f\"mean benefit={hk_le_benefit:+.4f} p={hk_le_pval}\"\n                )\n\n    # ── Summary ──\n    valid = {k: v for k, v in condition_results.items() if not v.get(\"skipped\")}\n    nv = len(valid)\n\n    if nv > 0:\n        n_adapt_sig = sum(\n            1 for v in valid.values()\n            if v[\"adaptive\"].get(\"keff_p\", 1) < 0.05 and v[\"adaptive\"].get(\"keff_beta\", 0) < 0\n        )\n        n_rf_sig = sum(\n            1 for v in valid.values()\n            if v[\"random_fault\"].get(\"keff_p\", 1) < 0.05 and v[\"random_fault\"].get(\"keff_beta\", 0) < 0\n        )\n        mean_dR2 = float(np.mean([v[\"delta_R2\"] for v in valid.values()]))\n        n_gains = sum(1 for v in valid.values() if v[\"keff_gains_significance\"])\n\n        # Build interpretation\n        parts = []\n        parts.append(\n            f\"K_eff significantly negative in {n_rf_sig}/{nv} conditions under RF \"\n            f\"vs {n_adapt_sig}/{nv} under adaptive.\"\n        )\n        if mean_dR2 > 0:\n            parts.append(\n                f\"RF model explains more variance (mean ΔR²={mean_dR2:+.3f}), \"\n                \"consistent with independent-error majority vote theory.\"\n            )\n        else:\n            parts.append(\n                f\"Adaptive model explains more variance (mean ΔR²={mean_dR2:+.3f}).\"\n            )\n        if n_gains > nv // 2:\n            parts.append(\n                f\"K_eff gains significance in {n_gains}/{nv} conditions under RF, \"\n                \"suggesting diversity benefit is undermined by adaptive attacks.\"\n            )\n        interpretation = \" \".join(parts)\n\n        summary = {\n            \"adaptive_keff_sig_negative\": f\"{n_adapt_sig}/{nv}\",\n            \"random_fault_keff_sig_negative\": f\"{n_rf_sig}/{nv}\",\n            \"mean_delta_R2\": mean_dR2,\n            \"keff_gains_significance_count\": f\"{n_gains}/{nv}\",\n            \"interpretation\": interpretation,\n        }\n    else:\n        summary = {\"note\": \"No valid conditions to summarize\"}\n\n    output = {\n        \"n_panels\": 455,\n        \"n_simulations\": N_SIMS,\n        \"n_samples_per_sim\": N_SAMPLES,\n        \"models\": ALL_MODELS,\n        \"conditions\": condition_results,\n        \"summary\": summary,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    out_path = OUTPUT_DIR / \"step5_random_fault_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    logger.info(f\"\\nResults saved: {out_path}\")\n\n    logger.info(\"\\n\" + \"=\" * 60)\n    logger.info(\"SUMMARY\")\n    logger.info(\"=\" * 60)\n    for k, v in summary.items():\n        if k != \"interpretation\":\n            logger.info(f\"  {k}: {v}\")\n    if \"interpretation\" in summary:\n        logger.info(f\"\\n  {summary['interpretation']}\")\n\n    # Comparison table\n    valid_keys = [k for k in condition_results if not condition_results[k].get(\"skipped\")]\n    logger.info(f\"\\n{'Condition':<35} {'Adap R²':>8} {'RF R²':>8} {'ΔR²':>7} {'Adap Kp':>8} {'RF Kp':>8} {'Gains':>5}\")\n    logger.info(\"-\" * 85)\n    for ck in valid_keys:\n        r = condition_results[ck]\n        a = r[\"adaptive\"]\n        rf = r[\"random_fault\"]\n        logger.info(\n            f\"  {ck:<33} {a.get('R2', 0):>8.4f} {rf.get('R2', 0):>8.4f} \"\n            f\"{r['delta_R2']:>+7.3f} {a.get('keff_p', 1):>8.4f} {rf.get('keff_p', 1):>8.4f} \"\n            f\"{'Y' if r['keff_gains_significance'] else 'N':>5}\"\n        )\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 524,
      "startLine": 1,
      "totalLines": 524
    }
  }
}
```

</details>

---

### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
Now I have all 4 scripts in full. Let me now create:

1. `src/unified_data_loader.py` - the unified data loader
2. Modified versions of all 4 scripts
3. Pipeline launcher script

Let me write all these files. I'll write them locally first, then scp to the server.

Let me analyze the exact changes needed for each script:

**Step 3 (MI Matrix):**
- Lines 21-41: Remove model lists and path constants → Import from loader
- Lines 44-91: Remove 3 loading functions → Use `load_all_scores()`


- Lines 177-179: Replace individual score loading calls → Use `load_all_scores()` instead
- Keep all MI-specific computation functions intact

**Confound Diagnosis:**
- Lines 23-57: Remove model lists, paths, and attack checkpoint constants → Import from loader
- Lines 60-186: Remove helper functions for inverting winners, computing ASR, loading individual ASR data, and merging ASR results → Use the unified loader instead

**Step 4 (Panel Regression):**
- Lines 399-405: Consolidate three separate data loading calls into `load_all_scores()`, `load_pairs()`, and ASR computation
- Lines 36-62: Remove model lists and paths → Import from loader
- Lines 82-170: Remove data loading and helper functions → Use loader functions
- Lines 370-372: Update function calls to use loader
- Keep all regression and analysis logic (majority voting, ASR computation, condition analysis, etc.)

**Step 5 (Random Fault):**
- Lines 33-62: Remove model lists and paths → Import from loader
- Lines 82-162: Remove data loading functions → Use loader
- Lines 278-280: Update function calls to use loader
- Keep all remaining analysis logic

Now I'm ready to build the unified loader. It'll export the constants (model lists, dataset names, attack types), directory paths, and the core data loading functions. Then I'll modify each script to import from this loader instead of defining everything locally.

Writing unified_data_loader.py...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "191d1b8e-f817-4b71-99ce-2259198675fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3s4R3tMjiMzbTVFQW1uiE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22559,
      "cache_read_input_tokens": 56931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22559
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

_source line 51_

All 4 scripts read完毕。关键发现：
- 4 个脚本都已硬编码 15 模型列表（一致）
- Step 4 和 Step 5 的 `load_all_scores()` 几乎完全相同
- Step 3 只加载 clean scores
- Confound 脚本有独立的 ASR 计算逻辑
- 大量重复代码：model lists、paths、`_invert_winners()`、数据加载函数

开始写统一加载器和修改脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "b05b38f9-017f-44c7-8b75-bf74b29c24ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3s4R3tMjiMzbTVFQW1uiE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22559,
      "cache_read_input_tokens": 56931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22559
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

_source line 52_

<details open><summary>🔧 Tool call — Write · `toolu_01VUbQPHWxo2ALc1vdP7tzbV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/unified_data_loader.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Unified data loader for 15-model cert_manip_resist_eval pipeline.\n\nHandles two data formats:\n  - Checkpoint files (local 6 models): nested {clean_scores: {ds: {model: [...]}}}\n  - Individual JSON files (API 9 models): flat {scores: [...], asr, accuracy, ...}\n\"\"\"\n\nimport json\nimport logging\nfrom pathlib import Path\n\nlogger = logging.getLogger(__name__)\n\n# ── Model lists ──────────────────────────────────────────────────────\nLOCAL_MODELS = [\n    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",\n    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",\n]\nAPI_MODELS = [\n    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",\n    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",\n    \"gpt-4o-mini\", \"claude-3-haiku\",\n]\nALL_MODELS = LOCAL_MODELS + API_MODELS\nDATASETS = [\"mmlu\", \"arc_challenge\"]\nATTACKS = [\n    \"prompt_injection\", \"sycophancy\", \"score_manipulation\",\n    \"verbosity_bias\", \"position_bias\", \"authority_bias\",\n]\n\n# ── Default paths ────────────────────────────────────────────────────\nRESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")\nPLAN001_DIR = RESULTS_DIR / \"plan001\"\nSCORES_DIR = PLAN001_DIR / \"individual_scores\"\nMI_PATH = PLAN001_DIR / \"mi_matrix\" / \"mi_matrix_15models.json\"\nCKPT_FILES = [\n    RESULTS_DIR / \"_taxonomy_checkpoint.json\",\n    RESULTS_DIR / \"_step2v3_checkpoint.json\",\n]\nOUTPUT_DIR = PLAN001_DIR / \"panel_regression\"\n\n\ndef _invert_winners(scores):\n    swap = {\"A\": \"B\", \"B\": \"A\", \"tie\": \"tie\"}\n    return [{**s, \"winner\": swap.get(s.get(\"winner\", \"tie\"), \"tie\")} for s in scores]\n\n\ndef load_all_scores(\n    checkpoint_files=None,\n    individual_dir=None,\n    datasets=None,\n    attacks=None,\n    all_models=None,\n):\n    \"\"\"Load sample-level clean + attacked scores for all 15 models.\n\n    Returns:\n        clean:    {ds: {model_id: [score_dicts]}}\n        attacked: {ds: {atk: {model_id: [score_dicts]}}}\n    \"\"\"\n    checkpoint_files = checkpoint_files or CKPT_FILES\n    individual_dir = Path(individual_dir or SCORES_DIR)\n    datasets = datasets or DATASETS\n    attacks = attacks or ATTACKS\n    all_models = all_models or ALL_MODELS\n\n    clean = {ds: {} for ds in datasets}\n    attacked = {ds: {a: {} for a in attacks} for ds in datasets}\n\n    for ckpt_path in checkpoint_files:\n        ckpt_path = Path(ckpt_path)\n        if not ckpt_path.exists():\n            logger.warning(f\"Checkpoint not found: {ckpt_path}\")\n            continue\n        logger.info(f\"Loading checkpoint: {ckpt_path.name}\")\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        for ds in datasets:\n            for mid, scores in data.get(\"clean_scores\", {}).get(ds, {}).items():\n                if mid not in clean[ds]:\n                    clean[ds][mid] = scores\n            for atk in attacks:\n                for mid, scores in (\n                    data.get(\"attacked_scores\", {}).get(ds, {}).get(atk, {}).items()\n                ):\n                    if mid not in attacked[ds][atk]:\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    if individual_dir.exists():\n        logger.info(f\"Loading individual scores from {individual_dir}\")\n        for mid in all_models:\n            for ds in datasets:\n                fp = individual_dir / f\"{mid}__{ds}__clean.json\"\n                if fp.exists() and mid not in clean[ds]:\n                    with open(fp) as f:\n                        clean[ds][mid] = json.load(f).get(\"scores\", [])\n                for atk in attacks:\n                    fp = individual_dir / f\"{mid}__{ds}__{atk}.json\"\n                    if fp.exists() and mid not in attacked[ds][atk]:\n                        with open(fp) as f:\n                            scores = json.load(f).get(\"scores\", [])\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    for ds in datasets:\n        nc = len(clean[ds])\n        logger.info(f\"  {ds} clean: {nc}/{len(all_models)}\")\n        for atk in attacks:\n            na = len(attacked[ds][atk])\n            if na > 0:\n                logger.info(f\"  {ds} {atk}: {na}/{len(all_models)}\")\n\n    return clean, attacked\n\n\ndef load_pairs(checkpoint_files=None, datasets=None):\n    \"\"\"Load evaluation pairs from checkpoint files.\n\n    Returns: {ds: [pair_dicts]} with up to 300 pairs per dataset.\n    \"\"\"\n    checkpoint_files = checkpoint_files or CKPT_FILES\n    datasets = datasets or DATASETS\n\n    for ckpt_path in checkpoint_files:\n        ckpt_path = Path(ckpt_path)\n        if not ckpt_path.exists():\n            continue\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        if \"pairs\" not in data:\n            continue\n        pairs = {}\n        for ds in datasets:\n            if ds in data[\"pairs\"]:\n                pairs[ds] = data[\"pairs\"][ds][:300]\n                logger.info(f\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\")\n        if pairs:\n            return pairs\n    raise FileNotFoundError(\"No pairs found in any checkpoint file\")\n\n\ndef load_mi_data(mi_path=None):\n    \"\"\"Load MI matrix from Step 3 output.\"\"\"\n    mi_path = Path(mi_path or MI_PATH)\n    if not mi_path.exists():\n        raise FileNotFoundError(\n            f\"MI matrix not found: {mi_path}. Run Step 3 first.\"\n        )\n    with open(mi_path) as f:\n        data = json.load(f)\n    logger.info(f\"Loaded MI matrix: {len(data['models'])} models\")\n    return data\n\n\ndef load_api_asr(individual_dir=None, datasets=None, attacks=None, api_models=None):\n    \"\"\"Load pre-computed ASR for API models from individual score files.\n\n    Returns: {ds: {atk: {model_id: asr}}}\n    \"\"\"\n    individual_dir = Path(individual_dir or SCORES_DIR)\n    datasets = datasets or DATASETS\n    attacks = attacks or ATTACKS\n    api_models = api_models or API_MODELS\n\n    asr_data = {}\n    for model_id in api_models:\n        for ds in datasets:\n            if ds not in asr_data:\n                asr_data[ds] = {}\n            clean_path = individual_dir / f\"{model_id}__{ds}__clean.json\"\n            if not clean_path.exists():\n                continue\n            for atk in attacks:\n                if atk not in asr_data[ds]:\n                    asr_data[ds][atk] = {}\n                atk_path = individual_dir / f\"{model_id}__{ds}__{atk}.json\"\n                if not atk_path.exists():\n                    continue\n                with open(atk_path) as f:\n                    atk_data = json.load(f)\n                asr = atk_data.get(\"asr\")\n                if asr is not None:\n                    asr_data[ds][atk][model_id] = asr\n    return asr_data\n\n\ndef validate_coverage(clean, attacked, datasets=None, attacks=None,\n                      all_models=None, expected_samples=300):\n    \"\"\"Check that all models have expected number of samples. Returns list of issues.\"\"\"\n    datasets = datasets or DATASETS\n    attacks = attacks or ATTACKS\n    all_models = all_models or ALL_MODELS\n\n    issues = []\n    for ds in datasets:\n        for mid in all_models:\n            if mid not in clean[ds]:\n                issues.append(f\"MISSING clean: {ds}/{mid}\")\n            elif len(clean[ds][mid]) != expected_samples:\n                issues.append(\n                    f\"COUNT clean: {ds}/{mid} has {len(clean[ds][mid])}, \"\n                    f\"expected {expected_samples}\"\n                )\n            for atk in attacks:\n                if mid not in attacked[ds][atk]:\n                    issues.append(f\"MISSING attacked: {ds}/{atk}/{mid}\")\n                elif len(attacked[ds][atk][mid]) != expected_samples:\n                    issues.append(\n                        f\"COUNT attacked: {ds}/{atk}/{mid} has \"\n                        f\"{len(attacked[ds][atk][mid])}, expected {expected_samples}\"\n                    )\n    if issues:\n        logger.warning(f\"Validation: {len(issues)} issues\")\n        for i in issues[:20]:\n            logger.warning(f\"  {i}\")\n        if len(issues) > 20:\n            logger.warning(f\"  ... and {len(issues) - 20} more\")\n    else:\n        logger.info(\n            f\"Validation passed: {len(all_models)} models x \"\n            f\"{len(datasets)} datasets x {len(attacks)+1} conditions\"\n        )\n    return issues\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "03ab709a-d6ba-4788-9c42-8c7b9caf6a2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3s4R3tMjiMzbTVFQW1uiE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22559,
      "cache_read_input_tokens": 56931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22559
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

_source line 53 · 2026-05-22T14:59:30.764Z_

<details><summary>↩ Tool result · `toolu_01VUbQPHWxo2ALc1vdP7tzbV`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/unified_data_loader.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "65e58fe8-806b-4421-b40c-bd70bc98c84d",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/unified_data_loader.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Unified data loader for 15-model cert_manip_resist_eval pipeline.\n\nHandles two data formats:\n  - Checkpoint files (local 6 models): nested {clean_scores: {ds: {model: [...]}}}\n  - Individual JSON files (API 9 models): flat {scores: [...], asr, accuracy, ...}\n\"\"\"\n\nimport json\nimport logging\nfrom pathlib import Path\n\nlogger = logging.getLogger(__name__)\n\n# ── Model lists ──────────────────────────────────────────────────────\nLOCAL_MODELS = [\n    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",\n    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",\n]\nAPI_MODELS = [\n    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",\n    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",\n    \"gpt-4o-mini\", \"claude-3-haiku\",\n]\nALL_MODELS = LOCAL_MODELS + API_MODELS\nDATASETS = [\"mmlu\", \"arc_challenge\"]\nATTACKS = [\n    \"prompt_injection\", \"sycophancy\", \"score_manipulation\",\n    \"verbosity_bias\", \"position_bias\", \"authority_bias\",\n]\n\n# ── Default paths ────────────────────────────────────────────────────\nRESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")\nPLAN001_DIR = RESULTS_DIR / \"plan001\"\nSCORES_DIR = PLAN001_DIR / \"individual_scores\"\nMI_PATH = PLAN001_DIR / \"mi_matrix\" / \"mi_matrix_15models.json\"\nCKPT_FILES = [\n    RESULTS_DIR / \"_taxonomy_checkpoint.json\",\n    RESULTS_DIR / \"_step2v3_checkpoint.json\",\n]\nOUTPUT_DIR = PLAN001_DIR / \"panel_regression\"\n\n\ndef _invert_winners(scores):\n    swap = {\"A\": \"B\", \"B\": \"A\", \"tie\": \"tie\"}\n    return [{**s, \"winner\": swap.get(s.get(\"winner\", \"tie\"), \"tie\")} for s in scores]\n\n\ndef load_all_scores(\n    checkpoint_files=None,\n    individual_dir=None,\n    datasets=None,\n    attacks=None,\n    all_models=None,\n):\n    \"\"\"Load sample-level clean + attacked scores for all 15 models.\n\n    Returns:\n        clean:    {ds: {model_id: [score_dicts]}}\n        attacked: {ds: {atk: {model_id: [score_dicts]}}}\n    \"\"\"\n    checkpoint_files = checkpoint_files or CKPT_FILES\n    individual_dir = Path(individual_dir or SCORES_DIR)\n    datasets = datasets or DATASETS\n    attacks = attacks or ATTACKS\n    all_models = all_models or ALL_MODELS\n\n    clean = {ds: {} for ds in datasets}\n    attacked = {ds: {a: {} for a in attacks} for ds in datasets}\n\n    for ckpt_path in checkpoint_files:\n        ckpt_path = Path(ckpt_path)\n        if not ckpt_path.exists():\n            logger.warning(f\"Checkpoint not found: {ckpt_path}\")\n            continue\n        logger.info(f\"Loading checkpoint: {ckpt_path.name}\")\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        for ds in datasets:\n            for mid, scores in data.get(\"clean_scores\", {}).get(ds, {}).items():\n                if mid not in clean[ds]:\n                    clean[ds][mid] = scores\n            for atk in attacks:\n                for mid, scores in (\n                    data.get(\"attacked_scores\", {}).get(ds, {}).get(atk, {}).items()\n                ):\n                    if mid not in attacked[ds][atk]:\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    if individual_dir.exists():\n        logger.info(f\"Loading individual scores from {individual_dir}\")\n        for mid in all_models:\n            for ds in datasets:\n                fp = individual_dir / f\"{mid}__{ds}__clean.json\"\n                if fp.exists() and mid not in clean[ds]:\n                    with open(fp) as f:\n                        clean[ds][mid] = json.load(f).get(\"scores\", [])\n                for atk in attacks:\n                    fp = individual_dir / f\"{mid}__{ds}__{atk}.json\"\n                    if fp.exists() and mid not in attacked[ds][atk]:\n                        with open(fp) as f:\n                            scores = json.load(f).get(\"scores\", [])\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    for ds in datasets:\n        nc = len(clean[ds])\n        logger.info(f\"  {ds} clean: {nc}/{len(all_models)}\")\n        for atk in attacks:\n            na = len(attacked[ds][atk])\n            if na > 0:\n                logger.info(f\"  {ds} {atk}: {na}/{len(all_models)}\")\n\n    return clean, attacked\n\n\ndef load_pairs(checkpoint_files=None, datasets=None):\n    \"\"\"Load evaluation pairs from checkpoint files.\n\n    Returns: {ds: [pair_dicts]} with up to 300 pairs per dataset.\n    \"\"\"\n    checkpoint_files = checkpoint_files or CKPT_FILES\n    datasets = datasets or DATASETS\n\n    for ckpt_path in checkpoint_files:\n        ckpt_path = Path(ckpt_path)\n        if not ckpt_path.exists():\n            continue\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        if \"pairs\" not in data:\n            continue\n        pairs = {}\n        for ds in datasets:\n            if ds in data[\"pairs\"]:\n                pairs[ds] = data[\"pairs\"][ds][:300]\n                logger.info(f\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\")\n        if pairs:\n            return pairs\n    raise FileNotFoundError(\"No pairs found in any checkpoint file\")\n\n\ndef load_mi_data(mi_path=None):\n    \"\"\"Load MI matrix from Step 3 output.\"\"\"\n    mi_path = Path(mi_path or MI_PATH)\n    if not mi_path.exists():\n        raise FileNotFoundError(\n            f\"MI matrix not found: {mi_path}. Run Step 3 first.\"\n        )\n    with open(mi_path) as f:\n        data = json.load(f)\n    logger.info(f\"Loaded MI matrix: {len(data['models'])} models\")\n    return data\n\n\ndef load_api_asr(individual_dir=None, datasets=None, attacks=None, api_models=None):\n    \"\"\"Load pre-computed ASR for API models from individual score files.\n\n    Returns: {ds: {atk: {model_id: asr}}}\n    \"\"\"\n    individual_dir = Path(individual_dir or SCORES_DIR)\n    datasets = datasets or DATASETS\n    attacks = attacks or ATTACKS\n    api_models = api_models or API_MODELS\n\n    asr_data = {}\n    for model_id in api_models:\n        for ds in datasets:\n            if ds not in asr_data:\n                asr_data[ds] = {}\n            clean_path = individual_dir / f\"{model_id}__{ds}__clean.json\"\n            if not clean_path.exists():\n                continue\n            for atk in attacks:\n                if atk not in asr_data[ds]:\n                    asr_data[ds][atk] = {}\n                atk_path = individual_dir / f\"{model_id}__{ds}__{atk}.json\"\n                if not atk_path.exists():\n                    continue\n                with open(atk_path) as f:\n                    atk_data = json.load(f)\n                asr = atk_data.get(\"asr\")\n                if asr is not None:\n                    asr_data[ds][atk][model_id] = asr\n    return asr_data\n\n\ndef validate_coverage(clean, attacked, datasets=None, attacks=None,\n                      all_models=None, expected_samples=300):\n    \"\"\"Check that all models have expected number of samples. Returns list of issues.\"\"\"\n    datasets = datasets or DATASETS\n    attacks = attacks or ATTACKS\n    all_models = all_models or ALL_MODELS\n\n    issues = []\n    for ds in datasets:\n        for mid in all_models:\n            if mid not in clean[ds]:\n                issues.append(f\"MISSING clean: {ds}/{mid}\")\n            elif len(clean[ds][mid]) != expected_samples:\n                issues.append(\n                    f\"COUNT clean: {ds}/{mid} has {len(clean[ds][mid])}, \"\n                    f\"expected {expected_samples}\"\n                )\n            for atk in attacks:\n                if mid not in attacked[ds][atk]:\n                    issues.append(f\"MISSING attacked: {ds}/{atk}/{mid}\")\n                elif len(attacked[ds][atk][mid]) != expected_samples:\n                    issues.append(\n                        f\"COUNT attacked: {ds}/{atk}/{mid} has \"\n                        f\"{len(attacked[ds][atk][mid])}, expected {expected_samples}\"\n                    )\n    if issues:\n        logger.warning(f\"Validation: {len(issues)} issues\")\n        for i in issues[:20]:\n            logger.warning(f\"  {i}\")\n        if len(issues) > 20:\n            logger.warning(f\"  ... and {len(issues) - 20} more\")\n    else:\n        logger.info(\n            f\"Validation passed: {len(all_models)} models x \"\n            f\"{len(datasets)} datasets x {len(attacks)+1} conditions\"\n        )\n    return issues\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 54_

Now writing the modified scripts. Starting with Step 3 and Confound in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "e33fbe72-8eba-4a49-b12b-e4773953b843",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5P8r6LkdeLYe64yWQGb9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3655,
      "cache_read_input_tokens": 79490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3655
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

_source line 55_

<details open><summary>🔧 Tool call — Write · `toolu_0159UunGPGsYGWXvmNDpr81S`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 3: Compute 15-model pairwise MI matrix and K_eff for all C(15,3) panels.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.metrics import mutual_info_score\n\nfrom src.utils import setup_logging\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, PLAN001_DIR, load_all_scores,\n)\n\nlogger = setup_logging(\"plan001_step3_mi\")\n\nMI_DIR = PLAN001_DIR / \"mi_matrix\"\n\n\ndef extract_winner_vector(score_list):\n    winners = []\n    for s in score_list:\n        w = s.get(\"winner\", \"tie\") if isinstance(s, dict) else \"tie\"\n        winners.append(w)\n    return winners\n\n\ndef compute_pairwise_mi(winners_i, winners_j):\n    n = min(len(winners_i), len(winners_j))\n    if n == 0:\n        return 0.0\n    return mutual_info_score(winners_i[:n], winners_j[:n])\n\n\ndef build_mi_matrix(clean_scores, dataset):\n    ds_scores = clean_scores.get(dataset, {})\n    n_models = len(ALL_MODELS)\n    mi_mat = np.zeros((n_models, n_models))\n\n    winner_vectors = {}\n    for i, model_id in enumerate(ALL_MODELS):\n        if model_id in ds_scores:\n            winner_vectors[i] = extract_winner_vector(ds_scores[model_id])\n        else:\n            logger.warning(f\"No clean scores for {model_id} on {dataset}\")\n\n    for i in range(n_models):\n        for j in range(i + 1, n_models):\n            if i in winner_vectors and j in winner_vectors:\n                mi = compute_pairwise_mi(winner_vectors[i], winner_vectors[j])\n                mi_mat[i, j] = mi\n                mi_mat[j, i] = mi\n\n    return mi_mat\n\n\ndef mi_based_keff(mi_matrix, model_indices):\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx, j_idx])\n        keff += term\n    return keff / K\n\n\ndef compute_all_panel_keffs(mi_matrix, dataset):\n    n_models = len(ALL_MODELS)\n    idx_to_model = {i: m for i, m in enumerate(ALL_MODELS)}\n    panels = {}\n\n    for combo in itertools.combinations(range(n_models), 3):\n        model_ids = [idx_to_model[i] for i in combo]\n        panel_key = \"|\".join(model_ids)\n        keff = mi_based_keff(mi_matrix, list(combo))\n\n        mi_pairs = {}\n        for a, b in itertools.combinations(combo, 2):\n            pair_key = f\"{idx_to_model[a]}|{idx_to_model[b]}\"\n            mi_pairs[pair_key] = float(mi_matrix[a, b])\n\n        panels[panel_key] = {\n            \"models\": model_ids,\n            \"keff\": float(keff),\n            \"mi_pairs\": mi_pairs,\n        }\n\n    return panels\n\n\ndef main():\n    logger.info(\"=== Plan 001 Step 3: MI Matrix Computation ===\")\n\n    clean_scores, _ = load_all_scores()\n\n    for ds in DATASETS:\n        available = list(clean_scores.get(ds, {}).keys())\n        missing = [m for m in ALL_MODELS if m not in available]\n        logger.info(f\"  {ds}: {len(available)}/{len(ALL_MODELS)} models available\")\n        if missing:\n            logger.warning(f\"  {ds}: missing models: {missing}\")\n\n    available_count = sum(\n        1 for ds in DATASETS\n        for m in ALL_MODELS\n        if m in clean_scores.get(ds, {})\n    )\n    total_needed = len(DATASETS) * len(ALL_MODELS)\n    if available_count < total_needed:\n        logger.warning(\n            f\"Only {available_count}/{total_needed} model*dataset combos available. \"\n            f\"MI matrix will have zeros for missing pairs.\"\n        )\n\n    mi_matrices = {}\n    keff_per_panel = {}\n\n    for ds in DATASETS:\n        logger.info(f\"\\n--- Computing MI matrix for {ds} ---\")\n        mi_mat = build_mi_matrix(clean_scores, ds)\n        mi_matrices[ds] = mi_mat.tolist()\n\n        nonzero = np.count_nonzero(mi_mat)\n        max_possible = len(ALL_MODELS) * (len(ALL_MODELS) - 1)\n        logger.info(f\"  MI matrix: {nonzero}/{max_possible} non-zero entries\")\n        if nonzero > 0:\n            upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\n            upper_nz = upper[upper > 0]\n            if len(upper_nz) > 0:\n                logger.info(\n                    f\"  MI range: [{upper_nz.min():.4f}, {upper_nz.max():.4f}], \"\n                    f\"mean={upper_nz.mean():.4f}\"\n                )\n\n        logger.info(f\"  Computing K_eff for all C(15,3)=455 panels on {ds}...\")\n        panels = compute_all_panel_keffs(mi_mat, ds)\n        keff_per_panel[ds] = panels\n\n        keff_values = [p[\"keff\"] for p in panels.values()]\n        logger.info(\n            f\"  K_eff range: [{min(keff_values):.3f}, {max(keff_values):.3f}], \"\n            f\"mean={np.mean(keff_values):.3f}\"\n        )\n\n    MI_DIR.mkdir(parents=True, exist_ok=True)\n    output = {\n        \"models\": ALL_MODELS,\n        \"mi_matrix\": mi_matrices,\n        \"keff_per_panel\": keff_per_panel,\n    }\n    output_path = MI_DIR / \"mi_matrix_15models.json\"\n    with open(output_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n    logger.info(f\"\\nSaved MI matrix to {output_path}\")\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"MI MATRIX SUMMARY\")\n    print(\"=\" * 70)\n    for ds in DATASETS:\n        mi_mat = np.array(mi_matrices[ds])\n        upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\n        n_computed = np.count_nonzero(upper)\n        print(f\"\\n{ds}:\")\n        print(f\"  Pairwise MI computed: {n_computed}/105\")\n        if n_computed > 0:\n            nz = upper[upper > 0]\n            print(f\"  MI range: [{nz.min():.4f}, {nz.max():.4f}]\")\n            print(f\"  MI mean:  {nz.mean():.4f}\")\n        keffs = [p[\"keff\"] for p in keff_per_panel[ds].values()]\n        print(f\"  K_eff (455 panels): [{min(keffs):.3f}, {max(keffs):.3f}], mean={np.mean(keffs):.3f}\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "c7b20765-45c3-4902-b7aa-2b57302c20d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5P8r6LkdeLYe64yWQGb9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3655,
      "cache_read_input_tokens": 79490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3655
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

_source line 56 · 2026-05-22T14:59:59.908Z_

<details><summary>↩ Tool result · `toolu_0159UunGPGsYGWXvmNDpr81S`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "3c4ecb4c-7ecd-4d71-9267-13508bd1b61c",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 3: Compute 15-model pairwise MI matrix and K_eff for all C(15,3) panels.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\nfrom sklearn.metrics import mutual_info_score\n\nfrom src.utils import setup_logging\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, PLAN001_DIR, load_all_scores,\n)\n\nlogger = setup_logging(\"plan001_step3_mi\")\n\nMI_DIR = PLAN001_DIR / \"mi_matrix\"\n\n\ndef extract_winner_vector(score_list):\n    winners = []\n    for s in score_list:\n        w = s.get(\"winner\", \"tie\") if isinstance(s, dict) else \"tie\"\n        winners.append(w)\n    return winners\n\n\ndef compute_pairwise_mi(winners_i, winners_j):\n    n = min(len(winners_i), len(winners_j))\n    if n == 0:\n        return 0.0\n    return mutual_info_score(winners_i[:n], winners_j[:n])\n\n\ndef build_mi_matrix(clean_scores, dataset):\n    ds_scores = clean_scores.get(dataset, {})\n    n_models = len(ALL_MODELS)\n    mi_mat = np.zeros((n_models, n_models))\n\n    winner_vectors = {}\n    for i, model_id in enumerate(ALL_MODELS):\n        if model_id in ds_scores:\n            winner_vectors[i] = extract_winner_vector(ds_scores[model_id])\n        else:\n            logger.warning(f\"No clean scores for {model_id} on {dataset}\")\n\n    for i in range(n_models):\n        for j in range(i + 1, n_models):\n            if i in winner_vectors and j in winner_vectors:\n                mi = compute_pairwise_mi(winner_vectors[i], winner_vectors[j])\n                mi_mat[i, j] = mi\n                mi_mat[j, i] = mi\n\n    return mi_mat\n\n\ndef mi_based_keff(mi_matrix, model_indices):\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx, j_idx])\n        keff += term\n    return keff / K\n\n\ndef compute_all_panel_keffs(mi_matrix, dataset):\n    n_models = len(ALL_MODELS)\n    idx_to_model = {i: m for i, m in enumerate(ALL_MODELS)}\n    panels = {}\n\n    for combo in itertools.combinations(range(n_models), 3):\n        model_ids = [idx_to_model[i] for i in combo]\n        panel_key = \"|\".join(model_ids)\n        keff = mi_based_keff(mi_matrix, list(combo))\n\n        mi_pairs = {}\n        for a, b in itertools.combinations(combo, 2):\n            pair_key = f\"{idx_to_model[a]}|{idx_to_model[b]}\"\n            mi_pairs[pair_key] = float(mi_matrix[a, b])\n\n        panels[panel_key] = {\n            \"models\": model_ids,\n            \"keff\": float(keff),\n            \"mi_pairs\": mi_pairs,\n        }\n\n    return panels\n\n\ndef main():\n    logger.info(\"=== Plan 001 Step 3: MI Matrix Computation ===\")\n\n    clean_scores, _ = load_all_scores()\n\n    for ds in DATASETS:\n        available = list(clean_scores.get(ds, {}).keys())\n        missing = [m for m in ALL_MODELS if m not in available]\n        logger.info(f\"  {ds}: {len(available)}/{len(ALL_MODELS)} models available\")\n        if missing:\n            logger.warning(f\"  {ds}: missing models: {missing}\")\n\n    available_count = sum(\n        1 for ds in DATASETS\n        for m in ALL_MODELS\n        if m in clean_scores.get(ds, {})\n    )\n    total_needed = len(DATASETS) * len(ALL_MODELS)\n    if available_count < total_needed:\n        logger.warning(\n            f\"Only {available_count}/{total_needed} model*dataset combos available. \"\n            f\"MI matrix will have zeros for missing pairs.\"\n        )\n\n    mi_matrices = {}\n    keff_per_panel = {}\n\n    for ds in DATASETS:\n        logger.info(f\"\\n--- Computing MI matrix for {ds} ---\")\n        mi_mat = build_mi_matrix(clean_scores, ds)\n        mi_matrices[ds] = mi_mat.tolist()\n\n        nonzero = np.count_nonzero(mi_mat)\n        max_possible = len(ALL_MODELS) * (len(ALL_MODELS) - 1)\n        logger.info(f\"  MI matrix: {nonzero}/{max_possible} non-zero entries\")\n        if nonzero > 0:\n            upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\n            upper_nz = upper[upper > 0]\n            if len(upper_nz) > 0:\n                logger.info(\n                    f\"  MI range: [{upper_nz.min():.4f}, {upper_nz.max():.4f}], \"\n                    f\"mean={upper_nz.mean():.4f}\"\n                )\n\n        logger.info(f\"  Computing K_eff for all C(15,3)=455 panels on {ds}...\")\n        panels = compute_all_panel_keffs(mi_mat, ds)\n        keff_per_panel[ds] = panels\n\n        keff_values = [p[\"keff\"] for p in panels.values()]\n        logger.info(\n            f\"  K_eff range: [{min(keff_values):.3f}, {max(keff_values):.3f}], \"\n            f\"mean={np.mean(keff_values):.3f}\"\n        )\n\n    MI_DIR.mkdir(parents=True, exist_ok=True)\n    output = {\n        \"models\": ALL_MODELS,\n        \"mi_matrix\": mi_matrices,\n        \"keff_per_panel\": keff_per_panel,\n    }\n    output_path = MI_DIR / \"mi_matrix_15models.json\"\n    with open(output_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n    logger.info(f\"\\nSaved MI matrix to {output_path}\")\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"MI MATRIX SUMMARY\")\n    print(\"=\" * 70)\n    for ds in DATASETS:\n        mi_mat = np.array(mi_matrices[ds])\n        upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\n        n_computed = np.count_nonzero(upper)\n        print(f\"\\n{ds}:\")\n        print(f\"  Pairwise MI computed: {n_computed}/105\")\n        if n_computed > 0:\n            nz = upper[upper > 0]\n            print(f\"  MI range: [{nz.min():.4f}, {nz.max():.4f}]\")\n            print(f\"  MI mean:  {nz.mean():.4f}\")\n        keffs = [p[\"keff\"] for p in keff_per_panel[ds].values()]\n        print(f\"  K_eff (455 panels): [{min(keffs):.3f}, {max(keffs):.3f}], mean={np.mean(keffs):.3f}\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 88,
        "newStart": 11,
        "newLines": 19,
        "lines": [
          " import itertools",
          " import numpy as np",
          " from pathlib import Path",
          "-from collections import Counter",
          " from sklearn.metrics import mutual_info_score",
          " ",
          " from src.utils import setup_logging",
          "+from src.unified_data_loader import (",
          "+    ALL_MODELS, DATASETS, PLAN001_DIR, load_all_scores,",
          "+)",
          " ",
          " logger = setup_logging(\"plan001_step3_mi\")",
          " ",
          "-# ── Model lists ──────────────────────────────────────────────────────",
          "-LOCAL_MODELS = [",
          "-    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",",
          "-    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",",
          "-]",
          "-API_MODELS = [",
          "-    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",",
          "-    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",",
          "-    \"gpt-4o-mini\", \"claude-3-haiku\",",
          "-]",
          "-ALL_MODELS = LOCAL_MODELS + API_MODELS",
          "-DATASETS = [\"mmlu\", \"arc_challenge\"]",
          "-",
          "-# ── Paths ────────────────────────────────────────────────────────────",
          "-RESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")",
          "-PLAN001_DIR = RESULTS_DIR / \"plan001\"",
          "-SCORES_DIR = PLAN001_DIR / \"individual_scores\"",
          " MI_DIR = PLAN001_DIR / \"mi_matrix\"",
          " ",
          "-STEP2V3_CKPT = RESULTS_DIR / \"_step2v3_checkpoint.json\"",
          "-TAXONOMY_CKPT = RESULTS_DIR / \"_taxonomy_checkpoint.json\"",
          " ",
          "-",
          "-def load_local_clean_scores():",
          "-    \"\"\"Load clean scores for 6 local models from checkpoint files.\"\"\"",
          "-    scores = {}",
          "-    for ckpt_path in [STEP2V3_CKPT, TAXONOMY_CKPT]:",
          "-        if not ckpt_path.exists():",
          "-            logger.warning(f\"Checkpoint not found: {ckpt_path}\")",
          "-            continue",
          "-        with open(ckpt_path) as f:",
          "-            data = json.load(f)",
          "-        cs = data.get(\"clean_scores\", {})",
          "-        for ds in DATASETS:",
          "-            if ds not in cs:",
          "-                continue",
          "-            if ds not in scores:",
          "-                scores[ds] = {}",
          "-            for model_id, model_scores in cs[ds].items():",
          "-                if model_id in LOCAL_MODELS and model_id not in scores[ds]:",
          "-                    scores[ds][model_id] = model_scores",
          "-    return scores",
          "-",
          "-",
          "-def load_api_clean_scores():",
          "-    \"\"\"Load clean scores for 9 API models from individual score files.\"\"\"",
          "-    scores = {}",
          "-    for model_id in API_MODELS:",
          "-        for ds in DATASETS:",
          "-            fname = f\"{model_id}__{ds}__clean.json\"",
          "-            fpath = SCORES_DIR / fname",
          "-            if not fpath.exists():",
          "-                logger.warning(f\"API score file not found: {fpath}\")",
          "-                continue",
          "-            with open(fpath) as f:",
          "-                data = json.load(f)",
          "-            if ds not in scores:",
          "-                scores[ds] = {}",
          "-            scores[ds][model_id] = data.get(\"scores\", [])",
          "-    return scores",
          "-",
          "-",
          "-def merge_clean_scores(local_scores, api_scores):",
          "-    \"\"\"Merge local and API clean scores into unified dict.\"\"\"",
          "-    merged = {}",
          "-    for ds in DATASETS:",
          "-        merged[ds] = {}",
          "-        for src in [local_scores, api_scores]:",
          "-            if ds in src:",
          "-                merged[ds].update(src[ds])",
          "-    return merged",
          "-",
          "-",
          " def extract_winner_vector(score_list):",
          "-    \"\"\"Extract winner labels from score list, normalizing to A/B/C/tie.\"\"\"",
          "     winners = []",
          "     for s in score_list:",
          "         w = s.get(\"winner\", \"tie\") if isinstance(s, dict) else \"tie\""
        ]
      },
      {
        "oldStart": 101,
        "oldLines": 7,
        "newStart": 32,
        "newLines": 6,
        "lines": [
          " ",
          " ",
          " def compute_pairwise_mi(winners_i, winners_j):",
          "-    \"\"\"Compute mutual information between two winner vectors.\"\"\"",
          "     n = min(len(winners_i), len(winners_j))",
          "     if n == 0:",
          "         return 0.0"
        ]
      },
      {
        "oldStart": 109,
        "oldLines": 7,
        "newStart": 39,
        "newLines": 6,
        "lines": [
          " ",
          " ",
          " def build_mi_matrix(clean_scores, dataset):",
          "-    \"\"\"Build 15x15 MI matrix for a dataset.\"\"\"",
          "     ds_scores = clean_scores.get(dataset, {})",
          "     n_models = len(ALL_MODELS)",
          "     mi_mat = np.zeros((n_models, n_models))"
        ]
      },
      {
        "oldStart": 132,
        "oldLines": 7,
        "newStart": 61,
        "newLines": 6,
        "lines": [
          " ",
          " ",
          " def mi_based_keff(mi_matrix, model_indices):",
          "-    \"\"\"K_eff = (1/K) * sum_i [1 + sum_{j!=i} exp(-2 * MI_ij)]\"\"\"",
          "     K = len(model_indices)",
          "     if K <= 1:",
          "         return 1.0"
        ]
      },
      {
        "oldStart": 147,
        "oldLines": 7,
        "newStart": 75,
        "newLines": 6,
        "lines": [
          " ",
          " ",
          " def compute_all_panel_keffs(mi_matrix, dataset):",
          "-    \"\"\"Compute K_eff for all C(15,3)=455 panels.\"\"\"",
          "     n_models = len(ALL_MODELS)",
          "     idx_to_model = {i: m for i, m in enumerate(ALL_MODELS)}",
          "     panels = {}"
        ]
      },
      {
        "oldStart": 174,
        "oldLines": 9,
        "newStart": 101,
        "newLines": 7,
        "lines": [
          " def main():",
          "     logger.info(\"=== Plan 001 Step 3: MI Matrix Computation ===\")",
          " ",
          "-    local_scores = load_local_clean_scores()",
          "-    api_scores = load_api_clean_scores()",
          "-    clean_scores = merge_clean_scores(local_scores, api_scores)",
          "+    clean_scores, _ = load_all_scores()",
          " ",
          "     for ds in DATASETS:",
          "         available = list(clean_scores.get(ds, {}).keys())"
        ]
      },
      {
        "oldStart": 193,
        "oldLines": 7,
        "newStart": 118,
        "newLines": 7,
        "lines": [
          "     total_needed = len(DATASETS) * len(ALL_MODELS)",
          "     if available_count < total_needed:",
          "         logger.warning(",
          "-            f\"Only {available_count}/{total_needed} model×dataset combos available. \"",
          "+            f\"Only {available_count}/{total_needed} model*dataset combos available. \"",
          "             f\"MI matrix will have zeros for missing pairs.\"",
          "         )",
          " "
        ]
      }
    ],
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 3: Compute 15-model pairwise MI matrix and K_eff for all C(15,3) panels.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\nfrom collections import Counter\nfrom sklearn.metrics import mutual_info_score\n\nfrom src.utils import setup_logging\n\nlogger = setup_logging(\"plan001_step3_mi\")\n\n# ── Model lists ──────────────────────────────────────────────────────\nLOCAL_MODELS = [\n    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",\n    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",\n]\nAPI_MODELS = [\n    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",\n    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",\n    \"gpt-4o-mini\", \"claude-3-haiku\",\n]\nALL_MODELS = LOCAL_MODELS + API_MODELS\nDATASETS = [\"mmlu\", \"arc_challenge\"]\n\n# ── Paths ────────────────────────────────────────────────────────────\nRESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")\nPLAN001_DIR = RESULTS_DIR / \"plan001\"\nSCORES_DIR = PLAN001_DIR / \"individual_scores\"\nMI_DIR = PLAN001_DIR / \"mi_matrix\"\n\nSTEP2V3_CKPT = RESULTS_DIR / \"_step2v3_checkpoint.json\"\nTAXONOMY_CKPT = RESULTS_DIR / \"_taxonomy_checkpoint.json\"\n\n\ndef load_local_clean_scores():\n    \"\"\"Load clean scores for 6 local models from checkpoint files.\"\"\"\n    scores = {}\n    for ckpt_path in [STEP2V3_CKPT, TAXONOMY_CKPT]:\n        if not ckpt_path.exists():\n            logger.warning(f\"Checkpoint not found: {ckpt_path}\")\n            continue\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        cs = data.get(\"clean_scores\", {})\n        for ds in DATASETS:\n            if ds not in cs:\n                continue\n            if ds not in scores:\n                scores[ds] = {}\n            for model_id, model_scores in cs[ds].items():\n                if model_id in LOCAL_MODELS and model_id not in scores[ds]:\n                    scores[ds][model_id] = model_scores\n    return scores\n\n\ndef load_api_clean_scores():\n    \"\"\"Load clean scores for 9 API models from individual score files.\"\"\"\n    scores = {}\n    for model_id in API_MODELS:\n        for ds in DATASETS:\n            fname = f\"{model_id}__{ds}__clean.json\"\n            fpath = SCORES_DIR / fname\n            if not fpath.exists():\n                logger.warning(f\"API score file not found: {fpath}\")\n                continue\n            with open(fpath) as f:\n                data = json.load(f)\n            if ds not in scores:\n                scores[ds] = {}\n            scores[ds][model_id] = data.get(\"scores\", [])\n    return scores\n\n\ndef merge_clean_scores(local_scores, api_scores):\n    \"\"\"Merge local and API clean scores into unified dict.\"\"\"\n    merged = {}\n    for ds in DATASETS:\n        merged[ds] = {}\n        for src in [local_scores, api_scores]:\n            if ds in src:\n                merged[ds].update(src[ds])\n    return merged\n\n\ndef extract_winner_vector(score_list):\n    \"\"\"Extract winner labels from score list, normalizing to A/B/C/tie.\"\"\"\n    winners = []\n    for s in score_list:\n        w = s.get(\"winner\", \"tie\") if isinstance(s, dict) else \"tie\"\n        winners.append(w)\n    return winners\n\n\ndef compute_pairwise_mi(winners_i, winners_j):\n    \"\"\"Compute mutual information between two winner vectors.\"\"\"\n    n = min(len(winners_i), len(winners_j))\n    if n == 0:\n        return 0.0\n    return mutual_info_score(winners_i[:n], winners_j[:n])\n\n\ndef build_mi_matrix(clean_scores, dataset):\n    \"\"\"Build 15x15 MI matrix for a dataset.\"\"\"\n    ds_scores = clean_scores.get(dataset, {})\n    n_models = len(ALL_MODELS)\n    mi_mat = np.zeros((n_models, n_models))\n\n    winner_vectors = {}\n    for i, model_id in enumerate(ALL_MODELS):\n        if model_id in ds_scores:\n            winner_vectors[i] = extract_winner_vector(ds_scores[model_id])\n        else:\n            logger.warning(f\"No clean scores for {model_id} on {dataset}\")\n\n    for i in range(n_models):\n        for j in range(i + 1, n_models):\n            if i in winner_vectors and j in winner_vectors:\n                mi = compute_pairwise_mi(winner_vectors[i], winner_vectors[j])\n                mi_mat[i, j] = mi\n                mi_mat[j, i] = mi\n\n    return mi_mat\n\n\ndef mi_based_keff(mi_matrix, model_indices):\n    \"\"\"K_eff = (1/K) * sum_i [1 + sum_{j!=i} exp(-2 * MI_ij)]\"\"\"\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx, j_idx])\n        keff += term\n    return keff / K\n\n\ndef compute_all_panel_keffs(mi_matrix, dataset):\n    \"\"\"Compute K_eff for all C(15,3)=455 panels.\"\"\"\n    n_models = len(ALL_MODELS)\n    idx_to_model = {i: m for i, m in enumerate(ALL_MODELS)}\n    panels = {}\n\n    for combo in itertools.combinations(range(n_models), 3):\n        model_ids = [idx_to_model[i] for i in combo]\n        panel_key = \"|\".join(model_ids)\n        keff = mi_based_keff(mi_matrix, list(combo))\n\n        mi_pairs = {}\n        for a, b in itertools.combinations(combo, 2):\n            pair_key = f\"{idx_to_model[a]}|{idx_to_model[b]}\"\n            mi_pairs[pair_key] = float(mi_matrix[a, b])\n\n        panels[panel_key] = {\n            \"models\": model_ids,\n            \"keff\": float(keff),\n            \"mi_pairs\": mi_pairs,\n        }\n\n    return panels\n\n\ndef main():\n    logger.info(\"=== Plan 001 Step 3: MI Matrix Computation ===\")\n\n    local_scores = load_local_clean_scores()\n    api_scores = load_api_clean_scores()\n    clean_scores = merge_clean_scores(local_scores, api_scores)\n\n    for ds in DATASETS:\n        available = list(clean_scores.get(ds, {}).keys())\n        missing = [m for m in ALL_MODELS if m not in available]\n        logger.info(f\"  {ds}: {len(available)}/{len(ALL_MODELS)} models available\")\n        if missing:\n            logger.warning(f\"  {ds}: missing models: {missing}\")\n\n    available_count = sum(\n        1 for ds in DATASETS\n        for m in ALL_MODELS\n        if m in clean_scores.get(ds, {})\n    )\n    total_needed = len(DATASETS) * len(ALL_MODELS)\n    if available_count < total_needed:\n        logger.warning(\n            f\"Only {available_count}/{total_needed} model×dataset combos available. \"\n            f\"MI matrix will have zeros for missing pairs.\"\n        )\n\n    mi_matrices = {}\n    keff_per_panel = {}\n\n    for ds in DATASETS:\n        logger.info(f\"\\n--- Computing MI matrix for {ds} ---\")\n        mi_mat = build_mi_matrix(clean_scores, ds)\n        mi_matrices[ds] = mi_mat.tolist()\n\n        nonzero = np.count_nonzero(mi_mat)\n        max_possible = len(ALL_MODELS) * (len(ALL_MODELS) - 1)\n        logger.info(f\"  MI matrix: {nonzero}/{max_possible} non-zero entries\")\n        if nonzero > 0:\n            upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\n            upper_nz = upper[upper > 0]\n            if len(upper_nz) > 0:\n                logger.info(\n                    f\"  MI range: [{upper_nz.min():.4f}, {upper_nz.max():.4f}], \"\n                    f\"mean={upper_nz.mean():.4f}\"\n                )\n\n        logger.info(f\"  Computing K_eff for all C(15,3)=455 panels on {ds}...\")\n        panels = compute_all_panel_keffs(mi_mat, ds)\n        keff_per_panel[ds] = panels\n\n        keff_values = [p[\"keff\"] for p in panels.values()]\n        logger.info(\n            f\"  K_eff range: [{min(keff_values):.3f}, {max(keff_values):.3f}], \"\n            f\"mean={np.mean(keff_values):.3f}\"\n        )\n\n    MI_DIR.mkdir(parents=True, exist_ok=True)\n    output = {\n        \"models\": ALL_MODELS,\n        \"mi_matrix\": mi_matrices,\n        \"keff_per_panel\": keff_per_panel,\n    }\n    output_path = MI_DIR / \"mi_matrix_15models.json\"\n    with open(output_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n    logger.info(f\"\\nSaved MI matrix to {output_path}\")\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"MI MATRIX SUMMARY\")\n    print(\"=\" * 70)\n    for ds in DATASETS:\n        mi_mat = np.array(mi_matrices[ds])\n        upper = mi_mat[np.triu_indices_from(mi_mat, k=1)]\n        n_computed = np.count_nonzero(upper)\n        print(f\"\\n{ds}:\")\n        print(f\"  Pairwise MI computed: {n_computed}/105\")\n        if n_computed > 0:\n            nz = upper[upper > 0]\n            print(f\"  MI range: [{nz.min():.4f}, {nz.max():.4f}]\")\n            print(f\"  MI mean:  {nz.mean():.4f}\")\n        keffs = [p[\"keff\"] for p in keff_per_panel[ds].values()]\n        print(f\"  K_eff (455 panels): [{min(keffs):.3f}, {max(keffs):.3f}], mean={np.mean(keffs):.3f}\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Write · `toolu_01T9oc3hzZ5esLeCCJTEhziU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_confound_diagnosis.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Plan 001: K_eff vs eta_max confound diagnosis across all C(15,3) panels.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nfrom pathlib import Path\nfrom scipy import stats\n\nfrom src.utils import setup_logging\nfrom src.unified_data_loader import (\n    ALL_MODELS, LOCAL_MODELS, API_MODELS, DATASETS, ATTACKS,\n    PLAN001_DIR, SCORES_DIR,\n    load_all_scores, load_pairs, load_mi_data, load_api_asr,\n)\n\nlogger = setup_logging(\"plan001_confound\")\n\n\ndef compute_asr_from_scores(clean_scores, attacked_scores, pairs):\n    n_flips = 0\n    n_total = 0\n    for clean, attacked, pair in zip(clean_scores, attacked_scores, pairs):\n        gt = pair.get(\"ground_truth_winner\")\n        cw = clean.get(\"winner\") if isinstance(clean, dict) else None\n        aw = attacked.get(\"winner\") if isinstance(attacked, dict) else None\n        if cw == gt:\n            n_total += 1\n            if aw != gt:\n                n_flips += 1\n    return n_flips / max(n_total, 1)\n\n\ndef compute_all_individual_asr(clean, attacked, pairs):\n    \"\"\"Compute per-model ASR from loaded scores and pairs.\n\n    Returns: {ds: {atk: {model_id: asr}}}\n    \"\"\"\n    asr_data = {}\n    for ds in DATASETS:\n        asr_data[ds] = {}\n        for atk in ATTACKS:\n            asr_data[ds][atk] = {}\n            for mid in ALL_MODELS:\n                if mid not in clean[ds] or mid not in attacked[ds][atk]:\n                    continue\n                if ds not in pairs:\n                    continue\n                asr = compute_asr_from_scores(\n                    clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                )\n                asr_data[ds][atk][mid] = asr\n    # Overlay pre-computed API ASR (from individual files) where available\n    api_asr = load_api_asr()\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid, asr in api_asr.get(ds, {}).get(atk, {}).items():\n                if mid not in asr_data[ds][atk]:\n                    asr_data[ds][atk][mid] = asr\n    return asr_data\n\n\ndef mi_based_keff(mi_matrix_np, model_indices):\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix_np[i_idx, j_idx])\n        keff += term\n    return keff / K\n\n\ndef classify_panel(model_ids):\n    n_api = sum(1 for m in model_ids if m in API_MODELS)\n    if n_api == 3:\n        return \"all_api\"\n    elif n_api == 0:\n        return \"all_local\"\n    elif n_api == 2:\n        return \"2api_1local\"\n    else:\n        return \"1api_2local\"\n\n\nPANEL_COLORS = {\n    \"all_api\": \"#e74c3c\",\n    \"all_local\": \"#2ecc71\",\n    \"2api_1local\": \"#e67e22\",\n    \"1api_2local\": \"#3498db\",\n}\n\nPANEL_LABELS = {\n    \"all_api\": \"3 API\",\n    \"all_local\": \"3 Local\",\n    \"2api_1local\": \"2 API + 1 Local\",\n    \"1api_2local\": \"1 API + 2 Local\",\n}\n\n\ndef run_confound_analysis(mi_data, asr_data):\n    models = mi_data[\"models\"]\n    model_to_idx = {m: i for i, m in enumerate(models)}\n    conditions = {}\n\n    for ds in DATASETS:\n        mi_mat = np.array(mi_data[\"mi_matrix\"][ds])\n\n        for attack in ATTACKS:\n            cond_key = f\"{ds}×{attack}\"\n            model_asrs = asr_data.get(ds, {}).get(attack, {})\n\n            if len(model_asrs) < 3:\n                logger.warning(\n                    f\"  {cond_key}: only {len(model_asrs)} models have ASR, \"\n                    f\"need >=3 for panel construction. Skipping.\"\n                )\n                conditions[cond_key] = {\n                    \"pearson_r\": None,\n                    \"p_value\": None,\n                    \"verdict\": \"INSUFFICIENT_DATA\",\n                    \"n_panels\": 0,\n                    \"n_models_with_asr\": len(model_asrs),\n                }\n                continue\n\n            available_models = [\n                m for m in models if m in model_asrs\n            ]\n\n            keffs = []\n            eta_maxs = []\n            panel_types = []\n\n            for combo in itertools.combinations(available_models, 3):\n                indices = [model_to_idx[m] for m in combo]\n                keff = mi_based_keff(mi_mat, indices)\n                eta_max = max(model_asrs[m] for m in combo)\n\n                keffs.append(keff)\n                eta_maxs.append(eta_max)\n                panel_types.append(classify_panel(combo))\n\n            keffs = np.array(keffs)\n            eta_maxs = np.array(eta_maxs)\n\n            if len(keffs) < 3 or np.std(keffs) < 1e-10 or np.std(eta_maxs) < 1e-10:\n                r, p = 0.0, 1.0\n            else:\n                r, p = stats.pearsonr(keffs, eta_maxs)\n\n            if r < -0.7:\n                verdict = \"CONFOUND_SEVERE\"\n            elif r <= -0.5:\n                verdict = \"CONFOUND_MODERATE\"\n            else:\n                verdict = \"CONFOUND_BROKEN\"\n\n            conditions[cond_key] = {\n                \"pearson_r\": float(r),\n                \"p_value\": float(p),\n                \"verdict\": verdict,\n                \"n_panels\": len(keffs),\n                \"n_models_with_asr\": len(available_models),\n                \"keffs\": keffs.tolist(),\n                \"eta_maxs\": eta_maxs.tolist(),\n                \"panel_types\": panel_types,\n            }\n            logger.info(\n                f\"  {cond_key}: r={r:.3f}, p={p:.4f}, \"\n                f\"verdict={verdict}, n_panels={len(keffs)}\"\n            )\n\n    return conditions\n\n\ndef plot_scatter_grid(conditions, output_path):\n    valid_conds = {\n        k: v for k, v in conditions.items()\n        if v.get(\"pearson_r\") is not None\n    }\n    n = len(valid_conds)\n    if n == 0:\n        logger.warning(\"No valid conditions to plot\")\n        return\n\n    if n <= 6:\n        nrows, ncols = 2, 3\n    elif n <= 9:\n        nrows, ncols = 3, 3\n    else:\n        nrows, ncols = 3, 4\n\n    fig, axes = plt.subplots(\n        nrows, ncols,\n        figsize=(5 * ncols, 4 * nrows),\n        squeeze=False,\n    )\n\n    for idx, (cond_key, cond_data) in enumerate(sorted(valid_conds.items())):\n        row, col = divmod(idx, ncols)\n        ax = axes[row][col]\n\n        keffs = np.array(cond_data[\"keffs\"])\n        eta_maxs = np.array(cond_data[\"eta_maxs\"])\n        panel_types = cond_data[\"panel_types\"]\n        r = cond_data[\"pearson_r\"]\n        verdict = cond_data[\"verdict\"]\n\n        plotted_labels = set()\n        for pt in [\"all_local\", \"1api_2local\", \"2api_1local\", \"all_api\"]:\n            mask = [t == pt for t in panel_types]\n            if not any(mask):\n                continue\n            k_sub = keffs[mask]\n            e_sub = eta_maxs[mask]\n            label = PANEL_LABELS[pt] if pt not in plotted_labels else None\n            ax.scatter(\n                k_sub, e_sub,\n                c=PANEL_COLORS[pt],\n                alpha=0.4, s=12, label=label,\n                edgecolors=\"none\",\n            )\n            plotted_labels.add(pt)\n\n        verdict_color = {\n            \"CONFOUND_SEVERE\": \"#e74c3c\",\n            \"CONFOUND_MODERATE\": \"#e67e22\",\n            \"CONFOUND_BROKEN\": \"#27ae60\",\n        }.get(verdict, \"#333\")\n\n        ax.set_title(\n            f\"{cond_key}\\nr = {r:.3f}  [{verdict}]\",\n            fontsize=9,\n            color=verdict_color,\n        )\n        ax.set_xlabel(\"K_eff\", fontsize=8)\n        ax.set_ylabel(\"eta_max (individual ASR)\", fontsize=8)\n        ax.tick_params(labelsize=7)\n\n        if len(keffs) >= 3 and np.std(keffs) > 1e-10:\n            z = np.polyfit(keffs, eta_maxs, 1)\n            x_line = np.linspace(keffs.min(), keffs.max(), 50)\n            ax.plot(x_line, np.polyval(z, x_line), \"k--\", alpha=0.3, linewidth=1)\n\n        if idx == 0:\n            ax.legend(fontsize=6, loc=\"best\", framealpha=0.7)\n\n    for idx in range(len(valid_conds), nrows * ncols):\n        row, col = divmod(idx, ncols)\n        axes[row][col].set_visible(False)\n\n    fig.suptitle(\n        \"K_eff vs eta_max Confound Diagnosis (15 models, K=3 panels)\",\n        fontsize=12, y=1.02,\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    logger.info(\"=== Plan 001: K_eff vs eta_max Confound Diagnosis ===\")\n\n    logger.info(\"Loading MI matrix...\")\n    mi_data = load_mi_data()\n\n    logger.info(\"Loading scores and computing ASR...\")\n    clean, attacked = load_all_scores()\n    pairs = load_pairs()\n    asr_data = compute_all_individual_asr(clean, attacked, pairs)\n\n    for ds in DATASETS:\n        for attack in ATTACKS:\n            models_with_asr = list(asr_data.get(ds, {}).get(attack, {}).keys())\n            logger.info(f\"  {ds}×{attack}: {len(models_with_asr)} models\")\n\n    logger.info(\"\\nRunning confound analysis...\")\n    conditions = run_confound_analysis(mi_data, asr_data)\n\n    scatter_path = PLAN001_DIR / \"confound_scatter.png\"\n    plot_scatter_grid(conditions, scatter_path)\n\n    r_values = [\n        v[\"pearson_r\"] for v in conditions.values()\n        if v.get(\"pearson_r\") is not None\n    ]\n    if r_values:\n        mean_r = float(np.mean(r_values))\n        if mean_r < -0.7:\n            overall = \"CONFOUND_SEVERE\"\n        elif mean_r <= -0.5:\n            overall = \"CONFOUND_MODERATE\"\n        else:\n            overall = \"CONFOUND_BROKEN\"\n    else:\n        mean_r = None\n        overall = \"INSUFFICIENT_DATA\"\n\n    output_conditions = {}\n    for k, v in conditions.items():\n        output_conditions[k] = {\n            \"pearson_r\": v.get(\"pearson_r\"),\n            \"p_value\": v.get(\"p_value\"),\n            \"verdict\": v.get(\"verdict\"),\n            \"n_panels\": v.get(\"n_panels\"),\n            \"n_models_with_asr\": v.get(\"n_models_with_asr\"),\n        }\n\n    output = {\n        \"conditions\": output_conditions,\n        \"scatter_plots\": str(scatter_path),\n        \"overall_verdict\": overall,\n        \"mean_r\": mean_r,\n    }\n\n    output_path = PLAN001_DIR / \"confound_diagnosis.json\"\n    with open(output_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n    logger.info(f\"\\nDiagnosis saved to {output_path}\")\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"CONFOUND DIAGNOSIS SUMMARY\")\n    print(\"=\" * 70)\n    for cond_key, cond in sorted(output_conditions.items()):\n        r = cond[\"pearson_r\"]\n        v = cond[\"verdict\"]\n        n = cond[\"n_panels\"]\n        r_str = f\"{r:.3f}\" if r is not None else \"N/A\"\n        print(f\"  {cond_key:40s}  r={r_str:>7s}  {v:20s}  ({n} panels)\")\n    print(f\"\\n  Overall: mean_r={'N/A' if mean_r is None else f'{mean_r:.3f}'}, verdict={overall}\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "e554462c-a788-467a-a5e4-1a4af0270613",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5P8r6LkdeLYe64yWQGb9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3655,
      "cache_read_input_tokens": 79490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3655
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

_source line 58 · 2026-05-22T15:00:43.179Z_

<details><summary>↩ Tool result · `toolu_01T9oc3hzZ5esLeCCJTEhziU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_confound_diagnosis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "956e1ae2-ff7d-4a2a-af33-20ba13867cae",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_confound_diagnosis.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Plan 001: K_eff vs eta_max confound diagnosis across all C(15,3) panels.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nfrom pathlib import Path\nfrom scipy import stats\n\nfrom src.utils import setup_logging\nfrom src.unified_data_loader import (\n    ALL_MODELS, LOCAL_MODELS, API_MODELS, DATASETS, ATTACKS,\n    PLAN001_DIR, SCORES_DIR,\n    load_all_scores, load_pairs, load_mi_data, load_api_asr,\n)\n\nlogger = setup_logging(\"plan001_confound\")\n\n\ndef compute_asr_from_scores(clean_scores, attacked_scores, pairs):\n    n_flips = 0\n    n_total = 0\n    for clean, attacked, pair in zip(clean_scores, attacked_scores, pairs):\n        gt = pair.get(\"ground_truth_winner\")\n        cw = clean.get(\"winner\") if isinstance(clean, dict) else None\n        aw = attacked.get(\"winner\") if isinstance(attacked, dict) else None\n        if cw == gt:\n            n_total += 1\n            if aw != gt:\n                n_flips += 1\n    return n_flips / max(n_total, 1)\n\n\ndef compute_all_individual_asr(clean, attacked, pairs):\n    \"\"\"Compute per-model ASR from loaded scores and pairs.\n\n    Returns: {ds: {atk: {model_id: asr}}}\n    \"\"\"\n    asr_data = {}\n    for ds in DATASETS:\n        asr_data[ds] = {}\n        for atk in ATTACKS:\n            asr_data[ds][atk] = {}\n            for mid in ALL_MODELS:\n                if mid not in clean[ds] or mid not in attacked[ds][atk]:\n                    continue\n                if ds not in pairs:\n                    continue\n                asr = compute_asr_from_scores(\n                    clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                )\n                asr_data[ds][atk][mid] = asr\n    # Overlay pre-computed API ASR (from individual files) where available\n    api_asr = load_api_asr()\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid, asr in api_asr.get(ds, {}).get(atk, {}).items():\n                if mid not in asr_data[ds][atk]:\n                    asr_data[ds][atk][mid] = asr\n    return asr_data\n\n\ndef mi_based_keff(mi_matrix_np, model_indices):\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix_np[i_idx, j_idx])\n        keff += term\n    return keff / K\n\n\ndef classify_panel(model_ids):\n    n_api = sum(1 for m in model_ids if m in API_MODELS)\n    if n_api == 3:\n        return \"all_api\"\n    elif n_api == 0:\n        return \"all_local\"\n    elif n_api == 2:\n        return \"2api_1local\"\n    else:\n        return \"1api_2local\"\n\n\nPANEL_COLORS = {\n    \"all_api\": \"#e74c3c\",\n    \"all_local\": \"#2ecc71\",\n    \"2api_1local\": \"#e67e22\",\n    \"1api_2local\": \"#3498db\",\n}\n\nPANEL_LABELS = {\n    \"all_api\": \"3 API\",\n    \"all_local\": \"3 Local\",\n    \"2api_1local\": \"2 API + 1 Local\",\n    \"1api_2local\": \"1 API + 2 Local\",\n}\n\n\ndef run_confound_analysis(mi_data, asr_data):\n    models = mi_data[\"models\"]\n    model_to_idx = {m: i for i, m in enumerate(models)}\n    conditions = {}\n\n    for ds in DATASETS:\n        mi_mat = np.array(mi_data[\"mi_matrix\"][ds])\n\n        for attack in ATTACKS:\n            cond_key = f\"{ds}×{attack}\"\n            model_asrs = asr_data.get(ds, {}).get(attack, {})\n\n            if len(model_asrs) < 3:\n                logger.warning(\n                    f\"  {cond_key}: only {len(model_asrs)} models have ASR, \"\n                    f\"need >=3 for panel construction. Skipping.\"\n                )\n                conditions[cond_key] = {\n                    \"pearson_r\": None,\n                    \"p_value\": None,\n                    \"verdict\": \"INSUFFICIENT_DATA\",\n                    \"n_panels\": 0,\n                    \"n_models_with_asr\": len(model_asrs),\n                }\n                continue\n\n            available_models = [\n                m for m in models if m in model_asrs\n            ]\n\n            keffs = []\n            eta_maxs = []\n            panel_types = []\n\n            for combo in itertools.combinations(available_models, 3):\n                indices = [model_to_idx[m] for m in combo]\n                keff = mi_based_keff(mi_mat, indices)\n                eta_max = max(model_asrs[m] for m in combo)\n\n                keffs.append(keff)\n                eta_maxs.append(eta_max)\n                panel_types.append(classify_panel(combo))\n\n            keffs = np.array(keffs)\n            eta_maxs = np.array(eta_maxs)\n\n            if len(keffs) < 3 or np.std(keffs) < 1e-10 or np.std(eta_maxs) < 1e-10:\n                r, p = 0.0, 1.0\n            else:\n                r, p = stats.pearsonr(keffs, eta_maxs)\n\n            if r < -0.7:\n                verdict = \"CONFOUND_SEVERE\"\n            elif r <= -0.5:\n                verdict = \"CONFOUND_MODERATE\"\n            else:\n                verdict = \"CONFOUND_BROKEN\"\n\n            conditions[cond_key] = {\n                \"pearson_r\": float(r),\n                \"p_value\": float(p),\n                \"verdict\": verdict,\n                \"n_panels\": len(keffs),\n                \"n_models_with_asr\": len(available_models),\n                \"keffs\": keffs.tolist(),\n                \"eta_maxs\": eta_maxs.tolist(),\n                \"panel_types\": panel_types,\n            }\n            logger.info(\n                f\"  {cond_key}: r={r:.3f}, p={p:.4f}, \"\n                f\"verdict={verdict}, n_panels={len(keffs)}\"\n            )\n\n    return conditions\n\n\ndef plot_scatter_grid(conditions, output_path):\n    valid_conds = {\n        k: v for k, v in conditions.items()\n        if v.get(\"pearson_r\") is not None\n    }\n    n = len(valid_conds)\n    if n == 0:\n        logger.warning(\"No valid conditions to plot\")\n        return\n\n    if n <= 6:\n        nrows, ncols = 2, 3\n    elif n <= 9:\n        nrows, ncols = 3, 3\n    else:\n        nrows, ncols = 3, 4\n\n    fig, axes = plt.subplots(\n        nrows, ncols,\n        figsize=(5 * ncols, 4 * nrows),\n        squeeze=False,\n    )\n\n    for idx, (cond_key, cond_data) in enumerate(sorted(valid_conds.items())):\n        row, col = divmod(idx, ncols)\n        ax = axes[row][col]\n\n        keffs = np.array(cond_data[\"keffs\"])\n        eta_maxs = np.array(cond_data[\"eta_maxs\"])\n        panel_types = cond_data[\"panel_types\"]\n        r = cond_data[\"pearson_r\"]\n        verdict = cond_data[\"verdict\"]\n\n        plotted_labels = set()\n        for pt in [\"all_local\", \"1api_2local\", \"2api_1local\", \"all_api\"]:\n            mask = [t == pt for t in panel_types]\n            if not any(mask):\n                continue\n            k_sub = keffs[mask]\n            e_sub = eta_maxs[mask]\n            label = PANEL_LABELS[pt] if pt not in plotted_labels else None\n            ax.scatter(\n                k_sub, e_sub,\n                c=PANEL_COLORS[pt],\n                alpha=0.4, s=12, label=label,\n                edgecolors=\"none\",\n            )\n            plotted_labels.add(pt)\n\n        verdict_color = {\n            \"CONFOUND_SEVERE\": \"#e74c3c\",\n            \"CONFOUND_MODERATE\": \"#e67e22\",\n            \"CONFOUND_BROKEN\": \"#27ae60\",\n        }.get(verdict, \"#333\")\n\n        ax.set_title(\n            f\"{cond_key}\\nr = {r:.3f}  [{verdict}]\",\n            fontsize=9,\n            color=verdict_color,\n        )\n        ax.set_xlabel(\"K_eff\", fontsize=8)\n        ax.set_ylabel(\"eta_max (individual ASR)\", fontsize=8)\n        ax.tick_params(labelsize=7)\n\n        if len(keffs) >= 3 and np.std(keffs) > 1e-10:\n            z = np.polyfit(keffs, eta_maxs, 1)\n            x_line = np.linspace(keffs.min(), keffs.max(), 50)\n            ax.plot(x_line, np.polyval(z, x_line), \"k--\", alpha=0.3, linewidth=1)\n\n        if idx == 0:\n            ax.legend(fontsize=6, loc=\"best\", framealpha=0.7)\n\n    for idx in range(len(valid_conds), nrows * ncols):\n        row, col = divmod(idx, ncols)\n        axes[row][col].set_visible(False)\n\n    fig.suptitle(\n        \"K_eff vs eta_max Confound Diagnosis (15 models, K=3 panels)\",\n        fontsize=12, y=1.02,\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    logger.info(\"=== Plan 001: K_eff vs eta_max Confound Diagnosis ===\")\n\n    logger.info(\"Loading MI matrix...\")\n    mi_data = load_mi_data()\n\n    logger.info(\"Loading scores and computing ASR...\")\n    clean, attacked = load_all_scores()\n    pairs = load_pairs()\n    asr_data = compute_all_individual_asr(clean, attacked, pairs)\n\n    for ds in DATASETS:\n        for attack in ATTACKS:\n            models_with_asr = list(asr_data.get(ds, {}).get(attack, {}).keys())\n            logger.info(f\"  {ds}×{attack}: {len(models_with_asr)} models\")\n\n    logger.info(\"\\nRunning confound analysis...\")\n    conditions = run_confound_analysis(mi_data, asr_data)\n\n    scatter_path = PLAN001_DIR / \"confound_scatter.png\"\n    plot_scatter_grid(conditions, scatter_path)\n\n    r_values = [\n        v[\"pearson_r\"] for v in conditions.values()\n        if v.get(\"pearson_r\") is not None\n    ]\n    if r_values:\n        mean_r = float(np.mean(r_values))\n        if mean_r < -0.7:\n            overall = \"CONFOUND_SEVERE\"\n        elif mean_r <= -0.5:\n            overall = \"CONFOUND_MODERATE\"\n        else:\n            overall = \"CONFOUND_BROKEN\"\n    else:\n        mean_r = None\n        overall = \"INSUFFICIENT_DATA\"\n\n    output_conditions = {}\n    for k, v in conditions.items():\n        output_conditions[k] = {\n            \"pearson_r\": v.get(\"pearson_r\"),\n            \"p_value\": v.get(\"p_value\"),\n            \"verdict\": v.get(\"verdict\"),\n            \"n_panels\": v.get(\"n_panels\"),\n            \"n_models_with_asr\": v.get(\"n_models_with_asr\"),\n        }\n\n    output = {\n        \"conditions\": output_conditions,\n        \"scatter_plots\": str(scatter_path),\n        \"overall_verdict\": overall,\n        \"mean_r\": mean_r,\n    }\n\n    output_path = PLAN001_DIR / \"confound_diagnosis.json\"\n    with open(output_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n    logger.info(f\"\\nDiagnosis saved to {output_path}\")\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"CONFOUND DIAGNOSIS SUMMARY\")\n    print(\"=\" * 70)\n    for cond_key, cond in sorted(output_conditions.items()):\n        r = cond[\"pearson_r\"]\n        v = cond[\"verdict\"]\n        n = cond[\"n_panels\"]\n        r_str = f\"{r:.3f}\" if r is not None else \"N/A\"\n        print(f\"  {cond_key:40s}  r={r_str:>7s}  {v:20s}  ({n} panels)\")\n    print(f\"\\n  Overall: mean_r={'N/A' if mean_r is None else f'{mean_r:.3f}'}, verdict={overall}\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " #!/usr/bin/env python3",
          "-\"\"\"Plan 001: K_eff vs η_max confound diagnosis across all C(15,3) panels.\"\"\"",
          "+\"\"\"Plan 001: K_eff vs eta_max confound diagnosis across all C(15,3) panels.\"\"\"",
          " ",
          " import os",
          " os.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\""
        ]
      },
      {
        "oldStart": 17,
        "oldLines": 54,
        "newStart": 17,
        "newLines": 16,
        "lines": [
          " from scipy import stats",
          " ",
          " from src.utils import setup_logging",
          "+from src.unified_data_loader import (",
          "+    ALL_MODELS, LOCAL_MODELS, API_MODELS, DATASETS, ATTACKS,",
          "+    PLAN001_DIR, SCORES_DIR,",
          "+    load_all_scores, load_pairs, load_mi_data, load_api_asr,",
          "+)",
          " ",
          " logger = setup_logging(\"plan001_confound\")",
          " ",
          "-# ── Model lists ──────────────────────────────────────────────────────",
          "-LOCAL_MODELS = [",
          "-    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",",
          "-    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",",
          "-]",
          "-API_MODELS = [",
          "-    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",",
          "-    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",",
          "-    \"gpt-4o-mini\", \"claude-3-haiku\",",
          "-]",
          "-ALL_MODELS = LOCAL_MODELS + API_MODELS",
          "-DATASETS = [\"mmlu\", \"arc_challenge\"]",
          "-ATTACKS = [",
          "-    \"prompt_injection\", \"sycophancy\", \"score_manipulation\",",
          "-    \"verbosity_bias\", \"position_bias\", \"authority_bias\",",
          "-]",
          " ",
          "-# ── Paths ────────────────────────────────────────────────────────────",
          "-RESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")",
          "-PLAN001_DIR = RESULTS_DIR / \"plan001\"",
          "-SCORES_DIR = PLAN001_DIR / \"individual_scores\"",
          "-MI_MATRIX_PATH = PLAN001_DIR / \"mi_matrix\" / \"mi_matrix_15models.json\"",
          "-",
          "-STEP2V3_CKPT = RESULTS_DIR / \"_step2v3_checkpoint.json\"",
          "-TAXONOMY_CKPT = RESULTS_DIR / \"_taxonomy_checkpoint.json\"",
          "-",
          "-# Attack → checkpoint mapping for local models",
          "-LOCAL_ATTACK_CKPT = {",
          "-    \"prompt_injection\": STEP2V3_CKPT,",
          "-    \"sycophancy\": STEP2V3_CKPT,",
          "-    \"score_manipulation\": STEP2V3_CKPT,",
          "-    \"verbosity_bias\": TAXONOMY_CKPT,",
          "-    \"position_bias\": TAXONOMY_CKPT,",
          "-    \"authority_bias\": TAXONOMY_CKPT,",
          "-}",
          "-",
          "-",
          "-def _invert_winners(scores):",
          "-    \"\"\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\"\"\"",
          "-    swap = {\"A\": \"B\", \"B\": \"A\", \"tie\": \"tie\"}",
          "-    return [{**s, \"winner\": swap.get(s.get(\"winner\", \"tie\"), \"tie\")} for s in scores]",
          "-",
          "-",
          " def compute_asr_from_scores(clean_scores, attacked_scores, pairs):",
          "-    \"\"\"Compute individual judge ASR: fraction of clean-correct flipped by attack.\"\"\"",
          "     n_flips = 0",
          "     n_total = 0",
          "     for clean, attacked, pair in zip(clean_scores, attacked_scores, pairs):"
        ]
      },
      {
        "oldStart": 78,
        "oldLines": 116,
        "newStart": 40,
        "newLines": 36,
        "lines": [
          "     return n_flips / max(n_total, 1)",
          " ",
          " ",
          "-def load_local_individual_asr():",
          "-    \"\"\"Load per-model ASR for local models from checkpoint files.",
          "+def compute_all_individual_asr(clean, attacked, pairs):",
          "+    \"\"\"Compute per-model ASR from loaded scores and pairs.",
          " ",
          "-    Returns: {dataset: {attack: {model_id: asr}}}",
          "+    Returns: {ds: {atk: {model_id: asr}}}",
          "     \"\"\"",
          "     asr_data = {}",
          "-    ckpt_cache = {}",
          "-",
          "-    for attack in ATTACKS:",
          "-        ckpt_path = LOCAL_ATTACK_CKPT[attack]",
          "-        if str(ckpt_path) not in ckpt_cache:",
          "-            if not ckpt_path.exists():",
          "-                logger.warning(f\"Checkpoint not found: {ckpt_path}\")",
          "-                continue",
          "-            with open(ckpt_path) as f:",
          "-                ckpt_cache[str(ckpt_path)] = json.load(f)",
          "-        data = ckpt_cache[str(ckpt_path)]",
          "-",
          "-        for ds in DATASETS:",
          "-            if ds not in asr_data:",
          "-                asr_data[ds] = {}",
          "-            if attack not in asr_data[ds]:",
          "-                asr_data[ds][attack] = {}",
          "-",
          "-            clean_all = data.get(\"clean_scores\", {}).get(ds, {})",
          "-            atk_all = data.get(\"attacked_scores\", {}).get(ds, {}).get(attack, {})",
          "-            pairs = data.get(\"pairs\", {}).get(ds, [])",
          "-",
          "-            if not pairs:",
          "-                logger.warning(f\"No pairs for {ds} in {ckpt_path.name}\")",
          "-                continue",
          "-",
          "-            for model_id in LOCAL_MODELS:",
          "-                if model_id not in clean_all or model_id not in atk_all:",
          "+    for ds in DATASETS:",
          "+        asr_data[ds] = {}",
          "+        for atk in ATTACKS:",
          "+            asr_data[ds][atk] = {}",
          "+            for mid in ALL_MODELS:",
          "+                if mid not in clean[ds] or mid not in attacked[ds][atk]:",
          "                     continue",
          "-                atk_scores = atk_all[model_id]",
          "-                if attack == \"position_bias\":",
          "-                    atk_scores = _invert_winners(atk_scores)",
          "+                if ds not in pairs:",
          "+                    continue",
          "                 asr = compute_asr_from_scores(",
          "-                    clean_all[model_id], atk_scores, pairs",
          "+                    clean[ds][mid], attacked[ds][atk][mid], pairs[ds]",
          "                 )",
          "-                asr_data[ds][attack][model_id] = asr",
          "-",
          "+                asr_data[ds][atk][mid] = asr",
          "+    # Overlay pre-computed API ASR (from individual files) where available",
          "+    api_asr = load_api_asr()",
          "+    for ds in DATASETS:",
          "+        for atk in ATTACKS:",
          "+            for mid, asr in api_asr.get(ds, {}).get(atk, {}).items():",
          "+                if mid not in asr_data[ds][atk]:",
          "+                    asr_data[ds][atk][mid] = asr",
          "     return asr_data",
          " ",
          " ",
          "-def load_api_individual_asr():",
          "-    \"\"\"Load per-model ASR for API models from individual score files.",
          "-",
          "-    Returns: {dataset: {attack: {model_id: asr}}}",
          "-    \"\"\"",
          "-    asr_data = {}",
          "-    for model_id in API_MODELS:",
          "-        for ds in DATASETS:",
          "-            if ds not in asr_data:",
          "-                asr_data[ds] = {}",
          "-",
          "-            clean_path = SCORES_DIR / f\"{model_id}__{ds}__clean.json\"",
          "-            if not clean_path.exists():",
          "-                continue",
          "-            with open(clean_path) as f:",
          "-                clean_data = json.load(f)",
          "-            clean_scores = clean_data.get(\"scores\", [])",
          "-",
          "-            for attack in ATTACKS:",
          "-                if attack not in asr_data[ds]:",
          "-                    asr_data[ds][attack] = {}",
          "-",
          "-                atk_path = SCORES_DIR / f\"{model_id}__{ds}__{attack}.json\"",
          "-                if not atk_path.exists():",
          "-                    continue",
          "-                with open(atk_path) as f:",
          "-                    atk_data = json.load(f)",
          "-",
          "-                asr = atk_data.get(\"asr\")",
          "-                if asr is not None:",
          "-                    asr_data[ds][attack][model_id] = asr",
          "-                else:",
          "-                    logger.warning(",
          "-                        f\"No ASR in {atk_path.name}, skipping\"",
          "-                    )",
          "-",
          "-    return asr_data",
          "-",
          "-",
          "-def merge_asr(local_asr, api_asr):",
          "-    \"\"\"Merge local and API ASR data.\"\"\"",
          "-    merged = {}",
          "-    for ds in DATASETS:",
          "-        merged[ds] = {}",
          "-        for attack in ATTACKS:",
          "-            merged[ds][attack] = {}",
          "-            for src in [local_asr, api_asr]:",
          "-                if ds in src and attack in src[ds]:",
          "-                    merged[ds][attack].update(src[ds][attack])",
          "-    return merged",
          "-",
          "-",
          "-def load_mi_matrix():",
          "-    \"\"\"Load MI matrix from Step 3 output.\"\"\"",
          "-    if not MI_MATRIX_PATH.exists():",
          "-        logger.error(f\"MI matrix not found: {MI_MATRIX_PATH}\")",
          "-        sys.exit(1)",
          "-    with open(MI_MATRIX_PATH) as f:",
          "-        data = json.load(f)",
          "-    return data",
          "-",
          "-",
          " def mi_based_keff(mi_matrix_np, model_indices):",
          "-    \"\"\"K_eff = (1/K) * sum_i [1 + sum_{j!=i} exp(-2 * MI_ij)]\"\"\"",
          "     K = len(model_indices)",
          "     if K <= 1:",
          "         return 1.0"
        ]
      },
      {
        "oldStart": 202,
        "oldLines": 7,
        "newStart": 84,
        "newLines": 6,
        "lines": [
          " ",
          " ",
          " def classify_panel(model_ids):",
          "-    \"\"\"Classify panel by composition for scatter plot coloring.\"\"\"",
          "     n_api = sum(1 for m in model_ids if m in API_MODELS)",
          "     if n_api == 3:",
          "         return \"all_api\""
        ]
      },
      {
        "oldStart": 230,
        "oldLines": 7,
        "newStart": 111,
        "newLines": 6,
        "lines": [
          " ",
          " ",
          " def run_confound_analysis(mi_data, asr_data):",
          "-    \"\"\"Run K_eff vs η_max analysis for all conditions.\"\"\"",
          "     models = mi_data[\"models\"]",
          "     model_to_idx = {m: i for i, m in enumerate(models)}",
          "     conditions = {}"
        ]
      },
      {
        "oldStart": 245,
        "oldLines": 7,
        "newStart": 125,
        "newLines": 7,
        "lines": [
          "             if len(model_asrs) < 3:",
          "                 logger.warning(",
          "                     f\"  {cond_key}: only {len(model_asrs)} models have ASR, \"",
          "-                    f\"need ≥3 for panel construction. Skipping.\"",
          "+                    f\"need >=3 for panel construction. Skipping.\"",
          "                 )",
          "                 conditions[cond_key] = {",
          "                     \"pearson_r\": None,"
        ]
      },
      {
        "oldStart": 307,
        "oldLines": 7,
        "newStart": 187,
        "newLines": 6,
        "lines": [
          " ",
          " ",
          " def plot_scatter_grid(conditions, output_path):",
          "-    \"\"\"Plot K_eff vs η_max scatter grid.\"\"\"",
          "     valid_conds = {",
          "         k: v for k, v in conditions.items()",
          "         if v.get(\"pearson_r\") is not None"
        ]
      },
      {
        "oldStart": 368,
        "oldLines": 7,
        "newStart": 247,
        "newLines": 7,
        "lines": [
          "             color=verdict_color,",
          "         )",
          "         ax.set_xlabel(\"K_eff\", fontsize=8)",
          "-        ax.set_ylabel(\"η_max (individual ASR)\", fontsize=8)",
          "+        ax.set_ylabel(\"eta_max (individual ASR)\", fontsize=8)",
          "         ax.tick_params(labelsize=7)",
          " ",
          "         if len(keffs) >= 3 and np.std(keffs) > 1e-10:"
        ]
      },
      {
        "oldStart": 384,
        "oldLines": 7,
        "newStart": 263,
        "newLines": 7,
        "lines": [
          "         axes[row][col].set_visible(False)",
          " ",
          "     fig.suptitle(",
          "-        \"K_eff vs η_max Confound Diagnosis (15 models, K=3 panels)\",",
          "+        \"K_eff vs eta_max Confound Diagnosis (15 models, K=3 panels)\",",
          "         fontsize=12, y=1.02,",
          "     )",
          "     plt.tight_layout()"
        ]
      },
      {
        "oldStart": 394,
        "oldLines": 15,
        "newStart": 273,
        "newLines": 15,
        "lines": [
          " ",
          " ",
          " def main():",
          "-    logger.info(\"=== Plan 001: K_eff vs η_max Confound Diagnosis ===\")",
          "+    logger.info(\"=== Plan 001: K_eff vs eta_max Confound Diagnosis ===\")",
          " ",
          "     logger.info(\"Loading MI matrix...\")",
          "-    mi_data = load_mi_matrix()",
          "+    mi_data = load_mi_data()",
          " ",
          "-    logger.info(\"Loading individual ASR data...\")",
          "-    local_asr = load_local_individual_asr()",
          "-    api_asr = load_api_individual_asr()",
          "-    asr_data = merge_asr(local_asr, api_asr)",
          "+    logger.info(\"Loading scores and computing ASR...\")",
          "+    clean, attacked = load_all_scores()",
          "+    pairs = load_pairs()",
          "+    asr_data = compute_all_individual_asr(clean, attacked, pairs)",
          " ",
          "     for ds in DATASETS:",
          "         for attack in ATTACKS:"
        ]
      },
      {
        "oldStart": 462,
        "oldLines": 7,
        "newStart": 341,
        "newLines": 7,
        "lines": [
          "         n = cond[\"n_panels\"]",
          "         r_str = f\"{r:.3f}\" if r is not None else \"N/A\"",
          "         print(f\"  {cond_key:40s}  r={r_str:>7s}  {v:20s}  ({n} panels)\")",
          "-    print(f\"\\n  Overall: mean_r={mean_r:.3f if mean_r else 'N/A'}, verdict={overall}\")",
          "+    print(f\"\\n  Overall: mean_r={'N/A' if mean_r is None else f'{mean_r:.3f}'}, verdict={overall}\")",
          "     print(\"=\" * 70)",
          " ",
          " "
        ]
      }
    ],
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Plan 001: K_eff vs η_max confound diagnosis across all C(15,3) panels.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\nfrom pathlib import Path\nfrom scipy import stats\n\nfrom src.utils import setup_logging\n\nlogger = setup_logging(\"plan001_confound\")\n\n# ── Model lists ──────────────────────────────────────────────────────\nLOCAL_MODELS = [\n    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",\n    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",\n]\nAPI_MODELS = [\n    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",\n    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",\n    \"gpt-4o-mini\", \"claude-3-haiku\",\n]\nALL_MODELS = LOCAL_MODELS + API_MODELS\nDATASETS = [\"mmlu\", \"arc_challenge\"]\nATTACKS = [\n    \"prompt_injection\", \"sycophancy\", \"score_manipulation\",\n    \"verbosity_bias\", \"position_bias\", \"authority_bias\",\n]\n\n# ── Paths ────────────────────────────────────────────────────────────\nRESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")\nPLAN001_DIR = RESULTS_DIR / \"plan001\"\nSCORES_DIR = PLAN001_DIR / \"individual_scores\"\nMI_MATRIX_PATH = PLAN001_DIR / \"mi_matrix\" / \"mi_matrix_15models.json\"\n\nSTEP2V3_CKPT = RESULTS_DIR / \"_step2v3_checkpoint.json\"\nTAXONOMY_CKPT = RESULTS_DIR / \"_taxonomy_checkpoint.json\"\n\n# Attack → checkpoint mapping for local models\nLOCAL_ATTACK_CKPT = {\n    \"prompt_injection\": STEP2V3_CKPT,\n    \"sycophancy\": STEP2V3_CKPT,\n    \"score_manipulation\": STEP2V3_CKPT,\n    \"verbosity_bias\": TAXONOMY_CKPT,\n    \"position_bias\": TAXONOMY_CKPT,\n    \"authority_bias\": TAXONOMY_CKPT,\n}\n\n\ndef _invert_winners(scores):\n    \"\"\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\"\"\"\n    swap = {\"A\": \"B\", \"B\": \"A\", \"tie\": \"tie\"}\n    return [{**s, \"winner\": swap.get(s.get(\"winner\", \"tie\"), \"tie\")} for s in scores]\n\n\ndef compute_asr_from_scores(clean_scores, attacked_scores, pairs):\n    \"\"\"Compute individual judge ASR: fraction of clean-correct flipped by attack.\"\"\"\n    n_flips = 0\n    n_total = 0\n    for clean, attacked, pair in zip(clean_scores, attacked_scores, pairs):\n        gt = pair.get(\"ground_truth_winner\")\n        cw = clean.get(\"winner\") if isinstance(clean, dict) else None\n        aw = attacked.get(\"winner\") if isinstance(attacked, dict) else None\n        if cw == gt:\n            n_total += 1\n            if aw != gt:\n                n_flips += 1\n    return n_flips / max(n_total, 1)\n\n\ndef load_local_individual_asr():\n    \"\"\"Load per-model ASR for local models from checkpoint files.\n\n    Returns: {dataset: {attack: {model_id: asr}}}\n    \"\"\"\n    asr_data = {}\n    ckpt_cache = {}\n\n    for attack in ATTACKS:\n        ckpt_path = LOCAL_ATTACK_CKPT[attack]\n        if str(ckpt_path) not in ckpt_cache:\n            if not ckpt_path.exists():\n                logger.warning(f\"Checkpoint not found: {ckpt_path}\")\n                continue\n            with open(ckpt_path) as f:\n                ckpt_cache[str(ckpt_path)] = json.load(f)\n        data = ckpt_cache[str(ckpt_path)]\n\n        for ds in DATASETS:\n            if ds not in asr_data:\n                asr_data[ds] = {}\n            if attack not in asr_data[ds]:\n                asr_data[ds][attack] = {}\n\n            clean_all = data.get(\"clean_scores\", {}).get(ds, {})\n            atk_all = data.get(\"attacked_scores\", {}).get(ds, {}).get(attack, {})\n            pairs = data.get(\"pairs\", {}).get(ds, [])\n\n            if not pairs:\n                logger.warning(f\"No pairs for {ds} in {ckpt_path.name}\")\n                continue\n\n            for model_id in LOCAL_MODELS:\n                if model_id not in clean_all or model_id not in atk_all:\n                    continue\n                atk_scores = atk_all[model_id]\n                if attack == \"position_bias\":\n                    atk_scores = _invert_winners(atk_scores)\n                asr = compute_asr_from_scores(\n                    clean_all[model_id], atk_scores, pairs\n                )\n                asr_data[ds][attack][model_id] = asr\n\n    return asr_data\n\n\ndef load_api_individual_asr():\n    \"\"\"Load per-model ASR for API models from individual score files.\n\n    Returns: {dataset: {attack: {model_id: asr}}}\n    \"\"\"\n    asr_data = {}\n    for model_id in API_MODELS:\n        for ds in DATASETS:\n            if ds not in asr_data:\n                asr_data[ds] = {}\n\n            clean_path = SCORES_DIR / f\"{model_id}__{ds}__clean.json\"\n            if not clean_path.exists():\n                continue\n            with open(clean_path) as f:\n                clean_data = json.load(f)\n            clean_scores = clean_data.get(\"scores\", [])\n\n            for attack in ATTACKS:\n                if attack not in asr_data[ds]:\n                    asr_data[ds][attack] = {}\n\n                atk_path = SCORES_DIR / f\"{model_id}__{ds}__{attack}.json\"\n                if not atk_path.exists():\n                    continue\n                with open(atk_path) as f:\n                    atk_data = json.load(f)\n\n                asr = atk_data.get(\"asr\")\n                if asr is not None:\n                    asr_data[ds][attack][model_id] = asr\n                else:\n                    logger.warning(\n                        f\"No ASR in {atk_path.name}, skipping\"\n                    )\n\n    return asr_data\n\n\ndef merge_asr(local_asr, api_asr):\n    \"\"\"Merge local and API ASR data.\"\"\"\n    merged = {}\n    for ds in DATASETS:\n        merged[ds] = {}\n        for attack in ATTACKS:\n            merged[ds][attack] = {}\n            for src in [local_asr, api_asr]:\n                if ds in src and attack in src[ds]:\n                    merged[ds][attack].update(src[ds][attack])\n    return merged\n\n\ndef load_mi_matrix():\n    \"\"\"Load MI matrix from Step 3 output.\"\"\"\n    if not MI_MATRIX_PATH.exists():\n        logger.error(f\"MI matrix not found: {MI_MATRIX_PATH}\")\n        sys.exit(1)\n    with open(MI_MATRIX_PATH) as f:\n        data = json.load(f)\n    return data\n\n\ndef mi_based_keff(mi_matrix_np, model_indices):\n    \"\"\"K_eff = (1/K) * sum_i [1 + sum_{j!=i} exp(-2 * MI_ij)]\"\"\"\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix_np[i_idx, j_idx])\n        keff += term\n    return keff / K\n\n\ndef classify_panel(model_ids):\n    \"\"\"Classify panel by composition for scatter plot coloring.\"\"\"\n    n_api = sum(1 for m in model_ids if m in API_MODELS)\n    if n_api == 3:\n        return \"all_api\"\n    elif n_api == 0:\n        return \"all_local\"\n    elif n_api == 2:\n        return \"2api_1local\"\n    else:\n        return \"1api_2local\"\n\n\nPANEL_COLORS = {\n    \"all_api\": \"#e74c3c\",\n    \"all_local\": \"#2ecc71\",\n    \"2api_1local\": \"#e67e22\",\n    \"1api_2local\": \"#3498db\",\n}\n\nPANEL_LABELS = {\n    \"all_api\": \"3 API\",\n    \"all_local\": \"3 Local\",\n    \"2api_1local\": \"2 API + 1 Local\",\n    \"1api_2local\": \"1 API + 2 Local\",\n}\n\n\ndef run_confound_analysis(mi_data, asr_data):\n    \"\"\"Run K_eff vs η_max analysis for all conditions.\"\"\"\n    models = mi_data[\"models\"]\n    model_to_idx = {m: i for i, m in enumerate(models)}\n    conditions = {}\n\n    for ds in DATASETS:\n        mi_mat = np.array(mi_data[\"mi_matrix\"][ds])\n\n        for attack in ATTACKS:\n            cond_key = f\"{ds}×{attack}\"\n            model_asrs = asr_data.get(ds, {}).get(attack, {})\n\n            if len(model_asrs) < 3:\n                logger.warning(\n                    f\"  {cond_key}: only {len(model_asrs)} models have ASR, \"\n                    f\"need ≥3 for panel construction. Skipping.\"\n                )\n                conditions[cond_key] = {\n                    \"pearson_r\": None,\n                    \"p_value\": None,\n                    \"verdict\": \"INSUFFICIENT_DATA\",\n                    \"n_panels\": 0,\n                    \"n_models_with_asr\": len(model_asrs),\n                }\n                continue\n\n            available_models = [\n                m for m in models if m in model_asrs\n            ]\n\n            keffs = []\n            eta_maxs = []\n            panel_types = []\n\n            for combo in itertools.combinations(available_models, 3):\n                indices = [model_to_idx[m] for m in combo]\n                keff = mi_based_keff(mi_mat, indices)\n                eta_max = max(model_asrs[m] for m in combo)\n\n                keffs.append(keff)\n                eta_maxs.append(eta_max)\n                panel_types.append(classify_panel(combo))\n\n            keffs = np.array(keffs)\n            eta_maxs = np.array(eta_maxs)\n\n            if len(keffs) < 3 or np.std(keffs) < 1e-10 or np.std(eta_maxs) < 1e-10:\n                r, p = 0.0, 1.0\n            else:\n                r, p = stats.pearsonr(keffs, eta_maxs)\n\n            if r < -0.7:\n                verdict = \"CONFOUND_SEVERE\"\n            elif r <= -0.5:\n                verdict = \"CONFOUND_MODERATE\"\n            else:\n                verdict = \"CONFOUND_BROKEN\"\n\n            conditions[cond_key] = {\n                \"pearson_r\": float(r),\n                \"p_value\": float(p),\n                \"verdict\": verdict,\n                \"n_panels\": len(keffs),\n                \"n_models_with_asr\": len(available_models),\n                \"keffs\": keffs.tolist(),\n                \"eta_maxs\": eta_maxs.tolist(),\n                \"panel_types\": panel_types,\n            }\n            logger.info(\n                f\"  {cond_key}: r={r:.3f}, p={p:.4f}, \"\n                f\"verdict={verdict}, n_panels={len(keffs)}\"\n            )\n\n    return conditions\n\n\ndef plot_scatter_grid(conditions, output_path):\n    \"\"\"Plot K_eff vs η_max scatter grid.\"\"\"\n    valid_conds = {\n        k: v for k, v in conditions.items()\n        if v.get(\"pearson_r\") is not None\n    }\n    n = len(valid_conds)\n    if n == 0:\n        logger.warning(\"No valid conditions to plot\")\n        return\n\n    if n <= 6:\n        nrows, ncols = 2, 3\n    elif n <= 9:\n        nrows, ncols = 3, 3\n    else:\n        nrows, ncols = 3, 4\n\n    fig, axes = plt.subplots(\n        nrows, ncols,\n        figsize=(5 * ncols, 4 * nrows),\n        squeeze=False,\n    )\n\n    for idx, (cond_key, cond_data) in enumerate(sorted(valid_conds.items())):\n        row, col = divmod(idx, ncols)\n        ax = axes[row][col]\n\n        keffs = np.array(cond_data[\"keffs\"])\n        eta_maxs = np.array(cond_data[\"eta_maxs\"])\n        panel_types = cond_data[\"panel_types\"]\n        r = cond_data[\"pearson_r\"]\n        verdict = cond_data[\"verdict\"]\n\n        plotted_labels = set()\n        for pt in [\"all_local\", \"1api_2local\", \"2api_1local\", \"all_api\"]:\n            mask = [t == pt for t in panel_types]\n            if not any(mask):\n                continue\n            k_sub = keffs[mask]\n            e_sub = eta_maxs[mask]\n            label = PANEL_LABELS[pt] if pt not in plotted_labels else None\n            ax.scatter(\n                k_sub, e_sub,\n                c=PANEL_COLORS[pt],\n                alpha=0.4, s=12, label=label,\n                edgecolors=\"none\",\n            )\n            plotted_labels.add(pt)\n\n        verdict_color = {\n            \"CONFOUND_SEVERE\": \"#e74c3c\",\n            \"CONFOUND_MODERATE\": \"#e67e22\",\n            \"CONFOUND_BROKEN\": \"#27ae60\",\n        }.get(verdict, \"#333\")\n\n        ax.set_title(\n            f\"{cond_key}\\nr = {r:.3f}  [{verdict}]\",\n            fontsize=9,\n            color=verdict_color,\n        )\n        ax.set_xlabel(\"K_eff\", fontsize=8)\n        ax.set_ylabel(\"η_max (individual ASR)\", fontsize=8)\n        ax.tick_params(labelsize=7)\n\n        if len(keffs) >= 3 and np.std(keffs) > 1e-10:\n            z = np.polyfit(keffs, eta_maxs, 1)\n            x_line = np.linspace(keffs.min(), keffs.max(), 50)\n            ax.plot(x_line, np.polyval(z, x_line), \"k--\", alpha=0.3, linewidth=1)\n\n        if idx == 0:\n            ax.legend(fontsize=6, loc=\"best\", framealpha=0.7)\n\n    for idx in range(len(valid_conds), nrows * ncols):\n        row, col = divmod(idx, ncols)\n        axes[row][col].set_visible(False)\n\n    fig.suptitle(\n        \"K_eff vs η_max Confound Diagnosis (15 models, K=3 panels)\",\n        fontsize=12, y=1.02,\n    )\n    plt.tight_layout()\n    plt.savefig(output_path, dpi=150, bbox_inches=\"tight\")\n    plt.close()\n    logger.info(f\"Scatter plot saved to {output_path}\")\n\n\ndef main():\n    logger.info(\"=== Plan 001: K_eff vs η_max Confound Diagnosis ===\")\n\n    logger.info(\"Loading MI matrix...\")\n    mi_data = load_mi_matrix()\n\n    logger.info(\"Loading individual ASR data...\")\n    local_asr = load_local_individual_asr()\n    api_asr = load_api_individual_asr()\n    asr_data = merge_asr(local_asr, api_asr)\n\n    for ds in DATASETS:\n        for attack in ATTACKS:\n            models_with_asr = list(asr_data.get(ds, {}).get(attack, {}).keys())\n            logger.info(f\"  {ds}×{attack}: {len(models_with_asr)} models\")\n\n    logger.info(\"\\nRunning confound analysis...\")\n    conditions = run_confound_analysis(mi_data, asr_data)\n\n    scatter_path = PLAN001_DIR / \"confound_scatter.png\"\n    plot_scatter_grid(conditions, scatter_path)\n\n    r_values = [\n        v[\"pearson_r\"] for v in conditions.values()\n        if v.get(\"pearson_r\") is not None\n    ]\n    if r_values:\n        mean_r = float(np.mean(r_values))\n        if mean_r < -0.7:\n            overall = \"CONFOUND_SEVERE\"\n        elif mean_r <= -0.5:\n            overall = \"CONFOUND_MODERATE\"\n        else:\n            overall = \"CONFOUND_BROKEN\"\n    else:\n        mean_r = None\n        overall = \"INSUFFICIENT_DATA\"\n\n    output_conditions = {}\n    for k, v in conditions.items():\n        output_conditions[k] = {\n            \"pearson_r\": v.get(\"pearson_r\"),\n            \"p_value\": v.get(\"p_value\"),\n            \"verdict\": v.get(\"verdict\"),\n            \"n_panels\": v.get(\"n_panels\"),\n            \"n_models_with_asr\": v.get(\"n_models_with_asr\"),\n        }\n\n    output = {\n        \"conditions\": output_conditions,\n        \"scatter_plots\": str(scatter_path),\n        \"overall_verdict\": overall,\n        \"mean_r\": mean_r,\n    }\n\n    output_path = PLAN001_DIR / \"confound_diagnosis.json\"\n    with open(output_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False)\n    logger.info(f\"\\nDiagnosis saved to {output_path}\")\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"CONFOUND DIAGNOSIS SUMMARY\")\n    print(\"=\" * 70)\n    for cond_key, cond in sorted(output_conditions.items()):\n        r = cond[\"pearson_r\"]\n        v = cond[\"verdict\"]\n        n = cond[\"n_panels\"]\n        r_str = f\"{r:.3f}\" if r is not None else \"N/A\"\n        print(f\"  {cond_key:40s}  r={r_str:>7s}  {v:20s}  ({n} panels)\")\n    print(f\"\\n  Overall: mean_r={mean_r:.3f if mean_r else 'N/A'}, verdict={overall}\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Write · `toolu_0164FBKizJsxhbPvFBttv2ew`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 4: Panel regression -- 455 panels x 12 conditions.\n\nInput:\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\n\nOutput:\n  - artifacts/results/plan001/panel_regression/step4_regression_results.json\n\nDependencies: numpy, scipy, statsmodels\nOptional: pingouin (for partial_corr; manual fallback included)\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport warnings\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy import optimize, stats, special\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\nfrom statsmodels.stats.multitest import multipletests\n\nfrom src.utils import setup_logging\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,\n    load_all_scores, load_pairs, load_mi_data,\n)\n\nlogger = setup_logging(\"plan001_step4\")\n\nEPS = 0.001\n\n\n# ── JSON Helper ──────────────────────────────────────────────────────\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\n# ── ASR Computation ──────────────────────────────────────────────────\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\n# ── Regression Helpers ───────────────────────────────────────────────\n\ndef partial_corr_manual(x, y, covar):\n    Xc = sm.add_constant(covar)\n    rx = sm.OLS(x, Xc).fit().resid\n    ry = sm.OLS(y, Xc).fit().resid\n    r, p = stats.pearsonr(rx, ry)\n    return float(r), float(p)\n\n\ntry:\n    import pingouin as pg\n    import pandas as pd\n\n    def partial_corr_fn(x, y, covar):\n        df = pd.DataFrame({\"x\": x, \"y\": y, \"z\": covar})\n        res = pg.partial_corr(data=df, x=\"x\", y=\"y\", covar=\"z\")\n        return float(res[\"r\"].values[0]), float(res[\"p-val\"].values[0])\n    logger.info(\"Using pingouin for partial correlation\")\nexcept ImportError:\n    partial_corr_fn = partial_corr_manual\n    logger.info(\"pingouin not available, using manual partial correlation\")\n\n\ndef beta_regression_mle(y_raw, X):\n    y = np.clip(y_raw, 1e-6, 1 - 1e-6)\n    n, k = X.shape\n\n    def neg_ll(params):\n        beta = params[:k]\n        phi = np.exp(params[k])\n        mu = 1.0 / (1.0 + np.exp(-(X @ beta)))\n        a = mu * phi\n        b = (1.0 - mu) * phi\n        return -np.sum(\n            special.gammaln(phi) - special.gammaln(a) - special.gammaln(b)\n            + (a - 1.0) * np.log(y) + (b - 1.0) * np.log(1.0 - y)\n        )\n\n    y_logit = np.log(y / (1.0 - y))\n    x0 = np.zeros(k + 1)\n    try:\n        init_fit = sm.OLS(y_logit, X).fit()\n        x0[:k] = init_fit.params\n    except Exception:\n        pass\n    x0[k] = np.log(10.0)\n\n    with warnings.catch_warnings():\n        warnings.simplefilter(\"ignore\")\n        res = optimize.minimize(neg_ll, x0, method=\"L-BFGS-B\",\n                                options={\"maxiter\": 5000, \"ftol\": 1e-12})\n    if not res.success:\n        return None\n\n    n_p = len(res.x)\n    H = np.zeros((n_p, n_p))\n    eps_h = 1e-5\n    for i in range(n_p):\n        for j in range(i, n_p):\n            ei = np.zeros(n_p)\n            ej = np.zeros(n_p)\n            ei[i] = eps_h\n            ej[j] = eps_h\n            fpp = neg_ll(res.x + ei + ej)\n            fpm = neg_ll(res.x + ei - ej)\n            fmp = neg_ll(res.x - ei + ej)\n            fmm = neg_ll(res.x - ei - ej)\n            H[i, j] = H[j, i] = (fpp - fpm - fmp + fmm) / (4.0 * eps_h * eps_h)\n\n    try:\n        cov = np.linalg.inv(H)\n        se = np.sqrt(np.maximum(np.diag(cov), 0.0))\n    except np.linalg.LinAlgError:\n        return None\n\n    beta = res.x[:k]\n    se_b = se[:k]\n    z = beta / np.maximum(se_b, 1e-12)\n    pvals = 2.0 * (1.0 - stats.norm.cdf(np.abs(z)))\n    return {\"beta\": beta, \"se\": se_b, \"z\": z, \"p\": pvals}\n\n\ndef run_condition_analysis(panel_asrs, keffs, eta_maxs):\n    n = len(panel_asrs)\n    y = np.log(panel_asrs + EPS)\n    x1 = np.log(keffs)\n    x2 = np.log(eta_maxs + EPS)\n    X = np.column_stack([x1, x2])\n    Xc = sm.add_constant(X)\n    results = {}\n\n    fit = sm.OLS(y, Xc).fit()\n    results[\"ols\"] = {\n        \"keff_beta\": float(fit.params[1]),\n        \"keff_t\": float(fit.tvalues[1]),\n        \"keff_p\": float(fit.pvalues[1]),\n        \"eta_max_beta\": float(fit.params[2]),\n        \"eta_max_t\": float(fit.tvalues[2]),\n        \"eta_max_p\": float(fit.pvalues[2]),\n        \"R2\": float(fit.rsquared),\n        \"adj_R2\": float(fit.rsquared_adj),\n        \"f_stat\": float(fit.fvalue) if np.isfinite(fit.fvalue) else None,\n        \"f_pvalue\": float(fit.f_pvalue) if np.isfinite(fit.f_pvalue) else None,\n    }\n\n    results[\"vif_keff\"] = float(variance_inflation_factor(Xc, 1))\n    results[\"vif_eta_max\"] = float(variance_inflation_factor(Xc, 2))\n\n    pr, pp = partial_corr_fn(x1, y, x2)\n    results[\"partial_r_keff\"] = pr\n    results[\"partial_r_keff_p\"] = pp\n\n    Xz = sm.add_constant(x2)\n    resid_keff = sm.OLS(x1, Xz).fit().resid\n    Xr = sm.add_constant(resid_keff)\n    fit_r = sm.OLS(y, Xr).fit()\n    results[\"residualized_keff_beta\"] = float(fit_r.params[1])\n    results[\"residualized_keff_t\"] = float(fit_r.tvalues[1])\n    results[\"residualized_keff_p\"] = float(fit_r.pvalues[1])\n\n    y_raw = np.clip(panel_asrs, 0.0, 1.0)\n    br = beta_regression_mle(y_raw, Xc)\n    if br is not None:\n        results[\"beta_reg_keff_beta\"] = float(br[\"beta\"][1])\n        results[\"beta_reg_keff_p\"] = float(br[\"p\"][1])\n        results[\"beta_reg_eta_max_beta\"] = float(br[\"beta\"][2])\n        results[\"beta_reg_eta_max_p\"] = float(br[\"p\"][2])\n    else:\n        results[\"beta_reg_keff_p\"] = None\n        results[\"beta_reg_eta_max_p\"] = None\n\n    return results\n\n\n# ── Main ─────────────────────────────────────────────────────────────\n\ndef main():\n    logger.info(\"=\" * 60)\n    logger.info(\"Plan 001 Step 4: Panel Regression (455 panels x 12 conditions)\")\n    logger.info(\"=\" * 60)\n\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    logger.info(\"\\nPrecomputing individual ASR...\")\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    logger.info(f\"  Computed {len(ind_asr)} individual ASR values\")\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n    logger.info(f\"  Total panels: {len(all_combos)}\")\n\n    condition_results = {}\n    raw_eta_ps = []\n    raw_keff_ps = []\n    valid_cond_keys = []\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        for atk in ATTACKS:\n            cond = f\"{ds}x{atk}\"\n            logger.info(f\"\\n--- {cond} ---\")\n\n            p_asrs, p_keffs, p_etas = [], [], []\n            skipped = 0\n\n            for combo in all_combos:\n                jids = [ALL_MODELS[i] for i in combo]\n\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    skipped += 1\n                    continue\n                pk = \"|\".join(jids)\n                if pk not in keff_data:\n                    skipped += 1\n                    continue\n\n                keff = keff_data[pk][\"keff\"]\n                etas = [ind_asr[(ds, atk, j)] for j in jids]\n                eta_max = max(etas)\n\n                cs = {j: clean[ds][j] for j in jids}\n                ats = {j: attacked[ds][atk][j] for j in jids}\n                p_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n                p_asrs.append(p_asr)\n                p_keffs.append(keff)\n                p_etas.append(eta_max)\n\n            n_panels = len(p_asrs)\n            logger.info(f\"  {n_panels} panels with data, {skipped} skipped\")\n\n            if n_panels < 10:\n                logger.warning(f\"  Too few panels ({n_panels}), skipping\")\n                condition_results[cond] = {\"n_panels\": n_panels, \"skipped\": True}\n                continue\n\n            p_asrs = np.array(p_asrs)\n            p_keffs = np.array(p_keffs)\n            p_etas = np.array(p_etas)\n\n            if np.std(p_asrs) < 1e-10:\n                logger.warning(f\"  Constant ASR ({p_asrs[0]:.4f}), skipping regression\")\n                condition_results[cond] = {\n                    \"n_panels\": n_panels, \"skipped\": True,\n                    \"reason\": \"constant_asr\", \"asr_value\": float(p_asrs[0]),\n                }\n                continue\n\n            cond_res = run_condition_analysis(p_asrs, p_keffs, p_etas)\n            cond_res[\"n_panels\"] = n_panels\n            cond_res[\"skipped\"] = False\n            cond_res[\"asr_stats\"] = {\n                \"mean\": float(np.mean(p_asrs)),\n                \"std\": float(np.std(p_asrs)),\n                \"min\": float(np.min(p_asrs)),\n                \"max\": float(np.max(p_asrs)),\n                \"pct_zero\": float(np.mean(p_asrs == 0)),\n            }\n            condition_results[cond] = cond_res\n\n            raw_eta_ps.append(cond_res[\"ols\"][\"eta_max_p\"])\n            raw_keff_ps.append(cond_res[\"ols\"][\"keff_p\"])\n            valid_cond_keys.append(cond)\n\n            ols = cond_res[\"ols\"]\n            sig_k = \"***\" if ols[\"keff_p\"] < 0.001 else \"**\" if ols[\"keff_p\"] < 0.01 else \"*\" if ols[\"keff_p\"] < 0.05 else \"ns\"\n            sig_e = \"***\" if ols[\"eta_max_p\"] < 0.001 else \"**\" if ols[\"eta_max_p\"] < 0.01 else \"*\" if ols[\"eta_max_p\"] < 0.05 else \"ns\"\n            logger.info(\n                f\"  OLS R2={ols['R2']:.4f}  \"\n                f\"K_eff: B={ols['keff_beta']:+.4f} p={ols['keff_p']:.4f} {sig_k}  \"\n                f\"eta_max: B={ols['eta_max_beta']:+.4f} p={ols['eta_max_p']:.4f} {sig_e}\"\n            )\n            logger.info(\n                f\"  VIF: K_eff={cond_res['vif_keff']:.2f}, eta_max={cond_res['vif_eta_max']:.2f}\"\n            )\n            logger.info(\n                f\"  Partial r(K_eff|eta_max)={cond_res['partial_r_keff']:.4f} \"\n                f\"p={cond_res['partial_r_keff_p']:.4f}\"\n            )\n            logger.info(\n                f\"  Residualized K_eff: B={cond_res['residualized_keff_beta']:+.4f} \"\n                f\"p={cond_res['residualized_keff_p']:.4f}\"\n            )\n\n    # ── Multiple testing corrections ──\n    if raw_eta_ps:\n        _, bonf_eta, _, _ = multipletests(raw_eta_ps, method=\"bonferroni\")\n        _, fdr_eta, _, _ = multipletests(raw_eta_ps, method=\"fdr_bh\")\n        _, bonf_keff, _, _ = multipletests(raw_keff_ps, method=\"bonferroni\")\n        _, fdr_keff, _, _ = multipletests(raw_keff_ps, method=\"fdr_bh\")\n\n        for i, ck in enumerate(valid_cond_keys):\n            condition_results[ck][\"eta_max_bonferroni_p\"] = float(bonf_eta[i])\n            condition_results[ck][\"eta_max_fdr_p\"] = float(fdr_eta[i])\n            condition_results[ck][\"keff_bonferroni_p\"] = float(bonf_keff[i])\n            condition_results[ck][\"keff_fdr_p\"] = float(fdr_keff[i])\n\n    # ── Summary ──\n    valid = [condition_results[k] for k in valid_cond_keys]\n    nv = len(valid)\n    summary = {}\n    if nv > 0:\n        summary = {\n            \"keff_sig_negative_count\": (\n                f\"{sum(1 for r in valid if r['ols']['keff_beta'] < 0 and r['ols']['keff_p'] < 0.05)}/{nv}\"\n            ),\n            \"keff_residualized_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('residualized_keff_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"eta_max_bonferroni_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('eta_max_bonferroni_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"eta_max_fdr_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('eta_max_fdr_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"mean_vif_keff\": float(np.mean([r[\"vif_keff\"] for r in valid])),\n            \"mean_R2\": float(np.mean([r[\"ols\"][\"R2\"] for r in valid])),\n        }\n\n    output = {\n        \"n_panels\": 455,\n        \"n_models\": len(ALL_MODELS),\n        \"models\": ALL_MODELS,\n        \"datasets\": DATASETS,\n        \"attacks\": ATTACKS,\n        \"conditions\": condition_results,\n        \"summary\": summary,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    out_path = OUTPUT_DIR / \"step4_regression_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    logger.info(f\"\\nResults saved: {out_path}\")\n\n    logger.info(\"\\n\" + \"=\" * 60)\n    logger.info(\"SUMMARY\")\n    logger.info(\"=\" * 60)\n    for k, v in summary.items():\n        logger.info(f\"  {k}: {v}\")\n\n    logger.info(f\"\\n{'Condition':<35} {'R2':>6} {'K_eff B':>9} {'K_eff p':>9} {'eta_max B':>9} {'eta_max p':>9} {'VIF':>5}\")\n    logger.info(\"-\" * 90)\n    for ck in valid_cond_keys:\n        r = condition_results[ck]\n        o = r[\"ols\"]\n        logger.info(\n            f\"  {ck:<33} {o['R2']:>6.3f} {o['keff_beta']:>+9.4f} {o['keff_p']:>9.4f} \"\n            f\"{o['eta_max_beta']:>+9.4f} {o['eta_max_p']:>9.4f} {r['vif_keff']:>5.1f}\"\n        )\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "0a2a3ce1-2317-4f4f-8610-692f4e3299db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uaes55sArjYoKj59Yfu2YX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6159,
      "cache_read_input_tokens": 83145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6159
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

_source line 60 · 2026-05-22T15:01:55.891Z_

<details><summary>↩ Tool result · `toolu_0164FBKizJsxhbPvFBttv2ew`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "de64d433-9f71-44fb-8035-f95e07d472f8",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 4: Panel regression -- 455 panels x 12 conditions.\n\nInput:\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\n\nOutput:\n  - artifacts/results/plan001/panel_regression/step4_regression_results.json\n\nDependencies: numpy, scipy, statsmodels\nOptional: pingouin (for partial_corr; manual fallback included)\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport warnings\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy import optimize, stats, special\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\nfrom statsmodels.stats.multitest import multipletests\n\nfrom src.utils import setup_logging\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,\n    load_all_scores, load_pairs, load_mi_data,\n)\n\nlogger = setup_logging(\"plan001_step4\")\n\nEPS = 0.001\n\n\n# ── JSON Helper ──────────────────────────────────────────────────────\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\n# ── ASR Computation ──────────────────────────────────────────────────\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\n# ── Regression Helpers ───────────────────────────────────────────────\n\ndef partial_corr_manual(x, y, covar):\n    Xc = sm.add_constant(covar)\n    rx = sm.OLS(x, Xc).fit().resid\n    ry = sm.OLS(y, Xc).fit().resid\n    r, p = stats.pearsonr(rx, ry)\n    return float(r), float(p)\n\n\ntry:\n    import pingouin as pg\n    import pandas as pd\n\n    def partial_corr_fn(x, y, covar):\n        df = pd.DataFrame({\"x\": x, \"y\": y, \"z\": covar})\n        res = pg.partial_corr(data=df, x=\"x\", y=\"y\", covar=\"z\")\n        return float(res[\"r\"].values[0]), float(res[\"p-val\"].values[0])\n    logger.info(\"Using pingouin for partial correlation\")\nexcept ImportError:\n    partial_corr_fn = partial_corr_manual\n    logger.info(\"pingouin not available, using manual partial correlation\")\n\n\ndef beta_regression_mle(y_raw, X):\n    y = np.clip(y_raw, 1e-6, 1 - 1e-6)\n    n, k = X.shape\n\n    def neg_ll(params):\n        beta = params[:k]\n        phi = np.exp(params[k])\n        mu = 1.0 / (1.0 + np.exp(-(X @ beta)))\n        a = mu * phi\n        b = (1.0 - mu) * phi\n        return -np.sum(\n            special.gammaln(phi) - special.gammaln(a) - special.gammaln(b)\n            + (a - 1.0) * np.log(y) + (b - 1.0) * np.log(1.0 - y)\n        )\n\n    y_logit = np.log(y / (1.0 - y))\n    x0 = np.zeros(k + 1)\n    try:\n        init_fit = sm.OLS(y_logit, X).fit()\n        x0[:k] = init_fit.params\n    except Exception:\n        pass\n    x0[k] = np.log(10.0)\n\n    with warnings.catch_warnings():\n        warnings.simplefilter(\"ignore\")\n        res = optimize.minimize(neg_ll, x0, method=\"L-BFGS-B\",\n                                options={\"maxiter\": 5000, \"ftol\": 1e-12})\n    if not res.success:\n        return None\n\n    n_p = len(res.x)\n    H = np.zeros((n_p, n_p))\n    eps_h = 1e-5\n    for i in range(n_p):\n        for j in range(i, n_p):\n            ei = np.zeros(n_p)\n            ej = np.zeros(n_p)\n            ei[i] = eps_h\n            ej[j] = eps_h\n            fpp = neg_ll(res.x + ei + ej)\n            fpm = neg_ll(res.x + ei - ej)\n            fmp = neg_ll(res.x - ei + ej)\n            fmm = neg_ll(res.x - ei - ej)\n            H[i, j] = H[j, i] = (fpp - fpm - fmp + fmm) / (4.0 * eps_h * eps_h)\n\n    try:\n        cov = np.linalg.inv(H)\n        se = np.sqrt(np.maximum(np.diag(cov), 0.0))\n    except np.linalg.LinAlgError:\n        return None\n\n    beta = res.x[:k]\n    se_b = se[:k]\n    z = beta / np.maximum(se_b, 1e-12)\n    pvals = 2.0 * (1.0 - stats.norm.cdf(np.abs(z)))\n    return {\"beta\": beta, \"se\": se_b, \"z\": z, \"p\": pvals}\n\n\ndef run_condition_analysis(panel_asrs, keffs, eta_maxs):\n    n = len(panel_asrs)\n    y = np.log(panel_asrs + EPS)\n    x1 = np.log(keffs)\n    x2 = np.log(eta_maxs + EPS)\n    X = np.column_stack([x1, x2])\n    Xc = sm.add_constant(X)\n    results = {}\n\n    fit = sm.OLS(y, Xc).fit()\n    results[\"ols\"] = {\n        \"keff_beta\": float(fit.params[1]),\n        \"keff_t\": float(fit.tvalues[1]),\n        \"keff_p\": float(fit.pvalues[1]),\n        \"eta_max_beta\": float(fit.params[2]),\n        \"eta_max_t\": float(fit.tvalues[2]),\n        \"eta_max_p\": float(fit.pvalues[2]),\n        \"R2\": float(fit.rsquared),\n        \"adj_R2\": float(fit.rsquared_adj),\n        \"f_stat\": float(fit.fvalue) if np.isfinite(fit.fvalue) else None,\n        \"f_pvalue\": float(fit.f_pvalue) if np.isfinite(fit.f_pvalue) else None,\n    }\n\n    results[\"vif_keff\"] = float(variance_inflation_factor(Xc, 1))\n    results[\"vif_eta_max\"] = float(variance_inflation_factor(Xc, 2))\n\n    pr, pp = partial_corr_fn(x1, y, x2)\n    results[\"partial_r_keff\"] = pr\n    results[\"partial_r_keff_p\"] = pp\n\n    Xz = sm.add_constant(x2)\n    resid_keff = sm.OLS(x1, Xz).fit().resid\n    Xr = sm.add_constant(resid_keff)\n    fit_r = sm.OLS(y, Xr).fit()\n    results[\"residualized_keff_beta\"] = float(fit_r.params[1])\n    results[\"residualized_keff_t\"] = float(fit_r.tvalues[1])\n    results[\"residualized_keff_p\"] = float(fit_r.pvalues[1])\n\n    y_raw = np.clip(panel_asrs, 0.0, 1.0)\n    br = beta_regression_mle(y_raw, Xc)\n    if br is not None:\n        results[\"beta_reg_keff_beta\"] = float(br[\"beta\"][1])\n        results[\"beta_reg_keff_p\"] = float(br[\"p\"][1])\n        results[\"beta_reg_eta_max_beta\"] = float(br[\"beta\"][2])\n        results[\"beta_reg_eta_max_p\"] = float(br[\"p\"][2])\n    else:\n        results[\"beta_reg_keff_p\"] = None\n        results[\"beta_reg_eta_max_p\"] = None\n\n    return results\n\n\n# ── Main ─────────────────────────────────────────────────────────────\n\ndef main():\n    logger.info(\"=\" * 60)\n    logger.info(\"Plan 001 Step 4: Panel Regression (455 panels x 12 conditions)\")\n    logger.info(\"=\" * 60)\n\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    logger.info(\"\\nPrecomputing individual ASR...\")\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    logger.info(f\"  Computed {len(ind_asr)} individual ASR values\")\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n    logger.info(f\"  Total panels: {len(all_combos)}\")\n\n    condition_results = {}\n    raw_eta_ps = []\n    raw_keff_ps = []\n    valid_cond_keys = []\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        for atk in ATTACKS:\n            cond = f\"{ds}x{atk}\"\n            logger.info(f\"\\n--- {cond} ---\")\n\n            p_asrs, p_keffs, p_etas = [], [], []\n            skipped = 0\n\n            for combo in all_combos:\n                jids = [ALL_MODELS[i] for i in combo]\n\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    skipped += 1\n                    continue\n                pk = \"|\".join(jids)\n                if pk not in keff_data:\n                    skipped += 1\n                    continue\n\n                keff = keff_data[pk][\"keff\"]\n                etas = [ind_asr[(ds, atk, j)] for j in jids]\n                eta_max = max(etas)\n\n                cs = {j: clean[ds][j] for j in jids}\n                ats = {j: attacked[ds][atk][j] for j in jids}\n                p_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n                p_asrs.append(p_asr)\n                p_keffs.append(keff)\n                p_etas.append(eta_max)\n\n            n_panels = len(p_asrs)\n            logger.info(f\"  {n_panels} panels with data, {skipped} skipped\")\n\n            if n_panels < 10:\n                logger.warning(f\"  Too few panels ({n_panels}), skipping\")\n                condition_results[cond] = {\"n_panels\": n_panels, \"skipped\": True}\n                continue\n\n            p_asrs = np.array(p_asrs)\n            p_keffs = np.array(p_keffs)\n            p_etas = np.array(p_etas)\n\n            if np.std(p_asrs) < 1e-10:\n                logger.warning(f\"  Constant ASR ({p_asrs[0]:.4f}), skipping regression\")\n                condition_results[cond] = {\n                    \"n_panels\": n_panels, \"skipped\": True,\n                    \"reason\": \"constant_asr\", \"asr_value\": float(p_asrs[0]),\n                }\n                continue\n\n            cond_res = run_condition_analysis(p_asrs, p_keffs, p_etas)\n            cond_res[\"n_panels\"] = n_panels\n            cond_res[\"skipped\"] = False\n            cond_res[\"asr_stats\"] = {\n                \"mean\": float(np.mean(p_asrs)),\n                \"std\": float(np.std(p_asrs)),\n                \"min\": float(np.min(p_asrs)),\n                \"max\": float(np.max(p_asrs)),\n                \"pct_zero\": float(np.mean(p_asrs == 0)),\n            }\n            condition_results[cond] = cond_res\n\n            raw_eta_ps.append(cond_res[\"ols\"][\"eta_max_p\"])\n            raw_keff_ps.append(cond_res[\"ols\"][\"keff_p\"])\n            valid_cond_keys.append(cond)\n\n            ols = cond_res[\"ols\"]\n            sig_k = \"***\" if ols[\"keff_p\"] < 0.001 else \"**\" if ols[\"keff_p\"] < 0.01 else \"*\" if ols[\"keff_p\"] < 0.05 else \"ns\"\n            sig_e = \"***\" if ols[\"eta_max_p\"] < 0.001 else \"**\" if ols[\"eta_max_p\"] < 0.01 else \"*\" if ols[\"eta_max_p\"] < 0.05 else \"ns\"\n            logger.info(\n                f\"  OLS R2={ols['R2']:.4f}  \"\n                f\"K_eff: B={ols['keff_beta']:+.4f} p={ols['keff_p']:.4f} {sig_k}  \"\n                f\"eta_max: B={ols['eta_max_beta']:+.4f} p={ols['eta_max_p']:.4f} {sig_e}\"\n            )\n            logger.info(\n                f\"  VIF: K_eff={cond_res['vif_keff']:.2f}, eta_max={cond_res['vif_eta_max']:.2f}\"\n            )\n            logger.info(\n                f\"  Partial r(K_eff|eta_max)={cond_res['partial_r_keff']:.4f} \"\n                f\"p={cond_res['partial_r_keff_p']:.4f}\"\n            )\n            logger.info(\n                f\"  Residualized K_eff: B={cond_res['residualized_keff_beta']:+.4f} \"\n                f\"p={cond_res['residualized_keff_p']:.4f}\"\n            )\n\n    # ── Multiple testing corrections ──\n    if raw_eta_ps:\n        _, bonf_eta, _, _ = multipletests(raw_eta_ps, method=\"bonferroni\")\n        _, fdr_eta, _, _ = multipletests(raw_eta_ps, method=\"fdr_bh\")\n        _, bonf_keff, _, _ = multipletests(raw_keff_ps, method=\"bonferroni\")\n        _, fdr_keff, _, _ = multipletests(raw_keff_ps, method=\"fdr_bh\")\n\n        for i, ck in enumerate(valid_cond_keys):\n            condition_results[ck][\"eta_max_bonferroni_p\"] = float(bonf_eta[i])\n            condition_results[ck][\"eta_max_fdr_p\"] = float(fdr_eta[i])\n            condition_results[ck][\"keff_bonferroni_p\"] = float(bonf_keff[i])\n            condition_results[ck][\"keff_fdr_p\"] = float(fdr_keff[i])\n\n    # ── Summary ──\n    valid = [condition_results[k] for k in valid_cond_keys]\n    nv = len(valid)\n    summary = {}\n    if nv > 0:\n        summary = {\n            \"keff_sig_negative_count\": (\n                f\"{sum(1 for r in valid if r['ols']['keff_beta'] < 0 and r['ols']['keff_p'] < 0.05)}/{nv}\"\n            ),\n            \"keff_residualized_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('residualized_keff_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"eta_max_bonferroni_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('eta_max_bonferroni_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"eta_max_fdr_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('eta_max_fdr_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"mean_vif_keff\": float(np.mean([r[\"vif_keff\"] for r in valid])),\n            \"mean_R2\": float(np.mean([r[\"ols\"][\"R2\"] for r in valid])),\n        }\n\n    output = {\n        \"n_panels\": 455,\n        \"n_models\": len(ALL_MODELS),\n        \"models\": ALL_MODELS,\n        \"datasets\": DATASETS,\n        \"attacks\": ATTACKS,\n        \"conditions\": condition_results,\n        \"summary\": summary,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    out_path = OUTPUT_DIR / \"step4_regression_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    logger.info(f\"\\nResults saved: {out_path}\")\n\n    logger.info(\"\\n\" + \"=\" * 60)\n    logger.info(\"SUMMARY\")\n    logger.info(\"=\" * 60)\n    for k, v in summary.items():\n        logger.info(f\"  {k}: {v}\")\n\n    logger.info(f\"\\n{'Condition':<35} {'R2':>6} {'K_eff B':>9} {'K_eff p':>9} {'eta_max B':>9} {'eta_max p':>9} {'VIF':>5}\")\n    logger.info(\"-\" * 90)\n    for ck in valid_cond_keys:\n        r = condition_results[ck]\n        o = r[\"ols\"]\n        logger.info(\n            f\"  {ck:<33} {o['R2']:>6.3f} {o['keff_beta']:>+9.4f} {o['keff_p']:>9.4f} \"\n            f\"{o['eta_max_beta']:>+9.4f} {o['eta_max_p']:>9.4f} {r['vif_keff']:>5.1f}\"\n        )\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " #!/usr/bin/env python3",
          "-\"\"\"Plan 001 Step 4: Panel regression — 455 panels × 12 conditions.",
          "+\"\"\"Plan 001 Step 4: Panel regression -- 455 panels x 12 conditions.",
          " ",
          " Input:",
          "   - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json"
        ]
      },
      {
        "oldStart": 30,
        "oldLines": 38,
        "newStart": 30,
        "newLines": 16,
        "lines": [
          " from statsmodels.stats.multitest import multipletests",
          " ",
          " from src.utils import setup_logging",
          "+from src.unified_data_loader import (",
          "+    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,",
          "+    load_all_scores, load_pairs, load_mi_data,",
          "+)",
          " ",
          " logger = setup_logging(\"plan001_step4\")",
          " ",
          "-# ── Constants ────────────────────────────────────────────────────────",
          "-LOCAL_MODELS = [",
          "-    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",",
          "-    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",",
          "-]",
          "-API_MODELS = [",
          "-    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",",
          "-    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",",
          "-    \"gpt-4o-mini\", \"claude-3-haiku\",",
          "-]",
          "-ALL_MODELS = LOCAL_MODELS + API_MODELS",
          "-DATASETS = [\"mmlu\", \"arc_challenge\"]",
          "-ATTACKS = [",
          "-    \"prompt_injection\", \"sycophancy\", \"score_manipulation\",",
          "-    \"verbosity_bias\", \"position_bias\", \"authority_bias\",",
          "-]",
          " EPS = 0.001",
          " ",
          "-RESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")",
          "-PLAN001_DIR = RESULTS_DIR / \"plan001\"",
          "-SCORES_DIR = PLAN001_DIR / \"individual_scores\"",
          "-MI_PATH = PLAN001_DIR / \"mi_matrix\" / \"mi_matrix_15models.json\"",
          "-CKPT_FILES = [",
          "-    RESULTS_DIR / \"_taxonomy_checkpoint.json\",",
          "-    RESULTS_DIR / \"_step2v3_checkpoint.json\",",
          "-]",
          "-OUTPUT_DIR = PLAN001_DIR / \"panel_regression\"",
          " ",
          "-",
          " # ── JSON Helper ──────────────────────────────────────────────────────",
          " ",
          " def _json_default(obj):"
        ]
      },
      {
        "oldStart": 77,
        "oldLines": 99,
        "newStart": 55,
        "newLines": 6,
        "lines": [
          "     raise TypeError(f\"Not JSON serializable: {type(obj)}\")",
          " ",
          " ",
          "-# ── Data Loading ─────────────────────────────────────────────────────",
          "-",
          "-def load_mi_data():",
          "-    if not MI_PATH.exists():",
          "-        logger.error(f\"MI matrix not found: {MI_PATH}\")",
          "-        logger.error(\"Run Step 3 first: scripts/run_plan001_step3_mi_matrix.py\")",
          "-        sys.exit(1)",
          "-    with open(MI_PATH) as f:",
          "-        data = json.load(f)",
          "-    logger.info(f\"Loaded MI matrix: {len(data['models'])} models\")",
          "-    return data",
          "-",
          "-",
          "-def load_pairs():",
          "-    for ckpt_path in CKPT_FILES:",
          "-        if not ckpt_path.exists():",
          "-            continue",
          "-        with open(ckpt_path) as f:",
          "-            data = json.load(f)",
          "-        if \"pairs\" not in data:",
          "-            continue",
          "-        pairs = {}",
          "-        for ds in DATASETS:",
          "-            if ds in data[\"pairs\"]:",
          "-                pairs[ds] = data[\"pairs\"][ds][:300]",
          "-                logger.info(f\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\")",
          "-        if pairs:",
          "-            return pairs",
          "-    logger.error(\"No pairs found in any checkpoint file\")",
          "-    sys.exit(1)",
          "-",
          "-",
          "-def _invert_winners(scores):",
          "-    \"\"\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\"\"\"",
          "-    swap = {\"A\": \"B\", \"B\": \"A\", \"tie\": \"tie\"}",
          "-    return [{**s, \"winner\": swap.get(s.get(\"winner\", \"tie\"), \"tie\")} for s in scores]",
          "-",
          "-",
          "-def load_all_scores():",
          "-    \"\"\"Load sample-level clean + attacked scores for all 15 models.",
          "-",
          "-    Returns:",
          "-        clean[ds][model_id] = [{\"winner\": ..., ...}, ...]",
          "-        attacked[ds][atk][model_id] = [{\"winner\": ..., ...}, ...]",
          "-    \"\"\"",
          "-    clean = {ds: {} for ds in DATASETS}",
          "-    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}",
          "-",
          "-    for ckpt_path in CKPT_FILES:",
          "-        if not ckpt_path.exists():",
          "-            continue",
          "-        logger.info(f\"Loading checkpoint: {ckpt_path.name}\")",
          "-        with open(ckpt_path) as f:",
          "-            data = json.load(f)",
          "-        for ds in DATASETS:",
          "-            for mid, scores in data.get(\"clean_scores\", {}).get(ds, {}).items():",
          "-                if mid not in clean[ds]:",
          "-                    clean[ds][mid] = scores",
          "-            for atk in ATTACKS:",
          "-                for mid, scores in data.get(\"attacked_scores\", {}).get(ds, {}).get(atk, {}).items():",
          "-                    if mid not in attacked[ds][atk]:",
          "-                        if atk == \"position_bias\":",
          "-                            scores = _invert_winners(scores)",
          "-                        attacked[ds][atk][mid] = scores",
          "-",
          "-    if SCORES_DIR.exists():",
          "-        logger.info(f\"Loading individual scores from {SCORES_DIR}\")",
          "-        for mid in ALL_MODELS:",
          "-            for ds in DATASETS:",
          "-                fp = SCORES_DIR / f\"{mid}__{ds}__clean.json\"",
          "-                if fp.exists() and mid not in clean[ds]:",
          "-                    with open(fp) as f:",
          "-                        clean[ds][mid] = json.load(f).get(\"scores\", [])",
          "-                for atk in ATTACKS:",
          "-                    fp = SCORES_DIR / f\"{mid}__{ds}__{atk}.json\"",
          "-                    if fp.exists() and mid not in attacked[ds][atk]:",
          "-                        with open(fp) as f:",
          "-                            scores = json.load(f).get(\"scores\", [])",
          "-                        if atk == \"position_bias\":",
          "-                            scores = _invert_winners(scores)",
          "-                        attacked[ds][atk][mid] = scores",
          "-",
          "-    for ds in DATASETS:",
          "-        nc = len(clean[ds])",
          "-        logger.info(f\"  {ds} clean: {nc}/{len(ALL_MODELS)}\")",
          "-        for atk in ATTACKS:",
          "-            na = len(attacked[ds][atk])",
          "-            if na > 0:",
          "-                logger.info(f\"  {ds} {atk}: {na}/{len(ALL_MODELS)}\")",
          "-",
          "-    return clean, attacked",
          "-",
          "-",
          " # ── ASR Computation ──────────────────────────────────────────────────",
          " ",
          " def majority_vote(votes):"
        ]
      },
      {
        "oldStart": 216,
        "oldLines": 7,
        "newStart": 101,
        "newLines": 6,
        "lines": [
          " # ── Regression Helpers ───────────────────────────────────────────────",
          " ",
          " def partial_corr_manual(x, y, covar):",
          "-    \"\"\"Partial correlation of x and y, controlling for covar.\"\"\"",
          "     Xc = sm.add_constant(covar)",
          "     rx = sm.OLS(x, Xc).fit().resid",
          "     ry = sm.OLS(y, Xc).fit().resid"
        ]
      },
      {
        "oldStart": 239,
        "oldLines": 9,
        "newStart": 123,
        "newLines": 6,
        "lines": [
          " ",
          " ",
          " def beta_regression_mle(y_raw, X):",
          "-    \"\"\"Beta regression via MLE. y in (0,1), logit link.",
          "-    X should include constant column.",
          "-    Returns dict with coefficients/p-values or None on failure.\"\"\"",
          "     y = np.clip(y_raw, 1e-6, 1 - 1e-6)",
          "     n, k = X.shape",
          " "
        ]
      },
      {
        "oldStart": 256,
        "oldLines": 7,
        "newStart": 137,
        "newLines": 6,
        "lines": [
          "             + (a - 1.0) * np.log(y) + (b - 1.0) * np.log(1.0 - y)",
          "         )",
          " ",
          "-    # Initial values from OLS on logit(y)",
          "     y_logit = np.log(y / (1.0 - y))",
          "     x0 = np.zeros(k + 1)",
          "     try:"
        ]
      },
      {
        "oldStart": 273,
        "oldLines": 7,
        "newStart": 153,
        "newLines": 6,
        "lines": [
          "     if not res.success:",
          "         return None",
          " ",
          "-    # Numerical Hessian for standard errors",
          "     n_p = len(res.x)",
          "     H = np.zeros((n_p, n_p))",
          "     eps_h = 1e-5"
        ]
      },
      {
        "oldStart": 303,
        "oldLines": 7,
        "newStart": 182,
        "newLines": 6,
        "lines": [
          " ",
          " ",
          " def run_condition_analysis(panel_asrs, keffs, eta_maxs):",
          "-    \"\"\"Full regression suite for one condition. All arrays shape (n,).\"\"\"",
          "     n = len(panel_asrs)",
          "     y = np.log(panel_asrs + EPS)",
          "     x1 = np.log(keffs)"
        ]
      },
      {
        "oldStart": 312,
        "oldLines": 7,
        "newStart": 190,
        "newLines": 6,
        "lines": [
          "     Xc = sm.add_constant(X)",
          "     results = {}",
          " ",
          "-    # ── OLS ──",
          "     fit = sm.OLS(y, Xc).fit()",
          "     results[\"ols\"] = {",
          "         \"keff_beta\": float(fit.params[1]),"
        ]
      },
      {
        "oldStart": 327,
        "oldLines": 16,
        "newStart": 204,
        "newLines": 13,
        "lines": [
          "         \"f_pvalue\": float(fit.f_pvalue) if np.isfinite(fit.f_pvalue) else None,",
          "     }",
          " ",
          "-    # ── VIF ──",
          "     results[\"vif_keff\"] = float(variance_inflation_factor(Xc, 1))",
          "     results[\"vif_eta_max\"] = float(variance_inflation_factor(Xc, 2))",
          " ",
          "-    # ── Partial correlation (K_eff | η_max) ──",
          "     pr, pp = partial_corr_fn(x1, y, x2)",
          "     results[\"partial_r_keff\"] = pr",
          "     results[\"partial_r_keff_p\"] = pp",
          " ",
          "-    # ── Residualized K_eff ──",
          "     Xz = sm.add_constant(x2)",
          "     resid_keff = sm.OLS(x1, Xz).fit().resid",
          "     Xr = sm.add_constant(resid_keff)"
        ]
      },
      {
        "oldStart": 345,
        "oldLines": 7,
        "newStart": 219,
        "newLines": 6,
        "lines": [
          "     results[\"residualized_keff_t\"] = float(fit_r.tvalues[1])",
          "     results[\"residualized_keff_p\"] = float(fit_r.pvalues[1])",
          " ",
          "-    # ── Beta regression ──",
          "     y_raw = np.clip(panel_asrs, 0.0, 1.0)",
          "     br = beta_regression_mle(y_raw, Xc)",
          "     if br is not None:"
        ]
      },
      {
        "oldStart": 364,
        "oldLines": 14,
        "newStart": 237,
        "newLines": 13,
        "lines": [
          " ",
          " def main():",
          "     logger.info(\"=\" * 60)",
          "-    logger.info(\"Plan 001 Step 4: Panel Regression (455 panels × 12 conditions)\")",
          "+    logger.info(\"Plan 001 Step 4: Panel Regression (455 panels x 12 conditions)\")",
          "     logger.info(\"=\" * 60)",
          " ",
          "     mi_data = load_mi_data()",
          "     pairs = load_pairs()",
          "     clean, attacked = load_all_scores()",
          " ",
          "-    # Precompute individual ASR for all model × condition",
          "     logger.info(\"\\nPrecomputing individual ASR...\")",
          "     ind_asr = {}",
          "     for ds in DATASETS:"
        ]
      },
      {
        "oldStart": 383,
        "oldLines": 7,
        "newStart": 255,
        "newLines": 6,
        "lines": [
          "                     )",
          "     logger.info(f\"  Computed {len(ind_asr)} individual ASR values\")",
          " ",
          "-    # Enumerate all C(15,3)=455 panels",
          "     all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))",
          "     logger.info(f\"  Total panels: {len(all_combos)}\")",
          " "
        ]
      },
      {
        "oldStart": 395,
        "oldLines": 7,
        "newStart": 266,
        "newLines": 7,
        "lines": [
          "     for ds in DATASETS:",
          "         keff_data = mi_data[\"keff_per_panel\"].get(ds, {})",
          "         for atk in ATTACKS:",
          "-            cond = f\"{ds}×{atk}\"",
          "+            cond = f\"{ds}x{atk}\"",
          "             logger.info(f\"\\n--- {cond} ---\")",
          " ",
          "             p_asrs, p_keffs, p_etas = [], [], []"
        ]
      },
      {
        "oldStart": 464,
        "oldLines": 19,
        "newStart": 335,
        "newLines": 19,
        "lines": [
          "             sig_k = \"***\" if ols[\"keff_p\"] < 0.001 else \"**\" if ols[\"keff_p\"] < 0.01 else \"*\" if ols[\"keff_p\"] < 0.05 else \"ns\"",
          "             sig_e = \"***\" if ols[\"eta_max_p\"] < 0.001 else \"**\" if ols[\"eta_max_p\"] < 0.01 else \"*\" if ols[\"eta_max_p\"] < 0.05 else \"ns\"",
          "             logger.info(",
          "-                f\"  OLS R²={ols['R2']:.4f}  \"",
          "-                f\"K_eff: β={ols['keff_beta']:+.4f} p={ols['keff_p']:.4f} {sig_k}  \"",
          "-                f\"η_max: β={ols['eta_max_beta']:+.4f} p={ols['eta_max_p']:.4f} {sig_e}\"",
          "+                f\"  OLS R2={ols['R2']:.4f}  \"",
          "+                f\"K_eff: B={ols['keff_beta']:+.4f} p={ols['keff_p']:.4f} {sig_k}  \"",
          "+                f\"eta_max: B={ols['eta_max_beta']:+.4f} p={ols['eta_max_p']:.4f} {sig_e}\"",
          "             )",
          "             logger.info(",
          "-                f\"  VIF: K_eff={cond_res['vif_keff']:.2f}, η_max={cond_res['vif_eta_max']:.2f}\"",
          "+                f\"  VIF: K_eff={cond_res['vif_keff']:.2f}, eta_max={cond_res['vif_eta_max']:.2f}\"",
          "             )",
          "             logger.info(",
          "-                f\"  Partial r(K_eff|η_max)={cond_res['partial_r_keff']:.4f} \"",
          "+                f\"  Partial r(K_eff|eta_max)={cond_res['partial_r_keff']:.4f} \"",
          "                 f\"p={cond_res['partial_r_keff_p']:.4f}\"",
          "             )",
          "             logger.info(",
          "-                f\"  Residualized K_eff: β={cond_res['residualized_keff_beta']:+.4f} \"",
          "+                f\"  Residualized K_eff: B={cond_res['residualized_keff_beta']:+.4f} \"",
          "                 f\"p={cond_res['residualized_keff_p']:.4f}\"",
          "             )",
          " "
        ]
      },
      {
        "oldStart": 537,
        "oldLines": 8,
        "newStart": 408,
        "newLines": 7,
        "lines": [
          "     for k, v in summary.items():",
          "         logger.info(f\"  {k}: {v}\")",
          " ",
          "-    # Per-condition table",
          "-    logger.info(f\"\\n{'Condition':<35} {'R²':>6} {'K_eff β':>9} {'K_eff p':>9} {'η_max β':>9} {'η_max p':>9} {'VIF':>5}\")",
          "+    logger.info(f\"\\n{'Condition':<35} {'R2':>6} {'K_eff B':>9} {'K_eff p':>9} {'eta_max B':>9} {'eta_max p':>9} {'VIF':>5}\")",
          "     logger.info(\"-\" * 90)",
          "     for ck in valid_cond_keys:",
          "         r = condition_results[ck]"
        ]
      }
    ],
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 4: Panel regression — 455 panels × 12 conditions.\n\nInput:\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\n\nOutput:\n  - artifacts/results/plan001/panel_regression/step4_regression_results.json\n\nDependencies: numpy, scipy, statsmodels\nOptional: pingouin (for partial_corr; manual fallback included)\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport warnings\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy import optimize, stats, special\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\nfrom statsmodels.stats.multitest import multipletests\n\nfrom src.utils import setup_logging\n\nlogger = setup_logging(\"plan001_step4\")\n\n# ── Constants ────────────────────────────────────────────────────────\nLOCAL_MODELS = [\n    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",\n    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",\n]\nAPI_MODELS = [\n    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",\n    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",\n    \"gpt-4o-mini\", \"claude-3-haiku\",\n]\nALL_MODELS = LOCAL_MODELS + API_MODELS\nDATASETS = [\"mmlu\", \"arc_challenge\"]\nATTACKS = [\n    \"prompt_injection\", \"sycophancy\", \"score_manipulation\",\n    \"verbosity_bias\", \"position_bias\", \"authority_bias\",\n]\nEPS = 0.001\n\nRESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")\nPLAN001_DIR = RESULTS_DIR / \"plan001\"\nSCORES_DIR = PLAN001_DIR / \"individual_scores\"\nMI_PATH = PLAN001_DIR / \"mi_matrix\" / \"mi_matrix_15models.json\"\nCKPT_FILES = [\n    RESULTS_DIR / \"_taxonomy_checkpoint.json\",\n    RESULTS_DIR / \"_step2v3_checkpoint.json\",\n]\nOUTPUT_DIR = PLAN001_DIR / \"panel_regression\"\n\n\n# ── JSON Helper ──────────────────────────────────────────────────────\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\n# ── Data Loading ─────────────────────────────────────────────────────\n\ndef load_mi_data():\n    if not MI_PATH.exists():\n        logger.error(f\"MI matrix not found: {MI_PATH}\")\n        logger.error(\"Run Step 3 first: scripts/run_plan001_step3_mi_matrix.py\")\n        sys.exit(1)\n    with open(MI_PATH) as f:\n        data = json.load(f)\n    logger.info(f\"Loaded MI matrix: {len(data['models'])} models\")\n    return data\n\n\ndef load_pairs():\n    for ckpt_path in CKPT_FILES:\n        if not ckpt_path.exists():\n            continue\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        if \"pairs\" not in data:\n            continue\n        pairs = {}\n        for ds in DATASETS:\n            if ds in data[\"pairs\"]:\n                pairs[ds] = data[\"pairs\"][ds][:300]\n                logger.info(f\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\")\n        if pairs:\n            return pairs\n    logger.error(\"No pairs found in any checkpoint file\")\n    sys.exit(1)\n\n\ndef _invert_winners(scores):\n    \"\"\"Invert A<->B winner labels for position bias scores (swapped pair orientation).\"\"\"\n    swap = {\"A\": \"B\", \"B\": \"A\", \"tie\": \"tie\"}\n    return [{**s, \"winner\": swap.get(s.get(\"winner\", \"tie\"), \"tie\")} for s in scores]\n\n\ndef load_all_scores():\n    \"\"\"Load sample-level clean + attacked scores for all 15 models.\n\n    Returns:\n        clean[ds][model_id] = [{\"winner\": ..., ...}, ...]\n        attacked[ds][atk][model_id] = [{\"winner\": ..., ...}, ...]\n    \"\"\"\n    clean = {ds: {} for ds in DATASETS}\n    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}\n\n    for ckpt_path in CKPT_FILES:\n        if not ckpt_path.exists():\n            continue\n        logger.info(f\"Loading checkpoint: {ckpt_path.name}\")\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        for ds in DATASETS:\n            for mid, scores in data.get(\"clean_scores\", {}).get(ds, {}).items():\n                if mid not in clean[ds]:\n                    clean[ds][mid] = scores\n            for atk in ATTACKS:\n                for mid, scores in data.get(\"attacked_scores\", {}).get(ds, {}).get(atk, {}).items():\n                    if mid not in attacked[ds][atk]:\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    if SCORES_DIR.exists():\n        logger.info(f\"Loading individual scores from {SCORES_DIR}\")\n        for mid in ALL_MODELS:\n            for ds in DATASETS:\n                fp = SCORES_DIR / f\"{mid}__{ds}__clean.json\"\n                if fp.exists() and mid not in clean[ds]:\n                    with open(fp) as f:\n                        clean[ds][mid] = json.load(f).get(\"scores\", [])\n                for atk in ATTACKS:\n                    fp = SCORES_DIR / f\"{mid}__{ds}__{atk}.json\"\n                    if fp.exists() and mid not in attacked[ds][atk]:\n                        with open(fp) as f:\n                            scores = json.load(f).get(\"scores\", [])\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    for ds in DATASETS:\n        nc = len(clean[ds])\n        logger.info(f\"  {ds} clean: {nc}/{len(ALL_MODELS)}\")\n        for atk in ATTACKS:\n            na = len(attacked[ds][atk])\n            if na > 0:\n                logger.info(f\"  {ds} {atk}: {na}/{len(ALL_MODELS)}\")\n\n    return clean, attacked\n\n\n# ── ASR Computation ──────────────────────────────────────────────────\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\n# ── Regression Helpers ───────────────────────────────────────────────\n\ndef partial_corr_manual(x, y, covar):\n    \"\"\"Partial correlation of x and y, controlling for covar.\"\"\"\n    Xc = sm.add_constant(covar)\n    rx = sm.OLS(x, Xc).fit().resid\n    ry = sm.OLS(y, Xc).fit().resid\n    r, p = stats.pearsonr(rx, ry)\n    return float(r), float(p)\n\n\ntry:\n    import pingouin as pg\n    import pandas as pd\n\n    def partial_corr_fn(x, y, covar):\n        df = pd.DataFrame({\"x\": x, \"y\": y, \"z\": covar})\n        res = pg.partial_corr(data=df, x=\"x\", y=\"y\", covar=\"z\")\n        return float(res[\"r\"].values[0]), float(res[\"p-val\"].values[0])\n    logger.info(\"Using pingouin for partial correlation\")\nexcept ImportError:\n    partial_corr_fn = partial_corr_manual\n    logger.info(\"pingouin not available, using manual partial correlation\")\n\n\ndef beta_regression_mle(y_raw, X):\n    \"\"\"Beta regression via MLE. y in (0,1), logit link.\n    X should include constant column.\n    Returns dict with coefficients/p-values or None on failure.\"\"\"\n    y = np.clip(y_raw, 1e-6, 1 - 1e-6)\n    n, k = X.shape\n\n    def neg_ll(params):\n        beta = params[:k]\n        phi = np.exp(params[k])\n        mu = 1.0 / (1.0 + np.exp(-(X @ beta)))\n        a = mu * phi\n        b = (1.0 - mu) * phi\n        return -np.sum(\n            special.gammaln(phi) - special.gammaln(a) - special.gammaln(b)\n            + (a - 1.0) * np.log(y) + (b - 1.0) * np.log(1.0 - y)\n        )\n\n    # Initial values from OLS on logit(y)\n    y_logit = np.log(y / (1.0 - y))\n    x0 = np.zeros(k + 1)\n    try:\n        init_fit = sm.OLS(y_logit, X).fit()\n        x0[:k] = init_fit.params\n    except Exception:\n        pass\n    x0[k] = np.log(10.0)\n\n    with warnings.catch_warnings():\n        warnings.simplefilter(\"ignore\")\n        res = optimize.minimize(neg_ll, x0, method=\"L-BFGS-B\",\n                                options={\"maxiter\": 5000, \"ftol\": 1e-12})\n    if not res.success:\n        return None\n\n    # Numerical Hessian for standard errors\n    n_p = len(res.x)\n    H = np.zeros((n_p, n_p))\n    eps_h = 1e-5\n    for i in range(n_p):\n        for j in range(i, n_p):\n            ei = np.zeros(n_p)\n            ej = np.zeros(n_p)\n            ei[i] = eps_h\n            ej[j] = eps_h\n            fpp = neg_ll(res.x + ei + ej)\n            fpm = neg_ll(res.x + ei - ej)\n            fmp = neg_ll(res.x - ei + ej)\n            fmm = neg_ll(res.x - ei - ej)\n            H[i, j] = H[j, i] = (fpp - fpm - fmp + fmm) / (4.0 * eps_h * eps_h)\n\n    try:\n        cov = np.linalg.inv(H)\n        se = np.sqrt(np.maximum(np.diag(cov), 0.0))\n    except np.linalg.LinAlgError:\n        return None\n\n    beta = res.x[:k]\n    se_b = se[:k]\n    z = beta / np.maximum(se_b, 1e-12)\n    pvals = 2.0 * (1.0 - stats.norm.cdf(np.abs(z)))\n    return {\"beta\": beta, \"se\": se_b, \"z\": z, \"p\": pvals}\n\n\ndef run_condition_analysis(panel_asrs, keffs, eta_maxs):\n    \"\"\"Full regression suite for one condition. All arrays shape (n,).\"\"\"\n    n = len(panel_asrs)\n    y = np.log(panel_asrs + EPS)\n    x1 = np.log(keffs)\n    x2 = np.log(eta_maxs + EPS)\n    X = np.column_stack([x1, x2])\n    Xc = sm.add_constant(X)\n    results = {}\n\n    # ── OLS ──\n    fit = sm.OLS(y, Xc).fit()\n    results[\"ols\"] = {\n        \"keff_beta\": float(fit.params[1]),\n        \"keff_t\": float(fit.tvalues[1]),\n        \"keff_p\": float(fit.pvalues[1]),\n        \"eta_max_beta\": float(fit.params[2]),\n        \"eta_max_t\": float(fit.tvalues[2]),\n        \"eta_max_p\": float(fit.pvalues[2]),\n        \"R2\": float(fit.rsquared),\n        \"adj_R2\": float(fit.rsquared_adj),\n        \"f_stat\": float(fit.fvalue) if np.isfinite(fit.fvalue) else None,\n        \"f_pvalue\": float(fit.f_pvalue) if np.isfinite(fit.f_pvalue) else None,\n    }\n\n    # ── VIF ──\n    results[\"vif_keff\"] = float(variance_inflation_factor(Xc, 1))\n    results[\"vif_eta_max\"] = float(variance_inflation_factor(Xc, 2))\n\n    # ── Partial correlation (K_eff | η_max) ──\n    pr, pp = partial_corr_fn(x1, y, x2)\n    results[\"partial_r_keff\"] = pr\n    results[\"partial_r_keff_p\"] = pp\n\n    # ── Residualized K_eff ──\n    Xz = sm.add_constant(x2)\n    resid_keff = sm.OLS(x1, Xz).fit().resid\n    Xr = sm.add_constant(resid_keff)\n    fit_r = sm.OLS(y, Xr).fit()\n    results[\"residualized_keff_beta\"] = float(fit_r.params[1])\n    results[\"residualized_keff_t\"] = float(fit_r.tvalues[1])\n    results[\"residualized_keff_p\"] = float(fit_r.pvalues[1])\n\n    # ── Beta regression ──\n    y_raw = np.clip(panel_asrs, 0.0, 1.0)\n    br = beta_regression_mle(y_raw, Xc)\n    if br is not None:\n        results[\"beta_reg_keff_beta\"] = float(br[\"beta\"][1])\n        results[\"beta_reg_keff_p\"] = float(br[\"p\"][1])\n        results[\"beta_reg_eta_max_beta\"] = float(br[\"beta\"][2])\n        results[\"beta_reg_eta_max_p\"] = float(br[\"p\"][2])\n    else:\n        results[\"beta_reg_keff_p\"] = None\n        results[\"beta_reg_eta_max_p\"] = None\n\n    return results\n\n\n# ── Main ─────────────────────────────────────────────────────────────\n\ndef main():\n    logger.info(\"=\" * 60)\n    logger.info(\"Plan 001 Step 4: Panel Regression (455 panels × 12 conditions)\")\n    logger.info(\"=\" * 60)\n\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    # Precompute individual ASR for all model × condition\n    logger.info(\"\\nPrecomputing individual ASR...\")\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    logger.info(f\"  Computed {len(ind_asr)} individual ASR values\")\n\n    # Enumerate all C(15,3)=455 panels\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n    logger.info(f\"  Total panels: {len(all_combos)}\")\n\n    condition_results = {}\n    raw_eta_ps = []\n    raw_keff_ps = []\n    valid_cond_keys = []\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        for atk in ATTACKS:\n            cond = f\"{ds}×{atk}\"\n            logger.info(f\"\\n--- {cond} ---\")\n\n            p_asrs, p_keffs, p_etas = [], [], []\n            skipped = 0\n\n            for combo in all_combos:\n                jids = [ALL_MODELS[i] for i in combo]\n\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    skipped += 1\n                    continue\n                pk = \"|\".join(jids)\n                if pk not in keff_data:\n                    skipped += 1\n                    continue\n\n                keff = keff_data[pk][\"keff\"]\n                etas = [ind_asr[(ds, atk, j)] for j in jids]\n                eta_max = max(etas)\n\n                cs = {j: clean[ds][j] for j in jids}\n                ats = {j: attacked[ds][atk][j] for j in jids}\n                p_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n                p_asrs.append(p_asr)\n                p_keffs.append(keff)\n                p_etas.append(eta_max)\n\n            n_panels = len(p_asrs)\n            logger.info(f\"  {n_panels} panels with data, {skipped} skipped\")\n\n            if n_panels < 10:\n                logger.warning(f\"  Too few panels ({n_panels}), skipping\")\n                condition_results[cond] = {\"n_panels\": n_panels, \"skipped\": True}\n                continue\n\n            p_asrs = np.array(p_asrs)\n            p_keffs = np.array(p_keffs)\n            p_etas = np.array(p_etas)\n\n            if np.std(p_asrs) < 1e-10:\n                logger.warning(f\"  Constant ASR ({p_asrs[0]:.4f}), skipping regression\")\n                condition_results[cond] = {\n                    \"n_panels\": n_panels, \"skipped\": True,\n                    \"reason\": \"constant_asr\", \"asr_value\": float(p_asrs[0]),\n                }\n                continue\n\n            cond_res = run_condition_analysis(p_asrs, p_keffs, p_etas)\n            cond_res[\"n_panels\"] = n_panels\n            cond_res[\"skipped\"] = False\n            cond_res[\"asr_stats\"] = {\n                \"mean\": float(np.mean(p_asrs)),\n                \"std\": float(np.std(p_asrs)),\n                \"min\": float(np.min(p_asrs)),\n                \"max\": float(np.max(p_asrs)),\n                \"pct_zero\": float(np.mean(p_asrs == 0)),\n            }\n            condition_results[cond] = cond_res\n\n            raw_eta_ps.append(cond_res[\"ols\"][\"eta_max_p\"])\n            raw_keff_ps.append(cond_res[\"ols\"][\"keff_p\"])\n            valid_cond_keys.append(cond)\n\n            ols = cond_res[\"ols\"]\n            sig_k = \"***\" if ols[\"keff_p\"] < 0.001 else \"**\" if ols[\"keff_p\"] < 0.01 else \"*\" if ols[\"keff_p\"] < 0.05 else \"ns\"\n            sig_e = \"***\" if ols[\"eta_max_p\"] < 0.001 else \"**\" if ols[\"eta_max_p\"] < 0.01 else \"*\" if ols[\"eta_max_p\"] < 0.05 else \"ns\"\n            logger.info(\n                f\"  OLS R²={ols['R2']:.4f}  \"\n                f\"K_eff: β={ols['keff_beta']:+.4f} p={ols['keff_p']:.4f} {sig_k}  \"\n                f\"η_max: β={ols['eta_max_beta']:+.4f} p={ols['eta_max_p']:.4f} {sig_e}\"\n            )\n            logger.info(\n                f\"  VIF: K_eff={cond_res['vif_keff']:.2f}, η_max={cond_res['vif_eta_max']:.2f}\"\n            )\n            logger.info(\n                f\"  Partial r(K_eff|η_max)={cond_res['partial_r_keff']:.4f} \"\n                f\"p={cond_res['partial_r_keff_p']:.4f}\"\n            )\n            logger.info(\n                f\"  Residualized K_eff: β={cond_res['residualized_keff_beta']:+.4f} \"\n                f\"p={cond_res['residualized_keff_p']:.4f}\"\n            )\n\n    # ── Multiple testing corrections ──\n    if raw_eta_ps:\n        _, bonf_eta, _, _ = multipletests(raw_eta_ps, method=\"bonferroni\")\n        _, fdr_eta, _, _ = multipletests(raw_eta_ps, method=\"fdr_bh\")\n        _, bonf_keff, _, _ = multipletests(raw_keff_ps, method=\"bonferroni\")\n        _, fdr_keff, _, _ = multipletests(raw_keff_ps, method=\"fdr_bh\")\n\n        for i, ck in enumerate(valid_cond_keys):\n            condition_results[ck][\"eta_max_bonferroni_p\"] = float(bonf_eta[i])\n            condition_results[ck][\"eta_max_fdr_p\"] = float(fdr_eta[i])\n            condition_results[ck][\"keff_bonferroni_p\"] = float(bonf_keff[i])\n            condition_results[ck][\"keff_fdr_p\"] = float(fdr_keff[i])\n\n    # ── Summary ──\n    valid = [condition_results[k] for k in valid_cond_keys]\n    nv = len(valid)\n    summary = {}\n    if nv > 0:\n        summary = {\n            \"keff_sig_negative_count\": (\n                f\"{sum(1 for r in valid if r['ols']['keff_beta'] < 0 and r['ols']['keff_p'] < 0.05)}/{nv}\"\n            ),\n            \"keff_residualized_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('residualized_keff_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"eta_max_bonferroni_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('eta_max_bonferroni_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"eta_max_fdr_sig_count\": (\n                f\"{sum(1 for r in valid if r.get('eta_max_fdr_p', 1) < 0.05)}/{nv}\"\n            ),\n            \"mean_vif_keff\": float(np.mean([r[\"vif_keff\"] for r in valid])),\n            \"mean_R2\": float(np.mean([r[\"ols\"][\"R2\"] for r in valid])),\n        }\n\n    output = {\n        \"n_panels\": 455,\n        \"n_models\": len(ALL_MODELS),\n        \"models\": ALL_MODELS,\n        \"datasets\": DATASETS,\n        \"attacks\": ATTACKS,\n        \"conditions\": condition_results,\n        \"summary\": summary,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    out_path = OUTPUT_DIR / \"step4_regression_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    logger.info(f\"\\nResults saved: {out_path}\")\n\n    logger.info(\"\\n\" + \"=\" * 60)\n    logger.info(\"SUMMARY\")\n    logger.info(\"=\" * 60)\n    for k, v in summary.items():\n        logger.info(f\"  {k}: {v}\")\n\n    # Per-condition table\n    logger.info(f\"\\n{'Condition':<35} {'R²':>6} {'K_eff β':>9} {'K_eff p':>9} {'η_max β':>9} {'η_max p':>9} {'VIF':>5}\")\n    logger.info(\"-\" * 90)\n    for ck in valid_cond_keys:\n        r = condition_results[ck]\n        o = r[\"ols\"]\n        logger.info(\n            f\"  {ck:<33} {o['R2']:>6.3f} {o['keff_beta']:>+9.4f} {o['keff_p']:>9.4f} \"\n            f\"{o['eta_max_beta']:>+9.4f} {o['eta_max_p']:>9.4f} {r['vif_keff']:>5.1f}\"\n        )\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — Write · `toolu_01LceptoxHvq1tmm9Gjvrh4b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step5_random_fault.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 5: Random-fault simulation -- 455 panels x 12 conditions.\n\nInput:\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\n\nOutput:\n  - artifacts/results/plan001/panel_regression/step5_random_fault_results.json\n\nDependencies: numpy, scipy, statsmodels\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport warnings\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy import stats\n\nfrom src.utils import setup_logging\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,\n    load_all_scores, load_pairs, load_mi_data,\n)\n\nlogger = setup_logging(\"plan001_step5\")\n\nEPS = 0.001\nN_SIMS = 1000\nN_SAMPLES = 300\nSIM_BATCH = 100\n\n\n# ── JSON Helper ──────────────────────────────────────────────────────\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\n# ── ASR Computation ──────────────────────────────────────────────────\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\n# ── Random-Fault Simulation ─────────────────────────────────────────\n\ndef analytical_rf_asr(eta):\n    e1, e2, e3 = eta\n    return e1 * e2 + e1 * e3 + e2 * e3 - 2.0 * e1 * e2 * e3\n\n\ndef simulate_rf_vectorized(eta_all, rng):\n    n_panels = eta_all.shape[0]\n    rf_sum = np.zeros(n_panels)\n    rf_sq_sum = np.zeros(n_panels)\n\n    for sim_start in range(0, N_SIMS, SIM_BATCH):\n        b = min(SIM_BATCH, N_SIMS - sim_start)\n        randoms = rng.random((n_panels, b, N_SAMPLES, 3))\n        errors = randoms < eta_all[:, np.newaxis, np.newaxis, :]\n        panel_err = errors.sum(axis=3) >= 2\n        rates = panel_err.mean(axis=2).astype(np.float64)\n        rf_sum += rates.sum(axis=1)\n        rf_sq_sum += (rates ** 2).sum(axis=1)\n\n    rf_mean = rf_sum / N_SIMS\n    rf_std = np.sqrt(np.maximum(rf_sq_sum / N_SIMS - rf_mean ** 2, 0.0))\n    return rf_mean, rf_std\n\n\n# ── Regression ───────────────────────────────────────────────────────\n\ndef run_ols(y_raw, keffs, eta_maxs):\n    y = np.log(y_raw + EPS)\n    X = np.column_stack([np.log(keffs), np.log(eta_maxs + EPS)])\n    Xc = sm.add_constant(X)\n    fit = sm.OLS(y, Xc).fit()\n    return {\n        \"keff_beta\": float(fit.params[1]),\n        \"keff_t\": float(fit.tvalues[1]),\n        \"keff_p\": float(fit.pvalues[1]),\n        \"eta_max_beta\": float(fit.params[2]),\n        \"eta_max_t\": float(fit.tvalues[2]),\n        \"eta_max_p\": float(fit.pvalues[2]),\n        \"R2\": float(fit.rsquared),\n        \"adj_R2\": float(fit.rsquared_adj),\n    }\n\n\n# ── Main ─────────────────────────────────────────────────────────────\n\ndef main():\n    logger.info(\"=\" * 60)\n    logger.info(\"Plan 001 Step 5: Random-Fault Simulation\")\n    logger.info(f\"  {N_SIMS} simulations x {N_SAMPLES} samples per panel\")\n    logger.info(\"=\" * 60)\n\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    logger.info(\"\\nPrecomputing individual ASR...\")\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    logger.info(f\"  Computed {len(ind_asr)} individual ASR values\")\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n    rng = np.random.default_rng(42)\n\n    condition_results = {}\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        for atk in ATTACKS:\n            cond = f\"{ds}x{atk}\"\n            logger.info(f\"\\n--- {cond} ---\")\n\n            panel_keffs = []\n            panel_eta_maxs = []\n            panel_eta_all = []\n            panel_adaptive_asrs = []\n            panel_jids_list = []\n            skipped = 0\n\n            for combo in all_combos:\n                jids = [ALL_MODELS[i] for i in combo]\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    skipped += 1\n                    continue\n                pk = \"|\".join(jids)\n                if pk not in keff_data:\n                    skipped += 1\n                    continue\n\n                keff = keff_data[pk][\"keff\"]\n                etas = [ind_asr[(ds, atk, j)] for j in jids]\n\n                cs = {j: clean[ds][j] for j in jids}\n                ats = {j: attacked[ds][atk][j] for j in jids}\n                adaptive_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n                panel_keffs.append(keff)\n                panel_eta_maxs.append(max(etas))\n                panel_eta_all.append(etas)\n                panel_adaptive_asrs.append(adaptive_asr)\n                panel_jids_list.append(jids)\n\n            n_panels = len(panel_keffs)\n            logger.info(f\"  {n_panels} panels with data, {skipped} skipped\")\n\n            if n_panels < 10:\n                logger.warning(f\"  Too few panels ({n_panels}), skipping\")\n                condition_results[cond] = {\"n_panels\": n_panels, \"skipped\": True}\n                continue\n\n            keffs = np.array(panel_keffs)\n            eta_maxs = np.array(panel_eta_maxs)\n            eta_all = np.array(panel_eta_all)\n            adaptive_asrs = np.array(panel_adaptive_asrs)\n\n            logger.info(f\"  Simulating {N_SIMS} RF runs...\")\n            rf_mean, rf_std = simulate_rf_vectorized(eta_all, rng)\n\n            analytical = np.array([analytical_rf_asr(e) for e in eta_all])\n            max_dev = np.max(np.abs(rf_mean - analytical))\n            logger.info(f\"  RF simulation done. Max deviation from analytical: {max_dev:.6f}\")\n\n            if np.std(adaptive_asrs) < 1e-10:\n                logger.warning(f\"  Constant adaptive ASR, skipping regression\")\n                adaptive_ols = {\"keff_beta\": 0, \"keff_p\": 1, \"R2\": 0, \"note\": \"constant_asr\"}\n            else:\n                adaptive_ols = run_ols(adaptive_asrs, keffs, eta_maxs)\n\n            if np.std(rf_mean) < 1e-10:\n                logger.warning(f\"  Constant RF ASR, skipping regression\")\n                rf_ols = {\"keff_beta\": 0, \"keff_p\": 1, \"R2\": 0, \"note\": \"constant_asr\"}\n            else:\n                rf_ols = run_ols(rf_mean, keffs, eta_maxs)\n\n            delta_R2 = rf_ols.get(\"R2\", 0) - adaptive_ols.get(\"R2\", 0)\n            keff_gains = (\n                rf_ols.get(\"keff_p\", 1) < 0.05\n                and rf_ols.get(\"keff_p\", 1) < adaptive_ols.get(\"keff_p\", 1)\n            )\n\n            keff_q75 = np.percentile(keffs, 75)\n            eta_q25 = np.percentile(eta_maxs, 25)\n            hk_le_mask = (keffs >= keff_q75) & (eta_maxs <= eta_q25)\n            n_hk_le = int(hk_le_mask.sum())\n            hk_le_benefit = None\n            hk_le_pval = None\n            if n_hk_le >= 5:\n                diff = adaptive_asrs[hk_le_mask] - rf_mean[hk_le_mask]\n                hk_le_benefit = float(np.mean(diff))\n                if np.std(diff) > 1e-10:\n                    _, hk_le_pval = stats.ttest_1samp(diff, 0)\n                    hk_le_pval = float(hk_le_pval)\n\n            cond_res = {\n                \"n_panels\": n_panels,\n                \"skipped\": False,\n                \"adaptive\": adaptive_ols,\n                \"random_fault\": rf_ols,\n                \"delta_R2\": float(delta_R2),\n                \"keff_gains_significance\": bool(keff_gains),\n                \"rf_stats\": {\n                    \"mean\": float(np.mean(rf_mean)),\n                    \"std\": float(np.mean(rf_std)),\n                    \"max_analytical_deviation\": float(max_dev),\n                },\n                \"adaptive_stats\": {\n                    \"mean\": float(np.mean(adaptive_asrs)),\n                    \"std\": float(np.std(adaptive_asrs)),\n                },\n                \"high_keff_low_eta\": {\n                    \"n_panels\": n_hk_le,\n                    \"keff_threshold\": float(keff_q75),\n                    \"eta_threshold\": float(eta_q25),\n                    \"mean_benefit_adaptive_minus_rf\": hk_le_benefit,\n                    \"benefit_pval\": hk_le_pval,\n                },\n            }\n            condition_results[cond] = cond_res\n\n            logger.info(\n                f\"  Adaptive: K_eff B={adaptive_ols.get('keff_beta', 0):+.4f} \"\n                f\"p={adaptive_ols.get('keff_p', 1):.4f} R2={adaptive_ols.get('R2', 0):.4f}\"\n            )\n            logger.info(\n                f\"  RF:       K_eff B={rf_ols.get('keff_beta', 0):+.4f} \"\n                f\"p={rf_ols.get('keff_p', 1):.4f} R2={rf_ols.get('R2', 0):.4f}\"\n            )\n            logger.info(f\"  dR2={delta_R2:+.4f}  K_eff gains significance: {keff_gains}\")\n            if n_hk_le >= 5:\n                logger.info(\n                    f\"  High-K/Low-eta panels ({n_hk_le}): \"\n                    f\"mean benefit={hk_le_benefit:+.4f} p={hk_le_pval}\"\n                )\n\n    # ── Summary ──\n    valid = {k: v for k, v in condition_results.items() if not v.get(\"skipped\")}\n    nv = len(valid)\n\n    if nv > 0:\n        n_adapt_sig = sum(\n            1 for v in valid.values()\n            if v[\"adaptive\"].get(\"keff_p\", 1) < 0.05 and v[\"adaptive\"].get(\"keff_beta\", 0) < 0\n        )\n        n_rf_sig = sum(\n            1 for v in valid.values()\n            if v[\"random_fault\"].get(\"keff_p\", 1) < 0.05 and v[\"random_fault\"].get(\"keff_beta\", 0) < 0\n        )\n        mean_dR2 = float(np.mean([v[\"delta_R2\"] for v in valid.values()]))\n        n_gains = sum(1 for v in valid.values() if v[\"keff_gains_significance\"])\n\n        parts = []\n        parts.append(\n            f\"K_eff significantly negative in {n_rf_sig}/{nv} conditions under RF \"\n            f\"vs {n_adapt_sig}/{nv} under adaptive.\"\n        )\n        if mean_dR2 > 0:\n            parts.append(\n                f\"RF model explains more variance (mean dR2={mean_dR2:+.3f}), \"\n                \"consistent with independent-error majority vote theory.\"\n            )\n        else:\n            parts.append(\n                f\"Adaptive model explains more variance (mean dR2={mean_dR2:+.3f}).\"\n            )\n        if n_gains > nv // 2:\n            parts.append(\n                f\"K_eff gains significance in {n_gains}/{nv} conditions under RF, \"\n                \"suggesting diversity benefit is undermined by adaptive attacks.\"\n            )\n        interpretation = \" \".join(parts)\n\n        summary = {\n            \"adaptive_keff_sig_negative\": f\"{n_adapt_sig}/{nv}\",\n            \"random_fault_keff_sig_negative\": f\"{n_rf_sig}/{nv}\",\n            \"mean_delta_R2\": mean_dR2,\n            \"keff_gains_significance_count\": f\"{n_gains}/{nv}\",\n            \"interpretation\": interpretation,\n        }\n    else:\n        summary = {\"note\": \"No valid conditions to summarize\"}\n\n    output = {\n        \"n_panels\": 455,\n        \"n_simulations\": N_SIMS,\n        \"n_samples_per_sim\": N_SAMPLES,\n        \"models\": ALL_MODELS,\n        \"conditions\": condition_results,\n        \"summary\": summary,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    out_path = OUTPUT_DIR / \"step5_random_fault_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    logger.info(f\"\\nResults saved: {out_path}\")\n\n    logger.info(\"\\n\" + \"=\" * 60)\n    logger.info(\"SUMMARY\")\n    logger.info(\"=\" * 60)\n    for k, v in summary.items():\n        if k != \"interpretation\":\n            logger.info(f\"  {k}: {v}\")\n    if \"interpretation\" in summary:\n        logger.info(f\"\\n  {summary['interpretation']}\")\n\n    valid_keys = [k for k in condition_results if not condition_results[k].get(\"skipped\")]\n    logger.info(f\"\\n{'Condition':<35} {'Adap R2':>8} {'RF R2':>8} {'dR2':>7} {'Adap Kp':>8} {'RF Kp':>8} {'Gains':>5}\")\n    logger.info(\"-\" * 85)\n    for ck in valid_keys:\n        r = condition_results[ck]\n        a = r[\"adaptive\"]\n        rf = r[\"random_fault\"]\n        logger.info(\n            f\"  {ck:<33} {a.get('R2', 0):>8.4f} {rf.get('R2', 0):>8.4f} \"\n            f\"{r['delta_R2']:>+7.3f} {a.get('keff_p', 1):>8.4f} {rf.get('keff_p', 1):>8.4f} \"\n            f\"{'Y' if r['keff_gains_significance'] else 'N':>5}\"\n        )\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "1392e837-94c0-4650-a978-3666e098e238",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uaes55sArjYoKj59Yfu2YX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6159,
      "cache_read_input_tokens": 83145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6159
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

_source line 62 · 2026-05-22T15:02:51.818Z_

<details><summary>↩ Tool result · `toolu_01LceptoxHvq1tmm9Gjvrh4b`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step5_random_fault.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "4ef69307-9692-4b2f-bddb-216bbd2950fb",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step5_random_fault.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 5: Random-fault simulation -- 455 panels x 12 conditions.\n\nInput:\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\n\nOutput:\n  - artifacts/results/plan001/panel_regression/step5_random_fault_results.json\n\nDependencies: numpy, scipy, statsmodels\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport warnings\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy import stats\n\nfrom src.utils import setup_logging\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,\n    load_all_scores, load_pairs, load_mi_data,\n)\n\nlogger = setup_logging(\"plan001_step5\")\n\nEPS = 0.001\nN_SIMS = 1000\nN_SAMPLES = 300\nSIM_BATCH = 100\n\n\n# ── JSON Helper ──────────────────────────────────────────────────────\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\n# ── ASR Computation ──────────────────────────────────────────────────\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\n# ── Random-Fault Simulation ─────────────────────────────────────────\n\ndef analytical_rf_asr(eta):\n    e1, e2, e3 = eta\n    return e1 * e2 + e1 * e3 + e2 * e3 - 2.0 * e1 * e2 * e3\n\n\ndef simulate_rf_vectorized(eta_all, rng):\n    n_panels = eta_all.shape[0]\n    rf_sum = np.zeros(n_panels)\n    rf_sq_sum = np.zeros(n_panels)\n\n    for sim_start in range(0, N_SIMS, SIM_BATCH):\n        b = min(SIM_BATCH, N_SIMS - sim_start)\n        randoms = rng.random((n_panels, b, N_SAMPLES, 3))\n        errors = randoms < eta_all[:, np.newaxis, np.newaxis, :]\n        panel_err = errors.sum(axis=3) >= 2\n        rates = panel_err.mean(axis=2).astype(np.float64)\n        rf_sum += rates.sum(axis=1)\n        rf_sq_sum += (rates ** 2).sum(axis=1)\n\n    rf_mean = rf_sum / N_SIMS\n    rf_std = np.sqrt(np.maximum(rf_sq_sum / N_SIMS - rf_mean ** 2, 0.0))\n    return rf_mean, rf_std\n\n\n# ── Regression ───────────────────────────────────────────────────────\n\ndef run_ols(y_raw, keffs, eta_maxs):\n    y = np.log(y_raw + EPS)\n    X = np.column_stack([np.log(keffs), np.log(eta_maxs + EPS)])\n    Xc = sm.add_constant(X)\n    fit = sm.OLS(y, Xc).fit()\n    return {\n        \"keff_beta\": float(fit.params[1]),\n        \"keff_t\": float(fit.tvalues[1]),\n        \"keff_p\": float(fit.pvalues[1]),\n        \"eta_max_beta\": float(fit.params[2]),\n        \"eta_max_t\": float(fit.tvalues[2]),\n        \"eta_max_p\": float(fit.pvalues[2]),\n        \"R2\": float(fit.rsquared),\n        \"adj_R2\": float(fit.rsquared_adj),\n    }\n\n\n# ── Main ─────────────────────────────────────────────────────────────\n\ndef main():\n    logger.info(\"=\" * 60)\n    logger.info(\"Plan 001 Step 5: Random-Fault Simulation\")\n    logger.info(f\"  {N_SIMS} simulations x {N_SAMPLES} samples per panel\")\n    logger.info(\"=\" * 60)\n\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    logger.info(\"\\nPrecomputing individual ASR...\")\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    logger.info(f\"  Computed {len(ind_asr)} individual ASR values\")\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n    rng = np.random.default_rng(42)\n\n    condition_results = {}\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        for atk in ATTACKS:\n            cond = f\"{ds}x{atk}\"\n            logger.info(f\"\\n--- {cond} ---\")\n\n            panel_keffs = []\n            panel_eta_maxs = []\n            panel_eta_all = []\n            panel_adaptive_asrs = []\n            panel_jids_list = []\n            skipped = 0\n\n            for combo in all_combos:\n                jids = [ALL_MODELS[i] for i in combo]\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    skipped += 1\n                    continue\n                pk = \"|\".join(jids)\n                if pk not in keff_data:\n                    skipped += 1\n                    continue\n\n                keff = keff_data[pk][\"keff\"]\n                etas = [ind_asr[(ds, atk, j)] for j in jids]\n\n                cs = {j: clean[ds][j] for j in jids}\n                ats = {j: attacked[ds][atk][j] for j in jids}\n                adaptive_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n                panel_keffs.append(keff)\n                panel_eta_maxs.append(max(etas))\n                panel_eta_all.append(etas)\n                panel_adaptive_asrs.append(adaptive_asr)\n                panel_jids_list.append(jids)\n\n            n_panels = len(panel_keffs)\n            logger.info(f\"  {n_panels} panels with data, {skipped} skipped\")\n\n            if n_panels < 10:\n                logger.warning(f\"  Too few panels ({n_panels}), skipping\")\n                condition_results[cond] = {\"n_panels\": n_panels, \"skipped\": True}\n                continue\n\n            keffs = np.array(panel_keffs)\n            eta_maxs = np.array(panel_eta_maxs)\n            eta_all = np.array(panel_eta_all)\n            adaptive_asrs = np.array(panel_adaptive_asrs)\n\n            logger.info(f\"  Simulating {N_SIMS} RF runs...\")\n            rf_mean, rf_std = simulate_rf_vectorized(eta_all, rng)\n\n            analytical = np.array([analytical_rf_asr(e) for e in eta_all])\n            max_dev = np.max(np.abs(rf_mean - analytical))\n            logger.info(f\"  RF simulation done. Max deviation from analytical: {max_dev:.6f}\")\n\n            if np.std(adaptive_asrs) < 1e-10:\n                logger.warning(f\"  Constant adaptive ASR, skipping regression\")\n                adaptive_ols = {\"keff_beta\": 0, \"keff_p\": 1, \"R2\": 0, \"note\": \"constant_asr\"}\n            else:\n                adaptive_ols = run_ols(adaptive_asrs, keffs, eta_maxs)\n\n            if np.std(rf_mean) < 1e-10:\n                logger.warning(f\"  Constant RF ASR, skipping regression\")\n                rf_ols = {\"keff_beta\": 0, \"keff_p\": 1, \"R2\": 0, \"note\": \"constant_asr\"}\n            else:\n                rf_ols = run_ols(rf_mean, keffs, eta_maxs)\n\n            delta_R2 = rf_ols.get(\"R2\", 0) - adaptive_ols.get(\"R2\", 0)\n            keff_gains = (\n                rf_ols.get(\"keff_p\", 1) < 0.05\n                and rf_ols.get(\"keff_p\", 1) < adaptive_ols.get(\"keff_p\", 1)\n            )\n\n            keff_q75 = np.percentile(keffs, 75)\n            eta_q25 = np.percentile(eta_maxs, 25)\n            hk_le_mask = (keffs >= keff_q75) & (eta_maxs <= eta_q25)\n            n_hk_le = int(hk_le_mask.sum())\n            hk_le_benefit = None\n            hk_le_pval = None\n            if n_hk_le >= 5:\n                diff = adaptive_asrs[hk_le_mask] - rf_mean[hk_le_mask]\n                hk_le_benefit = float(np.mean(diff))\n                if np.std(diff) > 1e-10:\n                    _, hk_le_pval = stats.ttest_1samp(diff, 0)\n                    hk_le_pval = float(hk_le_pval)\n\n            cond_res = {\n                \"n_panels\": n_panels,\n                \"skipped\": False,\n                \"adaptive\": adaptive_ols,\n                \"random_fault\": rf_ols,\n                \"delta_R2\": float(delta_R2),\n                \"keff_gains_significance\": bool(keff_gains),\n                \"rf_stats\": {\n                    \"mean\": float(np.mean(rf_mean)),\n                    \"std\": float(np.mean(rf_std)),\n                    \"max_analytical_deviation\": float(max_dev),\n                },\n                \"adaptive_stats\": {\n                    \"mean\": float(np.mean(adaptive_asrs)),\n                    \"std\": float(np.std(adaptive_asrs)),\n                },\n                \"high_keff_low_eta\": {\n                    \"n_panels\": n_hk_le,\n                    \"keff_threshold\": float(keff_q75),\n                    \"eta_threshold\": float(eta_q25),\n                    \"mean_benefit_adaptive_minus_rf\": hk_le_benefit,\n                    \"benefit_pval\": hk_le_pval,\n                },\n            }\n            condition_results[cond] = cond_res\n\n            logger.info(\n                f\"  Adaptive: K_eff B={adaptive_ols.get('keff_beta', 0):+.4f} \"\n                f\"p={adaptive_ols.get('keff_p', 1):.4f} R2={adaptive_ols.get('R2', 0):.4f}\"\n            )\n            logger.info(\n                f\"  RF:       K_eff B={rf_ols.get('keff_beta', 0):+.4f} \"\n                f\"p={rf_ols.get('keff_p', 1):.4f} R2={rf_ols.get('R2', 0):.4f}\"\n            )\n            logger.info(f\"  dR2={delta_R2:+.4f}  K_eff gains significance: {keff_gains}\")\n            if n_hk_le >= 5:\n                logger.info(\n                    f\"  High-K/Low-eta panels ({n_hk_le}): \"\n                    f\"mean benefit={hk_le_benefit:+.4f} p={hk_le_pval}\"\n                )\n\n    # ── Summary ──\n    valid = {k: v for k, v in condition_results.items() if not v.get(\"skipped\")}\n    nv = len(valid)\n\n    if nv > 0:\n        n_adapt_sig = sum(\n            1 for v in valid.values()\n            if v[\"adaptive\"].get(\"keff_p\", 1) < 0.05 and v[\"adaptive\"].get(\"keff_beta\", 0) < 0\n        )\n        n_rf_sig = sum(\n            1 for v in valid.values()\n            if v[\"random_fault\"].get(\"keff_p\", 1) < 0.05 and v[\"random_fault\"].get(\"keff_beta\", 0) < 0\n        )\n        mean_dR2 = float(np.mean([v[\"delta_R2\"] for v in valid.values()]))\n        n_gains = sum(1 for v in valid.values() if v[\"keff_gains_significance\"])\n\n        parts = []\n        parts.append(\n            f\"K_eff significantly negative in {n_rf_sig}/{nv} conditions under RF \"\n            f\"vs {n_adapt_sig}/{nv} under adaptive.\"\n        )\n        if mean_dR2 > 0:\n            parts.append(\n                f\"RF model explains more variance (mean dR2={mean_dR2:+.3f}), \"\n                \"consistent with independent-error majority vote theory.\"\n            )\n        else:\n            parts.append(\n                f\"Adaptive model explains more variance (mean dR2={mean_dR2:+.3f}).\"\n            )\n        if n_gains > nv // 2:\n            parts.append(\n                f\"K_eff gains significance in {n_gains}/{nv} conditions under RF, \"\n                \"suggesting diversity benefit is undermined by adaptive attacks.\"\n            )\n        interpretation = \" \".join(parts)\n\n        summary = {\n            \"adaptive_keff_sig_negative\": f\"{n_adapt_sig}/{nv}\",\n            \"random_fault_keff_sig_negative\": f\"{n_rf_sig}/{nv}\",\n            \"mean_delta_R2\": mean_dR2,\n            \"keff_gains_significance_count\": f\"{n_gains}/{nv}\",\n            \"interpretation\": interpretation,\n        }\n    else:\n        summary = {\"note\": \"No valid conditions to summarize\"}\n\n    output = {\n        \"n_panels\": 455,\n        \"n_simulations\": N_SIMS,\n        \"n_samples_per_sim\": N_SAMPLES,\n        \"models\": ALL_MODELS,\n        \"conditions\": condition_results,\n        \"summary\": summary,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    out_path = OUTPUT_DIR / \"step5_random_fault_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    logger.info(f\"\\nResults saved: {out_path}\")\n\n    logger.info(\"\\n\" + \"=\" * 60)\n    logger.info(\"SUMMARY\")\n    logger.info(\"=\" * 60)\n    for k, v in summary.items():\n        if k != \"interpretation\":\n            logger.info(f\"  {k}: {v}\")\n    if \"interpretation\" in summary:\n        logger.info(f\"\\n  {summary['interpretation']}\")\n\n    valid_keys = [k for k in condition_results if not condition_results[k].get(\"skipped\")]\n    logger.info(f\"\\n{'Condition':<35} {'Adap R2':>8} {'RF R2':>8} {'dR2':>7} {'Adap Kp':>8} {'RF Kp':>8} {'Gains':>5}\")\n    logger.info(\"-\" * 85)\n    for ck in valid_keys:\n        r = condition_results[ck]\n        a = r[\"adaptive\"]\n        rf = r[\"random_fault\"]\n        logger.info(\n            f\"  {ck:<33} {a.get('R2', 0):>8.4f} {rf.get('R2', 0):>8.4f} \"\n            f\"{r['delta_R2']:>+7.3f} {a.get('keff_p', 1):>8.4f} {rf.get('keff_p', 1):>8.4f} \"\n            f\"{'Y' if r['keff_gains_significance'] else 'N':>5}\"\n        )\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " #!/usr/bin/env python3",
          "-\"\"\"Plan 001 Step 5: Random-fault simulation — 455 panels × 12 conditions.",
          "+\"\"\"Plan 001 Step 5: Random-fault simulation -- 455 panels x 12 conditions.",
          " ",
          " Input:",
          "   - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json"
        ]
      },
      {
        "oldStart": 27,
        "oldLines": 41,
        "newStart": 27,
        "newLines": 19,
        "lines": [
          " from scipy import stats",
          " ",
          " from src.utils import setup_logging",
          "+from src.unified_data_loader import (",
          "+    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,",
          "+    load_all_scores, load_pairs, load_mi_data,",
          "+)",
          " ",
          " logger = setup_logging(\"plan001_step5\")",
          " ",
          "-# ── Constants ────────────────────────────────────────────────────────",
          "-LOCAL_MODELS = [",
          "-    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",",
          "-    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",",
          "-]",
          "-API_MODELS = [",
          "-    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",",
          "-    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",",
          "-    \"gpt-4o-mini\", \"claude-3-haiku\",",
          "-]",
          "-ALL_MODELS = LOCAL_MODELS + API_MODELS",
          "-DATASETS = [\"mmlu\", \"arc_challenge\"]",
          "-ATTACKS = [",
          "-    \"prompt_injection\", \"sycophancy\", \"score_manipulation\",",
          "-    \"verbosity_bias\", \"position_bias\", \"authority_bias\",",
          "-]",
          " EPS = 0.001",
          " N_SIMS = 1000",
          " N_SAMPLES = 300",
          " SIM_BATCH = 100",
          " ",
          "-RESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")",
          "-PLAN001_DIR = RESULTS_DIR / \"plan001\"",
          "-SCORES_DIR = PLAN001_DIR / \"individual_scores\"",
          "-MI_PATH = PLAN001_DIR / \"mi_matrix\" / \"mi_matrix_15models.json\"",
          "-CKPT_FILES = [",
          "-    RESULTS_DIR / \"_taxonomy_checkpoint.json\",",
          "-    RESULTS_DIR / \"_step2v3_checkpoint.json\",",
          "-]",
          "-OUTPUT_DIR = PLAN001_DIR / \"panel_regression\"",
          " ",
          "-",
          " # ── JSON Helper ──────────────────────────────────────────────────────",
          " ",
          " def _json_default(obj):"
        ]
      },
      {
        "oldStart": 77,
        "oldLines": 91,
        "newStart": 55,
        "newLines": 6,
        "lines": [
          "     raise TypeError(f\"Not JSON serializable: {type(obj)}\")",
          " ",
          " ",
          "-# ── Data Loading (shared with Step 4) ────────────────────────────────",
          "-",
          "-def load_mi_data():",
          "-    if not MI_PATH.exists():",
          "-        logger.error(f\"MI matrix not found: {MI_PATH}\")",
          "-        sys.exit(1)",
          "-    with open(MI_PATH) as f:",
          "-        data = json.load(f)",
          "-    logger.info(f\"Loaded MI matrix: {len(data['models'])} models\")",
          "-    return data",
          "-",
          "-",
          "-def load_pairs():",
          "-    for ckpt_path in CKPT_FILES:",
          "-        if not ckpt_path.exists():",
          "-            continue",
          "-        with open(ckpt_path) as f:",
          "-            data = json.load(f)",
          "-        if \"pairs\" not in data:",
          "-            continue",
          "-        pairs = {}",
          "-        for ds in DATASETS:",
          "-            if ds in data[\"pairs\"]:",
          "-                pairs[ds] = data[\"pairs\"][ds][:300]",
          "-                logger.info(f\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\")",
          "-        if pairs:",
          "-            return pairs",
          "-    logger.error(\"No pairs found in any checkpoint file\")",
          "-    sys.exit(1)",
          "-",
          "-",
          "-def _invert_winners(scores):",
          "-    swap = {\"A\": \"B\", \"B\": \"A\", \"tie\": \"tie\"}",
          "-    return [{**s, \"winner\": swap.get(s.get(\"winner\", \"tie\"), \"tie\")} for s in scores]",
          "-",
          "-",
          "-def load_all_scores():",
          "-    clean = {ds: {} for ds in DATASETS}",
          "-    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}",
          "-",
          "-    for ckpt_path in CKPT_FILES:",
          "-        if not ckpt_path.exists():",
          "-            continue",
          "-        logger.info(f\"Loading checkpoint: {ckpt_path.name}\")",
          "-        with open(ckpt_path) as f:",
          "-            data = json.load(f)",
          "-        for ds in DATASETS:",
          "-            for mid, scores in data.get(\"clean_scores\", {}).get(ds, {}).items():",
          "-                if mid not in clean[ds]:",
          "-                    clean[ds][mid] = scores",
          "-            for atk in ATTACKS:",
          "-                for mid, scores in data.get(\"attacked_scores\", {}).get(ds, {}).get(atk, {}).items():",
          "-                    if mid not in attacked[ds][atk]:",
          "-                        if atk == \"position_bias\":",
          "-                            scores = _invert_winners(scores)",
          "-                        attacked[ds][atk][mid] = scores",
          "-",
          "-    if SCORES_DIR.exists():",
          "-        logger.info(f\"Loading individual scores from {SCORES_DIR}\")",
          "-        for mid in ALL_MODELS:",
          "-            for ds in DATASETS:",
          "-                fp = SCORES_DIR / f\"{mid}__{ds}__clean.json\"",
          "-                if fp.exists() and mid not in clean[ds]:",
          "-                    with open(fp) as f:",
          "-                        clean[ds][mid] = json.load(f).get(\"scores\", [])",
          "-                for atk in ATTACKS:",
          "-                    fp = SCORES_DIR / f\"{mid}__{ds}__{atk}.json\"",
          "-                    if fp.exists() and mid not in attacked[ds][atk]:",
          "-                        with open(fp) as f:",
          "-                            scores = json.load(f).get(\"scores\", [])",
          "-                        if atk == \"position_bias\":",
          "-                            scores = _invert_winners(scores)",
          "-                        attacked[ds][atk][mid] = scores",
          "-",
          "-    for ds in DATASETS:",
          "-        nc = len(clean[ds])",
          "-        logger.info(f\"  {ds} clean: {nc}/{len(ALL_MODELS)}\")",
          "-        for atk in ATTACKS:",
          "-            na = len(attacked[ds][atk])",
          "-            if na > 0:",
          "-                logger.info(f\"  {ds} {atk}: {na}/{len(ALL_MODELS)}\")",
          "-",
          "-    return clean, attacked",
          "-",
          "-",
          " # ── ASR Computation ──────────────────────────────────────────────────",
          " ",
          " def majority_vote(votes):"
        ]
      },
      {
        "oldStart": 208,
        "oldLines": 36,
        "newStart": 101,
        "newLines": 20,
        "lines": [
          " # ── Random-Fault Simulation ─────────────────────────────────────────",
          " ",
          " def analytical_rf_asr(eta):",
          "-    \"\"\"Analytical P(panel error) for majority vote with 3 independent judges.",
          "-    P(≥2 fail) = η₁η₂ + η₁η₃ + η₂η₃ - 2η₁η₂η₃\"\"\"",
          "     e1, e2, e3 = eta",
          "     return e1 * e2 + e1 * e3 + e2 * e3 - 2.0 * e1 * e2 * e3",
          " ",
          " ",
          " def simulate_rf_vectorized(eta_all, rng):",
          "-    \"\"\"Simulate random-fault ASR for all panels.",
          "-",
          "-    Args:",
          "-        eta_all: (n_panels, 3) array of individual judge error rates",
          "-        rng: numpy random generator",
          "-",
          "-    Returns:",
          "-        rf_mean: (n_panels,) mean RF ASR across simulations",
          "-        rf_std: (n_panels,) std RF ASR across simulations",
          "-    \"\"\"",
          "     n_panels = eta_all.shape[0]",
          "     rf_sum = np.zeros(n_panels)",
          "     rf_sq_sum = np.zeros(n_panels)",
          " ",
          "     for sim_start in range(0, N_SIMS, SIM_BATCH):",
          "         b = min(SIM_BATCH, N_SIMS - sim_start)",
          "-        # (n_panels, batch, n_samples, 3) random draws",
          "         randoms = rng.random((n_panels, b, N_SAMPLES, 3))",
          "-        # Each judge errors independently with probability eta_j",
          "         errors = randoms < eta_all[:, np.newaxis, np.newaxis, :]",
          "-        # Majority vote: panel errs if ≥2 judges err",
          "         panel_err = errors.sum(axis=3) >= 2",
          "-        # Error rate per sim: (n_panels, batch)",
          "         rates = panel_err.mean(axis=2).astype(np.float64)",
          "         rf_sum += rates.sum(axis=1)",
          "         rf_sq_sum += (rates ** 2).sum(axis=1)"
        ]
      },
      {
        "oldStart": 250,
        "oldLines": 7,
        "newStart": 127,
        "newLines": 6,
        "lines": [
          " # ── Regression ───────────────────────────────────────────────────────",
          " ",
          " def run_ols(y_raw, keffs, eta_maxs):",
          "-    \"\"\"Simple OLS: log(y+ε) ~ log(K_eff) + log(η_max+ε).\"\"\"",
          "     y = np.log(y_raw + EPS)",
          "     X = np.column_stack([np.log(keffs), np.log(eta_maxs + EPS)])",
          "     Xc = sm.add_constant(X)"
        ]
      },
      {
        "oldStart": 272,
        "oldLines": 14,
        "newStart": 148,
        "newLines": 13,
        "lines": [
          " def main():",
          "     logger.info(\"=\" * 60)",
          "     logger.info(\"Plan 001 Step 5: Random-Fault Simulation\")",
          "-    logger.info(f\"  {N_SIMS} simulations × {N_SAMPLES} samples per panel\")",
          "+    logger.info(f\"  {N_SIMS} simulations x {N_SAMPLES} samples per panel\")",
          "     logger.info(\"=\" * 60)",
          " ",
          "     mi_data = load_mi_data()",
          "     pairs = load_pairs()",
          "     clean, attacked = load_all_scores()",
          " ",
          "-    # Precompute individual ASR",
          "     logger.info(\"\\nPrecomputing individual ASR...\")",
          "     ind_asr = {}",
          "     for ds in DATASETS:"
        ]
      },
      {
        "oldStart": 299,
        "oldLines": 13,
        "newStart": 174,
        "newLines": 12,
        "lines": [
          "     for ds in DATASETS:",
          "         keff_data = mi_data[\"keff_per_panel\"].get(ds, {})",
          "         for atk in ATTACKS:",
          "-            cond = f\"{ds}×{atk}\"",
          "+            cond = f\"{ds}x{atk}\"",
          "             logger.info(f\"\\n--- {cond} ---\")",
          " ",
          "-            # Collect panel data",
          "             panel_keffs = []",
          "             panel_eta_maxs = []",
          "-            panel_eta_all = []  # (n_panels, 3) for simulation",
          "+            panel_eta_all = []",
          "             panel_adaptive_asrs = []",
          "             panel_jids_list = []",
          "             skipped = 0"
        ]
      },
      {
        "oldStart": 323,
        "oldLines": 7,
        "newStart": 197,
        "newLines": 6,
        "lines": [
          "                 keff = keff_data[pk][\"keff\"]",
          "                 etas = [ind_asr[(ds, atk, j)] for j in jids]",
          " ",
          "-                # Adaptive panel ASR (majority vote on actual scores)",
          "                 cs = {j: clean[ds][j] for j in jids}",
          "                 ats = {j: attacked[ds][atk][j] for j in jids}",
          "                 adaptive_asr = compute_panel_asr(jids, cs, ats, pairs[ds])"
        ]
      },
      {
        "oldStart": 344,
        "oldLines": 27,
        "newStart": 217,
        "newLines": 22,
        "lines": [
          " ",
          "             keffs = np.array(panel_keffs)",
          "             eta_maxs = np.array(panel_eta_maxs)",
          "-            eta_all = np.array(panel_eta_all)  # (n_panels, 3)",
          "+            eta_all = np.array(panel_eta_all)",
          "             adaptive_asrs = np.array(panel_adaptive_asrs)",
          " ",
          "-            # ── Random-fault simulation ──",
          "             logger.info(f\"  Simulating {N_SIMS} RF runs...\")",
          "             rf_mean, rf_std = simulate_rf_vectorized(eta_all, rng)",
          " ",
          "-            # Analytical validation",
          "             analytical = np.array([analytical_rf_asr(e) for e in eta_all])",
          "             max_dev = np.max(np.abs(rf_mean - analytical))",
          "             logger.info(f\"  RF simulation done. Max deviation from analytical: {max_dev:.6f}\")",
          " ",
          "-            # ── Regressions ──",
          "-            # Adaptive",
          "             if np.std(adaptive_asrs) < 1e-10:",
          "                 logger.warning(f\"  Constant adaptive ASR, skipping regression\")",
          "                 adaptive_ols = {\"keff_beta\": 0, \"keff_p\": 1, \"R2\": 0, \"note\": \"constant_asr\"}",
          "             else:",
          "                 adaptive_ols = run_ols(adaptive_asrs, keffs, eta_maxs)",
          " ",
          "-            # Random-fault",
          "             if np.std(rf_mean) < 1e-10:",
          "                 logger.warning(f\"  Constant RF ASR, skipping regression\")",
          "                 rf_ols = {\"keff_beta\": 0, \"keff_p\": 1, \"R2\": 0, \"note\": \"constant_asr\"}"
        ]
      },
      {
        "oldStart": 377,
        "oldLines": 7,
        "newStart": 245,
        "newLines": 6,
        "lines": [
          "                 and rf_ols.get(\"keff_p\", 1) < adaptive_ols.get(\"keff_p\", 1)",
          "             )",
          " ",
          "-            # ── High-K_eff + Low-η_max benefit analysis ──",
          "             keff_q75 = np.percentile(keffs, 75)",
          "             eta_q25 = np.percentile(eta_maxs, 25)",
          "             hk_le_mask = (keffs >= keff_q75) & (eta_maxs <= eta_q25)"
        ]
      },
      {
        "oldStart": 418,
        "oldLines": 17,
        "newStart": 285,
        "newLines": 17,
        "lines": [
          "             condition_results[cond] = cond_res",
          " ",
          "             logger.info(",
          "-                f\"  Adaptive: K_eff β={adaptive_ols.get('keff_beta', 0):+.4f} \"",
          "-                f\"p={adaptive_ols.get('keff_p', 1):.4f} R²={adaptive_ols.get('R2', 0):.4f}\"",
          "+                f\"  Adaptive: K_eff B={adaptive_ols.get('keff_beta', 0):+.4f} \"",
          "+                f\"p={adaptive_ols.get('keff_p', 1):.4f} R2={adaptive_ols.get('R2', 0):.4f}\"",
          "             )",
          "             logger.info(",
          "-                f\"  RF:       K_eff β={rf_ols.get('keff_beta', 0):+.4f} \"",
          "-                f\"p={rf_ols.get('keff_p', 1):.4f} R²={rf_ols.get('R2', 0):.4f}\"",
          "+                f\"  RF:       K_eff B={rf_ols.get('keff_beta', 0):+.4f} \"",
          "+                f\"p={rf_ols.get('keff_p', 1):.4f} R2={rf_ols.get('R2', 0):.4f}\"",
          "             )",
          "-            logger.info(f\"  ΔR²={delta_R2:+.4f}  K_eff gains significance: {keff_gains}\")",
          "+            logger.info(f\"  dR2={delta_R2:+.4f}  K_eff gains significance: {keff_gains}\")",
          "             if n_hk_le >= 5:",
          "                 logger.info(",
          "-                    f\"  High-K/Low-η panels ({n_hk_le}): \"",
          "+                    f\"  High-K/Low-eta panels ({n_hk_le}): \"",
          "                     f\"mean benefit={hk_le_benefit:+.4f} p={hk_le_pval}\"",
          "                 )",
          " "
        ]
      },
      {
        "oldStart": 448,
        "oldLines": 7,
        "newStart": 315,
        "newLines": 6,
        "lines": [
          "         mean_dR2 = float(np.mean([v[\"delta_R2\"] for v in valid.values()]))",
          "         n_gains = sum(1 for v in valid.values() if v[\"keff_gains_significance\"])",
          " ",
          "-        # Build interpretation",
          "         parts = []",
          "         parts.append(",
          "             f\"K_eff significantly negative in {n_rf_sig}/{nv} conditions under RF \""
        ]
      },
      {
        "oldStart": 456,
        "oldLines": 12,
        "newStart": 322,
        "newLines": 12,
        "lines": [
          "         )",
          "         if mean_dR2 > 0:",
          "             parts.append(",
          "-                f\"RF model explains more variance (mean ΔR²={mean_dR2:+.3f}), \"",
          "+                f\"RF model explains more variance (mean dR2={mean_dR2:+.3f}), \"",
          "                 \"consistent with independent-error majority vote theory.\"",
          "             )",
          "         else:",
          "             parts.append(",
          "-                f\"Adaptive model explains more variance (mean ΔR²={mean_dR2:+.3f}).\"",
          "+                f\"Adaptive model explains more variance (mean dR2={mean_dR2:+.3f}).\"",
          "             )",
          "         if n_gains > nv // 2:",
          "             parts.append("
        ]
      },
      {
        "oldStart": 504,
        "oldLines": 9,
        "newStart": 370,
        "newLines": 8,
        "lines": [
          "     if \"interpretation\" in summary:",
          "         logger.info(f\"\\n  {summary['interpretation']}\")",
          " ",
          "-    # Comparison table",
          "     valid_keys = [k for k in condition_results if not condition_results[k].get(\"skipped\")]",
          "-    logger.info(f\"\\n{'Condition':<35} {'Adap R²':>8} {'RF R²':>8} {'ΔR²':>7} {'Adap Kp':>8} {'RF Kp':>8} {'Gains':>5}\")",
          "+    logger.info(f\"\\n{'Condition':<35} {'Adap R2':>8} {'RF R2':>8} {'dR2':>7} {'Adap Kp':>8} {'RF Kp':>8} {'Gains':>5}\")",
          "     logger.info(\"-\" * 85)",
          "     for ck in valid_keys:",
          "         r = condition_results[ck]"
        ]
      }
    ],
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Plan 001 Step 5: Random-fault simulation — 455 panels × 12 conditions.\n\nInput:\n  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json\n  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/\n  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json\n\nOutput:\n  - artifacts/results/plan001/panel_regression/step5_random_fault_results.json\n\nDependencies: numpy, scipy, statsmodels\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport warnings\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy import stats\n\nfrom src.utils import setup_logging\n\nlogger = setup_logging(\"plan001_step5\")\n\n# ── Constants ────────────────────────────────────────────────────────\nLOCAL_MODELS = [\n    \"qwen2.5-72b\", \"llama3.1-70b\", \"mistral-large\",\n    \"qwen2.5-32b\", \"qwen2.5-14b\", \"llama3.1-8b\",\n]\nAPI_MODELS = [\n    \"claude-opus-4\", \"gpt-5.5\", \"gemini-2.5-pro\", \"gpt-4.1\",\n    \"claude-sonnet-4\", \"gpt-4o\", \"gemini-2.5-flash\",\n    \"gpt-4o-mini\", \"claude-3-haiku\",\n]\nALL_MODELS = LOCAL_MODELS + API_MODELS\nDATASETS = [\"mmlu\", \"arc_challenge\"]\nATTACKS = [\n    \"prompt_injection\", \"sycophancy\", \"score_manipulation\",\n    \"verbosity_bias\", \"position_bias\", \"authority_bias\",\n]\nEPS = 0.001\nN_SIMS = 1000\nN_SAMPLES = 300\nSIM_BATCH = 100\n\nRESULTS_DIR = Path(\"/root/cert_manip_resist_eval/artifacts/results\")\nPLAN001_DIR = RESULTS_DIR / \"plan001\"\nSCORES_DIR = PLAN001_DIR / \"individual_scores\"\nMI_PATH = PLAN001_DIR / \"mi_matrix\" / \"mi_matrix_15models.json\"\nCKPT_FILES = [\n    RESULTS_DIR / \"_taxonomy_checkpoint.json\",\n    RESULTS_DIR / \"_step2v3_checkpoint.json\",\n]\nOUTPUT_DIR = PLAN001_DIR / \"panel_regression\"\n\n\n# ── JSON Helper ──────────────────────────────────────────────────────\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\n# ── Data Loading (shared with Step 4) ────────────────────────────────\n\ndef load_mi_data():\n    if not MI_PATH.exists():\n        logger.error(f\"MI matrix not found: {MI_PATH}\")\n        sys.exit(1)\n    with open(MI_PATH) as f:\n        data = json.load(f)\n    logger.info(f\"Loaded MI matrix: {len(data['models'])} models\")\n    return data\n\n\ndef load_pairs():\n    for ckpt_path in CKPT_FILES:\n        if not ckpt_path.exists():\n            continue\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        if \"pairs\" not in data:\n            continue\n        pairs = {}\n        for ds in DATASETS:\n            if ds in data[\"pairs\"]:\n                pairs[ds] = data[\"pairs\"][ds][:300]\n                logger.info(f\"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}\")\n        if pairs:\n            return pairs\n    logger.error(\"No pairs found in any checkpoint file\")\n    sys.exit(1)\n\n\ndef _invert_winners(scores):\n    swap = {\"A\": \"B\", \"B\": \"A\", \"tie\": \"tie\"}\n    return [{**s, \"winner\": swap.get(s.get(\"winner\", \"tie\"), \"tie\")} for s in scores]\n\n\ndef load_all_scores():\n    clean = {ds: {} for ds in DATASETS}\n    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}\n\n    for ckpt_path in CKPT_FILES:\n        if not ckpt_path.exists():\n            continue\n        logger.info(f\"Loading checkpoint: {ckpt_path.name}\")\n        with open(ckpt_path) as f:\n            data = json.load(f)\n        for ds in DATASETS:\n            for mid, scores in data.get(\"clean_scores\", {}).get(ds, {}).items():\n                if mid not in clean[ds]:\n                    clean[ds][mid] = scores\n            for atk in ATTACKS:\n                for mid, scores in data.get(\"attacked_scores\", {}).get(ds, {}).get(atk, {}).items():\n                    if mid not in attacked[ds][atk]:\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    if SCORES_DIR.exists():\n        logger.info(f\"Loading individual scores from {SCORES_DIR}\")\n        for mid in ALL_MODELS:\n            for ds in DATASETS:\n                fp = SCORES_DIR / f\"{mid}__{ds}__clean.json\"\n                if fp.exists() and mid not in clean[ds]:\n                    with open(fp) as f:\n                        clean[ds][mid] = json.load(f).get(\"scores\", [])\n                for atk in ATTACKS:\n                    fp = SCORES_DIR / f\"{mid}__{ds}__{atk}.json\"\n                    if fp.exists() and mid not in attacked[ds][atk]:\n                        with open(fp) as f:\n                            scores = json.load(f).get(\"scores\", [])\n                        if atk == \"position_bias\":\n                            scores = _invert_winners(scores)\n                        attacked[ds][atk][mid] = scores\n\n    for ds in DATASETS:\n        nc = len(clean[ds])\n        logger.info(f\"  {ds} clean: {nc}/{len(ALL_MODELS)}\")\n        for atk in ATTACKS:\n            na = len(attacked[ds][atk])\n            if na > 0:\n                logger.info(f\"  {ds} {atk}: {na}/{len(ALL_MODELS)}\")\n\n    return clean, attacked\n\n\n# ── ASR Computation ──────────────────────────────────────────────────\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\n# ── Random-Fault Simulation ─────────────────────────────────────────\n\ndef analytical_rf_asr(eta):\n    \"\"\"Analytical P(panel error) for majority vote with 3 independent judges.\n    P(≥2 fail) = η₁η₂ + η₁η₃ + η₂η₃ - 2η₁η₂η₃\"\"\"\n    e1, e2, e3 = eta\n    return e1 * e2 + e1 * e3 + e2 * e3 - 2.0 * e1 * e2 * e3\n\n\ndef simulate_rf_vectorized(eta_all, rng):\n    \"\"\"Simulate random-fault ASR for all panels.\n\n    Args:\n        eta_all: (n_panels, 3) array of individual judge error rates\n        rng: numpy random generator\n\n    Returns:\n        rf_mean: (n_panels,) mean RF ASR across simulations\n        rf_std: (n_panels,) std RF ASR across simulations\n    \"\"\"\n    n_panels = eta_all.shape[0]\n    rf_sum = np.zeros(n_panels)\n    rf_sq_sum = np.zeros(n_panels)\n\n    for sim_start in range(0, N_SIMS, SIM_BATCH):\n        b = min(SIM_BATCH, N_SIMS - sim_start)\n        # (n_panels, batch, n_samples, 3) random draws\n        randoms = rng.random((n_panels, b, N_SAMPLES, 3))\n        # Each judge errors independently with probability eta_j\n        errors = randoms < eta_all[:, np.newaxis, np.newaxis, :]\n        # Majority vote: panel errs if ≥2 judges err\n        panel_err = errors.sum(axis=3) >= 2\n        # Error rate per sim: (n_panels, batch)\n        rates = panel_err.mean(axis=2).astype(np.float64)\n        rf_sum += rates.sum(axis=1)\n        rf_sq_sum += (rates ** 2).sum(axis=1)\n\n    rf_mean = rf_sum / N_SIMS\n    rf_std = np.sqrt(np.maximum(rf_sq_sum / N_SIMS - rf_mean ** 2, 0.0))\n    return rf_mean, rf_std\n\n\n# ── Regression ───────────────────────────────────────────────────────\n\ndef run_ols(y_raw, keffs, eta_maxs):\n    \"\"\"Simple OLS: log(y+ε) ~ log(K_eff) + log(η_max+ε).\"\"\"\n    y = np.log(y_raw + EPS)\n    X = np.column_stack([np.log(keffs), np.log(eta_maxs + EPS)])\n    Xc = sm.add_constant(X)\n    fit = sm.OLS(y, Xc).fit()\n    return {\n        \"keff_beta\": float(fit.params[1]),\n        \"keff_t\": float(fit.tvalues[1]),\n        \"keff_p\": float(fit.pvalues[1]),\n        \"eta_max_beta\": float(fit.params[2]),\n        \"eta_max_t\": float(fit.tvalues[2]),\n        \"eta_max_p\": float(fit.pvalues[2]),\n        \"R2\": float(fit.rsquared),\n        \"adj_R2\": float(fit.rsquared_adj),\n    }\n\n\n# ── Main ─────────────────────────────────────────────────────────────\n\ndef main():\n    logger.info(\"=\" * 60)\n    logger.info(\"Plan 001 Step 5: Random-Fault Simulation\")\n    logger.info(f\"  {N_SIMS} simulations × {N_SAMPLES} samples per panel\")\n    logger.info(\"=\" * 60)\n\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    # Precompute individual ASR\n    logger.info(\"\\nPrecomputing individual ASR...\")\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    logger.info(f\"  Computed {len(ind_asr)} individual ASR values\")\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n    rng = np.random.default_rng(42)\n\n    condition_results = {}\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        for atk in ATTACKS:\n            cond = f\"{ds}×{atk}\"\n            logger.info(f\"\\n--- {cond} ---\")\n\n            # Collect panel data\n            panel_keffs = []\n            panel_eta_maxs = []\n            panel_eta_all = []  # (n_panels, 3) for simulation\n            panel_adaptive_asrs = []\n            panel_jids_list = []\n            skipped = 0\n\n            for combo in all_combos:\n                jids = [ALL_MODELS[i] for i in combo]\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    skipped += 1\n                    continue\n                pk = \"|\".join(jids)\n                if pk not in keff_data:\n                    skipped += 1\n                    continue\n\n                keff = keff_data[pk][\"keff\"]\n                etas = [ind_asr[(ds, atk, j)] for j in jids]\n\n                # Adaptive panel ASR (majority vote on actual scores)\n                cs = {j: clean[ds][j] for j in jids}\n                ats = {j: attacked[ds][atk][j] for j in jids}\n                adaptive_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n                panel_keffs.append(keff)\n                panel_eta_maxs.append(max(etas))\n                panel_eta_all.append(etas)\n                panel_adaptive_asrs.append(adaptive_asr)\n                panel_jids_list.append(jids)\n\n            n_panels = len(panel_keffs)\n            logger.info(f\"  {n_panels} panels with data, {skipped} skipped\")\n\n            if n_panels < 10:\n                logger.warning(f\"  Too few panels ({n_panels}), skipping\")\n                condition_results[cond] = {\"n_panels\": n_panels, \"skipped\": True}\n                continue\n\n            keffs = np.array(panel_keffs)\n            eta_maxs = np.array(panel_eta_maxs)\n            eta_all = np.array(panel_eta_all)  # (n_panels, 3)\n            adaptive_asrs = np.array(panel_adaptive_asrs)\n\n            # ── Random-fault simulation ──\n            logger.info(f\"  Simulating {N_SIMS} RF runs...\")\n            rf_mean, rf_std = simulate_rf_vectorized(eta_all, rng)\n\n            # Analytical validation\n            analytical = np.array([analytical_rf_asr(e) for e in eta_all])\n            max_dev = np.max(np.abs(rf_mean - analytical))\n            logger.info(f\"  RF simulation done. Max deviation from analytical: {max_dev:.6f}\")\n\n            # ── Regressions ──\n            # Adaptive\n            if np.std(adaptive_asrs) < 1e-10:\n                logger.warning(f\"  Constant adaptive ASR, skipping regression\")\n                adaptive_ols = {\"keff_beta\": 0, \"keff_p\": 1, \"R2\": 0, \"note\": \"constant_asr\"}\n            else:\n                adaptive_ols = run_ols(adaptive_asrs, keffs, eta_maxs)\n\n            # Random-fault\n            if np.std(rf_mean) < 1e-10:\n                logger.warning(f\"  Constant RF ASR, skipping regression\")\n                rf_ols = {\"keff_beta\": 0, \"keff_p\": 1, \"R2\": 0, \"note\": \"constant_asr\"}\n            else:\n                rf_ols = run_ols(rf_mean, keffs, eta_maxs)\n\n            delta_R2 = rf_ols.get(\"R2\", 0) - adaptive_ols.get(\"R2\", 0)\n            keff_gains = (\n                rf_ols.get(\"keff_p\", 1) < 0.05\n                and rf_ols.get(\"keff_p\", 1) < adaptive_ols.get(\"keff_p\", 1)\n            )\n\n            # ── High-K_eff + Low-η_max benefit analysis ──\n            keff_q75 = np.percentile(keffs, 75)\n            eta_q25 = np.percentile(eta_maxs, 25)\n            hk_le_mask = (keffs >= keff_q75) & (eta_maxs <= eta_q25)\n            n_hk_le = int(hk_le_mask.sum())\n            hk_le_benefit = None\n            hk_le_pval = None\n            if n_hk_le >= 5:\n                diff = adaptive_asrs[hk_le_mask] - rf_mean[hk_le_mask]\n                hk_le_benefit = float(np.mean(diff))\n                if np.std(diff) > 1e-10:\n                    _, hk_le_pval = stats.ttest_1samp(diff, 0)\n                    hk_le_pval = float(hk_le_pval)\n\n            cond_res = {\n                \"n_panels\": n_panels,\n                \"skipped\": False,\n                \"adaptive\": adaptive_ols,\n                \"random_fault\": rf_ols,\n                \"delta_R2\": float(delta_R2),\n                \"keff_gains_significance\": bool(keff_gains),\n                \"rf_stats\": {\n                    \"mean\": float(np.mean(rf_mean)),\n                    \"std\": float(np.mean(rf_std)),\n                    \"max_analytical_deviation\": float(max_dev),\n                },\n                \"adaptive_stats\": {\n                    \"mean\": float(np.mean(adaptive_asrs)),\n                    \"std\": float(np.std(adaptive_asrs)),\n                },\n                \"high_keff_low_eta\": {\n                    \"n_panels\": n_hk_le,\n                    \"keff_threshold\": float(keff_q75),\n                    \"eta_threshold\": float(eta_q25),\n                    \"mean_benefit_adaptive_minus_rf\": hk_le_benefit,\n                    \"benefit_pval\": hk_le_pval,\n                },\n            }\n            condition_results[cond] = cond_res\n\n            logger.info(\n                f\"  Adaptive: K_eff β={adaptive_ols.get('keff_beta', 0):+.4f} \"\n                f\"p={adaptive_ols.get('keff_p', 1):.4f} R²={adaptive_ols.get('R2', 0):.4f}\"\n            )\n            logger.info(\n                f\"  RF:       K_eff β={rf_ols.get('keff_beta', 0):+.4f} \"\n                f\"p={rf_ols.get('keff_p', 1):.4f} R²={rf_ols.get('R2', 0):.4f}\"\n            )\n            logger.info(f\"  ΔR²={delta_R2:+.4f}  K_eff gains significance: {keff_gains}\")\n            if n_hk_le >= 5:\n                logger.info(\n                    f\"  High-K/Low-η panels ({n_hk_le}): \"\n                    f\"mean benefit={hk_le_benefit:+.4f} p={hk_le_pval}\"\n                )\n\n    # ── Summary ──\n    valid = {k: v for k, v in condition_results.items() if not v.get(\"skipped\")}\n    nv = len(valid)\n\n    if nv > 0:\n        n_adapt_sig = sum(\n            1 for v in valid.values()\n            if v[\"adaptive\"].get(\"keff_p\", 1) < 0.05 and v[\"adaptive\"].get(\"keff_beta\", 0) < 0\n        )\n        n_rf_sig = sum(\n            1 for v in valid.values()\n            if v[\"random_fault\"].get(\"keff_p\", 1) < 0.05 and v[\"random_fault\"].get(\"keff_beta\", 0) < 0\n        )\n        mean_dR2 = float(np.mean([v[\"delta_R2\"] for v in valid.values()]))\n        n_gains = sum(1 for v in valid.values() if v[\"keff_gains_significance\"])\n\n        # Build interpretation\n        parts = []\n        parts.append(\n            f\"K_eff significantly negative in {n_rf_sig}/{nv} conditions under RF \"\n            f\"vs {n_adapt_sig}/{nv} under adaptive.\"\n        )\n        if mean_dR2 > 0:\n            parts.append(\n                f\"RF model explains more variance (mean ΔR²={mean_dR2:+.3f}), \"\n                \"consistent with independent-error majority vote theory.\"\n            )\n        else:\n            parts.append(\n                f\"Adaptive model explains more variance (mean ΔR²={mean_dR2:+.3f}).\"\n            )\n        if n_gains > nv // 2:\n            parts.append(\n                f\"K_eff gains significance in {n_gains}/{nv} conditions under RF, \"\n                \"suggesting diversity benefit is undermined by adaptive attacks.\"\n            )\n        interpretation = \" \".join(parts)\n\n        summary = {\n            \"adaptive_keff_sig_negative\": f\"{n_adapt_sig}/{nv}\",\n            \"random_fault_keff_sig_negative\": f\"{n_rf_sig}/{nv}\",\n            \"mean_delta_R2\": mean_dR2,\n            \"keff_gains_significance_count\": f\"{n_gains}/{nv}\",\n            \"interpretation\": interpretation,\n        }\n    else:\n        summary = {\"note\": \"No valid conditions to summarize\"}\n\n    output = {\n        \"n_panels\": 455,\n        \"n_simulations\": N_SIMS,\n        \"n_samples_per_sim\": N_SAMPLES,\n        \"models\": ALL_MODELS,\n        \"conditions\": condition_results,\n        \"summary\": summary,\n    }\n\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n    out_path = OUTPUT_DIR / \"step5_random_fault_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    logger.info(f\"\\nResults saved: {out_path}\")\n\n    logger.info(\"\\n\" + \"=\" * 60)\n    logger.info(\"SUMMARY\")\n    logger.info(\"=\" * 60)\n    for k, v in summary.items():\n        if k != \"interpretation\":\n            logger.info(f\"  {k}: {v}\")\n    if \"interpretation\" in summary:\n        logger.info(f\"\\n  {summary['interpretation']}\")\n\n    # Comparison table\n    valid_keys = [k for k in condition_results if not condition_results[k].get(\"skipped\")]\n    logger.info(f\"\\n{'Condition':<35} {'Adap R²':>8} {'RF R²':>8} {'ΔR²':>7} {'Adap Kp':>8} {'RF Kp':>8} {'Gains':>5}\")\n    logger.info(\"-\" * 85)\n    for ck in valid_keys:\n        r = condition_results[ck]\n        a = r[\"adaptive\"]\n        rf = r[\"random_fault\"]\n        logger.info(\n            f\"  {ck:<33} {a.get('R2', 0):>8.4f} {rf.get('R2', 0):>8.4f} \"\n            f\"{r['delta_R2']:>+7.3f} {a.get('keff_p', 1):>8.4f} {rf.get('keff_p', 1):>8.4f} \"\n            f\"{'Y' if r['keff_gains_significance'] else 'N':>5}\"\n        )\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 63_

写 pipeline 启动脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "a96cc195-989c-448a-8f80-5fce924f276d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1sYHQGZjxpyiLx7SyqPTH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10896,
      "cache_read_input_tokens": 89304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10896
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

_source line 64_

<details open><summary>🔧 Tool call — Write · `toolu_01TYDbac6Ynt7y4bmYSGi6oU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_pipeline_15model.sh",
  "content": "#!/bin/bash\n# 15-model pipeline: Step 3 -> Confound -> Step 4 -> Step 5\n# Prereq: individual_scores/ has all 9 API model x 14 condition JSON files\nset -e\ncd /root/cert_manip_resist_eval\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n\necho \"=== Step 3: MI Matrix (105 pairs, 455 panels) ===\"\npython scripts/run_plan001_step3_mi_matrix.py\n\necho \"\"\necho \"=== Confound Diagnosis ===\"\npython scripts/run_plan001_confound_diagnosis.py\n\necho \"\"\necho \"=== Step 4: Panel Regression (455 panels x 12 conditions) ===\"\npython scripts/run_plan001_step4_panel_regression.py\n\necho \"\"\necho \"=== Step 5: Random-Fault Simulation (455 panels x 1000 sims) ===\"\npython scripts/run_plan001_step5_random_fault.py\n\necho \"\"\necho \"=== PIPELINE COMPLETE ===\"\necho \"Results in: /root/cert_manip_resist_eval/artifacts/results/plan001/\"\nls -la /root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/ 2>/dev/null\nls -la /root/cert_manip_resist_eval/artifacts/results/plan001/panel_regression/ 2>/dev/null\nls -la /root/cert_manip_resist_eval/artifacts/results/plan001/confound_*.{json,png} 2>/dev/null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "eba627a7-5eb4-42b3-a32f-c033d913809c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T1sYHQGZjxpyiLx7SyqPTH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10896,
      "cache_read_input_tokens": 89304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10896
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

_source line 65 · 2026-05-22T15:03:03.503Z_

<details><summary>↩ Tool result · `toolu_01TYDbac6Ynt7y4bmYSGi6oU`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_pipeline_15model.sh
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "5352ea6e-3c89-47e4-93cc-ecb2ea93fbaf",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_pipeline_15model.sh",
    "content": "#!/bin/bash\n# 15-model pipeline: Step 3 -> Confound -> Step 4 -> Step 5\n# Prereq: individual_scores/ has all 9 API model x 14 condition JSON files\nset -e\ncd /root/cert_manip_resist_eval\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n\necho \"=== Step 3: MI Matrix (105 pairs, 455 panels) ===\"\npython scripts/run_plan001_step3_mi_matrix.py\n\necho \"\"\necho \"=== Confound Diagnosis ===\"\npython scripts/run_plan001_confound_diagnosis.py\n\necho \"\"\necho \"=== Step 4: Panel Regression (455 panels x 12 conditions) ===\"\npython scripts/run_plan001_step4_panel_regression.py\n\necho \"\"\necho \"=== Step 5: Random-Fault Simulation (455 panels x 1000 sims) ===\"\npython scripts/run_plan001_step5_random_fault.py\n\necho \"\"\necho \"=== PIPELINE COMPLETE ===\"\necho \"Results in: /root/cert_manip_resist_eval/artifacts/results/plan001/\"\nls -la /root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/ 2>/dev/null\nls -la /root/cert_manip_resist_eval/artifacts/results/plan001/panel_regression/ 2>/dev/null\nls -la /root/cert_manip_resist_eval/artifacts/results/plan001/confound_*.{json,png} 2>/dev/null\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 66_

SCP 所有文件到服务器。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "b1d3dc69-ee6c-46c3-8e00-f2a7335e4e64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgrLfEEGb4LpmU3YH3B5UB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 100200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 681
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

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_01DJyrdX55cMMec26q37mS7C`</summary>

```json
{
  "command": "scp /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/unified_data_loader.py seetacloud-rtx6000:/root/cert_manip_resist_eval/src/unified_data_loader.py",
  "description": "SCP unified_data_loader.py to server"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "8d889237-dc44-4469-ba88-8786ea49bacf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgrLfEEGb4LpmU3YH3B5UB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 100200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 681
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

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_01GqMXy5BZ2Yb7uj56PeuUsA`</summary>

```json
{
  "command": "scp /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py seetacloud-rtx6000:/root/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py",
  "description": "SCP step3 script to server"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "5040f459-e4ca-4ff2-a10c-6587fd826685",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgrLfEEGb4LpmU3YH3B5UB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 100200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 681
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

_source line 69 · 2026-05-22T15:03:09.554Z_

<details><summary>↩ Tool result · `toolu_01DJyrdX55cMMec26q37mS7C`</summary>

```text
Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "1bb12a53-42d3-4ea5-88fd-2a6489722440",
  "tool_use_result": {
    "stdout": "Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.",
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

_source line 70_

<details open><summary>🔧 Tool call — Bash · `toolu_01T9RPUa6Sk4uDCVUb3rcPc4`</summary>

```json
{
  "command": "scp /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_confound_diagnosis.py seetacloud-rtx6000:/root/cert_manip_resist_eval/scripts/run_plan001_confound_diagnosis.py",
  "description": "SCP confound script to server"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "a8eed594-984b-4495-ac9a-3ef071784ff9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgrLfEEGb4LpmU3YH3B5UB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 100200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 681
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

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_01UTRDaV66qBFjQs44un49HQ`</summary>

```json
{
  "command": "scp /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py seetacloud-rtx6000:/root/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py",
  "description": "SCP step4 script to server"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "907a28b8-4876-4e16-86a9-12b4841e1545",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgrLfEEGb4LpmU3YH3B5UB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 100200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 681
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

_source line 72 · 2026-05-22T15:03:11.111Z_

<details><summary>↩ Tool result · `toolu_01GqMXy5BZ2Yb7uj56PeuUsA`</summary>

```text
Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "8e72affb-d9a5-45ab-aa72-715b8036c708",
  "tool_use_result": {
    "stdout": "Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.",
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

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_018idVWGexYPAhkif29VnHeq`</summary>

```json
{
  "command": "scp /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step5_random_fault.py seetacloud-rtx6000:/root/cert_manip_resist_eval/scripts/run_plan001_step5_random_fault.py",
  "description": "SCP step5 script to server"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "c1f56126-cb92-47d9-9136-52f5e6141e15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgrLfEEGb4LpmU3YH3B5UB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 100200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 681
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

_source line 74_

<details open><summary>🔧 Tool call — Bash · `toolu_01XEWGs7tEG21zPohiSxa236`</summary>

```json
{
  "command": "scp /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_pipeline_15model.sh seetacloud-rtx6000:/root/cert_manip_resist_eval/scripts/run_pipeline_15model.sh",
  "description": "SCP pipeline launcher to server"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "9e30354d-6c4e-4c2f-a75c-92e380053026",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgrLfEEGb4LpmU3YH3B5UB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 100200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 681
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

_source line 75 · 2026-05-22T15:03:12.753Z_

<details><summary>↩ Tool result · `toolu_01T9RPUa6Sk4uDCVUb3rcPc4`</summary>

```text
Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "73138ae1-e999-42db-a0fa-3c4e629cceed",
  "tool_use_result": {
    "stdout": "Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-22T15:03:14.471Z_

<details><summary>↩ Tool result · `toolu_01UTRDaV66qBFjQs44un49HQ`</summary>

```text
Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "c04e1d8a-2eab-471f-b5ef-7bc3b42613bf",
  "tool_use_result": {
    "stdout": "Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-22T15:03:16.157Z_

<details><summary>↩ Tool result · `toolu_018idVWGexYPAhkif29VnHeq`</summary>

```text
Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "5f9f1cd3-7d3f-42a4-9962-b4a8393985a8",
  "tool_use_result": {
    "stdout": "Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-22T15:03:17.795Z_

<details><summary>↩ Tool result · `toolu_01XEWGs7tEG21zPohiSxa236`</summary>

```text
Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "867259a9-688b-4816-bbd7-48df9d21fdad",
  "tool_use_result": {
    "stdout": "Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.",
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

_source line 79_

所有文件已传。设置执行权限并做 dry-run 验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "a4e588ec-258f-4a5c-ba80-c3e1f3de8b23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1dWDKk3EHv8Px2sPc8VU1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 100881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1205
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

_source line 80_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_011xGWbjewpgWZXTabb75AkU`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "chmod +x /root/cert_manip_resist_eval/scripts/run_pipeline_15model.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "b05760db-d9a9-460e-89dc-1cf790056abe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1dWDKk3EHv8Px2sPc8VU1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 100881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1205
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

_source line 81 · 2026-05-22T15:03:21.895Z_

<details><summary>↩ Tool result · `toolu_011xGWbjewpgWZXTabb75AkU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "c5d4e475-79cc-49e7-9618-cdac9d6d4ee8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01HUBwEFBz23hZ8Dg1akCfXX`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cd /root/cert_manip_resist_eval && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nfrom src.unified_data_loader import (\n    ALL_MODELS, LOCAL_MODELS, API_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data, load_api_asr, validate_coverage,\n)\nprint(f'ALL_MODELS: {len(ALL_MODELS)} models')\nprint(f'  Local: {LOCAL_MODELS}')\nprint(f'  API:   {API_MODELS}')\nprint(f'DATASETS: {DATASETS}')\nprint(f'ATTACKS:  {ATTACKS}')\nprint()\n\n# Test load_all_scores\nclean, attacked = load_all_scores()\nprint('--- Coverage ---')\nfor ds in DATASETS:\n    nc = len(clean[ds])\n    print(f'{ds} clean: {nc}/{len(ALL_MODELS)} models')\n    for atk in ATTACKS:\n        na = len(attacked[ds][atk])\n        if na > 0:\n            print(f'  {atk}: {na} models')\n\n# Test load_pairs\npairs = load_pairs()\nfor ds, p in pairs.items():\n    print(f'Pairs {ds}: {len(p)}')\n\nprint()\nprint('loader OK')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "87a515c2-7522-4225-948d-06e0b11f70bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAvpcf5zRtwcvPzvMNfzGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 208,
      "cache_read_input_tokens": 102086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 208
      },
      "output_tokens": 72,
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

_source line 83 · 2026-05-22T15:03:30.398Z_

<details><summary>↩ Tool result · `toolu_01HUBwEFBz23hZ8Dg1akCfXX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"ALL_MODELS: 15 models\\n  Local: ['qwen2.5-72b', 'llama3.1-70b', 'mistral-large', 'qwen2.5-32b', 'qwen2.5-14b', 'llama3.1-8b']\\n  API:   ['claude-opus-4', 'gpt-5.5', 'gemini-2.5-pro', 'gpt-4.1', 'claude-sonnet-4', 'gpt-4o', 'gemini-2.5-flash', 'gpt-4o-mini', 'claude-3-haiku']\\nDATASETS: ['mmlu', 'arc_challenge']\\nATTACKS:  ['prompt_injection', 'sycophancy', 'score_manipulation', 'verbosity_bias', 'position_bias', 'authority_bias']\\n\\n--- Coverage ---\\nmmlu clean: 8/15 models\\n  prompt_injection: 8 models\\n  sycophancy: 8 models\\n  score_manipulation: 8 models\\n  verbosity_bias: 8 models\\n  position_bias: 8 models\\n  authority_bias: 8 models\\narc_challenge clean: 8/15 models\\n  prompt_injection: 8 models\\n  sycophancy: 7 models\\n  score_manipulation: 7 models\\n  verbosity_bias: 7 models\\n  position_bias: 7 models\\n  authority_bias: 7 models\\nPairs mmlu: 300\\nPairs arc_challenge: 300\\n\\nloader OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "0e9ef2ba-9cd4-4428-b350-3408bcd083f8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"ALL_MODELS: 15 models\\\\n  Local: ['qwen2.5-72b', 'llama3.1-70b', 'mistral-large', 'qwen2.5-32b', 'qwen2.5-14b', 'llama3.1-8b']\\\\n  API:   ['claude-opus-4', 'gpt-5.5', 'gemini-2.5-pro', 'gpt-4.1', 'claude-sonnet-4', 'gpt-4o', 'gemini-2.5-flash', 'gpt-4o-mini', 'claude-3-haiku']\\\\nDATASETS: ['mmlu', 'arc_challenge']\\\\nATTACKS:  ['prompt_injection', 'sycophancy', 'score_manipulation', 'verbosity_bias', 'position_bias', 'authority_bias']\\\\n\\\\n--- Coverage ---\\\\nmmlu clean: 8/15 models\\\\n  prompt_injection: 8 models\\\\n  sycophancy: 8 models\\\\n  score_manipulation: 8 models\\\\n  verbosity_bias: 8 models\\\\n  position_bias: 8 models\\\\n  authority_bias: 8 models\\\\narc_challenge clean: 8/15 models\\\\n  prompt_injection: 8 models\\\\n  sycophancy: 7 models\\\\n  score_manipulation: 7 models\\\\n  verbosity_bias: 7 models\\\\n  position_bias: 7 models\\\\n  authority_bias: 7 models\\\\nPairs mmlu: 300\\\\nPairs arc_challenge: 300\\\\n\\\\nloader OK\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.71}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"ALL_MODELS: 15 models\\n  Local: ['qwen2.5-72b', 'llama3.1-70b', 'mistral-large', 'qwen2.5-32b', 'qwen2.5-14b', 'llama3.1-8b']\\n  API:   ['claude-opus-4', 'gpt-5.5', 'gemini-2.5-pro', 'gpt-4.1', 'claude-sonnet-4', 'gpt-4o', 'gemini-2.5-flash', 'gpt-4o-mini', 'claude-3-haiku']\\nDATASETS: ['mmlu', 'arc_challenge']\\nATTACKS:  ['prompt_injection', 'sycophancy', 'score_manipulation', 'verbosity_bias', 'position_bias', 'authority_bias']\\n\\n--- Coverage ---\\nmmlu clean: 8/15 models\\n  prompt_injection: 8 models\\n  sycophancy: 8 models\\n  score_manipulation: 8 models\\n  verbosity_bias: 8 models\\n  position_bias: 8 models\\n  authority_bias: 8 models\\narc_challenge clean: 8/15 models\\n  prompt_injection: 8 models\\n  sycophancy: 7 models\\n  score_manipulation: 7 models\\n  verbosity_bias: 7 models\\n  position_bias: 7 models\\n  authority_bias: 7 models\\nPairs mmlu: 300\\nPairs arc_challenge: 300\\n\\nloader OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.71}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 84_

<details><summary>Logged reasoning block</summary>

```text
Loader works. Now let me verify that each script can import correctly too.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "fe581667-8f04-4f69-8d21-8e1f5c39c2e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gw2WY9pbhYf8bBxhgqNoo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 102294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1034
      },
      "output_tokens": 22,
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

_source line 85_

Loader 验证通过（8/15 模型可用 = 6 local + haiku + gpt-4o partial）。验证 4 个脚本的 import。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "ead96016-6e54-41c9-a384-862bc3924848",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gw2WY9pbhYf8bBxhgqNoo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 102294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1034
      },
      "output_tokens": 22,
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

_source line 86_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Q5fnT7Xb8eUZX3WnMChg5H`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cd /root/cert_manip_resist_eval && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport importlib, sys\nscripts = [\n    'scripts.run_plan001_step3_mi_matrix',\n    'scripts.run_plan001_confound_diagnosis',\n    'scripts.run_plan001_step4_panel_regression',\n    'scripts.run_plan001_step5_random_fault',\n]\nsys.path.insert(0, '/root/cert_manip_resist_eval')\nfor s in scripts:\n    # Test that the module can be imported (not executed)\n    mod_path = s.replace('.', '/') + '.py'\n    with open(mod_path) as f:\n        code = f.read()\n    try:\n        compile(code, mod_path, 'exec')\n        print(f'  {s}: syntax OK')\n    except SyntaxError as e:\n        print(f'  {s}: SYNTAX ERROR: {e}')\n\n# Also test actual imports of the unified loader references\nfrom src.unified_data_loader import ALL_MODELS, DATASETS, ATTACKS, PLAN001_DIR, OUTPUT_DIR, SCORES_DIR\nfrom src.unified_data_loader import load_all_scores, load_pairs, load_mi_data, load_api_asr\nprint('  All imports OK')\nprint(f'  C(15,2) = {15*14//2} pairs')\nprint(f'  C(15,3) = {15*14*13//(3*2*1)} panels')\nprint(f'  {len(DATASETS)} datasets x {len(ATTACKS)} attacks = {len(DATASETS)*len(ATTACKS)} conditions')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "cf3f4011-e7e6-49a7-9758-5e39b0688002",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gw2WY9pbhYf8bBxhgqNoo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 102294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1034
      },
      "output_tokens": 22,
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

_source line 87 · 2026-05-22T15:03:42.021Z_

<details><summary>↩ Tool result · `toolu_01Q5fnT7Xb8eUZX3WnMChg5H`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  scripts.run_plan001_step3_mi_matrix: syntax OK\\n  scripts.run_plan001_confound_diagnosis: syntax OK\\n  scripts.run_plan001_step4_panel_regression: syntax OK\\n  scripts.run_plan001_step5_random_fault: syntax OK\\n  All imports OK\\n  C(15,2) = 105 pairs\\n  C(15,3) = 455 panels\\n  2 datasets x 6 attacks = 12 conditions\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.62}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "36fdffa6-f935-493a-8ed9-e0f13379d0fe",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  scripts.run_plan001_step3_mi_matrix: syntax OK\\\\n  scripts.run_plan001_confound_diagnosis: syntax OK\\\\n  scripts.run_plan001_step4_panel_regression: syntax OK\\\\n  scripts.run_plan001_step5_random_fault: syntax OK\\\\n  All imports OK\\\\n  C(15,2) = 105 pairs\\\\n  C(15,3) = 455 panels\\\\n  2 datasets x 6 attacks = 12 conditions\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.62}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  scripts.run_plan001_step3_mi_matrix: syntax OK\\n  scripts.run_plan001_confound_diagnosis: syntax OK\\n  scripts.run_plan001_step4_panel_regression: syntax OK\\n  scripts.run_plan001_step5_random_fault: syntax OK\\n  All imports OK\\n  C(15,2) = 105 pairs\\n  C(15,3) = 455 panels\\n  2 datasets x 6 attacks = 12 conditions\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.62}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 88_

确认目录结构就绪。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "5582cb23-0c1f-46a5-aa2b-22ac5222f590",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSUkzN1gKHFg44neuEh33n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 103328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 792
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

_source line 89_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Th7My7TRv56itvGSgeGAZH`</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "ls -la /root/cert_manip_resist_eval/artifacts/results/plan001/individual_scores/ /root/cert_manip_resist_eval/scripts/run_pipeline_15model.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "42b0eef4-1933-45a6-8d44-4d193bbc5aec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSUkzN1gKHFg44neuEh33n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 103328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 792
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

_source line 90 · 2026-05-22T15:03:46.002Z_

<details><summary>↩ Tool result · `toolu_01Th7My7TRv56itvGSgeGAZH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rwxr-xr-x 1 root root 1103 May 22 23:03 /root/cert_manip_resist_eval/scripts/run_pipeline_15model.sh\\n\\n/root/cert_manip_resist_eval/artifacts/results/plan001/individual_scores/:\\ntotal 3452\\ndrwxr-xr-x 2 root root   4096 May 22 17:36 .\\ndrwxr-xr-x 5 root root    130 May 22 15:44 ..\\n-rw-r--r-- 1 root root 157950 May 22 16:30 claude-3-haiku__arc_challenge__authority_bias.json\\n-rw-r--r-- 1 root root 151830 May 22 16:12 claude-3-haiku__arc_challenge__clean.json\\n-rw-r--r-- 1 root root 151660 May 22 16:27 claude-3-haiku__arc_challenge__position_bias.json\\n-rw-r--r-- 1 root root 154890 May 22 16:15 claude-3-haiku__arc_challenge__prompt_injection.json\\n-rw-r--r-- 1 root root 154977 May 22 16:21 claude-3-haiku__arc_challenge__score_manipulation.json\\n-rw-r--r-- 1 root root 154995 May 22 16:18 claude-3-haiku__arc_challenge__sycophancy.json\\n-rw-r--r-- 1 root root 163364 May 22 16:23 claude-3-haiku__arc_challenge__verbosity_bias.json\\n-rw-r--r-- 1 root root 154207 May 22 16:08 claude-3-haiku__mmlu__authority_bias.json\\n-rw-r--r-- 1 root root 150723 May 22 15:49 claude-3-haiku__mmlu__clean.json\\n-rw-r--r-- 1 root root 150601 May 22 16:05 claude-3-haiku__mmlu__position_bias.json\\n-rw-r--r-- 1 root root 154083 May 22 15:52 claude-3-haiku__mmlu__prompt_injection.json\\n-rw-r--r-- 1 root root 152097 May 22 15:59 claude-3-haiku__mmlu__score_manipulation.json\\n-rw-r--r-- 1 root root 149719 May 22 15:55 claude-3-haiku__mmlu__sycophancy.json\\n-rw-r--r-- 1 root root 156472 May 22 16:02 claude-3-haiku__mmlu__verbosity_bias.json\\n-rw-r--r-- 1 root root 135818 May 22 16:59 gpt-4o__arc_challenge__clean.json\\n-rw-r--r-- 1 root root 143586 May 22 17:16 gpt-4o__arc_challenge__prompt_injection.json\\n-rw-r--r-- 1 root root 148463 May 22 16:55 gpt-4o__mmlu__authority_bias.json\\n-rw-r--r-- 1 root root 143377 May 22 16:33 gpt-4o__mmlu__clean.json\\n-rw-r--r-- 1 root root 145117 May 22 16:52 gpt-4o__mmlu__position_bias.json\\n-rw-r--r-- 1 root root 151811 May 22 16:37 gpt-4o__mmlu__prompt_injection.json\\n-rw-r--r-- 1 root root 148081 May 22 16:45 gpt-4o__mmlu__score_manipulation.json\\n-rw-r--r-- 1 root root 147667 May 22 16:41 gpt-4o__mmlu__sycophancy.json\\n-rw-r--r-- 1 root root 154018 May 22 16:48 gpt-4o__mmlu__verbosity_bias.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "f2fb1c43-b1ff-499b-a889-524c452ab8bd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"-rwxr-xr-x 1 root root 1103 May 22 23:03 /root/cert_manip_resist_eval/scripts/run_pipeline_15model.sh\\\\n\\\\n/root/cert_manip_resist_eval/artifacts/results/plan001/individual_scores/:\\\\ntotal 3452\\\\ndrwxr-xr-x 2 root root   4096 May 22 17:36 .\\\\ndrwxr-xr-x 5 root root    130 May 22 15:44 ..\\\\n-rw-r--r-- 1 root root 157950 May 22 16:30 claude-3-haiku__arc_challenge__authority_bias.json\\\\n-rw-r--r-- 1 root root 151830 May 22 16:12 claude-3-haiku__arc_challenge__clean.json\\\\n-rw-r--r-- 1 root root 151660 May 22 16:27 claude-3-haiku__arc_challenge__position_bias.json\\\\n-rw-r--r-- 1 root root 154890 May 22 16:15 claude-3-haiku__arc_challenge__prompt_injection.json\\\\n-rw-r--r-- 1 root root 154977 May 22 16:21 claude-3-haiku__arc_challenge__score_manipulation.json\\\\n-rw-r--r-- 1 root root 154995 May 22 16:18 claude-3-haiku__arc_challenge__sycophancy.json\\\\n-rw-r--r-- 1 root root 163364 May 22 16:23 claude-3-haiku__arc_challenge__verbosity_bias.json\\\\n-rw-r--r-- 1 root root 154207 May 22 16:08 claude-3-haiku__mmlu__authority_bias.json\\\\n-rw-r--r-- 1 root root 150723 May 22 15:49 claude-3-haiku__mmlu__clean.json\\\\n-rw-r--r-- 1 root root 150601 May 22 16:05 claude-3-haiku__mmlu__position_bias.json\\\\n-rw-r--r-- 1 root root 154083 May 22 15:52 claude-3-haiku__mmlu__prompt_injection.json\\\\n-rw-r--r-- 1 root root 152097 May 22 15:59 claude-3-haiku__mmlu__score_manipulation.json\\\\n-rw-r--r-- 1 root root 149719 May 22 15:55 claude-3-haiku__mmlu__sycophancy.json\\\\n-rw-r--r-- 1 root root 156472 May 22 16:02 claude-3-haiku__mmlu__verbosity_bias.json\\\\n-rw-r--r-- 1 root root 135818 May 22 16:59 gpt-4o__arc_challenge__clean.json\\\\n-rw-r--r-- 1 root root 143586 May 22 17:16 gpt-4o__arc_challenge__prompt_injection.json\\\\n-rw-r--r-- 1 root root 148463 May 22 16:55 gpt-4o__mmlu__authority_bias.json\\\\n-rw-r--r-- 1 root root 143377 May 22 16:33 gpt-4o__mmlu__clean.json\\\\n-rw-r--r-- 1 root root 145117 May 22 16:52 gpt-4o__mmlu__position_bias.json\\\\n-rw-r--r-- 1 root root 151811 May 22 16:37 gpt-4o__mmlu__prompt_injection.json\\\\n-rw-r--r-- 1 root root 148081 May 22 16:45 gpt-4o__mmlu__score_manipulation.json\\\\n-rw-r--r-- 1 root root 147667 May 22 16:41 gpt-4o__mmlu__sycophancy.json\\\\n-rw-r--r-- 1 root root 154018 May 22 16:48 gpt-4o__mmlu__verbosity_bias.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"-rwxr-xr-x 1 root root 1103 May 22 23:03 /root/cert_manip_resist_eval/scripts/run_pipeline_15model.sh\\n\\n/root/cert_manip_resist_eval/artifacts/results/plan001/individual_scores/:\\ntotal 3452\\ndrwxr-xr-x 2 root root   4096 May 22 17:36 .\\ndrwxr-xr-x 5 root root    130 May 22 15:44 ..\\n-rw-r--r-- 1 root root 157950 May 22 16:30 claude-3-haiku__arc_challenge__authority_bias.json\\n-rw-r--r-- 1 root root 151830 May 22 16:12 claude-3-haiku__arc_challenge__clean.json\\n-rw-r--r-- 1 root root 151660 May 22 16:27 claude-3-haiku__arc_challenge__position_bias.json\\n-rw-r--r-- 1 root root 154890 May 22 16:15 claude-3-haiku__arc_challenge__prompt_injection.json\\n-rw-r--r-- 1 root root 154977 May 22 16:21 claude-3-haiku__arc_challenge__score_manipulation.json\\n-rw-r--r-- 1 root root 154995 May 22 16:18 claude-3-haiku__arc_challenge__sycophancy.json\\n-rw-r--r-- 1 root root 163364 May 22 16:23 claude-3-haiku__arc_challenge__verbosity_bias.json\\n-rw-r--r-- 1 root root 154207 May 22 16:08 claude-3-haiku__mmlu__authority_bias.json\\n-rw-r--r-- 1 root root 150723 May 22 15:49 claude-3-haiku__mmlu__clean.json\\n-rw-r--r-- 1 root root 150601 May 22 16:05 claude-3-haiku__mmlu__position_bias.json\\n-rw-r--r-- 1 root root 154083 May 22 15:52 claude-3-haiku__mmlu__prompt_injection.json\\n-rw-r--r-- 1 root root 152097 May 22 15:59 claude-3-haiku__mmlu__score_manipulation.json\\n-rw-r--r-- 1 root root 149719 May 22 15:55 claude-3-haiku__mmlu__sycophancy.json\\n-rw-r--r-- 1 root root 156472 May 22 16:02 claude-3-haiku__mmlu__verbosity_bias.json\\n-rw-r--r-- 1 root root 135818 May 22 16:59 gpt-4o__arc_challenge__clean.json\\n-rw-r--r-- 1 root root 143586 May 22 17:16 gpt-4o__arc_challenge__prompt_injection.json\\n-rw-r--r-- 1 root root 148463 May 22 16:55 gpt-4o__mmlu__authority_bias.json\\n-rw-r--r-- 1 root root 143377 May 22 16:33 gpt-4o__mmlu__clean.json\\n-rw-r--r-- 1 root root 145117 May 22 16:52 gpt-4o__mmlu__position_bias.json\\n-rw-r--r-- 1 root root 151811 May 22 16:37 gpt-4o__mmlu__prompt_injection.json\\n-rw-r--r-- 1 root root 148081 May 22 16:45 gpt-4o__mmlu__score_manipulation.json\\n-rw-r--r-- 1 root root 147667 May 22 16:41 gpt-4o__mmlu__sycophancy.json\\n-rw-r--r-- 1 root root 154018 May 22 16:48 gpt-4o__mmlu__verbosity_bias.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 91_

全部完成。汇报：

## 汇报

### 1. 各脚本原数据加载方式
| 脚本 | 原来 | 变化 |
|------|------|------|
| Step 3 (MI) | 3 个函数: `load_local_clean_scores` + `load_api_clean_scores` + `merge_clean_scores` | → `clean, _ = load_all_scores()` |
| Confound | 3 个函数: `load_local_individual_asr` + `load_api_individual_asr` + `merge_asr` | → `load_all_scores()` + `load_pairs()` + 统一 ASR 计算 |
| Step 4 | 3 个函数: `load_mi_data` + `load_pairs` + `load_all_scores`（本地定义） | → 从 unified_data_loader 导入 |
| Step 5 | 与 Step 4 完全重复的 3 个函数 | → 从 unified_data_loader 导入 |

### 2. 完成项
- **统一加载器** `src/unified_data_loader.py` — 已创建并验证
  - 导出: `ALL_MODELS(15)`, `DATASETS`, `ATTACKS`, 所有路径常量
  - 函数: `load_all_scores()`, `load_pairs()`, `load_mi_data()`, `load_api_asr()`, `validate_coverage()`
  - 自动处理 checkpoint 嵌套格式 + individual JSON 格式
  - position_bias winner 反转统一处理
- **4 个脚本** — 已全部改用统一加载器，去除重复代码
- **Pipeline 启动脚本** `scripts/run_pipeline_15model.sh` — 已创建并设为可执行
- **目录结构** `individual_scores/` — 已就绪

### 3. 验证结果
- `loader OK` — import 验证通过
- 4 个脚本语法检查全部通过
- 当前数据: 8/15 模型 (6 local + haiku + gpt-4o partial)
- C(15,2)=105 pairs, C(15,3)=455 panels, 12 conditions 确认

### 4. Scoring 完成后操作步骤
```bash
# 1. 从本地 scp 9 个 API 模型的 scoring 结果
scp /path/to/individual_scores/*__*.json seetacloud-rtx6000:/root/cert_manip_resist_eval/artifacts/results/plan001/individual_scores/

# 2. 一键启动 pipeline
ssh seetacloud-rtx6000 'bash /root/cert_manip_resist_eval/scripts/run_pipeline_15model.sh'
```

缺 7 个 API 模型的数据 (claude-opus-4, claude-sonnet-4, gpt-5.5, gpt-4.1, gpt-4o-mini, gemini-2.5-pro, gemini-2.5-flash)，加上 gpt-4o 缺 arc_challenge 的 5 个攻击条件。数据到位后零配置启动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "uuid": "44429085-0b79-4bb2-89ec-670be0b0d27a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBmSR3NuoxPsqp2xbL2GVr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1324,
      "cache_read_input_tokens": 104120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1324
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

_source line 92_

全部完成。汇报：

## 汇报

### 1. 各脚本原数据加载方式
| 脚本 | 原来 | 变化 |
|------|------|------|
| Step 3 (MI) | 3 个函数: `load_local_clean_scores` + `load_api_clean_scores` + `merge_clean_scores` | → `clean, _ = load_all_scores()` |
| Confound | 3 个函数: `load_local_individual_asr` + `load_api_individual_asr` + `merge_asr` | → `load_all_scores()` + `load_pairs()` + 统一 ASR 计算 |
| Step 4 | 3 个函数: `load_mi_data` + `load_pairs` + `load_all_scores`（本地定义） | → 从 unified_data_loader 导入 |
| Step 5 | 与 Step 4 完全重复的 3 个函数 | → 从 unified_data_loader 导入 |

### 2. 完成项
- **统一加载器** `src/unified_data_loader.py` — 已创建并验证
  - 导出: `ALL_MODELS(15)`, `DATASETS`, `ATTACKS`, 所有路径常量
  - 函数: `load_all_scores()`, `load_pairs()`, `load_mi_data()`, `load_api_asr()`, `validate_coverage()`
  - 自动处理 checkpoint 嵌套格式 + individual JSON 格式
  - position_bias winner 反转统一处理
- **4 个脚本** — 已全部改用统一加载器，去除重复代码
- **Pipeline 启动脚本** `scripts/run_pipeline_15model.sh` — 已创建并设为可执行
- **目录结构** `individual_scores/` — 已就绪

### 3. 验证结果
- `loader OK` — import 验证通过
- 4 个脚本语法检查全部通过
- 当前数据: 8/15 模型 (6 local + haiku + gpt-4o partial)
- C(15,2)=105 pairs, C(15,3)=455 panels, 12 conditions 确认

### 4. Scoring 完成后操作步骤
```bash
# 1. 从本地 scp 9 个 API 模型的 scoring 结果
scp /path/to/individual_scores/*__*.json seetacloud-rtx6000:/root/cert_manip_resist_eval/artifacts/results/plan001/individual_scores/

# 2. 一键启动 pipeline
ssh seetacloud-rtx6000 'bash /root/cert_manip_resist_eval/scripts/run_pipeline_15model.sh'
```

缺 7 个 API 模型的数据 (claude-opus-4, claude-sonnet-4, gpt-5.5, gpt-4.1, gpt-4o-mini, gemini-2.5-pro, gemini-2.5-flash)，加上 gpt-4o 缺 arc_challenge 的 5 个攻击条件。数据到位后零配置启动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 482729,
  "duration_api_ms": 474272,
  "num_turns": 34,
  "stop_reason": "end_turn",
  "session_id": "c61b2da9-2ce0-4163-95ea-ea3b046e541e",
  "total_cost_usd": 2.04026925,
  "usage": {
    "input_tokens": 6177,
    "cache_creation_input_tokens": 93997,
    "cache_read_input_tokens": 1220088,
    "output_tokens": 32379,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 93997,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 875,
        "cache_read_input_tokens": 104120,
        "cache_creation_input_tokens": 1324,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1324
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2254,
      "outputTokens": 26,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002384,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6177,
      "outputTokens": 32379,
      "cacheReadInputTokens": 1220088,
      "cacheCreationInputTokens": 93997,
      "webSearchRequests": 0,
      "costUSD": 2.03788525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c5de6ea4-c280-4711-9fe5-f97bdff56d4b"
}
```

</details>

---
