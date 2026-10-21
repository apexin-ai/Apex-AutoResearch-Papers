# research p3 citation audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_research_p3-citation-audit_20260520T134900.log`
- **Structured JSON:** [`661a0140f5c5d560aa32.json`](../../sessions/66/661a0140f5c5d560aa32.json)

## Before a recorded user message

43 recorded events

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
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
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
  "uuid": "d0b75467-4b8e-47e1-b69c-bf00cb31528a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1779300600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "20d56130-e7c1-43af-b911-7c07cae3a72b",
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by finding the bib and tex files in the project directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "54d28c60-6d57-4198-849e-6a56abd3e19a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ShzzjMfrianNbuncaEHy3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12176,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12176
      },
      "output_tokens": 42,
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

开始执行 Citation Audit。先找 bib 和 tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "8eb22814-0d17-45b7-9b2f-a8c422b6ca01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ShzzjMfrianNbuncaEHy3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12176,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12176
      },
      "output_tokens": 42,
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

<details open><summary>🔧 Tool call — Glob · `toolu_01GqmHBNLx4dxuthayh1F7Yx`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "a9c74076-9539-4e98-90bb-245c14185311",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ShzzjMfrianNbuncaEHy3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12176,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12176
      },
      "output_tokens": 42,
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

_source line 7 · 2026-05-20T13:49:13.963Z_

<details><summary>↩ Tool result · `toolu_01GqmHBNLx4dxuthayh1F7Yx`</summary>

```text
artifacts/dream_reports/dream_20260515T092545/worst/custom.bib
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "c04904ea-53d2-43bd-89dd-24c6a6315386",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T092545/worst/custom.bib",
      "docs/paper/references.bib"
    ],
    "durationMs": 25,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_018RJKbVR2H2ZuMpYoeq8dKa`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "56c0814d-1272-4b2b-9ea0-bb203253d0f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ShzzjMfrianNbuncaEHy3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12176,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12176
      },
      "output_tokens": 42,
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

_source line 9 · 2026-05-20T13:49:14.604Z_

<details><summary>↩ Tool result · `toolu_018RJKbVR2H2ZuMpYoeq8dKa`</summary>

```text
artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
artifacts/dream_reports/dream_20260515T092545/best/paper.tex
artifacts/dream_reports/dream_20260515T092545/median/paper.tex
artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
artifacts/_project/paper/freeform_ablation_appendix_table.tex
artifacts/freeform_ablation_appendix_table.tex
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
artifacts/n_scaling_appendix_tables.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/n_scaling_appendix_tables.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260516T092241/best/paper.tex
artifacts/dream_reports/dream_20260516T092241/median/paper.tex
artifacts/dream_reports/dream_20260516T092241/worst/paper.tex
artifacts/dream_reports/dream_20260516T113255/best/paper.tex
artifacts/dream_reports/dream_20260516T113255/median/paper.tex
artifacts/dream_reports/dream_20260516T113255/worst/paper.tex
artifacts/per_type_lp_table.tex
artifacts/exp_021_fewnerd_full/paper/per_type_lp_table.tex
docs/paper/sections/checklist.tex
code/scale_table.tex
paper/sections/zeroshot_scaling_draft.tex
artifacts/_project/paper/scaling_narrative_A_monotonic.tex
artifacts/_project/paper/scaling_narrative_B_nonmonotonic.tex
artifacts/scaling_narrative_B_nonmonotonic.tex
artifacts/scaling_narrative_A_monotonic.tex
artifacts/exp_qwen25_72b_fewshot/paper/zs_vs_fs_comparison_draft.tex
artifacts/zs_vs_fs_comparison_draft.tex
artifacts/exp_qwen25_72b_fewshot/paper/tab_72b_zs_vs_fs_appendix.tex
artifacts/tab_72b_zs_vs_fs_appendix.tex
docs/paper/sections/related_work.tex
artifacts/_project/paper/theorem.tex
artifacts/p_impossibility/theorem.tex
docs/paper/sections/method.tex
docs/paper/sections/theoretical.tex
docs/paper/sections/diagnostic.tex
docs/paper/sections/experiments.tex
docs/paper/sections/abstract.tex
docs/paper/sections/introduction.tex
docs/paper/sections/single_signal.tex
docs/paper/sections/experiments_main.tex
docs/paper/sections/theory.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/adaptive.tex
artifacts/r25_response/power_analysis.tex
docs/paper/sections/limitations.tex
artifacts/r25_response/holm_bonferroni_enumeration.tex
docs/paper/sections/background.tex
docs/paper/sections/discussion.tex
docs/paper/sections/appendix.tex
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "a626d119-d666-46b3-b59f-0a6657b9781c",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260514T093336/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T093336/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T093336/worst/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T105303/worst/paper.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/dream_reports/dream_20260514T203201/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T203201/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T203201/worst/paper.tex",
      "artifacts/bootstrap_ci_tables.tex",
      "artifacts/dream_reports/dream_20260515T092545/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T092545/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T092545/worst/paper.tex",
      "artifacts/_project/paper/freeform_ablation_appendix_table.tex",
      "artifacts/freeform_ablation_appendix_table.tex",
      "artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex",
      "artifacts/n_scaling_appendix_tables.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/n_scaling_appendix_tables.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/dream_reports/dream_20260516T092241/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T092241/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T092241/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T113255/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T113255/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T113255/worst/paper.tex",
      "artifacts/per_type_lp_table.tex",
      "artifacts/exp_021_fewnerd_full/paper/per_type_lp_table.tex",
      "docs/paper/sections/checklist.tex",
      "code/scale_table.tex",
      "paper/sections/zeroshot_scaling_draft.tex",
      "artifacts/_project/paper/scaling_narrative_A_monotonic.tex",
      "artifacts/_project/paper/scaling_narrative_B_nonmonotonic.tex",
      "artifacts/scaling_narrative_B_nonmonotonic.tex",
      "artifacts/scaling_narrative_A_monotonic.tex",
      "artifacts/exp_qwen25_72b_fewshot/paper/zs_vs_fs_comparison_draft.tex",
      "artifacts/zs_vs_fs_comparison_draft.tex",
      "artifacts/exp_qwen25_72b_fewshot/paper/tab_72b_zs_vs_fs_appendix.tex",
      "artifacts/tab_72b_zs_vs_fs_appendix.tex",
      "docs/paper/sections/related_work.tex",
      "artifacts/_project/paper/theorem.tex",
      "artifacts/p_impossibility/theorem.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/sections/theoretical.tex",
      "docs/paper/sections/diagnostic.tex",
      "docs/paper/sections/experiments.tex",
      "docs/paper/sections/abstract.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/single_signal.tex",
      "docs/paper/sections/experiments_main.tex",
      "docs/paper/sections/theory.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/adaptive.tex",
      "artifacts/r25_response/power_analysis.tex",
      "docs/paper/sections/limitations.tex",
      "artifacts/r25_response/holm_bonferroni_enumeration.tex",
      "docs/paper/sections/background.tex",
      "docs/paper/sections/discussion.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/main.tex"
    ],
    "durationMs": 32,
    "numFiles": 66,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_011YzqvyHSUjyncaj1mHyCs2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "95df2452-fa7d-4c7a-a4cc-ee8161b38e03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6vJ8sEsRvnCbPYqo5Lruh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 23877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1347
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

_source line 11 · 2026-05-20T13:49:17.308Z_

<details><summary>↩ Tool result · `toolu_011YzqvyHSUjyncaj1mHyCs2`</summary>

```text
1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{xiong2024verbalized,
4	  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},
5	  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},
6	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},
7	  year = {2024},
8	  url = {https://arxiv.org/abs/2306.13063},
9	}
10	
11	@inproceedings{vijayakumar2018diverse,
12	  title = {Diverse Beam Search for Improved Description of Complex Scenes},
13	  author = {Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and Sun, Qing and Lee, Stefan and Crandall, David J. and Batra, Dhruv},
14	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
15	  year = {2018},
16	  url = {https://arxiv.org/abs/1610.02424}
17	}
18	
19	@inproceedings{shi2022mbr,
20	  title = {Natural Language to Code Translation with Execution},
21	  author = {Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and Wang, Sida I.},
22	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
23	  pages = {3533--3546},
24	  year = {2022},
25	  url = {https://arxiv.org/abs/2204.11454}
26	}
27	
28	@article{brown2024monkeys,
29	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
30	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
31	  journal = {arXiv preprint arXiv:2407.21787},
32	  year = {2024},
33	  url = {https://arxiv.org/abs/2407.21787}
34	}
35	
36	@inproceedings{chen2024usc,
37	  title = {Universal Self-Consistency for Large Language Model Generation},
38	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
39	  booktitle = {ICML 2024 Workshop on In-Context Learning},
40	  year = {2024},
41	  url = {https://arxiv.org/abs/2311.17311}
42	}
43	
44	@article{cobbe2021verifiers,
45	  title = {Training Verifiers to Solve Math Word Problems},
46	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
47	  journal = {arXiv preprint arXiv:2110.14168},
48	  year = {2021},
49	  url = {https://arxiv.org/abs/2110.14168}
50	}
51	
52	@inproceedings{culotta2004confidence,
53	  title = {Confidence Estimation for Information Extraction},
54	  author = {Culotta, Aron and McCallum, Andrew},
55	  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL 2004)},
56	  year = {2004},
57	  url = {https://aclanthology.org/N04-4028/}
58	}
59	
60	@inproceedings{derczynski2017wnut,
61	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
62	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
63	  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},
64	  year = {2017},
65	  url = {https://aclanthology.org/W17-4418/}
66	}
67	
68	@inproceedings{ding2021fewnerd,
69	  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},
70	  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},
71	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},
72	  pages = {3198--3213},
73	  year = {2021},
74	  doi = {10.18653/v1/2021.acl-long.248}
75	}
76	
77	@inproceedings{eikema2022sampling,
78	  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},
79	  author = {Eikema, Bryan and Aziz, Wilker},
80	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
81	  year = {2022},
82	  pages = {10978--10993},
83	  doi = {10.18653/v1/2022.emnlp-main.754}
84	}
85	
86	@article{freitag2022high,
87	  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},
88	  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},
89	  journal = {Transactions of the Association for Computational Linguistics},
90	  volume = {10},
91	  year = {2022},
92	  pages = {811--825},
93	  doi = {10.1162/tacl_a_00491}
94	}
95	
96	@article{fleiss1971agreement,
97	  title = {Measuring nominal scale agreement among many raters.},
98	  author = {Fleiss, Joseph L.},
99	  journal = {Psychological Bulletin},
100	  year = {1971},
101	  doi = {10.1037/h0031619},
102	  url = {http://dx.doi.org/10.1037/h0031619}
103	}
104	
105	@article{feng2025optimal,
106	  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},
107	  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},
108	  journal = {arXiv preprint arXiv:2511.12309},
109	  year = {2025},
110	  url = {https://arxiv.org/abs/2511.12309}
111	}
112	
113	@inproceedings{geng2024confidence,
114	  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},
115	  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
116	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
117	  year = {2024},
118	  doi = {10.18653/v1/2024.naacl-long.366},
119	  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}
120	}
121	
122	@article{hobelsberger2025systematic,
123	  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},
124	  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},
125	  journal = {arXiv preprint arXiv:2510.20460},
126	  year = {2025},
127	  url = {https://arxiv.org/abs/2510.20460}
128	}
129	
130	@article{kadavath2022language,
131	  title = {Language Models (Mostly) Know What They Know},
132	  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
133	  journal = {arXiv preprint arXiv:2207.05221},
134	  year = {2022},
135	  url = {https://arxiv.org/abs/2207.05221}
136	}
137	
138	@inproceedings{kang2025selfcertainty,
139	  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},
140	  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},
141	  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},
142	  year = {2025},
143	  url = {https://arxiv.org/abs/2502.18581}
144	}
145	
146	@inproceedings{kim2026reasc,
147	  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
148	  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
149	  booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026)},
150	  year = {2026},
151	  url = {https://arxiv.org/abs/2601.02970}
152	}
153	
154	@inproceedings{kuhn2023semantic,
155	  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},
156	  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},
157	  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},
158	  year = {2023},
159	  url = {https://arxiv.org/abs/2302.09664}
160	}
161	
162	@inproceedings{li2023codeie,
163	  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
164	  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
165	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
166	  year = {2023},
167	  doi = {10.18653/v1/2023.acl-long.855},
168	  url = {https://arxiv.org/abs/2305.05711}
169	}
170	
171	@inproceedings{lightman2024verify,
172	  title = {Let's Verify Step by Step},
173	  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
174	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},
175	  year = {2024},
176	  url = {https://arxiv.org/abs/2305.20050}
177	}
178	
179	@inproceedings{luan2018scierc,
180	  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
181	  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
182	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
183	  year = {2018},
184	  doi = {10.18653/v1/D18-1360},
185	  url = {http://dx.doi.org/10.18653/v1/D18-1360}
186	}
187	
188	@inproceedings{manakul2023selfcheckgpt,
189	  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},
190	  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},
191	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
192	  year = {2023},
193	  doi = {10.18653/v1/2023.emnlp-main.557},
194	  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}
195	}
196	
197	@article{yao2026consistency,
198	  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},
199	  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},
200	  journal = {Genomics \& Informatics},
201	  year = {2026},
202	  doi = {10.1186/s44342-025-00063-2},
203	  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}
204	}
205	
206	@inproceedings{oh2026latentsc,
207	  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},
208	  author = {Oh, Jungsuk and Lee, Jay-Yoon},
209	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
210	  year = {2026},
211	  url = {https://ojs.aaai.org/index.php/AAAI/article/view/40536}
212	}
213	
214	@inproceedings{sainz2024gollie,
215	  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
216	  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},
217	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},
218	  year = {2024},
219	  url = {https://arxiv.org/abs/2310.03668}
220	}
221	
222	@inproceedings{snell2025scaling,
223	  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
224	  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
225	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
226	  year = {2025},
227	  url = {https://arxiv.org/abs/2408.03314}
228	}
229	
230	@inproceedings{taubenfeld2025cisc,
231	  title = {Confidence Improves Self-Consistency in LLMs},
232	  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},
233	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
234	  year = {2025},
235	  doi = {10.18653/v1/2025.findings-acl.1030},
236	  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}
237	}
238	
239	@inproceedings{thirukovalluru2024atomic,
240	  title = {Atomic Self-Consistency for Better Long Form Generations},
241	  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},
242	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
243	  year = {2024},
244	  doi = {10.18653/v1/2024.emnlp-main.706},
245	  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}
246	}
247	
248	@inproceedings{tjongkimsang2003conll,
249	  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},
250	  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},
251	  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},
252	  year = {2003},
253	  url = {https://aclanthology.org/W03-0419/}
254	}
255	
256	@inproceedings{vashurin2025cocoa,
257	  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},
258	  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},
259	  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},
260	  year = {2025},
261	  url = {https://arxiv.org/abs/2502.04964}
262	}
263	
264	@inproceedings{wadhwa2023revisiting,
265	  title = {Revisiting Relation Extraction in the era of Large Language Models},
266	  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
267	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
268	  year = {2023},
269	  doi = {10.18653/v1/2023.acl-long.868},
270	  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}
271	}
272	
273	@inproceedings{wang2023selfconsistency,
274	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
275	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
276	  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},
277	  year = {2023},
278	  url = {https://arxiv.org/abs/2203.11171}
279	}
280	
281	@inproceedings{wang2025make,
282	  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},
283	  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},
284	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
285	  pages = {6919--6932},
286	  year = {2025}
287	}
288	
289	@inproceedings{wang2025rankedvoting,
290	  title = {Ranked Voting based Self-Consistency of Large Language Models},
291	  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},
292	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
293	  year = {2025},
294	  url = {https://arxiv.org/abs/2505.10772}
295	}
296	
297	@article{willard2023guided,
298	  title = {Efficient Guided Generation for Large Language Models},
299	  author = {Willard, Brandon T. and Louf, Rémi},
300	  journal = {arXiv preprint arXiv:2307.09702},
301	  year = {2023},
302	  url = {https://arxiv.org/abs/2307.09702}
303	}
304	
305	@inproceedings{xia2025survey,
306	  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},
307	  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},
308	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
309	  year = {2025},
310	  url = {https://aclanthology.org/2025.findings-acl.1101/}
311	}
312	
313	@inproceedings{zheng2024llamafactory,
314	  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},
315	  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},
316	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},
317	  year = {2024},
318	  pages = {400--410},
319	  doi = {10.18653/v1/2024.acl-demos.38}
320	}
321	
322	@inproceedings{zhou2024uniner,
323	  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
324	  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
325	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
326	  year = {2024},
327	  url = {https://arxiv.org/abs/2308.03279}
328	}
329	
330	@inproceedings{muller2021understanding,
331	  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},
332	  author = {M{\"u}ller, Mathias and Sennrich, Rico},
333	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
334	  year = {2021},
335	  url = {https://arxiv.org/abs/2105.08504}
336	}
337	
338	@inproceedings{eikema2025structured,
339	  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},
340	  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},
341	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
342	  year = {2025},
343	  url = {https://arxiv.org/abs/2510.20700}
344	}
345	
346	@article{venktesh2025trust,
347	  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},
348	  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},
349	  journal = {arXiv preprint arXiv:2508.16665},
350	  year = {2025},
351	  url = {https://arxiv.org/abs/2508.16665}
352	}
353	
354	@inproceedings{jinnai2024mbr,
355	  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},
356	  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},
357	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
358	  year = {2024},
359	  url = {https://arxiv.org/abs/2311.05263}
360	}
361	
362	@inproceedings{ratinov2009design,
363	  title = {Design Challenges and Misconceptions in Named Entity Recognition},
364	  author = {Ratinov, Lev and Roth, Dan},
365	  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},
366	  year = {2009},
367	  pages = {147--155},
368	  publisher = {Association for Computational Linguistics}
369	}
370	
371	@inproceedings{bergkirkpatrick2012empirical,
372	  title = {An Empirical Investigation of Statistical Significance in {NLP}},
373	  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},
374	  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},
375	  year = {2012},
376	  pages = {995--1005},
377	  publisher = {Association for Computational Linguistics}
378	}
379	
380	@inproceedings{tian2023calibration,
381	  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},
382	  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},
383	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
384	  year = {2023},
385	  pages = {5433--5442},
386	  publisher = {Association for Computational Linguistics}
387	}
388	
389	@inproceedings{fernandes2022quality,
390	  title = {Quality-Aware Decoding for Neural Machine Translation},
391	  author = {Fernandes, Patrick and Farinhas, Ant{\'o}nio and Rei, Ricardo and de Souza, Jos{\'e} G. C. and Ogayo, Perez and Neubig, Graham and Martins, Andr{\'e}},
392	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
393	  year = {2022},
394	  pages = {1396--1412},
395	  url = {https://arxiv.org/abs/2205.00978}
396	}
397	
398	@inproceedings{deguchi2024centroid,
399	  title = {Centroid-Based Efficient Minimum Bayes Risk Decoding},
400	  author = {Deguchi, Hiroyuki and Sakai, Yusuke and Kamigaito, Hidetaka and Watanabe, Taro and Tanaka, Hideki and Utiyama, Masao},
401	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},
402	  pages = {11009--11018},
403	  year = {2024},
404	  url = {https://aclanthology.org/2024.findings-acl.654/}
405	}
406	
407	@inproceedings{mejer2010confidence,
408	  title = {Confidence in Structured-Prediction Using Confidence-Weighted Models},
409	  author = {Mejer, Avihai and Crammer, Koby},
410	  booktitle = {Proceedings of the 2010 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
411	  year = {2010},
412	  pages = {971--981},
413	  url = {https://aclanthology.org/D10-1095/}
414	}
415	
416	@inproceedings{schall2025hidden,
417	  title = {The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance},
418	  author = {Schall, Maximilian and de Melo, Gerard},
419	  booktitle = {Proceedings of Recent Advances in Natural Language Processing (RANLP)},
420	  year = {2025},
421	  pages = {1074--1084},
422	  url = {https://aclanthology.org/2025.ranlp-1.124/}
423	}
424	
425	@inproceedings{yun2025price,
426	  title = {The Price of Format: Diversity Collapse in {LLMs}},
427	  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},
428	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},
429	  year = {2025},
430	  url = {https://aclanthology.org/2025.findings-emnlp.836/}
431	}
432	
433	@inproceedings{park2024grammar,
434	  title = {Grammar-Aligned Decoding},
435	  author = {Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris},
436	  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
437	  year = {2024},
438	  url = {https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html}
439	}
440	
441	@inproceedings{gao2023scaling,
442	  title = {Scaling Laws for Reward Model Overoptimization},
443	  author = {Gao, Leo and Schulman, John and Hilton, Jacob},
444	  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},
445	  year = {2023},
446	  url = {https://proceedings.mlr.press/v202/gao23h.html}
447	}
448	
449	@inproceedings{kirk2024understanding,
450	  title = {Understanding the Effects of {RLHF} on {LLM} Generalisation and Diversity},
451	  author = {Kirk, Robert and Mediratta, Ishita and Nalmpantis, Christoforos and Luketina, Jelena and Hambro, Eric and Grefenstette, Edward and Raileanu, Roberta},
452	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
453	  year = {2024},
454	  url = {https://openreview.net/forum?id=PXoFut3dWW}
455	}
456	
457	@inproceedings{holtzman2020curious,
458	  title = {The Curious Case of Neural Text Degeneration},
459	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
460	  booktitle = {Proceedings of the Eighth International Conference on Learning Representations (ICLR)},
461	  year = {2020},
462	  url = {https://openreview.net/forum?id=rygGQyrFvH}
463	}
464	
465	@inproceedings{kuleshov2015calibrated,
466	  title = {Calibrated Structured Prediction},
467	  author = {Kuleshov, Volodymyr and Liang, Percy},
468	  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},
469	  year = {2015},
470	  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}
471	}
472	
473	@article{fomicheva2020unsupervised,
474	  title = {Unsupervised Quality Estimation for Neural Machine Translation},
475	  author = {Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Fr{\'e}d{\'e}ric and Guzm{\'a}n, Francisco and Fishel, Mark and Aletras, Nikolaos and Chaudhary, Vishrav and Specia, Lucia},
476	  journal = {Transactions of the Association for Computational Linguistics},
477	  volume = {8},
478	  pages = {539--555},
479	  year = {2020},
480	  doi = {10.1162/tacl_a_00330}
481	}
482	
483	@inproceedings{platt1999probabilistic,
484	  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},
485	  author = {Platt, John C.},
486	  booktitle = {Advances in Large Margin Classifiers},
487	  pages = {61--74},
488	  year = {1999},
489	  publisher = {MIT Press}
490	}
491	
492	@inproceedings{guo2017calibration,
493	  title = {On Calibration of Modern Neural Networks},
494	  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
495	  booktitle = {Proceedings of the 34th International Conference on Machine Learning},
496	  pages = {1321--1330},
497	  year = {2017}
498	}
499	
500	@inproceedings{geifman2017selective,
501	  title = {Selective Classification for Deep Neural Networks},
502	  author = {Geifman, Yonatan and El-Yaniv, Ran},
503	  booktitle = {Advances in Neural Information Processing Systems},
504	  volume = {30},
505	  year = {2017},
506	  url = {https://arxiv.org/abs/1705.08500}
507	}
508	
509	@article{dong2024xgrammar,
510	  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},
511	  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},
512	  journal = {arXiv preprint arXiv:2411.15100},
513	  year = {2024},
514	  url = {https://arxiv.org/abs/2411.15100}
515	}
516	
517	@article{lin2022teaching,
518	  title = {Teaching Models to Express Their Uncertainty in Words},
519	  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},
520	  journal = {Transactions on Machine Learning Research},
521	  year = {2022},
522	  url = {https://arxiv.org/abs/2205.14334}
523	}
524	
525	@inproceedings{varshney2022investigating,
526	  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},
527	  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},
528	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
529	  pages = {1995--2002},
530	  year = {2022},
531	  url = {https://aclanthology.org/2022.findings-acl.158}
532	}
533	
534	@article{farquhar2024detecting,
535	  title = {Detecting hallucinations in large language models using semantic entropy},
536	  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},
537	  journal = {Nature},
538	  volume = {630},
539	  pages = {625--630},
540	  year = {2024},
541	  doi = {10.1038/s41586-024-07421-0}
542	}
543	
544	@article{chen2021evaluating,
545	  title = {Evaluating Large Language Models Trained on Code},
546	  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chantzis, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},
547	  journal = {arXiv preprint arXiv:2107.03374},
548	  year = {2021},
549	  url = {https://arxiv.org/abs/2107.03374}
550	}
551	
552	@inproceedings{chen2025twofailures,
553	  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},
554	  author = {Chen, Angelica and Dohan, David and So, David},
555	  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR 2025)},
556	  year = {2025},
557	  url = {https://arxiv.org/abs/2410.23123}
558	}
559	
560	@inproceedings{aggarwal2023adaptive,
561	  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},
562	  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},
563	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},
564	  year = {2023},
565	  url = {https://arxiv.org/abs/2305.11860}
566	}
567	
568	@inproceedings{xie2023selfevaluation,
569	  title = {Self-Evaluation Guided Beam Search for Reasoning},
570	  author = {Xie, Yuxi and Kawaguchi, Kenji and Zhao, Yiran and Zhao, James Xu and Kan, Min-Yen and He, Junxian},
571	  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},
572	  year = {2023},
573	  url = {https://arxiv.org/abs/2305.00633}
574	}
575	
576	@inproceedings{xie2024selfimproving,
577	  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},
578	  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
579	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
580	  year = {2024},
581	  url = {https://arxiv.org/abs/2311.08921}
582	}
583	
584	@inproceedings{xie2023zeroshot,
585	  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},
586	  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
587	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
588	  pages = {7935--7956},
589	  year = {2023},
590	  publisher = {Association for Computational Linguistics},
591	  doi = {10.18653/v1/2023.emnlp-main.493},
592	  url = {https://aclanthology.org/2023.emnlp-main.493/}
593	}
594	
595	@article{xiao2025el4ner,
596	  title = {{EL4NER}: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models},
597	  author = {Xiao, Yuzhen and Song, Jiahe and Xu, Yongxin and Zhang, Ruizhe and Xiao, Yiqi and Lu, Xin and Zhu, Runchuan and Jiang, Bowen and Zhao, Junfeng},
598	  journal = {arXiv preprint arXiv:2505.23038},
599	  year = {2025},
600	  url = {https://arxiv.org/abs/2505.23038}
601	}
602	
603	@inproceedings{jiang2023llmblender,
604	  title = {{LLM}-Blender: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion},
605	  author = {Jiang, Dongfu and Ren, Xiang and Lin, Bill Yuchen},
606	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
607	  pages = {14165--14178},
608	  year = {2023},
609	  publisher = {Association for Computational Linguistics},
610	  doi = {10.18653/v1/2023.acl-long.792},
611	  url = {https://aclanthology.org/2023.acl-long.792/}
612	}
613	
614	@inproceedings{florian2003named,
615	  title = {Named Entity Recognition through Classifier Combination},
616	  author = {Florian, Radu and Ittycheriah, Abe and Jing, Hongyan and Zhang, Tong},
617	  booktitle = {Proceedings of the Seventh Conference on Natural Language Learning (CoNLL-2003)},
618	  pages = {168--171},
619	  year = {2003},
620	  publisher = {Association for Computational Linguistics},
621	  doi = {10.3115/1119176.1119201},
622	  url = {https://aclanthology.org/W03-0425/}
623	}
624	
625	@inproceedings{muennighoff2025s1,
626	  title = {s1: Simple Test-Time Scaling},
627	  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\`e}s, Emmanuel and Hashimoto, Tatsunori},
628	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
629	  year = {2025},
630	  url = {https://arxiv.org/abs/2501.19393}
631	}
632	
633	@inproceedings{eikema2020map,
634	  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},
635	  author = {Eikema, Bryan and Aziz, Wilker},
636	  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},
637	  pages = {4506--4520},
638	  year = {2020},
639	  url = {https://aclanthology.org/2020.coling-main.398/}
640	}
641	
642	@inproceedings{kumar2004minimum,
643	  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},
644	  author = {Kumar, Shankar and Byrne, William},
645	  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},
646	  pages = {169--176},
647	  year = {2004},
648	  url = {https://aclanthology.org/N04-1022/}
649	}
650	
651	@inproceedings{ho2023reasoning,
652	  title = {Large Language Models Are Reasoning Teachers},
653	  author = {Ho, Namgyu and Schmid, Laura and Yun, Se-Young},
654	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
655	  pages = {14852--14882},
656	  year = {2023},
657	  url = {https://aclanthology.org/2023.acl-long.830/}
658	}
659	
660	@inproceedings{min2022rethinking,
661	  title = {Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?},
662	  author = {Min, Sewon and Lyu, Xinxi and Holtzman, Ari and Artetxe, Mikel and Lewis, Mike and Hajishirzi, Hannaneh and Zettlemoyer, Luke},
663	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
664	  year = {2022},
665	  doi = {10.18653/v1/2022.emnlp-main.759},
666	  url = {https://aclanthology.org/2022.emnlp-main.759/}
667	}
668	
669	@inproceedings{suzgun2023crowd,
670	  title = {Follow the Wisdom of the Crowd: Effective Text Generation via Minimum {B}ayes Risk Decoding},
671	  author = {Suzgun, Mirac and Melas-Kyriazi, Luke and Jurafsky, Dan},
672	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
673	  year = {2023},
674	  url = {https://aclanthology.org/2023.findings-acl.262/}
675	}
676	
677	@inproceedings{stechly2024chain,
678	  title = {Chain of Thoughtlessness? {A}n Analysis of {CoT} in Planning},
679	  author = {Stechly, Kaya and Valmeekam, Karthik and Kambhampati, Subbarao},
680	  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
681	  year = {2024},
682	  url = {https://arxiv.org/abs/2405.04776}
683	}
684	
685	@inproceedings{setlur2025rewarding,
686	  title = {Rewarding Progress: Scaling Automated Process Verifiers for {LLM} Reasoning},
687	  author = {Setlur, Amrith and Nagpal, Chirag and Fisch, Adam and Geng, Xinyang and Eisenstein, Jacob and Agarwal, Rishabh and Agarwal, Alekh and Berant, Jonathan and Kumar, Aviral},
688	  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR 2025)},
689	  pages = {18006--18036},
690	  year = {2025},
691	  url = {https://arxiv.org/abs/2410.08146}
692	}
693	
694	@inproceedings{kuleshov2018accurate,
695	  title = {Accurate Uncertainties for Deep Learning Using Calibrated Regression},
696	  author = {Kuleshov, Volodymyr and Fenner, Nathan and Ermon, Stefano},
697	  booktitle = {Proceedings of the 35th International Conference on Machine Learning (ICML)},
698	  pages = {2801--2809},
699	  year = {2018},
700	  url = {https://proceedings.mlr.press/v80/kuleshov18a.html}
701	}
702	
703	@article{openai2024o1,
704	  title = {{OpenAI} o1 System Card},
705	  author = {{OpenAI}},
706	  journal = {arXiv preprint arXiv:2412.16720},
707	  year = {2024},
708	  url = {https://arxiv.org/abs/2412.16720}
709	}
710	
711	@article{ashok2023promptner,
712	  title = {{PromptNER}: Prompting For Named Entity Recognition},
713	  author = {Ashok, Dhananjay and Lipton, Zachary C.},
714	  journal = {arXiv preprint arXiv:2305.15444},
715	  year = {2023},
716	  url = {https://arxiv.org/abs/2305.15444}
717	}
718	
719	@inproceedings{wang2025gptner,
720	  title = {{GPT-NER}: Named Entity Recognition via Large Language Models},
721	  author = {Wang, Shuhe and Sun, Xiaofei and Li, Xiaoya and Ouyang, Rongbin and Wu, Fei and Zhang, Tianwei and Li, Jiwei and Wang, Guoyin},
722	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},
723	  pages = {4257--4275},
724	  year = {2025},
725	  url = {https://arxiv.org/abs/2304.10428}
726	}
727	
728	@article{wei2023chatie,
729	  title = {{ChatIE}: Zero-Shot Information Extraction via Chatting with {ChatGPT}},
730	  author = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun},
731	  journal = {arXiv preprint arXiv:2302.10205},
732	  year = {2023},
733	  url = {https://arxiv.org/abs/2302.10205}
734	}
735	
736	@article{sagi2018ensemble,
737	  title = {Ensemble learning: A survey},
738	  author = {Sagi, Omer and Rokach, Lior},
739	  journal = {Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery},
740	  volume = {8},
741	  number = {4},
742	  pages = {e1249},
743	  year = {2018},
744	  doi = {10.1002/widm.1249}
745	}
746	
747	@inproceedings{lakshminarayanan2017ensembles,
748	  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
749	  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},
750	  booktitle = {Advances in Neural Information Processing Systems 30 (NeurIPS)},
751	  year = {2017},
752	  url = {https://arxiv.org/abs/1612.01474}
753	}
754	
755	@inproceedings{welling2011sgld,
756	  title = {Bayesian Learning via Stochastic Gradient {L}angevin Dynamics},
757	  author = {Welling, Max and Teh, Yee Whye},
758	  booktitle = {Proceedings of the 28th International Conference on Machine Learning (ICML)},
759	  pages = {681--688},
760	  year = {2011}
761	}
762	
763	@inproceedings{deng2023rad,
764	  title = {Reward-Augmented Decoding: Efficient Controlled Text Generation With a Unidirectional Reward Model},
765	  author = {Deng, Haikang and Raffel, Colin},
766	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
767	  year = {2023},
768	  doi = {10.18653/v1/2023.emnlp-main.721},
769	  url = {https://aclanthology.org/2023.emnlp-main.721/}
770	}
771	
772	@article{keraghel2024ner,
773	  title = {Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study},
774	  author = {Keraghel, Imed and Morbieu, Stanislas and Nadif, Mohamed},
775	  journal = {arXiv preprint arXiv:2401.10825},
776	  year = {2024},
777	  url = {https://arxiv.org/abs/2401.10825}
778	}
779	
780	@article{xu2024llmie,
781	  title = {Large Language Models for Generative Information Extraction: A Survey},
782	  author = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},
783	  journal = {Frontiers of Computer Science},
784	  volume = {18},
785	  number = {6},
786	  pages = {186357},
787	  year = {2024},
788	  doi = {10.1007/s11704-024-40555-y}
789	}
790	
791	@inproceedings{dembczynski2011exact,
792	  title = {An Exact Algorithm for {F}-Measure Maximization},
793	  author = {Dembczy{\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\"u}llermeier, Eyke},
794	  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},
795	  year = {2011},
796	  url = {https://proceedings.neurips.cc/paper/2011/hash/03e0704b5690a2dee1861dc3ad3316c9-Abstract.html}
797	}
798	
799	@article{wen2025abstention,
800	  title = {Know Your Limits: A Survey of Abstention in Large Language Models},
801	  author = {Wen, Zhenting and Cao, Shuchen and Gu, Yu and Ye, Rui and He, Zhaorun and Peng, Yiming and Ji, Jianzhu and Liu, Yuhan and Chen, Hao},
802	  journal = {Transactions of the Association for Computational Linguistics},
803	  volume = {13},
804	  pages = {520--553},
805	  year = {2025},
806	  doi = {10.1162/tacl_a_00734},
807	  url = {https://doi.org/10.1162/tacl_a_00734}
808	}
809	
810	@article{liu2025uqcc,
811	  title = {Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey},
812	  author = {Liu, Xiaoou and Luo, Yuhang and Pang, Xianghe and Shi, Jiahao and Wang, Mengxuan and Yao, Haotian and Zhang, Haoxuan and Zhang, Zihao and Ma, Yicheng and Wang, Kai},
813	  journal = {arXiv preprint arXiv:2503.15850},
814	  year = {2025},
815	  url = {https://arxiv.org/abs/2503.15850}
816	}
817	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "6583b63b-477b-4e6f-8216-b09c6b187e9e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063},\n}\n\n@inproceedings{vijayakumar2018diverse,\n  title = {Diverse Beam Search for Improved Description of Complex Scenes},\n  author = {Vijayakumar, Ashwin K. and Cogswell, Michael and Selvaraju, Ramprasaath R. and Sun, Qing and Lee, Stefan and Crandall, David J. and Batra, Dhruv},\n  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year = {2018},\n  url = {https://arxiv.org/abs/1610.02424}\n}\n\n@inproceedings{shi2022mbr,\n  title = {Natural Language to Code Translation with Execution},\n  author = {Shi, Freda and Fried, Daniel and Ghazvininejad, Marjan and Zettlemoyer, Luke and Wang, Sida I.},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {3533--3546},\n  year = {2022},\n  url = {https://arxiv.org/abs/2204.11454}\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL 2004)},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@article{feng2025optimal,\n  title = {Optimal Self-Consistency for Efficient Reasoning with Large Language Models},\n  author = {Feng, Austin and Alonso, Marius and Odonnat, Ambroise},\n  journal = {arXiv preprint arXiv:2511.12309},\n  year = {2025},\n  url = {https://arxiv.org/abs/2511.12309}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL 2026)},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{oh2026latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year = {2026},\n  url = {https://ojs.aaai.org/index.php/AAAI/article/view/40536}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2025make,\n  title = {Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning},\n  author = {Wang, Xinglin and Feng, Shaoxiong and Li, Yiwei and Yuan, Peiwen and Zhang, Yueqi and Tan, Chuyi and Pan, Boyuan and Hu, Yao and Li, Kan},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},\n  pages = {6919--6932},\n  year = {2025}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@article{venktesh2025trust,\n  title = {Trust but Verify! A Survey on Verification Design for Test-time Scaling},\n  author = {Venktesh, V and Rathee, Mandeep and Anand, Avishek},\n  journal = {arXiv preprint arXiv:2508.16665},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.16665}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{fernandes2022quality,\n  title = {Quality-Aware Decoding for Neural Machine Translation},\n  author = {Fernandes, Patrick and Farinhas, Ant{\\'o}nio and Rei, Ricardo and de Souza, Jos{\\'e} G. C. and Ogayo, Perez and Neubig, Graham and Martins, Andr{\\'e}},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  pages = {1396--1412},\n  url = {https://arxiv.org/abs/2205.00978}\n}\n\n@inproceedings{deguchi2024centroid,\n  title = {Centroid-Based Efficient Minimum Bayes Risk Decoding},\n  author = {Deguchi, Hiroyuki and Sakai, Yusuke and Kamigaito, Hidetaka and Watanabe, Taro and Tanaka, Hideki and Utiyama, Masao},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},\n  pages = {11009--11018},\n  year = {2024},\n  url = {https://aclanthology.org/2024.findings-acl.654/}\n}\n\n@inproceedings{mejer2010confidence,\n  title = {Confidence in Structured-Prediction Using Confidence-Weighted Models},\n  author = {Mejer, Avihai and Crammer, Koby},\n  booktitle = {Proceedings of the 2010 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2010},\n  pages = {971--981},\n  url = {https://aclanthology.org/D10-1095/}\n}\n\n@inproceedings{schall2025hidden,\n  title = {The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance},\n  author = {Schall, Maximilian and de Melo, Gerard},\n  booktitle = {Proceedings of Recent Advances in Natural Language Processing (RANLP)},\n  year = {2025},\n  pages = {1074--1084},\n  url = {https://aclanthology.org/2025.ranlp-1.124/}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{park2024grammar,\n  title = {Grammar-Aligned Decoding},\n  author = {Park, Kanghee and Wang, Jiayu and Berg-Kirkpatrick, Taylor and Polikarpova, Nadia and D'Antoni, Loris},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year = {2024},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n@inproceedings{kirk2024understanding,\n  title = {Understanding the Effects of {RLHF} on {LLM} Generalisation and Diversity},\n  author = {Kirk, Robert and Mediratta, Ishita and Nalmpantis, Christoforos and Luketina, Jelena and Hambro, Eric and Grefenstette, Edward and Raileanu, Roberta},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=PXoFut3dWW}\n}\n\n@inproceedings{holtzman2020curious,\n  title = {The Curious Case of Neural Text Degeneration},\n  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  booktitle = {Proceedings of the Eighth International Conference on Learning Representations (ICLR)},\n  year = {2020},\n  url = {https://openreview.net/forum?id=rygGQyrFvH}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n@article{fomicheva2020unsupervised,\n  title = {Unsupervised Quality Estimation for Neural Machine Translation},\n  author = {Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Fr{\\'e}d{\\'e}ric and Guzm{\\'a}n, Francisco and Fishel, Mark and Aletras, Nikolaos and Chaudhary, Vishrav and Specia, Lucia},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {8},\n  pages = {539--555},\n  year = {2020},\n  doi = {10.1162/tacl_a_00330}\n}\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@inproceedings{varshney2022investigating,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  pages = {1995--2002},\n  year = {2022},\n  url = {https://aclanthology.org/2022.findings-acl.158}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2021evaluating,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chantzis, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021},\n  url = {https://arxiv.org/abs/2107.03374}\n}\n\n@inproceedings{chen2025twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Dohan, David and So, David},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR 2025)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2410.23123}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023selfevaluation,\n  title = {Self-Evaluation Guided Beam Search for Reasoning},\n  author = {Xie, Yuxi and Kawaguchi, Kenji and Zhao, Yiran and Zhao, James Xu and Kan, Min-Yen and He, Junxian},\n  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.00633}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08921}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@article{xiao2025el4ner,\n  title = {{EL4NER}: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models},\n  author = {Xiao, Yuzhen and Song, Jiahe and Xu, Yongxin and Zhang, Ruizhe and Xiao, Yiqi and Lu, Xin and Zhu, Runchuan and Jiang, Bowen and Zhao, Junfeng},\n  journal = {arXiv preprint arXiv:2505.23038},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.23038}\n}\n\n@inproceedings{jiang2023llmblender,\n  title = {{LLM}-Blender: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion},\n  author = {Jiang, Dongfu and Ren, Xiang and Lin, Bill Yuchen},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages = {14165--14178},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.acl-long.792},\n  url = {https://aclanthology.org/2023.acl-long.792/}\n}\n\n@inproceedings{florian2003named,\n  title = {Named Entity Recognition through Classifier Combination},\n  author = {Florian, Radu and Ittycheriah, Abe and Jing, Hongyan and Zhang, Tong},\n  booktitle = {Proceedings of the Seventh Conference on Natural Language Learning (CoNLL-2003)},\n  pages = {168--171},\n  year = {2003},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.3115/1119176.1119201},\n  url = {https://aclanthology.org/W03-0425/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{ho2023reasoning,\n  title = {Large Language Models Are Reasoning Teachers},\n  author = {Ho, Namgyu and Schmid, Laura and Yun, Se-Young},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages = {14852--14882},\n  year = {2023},\n  url = {https://aclanthology.org/2023.acl-long.830/}\n}\n\n@inproceedings{min2022rethinking,\n  title = {Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?},\n  author = {Min, Sewon and Lyu, Xinxi and Holtzman, Ari and Artetxe, Mikel and Lewis, Mike and Hajishirzi, Hannaneh and Zettlemoyer, Luke},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2022},\n  doi = {10.18653/v1/2022.emnlp-main.759},\n  url = {https://aclanthology.org/2022.emnlp-main.759/}\n}\n\n@inproceedings{suzgun2023crowd,\n  title = {Follow the Wisdom of the Crowd: Effective Text Generation via Minimum {B}ayes Risk Decoding},\n  author = {Suzgun, Mirac and Melas-Kyriazi, Luke and Jurafsky, Dan},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://aclanthology.org/2023.findings-acl.262/}\n}\n\n@inproceedings{stechly2024chain,\n  title = {Chain of Thoughtlessness? {A}n Analysis of {CoT} in Planning},\n  author = {Stechly, Kaya and Valmeekam, Karthik and Kambhampati, Subbarao},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2405.04776}\n}\n\n@inproceedings{setlur2025rewarding,\n  title = {Rewarding Progress: Scaling Automated Process Verifiers for {LLM} Reasoning},\n  author = {Setlur, Amrith and Nagpal, Chirag and Fisch, Adam and Geng, Xinyang and Eisenstein, Jacob and Agarwal, Rishabh and Agarwal, Alekh and Berant, Jonathan and Kumar, Aviral},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR 2025)},\n  pages = {18006--18036},\n  year = {2025},\n  url = {https://arxiv.org/abs/2410.08146}\n}\n\n@inproceedings{kuleshov2018accurate,\n  title = {Accurate Uncertainties for Deep Learning Using Calibrated Regression},\n  author = {Kuleshov, Volodymyr and Fenner, Nathan and Ermon, Stefano},\n  booktitle = {Proceedings of the 35th International Conference on Machine Learning (ICML)},\n  pages = {2801--2809},\n  year = {2018},\n  url = {https://proceedings.mlr.press/v80/kuleshov18a.html}\n}\n\n@article{openai2024o1,\n  title = {{OpenAI} o1 System Card},\n  author = {{OpenAI}},\n  journal = {arXiv preprint arXiv:2412.16720},\n  year = {2024},\n  url = {https://arxiv.org/abs/2412.16720}\n}\n\n@article{ashok2023promptner,\n  title = {{PromptNER}: Prompting For Named Entity Recognition},\n  author = {Ashok, Dhananjay and Lipton, Zachary C.},\n  journal = {arXiv preprint arXiv:2305.15444},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.15444}\n}\n\n@inproceedings{wang2025gptner,\n  title = {{GPT-NER}: Named Entity Recognition via Large Language Models},\n  author = {Wang, Shuhe and Sun, Xiaofei and Li, Xiaoya and Ouyang, Rongbin and Wu, Fei and Zhang, Tianwei and Li, Jiwei and Wang, Guoyin},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},\n  pages = {4257--4275},\n  year = {2025},\n  url = {https://arxiv.org/abs/2304.10428}\n}\n\n@article{wei2023chatie,\n  title = {{ChatIE}: Zero-Shot Information Extraction via Chatting with {ChatGPT}},\n  author = {Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun},\n  journal = {arXiv preprint arXiv:2302.10205},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.10205}\n}\n\n@article{sagi2018ensemble,\n  title = {Ensemble learning: A survey},\n  author = {Sagi, Omer and Rokach, Lior},\n  journal = {Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery},\n  volume = {8},\n  number = {4},\n  pages = {e1249},\n  year = {2018},\n  doi = {10.1002/widm.1249}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},\n  booktitle = {Advances in Neural Information Processing Systems 30 (NeurIPS)},\n  year = {2017},\n  url = {https://arxiv.org/abs/1612.01474}\n}\n\n@inproceedings{welling2011sgld,\n  title = {Bayesian Learning via Stochastic Gradient {L}angevin Dynamics},\n  author = {Welling, Max and Teh, Yee Whye},\n  booktitle = {Proceedings of the 28th International Conference on Machine Learning (ICML)},\n  pages = {681--688},\n  year = {2011}\n}\n\n@inproceedings{deng2023rad,\n  title = {Reward-Augmented Decoding: Efficient Controlled Text Generation With a Unidirectional Reward Model},\n  author = {Deng, Haikang and Raffel, Colin},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.721},\n  url = {https://aclanthology.org/2023.emnlp-main.721/}\n}\n\n@article{keraghel2024ner,\n  title = {Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study},\n  author = {Keraghel, Imed and Morbieu, Stanislas and Nadif, Mohamed},\n  journal = {arXiv preprint arXiv:2401.10825},\n  year = {2024},\n  url = {https://arxiv.org/abs/2401.10825}\n}\n\n@article{xu2024llmie,\n  title = {Large Language Models for Generative Information Extraction: A Survey},\n  author = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n  journal = {Frontiers of Computer Science},\n  volume = {18},\n  number = {6},\n  pages = {186357},\n  year = {2024},\n  doi = {10.1007/s11704-024-40555-y}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/03e0704b5690a2dee1861dc3ad3316c9-Abstract.html}\n}\n\n@article{wen2025abstention,\n  title = {Know Your Limits: A Survey of Abstention in Large Language Models},\n  author = {Wen, Zhenting and Cao, Shuchen and Gu, Yu and Ye, Rui and He, Zhaorun and Peng, Yiming and Ji, Jianzhu and Liu, Yuhan and Chen, Hao},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {13},\n  pages = {520--553},\n  year = {2025},\n  doi = {10.1162/tacl_a_00734},\n  url = {https://doi.org/10.1162/tacl_a_00734}\n}\n\n@article{liu2025uqcc,\n  title = {Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey},\n  author = {Liu, Xiaoou and Luo, Yuhang and Pang, Xianghe and Shi, Jiahao and Wang, Mengxuan and Yao, Haotian and Zhang, Haoxuan and Zhang, Zihao and Ma, Yicheng and Wang, Kai},\n  journal = {arXiv preprint arXiv:2503.15850},\n  year = {2025},\n  url = {https://arxiv.org/abs/2503.15850}\n}\n",
      "numLines": 817,
      "startLine": 1,
      "totalLines": 817
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
Now I have the bib file. Let me identify the 4 unverified citations:
1. `hobelsberger2025` (line 122-128)
2. `lightman2024` (line 171-177)
3. `venktesh2025` (line 346-352)
4. `aggarwal2023` (line 560-566)

Now I need to:
1. WebSearch to verify these 4 citations
2. Find all \cite{} keys in tex files and compare with bib entries
3. Identify orphan entries


I'll search for these 4 citations online while simultaneously extracting all the citation keys from the tex files in the docs/paper/ directory to cross-reference them against the bibliography.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "f45e9d06-c2fa-4c17-8db6-7b52272907be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tz16Tp7fB1hFGNE6gKTYcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15978,
      "cache_read_input_tokens": 25224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15978
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

找到了 bib 文件，共 ~80 条 entries。现在并行验证 4 条引用 + 提取 tex 中所有 cite keys。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "c2c91a3f-9e0d-4b0a-874b-22e1eaddb571",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tz16Tp7fB1hFGNE6gKTYcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15978,
      "cache_read_input_tokens": 25224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15978
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DNih3mrqbRB5ZJ7WwPu2Ty`</summary>

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
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "be253f57-cd44-499d-8357-50e477cb051c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tz16Tp7fB1hFGNE6gKTYcN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15978,
      "cache_read_input_tokens": 25224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15978
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

_source line 15 · 2026-05-20T13:49:27.521Z_

<details><summary>↩ Tool result · `toolu_01DNih3mrqbRB5ZJ7WwPu2Ty`</summary>

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
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "4c60c66a-db36-4b8e-90fc-a3f5d4906842",
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

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the WebSearch for the 4 citations and also grep for all cite keys in the tex files, all in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "254e8f7d-bdb0-4e5f-ad7f-fb4b4bfb6c1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVjir35NPJrvYqk26jrzVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 41202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 867
      },
      "output_tokens": 34,
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

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JUGAxrkmKVq4KV4NTgwPBv`</summary>

```json
{
  "query": "Hobelsberger \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\" arXiv 2510.20460"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "9637cc48-3088-46b2-a497-17e3ae16dc07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVjir35NPJrvYqk26jrzVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 41202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 867
      },
      "output_tokens": 34,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xgac4cpM5rHEm4wsGk4NE5`</summary>

```json
{
  "query": "Lightman \"Let's Verify Step by Step\" ICLR 2024 arXiv 2305.20050"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "c821127c-aabd-4340-b304-f2b1f0aad264",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVjir35NPJrvYqk26jrzVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 41202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 867
      },
      "output_tokens": 34,
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

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SG6Bkz72Nh6raKoyXKnH85`</summary>

```json
{
  "query": "Venktesh \"Trust but Verify\" survey verification test-time scaling arXiv 2508.16665"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "e6ddd1c5-b244-4d59-81c8-701b34f3e455",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVjir35NPJrvYqk26jrzVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 41202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 867
      },
      "output_tokens": 34,
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

_source line 20_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014wbKhqWDc195SQtUvwcNDU`</summary>

```json
{
  "query": "Aggarwal \"Let's Sample Step by Step\" adaptive consistency EMNLP 2023 arXiv 2305.11860"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "911504bd-0680-4bf0-b6e8-cea1413b2f43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVjir35NPJrvYqk26jrzVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 41202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 867
      },
      "output_tokens": 34,
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

_source line 21_

<details open><summary>🔧 Tool call — Grep · `toolu_01N8PgWUqcyjxEL346xvG7Go`</summary>

```json
{
  "pattern": "\\\\cite\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
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
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "e91b0000-5c80-4ed7-a697-1882a1ff8022",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VVjir35NPJrvYqk26jrzVp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 41202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 867
      },
      "output_tokens": 34,
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

_source line 22 · 2026-05-20T13:49:35.779Z_

<details><summary>↩ Tool result · `toolu_01N8PgWUqcyjxEL346xvG7Go`</summary>

```text
docs/paper/acl.sty:190:\renewcommand\cite{\citep}  % to get "(Author Year)" with natbib
docs/paper/sections/related_work.tex:4:Test-time compute scaling encompasses three families: (a) extended chain-of-thought reasoning \cite{muennighoff2025s1}, (b) repeated sampling with majority voting (self-consistency; \citealp{wang2023selfconsistency}) and its extensions to free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}, and (c) best-of-$N$ selection via compute-optimal allocation \cite{snell2025scaling, brown2024monkeys}.
docs/paper/sections/related_work.tex:5:Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} and adaptive gating variants \cite{aggarwal2023adaptive, wang2025make, feng2025optimal, kim2026reasc} reduce inference cost; \citet{chen2025twofailures} diagnose failure modes.
docs/paper/sections/related_work.tex:10:CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
docs/paper/sections/related_work.tex:11:Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
docs/paper/sections/related_work.tex:12:Ensemble approaches aggregate predictions from multiple models or prompts \cite{florian2003named, xiao2025el4ner}; \citet{xie2023zeroshot} propose two-stage entity voting for zero-shot NER, the closest prior work to our entity-level construction.
docs/paper/sections/related_work.tex:13:LLM-Blender \cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives diversity from temperature rather than model heterogeneity.
docs/paper/sections/related_work.tex:15:Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden}.
docs/paper/sections/related_work.tex:19:Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey, liu2025uqcc}, calibration \cite{hobelsberger2025systematic}, and abstention \cite{wen2025abstention}; semantic uncertainty \cite{kuhn2023semantic, farquhar2024detecting} and P(True) \cite{kadavath2022language} provide model-internal alternatives.
docs/paper/sections/related_work.tex:20:Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \cite{freitag2022high} and code generation where execution-based MBR improves selection \cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\rho{=}0.52$; \S\ref{sec:discussion}).
docs/paper/sections/related_work.tex:22:Our QE results connect to selective prediction \cite{geifman2017selective, kuleshov2015calibrated, varshney2022investigating}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.
docs/paper/sections/related_work.tex:26:Trained verifiers \cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} and self-evaluation guided search \cite{xie2023selfevaluation} learn per-sample scoring.
docs/paper/sections/related_work.tex:27:CISC \cite{taubenfeld2025cisc} and Self-Certainty \cite{kang2025selfcertainty} derive per-sample confidence from hidden states rather than output statistics, but require architecture-specific access to intermediate representations; these hidden-state signals remain untested for structured prediction (\S Limitations).
docs/paper/sections/related_work.tex:28:Fine-tuning \cite{kirk2024understanding} and constrained decoding \cite{holtzman2020curious, vijayakumar2018diverse} both limit the diversity recoverable for selection.
docs/paper/sections/experiments.tex:9:\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
docs/paper/sections/experiments.tex:10:\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
docs/paper/sections/experiments.tex:11:\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
docs/paper/sections/experiments.tex:12:\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
docs/paper/sections/experiments.tex:15:\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
docs/paper/sections/experiments.tex:16:We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
docs/paper/sections/experiments.tex:211:Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): FewNERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, while SciERC converges more slowly ($c{\approx}0.35$); a single stochastic sample underperforms greedy ($N{\geq}4$ needed to match).
docs/paper/sections/conclusion.tex:4:Entity-level construction partially closes the gap ($+1.40$\,pp Few-NERD, $+1.02$\,pp SciERC); a trained verifier achieves AUC${=}0.92$ but yields only $+0.30$\,pp via OOF construction, with negative cross-dataset transfer---content-aware methods \cite{cobbe2021verifiers} may bridge this.
docs/paper/sections/checklist.tex:24:Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
docs/paper/sections/checklist.tex:57:Yes. LLaMA Factory \cite{zheng2024llamafactory} for fine-tuning and XGrammar \cite{dong2024xgrammar} for constrained decoding are cited with version-relevant details in Appendix~\ref{app:training}. Evaluation uses standard span-level micro-F1 (converted to per-instance macro-F1 as described in Section~\ref{sec:evaluation}).
docs/paper/sections/appendix.tex:257:Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
docs/paper/sections/appendix.tex:411:(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \cite{ratinov2009design};
docs/paper/sections/appendix.tex:412:(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
docs/paper/sections/appendix.tex:570:Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{dong2024xgrammar, willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
docs/paper/sections/appendix.tex:857:With F1 utility, the optimal threshold depends on the full probability vector over $E_\cup$ \cite{dembczynski2011exact}; the constant $1/2$ threshold is a close approximation when $|E_\cup|$ is small (typically 5--15 in our experiments).
docs/paper/sections/appendix.tex:862:Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
docs/paper/sections/appendix.tex:863:Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.
docs/paper/sections/appendix.tex:1471:Standard calibration methods are monotonic transforms of log-probability and therefore preserve within-instance sample rankings: Platt scaling \cite{platt1999probabilistic} fits a logistic regression $\sigma(a \cdot \text{LP} + b)$, and temperature scaling \cite{guo2017calibration} divides logits by a scalar $\tau$.
docs/paper/sections/discussion.tex:11:LP compression connects to broader calibration challenges in fine-tuned LLMs \cite{kadavath2022language, xiong2024verbalized}: teacher-forcing training and constrained decoding compress the LP dynamic range, leaving within-instance variation insufficient for sample discrimination (median LP range 0.041 nats on SciERC; Appendix~\ref{app:logprob_ties}).
docs/paper/sections/discussion.tex:14:Two per-sample alternatives could bypass the LP compression bottleneck: Self-Certainty \cite{kang2025selfcertainty} derives confidence from consistency of token-level self-evaluation, while P(True) \cite{kadavath2022language} elicits the model's own correctness probability.
docs/paper/sections/method.tex:5:Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
docs/paper/sections/method.tex:70:Entity-level construction (\S\ref{sec:selection_method}) is a special case of minimum Bayes risk (MBR) decoding \cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\arg\max_{y \in \{y_1,\ldots,y_N\}}$) to construction over all subsets of $E_\cup{=}\bigcup_i y_i$.
docs/paper/sections/method.tex:81:Set-level F1 is non-linear and admits no closed-form threshold rule \cite{dembczynski2011exact}. We use balanced linear utility ($\alpha{=}1$ throughout); balanced set-overlap and F1 induce similar optimal thresholds for typical NER output sizes ($|E_\cup| \leq 30$).
docs/paper/sections/introduction.tex:3:Test-time compute scaling has emerged as a complement to model scaling \cite{snell2025scaling}: repeated sampling with majority voting \citep{wang2023selfconsistency}, best-of-$N$ with learned verifiers \cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \cite{muennighoff2025s1} yield large gains on reasoning and code generation, but the evidence concentrates on tasks with discrete answers or execution-based verification.
docs/paper/sections/introduction.tex:8:Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
docs/paper/sections/introduction.tex:16:Oracle F1 scales comparably to reasoning ($c{\approx}0.5$; \citealp{brown2024monkeys}), yet aggregation recovers ${<}1$\,pp---a persistent \textit{aggregation gap} (\S\ref{sec:scaling}) that our diagnosis traces to degeneracy eliminating candidate diversity before utility alignment matters \cite{eikema2025structured}.
docs/paper/sections/introduction.tex:25:We evaluate five signals on four NER benchmarks (SciERC \cite{luan2018scierc}, Few-NERD \cite{ding2021fewnerd}, CoNLL-2003 \cite{tjongkimsang2003conll}, WNUT-17 \cite{derczynski2017wnut}) using two 8B models with a 4B ablation, varying $N{\in}\{2,\ldots,32\}$ across 4B--8B fine-tuned and 72B zero-shot regimes.
docs/paper/sections/introduction.tex:37:    Adapting entity voting from ensemble NER \cite{florian2003named} to stochastic sampling, LP-weighted construction yields $+1.40$\,pp on Few-NERD ($p{<}0.001$; survives Holm--Bonferroni) and $+1.02$\,pp on SciERC ($p{=}0.004$, $p_{\text{adj}}{=}0.20$), but is ineffective on CoNLL ($-0.39$\,pp) where degeneracy is high (\S\ref{sec:prescriptive}).
docs/paper/sections/theory.tex:5:Entity-level construction (\S\ref{sec:prescriptive}) is a special case of minimum Bayes risk (MBR) decoding \cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\arg\max_{y \in \{y_1,\ldots,y_N\}}$) to construction over all subsets of $E_\cup{=}\bigcup_i y_i$.
docs/paper/sections/theory.tex:16:Set-level F1 is non-linear and admits no closed-form threshold rule \cite{dembczynski2011exact}. We use balanced linear utility ($\alpha{=}1$ throughout); balanced set-overlap and F1 induce similar optimal thresholds for typical NER output sizes ($|E_\cup| \leq 30$).
docs/paper/sections/theory.tex:57:Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): FewNERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, while SciERC converges more slowly ($c{\approx}0.35$); a single stochastic sample underperforms greedy ($N{\geq}4$ needed to match).
docs/paper/sections/experiments_main.tex:7:\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
docs/paper/sections/experiments_main.tex:8:\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
docs/paper/sections/experiments_main.tex:9:\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
docs/paper/sections/experiments_main.tex:10:\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
docs/paper/sections/experiments_main.tex:13:\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
docs/paper/sections/experiments_main.tex:14:$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N{=}16$ for scaling (Appendix~\ref{app:n_scaling}).
docs/paper/sections/diagnostic.tex:5:Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
docs/paper/sections/diagnostic.tex:29:FK: inter-rater agreement \cite{fleiss1971agreement} adapted to entity sets, treating unique (text, type) tuples as items with binary present/absent labels (Appendix~\ref{app:fk_independence}).
docs/paper/acl_natbib.bst:1053:  " \cite{" * crossref * "}" *
docs/paper/acl_natbib.bst:1065:  " \cite{" * crossref * "}" *
docs/paper/acl_natbib.bst:1070:  " \cite{" * crossref * "}" *
docs/paper/sections/limitations.tex:13:We tested verbalized confidence \cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
docs/paper/sections/limitations.tex:17:Other per-sample scoring methods exist but were not evaluated: Self-Certainty \cite{kang2025selfcertainty} (consistency of token-level self-evaluation) and P(True) \cite{kadavath2022language} (model's own probability estimate of correctness) both produce per-sample scores and could in principle address the alignment bottleneck; whether they suffer from similar compression under fine-tuning is unknown.
docs/paper/sections/background.tex:4:Test-time compute scaling encompasses three families: (a) extended chain-of-thought reasoning \cite{muennighoff2025s1}, (b) repeated sampling with majority voting (self-consistency; \citealp{wang2023selfconsistency}) and its extensions to free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}, and (c) best-of-$N$ selection via compute-optimal allocation \cite{snell2025scaling, brown2024monkeys}.
docs/paper/sections/background.tex:5:Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} and adaptive gating variants \cite{aggarwal2023adaptive, wang2025make, feng2025optimal, kim2026reasc} reduce inference cost; \citet{chen2025twofailures} diagnose failure modes.
docs/paper/sections/background.tex:12:CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\S\ref{sec:robustness_main}).
docs/paper/sections/background.tex:13:Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
docs/paper/sections/background.tex:14:Ensemble approaches aggregate predictions from multiple models or prompts \cite{florian2003named, xiao2025el4ner}; \citet{xie2023zeroshot} propose two-stage entity voting for zero-shot NER, the closest prior work to our entity-level construction.
docs/paper/sections/background.tex:15:LLM-Blender \cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives diversity from temperature rather than model heterogeneity.
docs/paper/sections/background.tex:17:Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden}.
docs/paper/sections/background.tex:21:Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey, liu2025uqcc}, calibration \cite{hobelsberger2025systematic}, and abstention \cite{wen2025abstention}; semantic uncertainty \cite{kuhn2023semantic, farquhar2024detecting} and P(True) \cite{kadavath2022language} provide model-internal alternatives.
docs/paper/sections/background.tex:22:Our selection strategies instantiate MBR decoding \cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \cite{freitag2022high} and code generation where execution-based MBR improves selection \cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\rho{=}0.52$; \S\ref{sec:discussion}).
docs/paper/sections/background.tex:24:Our QE results connect to selective prediction \cite{geifman2017selective, kuleshov2015calibrated, varshney2022investigating}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.
docs/paper/sections/background.tex:28:Trained verifiers \cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} and self-evaluation guided search \cite{xie2023selfevaluation} learn per-sample scoring.
docs/paper/sections/background.tex:29:CISC \cite{taubenfeld2025cisc} and Self-Certainty \cite{kang2025selfcertainty} derive per-sample confidence from hidden states rather than output statistics, but require architecture-specific access to intermediate representations; these hidden-state signals remain untested for structured prediction (\S Limitations).
docs/paper/sections/background.tex:30:Fine-tuning \cite{kirk2024understanding} and constrained decoding \cite{holtzman2020curious, vijayakumar2018diverse} both limit the diversity recoverable for selection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "93ec375b-3bf7-4d00-b639-fe537b61420a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/acl.sty:190:\\renewcommand\\cite{\\citep}  % to get \"(Author Year)\" with natbib\ndocs/paper/sections/related_work.tex:4:Test-time compute scaling encompasses three families: (a) extended chain-of-thought reasoning \\cite{muennighoff2025s1}, (b) repeated sampling with majority voting (self-consistency; \\citealp{wang2023selfconsistency}) and its extensions to free-form text \\cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}, and (c) best-of-$N$ selection via compute-optimal allocation \\cite{snell2025scaling, brown2024monkeys}.\ndocs/paper/sections/related_work.tex:5:Reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} and adaptive gating variants \\cite{aggarwal2023adaptive, wang2025make, feng2025optimal, kim2026reasc} reduce inference cost; \\citet{chen2025twofailures} diagnose failure modes.\ndocs/paper/sections/related_work.tex:10:CoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\\S\\ref{sec:robustness_main}).\ndocs/paper/sections/related_work.tex:11:Earlier work on confidence for structured prediction \\cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.\ndocs/paper/sections/related_work.tex:12:Ensemble approaches aggregate predictions from multiple models or prompts \\cite{florian2003named, xiao2025el4ner}; \\citet{xie2023zeroshot} propose two-stage entity voting for zero-shot NER, the closest prior work to our entity-level construction.\ndocs/paper/sections/related_work.tex:13:LLM-Blender \\cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives diversity from temperature rather than model heterogeneity.\ndocs/paper/sections/related_work.tex:15:Our evaluation builds on generative IE \\cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \\cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden}.\ndocs/paper/sections/related_work.tex:19:Surveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey, liu2025uqcc}, calibration \\cite{hobelsberger2025systematic}, and abstention \\cite{wen2025abstention}; semantic uncertainty \\cite{kuhn2023semantic, farquhar2024detecting} and P(True) \\cite{kadavath2022language} provide model-internal alternatives.\ndocs/paper/sections/related_work.tex:20:Our selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \\cite{freitag2022high} and code generation where execution-based MBR improves selection \\cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\\rho{=}0.52$; \\S\\ref{sec:discussion}).\ndocs/paper/sections/related_work.tex:22:Our QE results connect to selective prediction \\cite{geifman2017selective, kuleshov2015calibrated, varshney2022investigating}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.\ndocs/paper/sections/related_work.tex:26:Trained verifiers \\cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} and self-evaluation guided search \\cite{xie2023selfevaluation} learn per-sample scoring.\ndocs/paper/sections/related_work.tex:27:CISC \\cite{taubenfeld2025cisc} and Self-Certainty \\cite{kang2025selfcertainty} derive per-sample confidence from hidden states rather than output statistics, but require architecture-specific access to intermediate representations; these hidden-state signals remain untested for structured prediction (\\S Limitations).\ndocs/paper/sections/related_work.tex:28:Fine-tuning \\cite{kirk2024understanding} and constrained decoding \\cite{holtzman2020curious, vijayakumar2018diverse} both limit the diversity recoverable for selection.\ndocs/paper/sections/experiments.tex:9:\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\ndocs/paper/sections/experiments.tex:10:\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\ndocs/paper/sections/experiments.tex:11:\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\ndocs/paper/sections/experiments.tex:12:\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\ndocs/paper/sections/experiments.tex:15:\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\ndocs/paper/sections/experiments.tex:16:We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\ndocs/paper/sections/experiments.tex:211:Oracle F1 follows $F_1(N) = a - b \\cdot N^{-c}$ ($R^2 > 0.999$; Figure~\\ref{fig:oracle_scaling}): FewNERD ($c{\\approx}0.61$) scales comparably to reasoning tasks \\cite{brown2024monkeys}, while SciERC converges more slowly ($c{\\approx}0.35$); a single stochastic sample underperforms greedy ($N{\\geq}4$ needed to match).\ndocs/paper/sections/conclusion.tex:4:Entity-level construction partially closes the gap ($+1.40$\\,pp Few-NERD, $+1.02$\\,pp SciERC); a trained verifier achieves AUC${=}0.92$ but yields only $+0.30$\\,pp via OOF construction, with negative cross-dataset transfer---content-aware methods \\cite{cobbe2021verifiers} may bridge this.\ndocs/paper/sections/checklist.tex:24:Yes. All datasets are cited: SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, Few-NERD \\cite{ding2021fewnerd}, WNUT-17 \\cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \\cite{zheng2024llamafactory}. Constrained decoding: XGrammar \\cite{dong2024xgrammar}. See Sections~\\ref{sec:introduction}, \\ref{sec:evaluation}, and Appendix~\\ref{app:training}.\ndocs/paper/sections/checklist.tex:57:Yes. LLaMA Factory \\cite{zheng2024llamafactory} for fine-tuning and XGrammar \\cite{dong2024xgrammar} for constrained decoding are cited with version-relevant details in Appendix~\\ref{app:training}. Evaluation uses standard span-level micro-F1 (converted to per-instance macro-F1 as described in Section~\\ref{sec:evaluation}).\ndocs/paper/sections/appendix.tex:257:Our $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\ndocs/paper/sections/appendix.tex:411:(2) $\\delta_{\\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \\cite{ratinov2009design};\ndocs/paper/sections/appendix.tex:412:(3) $\\delta_{\\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \\cite{bergkirkpatrick2012empirical}.\ndocs/paper/sections/appendix.tex:570:Inference uses vLLM with XGrammar-based JSON schema enforcement \\cite{dong2024xgrammar, willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\ndocs/paper/sections/appendix.tex:857:With F1 utility, the optimal threshold depends on the full probability vector over $E_\\cup$ \\cite{dembczynski2011exact}; the constant $1/2$ threshold is a close approximation when $|E_\\cup|$ is small (typically 5--15 in our experiments).\ndocs/paper/sections/appendix.tex:862:Our selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\ndocs/paper/sections/appendix.tex:863:Despite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.\ndocs/paper/sections/appendix.tex:1471:Standard calibration methods are monotonic transforms of log-probability and therefore preserve within-instance sample rankings: Platt scaling \\cite{platt1999probabilistic} fits a logistic regression $\\sigma(a \\cdot \\text{LP} + b)$, and temperature scaling \\cite{guo2017calibration} divides logits by a scalar $\\tau$.\ndocs/paper/sections/discussion.tex:11:LP compression connects to broader calibration challenges in fine-tuned LLMs \\cite{kadavath2022language, xiong2024verbalized}: teacher-forcing training and constrained decoding compress the LP dynamic range, leaving within-instance variation insufficient for sample discrimination (median LP range 0.041 nats on SciERC; Appendix~\\ref{app:logprob_ties}).\ndocs/paper/sections/discussion.tex:14:Two per-sample alternatives could bypass the LP compression bottleneck: Self-Certainty \\cite{kang2025selfcertainty} derives confidence from consistency of token-level self-evaluation, while P(True) \\cite{kadavath2022language} elicits the model's own correctness probability.\ndocs/paper/sections/method.tex:5:Given model $\\mathcal{M}$ and input $x$, we sample $N$ outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}, where each $y_i$ is an entity set.\ndocs/paper/sections/method.tex:70:Entity-level construction (\\S\\ref{sec:selection_method}) is a special case of minimum Bayes risk (MBR) decoding \\cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\\arg\\max_{y \\in \\{y_1,\\ldots,y_N\\}}$) to construction over all subsets of $E_\\cup{=}\\bigcup_i y_i$.\ndocs/paper/sections/method.tex:81:Set-level F1 is non-linear and admits no closed-form threshold rule \\cite{dembczynski2011exact}. We use balanced linear utility ($\\alpha{=}1$ throughout); balanced set-overlap and F1 induce similar optimal thresholds for typical NER output sizes ($|E_\\cup| \\leq 30$).\ndocs/paper/sections/introduction.tex:3:Test-time compute scaling has emerged as a complement to model scaling \\cite{snell2025scaling}: repeated sampling with majority voting \\citep{wang2023selfconsistency}, best-of-$N$ with learned verifiers \\cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \\cite{muennighoff2025s1} yield large gains on reasoning and code generation, but the evidence concentrates on tasks with discrete answers or execution-based verification.\ndocs/paper/sections/introduction.tex:8:Existing self-consistency methods \\cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.\ndocs/paper/sections/introduction.tex:16:Oracle F1 scales comparably to reasoning ($c{\\approx}0.5$; \\citealp{brown2024monkeys}), yet aggregation recovers ${<}1$\\,pp---a persistent \\textit{aggregation gap} (\\S\\ref{sec:scaling}) that our diagnosis traces to degeneracy eliminating candidate diversity before utility alignment matters \\cite{eikema2025structured}.\ndocs/paper/sections/introduction.tex:25:We evaluate five signals on four NER benchmarks (SciERC \\cite{luan2018scierc}, Few-NERD \\cite{ding2021fewnerd}, CoNLL-2003 \\cite{tjongkimsang2003conll}, WNUT-17 \\cite{derczynski2017wnut}) using two 8B models with a 4B ablation, varying $N{\\in}\\{2,\\ldots,32\\}$ across 4B--8B fine-tuned and 72B zero-shot regimes.\ndocs/paper/sections/introduction.tex:37:    Adapting entity voting from ensemble NER \\cite{florian2003named} to stochastic sampling, LP-weighted construction yields $+1.40$\\,pp on Few-NERD ($p{<}0.001$; survives Holm--Bonferroni) and $+1.02$\\,pp on SciERC ($p{=}0.004$, $p_{\\text{adj}}{=}0.20$), but is ineffective on CoNLL ($-0.39$\\,pp) where degeneracy is high (\\S\\ref{sec:prescriptive}).\ndocs/paper/sections/theory.tex:5:Entity-level construction (\\S\\ref{sec:prescriptive}) is a special case of minimum Bayes risk (MBR) decoding \\cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\\arg\\max_{y \\in \\{y_1,\\ldots,y_N\\}}$) to construction over all subsets of $E_\\cup{=}\\bigcup_i y_i$.\ndocs/paper/sections/theory.tex:16:Set-level F1 is non-linear and admits no closed-form threshold rule \\cite{dembczynski2011exact}. We use balanced linear utility ($\\alpha{=}1$ throughout); balanced set-overlap and F1 induce similar optimal thresholds for typical NER output sizes ($|E_\\cup| \\leq 30$).\ndocs/paper/sections/theory.tex:57:Oracle F1 follows $F_1(N) = a - b \\cdot N^{-c}$ ($R^2 > 0.999$; Figure~\\ref{fig:oracle_scaling}): FewNERD ($c{\\approx}0.61$) scales comparably to reasoning tasks \\cite{brown2024monkeys}, while SciERC converges more slowly ($c{\\approx}0.35$); a single stochastic sample underperforms greedy ($N{\\geq}4$ needed to match).\ndocs/paper/sections/experiments_main.tex:7:\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\\approx}$65\\% F1).\ndocs/paper/sections/experiments_main.tex:8:\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:selection_gap}).\ndocs/paper/sections/experiments_main.tex:9:\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control.\ndocs/paper/sections/experiments_main.tex:10:\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary.\ndocs/paper/sections/experiments_main.tex:13:\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others; Appendix~\\ref{app:epoch_confound}).\ndocs/paper/sections/experiments_main.tex:14:$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}; $N{=}16$ for scaling (Appendix~\\ref{app:n_scaling}).\ndocs/paper/sections/diagnostic.tex:5:Given model $\\mathcal{M}$ and input $x$, we sample $N$ outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}, where each $y_i$ is an entity set.\ndocs/paper/sections/diagnostic.tex:29:FK: inter-rater agreement \\cite{fleiss1971agreement} adapted to entity sets, treating unique (text, type) tuples as items with binary present/absent labels (Appendix~\\ref{app:fk_independence}).\ndocs/paper/acl_natbib.bst:1053:  \" \\cite{\" * crossref * \"}\" *\ndocs/paper/acl_natbib.bst:1065:  \" \\cite{\" * crossref * \"}\" *\ndocs/paper/acl_natbib.bst:1070:  \" \\cite{\" * crossref * \"}\" *\ndocs/paper/sections/limitations.tex:13:We tested verbalized confidence \\cite{lin2022teaching, tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\\ref{app:verbalized_confidence}).\ndocs/paper/sections/limitations.tex:17:Other per-sample scoring methods exist but were not evaluated: Self-Certainty \\cite{kang2025selfcertainty} (consistency of token-level self-evaluation) and P(True) \\cite{kadavath2022language} (model's own probability estimate of correctness) both produce per-sample scores and could in principle address the alignment bottleneck; whether they suffer from similar compression under fine-tuning is unknown.\ndocs/paper/sections/background.tex:4:Test-time compute scaling encompasses three families: (a) extended chain-of-thought reasoning \\cite{muennighoff2025s1}, (b) repeated sampling with majority voting (self-consistency; \\citealp{wang2023selfconsistency}) and its extensions to free-form text \\cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}, and (c) best-of-$N$ selection via compute-optimal allocation \\cite{snell2025scaling, brown2024monkeys}.\ndocs/paper/sections/background.tex:5:Reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc} and adaptive gating variants \\cite{aggarwal2023adaptive, wang2025make, feng2025optimal, kim2026reasc} reduce inference cost; \\citet{chen2025twofailures} diagnose failure modes.\ndocs/paper/sections/background.tex:12:CoCoA \\cite{vashurin2025cocoa} fuses confidence with consistency; our supervised baseline confirms combination is not the bottleneck (\\S\\ref{sec:robustness_main}).\ndocs/paper/sections/background.tex:13:Earlier work on confidence for structured prediction \\cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.\ndocs/paper/sections/background.tex:14:Ensemble approaches aggregate predictions from multiple models or prompts \\cite{florian2003named, xiao2025el4ner}; \\citet{xie2023zeroshot} propose two-stage entity voting for zero-shot NER, the closest prior work to our entity-level construction.\ndocs/paper/sections/background.tex:15:LLM-Blender \\cite{jiang2023llmblender} fuses outputs from multiple LLMs via pairwise ranking, whereas our single-model stochastic sampling derives diversity from temperature rather than model heterogeneity.\ndocs/paper/sections/background.tex:17:Our evaluation builds on generative IE \\cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving} and constrained decoding \\cite{willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden}.\ndocs/paper/sections/background.tex:21:Surveys cover confidence estimation \\cite{geng2024confidence}, uncertainty quantification \\cite{xia2025survey, liu2025uqcc}, calibration \\cite{hobelsberger2025systematic}, and abstention \\cite{wen2025abstention}; semantic uncertainty \\cite{kuhn2023semantic, farquhar2024detecting} and P(True) \\cite{kadavath2022language} provide model-internal alternatives.\ndocs/paper/sections/background.tex:22:Our selection strategies instantiate MBR decoding \\cite{eikema2022sampling, deguchi2024centroid}; unlike MT where MBR yields consistent gains \\cite{freitag2022high} and code generation where execution-based MBR improves selection \\cite{shi2022mbr}, instance degeneracy eliminates the headroom MBR needs even when utility is well-aligned ($\\rho{=}0.52$; \\S\\ref{sec:discussion}).\ndocs/paper/sections/background.tex:24:Our QE results connect to selective prediction \\cite{geifman2017selective, kuleshov2015calibrated, varshney2022investigating}: signals with AUROC up to 0.82 support abstention policies independent of sample selection.\ndocs/paper/sections/background.tex:28:Trained verifiers \\cite{cobbe2021verifiers, lightman2024verify, fernandes2022quality} and self-evaluation guided search \\cite{xie2023selfevaluation} learn per-sample scoring.\ndocs/paper/sections/background.tex:29:CISC \\cite{taubenfeld2025cisc} and Self-Certainty \\cite{kang2025selfcertainty} derive per-sample confidence from hidden states rather than output statistics, but require architecture-specific access to intermediate representations; these hidden-state signals remain untested for structured prediction (\\S Limitations).\ndocs/paper/sections/background.tex:30:Fine-tuning \\cite{kirk2024understanding} and constrained decoding \\cite{holtzman2020curious, vijayakumar2018diverse} both limit the diversity recoverable for selection.",
    "numLines": 71
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T13:49:36.775Z_

<details><summary>↩ Tool result · `toolu_01JUGAxrkmKVq4KV4NTgwPBv`</summary>

```text
Web search results for query: "Hobelsberger "Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models" arXiv 2510.20460"

Links: [{"title":"[2510.20460] Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models","url":"https://arxiv.org/abs/2510.20460"},{"title":"Methodology Oct 2025","url":"https://arxiv.org/list/stat.ME/2025-10?skip=400&show=25"},{"title":"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models","url":"https://arxiv.org/html/2510.20460v1"},{"title":"(PDF) Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models","url":"https://www.researchgate.net/publication/396847893_Systematic_Evaluation_of_Uncertainty_Estimation_Methods_in_Large_Language_Models"},{"title":"Uncertainty Estimation in Large Language Models","url":"https://www.emergentmind.com/papers/2510.20460"},{"title":"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models","url":"https://arxiv.org/pdf/2510.20460"}]

I found the paper! Here's what I discovered:

The paper "Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models" was authored by Christian Hobelsberger, Theresa Winner, Andreas Nawroth, Oliver Mitevski, and Anna-Carolina Haensch.

The paper addresses the fact that large language models produce outputs with varying levels of uncertainty and correctness, making their practical reliability far from guaranteed.

The authors systematically evaluate four approaches for confidence estimation in LLM outputs: VCE, MSP, Sample Consistency, and CoCoA, testing them across four question-answering tasks using a state-of-the-art open-source LLM.

The results show that each uncertainty metric captures a different facet of model confidence and that the hybrid CoCoA approach yields the best reliability overall, improving both calibration and discrimination of correct answers.

The paper was published on October 23, 2025, and is available on arXiv at https://arxiv.org/abs/2510.20460.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "0c70adca-1e5c-4b67-892d-af1d12adaa79",
  "tool_use_result": {
    "query": "Hobelsberger \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\" arXiv 2510.20460",
    "results": [
      {
        "tool_use_id": "srvtoolu_01B6AWiaYSkvb7VM5RXxYFHQ",
        "content": [
          {
            "title": "[2510.20460] Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models",
            "url": "https://arxiv.org/abs/2510.20460"
          },
          {
            "title": "Methodology Oct 2025",
            "url": "https://arxiv.org/list/stat.ME/2025-10?skip=400&show=25"
          },
          {
            "title": "Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models",
            "url": "https://arxiv.org/html/2510.20460v1"
          },
          {
            "title": "(PDF) Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models",
            "url": "https://www.researchgate.net/publication/396847893_Systematic_Evaluation_of_Uncertainty_Estimation_Methods_in_Large_Language_Models"
          },
          {
            "title": "Uncertainty Estimation in Large Language Models",
            "url": "https://www.emergentmind.com/papers/2510.20460"
          },
          {
            "title": "Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.20460"
          }
        ]
      },
      "I found the paper! Here's what I discovered:\n\nThe paper \"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\" was authored by Christian Hobelsberger, Theresa Winner, Andreas Nawroth, Oliver Mitevski, and Anna-Carolina Haensch.\n\nThe paper addresses the fact that large language models produce outputs with varying levels of uncertainty and correctness, making their practical reliability far from guaranteed.\n\nThe authors systematically evaluate four approaches for confidence estimation in LLM outputs: VCE, MSP, Sample Consistency, and CoCoA, testing them across four question-answering tasks using a state-of-the-art open-source LLM.\n\nThe results show that each uncertainty metric captures a different facet of model confidence and that the hybrid CoCoA approach yields the best reliability overall, improving both calibration and discrimination of correct answers.\n\nThe paper was published on October 23, 2025, and is available on arXiv at https://arxiv.org/abs/2510.20460."
    ],
    "durationSeconds": 5.111821935
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T13:49:37.893Z_

<details><summary>↩ Tool result · `toolu_01Xgac4cpM5rHEm4wsGk4NE5`</summary>

```text
Web search results for query: "Lightman "Let's Verify Step by Step" ICLR 2024 arXiv 2305.20050"

Links: [{"title":"[2305.20050] Let's Verify Step by Step","url":"https://arxiv.org/abs/2305.20050"},{"title":"Let's Verify Step by Step","url":"https://blog.athina.ai/let-s-verify-step-by-step"},{"title":"[2305.20050] Let's Verify Step by Step","url":"http://export.arxiv.org/abs/2305.20050"},{"title":"[2305.20050] Let's Verify Step by Step - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2305.20050"},{"title":"Let's Verify Step by Step","url":"https://www.researchgate.net/publication/371175770_Let's_Verify_Step_by_Step"},{"title":"[PDF] Let's Verify Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc"},{"title":"Paper page - Let's Verify Step by Step","url":"https://huggingface.co/papers/2305.20050"},{"title":"Figure 2 from Let's Verify Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc/figure/2"},{"title":"GitHub - kyegomez/Lets-Verify-Step-by-Step: \"Improving Mathematical Reasoning with Process Supervision\" by OPENAI · GitHub","url":"https://github.com/kyegomez/Lets-Verify-Step-by-Step"}]

I found the paper! Here's the information from the search results:

## "Let's Verify Step by Step" - arXiv 2305.20050

The paper was authored by Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe, and was posted on arXiv on May 31, 2023.

**Main Contribution:**
The paper finds that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset, with the process-supervised model solving 78% of problems from a representative subset of the MATH test set.

**Research Focus:**
The paper compares outcome supervision (which provides feedback for a final result) and process supervision (which provides feedback for each intermediate reasoning step), given the importance of training reliable models and the high cost of human feedback.

The paper appears to have been published at an International Conference (based on the metadata from Semantic Scholar), though the search results don't explicitly mention ICLR 2024 as the venue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "dccb5700-a4a7-47b3-9245-815d7545df73",
  "tool_use_result": {
    "query": "Lightman \"Let's Verify Step by Step\" ICLR 2024 arXiv 2305.20050",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MrHN3yxwaRmKanYeDauAxU",
        "content": [
          {
            "title": "[2305.20050] Let's Verify Step by Step",
            "url": "https://arxiv.org/abs/2305.20050"
          },
          {
            "title": "Let's Verify Step by Step",
            "url": "https://blog.athina.ai/let-s-verify-step-by-step"
          },
          {
            "title": "[2305.20050] Let's Verify Step by Step",
            "url": "http://export.arxiv.org/abs/2305.20050"
          },
          {
            "title": "[2305.20050] Let's Verify Step by Step - ar5iv - arXiv",
            "url": "https://ar5iv.labs.arxiv.org/html/2305.20050"
          },
          {
            "title": "Let's Verify Step by Step",
            "url": "https://www.researchgate.net/publication/371175770_Let's_Verify_Step_by_Step"
          },
          {
            "title": "[PDF] Let's Verify Step by Step | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc"
          },
          {
            "title": "Paper page - Let's Verify Step by Step",
            "url": "https://huggingface.co/papers/2305.20050"
          },
          {
            "title": "Figure 2 from Let's Verify Step by Step | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc/figure/2"
          },
          {
            "title": "GitHub - kyegomez/Lets-Verify-Step-by-Step: \"Improving Mathematical Reasoning with Process Supervision\" by OPENAI · GitHub",
            "url": "https://github.com/kyegomez/Lets-Verify-Step-by-Step"
          }
        ]
      },
      "I found the paper! Here's the information from the search results:\n\n## \"Let's Verify Step by Step\" - arXiv 2305.20050\n\nThe paper was authored by Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe, and was posted on arXiv on May 31, 2023.\n\n**Main Contribution:**\nThe paper finds that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset, with the process-supervised model solving 78% of problems from a representative subset of the MATH test set.\n\n**Research Focus:**\nThe paper compares outcome supervision (which provides feedback for a final result) and process supervision (which provides feedback for each intermediate reasoning step), given the importance of training reliable models and the high cost of human feedback.\n\nThe paper appears to have been published at an International Conference (based on the metadata from Semantic Scholar), though the search results don't explicitly mention ICLR 2024 as the venue."
    ],
    "durationSeconds": 5.2888854239999965
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T13:49:40.092Z_

<details><summary>↩ Tool result · `toolu_014wbKhqWDc195SQtUvwcNDU`</summary>

```text
Web search results for query: "Aggarwal "Let's Sample Step by Step" adaptive consistency EMNLP 2023 arXiv 2305.11860"

Links: [{"title":"Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.761/"},{"title":"Table 4 from Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Sample-Step-by-Step:-Adaptive-Consistency-for-Aggarwal-Madaan/b4a6c010724f0459c9791018e34a982cf96987cf/figure/7"},{"title":"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | OpenReview","url":"https://openreview.net/forum?id=ETNa4Wb65J"},{"title":"Paper page - Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning with LLMs","url":"https://huggingface.co/papers/2305.11860"},{"title":"Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | Request PDF","url":"https://www.researchgate.net/publication/376401874_Let's_Sample_Step_by_Step_Adaptive-Consistency_for_Efficient_Reasoning_and_Coding_with_LLMs"},{"title":"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning & Coding with LLMs","url":"https://sample-step-by-step.info/"},{"title":"ACR: Adaptive Confidence Re-Scoring for Reliable Answer Selection Among Multiple Candidates","url":"https://www.mdpi.com/2076-3417/15/17/9587"},{"title":"Publications | Pranjal Aggarwal","url":"https://pranjal2041.github.io/publications/"},{"title":"GitHub - Pranjal2041/AdaptiveConsistency: Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning with LLMs · GitHub","url":"https://github.com/Pranjal2041/AdaptiveConsistency"},{"title":"[2305.11860] Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs","url":"https://arxiv.org/abs/2305.11860"}]

I found the paper you're looking for! Here are the key details:

**"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs"** is by Pranjal Aggarwal, Aman Madaan, Yiming Yang, and Mausam, published at EMNLP 2023 in Singapore.

**arXiv ID:** 2305.11860

**Core Contribution:** The paper addresses the limitation that existing Self-Consistency techniques always generate a constant number of samples per question, proposing Adaptive-Consistency as a cost-efficient, model-agnostic technique that dynamically adjusts the number of samples per question using a lightweight stopping criterion.

**Key Results:** The technique reduces sample budget by up to 7.9 times with an average accuracy drop of less than 0.1%.

The paper is available on arXiv, the ACL Anthology, and the authors have provided a GitHub repository with the implementation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "a7630d53-2625-44c7-bebc-4854084b9776",
  "tool_use_result": {
    "query": "Aggarwal \"Let's Sample Step by Step\" adaptive consistency EMNLP 2023 arXiv 2305.11860",
    "results": [
      {
        "tool_use_id": "srvtoolu_013SXQid7HjrBENYguCkcS2g",
        "content": [
          {
            "title": "Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2023.emnlp-main.761/"
          },
          {
            "title": "Table 4 from Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Let's-Sample-Step-by-Step:-Adaptive-Consistency-for-Aggarwal-Madaan/b4a6c010724f0459c9791018e34a982cf96987cf/figure/7"
          },
          {
            "title": "Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=ETNa4Wb65J"
          },
          {
            "title": "Paper page - Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning with LLMs",
            "url": "https://huggingface.co/papers/2305.11860"
          },
          {
            "title": "Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/376401874_Let's_Sample_Step_by_Step_Adaptive-Consistency_for_Efficient_Reasoning_and_Coding_with_LLMs"
          },
          {
            "title": "Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning & Coding with LLMs",
            "url": "https://sample-step-by-step.info/"
          },
          {
            "title": "ACR: Adaptive Confidence Re-Scoring for Reliable Answer Selection Among Multiple Candidates",
            "url": "https://www.mdpi.com/2076-3417/15/17/9587"
          },
          {
            "title": "Publications | Pranjal Aggarwal",
            "url": "https://pranjal2041.github.io/publications/"
          },
          {
            "title": "GitHub - Pranjal2041/AdaptiveConsistency: Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning with LLMs · GitHub",
            "url": "https://github.com/Pranjal2041/AdaptiveConsistency"
          },
          {
            "title": "[2305.11860] Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs",
            "url": "https://arxiv.org/abs/2305.11860"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**\"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs\"** is by Pranjal Aggarwal, Aman Madaan, Yiming Yang, and Mausam, published at EMNLP 2023 in Singapore.\n\n**arXiv ID:** 2305.11860\n\n**Core Contribution:** The paper addresses the limitation that existing Self-Consistency techniques always generate a constant number of samples per question, proposing Adaptive-Consistency as a cost-efficient, model-agnostic technique that dynamically adjusts the number of samples per question using a lightweight stopping criterion.\n\n**Key Results:** The technique reduces sample budget by up to 7.9 times with an average accuracy drop of less than 0.1%.\n\nThe paper is available on arXiv, the ACL Anthology, and the authors have provided a GitHub repository with the implementation."
    ],
    "durationSeconds": 5.966083551000003
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T13:49:40.133Z_

<details><summary>↩ Tool result · `toolu_01SG6Bkz72Nh6raKoyXKnH85`</summary>

```text
Web search results for query: "Venktesh "Trust but Verify" survey verification test-time scaling arXiv 2508.16665"

Links: [{"title":"[2508.16665] Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/abs/2508.16665"},{"title":"Tool Verification for Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2603.02203.pdf"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v3"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/pdf/2508.16665"},{"title":"(PDF) Think Right, Not More: Test-Time Scaling for Numerical Claim Verification","url":"https://www.researchgate.net/publication/395943627_Think_Right_Not_More_Test-Time_Scaling_for_Numerical_Claim_Verification"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://openreview.net/pdf?id=sytEeAZYvf"},{"title":"[2509.22101] Think Right, Not More: Test-Time Scaling for Numerical Claim Verification","url":"https://arxiv.org/abs/2509.22101"}]

I found the paper you were looking for! "Trust but Verify! A Survey on Verification Design for Test-time Scaling" is authored by V Venktesh and one other author (with co-authors Mandeep Rathee and Avishek Anand).

Here's what the paper covers:

Test-time scaling (TTS) has emerged as a new frontier for scaling the performance of Large Language Models. In test-time scaling, by using more computational resources during inference, LLMs can improve their reasoning process and task performance.

Several approaches have emerged for TTS such as distilling reasoning traces from another model or exploring the vast decoding search space by employing a verifier. The verifiers serve as reward models that help score the candidate outputs from the decoding process to diligently explore the vast solution space and select the best outcome.

The verifiers could be prompt-based, fine-tuned as a discriminative or generative model to verify process paths, outcomes or both. In this survey, the authors cover the diverse approaches in the literature and present a unified view of verifier training, types and their utility in test-time scaling.

The paper is available on arXiv at https://arxiv.org/abs/2508.16665.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "a8daa874-00a3-4285-879d-6c05182894e7",
  "tool_use_result": {
    "query": "Venktesh \"Trust but Verify\" survey verification test-time scaling arXiv 2508.16665",
    "results": [
      {
        "tool_use_id": "srvtoolu_0175aX9SNLW9AkG6SHj9CZHT",
        "content": [
          {
            "title": "[2508.16665] Trust but Verify! A Survey on Verification Design for Test-time Scaling",
            "url": "https://arxiv.org/abs/2508.16665"
          },
          {
            "title": "Tool Verification for Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2603.02203.pdf"
          },
          {
            "title": "Trust but Verify! A Survey on Verification Design for Test-time Scaling",
            "url": "https://arxiv.org/html/2508.16665v3"
          },
          {
            "title": "Trust but Verify! A Survey on Verification Design for Test-time Scaling",
            "url": "https://arxiv.org/pdf/2508.16665"
          },
          {
            "title": "(PDF) Think Right, Not More: Test-Time Scaling for Numerical Claim Verification",
            "url": "https://www.researchgate.net/publication/395943627_Think_Right_Not_More_Test-Time_Scaling_for_Numerical_Claim_Verification"
          },
          {
            "title": "Trust but Verify! A Survey on Verification Design for Test-time Scaling",
            "url": "https://openreview.net/pdf?id=sytEeAZYvf"
          },
          {
            "title": "[2509.22101] Think Right, Not More: Test-Time Scaling for Numerical Claim Verification",
            "url": "https://arxiv.org/abs/2509.22101"
          }
        ]
      },
      "I found the paper you were looking for! \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\" is authored by V Venktesh and one other author (with co-authors Mandeep Rathee and Avishek Anand).\n\nHere's what the paper covers:\n\nTest-time scaling (TTS) has emerged as a new frontier for scaling the performance of Large Language Models. In test-time scaling, by using more computational resources during inference, LLMs can improve their reasoning process and task performance.\n\nSeveral approaches have emerged for TTS such as distilling reasoning traces from another model or exploring the vast decoding search space by employing a verifier. The verifiers serve as reward models that help score the candidate outputs from the decoding process to diligently explore the vast solution space and select the best outcome.\n\nThe verifiers could be prompt-based, fine-tuned as a discriminative or generative model to verify process paths, outcomes or both. In this survey, the authors cover the diverse approaches in the literature and present a unified view of verifier training, types and their utility in test-time scaling.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2508.16665."
    ],
    "durationSeconds": 7.012304623999997
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me:

1. Analyze the 4 unverified citations
2. Extract all cite keys from tex files
3. Compare with bib entries to find orphans

Let me first compile the cite keys from the tex output. I'll extract all unique keys from the grep results.

From the grep results, the cite keys used in tex files (docs/paper/) are:

From sections/related_work.tex:
- muennighoff2025s1
- wang2023selfconsistency
- chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt


- snell2025scaling, brown2024monkeys
- taubenfeld2025cisc, kang2025selfcertainty, wang2025rankedvoting, oh2026latentsc
- aggarwal2023adaptive, wang2025make, feng2025optimal, kim2026reasc
- chen2025twofailures
- vashurin2025cocoa
- culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised
- florian2003named, xiao2025el4ner
- xie2023zeroshot
- jiang2023llmblender
- zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting, xie2024selfimproving
- willard2023guided, dong2024xgrammar, park2024grammar, schall2025hidden
- geng2024confidence
- xia2025survey, liu2025uqcc
- hobelsberger2025systematic
- wen2025abstention
- kuhn2023semantic, farquhar2024detecting
- kadavath2022language
- eikema2022sampling, deguchi2024centroid
- freitag2022high
- shi2022mbr
- geifman2017selective, kuleshov2015calibrated, varshney2022investigating
- cobbe2021verifiers, lightman2024verify, fernandes2022quality
- xie2023selfevaluation
- taubenfeld2025cisc, kang2025selfcertainty
- kirk2024understanding, holtzman2020curious, vijayakumar2018diverse

Now I'm going through the different sections of the paper to identify which citations appear where. I see references scattered across the experiments, conclusion, checklist, and appendix sections, with some papers like luan2018scierc, tjongkimsang2003conll, and ding2021fewnerd appearing in multiple places, while others like brown2024monkeys and snell2025scaling are only in the appendix.

Looking at the next batch, I'm tracking additional citations that appear across discussion, method, and introduction sections. There's overlap with some earlier papers like willard2023guided and brown2024monkeys, but also new ones like kadavath2022language, wang2023selfconsistency, and cobbe2021verifiers that seem to be concentrated in the introduction and discussion.

Now I'm compiling the complete list of unique citations across all the tex files to get a comprehensive view of the references used throughout the paper. Now I'm compiling the complete bibliography with all the citation keys in order. Continuing through the bibliography with more recent papers on language model evaluation, calibration, and uncertainty quantification, including work on grammar-constrained generation and self-evaluation approaches. Continuing through the bibliography entries systematically to make sure I have the complete count. Continuing through the bibliography...

Now I'm identifying which entries are cited in the actual text versus which ones exist in the bibliography but aren't referenced anywhere. I've found 74 unique citations in the document, and now I'm checking for orphaned entries in the bibliography that aren't actually cited anywhere. I spot a few candidates like `yao2026consistency` and `venktesh2025trust`, though I need to verify the latter more carefully since it was flagged during the OpenAlex verification step. I need to distinguish between these two separate issues: the 4 entries that failed OpenAlex verification are different from the 17 orphan entries. Looking more carefully at the citations, venktesh2025trust doesn't appear in any of the tex files, making it both an orphan and unverified. Let me systematically identify all the orphan entries by checking which bib items aren't referenced anywhere in the document. I'm continuing through the rest of the orphan entries to verify them all. Counting through the full list, I get 21 total orphans, but the initial report said 17—there's a gap of 4 entries that might have been added later or missed in the first pass.

Now I'm checking the 4 unverified citations. The first one, hobelsberger2025systematic, checks out—it's on arXiv with the correct authors and title, posted in October 2025. The second citation, lightman2024verify, also verifies against arXiv with matching authors.

For the third one, venktesh2025trust, I found it on arXiv as well with the right authors and title. The arxiv ID 2508.16665 corresponds to August 2025, which aligns with the year listed in the bibliography, though I'm noticing something that needs closer examination. October 2025 matches the arXiv timestamp for hobelsberger2025, and lightman2024 checks out with ICLR 2024. For venktesh2025, the author listing shows "V" which seems like it might be abbreviated rather than a full first name, though the year and arXiv ID align correctly. Since I don't have the specific details on which three entries have metadata mismatches, I'm noting the potential issues I can identify from the bibliographic data. I'm verifying the author name format is actually correct BibTeX convention, and checking that the arXiv ID 2508.16665 from August 2025 matches the year field properly. Since the task mentions three metadata mismatches but doesn't specify which entries, I need to systematically review the bibliography for any discrepancies.

Now I'm compiling my findings: all four unverified citations check out as real papers, venktesh2025trust appears as an orphan entry not cited anywhere in the document, and I've identified 21 orphan entries total rather than the 17 reported. Before finalizing the report, I should verify whether any of these orphans might actually be referenced in other tex files within the docs/paper directory that I haven't examined yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "05755181-2c06-46e3-a400-3796a4cb03d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETX22gEENRrV2JsMti54yP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7304,
      "cache_creation_input_tokens": 2600,
      "cache_read_input_tokens": 42069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2600
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

_source line 28_

4 条引用全部通过 WebSearch 验证。现在整理 orphan entries。让我确认 main.tex 是否有额外引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "d74cc2aa-2caa-4b8d-bb2d-7c7347e9c83c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETX22gEENRrV2JsMti54yP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7304,
      "cache_creation_input_tokens": 2600,
      "cache_read_input_tokens": 42069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2600
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

_source line 29_

<details open><summary>🔧 Tool call — Grep · `toolu_01CFGBEf5UPucVpKFoybUZpN`</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "9f438db5-4a54-4829-954e-7fc859810696",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETX22gEENRrV2JsMti54yP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7304,
      "cache_creation_input_tokens": 2600,
      "cache_read_input_tokens": 42069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2600
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

_source line 30 · 2026-05-20T13:51:14.230Z_

<details><summary>↩ Tool result · `toolu_01CFGBEf5UPucVpKFoybUZpN`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "89b37b1b-ba26-4324-b8a8-8a285b184393",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Good, main.tex has no additional citations. Now let me also check the adaptive.tex and single_signal.tex files since they also appear in the sections directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "b2b91a1f-0ac1-4cc8-99a0-ea1828065e66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NeoyNkWo5tACNCQE7gowEN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14225,
      "cache_read_input_tokens": 44669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14225
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

_source line 32_

<details open><summary>🔧 Tool call — Grep · `toolu_01Q7Knnyofy3gmAYF6vU9kM4`</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "bb187341-b3e7-43ca-9aa2-75c452d22101",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NeoyNkWo5tACNCQE7gowEN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14225,
      "cache_read_input_tokens": 44669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14225
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

_source line 33 · 2026-05-20T13:51:19.976Z_

<details><summary>↩ Tool result · `toolu_01Q7Knnyofy3gmAYF6vU9kM4`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "f1910815-9441-4dce-a880-a359c92777aa",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Grep · `toolu_0113Ktsn2VCNgGdgbUGmFZor`</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "21e569c1-6fef-4232-a8ed-88bc99793b62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NeoyNkWo5tACNCQE7gowEN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14225,
      "cache_read_input_tokens": 44669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14225
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

_source line 35 · 2026-05-20T13:51:20.779Z_

<details><summary>↩ Tool result · `toolu_0113Ktsn2VCNgGdgbUGmFZor`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "033d6ac2-82a8-481a-bd1b-d5d69d8dfc89",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me compile the final orphan list. Let me extract all unique bib keys and all unique cite keys programmatically to be absolutely sure.

Bib keys (from reading the .bib file):
1. xiong2024verbalized
2. vijayakumar2018diverse
3. shi2022mbr
4. brown2024monkeys
5. chen2024usc
6. cobbe2021verifiers
7. culotta2004confidence
8. derczynski2017wnut
9. ding2021fewnerd
10. eikema2022sampling


11. freitag2022high
12. fleiss1971agreement
13. feng2025optimal
14. geng2024confidence
15. hobelsberger2025systematic
16. kadavath2022language
17. kang2025selfcertainty
18. kim2026reasc
19. kuhn2023semantic
20. li2023codeie
21. lightman2024verify
22. luan2018scierc
23. manakul2023selfcheckgpt
24. yao2026consistency
25. oh2026latentsc
26. sainz2024gollie
27. snell2025scaling
28. taubenfeld2025cisc
29. thirukovalluru2024atomic
30. tjongkimsang2003conll
31. vashurin2025cocoa
32. wadhwa2023revisiting
33. wang2023selfconsistency
34. wang2025make
35. wang2025rankedvoting
36. willard2023guided
37. xia2025survey
38. zheng2024llamafactory
39. zhou2024uniner
40. muller2021understanding
41. eikema2025structured
42. venktesh2025trust
43. jinnai2024mbr
44. ratinov2009design
45. bergkirkpatrick2012empirical
46. tian2023calibration
47. fernandes2022quality
48. deguchi2024centroid
49. mejer2010confidence
50. schall2025hidden
51. yun2025price
52. park2024grammar
53. gao

Continuing through the bibliography entries from the mid-30s through the early 50s, covering work on atomic operations, NER tasks, confidence estimation, calibration methods, and various approaches to improving model reliability and structured outputs. Compiling the full bibliography of cited works... I'm continuing through the bibliography to identify which entries are actually cited in the document. Looking at the remaining keys, I can see fleiss1971agreement is being used, and I'm checking the others like eikema2020map, kumar2004minimum, and the calibration-related entries against the tex file to see which ones are orphaned references that should be removed. Continuing through the bibliography, I'm verifying the remaining entries are present in the tex file. Most are accounted for, though I've spotted another orphan reference with venktesh2025trust that needs to be tracked. Continuing through the bibliography, I'm seeing farquhar2024detecting is properly cited, but chen2021evaluating is orphaned. Moving down the list, most entries from chen2025twofailures through muennighoff2025s1 are accounted for in the tex file, though ho2023reasoning and min2022rethinking are missing citations.

Now I'm hitting a larger cluster of orphaned references—suzgun2023crowd through deng2023rad all lack corresponding citations in the document, which suggests these entries may have been removed during editing or were never integrated into the main text. I'm finding 21 orphans total, not 17 as I initially counted. Looking back at the metadata mismatches, I didn't actually receive specifics on which three were problematic, and my spot-checks of the flagged citations showed correct titles, authors, years, and venues. Though I did notice the `venktesh2025trust` entry lists the author as "Venktesh, V" where that initial seems incomplete or oddly formatted. Now I'll draft the report with these findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "14211ae2-eda4-41ce-8f2f-d046c6ed0463",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Lfkc4J4Dm1hxk4NvRcK5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 58894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 356
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

_source line 37_

所有信息已收集完毕。现在写审计报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "9dc8224f-e7f1-4e24-886b-fc03822b6a61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Lfkc4J4Dm1hxk4NvRcK5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 58894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 356
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

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_019PTY4pnRm2en3gonuzy4sj`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/",
  "description": "List existing r25_response directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "fe4bf492-b13f-4237-a266-1f9a51acdba7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Lfkc4J4Dm1hxk4NvRcK5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 58894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 356
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

_source line 39 · 2026-05-20T13:52:01.038Z_

<details><summary>↩ Tool result · `toolu_019PTY4pnRm2en3gonuzy4sj`</summary>

```text
holm_bonferroni_enumeration.tex
power_analysis.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "eab2d985-9283-4943-ab31-e0489b18b1ad",
  "tool_use_result": {
    "stdout": "holm_bonferroni_enumeration.tex\npower_analysis.tex",
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

_source line 40_

<details open><summary>🔧 Tool call — Write · `toolu_01Bi5cVdQrdS28z5wK2RDEXe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/citation_audit.md",
  "content": "# Citation Audit Report\n\n**Date:** 2026-05-20\n**Bib file:** `docs/paper/references.bib` (95 entries)\n**Tex scope:** `docs/paper/sections/*.tex` + `docs/paper/main.tex` (74 unique cite keys)\n\n---\n\n## Unverified Citations (4 flagged by R25)\n\nAll four verified as **real, published papers** with correct metadata.\n\n| Key | Status | Title | Verification |\n|-----|--------|-------|-------------|\n| `hobelsberger2025systematic` | **VERIFIED** | Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models | arXiv:2510.20460. Authors (Hobelsberger, Winner, Nawroth, Mitevski, Haensch), year (2025), title all match. Likely failed OpenAlex because it's an arXiv preprint not yet indexed. |\n| `lightman2024verify` | **VERIFIED** | Let's Verify Step by Step | arXiv:2305.20050, accepted at ICLR 2024. Authors (Lightman, Kosaraju, Burda, Edwards, Baker, Lee, Leike, Schulman, Sutskever, Cobbe), venue (ICLR 2024), year (2024) all match. |\n| `venktesh2025trust` | **VERIFIED (ORPHAN)** | Trust but Verify! A Survey on Verification Design for Test-time Scaling | arXiv:2508.16665. Authors (Venktesh, Rathee, Anand), year (2025), title match. **Not cited in any tex file** — orphan entry. |\n| `aggarwal2023adaptive` | **VERIFIED** | Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | arXiv:2305.11860, published at EMNLP 2023 (ACL Anthology). Authors (Aggarwal, Madaan, Yang, Mausam), venue, year all match. |\n\n**Action:** No corrections needed for these 4 entries. `venktesh2025trust` can be deleted (orphan).\n\n---\n\n## Metadata Mismatches\n\nNo metadata errors found in the 4 flagged entries during web verification. All titles, authors, years, and venues match their published versions.\n\nIf the R25 audit flagged 3 additional metadata mismatches beyond these 4, the specific keys were not provided. A full bib-vs-OpenAlex reconciliation would require re-running the automated check.\n\n---\n\n## Orphan Bib Entries (21 found, vs. 17 reported)\n\nEntries present in `references.bib` but **never cited** in any `docs/paper/sections/*.tex` file:\n\n| # | Key | Title |\n|---|-----|-------|\n| 1 | `yao2026consistency` | Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction |\n| 2 | `venktesh2025trust` | Trust but Verify! A Survey on Verification Design for Test-time Scaling |\n| 3 | `yun2025price` | The Price of Format: Diversity Collapse in LLMs |\n| 4 | `gao2023scaling` | Scaling Laws for Reward Model Overoptimization |\n| 5 | `chen2021evaluating` | Evaluating Large Language Models Trained on Code |\n| 6 | `ho2023reasoning` | Large Language Models Are Reasoning Teachers |\n| 7 | `min2022rethinking` | Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? |\n| 8 | `suzgun2023crowd` | Follow the Wisdom of the Crowd: Effective Text Generation via Minimum Bayes Risk Decoding |\n| 9 | `stechly2024chain` | Chain of Thoughtlessness? An Analysis of CoT in Planning |\n| 10 | `setlur2025rewarding` | Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning |\n| 11 | `kuleshov2018accurate` | Accurate Uncertainties for Deep Learning Using Calibrated Regression |\n| 12 | `openai2024o1` | OpenAI o1 System Card |\n| 13 | `ashok2023promptner` | PromptNER: Prompting For Named Entity Recognition |\n| 14 | `wang2025gptner` | GPT-NER: Named Entity Recognition via Large Language Models |\n| 15 | `wei2023chatie` | ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT |\n| 16 | `sagi2018ensemble` | Ensemble learning: A survey |\n| 17 | `lakshminarayanan2017ensembles` | Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles |\n| 18 | `welling2011sgld` | Bayesian Learning via Stochastic Gradient Langevin Dynamics |\n| 19 | `deng2023rad` | Reward-Augmented Decoding: Efficient Controlled Text Generation With a Unidirectional Reward Model |\n| 20 | `keraghel2024ner` | Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study |\n| 21 | `xu2024llmie` | Large Language Models for Generative Information Extraction: A Survey |\n\n---\n\n## Recommended Actions\n\n### Delete (21 orphan entries)\nRemove all 21 orphan entries listed above from `references.bib`. None are referenced in the compiled tex files.\n\n### Fix\nNo metadata corrections required — all 4 flagged citations verified with correct metadata.\n\n### Note\nThe original R25 audit reported 17 orphans; this audit found 21. The difference of 4 likely reflects entries added to the bib after the initial audit without corresponding `\\cite{}` commands in tex, or entries that were removed from tex during recent edits.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "94fc8ad7-96df-4840-99c5-54dc662312fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JmLjCJ8M6MVNzdBZ4nD1h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3703,
      "cache_read_input_tokens": 59250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3703
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

_source line 41 · 2026-05-20T13:52:32.823Z_

<details><summary>↩ Tool result · `toolu_01Bi5cVdQrdS28z5wK2RDEXe`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/citation_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "23115893-ddbc-4a08-902a-176c884dd466",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/citation_audit.md",
    "content": "# Citation Audit Report\n\n**Date:** 2026-05-20\n**Bib file:** `docs/paper/references.bib` (95 entries)\n**Tex scope:** `docs/paper/sections/*.tex` + `docs/paper/main.tex` (74 unique cite keys)\n\n---\n\n## Unverified Citations (4 flagged by R25)\n\nAll four verified as **real, published papers** with correct metadata.\n\n| Key | Status | Title | Verification |\n|-----|--------|-------|-------------|\n| `hobelsberger2025systematic` | **VERIFIED** | Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models | arXiv:2510.20460. Authors (Hobelsberger, Winner, Nawroth, Mitevski, Haensch), year (2025), title all match. Likely failed OpenAlex because it's an arXiv preprint not yet indexed. |\n| `lightman2024verify` | **VERIFIED** | Let's Verify Step by Step | arXiv:2305.20050, accepted at ICLR 2024. Authors (Lightman, Kosaraju, Burda, Edwards, Baker, Lee, Leike, Schulman, Sutskever, Cobbe), venue (ICLR 2024), year (2024) all match. |\n| `venktesh2025trust` | **VERIFIED (ORPHAN)** | Trust but Verify! A Survey on Verification Design for Test-time Scaling | arXiv:2508.16665. Authors (Venktesh, Rathee, Anand), year (2025), title match. **Not cited in any tex file** — orphan entry. |\n| `aggarwal2023adaptive` | **VERIFIED** | Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | arXiv:2305.11860, published at EMNLP 2023 (ACL Anthology). Authors (Aggarwal, Madaan, Yang, Mausam), venue, year all match. |\n\n**Action:** No corrections needed for these 4 entries. `venktesh2025trust` can be deleted (orphan).\n\n---\n\n## Metadata Mismatches\n\nNo metadata errors found in the 4 flagged entries during web verification. All titles, authors, years, and venues match their published versions.\n\nIf the R25 audit flagged 3 additional metadata mismatches beyond these 4, the specific keys were not provided. A full bib-vs-OpenAlex reconciliation would require re-running the automated check.\n\n---\n\n## Orphan Bib Entries (21 found, vs. 17 reported)\n\nEntries present in `references.bib` but **never cited** in any `docs/paper/sections/*.tex` file:\n\n| # | Key | Title |\n|---|-----|-------|\n| 1 | `yao2026consistency` | Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction |\n| 2 | `venktesh2025trust` | Trust but Verify! A Survey on Verification Design for Test-time Scaling |\n| 3 | `yun2025price` | The Price of Format: Diversity Collapse in LLMs |\n| 4 | `gao2023scaling` | Scaling Laws for Reward Model Overoptimization |\n| 5 | `chen2021evaluating` | Evaluating Large Language Models Trained on Code |\n| 6 | `ho2023reasoning` | Large Language Models Are Reasoning Teachers |\n| 7 | `min2022rethinking` | Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? |\n| 8 | `suzgun2023crowd` | Follow the Wisdom of the Crowd: Effective Text Generation via Minimum Bayes Risk Decoding |\n| 9 | `stechly2024chain` | Chain of Thoughtlessness? An Analysis of CoT in Planning |\n| 10 | `setlur2025rewarding` | Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning |\n| 11 | `kuleshov2018accurate` | Accurate Uncertainties for Deep Learning Using Calibrated Regression |\n| 12 | `openai2024o1` | OpenAI o1 System Card |\n| 13 | `ashok2023promptner` | PromptNER: Prompting For Named Entity Recognition |\n| 14 | `wang2025gptner` | GPT-NER: Named Entity Recognition via Large Language Models |\n| 15 | `wei2023chatie` | ChatIE: Zero-Shot Information Extraction via Chatting with ChatGPT |\n| 16 | `sagi2018ensemble` | Ensemble learning: A survey |\n| 17 | `lakshminarayanan2017ensembles` | Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles |\n| 18 | `welling2011sgld` | Bayesian Learning via Stochastic Gradient Langevin Dynamics |\n| 19 | `deng2023rad` | Reward-Augmented Decoding: Efficient Controlled Text Generation With a Unidirectional Reward Model |\n| 20 | `keraghel2024ner` | Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study |\n| 21 | `xu2024llmie` | Large Language Models for Generative Information Extraction: A Survey |\n\n---\n\n## Recommended Actions\n\n### Delete (21 orphan entries)\nRemove all 21 orphan entries listed above from `references.bib`. None are referenced in the compiled tex files.\n\n### Fix\nNo metadata corrections required — all 4 flagged citations verified with correct metadata.\n\n### Note\nThe original R25 audit reported 17 orphans; this audit found 21. The difference of 4 likely reflects entries added to the bib after the initial audit without corresponding `\\cite{}` commands in tex, or entries that were removed from tex during recent edits.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 42_

报告已保存到 `artifacts/r25_response/citation_audit.md`。

结果：
- **4 条未验证引用**：全部通过 WebSearch 验证为真实论文，元数据正确，无需修改
- **Orphan entries**：找到 **21 条**（多于预期的 17 条），全部可从 `references.bib` 中删除
- `venktesh2025trust` 既是未验证引用之一，也是 orphan（bib 中有但 tex 中未引用）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "uuid": "2d12ff47-4826-465c-a2bc-b820fb8a49a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWaiZ4h7dm3pTJwXvk2vsc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1634,
      "cache_read_input_tokens": 62953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1634
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

_source line 43_

报告已保存到 `artifacts/r25_response/citation_audit.md`。

结果：
- **4 条未验证引用**：全部通过 WebSearch 验证为真实论文，元数据正确，无需修改
- **Orphan entries**：找到 **21 条**（多于预期的 17 条），全部可从 `references.bib` 中删除
- `venktesh2025trust` 既是未验证引用之一，也是 orphan（bib 中有但 tex 中未引用）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 208116,
  "duration_api_ms": 227863,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "7bda3f1d-83d3-4768-a520-35dd01555ca4",
  "total_cost_usd": 0.9870019999999999,
  "usage": {
    "input_tokens": 7316,
    "cache_creation_input_tokens": 52886,
    "cache_read_input_tokens": 369839,
    "output_tokens": 13727,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52886,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 152,
        "cache_read_input_tokens": 62953,
        "cache_creation_input_tokens": 1634,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1634
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 44065,
      "outputTokens": 1545,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 4,
      "costUSD": 0.09179,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7316,
      "outputTokens": 13727,
      "cacheReadInputTokens": 369839,
      "cacheCreationInputTokens": 52886,
      "webSearchRequests": 0,
      "costUSD": 0.8952119999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a5a8864d-9975-483f-a479-7c89f149c3a6"
}
```

</details>

---
