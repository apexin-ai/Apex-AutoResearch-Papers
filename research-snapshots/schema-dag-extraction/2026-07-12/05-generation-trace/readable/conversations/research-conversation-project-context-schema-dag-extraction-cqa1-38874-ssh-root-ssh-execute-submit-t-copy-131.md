# Research conversation: <project_context> # 项目: schema-dag-extraction ## 运行环境 - 服务器名: cqa1-38874 - SSH 账户: root（调用 ssh_execute / submit_training

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/b365b022-44d5-4c79-a1dc-0aafaae183ac.jsonl`
- **Structured JSON:** [`015e67c87a7e562e3a88.json`](../../sessions/01/015e67c87a7e562e3a88.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T21:37:07.097Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T21:37:07.097Z",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "content": "&lt;project_context>\n# 项目: schema-dag-extraction\n\n## 运行环境\n- 服务器名: cqa1-38874\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/schema-dag-extraction\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 论文中 count_40 子集必须明确说明 \"40-rel subsets sampled from the 80-relation pool\"，不能暗示是独立的 40-type pool（原因：count_40 实际是从 80-type pool 中采样的子集，不是独立构建的 pool。Reviewer 指出如果表述不清会误导读者认为存在三个独立 pool size）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：更新 experiment_plan.yaml 的 registry_id 字段\n\n### 目标\n5 个已完成的 planned 实验需要在 experiment_plan.yaml 中关联 registry_id。\n\n### 映射关系\n| plan_id | registry_id |\n|---------|-------------|\n| exp-005 | exp_docred_confusability |\n| exp-006 | exp006_interaction_2x2 |\n| exp-007 | exp007_error_taxonomy 或 exp016_fewrel_error_taxonomy（取较完整的） |\n| exp-013 | exp008_sdgd_v2_fewnerd + exp_confusability_batch_composition（备注已覆盖） |\n| exp-015 | exp015_scs_validation |\n\n### 步骤\n\n1. 先读取 experiment_plan.yaml，找到这 5 个 plan_id 的位置：\n```bash\n# 本地文件路径\ncat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml\n```\n如果文件不存在，检查：\n```bash\nfind /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ -name \"experiment_plan*\" 2>/dev/null\n```\n\n2. 用 `read_registry` 确认这些 registry_id 存在且状态正确：\n   - 读取 exp_docred_confusability, exp006_interaction_2x2, exp007_error_taxonomy, exp016_fewrel_error_taxonomy, exp008_sdgd_v2_fewnerd, exp_confusability_batch_composition, exp015_scs_validation\n\n3. 对于 exp-007，比较 `exp007_error_taxonomy` 和 `exp016_fewrel_error_taxonomy` 哪个更完整（看 metrics/conclusion），选更完整的\n\n4. 编辑 experiment_plan.yaml，在每个 plan entry 中添加或更新 `registry_id` 字段\n\n5. 对于 exp-013（映射到两个 registry 实验），用列表格式：\n```yaml\nregistry_id: \n  - exp008_sdgd_v2_fewnerd\n  - exp_confusability_batch_composition\n```\n并添加 note 说明已覆盖\n\n### 验证\n编辑完后确认 YAML 语法正确：\n```python\nimport yaml\nwith open('experiment_plan.yaml') as f:\n    data = yaml.safe_load(f)\nprint(\"Valid YAML\")\n```\n\n### 产出\n更新后的 experiment_plan.yaml（本地路径编辑）"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T21:37:07.101Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T21:37:07.101Z",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---

## Round 1

65 recorded events

### User

_source line 3 · 2026-05-18T21:37:07.145Z_

&lt;project_context>
# 项目: schema-dag-extraction

## 运行环境
- 服务器名: cqa1-38874
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.cqa1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/schema-dag-extraction

## ⚠️ 活跃约束（必须遵守）

- **C001**: 论文中 count_40 子集必须明确说明 "40-rel subsets sampled from the 80-relation pool"，不能暗示是独立的 40-type pool（原因：count_40 实际是从 80-type pool 中采样的子集，不是独立构建的 pool。Reviewer 指出如果表述不清会误导读者认为存在三个独立 pool size）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：更新 experiment_plan.yaml 的 registry_id 字段

### 目标
5 个已完成的 planned 实验需要在 experiment_plan.yaml 中关联 registry_id。

### 映射关系
| plan_id | registry_id |
|---------|-------------|
| exp-005 | exp_docred_confusability |
| exp-006 | exp006_interaction_2x2 |
| exp-007 | exp007_error_taxonomy 或 exp016_fewrel_error_taxonomy（取较完整的） |
| exp-013 | exp008_sdgd_v2_fewnerd + exp_confusability_batch_composition（备注已覆盖） |
| exp-015 | exp015_scs_validation |

### 步骤

1. 先读取 experiment_plan.yaml，找到这 5 个 plan_id 的位置：
```bash
# 本地文件路径
cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml
```
如果文件不存在，检查：
```bash
find /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/ -name "experiment_plan*" 2>/dev/null
```

2. 用 `read_registry` 确认这些 registry_id 存在且状态正确：
   - 读取 exp_docred_confusability, exp006_interaction_2x2, exp007_error_taxonomy, exp016_fewrel_error_taxonomy, exp008_sdgd_v2_fewnerd, exp_confusability_batch_composition, exp015_scs_validation

3. 对于 exp-007，比较 `exp007_error_taxonomy` 和 `exp016_fewrel_error_taxonomy` 哪个更完整（看 metrics/conclusion），选更完整的

4. 编辑 experiment_plan.yaml，在每个 plan entry 中添加或更新 `registry_id` 字段

5. 对于 exp-013（映射到两个 registry 实验），用列表格式：
```yaml
registry_id: 
  - exp008_sdgd_v2_fewnerd
  - exp_confusability_batch_composition
```
并添加 note 说明已覆盖

### 验证
编辑完后确认 YAML 语法正确：
```python
import yaml
with open('experiment_plan.yaml') as f:
    data = yaml.safe_load(f)
print("Valid YAML")
```

### 产出
更新后的 experiment_plan.yaml（本地路径编辑）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "43ddd370-79b0-4515-890d-45731f37001f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T21:37:07.145Z_

```json
{
  "parentUuid": "43ddd370-79b0-4515-890d-45731f37001f",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "cb629c1f-014e-4b83-aa2d-78a1a30d1513",
  "timestamp": "2026-05-18T21:37:07.145Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T21:37:07.145Z_

```json
{
  "parentUuid": "cb629c1f-014e-4b83-aa2d-78a1a30d1513",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c24931cb-a508-4517-b391-d3fe5bb503a6",
  "timestamp": "2026-05-18T21:37:07.145Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-18T21:37:07.145Z_

```json
{
  "parentUuid": "c24931cb-a508-4517-b391-d3fe5bb503a6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4ff63525-9494-4108-8181-e16b8069e818",
  "timestamp": "2026-05-18T21:37:07.145Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Update experiment_plan.yaml with registry_id mappings",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---

### Assistant

_source line 8 · 2026-05-18T21:37:09.460Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the experiment_plan.yaml file and checking the registry for the relevant experiment IDs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ff63525-9494-4108-8181-e16b8069e818",
  "isSidechain": false,
  "requestId": "req_011CbAknaSCjw4QwSxPT3fHV",
  "type": "assistant",
  "uuid": "2c18ac02-15dc-4895-b3e6-0fa332491a9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PU6qNwmLFsAxhjrEATTyS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13137,
      "cache_read_input_tokens": 11841,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 192,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13137
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T21:37:10.468Z_

<details open><summary>🔧 Tool call — Read · `toolu_019nkweMaSXb13wsJx2mcrEe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c18ac02-15dc-4895-b3e6-0fa332491a9c",
  "isSidechain": false,
  "requestId": "req_011CbAknaSCjw4QwSxPT3fHV",
  "type": "assistant",
  "uuid": "ad4c11c0-7795-4c04-b27c-9847abd5a93d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PU6qNwmLFsAxhjrEATTyS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13137,
      "cache_read_input_tokens": 11841,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 192,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13137
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T21:37:10.487Z_

<details><summary>↩ Tool result · `toolu_019nkweMaSXb13wsJx2mcrEe`</summary>

```text
1	experiments:
2	- id: exp-001
3	  claim:
4	  - 1
5	  - 2
6	  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]
7	    on Few-NERD with Qwen3-32B-FP8'
8	  priority: P0
9	  gpu_budget_hours: 3.5
10	  deps: []
11	  registry_id: exp001_count_baseline
12	  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction
13	    at low counts.
14	- id: exp-002
15	  claim:
16	  - 1
17	  - 2
18	  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,
19	    25 random + extreme batches on Few-NERD'
20	  priority: P0
21	  gpu_budget_hours: 3
22	  deps:
23	  - exp-001
24	  registry_id: exp002_confusability_controlled
25	  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion
26	    rate 10-28x.
27	- id: exp-003a
28	  claim:
29	  - 1
30	  - 2
31	  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination
32	    instruction. Re-run exp1+exp2.'
33	  priority: P0
34	  gpu_budget_hours: 3
35	  deps:
36	  - exp-001
37	  - exp-002
38	  registry_id: exp003a_prompt_v2_rerun
39	  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.
40	- id: exp-004
41	  claim:
42	  - 1
43	  - 2
44	  - 3
45	  description: 'MAVEN confusability study: count curve + within-count BCS correlation
46	    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core
47	    finding cross-task (NER→ED) with larger type space and known sibling confusion
48	    (14.6-19.8%).'
49	  priority: P0
50	  gpu_budget_hours: 4
51	  deps:
52	  - exp-003a
53	  registry_id: exp-004
54	  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs
55	    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy
56	    structure.'
57	- id: exp-005
58	  claim:
59	  - 1
60	  - 2
61	  description: 'DocRED confusability study: count curve + BCS correlation on DocRED
62	    (96 relation types). Scaling stress test.'
63	  priority: P1
64	  gpu_budget_hours: 5
65	  deps:
66	  - exp-003a
67	- id: exp-006
68	  claim:
69	  - 2
70	  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}
71	    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'
72	  priority: P1
73	  gpu_budget_hours: 2
74	  deps:
75	  - exp-003a
76	- id: exp-007
77	  claim:
78	  - 2
79	  description: 'Error taxonomy: systematic FP classification (type_substitution /
80	    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic
81	    evidence for multi-channel model.'
82	  priority: P1
83	  gpu_budget_hours: 1
84	  deps:
85	  - exp-002
86	  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic
87	    BCS-binned analysis.
88	- id: exp-012
89	  claim:
90	  - 1
91	  - 2
92	  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional
93	    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model
94	    generalizability.'
95	  priority: P0
96	  gpu_budget_hours: 6
97	  deps:
98	  - exp-003a
99	  registry_id: exp012_llama_8b_r3
100	- id: exp-016
101	  claim:
102	  - 1
103	  - 2
104	  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel
105	    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.
106	    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'
107	  priority: P0
108	  gpu_budget_hours: 4
109	  deps:
110	  - exp-003a
111	  registry_id: exp_fewrel_formal
112	  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full
113	    count curve after current run completes.
114	- id: exp-008
115	  claim:
116	  - 3
117	  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition
118	    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'
119	  priority: P0
120	  gpu_budget_hours: 3
121	  deps:
122	  - exp-003a
123	  registry_id: exp008_sdgd_v2_fewnerd
124	  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass
125	    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'
126	- id: exp-009
127	  claim:
128	  - 3
129	  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on
130	    168 event types. Compare vs single-pass + random batching. Cross-task validation
131	    of SDGD framework (NER→ED).'
132	  priority: P0
133	  gpu_budget_hours: 4
134	  deps:
135	  - exp-004
136	  - exp-008
137	- id: exp-010
138	  claim:
139	  - 3
140	  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration
141	    examples (no gradients). Compare vs SDGD-zero.'
142	  priority: P1
143	  gpu_budget_hours: 4
144	  deps:
145	  - exp-008
146	- id: exp-011
147	  claim:
148	  - 3
149	  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168
150	    event types. Full comparison table.'
151	  priority: P1
152	  gpu_budget_hours: 4
153	  deps:
154	  - exp-009
155	  - exp-010
156	- id: exp-013
157	  claim:
158	  - 3
159	  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.
160	    Isolates confusability-aware grouping from batch count reduction.'
161	  priority: P0
162	  gpu_budget_hours: 3
163	  deps:
164	  - exp-008
165	- id: exp-014
166	  claim:
167	  - 3
168	  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper
169	    bound on decomposition benefit. Reveals latency vs quality tradeoff.'
170	  priority: P1
171	  gpu_budget_hours: 3
172	  deps:
173	  - exp-008
174	- id: exp-015
175	  claim:
176	  - 1
177	  description: 'SCS validation: Spearman/Kendall rank correlation between embedding
178	    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'
179	  priority: P1
180	  gpu_budget_hours: 1
181	  deps:
182	  - exp-010
183	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad4c11c0-7795-4c04-b27c-9847abd5a93d",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "43a63564-788e-4a34-8fae-a8e6859eb721",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
      "content": "experiments:\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_8b_r3\n- id: exp-016\n  claim:\n  - 1\n  - 2\n  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel\n    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.\n    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp_fewrel_formal\n  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full\n    count curve after current run completes.\n- id: exp-008\n  claim:\n  - 3\n  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition\n    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-003a\n  registry_id: exp008_sdgd_v2_fewnerd\n  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass\n    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'\n- id: exp-009\n  claim:\n  - 3\n  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on\n    168 event types. Compare vs single-pass + random batching. Cross-task validation\n    of SDGD framework (NER→ED).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-004\n  - exp-008\n- id: exp-010\n  claim:\n  - 3\n  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration\n    examples (no gradients). Compare vs SDGD-zero.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-008\n- id: exp-011\n  claim:\n  - 3\n  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168\n    event types. Full comparison table.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-009\n  - exp-010\n- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n- id: exp-014\n  claim:\n  - 3\n  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper\n    bound on decomposition benefit. Reveals latency vs quality tradeoff.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n",
      "numLines": 183,
      "startLine": 1,
      "totalLines": 183
    }
  },
  "sourceToolAssistantUUID": "ad4c11c0-7795-4c04-b27c-9847abd5a93d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T21:37:10.969Z_

<details><summary>↩ Tool result · `toolu_01XpAtrSZh4kebHQkr7MMf9t`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad09ecf0-e88c-4301-949c-92dabacf8345",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "715df900-5031-4995-892d-462e3e4466c0",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "ad09ecf0-e88c-4301-949c-92dabacf8345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T21:37:10.964Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XpAtrSZh4kebHQkr7MMf9t`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43a63564-788e-4a34-8fae-a8e6859eb721",
  "isSidechain": false,
  "requestId": "req_011CbAknaSCjw4QwSxPT3fHV",
  "type": "assistant",
  "uuid": "ad09ecf0-e88c-4301-949c-92dabacf8345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019PU6qNwmLFsAxhjrEATTyS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13137,
      "cache_read_input_tokens": 11841,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 192,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13137
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-18T21:37:14.211Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the registry entries for the relevant experiment IDs to confirm they exist and check their status. Let me query them all.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "715df900-5031-4995-892d-462e3e4466c0",
  "isSidechain": false,
  "requestId": "req_011CbAknrve9aQNDwWjudRYZ",
  "type": "assistant",
  "uuid": "92bcd68c-a1dc-45fb-910c-353764d981f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jhdqqgjphwm2nGF2ejf1o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 24978,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 626,
          "cache_read_input_tokens": 24978,
          "cache_creation_input_tokens": 2959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T21:37:15.166Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01R8Ud4TsouYcBJSyRgnKFeJ`</summary>

```json
{
  "project": "schema-dag-extraction",
  "filters": {
    "experiment_id": "exp_docred_confusability"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92bcd68c-a1dc-45fb-910c-353764d981f4",
  "isSidechain": false,
  "requestId": "req_011CbAknrve9aQNDwWjudRYZ",
  "type": "assistant",
  "uuid": "58ad6f5c-a032-45c5-901f-156972116d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jhdqqgjphwm2nGF2ejf1o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 24978,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 626,
          "cache_read_input_tokens": 24978,
          "cache_creation_input_tokens": 2959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T21:37:15.450Z_

<details><summary>↩ Tool result · `toolu_01R8Ud4TsouYcBJSyRgnKFeJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2713}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58ad6f5c-a032-45c5-901f-156972116d09",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "55720cc4-e7e1-43f6-a6bf-21a058b10cbb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2713}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2713}}"
    }
  },
  "sourceToolAssistantUUID": "58ad6f5c-a032-45c5-901f-156972116d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T21:37:16.111Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011yErWgUPM4EWTWDzaveFoX`</summary>

```json
{
  "project": "schema-dag-extraction",
  "filters": {
    "experiment_id": "exp006_interaction_2x2"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55720cc4-e7e1-43f6-a6bf-21a058b10cbb",
  "isSidechain": false,
  "requestId": "req_011CbAknrve9aQNDwWjudRYZ",
  "type": "assistant",
  "uuid": "770ba222-522c-40e9-aa17-1ff0290f2800",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jhdqqgjphwm2nGF2ejf1o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 24978,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 626,
          "cache_read_input_tokens": 24978,
          "cache_creation_input_tokens": 2959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T21:37:16.357Z_

<details><summary>↩ Tool result · `toolu_011yErWgUPM4EWTWDzaveFoX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2309}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "770ba222-522c-40e9-aa17-1ff0290f2800",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "cb932752-7a0a-4d3b-875b-e4a529d09614",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2309}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2309}}"
    }
  },
  "sourceToolAssistantUUID": "770ba222-522c-40e9-aa17-1ff0290f2800",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T21:37:16.585Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019HqbuzsvWi3MBQ1SS3qm5j`</summary>

```json
{
  "project": "schema-dag-extraction",
  "filters": {
    "experiment_id": "exp007_error_taxonomy"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb932752-7a0a-4d3b-875b-e4a529d09614",
  "isSidechain": false,
  "requestId": "req_011CbAknrve9aQNDwWjudRYZ",
  "type": "assistant",
  "uuid": "dde0fdfd-0ad1-487c-ad5c-b7bc19f62bd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jhdqqgjphwm2nGF2ejf1o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 24978,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 626,
          "cache_read_input_tokens": 24978,
          "cache_creation_input_tokens": 2959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T21:37:16.813Z_

<details><summary>↩ Tool result · `toolu_019HqbuzsvWi3MBQ1SS3qm5j`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2159}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dde0fdfd-0ad1-487c-ad5c-b7bc19f62bd2",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "86f9fa14-5871-408c-bc53-900cd113bedd",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2159}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2159}}"
    }
  },
  "sourceToolAssistantUUID": "dde0fdfd-0ad1-487c-ad5c-b7bc19f62bd2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T21:37:17.530Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019titViKEJNHXitiek2xdHE`</summary>

```json
{
  "project": "schema-dag-extraction",
  "filters": {
    "experiment_id": "exp016_fewrel_error_taxonomy"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86f9fa14-5871-408c-bc53-900cd113bedd",
  "isSidechain": false,
  "requestId": "req_011CbAknrve9aQNDwWjudRYZ",
  "type": "assistant",
  "uuid": "d1adb254-09b2-4044-8e51-6f454f887501",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jhdqqgjphwm2nGF2ejf1o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 24978,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 626,
          "cache_read_input_tokens": 24978,
          "cache_creation_input_tokens": 2959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T21:37:17.782Z_

<details><summary>↩ Tool result · `toolu_019titViKEJNHXitiek2xdHE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2351}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1adb254-09b2-4044-8e51-6f454f887501",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "dba7d248-9c78-4ab2-a864-692efb279ed8",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2351}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2351}}"
    }
  },
  "sourceToolAssistantUUID": "d1adb254-09b2-4044-8e51-6f454f887501",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T21:37:18.472Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01DsGvExECh9kMF962DX7Fp5`</summary>

```json
{
  "project": "schema-dag-extraction",
  "filters": {
    "experiment_id": "exp008_sdgd_v2_fewnerd"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dba7d248-9c78-4ab2-a864-692efb279ed8",
  "isSidechain": false,
  "requestId": "req_011CbAknrve9aQNDwWjudRYZ",
  "type": "assistant",
  "uuid": "84596426-321e-4467-bf04-ebd77a475ace",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jhdqqgjphwm2nGF2ejf1o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 24978,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 626,
          "cache_read_input_tokens": 24978,
          "cache_creation_input_tokens": 2959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T21:37:18.859Z_

<details><summary>↩ Tool result · `toolu_01DsGvExECh9kMF962DX7Fp5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3652}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84596426-321e-4467-bf04-ebd77a475ace",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "4b7ac2b8-5530-40d1-937e-0093dfccd7b5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3652}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3652}}"
    }
  },
  "sourceToolAssistantUUID": "84596426-321e-4467-bf04-ebd77a475ace",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T21:37:18.951Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_015XWc1ZrQe86X174vbfS8ho`</summary>

```json
{
  "project": "schema-dag-extraction",
  "filters": {
    "experiment_id": "exp_confusability_batch_composition"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b7ac2b8-5530-40d1-937e-0093dfccd7b5",
  "isSidechain": false,
  "requestId": "req_011CbAknrve9aQNDwWjudRYZ",
  "type": "assistant",
  "uuid": "91aa7fbd-69a7-4e1f-bdd5-b860cca21253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jhdqqgjphwm2nGF2ejf1o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 24978,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 626,
          "cache_read_input_tokens": 24978,
          "cache_creation_input_tokens": 2959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T21:37:19.410Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Xiobz6wLEcwDJbqpkqZ8HU`</summary>

```json
{
  "project": "schema-dag-extraction",
  "filters": {
    "experiment_id": "exp015_scs_validation"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91aa7fbd-69a7-4e1f-bdd5-b860cca21253",
  "isSidechain": false,
  "requestId": "req_011CbAknrve9aQNDwWjudRYZ",
  "type": "assistant",
  "uuid": "a60c4483-10c2-460f-98aa-d8528ea634cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jhdqqgjphwm2nGF2ejf1o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 24978,
      "output_tokens": 626,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 626,
          "cache_read_input_tokens": 24978,
          "cache_creation_input_tokens": 2959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2959
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T21:37:19.583Z_

<details><summary>↩ Tool result · `toolu_015XWc1ZrQe86X174vbfS8ho`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6031}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91aa7fbd-69a7-4e1f-bdd5-b860cca21253",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "839ca5fd-d88c-4488-a9bb-88b4dd782c8f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.6031}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6031}}"
    }
  },
  "sourceToolAssistantUUID": "91aa7fbd-69a7-4e1f-bdd5-b860cca21253",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "leafUuid": "839ca5fd-d88c-4488-a9bb-88b4dd782c8f",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Update experiment_plan.yaml with registry_id mappings",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---

### Tool result

_source line 29 · 2026-05-18T21:37:19.964Z_

<details><summary>↩ Tool result · `toolu_01Xiobz6wLEcwDJbqpkqZ8HU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3557}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a60c4483-10c2-460f-98aa-d8528ea634cd",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "a1a7dc8c-4050-4baa-85f8-e91b48c055d6",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3557}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3557}}"
    }
  },
  "sourceToolAssistantUUID": "a60c4483-10c2-460f-98aa-d8528ea634cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-18T21:37:22.576Z_

<details><summary>Logged reasoning block</summary>

```text
All returned 0 results. The `experiment_id` filter might not be the right field name. Let me try reading all experiments to see the structure and find the correct field names.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1a7dc8c-4050-4baa-85f8-e91b48c055d6",
  "isSidechain": false,
  "requestId": "req_011CbAkoX8J3EfEtje6v2EUy",
  "type": "assistant",
  "uuid": "aa6aff90-8911-4771-9dfe-cd1ce673e2b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLe8CjZD6heWRLp36rfT6c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1333,
      "cache_read_input_tokens": 27937,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 27937,
          "cache_creation_input_tokens": 1333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1333
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-18T21:37:23.576Z_

所有按 `experiment_id` 过滤都返回 0 条。让我看一下 registry 的实际结构。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa6aff90-8911-4771-9dfe-cd1ce673e2b6",
  "isSidechain": false,
  "requestId": "req_011CbAkoX8J3EfEtje6v2EUy",
  "type": "assistant",
  "uuid": "db6547cc-e40a-499c-89da-8b2a1b9c7f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLe8CjZD6heWRLp36rfT6c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1333,
      "cache_read_input_tokens": 27937,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 27937,
          "cache_creation_input_tokens": 1333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1333
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-18T21:37:24.177Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01DfhdKLtSyFCH61g542PmA3`</summary>

```json
{
  "project": "schema-dag-extraction",
  "limit": 5,
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db6547cc-e40a-499c-89da-8b2a1b9c7f23",
  "isSidechain": false,
  "requestId": "req_011CbAkoX8J3EfEtje6v2EUy",
  "type": "assistant",
  "uuid": "1b8042fc-0bfb-42f8-b8e7-06e8ac29e512",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLe8CjZD6heWRLp36rfT6c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1333,
      "cache_read_input_tokens": 27937,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 27937,
          "cache_creation_input_tokens": 1333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1333
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-18T21:37:24.389Z_

<details><summary>↩ Tool result · `toolu_01DfhdKLtSyFCH61g542PmA3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_unconstrained_decoding_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T09:54:50.724Z\", \"updated_at\": \"2026-05-18T14:22:10.672Z\", \"hypothesis\": \"The BCS-accuracy correlation in RE arises from semantic confusion rather than forced-choice format artifacts. If removing the enum constraint (relaxed decoding) preserves the negative BCS-accuracy correlation direction and significance, confusability is a genuine semantic property; if the correlation disappears, the effect is specific to constrained classification where all errors are channeled into type substitution. Either outcome strengthens the paper: preservation broadens the claim, disappearance validates the error-channeling hypothesis stated in Discussion.\", \"parent\": \"exp_fewrel_formal_80rel\", \"spec\": {\"command\": \"bash -c \\\"cd /root/schema-dag-extraction && source /root/miniconda3/bin/activate base && python src/run_unconstrained_decoding_ablation.py\\\"\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"542072\", \"log_path\": \"~/runs/schema-dag-extraction/exp_unconstrained_decoding_ablation.log\", \"submitted_at\": \"2026-05-18T10:21:03.700Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1903.1, \"gpu_hours\": 0.53}, \"conclusion\": \"success\", \"metrics\": {\"n10\": {\"low_bcs_mean_acc\": 0.8042, \"high_bcs_mean_acc\": 0.725, \"delta_pp\": 7.92, \"spearman_rho\": -0.4303, \"spearman_pval\": 0.214, \"oov_rate\": 0}, \"n25\": {\"low_bcs_mean_acc\": 0.8093, \"high_bcs_mean_acc\": 0.7812, \"delta_pp\": 2.8, \"ci_95_lower_pp\": -4.53, \"ci_95_upper_pp\": 10.56, \"spearman_rho\": -0.1442, \"spearman_pval\": 0.492, \"oov_rate\": 0.0008, \"total_samples\": 2400}}, \"log_path\": \"/root/schema-dag-extraction/results/unconstrained_decoding_ablation/\", \"checkpoint_path\": \"N/A (inference-only ablation)\", \"completed_at\": \"2026-05-18T10:52:46.803Z\"}, \"exp_multiseed_bcs_re\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:44:12.639Z\", \"updated_at\": \"2026-05-18T08:07:35.728Z\", \"hypothesis\": \"The BCS-accuracy correlation observed in FewRel BCS-controlled experiments (R²=0.22-0.53) is robust across random seeds. If seed=123 and seed=456 replicate the negative BCS-accuracy correlation direction and significance observed with seed=42, this confirms the finding is not a single-seed artifact. Rebuttal material for R15-W2 single-seed concern.\", \"parent\": \"exp_fewrel_formal_80rel\", \"server\": \"cqa1-38874\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-38874\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T07:24:36.762Z\"}, \"spec\": {\"command\": \"bash /root/schema-dag-extraction/scripts/run_multiseed_bcs.sh\", \"server\": \"cqa1-38874\", \"data_path\": \"data/fewrel/fewrel_samples_960.json\", \"data_count\": 14400, \"model_name\": \"Qwen3-32B-FP8\", \"seed\": \"123,456\", \"gpu\": \"cuda:0\", \"pid\": 531145, \"checkpoint_source\": \"Qwen3-32B-FP8 (vLLM inference, no training checkpoint)\", \"eval_data\": \"FewRel 80-rel BCS-controlled batches (25 low-BCS + 25 high-BCS)\", \"note\": \"50 batches x 3 shot conditions x 2 seeds = 300 batches total. Started via nohup (worker bypassed submit_training_job).\"}, \"conclusion\": \"success\", \"log_path\": \"/root/schema-dag-extraction/artifacts/multiseed_bcs_re/run_all.log\", \"checkpoint_path\": \"/root/schema-dag-extraction/artifacts/multiseed_bcs_re/\", \"completed_at\": \"2026-05-18T08:07:29.393Z\", \"metrics\": {\"seed_123\": {\"shot0_delta_pp\": 21.88, \"shot1_delta_pp\": 25.25, \"shot5_delta_pp\": 24.25, \"shot0_ci\": [18.79, 24.83], \"shot1_ci\": [21.08, 29.29], \"shot5_ci\": [19.96, 28.29]}, \"seed_456\": {\"shot0_delta_pp\": 22.38, \"shot1_delta_pp\": 24.38, \"shot5_delta_pp\": 25.08, \"shot0_ci\": [19.58, 24.96], \"shot1_ci\": [20.58, 28.04], \"shot5_ci\": [21.62, 28.58]}, \"finding\": \"Few-shot does NOT mitigate BCS effect; delta increases from ~22pp (0-shot) to ~25pp (5-shot)\"}}, \"exp_gemini_flash_cross_model\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:57:39.493Z\", \"updated_at\": \"2026-05-18T07:36:32.176Z\", \"hypothesis\": \"The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open-weight Qwen/LLaMA + proprietary Gemini).\", \"spec\": {\"command\": \"python3 scripts/run_gemini_flash_fewrel.py --mode all --sleep 0.15\", \"server\": \"local (tmux session: gemini_flash)\", \"data_path\": \"data/fewrel/fewrel_samples_960.json\", \"data_count\": 960, \"model_name\": \"gemini-2.5-flash\", \"seed\": 42}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T02:11:13.608Z\", \"metrics\": {\"count_curve_spearman_rho\": -0.943, \"count_curve_spearman_p\": 0.0048, \"count_1_acc\": 0.8267, \"count_4_acc\": 0.8725, \"count_8_acc\": 0.8204, \"count_16_acc\": 0.7868, \"count_32_acc\": 0.7394, \"count_64_acc\": 0.6343, \"total_drop_count1_to_64_pp\": -19.2, \"complete_count_levels\": \"1,4,8,16,32\", \"partial_count_levels\": \"64 (11/25)\", \"missing\": \"count_80, part2_bcs\", \"note\": \"tmux resumed, still collecting remaining data\"}, \"notes\": \"Gemini 2.5 Flash count curve via local API call. Count 1-32 complete (25 batches each), count 64 partial (11/25). Data at artifacts/exp_gemini_flash/part1/count_curve_analysis.json. Count 80 and part2 BCS not yet collected.\"}, \"exp_schema_intervention\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:57:35.343Z\", \"updated_at\": \"2026-05-17T16:25:52.346Z\", \"hypothesis\": \"If type confusability is a causal driver of extraction errors, then renaming high-BCS type pairs to reduce embedding similarity (while preserving semantic equivalence) should improve accuracy on high-BCS batches. This tests the causal direction: SCS → confusion, not merely correlation. If treatment (renamed) accuracy on previously-high-BCS batches improves significantly over control (original names), confusability is actionable via schema design.\", \"spec\": {\"command\": \"python /root/schema-dag-extraction/scripts/run_schema_intervention.py\", \"server\": \"cqa1-38874\", \"data_path\": \"/root/schema-dag-extraction/data/fewrel/\", \"data_count\": 960, \"model_name\": \"Qwen3-32B-FP8\", \"seed\": 42, \"checkpoint_path\": \"/root/schema-dag-extraction/artifacts/exp_schema_intervention/\", \"log_path\": \"/root/schema-dag-extraction/artifacts/exp_schema_intervention/\"}, \"conclusion\": \"negative\", \"metrics\": {\"high_bcs_control\": 0.693, \"high_bcs_treatment\": 0.605, \"high_bcs_delta\": -0.0883, \"low_bcs_control\": 0.901, \"low_bcs_treatment\": 0.871, \"low_bcs_delta\": -0.0296, \"interaction_delta\": -0.0588, \"interaction_p\": \"<0.001\", \"interaction_t\": -7.23, \"rename_count_correlation_r\": -0.625, \"rename_count_correlation_p\": \"<0.001\", \"cohens_d_high\": -2.92, \"cohens_d_low\": -1.09}, \"completed_at\": \"2026-05-17T16:25:52.346Z\"}, \"exp_fewshot_bcs_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:18:15.923Z\", \"updated_at\": \"2026-05-17T14:08:59.677Z\", \"hypothesis\": \"Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples, tested on extreme-BCS batches (low ~0.36, high ~0.80) where 0-shot delta is ~25-31pp. If delta shrinks significantly under few-shot, confusability is addressable via prompting. If delta persists, confusability is a fundamental schema-structural constraint.\", \"parent\": \"exp_fewrel_v2_n25\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/schema-dag-extraction && python3 src/run_fewshot_bcs_v2.py --stage all --n_shots 0 1 5 --seed 42\\\"\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"480497\", \"log_path\": \"~/runs/schema-dag-extraction/exp_fewshot_bcs_v2.log\", \"submitted_at\": \"2026-05-17T13:39:04.351Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema-dag-extraction/data/exp_v2_re_n25/batch_groups.json\", \"data_count\": \"50 batches (25 low-BCS ~0.36, 25 high-BCS ~0.80) x 3 shots = 450 tasks\", \"model_name\": \"Qwen3-32B-FP8\", \"seed\": 42, \"checkpoint_source\": \"Qwen3-32B-FP8 (vLLM served, no fine-tuning)\", \"eval_data\": \"FewRel extreme-BCS batches from exp_fewrel_v2_n25/batch_groups.json\", \"wall_clock_seconds\": 1727.9, \"gpu_hours\": 0.48}, \"reproduce\": {\"finished_at\": \"2026-05-17T14:03:41.759Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:03:47.723099+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"0shot_low_bcs\": 0.6821, \"0shot_high_bcs\": 0.4975, \"0shot_delta_pp\": 18.46, \"1shot_low_bcs\": 0.7538, \"1shot_high_bcs\": 0.5542, \"1shot_delta_pp\": 19.96, \"5shot_low_bcs\": 0.7154, \"5shot_high_bcs\": 0.4875, \"5shot_delta_pp\": 22.79, \"delta_widening_0to5shot_pp\": 4.33, \"widening_p_value\": 0.014}, \"checkpoint_path\": \"/root/schema-dag-extraction/artifacts/fewshot_bcs_v2/analysis.json\", \"log_path\": \"~/runs/schema-dag-extraction/exp_fewshot_bcs_v2.log\", \"completed_at\": \"2026-05-17T14:07:52.204Z\"}}, \"count\": 5, \"total\": 62, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2016}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b8042fc-0bfb-42f8-b8e7-06e8ac29e512",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "fd0ced10-615c-40e3-b2a6-1bc9caa485d1",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_unconstrained_decoding_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T09:54:50.724Z\\\", \\\"updated_at\\\": \\\"2026-05-18T14:22:10.672Z\\\", \\\"hypothesis\\\": \\\"The BCS-accuracy correlation in RE arises from semantic confusion rather than forced-choice format artifacts. If removing the enum constraint (relaxed decoding) preserves the negative BCS-accuracy correlation direction and significance, confusability is a genuine semantic property; if the correlation disappears, the effect is specific to constrained classification where all errors are channeled into type substitution. Either outcome strengthens the paper: preservation broadens the claim, disappearance validates the error-channeling hypothesis stated in Discussion.\\\", \\\"parent\\\": \\\"exp_fewrel_formal_80rel\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"cd /root/schema-dag-extraction && source /root/miniconda3/bin/activate base && python src/run_unconstrained_decoding_ablation.py\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"542072\\\", \\\"log_path\\\": \\\"~/runs/schema-dag-extraction/exp_unconstrained_decoding_ablation.log\\\", \\\"submitted_at\\\": \\\"2026-05-18T10:21:03.700Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"wall_clock_seconds\\\": 1903.1, \\\"gpu_hours\\\": 0.53}, \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n10\\\": {\\\"low_bcs_mean_acc\\\": 0.8042, \\\"high_bcs_mean_acc\\\": 0.725, \\\"delta_pp\\\": 7.92, \\\"spearman_rho\\\": -0.4303, \\\"spearman_pval\\\": 0.214, \\\"oov_rate\\\": 0}, \\\"n25\\\": {\\\"low_bcs_mean_acc\\\": 0.8093, \\\"high_bcs_mean_acc\\\": 0.7812, \\\"delta_pp\\\": 2.8, \\\"ci_95_lower_pp\\\": -4.53, \\\"ci_95_upper_pp\\\": 10.56, \\\"spearman_rho\\\": -0.1442, \\\"spearman_pval\\\": 0.492, \\\"oov_rate\\\": 0.0008, \\\"total_samples\\\": 2400}}, \\\"log_path\\\": \\\"/root/schema-dag-extraction/results/unconstrained_decoding_ablation/\\\", \\\"checkpoint_path\\\": \\\"N/A (inference-only ablation)\\\", \\\"completed_at\\\": \\\"2026-05-18T10:52:46.803Z\\\"}, \\\"exp_multiseed_bcs_re\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T06:44:12.639Z\\\", \\\"updated_at\\\": \\\"2026-05-18T08:07:35.728Z\\\", \\\"hypothesis\\\": \\\"The BCS-accuracy correlation observed in FewRel BCS-controlled experiments (R²=0.22-0.53) is robust across random seeds. If seed=123 and seed=456 replicate the negative BCS-accuracy correlation direction and significance observed with seed=42, this confirms the finding is not a single-seed artifact. Rebuttal material for R15-W2 single-seed concern.\\\", \\\"parent\\\": \\\"exp_fewrel_formal_80rel\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"account\\\": \\\"root\\\", \\\"reproduce\\\": {\\\"server\\\": \\\"cqa1-38874\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"started_at\\\": \\\"2026-05-18T07:24:36.762Z\\\"}, \\\"spec\\\": {\\\"command\\\": \\\"bash /root/schema-dag-extraction/scripts/run_multiseed_bcs.sh\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"data_path\\\": \\\"data/fewrel/fewrel_samples_960.json\\\", \\\"data_count\\\": 14400, \\\"model_name\\\": \\\"Qwen3-32B-FP8\\\", \\\"seed\\\": \\\"123,456\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 531145, \\\"checkpoint_source\\\": \\\"Qwen3-32B-FP8 (vLLM inference, no training checkpoint)\\\", \\\"eval_data\\\": \\\"FewRel 80-rel BCS-controlled batches (25 low-BCS + 25 high-BCS)\\\", \\\"note\\\": \\\"50 batches x 3 shot conditions x 2 seeds = 300 batches total. Started via nohup (worker bypassed submit_training_job).\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"log_path\\\": \\\"/root/schema-dag-extraction/artifacts/multiseed_bcs_re/run_all.log\\\", \\\"checkpoint_path\\\": \\\"/root/schema-dag-extraction/artifacts/multiseed_bcs_re/\\\", \\\"completed_at\\\": \\\"2026-05-18T08:07:29.393Z\\\", \\\"metrics\\\": {\\\"seed_123\\\": {\\\"shot0_delta_pp\\\": 21.88, \\\"shot1_delta_pp\\\": 25.25, \\\"shot5_delta_pp\\\": 24.25, \\\"shot0_ci\\\": [18.79, 24.83], \\\"shot1_ci\\\": [21.08, 29.29], \\\"shot5_ci\\\": [19.96, 28.29]}, \\\"seed_456\\\": {\\\"shot0_delta_pp\\\": 22.38, \\\"shot1_delta_pp\\\": 24.38, \\\"shot5_delta_pp\\\": 25.08, \\\"shot0_ci\\\": [19.58, 24.96], \\\"shot1_ci\\\": [20.58, 28.04], \\\"shot5_ci\\\": [21.62, 28.58]}, \\\"finding\\\": \\\"Few-shot does NOT mitigate BCS effect; delta increases from ~22pp (0-shot) to ~25pp (5-shot)\\\"}}, \\\"exp_gemini_flash_cross_model\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T14:57:39.493Z\\\", \\\"updated_at\\\": \\\"2026-05-18T07:36:32.176Z\\\", \\\"hypothesis\\\": \\\"The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open-weight Qwen/LLaMA + proprietary Gemini).\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 scripts/run_gemini_flash_fewrel.py --mode all --sleep 0.15\\\", \\\"server\\\": \\\"local (tmux session: gemini_flash)\\\", \\\"data_path\\\": \\\"data/fewrel/fewrel_samples_960.json\\\", \\\"data_count\\\": 960, \\\"model_name\\\": \\\"gemini-2.5-flash\\\", \\\"seed\\\": 42}, \\\"failure_reason\\\": \\\"startup recovery: RUNNING with no cron and no server/pid info\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-18T02:11:13.608Z\\\", \\\"metrics\\\": {\\\"count_curve_spearman_rho\\\": -0.943, \\\"count_curve_spearman_p\\\": 0.0048, \\\"count_1_acc\\\": 0.8267, \\\"count_4_acc\\\": 0.8725, \\\"count_8_acc\\\": 0.8204, \\\"count_16_acc\\\": 0.7868, \\\"count_32_acc\\\": 0.7394, \\\"count_64_acc\\\": 0.6343, \\\"total_drop_count1_to_64_pp\\\": -19.2, \\\"complete_count_levels\\\": \\\"1,4,8,16,32\\\", \\\"partial_count_levels\\\": \\\"64 (11/25)\\\", \\\"missing\\\": \\\"count_80, part2_bcs\\\", \\\"note\\\": \\\"tmux resumed, still collecting remaining data\\\"}, \\\"notes\\\": \\\"Gemini 2.5 Flash count curve via local API call. Count 1-32 complete (25 batches each), count 64 partial (11/25). Data at artifacts/exp_gemini_flash/part1/count_curve_analysis.json. Count 80 and part2 BCS not yet collected.\\\"}, \\\"exp_schema_intervention\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T14:57:35.343Z\\\", \\\"updated_at\\\": \\\"2026-05-17T16:25:52.346Z\\\", \\\"hypothesis\\\": \\\"If type confusability is a causal driver of extraction errors, then renaming high-BCS type pairs to reduce embedding similarity (while preserving semantic equivalence) should improve accuracy on high-BCS batches. This tests the causal direction: SCS → confusion, not merely correlation. If treatment (renamed) accuracy on previously-high-BCS batches improves significantly over control (original names), confusability is actionable via schema design.\\\", \\\"spec\\\": {\\\"command\\\": \\\"python /root/schema-dag-extraction/scripts/run_schema_intervention.py\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"data_path\\\": \\\"/root/schema-dag-extraction/data/fewrel/\\\", \\\"data_count\\\": 960, \\\"model_name\\\": \\\"Qwen3-32B-FP8\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"/root/schema-dag-extraction/artifacts/exp_schema_intervention/\\\", \\\"log_path\\\": \\\"/root/schema-dag-extraction/artifacts/exp_schema_intervention/\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"high_bcs_control\\\": 0.693, \\\"high_bcs_treatment\\\": 0.605, \\\"high_bcs_delta\\\": -0.0883, \\\"low_bcs_control\\\": 0.901, \\\"low_bcs_treatment\\\": 0.871, \\\"low_bcs_delta\\\": -0.0296, \\\"interaction_delta\\\": -0.0588, \\\"interaction_p\\\": \\\"<0.001\\\", \\\"interaction_t\\\": -7.23, \\\"rename_count_correlation_r\\\": -0.625, \\\"rename_count_correlation_p\\\": \\\"<0.001\\\", \\\"cohens_d_high\\\": -2.92, \\\"cohens_d_low\\\": -1.09}, \\\"completed_at\\\": \\\"2026-05-17T16:25:52.346Z\\\"}, \\\"exp_fewshot_bcs_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-17T13:18:15.923Z\\\", \\\"updated_at\\\": \\\"2026-05-17T14:08:59.677Z\\\", \\\"hypothesis\\\": \\\"Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples, tested on extreme-BCS batches (low ~0.36, high ~0.80) where 0-shot delta is ~25-31pp. If delta shrinks significantly under few-shot, confusability is addressable via prompting. If delta persists, confusability is a fundamental schema-structural constraint.\\\", \\\"parent\\\": \\\"exp_fewrel_v2_n25\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/bin/activate base && cd /root/schema-dag-extraction && python3 src/run_fewshot_bcs_v2.py --stage all --n_shots 0 1 5 --seed 42\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-38874\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"480497\\\", \\\"log_path\\\": \\\"~/runs/schema-dag-extraction/exp_fewshot_bcs_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-17T13:39:04.351Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"/root/schema-dag-extraction/data/exp_v2_re_n25/batch_groups.json\\\", \\\"data_count\\\": \\\"50 batches (25 low-BCS ~0.36, 25 high-BCS ~0.80) x 3 shots = 450 tasks\\\", \\\"model_name\\\": \\\"Qwen3-32B-FP8\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"Qwen3-32B-FP8 (vLLM served, no fine-tuning)\\\", \\\"eval_data\\\": \\\"FewRel extreme-BCS batches from exp_fewrel_v2_n25/batch_groups.json\\\", \\\"wall_clock_seconds\\\": 1727.9, \\\"gpu_hours\\\": 0.48}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-17T14:03:41.759Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-17T14:03:47.723099+00:00\\\"}]}, \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"0shot_low_bcs\\\": 0.6821, \\\"0shot_high_bcs\\\": 0.4975, \\\"0shot_delta_pp\\\": 18.46, \\\"1shot_low_bcs\\\": 0.7538, \\\"1shot_high_bcs\\\": 0.5542, \\\"1shot_delta_pp\\\": 19.96, \\\"5shot_low_bcs\\\": 0.7154, \\\"5shot_high_bcs\\\": 0.4875, \\\"5shot_delta_pp\\\": 22.79, \\\"delta_widening_0to5shot_pp\\\": 4.33, \\\"widening_p_value\\\": 0.014}, \\\"checkpoint_path\\\": \\\"/root/schema-dag-extraction/artifacts/fewshot_bcs_v2/analysis.json\\\", \\\"log_path\\\": \\\"~/runs/schema-dag-extraction/exp_fewshot_bcs_v2.log\\\", \\\"completed_at\\\": \\\"2026-05-17T14:07:52.204Z\\\"}}, \\\"count\\\": 5, \\\"total\\\": 62, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2016}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_unconstrained_decoding_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T09:54:50.724Z\", \"updated_at\": \"2026-05-18T14:22:10.672Z\", \"hypothesis\": \"The BCS-accuracy correlation in RE arises from semantic confusion rather than forced-choice format artifacts. If removing the enum constraint (relaxed decoding) preserves the negative BCS-accuracy correlation direction and significance, confusability is a genuine semantic property; if the correlation disappears, the effect is specific to constrained classification where all errors are channeled into type substitution. Either outcome strengthens the paper: preservation broadens the claim, disappearance validates the error-channeling hypothesis stated in Discussion.\", \"parent\": \"exp_fewrel_formal_80rel\", \"spec\": {\"command\": \"bash -c \\\"cd /root/schema-dag-extraction && source /root/miniconda3/bin/activate base && python src/run_unconstrained_decoding_ablation.py\\\"\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"542072\", \"log_path\": \"~/runs/schema-dag-extraction/exp_unconstrained_decoding_ablation.log\", \"submitted_at\": \"2026-05-18T10:21:03.700Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1903.1, \"gpu_hours\": 0.53}, \"conclusion\": \"success\", \"metrics\": {\"n10\": {\"low_bcs_mean_acc\": 0.8042, \"high_bcs_mean_acc\": 0.725, \"delta_pp\": 7.92, \"spearman_rho\": -0.4303, \"spearman_pval\": 0.214, \"oov_rate\": 0}, \"n25\": {\"low_bcs_mean_acc\": 0.8093, \"high_bcs_mean_acc\": 0.7812, \"delta_pp\": 2.8, \"ci_95_lower_pp\": -4.53, \"ci_95_upper_pp\": 10.56, \"spearman_rho\": -0.1442, \"spearman_pval\": 0.492, \"oov_rate\": 0.0008, \"total_samples\": 2400}}, \"log_path\": \"/root/schema-dag-extraction/results/unconstrained_decoding_ablation/\", \"checkpoint_path\": \"N/A (inference-only ablation)\", \"completed_at\": \"2026-05-18T10:52:46.803Z\"}, \"exp_multiseed_bcs_re\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:44:12.639Z\", \"updated_at\": \"2026-05-18T08:07:35.728Z\", \"hypothesis\": \"The BCS-accuracy correlation observed in FewRel BCS-controlled experiments (R²=0.22-0.53) is robust across random seeds. If seed=123 and seed=456 replicate the negative BCS-accuracy correlation direction and significance observed with seed=42, this confirms the finding is not a single-seed artifact. Rebuttal material for R15-W2 single-seed concern.\", \"parent\": \"exp_fewrel_formal_80rel\", \"server\": \"cqa1-38874\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"cqa1-38874\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-18T07:24:36.762Z\"}, \"spec\": {\"command\": \"bash /root/schema-dag-extraction/scripts/run_multiseed_bcs.sh\", \"server\": \"cqa1-38874\", \"data_path\": \"data/fewrel/fewrel_samples_960.json\", \"data_count\": 14400, \"model_name\": \"Qwen3-32B-FP8\", \"seed\": \"123,456\", \"gpu\": \"cuda:0\", \"pid\": 531145, \"checkpoint_source\": \"Qwen3-32B-FP8 (vLLM inference, no training checkpoint)\", \"eval_data\": \"FewRel 80-rel BCS-controlled batches (25 low-BCS + 25 high-BCS)\", \"note\": \"50 batches x 3 shot conditions x 2 seeds = 300 batches total. Started via nohup (worker bypassed submit_training_job).\"}, \"conclusion\": \"success\", \"log_path\": \"/root/schema-dag-extraction/artifacts/multiseed_bcs_re/run_all.log\", \"checkpoint_path\": \"/root/schema-dag-extraction/artifacts/multiseed_bcs_re/\", \"completed_at\": \"2026-05-18T08:07:29.393Z\", \"metrics\": {\"seed_123\": {\"shot0_delta_pp\": 21.88, \"shot1_delta_pp\": 25.25, \"shot5_delta_pp\": 24.25, \"shot0_ci\": [18.79, 24.83], \"shot1_ci\": [21.08, 29.29], \"shot5_ci\": [19.96, 28.29]}, \"seed_456\": {\"shot0_delta_pp\": 22.38, \"shot1_delta_pp\": 24.38, \"shot5_delta_pp\": 25.08, \"shot0_ci\": [19.58, 24.96], \"shot1_ci\": [20.58, 28.04], \"shot5_ci\": [21.62, 28.58]}, \"finding\": \"Few-shot does NOT mitigate BCS effect; delta increases from ~22pp (0-shot) to ~25pp (5-shot)\"}}, \"exp_gemini_flash_cross_model\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:57:39.493Z\", \"updated_at\": \"2026-05-18T07:36:32.176Z\", \"hypothesis\": \"The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open-weight Qwen/LLaMA + proprietary Gemini).\", \"spec\": {\"command\": \"python3 scripts/run_gemini_flash_fewrel.py --mode all --sleep 0.15\", \"server\": \"local (tmux session: gemini_flash)\", \"data_path\": \"data/fewrel/fewrel_samples_960.json\", \"data_count\": 960, \"model_name\": \"gemini-2.5-flash\", \"seed\": 42}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T02:11:13.608Z\", \"metrics\": {\"count_curve_spearman_rho\": -0.943, \"count_curve_spearman_p\": 0.0048, \"count_1_acc\": 0.8267, \"count_4_acc\": 0.8725, \"count_8_acc\": 0.8204, \"count_16_acc\": 0.7868, \"count_32_acc\": 0.7394, \"count_64_acc\": 0.6343, \"total_drop_count1_to_64_pp\": -19.2, \"complete_count_levels\": \"1,4,8,16,32\", \"partial_count_levels\": \"64 (11/25)\", \"missing\": \"count_80, part2_bcs\", \"note\": \"tmux resumed, still collecting remaining data\"}, \"notes\": \"Gemini 2.5 Flash count curve via local API call. Count 1-32 complete (25 batches each), count 64 partial (11/25). Data at artifacts/exp_gemini_flash/part1/count_curve_analysis.json. Count 80 and part2 BCS not yet collected.\"}, \"exp_schema_intervention\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:57:35.343Z\", \"updated_at\": \"2026-05-17T16:25:52.346Z\", \"hypothesis\": \"If type confusability is a causal driver of extraction errors, then renaming high-BCS type pairs to reduce embedding similarity (while preserving semantic equivalence) should improve accuracy on high-BCS batches. This tests the causal direction: SCS → confusion, not merely correlation. If treatment (renamed) accuracy on previously-high-BCS batches improves significantly over control (original names), confusability is actionable via schema design.\", \"spec\": {\"command\": \"python /root/schema-dag-extraction/scripts/run_schema_intervention.py\", \"server\": \"cqa1-38874\", \"data_path\": \"/root/schema-dag-extraction/data/fewrel/\", \"data_count\": 960, \"model_name\": \"Qwen3-32B-FP8\", \"seed\": 42, \"checkpoint_path\": \"/root/schema-dag-extraction/artifacts/exp_schema_intervention/\", \"log_path\": \"/root/schema-dag-extraction/artifacts/exp_schema_intervention/\"}, \"conclusion\": \"negative\", \"metrics\": {\"high_bcs_control\": 0.693, \"high_bcs_treatment\": 0.605, \"high_bcs_delta\": -0.0883, \"low_bcs_control\": 0.901, \"low_bcs_treatment\": 0.871, \"low_bcs_delta\": -0.0296, \"interaction_delta\": -0.0588, \"interaction_p\": \"<0.001\", \"interaction_t\": -7.23, \"rename_count_correlation_r\": -0.625, \"rename_count_correlation_p\": \"<0.001\", \"cohens_d_high\": -2.92, \"cohens_d_low\": -1.09}, \"completed_at\": \"2026-05-17T16:25:52.346Z\"}, \"exp_fewshot_bcs_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T13:18:15.923Z\", \"updated_at\": \"2026-05-17T14:08:59.677Z\", \"hypothesis\": \"Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples, tested on extreme-BCS batches (low ~0.36, high ~0.80) where 0-shot delta is ~25-31pp. If delta shrinks significantly under few-shot, confusability is addressable via prompting. If delta persists, confusability is a fundamental schema-structural constraint.\", \"parent\": \"exp_fewrel_v2_n25\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate base && cd /root/schema-dag-extraction && python3 src/run_fewshot_bcs_v2.py --stage all --n_shots 0 1 5 --seed 42\\\"\", \"server\": \"cqa1-38874\", \"gpu\": [\"cuda:0\"], \"pid\": \"480497\", \"log_path\": \"~/runs/schema-dag-extraction/exp_fewshot_bcs_v2.log\", \"submitted_at\": \"2026-05-17T13:39:04.351Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/schema-dag-extraction/data/exp_v2_re_n25/batch_groups.json\", \"data_count\": \"50 batches (25 low-BCS ~0.36, 25 high-BCS ~0.80) x 3 shots = 450 tasks\", \"model_name\": \"Qwen3-32B-FP8\", \"seed\": 42, \"checkpoint_source\": \"Qwen3-32B-FP8 (vLLM served, no fine-tuning)\", \"eval_data\": \"FewRel extreme-BCS batches from exp_fewrel_v2_n25/batch_groups.json\", \"wall_clock_seconds\": 1727.9, \"gpu_hours\": 0.48}, \"reproduce\": {\"finished_at\": \"2026-05-17T14:03:41.759Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T14:03:47.723099+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"0shot_low_bcs\": 0.6821, \"0shot_high_bcs\": 0.4975, \"0shot_delta_pp\": 18.46, \"1shot_low_bcs\": 0.7538, \"1shot_high_bcs\": 0.5542, \"1shot_delta_pp\": 19.96, \"5shot_low_bcs\": 0.7154, \"5shot_high_bcs\": 0.4875, \"5shot_delta_pp\": 22.79, \"delta_widening_0to5shot_pp\": 4.33, \"widening_p_value\": 0.014}, \"checkpoint_path\": \"/root/schema-dag-extraction/artifacts/fewshot_bcs_v2/analysis.json\", \"log_path\": \"~/runs/schema-dag-extraction/exp_fewshot_bcs_v2.log\", \"completed_at\": \"2026-05-17T14:07:52.204Z\"}}, \"count\": 5, \"total\": 62, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2016}}"
    }
  },
  "sourceToolAssistantUUID": "1b8042fc-0bfb-42f8-b8e7-06e8ac29e512",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-18T21:37:24.393Z_

```json
{
  "parentUuid": "fd0ced10-615c-40e3-b2a6-1bc9caa485d1",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "22bfdbce-da74-48de-accc-d9482ef53d6f",
  "timestamp": "2026-05-18T21:37:24.393Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "leafUuid": "22bfdbce-da74-48de-accc-d9482ef53d6f",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Update experiment_plan.yaml with registry_id mappings",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---

### Assistant

_source line 37 · 2026-05-18T21:37:28.978Z_

<details><summary>Logged reasoning block</summary>

```text
The registry keys are the experiment IDs themselves (like `exp_unconstrained_decoding_ablation`). The filter `experiment_id` didn't work because it's not a field - the experiment ID is the key in the dictionary. Let me search for the specific experiments by name. Let me try without filters to find them, or search more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22bfdbce-da74-48de-accc-d9482ef53d6f",
  "isSidechain": false,
  "requestId": "req_011CbAkorVNaWiMYmiz32PLG",
  "type": "assistant",
  "uuid": "4a90e81b-fb21-4fc7-bf14-b4f237c44dda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFwkh6VdXG8Moxu88Ay5tC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4139,
      "cache_read_input_tokens": 29270,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 29270,
          "cache_creation_input_tokens": 4139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4139
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-18T21:37:30.445Z_

Registry 用 experiment name 作 key，不是 field 过滤。让我直接搜索需要的实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a90e81b-fb21-4fc7-bf14-b4f237c44dda",
  "isSidechain": false,
  "requestId": "req_011CbAkorVNaWiMYmiz32PLG",
  "type": "assistant",
  "uuid": "a56edba4-344b-42f9-9ee9-5d995cc615f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFwkh6VdXG8Moxu88Ay5tC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4139,
      "cache_read_input_tokens": 29270,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 29270,
          "cache_creation_input_tokens": 4139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4139
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T21:37:31.312Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01LN49e9AHkgkpjDSpoB1znJ`</summary>

```json
{
  "project": "schema-dag-extraction",
  "limit": 0,
  "fields": [
    "status",
    "conclusion"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a56edba4-344b-42f9-9ee9-5d995cc615f2",
  "isSidechain": false,
  "requestId": "req_011CbAkorVNaWiMYmiz32PLG",
  "type": "assistant",
  "uuid": "7406bdf0-bce0-47c6-be9e-fc24cb105c9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFwkh6VdXG8Moxu88Ay5tC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4139,
      "cache_read_input_tokens": 29270,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4139,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 29270,
          "cache_creation_input_tokens": 4139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4139
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T21:37:31.532Z_

<details><summary>↩ Tool result · `toolu_01LN49e9AHkgkpjDSpoB1znJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_unconstrained_decoding_ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_multiseed_bcs_re\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_gemini_flash_cross_model\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_schema_intervention\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_fewshot_bcs_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_llama70b_cross_model\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewshot_bcs_mitigation\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_prompt_sensitivity\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"prompt_sensitivity\": {\"status\": \"PREPARING\"}, \"prompt_sensitivity_dry4\": {\"status\": \"PREPARING\"}, \"prompt_sensitivity_dry3\": {\"status\": \"PREPARING\"}, \"prompt_sensitivity_dry2\": {\"status\": \"PREPARING\"}, \"prompt_sensitivity_dry\": {\"status\": \"PREPARING\"}, \"exp_sdgd_routing_strategies\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_d051_count_curves_25\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_confusability_batch_composition\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_maven_residualized_bcs\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_80pool_16sub_bootstrap\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_40rel_r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_factorial_tost\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_partial_corr_freq\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_formal\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_formal_80rel\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp016_fewrel_error_taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"bootstrap_ci_analysis\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp015_scs_validation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp008_sdgd_v2_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp008_sdgd_zero_fewnerd_r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp007_error_taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp004_maven_bcs\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp003a_prompt_v2_rerun\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp002_confusability_controlled\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"fewrel_pilot\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-004\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp001_count_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_aggregation_monte_carlo\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp_scs_name_def_ablation\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp_fewrel_contamination_check\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp017_gpt4o_mini_fewrel\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"exp_fewrel_16rel_bootstrap\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_cross_embedding_sensitivity\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp_fewrel_v2_n25\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp_docred_confusability\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"bcs_max_to_mean_fix\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp_fewrel_v2_bcs_controlled\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_16rel_100batch\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp012_llama_fewrel_ch2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp012_llama_8b_r2_exp2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp012_llama_8b_r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp006_interaction_2x2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp012_llama_awq\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp012_llama_8b_r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_8b\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_fewrel_40rel_r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_fewrel_40rel_r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_8b_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_fewrel_40rel\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp008_sdgd_zero_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}}, \"count\": 62, \"total\": 62, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2074}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7406bdf0-bce0-47c6-be9e-fc24cb105c9a",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "04b0f6f1-2e12-4f3e-b075-77807978ba52",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_unconstrained_decoding_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_multiseed_bcs_re\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_gemini_flash_cross_model\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_schema_intervention\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp_fewshot_bcs_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp_llama70b_cross_model\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewshot_bcs_mitigation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_prompt_sensitivity\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"prompt_sensitivity\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"prompt_sensitivity_dry4\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"prompt_sensitivity_dry3\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"prompt_sensitivity_dry2\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"prompt_sensitivity_dry\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"exp_sdgd_routing_strategies\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp_d051_count_curves_25\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_confusability_batch_composition\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_maven_residualized_bcs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewrel_80pool_16sub_bootstrap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewrel_40rel_r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewrel_factorial_tost\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewrel_partial_corr_freq\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewrel_formal\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewrel_formal_80rel\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp016_fewrel_error_taxonomy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"bootstrap_ci_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp015_scs_validation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp008_sdgd_v2_fewnerd\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp008_sdgd_zero_fewnerd_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp007_error_taxonomy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp004_maven_bcs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp003a_prompt_v2_rerun\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp002_confusability_controlled\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"fewrel_pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp-004\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp001_count_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_aggregation_monte_carlo\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_scs_name_def_ablation\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewrel_contamination_check\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp017_gpt4o_mini_fewrel\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_fewrel_16rel_bootstrap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_cross_embedding_sensitivity\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewrel_v2_n25\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_docred_confusability\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"bcs_max_to_mean_fix\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewrel_v2_bcs_controlled\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewrel_16rel_100batch\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp012_llama_fewrel_ch2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp012_llama_8b_r2_exp2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp012_llama_8b_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp006_interaction_2x2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp012_llama_awq\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp012_llama_8b_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_8b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_fewrel_40rel_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_fewrel_40rel_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_fewnerd_r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_8b_fewnerd\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_fewrel_40rel\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_fewnerd_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_fewnerd_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_fewnerd\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp008_sdgd_zero_fewnerd\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}}, \\\"count\\\": 62, \\\"total\\\": 62, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.2074}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_unconstrained_decoding_ablation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_multiseed_bcs_re\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_gemini_flash_cross_model\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_schema_intervention\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_fewshot_bcs_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_llama70b_cross_model\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewshot_bcs_mitigation\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_prompt_sensitivity\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"prompt_sensitivity\": {\"status\": \"PREPARING\"}, \"prompt_sensitivity_dry4\": {\"status\": \"PREPARING\"}, \"prompt_sensitivity_dry3\": {\"status\": \"PREPARING\"}, \"prompt_sensitivity_dry2\": {\"status\": \"PREPARING\"}, \"prompt_sensitivity_dry\": {\"status\": \"PREPARING\"}, \"exp_sdgd_routing_strategies\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp_d051_count_curves_25\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_confusability_batch_composition\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_maven_residualized_bcs\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_80pool_16sub_bootstrap\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_40rel_r4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_factorial_tost\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_partial_corr_freq\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_formal\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_formal_80rel\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp016_fewrel_error_taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"bootstrap_ci_analysis\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp015_scs_validation\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp008_sdgd_v2_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp008_sdgd_zero_fewnerd_r2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp007_error_taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp004_maven_bcs\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp003a_prompt_v2_rerun\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp002_confusability_controlled\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"fewrel_pilot\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp-004\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp001_count_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_aggregation_monte_carlo\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp_scs_name_def_ablation\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp_fewrel_contamination_check\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp017_gpt4o_mini_fewrel\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"exp_fewrel_16rel_bootstrap\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_cross_embedding_sensitivity\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp_fewrel_v2_n25\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp_docred_confusability\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"bcs_max_to_mean_fix\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"exp_fewrel_v2_bcs_controlled\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp_fewrel_16rel_100batch\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp012_llama_fewrel_ch2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp012_llama_8b_r2_exp2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp012_llama_8b_r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"exp006_interaction_2x2\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"exp012_llama_awq\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp012_llama_8b_r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_8b\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_fewrel_40rel_r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_fewrel_40rel_r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r4\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_8b_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_fewrel_40rel\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp008_sdgd_zero_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}}, \"count\": 62, \"total\": 62, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2074}}"
    }
  },
  "sourceToolAssistantUUID": "7406bdf0-bce0-47c6-be9e-fc24cb105c9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-18T21:37:34.718Z_

<details><summary>Logged reasoning block</summary>

```text
All 7 registry IDs exist. Let me now compare exp007_error_taxonomy vs exp016_fewrel_error_taxonomy to decide which is more complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04b0f6f1-2e12-4f3e-b075-77807978ba52",
  "isSidechain": false,
  "requestId": "req_011CbAkpNY9GPXGN4qAtYVCq",
  "type": "assistant",
  "uuid": "645ecf5f-6b4e-4d4f-bf39-875a045422da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sDrh1rR2DRVtxLvujty63",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2148,
      "cache_read_input_tokens": 33409,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 33409,
          "cache_creation_input_tokens": 2148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2148
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-18T21:37:36.137Z_

所有 registry ID 都存在。现在比较 exp007 和 exp016 的完整度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "645ecf5f-6b4e-4d4f-bf39-875a045422da",
  "isSidechain": false,
  "requestId": "req_011CbAkpNY9GPXGN4qAtYVCq",
  "type": "assistant",
  "uuid": "c7e3a772-85cd-4032-bfbc-8ff3e1f5dc45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sDrh1rR2DRVtxLvujty63",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2148,
      "cache_read_input_tokens": 33409,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 33409,
          "cache_creation_input_tokens": 2148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2148
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T21:37:37.262Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01631QUQPVYAENx2EXBJYpgj`</summary>

```json
{
  "project": "schema-dag-extraction",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "status",
    "conclusion",
    "metrics",
    "hypothesis"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7e3a772-85cd-4032-bfbc-8ff3e1f5dc45",
  "isSidechain": false,
  "requestId": "req_011CbAkpNY9GPXGN4qAtYVCq",
  "type": "assistant",
  "uuid": "7591f5ce-9028-4760-8445-7aea962eacfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012sDrh1rR2DRVtxLvujty63",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2148,
      "cache_read_input_tokens": 33409,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2148,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 215,
          "cache_read_input_tokens": 33409,
          "cache_creation_input_tokens": 2148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2148
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T21:37:37.466Z_

<details><summary>↩ Tool result · `toolu_01631QUQPVYAENx2EXBJYpgj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_unconstrained_decoding_ablation\": {\"status\": \"DONE\", \"hypothesis\": \"The BCS-accuracy correlation in RE arises from semantic confusion rather than forced-choice format artifacts. If removing the enum constraint (relaxed decoding) preserves the negative BCS-accuracy correlation direction and significance, confusability is a genuine semantic property; if the correlation disappears, the effect is specific to constrained classification where all errors are channeled into type substitution. Either outcome strengthens the paper: preservation broadens the claim, disappearance validates the error-channeling hypothesis stated in Discussion.\", \"conclusion\": \"success\", \"metrics\": {\"n10\": {\"low_bcs_mean_acc\": 0.8042, \"high_bcs_mean_acc\": 0.725, \"delta_pp\": 7.92, \"spearman_rho\": -0.4303, \"spearman_pval\": 0.214, \"oov_rate\": 0}, \"n25\": {\"low_bcs_mean_acc\": 0.8093, \"high_bcs_mean_acc\": 0.7812, \"delta_pp\": 2.8, \"ci_95_lower_pp\": -4.53, \"ci_95_upper_pp\": 10.56, \"spearman_rho\": -0.1442, \"spearman_pval\": 0.492, \"oov_rate\": 0.0008, \"total_samples\": 2400}}}, \"exp_multiseed_bcs_re\": {\"status\": \"DONE\", \"hypothesis\": \"The BCS-accuracy correlation observed in FewRel BCS-controlled experiments (R²=0.22-0.53) is robust across random seeds. If seed=123 and seed=456 replicate the negative BCS-accuracy correlation direction and significance observed with seed=42, this confirms the finding is not a single-seed artifact. Rebuttal material for R15-W2 single-seed concern.\", \"conclusion\": \"success\", \"metrics\": {\"seed_123\": {\"shot0_delta_pp\": 21.88, \"shot1_delta_pp\": 25.25, \"shot5_delta_pp\": 24.25, \"shot0_ci\": [18.79, 24.83], \"shot1_ci\": [21.08, 29.29], \"shot5_ci\": [19.96, 28.29]}, \"seed_456\": {\"shot0_delta_pp\": 22.38, \"shot1_delta_pp\": 24.38, \"shot5_delta_pp\": 25.08, \"shot0_ci\": [19.58, 24.96], \"shot1_ci\": [20.58, 28.04], \"shot5_ci\": [21.62, 28.58]}, \"finding\": \"Few-shot does NOT mitigate BCS effect; delta increases from ~22pp (0-shot) to ~25pp (5-shot)\"}}, \"exp_gemini_flash_cross_model\": {\"status\": \"DONE\", \"hypothesis\": \"The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open-weight Qwen/LLaMA + proprietary Gemini).\", \"conclusion\": \"success\", \"metrics\": {\"count_curve_spearman_rho\": -0.943, \"count_curve_spearman_p\": 0.0048, \"count_1_acc\": 0.8267, \"count_4_acc\": 0.8725, \"count_8_acc\": 0.8204, \"count_16_acc\": 0.7868, \"count_32_acc\": 0.7394, \"count_64_acc\": 0.6343, \"total_drop_count1_to_64_pp\": -19.2, \"complete_count_levels\": \"1,4,8,16,32\", \"partial_count_levels\": \"64 (11/25)\", \"missing\": \"count_80, part2_bcs\", \"note\": \"tmux resumed, still collecting remaining data\"}}, \"exp_schema_intervention\": {\"status\": \"DONE\", \"hypothesis\": \"If type confusability is a causal driver of extraction errors, then renaming high-BCS type pairs to reduce embedding similarity (while preserving semantic equivalence) should improve accuracy on high-BCS batches. This tests the causal direction: SCS → confusion, not merely correlation. If treatment (renamed) accuracy on previously-high-BCS batches improves significantly over control (original names), confusability is actionable via schema design.\", \"conclusion\": \"negative\", \"metrics\": {\"high_bcs_control\": 0.693, \"high_bcs_treatment\": 0.605, \"high_bcs_delta\": -0.0883, \"low_bcs_control\": 0.901, \"low_bcs_treatment\": 0.871, \"low_bcs_delta\": -0.0296, \"interaction_delta\": -0.0588, \"interaction_p\": \"<0.001\", \"interaction_t\": -7.23, \"rename_count_correlation_r\": -0.625, \"rename_count_correlation_p\": \"<0.001\", \"cohens_d_high\": -2.92, \"cohens_d_low\": -1.09}}, \"exp_fewshot_bcs_v2\": {\"status\": \"DONE\", \"hypothesis\": \"Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples, tested on extreme-BCS batches (low ~0.36, high ~0.80) where 0-shot delta is ~25-31pp. If delta shrinks significantly under few-shot, confusability is addressable via prompting. If delta persists, confusability is a fundamental schema-structural constraint.\", \"conclusion\": \"negative\", \"metrics\": {\"0shot_low_bcs\": 0.6821, \"0shot_high_bcs\": 0.4975, \"0shot_delta_pp\": 18.46, \"1shot_low_bcs\": 0.7538, \"1shot_high_bcs\": 0.5542, \"1shot_delta_pp\": 19.96, \"5shot_low_bcs\": 0.7154, \"5shot_high_bcs\": 0.4875, \"5shot_delta_pp\": 22.79, \"delta_widening_0to5shot_pp\": 4.33, \"widening_p_value\": 0.014}}, \"exp_llama70b_cross_model\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA 3.1 70B-Instruct FP8 will replicate the two-dimensional degradation pattern (count-associated recall decline + confusability-associated type confusion) observed on Qwen3-32B, with BCS-accuracy correlation direction preserved despite potential magnitude differences. 70B scale should show stronger Dimension 2 signal than 8B, closing the gap with 32B.\", \"metrics\": {\"exp1_fewrel_count_curve\": {\"count_8_to_80_decline_pp\": -30.7, \"vs_qwen3_decline_pp\": -30.1, \"note\": \"slopes near-identical, 70B absolute ~4pp lower\"}, \"exp2_bcs_controlled\": {\"count_16_low_bcs\": 0.7083, \"count_16_high_bcs\": 0.599, \"delta_pp\": 10.94, \"ci_95\": [3.02, 20.1], \"count_8_delta_pp\": -4.2, \"count_8_note\": \"BCS range too narrow, CI crosses zero\"}, \"exp3_fewnerd_unified_protocol\": {\"metric\": \"text_match recall (unified with Qwen3 protocol: offset correction + hallucination detection + greedy matching + type+text)\", \"count_2\": {\"llama70b\": 0.323, \"qwen3\": 0.515, \"delta_pp\": -19}, \"count_6\": {\"llama70b\": 0.3, \"qwen3\": 0.399, \"delta_pp\": -10}, \"count_12\": {\"llama70b\": 0.278, \"qwen3\": 0.318, \"delta_pp\": -4}, \"count_22\": {\"llama70b\": 0.252, \"qwen3\": 0.279, \"delta_pp\": -3}, \"count_44\": {\"llama70b\": 0.297, \"qwen3\": 0.309, \"delta_pp\": -1}, \"count_66\": {\"llama70b\": 0.273, \"qwen3\": 0.407, \"delta_pp\": -13}, \"precision\": {\"count_2\": {\"llama70b\": 0.446, \"qwen3\": 0.32}, \"count_6\": {\"llama70b\": 0.323, \"qwen3\": 0.248}, \"count_12\": {\"llama70b\": 0.311, \"qwen3\": 0.269}, \"count_22\": {\"llama70b\": 0.376, \"qwen3\": 0.365}, \"count_44\": {\"llama70b\": 0.468, \"qwen3\": 0.504}, \"count_66\": {\"llama70b\": 0.609, \"qwen3\": 0.633}}, \"n_batches\": 25, \"status\": \"complete\", \"result_path\": \"/root/schema-dag-extraction/artifacts/d051_llama-3.1-70b-fp8_fewnerd_n25_s42/summary_unified_protocol.json\", \"key_findings\": [\"Old values invalidated: count_2 0.962→0.323 (-64pp)\", \"70B recall lower than Qwen3 at all counts (1-19pp gap)\", \"70B more conservative: higher precision, lower recall\", \"Middle range count_12-44 close (1-4pp gap)\", \"Both models show count-driven decline pattern\"]}}, \"conclusion\": \"success\"}, \"exp_fewshot_bcs_mitigation\": {\"status\": \"DONE\", \"hypothesis\": \"Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples. If the BCS delta (low-high) shrinks significantly under few-shot, confusability is addressable via better prompting. If delta persists, confusability is a fundamental schema-structural constraint even with demonstrations.\", \"conclusion\": \"killed\"}, \"exp_prompt_sensitivity\": {\"status\": \"DONE\", \"hypothesis\": \"BCS-driven type confusion is a schema-structural property independent of prompt wording: the BCS-accuracy correlation direction and significance persist across diverse prompt variants (V2 baseline, instruction-rewrite, chain-of-thought, minimal), confirming that confusability effects arise from schema composition rather than prompt-specific instruction framing.\", \"metrics\": {\"per_condition\": {\"v2_count8\": {\"mean_acc\": 0.7688, \"bcs_r\": -0.3326, \"bcs_p\": 0.348}, \"v2_count32\": {\"mean_acc\": 0.5643, \"bcs_r\": -0.6477, \"bcs_p\": 0.043, \"significant\": true}, \"instruction_rewrite_count8\": {\"mean_acc\": 0.8469, \"bcs_r\": -0.2228, \"bcs_p\": 0.536}, \"instruction_rewrite_count32\": {\"mean_acc\": 0.6617, \"bcs_r\": -0.4693, \"bcs_p\": 0.171}, \"cot_count8\": {\"mean_acc\": 0.749, \"bcs_r\": 0.2543, \"bcs_p\": 0.478}, \"cot_count32\": {\"mean_acc\": 0.6169, \"bcs_r\": -0.5661, \"bcs_p\": 0.088}, \"minimal_count8\": {\"mean_acc\": 0.8521, \"bcs_r\": -0.1703, \"bcs_p\": 0.638}, \"minimal_count32\": {\"mean_acc\": 0.6146, \"bcs_r\": -0.771, \"bcs_p\": 0.009, \"significant\": true}}, \"summary\": {\"negative_direction\": \"7/8 conditions\", \"significant_at_count32\": \"2/4 (v2 p=0.043, minimal p=0.009), 1 marginal (cot p=0.088)\", \"count_as_moderator\": \"count=32 effects stronger than count=8, consistent with BCS range compression at lower counts\", \"cot_anomaly\": \"only variant with positive r at count_8 (0.25, n.s.)\"}, \"key_finding\": \"BCS-accuracy negative correlation is directionally consistent across 4 prompt variants at count=32 (7/8 conditions negative). Prompt design modulates magnitude but does not eliminate the effect. Supports schema-structural interpretation of confusability.\"}, \"conclusion\": \"success\"}, \"exp_sdgd_routing_strategies\": {\"status\": \"DONE\", \"hypothesis\": \"Max-confidence and none-aware routing strategies can recover a significant fraction of the oracle routing gain (+29.8pp over single-pass) by using LLM generation logprobs to select the most reliable sub-schema prediction, since the correct sub-schema should produce higher-confidence predictions than sub-schemas forced to classify into unrelated types.\", \"conclusion\": \"negative\", \"metrics\": {\"strategies\": {\"single_pass\": {\"accuracy\": 0.504}, \"random_routing\": {\"accuracy\": 0.147}, \"max_conf_all\": {\"accuracy\": 0.277}, \"max_conf_positive\": {\"accuracy\": 0.365}, \"none_aware\": {\"accuracy\": 0.365}, \"margin_positive\": {\"accuracy\": 0.359}, \"oracle\": {\"accuracy\": 0.724}}, \"none_detection\": {\"multi_positive_rate\": 0.734, \"exclusive_positive_rate\": 0.07, \"exclusive_positive_precision\": 0.42, \"none_rate_per_group\": \"20-40%\"}, \"key_finding\": \"All practical routing strategies perform worse than single-pass. Structured decoding forces confident predictions even for wrong sub-schemas, making confidence-based and none-aware routing ineffective. Oracle gain (+22pp) is not recoverable via post-hoc routing.\"}}, \"exp_d051_count_curves_25\": {\"status\": \"DONE\", \"metrics\": {\"seed42_complete\": true, \"fewrel_s42\": {\"counts\": [4, 8, 16, 32, 40, 64, 80], \"accuracy_mean\": [0.87, 0.805, 0.719, 0.652, 0.606, 0.539, 0.504], \"n_batches\": 25, \"status\": \"complete\"}, \"fewnerd_s42\": {\"counts\": [2, 6, 12, 22, 44, 66], \"recall_mean\": [0.527, 0.39, 0.306, 0.268, 0.301, 0.407], \"n_batches\": 25, \"status\": \"complete\"}, \"fewrel_s123\": {\"counts\": [4, 8, 16, 32, 40, 64, 80], \"accuracy_mean\": [0.848, 0.799, 0.745, 0.638, 0.609, 0.536, 0.496], \"n_batches\": 25, \"status\": \"complete\"}, \"fewnerd_s123\": {\"counts\": [2, 6, 12, 22, 44, 66], \"recall_mean\": [0.446, 0.422, 0.357, 0.277, 0.272, 0.407], \"n_batches\": 25, \"status\": \"complete\", \"minimum_count\": 44, \"minimum_recall\": 0.272}, \"fewrel_s456\": {\"counts\": [4, 8, 16, 32, 40, 64, 80], \"accuracy_mean\": [0.851, 0.786, 0.692, 0.655, 0.609, 0.535, 0.487], \"n_batches\": 25, \"status\": \"complete\"}, \"fewnerd_s456\": {\"counts\": [2, 6, 12, 22, 44, 66], \"recall_mean\": [0.553, 0.409, 0.305, 0.258, 0.29, 0.407], \"n_batches\": 25, \"status\": \"complete\", \"minimum_count\": 22, \"minimum_recall\": 0.258}, \"cross_seed_fewrel\": {\"max_delta_pp\": 2.7, \"within_1sd\": true, \"note\": \"All 3 seeds monotonic, max pairwise Δ at any count = 2.7pp\"}, \"cross_seed_fewnerd\": {\"note\": \"seed=42 min at count_22 (0.268), seed=123 min at count_44 (0.272), seed=456 min at count_22 (0.258), all within batch SD (~0.10), confirming plateau\"}, \"all_12_complete\": true, \"figure_1a_generated\": true, \"figure_path\": \"figures/paper/fig_count_curves.pdf\"}, \"hypothesis\": \"Increasing batch count from 5 to 25 per count level reduces sampling variance sufficiently to tighten confidence intervals and confirm the U-shaped NER count response is robust across random seeds (42, 123, 456).\", \"conclusion\": \"success\"}, \"exp_confusability_batch_composition\": {\"status\": \"DONE\", \"hypothesis\": \"Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\", \"conclusion\": \"success\", \"metrics\": {\"confusability_aware\": {\"accuracy\": 0.8021, \"macro_f1\": 0.8021, \"mean_batch_bcs\": 0.5524}, \"random_batch_15seeds\": {\"accuracy_mean\": 0.7877, \"accuracy_std\": 0.0178, \"macro_f1_mean\": 0.7877, \"mean_batch_bcs\": 0.5585, \"ci_95_upper\": 0.7967, \"seeds_above_aware\": 2, \"seeds_above_aware_values\": [0.8125, 0.8146]}, \"single_pass\": {\"accuracy\": 0.5042, \"macro_f1\": 0.5042, \"mean_batch_bcs\": 0.5572}, \"improvement\": {\"confusability_vs_random_pp\": 1.44, \"significant\": false, \"rank_among_random\": \"13/15\", \"p_rank\": 0.19, \"p_z\": 0.22, \"note\": \"Directional only. BCS margin 0.006 too narrow for significance at this partition granularity.\"}, \"per_type\": {\"types_improved\": 51, \"types_degraded\": 28, \"mean_delta_pp\": 1.44}, \"n_conditions\": 17, \"n_samples\": 960}}, \"exp_maven_residualized_bcs\": {\"status\": \"DONE\", \"hypothesis\": \"MAVEN per-type BCS 正相关是 centrality artifact。控制 log_freq/degree_centrality 后 BCS-F1 相关应消失。回答审稿人 Q4。\", \"conclusion\": \"success\", \"metrics\": {\"minilm\": {\"raw_rho\": 0.208, \"raw_p\": 0.011, \"confound\": \"log_freq\", \"bcs_confound_r\": 0.201, \"partial_r\": 0.133, \"partial_p\": 0.107}, \"qwen3\": {\"raw_rho\": 0.184, \"raw_p\": 0.025, \"confound\": \"degree_centrality_0.7\", \"bcs_confound_r\": 0.854, \"partial_r\": 0.063, \"partial_p\": 0.442}, \"joint_control\": {\"qwen3_p\": 0.439, \"minilm_p\": 0.226, \"note\": \"Both n.s. after controlling log_freq + degree jointly\"}, \"key_finding\": \"MAVEN BCS-F1 positive correlation is centrality artifact. MiniLM confound=frequency, Qwen3 confound=degree centrality (r=0.854). After joint control, both correlations vanish. Confirms pairwise SCS remains valid but per-type aggregation fails on homogeneous schemas.\"}}, \"exp_fewrel_80pool_16sub_bootstrap\": {\"status\": \"DONE\", \"hypothesis\": \"从 80-rel pool 随机采样 16 types 构造 8-type batches，100 random batches + BCS quartile bootstrap CI。消除跨 pool 混淆（MW1 审稿人），与 D033 独立 16-rel pool 和 80-rel 做三方比较。\", \"metrics\": {\"n_batches\": 100, \"pool_size\": \"80-rel pool, 16-type subsamples\", \"batch_size\": 8, \"mean_accuracy\": 0.8077, \"mean_bcs\": 0.557, \"bcs_range\": [0.4578, 0.6836], \"quartile_delta\": {\"Q4_minus_Q1_pp\": -3.92, \"ci_95_lower\": -7.79, \"ci_95_upper\": 0.42}, \"pearson_r_bcs_acc\": -0.221, \"pearson_p\": 0.027, \"regression_slope\": {\"slope\": -0.401, \"ci_95_lower\": -0.684, \"ci_95_upper\": -0.062, \"interpretation\": \"per +0.1 BCS → -4.01pp accuracy\"}, \"key_finding\": \"80-pool 16-sub BCS effect directional: Δ(Q4-Q1)=-3.92pp CI crosses zero [-7.79,+0.42], but regression slope=-0.401 CI[-0.684,-0.062] excludes zero. Effect weaker than independent 16-rel pool (Δ=-7.42pp) due to narrower BCS range.\"}, \"conclusion\": \"success\"}, \"exp_fewrel_40rel_r4\": {\"status\": \"DONE\", \"metrics\": {\"exp1_acc_count1\": 0.858, \"exp1_acc_count4\": 0.867, \"exp1_acc_count8\": 0.802, \"exp1_acc_count16\": 0.697, \"exp1_acc_count32\": 0.658, \"exp1_acc_count40\": 0.588, \"exp1_decline_pp\": -27, \"exp2_bcs_delta_count8\": 0.333, \"exp2_bcs_delta_count16\": 0.318, \"exp2_low_bcs_acc_count8\": 0.833, \"exp2_high_bcs_acc_count8\": 0.5, \"exp2_low_bcs_acc_count16\": 0.818, \"exp2_high_bcs_acc_count16\": 0.5}, \"conclusion\": \"success\", \"hypothesis\": \"FewRel count-degradation is monotonic across intermediate scales (40 relations): accuracy declines continuously from count=1 through count=40, with no recovery plateau, confirming the scaling pattern observed at 16 and 80 relations.\"}, \"exp_fewrel_factorial_tost\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"design\": {\"factors\": [\"count (4,8,16,32,40)\", \"BCS (continuous)\"], \"n_batches\": 69, \"dataset\": \"FewRel 40-rel\", \"method\": \"multiple regression (accuracy ~ log2_count + BCS + interaction)\"}, \"analysis_1_factorial\": {\"count_F\": 10.98, \"count_p\": 0.002, \"bcs_F\": 1.24, \"bcs_p\": 0.27, \"interaction_F\": 0.6, \"interaction_p\": 0.44, \"tost\": \"inconclusive\", \"n\": 54}, \"analysis_2_regression\": {\"count_beta\": -0.035, \"count_p\": 0.008, \"bcs_beta\": -0.051, \"bcs_p\": 0.0002, \"interaction_beta\": 0.005, \"interaction_p\": 0.61, \"interaction_effect_pp\": 0.47, \"tost_p\": 0.003, \"tost_conclusion\": \"equivalent\", \"equivalence_margin_pp\": 3, \"R_squared\": 0.52, \"n\": 69}, \"analysis_3_cross_dataset\": {\"count_F\": 21.9, \"count_p\": 0.001, \"bcs_F\": 5.9, \"bcs_p\": 0.016, \"interaction_F\": 2.76, \"interaction_p\": 0.098, \"tost\": \"inconclusive\", \"n\": 200}, \"conclusion\": \"Count and BCS channels are additively separable. TOST confirms equivalence (p=0.003, margin ±3pp) in regression analysis.\"}, \"hypothesis\": \"Count and BCS operate as separable (non-interacting) channels on RE accuracy: the count x BCS interaction term is equivalence-bounded within ±3pp (TOST), supporting a two-channel additive degradation model.\"}, \"exp_fewrel_partial_corr_freq\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pearson_r\": 0.187, \"pearson_p\": 2.56e-26, \"spearman_rho\": 0.227, \"spearman_p\": 3.63e-38, \"n_pairs\": 3160, \"bootstrap_ci_95\": [0.145, 0.231], \"partial_r_eval_freq\": 0.189, \"partial_r_change_pct\": 1.2, \"note\": \"FewRel is perfectly balanced (700 samples/type). Type frequency is zero-variance, cannot confound BCS-confusion relationship. Eval-level frequency partial correlation changes by only 1.2%.\"}, \"hypothesis\": \"The SCS-confusion correlation on FewRel survives partial correlation controlling for type frequency, ruling out the confound that high-SCS pairs are simply rare types with inherently higher error rates.\"}, \"exp_fewrel_formal\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"note\": \"16-rel sanity check only\", \"exp1\": {\"count_1\": {\"mean_acc\": 0.904, \"n_batches\": 16}, \"count_4\": {\"mean_acc\": 0.932, \"n_batches\": 5}, \"count_8\": {\"mean_acc\": 0.867, \"n_batches\": 5}, \"count_16\": {\"mean_acc\": 0.778, \"n_batches\": 5, \"bcs\": 0.9, \"zero_variance\": true}}, \"exp2\": {\"count_8_low_bcs\": {\"acc\": 0.889, \"bcs\": 0.782}, \"count_8_high_bcs\": {\"acc\": 0.798, \"bcs\": 0.892}, \"delta_bcs_effect\": -0.091}, \"trend\": \"count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\"}, \"hypothesis\": \"A 16-relation subset of FewRel exhibits count-driven accuracy degradation consistent with the Few-NERD NER pattern, validating the experimental framework before scaling to the full 80-relation schema.\"}, \"exp_fewrel_formal_80rel\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"exp1_count_curve\": {\"count_1\": {\"acc\": 0.8573, \"n_batches\": 80, \"bcs\": 0}, \"count_4\": {\"acc\": 0.8667, \"n_batches\": 5, \"bcs\": 0.6335}, \"count_8\": {\"acc\": 0.8021, \"n_batches\": 5, \"bcs\": 0.7175}, \"count_16\": {\"acc\": 0.6958, \"n_batches\": 5, \"bcs\": 0.795}, \"count_32\": {\"acc\": 0.6578, \"n_batches\": 5, \"bcs\": 0.8893}, \"count_64\": {\"acc\": 0.5424, \"n_batches\": 5, \"bcs\": 0.9434}, \"count_80\": {\"acc\": 0.5042, \"n_batches\": 5, \"bcs\": 0.9706}}, \"exp2_bcs_controlled\": {\"count_8\": {\"low_bcs_acc\": 0.8229, \"low_bcs\": 0.4715, \"high_bcs_acc\": 0.5104, \"high_bcs\": 0.9706, \"random_acc\": 0.8025, \"delta_pp\": -31.2}, \"count_16\": {\"low_bcs_acc\": 0.8281, \"low_bcs\": 0.5705, \"high_bcs_acc\": 0.5156, \"high_bcs\": 0.9706, \"random_acc\": 0.7169, \"delta_pp\": -31.2}}, \"vs_16rel\": {\"degradation_16rel\": \"-12.6pp (0.904→0.778)\", \"degradation_80rel\": \"-35.3pp (0.857→0.504)\", \"bcs_effect_16rel\": \"-9.1pp\", \"bcs_effect_80rel\": \"-31.2pp\", \"amplification\": \"3.4x\"}, \"key_finding\": \"80-rel count curve 0.857→0.504 (degradation 35.3pp, 远强于 16-rel 12.6pp). BCS effect -31.2pp (3.4x amplification vs 16-rel). 更多 relations → 更大 confusion space → 更强 degradation + BCS effect.\"}, \"hypothesis\": \"Scaling FewRel from 16 to 80 relations amplifies both count-degradation and BCS-accuracy effects due to wider confusability range, producing extreme-batch gaps exceeding 30pp between low-BCS and high-BCS conditions.\"}, \"exp016_fewrel_error_taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"error_distribution\": {\"zero_bcs\": {\"bcs_mean\": 0, \"correct_pct\": 85.73, \"wrong_type_pct\": 0, \"intra_sub_pct\": 0, \"missed_pct\": 14.27}, \"low_bcs\": {\"bcs_mean\": 0.565, \"correct_pct\": 85.42, \"wrong_type_pct\": 4.17, \"intra_sub_pct\": 4.17, \"missed_pct\": 10.42}, \"medium_bcs\": {\"bcs_mean\": 0.729, \"correct_pct\": 75.7, \"wrong_type_pct\": 13, \"intra_sub_pct\": 13, \"missed_pct\": 11.3}, \"high_bcs\": {\"bcs_mean\": 0.86, \"correct_pct\": 66.67, \"wrong_type_pct\": 20.28, \"intra_sub_pct\": 20.28, \"missed_pct\": 13.05}, \"very_high_bcs\": {\"bcs_mean\": 0.971, \"correct_pct\": 52.03, \"wrong_type_pct\": 32.25, \"intra_sub_pct\": 32.25, \"missed_pct\": 15.71}}, \"correlations\": {\"intra_sub_vs_bcs_spearman\": 0.9539, \"intra_sub_vs_bcs_p\": \"<1e-6\", \"accuracy_vs_bcs_spearman\": -0.5821, \"accuracy_vs_bcs_p\": \"<1e-6\"}, \"cross_task\": {\"ner_intra_sub_vs_bcs_rho\": 1, \"re_intra_sub_vs_bcs_rho\": 0.9539}, \"key_finding\": \"100% of type confusion in RE is intra-batch (model only predicts from schema). IntraSub vs BCS ρ=0.954 confirms NER finding. Missed rate flat (10-16%), BCS drives confusion not detection failure.\"}, \"hypothesis\": \"The error taxonomy pattern observed on NER (IntraSub scales with BCS, missed rate driven by count) replicates on FewRel RE under closed-set classification, with IntraSub as the dominant error mode since RE has no span boundary ambiguity.\"}, \"bootstrap_ci_analysis\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"fewnerd_pairwise_r\": {\"point\": 0.112, \"ci_lower\": 0.076, \"ci_upper\": 0.156, \"n\": 1953, \"note\": \"point estimate 0.112 vs old 0.156 — re-run confirmed current value\"}, \"maven_minilm_pairwise_r\": {\"point\": 0.129, \"ci_lower\": 0.104, \"ci_upper\": 0.156, \"n\": 11026}, \"fewrel_count8_delta_pp\": {\"point\": 31.2, \"ci_lower\": 17.7, \"ci_upper\": 42.7, \"n\": \"96+96\"}, \"fewrel_count16_delta_pp\": {\"point\": 31.2, \"ci_lower\": 22.9, \"ci_upper\": 39.6, \"n\": \"192+192\"}, \"fewnerd_pertype_rho\": {\"point\": -0.293, \"ci_lower\": -0.492, \"ci_upper\": -0.054, \"n\": 63}, \"confusion_ratio_count6\": {\"point\": 25.3, \"ci_lower\": 6.1, \"ci_upper\": 60.5}, \"confusion_ratio_count12\": {\"point\": 21.2, \"ci_lower\": 5.3, \"ci_upper\": 52.2}, \"key_finding\": \"All CIs exclude null (0 for correlations, 1 for ratios). All effects are directionally robust at 95% level.\"}, \"hypothesis\": \"Pair-level percentile bootstrap (B=10000) and type-level cluster bootstrap both yield confidence intervals excluding zero for the SCS-confusion correlation, confirming statistical robustness beyond naive standard errors that ignore within-type dependence.\"}, \"exp015_scs_validation\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"all_pairs\": {\"n\": 1953, \"n_nonzero\": 216, \"qwen3_spearman\": 0.1682, \"qwen3_spearman_p\": \"7.3e-14\", \"qwen3_kendall\": 0.1351, \"minilm_spearman\": 0.1439, \"minilm_spearman_p\": \"1.7e-10\", \"minilm_kendall\": 0.1152}, \"nonzero_only\": {\"n\": 216, \"qwen3_spearman\": 0.2722, \"qwen3_spearman_p\": \"5.0e-05\", \"qwen3_kendall\": 0.2001, \"minilm_spearman\": 0.306, \"minilm_spearman_p\": \"4.6e-06\", \"minilm_kendall\": 0.2276}, \"key_finding\": \"Both embeddings significantly predict confusion (all p<1e-5). Qwen3 better overall (rho=0.168), MiniLM better on nonzero pairs (rho=0.306). SCS is a valid but partial proxy — context, frequency, mention ambiguity also matter.\"}, \"hypothesis\": \"Pairwise SCS (embedding cosine similarity between type labels) positively correlates with empirical type confusion rates across all type pairs, validating SCS as a pre-hoc proxy for confusability without requiring extraction outputs.\"}, \"exp008_sdgd_v2_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"single_pass\": {\"f1\": 0.4451, \"precision\": 0.5631, \"recall\": 0.3679, \"batches\": 1, \"time_s\": 79}, \"random_batch\": {\"f1\": 0.3007, \"precision\": 0.3307, \"recall\": 0.2758, \"batches\": 8, \"time_s\": 494}, \"sdgd_zero\": {\"f1\": 0.2407, \"precision\": 0.3244, \"recall\": 0.1913, \"batches\": 4, \"time_s\": 261}, \"per_type\": \"killed before completion (3/4 modes done, Director approved kill)\", \"vs_v1\": \"confidence-gated merge did not improve over union merge. sdgd_zero 0.241 vs v1 0.251, random_batch 0.301 vs v1 0.320\", \"key_finding\": \"SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental rethink.\"}, \"hypothesis\": \"The v2 prompt's reduced over-prediction mitigates merge amplification in multi-pass SDGD decomposition, recovering net F1 above single-pass baseline where v1 failed due to excessive false positives per pass.\"}, \"exp008_sdgd_zero_fewnerd_r2\": {\"status\": \"DONE\", \"metrics\": {\"single_pass\": {\"f1\": 0.4451, \"precision\": 0.5631, \"recall\": 0.3679, \"batches\": 1, \"time_s\": 77.3}, \"sdgd_zero\": {\"f1\": 0.2514, \"precision\": 0.2096, \"recall\": 0.3141, \"batches\": 8, \"time_s\": 408.7}, \"random_batch\": {\"f1\": 0.3197, \"precision\": 0.2491, \"recall\": 0.4462, \"batches\": 8, \"time_s\": 476.1}, \"per_type\": {\"f1\": 0.2915, \"precision\": 0.194, \"recall\": 0.5856, \"batches\": 66, \"time_s\": 2532.2}, \"key_finding\": \"All decomposition modes F1 < single_pass. Decomposition boosts recall but kills precision (merge amplification). sdgd_zero worst F1, even below random_batch.\"}, \"conclusion\": \"negative\", \"hypothesis\": \"Partitioning confusable types into separate batches via graph coloring reduces intra-batch substitution errors sufficiently to offset the precision loss from multi-pass union merge, yielding higher net F1 than single-pass extraction on NER.\"}, \"exp007_error_taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"exp1_random\": {\"bcs_zero\": {\"n_fp\": 6172, \"intra_sub_pct\": 0, \"extra_sub_pct\": 90.3, \"intra_sub_per_100_gold\": 0}, \"bcs_low\": {\"n_fp\": 2231, \"intra_sub_pct\": 1.6, \"extra_sub_pct\": 89.9, \"intra_sub_per_100_gold\": 3.4}, \"bcs_medium\": {\"n_fp\": 3843, \"intra_sub_pct\": 10.6, \"extra_sub_pct\": 78.1, \"intra_sub_per_100_gold\": 6.47}, \"bcs_high\": {\"n_fp\": 6188, \"intra_sub_pct\": 49.4, \"extra_sub_pct\": 30.8, \"intra_sub_per_100_gold\": 12.93}}, \"correlation\": {\"intra_sub_vs_bcs_spearman_rho\": 1, \"intra_sub_vs_bcs_p\": \"<0.001\", \"chi_square\": 6952, \"chi_square_p\": \"~0\"}, \"exp2_controlled\": {\"trend\": \"IntraSub 3.2% -> 7.3% -> 8.6% (rho=1.0, p<0.001)\"}, \"key_finding\": \"BCS>=0.95: 49.4% FP are intra-batch type confusion (13/100 gold). Hallucination+boundary <3%. LLM main error mode is type confusion, not hallucination.\"}, \"hypothesis\": \"Intra-batch type substitution errors scale monotonically with BCS while missed-entity rates are driven primarily by count, establishing mechanistically distinct error channels that decompose total degradation into confusability-driven and capacity-driven components.\"}, \"exp004_maven_bcs\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"exp1_count_curve\": {\"count_1\": {\"n_batches\": 64, \"exact_f1\": 0.009, \"relaxed_f1\": 0.106, \"bcs\": 0}, \"count_6\": {\"n_batches\": 5, \"exact_f1\": 0.003, \"relaxed_f1\": 0.103, \"bcs\": 0.892}, \"count_12\": {\"n_batches\": 5, \"exact_f1\": 0.008, \"relaxed_f1\": 0.146, \"bcs\": 0.921}, \"count_22\": {\"n_batches\": 5, \"exact_f1\": 0.013, \"relaxed_f1\": 0.185, \"bcs\": 0.933}, \"count_44\": {\"n_batches\": 5, \"exact_f1\": 0.018, \"relaxed_f1\": 0.247, \"bcs\": 0.967}, \"count_64\": {\"n_batches\": 5, \"exact_f1\": 0.013, \"relaxed_f1\": 0.245, \"bcs\": 0.973}}, \"exp2_bcs_controlled\": {\"count_6_high_bcs\": {\"exact_f1\": 0.0354, \"relaxed_f1\": 0.211, \"bcs\": 0.9447}, \"count_6_low_bcs\": {\"exact_f1\": 0.0068, \"relaxed_f1\": 0.089, \"bcs\": 0.8709}, \"count_12_high_bcs\": {\"exact_f1\": 0.0151, \"relaxed_f1\": 0.1568, \"bcs\": 0.9447}, \"count_12_low_bcs\": {\"exact_f1\": 0.0068, \"relaxed_f1\": 0.105, \"bcs\": 0.9148}}, \"key_finding\": \"MAVEN batch-level: high_bcs relaxed_F1 2.4x vs low_bcs (count_6). Direction same as Few-NERD batch-level (positive). Pairwise + per-type analysis needed to control frequency confound.\", \"note\": \"exact_F1 very low (0.003-0.035), relaxed_F1 usable (0.089-0.247). Event trigger boundary matching is fuzzy. A re-run (500 samples) is still in progress in artifacts/exp004/.\"}, \"hypothesis\": \"Schema-induced confusability degradation (higher BCS → lower F1) replicates on MAVEN event detection, confirming the channel generalizes beyond NER/RE to event extraction tasks with semantically dense type inventories.\"}, \"exp003a_prompt_v2_rerun\": {\"status\": \"DONE\", \"metrics\": {\"eval_mode\": \"text_match\", \"exp1_text_match\": {\"count_1\": {\"f1\": 0.323, \"precision\": 0.216, \"recall\": 0.641, \"pred_gold_ratio\": 2.97, \"n_batches\": 64}, \"count_2\": {\"f1\": 0.273, \"precision\": 0.18, \"recall\": 0.56, \"pred_gold_ratio\": 3.11, \"n_batches\": 5}, \"count_6\": {\"f1\": 0.306, \"precision\": 0.226, \"recall\": 0.475, \"pred_gold_ratio\": 2.1, \"n_batches\": 5}, \"count_12\": {\"f1\": 0.347, \"precision\": 0.367, \"recall\": 0.329, \"pred_gold_ratio\": 0.9, \"n_batches\": 5}, \"count_22\": {\"f1\": 0.299, \"precision\": 0.339, \"recall\": 0.267, \"pred_gold_ratio\": 0.79, \"n_batches\": 5}, \"count_44\": {\"f1\": 0.445, \"precision\": 0.506, \"recall\": 0.396, \"pred_gold_ratio\": 0.78, \"n_batches\": 5}, \"count_64\": {\"f1\": 0.414, \"precision\": 0.648, \"recall\": 0.304, \"pred_gold_ratio\": 0.47, \"n_batches\": 5}}, \"exp2_text_match\": {\"count_6\": {\"f1\": 0.32, \"precision\": 0.26, \"recall\": 0.416, \"pred_gold_ratio\": 1.6, \"n_batches\": 27}, \"count_12\": {\"f1\": 0.306, \"precision\": 0.291, \"recall\": 0.323, \"pred_gold_ratio\": 1.11, \"n_batches\": 27}}, \"vs_exp001_delta\": {\"count_1\": {\"f1_delta\": \"+0.139 (+76%)\", \"precision_delta\": \"+0.111 (+106%)\", \"recall_delta\": \"-0.079 (-11%)\", \"overpred_fix\": \"6.85→2.97\"}, \"count_6\": {\"f1_delta\": \"+0.151 (+97%)\", \"precision_delta\": \"+0.138 (+157%)\", \"recall_delta\": \"-0.145 (-23%)\"}, \"count_12\": {\"f1_delta\": \"+0.101 (+41%)\", \"precision_delta\": \"+0.207 (+129%)\", \"recall_delta\": \"-0.210 (-39%)\"}, \"count_44\": {\"f1_delta\": \"-0.028 (-6%)\", \"precision_delta\": \"+0.092 (+22%)\", \"recall_delta\": \"-0.155 (-28%)\"}, \"count_64\": {\"f1_delta\": \"-0.049 (-11%)\", \"precision_delta\": \"+0.128 (+25%)\", \"recall_delta\": \"-0.114 (-27%)\"}}, \"key_finding\": \"V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1). But over-corrected at high counts: under-prediction (pred/gold<1) caused recall drops of 27-39%, slightly lowering F1 at count_22-64.\"}, \"conclusion\": \"success\", \"hypothesis\": \"A restructured prompt (v2: definition-enriched, explicit output constraints) modulates the magnitude of count-driven and BCS-driven degradation but does not eliminate either channel, confirming schema configuration as the dominant factor.\"}, \"exp002_confusability_controlled\": {\"status\": \"DONE\", \"metrics\": {\"data_source\": \"exp2_reeval_results.json (text_match, CLEAN)\", \"primary_recall_vs_bcs\": {\"count_6\": {\"r\": 0.2754, \"p\": 0.1644, \"n\": 27, \"verdict\": \"FAIL\"}, \"count_12\": {\"r\": 0.2219, \"p\": 0.266, \"n\": 27, \"verdict\": \"FAIL\"}, \"partial\": {\"r\": 0.2522, \"p\": 0.0658, \"n\": 54, \"verdict\": \"FAIL\"}}, \"secondary_f1_vs_bcs\": {\"count_6\": {\"r\": 0.1754, \"p\": 0.3814, \"n\": 27, \"verdict\": \"FAIL\"}, \"count_12\": {\"r\": 0.5012, \"p\": 0.0077, \"n\": 27, \"verdict\": \"PASS\"}, \"partial\": {\"r\": 0.3025, \"p\": 0.0262, \"n\": 54, \"verdict\": \"PASS\"}}, \"mechanistic_confusion_rate\": {\"random_batches\": {\"count_6_high\": 0.0157, \"count_6_low\": 0.0088, \"ratio_6\": 1.7, \"count_12_high\": 0.0304, \"count_12_low\": 0.0131, \"ratio_12\": 2.4}, \"extreme_batches\": {\"count_6_high\": 0.0728, \"count_6_low\": 0.0014, \"ratio_6\": 27.5, \"count_12_high\": 0.048, \"count_12_low\": 0.0061, \"ratio_12\": 9.9}, \"verdict\": \"PASS\"}, \"pairwise_confusion_analysis\": {\"all\": {\"n_pairs\": 1953, \"pearson_r\": 0.156, \"pearson_p\": 4.6e-12, \"spearman_rho\": 0.16, \"spearman_p\": 1.3e-12}, \"count_6\": {\"n_pairs\": 1770, \"pearson_r\": 0.078, \"pearson_p\": 0.001}, \"count_12\": {\"n_pairs\": 1953, \"pearson_r\": 0.147, \"pearson_p\": 6.7e-11}, \"nonzero_only\": {\"all_spearman_rho\": 0.254, \"all_spearman_p\": 1.1e-06, \"count_12_pearson_r\": 0.212, \"count_12_p\": 0.00034}, \"top_confused_pair\": \"person-other <-> person-politician (BCS=0.934, confusion=156)\"}, \"per_type_analysis\": {\"n_types\": 63, \"filter\": \"freq>=5\", \"micro_f1_vs_bcs\": {\"pearson_r\": -0.1828, \"pearson_p\": 0.1516, \"spearman_rho\": -0.2927, \"spearman_p\": 0.0199, \"partial_r_ctrl_logfreq\": -0.1998, \"partial_p\": 0.1163}, \"mean_f1_vs_bcs\": {\"pearson_r\": -0.1374, \"pearson_p\": 0.283, \"spearman_rho\": -0.2412, \"spearman_p\": 0.0568, \"partial_r_ctrl_logfreq\": -0.1428, \"partial_p\": 0.2641}, \"quartile_comparison\": {\"low_bcs_cutoff\": 0.798, \"high_bcs_cutoff\": 0.827, \"low_bcs_f1\": 0.3098, \"high_bcs_f1\": 0.2275, \"delta_f1\": -0.0823, \"low_bcs_freq\": 2134, \"high_bcs_freq\": 2049}, \"confound_check\": {\"bcs_vs_logfreq_r\": 0.042, \"bcs_vs_logfreq_p\": 0.74, \"logfreq_vs_f1_r\": 0.25, \"logfreq_vs_f1_p\": 0.048}, \"verdict\": \"Direction supports hypothesis. Spearman significant (p=0.02). Frequency confound absent at type level (r=0.04).\"}, \"overall_verdict\": \"PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE STRONG PASS, PER-TYPE DIRECTIONAL PASS\"}, \"conclusion\": \"success\", \"hypothesis\": \"At fixed type count, batches with higher mean pairwise embedding similarity (BCS) produce lower NER recall because semantically confusable types compete for the same entity mentions, increasing substitution errors.\"}, \"fewrel_pilot\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"embedding\": \"all-MiniLM-L6-v2\", \"n_batches\": 15, \"n_predictions\": 374, \"count_4\": {\"low_bcs_acc\": 0.917, \"high_bcs_acc\": 0.708, \"delta_pp\": -20.9, \"low_bcs\": 0.42, \"high_bcs\": 0.97}, \"count_8\": {\"low_bcs_acc\": 1, \"high_bcs_acc\": 0.5, \"delta_pp\": -50, \"low_bcs\": 0.47, \"high_bcs\": 0.97}, \"count_16\": {\"low_bcs_acc\": 0.917, \"high_bcs_acc\": 0.431, \"delta_pp\": -48.6, \"low_bcs\": 0.57, \"high_bcs\": 0.97}, \"key_finding\": \"BCS-accuracy strong negative: high-BCS batches 43-71% vs low-BCS 92-100%. Effect increases with count. Cross-task (NER→RE) replication of confusability hypothesis.\"}, \"hypothesis\": \"Pairwise embedding similarity (SCS) between relation types predicts extraction accuracy degradation: high-BCS batches yield lower accuracy than low-BCS batches at matched count, establishing the confusability channel on RE.\"}, \"exp-004\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_event_types\": 168, \"n_pairs\": 14028, \"scs_mean\": 0.2161, \"scs_std\": 0.103, \"scs_max\": 0.8368, \"scs_median\": 0.2121, \"scs_q90\": 0.3457, \"scs_q95\": 0.3892, \"pairs_above_0.5\": 119, \"pct_above_0.5\": 0.85, \"train_docs\": 2913, \"train_mentions\": 77993, \"valid_docs\": 710, \"valid_mentions\": 18904}, \"hypothesis\": \"MAVEN's 168 FrameNet-derived event types exhibit higher mean SCS than Few-NERD's cross-domain entity types due to same-domain semantic clustering, enabling a cross-task replication test of confusability effects.\"}, \"exp001_count_baseline\": {\"status\": \"DONE\", \"metrics\": {\"diagnosis\": \"char offset 96.5% fabricated by model\", \"text_match_reeval\": {\"count_1\": {\"f1\": 0.184, \"precision\": 0.105, \"recall\": 0.72, \"pred_gold_ratio\": 6.85}, \"count_2\": {\"f1\": 0.123, \"precision\": 0.068, \"recall\": 0.698, \"pred_gold_ratio\": 10.33}, \"count_6\": {\"f1\": 0.155, \"precision\": 0.088, \"recall\": 0.62, \"pred_gold_ratio\": 7.02}, \"count_12\": {\"f1\": 0.246, \"precision\": 0.16, \"recall\": 0.539, \"pred_gold_ratio\": 3.38}, \"count_22\": {\"f1\": 0.322, \"precision\": 0.232, \"recall\": 0.527, \"pred_gold_ratio\": 2.27}, \"count_44\": {\"f1\": 0.473, \"precision\": 0.414, \"recall\": 0.551, \"pred_gold_ratio\": 1.33}, \"count_64\": {\"f1\": 0.463, \"precision\": 0.52, \"recall\": 0.418, \"pred_gold_ratio\": 0.8}}, \"key_finding\": \"recall monotonically decreases (0.72→0.42), precision monotonically increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at count_44\", \"wrong_type_trend\": \"type confusion increases with count: 0→2434, supports confusability hypothesis\", \"spurious_dominant\": \"spurious FPs (text in source but not entity) dominate at low count, not hallucination\", \"conclusion_text_match\": \"F1 curve inversion caused by over-prediction confound, NOT absence of confusability effect. Recall curve + type confusion pattern support hypothesis.\"}, \"conclusion\": \"success\", \"hypothesis\": \"Increasing the number of schema types in a zero-shot LLM extraction prompt degrades per-type recall due to bounded attention capacity and instruction-following limits, producing a monotonic count-performance curve on Few-NERD NER.\"}, \"exp_fewrel_16rel_bootstrap\": {\"status\": \"DONE\", \"hypothesis\": \"FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。\", \"metrics\": {\"n_batches\": 100, \"pool_size\": 16, \"batch_size\": 8, \"bcs_range\": [0.6532, 0.9002], \"quartile_delta\": {\"Q4_minus_Q1_pp\": -5.31, \"ci_95_lower\": -9.45, \"ci_95_upper\": -4.49, \"note\": \"CI values from pre-D038 bootstrap, may need re-verification with MEAN-based BCS\"}, \"pearson_r_bcs_acc\": -0.467, \"regression_slope\": {\"slope\": -0.509, \"ci_95_lower\": -0.556, \"ci_95_upper\": -0.349, \"r_squared\": 0.218, \"p_value\": 1.01e-12, \"interpretation\": \"per +0.1 BCS → -5.09pp accuracy\", \"note\": \"CI from pre-D038 bootstrap\"}, \"amplification_ratio\": {\"quartile_16_vs_80\": 4.2, \"ci_95_lower\": 3.3, \"ci_95_upper\": 6.95}, \"key_finding\": \"16-rel pool BCS effect (MEAN-based, D038): Δ(Q4-Q1)=-5.31pp, r=-0.467. Regression slope=-0.509. Bootstrap 1000 resamples. [D038 MEAN correction applied, old values: r=-0.637/Δ=-7.42pp/slope=-0.449]\"}, \"conclusion\": \"success\"}, \"exp_docred_confusability\": {\"status\": \"DONE\", \"hypothesis\": \"Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2.\", \"conclusion\": \"success\", \"metrics\": {\"n_relation_types\": 96, \"n_eval_samples\": 1240, \"total_inferences\": 13618, \"count_curve\": {\"count_1\": 0.88, \"count_4\": 0.77, \"count_8\": 0.774, \"count_16\": 0.524, \"count_32\": 0.521, \"count_64\": 0.424, \"count_96\": 0.387}, \"bcs_effect_count16\": {\"low_bcs_acc\": 0.679, \"high_bcs_acc\": 0.447, \"gap\": 0.233, \"spearman_r\": -0.661, \"slope\": -0.713, \"slope_95ci\": [-0.909, -0.529]}, \"bcs_effect_count32\": {\"low_bcs_acc\": 0.578, \"high_bcs_acc\": 0.403, \"gap\": 0.176, \"spearman_r\": -0.509, \"slope\": -0.69, \"slope_95ci\": [-0.854, -0.519]}}}, \"exp_fewrel_v2_bcs_controlled\": {\"status\": \"DONE\", \"hypothesis\": \"验证 Channel 2 (BCS→type confusion) 在 v2 prompt 下方向一致。FewRel 80-rel, count=8, low-BCS 5 batches + high-BCS 5 batches, Qwen3-32B-FP8, v2 prompt。D037 Round 2 审稿 C1b。\", \"conclusion\": \"success\", \"metrics\": {\"low_bcs_mean_acc\": 0.8042, \"high_bcs_mean_acc\": 0.725, \"delta_low_minus_high_pp\": 7.92, \"bootstrap_ci_95_lower_pp\": -5.21, \"bootstrap_ci_95_upper_pp\": 21.46, \"n_bootstrap\": 10000, \"n_batches_per_group\": 5, \"samples_per_batch\": 96, \"total_inferences\": 960}}, \"exp_fewrel_16rel_100batch\": {\"status\": \"DONE\", \"hypothesis\": \"D033: 16-rel pool 100 random batches (count_8) + bootstrap CI，填补 tab:bcs_controlled 16-rel 空白，为 3.4× amplification ratio 提供双端 CI 支撑。\", \"conclusion\": \"killed\"}, \"exp012_llama_fewrel_ch2\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct 在 FewRel 80-rel RE 任务上验证 Channel 2 (BCS-controlled confusability effect)。跨模型家族(Qwen→LLaMA) + 跨规模(32B→8B) + 跨任务(NER→RE) 三重泛化验证。exp2 design: count 8/16 × low/high BCS × 27 batches。\", \"conclusion\": \"success\", \"metrics\": {\"exp2_bcs_controlled\": {\"count_8\": {\"low_bcs_acc\": 0.7812, \"high_bcs_acc\": 0.5104, \"delta_pp\": -27.1}, \"count_16\": {\"low_bcs_acc\": 0.7552, \"high_bcs_acc\": 0.5156, \"delta_pp\": -24}}, \"overall_correlation\": {\"n_batches\": 54, \"pearson_r\": -0.39, \"pearson_p\": 0.004, \"spearman_rho\": -0.43, \"spearman_p\": 0.001}, \"cross_model_comparison\": {\"llama_delta_pp\": -27.1, \"qwen3_delta_pp\": -31.2, \"ratio\": 0.87, \"note\": \"LLaMA effect = 87% of Qwen3, direction and magnitude consistent\"}, \"no_floor_effect\": true, \"mean_accuracy\": 0.77, \"accuracy_range\": \"0.41-0.98\", \"key_finding\": \"BCS confusability effect cross-model replicated: LLaMA Δ=-27.1pp (87% of Qwen3 -31.2pp). Pearson r=-0.39 (p=0.004), Spearman ρ=-0.43 (p=0.001). No floor effect.\"}}, \"exp012_llama_8b_r2_exp2\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct exp2 重跑：BCS-controlled factorial (count=6/12, low/high BCS)，验证 confusability effect 跨模型泛化。Parent exp012_llama_8b_r2 的 exp1 count curve 已完成。\", \"conclusion\": \"negative\"}, \"exp012_llama_8b_r2\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct 复现 confusability-driven type confusion（chat template 修复版）。验证 confusability effect 跨模型家族（Qwen→LLaMA）+ 跨规模（32B→8B）泛化。\", \"conclusion\": \"success\", \"metrics\": {\"exp1_llama_recall_count1\": 0.702, \"exp1_llama_recall_count64\": 0.273, \"exp1_recall_decline_pp\": -42.9, \"exp1_per_batch_recall_corr_vs_qwen\": 0.7249, \"exp1_llama_text_match_f1_range\": \"0.06-0.36\", \"exp1_exact_f1\": 0, \"exp1_note\": \"exact/relaxed F1=0 due to missing char offsets, text_match is correct metric\"}}, \"exp006_interaction_2x2\": {\"status\": \"DONE\", \"hypothesis\": \"Count × Confusability 交互效应：{low count, high count} × {low BCS, high BCS} 2×2 设计，测试 count 和 confusability 对 accuracy 的影响是 additive 还是 multiplicative。若 multiplicative，高 count + 高 BCS 组的 degradation 应超过两个主效应之和。\", \"metrics\": {\"cell_means_f1\": {\"low_count_low_bcs\": 0.324, \"low_count_high_bcs\": 0.313, \"high_count_low_bcs\": 0.325, \"high_count_high_bcs\": 0.277}, \"main_effects\": {\"count\": -0.018, \"bcs\": -0.029}, \"interaction\": {\"estimate\": -0.036, \"z\": -0.667, \"p\": 0.505, \"bcs_effect_at_low_count\": -0.011, \"bcs_effect_at_high_count\": -0.048}, \"verdict\": \"交互方向符合 multiplicative 假设但统计不显著 (p=0.505)，未检测到显著交互效应\"}, \"conclusion\": \"negative\"}, \"exp012_llama_awq\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp012_llama_8b_r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_8b\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_fewrel_40rel_r3\": {\"status\": \"DONE\", \"hypothesis\": \"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\", \"conclusion\": \"failed\"}, \"exp_fewrel_40rel_r2\": {\"status\": \"DONE\", \"hypothesis\": \"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r4\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA model replicates confusability-driven type confusion pattern observed with Qwen, validating model-independence of the phenomenon\", \"conclusion\": \"failed\"}, \"exp012_llama_8b_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_fewrel_40rel\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp008_sdgd_zero_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}}, \"count\": 50, \"total\": 50, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1891}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7591f5ce-9028-4760-8445-7aea962eacfd",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "63dd2c1c-07c8-4c64-9e86-e0380da84200",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_unconstrained_decoding_ablation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"The BCS-accuracy correlation in RE arises from semantic confusion rather than forced-choice format artifacts. If removing the enum constraint (relaxed decoding) preserves the negative BCS-accuracy correlation direction and significance, confusability is a genuine semantic property; if the correlation disappears, the effect is specific to constrained classification where all errors are channeled into type substitution. Either outcome strengthens the paper: preservation broadens the claim, disappearance validates the error-channeling hypothesis stated in Discussion.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n10\\\": {\\\"low_bcs_mean_acc\\\": 0.8042, \\\"high_bcs_mean_acc\\\": 0.725, \\\"delta_pp\\\": 7.92, \\\"spearman_rho\\\": -0.4303, \\\"spearman_pval\\\": 0.214, \\\"oov_rate\\\": 0}, \\\"n25\\\": {\\\"low_bcs_mean_acc\\\": 0.8093, \\\"high_bcs_mean_acc\\\": 0.7812, \\\"delta_pp\\\": 2.8, \\\"ci_95_lower_pp\\\": -4.53, \\\"ci_95_upper_pp\\\": 10.56, \\\"spearman_rho\\\": -0.1442, \\\"spearman_pval\\\": 0.492, \\\"oov_rate\\\": 0.0008, \\\"total_samples\\\": 2400}}}, \\\"exp_multiseed_bcs_re\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"The BCS-accuracy correlation observed in FewRel BCS-controlled experiments (R²=0.22-0.53) is robust across random seeds. If seed=123 and seed=456 replicate the negative BCS-accuracy correlation direction and significance observed with seed=42, this confirms the finding is not a single-seed artifact. Rebuttal material for R15-W2 single-seed concern.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"seed_123\\\": {\\\"shot0_delta_pp\\\": 21.88, \\\"shot1_delta_pp\\\": 25.25, \\\"shot5_delta_pp\\\": 24.25, \\\"shot0_ci\\\": [18.79, 24.83], \\\"shot1_ci\\\": [21.08, 29.29], \\\"shot5_ci\\\": [19.96, 28.29]}, \\\"seed_456\\\": {\\\"shot0_delta_pp\\\": 22.38, \\\"shot1_delta_pp\\\": 24.38, \\\"shot5_delta_pp\\\": 25.08, \\\"shot0_ci\\\": [19.58, 24.96], \\\"shot1_ci\\\": [20.58, 28.04], \\\"shot5_ci\\\": [21.62, 28.58]}, \\\"finding\\\": \\\"Few-shot does NOT mitigate BCS effect; delta increases from ~22pp (0-shot) to ~25pp (5-shot)\\\"}}, \\\"exp_gemini_flash_cross_model\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open-weight Qwen/LLaMA + proprietary Gemini).\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"count_curve_spearman_rho\\\": -0.943, \\\"count_curve_spearman_p\\\": 0.0048, \\\"count_1_acc\\\": 0.8267, \\\"count_4_acc\\\": 0.8725, \\\"count_8_acc\\\": 0.8204, \\\"count_16_acc\\\": 0.7868, \\\"count_32_acc\\\": 0.7394, \\\"count_64_acc\\\": 0.6343, \\\"total_drop_count1_to_64_pp\\\": -19.2, \\\"complete_count_levels\\\": \\\"1,4,8,16,32\\\", \\\"partial_count_levels\\\": \\\"64 (11/25)\\\", \\\"missing\\\": \\\"count_80, part2_bcs\\\", \\\"note\\\": \\\"tmux resumed, still collecting remaining data\\\"}}, \\\"exp_schema_intervention\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"If type confusability is a causal driver of extraction errors, then renaming high-BCS type pairs to reduce embedding similarity (while preserving semantic equivalence) should improve accuracy on high-BCS batches. This tests the causal direction: SCS → confusion, not merely correlation. If treatment (renamed) accuracy on previously-high-BCS batches improves significantly over control (original names), confusability is actionable via schema design.\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"high_bcs_control\\\": 0.693, \\\"high_bcs_treatment\\\": 0.605, \\\"high_bcs_delta\\\": -0.0883, \\\"low_bcs_control\\\": 0.901, \\\"low_bcs_treatment\\\": 0.871, \\\"low_bcs_delta\\\": -0.0296, \\\"interaction_delta\\\": -0.0588, \\\"interaction_p\\\": \\\"<0.001\\\", \\\"interaction_t\\\": -7.23, \\\"rename_count_correlation_r\\\": -0.625, \\\"rename_count_correlation_p\\\": \\\"<0.001\\\", \\\"cohens_d_high\\\": -2.92, \\\"cohens_d_low\\\": -1.09}}, \\\"exp_fewshot_bcs_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples, tested on extreme-BCS batches (low ~0.36, high ~0.80) where 0-shot delta is ~25-31pp. If delta shrinks significantly under few-shot, confusability is addressable via prompting. If delta persists, confusability is a fundamental schema-structural constraint.\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"0shot_low_bcs\\\": 0.6821, \\\"0shot_high_bcs\\\": 0.4975, \\\"0shot_delta_pp\\\": 18.46, \\\"1shot_low_bcs\\\": 0.7538, \\\"1shot_high_bcs\\\": 0.5542, \\\"1shot_delta_pp\\\": 19.96, \\\"5shot_low_bcs\\\": 0.7154, \\\"5shot_high_bcs\\\": 0.4875, \\\"5shot_delta_pp\\\": 22.79, \\\"delta_widening_0to5shot_pp\\\": 4.33, \\\"widening_p_value\\\": 0.014}}, \\\"exp_llama70b_cross_model\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"LLaMA 3.1 70B-Instruct FP8 will replicate the two-dimensional degradation pattern (count-associated recall decline + confusability-associated type confusion) observed on Qwen3-32B, with BCS-accuracy correlation direction preserved despite potential magnitude differences. 70B scale should show stronger Dimension 2 signal than 8B, closing the gap with 32B.\\\", \\\"metrics\\\": {\\\"exp1_fewrel_count_curve\\\": {\\\"count_8_to_80_decline_pp\\\": -30.7, \\\"vs_qwen3_decline_pp\\\": -30.1, \\\"note\\\": \\\"slopes near-identical, 70B absolute ~4pp lower\\\"}, \\\"exp2_bcs_controlled\\\": {\\\"count_16_low_bcs\\\": 0.7083, \\\"count_16_high_bcs\\\": 0.599, \\\"delta_pp\\\": 10.94, \\\"ci_95\\\": [3.02, 20.1], \\\"count_8_delta_pp\\\": -4.2, \\\"count_8_note\\\": \\\"BCS range too narrow, CI crosses zero\\\"}, \\\"exp3_fewnerd_unified_protocol\\\": {\\\"metric\\\": \\\"text_match recall (unified with Qwen3 protocol: offset correction + hallucination detection + greedy matching + type+text)\\\", \\\"count_2\\\": {\\\"llama70b\\\": 0.323, \\\"qwen3\\\": 0.515, \\\"delta_pp\\\": -19}, \\\"count_6\\\": {\\\"llama70b\\\": 0.3, \\\"qwen3\\\": 0.399, \\\"delta_pp\\\": -10}, \\\"count_12\\\": {\\\"llama70b\\\": 0.278, \\\"qwen3\\\": 0.318, \\\"delta_pp\\\": -4}, \\\"count_22\\\": {\\\"llama70b\\\": 0.252, \\\"qwen3\\\": 0.279, \\\"delta_pp\\\": -3}, \\\"count_44\\\": {\\\"llama70b\\\": 0.297, \\\"qwen3\\\": 0.309, \\\"delta_pp\\\": -1}, \\\"count_66\\\": {\\\"llama70b\\\": 0.273, \\\"qwen3\\\": 0.407, \\\"delta_pp\\\": -13}, \\\"precision\\\": {\\\"count_2\\\": {\\\"llama70b\\\": 0.446, \\\"qwen3\\\": 0.32}, \\\"count_6\\\": {\\\"llama70b\\\": 0.323, \\\"qwen3\\\": 0.248}, \\\"count_12\\\": {\\\"llama70b\\\": 0.311, \\\"qwen3\\\": 0.269}, \\\"count_22\\\": {\\\"llama70b\\\": 0.376, \\\"qwen3\\\": 0.365}, \\\"count_44\\\": {\\\"llama70b\\\": 0.468, \\\"qwen3\\\": 0.504}, \\\"count_66\\\": {\\\"llama70b\\\": 0.609, \\\"qwen3\\\": 0.633}}, \\\"n_batches\\\": 25, \\\"status\\\": \\\"complete\\\", \\\"result_path\\\": \\\"/root/schema-dag-extraction/artifacts/d051_llama-3.1-70b-fp8_fewnerd_n25_s42/summary_unified_protocol.json\\\", \\\"key_findings\\\": [\\\"Old values invalidated: count_2 0.962→0.323 (-64pp)\\\", \\\"70B recall lower than Qwen3 at all counts (1-19pp gap)\\\", \\\"70B more conservative: higher precision, lower recall\\\", \\\"Middle range count_12-44 close (1-4pp gap)\\\", \\\"Both models show count-driven decline pattern\\\"]}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewshot_bcs_mitigation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples. If the BCS delta (low-high) shrinks significantly under few-shot, confusability is addressable via better prompting. If delta persists, confusability is a fundamental schema-structural constraint even with demonstrations.\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_prompt_sensitivity\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"BCS-driven type confusion is a schema-structural property independent of prompt wording: the BCS-accuracy correlation direction and significance persist across diverse prompt variants (V2 baseline, instruction-rewrite, chain-of-thought, minimal), confirming that confusability effects arise from schema composition rather than prompt-specific instruction framing.\\\", \\\"metrics\\\": {\\\"per_condition\\\": {\\\"v2_count8\\\": {\\\"mean_acc\\\": 0.7688, \\\"bcs_r\\\": -0.3326, \\\"bcs_p\\\": 0.348}, \\\"v2_count32\\\": {\\\"mean_acc\\\": 0.5643, \\\"bcs_r\\\": -0.6477, \\\"bcs_p\\\": 0.043, \\\"significant\\\": true}, \\\"instruction_rewrite_count8\\\": {\\\"mean_acc\\\": 0.8469, \\\"bcs_r\\\": -0.2228, \\\"bcs_p\\\": 0.536}, \\\"instruction_rewrite_count32\\\": {\\\"mean_acc\\\": 0.6617, \\\"bcs_r\\\": -0.4693, \\\"bcs_p\\\": 0.171}, \\\"cot_count8\\\": {\\\"mean_acc\\\": 0.749, \\\"bcs_r\\\": 0.2543, \\\"bcs_p\\\": 0.478}, \\\"cot_count32\\\": {\\\"mean_acc\\\": 0.6169, \\\"bcs_r\\\": -0.5661, \\\"bcs_p\\\": 0.088}, \\\"minimal_count8\\\": {\\\"mean_acc\\\": 0.8521, \\\"bcs_r\\\": -0.1703, \\\"bcs_p\\\": 0.638}, \\\"minimal_count32\\\": {\\\"mean_acc\\\": 0.6146, \\\"bcs_r\\\": -0.771, \\\"bcs_p\\\": 0.009, \\\"significant\\\": true}}, \\\"summary\\\": {\\\"negative_direction\\\": \\\"7/8 conditions\\\", \\\"significant_at_count32\\\": \\\"2/4 (v2 p=0.043, minimal p=0.009), 1 marginal (cot p=0.088)\\\", \\\"count_as_moderator\\\": \\\"count=32 effects stronger than count=8, consistent with BCS range compression at lower counts\\\", \\\"cot_anomaly\\\": \\\"only variant with positive r at count_8 (0.25, n.s.)\\\"}, \\\"key_finding\\\": \\\"BCS-accuracy negative correlation is directionally consistent across 4 prompt variants at count=32 (7/8 conditions negative). Prompt design modulates magnitude but does not eliminate the effect. Supports schema-structural interpretation of confusability.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_sdgd_routing_strategies\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Max-confidence and none-aware routing strategies can recover a significant fraction of the oracle routing gain (+29.8pp over single-pass) by using LLM generation logprobs to select the most reliable sub-schema prediction, since the correct sub-schema should produce higher-confidence predictions than sub-schemas forced to classify into unrelated types.\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"strategies\\\": {\\\"single_pass\\\": {\\\"accuracy\\\": 0.504}, \\\"random_routing\\\": {\\\"accuracy\\\": 0.147}, \\\"max_conf_all\\\": {\\\"accuracy\\\": 0.277}, \\\"max_conf_positive\\\": {\\\"accuracy\\\": 0.365}, \\\"none_aware\\\": {\\\"accuracy\\\": 0.365}, \\\"margin_positive\\\": {\\\"accuracy\\\": 0.359}, \\\"oracle\\\": {\\\"accuracy\\\": 0.724}}, \\\"none_detection\\\": {\\\"multi_positive_rate\\\": 0.734, \\\"exclusive_positive_rate\\\": 0.07, \\\"exclusive_positive_precision\\\": 0.42, \\\"none_rate_per_group\\\": \\\"20-40%\\\"}, \\\"key_finding\\\": \\\"All practical routing strategies perform worse than single-pass. Structured decoding forces confident predictions even for wrong sub-schemas, making confidence-based and none-aware routing ineffective. Oracle gain (+22pp) is not recoverable via post-hoc routing.\\\"}}, \\\"exp_d051_count_curves_25\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"seed42_complete\\\": true, \\\"fewrel_s42\\\": {\\\"counts\\\": [4, 8, 16, 32, 40, 64, 80], \\\"accuracy_mean\\\": [0.87, 0.805, 0.719, 0.652, 0.606, 0.539, 0.504], \\\"n_batches\\\": 25, \\\"status\\\": \\\"complete\\\"}, \\\"fewnerd_s42\\\": {\\\"counts\\\": [2, 6, 12, 22, 44, 66], \\\"recall_mean\\\": [0.527, 0.39, 0.306, 0.268, 0.301, 0.407], \\\"n_batches\\\": 25, \\\"status\\\": \\\"complete\\\"}, \\\"fewrel_s123\\\": {\\\"counts\\\": [4, 8, 16, 32, 40, 64, 80], \\\"accuracy_mean\\\": [0.848, 0.799, 0.745, 0.638, 0.609, 0.536, 0.496], \\\"n_batches\\\": 25, \\\"status\\\": \\\"complete\\\"}, \\\"fewnerd_s123\\\": {\\\"counts\\\": [2, 6, 12, 22, 44, 66], \\\"recall_mean\\\": [0.446, 0.422, 0.357, 0.277, 0.272, 0.407], \\\"n_batches\\\": 25, \\\"status\\\": \\\"complete\\\", \\\"minimum_count\\\": 44, \\\"minimum_recall\\\": 0.272}, \\\"fewrel_s456\\\": {\\\"counts\\\": [4, 8, 16, 32, 40, 64, 80], \\\"accuracy_mean\\\": [0.851, 0.786, 0.692, 0.655, 0.609, 0.535, 0.487], \\\"n_batches\\\": 25, \\\"status\\\": \\\"complete\\\"}, \\\"fewnerd_s456\\\": {\\\"counts\\\": [2, 6, 12, 22, 44, 66], \\\"recall_mean\\\": [0.553, 0.409, 0.305, 0.258, 0.29, 0.407], \\\"n_batches\\\": 25, \\\"status\\\": \\\"complete\\\", \\\"minimum_count\\\": 22, \\\"minimum_recall\\\": 0.258}, \\\"cross_seed_fewrel\\\": {\\\"max_delta_pp\\\": 2.7, \\\"within_1sd\\\": true, \\\"note\\\": \\\"All 3 seeds monotonic, max pairwise Δ at any count = 2.7pp\\\"}, \\\"cross_seed_fewnerd\\\": {\\\"note\\\": \\\"seed=42 min at count_22 (0.268), seed=123 min at count_44 (0.272), seed=456 min at count_22 (0.258), all within batch SD (~0.10), confirming plateau\\\"}, \\\"all_12_complete\\\": true, \\\"figure_1a_generated\\\": true, \\\"figure_path\\\": \\\"figures/paper/fig_count_curves.pdf\\\"}, \\\"hypothesis\\\": \\\"Increasing batch count from 5 to 25 per count level reduces sampling variance sufficiently to tighten confidence intervals and confirm the U-shaped NER count response is robust across random seeds (42, 123, 456).\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_confusability_batch_composition\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"confusability_aware\\\": {\\\"accuracy\\\": 0.8021, \\\"macro_f1\\\": 0.8021, \\\"mean_batch_bcs\\\": 0.5524}, \\\"random_batch_15seeds\\\": {\\\"accuracy_mean\\\": 0.7877, \\\"accuracy_std\\\": 0.0178, \\\"macro_f1_mean\\\": 0.7877, \\\"mean_batch_bcs\\\": 0.5585, \\\"ci_95_upper\\\": 0.7967, \\\"seeds_above_aware\\\": 2, \\\"seeds_above_aware_values\\\": [0.8125, 0.8146]}, \\\"single_pass\\\": {\\\"accuracy\\\": 0.5042, \\\"macro_f1\\\": 0.5042, \\\"mean_batch_bcs\\\": 0.5572}, \\\"improvement\\\": {\\\"confusability_vs_random_pp\\\": 1.44, \\\"significant\\\": false, \\\"rank_among_random\\\": \\\"13/15\\\", \\\"p_rank\\\": 0.19, \\\"p_z\\\": 0.22, \\\"note\\\": \\\"Directional only. BCS margin 0.006 too narrow for significance at this partition granularity.\\\"}, \\\"per_type\\\": {\\\"types_improved\\\": 51, \\\"types_degraded\\\": 28, \\\"mean_delta_pp\\\": 1.44}, \\\"n_conditions\\\": 17, \\\"n_samples\\\": 960}}, \\\"exp_maven_residualized_bcs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"MAVEN per-type BCS 正相关是 centrality artifact。控制 log_freq/degree_centrality 后 BCS-F1 相关应消失。回答审稿人 Q4。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"minilm\\\": {\\\"raw_rho\\\": 0.208, \\\"raw_p\\\": 0.011, \\\"confound\\\": \\\"log_freq\\\", \\\"bcs_confound_r\\\": 0.201, \\\"partial_r\\\": 0.133, \\\"partial_p\\\": 0.107}, \\\"qwen3\\\": {\\\"raw_rho\\\": 0.184, \\\"raw_p\\\": 0.025, \\\"confound\\\": \\\"degree_centrality_0.7\\\", \\\"bcs_confound_r\\\": 0.854, \\\"partial_r\\\": 0.063, \\\"partial_p\\\": 0.442}, \\\"joint_control\\\": {\\\"qwen3_p\\\": 0.439, \\\"minilm_p\\\": 0.226, \\\"note\\\": \\\"Both n.s. after controlling log_freq + degree jointly\\\"}, \\\"key_finding\\\": \\\"MAVEN BCS-F1 positive correlation is centrality artifact. MiniLM confound=frequency, Qwen3 confound=degree centrality (r=0.854). After joint control, both correlations vanish. Confirms pairwise SCS remains valid but per-type aggregation fails on homogeneous schemas.\\\"}}, \\\"exp_fewrel_80pool_16sub_bootstrap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"从 80-rel pool 随机采样 16 types 构造 8-type batches，100 random batches + BCS quartile bootstrap CI。消除跨 pool 混淆（MW1 审稿人），与 D033 独立 16-rel pool 和 80-rel 做三方比较。\\\", \\\"metrics\\\": {\\\"n_batches\\\": 100, \\\"pool_size\\\": \\\"80-rel pool, 16-type subsamples\\\", \\\"batch_size\\\": 8, \\\"mean_accuracy\\\": 0.8077, \\\"mean_bcs\\\": 0.557, \\\"bcs_range\\\": [0.4578, 0.6836], \\\"quartile_delta\\\": {\\\"Q4_minus_Q1_pp\\\": -3.92, \\\"ci_95_lower\\\": -7.79, \\\"ci_95_upper\\\": 0.42}, \\\"pearson_r_bcs_acc\\\": -0.221, \\\"pearson_p\\\": 0.027, \\\"regression_slope\\\": {\\\"slope\\\": -0.401, \\\"ci_95_lower\\\": -0.684, \\\"ci_95_upper\\\": -0.062, \\\"interpretation\\\": \\\"per +0.1 BCS → -4.01pp accuracy\\\"}, \\\"key_finding\\\": \\\"80-pool 16-sub BCS effect directional: Δ(Q4-Q1)=-3.92pp CI crosses zero [-7.79,+0.42], but regression slope=-0.401 CI[-0.684,-0.062] excludes zero. Effect weaker than independent 16-rel pool (Δ=-7.42pp) due to narrower BCS range.\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_fewrel_40rel_r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"exp1_acc_count1\\\": 0.858, \\\"exp1_acc_count4\\\": 0.867, \\\"exp1_acc_count8\\\": 0.802, \\\"exp1_acc_count16\\\": 0.697, \\\"exp1_acc_count32\\\": 0.658, \\\"exp1_acc_count40\\\": 0.588, \\\"exp1_decline_pp\\\": -27, \\\"exp2_bcs_delta_count8\\\": 0.333, \\\"exp2_bcs_delta_count16\\\": 0.318, \\\"exp2_low_bcs_acc_count8\\\": 0.833, \\\"exp2_high_bcs_acc_count8\\\": 0.5, \\\"exp2_low_bcs_acc_count16\\\": 0.818, \\\"exp2_high_bcs_acc_count16\\\": 0.5}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"FewRel count-degradation is monotonic across intermediate scales (40 relations): accuracy declines continuously from count=1 through count=40, with no recovery plateau, confirming the scaling pattern observed at 16 and 80 relations.\\\"}, \\\"exp_fewrel_factorial_tost\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"design\\\": {\\\"factors\\\": [\\\"count (4,8,16,32,40)\\\", \\\"BCS (continuous)\\\"], \\\"n_batches\\\": 69, \\\"dataset\\\": \\\"FewRel 40-rel\\\", \\\"method\\\": \\\"multiple regression (accuracy ~ log2_count + BCS + interaction)\\\"}, \\\"analysis_1_factorial\\\": {\\\"count_F\\\": 10.98, \\\"count_p\\\": 0.002, \\\"bcs_F\\\": 1.24, \\\"bcs_p\\\": 0.27, \\\"interaction_F\\\": 0.6, \\\"interaction_p\\\": 0.44, \\\"tost\\\": \\\"inconclusive\\\", \\\"n\\\": 54}, \\\"analysis_2_regression\\\": {\\\"count_beta\\\": -0.035, \\\"count_p\\\": 0.008, \\\"bcs_beta\\\": -0.051, \\\"bcs_p\\\": 0.0002, \\\"interaction_beta\\\": 0.005, \\\"interaction_p\\\": 0.61, \\\"interaction_effect_pp\\\": 0.47, \\\"tost_p\\\": 0.003, \\\"tost_conclusion\\\": \\\"equivalent\\\", \\\"equivalence_margin_pp\\\": 3, \\\"R_squared\\\": 0.52, \\\"n\\\": 69}, \\\"analysis_3_cross_dataset\\\": {\\\"count_F\\\": 21.9, \\\"count_p\\\": 0.001, \\\"bcs_F\\\": 5.9, \\\"bcs_p\\\": 0.016, \\\"interaction_F\\\": 2.76, \\\"interaction_p\\\": 0.098, \\\"tost\\\": \\\"inconclusive\\\", \\\"n\\\": 200}, \\\"conclusion\\\": \\\"Count and BCS channels are additively separable. TOST confirms equivalence (p=0.003, margin ±3pp) in regression analysis.\\\"}, \\\"hypothesis\\\": \\\"Count and BCS operate as separable (non-interacting) channels on RE accuracy: the count x BCS interaction term is equivalence-bounded within ±3pp (TOST), supporting a two-channel additive degradation model.\\\"}, \\\"exp_fewrel_partial_corr_freq\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"pearson_r\\\": 0.187, \\\"pearson_p\\\": 2.56e-26, \\\"spearman_rho\\\": 0.227, \\\"spearman_p\\\": 3.63e-38, \\\"n_pairs\\\": 3160, \\\"bootstrap_ci_95\\\": [0.145, 0.231], \\\"partial_r_eval_freq\\\": 0.189, \\\"partial_r_change_pct\\\": 1.2, \\\"note\\\": \\\"FewRel is perfectly balanced (700 samples/type). Type frequency is zero-variance, cannot confound BCS-confusion relationship. Eval-level frequency partial correlation changes by only 1.2%.\\\"}, \\\"hypothesis\\\": \\\"The SCS-confusion correlation on FewRel survives partial correlation controlling for type frequency, ruling out the confound that high-SCS pairs are simply rare types with inherently higher error rates.\\\"}, \\\"exp_fewrel_formal\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"note\\\": \\\"16-rel sanity check only\\\", \\\"exp1\\\": {\\\"count_1\\\": {\\\"mean_acc\\\": 0.904, \\\"n_batches\\\": 16}, \\\"count_4\\\": {\\\"mean_acc\\\": 0.932, \\\"n_batches\\\": 5}, \\\"count_8\\\": {\\\"mean_acc\\\": 0.867, \\\"n_batches\\\": 5}, \\\"count_16\\\": {\\\"mean_acc\\\": 0.778, \\\"n_batches\\\": 5, \\\"bcs\\\": 0.9, \\\"zero_variance\\\": true}}, \\\"exp2\\\": {\\\"count_8_low_bcs\\\": {\\\"acc\\\": 0.889, \\\"bcs\\\": 0.782}, \\\"count_8_high_bcs\\\": {\\\"acc\\\": 0.798, \\\"bcs\\\": 0.892}, \\\"delta_bcs_effect\\\": -0.091}, \\\"trend\\\": \\\"count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\\\"}, \\\"hypothesis\\\": \\\"A 16-relation subset of FewRel exhibits count-driven accuracy degradation consistent with the Few-NERD NER pattern, validating the experimental framework before scaling to the full 80-relation schema.\\\"}, \\\"exp_fewrel_formal_80rel\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"exp1_count_curve\\\": {\\\"count_1\\\": {\\\"acc\\\": 0.8573, \\\"n_batches\\\": 80, \\\"bcs\\\": 0}, \\\"count_4\\\": {\\\"acc\\\": 0.8667, \\\"n_batches\\\": 5, \\\"bcs\\\": 0.6335}, \\\"count_8\\\": {\\\"acc\\\": 0.8021, \\\"n_batches\\\": 5, \\\"bcs\\\": 0.7175}, \\\"count_16\\\": {\\\"acc\\\": 0.6958, \\\"n_batches\\\": 5, \\\"bcs\\\": 0.795}, \\\"count_32\\\": {\\\"acc\\\": 0.6578, \\\"n_batches\\\": 5, \\\"bcs\\\": 0.8893}, \\\"count_64\\\": {\\\"acc\\\": 0.5424, \\\"n_batches\\\": 5, \\\"bcs\\\": 0.9434}, \\\"count_80\\\": {\\\"acc\\\": 0.5042, \\\"n_batches\\\": 5, \\\"bcs\\\": 0.9706}}, \\\"exp2_bcs_controlled\\\": {\\\"count_8\\\": {\\\"low_bcs_acc\\\": 0.8229, \\\"low_bcs\\\": 0.4715, \\\"high_bcs_acc\\\": 0.5104, \\\"high_bcs\\\": 0.9706, \\\"random_acc\\\": 0.8025, \\\"delta_pp\\\": -31.2}, \\\"count_16\\\": {\\\"low_bcs_acc\\\": 0.8281, \\\"low_bcs\\\": 0.5705, \\\"high_bcs_acc\\\": 0.5156, \\\"high_bcs\\\": 0.9706, \\\"random_acc\\\": 0.7169, \\\"delta_pp\\\": -31.2}}, \\\"vs_16rel\\\": {\\\"degradation_16rel\\\": \\\"-12.6pp (0.904→0.778)\\\", \\\"degradation_80rel\\\": \\\"-35.3pp (0.857→0.504)\\\", \\\"bcs_effect_16rel\\\": \\\"-9.1pp\\\", \\\"bcs_effect_80rel\\\": \\\"-31.2pp\\\", \\\"amplification\\\": \\\"3.4x\\\"}, \\\"key_finding\\\": \\\"80-rel count curve 0.857→0.504 (degradation 35.3pp, 远强于 16-rel 12.6pp). BCS effect -31.2pp (3.4x amplification vs 16-rel). 更多 relations → 更大 confusion space → 更强 degradation + BCS effect.\\\"}, \\\"hypothesis\\\": \\\"Scaling FewRel from 16 to 80 relations amplifies both count-degradation and BCS-accuracy effects due to wider confusability range, producing extreme-batch gaps exceeding 30pp between low-BCS and high-BCS conditions.\\\"}, \\\"exp016_fewrel_error_taxonomy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"error_distribution\\\": {\\\"zero_bcs\\\": {\\\"bcs_mean\\\": 0, \\\"correct_pct\\\": 85.73, \\\"wrong_type_pct\\\": 0, \\\"intra_sub_pct\\\": 0, \\\"missed_pct\\\": 14.27}, \\\"low_bcs\\\": {\\\"bcs_mean\\\": 0.565, \\\"correct_pct\\\": 85.42, \\\"wrong_type_pct\\\": 4.17, \\\"intra_sub_pct\\\": 4.17, \\\"missed_pct\\\": 10.42}, \\\"medium_bcs\\\": {\\\"bcs_mean\\\": 0.729, \\\"correct_pct\\\": 75.7, \\\"wrong_type_pct\\\": 13, \\\"intra_sub_pct\\\": 13, \\\"missed_pct\\\": 11.3}, \\\"high_bcs\\\": {\\\"bcs_mean\\\": 0.86, \\\"correct_pct\\\": 66.67, \\\"wrong_type_pct\\\": 20.28, \\\"intra_sub_pct\\\": 20.28, \\\"missed_pct\\\": 13.05}, \\\"very_high_bcs\\\": {\\\"bcs_mean\\\": 0.971, \\\"correct_pct\\\": 52.03, \\\"wrong_type_pct\\\": 32.25, \\\"intra_sub_pct\\\": 32.25, \\\"missed_pct\\\": 15.71}}, \\\"correlations\\\": {\\\"intra_sub_vs_bcs_spearman\\\": 0.9539, \\\"intra_sub_vs_bcs_p\\\": \\\"<1e-6\\\", \\\"accuracy_vs_bcs_spearman\\\": -0.5821, \\\"accuracy_vs_bcs_p\\\": \\\"<1e-6\\\"}, \\\"cross_task\\\": {\\\"ner_intra_sub_vs_bcs_rho\\\": 1, \\\"re_intra_sub_vs_bcs_rho\\\": 0.9539}, \\\"key_finding\\\": \\\"100% of type confusion in RE is intra-batch (model only predicts from schema). IntraSub vs BCS ρ=0.954 confirms NER finding. Missed rate flat (10-16%), BCS drives confusion not detection failure.\\\"}, \\\"hypothesis\\\": \\\"The error taxonomy pattern observed on NER (IntraSub scales with BCS, missed rate driven by count) replicates on FewRel RE under closed-set classification, with IntraSub as the dominant error mode since RE has no span boundary ambiguity.\\\"}, \\\"bootstrap_ci_analysis\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"fewnerd_pairwise_r\\\": {\\\"point\\\": 0.112, \\\"ci_lower\\\": 0.076, \\\"ci_upper\\\": 0.156, \\\"n\\\": 1953, \\\"note\\\": \\\"point estimate 0.112 vs old 0.156 — re-run confirmed current value\\\"}, \\\"maven_minilm_pairwise_r\\\": {\\\"point\\\": 0.129, \\\"ci_lower\\\": 0.104, \\\"ci_upper\\\": 0.156, \\\"n\\\": 11026}, \\\"fewrel_count8_delta_pp\\\": {\\\"point\\\": 31.2, \\\"ci_lower\\\": 17.7, \\\"ci_upper\\\": 42.7, \\\"n\\\": \\\"96+96\\\"}, \\\"fewrel_count16_delta_pp\\\": {\\\"point\\\": 31.2, \\\"ci_lower\\\": 22.9, \\\"ci_upper\\\": 39.6, \\\"n\\\": \\\"192+192\\\"}, \\\"fewnerd_pertype_rho\\\": {\\\"point\\\": -0.293, \\\"ci_lower\\\": -0.492, \\\"ci_upper\\\": -0.054, \\\"n\\\": 63}, \\\"confusion_ratio_count6\\\": {\\\"point\\\": 25.3, \\\"ci_lower\\\": 6.1, \\\"ci_upper\\\": 60.5}, \\\"confusion_ratio_count12\\\": {\\\"point\\\": 21.2, \\\"ci_lower\\\": 5.3, \\\"ci_upper\\\": 52.2}, \\\"key_finding\\\": \\\"All CIs exclude null (0 for correlations, 1 for ratios). All effects are directionally robust at 95% level.\\\"}, \\\"hypothesis\\\": \\\"Pair-level percentile bootstrap (B=10000) and type-level cluster bootstrap both yield confidence intervals excluding zero for the SCS-confusion correlation, confirming statistical robustness beyond naive standard errors that ignore within-type dependence.\\\"}, \\\"exp015_scs_validation\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"all_pairs\\\": {\\\"n\\\": 1953, \\\"n_nonzero\\\": 216, \\\"qwen3_spearman\\\": 0.1682, \\\"qwen3_spearman_p\\\": \\\"7.3e-14\\\", \\\"qwen3_kendall\\\": 0.1351, \\\"minilm_spearman\\\": 0.1439, \\\"minilm_spearman_p\\\": \\\"1.7e-10\\\", \\\"minilm_kendall\\\": 0.1152}, \\\"nonzero_only\\\": {\\\"n\\\": 216, \\\"qwen3_spearman\\\": 0.2722, \\\"qwen3_spearman_p\\\": \\\"5.0e-05\\\", \\\"qwen3_kendall\\\": 0.2001, \\\"minilm_spearman\\\": 0.306, \\\"minilm_spearman_p\\\": \\\"4.6e-06\\\", \\\"minilm_kendall\\\": 0.2276}, \\\"key_finding\\\": \\\"Both embeddings significantly predict confusion (all p<1e-5). Qwen3 better overall (rho=0.168), MiniLM better on nonzero pairs (rho=0.306). SCS is a valid but partial proxy — context, frequency, mention ambiguity also matter.\\\"}, \\\"hypothesis\\\": \\\"Pairwise SCS (embedding cosine similarity between type labels) positively correlates with empirical type confusion rates across all type pairs, validating SCS as a pre-hoc proxy for confusability without requiring extraction outputs.\\\"}, \\\"exp008_sdgd_v2_fewnerd\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"single_pass\\\": {\\\"f1\\\": 0.4451, \\\"precision\\\": 0.5631, \\\"recall\\\": 0.3679, \\\"batches\\\": 1, \\\"time_s\\\": 79}, \\\"random_batch\\\": {\\\"f1\\\": 0.3007, \\\"precision\\\": 0.3307, \\\"recall\\\": 0.2758, \\\"batches\\\": 8, \\\"time_s\\\": 494}, \\\"sdgd_zero\\\": {\\\"f1\\\": 0.2407, \\\"precision\\\": 0.3244, \\\"recall\\\": 0.1913, \\\"batches\\\": 4, \\\"time_s\\\": 261}, \\\"per_type\\\": \\\"killed before completion (3/4 modes done, Director approved kill)\\\", \\\"vs_v1\\\": \\\"confidence-gated merge did not improve over union merge. sdgd_zero 0.241 vs v1 0.251, random_batch 0.301 vs v1 0.320\\\", \\\"key_finding\\\": \\\"SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental rethink.\\\"}, \\\"hypothesis\\\": \\\"The v2 prompt's reduced over-prediction mitigates merge amplification in multi-pass SDGD decomposition, recovering net F1 above single-pass baseline where v1 failed due to excessive false positives per pass.\\\"}, \\\"exp008_sdgd_zero_fewnerd_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"single_pass\\\": {\\\"f1\\\": 0.4451, \\\"precision\\\": 0.5631, \\\"recall\\\": 0.3679, \\\"batches\\\": 1, \\\"time_s\\\": 77.3}, \\\"sdgd_zero\\\": {\\\"f1\\\": 0.2514, \\\"precision\\\": 0.2096, \\\"recall\\\": 0.3141, \\\"batches\\\": 8, \\\"time_s\\\": 408.7}, \\\"random_batch\\\": {\\\"f1\\\": 0.3197, \\\"precision\\\": 0.2491, \\\"recall\\\": 0.4462, \\\"batches\\\": 8, \\\"time_s\\\": 476.1}, \\\"per_type\\\": {\\\"f1\\\": 0.2915, \\\"precision\\\": 0.194, \\\"recall\\\": 0.5856, \\\"batches\\\": 66, \\\"time_s\\\": 2532.2}, \\\"key_finding\\\": \\\"All decomposition modes F1 < single_pass. Decomposition boosts recall but kills precision (merge amplification). sdgd_zero worst F1, even below random_batch.\\\"}, \\\"conclusion\\\": \\\"negative\\\", \\\"hypothesis\\\": \\\"Partitioning confusable types into separate batches via graph coloring reduces intra-batch substitution errors sufficiently to offset the precision loss from multi-pass union merge, yielding higher net F1 than single-pass extraction on NER.\\\"}, \\\"exp007_error_taxonomy\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"exp1_random\\\": {\\\"bcs_zero\\\": {\\\"n_fp\\\": 6172, \\\"intra_sub_pct\\\": 0, \\\"extra_sub_pct\\\": 90.3, \\\"intra_sub_per_100_gold\\\": 0}, \\\"bcs_low\\\": {\\\"n_fp\\\": 2231, \\\"intra_sub_pct\\\": 1.6, \\\"extra_sub_pct\\\": 89.9, \\\"intra_sub_per_100_gold\\\": 3.4}, \\\"bcs_medium\\\": {\\\"n_fp\\\": 3843, \\\"intra_sub_pct\\\": 10.6, \\\"extra_sub_pct\\\": 78.1, \\\"intra_sub_per_100_gold\\\": 6.47}, \\\"bcs_high\\\": {\\\"n_fp\\\": 6188, \\\"intra_sub_pct\\\": 49.4, \\\"extra_sub_pct\\\": 30.8, \\\"intra_sub_per_100_gold\\\": 12.93}}, \\\"correlation\\\": {\\\"intra_sub_vs_bcs_spearman_rho\\\": 1, \\\"intra_sub_vs_bcs_p\\\": \\\"<0.001\\\", \\\"chi_square\\\": 6952, \\\"chi_square_p\\\": \\\"~0\\\"}, \\\"exp2_controlled\\\": {\\\"trend\\\": \\\"IntraSub 3.2% -> 7.3% -> 8.6% (rho=1.0, p<0.001)\\\"}, \\\"key_finding\\\": \\\"BCS>=0.95: 49.4% FP are intra-batch type confusion (13/100 gold). Hallucination+boundary <3%. LLM main error mode is type confusion, not hallucination.\\\"}, \\\"hypothesis\\\": \\\"Intra-batch type substitution errors scale monotonically with BCS while missed-entity rates are driven primarily by count, establishing mechanistically distinct error channels that decompose total degradation into confusability-driven and capacity-driven components.\\\"}, \\\"exp004_maven_bcs\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"exp1_count_curve\\\": {\\\"count_1\\\": {\\\"n_batches\\\": 64, \\\"exact_f1\\\": 0.009, \\\"relaxed_f1\\\": 0.106, \\\"bcs\\\": 0}, \\\"count_6\\\": {\\\"n_batches\\\": 5, \\\"exact_f1\\\": 0.003, \\\"relaxed_f1\\\": 0.103, \\\"bcs\\\": 0.892}, \\\"count_12\\\": {\\\"n_batches\\\": 5, \\\"exact_f1\\\": 0.008, \\\"relaxed_f1\\\": 0.146, \\\"bcs\\\": 0.921}, \\\"count_22\\\": {\\\"n_batches\\\": 5, \\\"exact_f1\\\": 0.013, \\\"relaxed_f1\\\": 0.185, \\\"bcs\\\": 0.933}, \\\"count_44\\\": {\\\"n_batches\\\": 5, \\\"exact_f1\\\": 0.018, \\\"relaxed_f1\\\": 0.247, \\\"bcs\\\": 0.967}, \\\"count_64\\\": {\\\"n_batches\\\": 5, \\\"exact_f1\\\": 0.013, \\\"relaxed_f1\\\": 0.245, \\\"bcs\\\": 0.973}}, \\\"exp2_bcs_controlled\\\": {\\\"count_6_high_bcs\\\": {\\\"exact_f1\\\": 0.0354, \\\"relaxed_f1\\\": 0.211, \\\"bcs\\\": 0.9447}, \\\"count_6_low_bcs\\\": {\\\"exact_f1\\\": 0.0068, \\\"relaxed_f1\\\": 0.089, \\\"bcs\\\": 0.8709}, \\\"count_12_high_bcs\\\": {\\\"exact_f1\\\": 0.0151, \\\"relaxed_f1\\\": 0.1568, \\\"bcs\\\": 0.9447}, \\\"count_12_low_bcs\\\": {\\\"exact_f1\\\": 0.0068, \\\"relaxed_f1\\\": 0.105, \\\"bcs\\\": 0.9148}}, \\\"key_finding\\\": \\\"MAVEN batch-level: high_bcs relaxed_F1 2.4x vs low_bcs (count_6). Direction same as Few-NERD batch-level (positive). Pairwise + per-type analysis needed to control frequency confound.\\\", \\\"note\\\": \\\"exact_F1 very low (0.003-0.035), relaxed_F1 usable (0.089-0.247). Event trigger boundary matching is fuzzy. A re-run (500 samples) is still in progress in artifacts/exp004/.\\\"}, \\\"hypothesis\\\": \\\"Schema-induced confusability degradation (higher BCS → lower F1) replicates on MAVEN event detection, confirming the channel generalizes beyond NER/RE to event extraction tasks with semantically dense type inventories.\\\"}, \\\"exp003a_prompt_v2_rerun\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"eval_mode\\\": \\\"text_match\\\", \\\"exp1_text_match\\\": {\\\"count_1\\\": {\\\"f1\\\": 0.323, \\\"precision\\\": 0.216, \\\"recall\\\": 0.641, \\\"pred_gold_ratio\\\": 2.97, \\\"n_batches\\\": 64}, \\\"count_2\\\": {\\\"f1\\\": 0.273, \\\"precision\\\": 0.18, \\\"recall\\\": 0.56, \\\"pred_gold_ratio\\\": 3.11, \\\"n_batches\\\": 5}, \\\"count_6\\\": {\\\"f1\\\": 0.306, \\\"precision\\\": 0.226, \\\"recall\\\": 0.475, \\\"pred_gold_ratio\\\": 2.1, \\\"n_batches\\\": 5}, \\\"count_12\\\": {\\\"f1\\\": 0.347, \\\"precision\\\": 0.367, \\\"recall\\\": 0.329, \\\"pred_gold_ratio\\\": 0.9, \\\"n_batches\\\": 5}, \\\"count_22\\\": {\\\"f1\\\": 0.299, \\\"precision\\\": 0.339, \\\"recall\\\": 0.267, \\\"pred_gold_ratio\\\": 0.79, \\\"n_batches\\\": 5}, \\\"count_44\\\": {\\\"f1\\\": 0.445, \\\"precision\\\": 0.506, \\\"recall\\\": 0.396, \\\"pred_gold_ratio\\\": 0.78, \\\"n_batches\\\": 5}, \\\"count_64\\\": {\\\"f1\\\": 0.414, \\\"precision\\\": 0.648, \\\"recall\\\": 0.304, \\\"pred_gold_ratio\\\": 0.47, \\\"n_batches\\\": 5}}, \\\"exp2_text_match\\\": {\\\"count_6\\\": {\\\"f1\\\": 0.32, \\\"precision\\\": 0.26, \\\"recall\\\": 0.416, \\\"pred_gold_ratio\\\": 1.6, \\\"n_batches\\\": 27}, \\\"count_12\\\": {\\\"f1\\\": 0.306, \\\"precision\\\": 0.291, \\\"recall\\\": 0.323, \\\"pred_gold_ratio\\\": 1.11, \\\"n_batches\\\": 27}}, \\\"vs_exp001_delta\\\": {\\\"count_1\\\": {\\\"f1_delta\\\": \\\"+0.139 (+76%)\\\", \\\"precision_delta\\\": \\\"+0.111 (+106%)\\\", \\\"recall_delta\\\": \\\"-0.079 (-11%)\\\", \\\"overpred_fix\\\": \\\"6.85→2.97\\\"}, \\\"count_6\\\": {\\\"f1_delta\\\": \\\"+0.151 (+97%)\\\", \\\"precision_delta\\\": \\\"+0.138 (+157%)\\\", \\\"recall_delta\\\": \\\"-0.145 (-23%)\\\"}, \\\"count_12\\\": {\\\"f1_delta\\\": \\\"+0.101 (+41%)\\\", \\\"precision_delta\\\": \\\"+0.207 (+129%)\\\", \\\"recall_delta\\\": \\\"-0.210 (-39%)\\\"}, \\\"count_44\\\": {\\\"f1_delta\\\": \\\"-0.028 (-6%)\\\", \\\"precision_delta\\\": \\\"+0.092 (+22%)\\\", \\\"recall_delta\\\": \\\"-0.155 (-28%)\\\"}, \\\"count_64\\\": {\\\"f1_delta\\\": \\\"-0.049 (-11%)\\\", \\\"precision_delta\\\": \\\"+0.128 (+25%)\\\", \\\"recall_delta\\\": \\\"-0.114 (-27%)\\\"}}, \\\"key_finding\\\": \\\"V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1). But over-corrected at high counts: under-prediction (pred/gold<1) caused recall drops of 27-39%, slightly lowering F1 at count_22-64.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"A restructured prompt (v2: definition-enriched, explicit output constraints) modulates the magnitude of count-driven and BCS-driven degradation but does not eliminate either channel, confirming schema configuration as the dominant factor.\\\"}, \\\"exp002_confusability_controlled\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"data_source\\\": \\\"exp2_reeval_results.json (text_match, CLEAN)\\\", \\\"primary_recall_vs_bcs\\\": {\\\"count_6\\\": {\\\"r\\\": 0.2754, \\\"p\\\": 0.1644, \\\"n\\\": 27, \\\"verdict\\\": \\\"FAIL\\\"}, \\\"count_12\\\": {\\\"r\\\": 0.2219, \\\"p\\\": 0.266, \\\"n\\\": 27, \\\"verdict\\\": \\\"FAIL\\\"}, \\\"partial\\\": {\\\"r\\\": 0.2522, \\\"p\\\": 0.0658, \\\"n\\\": 54, \\\"verdict\\\": \\\"FAIL\\\"}}, \\\"secondary_f1_vs_bcs\\\": {\\\"count_6\\\": {\\\"r\\\": 0.1754, \\\"p\\\": 0.3814, \\\"n\\\": 27, \\\"verdict\\\": \\\"FAIL\\\"}, \\\"count_12\\\": {\\\"r\\\": 0.5012, \\\"p\\\": 0.0077, \\\"n\\\": 27, \\\"verdict\\\": \\\"PASS\\\"}, \\\"partial\\\": {\\\"r\\\": 0.3025, \\\"p\\\": 0.0262, \\\"n\\\": 54, \\\"verdict\\\": \\\"PASS\\\"}}, \\\"mechanistic_confusion_rate\\\": {\\\"random_batches\\\": {\\\"count_6_high\\\": 0.0157, \\\"count_6_low\\\": 0.0088, \\\"ratio_6\\\": 1.7, \\\"count_12_high\\\": 0.0304, \\\"count_12_low\\\": 0.0131, \\\"ratio_12\\\": 2.4}, \\\"extreme_batches\\\": {\\\"count_6_high\\\": 0.0728, \\\"count_6_low\\\": 0.0014, \\\"ratio_6\\\": 27.5, \\\"count_12_high\\\": 0.048, \\\"count_12_low\\\": 0.0061, \\\"ratio_12\\\": 9.9}, \\\"verdict\\\": \\\"PASS\\\"}, \\\"pairwise_confusion_analysis\\\": {\\\"all\\\": {\\\"n_pairs\\\": 1953, \\\"pearson_r\\\": 0.156, \\\"pearson_p\\\": 4.6e-12, \\\"spearman_rho\\\": 0.16, \\\"spearman_p\\\": 1.3e-12}, \\\"count_6\\\": {\\\"n_pairs\\\": 1770, \\\"pearson_r\\\": 0.078, \\\"pearson_p\\\": 0.001}, \\\"count_12\\\": {\\\"n_pairs\\\": 1953, \\\"pearson_r\\\": 0.147, \\\"pearson_p\\\": 6.7e-11}, \\\"nonzero_only\\\": {\\\"all_spearman_rho\\\": 0.254, \\\"all_spearman_p\\\": 1.1e-06, \\\"count_12_pearson_r\\\": 0.212, \\\"count_12_p\\\": 0.00034}, \\\"top_confused_pair\\\": \\\"person-other <-> person-politician (BCS=0.934, confusion=156)\\\"}, \\\"per_type_analysis\\\": {\\\"n_types\\\": 63, \\\"filter\\\": \\\"freq>=5\\\", \\\"micro_f1_vs_bcs\\\": {\\\"pearson_r\\\": -0.1828, \\\"pearson_p\\\": 0.1516, \\\"spearman_rho\\\": -0.2927, \\\"spearman_p\\\": 0.0199, \\\"partial_r_ctrl_logfreq\\\": -0.1998, \\\"partial_p\\\": 0.1163}, \\\"mean_f1_vs_bcs\\\": {\\\"pearson_r\\\": -0.1374, \\\"pearson_p\\\": 0.283, \\\"spearman_rho\\\": -0.2412, \\\"spearman_p\\\": 0.0568, \\\"partial_r_ctrl_logfreq\\\": -0.1428, \\\"partial_p\\\": 0.2641}, \\\"quartile_comparison\\\": {\\\"low_bcs_cutoff\\\": 0.798, \\\"high_bcs_cutoff\\\": 0.827, \\\"low_bcs_f1\\\": 0.3098, \\\"high_bcs_f1\\\": 0.2275, \\\"delta_f1\\\": -0.0823, \\\"low_bcs_freq\\\": 2134, \\\"high_bcs_freq\\\": 2049}, \\\"confound_check\\\": {\\\"bcs_vs_logfreq_r\\\": 0.042, \\\"bcs_vs_logfreq_p\\\": 0.74, \\\"logfreq_vs_f1_r\\\": 0.25, \\\"logfreq_vs_f1_p\\\": 0.048}, \\\"verdict\\\": \\\"Direction supports hypothesis. Spearman significant (p=0.02). Frequency confound absent at type level (r=0.04).\\\"}, \\\"overall_verdict\\\": \\\"PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE STRONG PASS, PER-TYPE DIRECTIONAL PASS\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"At fixed type count, batches with higher mean pairwise embedding similarity (BCS) produce lower NER recall because semantically confusable types compete for the same entity mentions, increasing substitution errors.\\\"}, \\\"fewrel_pilot\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"embedding\\\": \\\"all-MiniLM-L6-v2\\\", \\\"n_batches\\\": 15, \\\"n_predictions\\\": 374, \\\"count_4\\\": {\\\"low_bcs_acc\\\": 0.917, \\\"high_bcs_acc\\\": 0.708, \\\"delta_pp\\\": -20.9, \\\"low_bcs\\\": 0.42, \\\"high_bcs\\\": 0.97}, \\\"count_8\\\": {\\\"low_bcs_acc\\\": 1, \\\"high_bcs_acc\\\": 0.5, \\\"delta_pp\\\": -50, \\\"low_bcs\\\": 0.47, \\\"high_bcs\\\": 0.97}, \\\"count_16\\\": {\\\"low_bcs_acc\\\": 0.917, \\\"high_bcs_acc\\\": 0.431, \\\"delta_pp\\\": -48.6, \\\"low_bcs\\\": 0.57, \\\"high_bcs\\\": 0.97}, \\\"key_finding\\\": \\\"BCS-accuracy strong negative: high-BCS batches 43-71% vs low-BCS 92-100%. Effect increases with count. Cross-task (NER→RE) replication of confusability hypothesis.\\\"}, \\\"hypothesis\\\": \\\"Pairwise embedding similarity (SCS) between relation types predicts extraction accuracy degradation: high-BCS batches yield lower accuracy than low-BCS batches at matched count, establishing the confusability channel on RE.\\\"}, \\\"exp-004\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_event_types\\\": 168, \\\"n_pairs\\\": 14028, \\\"scs_mean\\\": 0.2161, \\\"scs_std\\\": 0.103, \\\"scs_max\\\": 0.8368, \\\"scs_median\\\": 0.2121, \\\"scs_q90\\\": 0.3457, \\\"scs_q95\\\": 0.3892, \\\"pairs_above_0.5\\\": 119, \\\"pct_above_0.5\\\": 0.85, \\\"train_docs\\\": 2913, \\\"train_mentions\\\": 77993, \\\"valid_docs\\\": 710, \\\"valid_mentions\\\": 18904}, \\\"hypothesis\\\": \\\"MAVEN's 168 FrameNet-derived event types exhibit higher mean SCS than Few-NERD's cross-domain entity types due to same-domain semantic clustering, enabling a cross-task replication test of confusability effects.\\\"}, \\\"exp001_count_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"diagnosis\\\": \\\"char offset 96.5% fabricated by model\\\", \\\"text_match_reeval\\\": {\\\"count_1\\\": {\\\"f1\\\": 0.184, \\\"precision\\\": 0.105, \\\"recall\\\": 0.72, \\\"pred_gold_ratio\\\": 6.85}, \\\"count_2\\\": {\\\"f1\\\": 0.123, \\\"precision\\\": 0.068, \\\"recall\\\": 0.698, \\\"pred_gold_ratio\\\": 10.33}, \\\"count_6\\\": {\\\"f1\\\": 0.155, \\\"precision\\\": 0.088, \\\"recall\\\": 0.62, \\\"pred_gold_ratio\\\": 7.02}, \\\"count_12\\\": {\\\"f1\\\": 0.246, \\\"precision\\\": 0.16, \\\"recall\\\": 0.539, \\\"pred_gold_ratio\\\": 3.38}, \\\"count_22\\\": {\\\"f1\\\": 0.322, \\\"precision\\\": 0.232, \\\"recall\\\": 0.527, \\\"pred_gold_ratio\\\": 2.27}, \\\"count_44\\\": {\\\"f1\\\": 0.473, \\\"precision\\\": 0.414, \\\"recall\\\": 0.551, \\\"pred_gold_ratio\\\": 1.33}, \\\"count_64\\\": {\\\"f1\\\": 0.463, \\\"precision\\\": 0.52, \\\"recall\\\": 0.418, \\\"pred_gold_ratio\\\": 0.8}}, \\\"key_finding\\\": \\\"recall monotonically decreases (0.72→0.42), precision monotonically increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at count_44\\\", \\\"wrong_type_trend\\\": \\\"type confusion increases with count: 0→2434, supports confusability hypothesis\\\", \\\"spurious_dominant\\\": \\\"spurious FPs (text in source but not entity) dominate at low count, not hallucination\\\", \\\"conclusion_text_match\\\": \\\"F1 curve inversion caused by over-prediction confound, NOT absence of confusability effect. Recall curve + type confusion pattern support hypothesis.\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Increasing the number of schema types in a zero-shot LLM extraction prompt degrades per-type recall due to bounded attention capacity and instruction-following limits, producing a monotonic count-performance curve on Few-NERD NER.\\\"}, \\\"exp_fewrel_16rel_bootstrap\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。\\\", \\\"metrics\\\": {\\\"n_batches\\\": 100, \\\"pool_size\\\": 16, \\\"batch_size\\\": 8, \\\"bcs_range\\\": [0.6532, 0.9002], \\\"quartile_delta\\\": {\\\"Q4_minus_Q1_pp\\\": -5.31, \\\"ci_95_lower\\\": -9.45, \\\"ci_95_upper\\\": -4.49, \\\"note\\\": \\\"CI values from pre-D038 bootstrap, may need re-verification with MEAN-based BCS\\\"}, \\\"pearson_r_bcs_acc\\\": -0.467, \\\"regression_slope\\\": {\\\"slope\\\": -0.509, \\\"ci_95_lower\\\": -0.556, \\\"ci_95_upper\\\": -0.349, \\\"r_squared\\\": 0.218, \\\"p_value\\\": 1.01e-12, \\\"interpretation\\\": \\\"per +0.1 BCS → -5.09pp accuracy\\\", \\\"note\\\": \\\"CI from pre-D038 bootstrap\\\"}, \\\"amplification_ratio\\\": {\\\"quartile_16_vs_80\\\": 4.2, \\\"ci_95_lower\\\": 3.3, \\\"ci_95_upper\\\": 6.95}, \\\"key_finding\\\": \\\"16-rel pool BCS effect (MEAN-based, D038): Δ(Q4-Q1)=-5.31pp, r=-0.467. Regression slope=-0.509. Bootstrap 1000 resamples. [D038 MEAN correction applied, old values: r=-0.637/Δ=-7.42pp/slope=-0.449]\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_docred_confusability\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"n_relation_types\\\": 96, \\\"n_eval_samples\\\": 1240, \\\"total_inferences\\\": 13618, \\\"count_curve\\\": {\\\"count_1\\\": 0.88, \\\"count_4\\\": 0.77, \\\"count_8\\\": 0.774, \\\"count_16\\\": 0.524, \\\"count_32\\\": 0.521, \\\"count_64\\\": 0.424, \\\"count_96\\\": 0.387}, \\\"bcs_effect_count16\\\": {\\\"low_bcs_acc\\\": 0.679, \\\"high_bcs_acc\\\": 0.447, \\\"gap\\\": 0.233, \\\"spearman_r\\\": -0.661, \\\"slope\\\": -0.713, \\\"slope_95ci\\\": [-0.909, -0.529]}, \\\"bcs_effect_count32\\\": {\\\"low_bcs_acc\\\": 0.578, \\\"high_bcs_acc\\\": 0.403, \\\"gap\\\": 0.176, \\\"spearman_r\\\": -0.509, \\\"slope\\\": -0.69, \\\"slope_95ci\\\": [-0.854, -0.519]}}}, \\\"exp_fewrel_v2_bcs_controlled\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"验证 Channel 2 (BCS→type confusion) 在 v2 prompt 下方向一致。FewRel 80-rel, count=8, low-BCS 5 batches + high-BCS 5 batches, Qwen3-32B-FP8, v2 prompt。D037 Round 2 审稿 C1b。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"low_bcs_mean_acc\\\": 0.8042, \\\"high_bcs_mean_acc\\\": 0.725, \\\"delta_low_minus_high_pp\\\": 7.92, \\\"bootstrap_ci_95_lower_pp\\\": -5.21, \\\"bootstrap_ci_95_upper_pp\\\": 21.46, \\\"n_bootstrap\\\": 10000, \\\"n_batches_per_group\\\": 5, \\\"samples_per_batch\\\": 96, \\\"total_inferences\\\": 960}}, \\\"exp_fewrel_16rel_100batch\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"D033: 16-rel pool 100 random batches (count_8) + bootstrap CI，填补 tab:bcs_controlled 16-rel 空白，为 3.4× amplification ratio 提供双端 CI 支撑。\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp012_llama_fewrel_ch2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"LLaMA-3.1-8B-Instruct 在 FewRel 80-rel RE 任务上验证 Channel 2 (BCS-controlled confusability effect)。跨模型家族(Qwen→LLaMA) + 跨规模(32B→8B) + 跨任务(NER→RE) 三重泛化验证。exp2 design: count 8/16 × low/high BCS × 27 batches。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"exp2_bcs_controlled\\\": {\\\"count_8\\\": {\\\"low_bcs_acc\\\": 0.7812, \\\"high_bcs_acc\\\": 0.5104, \\\"delta_pp\\\": -27.1}, \\\"count_16\\\": {\\\"low_bcs_acc\\\": 0.7552, \\\"high_bcs_acc\\\": 0.5156, \\\"delta_pp\\\": -24}}, \\\"overall_correlation\\\": {\\\"n_batches\\\": 54, \\\"pearson_r\\\": -0.39, \\\"pearson_p\\\": 0.004, \\\"spearman_rho\\\": -0.43, \\\"spearman_p\\\": 0.001}, \\\"cross_model_comparison\\\": {\\\"llama_delta_pp\\\": -27.1, \\\"qwen3_delta_pp\\\": -31.2, \\\"ratio\\\": 0.87, \\\"note\\\": \\\"LLaMA effect = 87% of Qwen3, direction and magnitude consistent\\\"}, \\\"no_floor_effect\\\": true, \\\"mean_accuracy\\\": 0.77, \\\"accuracy_range\\\": \\\"0.41-0.98\\\", \\\"key_finding\\\": \\\"BCS confusability effect cross-model replicated: LLaMA Δ=-27.1pp (87% of Qwen3 -31.2pp). Pearson r=-0.39 (p=0.004), Spearman ρ=-0.43 (p=0.001). No floor effect.\\\"}}, \\\"exp012_llama_8b_r2_exp2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"LLaMA-3.1-8B-Instruct exp2 重跑：BCS-controlled factorial (count=6/12, low/high BCS)，验证 confusability effect 跨模型泛化。Parent exp012_llama_8b_r2 的 exp1 count curve 已完成。\\\", \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp012_llama_8b_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"LLaMA-3.1-8B-Instruct 复现 confusability-driven type confusion（chat template 修复版）。验证 confusability effect 跨模型家族（Qwen→LLaMA）+ 跨规模（32B→8B）泛化。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"exp1_llama_recall_count1\\\": 0.702, \\\"exp1_llama_recall_count64\\\": 0.273, \\\"exp1_recall_decline_pp\\\": -42.9, \\\"exp1_per_batch_recall_corr_vs_qwen\\\": 0.7249, \\\"exp1_llama_text_match_f1_range\\\": \\\"0.06-0.36\\\", \\\"exp1_exact_f1\\\": 0, \\\"exp1_note\\\": \\\"exact/relaxed F1=0 due to missing char offsets, text_match is correct metric\\\"}}, \\\"exp006_interaction_2x2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"Count × Confusability 交互效应：{low count, high count} × {low BCS, high BCS} 2×2 设计，测试 count 和 confusability 对 accuracy 的影响是 additive 还是 multiplicative。若 multiplicative，高 count + 高 BCS 组的 degradation 应超过两个主效应之和。\\\", \\\"metrics\\\": {\\\"cell_means_f1\\\": {\\\"low_count_low_bcs\\\": 0.324, \\\"low_count_high_bcs\\\": 0.313, \\\"high_count_low_bcs\\\": 0.325, \\\"high_count_high_bcs\\\": 0.277}, \\\"main_effects\\\": {\\\"count\\\": -0.018, \\\"bcs\\\": -0.029}, \\\"interaction\\\": {\\\"estimate\\\": -0.036, \\\"z\\\": -0.667, \\\"p\\\": 0.505, \\\"bcs_effect_at_low_count\\\": -0.011, \\\"bcs_effect_at_high_count\\\": -0.048}, \\\"verdict\\\": \\\"交互方向符合 multiplicative 假设但统计不显著 (p=0.505)，未检测到显著交互效应\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"exp012_llama_awq\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp012_llama_8b_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_8b\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"exp_fewrel_40rel_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_fewrel_40rel_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_fewnerd_r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"hypothesis\\\": \\\"LLaMA model replicates confusability-driven type confusion pattern observed with Qwen, validating model-independence of the phenomenon\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_8b_fewnerd\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp_fewrel_40rel\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_fewnerd_r3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_fewnerd_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp012_llama_fewnerd\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"exp008_sdgd_zero_fewnerd\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}}, \\\"count\\\": 50, \\\"total\\\": 50, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.1891}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_unconstrained_decoding_ablation\": {\"status\": \"DONE\", \"hypothesis\": \"The BCS-accuracy correlation in RE arises from semantic confusion rather than forced-choice format artifacts. If removing the enum constraint (relaxed decoding) preserves the negative BCS-accuracy correlation direction and significance, confusability is a genuine semantic property; if the correlation disappears, the effect is specific to constrained classification where all errors are channeled into type substitution. Either outcome strengthens the paper: preservation broadens the claim, disappearance validates the error-channeling hypothesis stated in Discussion.\", \"conclusion\": \"success\", \"metrics\": {\"n10\": {\"low_bcs_mean_acc\": 0.8042, \"high_bcs_mean_acc\": 0.725, \"delta_pp\": 7.92, \"spearman_rho\": -0.4303, \"spearman_pval\": 0.214, \"oov_rate\": 0}, \"n25\": {\"low_bcs_mean_acc\": 0.8093, \"high_bcs_mean_acc\": 0.7812, \"delta_pp\": 2.8, \"ci_95_lower_pp\": -4.53, \"ci_95_upper_pp\": 10.56, \"spearman_rho\": -0.1442, \"spearman_pval\": 0.492, \"oov_rate\": 0.0008, \"total_samples\": 2400}}}, \"exp_multiseed_bcs_re\": {\"status\": \"DONE\", \"hypothesis\": \"The BCS-accuracy correlation observed in FewRel BCS-controlled experiments (R²=0.22-0.53) is robust across random seeds. If seed=123 and seed=456 replicate the negative BCS-accuracy correlation direction and significance observed with seed=42, this confirms the finding is not a single-seed artifact. Rebuttal material for R15-W2 single-seed concern.\", \"conclusion\": \"success\", \"metrics\": {\"seed_123\": {\"shot0_delta_pp\": 21.88, \"shot1_delta_pp\": 25.25, \"shot5_delta_pp\": 24.25, \"shot0_ci\": [18.79, 24.83], \"shot1_ci\": [21.08, 29.29], \"shot5_ci\": [19.96, 28.29]}, \"seed_456\": {\"shot0_delta_pp\": 22.38, \"shot1_delta_pp\": 24.38, \"shot5_delta_pp\": 25.08, \"shot0_ci\": [19.58, 24.96], \"shot1_ci\": [20.58, 28.04], \"shot5_ci\": [21.62, 28.58]}, \"finding\": \"Few-shot does NOT mitigate BCS effect; delta increases from ~22pp (0-shot) to ~25pp (5-shot)\"}}, \"exp_gemini_flash_cross_model\": {\"status\": \"DONE\", \"hypothesis\": \"The two-dimensional degradation pattern (count-related decline + confusability-related type confusion) generalizes beyond open-weight models to proprietary API models. Gemini 2.5 Flash should show: (1) monotonic RE accuracy decline with count, and (2) significant BCS-accuracy correlation on extreme batches. If confirmed, the pattern is architecture-family-independent (open-weight Qwen/LLaMA + proprietary Gemini).\", \"conclusion\": \"success\", \"metrics\": {\"count_curve_spearman_rho\": -0.943, \"count_curve_spearman_p\": 0.0048, \"count_1_acc\": 0.8267, \"count_4_acc\": 0.8725, \"count_8_acc\": 0.8204, \"count_16_acc\": 0.7868, \"count_32_acc\": 0.7394, \"count_64_acc\": 0.6343, \"total_drop_count1_to_64_pp\": -19.2, \"complete_count_levels\": \"1,4,8,16,32\", \"partial_count_levels\": \"64 (11/25)\", \"missing\": \"count_80, part2_bcs\", \"note\": \"tmux resumed, still collecting remaining data\"}}, \"exp_schema_intervention\": {\"status\": \"DONE\", \"hypothesis\": \"If type confusability is a causal driver of extraction errors, then renaming high-BCS type pairs to reduce embedding similarity (while preserving semantic equivalence) should improve accuracy on high-BCS batches. This tests the causal direction: SCS → confusion, not merely correlation. If treatment (renamed) accuracy on previously-high-BCS batches improves significantly over control (original names), confusability is actionable via schema design.\", \"conclusion\": \"negative\", \"metrics\": {\"high_bcs_control\": 0.693, \"high_bcs_treatment\": 0.605, \"high_bcs_delta\": -0.0883, \"low_bcs_control\": 0.901, \"low_bcs_treatment\": 0.871, \"low_bcs_delta\": -0.0296, \"interaction_delta\": -0.0588, \"interaction_p\": \"<0.001\", \"interaction_t\": -7.23, \"rename_count_correlation_r\": -0.625, \"rename_count_correlation_p\": \"<0.001\", \"cohens_d_high\": -2.92, \"cohens_d_low\": -1.09}}, \"exp_fewshot_bcs_v2\": {\"status\": \"DONE\", \"hypothesis\": \"Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples, tested on extreme-BCS batches (low ~0.36, high ~0.80) where 0-shot delta is ~25-31pp. If delta shrinks significantly under few-shot, confusability is addressable via prompting. If delta persists, confusability is a fundamental schema-structural constraint.\", \"conclusion\": \"negative\", \"metrics\": {\"0shot_low_bcs\": 0.6821, \"0shot_high_bcs\": 0.4975, \"0shot_delta_pp\": 18.46, \"1shot_low_bcs\": 0.7538, \"1shot_high_bcs\": 0.5542, \"1shot_delta_pp\": 19.96, \"5shot_low_bcs\": 0.7154, \"5shot_high_bcs\": 0.4875, \"5shot_delta_pp\": 22.79, \"delta_widening_0to5shot_pp\": 4.33, \"widening_p_value\": 0.014}}, \"exp_llama70b_cross_model\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA 3.1 70B-Instruct FP8 will replicate the two-dimensional degradation pattern (count-associated recall decline + confusability-associated type confusion) observed on Qwen3-32B, with BCS-accuracy correlation direction preserved despite potential magnitude differences. 70B scale should show stronger Dimension 2 signal than 8B, closing the gap with 32B.\", \"metrics\": {\"exp1_fewrel_count_curve\": {\"count_8_to_80_decline_pp\": -30.7, \"vs_qwen3_decline_pp\": -30.1, \"note\": \"slopes near-identical, 70B absolute ~4pp lower\"}, \"exp2_bcs_controlled\": {\"count_16_low_bcs\": 0.7083, \"count_16_high_bcs\": 0.599, \"delta_pp\": 10.94, \"ci_95\": [3.02, 20.1], \"count_8_delta_pp\": -4.2, \"count_8_note\": \"BCS range too narrow, CI crosses zero\"}, \"exp3_fewnerd_unified_protocol\": {\"metric\": \"text_match recall (unified with Qwen3 protocol: offset correction + hallucination detection + greedy matching + type+text)\", \"count_2\": {\"llama70b\": 0.323, \"qwen3\": 0.515, \"delta_pp\": -19}, \"count_6\": {\"llama70b\": 0.3, \"qwen3\": 0.399, \"delta_pp\": -10}, \"count_12\": {\"llama70b\": 0.278, \"qwen3\": 0.318, \"delta_pp\": -4}, \"count_22\": {\"llama70b\": 0.252, \"qwen3\": 0.279, \"delta_pp\": -3}, \"count_44\": {\"llama70b\": 0.297, \"qwen3\": 0.309, \"delta_pp\": -1}, \"count_66\": {\"llama70b\": 0.273, \"qwen3\": 0.407, \"delta_pp\": -13}, \"precision\": {\"count_2\": {\"llama70b\": 0.446, \"qwen3\": 0.32}, \"count_6\": {\"llama70b\": 0.323, \"qwen3\": 0.248}, \"count_12\": {\"llama70b\": 0.311, \"qwen3\": 0.269}, \"count_22\": {\"llama70b\": 0.376, \"qwen3\": 0.365}, \"count_44\": {\"llama70b\": 0.468, \"qwen3\": 0.504}, \"count_66\": {\"llama70b\": 0.609, \"qwen3\": 0.633}}, \"n_batches\": 25, \"status\": \"complete\", \"result_path\": \"/root/schema-dag-extraction/artifacts/d051_llama-3.1-70b-fp8_fewnerd_n25_s42/summary_unified_protocol.json\", \"key_findings\": [\"Old values invalidated: count_2 0.962→0.323 (-64pp)\", \"70B recall lower than Qwen3 at all counts (1-19pp gap)\", \"70B more conservative: higher precision, lower recall\", \"Middle range count_12-44 close (1-4pp gap)\", \"Both models show count-driven decline pattern\"]}}, \"conclusion\": \"success\"}, \"exp_fewshot_bcs_mitigation\": {\"status\": \"DONE\", \"hypothesis\": \"Few-shot demonstrations (1-shot and 5-shot) reduce the BCS-driven confusability effect (high-BCS accuracy penalty) by grounding type boundaries through explicit examples. If the BCS delta (low-high) shrinks significantly under few-shot, confusability is addressable via better prompting. If delta persists, confusability is a fundamental schema-structural constraint even with demonstrations.\", \"conclusion\": \"killed\"}, \"exp_prompt_sensitivity\": {\"status\": \"DONE\", \"hypothesis\": \"BCS-driven type confusion is a schema-structural property independent of prompt wording: the BCS-accuracy correlation direction and significance persist across diverse prompt variants (V2 baseline, instruction-rewrite, chain-of-thought, minimal), confirming that confusability effects arise from schema composition rather than prompt-specific instruction framing.\", \"metrics\": {\"per_condition\": {\"v2_count8\": {\"mean_acc\": 0.7688, \"bcs_r\": -0.3326, \"bcs_p\": 0.348}, \"v2_count32\": {\"mean_acc\": 0.5643, \"bcs_r\": -0.6477, \"bcs_p\": 0.043, \"significant\": true}, \"instruction_rewrite_count8\": {\"mean_acc\": 0.8469, \"bcs_r\": -0.2228, \"bcs_p\": 0.536}, \"instruction_rewrite_count32\": {\"mean_acc\": 0.6617, \"bcs_r\": -0.4693, \"bcs_p\": 0.171}, \"cot_count8\": {\"mean_acc\": 0.749, \"bcs_r\": 0.2543, \"bcs_p\": 0.478}, \"cot_count32\": {\"mean_acc\": 0.6169, \"bcs_r\": -0.5661, \"bcs_p\": 0.088}, \"minimal_count8\": {\"mean_acc\": 0.8521, \"bcs_r\": -0.1703, \"bcs_p\": 0.638}, \"minimal_count32\": {\"mean_acc\": 0.6146, \"bcs_r\": -0.771, \"bcs_p\": 0.009, \"significant\": true}}, \"summary\": {\"negative_direction\": \"7/8 conditions\", \"significant_at_count32\": \"2/4 (v2 p=0.043, minimal p=0.009), 1 marginal (cot p=0.088)\", \"count_as_moderator\": \"count=32 effects stronger than count=8, consistent with BCS range compression at lower counts\", \"cot_anomaly\": \"only variant with positive r at count_8 (0.25, n.s.)\"}, \"key_finding\": \"BCS-accuracy negative correlation is directionally consistent across 4 prompt variants at count=32 (7/8 conditions negative). Prompt design modulates magnitude but does not eliminate the effect. Supports schema-structural interpretation of confusability.\"}, \"conclusion\": \"success\"}, \"exp_sdgd_routing_strategies\": {\"status\": \"DONE\", \"hypothesis\": \"Max-confidence and none-aware routing strategies can recover a significant fraction of the oracle routing gain (+29.8pp over single-pass) by using LLM generation logprobs to select the most reliable sub-schema prediction, since the correct sub-schema should produce higher-confidence predictions than sub-schemas forced to classify into unrelated types.\", \"conclusion\": \"negative\", \"metrics\": {\"strategies\": {\"single_pass\": {\"accuracy\": 0.504}, \"random_routing\": {\"accuracy\": 0.147}, \"max_conf_all\": {\"accuracy\": 0.277}, \"max_conf_positive\": {\"accuracy\": 0.365}, \"none_aware\": {\"accuracy\": 0.365}, \"margin_positive\": {\"accuracy\": 0.359}, \"oracle\": {\"accuracy\": 0.724}}, \"none_detection\": {\"multi_positive_rate\": 0.734, \"exclusive_positive_rate\": 0.07, \"exclusive_positive_precision\": 0.42, \"none_rate_per_group\": \"20-40%\"}, \"key_finding\": \"All practical routing strategies perform worse than single-pass. Structured decoding forces confident predictions even for wrong sub-schemas, making confidence-based and none-aware routing ineffective. Oracle gain (+22pp) is not recoverable via post-hoc routing.\"}}, \"exp_d051_count_curves_25\": {\"status\": \"DONE\", \"metrics\": {\"seed42_complete\": true, \"fewrel_s42\": {\"counts\": [4, 8, 16, 32, 40, 64, 80], \"accuracy_mean\": [0.87, 0.805, 0.719, 0.652, 0.606, 0.539, 0.504], \"n_batches\": 25, \"status\": \"complete\"}, \"fewnerd_s42\": {\"counts\": [2, 6, 12, 22, 44, 66], \"recall_mean\": [0.527, 0.39, 0.306, 0.268, 0.301, 0.407], \"n_batches\": 25, \"status\": \"complete\"}, \"fewrel_s123\": {\"counts\": [4, 8, 16, 32, 40, 64, 80], \"accuracy_mean\": [0.848, 0.799, 0.745, 0.638, 0.609, 0.536, 0.496], \"n_batches\": 25, \"status\": \"complete\"}, \"fewnerd_s123\": {\"counts\": [2, 6, 12, 22, 44, 66], \"recall_mean\": [0.446, 0.422, 0.357, 0.277, 0.272, 0.407], \"n_batches\": 25, \"status\": \"complete\", \"minimum_count\": 44, \"minimum_recall\": 0.272}, \"fewrel_s456\": {\"counts\": [4, 8, 16, 32, 40, 64, 80], \"accuracy_mean\": [0.851, 0.786, 0.692, 0.655, 0.609, 0.535, 0.487], \"n_batches\": 25, \"status\": \"complete\"}, \"fewnerd_s456\": {\"counts\": [2, 6, 12, 22, 44, 66], \"recall_mean\": [0.553, 0.409, 0.305, 0.258, 0.29, 0.407], \"n_batches\": 25, \"status\": \"complete\", \"minimum_count\": 22, \"minimum_recall\": 0.258}, \"cross_seed_fewrel\": {\"max_delta_pp\": 2.7, \"within_1sd\": true, \"note\": \"All 3 seeds monotonic, max pairwise Δ at any count = 2.7pp\"}, \"cross_seed_fewnerd\": {\"note\": \"seed=42 min at count_22 (0.268), seed=123 min at count_44 (0.272), seed=456 min at count_22 (0.258), all within batch SD (~0.10), confirming plateau\"}, \"all_12_complete\": true, \"figure_1a_generated\": true, \"figure_path\": \"figures/paper/fig_count_curves.pdf\"}, \"hypothesis\": \"Increasing batch count from 5 to 25 per count level reduces sampling variance sufficiently to tighten confidence intervals and confirm the U-shaped NER count response is robust across random seeds (42, 123, 456).\", \"conclusion\": \"success\"}, \"exp_confusability_batch_composition\": {\"status\": \"DONE\", \"hypothesis\": \"Confusability-aware batch composition (graph coloring on SCS matrix to separate high-SCS pairs) improves per-type accuracy and reduces substitution errors compared to random batching and single-pass full schema, providing a practical application of the confusability findings.\", \"conclusion\": \"success\", \"metrics\": {\"confusability_aware\": {\"accuracy\": 0.8021, \"macro_f1\": 0.8021, \"mean_batch_bcs\": 0.5524}, \"random_batch_15seeds\": {\"accuracy_mean\": 0.7877, \"accuracy_std\": 0.0178, \"macro_f1_mean\": 0.7877, \"mean_batch_bcs\": 0.5585, \"ci_95_upper\": 0.7967, \"seeds_above_aware\": 2, \"seeds_above_aware_values\": [0.8125, 0.8146]}, \"single_pass\": {\"accuracy\": 0.5042, \"macro_f1\": 0.5042, \"mean_batch_bcs\": 0.5572}, \"improvement\": {\"confusability_vs_random_pp\": 1.44, \"significant\": false, \"rank_among_random\": \"13/15\", \"p_rank\": 0.19, \"p_z\": 0.22, \"note\": \"Directional only. BCS margin 0.006 too narrow for significance at this partition granularity.\"}, \"per_type\": {\"types_improved\": 51, \"types_degraded\": 28, \"mean_delta_pp\": 1.44}, \"n_conditions\": 17, \"n_samples\": 960}}, \"exp_maven_residualized_bcs\": {\"status\": \"DONE\", \"hypothesis\": \"MAVEN per-type BCS 正相关是 centrality artifact。控制 log_freq/degree_centrality 后 BCS-F1 相关应消失。回答审稿人 Q4。\", \"conclusion\": \"success\", \"metrics\": {\"minilm\": {\"raw_rho\": 0.208, \"raw_p\": 0.011, \"confound\": \"log_freq\", \"bcs_confound_r\": 0.201, \"partial_r\": 0.133, \"partial_p\": 0.107}, \"qwen3\": {\"raw_rho\": 0.184, \"raw_p\": 0.025, \"confound\": \"degree_centrality_0.7\", \"bcs_confound_r\": 0.854, \"partial_r\": 0.063, \"partial_p\": 0.442}, \"joint_control\": {\"qwen3_p\": 0.439, \"minilm_p\": 0.226, \"note\": \"Both n.s. after controlling log_freq + degree jointly\"}, \"key_finding\": \"MAVEN BCS-F1 positive correlation is centrality artifact. MiniLM confound=frequency, Qwen3 confound=degree centrality (r=0.854). After joint control, both correlations vanish. Confirms pairwise SCS remains valid but per-type aggregation fails on homogeneous schemas.\"}}, \"exp_fewrel_80pool_16sub_bootstrap\": {\"status\": \"DONE\", \"hypothesis\": \"从 80-rel pool 随机采样 16 types 构造 8-type batches，100 random batches + BCS quartile bootstrap CI。消除跨 pool 混淆（MW1 审稿人），与 D033 独立 16-rel pool 和 80-rel 做三方比较。\", \"metrics\": {\"n_batches\": 100, \"pool_size\": \"80-rel pool, 16-type subsamples\", \"batch_size\": 8, \"mean_accuracy\": 0.8077, \"mean_bcs\": 0.557, \"bcs_range\": [0.4578, 0.6836], \"quartile_delta\": {\"Q4_minus_Q1_pp\": -3.92, \"ci_95_lower\": -7.79, \"ci_95_upper\": 0.42}, \"pearson_r_bcs_acc\": -0.221, \"pearson_p\": 0.027, \"regression_slope\": {\"slope\": -0.401, \"ci_95_lower\": -0.684, \"ci_95_upper\": -0.062, \"interpretation\": \"per +0.1 BCS → -4.01pp accuracy\"}, \"key_finding\": \"80-pool 16-sub BCS effect directional: Δ(Q4-Q1)=-3.92pp CI crosses zero [-7.79,+0.42], but regression slope=-0.401 CI[-0.684,-0.062] excludes zero. Effect weaker than independent 16-rel pool (Δ=-7.42pp) due to narrower BCS range.\"}, \"conclusion\": \"success\"}, \"exp_fewrel_40rel_r4\": {\"status\": \"DONE\", \"metrics\": {\"exp1_acc_count1\": 0.858, \"exp1_acc_count4\": 0.867, \"exp1_acc_count8\": 0.802, \"exp1_acc_count16\": 0.697, \"exp1_acc_count32\": 0.658, \"exp1_acc_count40\": 0.588, \"exp1_decline_pp\": -27, \"exp2_bcs_delta_count8\": 0.333, \"exp2_bcs_delta_count16\": 0.318, \"exp2_low_bcs_acc_count8\": 0.833, \"exp2_high_bcs_acc_count8\": 0.5, \"exp2_low_bcs_acc_count16\": 0.818, \"exp2_high_bcs_acc_count16\": 0.5}, \"conclusion\": \"success\", \"hypothesis\": \"FewRel count-degradation is monotonic across intermediate scales (40 relations): accuracy declines continuously from count=1 through count=40, with no recovery plateau, confirming the scaling pattern observed at 16 and 80 relations.\"}, \"exp_fewrel_factorial_tost\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"design\": {\"factors\": [\"count (4,8,16,32,40)\", \"BCS (continuous)\"], \"n_batches\": 69, \"dataset\": \"FewRel 40-rel\", \"method\": \"multiple regression (accuracy ~ log2_count + BCS + interaction)\"}, \"analysis_1_factorial\": {\"count_F\": 10.98, \"count_p\": 0.002, \"bcs_F\": 1.24, \"bcs_p\": 0.27, \"interaction_F\": 0.6, \"interaction_p\": 0.44, \"tost\": \"inconclusive\", \"n\": 54}, \"analysis_2_regression\": {\"count_beta\": -0.035, \"count_p\": 0.008, \"bcs_beta\": -0.051, \"bcs_p\": 0.0002, \"interaction_beta\": 0.005, \"interaction_p\": 0.61, \"interaction_effect_pp\": 0.47, \"tost_p\": 0.003, \"tost_conclusion\": \"equivalent\", \"equivalence_margin_pp\": 3, \"R_squared\": 0.52, \"n\": 69}, \"analysis_3_cross_dataset\": {\"count_F\": 21.9, \"count_p\": 0.001, \"bcs_F\": 5.9, \"bcs_p\": 0.016, \"interaction_F\": 2.76, \"interaction_p\": 0.098, \"tost\": \"inconclusive\", \"n\": 200}, \"conclusion\": \"Count and BCS channels are additively separable. TOST confirms equivalence (p=0.003, margin ±3pp) in regression analysis.\"}, \"hypothesis\": \"Count and BCS operate as separable (non-interacting) channels on RE accuracy: the count x BCS interaction term is equivalence-bounded within ±3pp (TOST), supporting a two-channel additive degradation model.\"}, \"exp_fewrel_partial_corr_freq\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"pearson_r\": 0.187, \"pearson_p\": 2.56e-26, \"spearman_rho\": 0.227, \"spearman_p\": 3.63e-38, \"n_pairs\": 3160, \"bootstrap_ci_95\": [0.145, 0.231], \"partial_r_eval_freq\": 0.189, \"partial_r_change_pct\": 1.2, \"note\": \"FewRel is perfectly balanced (700 samples/type). Type frequency is zero-variance, cannot confound BCS-confusion relationship. Eval-level frequency partial correlation changes by only 1.2%.\"}, \"hypothesis\": \"The SCS-confusion correlation on FewRel survives partial correlation controlling for type frequency, ruling out the confound that high-SCS pairs are simply rare types with inherently higher error rates.\"}, \"exp_fewrel_formal\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"note\": \"16-rel sanity check only\", \"exp1\": {\"count_1\": {\"mean_acc\": 0.904, \"n_batches\": 16}, \"count_4\": {\"mean_acc\": 0.932, \"n_batches\": 5}, \"count_8\": {\"mean_acc\": 0.867, \"n_batches\": 5}, \"count_16\": {\"mean_acc\": 0.778, \"n_batches\": 5, \"bcs\": 0.9, \"zero_variance\": true}}, \"exp2\": {\"count_8_low_bcs\": {\"acc\": 0.889, \"bcs\": 0.782}, \"count_8_high_bcs\": {\"acc\": 0.798, \"bcs\": 0.892}, \"delta_bcs_effect\": -0.091}, \"trend\": \"count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\"}, \"hypothesis\": \"A 16-relation subset of FewRel exhibits count-driven accuracy degradation consistent with the Few-NERD NER pattern, validating the experimental framework before scaling to the full 80-relation schema.\"}, \"exp_fewrel_formal_80rel\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"exp1_count_curve\": {\"count_1\": {\"acc\": 0.8573, \"n_batches\": 80, \"bcs\": 0}, \"count_4\": {\"acc\": 0.8667, \"n_batches\": 5, \"bcs\": 0.6335}, \"count_8\": {\"acc\": 0.8021, \"n_batches\": 5, \"bcs\": 0.7175}, \"count_16\": {\"acc\": 0.6958, \"n_batches\": 5, \"bcs\": 0.795}, \"count_32\": {\"acc\": 0.6578, \"n_batches\": 5, \"bcs\": 0.8893}, \"count_64\": {\"acc\": 0.5424, \"n_batches\": 5, \"bcs\": 0.9434}, \"count_80\": {\"acc\": 0.5042, \"n_batches\": 5, \"bcs\": 0.9706}}, \"exp2_bcs_controlled\": {\"count_8\": {\"low_bcs_acc\": 0.8229, \"low_bcs\": 0.4715, \"high_bcs_acc\": 0.5104, \"high_bcs\": 0.9706, \"random_acc\": 0.8025, \"delta_pp\": -31.2}, \"count_16\": {\"low_bcs_acc\": 0.8281, \"low_bcs\": 0.5705, \"high_bcs_acc\": 0.5156, \"high_bcs\": 0.9706, \"random_acc\": 0.7169, \"delta_pp\": -31.2}}, \"vs_16rel\": {\"degradation_16rel\": \"-12.6pp (0.904→0.778)\", \"degradation_80rel\": \"-35.3pp (0.857→0.504)\", \"bcs_effect_16rel\": \"-9.1pp\", \"bcs_effect_80rel\": \"-31.2pp\", \"amplification\": \"3.4x\"}, \"key_finding\": \"80-rel count curve 0.857→0.504 (degradation 35.3pp, 远强于 16-rel 12.6pp). BCS effect -31.2pp (3.4x amplification vs 16-rel). 更多 relations → 更大 confusion space → 更强 degradation + BCS effect.\"}, \"hypothesis\": \"Scaling FewRel from 16 to 80 relations amplifies both count-degradation and BCS-accuracy effects due to wider confusability range, producing extreme-batch gaps exceeding 30pp between low-BCS and high-BCS conditions.\"}, \"exp016_fewrel_error_taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"error_distribution\": {\"zero_bcs\": {\"bcs_mean\": 0, \"correct_pct\": 85.73, \"wrong_type_pct\": 0, \"intra_sub_pct\": 0, \"missed_pct\": 14.27}, \"low_bcs\": {\"bcs_mean\": 0.565, \"correct_pct\": 85.42, \"wrong_type_pct\": 4.17, \"intra_sub_pct\": 4.17, \"missed_pct\": 10.42}, \"medium_bcs\": {\"bcs_mean\": 0.729, \"correct_pct\": 75.7, \"wrong_type_pct\": 13, \"intra_sub_pct\": 13, \"missed_pct\": 11.3}, \"high_bcs\": {\"bcs_mean\": 0.86, \"correct_pct\": 66.67, \"wrong_type_pct\": 20.28, \"intra_sub_pct\": 20.28, \"missed_pct\": 13.05}, \"very_high_bcs\": {\"bcs_mean\": 0.971, \"correct_pct\": 52.03, \"wrong_type_pct\": 32.25, \"intra_sub_pct\": 32.25, \"missed_pct\": 15.71}}, \"correlations\": {\"intra_sub_vs_bcs_spearman\": 0.9539, \"intra_sub_vs_bcs_p\": \"<1e-6\", \"accuracy_vs_bcs_spearman\": -0.5821, \"accuracy_vs_bcs_p\": \"<1e-6\"}, \"cross_task\": {\"ner_intra_sub_vs_bcs_rho\": 1, \"re_intra_sub_vs_bcs_rho\": 0.9539}, \"key_finding\": \"100% of type confusion in RE is intra-batch (model only predicts from schema). IntraSub vs BCS ρ=0.954 confirms NER finding. Missed rate flat (10-16%), BCS drives confusion not detection failure.\"}, \"hypothesis\": \"The error taxonomy pattern observed on NER (IntraSub scales with BCS, missed rate driven by count) replicates on FewRel RE under closed-set classification, with IntraSub as the dominant error mode since RE has no span boundary ambiguity.\"}, \"bootstrap_ci_analysis\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"fewnerd_pairwise_r\": {\"point\": 0.112, \"ci_lower\": 0.076, \"ci_upper\": 0.156, \"n\": 1953, \"note\": \"point estimate 0.112 vs old 0.156 — re-run confirmed current value\"}, \"maven_minilm_pairwise_r\": {\"point\": 0.129, \"ci_lower\": 0.104, \"ci_upper\": 0.156, \"n\": 11026}, \"fewrel_count8_delta_pp\": {\"point\": 31.2, \"ci_lower\": 17.7, \"ci_upper\": 42.7, \"n\": \"96+96\"}, \"fewrel_count16_delta_pp\": {\"point\": 31.2, \"ci_lower\": 22.9, \"ci_upper\": 39.6, \"n\": \"192+192\"}, \"fewnerd_pertype_rho\": {\"point\": -0.293, \"ci_lower\": -0.492, \"ci_upper\": -0.054, \"n\": 63}, \"confusion_ratio_count6\": {\"point\": 25.3, \"ci_lower\": 6.1, \"ci_upper\": 60.5}, \"confusion_ratio_count12\": {\"point\": 21.2, \"ci_lower\": 5.3, \"ci_upper\": 52.2}, \"key_finding\": \"All CIs exclude null (0 for correlations, 1 for ratios). All effects are directionally robust at 95% level.\"}, \"hypothesis\": \"Pair-level percentile bootstrap (B=10000) and type-level cluster bootstrap both yield confidence intervals excluding zero for the SCS-confusion correlation, confirming statistical robustness beyond naive standard errors that ignore within-type dependence.\"}, \"exp015_scs_validation\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"all_pairs\": {\"n\": 1953, \"n_nonzero\": 216, \"qwen3_spearman\": 0.1682, \"qwen3_spearman_p\": \"7.3e-14\", \"qwen3_kendall\": 0.1351, \"minilm_spearman\": 0.1439, \"minilm_spearman_p\": \"1.7e-10\", \"minilm_kendall\": 0.1152}, \"nonzero_only\": {\"n\": 216, \"qwen3_spearman\": 0.2722, \"qwen3_spearman_p\": \"5.0e-05\", \"qwen3_kendall\": 0.2001, \"minilm_spearman\": 0.306, \"minilm_spearman_p\": \"4.6e-06\", \"minilm_kendall\": 0.2276}, \"key_finding\": \"Both embeddings significantly predict confusion (all p<1e-5). Qwen3 better overall (rho=0.168), MiniLM better on nonzero pairs (rho=0.306). SCS is a valid but partial proxy — context, frequency, mention ambiguity also matter.\"}, \"hypothesis\": \"Pairwise SCS (embedding cosine similarity between type labels) positively correlates with empirical type confusion rates across all type pairs, validating SCS as a pre-hoc proxy for confusability without requiring extraction outputs.\"}, \"exp008_sdgd_v2_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"single_pass\": {\"f1\": 0.4451, \"precision\": 0.5631, \"recall\": 0.3679, \"batches\": 1, \"time_s\": 79}, \"random_batch\": {\"f1\": 0.3007, \"precision\": 0.3307, \"recall\": 0.2758, \"batches\": 8, \"time_s\": 494}, \"sdgd_zero\": {\"f1\": 0.2407, \"precision\": 0.3244, \"recall\": 0.1913, \"batches\": 4, \"time_s\": 261}, \"per_type\": \"killed before completion (3/4 modes done, Director approved kill)\", \"vs_v1\": \"confidence-gated merge did not improve over union merge. sdgd_zero 0.241 vs v1 0.251, random_batch 0.301 vs v1 0.320\", \"key_finding\": \"SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental rethink.\"}, \"hypothesis\": \"The v2 prompt's reduced over-prediction mitigates merge amplification in multi-pass SDGD decomposition, recovering net F1 above single-pass baseline where v1 failed due to excessive false positives per pass.\"}, \"exp008_sdgd_zero_fewnerd_r2\": {\"status\": \"DONE\", \"metrics\": {\"single_pass\": {\"f1\": 0.4451, \"precision\": 0.5631, \"recall\": 0.3679, \"batches\": 1, \"time_s\": 77.3}, \"sdgd_zero\": {\"f1\": 0.2514, \"precision\": 0.2096, \"recall\": 0.3141, \"batches\": 8, \"time_s\": 408.7}, \"random_batch\": {\"f1\": 0.3197, \"precision\": 0.2491, \"recall\": 0.4462, \"batches\": 8, \"time_s\": 476.1}, \"per_type\": {\"f1\": 0.2915, \"precision\": 0.194, \"recall\": 0.5856, \"batches\": 66, \"time_s\": 2532.2}, \"key_finding\": \"All decomposition modes F1 < single_pass. Decomposition boosts recall but kills precision (merge amplification). sdgd_zero worst F1, even below random_batch.\"}, \"conclusion\": \"negative\", \"hypothesis\": \"Partitioning confusable types into separate batches via graph coloring reduces intra-batch substitution errors sufficiently to offset the precision loss from multi-pass union merge, yielding higher net F1 than single-pass extraction on NER.\"}, \"exp007_error_taxonomy\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"exp1_random\": {\"bcs_zero\": {\"n_fp\": 6172, \"intra_sub_pct\": 0, \"extra_sub_pct\": 90.3, \"intra_sub_per_100_gold\": 0}, \"bcs_low\": {\"n_fp\": 2231, \"intra_sub_pct\": 1.6, \"extra_sub_pct\": 89.9, \"intra_sub_per_100_gold\": 3.4}, \"bcs_medium\": {\"n_fp\": 3843, \"intra_sub_pct\": 10.6, \"extra_sub_pct\": 78.1, \"intra_sub_per_100_gold\": 6.47}, \"bcs_high\": {\"n_fp\": 6188, \"intra_sub_pct\": 49.4, \"extra_sub_pct\": 30.8, \"intra_sub_per_100_gold\": 12.93}}, \"correlation\": {\"intra_sub_vs_bcs_spearman_rho\": 1, \"intra_sub_vs_bcs_p\": \"<0.001\", \"chi_square\": 6952, \"chi_square_p\": \"~0\"}, \"exp2_controlled\": {\"trend\": \"IntraSub 3.2% -> 7.3% -> 8.6% (rho=1.0, p<0.001)\"}, \"key_finding\": \"BCS>=0.95: 49.4% FP are intra-batch type confusion (13/100 gold). Hallucination+boundary <3%. LLM main error mode is type confusion, not hallucination.\"}, \"hypothesis\": \"Intra-batch type substitution errors scale monotonically with BCS while missed-entity rates are driven primarily by count, establishing mechanistically distinct error channels that decompose total degradation into confusability-driven and capacity-driven components.\"}, \"exp004_maven_bcs\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"exp1_count_curve\": {\"count_1\": {\"n_batches\": 64, \"exact_f1\": 0.009, \"relaxed_f1\": 0.106, \"bcs\": 0}, \"count_6\": {\"n_batches\": 5, \"exact_f1\": 0.003, \"relaxed_f1\": 0.103, \"bcs\": 0.892}, \"count_12\": {\"n_batches\": 5, \"exact_f1\": 0.008, \"relaxed_f1\": 0.146, \"bcs\": 0.921}, \"count_22\": {\"n_batches\": 5, \"exact_f1\": 0.013, \"relaxed_f1\": 0.185, \"bcs\": 0.933}, \"count_44\": {\"n_batches\": 5, \"exact_f1\": 0.018, \"relaxed_f1\": 0.247, \"bcs\": 0.967}, \"count_64\": {\"n_batches\": 5, \"exact_f1\": 0.013, \"relaxed_f1\": 0.245, \"bcs\": 0.973}}, \"exp2_bcs_controlled\": {\"count_6_high_bcs\": {\"exact_f1\": 0.0354, \"relaxed_f1\": 0.211, \"bcs\": 0.9447}, \"count_6_low_bcs\": {\"exact_f1\": 0.0068, \"relaxed_f1\": 0.089, \"bcs\": 0.8709}, \"count_12_high_bcs\": {\"exact_f1\": 0.0151, \"relaxed_f1\": 0.1568, \"bcs\": 0.9447}, \"count_12_low_bcs\": {\"exact_f1\": 0.0068, \"relaxed_f1\": 0.105, \"bcs\": 0.9148}}, \"key_finding\": \"MAVEN batch-level: high_bcs relaxed_F1 2.4x vs low_bcs (count_6). Direction same as Few-NERD batch-level (positive). Pairwise + per-type analysis needed to control frequency confound.\", \"note\": \"exact_F1 very low (0.003-0.035), relaxed_F1 usable (0.089-0.247). Event trigger boundary matching is fuzzy. A re-run (500 samples) is still in progress in artifacts/exp004/.\"}, \"hypothesis\": \"Schema-induced confusability degradation (higher BCS → lower F1) replicates on MAVEN event detection, confirming the channel generalizes beyond NER/RE to event extraction tasks with semantically dense type inventories.\"}, \"exp003a_prompt_v2_rerun\": {\"status\": \"DONE\", \"metrics\": {\"eval_mode\": \"text_match\", \"exp1_text_match\": {\"count_1\": {\"f1\": 0.323, \"precision\": 0.216, \"recall\": 0.641, \"pred_gold_ratio\": 2.97, \"n_batches\": 64}, \"count_2\": {\"f1\": 0.273, \"precision\": 0.18, \"recall\": 0.56, \"pred_gold_ratio\": 3.11, \"n_batches\": 5}, \"count_6\": {\"f1\": 0.306, \"precision\": 0.226, \"recall\": 0.475, \"pred_gold_ratio\": 2.1, \"n_batches\": 5}, \"count_12\": {\"f1\": 0.347, \"precision\": 0.367, \"recall\": 0.329, \"pred_gold_ratio\": 0.9, \"n_batches\": 5}, \"count_22\": {\"f1\": 0.299, \"precision\": 0.339, \"recall\": 0.267, \"pred_gold_ratio\": 0.79, \"n_batches\": 5}, \"count_44\": {\"f1\": 0.445, \"precision\": 0.506, \"recall\": 0.396, \"pred_gold_ratio\": 0.78, \"n_batches\": 5}, \"count_64\": {\"f1\": 0.414, \"precision\": 0.648, \"recall\": 0.304, \"pred_gold_ratio\": 0.47, \"n_batches\": 5}}, \"exp2_text_match\": {\"count_6\": {\"f1\": 0.32, \"precision\": 0.26, \"recall\": 0.416, \"pred_gold_ratio\": 1.6, \"n_batches\": 27}, \"count_12\": {\"f1\": 0.306, \"precision\": 0.291, \"recall\": 0.323, \"pred_gold_ratio\": 1.11, \"n_batches\": 27}}, \"vs_exp001_delta\": {\"count_1\": {\"f1_delta\": \"+0.139 (+76%)\", \"precision_delta\": \"+0.111 (+106%)\", \"recall_delta\": \"-0.079 (-11%)\", \"overpred_fix\": \"6.85→2.97\"}, \"count_6\": {\"f1_delta\": \"+0.151 (+97%)\", \"precision_delta\": \"+0.138 (+157%)\", \"recall_delta\": \"-0.145 (-23%)\"}, \"count_12\": {\"f1_delta\": \"+0.101 (+41%)\", \"precision_delta\": \"+0.207 (+129%)\", \"recall_delta\": \"-0.210 (-39%)\"}, \"count_44\": {\"f1_delta\": \"-0.028 (-6%)\", \"precision_delta\": \"+0.092 (+22%)\", \"recall_delta\": \"-0.155 (-28%)\"}, \"count_64\": {\"f1_delta\": \"-0.049 (-11%)\", \"precision_delta\": \"+0.128 (+25%)\", \"recall_delta\": \"-0.114 (-27%)\"}}, \"key_finding\": \"V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1). But over-corrected at high counts: under-prediction (pred/gold<1) caused recall drops of 27-39%, slightly lowering F1 at count_22-64.\"}, \"conclusion\": \"success\", \"hypothesis\": \"A restructured prompt (v2: definition-enriched, explicit output constraints) modulates the magnitude of count-driven and BCS-driven degradation but does not eliminate either channel, confirming schema configuration as the dominant factor.\"}, \"exp002_confusability_controlled\": {\"status\": \"DONE\", \"metrics\": {\"data_source\": \"exp2_reeval_results.json (text_match, CLEAN)\", \"primary_recall_vs_bcs\": {\"count_6\": {\"r\": 0.2754, \"p\": 0.1644, \"n\": 27, \"verdict\": \"FAIL\"}, \"count_12\": {\"r\": 0.2219, \"p\": 0.266, \"n\": 27, \"verdict\": \"FAIL\"}, \"partial\": {\"r\": 0.2522, \"p\": 0.0658, \"n\": 54, \"verdict\": \"FAIL\"}}, \"secondary_f1_vs_bcs\": {\"count_6\": {\"r\": 0.1754, \"p\": 0.3814, \"n\": 27, \"verdict\": \"FAIL\"}, \"count_12\": {\"r\": 0.5012, \"p\": 0.0077, \"n\": 27, \"verdict\": \"PASS\"}, \"partial\": {\"r\": 0.3025, \"p\": 0.0262, \"n\": 54, \"verdict\": \"PASS\"}}, \"mechanistic_confusion_rate\": {\"random_batches\": {\"count_6_high\": 0.0157, \"count_6_low\": 0.0088, \"ratio_6\": 1.7, \"count_12_high\": 0.0304, \"count_12_low\": 0.0131, \"ratio_12\": 2.4}, \"extreme_batches\": {\"count_6_high\": 0.0728, \"count_6_low\": 0.0014, \"ratio_6\": 27.5, \"count_12_high\": 0.048, \"count_12_low\": 0.0061, \"ratio_12\": 9.9}, \"verdict\": \"PASS\"}, \"pairwise_confusion_analysis\": {\"all\": {\"n_pairs\": 1953, \"pearson_r\": 0.156, \"pearson_p\": 4.6e-12, \"spearman_rho\": 0.16, \"spearman_p\": 1.3e-12}, \"count_6\": {\"n_pairs\": 1770, \"pearson_r\": 0.078, \"pearson_p\": 0.001}, \"count_12\": {\"n_pairs\": 1953, \"pearson_r\": 0.147, \"pearson_p\": 6.7e-11}, \"nonzero_only\": {\"all_spearman_rho\": 0.254, \"all_spearman_p\": 1.1e-06, \"count_12_pearson_r\": 0.212, \"count_12_p\": 0.00034}, \"top_confused_pair\": \"person-other <-> person-politician (BCS=0.934, confusion=156)\"}, \"per_type_analysis\": {\"n_types\": 63, \"filter\": \"freq>=5\", \"micro_f1_vs_bcs\": {\"pearson_r\": -0.1828, \"pearson_p\": 0.1516, \"spearman_rho\": -0.2927, \"spearman_p\": 0.0199, \"partial_r_ctrl_logfreq\": -0.1998, \"partial_p\": 0.1163}, \"mean_f1_vs_bcs\": {\"pearson_r\": -0.1374, \"pearson_p\": 0.283, \"spearman_rho\": -0.2412, \"spearman_p\": 0.0568, \"partial_r_ctrl_logfreq\": -0.1428, \"partial_p\": 0.2641}, \"quartile_comparison\": {\"low_bcs_cutoff\": 0.798, \"high_bcs_cutoff\": 0.827, \"low_bcs_f1\": 0.3098, \"high_bcs_f1\": 0.2275, \"delta_f1\": -0.0823, \"low_bcs_freq\": 2134, \"high_bcs_freq\": 2049}, \"confound_check\": {\"bcs_vs_logfreq_r\": 0.042, \"bcs_vs_logfreq_p\": 0.74, \"logfreq_vs_f1_r\": 0.25, \"logfreq_vs_f1_p\": 0.048}, \"verdict\": \"Direction supports hypothesis. Spearman significant (p=0.02). Frequency confound absent at type level (r=0.04).\"}, \"overall_verdict\": \"PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE STRONG PASS, PER-TYPE DIRECTIONAL PASS\"}, \"conclusion\": \"success\", \"hypothesis\": \"At fixed type count, batches with higher mean pairwise embedding similarity (BCS) produce lower NER recall because semantically confusable types compete for the same entity mentions, increasing substitution errors.\"}, \"fewrel_pilot\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"embedding\": \"all-MiniLM-L6-v2\", \"n_batches\": 15, \"n_predictions\": 374, \"count_4\": {\"low_bcs_acc\": 0.917, \"high_bcs_acc\": 0.708, \"delta_pp\": -20.9, \"low_bcs\": 0.42, \"high_bcs\": 0.97}, \"count_8\": {\"low_bcs_acc\": 1, \"high_bcs_acc\": 0.5, \"delta_pp\": -50, \"low_bcs\": 0.47, \"high_bcs\": 0.97}, \"count_16\": {\"low_bcs_acc\": 0.917, \"high_bcs_acc\": 0.431, \"delta_pp\": -48.6, \"low_bcs\": 0.57, \"high_bcs\": 0.97}, \"key_finding\": \"BCS-accuracy strong negative: high-BCS batches 43-71% vs low-BCS 92-100%. Effect increases with count. Cross-task (NER→RE) replication of confusability hypothesis.\"}, \"hypothesis\": \"Pairwise embedding similarity (SCS) between relation types predicts extraction accuracy degradation: high-BCS batches yield lower accuracy than low-BCS batches at matched count, establishing the confusability channel on RE.\"}, \"exp-004\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"n_event_types\": 168, \"n_pairs\": 14028, \"scs_mean\": 0.2161, \"scs_std\": 0.103, \"scs_max\": 0.8368, \"scs_median\": 0.2121, \"scs_q90\": 0.3457, \"scs_q95\": 0.3892, \"pairs_above_0.5\": 119, \"pct_above_0.5\": 0.85, \"train_docs\": 2913, \"train_mentions\": 77993, \"valid_docs\": 710, \"valid_mentions\": 18904}, \"hypothesis\": \"MAVEN's 168 FrameNet-derived event types exhibit higher mean SCS than Few-NERD's cross-domain entity types due to same-domain semantic clustering, enabling a cross-task replication test of confusability effects.\"}, \"exp001_count_baseline\": {\"status\": \"DONE\", \"metrics\": {\"diagnosis\": \"char offset 96.5% fabricated by model\", \"text_match_reeval\": {\"count_1\": {\"f1\": 0.184, \"precision\": 0.105, \"recall\": 0.72, \"pred_gold_ratio\": 6.85}, \"count_2\": {\"f1\": 0.123, \"precision\": 0.068, \"recall\": 0.698, \"pred_gold_ratio\": 10.33}, \"count_6\": {\"f1\": 0.155, \"precision\": 0.088, \"recall\": 0.62, \"pred_gold_ratio\": 7.02}, \"count_12\": {\"f1\": 0.246, \"precision\": 0.16, \"recall\": 0.539, \"pred_gold_ratio\": 3.38}, \"count_22\": {\"f1\": 0.322, \"precision\": 0.232, \"recall\": 0.527, \"pred_gold_ratio\": 2.27}, \"count_44\": {\"f1\": 0.473, \"precision\": 0.414, \"recall\": 0.551, \"pred_gold_ratio\": 1.33}, \"count_64\": {\"f1\": 0.463, \"precision\": 0.52, \"recall\": 0.418, \"pred_gold_ratio\": 0.8}}, \"key_finding\": \"recall monotonically decreases (0.72→0.42), precision monotonically increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at count_44\", \"wrong_type_trend\": \"type confusion increases with count: 0→2434, supports confusability hypothesis\", \"spurious_dominant\": \"spurious FPs (text in source but not entity) dominate at low count, not hallucination\", \"conclusion_text_match\": \"F1 curve inversion caused by over-prediction confound, NOT absence of confusability effect. Recall curve + type confusion pattern support hypothesis.\"}, \"conclusion\": \"success\", \"hypothesis\": \"Increasing the number of schema types in a zero-shot LLM extraction prompt degrades per-type recall due to bounded attention capacity and instruction-following limits, producing a monotonic count-performance curve on Few-NERD NER.\"}, \"exp_fewrel_16rel_bootstrap\": {\"status\": \"DONE\", \"hypothesis\": \"FewRel 16-type pool, 100 random 8-type batches, bootstrap CI for BCS effect (Δ_BCS). 填 tab:bcs_controlled 16-rel 行的 CI，并与 80-rel 计算 amplification ratio 正式 CI。D033 已批准。\", \"metrics\": {\"n_batches\": 100, \"pool_size\": 16, \"batch_size\": 8, \"bcs_range\": [0.6532, 0.9002], \"quartile_delta\": {\"Q4_minus_Q1_pp\": -5.31, \"ci_95_lower\": -9.45, \"ci_95_upper\": -4.49, \"note\": \"CI values from pre-D038 bootstrap, may need re-verification with MEAN-based BCS\"}, \"pearson_r_bcs_acc\": -0.467, \"regression_slope\": {\"slope\": -0.509, \"ci_95_lower\": -0.556, \"ci_95_upper\": -0.349, \"r_squared\": 0.218, \"p_value\": 1.01e-12, \"interpretation\": \"per +0.1 BCS → -5.09pp accuracy\", \"note\": \"CI from pre-D038 bootstrap\"}, \"amplification_ratio\": {\"quartile_16_vs_80\": 4.2, \"ci_95_lower\": 3.3, \"ci_95_upper\": 6.95}, \"key_finding\": \"16-rel pool BCS effect (MEAN-based, D038): Δ(Q4-Q1)=-5.31pp, r=-0.467. Regression slope=-0.509. Bootstrap 1000 resamples. [D038 MEAN correction applied, old values: r=-0.637/Δ=-7.42pp/slope=-0.449]\"}, \"conclusion\": \"success\"}, \"exp_docred_confusability\": {\"status\": \"DONE\", \"hypothesis\": \"Schema-induced degradation (count + confusability channels) generalizes to document-level RE (DocRED, 96 relation types), strengthening cross-dataset evidence for Claims 1 and 2.\", \"conclusion\": \"success\", \"metrics\": {\"n_relation_types\": 96, \"n_eval_samples\": 1240, \"total_inferences\": 13618, \"count_curve\": {\"count_1\": 0.88, \"count_4\": 0.77, \"count_8\": 0.774, \"count_16\": 0.524, \"count_32\": 0.521, \"count_64\": 0.424, \"count_96\": 0.387}, \"bcs_effect_count16\": {\"low_bcs_acc\": 0.679, \"high_bcs_acc\": 0.447, \"gap\": 0.233, \"spearman_r\": -0.661, \"slope\": -0.713, \"slope_95ci\": [-0.909, -0.529]}, \"bcs_effect_count32\": {\"low_bcs_acc\": 0.578, \"high_bcs_acc\": 0.403, \"gap\": 0.176, \"spearman_r\": -0.509, \"slope\": -0.69, \"slope_95ci\": [-0.854, -0.519]}}}, \"exp_fewrel_v2_bcs_controlled\": {\"status\": \"DONE\", \"hypothesis\": \"验证 Channel 2 (BCS→type confusion) 在 v2 prompt 下方向一致。FewRel 80-rel, count=8, low-BCS 5 batches + high-BCS 5 batches, Qwen3-32B-FP8, v2 prompt。D037 Round 2 审稿 C1b。\", \"conclusion\": \"success\", \"metrics\": {\"low_bcs_mean_acc\": 0.8042, \"high_bcs_mean_acc\": 0.725, \"delta_low_minus_high_pp\": 7.92, \"bootstrap_ci_95_lower_pp\": -5.21, \"bootstrap_ci_95_upper_pp\": 21.46, \"n_bootstrap\": 10000, \"n_batches_per_group\": 5, \"samples_per_batch\": 96, \"total_inferences\": 960}}, \"exp_fewrel_16rel_100batch\": {\"status\": \"DONE\", \"hypothesis\": \"D033: 16-rel pool 100 random batches (count_8) + bootstrap CI，填补 tab:bcs_controlled 16-rel 空白，为 3.4× amplification ratio 提供双端 CI 支撑。\", \"conclusion\": \"killed\"}, \"exp012_llama_fewrel_ch2\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct 在 FewRel 80-rel RE 任务上验证 Channel 2 (BCS-controlled confusability effect)。跨模型家族(Qwen→LLaMA) + 跨规模(32B→8B) + 跨任务(NER→RE) 三重泛化验证。exp2 design: count 8/16 × low/high BCS × 27 batches。\", \"conclusion\": \"success\", \"metrics\": {\"exp2_bcs_controlled\": {\"count_8\": {\"low_bcs_acc\": 0.7812, \"high_bcs_acc\": 0.5104, \"delta_pp\": -27.1}, \"count_16\": {\"low_bcs_acc\": 0.7552, \"high_bcs_acc\": 0.5156, \"delta_pp\": -24}}, \"overall_correlation\": {\"n_batches\": 54, \"pearson_r\": -0.39, \"pearson_p\": 0.004, \"spearman_rho\": -0.43, \"spearman_p\": 0.001}, \"cross_model_comparison\": {\"llama_delta_pp\": -27.1, \"qwen3_delta_pp\": -31.2, \"ratio\": 0.87, \"note\": \"LLaMA effect = 87% of Qwen3, direction and magnitude consistent\"}, \"no_floor_effect\": true, \"mean_accuracy\": 0.77, \"accuracy_range\": \"0.41-0.98\", \"key_finding\": \"BCS confusability effect cross-model replicated: LLaMA Δ=-27.1pp (87% of Qwen3 -31.2pp). Pearson r=-0.39 (p=0.004), Spearman ρ=-0.43 (p=0.001). No floor effect.\"}}, \"exp012_llama_8b_r2_exp2\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct exp2 重跑：BCS-controlled factorial (count=6/12, low/high BCS)，验证 confusability effect 跨模型泛化。Parent exp012_llama_8b_r2 的 exp1 count curve 已完成。\", \"conclusion\": \"negative\"}, \"exp012_llama_8b_r2\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA-3.1-8B-Instruct 复现 confusability-driven type confusion（chat template 修复版）。验证 confusability effect 跨模型家族（Qwen→LLaMA）+ 跨规模（32B→8B）泛化。\", \"conclusion\": \"success\", \"metrics\": {\"exp1_llama_recall_count1\": 0.702, \"exp1_llama_recall_count64\": 0.273, \"exp1_recall_decline_pp\": -42.9, \"exp1_per_batch_recall_corr_vs_qwen\": 0.7249, \"exp1_llama_text_match_f1_range\": \"0.06-0.36\", \"exp1_exact_f1\": 0, \"exp1_note\": \"exact/relaxed F1=0 due to missing char offsets, text_match is correct metric\"}}, \"exp006_interaction_2x2\": {\"status\": \"DONE\", \"hypothesis\": \"Count × Confusability 交互效应：{low count, high count} × {low BCS, high BCS} 2×2 设计，测试 count 和 confusability 对 accuracy 的影响是 additive 还是 multiplicative。若 multiplicative，高 count + 高 BCS 组的 degradation 应超过两个主效应之和。\", \"metrics\": {\"cell_means_f1\": {\"low_count_low_bcs\": 0.324, \"low_count_high_bcs\": 0.313, \"high_count_low_bcs\": 0.325, \"high_count_high_bcs\": 0.277}, \"main_effects\": {\"count\": -0.018, \"bcs\": -0.029}, \"interaction\": {\"estimate\": -0.036, \"z\": -0.667, \"p\": 0.505, \"bcs_effect_at_low_count\": -0.011, \"bcs_effect_at_high_count\": -0.048}, \"verdict\": \"交互方向符合 multiplicative 假设但统计不显著 (p=0.505)，未检测到显著交互效应\"}, \"conclusion\": \"negative\"}, \"exp012_llama_awq\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp012_llama_8b_r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_8b\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_fewrel_40rel_r3\": {\"status\": \"DONE\", \"hypothesis\": \"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\", \"conclusion\": \"failed\"}, \"exp_fewrel_40rel_r2\": {\"status\": \"DONE\", \"hypothesis\": \"FewRel 40-rel 中间点 scaling curve: 验证 count↑→accuracy↓ 在 40-rel 规模下的 degradation 幅度，补全 16-rel 到 80-rel 之间的 scaling 趋势\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r4\": {\"status\": \"DONE\", \"hypothesis\": \"LLaMA model replicates confusability-driven type confusion pattern observed with Qwen, validating model-independence of the phenomenon\", \"conclusion\": \"failed\"}, \"exp012_llama_8b_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_fewrel_40rel\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd_r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp012_llama_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp008_sdgd_zero_fewnerd\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}}, \"count\": 50, \"total\": 50, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1891}}"
    }
  },
  "sourceToolAssistantUUID": "7591f5ce-9028-4760-8445-7aea962eacfd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "leafUuid": "63dd2c1c-07c8-4c64-9e86-e0380da84200",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Update experiment_plan.yaml with registry_id mappings",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---

### Assistant

_source line 47 · 2026-05-18T21:38:13.020Z_

<details><summary>Logged reasoning block</summary>

```text
All registry IDs confirmed. Now let me compare exp007_error_taxonomy vs exp016_fewrel_error_taxonomy:

**exp007_error_taxonomy** (NER - Few-NERD):
- conclusion: success
- metrics: FP classification across BCS bins, IntraSub vs BCS spearman rho = 1.0, chi_square = 6952, covers random and controlled experiments
- Key finding: "BCS>=0.95: 49.4% FP are intra-batch type confusion (13/100 gold). Hallucination+boundary <3%. LLM main error mode is type confusion, not hallucination."


- **exp016_fewrel_error_taxonomy** (RE - FewRel) shows similar patterns with 100% of type confusion being intra-batch, a spearman correlation of 0.954 between IntraSub and BCS that validates the NER finding, and a flat missed rate across BCS bins indicating that confusion rather than detection failure drives performance. The RE experiment uses five BCS bins for more granular analysis compared to the NER taxonomy.

- **exp007_error_taxonomy** is the direct NER implementation mapping to the original exp-007 description, since it depends on exp-002 (Few-NERD confusability controlled). This makes it the more appropriate choice for the task.
- **exp016_fewrel_error_taxonomy** offers a cross-task extension with 5 BCS bins and cleaner structure, including correlation stats and cross-task comparison data that exp007 lacks.

Given that exp-007 is specifically about Few-NERD NER with mechanistic evidence, exp007_error_taxonomy is the direct match, though exp016 provides valuable complementary insights with its more complete binning and cleaner presentation of the intra-substitution trends. I'm weighing whether to use exp007_error_taxonomy since it directly matches the Few-NERD task, or exp016_fewrel_error_taxonomy which has more comprehensive metrics with 5 bins and cross-task validation. The user asked for the more complete version, but using FewRel's taxonomy for a Few-NERD experiment feels semantically off. Let me go with exp007 as the primary choice since it's the correct task match, even though exp016 has richer data. I'm mapping out the registry IDs for the remaining experiments—exp-013 has two options to choose from, and exp-015 uses the validation approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63dd2c1c-07c8-4c64-9e86-e0380da84200",
  "isSidechain": false,
  "requestId": "req_011CbAkpoudH45Jo5rj9hEpx",
  "type": "assistant",
  "uuid": "2cce57fd-1102-456e-94b5-646664b299fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeYathPbiKF6vYNeupbM5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19054,
      "cache_read_input_tokens": 35557,
      "output_tokens": 3197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19054,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3197,
          "cache_read_input_tokens": 35557,
          "cache_creation_input_tokens": 19054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19054
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-18T21:38:14.672Z_

所有 registry ID 确认存在。比较 exp-007 的两个候选：

- **exp007_error_taxonomy**: 4 BCS bins, NER (Few-NERD), rho=1.0, chi_square=6952
- **exp016_fewrel_error_taxonomy**: 5 BCS bins, RE (FewRel), rho=0.954, cross-task comparison, 更详细的 per-bin breakdown

exp016 更完整（5 bins + cross-task），选它。开始编辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cce57fd-1102-456e-94b5-646664b299fb",
  "isSidechain": false,
  "requestId": "req_011CbAkpoudH45Jo5rj9hEpx",
  "type": "assistant",
  "uuid": "d31f14da-20f6-498a-a895-287d4d6887bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeYathPbiKF6vYNeupbM5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19054,
      "cache_read_input_tokens": 35557,
      "output_tokens": 3197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19054,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3197,
          "cache_read_input_tokens": 35557,
          "cache_creation_input_tokens": 19054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19054
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-18T21:38:20.136Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01LqA2h5TNcDqpwCTnTahFrg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
  "old_string": "- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a",
  "new_string": "- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n  registry_id: exp_docred_confusability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d31f14da-20f6-498a-a895-287d4d6887bb",
  "isSidechain": false,
  "requestId": "req_011CbAkpoudH45Jo5rj9hEpx",
  "type": "assistant",
  "uuid": "f24a56f1-70c0-4c22-ae08-5419f552edb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeYathPbiKF6vYNeupbM5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19054,
      "cache_read_input_tokens": 35557,
      "output_tokens": 3197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19054,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3197,
          "cache_read_input_tokens": 35557,
          "cache_creation_input_tokens": 19054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19054
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-18T21:38:20.167Z_

<details><summary>↩ Tool result · `toolu_01LqA2h5TNcDqpwCTnTahFrg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f24a56f1-70c0-4c22-ae08-5419f552edb5",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "77b6a6fc-154d-4a27-a045-e1008c068558",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
    "oldString": "- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a",
    "newString": "- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n  registry_id: exp_docred_confusability",
    "originalFile": "experiments:\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_8b_r3\n- id: exp-016\n  claim:\n  - 1\n  - 2\n  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel\n    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.\n    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp_fewrel_formal\n  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full\n    count curve after current run completes.\n- id: exp-008\n  claim:\n  - 3\n  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition\n    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-003a\n  registry_id: exp008_sdgd_v2_fewnerd\n  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass\n    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'\n- id: exp-009\n  claim:\n  - 3\n  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on\n    168 event types. Compare vs single-pass + random batching. Cross-task validation\n    of SDGD framework (NER→ED).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-004\n  - exp-008\n- id: exp-010\n  claim:\n  - 3\n  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration\n    examples (no gradients). Compare vs SDGD-zero.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-008\n- id: exp-011\n  claim:\n  - 3\n  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168\n    event types. Full comparison table.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-009\n  - exp-010\n- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n- id: exp-014\n  claim:\n  - 3\n  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper\n    bound on decomposition benefit. Reveals latency vs quality tradeoff.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n",
    "structuredPatch": [
      {
        "oldStart": 64,
        "oldLines": 6,
        "newStart": 64,
        "newLines": 7,
        "lines": [
          "   gpu_budget_hours: 5",
          "   deps:",
          "   - exp-003a",
          "+  registry_id: exp_docred_confusability",
          " - id: exp-006",
          "   claim:",
          "   - 2"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f24a56f1-70c0-4c22-ae08-5419f552edb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-18T21:38:22.965Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01BAf1dGZafcDhtYAGRCMJBJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
  "old_string": "- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a",
  "new_string": "- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n  registry_id: exp006_interaction_2x2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77b6a6fc-154d-4a27-a045-e1008c068558",
  "isSidechain": false,
  "requestId": "req_011CbAkpoudH45Jo5rj9hEpx",
  "type": "assistant",
  "uuid": "1f321785-4209-43e7-9af4-34f509ed6c8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeYathPbiKF6vYNeupbM5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19054,
      "cache_read_input_tokens": 35557,
      "output_tokens": 3197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19054,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3197,
          "cache_read_input_tokens": 35557,
          "cache_creation_input_tokens": 19054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19054
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T21:38:22.981Z_

<details><summary>↩ Tool result · `toolu_01BAf1dGZafcDhtYAGRCMJBJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f321785-4209-43e7-9af4-34f509ed6c8d",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "71bf0305-3897-40ae-9653-d470bf9ae7ca",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
    "oldString": "- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a",
    "newString": "- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n  registry_id: exp006_interaction_2x2",
    "originalFile": "experiments:\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n  registry_id: exp_docred_confusability\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_8b_r3\n- id: exp-016\n  claim:\n  - 1\n  - 2\n  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel\n    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.\n    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp_fewrel_formal\n  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full\n    count curve after current run completes.\n- id: exp-008\n  claim:\n  - 3\n  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition\n    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-003a\n  registry_id: exp008_sdgd_v2_fewnerd\n  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass\n    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'\n- id: exp-009\n  claim:\n  - 3\n  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on\n    168 event types. Compare vs single-pass + random batching. Cross-task validation\n    of SDGD framework (NER→ED).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-004\n  - exp-008\n- id: exp-010\n  claim:\n  - 3\n  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration\n    examples (no gradients). Compare vs SDGD-zero.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-008\n- id: exp-011\n  claim:\n  - 3\n  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168\n    event types. Full comparison table.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-009\n  - exp-010\n- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n- id: exp-014\n  claim:\n  - 3\n  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper\n    bound on decomposition benefit. Reveals latency vs quality tradeoff.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n",
    "structuredPatch": [
      {
        "oldStart": 74,
        "oldLines": 6,
        "newStart": 74,
        "newLines": 7,
        "lines": [
          "   gpu_budget_hours: 2",
          "   deps:",
          "   - exp-003a",
          "+  registry_id: exp006_interaction_2x2",
          " - id: exp-007",
          "   claim:",
          "   - 2"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "1f321785-4209-43e7-9af4-34f509ed6c8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-18T21:38:27.144Z_

<details open><summary>🔧 Tool call — Edit · `toolu_0133dWhCYQAvME78pyZm7vwg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
  "old_string": "- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.",
  "new_string": "- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  registry_id: exp016_fewrel_error_taxonomy\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71bf0305-3897-40ae-9653-d470bf9ae7ca",
  "isSidechain": false,
  "requestId": "req_011CbAkpoudH45Jo5rj9hEpx",
  "type": "assistant",
  "uuid": "eb3bbf75-70a0-4795-a903-bb063ec5a498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeYathPbiKF6vYNeupbM5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19054,
      "cache_read_input_tokens": 35557,
      "output_tokens": 3197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19054,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3197,
          "cache_read_input_tokens": 35557,
          "cache_creation_input_tokens": 19054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19054
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-18T21:38:27.162Z_

<details><summary>↩ Tool result · `toolu_0133dWhCYQAvME78pyZm7vwg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb3bbf75-70a0-4795-a903-bb063ec5a498",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "8ad4747e-6fff-47ee-b85e-fd2dce2acd96",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
    "oldString": "- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.",
    "newString": "- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  registry_id: exp016_fewrel_error_taxonomy\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.",
    "originalFile": "experiments:\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n  registry_id: exp_docred_confusability\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n  registry_id: exp006_interaction_2x2\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_8b_r3\n- id: exp-016\n  claim:\n  - 1\n  - 2\n  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel\n    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.\n    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp_fewrel_formal\n  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full\n    count curve after current run completes.\n- id: exp-008\n  claim:\n  - 3\n  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition\n    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-003a\n  registry_id: exp008_sdgd_v2_fewnerd\n  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass\n    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'\n- id: exp-009\n  claim:\n  - 3\n  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on\n    168 event types. Compare vs single-pass + random batching. Cross-task validation\n    of SDGD framework (NER→ED).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-004\n  - exp-008\n- id: exp-010\n  claim:\n  - 3\n  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration\n    examples (no gradients). Compare vs SDGD-zero.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-008\n- id: exp-011\n  claim:\n  - 3\n  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168\n    event types. Full comparison table.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-009\n  - exp-010\n- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n- id: exp-014\n  claim:\n  - 3\n  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper\n    bound on decomposition benefit. Reveals latency vs quality tradeoff.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n",
    "structuredPatch": [
      {
        "oldStart": 85,
        "oldLines": 6,
        "newStart": 85,
        "newLines": 7,
        "lines": [
          "   gpu_budget_hours: 1",
          "   deps:",
          "   - exp-002",
          "+  registry_id: exp016_fewrel_error_taxonomy",
          "   status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic",
          "     BCS-binned analysis.",
          " - id: exp-012"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "eb3bbf75-70a0-4795-a903-bb063ec5a498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T21:38:31.626Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01NkVZGQuAVFTHRbt3HptuAZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
  "old_string": "- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008",
  "new_string": "- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  registry_id:\n  - exp008_sdgd_v2_fewnerd\n  - exp_confusability_batch_composition\n  status_note: Covered by SDGD v2 (negative) + confusability-aware batch composition\n    (positive, +1.44pp directional)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ad4747e-6fff-47ee-b85e-fd2dce2acd96",
  "isSidechain": false,
  "requestId": "req_011CbAkpoudH45Jo5rj9hEpx",
  "type": "assistant",
  "uuid": "7e047498-f2a6-46be-a725-de3fdcc442e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeYathPbiKF6vYNeupbM5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19054,
      "cache_read_input_tokens": 35557,
      "output_tokens": 3197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19054,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3197,
          "cache_read_input_tokens": 35557,
          "cache_creation_input_tokens": 19054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19054
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-18T21:38:31.636Z_

<details><summary>↩ Tool result · `toolu_01NkVZGQuAVFTHRbt3HptuAZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e047498-f2a6-46be-a725-de3fdcc442e3",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "8c24a845-62bf-4233-aeb6-0fc3528e5d04",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
    "oldString": "- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008",
    "newString": "- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  registry_id:\n  - exp008_sdgd_v2_fewnerd\n  - exp_confusability_batch_composition\n  status_note: Covered by SDGD v2 (negative) + confusability-aware batch composition\n    (positive, +1.44pp directional).",
    "originalFile": "experiments:\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n  registry_id: exp_docred_confusability\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n  registry_id: exp006_interaction_2x2\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  registry_id: exp016_fewrel_error_taxonomy\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_8b_r3\n- id: exp-016\n  claim:\n  - 1\n  - 2\n  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel\n    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.\n    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp_fewrel_formal\n  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full\n    count curve after current run completes.\n- id: exp-008\n  claim:\n  - 3\n  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition\n    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-003a\n  registry_id: exp008_sdgd_v2_fewnerd\n  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass\n    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'\n- id: exp-009\n  claim:\n  - 3\n  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on\n    168 event types. Compare vs single-pass + random batching. Cross-task validation\n    of SDGD framework (NER→ED).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-004\n  - exp-008\n- id: exp-010\n  claim:\n  - 3\n  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration\n    examples (no gradients). Compare vs SDGD-zero.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-008\n- id: exp-011\n  claim:\n  - 3\n  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168\n    event types. Full comparison table.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-009\n  - exp-010\n- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n- id: exp-014\n  claim:\n  - 3\n  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper\n    bound on decomposition benefit. Reveals latency vs quality tradeoff.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n",
    "structuredPatch": [
      {
        "oldStart": 165,
        "oldLines": 6,
        "newStart": 165,
        "newLines": 11,
        "lines": [
          "   gpu_budget_hours: 3",
          "   deps:",
          "   - exp-008",
          "+  registry_id:",
          "+  - exp008_sdgd_v2_fewnerd",
          "+  - exp_confusability_batch_composition",
          "+  status_note: Covered by SDGD v2 (negative) + confusability-aware batch composition",
          "+    (positive, +1.44pp directional).",
          " - id: exp-014",
          "   claim:",
          "   - 3"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "7e047498-f2a6-46be-a725-de3fdcc442e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-18T21:38:34.264Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01ESNCVniuCBFHc2Y47nxLj4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
  "old_string": "- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010",
  "new_string": "- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n  registry_id: exp015_scs_validation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c24a845-62bf-4233-aeb6-0fc3528e5d04",
  "isSidechain": false,
  "requestId": "req_011CbAkpoudH45Jo5rj9hEpx",
  "type": "assistant",
  "uuid": "2e6d2dcc-4902-48ec-bcb4-5cc315d1e98a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeYathPbiKF6vYNeupbM5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19054,
      "cache_read_input_tokens": 35557,
      "output_tokens": 3197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19054,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3197,
          "cache_read_input_tokens": 35557,
          "cache_creation_input_tokens": 19054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19054
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T21:38:34.282Z_

<details><summary>↩ Tool result · `toolu_01ESNCVniuCBFHc2Y47nxLj4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e6d2dcc-4902-48ec-bcb4-5cc315d1e98a",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "ce06f506-8de9-44a7-877d-b7058d62d96f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
    "oldString": "- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010",
    "newString": "- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n  registry_id: exp015_scs_validation",
    "originalFile": "experiments:\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n  registry_id: exp_docred_confusability\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n  registry_id: exp006_interaction_2x2\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  registry_id: exp016_fewrel_error_taxonomy\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_8b_r3\n- id: exp-016\n  claim:\n  - 1\n  - 2\n  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel\n    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.\n    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp_fewrel_formal\n  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full\n    count curve after current run completes.\n- id: exp-008\n  claim:\n  - 3\n  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition\n    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-003a\n  registry_id: exp008_sdgd_v2_fewnerd\n  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass\n    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'\n- id: exp-009\n  claim:\n  - 3\n  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on\n    168 event types. Compare vs single-pass + random batching. Cross-task validation\n    of SDGD framework (NER→ED).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-004\n  - exp-008\n- id: exp-010\n  claim:\n  - 3\n  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration\n    examples (no gradients). Compare vs SDGD-zero.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-008\n- id: exp-011\n  claim:\n  - 3\n  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168\n    event types. Full comparison table.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-009\n  - exp-010\n- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  registry_id:\n  - exp008_sdgd_v2_fewnerd\n  - exp_confusability_batch_composition\n  status_note: Covered by SDGD v2 (negative) + confusability-aware batch composition\n    (positive, +1.44pp directional).\n- id: exp-014\n  claim:\n  - 3\n  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper\n    bound on decomposition benefit. Reveals latency vs quality tradeoff.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n",
    "structuredPatch": [
      {
        "oldStart": 188,
        "oldLines": 3,
        "newStart": 188,
        "newLines": 4,
        "lines": [
          "   gpu_budget_hours: 1",
          "   deps:",
          "   - exp-010",
          "+  registry_id: exp015_scs_validation"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "2e6d2dcc-4902-48ec-bcb4-5cc315d1e98a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 59 · 2026-05-18T21:38:34.287Z_

```json
{
  "parentUuid": "ce06f506-8de9-44a7-877d-b7058d62d96f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7437ae9b-827e-4caa-a0ee-6ca279b68a2a",
  "timestamp": "2026-05-18T21:38:34.287Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "last-prompt",
  "leafUuid": "7437ae9b-827e-4caa-a0ee-6ca279b68a2a",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "Update experiment_plan.yaml with registry_id mappings",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---

### Assistant

_source line 62 · 2026-05-18T21:38:36.297Z_

验证 YAML 语法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7437ae9b-827e-4caa-a0ee-6ca279b68a2a",
  "isSidechain": false,
  "requestId": "req_011CbAktzvmNbmXsB5WKrfRR",
  "type": "assistant",
  "uuid": "ab60366e-1250-4586-8c74-36861b5a48df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HHPjsVKh1QiKCrXTGL6kq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3717,
      "cache_read_input_tokens": 54611,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 54611,
          "cache_creation_input_tokens": 3717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3717
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-18T21:38:39.045Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MrhFKpabzQZVpB34ieZZfH`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('experiment_plan.yaml') as f:\n    data = yaml.safe_load(f)\nprint('Valid YAML')\n# Verify the 5 entries\nfor exp in data['experiments']:\n    eid = exp['id']\n    if eid in ['exp-005','exp-006','exp-007','exp-013','exp-015']:\n        print(f\\\"{eid}: registry_id = {exp.get('registry_id', 'MISSING')}\\\")\n\"",
  "description": "Validate YAML and verify registry_id fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab60366e-1250-4586-8c74-36861b5a48df",
  "isSidechain": false,
  "requestId": "req_011CbAktzvmNbmXsB5WKrfRR",
  "type": "assistant",
  "uuid": "12c18096-0c1d-4bf5-84b6-fecaac981a71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012HHPjsVKh1QiKCrXTGL6kq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3717,
      "cache_read_input_tokens": 54611,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 54611,
          "cache_creation_input_tokens": 3717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3717
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-18T21:38:39.273Z_

<details><summary>↩ Tool result · `toolu_01MrhFKpabzQZVpB34ieZZfH`</summary>

```text
Valid YAML
exp-005: registry_id = exp_docred_confusability
exp-006: registry_id = exp006_interaction_2x2
exp-007: registry_id = exp016_fewrel_error_taxonomy
exp-013: registry_id = ['exp008_sdgd_v2_fewnerd', 'exp_confusability_batch_composition']
exp-015: registry_id = exp015_scs_validation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12c18096-0c1d-4bf5-84b6-fecaac981a71",
  "isSidechain": false,
  "promptId": "9619f61e-9358-4135-8c6a-70fec77c7f64",
  "type": "user",
  "uuid": "6d4545de-0ec8-43ea-8f40-9a3f11bcf928",
  "toolUseResult": {
    "stdout": "Valid YAML\nexp-005: registry_id = exp_docred_confusability\nexp-006: registry_id = exp006_interaction_2x2\nexp-007: registry_id = exp016_fewrel_error_taxonomy\nexp-013: registry_id = ['exp008_sdgd_v2_fewnerd', 'exp_confusability_batch_composition']\nexp-015: registry_id = exp015_scs_validation",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "12c18096-0c1d-4bf5-84b6-fecaac981a71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-18T21:38:43.633Z_

YAML 合法，5 个 plan_id 的 registry_id 已正确关联：

| plan_id | registry_id |
|---------|-------------|
| exp-005 | `exp_docred_confusability` |
| exp-006 | `exp006_interaction_2x2` |
| exp-007 | `exp016_fewrel_error_taxonomy` (选了更完整的：5 BCS bins + cross-task comparison) |
| exp-013 | `[exp008_sdgd_v2_fewnerd, exp_confusability_batch_composition]` + status_note |
| exp-015 | `exp015_scs_validation` |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d4545de-0ec8-43ea-8f40-9a3f11bcf928",
  "isSidechain": false,
  "requestId": "req_011CbAkuN8y51nk5qHMBKQp1",
  "type": "assistant",
  "uuid": "92aeacfc-4110-4abe-9859-a4905c298002",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W2w6jTfyKYCsexdL4YZNP9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 58328,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 333,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 58328,
          "cache_creation_input_tokens": 333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 333
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 66_

```json
{
  "type": "last-prompt",
  "leafUuid": "92aeacfc-4110-4abe-9859-a4905c298002",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Update experiment_plan.yaml with registry_id mappings",
  "sessionId": "b365b022-44d5-4c79-a1dc-0aafaae183ac"
}
```

---
