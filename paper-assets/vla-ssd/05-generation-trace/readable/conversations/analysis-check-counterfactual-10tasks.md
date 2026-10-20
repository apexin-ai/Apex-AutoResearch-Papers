# analysis check counterfactual 10tasks

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_check_counterfactual_10tasks_20260520T195619.jsonl`
- **Structured JSON:** [`80a45be0dd4e26b94860.json`](../../sessions/80/80a45be0dd4e26b94860.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-20T19:57:11.738907+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T19:57:11.739373+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T19:57:11.739612+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/ 2>/dev/null; echo \"---PROC---\"; ps aux | grep counterfactual; echo \"---TMUX---\"; tmux ls 2>/dev/null; echo \"---LOGS---\"; ls -la /root/autodl-tmp/vla-ssd/logs/ 2>/dev/null | grep counterfactual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/ 2>/dev/null; echo \"---PROC---\"; ps aux | grep counterfactual; echo \"---TMUX---\"; tmux ls 2>/dev/null; echo \"---LOGS---\"; ls -la /root/autodl-tmp/vla-ssd/logs/ 2>/dev/null | grep counterfactual"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T19:57:11.739825+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T19:57:11.740089+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ls -la /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ls -la /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T19:57:11.740284+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "ps aux | grep counterfactual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "ps aux | grep counterfactual"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T19:57:11.740466+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tmux ls"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tmux ls"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T19:57:11.740657+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 196\\ndrwxr-xr-x  2 root root  4096 May 21 03:47 .\\ndrwxr-xr-x 46 root root  8192 May 21 03:07 ..\\n-rw-r--r--  1 root root 92338 May 21 03:47 counterfactual_10tasks_combined.json\\n-rw-r--r--  1 root root  6362 May 21 03:47 counterfactual_correct.json\\n-rw-r--r--  1 root root 17682 May 21 03:47 counterfactual_empty.json\\n-rw-r--r--  1 root root 18087 May 21 03:47 counterfactual_paraphrased.json\\n-rw-r--r--  1 root root 18009 May 21 03:47 counterfactual_shuffled.json\\n-rw-r--r--  1 root root 18010 May 21 03:47 counterfactual_wrong.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.15}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T19:57:11.740851+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T19:57:11.741056+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T19:57:11.741251+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "find /root/autodl-tmp/vla-ssd/logs/ -name \"*counterfactual*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "find /root/autodl-tmp/vla-ssd/logs/ -name \"*counterfactual*\""
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T19:57:11.741455+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T19:57:11.741692+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_correct.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_correct.json"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T19:57:11.741878+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -200 /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_combined.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -200 /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_combined.json"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T19:57:11.742256+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"condition\\\": \\\"correct\\\",\\n    \\\"n_tasks\\\": 10,\\n    \\\"n_demos_per_task\\\": 10,\\n    \\\"n_timesteps_per_demo\\\": 50,\\n    \\\"model\\\": \\\"openvla-7b\\\",\\n    \\\"unnorm_key\\\": \\\"bridge_orig\\\",\\n    \\\"seed\\\": 42\\n  },\\n  \\\"global\\\": {\\n    \\\"n_samples\\\": 5000,\\n    \\\"action_mean\\\": [\\n      -0.0010966845900479678,\\n      -0.002679368670198183,\\n      0.0047844006140688065,\\n      -0.0020650087210289506,\\n      -0.011563276064081779,\\n      -0.012406959752565833,\\n      0.6034290196078443\\n    ],\\n    \\\"action_std\\\": [\\n      0.005888407291554524,\\n      0.009824169564563475,\\n      0.009978558395473621,\\n      0.02223919174902263,\\n      0.03168217197441766,\\n      0.038821909118438115,\\n      0.48463910042894953\\n    ],\\n    \\\"dim_names\\\": [\\n      \\\"dx\\\",\\n      \\\"dy\\\",\\n      \\\"dz\\\",\\n      \\\"rx\\\",\\n      \\\"ry\\\",\\n      \\\"rz\\\",\\n      \\\"gripper\\\"\\n    ]\\n  },\\n  \\\"per_task\\\": {\\n    \\\"open_the_middle_drawer_of_the_cabinet\\\": {\\n      \\\"n_samples\\\": 500,\\n      \\\"action_mean\\\": [\\n        -0.0019176585250742474,\\n        -0.004096853916448747,\\n        0.006604112917772091,\\n        -0.009587521018005004,\\n        -0.00499538658358072,\\n        -0.010530504435127923,\\n        0.8995294117647088\\n      ],\\n      \\\"action_std\\\": [\\n        0.004865942511404777,\\n        0.009310094413900738,\\n        0.009079777398332,\\n        0.021820442267064012,\\n        0.03211705256493082,\\n        0.03321406819384655,\\n        0.29300998220743546\\n      ]\\n    },\\n    \\\"open_the_top_drawer_and_put_the_bowl_inside\\\": {\\n      \\\"n_samples\\\": 500,\\n      \\\"action_mean\\\": [\\n        -0.005377899036968458,\\n        -0.005598451964073357,\\n        0.003440480355962227,\\n        -0.009731843313724505,\\n        -0.019092019
…[truncated 5410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T19:57:11.742665+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"experiment\\\": \\\"counterfactual_instruction_10tasks\\\",\\n    \\\"conditions\\\": [\\n      \\\"wrong\\\",\\n      \\\"empty\\\",\\n      \\\"shuffled\\\",\\n      \\\"paraphrased\\\"\\n    ],\\n    \\\"n_tasks\\\": 10,\\n    \\\"n_demos_per_task\\\": 10,\\n    \\\"n_timesteps_per_demo\\\": 50,\\n    \\\"model\\\": \\\"openvla-7b\\\",\\n    \\\"unnorm_key\\\": \\\"bridge_orig\\\",\\n    \\\"seed\\\": 42,\\n    \\\"task_names\\\": [\\n      \\\"open_the_middle_drawer_of_the_cabinet\\\",\\n      \\\"open_the_top_drawer_and_put_the_bowl_inside\\\",\\n      \\\"push_the_plate_to_the_front_of_the_stove\\\",\\n      \\\"put_the_bowl_on_the_plate\\\",\\n      \\\"put_the_bowl_on_the_stove\\\",\\n      \\\"put_the_bowl_on_top_of_the_cabinet\\\",\\n      \\\"put_the_cream_cheese_in_the_bowl\\\",\\n      \\\"put_the_wine_bottle_on_the_rack\\\",\\n      \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\",\\n      \\\"turn_on_the_stove\\\"\\n    ]\\n  },\\n  \\\"conditions\\\": {\\n    \\\"wrong\\\": {\\n      \\\"global_metrics\\\": {\\n        \\\"paired_mse\\\": {\\n          \\\"mean\\\": 0.06469925227162468,\\n          \\\"std\\\": 0.07003723721073031,\\n          \\\"t_stat\\\": 65.31483348572935,\\n          \\\"p_value\\\": 0.0,\\n          \\\"cohens_d\\\": 0.9236912333834009,\\n          \\\"ci_95\\\": [\\n            0.8959664441611344,\\n            0.9514160226056674\\n          ]\\n        },\\n        \\\"per_dim_shift\\\": {\\n          \\\"means\\\": [\\n            0.005212683457116499,\\n            0.009701657278115717,\\n            0.010381370871684104,\\n            0.024219580160956013,\\n            0.03510734135497613,\\n            0.03954739989668392,\\n            0.4519435294117663\\n          ],\\n          \\\"stds\\\": [\\n            0.005405998172843991,\\n            0.010095792763667271,\\n            0.009512956661715331,\\n            0.02217933813
…[truncated 5097 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T19:57:11.742956+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -300 /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_combined.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -300 /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_combined.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T19:57:11.743445+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"            ]\\n          },\\n          \\\"per_dim_shift\\\": {\\n            \\\"means\\\": [\\n              0.002683643546328822,\\n              0.007852470687168473,\\n              0.008097194904422046,\\n              0.016717119722766006,\\n              0.03161627444727976,\\n              0.03783857157891407,\\n              0.1401098039215686\\n            ],\\n            \\\"stds\\\": [\\n              0.003758832120941365,\\n              0.009408359468187362,\\n              0.00768621446873719,\\n              0.01647724480006979,\\n              0.027210451866701825,\\n              0.03661349038053608,\\n              0.3328631058378052\\n            ],\\n            \\\"dim_names\\\": [\\n              \\\"dx\\\",\\n              \\\"dy\\\",\\n              \\\"dz\\\",\\n              \\\"rx\\\",\\n              \\\"ry\\\",\\n              \\\"rz\\\",\\n              \\\"gripper\\\"\\n            ]\\n          },\\n          \\\"token_divergence_rate\\\": 0.7765714285714286,\\n          \\\"kl_divergence\\\": {\\n            \\\"mean\\\": 5.632013320922852,\\n            \\\"std\\\": 4.643463134765625,\\n            \\\"per_token_position\\\": [\\n              0.9418880343437195,\\n              4.782595634460449,\\n              7.432372570037842,\\n              7.597500801086426,\\n              9.224662780761719,\\n              8.498820304870605,\\n              0.9462519288063049\\n            ]\\n          },\\n          \\\"wilcoxon_p\\\": 2.682749320494914e-83,\\n          \\\"n_samples\\\": 500,\\n          \\\"instruction_correct\\\": \\\"put the wine bottle on the rack\\\",\\n          \\\"instruction_counterfactual\\\": \\\"set the wine bottle onto the rack\\\"\\n        },\\n        \\\"put_the_wine_bottle_on_top_of_the_cabinet\\\": {\\n          \\\"paired_mse\\\": {\\n            \\\"mean\\\": 0.018300965657979958,\\n            \\\"std\\\": 0.044530959878456296,\\n        
…[truncated 7629 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T19:57:11.743685+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "wc -l /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_combined.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "wc -l /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_combined.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T19:57:11.743878+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"3014 /root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_combined.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T19:57:11.744163+00:00_

实验已完成。以下是 10-task counterfactual 实验汇总：

## 实验配置
- 10 tasks × 10 demos × 50 timesteps = 5000 samples/condition
- 4 counterfactual conditions: wrong, empty, shuffled, paraphrased
- Model: openvla-7b, seed 42

## Global Effect Ranking (by Cohen's d)

| Condition | Cohen's d | Paired MSE | Token Divergence | KL Divergence |
|-----------|-----------|------------|------------------|---------------|
| **empty** | **0.978** | 0.0691 | 91.3% | 8.81 |
| **wrong** | **0.924** | 0.0647 | 90.8% | 8.38 |
| **shuffled** | 0.763 | 0.0512 | 87.1% | 7.33 |
| **paraphrased** | 0.707 | 0.0462 | 83.0% | 6.46 |

## Cross-Task Variance

| Condition | Cohen's d (mean±std) | Range | CV |
|-----------|---------------------|-------|-----|
| empty | 0.989 ± 0.169 | [0.681, 1.245] | 0.171 |
| wrong | 0.949 ± 0.260 | [0.536, 1.505] | 0.274 |
| shuffled | 0.766 ± 0.142 | [0.458, 0.930] | 0.185 |
| paraphrased | 0.713 ± 0.211 | [0.411, 0.959] | 0.296 |

## Paraphrased Condition Per-Task Cohen's d

| Task | Cohen's d |
|------|-----------|
| push_plate_to_stove | 0.959 |
| put_wine_bottle_on_rack | 0.427 |
| put_wine_bottle_on_cabinet | 0.411 |
| open_middle_drawer | 0.444 |
| put_bowl_on_plate | 0.759 |
| put_bowl_on_stove | 0.856 |
| put_bowl_on_cabinet | 0.867 |
| put_cream_cheese_in_bowl | 0.921 |
| open_top_drawer_put_bowl | 0.713 |
| turn_on_stove | 0.778 |

## 关键发现

1. **Effect ordering 与 3-task 一致**: empty > wrong > shuffled > paraphrased
2. **所有 condition 全部显著** (p ≈ 0, 所有 Cohen's d > 0.7)
3. **Paraphrased condition 的 cross-task variance 最大** (CV=0.296)，说明语义敏感度因 task 而异——有些 task 对措辞改变几乎不敏感 (d≈0.41)，有些非常敏感 (d≈0.96)
4. **empty 最稳定** (CV=0.171)，符合预期——移除指令的效果不依赖具体 task 语义

结果文件路径：`/root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_combined.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_check_counterfactual_10tasks_20260520T195619"
}
```

</details>

---
