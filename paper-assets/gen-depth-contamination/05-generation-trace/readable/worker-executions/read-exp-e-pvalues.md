# read exp E pvalues

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_read_exp_E_pvalues_20260515T142948.log`
- **Structured JSON:** [`89f6d338492abf09564a.json`](../../sessions/89/89f6d338492abf09564a.json)

## Before a recorded user message

16 recorded events

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
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
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
  "uuid": "f57b36c2-3cf2-40d3-837b-ed446bcd0d71",
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
    "resetsAt": 1778872800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3235dddc-f0f8-4a18-ac7f-568dec39a97a",
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the JSON file from the remote server using ssh_read_only.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "0dbbfe8f-f50a-406b-847c-90398f7887fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rqpexkZwKRpbBCuAGokHw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11148,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11148
      },
      "output_tokens": 49,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DVvLM98Gm7YPdqUJJPoS6A`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "b930b469-9215-442b-bdc5-68712ba141fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rqpexkZwKRpbBCuAGokHw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11148,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11148
      },
      "output_tokens": 49,
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

_source line 6 · 2026-05-15T14:29:59.974Z_

<details><summary>↩ Tool result · `toolu_01DVvLM98Gm7YPdqUJJPoS6A`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
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
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "2893367b-f306-4b26-a43a-8f7c1e4a43e9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01F1MVmVe49ezSbJGypu9mfp`</summary>

```json
{
  "server": "westc-26893",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/artifacts/exp_E_paired_stats.json",
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
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "38b0c06e-984e-4dfe-b585-0c2028db0da7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XytnNzKofsWzPsW3qTy8Ac",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 22989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
      },
      "output_tokens": 73,
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

_source line 8 · 2026-05-15T14:30:07.072Z_

<details><summary>↩ Tool result · `toolu_01F1MVmVe49ezSbJGypu9mfp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mmlu\\\": {\\n    \\\"pairwise_comparisons\\\": [\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-ours\\\",\\n          \\\"dsir\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.007235436547500362,\\n        \\\"t_stat\\\": 24.598249063205415,\\n        \\\"raw_p\\\": 1.6209310233228965e-05,\\n        \\\"cohens_d\\\": 10.836755388457677,\\n        \\\"corrected_p\\\": 0.00024313965349843447,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-ours\\\",\\n          \\\"binary-drayson\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0028058681099558448,\\n        \\\"t_stat\\\": 17.515436444289804,\\n        \\\"raw_p\\\": 6.238619313918888e-05,\\n        \\\"cohens_d\\\": 2.852751540168622,\\n        \\\"corrected_p\\\": 0.0008734067039486444,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-ours\\\",\\n          \\\"no-filter\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.007662726107392115,\\n        \\\"t_stat\\\": 13.593055060087883,\\n        \\\"raw_p\\\": 0.00016957959325503732,\\n        \\\"cohens_d\\\": 7.383036494013822,\\n        \\\"corrected_p\\\": 0.0022045347123154854,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-drayson\\\",\\n          \\\"dsir\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.004429568437544518,\\n        \\\"t_stat\\\": 12.607532539957875,\\n        \\\"raw_p\\\": 0.00022784095885562328,\\n        \\\"cohens_d\\\": 5.717501056881729,\\n        \\\"corrected_p\\\": 0.0027340915062674795,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-ours\\\",\\n          \\\"graduated_a0.9\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0049565588947443565,\\n        \\\"t_stat\\\": 8.556802169125492,\\n        \\\"raw_p\\\": 0.0010241458708119772,\\n        \\\"cohens_d\\\": 5.5653292827627565,\\n        \\\"corrected_p\\\": 0.011265604578931748,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-drayson\\\",\\n          \\\"no-filter\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.00485685799743627,\\n        \\\"t_stat\\\": 7.239768218559279,\\n        \\\"raw_p\\\": 0.0019316941682584218,\\n        \\\"cohens_d\\\": 4.376382983859104,\\n        \\\"corrected_p\\\": 0.01931694168258422,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-ours\\\",\\n          \\\"surprisal\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.004728671129468754,\\n        \\\"t_stat\\\": 6.920422255077682,\\n        \\\"raw_p\\\": 0.002288028327494149,\\n        \\\"cohens_d\\\": 4.801394133053051,\\n        \\\"corrected_p\\\": 0.02059225494744734,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"surprisal\\\",\\n          \\\"no-filter\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0029340549779233614,\\n        \\\"t_stat\\\": 6.384719991949423,\\n        \\\"raw_p\\\": 0.0030881523071242785,\\n        \\\"cohens_d\\\": 2.6410799044016096,\\n        \\\"corrected_p\\\": 0.024705218456994228,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"graduated_a0.9\\\",\\n          \\\"dsir\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0022788776527560063,\\n        \\\"t_stat\\\": 5.003666137605971,\\n        \\\"raw_p\\\": 0.007471036682110306,\\n        \\\"cohens_d\\\": 3.4914862437758036,\\n        \\\"corrected_p\\\": 0.05229725677477214,\\n        \\\"significant\\\": false\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"graduated_a0.9\\\",\\n          \\\"no-filter\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0027061672126477586,\\n        \\\"t_stat\\\": 4.861418300116258,\\n        \\\"raw_p\\\": 0.008270807199636267,\\n        \\\"cohens_d\\\": 2.6316647720448314,\\n        \\\"corrected_p\\\": 0.05229725677477214,\\n        \\\"significant\\\": false\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"surprisal\\\",\\n          \\\"dsir\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.002506765418031609,\\n        \\\"t_stat\\\": 4.677147230384029,\\n        \\\"raw_p\\\": 0.00946778993302357,\\n        \\\"cohens_d\\\": 3.228814318222188,\\n        \\\"corrected_p\\\": 0.05229725677477214,\\n        \\\"significant\\\": false\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-drayson\\\",\\n          \\\"graduated_a0.9\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0021506907847885113,\\n        \\\"t_stat\\\": 2.9940639785296623,\\n        \\\"raw_p\\\": 0.04017657284695923,\\n        \\\"cohens_d\\\": 2.2093289931439317,\\n        \\\"corrected_p\\\": 0.16070629138783693,\\n        \\\"significant\\\": false\\n      },\\n      {\\n        \\\"pair\\\": [\\n         \\n\\n... [截断: 输出过长，省略 31807 字符] ...\\n\\n: false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"graduated_a0.9\\\",\\n            \\\"graduated_a0.7\\\"\\n          ],\\n          \\\"mean_diff\\\": 0.0005775741884086916,\\n          \\\"t_stat\\\": 2.6640282306129635,\\n          \\\"raw_p\\\": 0.05615411746185,\\n          \\\"cohens_d\\\": 0.9496718778626968,\\n          \\\"corrected_p\\\": 0.7123999492078322,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"binary-ours\\\",\\n            \\\"graduated_a0.5\\\"\\n          ],\\n          \\\"mean_diff\\\": 0.0014538936466839346,\\n          \\\"t_stat\\\": 2.645379028333393,\\n          \\\"raw_p\\\": 0.05725750005173216,\\n          \\\"cohens_d\\\": 1.857951507889329,\\n          \\\"corrected_p\\\": 0.7123999492078322,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"graduated_a0.9\\\",\\n            \\\"graduated_a0.5\\\"\\n          ],\\n          \\\"mean_diff\\\": 0.0014538936466839346,\\n          \\\"t_stat\\\": 2.4449061127512546,\\n          \\\"raw_p\\\": 0.07083284836349661,\\n          \\\"cohens_d\\\": 1.7608262523341858,\\n          \\\"corrected_p\\\": 0.7123999492078322,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"graduated_a0.5\\\",\\n            \\\"graduated_a0.7\\\"\\n          ],\\n          \\\"mean_diff\\\": -0.0008763194582752431,\\n          \\\"t_stat\\\": -2.176991062379295,\\n          \\\"raw_p\\\": 0.0950637475781524,\\n          \\\"cohens_d\\\": -1.260362178309412,\\n          \\\"corrected_p\\\": 0.8555737282033716,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"dsir\\\",\\n            \\\"graduated_a0.1\\\"\\n          ],\\n          \\\"mean_diff\\\": -0.0009759012148974566,\\n          \\\"t_stat\\\": -1.9278792146434196,\\n          \\\"raw_p\\\": 0.12612268686357775,\\n          \\\"cohens_d\\\": -1.0789444898238614,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"binary-drayson\\\",\\n            \\\"graduated_a0.7\\\"\\n          ],\\n          \\\"mean_diff\\\": -0.0004779924317864781,\\n          \\\"t_stat\\\": -1.4191497503736252,\\n          \\\"raw_p\\\": 0.22886008250149933,\\n          \\\"cohens_d\\\": -1.0474458731326661,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"binary-drayson\\\",\\n            \\\"graduated_a0.5\\\"\\n          ],\\n          \\\"mean_diff\\\": 0.00039832702648876504,\\n          \\\"t_stat\\\": 0.7519115803969555,\\n          \\\"raw_p\\\": 0.49392844139373543,\\n          \\\"cohens_d\\\": 0.552315517513844,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"no-filter\\\",\\n            \\\"graduated_a0.1\\\"\\n          ],\\n          \\\"mean_diff\\\": -0.0002788289185421622,\\n          \\\"t_stat\\\": -0.6803013430499374,\\n          \\\"raw_p\\\": 0.533651991130784,\\n          \\\"cohens_d\\\": -0.29034647452456464,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"surprisal\\\",\\n            \\\"graduated_a0.1\\\"\\n          ],\\n          \\\"mean_diff\\\": 3.9832702648867625e-05,\\n          \\\"t_stat\\\": 0.09600307214745031,\\n          \\\"raw_p\\\": 0.9281356155015111,\\n          \\\"cohens_d\\\": 0.04611123341633106,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"binary-ours\\\",\\n            \\\"graduated_a0.9\\\"\\n          ],\\n          \\\"mean_diff\\\": 0.0,\\n          \\\"t_stat\\\": 0.0,\\n          \\\"raw_p\\\": 1.0,\\n          \\\"cohens_d\\\": 0.0,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        }\\n      ],\\n      \\\"correction_method\\\": \\\"Holm-Bonferroni\\\",\\n      \\\"n_comparisons\\\": 45\\n    }\\n  },\\n  \\\"key_findings\\\": \\\"MMLU: 8/15 pairs significant after Holm-Bonferroni correction. HellaSwag: 9/15 pairs significant after Holm-Bonferroni correction. Largest MMLU effect sizes: binary-ours vs dsir (d=10.84, p_corr=0.0002); binary-ours vs no-filter (d=7.38, p_corr=0.0022); binary-drayson vs dsir (d=5.72, p_corr=0.0027) Largest HellaSwag effect sizes: binary-ours vs dsir (d=10.19, p_corr=0.0006); binary-drayson vs dsir (d=9.64, p_corr=0.0029); graduated_a0.9 vs dsir (d=9.53, p_corr=0.0005)\\\"\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.07}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "1e9dc761-7e9a-4e03-946d-1b2509f4d02d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mmlu\\\\\\\": {\\\\n    \\\\\\\"pairwise_comparisons\\\\\\\": [\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"binary-ours\\\\\\\",\\\\n          \\\\\\\"dsir\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.007235436547500362,\\\\n        \\\\\\\"t_stat\\\\\\\": 24.598249063205415,\\\\n        \\\\\\\"raw_p\\\\\\\": 1.6209310233228965e-05,\\\\n        \\\\\\\"cohens_d\\\\\\\": 10.836755388457677,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.00024313965349843447,\\\\n        \\\\\\\"significant\\\\\\\": true\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"binary-ours\\\\\\\",\\\\n          \\\\\\\"binary-drayson\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.0028058681099558448,\\\\n        \\\\\\\"t_stat\\\\\\\": 17.515436444289804,\\\\n        \\\\\\\"raw_p\\\\\\\": 6.238619313918888e-05,\\\\n        \\\\\\\"cohens_d\\\\\\\": 2.852751540168622,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.0008734067039486444,\\\\n        \\\\\\\"significant\\\\\\\": true\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"binary-ours\\\\\\\",\\\\n          \\\\\\\"no-filter\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.007662726107392115,\\\\n        \\\\\\\"t_stat\\\\\\\": 13.593055060087883,\\\\n        \\\\\\\"raw_p\\\\\\\": 0.00016957959325503732,\\\\n        \\\\\\\"cohens_d\\\\\\\": 7.383036494013822,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.0022045347123154854,\\\\n        \\\\\\\"significant\\\\\\\": true\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"binary-drayson\\\\\\\",\\\\n          \\\\\\\"dsir\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.004429568437544518,\\\\n        \\\\\\\"t_stat\\\\\\\": 12.607532539957875,\\\\n        \\\\\\\"raw_p\\\\\\\": 0.00022784095885562328,\\\\n        \\\\\\\"cohens_d\\\\\\\": 5.717501056881729,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.0027340915062674795,\\\\n        \\\\\\\"significant\\\\\\\": true\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"binary-ours\\\\\\\",\\\\n          \\\\\\\"graduated_a0.9\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.0049565588947443565,\\\\n        \\\\\\\"t_stat\\\\\\\": 8.556802169125492,\\\\n        \\\\\\\"raw_p\\\\\\\": 0.0010241458708119772,\\\\n        \\\\\\\"cohens_d\\\\\\\": 5.5653292827627565,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.011265604578931748,\\\\n        \\\\\\\"significant\\\\\\\": true\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"binary-drayson\\\\\\\",\\\\n          \\\\\\\"no-filter\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.00485685799743627,\\\\n        \\\\\\\"t_stat\\\\\\\": 7.239768218559279,\\\\n        \\\\\\\"raw_p\\\\\\\": 0.0019316941682584218,\\\\n        \\\\\\\"cohens_d\\\\\\\": 4.376382983859104,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.01931694168258422,\\\\n        \\\\\\\"significant\\\\\\\": true\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"binary-ours\\\\\\\",\\\\n          \\\\\\\"surprisal\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.004728671129468754,\\\\n        \\\\\\\"t_stat\\\\\\\": 6.920422255077682,\\\\n        \\\\\\\"raw_p\\\\\\\": 0.002288028327494149,\\\\n        \\\\\\\"cohens_d\\\\\\\": 4.801394133053051,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.02059225494744734,\\\\n        \\\\\\\"significant\\\\\\\": true\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"surprisal\\\\\\\",\\\\n          \\\\\\\"no-filter\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.0029340549779233614,\\\\n        \\\\\\\"t_stat\\\\\\\": 6.384719991949423,\\\\n        \\\\\\\"raw_p\\\\\\\": 0.0030881523071242785,\\\\n        \\\\\\\"cohens_d\\\\\\\": 2.6410799044016096,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.024705218456994228,\\\\n        \\\\\\\"significant\\\\\\\": true\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"graduated_a0.9\\\\\\\",\\\\n          \\\\\\\"dsir\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.0022788776527560063,\\\\n        \\\\\\\"t_stat\\\\\\\": 5.003666137605971,\\\\n        \\\\\\\"raw_p\\\\\\\": 0.007471036682110306,\\\\n        \\\\\\\"cohens_d\\\\\\\": 3.4914862437758036,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.05229725677477214,\\\\n        \\\\\\\"significant\\\\\\\": false\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"graduated_a0.9\\\\\\\",\\\\n          \\\\\\\"no-filter\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.0027061672126477586,\\\\n        \\\\\\\"t_stat\\\\\\\": 4.861418300116258,\\\\n        \\\\\\\"raw_p\\\\\\\": 0.008270807199636267,\\\\n        \\\\\\\"cohens_d\\\\\\\": 2.6316647720448314,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.05229725677477214,\\\\n        \\\\\\\"significant\\\\\\\": false\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"surprisal\\\\\\\",\\\\n          \\\\\\\"dsir\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.002506765418031609,\\\\n        \\\\\\\"t_stat\\\\\\\": 4.677147230384029,\\\\n        \\\\\\\"raw_p\\\\\\\": 0.00946778993302357,\\\\n        \\\\\\\"cohens_d\\\\\\\": 3.228814318222188,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.05229725677477214,\\\\n        \\\\\\\"significant\\\\\\\": false\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n          \\\\\\\"binary-drayson\\\\\\\",\\\\n          \\\\\\\"graduated_a0.9\\\\\\\"\\\\n        ],\\\\n        \\\\\\\"mean_diff\\\\\\\": 0.0021506907847885113,\\\\n        \\\\\\\"t_stat\\\\\\\": 2.9940639785296623,\\\\n        \\\\\\\"raw_p\\\\\\\": 0.04017657284695923,\\\\n        \\\\\\\"cohens_d\\\\\\\": 2.2093289931439317,\\\\n        \\\\\\\"corrected_p\\\\\\\": 0.16070629138783693,\\\\n        \\\\\\\"significant\\\\\\\": false\\\\n      },\\\\n      {\\\\n        \\\\\\\"pair\\\\\\\": [\\\\n         \\\\n\\\\n... [截断: 输出过长，省略 31807 字符] ...\\\\n\\\\n: false\\\\n        },\\\\n        {\\\\n          \\\\\\\"pair\\\\\\\": [\\\\n            \\\\\\\"graduated_a0.9\\\\\\\",\\\\n            \\\\\\\"graduated_a0.7\\\\\\\"\\\\n          ],\\\\n          \\\\\\\"mean_diff\\\\\\\": 0.0005775741884086916,\\\\n          \\\\\\\"t_stat\\\\\\\": 2.6640282306129635,\\\\n          \\\\\\\"raw_p\\\\\\\": 0.05615411746185,\\\\n          \\\\\\\"cohens_d\\\\\\\": 0.9496718778626968,\\\\n          \\\\\\\"corrected_p\\\\\\\": 0.7123999492078322,\\\\n          \\\\\\\"significant\\\\\\\": false\\\\n        },\\\\n        {\\\\n          \\\\\\\"pair\\\\\\\": [\\\\n            \\\\\\\"binary-ours\\\\\\\",\\\\n            \\\\\\\"graduated_a0.5\\\\\\\"\\\\n          ],\\\\n          \\\\\\\"mean_diff\\\\\\\": 0.0014538936466839346,\\\\n          \\\\\\\"t_stat\\\\\\\": 2.645379028333393,\\\\n          \\\\\\\"raw_p\\\\\\\": 0.05725750005173216,\\\\n          \\\\\\\"cohens_d\\\\\\\": 1.857951507889329,\\\\n          \\\\\\\"corrected_p\\\\\\\": 0.7123999492078322,\\\\n          \\\\\\\"significant\\\\\\\": false\\\\n        },\\\\n        {\\\\n          \\\\\\\"pair\\\\\\\": [\\\\n            \\\\\\\"graduated_a0.9\\\\\\\",\\\\n            \\\\\\\"graduated_a0.5\\\\\\\"\\\\n          ],\\\\n          \\\\\\\"mean_diff\\\\\\\": 0.0014538936466839346,\\\\n          \\\\\\\"t_stat\\\\\\\": 2.4449061127512546,\\\\n          \\\\\\\"raw_p\\\\\\\": 0.07083284836349661,\\\\n          \\\\\\\"cohens_d\\\\\\\": 1.7608262523341858,\\\\n          \\\\\\\"corrected_p\\\\\\\": 0.7123999492078322,\\\\n          \\\\\\\"significant\\\\\\\": false\\\\n        },\\\\n        {\\\\n          \\\\\\\"pair\\\\\\\": [\\\\n            \\\\\\\"graduated_a0.5\\\\\\\",\\\\n            \\\\\\\"graduated_a0.7\\\\\\\"\\\\n          ],\\\\n          \\\\\\\"mean_diff\\\\\\\": -0.0008763194582752431,\\\\n          \\\\\\\"t_stat\\\\\\\": -2.176991062379295,\\\\n          \\\\\\\"raw_p\\\\\\\": 0.0950637475781524,\\\\n          \\\\\\\"cohens_d\\\\\\\": -1.260362178309412,\\\\n          \\\\\\\"corrected_p\\\\\\\": 0.8555737282033716,\\\\n          \\\\\\\"significant\\\\\\\": false\\\\n        },\\\\n        {\\\\n          \\\\\\\"pair\\\\\\\": [\\\\n            \\\\\\\"dsir\\\\\\\",\\\\n            \\\\\\\"graduated_a0.1\\\\\\\"\\\\n          ],\\\\n          \\\\\\\"mean_diff\\\\\\\": -0.0009759012148974566,\\\\n          \\\\\\\"t_stat\\\\\\\": -1.9278792146434196,\\\\n          \\\\\\\"raw_p\\\\\\\": 0.12612268686357775,\\\\n          \\\\\\\"cohens_d\\\\\\\": -1.0789444898238614,\\\\n          \\\\\\\"corrected_p\\\\\\\": 1.0,\\\\n          \\\\\\\"significant\\\\\\\": false\\\\n        },\\\\n        {\\\\n          \\\\\\\"pair\\\\\\\": [\\\\n            \\\\\\\"binary-drayson\\\\\\\",\\\\n            \\\\\\\"graduated_a0.7\\\\\\\"\\\\n          ],\\\\n          \\\\\\\"mean_diff\\\\\\\": -0.0004779924317864781,\\\\n          \\\\\\\"t_stat\\\\\\\": -1.4191497503736252,\\\\n          \\\\\\\"raw_p\\\\\\\": 0.22886008250149933,\\\\n          \\\\\\\"cohens_d\\\\\\\": -1.0474458731326661,\\\\n          \\\\\\\"corrected_p\\\\\\\": 1.0,\\\\n          \\\\\\\"significant\\\\\\\": false\\\\n        },\\\\n        {\\\\n          \\\\\\\"pair\\\\\\\": [\\\\n            \\\\\\\"binary-drayson\\\\\\\",\\\\n            \\\\\\\"graduated_a0.5\\\\\\\"\\\\n          ],\\\\n          \\\\\\\"mean_diff\\\\\\\": 0.00039832702648876504,\\\\n          \\\\\\\"t_stat\\\\\\\": 0.7519115803969555,\\\\n          \\\\\\\"raw_p\\\\\\\": 0.49392844139373543,\\\\n          \\\\\\\"cohens_d\\\\\\\": 0.552315517513844,\\\\n          \\\\\\\"corrected_p\\\\\\\": 1.0,\\\\n          \\\\\\\"significant\\\\\\\": false\\\\n        },\\\\n        {\\\\n          \\\\\\\"pair\\\\\\\": [\\\\n            \\\\\\\"no-filter\\\\\\\",\\\\n            \\\\\\\"graduated_a0.1\\\\\\\"\\\\n          ],\\\\n          \\\\\\\"mean_diff\\\\\\\": -0.0002788289185421622,\\\\n          \\\\\\\"t_stat\\\\\\\": -0.6803013430499374,\\\\n          \\\\\\\"raw_p\\\\\\\": 0.533651991130784,\\\\n          \\\\\\\"cohens_d\\\\\\\": -0.29034647452456464,\\\\n          \\\\\\\"corrected_p\\\\\\\": 1.0,\\\\n          \\\\\\\"significant\\\\\\\": false\\\\n        },\\\\n        {\\\\n          \\\\\\\"pair\\\\\\\": [\\\\n            \\\\\\\"surprisal\\\\\\\",\\\\n            \\\\\\\"graduated_a0.1\\\\\\\"\\\\n          ],\\\\n          \\\\\\\"mean_diff\\\\\\\": 3.9832702648867625e-05,\\\\n          \\\\\\\"t_stat\\\\\\\": 0.09600307214745031,\\\\n          \\\\\\\"raw_p\\\\\\\": 0.9281356155015111,\\\\n          \\\\\\\"cohens_d\\\\\\\": 0.04611123341633106,\\\\n          \\\\\\\"corrected_p\\\\\\\": 1.0,\\\\n          \\\\\\\"significant\\\\\\\": false\\\\n        },\\\\n        {\\\\n          \\\\\\\"pair\\\\\\\": [\\\\n            \\\\\\\"binary-ours\\\\\\\",\\\\n            \\\\\\\"graduated_a0.9\\\\\\\"\\\\n          ],\\\\n          \\\\\\\"mean_diff\\\\\\\": 0.0,\\\\n          \\\\\\\"t_stat\\\\\\\": 0.0,\\\\n          \\\\\\\"raw_p\\\\\\\": 1.0,\\\\n          \\\\\\\"cohens_d\\\\\\\": 0.0,\\\\n          \\\\\\\"corrected_p\\\\\\\": 1.0,\\\\n          \\\\\\\"significant\\\\\\\": false\\\\n        }\\\\n      ],\\\\n      \\\\\\\"correction_method\\\\\\\": \\\\\\\"Holm-Bonferroni\\\\\\\",\\\\n      \\\\\\\"n_comparisons\\\\\\\": 45\\\\n    }\\\\n  },\\\\n  \\\\\\\"key_findings\\\\\\\": \\\\\\\"MMLU: 8/15 pairs significant after Holm-Bonferroni correction. HellaSwag: 9/15 pairs significant after Holm-Bonferroni correction. Largest MMLU effect sizes: binary-ours vs dsir (d=10.84, p_corr=0.0002); binary-ours vs no-filter (d=7.38, p_corr=0.0022); binary-drayson vs dsir (d=5.72, p_corr=0.0027) Largest HellaSwag effect sizes: binary-ours vs dsir (d=10.19, p_corr=0.0006); binary-drayson vs dsir (d=9.64, p_corr=0.0029); graduated_a0.9 vs dsir (d=9.53, p_corr=0.0005)\\\\\\\"\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.07}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mmlu\\\": {\\n    \\\"pairwise_comparisons\\\": [\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-ours\\\",\\n          \\\"dsir\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.007235436547500362,\\n        \\\"t_stat\\\": 24.598249063205415,\\n        \\\"raw_p\\\": 1.6209310233228965e-05,\\n        \\\"cohens_d\\\": 10.836755388457677,\\n        \\\"corrected_p\\\": 0.00024313965349843447,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-ours\\\",\\n          \\\"binary-drayson\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0028058681099558448,\\n        \\\"t_stat\\\": 17.515436444289804,\\n        \\\"raw_p\\\": 6.238619313918888e-05,\\n        \\\"cohens_d\\\": 2.852751540168622,\\n        \\\"corrected_p\\\": 0.0008734067039486444,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-ours\\\",\\n          \\\"no-filter\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.007662726107392115,\\n        \\\"t_stat\\\": 13.593055060087883,\\n        \\\"raw_p\\\": 0.00016957959325503732,\\n        \\\"cohens_d\\\": 7.383036494013822,\\n        \\\"corrected_p\\\": 0.0022045347123154854,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-drayson\\\",\\n          \\\"dsir\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.004429568437544518,\\n        \\\"t_stat\\\": 12.607532539957875,\\n        \\\"raw_p\\\": 0.00022784095885562328,\\n        \\\"cohens_d\\\": 5.717501056881729,\\n        \\\"corrected_p\\\": 0.0027340915062674795,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-ours\\\",\\n          \\\"graduated_a0.9\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0049565588947443565,\\n        \\\"t_stat\\\": 8.556802169125492,\\n        \\\"raw_p\\\": 0.0010241458708119772,\\n        \\\"cohens_d\\\": 5.5653292827627565,\\n        \\\"corrected_p\\\": 0.011265604578931748,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-drayson\\\",\\n          \\\"no-filter\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.00485685799743627,\\n        \\\"t_stat\\\": 7.239768218559279,\\n        \\\"raw_p\\\": 0.0019316941682584218,\\n        \\\"cohens_d\\\": 4.376382983859104,\\n        \\\"corrected_p\\\": 0.01931694168258422,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-ours\\\",\\n          \\\"surprisal\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.004728671129468754,\\n        \\\"t_stat\\\": 6.920422255077682,\\n        \\\"raw_p\\\": 0.002288028327494149,\\n        \\\"cohens_d\\\": 4.801394133053051,\\n        \\\"corrected_p\\\": 0.02059225494744734,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"surprisal\\\",\\n          \\\"no-filter\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0029340549779233614,\\n        \\\"t_stat\\\": 6.384719991949423,\\n        \\\"raw_p\\\": 0.0030881523071242785,\\n        \\\"cohens_d\\\": 2.6410799044016096,\\n        \\\"corrected_p\\\": 0.024705218456994228,\\n        \\\"significant\\\": true\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"graduated_a0.9\\\",\\n          \\\"dsir\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0022788776527560063,\\n        \\\"t_stat\\\": 5.003666137605971,\\n        \\\"raw_p\\\": 0.007471036682110306,\\n        \\\"cohens_d\\\": 3.4914862437758036,\\n        \\\"corrected_p\\\": 0.05229725677477214,\\n        \\\"significant\\\": false\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"graduated_a0.9\\\",\\n          \\\"no-filter\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0027061672126477586,\\n        \\\"t_stat\\\": 4.861418300116258,\\n        \\\"raw_p\\\": 0.008270807199636267,\\n        \\\"cohens_d\\\": 2.6316647720448314,\\n        \\\"corrected_p\\\": 0.05229725677477214,\\n        \\\"significant\\\": false\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"surprisal\\\",\\n          \\\"dsir\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.002506765418031609,\\n        \\\"t_stat\\\": 4.677147230384029,\\n        \\\"raw_p\\\": 0.00946778993302357,\\n        \\\"cohens_d\\\": 3.228814318222188,\\n        \\\"corrected_p\\\": 0.05229725677477214,\\n        \\\"significant\\\": false\\n      },\\n      {\\n        \\\"pair\\\": [\\n          \\\"binary-drayson\\\",\\n          \\\"graduated_a0.9\\\"\\n        ],\\n        \\\"mean_diff\\\": 0.0021506907847885113,\\n        \\\"t_stat\\\": 2.9940639785296623,\\n        \\\"raw_p\\\": 0.04017657284695923,\\n        \\\"cohens_d\\\": 2.2093289931439317,\\n        \\\"corrected_p\\\": 0.16070629138783693,\\n        \\\"significant\\\": false\\n      },\\n      {\\n        \\\"pair\\\": [\\n         \\n\\n... [截断: 输出过长，省略 31807 字符] ...\\n\\n: false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"graduated_a0.9\\\",\\n            \\\"graduated_a0.7\\\"\\n          ],\\n          \\\"mean_diff\\\": 0.0005775741884086916,\\n          \\\"t_stat\\\": 2.6640282306129635,\\n          \\\"raw_p\\\": 0.05615411746185,\\n          \\\"cohens_d\\\": 0.9496718778626968,\\n          \\\"corrected_p\\\": 0.7123999492078322,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"binary-ours\\\",\\n            \\\"graduated_a0.5\\\"\\n          ],\\n          \\\"mean_diff\\\": 0.0014538936466839346,\\n          \\\"t_stat\\\": 2.645379028333393,\\n          \\\"raw_p\\\": 0.05725750005173216,\\n          \\\"cohens_d\\\": 1.857951507889329,\\n          \\\"corrected_p\\\": 0.7123999492078322,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"graduated_a0.9\\\",\\n            \\\"graduated_a0.5\\\"\\n          ],\\n          \\\"mean_diff\\\": 0.0014538936466839346,\\n          \\\"t_stat\\\": 2.4449061127512546,\\n          \\\"raw_p\\\": 0.07083284836349661,\\n          \\\"cohens_d\\\": 1.7608262523341858,\\n          \\\"corrected_p\\\": 0.7123999492078322,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"graduated_a0.5\\\",\\n            \\\"graduated_a0.7\\\"\\n          ],\\n          \\\"mean_diff\\\": -0.0008763194582752431,\\n          \\\"t_stat\\\": -2.176991062379295,\\n          \\\"raw_p\\\": 0.0950637475781524,\\n          \\\"cohens_d\\\": -1.260362178309412,\\n          \\\"corrected_p\\\": 0.8555737282033716,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"dsir\\\",\\n            \\\"graduated_a0.1\\\"\\n          ],\\n          \\\"mean_diff\\\": -0.0009759012148974566,\\n          \\\"t_stat\\\": -1.9278792146434196,\\n          \\\"raw_p\\\": 0.12612268686357775,\\n          \\\"cohens_d\\\": -1.0789444898238614,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"binary-drayson\\\",\\n            \\\"graduated_a0.7\\\"\\n          ],\\n          \\\"mean_diff\\\": -0.0004779924317864781,\\n          \\\"t_stat\\\": -1.4191497503736252,\\n          \\\"raw_p\\\": 0.22886008250149933,\\n          \\\"cohens_d\\\": -1.0474458731326661,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"binary-drayson\\\",\\n            \\\"graduated_a0.5\\\"\\n          ],\\n          \\\"mean_diff\\\": 0.00039832702648876504,\\n          \\\"t_stat\\\": 0.7519115803969555,\\n          \\\"raw_p\\\": 0.49392844139373543,\\n          \\\"cohens_d\\\": 0.552315517513844,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"no-filter\\\",\\n            \\\"graduated_a0.1\\\"\\n          ],\\n          \\\"mean_diff\\\": -0.0002788289185421622,\\n          \\\"t_stat\\\": -0.6803013430499374,\\n          \\\"raw_p\\\": 0.533651991130784,\\n          \\\"cohens_d\\\": -0.29034647452456464,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"surprisal\\\",\\n            \\\"graduated_a0.1\\\"\\n          ],\\n          \\\"mean_diff\\\": 3.9832702648867625e-05,\\n          \\\"t_stat\\\": 0.09600307214745031,\\n          \\\"raw_p\\\": 0.9281356155015111,\\n          \\\"cohens_d\\\": 0.04611123341633106,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        },\\n        {\\n          \\\"pair\\\": [\\n            \\\"binary-ours\\\",\\n            \\\"graduated_a0.9\\\"\\n          ],\\n          \\\"mean_diff\\\": 0.0,\\n          \\\"t_stat\\\": 0.0,\\n          \\\"raw_p\\\": 1.0,\\n          \\\"cohens_d\\\": 0.0,\\n          \\\"corrected_p\\\": 1.0,\\n          \\\"significant\\\": false\\n        }\\n      ],\\n      \\\"correction_method\\\": \\\"Holm-Bonferroni\\\",\\n      \\\"n_comparisons\\\": 45\\n    }\\n  },\\n  \\\"key_findings\\\": \\\"MMLU: 8/15 pairs significant after Holm-Bonferroni correction. HellaSwag: 9/15 pairs significant after Holm-Bonferroni correction. Largest MMLU effect sizes: binary-ours vs dsir (d=10.84, p_corr=0.0002); binary-ours vs no-filter (d=7.38, p_corr=0.0022); binary-drayson vs dsir (d=5.72, p_corr=0.0027) Largest HellaSwag effect sizes: binary-ours vs dsir (d=10.19, p_corr=0.0006); binary-drayson vs dsir (d=9.64, p_corr=0.0029); graduated_a0.9 vs dsir (d=9.53, p_corr=0.0005)\\\"\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.07}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

文件已截断，用 python 精确提取目标数值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "b4bcedf1-0f99-402d-923c-aa6ca0d4a31b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J64H7tL2yYE5ToXFYUsqS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4315,
      "cache_read_input_tokens": 23447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4315
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013cXGMXQ2n1abznQJz4A39s`</summary>

```json
{
  "server": "westc-26893",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/gen-depth-contamination/artifacts/exp_E_paired_stats.json')); pairs=d['mmlu']['pairwise_comparisons']; [print(p['pair'],p['corrected_p']) for p in pairs if set(p['pair'])=={'graduated_a0.9','no-filter'} or set(p['pair'])=={'surprisal','dsir'}]\"",
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
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "40ad6885-a44a-476b-8e60-70c85127fc89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J64H7tL2yYE5ToXFYUsqS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4315,
      "cache_read_input_tokens": 23447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4315
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

_source line 11 · 2026-05-15T14:30:13.268Z_

<details><summary>↩ Tool result · `toolu_013cXGMXQ2n1abznQJz4A39s`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "198be0c3-e7b7-486f-9f2c-40e1fcbf0642",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Liyh69SqNG3PEkwQs3Voyf`</summary>

```json
{
  "server": "westc-26893",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/gen-depth-contamination/artifacts/exp_E_paired_stats.json')); pairs=d['mmlu']['pairwise_comparisons']; [print(p['pair'],p['corrected_p']) for p in pairs if set(p['pair'])=={'graduated_a0.9','no-filter'} or set(p['pair'])=={'surprisal','dsir'}]\"",
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
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "c43d4184-ee3a-4bdb-8b11-ba8bb55b8d2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UM1eQAEL8PDYRQp3GE74jR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 330,
      "cache_read_input_tokens": 27762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 330
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

_source line 13 · 2026-05-15T14:30:16.978Z_

<details><summary>↩ Tool result · `toolu_01Liyh69SqNG3PEkwQs3Voyf`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "8f5e6c61-a4a1-44df-aed1-f42c4505e961",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

````text
The semicolons are blocked. Let me use grep instead to find the specific pairs, or use a python one-liner without semicolons.

Actually, I already have the data from the first cat command. Let me look at what was returned.

From the output, I can see the MMLU pairwise comparisons. Let me find the two pairs:

1. graduated_a0.9 vs no-filter:
```
"pair": ["graduated_a0.9", "no-filter"],
"mean_diff": 0.0027061672126477586,
"t_stat": 4.861418300116258,


"raw_p": 0.008270807199636267,
"cohens_d": 2.6316647720448314,
"corrected_p": 0.05229725677477214,
"significant": false
```

2. surprisal vs dsir:
```
"pair": ["surprisal", "dsir"],
"mean_diff": 0.002506765418031609,
"t_stat": 4.677147230384029,
"raw_p": 0.00946778993302357,
"cohens_d": 3.228814318222188,
"corrected_p": 0.05229725677477214,
"significant": false
```

Both comparisons show strong t-statistics and Cohen's d values, but after multiple comparison correction, neither reaches statistical significance.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "c8cd197b-5678-41d3-a6e7-a13bb0b9458d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBAXEUnCTHUU44xafntSTA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 28092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 310
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

_source line 15_

从第一次读取的输出中已提取到两个值：

```
graduated_a0.9 vs no-filter (MMLU): p_holm = 0.05229725677477214
surprisal vs dsir (MMLU): p_holm = 0.05229725677477214
```

两个 pair 的 Holm-Bonferroni 校正后 p 值相同（`corrected_p = 0.05229725677477214`），均未达到显著性阈值（`significant: false`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "uuid": "0e702373-dd5d-4be6-ade2-d3b43bf4b599",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BBAXEUnCTHUU44xafntSTA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 28092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 310
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

### Task result

_source line 16_

从第一次读取的输出中已提取到两个值：

```
graduated_a0.9 vs no-filter (MMLU): p_holm = 0.05229725677477214
surprisal vs dsir (MMLU): p_holm = 0.05229725677477214
```

两个 pair 的 Holm-Bonferroni 校正后 p 值相同（`corrected_p = 0.05229725677477214`），均未达到显著性阈值（`significant: false`）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 29774,
  "duration_api_ms": 26745,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "a2d17b61-7870-4a43-b140-665d9f95c8a4",
  "total_cost_usd": 0.19139274999999997,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 16561,
    "cache_read_input_tokens": 114131,
    "output_tokens": 1186,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 16561,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 483,
        "cache_read_input_tokens": 28092,
        "cache_creation_input_tokens": 310,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 310
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1006,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001126,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 1186,
      "cacheReadInputTokens": 114131,
      "cacheCreationInputTokens": 16561,
      "webSearchRequests": 0,
      "costUSD": 0.19026674999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f2153423-5520-4015-a575-3c411200aa0f"
}
```

</details>

---
