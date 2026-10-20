# Research conversation: <agent_context> 项目路径：/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/ Memory 记录：LLM-gener

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/fa623007-1118-4644-bf66-dcd1a38ff1d6.jsonl`
- **Structured JSON:** [`393f0e8d9db9e7810f78.json`](../../sessions/39/393f0e8d9db9e7810f78.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T23:58:11.630Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T23:58:11.630Z",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "content": "&lt;agent_context>\n项目路径：/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/\nMemory 记录：LLM-generated bib had hallucinated authors; all new citations must go through reference-audit\n&lt;/agent_context>\n\n&lt;project_context>\n# 项目: gen-depth-fingerprint\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/gen-depth-fingerprint\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：Rd2-M7 bib 年份验证（Reference Audit）\n\n对论文的 references.bib 文件做完整的引用审计，重点检查：\n\n1. **年份准确性**：每个 bib 条目的 year 字段是否正确（LLM 生成的 bib 容易出错）\n2. **作者准确性**：作者列表是否完整、拼写是否正确\n3. **venue 准确性**：会议/期刊名称是否正确\n4. **条目完整性**：是否缺少必要字段（title, author, year, booktitle/journal）\n5. **格式一致性**：所有条目格式是否统一\n\n### 操作步骤\n\n1. 先 Read `docs/paper/references.bib` 获取完整 bib 文件\n2. 读取 skill 文件了解审计规范：Read `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n3. 用 WebSearch 验证每个条目的年份、作者、venue 是否准确\n4. 特别关注 2024-2026 年的条目（最近发表的论文最容易被 hallucinate）\n5. 发现错误 → 直接修复 `docs/paper/references.bib`\n6. 同步修复 `artifacts/_project/paper/` 下的 bib 文件（如果存在）\n7. 产出一份审计摘要：多少条目、发现多少错误、修复了什么\n\n### 已知风险\n前次审计发现过 hallucinated authors（见 memory），这次要特别仔细验证所有作者名。\n\n### 项目路径\n/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T23:58:11.633Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T23:58:11.633Z",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-15T23:58:11.663Z_

&lt;agent_context>
项目路径：/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/
Memory 记录：LLM-generated bib had hallucinated authors; all new citations must go through reference-audit
&lt;/agent_context>

&lt;project_context>
# 项目: gen-depth-fingerprint

## 运行环境
- 服务器名: autodl-5090
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/gen-depth-fingerprint


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：Rd2-M7 bib 年份验证（Reference Audit）

对论文的 references.bib 文件做完整的引用审计，重点检查：

1. **年份准确性**：每个 bib 条目的 year 字段是否正确（LLM 生成的 bib 容易出错）
2. **作者准确性**：作者列表是否完整、拼写是否正确
3. **venue 准确性**：会议/期刊名称是否正确
4. **条目完整性**：是否缺少必要字段（title, author, year, booktitle/journal）
5. **格式一致性**：所有条目格式是否统一

### 操作步骤

1. 先 Read `docs/paper/references.bib` 获取完整 bib 文件
2. 读取 skill 文件了解审计规范：Read `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`
3. 用 WebSearch 验证每个条目的年份、作者、venue 是否准确
4. 特别关注 2024-2026 年的条目（最近发表的论文最容易被 hallucinate）
5. 发现错误 → 直接修复 `docs/paper/references.bib`
6. 同步修复 `artifacts/_project/paper/` 下的 bib 文件（如果存在）
7. 产出一份审计摘要：多少条目、发现多少错误、修复了什么

### 已知风险
前次审计发现过 hallucinated authors（见 memory），这次要特别仔细验证所有作者名。

### 项目路径
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "717c1a5f-05be-403b-aa0c-e27dacf66b17",
  "type": "user",
  "uuid": "42b340ab-18ee-4c53-95ff-712b9487ba6d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T23:58:11.662Z_

```json
{
  "parentUuid": "42b340ab-18ee-4c53-95ff-712b9487ba6d",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__verify_references"
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__verify_references"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "cd0b382d-14e7-433b-aa7f-ce9574c293ff",
  "timestamp": "2026-05-15T23:58:11.662Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T23:58:11.662Z_

```json
{
  "parentUuid": "cd0b382d-14e7-433b-aa7f-ce9574c293ff",
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
  "uuid": "998979a1-2f71-4337-a598-dda885ae0c98",
  "timestamp": "2026-05-15T23:58:11.662Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T23:58:11.662Z_

```json
{
  "parentUuid": "998979a1-2f71-4337-a598-dda885ae0c98",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f865fd8a-0f86-45c9-903f-9f944946ef21",
  "timestamp": "2026-05-15T23:58:11.662Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit references.bib for accuracy and hallucinations",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Assistant

_source line 8 · 2026-05-15T23:58:14.624Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the references.bib file and the reference-audit skill file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f865fd8a-0f86-45c9-903f-9f944946ef21",
  "isSidechain": false,
  "requestId": "req_011Cb5G7nW7f4McXmQJ69WQS",
  "type": "assistant",
  "uuid": "d35ff369-33a3-41a2-b188-9900bb7f4869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmS64Fv8y63uZdJtT6jgYo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12264,
      "cache_read_input_tokens": 11841,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 181,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12264
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

_source line 9 · 2026-05-15T23:58:15.144Z_

<details open><summary>🔧 Tool call — Read · `toolu_012HhB3yx2KKZvjqT2y96Ye5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d35ff369-33a3-41a2-b188-9900bb7f4869",
  "isSidechain": false,
  "requestId": "req_011Cb5G7nW7f4McXmQJ69WQS",
  "type": "assistant",
  "uuid": "ebe22a9d-50fe-445e-bcd8-0e644ec55af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmS64Fv8y63uZdJtT6jgYo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12264,
      "cache_read_input_tokens": 11841,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 181,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12264
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

_source line 10 · 2026-05-15T23:58:15.159Z_

<details><summary>↩ Tool result · `toolu_012HhB3yx2KKZvjqT2y96Ye5`</summary>

```text
1	% ===== Detection =====
2	
3	@inproceedings{detectgpt,
4	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
5	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
6	  booktitle = {Proceedings of the International Conference on Machine Learning},
7	  year = {2023},
8	}
9	
10	@inproceedings{gltr,
11	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
12	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
14	  year = {2019},
15	}
16	
17	@inproceedings{dna_gpt,
18	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
19	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
20	  booktitle = {Proceedings of the International Conference on Learning Representations},
21	  year = {2024},
22	}
23	
24	@inproceedings{binoculars,
25	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
26	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
27	  booktitle = {Proceedings of the International Conference on Machine Learning},
28	  year = {2024},
29	}
30	
31	@inproceedings{fast_detectgpt,
32	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
33	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
34	  booktitle = {Proceedings of the International Conference on Learning Representations},
35	  year = {2024},
36	}
37	
38	@article{ld_score,
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
40	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
41	  journal = {arXiv preprint arXiv:2605.01647},
42	  year = {2026},
43	}
44	
45	@inproceedings{intrinsic_dimension,
46	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
47	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
48	  booktitle = {Advances in Neural Information Processing Systems},
49	  year = {2023},
50	}
51	
52	@article{diveye,
53	  title = {{Diversity Boosts AI-Generated Text Detection}},
54	  author = {Basani, Advik Raj and Chen, Pin-Yu},
55	  journal = {Transactions on Machine Learning Research},
56	  year = {2026},
57	}
58	
59	@article{generator_barrier,
60	  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
61	  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
62	  journal = {arXiv preprint arXiv:2604.13692},
63	  year = {2026},
64	}
65	
66	@article{feat_aug_transformer,
67	  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},
68	  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn},
69	  journal = {arXiv preprint arXiv:2605.03969},
70	  year = {2026},
71	}
72	
73	@article{reliable_detection,
74	  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
75	  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
76	  journal = {Transactions on Machine Learning Research},
77	  year = {2025},
78	  url = {https://openreview.net/forum?id=OOgsAZdFOt},
79	}
80	
81	@inproceedings{paraphrase_evades,
82	  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
83	  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
84	  booktitle = {Advances in Neural Information Processing Systems},
85	  year = {2023},
86	}
87	
88	@inproceedings{detection_possibilities,
89	  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
90	  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
91	  booktitle = {Proceedings of the International Conference on Machine Learning},
92	  year = {2024},
93	}
94	
95	@inproceedings{grover,
96	  title = {{Defending Against Neural Fake News}},
97	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
98	  booktitle = {Advances in Neural Information Processing Systems},
99	  year = {2019},
100	}
101	
102	@article{release_strategies,
103	  title = {{Release Strategies and the Social Impacts of Language Models}},
104	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
105	  journal = {arXiv preprint arXiv:1908.09203},
106	  year = {2019},
107	}
108	
109	@inproceedings{beyond_binary,
110	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
111	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
112	  booktitle = {Proceedings of the ACM Web Conference},
113	  year = {2025},
114	}
115	
116	@inproceedings{semeval2024_task8,
117	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
118	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
119	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
120	  year = {2024},
121	}
122	
123	% ===== Model Collapse =====
124	
125	@inproceedings{self_consuming_mad,
126	  title = {{Self-Consuming Generative Models Go MAD}},
127	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
128	  booktitle = {Proceedings of the International Conference on Learning Representations},
129	  year = {2024},
130	}
131	
132	@article{curse_of_recursion,
133	  title = {{AI models collapse when trained on recursively generated data}},
134	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
135	  journal = {Nature},
136	  volume = {631},
137	  pages = {755--759},
138	  year = {2024},
139	}
140	
141	@inproceedings{strong_model_collapse,
142	  title = {{Strong Model Collapse}},
143	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
144	  booktitle = {Proceedings of the International Conference on Learning Representations},
145	  year = {2025},
146	}
147	
148	@inproceedings{model_collapse_avoidable,
149	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
150	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
151	  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},
152	  year = {2024},
153	}
154	
155	% ===== OOD Detection =====
156	
157	@inproceedings{ood_baseline,
158	  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},
159	  author = {Hendrycks, Dan and Gimpel, Kevin},
160	  booktitle = {Proceedings of the International Conference on Learning Representations},
161	  year = {2017},
162	}
163	
164	% ===== Data Quality =====
165	
166	@inproceedings{dsir,
167	  title = {{Data Selection for Language Models via Importance Resampling}},
168	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
169	  booktitle = {Advances in Neural Information Processing Systems},
170	  year = {2023},
171	}
172	
173	@inproceedings{qurating,
174	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
175	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
176	  booktitle = {Proceedings of the International Conference on Machine Learning},
177	  year = {2024},
178	}
179	
180	@inproceedings{ccnet,
181	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
182	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
183	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
184	  year = {2020},
185	}
186	
187	% ===== Watermarking =====
188	
189	@inproceedings{watermark_llm,
190	  title = {{A Watermark for Large Language Models}},
191	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
192	  booktitle = {Proceedings of the International Conference on Machine Learning},
193	  year = {2023},
194	}
195	
196	@article{synthid_text,
197	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
198	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
199	  journal = {Nature},
200	  volume = {634},
201	  pages = {818--823},
202	  year = {2024},
203	}
204	
205	@misc{aaronson_watermark,
206	  title = {{Watermarking GPT Outputs}},
207	  author = {Aaronson, Scott and Kirchner, Hendrik},
208	  year = {2022},
209	  howpublished = {Technical Talk},
210	  url = {https://scottaaronson.blog/?p=6823},
211	}
212	
213	@article{chainwash,
214	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
215	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
216	  journal = {arXiv preprint arXiv:2605.05503},
217	  year = {2026},
218	}
219	
220	% ===== Vocabulary Diversity =====
221	
222	@inproceedings{curious_decline,
223	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
224	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
225	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
226	  year = {2024},
227	}
228	
229	@inproceedings{writing_diversity,
230	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
231	  author = {Padmakumar, Vishakh and He, He},
232	  booktitle = {Proceedings of the International Conference on Learning Representations},
233	  year = {2024},
234	}
235	
236	@inproceedings{nucleus_sampling,
237	  title = {{The Curious Case of Neural Text Degeneration}},
238	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
239	  booktitle = {Proceedings of the International Conference on Learning Representations},
240	  year = {2020},
241	}
242	
243	@inproceedings{mapping_llm_science,
244	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
245	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
246	  booktitle = {Proceedings of the Conference on Language Modeling},
247	  year = {2024},
248	}
249	
250	@inproceedings{monitoring_ai_review,
251	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
252	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
253	  booktitle = {Proceedings of the International Conference on Machine Learning},
254	  year = {2024},
255	}
256	
257	% ===== Stylometry =====
258	
259	@article{stamatatos_survey,
260	  title = {{A Survey of Modern Authorship Attribution Methods}},
261	  author = {Stamatatos, Efstathios},
262	  journal = {Journal of the American Society for Information Science and Technology},
263	  year = {2009},
264	}
265	
266	@article{koppel_authorship,
267	  title = {{Computational Methods in Authorship Attribution}},
268	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
269	  journal = {Journal of the American Society for Information Science and Technology},
270	  year = {2009},
271	}
272	
273	@inproceedings{uchendu_attribution,
274	  title = {{Authorship Attribution for Neural Text Generation}},
275	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
276	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
277	  year = {2020},
278	}
279	
280	@inproceedings{munir_looking_glass,
281	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
282	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
283	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
284	  year = {2021},
285	}
286	
287	% ===== Iterative Generation =====
288	
289	@inproceedings{broken_telephone,
290	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
291	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
292	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
293	  year = {2025},
294	}
295	
296	@article{markovian_chains,
297	  title = {{Markovian Generation Chains in Large Language Models}},
298	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
299	  journal = {arXiv preprint arXiv:2603.11228},
300	  year = {2026},
301	}
302	
303	% ===== Membership Inference =====
304	
305	@inproceedings{min_k_percent,
306	  title = {{Detecting Pretraining Data from Large Language Models}},
307	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
308	  booktitle = {Proceedings of the International Conference on Learning Representations},
309	  year = {2024},
310	}
311	
312	% ===== Survey =====
313	
314	@article{wu_survey_2025,
315	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
316	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
317	  journal = {Computational Linguistics},
318	  publisher = {MIT Press},
319	  year = {2025},
320	}
321	
322	@inproceedings{jawahar_survey,
323	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
324	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
325	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
326	  year = {2020},
327	}
328	
329	% ===== Models =====
330	
331	@inproceedings{pythia,
332	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
333	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
334	  booktitle = {Proceedings of the International Conference on Machine Learning},
335	  year = {2023},
336	}
337	
338	@inproceedings{olmo,
339	  title = {{OLMo: Accelerating the Science of Language Models}},
340	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
341	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
342	  year = {2024},
343	}
344	
345	@article{qwen3,
346	  title = {{Qwen3 Technical Report}},
347	  author = {{Qwen Team}},
348	  journal = {arXiv preprint arXiv:2505.09388},
349	  year = {2025},
350	}
351	
352	% ===== Machine Learning =====
353	
354	@article{coral_ordinal,
355	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
356	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
357	  journal = {Pattern Recognition Letters},
358	  volume = {140},
359	  pages = {325--331},
360	  year = {2020},
361	}
362	
363	@inproceedings{frank_hall_ordinal,
364	  title = {{A Simple Approach to Ordinal Classification}},
365	  author = {Frank, Eibe and Hall, Mark},
366	  booktitle = {Proceedings of the European Conference on Machine Learning},
367	  year = {2001},
368	}
369	
370	@inproceedings{xgboost,
371	  title = {{XGBoost: A Scalable Tree Boosting System}},
372	  author = {Chen, Tianqi and Guestrin, Carlos},
373	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
374	  year = {2016},
375	}
376	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebe22a9d-50fe-445e-bcd8-0e644ec55af0",
  "isSidechain": false,
  "promptId": "717c1a5f-05be-403b-aa0c-e27dacf66b17",
  "type": "user",
  "uuid": "8504e39c-10d7-48f4-a964-f3de3706bf50",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
      "content": "% ===== Detection =====\n\n@inproceedings{detectgpt,\n  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{gltr,\n  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year = {2019},\n}\n\n@inproceedings{dna_gpt,\n  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{binoculars,\n  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{fast_detectgpt,\n  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{ld_score,\n  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},\n  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},\n  journal = {arXiv preprint arXiv:2605.01647},\n  year = {2026},\n}\n\n@inproceedings{intrinsic_dimension,\n  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@article{diveye,\n  title = {{Diversity Boosts AI-Generated Text Detection}},\n  author = {Basani, Advik Raj and Chen, Pin-Yu},\n  journal = {Transactions on Machine Learning Research},\n  year = {2026},\n}\n\n@article{generator_barrier,\n  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  journal = {arXiv preprint arXiv:2604.13692},\n  year = {2026},\n}\n\n@article{feat_aug_transformer,\n  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},\n  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\\\"o}rn},\n  journal = {arXiv preprint arXiv:2605.03969},\n  year = {2026},\n}\n\n@article{reliable_detection,\n  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},\n  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal = {Transactions on Machine Learning Research},\n  year = {2025},\n  url = {https://openreview.net/forum?id=OOgsAZdFOt},\n}\n\n@inproceedings{paraphrase_evades,\n  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},\n  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{detection_possibilities,\n  title = {{Position: On the Possibilities of AI-Generated Text Detection}},\n  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{grover,\n  title = {{Defending Against Neural Fake News}},\n  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2019},\n}\n\n@article{release_strategies,\n  title = {{Release Strategies and the Social Impacts of Language Models}},\n  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},\n  journal = {arXiv preprint arXiv:1908.09203},\n  year = {2019},\n}\n\n@inproceedings{beyond_binary,\n  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},\n  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle = {Proceedings of the ACM Web Conference},\n  year = {2025},\n}\n\n@inproceedings{semeval2024_task8,\n  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},\n  year = {2024},\n}\n\n% ===== Model Collapse =====\n\n@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{curse_of_recursion,\n  title = {{AI models collapse when trained on recursively generated data}},\n  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal = {Nature},\n  volume = {631},\n  pages = {755--759},\n  year = {2024},\n}\n\n@inproceedings{strong_model_collapse,\n  title = {{Strong Model Collapse}},\n  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2025},\n}\n\n@inproceedings{model_collapse_avoidable,\n  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {Proceedings of the First Conference on Language Modeling (COLM)},\n  year = {2024},\n}\n\n% ===== OOD Detection =====\n\n@inproceedings{ood_baseline,\n  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},\n  author = {Hendrycks, Dan and Gimpel, Kevin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2017},\n}\n\n% ===== Data Quality =====\n\n@inproceedings{dsir,\n  title = {{Data Selection for Language Models via Importance Resampling}},\n  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{qurating,\n  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{ccnet,\n  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},\n  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle = {Proceedings of the Language Resources and Evaluation Conference},\n  year = {2020},\n}\n\n% ===== Watermarking =====\n\n@inproceedings{watermark_llm,\n  title = {{A Watermark for Large Language Models}},\n  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@article{synthid_text,\n  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},\n  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},\n  journal = {Nature},\n  volume = {634},\n  pages = {818--823},\n  year = {2024},\n}\n\n@misc{aaronson_watermark,\n  title = {{Watermarking GPT Outputs}},\n  author = {Aaronson, Scott and Kirchner, Hendrik},\n  year = {2022},\n  howpublished = {Technical Talk},\n  url = {https://scottaaronson.blog/?p=6823},\n}\n\n@article{chainwash,\n  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},\n  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},\n  journal = {arXiv preprint arXiv:2605.05503},\n  year = {2026},\n}\n\n% ===== Vocabulary Diversity =====\n\n@inproceedings{curious_decline,\n  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\'{e}},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL},\n  year = {2024},\n}\n\n@inproceedings{writing_diversity,\n  title = {{Does Writing with Language Models Reduce Content Diversity?}},\n  author = {Padmakumar, Vishakh and He, He},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{nucleus_sampling,\n  title = {{The Curious Case of Neural Text Degeneration}},\n  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2020},\n}\n\n@inproceedings{mapping_llm_science,\n  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},\n  booktitle = {Proceedings of the Conference on Language Modeling},\n  year = {2024},\n}\n\n@inproceedings{monitoring_ai_review,\n  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n% ===== Stylometry =====\n\n@article{stamatatos_survey,\n  title = {{A Survey of Modern Authorship Attribution Methods}},\n  author = {Stamatatos, Efstathios},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@article{koppel_authorship,\n  title = {{Computational Methods in Authorship Attribution}},\n  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@inproceedings{uchendu_attribution,\n  title = {{Authorship Attribution for Neural Text Generation}},\n  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2020},\n}\n\n@inproceedings{munir_looking_glass,\n  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},\n  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},\n  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},\n  year = {2021},\n}\n\n% ===== Iterative Generation =====\n\n@inproceedings{broken_telephone,\n  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n}\n\n@article{markovian_chains,\n  title = {{Markovian Generation Chains in Large Language Models}},\n  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},\n  journal = {arXiv preprint arXiv:2603.11228},\n  year = {2026},\n}\n\n% ===== Membership Inference =====\n\n@inproceedings{min_k_percent,\n  title = {{Detecting Pretraining Data from Large Language Models}},\n  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n% ===== Survey =====\n\n@article{wu_survey_2025,\n  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  journal = {Computational Linguistics},\n  publisher = {MIT Press},\n  year = {2025},\n}\n\n@inproceedings{jawahar_survey,\n  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},\n  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics},\n  year = {2020},\n}\n\n% ===== Models =====\n\n@inproceedings{pythia,\n  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},\n  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{olmo,\n  title = {{OLMo: Accelerating the Science of Language Models}},\n  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@article{qwen3,\n  title = {{Qwen3 Technical Report}},\n  author = {{Qwen Team}},\n  journal = {arXiv preprint arXiv:2505.09388},\n  year = {2025},\n}\n\n% ===== Machine Learning =====\n\n@article{coral_ordinal,\n  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal = {Pattern Recognition Letters},\n  volume = {140},\n  pages = {325--331},\n  year = {2020},\n}\n\n@inproceedings{frank_hall_ordinal,\n  title = {{A Simple Approach to Ordinal Classification}},\n  author = {Frank, Eibe and Hall, Mark},\n  booktitle = {Proceedings of the European Conference on Machine Learning},\n  year = {2001},\n}\n\n@inproceedings{xgboost,\n  title = {{XGBoost: A Scalable Tree Boosting System}},\n  author = {Chen, Tianqi and Guestrin, Carlos},\n  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},\n  year = {2016},\n}\n",
      "numLines": 376,
      "startLine": 1,
      "totalLines": 376
    }
  },
  "sourceToolAssistantUUID": "ebe22a9d-50fe-445e-bcd8-0e644ec55af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T23:58:15.253Z_

<details><summary>↩ Tool result · `toolu_01N6hFS4iRkFRzUgg3iX9UmJ`</summary>

````text
1	---
2	name: reference-audit
3	description: 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。
4	scope: global
5	tags:
6	- workflow
7	- submission
8	- writing
9	- quality
10	priority: 6
11	version: 2
12	roles:
13	- agent
14	- paper_agent
15	- review_reviewer
16	- worker
17	---
18	
19	# 引用验证与审计（Reference Audit）
20	
21	## 核心原则
22	
23	**写时验证，而非写后检查。** 每添加一条引用，立即验证真实性。AI 生成的引用约 40% 存在错误——绝不信任记忆中的引用信息。
24	
25	## 触发条件
26	
27	- 写论文时添加引用
28	- Review Reviewer 审查论文引用质量
29	- 提交前最终检查
30	- 发现可疑引用（年份不对、作者不存在、找不到原文）
31	
32	## 验证流程
33	
34	### 1. 单条引用验证（写论文时）
35	
36	每次需要引用时：
37	
38	1. **WebSearch 查找**：搜索论文标题 + 第一作者
39	2. **Google Scholar 确认**：`site:scholar.google.com [论文标题] [作者]`
40	3. **核对关键信息**：标题、第一作者、年份（±1 年）、venue
41	4. **获取 BibTeX**：从 Google Scholar 或 DBLP 获取标准格式
42	5. **验证 claim**（如果引用了具体结论）：确认该 claim 确实出现在原文中
43	
44	### 2. 全文引用审计（批量检查）
45	
46	**Step 1：调用 `verify_references(paper_dir)`**
47	
48	这是首选方式。该工具自动完成：
49	- 解析所有 .bib 文件，提取结构化条目
50	- 解析所有 .tex 文件，提取 `\cite{}`/`\citep{}`/`\citet{}` 引用
51	- 交叉检查：找出 orphan（.bib 有但未引用）和 missing（引用了但 .bib 没有）
52	- 调 OpenAlex API 在线验证每条引用是否存在（返回 verified/not_found/mismatch）
53	
54	如果只需快速离线检查，传 `skip_online=True`。
55	
56	**Step 2：人工复核工具报告中的问题条目**
57	
58	重点关注：
59	- `status: not_found` — 可能是幻觉引用，用 WebSearch 二次验证
60	- `status: mismatch` — 年份等信息不一致，检查 preprint vs published 版本
61	- `missing_bib` — 正文引用了但 .bib 中不存在，编译会报错
62	- `orphan_bib` — .bib 中有但正文未引用，清理或补引用
63	
64	**Step 3：语义验证**（优先级排序）
65	1. 首先验证 Introduction 和 Related Work 中的高频引用
66	2. 然后验证 Method 中支撑技术 claim 的引用
67	3. 最后验证其余引用
68	
69	对于 OpenAlex 未找到的条目，用 WebSearch 补充验证（arXiv、DOI、DBLP）。
70	
71	### 3. 验证失败处理
72	
73	**找不到论文时**：
74	1. 检查拼写——标题或作者名是否有误？
75	2. 尝试不同查询组合（WebSearch + Google Scholar + DBLP）
76	3. 标记为 `[CITATION NEEDED]`
77	4. 明确告知——说明哪条引用无法验证
78	
79	**信息不匹配时**：
80	1. 确认是否找对了论文
81	2. 检查版本——preprint vs published 版本
82	3. 用最准确的版本更新信息
83	
84	**绝不做的事**：
85	- 从记忆生成 BibTeX——AI 生成引用 40% 错误率
86	- 跳过验证步骤
87	- 假设论文存在
88	- 对无法验证的引用不做标记
89	
90	## 常见引用问题模式
91	
92	| 问题类型 | 特征 | 风险 |
93	|---------|------|------|
94	| **幻觉引用** | 论文不存在，作者或标题是 AI 编造的 | 严重——直接影响学术诚信 |
95	| **信息错位** | 作者、年份、venue 不匹配 | 中等——reviewer 一查就发现 |
96	| **孤立引用** | .bib 有但正文没引用 | 轻微——但显得不够整洁 |
97	| **缺失引用** | 正文引用但 .bib 没有 | 编译错误——必须修复 |
98	| **Claim 不匹配** | 引用了论文但声称的结论不在原文中 | 严重——误导性引用 |
99	
100	## 输出格式
101	
102	审计完成后，生成结构化报告：
103	
104	```
105	## 引用审计报告
106	
107	**总数**: X 条引用
108	**已验证**: Y 条（OpenAlex confirmed）
109	**问题**: Z 条
110	
111	### 问题列表
112	
113	1. [severity: critical] `\cite{xxx}` — OpenAlex 未找到，WebSearch 也无结果，疑似幻觉引用
114	   - 建议：删除或替换为已验证的替代引用
115	
116	2. [severity: warning] `\cite{yyy}` — 年份不匹配（bib: 2023, OpenAlex: 2022）
117	   - 建议：更新为正确年份
118	
119	3. [severity: info] `\cite{zzz}` — bib 中存在但正文未引用
120	   - 建议：删除或在相关段落补充引用
121	```
122	
123	## 设计参考
124	
125	本 skill 的验证原则参考了 Dr. Claw (K-Dense Inc.) 的 inno-reference-audit skill。
126	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "c452e6b1-685a-4662-82a5-6dccfae47df5",
  "isSidechain": false,
  "promptId": "717c1a5f-05be-403b-aa0c-e27dacf66b17",
  "type": "user",
  "uuid": "f8e26564-1a8e-4a6a-8798-2769b14a3921",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md",
      "content": "---\nname: reference-audit\ndescription: 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。\nscope: global\ntags:\n- workflow\n- submission\n- writing\n- quality\npriority: 6\nversion: 2\nroles:\n- agent\n- paper_agent\n- review_reviewer\n- worker\n---\n\n# 引用验证与审计（Reference Audit）\n\n## 核心原则\n\n**写时验证，而非写后检查。** 每添加一条引用，立即验证真实性。AI 生成的引用约 40% 存在错误——绝不信任记忆中的引用信息。\n\n## 触发条件\n\n- 写论文时添加引用\n- Review Reviewer 审查论文引用质量\n- 提交前最终检查\n- 发现可疑引用（年份不对、作者不存在、找不到原文）\n\n## 验证流程\n\n### 1. 单条引用验证（写论文时）\n\n每次需要引用时：\n\n1. **WebSearch 查找**：搜索论文标题 + 第一作者\n2. **Google Scholar 确认**：`site:scholar.google.com [论文标题] [作者]`\n3. **核对关键信息**：标题、第一作者、年份（±1 年）、venue\n4. **获取 BibTeX**：从 Google Scholar 或 DBLP 获取标准格式\n5. **验证 claim**（如果引用了具体结论）：确认该 claim 确实出现在原文中\n\n### 2. 全文引用审计（批量检查）\n\n**Step 1：调用 `verify_references(paper_dir)`**\n\n这是首选方式。该工具自动完成：\n- 解析所有 .bib 文件，提取结构化条目\n- 解析所有 .tex 文件，提取 `\\cite{}`/`\\citep{}`/`\\citet{}` 引用\n- 交叉检查：找出 orphan（.bib 有但未引用）和 missing（引用了但 .bib 没有）\n- 调 OpenAlex API 在线验证每条引用是否存在（返回 verified/not_found/mismatch）\n\n如果只需快速离线检查，传 `skip_online=True`。\n\n**Step 2：人工复核工具报告中的问题条目**\n\n重点关注：\n- `status: not_found` — 可能是幻觉引用，用 WebSearch 二次验证\n- `status: mismatch` — 年份等信息不一致，检查 preprint vs published 版本\n- `missing_bib` — 正文引用了但 .bib 中不存在，编译会报错\n- `orphan_bib` — .bib 中有但正文未引用，清理或补引用\n\n**Step 3：语义验证**（优先级排序）\n1. 首先验证 Introduction 和 Related Work 中的高频引用\n2. 然后验证 Method 中支撑技术 claim 的引用\n3. 最后验证其余引用\n\n对于 OpenAlex 未找到的条目，用 WebSearch 补充验证（arXiv、DOI、DBLP）。\n\n### 3. 验证失败处理\n\n**找不到论文时**：\n1. 检查拼写——标题或作者名是否有误？\n2. 尝试不同查询组合（WebSearch + Google Scholar + DBLP）\n3. 标记为 `[CITATION NEEDED]`\n4. 明确告知——说明哪条引用无法验证\n\n**信息不匹配时**：\n1. 确认是否找对了论文\n2. 检查版本——preprint vs published 版本\n3. 用最准确的版本更新信息\n\n**绝不做的事**：\n- 从记忆生成 BibTeX——AI 生成引用 40% 错误率\n- 跳过验证步骤\n- 假设论文存在\n- 对无法验证的引用不做标记\n\n## 常见引用问题模式\n\n| 问题类型 | 特征 | 风险 |\n|---------|------|------|\n| **幻觉引用** | 论文不存在，作者或标题是 AI 编造的 | 严重——直接影响学术诚信 |\n| **信息错位** | 作者、年份、venue 不匹配 | 中等——reviewer 一查就发现 |\n| **孤立引用** | .bib 有但正文没引用 | 轻微——但显得不够整洁 |\n| **缺失引用** | 正文引用但 .bib 没有 | 编译错误——必须修复 |\n| **Claim 不匹配** | 引用了论文但声称的结论不在原文中 | 严重——误导性引用 |\n\n## 输出格式\n\n审计完成后，生成结构化报告：\n\n```\n## 引用审计报告\n\n**总数**: X 条引用\n**已验证**: Y 条（OpenAlex confirmed）\n**问题**: Z 条\n\n### 问题列表\n\n1. [severity: critical] `\\cite{xxx}` — OpenAlex 未找到，WebSearch 也无结果，疑似幻觉引用\n   - 建议：删除或替换为已验证的替代引用\n\n2. [severity: warning] `\\cite{yyy}` — 年份不匹配（bib: 2023, OpenAlex: 2022）\n   - 建议：更新为正确年份\n\n3. [severity: info] `\\cite{zzz}` — bib 中存在但正文未引用\n   - 建议：删除或在相关段落补充引用\n```\n\n## 设计参考\n\n本 skill 的验证原则参考了 Dr. Claw (K-Dense Inc.) 的 inno-reference-audit skill。\n",
      "numLines": 126,
      "startLine": 1,
      "totalLines": 126
    }
  },
  "sourceToolAssistantUUID": "c452e6b1-685a-4662-82a5-6dccfae47df5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Tool call

_source line 12 · 2026-05-15T23:58:15.248Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N6hFS4iRkFRzUgg3iX9UmJ`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8504e39c-10d7-48f4-a964-f3de3706bf50",
  "isSidechain": false,
  "requestId": "req_011Cb5G7nW7f4McXmQJ69WQS",
  "type": "assistant",
  "uuid": "c452e6b1-685a-4662-82a5-6dccfae47df5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmS64Fv8y63uZdJtT6jgYo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12264,
      "cache_read_input_tokens": 11841,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 181,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12264
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

_source line 13_

```json
{
  "type": "last-prompt",
  "leafUuid": "f8e26564-1a8e-4a6a-8798-2769b14a3921",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit references.bib for accuracy and hallucinations",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Assistant

_source line 15 · 2026-05-15T23:58:18.594Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to verify each bib entry. Let me first use the `verify_references` tool to do an automated check, and then I'll use WebSearch to verify specific entries. Let me load the necessary tools first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8e26564-1a8e-4a6a-8798-2769b14a3921",
  "isSidechain": false,
  "requestId": "req_011Cb5G841mmvFiDfWwHYXLQ",
  "type": "assistant",
  "uuid": "3557e49b-3c60-41bd-9060-9d1090c6d38e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4F5mxCaDU6vXVz4B5ytvj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9137,
      "cache_read_input_tokens": 24105,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 24105,
          "cache_creation_input_tokens": 9137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9137
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

_source line 16 · 2026-05-15T23:58:19.663Z_

读取完成，共 37 条 bib 条目。先用 `verify_references` 做自动化检查，再逐条 WebSearch 验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3557e49b-3c60-41bd-9060-9d1090c6d38e",
  "isSidechain": false,
  "requestId": "req_011Cb5G841mmvFiDfWwHYXLQ",
  "type": "assistant",
  "uuid": "fc2d0540-5a8a-4f74-b8c0-3c9b14b9071a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4F5mxCaDU6vXVz4B5ytvj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9137,
      "cache_read_input_tokens": 24105,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 24105,
          "cache_creation_input_tokens": 9137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9137
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

_source line 17 · 2026-05-15T23:58:20.307Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PDJ3XKjuuKoykb2mPNNcUR`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__verify_references,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc2d0540-5a8a-4f74-b8c0-3c9b14b9071a",
  "isSidechain": false,
  "requestId": "req_011Cb5G841mmvFiDfWwHYXLQ",
  "type": "assistant",
  "uuid": "27d785e9-4621-4ae3-a73c-f3d6fbda74c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4F5mxCaDU6vXVz4B5ytvj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9137,
      "cache_read_input_tokens": 24105,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 24105,
          "cache_creation_input_tokens": 9137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9137
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

_source line 18 · 2026-05-15T23:58:20.310Z_

<details><summary>↩ Tool result · `toolu_01PDJ3XKjuuKoykb2mPNNcUR`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__verify_references"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27d785e9-4621-4ae3-a73c-f3d6fbda74c2",
  "isSidechain": false,
  "promptId": "717c1a5f-05be-403b-aa0c-e27dacf66b17",
  "type": "user",
  "uuid": "e2f673a5-ce68-4871-ae98-22574383cd37",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__verify_references",
      "WebSearch"
    ],
    "query": "select:mcp__agent-ml-research__verify_references,WebSearch",
    "total_deferred_tools": 23
  },
  "sourceToolAssistantUUID": "27d785e9-4621-4ae3-a73c-f3d6fbda74c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T23:58:25.056Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_0178MVSmD67m2GvoRDYNrVm1`</summary>

```json
{
  "paper_dir": "docs/paper",
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2f673a5-ce68-4871-ae98-22574383cd37",
  "isSidechain": false,
  "requestId": "req_011Cb5G8RgWPuhrh4CfGGrGS",
  "type": "assistant",
  "uuid": "9aa3eb11-66b9-4609-b838-a8349ce12f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMA2md9cptWNbReUgDTEBA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 33242,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1063,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 33242,
          "cache_creation_input_tokens": 1063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1063
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

_source line 20 · 2026-05-15T23:59:15.854Z_

<details><summary>↩ Tool result · `toolu_0178MVSmD67m2GvoRDYNrVm1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 72, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 41, \"online_not_found\": 6, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"detectgpt\", \"type\": \"inproceedings\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"authors\": \"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"gltr\", \"type\": \"inproceedings\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"authors\": \"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\", \"year\": \"2019\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"dna_gpt\", \"type\": \"inproceedings\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"authors\": \"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"binoculars\", \"type\": \"inproceedings\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"authors\": \"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"fast_detectgpt\", \"type\": \"inproceedings\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"authors\": \"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"ld_score\", \"type\": \"article\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"authors\": \"Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardi...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.01647\"}, {\"key\": \"intrinsic_dimension\", \"type\": \"inproceedings\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"authors\": \"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"diveye\", \"type\": \"article\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"authors\": \"Basani, Advik Raj and Chen, Pin-Yu\", \"year\": \"2026\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"generator_barrier\", \"type\": \"article\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"authors\": \"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.13692\"}, {\"key\": \"feat_aug_transformer\", \"type\": \"article\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"authors\": \"Mady, Mohamed and Reschke, Johannes and Schuller, Bj\\\\\\\"orn\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.03969\"}, {\"key\": \"reliable_detection\", \"type\": \"article\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"authors\": \"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\", \"year\": \"2025\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"paraphrase_evades\", \"type\": \"inproceedings\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"authors\": \"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"detection_possibilities\", \"type\": \"inproceedings\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"authors\": \"Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Ma...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"grover\", \"type\": \"inproceedings\", \"title\": \"Defending Against Neural Fake News\", \"authors\": \"Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farha...\", \"year\": \"2019\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"release_strategies\", \"type\": \"article\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"authors\": \"Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbe...\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1908.09203\"}, {\"key\": \"beyond_binary\", \"type\": \"inproceedings\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"authors\": \"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference\"}, {\"key\": \"semeval2024_task8\", \"type\": \"inproceedings\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"authors\": \"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Workshop on Semantic Evaluation\"}, {\"key\": \"self_consuming_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"curse_of_recursion\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"strong_model_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"model_collapse_avoidable\", \"type\": \"inproceedings\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\", \"year\": \"2024\", \"venue\": \"Proceedings of the First Conference on Language Modeling (COLM)\"}, {\"key\": \"ood_baseline\", \"type\": \"inproceedings\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"authors\": \"Hendrycks, Dan and Gimpel, Kevin\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"dsir\", \"type\": \"inproceedings\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"authors\": \"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"qurating\", \"type\": \"inproceedings\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"authors\": \"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"ccnet\", \"type\": \"inproceedings\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"authors\": \"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\", \"year\": \"2020\", \"venue\": \"Proceedings of the Language Resources and Evaluation Conference\"}, {\"key\": \"watermark_llm\", \"type\": \"inproceedings\", \"title\": \"A Watermark for Large Language Models\", \"authors\": \"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"synthid_text\", \"type\": \"article\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"authors\": \"Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and Mc...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"aaronson_watermark\", \"type\": \"misc\", \"title\": \"Watermarking GPT Outputs\", \"authors\": \"Aaronson, Scott and Kirchner, Hendrik\", \"year\": \"2022\", \"venue\": \"\"}, {\"key\": \"chainwash\", \"type\": \"article\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"authors\": \"Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.05503\"}, {\"key\": \"curious_decline\", \"type\": \"inproceedings\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"authors\": \"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\'e\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL\"}, {\"key\": \"writing_diversity\", \"type\": \"inproceedings\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"authors\": \"Padmakumar, Vishakh and He, He\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"nucleus_sampling\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"mapping_llm_science\", \"type\": \"inproceedings\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"authors\": \"Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlon...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Conference on Language Modeling\"}, {\"key\": \"monitoring_ai_review\", \"type\": \"inproceedings\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"authors\": \"Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hanch...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"stamatatos_survey\", \"type\": \"article\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"authors\": \"Stamatatos, Efstathios\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"koppel_authorship\", \"type\": \"article\", \"title\": \"Computational Methods in Authorship Attribution\", \"authors\": \"Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"uchendu_attribution\", \"type\": \"inproceedings\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"authors\": \"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\", \"year\": \"2020\", \"venue\": \"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\"}, {\"key\": \"munir_looking_glass\", \"type\": \"inproceedings\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"authors\": \"Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and...\", \"year\": \"2021\", \"venue\": \"Proceedings of the Conference of the European Chapter of the Association for Com...\"}, {\"key\": \"broken_telephone\", \"type\": \"inproceedings\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"authors\": \"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\", \"year\": \"2025\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"markovian_chains\", \"type\": \"article\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"authors\": \"Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2603.11228\"}, {\"key\": \"min_k_percent\", \"type\": \"inproceedings\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"authors\": \"Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Da...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"wu_survey_2025\", \"type\": \"article\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"authors\": \"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\", \"year\": \"2025\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"jawahar_survey\", \"type\": \"inproceedings\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"authors\": \"Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Computational Linguistics\"}, {\"key\": \"pythia\", \"type\": \"inproceedings\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"authors\": \"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"olmo\", \"type\": \"inproceedings\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"authors\": \"Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"qwen3\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"coral_ordinal\", \"type\": \"article\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"authors\": \"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\", \"year\": \"2020\", \"venue\": \"Pattern Recognition Letters\"}, {\"key\": \"frank_hall_ordinal\", \"type\": \"inproceedings\", \"title\": \"A Simple Approach to Ordinal Classification\", \"authors\": \"Frank, Eibe and Hall, Mark\", \"year\": \"2001\", \"venue\": \"Proceedings of the European Conference on Machine Learning\"}, {\"key\": \"xgboost\", \"type\": \"inproceedings\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"authors\": \"Chen, Tianqi and Guestrin, Carlos\", \"year\": \"2016\", \"venue\": \"Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery an...\"}], \"tex_citations\": [{\"key\": \"mapping_llm_science\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"monitoring_ai_review\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"markovian_chains\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"grover\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"release_strategies\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"dna_gpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feat_aug_transformer\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"reliable_detection\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"intrinsic_dimension\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"diveye\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"generator_barrier\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wu_survey_2025\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"jawahar_survey\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"beyond_binary\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citet\"}, {\"key\": \"semeval2024_task8\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"paraphrase_evades\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"detection_possibilities\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"ood_baseline\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"munir_looking_glass\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"self_consuming_mad\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"curse_of_recursion\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"model_collapse_avoidable\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"strong_model_collapse\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"broken_telephone\", \"file\": \"related_work.tex\", \"line\": 35, \"command\": \"citet\"}, {\"key\": \"markovian_chains\", \"file\": \"related_work.tex\", \"line\": 36, \"command\": \"citet\"}, {\"key\": \"curious_decline\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"writing_diversity\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"stamatatos_survey\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"koppel_authorship\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 46, \"command\": \"citet\"}, {\"key\": \"nucleus_sampling\", \"file\": \"related_work.tex\", \"line\": 48, \"command\": \"citet\"}, {\"key\": \"dsir\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"qurating\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"ccnet\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"watermark_llm\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"synthid_text\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"aaronson_watermark\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"chainwash\", \"file\": \"related_work.tex\", \"line\": 58, \"command\": \"citet\"}, {\"key\": \"min_k_percent\", \"file\": \"related_work.tex\", \"line\": 60, \"command\": \"citet\"}, {\"key\": \"pythia\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"olmo\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"qwen3\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"method.tex\", \"line\": 49, \"command\": \"cite\"}, {\"key\": \"xgboost\", \"file\": \"method.tex\", \"line\": 72, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"method.tex\", \"line\": 78, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"method.tex\", \"line\": 78, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"results.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"results.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"discussion.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"discussion.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 34, \"command\": \"cite\"}, {\"key\": \"curse_of_recursion\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"strong_model_collapse\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"detectgpt\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"status\": \"not_found\", \"confidence\": 0.382, \"matched_title\": \"Regulating ChatGPT and other Large Generative AI Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"gltr\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dna_gpt\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"binoculars\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fast_detectgpt\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ld_score\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"intrinsic_dimension\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"diveye\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Diversity Boosts AI-Generated Text Detection\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"generator_barrier\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feat_aug_transformer\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reliable_detection\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"status\": \"not_found\", \"confidence\": 0.344, \"matched_title\": \"2015 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"paraphrase_evades\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"detection_possibilities\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"status\": \"not_found\", \"confidence\": 0.253, \"matched_title\": \"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"grover\", \"title\": \"Defending Against Neural Fake News\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Defending Against Neural Fake News\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"release_strategies\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Release Strategies and the Social Impacts of Language Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"beyond_binary\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"semeval2024_task8\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"self_consuming_mad\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Consuming Generative Models go MAD\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=alemohammad vs api=casco-rodriguez\"], \"note\": \"\"}, {\"key\": \"curse_of_recursion\", \"title\": \"AI models collapse when trained on recursively generated data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AI models collapse when trained on recursively generated data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"strong_model_collapse\", \"title\": \"Strong Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Strong Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"model_collapse_avoidable\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ood_baseline\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dsir\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Data Selection for Language Models via Importance Resampling\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qurating\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ccnet\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"watermark_llm\", \"title\": \"A Watermark for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Watermark for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"synthid_text\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable watermarking for identifying large language model outputs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"aaronson_watermark\", \"title\": \"Watermarking GPT Outputs\", \"status\": \"not_found\", \"confidence\": 0.418, \"matched_title\": \"Undetectable Watermarks for Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.42 below threshold 0.82\"}, {\"key\": \"chainwash\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"curious_decline\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"writing_diversity\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nucleus_sampling\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mapping_llm_science\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"monitoring_ai_review\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stamatatos_survey\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A survey of modern authorship attribution methods\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"koppel_authorship\", \"title\": \"Computational Methods in Authorship Attribution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Computational methods in authorship attribution\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uchendu_attribution\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Authorship Attribution for Neural Text Generation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"munir_looking_glass\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"broken_telephone\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"markovian_chains\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Markovian Generation Chains in Large Language Models\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"min_k_percent\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Detecting Pretraining Data from Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wu_survey_2025\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jawahar_survey\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pythia\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"status\": \"not_found\", \"confidence\": 0.497, \"matched_title\": \"The TRIPOD-LLM reporting guideline for studies using large language models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"olmo\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OLMo: Accelerating the Science of Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"coral_ordinal\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rank consistent ordinal regression for neural networks with application to age estimation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frank_hall_ordinal\", \"title\": \"A Simple Approach to Ordinal Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple Approach to Ordinal Classification\", \"matched_year\": \"2001\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xgboost\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"status\": \"not_found\", \"confidence\": 0.298, \"matched_title\": \"XGBoost\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aa3eb11-66b9-4609-b838-a8349ce12f81",
  "isSidechain": false,
  "promptId": "717c1a5f-05be-403b-aa0c-e27dacf66b17",
  "type": "user",
  "uuid": "87b6711a-b554-4191-bc26-3656c303b738",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 49, \\\"total_citations\\\": 72, \\\"unique_cited_keys\\\": 49, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 41, \\\"online_not_found\\\": 6, \\\"online_mismatch\\\": 2}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"detectgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\", \\\"authors\\\": \\\"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"authors\\\": \\\"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\\\"}, {\\\"key\\\": \\\"dna_gpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"authors\\\": \\\"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"authors\\\": \\\"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"authors\\\": \\\"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\\\", \\\"authors\\\": \\\"Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardi...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.01647\\\"}, {\\\"key\\\": \\\"intrinsic_dimension\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"authors\\\": \\\"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"diveye\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"authors\\\": \\\"Basani, Advik Raj and Chen, Pin-Yu\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Transactions on Machine Learning Research\\\"}, {\\\"key\\\": \\\"generator_barrier\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"authors\\\": \\\"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2604.13692\\\"}, {\\\"key\\\": \\\"feat_aug_transformer\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\", \\\"authors\\\": \\\"Mady, Mohamed and Reschke, Johannes and Schuller, Bj\\\\\\\\\\\\\\\"orn\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.03969\\\"}, {\\\"key\\\": \\\"reliable_detection\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\\\", \\\"authors\\\": \\\"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Transactions on Machine Learning Research\\\"}, {\\\"key\\\": \\\"paraphrase_evades\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\\\", \\\"authors\\\": \\\"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"detection_possibilities\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Position: On the Possibilities of AI-Generated Text Detection\\\", \\\"authors\\\": \\\"Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Ma...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"grover\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Defending Against Neural Fake News\\\", \\\"authors\\\": \\\"Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farha...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"release_strategies\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Release Strategies and the Social Impacts of Language Models\\\", \\\"authors\\\": \\\"Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbe...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1908.09203\\\"}, {\\\"key\\\": \\\"beyond_binary\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"authors\\\": \\\"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the ACM Web Conference\\\"}, {\\\"key\\\": \\\"semeval2024_task8\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"authors\\\": \\\"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Workshop on Semantic Evaluation\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consuming Generative Models Go MAD\\\", \\\"authors\\\": \\\"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"authors\\\": \\\"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Nature\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Strong Model Collapse\\\", \\\"authors\\\": \\\"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"model_collapse_avoidable\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"authors\\\": \\\"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the First Conference on Language Modeling (COLM)\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\\\", \\\"authors\\\": \\\"Hendrycks, Dan and Gimpel, Kevin\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"dsir\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"authors\\\": \\\"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"qurating\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"authors\\\": \\\"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"ccnet\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"authors\\\": \\\"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the Language Resources and Evaluation Conference\\\"}, {\\\"key\\\": \\\"watermark_llm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Watermark for Large Language Models\\\", \\\"authors\\\": \\\"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"synthid_text\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Scalable Watermarking for Identifying Large Language Model Outputs\\\", \\\"authors\\\": \\\"Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and Mc...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Nature\\\"}, {\\\"key\\\": \\\"aaronson_watermark\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Watermarking GPT Outputs\\\", \\\"authors\\\": \\\"Aaronson, Scott and Kirchner, Hendrik\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"chainwash\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\\\", \\\"authors\\\": \\\"Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.05503\\\"}, {\\\"key\\\": \\\"curious_decline\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"authors\\\": \\\"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\\\\\'e\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL\\\"}, {\\\"key\\\": \\\"writing_diversity\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"authors\\\": \\\"Padmakumar, Vishakh and He, He\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"nucleus_sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"authors\\\": \\\"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"mapping_llm_science\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Mapping the Increasing Use of LLMs in Scientific Papers\\\", \\\"authors\\\": \\\"Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlon...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Conference on Language Modeling\\\"}, {\\\"key\\\": \\\"monitoring_ai_review\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\\\", \\\"authors\\\": \\\"Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hanch...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"stamatatos_survey\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Survey of Modern Authorship Attribution Methods\\\", \\\"authors\\\": \\\"Stamatatos, Efstathios\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Journal of the American Society for Information Science and Technology\\\"}, {\\\"key\\\": \\\"koppel_authorship\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Computational Methods in Authorship Attribution\\\", \\\"authors\\\": \\\"Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Journal of the American Society for Information Science and Technology\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"authors\\\": \\\"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\\\"}, {\\\"key\\\": \\\"munir_looking_glass\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\\\", \\\"authors\\\": \\\"Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the Conference of the European Chapter of the Association for Com...\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"authors\\\": \\\"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Markovian Generation Chains in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2603.11228\\\"}, {\\\"key\\\": \\\"min_k_percent\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Detecting Pretraining Data from Large Language Models\\\", \\\"authors\\\": \\\"Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Da...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"wu_survey_2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"authors\\\": \\\"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Computational Linguistics\\\"}, {\\\"key\\\": \\\"jawahar_survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Automatic Detection of Machine Generated Text: A Critical Survey\\\", \\\"authors\\\": \\\"Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Computational Linguistics\\\"}, {\\\"key\\\": \\\"pythia\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\\\", \\\"authors\\\": \\\"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"olmo\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"OLMo: Accelerating the Science of Language Models\\\", \\\"authors\\\": \\\"Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\\\"}, {\\\"key\\\": \\\"qwen3\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"authors\\\": \\\"Qwen Team\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2505.09388\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\", \\\"authors\\\": \\\"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Pattern Recognition Letters\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"authors\\\": \\\"Frank, Eibe and Hall, Mark\\\", \\\"year\\\": \\\"2001\\\", \\\"venue\\\": \\\"Proceedings of the European Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"xgboost\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"XGBoost: A Scalable Tree Boosting System\\\", \\\"authors\\\": \\\"Chen, Tianqi and Guestrin, Carlos\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery an...\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"mapping_llm_science\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"monitoring_ai_review\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"detectgpt\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"grover\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"release_strategies\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"detectgpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dna_gpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feat_aug_transformer\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"reliable_detection\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"intrinsic_dimension\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"diveye\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"generator_barrier\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wu_survey_2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"jawahar_survey\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"beyond_binary\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"semeval2024_task8\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"paraphrase_evades\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"detection_possibilities\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"munir_looking_glass\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"model_collapse_avoidable\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 36, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"curious_decline\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 42, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"writing_diversity\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 42, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"stamatatos_survey\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"koppel_authorship\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 46, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"nucleus_sampling\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 48, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dsir\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"qurating\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ccnet\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"watermark_llm\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 57, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"synthid_text\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 57, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"aaronson_watermark\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 57, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chainwash\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 58, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"min_k_percent\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 60, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"pythia\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"olmo\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 49, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xgboost\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 72, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 78, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 78, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 90, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 90, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 90, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 60, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 60, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"detectgpt\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 24, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 34, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 37, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"detectgpt\\\", \\\"title\\\": \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.382, \\\"matched_title\\\": \\\"Regulating ChatGPT and other Large Generative AI Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.38 below threshold 0.82\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dna_gpt\\\", \\\"title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"title\\\": \\\"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"intrinsic_dimension\\\", \\\"title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"diveye\\\", \\\"title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"generator_barrier\\\", \\\"title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feat_aug_transformer\\\", \\\"title\\\": \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"reliable_detection\\\", \\\"title\\\": \\\"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.344, \\\"matched_title\\\": \\\"2015 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.34 below threshold 0.82\\\"}, {\\\"key\\\": \\\"paraphrase_evades\\\", \\\"title\\\": \\\"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"detection_possibilities\\\", \\\"title\\\": \\\"Position: On the Possibilities of AI-Generated Text Detection\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.253, \\\"matched_title\\\": \\\"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"grover\\\", \\\"title\\\": \\\"Defending Against Neural Fake News\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Defending Against Neural Fake News\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"release_strategies\\\", \\\"title\\\": \\\"Release Strategies and the Social Impacts of Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Release Strategies and the Social Impacts of Language Models\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"beyond_binary\\\", \\\"title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"semeval2024_task8\\\", \\\"title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"title\\\": \\\"Self-Consuming Generative Models Go MAD\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consuming Generative Models go MAD\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=alemohammad vs api=casco-rodriguez\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"title\\\": \\\"Strong Model Collapse\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Strong Model Collapse\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"model_collapse_avoidable\\\", \\\"title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"title\\\": \\\"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dsir\\\", \\\"title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qurating\\\", \\\"title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ccnet\\\", \\\"title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"watermark_llm\\\", \\\"title\\\": \\\"A Watermark for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Watermark for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"synthid_text\\\", \\\"title\\\": \\\"Scalable Watermarking for Identifying Large Language Model Outputs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable watermarking for identifying large language model outputs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"aaronson_watermark\\\", \\\"title\\\": \\\"Watermarking GPT Outputs\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.418, \\\"matched_title\\\": \\\"Undetectable Watermarks for Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.42 below threshold 0.82\\\"}, {\\\"key\\\": \\\"chainwash\\\", \\\"title\\\": \\\"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"curious_decline\\\", \\\"title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"writing_diversity\\\", \\\"title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nucleus_sampling\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mapping_llm_science\\\", \\\"title\\\": \\\"Mapping the Increasing Use of LLMs in Scientific Papers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Mapping the Increasing Use of LLMs in Scientific Papers\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"monitoring_ai_review\\\", \\\"title\\\": \\\"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"stamatatos_survey\\\", \\\"title\\\": \\\"A Survey of Modern Authorship Attribution Methods\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A survey of modern authorship attribution methods\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"koppel_authorship\\\", \\\"title\\\": \\\"Computational Methods in Authorship Attribution\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Computational methods in authorship attribution\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"munir_looking_glass\\\", \\\"title\\\": \\\"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"title\\\": \\\"Markovian Generation Chains in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Markovian Generation Chains in Large Language Models\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"min_k_percent\\\", \\\"title\\\": \\\"Detecting Pretraining Data from Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Detecting Pretraining Data from Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wu_survey_2025\\\", \\\"title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jawahar_survey\\\", \\\"title\\\": \\\"Automatic Detection of Machine Generated Text: A Critical Survey\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Automatic Detection of Machine Generated Text: A Critical Survey\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"pythia\\\", \\\"title\\\": \\\"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.497, \\\"matched_title\\\": \\\"The TRIPOD-LLM reporting guideline for studies using large language models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.50 below threshold 0.82\\\"}, {\\\"key\\\": \\\"olmo\\\", \\\"title\\\": \\\"OLMo: Accelerating the Science of Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"OLMo: Accelerating the Science of Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qwen3\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Qwen3 Technical Report\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=team vs api=yang\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"title\\\": \\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Rank consistent ordinal regression for neural networks with application to age estimation\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"matched_year\\\": \\\"2001\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xgboost\\\", \\\"title\\\": \\\"XGBoost: A Scalable Tree Boosting System\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.298, \\\"matched_title\\\": \\\"XGBoost\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.30 below threshold 0.82\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 72, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 41, \"online_not_found\": 6, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"detectgpt\", \"type\": \"inproceedings\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"authors\": \"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"gltr\", \"type\": \"inproceedings\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"authors\": \"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\", \"year\": \"2019\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"dna_gpt\", \"type\": \"inproceedings\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"authors\": \"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"binoculars\", \"type\": \"inproceedings\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"authors\": \"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"fast_detectgpt\", \"type\": \"inproceedings\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"authors\": \"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"ld_score\", \"type\": \"article\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"authors\": \"Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardi...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.01647\"}, {\"key\": \"intrinsic_dimension\", \"type\": \"inproceedings\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"authors\": \"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"diveye\", \"type\": \"article\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"authors\": \"Basani, Advik Raj and Chen, Pin-Yu\", \"year\": \"2026\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"generator_barrier\", \"type\": \"article\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"authors\": \"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.13692\"}, {\"key\": \"feat_aug_transformer\", \"type\": \"article\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"authors\": \"Mady, Mohamed and Reschke, Johannes and Schuller, Bj\\\\\\\"orn\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.03969\"}, {\"key\": \"reliable_detection\", \"type\": \"article\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"authors\": \"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\", \"year\": \"2025\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"paraphrase_evades\", \"type\": \"inproceedings\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"authors\": \"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"detection_possibilities\", \"type\": \"inproceedings\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"authors\": \"Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Ma...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"grover\", \"type\": \"inproceedings\", \"title\": \"Defending Against Neural Fake News\", \"authors\": \"Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farha...\", \"year\": \"2019\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"release_strategies\", \"type\": \"article\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"authors\": \"Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbe...\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1908.09203\"}, {\"key\": \"beyond_binary\", \"type\": \"inproceedings\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"authors\": \"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference\"}, {\"key\": \"semeval2024_task8\", \"type\": \"inproceedings\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"authors\": \"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Workshop on Semantic Evaluation\"}, {\"key\": \"self_consuming_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"curse_of_recursion\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"strong_model_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"model_collapse_avoidable\", \"type\": \"inproceedings\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\", \"year\": \"2024\", \"venue\": \"Proceedings of the First Conference on Language Modeling (COLM)\"}, {\"key\": \"ood_baseline\", \"type\": \"inproceedings\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"authors\": \"Hendrycks, Dan and Gimpel, Kevin\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"dsir\", \"type\": \"inproceedings\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"authors\": \"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"qurating\", \"type\": \"inproceedings\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"authors\": \"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"ccnet\", \"type\": \"inproceedings\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"authors\": \"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\", \"year\": \"2020\", \"venue\": \"Proceedings of the Language Resources and Evaluation Conference\"}, {\"key\": \"watermark_llm\", \"type\": \"inproceedings\", \"title\": \"A Watermark for Large Language Models\", \"authors\": \"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"synthid_text\", \"type\": \"article\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"authors\": \"Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and Mc...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"aaronson_watermark\", \"type\": \"misc\", \"title\": \"Watermarking GPT Outputs\", \"authors\": \"Aaronson, Scott and Kirchner, Hendrik\", \"year\": \"2022\", \"venue\": \"\"}, {\"key\": \"chainwash\", \"type\": \"article\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"authors\": \"Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.05503\"}, {\"key\": \"curious_decline\", \"type\": \"inproceedings\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"authors\": \"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\'e\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL\"}, {\"key\": \"writing_diversity\", \"type\": \"inproceedings\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"authors\": \"Padmakumar, Vishakh and He, He\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"nucleus_sampling\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"mapping_llm_science\", \"type\": \"inproceedings\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"authors\": \"Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlon...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Conference on Language Modeling\"}, {\"key\": \"monitoring_ai_review\", \"type\": \"inproceedings\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"authors\": \"Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hanch...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"stamatatos_survey\", \"type\": \"article\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"authors\": \"Stamatatos, Efstathios\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"koppel_authorship\", \"type\": \"article\", \"title\": \"Computational Methods in Authorship Attribution\", \"authors\": \"Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"uchendu_attribution\", \"type\": \"inproceedings\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"authors\": \"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\", \"year\": \"2020\", \"venue\": \"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\"}, {\"key\": \"munir_looking_glass\", \"type\": \"inproceedings\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"authors\": \"Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and...\", \"year\": \"2021\", \"venue\": \"Proceedings of the Conference of the European Chapter of the Association for Com...\"}, {\"key\": \"broken_telephone\", \"type\": \"inproceedings\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"authors\": \"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\", \"year\": \"2025\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"markovian_chains\", \"type\": \"article\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"authors\": \"Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2603.11228\"}, {\"key\": \"min_k_percent\", \"type\": \"inproceedings\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"authors\": \"Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Da...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"wu_survey_2025\", \"type\": \"article\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"authors\": \"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\", \"year\": \"2025\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"jawahar_survey\", \"type\": \"inproceedings\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"authors\": \"Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Computational Linguistics\"}, {\"key\": \"pythia\", \"type\": \"inproceedings\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"authors\": \"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"olmo\", \"type\": \"inproceedings\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"authors\": \"Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"qwen3\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"coral_ordinal\", \"type\": \"article\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"authors\": \"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\", \"year\": \"2020\", \"venue\": \"Pattern Recognition Letters\"}, {\"key\": \"frank_hall_ordinal\", \"type\": \"inproceedings\", \"title\": \"A Simple Approach to Ordinal Classification\", \"authors\": \"Frank, Eibe and Hall, Mark\", \"year\": \"2001\", \"venue\": \"Proceedings of the European Conference on Machine Learning\"}, {\"key\": \"xgboost\", \"type\": \"inproceedings\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"authors\": \"Chen, Tianqi and Guestrin, Carlos\", \"year\": \"2016\", \"venue\": \"Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery an...\"}], \"tex_citations\": [{\"key\": \"mapping_llm_science\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"monitoring_ai_review\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"markovian_chains\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"grover\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"release_strategies\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"dna_gpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feat_aug_transformer\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"reliable_detection\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"intrinsic_dimension\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"diveye\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"generator_barrier\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wu_survey_2025\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"jawahar_survey\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"beyond_binary\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citet\"}, {\"key\": \"semeval2024_task8\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"paraphrase_evades\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"detection_possibilities\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"ood_baseline\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"munir_looking_glass\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"self_consuming_mad\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"curse_of_recursion\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"model_collapse_avoidable\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"strong_model_collapse\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"broken_telephone\", \"file\": \"related_work.tex\", \"line\": 35, \"command\": \"citet\"}, {\"key\": \"markovian_chains\", \"file\": \"related_work.tex\", \"line\": 36, \"command\": \"citet\"}, {\"key\": \"curious_decline\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"writing_diversity\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"stamatatos_survey\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"koppel_authorship\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 46, \"command\": \"citet\"}, {\"key\": \"nucleus_sampling\", \"file\": \"related_work.tex\", \"line\": 48, \"command\": \"citet\"}, {\"key\": \"dsir\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"qurating\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"ccnet\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"watermark_llm\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"synthid_text\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"aaronson_watermark\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"chainwash\", \"file\": \"related_work.tex\", \"line\": 58, \"command\": \"citet\"}, {\"key\": \"min_k_percent\", \"file\": \"related_work.tex\", \"line\": 60, \"command\": \"citet\"}, {\"key\": \"pythia\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"olmo\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"qwen3\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"method.tex\", \"line\": 49, \"command\": \"cite\"}, {\"key\": \"xgboost\", \"file\": \"method.tex\", \"line\": 72, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"method.tex\", \"line\": 78, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"method.tex\", \"line\": 78, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"method.tex\", \"line\": 90, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"results.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"results.tex\", \"line\": 60, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"discussion.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"discussion.tex\", \"line\": 24, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 34, \"command\": \"cite\"}, {\"key\": \"curse_of_recursion\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"strong_model_collapse\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 37, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"detectgpt\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"status\": \"not_found\", \"confidence\": 0.382, \"matched_title\": \"Regulating ChatGPT and other Large Generative AI Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"gltr\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dna_gpt\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"binoculars\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fast_detectgpt\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ld_score\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"intrinsic_dimension\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"diveye\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Diversity Boosts AI-Generated Text Detection\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"generator_barrier\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feat_aug_transformer\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reliable_detection\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"status\": \"not_found\", \"confidence\": 0.344, \"matched_title\": \"2015 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"paraphrase_evades\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"detection_possibilities\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"status\": \"not_found\", \"confidence\": 0.253, \"matched_title\": \"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"grover\", \"title\": \"Defending Against Neural Fake News\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Defending Against Neural Fake News\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"release_strategies\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Release Strategies and the Social Impacts of Language Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"beyond_binary\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"semeval2024_task8\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"self_consuming_mad\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Consuming Generative Models go MAD\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=alemohammad vs api=casco-rodriguez\"], \"note\": \"\"}, {\"key\": \"curse_of_recursion\", \"title\": \"AI models collapse when trained on recursively generated data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AI models collapse when trained on recursively generated data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"strong_model_collapse\", \"title\": \"Strong Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Strong Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"model_collapse_avoidable\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ood_baseline\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dsir\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Data Selection for Language Models via Importance Resampling\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qurating\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ccnet\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"watermark_llm\", \"title\": \"A Watermark for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Watermark for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"synthid_text\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable watermarking for identifying large language model outputs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"aaronson_watermark\", \"title\": \"Watermarking GPT Outputs\", \"status\": \"not_found\", \"confidence\": 0.418, \"matched_title\": \"Undetectable Watermarks for Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.42 below threshold 0.82\"}, {\"key\": \"chainwash\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"curious_decline\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"writing_diversity\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nucleus_sampling\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mapping_llm_science\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"monitoring_ai_review\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stamatatos_survey\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A survey of modern authorship attribution methods\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"koppel_authorship\", \"title\": \"Computational Methods in Authorship Attribution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Computational methods in authorship attribution\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uchendu_attribution\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Authorship Attribution for Neural Text Generation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"munir_looking_glass\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"broken_telephone\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"markovian_chains\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Markovian Generation Chains in Large Language Models\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"min_k_percent\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Detecting Pretraining Data from Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wu_survey_2025\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jawahar_survey\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pythia\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"status\": \"not_found\", \"confidence\": 0.497, \"matched_title\": \"The TRIPOD-LLM reporting guideline for studies using large language models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"olmo\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OLMo: Accelerating the Science of Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"coral_ordinal\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rank consistent ordinal regression for neural networks with application to age estimation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frank_hall_ordinal\", \"title\": \"A Simple Approach to Ordinal Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple Approach to Ordinal Classification\", \"matched_year\": \"2001\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xgboost\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"status\": \"not_found\", \"confidence\": 0.298, \"matched_title\": \"XGBoost\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}]}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "9aa3eb11-66b9-4609-b838-a8349ce12f81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "leafUuid": "87b6711a-b554-4191-bc26-3656c303b738",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit references.bib for accuracy and hallucinations",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Assistant

_source line 23 · 2026-05-15T23:59:30.867Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the OpenAlex results. I have:

**not_found (6)**:
1. `detectgpt` - OpenAlex didn't find it, but this is a very well-known paper (Mitchell et al., ICML 2023). This is an OpenAlex search limitation.
2. `reliable_detection` - Sadasivan et al. OpenAlex didn't find it, but it's a well-known paper.
3. `detection_possibilities` - Chakraborty et al. ICML 2024. OpenAlex search issue.


4. `aaronson_watermark` - This is a blog post/talk rather than a formal paper, so OpenAlex won't have it.
5. `pythia` - Very well-known paper (Biderman et al., ICML 2023) that OpenAlex is missing.
6. `xgboost` - Very well-known paper (Chen & Guestrin, KDD 2016) that OpenAlex is also missing.

**mismatch (2)**:
1. `self_consuming_mad` - OpenAlex has year=2023 while the bibliography says 2024, and there's a first author discrepancy between Alemohammad and Casco-Rodriguez that I need to verify.
2. `qwen3` - The first author differs because the bibliography lists "{Qwen Team}" while OpenAlex parsed it as Yang.

Looking at year discrepancies across the verified OpenAlex entries, I'm seeing a pattern where several papers have different years in the bibliography versus OpenAlex—likely due to preprint versus published versions. The entries like `dna_gpt`, `fast_detectgpt`, `writing_diversity`, and `nucleus_sampling` show this pattern, while others like `diveye`, `ood_baseline`, and `ccnet` have more significant year gaps that warrant investigation.

I should prioritize web searches for the entries that are either not found or have mismatches, starting with the most critical ones to verify the correct publication years.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87b6711a-b554-4191-bc26-3656c303b738",
  "isSidechain": false,
  "requestId": "req_011Cb5GCWw8h4tm5obEaygyL",
  "type": "assistant",
  "uuid": "ffc2584f-d925-42a0-b66d-436044181d25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019y5cix1Vm4DGaV2RLtwxvT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13517,
      "cache_read_input_tokens": 34305,
      "output_tokens": 3667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3667,
          "cache_read_input_tokens": 34305,
          "cache_creation_input_tokens": 13517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13517
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

_source line 24 · 2026-05-15T23:59:32.352Z_

OpenAlex 报告：41 verified, 6 not_found, 2 mismatch。还有多条年份可能不一致。现在用 WebSearch 逐条验证所有可疑条目。

先验证 6 个 not_found + 2 个 mismatch，以及 OpenAlex 返回年份与 bib 不一致的条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffc2584f-d925-42a0-b66d-436044181d25",
  "isSidechain": false,
  "requestId": "req_011Cb5GCWw8h4tm5obEaygyL",
  "type": "assistant",
  "uuid": "30aa605d-9b84-41a3-869d-4688db36b0df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019y5cix1Vm4DGaV2RLtwxvT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13517,
      "cache_read_input_tokens": 34305,
      "output_tokens": 3667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3667,
          "cache_read_input_tokens": 34305,
          "cache_creation_input_tokens": 13517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13517
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

_source line 25 · 2026-05-15T23:59:44.489Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015qtuXZaLvJjFpcwfBu7UE5`</summary>

```json
{
  "description": "Verify batch 1: not_found entries",
  "prompt": "I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) all authors (full list), (3) year of publication, (4) venue/journal. Report any discrepancies from what the bib file claims.\n\nPapers to verify:\n\n1. **detectgpt** — bib claims: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea, ICML 2023\n\n2. **reliable_detection** — bib claims: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil, TMLR 2025\n\n3. **detection_possibilities** — bib claims: \"Position: On the Possibilities of AI-Generated Text Detection\", Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong, ICML 2024\n\n4. **aaronson_watermark** — bib claims: \"Watermarking GPT Outputs\", Aaronson, Scott and Kirchner, Hendrik, 2022, Technical Talk\n\n5. **pythia** — bib claims: \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar, ICML 2023\n\n6. **xgboost** — bib claims: \"XGBoost: A Scalable Tree Boosting System\", Chen, Tianqi and Guestrin, Carlos, KDD 2016\n\nReport all findings precisely, including any year, author, or venue discrepancies.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30aa605d-9b84-41a3-869d-4688db36b0df",
  "isSidechain": false,
  "requestId": "req_011Cb5GCWw8h4tm5obEaygyL",
  "type": "assistant",
  "uuid": "5b722315-6b83-44e9-a00c-c70017944576",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019y5cix1Vm4DGaV2RLtwxvT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13517,
      "cache_read_input_tokens": 34305,
      "output_tokens": 3667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3667,
          "cache_read_input_tokens": 34305,
          "cache_creation_input_tokens": 13517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13517
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

_source line 26 · 2026-05-15T23:59:59.740Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MfNwpzXjZ5JJuaohdfNX9D`</summary>

```json
{
  "description": "Verify batch 2: mismatches + year discrepancies",
  "prompt": "I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) first author and author list, (3) year of publication (conference proceedings year, not arXiv preprint year), (4) venue. Report any discrepancies from what the bib file claims.\n\n**Mismatch entries:**\n\n1. **self_consuming_mad** — bib claims: \"Self-Consuming Generative Models Go MAD\", Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G., ICLR 2024. OpenAlex says year=2023, first_author=Casco-Rodriguez.\n\n2. **qwen3** — bib claims: \"Qwen3 Technical Report\", {Qwen Team}, arXiv:2505.09388, 2025. OpenAlex says first_author=Yang. Check if there's a specific author list or if team authorship is standard.\n\n**Year discrepancy entries (OpenAlex verified year differs from bib year):**\n\n3. **dna_gpt** — bib=2024, OpenAlex=2023. \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", Yang et al., ICLR 2024.\n\n4. **fast_detectgpt** — bib=2024, OpenAlex=2023. \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", Bao et al., ICLR 2024.\n\n5. **diveye** — bib=2026, OpenAlex=2025. \"Diversity Boosts AI-Generated Text Detection\", Basani, Advik Raj and Chen, Pin-Yu, TMLR.\n\n6. **ood_baseline** — bib=2017, OpenAlex=2016. \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", Hendrycks, Dan and Gimpel, Kevin, ICLR 2017.\n\n7. **ccnet** — bib=2020, OpenAlex=2019. \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", Wenzek et al., LREC 2020.\n\n8. **writing_diversity** — bib=2024, OpenAlex=2023. \"Does Writing with Language Models Reduce Content Diversity?\", Padmakumar, Vishakh and He, He, ICLR 2024.\n\n9. **nucleus_sampling** — bib=2020, OpenAlex=2019. \"The Curious Case of Neural Text Degeneration\", Holtzman et al., ICLR 2020.\n\n10. **min_k_percent** — bib=2024, OpenAlex=2023. \"Detecting Pretraining Data from Large Language Models\", Shi et al., ICLR 2024.\n\n11. **stamatatos_survey** — bib=2009, OpenAlex=2008. \"A Survey of Modern Authorship Attribution Methods\", Stamatatos, Efstathios, JASIST.\n\n12. **koppel_authorship** — bib=2009, OpenAlex=2008. \"Computational Methods in Authorship Attribution\", Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo, JASIST.\n\n13. **strong_model_collapse** — bib=2025, OpenAlex=2024. \"Strong Model Collapse\", Dohmatob et al., ICLR 2025.\n\nFor each, confirm the correct publication year (use conference year, not arXiv year) and report whether the bib entry is correct or needs updating.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b722315-6b83-44e9-a00c-c70017944576",
  "isSidechain": false,
  "requestId": "req_011Cb5GCWw8h4tm5obEaygyL",
  "type": "assistant",
  "uuid": "a29433b9-d67b-473e-8479-05890da1b7a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019y5cix1Vm4DGaV2RLtwxvT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13517,
      "cache_read_input_tokens": 34305,
      "output_tokens": 3667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3667,
          "cache_read_input_tokens": 34305,
          "cache_creation_input_tokens": 13517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13517
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

_source line 27 · 2026-05-16T00:00:22.708Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01CdrqHc4AbBgAzr45qMtpJW`</summary>

```json
{
  "description": "Verify batch 3: 2024-2026 recent papers",
  "prompt": "I need you to verify the following recent (2024-2026) academic paper citations using WebSearch. Recent papers are most likely to have hallucinated information in LLM-generated bib entries. For each paper, search for it and confirm: (1) exact title, (2) authors (especially check for hallucinated/incorrect authors), (3) year of publication, (4) venue. Report any discrepancies.\n\n1. **binoculars** — \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom, ICML 2024\n\n2. **ld_score** — \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul, arXiv:2605.01647, 2026\n\n3. **generator_barrier** — \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli, arXiv:2604.13692, 2026\n\n4. **feat_aug_transformer** — \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", Mady, Mohamed and Reschke, Johannes and Schuller, Björn, arXiv:2605.03969, 2026\n\n5. **chainwash** — \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul, arXiv:2605.05503, 2026\n\n6. **markovian_chains** — \"Markovian Generation Chains in Large Language Models\", Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry, arXiv:2603.11228, 2026\n\n7. **broken_telephone** — \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan, ACL 2025\n\n8. **beyond_binary** — \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou, WWW 2025\n\n9. **semeval2024_task8** — \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav, SemEval 2024\n\n10. **wu_survey_2025** — \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai, Computational Linguistics (MIT Press) 2025\n\n11. **reliable_detection** — \"Can AI-Generated Text be Reliably Detected?\", Sadasivan et al., TMLR 2025. Was this first published as arXiv preprint? What year?\n\nReport all findings precisely.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a29433b9-d67b-473e-8479-05890da1b7a7",
  "isSidechain": false,
  "requestId": "req_011Cb5GCWw8h4tm5obEaygyL",
  "type": "assistant",
  "uuid": "1c63f942-1f72-4461-b78e-61dcc3b8b681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019y5cix1Vm4DGaV2RLtwxvT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13517,
      "cache_read_input_tokens": 34305,
      "output_tokens": 3667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3667,
          "cache_read_input_tokens": 34305,
          "cache_creation_input_tokens": 13517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13517
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

_source line 28 · 2026-05-16T00:01:16.797Z_

<details><summary>↩ Tool result · `toolu_015qtuXZaLvJjFpcwfBu7UE5`</summary>

```text
Now I have enough information. Let me also confirm the exact title in the TMLR version (the bib says the shorter title but TMLR used a longer "Stress Testing" title).

Here are the verification results for all 6 papers:

---

## 1. `detectgpt`

**Bib claims:** "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature", Mitchell/Lee/Khazatsky/Manning/Finn, ICML 2023

**Verified:** All details are **correct**.
- Title: exact match
- Authors: Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn -- correct
- Venue: ICML 2023 (Proceedings of Machine Learning Research, v202) -- correct
- No discrepancies.

---

## 2. `reliable_detection`

**Bib claims:** "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks", Sadasivan/Kumar/Balasubramanian/Wang/Feizi, TMLR 2025

**Verified:** All details are **correct**.
- Title: The TMLR-accepted version uses the full title "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" -- matches bib
- Authors: Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi -- correct
- Venue: TMLR (Transactions on Machine Learning Research) -- correct
- Year: The TMLR acceptance announcement was posted on March 13, 2025 (via the @TmlrPub tweet). The bib says 2025 -- **correct**
- Note: The earlier arXiv version (2303.11156) had a shorter title ("Can AI-Generated Text be Reliably Detected?") and was first posted in 2023. The TMLR-published version added the "Stress Testing..." subtitle.
- No discrepancies.

---

## 3. `detection_possibilities`

**Bib claims:** "Position: On the Possibilities of AI-Generated Text Detection", Chakraborty/Bedi/Zhu/An/Manocha/Huang, ICML 2024

**Verified:** All details are **correct**.
- Title: exact match (published as a Position paper at ICML 2024)
- Authors: Souradip Chakraborty, Amrit Singh Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, Furong Huang -- correct
- Venue: ICML 2024 (Proceedings of the 41st ICML, pages 6093-6115) -- correct
- No discrepancies.

---

## 4. `aaronson_watermark`

**Bib claims:** "Watermarking GPT Outputs", Aaronson/Kirchner, 2022, Technical Talk

**Verified:** All details are **correct**.
- Title: "Watermarking GPT Outputs" -- matches the title on Aaronson's talks page and blog post
- Authors: Scott Aaronson and Hendrik Kirchner (Kirchner was the OpenAI engineer who built the prototype) -- correct
- Year: 2022 -- correct (the talk was given at UT Austin Math Club on Oct 18, 2022; at UT Austin EA Club on Nov 14, 2022; and at OpenAI SF on Dec 13, 2022)
- Type: Technical Talk / `@misc` -- correct. This was never published as a formal paper; it remains a talk/blog post (scottaaronson.blog/?p=6823)
- No discrepancies.

---

## 5. `pythia`

**Bib claims:** "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling", Biderman/Schoelkopf/Anthony(Quentin Gregory)/Bradley/O'Brien/Hallahan/Khan/Purohit/Prashanth(USVSN Sai)/Raff/Skowron/Sutawika/van der Wal, ICML 2023

**Verified:** All details are **correct**.
- Title: exact match
- Authors (full list from DBLP/PMLR proceedings): Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, Aviya Skowron, Lintang Sutawika, Oskar van der Wal -- all 13 authors match
- Venue: ICML 2023 (PMLR v202, pages 2397-2430) -- correct
- No discrepancies.

---

## 6. `xgboost`

**Bib claims:** "XGBoost: A Scalable Tree Boosting System", Chen/Guestrin, KDD 2016

**Verified:** All details are **correct**.
- Title: exact match
- Authors: Tianqi Chen and Carlos Guestrin -- correct
- Venue: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2016), pages 785-794 -- correct
- No discrepancies.

---

## Summary

**All 6 citations are accurate.** No discrepancies were found in titles, author lists, venues, or years. The bib entries faithfully represent the published records.

Sources:
- [DetectGPT - ICML Proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)
- [DetectGPT - arXiv](https://arxiv.org/abs/2301.11305)
- [Reliable Detection - OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt)
- [Reliable Detection - TMLR Announcement](https://x.com/TmlrPub/status/1900336120296034775)
- [Detection Possibilities - ICML Proceedings](https://proceedings.mlr.press/v235/chakraborty24a.html)
- [Aaronson Watermark - Blog Post](https://scottaaronson.blog/?p=6823)
- [Aaronson Talks Page](https://www.scottaaronson.com/talks/)
- [Pythia - DBLP](https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html)
- [Pythia - ICML Proceedings](https://proceedings.mlr.press/v202/biderman23a.html)
- [XGBoost - ACM DL](https://dl.acm.org/doi/10.1145/2939672.2939785)
- [XGBoost - arXiv](https://arxiv.org/abs/1603.02754)

agentId: a4dc224666d3c663a (use SendMessage with to: 'a4dc224666d3c663a' to continue this agent)
&lt;usage>total_tokens: 39963
tool_uses: 18
duration_ms: 92303&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b722315-6b83-44e9-a00c-c70017944576",
  "isSidechain": false,
  "promptId": "717c1a5f-05be-403b-aa0c-e27dacf66b17",
  "type": "user",
  "uuid": "beeb6883-37a0-4546-a755-acc984635aa9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) all authors (full list), (3) year of publication, (4) venue/journal. Report any discrepancies from what the bib file claims.\n\nPapers to verify:\n\n1. **detectgpt** — bib claims: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea, ICML 2023\n\n2. **reliable_detection** — bib claims: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil, TMLR 2025\n\n3. **detection_possibilities** — bib claims: \"Position: On the Possibilities of AI-Generated Text Detection\", Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong, ICML 2024\n\n4. **aaronson_watermark** — bib claims: \"Watermarking GPT Outputs\", Aaronson, Scott and Kirchner, Hendrik, 2022, Technical Talk\n\n5. **pythia** — bib claims: \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar, ICML 2023\n\n6. **xgboost** — bib claims: \"XGBoost: A Scalable Tree Boosting System\", Chen, Tianqi and Guestrin, Carlos, KDD 2016\n\nReport all findings precisely, including any year, author, or venue discrepancies.",
    "agentId": "a4dc224666d3c663a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information. Let me also confirm the exact title in the TMLR version (the bib says the shorter title but TMLR used a longer \"Stress Testing\" title).\n\nHere are the verification results for all 6 papers:\n\n---\n\n## 1. `detectgpt`\n\n**Bib claims:** \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", Mitchell/Lee/Khazatsky/Manning/Finn, ICML 2023\n\n**Verified:** All details are **correct**.\n- Title: exact match\n- Authors: Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn -- correct\n- Venue: ICML 2023 (Proceedings of Machine Learning Research, v202) -- correct\n- No discrepancies.\n\n---\n\n## 2. `reliable_detection`\n\n**Bib claims:** \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", Sadasivan/Kumar/Balasubramanian/Wang/Feizi, TMLR 2025\n\n**Verified:** All details are **correct**.\n- Title: The TMLR-accepted version uses the full title \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\" -- matches bib\n- Authors: Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi -- correct\n- Venue: TMLR (Transactions on Machine Learning Research) -- correct\n- Year: The TMLR acceptance announcement was posted on March 13, 2025 (via the @TmlrPub tweet). The bib says 2025 -- **correct**\n- Note: The earlier arXiv version (2303.11156) had a shorter title (\"Can AI-Generated Text be Reliably Detected?\") and was first posted in 2023. The TMLR-published version added the \"Stress Testing...\" subtitle.\n- No discrepancies.\n\n---\n\n## 3. `detection_possibilities`\n\n**Bib claims:** \"Position: On the Possibilities of AI-Generated Text Detection\", Chakraborty/Bedi/Zhu/An/Manocha/Huang, ICML 2024\n\n**Verified:** All details are **correct**.\n- Title: exact match (published as a Position paper at ICML 2024)\n- Authors: Souradip Chakraborty, Amrit Singh Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, Furong Huang -- correct\n- Venue: ICML 2024 (Proceedings of the 41st ICML, pages 6093-6115) -- correct\n- No discrepancies.\n\n---\n\n## 4. `aaronson_watermark`\n\n**Bib claims:** \"Watermarking GPT Outputs\", Aaronson/Kirchner, 2022, Technical Talk\n\n**Verified:** All details are **correct**.\n- Title: \"Watermarking GPT Outputs\" -- matches the title on Aaronson's talks page and blog post\n- Authors: Scott Aaronson and Hendrik Kirchner (Kirchner was the OpenAI engineer who built the prototype) -- correct\n- Year: 2022 -- correct (the talk was given at UT Austin Math Club on Oct 18, 2022; at UT Austin EA Club on Nov 14, 2022; and at OpenAI SF on Dec 13, 2022)\n- Type: Technical Talk / `@misc` -- correct. This was never published as a formal paper; it remains a talk/blog post (scottaaronson.blog/?p=6823)\n- No discrepancies.\n\n---\n\n## 5. `pythia`\n\n**Bib claims:** \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", Biderman/Schoelkopf/Anthony(Quentin Gregory)/Bradley/O'Brien/Hallahan/Khan/Purohit/Prashanth(USVSN Sai)/Raff/Skowron/Sutawika/van der Wal, ICML 2023\n\n**Verified:** All details are **correct**.\n- Title: exact match\n- Authors (full list from DBLP/PMLR proceedings): Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, Aviya Skowron, Lintang Sutawika, Oskar van der Wal -- all 13 authors match\n- Venue: ICML 2023 (PMLR v202, pages 2397-2430) -- correct\n- No discrepancies.\n\n---\n\n## 6. `xgboost`\n\n**Bib claims:** \"XGBoost: A Scalable Tree Boosting System\", Chen/Guestrin, KDD 2016\n\n**Verified:** All details are **correct**.\n- Title: exact match\n- Authors: Tianqi Chen and Carlos Guestrin -- correct\n- Venue: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD 2016), pages 785-794 -- correct\n- No discrepancies.\n\n---\n\n## Summary\n\n**All 6 citations are accurate.** No discrepancies were found in titles, author lists, venues, or years. The bib entries faithfully represent the published records.\n\nSources:\n- [DetectGPT - ICML Proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)\n- [DetectGPT - arXiv](https://arxiv.org/abs/2301.11305)\n- [Reliable Detection - OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt)\n- [Reliable Detection - TMLR Announcement](https://x.com/TmlrPub/status/1900336120296034775)\n- [Detection Possibilities - ICML Proceedings](https://proceedings.mlr.press/v235/chakraborty24a.html)\n- [Aaronson Watermark - Blog Post](https://scottaaronson.blog/?p=6823)\n- [Aaronson Talks Page](https://www.scottaaronson.com/talks/)\n- [Pythia - DBLP](https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html)\n- [Pythia - ICML Proceedings](https://proceedings.mlr.press/v202/biderman23a.html)\n- [XGBoost - ACM DL](https://dl.acm.org/doi/10.1145/2939672.2939785)\n- [XGBoost - arXiv](https://arxiv.org/abs/1603.02754)"
      }
    ],
    "totalDurationMs": 92303,
    "totalTokens": 39963,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1655,
      "cache_read_input_tokens": 36558,
      "output_tokens": 1749,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1655
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1749,
          "cache_read_input_tokens": 36558,
          "cache_creation_input_tokens": 1655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1655,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 1,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "5b722315-6b83-44e9-a00c-c70017944576",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "leafUuid": "beeb6883-37a0-4546-a755-acc984635aa9",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit references.bib for accuracy and hallucinations",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Tool result

_source line 31 · 2026-05-16T00:01:34.769Z_

<details><summary>↩ Tool result · `toolu_01MfNwpzXjZ5JJuaohdfNX9D`</summary>

```text
I now have all the information needed. Here is my comprehensive verification report:

---

## Citation Verification Results

### 1. self_consuming_mad -- BIB IS CORRECT

- **Title**: "Self-Consuming Generative Models Go MAD" -- CORRECT
- **First author**: Alemohammad, Sina -- CORRECT. The arXiv listing, Semantic Scholar, and ICLR proceedings all list Alemohammad as first author. OpenAlex's claim that Casco-Rodriguez is first author is wrong.
- **Author list**: Correct as listed in bib
- **Year**: 2024 -- CORRECT. Published at ICLR 2024 (Vienna). The arXiv preprint was July 2023, which explains OpenAlex showing 2023.
- **Venue**: ICLR 2024 -- CORRECT
- **Verdict**: No changes needed.

### 2. qwen3 -- BIB IS CORRECT

- **Title**: "Qwen3 Technical Report" -- CORRECT
- **Author**: `{Qwen Team}` -- CORRECT. The official arXiv BibTeX and HuggingFace both use "Qwen Team" as the corporate author. While there are 60+ individual contributors (with An Yang listed first alphabetically), the standard citation convention for this paper is the team name.
- **Year**: 2025 -- CORRECT (arXiv preprint May 2025, no conference proceedings)
- **Venue**: arXiv:2505.09388 -- CORRECT
- **Verdict**: No changes needed. OpenAlex listing "Yang" as first author reflects the individual author list, but {Qwen Team} is the standard citation form.

### 3. dna_gpt -- BIB IS CORRECT (year=2024)

- **Title**: Correct
- **Authors**: Yang, Xianjun et al. -- Correct
- **Year**: 2024 -- CORRECT. This is an ICLR 2024 paper (poster). The arXiv preprint was May 2023, which explains OpenAlex showing 2023. The conference proceedings year is 2024.
- **Venue**: ICLR 2024 -- CORRECT
- **Verdict**: No changes needed.

### 4. fast_detectgpt -- BIB IS CORRECT (year=2024)

- **Title**: Correct
- **Authors**: Bao, Guangsheng et al. -- Correct
- **Year**: 2024 -- CORRECT. ICLR 2024 poster. ArXiv preprint October 2023 explains the OpenAlex discrepancy.
- **Venue**: ICLR 2024 -- CORRECT
- **Verdict**: No changes needed.

### 5. diveye -- BIB IS CORRECT (year=2026)

- **Title**: Correct
- **Authors**: Basani, Advik Raj and Chen, Pin-Yu -- Correct
- **Year**: 2026 -- CORRECT. Published in TMLR February 2026 (the GitHub repo is tagged `[TMLR '26]` and the arXiv PDF header reads "Published in Transactions on Machine Learning Research (02/2026)"). The arXiv preprint was September 2025, which explains OpenAlex showing 2025.
- **Venue**: TMLR -- CORRECT
- **Verdict**: No changes needed.

### 6. ood_baseline -- BIB IS CORRECT (year=2017)

- **Title**: Correct
- **Authors**: Hendrycks, Dan and Gimpel, Kevin -- Correct
- **Year**: 2017 -- CORRECT. This is an ICLR 2017 paper (DBLP key: `conf/iclr/HendrycksG17`). The arXiv preprint was October 2016, which explains OpenAlex showing 2016. The conference proceedings year is 2017.
- **Venue**: ICLR 2017 -- CORRECT
- **Verdict**: No changes needed.

### 7. ccnet -- BIB IS CORRECT (year=2020)

- **Title**: Correct
- **Authors**: Wenzek, Guillaume et al. -- Correct
- **Year**: 2020 -- CORRECT. Published in LREC 2020 proceedings (ACL Anthology: `2020.lrec-1.494`). The arXiv preprint was November 2019, explaining OpenAlex's 2019.
- **Venue**: LREC 2020 -- CORRECT
- **Verdict**: No changes needed.

### 8. writing_diversity -- BIB IS CORRECT (year=2024)

- **Title**: Correct
- **Authors**: Padmakumar, Vishakh and He, He -- Correct
- **Year**: 2024 -- CORRECT. ICLR 2024 poster. ArXiv preprint September 2023 explains OpenAlex's 2023.
- **Venue**: ICLR 2024 -- CORRECT
- **Verdict**: No changes needed.

### 9. nucleus_sampling -- BIB IS CORRECT (year=2020)

- **Title**: "The Curious Case of Neural Text Degeneration" -- Correct
- **Authors**: Holtzman, Ari et al. -- Correct
- **Year**: 2020 -- CORRECT. ICLR 2020 paper (OpenReview ID: `rygGQyrFvH`). ArXiv preprint April 2019 explains OpenAlex's 2019.
- **Venue**: ICLR 2020 -- CORRECT
- **Verdict**: No changes needed.

### 10. min_k_percent -- BIB IS CORRECT (year=2024)

- **Title**: Correct
- **Authors**: Shi, Weijia et al. -- Correct
- **Year**: 2024 -- CORRECT. ICLR 2024 paper (OpenReview ID: `zWqr3MQuNs`). ArXiv preprint October 2023 explains OpenAlex's 2023.
- **Venue**: ICLR 2024 -- CORRECT
- **Verdict**: No changes needed.

### 11. stamatatos_survey -- BIB IS CORRECT (year=2009)

- **Title**: Correct
- **Authors**: Stamatatos, Efstathios -- Correct
- **Year**: 2009 -- CORRECT. Published in JASIST volume 60, issue 3, pages 538-556, March 2009. It was available online first on December 16, 2008, which explains OpenAlex showing 2008. The standard citation year for journal articles is the volume/issue publication year, which is 2009.
- **Venue**: JASIST -- CORRECT
- **Verdict**: No changes needed.

### 12. koppel_authorship -- BIB IS CORRECT (year=2009)

- **Title**: Correct
- **Authors**: Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo -- Correct
- **Year**: 2009 -- CORRECT. Published in JASIST volume 60, issue 1, pages 9-26, January 2009. It was published online first on September 26, 2008, explaining OpenAlex's 2008. The correct citation year is 2009.
- **Venue**: JASIST -- CORRECT
- **Verdict**: No changes needed.

### 13. strong_model_collapse -- BIB IS CORRECT (year=2025)

- **Title**: Correct
- **Authors**: Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia -- Correct
- **Year**: 2025 -- CORRECT. Published as an ICLR 2025 conference paper (Spotlight). ArXiv preprint October 2024 explains OpenAlex showing 2024.
- **Venue**: ICLR 2025 -- CORRECT
- **Verdict**: No changes needed.

---

## Summary

All 13 bib entries are **correct as-is**. In every case, the OpenAlex year discrepancy is explained by OpenAlex using the arXiv preprint date or online-first date rather than the official conference proceedings / journal volume year. The bib file consistently and correctly uses the conference/journal publication year, which is the standard academic citation practice. No updates are needed.

agentId: abd348b8cf003e5f5 (use SendMessage with to: 'abd348b8cf003e5f5' to continue this agent)
&lt;usage>total_tokens: 45533
tool_uses: 22
duration_ms: 95027&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a29433b9-d67b-473e-8479-05890da1b7a7",
  "isSidechain": false,
  "promptId": "717c1a5f-05be-403b-aa0c-e27dacf66b17",
  "type": "user",
  "uuid": "5bd78bea-0717-4047-88aa-865cdc439d29",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to verify the following academic paper citations using WebSearch. For each paper, search for it and confirm: (1) exact title, (2) first author and author list, (3) year of publication (conference proceedings year, not arXiv preprint year), (4) venue. Report any discrepancies from what the bib file claims.\n\n**Mismatch entries:**\n\n1. **self_consuming_mad** — bib claims: \"Self-Consuming Generative Models Go MAD\", Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G., ICLR 2024. OpenAlex says year=2023, first_author=Casco-Rodriguez.\n\n2. **qwen3** — bib claims: \"Qwen3 Technical Report\", {Qwen Team}, arXiv:2505.09388, 2025. OpenAlex says first_author=Yang. Check if there's a specific author list or if team authorship is standard.\n\n**Year discrepancy entries (OpenAlex verified year differs from bib year):**\n\n3. **dna_gpt** — bib=2024, OpenAlex=2023. \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", Yang et al., ICLR 2024.\n\n4. **fast_detectgpt** — bib=2024, OpenAlex=2023. \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", Bao et al., ICLR 2024.\n\n5. **diveye** — bib=2026, OpenAlex=2025. \"Diversity Boosts AI-Generated Text Detection\", Basani, Advik Raj and Chen, Pin-Yu, TMLR.\n\n6. **ood_baseline** — bib=2017, OpenAlex=2016. \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", Hendrycks, Dan and Gimpel, Kevin, ICLR 2017.\n\n7. **ccnet** — bib=2020, OpenAlex=2019. \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", Wenzek et al., LREC 2020.\n\n8. **writing_diversity** — bib=2024, OpenAlex=2023. \"Does Writing with Language Models Reduce Content Diversity?\", Padmakumar, Vishakh and He, He, ICLR 2024.\n\n9. **nucleus_sampling** — bib=2020, OpenAlex=2019. \"The Curious Case of Neural Text Degeneration\", Holtzman et al., ICLR 2020.\n\n10. **min_k_percent** — bib=2024, OpenAlex=2023. \"Detecting Pretraining Data from Large Language Models\", Shi et al., ICLR 2024.\n\n11. **stamatatos_survey** — bib=2009, OpenAlex=2008. \"A Survey of Modern Authorship Attribution Methods\", Stamatatos, Efstathios, JASIST.\n\n12. **koppel_authorship** — bib=2009, OpenAlex=2008. \"Computational Methods in Authorship Attribution\", Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo, JASIST.\n\n13. **strong_model_collapse** — bib=2025, OpenAlex=2024. \"Strong Model Collapse\", Dohmatob et al., ICLR 2025.\n\nFor each, confirm the correct publication year (use conference year, not arXiv year) and report whether the bib entry is correct or needs updating.",
    "agentId": "abd348b8cf003e5f5",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is my comprehensive verification report:\n\n---\n\n## Citation Verification Results\n\n### 1. self_consuming_mad -- BIB IS CORRECT\n\n- **Title**: \"Self-Consuming Generative Models Go MAD\" -- CORRECT\n- **First author**: Alemohammad, Sina -- CORRECT. The arXiv listing, Semantic Scholar, and ICLR proceedings all list Alemohammad as first author. OpenAlex's claim that Casco-Rodriguez is first author is wrong.\n- **Author list**: Correct as listed in bib\n- **Year**: 2024 -- CORRECT. Published at ICLR 2024 (Vienna). The arXiv preprint was July 2023, which explains OpenAlex showing 2023.\n- **Venue**: ICLR 2024 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 2. qwen3 -- BIB IS CORRECT\n\n- **Title**: \"Qwen3 Technical Report\" -- CORRECT\n- **Author**: `{Qwen Team}` -- CORRECT. The official arXiv BibTeX and HuggingFace both use \"Qwen Team\" as the corporate author. While there are 60+ individual contributors (with An Yang listed first alphabetically), the standard citation convention for this paper is the team name.\n- **Year**: 2025 -- CORRECT (arXiv preprint May 2025, no conference proceedings)\n- **Venue**: arXiv:2505.09388 -- CORRECT\n- **Verdict**: No changes needed. OpenAlex listing \"Yang\" as first author reflects the individual author list, but {Qwen Team} is the standard citation form.\n\n### 3. dna_gpt -- BIB IS CORRECT (year=2024)\n\n- **Title**: Correct\n- **Authors**: Yang, Xianjun et al. -- Correct\n- **Year**: 2024 -- CORRECT. This is an ICLR 2024 paper (poster). The arXiv preprint was May 2023, which explains OpenAlex showing 2023. The conference proceedings year is 2024.\n- **Venue**: ICLR 2024 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 4. fast_detectgpt -- BIB IS CORRECT (year=2024)\n\n- **Title**: Correct\n- **Authors**: Bao, Guangsheng et al. -- Correct\n- **Year**: 2024 -- CORRECT. ICLR 2024 poster. ArXiv preprint October 2023 explains the OpenAlex discrepancy.\n- **Venue**: ICLR 2024 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 5. diveye -- BIB IS CORRECT (year=2026)\n\n- **Title**: Correct\n- **Authors**: Basani, Advik Raj and Chen, Pin-Yu -- Correct\n- **Year**: 2026 -- CORRECT. Published in TMLR February 2026 (the GitHub repo is tagged `[TMLR '26]` and the arXiv PDF header reads \"Published in Transactions on Machine Learning Research (02/2026)\"). The arXiv preprint was September 2025, which explains OpenAlex showing 2025.\n- **Venue**: TMLR -- CORRECT\n- **Verdict**: No changes needed.\n\n### 6. ood_baseline -- BIB IS CORRECT (year=2017)\n\n- **Title**: Correct\n- **Authors**: Hendrycks, Dan and Gimpel, Kevin -- Correct\n- **Year**: 2017 -- CORRECT. This is an ICLR 2017 paper (DBLP key: `conf/iclr/HendrycksG17`). The arXiv preprint was October 2016, which explains OpenAlex showing 2016. The conference proceedings year is 2017.\n- **Venue**: ICLR 2017 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 7. ccnet -- BIB IS CORRECT (year=2020)\n\n- **Title**: Correct\n- **Authors**: Wenzek, Guillaume et al. -- Correct\n- **Year**: 2020 -- CORRECT. Published in LREC 2020 proceedings (ACL Anthology: `2020.lrec-1.494`). The arXiv preprint was November 2019, explaining OpenAlex's 2019.\n- **Venue**: LREC 2020 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 8. writing_diversity -- BIB IS CORRECT (year=2024)\n\n- **Title**: Correct\n- **Authors**: Padmakumar, Vishakh and He, He -- Correct\n- **Year**: 2024 -- CORRECT. ICLR 2024 poster. ArXiv preprint September 2023 explains OpenAlex's 2023.\n- **Venue**: ICLR 2024 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 9. nucleus_sampling -- BIB IS CORRECT (year=2020)\n\n- **Title**: \"The Curious Case of Neural Text Degeneration\" -- Correct\n- **Authors**: Holtzman, Ari et al. -- Correct\n- **Year**: 2020 -- CORRECT. ICLR 2020 paper (OpenReview ID: `rygGQyrFvH`). ArXiv preprint April 2019 explains OpenAlex's 2019.\n- **Venue**: ICLR 2020 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 10. min_k_percent -- BIB IS CORRECT (year=2024)\n\n- **Title**: Correct\n- **Authors**: Shi, Weijia et al. -- Correct\n- **Year**: 2024 -- CORRECT. ICLR 2024 paper (OpenReview ID: `zWqr3MQuNs`). ArXiv preprint October 2023 explains OpenAlex's 2023.\n- **Venue**: ICLR 2024 -- CORRECT\n- **Verdict**: No changes needed.\n\n### 11. stamatatos_survey -- BIB IS CORRECT (year=2009)\n\n- **Title**: Correct\n- **Authors**: Stamatatos, Efstathios -- Correct\n- **Year**: 2009 -- CORRECT. Published in JASIST volume 60, issue 3, pages 538-556, March 2009. It was available online first on December 16, 2008, which explains OpenAlex showing 2008. The standard citation year for journal articles is the volume/issue publication year, which is 2009.\n- **Venue**: JASIST -- CORRECT\n- **Verdict**: No changes needed.\n\n### 12. koppel_authorship -- BIB IS CORRECT (year=2009)\n\n- **Title**: Correct\n- **Authors**: Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo -- Correct\n- **Year**: 2009 -- CORRECT. Published in JASIST volume 60, issue 1, pages 9-26, January 2009. It was published online first on September 26, 2008, explaining OpenAlex's 2008. The correct citation year is 2009.\n- **Venue**: JASIST -- CORRECT\n- **Verdict**: No changes needed.\n\n### 13. strong_model_collapse -- BIB IS CORRECT (year=2025)\n\n- **Title**: Correct\n- **Authors**: Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia -- Correct\n- **Year**: 2025 -- CORRECT. Published as an ICLR 2025 conference paper (Spotlight). ArXiv preprint October 2024 explains OpenAlex showing 2024.\n- **Venue**: ICLR 2025 -- CORRECT\n- **Verdict**: No changes needed.\n\n---\n\n## Summary\n\nAll 13 bib entries are **correct as-is**. In every case, the OpenAlex year discrepancy is explained by OpenAlex using the arXiv preprint date or online-first date rather than the official conference proceedings / journal volume year. The bib file consistently and correctly uses the conference/journal publication year, which is the standard academic citation practice. No updates are needed."
      }
    ],
    "totalDurationMs": 95027,
    "totalTokens": 45533,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1642,
      "cache_read_input_tokens": 41845,
      "output_tokens": 2045,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1642
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2045,
          "cache_read_input_tokens": 41845,
          "cache_creation_input_tokens": 1642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1642,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "a29433b9-d67b-473e-8479-05890da1b7a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T00:04:26.297Z_

<details><summary>↩ Tool result · `toolu_01CdrqHc4AbBgAzr45qMtpJW`</summary>

```text
Now I have all the data. Let me compile the findings.

Here is the verification report for all 11 papers:

---

## 1. binoculars
**Cited as:** "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text", Hans et al., ICML 2024

**Verdict: CORRECT.** Title, all 8 authors (Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldblum, Geiping, Goldstein), year (2024), and venue (ICML 2024 = Proceedings of the 41st International Conference on Machine Learning) all match. No discrepancies.

---

## 2. ld_score
**Cited as:** "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection", Narayanasamy, Agrawal, Faber, Alam, arXiv:2605.01647, 2026

**Verdict: CORRECT.** Title exact match. Authors (Priyadarshan Narayanasamy, Swastik Agrawal, Klint Faber, Fardina Fathmiul Alam) confirmed. arXiv ID 2605.01647 confirmed, submitted May 3, 2026. No discrepancies.

---

## 3. generator_barrier
**Cited as:** "Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection", Pu, Cheng, Yuan, Wu, Bi, arXiv:2604.13692, 2026

**Verdict: CORRECT.** Title exact match. Authors (Xiao Pu, Zepeng Cheng, Lin Yuan, Yu Wu, Xiuli Bi) confirmed. arXiv ID 2604.13692 confirmed, submitted April 15, 2026. No discrepancies.

---

## 4. feat_aug_transformer
**Cited as:** "Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators", Mady, Reschke, Schuller, arXiv:2605.03969, 2026

**Verdict: CORRECT.** Title exact match. Authors (Mohamed Mady, Johannes Reschke, Bjorn Schuller) confirmed. arXiv ID 2605.03969 confirmed, submitted May 5, 2026. No discrepancies. (Note: the umlaut on "Bjorn" should be preserved as "Bjorn W. Schuller" or "Bjorn Schuller" depending on convention.)

---

## 5. chainwash
**Cited as:** "Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks", Ameen, Islam, Mahmud, Hamid, arXiv:2605.05503, 2026

**Verdict: CORRECT.** Title exact match. Authors (Mohd Ruhul Ameen, Akif Islam, Nadim Mahmud, Md. Ekramul Hamid) confirmed. arXiv ID 2605.05503 confirmed. No discrepancies.

---

## 6. markovian_chains
**Cited as:** "Markovian Generation Chains in Large Language Models", Geng, Mohamed, Shang, Vazirgiannis, Poibeau, arXiv:2603.11228, 2026

**Verdict: CORRECT.** Title exact match. Authors (Mingmeng Geng, Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, Thierry Poibeau) confirmed. arXiv ID 2603.11228 confirmed, submitted March 11, 2026. No discrepancies.

---

## 7. broken_telephone
**Cited as:** "LLM as a Broken Telephone: Iterative Generation Distorts Information", Mohamed, Geng, Vazirgiannis, Shang, ACL 2025

**Verdict: CORRECT.** Title exact match. Authors (Amr Mohamed, Mingmeng Geng, Michalis Vazirgiannis, Guokan Shang) confirmed. Published in Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025), Vienna, Austria, pages 7493-7509. No discrepancies.

---

## 8. beyond_binary
**Cited as:** "Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement", Cheng, Zhou, Jiang, Wang, Li, WWW 2025

**Verdict: CORRECT.** Title exact match. Authors (Zihao Cheng, Li Zhou, Feng Jiang, Benyou Wang, Haizhou Li) confirmed. Published in Proceedings of the ACM Web Conference 2025 (WWW '25), Sydney, Australia. No discrepancies.

---

## 9. semeval2024_task8
**Cited as:** "SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection", Wang, Mansurov, Ivanov, Su, Shelmanov, Tsvigun, Afzal, Mahmoud, Puccetti, Arnold, Whitehouse, Aji, Habash, Gurevych, Nakov, SemEval 2024

**Verdict: CORRECT.** Title exact match. All 15 authors confirmed: Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, Thomas Arnold, Chenxi Whitehouse, Alham Fikri Aji, Nizar Habash, Iryna Gurevych, Preslav Nakov. Published in Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024), co-located with NAACL 2024, Mexico City. No discrepancies.

---

## 10. wu_survey_2025
**Cited as:** "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions", Wu, Yang, Zhan, Yuan, Chao, Wong, Computational Linguistics (MIT Press) 2025

**Verdict: MINOR DISCREPANCY in author name convention.** Title, arXiv ID, year, and venue are all correct. Published in Computational Linguistics, Vol. 51, No. 1, pp. 275-338, March 2025 (MIT Press). The author "Lidia Sam Chao" is cited as listed in the paper itself. However, she is more commonly known in academic databases as **"Lidia S. Chao"** (e.g., on ACL Anthology, ResearchGate, IEEE Xplore, OpenReview). "Sam" is her Chinese family name; "Lidia S. Chao" is her standard academic name form. The bib entry listing "Lidia Sam Chao" is technically what appears on some versions of the paper, so this is a very minor convention issue, not an error per se.

---

## 11. reliable_detection
**Cited as:** "Can AI-Generated Text be Reliably Detected?", Sadasivan et al., TMLR 2025

**Verdict: DISCREPANCIES FOUND.**

1. **Title:** The TMLR-published version has an extended title: **"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks"**. The original arXiv title was just "Can AI-Generated Text be Reliably Detected?" The bib entry should use the TMLR published title if citing the TMLR version.

2. **Authors:** Full author list is **Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi** (5 authors). Verify the bib entry has all five.

3. **Year / preprint history:** The arXiv preprint was first posted **March 20, 2023** (arXiv:2303.11156). The TMLR acceptance was announced **March 13, 2025** (per the TMLR Twitter/X account). So yes, it was first an arXiv 2023 preprint, with the TMLR publication in 2025. If the bib entry says "2025" for the TMLR version, that is correct for the journal publication year, but be aware the work has been circulating since 2023.

---

## Summary of discrepancies

| # | Key | Issue | Severity |
|---|-----|-------|----------|
| 10 | wu_survey_2025 | Author "Lidia Sam Chao" vs standard academic form "Lidia S. Chao" | Negligible (both forms used) |
| 11 | reliable_detection | TMLR published title adds subtitle "Stress Testing AI Text Detectors Under Various Attacks" | Medium -- should update title if citing TMLR version |
| 11 | reliable_detection | Originally arXiv preprint from March 2023 (arXiv:2303.11156), TMLR publication 2025 | Note for context |

All other entries (1-9) are verified correct with no discrepancies in title, authors, year, or venue.

agentId: a80e1c4070014e5bd (use SendMessage with to: 'a80e1c4070014e5bd' to continue this agent)
&lt;usage>total_tokens: 39355
tool_uses: 21
duration_ms: 243586&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c63f942-1f72-4461-b78e-61dcc3b8b681",
  "isSidechain": false,
  "promptId": "717c1a5f-05be-403b-aa0c-e27dacf66b17",
  "type": "user",
  "uuid": "7be820b5-d079-437d-88a3-a7300203307b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to verify the following recent (2024-2026) academic paper citations using WebSearch. Recent papers are most likely to have hallucinated information in LLM-generated bib entries. For each paper, search for it and confirm: (1) exact title, (2) authors (especially check for hallucinated/incorrect authors), (3) year of publication, (4) venue. Report any discrepancies.\n\n1. **binoculars** — \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom, ICML 2024\n\n2. **ld_score** — \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul, arXiv:2605.01647, 2026\n\n3. **generator_barrier** — \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli, arXiv:2604.13692, 2026\n\n4. **feat_aug_transformer** — \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", Mady, Mohamed and Reschke, Johannes and Schuller, Björn, arXiv:2605.03969, 2026\n\n5. **chainwash** — \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul, arXiv:2605.05503, 2026\n\n6. **markovian_chains** — \"Markovian Generation Chains in Large Language Models\", Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry, arXiv:2603.11228, 2026\n\n7. **broken_telephone** — \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan, ACL 2025\n\n8. **beyond_binary** — \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou, WWW 2025\n\n9. **semeval2024_task8** — \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav, SemEval 2024\n\n10. **wu_survey_2025** — \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai, Computational Linguistics (MIT Press) 2025\n\n11. **reliable_detection** — \"Can AI-Generated Text be Reliably Detected?\", Sadasivan et al., TMLR 2025. Was this first published as arXiv preprint? What year?\n\nReport all findings precisely.",
    "agentId": "a80e1c4070014e5bd",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data. Let me compile the findings.\n\nHere is the verification report for all 11 papers:\n\n---\n\n## 1. binoculars\n**Cited as:** \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", Hans et al., ICML 2024\n\n**Verdict: CORRECT.** Title, all 8 authors (Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldblum, Geiping, Goldstein), year (2024), and venue (ICML 2024 = Proceedings of the 41st International Conference on Machine Learning) all match. No discrepancies.\n\n---\n\n## 2. ld_score\n**Cited as:** \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", Narayanasamy, Agrawal, Faber, Alam, arXiv:2605.01647, 2026\n\n**Verdict: CORRECT.** Title exact match. Authors (Priyadarshan Narayanasamy, Swastik Agrawal, Klint Faber, Fardina Fathmiul Alam) confirmed. arXiv ID 2605.01647 confirmed, submitted May 3, 2026. No discrepancies.\n\n---\n\n## 3. generator_barrier\n**Cited as:** \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", Pu, Cheng, Yuan, Wu, Bi, arXiv:2604.13692, 2026\n\n**Verdict: CORRECT.** Title exact match. Authors (Xiao Pu, Zepeng Cheng, Lin Yuan, Yu Wu, Xiuli Bi) confirmed. arXiv ID 2604.13692 confirmed, submitted April 15, 2026. No discrepancies.\n\n---\n\n## 4. feat_aug_transformer\n**Cited as:** \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", Mady, Reschke, Schuller, arXiv:2605.03969, 2026\n\n**Verdict: CORRECT.** Title exact match. Authors (Mohamed Mady, Johannes Reschke, Bjorn Schuller) confirmed. arXiv ID 2605.03969 confirmed, submitted May 5, 2026. No discrepancies. (Note: the umlaut on \"Bjorn\" should be preserved as \"Bjorn W. Schuller\" or \"Bjorn Schuller\" depending on convention.)\n\n---\n\n## 5. chainwash\n**Cited as:** \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", Ameen, Islam, Mahmud, Hamid, arXiv:2605.05503, 2026\n\n**Verdict: CORRECT.** Title exact match. Authors (Mohd Ruhul Ameen, Akif Islam, Nadim Mahmud, Md. Ekramul Hamid) confirmed. arXiv ID 2605.05503 confirmed. No discrepancies.\n\n---\n\n## 6. markovian_chains\n**Cited as:** \"Markovian Generation Chains in Large Language Models\", Geng, Mohamed, Shang, Vazirgiannis, Poibeau, arXiv:2603.11228, 2026\n\n**Verdict: CORRECT.** Title exact match. Authors (Mingmeng Geng, Amr Mohamed, Guokan Shang, Michalis Vazirgiannis, Thierry Poibeau) confirmed. arXiv ID 2603.11228 confirmed, submitted March 11, 2026. No discrepancies.\n\n---\n\n## 7. broken_telephone\n**Cited as:** \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", Mohamed, Geng, Vazirgiannis, Shang, ACL 2025\n\n**Verdict: CORRECT.** Title exact match. Authors (Amr Mohamed, Mingmeng Geng, Michalis Vazirgiannis, Guokan Shang) confirmed. Published in Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025), Vienna, Austria, pages 7493-7509. No discrepancies.\n\n---\n\n## 8. beyond_binary\n**Cited as:** \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", Cheng, Zhou, Jiang, Wang, Li, WWW 2025\n\n**Verdict: CORRECT.** Title exact match. Authors (Zihao Cheng, Li Zhou, Feng Jiang, Benyou Wang, Haizhou Li) confirmed. Published in Proceedings of the ACM Web Conference 2025 (WWW '25), Sydney, Australia. No discrepancies.\n\n---\n\n## 9. semeval2024_task8\n**Cited as:** \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", Wang, Mansurov, Ivanov, Su, Shelmanov, Tsvigun, Afzal, Mahmoud, Puccetti, Arnold, Whitehouse, Aji, Habash, Gurevych, Nakov, SemEval 2024\n\n**Verdict: CORRECT.** Title exact match. All 15 authors confirmed: Yuxia Wang, Jonibek Mansurov, Petar Ivanov, Jinyan Su, Artem Shelmanov, Akim Tsvigun, Osama Mohammed Afzal, Tarek Mahmoud, Giovanni Puccetti, Thomas Arnold, Chenxi Whitehouse, Alham Fikri Aji, Nizar Habash, Iryna Gurevych, Preslav Nakov. Published in Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024), co-located with NAACL 2024, Mexico City. No discrepancies.\n\n---\n\n## 10. wu_survey_2025\n**Cited as:** \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", Wu, Yang, Zhan, Yuan, Chao, Wong, Computational Linguistics (MIT Press) 2025\n\n**Verdict: MINOR DISCREPANCY in author name convention.** Title, arXiv ID, year, and venue are all correct. Published in Computational Linguistics, Vol. 51, No. 1, pp. 275-338, March 2025 (MIT Press). The author \"Lidia Sam Chao\" is cited as listed in the paper itself. However, she is more commonly known in academic databases as **\"Lidia S. Chao\"** (e.g., on ACL Anthology, ResearchGate, IEEE Xplore, OpenReview). \"Sam\" is her Chinese family name; \"Lidia S. Chao\" is her standard academic name form. The bib entry listing \"Lidia Sam Chao\" is technically what appears on some versions of the paper, so this is a very minor convention issue, not an error per se.\n\n---\n\n## 11. reliable_detection\n**Cited as:** \"Can AI-Generated Text be Reliably Detected?\", Sadasivan et al., TMLR 2025\n\n**Verdict: DISCREPANCIES FOUND.**\n\n1. **Title:** The TMLR-published version has an extended title: **\"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\"**. The original arXiv title was just \"Can AI-Generated Text be Reliably Detected?\" The bib entry should use the TMLR published title if citing the TMLR version.\n\n2. **Authors:** Full author list is **Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi** (5 authors). Verify the bib entry has all five.\n\n3. **Year / preprint history:** The arXiv preprint was first posted **March 20, 2023** (arXiv:2303.11156). The TMLR acceptance was announced **March 13, 2025** (per the TMLR Twitter/X account). So yes, it was first an arXiv 2023 preprint, with the TMLR publication in 2025. If the bib entry says \"2025\" for the TMLR version, that is correct for the journal publication year, but be aware the work has been circulating since 2023.\n\n---\n\n## Summary of discrepancies\n\n| # | Key | Issue | Severity |\n|---|-----|-------|----------|\n| 10 | wu_survey_2025 | Author \"Lidia Sam Chao\" vs standard academic form \"Lidia S. Chao\" | Negligible (both forms used) |\n| 11 | reliable_detection | TMLR published title adds subtitle \"Stress Testing AI Text Detectors Under Various Attacks\" | Medium -- should update title if citing TMLR version |\n| 11 | reliable_detection | Originally arXiv preprint from March 2023 (arXiv:2303.11156), TMLR publication 2025 | Note for context |\n\nAll other entries (1-9) are verified correct with no discrepancies in title, authors, year, or venue."
      }
    ],
    "totalDurationMs": 243586,
    "totalTokens": 39355,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 875,
      "cache_read_input_tokens": 36164,
      "output_tokens": 2315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 875
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2315,
          "cache_read_input_tokens": 36164,
          "cache_creation_input_tokens": 875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 875,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "1c63f942-1f72-4461-b78e-61dcc3b8b681",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "leafUuid": "7be820b5-d079-437d-88a3-a7300203307b",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit references.bib for accuracy and hallucinations",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Assistant

_source line 35 · 2026-05-16T00:05:00.323Z_

<details><summary>Logged reasoning block</summary>

```text
All three verification batches are back. Let me now compile the findings:

**Batch 1 (not_found entries):** All 6 correct. OpenAlex search limitations caused false negatives.

**Batch 2 (mismatches + year discrepancies):** All 13 correct. OpenAlex used arXiv/online-first dates vs conference publication years. No changes needed.

**Batch 3 (recent papers 2024-2026):** 
- 9 out of 11 verified as correct
- `wu_survey_2025`: negligible author name convention issue (Lidia Sam Chao vs Lidia S. 

Chao) - the bib uses what's on the paper, so it's fine
- `reliable_detection`: the full title is already in the bib file, so this is correct as-is

The batch 3 agent flagged a discrepancy, but they were working from a truncated version of the prompt. The actual bibliography already contains the complete title "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks", so there's no issue here.

Now I'm going through the remaining entries I haven't checked yet - `gltr`, `paraphrase_evades`, `grover`, `release_strategies`, `curse_of_recursion`, `model_collapse_avoidable`, and `dsir` - all verified through OpenAlex with their respective years.

Continuing through the rest of the bibliography, I'm verifying `qurating`, `watermark_llm`, `synthid_text`, `curious_decline`, `mapping_llm_science`, `monitoring_ai_review`, `uchendu_attribution`, `munir_looking_glass`, and `olmo` - all confirmed through OpenAlex.

Now I'm double-checking the venues for the more recent papers. `mapping_llm_science` from 2024 lists "Proceedings of the Conference on Language Modeling" which appears to be COLM 2024, the same venue as `model_collapse_avoidable`. And `monitoring_ai_review` is confirmed as ICML 2024. Both look correct.

I need to reconcile a discrepancy though—the bib file I examined has 37 entries, but the verification tool reports 49 total entries. Let me recount what I've actually seen so far: detectgpt, gltr, dna_gpt, binoculars, fast_detectgpt, ld_score, intrinsic_dimension, diveye, generator_barrier, feat_aug_transformer, reliable_detection, paraphrase_evades, detection_possibilities, grover, release_strategies, and beyond—that's 16 entries, so there are clearly more I haven't reviewed yet.

Looking at the remaining entries from the verification output, I can see entries 17 through 43 including semeval2024_task8, self_consuming_mad, curse_of_recursion, strong_model_collapse, model_collapse_avoidable, ood_baseline, dsir, qurating, ccnet, watermark_llm, synthid_text, aaronson_watermark, chainwash, curious_decline, writing_diversity, nucleus_sampling, mapping_llm_science, monitoring_ai_review, stamatatos_survey, koppel_authorship, uchendu_attribution, munir_looking_glass, broken_telephone, markovian_chains, min_k_percent, and wu_survey_2025, with at least one more entry cut off. So I'm seeing a much larger set of references than what appeared in the file I initially read.

The file contains all 49 entries verified as correct with no errors to fix. I notice there's a discrepancy where OpenAlex shows diveye with year 2025, but the bibliography has 2026, which the agent confirmed is correct since it's published in TMLR in February 2026. Now I'm checking whether there's also an artifacts version of the bibliography file to validate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7be820b5-d079-437d-88a3-a7300203307b",
  "isSidechain": false,
  "requestId": "req_011Cb5GbQChxUd4ZVymKsn5Z",
  "type": "assistant",
  "uuid": "d537711a-e9a8-4b31-ac75-e7727d10856f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2wK5TdWTM1vwiK8aZn4DM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10069,
      "cache_read_input_tokens": 47822,
      "output_tokens": 1976,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1976,
          "cache_read_input_tokens": 47822,
          "cache_creation_input_tokens": 10069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10069
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

_source line 36 · 2026-05-16T00:05:01.859Z_

所有三批验证完成。结论：**全部 49 条 bib 条目均准确无误。** OpenAlex 的 6 个 not_found 和 2 个 mismatch 都是 OpenAlex 搜索局限（标题匹配阈值过高、使用 arXiv 日期而非会议日期）。

让我检查 artifacts 目录是否有 bib 副本需要同步。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d537711a-e9a8-4b31-ac75-e7727d10856f",
  "isSidechain": false,
  "requestId": "req_011Cb5GbQChxUd4ZVymKsn5Z",
  "type": "assistant",
  "uuid": "bdb05c92-3ff1-4423-863c-95e02e454d2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2wK5TdWTM1vwiK8aZn4DM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10069,
      "cache_read_input_tokens": 47822,
      "output_tokens": 1976,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1976,
          "cache_read_input_tokens": 47822,
          "cache_creation_input_tokens": 10069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10069
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

_source line 37 · 2026-05-16T00:05:03.933Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NbJs6QjEq5uEBZpjN3ZEME`</summary>

```json
{
  "pattern": "artifacts/_project/paper/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdb05c92-3ff1-4423-863c-95e02e454d2c",
  "isSidechain": false,
  "requestId": "req_011Cb5GbQChxUd4ZVymKsn5Z",
  "type": "assistant",
  "uuid": "6f9fe1f6-729b-44ac-b483-1d7d357acccf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2wK5TdWTM1vwiK8aZn4DM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10069,
      "cache_read_input_tokens": 47822,
      "output_tokens": 1976,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1976,
          "cache_read_input_tokens": 47822,
          "cache_creation_input_tokens": 10069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10069
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

_source line 38 · 2026-05-16T00:05:03.952Z_

<details><summary>↩ Tool result · `toolu_01NbJs6QjEq5uEBZpjN3ZEME`</summary>

```text
artifacts/_project/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f9fe1f6-729b-44ac-b483-1d7d357acccf",
  "isSidechain": false,
  "promptId": "717c1a5f-05be-403b-aa0c-e27dacf66b17",
  "type": "user",
  "uuid": "c31c58a5-8776-4cf4-8b5f-a82bdc36275e",
  "toolUseResult": {
    "filenames": [
      "artifacts/_project/paper/references.bib"
    ],
    "durationMs": 13,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "6f9fe1f6-729b-44ac-b483-1d7d357acccf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 39 · 2026-05-16T00:05:04.067Z_

```json
{
  "parentUuid": "c31c58a5-8776-4cf4-8b5f-a82bdc36275e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fc9dbce2-bf61-45b9-a6d4-ea99bb1b5e78",
  "timestamp": "2026-05-16T00:05:04.067Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 40 · 2026-05-16T00:05:07.633Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TWdmDyiDTYz5j9hnoXewnB`</summary>

```json
{
  "command": "diff /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
  "description": "Compare docs and artifacts bib files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc9dbce2-bf61-45b9-a6d4-ea99bb1b5e78",
  "isSidechain": false,
  "requestId": "req_011Cb5GeBfV6PAiacqrbjiTU",
  "type": "assistant",
  "uuid": "871f7608-c4e2-461e-8afb-891f30a47bd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A29ER9ApojJVb2bJEovy1f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2097,
      "cache_read_input_tokens": 57891,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2097,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 57891,
          "cache_creation_input_tokens": 2097,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2097
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

_source line 41 · 2026-05-16T00:05:07.780Z_

<details><summary>↩ Tool result · `toolu_01TWdmDyiDTYz5j9hnoXewnB`</summary>

```text
138a139
>   doi = {10.1038/s41586-024-07566-y},
202a204
>   doi = {10.1038/s41586-024-08025-4},
283a286
>   pages = {1811--1822},
284a288
>   doi = {10.18653/v1/2021.eacl-main.155},
318a323,325
>   volume = {51},
>   number = {1},
>   pages = {275--338},
319a327
>   doi = {10.1162/coli_a_00549},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "871f7608-c4e2-461e-8afb-891f30a47bd6",
  "isSidechain": false,
  "promptId": "717c1a5f-05be-403b-aa0c-e27dacf66b17",
  "type": "user",
  "uuid": "1be02bd1-0103-448f-b95e-e94d07be9262",
  "toolUseResult": {
    "stdout": "138a139\n>   doi = {10.1038/s41586-024-07566-y},\n202a204\n>   doi = {10.1038/s41586-024-08025-4},\n283a286\n>   pages = {1811--1822},\n284a288\n>   doi = {10.18653/v1/2021.eacl-main.155},\n318a323,325\n>   volume = {51},\n>   number = {1},\n>   pages = {275--338},\n319a327\n>   doi = {10.1162/coli_a_00549},",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "Files differ",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "871f7608-c4e2-461e-8afb-891f30a47bd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-16T00:05:12.887Z_

<details><summary>Logged reasoning block</summary>

```text
The artifacts version has some extra fields (doi, volume, number, pages) that the docs version doesn't have. The artifacts version is actually more complete. The docs version is the one referenced in the paper compilation though. These are minor formatting additions, not corrections - both files have the same entries and same core data.

Since neither file has any errors in the verified fields (title, author, year, venue), no corrections are needed. The artifacts version just has a few extra metadata fields.

Let me produce the audit summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1be02bd1-0103-448f-b95e-e94d07be9262",
  "isSidechain": false,
  "requestId": "req_011Cb5GeTYxHyFVTTmxnyG1T",
  "type": "assistant",
  "uuid": "c96b39ff-5ea6-49ae-bcf3-29018082717f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YB4K9iF6Z46vFQLiHg9WGx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 59988,
      "output_tokens": 744,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 314,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 744,
          "cache_read_input_tokens": 59988,
          "cache_creation_input_tokens": 314,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 314
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

_source line 43 · 2026-05-16T00:05:24.573Z_

artifacts 版本比 docs 版本多了一些 doi/volume/pages 字段，但核心信息（title/author/year/venue）完全一致，无需修复。

---

## 引用审计报告

**总数**: 49 条引用（`docs/paper/references.bib`）
**正文引用**: 72 处 `\cite`/`\citet`/`\citep`，覆盖 49 个唯一 key
**交叉检查**: 0 孤立条目，0 缺失条目，0 重复 key
**已验证**: 49 条全部通过 ✓
**需修复**: 0 条

### 验证详情

| 验证方式 | 条目数 | 结果 |
|---------|--------|------|
| OpenAlex 自动验证 | 41 | 标题+年份匹配 |
| WebSearch 人工复核（OpenAlex not_found） | 6 | detectgpt, reliable_detection, detection_possibilities, aaronson_watermark, pythia, xgboost — 全部确认存在且信息正确 |
| WebSearch 人工复核（OpenAlex mismatch） | 2 | self_consuming_mad（Alemohammad 确为第一作者，OpenAlex 索引错误）、qwen3（{Qwen Team} 是标准引用形式）|

### OpenAlex 年份差异说明

13 条 OpenAlex 返回年份与 bib 不同（如 dna_gpt bib=2024 vs OA=2023），全部核实为 **OpenAlex 使用 arXiv preprint 日期**，bib 使用会议/期刊出版年份，bib 写法正确。

### 2024-2026 近期论文重点核查

11 条 2024-2026 论文逐条 WebSearch 验证，标题、作者、年份、venue 全部准确，未发现 hallucinated 作者或编造条目。

### artifacts 同步

`artifacts/_project/paper/references.bib` 与 `docs/paper/references.bib` 核心信息一致，artifacts 版本额外包含部分 doi/volume/pages 字段，无冲突。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c96b39ff-5ea6-49ae-bcf3-29018082717f",
  "isSidechain": false,
  "requestId": "req_011Cb5GeTYxHyFVTTmxnyG1T",
  "type": "assistant",
  "uuid": "96e429f3-3173-481a-953e-d5fce82886e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YB4K9iF6Z46vFQLiHg9WGx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 59988,
      "output_tokens": 744,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 314,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 744,
          "cache_read_input_tokens": 59988,
          "cache_creation_input_tokens": 314,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 314
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

_source line 44_

```json
{
  "type": "last-prompt",
  "leafUuid": "96e429f3-3173-481a-953e-d5fce82886e4",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit references.bib for accuracy and hallucinations",
  "sessionId": "fa623007-1118-4644-bf66-dcd1a38ff1d6"
}
```

---
