# Research conversation: <project_context> # 项目: symb_invariant_consensus ## 运行环境 - 服务器名: westd-16639 - SSH 连接命令: ssh westd-16639 # 必须用此命令，~/.ssh

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/918f3ef6-eada-4f79-bb59-250954707386.jsonl`
- **Structured JSON:** [`832046056c0fff1673f0.json`](../../sessions/83/832046056c0fff1673f0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-25T00:04:54.764Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T00:04:54.764Z",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
  "content": "&lt;project_context>\n# 项目: symb_invariant_consensus\n\n## 运行环境\n- 服务器名: westd-16639\n- SSH 连接命令: ssh westd-16639  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/symb_invariant_consensus\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 所有实验代码写完后必须先 dry-run 验证（python 可用性、路径存在性、端口无冲突、数据文件存在）再正式部署运行（原因：多次出现代码部署后才发现 python command not found、模型路径不存在、GPU/端口冲突等低级错误，浪费 GPU 时间和调试周期。用户明确要求。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：补充两个 bib entries（P0 紧急，deadline 明天）\n\n### 目标\n在 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib` 中补充两个引用条目。\n\n### 步骤\n\n1. **先读取现有 references.bib**，确认这两个条目是否已存在（避免重复）。\n\n2. **Math-Shepherd**:\n   - 已知信息: Wang et al., 2024, \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\"\n   - 用 WebSearch 确认: 准确作者列表、发表venue（应该是 ACL 2024 或 arXiv）、年份\n   - 生成 BibTeX 条目（@inproceedings 或 @article）\n\n3. **GRACE**:\n   - 不确定准确标题和作者\n   - 用 WebSearch 搜索 \"GRACE LLM reasoning\" 或 \"GRACE verification language model\" 确认准确信息\n   - 这可能是关于 reasoning verification 或 constraint-based reasoning 的论文\n   - 生成 BibTeX 条目\n\n4. **将两个条目追加到 references.bib 末尾**，保持与现有条目格式一致。\n\n### 注意\n- BibTeX key 格式与文件中现有条目保持一致\n- 确保所有字段完整: author, title, booktitle/journal, year, pages(如有), url(如有)\n- 引用信息必须准确，不要编造——通过 WebSearch 确认\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-25T00:04:54.767Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T00:04:54.767Z",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386"
}
```

---

## Round 1

16 recorded events

### User

_source line 3 · 2026-05-25T00:04:54.806Z_

&lt;project_context>
# 项目: symb_invariant_consensus

## 运行环境
- 服务器名: westd-16639
- SSH 连接命令: ssh westd-16639  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/symb_invariant_consensus

## ⚠️ 活跃约束（必须遵守）

- **C001**: 所有实验代码写完后必须先 dry-run 验证（python 可用性、路径存在性、端口无冲突、数据文件存在）再正式部署运行（原因：多次出现代码部署后才发现 python command not found、模型路径不存在、GPU/端口冲突等低级错误，浪费 GPU 时间和调试周期。用户明确要求。）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：补充两个 bib entries（P0 紧急，deadline 明天）

### 目标
在 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib` 中补充两个引用条目。

### 步骤

1. **先读取现有 references.bib**，确认这两个条目是否已存在（避免重复）。

2. **Math-Shepherd**:
   - 已知信息: Wang et al., 2024, "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations"
   - 用 WebSearch 确认: 准确作者列表、发表venue（应该是 ACL 2024 或 arXiv）、年份
   - 生成 BibTeX 条目（@inproceedings 或 @article）

3. **GRACE**:
   - 不确定准确标题和作者
   - 用 WebSearch 搜索 "GRACE LLM reasoning" 或 "GRACE verification language model" 确认准确信息
   - 这可能是关于 reasoning verification 或 constraint-based reasoning 的论文
   - 生成 BibTeX 条目

4. **将两个条目追加到 references.bib 末尾**，保持与现有条目格式一致。

### 注意
- BibTeX key 格式与文件中现有条目保持一致
- 确保所有字段完整: author, title, booktitle/journal, year, pages(如有), url(如有)
- 引用信息必须准确，不要编造——通过 WebSearch 确认


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9f9c7037-9fab-4b08-9ced-bd3bebc047c0",
  "type": "user",
  "uuid": "6d7154fa-8496-43e0-bbed-e7ad67aaf317",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-25T00:04:54.805Z_

```json
{
  "parentUuid": "6d7154fa-8496-43e0-bbed-e7ad67aaf317",
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
      "mcp__agent-ml-research__save_project_file"
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
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "95638ec3-950d-4137-8c5c-98ecc43934aa",
  "timestamp": "2026-05-25T00:04:54.805Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-25T00:04:54.805Z_

```json
{
  "parentUuid": "95638ec3-950d-4137-8c5c-98ecc43934aa",
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
  "uuid": "954cb5a2-930d-407f-a77c-44e0f46336aa",
  "timestamp": "2026-05-25T00:04:54.805Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-25T00:04:54.805Z_

```json
{
  "parentUuid": "954cb5a2-930d-407f-a77c-44e0f46336aa",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7560f30a-e20a-4546-9d04-10c501abb860",
  "timestamp": "2026-05-25T00:04:54.805Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
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
  "aiTitle": "Add two bib entries to references",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386"
}
```

---

### Assistant

_source line 8 · 2026-05-25T00:04:59.099Z_

Let me start by reading the existing references.bib and searching for the two papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7560f30a-e20a-4546-9d04-10c501abb860",
  "isSidechain": false,
  "requestId": "req_011CbNJuk5bUq1XWvCiwji6i",
  "type": "assistant",
  "uuid": "e5f8efd4-25a7-48c6-a304-7b7afe5df793",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017H5Xj4JDJCRt9tkUh1r4KU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12159,
      "cache_read_input_tokens": 11841,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 170,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12159
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

_source line 9 · 2026-05-25T00:04:59.251Z_

<details open><summary>🔧 Tool call — Read · `toolu_013YRVkRN6XkALme7sqnjrTZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5f8efd4-25a7-48c6-a304-7b7afe5df793",
  "isSidechain": false,
  "requestId": "req_011CbNJuk5bUq1XWvCiwji6i",
  "type": "assistant",
  "uuid": "ec45fdf7-c3c2-4529-a18a-8828ff12e53e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017H5Xj4JDJCRt9tkUh1r4KU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12159,
      "cache_read_input_tokens": 11841,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 170,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12159
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

_source line 10 · 2026-05-25T00:04:59.271Z_

<details><summary>↩ Tool result · `toolu_013YRVkRN6XkALme7sqnjrTZ`</summary>

```text
1	% References for SICA paper
2	% Generated from literature_map.yaml — 2026-05-17
3	
4	@book{cover2006elements,
5	  title={Elements of Information Theory},
6	  author={Cover, Thomas M. and Thomas, Joy A.},
7	  edition={2nd},
8	  publisher={Wiley-Interscience},
9	  year={2006}
10	}
11	
12	%%% SAT-Based Reasoning %%%
13	
14	@inproceedings{ye2024satlm,
15	  title={SatLM: Satisfiability-Aided Language Models Using Declarative Prompting},
16	  author={Ye, Xi and Chen, Qiaochu and Dillig, Isil and Durrett, Greg},
17	  booktitle={Advances in Neural Information Processing Systems},
18	  volume={36},
19	  year={2024}
20	}
21	
22	%%% Program-Aided Reasoning %%%
23	
24	@inproceedings{gao2023pal,
25	  title={{PAL}: Program-aided Language Models},
26	  author={Gao, Luyu and Madaan, Aman and Zhou, Shuyan and Alon, Uri and Liu, Pengfei and Yang, Yiming and Callan, Jamie and Neubig, Graham},
27	  booktitle={Proceedings of the 40th International Conference on Machine Learning (ICML)},
28	  year={2023}
29	}
30	
31	@article{chen2023program,
32	  title={Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks},
33	  author={Chen, Wenhu and Ma, Xueguang and Wang, Xinyi and Cohen, William W.},
34	  journal={Transactions on Machine Learning Research},
35	  year={2023}
36	}
37	
38	@inproceedings{lyu2023faithful,
39	  title={Faithful Chain-of-Thought Reasoning},
40	  author={Lyu, Qing and Havaldar, Shreya and Stein, Adam and Zhang, Li and Rao, Delip and Wong, Eric and Apidianaki, Marianna and Callison-Burch, Chris},
41	  booktitle={Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},
42	  year={2023}
43	}
44	
45	%%% Theoretical Foundations %%%
46	
47	@book{condorcet1785,
48	  title={Essai sur l'application de l'analyse \`a la probabilit\'e des d\'ecisions rendues \`a la pluralit\'e des voix},
49	  author={de Condorcet, Marie Jean Antoine Nicolas de Caritat},
50	  year={1785},
51	  publisher={Imprimerie Royale},
52	  address={Paris}
53	}
54	
55	@article{ladha1992correlated,
56	  title={The {C}ondorcet Jury Theorem, Free Speech, and Correlated Votes},
57	  author={Ladha, Krishna K.},
58	  journal={American Journal of Political Science},
59	  volume={36},
60	  number={3},
61	  pages={617--634},
62	  year={1992}
63	}
64	
65	@article{fleiss1971kappa,
66	  title={Measuring Nominal Scale Agreement Among Many Raters},
67	  author={Fleiss, Joseph L.},
68	  journal={Psychological Bulletin},
69	  volume={76},
70	  number={5},
71	  pages={378--382},
72	  year={1971}
73	}
74	
75	%%% Self-Consistency and Variants %%%
76	
77	@inproceedings{wang2023sc,
78	  title={Self-Consistency Improves Chain of Thought Reasoning in Language Models},
79	  author={Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
80	  booktitle={ICLR},
81	  year={2023}
82	}
83	
84	@inproceedings{chen2024usc,
85	  title={Universal Self-Consistency for Large Language Model Generation},
86	  author={Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
87	  booktitle={ICML},
88	  year={2024}
89	}
90	
91	@inproceedings{taubenfeld2025cisc,
92	  title={Confidence Improves Self-Consistency in {LLM}s},
93	  author={Taubenfeld, Asaf and Goldstein, Ido and Tsur, Oren},
94	  booktitle={ACL Findings},
95	  year={2025}
96	}
97	
98	@article{loo2025reevaluating,
99	  title={Reevaluating Self-Consistency Scaling in Multi-Agent Systems},
100	  author={Loo, Ryan and others},
101	  journal={arXiv preprint arXiv:2511.00751},
102	  year={2025}
103	}
104	
105	@inproceedings{li2023diverse,
106	  title={Making Language Models Better Reasoners with Step-Aware Verifier},
107	  author={Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},
108	  booktitle={ACL},
109	  year={2023}
110	}
111	
112	%%% Neuro-Symbolic Reasoning %%%
113	
114	@inproceedings{pan2023logiclm,
115	  title={Logic-{LM}: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning},
116	  author={Pan, Liangming and Alber, Alon and Xu, Wenhu and Deng, Yixin and Chen, Huan and Ji, Heng},
117	  booktitle={EMNLP Findings},
118	  year={2023}
119	}
120	
121	@inproceedings{olausson2023linc,
122	  title={{LINC}: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers},
123	  author={Olausson, Theo X. and Gu, Alex and Lipkin, Benjamin and Zhang, Cedegao E. and Solar-Lezama, Armando and Tenenbaum, Joshua B. and Levy, Roger},
124	  booktitle={EMNLP},
125	  year={2023}
126	}
127	
128	@inproceedings{xu2026dylos,
129	  title={Adaptive {LLM}-Symbolic Reasoning via Dynamic Logical Solver Composition ({DyLoS})},
130	  author={Xu, Lei and Beckmann, Pierre and Valentino, Marco and Freitas, Andre},
131	  booktitle={EACL},
132	  year={2026}
133	}
134	
135	@article{wang2025fover,
136	  title={{FoVer}: First-Order Logic Verification for Natural Language Reasoning},
137	  author={Wang, Yilun and others},
138	  journal={TACL},
139	  year={2025}
140	}
141	
142	@inproceedings{li2025aristotle,
143	  title={Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework},
144	  author={Li, Jundong and others},
145	  booktitle={ACL},
146	  year={2025}
147	}
148	
149	@article{luo2025logicagent,
150	  title={From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for {LLM} Logical Reasoning},
151	  author={Luo, Yiqi and others},
152	  journal={arXiv preprint arXiv:2509.24765},
153	  year={2025}
154	}
155	
156	%%% Test-Time Compute and Reasoning Models %%%
157	
158	@inproceedings{snell2025scaling,
159	  title={Scaling {LLM} Test-Time Compute Optimally Can be More Effective than Scaling Parameters},
160	  author={Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
161	  booktitle={ICLR (Oral)},
162	  year={2025}
163	}
164	
165	@inproceedings{yao2023tree,
166	  title={Tree of Thoughts: Deliberate Problem Solving with Large Language Models},
167	  author={Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L. and Cao, Yuan and Narasimhan, Karthik},
168	  booktitle={Advances in Neural Information Processing Systems},
169	  volume={36},
170	  year={2023}
171	}
172	
173	
174	%%% Verification and Reranking %%%
175	
176	@article{cobbe2021gsm8k,
177	  title={Training Verifiers to Solve Math Word Problems},
178	  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
179	  journal={arXiv preprint arXiv:2110.14168},
180	  year={2021}
181	}
182	
183	@inproceedings{lightman2024prm,
184	  title={Let's Verify Step by Step},
185	  author={Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
186	  booktitle={ICLR},
187	  year={2024}
188	}
189	
190	@inproceedings{wang2024mathshepherd,
191	  title={Math-Shepherd: Verify and Reinforce {LLM}s Step-by-step without Human Annotations},
192	  author={Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, R.X. and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Y. and Sui, Zhifang},
193	  booktitle={ACL},
194	  year={2024}
195	}
196	
197	@inproceedings{khalifa2023grace,
198	  title={{GRACE}: Discriminator-Guided Chain-of-Thought Reasoning},
199	  author={Khalifa, Muhammad and Logeswaran, Lajanugen and Lee, Moontae and Lee, Honglak and Wang, Lu},
200	  booktitle={Findings of EMNLP},
201	  year={2023}
202	}
203	
204	%%% Constraint Satisfaction in NLP %%%
205	
206	%%% Debate and Multi-Agent %%%
207	
208	@article{liang2023encouraging,
209	  title={Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate},
210	  author={Liang, Tian and He, Zhiwei and Jiao, Wenxiang and Wang, Xing and Wang, Yan and Wang, Rui and Yang, Yujiu and Tu, Zhaopeng and Shi, Shuming},
211	  journal={arXiv preprint arXiv:2305.19118},
212	  year={2023}
213	}
214	
215	@inproceedings{du2023improving,
216	  title={Improving Factuality and Reasoning in Language Models through Multiagent Debate},
217	  author={Du, Yilun and Li, Shuang and Torralba, Antonio and Tenenbaum, Joshua B. and Mordatch, Igor},
218	  booktitle={ICML},
219	  year={2024}
220	}
221	
222	%%% Benchmarks and Datasets %%%
223	
224	@article{han2022folio,
225	  title={{FOLIO}: Natural Language Reasoning with First-Order Logic},
226	  author={Han, Simeng and Schoelkopf, Hailey and Zhao, Yilun and Qi, Zhenting and Riddell, Martin and Benson, Luke and Sun, Lucy and Zubova, Ekaterina and Qiao, Yujie and Burtell, Matthew and Peng, David and Fan, Jonathan and Liu, Yi and Wong, Brian and Sailor, Malcolm and Ni, Ansong and Nan, Linyong and Kasai, Jungo and Yu, Tao and Zhang, Rui and Joty, Shafiq and Fabbri, Alexander R. and Kryscinski, Wojciech and Lin, Xi Victoria and Xiong, Caiming and Radev, Dragomir},
227	  journal={arXiv preprint arXiv:2209.00840},
228	  year={2022}
229	}
230	
231	@inproceedings{tafjord2021proofwriter,
232	  title={{ProofWriter}: Generating Implications, Proofs, and Abductive Statements over Natural Language},
233	  author={Tafjord, Oyvind and Dalvi, Bhavana and Clark, Peter},
234	  booktitle={ACL Findings},
235	  year={2021}
236	}
237	
238	@article{geva2021strategyqa,
239	  title={Did {Aristotle} Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies},
240	  author={Geva, Mor and Khashabi, Daniel and Segal, Elad and Khot, Tushar and Roth, Dan and Berant, Jonathan},
241	  journal={TACL},
242	  year={2021}
243	}
244	
245	@inproceedings{liu2020logiqa,
246	  title={{LogiQA}: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning},
247	  author={Liu, Jian and Cui, Leyang and Liu, Hanmeng and Huang, Dandan and Wang, Yile and Zhang, Yue},
248	  booktitle={IJCAI},
249	  pages={3622--3628},
250	  year={2020}
251	}
252	
253	%%% Negative Results / Analysis Papers %%%
254	
255	@inproceedings{huang2024selfcorrect,
256	  title={Large Language Models Cannot Self-Correct Reasoning Yet},
257	  author={Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},
258	  booktitle={ICLR},
259	  year={2024}
260	}
261	
262	@inproceedings{xie2023selfevaluation,
263	  title={Self-Evaluation Guided Beam Search for Reasoning},
264	  author={Xie, Yuxi and Kawaguchi, Kenji and Zhao, Yiran and Zhao, Xu and Kan, Min-Yen and He, Junehao and Xie, Qian},
265	  booktitle={NeurIPS},
266	  year={2023}
267	}
268	
269	@inproceedings{weng2023selfverification,
270	  title={Large Language Models are Better Reasoners with Self-Verification},
271	  author={Weng, Yixuan and Zhu, Minjun and Xia, Fei and Li, Bin and He, Shizhu and Liu, Shengping and Sun, Bin and Liu, Kang and Zhao, Jun},
272	  booktitle={Findings of EMNLP},
273	  year={2023}
274	}
275	
276	@article{dhuliawala2023chainofverification,
277	  title={Chain-of-Verification Reduces Hallucination in Large Language Models},
278	  author={Dhuliawala, Shehzaad and Komeili, Mojtaba and Xu, Jing and Raileanu, Roberta and Li, Xian and Celikyilmaz, Asli and Weston, Jason},
279	  journal={arXiv preprint arXiv:2309.11495},
280	  year={2023}
281	}
282	
283	@inproceedings{madaan2023selfrefine,
284	  title={Self-Refine: Iterative Refinement with Self-Feedback},
285	  author={Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and others},
286	  booktitle={NeurIPS},
287	  year={2023}
288	}
289	
290	@inproceedings{gou2024critic,
291	  title={{CRITIC}: Large Language Models Can Self-Correct with Tool-Interactive Critiquing},
292	  author={Gou, Zhibin and Shao, Zhihong and Gong, Yeyun and Shen, Yelong and Yang, Yujiu and Huang, Minlie and Duan, Nan and Chen, Weizhu},
293	  booktitle={ICLR},
294	  year={2024}
295	}
296	
297	@article{zhu2025vericot,
298	  title={VeriCoT: Verified Chain of Thought},
299	  author={Zhu, Hao and Gao, Yuxuan and Ke, Nuo Xu and Lu, Pan},
300	  journal={arXiv preprint arXiv:2511.04662},
301	  year={2025}
302	}
303	
304	%%% Model Papers %%%
305	
306	@article{yang2024qwen25,
307	  title={Qwen2.5 Technical Report},
308	  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Wang, Bo and others},
309	  journal={arXiv preprint arXiv:2412.15115},
310	  year={2024}
311	}
312	
313	@article{jiang2023mistral,
314	  title={Mistral 7{B}},
315	  author={Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and de las Casas, Diego and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and Lavaud, L{\'e}lio Renard and Lachaux, Marie-Anne and Stock, Pierre and Scao, Teven Le and Lavril, Thibaut and Wang, Thomas and Lacroix, Timoth{\'e}e and El Sayed, William},
316	  journal={arXiv preprint arXiv:2310.06825},
317	  year={2023}
318	}
319	
320	@article{dubey2024llama3,
321	  title={The {Llama} 3 Herd of Models},
322	  author={Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and others},
323	  journal={arXiv preprint arXiv:2407.21783},
324	  year={2024}
325	}
326	
327	@article{guo2025deepseekr1,
328	  title={{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLM}s via Reinforcement Learning},
329	  author={Guo, Daya and Yang, Dejian and Zhang, He and Song, Junxiao and others},
330	  journal={arXiv preprint arXiv:2501.12948},
331	  year={2025}
332	}
333	
334	@misc{qwen2024qwq,
335	  title={{QwQ}: Reflect Deeply on the Boundaries of the Unknown},
336	  author={{Qwen Team}},
337	  year={2024},
338	  howpublished={Technical Blog},
339	  note={\url{https://qwenlm.github.io/blog/qwq-32b-preview/}}
340	}
341	
342	%%% Oracle/Upper-Bound Experiments %%%
343	
344	%%% Reasoning-Aware SC Variants %%%
345	
346	@article{wan2024rasc,
347	  title={Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient {LLM} Sampling},
348	  author={Wan, Guangya and Wu, Yuqi and Chen, Jie and Li, Sheng},
349	  journal={arXiv preprint arXiv:2408.17017},
350	  year={2024}
351	}
352	
353	@article{kim2026reasc,
354	  title={Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
355	  author={Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
356	  journal={arXiv preprint arXiv:2601.02970},
357	  year={2026}
358	}
359	
360	%%% LLM Formalization %%%
361	
362	@article{amonkar2025realitycheck,
363	  title={A Reality Check of Language Models as Formalizers on Constraint Satisfaction Problems},
364	  author={Amonkar, Rikhil and Kayan, Ceyhun Efe and Lai, Qimei and Le Bras, Ronan and Zhang, Li},
365	  journal={arXiv preprint arXiv:2505.13252},
366	  year={2025}
367	}
368	
369	%%% Tools and Solvers %%%
370	
371	@inproceedings{demoura2008z3,
372	  title={{Z3}: An Efficient {SMT} Solver},
373	  author={de Moura, Leonardo and Bj{\o}rner, Nikolaj},
374	  booktitle={TACAS},
375	  year={2008}
376	}
377	
378	%%% Condorcet / Voting Theory %%%
379	
380	%%% CoT Faithfulness %%%
381	
382	@inproceedings{turpin2023language,
383	  title={Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting},
384	  author={Turpin, Miles and Michael, Julian and Perez, Ethan and Bowman, Samuel},
385	  booktitle={NeurIPS},
386	  year={2023}
387	}
388	
389	%%% Confirmation Bias in LLM Reasoning %%%
390	
391	@inproceedings{wan2025unveiling,
392	  title={Unveiling Confirmation Bias in Chain-of-Thought Reasoning},
393	  author={Wan, Yue and Jia, Xiaowei and Li, Xiang Lorraine},
394	  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},
395	  year={2025}
396	}
397	
398	@article{jhaveri2026failing,
399	  title={Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models},
400	  author={Jhaveri, Ayush Rajesh and GX-Chen, Anthony and Sucholutsky, Ilia and Choi, Eunsol},
401	  journal={arXiv preprint arXiv:2604.02485},
402	  year={2026}
403	}
404	
405	@article{miya2025eidoku,
406	  title={Eidoku: A Neuro-Symbolic Verification Gate for {LLM} Reasoning via Structural Constraint Satisfaction},
407	  author={Miya, Shinobu},
408	  journal={arXiv preprint arXiv:2512.20664},
409	  year={2025}
410	}
411	
412	%%% Ensemble Diversity %%%
413	
414	@incollection{dietterich2000ensemble,
415	  title={Ensemble Methods in Machine Learning},
416	  author={Dietterich, Thomas G.},
417	  booktitle={Multiple Classifier Systems (MCS)},
418	  pages={1--15},
419	  year={2000},
420	  publisher={Springer}
421	}
422	
423	@inproceedings{krogh1994neural,
424	  title={Neural Network Ensembles, Cross Validation, and Active Learning},
425	  author={Krogh, Anders and Vedelsby, Jesper},
426	  booktitle={Advances in Neural Information Processing Systems},
427	  volume={7},
428	  year={1994}
429	}
430	
431	@article{brown2005diversity,
432	  title={Diversity Creation Methods: A Survey and Categorisation},
433	  author={Brown, Gavin and Wyatt, Jeremy and Harris, Rachel and Yao, Xin},
434	  journal={Information Fusion},
435	  volume={6},
436	  number={1},
437	  pages={5--20},
438	  year={2005}
439	}
440	
441	%%% Cross-Architecture Verification %%%
442	
443	@inproceedings{he2021deberta,
444	  title={{DeBERTa}: Decoding-enhanced {BERT} with Disentangled Attention},
445	  author={He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu},
446	  booktitle={Proceedings of ICLR},
447	  year={2021}
448	}
449	
450	@inproceedings{williams2018mnli,
451	  title={A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference},
452	  author={Williams, Adina and Nangia, Nikita and Bowman, Samuel},
453	  booktitle={Proceedings of NAACL-HLT},
454	  pages={1112--1122},
455	  year={2018}
456	}
457	
458	%%% Compositional / Iterative Neuro-Symbolic Verification %%%
459	
460	@inproceedings{ryu2025clover,
461	  title={Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning},
462	  author={Ryu, Hyun and Kim, Gyeongman and Lee, Hyemin S. and Yang, Eunho},
463	  booktitle={International Conference on Learning Representations (ICLR)},
464	  year={2025}
465	}
466	
467	@article{singh2026verge,
468	  title={{VERGE}: Formal Refinement and Guidance Engine for Verifiable {LLM} Reasoning},
469	  author={Singh, Vikash and Cassel, Darion and Weir, Nathaniel and Feng, Nick and Bayless, Sam},
470	  journal={arXiv preprint arXiv:2601.20055},
471	  year={2026}
472	}
473	
474	%%% Programs-as-Verifiers %%%
475	
476	@article{toh2024notallvotes,
477	  title={Not All Votes Count! Programs as Verifiers Improve Self-Consistency of Language Models for Math Reasoning},
478	  author={Toh, Vernon Y.H. and Ghosal, Deepanway and Poria, Soujanya},
479	  journal={arXiv preprint arXiv:2410.12608},
480	  year={2024}
481	}
482	
483	%%% Logical Soundness Critique %%%
484	
485	@article{chan2026position,
486	  title={Position: Logical Soundness is not a Reliable Criterion for Neurosymbolic Fact-Checking with {LLMs}},
487	  author={Chan, Jason and Gaizauskas, Robert and Zhao, Zhixue},
488	  journal={arXiv preprint arXiv:2604.04177},
489	  year={2026}
490	}
491	
492	%%% Statistical Methods %%%
493	
494	@article{lakens2017equivalence,
495	  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},
496	  author={Lakens, Dani{\"e}l},
497	  journal={Social Psychological and Personality Science},
498	  volume={8},
499	  number={4},
500	  pages={355--362},
501	  year={2017},
502	  doi={10.1177/1948550617697177}
503	}
504	
505	%%% R11 Added Citations %%%
506	
507	@article{byerly2025selfconsistency,
508	  title={Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems},
509	  author={Byerly, Adam and Khashabi, Daniel},
510	  journal={Transactions of the Association for Computational Linguistics},
511	  year={2025},
512	  note={arXiv:2411.01101}
513	}
514	
515	@article{kuai2026independent,
516	  title={How Independent are Large Language Models? {A} Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles},
517	  author={Kuai, Chenchen and Jiang, Jiwan and Zhu, Zihao and Wang, Hao and Wu, Keshu and Li, Zihao and Zhang, Yunlong and Liu, Chenxi and Tu, Zhengzhong and Fan, Zhiwen and Zhou, Yang},
518	  journal={arXiv preprint arXiv:2604.07650},
519	  year={2026}
520	}
521	
522	@article{kim2025correlated,
523	  title={Correlated Errors in Large Language Models},
524	  author={Kim, Elliot and Garg, Avi and Peng, Kenny and Garg, Nikhil},
525	  journal={arXiv preprint arXiv:2506.07962},
526	  year={2025}
527	}
528	
529	@article{chen2025sets,
530	  title={{SETS}: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling},
531	  author={Chen, Jiefeng and Ren, Jie and Chen, Xinyun and Yang, Chengrun and Sun, Ruoxi and Yoon, Jinsung and Ar{\i}k, Sercan {\"O}.},
532	  journal={arXiv preprint arXiv:2501.19306},
533	  year={2025}
534	}
535	
536	
537	
538	@article{kuncheva2003measures,
539	  title={Measures of Diversity in Classifier Ensembles and Their Relationship with the Ensemble Accuracy},
540	  author={Kuncheva, Ludmila I. and Whitaker, Christopher J.},
541	  journal={Machine Learning},
542	  volume={51},
543	  number={2},
544	  pages={181--207},
545	  year={2003}
546	}
547	
548	%%% Test-Time Scaling and Multi-Agent Verification %%%
549	
550	@article{lifshitz2025mav,
551	  title={Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers},
552	  author={Lifshitz, Shalev and McIlraith, Sheila A. and Du, Simon S.},
553	  journal={arXiv preprint arXiv:2502.20379},
554	  year={2025}
555	}
556	
557	%%% Training-Based Self-Verification %%%
558	
559	@article{kamoi2024selfcorrect,
560	  title={When Can {LLMs} Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of {LLMs}},
561	  author={Kamoi, Ryo and Kobayashi, Yusen and Goyal, Tharindu and Hou, Rui and Sun, Hanjie and Caverlee, James},
562	  journal={Transactions of the Association for Computational Linguistics},
563	  volume={12},
564	  pages={1--20},
565	  year={2024}
566	}
567	
568	
569	@inproceedings{zeng2025s2r,
570	  title={{S$^2$R}: Teaching {LLMs} to Self-verify and Self-correct via Reinforcement Learning},
571	  author={Zeng, Ruotian and Liu, Yuanzhi and others},
572	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
573	  year={2025}
574	}
575	
576	@article{dupo2025,
577	  title={{DuPO}: Enabling Reliable {LLM} Self-Verification via Dual Preference Optimization},
578	  author={She, Shuaijie and Bao, Yu and Lu, Yu and Xu, Lu and Li, Tao and Zhu, Wenhao and Huang, Shujian and Cheng, Shanbo and Lu, Lu and Wang, Yuxuan},
579	  journal={arXiv preprint arXiv:2508.14460},
580	  year={2025}
581	}
582	
583	@inproceedings{li2022alphacode,
584	  title={Competition-Level Code Generation with {AlphaCode}},
585	  author={Li, Yujia and Choi, David and Chung, Junyoung and Kushman, Nate and Schrittwieser, Julian and others},
586	  booktitle={Science},
587	  volume={378},
588	  number={6624},
589	  pages={1092--1097},
590	  year={2022}
591	}
592	
593	@inproceedings{chen2023codet,
594	  title={{CodeT}: Code Generation with Generated Tests},
595	  author={Chen, Bei and Zhang, Fengji and Nguyen, Anh and Zan, Daoguang and Lin, Zeqi and Lou, Jian-Guang and Chen, Weizhu},
596	  booktitle={Proceedings of the 11th International Conference on Learning Representations (ICLR)},
597	  year={2023}
598	}
599	
600	
601	@inproceedings{shinn2023reflexion,
602	  title={Reflexion: Language Agents with Verbal Reinforcement Learning},
603	  author={Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
604	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
605	  year={2023}
606	}
607	
608	@inproceedings{zhou2023lats,
609	  title={Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models},
610	  author={Zhou, Andy and Yan, Kai and Shlapentokh-Rothman, Michal and Wang, Haohan and Wang, Yu-Xiong},
611	  booktitle={International Conference on Machine Learning (ICML)},
612	  year={2024}
613	}
614	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec45fdf7-c3c2-4529-a18a-8828ff12e53e",
  "isSidechain": false,
  "promptId": "9f9c7037-9fab-4b08-9ced-bd3bebc047c0",
  "type": "user",
  "uuid": "8dcd3df1-071e-4dea-a411-ddefc2f1860a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/references.bib",
      "content": "% References for SICA paper\n% Generated from literature_map.yaml — 2026-05-17\n\n@book{cover2006elements,\n  title={Elements of Information Theory},\n  author={Cover, Thomas M. and Thomas, Joy A.},\n  edition={2nd},\n  publisher={Wiley-Interscience},\n  year={2006}\n}\n\n%%% SAT-Based Reasoning %%%\n\n@inproceedings{ye2024satlm,\n  title={SatLM: Satisfiability-Aided Language Models Using Declarative Prompting},\n  author={Ye, Xi and Chen, Qiaochu and Dillig, Isil and Durrett, Greg},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={36},\n  year={2024}\n}\n\n%%% Program-Aided Reasoning %%%\n\n@inproceedings{gao2023pal,\n  title={{PAL}: Program-aided Language Models},\n  author={Gao, Luyu and Madaan, Aman and Zhou, Shuyan and Alon, Uri and Liu, Pengfei and Yang, Yiming and Callan, Jamie and Neubig, Graham},\n  booktitle={Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year={2023}\n}\n\n@article{chen2023program,\n  title={Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks},\n  author={Chen, Wenhu and Ma, Xueguang and Wang, Xinyi and Cohen, William W.},\n  journal={Transactions on Machine Learning Research},\n  year={2023}\n}\n\n@inproceedings{lyu2023faithful,\n  title={Faithful Chain-of-Thought Reasoning},\n  author={Lyu, Qing and Havaldar, Shreya and Stein, Adam and Zhang, Li and Rao, Delip and Wong, Eric and Apidianaki, Marianna and Callison-Burch, Chris},\n  booktitle={Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},\n  year={2023}\n}\n\n%%% Theoretical Foundations %%%\n\n@book{condorcet1785,\n  title={Essai sur l'application de l'analyse \\`a la probabilit\\'e des d\\'ecisions rendues \\`a la pluralit\\'e des voix},\n  author={de Condorcet, Marie Jean Antoine Nicolas de Caritat},\n  year={1785},\n  publisher={Imprimerie Royale},\n  address={Paris}\n}\n\n@article{ladha1992correlated,\n  title={The {C}ondorcet Jury Theorem, Free Speech, and Correlated Votes},\n  author={Ladha, Krishna K.},\n  journal={American Journal of Political Science},\n  volume={36},\n  number={3},\n  pages={617--634},\n  year={1992}\n}\n\n@article{fleiss1971kappa,\n  title={Measuring Nominal Scale Agreement Among Many Raters},\n  author={Fleiss, Joseph L.},\n  journal={Psychological Bulletin},\n  volume={76},\n  number={5},\n  pages={378--382},\n  year={1971}\n}\n\n%%% Self-Consistency and Variants %%%\n\n@inproceedings{wang2023sc,\n  title={Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author={Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle={ICLR},\n  year={2023}\n}\n\n@inproceedings{chen2024usc,\n  title={Universal Self-Consistency for Large Language Model Generation},\n  author={Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle={ICML},\n  year={2024}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title={Confidence Improves Self-Consistency in {LLM}s},\n  author={Taubenfeld, Asaf and Goldstein, Ido and Tsur, Oren},\n  booktitle={ACL Findings},\n  year={2025}\n}\n\n@article{loo2025reevaluating,\n  title={Reevaluating Self-Consistency Scaling in Multi-Agent Systems},\n  author={Loo, Ryan and others},\n  journal={arXiv preprint arXiv:2511.00751},\n  year={2025}\n}\n\n@inproceedings{li2023diverse,\n  title={Making Language Models Better Reasoners with Step-Aware Verifier},\n  author={Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle={ACL},\n  year={2023}\n}\n\n%%% Neuro-Symbolic Reasoning %%%\n\n@inproceedings{pan2023logiclm,\n  title={Logic-{LM}: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning},\n  author={Pan, Liangming and Alber, Alon and Xu, Wenhu and Deng, Yixin and Chen, Huan and Ji, Heng},\n  booktitle={EMNLP Findings},\n  year={2023}\n}\n\n@inproceedings{olausson2023linc,\n  title={{LINC}: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers},\n  author={Olausson, Theo X. and Gu, Alex and Lipkin, Benjamin and Zhang, Cedegao E. and Solar-Lezama, Armando and Tenenbaum, Joshua B. and Levy, Roger},\n  booktitle={EMNLP},\n  year={2023}\n}\n\n@inproceedings{xu2026dylos,\n  title={Adaptive {LLM}-Symbolic Reasoning via Dynamic Logical Solver Composition ({DyLoS})},\n  author={Xu, Lei and Beckmann, Pierre and Valentino, Marco and Freitas, Andre},\n  booktitle={EACL},\n  year={2026}\n}\n\n@article{wang2025fover,\n  title={{FoVer}: First-Order Logic Verification for Natural Language Reasoning},\n  author={Wang, Yilun and others},\n  journal={TACL},\n  year={2025}\n}\n\n@inproceedings{li2025aristotle,\n  title={Aristotle: Mastering Logical Reasoning with A Logic-Complete Decompose-Search-Resolve Framework},\n  author={Li, Jundong and others},\n  booktitle={ACL},\n  year={2025}\n}\n\n@article{luo2025logicagent,\n  title={From Ambiguity to Verdict: A Semiotic-Grounded Multi-Perspective Agent for {LLM} Logical Reasoning},\n  author={Luo, Yiqi and others},\n  journal={arXiv preprint arXiv:2509.24765},\n  year={2025}\n}\n\n%%% Test-Time Compute and Reasoning Models %%%\n\n@inproceedings{snell2025scaling,\n  title={Scaling {LLM} Test-Time Compute Optimally Can be More Effective than Scaling Parameters},\n  author={Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle={ICLR (Oral)},\n  year={2025}\n}\n\n@inproceedings{yao2023tree,\n  title={Tree of Thoughts: Deliberate Problem Solving with Large Language Models},\n  author={Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L. and Cao, Yuan and Narasimhan, Karthik},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={36},\n  year={2023}\n}\n\n\n%%% Verification and Reranking %%%\n\n@article{cobbe2021gsm8k,\n  title={Training Verifiers to Solve Math Word Problems},\n  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal={arXiv preprint arXiv:2110.14168},\n  year={2021}\n}\n\n@inproceedings{lightman2024prm,\n  title={Let's Verify Step by Step},\n  author={Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle={ICLR},\n  year={2024}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title={Math-Shepherd: Verify and Reinforce {LLM}s Step-by-step without Human Annotations},\n  author={Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, R.X. and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Y. and Sui, Zhifang},\n  booktitle={ACL},\n  year={2024}\n}\n\n@inproceedings{khalifa2023grace,\n  title={{GRACE}: Discriminator-Guided Chain-of-Thought Reasoning},\n  author={Khalifa, Muhammad and Logeswaran, Lajanugen and Lee, Moontae and Lee, Honglak and Wang, Lu},\n  booktitle={Findings of EMNLP},\n  year={2023}\n}\n\n%%% Constraint Satisfaction in NLP %%%\n\n%%% Debate and Multi-Agent %%%\n\n@article{liang2023encouraging,\n  title={Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate},\n  author={Liang, Tian and He, Zhiwei and Jiao, Wenxiang and Wang, Xing and Wang, Yan and Wang, Rui and Yang, Yujiu and Tu, Zhaopeng and Shi, Shuming},\n  journal={arXiv preprint arXiv:2305.19118},\n  year={2023}\n}\n\n@inproceedings{du2023improving,\n  title={Improving Factuality and Reasoning in Language Models through Multiagent Debate},\n  author={Du, Yilun and Li, Shuang and Torralba, Antonio and Tenenbaum, Joshua B. and Mordatch, Igor},\n  booktitle={ICML},\n  year={2024}\n}\n\n%%% Benchmarks and Datasets %%%\n\n@article{han2022folio,\n  title={{FOLIO}: Natural Language Reasoning with First-Order Logic},\n  author={Han, Simeng and Schoelkopf, Hailey and Zhao, Yilun and Qi, Zhenting and Riddell, Martin and Benson, Luke and Sun, Lucy and Zubova, Ekaterina and Qiao, Yujie and Burtell, Matthew and Peng, David and Fan, Jonathan and Liu, Yi and Wong, Brian and Sailor, Malcolm and Ni, Ansong and Nan, Linyong and Kasai, Jungo and Yu, Tao and Zhang, Rui and Joty, Shafiq and Fabbri, Alexander R. and Kryscinski, Wojciech and Lin, Xi Victoria and Xiong, Caiming and Radev, Dragomir},\n  journal={arXiv preprint arXiv:2209.00840},\n  year={2022}\n}\n\n@inproceedings{tafjord2021proofwriter,\n  title={{ProofWriter}: Generating Implications, Proofs, and Abductive Statements over Natural Language},\n  author={Tafjord, Oyvind and Dalvi, Bhavana and Clark, Peter},\n  booktitle={ACL Findings},\n  year={2021}\n}\n\n@article{geva2021strategyqa,\n  title={Did {Aristotle} Use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies},\n  author={Geva, Mor and Khashabi, Daniel and Segal, Elad and Khot, Tushar and Roth, Dan and Berant, Jonathan},\n  journal={TACL},\n  year={2021}\n}\n\n@inproceedings{liu2020logiqa,\n  title={{LogiQA}: A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning},\n  author={Liu, Jian and Cui, Leyang and Liu, Hanmeng and Huang, Dandan and Wang, Yile and Zhang, Yue},\n  booktitle={IJCAI},\n  pages={3622--3628},\n  year={2020}\n}\n\n%%% Negative Results / Analysis Papers %%%\n\n@inproceedings{huang2024selfcorrect,\n  title={Large Language Models Cannot Self-Correct Reasoning Yet},\n  author={Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle={ICLR},\n  year={2024}\n}\n\n@inproceedings{xie2023selfevaluation,\n  title={Self-Evaluation Guided Beam Search for Reasoning},\n  author={Xie, Yuxi and Kawaguchi, Kenji and Zhao, Yiran and Zhao, Xu and Kan, Min-Yen and He, Junehao and Xie, Qian},\n  booktitle={NeurIPS},\n  year={2023}\n}\n\n@inproceedings{weng2023selfverification,\n  title={Large Language Models are Better Reasoners with Self-Verification},\n  author={Weng, Yixuan and Zhu, Minjun and Xia, Fei and Li, Bin and He, Shizhu and Liu, Shengping and Sun, Bin and Liu, Kang and Zhao, Jun},\n  booktitle={Findings of EMNLP},\n  year={2023}\n}\n\n@article{dhuliawala2023chainofverification,\n  title={Chain-of-Verification Reduces Hallucination in Large Language Models},\n  author={Dhuliawala, Shehzaad and Komeili, Mojtaba and Xu, Jing and Raileanu, Roberta and Li, Xian and Celikyilmaz, Asli and Weston, Jason},\n  journal={arXiv preprint arXiv:2309.11495},\n  year={2023}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title={Self-Refine: Iterative Refinement with Self-Feedback},\n  author={Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and others},\n  booktitle={NeurIPS},\n  year={2023}\n}\n\n@inproceedings{gou2024critic,\n  title={{CRITIC}: Large Language Models Can Self-Correct with Tool-Interactive Critiquing},\n  author={Gou, Zhibin and Shao, Zhihong and Gong, Yeyun and Shen, Yelong and Yang, Yujiu and Huang, Minlie and Duan, Nan and Chen, Weizhu},\n  booktitle={ICLR},\n  year={2024}\n}\n\n@article{zhu2025vericot,\n  title={VeriCoT: Verified Chain of Thought},\n  author={Zhu, Hao and Gao, Yuxuan and Ke, Nuo Xu and Lu, Pan},\n  journal={arXiv preprint arXiv:2511.04662},\n  year={2025}\n}\n\n%%% Model Papers %%%\n\n@article{yang2024qwen25,\n  title={Qwen2.5 Technical Report},\n  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Wang, Bo and others},\n  journal={arXiv preprint arXiv:2412.15115},\n  year={2024}\n}\n\n@article{jiang2023mistral,\n  title={Mistral 7{B}},\n  author={Jiang, Albert Q. and Sablayrolles, Alexandre and Mensch, Arthur and Bamford, Chris and Chaplot, Devendra Singh and de las Casas, Diego and Bressand, Florian and Lengyel, Gianna and Lample, Guillaume and Saulnier, Lucile and Lavaud, L{\\'e}lio Renard and Lachaux, Marie-Anne and Stock, Pierre and Scao, Teven Le and Lavril, Thibaut and Wang, Thomas and Lacroix, Timoth{\\'e}e and El Sayed, William},\n  journal={arXiv preprint arXiv:2310.06825},\n  year={2023}\n}\n\n@article{dubey2024llama3,\n  title={The {Llama} 3 Herd of Models},\n  author={Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and others},\n  journal={arXiv preprint arXiv:2407.21783},\n  year={2024}\n}\n\n@article{guo2025deepseekr1,\n  title={{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLM}s via Reinforcement Learning},\n  author={Guo, Daya and Yang, Dejian and Zhang, He and Song, Junxiao and others},\n  journal={arXiv preprint arXiv:2501.12948},\n  year={2025}\n}\n\n@misc{qwen2024qwq,\n  title={{QwQ}: Reflect Deeply on the Boundaries of the Unknown},\n  author={{Qwen Team}},\n  year={2024},\n  howpublished={Technical Blog},\n  note={\\url{https://qwenlm.github.io/blog/qwq-32b-preview/}}\n}\n\n%%% Oracle/Upper-Bound Experiments %%%\n\n%%% Reasoning-Aware SC Variants %%%\n\n@article{wan2024rasc,\n  title={Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient {LLM} Sampling},\n  author={Wan, Guangya and Wu, Yuqi and Chen, Jie and Li, Sheng},\n  journal={arXiv preprint arXiv:2408.17017},\n  year={2024}\n}\n\n@article{kim2026reasc,\n  title={Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author={Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  journal={arXiv preprint arXiv:2601.02970},\n  year={2026}\n}\n\n%%% LLM Formalization %%%\n\n@article{amonkar2025realitycheck,\n  title={A Reality Check of Language Models as Formalizers on Constraint Satisfaction Problems},\n  author={Amonkar, Rikhil and Kayan, Ceyhun Efe and Lai, Qimei and Le Bras, Ronan and Zhang, Li},\n  journal={arXiv preprint arXiv:2505.13252},\n  year={2025}\n}\n\n%%% Tools and Solvers %%%\n\n@inproceedings{demoura2008z3,\n  title={{Z3}: An Efficient {SMT} Solver},\n  author={de Moura, Leonardo and Bj{\\o}rner, Nikolaj},\n  booktitle={TACAS},\n  year={2008}\n}\n\n%%% Condorcet / Voting Theory %%%\n\n%%% CoT Faithfulness %%%\n\n@inproceedings{turpin2023language,\n  title={Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting},\n  author={Turpin, Miles and Michael, Julian and Perez, Ethan and Bowman, Samuel},\n  booktitle={NeurIPS},\n  year={2023}\n}\n\n%%% Confirmation Bias in LLM Reasoning %%%\n\n@inproceedings{wan2025unveiling,\n  title={Unveiling Confirmation Bias in Chain-of-Thought Reasoning},\n  author={Wan, Yue and Jia, Xiaowei and Li, Xiang Lorraine},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2025},\n  year={2025}\n}\n\n@article{jhaveri2026failing,\n  title={Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models},\n  author={Jhaveri, Ayush Rajesh and GX-Chen, Anthony and Sucholutsky, Ilia and Choi, Eunsol},\n  journal={arXiv preprint arXiv:2604.02485},\n  year={2026}\n}\n\n@article{miya2025eidoku,\n  title={Eidoku: A Neuro-Symbolic Verification Gate for {LLM} Reasoning via Structural Constraint Satisfaction},\n  author={Miya, Shinobu},\n  journal={arXiv preprint arXiv:2512.20664},\n  year={2025}\n}\n\n%%% Ensemble Diversity %%%\n\n@incollection{dietterich2000ensemble,\n  title={Ensemble Methods in Machine Learning},\n  author={Dietterich, Thomas G.},\n  booktitle={Multiple Classifier Systems (MCS)},\n  pages={1--15},\n  year={2000},\n  publisher={Springer}\n}\n\n@inproceedings{krogh1994neural,\n  title={Neural Network Ensembles, Cross Validation, and Active Learning},\n  author={Krogh, Anders and Vedelsby, Jesper},\n  booktitle={Advances in Neural Information Processing Systems},\n  volume={7},\n  year={1994}\n}\n\n@article{brown2005diversity,\n  title={Diversity Creation Methods: A Survey and Categorisation},\n  author={Brown, Gavin and Wyatt, Jeremy and Harris, Rachel and Yao, Xin},\n  journal={Information Fusion},\n  volume={6},\n  number={1},\n  pages={5--20},\n  year={2005}\n}\n\n%%% Cross-Architecture Verification %%%\n\n@inproceedings{he2021deberta,\n  title={{DeBERTa}: Decoding-enhanced {BERT} with Disentangled Attention},\n  author={He, Pengcheng and Liu, Xiaodong and Gao, Jianfeng and Chen, Weizhu},\n  booktitle={Proceedings of ICLR},\n  year={2021}\n}\n\n@inproceedings{williams2018mnli,\n  title={A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference},\n  author={Williams, Adina and Nangia, Nikita and Bowman, Samuel},\n  booktitle={Proceedings of NAACL-HLT},\n  pages={1112--1122},\n  year={2018}\n}\n\n%%% Compositional / Iterative Neuro-Symbolic Verification %%%\n\n@inproceedings{ryu2025clover,\n  title={Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning},\n  author={Ryu, Hyun and Kim, Gyeongman and Lee, Hyemin S. and Yang, Eunho},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@article{singh2026verge,\n  title={{VERGE}: Formal Refinement and Guidance Engine for Verifiable {LLM} Reasoning},\n  author={Singh, Vikash and Cassel, Darion and Weir, Nathaniel and Feng, Nick and Bayless, Sam},\n  journal={arXiv preprint arXiv:2601.20055},\n  year={2026}\n}\n\n%%% Programs-as-Verifiers %%%\n\n@article{toh2024notallvotes,\n  title={Not All Votes Count! Programs as Verifiers Improve Self-Consistency of Language Models for Math Reasoning},\n  author={Toh, Vernon Y.H. and Ghosal, Deepanway and Poria, Soujanya},\n  journal={arXiv preprint arXiv:2410.12608},\n  year={2024}\n}\n\n%%% Logical Soundness Critique %%%\n\n@article{chan2026position,\n  title={Position: Logical Soundness is not a Reliable Criterion for Neurosymbolic Fact-Checking with {LLMs}},\n  author={Chan, Jason and Gaizauskas, Robert and Zhao, Zhixue},\n  journal={arXiv preprint arXiv:2604.04177},\n  year={2026}\n}\n\n%%% Statistical Methods %%%\n\n@article{lakens2017equivalence,\n  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},\n  author={Lakens, Dani{\\\"e}l},\n  journal={Social Psychological and Personality Science},\n  volume={8},\n  number={4},\n  pages={355--362},\n  year={2017},\n  doi={10.1177/1948550617697177}\n}\n\n%%% R11 Added Citations %%%\n\n@article{byerly2025selfconsistency,\n  title={Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems},\n  author={Byerly, Adam and Khashabi, Daniel},\n  journal={Transactions of the Association for Computational Linguistics},\n  year={2025},\n  note={arXiv:2411.01101}\n}\n\n@article{kuai2026independent,\n  title={How Independent are Large Language Models? {A} Statistical Framework for Auditing Behavioral Entanglement and Reweighting Verifier Ensembles},\n  author={Kuai, Chenchen and Jiang, Jiwan and Zhu, Zihao and Wang, Hao and Wu, Keshu and Li, Zihao and Zhang, Yunlong and Liu, Chenxi and Tu, Zhengzhong and Fan, Zhiwen and Zhou, Yang},\n  journal={arXiv preprint arXiv:2604.07650},\n  year={2026}\n}\n\n@article{kim2025correlated,\n  title={Correlated Errors in Large Language Models},\n  author={Kim, Elliot and Garg, Avi and Peng, Kenny and Garg, Nikhil},\n  journal={arXiv preprint arXiv:2506.07962},\n  year={2025}\n}\n\n@article{chen2025sets,\n  title={{SETS}: Leveraging Self-Verification and Self-Correction for Improved Test-Time Scaling},\n  author={Chen, Jiefeng and Ren, Jie and Chen, Xinyun and Yang, Chengrun and Sun, Ruoxi and Yoon, Jinsung and Ar{\\i}k, Sercan {\\\"O}.},\n  journal={arXiv preprint arXiv:2501.19306},\n  year={2025}\n}\n\n\n\n@article{kuncheva2003measures,\n  title={Measures of Diversity in Classifier Ensembles and Their Relationship with the Ensemble Accuracy},\n  author={Kuncheva, Ludmila I. and Whitaker, Christopher J.},\n  journal={Machine Learning},\n  volume={51},\n  number={2},\n  pages={181--207},\n  year={2003}\n}\n\n%%% Test-Time Scaling and Multi-Agent Verification %%%\n\n@article{lifshitz2025mav,\n  title={Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers},\n  author={Lifshitz, Shalev and McIlraith, Sheila A. and Du, Simon S.},\n  journal={arXiv preprint arXiv:2502.20379},\n  year={2025}\n}\n\n%%% Training-Based Self-Verification %%%\n\n@article{kamoi2024selfcorrect,\n  title={When Can {LLMs} Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of {LLMs}},\n  author={Kamoi, Ryo and Kobayashi, Yusen and Goyal, Tharindu and Hou, Rui and Sun, Hanjie and Caverlee, James},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={12},\n  pages={1--20},\n  year={2024}\n}\n\n\n@inproceedings{zeng2025s2r,\n  title={{S$^2$R}: Teaching {LLMs} to Self-verify and Self-correct via Reinforcement Learning},\n  author={Zeng, Ruotian and Liu, Yuanzhi and others},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2025}\n}\n\n@article{dupo2025,\n  title={{DuPO}: Enabling Reliable {LLM} Self-Verification via Dual Preference Optimization},\n  author={She, Shuaijie and Bao, Yu and Lu, Yu and Xu, Lu and Li, Tao and Zhu, Wenhao and Huang, Shujian and Cheng, Shanbo and Lu, Lu and Wang, Yuxuan},\n  journal={arXiv preprint arXiv:2508.14460},\n  year={2025}\n}\n\n@inproceedings{li2022alphacode,\n  title={Competition-Level Code Generation with {AlphaCode}},\n  author={Li, Yujia and Choi, David and Chung, Junyoung and Kushman, Nate and Schrittwieser, Julian and others},\n  booktitle={Science},\n  volume={378},\n  number={6624},\n  pages={1092--1097},\n  year={2022}\n}\n\n@inproceedings{chen2023codet,\n  title={{CodeT}: Code Generation with Generated Tests},\n  author={Chen, Bei and Zhang, Fengji and Nguyen, Anh and Zan, Daoguang and Lin, Zeqi and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle={Proceedings of the 11th International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n\n@inproceedings{shinn2023reflexion,\n  title={Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author={Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{zhou2023lats,\n  title={Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models},\n  author={Zhou, Andy and Yan, Kai and Shlapentokh-Rothman, Michal and Wang, Haohan and Wang, Yu-Xiong},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024}\n}\n",
      "numLines": 614,
      "startLine": 1,
      "totalLines": 614
    }
  },
  "sourceToolAssistantUUID": "ec45fdf7-c3c2-4529-a18a-8828ff12e53e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T00:04:59.288Z_

<details><summary>↩ Tool result · `toolu_01Qx5cM1vgAnYfZntcfst1fB`</summary>

````text
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
  "parentUuid": "4e931e66-be03-4487-862d-0802f7b2cfcf",
  "isSidechain": false,
  "promptId": "9f9c7037-9fab-4b08-9ced-bd3bebc047c0",
  "type": "user",
  "uuid": "d0d0c6b3-d935-4daa-a442-8f23c37d9a14",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "4e931e66-be03-4487-862d-0802f7b2cfcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T00:04:59.284Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Qx5cM1vgAnYfZntcfst1fB`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dcd3df1-071e-4dea-a411-ddefc2f1860a",
  "isSidechain": false,
  "requestId": "req_011CbNJuk5bUq1XWvCiwji6i",
  "type": "assistant",
  "uuid": "4e931e66-be03-4487-862d-0802f7b2cfcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017H5Xj4JDJCRt9tkUh1r4KU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12159,
      "cache_read_input_tokens": 11841,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12159,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 170,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12159,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12159
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
  "leafUuid": "d0d0c6b3-d935-4daa-a442-8f23c37d9a14",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Add two bib entries to references",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386"
}
```

---

### Assistant

_source line 15 · 2026-05-25T00:05:05.210Z_

<details><summary>Logged reasoning block</summary>

```text
Both papers already exist in the bib file:

1. **Math-Shepherd** — line 190-195, key `wang2024mathshepherd`
2. **GRACE** — line 197-201, key `khalifa2023grace`

No action needed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0d0c6b3-d935-4daa-a442-8f23c37d9a14",
  "isSidechain": false,
  "requestId": "req_011CbNJv5bqxKQ4EfGQqbtFQ",
  "type": "assistant",
  "uuid": "48eee4ca-ace3-4f45-b875-b3f5a567487d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCywHfp3DzBEkV5y9HV2F2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10386,
      "cache_read_input_tokens": 24000,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 141,
          "cache_read_input_tokens": 24000,
          "cache_creation_input_tokens": 10386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10386
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

_source line 16 · 2026-05-25T00:05:05.906Z_

两个条目都已存在：

- **Math-Shepherd**: `wang2024mathshepherd`（第190-195行）
- **GRACE**: `khalifa2023grace`（第197-201行）

无需添加。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48eee4ca-ace3-4f45-b875-b3f5a567487d",
  "isSidechain": false,
  "requestId": "req_011CbNJv5bqxKQ4EfGQqbtFQ",
  "type": "assistant",
  "uuid": "98a54c5f-559b-4620-854e-96e61a0d63fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCywHfp3DzBEkV5y9HV2F2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10386,
      "cache_read_input_tokens": 24000,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 141,
          "cache_read_input_tokens": 24000,
          "cache_creation_input_tokens": 10386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10386
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

_source line 17_

```json
{
  "type": "last-prompt",
  "leafUuid": "98a54c5f-559b-4620-854e-96e61a0d63fc",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Add two bib entries to references",
  "sessionId": "918f3ef6-eada-4f79-bb59-250954707386"
}
```

---
