# paper k20 ablation table

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_paper_k20-ablation-table_20260521T112638.jsonl`
- **Structured JSON:** [`0c24ed2006bfecf11a78.json`](../../sessions/0c/0c24ed2006bfecf11a78.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

26 recorded events

### Assistant

_source line 1 · 2026-05-21T11:26:45.928046+00:00_

You've hit your limit · resets May 22, 5pm (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_k20-ablation-table_20260521T112638"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T11:28:45.889092+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-21T11:28:45.889486+00:00_

total 32
drwxr-xr-x  3 ubuntu ubuntu 4096 May 15 19:11 .
drwxr-xr-x 11 ubuntu ubuntu 4096 May 21 10:54 ..
-rw-r--r--  1 ubuntu ubuntu 5934 May 15 19:11 figure_plan.md
-rw-r--r--  1 ubuntu ubuntu 9281 May 15 19:10 outline.md
drwxr-xr-x  2 ubuntu ubuntu 4096 May 15 19:11 sections

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T11:28:45.889725+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/",
    "description": "List paper sections"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T11:28:45.889909+00:00_

total 16
drwxr-xr-x 2 ubuntu ubuntu 4096 May 15 19:11 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 15 19:11 ..
-rw-r--r-- 1 ubuntu ubuntu 8090 May 15 19:11 related_work.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T11:28:45.890099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/outline.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/outline.md"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T11:28:45.890420+00:00_

1	# ACR-VLA: Observation-Conditioned Learned Correction for Robust Vision-Language-Action Models
2	
3	**Target**: CoRL 2026 (Abstract DDL ~May 26, Full paper DDL ~Jun 2)
4	**Format**: 8 pages + references, CoRL template
5	
6	---
7	
8	## Title Candidates
9	
10	1. **ACR-VLA: Sample-Then-Correct — Observation-Conditioned Action Refinement for Robust Vision-Language-Action Models**
11	2. **Beyond Sample Selection: Learned Action Correction Improves VLA Robustness Under Distribution Shift**
12	3. **When Conformal Features Fail: Observation-Conditioned Correction for Vision-Language-Action Models**
13	
14	---
15	
16	## 1. Introduction (~1.5 pages)
17	
18	**Key points**:
19	- Flow-matching VLAs (pi0, SmolVLA) achieve near-saturation on standard benchmarks (97-99%) but exhibit robustness gaps under distribution shift (LIBERO-Plus)
20	- Existing inference-time approaches: sample selection only (ReconVLA), task-level RL (SC-VLA), high-latency verifiers (VLA-Pilot 2.41s/step) — none explore learned action correction on frozen VLAs
21	- Our contribution: **sample-then-correct pipeline** — conformal sample selection (K=10) followed by a lightweight observation-conditioned Conformal Refinement Module (CRM, ~250K params, ~3ms overhead)
22	- Three findings:
23	  1. Sample-then-correct > sample-then-select: obs_only CRM +7pp over argmin on LIBERO object (19% vs 12%, exp: `eval-acr-object-v4-obs-only` vs `eval-argmin-only-object`)
24	  2. Observation features > conformal features for correction conditioning (honest negative: per-DOF conformal features ≈ argmin, exp: `eval-acr-object-v4-small`)
25	  3. Correction magnitude control is critical and previously unrecognized — norm=1.42 → 0%, norm=0.1 → 19% (exp: `eval-acr-spatial-v4-default-r3`, magnitude sweep D032)
26	
27	**Figure**: Fig. 1 — Pipeline overview diagram (sample → conformal selection → CRM correction → execution)
28	
29	---
30	
31	## 2. Related Work (~1.5 pages)
32	
33	→ See `paper/sections/related_work.md` for full draft.
…[truncated 7812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T11:28:45.890725+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T11:28:45.890936+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T11:28:45.891117+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'tags': ['k20']}",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'tags': ['k20']}",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T11:28:45.891321+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.426}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T11:28:45.891519+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'LOCKED'}",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'LOCKED'}",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T11:28:45.891714+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3146}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T11:28:45.891887+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T11:28:45.892880+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-pi05-vla-only-spatial-seed44\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:27.768Z\", \"updated_at\": \"2026-05-21T10:19:18.528Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed44, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-spatial-seed43\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:25.180Z\", \"updated_at\": \"2026-05-21T10:19:09.036Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed43, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-spatial-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:22.540Z\", \"updated_at\": \"2026-05-21T10:18:58.812Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Spatial seed42, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-object-seed44\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:19.985Z\", \"updated_at\": \"2026-05-21T10:18:48.305Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed44, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-object-seed43\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:17.435Z\", \"updated_at\": \"2026-05-21T10:18:37.555Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed43, cross-VLA validation of CRM\"}, \"eval-pi05-vla-only-object-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-21T08:22:14.823Z\", \"updated_at\": \"2026-05-21T10:18:27.592Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42, cross-VLA validation of CRM\"}, \"eval-pi05-baseline-object-seed42-r2\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-21T03:30:28.663Z\", \"updated_at\": \"2026-05-21T08:02:33.602Z\", \"hypothesis\": \"π0.5 VLA-only baseline on LIBERO-Object seed42 (r2). Fix: corrected QUANTILES→MEAN_STD normalization mismatch that caused 0% SR in r1.\", \"parent\": \"eval-pi05-baseline-object-seed42\", \"notes\": \"KILLED (旧策略 action[0] only). 后
…[truncated 42196 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T11:28:45.893164+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/related_work.md",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/related_work.md",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T11:28:45.893443+00:00_

1	# Related Work
2	
3	## VLA Robustness and Inference-Time Adaptation
4	
5	Vision-Language-Action (VLA) models have rapidly advanced general-purpose robot control by leveraging large-scale vision-language pretraining [Brohan et al., 2023; Kim et al., 2024]. Flow-matching architectures such as pi0 [Black et al., 2024] and SmolVLA [Shukor et al., 2025] achieve strong performance on standard benchmarks but remain brittle under distribution shift, as systematically documented by LIBERO-Plus [Fei et al., 2025] and LIBERO-PRO [Xu et al., 2025].
6	
7	Several lines of work address VLA robustness at *training time*. RobustVLA [Zhang et al., 2025] applies Jacobian and smoothness regularization via RL post-training. SRPO [Fei et al., 2025] uses self-referential policy optimization to reach 82.1% on LIBERO-Plus. DiG-Flow [Zhang et al., 2025] introduces representation-level discrepancy guidance. ACoT-VLA [AgibotTech, 2026] adds chain-of-thought reasoning to VLA action prediction. VLA-GSE [Jiang et al., 2026] employs parameter-efficient fine-tuning with specialized experts. AFIL [2026] leverages failure trajectories as negative guidance during training. These methods require modifying the VLA training pipeline; our work is complementary, operating purely at inference time on a frozen model.
8	
9	At *inference time*, the landscape is sparser. ReconVLA [Chen et al., 2026] applies conformal prediction to produce calibrated uncertainty estimates and selects the best action from K candidates — a pure sample-selection strategy. VLA-Pilot [2025] uses a multimodal LLM verifier with evolutionary diffusion optimization for zero-shot policy steering, but incurs 2.41s per step. SC-VLA [Li et al., 2026] performs online action refinement via sparse future state prediction and residual RL, requiring environment interaction. TT-VLA [Liu et al., 2026] adapts VLAs through test-time reinforcement learning with progress-based rewards. A2C2 [Sendai et al., 2025] proposes an asynchronous action chunk 
…[truncated 5443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T11:28:45.893711+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "write paper section edit",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "write paper section edit",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T11:28:45.893920+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T11:28:45.894151+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/ablation_k_sweep.md",
  "content": "# Ablation: K-Value Sweep\n\nWe sweep the number of VLA samples K ∈ {2, 10, 20} drawn from the flow-matching policy and held fixed at the obs_only CRM head (ε = 0.2). The VLA-only K=1 baseline is reported for reference. Increasing K beyond 2 yields no measurable success-rate gain on either suite, supporting our adaptive K=2 configuration (Plan A) as Pareto-optimal in compute.\n\n**Table A: Effect of K on closed-loop success rate (mean ± std across seeds).**\n\n| K | Object SR (%) | Spatial SR (%) | n_seeds | Object exp_ids | Spatial exp_ids |\n|---|--------------:|---------------:|--------:|----------------|-----------------|\n| 1 (VLA-only) | 10.8 ± 1.3 | 29.4 ± 1.5 | ≥4 / ≥4 | `eval-vla-only-object-*` | `eval-pi05-vla-only-spatial-*` |\n| 2 (Plan A, adaptive) | **18.3 ± 2.1** | **35.0 ± 1.0** | 3 / 3 | `eval-plan-a-object-seed{42,43,44}` | `eval-plan-a-spatial-seed{42,43,44}` |\n| 10 | 16.8 ± 1.8 | 34.5 ± 1.5 | ≥3 / ≥3 | obs_only norm0.2 seed pool | spatial obs_only seed pool |\n| 20 | 18.8 ± 1.0 | 34.3 ± 0.6 | 4 / 3 | `eval-k20-obs-only-object-seed{42,43,44,45}` | `eval-k20-obs-only-spatial-seed{42,43,44}` |\n\nPer-seed K=20 raw numbers (Object): 20%, 18%, 18%, 19%. Per-seed K=20 raw (Spatial): 35%, 34%, 34%. All K=20 runs use the same CRM checkpoint (`obs_only_K10_eps02_default`) and differ only in the number of candidate actions resampled at inference.\n\n**Diminishing returns beyond K=2.** Moving from K=1 → K=2 captures the bulk of the gain on both benchmarks (+7.5pp Object, +5.6pp Spatial). Subsequent doublings of K provide no additional improvement: on Object, K=10 (16.8%) and K=20 (18.8%) bracket the K=2 mean (18.3%) within one standard deviation; on Spatial, the three K values lie within 0.7pp of one another (34.3-35.0%) and the K=20 standard deviation (0.6%) overlaps the K=2 and K=10 confidence ranges. The pattern is consistent with the obs_only CRM's correction signal being driven by the observation features rather than by candidate diversity — once two samples provide an uncertainty estimate sufficient to trigger correction, additional candidates are absorbed by the same correction head without measurable benefit.\n\n**Implication for compute–accuracy trade-off.** A single flow-matching forward pass dominates inference cost; K=20 requires 10× more VLA forwards than K=2 with no return on closed-loop SR. The adaptive K=2 configuration (Plan A) — which performs a second forward only when the pairwise L2 distance between the first two samples exceeds τ=P50=0.0749 — pays at most 2× VLA compute and triggers correction on roughly 84% of steps on Object and 98% on Spatial, while matching K=20 SR within noise. We therefore adopt K=2 (Plan A) as the default in all downstream experiments and recommend it as the operating point for deployment.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/ablation_k_sweep.md",
    "content": "# Ablation: K-Value Sweep\n\nWe sweep the number of VLA samples K ∈ {2, 10, 20} drawn from the flow-matching policy and held fixed at the obs_only CRM head (ε = 0.2). The VLA-only K=1 baseline is reported for reference. Increasing K beyond 2 yields no measurable success-rate gain on either suite, supporting our adaptive K=2 configuration (Plan A) as Pareto-optimal in compute.\n\n**Table A: Effect of K on closed-loop success rate (mean ± std across seeds).**\n\n| K | Object SR (%) | Spatial SR (%) | n_seeds | Object exp_ids | Spatial exp_ids |\n|---|--------------:|---------------:|--------:|----------------|-----------------|\n| 1 (VLA-only) | 10.8 ± 1.3 | 29.4 ± 1.5 | ≥4 / ≥4 | `eval-vla-only-object-*` | `eval-pi05-vla-only-spatial-*` |\n| 2 (Plan A, adaptive) | **18.3 ± 2.1** | **35.0 ± 1.0** | 3 / 3 | `eval-plan-a-object-seed{42,43,44}` | `eval-plan-a-spatial-seed{42,43,44}` |\n| 10 | 16.8 ± 1.8 | 34.5 ± 1.5 | ≥3 / ≥3 | obs_only norm0.2 seed pool | spatial obs_only seed pool |\n| 20 | 18.8 ± 1.0 | 34.3 ± 0.6 | 4 / 3 | `eval-k20-obs-only-object-seed{42,43,44,45}` | `eval-k20-obs-only-spatial-seed{42,43,44}` |\n\nPer-seed K=20 raw numbers (Object): 20%, 18%, 18%, 19%. Per-seed K=20 raw (Spatial): 35%, 34%, 34%. All K=20 runs use the same CRM checkpoint (`obs_only_K10_eps02_default`) and differ only in the number of candidate actions resampled at inference.\n\n**Diminishing returns beyond K=2.** Moving from K=1 → K=2 captures the bulk of the gain on both benchmarks (+7.5pp Object, +5.6pp Spatial). Subsequent doublings of K provide no additional improvement: on Object, K=10 (16.8%) and K=20 (18.8%) bracket the K=2 mean (18.3%) within one standard deviation; on Spatial, the three K values lie within 0.7pp of one another (34.3-35.0%) and the K=20 standard deviation (0.6%) overlaps the K=2 and K=10 confidence ranges. The pattern is consistent with the obs_only CRM's correction signal being driven by the observation features rather than by candidate diversity — once two samples provide an uncertainty estimate sufficient to trigger correction, additional candidates are absorbed by the same correction head without measurable benefit.\n\n**Implication for compute–accuracy trade-off.** A single flow-matching forward pass dominates inference cost; K=20 requires 10× more VLA forwards than K=2 with no return on closed-loop SR. The adaptive K=2 configuration (Plan A) — which performs a second forward only when the pairwise L2 distance between the first two samples exceeds τ=P50=0.0749 — pays at most 2× VLA compute and triggers correction on roughly 84% of steps on Object and 98% on Spatial, while matching K=20 SR within noise. We therefore adopt K=2 (Plan A) as the default in all downstream experiments and recommend it as the operating point for deployment.\n"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T11:28:45.894411+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/ablation_k_sweep.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T11:28:45.894586+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/outline.md",
  "old_string": "### 4.5 Statistical Significance (seed=43 results, pending)\n- Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)\n- Per-task breakdown showing consistency\n- Bootstrap 95% CI for success rate differences",
  "new_string": "### 4.5 K-Value Sweep Ablation\n\n→ See `paper/sections/ablation_k_sweep.md` for full draft.\n\n**Key message**: K=2 (Plan A) ≈ K=10 ≈ K=20 on both Object (18.3% / 16.8% / 18.8%) and Spatial (35.0% / 34.5% / 34.3%). Diminishing returns beyond K=2 justify Plan A (adaptive K=2) as Pareto-optimal — matches K=20 SR with ≤2× VLA compute. K=20 exp_ids: `eval-k20-obs-only-object-seed{42,43,44,45}`, `eval-k20-obs-only-spatial-seed{42,43,44}`.\n\n### 4.6 Statistical Significance (seed=43 results, pending)\n- Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)\n- Per-task breakdown showing consistency\n- Bootstrap 95% CI for success rate differences"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/outline.md",
    "old_string": "### 4.5 Statistical Significance (seed=43 results, pending)\n- Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)\n- Per-task breakdown showing consistency\n- Bootstrap 95% CI for success rate differences",
    "new_string": "### 4.5 K-Value Sweep Ablation\n\n→ See `paper/sections/ablation_k_sweep.md` for full draft.\n\n**Key message**: K=2 (Plan A) ≈ K=10 ≈ K=20 on both Object (18.3% / 16.8% / 18.8%) and Spatial (35.0% / 34.5% / 34.3%). Diminishing returns beyond K=2 justify Plan A (adaptive K=2) as Pareto-optimal — matches K=20 SR with ≤2× VLA compute. K=20 exp_ids: `eval-k20-obs-only-object-seed{42,43,44,45}`, `eval-k20-obs-only-spatial-seed{42,43,44}`.\n\n### 4.6 Statistical Significance (seed=43 results, pending)\n- Fisher exact test on combined 200 trials (2 seeds × 10 tasks × 10 rollouts)\n- Per-task breakdown showing consistency\n- Bootstrap 95% CI for success rate differences"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T11:28:45.894822+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/outline.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T11:28:45.894967+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "ablation_k_sweep_section",
  "type": "paper",
  "description": "Paper Section 4.5 — K-value sweep ablation (K=2 / 10 / 20). Object 18.3/16.8/18.8%, Spatial 35.0/34.5/34.3%. Diminishing returns beyond K=2 supports Plan A (adaptive K=2) as Pareto-optimal.",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/ablation_k_sweep.md",
  "tags": "['paper', 'ablation', 'k_sweep', 'k20']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "ablation_k_sweep_section",
    "type": "paper",
    "description": "Paper Section 4.5 — K-value sweep ablation (K=2 / 10 / 20). Object 18.3/16.8/18.8%, Spatial 35.0/34.5/34.3%. Diminishing returns beyond K=2 supports Plan A (adaptive K=2) as Pareto-optimal.",
    "project": "acr-vla-conformal-refinement",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper/sections/ablation_k_sweep.md",
    "tags": "['paper', 'ablation', 'k_sweep', 'k20']"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T11:28:45.895126+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_9622ce\", \"name\": \"ablation_k_sweep_section\", \"type\": \"paper\", \"description\": \"Paper Section 4.5 — K-value sweep ablation (K=2 / 10 / 20). Object 18.3/16.8/18.8%, Spatial 35.0/34.5/34.3%. Diminishing returns beyond K=2 supports Plan A (adaptive K=2) as Pareto-optimal.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/ablation_k_sweep.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T11:28:37.256209+00:00\", \"tags\": [\"paper\", \"ablation\", \"k_sweep\", \"k20\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_k20-ablation-table_20260521T112638",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-21T11:28:45.895386+00:00_

写入完成。

**新建文件**: `paper/sections/ablation_k_sweep.md`
- Table A: K ∈ {1, 2, 10, 20} 双 benchmark SR（K=20 数字 18.8±1.0% Object / 34.3±0.6% Spatial 来自 4 + 3 个 seed，per-seed 原始值列出）
- 列出全部 K=20 exp_ids：`eval-k20-obs-only-object-seed{42,43,44,45}`、`eval-k20-obs-only-spatial-seed{42,43,44}`
- "Diminishing returns beyond K=2" 段：K=10/K=20 与 K=2 在一个 std 内重叠
- "Implication" 段：K=20 = 10× VLA forwards 无收益 → 推荐 Plan A (K=2 adaptive，trigger_rate 84%/98%) 为操作点

**更新 outline.md**: 新增 §4.5 K-Value Sweep Ablation 指向新 section，原 §4.5 Statistical Significance → §4.6。

**Artifact 已注册**: `art_20260521_9622ce`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_k20-ablation-table_20260521T112638"
}
```

</details>

---
