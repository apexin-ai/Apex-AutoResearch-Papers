# ops verify bib and prep eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_ops_verify_bib_and_prep_eval_20260523T154920.jsonl`
- **Structured JSON:** [`fe49750f12d8238f51e6.json`](../../sessions/fe/fe49750f12d8238f51e6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-23T15:55:31.617472+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T15:55:31.617904+00:00_

1	
2	\section{Related Work}
3	\label{sec:related}
4	
5	\subsection{Safety in Vision-Language-Action Models}
6	
7	Vision-language-action (VLA) models achieve high task success rates on manipulation benchmarks~\cite{kim2024openvla, brohan2023rt2, ma2026vlanext, shukor2025smolvla} % Kim et al., OpenVLA, arXiv:2406.09246; Brohan et al., RT-2, arXiv:2307.15818
8	but remain prone to collisions when obstacles occupy the manipulation workspace. Two strategies have emerged to address this gap between task completion and behavioral safety~\cite{li2026vlasafety}.
9	
10	The first strategy applies runtime constraints to filter or adjust unsafe actions~\cite{yu2026safenightvla}. The AEGIS framework~\cite{hu2025vlsa} % Hu et al., "VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer", arXiv:2512.11891, 2025
11	adds a plug-and-play safety layer that identifies obstacles through a vision-language assessment module and enforces avoidance via a control barrier function (CBF) quadratic program, improving collision avoidance rate by 59.16 percentage points on SafeLIBERO, a benchmark of 32 safety-critical manipulation scenarios introduced in the same work. CoFreeVLA~\cite{zhai2026cofreevla} % Zhai et al., "CoFreeVLA: Collision-Free Dual-Arm Manipulation via VLA Model and Risk Estimation", arXiv:2601.21712, 2026
12	addresses a related problem in dual-arm settings by training a short-horizon collision risk estimator that gates risky commands and triggers recovery to safe configurations. Control barrier functions have also been applied directly to manipulation independently of VLAs~\cite{kwon2026learningnudge, long2025neuralcsbf}. Morton and Pavone~\cite{morton2025oscbf} % Morton and Pavone, "Safe, Task-Consistent Manipulation with Operational Space Control Barrier Functions", IROS 2025, arXiv:2503.06736
13	formulate operational-space CBFs that scale to hundreds of simultaneous constraints at real-time control rates, and Raja et al.~\cite{raja2024ogmcbf} % Raja et 
…[truncated 9696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T15:55:31.618095+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T15:55:31.618231+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T15:55:31.618376+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T15:55:31.618614+00:00_

1	% References for OccSafe-VLA
2	% Bib key convention: {first_author_surname_lower}{year}{keyword_lower}
3	
4	% ============================================================
5	% VLA Safety
6	% ============================================================
7	
8	@article{hu2025vlsa,
9	  author    = {Songqiao Hu and Zeyi Liu and Shuang Liu and Jun Cen and Zihan Meng and Xiao He},
10	  title     = {{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
11	  journal   = {arXiv preprint arXiv:2512.11891},
12	  year      = {2025},
13	  note      = {arXiv:2512.11891}
14	}
15	
16	@inproceedings{zhang2025safevla,
17	  author    = {Borong Zhang and others},
18	  title     = {{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
19	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
20	  year      = {2025},
21	  note      = {Spotlight. arXiv:2503.03480}
22	}
23	
24	@article{zhai2026cofreevla,
25	  author    = {Xuanran Zhai and others},
26	  title     = {{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via {VLA} Model and Risk Estimation},
27	  journal   = {arXiv preprint arXiv:2601.21712},
28	  year      = {2026},
29	  note      = {arXiv:2601.21712}
30	}
31	
32	@article{yu2026safenightvla,
33	  author    = {Yu and others},
34	  title     = {{Safe-Night VLA}: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation},
35	  journal   = {arXiv preprint arXiv:2603.05754},
36	  year      = {2026},
37	  note      = {arXiv:2603.05754}
38	}
39	
40	@article{li2026vlasafety,
41	  author    = {Li and others},
42	  title     = {Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
43	  journal   = {arXiv preprint arXiv:2604.23775},
44	  year      = {2026},
45	  note      = {arXiv:2604.23775}
46	}
47	
48	% ============================================================
49	% Safety Mechanisms (barrier functions / occupancy-based sa
…[truncated 17109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T15:55:31.618811+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "occsafe_vla",
  "filters": "{'exp_name': 'vanilla_retrain_s0'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "occsafe_vla",
    "filters": "{'exp_name': 'vanilla_retrain_s0'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T15:55:31.618947+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3709}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T15:55:31.619066+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "occsafe_vla",
  "filters": "{'exp_name': 'full_occ_retrain_s0'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "occsafe_vla",
    "filters": "{'exp_name': 'full_occ_retrain_s0'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T15:55:31.619188+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1718}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T15:55:31.619302+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "occsafe_vla",
  "filters": "{'exp_name': 'reverse_cutoff_s0'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "occsafe_vla",
    "filters": "{'exp_name': 'reverse_cutoff_s0'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T15:55:31.619421+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1773}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T15:55:31.619532+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "occsafe_vla",
  "filters": "{'exp_name': 'cutoff_25k_s0'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "occsafe_vla",
    "filters": "{'exp_name': 'cutoff_25k_s0'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T15:55:31.619654+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.181}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T15:55:31.619796+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "occsafe_vla",
  "filters": "{'exp_name': 'cutoff_s1_eval'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "occsafe_vla",
    "filters": "{'exp_name': 'cutoff_s1_eval'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T15:55:31.619912+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1811}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T15:55:31.620112+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "choi2026vlaeval",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Grep",
  "tool_args": {
    "pattern": "choi2026vlaeval",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T15:55:31.620261+00:00_

docs/paper/references.tex:331:@article{choi2026vlaeval,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T15:55:31.620380+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "occsafe_vla",
  "limit": "30",
  "fields": "['exp_name', 'status', 'spec']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "occsafe_vla",
    "limit": "30",
    "fields": "['exp_name', 'status', 'spec']"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T15:55:31.620893+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"cutoff_s2_v2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"torchrun finetune.py --occ_detach false --occ_loss_cutoff_step 35000\", \"server\": \"westd-10894\", \"data_path\": \"/root/autodl-tmp/data/modified_libero_rlds/libero_spatial_no_noops\", \"data_count\": 25000, \"model_name\": \"openvla-7b\", \"seed\": 44, \"checkpoint_source\": \"openvla-7b (from scratch)\", \"eval_data\": \"N/A (training)\", \"pid\": 435043, \"log_path\": \"~/runs/occsafe_vla/cutoff_s2_v2.log\", \"gpu\": \"cuda:0\", \"master_port\": 29505}}, \"detach_ln_s2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"torchrun finetune.py --resume True --resume_step 10000\", \"server\": \"westd-10894\", \"gpu\": [\"cuda:3\"], \"pid\": 442016, \"log_path\": \"~/runs/occsafe_vla/detach_ln_s2.log\", \"submitted_at\": \"2026-05-23T05:27:26.856Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/modified_libero_rlds/libero_spatial_no_noops\", \"data_count\": 25000, \"model_name\": \"openvla-7b\", \"seed\": 44, \"checkpoint_source\": \"openvla-7b (from scratch)\", \"eval_data\": \"N/A (training)\"}}, \"detach_ln_s1\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"torchrun finetune.py --resume True --resume_step 20000\", \"server\": \"westd-10894\", \"gpu\": [\"cuda:2\"], \"pid\": 439399, \"log_path\": \"~/runs/occsafe_vla/detach_ln_s1.log\", \"submitted_at\": \"2026-05-23T05:27:23.673Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/modified_libero_rlds/libero_spatial_no_noops\", \"data_count\": 25000, \"model_name\": \"openvla-7b\", \"seed\": 43, \"checkpoint_source\": \"openvla-7b (from scratch)\", \"eval_data\": \"N/A (training)\"}}, \"detach_ln_s0\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"torchrun finetune.py --resume True --resume_step 20000\", \"s
…[truncated 21638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T15:55:31.621118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.tex",
  "offset": "320",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/references.tex",
    "offset": "320",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T15:55:31.621263+00:00_

320	  note      = {arXiv:2602.18532}
321	}
322	
323	@article{shukor2025smolvla,
324	  author    = {Shukor and others},
325	  title     = {{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},
326	  journal   = {arXiv preprint arXiv:2506.01844},
327	  year      = {2025},
328	  note      = {arXiv:2506.01844}
329	}
330	
331	@article{choi2026vlaeval,
332	  author    = {Choi and others},
333	  title     = {vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models},
334	  journal   = {arXiv preprint arXiv:2603.13966},
335	  year      = {2026},
336	  note      = {arXiv:2603.13966}
337	}
338	
339	% ============================================================
340	% Benchmarks
341	% ============================================================
342	
343	@inproceedings{liu2023libero,
344	  author    = {Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},
345	  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
346	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
347	  year      = {2023},
348	  note      = {arXiv:2306.03310}
349	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T15:55:31.621395+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "occsafe_vla",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "occsafe_vla",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T15:55:31.621578+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/memory.md\", \"content\": \"# Project Memory — occsafe_vla\\n\\n## 决策与约束\\n\\n### Depth 2-seed 初步结论：Depth ≈ Vanilla，指向 Path B (2026-05-23)\\n\\n**depth_s2 (seed44) + depth_s3 (seed45), @50000, 50r：**\\n| seed | CAR | TSR |\\n|------|-----|-----|\\n| s2 | 0.758 | 0.860 |\\n| s3 | 0.806 | 0.848 |\\n| **avg** | **0.782** | **0.854** |\\n\\n**Depth avg CAR=0.782 vs Vanilla avg CAR=0.780，差仅 +0.2pp，在噪声范围内。**\\n\\nDepth < Random (0.789)：egocentric depth 信号没有比 random noise 更好的正则化效果。这否定了\\\"depth 作为更自然的空间信号\\\"的假说——空间内容（无论是 BEV occ 还是 ego depth）不提供有意义的信号增量，梯度流正则化才是核心效应。\\n\\n**Depth seed 方差 (std=0.034) 与 OCC/Random 类似**——辅助任务普遍放大 seed 敏感性，不限于 BEV 表征。\\n\\n等待 depth_s0/s1 完成后做 4-seed 统计检验确认。\\n\\n### 3-Seed 决定性结论：OCC = Vanilla (2026-05-22)\\n\\n**47500 checkpoint（apple-to-apple 对比点，3 seed）：**\\n| 条件 | s0 CAR | s1 CAR | s2 CAR | **avg CAR** | **avg TSR** |\\n|------|--------|--------|--------|------------|------------|\\n| OCC | 0.750 | 0.802 | 0.788 | **0.780** | **0.919** |\\n| Vanilla | 0.788 | 0.766 | 0.786 | **0.780** | **0.907** |\\n\\n**OCC 47500 avg CAR = Vanilla avg CAR = 0.780**。完全持平。\\n\\n**50000 checkpoint（3 seed）：**\\nOCC avg 0.797 vs Vanilla avg 0.780 (+1.7pp)，但主要由 s0 异常高值 (0.832) 驱动，且 47500→50000 行为 seed-dependent（s0 +8.2pp, s1 -1.4pp, s2 -1.8pp），不可靠。\\n\\n**OCC 放大 seed 敏感性**：OCC seed std ~0.026 vs Vanilla std ~0.012 (2.2x)。\\n\\n### 核心诊断结论：OCC 梯度流是隐式正则化器，BEV 空间信号有害 (2026-05-22)\\n**Ablation 2-seed 50r 排序：Random(0.806) > Vanilla(0.777) > Full OCC(0.769) > Detach(0.745)**\\n\\n更新至 3-seed 50r：\\n**Random(0.789) > OCC(0.797) > Depth(0.782, 2-seed) ≈ Vanilla(0.780) > Detach(0.746)**\\n\\n- Random OCC > Vanilla: 辅助任务的梯度流本身提供正向正则化效应\\n- Full OCC ≈ Vanilla: BEV 空间信号的负向干扰恰好抵消了梯度正则化收益\\n- Detach < Vanilla: 没有梯度流 → 没有正则化收益 → OCC head 前向计算只是额外开销\\n- Depth ≈ Vanilla: egocentric depth 的空间信号同样不提供有意义的增量\\n- 推论：辅助任务的空间内容（BEV 或 ego depth）对避障不提供信号增量——梯度流正则化是全部效应
…[truncated 1708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T15:55:31.621824+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls /root/autodl-tmp/checkpoints/reverse_cutoff_s0/ /root/autodl-tmp/checkpoints/cutoff_25k_s0/ 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls /root/autodl-tmp/checkpoints/reverse_cutoff_s0/ /root/autodl-tmp/checkpoints/cutoff_25k_s0/ 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T15:55:31.621964+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T15:55:31.622089+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\\\\\bibliography|\\\\\\\\input\\{references|\\\\\\\\addbibresource",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\\\\\bibliography|\\\\\\\\input\\{references|\\\\\\\\addbibresource",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T15:55:31.622206+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T15:55:31.622317+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "choi2026vlaeval",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Grep",
  "tool_args": {
    "pattern": "choi2026vlaeval",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T15:55:31.622426+00:00_

docs/paper/references.tex:331:@article{choi2026vlaeval,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T15:55:31.622562+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls /root/autodl-tmp/checkpoints/reverse_cutoff_s0/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls /root/autodl-tmp/checkpoints/reverse_cutoff_s0/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-23T15:55:31.622710+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls /root/autodl-tmp/checkpoints/cutoff_25k_s0/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls /root/autodl-tmp/checkpoints/cutoff_25k_s0/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-23T15:55:31.622853+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug\\nopenvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--30000_chkpt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-23T15:55:31.622971+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-23T15:55:31.623087+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug\\nopenvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--30000_chkpt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T15:55:31.623198+00:00_

docs/paper/references.tex
docs/paper/method.tex
docs/paper/experiment_setup.tex
docs/paper/results.tex
docs/paper/conclusion.tex
docs/paper/experiments.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/scenario_variants.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T15:55:31.623325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T15:55:31.623458+00:00_

1	% OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models
2	% Target: CoRL 2026
3	\documentclass{article}
4	
5	\usepackage[dvipsnames]{xcolor}
6	\usepackage{corl_2026}
7	
8	\usepackage{graphicx}
9	\usepackage{amsmath,amssymb}
10	\usepackage{booktabs}
11	\usepackage{enumitem}
12	\usepackage{subcaption}
13	
14	\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}
15	
16	\title{OccSafe-VLA: Occupancy-Aware Safety for Vision-Language-Action Models}
17	
18	\author{
19	Anonymous Author(s)
20	}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success rates yet remain behaviorally unsafe: on SafeLIBERO Level~I, OpenVLA attains 90.7\% task success but only 78.0\% collision avoidance.
27	This paper presents the first factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.
28	Six conditions on OpenVLA-OFT with LoRA vary gradient flow, label content, spatial reference frame, and temporal extent: Vanilla (action loss only), Full OCC (BEV occupancy with ground-truth labels), Random OCC (random binary labels), Detach OCC (ground-truth labels, encoder gradients blocked), Depth (egocentric depth prediction, 4 seeds), and Cutoff (occupancy for the first 35K steps only, 2 seeds$^{\dagger}$).
29	The central finding is that gradient flow through the vision encoder is a necessary condition for preventing safety degradation.
30	Detach OCC, the only condition blocking encoder gradients, drops collision avoidance to 74.6\% ($-$3.4\,pp vs.\ Vanilla at 78.0\%), while all gradient-flow conditions remain within 1.7\,pp of Vanilla (78.0--79.7\%).
31	Label content is secondary: structured occupancy, random binary maps, and egocentric depth yield comparable collision avoidance.
32	Cutoff$^{\dagger}$ retains the highest task success (91.5\%) but loses collision avoidance on the hardest safety task (T5 CAR 0.00).
33	Because the auxiliary head is di
…[truncated 489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T15:55:31.623652+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "references\\.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Grep",
  "tool_args": {
    "pattern": "references\\.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T15:55:31.623886+00:00_

artifacts/dream_reports/dream_20260523T034027/logs/review_best.log:84:[Omitted long matching line]
artifacts/dream_reports/dream_20260523T034027/logs/review_best.log:129:[Omitted long matching line]
artifacts/dream_reports/dream_20260523T034027/logs/review_best.log:166:{"type":"system","subtype":"task_progress","task_id":"afe5579a328e72e53","tool_use_id":"toolu_01VGfo15bnabCdVA3evbQgKc","description":"Reading docs/paper/references.tex","usage":{"total_tokens":59818,"tool_uses":19,"duration_ms":38760},"last_tool_name":"Read","uuid":"732ee557-5384-499c-ac52-75572b548e69","session_id":"6fd64fbd-040e-43dd-8257-d68950227536"}
artifacts/dream_reports/dream_20260523T034027/logs/review_best.log:167:[Omitted long matching line]
artifacts/dream_reports/dream_20260523T034027/logs/review_median.log:128:[Omitted long matching line]
artifacts/dream_reports/dream_20260523T034027/logs/review_median.log:159:{"type":"system","subtype":"task_progress","task_id":"a86b91e3060b7dad0","tool_use_id":"toolu_018fH1bx851t3wjnet2HMt5b","description":"Reading docs/paper/references.tex","usage":{"total_tokens":81995,"tool_uses":22,"duration_ms":64721},"last_tool_name":"Read","uuid":"72c6671d-eab2-4df9-80ae-51d6443c74f7","session_id":"d0b8a538-408e-485b-8d42-e69bd1c2f218"}
artifacts/dream_reports/dream_20260523T034027/logs/review_median.log:160:[Omitted long matching line]
artifacts/dream_reports/dream_20260523T034027/logs/review_median.log:174:[Omitted long matching line]
logs/chats/feishu_group_oc_b83478cb96de9d1a19f52f25842063f6.jsonl:878:[Omitted long matching line]
logs/chats/feishu_group_oc_b83478cb96de9d1a19f52f25842063f6.jsonl:1056:[Omitted long matching line]
logs/chats/feishu_group_oc_b83478cb96de9d1a19f52f25842063f6.jsonl:1152:[Omitted long matching line]
logs/chats/feishu_group_oc_b83478cb96de9d1a19f52f25842063f6.jsonl:1219:[Omitted long matching line]
logs/chats/feishu_group_oc_b83478cb96de9d1a19f52f25842063f6.jsonl:1221:[Omitted long matching line]
logs/chats/feishu_group_oc_b83478c
…[truncated 6564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T15:55:31.624073+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "occsafe_vla",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "occsafe_vla",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T15:55:31.624245+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/memory.md\", \"content\": \"# Project Memory — occsafe_vla\\n\\n## 决策与约束\\n\\n### Depth 2-seed 初步结论：Depth ≈ Vanilla，指向 Path B (2026-05-23)\\n\\n**depth_s2 (seed44) + depth_s3 (seed45), @50000, 50r：**\\n| seed | CAR | TSR |\\n|------|-----|-----|\\n| s2 | 0.758 | 0.860 |\\n| s3 | 0.806 | 0.848 |\\n| **avg** | **0.782** | **0.854** |\\n\\n**Depth avg CAR=0.782 vs Vanilla avg CAR=0.780，差仅 +0.2pp，在噪声范围内。**\\n\\nDepth < Random (0.789)：egocentric depth 信号没有比 random noise 更好的正则化效果。这否定了\\\"depth 作为更自然的空间信号\\\"的假说——空间内容（无论是 BEV occ 还是 ego depth）不提供有意义的信号增量，梯度流正则化才是核心效应。\\n\\n**Depth seed 方差 (std=0.034) 与 OCC/Random 类似**——辅助任务普遍放大 seed 敏感性，不限于 BEV 表征。\\n\\n等待 depth_s0/s1 完成后做 4-seed 统计检验确认。\\n\\n### 3-Seed 决定性结论：OCC = Vanilla (2026-05-22)\\n\\n**47500 checkpoint（apple-to-apple 对比点，3 seed）：**\\n| 条件 | s0 CAR | s1 CAR | s2 CAR | **avg CAR** | **avg TSR** |\\n|------|--------|--------|--------|------------|------------|\\n| OCC | 0.750 | 0.802 | 0.788 | **0.780** | **0.919** |\\n| Vanilla | 0.788 | 0.766 | 0.786 | **0.780** | **0.907** |\\n\\n**OCC 47500 avg CAR = Vanilla avg CAR = 0.780**。完全持平。\\n\\n**50000 checkpoint（3 seed）：**\\nOCC avg 0.797 vs Vanilla avg 0.780 (+1.7pp)，但主要由 s0 异常高值 (0.832) 驱动，且 47500→50000 行为 seed-dependent（s0 +8.2pp, s1 -1.4pp, s2 -1.8pp），不可靠。\\n\\n**OCC 放大 seed 敏感性**：OCC seed std ~0.026 vs Vanilla std ~0.012 (2.2x)。\\n\\n### 核心诊断结论：OCC 梯度流是隐式正则化器，BEV 空间信号有害 (2026-05-22)\\n**Ablation 2-seed 50r 排序：Random(0.806) > Vanilla(0.777) > Full OCC(0.769) > Detach(0.745)**\\n\\n更新至 3-seed 50r：\\n**Random(0.789) > OCC(0.797) > Depth(0.782, 2-seed) ≈ Vanilla(0.780) > Detach(0.746)**\\n\\n- Random OCC > Vanilla: 辅助任务的梯度流本身提供正向正则化效应\\n- Full OCC ≈ Vanilla: BEV 空间信号的负向干扰恰好抵消了梯度正则化收益\\n- Detach < Vanilla: 没有梯度流 → 没有正则化收益 → OCC head 前向计算只是额外开销\\n- Depth ≈ Vanilla: egocentric depth 的空间信号同样不提供有意义的增量\\n- 推论：辅助任务的空间内容（BEV 或 ego depth）对避障不提供信号增量——梯度流正则化是全部效应
…[truncated 1708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T15:55:31.624416+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "occsafe_vla",
  "file": "memory.md",
  "content": "# Project Memory — occsafe_vla\n\n## 决策与约束\n\n### Depth 2-seed 初步结论：Depth ≈ Vanilla，指向 Path B (2026-05-23)\n\n**depth_s2 (seed44) + depth_s3 (seed45), @50000, 50r：**\n| seed | CAR | TSR |\n|------|-----|-----|\n| s2 | 0.758 | 0.860 |\n| s3 | 0.806 | 0.848 |\n| **avg** | **0.782** | **0.854** |\n\n**Depth avg CAR=0.782 vs Vanilla avg CAR=0.780，差仅 +0.2pp，在噪声范围内。**\n\nDepth < Random (0.789)：egocentric depth 信号没有比 random noise 更好的正则化效果。这否定了\"depth 作为更自然的空间信号\"的假说——空间内容（无论是 BEV occ 还是 ego depth）不提供有意义的信号增量，梯度流正则化才是核心效应。\n\n**Depth seed 方差 (std=0.034) 与 OCC/Random 类似**——辅助任务普遍放大 seed 敏感性，不限于 BEV 表征。\n\n等待 depth_s0/s1 完成后做 4-seed 统计检验确认。\n\n### 3-Seed 决定性结论：OCC = Vanilla (2026-05-22)\n\n**47500 checkpoint（apple-to-apple 对比点，3 seed）：**\n| 条件 | s0 CAR | s1 CAR | s2 CAR | **avg CAR** | **avg TSR** |\n|------|--------|--------|--------|------------|------------|\n| OCC | 0.750 | 0.802 | 0.788 | **0.780** | **0.919** |\n| Vanilla | 0.788 | 0.766 | 0.786 | **0.780** | **0.907** |\n\n**OCC 47500 avg CAR = Vanilla avg CAR = 0.780**。完全持平。\n\n**50000 checkpoint（3 seed）：**\nOCC avg 0.797 vs Vanilla avg 0.780 (+1.7pp)，但主要由 s0 异常高值 (0.832) 驱动，且 47500→50000 行为 seed-dependent（s0 +8.2pp, s1 -1.4pp, s2 -1.8pp），不可靠。\n\n**OCC 放大 seed 敏感性**：OCC seed std ~0.026 vs Vanilla std ~0.012 (2.2x)。\n\n### 核心诊断结论：OCC 梯度流是隐式正则化器，BEV 空间信号有害 (2026-05-22)\n**Ablation 2-seed 50r 排序：Random(0.806) > Vanilla(0.777) > Full OCC(0.769) > Detach(0.745)**\n\n更新至 3-seed 50r：\n**Random(0.789) > OCC(0.797) > Depth(0.782, 2-seed) ≈ Vanilla(0.780) > Detach(0.746)**\n\n- Random OCC > Vanilla: 辅助任务的梯度流本身提供正向正则化效应\n- Full OCC ≈ Vanilla: BEV 空间信号的负向干扰恰好抵消了梯度正则化收益\n- Detach < Vanilla: 没有梯度流 → 没有正则化收益 → OCC head 前向计算只是额外开销\n- Depth ≈ Vanilla: egocentric depth 的空间信号同样不提供有意义的增量\n- 推论：辅助任务的空间内容（BEV 或 ego depth）对避障不提供信号增量——梯度流正则化是全部效应\n\n### Per-Task Case 诊断 (2026-05-22, 50r formal)\n**Case 统计: A=0, B=6, C=2, D=2**\n- Case B（空间信号无用）主导：T0/T2/T4/T5/T8/T9\n- Case C（BEV 有害 + gradient 也不帮忙）：T3, T6 — 这两个 hard task 上 OCC 全面有害\n- Case D（混合）：T1, T7\n- **Case A = 0**：排除了\"gradient 干扰\"假说\n- **T5 特殊**：FullOCC(0.20), Random(0.24) 远超 Vanilla(0.07), Detach(0.05)——gradient flow 对 T5 至关重要，正则化效应最强的 task（物理约束最强的场景）\n\n### random_s0 seed 误报 (2026-05-22)\n原始 random_s0 50r eval config 中已包含 seed=42。之前 Worker 报告\"无 seed\"是检查方法有误（查 /proc/cmdline 而非 config 文件）。rerun 是多余的，已 kill。\n\n### occ_s1 数据不可用 (2026-05-21)\n- mvp_occ_s1 从 17500 resume，数据受 confound 污染，被 D013 排除\n- occ_s1_fresh 替代完成，47500 和 50000 eval 均完成\n\n## 待提交 eval 命令 (2026-05-23)\n\nwestd-34685 上 4 个实验（vanilla_retrain_s0, full_occ_retrain_s0, reverse_cutoff_s0, cutoff_25k_s0）完成后的操作：\n\n- **vanilla_retrain_s0** / **full_occ_retrain_s0**：仅需梯度分析，不需要 eval\n- **reverse_cutoff_s0** / **cutoff_25k_s0**：需要 SafeLIBERO eval\n\n### reverse_cutoff_s0_eval\n\n```bash\nCUDA_VISIBLE_DEVICES=0 MUJOCO_EGL_DEVICE_ID=0 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \\\n  --pretrained_checkpoint /root/autodl-tmp/checkpoints/reverse_cutoff_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n  --num_rollouts 50 --seed 42\n```\n\n- 服务器: westd-34685\n- GPU: 训练完成后任选空闲 GPU，CUDA_VISIBLE_DEVICES 和 MUJOCO_EGL_DEVICE_ID 必须匹配物理 GPU 编号\n- 参考: cutoff_s1_eval 命令格式（同服务器已成功完成）\n- 预计耗时: ~1h（参考 cutoff_s0_eval wall_clock 3427s）\n\n### cutoff_25k_s0_eval\n\n```bash\nCUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \\\n  --pretrained_checkpoint /root/autodl-tmp/checkpoints/cutoff_25k_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n  --num_rollouts 50 --seed 42\n```\n\n- 服务器: westd-34685\n- GPU: 同上，按物理 GPU 编号匹配\n- 两个 eval 可并行跑在不同 GPU 上\n\n### 注意事项\n- checkpoint 路径中的目录名模式已通过 `ls` 确认（当前 30000_chkpt 已存在，50000_chkpt 待训练完成后生成）\n- conda 环境激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe`\n- 工作目录: `cd /root/occsafe_vla/openvla-oft`\n- 如通过 submit_training_job 提交，conda 和 cwd 由框架自动处理\n\n## 基础设施经验\n\n### 训练命令必须显式指定所有关键参数 (2026-05-23)\n**事故**：cutoff_s2 提交时缺少 `--num_images_in_input 2 --use_proprio True`，使用了脚本默认值（1-image, no-proprio），导致模型架构不同（少 proprio_projector 16.8M 参数），训练速度 2.05 vs 1.07 it/s，结果完全不可比。训练 + eval 均作废。\n**教训**：提交任何训练实验时，必须显式写出以下参数，不依赖脚本默认值：\n```\n--num_images_in_input 2 --use_proprio True --use_l1_regression True\n--batch_size 8 --learning_rate 5e-4 --lora_rank 32 --image_aug True\n```\n**检测方法**：trainable params 总数应为 ~279,977,608（含 proprio_projector）。如果显著偏低，配置有误。训练速度应为 ~1.0-1.1 it/s，如果 >1.5 it/s 说明 input 配置不对。\n\n### westd-34685 磁盘管理教训 (2026-05-22)\n- 350G 数据盘满导致 3 个实验同时崩溃（save_freq=2500 时 checkpoint 积累过快）\n- occ_s1_fresh 残留 149G 是主要元凶\n- 从头重跑时改用 save_freq=10000 减少 checkpoint 数量\n- 教训：提交实验前检查磁盘空间，特别是多实验共用数据盘时\n\n### conda 环境 (2026-05-22)\n- 两台服务器均使用 conda env `occsafe`\n- 激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe`\n- 不要假设 .venv 存在\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "occsafe_vla",
    "file": "memory.md",
    "content": "# Project Memory — occsafe_vla\n\n## 决策与约束\n\n### Depth 2-seed 初步结论：Depth ≈ Vanilla，指向 Path B (2026-05-23)\n\n**depth_s2 (seed44) + depth_s3 (seed45), @50000, 50r：**\n| seed | CAR | TSR |\n|------|-----|-----|\n| s2 | 0.758 | 0.860 |\n| s3 | 0.806 | 0.848 |\n| **avg** | **0.782** | **0.854** |\n\n**Depth avg CAR=0.782 vs Vanilla avg CAR=0.780，差仅 +0.2pp，在噪声范围内。**\n\nDepth < Random (0.789)：egocentric depth 信号没有比 random noise 更好的正则化效果。这否定了\"depth 作为更自然的空间信号\"的假说——空间内容（无论是 BEV occ 还是 ego depth）不提供有意义的信号增量，梯度流正则化才是核心效应。\n\n**Depth seed 方差 (std=0.034) 与 OCC/Random 类似**——辅助任务普遍放大 seed 敏感性，不限于 BEV 表征。\n\n等待 depth_s0/s1 完成后做 4-seed 统计检验确认。\n\n### 3-Seed 决定性结论：OCC = Vanilla (2026-05-22)\n\n**47500 checkpoint（apple-to-apple 对比点，3 seed）：**\n| 条件 | s0 CAR | s1 CAR | s2 CAR | **avg CAR** | **avg TSR** |\n|------|--------|--------|--------|------------|------------|\n| OCC | 0.750 | 0.802 | 0.788 | **0.780** | **0.919** |\n| Vanilla | 0.788 | 0.766 | 0.786 | **0.780** | **0.907** |\n\n**OCC 47500 avg CAR = Vanilla avg CAR = 0.780**。完全持平。\n\n**50000 checkpoint（3 seed）：**\nOCC avg 0.797 vs Vanilla avg 0.780 (+1.7pp)，但主要由 s0 异常高值 (0.832) 驱动，且 47500→50000 行为 seed-dependent（s0 +8.2pp, s1 -1.4pp, s2 -1.8pp），不可靠。\n\n**OCC 放大 seed 敏感性**：OCC seed std ~0.026 vs Vanilla std ~0.012 (2.2x)。\n\n### 核心诊断结论：OCC 梯度流是隐式正则化器，BEV 空间信号有害 (2026-05-22)\n**Ablation 2-seed 50r 排序：Random(0.806) > Vanilla(0.777) > Full OCC(0.769) > Detach(0.745)**\n\n更新至 3-seed 50r：\n**Random(0.789) > OCC(0.797) > Depth(0.782, 2-seed) ≈ Vanilla(0.780) > Detach(0.746)**\n\n- Random OCC > Vanilla: 辅助任务的梯度流本身提供正向正则化效应\n- Full OCC ≈ Vanilla: BEV 空间信号的负向干扰恰好抵消了梯度正则化收益\n- Detach < Vanilla: 没有梯度流 → 没有正则化收益 → OCC head 前向计算只是额外开销\n- Depth ≈ Vanilla: egocentric depth 的空间信号同样不提供有意义的增量\n- 推论：辅助任务的空间内容（BEV 或 ego depth）对避障不提供信号增量——梯度流正则化是全部效应\n\n### Per-Task Case 诊断 (2026-05-22, 50r formal)\n**Case 统计: A=0, B=6, C=2, D=2**\n- Case B（空间信号无用）主导：T0/T2/T4/T5/T8/T9\n- Case C（BEV 有害 + gradient 也不帮忙）：T3, T6 — 这两个 hard task 上 OCC 全面有害\n- Case D（混合）：T1, T7\n- **Case A = 0**：排除了\"gradient 干扰\"假说\n- **T5 特殊**：FullOCC(0.20), Random(0.24) 远超 Vanilla(0.07), Detach(0.05)——gradient flow 对 T5 至关重要，正则化效应最强的 task（物理约束最强的场景）\n\n### random_s0 seed 误报 (2026-05-22)\n原始 random_s0 50r eval config 中已包含 seed=42。之前 Worker 报告\"无 seed\"是检查方法有误（查 /proc/cmdline 而非 config 文件）。rerun 是多余的，已 kill。\n\n### occ_s1 数据不可用 (2026-05-21)\n- mvp_occ_s1 从 17500 resume，数据受 confound 污染，被 D013 排除\n- occ_s1_fresh 替代完成，47500 和 50000 eval 均完成\n\n## 待提交 eval 命令 (2026-05-23)\n\nwestd-34685 上 4 个实验（vanilla_retrain_s0, full_occ_retrain_s0, reverse_cutoff_s0, cutoff_25k_s0）完成后的操作：\n\n- **vanilla_retrain_s0** / **full_occ_retrain_s0**：仅需梯度分析，不需要 eval\n- **reverse_cutoff_s0** / **cutoff_25k_s0**：需要 SafeLIBERO eval\n\n### reverse_cutoff_s0_eval\n\n```bash\nCUDA_VISIBLE_DEVICES=0 MUJOCO_EGL_DEVICE_ID=0 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \\\n  --pretrained_checkpoint /root/autodl-tmp/checkpoints/reverse_cutoff_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n  --num_rollouts 50 --seed 42\n```\n\n- 服务器: westd-34685\n- GPU: 训练完成后任选空闲 GPU，CUDA_VISIBLE_DEVICES 和 MUJOCO_EGL_DEVICE_ID 必须匹配物理 GPU 编号\n- 参考: cutoff_s1_eval 命令格式（同服务器已成功完成）\n- 预计耗时: ~1h（参考 cutoff_s0_eval wall_clock 3427s）\n\n### cutoff_25k_s0_eval\n\n```bash\nCUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py \\\n  --pretrained_checkpoint /root/autodl-tmp/checkpoints/cutoff_25k_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \\\n  --num_rollouts 50 --seed 42\n```\n\n- 服务器: westd-34685\n- GPU: 同上，按物理 GPU 编号匹配\n- 两个 eval 可并行跑在不同 GPU 上\n\n### 注意事项\n- checkpoint 路径中的目录名模式已通过 `ls` 确认（当前 30000_chkpt 已存在，50000_chkpt 待训练完成后生成）\n- conda 环境激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe`\n- 工作目录: `cd /root/occsafe_vla/openvla-oft`\n- 如通过 submit_training_job 提交，conda 和 cwd 由框架自动处理\n\n## 基础设施经验\n\n### 训练命令必须显式指定所有关键参数 (2026-05-23)\n**事故**：cutoff_s2 提交时缺少 `--num_images_in_input 2 --use_proprio True`，使用了脚本默认值（1-image, no-proprio），导致模型架构不同（少 proprio_projector 16.8M 参数），训练速度 2.05 vs 1.07 it/s，结果完全不可比。训练 + eval 均作废。\n**教训**：提交任何训练实验时，必须显式写出以下参数，不依赖脚本默认值：\n```\n--num_images_in_input 2 --use_proprio True --use_l1_regression True\n--batch_size 8 --learning_rate 5e-4 --lora_rank 32 --image_aug True\n```\n**检测方法**：trainable params 总数应为 ~279,977,608（含 proprio_projector）。如果显著偏低，配置有误。训练速度应为 ~1.0-1.1 it/s，如果 >1.5 it/s 说明 input 配置不对。\n\n### westd-34685 磁盘管理教训 (2026-05-22)\n- 350G 数据盘满导致 3 个实验同时崩溃（save_freq=2500 时 checkpoint 积累过快）\n- occ_s1_fresh 残留 149G 是主要元凶\n- 从头重跑时改用 save_freq=10000 减少 checkpoint 数量\n- 教训：提交实验前检查磁盘空间，特别是多实验共用数据盘时\n\n### conda 环境 (2026-05-22)\n- 两台服务器均使用 conda env `occsafe`\n- 激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe`\n- 不要假设 .venv 存在\n"
  }
}
````

</details>

---

### Tool result

_source line 44 · 2026-05-23T15:55:31.624602+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-23T15:55:31.624802+00:00_

两个任务完成。

---

## 任务 1: related_work.tex 质量报告

**引用语义检查 — 全部通过，无需修复。**

逐条验证结果：
- 所有 \cite{} 均放在语义匹配的位置。VLA safety 类引用在 §2.1，spatial VLA 在 §2.2，multi-task/regularization 在 §2.3
- `li2026spatialforcing` 被引用两次（line 33 空间VLA对齐方法 + line 52 辅助 depth-alignment loss），两处上下文不同，合理
- 分组引用语义正确：`{sun2025geovla, tu2026sgvla, li2026corridorvla, pan2026savla}` 均为"3D structure into manipulation VLAs"；`{chen2026gstvla, li2025qdepthvla, bhat20253dcavla}` 均为 depth-based approaches
- 无语法或逻辑错误

**choi2026vlaeval 删除确认：**
- `references.bib` — 已删除 ✅（main.tex line 52 用 `\bibliography{references}` 指向此文件）
- `references.tex` — 仍存在（line 331-337），但该文件**未被任何 tex 文件引用**，不影响编译。可在后续清理时删除

---

## 任务 2: eval 命令已写入 memory.md

已基于 cutoff_s1_eval（同服务器已成功完成）的命令格式，准备了 `reverse_cutoff_s0_eval` 和 `cutoff_25k_s0_eval` 的完整命令。checkpoint 路径模式已通过 SSH `ls` 确认（当前两个实验都已有 30000_chkpt，50000_chkpt 待训练完成后生成）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_verify_bib_and_prep_eval_20260523T154920"
}
```

</details>

---
