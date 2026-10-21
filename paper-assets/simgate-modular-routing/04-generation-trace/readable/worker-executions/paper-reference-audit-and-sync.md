# paper reference audit and sync

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_reference-audit-and-sync_20260514T144920.log`
- **Structured JSON:** [`dcbf32b3c36807a5f0a8.json`](../../sessions/dc/dcbf32b3c36807a5f0a8.json)

## Before a recorded user message

32 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
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
  "uuid": "459e8f28-b532-421f-a17a-280adf82e962",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/memory/"
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
    "resetsAt": 1778785200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2d3508eb-47b0-45cc-a4be-ea4f0aded96d",
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this into parallel tasks where possible. First, I need to read the bib file and search for citations in tex files simultaneously, and also list files in both directories.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "b7ab7846-ad81-4478-80da-c01db20cb892",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uhihn5Fkrqf88okaqLDm2x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11353,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11353
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

_source line 5_

开始执行引用审计和目录同步。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "8820a2a8-5d56-4eed-b34d-39ed10a10c71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uhihn5Fkrqf88okaqLDm2x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11353,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11353
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01FRWuqb3KkPcfP4eXnhuQQB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "ee9ad3f8-1982-4ad8-9506-255c36960de9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uhihn5Fkrqf88okaqLDm2x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11353,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11353
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

_source line 7 · 2026-05-14T14:49:38.022Z_

<details><summary>↩ Tool result · `toolu_01FRWuqb3KkPcfP4eXnhuQQB`</summary>

```text
1	@inproceedings{scienceworld-2022,
2	  title={ScienceWorld: Is Your Agent Smarter Than a 5th Grader?},
3	  author={Wang, Ruoyao and Jansen, Peter and C{\^o}t{\'e}, Marc-Alexandre and Ammanabrolu, Prithviraj},
4	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
5	  year={2022}
6	}
7	
8	@inproceedings{toolformer-2024,
9	  title={Toolformer: Language Models Can Teach Themselves to Use Tools},
10	  author={Schick, Timo and Dwivedi-Yu, Jane and Dess{\`i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
11	  booktitle={Advances in Neural Information Processing Systems},
12	  year={2023}
13	}
14	
15	@inproceedings{art-2023,
16	  title={{ART}: Automatic Multi-step Reasoning and Tool-use for Large Language Models},
17	  author={Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio},
18	  booktitle={arXiv preprint arXiv:2303.09014},
19	  year={2023}
20	}
21	
22	@inproceedings{chameleon-2024,
23	  title={Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models},
24	  author={Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng},
25	  booktitle={Advances in Neural Information Processing Systems},
26	  year={2023}
27	}
28	
29	@inproceedings{retool-2026,
30	  title={{ReTool}: Reinforcement Learning for Strategic Tool Use in {LLM}s},
31	  author={Feng, Yutong and Qian, Shengjie and Luo, Boyu and Shi, Yibo and Yang, Ke and Ma, Liang and Zheng, Ling},
32	  booktitle={arXiv preprint arXiv:2504.11536},
33	  year={2025}
34	}
35	
36	@inproceedings{react-2023,
37	  title={{ReAct}: Synergizing Reasoning and Acting in Language Models},
38	  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
39	  booktitle={International Conference on Learning Representations},
40	  year={2023}
41	}
42	
43	@inproceedings{cogrouter-2026,
44	  title={{CogRouter}: Cooperative Policy Optimization for Cognitive Depth Routing},
45	  author={Yang, Ruihan and Li, Zheng and Wang, Yue and Chen, Wei},
46	  booktitle={arXiv preprint arXiv:2503.16783},
47	  year={2026}
48	}
49	
50	@inproceedings{ares-2026,
51	  title={{ARES}: Adaptive Reasoning Effort Scaling for {LLM}s},
52	  author={Yang, Jingbo and Zhao, Chen and Liu, Shuo and Wang, Zhiyu},
53	  booktitle={arXiv preprint arXiv:2501.05661},
54	  year={2026}
55	}
56	
57	@inproceedings{mixture-of-recursions-2025,
58	  title={Mixture of Recursions: Learnable and Efficient Adaptive Processing},
59	  author={Bae, Sangmin and Hwang, Hyungwon and Kim, Jeonghwan and Yun, Se-Young},
60	  booktitle={arXiv preprint arXiv:2501.05470},
61	  year={2025}
62	}
63	
64	@inproceedings{itp-2026,
65	  title={{ITP}: Imagination-Augmented Task Planning with World Model Lookahead},
66	  author={Liu, Youwei and Wang, Zeming and Zhang, Xin and Chen, Yang},
67	  booktitle={arXiv preprint arXiv:2505.02605},
68	  year={2026}
69	}
70	
71	@inproceedings{dynathink-2025,
72	  title={{Dyna-Think}: Integrating World Model Simulation into the Reasoning Loop},
73	  author={Yu, Xiao and Liang, Yuxuan and Wang, Zhen and Sun, Lichao},
74	  booktitle={arXiv preprint arXiv:2502.14458},
75	  year={2025}
76	}
77	
78	@inproceedings{mtrouter-2026,
79	  title={{MTRouter}: Multi-Model Routing for Cost-Efficient Interactive Agents},
80	  author={Zhang, Yiqun and Liu, Yang and Xu, Hongming and Chen, Jian},
81	  booktitle={arXiv preprint arXiv:2504.09750},
82	  year={2026}
83	}
84	
85	@inproceedings{dagger-2011,
86	  title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},
87	  author={Ross, St{\'e}phane and Gordon, Geoffrey J and Bagnell, Drew},
88	  booktitle={Proceedings of the International Conference on Artificial Intelligence and Statistics (AISTATS)},
89	  year={2011}
90	}
91	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "ff54feb3-5f8f-4afe-9f9c-7d0297c4cf0f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/references.bib",
      "content": "@inproceedings{scienceworld-2022,\n  title={ScienceWorld: Is Your Agent Smarter Than a 5th Grader?},\n  author={Wang, Ruoyao and Jansen, Peter and C{\\^o}t{\\'e}, Marc-Alexandre and Ammanabrolu, Prithviraj},\n  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year={2022}\n}\n\n@inproceedings{toolformer-2024,\n  title={Toolformer: Language Models Can Teach Themselves to Use Tools},\n  author={Schick, Timo and Dwivedi-Yu, Jane and Dess{\\`i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{art-2023,\n  title={{ART}: Automatic Multi-step Reasoning and Tool-use for Large Language Models},\n  author={Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio},\n  booktitle={arXiv preprint arXiv:2303.09014},\n  year={2023}\n}\n\n@inproceedings{chameleon-2024,\n  title={Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models},\n  author={Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{retool-2026,\n  title={{ReTool}: Reinforcement Learning for Strategic Tool Use in {LLM}s},\n  author={Feng, Yutong and Qian, Shengjie and Luo, Boyu and Shi, Yibo and Yang, Ke and Ma, Liang and Zheng, Ling},\n  booktitle={arXiv preprint arXiv:2504.11536},\n  year={2025}\n}\n\n@inproceedings{react-2023,\n  title={{ReAct}: Synergizing Reasoning and Acting in Language Models},\n  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},\n  booktitle={International Conference on Learning Representations},\n  year={2023}\n}\n\n@inproceedings{cogrouter-2026,\n  title={{CogRouter}: Cooperative Policy Optimization for Cognitive Depth Routing},\n  author={Yang, Ruihan and Li, Zheng and Wang, Yue and Chen, Wei},\n  booktitle={arXiv preprint arXiv:2503.16783},\n  year={2026}\n}\n\n@inproceedings{ares-2026,\n  title={{ARES}: Adaptive Reasoning Effort Scaling for {LLM}s},\n  author={Yang, Jingbo and Zhao, Chen and Liu, Shuo and Wang, Zhiyu},\n  booktitle={arXiv preprint arXiv:2501.05661},\n  year={2026}\n}\n\n@inproceedings{mixture-of-recursions-2025,\n  title={Mixture of Recursions: Learnable and Efficient Adaptive Processing},\n  author={Bae, Sangmin and Hwang, Hyungwon and Kim, Jeonghwan and Yun, Se-Young},\n  booktitle={arXiv preprint arXiv:2501.05470},\n  year={2025}\n}\n\n@inproceedings{itp-2026,\n  title={{ITP}: Imagination-Augmented Task Planning with World Model Lookahead},\n  author={Liu, Youwei and Wang, Zeming and Zhang, Xin and Chen, Yang},\n  booktitle={arXiv preprint arXiv:2505.02605},\n  year={2026}\n}\n\n@inproceedings{dynathink-2025,\n  title={{Dyna-Think}: Integrating World Model Simulation into the Reasoning Loop},\n  author={Yu, Xiao and Liang, Yuxuan and Wang, Zhen and Sun, Lichao},\n  booktitle={arXiv preprint arXiv:2502.14458},\n  year={2025}\n}\n\n@inproceedings{mtrouter-2026,\n  title={{MTRouter}: Multi-Model Routing for Cost-Efficient Interactive Agents},\n  author={Zhang, Yiqun and Liu, Yang and Xu, Hongming and Chen, Jian},\n  booktitle={arXiv preprint arXiv:2504.09750},\n  year={2026}\n}\n\n@inproceedings{dagger-2011,\n  title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},\n  author={Ross, St{\\'e}phane and Gordon, Geoffrey J and Bagnell, Drew},\n  booktitle={Proceedings of the International Conference on Artificial Intelligence and Statistics (AISTATS)},\n  year={2011}\n}\n",
      "numLines": 91,
      "startLine": 1,
      "totalLines": 91
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Grep · `toolu_01U6YRmNqS3ejWhv49cPpZC3`</summary>

```json
{
  "pattern": "\\\\cite\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex",
  "glob": "*.tex",
  "output_mode": "content",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "c1fd611e-2ccc-406b-b62d-984fb1a6485c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uhihn5Fkrqf88okaqLDm2x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11353,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11353
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

_source line 9 · 2026-05-14T14:49:39.531Z_

<details><summary>↩ Tool result · `toolu_01U6YRmNqS3ejWhv49cPpZC3`</summary>

```text
artifacts/_project/paper/latex/related_work.tex:4:Toolformer \cite{toolformer-2024} inserts API calls via self-supervised filtering;
artifacts/_project/paper/latex/related_work.tex:5:ART \cite{art-2023} delegates tool selection to LLM reasoning chains;
artifacts/_project/paper/latex/related_work.tex:6:Chameleon \cite{chameleon-2024} composes modules under LLM-as-planner orchestration;
artifacts/_project/paper/latex/related_work.tex:7:ReTool \cite{retool-2026} applies RL for implicit code-interpreter invocation.
artifacts/_project/paper/latex/related_work.tex:12:CogRouter \cite{cogrouter-2026} achieves 82.3\% on ScienceWorld (success rate, different evaluation protocol) via cognitive depth routing.
artifacts/_project/paper/latex/related_work.tex:13:ARES \cite{ares-2026} reduces token cost by 52.7\% with per-step reasoning effort selection.
artifacts/_project/paper/latex/related_work.tex:14:Mixture-of-Recursions \cite{mixture-of-recursions-2025} applies adaptive depth via per-token recursive routing.
artifacts/_project/paper/latex/related_work.tex:18:ITP \cite{itp-2026} augments agents with LLM-based world model lookahead;
artifacts/_project/paper/latex/related_work.tex:19:Dyna-Think \cite{dynathink-2025} integrates world model simulation into reasoning, matching 685B performance with 32B at half the token cost.
artifacts/_project/paper/latex/related_work.tex:24:ReAct \cite{react-2023} interleaves reasoning and acting and serves as our internal-reasoning baseline.
artifacts/_project/paper/latex/related_work.tex:25:MTRouter \cite{mtrouter-2026} routes between LLMs for cost optimization on ScienceWorld.
artifacts/_project/paper/latex/experiments.tex:6:We evaluate on ScienceWorld \cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ death penalty. Using the methodology in \S\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 per type). The LLM backbone is Qwen2.5-7B-Instruct served via vLLM with episodes capped at 30 steps.
artifacts/_project/paper/latex/main.tex:33:This work uses ScienceWorld \cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All language models are accessed via standard APIs or publicly released weights. We report computational costs: approximately 40 GPU-hours on two RTX 5090 GPUs for data collection, router training, and evaluation.
artifacts/_project/paper/latex/method.tex:6:Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each modality. Under sparse terminal rewards, this degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.
artifacts/_project/paper/latex/method.tex:8:[Omitted long matching line]
artifacts/_project/paper/latex/introduction.tex:3:[Omitted long matching line]
artifacts/_project/paper/latex/introduction.tex:5:[Omitted long matching line]
artifacts/_project/paper/latex/introduction.tex:7:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "7076f74f-1c94-4482-98ae-70e979f37739",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/latex/related_work.tex:4:Toolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering;\nartifacts/_project/paper/latex/related_work.tex:5:ART \\cite{art-2023} delegates tool selection to LLM reasoning chains;\nartifacts/_project/paper/latex/related_work.tex:6:Chameleon \\cite{chameleon-2024} composes modules under LLM-as-planner orchestration;\nartifacts/_project/paper/latex/related_work.tex:7:ReTool \\cite{retool-2026} applies RL for implicit code-interpreter invocation.\nartifacts/_project/paper/latex/related_work.tex:12:CogRouter \\cite{cogrouter-2026} achieves 82.3\\% on ScienceWorld (success rate, different evaluation protocol) via cognitive depth routing.\nartifacts/_project/paper/latex/related_work.tex:13:ARES \\cite{ares-2026} reduces token cost by 52.7\\% with per-step reasoning effort selection.\nartifacts/_project/paper/latex/related_work.tex:14:Mixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth via per-token recursive routing.\nartifacts/_project/paper/latex/related_work.tex:18:ITP \\cite{itp-2026} augments agents with LLM-based world model lookahead;\nartifacts/_project/paper/latex/related_work.tex:19:Dyna-Think \\cite{dynathink-2025} integrates world model simulation into reasoning, matching 685B performance with 32B at half the token cost.\nartifacts/_project/paper/latex/related_work.tex:24:ReAct \\cite{react-2023} interleaves reasoning and acting and serves as our internal-reasoning baseline.\nartifacts/_project/paper/latex/related_work.tex:25:MTRouter \\cite{mtrouter-2026} routes between LLMs for cost optimization on ScienceWorld.\nartifacts/_project/paper/latex/experiments.tex:6:We evaluate on ScienceWorld \\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ death penalty. Using the methodology in \\S\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 per type). The LLM backbone is Qwen2.5-7B-Instruct served via vLLM with episodes capped at 30 steps.\nartifacts/_project/paper/latex/main.tex:33:This work uses ScienceWorld \\cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All language models are accessed via standard APIs or publicly released weights. We report computational costs: approximately 40 GPU-hours on two RTX 5090 GPUs for data collection, router training, and evaluation.\nartifacts/_project/paper/latex/method.tex:6:Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each modality. Under sparse terminal rewards, this degenerates: on ScienceWorld \\cite{scienceworld-2022}, 97.4\\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\nartifacts/_project/paper/latex/method.tex:8:[Omitted long matching line]\nartifacts/_project/paper/latex/introduction.tex:3:[Omitted long matching line]\nartifacts/_project/paper/latex/introduction.tex:5:[Omitted long matching line]\nartifacts/_project/paper/latex/introduction.tex:7:[Omitted long matching line]",
    "numLines": 18
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01PiUckdYhMRQFrskNzZuGGm`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "e6ce3b68-89cd-4264-b371-b648c92488e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uhihn5Fkrqf88okaqLDm2x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11353,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11353
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

_source line 11 · 2026-05-14T14:49:40.169Z_

<details><summary>↩ Tool result · `toolu_01PiUckdYhMRQFrskNzZuGGm`</summary>

```text
artifacts/_project/paper/latex/abstract.tex
artifacts/_project/paper/latex/related_work.tex
artifacts/_project/paper/latex/discussion.tex
artifacts/_project/paper/latex/main.tex
artifacts/_project/paper/latex/introduction.tex
artifacts/_project/paper/latex/method.tex
artifacts/_project/paper/latex/experiments.tex
artifacts/_project/paper/latex/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "80831abd-1f23-4a48-ace2-5bef341ae5f7",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/latex/abstract.tex",
      "artifacts/_project/paper/latex/related_work.tex",
      "artifacts/_project/paper/latex/discussion.tex",
      "artifacts/_project/paper/latex/main.tex",
      "artifacts/_project/paper/latex/introduction.tex",
      "artifacts/_project/paper/latex/method.tex",
      "artifacts/_project/paper/latex/experiments.tex",
      "artifacts/_project/paper/latex/conclusion.tex"
    ],
    "durationMs": 25,
    "numFiles": 8,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_014yN9xKhJuXmBJ6V9yJEyRM`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "b5102349-bebf-41d4-a505-3c704fb008f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uhihn5Fkrqf88okaqLDm2x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11353,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11353
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

_source line 13 · 2026-05-14T14:49:40.556Z_

<details><summary>↩ Tool result · `toolu_014yN9xKhJuXmBJ6V9yJEyRM`</summary>

```text
docs/paper/related_work.tex
docs/paper/main.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/method.tex
docs/paper/experiments.tex
docs/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "d8fe4412-5257-4b6b-8f9e-2baecce31fcf",
  "tool_use_result": {
    "filenames": [
      "docs/paper/related_work.tex",
      "docs/paper/main.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/method.tex",
      "docs/paper/experiments.tex",
      "docs/paper/conclusion.tex"
    ],
    "durationMs": 14,
    "numFiles": 7,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_01PLa4BQcMBnc1GvSNFAqUZ5`</summary>

```json
{
  "pattern": "*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "f784b87e-5b31-44c1-a86c-259caf316ae6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uhihn5Fkrqf88okaqLDm2x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11353,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11353
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

_source line 15 · 2026-05-14T14:49:41.209Z_

<details><summary>↩ Tool result · `toolu_01PLa4BQcMBnc1GvSNFAqUZ5`</summary>

```text
docs/paper/SETUP_NOTES.md
docs/paper/acl.sty
docs/paper/acl_natbib.bst
docs/paper/related_work.tex
docs/paper/references.bib
docs/paper/main.tex
docs/paper/main.fls
docs/paper/main.fdb_latexmk
docs/paper/_pdf_images/main_p1.png
docs/paper/_pdf_images/main_p2.png
docs/paper/_pdf_images/main_p3.png
docs/paper/_pdf_images/main_p5.png
docs/paper/_pdf_images/main_p4.png
docs/paper/main.blg
docs/paper/main.bbl
docs/paper/main.aux
docs/paper/main.out
docs/paper/main.log
docs/paper/main.pdf
docs/paper/figures/fig1_daf_scatter.pdf
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/method.tex
docs/paper/experiments.tex
docs/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "452a6bcc-4449-48b0-a945-d9fb60e890f9",
  "tool_use_result": {
    "filenames": [
      "docs/paper/SETUP_NOTES.md",
      "docs/paper/acl.sty",
      "docs/paper/acl_natbib.bst",
      "docs/paper/related_work.tex",
      "docs/paper/references.bib",
      "docs/paper/main.tex",
      "docs/paper/main.fls",
      "docs/paper/main.fdb_latexmk",
      "docs/paper/_pdf_images/main_p1.png",
      "docs/paper/_pdf_images/main_p2.png",
      "docs/paper/_pdf_images/main_p3.png",
      "docs/paper/_pdf_images/main_p5.png",
      "docs/paper/_pdf_images/main_p4.png",
      "docs/paper/main.blg",
      "docs/paper/main.bbl",
      "docs/paper/main.aux",
      "docs/paper/main.out",
      "docs/paper/main.log",
      "docs/paper/main.pdf",
      "docs/paper/figures/fig1_daf_scatter.pdf",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/method.tex",
      "docs/paper/experiments.tex",
      "docs/paper/conclusion.tex"
    ],
    "durationMs": 19,
    "numFiles": 25,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the results:

**Bib keys:**
1. scienceworld-2022
2. toolformer-2024
3. art-2023
4. chameleon-2024
5. retool-2026
6. react-2023
7. cogrouter-2026
8. ares-2026
9. mixture-of-recursions-2025
10. itp-2026
11. dynathink-2025
12. mtrouter-2026
13. dagger-2011

**Cited keys from grep:**
- toolformer-2024


- art-2023
- chameleon-2024
- retool-2026
- cogrouter-2026
- ares-2026
- mixture-of-recursions-2025
- itp-2026
- dynathink-2025
- react-2023
- mtrouter-2026
- scienceworld-2022 (appears multiple times)

I need to check the omitted lines in introduction.tex and method.tex to capture all the citations that were truncated in the grep output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "8d0e355a-933d-4746-a10d-e0219eabf0df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RtG53Q3VwQNUCHqtFrapb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3622,
      "cache_read_input_tokens": 23194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3622
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

_source line 17_

有几行被截断了，需要读取完整内容以提取所有 cite key。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "8d57b463-96ee-4881-b614-d15d4e776d93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RtG53Q3VwQNUCHqtFrapb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3622,
      "cache_read_input_tokens": 23194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3622
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

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01TjbBBBpLMvfKYGsBfQ3Pgg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "43fcbaf6-c5d0-4f5b-b833-147b95febf4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RtG53Q3VwQNUCHqtFrapb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3622,
      "cache_read_input_tokens": 23194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3622
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

_source line 19 · 2026-05-14T14:49:48.807Z_

<details><summary>↩ Tool result · `toolu_01TjbBBBpLMvfKYGsBfQ3Pgg`</summary>

```text
1	\section{Introduction}
2	
3	When a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?
4	
5	Existing routing approaches \cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\% of steps produce tied intermediate scores under both strategies across 245 episodes---no step-level signal exists to train a router (\S\ref{sec:collection}).
6	
7	We propose \emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\S\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\Delta_{\text{full}} = +29.60$ points. Excluding death episodes, this gap collapses to $\Delta_{\text{nd}} = +2.84$---a Death Avoidance Factor (DAF; \S\ref{sec:daf}) of 90.41\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), confirming death avoidance as the primary mechanism (\S\ref{sec:death-decomp}). Death rates differ sharply: 42.9\% for internal reasoning versus 16.3\% for deterministic computation. Of 245 episodes, 86 prefer deterministic, 9 prefer internal, and 150 show no preference---96.3\% of oracle decisions match always-deterministic (\S\ref{sec:baselines}).
8	
9	Our contributions:
10	\begin{enumerate}
11	\item \textbf{Episode-level counterfactual methodology.} We introduce episode-level counterfactual analysis with death-aware labeling and the DAF decomposition metric, overcoming per-step oracle degeneracy in sparse-reward environments (\S\ref{sec:collection}, \S\ref{sec:daf}).
12	\item \textbf{Death avoidance dominates routing signal.} Across 11 task types (245 episodes), death avoidance accounts for 90.41\% of the routing signal ($\Delta_{\text{nd}} = +2.84$, 9.6\% of $\Delta_{\text{full}}$). Router training as a diagnostic probe confirms learnable routing structure at the representation level (\S\ref{sec:router-diagnostic}).
13	\end{enumerate}
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "d4943ef3-d7cc-46eb-b4b1-03964f644335",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/introduction.tex",
      "content": "\\section{Introduction}\n\nWhen a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \\cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?\n\nExisting routing approaches \\cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \\emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\\% of steps produce tied intermediate scores under both strategies across 245 episodes---no step-level signal exists to train a router (\\S\\ref{sec:collection}).\n\nWe propose \\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\S\\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\\Delta_{\\text{full}} = +29.60$ points. Excluding death episodes, this gap collapses to $\\Delta_{\\text{nd}} = +2.84$---a Death Avoidance Factor (DAF; \\S\\ref{sec:daf}) of 90.41\\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), confirming death avoidance as the primary mechanism (\\S\\ref{sec:death-decomp}). Death rates differ sharply: 42.9\\% for internal reasoning versus 16.3\\% for deterministic computation. Of 245 episodes, 86 prefer deterministic, 9 prefer internal, and 150 show no preference---96.3\\% of oracle decisions match always-deterministic (\\S\\ref{sec:baselines}).\n\nOur contributions:\n\\begin{enumerate}\n\\item \\textbf{Episode-level counterfactual methodology.} We introduce episode-level counterfactual analysis with death-aware labeling and the DAF decomposition metric, overcoming per-step oracle degeneracy in sparse-reward environments (\\S\\ref{sec:collection}, \\S\\ref{sec:daf}).\n\\item \\textbf{Death avoidance dominates routing signal.} Across 11 task types (245 episodes), death avoidance accounts for 90.41\\% of the routing signal ($\\Delta_{\\text{nd}} = +2.84$, 9.6\\% of $\\Delta_{\\text{full}}$). Router training as a diagnostic probe confirms learnable routing structure at the representation level (\\S\\ref{sec:router-diagnostic}).\n\\end{enumerate}\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01J7fvaMLWSGd1EDsdyo7cEM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "da4ec293-fc7d-4641-9280-a44fc73e603e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RtG53Q3VwQNUCHqtFrapb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3622,
      "cache_read_input_tokens": 23194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3622
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

_source line 21 · 2026-05-14T14:49:49.315Z_

<details><summary>↩ Tool result · `toolu_01J7fvaMLWSGd1EDsdyo7cEM`</summary>

```text
1	\section{Method}
2	
3	\subsection{Counterfactual Episode Collection}
4	\label{sec:collection}
5	
6	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each modality. Under sparse terminal rewards, this degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.
7	
8	For each task instance, we execute two complete episodes under identical initial conditions. The \emph{pure-internal} episode follows the ReAct paradigm \cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction---equivalent to giving the agent a perfect world model.
9	
10	Each episode pair produces a tuple $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$, where $s$ denotes the terminal score and $d \in \{0,1\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. ScienceWorld spans 30 task types with a $-100$ death penalty; after prescreening, we collect 245 episode pairs across 11 task types (20--40 per type).
11	
12	\subsection{Death-Aware Labeling}
13	\label{sec:labeling}
14	
15	Each counterfactual pair receives an episode-level routing label based on $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$. Scores are integer-valued, so we use exact (in)equality. The label is assigned by four mutually exclusive cases:
16	
17	\begin{enumerate}
18	    \item \textbf{Death asymmetry}: $d^{\text{int}} \neq d^{\text{det}}$ $\rightarrow$ surviving strategy preferred.
19	    \item \textbf{Both dead}: $d^{\text{int}} = d^{\text{det}} = 1$ $\rightarrow$ \texttt{no\_preference}.
20	    \item \textbf{Score gap}: both survive, $s^{\text{det}} \neq s^{\text{int}}$ $\rightarrow$ higher-scoring strategy preferred.
21	    \item \textbf{Tied alive}: both survive, $s^{\text{det}} = s^{\text{int}}$ $\rightarrow$ \texttt{no\_preference}.
22	\end{enumerate}
23	
24	\subsection{Death Avoidance Factor}
25	\label{sec:daf}
26	
27	To quantify the contribution of death avoidance to routing signal, we define the Death Avoidance Factor (DAF):
28	\begin{equation}
29	    \text{DAF} = 1 - \frac{\Delta_{\text{nd}}}{\Delta_{\text{full}}}
30	\end{equation}
31	where $\Delta_{\text{full}}$ is the mean score gap ($s^{\text{det}} - s^{\text{int}}$) across all episodes and $\Delta_{\text{nd}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all signal stems from death avoidance; DAF $= 0$ indicates none does. We report results in \S\ref{sec:death-decomp}.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "63fbef1c-1357-4801-a230-effbef78aca8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/method.tex",
      "content": "\\section{Method}\n\n\\subsection{Counterfactual Episode Collection}\n\\label{sec:collection}\n\nPer-step oracle labeling assigns routing labels by comparing single-step outcomes under each modality. Under sparse terminal rewards, this degenerates: on ScienceWorld \\cite{scienceworld-2022}, 97.4\\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\n\nFor each task instance, we execute two complete episodes under identical initial conditions. The \\emph{pure-internal} episode follows the ReAct paradigm \\cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \\emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction---equivalent to giving the agent a perfect world model.\n\nEach episode pair produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes the terminal score and $d \\in \\{0,1\\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. ScienceWorld spans 30 task types with a $-100$ death penalty; after prescreening, we collect 245 episode pairs across 11 task types (20--40 per type).\n\n\\subsection{Death-Aware Labeling}\n\\label{sec:labeling}\n\nEach counterfactual pair receives an episode-level routing label based on $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$. Scores are integer-valued, so we use exact (in)equality. The label is assigned by four mutually exclusive cases:\n\n\\begin{enumerate}\n    \\item \\textbf{Death asymmetry}: $d^{\\text{int}} \\neq d^{\\text{det}}$ $\\rightarrow$ surviving strategy preferred.\n    \\item \\textbf{Both dead}: $d^{\\text{int}} = d^{\\text{det}} = 1$ $\\rightarrow$ \\texttt{no\\_preference}.\n    \\item \\textbf{Score gap}: both survive, $s^{\\text{det}} \\neq s^{\\text{int}}$ $\\rightarrow$ higher-scoring strategy preferred.\n    \\item \\textbf{Tied alive}: both survive, $s^{\\text{det}} = s^{\\text{int}}$ $\\rightarrow$ \\texttt{no\\_preference}.\n\\end{enumerate}\n\n\\subsection{Death Avoidance Factor}\n\\label{sec:daf}\n\nTo quantify the contribution of death avoidance to routing signal, we define the Death Avoidance Factor (DAF):\n\\begin{equation}\n    \\text{DAF} = 1 - \\frac{\\Delta_{\\text{nd}}}{\\Delta_{\\text{full}}}\n\\end{equation}\nwhere $\\Delta_{\\text{full}}$ is the mean score gap ($s^{\\text{det}} - s^{\\text{int}}$) across all episodes and $\\Delta_{\\text{nd}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all signal stems from death avoidance; DAF $= 0$ indicates none does. We report results in \\S\\ref{sec:death-decomp}.\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01BGi64vDrumxktGwFN7vjk6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "1bc39853-9650-48a4-a062-34bdb6635a32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RtG53Q3VwQNUCHqtFrapb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3622,
      "cache_read_input_tokens": 23194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3622
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

_source line 23 · 2026-05-14T14:49:49.706Z_

<details><summary>↩ Tool result · `toolu_01BGi64vDrumxktGwFN7vjk6`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A preliminary 50-problem pilot on MATH Level~4--5, using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 80\% accuracy versus 72\% for code interpreter, with 88\% of problems showing no modality preference (label distribution: 1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld. A larger-scale replication with improved code execution (addressing sandbox limitations in the pilot) is in progress.
6	
7	% TODO: Replace pilot-50 numbers with math-200-fixed results when available
8	
9	\paragraph{Scope and future directions.}
10	Our analysis is grounded in a single interactive environment with a specific failure mode (the $-100$ death penalty). Extending the counterfactual methodology to environments with graded failure costs, embodied agents with continuous action spaces, or multi-turn dialogue systems would clarify how broadly death avoidance---or analogous catastrophic-failure avoidance---accounts for apparent routing signal. Step-level counterfactual labeling, rather than episode-level, is a complementary direction that could reveal finer-grained routing structure masked by our current aggregation.
11	
12	% TODO: ALFWorld results pending; add cross-environment comparison if signal emerges
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "503a3830-b0cd-4d64-ac86-9fd9e7ae798c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Cross-environment evidence.}\nThe death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? A preliminary 50-problem pilot on MATH Level~4--5, using code interpreter as the deterministic modality, suggests not. Internal reasoning achieved 80\\% accuracy versus 72\\% for code interpreter, with 88\\% of problems showing no modality preference (label distribution: 1 deterministic-preferred, 5 internal-preferred, 44 no-preference). In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld. A larger-scale replication with improved code execution (addressing sandbox limitations in the pilot) is in progress.\n\n% TODO: Replace pilot-50 numbers with math-200-fixed results when available\n\n\\paragraph{Scope and future directions.}\nOur analysis is grounded in a single interactive environment with a specific failure mode (the $-100$ death penalty). Extending the counterfactual methodology to environments with graded failure costs, embodied agents with continuous action spaces, or multi-turn dialogue systems would clarify how broadly death avoidance---or analogous catastrophic-failure avoidance---accounts for apparent routing signal. Step-level counterfactual labeling, rather than episode-level, is a complementary direction that could reveal finer-grained routing structure masked by our current aggregation.\n\n% TODO: ALFWorld results pending; add cross-environment comparison if signal emerges\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now let me extract all cite keys from the tex files:

From the grep output and full file reads:

**All cited keys:**
- scienceworld-2022 (introduction.tex, method.tex, experiments.tex, main.tex)
- toolformer-2024 (related_work.tex, introduction.tex)
- art-2023 (related_work.tex, introduction.tex)
- chameleon-2024 (related_work.tex, introduction.tex)
- retool-2026 (related_work.tex)


- react-2023 (related_work.tex, introduction.tex, method.tex)
- cogrouter-2026 (related_work.tex)
- ares-2026 (related_work.tex)
- mixture-of-recursions-2025 (related_work.tex)
- itp-2026 (related_work.tex)
- dynathink-2025 (related_work.tex)
- mtrouter-2026 (related_work.tex)

**Bib keys:**
1. scienceworld-2022
2. toolformer-2024
3. art-2023
4. chameleon-2024

Now I'm checking the full list of cited keys against what's in the bibliography. I see retool-2026, react-2023, cogrouter-2026, ares-2026, mixture-of-recursions-2025, itp-2026, dynathink-2025, mtrouter-2026, and dagger-2011 are all referenced, but dagger-2011 appears in the bib without being cited anywhere. Looking at the entry quality, scienceworld-2022 has all required fields, and toolformer-2024 has a naming inconsistency where the key says 2024 but the actual year is 2023 from NeurIPS.

Continuing through the entries, I notice art-2023 uses "arXiv preprint" as a booktitle which isn't appropriate for an inproceedings entry, and there are several other key-year mismatches: chameleon-2024 and retool-2026 both have keys that don't match their actual publication years. The remaining entries seem consistent between their keys and years.

Looking at the bibliography entries more broadly, I'm seeing a pattern where multiple papers marked as inproceedings are actually arXiv preprints—art-2023, retool-2026, cogrouter-2026, ares-2026, mixture-of-recursions-2025, itp-2026, dynathink-2025, and mtrouter-2026 should probably be recategorized as articles or misc entries instead.

Now I'm comparing the LaTeX files across the two directories. The artifacts directory has the full set of chapter files, while the docs directory has the same structure but is missing the discussion.tex file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "4c3abf93-3a2e-49b8-b93c-42f26ae82726",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017egM7JdPKMAZuV1NyiQYgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 26816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

_source line 25_

Now comparing files between the two directories. Let me read the docs/paper versions to diff.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "9ca0e380-2378-4d26-a981-3f00819b5d33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017egM7JdPKMAZuV1NyiQYgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 26816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01KeSTFM97hvVMCnzM2Pkxuu`</summary>

```json
{
  "command": "for f in abstract.tex introduction.tex method.tex experiments.tex related_work.tex conclusion.tex main.tex references.bib; do echo \"=== $f ===\" ; diff \"artifacts/_project/paper/latex/$f\" \"docs/paper/$f\" 2>&1 || true; echo; done",
  "description": "Diff all shared files between latex/ and docs/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "561a143a-ac73-4671-be9d-3891b3518790",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017egM7JdPKMAZuV1NyiQYgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 26816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

_source line 27 · 2026-05-14T14:50:09.982Z_

<details><summary>↩ Tool result · `toolu_01KeSTFM97hvVMCnzM2Pkxuu`</summary>

```text
&lt;persisted-output>
Output too large (40.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/87e7d2fa-3544-463f-a483-079969decfa9/tool-results/b2rmqqghl.txt

Preview (first 2KB):
=== abstract.tex ===
2,3c2,3
< Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97.4\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Across 245 episodes with a Qwen2.5-7B-Instruct backbone, death avoidance accounts for approximately 90\% of the routing signal (Death Avoidance Factor), with near-perfect cross-task correlation ($r = 0.97$). These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.
< \end{abstract}
---
> LLM agents in rule-governed interactive environments face catastrophic failures when internal reasoning hallucinates state transitions. Deterministic external computation (environment simulators, code interpreters) can prevent such failures, but what does routing between these modalities actually learn? Per-step oracle labeling degenerates under sparse rewards---on ScienceWorld, 97.4\% of steps produce identical scores regardless of modality. We propose episode-level counterfactual analysis: running complete episodes under pure-internal and pure-deterministic strategies to generate routing labels from episode outcomes. Across 11 ScienceWorld task types (245 episodes), we find that death avoidance accounts for 90.41\% of the routing signal between Qwen2.5-7B-Instruct internal reasoning and deterministic computation ($\Delta_{\text{full}} = +29.60$, $\Delta_{\text{nd}} = +2.84$; Pearson $r = 0.9698$, $p = 8.12 \times 10^{-7}$ across task types). When neither strategy causes agent death, the performance gap is small but non-neglig
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "ab8da52d-0731-4453-a479-26a45fc3dae9",
  "tool_use_result": {
    "stdout": "=== abstract.tex ===\n2,3c2,3\n< Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97.4\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Across 245 episodes with a Qwen2.5-7B-Instruct backbone, death avoidance accounts for approximately 90\\% of the routing signal (Death Avoidance Factor), with near-perfect cross-task correlation ($r = 0.97$). These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\n< \\end{abstract}\n---\n> LLM agents in rule-governed interactive environments face catastrophic failures when internal reasoning hallucinates state transitions. Deterministic external computation (environment simulators, code interpreters) can prevent such failures, but what does routing between these modalities actually learn? Per-step oracle labeling degenerates under sparse rewards---on ScienceWorld, 97.4\\% of steps produce identical scores regardless of modality. We propose episode-level counterfactual analysis: running complete episodes under pure-internal and pure-deterministic strategies to generate routing labels from episode outcomes. Across 11 ScienceWorld task types (245 episodes), we find that death avoidance accounts for 90.41\\% of the routing signal between Qwen2.5-7B-Instruct internal reasoning and deterministic computation ($\\Delta_{\\text{full}} = +29.60$, $\\Delta_{\\text{nd}} = +2.84$; Pearson $r = 0.9698$, $p = 8.12 \\times 10^{-7}$ across task types). When neither strategy causes agent death, the performance gap is small but non-negligible ($\\Delta_{\\text{nd}} = +2.84$, 9.6\\% of the total gap). A trained router does not significantly outperform an unconditional always-deterministic strategy ($-10.70$ vs.\\ $-9.47$), confirming that the value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.\n> \\end{abstract}\n\\ No newline at end of file\n\n=== introduction.tex ===\n3c3\n< When a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \\cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?\n---\n> When a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \\cite{scienceworld-2022}, it must track temperature thresholds and container states across dozens of steps. Internal reasoning hallucinates these transitions---predicting water has boiled when the stove was never activated---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?\n5c5\n< Existing routing approaches \\cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \\emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\\% of steps produce tied intermediate scores under both strategies across 245 episodes---no step-level signal exists to train a router (\\S\\ref{sec:collection}).\n---\n> Existing routing approaches \\cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \\emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\\% of steps produce identical scores regardless of modality---no step-level signal exists to train a router (\\S\\ref{sec:collection}). Keyword-based heuristics (\\S\\ref{sec:rule}) also fail structurally: ScienceWorld actions use generic verbs (\\texttt{pour}, \\texttt{move}, \\texttt{activate}) rather than science-specific terminology, providing no lexical basis for routing decisions.\n7c7\n< We propose \\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\S\\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\\Delta_{\\text{full}} = +29.60$ points. Excluding death episodes, this gap collapses to $\\Delta_{\\text{nd}} = +2.84$---a Death Avoidance Factor (DAF; \\S\\ref{sec:daf}) of 90.41\\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), confirming death avoidance as the primary mechanism (\\S\\ref{sec:death-decomp}). Death rates differ sharply: 42.9\\% for internal reasoning versus 16.3\\% for deterministic computation. Of 245 episodes, 86 prefer deterministic, 9 prefer internal, and 150 show no preference---96.3\\% of oracle decisions match always-deterministic (\\S\\ref{sec:baselines}).\n---\n> We propose \\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\S\\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\\Delta_{\\text{full}} = +29.60$ points. Excluding episodes where either strategy causes agent death, this gap collapses to $\\Delta_{\\text{nd}} = +2.84$---a Death Avoidance Factor (DAF; \\S\\ref{sec:daf}) of 90.41\\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), confirming that death avoidance is the primary mechanism across task types (\\S\\ref{sec:death-decomp}). Death rates differ sharply (42.9\\% internal vs.\\ 16.3\\% deterministic), and 96.3\\% of oracle routing decisions match always-deterministic (\\S\\ref{sec:baselines}).\n9,13c9\n< Our contributions:\n< \\begin{enumerate}\n< \\item \\textbf{Episode-level counterfactual methodology.} We introduce episode-level counterfactual analysis with death-aware labeling and the DAF decomposition metric, overcoming per-step oracle degeneracy in sparse-reward environments (\\S\\ref{sec:collection}, \\S\\ref{sec:daf}).\n< \\item \\textbf{Death avoidance dominates routing signal.} Across 11 task types (245 episodes), death avoidance accounts for 90.41\\% of the routing signal ($\\Delta_{\\text{nd}} = +2.84$, 9.6\\% of $\\Delta_{\\text{full}}$). Router training as a diagnostic probe confirms learnable routing structure at the representation level (\\S\\ref{sec:router-diagnostic}).\n< \\end{enumerate}\n---\n> Our contributions: (1) an \\emph{episode-level counterfactual methodology} with death avoidance decomposition via the DAF metric (\\S\\ref{sec:collection}--\\ref{sec:daf}), overcoming per-step oracle degeneracy in sparse-reward environments; and (2) the empirical finding that \\emph{death avoidance accounts for 90.41\\% of routing signal} on ScienceWorld, with a trained router failing to outperform always-deterministic (\\S\\ref{sec:death-decomp}--\\ref{sec:router-diagnostic}).\n\\ No newline at end of file\n\n=== method.tex ===\n6c6\n< Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each modality. Under sparse terminal rewards, this degenerates: on ScienceWorld \\cite{scienceworld-2022}, 97.4\\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\n---\n> Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \\cite{scienceworld-2022}, 97.4\\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\n8c8\n< For each task instance, we execute two complete episodes under identical initial conditions. The \\emph{pure-internal} episode follows the ReAct paradigm \\cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \\emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction---equivalent to giving the agent a perfect world model.\n---\n> For each task instance, we execute two complete episodes under identical initial conditions (same random seed, same task variation). The \\emph{pure-internal} episode follows the ReAct paradigm \\cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \\emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions for each action. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction, not action selection---equivalent to giving the agent access to a perfect world model.\n10c10\n< Each episode pair produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes the terminal score and $d \\in \\{0,1\\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. ScienceWorld spans 30 task types with a $-100$ death penalty; after prescreening, we collect 245 episode pairs across 11 task types (20--40 per type).\n---\n> Each episode pair produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes the terminal score and $d \\in \\{0,1\\}$ indicates agent death. We use Qwen2.5-7B-Instruct (vLLM) on ScienceWorld \\cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty, with episodes capped at 30 steps. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type).\n15c15\n< Each counterfactual pair receives an episode-level routing label based on $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$. Scores are integer-valued, so we use exact (in)equality. The label is assigned by four mutually exclusive cases:\n---\n> Each counterfactual pair receives an episode-level routing label based on $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The label is assigned by one of four mutually exclusive cases:\n18c18\n<     \\item \\textbf{Death asymmetry}: $d^{\\text{int}} \\neq d^{\\text{det}}$ $\\rightarrow$ surviving strategy preferred.\n---\n>     \\item \\textbf{Death asymmetry}: $d^{\\text{int}} \\neq d^{\\text{det}}$ $\\rightarrow$ the surviving strategy is preferred.\n20,21c20,21\n<     \\item \\textbf{Score gap}: both survive, $s^{\\text{det}} \\neq s^{\\text{int}}$ $\\rightarrow$ higher-scoring strategy preferred.\n<     \\item \\textbf{Tied alive}: both survive, $s^{\\text{det}} = s^{\\text{int}}$ $\\rightarrow$ \\texttt{no\\_preference}.\n---\n>     \\item \\textbf{Score comparison}: both survive and $s^{\\text{det}} \\neq s^{\\text{int}}$ $\\rightarrow$ the higher-scoring strategy is preferred.\n>     \\item \\textbf{Tied alive}: both survive and $s^{\\text{det}} = s^{\\text{int}}$ $\\rightarrow$ \\texttt{no\\_preference}.\n23a24,25\n> Label distributions are reported in \\S\\ref{sec:death-decomp}.\n> \n31c33,40\n< where $\\Delta_{\\text{full}}$ is the mean score gap ($s^{\\text{det}} - s^{\\text{int}}$) across all episodes and $\\Delta_{\\text{nd}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all signal stems from death avoidance; DAF $= 0$ indicates none does. We report results in \\S\\ref{sec:death-decomp}.\n---\n> where $\\Delta_{\\text{full}}$ is the mean score gap ($s^{\\text{det}} - s^{\\text{int}}$) across all episodes and $\\Delta_{\\text{nd}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all routing signal stems from death avoidance; DAF $= 0$ indicates all signal stems from non-death performance differences. When $\\Delta_{\\text{full}} = 0$, DAF is undefined, as no routing signal exists to decompose; we report DAF only for task types where $|\\Delta_{\\text{full}}| > 0$.\n> \n> Results using DAF are reported in \\S\\ref{sec:death-decomp}.\n> \n> \\subsection{Rule-Based Baseline}\n> \\label{sec:rule}\n> \n> We test keyword-based routing that selects deterministic computation when the action contains science-related verbs. Three keyword lists of decreasing breadth produce match rates of 85.8\\% (v1, degenerating to always-deterministic), 4.9\\% (v2), and 2.8\\% (v3, both degenerating to always-internal). ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}) rather than science-specific terms; no keyword granularity bridges the gap between near-total and negligible match rates.\n\\ No newline at end of file\n\n=== experiments.tex ===\n3,7d2\n< \\subsection{Setup}\n< \\label{sec:exp-setup}\n< \n< We evaluate on ScienceWorld \\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ death penalty. Using the methodology in \\S\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 per type). The LLM backbone is Qwen2.5-7B-Instruct served via vLLM with episodes capped at 30 steps.\n< \n13,14c8,9\n< \\includegraphics[width=\\columnwidth]{fig1_daf_scatter.pdf}\n< \\caption{Per-task death rate differential (internal minus deterministic) vs.\\ $\\Delta_{\\text{full}}$. Each point represents one of 11 task types. Regression: $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$).}\n---\n> \\includegraphics[width=\\columnwidth]{figures/fig1_daf_scatter.pdf}\n> \\caption{Per-task scatter plot: death rate differential (internal minus deterministic) vs.\\ performance gap ($\\Delta_{\\text{full}}$). Pearson $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$). Each point is one of 11 ScienceWorld task types.}\n18c13\n< The full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. Excluding all episodes where either strategy results in death, the gap collapses to $\\Delta_{\\text{nd}} = +2.84$. The resulting DAF (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage is attributable to death avoidance.\n---\n> The full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\\Delta_{\\text{nd}} = +2.84$. The resulting Death Avoidance Factor (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.\n20c15\n< This concentration is consistent across task types. The Pearson correlation between per-task death rate differential and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$; Figure~\\ref{fig:decomposition}). The internal strategy dies in 42.9\\% of episodes versus 16.3\\% for deterministic---a 2.6$\\times$ ratio driving the bulk of the score difference.\n---\n> This concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), as shown in Figure~\\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\\% of episodes compared to 16.3\\% for deterministic computation---a 2.6$\\times$ ratio that drives the bulk of the observed score difference.\n22c17\n< The label distribution reflects this asymmetry: 86 \\texttt{det\\_preferred}, 9 \\texttt{internal\\_preferred}, 150 \\texttt{no\\_preference}. When internal reasoning does not cause death, it performs comparably to deterministic computation.\n---\n> The episode-level label distribution reflects this asymmetry: of 245 episodes, 86 are \\texttt{det\\_preferred}, only 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}---when internal reasoning does not cause death, it performs comparably to deterministic computation.\n24c19\n< One task reveals residual non-death signal: \\texttt{find-non-living-thing} ($n=40$) has zero deaths yet $\\Delta_{\\text{full}} = +9.58$, entirely from non-death differences. Among the 10 death-prone task types, however, death avoidance overwhelms non-death signal.\n---\n> One task reveals the residual non-death signal. \\texttt{find-non-living-thing} ($n=40$) has zero deaths under both strategies yet shows $\\Delta_{\\text{full}} = +9.58$, entirely from non-death performance differences---deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, among the 10 death-prone task types, death avoidance overwhelms non-death differences. When both modalities survive, the gap is small but non-negligible ($\\Delta_{\\text{nd}} = +2.84$, 9.6\\% of $\\Delta_{\\text{full}}$).\n34c29\n< Strategy & Score & 95\\% CI & Death \\% \\\\\n---\n> Strategy & Score & 90\\% CI & Death \\% \\\\\n36,39c31,34\n< Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\\\\n< Always-Det. & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\\\\n< Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\\\\n< Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\\\\n---\n> Always-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\\\\n> Always-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\\\\n> Random & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\\\\n> Oracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\\\\n41c36\n< Trained Router & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\\\\n---\n> Trained Router & $-10.70$ & [$-15.25$, $-6.38$] & 17.6 \\\\\n44c39\n< \\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). 95\\% Bootstrap CIs. The oracle selects the higher-scoring strategy per episode; 96.3\\% of its decisions match always-deterministic.}\n---\n> \\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). 90\\% confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.3\\% of its decisions match the always-deterministic strategy.}\n48,50c43\n< Table~\\ref{tab:baselines} reports episode-weighted mean scores and death rates. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle improves only modestly to $-6.58$, with 96.3\\% of its decisions matching always-deterministic---\\emph{oracle degeneracy} indicating the optimal routing policy closely resembles unconditional deterministic computation. Random routing ($-22.38$) falls between the two pure strategies.\n< \n< Keyword-based routing fails structurally: ScienceWorld actions use generic verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing match rates to cluster at extremes---near-total (85.8\\%, degenerating to always-deterministic) or negligible ($<$5\\%, degenerating to always-internal).\n---\n> Table~\\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.3\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.\n52c45\n< The trained router (\\S\\ref{sec:router-diagnostic}) scores $-10.70$, 1.23 points below always-deterministic, with comparable death rate (17.6\\% vs.\\ 16.3\\%).\n---\n> Keyword-based routing (\\S\\ref{sec:rule}) fails structurally: match rates cluster at extremes (85.8\\% or $<$5\\%), precluding meaningful routing discrimination.\n57c50,56\n< We investigate whether episode-level counterfactual labels can train a step-level router, as a diagnostic probe rather than a routing system proposal.\n---\n> A natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.\n> \n> \\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.\n> \n> \\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. Gradient accumulation is critical: with gradient accumulation of 1, the model fails to achieve meaningful routing discrimination (internal recall 26.7\\%); with gradient accumulation of 8, the model becomes non-degenerate (internal recall above 50\\% across all seeds). We report results for the non-degenerate configuration (gradient accumulation 8). At both the logit and generation levels, accuracy is 65.4\\%, balanced accuracy 59.3\\%, and internal recall 51.5\\%---no logit-generation gap exists for this configuration, demonstrating a weak but above-chance routing signal beyond what a degenerate always-deterministic predictor captures.\n> \n> \\paragraph{Cross-seed stability.} Balanced accuracy is stable across seeds (57--59\\%), but internal recall varies from 51.5\\% to 81.8\\%---the signal exists but is insufficient for practical routing, consistent with the death avoidance decomposition: when ${\\sim}90\\%$ of routing value is death avoidance, the learnable non-death signal is structurally thin.\n59c58\n< \\paragraph{Classification head.} A linear head appended to the LLM's hidden representations degenerates to always-deterministic (0\\% internal recall) across all configurations (class weighting, focal loss, undersampling, temperature scaling).\n---\n> \\paragraph{End-to-end evaluation.} Deployed as an episode-level router (Table~\\ref{tab:baselines}), the trained router scores $-10.70$ (90\\% CI $[-15.25, -6.38]$) with 17.6\\% death rate, allocating 97.0\\% of episodes to deterministic computation. It did not significantly outperform always-deterministic ($-9.47$, $[-13.66, -5.11]$)---CIs overlap substantially. The few internally-routed episodes include cases where the agent dies, and misrouting cost exceeds the benefit of correctly routing rare internal-preferred episodes. This is a direct corollary of death avoidance dominance: any router that occasionally routes internally risks catastrophic failure, while always-deterministic avoids this risk entirely.\n61c60\n< \\paragraph{Implicit router.} We fine-tune Qwen3-1.7B to internalize routing decisions. Training configuration significantly affects results. With gradient accumulation GA=8 (effective batch size 32), the model achieves generation accuracy of 65.4\\% with internal recall of 51.5\\%---the only non-degenerate configuration. With GA=1 (effective batch size 4), logit-level accuracy reaches 74.5\\% (balanced accuracy 79\\%), but generation degenerates to 53.3\\% accuracy with only 26.7\\% internal recall---a 21.2 percentage point logit--generation gap. Effective batch size determines whether learned patterns transfer to generation.\n---\n> Three observations follow. First, logit-level success rules out uninformative labels, pointing to the episode-to-step granularity mismatch as the classification head bottleneck. Second, in death-dominated environments, always-deterministic is near-optimal and any learned router must overcome asymmetric misrouting cost (death vs.\\ marginal score improvement). Third, when DAF $\\approx 90\\%$, router headroom is structurally limited to the ${\\sim}10\\%$ non-death signal.\n63c62\n< Across four seeds (GA=8), balanced accuracy is $58.1 \\pm 0.8\\%$---8 points above chance. Internal recall varies from 51.5\\% to 81.8\\%, indicating seed-dependent boundaries with consistent weak discriminability. End-to-end (Table~\\ref{tab:baselines}): the router's 97.0\\% simulator invocation ratio means it routes internally only 3\\% of the time---weak signal with unstable thresholds, consistent with minimal routing structure beyond death avoidance.\n---\n> \\paragraph{Labeling quality.} We verify that the episode-level counterfactual labels are free of oracle circularity. Of 245 episodes, 0\\% of oracle routing decisions are determined by tie-breaking rules---all are based on genuine score differences. The remaining 61.2\\% of episodes are ties (46.9\\% both-alive, 14.3\\% both-died) and are excluded from training. Retraining the implicit router on strict-only (non-tie) labels yields balanced accuracy of 0.5729, consistent with the full-label result (0.5761 $\\pm$ 0.005), confirming that the labeling methodology introduces no circular signal.\n\\ No newline at end of file\n\n=== related_work.tex ===\n4,9c4,5\n< Toolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering;\n< ART \\cite{art-2023} delegates tool selection to LLM reasoning chains;\n< Chameleon \\cite{chameleon-2024} composes modules under LLM-as-planner orchestration;\n< ReTool \\cite{retool-2026} applies RL for implicit code-interpreter invocation.\n< These methods learn \\emph{which tool} to use but do not analyze what signal drives routing.\n< We generate labels via \\emph{episode-level counterfactual analysis} and diagnose what the signal encodes---revealing ${\\sim}90\\%$ is death avoidance.\n---\n> Toolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering; ART \\cite{art-2023} and Chameleon \\cite{chameleon-2024} compose tools under LLM orchestration; ReTool \\cite{retool-2026} applies RL for code-interpreter invocation.\n> We differ by generating routing labels via \\emph{episode-level counterfactual analysis}, framing routing as \\emph{catastrophic failure prevention}, and training an explicit lightweight router for diagnostic analysis.\n12,15c8,10\n< CogRouter \\cite{cogrouter-2026} achieves 82.3\\% on ScienceWorld (success rate, different evaluation protocol) via cognitive depth routing.\n< ARES \\cite{ares-2026} reduces token cost by 52.7\\% with per-step reasoning effort selection.\n< Mixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth via per-token recursive routing.\n< These route \\emph{how much} to reason; we route \\emph{which modality}. None quantify routing signal composition.\n---\n> CogRouter \\cite{cogrouter-2026} routes among cognitive depth levels on ScienceWorld; ARES \\cite{ares-2026} selects per-step reasoning effort; Mixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level.\n> MTRouter \\cite{mtrouter-2026} routes among LLMs to optimize cost-quality tradeoffs.\n> These methods route \\emph{how much} or \\emph{which model}; we route \\emph{which modality} and find that death avoidance accounts for ${\\sim}90\\%$ of the routing signal.\n18,21c13,14\n< ITP \\cite{itp-2026} augments agents with LLM-based world model lookahead;\n< Dyna-Think \\cite{dynathink-2025} integrates world model simulation into reasoning, matching 685B performance with 32B at half the token cost.\n< Both route to \\emph{approximate} world models inheriting LLM hallucinations.\n< Our deterministic modality provides \\emph{exact} state transitions; counterfactual analysis shows this exactness matters almost exclusively for death avoidance.\n---\n> ITP \\cite{itp-2026} and Dyna-Think \\cite{dynathink-2025} route to approximate LLM-based world models that inherit hallucination failures.\n> Our deterministic modality provides exact state transitions, and our analysis reveals that this exactness matters almost exclusively for death avoidance.\n24,26c17\n< ReAct \\cite{react-2023} interleaves reasoning and acting and serves as our internal-reasoning baseline.\n< MTRouter \\cite{mtrouter-2026} routes between LLMs for cost optimization on ScienceWorld.\n< Our work asks what a learned router captures---the answer is dominated by catastrophic-failure prevention, suggesti",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/87e7d2fa-3544-463f-a483-079969decfa9/tool-results/b2rmqqghl.txt",
    "persistedOutputSize": 41097
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01KZT1koMnPR5xr2uis9anXg`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/87e7d2fa-3544-463f-a483-079969decfa9/tool-results/b2rmqqghl.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "4d2585ed-56ae-4b16-b208-625498f721cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hqauUf4JvkrEYaBbNE7kU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1848,
      "cache_read_input_tokens": 29752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1848
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

_source line 29 · 2026-05-14T14:50:13.679Z_

<details><summary>↩ Tool result · `toolu_01KZT1koMnPR5xr2uis9anXg`</summary>

```text
1	=== abstract.tex ===
2	2,3c2,3
3	< Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97.4\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Across 245 episodes with a Qwen2.5-7B-Instruct backbone, death avoidance accounts for approximately 90\% of the routing signal (Death Avoidance Factor), with near-perfect cross-task correlation ($r = 0.97$). These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.
4	< \end{abstract}
5	---
6	> LLM agents in rule-governed interactive environments face catastrophic failures when internal reasoning hallucinates state transitions. Deterministic external computation (environment simulators, code interpreters) can prevent such failures, but what does routing between these modalities actually learn? Per-step oracle labeling degenerates under sparse rewards---on ScienceWorld, 97.4\% of steps produce identical scores regardless of modality. We propose episode-level counterfactual analysis: running complete episodes under pure-internal and pure-deterministic strategies to generate routing labels from episode outcomes. Across 11 ScienceWorld task types (245 episodes), we find that death avoidance accounts for 90.41\% of the routing signal between Qwen2.5-7B-Instruct internal reasoning and deterministic computation ($\Delta_{\text{full}} = +29.60$, $\Delta_{\text{nd}} = +2.84$; Pearson $r = 0.9698$, $p = 8.12 \times 10^{-7}$ across task types). When neither strategy causes agent death, the performance gap is small but non-negligible ($\Delta_{\text{nd}} = +2.84$, 9.6\% of the total gap). A trained router does not significantly outperform an unconditional always-deterministic strategy ($-10.70$ vs.\ $-9.47$), confirming that the value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.
7	> \end{abstract}
8	\ No newline at end of file
9	
10	=== introduction.tex ===
11	3c3
12	< When a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?
13	---
14	> When a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \cite{scienceworld-2022}, it must track temperature thresholds and container states across dozens of steps. Internal reasoning hallucinates these transitions---predicting water has boiled when the stove was never activated---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?
15	5c5
16	< Existing routing approaches \cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\% of steps produce tied intermediate scores under both strategies across 245 episodes---no step-level signal exists to train a router (\S\ref{sec:collection}).
17	---
18	> Existing routing approaches \cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\% of steps produce identical scores regardless of modality---no step-level signal exists to train a router (\S\ref{sec:collection}). Keyword-based heuristics (\S\ref{sec:rule}) also fail structurally: ScienceWorld actions use generic verbs (\texttt{pour}, \texttt{move}, \texttt{activate}) rather than science-specific terminology, providing no lexical basis for routing decisions.
19	7c7
20	< We propose \emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\S\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\Delta_{\text{full}} = +29.60$ points. Excluding death episodes, this gap collapses to $\Delta_{\text{nd}} = +2.84$---a Death Avoidance Factor (DAF; \S\ref{sec:daf}) of 90.41\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), confirming death avoidance as the primary mechanism (\S\ref{sec:death-decomp}). Death rates differ sharply: 42.9\% for internal reasoning versus 16.3\% for deterministic computation. Of 245 episodes, 86 prefer deterministic, 9 prefer internal, and 150 show no preference---96.3\% of oracle decisions match always-deterministic (\S\ref{sec:baselines}).
21	---
22	> We propose \emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\S\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\Delta_{\text{full}} = +29.60$ points. Excluding episodes where either strategy causes agent death, this gap collapses to $\Delta_{\text{nd}} = +2.84$---a Death Avoidance Factor (DAF; \S\ref{sec:daf}) of 90.41\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), confirming that death avoidance is the primary mechanism across task types (\S\ref{sec:death-decomp}). Death rates differ sharply (42.9\% internal vs.\ 16.3\% deterministic), and 96.3\% of oracle routing decisions match always-deterministic (\S\ref{sec:baselines}).
23	9,13c9
24	< Our contributions:
25	< \begin{enumerate}
26	< \item \textbf{Episode-level counterfactual methodology.} We introduce episode-level counterfactual analysis with death-aware labeling and the DAF decomposition metric, overcoming per-step oracle degeneracy in sparse-reward environments (\S\ref{sec:collection}, \S\ref{sec:daf}).
27	< \item \textbf{Death avoidance dominates routing signal.} Across 11 task types (245 episodes), death avoidance accounts for 90.41\% of the routing signal ($\Delta_{\text{nd}} = +2.84$, 9.6\% of $\Delta_{\text{full}}$). Router training as a diagnostic probe confirms learnable routing structure at the representation level (\S\ref{sec:router-diagnostic}).
28	< \end{enumerate}
29	---
30	> Our contributions: (1) an \emph{episode-level counterfactual methodology} with death avoidance decomposition via the DAF metric (\S\ref{sec:collection}--\ref{sec:daf}), overcoming per-step oracle degeneracy in sparse-reward environments; and (2) the empirical finding that \emph{death avoidance accounts for 90.41\% of routing signal} on ScienceWorld, with a trained router failing to outperform always-deterministic (\S\ref{sec:death-decomp}--\ref{sec:router-diagnostic}).
31	\ No newline at end of file
32	
33	=== method.tex ===
34	6c6
35	< Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each modality. Under sparse terminal rewards, this degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.
36	---
37	> Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.
38	8c8
39	< For each task instance, we execute two complete episodes under identical initial conditions. The \emph{pure-internal} episode follows the ReAct paradigm \cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction---equivalent to giving the agent a perfect world model.
40	---
41	> For each task instance, we execute two complete episodes under identical initial conditions (same random seed, same task variation). The \emph{pure-internal} episode follows the ReAct paradigm \cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions for each action. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction, not action selection---equivalent to giving the agent access to a perfect world model.
42	10c10
43	< Each episode pair produces a tuple $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$, where $s$ denotes the terminal score and $d \in \{0,1\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. ScienceWorld spans 30 task types with a $-100$ death penalty; after prescreening, we collect 245 episode pairs across 11 task types (20--40 per type).
44	---
45	> Each episode pair produces a tuple $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$, where $s$ denotes the terminal score and $d \in \{0,1\}$ indicates agent death. We use Qwen2.5-7B-Instruct (vLLM) on ScienceWorld \cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty, with episodes capped at 30 steps. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type).
46	15c15
47	< Each counterfactual pair receives an episode-level routing label based on $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$. Scores are integer-valued, so we use exact (in)equality. The label is assigned by four mutually exclusive cases:
48	---
49	> Each counterfactual pair receives an episode-level routing label based on $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The label is assigned by one of four mutually exclusive cases:
50	18c18
51	<     \item \textbf{Death asymmetry}: $d^{\text{int}} \neq d^{\text{det}}$ $\rightarrow$ surviving strategy preferred.
52	---
53	>     \item \textbf{Death asymmetry}: $d^{\text{int}} \neq d^{\text{det}}$ $\rightarrow$ the surviving strategy is preferred.
54	20,21c20,21
55	<     \item \textbf{Score gap}: both survive, $s^{\text{det}} \neq s^{\text{int}}$ $\rightarrow$ higher-scoring strategy preferred.
56	<     \item \textbf{Tied alive}: both survive, $s^{\text{det}} = s^{\text{int}}$ $\rightarrow$ \texttt{no\_preference}.
57	---
58	>     \item \textbf{Score comparison}: both survive and $s^{\text{det}} \neq s^{\text{int}}$ $\rightarrow$ the higher-scoring strategy is preferred.
59	>     \item \textbf{Tied alive}: both survive and $s^{\text{det}} = s^{\text{int}}$ $\rightarrow$ \texttt{no\_preference}.
60	23a24,25
61	> Label distributions are reported in \S\ref{sec:death-decomp}.
62	> 
63	31c33,40
64	< where $\Delta_{\text{full}}$ is the mean score gap ($s^{\text{det}} - s^{\text{int}}$) across all episodes and $\Delta_{\text{nd}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all signal stems from death avoidance; DAF $= 0$ indicates none does. We report results in \S\ref{sec:death-decomp}.
65	---
66	> where $\Delta_{\text{full}}$ is the mean score gap ($s^{\text{det}} - s^{\text{int}}$) across all episodes and $\Delta_{\text{nd}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all routing signal stems from death avoidance; DAF $= 0$ indicates all signal stems from non-death performance differences. When $\Delta_{\text{full}} = 0$, DAF is undefined, as no routing signal exists to decompose; we report DAF only for task types where $|\Delta_{\text{full}}| > 0$.
67	> 
68	> Results using DAF are reported in \S\ref{sec:death-decomp}.
69	> 
70	> \subsection{Rule-Based Baseline}
71	> \label{sec:rule}
72	> 
73	> We test keyword-based routing that selects deterministic computation when the action contains science-related verbs. Three keyword lists of decreasing breadth produce match rates of 85.8\% (v1, degenerating to always-deterministic), 4.9\% (v2), and 2.8\% (v3, both degenerating to always-internal). ScienceWorld actions use generic interaction verbs (\texttt{pick up}, \texttt{move}) rather than science-specific terms; no keyword granularity bridges the gap between near-total and negligible match rates.
74	\ No newline at end of file
75	
76	=== experiments.tex ===
77	3,7d2
78	< \subsection{Setup}
79	< \label{sec:exp-setup}
80	< 
81	< We evaluate on ScienceWorld \cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ death penalty. Using the methodology in \S\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 per type). The LLM backbone is Qwen2.5-7B-Instruct served via vLLM with episodes capped at 30 steps.
82	< 
83	13,14c8,9
84	< \includegraphics[width=\columnwidth]{fig1_daf_scatter.pdf}
85	< \caption{Per-task death rate differential (internal minus deterministic) vs.\ $\Delta_{\text{full}}$. Each point represents one of 11 task types. Regression: $r = 0.9698$ ($p = 8.12 \times 10^{-7}$).}
86	---
87	> \includegraphics[width=\columnwidth]{figures/fig1_daf_scatter.pdf}
88	> \caption{Per-task scatter plot: death rate differential (internal minus deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). Pearson $r = 0.9698$ ($p = 8.12 \times 10^{-7}$). Each point is one of 11 ScienceWorld task types.}
89	18c13
90	< The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. Excluding all episodes where either strategy results in death, the gap collapses to $\Delta_{\text{nd}} = +2.84$. The resulting DAF (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage is attributable to death avoidance.
91	---
92	> The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\Delta_{\text{nd}} = +2.84$. The resulting Death Avoidance Factor (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.
93	20c15
94	< This concentration is consistent across task types. The Pearson correlation between per-task death rate differential and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$; Figure~\ref{fig:decomposition}). The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic---a 2.6$\times$ ratio driving the bulk of the score difference.
95	---
96	> This concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), as shown in Figure~\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\% of episodes compared to 16.3\% for deterministic computation---a 2.6$\times$ ratio that drives the bulk of the observed score difference.
97	22c17
98	< The label distribution reflects this asymmetry: 86 \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, 150 \texttt{no\_preference}. When internal reasoning does not cause death, it performs comparably to deterministic computation.
99	---
100	> The episode-level label distribution reflects this asymmetry: of 245 episodes, 86 are \texttt{det\_preferred}, only 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}---when internal reasoning does not cause death, it performs comparably to deterministic computation.
101	24c19
102	< One task reveals residual non-death signal: \texttt{find-non-living-thing} ($n=40$) has zero deaths yet $\Delta_{\text{full}} = +9.58$, entirely from non-death differences. Among the 10 death-prone task types, however, death avoidance overwhelms non-death signal.
103	---
104	> One task reveals the residual non-death signal. \texttt{find-non-living-thing} ($n=40$) has zero deaths under both strategies yet shows $\Delta_{\text{full}} = +9.58$, entirely from non-death performance differences---deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, among the 10 death-prone task types, death avoidance overwhelms non-death differences. When both modalities survive, the gap is small but non-negligible ($\Delta_{\text{nd}} = +2.84$, 9.6\% of $\Delta_{\text{full}}$).
105	34c29
106	< Strategy & Score & 95\% CI & Death \% \\
107	---
108	> Strategy & Score & 90\% CI & Death \% \\
109	36,39c31,34
110	< Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\
111	< Always-Det. & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\
112	< Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\
113	< Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\
114	---
115	> Always-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\
116	> Always-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\
117	> Random & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\
118	> Oracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\
119	41c36
120	< Trained Router & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\
121	---
122	> Trained Router & $-10.70$ & [$-15.25$, $-6.38$] & 17.6 \\
123	44c39
124	< \caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). 95\% Bootstrap CIs. The oracle selects the higher-scoring strategy per episode; 96.3\% of its decisions match always-deterministic.}
125	---
126	> \caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). 90\% confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.3\% of its decisions match the always-deterministic strategy.}
127	48,50c43
128	< Table~\ref{tab:baselines} reports episode-weighted mean scores and death rates. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\Delta_{\text{full}}$. The oracle improves only modestly to $-6.58$, with 96.3\% of its decisions matching always-deterministic---\emph{oracle degeneracy} indicating the optimal routing policy closely resembles unconditional deterministic computation. Random routing ($-22.38$) falls between the two pure strategies.
129	< 
130	< Keyword-based routing fails structurally: ScienceWorld actions use generic verbs (\texttt{pick up}, \texttt{move}, \texttt{connect}) rather than science-specific terms, causing match rates to cluster at extremes---near-total (85.8\%, degenerating to always-deterministic) or negligible ($<$5\%, degenerating to always-internal).
131	---
132	> Table~\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\Delta_{\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.3\% of its routing decisions matching always-deterministic. This \emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\%) proportional to its 50/50 allocation.
133	52c45
134	< The trained router (\S\ref{sec:router-diagnostic}) scores $-10.70$, 1.23 points below always-deterministic, with comparable death rate (17.6\% vs.\ 16.3\%).
135	---
136	> Keyword-based routing (\S\ref{sec:rule}) fails structurally: match rates cluster at extremes (85.8\% or $<$5\%), precluding meaningful routing discrimination.
137	57c50,56
138	< We investigate whether episode-level counterfactual labels can train a step-level router, as a diagnostic probe rather than a routing system proposal.
139	---
140	> A natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.
141	> 
142	> \paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.
143	> 
144	> \paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. Gradient accumulation is critical: with gradient accumulation of 1, the model fails to achieve meaningful routing discrimination (internal recall 26.7\%); with gradient accumulation of 8, the model becomes non-degenerate (internal recall above 50\% across all seeds). We report results for the non-degenerate configuration (gradient accumulation 8). At both the logit and generation levels, accuracy is 65.4\%, balanced accuracy 59.3\%, and internal recall 51.5\%---no logit-generation gap exists for this configuration, demonstrating a weak but above-chance routing signal beyond what a degenerate always-deterministic predictor captures.
145	> 
146	> \paragraph{Cross-seed stability.} Balanced accuracy is stable across seeds (57--59\%), but internal recall varies from 51.5\% to 81.8\%---the signal exists but is insufficient for practical routing, consistent with the death avoidance decomposition: when ${\sim}90\%$ of routing value is death avoidance, the learnable non-death signal is structurally thin.
147	59c58
148	< \paragraph{Classification head.} A linear head appended to the LLM's hidden representations degenerates to always-deterministic (0\% internal recall) across all configurations (class weighting, focal loss, undersampling, temperature scaling).
149	---
150	> \paragraph{End-to-end evaluation.} Deployed as an episode-level router (Table~\ref{tab:baselines}), the trained router scores $-10.70$ (90\% CI $[-15.25, -6.38]$) with 17.6\% death rate, allocating 97.0\% of episodes to deterministic computation. It did not significantly outperform always-deterministic ($-9.47$, $[-13.66, -5.11]$)---CIs overlap substantially. The few internally-routed episodes include cases where the agent dies, and misrouting cost exceeds the benefit of correctly routing rare internal-preferred episodes. This is a direct corollary of death avoidance dominance: any router that occasionally routes internally risks catastrophic failure, while always-deterministic avoids this risk entirely.
151	61c60
152	< \paragraph{Implicit router.} We fine-tune Qwen3-1.7B to internalize routing decisions. Training configuration significantly affects results. With gradient accumulation GA=8 (effective batch size 32), the model achieves generation accuracy of 65.4\% with internal recall of 51.5\%---the only non-degenerate configuration. With GA=1 (effective batch size 4), logit-level accuracy reaches 74.5\% (balanced accuracy 79\%), but generation degenerates to 53.3\% accuracy with only 26.7\% internal recall---a 21.2 percentage point logit--generation gap. Effective batch size determines whether learned patterns transfer to generation.
153	---
154	> Three observations follow. First, logit-level success rules out uninformative labels, pointing to the episode-to-step granularity mismatch as the classification head bottleneck. Second, in death-dominated environments, always-deterministic is near-optimal and any learned router must overcome asymmetric misrouting cost (death vs.\ marginal score improvement). Third, when DAF $\approx 90\%$, router headroom is structurally limited to the ${\sim}10\%$ non-death signal.
155	63c62
156	< Across four seeds (GA=8), balanced accuracy is $58.1 \pm 0.8\%$---8 points above chance. Internal recall varies from 51.5\% to 81.8\%, indicating seed-dependent boundaries with consistent weak discriminability. End-to-end (Table~\ref{tab:baselines}): the router's 97.0\% simulator invocation ratio means it routes internally only 3\% of the time---weak signal with unstable thresholds, consistent with minimal routing structure beyond death avoidance.
157	---
158	> \paragraph{Labeling quality.} We verify that the episode-level counterfactual labels are free of oracle circularity. Of 245 episodes, 0\% of oracle routing decisions are determined by tie-breaking rules---all are based on genuine score differences. The remaining 61.2\% of episodes are ties (46.9\% both-alive, 14.3\% both-died) and are excluded from training. Retraining the implicit router on strict-only (non-tie) labels yields balanced accuracy of 0.5729, consistent with the full-label result (0.5761 $\pm$ 0.005), confirming that the labeling methodology introduces no circular signal.
159	\ No newline at end of file
160	
161	=== related_work.tex ===
162	4,9c4,5
163	< Toolformer \cite{toolformer-2024} inserts API calls via self-supervised filtering;
164	< ART \cite{art-2023} delegates tool selection to LLM reasoning chains;
165	< Chameleon \cite{chameleon-2024} composes modules under LLM-as-planner orchestration;
166	< ReTool \cite{retool-2026} applies RL for implicit code-interpreter invocation.
167	< These methods learn \emph{which tool} to use but do not analyze what signal drives routing.
168	< We generate labels via \emph{episode-level counterfactual analysis} and diagnose what the signal encodes---revealing ${\sim}90\%$ is death avoidance.
169	---
170	> Toolformer \cite{toolformer-2024} inserts API calls via self-supervised filtering; ART \cite{art-2023} and Chameleon \cite{chameleon-2024} compose tools under LLM orchestration; ReTool \cite{retool-2026} applies RL for code-interpreter invocation.
171	> We differ by generating routing labels via \emph{episode-level counterfactual analysis}, framing routing as \emph{catastrophic failure prevention}, and training an explicit lightweight router for diagnostic analysis.
172	12,15c8,10
173	< CogRouter \cite{cogrouter-2026} achieves 82.3\% on ScienceWorld (success rate, different evaluation protocol) via cognitive depth routing.
174	< ARES \cite{ares-2026} reduces token cost by 52.7\% with per-step reasoning effort selection.
175	< Mixture-of-Recursions \cite{mixture-of-recursions-2025} applies adaptive depth via per-token recursive routing.
176	< These route \emph{how much} to reason; we route \emph{which modality}. None quantify routing signal composition.
177	---
178	> CogRouter \cite{cogrouter-2026} routes among cognitive depth levels on ScienceWorld; ARES \cite{ares-2026} selects per-step reasoning effort; Mixture-of-Recursions \cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level.
179	> MTRouter \cite{mtrouter-2026} routes among LLMs to optimize cost-quality tradeoffs.
180	> These methods route \emph{how much} or \emph{which model}; we route \emph{which modality} and find that death avoidance accounts for ${\sim}90\%$ of the routing signal.
181	18,21c13,14
182	< ITP \cite{itp-2026} augments agents with LLM-based world model lookahead;
183	< Dyna-Think \cite{dynathink-2025} integrates world model simulation into reasoning, matching 685B performance with 32B at half the token cost.
184	< Both route to \emph{approximate} world models inheriting LLM hallucinations.
185	< Our deterministic modality provides \emph{exact} state transitions; counterfactual analysis shows this exactness matters almost exclusively for death avoidance.
186	---
187	> ITP \cite{itp-2026} and Dyna-Think \cite{dynathink-2025} route to approximate LLM-based world models that inherit hallucination failures.
188	> Our deterministic modality provides exact state transitions, and our analysis reveals that this exactness matters almost exclusively for death avoidance.
189	24,26c17
190	< ReAct \cite{react-2023} interleaves reasoning and acting and serves as our internal-reasoning baseline.
191	< MTRouter \cite{mtrouter-2026} routes between LLMs for cost optimization on ScienceWorld.
192	< Our work asks what a learned router captures---the answer is dominated by catastrophic-failure prevention, suggesting safety-aware computation allocation over general reasoning enhancement.
193	---
194	> ReAct \cite{react-2023} interleaves reasoning and acting and serves as our internal-reasoning baseline. We analyze \emph{when} reasoning should yield to deterministic computation, finding the answer concentrated in catastrophic failure scenarios.
195	\ No newline at end of file
196	
197	=== conclusion.tex ===
198	3c3,7
199	< We presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Applied to 245 episodes across 11 ScienceWorld task types, death avoidance accounts for 90.41\% of the routing signal ($\Delta_{\text{full}}$ = +29.60 vs.\ $\Delta_{\text{nd}}$ = +2.84), corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.3\% agreement with always-deterministic), and near-random trained-router accuracy (58.1\%). Preliminary cross-environment evidence (\S\ref{sec:discussion}) suggests this finding reflects a structural property of catastrophic-failure environments rather than a ScienceWorld artifact.
200	---
201	> We introduce episode-level counterfactual analysis for understanding routing between LLM internal reasoning and deterministic computation, overcoming per-step oracle degeneracy (97.4\% tie rate) in sparse-reward settings. On 11 ScienceWorld task types (245 episodes), death avoidance accounts for 90.41\% of routing signal ($\Delta_{\text{full}} = +29.60 \rightarrow \Delta_{\text{nd}} = +2.84$; $r = 0.9698$, $p = 8.12 \times 10^{-7}$). The value of deterministic computation is predominantly concentrated in preventing catastrophic failures.
202	> 
203	> \paragraph{Labeling Quality.} Episode-level ties (61.2\% of pairs: 46.9\% both-alive, 14.3\% both-died) are excluded as \texttt{no\_preference} with no tie-breaking, so all 95 training labels reflect genuine outcome asymmetries (70 death-asymmetry det-preferred, 16 score-comparison det-preferred, 5 death-asymmetry internal-preferred, 4 score-comparison internal-preferred). A strict-only retrain excluding any potentially ambiguous labels yields balanced accuracy 0.5729, within $1\sigma$ of the full-label ablation (0.5761$\pm$0.005), confirming that oracle circularity does not inflate routing performance.
204	> 
205	> \paragraph{Limitations and Future Work.} Our analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct). ScienceWorld's $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure modes could exhibit lower DAF values. Our counterfactual labels operate at episode granularity, limiting router training resolution. Cross-seed instability in internal recall (51.5--81.8\%) warrants further investigation. Step-level labeling with denser rewards (e.g., DAgger-style \cite{dagger-2011} imitation learning) could improve both decomposition and router training. Extension to code-interpreter routing and multi-LLM evaluation would test generalization beyond simulator-based environments.
206	\ No newline at end of file
207	
208	=== main.tex ===
209	1a2
210	> 
211	2a4
212	> 
213	5,6c7,9
214	< \usepackage{amsmath}
215	< \usepackage{amssymb}
216	---
217	> \usepackage[T1]{fontenc}
218	> \usepackage[utf8]{inputenc}
219	> \usepackage{microtype}
220	8a12
221	> \usepackage{amsmath}
222	10c14
223	< \title{Death Avoidance Accounts for 90\% of the Routing Signal in LLM Agent Tool Use}
224	---
225	> \title{Death Avoidance Dominates Routing Signal\\in LLM Agent Computation}
226	12c16
227	< \author{Anonymous ACL submission}
228	---
229	> \author{Anonymous}
230	15a20
231	> 
232	21d25
233	< \input{discussion}
234	23,33d26
235	< 
236	< \section*{Limitations}
237	< 
238	< Our analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. Step-level labeling with denser rewards is a natural extension. The logit--generation gap in the implicit router warrants further investigation.
239	< 
240	< \paragraph{Labeling quality.}
241	< A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine modality differences. We audit all 245 labels. Of the 150 \texttt{no\_preference} labels (61.2\%), 115 (46.9\%) are both-alive ties and 35 (14.3\%) are both-dead---all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields balanced accuracy of 57.3\%, within 1$\sigma$ of the full-label retrain (57.6 $\pm$ 0.5\%), confirming that score-comparison labels contribute negligible additional signal. The 97.4\% step-level tie rate (\S\ref{sec:collection}) further motivates episode-level over step-level labeling.
242	< 
243	< \section*{Ethics Statement}
244	< 
245	< This work uses ScienceWorld \cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All language models are accessed via standard APIs or publicly released weights. We report computational costs: approximately 40 GPU-hours on two RTX 5090 GPUs for data collection, router training, and evaluation.
246	
247	=== references.bib ===
248	3,4c3,4
249	<   author={Wang, Ruoyao and Jansen, Peter and C{\^o}t{\'e}, Marc-Alexandre and Ammanabrolu, Prithviraj},
250	<   booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
251	---
252	>   author={Wang, Ruoyao and Jansen, Peter and C\^{o}t\'{e}, Marc-Alexandre and Ammanabrolu, Prithviraj},
253	>   booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
254	7a8,14
255	> @inproceedings{react-2023,
256	>   title={ReAct: Synergizing Reasoning and Acting in Language Models},
257	>   author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
258	>   booktitle={International Conference on Learning Representations (ICLR)},
259	>   year={2023}
260	> }
261	> 
262	10,11c17,18
263	<   author={Schick, Timo and Dwivedi-Yu, Jane and Dess{\`i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
264	<   booktitle={Advances in Neural Information Processing Systems},
265	---
266	>   author={Schick, Timo and Dwivedi-Yu, Jane and Dess\`{i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
267	>   booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
268	15,16c22,23
269	< @inproceedings{art-2023,
270	<   title={{ART}: Automatic Multi-step Reasoning and Tool-use for Large Language Models},
271	---
272	> @article{art-2023,
273	>   title={ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models},
274	18c25
275	<   booktitle={arXiv preprint arXiv:2303.09014},
276	---
277	>   journal={arXiv preprint arXiv:2303.09014},
278	25c32
279	<   booktitle={Advances in Neural Information Processing Systems},
280	---
281	>   booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
282	29,32c36,39
283	< @inproceedings{retool-2026,
284	<   title={{ReTool}: Reinforcement Learning for Strategic Tool Use in {LLM}s},
285	<   author={Feng, Yutong and Qian, Shengjie and Luo, Boyu and Shi, Yibo and Yang, Ke and Ma, Liang and Zheng, Ling},
286	<   booktitle={arXiv preprint arXiv:2504.11536},
287	---
288	> @article{retool-2026,
289	>   title={ReTool: Reinforcement Learning for Strategic Tool Use in LLMs},
290	>   author={Feng, Jiazhan and others},
291	>   journal={arXiv preprint arXiv:2504.11536},
292	36,46c43,46
293	< @inproceedings{react-2023,
294	<   title={{ReAct}: Synergizing Reasoning and Acting in Language Models},
295	<   author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
296	<   booktitle={International Conference on Learning Representations},
297	<   year={2023}
298	< }
299	< 
300	< @inproceedings{cogrouter-2026,
301	<   title={{CogRouter}: Cooperative Policy Optimization for Cognitive Depth Routing},
302	<   author={Yang, Ruihan and Li, Zheng and Wang, Yue and Chen, Wei},
303	<   booktitle={arXiv preprint arXiv:2503.16783},
304	---
305	> @article{cogrouter-2026,
306	>   title={Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents},
307	>   author={Yang, Ruihan and others},
308	>   journal={arXiv preprint arXiv:2602.12662},
309	50,53c50,53
310	< @inproceedings{ares-2026,
311	<   title={{ARES}: Adaptive Reasoning Effort Scaling for {LLM}s},
312	<   author={Yang, Jingbo and Zhao, Chen and Liu, Shuo and Wang, Zhiyu},
313	<   booktitle={arXiv preprint arXiv:2501.05661},
314	---
315	> @article{ares-2026,
316	>   title={ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents},
317	>   author={Yang, Jingbo and others},
318	>   journal={arXiv preprint arXiv:2603.07915},
319	58,60c58,60
320	<   title={Mixture of Recursions: Learnable and Efficient Adaptive Processing},
321	<   author={Bae, Sangmin and Hwang, Hyungwon and Kim, Jeonghwan and Yun, Se-Young},
322	<   booktitle={arXiv preprint arXiv:2501.05470},
323	---
324	>   title={Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation},
325	>   author={Bae, Sangmin and others},
326	>   booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
327	64,67c64,67
328	< @inproceedings{itp-2026,
329	<   title={{ITP}: Imagination-Augmented Task Planning with World Model Lookahead},
330	<   author={Liu, Youwei and Wang, Zeming and Zhang, Xin and Chen, Yang},
331	<   booktitle={arXiv preprint arXiv:2505.02605},
332	---
333	> @inproceedings{mtrouter-2026,
334	>   title={MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings},
335	>   author={Zhang, Yiqun and others},
336	>   booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL)},
337	71,75c71,75
338	< @inproceedings{dynathink-2025,
339	<   title={{Dyna-Think}: Integrating World Model Simulation into the Reasoning Loop},
340	<   author={Yu, Xiao and Liang, Yuxuan and Wang, Zhen and Sun, Lichao},
341	<   booktitle={arXiv preprint arXiv:2502.14458},
342	<   year={2025}
343	---
344	> @article{itp-2026,
345	>   title={Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models},
346	>   author={Liu, Youwei and others},
347	>   journal={arXiv preprint arXiv:2601.08955},
348	>   year={2026}
349	78,82c78,82
350	< @inproceedings{mtrouter-2026,
351	<   title={{MTRouter}: Multi-Model Routing for Cost-Efficient Interactive Agents},
352	<   author={Zhang, Yiqun and Liu, Yang and Xu, Hongming and Chen, Jian},
353	<   booktitle={arXiv preprint arXiv:2504.09750},
354	<   year={2026}
355	---
356	> @article{dynathink-2025,
357	>   title={Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents},
358	>   author={Yu, Xiao and others},
359	>   journal={arXiv preprint arXiv:2506.00320},
360	>   year={2025}
361	87c87
362	<   author={Ross, St{\'e}phane and Gordon, Geoffrey J and Bagnell, Drew},
363	---
364	>   author={Ross, St\'{e}phane and Gordon, Geoffrey J and Bagnell, Drew},
365	90c90
366	< }
367	---
368	> }
369	\ No newline at end of file
370	
371	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "20058bda-4b50-4893-ba4c-526aa29526ad",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/87e7d2fa-3544-463f-a483-079969decfa9/tool-results/b2rmqqghl.txt",
      "content": "=== abstract.tex ===\n2,3c2,3\n< Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability in rule-governed environments, yet understanding \\emph{what} drives effective routing remains unclear. Per-step oracle labeling degenerates in sparse-reward settings---in ScienceWorld, 97.4\\% of steps yield tied outcomes, rendering step-level analysis uninformative. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to derive per-episode routing labels. Across 245 episodes with a Qwen2.5-7B-Instruct backbone, death avoidance accounts for approximately 90\\% of the routing signal (Death Avoidance Factor), with near-perfect cross-task correlation ($r = 0.97$). These results indicate that deterministic computation's value is concentrated in catastrophic failure prevention rather than positive task guidance.\n< \\end{abstract}\n---\n> LLM agents in rule-governed interactive environments face catastrophic failures when internal reasoning hallucinates state transitions. Deterministic external computation (environment simulators, code interpreters) can prevent such failures, but what does routing between these modalities actually learn? Per-step oracle labeling degenerates under sparse rewards---on ScienceWorld, 97.4\\% of steps produce identical scores regardless of modality. We propose episode-level counterfactual analysis: running complete episodes under pure-internal and pure-deterministic strategies to generate routing labels from episode outcomes. Across 11 ScienceWorld task types (245 episodes), we find that death avoidance accounts for 90.41\\% of the routing signal between Qwen2.5-7B-Instruct internal reasoning and deterministic computation ($\\Delta_{\\text{full}} = +29.60$, $\\Delta_{\\text{nd}} = +2.84$; Pearson $r = 0.9698$, $p = 8.12 \\times 10^{-7}$ across task types). When neither strategy causes agent death, the performance gap is small but non-negligible ($\\Delta_{\\text{nd}} = +2.84$, 9.6\\% of the total gap). A trained router does not significantly outperform an unconditional always-deterministic strategy ($-10.70$ vs.\\ $-9.47$), confirming that the value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.\n> \\end{abstract}\n\\ No newline at end of file\n\n=== introduction.tex ===\n3c3\n< When a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \\cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?\n---\n> When a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \\cite{scienceworld-2022}, it must track temperature thresholds and container states across dozens of steps. Internal reasoning hallucinates these transitions---predicting water has boiled when the stove was never activated---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?\n5c5\n< Existing routing approaches \\cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \\emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\\% of steps produce tied intermediate scores under both strategies across 245 episodes---no step-level signal exists to train a router (\\S\\ref{sec:collection}).\n---\n> Existing routing approaches \\cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \\emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 97.4\\% of steps produce identical scores regardless of modality---no step-level signal exists to train a router (\\S\\ref{sec:collection}). Keyword-based heuristics (\\S\\ref{sec:rule}) also fail structurally: ScienceWorld actions use generic verbs (\\texttt{pour}, \\texttt{move}, \\texttt{activate}) rather than science-specific terminology, providing no lexical basis for routing decisions.\n7c7\n< We propose \\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\S\\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\\Delta_{\\text{full}} = +29.60$ points. Excluding death episodes, this gap collapses to $\\Delta_{\\text{nd}} = +2.84$---a Death Avoidance Factor (DAF; \\S\\ref{sec:daf}) of 90.41\\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), confirming death avoidance as the primary mechanism (\\S\\ref{sec:death-decomp}). Death rates differ sharply: 42.9\\% for internal reasoning versus 16.3\\% for deterministic computation. Of 245 episodes, 86 prefer deterministic, 9 prefer internal, and 150 show no preference---96.3\\% of oracle decisions match always-deterministic (\\S\\ref{sec:baselines}).\n---\n> We propose \\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\S\\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\\Delta_{\\text{full}} = +29.60$ points. Excluding episodes where either strategy causes agent death, this gap collapses to $\\Delta_{\\text{nd}} = +2.84$---a Death Avoidance Factor (DAF; \\S\\ref{sec:daf}) of 90.41\\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), confirming that death avoidance is the primary mechanism across task types (\\S\\ref{sec:death-decomp}). Death rates differ sharply (42.9\\% internal vs.\\ 16.3\\% deterministic), and 96.3\\% of oracle routing decisions match always-deterministic (\\S\\ref{sec:baselines}).\n9,13c9\n< Our contributions:\n< \\begin{enumerate}\n< \\item \\textbf{Episode-level counterfactual methodology.} We introduce episode-level counterfactual analysis with death-aware labeling and the DAF decomposition metric, overcoming per-step oracle degeneracy in sparse-reward environments (\\S\\ref{sec:collection}, \\S\\ref{sec:daf}).\n< \\item \\textbf{Death avoidance dominates routing signal.} Across 11 task types (245 episodes), death avoidance accounts for 90.41\\% of the routing signal ($\\Delta_{\\text{nd}} = +2.84$, 9.6\\% of $\\Delta_{\\text{full}}$). Router training as a diagnostic probe confirms learnable routing structure at the representation level (\\S\\ref{sec:router-diagnostic}).\n< \\end{enumerate}\n---\n> Our contributions: (1) an \\emph{episode-level counterfactual methodology} with death avoidance decomposition via the DAF metric (\\S\\ref{sec:collection}--\\ref{sec:daf}), overcoming per-step oracle degeneracy in sparse-reward environments; and (2) the empirical finding that \\emph{death avoidance accounts for 90.41\\% of routing signal} on ScienceWorld, with a trained router failing to outperform always-deterministic (\\S\\ref{sec:death-decomp}--\\ref{sec:router-diagnostic}).\n\\ No newline at end of file\n\n=== method.tex ===\n6c6\n< Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each modality. Under sparse terminal rewards, this degenerates: on ScienceWorld \\cite{scienceworld-2022}, 97.4\\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\n---\n> Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \\cite{scienceworld-2022}, 97.4\\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\n8c8\n< For each task instance, we execute two complete episodes under identical initial conditions. The \\emph{pure-internal} episode follows the ReAct paradigm \\cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \\emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction---equivalent to giving the agent a perfect world model.\n---\n> For each task instance, we execute two complete episodes under identical initial conditions (same random seed, same task variation). The \\emph{pure-internal} episode follows the ReAct paradigm \\cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \\emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions for each action. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction, not action selection---equivalent to giving the agent access to a perfect world model.\n10c10\n< Each episode pair produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes the terminal score and $d \\in \\{0,1\\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. ScienceWorld spans 30 task types with a $-100$ death penalty; after prescreening, we collect 245 episode pairs across 11 task types (20--40 per type).\n---\n> Each episode pair produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes the terminal score and $d \\in \\{0,1\\}$ indicates agent death. We use Qwen2.5-7B-Instruct (vLLM) on ScienceWorld \\cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty, with episodes capped at 30 steps. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type).\n15c15\n< Each counterfactual pair receives an episode-level routing label based on $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$. Scores are integer-valued, so we use exact (in)equality. The label is assigned by four mutually exclusive cases:\n---\n> Each counterfactual pair receives an episode-level routing label based on $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The label is assigned by one of four mutually exclusive cases:\n18c18\n<     \\item \\textbf{Death asymmetry}: $d^{\\text{int}} \\neq d^{\\text{det}}$ $\\rightarrow$ surviving strategy preferred.\n---\n>     \\item \\textbf{Death asymmetry}: $d^{\\text{int}} \\neq d^{\\text{det}}$ $\\rightarrow$ the surviving strategy is preferred.\n20,21c20,21\n<     \\item \\textbf{Score gap}: both survive, $s^{\\text{det}} \\neq s^{\\text{int}}$ $\\rightarrow$ higher-scoring strategy preferred.\n<     \\item \\textbf{Tied alive}: both survive, $s^{\\text{det}} = s^{\\text{int}}$ $\\rightarrow$ \\texttt{no\\_preference}.\n---\n>     \\item \\textbf{Score comparison}: both survive and $s^{\\text{det}} \\neq s^{\\text{int}}$ $\\rightarrow$ the higher-scoring strategy is preferred.\n>     \\item \\textbf{Tied alive}: both survive and $s^{\\text{det}} = s^{\\text{int}}$ $\\rightarrow$ \\texttt{no\\_preference}.\n23a24,25\n> Label distributions are reported in \\S\\ref{sec:death-decomp}.\n> \n31c33,40\n< where $\\Delta_{\\text{full}}$ is the mean score gap ($s^{\\text{det}} - s^{\\text{int}}$) across all episodes and $\\Delta_{\\text{nd}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all signal stems from death avoidance; DAF $= 0$ indicates none does. We report results in \\S\\ref{sec:death-decomp}.\n---\n> where $\\Delta_{\\text{full}}$ is the mean score gap ($s^{\\text{det}} - s^{\\text{int}}$) across all episodes and $\\Delta_{\\text{nd}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all routing signal stems from death avoidance; DAF $= 0$ indicates all signal stems from non-death performance differences. When $\\Delta_{\\text{full}} = 0$, DAF is undefined, as no routing signal exists to decompose; we report DAF only for task types where $|\\Delta_{\\text{full}}| > 0$.\n> \n> Results using DAF are reported in \\S\\ref{sec:death-decomp}.\n> \n> \\subsection{Rule-Based Baseline}\n> \\label{sec:rule}\n> \n> We test keyword-based routing that selects deterministic computation when the action contains science-related verbs. Three keyword lists of decreasing breadth produce match rates of 85.8\\% (v1, degenerating to always-deterministic), 4.9\\% (v2), and 2.8\\% (v3, both degenerating to always-internal). ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}) rather than science-specific terms; no keyword granularity bridges the gap between near-total and negligible match rates.\n\\ No newline at end of file\n\n=== experiments.tex ===\n3,7d2\n< \\subsection{Setup}\n< \\label{sec:exp-setup}\n< \n< We evaluate on ScienceWorld \\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ death penalty. Using the methodology in \\S\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 per type). The LLM backbone is Qwen2.5-7B-Instruct served via vLLM with episodes capped at 30 steps.\n< \n13,14c8,9\n< \\includegraphics[width=\\columnwidth]{fig1_daf_scatter.pdf}\n< \\caption{Per-task death rate differential (internal minus deterministic) vs.\\ $\\Delta_{\\text{full}}$. Each point represents one of 11 task types. Regression: $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$).}\n---\n> \\includegraphics[width=\\columnwidth]{figures/fig1_daf_scatter.pdf}\n> \\caption{Per-task scatter plot: death rate differential (internal minus deterministic) vs.\\ performance gap ($\\Delta_{\\text{full}}$). Pearson $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$). Each point is one of 11 ScienceWorld task types.}\n18c13\n< The full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. Excluding all episodes where either strategy results in death, the gap collapses to $\\Delta_{\\text{nd}} = +2.84$. The resulting DAF (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage is attributable to death avoidance.\n---\n> The full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\\Delta_{\\text{nd}} = +2.84$. The resulting Death Avoidance Factor (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.\n20c15\n< This concentration is consistent across task types. The Pearson correlation between per-task death rate differential and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$; Figure~\\ref{fig:decomposition}). The internal strategy dies in 42.9\\% of episodes versus 16.3\\% for deterministic---a 2.6$\\times$ ratio driving the bulk of the score difference.\n---\n> This concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), as shown in Figure~\\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\\% of episodes compared to 16.3\\% for deterministic computation---a 2.6$\\times$ ratio that drives the bulk of the observed score difference.\n22c17\n< The label distribution reflects this asymmetry: 86 \\texttt{det\\_preferred}, 9 \\texttt{internal\\_preferred}, 150 \\texttt{no\\_preference}. When internal reasoning does not cause death, it performs comparably to deterministic computation.\n---\n> The episode-level label distribution reflects this asymmetry: of 245 episodes, 86 are \\texttt{det\\_preferred}, only 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}---when internal reasoning does not cause death, it performs comparably to deterministic computation.\n24c19\n< One task reveals residual non-death signal: \\texttt{find-non-living-thing} ($n=40$) has zero deaths yet $\\Delta_{\\text{full}} = +9.58$, entirely from non-death differences. Among the 10 death-prone task types, however, death avoidance overwhelms non-death signal.\n---\n> One task reveals the residual non-death signal. \\texttt{find-non-living-thing} ($n=40$) has zero deaths under both strategies yet shows $\\Delta_{\\text{full}} = +9.58$, entirely from non-death performance differences---deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, among the 10 death-prone task types, death avoidance overwhelms non-death differences. When both modalities survive, the gap is small but non-negligible ($\\Delta_{\\text{nd}} = +2.84$, 9.6\\% of $\\Delta_{\\text{full}}$).\n34c29\n< Strategy & Score & 95\\% CI & Death \\% \\\\\n---\n> Strategy & Score & 90\\% CI & Death \\% \\\\\n36,39c31,34\n< Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\\\\n< Always-Det. & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\\\\n< Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\\\\n< Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\\\\n---\n> Always-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\\\\n> Always-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\\\\n> Random & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\\\\n> Oracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\\\\n41c36\n< Trained Router & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\\\\n---\n> Trained Router & $-10.70$ & [$-15.25$, $-6.38$] & 17.6 \\\\\n44c39\n< \\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). 95\\% Bootstrap CIs. The oracle selects the higher-scoring strategy per episode; 96.3\\% of its decisions match always-deterministic.}\n---\n> \\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). 90\\% confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.3\\% of its decisions match the always-deterministic strategy.}\n48,50c43\n< Table~\\ref{tab:baselines} reports episode-weighted mean scores and death rates. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle improves only modestly to $-6.58$, with 96.3\\% of its decisions matching always-deterministic---\\emph{oracle degeneracy} indicating the optimal routing policy closely resembles unconditional deterministic computation. Random routing ($-22.38$) falls between the two pure strategies.\n< \n< Keyword-based routing fails structurally: ScienceWorld actions use generic verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing match rates to cluster at extremes---near-total (85.8\\%, degenerating to always-deterministic) or negligible ($<$5\\%, degenerating to always-internal).\n---\n> Table~\\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.3\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.\n52c45\n< The trained router (\\S\\ref{sec:router-diagnostic}) scores $-10.70$, 1.23 points below always-deterministic, with comparable death rate (17.6\\% vs.\\ 16.3\\%).\n---\n> Keyword-based routing (\\S\\ref{sec:rule}) fails structurally: match rates cluster at extremes (85.8\\% or $<$5\\%), precluding meaningful routing discrimination.\n57c50,56\n< We investigate whether episode-level counterfactual labels can train a step-level router, as a diagnostic probe rather than a routing system proposal.\n---\n> A natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.\n> \n> \\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.\n> \n> \\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. Gradient accumulation is critical: with gradient accumulation of 1, the model fails to achieve meaningful routing discrimination (internal recall 26.7\\%); with gradient accumulation of 8, the model becomes non-degenerate (internal recall above 50\\% across all seeds). We report results for the non-degenerate configuration (gradient accumulation 8). At both the logit and generation levels, accuracy is 65.4\\%, balanced accuracy 59.3\\%, and internal recall 51.5\\%---no logit-generation gap exists for this configuration, demonstrating a weak but above-chance routing signal beyond what a degenerate always-deterministic predictor captures.\n> \n> \\paragraph{Cross-seed stability.} Balanced accuracy is stable across seeds (57--59\\%), but internal recall varies from 51.5\\% to 81.8\\%---the signal exists but is insufficient for practical routing, consistent with the death avoidance decomposition: when ${\\sim}90\\%$ of routing value is death avoidance, the learnable non-death signal is structurally thin.\n59c58\n< \\paragraph{Classification head.} A linear head appended to the LLM's hidden representations degenerates to always-deterministic (0\\% internal recall) across all configurations (class weighting, focal loss, undersampling, temperature scaling).\n---\n> \\paragraph{End-to-end evaluation.} Deployed as an episode-level router (Table~\\ref{tab:baselines}), the trained router scores $-10.70$ (90\\% CI $[-15.25, -6.38]$) with 17.6\\% death rate, allocating 97.0\\% of episodes to deterministic computation. It did not significantly outperform always-deterministic ($-9.47$, $[-13.66, -5.11]$)---CIs overlap substantially. The few internally-routed episodes include cases where the agent dies, and misrouting cost exceeds the benefit of correctly routing rare internal-preferred episodes. This is a direct corollary of death avoidance dominance: any router that occasionally routes internally risks catastrophic failure, while always-deterministic avoids this risk entirely.\n61c60\n< \\paragraph{Implicit router.} We fine-tune Qwen3-1.7B to internalize routing decisions. Training configuration significantly affects results. With gradient accumulation GA=8 (effective batch size 32), the model achieves generation accuracy of 65.4\\% with internal recall of 51.5\\%---the only non-degenerate configuration. With GA=1 (effective batch size 4), logit-level accuracy reaches 74.5\\% (balanced accuracy 79\\%), but generation degenerates to 53.3\\% accuracy with only 26.7\\% internal recall---a 21.2 percentage point logit--generation gap. Effective batch size determines whether learned patterns transfer to generation.\n---\n> Three observations follow. First, logit-level success rules out uninformative labels, pointing to the episode-to-step granularity mismatch as the classification head bottleneck. Second, in death-dominated environments, always-deterministic is near-optimal and any learned router must overcome asymmetric misrouting cost (death vs.\\ marginal score improvement). Third, when DAF $\\approx 90\\%$, router headroom is structurally limited to the ${\\sim}10\\%$ non-death signal.\n63c62\n< Across four seeds (GA=8), balanced accuracy is $58.1 \\pm 0.8\\%$---8 points above chance. Internal recall varies from 51.5\\% to 81.8\\%, indicating seed-dependent boundaries with consistent weak discriminability. End-to-end (Table~\\ref{tab:baselines}): the router's 97.0\\% simulator invocation ratio means it routes internally only 3\\% of the time---weak signal with unstable thresholds, consistent with minimal routing structure beyond death avoidance.\n---\n> \\paragraph{Labeling quality.} We verify that the episode-level counterfactual labels are free of oracle circularity. Of 245 episodes, 0\\% of oracle routing decisions are determined by tie-breaking rules---all are based on genuine score differences. The remaining 61.2\\% of episodes are ties (46.9\\% both-alive, 14.3\\% both-died) and are excluded from training. Retraining the implicit router on strict-only (non-tie) labels yields balanced accuracy of 0.5729, consistent with the full-label result (0.5761 $\\pm$ 0.005), confirming that the labeling methodology introduces no circular signal.\n\\ No newline at end of file\n\n=== related_work.tex ===\n4,9c4,5\n< Toolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering;\n< ART \\cite{art-2023} delegates tool selection to LLM reasoning chains;\n< Chameleon \\cite{chameleon-2024} composes modules under LLM-as-planner orchestration;\n< ReTool \\cite{retool-2026} applies RL for implicit code-interpreter invocation.\n< These methods learn \\emph{which tool} to use but do not analyze what signal drives routing.\n< We generate labels via \\emph{episode-level counterfactual analysis} and diagnose what the signal encodes---revealing ${\\sim}90\\%$ is death avoidance.\n---\n> Toolformer \\cite{toolformer-2024} inserts API calls via self-supervised filtering; ART \\cite{art-2023} and Chameleon \\cite{chameleon-2024} compose tools under LLM orchestration; ReTool \\cite{retool-2026} applies RL for code-interpreter invocation.\n> We differ by generating routing labels via \\emph{episode-level counterfactual analysis}, framing routing as \\emph{catastrophic failure prevention}, and training an explicit lightweight router for diagnostic analysis.\n12,15c8,10\n< CogRouter \\cite{cogrouter-2026} achieves 82.3\\% on ScienceWorld (success rate, different evaluation protocol) via cognitive depth routing.\n< ARES \\cite{ares-2026} reduces token cost by 52.7\\% with per-step reasoning effort selection.\n< Mixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth via per-token recursive routing.\n< These route \\emph{how much} to reason; we route \\emph{which modality}. None quantify routing signal composition.\n---\n> CogRouter \\cite{cogrouter-2026} routes among cognitive depth levels on ScienceWorld; ARES \\cite{ares-2026} selects per-step reasoning effort; Mixture-of-Recursions \\cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level.\n> MTRouter \\cite{mtrouter-2026} routes among LLMs to optimize cost-quality tradeoffs.\n> These methods route \\emph{how much} or \\emph{which model}; we route \\emph{which modality} and find that death avoidance accounts for ${\\sim}90\\%$ of the routing signal.\n18,21c13,14\n< ITP \\cite{itp-2026} augments agents with LLM-based world model lookahead;\n< Dyna-Think \\cite{dynathink-2025} integrates world model simulation into reasoning, matching 685B performance with 32B at half the token cost.\n< Both route to \\emph{approximate} world models inheriting LLM hallucinations.\n< Our deterministic modality provides \\emph{exact} state transitions; counterfactual analysis shows this exactness matters almost exclusively for death avoidance.\n---\n> ITP \\cite{itp-2026} and Dyna-Think \\cite{dynathink-2025} route to approximate LLM-based world models that inherit hallucination failures.\n> Our deterministic modality provides exact state transitions, and our analysis reveals that this exactness matters almost exclusively for death avoidance.\n24,26c17\n< ReAct \\cite{react-2023} interleaves reasoning and acting and serves as our internal-reasoning baseline.\n< MTRouter \\cite{mtrouter-2026} routes between LLMs for cost optimization on ScienceWorld.\n< Our work asks what a learned router captures---the answer is dominated by catastrophic-failure prevention, suggesting safety-aware computation allocation over general reasoning enhancement.\n---\n> ReAct \\cite{react-2023} interleaves reasoning and acting and serves as our internal-reasoning baseline. We analyze \\emph{when} reasoning should yield to deterministic computation, finding the answer concentrated in catastrophic failure scenarios.\n\\ No newline at end of file\n\n=== conclusion.tex ===\n3c3,7\n< We presented episode-level counterfactual analysis for diagnosing routing behavior in modular LLM agents. Applied to 245 episodes across 11 ScienceWorld task types, death avoidance accounts for 90.41\\% of the routing signal ($\\Delta_{\\text{full}}$ = +29.60 vs.\\ $\\Delta_{\\text{nd}}$ = +2.84), corroborated by near-perfect cross-task correlation ($r$ = 0.9698), oracle degeneracy (96.3\\% agreement with always-deterministic), and near-random trained-router accuracy (58.1\\%). Preliminary cross-environment evidence (\\S\\ref{sec:discussion}) suggests this finding reflects a structural property of catastrophic-failure environments rather than a ScienceWorld artifact.\n---\n> We introduce episode-level counterfactual analysis for understanding routing between LLM internal reasoning and deterministic computation, overcoming per-step oracle degeneracy (97.4\\% tie rate) in sparse-reward settings. On 11 ScienceWorld task types (245 episodes), death avoidance accounts for 90.41\\% of routing signal ($\\Delta_{\\text{full}} = +29.60 \\rightarrow \\Delta_{\\text{nd}} = +2.84$; $r = 0.9698$, $p = 8.12 \\times 10^{-7}$). The value of deterministic computation is predominantly concentrated in preventing catastrophic failures.\n> \n> \\paragraph{Labeling Quality.} Episode-level ties (61.2\\% of pairs: 46.9\\% both-alive, 14.3\\% both-died) are excluded as \\texttt{no\\_preference} with no tie-breaking, so all 95 training labels reflect genuine outcome asymmetries (70 death-asymmetry det-preferred, 16 score-comparison det-preferred, 5 death-asymmetry internal-preferred, 4 score-comparison internal-preferred). A strict-only retrain excluding any potentially ambiguous labels yields balanced accuracy 0.5729, within $1\\sigma$ of the full-label ablation (0.5761$\\pm$0.005), confirming that oracle circularity does not inflate routing performance.\n> \n> \\paragraph{Limitations and Future Work.} Our analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct). ScienceWorld's $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure modes could exhibit lower DAF values. Our counterfactual labels operate at episode granularity, limiting router training resolution. Cross-seed instability in internal recall (51.5--81.8\\%) warrants further investigation. Step-level labeling with denser rewards (e.g., DAgger-style \\cite{dagger-2011} imitation learning) could improve both decomposition and router training. Extension to code-interpreter routing and multi-LLM evaluation would test generalization beyond simulator-based environments.\n\\ No newline at end of file\n\n=== main.tex ===\n1a2\n> \n2a4\n> \n5,6c7,9\n< \\usepackage{amsmath}\n< \\usepackage{amssymb}\n---\n> \\usepackage[T1]{fontenc}\n> \\usepackage[utf8]{inputenc}\n> \\usepackage{microtype}\n8a12\n> \\usepackage{amsmath}\n10c14\n< \\title{Death Avoidance Accounts for 90\\% of the Routing Signal in LLM Agent Tool Use}\n---\n> \\title{Death Avoidance Dominates Routing Signal\\\\in LLM Agent Computation}\n12c16\n< \\author{Anonymous ACL submission}\n---\n> \\author{Anonymous}\n15a20\n> \n21d25\n< \\input{discussion}\n23,33d26\n< \n< \\section*{Limitations}\n< \n< Our analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. Step-level labeling with denser rewards is a natural extension. The logit--generation gap in the implicit router warrants further investigation.\n< \n< \\paragraph{Labeling quality.}\n< A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine modality differences. We audit all 245 labels. Of the 150 \\texttt{no\\_preference} labels (61.2\\%), 115 (46.9\\%) are both-alive ties and 35 (14.3\\%) are both-dead---all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields balanced accuracy of 57.3\\%, within 1$\\sigma$ of the full-label retrain (57.6 $\\pm$ 0.5\\%), confirming that score-comparison labels contribute negligible additional signal. The 97.4\\% step-level tie rate (\\S\\ref{sec:collection}) further motivates episode-level over step-level labeling.\n< \n< \\section*{Ethics Statement}\n< \n< This work uses ScienceWorld \\cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All language models are accessed via standard APIs or publicly released weights. We report computational costs: approximately 40 GPU-hours on two RTX 5090 GPUs for data collection, router training, and evaluation.\n\n=== references.bib ===\n3,4c3,4\n<   author={Wang, Ruoyao and Jansen, Peter and C{\\^o}t{\\'e}, Marc-Alexandre and Ammanabrolu, Prithviraj},\n<   booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n---\n>   author={Wang, Ruoyao and Jansen, Peter and C\\^{o}t\\'{e}, Marc-Alexandre and Ammanabrolu, Prithviraj},\n>   booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n7a8,14\n> @inproceedings{react-2023,\n>   title={ReAct: Synergizing Reasoning and Acting in Language Models},\n>   author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},\n>   booktitle={International Conference on Learning Representations (ICLR)},\n>   year={2023}\n> }\n> \n10,11c17,18\n<   author={Schick, Timo and Dwivedi-Yu, Jane and Dess{\\`i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},\n<   booktitle={Advances in Neural Information Processing Systems},\n---\n>   author={Schick, Timo and Dwivedi-Yu, Jane and Dess\\`{i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},\n>   booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n15,16c22,23\n< @inproceedings{art-2023,\n<   title={{ART}: Automatic Multi-step Reasoning and Tool-use for Large Language Models},\n---\n> @article{art-2023,\n>   title={ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models},\n18c25\n<   booktitle={arXiv preprint arXiv:2303.09014},\n---\n>   journal={arXiv preprint arXiv:2303.09014},\n25c32\n<   booktitle={Advances in Neural Information Processing Systems},\n---\n>   booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n29,32c36,39\n< @inproceedings{retool-2026,\n<   title={{ReTool}: Reinforcement Learning for Strategic Tool Use in {LLM}s},\n<   author={Feng, Yutong and Qian, Shengjie and Luo, Boyu and Shi, Yibo and Yang, Ke and Ma, Liang and Zheng, Ling},\n<   booktitle={arXiv preprint arXiv:2504.11536},\n---\n> @article{retool-2026,\n>   title={ReTool: Reinforcement Learning for Strategic Tool Use in LLMs},\n>   author={Feng, Jiazhan and others},\n>   journal={arXiv preprint arXiv:2504.11536},\n36,46c43,46\n< @inproceedings{react-2023,\n<   title={{ReAct}: Synergizing Reasoning and Acting in Language Models},\n<   author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},\n<   booktitle={International Conference on Learning Representations},\n<   year={2023}\n< }\n< \n< @inproceedings{cogrouter-2026,\n<   title={{CogRouter}: Cooperative Policy Optimization for Cognitive Depth Routing},\n<   author={Yang, Ruihan and Li, Zheng and Wang, Yue and Chen, Wei},\n<   booktitle={arXiv preprint arXiv:2503.16783},\n---\n> @article{cogrouter-2026,\n>   title={Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents},\n>   author={Yang, Ruihan and others},\n>   journal={arXiv preprint arXiv:2602.12662},\n50,53c50,53\n< @inproceedings{ares-2026,\n<   title={{ARES}: Adaptive Reasoning Effort Scaling for {LLM}s},\n<   author={Yang, Jingbo and Zhao, Chen and Liu, Shuo and Wang, Zhiyu},\n<   booktitle={arXiv preprint arXiv:2501.05661},\n---\n> @article{ares-2026,\n>   title={ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents},\n>   author={Yang, Jingbo and others},\n>   journal={arXiv preprint arXiv:2603.07915},\n58,60c58,60\n<   title={Mixture of Recursions: Learnable and Efficient Adaptive Processing},\n<   author={Bae, Sangmin and Hwang, Hyungwon and Kim, Jeonghwan and Yun, Se-Young},\n<   booktitle={arXiv preprint arXiv:2501.05470},\n---\n>   title={Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation},\n>   author={Bae, Sangmin and others},\n>   booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n64,67c64,67\n< @inproceedings{itp-2026,\n<   title={{ITP}: Imagination-Augmented Task Planning with World Model Lookahead},\n<   author={Liu, Youwei and Wang, Zeming and Zhang, Xin and Chen, Yang},\n<   booktitle={arXiv preprint arXiv:2505.02605},\n---\n> @inproceedings{mtrouter-2026,\n>   title={MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings},\n>   author={Zhang, Yiqun and others},\n>   booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL)},\n71,75c71,75\n< @inproceedings{dynathink-2025,\n<   title={{Dyna-Think}: Integrating World Model Simulation into the Reasoning Loop},\n<   author={Yu, Xiao and Liang, Yuxuan and Wang, Zhen and Sun, Lichao},\n<   booktitle={arXiv preprint arXiv:2502.14458},\n<   year={2025}\n---\n> @article{itp-2026,\n>   title={Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models},\n>   author={Liu, Youwei and others},\n>   journal={arXiv preprint arXiv:2601.08955},\n>   year={2026}\n78,82c78,82\n< @inproceedings{mtrouter-2026,\n<   title={{MTRouter}: Multi-Model Routing for Cost-Efficient Interactive Agents},\n<   author={Zhang, Yiqun and Liu, Yang and Xu, Hongming and Chen, Jian},\n<   booktitle={arXiv preprint arXiv:2504.09750},\n<   year={2026}\n---\n> @article{dynathink-2025,\n>   title={Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents},\n>   author={Yu, Xiao and others},\n>   journal={arXiv preprint arXiv:2506.00320},\n>   year={2025}\n87c87\n<   author={Ross, St{\\'e}phane and Gordon, Geoffrey J and Bagnell, Drew},\n---\n>   author={Ross, St\\'{e}phane and Gordon, Geoffrey J and Bagnell, Drew},\n90c90\n< }\n---\n> }\n\\ No newline at end of file\n\n",
      "numLines": 371,
      "startLine": 1,
      "totalLines": 371
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed to:

1. Complete the citation audit
2. Sync the files

Let me compile the citation audit first:

**Bib keys in artifacts/_project/paper/latex/references.bib:**
1. scienceworld-2022
2. toolformer-2024
3. art-2023
4. chameleon-2024
5. retool-2026
6. react-2023
7. cogrouter-2026
8. ares-2026
9. mixture-of-recursions-2025
10. itp-2026


11. dynathink-2025
12. mtrouter-2026
13. dagger-2011

Now I'm checking which of these are actually cited across the .tex files to identify any unused references.

Looking at the conclusion section, I see dagger-2011 appears in the docs version with a DAgger-style citation, but when I check the artifacts version of the same file, that reference isn't there. Let me verify whether dagger-2011 is cited anywhere in the actual artifacts latex files—from my earlier grep results, it doesn't appear to be cited in any of them, so it's in the bibliography but unused. I'm noticing the references.bib file has quality differences too—the docs version correctly uses @article for arXiv papers while the artifacts master incorrectly uses @inproceedings with booktitle. Since the sync goes from artifacts to docs, the master's inferior bibliography format will overwrite the docs version, and dagger-2011 will end up uncited across all files. Audit Summary (based on artifacts/_project/paper/latex/ — the master):

❌ Cited but missing from bib: NONE

⚠️ In bib but uncited: `dagger-2011`

Quality issues in artifacts/latex/references.bib:
1. Key-year mismatches:
   - `toolformer-2024`: year=2023 (NeurIPS 2023)
   - `chameleon-2024`: year=2023 (NeurIPS 2023)
   - `retool-2026`: year=2025
2. arXiv entries use @inproceedings with `booktitle` instead of @article with `journal`:
   - art-2023, retool-2026, cogrouter-2026, ares-2026, mixture-of-recursions-2025, itp-2026, dynathink-2025, mtrouter-2026

The docs version has already corrected many of these issues—using @article for arXiv papers and adding venue abbreviations—so I need to be careful that syncing from artifacts doesn't undo those improvements. I'm planning to copy over the newer content files and the bibliography from artifacts, but this means I'll need to manually reapply the reference formatting fixes to avoid regression. I see the issue now—the artifacts version is actually the older, less polished one, while docs contains more recent improvements like expanded experiments, a rule-based baseline section, and better organization. Since the user explicitly wants artifacts as the source of truth, I need to flag this as a significant regression before proceeding with the sync. I'm realizing that overwriting newer work with older versions is a significant risk I should flag before executing any destructive operations. Let me report the audit findings and highlight this concern to the user before proceeding with the sync.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "aea8d4ae-08bd-4d36-b33d-f5967264aef3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xZCxGCvom94Fk1UZcxtvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13045,
      "cache_read_input_tokens": 31600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13045
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

_source line 31_

分析完成。在执行同步前，需要先报告一个重要发现。

---

## 1. 引用审计报告

### 引用完整性

| 检查项 | 结果 |
|--------|------|
| ❌ 论文中 cite 了但 bib 中不存在的 | **无** — 所有 12 个被引用的 key 均存在于 bib 中 |
| ⚠️ bib 中存在但论文中未 cite 的 | **`dagger-2011`** (Ross et al., 2011, DAgger) |

被引用的 12 个 key: `scienceworld-2022`, `toolformer-2024`, `art-2023`, `chameleon-2024`, `retool-2026`, `react-2023`, `cogrouter-2026`, `ares-2026`, `mixture-of-recursions-2025`, `itp-2026`, `dynathink-2025`, `mtrouter-2026`

### Bib entry 质量问题

**Key 与 year 字段不匹配（3 个）：**
| Key | key 中的年份 | year 字段 |
|-----|------------|-----------|
| `toolformer-2024` | 2024 | 2023 |
| `chameleon-2024` | 2024 | 2023 |
| `retool-2026` | 2026 | 2025 |

**Entry type 错误（8 个）：** 以下 arXiv 预印本使用了 `@inproceedings` + `booktitle`，应改为 `@article` + `journal`：
`art-2023`, `retool-2026`, `cogrouter-2026`, `ares-2026`, `mixture-of-recursions-2025`, `itp-2026`, `dynathink-2025`, `mtrouter-2026`

**缺失字段：** 无。所有 entry 均有 title, author, year。

---

## 2. 同步：重要警告

**逐文件 diff 显示 `docs/paper/` 很可能是更新的版本，`artifacts/_project/paper/latex/` 是旧版本。** 具体证据：

| 文件 | artifacts (主) | docs (副) | 差异 |
|------|---------------|-----------|------|
| `abstract.tex` | 更短，约 3 行 | 更详细，含具体数值 | docs 更完整 |
| `introduction.tex` | 枚举式 contributions | 压缩为 1 段 + 引用 §rule | docs 增加了 keyword baseline 引用 |
| `method.tex` | 3 小节 | 4 小节（多了 Rule-Based Baseline §rule） | docs 新增内容 |
| `experiments.tex` | 有独立 Setup 小节；router 分析简略 | Setup 移走；增加 classification head / implicit router / cross-seed / end-to-end / labeling quality 段落 | docs 大幅扩充 |
| `conclusion.tex` | 1 段 | 3 段（含 labeling quality + limitations） | docs 大幅扩充 |
| `main.tex` | 含 `\input{discussion}` + Limitations + Ethics 节 | 不含 discussion；限制移入 conclusion | 结构不同 |
| `related_work.tex` | 分段引用，较松散 | 合并压缩，更紧凑 | docs 更精炼 |
| `references.bib` | @inproceedings 用于 arXiv | 已修正为 @article + venue 缩写 | docs 质量更高 |
| `discussion.tex` | 存在 | **缺失** | 需要复制 |

**如果按原计划用 artifacts 覆盖 docs，会丢失 docs 中的大量改进（实验分析扩充、bib 修正、结构重组等）。**

### 建议

反向同步更合理：以 `docs/paper/` 为准更新 `artifacts/_project/paper/latex/`，并将 `discussion.tex` 复制到 docs。

是否按原计划执行（artifacts → docs 覆盖），还是反向同步（docs → artifacts + 补 discussion.tex）？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "uuid": "fd9e450d-b211-4e31-b286-03a4ecbc352e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011xZCxGCvom94Fk1UZcxtvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13045,
      "cache_read_input_tokens": 31600,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13045
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

_source line 32_

分析完成。在执行同步前，需要先报告一个重要发现。

---

## 1. 引用审计报告

### 引用完整性

| 检查项 | 结果 |
|--------|------|
| ❌ 论文中 cite 了但 bib 中不存在的 | **无** — 所有 12 个被引用的 key 均存在于 bib 中 |
| ⚠️ bib 中存在但论文中未 cite 的 | **`dagger-2011`** (Ross et al., 2011, DAgger) |

被引用的 12 个 key: `scienceworld-2022`, `toolformer-2024`, `art-2023`, `chameleon-2024`, `retool-2026`, `react-2023`, `cogrouter-2026`, `ares-2026`, `mixture-of-recursions-2025`, `itp-2026`, `dynathink-2025`, `mtrouter-2026`

### Bib entry 质量问题

**Key 与 year 字段不匹配（3 个）：**
| Key | key 中的年份 | year 字段 |
|-----|------------|-----------|
| `toolformer-2024` | 2024 | 2023 |
| `chameleon-2024` | 2024 | 2023 |
| `retool-2026` | 2026 | 2025 |

**Entry type 错误（8 个）：** 以下 arXiv 预印本使用了 `@inproceedings` + `booktitle`，应改为 `@article` + `journal`：
`art-2023`, `retool-2026`, `cogrouter-2026`, `ares-2026`, `mixture-of-recursions-2025`, `itp-2026`, `dynathink-2025`, `mtrouter-2026`

**缺失字段：** 无。所有 entry 均有 title, author, year。

---

## 2. 同步：重要警告

**逐文件 diff 显示 `docs/paper/` 很可能是更新的版本，`artifacts/_project/paper/latex/` 是旧版本。** 具体证据：

| 文件 | artifacts (主) | docs (副) | 差异 |
|------|---------------|-----------|------|
| `abstract.tex` | 更短，约 3 行 | 更详细，含具体数值 | docs 更完整 |
| `introduction.tex` | 枚举式 contributions | 压缩为 1 段 + 引用 §rule | docs 增加了 keyword baseline 引用 |
| `method.tex` | 3 小节 | 4 小节（多了 Rule-Based Baseline §rule） | docs 新增内容 |
| `experiments.tex` | 有独立 Setup 小节；router 分析简略 | Setup 移走；增加 classification head / implicit router / cross-seed / end-to-end / labeling quality 段落 | docs 大幅扩充 |
| `conclusion.tex` | 1 段 | 3 段（含 labeling quality + limitations） | docs 大幅扩充 |
| `main.tex` | 含 `\input{discussion}` + Limitations + Ethics 节 | 不含 discussion；限制移入 conclusion | 结构不同 |
| `related_work.tex` | 分段引用，较松散 | 合并压缩，更紧凑 | docs 更精炼 |
| `references.bib` | @inproceedings 用于 arXiv | 已修正为 @article + venue 缩写 | docs 质量更高 |
| `discussion.tex` | 存在 | **缺失** | 需要复制 |

**如果按原计划用 artifacts 覆盖 docs，会丢失 docs 中的大量改进（实验分析扩充、bib 修正、结构重组等）。**

### 建议

反向同步更合理：以 `docs/paper/` 为准更新 `artifacts/_project/paper/latex/`，并将 `discussion.tex` 复制到 docs。

是否按原计划执行（artifacts → docs 覆盖），还是反向同步（docs → artifacts + 补 discussion.tex）？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 107882,
  "duration_api_ms": 108913,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "87e7d2fa-3544-463f-a483-079969decfa9",
  "total_cost_usd": 0.4124335,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 32804,
    "cache_read_input_tokens": 123203,
    "output_tokens": 5779,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32804,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3219,
        "cache_read_input_tokens": 31600,
        "cache_creation_input_tokens": 13045,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 13045
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1217,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001297,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 5779,
      "cacheReadInputTokens": 123203,
      "cacheCreationInputTokens": 32804,
      "webSearchRequests": 0,
      "costUSD": 0.4111365,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c2e6ab66-6d4c-4c3d-896d-ade9a38e9950"
}
```

</details>

---
