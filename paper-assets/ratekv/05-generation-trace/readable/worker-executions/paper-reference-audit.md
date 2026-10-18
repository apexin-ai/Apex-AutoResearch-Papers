# paper reference audit

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_paper_reference_audit_20260514T120938.log`
- **Structured JSON:** [`8a4447884c5bc5dd427e.json`](../../sessions/8a/8a4447884c5bc5dd427e.json)

## Before a recorded user message

49 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
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
  "uuid": "7c8fc3b6-040c-478e-922a-88ae5e72c1bc",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/memory/"
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
    "resetsAt": 1778922000,
    "rateLimitType": "seven_day",
    "utilization": 0.89,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "139e6c78-d5f8-4c7b-9e38-e7fbce5a16c4",
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a reference audit on the paper in `docs/paper/`. Let me start by reading the relevant files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "1cb1c3ba-2c15-456e-a843-c53586fc4fa6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUp8AHV4KEf8QwN38Jf3f7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11570,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11570
      },
      "output_tokens": 36,
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

开始引用审计。先读取 .bib 和所有 .tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "c219dcc6-33f7-4641-b42d-6f8242ba4099",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUp8AHV4KEf8QwN38Jf3f7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11570,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11570
      },
      "output_tokens": 36,
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

<details open><summary>🔧 Tool call — Read · `toolu_01R5ULipMjyYZh6sBkxBSdSu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "eb2116da-b903-43e1-85cf-ced5fd88dc17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUp8AHV4KEf8QwN38Jf3f7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11570,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11570
      },
      "output_tokens": 36,
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

_source line 7 · 2026-05-14T12:09:48.178Z_

<details><summary>↩ Tool result · `toolu_01R5ULipMjyYZh6sBkxBSdSu`</summary>

```text
1	% Auto-generated from literature_map.yaml (verified=true entries)
2	
3	@inproceedings{liu2024kivi,
4	  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},
5	  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},
6	  year = {2024},
7	  booktitle = {ICML 2024},
8	  url = {https://arxiv.org/abs/2402.02750},
9	}
10	
11	@inproceedings{hooper2024kvquant,
12	  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},
13	  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},
14	  year = {2024},
15	  booktitle = {NeurIPS 2024},
16	  url = {https://arxiv.org/abs/2401.18079},
17	}
18	
19	@inproceedings{lin2024qserve,
20	  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},
21	  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},
22	  year = {2025},
23	  booktitle = {MLSys 2025},
24	  url = {https://arxiv.org/abs/2405.04532},
25	}
26	
27	@inproceedings{he2024zipcache,
28	  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},
29	  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},
30	  year = {2024},
31	  booktitle = {NeurIPS 2024},
32	  url = {https://arxiv.org/abs/2405.14256},
33	}
34	
35	@misc{kang2024gear,
36	  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},
37	  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},
38	  year = {2024},
39	  note = {arXiv preprint},
40	  url = {https://arxiv.org/abs/2403.05527},
41	  eprint = {2403.05527},
42	  archivePrefix = {arXiv},
43	}
44	
45	@misc{duanmu2024skvq,
46	  title = {{SKVQ}: Sliding-window Key and Value Cache Quantization for Large Language Models},
47	  author = {Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zhang and Dahua Lin},
48	  year = {2024},
49	  note = {arXiv preprint},
50	  url = {https://arxiv.org/abs/2405.06219},
51	  eprint = {2405.06219},
52	  archivePrefix = {arXiv},
53	}
54	
55	@inproceedings{zhang2023h2o,
56	  title = {{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
57	  author = {Zhenyu Zhang and Ying Sheng and Tianyi Zhou and Tianlong Chen and Lianmin Zheng and Ruisi Cai and Zhao Song and Yuandong Tian and Christopher R{\'{e}} and Clark Barrett and Zhangyang Wang and Beidi Chen},
58	  year = {2023},
59	  booktitle = {NeurIPS 2023},
60	  url = {https://arxiv.org/abs/2306.14048},
61	}
62	
63	@inproceedings{li2024snapkv,
64	  title = {{SnapKV}: {LLM} Knows What You are Looking for Before Generation},
65	  author = {Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locatelli and Hanchen Ye and Tianle Cai and Patrick Lewis and Deming Chen},
66	  year = {2024},
67	  booktitle = {NeurIPS 2024},
68	  url = {https://arxiv.org/abs/2404.14469},
69	}
70	
71	@inproceedings{ge2024fastgen,
72	  title = {Model Tells You What to Discard: Adaptive {KV} Cache Compression for {LLMs}},
73	  author = {Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianfeng Gao},
74	  year = {2024},
75	  booktitle = {ICLR 2024},
76	  url = {https://arxiv.org/abs/2310.01801},
77	}
78	
79	@inproceedings{xiao2024streamingllm,
80	  title = {Efficient Streaming Language Models with Attention Sinks},
81	  author = {Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis},
82	  year = {2024},
83	  booktitle = {ICLR 2024},
84	  url = {https://arxiv.org/abs/2309.17453},
85	}
86	
87	@inproceedings{liu2024scissorhands,
88	  title = {Scissorhands: Exploiting the Persistence of Importance Hypothesis for {LLM} {KV} Cache Compression at Test Time},
89	  author = {Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie and Zhaozhuo Xu and Anastasios Kyrillidis and Anshumali Shrivastava},
90	  year = {2023},
91	  booktitle = {NeurIPS 2023},
92	  url = {https://arxiv.org/abs/2305.17118},
93	}
94	
95	@inproceedings{yang2024pyramidinfer,
96	  title = {{PyramidInfer}: Pyramid {KV} Cache Compression for High-throughput {LLM} Inference},
97	  author = {Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zhao},
98	  year = {2024},
99	  booktitle = {Findings of ACL 2024},
100	  url = {https://arxiv.org/abs/2405.12532},
101	}
102	
103	@misc{zuo2026ratequant,
104	  title = {{RateQuant}: Optimal Mixed-Precision {KV} Cache Quantization via Rate-Distortion Theory},
105	  author = {Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung},
106	  year = {2026},
107	  note = {arXiv preprint},
108	  url = {https://arxiv.org/abs/2605.06675},
109	  eprint = {2605.06675},
110	  archivePrefix = {arXiv},
111	}
112	
113	@misc{lei2026arkv,
114	  title = {{ARKV}: Adaptive and Resource-Efficient {KV} Cache Management under Limited Memory Budget for Long-Context Inference in {LLMs}},
115	  author = {Jianlong Lei and Shashikant Ilager},
116	  year = {2026},
117	  note = {arXiv preprint},
118	  url = {https://arxiv.org/abs/2603.08727},
119	  eprint = {2603.08727},
120	  archivePrefix = {arXiv},
121	}
122	
123	@misc{li2025kvmix,
124	  title = {{KVmix}: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for {KV} Cache},
125	  author = {Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang},
126	  year = {2025},
127	  note = {arXiv preprint},
128	  url = {https://arxiv.org/abs/2506.08018},
129	  eprint = {2506.08018},
130	  archivePrefix = {arXiv},
131	}
132	
133	@misc{zhang2025mixkvq,
134	  title = {{MixKVQ}: Query-Aware Mixed-Precision {KV} Cache Quantization for Long-Context Reasoning},
135	  author = {Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen},
136	  year = {2025},
137	  note = {arXiv preprint},
138	  url = {https://arxiv.org/abs/2512.19206},
139	  eprint = {2512.19206},
140	  archivePrefix = {arXiv},
141	}
142	
143	@inproceedings{kim2024squeezellm,
144	  title = {{SqueezeLLM}: Dense-and-Sparse Quantization},
145	  author = {Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sheng Shen and Michael W. Mahoney and Kurt Keutzer},
146	  year = {2024},
147	  booktitle = {ICML 2024},
148	  url = {https://arxiv.org/abs/2306.07629},
149	}
150	
151	@inproceedings{voita2019analyzing,
152	  title = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},
153	  author = {Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov},
154	  year = {2019},
155	  booktitle = {ACL 2019},
156	  url = {https://arxiv.org/abs/1905.09418},
157	}
158	
159	@inproceedings{michel2019sixteen,
160	  title = {Are Sixteen Heads Really Better than One?},
161	  author = {Paul Michel and Omer Levy and Graham Neubig},
162	  year = {2019},
163	  booktitle = {NeurIPS 2019},
164	  url = {https://arxiv.org/abs/1905.10650},
165	}
166	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "3a3d1d84-f1e7-48ea-8851-ef1acb4e2327",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml (verified=true entries)\n\n@inproceedings{liu2024kivi,\n  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},\n  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2402.02750},\n}\n\n@inproceedings{hooper2024kvquant,\n  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},\n  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2401.18079},\n}\n\n@inproceedings{lin2024qserve,\n  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},\n  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},\n  year = {2025},\n  booktitle = {MLSys 2025},\n  url = {https://arxiv.org/abs/2405.04532},\n}\n\n@inproceedings{he2024zipcache,\n  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},\n  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2405.14256},\n}\n\n@misc{kang2024gear,\n  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},\n  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},\n  year = {2024},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2403.05527},\n  eprint = {2403.05527},\n  archivePrefix = {arXiv},\n}\n\n@misc{duanmu2024skvq,\n  title = {{SKVQ}: Sliding-window Key and Value Cache Quantization for Large Language Models},\n  author = {Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zhang and Dahua Lin},\n  year = {2024},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2405.06219},\n  eprint = {2405.06219},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{zhang2023h2o,\n  title = {{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author = {Zhenyu Zhang and Ying Sheng and Tianyi Zhou and Tianlong Chen and Lianmin Zheng and Ruisi Cai and Zhao Song and Yuandong Tian and Christopher R{\\'{e}} and Clark Barrett and Zhangyang Wang and Beidi Chen},\n  year = {2023},\n  booktitle = {NeurIPS 2023},\n  url = {https://arxiv.org/abs/2306.14048},\n}\n\n@inproceedings{li2024snapkv,\n  title = {{SnapKV}: {LLM} Knows What You are Looking for Before Generation},\n  author = {Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locatelli and Hanchen Ye and Tianle Cai and Patrick Lewis and Deming Chen},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2404.14469},\n}\n\n@inproceedings{ge2024fastgen,\n  title = {Model Tells You What to Discard: Adaptive {KV} Cache Compression for {LLMs}},\n  author = {Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianfeng Gao},\n  year = {2024},\n  booktitle = {ICLR 2024},\n  url = {https://arxiv.org/abs/2310.01801},\n}\n\n@inproceedings{xiao2024streamingllm,\n  title = {Efficient Streaming Language Models with Attention Sinks},\n  author = {Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis},\n  year = {2024},\n  booktitle = {ICLR 2024},\n  url = {https://arxiv.org/abs/2309.17453},\n}\n\n@inproceedings{liu2024scissorhands,\n  title = {Scissorhands: Exploiting the Persistence of Importance Hypothesis for {LLM} {KV} Cache Compression at Test Time},\n  author = {Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie and Zhaozhuo Xu and Anastasios Kyrillidis and Anshumali Shrivastava},\n  year = {2023},\n  booktitle = {NeurIPS 2023},\n  url = {https://arxiv.org/abs/2305.17118},\n}\n\n@inproceedings{yang2024pyramidinfer,\n  title = {{PyramidInfer}: Pyramid {KV} Cache Compression for High-throughput {LLM} Inference},\n  author = {Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zhao},\n  year = {2024},\n  booktitle = {Findings of ACL 2024},\n  url = {https://arxiv.org/abs/2405.12532},\n}\n\n@misc{zuo2026ratequant,\n  title = {{RateQuant}: Optimal Mixed-Precision {KV} Cache Quantization via Rate-Distortion Theory},\n  author = {Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung},\n  year = {2026},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2605.06675},\n  eprint = {2605.06675},\n  archivePrefix = {arXiv},\n}\n\n@misc{lei2026arkv,\n  title = {{ARKV}: Adaptive and Resource-Efficient {KV} Cache Management under Limited Memory Budget for Long-Context Inference in {LLMs}},\n  author = {Jianlong Lei and Shashikant Ilager},\n  year = {2026},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2603.08727},\n  eprint = {2603.08727},\n  archivePrefix = {arXiv},\n}\n\n@misc{li2025kvmix,\n  title = {{KVmix}: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for {KV} Cache},\n  author = {Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2506.08018},\n  eprint = {2506.08018},\n  archivePrefix = {arXiv},\n}\n\n@misc{zhang2025mixkvq,\n  title = {{MixKVQ}: Query-Aware Mixed-Precision {KV} Cache Quantization for Long-Context Reasoning},\n  author = {Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2512.19206},\n  eprint = {2512.19206},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{kim2024squeezellm,\n  title = {{SqueezeLLM}: Dense-and-Sparse Quantization},\n  author = {Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sheng Shen and Michael W. Mahoney and Kurt Keutzer},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2306.07629},\n}\n\n@inproceedings{voita2019analyzing,\n  title = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n  author = {Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov},\n  year = {2019},\n  booktitle = {ACL 2019},\n  url = {https://arxiv.org/abs/1905.09418},\n}\n\n@inproceedings{michel2019sixteen,\n  title = {Are Sixteen Heads Really Better than One?},\n  author = {Paul Michel and Omer Levy and Graham Neubig},\n  year = {2019},\n  booktitle = {NeurIPS 2019},\n  url = {https://arxiv.org/abs/1905.10650},\n}\n",
      "numLines": 166,
      "startLine": 1,
      "totalLines": 166
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01CAJ6qe9d7M1c7obD4SDEBg`</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "a49e4a05-0409-489a-a899-940c11bd3a4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUp8AHV4KEf8QwN38Jf3f7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11570,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11570
      },
      "output_tokens": 36,
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

_source line 9 · 2026-05-14T12:09:48.758Z_

<details><summary>↩ Tool result · `toolu_01CAJ6qe9d7M1c7obD4SDEBg`</summary>

```text
docs/paper/main.tex
docs/paper/method.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/related_work.tex
docs/paper/analysis.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "883b9940-d39a-479c-811f-6e43480a4a79",
  "tool_use_result": {
    "filenames": [
      "docs/paper/main.tex",
      "docs/paper/method.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/related_work.tex",
      "docs/paper/analysis.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/experiments.tex"
    ],
    "durationMs": 15,
    "numFiles": 8,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now let me read all the .tex files to find all \cite{} references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "93ce050a-4288-4097-9a9e-7a2212762789",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWAfxCxf3V59zkdvYFgYtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3376
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

_source line 11_

现在读取所有 .tex 文件并提取 \cite{} 引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "8d4d90a1-390a-4f5b-b502-5714a08eb8bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWAfxCxf3V59zkdvYFgYtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3376
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01K4U27v5jDg2QmR3P11TGHp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "1266813d-7335-4414-8e3b-91da8be4e48b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWAfxCxf3V59zkdvYFgYtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3376
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

_source line 13 · 2026-05-14T12:09:53.024Z_

<details><summary>↩ Tool result · `toolu_01K4U27v5jDg2QmR3P11TGHp`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{enumitem}
10	
11	\title{When Does Non-Uniform KV Cache Quantization Help?\\Cardinality Constraints and a Heterogeneity Diagnostic}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	\input{abstract}
20	\end{abstract}
21	
22	\input{introduction}
23	\input{related_work}
24	\input{method}
25	\input{experiments}
26	\input{analysis}
27	\input{conclusion}
28	
29	\bibliography{references}
30	
31	\end{document}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "1e07aff7-94fb-42ca-bddd-8065b17f5f2d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\n\\title{When Does Non-Uniform KV Cache Quantization Help?\\\\Cardinality Constraints and a Heterogeneity Diagnostic}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{analysis}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\end{document}\n",
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

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_012GJMmpLioj57VT2g5bx6k2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "e00cc453-cf82-469c-81fe-890c6045e661",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWAfxCxf3V59zkdvYFgYtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3376
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

_source line 15 · 2026-05-14T12:09:53.386Z_

<details><summary>↩ Tool result · `toolu_012GJMmpLioj57VT2g5bx6k2`</summary>

```text
1	Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
2	We trace this failure to \emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.
3	We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
4	On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
5	The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
6	However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\ 7.13).
7	We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "3a6a666c-85c2-4ebf-a20f-e1de7d735f5e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex",
      "content": "Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\\{2, 4, 8, 16\\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).\nWe trace this failure to \\emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.\nWe show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.\nOn Qwen2.5-7B at $4\\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\\% reduction over uniform 4-bit.\nThe constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\\Delta{=}0.0000$), enabling use of a simple $O(H \\log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).\nHowever, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\\ 7.13).\nWe propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01T9DZaXVZRurytMAoSXA9Te`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "80f6a922-ddc3-4839-83fc-6802824922e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWAfxCxf3V59zkdvYFgYtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3376
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

_source line 17 · 2026-05-14T12:09:53.845Z_

<details><summary>↩ Tool result · `toolu_01T9DZaXVZRurytMAoSXA9Te`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.
17	The additive model predicts $\sim$11 PPL for these allocations; the actual PPL is $3$--$4\times$ higher.
18	At 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves close to its additive prediction---but 2-bit distortions are orders of magnitude larger.
19	When most heads are quantized to 2-bit simultaneously, cumulative truncation errors exceed the network's capacity to compensate, and perplexity degrades super-linearly.
20	
21	This observation points to a minimal intervention: cap the number of 2-bit assignments.
22	We add a single cardinality constraint $\sum_h \mathbb{1}[b_h{=}2] \leq k$ to the standard MCKP formulation (\S\ref{sec:method}).
23	On Qwen2.5-7B, setting $k{=}8$ (7\% of heads) yields 11.23 PPL---a 27.3\% reduction over uniform 4-bit.
24	The constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.
25	This is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.
26	
27	A surprising consequence is that, under the cardinality constraint, the choice of solver becomes irrelevant.
28	Constrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).
29	The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\S\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \log H)$ greedy algorithm without sacrificing solution quality.
30	A per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\% of the total improvement (\S\ref{sec:solver_equiv}).
31	
32	However, non-uniform allocation does not help universally.
33	On Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\ uniform 8.47---a marginal 0.2\% improvement.
34	On Mistral-7B-v0.3, it is slightly \emph{worse}: 7.16 vs.\ 7.13.
35	The difference across architectures traces to head sensitivity heterogeneity: Qwen's KV heads vary widely in 2-bit distortion, with Layer-0 heads contributing a disproportionate share, while Mistral's heads are nearly uniform in sensitivity.
36	When there is no heterogeneity to exploit, non-uniform allocation adds noise without benefit.
37	
38	This motivates a diagnostic question that prior work does not address: \emph{when} should a practitioner use per-head mixed-precision quantization?
39	We propose a heterogeneity diagnostic based on the top-5\% concentration of per-head distortion (\S\ref{sec:heterogeneity}).
40	On our three architectures, the metric distinguishes the beneficial case (Qwen, concentration 0.59--0.66, 27.3\% PPL improvement) from the neutral case (Llama, 0.34--0.59, marginal) and the counterproductive case (Mistral, 0.42, slightly worse than uniform) across the three tested architectures.
41	The diagnostic reuses profiling data already required by the solver and adds no computational overhead.
42	
43	Our contributions are:
44	\begin{enumerate}[nosep]
45	\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
46	
47	\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent per-head allocations across three architectures, enabling use of a simple greedy algorithm (\S\ref{sec:solver_equiv}).
48	
49	\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\S\ref{sec:heterogeneity}).
50	\end{enumerate}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "671b5688-f689-4223-b27c-95d2833aea11",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nPer-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.\nRecent work on KV cache quantization explores both uniform schemes~\\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\\cite{zhang2023h2o,li2024snapkv}.\nRateQuant~\\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\\{2,3,4,5,6\\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).\n\nIn practice, hardware-efficient inference requires bit-widths drawn from $\\{2, 4, 8, 16\\}$---the formats natively supported by modern accelerators.\nOn this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.\nOne might expect that exact MCKP solvers would fill this gap.\nThey do not.\nOn Qwen2.5-7B at $4\\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \\emph{far worse} than uniform 4-bit (15.45).\nThe optimization does not merely underperform; it fails catastrophically.\n\nThe root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.\nBoth solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.\nThe additive model predicts $\\sim$11 PPL for these allocations; the actual PPL is $3$--$4\\times$ higher.\nAt 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves close to its additive prediction---but 2-bit distortions are orders of magnitude larger.\nWhen most heads are quantized to 2-bit simultaneously, cumulative truncation errors exceed the network's capacity to compensate, and perplexity degrades super-linearly.\n\nThis observation points to a minimal intervention: cap the number of 2-bit assignments.\nWe add a single cardinality constraint $\\sum_h \\mathbb{1}[b_h{=}2] \\leq k$ to the standard MCKP formulation (\\S\\ref{sec:method}).\nOn Qwen2.5-7B, setting $k{=}8$ (7\\% of heads) yields 11.23 PPL---a 27.3\\% reduction over uniform 4-bit.\nThe constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.\nThis is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.\n\nA surprising consequence is that, under the cardinality constraint, the choice of solver becomes irrelevant.\nConstrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).\nThe constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\\S\\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \\log H)$ greedy algorithm without sacrificing solution quality.\nA per-layer brute-force oracle confirms near-optimality: the maximum gap across 28 layers is 0.02 PPL, 0.4\\% of the total improvement (\\S\\ref{sec:solver_equiv}).\n\nHowever, non-uniform allocation does not help universally.\nOn Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\\ uniform 8.47---a marginal 0.2\\% improvement.\nOn Mistral-7B-v0.3, it is slightly \\emph{worse}: 7.16 vs.\\ 7.13.\nThe difference across architectures traces to head sensitivity heterogeneity: Qwen's KV heads vary widely in 2-bit distortion, with Layer-0 heads contributing a disproportionate share, while Mistral's heads are nearly uniform in sensitivity.\nWhen there is no heterogeneity to exploit, non-uniform allocation adds noise without benefit.\n\nThis motivates a diagnostic question that prior work does not address: \\emph{when} should a practitioner use per-head mixed-precision quantization?\nWe propose a heterogeneity diagnostic based on the top-5\\% concentration of per-head distortion (\\S\\ref{sec:heterogeneity}).\nOn our three architectures, the metric distinguishes the beneficial case (Qwen, concentration 0.59--0.66, 27.3\\% PPL improvement) from the neutral case (Llama, 0.34--0.59, marginal) and the counterproductive case (Mistral, 0.42, slightly worse than uniform) across the three tested architectures.\nThe diagnostic reuses profiling data already required by the solver and adds no computational overhead.\n\nOur contributions are:\n\\begin{enumerate}[nosep]\n\\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\\times$ compression (\\S\\ref{sec:compounding}, \\S\\ref{sec:experiments}).\n\n\\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent per-head allocations across three architectures, enabling use of a simple greedy algorithm (\\S\\ref{sec:solver_equiv}).\n\n\\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\\S\\ref{sec:heterogeneity}).\n\\end{enumerate}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_011w8SQXzQ9v8jChAmiyShNP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "390de4d0-5e10-4cad-b3ea-e805cced478e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWAfxCxf3V59zkdvYFgYtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3376
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

_source line 19 · 2026-05-14T12:09:54.296Z_

<details><summary>↩ Tool result · `toolu_011w8SQXzQ9v8jChAmiyShNP`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{KV Cache Quantization.}
4	Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, and sliding-window adaptation~\cite{duanmu2024skvq}.
5	We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\{2,4,8,16\}$.
6	
7	\paragraph{KV Cache Eviction.}
8	Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
9	Our work focuses exclusively on the quantization allocation problem.
10	
11	\paragraph{Mixed-Precision Rate-Distortion Allocation.}
12	RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure.
13	On hardware-aligned $\{2,4,8,16\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.
14	Related mixed-precision work operates at coarser granularity (layer-level~\cite{li2025kvmix}, memory-budget-level~\cite{lei2026arkv}), at the weight level~\cite{kim2024squeezellm}, or dynamically at inference time~\cite{zhang2025mixkvq}; our allocation is static and per-head.
15	
16	\paragraph{Attention Head Analysis.}
17	Prior work studies head redundancy and pruning~\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.
18	Our analysis asks a different question: which heads are sensitive to \emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\S\ref{sec:heterogeneity}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "f41bcaa7-c55e-417b-b8e4-75694017b250",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{KV Cache Quantization.}\nUniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, and sliding-window adaptation~\\cite{duanmu2024skvq}.\nWe extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$.\n\n\\paragraph{KV Cache Eviction.}\nComplementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\\cite{zhang2023h2o}, per-head important tokens~\\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\\cite{liu2024scissorhands}, attention sinks~\\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\\cite{yang2024pyramidinfer}.\nOur work focuses exclusively on the quantization allocation problem.\n\n\\paragraph{Mixed-Precision Rate-Distortion Allocation.}\nRateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure.\nOn hardware-aligned $\\{2,4,8,16\\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.\nRelated mixed-precision work operates at coarser granularity (layer-level~\\cite{li2025kvmix}, memory-budget-level~\\cite{lei2026arkv}), at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.\n\n\\paragraph{Attention Head Analysis.}\nPrior work studies head redundancy and pruning~\\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.\nOur analysis asks a different question: which heads are sensitive to \\emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01Y6eKSP8Xfyw5fzRHMmLkmF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "f2a89c67-9127-4d71-ab4c-81c0b2413dd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWAfxCxf3V59zkdvYFgYtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3376
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

_source line 21 · 2026-05-14T12:09:55.278Z_

<details><summary>↩ Tool result · `toolu_01Y6eKSP8Xfyw5fzRHMmLkmF`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:formulation}
6	
7	We formulate per-head KV cache quantization as a constrained optimization problem.
8	Let $h \in \{1,\ldots,H\}$ index the KV heads across all layers, $b_h \in \mathcal{B}$ the bit-width assigned to head $h$, and $\mathcal{B} = \{2, 4, 8, 16\}$ the set of hardware-aligned bit-widths.
9	Each head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.
10	Given a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\times$ compression), we seek the allocation that minimizes total distortion:
11	\begin{equation}
12	\label{eq:objective}
13	\min_{\{b_h\}} \sum_{h=1}^{H} d_h(b_h) \quad \text{s.t.} \quad \frac{1}{H \cdot 16}\sum_{h=1}^{H} b_h \leq R.
14	\end{equation}
15	
16	This is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\mathcal{B}$ to minimize total distortion under a budget.
17	RateQuant~\cite{zuo2026ratequant} solves this for consecutive bit-widths $\{2,3,4,5,6\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).
18	Hardware-aligned bit-widths $\{2,4,8,16\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.
19	Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.
20	
21	\subsection{PPL-based Per-Head Profiling}
22	\label{sec:profiling}
23	
24	We profile each KV head independently by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\times$ 2048 tokens from WikiText-2 train.
25	This yields a distortion table of $H \times |\mathcal{B}|$ entries that serves as input to the solver.
26	
27	The optimization in Eq.~\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\sum_h d_h(b_h)$.
28	This holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.
29	At 2-bit, however, individual distortions are orders of magnitude larger, and the additive assumption breaks down.
30	
31	\subsection{Compounding Effect}
32	\label{sec:compounding}
33	
34	When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively.
35	The mechanism is straightforward: each head's quantized output feeds into the residual stream, and truncation errors from multiple 2-bit heads accumulate through subsequent layers.
36	When the number of 2-bit heads is small, these errors are absorbed by the remaining high-precision heads.
37	As the count grows, cumulative errors exceed the capacity of the residual stream to compensate, and PPL degrades super-linearly.
38	
39	\begin{figure}[t]
40	\centering
41	\includegraphics[width=\columnwidth]{figures/fig2_compounding_curve.pdf}
42	\caption{PPL on Qwen2.5-7B ($4\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}
43	\label{fig:compounding}
44	\end{figure}
45	
46	Unconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.
47	On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).
48	Standard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \approx 0$, so most 2-bit assignments appear free to the additive objective.
49	The resulting additive prediction is $\sum_h d_h(b_h) + \text{baseline} \approx 11$ PPL---$3\text{--}4\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.
50	
51	This compounding is specific to 2-bit quantization.
52	At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).
53	The qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.
54	
55	Figure~\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\times$ compression.
56	The curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.
57	
58	\subsection{Cardinality Constraint}
59	\label{sec:cardinality}
60	
61	The compounding effect motivates a simple addition to Eq.~\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.
62	\begin{equation}
63	\label{eq:constraint}
64	\sum_{h=1}^{H} \mathbb{1}[b_h = 2] \leq k.
65	\end{equation}
66	
67	The constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\ref{fig:compounding}).
68	For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\sim$7\% of heads).
69	
70	The constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.
71	
72	A natural question is whether Layer-0 heads require explicit protection, since attention heads in the first layer are known to carry disproportionate importance.
73	On Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\% relative to the bf16 baseline (9.81 $\to$ 12.94), L0H2 by 23.2\% (9.81 $\to$ 12.09), L0H3 by 11.7\% (9.81 $\to$ 10.96).
74	These values are large enough that no solver would assign 2-bit to Layer-0 under any reasonable budget.
75	We verify this empirically: running the solver with and without manual Layer-0 exclusion produces identical allocations across all 112 heads.
76	No manual exclusion rule is needed; the profiler signal is sufficient.
77	
78	\subsection{Solver Equivalence}
79	\label{sec:solver_equiv}
80	
81	\begin{table}[t]
82	\centering
83	\small
84	\caption{Solver comparison on Qwen2.5-7B at $4\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\leq}8$) makes greedy and MCKP produce identical allocations.\protect\footnotemark}
85	\label{tab:solver_equiv}
86	\begin{tabular}{llcccc}
87	\toprule
88	Solver & Constraint & PPL & \multicolumn{3}{c}{Bit distribution} \\
89	 & & & 2-bit & 4-bit & 8/16-bit \\
90	\midrule
91	Greedy & None & 32.45 & 68 & 30 & 14 \\
92	MCKP & None & 36.92 & 75 & 33 & 4 \\
93	Greedy & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
94	MCKP & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
95	Uniform & --- & 15.45 & 0 & 112 & 0 \\
96	\bottomrule
97	\end{tabular}
98	\end{table}
99	\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\times$ 2048 tok) achieves 10.91 (\S\ref{sec:profiling_resolution}).}
100	
101	With the cardinality constraint in place, greedy and MCKP produce identical results---not approximately, but exactly.
102	Table~\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.
103	We verify this at the per-head level across three models:
104	
105	\begin{itemize}[nosep]
106	\item \textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.
107	\item \textbf{Llama-3.1-8B:} 256/256 heads identical.
108	\item \textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.
109	\end{itemize}
110	
111	The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal.
112	Without it, greedy cascades into excessive 2-bit allocation: each additional 2-bit head looks locally beneficial (freeing budget) but contributes to the compounding effect that degrades global PPL.
113	The cardinality constraint breaks this cascade by capping the number of 2-bit heads, aligning local and global optima.
114	
115	The practical implication is that practitioners can use the simpler $O(H \log H)$ greedy algorithm instead of MCKP without sacrificing optimality.
116	
117	To verify that constrained MCKP is near-optimal, we perform a per-layer brute-force oracle on Qwen2.5-7B: for each of the 28 layers, we enumerate all $4^4{=}256$ bit-width assignments to the 4 KV heads and select the allocation minimizing per-layer PPL.
118	Of the 8 layers with non-trivial (non-all-4-bit) allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.0183 PPL---0.4\% of the constrained-vs-uniform improvement (4.53 PPL)---due to within-layer 2-bit head position swaps with no change to the per-layer bit budget.
119	Combined with the greedy--MCKP equivalence above, this closes the optimality chain: a simple $O(H \log H)$ greedy algorithm (runtime 0.005s) produces allocations within 0.02 PPL of the brute-force optimum.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "ade9c4d2-36cc-4a5b-af10-1b61ce37ab54",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nWe formulate per-head KV cache quantization as a constrained optimization problem.\nLet $h \\in \\{1,\\ldots,H\\}$ index the KV heads across all layers, $b_h \\in \\mathcal{B}$ the bit-width assigned to head $h$, and $\\mathcal{B} = \\{2, 4, 8, 16\\}$ the set of hardware-aligned bit-widths.\nEach head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.\nGiven a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\\times$ compression), we seek the allocation that minimizes total distortion:\n\\begin{equation}\n\\label{eq:objective}\n\\min_{\\{b_h\\}} \\sum_{h=1}^{H} d_h(b_h) \\quad \\text{s.t.} \\quad \\frac{1}{H \\cdot 16}\\sum_{h=1}^{H} b_h \\leq R.\n\\end{equation}\n\nThis is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\\mathcal{B}$ to minimize total distortion under a budget.\nRateQuant~\\cite{zuo2026ratequant} solves this for consecutive bit-widths $\\{2,3,4,5,6\\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).\nHardware-aligned bit-widths $\\{2,4,8,16\\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.\nMoreover, as we show in \\S\\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.\n\n\\subsection{PPL-based Per-Head Profiling}\n\\label{sec:profiling}\n\nWe profile each KV head independently by quantizing it to each $b \\in \\mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\\times$ 2048 tokens from WikiText-2 train.\nThis yields a distortion table of $H \\times |\\mathcal{B}|$ entries that serves as input to the solver.\n\nThe optimization in Eq.~\\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\\sum_h d_h(b_h)$.\nThis holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.\nAt 2-bit, however, individual distortions are orders of magnitude larger, and the additive assumption breaks down.\n\n\\subsection{Compounding Effect}\n\\label{sec:compounding}\n\nWhen many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively.\nThe mechanism is straightforward: each head's quantized output feeds into the residual stream, and truncation errors from multiple 2-bit heads accumulate through subsequent layers.\nWhen the number of 2-bit heads is small, these errors are absorbed by the remaining high-precision heads.\nAs the count grows, cumulative errors exceed the capacity of the residual stream to compensate, and PPL degrades super-linearly.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_compounding_curve.pdf}\n\\caption{PPL on Qwen2.5-7B ($4\\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}\n\\label{fig:compounding}\n\\end{figure}\n\nUnconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.\nOn Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).\nStandard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \\approx 0$, so most 2-bit assignments appear free to the additive objective.\nThe resulting additive prediction is $\\sum_h d_h(b_h) + \\text{baseline} \\approx 11$ PPL---$3\\text{--}4\\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.\n\nThis compounding is specific to 2-bit quantization.\nAt 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).\nThe qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.\n\nFigure~\\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\\times$ compression.\nThe curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.\n\n\\subsection{Cardinality Constraint}\n\\label{sec:cardinality}\n\nThe compounding effect motivates a simple addition to Eq.~\\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.\n\\begin{equation}\n\\label{eq:constraint}\n\\sum_{h=1}^{H} \\mathbb{1}[b_h = 2] \\leq k.\n\\end{equation}\n\nThe constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\\ref{fig:compounding}).\nFor Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\\sim$7\\% of heads).\n\nThe constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.\n\nA natural question is whether Layer-0 heads require explicit protection, since attention heads in the first layer are known to carry disproportionate importance.\nOn Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\\% relative to the bf16 baseline (9.81 $\\to$ 12.94), L0H2 by 23.2\\% (9.81 $\\to$ 12.09), L0H3 by 11.7\\% (9.81 $\\to$ 10.96).\nThese values are large enough that no solver would assign 2-bit to Layer-0 under any reasonable budget.\nWe verify this empirically: running the solver with and without manual Layer-0 exclusion produces identical allocations across all 112 heads.\nNo manual exclusion rule is needed; the profiler signal is sufficient.\n\n\\subsection{Solver Equivalence}\n\\label{sec:solver_equiv}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Solver comparison on Qwen2.5-7B at $4\\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\\leq}8$) makes greedy and MCKP produce identical allocations.\\protect\\footnotemark}\n\\label{tab:solver_equiv}\n\\begin{tabular}{llcccc}\n\\toprule\nSolver & Constraint & PPL & \\multicolumn{3}{c}{Bit distribution} \\\\\n & & & 2-bit & 4-bit & 8/16-bit \\\\\n\\midrule\nGreedy & None & 32.45 & 68 & 30 & 14 \\\\\nMCKP & None & 36.92 & 75 & 33 & 4 \\\\\nGreedy & $k{\\leq}8$ & 11.23 & 8 & 100 & 4 \\\\\nMCKP & $k{\\leq}8$ & 11.23 & 8 & 100 & 4 \\\\\nUniform & --- & 15.45 & 0 & 112 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\\times$ 2048 tok) achieves 10.91 (\\S\\ref{sec:profiling_resolution}).}\n\nWith the cardinality constraint in place, greedy and MCKP produce identical results---not approximately, but exactly.\nTable~\\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.\nWe verify this at the per-head level across three models:\n\n\\begin{itemize}[nosep]\n\\item \\textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.\n\\item \\textbf{Llama-3.1-8B:} 256/256 heads identical.\n\\item \\textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.\n\\end{itemize}\n\nThe constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal.\nWithout it, greedy cascades into excessive 2-bit allocation: each additional 2-bit head looks locally beneficial (freeing budget) but contributes to the compounding effect that degrades global PPL.\nThe cardinality constraint breaks this cascade by capping the number of 2-bit heads, aligning local and global optima.\n\nThe practical implication is that practitioners can use the simpler $O(H \\log H)$ greedy algorithm instead of MCKP without sacrificing optimality.\n\nTo verify that constrained MCKP is near-optimal, we perform a per-layer brute-force oracle on Qwen2.5-7B: for each of the 28 layers, we enumerate all $4^4{=}256$ bit-width assignments to the 4 KV heads and select the allocation minimizing per-layer PPL.\nOf the 8 layers with non-trivial (non-all-4-bit) allocations, MCKP matches the oracle on 5; the remaining 3 have a maximum gap of 0.0183 PPL---0.4\\% of the constrained-vs-uniform improvement (4.53 PPL)---due to within-layer 2-bit head position swaps with no change to the per-layer bit budget.\nCombined with the greedy--MCKP equivalence above, this closes the optimality chain: a simple $O(H \\log H)$ greedy algorithm (runtime 0.005s) produces allocations within 0.02 PPL of the brute-force optimum.",
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01TgH8DoKCb6g1RPhTD94iTt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "73601eef-9024-4606-856b-daea92d3336b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWAfxCxf3V59zkdvYFgYtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3376
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

_source line 23 · 2026-05-14T12:09:55.758Z_

<details><summary>↩ Tool result · `toolu_01TgH8DoKCb6g1RPhTD94iTt`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate on three architectures spanning different grouped-query attention (GQA) configurations:
9	\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\times$ 4 KV heads = 112 KV heads),
10	\textbf{Llama-3.1-8B} (4:1, 32 $\times$ 8 = 256 KV heads),
11	and \textbf{Mistral-7B-v0.3} (4:1, 32 $\times$ 8 = 256 KV heads, sliding window attention).
12	This selection covers the two dominant KV head counts (112 vs.\ 256) and both standard and sliding-window attention.
13	
14	\paragraph{Evaluation.}
15	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
16	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
17	
18	\paragraph{Profiling.}
19	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
20	We use two profiling resolutions: \emph{standard} (16 sequences $\times$ 512 tokens) and \emph{high-resolution} (64 sequences $\times$ 2048 tokens), both from WikiText-2 train.
21	Unless marked with $\dagger$, all results use standard-resolution profiling; \S\ref{sec:profiling_resolution} analyzes the effect of resolution.
22	
23	\paragraph{Compression and constraint.}
24	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
25	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).
26	
27	\paragraph{Baselines.}
28	We compare against:
29	(1)~uniform 4-bit quantization;
30	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
31	(3)~unconstrained MCKP allocation;
32	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
33	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
34	
35	\subsection{Main Results}
36	\label{sec:main_results}
37	
38	\begin{table}[t]
39	\centering
40	\small
41	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained allocation fails catastrophically on $\{2,4,8,16\}$; our cardinality constraint restores performance. Best constrained result per model in \textbf{bold}. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\ddagger$Best $k$ from ablation ($k{=}4$). The $\pm$0.06 on Qwen reports std over 3 calibration seeds (hires profiling); bit distributions are identical across seeds.}
42	\label{tab:main_results}
43	\begin{tabular}{lcccccc}
44	\toprule
45	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
46	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
47	\midrule
48	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{11.23}$\pm$0.06 \\
49	Llama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \textbf{8.45}$^\dagger$ \\
50	Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\dagger\ddagger}$ \\
51	\bottomrule
52	\end{tabular}
53	\end{table}
54	
55	Table~\ref{tab:main_results} summarizes the main results.
56	On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\% reduction over uniform 4-bit (15.45).
57	Higher-resolution profiling (64 seq $\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in \S\ref{sec:profiling_resolution}.
58	Without the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.
59	The constraint eliminates this failure mode entirely.
60	Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 (std is 1.3\% of the uniform gap), with 90.2\% three-way allocation agreement, confirming profiling stability.
61	
62	On Llama-3.1-8B, the improvement is marginal: 8.45 vs.\ 8.47 (0.2\%).
63	The profiler finds low sensitivity heterogeneity across Llama's 256 KV heads, leaving little room for non-uniform allocation to improve over uniform.
64	
65	On Mistral-7B-v0.3, constrained MCKP (7.16) is slightly worse than uniform (7.13, $+$0.4\%).
66	This is a genuine negative result: the profiler reports near-zero sensitivity differences across heads, meaning the optimization has no reliable signal to exploit.
67	Mistral's sliding-window attention may contribute to this uniformity by limiting head-level variation in effective context length.
68	
69	Unconstrained results for Llama and Mistral are omitted (---) as those experiments were conducted only on Qwen, where the failure mode is most pronounced.
70	Figure~\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.
71	
72	\begin{figure}[t]
73	\centering
74	\includegraphics[width=\columnwidth]{figures/fig3_allocation_comparison.pdf}
75	\caption{Bit-width allocation on Qwen2.5-7B at 4$\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}
76	\label{fig:allocation}
77	\end{figure}
78	
79	\subsection{Budget Sweep}
80	\label{sec:budget_sweep}
81	
82	\begin{table}[t]
83	\centering
84	\small
85	\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\geq$4$\times$). Standard-resolution profiling; hires results in \S\ref{sec:profiling_resolution}.}
86	\label{tab:budget_sweep}
87	\begin{tabular}{cccc}
88	\toprule
89	Compression & Uniform PPL & Constr.\ MCKP PPL & $\Delta$ PPL \\
90	\midrule
91	2$\times$ & 10.10 & 10.66 & $-$0.56 \\
92	4$\times$ & 15.45 & 11.23 & $+$4.21 \\
93	8$\times$ & 14{,}759 & 907 & $+$13{,}852 \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	Table~\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.
99	
100	At 2$\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\ 9.81 bf16, $+$0.29).
101	Per-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.
102	
103	At 4$\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\% improvement.
104	Hires profiling further reduces this to 10.91 (\S\ref{sec:profiling_resolution}).
105	
106	At 8$\times$, both methods degrade catastrophically---the budget is too aggressive for any allocation to preserve model quality.
107	However, constrained MCKP (907) is an order of magnitude better than uniform (14{,}759) because the constraint still protects Layer-0 heads at 8-bit, preventing total representational collapse.
108	Neither result is practically usable, but the gap demonstrates the protection mechanism at work.
109	
110	\subsection{Heuristic Baselines}
111	\label{sec:heuristic}
112	
113	\begin{table}[t]
114	\centering
115	\small
116	\caption{Constrained MCKP vs.\ heuristic baselines at 4$\times$ compression. L0-random reports median and mean$\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}4$ for Mistral).}
117	\label{tab:heuristic}
118	\begin{tabular}{lcccc}
119	\toprule
120	Model & MCKP & \multicolumn{2}{c}{L0-random} & Naive \\
121	 & & Median & Mean$\pm$Std & Positional \\
122	\midrule
123	Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
124	Llama-3.1-8B    & 8.45  & 10.04 & 10.48$\pm$1.03 & 9.94 \\
125	Mistral-7B-v0.3 & 7.16  & 7.59  & 7.56$\pm$0.09  & 7.48 \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	Table~\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.
131	
132	On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.
133	
134	On Llama, the gap is larger: MCKP achieves 8.45 vs.\ L0-random median 10.04.
135	The high variance of L0-random on this architecture (std$=$1.03) indicates that 2-bit assignment is position-sensitive on 256-head models, making random selection unreliable.
136	The naive positional heuristic (9.94) performs better than random but still 1.49 PPL worse than MCKP, confirming that depth alone is an imperfect proxy for head sensitivity.
137	
138	On Mistral, the gap is small (7.16 vs.\ 7.59), consistent with the low heterogeneity observed in \S\ref{sec:main_results}.
139	The low L0-random variance (std$=$0.09) further confirms that head sensitivities are nearly uniform, so the choice of which heads receive 2-bit has little impact.
140	All non-uniform strategies (MCKP 7.16, naive 7.48, L0-random 7.56) are worse than uniform 4-bit (7.13) on this architecture, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.
141	
142	\subsection{Downstream Evaluation}
143	\label{sec:downstream}
144	
145	\begin{table}[t]
146	\centering
147	\small
148	\caption{0-shot accuracy on Qwen2.5-7B at 4$\times$ compression. Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization.}
149	\label{tab:downstream}
150	\begin{tabular}{lcccc}
151	\toprule
152	Task & Baseline & Uniform & MCKP & $\Delta$ vs \\
153	 & (bf16) & (4-bit) & (Ours) & Uniform \\
154	\midrule
155	ARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\
156	HellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\
157	PIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\
158	WinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\
159	\midrule
160	Average    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	
165	Table~\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.
166	Constrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\ 0.660), with gains on all four benchmarks.
167	The largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.
168	
169	Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization, indicating that per-head bit allocation addresses much of the degradation, though a gap to bf16 remains.
170	
171	\subsection{Cross-Dataset Stability}
172	\label{sec:cross_dataset}
173	
174	To verify that the profiled allocation is not overfit to the calibration corpus, we profile on C4 and evaluate on WikiText-2, and vice versa, on Qwen2.5-7B at $4\times$ compression.
175	C4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\ 15.45 uniform, a 27\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).
176	In the reverse direction, WikiText-2-calibrated MCKP achieves 20.56 PPL on C4 (vs.\ 35.42 uniform, a 42\% reduction; C4 bf16 baseline is 12.65).
177	The two calibration corpora produce 96.4\% identical head assignments (108/112 heads), confirming that the profiled sensitivity ranking is stable across domains.
178	In both directions, constrained MCKP substantially outperforms uniform 4-bit quantization regardless of whether calibration and evaluation corpora are matched.
179	These results are reported for Qwen2.5-7B only; cross-dataset validation on Llama and Mistral is left for future work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "e1706cfd-0ce4-45b6-812e-07c4a176dc64",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe evaluate on three architectures spanning different grouped-query attention (GQA) configurations:\n\\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\\times$ 4 KV heads = 112 KV heads),\n\\textbf{Llama-3.1-8B} (4:1, 32 $\\times$ 8 = 256 KV heads),\nand \\textbf{Mistral-7B-v0.3} (4:1, 32 $\\times$ 8 = 256 KV heads, sliding window attention).\nThis selection covers the two dominant KV head counts (112 vs.\\ 256) and both standard and sliding-window attention.\n\n\\paragraph{Evaluation.}\nWe report perplexity (PPL, $\\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.\nFor downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.\n\n\\paragraph{Profiling.}\nPer-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\\{2, 4, 8, 16\\}$ and recording the PPL increase over the bf16 baseline.\nWe use two profiling resolutions: \\emph{standard} (16 sequences $\\times$ 512 tokens) and \\emph{high-resolution} (64 sequences $\\times$ 2048 tokens), both from WikiText-2 train.\nUnless marked with $\\dagger$, all results use standard-resolution profiling; \\S\\ref{sec:profiling_resolution} analyzes the effect of resolution.\n\n\\paragraph{Compression and constraint.}\nThe default target is 4$\\times$ compression (average 4 bits, budget ratio 0.25).\nThe cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \\S\\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).\n\n\\paragraph{Baselines.}\nWe compare against:\n(1)~uniform 4-bit quantization;\n(2)~unconstrained greedy allocation (RateQuant-style~\\cite{zuo2026ratequant});\n(3)~unconstrained MCKP allocation;\n(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\\pm$std and median);\nand (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{PPL ($\\downarrow$) on WikiText-2 at 4$\\times$ compression. Unconstrained allocation fails catastrophically on $\\{2,4,8,16\\}$; our cardinality constraint restores performance. Best constrained result per model in \\textbf{bold}. $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\\ddagger$Best $k$ from ablation ($k{=}4$). The $\\pm$0.06 on Qwen reports std over 3 calibration seeds (hires profiling); bit distributions are identical across seeds.}\n\\label{tab:main_results}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & Baseline & Uniform & \\multicolumn{2}{c}{Unconstrained} & Ours \\\\\n & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\\\\n\\midrule\nQwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \\textbf{11.23}$\\pm$0.06 \\\\\nLlama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \\textbf{8.45}$^\\dagger$ \\\\\nMistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\\dagger\\ddagger}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:main_results} summarizes the main results.\nOn Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\\% reduction over uniform 4-bit (15.45).\nHigher-resolution profiling (64 seq $\\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in \\S\\ref{sec:profiling_resolution}.\nWithout the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \\emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.\nThe constraint eliminates this failure mode entirely.\nAcross 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\\pm$0.06 (std is 1.3\\% of the uniform gap), with 90.2\\% three-way allocation agreement, confirming profiling stability.\n\nOn Llama-3.1-8B, the improvement is marginal: 8.45 vs.\\ 8.47 (0.2\\%).\nThe profiler finds low sensitivity heterogeneity across Llama's 256 KV heads, leaving little room for non-uniform allocation to improve over uniform.\n\nOn Mistral-7B-v0.3, constrained MCKP (7.16) is slightly worse than uniform (7.13, $+$0.4\\%).\nThis is a genuine negative result: the profiler reports near-zero sensitivity differences across heads, meaning the optimization has no reliable signal to exploit.\nMistral's sliding-window attention may contribute to this uniformity by limiting head-level variation in effective context length.\n\nUnconstrained results for Llama and Mistral are omitted (---) as those experiments were conducted only on Qwen, where the failure mode is most pronounced.\nFigure~\\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_allocation_comparison.pdf}\n\\caption{Bit-width allocation on Qwen2.5-7B at 4$\\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}\n\\label{fig:allocation}\n\\end{figure}\n\n\\subsection{Budget Sweep}\n\\label{sec:budget_sweep}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\\geq$4$\\times$). Standard-resolution profiling; hires results in \\S\\ref{sec:profiling_resolution}.}\n\\label{tab:budget_sweep}\n\\begin{tabular}{cccc}\n\\toprule\nCompression & Uniform PPL & Constr.\\ MCKP PPL & $\\Delta$ PPL \\\\\n\\midrule\n2$\\times$ & 10.10 & 10.66 & $-$0.56 \\\\\n4$\\times$ & 15.45 & 11.23 & $+$4.21 \\\\\n8$\\times$ & 14{,}759 & 907 & $+$13{,}852 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.\n\nAt 2$\\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\\ 9.81 bf16, $+$0.29).\nPer-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.\n\nAt 4$\\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\\% improvement.\nHires profiling further reduces this to 10.91 (\\S\\ref{sec:profiling_resolution}).\n\nAt 8$\\times$, both methods degrade catastrophically---the budget is too aggressive for any allocation to preserve model quality.\nHowever, constrained MCKP (907) is an order of magnitude better than uniform (14{,}759) because the constraint still protects Layer-0 heads at 8-bit, preventing total representational collapse.\nNeither result is practically usable, but the gap demonstrates the protection mechanism at work.\n\n\\subsection{Heuristic Baselines}\n\\label{sec:heuristic}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Constrained MCKP vs.\\ heuristic baselines at 4$\\times$ compression. L0-random reports median and mean$\\pm$std over 5 seeds. All methods use per-model optimal $k$ ($k{=}8$ for Qwen, $k{=}2$ for Llama, $k{=}4$ for Mistral).}\n\\label{tab:heuristic}\n\\begin{tabular}{lcccc}\n\\toprule\nModel & MCKP & \\multicolumn{2}{c}{L0-random} & Naive \\\\\n & & Median & Mean$\\pm$Std & Positional \\\\\n\\midrule\nQwen2.5-7B      & 11.23 & 11.52 & 11.69$\\pm$0.47 & 12.23 \\\\\nLlama-3.1-8B    & 8.45  & 10.04 & 10.48$\\pm$1.03 & 9.94 \\\\\nMistral-7B-v0.3 & 7.16  & 7.59  & 7.56$\\pm$0.09  & 7.48 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.\n\nOn Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.\n\nOn Llama, the gap is larger: MCKP achieves 8.45 vs.\\ L0-random median 10.04.\nThe high variance of L0-random on this architecture (std$=$1.03) indicates that 2-bit assignment is position-sensitive on 256-head models, making random selection unreliable.\nThe naive positional heuristic (9.94) performs better than random but still 1.49 PPL worse than MCKP, confirming that depth alone is an imperfect proxy for head sensitivity.\n\nOn Mistral, the gap is small (7.16 vs.\\ 7.59), consistent with the low heterogeneity observed in \\S\\ref{sec:main_results}.\nThe low L0-random variance (std$=$0.09) further confirms that head sensitivities are nearly uniform, so the choice of which heads receive 2-bit has little impact.\nAll non-uniform strategies (MCKP 7.16, naive 7.48, L0-random 7.56) are worse than uniform 4-bit (7.13) on this architecture, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.\n\n\\subsection{Downstream Evaluation}\n\\label{sec:downstream}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{0-shot accuracy on Qwen2.5-7B at 4$\\times$ compression. Constrained MCKP recovers approximately 73\\% of the accuracy lost by uniform 4-bit quantization.}\n\\label{tab:downstream}\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Baseline & Uniform & MCKP & $\\Delta$ vs \\\\\n & (bf16) & (4-bit) & (Ours) & Uniform \\\\\n\\midrule\nARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\\\\nHellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\\\\nPIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\\\\nWinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\\\\n\\midrule\nAverage    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.\nConstrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\\ 0.660), with gains on all four benchmarks.\nThe largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.\n\nConstrained MCKP recovers approximately 73\\% of the accuracy lost by uniform 4-bit quantization, indicating that per-head bit allocation addresses much of the degradation, though a gap to bf16 remains.\n\n\\subsection{Cross-Dataset Stability}\n\\label{sec:cross_dataset}\n\nTo verify that the profiled allocation is not overfit to the calibration corpus, we profile on C4 and evaluate on WikiText-2, and vice versa, on Qwen2.5-7B at $4\\times$ compression.\nC4-calibrated MCKP achieves 11.29 PPL on WikiText-2 (vs.\\ 15.45 uniform, a 27\\% reduction), only 0.06 PPL above the WikiText-2-calibrated result (11.23).\nIn the reverse direction, WikiText-2-calibrated MCKP achieves 20.56 PPL on C4 (vs.\\ 35.42 uniform, a 42\\% reduction; C4 bf16 baseline is 12.65).\nThe two calibration corpora produce 96.4\\% identical head assignments (108/112 heads), confirming that the profiled sensitivity ranking is stable across domains.\nIn both directions, constrained MCKP substantially outperforms uniform 4-bit quantization regardless of whether calibration and evaluation corpora are matched.\nThese results are reported for Qwen2.5-7B only; cross-dataset validation on Llama and Mistral is left for future work.",
      "numLines": 179,
      "startLine": 1,
      "totalLines": 179
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01QNgkD86otdeWTXjW4YpoMr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "77e6c93e-9a73-4d5a-9a9d-3116cbd126ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWAfxCxf3V59zkdvYFgYtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3376
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

_source line 25 · 2026-05-14T12:09:56.152Z_

<details><summary>↩ Tool result · `toolu_01QNgkD86otdeWTXjW4YpoMr`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across three architectures at $4\times$ compression.
12	Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.
13	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit.
14	Llama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\ $+$0.38).
15	Mistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.
16	Here, constrained MCKP is slightly \emph{worse} than uniform ($+$0.13 vs.\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\times$ compression. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok).}
22	\label{tab:heterogeneity}
23	\begin{tabular}{lccccc}
24	\toprule
25	Model & GQA & Top-5\% & $\Delta$ PPL & $\Delta$ PPL & Recommendation \\
26	 & Ratio & Conc. & (Uniform) & (Ours) & \\
27	\midrule
28	Qwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\
29	Llama-3.1-8B$^\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\
30	Mistral-7B-v0.3$^\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\begin{figure*}[t]
36	\centering
37	\includegraphics[width=\textwidth]{figures/fig1_head_delta_heatmap.pdf}
38	\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}
39	\label{fig:heatmap}
40	\end{figure*}
41	
42	Figure~\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.
43	The contrast is stark: Qwen's Layer-0 heads show high distortion (dark cells) while mid-to-deep layers are near-zero; Mistral shows uniformly low distortion across all layers and heads.
44	
45	\subsection{Diagnostic Framework}
46	\label{sec:diagnostic}
47	
48	The heterogeneity characterization yields a preliminary guideline, based on three architectures, for deciding when non-uniform allocation is worthwhile:
49	
50	\begin{enumerate}[nosep]
51	\item Run per-head profiling as described in \S\ref{sec:profiling}.
52	\item Compute the top-5\% concentration from the resulting distortion table.
53	\item Select allocation strategy:
54	  \begin{itemize}[nosep]
55	  \item Concentration ${>}\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\% PPL improvement).
56	  \item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\% at $4\times$).
57	  \item Near-zero absolute distortion for most heads: use uniform directly (Mistral case; non-uniform is counterproductive).
58	  \end{itemize}
59	\end{enumerate}
60	
61	The diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.
62	This avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.
63	The thresholds above are derived from three architectures and should be validated on a broader set of models before being treated as general rules.
64	
65	\subsection{Aggressive Compression Amplifies Benefit}
66	\label{sec:aggressive}
67	
68	At $4\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.
69	At more aggressive ratios, the picture changes: at $5.3\times$ (average 3 bits), constrained MCKP achieves $45\times$ lower PPL than uniform on Llama (57.60 vs.\ 2643.77) and $44\times$ on Mistral (11.91 vs.\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.
70	At $8\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).
71	The intermediate regime ($5.3\times$) provides the largest relative benefit.
72	
73	\subsection{Profiling Resolution}
74	\label{sec:profiling_resolution}
75	
76	We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
77	
78	High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
79	Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\% reduction.
80	The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
81	
82	The additional signal changes 8 of 112 head assignments.
83	High-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.
84	
85	\subsection{KV Separation Ablation}
86	\label{sec:kv_separation}
87	
88	We test whether treating K and V caches as independent items in the MCKP solver---allowing different bit-widths for K and V within the same head---improves over joint allocation where K and V share a bit-width.
89	
90	Joint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).
91	The degradation stems from K-side over-compression: the separated solver doubles the maximum number of 2-bit K items to 16 (vs.\ 8 in the joint formulation), since K and V are counted independently against the cardinality constraint.
92	Meanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.
93	
94	Of the 112 heads, 21 show K$\neq$V asymmetry in the separated allocation, all with K receiving a lower bit-width than V.
95	This systematic asymmetry suggests that K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content.
96	
97	Joint allocation is sufficient under the current constraint formulation.
98	Separated K/V allocation with per-side cardinality constraints---limiting 2-bit assignments independently for K and V---is a direction for future work.
99	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "2221360d-3470-4589-95a9-1cb08292d8f3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Heterogeneity Characterization}\n\\label{sec:heterogeneity}\n\nThe benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.\nWe quantify this with a \\emph{top-5\\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\\% of heads.\nHigh concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.\n\nTable~\\ref{tab:heterogeneity} summarizes the results across three architectures at $4\\times$ compression.\nQwen2.5-7B exhibits the highest heterogeneity (top-5\\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\\% improvement over uniform 4-bit.\nLlama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\\ $+$0.38).\nMistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.\nHere, constrained MCKP is slightly \\emph{worse} than uniform ($+$0.13 vs.\\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\\times$ compression. $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok).}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & GQA & Top-5\\% & $\\Delta$ PPL & $\\Delta$ PPL & Recommendation \\\\\n & Ratio & Conc. & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\\\\nLlama-3.1-8B$^\\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\\\\nMistral-7B-v0.3$^\\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_head_delta_heatmap.pdf}\n\\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}\n\\label{fig:heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.\nThe contrast is stark: Qwen's Layer-0 heads show high distortion (dark cells) while mid-to-deep layers are near-zero; Mistral shows uniformly low distortion across all layers and heads.\n\n\\subsection{Diagnostic Framework}\n\\label{sec:diagnostic}\n\nThe heterogeneity characterization yields a preliminary guideline, based on three architectures, for deciding when non-uniform allocation is worthwhile:\n\n\\begin{enumerate}[nosep]\n\\item Run per-head profiling as described in \\S\\ref{sec:profiling}.\n\\item Compute the top-5\\% concentration from the resulting distortion table.\n\\item Select allocation strategy:\n  \\begin{itemize}[nosep]\n  \\item Concentration ${>}\\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\\% PPL improvement).\n  \\item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\\% at $4\\times$).\n  \\item Near-zero absolute distortion for most heads: use uniform directly (Mistral case; non-uniform is counterproductive).\n  \\end{itemize}\n\\end{enumerate}\n\nThe diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.\nThis avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.\nThe thresholds above are derived from three architectures and should be validated on a broader set of models before being treated as general rules.\n\n\\subsection{Aggressive Compression Amplifies Benefit}\n\\label{sec:aggressive}\n\nAt $4\\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.\nAt more aggressive ratios, the picture changes: at $5.3\\times$ (average 3 bits), constrained MCKP achieves $45\\times$ lower PPL than uniform on Llama (57.60 vs.\\ 2643.77) and $44\\times$ on Mistral (11.91 vs.\\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.\nAt $8\\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).\nThe intermediate regime ($5.3\\times$) provides the largest relative benefit.\n\n\\subsection{Profiling Resolution}\n\\label{sec:profiling_resolution}\n\nWe compare standard-resolution profiling (16 sequences $\\times$ 512 tokens) against high-resolution profiling (64 sequences $\\times$ 2048 tokens) on Qwen2.5-7B at $4\\times$ compression.\n\nHigh-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).\nRelative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\\% reduction.\nThe improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\\times$ more).\n\nThe additional signal changes 8 of 112 head assignments.\nHigh-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.\n\n\\subsection{KV Separation Ablation}\n\\label{sec:kv_separation}\n\nWe test whether treating K and V caches as independent items in the MCKP solver---allowing different bit-widths for K and V within the same head---improves over joint allocation where K and V share a bit-width.\n\nJoint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).\nThe degradation stems from K-side over-compression: the separated solver doubles the maximum number of 2-bit K items to 16 (vs.\\ 8 in the joint formulation), since K and V are counted independently against the cardinality constraint.\nMeanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.\n\nOf the 112 heads, 21 show K$\\neq$V asymmetry in the separated allocation, all with K receiving a lower bit-width than V.\nThis systematic asymmetry suggests that K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content.\n\nJoint allocation is sufficient under the current constraint formulation.\nSeparated K/V allocation with per-side cardinality constraints---limiting 2-bit assignments independently for K and V---is a direction for future work.\n",
      "numLines": 99,
      "startLine": 1,
      "totalLines": 99
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01U3sboQH2csoBU4zfmYg9kF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "93c3c5c5-ef76-4eb5-8d5a-f8424aea09c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HWAfxCxf3V59zkdvYFgYtF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3376,
      "cache_read_input_tokens": 23411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3376
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

_source line 27 · 2026-05-14T12:09:56.352Z_

<details><summary>↩ Tool result · `toolu_01U3sboQH2csoBU4zfmYg9kF`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.
4	A single constraint---limiting simultaneously active 2-bit heads to $k \leq 8$ (7\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\% improvement at $4\times$ compression.
5	Under the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\Delta = 0.0000$), so a simple $O(H \log H)$ greedy algorithm suffices.
6	The benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs.\ 7.13 PPL).
7	This diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \emph{before deployment} whether non-uniform quantization is worthwhile for a given model.
8	
9	\paragraph{Limitations.}
10	Our study has several limitations that temper the generality of the findings.
11	First, we evaluate only three 7B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.
12	Second, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnostics remain unexplored and could yield different allocation decisions.
13	Third, we report perplexity and downstream accuracy but no real-kernel latency benchmarks, leaving the practical inference speedup from mixed-precision allocation unquantified.
14	Fourth, we have not verified whether these findings transfer to larger scales (70B+), where head counts and attention patterns differ substantially.
15	Finally, although we validate on four downstream tasks, profiling and primary evaluation use a single dataset (WikiText-2).
16	
17	\paragraph{Future Work.}
18	Extending evaluation to 70B+ models would test whether the heterogeneity--benefit relationship holds at scale.
19	Integration with production inference engines (vLLM, TensorRT-LLM) would enable real-kernel latency measurement, and investigating per-side K/V cardinality constraints (\S\ref{sec:kv_separation}) or dynamic per-request allocation could further improve the framework.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "57c7926a-2cc4-41f8-a562-fbe49720c1fd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.\nA single constraint---limiting simultaneously active 2-bit heads to $k \\leq 8$ (7\\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\\% improvement at $4\\times$ compression.\nUnder the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\\Delta = 0.0000$), so a simple $O(H \\log H)$ greedy algorithm suffices.\nThe benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs.\\ 7.13 PPL).\nThis diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \\emph{before deployment} whether non-uniform quantization is worthwhile for a given model.\n\n\\paragraph{Limitations.}\nOur study has several limitations that temper the generality of the findings.\nFirst, we evaluate only three 7B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.\nSecond, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnostics remain unexplored and could yield different allocation decisions.\nThird, we report perplexity and downstream accuracy but no real-kernel latency benchmarks, leaving the practical inference speedup from mixed-precision allocation unquantified.\nFourth, we have not verified whether these findings transfer to larger scales (70B+), where head counts and attention patterns differ substantially.\nFinally, although we validate on four downstream tasks, profiling and primary evaluation use a single dataset (WikiText-2).\n\n\\paragraph{Future Work.}\nExtending evaluation to 70B+ models would test whether the heterogeneity--benefit relationship holds at scale.\nIntegration with production inference engines (vLLM, TensorRT-LLM) would enable real-kernel latency measurement, and investigating per-side K/V cardinality constraints (\\S\\ref{sec:kv_separation}) or dynamic per-request allocation could further improve the framework.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me extract:

1. All bib keys from references.bib
2. All \cite{} keys from .tex files
3. Check for orphans, missing, duplicates, format issues, year issues

**Bib keys:**
1. liu2024kivi
2. hooper2024kvquant
3. lin2024qserve
4. he2024zipcache
5. kang2024gear
6. duanmu2024skvq
7. zhang2023h2o


8. li2024snapkv
9. ge2024fastgen
10. xiao2024streamingllm
11. liu2024scissorhands
12. yang2024pyramidinfer
13. zuo2026ratequant
14. lei2026arkv
15. li2025kvmix
16. zhang2025mixkvq
17. kim2024squeezellm
18. voita2019analyzing
19. michel2019sixteen

That gives me 19 total bib entries to work with. Now I'm scanning through the .tex files to find all citations, starting with abstract.tex which has none, then introduction.tex where I see liu2024kivi, hooper2024kvquant, lin2024qserve, and he2024zipcache cited.

Moving into related_work.tex, I'm tracking citations across multiple lines—liu2024kivi and hooper2024kvquant appear early, followed by lin2024qserve and he2024zipcache on line 4, then kang2024gear and duanmu2024skvq also on line 4. Further down, zhang2023h2o shows up on line 8 alongside li2024snapkv and ge2024fastgen, with liu2024scissorhands, xiao2024streamingllm, and yang2024pyramidinfer also cited in that section, and zuo2026ratequant appearing as well.

Continuing through method.tex and experiments.tex, I see zuo2026ratequant cited again, and then in the later sections I'm finding li2025kvmix, lei2026arkv, kim2024squeezellm, and zhang2025mixkvq on lines 14 and 17, plus voita2019analyzing and michel2019sixteen. Analysis, conclusion, and main files don't have any citations to track.

Compiling the unique keys, I've got liu2024kivi, hooper2024kvquant, lin2024qserve, he2024zipcache, ge2024fastgen, lei2026arkv, zhang2023h2o, li2024snapkv, and zuo2026ratequant confirmed across the documents.

Now checking the remaining entries—kang2024gear, duanmu2024skvq, liu2024scissorhands, xiao2024streamingllm, yang2024pyramidinfer, li2025kvmix, kim2024squeezellm, zhang2025mixkvq, voita2019analyzing, and michel2019sixteen—all 19 bib entries are accounted for and cited. No orphans or missing references.

Looking at the bibliography entries themselves, each one appears to be a distinct paper with no obvious duplicates. Spot-checking the format, they all have the required fields—title, author, year, and either a booktitle or journal field where appropriate. Continuing through the bibliography entries, I'm verifying the remaining papers have their required fields—most have titles, authors, years, and booktitles, while a few arXiv preprints use notes instead. Checking the year fields more carefully now—I notice lin2024qserve has a mismatch where the key indicates 2024 but the year field shows 2025 with MLSys 2025 as the booktitle, so that's inconsistent. Similarly, liu2024scissorhands appears to have a key-year discrepancy I need to verify.

Let me spot-check a few entries to validate the data: liu2024kivi on asymmetric 2-bit KV cache quantization, zhang2023h2o on heavy-hitter oracle methods, voita2019analyzing on multi-head attention analysis, he2024zipcache on salient token identification for KV quantization, and zuo2026ratequant to confirm the details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "dbd47894-dd23-4267-ab2c-fa32a0467435",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D3Av1Ydp7w7oztZksRQCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14914,
      "cache_read_input_tokens": 26787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14914
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

_source line 29_

数据收集完毕。现在做引用真实性抽查，搜索 5 篇论文验证真实性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "88baf4fb-274c-4c29-a51e-e18044800477",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D3Av1Ydp7w7oztZksRQCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14914,
      "cache_read_input_tokens": 26787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14914
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

_source line 30_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AJc4WvUwiFir1bhK9tMf1Z`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "0098381c-75ad-490b-92ed-71d1219f2807",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014D3Av1Ydp7w7oztZksRQCq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14914,
      "cache_read_input_tokens": 26787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14914
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

_source line 31 · 2026-05-14T12:10:29.604Z_

<details><summary>↩ Tool result · `toolu_01AJc4WvUwiFir1bhK9tMf1Z`</summary>

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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "ac4466f0-6d27-4acc-b21d-7b424da01d17",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FgZQu5w2EVv2dsu7HzwDLF`</summary>

```json
{
  "query": "KIVI Tuning-Free Asymmetric 2bit Quantization KV Cache Zirui Liu ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "e2c7e7c7-7e9c-461b-a1c3-fd413d81bfec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjQQcXfjjWKTvYhAiWczxX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 41701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2775
      },
      "output_tokens": 52,
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

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TpJ9qYVnairg7sLYJdHxSb`</summary>

```json
{
  "query": "H2O Heavy-Hitter Oracle Efficient Generative Inference LLM Zhenyu Zhang NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "86977b5a-1148-4ebe-b5e8-6a88387f1101",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjQQcXfjjWKTvYhAiWczxX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 41701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2775
      },
      "output_tokens": 52,
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

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016YT1L4iexDrcTvcxwfX5QW`</summary>

```json
{
  "query": "Analyzing Multi-Head Self-Attention Specialized Heads Heavy Lifting Pruned Elena Voita ACL 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "3e96aa6a-0ec5-4b91-abcf-b22a3a78a90f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjQQcXfjjWKTvYhAiWczxX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 41701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2775
      },
      "output_tokens": 52,
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

_source line 35_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BrpSBTu1YR4Nefs8K8jvJU`</summary>

```json
{
  "query": "ZipCache Accurate Efficient KV Cache Quantization Salient Token Yefei He NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "f3088290-d848-4598-ba06-278e9c79e596",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjQQcXfjjWKTvYhAiWczxX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 41701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2775
      },
      "output_tokens": 52,
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

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SFUQor16PS3eTvj2Vhst82`</summary>

```json
{
  "query": "RateQuant Optimal Mixed-Precision KV Cache Quantization Rate-Distortion Theory Fei Zuo arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "77bbfc96-bb51-48f7-871e-6619299b9295",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PjQQcXfjjWKTvYhAiWczxX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2775,
      "cache_read_input_tokens": 41701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2775
      },
      "output_tokens": 52,
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

_source line 37 · 2026-05-14T12:10:40.632Z_

<details><summary>↩ Tool result · `toolu_01FgZQu5w2EVv2dsu7HzwDLF`</summary>

```text
Web search results for query: "KIVI Tuning-Free Asymmetric 2bit Quantization KV Cache Zirui Liu ICML 2024"

Links: [{"title":"GitHub - jy-yuan/KIVI: [ICML 2024] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache · GitHub","url":"https://github.com/jy-yuan/KIVI"},{"title":"[2402.02750] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://arxiv.org/abs/2402.02750"},{"title":"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://proceedings.mlr.press/v235/liu24bz.html"},{"title":"[PDF] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache | Semantic Scholar","url":"https://www.semanticscholar.org/paper/KIVI:-A-Tuning-Free-Asymmetric-2bit-Quantization-KV-Liu-Yuan/a3e000e0d7f64c1d094c2a8bf6f43992cbabe91b"},{"title":"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://arxiv.org/html/2402.02750v2"},{"title":"ICML Poster KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://icml.cc/virtual/2024/poster/34318"},{"title":"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache - Experts@Minnesota","url":"https://experts.umn.edu/en/publications/kivi-a-tuning-free-asymmetric-2bit-quantization-for-kv-cache/"},{"title":"KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bz/liu24bz.pdf"},{"title":"dblp: KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache.","url":"https://dblp.org/rec/conf/icml/LiuYJZXBC024.html"},{"title":"[2402.02750v2] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache","url":"https://arxiv.org/abs/2402.02750v2"}]

Based on the search results, here's information about the KIVI paper:

## Overview

KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache was authored by Zirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu, and was published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024).

## Problem Addressed

The paper addresses the challenge that while efficiently serving large language models requires batching many requests to reduce cost per request, the key-value (KV) cache significantly increases memory demands and becomes a bottleneck in speed and memory usage, with memory demand increasing with larger batch sizes and longer context lengths.

## Key Innovation

The authors conducted a comprehensive study on element distribution in KV cache of popular LLMs and found that the key cache should be quantized per-channel while the value cache should be quantized per-token, leading to the development of the tuning-free 2bit KV cache quantization algorithm named KIVI.

## Performance Results

KIVI's hardware-friendly design allows LLMs like Llama-2, Falcon, and Mistral to maintain comparable quality levels while reducing peak memory usage by 2.6 times, enabling up to 4 times larger batch sizes and increasing throughput by 2.35 to 3.47 times in real LLM inference workloads.

## Resources

The paper is available on arXiv (2402.02750) and has an official GitHub repository at https://github.com/jy-yuan/KIVI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "35853f11-1f99-4b0f-9c0a-568f79b8fb17",
  "tool_use_result": {
    "query": "KIVI Tuning-Free Asymmetric 2bit Quantization KV Cache Zirui Liu ICML 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M3uY1MbTd6bfujYdXSd6ZY",
        "content": [
          {
            "title": "GitHub - jy-yuan/KIVI: [ICML 2024] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache · GitHub",
            "url": "https://github.com/jy-yuan/KIVI"
          },
          {
            "title": "[2402.02750] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache",
            "url": "https://arxiv.org/abs/2402.02750"
          },
          {
            "title": "KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache",
            "url": "https://proceedings.mlr.press/v235/liu24bz.html"
          },
          {
            "title": "[PDF] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/KIVI:-A-Tuning-Free-Asymmetric-2bit-Quantization-KV-Liu-Yuan/a3e000e0d7f64c1d094c2a8bf6f43992cbabe91b"
          },
          {
            "title": "KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache",
            "url": "https://arxiv.org/html/2402.02750v2"
          },
          {
            "title": "ICML Poster KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache",
            "url": "https://icml.cc/virtual/2024/poster/34318"
          },
          {
            "title": "KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache - Experts@Minnesota",
            "url": "https://experts.umn.edu/en/publications/kivi-a-tuning-free-asymmetric-2bit-quantization-for-kv-cache/"
          },
          {
            "title": "KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache",
            "url": "https://raw.githubusercontent.com/mlresearch/v235/main/assets/liu24bz/liu24bz.pdf"
          },
          {
            "title": "dblp: KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache.",
            "url": "https://dblp.org/rec/conf/icml/LiuYJZXBC024.html"
          },
          {
            "title": "[2402.02750v2] KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache",
            "url": "https://arxiv.org/abs/2402.02750v2"
          }
        ]
      },
      "Based on the search results, here's information about the KIVI paper:\n\n## Overview\n\nKIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache was authored by Zirui Liu, Jiayi Yuan, Hongye Jin, Shaochen Zhong, Zhaozhuo Xu, Vladimir Braverman, Beidi Chen, and Xia Hu, and was published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024).\n\n## Problem Addressed\n\nThe paper addresses the challenge that while efficiently serving large language models requires batching many requests to reduce cost per request, the key-value (KV) cache significantly increases memory demands and becomes a bottleneck in speed and memory usage, with memory demand increasing with larger batch sizes and longer context lengths.\n\n## Key Innovation\n\nThe authors conducted a comprehensive study on element distribution in KV cache of popular LLMs and found that the key cache should be quantized per-channel while the value cache should be quantized per-token, leading to the development of the tuning-free 2bit KV cache quantization algorithm named KIVI.\n\n## Performance Results\n\nKIVI's hardware-friendly design allows LLMs like Llama-2, Falcon, and Mistral to maintain comparable quality levels while reducing peak memory usage by 2.6 times, enabling up to 4 times larger batch sizes and increasing throughput by 2.35 to 3.47 times in real LLM inference workloads.\n\n## Resources\n\nThe paper is available on arXiv (2402.02750) and has an official GitHub repository at https://github.com/jy-yuan/KIVI."
    ],
    "durationSeconds": 7.7112373660000015
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T12:10:40.815Z_

<details><summary>↩ Tool result · `toolu_01TpJ9qYVnairg7sLYJdHxSb`</summary>

```text
Web search results for query: "H2O Heavy-Hitter Oracle Efficient Generative Inference LLM Zhenyu Zhang NeurIPS 2023"

Links: [{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=RkRrPp7GKO"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/6ceefa7b15572587b78ecfcebb2827f8-Paper-Conference.pdf"},{"title":"[2306.14048] H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/abs/2306.14048"},{"title":"Paper page - H_2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://huggingface.co/papers/2306.14048"},{"title":"NeurIPS Poster H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://neurips.cc/virtual/2023/poster/71645"},{"title":"H 2 O: heavy-hitter oracle for efficient generative inference ...","url":"https://dl.acm.org/doi/10.5555/3666122.3667628"},{"title":"\"H\"₂⁢\"O\": Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/html/2306.14048v1"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html"},{"title":"[NeurIPS’23] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models - Zhenyu's Blog","url":"https://allenz.work/?p=11"},{"title":"[PDF] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/H2O:-Heavy-Hitter-Oracle-for-Efficient-Generative-Zhang-Sheng/e586a4591ba0303b769f2c07cbddaf1899cb72e4"}]

Based on the search results, I found comprehensive information about the H2O paper. Here's what I found:

## H2O: Heavy-Hitter Oracle for Efficient Generative Inference

This paper was published at NeurIPS 2023, and the authors are Zhenyu Zhang, Ying Sheng, Tianyi Zhou, Tianlong Chen, Lianmin Zheng, Ruisi Cai, Zhao Song, Yuandong Tian, Christopher Ré, Clark Barrett, Zhangyang "Atlas" Wang, and Beidi Chen.

### Problem and Approach

Large Language Models (LLMs) are cost-prohibitive to deploy, particularly for long-content generation applications. A large amount of transient state information, referred to as the KV cache, is stored in GPU memory in addition to model parameters, scaling linearly with the sequence length and batch size.

The paper is based on the observation that a small portion of tokens contributes most of the value when computing attention scores.

### Key Findings

LLMs are over 95% sparse at inference time across a wide range of pre-trained LLMs. Only 5% of the KV cache is sufficient for decoding the same output token at each generation step, which suggests up to a 20× reduction in KV cache size without an accuracy drop.

### Solution

The paper proposes Heavy Hitter Oracle (H2O), a KV cache eviction policy that dynamically retains a balance of recent and H2 tokens.

### Performance Results

The implementation of H2O with 20% heavy hitters improves throughput over three leading inference systems (DeepSpeed Zero-Inference, Hugging Face Accelerate, and FlexGen) by up to 29×, 29×, and 3× on OPT-6.7B and OPT-30B models. With the same batch size, H2O can reduce latency by up to 1.9×.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "4474264c-fd94-405a-9336-91e0fadc1d34",
  "tool_use_result": {
    "query": "H2O Heavy-Hitter Oracle Efficient Generative Inference LLM Zhenyu Zhang NeurIPS 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RLu18qDJRdZwPNdxn2p4pQ",
        "content": [
          {
            "title": "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=RkRrPp7GKO"
          },
          {
            "title": "H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/6ceefa7b15572587b78ecfcebb2827f8-Paper-Conference.pdf"
          },
          {
            "title": "[2306.14048] H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models",
            "url": "https://arxiv.org/abs/2306.14048"
          },
          {
            "title": "Paper page - H_2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models",
            "url": "https://huggingface.co/papers/2306.14048"
          },
          {
            "title": "NeurIPS Poster H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models",
            "url": "https://neurips.cc/virtual/2023/poster/71645"
          },
          {
            "title": "H 2 O: heavy-hitter oracle for efficient generative inference ...",
            "url": "https://dl.acm.org/doi/10.5555/3666122.3667628"
          },
          {
            "title": "\"H\"₂⁢\"O\": Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models",
            "url": "https://arxiv.org/html/2306.14048v1"
          },
          {
            "title": "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html"
          },
          {
            "title": "[NeurIPS’23] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models - Zhenyu's Blog",
            "url": "https://allenz.work/?p=11"
          },
          {
            "title": "[PDF] H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/H2O:-Heavy-Hitter-Oracle-for-Efficient-Generative-Zhang-Sheng/e586a4591ba0303b769f2c07cbddaf1899cb72e4"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the H2O paper. Here's what I found:\n\n## H2O: Heavy-Hitter Oracle for Efficient Generative Inference\n\nThis paper was published at NeurIPS 2023, and the authors are Zhenyu Zhang, Ying Sheng, Tianyi Zhou, Tianlong Chen, Lianmin Zheng, Ruisi Cai, Zhao Song, Yuandong Tian, Christopher Ré, Clark Barrett, Zhangyang \"Atlas\" Wang, and Beidi Chen.\n\n### Problem and Approach\n\nLarge Language Models (LLMs) are cost-prohibitive to deploy, particularly for long-content generation applications. A large amount of transient state information, referred to as the KV cache, is stored in GPU memory in addition to model parameters, scaling linearly with the sequence length and batch size.\n\nThe paper is based on the observation that a small portion of tokens contributes most of the value when computing attention scores.\n\n### Key Findings\n\nLLMs are over 95% sparse at inference time across a wide range of pre-trained LLMs. Only 5% of the KV cache is sufficient for decoding the same output token at each generation step, which suggests up to a 20× reduction in KV cache size without an accuracy drop.\n\n### Solution\n\nThe paper proposes Heavy Hitter Oracle (H2O), a KV cache eviction policy that dynamically retains a balance of recent and H2 tokens.\n\n### Performance Results\n\nThe implementation of H2O with 20% heavy hitters improves throughput over three leading inference systems (DeepSpeed Zero-Inference, Hugging Face Accelerate, and FlexGen) by up to 29×, 29×, and 3× on OPT-6.7B and OPT-30B models. With the same batch size, H2O can reduce latency by up to 1.9×."
    ],
    "durationSeconds": 7.291974841999996
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T12:10:41.362Z_

<details><summary>↩ Tool result · `toolu_016YT1L4iexDrcTvcxwfX5QW`</summary>

```text
Web search results for query: "Analyzing Multi-Head Self-Attention Specialized Heads Heavy Lifting Pruned Elena Voita ACL 2019"

Links: [{"title":"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned - ACL Anthology","url":"https://aclanthology.org/P19-1580/"},{"title":"[1905.09418] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://arxiv.org/abs/1905.09418"},{"title":"GitHub - lena-voita/the-story-of-heads: This is a repository with the code for the ACL 2019 paper \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\" and the ACL 2021 paper \"Analyzing Source and Target Contributions to NMT Predictions\". · GitHub","url":"https://github.com/lena-voita/the-story-of-heads"},{"title":"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/analyzing-multi-head-self-attention-specialized-heads-do-the-heav/"},{"title":"[PDF] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Analyzing-Multi-Head-Self-Attention:-Specialized-Do-Voita-Talbot/07a64686ce8e43ac475a8d820a8a9f1d87989583"},{"title":"The Story of Heads","url":"https://lena-voita.github.io/posts/acl19_heads.html"},{"title":"lena-voita (Lena Voita) · GitHub","url":"https://github.com/lena-voita"},{"title":"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://bibbase.org/network/publication/voita-talbot-moiseev-sennrich-titov-analyzingmultiheadselfattentionspecializedheadsdotheheavyliftingtherestcanbepruned-2019"},{"title":"[1905.09418v2] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://arxiv.org/abs/1905.09418v2"},{"title":"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned | Request PDF","url":"https://www.researchgate.net/publication/335781053_Analyzing_Multi-Head_Self-Attention_Specialized_Heads_Do_the_Heavy_Lifting_the_Rest_Can_Be_Pruned"}]

I found the paper successfully! Here's what I found:

## Paper Information

The paper "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned" was published at ACL 2019 by Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, and Ivan Titov.

## Research Focus

The work evaluates the contribution made by individual attention heads to the overall performance of the model and analyzes the roles played by them in the encoder.

## Key Findings

The authors found that the most important and confident heads play consistent and often linguistically-interpretable roles. Important heads have one or more interpretable functions in the model, including attending to adjacent words and tracking specific syntactic relations.

## Pruning Method and Results

When pruning heads using a method based on stochastic gates and a differentiable relaxation of the L0 penalty, the authors observed that specialized heads are last to be pruned, and their novel pruning method removes the vast majority of heads without seriously affecting performance. For example, on the English-Russian WMT dataset, pruning 38 out of 48 encoder heads results in a drop of only 0.15 BLEU.

The paper is available on the ACL Anthology (https://aclanthology.org/P19-1580/) and on arXiv (1905.09418), with code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "cd646a7f-c76b-43dc-8ca1-86c275d12652",
  "tool_use_result": {
    "query": "Analyzing Multi-Head Self-Attention Specialized Heads Heavy Lifting Pruned Elena Voita ACL 2019",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MwmxiXP3gERVmtqE7f9HzM",
        "content": [
          {
            "title": "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned - ACL Anthology",
            "url": "https://aclanthology.org/P19-1580/"
          },
          {
            "title": "[1905.09418] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned",
            "url": "https://arxiv.org/abs/1905.09418"
          },
          {
            "title": "GitHub - lena-voita/the-story-of-heads: This is a repository with the code for the ACL 2019 paper \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\" and the ACL 2021 paper \"Analyzing Source and Target Contributions to NMT Predictions\". · GitHub",
            "url": "https://github.com/lena-voita/the-story-of-heads"
          },
          {
            "title": "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned - University of Edinburgh Research Explorer",
            "url": "https://www.research.ed.ac.uk/en/publications/analyzing-multi-head-self-attention-specialized-heads-do-the-heav/"
          },
          {
            "title": "[PDF] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Analyzing-Multi-Head-Self-Attention:-Specialized-Do-Voita-Talbot/07a64686ce8e43ac475a8d820a8a9f1d87989583"
          },
          {
            "title": "The Story of Heads",
            "url": "https://lena-voita.github.io/posts/acl19_heads.html"
          },
          {
            "title": "lena-voita (Lena Voita) · GitHub",
            "url": "https://github.com/lena-voita"
          },
          {
            "title": "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned",
            "url": "https://bibbase.org/network/publication/voita-talbot-moiseev-sennrich-titov-analyzingmultiheadselfattentionspecializedheadsdotheheavyliftingtherestcanbepruned-2019"
          },
          {
            "title": "[1905.09418v2] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned",
            "url": "https://arxiv.org/abs/1905.09418v2"
          },
          {
            "title": "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned | Request PDF",
            "url": "https://www.researchgate.net/publication/335781053_Analyzing_Multi-Head_Self-Attention_Specialized_Heads_Do_the_Heavy_Lifting_the_Rest_Can_Be_Pruned"
          }
        ]
      },
      "I found the paper successfully! Here's what I found:\n\n## Paper Information\n\nThe paper \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\" was published at ACL 2019 by Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, and Ivan Titov.\n\n## Research Focus\n\nThe work evaluates the contribution made by individual attention heads to the overall performance of the model and analyzes the roles played by them in the encoder.\n\n## Key Findings\n\nThe authors found that the most important and confident heads play consistent and often linguistically-interpretable roles. Important heads have one or more interpretable functions in the model, including attending to adjacent words and tracking specific syntactic relations.\n\n## Pruning Method and Results\n\nWhen pruning heads using a method based on stochastic gates and a differentiable relaxation of the L0 penalty, the authors observed that specialized heads are last to be pruned, and their novel pruning method removes the vast majority of heads without seriously affecting performance. For example, on the English-Russian WMT dataset, pruning 38 out of 48 encoder heads results in a drop of only 0.15 BLEU.\n\nThe paper is available on the ACL Anthology (https://aclanthology.org/P19-1580/) and on arXiv (1905.09418), with code available on GitHub."
    ],
    "durationSeconds": 6.969562448999997
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T12:10:42.653Z_

<details><summary>↩ Tool result · `toolu_01BrpSBTu1YR4Nefs8K8jvJU`</summary>

```text
Web search results for query: "ZipCache Accurate Efficient KV Cache Quantization Salient Token Yefei He NeurIPS 2024"

Links: [{"title":"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/7e57131fdeb815764434b65162c88895-Abstract-Conference.html"},{"title":"GitHub - ThisisBillhe/ZipCache: [NeurIPS 2024] The official implementation of ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification","url":"https://github.com/ThisisBillhe/ZipCache"},{"title":"NeurIPS Poster ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification","url":"https://neurips.cc/virtual/2024/poster/96563"},{"title":"[2405.14256] ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification","url":"https://arxiv.org/abs/2405.14256"},{"title":"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification | OpenReview","url":"https://openreview.net/forum?id=5t4ZAkPiJs"},{"title":"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification","url":"https://arxiv.org/html/2405.14256v1"},{"title":"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240514256H/abstract"},{"title":"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification | Yefei He","url":"http://hexy.tech/publication/he-2024-zipcache/"},{"title":"dblp: ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification.","url":"https://dblp.org/rec/journals/corr/abs-2405-14256.html"},{"title":"ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/zipcache-accurate-efficient-kv-cache-quantization-salient"}]

I found comprehensive information about ZipCache from the search results. Here's a summary:

## Overview

ZipCache is an accurate and efficient KV cache quantization method for large language models (LLMs). The paper was presented at NeurIPS 2024 as part of the Main Conference Track, with authors including Yefei He, Luoming Zhang, Weijia Wu, Jing Liu, Hong Zhou, and Bohan Zhuang.

## Problem Statement

KV cache stores key and value states from previous tokens to avoid re-computation, yet it demands substantial storage space, especially for long sequences. Adaptive KV cache compression seeks to discern the saliency of tokens, preserving vital information while aggressively compressing those of less importance. However, previous methods exhibit significant performance degradation at high compression ratios due to inaccuracies in identifying salient tokens, and the compression process introduces excessive overhead, substantially increasing memory burdens and generation latency.

## Key Technical Contributions

Through the proposed channel-separable tokenwise quantization scheme, the memory overhead of quantization parameters are substantially reduced compared to fine-grained groupwise quantization. ZipCache proposes normalized attention score as an effective metric for identifying salient tokens by considering the lower triangle characteristics of the attention matrix. An efficient approximation method decouples the saliency metric from full attention scores, enabling compatibility with fast attention implementations like FlashAttention.

## Performance Results

When evaluating Mistral-7B model on GSM8k dataset, ZipCache is capable of compressing the KV cache by 4.98x, with only a 0.38% drop in accuracy. With LLaMA3-8B model at input length 4096, ZipCache showcases a 37.3% reduction in prefill-phase latency, a 56.9% reduction in decoding-phase latency, and a 19.8% reduction in GPU memory usage.

Code is available at https://github.com/ThisisBillhe/ZipCache/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "10b0ae41-73d4-47d7-819a-2359d3a40ac5",
  "tool_use_result": {
    "query": "ZipCache Accurate Efficient KV Cache Quantization Salient Token Yefei He NeurIPS 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_015iSK62ueJVf73TA8ZvAnVB",
        "content": [
          {
            "title": "ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/hash/7e57131fdeb815764434b65162c88895-Abstract-Conference.html"
          },
          {
            "title": "GitHub - ThisisBillhe/ZipCache: [NeurIPS 2024] The official implementation of ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification",
            "url": "https://github.com/ThisisBillhe/ZipCache"
          },
          {
            "title": "NeurIPS Poster ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification",
            "url": "https://neurips.cc/virtual/2024/poster/96563"
          },
          {
            "title": "[2405.14256] ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification",
            "url": "https://arxiv.org/abs/2405.14256"
          },
          {
            "title": "ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification | OpenReview",
            "url": "https://openreview.net/forum?id=5t4ZAkPiJs"
          },
          {
            "title": "ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification",
            "url": "https://arxiv.org/html/2405.14256v1"
          },
          {
            "title": "ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240514256H/abstract"
          },
          {
            "title": "ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification | Yefei He",
            "url": "http://hexy.tech/publication/he-2024-zipcache/"
          },
          {
            "title": "dblp: ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification.",
            "url": "https://dblp.org/rec/journals/corr/abs-2405-14256.html"
          },
          {
            "title": "ZipCache: Accurate and Efficient KV Cache Quantization with Salient Token Identification | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/zipcache-accurate-efficient-kv-cache-quantization-salient"
          }
        ]
      },
      "I found comprehensive information about ZipCache from the search results. Here's a summary:\n\n## Overview\n\nZipCache is an accurate and efficient KV cache quantization method for large language models (LLMs). The paper was presented at NeurIPS 2024 as part of the Main Conference Track, with authors including Yefei He, Luoming Zhang, Weijia Wu, Jing Liu, Hong Zhou, and Bohan Zhuang.\n\n## Problem Statement\n\nKV cache stores key and value states from previous tokens to avoid re-computation, yet it demands substantial storage space, especially for long sequences. Adaptive KV cache compression seeks to discern the saliency of tokens, preserving vital information while aggressively compressing those of less importance. However, previous methods exhibit significant performance degradation at high compression ratios due to inaccuracies in identifying salient tokens, and the compression process introduces excessive overhead, substantially increasing memory burdens and generation latency.\n\n## Key Technical Contributions\n\nThrough the proposed channel-separable tokenwise quantization scheme, the memory overhead of quantization parameters are substantially reduced compared to fine-grained groupwise quantization. ZipCache proposes normalized attention score as an effective metric for identifying salient tokens by considering the lower triangle characteristics of the attention matrix. An efficient approximation method decouples the saliency metric from full attention scores, enabling compatibility with fast attention implementations like FlashAttention.\n\n## Performance Results\n\nWhen evaluating Mistral-7B model on GSM8k dataset, ZipCache is capable of compressing the KV cache by 4.98x, with only a 0.38% drop in accuracy. With LLaMA3-8B model at input length 4096, ZipCache showcases a 37.3% reduction in prefill-phase latency, a 56.9% reduction in decoding-phase latency, and a 19.8% reduction in GPU memory usage.\n\nCode is available at https://github.com/ThisisBillhe/ZipCache/."
    ],
    "durationSeconds": 7.758908637
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T12:10:43.054Z_

<details><summary>↩ Tool result · `toolu_01SFUQor16PS3eTvj2Vhst82`</summary>

```text
Web search results for query: "RateQuant Optimal Mixed-Precision KV Cache Quantization Rate-Distortion Theory Fei Zuo arXiv 2026"

Links: [{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/abs/2605.06675"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/new"},{"title":"TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate","url":"https://arxiv.org/html/2504.19874v1"},{"title":"More Tokens, Lower Precision: Towards the Optimal Token-Precision Trade-off in KV Cache Compression","url":"https://arxiv.org/html/2412.12706v1"},{"title":"KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference","url":"https://arxiv.org/html/2502.04420"},{"title":"Quantization Dominates Rank Reduction for KV-Cache Compression","url":"https://arxiv.org/html/2604.11501"},{"title":"HeadQ: Model-Visible Distortion and a Prototype KV Quantizer-Corrector Codec","url":"https://arxiv.org/html/2605.03562"},{"title":"KITTY: ACCURATE AND EFFICIENT 2-BIT KV CACHE QUANTIZATION WITH","url":"https://www.arxiv.org/pdf/2511.18643"},{"title":"FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression","url":"https://arxiv.org/html/2605.11478"}]

Based on the search results, I found the paper you were looking for. Here's what I found about RateQuant:

## RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory

RateQuant was developed by Fei Zuo, Zikang Zhou, Hao Cong, Xiaoyan Xi, and Ho Fai Leung from BA TechWorks (BMW Group), National University of Singapore, and Tsinghua University.

### Key Problem Addressed

Large language models cache key-value (KV) pairs during generation, and this KV cache grows linearly with sequence length, making it a memory bottleneck for serving. While quantizing the KV cache reduces this cost, current quantizers assign the same bit-width to every attention head, ignoring the large variation in head importance.

### Main Innovation

RateQuant addresses a failure mode called "distortion model mismatch" and solves it by fitting a per-quantizer distortion model from a small calibration set, then solving the resulting bit-allocation problem in closed form via reverse waterfilling from rate-distortion theory.

### Results

On Qwen3-8B at 2.5 average bits, calibrated RateQuant reduces KIVI's perplexity from 49.3 to 14.9 (70% reduction) and improves QuaRot by 6.6 PPL. The entire calibration takes 1.6 s on a single GPU and adds zero overhead at inference time.

The paper was posted to arXiv on April 22, 2026 (arXiv ID: 2605.06675).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "d47edd7b-87b5-42f1-993e-eda34c14e609",
  "tool_use_result": {
    "query": "RateQuant Optimal Mixed-Precision KV Cache Quantization Rate-Distortion Theory Fei Zuo arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HARVVnHUgWeU1dDvBw5dXq",
        "content": [
          {
            "title": "RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory",
            "url": "https://arxiv.org/html/2605.06675"
          },
          {
            "title": "[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory",
            "url": "https://arxiv.org/abs/2605.06675"
          },
          {
            "title": "Machine Learning",
            "url": "https://arxiv.org/list/cs.LG/new"
          },
          {
            "title": "TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate",
            "url": "https://arxiv.org/html/2504.19874v1"
          },
          {
            "title": "More Tokens, Lower Precision: Towards the Optimal Token-Precision Trade-off in KV Cache Compression",
            "url": "https://arxiv.org/html/2412.12706v1"
          },
          {
            "title": "KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference",
            "url": "https://arxiv.org/html/2502.04420"
          },
          {
            "title": "Quantization Dominates Rank Reduction for KV-Cache Compression",
            "url": "https://arxiv.org/html/2604.11501"
          },
          {
            "title": "HeadQ: Model-Visible Distortion and a Prototype KV Quantizer-Corrector Codec",
            "url": "https://arxiv.org/html/2605.03562"
          },
          {
            "title": "KITTY: ACCURATE AND EFFICIENT 2-BIT KV CACHE QUANTIZATION WITH",
            "url": "https://www.arxiv.org/pdf/2511.18643"
          },
          {
            "title": "FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression",
            "url": "https://arxiv.org/html/2605.11478"
          }
        ]
      },
      "Based on the search results, I found the paper you were looking for. Here's what I found about RateQuant:\n\n## RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory\n\nRateQuant was developed by Fei Zuo, Zikang Zhou, Hao Cong, Xiaoyan Xi, and Ho Fai Leung from BA TechWorks (BMW Group), National University of Singapore, and Tsinghua University.\n\n### Key Problem Addressed\n\nLarge language models cache key-value (KV) pairs during generation, and this KV cache grows linearly with sequence length, making it a memory bottleneck for serving. While quantizing the KV cache reduces this cost, current quantizers assign the same bit-width to every attention head, ignoring the large variation in head importance.\n\n### Main Innovation\n\nRateQuant addresses a failure mode called \"distortion model mismatch\" and solves it by fitting a per-quantizer distortion model from a small calibration set, then solving the resulting bit-allocation problem in closed form via reverse waterfilling from rate-distortion theory.\n\n### Results\n\nOn Qwen3-8B at 2.5 average bits, calibrated RateQuant reduces KIVI's perplexity from 49.3 to 14.9 (70% reduction) and improves QuaRot by 6.6 PPL. The entire calibration takes 1.6 s on a single GPU and adds zero overhead at inference time.\n\nThe paper was posted to arXiv on April 22, 2026 (arXiv ID: 2605.06675)."
    ],
    "durationSeconds": 7.602417674000004
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
All 5 searched papers are verified as real. Now let me compile the analysis:

**Bib keys (19 total):**
1. liu2024kivi
2. hooper2024kvquant
3. lin2024qserve
4. he2024zipcache
5. kang2024gear
6. duanmu2024skvq
7. zhang2023h2o
8. li2024snapkv
9. ge2024fastgen
10. xiao2024streamingllm
11. liu2024scissorhands
12. yang2024pyramidinfer


13. zuo2026ratequant
14. lei2026arkv
15. li2025kvmix
16. zhang2025mixkvq
17. kim2024squeezellm
18. voita2019analyzing
19. michel2019sixteen

All 19 bibliography entries are properly cited in the .tex files with no orphans, missing entries, or duplicates, and each one includes the required metadata fields.

I'm noticing a couple of key-year mismatches: `lin2024qserve` is labeled as 2024 but the year field shows 2025 for MLSys 2025, and `liu2024scissorhands` says 2024 in the key but 2023 in the year field for NeurIPS 2023. The year range across all entries spans 2019 to 2026, which is reasonable given the current date, with the 2026 entries being acceptable as preprints. I've verified the first entry so far—liu2024kivi checks out as ICML 2024 with matching authors and title.

I've now verified all five entries: zhang2023h2o and voita2019analyzing both match their respective venues and arXiv identifiers, he2024zipcache is confirmed as NeurIPS 2024, and zuo2026ratequant matches the arXiv preprint with the correct author list.

For RateQuant specifically, there's a minor inconsistency between the search result's date of April 22, 2026 and the arXiv ID format 2605.xxxxx which indicates May 2026, but the year 2026 in the bibliography is correct and the paper is verified.

Now I'm checking QServe and finding a naming issue—the key says "lin2024qserve" but the paper was published at MLSys 2025, so the year field is correct even though the arXiv preprint is from May 2024. The key should probably reflect the venue year. Similarly, ScissorHands has a mismatch where the key says "liu2024scissorhands" but the paper is from NeurIPS 2023 with an arXiv date of May 2023, so the key naming is definitely wrong here.

Now I'm generating the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "0e97e1f7-282a-49de-bfc5-20d963b889da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012krKHYBuAZNmcJgvuRPZe1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5767,
      "cache_read_input_tokens": 44476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5767
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

_source line 43_

分析完毕，生成报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "811c0016-5f7c-4247-ae45-60329251e8a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012krKHYBuAZNmcJgvuRPZe1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5767,
      "cache_read_input_tokens": 44476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5767
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

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_016wtyVKtkwvdDkGg13CUZZA`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "2f701db3-f8e2-4296-b346-a222e94bf682",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012krKHYBuAZNmcJgvuRPZe1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5767,
      "cache_read_input_tokens": 44476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5767
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

_source line 45 · 2026-05-14T12:11:10.401Z_

<details><summary>↩ Tool result · `toolu_016wtyVKtkwvdDkGg13CUZZA`</summary>

```text
_project
budget_sweep
c4_cross_dataset_eval
compounding_sweep
compounding_sweep_k10_12
dream_reports
figures
full_bitwidth_profiler.py
generate_figures.py
greedy_cardinality_ablation
head_sensitivity_viz
hires_mckp_reeval
hires_reeval
llama_k_ablation
manifest.yaml
mistral_heuristic_k4
mistral_k_ablation
multi_seed_lowres
plan_011
qwen_bf16_reeval
ratequant_greedy_comparison
run_bf16_reeval.py
run_full_bitwidth.py
run_l0_heuristic_corrected.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "336f6577-fde2-4144-9db9-97ab4a1e970f",
  "tool_use_result": {
    "stdout": "_project\nbudget_sweep\nc4_cross_dataset_eval\ncompounding_sweep\ncompounding_sweep_k10_12\ndream_reports\nfigures\nfull_bitwidth_profiler.py\ngenerate_figures.py\ngreedy_cardinality_ablation\nhead_sensitivity_viz\nhires_mckp_reeval\nhires_reeval\nllama_k_ablation\nmanifest.yaml\nmistral_heuristic_k4\nmistral_k_ablation\nmulti_seed_lowres\nplan_011\nqwen_bf16_reeval\nratequant_greedy_comparison\nrun_bf16_reeval.py\nrun_full_bitwidth.py\nrun_l0_heuristic_corrected.py",
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

_source line 46_

<details open><summary>🔧 Tool call — Write · `toolu_013ZGug4EonkLcnuhU7VBmBM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/reference_audit_report.md",
  "content": "# Reference Audit Report\n\n**Project:** ratekv  \n**Date:** 2026-05-14  \n**Scope:** `docs/paper/references.bib` + all `.tex` files in `docs/paper/`\n\n---\n\n## 统计摘要\n\n| 指标 | 数值 |\n|------|------|\n| .bib 总条目数 | 19 |\n| .tex 中引用的唯一 key 数 | 19 |\n| 孤立引用（.bib 有，.tex 未引用） | 0 |\n| 缺失引用（.tex 引用，.bib 无） | 0 |\n| 疑似重复条目 | 0 |\n| 格式不完整条目 | 0 |\n\n**结论：引用集合完全一致，无孤立或缺失条目。**\n\n---\n\n## 问题清单（按严重性排序）\n\n### 中等：Bib key 与 year 字段不一致（2 处）\n\n| Bib Key | Key 中隐含年份 | year 字段 | 实际 venue | 建议 |\n|---------|---------------|-----------|------------|------|\n| `lin2024qserve` | 2024 | 2025 | MLSys 2025 | 改 key 为 `lin2025qserve`，或保持 key 不变但知悉不一致 |\n| `liu2024scissorhands` | 2024 | 2023 | NeurIPS 2023 | 改 key 为 `liu2023scissorhands`，或保持 key 不变但知悉不一致 |\n\n说明：key 中的年份仅为命名约定，不影响编译或显示，但可能造成维护混淆。修改 key 需同步更新所有 .tex 文件中的 `\\cite{}` 引用。\n\n### 低：entry type 与 venue 不完全匹配（2 处）\n\n| Bib Key | 当前 type | 实际情况 | 说明 |\n|---------|-----------|---------|------|\n| `kang2024gear` | `@misc` | arXiv preprint（但已被接受到某 venue） | 如已正式发表，建议更新为 `@inproceedings` 并补充 venue |\n| `duanmu2024skvq` | `@misc` | arXiv preprint | 如仍为 preprint 则无问题 |\n\n---\n\n## 格式一致性检查\n\n所有 19 条 .bib 条目均包含以下必需字段：\n\n- `title` ✅\n- `author` ✅\n- `year` ✅\n- `booktitle`（对 `@inproceedings`）或 `note`（对 `@misc`）✅\n\n附加观察：\n- 所有 `@inproceedings` 条目的 `booktitle` 使用简写格式（如 \"ICML 2024\" 而非完整名称），风格一致。\n- 所有 `@misc` 条目含 `url`、`eprint`、`archivePrefix` 字段，格式统一。\n- 所有条目含 `url` 字段。\n\n---\n\n## 年份合理性检查\n\n| 年份范围 | 条目数 | 判定 |\n|---------|--------|------|\n| 2019 | 2 | ✅ 合理（经典 attention head 分析论文） |\n| 2023 | 2 | ✅ 合理 |\n| 2024 | 9 | ✅ 合理 |\n| 2025 | 3 | ✅ 合理 |\n| 2026 | 3 | ✅ 合理（当前年份，均为 arXiv preprint 或本文自身） |\n\n无异常年份（无未来日期、无明显 typo）。\n\n---\n\n## 真实性抽查结果（5/19）\n\n随机抽取 5 篇，通过 Web 搜索验证 title、author、year、venue：\n\n| Bib Key | Title 匹配 | Author 匹配 | Year/Venue 匹配 | 判定 |\n|---------|-----------|-------------|----------------|------|\n| `liu2024kivi` | ✅ | ✅ | ✅ ICML 2024, arXiv 2402.02750 | **真实** |\n| `zhang2023h2o` | ✅ | ✅ | ✅ NeurIPS 2023, arXiv 2306.14048 | **真实** |\n| `voita2019analyzing` | ✅ | ✅ | ✅ ACL 2019, arXiv 1905.09418 | **真实** |\n| `he2024zipcache` | ✅ | ✅ | ✅ NeurIPS 2024, arXiv 2405.14256 | **真实** |\n| `zuo2026ratequant` | ✅ | ✅ | ✅ arXiv 2605.06675 (May 2026) | **真实** |\n\n**5/5 抽查条目均为真实论文，无 LLM 幻觉引用。**\n\n---\n\n## 引用分布\n\n| .tex 文件 | 引用数 |\n|-----------|--------|\n| introduction.tex | 9 |\n| related_work.tex | 17（覆盖全部 19 条中的 17 条） |\n| method.tex | 1 |\n| experiments.tex | 1 |\n| abstract.tex | 0 |\n| analysis.tex | 0 |\n| conclusion.tex | 0 |\n| main.tex | 0 |\n\n---\n\n## 建议修复\n\n1. **（可选）** 统一 bib key 命名中的年份：将 `lin2024qserve` → `lin2025qserve`，`liu2024scissorhands` → `liu2023scissorhands`，并同步更新所有 .tex 中的 `\\cite{}` 调用。这是命名规范问题，不影响编译。\n\n2. **（可选）** 检查 `kang2024gear` (GEAR) 是否已被正式会议/期刊接收，如是则更新 entry type 和 venue 信息。\n\n---\n\n## 总结\n\n引用系统整体健康。19 条 bib 条目与 .tex 引用完全对应，无孤立、无缺失、无重复、无虚假引用。仅有 2 处 key 命名与 year 字段的轻微不一致，不影响论文编译和引用显示。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "c03a9871-687b-4f19-9017-27cf3b14b9ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rdw5PNnb5QcZ6nJ1d3xMHs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 50243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1457
      },
      "output_tokens": 61,
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

_source line 47 · 2026-05-14T12:11:41.629Z_

<details><summary>↩ Tool result · `toolu_013ZGug4EonkLcnuhU7VBmBM`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/reference_audit_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "8dc2034d-bb25-4e8d-95c1-1d5123066cbf",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/reference_audit_report.md",
    "content": "# Reference Audit Report\n\n**Project:** ratekv  \n**Date:** 2026-05-14  \n**Scope:** `docs/paper/references.bib` + all `.tex` files in `docs/paper/`\n\n---\n\n## 统计摘要\n\n| 指标 | 数值 |\n|------|------|\n| .bib 总条目数 | 19 |\n| .tex 中引用的唯一 key 数 | 19 |\n| 孤立引用（.bib 有，.tex 未引用） | 0 |\n| 缺失引用（.tex 引用，.bib 无） | 0 |\n| 疑似重复条目 | 0 |\n| 格式不完整条目 | 0 |\n\n**结论：引用集合完全一致，无孤立或缺失条目。**\n\n---\n\n## 问题清单（按严重性排序）\n\n### 中等：Bib key 与 year 字段不一致（2 处）\n\n| Bib Key | Key 中隐含年份 | year 字段 | 实际 venue | 建议 |\n|---------|---------------|-----------|------------|------|\n| `lin2024qserve` | 2024 | 2025 | MLSys 2025 | 改 key 为 `lin2025qserve`，或保持 key 不变但知悉不一致 |\n| `liu2024scissorhands` | 2024 | 2023 | NeurIPS 2023 | 改 key 为 `liu2023scissorhands`，或保持 key 不变但知悉不一致 |\n\n说明：key 中的年份仅为命名约定，不影响编译或显示，但可能造成维护混淆。修改 key 需同步更新所有 .tex 文件中的 `\\cite{}` 引用。\n\n### 低：entry type 与 venue 不完全匹配（2 处）\n\n| Bib Key | 当前 type | 实际情况 | 说明 |\n|---------|-----------|---------|------|\n| `kang2024gear` | `@misc` | arXiv preprint（但已被接受到某 venue） | 如已正式发表，建议更新为 `@inproceedings` 并补充 venue |\n| `duanmu2024skvq` | `@misc` | arXiv preprint | 如仍为 preprint 则无问题 |\n\n---\n\n## 格式一致性检查\n\n所有 19 条 .bib 条目均包含以下必需字段：\n\n- `title` ✅\n- `author` ✅\n- `year` ✅\n- `booktitle`（对 `@inproceedings`）或 `note`（对 `@misc`）✅\n\n附加观察：\n- 所有 `@inproceedings` 条目的 `booktitle` 使用简写格式（如 \"ICML 2024\" 而非完整名称），风格一致。\n- 所有 `@misc` 条目含 `url`、`eprint`、`archivePrefix` 字段，格式统一。\n- 所有条目含 `url` 字段。\n\n---\n\n## 年份合理性检查\n\n| 年份范围 | 条目数 | 判定 |\n|---------|--------|------|\n| 2019 | 2 | ✅ 合理（经典 attention head 分析论文） |\n| 2023 | 2 | ✅ 合理 |\n| 2024 | 9 | ✅ 合理 |\n| 2025 | 3 | ✅ 合理 |\n| 2026 | 3 | ✅ 合理（当前年份，均为 arXiv preprint 或本文自身） |\n\n无异常年份（无未来日期、无明显 typo）。\n\n---\n\n## 真实性抽查结果（5/19）\n\n随机抽取 5 篇，通过 Web 搜索验证 title、author、year、venue：\n\n| Bib Key | Title 匹配 | Author 匹配 | Year/Venue 匹配 | 判定 |\n|---------|-----------|-------------|----------------|------|\n| `liu2024kivi` | ✅ | ✅ | ✅ ICML 2024, arXiv 2402.02750 | **真实** |\n| `zhang2023h2o` | ✅ | ✅ | ✅ NeurIPS 2023, arXiv 2306.14048 | **真实** |\n| `voita2019analyzing` | ✅ | ✅ | ✅ ACL 2019, arXiv 1905.09418 | **真实** |\n| `he2024zipcache` | ✅ | ✅ | ✅ NeurIPS 2024, arXiv 2405.14256 | **真实** |\n| `zuo2026ratequant` | ✅ | ✅ | ✅ arXiv 2605.06675 (May 2026) | **真实** |\n\n**5/5 抽查条目均为真实论文，无 LLM 幻觉引用。**\n\n---\n\n## 引用分布\n\n| .tex 文件 | 引用数 |\n|-----------|--------|\n| introduction.tex | 9 |\n| related_work.tex | 17（覆盖全部 19 条中的 17 条） |\n| method.tex | 1 |\n| experiments.tex | 1 |\n| abstract.tex | 0 |\n| analysis.tex | 0 |\n| conclusion.tex | 0 |\n| main.tex | 0 |\n\n---\n\n## 建议修复\n\n1. **（可选）** 统一 bib key 命名中的年份：将 `lin2024qserve` → `lin2025qserve`，`liu2024scissorhands` → `liu2023scissorhands`，并同步更新所有 .tex 中的 `\\cite{}` 调用。这是命名规范问题，不影响编译。\n\n2. **（可选）** 检查 `kang2024gear` (GEAR) 是否已被正式会议/期刊接收，如是则更新 entry type 和 venue 信息。\n\n---\n\n## 总结\n\n引用系统整体健康。19 条 bib 条目与 .tex 引用完全对应，无孤立、无缺失、无重复、无虚假引用。仅有 2 处 key 命名与 year 字段的轻微不一致，不影响论文编译和引用显示。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 48_

审计完成。报告已写入 `artifacts/reference_audit_report.md`。

核心结论：
- **19 条 bib 条目与 .tex 引用完全一致**，无孤立、无缺失、无重复
- **5 篇抽查全部真实**，无幻觉引用
- 发现 **2 处轻微问题**：`lin2024qserve` 的 key 隐含 2024 但实际 venue 是 MLSys 2025；`liu2024scissorhands` 的 key 隐含 2024 但实际是 NeurIPS 2023。这是命名规范不一致，不影响编译

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "uuid": "e7882d91-82f6-4e6e-b810-efd6710a61a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPApmnqVNjat2UUqYsc6Yd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2090,
      "cache_read_input_tokens": 51700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2090
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

_source line 49_

审计完成。报告已写入 `artifacts/reference_audit_report.md`。

核心结论：
- **19 条 bib 条目与 .tex 引用完全一致**，无孤立、无缺失、无重复
- **5 篇抽查全部真实**，无幻觉引用
- 发现 **2 处轻微问题**：`lin2024qserve` 的 key 隐含 2024 但实际 venue 是 MLSys 2025；`liu2024scissorhands` 的 key 隐含 2024 但实际是 NeurIPS 2023。这是命名规范不一致，不影响编译

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 123319,
  "duration_api_ms": 153968,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "893754e9-f89a-4e91-a863-ff652a2b656d",
  "total_cost_usd": 0.71099975,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 41949,
    "cache_read_input_tokens": 250159,
    "output_tokens": 6847,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41949,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 194,
        "cache_read_input_tokens": 51700,
        "cache_creation_input_tokens": 2090,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2090
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 87859,
      "outputTokens": 2930,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 5,
      "costUSD": 0.152509,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 6847,
      "cacheReadInputTokens": 250159,
      "cacheCreationInputTokens": 41949,
      "webSearchRequests": 0,
      "costUSD": 0.5584907499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9f5f67b5-02b9-4993-a715-753234ae223a"
}
```

</details>

---
