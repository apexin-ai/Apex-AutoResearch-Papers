# fix success summary nmin section

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_fix_success_summary_nmin_section_20260515T153705.log`
- **Structured JSON:** [`46cb62c9d694937f7565.json`](../../sessions/46/46cb62c9d694937f7565.json)

## Before a recorded user message

54 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training",
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "504ad5e3-883f-42d2-83fc-bd0d4bcf32ce",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/memory/"
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
    "resetsAt": 1778863200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "71288fa4-dc73-441a-bb69-c391bf12c6f1",
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current summary file and fetching precise data from the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "4c49b56c-7dfe-41d8-9f89-d6e7f6488486",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CWV4yTh1EDps9CQNkXhLKu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12539,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12539
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KtzYo6c64C6PhQvHuVN8Mx`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "66ae3ddc-bacd-41ef-81e9-6d5537d0341b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CWV4yTh1EDps9CQNkXhLKu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12539,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12539
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

_source line 6 · 2026-05-15T15:37:20.766Z_

<details><summary>↩ Tool result · `toolu_01KtzYo6c64C6PhQvHuVN8Mx`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "78d589f1-9b59-4b22-8b3e-5987253e9627",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read the current summary file and fetch registry data in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "9860acf5-6160-4f7a-aaea-d033d2fe9bc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01492H8F6tzn94DVqYj38Daw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 23986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 801
      },
      "output_tokens": 46,
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01R9Ne9k5UH4m19E5Ubgi1wR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "ae2363e8-5114-4ab0-a478-35dcca44ffb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01492H8F6tzn94DVqYj38Daw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 23986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 801
      },
      "output_tokens": 46,
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

_source line 9 · 2026-05-15T15:37:24.581Z_

<details><summary>↩ Tool result · `toolu_01R9Ne9k5UH4m19E5Ubgi1wR`</summary>

```text
1	# All Successful Experiments Summary
2	
3	> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure
4	
5	---
6	
7	## Grid-b Experiments
8	
9	Fixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.
10	
11	| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |
12	|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|
13	| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |
14	| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |
15	| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |
16	| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |
17	| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |
18	| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |
19	| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |
20	| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |
21	| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |
22	| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |
23	| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |
24	| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |
25	| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |
26	| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |
27	| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |
28	| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |
29	| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |
30	| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |
31	
32	> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。
33	> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。
34	
35	---
36	
37	## Adaptive Experiments
38	
39	Per-batch adaptive b* via α_eff theory. Sorted by PPL ascending.
40	
41	| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |
42	|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|
43	| adaptive_seed123 | original | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |
44	| adaptive_seed456 | original | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |
45	| adaptive_fix_seed123 | n_min fix | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |
46	| adaptive_fix_seed42 | n_min fix | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |
47	| adaptive_fix_seed456 | n_min fix | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |
48	| adaptive_seed42 | original | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |
49	
50	> "original" = n_min=3 bug (batch_size-1)。"n_min fix" = D012 修复后 n_min=max(2, batch_size//2)。
51	> original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。
52	> adaptive_fix b* 分布：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。
53	
54	---
55	
56	## Ablation Experiments
57	
58	Single-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.
59	
60	| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |
61	|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|
62	| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |
63	| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |
64	| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |
65	
66	> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。
67	> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。
68	> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。
69	
70	---
71	
72	## Baseline Experiments
73	
74	Uniform weighting (no provenance information). Sorted by PPL ascending.
75	
76	| exp_id | seed | PPL | eval_loss | gpu_hours |
77	|--------|------|-----|-----------|-----------|
78	| uniform_seed42 | 42 | 17.690 | - | 3.43 |
79	| uniform_seed123 | 123 | 17.690 | - | 3.43 |
80	| uniform_seed456 | 456 | 17.700 | - | 3.43 |
81	
82	---
83	
84	## Infrastructure Experiments (non-training)
85	
86	| exp_id | 类型 | 关键指标 |
87	|--------|------|---------|
88	| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |
89	| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |
90	
91	---
92	
93	## Key Findings
94	
95	1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。
96	
97	2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。
98	
99	3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。
100	
101	4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。
102	
103	5. **Golden ratio oracle (PPL=17.654) 确认 adaptive 接近最优。** 使用真实标签的 oracle 仅略优于 adaptive_fix (17.650)，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。
104	
105	---
106	
107	## PPL Ratio Reference
108	
109	| 方法 | seed42 | seed123 | seed456 | mean |
110	|------|--------|---------|---------|------|
111	| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
112	| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |
113	| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |
114	| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |
115	| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |
116	| golden_ratio oracle | 0.9980 | - | - | - |
117	| ess_only | 1.0023 | - | - | - |
118	| nmin1 | 1.0056 | - | - | - |
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "2bfe89c4-f0d0-44b2-8547-1ba7e55523e9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
      "content": "# All Successful Experiments Summary\n\n> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure\n\n---\n\n## Grid-b Experiments\n\nFixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.\n\n| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|\n| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |\n| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |\n| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |\n| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |\n| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |\n| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |\n| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |\n| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |\n| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |\n| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |\n| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |\n| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |\n| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |\n| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |\n| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |\n| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |\n| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |\n| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |\n\n> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。\n> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。\n\n---\n\n## Adaptive Experiments\n\nPer-batch adaptive b* via α_eff theory. Sorted by PPL ascending.\n\n| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|\n| adaptive_seed123 | original | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |\n| adaptive_seed456 | original | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |\n| adaptive_fix_seed123 | n_min fix | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |\n| adaptive_fix_seed42 | n_min fix | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |\n| adaptive_fix_seed456 | n_min fix | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |\n| adaptive_seed42 | original | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |\n\n> \"original\" = n_min=3 bug (batch_size-1)。\"n_min fix\" = D012 修复后 n_min=max(2, batch_size//2)。\n> original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。\n> adaptive_fix b* 分布：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。\n\n---\n\n## Ablation Experiments\n\nSingle-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.\n\n| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |\n|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|\n| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |\n| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |\n| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |\n\n> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。\n> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。\n> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。\n\n---\n\n## Baseline Experiments\n\nUniform weighting (no provenance information). Sorted by PPL ascending.\n\n| exp_id | seed | PPL | eval_loss | gpu_hours |\n|--------|------|-----|-----------|-----------|\n| uniform_seed42 | 42 | 17.690 | - | 3.43 |\n| uniform_seed123 | 123 | 17.690 | - | 3.43 |\n| uniform_seed456 | 456 | 17.700 | - | 3.43 |\n\n---\n\n## Infrastructure Experiments (non-training)\n\n| exp_id | 类型 | 关键指标 |\n|--------|------|---------|\n| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |\n| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |\n\n---\n\n## Key Findings\n\n1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。\n\n2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。\n\n3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。\n\n4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。\n\n5. **Golden ratio oracle (PPL=17.654) 确认 adaptive 接近最优。** 使用真实标签的 oracle 仅略优于 adaptive_fix (17.650)，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。\n\n---\n\n## PPL Ratio Reference\n\n| 方法 | seed42 | seed123 | seed456 | mean |\n|------|--------|---------|---------|------|\n| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |\n| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |\n| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |\n| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |\n| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |\n| golden_ratio oracle | 0.9980 | - | - | - |\n| ess_only | 1.0023 | - | - | - |\n| nmin1 | 1.0056 | - | - | - |\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01MDqYuGGaeHDjCd2qNPDRbS`</summary>

```json
{
  "project": "provenance_weight_training",
  "fields": [
    "*"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "082d1838-689e-40da-bb49-49e51887b585",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01492H8F6tzn94DVqYj38Daw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 23986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 801
      },
      "output_tokens": 46,
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

_source line 11 · 2026-05-15T15:37:25.421Z_

<details><summary>↩ Tool result · `toolu_01MDqYuGGaeHDjCd2qNPDRbS`</summary>

```text
Error: result (75,011 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/2a0c2b2e-ded9-41da-a3cc-a87bffb93fea/tool-results/mcp-agent-ml-research-read_registry-1778859445396.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/2a0c2b2e-ded9-41da-a3cc-a87bffb93fea/tool-results/mcp-agent-ml-research-read_registry-1778859445396.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/2a0c2b2e-ded9-41da-a3cc-a87bffb93fea/tool-results/mcp-agent-ml-research-read_registry-1778859445396.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "fea8cc1a-ad0f-44cf-8c7b-17d96685a872",
  "tool_use_result": {
    "content": "Error: result (75,011 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/2a0c2b2e-ded9-41da-a3cc-a87bffb93fea/tool-results/mcp-agent-ml-research-read_registry-1778859445396.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/2a0c2b2e-ded9-41da-a3cc-a87bffb93fea/tool-results/mcp-agent-ml-research-read_registry-1778859445396.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/2a0c2b2e-ded9-41da-a3cc-a87bffb93fea/tool-results/mcp-agent-ml-research-read_registry-1778859445396.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"tau_095_seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:32.419Z\", \"updated_at\": \"2026-05-15T14:58:16.987Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.95 (most strict α_eff threshold), testing upper bound — may over-constrain b* to near-zero. Baseline τ=0.8 PPL=17.65.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_095_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.95 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"215505\", \"log_path\": \"~/runs/provenance_weight_training/tau_095_seed42.log\", \"submitted_at\": \"2026-05-15T14:32:12.920Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training experiment\"}}, \"tau_09_seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:28.658Z\", \"updated_at\": \"2026-05-15T14:58:14.274Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.9 (stricter α_eff threshold), testing if higher quality threshold improves PPL. Baseline τ=0.8 PPL=17.65.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_09_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.9 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"213283\", \"log_path\": \"~/runs/provenance_weight_training/tau_09_seed42.log\", \"submitted_at\": \"2026-05-15T13:59:38.171Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training experiment\"}}, \"tau_05_seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:27.263Z\", \"updated_at\": \"2026-05-15T14:57:33.364Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.5 (most permissive α_eff threshold), testing lower bound of useful τ range. Baseline τ=0.8 PPL=17.65.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_05_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.5 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"205652\", \"log_path\": \"~/runs/provenance_weight_training/tau_05_seed42.log\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"gpu\": \"cuda:1\", \"server\": \"westd-47453\"}, \"nmin4_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:36:45.229Z\", \"updated_at\": \"2026-05-15T14:38:42.341Z\", \"spec\": {\"hypothesis\": \"n_min=4 (=batch_size) boundary case: maximal ESS constraint forces b*→0 on most batches, testing if over-constrained adaptive degrades to near-uniform. Baseline: adaptive_fix n_min=2 PPL=17.650.\", \"parent\": \"adaptive_fix_seed42\", \"planned_gpu\": \"cuda:1\", \"planned_command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin4_seed42 --weighting_method adaptive --n_min 4 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\"}, \"hypothesis\": \"n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=batch_size. Should degrade to uniform-equivalent PPL (~17.69). Key boundary condition for n_min sensitivity analysis.\"}, \"nmin1_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:48:31.298Z\", \"updated_at\": \"2026-05-15T14:36:49.692Z\", \"hypothesis\": \"n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades with overly permissive ESS bound\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T09:34:56.077Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"finished_at\": \"2026-05-15T14:27:21.174Z\", \"training_hours\": 4.87}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"194005\", \"log_path\": \"~/runs/provenance_weight_training/nmin1_seed42.log\", \"submitted_at\": \"2026-05-15T09:36:06.479Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18033.6, \"gpu_hours\": 5.01}, \"pid\": \"194005\", \"log_path\": \"~/runs/provenance_weight_training/nmin1_seed42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:27:22.547409+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.789, \"eval_loss\": 2.8786, \"eval_holdout_tokens\": 4077068, \"b_star_mean\": 7.197, \"b_star_median\": 1.746, \"b_star_std\": 8.374, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.803, \"b_star_p75\": 20, \"b_star_zero_frac\": 0.019, \"b_star_pct_below_0.5\": 13.1, \"b_star_pct_0.5_to_1\": 19.1, \"b_star_pct_1_to_2\": 21.1, \"b_star_pct_above_2\": 46.7, \"b_star_count\": 24412, \"alpha_eff_mean\": 0.714, \"alpha_eff_median\": 0.8}, \"notes\": \"训练完成(EXIT_CODE=0, 4h50m)。PPL=17.789，比 adaptive_fix(n_min=2, 17.650) 差 +0.139，比 uniform(17.690) 差 +0.099。n_min=1 导致极端 b* 分布：46.7% batch b*≥2，p75=20.0(上限)，mean=7.197。ESS 约束几乎失效，over-downweighting 明显。confirms n_min=2 是更优选择。\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/nmin1_seed42\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:36:40.056Z\"}, \"tau_06_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:01:37.442Z\", \"updated_at\": \"2026-05-15T13:57:30.777Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).\", \"parent\": \"adaptive_fix_seed42\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T10:01:53.614Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.6_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.6 --bf16\\\"\", \"finished_at\": \"2026-05-15T13:47:39.608Z\", \"training_hours\": 3.76}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.6_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.6 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"195746\", \"log_path\": \"~/runs/provenance_weight_training/tau_06_seed42.log\", \"submitted_at\": \"2026-05-15T10:01:55.290Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13972.6, \"gpu_hours\": 3.88, \"tau\": 0.6, \"seed\": 42, \"rho\": 0.4, \"model\": \"Qwen3-0.6B\", \"tokens\": \"200M\", \"method\": \"adaptive\", \"parent\": \"adaptive_fix_seed42\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.6_seed42/final\", \"eval_results_path\": \"/root/provenance_weight_training/output/eval/posthoc_eval_tau_06_seed42.json\"}, \"pid\": \"195746\", \"log_path\": \"~/runs/provenance_weight_training/tau_06_seed42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:47:40.932954+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.6805, \"eval_loss\": 2.8725, \"train_loss\": 9.275, \"total_steps\": 6103, \"train_runtime_s\": 13436.64, \"train_samples_per_second\": 7.267, \"b_star_mean\": 0.5899, \"b_star_median\": 0.3746, \"b_star_std\": 1.0693, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.1195, \"b_star_p75\": 0.66, \"b_star_zero_frac\": 0.156, \"b_star_nonzero_mean\": 0.699, \"b_star_nonzero_median\": 0.4473}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/tau_0.6_seed42/final\", \"completed_at\": \"2026-05-15T13:54:47.892Z\", \"notes\": \"PPL=17.681 劣于 τ=0.8 baseline (17.650)，conclusion=negative。概念修正：τ 越低 → α_eff 下界越松 → b* 更小 → 降权力度更弱（非更激进）。正确因果链：τ 越高 → α_eff 下界越严 → min-intervention 需要更大 b* 才能满足约束 → 降权力度更强。\"}, \"ess_only_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:20:13.656Z\", \"updated_at\": \"2026-05-15T13:38:10.040Z\", \"hypothesis\": \"ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — proves min-intervention (adaptive) superior to max-intervention (ESS-only)\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-15T09:13:26.412Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed42 --weighting_method ess_only --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"finished_at\": \"2026-05-15T12:50:22.690Z\", \"training_hours\": 3.62}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/ess_only_seed42 --weighting_method ess_only --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"189240\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed42.log\", \"submitted_at\": \"2026-05-15T09:13:28.595Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 15334.6, \"gpu_hours\": 4.26}, \"pid\": \"189240\", \"log_path\": \"~/runs/provenance_weight_training/ess_only_seed42.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T12:50:24.148259+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_ppl\": 17.73, \"eval_loss\": 2.875, \"b_star_median\": 1.58, \"b_star_mean\": 3.51, \"vs_uniform_ppl_delta\": \"+0.038\", \"vs_adaptive_ppl_delta\": \"+0.08\"}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/ess_only_seed42\", \"completed_at\": \"2026-05-15T13:29:03.148Z\"}, \"tau_07_seed42\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:03:27.838Z\", \"updated_at\": \"2026-05-15T13:37:09.277Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.7 (slightly below baseline), testing if moderate τ reduction improves or degrades PPL. Baseline τ=0.8 PPL=17.65.\", \"parent\": \"adaptive_fix_seed42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/tau_0.7_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.7 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"209824\", \"log_path\": \"~/runs/provenance_weight_training/tau_07_seed42.log\", \"submitted_at\": \"2026-05-15T13:35:52.041Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 200000000, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"N/A - training experiment\"}}, \"golden_ratio_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:20:12.943Z\", \"updated_at\": \"2026-05-15T13:33:31.162Z\", \"hypothesis\": \"Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real — requires known proportion, serves as oracle upper bound for adaptive method\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T09:34:55.278Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"finished_at\": \"2026-05-15T13:21:54.212Z\", \"training_hours\": 3.78}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/golden_ratio_seed42 --weighting_method golden_ratio --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"193921\", \"log_path\": \"~/runs/provenance_weight_training/golden_ratio_seed42.log\", \"submitted_at\": \"2026-05-15T09:36:04.200Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14247.0, \"gpu_hours\": 3.96}, \"pid\": \"193921\", \"log_path\": \"/root/provenance_weight_training/output/models/golden_ratio_seed42/step_metrics.jsonl\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T13:21:55.558374+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.654, \"eval_loss\": 2.871, \"train_loss\": 2.1145, \"train_loss_last500\": 2.109, \"eval_holdout_tokens\": 4077068, \"total_steps\": 6103, \"train_runtime_s\": 13442, \"gpu_hours\": 3.73}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/golden_ratio_seed42/final\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:33:31.162Z\"}, \"tau_0.6_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:58:48.894Z\", \"updated_at\": \"2026-05-15T12:39:47.541Z\", \"hypothesis\": \"τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves or degrades vs τ=0.8 baseline (adaptive_fix PPL=17.65). Key evidence for Claim 3 (τ as robust empirical hyperparameter).\", \"parent\": \"adaptive_fix_seed42\", \"conclusion\": \"killed\", \"notes\": \"废弃: exp_id 含点号不合法，已用 tau_06_seed42 替代\", \"completed_at\": \"2026-05-15T12:39:47.541Z\"}, \"detector_modernbert\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:40:06.106Z\", \"updated_at\": \"2026-05-15T11:46:24.749Z\", \"conclusion\": \"killed\", \"hypothesis\": \"ModernBERT-base can distinguish Qwen3-0.6B synthetic text from FineWeb human text with AUC>=0.95 and ECE<=0.05\", \"notes\": \"Superseded by TF-IDF detector (detector_tfidf_lr). Never ran — cancelled at QUEUED stage.\"}, \"grid_b5_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:59:39.050Z\", \"updated_at\": \"2026-05-15T10:05:51.443Z\", \"hypothesis\": \"Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-15T00:52:41.923Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --eval_data_path data/human/eval_holdout.jsonl --eval_steps 500\\\"\", \"finished_at\": \"2026-05-15T09:31:34.604Z\", \"training_hours\": 8.65}, \"failure_reason\": \"\", \"notes\": \"⚠️ checkpoint resume artifact: PPL=17.993, 比 seed42(17.818)/seed123(17.804) 高 +0.18。训练中断后从 checkpoint-3000 恢复，导致系统性 PPL 偏高。论文 Table 1 中 b=5.0 行仅报 2 seeds (seed42+seed123)。\", \"completed_at\": \"2026-05-15T07:46:15.281Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:46:16.570901+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:31:35.946616+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"方案 A 重跑：无 inline eval，从 checkpoint-3000 恢复（~3100 步剩余）。PID=183240, cuda:2, timeout=5h。训练完后 post-hoc eval。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed456 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b5_0_seed456/checkpoint-3000\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"183240\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed456.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.993, \"eval_loss\": 2.89, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.488, \"total_steps\": 6103, \"train_runtime_s\": 6601, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"output/models/grid_b5_0_seed456/final\", \"conclusion\": \"success\"}, \"grid_b3_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:59:38.011Z\", \"updated_at\": \"2026-05-15T10:05:50.357Z\", \"hypothesis\": \"Grid-b weighting with b=3.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T00:52:41.254Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b3_0_seed456 --weighting_method grid --grid_b_value 3.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --eval_data_path data/human/eval_holdout.jsonl --eval_steps 500\\\"\", \"finished_at\": \"2026-05-15T09:31:37.181Z\", \"training_hours\": 8.65}, \"failure_reason\": \"\", \"notes\": \"⚠️ checkpoint resume artifact: PPL=17.921, 比 seed42(17.774)/seed123(17.76) 高 +0.16。训练中断后从 checkpoint-3000 恢复，导致系统性 PPL 偏高。论文 Table 1 中 b=3.0 行仅报 2 seeds (seed42+seed123)。\", \"completed_at\": \"2026-05-15T07:46:09.092Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:46:12.926805+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:31:39.113223+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"方案 A 重跑：无 inline eval，从 checkpoint-3000 恢复（~3100 步剩余）。PID=183446, cuda:3, timeout=5h。训练完后 post-hoc eval。\"}}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b3_0_seed456 --weighting_method grid --grid_b_value 3.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b3_0_seed456/checkpoint-3000\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"183446\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"log_path\": \"~/runs/provenance_weight_training/grid_b3_0_seed456.log\"}, \"metrics\": {\"eval_ppl_holdout\": 17.921, \"eval_loss\": 2.886, \"eval_holdout_tokens\": 4077068, \"train_loss\": 5.435, \"total_steps\": 6103, \"train_runtime_s\": 6602, \"gpu_hours\": 1.83, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"output/models/grid_b3_0_seed456/final\", \"conclusion\": \"success\"}, \"grid_b2_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:59:37.073Z\", \"updated_at\": \"2026-05-15T10:05:48.101Z\", \"hypothesis\": \"Grid-b weighting with b=2.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T22:22:43.944Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed456 --weighting_method grid --grid_b_value 2.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --eval_data_path data/human/eval_holdout.jsonl --eval_steps 500\\\"\", \"finished_at\": \"2026-05-15T09:15:04.029Z\", \"training_hours\": 10.87}, \"failure_reason\": \"eval overhead timeout at 65.5% (checkpoint-3500 available). Eval dataset 8477 samples × every 500 steps caused ~40min per eval round, exceeding original timeout.\", \"completed_at\": \"2026-05-15T07:31:09.178Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T07:31:10.598336+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:15:05.368569+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"恢复自 checkpoint-3500（原超时于 65.5%）。timeout 增至 6h（原因：eval 8477 条 × 每 500 步 ≈ 40min/轮）。PID=182488, cuda:0。\"}}, \"notes\": \"⚠️ checkpoint resume artifact: PPL=17.989, 比 seed42(17.741)/seed123(17.725) 高 +0.25。训练中断后从 checkpoint-3500 恢复，导致系统性 PPL 偏高。论文 Table 1 中 b=2.0 行仅报 2 seeds (seed42+seed123)。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed456 --weighting_method grid --grid_b_value 2.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --bf16 --resume_from_checkpoint output/models/grid_b2_0_seed456/checkpoint-3500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"183161\", \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed456.log\", \"submitted_at\": \"2026-05-15T07:40:59.398Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6408.6, \"gpu_hours\": 1.78}, \"metrics\": {\"eval_ppl_holdout\": 17.989, \"eval_loss\": 2.8898, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.625, \"total_steps\": 6103, \"train_runtime_s\": 12969, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.53, \"eval_method\": \"eval_perplexity.py (sliding window, stride=1024, max_docs=5000, fp16)\"}, \"checkpoint_path\": \"output/models/grid_b2_0_seed456/final\", \"conclusion\": \"success\"}, \"grid_b_low_seed42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T01:18:54.793Z\", \"updated_at\": \"2026-05-15T09:33:21.503Z\", \"hypothesis\": \"Grid-b extension to b<0.5 (b=0.1/0.2/0.3 serial), seed42, confirming whether grid-best lies at b=0.5 or below\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-15T05:23:13.303Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:02:07.651872+00:00\"}]}, \"spec\": {\"command\": \"bash run_grid_b_low_seed42.sh\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"163662\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_low_seed42.log\", \"submitted_at\": \"2026-05-15T09:20:20Z\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 774.2, \"gpu_hours\": 0.22}, \"notes\": \"cron框架误杀(infrastructure bug)。根因: WANDB_MODE=disabled + tmux wrapper PID 不匹配，reconcile_crons 判定进程死亡并发送 SIGTERM。训练实际曾完成 3 个 b 值(8477/8477×3)，但第二次重启后在 step 431 被杀，所有 checkpoint 目录丢失(grid_b0_1/0_2/0_3_seed42 不存在)。需在 cuda:2/3 释放后完全重跑。\", \"reproduce\": {\"finished_at\": \"2026-05-15T09:02:05.942Z\"}, \"conclusion\": \"failed\"}, \"grid_b1_5_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:59:35.658Z\", \"updated_at\": \"2026-05-15T01:03:24.328Z\", \"spec\": {\"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456}, \"hypothesis\": \"Grid-b weighting with b=1.5, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T21:10:45.479Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_5_seed456 --weighting_method grid --grid_b_value 1.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-15T00:50:58.269Z\", \"training_hours\": 3.67}, \"pid\": \"142985\", \"log_path\": \"~/runs/provenance_weight_training/grid_b1_5_seed456.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:51:00.583331+00:00\"}]}, \"checkpoint_path\": \"output/models/grid_b1_5_seed456/final\", \"metrics\": {\"train_loss\": 10.435, \"total_steps\": 6103, \"train_runtime_s\": 12950.16, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.54, \"eval_loss\": 2.8741, \"eval_ppl_holdout\": 17.71, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.875, \"eval_tokens\": 5004058}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:56:27.189Z\"}, \"grid_b1_0_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:59:34.733Z\", \"updated_at\": \"2026-05-15T01:03:23.307Z\", \"spec\": {\"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456}, \"hypothesis\": \"Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T21:10:44.681Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_0_seed456 --weighting_method grid --grid_b_value 1.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-15T00:50:55.540Z\", \"training_hours\": 3.67}, \"pid\": \"142902\", \"log_path\": \"~/runs/provenance_weight_training/grid_b1_0_seed456.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:50:56.660568+00:00\"}]}, \"checkpoint_path\": \"output/models/grid_b1_0_seed456/final\", \"metrics\": {\"train_loss\": 10.178, \"total_steps\": 6103, \"train_runtime_s\": 12963.87, \"gpu_hours\": 3.67, \"train_samples_per_second\": 7.532, \"eval_loss\": 2.8725, \"eval_ppl_holdout\": 17.68, \"eval_holdout_tokens\": 4077068, \"eval_loss_holdout\": 2.8734, \"eval_tokens\": 5004058}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:56:26.614Z\"}, \"grid_b0_5_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T06:58:17.956Z\", \"updated_at\": \"2026-05-15T01:03:04.640Z\", \"hypothesis\": \"Grid-b weighting with b=0.5, seed=456, for multi-seed validation of best-b baseline\", \"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T21:10:43.728Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed456 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-15T00:57:32.591Z\", \"training_hours\": 3.78}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T21:13:26.329Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:13:27.262433+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:57:33.835977+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: CUDA OOM at step 0 — GPU 0 被 3 个进程挤爆（PID 138525: 68.61GiB + PID 139132: 19.21GiB + 本进程 7.08GiB > 94.97GiB）。实验分配 cuda:1 但进程实际跑在 GPU 0 上，疑 CUDA_VISIBLE_DEVICES 未正确注入或有残留进程干扰。已有成果: 无（0% 进度）。建议: 清理 GPU 0 残留进程后在 cuda:1 上重新提交，补充 --eval_data_path 和 --eval_steps 参数。\"}}, \"notes\": \"重提交成功（retry_count=1）。原 OOM 因 cuda:1 残留 eval 进程。已清理 exit marker，日志重定向正常。step 56/6103, ETA ~3.5h。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed456 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"144400\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed456.log\", \"submitted_at\": \"2026-05-14T21:20:21.115Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"wall_clock_seconds\": 13363.5, \"gpu_hours\": 3.71}, \"pid\": 145062, \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed456.log\", \"metrics\": {\"train_loss\": 9.5622, \"total_steps\": 6103, \"train_runtime_s\": 12953.96, \"gpu_hours\": 3.6, \"train_samples_per_second\": 7.538, \"eval_loss\": 2.8705, \"eval_ppl_holdout\": 17.65, \"eval_holdout_tokens\": 4077068}, \"checkpoint_path\": \"output/models/grid_b0_5_seed456/final\", \"conclusion\": \"success\"}, \"adaptive_fix_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:31.779Z\", \"updated_at\": \"2026-05-15T00:00:33.021Z\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performance (baseline adaptive PPL=17.64, uniform PPL=17.70)\", \"parent\": \"adaptive_seed456\", \"notes\": \"最终清理后重提交。从 checkpoint-1000 恢复，无 inline eval。PID=127285\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_fix_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint output/models/adaptive_fix_seed456/checkpoint-1000\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"127280\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed456.log\", \"submitted_at\": \"2026-05-14T17:47:33.774Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12040.6, \"gpu_hours\": 3.34}, \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"pid\": \"115066\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed456.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --eval_data_path data/human/eval_holdout.jsonl --output_dir output/models/adaptive_fix_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --eval_steps 500 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\", \"finished_at\": \"2026-05-14T21:00:17.106Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:38:47.164099+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T21:00:18.079813+00:00\"}]}, \"metrics\": {\"train_loss\": 8.3124, \"train_runtime\": 11436.05, \"train_samples_per_second\": 8.539, \"train_steps_per_second\": 0.534, \"total_steps\": 6103, \"eval_loss_holdout\": 2.8711, \"eval_ppl_holdout\": 17.66, \"eval_tokens\": 4077068, \"b_star_count\": 26396, \"b_star_mean\": 1.416, \"b_star_median\": 0.88, \"b_star_std\": 1.993, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}, \"checkpoint_path\": \"output/models/adaptive_fix_seed456/final\"}, \"adaptive_fix_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:32:31.409Z\", \"updated_at\": \"2026-05-15T00:00:29.758Z\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performance (baseline adaptive PPL=17.63, uniform PPL=17.69)\", \"parent\": \"adaptive_seed123\", \"notes\": \"最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126944\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python run_clm_weighted.py --weighting_method adaptive --n_min 2 --no_ema --resume_from_checkpoint checkpoint-1500\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"126939\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed123.log\", \"submitted_at\": \"2026-05-14T17:47:28.582Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen3-0.6B\", \"seed\": 123, \"checkpoint_source\": \"checkpoint-1500 (D012 fix)\", \"eval_data\": \"/root/provenance_weight_training/data/human/eval_holdout.jsonl\", \"wall_clock_seconds\": 10807.2, \"gpu_hours\": 3.0}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:41:22.910Z\"}, \"completed_at\": \"\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:38:38.735034+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:41:26.828424+00:00\"}]}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/adaptive_fix_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed123.log\", \"metrics\": {\"eval_ppl_holdout\": 17.643, \"eval_loss\": 2.8704, \"eval_tokens\": 4077068, \"train_loss_weighted\": 7.517, \"train_runtime_s\": 10347, \"total_steps\": 6103, \"epoch\": 0.26, \"b_star_mean\": 1.431, \"b_star_median\": 0.88, \"b_star_std\": 2.029, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_2_to_5\": 6.3, \"b_star_pct_above_5\": 1.9, \"b_star_count\": 25906, \"b_star_p25\": 0.54, \"b_star_p75\": 1.52, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}}, \"adaptive_fix_seed42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T13:32:30.463Z\", \"updated_at\": \"2026-05-15T00:00:25.930Z\", \"hypothesis\": \"D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)\", \"parent\": \"adaptive_seed42\", \"notes\": \"最终清理后重提交。从 checkpoint-1500 恢复，无 inline eval。PID=126801\", \"failure_reason\": \"\", \"completed_at\": \"\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"D012 代码验证通过（n_min=max(2,batch_size//2), 无EMA, import OK）。等 GPU 释放后提交。\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:38:26.312269+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T20:39:45.953045+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_fix_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint output/models/adaptive_fix_seed42/checkpoint-1500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"126796\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed42.log\", \"submitted_at\": \"2026-05-14T17:47:21.683Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12053.2, \"gpu_hours\": 3.35}, \"reproduce\": {\"finished_at\": \"2026-05-14T20:39:44.942Z\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.5167, \"train_runtime\": 10304.37, \"train_samples_per_second\": 9.476, \"train_steps_per_second\": 0.592, \"total_steps\": 6103, \"eval_loss_holdout\": 2.8709, \"eval_ppl_holdout\": 17.65, \"eval_tokens\": 4077068, \"b_star_count\": 26458, \"b_star_mean\": 1.399, \"b_star_median\": 0.871, \"b_star_std\": 1.933, \"b_star_min\": 0, \"b_star_max\": 20, \"b_star_p25\": 0.54, \"b_star_p75\": 1.512, \"b_star_pct_below_0.5\": 20.9, \"b_star_pct_0.5_to_1\": 35.7, \"b_star_pct_1_to_2\": 27.3, \"b_star_pct_above_2\": 16.1, \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"}, \"checkpoint_path\": \"output/models/adaptive_fix_seed42/final\"}, \"grid_b_seed42_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:50:09.001Z\", \"updated_at\": \"2026-05-14T22:21:47.253Z\", \"spec\": {\"command\": \"bash run_grid_b_seed42.sh (6 b values serial: 0.5, 1.0, 1.5, 2.0, 3.0, 5.0)\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:0\"], \"pid\": \"50134\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_seed42_batch.log\", \"submitted_at\": \"2026-05-13T23:50:08.990Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"wall_clock_seconds\": 81098.3, \"gpu_hours\": 22.53}, \"hypothesis\": \"Grid-b weighting with 6 b values (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) for seed=42, establishes best-b baseline for comparison with adaptive b*\", \"metrics\": {\"b_values\": [0.5, 1, 1.5, 2, 3, 5], \"b0_5_train_loss\": 9.598, \"b0_5_completed\": true, \"b1_0_completed\": true, \"b1_5_completed\": true, \"b2_0_current_step\": 5149, \"b2_0_total_steps\": 6103, \"completed_b_values\": [0.5, 1, 1.5, 2, 3], \"current_b\": 5, \"total_steps\": 6103, \"current_step\": 3422, \"b5_0_progress_pct\": 56, \"eta_minutes\": 95, \"b2_0_completed\": true, \"b2_0_train_loss\": 10.621, \"b2_0_train_runtime_s\": 13034, \"b3_0_completed\": true, \"b3_0_train_loss\": 10.754, \"b3_0_train_runtime_s\": 13036, \"all_completed\": true, \"b1_0_train_loss\": 10.223, \"b1_5_train_loss\": 10.485, \"b5_0_train_loss\": 10.858, \"b0_5_runtime_s\": 13036, \"b1_0_runtime_s\": 12968, \"b1_5_runtime_s\": 14789, \"b2_0_runtime_s\": 13034, \"b3_0_runtime_s\": 13036, \"b5_0_runtime_s\": 13115, \"note\": \"eval_ppl missing - no --eval_data_path in batch script, post-hoc eval pending\", \"b0_5_eval_ppl\": 17.651, \"b1_0_eval_ppl\": 17.692, \"b1_5_eval_ppl\": 17.718, \"b2_0_eval_ppl\": 17.741, \"b3_0_eval_ppl\": 17.774, \"b5_0_eval_ppl\": 17.818, \"eval_holdout_tokens\": 4077068, \"best_b\": 0.5, \"best_eval_ppl\": 17.651}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:05:39.706Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:05:40.772794+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/models/grid_b{0.5,1.0,1.5,2.0,3.0,5.0}_seed42/final/\", \"log_path\": \"~/runs/provenance_weight_training/grid_b_seed42_batch.log\", \"completed_at\": \"2026-05-14T22:21:47.253Z\"}, \"grid_b5_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T02:52:56.873Z\", \"updated_at\": \"2026-05-14T15:34:56.261Z\", \"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-47453\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T11:22:30Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed123 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"finished_at\": \"2026-05-14T15:09:25.359Z\", \"training_hours\": 3.78}, \"completed_at\": \"2026-05-14T11:20:36.319Z\", \"notes\": \"PID 94717 已确认存活（SSH 验证 2026-05-14T11:39）。旧 PID 92798 已 kill，cron 重新注册。\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"前次提交 (PID 92793) 未实际启动训练，标记 killed。等 eval PID 92274 完成后重新提交。\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:36:18.619551+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:09:26.285900+00:00\"}]}, \"failure_reason\": \"\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b5_0_seed123 --weighting_method grid --grid_b_value 5.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"94717\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed123.log\"}, \"metrics\": {\"train_loss\": 10.8468, \"total_steps\": 6103, \"train_runtime_s\": 14434, \"gpu_hours\": 4.01, \"eval_ppl_holdout\": 17.8039, \"eval_loss\": 2.8794, \"eval_holdout_tokens\": 4077068}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b5_0_seed123/final/\", \"log_path\": \"~/runs/provenance_weight_training/grid_b5_0_seed123.log\"}, \"grid_b2_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:55.329Z\", \"updated_at\": \"2026-05-14T14:43:39.107Z\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b2_0_seed123 --weighting_method grid --grid_b_value 2.0 --contamination_ratio 0.4 --seed 123\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"88022\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed123.log\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 10.61, \"total_steps\": 6103, \"train_runtime_s\": 13058.8, \"gpu_hours\": 3.63, \"train_samples_per_second\": 7.478, \"train_steps_per_second\": 0.467, \"eval_ppl_holdout\": 17.725, \"eval_loss\": 2.875, \"eval_holdout_tokens\": 4077068}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:14:05.530Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:14:06.752002+00:00\"}]}, \"checkpoint_path\": \"output/models/grid_b2_0_seed123/final\", \"log_path\": \"~/runs/provenance_weight_training/grid_b2_0_seed123.log\", \"completed_at\": \"2026-05-14T14:14:33.471Z\"}, \"grid_b3_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:56.285Z\", \"updated_at\": \"2026-05-14T14:41:44.081Z\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/final/\", \"log_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:23:51.699Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:23:52.658692+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 10.7422, \"total_steps\": 6103, \"train_runtime_s\": 12955.83, \"gpu_hours\": 3.6, \"eval_ppl_holdout\": 17.76, \"eval_loss\": 2.877, \"eval_holdout_tokens\": 4077068}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b3_0_seed123/final/\", \"completed_at\": \"2026-05-14T14:24:22.860Z\", \"log_path\": \"~/runs/provenance_weight_training/grid_b3_0_seed123.log\", \"notes\": \"训练完成，eval 未执行（should_evaluate=false，缺少 --eval_data_path 和 --eval_steps）。Checkpoint: /root/provenance_weight_training/output/models/grid_b3_0_seed123/final/ (model.safetensors 1.19GB)。需补跑 eval。\"}, \"adaptive_v2_seed456\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:19.549Z\", \"updated_at\": \"2026-05-14T13:32:26.136Z\", \"hypothesis\": \"Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed456 performance (baseline adaptive PPL=17.64)\", \"conclusion\": \"killed\", \"notes\": \"D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）\"}, \"adaptive_v2_seed123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:19.157Z\", \"updated_at\": \"2026-05-14T13:32:25.356Z\", \"hypothesis\": \"Adaptive v2 (n_min fix: 3→2, no EMA) maintains or improves seed123 performance (baseline adaptive PPL=17.63)\", \"conclusion\": \"killed\", \"notes\": \"D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）\"}, \"adaptive_v2_seed42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:18.265Z\", \"updated_at\": \"2026-05-14T13:32:24.351Z\", \"hypothesis\": \"Adaptive v2 (n_min fix: 3→2, no EMA) fixes ESS clamping issue, achieves meaningful improvement over uniform baseline for seed=42\", \"conclusion\": \"killed\", \"notes\": \"D012 修正：取消 v2（含 EMA），改用 adaptive_fix（仅修 n_min=2，无 EMA）\"}, \"grid_b1_5_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:43.491Z\", \"updated_at\": \"2026-05-14T11:36:25.428Z\", \"spec\": {\"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_5_seed123/final/\", \"wall_clock_seconds\": 15053.1, \"gpu_hours\": 4.18}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:06:15.864Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:06:16.350913+00:00\"}]}, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_5_seed123/final/\", \"metrics\": {\"train_loss\": 10.4776, \"total_steps\": 6103, \"train_runtime_s\": 15053.1, \"gpu_hours\": 4.18, \"eval_ppl_holdout\": 17.701, \"eval_loss\": 2.8736}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:18:32.771Z\"}, \"grid_b1_0_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:42.784Z\", \"updated_at\": \"2026-05-14T10:54:12.453Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b1_0_seed123 --weighting_method grid --grid_b_value 1.0 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"68306\", \"log_path\": \"~/runs/provenance_weight_training/grid_b1_0_seed123.log\", \"submitted_at\": \"2026-05-14T06:53:47.084Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b1_0_seed123/final/\", \"wall_clock_seconds\": 13950, \"gpu_hours\": 3.88}, \"reproduce\": {\"finished_at\": \"2026-05-14T10:46:17.839Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:46:18.691130+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.674, \"eval_loss\": 2.8721, \"eval_holdout_tokens\": 4077068, \"train_loss\": 10.218, \"total_steps\": 6103, \"train_runtime_s\": 13878, \"gpu_hours\": 3.88}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:53:00Z\"}, \"grid_b0_5_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:52:42.314Z\", \"updated_at\": \"2026-05-14T10:42:12.465Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/grid_b0_5_seed123 --weighting_method grid --grid_b_value 0.5 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"68163\", \"log_path\": \"~/runs/provenance_weight_training/grid_b0_5_seed123.log\", \"submitted_at\": \"2026-05-14T06:53:43.648Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/grid_b0_5_seed123/final/\", \"wall_clock_seconds\": 13678.0, \"gpu_hours\": 3.8}, \"reproduce\": {\"finished_at\": \"2026-05-14T10:33:23.511Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:33:24.806181+00:00\"}]}, \"metrics\": {\"eval_ppl_holdout\": 17.638, \"eval_loss\": 2.87, \"eval_holdout_tokens\": 4077068, \"train_loss\": 9.601, \"total_steps\": 6103, \"train_runtime_s\": 13104, \"gpu_hours\": 3.8}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T10:41:41.614Z\"}, \"diagnostic_contamination100\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:14:09.555Z\", \"updated_at\": \"2026-05-14T08:48:08.828Z\", \"hypothesis\": \"Diagnostic: does 100% synthetic contamination significantly degrade held-out PPL vs 40%? If PPL ≈ 17.7, contamination sensitivity is too low for this scale.\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/synthetic_only.jsonl --output_dir output/models/diagnostic_contamination100_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 20000000 --seed 42\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"77187\", \"data_path\": \"data/synthetic_only.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T08:48:07.663Z\", \"notes\": \"Director 指令 kill：GPU 2/3 显存打满影响 grid-b seed123 训练速度。诊断实验等 grid-b round 1 完成后重跑。\"}, \"uniform_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:17:55.165Z\", \"updated_at\": \"2026-05-14T07:27:36.904Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed456 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed456/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"47890\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed456.log\", \"submitted_at\": \"2026-05-13T23:23:58.435Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed456/final/\", \"wall_clock_seconds\": 12349.2, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.2895, \"total_steps\": 6103, \"train_duration_s\": 11974, \"eval_ppl_holdout\": 17.7, \"eval_holdout_tokens\": 4080000}, \"completed_at\": \"2026-05-14T02:49:47.621Z\"}, \"uniform_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:17:53.217Z\", \"updated_at\": \"2026-05-14T07:27:35.749Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed123 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed123/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"47749\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed123.log\", \"submitted_at\": \"2026-05-13T23:23:55.904Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed123/final/\", \"wall_clock_seconds\": 12350.8, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.3121, \"total_steps\": 6103, \"train_duration_s\": 11994, \"eval_ppl_holdout\": 17.69, \"eval_holdout_tokens\": 4080000}, \"completed_at\": \"2026-05-14T02:49:46.681Z\"}, \"uniform_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:17:51.722Z\", \"updated_at\": \"2026-05-14T07:27:34.800Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed42/checkpoint-500\\\"\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"47603\", \"log_path\": \"~/runs/provenance_weight_training/uniform_seed42.log\", \"submitted_at\": \"2026-05-13T23:23:53.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed42/final/\", \"wall_clock_seconds\": 12352.2, \"gpu_hours\": 3.43}, \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 7.3104, \"total_steps\": 6103, \"train_duration_s\": 11946, \"eval_ppl_holdout\": 17.69, \"eval_holdout_tokens\": 4080000}, \"completed_at\": \"2026-05-14T02:49:45.269Z\"}, \"adaptive_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:25:03.137Z\", \"updated_at\": \"2026-05-14T07:27:33.394Z\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed456 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:3\"], \"pid\": \"59058\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed456.log\", \"submitted_at\": \"2026-05-14T02:46:25.330Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 456, \"checkpoint_path\": \"output/models/adaptive_seed456/final\", \"wall_clock_seconds\": 15161.8, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2354, \"train_runtime_s\": 13130.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.437, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.09-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.64, \"eval_holdout_tokens\": 4080000}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:59:07.123Z\", \"notes\": \"⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。\"}, \"adaptive_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:25:02.771Z\", \"updated_at\": \"2026-05-14T07:27:31.026Z\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed123 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:2\"], \"pid\": \"58978\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed123.log\", \"submitted_at\": \"2026-05-14T02:46:24.381Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 123, \"checkpoint_path\": \"output/models/adaptive_seed123/final\", \"wall_clock_seconds\": 15162.4, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13197.18, \"total_steps\": 6103, \"train_samples_per_second\": 7.399, \"train_steps_per_second\": 0.462, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.04-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.63, \"eval_holdout_tokens\": 4080000}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:59:06.757Z\", \"notes\": \"⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。\"}, \"adaptive_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:25:01.824Z\", \"updated_at\": \"2026-05-14T07:27:29.112Z\", \"hypothesis\": \"Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42\", \"spec\": {\"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\", \"server\": \"westd-47453\", \"gpu\": [\"cuda:1\"], \"pid\": \"58888\", \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed42.log\", \"submitted_at\": \"2026-05-14T02:46:23.000Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scored_data.jsonl\", \"data_count\": 371499, \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": 42, \"checkpoint_path\": \"output/models/adaptive_seed42/final\", \"wall_clock_seconds\": 15162.9, \"gpu_hours\": 4.21}, \"metrics\": {\"train_loss\": 9.2665, \"train_runtime_s\": 13115.09, \"total_steps\": 6103, \"train_samples_per_second\": 7.445, \"train_steps_per_second\": 0.465, \"epoch\": 0.26, \"weighting_method\": \"adaptive\", \"tau\": 0.8, \"n_min\": 3, \"contamination_ratio\": 0.4, \"b_star\": \"per-batch adaptive (0.0-3.8)\", \"alpha_eff_range\": \"0.03-0.80 (capped at tau)\", \"eval_ppl_holdout\": 17.69, \"eval_holdout_tokens\": 4080000}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:59:05.861Z\", \"notes\": \"⚠️ success 仅指训练完成无报错。MVP 假设验证待 held-out eval perplexity 结果。\"}, \"detector_tfidf_lr\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:28:08.894Z\", \"updated_at\": \"2026-05-13T23:28:28.425Z\", \"spec\": {\"command\": \"python train_tfidf_detector.py (combo_degrade: unigrams, max_features=10000, C=0.01, truncate 100 words)\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/detector.jsonl\", \"data_count\": 67960, \"model_name\": \"TF-IDF + LogisticRegression\", \"seed\": 42, \"checkpoint_path\": \"/root/provenance_weight_training/output/detector_tfidf/\", \"log_path\": \"/root/provenance_weight_training/output/detector_tfidf/calibration_results.json\"}, \"conclusion\": \"success\", \"hypothesis\": \"TF-IDF + LogisticRegression detector provides spread q-scores (AUC~0.94, not binarized) for provenance weighting, replacing over-accurate ModernBERT (D007)\", \"metrics\": {\"auc\": 0.939, \"accuracy\": 0.858, \"ece_raw\": 0.24, \"ece_calibrated\": 0.048, \"temperature_T\": 0.204, \"q_score_mean\": 0.6, \"q_score_std\": 0.374, \"q_score_median\": 0.707, \"mid_range_ratio\": 0.463}, \"completed_at\": \"2026-05-13T23:28:28.425Z\"}, \"datagen_synthetic_4gpu\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:12:11.474Z\", \"updated_at\": \"2026-05-13T21:50:46.682Z\", \"spec\": {\"command\": \"4x parallel generate_synthetic.py --depth 1 --num_tokens 33000000 --batch_size 128\", \"server\": \"westd-47453\", \"data_path\": \"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\", \"data_count\": \"target 132M tokens across 4 shards\", \"model_name\": \"Qwen/Qwen3-0.6B\", \"seed\": \"42/1042/2042/3042\", \"hypothesis\": \"4-GPU parallel generation produces 132M synthetic tokens in ~2.5h\", \"gpu\": \"cuda:0,1,2,3\", \"checkpoint_path\": \"/root/provenance_weight_training/data/synthetic/shard_{0,1,2,3}/\", \"log_path\": \"/root/provenance_weight_training/data/synthetic/gen_gpu{0,1,2,3}.log\", \"total_docs\": 340992, \"total_tokens\": 132033764}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T21:50:46.682Z\"}}, \"count\": 40, \"total\": 40, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2236}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The registry data is too large to load directly. Let me extract the specific experiments I need from the registry JSON file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "baaaa285-fd77-4b6b-a883-85c5c3a9aecf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTmedugqza7GNsHBkYLmaN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4332,
      "cache_read_input_tokens": 24787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4332
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

_source line 13_

Registry output is too large. Let me extract the specific experiments I need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "77bf0135-5409-4660-baef-4093e72cc31e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTmedugqza7GNsHBkYLmaN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4332,
      "cache_read_input_tokens": 24787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4332
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

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_01SQR7C6MitqdTJ5mn5WpD2S`</summary>

```json
{
  "command": "REGISTRY_FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/2a0c2b2e-ded9-41da-a3cc-a87bffb93fea/tool-results/mcp-agent-ml-research-read_registry-1778859445396.txt\"\n\n# Extract the result string, parse it as JSON, then filter for our target experiments\npython3 -c \"\nimport json\n\nwith open('$REGISTRY_FILE') as f:\n    data = json.load(f)\n\n# The result field is a JSON string itself\nexperiments = json.loads(data['result'])\n\ntargets = ['adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456',\n           'adaptive_fix_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456',\n           'nmin1_seed42', 'nmin4_seed42',\n           'uniform_seed42', 'uniform_seed123', 'uniform_seed456']\n\nfor exp in experiments:\n    if exp.get('exp_id') in targets:\n        print(json.dumps(exp, indent=2))\n        print('---')\n\"\n",
  "description": "Extract specific experiments from registry JSON",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "feacf1c9-92f7-45bf-999b-759b6563cc49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTmedugqza7GNsHBkYLmaN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4332,
      "cache_read_input_tokens": 24787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4332
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

_source line 15 · 2026-05-15T15:37:32.985Z_

<details><summary>↩ Tool result · reported error · `toolu_01SQR7C6MitqdTJ5mn5WpD2S`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 16, in &lt;module>
    if exp.get('exp_id') in targets:
       ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "db7d58bc-6ccc-4d0c-8d27-26f2cb88897f",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 16, in &lt;module>\n    if exp.get('exp_id') in targets:\n       ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01AxoqpVersU3dAW1yjcSeJW`</summary>

```json
{
  "command": "REGISTRY_FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/2a0c2b2e-ded9-41da-a3cc-a87bffb93fea/tool-results/mcp-agent-ml-research-read_registry-1778859445396.txt\"\n\npython3 -c \"\nimport json\n\nwith open('$REGISTRY_FILE') as f:\n    data = json.load(f)\n\nresult = data['result']\n# Check the type/structure\nif isinstance(result, str):\n    parsed = json.loads(result)\nelse:\n    parsed = result\n\nif isinstance(parsed, str):\n    parsed = json.loads(parsed)\n\nprint(type(parsed).__name__)\nif isinstance(parsed, list):\n    print(f'Length: {len(parsed)}')\n    if len(parsed) > 0:\n        print(f'First element type: {type(parsed[0]).__name__}')\n        if isinstance(parsed[0], dict):\n            print(f'Keys: {list(parsed[0].keys())}')\n        else:\n            print(f'First element: {str(parsed[0])[:200]}')\nelif isinstance(parsed, dict):\n    print(f'Keys: {list(parsed.keys())}')\n\"\n",
  "description": "Probe registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "3cd480c4-1674-471e-ae37-3fdf8324aea0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDjxbWx6zvCLWwuie2juL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 536,
      "cache_read_input_tokens": 29119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 536
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

_source line 17 · 2026-05-15T15:37:39.028Z_

<details><summary>↩ Tool result · `toolu_01AxoqpVersU3dAW1yjcSeJW`</summary>

```text
dict
Keys: ['success', 'data', 'error', 'metadata']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "3668b969-b8c7-4031-ab19-da4302f0265f",
  "tool_use_result": {
    "stdout": "dict\nKeys: ['success', 'data', 'error', 'metadata']",
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_011mCck41fsPV1Ej7a4CoWxn`</summary>

```json
{
  "command": "REGISTRY_FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/2a0c2b2e-ded9-41da-a3cc-a87bffb93fea/tool-results/mcp-agent-ml-research-read_registry-1778859445396.txt\"\n\npython3 -c \"\nimport json\n\nwith open('$REGISTRY_FILE') as f:\n    data = json.load(f)\n\nresult = data['result']\nif isinstance(result, str):\n    parsed = json.loads(result)\nelse:\n    parsed = result\nif isinstance(parsed, str):\n    parsed = json.loads(parsed)\n\nexperiments = parsed['data']\n\ntargets = ['adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456',\n           'adaptive_fix_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456',\n           'nmin1_seed42', 'nmin4_seed42',\n           'uniform_seed42', 'uniform_seed123', 'uniform_seed456']\n\nfor exp in experiments:\n    eid = exp.get('exp_id', '')\n    if eid in targets:\n        print(json.dumps(exp, indent=2))\n        print('---END---')\n\"\n",
  "description": "Extract target experiments from registry data",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "4324b4d6-87f7-405b-aa9f-3a21d1ce5e0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVu9iyPaHF41L3eG3nLoTY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 439,
      "cache_read_input_tokens": 29655,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 439
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

_source line 19 · 2026-05-15T15:37:44.665Z_

<details><summary>↩ Tool result · reported error · `toolu_011mCck41fsPV1Ej7a4CoWxn`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 23, in &lt;module>
    eid = exp.get('exp_id', '')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "f831658c-ce03-4401-8ba7-29a01c43a6d5",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 23, in &lt;module>\n    eid = exp.get('exp_id', '')\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01LqdbYgsAnpWm7Uuyicqhqt`</summary>

```json
{
  "command": "REGISTRY_FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/2a0c2b2e-ded9-41da-a3cc-a87bffb93fea/tool-results/mcp-agent-ml-research-read_registry-1778859445396.txt\"\n\npython3 -c \"\nimport json\n\nwith open('$REGISTRY_FILE') as f:\n    data = json.load(f)\n\nresult = data['result']\nif isinstance(result, str):\n    parsed = json.loads(result)\nelse:\n    parsed = result\nif isinstance(parsed, str):\n    parsed = json.loads(parsed)\n\nd = parsed['data']\nprint(type(d).__name__)\nif isinstance(d, list):\n    print(f'len={len(d)}, first type={type(d[0]).__name__}')\n    if isinstance(d[0], str):\n        # try parsing first element\n        try:\n            inner = json.loads(d[0])\n            print(f'Parsed first element type: {type(inner).__name__}')\n            if isinstance(inner, dict):\n                print(f'Keys: {list(inner.keys())}')\n        except:\n            print(f'First 300 chars: {d[0][:300]}')\nelif isinstance(d, dict):\n    print(f'Keys: {list(d.keys())[:10]}')\n    # check first value\n    first_key = list(d.keys())[0]\n    print(f'First key: {first_key}, value type: {type(d[first_key]).__name__}')\n    if isinstance(d[first_key], dict):\n        print(f'Value keys: {list(d[first_key].keys())}')\n    elif isinstance(d[first_key], str):\n        print(f'Value[:200]: {d[first_key][:200]}')\n\"\n",
  "description": "Probe data structure deeper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "6a9a2547-3d1f-4801-8a84-fc550d9ebaf5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEJBLcjzyVzrQSTHJawEMM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 510,
      "cache_read_input_tokens": 30094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 510
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

_source line 21 · 2026-05-15T15:37:52.513Z_

<details><summary>↩ Tool result · `toolu_01LqdbYgsAnpWm7Uuyicqhqt`</summary>

```text
dict
Keys: ['experiments', 'count', 'total', 'baseline']
First key: experiments, value type: dict
Value keys: ['tau_095_seed42', 'tau_09_seed42', 'tau_05_seed42', 'nmin4_seed42', 'nmin1_seed42', 'tau_06_seed42', 'ess_only_seed42', 'tau_07_seed42', 'golden_ratio_seed42', 'tau_0.6_seed42', 'detector_modernbert', 'grid_b5_0_seed456', 'grid_b3_0_seed456', 'grid_b2_0_seed456', 'grid_b_low_seed42', 'grid_b1_5_seed456', 'grid_b1_0_seed456', 'grid_b0_5_seed456', 'adaptive_fix_seed456', 'adaptive_fix_seed123', 'adaptive_fix_seed42', 'grid_b_seed42_batch', 'grid_b5_0_seed123', 'grid_b2_0_seed123', 'grid_b3_0_seed123', 'adaptive_v2_seed456', 'adaptive_v2_seed123', 'adaptive_v2_seed42', 'grid_b1_5_seed123', 'grid_b1_0_seed123', 'grid_b0_5_seed123', 'diagnostic_contamination100', 'uniform_seed456', 'uniform_seed123', 'uniform_seed42', 'adaptive_seed456', 'adaptive_seed123', 'adaptive_seed42', 'detector_tfidf_lr', 'datagen_synthetic_4gpu']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "855d6f0e-ef64-483f-9a3a-f25968bedfe5",
  "tool_use_result": {
    "stdout": "dict\nKeys: ['experiments', 'count', 'total', 'baseline']\nFirst key: experiments, value type: dict\nValue keys: ['tau_095_seed42', 'tau_09_seed42', 'tau_05_seed42', 'nmin4_seed42', 'nmin1_seed42', 'tau_06_seed42', 'ess_only_seed42', 'tau_07_seed42', 'golden_ratio_seed42', 'tau_0.6_seed42', 'detector_modernbert', 'grid_b5_0_seed456', 'grid_b3_0_seed456', 'grid_b2_0_seed456', 'grid_b_low_seed42', 'grid_b1_5_seed456', 'grid_b1_0_seed456', 'grid_b0_5_seed456', 'adaptive_fix_seed456', 'adaptive_fix_seed123', 'adaptive_fix_seed42', 'grid_b_seed42_batch', 'grid_b5_0_seed123', 'grid_b2_0_seed123', 'grid_b3_0_seed123', 'adaptive_v2_seed456', 'adaptive_v2_seed123', 'adaptive_v2_seed42', 'grid_b1_5_seed123', 'grid_b1_0_seed123', 'grid_b0_5_seed123', 'diagnostic_contamination100', 'uniform_seed456', 'uniform_seed123', 'uniform_seed42', 'adaptive_seed456', 'adaptive_seed123', 'adaptive_seed42', 'detector_tfidf_lr', 'datagen_synthetic_4gpu']",
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

_source line 22_

Now I can see the structure. Let me extract the specific experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "681fa473-c440-4506-8e27-86a0fbefb012",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EKc66q3Z89GGNkGoZNXYW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1000,
      "cache_read_input_tokens": 30604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1000
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

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ez3PQUWg3sNtH6ycSMNVxN`</summary>

```json
{
  "command": "REGISTRY_FILE=\"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/2a0c2b2e-ded9-41da-a3cc-a87bffb93fea/tool-results/mcp-agent-ml-research-read_registry-1778859445396.txt\"\n\npython3 -c \"\nimport json\n\nwith open('$REGISTRY_FILE') as f:\n    data = json.load(f)\n\nresult = json.loads(data['result'])\nif isinstance(result, str):\n    result = json.loads(result)\n\nexperiments = result['data']['experiments']\n\ntargets = ['adaptive_seed42', 'adaptive_seed123', 'adaptive_seed456',\n           'adaptive_fix_seed42', 'adaptive_fix_seed123', 'adaptive_fix_seed456',\n           'nmin1_seed42', 'nmin4_seed42',\n           'uniform_seed42', 'uniform_seed123', 'uniform_seed456']\n\nfor t in targets:\n    if t in experiments:\n        print(f'=== {t} ===')\n        print(json.dumps(experiments[t], indent=2))\n        print()\n    else:\n        print(f'=== {t} === NOT FOUND')\n        print()\n\"\n",
  "description": "Extract target experiments by key",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "31cc2984-73ad-491f-a56e-24624779ec84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014EKc66q3Z89GGNkGoZNXYW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1000,
      "cache_read_input_tokens": 30604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1000
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

_source line 24 · 2026-05-15T15:37:58.328Z_

<details><summary>↩ Tool result · `toolu_01Ez3PQUWg3sNtH6ycSMNVxN`</summary>

```text
=== adaptive_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T02:25:01.824Z",
  "updated_at": "2026-05-14T07:27:29.112Z",
  "hypothesis": "Adaptive b* (from \u03b1_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42",
  "spec": {
    "command": "python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4",
    "server": "westd-47453",
    "gpu": [
      "cuda:1"
    ],
    "pid": "58888",
    "log_path": "~/runs/provenance_weight_training/adaptive_seed42.log",
    "submitted_at": "2026-05-14T02:46:23.000Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/scored_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 42,
    "checkpoint_path": "output/models/adaptive_seed42/final",
    "wall_clock_seconds": 15162.9,
    "gpu_hours": 4.21
  },
  "metrics": {
    "train_loss": 9.2665,
    "train_runtime_s": 13115.09,
    "total_steps": 6103,
    "train_samples_per_second": 7.445,
    "train_steps_per_second": 0.465,
    "epoch": 0.26,
    "weighting_method": "adaptive",
    "tau": 0.8,
    "n_min": 3,
    "contamination_ratio": 0.4,
    "b_star": "per-batch adaptive (0.0-3.8)",
    "alpha_eff_range": "0.03-0.80 (capped at tau)",
    "eval_ppl_holdout": 17.69,
    "eval_holdout_tokens": 4080000
  },
  "conclusion": "success",
  "completed_at": "2026-05-14T06:59:05.861Z",
  "notes": "\u26a0\ufe0f success \u4ec5\u6307\u8bad\u7ec3\u5b8c\u6210\u65e0\u62a5\u9519\u3002MVP \u5047\u8bbe\u9a8c\u8bc1\u5f85 held-out eval perplexity \u7ed3\u679c\u3002"
}

=== adaptive_seed123 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T02:25:02.771Z",
  "updated_at": "2026-05-14T07:27:31.026Z",
  "hypothesis": "Adaptive b* (from \u03b1_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123",
  "spec": {
    "command": "python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed123 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4",
    "server": "westd-47453",
    "gpu": [
      "cuda:2"
    ],
    "pid": "58978",
    "log_path": "~/runs/provenance_weight_training/adaptive_seed123.log",
    "submitted_at": "2026-05-14T02:46:24.381Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/scored_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 123,
    "checkpoint_path": "output/models/adaptive_seed123/final",
    "wall_clock_seconds": 15162.4,
    "gpu_hours": 4.21
  },
  "metrics": {
    "train_loss": 9.2665,
    "train_runtime_s": 13197.18,
    "total_steps": 6103,
    "train_samples_per_second": 7.399,
    "train_steps_per_second": 0.462,
    "epoch": 0.26,
    "weighting_method": "adaptive",
    "tau": 0.8,
    "n_min": 3,
    "contamination_ratio": 0.4,
    "b_star": "per-batch adaptive (0.0-3.8)",
    "alpha_eff_range": "0.04-0.80 (capped at tau)",
    "eval_ppl_holdout": 17.63,
    "eval_holdout_tokens": 4080000
  },
  "conclusion": "success",
  "completed_at": "2026-05-14T06:59:06.757Z",
  "notes": "\u26a0\ufe0f success \u4ec5\u6307\u8bad\u7ec3\u5b8c\u6210\u65e0\u62a5\u9519\u3002MVP \u5047\u8bbe\u9a8c\u8bc1\u5f85 held-out eval perplexity \u7ed3\u679c\u3002"
}

=== adaptive_seed456 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T02:25:03.137Z",
  "updated_at": "2026-05-14T07:27:33.394Z",
  "hypothesis": "Adaptive b* (from \u03b1_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456",
  "spec": {
    "command": "python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed456 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4",
    "server": "westd-47453",
    "gpu": [
      "cuda:3"
    ],
    "pid": "59058",
    "log_path": "~/runs/provenance_weight_training/adaptive_seed456.log",
    "submitted_at": "2026-05-14T02:46:25.330Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "data/scored_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 456,
    "checkpoint_path": "output/models/adaptive_seed456/final",
    "wall_clock_seconds": 15161.8,
    "gpu_hours": 4.21
  },
  "metrics": {
    "train_loss": 9.2354,
    "train_runtime_s": 13130.09,
    "total_steps": 6103,
    "train_samples_per_second": 7.437,
    "train_steps_per_second": 0.465,
    "epoch": 0.26,
    "weighting_method": "adaptive",
    "tau": 0.8,
    "n_min": 3,
    "contamination_ratio": 0.4,
    "b_star": "per-batch adaptive (0.0-3.8)",
    "alpha_eff_range": "0.09-0.80 (capped at tau)",
    "eval_ppl_holdout": 17.64,
    "eval_holdout_tokens": 4080000
  },
  "conclusion": "success",
  "completed_at": "2026-05-14T06:59:07.123Z",
  "notes": "\u26a0\ufe0f success \u4ec5\u6307\u8bad\u7ec3\u5b8c\u6210\u65e0\u62a5\u9519\u3002MVP \u5047\u8bbe\u9a8c\u8bc1\u5f85 held-out eval perplexity \u7ed3\u679c\u3002"
}

=== adaptive_fix_seed42 ===
{
  "status": "DONE",
  "retry_count": 2,
  "created_at": "2026-05-14T13:32:30.463Z",
  "updated_at": "2026-05-15T00:00:25.930Z",
  "hypothesis": "D012 n_min fix (3\u21922, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)",
  "parent": "adaptive_seed42",
  "notes": "\u6700\u7ec8\u6e05\u7406\u540e\u91cd\u63d0\u4ea4\u3002\u4ece checkpoint-1500 \u6062\u590d\uff0c\u65e0 inline eval\u3002PID=126801",
  "failure_reason": "",
  "completed_at": "",
  "extra": {
    "previous_failure": {
      "conclusion": "failed",
      "notes": "D012 \u4ee3\u7801\u9a8c\u8bc1\u901a\u8fc7\uff08n_min=max(2,batch_size//2), \u65e0EMA, import OK\uff09\u3002\u7b49 GPU \u91ca\u653e\u540e\u63d0\u4ea4\u3002"
    },
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-14T17:38:26.312269+00:00"
      },
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-14T20:39:45.953045+00:00"
      }
    ]
  },
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_fix_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint output/models/adaptive_fix_seed42/checkpoint-1500\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:1"
    ],
    "pid": "126796",
    "log_path": "~/runs/provenance_weight_training/adaptive_fix_seed42.log",
    "submitted_at": "2026-05-14T17:47:21.683Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 12053.2,
    "gpu_hours": 3.35
  },
  "reproduce": {
    "finished_at": "2026-05-14T20:39:44.942Z"
  },
  "conclusion": "success",
  "metrics": {
    "train_loss": 7.5167,
    "train_runtime": 10304.37,
    "train_samples_per_second": 9.476,
    "train_steps_per_second": 0.592,
    "total_steps": 6103,
    "eval_loss_holdout": 2.8709,
    "eval_ppl_holdout": 17.65,
    "eval_tokens": 4077068,
    "b_star_count": 26458,
    "b_star_mean": 1.399,
    "b_star_median": 0.871,
    "b_star_std": 1.933,
    "b_star_min": 0,
    "b_star_max": 20,
    "b_star_p25": 0.54,
    "b_star_p75": 1.512,
    "b_star_pct_below_0.5": 20.9,
    "b_star_pct_0.5_to_1": 35.7,
    "b_star_pct_1_to_2": 27.3,
    "b_star_pct_above_2": 16.1,
    "b_star_note": "Training-only records (eval checkpoint records with b*=0 excluded)"
  },
  "checkpoint_path": "output/models/adaptive_fix_seed42/final"
}

=== adaptive_fix_seed123 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T13:32:31.409Z",
  "updated_at": "2026-05-15T00:00:29.758Z",
  "hypothesis": "D012 n_min fix (3\u21922, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performance (baseline adaptive PPL=17.63, uniform PPL=17.69)",
  "parent": "adaptive_seed123",
  "notes": "\u6700\u7ec8\u6e05\u7406\u540e\u91cd\u63d0\u4ea4\u3002\u4ece checkpoint-1500 \u6062\u590d\uff0c\u65e0 inline eval\u3002PID=126944",
  "failure_reason": "",
  "conclusion": "success",
  "spec": {
    "command": "python run_clm_weighted.py --weighting_method adaptive --n_min 2 --no_ema --resume_from_checkpoint checkpoint-1500",
    "server": "westd-47453",
    "gpu": [
      "cuda:2"
    ],
    "pid": "126939",
    "log_path": "~/runs/provenance_weight_training/adaptive_fix_seed123.log",
    "submitted_at": "2026-05-14T17:47:28.582Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/provenance_weight_training/data/scored_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen3-0.6B",
    "seed": 123,
    "checkpoint_source": "checkpoint-1500 (D012 fix)",
    "eval_data": "/root/provenance_weight_training/data/human/eval_holdout.jsonl",
    "wall_clock_seconds": 10807.2,
    "gpu_hours": 3.0
  },
  "reproduce": {
    "finished_at": "2026-05-14T20:41:22.910Z"
  },
  "completed_at": "",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-14T17:38:38.735034+00:00"
      },
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-14T20:41:26.828424+00:00"
      }
    ]
  },
  "checkpoint_path": "/root/provenance_weight_training/output/models/adaptive_fix_seed123/final",
  "log_path": "~/runs/provenance_weight_training/adaptive_fix_seed123.log",
  "metrics": {
    "eval_ppl_holdout": 17.643,
    "eval_loss": 2.8704,
    "eval_tokens": 4077068,
    "train_loss_weighted": 7.517,
    "train_runtime_s": 10347,
    "total_steps": 6103,
    "epoch": 0.26,
    "b_star_mean": 1.431,
    "b_star_median": 0.88,
    "b_star_std": 2.029,
    "b_star_min": 0,
    "b_star_max": 20,
    "b_star_pct_below_0.5": 20.9,
    "b_star_pct_0.5_to_1": 35.7,
    "b_star_pct_1_to_2": 27.3,
    "b_star_pct_2_to_5": 6.3,
    "b_star_pct_above_5": 1.9,
    "b_star_count": 25906,
    "b_star_p25": 0.54,
    "b_star_p75": 1.52,
    "b_star_pct_above_2": 16.1,
    "b_star_note": "Training-only records (eval checkpoint records with b*=0 excluded)"
  }
}

=== adaptive_fix_seed456 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T13:32:31.779Z",
  "updated_at": "2026-05-15T00:00:33.021Z",
  "hypothesis": "D012 n_min fix (3\u21922, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performance (baseline adaptive PPL=17.64, uniform PPL=17.70)",
  "parent": "adaptive_seed456",
  "notes": "\u6700\u7ec8\u6e05\u7406\u540e\u91cd\u63d0\u4ea4\u3002\u4ece checkpoint-1000 \u6062\u590d\uff0c\u65e0 inline eval\u3002PID=127285",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_fix_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint output/models/adaptive_fix_seed456/checkpoint-1000\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:3"
    ],
    "pid": "127280",
    "log_path": "~/runs/provenance_weight_training/adaptive_fix_seed456.log",
    "submitted_at": "2026-05-14T17:47:33.774Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 12040.6,
    "gpu_hours": 3.34
  },
  "server": "westd-47453",
  "gpu": "cuda:3",
  "account": "root",
  "pid": "115066",
  "log_path": "~/runs/provenance_weight_training/adaptive_fix_seed456.log",
  "reproduce": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --eval_data_path data/human/eval_holdout.jsonl --output_dir output/models/adaptive_fix_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --eval_steps 500 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\"",
    "finished_at": "2026-05-14T21:00:17.106Z"
  },
  "failure_reason": "",
  "conclusion": "success",
  "completed_at": "",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-14T17:38:47.164099+00:00"
      },
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-14T21:00:18.079813+00:00"
      }
    ]
  },
  "metrics": {
    "train_loss": 8.3124,
    "train_runtime": 11436.05,
    "train_samples_per_second": 8.539,
    "train_steps_per_second": 0.534,
    "total_steps": 6103,
    "eval_loss_holdout": 2.8711,
    "eval_ppl_holdout": 17.66,
    "eval_tokens": 4077068,
    "b_star_count": 26396,
    "b_star_mean": 1.416,
    "b_star_median": 0.88,
    "b_star_std": 1.993,
    "b_star_min": 0,
    "b_star_max": 20,
    "b_star_p25": 0.54,
    "b_star_p75": 1.52,
    "b_star_pct_below_0.5": 20.9,
    "b_star_pct_0.5_to_1": 35.7,
    "b_star_pct_1_to_2": 27.3,
    "b_star_pct_above_2": 16.1,
    "b_star_note": "Training-only records (eval checkpoint records with b*=0 excluded)"
  },
  "checkpoint_path": "output/models/adaptive_fix_seed456/final"
}

=== nmin1_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T07:48:31.298Z",
  "updated_at": "2026-05-15T14:36:49.692Z",
  "hypothesis": "n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades with overly permissive ESS bound",
  "server": "westd-47453",
  "gpu": "cuda:2",
  "account": "root",
  "reproduce": {
    "server": "westd-47453",
    "gpu": "cuda:2",
    "started_at": "2026-05-15T09:34:56.077Z",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\"",
    "finished_at": "2026-05-15T14:27:21.174Z",
    "training_hours": 4.87
  },
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:2"
    ],
    "pid": "194005",
    "log_path": "~/runs/provenance_weight_training/nmin1_seed42.log",
    "submitted_at": "2026-05-15T09:36:06.479Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "wall_clock_seconds": 18033.6,
    "gpu_hours": 5.01
  },
  "pid": "194005",
  "log_path": "~/runs/provenance_weight_training/nmin1_seed42.log",
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-15T14:27:22.547409+00:00"
      }
    ]
  },
  "metrics": {
    "eval_ppl_holdout": 17.789,
    "eval_loss": 2.8786,
    "eval_holdout_tokens": 4077068,
    "b_star_mean": 7.197,
    "b_star_median": 1.746,
    "b_star_std": 8.374,
    "b_star_min": 0,
    "b_star_max": 20,
    "b_star_p25": 0.803,
    "b_star_p75": 20,
    "b_star_zero_frac": 0.019,
    "b_star_pct_below_0.5": 13.1,
    "b_star_pct_0.5_to_1": 19.1,
    "b_star_pct_1_to_2": 21.1,
    "b_star_pct_above_2": 46.7,
    "b_star_count": 24412,
    "alpha_eff_mean": 0.714,
    "alpha_eff_median": 0.8
  },
  "notes": "\u8bad\u7ec3\u5b8c\u6210(EXIT_CODE=0, 4h50m)\u3002PPL=17.789\uff0c\u6bd4 adaptive_fix(n_min=2, 17.650) \u5dee +0.139\uff0c\u6bd4 uniform(17.690) \u5dee +0.099\u3002n_min=1 \u5bfc\u81f4\u6781\u7aef b* \u5206\u5e03\uff1a46.7% batch b*\u22652\uff0cp75=20.0(\u4e0a\u9650)\uff0cmean=7.197\u3002ESS \u7ea6\u675f\u51e0\u4e4e\u5931\u6548\uff0cover-downweighting \u660e\u663e\u3002confirms n_min=2 \u662f\u66f4\u4f18\u9009\u62e9\u3002",
  "checkpoint_path": "/root/provenance_weight_training/output/models/nmin1_seed42",
  "conclusion": "success",
  "completed_at": "2026-05-15T14:36:40.056Z"
}

=== nmin4_seed42 ===
{
  "status": "PREPARING",
  "retry_count": 0,
  "created_at": "2026-05-15T14:36:45.229Z",
  "updated_at": "2026-05-15T14:38:42.341Z",
  "spec": {
    "hypothesis": "n_min=4 (=batch_size) boundary case: maximal ESS constraint forces b*\u21920 on most batches, testing if over-constrained adaptive degrades to near-uniform. Baseline: adaptive_fix n_min=2 PPL=17.650.",
    "parent": "adaptive_fix_seed42",
    "planned_gpu": "cuda:1",
    "planned_command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin4_seed42 --weighting_method adaptive --n_min 4 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\""
  },
  "hypothesis": "n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=batch_size. Should degrade to uniform-equivalent PPL (~17.69). Key boundary condition for n_min sensitivity analysis."
}

=== uniform_seed42 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-13T22:17:51.722Z",
  "updated_at": "2026-05-14T07:27:34.800Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed42/checkpoint-500\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:1"
    ],
    "pid": "47603",
    "log_path": "~/runs/provenance_weight_training/uniform_seed42.log",
    "submitted_at": "2026-05-13T23:23:53.026Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/provenance_weight_training/data/mixed_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 42,
    "checkpoint_path": "/root/provenance_weight_training/output/models/uniform_seed42/final/",
    "wall_clock_seconds": 12352.2,
    "gpu_hours": 3.43
  },
  "hypothesis": "Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods",
  "conclusion": "success",
  "metrics": {
    "train_loss": 7.3104,
    "total_steps": 6103,
    "train_duration_s": 11946,
    "eval_ppl_holdout": 17.69,
    "eval_holdout_tokens": 4080000
  },
  "completed_at": "2026-05-14T02:49:45.269Z"
}

=== uniform_seed123 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-13T22:17:53.217Z",
  "updated_at": "2026-05-14T07:27:35.749Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed123 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed123/checkpoint-500\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:2"
    ],
    "pid": "47749",
    "log_path": "~/runs/provenance_weight_training/uniform_seed123.log",
    "submitted_at": "2026-05-13T23:23:55.904Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/provenance_weight_training/data/mixed_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 123,
    "checkpoint_path": "/root/provenance_weight_training/output/models/uniform_seed123/final/",
    "wall_clock_seconds": 12350.8,
    "gpu_hours": 3.43
  },
  "hypothesis": "Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods",
  "conclusion": "success",
  "metrics": {
    "train_loss": 7.3121,
    "total_steps": 6103,
    "train_duration_s": 11994,
    "eval_ppl_holdout": 17.69,
    "eval_holdout_tokens": 4080000
  },
  "completed_at": "2026-05-14T02:49:46.681Z"
}

=== uniform_seed456 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-13T22:17:55.165Z",
  "updated_at": "2026-05-14T07:27:36.904Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed456 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed456/checkpoint-500\"",
    "server": "westd-47453",
    "gpu": [
      "cuda:3"
    ],
    "pid": "47890",
    "log_path": "~/runs/provenance_weight_training/uniform_seed456.log",
    "submitted_at": "2026-05-13T23:23:58.435Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "/root/provenance_weight_training/data/mixed_data.jsonl",
    "data_count": 371499,
    "model_name": "Qwen/Qwen3-0.6B",
    "seed": 456,
    "checkpoint_path": "/root/provenance_weight_training/output/models/uniform_seed456/final/",
    "wall_clock_seconds": 12349.2,
    "gpu_hours": 3.43
  },
  "hypothesis": "Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods",
  "conclusion": "success",
  "metrics": {
    "train_loss": 7.2895,
    "total_steps": 6103,
    "train_duration_s": 11974,
    "eval_ppl_holdout": 17.7,
    "eval_holdout_tokens": 4080000
  },
  "completed_at": "2026-05-14T02:49:47.621Z"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "32b57eda-2591-4494-87fd-4a4ae5e70076",
  "tool_use_result": {
    "stdout": "=== adaptive_seed42 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-14T02:25:01.824Z\",\n  \"updated_at\": \"2026-05-14T07:27:29.112Z\",\n  \"hypothesis\": \"Adaptive b* (from \\u03b1_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42\",\n  \"spec\": {\n    \"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed42 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\",\n    \"server\": \"westd-47453\",\n    \"gpu\": [\n      \"cuda:1\"\n    ],\n    \"pid\": \"58888\",\n    \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed42.log\",\n    \"submitted_at\": \"2026-05-14T02:46:23.000Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"data_path\": \"data/scored_data.jsonl\",\n    \"data_count\": 371499,\n    \"model_name\": \"Qwen/Qwen3-0.6B\",\n    \"seed\": 42,\n    \"checkpoint_path\": \"output/models/adaptive_seed42/final\",\n    \"wall_clock_seconds\": 15162.9,\n    \"gpu_hours\": 4.21\n  },\n  \"metrics\": {\n    \"train_loss\": 9.2665,\n    \"train_runtime_s\": 13115.09,\n    \"total_steps\": 6103,\n    \"train_samples_per_second\": 7.445,\n    \"train_steps_per_second\": 0.465,\n    \"epoch\": 0.26,\n    \"weighting_method\": \"adaptive\",\n    \"tau\": 0.8,\n    \"n_min\": 3,\n    \"contamination_ratio\": 0.4,\n    \"b_star\": \"per-batch adaptive (0.0-3.8)\",\n    \"alpha_eff_range\": \"0.03-0.80 (capped at tau)\",\n    \"eval_ppl_holdout\": 17.69,\n    \"eval_holdout_tokens\": 4080000\n  },\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-14T06:59:05.861Z\",\n  \"notes\": \"\\u26a0\\ufe0f success \\u4ec5\\u6307\\u8bad\\u7ec3\\u5b8c\\u6210\\u65e0\\u62a5\\u9519\\u3002MVP \\u5047\\u8bbe\\u9a8c\\u8bc1\\u5f85 held-out eval perplexity \\u7ed3\\u679c\\u3002\"\n}\n\n=== adaptive_seed123 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-14T02:25:02.771Z\",\n  \"updated_at\": \"2026-05-14T07:27:31.026Z\",\n  \"hypothesis\": \"Adaptive b* (from \\u03b1_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123\",\n  \"spec\": {\n    \"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed123 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\",\n    \"server\": \"westd-47453\",\n    \"gpu\": [\n      \"cuda:2\"\n    ],\n    \"pid\": \"58978\",\n    \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed123.log\",\n    \"submitted_at\": \"2026-05-14T02:46:24.381Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"data_path\": \"data/scored_data.jsonl\",\n    \"data_count\": 371499,\n    \"model_name\": \"Qwen/Qwen3-0.6B\",\n    \"seed\": 123,\n    \"checkpoint_path\": \"output/models/adaptive_seed123/final\",\n    \"wall_clock_seconds\": 15162.4,\n    \"gpu_hours\": 4.21\n  },\n  \"metrics\": {\n    \"train_loss\": 9.2665,\n    \"train_runtime_s\": 13197.18,\n    \"total_steps\": 6103,\n    \"train_samples_per_second\": 7.399,\n    \"train_steps_per_second\": 0.462,\n    \"epoch\": 0.26,\n    \"weighting_method\": \"adaptive\",\n    \"tau\": 0.8,\n    \"n_min\": 3,\n    \"contamination_ratio\": 0.4,\n    \"b_star\": \"per-batch adaptive (0.0-3.8)\",\n    \"alpha_eff_range\": \"0.04-0.80 (capped at tau)\",\n    \"eval_ppl_holdout\": 17.63,\n    \"eval_holdout_tokens\": 4080000\n  },\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-14T06:59:06.757Z\",\n  \"notes\": \"\\u26a0\\ufe0f success \\u4ec5\\u6307\\u8bad\\u7ec3\\u5b8c\\u6210\\u65e0\\u62a5\\u9519\\u3002MVP \\u5047\\u8bbe\\u9a8c\\u8bc1\\u5f85 held-out eval perplexity \\u7ed3\\u679c\\u3002\"\n}\n\n=== adaptive_seed456 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-14T02:25:03.137Z\",\n  \"updated_at\": \"2026-05-14T07:27:33.394Z\",\n  \"hypothesis\": \"Adaptive b* (from \\u03b1_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456\",\n  \"spec\": {\n    \"command\": \"python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_seed456 --weighting_method adaptive --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4\",\n    \"server\": \"westd-47453\",\n    \"gpu\": [\n      \"cuda:3\"\n    ],\n    \"pid\": \"59058\",\n    \"log_path\": \"~/runs/provenance_weight_training/adaptive_seed456.log\",\n    \"submitted_at\": \"2026-05-14T02:46:25.330Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"data_path\": \"data/scored_data.jsonl\",\n    \"data_count\": 371499,\n    \"model_name\": \"Qwen/Qwen3-0.6B\",\n    \"seed\": 456,\n    \"checkpoint_path\": \"output/models/adaptive_seed456/final\",\n    \"wall_clock_seconds\": 15161.8,\n    \"gpu_hours\": 4.21\n  },\n  \"metrics\": {\n    \"train_loss\": 9.2354,\n    \"train_runtime_s\": 13130.09,\n    \"total_steps\": 6103,\n    \"train_samples_per_second\": 7.437,\n    \"train_steps_per_second\": 0.465,\n    \"epoch\": 0.26,\n    \"weighting_method\": \"adaptive\",\n    \"tau\": 0.8,\n    \"n_min\": 3,\n    \"contamination_ratio\": 0.4,\n    \"b_star\": \"per-batch adaptive (0.0-3.8)\",\n    \"alpha_eff_range\": \"0.09-0.80 (capped at tau)\",\n    \"eval_ppl_holdout\": 17.64,\n    \"eval_holdout_tokens\": 4080000\n  },\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-14T06:59:07.123Z\",\n  \"notes\": \"\\u26a0\\ufe0f success \\u4ec5\\u6307\\u8bad\\u7ec3\\u5b8c\\u6210\\u65e0\\u62a5\\u9519\\u3002MVP \\u5047\\u8bbe\\u9a8c\\u8bc1\\u5f85 held-out eval perplexity \\u7ed3\\u679c\\u3002\"\n}\n\n=== adaptive_fix_seed42 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 2,\n  \"created_at\": \"2026-05-14T13:32:30.463Z\",\n  \"updated_at\": \"2026-05-15T00:00:25.930Z\",\n  \"hypothesis\": \"D012 n_min fix (3\\u21922, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over uniform baseline (PPL=17.69) for seed=42. Parent: adaptive_seed42 (PPL=17.69, n_min=3 bug)\",\n  \"parent\": \"adaptive_seed42\",\n  \"notes\": \"\\u6700\\u7ec8\\u6e05\\u7406\\u540e\\u91cd\\u63d0\\u4ea4\\u3002\\u4ece checkpoint-1500 \\u6062\\u590d\\uff0c\\u65e0 inline eval\\u3002PID=126801\",\n  \"failure_reason\": \"\",\n  \"completed_at\": \"\",\n  \"extra\": {\n    \"previous_failure\": {\n      \"conclusion\": \"failed\",\n      \"notes\": \"D012 \\u4ee3\\u7801\\u9a8c\\u8bc1\\u901a\\u8fc7\\uff08n_min=max(2,batch_size//2), \\u65e0EMA, import OK\\uff09\\u3002\\u7b49 GPU \\u91ca\\u653e\\u540e\\u63d0\\u4ea4\\u3002\"\n    },\n    \"hook_events\": [\n      {\n        \"event\": \"on_failed\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-14T17:38:26.312269+00:00\"\n      },\n      {\n        \"event\": \"on_complete\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-14T20:39:45.953045+00:00\"\n      }\n    ]\n  },\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_fix_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 42 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint output/models/adaptive_fix_seed42/checkpoint-1500\\\"\",\n    \"server\": \"westd-47453\",\n    \"gpu\": [\n      \"cuda:1\"\n    ],\n    \"pid\": \"126796\",\n    \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed42.log\",\n    \"submitted_at\": \"2026-05-14T17:47:21.683Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"wall_clock_seconds\": 12053.2,\n    \"gpu_hours\": 3.35\n  },\n  \"reproduce\": {\n    \"finished_at\": \"2026-05-14T20:39:44.942Z\"\n  },\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"train_loss\": 7.5167,\n    \"train_runtime\": 10304.37,\n    \"train_samples_per_second\": 9.476,\n    \"train_steps_per_second\": 0.592,\n    \"total_steps\": 6103,\n    \"eval_loss_holdout\": 2.8709,\n    \"eval_ppl_holdout\": 17.65,\n    \"eval_tokens\": 4077068,\n    \"b_star_count\": 26458,\n    \"b_star_mean\": 1.399,\n    \"b_star_median\": 0.871,\n    \"b_star_std\": 1.933,\n    \"b_star_min\": 0,\n    \"b_star_max\": 20,\n    \"b_star_p25\": 0.54,\n    \"b_star_p75\": 1.512,\n    \"b_star_pct_below_0.5\": 20.9,\n    \"b_star_pct_0.5_to_1\": 35.7,\n    \"b_star_pct_1_to_2\": 27.3,\n    \"b_star_pct_above_2\": 16.1,\n    \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"\n  },\n  \"checkpoint_path\": \"output/models/adaptive_fix_seed42/final\"\n}\n\n=== adaptive_fix_seed123 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-14T13:32:31.409Z\",\n  \"updated_at\": \"2026-05-15T00:00:29.758Z\",\n  \"hypothesis\": \"D012 n_min fix (3\\u21922, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performance (baseline adaptive PPL=17.63, uniform PPL=17.69)\",\n  \"parent\": \"adaptive_seed123\",\n  \"notes\": \"\\u6700\\u7ec8\\u6e05\\u7406\\u540e\\u91cd\\u63d0\\u4ea4\\u3002\\u4ece checkpoint-1500 \\u6062\\u590d\\uff0c\\u65e0 inline eval\\u3002PID=126944\",\n  \"failure_reason\": \"\",\n  \"conclusion\": \"success\",\n  \"spec\": {\n    \"command\": \"python run_clm_weighted.py --weighting_method adaptive --n_min 2 --no_ema --resume_from_checkpoint checkpoint-1500\",\n    \"server\": \"westd-47453\",\n    \"gpu\": [\n      \"cuda:2\"\n    ],\n    \"pid\": \"126939\",\n    \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed123.log\",\n    \"submitted_at\": \"2026-05-14T17:47:28.582Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"data_path\": \"/root/provenance_weight_training/data/scored_data.jsonl\",\n    \"data_count\": 371499,\n    \"model_name\": \"Qwen3-0.6B\",\n    \"seed\": 123,\n    \"checkpoint_source\": \"checkpoint-1500 (D012 fix)\",\n    \"eval_data\": \"/root/provenance_weight_training/data/human/eval_holdout.jsonl\",\n    \"wall_clock_seconds\": 10807.2,\n    \"gpu_hours\": 3.0\n  },\n  \"reproduce\": {\n    \"finished_at\": \"2026-05-14T20:41:22.910Z\"\n  },\n  \"completed_at\": \"\",\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_failed\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-14T17:38:38.735034+00:00\"\n      },\n      {\n        \"event\": \"on_complete\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-14T20:41:26.828424+00:00\"\n      }\n    ]\n  },\n  \"checkpoint_path\": \"/root/provenance_weight_training/output/models/adaptive_fix_seed123/final\",\n  \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed123.log\",\n  \"metrics\": {\n    \"eval_ppl_holdout\": 17.643,\n    \"eval_loss\": 2.8704,\n    \"eval_tokens\": 4077068,\n    \"train_loss_weighted\": 7.517,\n    \"train_runtime_s\": 10347,\n    \"total_steps\": 6103,\n    \"epoch\": 0.26,\n    \"b_star_mean\": 1.431,\n    \"b_star_median\": 0.88,\n    \"b_star_std\": 2.029,\n    \"b_star_min\": 0,\n    \"b_star_max\": 20,\n    \"b_star_pct_below_0.5\": 20.9,\n    \"b_star_pct_0.5_to_1\": 35.7,\n    \"b_star_pct_1_to_2\": 27.3,\n    \"b_star_pct_2_to_5\": 6.3,\n    \"b_star_pct_above_5\": 1.9,\n    \"b_star_count\": 25906,\n    \"b_star_p25\": 0.54,\n    \"b_star_p75\": 1.52,\n    \"b_star_pct_above_2\": 16.1,\n    \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"\n  }\n}\n\n=== adaptive_fix_seed456 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-14T13:32:31.779Z\",\n  \"updated_at\": \"2026-05-15T00:00:33.021Z\",\n  \"hypothesis\": \"D012 n_min fix (3\\u21922, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performance (baseline adaptive PPL=17.64, uniform PPL=17.70)\",\n  \"parent\": \"adaptive_seed456\",\n  \"notes\": \"\\u6700\\u7ec8\\u6e05\\u7406\\u540e\\u91cd\\u63d0\\u4ea4\\u3002\\u4ece checkpoint-1000 \\u6062\\u590d\\uff0c\\u65e0 inline eval\\u3002PID=127285\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/adaptive_fix_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model --resume_from_checkpoint output/models/adaptive_fix_seed456/checkpoint-1000\\\"\",\n    \"server\": \"westd-47453\",\n    \"gpu\": [\n      \"cuda:3\"\n    ],\n    \"pid\": \"127280\",\n    \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed456.log\",\n    \"submitted_at\": \"2026-05-14T17:47:33.774Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"wall_clock_seconds\": 12040.6,\n    \"gpu_hours\": 3.34\n  },\n  \"server\": \"westd-47453\",\n  \"gpu\": \"cuda:3\",\n  \"account\": \"root\",\n  \"pid\": \"115066\",\n  \"log_path\": \"~/runs/provenance_weight_training/adaptive_fix_seed456.log\",\n  \"reproduce\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --eval_data_path data/human/eval_holdout.jsonl --output_dir output/models/adaptive_fix_seed456 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --learning_rate 5e-5 --max_length 2048 --seed 456 --eval_steps 500 --save_steps 500 --logging_steps 10 --bf16 --save_total_limit 3 --save_only_model\\\"\",\n    \"finished_at\": \"2026-05-14T21:00:17.106Z\"\n  },\n  \"failure_reason\": \"\",\n  \"conclusion\": \"success\",\n  \"completed_at\": \"\",\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_failed\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-14T17:38:47.164099+00:00\"\n      },\n      {\n        \"event\": \"on_complete\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-14T21:00:18.079813+00:00\"\n      }\n    ]\n  },\n  \"metrics\": {\n    \"train_loss\": 8.3124,\n    \"train_runtime\": 11436.05,\n    \"train_samples_per_second\": 8.539,\n    \"train_steps_per_second\": 0.534,\n    \"total_steps\": 6103,\n    \"eval_loss_holdout\": 2.8711,\n    \"eval_ppl_holdout\": 17.66,\n    \"eval_tokens\": 4077068,\n    \"b_star_count\": 26396,\n    \"b_star_mean\": 1.416,\n    \"b_star_median\": 0.88,\n    \"b_star_std\": 1.993,\n    \"b_star_min\": 0,\n    \"b_star_max\": 20,\n    \"b_star_p25\": 0.54,\n    \"b_star_p75\": 1.52,\n    \"b_star_pct_below_0.5\": 20.9,\n    \"b_star_pct_0.5_to_1\": 35.7,\n    \"b_star_pct_1_to_2\": 27.3,\n    \"b_star_pct_above_2\": 16.1,\n    \"b_star_note\": \"Training-only records (eval checkpoint records with b*=0 excluded)\"\n  },\n  \"checkpoint_path\": \"output/models/adaptive_fix_seed456/final\"\n}\n\n=== nmin1_seed42 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-15T07:48:31.298Z\",\n  \"updated_at\": \"2026-05-15T14:36:49.692Z\",\n  \"hypothesis\": \"n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades with overly permissive ESS bound\",\n  \"server\": \"westd-47453\",\n  \"gpu\": \"cuda:2\",\n  \"account\": \"root\",\n  \"reproduce\": {\n    \"server\": \"westd-47453\",\n    \"gpu\": \"cuda:2\",\n    \"started_at\": \"2026-05-15T09:34:56.077Z\",\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\",\n    \"finished_at\": \"2026-05-15T14:27:21.174Z\",\n    \"training_hours\": 4.87\n  },\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin1_seed42 --weighting_method adaptive --n_min 1 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\",\n    \"server\": \"westd-47453\",\n    \"gpu\": [\n      \"cuda:2\"\n    ],\n    \"pid\": \"194005\",\n    \"log_path\": \"~/runs/provenance_weight_training/nmin1_seed42.log\",\n    \"submitted_at\": \"2026-05-15T09:36:06.479Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"wall_clock_seconds\": 18033.6,\n    \"gpu_hours\": 5.01\n  },\n  \"pid\": \"194005\",\n  \"log_path\": \"~/runs/provenance_weight_training/nmin1_seed42.log\",\n  \"extra\": {\n    \"hook_events\": [\n      {\n        \"event\": \"on_complete\",\n        \"action\": \"agent\",\n        \"ts\": \"2026-05-15T14:27:22.547409+00:00\"\n      }\n    ]\n  },\n  \"metrics\": {\n    \"eval_ppl_holdout\": 17.789,\n    \"eval_loss\": 2.8786,\n    \"eval_holdout_tokens\": 4077068,\n    \"b_star_mean\": 7.197,\n    \"b_star_median\": 1.746,\n    \"b_star_std\": 8.374,\n    \"b_star_min\": 0,\n    \"b_star_max\": 20,\n    \"b_star_p25\": 0.803,\n    \"b_star_p75\": 20,\n    \"b_star_zero_frac\": 0.019,\n    \"b_star_pct_below_0.5\": 13.1,\n    \"b_star_pct_0.5_to_1\": 19.1,\n    \"b_star_pct_1_to_2\": 21.1,\n    \"b_star_pct_above_2\": 46.7,\n    \"b_star_count\": 24412,\n    \"alpha_eff_mean\": 0.714,\n    \"alpha_eff_median\": 0.8\n  },\n  \"notes\": \"\\u8bad\\u7ec3\\u5b8c\\u6210(EXIT_CODE=0, 4h50m)\\u3002PPL=17.789\\uff0c\\u6bd4 adaptive_fix(n_min=2, 17.650) \\u5dee +0.139\\uff0c\\u6bd4 uniform(17.690) \\u5dee +0.099\\u3002n_min=1 \\u5bfc\\u81f4\\u6781\\u7aef b* \\u5206\\u5e03\\uff1a46.7% batch b*\\u22652\\uff0cp75=20.0(\\u4e0a\\u9650)\\uff0cmean=7.197\\u3002ESS \\u7ea6\\u675f\\u51e0\\u4e4e\\u5931\\u6548\\uff0cover-downweighting \\u660e\\u663e\\u3002confirms n_min=2 \\u662f\\u66f4\\u4f18\\u9009\\u62e9\\u3002\",\n  \"checkpoint_path\": \"/root/provenance_weight_training/output/models/nmin1_seed42\",\n  \"conclusion\": \"success\",\n  \"completed_at\": \"2026-05-15T14:36:40.056Z\"\n}\n\n=== nmin4_seed42 ===\n{\n  \"status\": \"PREPARING\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-15T14:36:45.229Z\",\n  \"updated_at\": \"2026-05-15T14:38:42.341Z\",\n  \"spec\": {\n    \"hypothesis\": \"n_min=4 (=batch_size) boundary case: maximal ESS constraint forces b*\\u21920 on most batches, testing if over-constrained adaptive degrades to near-uniform. Baseline: adaptive_fix n_min=2 PPL=17.650.\",\n    \"parent\": \"adaptive_fix_seed42\",\n    \"planned_gpu\": \"cuda:1\",\n    \"planned_command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && WANDB_MODE=disabled python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/nmin4_seed42 --weighting_method adaptive --n_min 4 --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --save_total_limit 2 --save_only_model --contamination_ratio 0.4 --tau 0.8 --bf16\\\"\"\n  },\n  \"hypothesis\": \"n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=batch_size. Should degrade to uniform-equivalent PPL (~17.69). Key boundary condition for n_min sensitivity analysis.\"\n}\n\n=== uniform_seed42 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-13T22:17:51.722Z\",\n  \"updated_at\": \"2026-05-14T07:27:34.800Z\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed42 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 42 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed42/checkpoint-500\\\"\",\n    \"server\": \"westd-47453\",\n    \"gpu\": [\n      \"cuda:1\"\n    ],\n    \"pid\": \"47603\",\n    \"log_path\": \"~/runs/provenance_weight_training/uniform_seed42.log\",\n    \"submitted_at\": \"2026-05-13T23:23:53.026Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\",\n    \"data_count\": 371499,\n    \"model_name\": \"Qwen/Qwen3-0.6B\",\n    \"seed\": 42,\n    \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed42/final/\",\n    \"wall_clock_seconds\": 12352.2,\n    \"gpu_hours\": 3.43\n  },\n  \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"train_loss\": 7.3104,\n    \"total_steps\": 6103,\n    \"train_duration_s\": 11946,\n    \"eval_ppl_holdout\": 17.69,\n    \"eval_holdout_tokens\": 4080000\n  },\n  \"completed_at\": \"2026-05-14T02:49:45.269Z\"\n}\n\n=== uniform_seed123 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-13T22:17:53.217Z\",\n  \"updated_at\": \"2026-05-14T07:27:35.749Z\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed123 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 123 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed123/checkpoint-500\\\"\",\n    \"server\": \"westd-47453\",\n    \"gpu\": [\n      \"cuda:2\"\n    ],\n    \"pid\": \"47749\",\n    \"log_path\": \"~/runs/provenance_weight_training/uniform_seed123.log\",\n    \"submitted_at\": \"2026-05-13T23:23:55.904Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\",\n    \"data_count\": 371499,\n    \"model_name\": \"Qwen/Qwen3-0.6B\",\n    \"seed\": 123,\n    \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed123/final/\",\n    \"wall_clock_seconds\": 12350.8,\n    \"gpu_hours\": 3.43\n  },\n  \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"train_loss\": 7.3121,\n    \"total_steps\": 6103,\n    \"train_duration_s\": 11994,\n    \"eval_ppl_holdout\": 17.69,\n    \"eval_holdout_tokens\": 4080000\n  },\n  \"completed_at\": \"2026-05-14T02:49:46.681Z\"\n}\n\n=== uniform_seed456 ===\n{\n  \"status\": \"DONE\",\n  \"retry_count\": 0,\n  \"created_at\": \"2026-05-13T22:17:55.165Z\",\n  \"updated_at\": \"2026-05-14T07:27:36.904Z\",\n  \"spec\": {\n    \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/mixed_data.jsonl --output_dir output/models/uniform_seed456 --weighting_method uniform --model_name models/Qwen/Qwen3-0.6B --num_train_tokens 200000000 --batch_size 4 --gradient_accumulation_steps 4 --max_length 2048 --learning_rate 5e-5 --seed 456 --logging_steps 10 --save_steps 500 --eval_steps 500 --save_total_limit 2 --save_only_model --resume_from_checkpoint output/models/uniform_seed456/checkpoint-500\\\"\",\n    \"server\": \"westd-47453\",\n    \"gpu\": [\n      \"cuda:3\"\n    ],\n    \"pid\": \"47890\",\n    \"log_path\": \"~/runs/provenance_weight_training/uniform_seed456.log\",\n    \"submitted_at\": \"2026-05-13T23:23:58.435Z\",\n    \"submitted_via\": \"submit_training_job\",\n    \"backend\": \"tmux\",\n    \"account\": \"root\",\n    \"data_path\": \"/root/provenance_weight_training/data/mixed_data.jsonl\",\n    \"data_count\": 371499,\n    \"model_name\": \"Qwen/Qwen3-0.6B\",\n    \"seed\": 456,\n    \"checkpoint_path\": \"/root/provenance_weight_training/output/models/uniform_seed456/final/\",\n    \"wall_clock_seconds\": 12349.2,\n    \"gpu_hours\": 3.43\n  },\n  \"hypothesis\": \"Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods\",\n  \"conclusion\": \"success\",\n  \"metrics\": {\n    \"train_loss\": 7.2895,\n    \"total_steps\": 6103,\n    \"train_duration_s\": 11974,\n    \"eval_ppl_holdout\": 17.7,\n    \"eval_holdout_tokens\": 4080000\n  },\n  \"completed_at\": \"2026-05-14T02:49:47.621Z\"\n}",
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

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the registry data. Let me compile the precise values:

**Registry values:**

**Uniform baselines:**
- uniform_seed42: PPL=17.69
- uniform_seed123: PPL=17.69
- uniform_seed456: PPL=17.70

Uniform mean = (17.69 + 17.69 + 17.70) / 3 = 17.693

**n_min=3 (adaptive, pre-D012):**
- adaptive_seed42: PPL=17.69, n_min=3, b_star="per-batch adaptive (0.0-3.8)", alpha_eff_range="0.03-0.80 (capped at tau)"


- adaptive_seed123: PPL=17.63, n_min=3, b_star="per-batch adaptive (0.0-3.8)", alpha_eff_range="0.04-0.80 (capped at tau)"
- adaptive_seed456: PPL=17.64, n_min=3, b_star="per-batch adaptive (0.0-3.8)", alpha_eff_range="0.09-0.80 (capped at tau)"

The n_min=3 configuration shows a mean perplexity of 17.653, which is slightly better than uniform, and I need to calculate the standard deviation to see the variance across seeds.

Computing the standard deviation for these three runs, I get a population std of 0.0263 and a sample std of 0.0322, indicating very tight clustering around the mean. Now looking at the n_min=2 results with the post-D012 adaptive fix, where adaptive_fix_seed42 achieves a PPL of 17.65. Looking at the results for n_min=1 and n_min=4, I see that n_min=1 has a PPL of 17.789 while n_min=4 is still preparing. Now examining the b_star statistics across different n_min values, I notice the means and medians vary considerably—n_min=2 clusters around b_star_mean values of 1.4-1.43, while n_min=1 shows much higher values at 7.197 for the mean and 1.746 for the median.

Checking the registry PPL values across seeds, I'm seeing some precision inconsistencies in how the results are recorded—n_min=3 has 2-decimal precision while n_min=2 shows mixed precision ranging from 2 to 3 decimals. Let me verify the exact registry values to ensure I'm comparing the right numbers. Looking at the existing table values more carefully, I can see the adaptive configurations are already populated with the correct metrics—the n_min fix variants show improved perplexity scores and additional performance indicators compared to the original versions. I'm looking at the performance metrics for the n_min variants and need to update the table labels to distinguish between the pre-D012 and post-D012 versions. Let me calculate the aggregate statistics for n_min=2 across the three seeds to establish the baseline for comparison. Now I'm finishing the standard deviation calculation for the n_min=3 case and comparing how the registry-based means deviate from the uniform mean across all three sample sizes. I'm checking the precision of the uniform baseline values from the registry—they're stored at two decimal places, which gives a mean of 17.6933. But I notice the task references slightly different numbers, so I need to verify whether I should use the exact registry values or if there's additional precision I'm missing from the reference table. Now I'm working through the precise calculations from the registry data. For the uniform distribution, the mean across the three values is 17.6933. With n_min=3, the mean drops to 17.6533, a difference of -0.040. With n_min=2, it's 17.651, which is -0.042 lower than uniform. For n_min=1, I'm getting 17.789, which would be about +0.096 higher.

For the standard deviation, I need to use Python to compute this accurately. Since I only have three data points, sample standard deviation with Bessel's correction makes more sense than population standard deviation. Computing the sample std for n_min=2 gives me 0.00854, and I'm working through the same calculation for n_min=3.

Now I'm verifying the ratio between these two standard deviations. The n_min=2 case is about 3.76 times more stable than n_min=3, which I can confirm by also checking with population standard deviation—the ratio stays consistent at 3.76x.

So my plan is to update the Adaptive Experiments table to clarify the n_min values, add a sensitivity analysis section before Key Findings, and enhance the stability details in the findings. Let me run a quick Python calculation to make sure everything's precise before making these edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "c142d212-f5af-4c65-917f-3e445d775d9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SANfs6jJv3hMUfJNyVr7Xb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11197,
      "cache_read_input_tokens": 31604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11197
      },
      "output_tokens": 9,
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

Got all registry data. Let me compute precise statistics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "3b145a10-6c38-49cc-b59f-2d136a50315e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SANfs6jJv3hMUfJNyVr7Xb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11197,
      "cache_read_input_tokens": 31604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11197
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Bash · `toolu_01SmErSAyRaxYRm6LrnL4qji`</summary>

```json
{
  "command": "python3 -c \"\nimport math\n\n# From registry\nuniform = [17.690, 17.690, 17.700]\nnmin2 = [17.650, 17.643, 17.660]\nnmin3 = [17.690, 17.630, 17.640]\nnmin1 = [17.789]\n\ndef stats(vals):\n    n = len(vals)\n    m = sum(vals) / n\n    if n < 2:\n        return m, None, None\n    pop_var = sum((x - m)**2 for x in vals) / n\n    samp_var = sum((x - m)**2 for x in vals) / (n - 1)\n    return m, math.sqrt(pop_var), math.sqrt(samp_var)\n\nu_mean, _, _ = stats(uniform)\nprint(f'Uniform mean: {u_mean:.4f}')\n\nfor name, vals in [('n_min=1', nmin1), ('n_min=2', nmin2), ('n_min=3', nmin3)]:\n    m, pop_std, samp_std = stats(vals)\n    delta = m - u_mean\n    print(f'{name}: mean={m:.3f}, pop_std={pop_std}, samp_std={samp_std}, vs_uniform={delta:+.3f}')\n\n# Stability ratio\n_, _, std2 = stats(nmin2)\n_, _, std3 = stats(nmin3)\nprint(f'Stability ratio (std3/std2): {std3/std2:.1f}x')\nprint(f'n_min=2 sample std: {std2:.4f}')\nprint(f'n_min=3 sample std: {std3:.4f}')\n\"\n",
  "description": "Compute precise statistics for n_min sensitivity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "14cbceb7-5088-4323-b700-c7d3df03229d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SANfs6jJv3hMUfJNyVr7Xb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11197,
      "cache_read_input_tokens": 31604,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11197
      },
      "output_tokens": 9,
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

_source line 28 · 2026-05-15T15:39:02.983Z_

<details><summary>↩ Tool result · `toolu_01SmErSAyRaxYRm6LrnL4qji`</summary>

```text
Uniform mean: 17.6933
n_min=1: mean=17.789, pop_std=None, samp_std=None, vs_uniform=+0.096
n_min=2: mean=17.651, pop_std=0.006976149845485318, samp_std=0.00854400374531737, vs_uniform=-0.042
n_min=3: mean=17.653, pop_std=0.026246692913373497, samp_std=0.03214550253664415, vs_uniform=-0.040
Stability ratio (std3/std2): 3.8x
n_min=2 sample std: 0.0085
n_min=3 sample std: 0.0321
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "64c54e06-5410-4649-a71a-a4bd5d711d11",
  "tool_use_result": {
    "stdout": "Uniform mean: 17.6933\nn_min=1: mean=17.789, pop_std=None, samp_std=None, vs_uniform=+0.096\nn_min=2: mean=17.651, pop_std=0.006976149845485318, samp_std=0.00854400374531737, vs_uniform=-0.042\nn_min=3: mean=17.653, pop_std=0.026246692913373497, samp_std=0.03214550253664415, vs_uniform=-0.040\nStability ratio (std3/std2): 3.8x\nn_min=2 sample std: 0.0085\nn_min=3 sample std: 0.0321",
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

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the precise values. Let me make the edits.

Precise values:
- Uniform mean: 17.693
- n_min=1: mean=17.789, vs uniform=+0.096
- n_min=2: mean=17.651, sample std=0.009, vs uniform=-0.042
- n_min=3: mean=17.653, sample std=0.032, vs uniform=-0.040
- Stability ratio: 3.8x

Now let me make the edits. I'll:


1. Update the Adaptive Experiments table variant labels
2. Update the notes below the table
3. Add n_min Sensitivity Analysis section before Key Findings
4. Update Key Findings item 4

Let me construct the edits carefully. I need to change the variant labels in the adaptive table from "original" to "n_min=3 (pre-D012)" and "n_min fix" to "n_min=2 (post-D012)". Looking at the current table structure, I'll need to make sure these labels fit properly in the variant column.

Updating the markdown table... Now I'm looking at the performance metrics across different model configurations, and I'm thinking it would be clearer to rename the experiment labels—calling the original runs "pre-D012" and the fixed versions "post-D012" since the n_min parameter is already factored into that distinction. I'm debating whether to include the n_min values in the variant column labels since that information already appears in its own column—ultimately, I'll go with "n_min=3 (pre-D012)" and "n_min=2 (post-D012)" as the task specifies, even though it creates some redundancy with the existing n_min column.

Now I need to update the note below the Adaptive table to reflect these new labels, then add a dedicated n_min sensitivity section before Key Findings with per-seed PPL comparisons and supporting analysis. Generating the comparison table... Generating markdown table...

The results show n_min=2 and n_min=3 produce nearly identical mean PPL (difference of just 0.002), well within the noise from individual seed variation, suggesting the adaptive method is fairly robust across these parameter choices. 动 ~0.04）
2. **n_min=2 跨 seed variance 显著更低**：std=0.009 vs std=0.032（3.8× 更稳定）
3. n_min=2 的 seed42 改善明显（17.690→17.650），消除了 n_min=3 时 seed42 的异常偏高（与 uniform 相同的 17.690）
4. n_min=1 明显恶化（+0.096 vs uniform），ESS 约束过松导致 46.7% batches b* 达到上限 20
5. **结论**：n_min=2 = batch_size//2 是最优选择，优势在稳定性（低 variance）而非均值

现在看 b* 分布的详细指标，n_min=2 在各个 seed 上的表现都很一致，中位数和分位数都远低于 n_min=1，进一步证实了 n_min=2 的稳定性优势。 I'm checking where "original" and "n_min fix" appear in the file to make sure my replacements are safe—they each show up three times in the table rows, which is exactly what I want to change. I also need to update the note that references these terms, so I'll handle that separately to avoid unintended changes elsewhere in the document. I'm settling on using "n_min=3 (pre-D012)" and "n_min=2 (post-D012)" as the variant labels to match what the task specifies, even though there's some redundancy with the n_min column already showing these values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "2b67f89e-48f1-4114-8e06-4ca22216c144",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpCfZ1yzpYxdNuXmTZs2rP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4805,
      "cache_read_input_tokens": 42801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4805
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

_source line 30_

Now I have precise values from registry. Let me make the edits.

Registry values confirmed:
- n_min=2: mean=17.651, sample std=0.009, vs uniform=-0.042
- n_min=3: mean=17.653, sample std=0.032, vs uniform=-0.040
- Stability ratio: 3.8x

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "85c6357c-ad93-4cdb-825b-9beee18ba698",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpCfZ1yzpYxdNuXmTZs2rP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4805,
      "cache_read_input_tokens": 42801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4805
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01JNQJ1Mmm52ZeAriRAboYn2`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
  "old_string": "| original |",
  "new_string": "| n_min=3 (pre-D012) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "4080c823-d927-45e6-9eed-c6ccc719a650",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpCfZ1yzpYxdNuXmTZs2rP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4805,
      "cache_read_input_tokens": 42801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4805
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

_source line 32 · 2026-05-15T15:39:59.349Z_

<details><summary>↩ Tool result · reported error · `toolu_01JNQJ1Mmm52ZeAriRAboYn2`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "bac617bc-ae93-4639-9d49-fd46ba2f8528",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01PyBHCGUSjReKc5erygYdbm`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
  "old_string": "| n_min fix |",
  "new_string": "| n_min=2 (post-D012) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "feed03ef-9cfc-4b6d-8e6b-b4fbf316dcd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpCfZ1yzpYxdNuXmTZs2rP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4805,
      "cache_read_input_tokens": 42801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4805
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

_source line 34 · 2026-05-15T15:40:00.313Z_

<details><summary>↩ Tool result · reported error · `toolu_01PyBHCGUSjReKc5erygYdbm`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "5f300506-6dea-4879-b60a-e7638adc95c5",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_011R9qxRsMkKDNvBh19TbKA4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "e95c9698-5280-414a-afbf-ccdf9c7253dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALVHtuDMsHQkpHN7UutB3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3901,
      "cache_read_input_tokens": 47606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3901
      },
      "output_tokens": 68,
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

_source line 36 · 2026-05-15T15:40:02.968Z_

<details><summary>↩ Tool result · `toolu_011R9qxRsMkKDNvBh19TbKA4`</summary>

```text
1	# All Successful Experiments Summary
2	
3	> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure
4	
5	---
6	
7	## Grid-b Experiments
8	
9	Fixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.
10	
11	| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |
12	|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|
13	| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |
14	| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |
15	| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |
16	| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |
17	| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |
18	| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |
19	| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |
20	| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |
21	| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |
22	| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |
23	| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |
24	| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |
25	| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |
26	| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |
27	| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |
28	| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |
29	| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |
30	| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |
31	
32	> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。
33	> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。
34	
35	---
36	
37	## Adaptive Experiments
38	
39	Per-batch adaptive b* via α_eff theory. Sorted by PPL ascending.
40	
41	| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |
42	|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|
43	| adaptive_seed123 | original | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |
44	| adaptive_seed456 | original | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |
45	| adaptive_fix_seed123 | n_min fix | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |
46	| adaptive_fix_seed42 | n_min fix | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |
47	| adaptive_fix_seed456 | n_min fix | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |
48	| adaptive_seed42 | original | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |
49	
50	> "original" = n_min=3 bug (batch_size-1)。"n_min fix" = D012 修复后 n_min=max(2, batch_size//2)。
51	> original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。
52	> adaptive_fix b* 分布：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。
53	
54	---
55	
56	## Ablation Experiments
57	
58	Single-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.
59	
60	| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |
61	|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|
62	| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |
63	| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |
64	| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |
65	
66	> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。
67	> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。
68	> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。
69	
70	---
71	
72	## Baseline Experiments
73	
74	Uniform weighting (no provenance information). Sorted by PPL ascending.
75	
76	| exp_id | seed | PPL | eval_loss | gpu_hours |
77	|--------|------|-----|-----------|-----------|
78	| uniform_seed42 | 42 | 17.690 | - | 3.43 |
79	| uniform_seed123 | 123 | 17.690 | - | 3.43 |
80	| uniform_seed456 | 456 | 17.700 | - | 3.43 |
81	
82	---
83	
84	## Infrastructure Experiments (non-training)
85	
86	| exp_id | 类型 | 关键指标 |
87	|--------|------|---------|
88	| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |
89	| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |
90	
91	---
92	
93	## Key Findings
94	
95	1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。
96	
97	2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。
98	
99	3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。
100	
101	4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。
102	
103	5. **Adaptive_fix (PPL=17.650) 略优于 golden ratio oracle (PPL=17.654)。** adaptive_fix 在不使用真实标签的情况下即可达到甚至超越已知比例的 oracle 水平，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。
104	
105	---
106	
107	## PPL Ratio Reference
108	
109	| 方法 | seed42 | seed123 | seed456 | mean |
110	|------|--------|---------|---------|------|
111	| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
112	| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |
113	| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |
114	| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |
115	| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |
116	| golden_ratio oracle | 0.9980 | - | - | - |
117	| ess_only | 1.0023 | - | - | - |
118	| nmin1 | 1.0056 | - | - | - |
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "5df81847-547e-43f3-af9f-2428c4d22d5e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
      "content": "# All Successful Experiments Summary\n\n> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure\n\n---\n\n## Grid-b Experiments\n\nFixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.\n\n| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|\n| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |\n| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |\n| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |\n| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |\n| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |\n| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |\n| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |\n| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |\n| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |\n| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |\n| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |\n| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |\n| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |\n| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |\n| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |\n| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |\n| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |\n| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |\n\n> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。\n> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。\n\n---\n\n## Adaptive Experiments\n\nPer-batch adaptive b* via α_eff theory. Sorted by PPL ascending.\n\n| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|\n| adaptive_seed123 | original | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |\n| adaptive_seed456 | original | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |\n| adaptive_fix_seed123 | n_min fix | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |\n| adaptive_fix_seed42 | n_min fix | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |\n| adaptive_fix_seed456 | n_min fix | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |\n| adaptive_seed42 | original | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |\n\n> \"original\" = n_min=3 bug (batch_size-1)。\"n_min fix\" = D012 修复后 n_min=max(2, batch_size//2)。\n> original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。\n> adaptive_fix b* 分布：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。\n\n---\n\n## Ablation Experiments\n\nSingle-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.\n\n| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |\n|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|\n| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |\n| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |\n| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |\n\n> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。\n> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。\n> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。\n\n---\n\n## Baseline Experiments\n\nUniform weighting (no provenance information). Sorted by PPL ascending.\n\n| exp_id | seed | PPL | eval_loss | gpu_hours |\n|--------|------|-----|-----------|-----------|\n| uniform_seed42 | 42 | 17.690 | - | 3.43 |\n| uniform_seed123 | 123 | 17.690 | - | 3.43 |\n| uniform_seed456 | 456 | 17.700 | - | 3.43 |\n\n---\n\n## Infrastructure Experiments (non-training)\n\n| exp_id | 类型 | 关键指标 |\n|--------|------|---------|\n| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |\n| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |\n\n---\n\n## Key Findings\n\n1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。\n\n2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。\n\n3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。\n\n4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。\n\n5. **Adaptive_fix (PPL=17.650) 略优于 golden ratio oracle (PPL=17.654)。** adaptive_fix 在不使用真实标签的情况下即可达到甚至超越已知比例的 oracle 水平，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。\n\n---\n\n## PPL Ratio Reference\n\n| 方法 | seed42 | seed123 | seed456 | mean |\n|------|--------|---------|---------|------|\n| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |\n| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |\n| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |\n| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |\n| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |\n| golden_ratio oracle | 0.9980 | - | - | - |\n| ess_only | 1.0023 | - | - | - |\n| nmin1 | 1.0056 | - | - | - |\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Now let me make all the edits. I'll do them sequentially since some depend on the same file area.

Edit 1: Replace variant labels in adaptive table
Edit 2: Replace note below adaptive table
Edit 3: Insert n_min sensitivity section before Key Findings
Edit 4: Update Key Findings item 4

Let me do edits 1 and 2 first (they're in separate locations).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "11c632da-e1c1-44e7-9efc-c9879206a7c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rpp9f1cpwo2H3qVX9kcGDZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3666,
      "cache_read_input_tokens": 51507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3666
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Edit · `toolu_01A7GP8o5ak6fp6Df66WZghj`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
  "old_string": "| original |",
  "new_string": "| n_min=3 (pre-D012) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "eb4135f1-c19a-4471-acea-31d9ccc6df9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rpp9f1cpwo2H3qVX9kcGDZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3666,
      "cache_read_input_tokens": 51507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3666
      },
      "output_tokens": 9,
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

_source line 39 · 2026-05-15T15:40:08.500Z_

<details><summary>↩ Tool result · `toolu_01A7GP8o5ak6fp6Df66WZghj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "5deda154-4d02-4adc-a02b-e93ee0896e3f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
    "oldString": "| original |",
    "newString": "| n_min=3 (pre-D012) |",
    "originalFile": "# All Successful Experiments Summary\n\n> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure\n\n---\n\n## Grid-b Experiments\n\nFixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.\n\n| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|\n| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |\n| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |\n| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |\n| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |\n| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |\n| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |\n| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |\n| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |\n| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |\n| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |\n| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |\n| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |\n| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |\n| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |\n| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |\n| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |\n| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |\n| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |\n\n> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。\n> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。\n\n---\n\n## Adaptive Experiments\n\nPer-batch adaptive b* via α_eff theory. Sorted by PPL ascending.\n\n| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|\n| adaptive_seed123 | original | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |\n| adaptive_seed456 | original | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |\n| adaptive_fix_seed123 | n_min fix | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |\n| adaptive_fix_seed42 | n_min fix | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |\n| adaptive_fix_seed456 | n_min fix | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |\n| adaptive_seed42 | original | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |\n\n> \"original\" = n_min=3 bug (batch_size-1)。\"n_min fix\" = D012 修复后 n_min=max(2, batch_size//2)。\n> original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。\n> adaptive_fix b* 分布：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。\n\n---\n\n## Ablation Experiments\n\nSingle-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.\n\n| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |\n|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|\n| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |\n| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |\n| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |\n\n> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。\n> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。\n> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。\n\n---\n\n## Baseline Experiments\n\nUniform weighting (no provenance information). Sorted by PPL ascending.\n\n| exp_id | seed | PPL | eval_loss | gpu_hours |\n|--------|------|-----|-----------|-----------|\n| uniform_seed42 | 42 | 17.690 | - | 3.43 |\n| uniform_seed123 | 123 | 17.690 | - | 3.43 |\n| uniform_seed456 | 456 | 17.700 | - | 3.43 |\n\n---\n\n## Infrastructure Experiments (non-training)\n\n| exp_id | 类型 | 关键指标 |\n|--------|------|---------|\n| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |\n| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |\n\n---\n\n## Key Findings\n\n1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。\n\n2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。\n\n3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。\n\n4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。\n\n5. **Adaptive_fix (PPL=17.650) 略优于 golden ratio oracle (PPL=17.654)。** adaptive_fix 在不使用真实标签的情况下即可达到甚至超越已知比例的 oracle 水平，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。\n\n---\n\n## PPL Ratio Reference\n\n| 方法 | seed42 | seed123 | seed456 | mean |\n|------|--------|---------|---------|------|\n| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |\n| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |\n| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |\n| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |\n| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |\n| golden_ratio oracle | 0.9980 | - | - | - |\n| ess_only | 1.0023 | - | - | - |\n| nmin1 | 1.0056 | - | - | - |\n",
    "structuredPatch": [
      {
        "oldStart": 40,
        "oldLines": 12,
        "newStart": 40,
        "newLines": 12,
        "lines": [
          " ",
          " | exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |",
          " |--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|",
          "-| adaptive_seed123 | original | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |",
          "-| adaptive_seed456 | original | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |",
          "+| adaptive_seed123 | n_min=3 (pre-D012) | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |",
          "+| adaptive_seed456 | n_min=3 (pre-D012) | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |",
          " | adaptive_fix_seed123 | n_min fix | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |",
          " | adaptive_fix_seed42 | n_min fix | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |",
          " | adaptive_fix_seed456 | n_min fix | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |",
          "-| adaptive_seed42 | original | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |",
          "+| adaptive_seed42 | n_min=3 (pre-D012) | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |",
          " ",
          " > \"original\" = n_min=3 bug (batch_size-1)。\"n_min fix\" = D012 修复后 n_min=max(2, batch_size//2)。",
          " > original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Edit · `toolu_016NixaAn2BLsukEtoosNhNL`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
  "old_string": "| n_min fix |",
  "new_string": "| n_min=2 (post-D012) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "45e2bf11-6ac8-45f8-8dc3-fed82ed361fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjixEtouHD1qCiK2EQhHj9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 55173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 333
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

_source line 41 · 2026-05-15T15:40:11.937Z_

<details><summary>↩ Tool result · `toolu_016NixaAn2BLsukEtoosNhNL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "dcf9a7bd-f89c-48de-a744-89fd12bb296c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
    "oldString": "| n_min fix |",
    "newString": "| n_min=2 (post-D012) |",
    "originalFile": "# All Successful Experiments Summary\n\n> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure\n\n---\n\n## Grid-b Experiments\n\nFixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.\n\n| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|\n| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |\n| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |\n| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |\n| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |\n| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |\n| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |\n| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |\n| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |\n| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |\n| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |\n| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |\n| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |\n| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |\n| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |\n| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |\n| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |\n| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |\n| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |\n\n> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。\n> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。\n\n---\n\n## Adaptive Experiments\n\nPer-batch adaptive b* via α_eff theory. Sorted by PPL ascending.\n\n| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|\n| adaptive_seed123 | n_min=3 (pre-D012) | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |\n| adaptive_seed456 | n_min=3 (pre-D012) | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |\n| adaptive_fix_seed123 | n_min fix | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |\n| adaptive_fix_seed42 | n_min fix | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |\n| adaptive_fix_seed456 | n_min fix | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |\n| adaptive_seed42 | n_min=3 (pre-D012) | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |\n\n> \"original\" = n_min=3 bug (batch_size-1)。\"n_min fix\" = D012 修复后 n_min=max(2, batch_size//2)。\n> original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。\n> adaptive_fix b* 分布：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。\n\n---\n\n## Ablation Experiments\n\nSingle-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.\n\n| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |\n|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|\n| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |\n| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |\n| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |\n\n> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。\n> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。\n> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。\n\n---\n\n## Baseline Experiments\n\nUniform weighting (no provenance information). Sorted by PPL ascending.\n\n| exp_id | seed | PPL | eval_loss | gpu_hours |\n|--------|------|-----|-----------|-----------|\n| uniform_seed42 | 42 | 17.690 | - | 3.43 |\n| uniform_seed123 | 123 | 17.690 | - | 3.43 |\n| uniform_seed456 | 456 | 17.700 | - | 3.43 |\n\n---\n\n## Infrastructure Experiments (non-training)\n\n| exp_id | 类型 | 关键指标 |\n|--------|------|---------|\n| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |\n| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |\n\n---\n\n## Key Findings\n\n1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。\n\n2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。\n\n3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。\n\n4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。\n\n5. **Adaptive_fix (PPL=17.650) 略优于 golden ratio oracle (PPL=17.654)。** adaptive_fix 在不使用真实标签的情况下即可达到甚至超越已知比例的 oracle 水平，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。\n\n---\n\n## PPL Ratio Reference\n\n| 方法 | seed42 | seed123 | seed456 | mean |\n|------|--------|---------|---------|------|\n| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |\n| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |\n| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |\n| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |\n| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |\n| golden_ratio oracle | 0.9980 | - | - | - |\n| ess_only | 1.0023 | - | - | - |\n| nmin1 | 1.0056 | - | - | - |\n",
    "structuredPatch": [
      {
        "oldStart": 42,
        "oldLines": 9,
        "newStart": 42,
        "newLines": 9,
        "lines": [
          " |--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|",
          " | adaptive_seed123 | n_min=3 (pre-D012) | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |",
          " | adaptive_seed456 | n_min=3 (pre-D012) | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |",
          "-| adaptive_fix_seed123 | n_min fix | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |",
          "-| adaptive_fix_seed42 | n_min fix | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |",
          "-| adaptive_fix_seed456 | n_min fix | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |",
          "+| adaptive_fix_seed123 | n_min=2 (post-D012) | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |",
          "+| adaptive_fix_seed42 | n_min=2 (post-D012) | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |",
          "+| adaptive_fix_seed456 | n_min=2 (post-D012) | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |",
          " | adaptive_seed42 | n_min=3 (pre-D012) | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |",
          " ",
          " > \"original\" = n_min=3 bug (batch_size-1)。\"n_min fix\" = D012 修复后 n_min=max(2, batch_size//2)。"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01AWEHeApR2JeinxSDuTwnum`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
  "old_string": "> \"original\" = n_min=3 bug (batch_size-1)。\"n_min fix\" = D012 修复后 n_min=max(2, batch_size//2)。\n> original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。\n> adaptive_fix b* 分布：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。",
  "new_string": "> \"n_min=3 (pre-D012)\" = D012 修复前 n_min=batch_size-1=3。\"n_min=2 (post-D012)\" = D012 修复后 n_min=max(2, batch_size//2)=2。\n> pre-D012 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串 \"0.0–3.8\"）。\n> post-D012 b* 分布（3 seeds 一致）：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "30c6084b-256b-49db-ab75-88d7e7b551bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpBC3mUt6WsqQ19TGSztYX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 55506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 228
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

_source line 43 · 2026-05-15T15:40:18.174Z_

<details><summary>↩ Tool result · `toolu_01AWEHeApR2JeinxSDuTwnum`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "b863dc5d-9db5-45f4-814f-d7c6f2406ce7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
    "oldString": "> \"original\" = n_min=3 bug (batch_size-1)。\"n_min fix\" = D012 修复后 n_min=max(2, batch_size//2)。\n> original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。\n> adaptive_fix b* 分布：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。",
    "newString": "> \"n_min=3 (pre-D012)\" = D012 修复前 n_min=batch_size-1=3。\"n_min=2 (post-D012)\" = D012 修复后 n_min=max(2, batch_size//2)=2。\n> pre-D012 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串 \"0.0–3.8\"）。\n> post-D012 b* 分布（3 seeds 一致）：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。",
    "originalFile": "# All Successful Experiments Summary\n\n> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure\n\n---\n\n## Grid-b Experiments\n\nFixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.\n\n| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|\n| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |\n| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |\n| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |\n| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |\n| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |\n| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |\n| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |\n| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |\n| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |\n| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |\n| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |\n| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |\n| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |\n| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |\n| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |\n| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |\n| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |\n| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |\n\n> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。\n> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。\n\n---\n\n## Adaptive Experiments\n\nPer-batch adaptive b* via α_eff theory. Sorted by PPL ascending.\n\n| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|\n| adaptive_seed123 | n_min=3 (pre-D012) | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |\n| adaptive_seed456 | n_min=3 (pre-D012) | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |\n| adaptive_fix_seed123 | n_min=2 (post-D012) | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |\n| adaptive_fix_seed42 | n_min=2 (post-D012) | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |\n| adaptive_fix_seed456 | n_min=2 (post-D012) | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |\n| adaptive_seed42 | n_min=3 (pre-D012) | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |\n\n> \"original\" = n_min=3 bug (batch_size-1)。\"n_min fix\" = D012 修复后 n_min=max(2, batch_size//2)。\n> original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。\n> adaptive_fix b* 分布：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。\n\n---\n\n## Ablation Experiments\n\nSingle-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.\n\n| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |\n|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|\n| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |\n| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |\n| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |\n\n> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。\n> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。\n> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。\n\n---\n\n## Baseline Experiments\n\nUniform weighting (no provenance information). Sorted by PPL ascending.\n\n| exp_id | seed | PPL | eval_loss | gpu_hours |\n|--------|------|-----|-----------|-----------|\n| uniform_seed42 | 42 | 17.690 | - | 3.43 |\n| uniform_seed123 | 123 | 17.690 | - | 3.43 |\n| uniform_seed456 | 456 | 17.700 | - | 3.43 |\n\n---\n\n## Infrastructure Experiments (non-training)\n\n| exp_id | 类型 | 关键指标 |\n|--------|------|---------|\n| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |\n| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |\n\n---\n\n## Key Findings\n\n1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。\n\n2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。\n\n3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。\n\n4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。\n\n5. **Adaptive_fix (PPL=17.650) 略优于 golden ratio oracle (PPL=17.654)。** adaptive_fix 在不使用真实标签的情况下即可达到甚至超越已知比例的 oracle 水平，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。\n\n---\n\n## PPL Ratio Reference\n\n| 方法 | seed42 | seed123 | seed456 | mean |\n|------|--------|---------|---------|------|\n| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |\n| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |\n| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |\n| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |\n| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |\n| golden_ratio oracle | 0.9980 | - | - | - |\n| ess_only | 1.0023 | - | - | - |\n| nmin1 | 1.0056 | - | - | - |\n",
    "structuredPatch": [
      {
        "oldStart": 47,
        "oldLines": 9,
        "newStart": 47,
        "newLines": 9,
        "lines": [
          " | adaptive_fix_seed456 | n_min=2 (post-D012) | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |",
          " | adaptive_seed42 | n_min=3 (pre-D012) | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |",
          " ",
          "-> \"original\" = n_min=3 bug (batch_size-1)。\"n_min fix\" = D012 修复后 n_min=max(2, batch_size//2)。",
          "-> original 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串）。",
          "-> adaptive_fix b* 分布：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。",
          "+> \"n_min=3 (pre-D012)\" = D012 修复前 n_min=batch_size-1=3。\"n_min=2 (post-D012)\" = D012 修复后 n_min=max(2, batch_size//2)=2。",
          "+> pre-D012 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串 \"0.0–3.8\"）。",
          "+> post-D012 b* 分布（3 seeds 一致）：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。",
          " ",
          " ---",
          " "
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

_source line 44_

Now add the n_min Sensitivity Analysis section before Key Findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "d861225c-7a11-4541-a710-79c9b7aa6f9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ASUCULyMNhkTpARdTu3hw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 55734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 517
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

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_012yQx8S6ECYKQkKKazuqqJp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
  "old_string": "## Key Findings",
  "new_string": "## n_min Sensitivity Analysis\n\nAdaptive method with varying n_min (minimum effective sample size constraint). Uniform baseline mean PPL = 17.693 (3 seeds).\n\n### Per-seed PPL Comparison\n\n| n_min | seed42 | seed123 | seed456 | mean | std (sample) | vs uniform mean |\n|-------|--------|---------|---------|------|--------------|-----------------|\n| 1 | 17.789 | — | — | 17.789 | — | +0.096 |\n| 2 | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 | −0.042 |\n| 3 | 17.690 | 17.630 | 17.640 | 17.653 | 0.032 | −0.040 |\n| 4 | pending | — | — | — | — | — |\n\n> std = sample standard deviation (ddof=1, n=3)。n_min=1/4 仅有 seed42，无法计算 std。\n\n### Key Observations\n\n1. **n_min=2 vs n_min=3 均值差仅 0.002**（17.651 vs 17.653），在 seed 噪声范围内（单 seed 波动 ~0.04）\n2. **n_min=2 跨 seed variance 显著更低**：std=0.009 vs std=0.032（3.8× 更稳定）\n3. n_min=2 的 seed42 改善明显（17.690→17.650），消除了 n_min=3 时 seed42 的异常偏高（与 uniform 持平的 17.690）\n4. n_min=1 明显恶化（+0.096 vs uniform），ESS 约束过松导致 46.7% batches b* 达到上限 20，over-downweighting 严重\n5. **结论**：n_min=2 (= batch_size//2) 是最优选择，优势在稳定性（低 variance）而非均值（均值差在噪声范围内）\n\n### b* Distribution Comparison\n\n| n_min | seed | b* mean | b* median | b* std | b* p25 | b* p75 | % b*≥2 |\n|-------|------|---------|-----------|--------|--------|--------|--------|\n| 1 | 42 | 7.197 | 1.746 | 8.374 | 0.803 | 20.000 | 46.7% |\n| 2 | 42 | 1.399 | 0.871 | 1.933 | 0.540 | 1.512 | 16.1% |\n| 2 | 123 | 1.431 | 0.880 | 2.029 | 0.540 | 1.520 | 16.1% |\n| 2 | 456 | 1.416 | 0.880 | 1.993 | 0.540 | 1.520 | 16.1% |\n| 3 | all | — | — | — | — | — | — |\n\n> n_min=3 (pre-D012) 仅记录了 b* range \"0.0–3.8\"，无详细分布统计。\n> n_min=1 的极端 b* 分布（mean=7.2, p75=20.0 即上限, 46.7% 达上限）解释了其 PPL 恶化：过多 batch 被过度降权。\n> n_min=2 的 b* 分布跨 3 seeds 高度一致（mean 1.40–1.43, median 0.87–0.88），与 PPL 低 variance 吻合。\n\n---\n\n## Key Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "23e7ee4e-b2ac-4063-8322-ae7669a94168",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ASUCULyMNhkTpARdTu3hw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 55734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 517
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

_source line 46 · 2026-05-15T15:40:39.049Z_

<details><summary>↩ Tool result · `toolu_012yQx8S6ECYKQkKKazuqqJp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "9d6080df-40e8-4063-91b3-e39a0c03c0e7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
    "oldString": "## Key Findings",
    "newString": "## n_min Sensitivity Analysis\n\nAdaptive method with varying n_min (minimum effective sample size constraint). Uniform baseline mean PPL = 17.693 (3 seeds).\n\n### Per-seed PPL Comparison\n\n| n_min | seed42 | seed123 | seed456 | mean | std (sample) | vs uniform mean |\n|-------|--------|---------|---------|------|--------------|-----------------|\n| 1 | 17.789 | — | — | 17.789 | — | +0.096 |\n| 2 | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 | −0.042 |\n| 3 | 17.690 | 17.630 | 17.640 | 17.653 | 0.032 | −0.040 |\n| 4 | pending | — | — | — | — | — |\n\n> std = sample standard deviation (ddof=1, n=3)。n_min=1/4 仅有 seed42，无法计算 std。\n\n### Key Observations\n\n1. **n_min=2 vs n_min=3 均值差仅 0.002**（17.651 vs 17.653），在 seed 噪声范围内（单 seed 波动 ~0.04）\n2. **n_min=2 跨 seed variance 显著更低**：std=0.009 vs std=0.032（3.8× 更稳定）\n3. n_min=2 的 seed42 改善明显（17.690→17.650），消除了 n_min=3 时 seed42 的异常偏高（与 uniform 持平的 17.690）\n4. n_min=1 明显恶化（+0.096 vs uniform），ESS 约束过松导致 46.7% batches b* 达到上限 20，over-downweighting 严重\n5. **结论**：n_min=2 (= batch_size//2) 是最优选择，优势在稳定性（低 variance）而非均值（均值差在噪声范围内）\n\n### b* Distribution Comparison\n\n| n_min | seed | b* mean | b* median | b* std | b* p25 | b* p75 | % b*≥2 |\n|-------|------|---------|-----------|--------|--------|--------|--------|\n| 1 | 42 | 7.197 | 1.746 | 8.374 | 0.803 | 20.000 | 46.7% |\n| 2 | 42 | 1.399 | 0.871 | 1.933 | 0.540 | 1.512 | 16.1% |\n| 2 | 123 | 1.431 | 0.880 | 2.029 | 0.540 | 1.520 | 16.1% |\n| 2 | 456 | 1.416 | 0.880 | 1.993 | 0.540 | 1.520 | 16.1% |\n| 3 | all | — | — | — | — | — | — |\n\n> n_min=3 (pre-D012) 仅记录了 b* range \"0.0–3.8\"，无详细分布统计。\n> n_min=1 的极端 b* 分布（mean=7.2, p75=20.0 即上限, 46.7% 达上限）解释了其 PPL 恶化：过多 batch 被过度降权。\n> n_min=2 的 b* 分布跨 3 seeds 高度一致（mean 1.40–1.43, median 0.87–0.88），与 PPL 低 variance 吻合。\n\n---\n\n## Key Findings",
    "originalFile": "# All Successful Experiments Summary\n\n> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure\n\n---\n\n## Grid-b Experiments\n\nFixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.\n\n| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|\n| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |\n| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |\n| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |\n| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |\n| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |\n| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |\n| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |\n| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |\n| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |\n| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |\n| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |\n| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |\n| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |\n| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |\n| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |\n| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |\n| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |\n| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |\n\n> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。\n> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。\n\n---\n\n## Adaptive Experiments\n\nPer-batch adaptive b* via α_eff theory. Sorted by PPL ascending.\n\n| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|\n| adaptive_seed123 | n_min=3 (pre-D012) | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |\n| adaptive_seed456 | n_min=3 (pre-D012) | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |\n| adaptive_fix_seed123 | n_min=2 (post-D012) | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |\n| adaptive_fix_seed42 | n_min=2 (post-D012) | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |\n| adaptive_fix_seed456 | n_min=2 (post-D012) | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |\n| adaptive_seed42 | n_min=3 (pre-D012) | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |\n\n> \"n_min=3 (pre-D012)\" = D012 修复前 n_min=batch_size-1=3。\"n_min=2 (post-D012)\" = D012 修复后 n_min=max(2, batch_size//2)=2。\n> pre-D012 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串 \"0.0–3.8\"）。\n> post-D012 b* 分布（3 seeds 一致）：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。\n\n---\n\n## Ablation Experiments\n\nSingle-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.\n\n| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |\n|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|\n| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |\n| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |\n| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |\n\n> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。\n> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。\n> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。\n\n---\n\n## Baseline Experiments\n\nUniform weighting (no provenance information). Sorted by PPL ascending.\n\n| exp_id | seed | PPL | eval_loss | gpu_hours |\n|--------|------|-----|-----------|-----------|\n| uniform_seed42 | 42 | 17.690 | - | 3.43 |\n| uniform_seed123 | 123 | 17.690 | - | 3.43 |\n| uniform_seed456 | 456 | 17.700 | - | 3.43 |\n\n---\n\n## Infrastructure Experiments (non-training)\n\n| exp_id | 类型 | 关键指标 |\n|--------|------|---------|\n| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |\n| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |\n\n---\n\n## Key Findings\n\n1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。\n\n2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。\n\n3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。\n\n4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。\n\n5. **Adaptive_fix (PPL=17.650) 略优于 golden ratio oracle (PPL=17.654)。** adaptive_fix 在不使用真实标签的情况下即可达到甚至超越已知比例的 oracle 水平，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。\n\n---\n\n## PPL Ratio Reference\n\n| 方法 | seed42 | seed123 | seed456 | mean |\n|------|--------|---------|---------|------|\n| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |\n| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |\n| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |\n| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |\n| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |\n| golden_ratio oracle | 0.9980 | - | - | - |\n| ess_only | 1.0023 | - | - | - |\n| nmin1 | 1.0056 | - | - | - |\n",
    "structuredPatch": [
      {
        "oldStart": 90,
        "oldLines": 6,
        "newStart": 90,
        "newLines": 45,
        "lines": [
          " ",
          " ---",
          " ",
          "+## n_min Sensitivity Analysis",
          "+",
          "+Adaptive method with varying n_min (minimum effective sample size constraint). Uniform baseline mean PPL = 17.693 (3 seeds).",
          "+",
          "+### Per-seed PPL Comparison",
          "+",
          "+| n_min | seed42 | seed123 | seed456 | mean | std (sample) | vs uniform mean |",
          "+|-------|--------|---------|---------|------|--------------|-----------------|",
          "+| 1 | 17.789 | — | — | 17.789 | — | +0.096 |",
          "+| 2 | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 | −0.042 |",
          "+| 3 | 17.690 | 17.630 | 17.640 | 17.653 | 0.032 | −0.040 |",
          "+| 4 | pending | — | — | — | — | — |",
          "+",
          "+> std = sample standard deviation (ddof=1, n=3)。n_min=1/4 仅有 seed42，无法计算 std。",
          "+",
          "+### Key Observations",
          "+",
          "+1. **n_min=2 vs n_min=3 均值差仅 0.002**（17.651 vs 17.653），在 seed 噪声范围内（单 seed 波动 ~0.04）",
          "+2. **n_min=2 跨 seed variance 显著更低**：std=0.009 vs std=0.032（3.8× 更稳定）",
          "+3. n_min=2 的 seed42 改善明显（17.690→17.650），消除了 n_min=3 时 seed42 的异常偏高（与 uniform 持平的 17.690）",
          "+4. n_min=1 明显恶化（+0.096 vs uniform），ESS 约束过松导致 46.7% batches b* 达到上限 20，over-downweighting 严重",
          "+5. **结论**：n_min=2 (= batch_size//2) 是最优选择，优势在稳定性（低 variance）而非均值（均值差在噪声范围内）",
          "+",
          "+### b* Distribution Comparison",
          "+",
          "+| n_min | seed | b* mean | b* median | b* std | b* p25 | b* p75 | % b*≥2 |",
          "+|-------|------|---------|-----------|--------|--------|--------|--------|",
          "+| 1 | 42 | 7.197 | 1.746 | 8.374 | 0.803 | 20.000 | 46.7% |",
          "+| 2 | 42 | 1.399 | 0.871 | 1.933 | 0.540 | 1.512 | 16.1% |",
          "+| 2 | 123 | 1.431 | 0.880 | 2.029 | 0.540 | 1.520 | 16.1% |",
          "+| 2 | 456 | 1.416 | 0.880 | 1.993 | 0.540 | 1.520 | 16.1% |",
          "+| 3 | all | — | — | — | — | — | — |",
          "+",
          "+> n_min=3 (pre-D012) 仅记录了 b* range \"0.0–3.8\"，无详细分布统计。",
          "+> n_min=1 的极端 b* 分布（mean=7.2, p75=20.0 即上限, 46.7% 达上限）解释了其 PPL 恶化：过多 batch 被过度降权。",
          "+> n_min=2 的 b* 分布跨 3 seeds 高度一致（mean 1.40–1.43, median 0.87–0.88），与 PPL 低 variance 吻合。",
          "+",
          "+---",
          "+",
          " ## Key Findings",
          " ",
          " 1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。"
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

_source line 47_

Now update Key Findings item 4 with richer n_min sensitivity insight.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "435cd992-383c-4e1e-861f-fbe3ed6b8064",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRQEoYg61iBUeMN8qnicfn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1323,
      "cache_read_input_tokens": 56251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1323
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

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_015iZYYtcqFvLPD9CsMVmPiQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
  "old_string": "4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。",
  "new_string": "4. **n_min 敏感性：n_min=2 的优势在稳定性而非均值。** n_min=2 vs n_min=3 均值差仅 0.002（17.651 vs 17.653，噪声范围内），但跨 seed std 从 0.032 降至 0.009（3.8× 更稳定）。n_min=2 消除了 n_min=3 时 seed42 的异常偏高（17.690→17.650）。n_min=1 明显恶化（PPL=17.789, +0.096 vs uniform），ESS 约束过松导致 46.7% batches 过度降权。n_min=2 (= batch_size//2) 在稳定性和干预力度间取得最优平衡。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "12960505-eeb7-4aca-b984-c66b28676b94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRQEoYg61iBUeMN8qnicfn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1323,
      "cache_read_input_tokens": 56251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1323
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

_source line 49 · 2026-05-15T15:40:46.437Z_

<details><summary>↩ Tool result · `toolu_015iZYYtcqFvLPD9CsMVmPiQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "a1e6934e-561f-441a-b1d2-fdf866040c30",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
    "oldString": "4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。",
    "newString": "4. **n_min 敏感性：n_min=2 的优势在稳定性而非均值。** n_min=2 vs n_min=3 均值差仅 0.002（17.651 vs 17.653，噪声范围内），但跨 seed std 从 0.032 降至 0.009（3.8× 更稳定）。n_min=2 消除了 n_min=3 时 seed42 的异常偏高（17.690→17.650）。n_min=1 明显恶化（PPL=17.789, +0.096 vs uniform），ESS 约束过松导致 46.7% batches 过度降权。n_min=2 (= batch_size//2) 在稳定性和干预力度间取得最优平衡。",
    "originalFile": "# All Successful Experiments Summary\n\n> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure\n\n---\n\n## Grid-b Experiments\n\nFixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.\n\n| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|\n| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |\n| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |\n| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |\n| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |\n| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |\n| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |\n| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |\n| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |\n| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |\n| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |\n| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |\n| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |\n| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |\n| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |\n| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |\n| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |\n| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |\n| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |\n\n> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。\n> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。\n\n---\n\n## Adaptive Experiments\n\nPer-batch adaptive b* via α_eff theory. Sorted by PPL ascending.\n\n| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|\n| adaptive_seed123 | n_min=3 (pre-D012) | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |\n| adaptive_seed456 | n_min=3 (pre-D012) | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |\n| adaptive_fix_seed123 | n_min=2 (post-D012) | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |\n| adaptive_fix_seed42 | n_min=2 (post-D012) | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |\n| adaptive_fix_seed456 | n_min=2 (post-D012) | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |\n| adaptive_seed42 | n_min=3 (pre-D012) | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |\n\n> \"n_min=3 (pre-D012)\" = D012 修复前 n_min=batch_size-1=3。\"n_min=2 (post-D012)\" = D012 修复后 n_min=max(2, batch_size//2)=2。\n> pre-D012 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串 \"0.0–3.8\"）。\n> post-D012 b* 分布（3 seeds 一致）：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。\n\n---\n\n## Ablation Experiments\n\nSingle-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.\n\n| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |\n|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|\n| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |\n| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |\n| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |\n\n> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。\n> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。\n> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。\n\n---\n\n## Baseline Experiments\n\nUniform weighting (no provenance information). Sorted by PPL ascending.\n\n| exp_id | seed | PPL | eval_loss | gpu_hours |\n|--------|------|-----|-----------|-----------|\n| uniform_seed42 | 42 | 17.690 | - | 3.43 |\n| uniform_seed123 | 123 | 17.690 | - | 3.43 |\n| uniform_seed456 | 456 | 17.700 | - | 3.43 |\n\n---\n\n## Infrastructure Experiments (non-training)\n\n| exp_id | 类型 | 关键指标 |\n|--------|------|---------|\n| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |\n| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |\n\n---\n\n## n_min Sensitivity Analysis\n\nAdaptive method with varying n_min (minimum effective sample size constraint). Uniform baseline mean PPL = 17.693 (3 seeds).\n\n### Per-seed PPL Comparison\n\n| n_min | seed42 | seed123 | seed456 | mean | std (sample) | vs uniform mean |\n|-------|--------|---------|---------|------|--------------|-----------------|\n| 1 | 17.789 | — | — | 17.789 | — | +0.096 |\n| 2 | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 | −0.042 |\n| 3 | 17.690 | 17.630 | 17.640 | 17.653 | 0.032 | −0.040 |\n| 4 | pending | — | — | — | — | — |\n\n> std = sample standard deviation (ddof=1, n=3)。n_min=1/4 仅有 seed42，无法计算 std。\n\n### Key Observations\n\n1. **n_min=2 vs n_min=3 均值差仅 0.002**（17.651 vs 17.653），在 seed 噪声范围内（单 seed 波动 ~0.04）\n2. **n_min=2 跨 seed variance 显著更低**：std=0.009 vs std=0.032（3.8× 更稳定）\n3. n_min=2 的 seed42 改善明显（17.690→17.650），消除了 n_min=3 时 seed42 的异常偏高（与 uniform 持平的 17.690）\n4. n_min=1 明显恶化（+0.096 vs uniform），ESS 约束过松导致 46.7% batches b* 达到上限 20，over-downweighting 严重\n5. **结论**：n_min=2 (= batch_size//2) 是最优选择，优势在稳定性（低 variance）而非均值（均值差在噪声范围内）\n\n### b* Distribution Comparison\n\n| n_min | seed | b* mean | b* median | b* std | b* p25 | b* p75 | % b*≥2 |\n|-------|------|---------|-----------|--------|--------|--------|--------|\n| 1 | 42 | 7.197 | 1.746 | 8.374 | 0.803 | 20.000 | 46.7% |\n| 2 | 42 | 1.399 | 0.871 | 1.933 | 0.540 | 1.512 | 16.1% |\n| 2 | 123 | 1.431 | 0.880 | 2.029 | 0.540 | 1.520 | 16.1% |\n| 2 | 456 | 1.416 | 0.880 | 1.993 | 0.540 | 1.520 | 16.1% |\n| 3 | all | — | — | — | — | — | — |\n\n> n_min=3 (pre-D012) 仅记录了 b* range \"0.0–3.8\"，无详细分布统计。\n> n_min=1 的极端 b* 分布（mean=7.2, p75=20.0 即上限, 46.7% 达上限）解释了其 PPL 恶化：过多 batch 被过度降权。\n> n_min=2 的 b* 分布跨 3 seeds 高度一致（mean 1.40–1.43, median 0.87–0.88），与 PPL 低 variance 吻合。\n\n---\n\n## Key Findings\n\n1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。\n\n2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。\n\n3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。\n\n4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。\n\n5. **Adaptive_fix (PPL=17.650) 略优于 golden ratio oracle (PPL=17.654)。** adaptive_fix 在不使用真实标签的情况下即可达到甚至超越已知比例的 oracle 水平，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。\n\n---\n\n## PPL Ratio Reference\n\n| 方法 | seed42 | seed123 | seed456 | mean |\n|------|--------|---------|---------|------|\n| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |\n| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |\n| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |\n| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |\n| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |\n| golden_ratio oracle | 0.9980 | - | - | - |\n| ess_only | 1.0023 | - | - | - |\n| nmin1 | 1.0056 | - | - | - |\n",
    "structuredPatch": [
      {
        "oldStart": 137,
        "oldLines": 7,
        "newStart": 137,
        "newLines": 7,
        "lines": [
          " ",
          " 3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。",
          " ",
          "-4. **n_min 敏感性：n_min=2 最优，n_min=1 退化。** n_min=1 (PPL=17.789) 比 uniform (17.69) 差 +0.10，因 ESS 约束失效导致过度降权。n_min=2 在保护 ESS 和允许降权之间取得平衡。",
          "+4. **n_min 敏感性：n_min=2 的优势在稳定性而非均值。** n_min=2 vs n_min=3 均值差仅 0.002（17.651 vs 17.653，噪声范围内），但跨 seed std 从 0.032 降至 0.009（3.8× 更稳定）。n_min=2 消除了 n_min=3 时 seed42 的异常偏高（17.690→17.650）。n_min=1 明显恶化（PPL=17.789, +0.096 vs uniform），ESS 约束过松导致 46.7% batches 过度降权。n_min=2 (= batch_size//2) 在稳定性和干预力度间取得最优平衡。",
          " ",
          " 5. **Adaptive_fix (PPL=17.650) 略优于 golden ratio oracle (PPL=17.654)。** adaptive_fix 在不使用真实标签的情况下即可达到甚至超越已知比例的 oracle 水平，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。",
          " "
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

_source line 50_

Let me verify the final file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "87743796-83db-4c11-b971-62c9c6df7a27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5Zi6444fyH37N3i6VGt8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 547,
      "cache_read_input_tokens": 57574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 547
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

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01ByGpb2PRNdEosi4QMTb4tw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "fb83289d-4c07-49a0-8271-a259dc71079b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5Zi6444fyH37N3i6VGt8n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 547,
      "cache_read_input_tokens": 57574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 547
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

_source line 52 · 2026-05-15T15:40:49.222Z_

<details><summary>↩ Tool result · `toolu_01ByGpb2PRNdEosi4QMTb4tw`</summary>

```text
1	# All Successful Experiments Summary
2	
3	> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure
4	
5	---
6	
7	## Grid-b Experiments
8	
9	Fixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.
10	
11	| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |
12	|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|
13	| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |
14	| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |
15	| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |
16	| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |
17	| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |
18	| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |
19	| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |
20	| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |
21	| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |
22	| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |
23	| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |
24	| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |
25	| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |
26	| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |
27	| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |
28	| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |
29	| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |
30	| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |
31	
32	> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。
33	> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。
34	
35	---
36	
37	## Adaptive Experiments
38	
39	Per-batch adaptive b* via α_eff theory. Sorted by PPL ascending.
40	
41	| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |
42	|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|
43	| adaptive_seed123 | n_min=3 (pre-D012) | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |
44	| adaptive_seed456 | n_min=3 (pre-D012) | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |
45	| adaptive_fix_seed123 | n_min=2 (post-D012) | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |
46	| adaptive_fix_seed42 | n_min=2 (post-D012) | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |
47	| adaptive_fix_seed456 | n_min=2 (post-D012) | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |
48	| adaptive_seed42 | n_min=3 (pre-D012) | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |
49	
50	> "n_min=3 (pre-D012)" = D012 修复前 n_min=batch_size-1=3。"n_min=2 (post-D012)" = D012 修复后 n_min=max(2, batch_size//2)=2。
51	> pre-D012 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串 "0.0–3.8"）。
52	> post-D012 b* 分布（3 seeds 一致）：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。
53	
54	---
55	
56	## Ablation Experiments
57	
58	Single-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.
59	
60	| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |
61	|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|
62	| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |
63	| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |
64	| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |
65	
66	> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。
67	> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。
68	> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。
69	
70	---
71	
72	## Baseline Experiments
73	
74	Uniform weighting (no provenance information). Sorted by PPL ascending.
75	
76	| exp_id | seed | PPL | eval_loss | gpu_hours |
77	|--------|------|-----|-----------|-----------|
78	| uniform_seed42 | 42 | 17.690 | - | 3.43 |
79	| uniform_seed123 | 123 | 17.690 | - | 3.43 |
80	| uniform_seed456 | 456 | 17.700 | - | 3.43 |
81	
82	---
83	
84	## Infrastructure Experiments (non-training)
85	
86	| exp_id | 类型 | 关键指标 |
87	|--------|------|---------|
88	| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |
89	| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |
90	
91	---
92	
93	## n_min Sensitivity Analysis
94	
95	Adaptive method with varying n_min (minimum effective sample size constraint). Uniform baseline mean PPL = 17.693 (3 seeds).
96	
97	### Per-seed PPL Comparison
98	
99	| n_min | seed42 | seed123 | seed456 | mean | std (sample) | vs uniform mean |
100	|-------|--------|---------|---------|------|--------------|-----------------|
101	| 1 | 17.789 | — | — | 17.789 | — | +0.096 |
102	| 2 | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 | −0.042 |
103	| 3 | 17.690 | 17.630 | 17.640 | 17.653 | 0.032 | −0.040 |
104	| 4 | pending | — | — | — | — | — |
105	
106	> std = sample standard deviation (ddof=1, n=3)。n_min=1/4 仅有 seed42，无法计算 std。
107	
108	### Key Observations
109	
110	1. **n_min=2 vs n_min=3 均值差仅 0.002**（17.651 vs 17.653），在 seed 噪声范围内（单 seed 波动 ~0.04）
111	2. **n_min=2 跨 seed variance 显著更低**：std=0.009 vs std=0.032（3.8× 更稳定）
112	3. n_min=2 的 seed42 改善明显（17.690→17.650），消除了 n_min=3 时 seed42 的异常偏高（与 uniform 持平的 17.690）
113	4. n_min=1 明显恶化（+0.096 vs uniform），ESS 约束过松导致 46.7% batches b* 达到上限 20，over-downweighting 严重
114	5. **结论**：n_min=2 (= batch_size//2) 是最优选择，优势在稳定性（低 variance）而非均值（均值差在噪声范围内）
115	
116	### b* Distribution Comparison
117	
118	| n_min | seed | b* mean | b* median | b* std | b* p25 | b* p75 | % b*≥2 |
119	|-------|------|---------|-----------|--------|--------|--------|--------|
120	| 1 | 42 | 7.197 | 1.746 | 8.374 | 0.803 | 20.000 | 46.7% |
121	| 2 | 42 | 1.399 | 0.871 | 1.933 | 0.540 | 1.512 | 16.1% |
122	| 2 | 123 | 1.431 | 0.880 | 2.029 | 0.540 | 1.520 | 16.1% |
123	| 2 | 456 | 1.416 | 0.880 | 1.993 | 0.540 | 1.520 | 16.1% |
124	| 3 | all | — | — | — | — | — | — |
125	
126	> n_min=3 (pre-D012) 仅记录了 b* range "0.0–3.8"，无详细分布统计。
127	> n_min=1 的极端 b* 分布（mean=7.2, p75=20.0 即上限, 46.7% 达上限）解释了其 PPL 恶化：过多 batch 被过度降权。
128	> n_min=2 的 b* 分布跨 3 seeds 高度一致（mean 1.40–1.43, median 0.87–0.88），与 PPL 低 variance 吻合。
129	
130	---
131	
132	## Key Findings
133	
134	1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。
135	
136	2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。
137	
138	3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。
139	
140	4. **n_min 敏感性：n_min=2 的优势在稳定性而非均值。** n_min=2 vs n_min=3 均值差仅 0.002（17.651 vs 17.653，噪声范围内），但跨 seed std 从 0.032 降至 0.009（3.8× 更稳定）。n_min=2 消除了 n_min=3 时 seed42 的异常偏高（17.690→17.650）。n_min=1 明显恶化（PPL=17.789, +0.096 vs uniform），ESS 约束过松导致 46.7% batches 过度降权。n_min=2 (= batch_size//2) 在稳定性和干预力度间取得最优平衡。
141	
142	5. **Adaptive_fix (PPL=17.650) 略优于 golden ratio oracle (PPL=17.654)。** adaptive_fix 在不使用真实标签的情况下即可达到甚至超越已知比例的 oracle 水平，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。
143	
144	---
145	
146	## PPL Ratio Reference
147	
148	| 方法 | seed42 | seed123 | seed456 | mean |
149	|------|--------|---------|---------|------|
150	| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
151	| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |
152	| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |
153	| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |
154	| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |
155	| golden_ratio oracle | 0.9980 | - | - | - |
156	| ess_only | 1.0023 | - | - | - |
157	| nmin1 | 1.0056 | - | - | - |
158	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "bf3b9727-9e41-45ed-9c6e-6d126ffc6121",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/all_success_summary.md",
      "content": "# All Successful Experiments Summary\n\n> Generated: 2026-05-15 | 27 experiments total | 25 training + 2 infrastructure\n\n---\n\n## Grid-b Experiments\n\nFixed b weighting: w(x) = q(x)^b where q is provenance score. Sorted by PPL ascending.\n\n| exp_id | b | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---|------|-----|-----------|-------------|---------|-----------|-----------|\n| grid_b0_5_seed123 | 0.5 | 123 | 17.638 | 2.8700 | 0.9971 | - | - | 3.64 |\n| grid_b0_5_seed456 | 0.5 | 456 | 17.650 | 2.8705 | 0.9972 | - | - | 3.60 |\n| grid_b0_5_seed42 | 0.5 | 42 | 17.651 | - | 0.9978 | - | - | 3.62 |\n| grid_b1_0_seed123 | 1.0 | 123 | 17.674 | 2.8721 | 0.9991 | - | - | 3.85 |\n| grid_b1_0_seed456 | 1.0 | 456 | 17.680 | 2.8725 | 0.9989 | - | - | 3.60 |\n| grid_b1_0_seed42 | 1.0 | 42 | 17.692 | - | 1.0001 | - | - | 3.60 |\n| grid_b1_5_seed123 | 1.5 | 123 | 17.701 | 2.8736 | 1.0006 | - | - | 4.18 |\n| grid_b1_5_seed456 | 1.5 | 456 | 17.710 | 2.8741 | 1.0006 | - | - | 3.60 |\n| grid_b1_5_seed42 | 1.5 | 42 | 17.718 | - | 1.0016 | - | - | 4.11 |\n| grid_b2_0_seed123 | 2.0 | 123 | 17.725 | 2.8750 | 1.0020 | - | - | 3.63 |\n| grid_b2_0_seed42 | 2.0 | 42 | 17.741 | - | 1.0029 | - | - | 3.62 |\n| grid_b3_0_seed123 | 3.0 | 123 | 17.760 | 2.8770 | 1.0040 | - | - | 3.60 |\n| grid_b3_0_seed42 | 3.0 | 42 | 17.774 | - | 1.0047 | - | - | 3.62 |\n| grid_b5_0_seed123 | 5.0 | 123 | 17.804 | 2.8794 | 1.0064 | - | - | 4.01 |\n| grid_b5_0_seed42 | 5.0 | 42 | 17.818 | - | 1.0072 | - | - | 3.64 |\n| grid_b3_0_seed456 ⚠️ | 3.0 | 456 | 17.921 | 2.8860 | 1.0125 | - | - | 1.83 |\n| grid_b2_0_seed456 ⚠️ | 2.0 | 456 | 17.989 | 2.8898 | 1.0163 | - | - | 3.60 |\n| grid_b5_0_seed456 ⚠️ | 5.0 | 456 | 17.993 | 2.8900 | 1.0166 | - | - | 1.83 |\n\n> ⚠️ seed456 的 b=2.0/3.0/5.0 训练中断后从 checkpoint 恢复，导致系统性 PPL 偏高 (+0.16–0.25)。论文 Table 1 中这些行仅报 2 seeds (seed42+seed123)。\n> seed42 的 grid 实验来自 grid_b_seed42_batch（6 个 b 值串行），eval_loss 未单独记录。\n\n---\n\n## Adaptive Experiments\n\nPer-batch adaptive b* via α_eff theory. Sorted by PPL ascending.\n\n| exp_id | variant | τ | n_min | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | gpu_hours |\n|--------|---------|---|-------|------|-----|-----------|-------------|---------|-----------|-----------|\n| adaptive_seed123 | n_min=3 (pre-D012) | 0.8 | 3 | 123 | 17.630 | - | 0.9966 | - | - | 4.21 |\n| adaptive_seed456 | n_min=3 (pre-D012) | 0.8 | 3 | 456 | 17.640 | - | 0.9966 | - | - | 4.21 |\n| adaptive_fix_seed123 | n_min=2 (post-D012) | 0.8 | 2 | 123 | 17.643 | 2.8704 | 0.9973 | 1.431 | 0.880 | 3.00 |\n| adaptive_fix_seed42 | n_min=2 (post-D012) | 0.8 | 2 | 42 | 17.650 | 2.8709 | 0.9977 | 1.399 | 0.871 | 3.35 |\n| adaptive_fix_seed456 | n_min=2 (post-D012) | 0.8 | 2 | 456 | 17.660 | 2.8711 | 0.9977 | 1.416 | 0.880 | 3.34 |\n| adaptive_seed42 | n_min=3 (pre-D012) | 0.8 | 3 | 42 | 17.690 | - | 1.0000 | - | - | 4.21 |\n\n> \"n_min=3 (pre-D012)\" = D012 修复前 n_min=batch_size-1=3。\"n_min=2 (post-D012)\" = D012 修复后 n_min=max(2, batch_size//2)=2。\n> pre-D012 实验无 b* 详细统计和 eval_loss（仅记录了 b* range 字符串 \"0.0–3.8\"）。\n> post-D012 b* 分布（3 seeds 一致）：~21% batches b*<0.5, ~36% in [0.5,1), ~27% in [1,2), ~16% above 2。\n\n---\n\n## Ablation Experiments\n\nSingle-variable ablations against adaptive_fix baseline (seed42, PPL=17.650). Sorted by PPL ascending.\n\n| exp_id | 变量 | 值 | seed | PPL | eval_loss | PPL/uniform | b* mean | b* median | α_eff mean | gpu_hours |\n|--------|------|---|------|-----|-----------|-------------|---------|-----------|------------|-----------|\n| golden_ratio_seed42 | method | oracle w=1/φ≈0.618 | 42 | 17.654 | 2.871 | 0.9980 | - | - | - | 3.78 |\n| ess_only_seed42 | method | max-intervention | 42 | 17.730 | 2.875 | 1.0023 | 3.51 | 1.58 | - | 3.62 |\n| nmin1_seed42 | n_min | 1 | 42 | 17.789 | 2.879 | 1.0056 | 7.197 | 1.746 | 0.714 | 4.87 |\n\n> golden_ratio: 已知合成比例的 oracle，w=1/φ 对 q>0.5 的样本，w=1.0 对其他。无需 b* 优化。\n> ess_only: b* = max{b : ESS(b) ≥ n_min}，最大化干预（vs adaptive 的最小化干预）。\n> nmin1: n_min=1 使 ESS 约束几乎失效，46.7% batches 的 b* 达到上限 20，over-downweighting 严重。\n\n---\n\n## Baseline Experiments\n\nUniform weighting (no provenance information). Sorted by PPL ascending.\n\n| exp_id | seed | PPL | eval_loss | gpu_hours |\n|--------|------|-----|-----------|-----------|\n| uniform_seed42 | 42 | 17.690 | - | 3.43 |\n| uniform_seed123 | 123 | 17.690 | - | 3.43 |\n| uniform_seed456 | 456 | 17.700 | - | 3.43 |\n\n---\n\n## Infrastructure Experiments (non-training)\n\n| exp_id | 类型 | 关键指标 |\n|--------|------|---------|\n| datagen_synthetic_4gpu | 数据生成 | 340,992 docs, 132M tokens, 4-GPU parallel |\n| detector_tfidf_lr | 检测器训练 | AUC=0.939, ECE_calibrated=0.048, T=0.204 |\n\n---\n\n## n_min Sensitivity Analysis\n\nAdaptive method with varying n_min (minimum effective sample size constraint). Uniform baseline mean PPL = 17.693 (3 seeds).\n\n### Per-seed PPL Comparison\n\n| n_min | seed42 | seed123 | seed456 | mean | std (sample) | vs uniform mean |\n|-------|--------|---------|---------|------|--------------|-----------------|\n| 1 | 17.789 | — | — | 17.789 | — | +0.096 |\n| 2 | 17.650 | 17.643 | 17.660 | 17.651 | 0.009 | −0.042 |\n| 3 | 17.690 | 17.630 | 17.640 | 17.653 | 0.032 | −0.040 |\n| 4 | pending | — | — | — | — | — |\n\n> std = sample standard deviation (ddof=1, n=3)。n_min=1/4 仅有 seed42，无法计算 std。\n\n### Key Observations\n\n1. **n_min=2 vs n_min=3 均值差仅 0.002**（17.651 vs 17.653），在 seed 噪声范围内（单 seed 波动 ~0.04）\n2. **n_min=2 跨 seed variance 显著更低**：std=0.009 vs std=0.032（3.8× 更稳定）\n3. n_min=2 的 seed42 改善明显（17.690→17.650），消除了 n_min=3 时 seed42 的异常偏高（与 uniform 持平的 17.690）\n4. n_min=1 明显恶化（+0.096 vs uniform），ESS 约束过松导致 46.7% batches b* 达到上限 20，over-downweighting 严重\n5. **结论**：n_min=2 (= batch_size//2) 是最优选择，优势在稳定性（低 variance）而非均值（均值差在噪声范围内）\n\n### b* Distribution Comparison\n\n| n_min | seed | b* mean | b* median | b* std | b* p25 | b* p75 | % b*≥2 |\n|-------|------|---------|-----------|--------|--------|--------|--------|\n| 1 | 42 | 7.197 | 1.746 | 8.374 | 0.803 | 20.000 | 46.7% |\n| 2 | 42 | 1.399 | 0.871 | 1.933 | 0.540 | 1.512 | 16.1% |\n| 2 | 123 | 1.431 | 0.880 | 2.029 | 0.540 | 1.520 | 16.1% |\n| 2 | 456 | 1.416 | 0.880 | 1.993 | 0.540 | 1.520 | 16.1% |\n| 3 | all | — | — | — | — | — | — |\n\n> n_min=3 (pre-D012) 仅记录了 b* range \"0.0–3.8\"，无详细分布统计。\n> n_min=1 的极端 b* 分布（mean=7.2, p75=20.0 即上限, 46.7% 达上限）解释了其 PPL 恶化：过多 batch 被过度降权。\n> n_min=2 的 b* 分布跨 3 seeds 高度一致（mean 1.40–1.43, median 0.87–0.88），与 PPL 低 variance 吻合。\n\n---\n\n## Key Findings\n\n1. **Adaptive 方法接近 grid-best 且无需搜索。** adaptive_fix (n_min=2) PPL 范围 17.643–17.660，与 grid-best b=0.5 (17.638–17.651) 差距 <0.01 PPL。adaptive 消除了对 b 值的 grid search 依赖。\n\n2. **Grid-b 单调趋势：b 越小 PPL 越好。** b=0.5 最优 (PPL/uniform ≈ 0.997)，b=5.0 最差 (PPL/uniform ≈ 1.007)。最优固定 b 在搜索边界，暗示需要更细粒度的 per-batch 控制。\n\n3. **Adaptive b* 分布揭示数据异质性。** median b*≈0.88 vs mean≈1.4，加上 16% batches b*>2，说明不同 batch 的污染严重程度差异大——任何固定 b 都无法同时最优。\n\n4. **n_min 敏感性：n_min=2 的优势在稳定性而非均值。** n_min=2 vs n_min=3 均值差仅 0.002（17.651 vs 17.653，噪声范围内），但跨 seed std 从 0.032 降至 0.009（3.8× 更稳定）。n_min=2 消除了 n_min=3 时 seed42 的异常偏高（17.690→17.650）。n_min=1 明显恶化（PPL=17.789, +0.096 vs uniform），ESS 约束过松导致 46.7% batches 过度降权。n_min=2 (= batch_size//2) 在稳定性和干预力度间取得最优平衡。\n\n5. **Adaptive_fix (PPL=17.650) 略优于 golden ratio oracle (PPL=17.654)。** adaptive_fix 在不使用真实标签的情况下即可达到甚至超越已知比例的 oracle 水平，验证了 α_eff 理论框架的有效性。ESS-only max-intervention (PPL=17.73) 显著劣于 min-intervention adaptive，确认设计选择正确。\n\n---\n\n## PPL Ratio Reference\n\n| 方法 | seed42 | seed123 | seed456 | mean |\n|------|--------|---------|---------|------|\n| uniform | 1.0000 | 1.0000 | 1.0000 | 1.0000 |\n| grid b=0.5 | 0.9978 | 0.9971 | 0.9972 | 0.9974 |\n| grid b=1.0 | 1.0001 | 0.9991 | 0.9989 | 0.9994 |\n| adaptive_fix (n_min=2) | 0.9977 | 0.9973 | 0.9977 | 0.9976 |\n| adaptive (n_min=3) | 1.0000 | 0.9966 | 0.9966 | 0.9977 |\n| golden_ratio oracle | 0.9980 | - | - | - |\n| ess_only | 1.0023 | - | - | - |\n| nmin1 | 1.0056 | - | - | - |\n",
      "numLines": 158,
      "startLine": 1,
      "totalLines": 158
    }
  }
}
```

</details>

---

### Assistant

_source line 53_

完成。修改内容：

1. **Adaptive 表 variant 标签**：`original` → `n_min=3 (pre-D012)`，`n_min fix` → `n_min=2 (post-D012)`，表下注释同步更新
2. **新增 `## n_min Sensitivity Analysis` 小节**（第 93–129 行），包含：
   - Per-seed PPL 对比表（n_min=1/2/3/4）
   - 5 条 key observations，核心叙事：n_min=2 优势在稳定性（std 0.009 vs 0.032, 3.8×）而非均值（差 0.002）
   - b* 分布对比表（n_min=1 和 n_min=2 有详细数据，n_min=3 仅有 range 字符串）
3. **Key Findings #4 更新**：补充了稳定性叙事和具体数值

所有数值均从 registry 取得，std 使用 sample standard deviation (ddof=1)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "uuid": "902dc06e-15ed-40e0-8c40-5c272360d508",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019U1LzGSS6GkPZNcMgEuZ45",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4979,
      "cache_read_input_tokens": 58121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4979
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

_source line 54_

完成。修改内容：

1. **Adaptive 表 variant 标签**：`original` → `n_min=3 (pre-D012)`，`n_min fix` → `n_min=2 (post-D012)`，表下注释同步更新
2. **新增 `## n_min Sensitivity Analysis` 小节**（第 93–129 行），包含：
   - Per-seed PPL 对比表（n_min=1/2/3/4）
   - 5 条 key observations，核心叙事：n_min=2 优势在稳定性（std 0.009 vs 0.032, 3.8×）而非均值（差 0.002）
   - b* 分布对比表（n_min=1 和 n_min=2 有详细数据，n_min=3 仅有 range 字符串）
3. **Key Findings #4 更新**：补充了稳定性叙事和具体数值

所有数值均从 registry 取得，std 使用 sample standard deviation (ddof=1)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 220188,
  "duration_api_ms": 220082,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "2a0c2b2e-ded9-41da-a3cc-a87bffb93fea",
  "total_cost_usd": 1.02148475,
  "usage": {
    "input_tokens": 21,
    "cache_creation_input_tokens": 51653,
    "cache_read_input_tokens": 691569,
    "output_tokens": 14029,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 51653,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 295,
        "cache_read_input_tokens": 58121,
        "cache_creation_input_tokens": 4979,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4979
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1959,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002039,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 21,
      "outputTokens": 14029,
      "cacheReadInputTokens": 691569,
      "cacheCreationInputTokens": 51653,
      "webSearchRequests": 0,
      "costUSD": 1.01944575,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bcee6946-1c58-48e1-a181-e185228d46c6"
}
```

</details>

---
