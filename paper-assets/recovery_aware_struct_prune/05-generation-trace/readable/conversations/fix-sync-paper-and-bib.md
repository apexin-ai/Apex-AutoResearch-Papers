# fix sync paper and bib

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_fix_sync-paper-and-bib_20260514T065218.jsonl`
- **Structured JSON:** [`0b992954f5971212d3ed.json`](../../sessions/0b/0b992954f5971212d3ed.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

67 recorded events

### Tool call

_source line 1 · 2026-05-14T06:58:25.610522+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T06:58:25.610850+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T06:58:25.611017+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "ls -la /root/recovery_aware_struct_prune/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "ls -la /root/recovery_aware_struct_prune/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T06:58:25.611147+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T06:58:25.611286+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T06:58:25.611427+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 20\\ndrwxr-xr-x  2 root root   60 May 14 13:11 .\\ndrwxr-xr-x 10 root root  149 May 14 13:50 ..\\n-rw-r--r--  1 root root 8736 May 14 13:11 method.tex\\n-rw-r--r--  1 root root 5782 May 14 13:11 related_work.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T06:58:25.611552+00:00_

paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T06:58:25.611665+00:00_

paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T06:58:25.611793+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/recovery_aware_struct_prune/paper/method.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat /root/recovery_aware_struct_prune/paper/method.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T06:58:25.612074+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Method: Recovery-Aware Structured Pruning}\\n\\\\label{sec:method}\\n\\nWe propose \\\\textbf{Recovery-Aware Structured Pruning (RASP)}, a three-stage framework that optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy preservation.\\nThe core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\\\\citep{rlsqueezes2026}.\\n\\n\\\\subsection{Preliminaries and Notation}\\n\\\\label{sec:prelim}\\n\\n\\\\paragraph{Structured pruning.}\\nGiven a pretrained transformer $\\\\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.\\nWe denote the set of prunable structures as $\\\\mathcal{H} = \\\\{h_1, h_2, \\\\ldots, h_N\\\\}$.\\n\\n\\\\paragraph{Grouped Query Attention (GQA).}\\nIn GQA architectures~\\\\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads, with each KV head serving a group of $G = n_Q / n_{KV}$ query heads.\\nFor DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$), $G = 7$, yielding 4 GQA groups per layer.\\nWe treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit, since removing a KV head necessitates removing all associated Q heads.\\n\\n\\\\paragraph{RLVR recovery.}\\nReinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.\\nWe use Group Relative Policy Optimization (GRPO;~\\\\citealp{shao2024grpo}) as the recovery algorithm, following~\\\\citet{selfhealing2025}.\\n\\n\\\\subsection{Stage 1: Reasoning-Trace Structural Analysis}\\n\\\\label{sec:stage1}\\n\\nRASP computes tw
…[truncated 7081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T06:58:25.612277+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "cat /root/recovery_aware_struct_prune/paper/related_work.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "cat /root/recovery_aware_struct_prune/paper/related_work.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T06:58:25.612419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T06:58:25.612596+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Related Work}\\n\\\\label{sec:related}\\n\\n\\\\subsection{Structured Pruning of Large Language Models}\\n\\\\label{sec:rw_pruning}\\n\\nStructured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.\\nLLM-Pruner~\\\\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.\\nBonsai~\\\\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.\\nGRASPrune~\\\\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.\\nShortGPT~\\\\citep{shortgpt2024} and SliceGPT~\\\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\\\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.\\n\\nFor reasoning models specifically, RESP~\\\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\\\% on GSM8K at 40\\\\% structured sparsity without any recovery training.\\n\\\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.\\nRAC~\\\\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.\\n\\\\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \\\\emph{which} structures are removed critically shapes recovery potent
…[truncated 4195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T06:58:25.612769+00:00_

1	@article{shao2024grpo,
2	  title={DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models},
3	  author={Shao, Zhihong and Wang, Peiyi and Zhu, Qihao and Xu, Runxin and Song, Junxiao and Zhang, Mingchuan and Li, Y.K. and Wu, Y. and Guo, Daya},
4	  journal={arXiv preprint arXiv:2402.03300},
5	  year={2024},
6	  url={https://arxiv.org/abs/2402.03300}
7	}
8	
9	@inproceedings{llmpruner2023,
10	  title={LLM-Pruner: On the Structural Pruning of Large Language Models},
11	  author={Ma, Xinyin and Fang, Gongfan and Wang, Xinchao},
12	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
13	  year={2023},
14	  url={https://arxiv.org/abs/2305.11627}
15	}
16	
17	@inproceedings{graspprune2026,
18	  title={GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models},
19	  author={Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},
20	  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
21	  year={2026},
22	  url={https://arxiv.org/abs/2604.19398}
23	}
24	
25	@article{resp2025,
26	  title={Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models},
27	  author={Wang, Ziyan and Diao, Enmao and Le, Qi and Wang, Pu and Wang, Guanchu and Lee, Minwoo and Yeh, Shu-ping and Yang, Li},
28	  journal={arXiv preprint arXiv:2512.02185},
29	  year={2025},
30	  url={https://arxiv.org/abs/2512.02185}
31	}
32	
33	@article{selfhealing2025,
34	  title={Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning},
35	  author={Ji, Yixin and Lin, Zhimin and Li, Juntao and Wu, Kaixin and Yao, Kai and Jia, Xu and Mo, Linjian and Zhang, Min},
36	  year={2025},
37	  note={Under review},
38	  url={https://openreview.net/forum?id=Cy8Qa4gAst}
39	}
40	
41	@inproceedings{bonsai2025,
42	  title={Everybody Prune Now: Structured Pruning of LLMs with only Forward Passes},
43	  author={Kolaw
…[truncated 2417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T06:58:25.612986+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "wc -l /root/recovery_aware_struct_prune/paper/method.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "wc -l /root/recovery_aware_struct_prune/paper/method.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T06:58:25.613126+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"124 /root/recovery_aware_struct_prune/paper/method.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.72}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T06:58:25.613247+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "head -65 /root/recovery_aware_struct_prune/paper/method.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "head -65 /root/recovery_aware_struct_prune/paper/method.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T06:58:25.613387+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-23072",
  "command": "tail -60 /root/recovery_aware_struct_prune/paper/method.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-23072",
    "command": "tail -60 /root/recovery_aware_struct_prune/paper/method.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T06:58:25.613565+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\section{Method: Recovery-Aware Structured Pruning}\\n\\\\label{sec:method}\\n\\nWe propose \\\\textbf{Recovery-Aware Structured Pruning (RASP)}, a three-stage framework that optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy preservation.\\nThe core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\\\\citep{rlsqueezes2026}.\\n\\n\\\\subsection{Preliminaries and Notation}\\n\\\\label{sec:prelim}\\n\\n\\\\paragraph{Structured pruning.}\\nGiven a pretrained transformer $\\\\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.\\nWe denote the set of prunable structures as $\\\\mathcal{H} = \\\\{h_1, h_2, \\\\ldots, h_N\\\\}$.\\n\\n\\\\paragraph{Grouped Query Attention (GQA).}\\nIn GQA architectures~\\\\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads, with each KV head serving a group of $G = n_Q / n_{KV}$ query heads.\\nFor DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$), $G = 7$, yielding 4 GQA groups per layer.\\nWe treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit, since removing a KV head necessitates removing all associated Q heads.\\n\\n\\\\paragraph{RLVR recovery.}\\nReinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.\\nWe use Group Relative Policy Optimization (GRPO;~\\\\citealp{shao2024grpo}) as the recovery algorithm, following~\\\\citet{selfhealing2025}.\\n\\n\\\\subsection{Stage 1: Reasoning-Trace Structural Analysis}\\n\\\\label{sec:stage1}\\n\\nRASP computes tw
…[truncated 3872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T06:58:25.613767+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    S(h) = I(h) \\\\times \\\\big(1 - F(h)\\\\big)^\\\\alpha,\\n    \\\\label{eq:score}\\n\\\\end{equation}\\nwhere $\\\\alpha > 0$ controls the strength of the recoverability penalty.\\nStructures with the lowest $S(h)$ are pruned up to the target sparsity ratio.\\n\\nThe scoring captures three regimes:\\n\\\\begin{itemize}[nosep,leftmargin=*]\\n    \\\\item \\\\textbf{High $I$, low $F$} (irreplaceable scaffolding): No other structure can assume its function. High $S$ $\\\\rightarrow$ \\\\emph{protected}.\\n    \\\\item \\\\textbf{High $I$, high $F$} (redundant but important): RLVR can redistribute its function via global exploration. Low $S$ $\\\\rightarrow$ \\\\emph{pruned preferentially}.\\n    \\\\item \\\\textbf{Low $I$} (unimportant): Pruned regardless of overlap.\\n\\\\end{itemize}\\n\\nThe key distinction from standard pruning---which ranks solely by $I(h)$---is that RASP additionally down-weights protection of structures whose function overlaps with retained structures.\\nThis is motivated by the finding that RLVR recovers through global exploration and path compression~\\\\citep{rlsqueezes2026}, making high-overlap structures more amenable to functional redistribution than unique structures of equivalent importance.\\n\\nAttention GQA groups and MLP channel groups are scored jointly and ranked in a unified list, enabling cross-component pruning decisions.\\nAlgorithm~\\\\ref{alg:rasp} summarizes the complete pipeline.\\n\\n\\\\subsection{Stage 3: RLVR Recovery}\\n\\\\label{sec:stage3}\\n\\nAfter pruning, we apply GRPO-based RLVR on mathematical reasoning data (GSM8K and MATH training sets) to recover the pruned model's reasoning ability.\\nThe reward is binary: $r = 1$ if the model's final answer matches the ground truth, $r = 0$ otherwise.\\n\\nWe choose RLVR over SFT for recovery based on their fundamentally different training dynamics.\\n\\\\citet{rlsqueezes2026} show that RLVR \\\\emph{compresses
…[truncated 2249 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T06:58:25.613987+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex",
  "content": "\\section{Method: Recovery-Aware Structured Pruning}\n\\label{sec:method}\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (RASP)}, a three-stage framework that optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy preservation.\nThe core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\\citep{rlsqueezes2026}.\n\n\\subsection{Preliminaries and Notation}\n\\label{sec:prelim}\n\n\\paragraph{Structured pruning.}\nGiven a pretrained transformer $\\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.\nWe denote the set of prunable structures as $\\mathcal{H} = \\{h_1, h_2, \\ldots, h_N\\}$.\n\n\\paragraph{Grouped Query Attention (GQA).}\nIn GQA architectures~\\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads, with each KV head serving a group of $G = n_Q / n_{KV}$ query heads.\nFor DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$), $G = 7$, yielding 4 GQA groups per layer.\nWe treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit, since removing a KV head necessitates removing all associated Q heads.\n\n\\paragraph{RLVR recovery.}\nReinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.\nWe use Group Relative Policy Optimization (GRPO;~\\citealp{shao2024grpo}) as the recovery algorithm, following~\\citet{selfhealing2025}.\n\n\\subsection{Stage 1: Reasoning-Trace Structural Analysis}\n\\label{sec:stage1}\n\nRASP computes two complementary scores per structure: \\emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \\emph{functional overlap} $F(h)$ measuring the degree to which its function is recoverable from other structures.\n\n\\paragraph{Self-calibrated reasoning traces.}\nFollowing~\\citet{resp2025}, we generate chain-of-thought reasoning traces from the model's own distribution rather than using external calibration data.\nGiven a calibration set of reasoning problems $\\mathcal{D}_\\text{cal}$, we sample traces $\\{(x_j, \\hat{y}_j)\\}_{j=1}^{M}$ where $\\hat{y}_j \\sim p_\\mathcal{M}(\\cdot \\mid x_j)$.\nThis ensures importance scores reflect the model's actual reasoning pathways.\n\n\\paragraph{Structural importance.}\nFor each structure $h$, we compute importance $I(h)$ via first-order Taylor expansion on the reasoning trace loss:\n\\begin{equation}\n    I(h) = \\left| \\sum_{(x,\\hat{y}) \\in \\mathcal{D}_\\text{cal}} \\mathbf{a}_h(x, \\hat{y})^\\top \\frac{\\partial \\mathcal{L}(x, \\hat{y})}{\\partial \\mathbf{a}_h} \\right|,\n    \\label{eq:importance}\n\\end{equation}\nwhere $\\mathbf{a}_h$ denotes the activation of structure $h$ and $\\mathcal{L}$ is the language modeling loss over the reasoning trace.\nFor a GQA group $g$ containing Q heads $\\{q_1, \\ldots, q_G\\}$ and KV head $k$, we aggregate: $I(g) = \\sum_{i=1}^{G} I(q_i) + I(k)$.\n\n\\paragraph{Functional overlap via CKA.}\nWe measure functional overlap using linear Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to invertible linear transformations.\nGiven activation matrices $\\mathbf{X}, \\mathbf{Y} \\in \\mathbb{R}^{n \\times d}$ collected over $n$ calibration examples, linear CKA is:\n\\begin{equation}\n    \\text{CKA}(\\mathbf{X}, \\mathbf{Y}) = \\frac{\\text{HSIC}(\\mathbf{X}, \\mathbf{Y})}{\\sqrt{\\text{HSIC}(\\mathbf{X}, \\mathbf{X}) \\cdot \\text{HSIC}(\\mathbf{Y}, \\mathbf{Y})}},\n    \\label{eq:cka}\n\\end{equation}\nwhere $\\text{HSIC}(\\mathbf{X}, \\mathbf{Y}) = \\frac{1}{(n-1)^2} \\operatorname{tr}(\\mathbf{K} \\mathbf{H} \\mathbf{L} \\mathbf{H})$, with $\\mathbf{K} = \\mathbf{X}\\mathbf{X}^\\top$, $\\mathbf{L} = \\mathbf{Y}\\mathbf{Y}^\\top$, and $\\mathbf{H} = \\mathbf{I}_n - \\frac{1}{n}\\mathbf{1}\\mathbf{1}^\\top$.\n\nFor a GQA group $g_i$ in layer $\\ell$, we form its representation by concatenating its constituent Q head activations: $\\mathbf{X}_{g_i} = [\\mathbf{a}_{q_1}; \\ldots; \\mathbf{a}_{q_G}] \\in \\mathbb{R}^{n \\times Gd_h}$.\nThe functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:\n\\begin{equation}\n    F(g_i) = \\frac{1}{|\\mathcal{G}_\\ell| - 1} \\sum_{\\substack{g_j \\in \\mathcal{G}_\\ell \\\\ j \\neq i}} \\text{CKA}(\\mathbf{X}_{g_i}, \\mathbf{X}_{g_j}),\n    \\label{eq:overlap}\n\\end{equation}\nwhere $\\mathcal{G}_\\ell$ is the set of GQA groups in layer $\\ell$.\nUnlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2024cka}, RASP uses \\emph{intra-layer} CKA between individual GQA groups to predict per-structure recoverability---a fundamentally different granularity and objective.\n\n\\subsection{Stage 2: Recovery-Aware Scoring}\n\\label{sec:stage2}\n\nThe recovery-aware score combines importance and functional overlap:\n\\begin{equation}\n    S(h) = I(h) \\times \\big(1 - F(h)\\big)^\\alpha,\n    \\label{eq:score}\n\\end{equation}\nwhere $\\alpha > 0$ controls the strength of the recoverability penalty.\nStructures with the lowest $S(h)$ are pruned up to the target sparsity ratio.\n\nThe scoring captures three regimes:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High $I$, low $F$} (irreplaceable scaffolding): No other structure can assume its function. High $S$ $\\rightarrow$ \\emph{protected}.\n    \\item \\textbf{High $I$, high $F$} (redundant but important): RLVR can redistribute its function via global exploration. Low $S$ $\\rightarrow$ \\emph{pruned preferentially}.\n    \\item \\textbf{Low $I$} (unimportant): Pruned regardless of overlap.\n\\end{itemize}\n\nThe key distinction from standard pruning---which ranks solely by $I(h)$---is that RASP additionally down-weights protection of structures whose function overlaps with retained structures.\nThis is motivated by the finding that RLVR recovers through global exploration and path compression~\\citep{rlsqueezes2026}, making high-overlap structures more amenable to functional redistribution than unique structures of equivalent importance.\n\nAttention GQA groups and MLP channel groups are scored jointly and ranked in a unified list, enabling cross-component pruning decisions.\nAlgorithm~\\ref{alg:rasp} summarizes the complete pipeline.\n\n\\subsection{Stage 3: RLVR Recovery}\n\\label{sec:stage3}\n\nAfter pruning, we apply GRPO-based RLVR on mathematical reasoning data (GSM8K and MATH training sets) to recover the pruned model's reasoning ability.\nThe reward is binary: $r = 1$ if the model's final answer matches the ground truth, $r = 0$ otherwise.\n\nWe choose RLVR over SFT for recovery based on their fundamentally different training dynamics.\n\\citet{rlsqueezes2026} show that RLVR \\emph{compresses} incorrect reasoning trajectories while SFT \\emph{expands} correct ones.\nFor a pruned model, RLVR can globally explore and redistribute functionality across remaining structures, while SFT is limited to imitating fixed trajectories through a reduced architecture.\nStructures with high functional overlap $F(h)$ are precisely those whose function can be absorbed by similar retained structures through RLVR's global optimization---the theoretical basis for RASP's scoring criterion.\n\n\\begin{algorithm}[t]\n\\caption{Recovery-Aware Structured Pruning (RASP)}\n\\label{alg:rasp}\n\\SetAlgoLined\n\\KwIn{Model $\\mathcal{M}$, calibration problems $\\mathcal{D}_\\text{cal}$, target sparsity $s$, overlap weight $\\alpha$, recovery data $\\mathcal{D}_\\text{rec}$}\n\\KwOut{Pruned and recovered model $\\mathcal{M}'$}\n\\BlankLine\n\\tcc{Stage 1: Reasoning-Trace Structural Analysis}\nSample reasoning traces $\\{(x_j, \\hat{y}_j)\\} \\sim p_\\mathcal{M}(\\cdot \\mid \\mathcal{D}_\\text{cal})$\\;\n\\ForEach{structure $h \\in \\mathcal{H}$}{\n    Compute importance $I(h)$ via Eq.~\\eqref{eq:importance}\\;\n    Collect activations $\\mathbf{X}_h$ over calibration traces\\;\n}\n\\ForEach{layer $\\ell = 1, \\ldots, L$}{\n    \\ForEach{group $g_i \\in \\mathcal{G}_\\ell$}{\n        $F(g_i) \\gets \\frac{1}{|\\mathcal{G}_\\ell|-1} \\sum_{j \\neq i} \\text{CKA}(\\mathbf{X}_{g_i}, \\mathbf{X}_{g_j})$\\;\n    }\n}\n\\BlankLine\n\\tcc{Stage 2: Recovery-Aware Scoring}\n\\ForEach{structure $h \\in \\mathcal{H}$}{\n    $S(h) \\gets I(h) \\times (1 - F(h))^\\alpha$\\;\n}\n$\\mathcal{P} \\gets$ bottom-$\\lfloor s \\cdot |\\mathcal{H}| \\rfloor$ structures by $S(h)$\\;\n$\\mathcal{M}_\\text{pruned} \\gets \\text{Remove}(\\mathcal{M}, \\mathcal{P})$\\;\n\\BlankLine\n\\tcc{Stage 3: RLVR Recovery}\n$\\mathcal{M}' \\gets \\text{GRPO}(\\mathcal{M}_\\text{pruned}, \\mathcal{D}_\\text{rec})$\\;\n\\Return{$\\mathcal{M}'$}\n\\end{algorithm}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex",
    "content": "\\section{Method: Recovery-Aware Structured Pruning}\n\\label{sec:method}\n\nWe propose \\textbf{Recovery-Aware Structured Pruning (RASP)}, a three-stage framework that optimizes structural pruning decisions for post-RLVR recoverability rather than immediate accuracy preservation.\nThe core insight is that structures with high functional overlap---those whose computations are redundant with other retained structures---are more recoverable under RLVR, because reinforcement learning can redistribute their function through global exploration~\\citep{rlsqueezes2026}.\n\n\\subsection{Preliminaries and Notation}\n\\label{sec:prelim}\n\n\\paragraph{Structured pruning.}\nGiven a pretrained transformer $\\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units---attention heads or MLP channels---to reduce model size while maintaining hardware-friendly dense computation.\nWe denote the set of prunable structures as $\\mathcal{H} = \\{h_1, h_2, \\ldots, h_N\\}$.\n\n\\paragraph{Grouped Query Attention (GQA).}\nIn GQA architectures~\\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads, with each KV head serving a group of $G = n_Q / n_{KV}$ query heads.\nFor DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$), $G = 7$, yielding 4 GQA groups per layer.\nWe treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit, since removing a KV head necessitates removing all associated Q heads.\n\n\\paragraph{RLVR recovery.}\nReinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.\nWe use Group Relative Policy Optimization (GRPO;~\\citealp{shao2024grpo}) as the recovery algorithm, following~\\citet{selfhealing2025}.\n\n\\subsection{Stage 1: Reasoning-Trace Structural Analysis}\n\\label{sec:stage1}\n\nRASP computes two complementary scores per structure: \\emph{importance} $I(h)$ capturing the structure's contribution to reasoning, and \\emph{functional overlap} $F(h)$ measuring the degree to which its function is recoverable from other structures.\n\n\\paragraph{Self-calibrated reasoning traces.}\nFollowing~\\citet{resp2025}, we generate chain-of-thought reasoning traces from the model's own distribution rather than using external calibration data.\nGiven a calibration set of reasoning problems $\\mathcal{D}_\\text{cal}$, we sample traces $\\{(x_j, \\hat{y}_j)\\}_{j=1}^{M}$ where $\\hat{y}_j \\sim p_\\mathcal{M}(\\cdot \\mid x_j)$.\nThis ensures importance scores reflect the model's actual reasoning pathways.\n\n\\paragraph{Structural importance.}\nFor each structure $h$, we compute importance $I(h)$ via first-order Taylor expansion on the reasoning trace loss:\n\\begin{equation}\n    I(h) = \\left| \\sum_{(x,\\hat{y}) \\in \\mathcal{D}_\\text{cal}} \\mathbf{a}_h(x, \\hat{y})^\\top \\frac{\\partial \\mathcal{L}(x, \\hat{y})}{\\partial \\mathbf{a}_h} \\right|,\n    \\label{eq:importance}\n\\end{equation}\nwhere $\\mathbf{a}_h$ denotes the activation of structure $h$ and $\\mathcal{L}$ is the language modeling loss over the reasoning trace.\nFor a GQA group $g$ containing Q heads $\\{q_1, \\ldots, q_G\\}$ and KV head $k$, we aggregate: $I(g) = \\sum_{i=1}^{G} I(q_i) + I(k)$.\n\n\\paragraph{Functional overlap via CKA.}\nWe measure functional overlap using linear Centered Kernel Alignment (CKA;~\\citealp{kornblith2019cka}), which quantifies similarity between two sets of representations invariant to invertible linear transformations.\nGiven activation matrices $\\mathbf{X}, \\mathbf{Y} \\in \\mathbb{R}^{n \\times d}$ collected over $n$ calibration examples, linear CKA is:\n\\begin{equation}\n    \\text{CKA}(\\mathbf{X}, \\mathbf{Y}) = \\frac{\\text{HSIC}(\\mathbf{X}, \\mathbf{Y})}{\\sqrt{\\text{HSIC}(\\mathbf{X}, \\mathbf{X}) \\cdot \\text{HSIC}(\\mathbf{Y}, \\mathbf{Y})}},\n    \\label{eq:cka}\n\\end{equation}\nwhere $\\text{HSIC}(\\mathbf{X}, \\mathbf{Y}) = \\frac{1}{(n-1)^2} \\operatorname{tr}(\\mathbf{K} \\mathbf{H} \\mathbf{L} \\mathbf{H})$, with $\\mathbf{K} = \\mathbf{X}\\mathbf{X}^\\top$, $\\mathbf{L} = \\mathbf{Y}\\mathbf{Y}^\\top$, and $\\mathbf{H} = \\mathbf{I}_n - \\frac{1}{n}\\mathbf{1}\\mathbf{1}^\\top$.\n\nFor a GQA group $g_i$ in layer $\\ell$, we form its representation by concatenating its constituent Q head activations: $\\mathbf{X}_{g_i} = [\\mathbf{a}_{q_1}; \\ldots; \\mathbf{a}_{q_G}] \\in \\mathbb{R}^{n \\times Gd_h}$.\nThe functional overlap of $g_i$ is the mean pairwise CKA with other groups in the same layer:\n\\begin{equation}\n    F(g_i) = \\frac{1}{|\\mathcal{G}_\\ell| - 1} \\sum_{\\substack{g_j \\in \\mathcal{G}_\\ell \\\\ j \\neq i}} \\text{CKA}(\\mathbf{X}_{g_i}, \\mathbf{X}_{g_j}),\n    \\label{eq:overlap}\n\\end{equation}\nwhere $\\mathcal{G}_\\ell$ is the set of GQA groups in layer $\\ell$.\nUnlike prior work that uses inter-layer CKA to identify globally redundant layers for depth pruning~\\citep{mpruner2024,lachance2024cka}, RASP uses \\emph{intra-layer} CKA between individual GQA groups to predict per-structure recoverability---a fundamentally different granularity and objective.\n\n\\subsection{Stage 2: Recovery-Aware Scoring}\n\\label{sec:stage2}\n\nThe recovery-aware score combines importance and functional overlap:\n\\begin{equation}\n    S(h) = I(h) \\times \\big(1 - F(h)\\big)^\\alpha,\n    \\label{eq:score}\n\\end{equation}\nwhere $\\alpha > 0$ controls the strength of the recoverability penalty.\nStructures with the lowest $S(h)$ are pruned up to the target sparsity ratio.\n\nThe scoring captures three regimes:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High $I$, low $F$} (irreplaceable scaffolding): No other structure can assume its function. High $S$ $\\rightarrow$ \\emph{protected}.\n    \\item \\textbf{High $I$, high $F$} (redundant but important): RLVR can redistribute its function via global exploration. Low $S$ $\\rightarrow$ \\emph{pruned preferentially}.\n    \\item \\textbf{Low $I$} (unimportant): Pruned regardless of overlap.\n\\end{itemize}\n\nThe key distinction from standard pruning---which ranks solely by $I(h)$---is that RASP additionally down-weights protection of structures whose function overlaps with retained structures.\nThis is motivated by the finding that RLVR recovers through global exploration and path compression~\\citep{rlsqueezes2026}, making high-overlap structures more amenable to functional redistribution than unique structures of equivalent importance.\n\nAttention GQA groups and MLP channel groups are scored jointly and ranked in a unified list, enabling cross-component pruning decisions.\nAlgorithm~\\ref{alg:rasp} summarizes the complete pipeline.\n\n\\subsection{Stage 3: RLVR Recovery}\n\\label{sec:stage3}\n\nAfter pruning, we apply GRPO-based RLVR on mathematical reasoning data (GSM8K and MATH training sets) to recover the pruned model's reasoning ability.\nThe reward is binary: $r = 1$ if the model's final answer matches the ground truth, $r = 0$ otherwise.\n\nWe choose RLVR over SFT for recovery based on their fundamentally different training dynamics.\n\\citet{rlsqueezes2026} show that RLVR \\emph{compresses} incorrect reasoning trajectories while SFT \\emph{expands} correct ones.\nFor a pruned model, RLVR can globally explore and redistribute functionality across remaining structures, while SFT is limited to imitating fixed trajectories through a reduced architecture.\nStructures with high functional overlap $F(h)$ are precisely those whose function can be absorbed by similar retained structures through RLVR's global optimization---the theoretical basis for RASP's scoring criterion.\n\n\\begin{algorithm}[t]\n\\caption{Recovery-Aware Structured Pruning (RASP)}\n\\label{alg:rasp}\n\\SetAlgoLined\n\\KwIn{Model $\\mathcal{M}$, calibration problems $\\mathcal{D}_\\text{cal}$, target sparsity $s$, overlap weight $\\alpha$, recovery data $\\mathcal{D}_\\text{rec}$}\n\\KwOut{Pruned and recovered model $\\mathcal{M}'$}\n\\BlankLine\n\\tcc{Stage 1: Reasoning-Trace Structural Analysis}\nSample reasoning traces $\\{(x_j, \\hat{y}_j)\\} \\sim p_\\mathcal{M}(\\cdot \\mid \\mathcal{D}_\\text{cal})$\\;\n\\ForEach{structure $h \\in \\mathcal{H}$}{\n    Compute importance $I(h)$ via Eq.~\\eqref{eq:importance}\\;\n    Collect activations $\\mathbf{X}_h$ over calibration traces\\;\n}\n\\ForEach{layer $\\ell = 1, \\ldots, L$}{\n    \\ForEach{group $g_i \\in \\mathcal{G}_\\ell$}{\n        $F(g_i) \\gets \\frac{1}{|\\mathcal{G}_\\ell|-1} \\sum_{j \\neq i} \\text{CKA}(\\mathbf{X}_{g_i}, \\mathbf{X}_{g_j})$\\;\n    }\n}\n\\BlankLine\n\\tcc{Stage 2: Recovery-Aware Scoring}\n\\ForEach{structure $h \\in \\mathcal{H}$}{\n    $S(h) \\gets I(h) \\times (1 - F(h))^\\alpha$\\;\n}\n$\\mathcal{P} \\gets$ bottom-$\\lfloor s \\cdot |\\mathcal{H}| \\rfloor$ structures by $S(h)$\\;\n$\\mathcal{M}_\\text{pruned} \\gets \\text{Remove}(\\mathcal{M}, \\mathcal{P})$\\;\n\\BlankLine\n\\tcc{Stage 3: RLVR Recovery}\n$\\mathcal{M}' \\gets \\text{GRPO}(\\mathcal{M}_\\text{pruned}, \\mathcal{D}_\\text{rec})$\\;\n\\Return{$\\mathcal{M}'$}\n\\end{algorithm}\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T06:58:25.614220+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T06:58:25.614395+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Structured Pruning of Large Language Models}\n\\label{sec:rw_pruning}\n\nStructured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.\nLLM-Pruner~\\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.\nBonsai~\\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.\nGRASPrune~\\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.\nShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.\n\nFor reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.\nRAC~\\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.\n\\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \\emph{which} structures are removed critically shapes recovery potential.\n\nRASP differs from all the above in that it optimizes the pruning decision for post-RLVR recoverability: structures are scored not only by their importance but by whether their function can be redistributed across retained structures during reinforcement learning recovery.\n\n\\subsection{Pruning-Aware Recovery and Re-training}\n\\label{sec:rw_recovery}\n\nPost-pruning recovery is essential at moderate to high compression ratios.\n\\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\\%+ accuracy at 25\\% compression, significantly outperforming SFT recovery (${\\sim}$80\\%).\nThis establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \\emph{choice} of what to prune affects how well RLVR can recover.\n\nP\\textsuperscript{2} Law~\\citep{p2law2025} establishes scaling laws for post-training loss after pruning ($L \\propto (1/\\rho)^\\gamma$), predicting recovery data requirements at a given compression ratio, but studies only continual pre-training rather than RLVR or SFT.\nPASER~\\citep{paser2025} optimizes which recovery \\emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \\emph{structures} to prune for recoverability.\nPAT~\\citep{pat2025} shows that jointly considering pruning and fine-tuning objectives outperforms the sequential prune-then-finetune pipeline.\n\nThe Lottery Ticket Hypothesis~\\citep{frankle2019lth} asks which subnetworks can train effectively from random initialization.\nRASP extends this notion to what we term \\emph{paradigm-conditioned trainability}: the optimal subnetwork to retain depends not only on the task but on the recovery paradigm (RLVR vs.\\ SFT), as each paradigm imposes fundamentally different functional requirements on the retained architecture.\n\n\\subsection{RLVR Training Dynamics}\n\\label{sec:rw_rlvr}\n\nUnderstanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.\n\\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms: RLVR \\emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \\emph{expands} correct trajectories via local imitation.\nThis asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.\nOPSD~\\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.\n\n\\paragraph{CKA-based pruning.}\nCKA~\\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.\nMPruner~\\citep{mpruner2024} uses \\emph{inter-layer} CKA to cluster globally redundant layers for depth pruning in CNNs and general transformers, achieving up to 50\\% parameter reduction by removing entire layers whose representations are similar to adjacent layers.\n\\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning of VGGNet.\nBoth operate at the \\emph{layer} level, using CKA to identify which layers are redundant and can be removed with minimal accuracy loss.\nIn contrast, RASP uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\\ immediate accuracy preservation).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Structured Pruning of Large Language Models}\n\\label{sec:rw_pruning}\n\nStructured pruning removes entire architectural units---attention heads, MLP channels, or layers---to reduce model size while maintaining hardware-friendly dense computation.\nLLM-Pruner~\\citep{llmpruner2023} introduced dependency-aware structural pruning that respects inter-component coupling in transformer architectures.\nBonsai~\\citep{bonsai2025} achieves competitive structured pruning using only forward passes, eliminating the need for gradient computation.\nGRASPrune~\\citep{graspprune2026} advances the state of the art with global gating that jointly prunes FFN channels and KV head groups under a unified budget constraint.\nShortGPT~\\citep{shortgpt2024} and SliceGPT~\\citep{slicegpt2024} target layer-level depth pruning, while Wanda~\\citep{wanda2024} addresses unstructured weight sparsity---both complementary but orthogonal to the width-level structural pruning we study.\n\nFor reasoning models specifically, RESP~\\citep{resp2025} introduces self-reflective pruning using gradient-based importance on self-generated reasoning traces, achieving 81.3\\% on GSM8K at 40\\% structured sparsity without any recovery training.\n\\citet{llms2lrms2026} systematically compare width and depth pruning for reasoning-centric models, finding width pruning more robust to reasoning degradation but not studying RLVR recovery.\nRAC~\\citep{rac2025} demonstrates that chain-of-thought calibrated reconstruction dramatically improves unstructured and 2:4 semi-structured pruning but does not extend to full structural pruning.\n\\citet{doingmore2026} reveal that unstructured pruning can improve test-time scaling for reasoning while structured pruning degrades it, suggesting that \\emph{which} structures are removed critically shapes recovery potential.\n\nRASP differs from all the above in that it optimizes the pruning decision for post-RLVR recoverability: structures are scored not only by their importance but by whether their function can be redistributed across retained structures during reinforcement learning recovery.\n\n\\subsection{Pruning-Aware Recovery and Re-training}\n\\label{sec:rw_recovery}\n\nPost-pruning recovery is essential at moderate to high compression ratios.\n\\citet{selfhealing2025} demonstrate that RLVR recovery restores pruned reasoning models to 95\\%+ accuracy at 25\\% compression, significantly outperforming SFT recovery (${\\sim}$80\\%).\nThis establishes RLVR as the preferred recovery paradigm for reasoning models, but Self-Healing treats the pruning method as a black box and tests only one compression ratio---it does not study whether the \\emph{choice} of what to prune affects how well RLVR can recover.\n\nP\\textsuperscript{2} Law~\\citep{p2law2025} establishes scaling laws for post-training loss after pruning ($L \\propto (1/\\rho)^\\gamma$), predicting recovery data requirements at a given compression ratio, but studies only continual pre-training rather than RLVR or SFT.\nPASER~\\citep{paser2025} optimizes which recovery \\emph{data} to use through manifold learning and capability-aware budget allocation---complementary to RASP, which optimizes which \\emph{structures} to prune for recoverability.\nPAT~\\citep{pat2025} shows that jointly considering pruning and fine-tuning objectives outperforms the sequential prune-then-finetune pipeline.\n\nThe Lottery Ticket Hypothesis~\\citep{frankle2019lth} asks which subnetworks can train effectively from random initialization.\nRASP extends this notion to what we term \\emph{paradigm-conditioned trainability}: the optimal subnetwork to retain depends not only on the task but on the recovery paradigm (RLVR vs.\\ SFT), as each paradigm imposes fundamentally different functional requirements on the retained architecture.\n\n\\subsection{RLVR Training Dynamics}\n\\label{sec:rw_rlvr}\n\nUnderstanding how RLVR reshapes model representations is central to predicting which pruned structures are recoverable.\n\\citet{rlsqueezes2026} show that RLVR and SFT shape reasoning capabilities through fundamentally different mechanisms: RLVR \\emph{compresses} incorrect reasoning trajectories via global exploration, while SFT \\emph{expands} correct trajectories via local imitation.\nThis asymmetry provides the theoretical foundation for RASP---structures with high functional overlap are more amenable to RLVR's redistribution mechanism, as their function can be absorbed by similar retained structures during global policy optimization, whereas SFT's trajectory-imitation objective cannot achieve such redistribution.\nOPSD~\\citep{opsd2026} proposes a post-RL compaction stage that further compresses reasoning traces after RLVR training, reinforcing the view that RLVR-trained models exhibit compressible internal structure.\n\n\\paragraph{CKA-based pruning.}\nCKA~\\citep{kornblith2019cka} has been previously applied to pruning, but at a fundamentally different granularity and with a different objective.\nMPruner~\\citep{mpruner2024} uses \\emph{inter-layer} CKA to cluster globally redundant layers for depth pruning in CNNs and general transformers, achieving up to 50\\% parameter reduction by removing entire layers whose representations are similar to adjacent layers.\n\\citet{lachance2024cka} similarly apply CKA-based layer similarity for depth pruning of VGGNet.\nBoth operate at the \\emph{layer} level, using CKA to identify which layers are redundant and can be removed with minimal accuracy loss.\nIn contrast, RASP uses \\emph{intra-layer} CKA between individual GQA groups and MLP channels to predict per-structure recoverability under RLVR---a finer granularity (width vs.\\ depth pruning) optimizing for a different objective (post-recovery reasoning performance vs.\\ immediate accuracy preservation).\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T06:58:25.614582+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T06:58:25.614722+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T06:58:25.614844+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T06:58:25.614982+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GQA Training Generalized Multi-Query Transformer Ainslie 2023 bibtex arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GQA Training Generalized Multi-Query Transformer Ainslie 2023 bibtex arxiv"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T06:58:25.615096+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ShortGPT Layers Large Language Models More Redundant 2024 arxiv bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ShortGPT Layers Large Language Models More Redundant 2024 arxiv bibtex"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T06:58:25.615205+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SliceGPT Compress Large Language Models Deleting Rows Columns 2024 arxiv bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SliceGPT Compress Large Language Models Deleting Rows Columns 2024 arxiv bibtex"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T06:58:25.615336+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wanda pruning simple effective approach large language models 2024 arxiv bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wanda pruning simple effective approach large language models 2024 arxiv bibtex"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T06:58:25.615451+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"LLMs to LRMs\" width depth pruning reasoning models 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"LLMs to LRMs\" width depth pruning reasoning models 2026 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T06:58:25.615588+00:00_

Web search results for query: "ShortGPT Layers Large Language Models More Redundant 2024 arxiv bibtex"

Links: [{"title":"[2403.03853] ShortGPT: Layers in Large Language Models are More Redundant Than You Expect","url":"https://arxiv.org/abs/2403.03853"},{"title":"ShortGPT: Layers in Large Language Models are More Redun- dant Than You Expect","url":"https://arxiv.org/pdf/2403.03853"},{"title":"[2403.03853v1] ShortGPT: Layers in Large Language Models are More Redundant Than You Expect","url":"https://arxiv.org/abs/2403.03853v1"},{"title":"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect","url":"https://arxiv.org/html/2403.03853v3"},{"title":"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect | OpenReview","url":"https://openreview.net/forum?id=JMNht3SmcG"},{"title":"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/shortgpt-layers-large-language-models-are-more"},{"title":"Paper page - ShortGPT: Layers in Large Language Models are More Redundant Than You Expect","url":"https://huggingface.co/papers/2403.03853"},{"title":"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/146d9dbdd6e13dd2d73e3ba6296817426"},{"title":"[PDF] ShortGPT: Layers in Large Language Models are More Redundant Than You Expect | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ShortGPT:-Layers-in-Large-Language-Models-are-More-Men-Xu/3c6f2e0c5ff5dff6151c3e6489378a53318a75b4"},{"title":"GitHub - sramshetty/ShortGPT: Unofficial implementations of block/layer-wise pruning methods for LLMs.","url":"https://github.com/sramshetty/ShortGPT"}]

I've successfully found the paper you were looking for. Here's the information:

## Paper Details

**Title:** ShortGPT: Layers in Large Language Models are More Redundant Than You Expect

**arXiv ID:** 2403.03853

**Aut
…[truncated 1131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T06:58:25.615762+00:00_

Web search results for query: "GQA Training Generalized Multi-Query Transformer Ainslie 2023 bibtex arxiv"

Links: [{"title":"[2305.13245] GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints","url":"https://arxiv.org/abs/2305.13245"},{"title":"GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230513245A/abstract"},{"title":"GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.298/"},{"title":"GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints","url":"https://arxiv.org/html/2305.13245v3"},{"title":"[PDF] GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GQA:-Training-Generalized-Multi-Query-Transformer-Ainslie-Lee-Thorp/5ae6fb6b5a3c7df515ff4a82ac9673bae6a8e200"},{"title":"[Paper Note] GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints, Joshua Ainslie+, arXiv'23, 2023.05 · Issue #1271 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1271"},{"title":"Paper page - GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints","url":"https://huggingface.co/papers/2305.13245"},{"title":"[2305.13245v2] GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints","url":"https://arxiv.org/abs/2305.13245v2"},{"title":"[2305.13245v3] GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints","url":"https://arxiv.org/abs/2305.13245v3"},{"title":"GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints | OpenReview","url":"https://openreview.net/forum?id=hmOwOZWzYE"}]

I found the paper you're looking for! Here are the key details:

**Paper Information:
…[truncated 1232 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T06:58:25.615939+00:00_

Web search results for query: "SliceGPT Compress Large Language Models Deleting Rows Columns 2024 arxiv bibtex"

Links: [{"title":"[2401.15024] SliceGPT: Compress Large Language Models by Deleting Rows and Columns","url":"https://arxiv.org/abs/2401.15024"},{"title":"Paper page - SliceGPT: Compress Large Language Models by Deleting Rows and Columns","url":"https://huggingface.co/papers/2401.15024"},{"title":"slicegpt: compress large language models","url":"https://arxiv.org/pdf/2401.15024"},{"title":"SliceGPT: Compress Large Language Models by Deleting Rows and Columns | OpenReview","url":"https://openreview.net/forum?id=vXxardq6db"},{"title":"[2401.15024v1] SliceGPT: Compress Large Language Models by Deleting Rows and Columns","url":"https://arxiv.org/abs/2401.15024v1"},{"title":"[PDF] SliceGPT: Compress Large Language Models by Deleting Rows and Columns | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SliceGPT:-Compress-Large-Language-Models-by-Rows-Ashkboos-Croci/7754ac3e8ff1286f17593159781487543cdddaba"},{"title":"SLICEGPT: COMPRESS LARGE LANGUAGE MODELS","url":"https://openreview.net/pdf?id=vXxardq6db"},{"title":"SliceGPT: Compress Large Language Models by Deleting Rows and Columns - Research Collection","url":"https://www.research-collection.ethz.ch/handle/20.500.11850/714235"},{"title":"Compression Laws for Large Language Models","url":"https://arxiv.org/pdf/2504.04342"},{"title":"Papers/Compression/SliceGPT: Compress Large Language Models by Deleting Rows and Columns.md at main · chanmuzi/Papers","url":"https://github.com/chanmuzi/Papers/blob/main/Compression/SliceGPT:%20Compress%20Large%20Language%20Models%20by%20Deleting%20Rows%20and%20Columns.md"}]

I found the paper! Here are the key details:

## Paper Information

**Title:** SliceGPT: Compress Large Language Models by Deleting Rows and Columns

**Authors:** Saleh Ashkboos, Maximilian L. Croci, Marcelo Gennari do Nascimento, Torsten Hoefler, and James Hensman

**ArXiv ID:** 2401.15024

**P
…[truncated 1077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T06:58:25.616110+00:00_

Web search results for query: "Wanda pruning simple effective approach large language models 2024 arxiv bibtex"

Links: [{"title":"[2306.11695] A Simple and Effective Pruning Approach for Large Language Models","url":"https://arxiv.org/abs/2306.11695"},{"title":"A Simple and Effective Pruning Approach for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=PxoFut3dWW"},{"title":"GitHub - locuslab/wanda: A simple and effective LLM pruning approach. · GitHub","url":"https://github.com/locuslab/wanda"},{"title":"A Simple and Effective Pruning Approach for Large Language Models.","url":"https://eric-mingjie.github.io/wanda/home.html"},{"title":"A Simple and Effective Pruning Approach for Large Language Models","url":"https://arxiv.org/html/2306.11695v3"},{"title":"Wanda++: Pruning Large Language Models via Regional ...","url":"https://arxiv.org/pdf/2503.04992"},{"title":"[2503.04992] Wanda++: Pruning Large Language Models via Regional Gradients","url":"https://arxiv.org/abs/2503.04992"},{"title":"arXiv:2306.11695v3 [cs.CL] 6 May 2024","url":"https://arxiv.org/pdf/2306.11695"},{"title":"[2306.11695v1] A Simple and Effective Pruning Approach for Large Language Models","url":"https://arxiv.org/abs/2306.11695v1"},{"title":"Wanda++: Pruning Large Language Models via Regional Gradients","url":"https://arxiv.org/html/2503.04992v1"}]

Based on the search results, here is the information about Wanda:

## Wanda: A Simple and Effective Pruning Approach for Large Language Models

Wanda (Pruning by Weights and activations) is a novel, straightforward yet effective pruning method designed to induce sparsity in pretrained LLMs.

### Key Characteristics:

**Methodology:** The approach prunes weights with the smallest magnitudes multiplied by the corresponding input activations, on a per-output basis.

**Advantages:** Notably, Wanda requires no retraining or weight update, and the pruned LLM can be used as is.

**Performance:** Wanda was evaluated on LLaMA and LLa
…[truncated 782 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T06:58:25.616289+00:00_

Web search results for query: ""LLMs to LRMs" width depth pruning reasoning models 2026 arxiv"

Links: [{"title":"[2601.18091] From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models","url":"https://arxiv.org/abs/2601.18091"},{"title":"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models","url":"https://arxiv.org/html/2601.18091"},{"title":"When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models","url":"https://arxiv.org/html/2504.02010"},{"title":"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/html/2604.24380"},{"title":"Rethinking Layer Redundancy in Large Language Models: Calibration Objectives and Search for Depth Pruning","url":"https://arxiv.org/html/2604.24938"},{"title":"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models | OpenReview","url":"https://openreview.net/forum?id=eHHQEsphbN"},{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"},{"title":"Pruning Long Chain-of-Thought of Large Reasoning Models via Small-Scale Preference Optimization","url":"https://arxiv.org/html/2508.10164"},{"title":"Demystifying the Roles of LLM Layers in Retrieval, Knowledge, and Reasoning","url":"https://arxiv.org/html/2510.02091"},{"title":"Compact: Common-token Optimized Model Pruning Across Channels and Tokens","url":"https://arxiv.org/html/2509.06836v1"}]

The search returned highly relevant results on the topic. Here are the key findings about "From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models" and related research:

## Main Findings

Depth pruning outperforms width pruning on classification tasks, while width pruning is more robust for generation and reasoning.

The study conducts a controlled study of pruning for both instruction-following (LLM-instruct) and reasoning-augment
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T06:58:25.616470+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RAC chain-of-thought calibrated reconstruction pruning reasoning models 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RAC chain-of-thought calibrated reconstruction pruning reasoning models 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T06:58:25.616593+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Doing More with Less\" pruning test-time scaling reasoning 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Doing More with Less\" pruning test-time scaling reasoning 2026 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T06:58:25.616707+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"P2 Law\" scaling laws post-training loss pruning 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"P2 Law\" scaling laws post-training loss pruning 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T06:58:25.616816+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PAT pruning-aware training jointly pruning fine-tuning LLM 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PAT pruning-aware training jointly pruning fine-tuning LLM 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T06:58:25.616922+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OPSD post-RL compaction reasoning traces compression 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OPSD post-RL compaction reasoning traces compression 2026 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T06:58:25.617051+00:00_

Web search results for query: ""Doing More with Less" pruning test-time scaling reasoning 2026 arxiv"

Links: [{"title":"[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/abs/2604.25098"},{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"},{"title":"[2605.08083] LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling","url":"https://arxiv.org/abs/2605.08083"},{"title":"[2605.08083v1] LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling","url":"https://arxiv.org/abs/2605.08083v1"},{"title":"[2511.22242] Rethinking Test Time Scaling for Flow-Matching Generative Models","url":"https://arxiv.org/abs/2511.22242"},{"title":"LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling","url":"https://arxiv.org/html/2605.08083v1"},{"title":"Test-Time Scaling Makes Overtraining Compute-Optimal","url":"https://arxiv.org/html/2604.01411"},{"title":"A Survey of Scaling in Large Language Model Reasoning","url":"https://arxiv.org/html/2504.02181v2"},{"title":"[2509.06861] Test-Time Scaling in Reasoning Models Is Not Effective for Knowledge-Intensive Tasks Yet","url":"https://arxiv.org/abs/2509.06861"},{"title":"ReProbe: Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models","url":"https://arxiv.org/html/2511.06209"}]

Based on the search results, I found the paper you're looking for:

"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling" (arXiv:2604.25098)

**Key Findings:**

The paper investigates LLM pruning methods in the context of test-time compute scaling, specifically comparing unstructured pruning (methods that remove certain redundant weights) versus structured pruning (methods that remove entire layer blocks).

The research experiments across four reasoning benchmarks on two reasoning LLMs (s1.1-7B and Qwen3-
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T06:58:25.617220+00:00_

Web search results for query: ""P2 Law" scaling laws post-training loss pruning 2025 arxiv"

Links: [{"title":"P2 Law: Scaling Law for Post-Training After Model Pruning","url":"https://arxiv.org/pdf/2411.10272"},{"title":"[2411.10272] P$^2$ Law: Scaling Law for Post-Training After Model Pruning","url":"https://arxiv.org/abs/2411.10272"},{"title":"P2 Law: Scaling Law for Post-Training After Model Pruning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.283/"},{"title":"[2411.10272v2] P$^2$ Law: Scaling Law for Post-Training After Model Pruning","url":"https://arxiv.org/abs/2411.10272v2"},{"title":"P2 Law: Scaling Law for Post-Training After Model Pruning","url":"https://aclanthology.org/2025.acl-long.283.pdf"},{"title":"[Literature Review] P$^2$ Law: Scaling Law for Post-Training After Model Pruning","url":"https://www.themoonlight.io/en/review/p2-law-scaling-law-for-post-training-after-model-pruning"},{"title":"Paper page - P^2 Law: Scaling Law for Post-Training After Model Pruning","url":"https://huggingface.co/papers/2411.10272"},{"title":"Position: Enough of Scaling LLMs! Lets Focus on Downscaling","url":"https://arxiv.org/html/2505.00985v2"},{"title":"Scaling Law for Post-training after Model Pruning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/pdollar2dollar-law-scaling-law-post-training-after"},{"title":"P$^2$ Law: Scaling Law for Post-Training After Model Pruning","url":"https://www.emergentmind.com/papers/2411.10272"}]

I found the paper you're looking for! Here's information about the P² Law research:

## Overview

The P² Law is a scaling law for post-training after model pruning that identifies four key factors for predicting the pruned model's post-training loss: the model size before pruning, the number of post-training tokens, the pruning rate, and the model's loss before pruning.

## Background

Pruning has become a widely adopted technique for reducing the hardware requirements of large language models (LLMs)
…[truncated 788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T06:58:25.617404+00:00_

Web search results for query: "RAC chain-of-thought calibrated reconstruction pruning reasoning models 2025 arxiv"

Links: [{"title":"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://arxiv.org/html/2509.12464v1"},{"title":"[2509.12464] Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction","url":"https://arxiv.org/abs/2509.12464"},{"title":"NeurIPS Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://neurips.cc/virtual/2025/loc/san-diego/126571"},{"title":"Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction | OpenReview","url":"https://openreview.net/forum?id=tyGfwG6xTh"},{"title":"Think Before You Prune: Selective Self-Generated Calibration for Pruning Large Reasoning Models","url":"https://arxiv.org/html/2511.18864"},{"title":"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models","url":"https://arxiv.org/html/2601.18091"},{"title":"Inference-Time Chain-of-Thought Pruning with Latent Informativeness Signals","url":"https://arxiv.org/html/2511.00699v1"},{"title":"[2604.05643v1] Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs","url":"https://arxiv.org/abs/2604.05643v1"},{"title":"Verifying Chain-of-Thought Reasoning via Its Computational Graph","url":"https://arxiv.org/html/2510.09312v1"},{"title":"Published in Transactions on Machine Learning Research (09/2025)","url":"https://arxiv.org/pdf/2504.10903"}]

Based on the search results, I found relevant information about the RAC (Reasoning-Aware Compression) research:

## RAC: Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction

The paper is titled "Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction" and was published on arXiv in September 2025.

### Key Concept

RAC reconstructs activations from both the input and the model's on-policy chain-of-thought traces during pruning, in
…[truncated 1170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T06:58:25.617575+00:00_

Web search results for query: "PAT pruning-aware training jointly pruning fine-tuning LLM 2025 arxiv"

Links: [{"title":"[2408.14721] PAT: Pruning-Aware Tuning for Large Language Models","url":"https://arxiv.org/abs/2408.14721"},{"title":"PAT: Pruning-Aware Tuning for Large Language Models","url":"https://arxiv.org/html/2408.14721v1"},{"title":"PAT: Pruning-Aware Tuning for Large Language Models","url":"https://www.arxiv.org/pdf/2408.14721v2"},{"title":"GitHub - kriskrisliu/PAT: [AAAI 2025] PAT: Pruning-Aware Tuning for Large Language Models","url":"https://github.com/kriskrisliu/PAT"},{"title":"[2509.23873v1] Winning the Pruning Gamble: A Unified Approach to Joint Sample and Token Pruning for Efficient Supervised Fine-Tuning","url":"https://arxiv.org/abs/2509.23873v1"},{"title":"P2 Law: Scaling Law for Post-Training After Model Pruning","url":"https://arxiv.org/pdf/2411.10272"},{"title":"PAT: Pruning-Aware Tuning for Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/pat-pruning-aware-tuning-large-language-models"},{"title":"Instruction-Following Pruning for Large Language Models","url":"https://arxiv.org/html/2501.02086v2"},{"title":"Scaling Law for Post-training after Model Pruning","url":"https://arxiv.org/html/2411.10272v1"},{"title":"[2509.23873] Winning the Pruning Gamble: A Unified Approach to Joint Sample and Token Pruning for Efficient Supervised Fine-Tuning","url":"https://arxiv.org/abs/2509.23873"}]

Based on the search results, I found the paper you're looking for:

## PAT: Pruning-Aware Tuning for Large Language Models

This is arXiv paper 2408.14721 titled "PAT: Pruning-Aware Tuning for Large Language Models".

### Key Overview

The PAT paradigm aims to incorporate structural pruning with fine-tuning to eliminate model redundancy while preserving model performance, addressing a key limitation where traditional post-hoc pruning often leads to significant performance loss, with limited recovery from further f
…[truncated 902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T06:58:25.617735+00:00_

Web search results for query: "OPSD post-RL compaction reasoning traces compression 2026 arxiv"

Links: [{"title":"OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models","url":"https://arxiv.org/html/2605.06188v1"},{"title":"[2605.06188] OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models","url":"https://arxiv.org/abs/2605.06188"},{"title":"On-Policy Self-Distillation for Reasoning Compression","url":"https://arxiv.org/html/2603.05433v1"},{"title":"Implicit Compression Regularization: Concise Reasoning via Internal Shorter Distributions in RL Post-Training","url":"https://arxiv.org/html/2605.07316v1"},{"title":"[2603.07598] Shorter Thoughts, Same Answers: Difficulty-Scaled Segment-Wise RL for CoT Compression","url":"https://arxiv.org/abs/2603.07598"},{"title":"Preprint. A Survey of On-Policy Distillation for Large Language Models","url":"https://arxiv.org/pdf/2604.00626"},{"title":"Gradually Compacting Large Language Models for Reasoning Like a Boiling Frog","url":"https://arxiv.org/html/2602.04919v1"},{"title":"Self-Distilled Reasoner: On-Policy Self-Distillation | Siyan Zhao","url":"https://siyan-zhao.github.io/blog/2026/opsd/"},{"title":"Fast KV Compaction via Attention Matching","url":"https://arxiv.org/pdf/2602.16284"},{"title":"Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION","url":"https://arxiv.org/pdf/2505.03801"}]

I found relevant results for your search. Here's what I found:

## Main Result: OPSD Paper on arXiv

The primary result is an arXiv paper titled "OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models" (paper ID: 2605.06188, published May 7, 2026).

## Key Findings

The research shows that in thinking-enabled mathematical reasoning, OPSD behaves most reliably as a compression mechanism rather than a correction mechanism: training only on correct rollouts preserves accuracy while substantially shortening responses, whereas trainin
…[truncated 1051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T06:58:25.617914+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.18091 \"From LLMs to LRMs\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.18091 \"From LLMs to LRMs\" authors"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T06:58:25.618050+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2509.12464 \"Reasoning Models Can be Accurately Pruned\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2509.12464 \"Reasoning Models Can be Accurately Pruned\" authors"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T06:58:25.618166+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.25098 \"Doing More With Less\" pruning test-time scaling authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.25098 \"Doing More With Less\" pruning test-time scaling authors"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T06:58:25.618302+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2411.10272 \"P2 Law\" pruning scaling law authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2411.10272 \"P2 Law\" pruning scaling law authors"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T06:58:25.618420+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.06188 \"OPSD Compresses What RLVR Teaches\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.06188 \"OPSD Compresses What RLVR Teaches\" authors"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T06:58:25.618544+00:00_

Web search results for query: "arxiv 2601.18091 "From LLMs to LRMs" authors"

Links: [{"title":"[2601.18091] From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models","url":"https://arxiv.org/abs/2601.18091"},{"title":"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models","url":"https://arxiv.org/html/2601.18091"},{"title":"Finding RELIEF: Shaping Reasoning Behavior without Reasoning Supervision via Belief Engineering","url":"https://arxiv.org/html/2601.13752"},{"title":"ConMax: Confidence-Maximizing Compression for Efficient Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2601.04973"},{"title":"[2601.19928] Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures","url":"https://arxiv.org/abs/2601.19928"},{"title":"[2601.09971] An Exploratory Study to Repurpose LLMs to a Unified Architecture for Time Series Classification","url":"https://arxiv.org/abs/2601.09971"},{"title":"[2601.09281] STaR: Sensitive Trajectory Regulation for Unlearning in Large Reasoning Models","url":"https://arxiv.org/abs/2601.09281"},{"title":"[2601.03630v1] Reasoning Model Is Superior LLM-Judge, Yet Suffers from Biases","url":"https://arxiv.org/abs/2601.03630v1"},{"title":"[2503.06072] A Survey on Post-training of Large Language Models","url":"https://arxiv.org/abs/2503.06072"},{"title":"[2601.04996] AlgBench: To What Extent Do Large Reasoning Models Understand Algorithms?","url":"https://arxiv.org/abs/2601.04996"}]

Based on the search results, the authors of the paper "From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models" (arxiv 2601.18091) are Longwei Ding, Anhao Zhao, Fanghua Ye, Ziyang Chen, and Xiaoyu Shen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T06:58:25.618691+00:00_

Web search results for query: "arxiv 2509.12464 "Reasoning Models Can be Accurately Pruned" authors"

Links: [{"title":"[2509.12464] Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction","url":"https://arxiv.org/abs/2509.12464"},{"title":"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://arxiv.org/html/2509.12464"},{"title":"Rohan Paul on X: \"This paper shows how to prune reasoning LLMs while keeping accuracy high. It fixes the main reason, pruned reasoning models get slower and less accurate by aligning pruning with decoding. It plugs into existing SparseGPT-style pipelines without retraining or distillation, so it https://t.co/PHO0xN60lx\" / X","url":"https://x.com/rohanpaul_ai/status/1971170823227461772"},{"title":"Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction | OpenReview","url":"https://openreview.net/forum?id=tyGfwG6xTh"}]

Based on the search results, the authors of arxiv paper 2509.12464 "Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction" are: Ryan Lucas, Kayhan Behdin, Zhipeng Wang, Qingquan Song, Shao Tang, and Rahul Mazumder.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T06:58:25.618823+00:00_

Web search results for query: "arxiv 2604.25098 "Doing More With Less" pruning test-time scaling authors"

Links: [{"title":"[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/abs/2604.25098"},{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"}]

Based on the search results, here's the information about arxiv 2604.25098:

**Title:** "Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling"

**Authors:** Ocean Monjur, Shahriar Kabir Nahin, Anshuman Chhabra

**Overview:** The paper examines how large language models exhibit remarkable reasoning capabilities through test-time compute scaling, and explores pruning methods that can reduce model size without sacrificing performance. Their experiments across four reasoning benchmarks on two reasoning LLMs (s1.1-7B and Qwen3-8B) show that unstructured pruning augments test-time scaling performance compared to structured pruning, and can even outperform unpruned full-weight LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-14T06:58:25.618949+00:00_

Web search results for query: "arxiv 2605.06188 "OPSD Compresses What RLVR Teaches" authors"

Links: [{"title":"[2605.06188] OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models","url":"https://arxiv.org/abs/2605.06188"},{"title":"OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models","url":"https://arxiv.org/html/2605.06188v1"}]

The paper "OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models" (arxiv 2605.06188) is authored by Jaehoon Kim and 1 other author. The search results do not provide the name of the second author. To find the complete author list, you can visit the full paper at https://arxiv.org/abs/2605.06188.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T06:58:25.619097+00:00_

Web search results for query: "arxiv 2411.10272 "P2 Law" pruning scaling law authors"

Links: [{"title":"[2411.10272] P$^2$ Law: Scaling Law for Post-Training After Model Pruning","url":"https://arxiv.org/abs/2411.10272"},{"title":"P2 Law: Scaling Law for Post-Training After Model Pruning","url":"https://arxiv.org/pdf/2411.10272"},{"title":"[2411.10272v2] P$^2$ Law: Scaling Law for Post-Training After Model Pruning","url":"https://arxiv.org/abs/2411.10272v2"},{"title":"Paper page - P^2 Law: Scaling Law for Post-Training After Model Pruning","url":"https://huggingface.co/papers/2411.10272"},{"title":"P$^2$ Law: Scaling Law for Post-Training After Model Pruning","url":"https://www.emergentmind.com/papers/2411.10272"},{"title":"[Literature Review] P$^2$ Law: Scaling Law for Post-Training After Model Pruning","url":"https://www.themoonlight.io/en/review/p2-law-scaling-law-for-post-training-after-model-pruning"},{"title":"P$^2$ Law: Scaling Law for Post-Training After Model Pruning | PromptLayer","url":"https://www.promptlayer.com/research-papers/the-p2-law-predicting-post-pruning-performance-in-llms"},{"title":"Scaling Law for Post-training after Model Pruning","url":"https://arxiv.org/html/2411.10272v1"},{"title":"How to Upscale Neural Networks with Scaling Law? A Survey and Practical Guidelines","url":"https://arxiv.org/html/2502.12051"},{"title":"Position: Enough of Scaling LLMs! Lets Focus on Downscaling","url":"https://arxiv.org/html/2505.00985v2"}]

Based on the search results, here is the information about arxiv paper 2411.10272 and the P² Law:

## Authors

The authors of the P² Law paper are: Xiaodong Chen, Yuxuan Hu, Xiaokang Zhang, Yanling Wang, Cuiping Li, Hong Chen, and Jing Zhang.

## Paper Overview

The P² Law identifies four key factors for predicting the pruned model's post-training loss: the model size before pruning, the number of post-training tokens, the pruning rate, and the model's loss before pruning.

The research was conducted through extensive 
…[truncated 202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T06:58:25.619253+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2408.14721 PAT Pruning-Aware Tuning author list AAAI 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2408.14721 PAT Pruning-Aware Tuning author list AAAI 2025"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T06:58:25.619396+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OPSD arxiv 2605.06188 author list Jaehoon Kim reasoning models post-RL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OPSD arxiv 2605.06188 author list Jaehoon Kim reasoning models post-RL"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T06:58:25.619524+00:00_

Web search results for query: "arxiv 2408.14721 PAT Pruning-Aware Tuning author list AAAI 2025"

Links: [{"title":"[2408.14721] PAT: Pruning-Aware Tuning for Large Language Models","url":"https://arxiv.org/abs/2408.14721"},{"title":"PAT: Pruning-Aware Tuning for Large Language Models","url":"https://www.arxiv.org/pdf/2408.14721v2"},{"title":"GitHub - kriskrisliu/PAT: [AAAI 2025] PAT: Pruning-Aware Tuning for Large Language Models","url":"https://github.com/kriskrisliu/PAT"},{"title":"PAT: Pruning-Aware Tuning for Large Language Models","url":"https://arxiv.org/html/2408.14721v1"},{"title":"Computation and Language Aug 2024","url":"https://arxiv.org/list/cs.CL/2024-08?skip=1175&show=25"},{"title":"PAT: Pruning-Aware Tuning for Large Language Models","url":"https://www.bohrium.com/paper/arxiv/2408.14721"},{"title":"Scaling Law for Post-training after Model Pruning","url":"https://arxiv.org/html/2411.10272v1"},{"title":"PAT: Pruning-Aware Tuning for Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/pat-pruning-aware-tuning-large-language-models"},{"title":"PAT: Pruning-Aware Tuning for Large Language Models | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34649"},{"title":"CFSP: An Efficient Structured Pruning Framework for LLMs ...","url":"https://aclanthology.org/2025.coling-main.626.pdf"}]

Based on the search results, here is the author list for the paper "PAT: Pruning-Aware Tuning for Large Language Models" (arxiv 2408.14721):

The authors are: Yijiang Liu, Huanrui Yang, Youxin Chen, Rongyu Zhang, Miao Wang, Yuan Du, and Li Du.

The paper has been accepted by AAAI 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T06:58:25.619674+00:00_

Web search results for query: "OPSD arxiv 2605.06188 author list Jaehoon Kim reasoning models post-RL"

Links: [{"title":"OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models","url":"https://arxiv.org/html/2605.06188"},{"title":"[2605.06188] OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models","url":"https://arxiv.org/abs/2605.06188"},{"title":"Jaehoon Kim | IEEE Xplore Author Details","url":"https://ieeexplore.ieee.org/author/37089814233"},{"title":"[2605.03460v1] FinSTaR: Towards Financial Reasoning with Time Series Reasoning Models","url":"https://arxiv.org/abs/2605.03460v1"},{"title":"[2605.12542] Earth Science Foundation Models: From Perception to Reasoning and Discovery","url":"https://arxiv.org/abs/2605.12542"},{"title":"[2605.04352] Probing Structural Mathematical Reasoning in Language Models with Algebraic Trapdoors","url":"https://arxiv.org/abs/2605.04352"},{"title":"Jaehoon Kim - Publications","url":"https://sites.google.com/view/jaehoon-kim/publications"},{"title":"[2605.07307] Rethinking Dense Sequential Chains: Reasoning Language Models Can Extract Answers from Sparse, Order-Shuffling Chain-of-Thoughts","url":"https://arxiv.org/abs/2605.07307"},{"title":"Machine Learning Jan 2025","url":"https://arxiv.org/list/cs.LG/2025-01?skip=2050&show=1000"},{"title":"[2605.03050] Evaluating Reasoning Models for Queries with Presuppositions","url":"https://arxiv.org/abs/2605.03050"}]

Based on the search results, I found information about arxiv paper 2605.06188. Here are the details:

**Paper Title:** OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models

**Author List:** The paper is by Jaehoon Kim from Yonsei University and Dongha Lee from Yonsei University

**Publication Date:** May 7, 2026

**Summary:** On-Policy Self-Distillation (OPSD) has recently emerged as an alternative to Reinforcement Learning with Verifiable Rewards (RLVR), promising higher accuracy and shorter re
…[truncated 355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T06:58:25.619862+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
  "old_string": "@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carlin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}",
  "new_string": "@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carlin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}\n\n@inproceedings{ainslie2023gqa,\n  title={{GQA}: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints},\n  author={Ainslie, Joshua and Lee-Thorp, James and de Jong, Michiel and Zemlyanskiy, Yury and Lebr{\\'o}n, Federico and Sanghai, Sumit},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.13245}\n}\n\n@article{shortgpt2024,\n  title={{ShortGPT}: Layers in Large Language Models are More Redundant Than You Expect},\n  author={Men, Xin and Xu, Mingyu and Zhang, Qingyu and Wang, Bingning and Lin, Hongyu and Lu, Yaojie and Han, Xianpei and Chen, Weipeng},\n  journal={arXiv preprint arXiv:2403.03853},\n  year={2024},\n  url={https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{slicegpt2024,\n  title={{SliceGPT}: Compress Large Language Models by Deleting Rows and Columns},\n  author={Ashkboos, Saleh and Croci, Maximilian L. and Gennari do Nascimento, Marcelo and Hoefler, Torsten and Hensman, James},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2401.15024}\n}\n\n@inproceedings{wanda2024,\n  title={A Simple and Effective Pruning Approach for Large Language Models},\n  author={Sun, Mingjie and Liu, Zhuang and Bair, Anna and Kolter, J. Zico},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2306.11695}\n}\n\n@article{llms2lrms2026,\n  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},\n  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},\n  journal={arXiv preprint arXiv:2601.18091},\n  year={2026},\n  url={https://arxiv.org/abs/2601.18091}\n}\n\n@inproceedings{rac2025,\n  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},\n  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  url={https://arxiv.org/abs/2509.12464}\n}\n\n@article{doingmore2026,\n  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n  journal={arXiv preprint arXiv:2604.25098},\n  year={2026},\n  url={https://arxiv.org/abs/2604.25098}\n}\n\n@inproceedings{p2law2025,\n  title={{P\\textsuperscript{2}} Law: Scaling Law for Post-Training After Model Pruning},\n  author={Chen, Xiaodong and Hu, Yuxuan and Zhang, Xiaokang and Wang, Yanling and Li, Cuiping and Chen, Hong and Zhang, Jing},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2025},\n  url={https://arxiv.org/abs/2411.10272}\n}\n\n@inproceedings{pat2025,\n  title={{PAT}: Pruning-Aware Tuning for Large Language Models},\n  author={Liu, Yijiang and Yang, Huanrui and Chen, Youxin and Zhang, Rongyu and Wang, Miao and Du, Yuan and Du, Li},\n  booktitle={Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  url={https://arxiv.org/abs/2408.14721}\n}\n\n@article{opsd2026,\n  title={{OPSD} Compresses What {RLVR} Teaches: A Post-{RL} Compaction Stage for Reasoning Models},\n  author={Kim, Jaehoon and Lee, Dongha},\n  journal={arXiv preprint arXiv:2605.06188},\n  year={2026},\n  url={https://arxiv.org/abs/2605.06188}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
    "old_string": "@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carlin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}",
    "new_string": "@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carlin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}\n\n@inproceedings{ainslie2023gqa,\n  title={{GQA}: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints},\n  author={Ainslie, Joshua and Lee-Thorp, James and de Jong, Michiel and Zemlyanskiy, Yury and Lebr{\\'o}n, Federico and Sanghai, Sumit},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.13245}\n}\n\n@article{shortgpt2024,\n  title={{ShortGPT}: Layers in Large Language Models are More Redundant Than You Expect},\n  author={Men, Xin and Xu, Mingyu and Zhang, Qingyu and Wang, Bingning and Lin, Hongyu and Lu, Yaojie and Han, Xianpei and Chen, Weipeng},\n  journal={arXiv preprint arXiv:2403.03853},\n  year={2024},\n  url={https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{slicegpt2024,\n  title={{SliceGPT}: Compress Large Language Models by Deleting Rows and Columns},\n  author={Ashkboos, Saleh and Croci, Maximilian L. and Gennari do Nascimento, Marcelo and Hoefler, Torsten and Hensman, James},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2401.15024}\n}\n\n@inproceedings{wanda2024,\n  title={A Simple and Effective Pruning Approach for Large Language Models},\n  author={Sun, Mingjie and Liu, Zhuang and Bair, Anna and Kolter, J. Zico},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2306.11695}\n}\n\n@article{llms2lrms2026,\n  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},\n  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},\n  journal={arXiv preprint arXiv:2601.18091},\n  year={2026},\n  url={https://arxiv.org/abs/2601.18091}\n}\n\n@inproceedings{rac2025,\n  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},\n  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  url={https://arxiv.org/abs/2509.12464}\n}\n\n@article{doingmore2026,\n  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n  journal={arXiv preprint arXiv:2604.25098},\n  year={2026},\n  url={https://arxiv.org/abs/2604.25098}\n}\n\n@inproceedings{p2law2025,\n  title={{P\\textsuperscript{2}} Law: Scaling Law for Post-Training After Model Pruning},\n  author={Chen, Xiaodong and Hu, Yuxuan and Zhang, Xiaokang and Wang, Yanling and Li, Cuiping and Chen, Hong and Zhang, Jing},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2025},\n  url={https://arxiv.org/abs/2411.10272}\n}\n\n@inproceedings{pat2025,\n  title={{PAT}: Pruning-Aware Tuning for Large Language Models},\n  author={Liu, Yijiang and Yang, Huanrui and Chen, Youxin and Zhang, Rongyu and Wang, Miao and Du, Yuan and Du, Li},\n  booktitle={Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  url={https://arxiv.org/abs/2408.14721}\n}\n\n@article{opsd2026,\n  title={{OPSD} Compresses What {RLVR} Teaches: A Post-{RL} Compaction Stage for Reasoning Models},\n  author={Kim, Jaehoon and Lee, Dongha},\n  journal={arXiv preprint arXiv:2605.06188},\n  year={2026},\n  url={https://arxiv.org/abs/2605.06188}\n}"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T06:58:25.620022+00:00_

&lt;tool_use_error>String to replace not found in file.
String: @inproceedings{frankle2019lth,
  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},
  author={Frankle, Jonathan and Carlin, Michael},
  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},
  year={2019},
  url={https://arxiv.org/abs/1803.03635}
}&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T06:58:25.620152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
  "offset": "88"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
    "offset": "88"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T06:58:25.620286+00:00_

88	
89	@inproceedings{frankle2019lth,
90	  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},
91	  author={Frankle, Jonathan and Carbin, Michael},
92	  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},
93	  year={2019},
94	  url={https://arxiv.org/abs/1803.03635}
95	}
96	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T06:58:25.620418+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
  "old_string": "@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carbin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}",
  "new_string": "@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carbin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}\n\n@inproceedings{ainslie2023gqa,\n  title={{GQA}: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints},\n  author={Ainslie, Joshua and Lee-Thorp, James and de Jong, Michiel and Zemlyanskiy, Yury and Lebr{\\'o}n, Federico and Sanghai, Sumit},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.13245}\n}\n\n@article{shortgpt2024,\n  title={{ShortGPT}: Layers in Large Language Models are More Redundant Than You Expect},\n  author={Men, Xin and Xu, Mingyu and Zhang, Qingyu and Wang, Bingning and Lin, Hongyu and Lu, Yaojie and Han, Xianpei and Chen, Weipeng},\n  journal={arXiv preprint arXiv:2403.03853},\n  year={2024},\n  url={https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{slicegpt2024,\n  title={{SliceGPT}: Compress Large Language Models by Deleting Rows and Columns},\n  author={Ashkboos, Saleh and Croci, Maximilian L. and Gennari do Nascimento, Marcelo and Hoefler, Torsten and Hensman, James},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2401.15024}\n}\n\n@inproceedings{wanda2024,\n  title={A Simple and Effective Pruning Approach for Large Language Models},\n  author={Sun, Mingjie and Liu, Zhuang and Bair, Anna and Kolter, J. Zico},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2306.11695}\n}\n\n@article{llms2lrms2026,\n  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},\n  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},\n  journal={arXiv preprint arXiv:2601.18091},\n  year={2026},\n  url={https://arxiv.org/abs/2601.18091}\n}\n\n@inproceedings{rac2025,\n  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},\n  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  url={https://arxiv.org/abs/2509.12464}\n}\n\n@article{doingmore2026,\n  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n  journal={arXiv preprint arXiv:2604.25098},\n  year={2026},\n  url={https://arxiv.org/abs/2604.25098}\n}\n\n@inproceedings{p2law2025,\n  title={{P\\textsuperscript{2}} Law: Scaling Law for Post-Training After Model Pruning},\n  author={Chen, Xiaodong and Hu, Yuxuan and Zhang, Xiaokang and Wang, Yanling and Li, Cuiping and Chen, Hong and Zhang, Jing},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2025},\n  url={https://arxiv.org/abs/2411.10272}\n}\n\n@inproceedings{pat2025,\n  title={{PAT}: Pruning-Aware Tuning for Large Language Models},\n  author={Liu, Yijiang and Yang, Huanrui and Chen, Youxin and Zhang, Rongyu and Wang, Miao and Du, Yuan and Du, Li},\n  booktitle={Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  url={https://arxiv.org/abs/2408.14721}\n}\n\n@article{opsd2026,\n  title={{OPSD} Compresses What {RLVR} Teaches: A Post-{RL} Compaction Stage for Reasoning Models},\n  author={Kim, Jaehoon and Lee, Dongha},\n  journal={arXiv preprint arXiv:2605.06188},\n  year={2026},\n  url={https://arxiv.org/abs/2605.06188}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib",
    "old_string": "@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carbin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}",
    "new_string": "@inproceedings{frankle2019lth,\n  title={The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks},\n  author={Frankle, Jonathan and Carbin, Michael},\n  booktitle={Proceedings of the 7th International Conference on Learning Representations (ICLR)},\n  year={2019},\n  url={https://arxiv.org/abs/1803.03635}\n}\n\n@inproceedings{ainslie2023gqa,\n  title={{GQA}: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints},\n  author={Ainslie, Joshua and Lee-Thorp, James and de Jong, Michiel and Zemlyanskiy, Yury and Lebr{\\'o}n, Federico and Sanghai, Sumit},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.13245}\n}\n\n@article{shortgpt2024,\n  title={{ShortGPT}: Layers in Large Language Models are More Redundant Than You Expect},\n  author={Men, Xin and Xu, Mingyu and Zhang, Qingyu and Wang, Bingning and Lin, Hongyu and Lu, Yaojie and Han, Xianpei and Chen, Weipeng},\n  journal={arXiv preprint arXiv:2403.03853},\n  year={2024},\n  url={https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{slicegpt2024,\n  title={{SliceGPT}: Compress Large Language Models by Deleting Rows and Columns},\n  author={Ashkboos, Saleh and Croci, Maximilian L. and Gennari do Nascimento, Marcelo and Hoefler, Torsten and Hensman, James},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2401.15024}\n}\n\n@inproceedings{wanda2024,\n  title={A Simple and Effective Pruning Approach for Large Language Models},\n  author={Sun, Mingjie and Liu, Zhuang and Bair, Anna and Kolter, J. Zico},\n  booktitle={Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2306.11695}\n}\n\n@article{llms2lrms2026,\n  title={From {LLMs} to {LRMs}: Rethinking Pruning for Reasoning-Centric Models},\n  author={Ding, Longwei and Zhao, Anhao and Ye, Fanghua and Chen, Ziyang and Shen, Xiaoyu},\n  journal={arXiv preprint arXiv:2601.18091},\n  year={2026},\n  url={https://arxiv.org/abs/2601.18091}\n}\n\n@inproceedings{rac2025,\n  title={Reasoning Models Can be Accurately Pruned Via Chain-of-Thought Reconstruction},\n  author={Lucas, Ryan and Behdin, Kayhan and Wang, Zhipeng and Song, Qingquan and Tang, Shao and Mazumder, Rahul},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  url={https://arxiv.org/abs/2509.12464}\n}\n\n@article{doingmore2026,\n  title={Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n  author={Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n  journal={arXiv preprint arXiv:2604.25098},\n  year={2026},\n  url={https://arxiv.org/abs/2604.25098}\n}\n\n@inproceedings{p2law2025,\n  title={{P\\textsuperscript{2}} Law: Scaling Law for Post-Training After Model Pruning},\n  author={Chen, Xiaodong and Hu, Yuxuan and Zhang, Xiaokang and Wang, Yanling and Li, Cuiping and Chen, Hong and Zhang, Jing},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2025},\n  url={https://arxiv.org/abs/2411.10272}\n}\n\n@inproceedings{pat2025,\n  title={{PAT}: Pruning-Aware Tuning for Large Language Models},\n  author={Liu, Yijiang and Yang, Huanrui and Chen, Youxin and Zhang, Rongyu and Wang, Miao and Du, Yuan and Du, Li},\n  booktitle={Proceedings of the 39th AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  url={https://arxiv.org/abs/2408.14721}\n}\n\n@article{opsd2026,\n  title={{OPSD} Compresses What {RLVR} Teaches: A Post-{RL} Compaction Stage for Reasoning Models},\n  author={Kim, Jaehoon and Lee, Dongha},\n  journal={arXiv preprint arXiv:2605.06188},\n  year={2026},\n  url={https://arxiv.org/abs/2605.06188}\n}"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T06:58:25.620615+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-14T06:58:25.620781+00:00_

完成。汇报：

**文件同步**
- `method.tex` — 从远程同步到本地（124行）
- `related_work.tex` — 从远程同步到本地

**新增 .bib 条目（10个）**

| Key | 论文 | 来源 |
|-----|------|------|
| `ainslie2023gqa` | GQA (Ainslie et al., EMNLP 2023) | arXiv:2305.13245 |
| `shortgpt2024` | ShortGPT (Men et al., 2024) | arXiv:2403.03853 |
| `slicegpt2024` | SliceGPT (Ashkboos et al., ICLR 2024) | arXiv:2401.15024 |
| `wanda2024` | Wanda (Sun et al., ICLR 2024) | arXiv:2306.11695 |
| `llms2lrms2026` | From LLMs to LRMs (Ding et al., 2026) | arXiv:2601.18091 |
| `rac2025` | RAC CoT Reconstruction (Lucas et al., NeurIPS 2025) | arXiv:2509.12464 |
| `doingmore2026` | Doing More With Less (Monjur et al., 2026) | arXiv:2604.25098 |
| `p2law2025` | P² Law (Chen et al., ACL 2025) | arXiv:2411.10272 |
| `pat2025` | PAT (Liu et al., AAAI 2025) | arXiv:2408.14721 |
| `opsd2026` | OPSD (Kim & Lee, 2026) | arXiv:2605.06188 |

**最终 references.bib 总条目数：22**（原有 12 + 新增 10）。method.tex 和 related_work.tex 中所有 cite key 现已全部覆盖。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_sync-paper-and-bib_20260514T065218"
}
```

</details>

---
