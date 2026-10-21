# debug read action trajectory results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_debug_read_action_trajectory_results_20260518T105940.log`
- **Structured JSON:** [`36629fb57b519f1bd305.json`](../../sessions/36/36629fb57b519f1bd305.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "b17ca778-4bc0-4bf9-afb1-5b60fdee0a3b",
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
  "uuid": "d8471bc0-008a-4c60-847f-68cec5ebb92d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779112800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "09ee9669-cc61-4a28-ac1c-402c3b0cc371",
  "session_id": "b17ca778-4bc0-4bf9-afb1-5b60fdee0a3b"
}
```

---

### Tool call

_source line 4_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UFwFdB1H71FfyEH39WRZ59`</summary>

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
  "session_id": "b17ca778-4bc0-4bf9-afb1-5b60fdee0a3b",
  "uuid": "850a962a-9a60-41fc-95d4-759f0e5a0476",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CT541s1Ppw9o3ouCs8gKSn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12254,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12254
      },
      "output_tokens": 53,
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

_source line 5 · 2026-05-18T10:59:53.680Z_

<details><summary>↩ Tool result · `toolu_01UFwFdB1H71FfyEH39WRZ59`</summary>

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
  "session_id": "b17ca778-4bc0-4bf9-afb1-5b60fdee0a3b",
  "uuid": "e25f116c-7b56-457f-bb37-19050ce9f247",
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

_source line 6_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Jgx3Z8QKdSWzKWrCuSthrS`</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b17ca778-4bc0-4bf9-afb1-5b60fdee0a3b",
  "uuid": "c643f9db-5d1b-4be1-85a9-b2a0e1836fae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkV7pYFTdTDEMEFCGxhnbQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 24095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 427
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

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GhrFGMjX94nXDZAtoAcuug`</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -30 /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b17ca778-4bc0-4bf9-afb1-5b60fdee0a3b",
  "uuid": "0477f31e-9893-431e-b5d7-6fd1c439f45f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WkV7pYFTdTDEMEFCGxhnbQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 24095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 427
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

_source line 8 · 2026-05-18T10:59:58.108Z_

<details><summary>↩ Tool result · `toolu_01Jgx3Z8QKdSWzKWrCuSthrS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"n_tasks\\\": 5,\\n    \\\"n_demos_per_task\\\": 10,\\n    \\\"n_timesteps_per_demo\\\": 50,\\n    \\\"total_forward_passes\\\": 5000,\\n    \\\"model\\\": \\\"openvla-7b\\\",\\n    \\\"ablation\\\": \\\"L1_dominant_24_heads_zeroed\\\",\\n    \\\"ablated_heads\\\": [\\n      0,\\n      1,\\n      2,\\n      4,\\n      7,\\n      8,\\n      10,\\n      11,\\n      12,\\n      14,\\n      15,\\n      16,\\n      17,\\n      18,\\n      19,\\n      20,\\n      22,\\n      23,\\n      25,\\n      26,\\n      27,\\n      29,\\n      30,\\n      31\\n    ],\\n    \\\"unnorm_key\\\": \\\"bridge_orig\\\"\\n  },\\n  \\\"main_metrics\\\": {\\n    \\\"paired_action_mse\\\": {\\n      \\\"mean\\\": 0.04164548042967141,\\n      \\\"std\\\": 0.06394581517413622,\\n      \\\"t_stat\\\": 32.55658746950337,\\n      \\\"p_value\\\": 3.9875267301509806e-194,\\n      \\\"cohens_d\\\": 0.6511317493798869\\n    },\\n    \\\"per_dim_action_shift\\\": {\\n      \\\"means\\\": [\\n        0.0018907630960015738,\\n        0.0053060349467249435,\\n        0.007621298928714849,\\n        0.02059210950341174,\\n        0.030713564767946917,\\n        0.033881929667518705,\\n        0.2907168627450989\\n      ],\\n      \\\"stds\\\": [\\n        0.003945774709271799,\\n        0.007996728850961761,\\n        0.00855598404937074,\\n        0.02115830546884926,\\n        0.02858547485740179,\\n        0.037737860644735575,\\n        0.44894904084862064\\n      ],\\n      \\\"dim_names\\\": [\\n        \\\"dx\\\",\\n        \\\"dy\\\",\\n        \\\"dz\\\",\\n        \\\"rx\\\",\\n        \\\"ry\\\",\\n        \\\"rz\\\",\\n        \\\"gripper\\\"\\n      ]\\n    },\\n    \\\"token_divergence_rate\\\": 0.7230285714285715\\n  },\\n  \\\"secondary_metrics\\\": {\\n    \\\"kl_divergence\\\": {\\n      \\\"mean\\\": 5.07937479019165,\\n      \\\"std\\\": 4.961368560791016,\\n      \\\"per_token_position\\\": [\\n        0.29015398025512695,\\n        3.0104427337646484,\\n        5.949150562286377,\\n        7.421013832092285,\\n        8.960497856140137,\\n        8.479713439941406,\\n        1.4446604251861572\\n      ]\\n    },\\n    \\\"mse_vs_gt_baseline\\\": {\\n      \\\"mean\\\": 0.43176415822445635,\\n      \\\"std\\\": 0.22077793994025996,\\n      \\\"note\\\": \\\"OOD, secondary\\\"\\n    },\\n    \\\"mse_vs_gt_ablated\\\": {\\n      \\\"mean\\\": 0.4357406635106642,\\n      \\\"std\\\": 0.2235285616028443,\\n      \\\"note\\\": \\\"OOD, secondary\\\"\\n    },\\n    \\\"wilcoxon_p\\\": 0.0\\n  },\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.02242838426504113,\\n        \\\"std\\\": 0.051757195878257986,\\n        \\\"t_stat\\\": 9.680048252096263,\\n        \\\"p_value\\\": 2.0038975148954835e-20,\\n        \\\"cohens_d\\\": 0.4329049183349495\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0014037795379863059,\\n          0.004451050012665628,\\n          0.006329343725828563,\\n          0.019142500603928258,\\n          0.030247070985899276,\\n          0.03025989703622987,\\n          0.15281568627450998\\n        ],\\n        \\\"stds\\\": [\\n          0.00311317121105672,\\n          0.007885665398470972,\\n          0.008240969667318977,\\n          0.019615421748166623,\\n          0.028676831314892466,\\n          0.033095946085946286,\\n          0.3590890901162581\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.664,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 4.503225326538086,\\n        \\\"std\\\": 4.8421173095703125\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.04458787875675457,\\n        \\\"std\\\": 0.0648704634241749,\\n        \\\"t_stat\\\": 15.353948651915177,\\n        \\\"p_value\\\": 7.46250518536467e-44,\\n        \\\"cohens_d\\\": 0.6866494581638973\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0017330280210831573,\\n          0.005302538340663201,\\n          0.007163902512666055,\\n          0.020680235506992665,\\n          0.03485707990039093,\\n          0.03459241025841939,\\n          0.3118901960784321\\n        ],\\n        \\\"stds\\\": [\\n          0.0037620949894889076,\\n          0.00825352063013232,\\n          0.007593216730760563,\\n          0.020277157204501794,\\n          0.03162330967091224,\\n          0.038133676245909076,\\n          0.4570695648337024\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.7094285714285714,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 5.153635501861572,\\n        \\\"std\\\": 5.071208477020264\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.04681500022487693,\\n        \\\"std\\\": 0.06645561015488266,\\n        \\\"t_stat\\\": 15.736337189550586,\\n        \\\"p_value\\\": 1.3382496765371354e-45,\\n        \\\"cohens_d\\\": 0.7037503934432828\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.002803980288112861,\\n          0.0054708934473395275,\\n          0.007187286787515175,\\n          0.018410671617669166,\\n          0.02898102668941719,\\n          0.02812265279046228,\\n          0.3252549019607852\\n        ],\\n        \\\"stds\\\": [\\n          0.0057296098847649055,\\n          0.007560437193942133,\\n          0.007359340564353495,\\n          0.018759688881726206,\\n          0.028137334353327288,\\n          0.02949191003799571,\\n          0.46658065445606245\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.7385714285714285,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 5.972511291503906,\\n        \\\"std\\\": 5.5687432289123535\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.04585327669100103,\\n        \\\"std\\\": 0.06512121324514131,\\n        \\\"t_stat\\\": 15.728893275695137,\\n        \\\"p_value\\\": 1.4476730761513222e-45,\\n        \\\"cohens_d\\\": 0.7034174914950824\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0016636890063005333,\\n          0.0052034678355805915,\\n          0.00747777144619647,\\n          0.020320068361922777,\\n          0.028729157559535055,\\n          0.035562712698805565,\\n          0.3252549019607849\\n        ],\\n        \\\"stds\\\": [\\n          0.00306018861719437,\\n          0.008431160867942903,\\n          0.008048276555242978,\\n          0.021654913911754142,\\n          0.026055373152750017,\\n          0.03568682198764817,\\n          0.4582868723436793\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.7365714285714285,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 4.935613632202148,\\n        \\\"std\\\": 4.755918502807617\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.048542862210683366,\\n        \\\"std\\\": 0.06656781244085376,\\n        \\\"t_stat\\\": 16.28963552846279,\\n        \\\"p_value\\\": 3.759600472033675e-48,\\n        \\\"cohens_d\\\": 0.7284946473958375\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0018493386265249795,\\n          0.00610222509737575,\\n          0.009948190171367981,\\n          0.024407071426545815,\\n          0.030753488704492044,\\n          0.04087197555367618,\\n          0.338368627450981\\n        ],\\n        \\\"stds\\\": [\\n          0.003264664633536739,\\n          0.0077321877439992396,\\n          0.010677892843435068,\\n          0.024496624444718028,\\n          0.027718819464147733,\\n          0.048263969493824666,\\n          0.46698264708631304\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.7665714285714286,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 4.831889629364014,\\n        \\\"std\\\": 4.366452693939209\\n      },\\n      \\\"n_samples\\\": 500\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.19}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b17ca778-4bc0-4bf9-afb1-5b60fdee0a3b",
  "uuid": "abe4aca2-f673-4297-9e93-519536e4c9b1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"n_tasks\\\\\\\": 5,\\\\n    \\\\\\\"n_demos_per_task\\\\\\\": 10,\\\\n    \\\\\\\"n_timesteps_per_demo\\\\\\\": 50,\\\\n    \\\\\\\"total_forward_passes\\\\\\\": 5000,\\\\n    \\\\\\\"model\\\\\\\": \\\\\\\"openvla-7b\\\\\\\",\\\\n    \\\\\\\"ablation\\\\\\\": \\\\\\\"L1_dominant_24_heads_zeroed\\\\\\\",\\\\n    \\\\\\\"ablated_heads\\\\\\\": [\\\\n      0,\\\\n      1,\\\\n      2,\\\\n      4,\\\\n      7,\\\\n      8,\\\\n      10,\\\\n      11,\\\\n      12,\\\\n      14,\\\\n      15,\\\\n      16,\\\\n      17,\\\\n      18,\\\\n      19,\\\\n      20,\\\\n      22,\\\\n      23,\\\\n      25,\\\\n      26,\\\\n      27,\\\\n      29,\\\\n      30,\\\\n      31\\\\n    ],\\\\n    \\\\\\\"unnorm_key\\\\\\\": \\\\\\\"bridge_orig\\\\\\\"\\\\n  },\\\\n  \\\\\\\"main_metrics\\\\\\\": {\\\\n    \\\\\\\"paired_action_mse\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.04164548042967141,\\\\n      \\\\\\\"std\\\\\\\": 0.06394581517413622,\\\\n      \\\\\\\"t_stat\\\\\\\": 32.55658746950337,\\\\n      \\\\\\\"p_value\\\\\\\": 3.9875267301509806e-194,\\\\n      \\\\\\\"cohens_d\\\\\\\": 0.6511317493798869\\\\n    },\\\\n    \\\\\\\"per_dim_action_shift\\\\\\\": {\\\\n      \\\\\\\"means\\\\\\\": [\\\\n        0.0018907630960015738,\\\\n        0.0053060349467249435,\\\\n        0.007621298928714849,\\\\n        0.02059210950341174,\\\\n        0.030713564767946917,\\\\n        0.033881929667518705,\\\\n        0.2907168627450989\\\\n      ],\\\\n      \\\\\\\"stds\\\\\\\": [\\\\n        0.003945774709271799,\\\\n        0.007996728850961761,\\\\n        0.00855598404937074,\\\\n        0.02115830546884926,\\\\n        0.02858547485740179,\\\\n        0.037737860644735575,\\\\n        0.44894904084862064\\\\n      ],\\\\n      \\\\\\\"dim_names\\\\\\\": [\\\\n        \\\\\\\"dx\\\\\\\",\\\\n        \\\\\\\"dy\\\\\\\",\\\\n        \\\\\\\"dz\\\\\\\",\\\\n        \\\\\\\"rx\\\\\\\",\\\\n        \\\\\\\"ry\\\\\\\",\\\\n        \\\\\\\"rz\\\\\\\",\\\\n        \\\\\\\"gripper\\\\\\\"\\\\n      ]\\\\n    },\\\\n    \\\\\\\"token_divergence_rate\\\\\\\": 0.7230285714285715\\\\n  },\\\\n  \\\\\\\"secondary_metrics\\\\\\\": {\\\\n    \\\\\\\"kl_divergence\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 5.07937479019165,\\\\n      \\\\\\\"std\\\\\\\": 4.961368560791016,\\\\n      \\\\\\\"per_token_position\\\\\\\": [\\\\n        0.29015398025512695,\\\\n        3.0104427337646484,\\\\n        5.949150562286377,\\\\n        7.421013832092285,\\\\n        8.960497856140137,\\\\n        8.479713439941406,\\\\n        1.4446604251861572\\\\n      ]\\\\n    },\\\\n    \\\\\\\"mse_vs_gt_baseline\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.43176415822445635,\\\\n      \\\\\\\"std\\\\\\\": 0.22077793994025996,\\\\n      \\\\\\\"note\\\\\\\": \\\\\\\"OOD, secondary\\\\\\\"\\\\n    },\\\\n    \\\\\\\"mse_vs_gt_ablated\\\\\\\": {\\\\n      \\\\\\\"mean\\\\\\\": 0.4357406635106642,\\\\n      \\\\\\\"std\\\\\\\": 0.2235285616028443,\\\\n      \\\\\\\"note\\\\\\\": \\\\\\\"OOD, secondary\\\\\\\"\\\\n    },\\\\n    \\\\\\\"wilcoxon_p\\\\\\\": 0.0\\\\n  },\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"open_the_middle_drawer_of_the_cabinet\\\\\\\": {\\\\n      \\\\\\\"paired_mse\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.02242838426504113,\\\\n        \\\\\\\"std\\\\\\\": 0.051757195878257986,\\\\n        \\\\\\\"t_stat\\\\\\\": 9.680048252096263,\\\\n        \\\\\\\"p_value\\\\\\\": 2.0038975148954835e-20,\\\\n        \\\\\\\"cohens_d\\\\\\\": 0.4329049183349495\\\\n      },\\\\n      \\\\\\\"per_dim_shift\\\\\\\": {\\\\n        \\\\\\\"means\\\\\\\": [\\\\n          0.0014037795379863059,\\\\n          0.004451050012665628,\\\\n          0.006329343725828563,\\\\n          0.019142500603928258,\\\\n          0.030247070985899276,\\\\n          0.03025989703622987,\\\\n          0.15281568627450998\\\\n        ],\\\\n        \\\\\\\"stds\\\\\\\": [\\\\n          0.00311317121105672,\\\\n          0.007885665398470972,\\\\n          0.008240969667318977,\\\\n          0.019615421748166623,\\\\n          0.028676831314892466,\\\\n          0.033095946085946286,\\\\n          0.3590890901162581\\\\n        ]\\\\n      },\\\\n      \\\\\\\"token_divergence_rate\\\\\\\": 0.664,\\\\n      \\\\\\\"kl_divergence\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 4.503225326538086,\\\\n        \\\\\\\"std\\\\\\\": 4.8421173095703125\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 500\\\\n    },\\\\n    \\\\\\\"open_the_top_drawer_and_put_the_bowl_inside\\\\\\\": {\\\\n      \\\\\\\"paired_mse\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.04458787875675457,\\\\n        \\\\\\\"std\\\\\\\": 0.0648704634241749,\\\\n        \\\\\\\"t_stat\\\\\\\": 15.353948651915177,\\\\n        \\\\\\\"p_value\\\\\\\": 7.46250518536467e-44,\\\\n        \\\\\\\"cohens_d\\\\\\\": 0.6866494581638973\\\\n      },\\\\n      \\\\\\\"per_dim_shift\\\\\\\": {\\\\n        \\\\\\\"means\\\\\\\": [\\\\n          0.0017330280210831573,\\\\n          0.005302538340663201,\\\\n          0.007163902512666055,\\\\n          0.020680235506992665,\\\\n          0.03485707990039093,\\\\n          0.03459241025841939,\\\\n          0.3118901960784321\\\\n        ],\\\\n        \\\\\\\"stds\\\\\\\": [\\\\n          0.0037620949894889076,\\\\n          0.00825352063013232,\\\\n          0.007593216730760563,\\\\n          0.020277157204501794,\\\\n          0.03162330967091224,\\\\n          0.038133676245909076,\\\\n          0.4570695648337024\\\\n        ]\\\\n      },\\\\n      \\\\\\\"token_divergence_rate\\\\\\\": 0.7094285714285714,\\\\n      \\\\\\\"kl_divergence\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 5.153635501861572,\\\\n        \\\\\\\"std\\\\\\\": 5.071208477020264\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 500\\\\n    },\\\\n    \\\\\\\"push_the_plate_to_the_front_of_the_stove\\\\\\\": {\\\\n      \\\\\\\"paired_mse\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.04681500022487693,\\\\n        \\\\\\\"std\\\\\\\": 0.06645561015488266,\\\\n        \\\\\\\"t_stat\\\\\\\": 15.736337189550586,\\\\n        \\\\\\\"p_value\\\\\\\": 1.3382496765371354e-45,\\\\n        \\\\\\\"cohens_d\\\\\\\": 0.7037503934432828\\\\n      },\\\\n      \\\\\\\"per_dim_shift\\\\\\\": {\\\\n        \\\\\\\"means\\\\\\\": [\\\\n          0.002803980288112861,\\\\n          0.0054708934473395275,\\\\n          0.007187286787515175,\\\\n          0.018410671617669166,\\\\n          0.02898102668941719,\\\\n          0.02812265279046228,\\\\n          0.3252549019607852\\\\n        ],\\\\n        \\\\\\\"stds\\\\\\\": [\\\\n          0.0057296098847649055,\\\\n          0.007560437193942133,\\\\n          0.007359340564353495,\\\\n          0.018759688881726206,\\\\n          0.028137334353327288,\\\\n          0.02949191003799571,\\\\n          0.46658065445606245\\\\n        ]\\\\n      },\\\\n      \\\\\\\"token_divergence_rate\\\\\\\": 0.7385714285714285,\\\\n      \\\\\\\"kl_divergence\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 5.972511291503906,\\\\n        \\\\\\\"std\\\\\\\": 5.5687432289123535\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 500\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_the_plate\\\\\\\": {\\\\n      \\\\\\\"paired_mse\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.04585327669100103,\\\\n        \\\\\\\"std\\\\\\\": 0.06512121324514131,\\\\n        \\\\\\\"t_stat\\\\\\\": 15.728893275695137,\\\\n        \\\\\\\"p_value\\\\\\\": 1.4476730761513222e-45,\\\\n        \\\\\\\"cohens_d\\\\\\\": 0.7034174914950824\\\\n      },\\\\n      \\\\\\\"per_dim_shift\\\\\\\": {\\\\n        \\\\\\\"means\\\\\\\": [\\\\n          0.0016636890063005333,\\\\n          0.0052034678355805915,\\\\n          0.00747777144619647,\\\\n          0.020320068361922777,\\\\n          0.028729157559535055,\\\\n          0.035562712698805565,\\\\n          0.3252549019607849\\\\n        ],\\\\n        \\\\\\\"stds\\\\\\\": [\\\\n          0.00306018861719437,\\\\n          0.008431160867942903,\\\\n          0.008048276555242978,\\\\n          0.021654913911754142,\\\\n          0.026055373152750017,\\\\n          0.03568682198764817,\\\\n          0.4582868723436793\\\\n        ]\\\\n      },\\\\n      \\\\\\\"token_divergence_rate\\\\\\\": 0.7365714285714285,\\\\n      \\\\\\\"kl_divergence\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 4.935613632202148,\\\\n        \\\\\\\"std\\\\\\\": 4.755918502807617\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 500\\\\n    },\\\\n    \\\\\\\"put_the_bowl_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"paired_mse\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 0.048542862210683366,\\\\n        \\\\\\\"std\\\\\\\": 0.06656781244085376,\\\\n        \\\\\\\"t_stat\\\\\\\": 16.28963552846279,\\\\n        \\\\\\\"p_value\\\\\\\": 3.759600472033675e-48,\\\\n        \\\\\\\"cohens_d\\\\\\\": 0.7284946473958375\\\\n      },\\\\n      \\\\\\\"per_dim_shift\\\\\\\": {\\\\n        \\\\\\\"means\\\\\\\": [\\\\n          0.0018493386265249795,\\\\n          0.00610222509737575,\\\\n          0.009948190171367981,\\\\n          0.024407071426545815,\\\\n          0.030753488704492044,\\\\n          0.04087197555367618,\\\\n          0.338368627450981\\\\n        ],\\\\n        \\\\\\\"stds\\\\\\\": [\\\\n          0.003264664633536739,\\\\n          0.0077321877439992396,\\\\n          0.010677892843435068,\\\\n          0.024496624444718028,\\\\n          0.027718819464147733,\\\\n          0.048263969493824666,\\\\n          0.46698264708631304\\\\n        ]\\\\n      },\\\\n      \\\\\\\"token_divergence_rate\\\\\\\": 0.7665714285714286,\\\\n      \\\\\\\"kl_divergence\\\\\\\": {\\\\n        \\\\\\\"mean\\\\\\\": 4.831889629364014,\\\\n        \\\\\\\"std\\\\\\\": 4.366452693939209\\\\n      },\\\\n      \\\\\\\"n_samples\\\\\\\": 500\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.19}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"n_tasks\\\": 5,\\n    \\\"n_demos_per_task\\\": 10,\\n    \\\"n_timesteps_per_demo\\\": 50,\\n    \\\"total_forward_passes\\\": 5000,\\n    \\\"model\\\": \\\"openvla-7b\\\",\\n    \\\"ablation\\\": \\\"L1_dominant_24_heads_zeroed\\\",\\n    \\\"ablated_heads\\\": [\\n      0,\\n      1,\\n      2,\\n      4,\\n      7,\\n      8,\\n      10,\\n      11,\\n      12,\\n      14,\\n      15,\\n      16,\\n      17,\\n      18,\\n      19,\\n      20,\\n      22,\\n      23,\\n      25,\\n      26,\\n      27,\\n      29,\\n      30,\\n      31\\n    ],\\n    \\\"unnorm_key\\\": \\\"bridge_orig\\\"\\n  },\\n  \\\"main_metrics\\\": {\\n    \\\"paired_action_mse\\\": {\\n      \\\"mean\\\": 0.04164548042967141,\\n      \\\"std\\\": 0.06394581517413622,\\n      \\\"t_stat\\\": 32.55658746950337,\\n      \\\"p_value\\\": 3.9875267301509806e-194,\\n      \\\"cohens_d\\\": 0.6511317493798869\\n    },\\n    \\\"per_dim_action_shift\\\": {\\n      \\\"means\\\": [\\n        0.0018907630960015738,\\n        0.0053060349467249435,\\n        0.007621298928714849,\\n        0.02059210950341174,\\n        0.030713564767946917,\\n        0.033881929667518705,\\n        0.2907168627450989\\n      ],\\n      \\\"stds\\\": [\\n        0.003945774709271799,\\n        0.007996728850961761,\\n        0.00855598404937074,\\n        0.02115830546884926,\\n        0.02858547485740179,\\n        0.037737860644735575,\\n        0.44894904084862064\\n      ],\\n      \\\"dim_names\\\": [\\n        \\\"dx\\\",\\n        \\\"dy\\\",\\n        \\\"dz\\\",\\n        \\\"rx\\\",\\n        \\\"ry\\\",\\n        \\\"rz\\\",\\n        \\\"gripper\\\"\\n      ]\\n    },\\n    \\\"token_divergence_rate\\\": 0.7230285714285715\\n  },\\n  \\\"secondary_metrics\\\": {\\n    \\\"kl_divergence\\\": {\\n      \\\"mean\\\": 5.07937479019165,\\n      \\\"std\\\": 4.961368560791016,\\n      \\\"per_token_position\\\": [\\n        0.29015398025512695,\\n        3.0104427337646484,\\n        5.949150562286377,\\n        7.421013832092285,\\n        8.960497856140137,\\n        8.479713439941406,\\n        1.4446604251861572\\n      ]\\n    },\\n    \\\"mse_vs_gt_baseline\\\": {\\n      \\\"mean\\\": 0.43176415822445635,\\n      \\\"std\\\": 0.22077793994025996,\\n      \\\"note\\\": \\\"OOD, secondary\\\"\\n    },\\n    \\\"mse_vs_gt_ablated\\\": {\\n      \\\"mean\\\": 0.4357406635106642,\\n      \\\"std\\\": 0.2235285616028443,\\n      \\\"note\\\": \\\"OOD, secondary\\\"\\n    },\\n    \\\"wilcoxon_p\\\": 0.0\\n  },\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.02242838426504113,\\n        \\\"std\\\": 0.051757195878257986,\\n        \\\"t_stat\\\": 9.680048252096263,\\n        \\\"p_value\\\": 2.0038975148954835e-20,\\n        \\\"cohens_d\\\": 0.4329049183349495\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0014037795379863059,\\n          0.004451050012665628,\\n          0.006329343725828563,\\n          0.019142500603928258,\\n          0.030247070985899276,\\n          0.03025989703622987,\\n          0.15281568627450998\\n        ],\\n        \\\"stds\\\": [\\n          0.00311317121105672,\\n          0.007885665398470972,\\n          0.008240969667318977,\\n          0.019615421748166623,\\n          0.028676831314892466,\\n          0.033095946085946286,\\n          0.3590890901162581\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.664,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 4.503225326538086,\\n        \\\"std\\\": 4.8421173095703125\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.04458787875675457,\\n        \\\"std\\\": 0.0648704634241749,\\n        \\\"t_stat\\\": 15.353948651915177,\\n        \\\"p_value\\\": 7.46250518536467e-44,\\n        \\\"cohens_d\\\": 0.6866494581638973\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0017330280210831573,\\n          0.005302538340663201,\\n          0.007163902512666055,\\n          0.020680235506992665,\\n          0.03485707990039093,\\n          0.03459241025841939,\\n          0.3118901960784321\\n        ],\\n        \\\"stds\\\": [\\n          0.0037620949894889076,\\n          0.00825352063013232,\\n          0.007593216730760563,\\n          0.020277157204501794,\\n          0.03162330967091224,\\n          0.038133676245909076,\\n          0.4570695648337024\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.7094285714285714,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 5.153635501861572,\\n        \\\"std\\\": 5.071208477020264\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"push_the_plate_to_the_front_of_the_stove\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.04681500022487693,\\n        \\\"std\\\": 0.06645561015488266,\\n        \\\"t_stat\\\": 15.736337189550586,\\n        \\\"p_value\\\": 1.3382496765371354e-45,\\n        \\\"cohens_d\\\": 0.7037503934432828\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.002803980288112861,\\n          0.0054708934473395275,\\n          0.007187286787515175,\\n          0.018410671617669166,\\n          0.02898102668941719,\\n          0.02812265279046228,\\n          0.3252549019607852\\n        ],\\n        \\\"stds\\\": [\\n          0.0057296098847649055,\\n          0.007560437193942133,\\n          0.007359340564353495,\\n          0.018759688881726206,\\n          0.028137334353327288,\\n          0.02949191003799571,\\n          0.46658065445606245\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.7385714285714285,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 5.972511291503906,\\n        \\\"std\\\": 5.5687432289123535\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"put_the_bowl_on_the_plate\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.04585327669100103,\\n        \\\"std\\\": 0.06512121324514131,\\n        \\\"t_stat\\\": 15.728893275695137,\\n        \\\"p_value\\\": 1.4476730761513222e-45,\\n        \\\"cohens_d\\\": 0.7034174914950824\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0016636890063005333,\\n          0.0052034678355805915,\\n          0.00747777144619647,\\n          0.020320068361922777,\\n          0.028729157559535055,\\n          0.035562712698805565,\\n          0.3252549019607849\\n        ],\\n        \\\"stds\\\": [\\n          0.00306018861719437,\\n          0.008431160867942903,\\n          0.008048276555242978,\\n          0.021654913911754142,\\n          0.026055373152750017,\\n          0.03568682198764817,\\n          0.4582868723436793\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.7365714285714285,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 4.935613632202148,\\n        \\\"std\\\": 4.755918502807617\\n      },\\n      \\\"n_samples\\\": 500\\n    },\\n    \\\"put_the_bowl_on_the_stove\\\": {\\n      \\\"paired_mse\\\": {\\n        \\\"mean\\\": 0.048542862210683366,\\n        \\\"std\\\": 0.06656781244085376,\\n        \\\"t_stat\\\": 16.28963552846279,\\n        \\\"p_value\\\": 3.759600472033675e-48,\\n        \\\"cohens_d\\\": 0.7284946473958375\\n      },\\n      \\\"per_dim_shift\\\": {\\n        \\\"means\\\": [\\n          0.0018493386265249795,\\n          0.00610222509737575,\\n          0.009948190171367981,\\n          0.024407071426545815,\\n          0.030753488704492044,\\n          0.04087197555367618,\\n          0.338368627450981\\n        ],\\n        \\\"stds\\\": [\\n          0.003264664633536739,\\n          0.0077321877439992396,\\n          0.010677892843435068,\\n          0.024496624444718028,\\n          0.027718819464147733,\\n          0.048263969493824666,\\n          0.46698264708631304\\n        ]\\n      },\\n      \\\"token_divergence_rate\\\": 0.7665714285714286,\\n      \\\"kl_divergence\\\": {\\n        \\\"mean\\\": 4.831889629364014,\\n        \\\"std\\\": 4.366452693939209\\n      },\\n      \\\"n_samples\\\": 500\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.19}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T10:59:58.629Z_

<details><summary>↩ Tool result · `toolu_01GhrFGMjX94nXDZAtoAcuug`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"  [3500 passes, 521s, 6.7 pass/s, ETA 223s]\\n  [3600 passes, 535s, 6.7 pass/s, ETA 208s]\\n  [3700 passes, 550s, 6.7 pass/s, ETA 193s]\\n  [3800 passes, 565s, 6.7 pass/s, ETA 178s]\\n  [3900 passes, 580s, 6.7 pass/s, ETA 163s]\\n  [4000 passes, 594s, 6.7 pass/s, ETA 149s]\\n  >> paired_mse=0.045853, token_div=0.7366, kl=4.9356\\n\\n============================================================\\nTask 4: put_the_bowl_on_the_stove\\n  Instruction: put the bowl on the stove\\n  [4100 passes, 609s, 6.7 pass/s, ETA 134s]\\n  [4200 passes, 624s, 6.7 pass/s, ETA 119s]\\n  [4300 passes, 639s, 6.7 pass/s, ETA 104s]\\n  [4400 passes, 654s, 6.7 pass/s, ETA 89s]\\n  [4500 passes, 669s, 6.7 pass/s, ETA 74s]\\n  [4600 passes, 685s, 6.7 pass/s, ETA 60s]\\n  [4700 passes, 700s, 6.7 pass/s, ETA 45s]\\n  [4800 passes, 715s, 6.7 pass/s, ETA 30s]\\n  [4900 passes, 731s, 6.7 pass/s, ETA 15s]\\n  [5000 passes, 746s, 6.7 pass/s, ETA 0s]\\n  >> paired_mse=0.048543, token_div=0.7666, kl=4.8319\\n\\n============================================================\\nDone. 5000 forward passes in 746s\\nPaired MSE: 0.041645 (p=3.99e-194, d=0.651)\\nToken divergence: 0.7230\\nKL divergence: 5.0794\\nMSE vs GT - baseline: 0.431764, ablated: 0.435741\\nResults saved to /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b17ca778-4bc0-4bf9-afb1-5b60fdee0a3b",
  "uuid": "57f135d4-53d8-4d01-9b4d-2bdb9f776976",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"  [3500 passes, 521s, 6.7 pass/s, ETA 223s]\\\\n  [3600 passes, 535s, 6.7 pass/s, ETA 208s]\\\\n  [3700 passes, 550s, 6.7 pass/s, ETA 193s]\\\\n  [3800 passes, 565s, 6.7 pass/s, ETA 178s]\\\\n  [3900 passes, 580s, 6.7 pass/s, ETA 163s]\\\\n  [4000 passes, 594s, 6.7 pass/s, ETA 149s]\\\\n  >> paired_mse=0.045853, token_div=0.7366, kl=4.9356\\\\n\\\\n============================================================\\\\nTask 4: put_the_bowl_on_the_stove\\\\n  Instruction: put the bowl on the stove\\\\n  [4100 passes, 609s, 6.7 pass/s, ETA 134s]\\\\n  [4200 passes, 624s, 6.7 pass/s, ETA 119s]\\\\n  [4300 passes, 639s, 6.7 pass/s, ETA 104s]\\\\n  [4400 passes, 654s, 6.7 pass/s, ETA 89s]\\\\n  [4500 passes, 669s, 6.7 pass/s, ETA 74s]\\\\n  [4600 passes, 685s, 6.7 pass/s, ETA 60s]\\\\n  [4700 passes, 700s, 6.7 pass/s, ETA 45s]\\\\n  [4800 passes, 715s, 6.7 pass/s, ETA 30s]\\\\n  [4900 passes, 731s, 6.7 pass/s, ETA 15s]\\\\n  [5000 passes, 746s, 6.7 pass/s, ETA 0s]\\\\n  >> paired_mse=0.048543, token_div=0.7666, kl=4.8319\\\\n\\\\n============================================================\\\\nDone. 5000 forward passes in 746s\\\\nPaired MSE: 0.041645 (p=3.99e-194, d=0.651)\\\\nToken divergence: 0.7230\\\\nKL divergence: 5.0794\\\\nMSE vs GT - baseline: 0.431764, ablated: 0.435741\\\\nResults saved to /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"  [3500 passes, 521s, 6.7 pass/s, ETA 223s]\\n  [3600 passes, 535s, 6.7 pass/s, ETA 208s]\\n  [3700 passes, 550s, 6.7 pass/s, ETA 193s]\\n  [3800 passes, 565s, 6.7 pass/s, ETA 178s]\\n  [3900 passes, 580s, 6.7 pass/s, ETA 163s]\\n  [4000 passes, 594s, 6.7 pass/s, ETA 149s]\\n  >> paired_mse=0.045853, token_div=0.7366, kl=4.9356\\n\\n============================================================\\nTask 4: put_the_bowl_on_the_stove\\n  Instruction: put the bowl on the stove\\n  [4100 passes, 609s, 6.7 pass/s, ETA 134s]\\n  [4200 passes, 624s, 6.7 pass/s, ETA 119s]\\n  [4300 passes, 639s, 6.7 pass/s, ETA 104s]\\n  [4400 passes, 654s, 6.7 pass/s, ETA 89s]\\n  [4500 passes, 669s, 6.7 pass/s, ETA 74s]\\n  [4600 passes, 685s, 6.7 pass/s, ETA 60s]\\n  [4700 passes, 700s, 6.7 pass/s, ETA 45s]\\n  [4800 passes, 715s, 6.7 pass/s, ETA 30s]\\n  [4900 passes, 731s, 6.7 pass/s, ETA 15s]\\n  [5000 passes, 746s, 6.7 pass/s, ETA 0s]\\n  >> paired_mse=0.048543, token_div=0.7666, kl=4.8319\\n\\n============================================================\\nDone. 5000 forward passes in 746s\\nPaired MSE: 0.041645 (p=3.99e-194, d=0.651)\\nToken divergence: 0.7230\\nKL divergence: 5.0794\\nMSE vs GT - baseline: 0.431764, ablated: 0.435741\\nResults saved to /root/autodl-tmp/vla-ssd/results/action_trajectory_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

实验已完成。完整 JSON 结果：

```json
{
  "config": {
    "n_tasks": 5,
    "n_demos_per_task": 10,
    "n_timesteps_per_demo": 50,
    "total_forward_passes": 5000,
    "model": "openvla-7b",
    "ablation": "L1_dominant_24_heads_zeroed",
    "ablated_heads": [0,1,2,4,7,8,10,11,12,14,15,16,17,18,19,20,22,23,25,26,27,29,30,31],
    "unnorm_key": "bridge_orig"
  },
  "main_metrics": {
    "paired_action_mse": {
      "mean": 0.04164548042967141,
      "std": 0.06394581517413622,
      "t_stat": 32.55658746950337,
      "p_value": 3.9875267301509806e-194,
      "cohens_d": 0.6511317493798869
    },
    "per_dim_action_shift": {
      "means": [0.0018907631, 0.0053060349, 0.0076212989, 0.0205921095, 0.0307135648, 0.0338819297, 0.2907168627],
      "stds":  [0.0039457747, 0.0079967289, 0.0085559840, 0.0211583055, 0.0285854749, 0.0377378606, 0.4489490408],
      "dim_names": ["dx", "dy", "dz", "rx", "ry", "rz", "gripper"]
    },
    "token_divergence_rate": 0.7230285714285715
  },
  "secondary_metrics": {
    "kl_divergence": {
      "mean": 5.07937479019165,
      "std": 4.961368560791016,
      "per_token_position": [0.2902, 3.0104, 5.9492, 7.4210, 8.9605, 8.4797, 1.4447]
    },
    "mse_vs_gt_baseline": {
      "mean": 0.43176415822445635,
      "std": 0.22077793994025996,
      "note": "OOD, secondary"
    },
    "mse_vs_gt_ablated": {
      "mean": 0.4357406635106642,
      "std": 0.2235285616028443,
      "note": "OOD, secondary"
    },
    "wilcoxon_p": 0.0
  },
  "per_task": {
    "open_the_middle_drawer_of_the_cabinet": {
      "paired_mse": {"mean": 0.02242838, "std": 0.05175720, "t_stat": 9.6800, "p_value": 2.00e-20, "cohens_d": 0.4329},
      "per_dim_shift": {
        "means": [0.001404, 0.004451, 0.006329, 0.019143, 0.030247, 0.030260, 0.152816],
        "stds":  [0.003113, 0.007886, 0.008241, 0.019615, 0.028677, 0.033096, 0.359089]
      },
      "token_divergence_rate": 0.664,
      "kl_divergence": {"mean": 4.5032, "std": 4.8421},
      "n_samples": 500
    },
    "open_the_top_drawer_and_put_the_bowl_inside": {
      "paired_mse": {"mean": 0.04458788, "std": 0.06487046, "t_stat": 15.3539, "p_value": 7.46e-44, "cohens_d": 0.6866},
      "per_dim_shift": {
        "means": [0.001733, 0.005303, 0.007164, 0.020680, 0.034857, 0.034592, 0.311890],
        "stds":  [0.003762, 0.008254, 0.007593, 0.020277, 0.031623, 0.038134, 0.457070]
      },
      "token_divergence_rate": 0.7094,
      "kl_divergence": {"mean": 5.1536, "std": 5.0712},
      "n_samples": 500
    },
    "push_the_plate_to_the_front_of_the_stove": {
      "paired_mse": {"mean": 0.04681500, "std": 0.06645561, "t_stat": 15.7363, "p_value": 1.34e-45, "cohens_d": 0.7038},
      "per_dim_shift": {
        "means": [0.002804, 0.005471, 0.007187, 0.018411, 0.028981, 0.028123, 0.325255],
        "stds":  [0.005730, 0.007560, 0.007359, 0.018760, 0.028137, 0.029492, 0.466581]
      },
      "token_divergence_rate": 0.7386,
      "kl_divergence": {"mean": 5.9725, "std": 5.5687},
      "n_samples": 500
    },
    "put_the_bowl_on_the_plate": {
      "paired_mse": {"mean": 0.04585328, "std": 0.06512121, "t_stat": 15.7289, "p_value": 1.45e-45, "cohens_d": 0.7034},
      "per_dim_shift": {
        "means": [0.001664, 0.005203, 0.007478, 0.020320, 0.028729, 0.035563, 0.325255],
        "stds":  [0.003060, 0.008431, 0.008048, 0.021655, 0.026055, 0.035687, 0.458287]
      },
      "token_divergence_rate": 0.7366,
      "kl_divergence": {"mean": 4.9356, "std": 4.7559},
      "n_samples": 500
    },
    "put_the_bowl_on_the_stove": {
      "paired_mse": {"mean": 0.04854286, "std": 0.06656781, "t_stat": 16.2896, "p_value": 3.76e-48, "cohens_d": 0.7285},
      "per_dim_shift": {
        "means": [0.001849, 0.006102, 0.009948, 0.024407, 0.030753, 0.040872, 0.338369],
        "stds":  [0.003265, 0.007732, 0.010678, 0.024497, 0.027719, 0.048264, 0.466983]
      },
      "token_divergence_rate": 0.7666,
      "kl_divergence": {"mean": 4.8319, "std": 4.3665},
      "n_samples": 500
    }
  }
}
```

日志确认 5000 次前向传播全部完成（746s），汇总指标：
- **Paired MSE**: 0.0416 (p=3.99e-194, Cohen's d=0.651)
- **Token divergence rate**: 72.3%
- **KL divergence**: 5.079
- **MSE vs GT**: baseline 0.4318 vs ablated 0.4357（差异极小）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b17ca778-4bc0-4bf9-afb1-5b60fdee0a3b",
  "uuid": "f3077b7d-22b3-4fd1-84a2-c5e9f38e46c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WKTwD5t1CFrbhUhHJxzAV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4561,
      "cache_read_input_tokens": 24522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4561
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

_source line 11_

实验已完成。完整 JSON 结果：

```json
{
  "config": {
    "n_tasks": 5,
    "n_demos_per_task": 10,
    "n_timesteps_per_demo": 50,
    "total_forward_passes": 5000,
    "model": "openvla-7b",
    "ablation": "L1_dominant_24_heads_zeroed",
    "ablated_heads": [0,1,2,4,7,8,10,11,12,14,15,16,17,18,19,20,22,23,25,26,27,29,30,31],
    "unnorm_key": "bridge_orig"
  },
  "main_metrics": {
    "paired_action_mse": {
      "mean": 0.04164548042967141,
      "std": 0.06394581517413622,
      "t_stat": 32.55658746950337,
      "p_value": 3.9875267301509806e-194,
      "cohens_d": 0.6511317493798869
    },
    "per_dim_action_shift": {
      "means": [0.0018907631, 0.0053060349, 0.0076212989, 0.0205921095, 0.0307135648, 0.0338819297, 0.2907168627],
      "stds":  [0.0039457747, 0.0079967289, 0.0085559840, 0.0211583055, 0.0285854749, 0.0377378606, 0.4489490408],
      "dim_names": ["dx", "dy", "dz", "rx", "ry", "rz", "gripper"]
    },
    "token_divergence_rate": 0.7230285714285715
  },
  "secondary_metrics": {
    "kl_divergence": {
      "mean": 5.07937479019165,
      "std": 4.961368560791016,
      "per_token_position": [0.2902, 3.0104, 5.9492, 7.4210, 8.9605, 8.4797, 1.4447]
    },
    "mse_vs_gt_baseline": {
      "mean": 0.43176415822445635,
      "std": 0.22077793994025996,
      "note": "OOD, secondary"
    },
    "mse_vs_gt_ablated": {
      "mean": 0.4357406635106642,
      "std": 0.2235285616028443,
      "note": "OOD, secondary"
    },
    "wilcoxon_p": 0.0
  },
  "per_task": {
    "open_the_middle_drawer_of_the_cabinet": {
      "paired_mse": {"mean": 0.02242838, "std": 0.05175720, "t_stat": 9.6800, "p_value": 2.00e-20, "cohens_d": 0.4329},
      "per_dim_shift": {
        "means": [0.001404, 0.004451, 0.006329, 0.019143, 0.030247, 0.030260, 0.152816],
        "stds":  [0.003113, 0.007886, 0.008241, 0.019615, 0.028677, 0.033096, 0.359089]
      },
      "token_divergence_rate": 0.664,
      "kl_divergence": {"mean": 4.5032, "std": 4.8421},
      "n_samples": 500
    },
    "open_the_top_drawer_and_put_the_bowl_inside": {
      "paired_mse": {"mean": 0.04458788, "std": 0.06487046, "t_stat": 15.3539, "p_value": 7.46e-44, "cohens_d": 0.6866},
      "per_dim_shift": {
        "means": [0.001733, 0.005303, 0.007164, 0.020680, 0.034857, 0.034592, 0.311890],
        "stds":  [0.003762, 0.008254, 0.007593, 0.020277, 0.031623, 0.038134, 0.457070]
      },
      "token_divergence_rate": 0.7094,
      "kl_divergence": {"mean": 5.1536, "std": 5.0712},
      "n_samples": 500
    },
    "push_the_plate_to_the_front_of_the_stove": {
      "paired_mse": {"mean": 0.04681500, "std": 0.06645561, "t_stat": 15.7363, "p_value": 1.34e-45, "cohens_d": 0.7038},
      "per_dim_shift": {
        "means": [0.002804, 0.005471, 0.007187, 0.018411, 0.028981, 0.028123, 0.325255],
        "stds":  [0.005730, 0.007560, 0.007359, 0.018760, 0.028137, 0.029492, 0.466581]
      },
      "token_divergence_rate": 0.7386,
      "kl_divergence": {"mean": 5.9725, "std": 5.5687},
      "n_samples": 500
    },
    "put_the_bowl_on_the_plate": {
      "paired_mse": {"mean": 0.04585328, "std": 0.06512121, "t_stat": 15.7289, "p_value": 1.45e-45, "cohens_d": 0.7034},
      "per_dim_shift": {
        "means": [0.001664, 0.005203, 0.007478, 0.020320, 0.028729, 0.035563, 0.325255],
        "stds":  [0.003060, 0.008431, 0.008048, 0.021655, 0.026055, 0.035687, 0.458287]
      },
      "token_divergence_rate": 0.7366,
      "kl_divergence": {"mean": 4.9356, "std": 4.7559},
      "n_samples": 500
    },
    "put_the_bowl_on_the_stove": {
      "paired_mse": {"mean": 0.04854286, "std": 0.06656781, "t_stat": 16.2896, "p_value": 3.76e-48, "cohens_d": 0.7285},
      "per_dim_shift": {
        "means": [0.001849, 0.006102, 0.009948, 0.024407, 0.030753, 0.040872, 0.338369],
        "stds":  [0.003265, 0.007732, 0.010678, 0.024497, 0.027719, 0.048264, 0.466983]
      },
      "token_divergence_rate": 0.7666,
      "kl_divergence": {"mean": 4.8319, "std": 4.3665},
      "n_samples": 500
    }
  }
}
```

日志确认 5000 次前向传播全部完成（746s），汇总指标：
- **Paired MSE**: 0.0416 (p=3.99e-194, Cohen's d=0.651)
- **Token divergence rate**: 72.3%
- **KL divergence**: 5.079
- **MSE vs GT**: baseline 0.4318 vs ablated 0.4357（差异极小）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 36295,
  "duration_api_ms": 36064,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "b17ca778-4bc0-4bf9-afb1-5b60fdee0a3b",
  "total_cost_usd": 0.19825349999999997,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 17242,
    "cache_read_input_tokens": 60458,
    "output_tokens": 2372,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 17242,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2081,
        "cache_read_input_tokens": 24522,
        "cache_creation_input_tokens": 4561,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4561
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 862,
      "outputTokens": 13,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.000927,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 2372,
      "cacheReadInputTokens": 60458,
      "cacheCreationInputTokens": 17242,
      "webSearchRequests": 0,
      "costUSD": 0.1973265,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "de215776-619e-457a-a172-17794d4856dc"
}
```

</details>

---
