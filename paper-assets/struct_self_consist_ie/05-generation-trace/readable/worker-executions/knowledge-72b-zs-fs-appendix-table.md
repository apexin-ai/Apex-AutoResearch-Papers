# knowledge 72b zs fs appendix table

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_knowledge_72b-zs-fs-appendix-table_20260520T013450.log`
- **Structured JSON:** [`a621d52eed46c92268b0.json`](../../sessions/a6/a621d52eed46c92268b0.json)

## Before a recorded user message

19 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
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
  "uuid": "eda10cd7-66d8-4d8c-aca7-8fb5d99cdead",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779253200,
    "rateLimitType": "seven_day",
    "utilization": 0.75,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "f13d9bae-f49f-46b6-b202-cac60021f423",
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07"
}
```

---

### Assistant

_source line 4_

Let me read the data files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "242f35e1-0c00-4ce7-a3ad-8b5b9c4ba762",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATu7AQATtAUASyhuN9C4cJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12203,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12203
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

<details open><summary>🔧 Tool call — Read · `toolu_01F5oxmsviTjrAjAqLYLLK4T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/72b_fewshot_signal_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "83a67723-84ce-4d0f-a6b5-ce6fb51cb496",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATu7AQATtAUASyhuN9C4cJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12203,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12203
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

_source line 6 · 2026-05-20T01:35:02.306Z_

<details><summary>↩ Tool result · `toolu_01F5oxmsviTjrAjAqLYLLK4T`</summary>

```text
1	{
2	  "model": "Qwen2.5-72B-Instruct-AWQ",
3	  "setting": "3-shot few-shot",
4	  "n_samples": 8,
5	  "datasets": {
6	    "scierc": {
7	      "n_instances": 529,
8	      "greedy_f1": 0.461,
9	      "oracle_f1": 0.604,
10	      "degeneracy_rate": 0.166,
11	      "construction_lp_weighted_f1": 0.461,
12	      "construction_delta": -0.0008,
13	      "construction_p": 0.54,
14	      "signals_rho": {
15	        "LP": 0.060,
16	        "SJ": 0.293,
17	        "FK": 0.301,
18	        "VC": 0.258,
19	        "EM": 0.205
20	      }
21	    },
22	    "conll2003": {
23	      "n_instances": 2756,
24	      "greedy_f1": 0.745,
25	      "oracle_f1": 0.796,
26	      "degeneracy_rate": 0.700,
27	      "construction_lp_weighted_f1": 0.745,
28	      "construction_delta": 0.0003,
29	      "construction_p": 0.42,
30	      "signals_rho": {
31	        "LP": 0.106,
32	        "SJ": 0.442,
33	        "FK": 0.451,
34	        "VC": 0.426,
35	        "EM": 0.403
36	      }
37	    },
38	    "fewnerd": {
39	      "n_instances": 32565,
40	      "greedy_f1": 0.619,
41	      "oracle_f1": 0.702,
42	      "degeneracy_rate": 0.452,
43	      "construction_lp_weighted_f1": 0.619,
44	      "construction_delta": 0.02,
45	      "construction_p": 0.401,
46	      "signals_rho": {
47	        "LP": 0.161,
48	        "SJ": 0.345,
49	        "FK": 0.327,
50	        "VC": 0.410,
51	        "EM": 0.302
52	      }
53	    }
54	  }
55	}
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "442c6bab-aa07-461e-b750-7f2bc1dd6c5a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/72b_fewshot_signal_summary.json",
      "content": "{\n  \"model\": \"Qwen2.5-72B-Instruct-AWQ\",\n  \"setting\": \"3-shot few-shot\",\n  \"n_samples\": 8,\n  \"datasets\": {\n    \"scierc\": {\n      \"n_instances\": 529,\n      \"greedy_f1\": 0.461,\n      \"oracle_f1\": 0.604,\n      \"degeneracy_rate\": 0.166,\n      \"construction_lp_weighted_f1\": 0.461,\n      \"construction_delta\": -0.0008,\n      \"construction_p\": 0.54,\n      \"signals_rho\": {\n        \"LP\": 0.060,\n        \"SJ\": 0.293,\n        \"FK\": 0.301,\n        \"VC\": 0.258,\n        \"EM\": 0.205\n      }\n    },\n    \"conll2003\": {\n      \"n_instances\": 2756,\n      \"greedy_f1\": 0.745,\n      \"oracle_f1\": 0.796,\n      \"degeneracy_rate\": 0.700,\n      \"construction_lp_weighted_f1\": 0.745,\n      \"construction_delta\": 0.0003,\n      \"construction_p\": 0.42,\n      \"signals_rho\": {\n        \"LP\": 0.106,\n        \"SJ\": 0.442,\n        \"FK\": 0.451,\n        \"VC\": 0.426,\n        \"EM\": 0.403\n      }\n    },\n    \"fewnerd\": {\n      \"n_instances\": 32565,\n      \"greedy_f1\": 0.619,\n      \"oracle_f1\": 0.702,\n      \"degeneracy_rate\": 0.452,\n      \"construction_lp_weighted_f1\": 0.619,\n      \"construction_delta\": 0.02,\n      \"construction_p\": 0.401,\n      \"signals_rho\": {\n        \"LP\": 0.161,\n        \"SJ\": 0.345,\n        \"FK\": 0.327,\n        \"VC\": 0.410,\n        \"EM\": 0.302\n      }\n    }\n  }\n}\n",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TzMce7XUJhSNosnZqDxcqa`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "ed23ffde-c648-4ad4-b3d1-bd39d7e56b8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATu7AQATtAUASyhuN9C4cJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12203,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12203
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

_source line 8 · 2026-05-20T01:35:03.071Z_

<details><summary>↩ Tool result · `toolu_01TzMce7XUJhSNosnZqDxcqa`</summary>

````text
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
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "3e11e44d-4d5e-422b-8543-d0b2bda582b1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
I have the FS data from the JSON. Now let me compile all the data. Let me also check memory.md for any ZS data I might need to verify.

From the task description, the ZS data is:
- SciERC ZS: degen=21.0%, LP ρ=0.081, SJ ρ=0.217, FK ρ=?, VC ρ=0.277, greedy=0.399, oracle=0.549, constr Δ=+1.53pp, p=0.008


- FewNERD ZS: degen=46.2%, LP ρ=0.119, SJ ρ=0.345(?), FK ρ=?, VC ρ=0.416, greedy=0.628, oracle=0.707, constr Δ=-0.20pp
- CoNLL ZS: degen=67.7%, LP ρ=-0.002, SJ ρ=0.304(?), FK ρ=?, VC ρ=0.297, greedy=0.712, oracle=0.765, constr Δ=-0.37pp

Now looking at the full-shot results across the datasets. SciERC shows much lower degeneracy at 16.6% compared to the zero-shot setting, with moderate correlations across methods and a small constraint penalty. CoNLL's full-shot performance is strong with 70% degeneracy and notably positive constraint effects. FewNERD follows a similar pattern to zero-shot but with slightly improved LP correlation. Looking at the FewNERD construction delta of 0.02, that translates to +2.00 percentage points with a p-value of 0.401. Let me check the memory file to see what the zero-shot FK values are.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "0704d5a0-17eb-484f-82e1-74c2c8c11635",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018H5papdPqTjCEbHEDgL5jR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1244,
      "cache_read_input_tokens": 24044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1244
      },
      "output_tokens": 15,
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

_source line 10_

Let me check memory for any additional ZS data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "41d4e84c-b409-420f-960b-45d66e5c103b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018H5papdPqTjCEbHEDgL5jR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1244,
      "cache_read_input_tokens": 24044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1244
      },
      "output_tokens": 15,
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01D2qHNwZB9G289MfBCKUuey`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "39f31d08-b2d0-4d9e-95a4-5b237ce4aaca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018H5papdPqTjCEbHEDgL5jR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1244,
      "cache_read_input_tokens": 24044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1244
      },
      "output_tokens": 15,
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

_source line 12 · 2026-05-20T01:35:19.300Z_

<details><summary>↩ Tool result · `toolu_01D2qHNwZB9G289MfBCKUuey`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory\\n\\n## exp_qwen25_72b_fewshot 完整结果（2026-05-20）\\n\\n实验于 2026-05-20 08:47 完成。模型：Qwen2.5-72B-Instruct-AWQ, 3-shot, N=8 samples, seed=42。\\n\\n### ZS vs FS 完整对比表\\n\\n| Dataset  | Regime | N inst | Degen% | LP ρ   | SJ ρ  | FK ρ  | VC ρ  | EM ρ  | Greedy F1 | Oracle F1 | LP-wt F1 | LP Δ (pp) | p-value |\\n|----------|--------|--------|--------|--------|-------|-------|-------|-------|-----------|-----------|----------|-----------|---------|\\n| SciERC   | ZS     | 529    | 21.0%  | 0.081  | 0.217 | 0.227 | 0.277 | 0.181 | 0.399     | 0.549     | 0.415    | +1.53     | 0.008** |\\n| SciERC   | FS     | 529    | 16.6%  | 0.060  | 0.293 | 0.301 | 0.258 | 0.205 | 0.461     | 0.604     | 0.461    | -0.08     | 0.544   |\\n| CoNLL    | ZS     | 2756   | 67.7%  | -0.002 | 0.304 | 0.302 | 0.297 | 0.281 | 0.712     | 0.765     | 0.708    | -0.37     | n/a     |\\n| CoNLL    | FS     | 2756   | 70.0%  | 0.106  | 0.442 | 0.451 | 0.426 | 0.403 | 0.745     | 0.796     | 0.745    | +0.03     | 0.417   |\\n| FewNERD  | ZS     | 32565  | 46.2%  | 0.119  | 0.345 | 0.321 | 0.416 | 0.303 | 0.628     | 0.707     | 0.626    | -0.20     | n/a     |\\n| FewNERD  | FS     | 32565  | 45.2%  | 0.161  | 0.345 | 0.327 | 0.410 | 0.302 | 0.619     | 0.702     | 0.619    | +0.02     | 0.401   |\\n\\n### FewNERD FS Bootstrap 详情\\n- observed_diff: +0.000154 (+0.02pp)\\n- 95% CI: [-0.0011, +0.0014]\\n- p-value: 0.4005 (n.s.)\\n- Cohen's d: 0.0014\\n- Instance positive/negative/tied: 2752/2371/27442 (8.5%/7.3%/84.3%)\\n- Non-degen diff: +0.0002 (+0.02pp), p=0.4009\\n\\n### FS 效果总结\\nFew-shot 对基础 NER 性能提升显著：\\n- SciERC: F1 0.399→0.461 (+6.2pp)\\n- CoNLL: F1 0.712→0.745 (+3.3pp)\\n- FewNERD: F1 0.628→0.619 (-0.9pp, 略降)\\n\\n但 LP-weighted construction 在所有 FS 条件下均不显著：\\n- SciERC FS: Δ=-0.08pp (p=0.544)\\n- CoNLL FS: Δ=+0.03pp (p=0.417)\\n- FewNERD FS: Δ=+0.02pp (p=0.401)\\n\\n### Dual-gating hypothesis 评估\\n\\nConstruction 仅在 SciERC ZS 一个条件下显著（+1.53pp, p=0.008）。\\n\\n**Dual-gating 在 FT+ZS regime 内成立（6/6 条件一致）：**\\n- Degen gate 阈值约 22%（SciERC ZS 21.0% 刚好通过）\\n- Low degen + adequate LP ρ = construction works（SciERC ZS 证明）\\n- High degen（CoNLL ZS 67.7%, FewNERD ZS 46.2%）→ construction 失效，符合预期\\n\\n**FS regime 引入独立失效因素：**\\n- SciERC FS: degen=16.6% 满足 degen gate，但 LP ρ=0.06 极弱，construction 失效（Δ=-0.08pp, p=0.544）。说明 FS 有额外的降级机制（可能是 in-context examples 压缩了 LP 的区分力）\\n- CoNLL FS: degen=70.0% 远超阈值，construction 失效符合预期\\n- FewNERD FS: degen=45.2% 远超 <22% 的 degen gate 阈值，不 qualify 为 dual-gating 的反例，construction 失效符合预期\\n\\n**结论**：Dual-gating 在 FT+ZS regime 内是 construction 成功的充要条件。FS regime 引入独立失效因素，需单独分析——但 FS 的三个失效案例均不构成对 dual-gating 的挑战（FewNERD/CoNLL FS 因 degen 过高不满足 gate，SciERC FS 因 LP 退化不满足 signal gate）。\\n\\n### Signal 质量 ZS→FS 变化趋势\\n| Signal | SciERC ZS→FS | CoNLL ZS→FS | FewNERD ZS→FS |\\n|--------|-------------|-------------|---------------|\\n| LP ρ   | 0.081→0.060 ↓ | -0.002→0.106 ↑ | 0.119→0.161 ↑ |\\n| SJ ρ   | 0.217→0.293 ↑ | 0.304→0.442 ↑ | 0.345→0.345 = |\\n| FK ρ   | 0.227→0.301 ↑ | 0.302→0.451 ↑ | 0.321→0.327 ↑ |\\n| VC ρ   | 0.277→0.258 ↓ | 0.297→0.426 ↑ | 0.416→0.410 ↓ |\\n| EM ρ   | 0.181→0.205 ↑ | 0.281→0.403 ↑ | 0.303→0.302 = |\\n\\nFS 对 CoNLL 所有 signal 大幅提升（SJ +0.14, FK +0.15），但对 FewNERD/SciERC signal 变化有限。\\n\\n### 文件路径\\n- SciERC signals: output/72b_fewshot_signals/scierc/full_signal_report.json\\n- CoNLL signals: output/72b_fewshot_signals/conll2003/full_signal_report.json\\n- FewNERD signals: output/72b_fewshot_signals/fewnerd/full_signal_report.json\\n- SciERC bootstrap: output/72b_fewshot_signals/scierc/scierc_paired_bootstrap_result.json\\n- CoNLL bootstrap: output/72b_fewshot_signals/conll2003/conll2003_paired_bootstrap_result.json\\n- FewNERD bootstrap: output/72b_fewshot_signals/fewnerd/fewnerd_paired_bootstrap_result.json\\n- ZS report: output/72b_zeroshot/full_signal_report.json\\n- ZS bootstrap (SciERC): output/72b_zeroshot/scierc/paired_bootstrap_result.json\\n\", \"total_chars\": 3784, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "c13bc34b-bd4d-4df8-8bea-cce14eb2ab7f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\\\", \\\"content\\\": \\\"# Memory\\\\n\\\\n## exp_qwen25_72b_fewshot 完整结果（2026-05-20）\\\\n\\\\n实验于 2026-05-20 08:47 完成。模型：Qwen2.5-72B-Instruct-AWQ, 3-shot, N=8 samples, seed=42。\\\\n\\\\n### ZS vs FS 完整对比表\\\\n\\\\n| Dataset  | Regime | N inst | Degen% | LP ρ   | SJ ρ  | FK ρ  | VC ρ  | EM ρ  | Greedy F1 | Oracle F1 | LP-wt F1 | LP Δ (pp) | p-value |\\\\n|----------|--------|--------|--------|--------|-------|-------|-------|-------|-----------|-----------|----------|-----------|---------|\\\\n| SciERC   | ZS     | 529    | 21.0%  | 0.081  | 0.217 | 0.227 | 0.277 | 0.181 | 0.399     | 0.549     | 0.415    | +1.53     | 0.008** |\\\\n| SciERC   | FS     | 529    | 16.6%  | 0.060  | 0.293 | 0.301 | 0.258 | 0.205 | 0.461     | 0.604     | 0.461    | -0.08     | 0.544   |\\\\n| CoNLL    | ZS     | 2756   | 67.7%  | -0.002 | 0.304 | 0.302 | 0.297 | 0.281 | 0.712     | 0.765     | 0.708    | -0.37     | n/a     |\\\\n| CoNLL    | FS     | 2756   | 70.0%  | 0.106  | 0.442 | 0.451 | 0.426 | 0.403 | 0.745     | 0.796     | 0.745    | +0.03     | 0.417   |\\\\n| FewNERD  | ZS     | 32565  | 46.2%  | 0.119  | 0.345 | 0.321 | 0.416 | 0.303 | 0.628     | 0.707     | 0.626    | -0.20     | n/a     |\\\\n| FewNERD  | FS     | 32565  | 45.2%  | 0.161  | 0.345 | 0.327 | 0.410 | 0.302 | 0.619     | 0.702     | 0.619    | +0.02     | 0.401   |\\\\n\\\\n### FewNERD FS Bootstrap 详情\\\\n- observed_diff: +0.000154 (+0.02pp)\\\\n- 95% CI: [-0.0011, +0.0014]\\\\n- p-value: 0.4005 (n.s.)\\\\n- Cohen's d: 0.0014\\\\n- Instance positive/negative/tied: 2752/2371/27442 (8.5%/7.3%/84.3%)\\\\n- Non-degen diff: +0.0002 (+0.02pp), p=0.4009\\\\n\\\\n### FS 效果总结\\\\nFew-shot 对基础 NER 性能提升显著：\\\\n- SciERC: F1 0.399→0.461 (+6.2pp)\\\\n- CoNLL: F1 0.712→0.745 (+3.3pp)\\\\n- FewNERD: F1 0.628→0.619 (-0.9pp, 略降)\\\\n\\\\n但 LP-weighted construction 在所有 FS 条件下均不显著：\\\\n- SciERC FS: Δ=-0.08pp (p=0.544)\\\\n- CoNLL FS: Δ=+0.03pp (p=0.417)\\\\n- FewNERD FS: Δ=+0.02pp (p=0.401)\\\\n\\\\n### Dual-gating hypothesis 评估\\\\n\\\\nConstruction 仅在 SciERC ZS 一个条件下显著（+1.53pp, p=0.008）。\\\\n\\\\n**Dual-gating 在 FT+ZS regime 内成立（6/6 条件一致）：**\\\\n- Degen gate 阈值约 22%（SciERC ZS 21.0% 刚好通过）\\\\n- Low degen + adequate LP ρ = construction works（SciERC ZS 证明）\\\\n- High degen（CoNLL ZS 67.7%, FewNERD ZS 46.2%）→ construction 失效，符合预期\\\\n\\\\n**FS regime 引入独立失效因素：**\\\\n- SciERC FS: degen=16.6% 满足 degen gate，但 LP ρ=0.06 极弱，construction 失效（Δ=-0.08pp, p=0.544）。说明 FS 有额外的降级机制（可能是 in-context examples 压缩了 LP 的区分力）\\\\n- CoNLL FS: degen=70.0% 远超阈值，construction 失效符合预期\\\\n- FewNERD FS: degen=45.2% 远超 <22% 的 degen gate 阈值，不 qualify 为 dual-gating 的反例，construction 失效符合预期\\\\n\\\\n**结论**：Dual-gating 在 FT+ZS regime 内是 construction 成功的充要条件。FS regime 引入独立失效因素，需单独分析——但 FS 的三个失效案例均不构成对 dual-gating 的挑战（FewNERD/CoNLL FS 因 degen 过高不满足 gate，SciERC FS 因 LP 退化不满足 signal gate）。\\\\n\\\\n### Signal 质量 ZS→FS 变化趋势\\\\n| Signal | SciERC ZS→FS | CoNLL ZS→FS | FewNERD ZS→FS |\\\\n|--------|-------------|-------------|---------------|\\\\n| LP ρ   | 0.081→0.060 ↓ | -0.002→0.106 ↑ | 0.119→0.161 ↑ |\\\\n| SJ ρ   | 0.217→0.293 ↑ | 0.304→0.442 ↑ | 0.345→0.345 = |\\\\n| FK ρ   | 0.227→0.301 ↑ | 0.302→0.451 ↑ | 0.321→0.327 ↑ |\\\\n| VC ρ   | 0.277→0.258 ↓ | 0.297→0.426 ↑ | 0.416→0.410 ↓ |\\\\n| EM ρ   | 0.181→0.205 ↑ | 0.281→0.403 ↑ | 0.303→0.302 = |\\\\n\\\\nFS 对 CoNLL 所有 signal 大幅提升（SJ +0.14, FK +0.15），但对 FewNERD/SciERC signal 变化有限。\\\\n\\\\n### 文件路径\\\\n- SciERC signals: output/72b_fewshot_signals/scierc/full_signal_report.json\\\\n- CoNLL signals: output/72b_fewshot_signals/conll2003/full_signal_report.json\\\\n- FewNERD signals: output/72b_fewshot_signals/fewnerd/full_signal_report.json\\\\n- SciERC bootstrap: output/72b_fewshot_signals/scierc/scierc_paired_bootstrap_result.json\\\\n- CoNLL bootstrap: output/72b_fewshot_signals/conll2003/conll2003_paired_bootstrap_result.json\\\\n- FewNERD bootstrap: output/72b_fewshot_signals/fewnerd/fewnerd_paired_bootstrap_result.json\\\\n- ZS report: output/72b_zeroshot/full_signal_report.json\\\\n- ZS bootstrap (SciERC): output/72b_zeroshot/scierc/paired_bootstrap_result.json\\\\n\\\", \\\"total_chars\\\": 3784, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory\\n\\n## exp_qwen25_72b_fewshot 完整结果（2026-05-20）\\n\\n实验于 2026-05-20 08:47 完成。模型：Qwen2.5-72B-Instruct-AWQ, 3-shot, N=8 samples, seed=42。\\n\\n### ZS vs FS 完整对比表\\n\\n| Dataset  | Regime | N inst | Degen% | LP ρ   | SJ ρ  | FK ρ  | VC ρ  | EM ρ  | Greedy F1 | Oracle F1 | LP-wt F1 | LP Δ (pp) | p-value |\\n|----------|--------|--------|--------|--------|-------|-------|-------|-------|-----------|-----------|----------|-----------|---------|\\n| SciERC   | ZS     | 529    | 21.0%  | 0.081  | 0.217 | 0.227 | 0.277 | 0.181 | 0.399     | 0.549     | 0.415    | +1.53     | 0.008** |\\n| SciERC   | FS     | 529    | 16.6%  | 0.060  | 0.293 | 0.301 | 0.258 | 0.205 | 0.461     | 0.604     | 0.461    | -0.08     | 0.544   |\\n| CoNLL    | ZS     | 2756   | 67.7%  | -0.002 | 0.304 | 0.302 | 0.297 | 0.281 | 0.712     | 0.765     | 0.708    | -0.37     | n/a     |\\n| CoNLL    | FS     | 2756   | 70.0%  | 0.106  | 0.442 | 0.451 | 0.426 | 0.403 | 0.745     | 0.796     | 0.745    | +0.03     | 0.417   |\\n| FewNERD  | ZS     | 32565  | 46.2%  | 0.119  | 0.345 | 0.321 | 0.416 | 0.303 | 0.628     | 0.707     | 0.626    | -0.20     | n/a     |\\n| FewNERD  | FS     | 32565  | 45.2%  | 0.161  | 0.345 | 0.327 | 0.410 | 0.302 | 0.619     | 0.702     | 0.619    | +0.02     | 0.401   |\\n\\n### FewNERD FS Bootstrap 详情\\n- observed_diff: +0.000154 (+0.02pp)\\n- 95% CI: [-0.0011, +0.0014]\\n- p-value: 0.4005 (n.s.)\\n- Cohen's d: 0.0014\\n- Instance positive/negative/tied: 2752/2371/27442 (8.5%/7.3%/84.3%)\\n- Non-degen diff: +0.0002 (+0.02pp), p=0.4009\\n\\n### FS 效果总结\\nFew-shot 对基础 NER 性能提升显著：\\n- SciERC: F1 0.399→0.461 (+6.2pp)\\n- CoNLL: F1 0.712→0.745 (+3.3pp)\\n- FewNERD: F1 0.628→0.619 (-0.9pp, 略降)\\n\\n但 LP-weighted construction 在所有 FS 条件下均不显著：\\n- SciERC FS: Δ=-0.08pp (p=0.544)\\n- CoNLL FS: Δ=+0.03pp (p=0.417)\\n- FewNERD FS: Δ=+0.02pp (p=0.401)\\n\\n### Dual-gating hypothesis 评估\\n\\nConstruction 仅在 SciERC ZS 一个条件下显著（+1.53pp, p=0.008）。\\n\\n**Dual-gating 在 FT+ZS regime 内成立（6/6 条件一致）：**\\n- Degen gate 阈值约 22%（SciERC ZS 21.0% 刚好通过）\\n- Low degen + adequate LP ρ = construction works（SciERC ZS 证明）\\n- High degen（CoNLL ZS 67.7%, FewNERD ZS 46.2%）→ construction 失效，符合预期\\n\\n**FS regime 引入独立失效因素：**\\n- SciERC FS: degen=16.6% 满足 degen gate，但 LP ρ=0.06 极弱，construction 失效（Δ=-0.08pp, p=0.544）。说明 FS 有额外的降级机制（可能是 in-context examples 压缩了 LP 的区分力）\\n- CoNLL FS: degen=70.0% 远超阈值，construction 失效符合预期\\n- FewNERD FS: degen=45.2% 远超 <22% 的 degen gate 阈值，不 qualify 为 dual-gating 的反例，construction 失效符合预期\\n\\n**结论**：Dual-gating 在 FT+ZS regime 内是 construction 成功的充要条件。FS regime 引入独立失效因素，需单独分析——但 FS 的三个失效案例均不构成对 dual-gating 的挑战（FewNERD/CoNLL FS 因 degen 过高不满足 gate，SciERC FS 因 LP 退化不满足 signal gate）。\\n\\n### Signal 质量 ZS→FS 变化趋势\\n| Signal | SciERC ZS→FS | CoNLL ZS→FS | FewNERD ZS→FS |\\n|--------|-------------|-------------|---------------|\\n| LP ρ   | 0.081→0.060 ↓ | -0.002→0.106 ↑ | 0.119→0.161 ↑ |\\n| SJ ρ   | 0.217→0.293 ↑ | 0.304→0.442 ↑ | 0.345→0.345 = |\\n| FK ρ   | 0.227→0.301 ↑ | 0.302→0.451 ↑ | 0.321→0.327 ↑ |\\n| VC ρ   | 0.277→0.258 ↓ | 0.297→0.426 ↑ | 0.416→0.410 ↓ |\\n| EM ρ   | 0.181→0.205 ↑ | 0.281→0.403 ↑ | 0.303→0.302 = |\\n\\nFS 对 CoNLL 所有 signal 大幅提升（SJ +0.14, FK +0.15），但对 FewNERD/SciERC signal 变化有限。\\n\\n### 文件路径\\n- SciERC signals: output/72b_fewshot_signals/scierc/full_signal_report.json\\n- CoNLL signals: output/72b_fewshot_signals/conll2003/full_signal_report.json\\n- FewNERD signals: output/72b_fewshot_signals/fewnerd/full_signal_report.json\\n- SciERC bootstrap: output/72b_fewshot_signals/scierc/scierc_paired_bootstrap_result.json\\n- CoNLL bootstrap: output/72b_fewshot_signals/conll2003/conll2003_paired_bootstrap_result.json\\n- FewNERD bootstrap: output/72b_fewshot_signals/fewnerd/fewnerd_paired_bootstrap_result.json\\n- ZS report: output/72b_zeroshot/full_signal_report.json\\n- ZS bootstrap (SciERC): output/72b_zeroshot/scierc/paired_bootstrap_result.json\\n\", \"total_chars\": 3784, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
Now I have all the data. Let me compile the table:

| Dataset | Regime | Degen% | LP ρ | SJ ρ | FK ρ | VC ρ | Greedy F1 | Constr Δ | p |
|---------|--------|--------|------|------|------|------|-----------|----------|---|
| SciERC | ZS | 21.0 | 0.081 | 0.217 | 0.227 | 0.277 | 0.399 | +1.53 | 0.008 |


| SciERC | FS | 16.6 | 0.060 | 0.293 | 0.301 | 0.258 | 0.461 | -0.08 | 0.544 |
| CoNLL | ZS | 67.7 | -0.002 | 0.304 | 0.302 | 0.297 | 0.712 | -0.37 | — |
| CoNLL | FS | 70.0 | 0.106 | 0.442 | 0.451 | 0.426 | 0.745 | +0.03 | 0.417 |
| FewNER

Generating markdown table... Generating LaTeX table...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "ba07c17a-8c96-4f09-964a-7c084052987a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvwJURNVtM8FgVeq9Qr6ie",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3240,
      "cache_read_input_tokens": 25288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3240
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

_source line 14_

Memory has complete data including FK ρ for ZS. Now I'll create the table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "65b87a54-7118-4426-9978-2eb2996f0039",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvwJURNVtM8FgVeq9Qr6ie",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3240,
      "cache_read_input_tokens": 25288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3240
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

_source line 15_

<details open><summary>🔧 Tool call — Write · `toolu_018WtbhaiacaoBAHLtYxBgXQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/tab_72b_zs_vs_fs_appendix.tex",
  "content": "\\begin{table*}[t]\n\\centering\n\\caption{Full zero-shot vs.\\ few-shot comparison for Qwen2.5-72B-Instruct-AWQ ($N{=}8$). Only SciERC under zero-shot yields a significant construction gain.}\n\\label{tab:72b_zs_vs_fs}\n\\begin{tabular}{ll rrrrr rr r}\n\\toprule\nDataset & Regime & Degen\\% & LP $\\rho$ & SJ $\\rho$ & FK $\\rho$ & VC $\\rho$ & Greedy F1 & Constr $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC  & ZS & 21.0 & .081  & .217 & .227 & .277 & .399 & \\textbf{+1.53} & .008 \\\\\nSciERC  & FS & 16.6 & .060  & .293 & .301 & .258 & .461 & $-$0.08 & .544 \\\\\n\\midrule\nCoNLL   & ZS & 67.7 & $-$.002 & .304 & .302 & .297 & .712 & $-$0.37 & --- \\\\\nCoNLL   & FS & 70.0 & .106  & .442 & .451 & .426 & .745 & +0.03 & .417 \\\\\n\\midrule\nFewNERD & ZS & 46.2 & .119  & .345 & .321 & .416 & .628 & $-$0.20 & --- \\\\\nFewNERD & FS & 45.2 & .161  & .345 & .327 & .410 & .619 & +0.02 & .401 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "084824bb-81d2-4070-bb5a-6f3b2eb716e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvwJURNVtM8FgVeq9Qr6ie",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3240,
      "cache_read_input_tokens": 25288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3240
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

_source line 16 · 2026-05-20T01:35:42.162Z_

<details><summary>↩ Tool result · `toolu_018WtbhaiacaoBAHLtYxBgXQ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/tab_72b_zs_vs_fs_appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "e9f45690-9cfd-468c-bc60-25b965613eac",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/tab_72b_zs_vs_fs_appendix.tex",
    "content": "\\begin{table*}[t]\n\\centering\n\\caption{Full zero-shot vs.\\ few-shot comparison for Qwen2.5-72B-Instruct-AWQ ($N{=}8$). Only SciERC under zero-shot yields a significant construction gain.}\n\\label{tab:72b_zs_vs_fs}\n\\begin{tabular}{ll rrrrr rr r}\n\\toprule\nDataset & Regime & Degen\\% & LP $\\rho$ & SJ $\\rho$ & FK $\\rho$ & VC $\\rho$ & Greedy F1 & Constr $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC  & ZS & 21.0 & .081  & .217 & .227 & .277 & .399 & \\textbf{+1.53} & .008 \\\\\nSciERC  & FS & 16.6 & .060  & .293 & .301 & .258 & .461 & $-$0.08 & .544 \\\\\n\\midrule\nCoNLL   & ZS & 67.7 & $-$.002 & .304 & .302 & .297 & .712 & $-$0.37 & --- \\\\\nCoNLL   & FS & 70.0 & .106  & .442 & .451 & .426 & .745 & +0.03 & .417 \\\\\n\\midrule\nFewNERD & ZS & 46.2 & .119  & .345 & .321 & .416 & .628 & $-$0.20 & --- \\\\\nFewNERD & FS & 45.2 & .161  & .345 & .327 & .410 & .619 & +0.02 & .401 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 17_

表格已写入 `artifacts/tab_72b_zs_vs_fs_appendix.tex`。

**内容总结：**

6 行配置（3 datasets × ZS/FS），核心发现：

- **Construction 仅 SciERC ZS 显著**：Δ=**+1.53pp**, p=.008。其余 5 个条件 Δ 均在 ±0.4pp 以内且不显著。
- **FS 提升基础 F1 但不改善 construction**：SciERC +6.2pp（.399→.461），CoNLL +3.3pp（.712→.745），FewNERD 略降（.628→.619）。但 FS 条件下所有 construction Δ 均不显著（p ∈ [.401, .544]）。
- **Signal 质量**：FS 在 CoNLL 上大幅提升所有 signal（SJ +.14, FK +.15），但在 SciERC/FewNERD 上变化有限。FK ρ 数据完整（ZS 值来自 memory.md）。
- **Degeneracy**：CoNLL 两个 regime 均 ~68-70% 高退化；SciERC ZS 最低（21.0%），是唯一通过 dual-gating 的条件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "uuid": "5cf5cd84-0ecb-4790-8182-596b7d9cf717",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsLH2nvPojuyfsd8AWVL3i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 28528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1407
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

### Runtime record

_source line 18_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779253200,
    "rateLimitType": "seven_day",
    "utilization": 0.76,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "6f5c206f-011b-4cf0-9259-035b5a8f4ec4",
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07"
}
```

---

### Task result

_source line 19_

表格已写入 `artifacts/tab_72b_zs_vs_fs_appendix.tex`。

**内容总结：**

6 行配置（3 datasets × ZS/FS），核心发现：

- **Construction 仅 SciERC ZS 显著**：Δ=**+1.53pp**, p=.008。其余 5 个条件 Δ 均在 ±0.4pp 以内且不显著。
- **FS 提升基础 F1 但不改善 construction**：SciERC +6.2pp（.399→.461），CoNLL +3.3pp（.712→.745），FewNERD 略降（.628→.619）。但 FS 条件下所有 construction Δ 均不显著（p ∈ [.401, .544]）。
- **Signal 质量**：FS 在 CoNLL 上大幅提升所有 signal（SJ +.14, FK +.15），但在 SciERC/FewNERD 上变化有限。FK ρ 数据完整（ZS 值来自 memory.md）。
- **Degeneracy**：CoNLL 两个 regime 均 ~68-70% 高退化；SciERC ZS 最低（21.0%），是唯一通过 dual-gating 的条件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 56791,
  "duration_api_ms": 57570,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "6fe99682-3153-4550-bb3c-cbbab1bfeb07",
  "total_cost_usd": 0.228958,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 18094,
    "cache_read_input_tokens": 89701,
    "output_tokens": 2771,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 18094,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 372,
        "cache_read_input_tokens": 28528,
        "cache_creation_input_tokens": 1407,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1407
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1600,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0017050000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 2771,
      "cacheReadInputTokens": 89701,
      "cacheCreationInputTokens": 18094,
      "webSearchRequests": 0,
      "costUSD": 0.227253,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7dc12c13-6c73-4a95-9f3c-b8f89ccfe5dc"
}
```

</details>

---
