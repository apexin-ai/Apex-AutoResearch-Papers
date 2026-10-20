# paper introduction rewrite

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_introduction_rewrite_20260517T232114.log`
- **Structured JSON:** [`54930a16d9a33a73c6c0.json`](../../sessions/54/54930a16d9a33a73c6c0.json)

## Before a recorded user message

30 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
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
  "uuid": "3787fdc8-b67b-4b43-9af9-316e58876d43",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1779076800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "974c348d-44ca-4bc8-97e0-eb5f5c8ba2de",
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current introduction, the paper_framing.md, and the references.bib to understand what I'm working with.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "4565bbc3-5f86-4b7b-989f-a8d587817aa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYsHmLn2LzBXvnQW8NwFjo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14008,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14008
      },
      "output_tokens": 32,
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

Let me read the current introduction, paper framing, and references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "0eb77b4b-07c7-4f14-b22f-3fda71da07ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYsHmLn2LzBXvnQW8NwFjo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14008,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14008
      },
      "output_tokens": 32,
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

<details open><summary>🔧 Tool call — Read · `toolu_011KKLGjWQ3AKEbZPyEsekAm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "1242e624-6649-44aa-9d00-cb64ec9d8ec7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYsHmLn2LzBXvnQW8NwFjo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14008,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14008
      },
      "output_tokens": 32,
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

_source line 7 · 2026-05-17T23:21:26.299Z_

<details><summary>↩ Tool result · `toolu_011KKLGjWQ3AKEbZPyEsekAm`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.
5	Structured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\citep{llmpruner2023,graspprune2026}.
6	However, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.
7	\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.
8	
9	Despite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\citep{selfhealing2025,paser2025}.
10	No prior work has studied whether the \emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.
11	This gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.
12	The optimal set of structures to retain should therefore depend on the recovery paradigm.
13	
14	We hypothesize that \emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.
15	If a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.
16	Conversely, structures with unique, non-redundant computations are difficult to recover once removed.
17	This yields what we term the \textbf{Redundancy Paradox}: counterintuitively, the structures most valuable to retain for post-RLVR recovery are not the most important ones, but the most \emph{functionally unique} ones.
18	Recovery-aware pruning therefore \emph{preferentially removes} important-but-redundant structures---whose high overlap means RLVR can redistribute their function across retained peers---while protecting functionally unique structures that, once removed, leave an irrecoverable gap.
19	Standard importance-only pruning, by contrast, protects high-importance structures regardless of redundancy, inadvertently removing unique structures whose function cannot be recovered.
20	
21	We propose \textbf{Recovery-Aware Structured Pruning (\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.
22	In Stage~1, \rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\citealp{kornblith2019cka}).
23	In Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \times (1 - F(h))^\alpha$ that protects structures which are both important \emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.
24	In Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\citep{shao2024grpo} to restore reasoning ability.
25	Unlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\citep{mpruner2024,lachance2024cka}, \rasp{} uses \emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.
26	
27	We evaluate \rasp{} on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} at 20\% structured sparsity.
28	At matched sparsity, \rasp{}-pruned models retain 29\% GSM8K~\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.
29	After SFT warmup, both pruning strategies recover substantially (57--64\%), with detailed comparison deferred to \S\ref{sec:experiments}.
30	[TBD: GRPO results]
31	
32	Our contributions are:
33	\begin{enumerate}[nosep,leftmargin=*]
34	    \item We identify the \emph{Redundancy Paradox}---that functional redundancy enables RLVR to recover the function of removed structures, making important-but-redundant structures safely removable while functionally unique structures become critical to retain---and formalize it through intra-layer CKA-based functional overlap scoring.
35	    \item We propose \rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\% post-prune GSM8K accuracy versus 1\% for importance-only pruning at matched 20\% sparsity on DeepSeek-R1-Distill-Qwen-7B.
36	    \item [TBD: GRPO recovery results---contribution demonstrating that \rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]
37	    \item We present preliminary evidence that the optimal pruning strategy may be conditioned on the recovery paradigm~\citep{frankle2019lth}, supporting the notion of \emph{paradigm-conditioned prunability} [TBD: pending GRPO confirmation and statistical validation].
38	\end{enumerate}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "2335c93e-a7ad-484f-b638-a9948c85484a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.\nStructured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.\nHowever, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.\n\\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.\n\nDespite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\nNo prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.\nThis gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.\nThe optimal set of structures to retain should therefore depend on the recovery paradigm.\n\nWe hypothesize that \\emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.\nIf a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.\nConversely, structures with unique, non-redundant computations are difficult to recover once removed.\nThis yields what we term the \\textbf{Redundancy Paradox}: counterintuitively, the structures most valuable to retain for post-RLVR recovery are not the most important ones, but the most \\emph{functionally unique} ones.\nRecovery-aware pruning therefore \\emph{preferentially removes} important-but-redundant structures---whose high overlap means RLVR can redistribute their function across retained peers---while protecting functionally unique structures that, once removed, leave an irrecoverable gap.\nStandard importance-only pruning, by contrast, protects high-importance structures regardless of redundancy, inadvertently removing unique structures whose function cannot be recovered.\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.\nIn Stage~1, \\rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}).\nIn Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important \\emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.\nIn Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\\citep{shao2024grpo} to restore reasoning ability.\nUnlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.\n\nWe evaluate \\rasp{} on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% structured sparsity.\nAt matched sparsity, \\rasp{}-pruned models retain 29\\% GSM8K~\\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.\nAfter SFT warmup, both pruning strategies recover substantially (57--64\\%), with detailed comparison deferred to \\S\\ref{sec:experiments}.\n[TBD: GRPO results]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify the \\emph{Redundancy Paradox}---that functional redundancy enables RLVR to recover the function of removed structures, making important-but-redundant structures safely removable while functionally unique structures become critical to retain---and formalize it through intra-layer CKA-based functional overlap scoring.\n    \\item We propose \\rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\\% post-prune GSM8K accuracy versus 1\\% for importance-only pruning at matched 20\\% sparsity on DeepSeek-R1-Distill-Qwen-7B.\n    \\item [TBD: GRPO recovery results---contribution demonstrating that \\rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]\n    \\item We present preliminary evidence that the optimal pruning strategy may be conditioned on the recovery paradigm~\\citep{frankle2019lth}, supporting the notion of \\emph{paradigm-conditioned prunability} [TBD: pending GRPO confirmation and statistical validation].\n\\end{enumerate}\n",
      "numLines": 39,
      "startLine": 1,
      "totalLines": 39
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Ls2rmHBbZF3RnNZ37SeZ65`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "ecf7cf3d-57f1-453f-9895-501d3b6eb1bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYsHmLn2LzBXvnQW8NwFjo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14008,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14008
      },
      "output_tokens": 32,
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

_source line 9 · 2026-05-17T23:21:27.226Z_

<details><summary>↩ Tool result · `toolu_01Ls2rmHBbZF3RnNZ37SeZ65`</summary>

```text
1	@article{deepseek2025r1,
2	  title={DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},
3	  author={{DeepSeek-AI}},
4	  journal={arXiv preprint arXiv:2501.12948},
5	  year={2025},
6	  url={https://arxiv.org/abs/2501.12948}
7	}
8	
9	@article{qwen2.5,
10	  title={Qwen2.5 Technical Report},
11	  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and others},
12	  journal={arXiv preprint arXiv:2412.15115},
13	  year={2024},
14	  url={https://arxiv.org/abs/2412.15115}
15	}
16	
17	@article{cobbe2021gsm8k,
18	  title={Training Verifiers to Solve Math Word Problems},
19	  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
20	  journal={arXiv preprint arXiv:2110.14168},
21	  year={2021},
22	  url={https://arxiv.org/abs/2110.14168}
23	}
24	
25	@article{shao2024grpo,
26	  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
27	  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
28	  journal={arXiv preprint arXiv:2402.03300},
29	  year={2024},
30	  url={https://arxiv.org/abs/2402.03300}
31	}
32	
33	@inproceedings{llmpruner2023,
34	  title={LLM-Pruner: On the Structural Pruning of Large Language Models},
35	  author={Ma, Xinyin and Fang, Gongfan and Wang, Xinchao},
36	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
37	  year={2023},
38	  url={https://arxiv.org/abs/2305.11627}
39	}
40	
41	@inproceedings{graspprune2026,
42	  title={GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models},
43	  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},
44	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
45	  year={2026},
46	  url={https://arxiv.org/abs/2604.19398}
47	}
48	
49	@article{resp2025,
50	  title={Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models},
51	  author={Wang, Ziyan and Diao, Enmao and Le, Qi and Wang, Pu and Wang, Guanchu and Lee, Minwoo and Yeh, Shu-ping and Yang, Li},
52	  journal={arXiv preprint arXiv:2512.02185},
53	  year={2025},
54	  url={https://arxiv.org/abs/2512.02185}
55	}
56	
57	@article{selfhealing2025,
58	  title={Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning},
59	  author={Ji, Yixin and Lin, Zhimin and Li, Juntao and Wu, Kaixin and Yao, Kai and Jia, Xu and Mo, Linjian and Zhang, Min},
60	  year={2025},
61	  note={Under review},
62	  url={https://openreview.net/forum?id=Cy8Qa4gAst}
63	}
64	
65	@inproceedings{bonsai2025,
66	  title={Everybody Prune Now: Structured Pruning of LLMs with only Forward Passes},
67	  author={Kolawole, Steven and Dery, Lucio and Kagy, Jean-Fran\c{c}ois and Smith, Virginia and Neubig, Graham and Talwalkar, Ameet},
68	  booktitle={Proceedings of the 42nd International Conference on Machine Learning (ICML)},
69	  year={2025},
70	  url={https://arxiv.org/abs/2402.05406}
71	}
72	
73	@article{paser2025,
74	  title={PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery},
75	  author={He, Bowei and Yin, Lihao and Zhen, Hui-Ling and Zhang, Xiaokun and Yuan, Mingxuan and Ma, Chen},
76	  journal={arXiv preprint arXiv:2502.12594},
77	  year={2025},
78	  url={https://arxiv.org/abs/2502.12594},
79	  note={Under review}
80	}
81	
82	@inproceedings{rlsqueezes2026,
83	  title={RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs},
84	  author={Matsutani, Kohsei and Takashiro, Shota and Minegishi, Gouki and Kojima, Takeshi and Iwasawa, Yusuke and Matsuo, Yutaka},
85	  booktitle={Proceedings of the 14th International Conference on Learning Representations (ICLR)},
86	  year={2026},
87	  url={https://arxiv.org/abs/2509.21128}
88	}
89	
90	@inproceedings{kornblith2019cka,
91	  title={Similarity of Neural Network Representations Revisited},
92	  author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},
93	  booktitle={Proceedings of the 36th International Conference on Machine Learning (ICML)},
94	  year={2019},
95	  url={https://arxiv.org/abs/1905.00414}
96	}
97	
98	@article{mpruner2024,
99	  title={MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning},
100	  author={Hu, Seungbeom and Park, Chanjun and Ferraiuolo, Andrew and Ko, Sang-Ki and Kim, Jinwoo and Song, Haein and Kim, Jieung},
101	  journal={arXiv preprint arXiv:2408.13482},
102	  year={2024},
103	  url={https://arxiv.org/abs/2408.13482}
104	}
105	
106	@mastersthesis{lachance2024cka,
107	  title={Using Centered Kernel Alignment for Understanding and Pruning Neural Networks},
108	  author={Lachance, Alex},
109	  school={University of Rhode Island},
110	  year={2024},
111	  url={https://digitalcommons.uri.edu/theses/2283/}
112	}
113	
114	@inproceedings{frankle2019lth,
115	  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},
116	  author={Frankle, Jonathan and Carbin, Michael},
117	  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},
118	  year={2019},
119	  url={https://arxiv.org/abs/1803.03635}
120	}
121	
122	@inproceedings{ainslie2023gqa,
123	  title={{GQA}: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints},
124	  author={Ainslie, Joshua and Lee-Thorp, James and de Jong, Michiel and Zemlyanskiy, Yury and Lebr{\'o}n, Federico and Sanghai, Sumit},
125	  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
126	  year={2023},
127	  url={https://arxiv.org/abs/2305.13245}
128	}
129	
130	@article{shortgpt2024,
131	  title={{ShortGPT}: Layers in Large Language Models are More Redundant Than You Expect},
132	  author={Men, Xin and Xu, Mingyu and Zhang, Qingyu and Wang, Bingning and Lin, Hongyu and Lu, Yaojie and Han, Xianpei and Chen, Weipeng},
133	  journal={arXiv preprint arXiv:2403.03853},
134	  year={2024},
135	  url={https://arxiv.org/abs/2403.03853}
136	}
137	
138	@inproceedings{slicegpt2024,
139	  title={{SliceGPT}: Compress Large Language Models by Deleting Rows and Columns},
140	  author={Ashkboos, Saleh and Croci, Maximilian L. and Gennari do Nascimento, Marcelo and Hoefler, Torsten and Hensman, James},
141	  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},
142	  year={2024},
143	  url={https://arxiv.org/abs/2401.15024}
144	}
145	
146	@inproceedings{wanda2024,
147	  title={A Simple and Effective Pruning Approach for Large Language Models},
148	  author={Sun, Mingjie and Liu, Zhuang and Bair, Anna and Kolter, J. Zico},
149	  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},
150	  year={2024},
151	  url={https://arxiv.org/abs/2306.11695}
152	}
153	
154	@article{llms2lrms2026,
155	  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},
156	  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},
157	  journal={arXiv preprint arXiv:2601.18091},
158	  year={2026},
159	  url={https://arxiv.org/abs/2601.18091}
160	}
161	
162	@inproceedings{rac2025,
163	  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},
164	  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},
165	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
166	  year={2025},
167	  url={https://arxiv.org/abs/2509.12464}
168	}
169	
170	@article{ssgr2025,
171	  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},
172	  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},
173	  journal={arXiv preprint arXiv:2511.18864},
174	  year={2025},
175	  url={https://arxiv.org/abs/2511.18864}
176	}
177	
178	@article{doingmore2026,
179	  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
180	  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
181	  journal={arXiv preprint arXiv:2604.25098},
182	  year={2026},
183	  url={https://arxiv.org/abs/2604.25098}
184	}
185	
186	@inproceedings{p2law2025,
187	  title={{P\textsuperscript{2}} Law: Scaling Law for Post-Training After Model Pruning},
188	  author={Chen, Xiaodong and Hu, Yuxuan and Zhang, Xiaokang and Wang, Yanling and Li, Cuiping and Chen, Hong and Zhang, Jing},
189	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
190	  year={2025},
191	  url={https://arxiv.org/abs/2411.10272}
192	}
193	
194	@inproceedings{pat2025,
195	  title={{PAT}: Pruning-Aware Tuning for Large Language Models},
196	  author={Liu, Yijiang and Yang, Huanrui and Chen, Youxin and Zhang, Rongyu and Wang, Miao and Du, Yuan and Du, Li},
197	  booktitle={Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI)},
198	  year={2025},
199	  url={https://arxiv.org/abs/2408.14721}
200	}
201	
202	@article{fang_2025,
203	  title={{FANG}: Improving Generalization in {LLM} Structured Pruning via Function-Aware Neuron Grouping},
204	  author={Yu, Tao and An, Yongqi and Zhu, Kuan and Zhu, Guibo and Tang, Ming and Wang, Jinqiao},
205	  journal={arXiv preprint arXiv:2512.23014},
206	  year={2025},
207	  url={https://arxiv.org/abs/2512.23014}
208	}
209	
210	@article{funcnet_2025,
211	  title={Pruning Large Language Models by Identifying and Preserving Functional Networks},
212	  author={Liu, Yiheng and Ning, Junhao and Xia, Sichen and Gao, Xiaohui and Qiang, Ning and Ge, Bao and Han, Junwei and Hu, Xintao},
213	  journal={arXiv preprint arXiv:2508.05239},
214	  year={2025},
215	  url={https://arxiv.org/abs/2508.05239}
216	}
217	
218	@article{klabunde_similarity_survey_2025,
219	  title={Similarity of Neural Network Models: A Survey of Functional and Representational Measures},
220	  author={Klabunde, Max and Schumacher, Tobias and Strohmaier, Markus and Lemmerich, Florian},
221	  journal={ACM Computing Surveys},
222	  volume={57},
223	  number={9},
224	  year={2025},
225	  url={https://arxiv.org/abs/2305.06329}
226	}
227	
228	@inproceedings{restorelcc_2025,
229	  title={{RestoreLCC}: Restoring Pruned Large Language Models via Lost Component Compensation},
230	  author={Feng, Zijian and Zhou, Hanzhang and Zhu, Zixiao and Li, Tianjiao and Chua, Jia Jim Deryl and Mak, Lee Onn and Ng, Gee Wah and Mao, Kezhi},
231	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
232	  year={2025},
233	  note={Spotlight},
234	  url={https://arxiv.org/abs/2510.21834}
235	}
236	
237	@article{boiling_frog_2026,
238	  title={Gradually Compacting Large Language Models for Reasoning Like a Boiling Frog},
239	  author={Zhao, Yiran and Zhou, Shengyang and Wu, Zijian and Hu, Tongyan and Xu, Yuhui and Dou, Rengan and Kawaguchi, Kenji and Joty, Shafiq and Li, Junnan and Shieh, Michael Qizhe},
240	  journal={arXiv preprint arXiv:2602.04919},
241	  year={2026},
242	  url={https://arxiv.org/abs/2602.04919}
243	}
244	
245	@article{hendrycks2021mmlu,
246	  title={Measuring Massive Multitask Language Understanding},
247	  author={Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
248	  journal={Proceedings of the International Conference on Learning Representations (ICLR)},
249	  year={2021},
250	  url={https://arxiv.org/abs/2009.03300}
251	}
252	
253	@article{chen2021humaneval,
254	  title={Evaluating Large Language Models Trained on Code},
255	  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},
256	  journal={arXiv preprint arXiv:2107.03374},
257	  year={2021},
258	  url={https://arxiv.org/abs/2107.03374}
259	}
260	
261	@article{bai2024longbench,
262	  title={LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding},
263	  author={Bai, Yushi and Lv, Xin and Zhang, Jiajie and Lyu, Hongchang and Tang, Jiankai and Huang, Zhidian and Du, Zhengxiao and Liu, Xiao and Zeng, Aohan and Hou, Lei and others},
264	  journal={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
265	  year={2024},
266	  url={https://arxiv.org/abs/2308.14508}
267	}
268	
269	@article{opsd2026,
270	  title={{OPSD} Compresses What {RLVR} Teaches: A Post-{RL} Compaction Stage for Reasoning Models},
271	  author={Kim, Jaehoon and Lee, Dongha},
272	  journal={arXiv preprint arXiv:2605.06188},
273	  year={2026},
274	  url={https://arxiv.org/abs/2605.06188}
275	}
276	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "f8239cb7-ed38-405a-986c-df4f78dd21c0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
      "content": "@article{deepseek2025r1,\n  title={DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning},\n  author={{DeepSeek-AI}},\n  journal={arXiv preprint arXiv:2501.12948},\n  year={2025},\n  url={https://arxiv.org/abs/2501.12948}\n}\n\n@article{qwen2.5,\n  title={Qwen2.5 Technical Report},\n  author={Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and others},\n  journal={arXiv preprint arXiv:2412.15115},\n  year={2024},\n  url={https://arxiv.org/abs/2412.15115}\n}\n\n@article{cobbe2021gsm8k,\n  title={Training Verifiers to Solve Math Word Problems},\n  author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal={arXiv preprint arXiv:2110.14168},\n  year={2021},\n  url={https://arxiv.org/abs/2110.14168}\n}\n\n@article{shao2024grpo,\n  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},\n  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},\n  journal={arXiv preprint arXiv:2402.03300},\n  year={2024},\n  url={https://arxiv.org/abs/2402.03300}\n}\n\n@inproceedings{llmpruner2023,\n  title={LLM-Pruner: On the Structural Pruning of Large Language Models},\n  author={Ma, Xinyin and Fang, Gongfan and Wang, Xinchao},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.11627}\n}\n\n@inproceedings{graspprune2026,\n  title={GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models},\n  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},\n  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2026},\n  url={https://arxiv.org/abs/2604.19398}\n}\n\n@article{resp2025,\n  title={Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models},\n  author={Wang, Ziyan and Diao, Enmao and Le, Qi and Wang, Pu and Wang, Guanchu and Lee, Minwoo and Yeh, Shu-ping and Yang, Li},\n  journal={arXiv preprint arXiv:2512.02185},\n  year={2025},\n  url={https://arxiv.org/abs/2512.02185}\n}\n\n@article{selfhealing2025,\n  title={Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning},\n  author={Ji, Yixin and Lin, Zhimin and Li, Juntao and Wu, Kaixin and Yao, Kai and Jia, Xu and Mo, Linjian and Zhang, Min},\n  year={2025},\n  note={Under review},\n  url={https://openreview.net/forum?id=Cy8Qa4gAst}\n}\n\n@inproceedings{bonsai2025,\n  title={Everybody Prune Now: Structured Pruning of LLMs with only Forward Passes},\n  author={Kolawole, Steven and Dery, Lucio and Kagy, Jean-Fran\\c{c}ois and Smith, Virginia and Neubig, Graham and Talwalkar, Ameet},\n  booktitle={Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2402.05406}\n}\n\n@article{paser2025,\n  title={PASER: Post-Training Data Selection for Efficient Pruned Large Language Model Recovery},\n  author={He, Bowei and Yin, Lihao and Zhen, Hui-Ling and Zhang, Xiaokun and Yuan, Mingxuan and Ma, Chen},\n  journal={arXiv preprint arXiv:2502.12594},\n  year={2025},\n  url={https://arxiv.org/abs/2502.12594},\n  note={Under review}\n}\n\n@inproceedings{rlsqueezes2026,\n  title={RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs},\n  author={Matsutani, Kohsei and Takashiro, Shota and Minegishi, Gouki and Kojima, Takeshi and Iwasawa, Yusuke and Matsuo, Yutaka},\n  booktitle={Proceedings of the 14th International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2509.21128}\n}\n\n@inproceedings{kornblith2019cka,\n  title={Similarity of Neural Network Representations Revisited},\n  author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle={Proceedings of the 36th International Conference on Machine Learning (ICML)},\n  year={2019},\n  url={https://arxiv.org/abs/1905.00414}\n}\n\n@article{mpruner2024,\n  title={MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning},\n  author={Hu, Seungbeom and Park, Chanjun and Ferraiuolo, Andrew and Ko, Sang-Ki and Kim, Jinwoo and Song, Haein and Kim, Jieung},\n  journal={arXiv preprint arXiv:2408.13482},\n  year={2024},\n  url={https://arxiv.org/abs/2408.13482}\n}\n\n@mastersthesis{lachance2024cka,\n  title={Using Centered Kernel Alignment for Understanding and Pruning Neural Networks},\n  author={Lachance, Alex},\n  school={University of Rhode Island},\n  year={2024},\n  url={https://digitalcommons.uri.edu/theses/2283/}\n}\n\n@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carbin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}\n\n@inproceedings{ainslie2023gqa,\n  title={{GQA}: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints},\n  author={Ainslie, Joshua and Lee-Thorp, James and de Jong, Michiel and Zemlyanskiy, Yury and Lebr{\\'o}n, Federico and Sanghai, Sumit},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.13245}\n}\n\n@article{shortgpt2024,\n  title={{ShortGPT}: Layers in Large Language Models are More Redundant Than You Expect},\n  author={Men, Xin and Xu, Mingyu and Zhang, Qingyu and Wang, Bingning and Lin, Hongyu and Lu, Yaojie and Han, Xianpei and Chen, Weipeng},\n  journal={arXiv preprint arXiv:2403.03853},\n  year={2024},\n  url={https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{slicegpt2024,\n  title={{SliceGPT}: Compress Large Language Models by Deleting Rows and Columns},\n  author={Ashkboos, Saleh and Croci, Maximilian L. and Gennari do Nascimento, Marcelo and Hoefler, Torsten and Hensman, James},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2401.15024}\n}\n\n@inproceedings{wanda2024,\n  title={A Simple and Effective Pruning Approach for Large Language Models},\n  author={Sun, Mingjie and Liu, Zhuang and Bair, Anna and Kolter, J. Zico},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2306.11695}\n}\n\n@article{llms2lrms2026,\n  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},\n  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},\n  journal={arXiv preprint arXiv:2601.18091},\n  year={2026},\n  url={https://arxiv.org/abs/2601.18091}\n}\n\n@inproceedings{rac2025,\n  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},\n  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  url={https://arxiv.org/abs/2509.12464}\n}\n\n@article{ssgr2025,\n  title={Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models},\n  author={Xiang, Yang and Ji, Yixin and Li, Juntao and Zhang, Min},\n  journal={arXiv preprint arXiv:2511.18864},\n  year={2025},\n  url={https://arxiv.org/abs/2511.18864}\n}\n\n@article{doingmore2026,\n  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n  journal={arXiv preprint arXiv:2604.25098},\n  year={2026},\n  url={https://arxiv.org/abs/2604.25098}\n}\n\n@inproceedings{p2law2025,\n  title={{P\\textsuperscript{2}} Law: Scaling Law for Post-Training After Model Pruning},\n  author={Chen, Xiaodong and Hu, Yuxuan and Zhang, Xiaokang and Wang, Yanling and Li, Cuiping and Chen, Hong and Zhang, Jing},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2025},\n  url={https://arxiv.org/abs/2411.10272}\n}\n\n@inproceedings{pat2025,\n  title={{PAT}: Pruning-Aware Tuning for Large Language Models},\n  author={Liu, Yijiang and Yang, Huanrui and Chen, Youxin and Zhang, Rongyu and Wang, Miao and Du, Yuan and Du, Li},\n  booktitle={Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  url={https://arxiv.org/abs/2408.14721}\n}\n\n@article{fang_2025,\n  title={{FANG}: Improving Generalization in {LLM} Structured Pruning via Function-Aware Neuron Grouping},\n  author={Yu, Tao and An, Yongqi and Zhu, Kuan and Zhu, Guibo and Tang, Ming and Wang, Jinqiao},\n  journal={arXiv preprint arXiv:2512.23014},\n  year={2025},\n  url={https://arxiv.org/abs/2512.23014}\n}\n\n@article{funcnet_2025,\n  title={Pruning Large Language Models by Identifying and Preserving Functional Networks},\n  author={Liu, Yiheng and Ning, Junhao and Xia, Sichen and Gao, Xiaohui and Qiang, Ning and Ge, Bao and Han, Junwei and Hu, Xintao},\n  journal={arXiv preprint arXiv:2508.05239},\n  year={2025},\n  url={https://arxiv.org/abs/2508.05239}\n}\n\n@article{klabunde_similarity_survey_2025,\n  title={Similarity of Neural Network Models: A Survey of Functional and Representational Measures},\n  author={Klabunde, Max and Schumacher, Tobias and Strohmaier, Markus and Lemmerich, Florian},\n  journal={ACM Computing Surveys},\n  volume={57},\n  number={9},\n  year={2025},\n  url={https://arxiv.org/abs/2305.06329}\n}\n\n@inproceedings{restorelcc_2025,\n  title={{RestoreLCC}: Restoring Pruned Large Language Models via Lost Component Compensation},\n  author={Feng, Zijian and Zhou, Hanzhang and Zhu, Zixiao and Li, Tianjiao and Chua, Jia Jim Deryl and Mak, Lee Onn and Ng, Gee Wah and Mao, Kezhi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  note={Spotlight},\n  url={https://arxiv.org/abs/2510.21834}\n}\n\n@article{boiling_frog_2026,\n  title={Gradually Compacting Large Language Models for Reasoning Like a Boiling Frog},\n  author={Zhao, Yiran and Zhou, Shengyang and Wu, Zijian and Hu, Tongyan and Xu, Yuhui and Dou, Rengan and Kawaguchi, Kenji and Joty, Shafiq and Li, Junnan and Shieh, Michael Qizhe},\n  journal={arXiv preprint arXiv:2602.04919},\n  year={2026},\n  url={https://arxiv.org/abs/2602.04919}\n}\n\n@article{hendrycks2021mmlu,\n  title={Measuring Massive Multitask Language Understanding},\n  author={Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},\n  journal={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2021},\n  url={https://arxiv.org/abs/2009.03300}\n}\n\n@article{chen2021humaneval,\n  title={Evaluating Large Language Models Trained on Code},\n  author={Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal={arXiv preprint arXiv:2107.03374},\n  year={2021},\n  url={https://arxiv.org/abs/2107.03374}\n}\n\n@article{bai2024longbench,\n  title={LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding},\n  author={Bai, Yushi and Lv, Xin and Zhang, Jiajie and Lyu, Hongchang and Tang, Jiankai and Huang, Zhidian and Du, Zhengxiao and Liu, Xiao and Zeng, Aohan and Hou, Lei and others},\n  journal={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2024},\n  url={https://arxiv.org/abs/2308.14508}\n}\n\n@article{opsd2026,\n  title={{OPSD} Compresses What {RLVR} Teaches: A Post-{RL} Compaction Stage for Reasoning Models},\n  author={Kim, Jaehoon and Lee, Dongha},\n  journal={arXiv preprint arXiv:2605.06188},\n  year={2026},\n  url={https://arxiv.org/abs/2605.06188}\n}\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018hjWUKh8LPYC3Ege32z99s`</summary>

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
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "5a087bde-10db-4c8c-b8c7-262d6c6183c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYsHmLn2LzBXvnQW8NwFjo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14008,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14008
      },
      "output_tokens": 32,
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

_source line 11 · 2026-05-17T23:21:27.592Z_

<details><summary>↩ Tool result · `toolu_018hjWUKh8LPYC3Ege32z99s`</summary>

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
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "cda99031-9e65-4878-827f-e785d7a846de",
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

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the paper_framing.md to get the full framing context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "e3b1af76-a43f-4840-b420-b6a5ba655985",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRTy4By75RSXiJMW6RUPyD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7441,
      "cache_read_input_tokens": 25849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7441
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

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01R7GYyUQxxc9kE2M7wUDf1h`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "paper_framing.md",
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
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "0dd0acc4-0728-49c5-b1bf-932852d0f03b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRTy4By75RSXiJMW6RUPyD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7441,
      "cache_read_input_tokens": 25849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7441
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

_source line 14 · 2026-05-17T23:21:33.156Z_

<details><summary>↩ Tool result · `toolu_01R7GYyUQxxc9kE2M7wUDf1h`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper_framing.md\", \"content\": \"# Paper Framing — recovery_aware_struct_prune\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 submission)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Insight (Redundancy-Stability Tradeoff)\\nRLVR alignment (GRPO) fundamentally fails on structurally pruned reasoning models: reward improves but accuracy does not — a pruning-induced reward hacking phenomenon. We show the failure mechanism via **collapse dynamics**: pruning method determines how fast GRPO collapses, and this speed is a diagnostic of structural damage type. Crucially, functional redundancy plays **opposite roles** under SFT vs RLVR recovery:\\n\\n- **SFT**: redundant structures (high CKA overlap) are safely removable — their function redistributes through gradient-based learning. CKA-aware pruning (RASP) yields marginal SFT advantage.\\n- **RLVR**: redundant structures provide **exploration stability** — backup paths that prevent policy collapse during RL. Removing them (as RASP does) accelerates collapse.\\n\\nThis creates a **Redundancy-Stability Tradeoff**: the structures optimal to prune for SFT recovery are exactly those needed for RLVR stability. Optimal pruning is fundamentally conditioned on the recovery paradigm.\\n\\n## Core Claims (3) — REVISED based on experimental evidence\\n\\n1. **GRPO reward-accuracy decoupling is universal; pruning adds training collapse**: GRPO does not improve reasoning accuracy for ANY model post-SFT — unpruned (**81.27% = SFT 81.27%, Δ=0.00pp, identical 1072/1319 correct**), Standard-pruned (58.91% vs 59.29%, Δ=-0.38pp), RASP-pruned (60.65% vs 61.49%, Δ=-0.84pp). Reward increases dramatically (unpruned: 0→0.661) yet accuracy is unchanged — a universal reward-accuracy decoupling under GRPO+GSM8K+greedy. The pruning-specific phenomenon is **training collapse**: RASP collapses permanently at step ~10 (frac_zero_std→0.95, grad→0.007), Standard shows transient dip at step ~60, while unpruned trains stably for 100 steps. GRPO's reward signal does not encode genuine reasoning improvement; pruning removes the structural capacity to even sustain RL training.\\n\\n2. **Collapse severity gradient diagnoses structural damage**: Three-model comparison reveals a clean severity gradient — RASP (removes redundant, protects unique): permanent collapse step ~10, peak reward 0.039; Standard (importance-only): transient dip step ~60, final reward 0.065; Unpruned: no collapse, final reward 0.661. The 6× speedup from Standard→RASP confirms that functional redundancy provides RLVR exploration stability. Collapse dynamics are a zero-cost diagnostic: fast collapse = aggressive redundancy removal = poor RL trainability.\\n\\n3. **Recovery method conditions optimal pruning strategy**: For SFT recovery, RASP shows marginal advantage (+2.2pp, RASP 61.49% vs Standard 59.29%, N=1319, p=0.25). For RLVR stability, RASP is actively harmful (6× faster collapse). The structures optimal to prune for SFT are exactly those needed for RLVR stability — a fundamental Redundancy-Stability Tradeoff. Consistent with \\\"RL Squeezes, SFT Expands\\\" (ICLR 2026).\\n\\n## Evidence Status (as of 2026-05-16, ALL CORE DATA COMPLETE)\\n\\n| Evidence | Status | Result |\\n|----------|--------|--------|\\n| Unpruned SFT eval (N=1319) | ✅ | 81.27% |\\n| Unpruned GRPO step-100 eval (N=1319) | ✅ | **81.27% (Δ=0.00pp, 1072/1319 = identical to SFT)** |\\n| Unpruned GRPO step-90 eval (N=1319) | ✅ | **80.59% (1063/1319, confirms stability across late training)** |\\n| Standard SFT eval (N=1319) | ✅ | 59.29% |\\n| Standard GRPO step-50 eval (N=1319) | ✅ | 58.91% (Δ=-0.38pp) |\\n| RASP SFT eval (N=1319) | ✅ | 61.49% |\\n| RASP GRPO step-5 eval (N=1319) | ✅ | 60.65% (Δ=-0.84pp) |\\n| RASP GRPO v9 collapse dynamics | ✅ | Permanent collapse step ~10, peak reward 0.039 |\\n| Standard GRPO v8 dynamics | ✅ | Transient dip step ~60, recovery step ~90 |\\n| Unpruned GRPO v2 dynamics | ✅ | No collapse, 100 steps stable, reward 0.661 |\\n| Alpha ablation (cal=512) | ✅ | U-shape: α≥1.0 > α≤0.5 post-prune |\\n| SFT gap significance | ⚠️ p=0.25 | Not significant at N=1319; scope expansion to higher sparsity planned |\\n| RASP GRPO step-10 eval (N=1319) | ✅ | **61.87% — collapse onset does NOT reduce accuracy (vs step-5 60.65%, p=0.52)** |\\n\\n## Story Spine\\n\\n- **Problem**: The reasoning model compression pipeline (prune → recover → align) assumes alignment is independent of pruning decisions. We show this assumption fails catastrophically: GRPO alignment on pruned models produces reward improvement without accuracy gain, followed by complete collapse. The pruning-alignment interaction is not merely suboptimal — it is fundamentally broken under current practice.\\n\\n- **Existing approaches & gaps**: Self-Healing (2025) claims RLVR recovers pruned reasoning models to 95%+ at 25% compression — but uses a single pruning ratio and does not report per-step accuracy during GRPO. GRASPrune (ACL 2026) provides SOTA budgeted structural pruning but doesn't study recovery or alignment at all. RESP (Dec 2025) uses reasoning-trace calibration without recovery. No work has documented GRPO collapse on pruned models, explained its mechanism, or shown that pruning strategy determines collapse dynamics.\\n\\n- **Our framing**: We present the first systematic study of how structural pruning interacts with RLVR alignment in reasoning LLMs. We introduce RASP (S(h) = I(h) × (1-F(h))^α) not as a universally superior method, but as a **diagnostic tool** that reveals the Redundancy-Stability Tradeoff: CKA-aware structure selection that benefits SFT recovery actively harms RLVR stability. This reframes the pruning-alignment relationship from \\\"which structures to remove for best recovery\\\" to \\\"recovery paradigm determines what counts as safe to remove.\\\"\\n\\n- **Headline result**: \\\"GRPO reward improvement never translates to accuracy gain (unpruned: reward 0→0.661, accuracy 81.27%→81.27%; identical 1072/1319 correct). But pruning causes GRPO training collapse: RASP-pruned collapses permanently at step 10, Standard-pruned at step 60, unpruned never. The severity gradient (RASP > Standard > Unpruned) reveals that structural redundancy — expendable for SFT — provides critical RL exploration stability.\\\"\\n\\n## Venue Fit\\n- EMNLP Efficient Methods track: structured pruning + reasoning model alignment failure analysis\\n- Negative/diagnostic results challenging published claims (Self-Healing) are high-impact at *ACL venues\\n- Reasoning model compression pipeline failures are immediately practical (timely: DeepSeek-R1, QwQ, Kimi-K1.5)\\n- Mechanistic analysis (collapse dynamics, reward-accuracy divergence) aligns with EMNLP empirical rigor\\n\\n## Venue Fit Risks\\n- **\\\"Just a negative result without solution\\\"**: Mitigate with (1) mechanistic explanation (redundancy-stability tradeoff), (2) RASP as diagnostic tool (collapse speed predicts pruning quality for RL), (3) actionable implication (SFT-only recovery is currently the safe path; RLVR needs pruning-aware modifications)\\n- **\\\"Single model\\\"**: DeepSeek-R1-Distill-Qwen-7B is the canonical open reasoning model; multi-method comparison (RASP/Standard/Unpruned) + multi-recovery (SFT/GRPO) compensates\\n- **\\\"GRPO config might be wrong\\\"**: Report hyperparameter sensitivity (alpha ablation), show collapse is robust across configs, cite Self-Healing uses similar GRPO setup\\n- **\\\"SFT gap not significant\\\"**: Frame honestly as marginal; the paper's contribution is the GRPO failure + mechanism, not the SFT comparison. SFT gap is supplementary context.\\n- **\\\"Collapse might be training instability, not pruning-specific\\\"**: Unpruned GRPO ran 100 steps with zero collapse (reward 0.661, stable frac_zero_std ≤0.275) — pruning-specificity confirmed\\n\\n## Anticipated Reviewer Concerns & Experimental Responses\\n\\n| Concern | Response | Supporting Experiment |\\n|---------|----------|----------------------|\\n| GRPO failure might be hyperparameter issue | Alpha ablation shows U-shape is robust; reward increases but accuracy never follows | alpha_ablation_sweep |\\n| Need unpruned control for pruning-specificity | Unpruned GRPO: 100 steps stable, no collapse, reward 0.661 vs pruned collapse at step 10-60 | grpo_unpruned_v2 |\\n| SFT gap not significant | Acknowledged; paper's main claim is GRPO failure, not SFT superiority | sft_eval N=1319 |\\n| Collapse speed might not generalize | Multi-method comparison (RASP/Standard) + multi-config (alpha sweep) | grpo_v8, grpo_v9 |\\n| How does this relate to Self-Healing claims? | Self-Healing uses 25% unstructured; our structured pruning at 20% creates different damage pattern | Discussion section |\\n| What's the practical recommendation? | SFT recovery only for structurally pruned models; RLVR requires pruning-aware alignment (future work) | All experiments |\\n| CKA-aware pruning hurts RLVR — why publish RASP? | RASP is the diagnostic tool that REVEALS the tradeoff; its failure under RLVR is the evidence | grpo_v9 vs grpo_v8 |\\n\\n## Key Differentiations\\n- **vs Self-Healing (2025)**: Claims RLVR recovers pruned models → we show GRPO fails (reward hacking + collapse); different pruning granularity and controlled collapse analysis\\n- **vs MPruner (2024)**: inter-layer CKA for depth pruning in CNNs → we use intra-layer CKA as diagnostic tool revealing redundancy-stability tradeoff in reasoning LLMs\\n- **vs GRASPrune (ACL 2026)**: SOTA budgeted pruning without recovery/alignment study → we study the full prune-recover-align pipeline failure\\n- **vs RESP (Dec 2025)**: reasoning-trace calibration without recovery → we study recovery paradigm interaction\\n- **vs PASER (2025)**: optimizes recovery DATA → we show even optimal pruning STRUCTURE cannot save RLVR alignment\\n\\n## Open Questions (scope expansion experiments planned)\\n1. ~~Does unpruned model also show reward-accuracy divergence?~~ → YES, confirmed: 81.27% = 81.27%\\n2. ~~What do RASP v9 fine-grained checkpoints show?~~ → Permanent collapse, step-5 eval = 60.65% (≈ SFT)\\n3. Can higher sparsity (25-30%) make SFT gap significant AND intensify GRPO collapse? (scope expansion Phase 1)\\n4. Does the collapse pattern reproduce on Qwen2.5-Math-7B? (scope expansion Phase 2)\\n5. Is there a GRPO config that avoids collapse on pruned models? (future work motivation)\\n\", \"total_chars\": 10165, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "cb752f74-4f9f-47ed-be1e-dcb4ae38f387",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — recovery_aware_struct_prune\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (ARR May 25 submission)\\\\n- Fallback: EMNLP 2026 Findings\\\\n- Deadline: ARR May 25, 2026\\\\n\\\\n## Core Insight (Redundancy-Stability Tradeoff)\\\\nRLVR alignment (GRPO) fundamentally fails on structurally pruned reasoning models: reward improves but accuracy does not — a pruning-induced reward hacking phenomenon. We show the failure mechanism via **collapse dynamics**: pruning method determines how fast GRPO collapses, and this speed is a diagnostic of structural damage type. Crucially, functional redundancy plays **opposite roles** under SFT vs RLVR recovery:\\\\n\\\\n- **SFT**: redundant structures (high CKA overlap) are safely removable — their function redistributes through gradient-based learning. CKA-aware pruning (RASP) yields marginal SFT advantage.\\\\n- **RLVR**: redundant structures provide **exploration stability** — backup paths that prevent policy collapse during RL. Removing them (as RASP does) accelerates collapse.\\\\n\\\\nThis creates a **Redundancy-Stability Tradeoff**: the structures optimal to prune for SFT recovery are exactly those needed for RLVR stability. Optimal pruning is fundamentally conditioned on the recovery paradigm.\\\\n\\\\n## Core Claims (3) — REVISED based on experimental evidence\\\\n\\\\n1. **GRPO reward-accuracy decoupling is universal; pruning adds training collapse**: GRPO does not improve reasoning accuracy for ANY model post-SFT — unpruned (**81.27% = SFT 81.27%, Δ=0.00pp, identical 1072/1319 correct**), Standard-pruned (58.91% vs 59.29%, Δ=-0.38pp), RASP-pruned (60.65% vs 61.49%, Δ=-0.84pp). Reward increases dramatically (unpruned: 0→0.661) yet accuracy is unchanged — a universal reward-accuracy decoupling under GRPO+GSM8K+greedy. The pruning-specific phenomenon is **training collapse**: RASP collapses permanently at step ~10 (frac_zero_std→0.95, grad→0.007), Standard shows transient dip at step ~60, while unpruned trains stably for 100 steps. GRPO's reward signal does not encode genuine reasoning improvement; pruning removes the structural capacity to even sustain RL training.\\\\n\\\\n2. **Collapse severity gradient diagnoses structural damage**: Three-model comparison reveals a clean severity gradient — RASP (removes redundant, protects unique): permanent collapse step ~10, peak reward 0.039; Standard (importance-only): transient dip step ~60, final reward 0.065; Unpruned: no collapse, final reward 0.661. The 6× speedup from Standard→RASP confirms that functional redundancy provides RLVR exploration stability. Collapse dynamics are a zero-cost diagnostic: fast collapse = aggressive redundancy removal = poor RL trainability.\\\\n\\\\n3. **Recovery method conditions optimal pruning strategy**: For SFT recovery, RASP shows marginal advantage (+2.2pp, RASP 61.49% vs Standard 59.29%, N=1319, p=0.25). For RLVR stability, RASP is actively harmful (6× faster collapse). The structures optimal to prune for SFT are exactly those needed for RLVR stability — a fundamental Redundancy-Stability Tradeoff. Consistent with \\\\\\\"RL Squeezes, SFT Expands\\\\\\\" (ICLR 2026).\\\\n\\\\n## Evidence Status (as of 2026-05-16, ALL CORE DATA COMPLETE)\\\\n\\\\n| Evidence | Status | Result |\\\\n|----------|--------|--------|\\\\n| Unpruned SFT eval (N=1319) | ✅ | 81.27% |\\\\n| Unpruned GRPO step-100 eval (N=1319) | ✅ | **81.27% (Δ=0.00pp, 1072/1319 = identical to SFT)** |\\\\n| Unpruned GRPO step-90 eval (N=1319) | ✅ | **80.59% (1063/1319, confirms stability across late training)** |\\\\n| Standard SFT eval (N=1319) | ✅ | 59.29% |\\\\n| Standard GRPO step-50 eval (N=1319) | ✅ | 58.91% (Δ=-0.38pp) |\\\\n| RASP SFT eval (N=1319) | ✅ | 61.49% |\\\\n| RASP GRPO step-5 eval (N=1319) | ✅ | 60.65% (Δ=-0.84pp) |\\\\n| RASP GRPO v9 collapse dynamics | ✅ | Permanent collapse step ~10, peak reward 0.039 |\\\\n| Standard GRPO v8 dynamics | ✅ | Transient dip step ~60, recovery step ~90 |\\\\n| Unpruned GRPO v2 dynamics | ✅ | No collapse, 100 steps stable, reward 0.661 |\\\\n| Alpha ablation (cal=512) | ✅ | U-shape: α≥1.0 > α≤0.5 post-prune |\\\\n| SFT gap significance | ⚠️ p=0.25 | Not significant at N=1319; scope expansion to higher sparsity planned |\\\\n| RASP GRPO step-10 eval (N=1319) | ✅ | **61.87% — collapse onset does NOT reduce accuracy (vs step-5 60.65%, p=0.52)** |\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: The reasoning model compression pipeline (prune → recover → align) assumes alignment is independent of pruning decisions. We show this assumption fails catastrophically: GRPO alignment on pruned models produces reward improvement without accuracy gain, followed by complete collapse. The pruning-alignment interaction is not merely suboptimal — it is fundamentally broken under current practice.\\\\n\\\\n- **Existing approaches & gaps**: Self-Healing (2025) claims RLVR recovers pruned reasoning models to 95%+ at 25% compression — but uses a single pruning ratio and does not report per-step accuracy during GRPO. GRASPrune (ACL 2026) provides SOTA budgeted structural pruning but doesn't study recovery or alignment at all. RESP (Dec 2025) uses reasoning-trace calibration without recovery. No work has documented GRPO collapse on pruned models, explained its mechanism, or shown that pruning strategy determines collapse dynamics.\\\\n\\\\n- **Our framing**: We present the first systematic study of how structural pruning interacts with RLVR alignment in reasoning LLMs. We introduce RASP (S(h) = I(h) × (1-F(h))^α) not as a universally superior method, but as a **diagnostic tool** that reveals the Redundancy-Stability Tradeoff: CKA-aware structure selection that benefits SFT recovery actively harms RLVR stability. This reframes the pruning-alignment relationship from \\\\\\\"which structures to remove for best recovery\\\\\\\" to \\\\\\\"recovery paradigm determines what counts as safe to remove.\\\\\\\"\\\\n\\\\n- **Headline result**: \\\\\\\"GRPO reward improvement never translates to accuracy gain (unpruned: reward 0→0.661, accuracy 81.27%→81.27%; identical 1072/1319 correct). But pruning causes GRPO training collapse: RASP-pruned collapses permanently at step 10, Standard-pruned at step 60, unpruned never. The severity gradient (RASP > Standard > Unpruned) reveals that structural redundancy — expendable for SFT — provides critical RL exploration stability.\\\\\\\"\\\\n\\\\n## Venue Fit\\\\n- EMNLP Efficient Methods track: structured pruning + reasoning model alignment failure analysis\\\\n- Negative/diagnostic results challenging published claims (Self-Healing) are high-impact at *ACL venues\\\\n- Reasoning model compression pipeline failures are immediately practical (timely: DeepSeek-R1, QwQ, Kimi-K1.5)\\\\n- Mechanistic analysis (collapse dynamics, reward-accuracy divergence) aligns with EMNLP empirical rigor\\\\n\\\\n## Venue Fit Risks\\\\n- **\\\\\\\"Just a negative result without solution\\\\\\\"**: Mitigate with (1) mechanistic explanation (redundancy-stability tradeoff), (2) RASP as diagnostic tool (collapse speed predicts pruning quality for RL), (3) actionable implication (SFT-only recovery is currently the safe path; RLVR needs pruning-aware modifications)\\\\n- **\\\\\\\"Single model\\\\\\\"**: DeepSeek-R1-Distill-Qwen-7B is the canonical open reasoning model; multi-method comparison (RASP/Standard/Unpruned) + multi-recovery (SFT/GRPO) compensates\\\\n- **\\\\\\\"GRPO config might be wrong\\\\\\\"**: Report hyperparameter sensitivity (alpha ablation), show collapse is robust across configs, cite Self-Healing uses similar GRPO setup\\\\n- **\\\\\\\"SFT gap not significant\\\\\\\"**: Frame honestly as marginal; the paper's contribution is the GRPO failure + mechanism, not the SFT comparison. SFT gap is supplementary context.\\\\n- **\\\\\\\"Collapse might be training instability, not pruning-specific\\\\\\\"**: Unpruned GRPO ran 100 steps with zero collapse (reward 0.661, stable frac_zero_std ≤0.275) — pruning-specificity confirmed\\\\n\\\\n## Anticipated Reviewer Concerns & Experimental Responses\\\\n\\\\n| Concern | Response | Supporting Experiment |\\\\n|---------|----------|----------------------|\\\\n| GRPO failure might be hyperparameter issue | Alpha ablation shows U-shape is robust; reward increases but accuracy never follows | alpha_ablation_sweep |\\\\n| Need unpruned control for pruning-specificity | Unpruned GRPO: 100 steps stable, no collapse, reward 0.661 vs pruned collapse at step 10-60 | grpo_unpruned_v2 |\\\\n| SFT gap not significant | Acknowledged; paper's main claim is GRPO failure, not SFT superiority | sft_eval N=1319 |\\\\n| Collapse speed might not generalize | Multi-method comparison (RASP/Standard) + multi-config (alpha sweep) | grpo_v8, grpo_v9 |\\\\n| How does this relate to Self-Healing claims? | Self-Healing uses 25% unstructured; our structured pruning at 20% creates different damage pattern | Discussion section |\\\\n| What's the practical recommendation? | SFT recovery only for structurally pruned models; RLVR requires pruning-aware alignment (future work) | All experiments |\\\\n| CKA-aware pruning hurts RLVR — why publish RASP? | RASP is the diagnostic tool that REVEALS the tradeoff; its failure under RLVR is the evidence | grpo_v9 vs grpo_v8 |\\\\n\\\\n## Key Differentiations\\\\n- **vs Self-Healing (2025)**: Claims RLVR recovers pruned models → we show GRPO fails (reward hacking + collapse); different pruning granularity and controlled collapse analysis\\\\n- **vs MPruner (2024)**: inter-layer CKA for depth pruning in CNNs → we use intra-layer CKA as diagnostic tool revealing redundancy-stability tradeoff in reasoning LLMs\\\\n- **vs GRASPrune (ACL 2026)**: SOTA budgeted pruning without recovery/alignment study → we study the full prune-recover-align pipeline failure\\\\n- **vs RESP (Dec 2025)**: reasoning-trace calibration without recovery → we study recovery paradigm interaction\\\\n- **vs PASER (2025)**: optimizes recovery DATA → we show even optimal pruning STRUCTURE cannot save RLVR alignment\\\\n\\\\n## Open Questions (scope expansion experiments planned)\\\\n1. ~~Does unpruned model also show reward-accuracy divergence?~~ → YES, confirmed: 81.27% = 81.27%\\\\n2. ~~What do RASP v9 fine-grained checkpoints show?~~ → Permanent collapse, step-5 eval = 60.65% (≈ SFT)\\\\n3. Can higher sparsity (25-30%) make SFT gap significant AND intensify GRPO collapse? (scope expansion Phase 1)\\\\n4. Does the collapse pattern reproduce on Qwen2.5-Math-7B? (scope expansion Phase 2)\\\\n5. Is there a GRPO config that avoids collapse on pruned models? (future work motivation)\\\\n\\\", \\\"total_chars\\\": 10165, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper_framing.md\", \"content\": \"# Paper Framing — recovery_aware_struct_prune\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 submission)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Insight (Redundancy-Stability Tradeoff)\\nRLVR alignment (GRPO) fundamentally fails on structurally pruned reasoning models: reward improves but accuracy does not — a pruning-induced reward hacking phenomenon. We show the failure mechanism via **collapse dynamics**: pruning method determines how fast GRPO collapses, and this speed is a diagnostic of structural damage type. Crucially, functional redundancy plays **opposite roles** under SFT vs RLVR recovery:\\n\\n- **SFT**: redundant structures (high CKA overlap) are safely removable — their function redistributes through gradient-based learning. CKA-aware pruning (RASP) yields marginal SFT advantage.\\n- **RLVR**: redundant structures provide **exploration stability** — backup paths that prevent policy collapse during RL. Removing them (as RASP does) accelerates collapse.\\n\\nThis creates a **Redundancy-Stability Tradeoff**: the structures optimal to prune for SFT recovery are exactly those needed for RLVR stability. Optimal pruning is fundamentally conditioned on the recovery paradigm.\\n\\n## Core Claims (3) — REVISED based on experimental evidence\\n\\n1. **GRPO reward-accuracy decoupling is universal; pruning adds training collapse**: GRPO does not improve reasoning accuracy for ANY model post-SFT — unpruned (**81.27% = SFT 81.27%, Δ=0.00pp, identical 1072/1319 correct**), Standard-pruned (58.91% vs 59.29%, Δ=-0.38pp), RASP-pruned (60.65% vs 61.49%, Δ=-0.84pp). Reward increases dramatically (unpruned: 0→0.661) yet accuracy is unchanged — a universal reward-accuracy decoupling under GRPO+GSM8K+greedy. The pruning-specific phenomenon is **training collapse**: RASP collapses permanently at step ~10 (frac_zero_std→0.95, grad→0.007), Standard shows transient dip at step ~60, while unpruned trains stably for 100 steps. GRPO's reward signal does not encode genuine reasoning improvement; pruning removes the structural capacity to even sustain RL training.\\n\\n2. **Collapse severity gradient diagnoses structural damage**: Three-model comparison reveals a clean severity gradient — RASP (removes redundant, protects unique): permanent collapse step ~10, peak reward 0.039; Standard (importance-only): transient dip step ~60, final reward 0.065; Unpruned: no collapse, final reward 0.661. The 6× speedup from Standard→RASP confirms that functional redundancy provides RLVR exploration stability. Collapse dynamics are a zero-cost diagnostic: fast collapse = aggressive redundancy removal = poor RL trainability.\\n\\n3. **Recovery method conditions optimal pruning strategy**: For SFT recovery, RASP shows marginal advantage (+2.2pp, RASP 61.49% vs Standard 59.29%, N=1319, p=0.25). For RLVR stability, RASP is actively harmful (6× faster collapse). The structures optimal to prune for SFT are exactly those needed for RLVR stability — a fundamental Redundancy-Stability Tradeoff. Consistent with \\\"RL Squeezes, SFT Expands\\\" (ICLR 2026).\\n\\n## Evidence Status (as of 2026-05-16, ALL CORE DATA COMPLETE)\\n\\n| Evidence | Status | Result |\\n|----------|--------|--------|\\n| Unpruned SFT eval (N=1319) | ✅ | 81.27% |\\n| Unpruned GRPO step-100 eval (N=1319) | ✅ | **81.27% (Δ=0.00pp, 1072/1319 = identical to SFT)** |\\n| Unpruned GRPO step-90 eval (N=1319) | ✅ | **80.59% (1063/1319, confirms stability across late training)** |\\n| Standard SFT eval (N=1319) | ✅ | 59.29% |\\n| Standard GRPO step-50 eval (N=1319) | ✅ | 58.91% (Δ=-0.38pp) |\\n| RASP SFT eval (N=1319) | ✅ | 61.49% |\\n| RASP GRPO step-5 eval (N=1319) | ✅ | 60.65% (Δ=-0.84pp) |\\n| RASP GRPO v9 collapse dynamics | ✅ | Permanent collapse step ~10, peak reward 0.039 |\\n| Standard GRPO v8 dynamics | ✅ | Transient dip step ~60, recovery step ~90 |\\n| Unpruned GRPO v2 dynamics | ✅ | No collapse, 100 steps stable, reward 0.661 |\\n| Alpha ablation (cal=512) | ✅ | U-shape: α≥1.0 > α≤0.5 post-prune |\\n| SFT gap significance | ⚠️ p=0.25 | Not significant at N=1319; scope expansion to higher sparsity planned |\\n| RASP GRPO step-10 eval (N=1319) | ✅ | **61.87% — collapse onset does NOT reduce accuracy (vs step-5 60.65%, p=0.52)** |\\n\\n## Story Spine\\n\\n- **Problem**: The reasoning model compression pipeline (prune → recover → align) assumes alignment is independent of pruning decisions. We show this assumption fails catastrophically: GRPO alignment on pruned models produces reward improvement without accuracy gain, followed by complete collapse. The pruning-alignment interaction is not merely suboptimal — it is fundamentally broken under current practice.\\n\\n- **Existing approaches & gaps**: Self-Healing (2025) claims RLVR recovers pruned reasoning models to 95%+ at 25% compression — but uses a single pruning ratio and does not report per-step accuracy during GRPO. GRASPrune (ACL 2026) provides SOTA budgeted structural pruning but doesn't study recovery or alignment at all. RESP (Dec 2025) uses reasoning-trace calibration without recovery. No work has documented GRPO collapse on pruned models, explained its mechanism, or shown that pruning strategy determines collapse dynamics.\\n\\n- **Our framing**: We present the first systematic study of how structural pruning interacts with RLVR alignment in reasoning LLMs. We introduce RASP (S(h) = I(h) × (1-F(h))^α) not as a universally superior method, but as a **diagnostic tool** that reveals the Redundancy-Stability Tradeoff: CKA-aware structure selection that benefits SFT recovery actively harms RLVR stability. This reframes the pruning-alignment relationship from \\\"which structures to remove for best recovery\\\" to \\\"recovery paradigm determines what counts as safe to remove.\\\"\\n\\n- **Headline result**: \\\"GRPO reward improvement never translates to accuracy gain (unpruned: reward 0→0.661, accuracy 81.27%→81.27%; identical 1072/1319 correct). But pruning causes GRPO training collapse: RASP-pruned collapses permanently at step 10, Standard-pruned at step 60, unpruned never. The severity gradient (RASP > Standard > Unpruned) reveals that structural redundancy — expendable for SFT — provides critical RL exploration stability.\\\"\\n\\n## Venue Fit\\n- EMNLP Efficient Methods track: structured pruning + reasoning model alignment failure analysis\\n- Negative/diagnostic results challenging published claims (Self-Healing) are high-impact at *ACL venues\\n- Reasoning model compression pipeline failures are immediately practical (timely: DeepSeek-R1, QwQ, Kimi-K1.5)\\n- Mechanistic analysis (collapse dynamics, reward-accuracy divergence) aligns with EMNLP empirical rigor\\n\\n## Venue Fit Risks\\n- **\\\"Just a negative result without solution\\\"**: Mitigate with (1) mechanistic explanation (redundancy-stability tradeoff), (2) RASP as diagnostic tool (collapse speed predicts pruning quality for RL), (3) actionable implication (SFT-only recovery is currently the safe path; RLVR needs pruning-aware modifications)\\n- **\\\"Single model\\\"**: DeepSeek-R1-Distill-Qwen-7B is the canonical open reasoning model; multi-method comparison (RASP/Standard/Unpruned) + multi-recovery (SFT/GRPO) compensates\\n- **\\\"GRPO config might be wrong\\\"**: Report hyperparameter sensitivity (alpha ablation), show collapse is robust across configs, cite Self-Healing uses similar GRPO setup\\n- **\\\"SFT gap not significant\\\"**: Frame honestly as marginal; the paper's contribution is the GRPO failure + mechanism, not the SFT comparison. SFT gap is supplementary context.\\n- **\\\"Collapse might be training instability, not pruning-specific\\\"**: Unpruned GRPO ran 100 steps with zero collapse (reward 0.661, stable frac_zero_std ≤0.275) — pruning-specificity confirmed\\n\\n## Anticipated Reviewer Concerns & Experimental Responses\\n\\n| Concern | Response | Supporting Experiment |\\n|---------|----------|----------------------|\\n| GRPO failure might be hyperparameter issue | Alpha ablation shows U-shape is robust; reward increases but accuracy never follows | alpha_ablation_sweep |\\n| Need unpruned control for pruning-specificity | Unpruned GRPO: 100 steps stable, no collapse, reward 0.661 vs pruned collapse at step 10-60 | grpo_unpruned_v2 |\\n| SFT gap not significant | Acknowledged; paper's main claim is GRPO failure, not SFT superiority | sft_eval N=1319 |\\n| Collapse speed might not generalize | Multi-method comparison (RASP/Standard) + multi-config (alpha sweep) | grpo_v8, grpo_v9 |\\n| How does this relate to Self-Healing claims? | Self-Healing uses 25% unstructured; our structured pruning at 20% creates different damage pattern | Discussion section |\\n| What's the practical recommendation? | SFT recovery only for structurally pruned models; RLVR requires pruning-aware alignment (future work) | All experiments |\\n| CKA-aware pruning hurts RLVR — why publish RASP? | RASP is the diagnostic tool that REVEALS the tradeoff; its failure under RLVR is the evidence | grpo_v9 vs grpo_v8 |\\n\\n## Key Differentiations\\n- **vs Self-Healing (2025)**: Claims RLVR recovers pruned models → we show GRPO fails (reward hacking + collapse); different pruning granularity and controlled collapse analysis\\n- **vs MPruner (2024)**: inter-layer CKA for depth pruning in CNNs → we use intra-layer CKA as diagnostic tool revealing redundancy-stability tradeoff in reasoning LLMs\\n- **vs GRASPrune (ACL 2026)**: SOTA budgeted pruning without recovery/alignment study → we study the full prune-recover-align pipeline failure\\n- **vs RESP (Dec 2025)**: reasoning-trace calibration without recovery → we study recovery paradigm interaction\\n- **vs PASER (2025)**: optimizes recovery DATA → we show even optimal pruning STRUCTURE cannot save RLVR alignment\\n\\n## Open Questions (scope expansion experiments planned)\\n1. ~~Does unpruned model also show reward-accuracy divergence?~~ → YES, confirmed: 81.27% = 81.27%\\n2. ~~What do RASP v9 fine-grained checkpoints show?~~ → Permanent collapse, step-5 eval = 60.65% (≈ SFT)\\n3. Can higher sparsity (25-30%) make SFT gap significant AND intensify GRPO collapse? (scope expansion Phase 1)\\n4. Does the collapse pattern reproduce on Qwen2.5-Math-7B? (scope expansion Phase 2)\\n5. Is there a GRPO config that avoids collapse on pruned models? (future work motivation)\\n\", \"total_chars\": 10165, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the new Introduction based on:

1. The new confirmed narrative (GRPO fails on pruned models, RASP as diagnostic tool)
2. The 5-paragraph structure specified
3. Available citation keys from references.bib
4. Writing norms (no dashes, no -ing phrases, etc.)

Let me draft the Introduction:

**Paragraph 1 (Background)**: Reasoning LLMs + structured pruning + recovery pipeline. Hook with the unpruned GRPO result showing reward-accuracy decoupling.

**Paragraph 2 (Problem importance)**: Self-Healing claims + gap in knowledge about step-level dynamics.


**Paragraph 3 (Existing methods insufficient)**: Prior work on GRASPrune, RESP, and LLM-Pruner focuses on optimizing pruning strategies without examining how alignment training interacts with model compression, leaving the mechanisms of performance collapse undocumented.

**Paragraph 4 (Our contribution)**: We conduct a systematic investigation into how pruning affects reinforcement learning from verification rewards, introducing RASP as a diagnostic tool to reveal the redundancy-stability tradeoff that emerges during this interaction.

**Paragraph 5 (Contribution list)**: Three main claims about the phenomenon, its characterization, and recovery strategies.

Now I'm reviewing the relevant citations across pruning methods, alignment techniques, and evaluation benchmarks to ground these contributions in the literature. I'm noting that structured pruning removes entire attention heads or MLP channels to compress models efficiently, but this severely hurts reasoning ability, so a three-stage recovery process is needed: pruning, then supervised fine-tuning, then alignment with reinforcement learning. On the DeepSeek-R1-Distill-Qwen-7B model, just 100 steps of Group Relative Policy Optimization appears sufficient to restore performance.

But here's the catch: the reward signal jumps dramatically from 0 to 0.661, yet accuracy on GSM8K stays flat at 81.27%, with over 1000 test problems producing identical answers before and after alignment. The reward improvement is misleading—GRPO is just learning to format outputs differently without actually improving the underlying reasoning. This matters because prior work claims RLVR-based recovery can restore pruned models to 95%+ performance at 25% compression, but those evaluations only look at final accuracy and don't track what happens during the actual training steps. If GRPO is gaming the reward signal rather than genuinely improving reasoning, the whole recovery pipeline might be less effective than it appears.

The problem gets worse on pruned models themselves. When I apply GRPO to structurally pruned architectures, training completely collapses—gradient norms drop to near zero and the model stops generating diverse outputs. This hasn't been documented or explained before. Meanwhile, existing pruning methods like GRASPrune, RESP, LLM-Pruner, and Bonsai all focus on immediate post-pruning quality without thinking about how the model will behave during downstream alignment training.

Recent work like PASER and PAT treats pruning and recovery as independent problems—you decide what to remove, then you fix whatever's left. But the real issue is whether the pruning decisions themselves make RLVR training impossible, not just whether accuracy drops. Prior research shows RL and SFT reshape model representations in opposite ways, which suggests pruning could interact badly with alignment, yet nobody's actually studied this interaction. So I'm conducting the first systematic investigation into how structural pruning affects RLVR alignment in reasoning models.

Testing on DeepSeek-R1-Distill-Qwen-7B at 20% sparsity, I found that GRPO training on pruned models catastrophically fails, with the severity depending entirely on which structures get pruned. To understand this, I developed Recovery-Aware Structured Pruning, which uses Centered Kernel Alignment to identify and preserve functionally unique structures while removing redundant ones. Interestingly, this approach gives a small SFT boost but causes GRPO to collapse almost immediately—much faster than standard pruning—which points to a deeper tradeoff: the redundancy that's safe to remove for SFT recovery actually stabilizes RLVR training.

The key insight is that this pruning method isn't universally better, but rather a diagnostic tool that reveals how structural choices fundamentally affect RL trainability. Looking at the contributions, I'm documenting that GRPO consistently decouples reward from accuracy improvements across both pruned and unpruned models, and on pruned models specifically triggers a collapse where gradients vanish. The severity of this collapse varies by pruning strategy—my method causes permanent failure at step 10, importance-only pruning shows a temporary dip around step 60, while unpruned models remain stable.

This 6x difference in training steps demonstrates that functional redundancy is essential for exploration stability. The deeper finding is the Redundancy-Stability Tradeoff: the structures that are optimal to remove for SFT recovery are precisely the ones needed to maintain RL stability, meaning the best pruning strategy depends entirely on whether you're recovering through supervised fine-tuning or reinforcement learning.

Now I'm checking the section references and making sure the hook about the unpruned model's reward-accuracy mismatch sets up the failure narrative effectively. The draft feels solid, so I'll finalize it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "a16aa889-cabc-4365-9ed8-e85be09b6d6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7Nctu1c8xhFP881XaV3vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3467,
      "cache_read_input_tokens": 33290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3467
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

_source line 16_

Now I have everything I need. Let me write the new Introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "a4a89eb5-d2a4-4a4f-a050-a2f5e8e7ab07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7Nctu1c8xhFP881XaV3vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3467,
      "cache_read_input_tokens": 33290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3467
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

_source line 17_

<details open><summary>🔧 Tool call — Write · `toolu_01DKbUcGHC47NQVVDgP39CcP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
  "content": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge Language Models (LLMs) trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong mathematical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.\nStructured pruning, which removes entire attention heads or MLP channels, provides a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.\nBecause structured pruning at moderate sparsity severely degrades reasoning ability, a post-pruning recovery stage is essential.\nThe standard compression pipeline therefore proceeds in three stages: prune, recover via Supervised Fine-Tuning (SFT), then align via RLVR to restore reasoning quality.\nThis final alignment step appears straightforward: on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1}, 100 steps of Group Relative Policy Optimization (GRPO;~\\citealp{shao2024grpo}) raises the reward from 0 to 0.661.\nYet accuracy on GSM8K~\\citep{cobbe2021gsm8k} remains exactly 81.27\\%, with 1,072 of 1,319 test problems producing identical correct answers before and after alignment.\nThe reward improvement is an illusion: GRPO learns to produce outputs that score higher rewards without solving additional problems.\n\nThis observation has immediate practical consequences for the compression pipeline.\n\\citet{selfhealing2025} report that RLVR-based recovery restores pruned reasoning models to 95\\%+ of original performance at 25\\% compression, establishing RLVR as the preferred recovery paradigm.\nHowever, their evaluation reports only final-checkpoint accuracy and does not document per-step training dynamics during GRPO.\nIf GRPO reward gains fail to reflect genuine reasoning improvement even on unpruned models, the claim that RLVR ``recovers'' pruned models demands scrutiny.\nThe problem becomes acute on pruned architectures: we observe that GRPO training on structurally pruned models not only fails to improve accuracy but triggers complete training collapse, where gradient norms approach zero and the model ceases to produce diverse outputs.\nNo prior work has documented or explained this failure mode.\n\nCurrent structured pruning methods for reasoning LLMs optimize for immediate post-pruning quality without studying downstream alignment behavior.\nGRASPrune~\\citep{graspprune2026} introduces global gating for budgeted compression.\nRESP~\\citep{resp2025} uses reasoning-trace self-reflection for calibration.\nLLM-Pruner~\\citep{llmpruner2023} and Bonsai~\\citep{bonsai2025} target general LLM compression.\nPASER~\\citep{paser2025} optimizes recovery data selection, while PAT~\\citep{pat2025} proposes pruning-aware tuning.\nAll treat pruning and recovery as separable stages: pruning methods optimize which structures to remove, and recovery methods operate on whatever architecture remains.\nThe critical question of whether pruning decisions affect RLVR trainability (not just post-prune accuracy) remains unexplored.\n\\citet{rlsqueezes2026} show that RL and SFT impose fundamentally different demands on model representations, with RL compressing solution paths while SFT expands them.\nThis suggests that pruning-alignment interactions could be substantial, yet no work has studied them.\n\nWe present the first systematic study of how structural pruning interacts with RLVR alignment in reasoning LLMs.\nOur experiments on DeepSeek-R1-Distill-Qwen-7B at 20\\% structured sparsity reveal a fundamental failure: GRPO training on pruned models produces training collapse whose severity depends on the pruning strategy.\nTo diagnose this interaction, we introduce Recovery-Aware Structured Pruning (\\rasp{}), which incorporates intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}) into pruning decisions through a composite score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that balances importance $I$ against functional overlap $F$.\n\\rasp{} preferentially removes structures with high functional redundancy while protecting unique ones.\nThis design yields a marginal SFT advantage (+2.2 percentage points over importance-only pruning) but produces the fastest GRPO collapse: permanent at step 10, versus a transient dip at step 60 for standard importance-only pruning, versus no collapse for the unpruned model.\nThe contrast reveals what we term the \\textbf{Redundancy-Stability Tradeoff}: functional redundancy that is expendable under SFT recovery provides critical exploration stability under RLVR.\n\\rasp{} therefore serves not as a universally superior pruning method, but as a controlled diagnostic that exposes how structure selection determines RL trainability.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We document universal GRPO reward-accuracy decoupling: reward improves while accuracy remains unchanged on both pruned and unpruned models post-SFT. On pruned models, GRPO additionally triggers training collapse with gradient norms approaching zero (\\S\\ref{sec:grpo_failure}).\n    \\item We establish a collapse severity gradient that diagnoses structural damage type: \\rasp{}-pruned models (redundancy removed) collapse permanently at step 10, importance-only pruned models exhibit a transient dip at step 60, and the unpruned model trains stably for 100 steps. The 6$\\times$ collapse acceleration from standard to \\rasp{} confirms that functional redundancy provides RL exploration stability (\\S\\ref{sec:collapse_analysis}).\n    \\item We identify the Redundancy-Stability Tradeoff: structures optimal to prune for SFT recovery are exactly those needed for RLVR stability. Optimal pruning is therefore conditioned on the recovery paradigm, consistent with the RL-SFT representation divergence documented by \\citet{rlsqueezes2026} (\\S\\ref{sec:tradeoff}).\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "fa7562bb-1b28-408b-bd94-771fd9a3a1d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7Nctu1c8xhFP881XaV3vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3467,
      "cache_read_input_tokens": 33290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3467
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

_source line 18 · 2026-05-17T23:22:45.330Z_

<details><summary>↩ Tool result · `toolu_01DKbUcGHC47NQVVDgP39CcP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "22f1b6d7-8017-41a4-a6cb-e403db739740",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
    "content": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge Language Models (LLMs) trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong mathematical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.\nStructured pruning, which removes entire attention heads or MLP channels, provides a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.\nBecause structured pruning at moderate sparsity severely degrades reasoning ability, a post-pruning recovery stage is essential.\nThe standard compression pipeline therefore proceeds in three stages: prune, recover via Supervised Fine-Tuning (SFT), then align via RLVR to restore reasoning quality.\nThis final alignment step appears straightforward: on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1}, 100 steps of Group Relative Policy Optimization (GRPO;~\\citealp{shao2024grpo}) raises the reward from 0 to 0.661.\nYet accuracy on GSM8K~\\citep{cobbe2021gsm8k} remains exactly 81.27\\%, with 1,072 of 1,319 test problems producing identical correct answers before and after alignment.\nThe reward improvement is an illusion: GRPO learns to produce outputs that score higher rewards without solving additional problems.\n\nThis observation has immediate practical consequences for the compression pipeline.\n\\citet{selfhealing2025} report that RLVR-based recovery restores pruned reasoning models to 95\\%+ of original performance at 25\\% compression, establishing RLVR as the preferred recovery paradigm.\nHowever, their evaluation reports only final-checkpoint accuracy and does not document per-step training dynamics during GRPO.\nIf GRPO reward gains fail to reflect genuine reasoning improvement even on unpruned models, the claim that RLVR ``recovers'' pruned models demands scrutiny.\nThe problem becomes acute on pruned architectures: we observe that GRPO training on structurally pruned models not only fails to improve accuracy but triggers complete training collapse, where gradient norms approach zero and the model ceases to produce diverse outputs.\nNo prior work has documented or explained this failure mode.\n\nCurrent structured pruning methods for reasoning LLMs optimize for immediate post-pruning quality without studying downstream alignment behavior.\nGRASPrune~\\citep{graspprune2026} introduces global gating for budgeted compression.\nRESP~\\citep{resp2025} uses reasoning-trace self-reflection for calibration.\nLLM-Pruner~\\citep{llmpruner2023} and Bonsai~\\citep{bonsai2025} target general LLM compression.\nPASER~\\citep{paser2025} optimizes recovery data selection, while PAT~\\citep{pat2025} proposes pruning-aware tuning.\nAll treat pruning and recovery as separable stages: pruning methods optimize which structures to remove, and recovery methods operate on whatever architecture remains.\nThe critical question of whether pruning decisions affect RLVR trainability (not just post-prune accuracy) remains unexplored.\n\\citet{rlsqueezes2026} show that RL and SFT impose fundamentally different demands on model representations, with RL compressing solution paths while SFT expands them.\nThis suggests that pruning-alignment interactions could be substantial, yet no work has studied them.\n\nWe present the first systematic study of how structural pruning interacts with RLVR alignment in reasoning LLMs.\nOur experiments on DeepSeek-R1-Distill-Qwen-7B at 20\\% structured sparsity reveal a fundamental failure: GRPO training on pruned models produces training collapse whose severity depends on the pruning strategy.\nTo diagnose this interaction, we introduce Recovery-Aware Structured Pruning (\\rasp{}), which incorporates intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}) into pruning decisions through a composite score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that balances importance $I$ against functional overlap $F$.\n\\rasp{} preferentially removes structures with high functional redundancy while protecting unique ones.\nThis design yields a marginal SFT advantage (+2.2 percentage points over importance-only pruning) but produces the fastest GRPO collapse: permanent at step 10, versus a transient dip at step 60 for standard importance-only pruning, versus no collapse for the unpruned model.\nThe contrast reveals what we term the \\textbf{Redundancy-Stability Tradeoff}: functional redundancy that is expendable under SFT recovery provides critical exploration stability under RLVR.\n\\rasp{} therefore serves not as a universally superior pruning method, but as a controlled diagnostic that exposes how structure selection determines RL trainability.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We document universal GRPO reward-accuracy decoupling: reward improves while accuracy remains unchanged on both pruned and unpruned models post-SFT. On pruned models, GRPO additionally triggers training collapse with gradient norms approaching zero (\\S\\ref{sec:grpo_failure}).\n    \\item We establish a collapse severity gradient that diagnoses structural damage type: \\rasp{}-pruned models (redundancy removed) collapse permanently at step 10, importance-only pruned models exhibit a transient dip at step 60, and the unpruned model trains stably for 100 steps. The 6$\\times$ collapse acceleration from standard to \\rasp{} confirms that functional redundancy provides RL exploration stability (\\S\\ref{sec:collapse_analysis}).\n    \\item We identify the Redundancy-Stability Tradeoff: structures optimal to prune for SFT recovery are exactly those needed for RLVR stability. Optimal pruning is therefore conditioned on the recovery paradigm, consistent with the RL-SFT representation divergence documented by \\citet{rlsqueezes2026} (\\S\\ref{sec:tradeoff}).\n\\end{enumerate}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 38,
        "newStart": 1,
        "newLines": 42,
        "lines": [
          " \\section{Introduction}",
          " \\label{sec:intro}",
          " ",
          "-Large language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.",
          "-Structured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.",
          "-However, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.",
          "-\\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.",
          "+Large Language Models (LLMs) trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong mathematical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.",
          "+Structured pruning, which removes entire attention heads or MLP channels, provides a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.",
          "+Because structured pruning at moderate sparsity severely degrades reasoning ability, a post-pruning recovery stage is essential.",
          "+The standard compression pipeline therefore proceeds in three stages: prune, recover via Supervised Fine-Tuning (SFT), then align via RLVR to restore reasoning quality.",
          "+This final alignment step appears straightforward: on an unpruned DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1}, 100 steps of Group Relative Policy Optimization (GRPO;~\\citealp{shao2024grpo}) raises the reward from 0 to 0.661.",
          "+Yet accuracy on GSM8K~\\citep{cobbe2021gsm8k} remains exactly 81.27\\%, with 1,072 of 1,319 test problems producing identical correct answers before and after alignment.",
          "+The reward improvement is an illusion: GRPO learns to produce outputs that score higher rewards without solving additional problems.",
          " ",
          "-Despite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.",
          "-No prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.",
          "-This gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.",
          "-The optimal set of structures to retain should therefore depend on the recovery paradigm.",
          "+This observation has immediate practical consequences for the compression pipeline.",
          "+\\citet{selfhealing2025} report that RLVR-based recovery restores pruned reasoning models to 95\\%+ of original performance at 25\\% compression, establishing RLVR as the preferred recovery paradigm.",
          "+However, their evaluation reports only final-checkpoint accuracy and does not document per-step training dynamics during GRPO.",
          "+If GRPO reward gains fail to reflect genuine reasoning improvement even on unpruned models, the claim that RLVR ``recovers'' pruned models demands scrutiny.",
          "+The problem becomes acute on pruned architectures: we observe that GRPO training on structurally pruned models not only fails to improve accuracy but triggers complete training collapse, where gradient norms approach zero and the model ceases to produce diverse outputs.",
          "+No prior work has documented or explained this failure mode.",
          " ",
          "-We hypothesize that \\emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.",
          "-If a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.",
          "-Conversely, structures with unique, non-redundant computations are difficult to recover once removed.",
          "-This yields what we term the \\textbf{Redundancy Paradox}: counterintuitively, the structures most valuable to retain for post-RLVR recovery are not the most important ones, but the most \\emph{functionally unique} ones.",
          "-Recovery-aware pruning therefore \\emph{preferentially removes} important-but-redundant structures---whose high overlap means RLVR can redistribute their function across retained peers---while protecting functionally unique structures that, once removed, leave an irrecoverable gap.",
          "-Standard importance-only pruning, by contrast, protects high-importance structures regardless of redundancy, inadvertently removing unique structures whose function cannot be recovered.",
          "+Current structured pruning methods for reasoning LLMs optimize for immediate post-pruning quality without studying downstream alignment behavior.",
          "+GRASPrune~\\citep{graspprune2026} introduces global gating for budgeted compression.",
          "+RESP~\\citep{resp2025} uses reasoning-trace self-reflection for calibration.",
          "+LLM-Pruner~\\citep{llmpruner2023} and Bonsai~\\citep{bonsai2025} target general LLM compression.",
          "+PASER~\\citep{paser2025} optimizes recovery data selection, while PAT~\\citep{pat2025} proposes pruning-aware tuning.",
          "+All treat pruning and recovery as separable stages: pruning methods optimize which structures to remove, and recovery methods operate on whatever architecture remains.",
          "+The critical question of whether pruning decisions affect RLVR trainability (not just post-prune accuracy) remains unexplored.",
          "+\\citet{rlsqueezes2026} show that RL and SFT impose fundamentally different demands on model representations, with RL compressing solution paths while SFT expands them.",
          "+This suggests that pruning-alignment interactions could be substantial, yet no work has studied them.",
          " ",
          "-We propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.",
          "-In Stage~1, \\rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}).",
          "-In Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important \\emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.",
          "-In Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\\citep{shao2024grpo} to restore reasoning ability.",
          "-Unlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.",
          "+We present the first systematic study of how structural pruning interacts with RLVR alignment in reasoning LLMs.",
          "+Our experiments on DeepSeek-R1-Distill-Qwen-7B at 20\\% structured sparsity reveal a fundamental failure: GRPO training on pruned models produces training collapse whose severity depends on the pruning strategy.",
          "+To diagnose this interaction, we introduce Recovery-Aware Structured Pruning (\\rasp{}), which incorporates intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}) into pruning decisions through a composite score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that balances importance $I$ against functional overlap $F$.",
          "+\\rasp{} preferentially removes structures with high functional redundancy while protecting unique ones.",
          "+This design yields a marginal SFT advantage (+2.2 percentage points over importance-only pruning) but produces the fastest GRPO collapse: permanent at step 10, versus a transient dip at step 60 for standard importance-only pruning, versus no collapse for the unpruned model.",
          "+The contrast reveals what we term the \\textbf{Redundancy-Stability Tradeoff}: functional redundancy that is expendable under SFT recovery provides critical exploration stability under RLVR.",
          "+\\rasp{} therefore serves not as a universally superior pruning method, but as a controlled diagnostic that exposes how structure selection determines RL trainability.",
          " ",
          "-We evaluate \\rasp{} on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% structured sparsity.",
          "-At matched sparsity, \\rasp{}-pruned models retain 29\\% GSM8K~\\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.",
          "-After SFT warmup, both pruning strategies recover substantially (57--64\\%), with detailed comparison deferred to \\S\\ref{sec:experiments}.",
          "-[TBD: GRPO results]",
          "-",
          " Our contributions are:",
          " \\begin{enumerate}[nosep,leftmargin=*]",
          "-    \\item We identify the \\emph{Redundancy Paradox}---that functional redundancy enables RLVR to recover the function of removed structures, making important-but-redundant structures safely removable while functionally unique structures become critical to retain---and formalize it through intra-layer CKA-based functional overlap scoring.",
          "-    \\item We propose \\rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\\% post-prune GSM8K accuracy versus 1\\% for importance-only pruning at matched 20\\% sparsity on DeepSeek-R1-Distill-Qwen-7B.",
          "-    \\item [TBD: GRPO recovery results---contribution demonstrating that \\rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]",
          "-    \\item We present preliminary evidence that the optimal pruning strategy may be conditioned on the recovery paradigm~\\citep{frankle2019lth}, supporting the notion of \\emph{paradigm-conditioned prunability} [TBD: pending GRPO confirmation and statistical validation].",
          "+    \\item We document universal GRPO reward-accuracy decoupling: reward improves while accuracy remains unchanged on both pruned and unpruned models post-SFT. On pruned models, GRPO additionally triggers training collapse with gradient norms approaching zero (\\S\\ref{sec:grpo_failure}).",
          "+    \\item We establish a collapse severity gradient that diagnoses structural damage type: \\rasp{}-pruned models (redundancy removed) collapse permanently at step 10, importance-only pruned models exhibit a transient dip at step 60, and the unpruned model trains stably for 100 steps. The 6$\\times$ collapse acceleration from standard to \\rasp{} confirms that functional redundancy provides RL exploration stability (\\S\\ref{sec:collapse_analysis}).",
          "+    \\item We identify the Redundancy-Stability Tradeoff: structures optimal to prune for SFT recovery are exactly those needed for RLVR stability. Optimal pruning is therefore conditioned on the recovery paradigm, consistent with the RL-SFT representation divergence documented by \\citet{rlsqueezes2026} (\\S\\ref{sec:tradeoff}).",
          " \\end{enumerate}"
        ]
      }
    ],
    "originalFile": "\\section{Introduction}\n\\label{sec:intro}\n\nLarge language models trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong performance on mathematical and logical reasoning~\\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.\nStructured pruning---removing entire attention heads or MLP channels---offers a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\\citep{llmpruner2023,graspprune2026}.\nHowever, structured pruning at moderate sparsity severely degrades reasoning ability, necessitating a post-pruning recovery stage.\n\\citet{selfhealing2025} show that RLVR-based recovery substantially outperforms SFT-based recovery for pruned reasoning models, establishing RLVR as the preferred recovery paradigm.\n\nDespite this, current approaches treat pruning and recovery as independent steps: pruning methods optimize for immediate post-pruning accuracy~\\citep{resp2025,graspprune2026,bonsai2025}, while recovery methods operate on whatever architecture they receive~\\citep{selfhealing2025,paser2025}.\nNo prior work has studied whether the \\emph{choice} of what to prune affects how well RLVR can subsequently recover reasoning---or whether this interaction differs from SFT-based recovery.\nThis gap is consequential because RLVR and SFT impose fundamentally different functional demands on the retained architecture: \\citet{rlsqueezes2026} show that RLVR recovers through global exploration and path compression, while SFT recovers through local trajectory imitation.\nThe optimal set of structures to retain should therefore depend on the recovery paradigm.\n\nWe hypothesize that \\emph{functional overlap}---the degree to which a structure's computation is redundant with its within-layer peers---positively predicts RLVR recoverability.\nIf a pruned structure has high overlap with retained structures, RLVR can absorb its function through global policy optimization over the remaining architecture.\nConversely, structures with unique, non-redundant computations are difficult to recover once removed.\nThis yields what we term the \\textbf{Redundancy Paradox}: counterintuitively, the structures most valuable to retain for post-RLVR recovery are not the most important ones, but the most \\emph{functionally unique} ones.\nRecovery-aware pruning therefore \\emph{preferentially removes} important-but-redundant structures---whose high overlap means RLVR can redistribute their function across retained peers---while protecting functionally unique structures that, once removed, leave an irrecoverable gap.\nStandard importance-only pruning, by contrast, protects high-importance structures regardless of redundancy, inadvertently removing unique structures whose function cannot be recovered.\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (\\rasp{})}, a three-stage framework that incorporates recoverability into the pruning decision.\nIn Stage~1, \\rasp{} computes for each structure both a gradient-based importance score and a functional overlap score via intra-layer Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}).\nIn Stage~2, these are combined into a recovery-aware score $S(h) = I(h) \\times (1 - F(h))^\\alpha$ that protects structures which are both important \\emph{and} functionally unique, while allowing removal of important-but-redundant structures whose function RLVR can redistribute.\nIn Stage~3, the pruned model undergoes a brief SFT warmup to restore generation competence, followed by GRPO-based RLVR recovery~\\citep{shao2024grpo} to restore reasoning ability.\nUnlike prior CKA-based pruning that uses inter-layer similarity for depth pruning~\\citep{mpruner2024,lachance2024cka}, \\rasp{} uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability---a finer granularity optimizing for a fundamentally different objective.\n\nWe evaluate \\rasp{} on DeepSeek-R1-Distill-Qwen-7B~\\citep{deepseek2025r1} at 20\\% structured sparsity.\nAt matched sparsity, \\rasp{}-pruned models retain 29\\% GSM8K~\\citep{cobbe2021gsm8k} accuracy immediately after pruning, compared to 1\\% for importance-only pruning ($N{=}100$, $p{<}0.0001$)---a 28-percentage-point advantage attributable to the recovery-aware scoring criterion.\nAfter SFT warmup, both pruning strategies recover substantially (57--64\\%), with detailed comparison deferred to \\S\\ref{sec:experiments}.\n[TBD: GRPO results]\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify the \\emph{Redundancy Paradox}---that functional redundancy enables RLVR to recover the function of removed structures, making important-but-redundant structures safely removable while functionally unique structures become critical to retain---and formalize it through intra-layer CKA-based functional overlap scoring.\n    \\item We propose \\rasp{}, a recovery-aware pruning framework that integrates functional overlap into structural pruning decisions, achieving 29\\% post-prune GSM8K accuracy versus 1\\% for importance-only pruning at matched 20\\% sparsity on DeepSeek-R1-Distill-Qwen-7B.\n    \\item [TBD: GRPO recovery results---contribution demonstrating that \\rasp{}'s post-prune advantage translates to superior post-RLVR reasoning performance.]\n    \\item We present preliminary evidence that the optimal pruning strategy may be conditioned on the recovery paradigm~\\citep{frankle2019lth}, supporting the notion of \\emph{paradigm-conditioned prunability} [TBD: pending GRPO confirmation and statistical validation].\n\\end{enumerate}\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 19_

Let me verify no em-dashes or en-dashes slipped in, and check the final output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "6b95aef8-b6b4-4b93-90f9-10545c55f42e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3AcAYe3XU1USPbbCdJPhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4048,
      "cache_read_input_tokens": 36757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4048
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

<details open><summary>🔧 Tool call — Grep · `toolu_01BvLAoqErUkUCN7MT8VGiHw`</summary>

```json
{
  "pattern": "—|–",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
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
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "6fe82e0c-8d07-4163-9c13-93f8bfbb0dd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3AcAYe3XU1USPbbCdJPhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4048,
      "cache_read_input_tokens": 36757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4048
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

_source line 21 · 2026-05-17T23:22:51.268Z_

<details><summary>↩ Tool result · `toolu_01BvLAoqErUkUCN7MT8VGiHw`</summary>

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
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "2e002de0-e264-4392-82b3-5ac47c08071d",
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

_source line 22_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ybf5MaaZX2bZ1WdmRkQ3sn`</summary>

```json
{
  "pattern": "---",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
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
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "782cab70-e866-4ee3-9c2b-b7639225d28e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3AcAYe3XU1USPbbCdJPhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4048,
      "cache_read_input_tokens": 36757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4048
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

_source line 23 · 2026-05-17T23:22:51.644Z_

<details><summary>↩ Tool result · `toolu_01Ybf5MaaZX2bZ1WdmRkQ3sn`</summary>

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
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "a073bfe9-e464-4aaf-80b9-0d36048906ab",
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

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Good - no dashes. Let me also quickly check for -ing phrase endings that might be AI-style.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "77afe89c-1052-4cb7-9883-08719e4edd25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmQ4xFq87keYhEoiorn48z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 40805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 425
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

No dashes. Let me also check for -ing phrase endings (the AI writing pattern).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "8b5fd8f0-1135-4855-8d23-86372ad33371",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmQ4xFq87keYhEoiorn48z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 40805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 425
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

<details open><summary>🔧 Tool call — Grep · `toolu_01QLKvEuXLmkrCkJZ8R5GmoU`</summary>

```json
{
  "pattern": "ing[,.]$",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
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
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "0504fabd-5712-4492-acc1-5ed78ffd2fb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NmQ4xFq87keYhEoiorn48z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 425,
      "cache_read_input_tokens": 40805,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 425
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

_source line 27 · 2026-05-17T23:22:58.317Z_

<details><summary>↩ Tool result · `toolu_01QLKvEuXLmkrCkJZ8R5GmoU`</summary>

```text
23:PASER~\citep{paser2025} optimizes recovery data selection, while PAT~\citep{pat2025} proposes pruning-aware tuning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "fe985964-758a-444a-93fd-bd63314cd9ff",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "23:PASER~\\citep{paser2025} optimizes recovery data selection, while PAT~\\citep{pat2025} proposes pruning-aware tuning.",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
That line ends with "tuning." which is fine - "pruning-aware tuning" is a proper noun/method name, not an -ing participial phrase. No issue there.

The introduction is complete. Let me summarize what I did.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "c8680559-2238-41d6-a8d6-3c1e424282eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Bv73EGbBzK2RJBKzTfb8M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 41230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 238
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

That's a method name ("pruning-aware tuning"), not an -ing participial phrase. No issue.

Introduction rewritten. Key changes:
- Replaced "Redundancy Paradox" narrative with the confirmed "GRPO fundamentally fails on pruned models" story
- Hook opens with the unpruned model's reward-accuracy decoupling (0→0.661 reward, 81.27%→81.27% accuracy)
- RASP repositioned as diagnostic tool, not superior method
- Three contributions map to the three confirmed claims (C1: universal decoupling + collapse, C2: severity gradient, C3: Redundancy-Stability Tradeoff)
- All `\citep{}` keys verified against references.bib
- Section references (`\S\ref{sec:grpo_failure}`, `\S\ref{sec:collapse_analysis}`, `\S\ref{sec:tradeoff}`) need matching labels in the corresponding sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "uuid": "8e8311b2-f562-4b55-b486-b348c6cbd0d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Bv73EGbBzK2RJBKzTfb8M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 41230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 238
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

_source line 30_

That's a method name ("pruning-aware tuning"), not an -ing participial phrase. No issue.

Introduction rewritten. Key changes:
- Replaced "Redundancy Paradox" narrative with the confirmed "GRPO fundamentally fails on pruned models" story
- Hook opens with the unpruned model's reward-accuracy decoupling (0→0.661 reward, 81.27%→81.27% accuracy)
- RASP repositioned as diagnostic tool, not superior method
- Three contributions map to the three confirmed claims (C1: universal decoupling + collapse, C2: severity gradient, C3: Redundancy-Stability Tradeoff)
- All `\citep{}` keys verified against references.bib
- Section references (`\S\ref{sec:grpo_failure}`, `\S\ref{sec:collapse_analysis}`, `\S\ref{sec:tradeoff}`) need matching labels in the corresponding sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 107319,
  "duration_api_ms": 108492,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "717bcd26-092e-4a1f-a8dd-8571c3490d82",
  "total_cost_usd": 0.41216575,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 29627,
    "cache_read_input_tokens": 189772,
    "output_tokens": 5174,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29627,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 293,
        "cache_read_input_tokens": 41230,
        "cache_creation_input_tokens": 238,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 238
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2601,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002711,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 5174,
      "cacheReadInputTokens": 189772,
      "cacheCreationInputTokens": 29627,
      "webSearchRequests": 0,
      "costUSD": 0.40945475,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9ee88e9b-ff86-48eb-af29-dee373c78b25"
}
```

</details>

---
