# code audit fix figures

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_code_audit_fix_figures_20260525T203207.log`
- **Structured JSON:** [`4c3defef5bd0f0cff2c3.json`](../../sessions/4c/4c3defef5bd0f0cff2c3.json)

## Before a recorded user message

11 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "3d36139d-2eac-4777-89a6-886ffe3102b5",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "7587fb8b-8f6e-415b-8242-a2a279cedf29",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
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
    "resetsAt": 1779756000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9f38a2f8-fd8a-4dec-8628-890f993c83ba",
  "session_id": "3d36139d-2eac-4777-89a6-886ffe3102b5"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the two scripts on the server to understand the current hardcoded values, then compare them with the correct cross-scored values provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d36139d-2eac-4777-89a6-886ffe3102b5",
  "uuid": "8f7e257e-7b50-4372-a2f5-695b59550dff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cowkj9YL5opgU5vyXUmrw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12913,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12913
      },
      "output_tokens": 28,
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

读取两个脚本的当前内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d36139d-2eac-4777-89a6-886ffe3102b5",
  "uuid": "8b8191bd-b0e0-4b41-a8a7-683e98a1442d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cowkj9YL5opgU5vyXUmrw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12913,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12913
      },
      "output_tokens": 28,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WKahL53Cb9eH5ZsHRNbFKw`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
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
  "session_id": "3d36139d-2eac-4777-89a6-886ffe3102b5",
  "uuid": "2cc8164a-8fca-42e6-b157-68812cf4798b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Cowkj9YL5opgU5vyXUmrw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12913,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12913
      },
      "output_tokens": 28,
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

_source line 7 · 2026-05-25T20:32:20.385Z_

<details><summary>↩ Tool result · `toolu_01WKahL53Cb9eH5ZsHRNbFKw`</summary>

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
  "session_id": "3d36139d-2eac-4777-89a6-886ffe3102b5",
  "uuid": "0b94088a-f618-458a-8095-fdb745f58a83",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 24
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UypQEQGeiNWeaYViRKewbS`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/plot_fig2_merged.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d36139d-2eac-4777-89a6-886ffe3102b5",
  "uuid": "709895e4-da29-4c74-88c0-7972d97c8ffb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5wre3wsLokH8zHh2rghKJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1344,
      "cache_read_input_tokens": 24754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1344
      },
      "output_tokens": 45,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0159ppyG8YMxR8VTmBMC3yNu`</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/scripts/draw_kstar_theta.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d36139d-2eac-4777-89a6-886ffe3102b5",
  "uuid": "bfb0aa5b-17f6-48f5-9a4f-be7e69a3c2a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5wre3wsLokH8zHh2rghKJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1344,
      "cache_read_input_tokens": 24754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1344
      },
      "output_tokens": 45,
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

_source line 10 · 2026-05-25T20:32:26.465Z_

<details><summary>↩ Tool result · `toolu_01UypQEQGeiNWeaYViRKewbS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Merged Figure 2: AUC decay curves with CI shaded bands.\\n\\nCombines the main AUC decay figure and the supplementary CI figure\\ninto a single plot for the main text.\\n\\\"\\\"\\\"\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nfrom pathlib import Path\\n\\nPAIR_KEYS = [\\\"0v1\\\", \\\"1v2\\\", \\\"2v3\\\", \\\"3v4\\\", \\\"4v5\\\"]\\nX_LABELS = [\\\"0 vs 1\\\", \\\"1 vs 2\\\", \\\"2 vs 3\\\", \\\"3 vs 4\\\", \\\"4 vs 5\\\"]\\n\\n# ── Curated data: Table 1 models (C4, 5-fold CV) ────────────────────────────\\n# CI: exact where available from bootstrap; estimated (±0.010 / ±0.002 for 0v1)\\n# at non-boundary pairs, consistent with observed bootstrap CI widths.\\nTABLE1 = {\\n    \\\"Qwen-rw\\\": {\\n        \\\"mean\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\n        \\\"ci_lower\\\": [0.9936, 0.686,  0.580,  0.534,  0.524],\\n        \\\"ci_upper\\\": [0.9976, 0.704,  0.599,  0.553,  0.544],\\n    },\\n    \\\"Pythia\\\": {\\n        \\\"mean\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\n        \\\"ci_lower\\\": [0.9912, 0.645,  0.542,  0.505,  0.504],\\n        \\\"ci_upper\\\": [0.9952, 0.663,  0.563,  0.525,  0.524],\\n    },\\n    \\\"OLMo\\\": {\\n        \\\"mean\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\n        \\\"ci_lower\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\n        \\\"ci_upper\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\n    },\\n    \\\"Qwen-cont\\\": {\\n        \\\"mean\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\n        \\\"ci_lower\\\": [0.9951, 0.602,  0.551,  0.531,  0.504],\\n        \\\"ci_upper\\\": [0.9991, 0.621,  0.571,  0.551,  0.524],\\n    },\\n    r\\\"Qwen-7B$^\\\\ddagger$\\\": {\\n        \\\"mean\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\n        \\\"ci_lower\\\": [0.961,  0.608,  0.539,  0.518,  0.499],\\n        \\\"ci_upper\\\": [0.967,  0.626,  0.559,  0.537,  0.518],\\n    },\\n}\\n\\n# ── Additional models with bootstrap CI (all pairs) ─────────────────────────\\nEXTRA_MODELS = {\\n    \\\"LLaMA-8B\\\": {\\n        \\\"mean\\\":     [0.9225, 0.6123, 0.5274, 0.5169, 0.5162],\\n        \\\"ci_lower\\\": [0.9174, 0.6028, 0.5169, 0.5062, 0.5052],\\n        \\\"ci_upper\\\": [0.9272, 0.6216, 0.5378, 0.5275, 0.5268],\\n    },\\n    \\\"Mistral-7B\\\": {\\n        \\\"mean\\\":     [0.9843, 0.5935, 0.5402, 0.5232, 0.5181],\\n        \\\"ci_lower\\\": [0.9824, 0.5835, 0.5301, 0.5128, 0.5070],\\n        \\\"ci_upper\\\": [0.9860, 0.6032, 0.5510, 0.5338, 0.5287],\\n    },\\n}\\n\\n# ── Decoding strategies (per_fold → approximate CI) ─────────────────────────\\nDECODE_FOLD = {\\n    \\\"Greedy\\\": {\\n        \\\"mean\\\": [0.9992, 0.8838, 0.5342, 0.5228, 0.5162],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9996, 0.9991, 0.9992, 0.9996, 0.9984],\\n            \\\"1v2\\\": [0.8906, 0.8766, 0.8847, 0.881, 0.8861],\\n            \\\"2v3\\\": [0.5188, 0.542, 0.5264, 0.5364, 0.5473],\\n            \\\"3v4\\\": [0.5223, 0.5135, 0.5187, 0.5355, 0.5239],\\n            \\\"4v5\\\": [0.5272, 0.5108, 0.5124, 0.5128, 0.5177],\\n        },\\n    },\\n    r\\\"Nuc $p{=}0.9$\\\": {\\n        \\\"mean\\\": [0.9948, 0.677, 0.5549, 0.5299, 0.5013],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9957, 0.9951, 0.9939, 0.9942, 0.9952],\\n            \\\"1v2\\\": [0.6875, 0.6745, 0.6838, 0.6631, 0.6763],\\n            \\\"2v3\\\": [0.548, 0.5563, 0.5534, 0.5638, 0.5531],\\n            \\\"3v4\\\": [0.525, 0.5494, 0.5317, 0.5301, 0.5133],\\n            \\\"4v5\\\": [0.5257, 0.4903, 0.4898, 0.5, 0.5008],\\n        },\\n    },\\n    r\\\"$T{=}0.7$\\\": {\\n        \\\"mean\\\": [0.9965, 0.7265, 0.5941, 0.5698, 0.5284],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9977, 0.9972, 0.9956, 0.9972, 0.995],\\n            \\\"1v2\\\": [0.7367, 0.7367, 0.7255, 0.7121, 0.7214],\\n            \\\"2v3\\\": [0.6009, 0.5951, 0.5954, 0.5754, 0.6036],\\n            \\\"3v4\\\": [0.5521, 0.5739, 0.5801, 0.5784, 0.5643],\\n            \\\"4v5\\\": [0.5209, 0.529, 0.5222, 0.5358, 0.5343],\\n        },\\n    },\\n    r\\\"$T{=}1.2$\\\": {\\n        \\\"mean\\\": [0.9933, 0.6172, 0.5226, 0.517, 0.5051],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9938, 0.9949, 0.9929, 0.9922, 0.9929],\\n            \\\"1v2\\\": [0.6193, 0.5961, 0.6182, 0.6258, 0.6265],\\n            \\\"2v3\\\": [0.5285, 0.5246, 0.5219, 0.5254, 0.5123],\\n            \\\"3v4\\\": [0.5464, 0.5142, 0.4998, 0.5028, 0.5218],\\n            \\\"4v5\\\": [0.5048, 0.5059, 0.5053, 0.4936, 0.5162],\\n        },\\n    },\\n}\\n\\nTABLEAU = [\\n    \\\"#4e79a7\\\", \\\"#e15759\\\", \\\"#76b7b2\\\", \\\"#59a14f\\\", \\\"#b07aa1\\\",\\n    \\\"#ff9da7\\\", \\\"#9c755f\\\", \\\"#edc948\\\", \\\"#f28e2b\\\", \\\"#bab0ac\\\",\\n    \\\"#86bcb6\\\",\\n]\\nMARKERS = [\\\"o\\\", \\\"s\\\", \\\"^\\\", \\\"D\\\", \\\"v\\\", \\\"P\\\", \\\"X\\\", \\\"*\\\", \\\"h\\\", \\\"<\\\", \\\">\\\"]\\n\\n\\ndef fold_ci(folds):\\n    arr = np.array(folds)\\n    m = arr.mean()\\n    se = arr.std(ddof=1) / np.sqrt(len(arr))\\n    return m - 1.96 * se, m + 1.96 * se\\n\\n\\ndef main():\\n    x = np.arange(len(PAIR_KEYS))\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 10,\\n        \\\"axes.linewidth\\\": 0.8,\\n        \\\"xtick.major.width\\\": 0.8,\\n        \\\"ytick.major.width\\\": 0.8,\\n    })\\n\\n    fig, ax = plt.subplots(figsize=(7, 4.2), constrained_layout=True)\\n\\n    # Reference lines\\n    ax.axhline(0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.608, r\\\"$\\\\theta = 0.60$\\\",\\n            fontsize=8, color=\\\"grey\\\", va=\\\"bottom\\\", ha=\\\"right\\\")\\n    ax.axhline(0.50, color=\\\"lightgrey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.507, \\\"chance\\\",\\n            fontsize=8, color=\\\"silver\\\", va=\\\"bottom\\\", ha=\\\"right\\\")\\n\\n    ci = 0\\n    model_handles = []\\n    decode_handles = []\\n\\n    # ── Model configs (solid + CI bands) ─────────────────────────────────\\n    all_models = {}\\n    all_models.update(TABLE1)\\n    all_models.update(EXTRA_MODELS)\\n\\n    for label, data in all_models.items():\\n        color = TABLEAU[ci % len(TABLEAU)]\\n        marker = MARKERS[ci % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n        lo = data[\\\"ci_lower\\\"]\\n        hi = data[\\\"ci_upper\\\"]\\n\\n        ax.fill_between(x, lo, hi, color=color, alpha=0.18, zorder=2,\\n                         linewidth=0)\\n        line, = ax.plot(x, means, \\\"-\\\", color=color, lw=1.6, marker=marker,\\n                        markersize=4.5, label=label, zorder=3)\\n        model_handles.append(line)\\n        ci += 1\\n\\n    # ── Decoding strategies (dashed, no CI bands) ────────────────────────\\n    for label, data in DECODE_FOLD.items():\\n        color = TABLEAU[ci % len(TABLEAU)]\\n        marker = MARKERS[ci % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n\\n        line, = ax.plot(x, means, \\\"--\\\", color=color, lw=1.4, marker=marker,\\n                        markersize=4, label=label, zorder=3)\\n        decode_handles.append(line)\\n        ci += 1\\n\\n    # ── Axes ─────────────────────────────────────────────────────────────\\n    ax.set_xticks(x)\\n    ax.set_xticklabels(X_LABELS)\\n    ax.set_xlabel(\\\"Depth Pair\\\", fontsize=10.5)\\n    ax.set_ylabel(\\\"Pairwise AUC\\\", fontsize=10.5)\\n    ax.set_ylim(0.45, 1.05)\\n    ax.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\n    ax.tick_params(direction=\\\"in\\\")\\n\\n    # ── Legends ──────────────────────────────────────────────────────────\\n    leg1 = ax.legend(handles=model_handles, title=\\\"Models\\\", title_fontsize=8.5,\\n                     fontsize=7.5, loc=\\\"upper right\\\", bbox_to_anchor=(1.0, 0.98),\\n                     framealpha=0.92, edgecolor=\\\"0.85\\\", handlelength=2.0)\\n    ax.add_artist(leg1)\\n    if decode_handles:\\n        ax.legend(handles=decode_handles, title=\\\"Decoding\\\", title_fontsize=8.5,\\n                  fontsize=7.5, loc=\\\"center right\\\", bbox_to_anchor=(1.0, 0.42),\\n                  framealpha=0.92, edgecolor=\\\"0.85\\\", handlelength=2.0)\\n\\n    # ── Save ─────────────────────────────────────────────────────────────\\n    out_dir = Path(__file__).resolve().parent.parent / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\n    out_dir.mkdir(parents=True, exist_ok=True)\\n\\n    pdf_path = out_dir / \\\"fig2_auc_decay.pdf\\\"\\n    png_path = out_dir / \\\"fig2_auc_decay.png\\\"\\n    fig.savefig(pdf_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    plt.close(fig)\\n\\n    print(f\\\"PDF: {pdf_path} ({pdf_path.stat().st_size/1024:.1f} KB)\\\")\\n    print(f\\\"PNG: {png_path} ({png_path.stat().st_size/1024:.1f} KB)\\\")\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d36139d-2eac-4777-89a6-886ffe3102b5",
  "uuid": "3695fa8c-a355-4122-a44f-e2263f050786",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Merged Figure 2: AUC decay curves with CI shaded bands.\\\\n\\\\nCombines the main AUC decay figure and the supplementary CI figure\\\\ninto a single plot for the main text.\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\nimport matplotlib.pyplot as plt\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\n\\\\nPAIR_KEYS = [\\\\\\\"0v1\\\\\\\", \\\\\\\"1v2\\\\\\\", \\\\\\\"2v3\\\\\\\", \\\\\\\"3v4\\\\\\\", \\\\\\\"4v5\\\\\\\"]\\\\nX_LABELS = [\\\\\\\"0 vs 1\\\\\\\", \\\\\\\"1 vs 2\\\\\\\", \\\\\\\"2 vs 3\\\\\\\", \\\\\\\"3 vs 4\\\\\\\", \\\\\\\"4 vs 5\\\\\\\"]\\\\n\\\\n# ── Curated data: Table 1 models (C4, 5-fold CV) ────────────────────────────\\\\n# CI: exact where available from bootstrap; estimated (±0.010 / ±0.002 for 0v1)\\\\n# at non-boundary pairs, consistent with observed bootstrap CI widths.\\\\nTABLE1 = {\\\\n    \\\\\\\"Qwen-rw\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9936, 0.686,  0.580,  0.534,  0.524],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9976, 0.704,  0.599,  0.553,  0.544],\\\\n    },\\\\n    \\\\\\\"Pythia\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9912, 0.645,  0.542,  0.505,  0.504],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9952, 0.663,  0.563,  0.525,  0.524],\\\\n    },\\\\n    \\\\\\\"OLMo\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\\\n    },\\\\n    \\\\\\\"Qwen-cont\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9951, 0.602,  0.551,  0.531,  0.504],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9991, 0.621,  0.571,  0.551,  0.524],\\\\n    },\\\\n    r\\\\\\\"Qwen-7B$^\\\\\\\\ddagger$\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.961,  0.608,  0.539,  0.518,  0.499],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.967,  0.626,  0.559,  0.537,  0.518],\\\\n    },\\\\n}\\\\n\\\\n# ── Additional models with bootstrap CI (all pairs) ─────────────────────────\\\\nEXTRA_MODELS = {\\\\n    \\\\\\\"LLaMA-8B\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9225, 0.6123, 0.5274, 0.5169, 0.5162],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9174, 0.6028, 0.5169, 0.5062, 0.5052],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9272, 0.6216, 0.5378, 0.5275, 0.5268],\\\\n    },\\\\n    \\\\\\\"Mistral-7B\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9843, 0.5935, 0.5402, 0.5232, 0.5181],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9824, 0.5835, 0.5301, 0.5128, 0.5070],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9860, 0.6032, 0.5510, 0.5338, 0.5287],\\\\n    },\\\\n}\\\\n\\\\n# ── Decoding strategies (per_fold → approximate CI) ─────────────────────────\\\\nDECODE_FOLD = {\\\\n    \\\\\\\"Greedy\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": [0.9992, 0.8838, 0.5342, 0.5228, 0.5162],\\\\n        \\\\\\\"folds\\\\\\\": {\\\\n            \\\\\\\"0v1\\\\\\\": [0.9996, 0.9991, 0.9992, 0.9996, 0.9984],\\\\n            \\\\\\\"1v2\\\\\\\": [0.8906, 0.8766, 0.8847, 0.881, 0.8861],\\\\n            \\\\\\\"2v3\\\\\\\": [0.5188, 0.542, 0.5264, 0.5364, 0.5473],\\\\n            \\\\\\\"3v4\\\\\\\": [0.5223, 0.5135, 0.5187, 0.5355, 0.5239],\\\\n            \\\\\\\"4v5\\\\\\\": [0.5272, 0.5108, 0.5124, 0.5128, 0.5177],\\\\n        },\\\\n    },\\\\n    r\\\\\\\"Nuc $p{=}0.9$\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": [0.9948, 0.677, 0.5549, 0.5299, 0.5013],\\\\n        \\\\\\\"folds\\\\\\\": {\\\\n            \\\\\\\"0v1\\\\\\\": [0.9957, 0.9951, 0.9939, 0.9942, 0.9952],\\\\n            \\\\\\\"1v2\\\\\\\": [0.6875, 0.6745, 0.6838, 0.6631, 0.6763],\\\\n            \\\\\\\"2v3\\\\\\\": [0.548, 0.5563, 0.5534, 0.5638, 0.5531],\\\\n            \\\\\\\"3v4\\\\\\\": [0.525, 0.5494, 0.5317, 0.5301, 0.5133],\\\\n            \\\\\\\"4v5\\\\\\\": [0.5257, 0.4903, 0.4898, 0.5, 0.5008],\\\\n        },\\\\n    },\\\\n    r\\\\\\\"$T{=}0.7$\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": [0.9965, 0.7265, 0.5941, 0.5698, 0.5284],\\\\n        \\\\\\\"folds\\\\\\\": {\\\\n            \\\\\\\"0v1\\\\\\\": [0.9977, 0.9972, 0.9956, 0.9972, 0.995],\\\\n            \\\\\\\"1v2\\\\\\\": [0.7367, 0.7367, 0.7255, 0.7121, 0.7214],\\\\n            \\\\\\\"2v3\\\\\\\": [0.6009, 0.5951, 0.5954, 0.5754, 0.6036],\\\\n            \\\\\\\"3v4\\\\\\\": [0.5521, 0.5739, 0.5801, 0.5784, 0.5643],\\\\n            \\\\\\\"4v5\\\\\\\": [0.5209, 0.529, 0.5222, 0.5358, 0.5343],\\\\n        },\\\\n    },\\\\n    r\\\\\\\"$T{=}1.2$\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": [0.9933, 0.6172, 0.5226, 0.517, 0.5051],\\\\n        \\\\\\\"folds\\\\\\\": {\\\\n            \\\\\\\"0v1\\\\\\\": [0.9938, 0.9949, 0.9929, 0.9922, 0.9929],\\\\n            \\\\\\\"1v2\\\\\\\": [0.6193, 0.5961, 0.6182, 0.6258, 0.6265],\\\\n            \\\\\\\"2v3\\\\\\\": [0.5285, 0.5246, 0.5219, 0.5254, 0.5123],\\\\n            \\\\\\\"3v4\\\\\\\": [0.5464, 0.5142, 0.4998, 0.5028, 0.5218],\\\\n            \\\\\\\"4v5\\\\\\\": [0.5048, 0.5059, 0.5053, 0.4936, 0.5162],\\\\n        },\\\\n    },\\\\n}\\\\n\\\\nTABLEAU = [\\\\n    \\\\\\\"#4e79a7\\\\\\\", \\\\\\\"#e15759\\\\\\\", \\\\\\\"#76b7b2\\\\\\\", \\\\\\\"#59a14f\\\\\\\", \\\\\\\"#b07aa1\\\\\\\",\\\\n    \\\\\\\"#ff9da7\\\\\\\", \\\\\\\"#9c755f\\\\\\\", \\\\\\\"#edc948\\\\\\\", \\\\\\\"#f28e2b\\\\\\\", \\\\\\\"#bab0ac\\\\\\\",\\\\n    \\\\\\\"#86bcb6\\\\\\\",\\\\n]\\\\nMARKERS = [\\\\\\\"o\\\\\\\", \\\\\\\"s\\\\\\\", \\\\\\\"^\\\\\\\", \\\\\\\"D\\\\\\\", \\\\\\\"v\\\\\\\", \\\\\\\"P\\\\\\\", \\\\\\\"X\\\\\\\", \\\\\\\"*\\\\\\\", \\\\\\\"h\\\\\\\", \\\\\\\"<\\\\\\\", \\\\\\\">\\\\\\\"]\\\\n\\\\n\\\\ndef fold_ci(folds):\\\\n    arr = np.array(folds)\\\\n    m = arr.mean()\\\\n    se = arr.std(ddof=1) / np.sqrt(len(arr))\\\\n    return m - 1.96 * se, m + 1.96 * se\\\\n\\\\n\\\\ndef main():\\\\n    x = np.arange(len(PAIR_KEYS))\\\\n\\\\n    plt.rcParams.update({\\\\n        \\\\\\\"font.family\\\\\\\": \\\\\\\"serif\\\\\\\",\\\\n        \\\\\\\"font.size\\\\\\\": 10,\\\\n        \\\\\\\"axes.linewidth\\\\\\\": 0.8,\\\\n        \\\\\\\"xtick.major.width\\\\\\\": 0.8,\\\\n        \\\\\\\"ytick.major.width\\\\\\\": 0.8,\\\\n    })\\\\n\\\\n    fig, ax = plt.subplots(figsize=(7, 4.2), constrained_layout=True)\\\\n\\\\n    # Reference lines\\\\n    ax.axhline(0.60, color=\\\\\\\"grey\\\\\\\", ls=\\\\\\\"--\\\\\\\", lw=0.8, zorder=1)\\\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.608, r\\\\\\\"$\\\\\\\\theta = 0.60$\\\\\\\",\\\\n            fontsize=8, color=\\\\\\\"grey\\\\\\\", va=\\\\\\\"bottom\\\\\\\", ha=\\\\\\\"right\\\\\\\")\\\\n    ax.axhline(0.50, color=\\\\\\\"lightgrey\\\\\\\", ls=\\\\\\\"--\\\\\\\", lw=0.8, zorder=1)\\\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.507, \\\\\\\"chance\\\\\\\",\\\\n            fontsize=8, color=\\\\\\\"silver\\\\\\\", va=\\\\\\\"bottom\\\\\\\", ha=\\\\\\\"right\\\\\\\")\\\\n\\\\n    ci = 0\\\\n    model_handles = []\\\\n    decode_handles = []\\\\n\\\\n    # ── Model configs (solid + CI bands) ─────────────────────────────────\\\\n    all_models = {}\\\\n    all_models.update(TABLE1)\\\\n    all_models.update(EXTRA_MODELS)\\\\n\\\\n    for label, data in all_models.items():\\\\n        color = TABLEAU[ci % len(TABLEAU)]\\\\n        marker = MARKERS[ci % len(MARKERS)]\\\\n        means = data[\\\\\\\"mean\\\\\\\"]\\\\n        lo = data[\\\\\\\"ci_lower\\\\\\\"]\\\\n        hi = data[\\\\\\\"ci_upper\\\\\\\"]\\\\n\\\\n        ax.fill_between(x, lo, hi, color=color, alpha=0.18, zorder=2,\\\\n                         linewidth=0)\\\\n        line, = ax.plot(x, means, \\\\\\\"-\\\\\\\", color=color, lw=1.6, marker=marker,\\\\n                        markersize=4.5, label=label, zorder=3)\\\\n        model_handles.append(line)\\\\n        ci += 1\\\\n\\\\n    # ── Decoding strategies (dashed, no CI bands) ────────────────────────\\\\n    for label, data in DECODE_FOLD.items():\\\\n        color = TABLEAU[ci % len(TABLEAU)]\\\\n        marker = MARKERS[ci % len(MARKERS)]\\\\n        means = data[\\\\\\\"mean\\\\\\\"]\\\\n\\\\n        line, = ax.plot(x, means, \\\\\\\"--\\\\\\\", color=color, lw=1.4, marker=marker,\\\\n                        markersize=4, label=label, zorder=3)\\\\n        decode_handles.append(line)\\\\n        ci += 1\\\\n\\\\n    # ── Axes ─────────────────────────────────────────────────────────────\\\\n    ax.set_xticks(x)\\\\n    ax.set_xticklabels(X_LABELS)\\\\n    ax.set_xlabel(\\\\\\\"Depth Pair\\\\\\\", fontsize=10.5)\\\\n    ax.set_ylabel(\\\\\\\"Pairwise AUC\\\\\\\", fontsize=10.5)\\\\n    ax.set_ylim(0.45, 1.05)\\\\n    ax.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\\\n    ax.tick_params(direction=\\\\\\\"in\\\\\\\")\\\\n\\\\n    # ── Legends ──────────────────────────────────────────────────────────\\\\n    leg1 = ax.legend(handles=model_handles, title=\\\\\\\"Models\\\\\\\", title_fontsize=8.5,\\\\n                     fontsize=7.5, loc=\\\\\\\"upper right\\\\\\\", bbox_to_anchor=(1.0, 0.98),\\\\n                     framealpha=0.92, edgecolor=\\\\\\\"0.85\\\\\\\", handlelength=2.0)\\\\n    ax.add_artist(leg1)\\\\n    if decode_handles:\\\\n        ax.legend(handles=decode_handles, title=\\\\\\\"Decoding\\\\\\\", title_fontsize=8.5,\\\\n                  fontsize=7.5, loc=\\\\\\\"center right\\\\\\\", bbox_to_anchor=(1.0, 0.42),\\\\n                  framealpha=0.92, edgecolor=\\\\\\\"0.85\\\\\\\", handlelength=2.0)\\\\n\\\\n    # ── Save ─────────────────────────────────────────────────────────────\\\\n    out_dir = Path(__file__).resolve().parent.parent / \\\\\\\"docs\\\\\\\" / \\\\\\\"paper\\\\\\\" / \\\\\\\"figures\\\\\\\"\\\\n    out_dir.mkdir(parents=True, exist_ok=True)\\\\n\\\\n    pdf_path = out_dir / \\\\\\\"fig2_auc_decay.pdf\\\\\\\"\\\\n    png_path = out_dir / \\\\\\\"fig2_auc_decay.png\\\\\\\"\\\\n    fig.savefig(pdf_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    fig.savefig(png_path, dpi=300, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    plt.close(fig)\\\\n\\\\n    print(f\\\\\\\"PDF: {pdf_path} ({pdf_path.stat().st_size/1024:.1f} KB)\\\\\\\")\\\\n    print(f\\\\\\\"PNG: {png_path} ({png_path.stat().st_size/1024:.1f} KB)\\\\\\\")\\\\n    print(\\\\\\\"OK\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.81}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Merged Figure 2: AUC decay curves with CI shaded bands.\\n\\nCombines the main AUC decay figure and the supplementary CI figure\\ninto a single plot for the main text.\\n\\\"\\\"\\\"\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nfrom pathlib import Path\\n\\nPAIR_KEYS = [\\\"0v1\\\", \\\"1v2\\\", \\\"2v3\\\", \\\"3v4\\\", \\\"4v5\\\"]\\nX_LABELS = [\\\"0 vs 1\\\", \\\"1 vs 2\\\", \\\"2 vs 3\\\", \\\"3 vs 4\\\", \\\"4 vs 5\\\"]\\n\\n# ── Curated data: Table 1 models (C4, 5-fold CV) ────────────────────────────\\n# CI: exact where available from bootstrap; estimated (±0.010 / ±0.002 for 0v1)\\n# at non-boundary pairs, consistent with observed bootstrap CI widths.\\nTABLE1 = {\\n    \\\"Qwen-rw\\\": {\\n        \\\"mean\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\n        \\\"ci_lower\\\": [0.9936, 0.686,  0.580,  0.534,  0.524],\\n        \\\"ci_upper\\\": [0.9976, 0.704,  0.599,  0.553,  0.544],\\n    },\\n    \\\"Pythia\\\": {\\n        \\\"mean\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\n        \\\"ci_lower\\\": [0.9912, 0.645,  0.542,  0.505,  0.504],\\n        \\\"ci_upper\\\": [0.9952, 0.663,  0.563,  0.525,  0.524],\\n    },\\n    \\\"OLMo\\\": {\\n        \\\"mean\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\n        \\\"ci_lower\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\n        \\\"ci_upper\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\n    },\\n    \\\"Qwen-cont\\\": {\\n        \\\"mean\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\n        \\\"ci_lower\\\": [0.9951, 0.602,  0.551,  0.531,  0.504],\\n        \\\"ci_upper\\\": [0.9991, 0.621,  0.571,  0.551,  0.524],\\n    },\\n    r\\\"Qwen-7B$^\\\\ddagger$\\\": {\\n        \\\"mean\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\n        \\\"ci_lower\\\": [0.961,  0.608,  0.539,  0.518,  0.499],\\n        \\\"ci_upper\\\": [0.967,  0.626,  0.559,  0.537,  0.518],\\n    },\\n}\\n\\n# ── Additional models with bootstrap CI (all pairs) ─────────────────────────\\nEXTRA_MODELS = {\\n    \\\"LLaMA-8B\\\": {\\n        \\\"mean\\\":     [0.9225, 0.6123, 0.5274, 0.5169, 0.5162],\\n        \\\"ci_lower\\\": [0.9174, 0.6028, 0.5169, 0.5062, 0.5052],\\n        \\\"ci_upper\\\": [0.9272, 0.6216, 0.5378, 0.5275, 0.5268],\\n    },\\n    \\\"Mistral-7B\\\": {\\n        \\\"mean\\\":     [0.9843, 0.5935, 0.5402, 0.5232, 0.5181],\\n        \\\"ci_lower\\\": [0.9824, 0.5835, 0.5301, 0.5128, 0.5070],\\n        \\\"ci_upper\\\": [0.9860, 0.6032, 0.5510, 0.5338, 0.5287],\\n    },\\n}\\n\\n# ── Decoding strategies (per_fold → approximate CI) ─────────────────────────\\nDECODE_FOLD = {\\n    \\\"Greedy\\\": {\\n        \\\"mean\\\": [0.9992, 0.8838, 0.5342, 0.5228, 0.5162],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9996, 0.9991, 0.9992, 0.9996, 0.9984],\\n            \\\"1v2\\\": [0.8906, 0.8766, 0.8847, 0.881, 0.8861],\\n            \\\"2v3\\\": [0.5188, 0.542, 0.5264, 0.5364, 0.5473],\\n            \\\"3v4\\\": [0.5223, 0.5135, 0.5187, 0.5355, 0.5239],\\n            \\\"4v5\\\": [0.5272, 0.5108, 0.5124, 0.5128, 0.5177],\\n        },\\n    },\\n    r\\\"Nuc $p{=}0.9$\\\": {\\n        \\\"mean\\\": [0.9948, 0.677, 0.5549, 0.5299, 0.5013],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9957, 0.9951, 0.9939, 0.9942, 0.9952],\\n            \\\"1v2\\\": [0.6875, 0.6745, 0.6838, 0.6631, 0.6763],\\n            \\\"2v3\\\": [0.548, 0.5563, 0.5534, 0.5638, 0.5531],\\n            \\\"3v4\\\": [0.525, 0.5494, 0.5317, 0.5301, 0.5133],\\n            \\\"4v5\\\": [0.5257, 0.4903, 0.4898, 0.5, 0.5008],\\n        },\\n    },\\n    r\\\"$T{=}0.7$\\\": {\\n        \\\"mean\\\": [0.9965, 0.7265, 0.5941, 0.5698, 0.5284],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9977, 0.9972, 0.9956, 0.9972, 0.995],\\n            \\\"1v2\\\": [0.7367, 0.7367, 0.7255, 0.7121, 0.7214],\\n            \\\"2v3\\\": [0.6009, 0.5951, 0.5954, 0.5754, 0.6036],\\n            \\\"3v4\\\": [0.5521, 0.5739, 0.5801, 0.5784, 0.5643],\\n            \\\"4v5\\\": [0.5209, 0.529, 0.5222, 0.5358, 0.5343],\\n        },\\n    },\\n    r\\\"$T{=}1.2$\\\": {\\n        \\\"mean\\\": [0.9933, 0.6172, 0.5226, 0.517, 0.5051],\\n        \\\"folds\\\": {\\n            \\\"0v1\\\": [0.9938, 0.9949, 0.9929, 0.9922, 0.9929],\\n            \\\"1v2\\\": [0.6193, 0.5961, 0.6182, 0.6258, 0.6265],\\n            \\\"2v3\\\": [0.5285, 0.5246, 0.5219, 0.5254, 0.5123],\\n            \\\"3v4\\\": [0.5464, 0.5142, 0.4998, 0.5028, 0.5218],\\n            \\\"4v5\\\": [0.5048, 0.5059, 0.5053, 0.4936, 0.5162],\\n        },\\n    },\\n}\\n\\nTABLEAU = [\\n    \\\"#4e79a7\\\", \\\"#e15759\\\", \\\"#76b7b2\\\", \\\"#59a14f\\\", \\\"#b07aa1\\\",\\n    \\\"#ff9da7\\\", \\\"#9c755f\\\", \\\"#edc948\\\", \\\"#f28e2b\\\", \\\"#bab0ac\\\",\\n    \\\"#86bcb6\\\",\\n]\\nMARKERS = [\\\"o\\\", \\\"s\\\", \\\"^\\\", \\\"D\\\", \\\"v\\\", \\\"P\\\", \\\"X\\\", \\\"*\\\", \\\"h\\\", \\\"<\\\", \\\">\\\"]\\n\\n\\ndef fold_ci(folds):\\n    arr = np.array(folds)\\n    m = arr.mean()\\n    se = arr.std(ddof=1) / np.sqrt(len(arr))\\n    return m - 1.96 * se, m + 1.96 * se\\n\\n\\ndef main():\\n    x = np.arange(len(PAIR_KEYS))\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 10,\\n        \\\"axes.linewidth\\\": 0.8,\\n        \\\"xtick.major.width\\\": 0.8,\\n        \\\"ytick.major.width\\\": 0.8,\\n    })\\n\\n    fig, ax = plt.subplots(figsize=(7, 4.2), constrained_layout=True)\\n\\n    # Reference lines\\n    ax.axhline(0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.608, r\\\"$\\\\theta = 0.60$\\\",\\n            fontsize=8, color=\\\"grey\\\", va=\\\"bottom\\\", ha=\\\"right\\\")\\n    ax.axhline(0.50, color=\\\"lightgrey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax.text(len(PAIR_KEYS) - 0.45, 0.507, \\\"chance\\\",\\n            fontsize=8, color=\\\"silver\\\", va=\\\"bottom\\\", ha=\\\"right\\\")\\n\\n    ci = 0\\n    model_handles = []\\n    decode_handles = []\\n\\n    # ── Model configs (solid + CI bands) ─────────────────────────────────\\n    all_models = {}\\n    all_models.update(TABLE1)\\n    all_models.update(EXTRA_MODELS)\\n\\n    for label, data in all_models.items():\\n        color = TABLEAU[ci % len(TABLEAU)]\\n        marker = MARKERS[ci % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n        lo = data[\\\"ci_lower\\\"]\\n        hi = data[\\\"ci_upper\\\"]\\n\\n        ax.fill_between(x, lo, hi, color=color, alpha=0.18, zorder=2,\\n                         linewidth=0)\\n        line, = ax.plot(x, means, \\\"-\\\", color=color, lw=1.6, marker=marker,\\n                        markersize=4.5, label=label, zorder=3)\\n        model_handles.append(line)\\n        ci += 1\\n\\n    # ── Decoding strategies (dashed, no CI bands) ────────────────────────\\n    for label, data in DECODE_FOLD.items():\\n        color = TABLEAU[ci % len(TABLEAU)]\\n        marker = MARKERS[ci % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n\\n        line, = ax.plot(x, means, \\\"--\\\", color=color, lw=1.4, marker=marker,\\n                        markersize=4, label=label, zorder=3)\\n        decode_handles.append(line)\\n        ci += 1\\n\\n    # ── Axes ─────────────────────────────────────────────────────────────\\n    ax.set_xticks(x)\\n    ax.set_xticklabels(X_LABELS)\\n    ax.set_xlabel(\\\"Depth Pair\\\", fontsize=10.5)\\n    ax.set_ylabel(\\\"Pairwise AUC\\\", fontsize=10.5)\\n    ax.set_ylim(0.45, 1.05)\\n    ax.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\n    ax.tick_params(direction=\\\"in\\\")\\n\\n    # ── Legends ──────────────────────────────────────────────────────────\\n    leg1 = ax.legend(handles=model_handles, title=\\\"Models\\\", title_fontsize=8.5,\\n                     fontsize=7.5, loc=\\\"upper right\\\", bbox_to_anchor=(1.0, 0.98),\\n                     framealpha=0.92, edgecolor=\\\"0.85\\\", handlelength=2.0)\\n    ax.add_artist(leg1)\\n    if decode_handles:\\n        ax.legend(handles=decode_handles, title=\\\"Decoding\\\", title_fontsize=8.5,\\n                  fontsize=7.5, loc=\\\"center right\\\", bbox_to_anchor=(1.0, 0.42),\\n                  framealpha=0.92, edgecolor=\\\"0.85\\\", handlelength=2.0)\\n\\n    # ── Save ─────────────────────────────────────────────────────────────\\n    out_dir = Path(__file__).resolve().parent.parent / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\n    out_dir.mkdir(parents=True, exist_ok=True)\\n\\n    pdf_path = out_dir / \\\"fig2_auc_decay.pdf\\\"\\n    png_path = out_dir / \\\"fig2_auc_decay.png\\\"\\n    fig.savefig(pdf_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    fig.savefig(png_path, dpi=300, bbox_inches=\\\"tight\\\")\\n    plt.close(fig)\\n\\n    print(f\\\"PDF: {pdf_path} ({pdf_path.stat().st_size/1024:.1f} KB)\\\")\\n    print(f\\\"PNG: {png_path} ({png_path.stat().st_size/1024:.1f} KB)\\\")\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.81}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T20:32:26.928Z_

<details><summary>↩ Tool result · `toolu_0159ppyG8YMxR8VTmBMC3yNu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Figure 3: two-panel K*(theta) figure.\\n\\nPanel (a): Pairwise AUC profile across depth pairs (C4 configs)\\nPanel (b): K*(theta) sensitivity\\n\\nOutput: docs/paper/figures/fig_kstar_theta.pdf\\n\\\"\\\"\\\"\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nfrom pathlib import Path\\n\\nPAIR_KEYS = [\\\"0v1\\\", \\\"1v2\\\", \\\"2v3\\\", \\\"3v4\\\", \\\"4v5\\\"]\\n\\nMODELS = {\\n    \\\"Qwen-rw\\\": {\\n        \\\"mean\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\n        \\\"ci_lower\\\": [0.9946, 0.6859, 0.5795, 0.5333, 0.5238],\\n        \\\"ci_upper\\\": [0.9976, 0.7041, 0.5991, 0.5551, 0.5448],\\n    },\\n    \\\"Pythia\\\": {\\n        \\\"mean\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\n        \\\"ci_lower\\\": [0.9921, 0.6454, 0.5417, 0.5041, 0.5021],\\n        \\\"ci_upper\\\": [0.9943, 0.6630, 0.5628, 0.5260, 0.5249],\\n    },\\n    \\\"OLMo\\\": {\\n        \\\"mean\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\n        \\\"ci_lower\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\n        \\\"ci_upper\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\n    },\\n    \\\"Qwen-cont\\\": {\\n        \\\"mean\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\n        \\\"ci_lower\\\": [0.9963, 0.6015, 0.5511, 0.5308, 0.5035],\\n        \\\"ci_upper\\\": [0.9978, 0.6213, 0.5712, 0.5508, 0.5255],\\n    },\\n    \\\"Qwen-7B\\\": {\\n        \\\"mean\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\n        \\\"ci_lower\\\": [0.9610, 0.6080, 0.5390, 0.5180, 0.4990],\\n        \\\"ci_upper\\\": [0.9670, 0.6260, 0.5590, 0.5370, 0.5180],\\n    },\\n}\\n\\nTABLEAU = [\\n    \\\"#4e79a7\\\", \\\"#e15759\\\", \\\"#76b7b2\\\", \\\"#59a14f\\\", \\\"#b07aa1\\\",\\n    \\\"#ff9da7\\\", \\\"#9c755f\\\", \\\"#bab0ac\\\", \\\"#edc948\\\", \\\"#f28e2b\\\",\\n]\\nMARKERS = [\\\"o\\\", \\\"s\\\", \\\"^\\\", \\\"D\\\", \\\"v\\\", \\\"P\\\", \\\"X\\\", \\\"*\\\", \\\"h\\\", \\\"<\\\"]\\n\\n\\ndef compute_kstar(ci_lowers, theta):\\n    k = 0\\n    for v in ci_lowers:\\n        if v >= theta:\\n            k += 1\\n        else:\\n            break\\n    return k\\n\\n\\ndef main():\\n    x = np.arange(len(PAIR_KEYS))\\n    thetas = np.arange(0.50, 0.751, 0.005)\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 10,\\n        \\\"axes.linewidth\\\": 0.8,\\n        \\\"xtick.direction\\\": \\\"in\\\",\\n        \\\"ytick.direction\\\": \\\"in\\\",\\n        \\\"xtick.major.width\\\": 0.8,\\n        \\\"ytick.major.width\\\": 0.8,\\n    })\\n\\n    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10, 3.5),\\n                                      gridspec_kw={\\\"width_ratios\\\": [1, 1.15]})\\n\\n    # ── Panel (a): Pairwise AUC profile ─────────────────────────────────\\n    ax_a.axhline(0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax_a.text(4.05, 0.607, r\\\"$\\\\theta = 0.60$\\\", fontsize=8, color=\\\"grey\\\",\\n              va=\\\"bottom\\\", ha=\\\"right\\\")\\n\\n    ax_a.axvspan(1.5, 2.5, color=\\\"#4e79a7\\\", alpha=0.06, zorder=0)\\n    ax_a.annotate(r\\\"$K^*\\\\!=\\\\!2$\\\", xy=(1.7, 0.68), fontsize=8, color=\\\"#4e79a7\\\",\\n                  alpha=0.7)\\n\\n    for i, (name, data) in enumerate(MODELS.items()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        marker = MARKERS[i % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n        lo = data[\\\"ci_lower\\\"]\\n        hi = data[\\\"ci_upper\\\"]\\n\\n        ax_a.fill_between(x, lo, hi, color=color, alpha=0.15, linewidth=0)\\n        ax_a.plot(x, means, \\\"-\\\", color=color, lw=1.6, marker=marker,\\n                  markersize=4.5, label=name, zorder=3)\\n\\n    ax_a.set_xticks(x)\\n    ax_a.set_xticklabels(PAIR_KEYS)\\n    ax_a.set_xlabel(\\\"Depth pair\\\")\\n    ax_a.set_ylabel(\\\"Pairwise AUC\\\")\\n    ax_a.set_ylim(0.47, 1.02)\\n    ax_a.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\n    ax_a.legend(fontsize=7.5, loc=\\\"upper right\\\", framealpha=0.92,\\n                edgecolor=\\\"0.85\\\", handlelength=2.0)\\n    ax_a.set_title(r\\\"$\\\\bf{(a)}$\\\" + \\\" Pairwise AUC profile\\\", fontsize=10,\\n                   loc=\\\"left\\\", pad=6)\\n\\n    # ── Panel (b): K*(θ) sensitivity ────────────────────────────────────\\n    all_kstar = {}\\n    for name, data in MODELS.items():\\n        ci_lo = data[\\\"ci_lower\\\"]\\n        ks = [compute_kstar(ci_lo, t) for t in thetas]\\n        all_kstar[name] = ks\\n\\n    kstar_arr = np.array(list(all_kstar.values()))\\n    k_min = kstar_arr.min(axis=0)\\n    k_max = kstar_arr.max(axis=0)\\n\\n    mask_23 = (k_min >= 2) & (k_max <= 3) & (k_min != k_max)\\n    mask_2  = (k_min == 2) & (k_max == 2)\\n\\n    for j in range(len(thetas)):\\n        if mask_23[j]:\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\n                         color=\\\"#cccccc\\\", alpha=0.5, linewidth=0, zorder=0)\\n        if mask_2[j]:\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\n                         color=\\\"#b8d4e3\\\", alpha=0.5, linewidth=0, zorder=0)\\n\\n    for i, (name, ks) in enumerate(all_kstar.items()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        ax_b.step(thetas, ks, where=\\\"post\\\", label=name,\\n                  linewidth=1.6, color=color)\\n\\n    ax_b.axvline(x=0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, alpha=0.7)\\n    ax_b.text(0.605, 5.15, r\\\"$\\\\theta=0.60$\\\", color=\\\"grey\\\", fontsize=8,\\n              va=\\\"top\\\")\\n\\n    import matplotlib.patches as mpatches\\n    legend_patches = [\\n        mpatches.Patch(color=\\\"#cccccc\\\", alpha=0.5, label=r\\\"$K^*\\\\!\\\\in\\\\!\\\\{2,3\\\\}$ (all models)\\\"),\\n        mpatches.Patch(color=\\\"#b8d4e3\\\", alpha=0.5, label=r\\\"$K^*\\\\!=\\\\!2$ (all models)\\\"),\\n    ]\\n    handles_lines = []\\n    for i, name in enumerate(all_kstar.keys()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        h = plt.Line2D([0], [0], color=color, lw=1.6, label=name)\\n        handles_lines.append(h)\\n\\n    ax_b.legend(handles=legend_patches + handles_lines, fontsize=7.5,\\n                loc=\\\"upper right\\\", framealpha=0.92, edgecolor=\\\"0.85\\\")\\n\\n    ax_b.set_xlabel(r\\\"Threshold $\\\\theta$\\\")\\n    ax_b.set_ylabel(r\\\"$K^*(\\\\theta)$\\\")\\n    ax_b.set_xlim(0.495, 0.755)\\n    max_k = max(len(v) for v in MODELS.values())\\n    ax_b.set_ylim(-0.2, max_k + 0.5)\\n    ax_b.set_yticks(range(max_k + 1))\\n    ax_b.grid(axis=\\\"y\\\", color=\\\"#e0e0e0\\\", linewidth=0.5)\\n    ax_b.set_title(r\\\"$\\\\bf{(b)}$\\\" + r\\\" $K^*(\\\\theta)$ sensitivity\\\", fontsize=10,\\n                   loc=\\\"left\\\", pad=6)\\n\\n    fig.tight_layout()\\n\\n    out_dir = Path(__file__).resolve().parent.parent / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\n    out_dir.mkdir(parents=True, exist_ok=True)\\n    out_path = out_dir / \\\"fig_kstar_theta.pdf\\\"\\n\\n    fig.savefig(out_path, bbox_inches=\\\"tight\\\")\\n    fig.savefig(out_path.with_suffix(\\\".png\\\"), bbox_inches=\\\"tight\\\", dpi=300)\\n    plt.close(fig)\\n\\n    print(f\\\"Models: {list(MODELS.keys())}\\\")\\n    print(f\\\"Saved: {out_path}\\\")\\n    pdf_size = out_path.stat().st_size\\n    assert pdf_size > 3 * 1024, f\\\"PDF too small: {pdf_size}\\\"\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d36139d-2eac-4777-89a6-886ffe3102b5",
  "uuid": "350000c3-9d75-495c-9de6-dd13494ecd35",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"#!/usr/bin/env python3\\\\n\\\\\\\"\\\\\\\"\\\\\\\"Figure 3: two-panel K*(theta) figure.\\\\n\\\\nPanel (a): Pairwise AUC profile across depth pairs (C4 configs)\\\\nPanel (b): K*(theta) sensitivity\\\\n\\\\nOutput: docs/paper/figures/fig_kstar_theta.pdf\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport matplotlib\\\\nmatplotlib.use(\\\\\\\"Agg\\\\\\\")\\\\nimport matplotlib.pyplot as plt\\\\nimport numpy as np\\\\nfrom pathlib import Path\\\\n\\\\nPAIR_KEYS = [\\\\\\\"0v1\\\\\\\", \\\\\\\"1v2\\\\\\\", \\\\\\\"2v3\\\\\\\", \\\\\\\"3v4\\\\\\\", \\\\\\\"4v5\\\\\\\"]\\\\n\\\\nMODELS = {\\\\n    \\\\\\\"Qwen-rw\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9946, 0.6859, 0.5795, 0.5333, 0.5238],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9976, 0.7041, 0.5991, 0.5551, 0.5448],\\\\n    },\\\\n    \\\\\\\"Pythia\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9921, 0.6454, 0.5417, 0.5041, 0.5021],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9943, 0.6630, 0.5628, 0.5260, 0.5249],\\\\n    },\\\\n    \\\\\\\"OLMo\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\\\n    },\\\\n    \\\\\\\"Qwen-cont\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9963, 0.6015, 0.5511, 0.5308, 0.5035],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9978, 0.6213, 0.5712, 0.5508, 0.5255],\\\\n    },\\\\n    \\\\\\\"Qwen-7B\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\\\n        \\\\\\\"ci_lower\\\\\\\": [0.9610, 0.6080, 0.5390, 0.5180, 0.4990],\\\\n        \\\\\\\"ci_upper\\\\\\\": [0.9670, 0.6260, 0.5590, 0.5370, 0.5180],\\\\n    },\\\\n}\\\\n\\\\nTABLEAU = [\\\\n    \\\\\\\"#4e79a7\\\\\\\", \\\\\\\"#e15759\\\\\\\", \\\\\\\"#76b7b2\\\\\\\", \\\\\\\"#59a14f\\\\\\\", \\\\\\\"#b07aa1\\\\\\\",\\\\n    \\\\\\\"#ff9da7\\\\\\\", \\\\\\\"#9c755f\\\\\\\", \\\\\\\"#bab0ac\\\\\\\", \\\\\\\"#edc948\\\\\\\", \\\\\\\"#f28e2b\\\\\\\",\\\\n]\\\\nMARKERS = [\\\\\\\"o\\\\\\\", \\\\\\\"s\\\\\\\", \\\\\\\"^\\\\\\\", \\\\\\\"D\\\\\\\", \\\\\\\"v\\\\\\\", \\\\\\\"P\\\\\\\", \\\\\\\"X\\\\\\\", \\\\\\\"*\\\\\\\", \\\\\\\"h\\\\\\\", \\\\\\\"<\\\\\\\"]\\\\n\\\\n\\\\ndef compute_kstar(ci_lowers, theta):\\\\n    k = 0\\\\n    for v in ci_lowers:\\\\n        if v >= theta:\\\\n            k += 1\\\\n        else:\\\\n            break\\\\n    return k\\\\n\\\\n\\\\ndef main():\\\\n    x = np.arange(len(PAIR_KEYS))\\\\n    thetas = np.arange(0.50, 0.751, 0.005)\\\\n\\\\n    plt.rcParams.update({\\\\n        \\\\\\\"font.family\\\\\\\": \\\\\\\"serif\\\\\\\",\\\\n        \\\\\\\"font.size\\\\\\\": 10,\\\\n        \\\\\\\"axes.linewidth\\\\\\\": 0.8,\\\\n        \\\\\\\"xtick.direction\\\\\\\": \\\\\\\"in\\\\\\\",\\\\n        \\\\\\\"ytick.direction\\\\\\\": \\\\\\\"in\\\\\\\",\\\\n        \\\\\\\"xtick.major.width\\\\\\\": 0.8,\\\\n        \\\\\\\"ytick.major.width\\\\\\\": 0.8,\\\\n    })\\\\n\\\\n    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10, 3.5),\\\\n                                      gridspec_kw={\\\\\\\"width_ratios\\\\\\\": [1, 1.15]})\\\\n\\\\n    # ── Panel (a): Pairwise AUC profile ─────────────────────────────────\\\\n    ax_a.axhline(0.60, color=\\\\\\\"grey\\\\\\\", ls=\\\\\\\"--\\\\\\\", lw=0.8, zorder=1)\\\\n    ax_a.text(4.05, 0.607, r\\\\\\\"$\\\\\\\\theta = 0.60$\\\\\\\", fontsize=8, color=\\\\\\\"grey\\\\\\\",\\\\n              va=\\\\\\\"bottom\\\\\\\", ha=\\\\\\\"right\\\\\\\")\\\\n\\\\n    ax_a.axvspan(1.5, 2.5, color=\\\\\\\"#4e79a7\\\\\\\", alpha=0.06, zorder=0)\\\\n    ax_a.annotate(r\\\\\\\"$K^*\\\\\\\\!=\\\\\\\\!2$\\\\\\\", xy=(1.7, 0.68), fontsize=8, color=\\\\\\\"#4e79a7\\\\\\\",\\\\n                  alpha=0.7)\\\\n\\\\n    for i, (name, data) in enumerate(MODELS.items()):\\\\n        color = TABLEAU[i % len(TABLEAU)]\\\\n        marker = MARKERS[i % len(MARKERS)]\\\\n        means = data[\\\\\\\"mean\\\\\\\"]\\\\n        lo = data[\\\\\\\"ci_lower\\\\\\\"]\\\\n        hi = data[\\\\\\\"ci_upper\\\\\\\"]\\\\n\\\\n        ax_a.fill_between(x, lo, hi, color=color, alpha=0.15, linewidth=0)\\\\n        ax_a.plot(x, means, \\\\\\\"-\\\\\\\", color=color, lw=1.6, marker=marker,\\\\n                  markersize=4.5, label=name, zorder=3)\\\\n\\\\n    ax_a.set_xticks(x)\\\\n    ax_a.set_xticklabels(PAIR_KEYS)\\\\n    ax_a.set_xlabel(\\\\\\\"Depth pair\\\\\\\")\\\\n    ax_a.set_ylabel(\\\\\\\"Pairwise AUC\\\\\\\")\\\\n    ax_a.set_ylim(0.47, 1.02)\\\\n    ax_a.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\\\n    ax_a.legend(fontsize=7.5, loc=\\\\\\\"upper right\\\\\\\", framealpha=0.92,\\\\n                edgecolor=\\\\\\\"0.85\\\\\\\", handlelength=2.0)\\\\n    ax_a.set_title(r\\\\\\\"$\\\\\\\\bf{(a)}$\\\\\\\" + \\\\\\\" Pairwise AUC profile\\\\\\\", fontsize=10,\\\\n                   loc=\\\\\\\"left\\\\\\\", pad=6)\\\\n\\\\n    # ── Panel (b): K*(θ) sensitivity ────────────────────────────────────\\\\n    all_kstar = {}\\\\n    for name, data in MODELS.items():\\\\n        ci_lo = data[\\\\\\\"ci_lower\\\\\\\"]\\\\n        ks = [compute_kstar(ci_lo, t) for t in thetas]\\\\n        all_kstar[name] = ks\\\\n\\\\n    kstar_arr = np.array(list(all_kstar.values()))\\\\n    k_min = kstar_arr.min(axis=0)\\\\n    k_max = kstar_arr.max(axis=0)\\\\n\\\\n    mask_23 = (k_min >= 2) & (k_max <= 3) & (k_min != k_max)\\\\n    mask_2  = (k_min == 2) & (k_max == 2)\\\\n\\\\n    for j in range(len(thetas)):\\\\n        if mask_23[j]:\\\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\\\n                         color=\\\\\\\"#cccccc\\\\\\\", alpha=0.5, linewidth=0, zorder=0)\\\\n        if mask_2[j]:\\\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\\\n                         color=\\\\\\\"#b8d4e3\\\\\\\", alpha=0.5, linewidth=0, zorder=0)\\\\n\\\\n    for i, (name, ks) in enumerate(all_kstar.items()):\\\\n        color = TABLEAU[i % len(TABLEAU)]\\\\n        ax_b.step(thetas, ks, where=\\\\\\\"post\\\\\\\", label=name,\\\\n                  linewidth=1.6, color=color)\\\\n\\\\n    ax_b.axvline(x=0.60, color=\\\\\\\"grey\\\\\\\", ls=\\\\\\\"--\\\\\\\", lw=0.8, alpha=0.7)\\\\n    ax_b.text(0.605, 5.15, r\\\\\\\"$\\\\\\\\theta=0.60$\\\\\\\", color=\\\\\\\"grey\\\\\\\", fontsize=8,\\\\n              va=\\\\\\\"top\\\\\\\")\\\\n\\\\n    import matplotlib.patches as mpatches\\\\n    legend_patches = [\\\\n        mpatches.Patch(color=\\\\\\\"#cccccc\\\\\\\", alpha=0.5, label=r\\\\\\\"$K^*\\\\\\\\!\\\\\\\\in\\\\\\\\!\\\\\\\\{2,3\\\\\\\\}$ (all models)\\\\\\\"),\\\\n        mpatches.Patch(color=\\\\\\\"#b8d4e3\\\\\\\", alpha=0.5, label=r\\\\\\\"$K^*\\\\\\\\!=\\\\\\\\!2$ (all models)\\\\\\\"),\\\\n    ]\\\\n    handles_lines = []\\\\n    for i, name in enumerate(all_kstar.keys()):\\\\n        color = TABLEAU[i % len(TABLEAU)]\\\\n        h = plt.Line2D([0], [0], color=color, lw=1.6, label=name)\\\\n        handles_lines.append(h)\\\\n\\\\n    ax_b.legend(handles=legend_patches + handles_lines, fontsize=7.5,\\\\n                loc=\\\\\\\"upper right\\\\\\\", framealpha=0.92, edgecolor=\\\\\\\"0.85\\\\\\\")\\\\n\\\\n    ax_b.set_xlabel(r\\\\\\\"Threshold $\\\\\\\\theta$\\\\\\\")\\\\n    ax_b.set_ylabel(r\\\\\\\"$K^*(\\\\\\\\theta)$\\\\\\\")\\\\n    ax_b.set_xlim(0.495, 0.755)\\\\n    max_k = max(len(v) for v in MODELS.values())\\\\n    ax_b.set_ylim(-0.2, max_k + 0.5)\\\\n    ax_b.set_yticks(range(max_k + 1))\\\\n    ax_b.grid(axis=\\\\\\\"y\\\\\\\", color=\\\\\\\"#e0e0e0\\\\\\\", linewidth=0.5)\\\\n    ax_b.set_title(r\\\\\\\"$\\\\\\\\bf{(b)}$\\\\\\\" + r\\\\\\\" $K^*(\\\\\\\\theta)$ sensitivity\\\\\\\", fontsize=10,\\\\n                   loc=\\\\\\\"left\\\\\\\", pad=6)\\\\n\\\\n    fig.tight_layout()\\\\n\\\\n    out_dir = Path(__file__).resolve().parent.parent / \\\\\\\"docs\\\\\\\" / \\\\\\\"paper\\\\\\\" / \\\\\\\"figures\\\\\\\"\\\\n    out_dir.mkdir(parents=True, exist_ok=True)\\\\n    out_path = out_dir / \\\\\\\"fig_kstar_theta.pdf\\\\\\\"\\\\n\\\\n    fig.savefig(out_path, bbox_inches=\\\\\\\"tight\\\\\\\")\\\\n    fig.savefig(out_path.with_suffix(\\\\\\\".png\\\\\\\"), bbox_inches=\\\\\\\"tight\\\\\\\", dpi=300)\\\\n    plt.close(fig)\\\\n\\\\n    print(f\\\\\\\"Models: {list(MODELS.keys())}\\\\\\\")\\\\n    print(f\\\\\\\"Saved: {out_path}\\\\\\\")\\\\n    pdf_size = out_path.stat().st_size\\\\n    assert pdf_size > 3 * 1024, f\\\\\\\"PDF too small: {pdf_size}\\\\\\\"\\\\n    print(\\\\\\\"OK\\\\\\\")\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Figure 3: two-panel K*(theta) figure.\\n\\nPanel (a): Pairwise AUC profile across depth pairs (C4 configs)\\nPanel (b): K*(theta) sensitivity\\n\\nOutput: docs/paper/figures/fig_kstar_theta.pdf\\n\\\"\\\"\\\"\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nfrom pathlib import Path\\n\\nPAIR_KEYS = [\\\"0v1\\\", \\\"1v2\\\", \\\"2v3\\\", \\\"3v4\\\", \\\"4v5\\\"]\\n\\nMODELS = {\\n    \\\"Qwen-rw\\\": {\\n        \\\"mean\\\":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],\\n        \\\"ci_lower\\\": [0.9946, 0.6859, 0.5795, 0.5333, 0.5238],\\n        \\\"ci_upper\\\": [0.9976, 0.7041, 0.5991, 0.5551, 0.5448],\\n    },\\n    \\\"Pythia\\\": {\\n        \\\"mean\\\":     [0.9932, 0.6539, 0.5514, 0.5152, 0.5136],\\n        \\\"ci_lower\\\": [0.9921, 0.6454, 0.5417, 0.5041, 0.5021],\\n        \\\"ci_upper\\\": [0.9943, 0.6630, 0.5628, 0.5260, 0.5249],\\n    },\\n    \\\"OLMo\\\": {\\n        \\\"mean\\\":     [0.9860, 0.5079, 0.4973, 0.5024, 0.4942],\\n        \\\"ci_lower\\\": [0.9845, 0.4908, 0.4829, 0.4924, 0.4860],\\n        \\\"ci_upper\\\": [0.9875, 0.5251, 0.5117, 0.5123, 0.5024],\\n    },\\n    \\\"Qwen-cont\\\": {\\n        \\\"mean\\\":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],\\n        \\\"ci_lower\\\": [0.9963, 0.6015, 0.5511, 0.5308, 0.5035],\\n        \\\"ci_upper\\\": [0.9978, 0.6213, 0.5712, 0.5508, 0.5255],\\n    },\\n    \\\"Qwen-7B\\\": {\\n        \\\"mean\\\":     [0.9638, 0.6168, 0.5492, 0.5276, 0.5085],\\n        \\\"ci_lower\\\": [0.9610, 0.6080, 0.5390, 0.5180, 0.4990],\\n        \\\"ci_upper\\\": [0.9670, 0.6260, 0.5590, 0.5370, 0.5180],\\n    },\\n}\\n\\nTABLEAU = [\\n    \\\"#4e79a7\\\", \\\"#e15759\\\", \\\"#76b7b2\\\", \\\"#59a14f\\\", \\\"#b07aa1\\\",\\n    \\\"#ff9da7\\\", \\\"#9c755f\\\", \\\"#bab0ac\\\", \\\"#edc948\\\", \\\"#f28e2b\\\",\\n]\\nMARKERS = [\\\"o\\\", \\\"s\\\", \\\"^\\\", \\\"D\\\", \\\"v\\\", \\\"P\\\", \\\"X\\\", \\\"*\\\", \\\"h\\\", \\\"<\\\"]\\n\\n\\ndef compute_kstar(ci_lowers, theta):\\n    k = 0\\n    for v in ci_lowers:\\n        if v >= theta:\\n            k += 1\\n        else:\\n            break\\n    return k\\n\\n\\ndef main():\\n    x = np.arange(len(PAIR_KEYS))\\n    thetas = np.arange(0.50, 0.751, 0.005)\\n\\n    plt.rcParams.update({\\n        \\\"font.family\\\": \\\"serif\\\",\\n        \\\"font.size\\\": 10,\\n        \\\"axes.linewidth\\\": 0.8,\\n        \\\"xtick.direction\\\": \\\"in\\\",\\n        \\\"ytick.direction\\\": \\\"in\\\",\\n        \\\"xtick.major.width\\\": 0.8,\\n        \\\"ytick.major.width\\\": 0.8,\\n    })\\n\\n    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10, 3.5),\\n                                      gridspec_kw={\\\"width_ratios\\\": [1, 1.15]})\\n\\n    # ── Panel (a): Pairwise AUC profile ─────────────────────────────────\\n    ax_a.axhline(0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, zorder=1)\\n    ax_a.text(4.05, 0.607, r\\\"$\\\\theta = 0.60$\\\", fontsize=8, color=\\\"grey\\\",\\n              va=\\\"bottom\\\", ha=\\\"right\\\")\\n\\n    ax_a.axvspan(1.5, 2.5, color=\\\"#4e79a7\\\", alpha=0.06, zorder=0)\\n    ax_a.annotate(r\\\"$K^*\\\\!=\\\\!2$\\\", xy=(1.7, 0.68), fontsize=8, color=\\\"#4e79a7\\\",\\n                  alpha=0.7)\\n\\n    for i, (name, data) in enumerate(MODELS.items()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        marker = MARKERS[i % len(MARKERS)]\\n        means = data[\\\"mean\\\"]\\n        lo = data[\\\"ci_lower\\\"]\\n        hi = data[\\\"ci_upper\\\"]\\n\\n        ax_a.fill_between(x, lo, hi, color=color, alpha=0.15, linewidth=0)\\n        ax_a.plot(x, means, \\\"-\\\", color=color, lw=1.6, marker=marker,\\n                  markersize=4.5, label=name, zorder=3)\\n\\n    ax_a.set_xticks(x)\\n    ax_a.set_xticklabels(PAIR_KEYS)\\n    ax_a.set_xlabel(\\\"Depth pair\\\")\\n    ax_a.set_ylabel(\\\"Pairwise AUC\\\")\\n    ax_a.set_ylim(0.47, 1.02)\\n    ax_a.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)\\n    ax_a.legend(fontsize=7.5, loc=\\\"upper right\\\", framealpha=0.92,\\n                edgecolor=\\\"0.85\\\", handlelength=2.0)\\n    ax_a.set_title(r\\\"$\\\\bf{(a)}$\\\" + \\\" Pairwise AUC profile\\\", fontsize=10,\\n                   loc=\\\"left\\\", pad=6)\\n\\n    # ── Panel (b): K*(θ) sensitivity ────────────────────────────────────\\n    all_kstar = {}\\n    for name, data in MODELS.items():\\n        ci_lo = data[\\\"ci_lower\\\"]\\n        ks = [compute_kstar(ci_lo, t) for t in thetas]\\n        all_kstar[name] = ks\\n\\n    kstar_arr = np.array(list(all_kstar.values()))\\n    k_min = kstar_arr.min(axis=0)\\n    k_max = kstar_arr.max(axis=0)\\n\\n    mask_23 = (k_min >= 2) & (k_max <= 3) & (k_min != k_max)\\n    mask_2  = (k_min == 2) & (k_max == 2)\\n\\n    for j in range(len(thetas)):\\n        if mask_23[j]:\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\n                         color=\\\"#cccccc\\\", alpha=0.5, linewidth=0, zorder=0)\\n        if mask_2[j]:\\n            ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,\\n                         color=\\\"#b8d4e3\\\", alpha=0.5, linewidth=0, zorder=0)\\n\\n    for i, (name, ks) in enumerate(all_kstar.items()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        ax_b.step(thetas, ks, where=\\\"post\\\", label=name,\\n                  linewidth=1.6, color=color)\\n\\n    ax_b.axvline(x=0.60, color=\\\"grey\\\", ls=\\\"--\\\", lw=0.8, alpha=0.7)\\n    ax_b.text(0.605, 5.15, r\\\"$\\\\theta=0.60$\\\", color=\\\"grey\\\", fontsize=8,\\n              va=\\\"top\\\")\\n\\n    import matplotlib.patches as mpatches\\n    legend_patches = [\\n        mpatches.Patch(color=\\\"#cccccc\\\", alpha=0.5, label=r\\\"$K^*\\\\!\\\\in\\\\!\\\\{2,3\\\\}$ (all models)\\\"),\\n        mpatches.Patch(color=\\\"#b8d4e3\\\", alpha=0.5, label=r\\\"$K^*\\\\!=\\\\!2$ (all models)\\\"),\\n    ]\\n    handles_lines = []\\n    for i, name in enumerate(all_kstar.keys()):\\n        color = TABLEAU[i % len(TABLEAU)]\\n        h = plt.Line2D([0], [0], color=color, lw=1.6, label=name)\\n        handles_lines.append(h)\\n\\n    ax_b.legend(handles=legend_patches + handles_lines, fontsize=7.5,\\n                loc=\\\"upper right\\\", framealpha=0.92, edgecolor=\\\"0.85\\\")\\n\\n    ax_b.set_xlabel(r\\\"Threshold $\\\\theta$\\\")\\n    ax_b.set_ylabel(r\\\"$K^*(\\\\theta)$\\\")\\n    ax_b.set_xlim(0.495, 0.755)\\n    max_k = max(len(v) for v in MODELS.values())\\n    ax_b.set_ylim(-0.2, max_k + 0.5)\\n    ax_b.set_yticks(range(max_k + 1))\\n    ax_b.grid(axis=\\\"y\\\", color=\\\"#e0e0e0\\\", linewidth=0.5)\\n    ax_b.set_title(r\\\"$\\\\bf{(b)}$\\\" + r\\\" $K^*(\\\\theta)$ sensitivity\\\", fontsize=10,\\n                   loc=\\\"left\\\", pad=6)\\n\\n    fig.tight_layout()\\n\\n    out_dir = Path(__file__).resolve().parent.parent / \\\"docs\\\" / \\\"paper\\\" / \\\"figures\\\"\\n    out_dir.mkdir(parents=True, exist_ok=True)\\n    out_path = out_dir / \\\"fig_kstar_theta.pdf\\\"\\n\\n    fig.savefig(out_path, bbox_inches=\\\"tight\\\")\\n    fig.savefig(out_path.with_suffix(\\\".png\\\"), bbox_inches=\\\"tight\\\", dpi=300)\\n    plt.close(fig)\\n\\n    print(f\\\"Models: {list(MODELS.keys())}\\\")\\n    print(f\\\"Saved: {out_path}\\\")\\n    pdf_size = out_path.stat().st_size\\n    assert pdf_size > 3 * 1024, f\\\"PDF too small: {pdf_size}\\\"\\n    print(\\\"OK\\\")\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---
