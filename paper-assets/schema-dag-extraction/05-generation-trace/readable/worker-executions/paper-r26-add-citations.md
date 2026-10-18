# paper r26 add citations

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_paper_r26_add_citations_20260522T055417.log`
- **Structured JSON:** [`2bacf954c422f5cb6aa1.json`](../../sessions/2b/2bacf954c422f5cb6aa1.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
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
  "uuid": "bd817838-980b-4549-a622-f955e3144b1e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1779438000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "dc7913f6-b44d-4a17-83eb-c3554cd11f97",
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc"
}
```

---

### Assistant

_source line 4_

Let me find the paper files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "48280901-fec4-447f-b3ef-139767c245ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jysmtmvpr9UZexVZ3p6U7J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12335,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12335
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

<details open><summary>🔧 Tool call — Glob · `toolu_01XpW2m6NBqpNKTEtx6ZK7rX`</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "69d7c9b0-9cd7-41d4-bb07-fa727447a069",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jysmtmvpr9UZexVZ3p6U7J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12335,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12335
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

_source line 6 · 2026-05-22T05:54:30.458Z_

<details><summary>↩ Tool result · `toolu_01XpW2m6NBqpNKTEtx6ZK7rX`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "5f3ad220-a196-4474-b4be-c2f09920927b",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 26,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01MxNwPgSs3Efkgydnd1hTvd`</summary>

```json
{
  "pattern": "**/related_work.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "6fe9ca6c-c1db-40b1-b20a-f3425344286d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jysmtmvpr9UZexVZ3p6U7J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12335,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12335
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

_source line 8 · 2026-05-22T05:54:30.712Z_

<details><summary>↩ Tool result · `toolu_01MxNwPgSs3Efkgydnd1hTvd`</summary>

```text
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "26d57964-fc32-4b21-b7f8-75fac3e52c59",
  "tool_use_result": {
    "filenames": [
      "docs/paper/related_work.tex"
    ],
    "durationMs": 26,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01LYNctNq6z4HuNBU4yTHtyV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "2874f360-71e3-45a7-a1c0-2b35197d7b27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vajp7ViedAGPYjpjpArg5M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 24176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_014SqUjU6qPNjeyjgWLz3D7g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "3ce0e99d-73c5-40cc-ad38-6ac7158aa78f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vajp7ViedAGPYjpjpArg5M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 24176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 11 · 2026-05-22T05:54:33.708Z_

<details><summary>↩ Tool result · `toolu_014SqUjU6qPNjeyjgWLz3D7g`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	\looseness=-1
6	Training-free LLM IE spans instruction tuning \citep{instructuie-2023}, code-style schema encoding \citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \citep{gollie-2024,adelie-2024}, schema-driven decoding \citep{slot-2025,oneke-2025}, and constrained JSON decoding \citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \citep{uniner-2024}, and bidirectional encoders \citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \citep{relationprompt-2022}, constrained generation \citep{josifoski-2022-genie}, and shared embedding spaces \citep{boylan-2025-glirel,wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.
7	
8	\paragraph{Schema complexity in IE.}
9	\looseness=-1
10	The most directly related work is LLM-PEE \citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21; \S\ref{sec:sdgd}). In short, LLM-PEE assumes decomposition helps; we show why it should (confusability), why it does not (merge amplification), and what predicts the degradation (BCS). Other approaches address schema complexity via hard negative mining \citep{iepile-2024}, schema definition optimization \citep{parse-2025}, multi-agent debate \citep{crossagentie-2025,cmas-ner-2025}, and active prompting \citep{reflect-learn-2026}; all treat it as an engineering problem rather than isolating degradation factors. Concurrently, \citet{chen-2026-multi-instance} show that instance count degrades LLM multi-instance processing more than context length, consistent with our count-dominant finding. \citet{golde-2025-familiarity} quantify training--evaluation type similarity to predict zero-shot NER difficulty; our SCS instead measures within-schema inter-type confusability without assuming access to training data. Label-space reduction approaches \citep{haystack-to-needle-2025,dlisc-2025,spt-2025} implicitly lower batch confusability---our framework explains \emph{why} such reduction works.
11	
12	\paragraph{Schema complexity in dialogue and IE.}
13	\looseness=-1
14	The Schema-Guided Dialogue dataset~\citep{rastogi2020towards} and SGD-X~\citep{lee2022sgd} document degradation with schema linguistic variation; \citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. The relationship between label similarity and confusion has precedent in visual recognition \citep{dubey-2018-pairwise-confusion}, correlated label noise \citep{collier-2021-correlated-noise}, hierarchical classification \citep{deng-2010-imagenet}, and label confusion matrices \citep{guo-2021-label-confusion,muller2019when,peterson2019human}.
15	
16	\paragraph{SCS novelty.}
17	\looseness=-1
18	SCS inherits the embedding-similarity criterion from LLM-PEE \citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \citep{snell2017prototypical} and zero-shot classification \citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\%) compounds at the ecological batch level to explain ${\sim}$22\% of cross-batch RE variance on FewRel (\S\ref{sec:bcs_controlled}).
19	
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "005e4350-28fb-4c7e-97e6-cf8bc49c482b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\n\\looseness=-1\nTraining-free LLM IE spans instruction tuning \\citep{instructuie-2023}, code-style schema encoding \\citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \\citep{gollie-2024,adelie-2024}, schema-driven decoding \\citep{slot-2025,oneke-2025}, and constrained JSON decoding \\citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \\citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \\citep{uniner-2024}, and bidirectional encoders \\citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \\citep{relationprompt-2022}, constrained generation \\citep{josifoski-2022-genie}, and shared embedding spaces \\citep{boylan-2025-glirel,wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.\n\n\\paragraph{Schema complexity in IE.}\n\\looseness=-1\nThe most directly related work is LLM-PEE \\citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\\to$0.21; \\S\\ref{sec:sdgd}). In short, LLM-PEE assumes decomposition helps; we show why it should (confusability), why it does not (merge amplification), and what predicts the degradation (BCS). Other approaches address schema complexity via hard negative mining \\citep{iepile-2024}, schema definition optimization \\citep{parse-2025}, multi-agent debate \\citep{crossagentie-2025,cmas-ner-2025}, and active prompting \\citep{reflect-learn-2026}; all treat it as an engineering problem rather than isolating degradation factors. Concurrently, \\citet{chen-2026-multi-instance} show that instance count degrades LLM multi-instance processing more than context length, consistent with our count-dominant finding. \\citet{golde-2025-familiarity} quantify training--evaluation type similarity to predict zero-shot NER difficulty; our SCS instead measures within-schema inter-type confusability without assuming access to training data. Label-space reduction approaches \\citep{haystack-to-needle-2025,dlisc-2025,spt-2025} implicitly lower batch confusability---our framework explains \\emph{why} such reduction works.\n\n\\paragraph{Schema complexity in dialogue and IE.}\n\\looseness=-1\nThe Schema-Guided Dialogue dataset~\\citep{rastogi2020towards} and SGD-X~\\citep{lee2022sgd} document degradation with schema linguistic variation; \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. The relationship between label similarity and confusion has precedent in visual recognition \\citep{dubey-2018-pairwise-confusion}, correlated label noise \\citep{collier-2021-correlated-noise}, hierarchical classification \\citep{deng-2010-imagenet}, and label confusion matrices \\citep{guo-2021-label-confusion,muller2019when,peterson2019human}.\n\n\\paragraph{SCS novelty.}\n\\looseness=-1\nSCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \\citep{snell2017prototypical} and zero-shot classification \\citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain ${\\sim}$22\\% of cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).\n\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T05:54:33.782Z_

<details><summary>↩ Tool result · `toolu_01LYNctNq6z4HuNBU4yTHtyV`</summary>

```text
1	@inproceedings{golde-2025-familiarity,
2	  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},
3	  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},
4	  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
5	  year      = {2025},
6	  url       = {https://arxiv.org/abs/2412.10121}
7	}
8	
9	@book{cohen-1988-statistical,
10	  author    = {Cohen, Jacob},
11	  title     = {Statistical Power Analysis for the Behavioral Sciences},
12	  edition   = {2nd},
13	  publisher = {Lawrence Erlbaum Associates},
14	  year      = {1988}
15	}
16	
17	@inproceedings{baan-2023-ecological,
18	  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},
19	  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},
20	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
21	  year      = {2023}
22	}
23	
24	@inproceedings{josifoski-2022-genie,
25	  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
26	  title     = {{GenIE}: Generative Information Extraction},
27	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
28	  pages     = {4626--4643},
29	  year      = {2022}
30	}
31	
32	@inproceedings{dubey-2018-pairwise-confusion,
33	  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},
34	  title     = {Pairwise Confusion for Fine-Grained Visual Classification},
35	  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},
36	  pages     = {71--88},
37	  year      = {2018}
38	}
39	
40	@inproceedings{collier-2021-correlated-noise,
41	  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},
42	  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},
43	  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
44	  pages     = {1551--1560},
45	  year      = {2021}
46	}
47	
48	@inproceedings{yin-2019-zero-shot-bench,
49	  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},
50	  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},
51	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
52	  pages     = {3914--3923},
53	  year      = {2019},
54	  url       = {https://arxiv.org/abs/1909.00161}
55	}
56	
57	@article{schuirmann-1987-tost,
58	  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},
59	  author    = {Schuirmann, Donald J.},
60	  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},
61	  volume    = {15},
62	  number    = {6},
63	  pages     = {657--680},
64	  year      = {1987},
65	  doi       = {10.1007/BF01068419}
66	}
67	
68	@article{gemini-2025,
69	  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},
70	  author    = {{Gemini Team}},
71	  journal   = {arXiv preprint arXiv:2507.06261},
72	  year      = {2025},
73	  url       = {https://arxiv.org/abs/2507.06261}
74	}
75	
76	@inproceedings{snell2017prototypical,
77	  title     = {Prototypical Networks for Few-shot Learning},
78	  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},
79	  booktitle = {Advances in Neural Information Processing Systems},
80	  volume    = {30},
81	  year      = {2017}
82	}
83	
84	@inproceedings{muller2019when,
85	  title     = {When Does Label Smoothing Help?},
86	  author    = {M{\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},
87	  booktitle = {Advances in Neural Information Processing Systems},
88	  volume    = {32},
89	  year      = {2019}
90	}
91	
92	@inproceedings{peterson2019human,
93	  title     = {Human Uncertainty Makes Classification More Robust},
94	  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},
95	  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},
96	  pages     = {9617--9626},
97	  year      = {2019}
98	}
99	
100	@article{willard2023efficient,
101	  title     = {Efficient Guided Generation for Large Language Models},
102	  author    = {Willard, Brandon T. and Louf, R{\'e}mi},
103	  journal   = {arXiv preprint arXiv:2307.09702},
104	  year      = {2023},
105	  url       = {https://arxiv.org/abs/2307.09702}
106	}
107	
108	
109	
110	% =============================================================================
111	% DIRECT COMPETITORS
112	% =============================================================================
113	
114	@inproceedings{llm-pee-2025,
115	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
116	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
117	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
118	    year      = {2025},
119	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
120	}
121	
122	@inproceedings{parse-2025,
123	    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
124	    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
125	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
126	    year      = {2025},
127	    url       = {https://aclanthology.org/2025.emnlp-industry.184/},
128	}
129	
130	@inproceedings{crossagentie-2025,
131	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
132	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
133	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
134	    year      = {2025},
135	    url       = {https://aclanthology.org/2025.findings-acl.718/},
136	}
137	
138	
139	@inproceedings{cmas-ner-2025,
140	    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},
141	    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},
142	    booktitle = {Proceedings of the ACM Web Conference 2025},
143	    year      = {2025},
144	    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},
145	    doi       = {10.1145/3696410.3714923},
146	}
147	
148	% =============================================================================
149	% METHOD COMPONENTS
150	% =============================================================================
151	
152	@inproceedings{uniner-2024,
153	    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
154	    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
155	    booktitle = {International Conference on Learning Representations},
156	    year      = {2024},
157	    url       = {https://arxiv.org/abs/2308.03279},
158	}
159	
160	@inproceedings{gollie-2024,
161	    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
162	    author    = {Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},
163	    booktitle = {International Conference on Learning Representations},
164	    year      = {2024},
165	    url       = {https://arxiv.org/abs/2310.03668},
166	}
167	
168	@inproceedings{gliner-2024,
169	    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},
170	    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},
171	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
172	    year      = {2024},
173	    url       = {https://arxiv.org/abs/2311.08526},
174	}
175	
176	@inproceedings{gliner2-2025,
177	    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},
178	    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},
179	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
180	    year      = {2025},
181	    url       = {https://aclanthology.org/2025.emnlp-demos.10/},
182	}
183	
184	
185	@inproceedings{iepile-2024,
186	    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},
187	    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},
188	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
189	    pages     = {127--146},
190	    year      = {2024},
191	    url       = {https://aclanthology.org/2024.acl-short.13/},
192	}
193	
194	
195	@inproceedings{dror-2018-significance,
196	    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},
197	    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},
198	    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},
199	    year      = {2018},
200	    url       = {https://aclanthology.org/P18-1128/},
201	}
202	
203	@article{lost-in-middle-2024,
204	    title   = {Lost in the Middle: How Language Models Use Long Contexts},
205	    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},
206	    journal = {Transactions of the Association for Computational Linguistics},
207	    volume  = {12},
208	    pages   = {157--173},
209	    year    = {2024},
210	    url     = {https://arxiv.org/abs/2307.03172},
211	    doi     = {10.1162/tacl_a_00638},
212	}
213	
214	% =============================================================================
215	% ZERO-SHOT NER / RE BASELINES
216	% =============================================================================
217	
218	
219	
220	% =============================================================================
221	% EVALUATION / BENCHMARKING
222	% =============================================================================
223	
224	% =============================================================================
225	% SURVEYS / BACKGROUND
226	% =============================================================================
227	
228	@article{llm4ie-survey-2024,
229	    title   = {Large Language Models for Generative Information Extraction: A Survey},
230	    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},
231	    journal = {Frontiers of Computer Science},
232	    volume  = {18},
233	    number  = {6},
234	    year    = {2024},
235	    url     = {https://arxiv.org/abs/2312.17617},
236	    doi     = {10.1007/s11704-024-40555-y},
237	}
238	
239	@inproceedings{knowcoder-2024,
240	    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},
241	    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
242	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
243	    year      = {2024},
244	    url       = {https://arxiv.org/abs/2403.07969},
245	}
246	
247	@inproceedings{slot-2025,
248	    title     = {{SLOT}: Structuring the Output of Large Language Models},
249	    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},
250	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
251	    year      = {2025},
252	    url       = {https://aclanthology.org/2025.emnlp-industry.32/},
253	}
254	
255	% =============================================================================
256	% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION
257	% =============================================================================
258	
259	
260	@inproceedings{ethayarajh-contextual-2019,
261	    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},
262	    author    = {Ethayarajh, Kawin},
263	    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},
264	    year      = {2019},
265	    url       = {https://aclanthology.org/D19-1006/},
266	}
267	
268	@inproceedings{cai-isotropy-clusters-2021,
269	    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},
270	    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},
271	    booktitle = {International Conference on Learning Representations},
272	    year      = {2021},
273	    url       = {https://openreview.net/forum?id=xYGNO86OWDH},
274	}
275	
276	
277	% =============================================================================
278	% ADDITIONAL REFERENCES (from references_survey.md only)
279	% =============================================================================
280	
281	@article{instructuie-2023,
282	    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
283	    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
284	    journal = {arXiv preprint arXiv:2304.08085},
285	    year    = {2023},
286	    url     = {https://arxiv.org/abs/2304.08085},
287	}
288	
289	@inproceedings{codeie-2023,
290	    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
291	    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
292	    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
293	    year      = {2023},
294	    url       = {https://aclanthology.org/2023.acl-long.855/},
295	}
296	
297	@inproceedings{adelie-2024,
298	    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},
299	    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},
300	    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
301	    year      = {2024},
302	    url       = {https://aclanthology.org/2024.emnlp-main.419/},
303	}
304	
305	@inproceedings{oneke-2025,
306	    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},
307	    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},
308	    booktitle = {Companion Proceedings of the ACM Web Conference 2025},
309	    year      = {2025},
310	    url       = {https://arxiv.org/abs/2412.20005},
311	    doi       = {10.1145/3701716.3715189},
312	}
313	
314	
315	
316	
317	% =============================================================================
318	% DATASETS
319	% =============================================================================
320	
321	@inproceedings{fewnerd-2021,
322	    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},
323	    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},
324	    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},
325	    year      = {2021},
326	    url       = {https://aclanthology.org/2021.acl-long.248/},
327	}
328	
329	@inproceedings{fewrel-2018,
330	    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},
331	    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},
332	    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
333	    year      = {2018},
334	    url       = {https://aclanthology.org/D18-1514/},
335	}
336	
337	@inproceedings{maven-2020,
338	    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},
339	    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},
340	    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
341	    year      = {2020},
342	    url       = {https://aclanthology.org/2020.emnlp-main.129/},
343	}
344	
345	@inproceedings{docred-2019,
346	    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
347	    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
348	    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
349	    year      = {2019},
350	    url       = {https://aclanthology.org/P19-1074/},
351	}
352	
353	% =============================================================================
354	% MODELS AND TOOLS
355	% =============================================================================
356	
357	@article{qwen3-2025,
358	    title   = {Qwen3 Technical Report},
359	    author  = {{Qwen Team}},
360	    journal = {arXiv preprint arXiv:2505.09388},
361	    year    = {2025},
362	    url     = {https://arxiv.org/abs/2505.09388},
363	}
364	
365	@article{llama3-2024,
366	    title   = {The {Llama} 3 Herd of Models},
367	    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},
368	    journal = {arXiv preprint arXiv:2407.21783},
369	    year    = {2024},
370	    url     = {https://arxiv.org/abs/2407.21783},
371	}
372	
373	@inproceedings{sentence-bert-2019,
374	    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
375	    author    = {Reimers, Nils and Gurevych, Iryna},
376	    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
377	    year      = {2019},
378	    url       = {https://aclanthology.org/D19-1410/},
379	}
380	
381	@inproceedings{minilm-2020,
382	    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},
383	    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},
384	    booktitle = {Advances in Neural Information Processing Systems},
385	    volume    = {33},
386	    year      = {2020},
387	    url       = {https://arxiv.org/abs/2002.10957},
388	}
389	
390	@inproceedings{reflect-learn-2026,
391	    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},
392	    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},
393	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
394	    volume    = {40},
395	    pages     = {34923--34931},
396	    year      = {2026},
397	    url       = {https://arxiv.org/abs/2508.10036},
398	    doi       = {10.1609/aaai.v40i41.40796},
399	}
400	
401	@inproceedings{sclar-sensitivity-2024,
402	    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},
403	    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},
404	    booktitle = {International Conference on Learning Representations},
405	    year      = {2024},
406	    url       = {https://arxiv.org/abs/2310.11324},
407	}
408	
409	@inproceedings{vllm-2023,
410	    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},
411	    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},
412	    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},
413	    year      = {2023},
414	    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},
415	}
416	
417	@inproceedings{xie-zeroshot-ner-2023,
418	    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},
419	    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
420	    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
421	    year      = {2023},
422	    url       = {https://aclanthology.org/2023.emnlp-main.493/},
423	}
424	
425	@inproceedings{wadhwa-re-llm-2023,
426	    title     = {Revisiting Relation Extraction in the era of Large Language Models},
427	    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},
428	    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
429	    pages     = {15566--15589},
430	    year      = {2023},
431	    url       = {https://aclanthology.org/2023.acl-long.868/},
432	}
433	
434	@inproceedings{relationprompt-2022,
435	    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},
436	    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},
437	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
438	    pages     = {45--57},
439	    year      = {2022},
440	    url       = {https://aclanthology.org/2022.findings-acl.5/},
441	}
442	
443	@article{promptner-2023,
444	    title   = {{PromptNER}: Prompting For Named Entity Recognition},
445	    author  = {Ashok, Dhananjay and Lipton, Zachary C.},
446	    journal = {arXiv preprint arXiv:2305.15444},
447	    year    = {2023},
448	    url     = {https://arxiv.org/abs/2305.15444},
449	}
450	
451	@article{json-schema-bench-2025,
452	    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},
453	    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},
454	    journal = {arXiv preprint arXiv:2501.10868},
455	    year    = {2025},
456	    url     = {https://arxiv.org/abs/2501.10868},
457	}
458	
459	@inproceedings{rastogi2020towards,
460	    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},
461	    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},
462	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
463	    volume    = {34},
464	    pages     = {8689--8696},
465	    year      = {2020},
466	    url       = {https://arxiv.org/abs/1909.05855},
467	}
468	
469	@article{li2023evaluating,
470	    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},
471	    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},
472	    journal = {arXiv preprint arXiv:2304.11633},
473	    year    = {2023},
474	    url     = {https://arxiv.org/abs/2304.11633},
475	}
476	
477	@inproceedings{lee2022sgd,
478	    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},
479	    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},
480	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
481	    volume    = {36},
482	    pages     = {10938--10946},
483	    year      = {2022},
484	    url       = {https://arxiv.org/abs/2110.06800},
485	}
486	
487	@article{haystack-to-needle-2025,
488	    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},
489	    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},
490	    journal = {arXiv preprint arXiv:2502.08436},
491	    year    = {2025},
492	    url     = {https://arxiv.org/abs/2502.08436},
493	}
494	
495	@inproceedings{deng-2010-imagenet,
496	    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},
497	    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},
498	    booktitle = {Proceedings of the 11th European Conference on Computer Vision},
499	    pages     = {71--84},
500	    year      = {2010},
501	    doi       = {10.1007/978-3-642-15555-0\_6},
502	}
503	
504	@article{rothman-1990,
505	    title   = {No Adjustments Are Needed for Multiple Comparisons},
506	    author  = {Rothman, Kenneth J.},
507	    journal = {Epidemiology},
508	    volume  = {1},
509	    number  = {1},
510	    pages   = {43--46},
511	    year    = {1990},
512	    doi     = {10.1097/00001648-199001000-00010},
513	}
514	
515	@article{lakens-2017-equivalence,
516	    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},
517	    author  = {Lakens, Dani{\"e}l},
518	    journal = {Social Psychological and Personality Science},
519	    volume  = {8},
520	    number  = {4},
521	    pages   = {355--362},
522	    year    = {2017},
523	    doi     = {10.1177/1948550617697177},
524	}
525	
526	
527	@inproceedings{guo-2021-label-confusion,
528	    title     = {Label Confusion Learning to Enhance Text Classification Models},
529	    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},
530	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
531	    volume    = {35},
532	    number    = {14},
533	    pages     = {12929--12936},
534	    year      = {2021},
535	    doi       = {10.1609/aaai.v35i14.17529},
536	}
537	
538	
539	@article{dlisc-2025,
540	    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},
541	    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},
542	    journal   = {arXiv preprint arXiv:2505.14992},
543	    year      = {2025},
544	    url       = {https://arxiv.org/abs/2505.14992}
545	}
546	
547	@article{spt-2025,
548	    title     = {Schema as Parameterized Tools for Universal Information Extraction},
549	    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},
550	    journal   = {arXiv preprint arXiv:2506.01276},
551	    year      = {2025},
552	    url       = {https://arxiv.org/abs/2506.01276}
553	}
554	
555	@inproceedings{card-2020-power,
556	    title     = {With Little Power Comes Great Responsibility},
557	    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},
558	    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
559	    pages     = {9263--9274},
560	    year      = {2020},
561	    publisher = {Association for Computational Linguistics},
562	    url       = {https://aclanthology.org/2020.emnlp-main.745}
563	}
564	
565	@article{chen-2026-multi-instance,
566	    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},
567	    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},
568	    journal   = {arXiv preprint arXiv:2603.22608},
569	    year      = {2026},
570	    url       = {https://arxiv.org/abs/2603.22608}
571	}
572	
573	@article{robinson-1950-ecological,
574	    author    = {Robinson, William S.},
575	    title     = {Ecological Correlations and the Behavior of Individuals},
576	    journal   = {American Sociological Review},
577	    volume    = {15},
578	    number    = {3},
579	    pages     = {351--357},
580	    year      = {1950}
581	}
582	
583	@inproceedings{boylan-2025-glirel,
584	    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},
585	    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},
586	    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
587	    year      = {2025},
588	    address   = {Albuquerque, New Mexico},
589	    publisher = {Association for Computational Linguistics},
590	    pages     = {8230--8245},
591	    url       = {https://aclanthology.org/2025.naacl-long.418/}
592	}
593	
594	
595	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "853f61f0-8755-45e4-bbff-2c40f10038f0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
      "content": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
      "numLines": 595,
      "startLine": 1,
      "totalLines": 595
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

````text
Now I have the files. Let me analyze:

1. **references.bib**: I need to add 2 bib entries. But wait - `reflect-learn-2026` already exists at line 390! The user's task says to add `zhao-2025-reflect-learn` but there's already a `reflect-learn-2026` entry for the same paper. Let me check if the user wants a different key or if this is a duplicate.

Looking at the user's bib entry:
```
@article{zhao-2025-reflect-learn,
    title = "Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion",
    author = "Zhao, Dong and Wang, Yadong and Chen, Xiang and others",
    journal = "arXiv preprint arXiv:2508.10036",
    year = "2025",
}
```

And the existing entry (line 390-398):
```
@inproceedings{reflect-learn-2026,
    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},
    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, C
```

These appear to be the same paper with different citation keys and slightly different formatting. The user's version uses `@article` with an arXiv reference and year 2025, while the existing one is `@inproceedings` with year 2026. I should clarify whether to replace the existing entry, add both, or use a different approach. The "Reflect then Learn" paper is already in the bibliography as `reflect-learn-2026` and cited in the related work section, so I don't need to add it again. What I do need to add is the NER Retriever paper by Shachar, which is new. Let me focus on adding just that bibliography entry and its corresponding citation in the related work section. I need to add the NER Retriever citation to the bibliography and incorporate it into the related work section, then figure out where to expand on the Reflect then Learn paper using the existing citation key since that entry is already in the references. I need to be strategic about where to add these citations. The NER Retriever paper should go in the section discussing NER methods, while the Reflect then Learn expansion can use the existing `reflect-learn-2026` key that's already cited in the schema complexity paragraph. Let me identify the exact spots in the related work where these fit best—NER Retriever in the first paragraph where named entity recognition approaches are covered, and the Reflect then Learn sentence either expanding the existing citation in the second paragraph or integrated into the training-free LLM IE discussion. I'm working through where to place these new citations about transformer representations and entity retrieval. The first paragraph on training-free LLM IE seems like the right spot, especially since the user specifically pointed to that section. I should add the new sentence after the RE methods citation but before the closing statement, keeping the existing "active prompting" mention in the second paragraph since it serves a different purpose there in listing engineering approaches. I'm working through where to place these new citations naturally. The NER Retriever reference should fit right after the bidirectional encoders mention, before the semicolon that transitions to RE methods. For Reflect then Learn, it makes more sense to integrate it into the broader LLM-based IE discussion rather than the scaling limitations conclusion, so I'll add it earlier in the paragraph where the other LLM approaches are introduced.

I'll insert both sentences between the end of the methods listing and the "These methods perform well..." transition. For the bibliography, I need to add the shachar entry in the zero-shot NER section, probably right after the existing NER-related citations. I'm debating whether citing reflect-learn-2026 again here makes sense, since it's already mentioned in paragraph 2 for a different purpose. Multiple citations of the same work are fine in academic writing, especially when highlighting different contributions, so adding this more detailed connection about LLM uncertainty and extraction difficulty should work well alongside the existing reference. I need to add the NER Retriever citation to paragraph 1 where the LLM-based IE methods are discussed, and place the Reflect then Learn sentence in paragraph 1 as the user requested, even though paragraph 2 already has a citation to that paper. Let me check the main.tex file to see the current structure before making these edits.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "75fc75fc-f81f-4877-a0d2-adb4412c2195",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvWpQJLZbRr32gpawrFTjm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1303,
      "cache_creation_input_tokens": 10892,
      "cache_read_input_tokens": 24448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10892
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

`reflect-learn-2026` already exists in `references.bib` (line 390, same paper with complete AAAI proceedings info), and it's already cited in `related_work.tex` line 10. I'll only add the `shachar-2025-ner-retriever` bib entry and both expanded citation sentences (using the existing key for Reflect then Learn).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "c61288ba-a399-4880-a831-44381049a6dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvWpQJLZbRr32gpawrFTjm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1303,
      "cache_creation_input_tokens": 10892,
      "cache_read_input_tokens": 24448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10892
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

<details open><summary>🔧 Tool call — Glob · `toolu_017n9jkxiVVyLFmNshbQuuUT`</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "f4f26dfc-4362-4998-96e7-738043d3d3c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QvWpQJLZbRr32gpawrFTjm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1303,
      "cache_creation_input_tokens": 10892,
      "cache_read_input_tokens": 24448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10892
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

_source line 16 · 2026-05-22T05:55:40.031Z_

<details><summary>↩ Tool result · reported error · `toolu_017n9jkxiVVyLFmNshbQuuUT`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "90b1e892-7679-455f-b0ab-7ab03a4f33fd",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction."
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_016CPsfd3PTL6SiByCN7D38E`</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "55156bb5-e694-4154-994f-0a1b32706cdb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RjLapEy9QM42KgyP6whBj2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4985,
      "cache_read_input_tokens": 35340,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4985
      },
      "output_tokens": 62,
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

_source line 18 · 2026-05-22T05:55:43.986Z_

<details><summary>↩ Tool result · `toolu_016CPsfd3PTL6SiByCN7D38E`</summary>

```text
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "918917fc-bcb5-4cf0-aa2b-c5a67f172dda",
  "tool_use_result": {
    "filenames": [
      "docs/paper/main.tex"
    ],
    "durationMs": 31,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 19_

Now I'll make the three edits: add bib entry, add NER Retriever sentence, and add Reflect then Learn expanded sentence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "1680c0d7-d4ee-4d43-90d0-686c06db58c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdEV8MTiR7sPvZJGPJFTZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 118,
      "cache_read_input_tokens": 40325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 118
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

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_016MtzaMYWAJpQZjEcDjuAXR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================",
  "new_string": "% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "faa065f4-d8dd-4041-987e-4295dd314534",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdEV8MTiR7sPvZJGPJFTZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 118,
      "cache_read_input_tokens": 40325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 118
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

_source line 21 · 2026-05-22T05:55:50.365Z_

<details><summary>↩ Tool result · `toolu_016MtzaMYWAJpQZjEcDjuAXR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "b3ca8d2d-e4c1-403c-8c62-ec21dc2c32d5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================",
    "newString": "% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 215,
        "oldLines": 8,
        "newStart": 215,
        "newLines": 16,
        "lines": [
          " % ZERO-SHOT NER / RE BASELINES",
          " % =============================================================================",
          " ",
          "+@inproceedings{shachar-2025-ner-retriever,",
          "+    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},",
          "+    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},",
          "+    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},",
          "+    year      = {2025},",
          "+    pages     = {11175--11186},",
          "+}",
          " ",
          " ",
          "+",
          " % =============================================================================",
          " % EVALUATION / BENCHMARKING",
          " % ============================================================================="
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

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01KEqhv9TwHtPv3Dtb21QtKZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "old_string": "RE methods include zero-shot triplet extraction \\citep{relationprompt-2022}, constrained generation \\citep{josifoski-2022-genie}, and shared embedding spaces \\citep{boylan-2025-glirel,wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.",
  "new_string": "RE methods include zero-shot triplet extraction \\citep{relationprompt-2022}, constrained generation \\citep{josifoski-2022-genie}, and shared embedding spaces \\citep{boylan-2025-glirel,wadhwa-re-llm-2023}. \\citet{shachar-2025-ner-retriever} show that mid-layer transformer representations encode fine-grained type information useful for zero-shot entity retrieval, complementing our finding that embedding-based type similarity predicts extraction difficulty. \\citet{reflect-learn-2026} use introspective confusion to select in-context examples for IE; their finding that LLM uncertainty correlates with extraction difficulty aligns with our schema-complexity perspective. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "c7c00411-19ae-479e-9a8e-f6c1779406b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdEV8MTiR7sPvZJGPJFTZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 118,
      "cache_read_input_tokens": 40325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 118
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

_source line 23 · 2026-05-22T05:55:53.074Z_

<details><summary>↩ Tool result · `toolu_01KEqhv9TwHtPv3Dtb21QtKZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "537548d1-14da-480e-b487-ef027fd446e5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "oldString": "RE methods include zero-shot triplet extraction \\citep{relationprompt-2022}, constrained generation \\citep{josifoski-2022-genie}, and shared embedding spaces \\citep{boylan-2025-glirel,wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.",
    "newString": "RE methods include zero-shot triplet extraction \\citep{relationprompt-2022}, constrained generation \\citep{josifoski-2022-genie}, and shared embedding spaces \\citep{boylan-2025-glirel,wadhwa-re-llm-2023}. \\citet{shachar-2025-ner-retriever} show that mid-layer transformer representations encode fine-grained type information useful for zero-shot entity retrieval, complementing our finding that embedding-based type similarity predicts extraction difficulty. \\citet{reflect-learn-2026} use introspective confusion to select in-context examples for IE; their finding that LLM uncertainty correlates with extraction difficulty aligns with our schema-complexity perspective. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\n\\looseness=-1\nTraining-free LLM IE spans instruction tuning \\citep{instructuie-2023}, code-style schema encoding \\citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \\citep{gollie-2024,adelie-2024}, schema-driven decoding \\citep{slot-2025,oneke-2025}, and constrained JSON decoding \\citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \\citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \\citep{uniner-2024}, and bidirectional encoders \\citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \\citep{relationprompt-2022}, constrained generation \\citep{josifoski-2022-genie}, and shared embedding spaces \\citep{boylan-2025-glirel,wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.\n\n\\paragraph{Schema complexity in IE.}\n\\looseness=-1\nThe most directly related work is LLM-PEE \\citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\\to$0.21; \\S\\ref{sec:sdgd}). In short, LLM-PEE assumes decomposition helps; we show why it should (confusability), why it does not (merge amplification), and what predicts the degradation (BCS). Other approaches address schema complexity via hard negative mining \\citep{iepile-2024}, schema definition optimization \\citep{parse-2025}, multi-agent debate \\citep{crossagentie-2025,cmas-ner-2025}, and active prompting \\citep{reflect-learn-2026}; all treat it as an engineering problem rather than isolating degradation factors. Concurrently, \\citet{chen-2026-multi-instance} show that instance count degrades LLM multi-instance processing more than context length, consistent with our count-dominant finding. \\citet{golde-2025-familiarity} quantify training--evaluation type similarity to predict zero-shot NER difficulty; our SCS instead measures within-schema inter-type confusability without assuming access to training data. Label-space reduction approaches \\citep{haystack-to-needle-2025,dlisc-2025,spt-2025} implicitly lower batch confusability---our framework explains \\emph{why} such reduction works.\n\n\\paragraph{Schema complexity in dialogue and IE.}\n\\looseness=-1\nThe Schema-Guided Dialogue dataset~\\citep{rastogi2020towards} and SGD-X~\\citep{lee2022sgd} document degradation with schema linguistic variation; \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. The relationship between label similarity and confusion has precedent in visual recognition \\citep{dubey-2018-pairwise-confusion}, correlated label noise \\citep{collier-2021-correlated-noise}, hierarchical classification \\citep{deng-2010-imagenet}, and label confusion matrices \\citep{guo-2021-label-confusion,muller2019when,peterson2019human}.\n\n\\paragraph{SCS novelty.}\n\\looseness=-1\nSCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \\citep{snell2017prototypical} and zero-shot classification \\citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain ${\\sim}$22\\% of cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).\n\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Training-free LLM IE.}",
          " \\looseness=-1",
          "-Training-free LLM IE spans instruction tuning \\citep{instructuie-2023}, code-style schema encoding \\citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \\citep{gollie-2024,adelie-2024}, schema-driven decoding \\citep{slot-2025,oneke-2025}, and constrained JSON decoding \\citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \\citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \\citep{uniner-2024}, and bidirectional encoders \\citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \\citep{relationprompt-2022}, constrained generation \\citep{josifoski-2022-genie}, and shared embedding spaces \\citep{boylan-2025-glirel,wadhwa-re-llm-2023}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.",
          "+Training-free LLM IE spans instruction tuning \\citep{instructuie-2023}, code-style schema encoding \\citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \\citep{gollie-2024,adelie-2024}, schema-driven decoding \\citep{slot-2025,oneke-2025}, and constrained JSON decoding \\citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \\citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \\citep{uniner-2024}, and bidirectional encoders \\citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \\citep{relationprompt-2022}, constrained generation \\citep{josifoski-2022-genie}, and shared embedding spaces \\citep{boylan-2025-glirel,wadhwa-re-llm-2023}. \\citet{shachar-2025-ner-retriever} show that mid-layer transformer representations encode fine-grained type information useful for zero-shot entity retrieval, complementing our finding that embedding-based type similarity predicts extraction difficulty. \\citet{reflect-learn-2026} use introspective confusion to select in-context examples for IE; their finding that LLM uncertainty correlates with extraction difficulty aligns with our schema-complexity perspective. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.",
          " ",
          " \\paragraph{Schema complexity in IE.}",
          " \\looseness=-1"
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

_source line 24_

Edits done. Now compiling to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "442d0d48-b3fd-4f20-be77-cc12e6a15f39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013N49K2mMFk12YVjJMoUNds",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 40443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1020
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

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_012o9K2ippHBNWRX6GKQaiUd`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "3b5ef632-6b23-4518-b52b-836da22138fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013N49K2mMFk12YVjJMoUNds",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1020,
      "cache_read_input_tokens": 40443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1020
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

_source line 26 · 2026-05-22T05:55:59.560Z_

<details><summary>↩ Tool result · `toolu_012o9K2ippHBNWRX6GKQaiUd`</summary>

```text
s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 480819 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "af09d813-a70d-4aed-8f06-089440dc30b6",
  "tool_use_result": {
    "stdout": "s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (27 pages, 480819 bytes).\nTranscript written on main.log.",
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

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_013AbvKLxxAtVEdFJEkUNfim`</summary>

```json
{
  "command": "bibtex main 2>&1",
  "description": "Run bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "4ebf9df2-435e-488d-a3aa-befd6fb7f9bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwMCFquqQ8rfNUqtZGk21H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 900,
      "cache_read_input_tokens": 41463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 900
      },
      "output_tokens": 70,
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

_source line 28 · 2026-05-22T05:56:02.496Z_

<details><summary>↩ Tool result · `toolu_013AbvKLxxAtVEdFJEkUNfim`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
Warning--can't use both volume and number fields in guo-2021-label-confusion
(There was 1 warning)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "a84afd98-eba0-4446-ba57-f98d353fc7a0",
  "tool_use_result": {
    "stdout": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nDatabase file #1: references.bib\nWarning--can't use both volume and number fields in guo-2021-label-confusion\n(There was 1 warning)",
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

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01JVSU1qhVumxsRroEY4MeSs`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "Two more pdflatex passes",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "035ed824-a6f0-4e05-a72d-d856415a4cd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WMiHjrb8HfwuJQ2WhZBZ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 178,
      "cache_read_input_tokens": 42363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 178
      },
      "output_tokens": 70,
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

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bft3y6tfw",
  "tool_use_id": "toolu_01JVSU1qhVumxsRroEY4MeSs",
  "description": "Two more pdflatex passes",
  "task_type": "local_bash",
  "uuid": "1702816f-5231-4d4d-86ec-e21c7cb78bdf",
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc"
}
```

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bft3y6tfw",
  "tool_use_id": "toolu_01JVSU1qhVumxsRroEY4MeSs",
  "status": "completed",
  "output_file": "",
  "summary": "Two more pdflatex passes",
  "uuid": "885a901c-4639-4dc8-a34a-8acaf83e2b6a",
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc"
}
```

---

### Tool result

_source line 32 · 2026-05-22T05:56:10.564Z_

<details><summary>↩ Tool result · `toolu_01JVSU1qhVumxsRroEY4MeSs`</summary>

```text
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 481413 bytes).
Transcript written on main.log.
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 481363 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "7c3a58c6-6274-485f-9ee2-f01ab0b6f41a",
  "tool_use_result": {
    "stdout": "re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (27 pages, 481413 bytes).\nTranscript written on main.log.\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (27 pages, 481363 bytes).\nTranscript written on main.log.",
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

_source line 33_

Now verify: no errors, no undefined references, page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "d8889245-8a0e-4778-918e-5cce4dbbb95b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VP2JnQ5taKTBDU8SnspfkD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 42541,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01TFKMqEbCdFYKcbytfBmwgy`</summary>

```json
{
  "command": "grep -c \"^!\" main.log; grep \"undefined\" main.log | head -5; grep \"Citation.*undefined\" main.log | head -5; grep \"Warning.*citation\" main.blg | head -5",
  "description": "Check for errors, undefined refs, missing citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "bcec0aab-7b9f-4944-85d2-a010287346dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VP2JnQ5taKTBDU8SnspfkD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 42541,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

_source line 35 · 2026-05-22T05:56:15.219Z_

<details><summary>↩ Tool result · `toolu_01TFKMqEbCdFYKcbytfBmwgy`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "8e707652-f2af-4d4b-b82c-24a89fef3f79",
  "tool_use_result": {
    "stdout": "0",
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

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_019i71N67yhqL7JnWUnZBqEJ`</summary>

```json
{
  "command": "grep -E \"Output written\" main.log | tail -1",
  "description": "Check page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "d197795a-71d2-4c79-9c81-8672af825460",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9S3fRtRhFAbMS2KfqT3a1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 153,
      "cache_read_input_tokens": 42947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 153
      },
      "output_tokens": 49,
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

_source line 37 · 2026-05-22T05:56:18.500Z_

<details><summary>↩ Tool result · `toolu_019i71N67yhqL7JnWUnZBqEJ`</summary>

```text
Output written on main.pdf (27 pages, 481363 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "d69b8ff4-1421-4e0a-9ec7-a36babd4bcbb",
  "tool_use_result": {
    "stdout": "Output written on main.pdf (27 pages, 481363 bytes).",
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

_source line 38_

Let me check body page count (before references/appendix).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "03b02551-dd4d-4322-a4eb-f6e14e728d79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5Dywei1YNMHL7NSvwjzjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 113,
      "cache_read_input_tokens": 43100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 113
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

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01LsA93kpAPcLwmzxyEARHV3`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\bibliography\\|\\\\\\\\appendix\\|\\\\\\\\newpage\" main.tex | head -10",
  "description": "Find where body ends"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "b6ced24c-b857-4041-bddf-575214502f81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5Dywei1YNMHL7NSvwjzjc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 113,
      "cache_read_input_tokens": 43100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 113
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

_source line 40 · 2026-05-22T05:56:21.925Z_

<details><summary>↩ Tool result · `toolu_01LsA93kpAPcLwmzxyEARHV3`</summary>

```text
56:\bibliography{references}
58:\appendix
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "6404b930-7e76-4138-9fbc-6a6882b02d75",
  "tool_use_result": {
    "stdout": "56:\\bibliography{references}\n58:\\appendix",
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

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01C59H1cqzMineUygvb66kru`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "0622492c-77d3-4bfd-904d-bc4adc84056c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVfnApnkg9a9Ro1wJjxU59",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 135,
      "cache_read_input_tokens": 43213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 135
      },
      "output_tokens": 65,
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

_source line 42 · 2026-05-22T05:56:29.462Z_

<details><summary>↩ Tool result · `toolu_01C59H1cqzMineUygvb66kru`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\S\ref{sec:multi_channel}) and SDGD failure analysis (\S\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\,=\,0$) yields residual SD${}\,=\,0.88$\,pp, approximately 18--44\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\,pp) is far inside the $\pm 3$\,pp equivalence margin.
43	
44	\item \textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.
45	
46	\item \textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\ref{app:split-origin}).
47	\item \textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.
48	\end{enumerate}
49	
50	\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.
51	
52	\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \citep{dror-2018-significance,card-2020-power}. The core claims (count decline, BCS--accuracy correlation) are robust to Bonferroni correction (all $p < 0.001$); the logit-scale interaction ($p = 0.047$) is the only result near the threshold and is already characterized as marginal.
53	
54	% \input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF
55	
56	\bibliography{references}
57	
58	\appendix
59	
60	\section{Additional Figures}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "5ab2a173-71d7-4cdd-8eae-1fb9bbfc5fe7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}. The core claims (count decline, BCS--accuracy correlation) are robust to Bonferroni correction (all $p < 0.001$); the logit-scale interaction ($p = 0.047$) is the only result near the threshold and is already characterized as marginal.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 918
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
The body ends at line 56 (`\bibliography`). I need to check what page the bibliography starts on. Let me check the log for page info. Actually, the total is 27 pages. With the `[review]` option (which is ACL format with line numbers), the body should be ≤ 8 pages. Let me check the page where bibliography starts by looking at the PDF or log.

Let me check the log for page references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "6ad8e9b0-7d94-4c3c-a88f-0ac4feff7256",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLXdw5Qkv9iQ4YezvNN1c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 43348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1923
      },
      "output_tokens": 13,
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

<details open><summary>🔧 Tool call — Bash · `toolu_01ErnWV9ZUePx6KDA1k2tapJ`</summary>

```json
{
  "command": "grep -o \"\\[[0-9]*\\]\" main.log | sort -t'[' -k1 -n | uniq | head -30",
  "description": "Check page numbers from log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "5a111ba6-511a-47f5-a73f-8d4503010c1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLXdw5Qkv9iQ4YezvNN1c7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 43348,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1923
      },
      "output_tokens": 13,
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

_source line 45 · 2026-05-22T05:56:36.804Z_

<details><summary>↩ Tool result · `toolu_01ErnWV9ZUePx6KDA1k2tapJ`</summary>

```text
[10]
[11]
[12]
[13]
[14]
[15]
[16]
[17]
[18]
[19]
[20]
[21]
[22]
[23]
[24]
[25]
[26]
[2]
[3]
[4]
[6]
[8]
[9]
[]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "887ed481-b52d-4980-98a1-d56ae968d969",
  "tool_use_result": {
    "stdout": "[10]\n[11]\n[12]\n[13]\n[14]\n[15]\n[16]\n[17]\n[18]\n[19]\n[20]\n[21]\n[22]\n[23]\n[24]\n[25]\n[26]\n[2]\n[3]\n[4]\n[6]\n[8]\n[9]\n[]",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01CfcPD3EiBeSdrMzvLqQeax`</summary>

```json
{
  "command": "grep -E \"^\\[\" main.log | head -20",
  "description": "Check page flow in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "c5fd3fd9-d1a6-4c66-98f2-31ac77970e8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CMsVCwiM7GJa9dbzDF9Vfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 45271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 326
      },
      "output_tokens": 62,
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

_source line 47 · 2026-05-22T05:56:39.480Z_

<details><summary>↩ Tool result · `toolu_01CfcPD3EiBeSdrMzvLqQeax`</summary>

```text
[Loading MPS to PDF converter (version 2006.09.02).]
[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
[2]
[4]
[5 <../../figures/paper/fig_count_curves.pdf> <../../figures/paper/fig_bcs_scal
[]\T1/ptm/m/n/10.95 (+20) The cor-re-la-tions are sta-tis-ti-cally sig-nif-i-ca
[]$\T1/ptm/m/n/10.95 (+20) 22% of RE ac-cu-racy vari-ance on FewRel
[][][]\T1/ptm/m/n/9 (+20) Partial cor-re-la-tion con-trol-ling for de-gree cen-
[7 <../../figures/paper/fig_error_taxonomy.pdf>]
[8]
[9] (./main.bbl
[]\T1/ptm/m/n/10 (+20) Dhananjay Ashok and Zachary C. Lip-ton. 2023.
[]\T1/ptm/m/n/10 (+20) Jack Boy-lan, Chris Hokamp, and Demian
[]\T1/ptm/m/n/10 (+20) Mark Col-lier, Basil Mustafa, Efi Kokiopoulou,
[10] [11]
[12]
[]\T1/ptm/m/n/10 (+20) Dong Zhao, Yadong Wang, Xi-ang Chen, Chenxi
[]\T1/ptm/m/n/10.95 (+20) Compute pair-wise SCS ma-trix $\OML/cmm/m/it/10.95 S[
[]\T1/ptm/m/n/10.95 (+20) Single-pass ex-trac-tion achieves F1=0.445
[13]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "a4e9c0ba-76b3-47b3-b11f-f325a5df3f30",
  "tool_use_result": {
    "stdout": "[Loading MPS to PDF converter (version 2006.09.02).]\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\n[2]\n[4]\n[5 <../../figures/paper/fig_count_curves.pdf> <../../figures/paper/fig_bcs_scal\n[]\\T1/ptm/m/n/10.95 (+20) The cor-re-la-tions are sta-tis-ti-cally sig-nif-i-ca\n[]$\\T1/ptm/m/n/10.95 (+20) 22% of RE ac-cu-racy vari-ance on FewRel\n[][][]\\T1/ptm/m/n/9 (+20) Partial cor-re-la-tion con-trol-ling for de-gree cen-\n[7 <../../figures/paper/fig_error_taxonomy.pdf>]\n[8]\n[9] (./main.bbl\n[]\\T1/ptm/m/n/10 (+20) Dhananjay Ashok and Zachary C. Lip-ton. 2023.\n[]\\T1/ptm/m/n/10 (+20) Jack Boy-lan, Chris Hokamp, and Demian\n[]\\T1/ptm/m/n/10 (+20) Mark Col-lier, Basil Mustafa, Efi Kokiopoulou,\n[10] [11]\n[12]\n[]\\T1/ptm/m/n/10 (+20) Dong Zhao, Yadong Wang, Xi-ang Chen, Chenxi\n[]\\T1/ptm/m/n/10.95 (+20) Compute pair-wise SCS ma-trix $\\OML/cmm/m/it/10.95 S[\n[]\\T1/ptm/m/n/10.95 (+20) Single-pass ex-trac-tion achieves F1=0.445\n[13]",
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

_source line 48_

Body ends on page 8, bibliography starts on page 9. Body ≤ 8 pages confirmed. No errors, no undefined references, no missing citations.

**Summary:**

| Item | Detail |
|------|--------|
| **Bib: `shachar-2025-ner-retriever`** | Added at `references.bib` line ~220 (ZERO-SHOT NER / RE BASELINES section) |
| **Bib: `zhao-2025-reflect-learn`** | **Skipped** — already exists as `reflect-learn-2026` (line 390, complete AAAI proceedings entry with DOI) |
| **Citation 1 (NER Retriever)** | Inserted in `related_work.tex:6`, paragraph "Training-free LLM IE", after RE methods sentence |
| **Citation 2 (Reflect then Learn)** | Inserted in same location using existing key `reflect-learn-2026` (was already `\citep`'d in paragraph 2; now also `\citet`'d with expanded context in paragraph 1) |
| **Compilation** | 0 errors, 0 undefined references, 0 missing citations, body = 8 pages |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "uuid": "077f0159-1367-49a6-8af4-9cedf1a3939d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XYEMYk2zFUfnzXn5e258g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 45597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 615
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

Body ends on page 8, bibliography starts on page 9. Body ≤ 8 pages confirmed. No errors, no undefined references, no missing citations.

**Summary:**

| Item | Detail |
|------|--------|
| **Bib: `shachar-2025-ner-retriever`** | Added at `references.bib` line ~220 (ZERO-SHOT NER / RE BASELINES section) |
| **Bib: `zhao-2025-reflect-learn`** | **Skipped** — already exists as `reflect-learn-2026` (line 390, complete AAAI proceedings entry with DOI) |
| **Citation 1 (NER Retriever)** | Inserted in `related_work.tex:6`, paragraph "Training-free LLM IE", after RE methods sentence |
| **Citation 2 (Reflect then Learn)** | Inserted in same location using existing key `reflect-learn-2026` (was already `\citep`'d in paragraph 2; now also `\citet`'d with expanded context in paragraph 1) |
| **Compilation** | 0 errors, 0 undefined references, 0 missing citations, body = 8 pages |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 142951,
  "duration_api_ms": 137866,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "b95c9edc-6114-42a6-8126-a46f6a22c0cc",
  "total_cost_usd": 0.66372875,
  "usage": {
    "input_tokens": 1318,
    "cache_creation_input_tokens": 34371,
    "cache_read_input_tokens": 566416,
    "output_tokens": 6296,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34371,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 296,
        "cache_read_input_tokens": 45597,
        "cache_creation_input_tokens": 615,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 615
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1632,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001712,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1318,
      "outputTokens": 6296,
      "cacheReadInputTokens": 566416,
      "cacheCreationInputTokens": 34371,
      "webSearchRequests": 0,
      "costUSD": 0.6620167499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6429e4a3-6afe-48c7-8f89-9229b651b6e5"
}
```

</details>

---
