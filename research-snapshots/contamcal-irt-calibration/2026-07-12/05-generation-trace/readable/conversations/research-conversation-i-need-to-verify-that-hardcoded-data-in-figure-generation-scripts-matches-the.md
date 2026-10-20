# Research conversation: I need to verify that hardcoded data in figure generation scripts matches the registry/paper values. Check these specifi

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a680f27424e263b05.jsonl`
- **Structured JSON:** [`9c6f562d10476d65bc6c.json`](../../sessions/9c/9c6f562d10476d65bc6c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-25T08:41:42.333Z_

I need to verify that hardcoded data in figure generation scripts matches the registry/paper values. Check these specific scripts for data accuracy:

1. Read `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_cross_benchmark_heatmap.py` — Check the 6x3 delta-acc matrix against these registry values:
   - OLMo-2: MMLU +3.21, ARC +3.92, GSM8K +2.10 (s42, mean s42+s123 for GSM8K)
   - Falcon3: MMLU +4.19, ARC +4.01, GSM8K +1.29
   - Gemma-2: MMLU +3.76, ARC -1.20, GSM8K excluded (CoT collapse)
   - Qwen-7B: MMLU -1.78, ARC -2.90, GSM8K +9.38
   - Phi-4: MMLU -0.17, ARC +0.60, GSM8K -0.50
   - Qwen-14B: MMLU -9.37, ARC -3.40, GSM8K +13.09

2. Read `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_baseline_vulnerability.py` — Check model baselines and deltas match paper Table 1.

3. Read `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci_v3.py` — Check CI values match paper Table 4 cross-seed data:
   - Gemma-2: CI [+1.49, +3.14]
   - Phi-4: CI [-0.17, +1.39]
   - Qwen-14B: CI [-24.99, -10.49]
   - Qwen-7B: CI [-1.82, -0.34]
   - OLMo-2: CI [-0.55, +2.60]
   - Falcon3: range [+3.91, +4.19]

4. Read `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_domain_gamma.py` — Check domain gamma values match paper Table 18 (tab:domain_gamma).

Report any discrepancies between script data and paper values. Be precise about which values mismatch.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "a8ef880a-d66b-46e5-931e-2e20d67d9afd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T08:41:42.337Z_

```json
{
  "parentUuid": "a8ef880a-d66b-46e5-931e-2e20d67d9afd",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "7f9c7ca3-a749-4814-98ad-9d81802a4465",
  "timestamp": "2026-05-25T08:41:42.337Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

---

### Assistant

_source line 3 · 2026-05-25T08:41:44.980Z_



I'll read all four scripts in parallel to check for data accuracy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f9c7ca3-a749-4814-98ad-9d81802a4465",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzKSabSx1ZqNNg84K6k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d182a7d-4d0c-4b13-8d92-1f0105fab16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RZ97AcczY2FkU6VHRcQL4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30631,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30631,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T08:41:45.940Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Un6Xu7vXQ5SdV8afbkR7wY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_cross_benchmark_heatmap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d182a7d-4d0c-4b13-8d92-1f0105fab16c",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzKSabSx1ZqNNg84K6k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "933ff98d-7508-4c4a-bab5-8e4fcae9b54e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RZ97AcczY2FkU6VHRcQL4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30631,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30631,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T08:41:45.948Z_

<details><summary>↩ Tool result · `toolu_01Un6Xu7vXQ5SdV8afbkR7wY`</summary>

```text
1	"""Figure 4: Cross-benchmark transfer heatmap — 6 models x 3 benchmarks."""
2	import sys
3	from pathlib import Path
4	
5	sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent / 'figures' / 'paper'))
6	from paper_style import *
7	
8	apply_style()
9	
10	import matplotlib.pyplot as plt
11	import matplotlib.colors as mcolors
12	import numpy as np
13	
14	# ── Data ─────────────────────────────────────────────────────────────
15	model_names = ['OLMo-2 7B', 'Falcon3 7B', 'Gemma-2 9B',
16	               'Qwen2.5-7B', 'Phi-4 14B', 'Qwen2.5-14B']
17	benchmarks = ['MMLU', 'ARC', 'GSM8K']
18	
19	data = np.array([
20	    [+3.21, +3.92, +2.10],
21	    [+4.19, +4.01, +1.29],
22	    [+3.76, -1.20, +1.33],
23	    [-1.78, -2.90, +9.38],
24	    [-0.17, +0.60, -0.50],
25	    [-9.37, -3.40, +13.09],
26	])
27	
28	# ── Figure ───────────────────────────────────────────────────────────
29	fig, ax = plt.subplots(figsize=figsize_column(aspect=0.54))
30	
31	vmax = 16.5
32	norm = mcolors.TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
33	masked = np.ma.masked_invalid(data)
34	im = ax.imshow(masked, cmap=DIVERGING_CMAP, norm=norm, aspect='auto')
35	
36	# Cell annotations with auto black/white text
37	na_mask = np.isnan(data)
38	for i in range(len(model_names)):
39	    for j in range(len(benchmarks)):
40	        if na_mask[i, j]:
41	            ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1,
42	                         fill=True, facecolor=COLORS['grid'],
43	                         edgecolor=COLORS['separator'], linewidth=0.5, zorder=1))
44	            ax.text(j, i, 'N/A', ha='center', va='center',
45	                    fontsize=8, color=COLORS['nonsignificant'], fontstyle='italic')
46	        else:
47	            val = data[i, j]
48	            rgba = DIVERGING_CMAP(norm(val))
49	            luminance = 0.299 * rgba[0] + 0.587 * rgba[1] + 0.114 * rgba[2]
50	            text_color = 'white' if luminance < 0.55 else COLORS['text']
51	            sign = '+' if val > 0 else ''
52	            ax.text(j, i, f'{sign}{val:.1f}', ha='center', va='center',
53	                    fontsize=10, color=text_color, fontweight='bold')
54	
55	ax.set_xticks(range(len(benchmarks)))
56	ax.set_yticks(range(len(model_names)))
57	ax.set_xticklabels(benchmarks)
58	ax.set_yticklabels(model_names)
59	
60	ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
61	
62	for spine in ax.spines.values():
63	    spine.set_visible(False)
64	
65	# White grid separators
66	ax.set_xticks(np.arange(len(benchmarks)+1)-.5, minor=True)
67	ax.set_yticks(np.arange(len(model_names)+1)-.5, minor=True)
68	ax.grid(which="minor", color="white", linestyle='-', linewidth=2)
69	ax.tick_params(which="minor", bottom=False, left=False)
70	
71	cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04, shrink=0.85)
72	cbar.set_label('$\\Delta$acc (pp)', fontsize=9)
73	cbar.ax.tick_params(labelsize=8)
74	
75	# ── Save ─────────────────────────────────────────────────────────────
76	out = str(Path(__file__).parent / 'fig_cross_benchmark_heatmap')
77	plt.savefig(out + '.pdf', facecolor='white', edgecolor='none')
78	plt.savefig(out + '.png', facecolor='white', edgecolor='none')
79	plt.close()
80	print(f'Saved: {out}.pdf')
81	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "933ff98d-7508-4c4a-bab5-8e4fcae9b54e",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "993e3772-b6e2-487f-8dc3-c0c5f343c5f4",
  "sourceToolAssistantUUID": "933ff98d-7508-4c4a-bab5-8e4fcae9b54e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T08:41:46.420Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JnUYpTouq6JjhsJmdDiKsc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/figures/gen_baseline_vulnerability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "993e3772-b6e2-487f-8dc3-c0c5f343c5f4",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzKSabSx1ZqNNg84K6k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28b68721-0a7d-4b93-93f3-43270d4ebaf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RZ97AcczY2FkU6VHRcQL4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30631,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30631,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-25T08:41:46.427Z_

<details><summary>↩ Tool result · `toolu_01JnUYpTouq6JjhsJmdDiKsc`</summary>

```text
1	"""Figure 3: Baseline-vulnerability scatter — d000 MMLU vs delta-acc@d100."""
2	import sys
3	from pathlib import Path
4	
5	sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent / 'figures' / 'paper'))
6	from paper_style import *
7	
8	apply_style()
9	
10	import matplotlib.pyplot as plt
11	import numpy as np
12	
13	# ── Data ─────────────────────────────────────────────────────────────
14	models = {
15	    'OLMo-2 7B':    (53.79, +3.21, 'Benefit'),
16	    'Falcon3 7B':   (58.77, +4.19, 'Benefit'),
17	    'Gemma-2 9B':   (61.86, +3.76, 'Benefit'),
18	    'Qwen2.5-7B':   (66.11, -1.78, 'V-recovery'),
19	    'Phi-4 14.7B':  (76.44, -0.17, 'Immune'),
20	    'Qwen2.5-14B':  (69.44, -9.37, 'Collapse'),
21	}
22	
23	cross_seed_ranges = {
24	    'OLMo-2 7B':    (-0.55, +3.21),
25	    'Falcon3 7B':   (+3.91, +4.19),
26	    'Gemma-2 9B':   (+1.49, +3.76),
27	    'Qwen2.5-7B':   (-1.78, -0.01),
28	    'Phi-4 14.7B':  (-0.17, +1.83),
29	    'Qwen2.5-14B':  (-25.03, -9.37),
30	}
31	
32	label_offsets = {
33	    'OLMo-2 7B':   (10, -2),
34	    'Falcon3 7B':   (10, 4),
35	    'Gemma-2 9B':   (10, -3),
36	    'Qwen2.5-7B':   (10, 6),
37	    'Phi-4 14.7B':  (-12, 8),
38	    'Qwen2.5-14B':  (10, 5),
39	}
40	
41	# ── Figure ───────────────────────────────────────────────────────────
42	fig, ax = plt.subplots(figsize=figsize_column(aspect=0.58))
43	
44	# Background zones
45	benefit_harm_zones(ax, -27, 7)
46	
47	# Zone labels
48	ax.text(51, 5.5, 'Benefit zone',
49	        fontsize=LABEL['zone_label_fontsize'],
50	        color=COLORS['zone_benefit'],
51	        alpha=LABEL['zone_label_alpha'],
52	        fontstyle='italic', zorder=1)
53	ax.text(51, -11, 'Harm zone',
54	        fontsize=LABEL['zone_label_fontsize'],
55	        color=COLORS['zone_harm'],
56	        alpha=LABEL['zone_label_alpha'],
57	        fontstyle='italic', zorder=1)
58	
59	# Zero line
60	zero_line(ax, direction='h')
61	
62	# Threshold band
63	ax.axvspan(61.86, 66.11, color=COLORS['zone_threshold'], alpha=0.25, zorder=1)
64	ax.annotate('threshold\nregion', xy=(64.0, -11.5), fontsize=6.5,
65	            color=COLORS['annotation'], ha='center', fontstyle='italic', zorder=2)
66	
67	# Error bars (cross-seed range)
68	ylim_lo, ylim_hi = -13, 7
69	for name, (x, y, pattern) in models.items():
70	    lo, hi = cross_seed_ranges[name]
71	    color = get_pattern_color(pattern)
72	    clipped_lo = max(lo, ylim_lo + 0.3)
73	    ax.plot([x, x], [clipped_lo, hi], color=color, linewidth=1.2,
74	            alpha=ALPHA['error_bar'], zorder=3)
75	    if lo < ylim_lo:
76	        ax.annotate('', xy=(x, ylim_lo + 0.15), xytext=(x, ylim_lo + 1.2),
77	                     arrowprops=dict(arrowstyle='->', color=color, lw=1.0,
78	                                     alpha=ALPHA['error_bar'] + 0.1),
79	                     zorder=3)
80	    else:
81	        ax.plot([x-0.4, x+0.4], [lo, lo], color=color, linewidth=0.8,
82	                alpha=ALPHA['error_bar'], zorder=3)
83	    ax.plot([x-0.4, x+0.4], [hi, hi], color=color, linewidth=0.8,
84	            alpha=ALPHA['error_bar'], zorder=3)
85	
86	# Scatter points
87	for name, (x, y, pattern) in models.items():
88	    color = get_pattern_color(pattern)
89	    marker = MARKERS.get(pattern, 'o')
90	    ax.scatter(x, y, c=color, marker=marker,
91	               s=SCATTER['size'], zorder=SCATTER['zorder'],
92	               edgecolors=SCATTER['edgecolor'],
93	               linewidths=SCATTER['linewidth'])
94	
95	    ox, oy = label_offsets[name]
96	    ha = 'right' if ox < 0 else 'left'
97	    ax.annotate(name, (x, y), xytext=(ox, oy),
98	                textcoords='offset points',
99	                fontsize=LABEL['inline_fontsize'],
100	                fontweight=LABEL['inline_fontweight'],
101	                color=COLORS['text'], ha=ha, va='center', zorder=6)
102	
103	ax.set_xlabel('Baseline MMLU Accuracy (%)')
104	ax.set_ylabel('$\\Delta$acc @ d100 (pp)')
105	ax.set_xlim(50, 80)
106	ax.set_ylim(ylim_lo, ylim_hi)
107	
108	# Legend
109	pattern_legend(ax, patterns=['Benefit', 'Immune', 'V-recovery', 'Collapse'],
110	               loc='upper right')
111	
112	plt.tight_layout()
113	
114	# ── Save ─────────────────────────────────────────────────────────────
115	out = str(Path(__file__).parent / 'fig_baseline_vulnerability')
116	plt.savefig(out + '.pdf', facecolor='white', edgecolor='none')
117	plt.savefig(out + '.png', facecolor='white', edgecolor='none')
118	plt.close()
119	print(f'Saved: {out}.pdf')
120	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28b68721-0a7d-4b93-93f3-43270d4ebaf1",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "48240a26-c1ef-42dc-a7d2-7027a0f41463",
  "sourceToolAssistantUUID": "28b68721-0a7d-4b93-93f3-43270d4ebaf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T08:41:46.885Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MDAszFiEc72nEn9A1PKzWn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_cross_seed_ci_v3.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48240a26-c1ef-42dc-a7d2-7027a0f41463",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzKSabSx1ZqNNg84K6k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3404fb16-c9c2-4d51-830d-44c60cc1d8a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RZ97AcczY2FkU6VHRcQL4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30631,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30631,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T08:41:46.890Z_

<details><summary>↩ Tool result · `toolu_01MDAszFiEc72nEn9A1PKzWn`</summary>

```text
1	#!/usr/bin/env python3
2	"""Figure 5: Cross-seed CI forest plot — unified paper style."""
3	import sys
4	from pathlib import Path
5	
6	sys.path.insert(0, str(Path(__file__).parent))
7	from paper_style import *
8	
9	apply_style()
10	
11	import matplotlib.pyplot as plt
12	import numpy as np
13	
14	# ── Data ─────────────────────────────────────────────────────────────
15	families = [
16	    ('Qwen2.5-14B',  'Collapse',   -15.7,  -24.99, -10.49, True),
17	    ('Qwen2.5-7B',   'V-recovery', -1.1,   -1.82,  -0.34,  True),
18	    ('Phi-4 14.7B',  'Immune',     +0.73,  -0.17,  +1.39,  False),
19	    ('OLMo-2 7B',    'Benefit',    +1.0,   -0.55,  +2.60,  False),
20	    ('Gemma-2 9B',   'Benefit',    +2.4,   +1.49,  +3.14,  True),
21	    ('Falcon3-7B',   'Benefit',    +4.1,   +3.91,  +4.19,  True),
22	]
23	
24	# ── Figure ───────────────────────────────────────────────────────────
25	fig, ax = plt.subplots(figsize=figsize_column(aspect=0.54))
26	
27	n = len(families)
28	y_positions = np.arange(n)[::-1]
29	
30	x_left = -27
31	x_right = 5.5
32	
33	# Background sections
34	ax.axhspan(3.5, 6.1, color=COLORS['zone_harm'],
35	           alpha=ALPHA['zone'], zorder=0)
36	ax.axhspan(-0.7, 2.5, color=COLORS['zone_benefit'],
37	           alpha=ALPHA['zone'], zorder=0)
38	
39	# Separator lines
40	ax.axhline(y=3.5, color=FOREST['separator_color'],
41	           linewidth=FOREST['separator_linewidth'], linestyle='-', zorder=1)
42	ax.axhline(y=2.5, color=FOREST['separator_color'],
43	           linewidth=FOREST['separator_linewidth'], linestyle='-', zorder=1)
44	
45	# Zero reference line
46	zero_line(ax, direction='v')
47	
48	# CI bars + markers
49	for i, (name, pattern, mean, ci_lo, ci_hi, sig) in enumerate(families):
50	    y = y_positions[i]
51	    col = get_pattern_color(pattern)
52	
53	    ax.hlines(y, ci_lo, ci_hi, color=col,
54	              linewidth=FOREST['ci_linewidth'], zorder=2, capstyle='butt')
55	
56	    ci_width = ci_hi - ci_lo
57	    cap_h = FOREST['cap_height'] if ci_width > 2.0 else FOREST['cap_height'] * 0.67
58	    ax.vlines(ci_lo, y - cap_h, y + cap_h, color=col,
59	              linewidth=FOREST['cap_linewidth'], zorder=2)
60	    ax.vlines(ci_hi, y - cap_h, y + cap_h, color=col,
61	              linewidth=FOREST['cap_linewidth'], zorder=2)
62	
63	    if sig:
64	        ax.plot(mean, y, 'o', color=col,
65	                markersize=FOREST['marker_size'], zorder=3,
66	                markeredgecolor=FOREST['marker_edgecolor'],
67	                markeredgewidth=FOREST['marker_edgewidth'])
68	    else:
69	        ax.plot(mean, y, 'o', color='white',
70	                markersize=FOREST['marker_size'], zorder=3,
71	                markeredgecolor=col, markeredgewidth=2.0)
72	
73	    sign_char = '+' if mean > 0 else ''
74	    label = f"{sign_char}{mean:.1f} pp"
75	    ax.annotate(label, xy=(1.03, y), xycoords=('axes fraction', 'data'),
76	                va='center', ha='left', fontsize=9, color=col,
77	                fontweight='medium', annotation_clip=False)
78	
79	# Falcon3 n=2 sub-annotation
80	falcon_y = y_positions[5]
81	ax.annotate('n = 2', xy=(1.03, falcon_y - 0.40),
82	            xycoords=('axes fraction', 'data'),
83	            va='center', ha='left',
84	            fontsize=LABEL['inline_fontsize'],
85	            color=COLORS['Benefit'], fontstyle='italic',
86	            alpha=0.55, annotation_clip=False)
87	
88	# Section labels
89	label_x = x_left + 0.8
90	ax.text(label_x, 5.88, 'Harm',
91	        fontsize=LABEL['section_fontsize'],
92	        color=COLORS['Collapse'],
93	        fontweight=LABEL['section_fontweight'],
94	        va='top', ha='left', alpha=LABEL['section_alpha'])
95	ax.text(label_x, 2.38, 'Benefit',
96	        fontsize=LABEL['section_fontsize'],
97	        color=COLORS['Benefit'],
98	        fontweight=LABEL['section_fontweight'],
99	        va='top', ha='left', alpha=LABEL['section_alpha'])
100	
101	ax.set_yticks(y_positions)
102	ax.set_yticklabels([f[0] for f in families], fontsize=10.5)
103	
104	ax.set_xlabel(r'Cross-seed mean $\Delta$acc at $d_{100}$ (pp)')
105	ax.set_xlim(x_left, x_right)
106	ax.set_ylim(-0.7, 6.1)
107	ax.grid(False)
108	ax.set_xticks([-25, -20, -15, -10, -5, 0, 5])
109	
110	plt.subplots_adjust(right=0.81, top=0.97, bottom=0.15, left=0.18)
111	
112	# ── Save ─────────────────────────────────────────────────────────────
113	out_dir = Path(__file__).parent
114	paper_dir = Path(__file__).resolve().parent.parent.parent / 'docs' / 'paper' / 'figures'
115	for d in [out_dir, paper_dir]:
116	    fig.savefig(d / 'fig_cross_seed_ci.pdf', format='pdf')
117	    fig.savefig(d / 'fig_cross_seed_ci.png', format='png')
118	plt.close()
119	print("Saved fig_cross_seed_ci.pdf/png")
120	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3404fb16-c9c2-4d51-830d-44c60cc1d8a4",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "33d32851-ea06-4740-a868-1abe6e20a1dd",
  "sourceToolAssistantUUID": "3404fb16-c9c2-4d51-830d-44c60cc1d8a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T08:41:47.384Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VpqArE5cDeTf1F1GLEtp4q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/figures/paper/gen_fig_domain_gamma.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33d32851-ea06-4740-a868-1abe6e20a1dd",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzKSabSx1ZqNNg84K6k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5259f8f-36f8-464d-8f51-9902bffd15ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RZ97AcczY2FkU6VHRcQL4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30631,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 30631,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T08:41:47.396Z_

<details><summary>↩ Tool result · `toolu_01VpqArE5cDeTf1F1GLEtp4q`</summary>

```text
1	"""Figure 6: Per-domain gamma forest plot with pooled estimate."""
2	import sys
3	from pathlib import Path
4	
5	sys.path.insert(0, str(Path(__file__).parent))
6	from paper_style import *
7	
8	apply_style()
9	
10	import matplotlib.pyplot as plt
11	import numpy as np
12	from matplotlib.lines import Line2D
13	
14	# ── Data: J=13 Qwen2.5 (8x1.5B + 5x3B) ─────────────────────────────
15	domains = ['STEM: Math', 'STEM: Science', 'STEM: CS/Eng',
16	           'Business/Law', 'Medical', 'Humanities', 'Social Sci.']
17	gamma_mean = [0.499, 0.504, 0.497, 0.044, 0.235, -0.309, -0.571]
18	ci_lower   = [-0.213, -0.189, -0.425, -0.497, -0.421, -0.852, -1.054]
19	ci_upper   = [1.203, 1.202, 1.397, 0.579, 0.879, 0.257, -0.103]
20	ppp        = [0.206, 0.149, 0.392, 0.299, 0.124, 0.530, 0.570]
21	
22	significant = [False, False, False, False, False, False, True]
23	
24	# Pooled J=13
25	pooled_gamma = 0.107
26	pooled_ci = [-0.401, 0.625]
27	
28	# ── Figure ───────────────────────────────────────────────────────────
29	fig, ax = plt.subplots(figsize=figsize_column(aspect=0.62))
30	
31	y_positions = np.arange(len(domains))[::-1]
32	
33	# Background: STEM vs non-STEM
34	ax.axhspan(3.5, 7.5, color=COLORS['zone_benefit'],
35	           alpha=ALPHA['zone'], zorder=0)
36	ax.axhspan(-0.5, 3.5, color=COLORS['zone_harm'],
37	           alpha=ALPHA['zone'], zorder=0)
38	
39	# Zero reference line
40	zero_line(ax, direction='v')
41	
42	# Domain-level estimates
43	for i, (y, gm, cl, cu, sig) in enumerate(
44	        zip(y_positions, gamma_mean, ci_lower, ci_upper, significant)):
45	    if sig:
46	        col = COLORS['positive_gamma'] if gm > 0 else COLORS['negative_gamma']
47	    else:
48	        col = COLORS['nonsignificant']
49	
50	    ax.hlines(y, cl, cu, color=col,
51	              linewidth=FOREST['ci_linewidth'], zorder=2)
52	
53	    if sig:
54	        ax.plot(gm, y, 'o', color=col,
55	                markersize=FOREST['marker_size'], zorder=3,
56	                markeredgecolor=FOREST['marker_edgecolor'],
57	                markeredgewidth=FOREST['marker_edgewidth'])
58	    else:
59	        ax.plot(gm, y, 'o', color='white',
60	                markersize=FOREST['marker_size'], zorder=3,
61	                markeredgecolor=col, markeredgewidth=2.0)
62	
63	    ppp_text = f"PPP={ppp[i]:.2f}"
64	    ax.text(1.55, y, ppp_text, va='center', ha='left',
65	            fontsize=LABEL['annotation_fontsize'],
66	            color=col, fontweight='medium')
67	
68	# Pooled bar — diamond marker, gray
69	pooled_y = -1.3
70	ax.hlines(pooled_y, pooled_ci[0], pooled_ci[1],
71	          color=COLORS['pooled'], linewidth=2.0, linestyle='-', zorder=2)
72	ax.plot(pooled_gamma, pooled_y, 'D', color=COLORS['pooled'],
73	        markersize=8, zorder=3,
74	        markeredgecolor=FOREST['marker_edgecolor'],
75	        markeredgewidth=FOREST['marker_edgewidth'])
76	
77	# Separator
78	ax.axhline(y=-0.5, color=FOREST['separator_color'],
79	           linewidth=FOREST['separator_linewidth'], linestyle='-')
80	
81	# Y-axis
82	ax.set_yticks(list(y_positions) + [pooled_y])
83	ax.set_yticklabels(domains + ['Pooled MMLU'], fontsize=10.5)
84	ytick_labels = ax.get_yticklabels()
85	ytick_labels[-1].set_fontstyle('italic')
86	ytick_labels[-1].set_color(COLORS['pooled'])
87	
88	# Group labels
89	ax.text(-1.05, 6.85, 'STEM',
90	        fontsize=LABEL['section_fontsize'],
91	        color=COLORS['positive_gamma'],
92	        fontweight=LABEL['section_fontweight'],
93	        va='top', ha='left', alpha=LABEL['section_alpha'])
94	ax.text(-1.05, 2.15, 'Non-STEM',
95	        fontsize=LABEL['section_fontsize'],
96	        color=COLORS['negative_gamma'],
97	        fontweight=LABEL['section_fontweight'],
98	        va='bottom', ha='left', alpha=LABEL['section_alpha'])
99	
100	# Pooled annotation
101	ax.text(pooled_ci[1] + 0.12, pooled_y, 'n.s. — dilution masking',
102	        va='center', ha='left', fontsize=8.5,
103	        color=COLORS['pooled'], fontstyle='italic')
104	
105	ax.set_xlabel(r'Contamination effect ($\gamma$)')
106	ax.set_xlim(-1.2, 1.8)
107	ax.set_ylim(-2.0, 7.2)
108	
109	# Legend
110	legend_elements = [
111	    Line2D([0], [0], marker='o', color='w',
112	           markerfacecolor=COLORS['negative_gamma'], markersize=9,
113	           markeredgecolor='white', markeredgewidth=0.5,
114	           label='CI excludes zero'),
115	    Line2D([0], [0], marker='o', color='w',
116	           markerfacecolor=COLORS['nonsignificant'], markersize=9,
117	           markeredgecolor='white', markeredgewidth=0.5,
118	           label='Non-significant'),
119	]
120	ax.legend(handles=legend_elements, loc='upper center', framealpha=0.92,
121	          edgecolor='#DDDDDD', bbox_to_anchor=(0.45, 1.08), ncol=2,
122	          columnspacing=1.0, handletextpad=0.3)
123	
124	ax.xaxis.grid(True)
125	plt.tight_layout()
126	
127	# ── Save ─────────────────────────────────────────────────────────────
128	out_dir = Path(__file__).parent
129	paper_dir = Path(__file__).resolve().parent.parent.parent / 'docs' / 'paper' / 'figures'
130	for d in [out_dir, paper_dir]:
131	    fig.savefig(d / 'fig_domain_gamma.pdf', format='pdf')
132	    fig.savefig(d / 'fig_domain_gamma.png', format='png')
133	plt.close()
134	print("Saved fig_domain_gamma.pdf/png")
135	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5259f8f-36f8-464d-8f51-9902bffd15ae",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "6673eb5c-2f61-4e08-936f-a122401d7c6f",
  "sourceToolAssistantUUID": "e5259f8f-36f8-464d-8f51-9902bffd15ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-25T08:41:51.464Z_

Now let me check the paper tables to cross-reference the values. Let me look for the paper content with Table 1, Table 4, and Table 18 data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6673eb5c-2f61-4e08-936f-a122401d7c6f",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzKpsXvVe36nsVagC1c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3f25f5b-8b8f-4741-895d-866a6efe8c2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbZHFzVsbDn8rTA1tYyxun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8663,
      "cache_read_input_tokens": 30631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8663,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T08:41:53.491Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Engrh69hesJZ4UxZP12XPs`</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3f25f5b-8b8f-4741-895d-866a6efe8c2c",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzKpsXvVe36nsVagC1c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dca988a1-2784-43dc-bec4-30e8ab1f4723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbZHFzVsbDn8rTA1tYyxun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8663,
      "cache_read_input_tokens": 30631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8663,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T08:41:53.558Z_

<details><summary>↩ Tool result · `toolu_01Engrh69hesJZ4UxZP12XPs`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/paper/fisher_info_appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/paper/related_work_04a735.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/paper/algorithm1_pseudocode.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/_project/paper/algorithm1_pseudocode_c1bd81.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dca988a1-2784-43dc-bec4-30e8ab1f4723",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "78c8f0bc-519e-48d1-addb-dffdb3d552b0",
  "sourceToolAssistantUUID": "dca988a1-2784-43dc-bec4-30e8ab1f4723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T08:41:54.011Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KME9hoguuxwG3jh9nrFDqB`</summary>

```json
{
  "pattern": "**/paper/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78c8f0bc-519e-48d1-addb-dffdb3d552b0",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzKpsXvVe36nsVagC1c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60535a95-0fe9-4f41-a441-2196c23aa9a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbZHFzVsbDn8rTA1tYyxun",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8663,
      "cache_read_input_tokens": 30631,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8663
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 30631,
          "cache_creation_input_tokens": 8663,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8663,
            "ephemeral_1h_input_tokens": 0
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

_source line 16 · 2026-05-25T08:41:54.026Z_

<details><summary>↩ Tool result · `toolu_01KME9hoguuxwG3jh9nrFDqB`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60535a95-0fe9-4f41-a441-2196c23aa9a2",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "43215110-9441-445a-8e0a-e453af30455d",
  "sourceToolAssistantUUID": "60535a95-0fe9-4f41-a441-2196c23aa9a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T08:41:59.733Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MiVqfCXHP6JsEyiTK6YiBk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43215110-9441-445a-8e0a-e453af30455d",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzLUEb1ijBxcGidRzZK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1856f1ff-c43b-47cd-a407-51d196c3e810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKVXjumewU7eoY23oyqDdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1144,
      "cache_read_input_tokens": 39294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1144,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T08:41:59.740Z_

<details><summary>↩ Tool result · `toolu_01MiVqfCXHP6JsEyiTK6YiBk`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=0.88\columnwidth]{figures/fig_cross_benchmark_heatmap.pdf}
7	\caption{Cross-benchmark transfer at d100. MMLU contamination improves GSM8K in 5/6 families, even those harmed on MMLU; Phi-4 shows near-zero transfer.}
8	\label{fig:cross_benchmark_heatmap}
9	\end{figure}
10	
11	Cross-family SFT-injection results (\S\ref{sec:taxonomy}) use seed$=$42 data across six models from five independent families ($\leq$3B dose-response in Appendix~\ref{sec:dose_response_details}). Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
12	
13	\subsection{Dose-Response Patterns}
14	\label{sec:taxonomy}
15	
16	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields a spectrum of dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. Figure~\ref{fig:baseline_vulnerability} visualizes how contamination response correlates with baseline accuracy across families.
17	
18	\paragraph{Replication status.}
19	Two patterns replicate across independent families (Table~\ref{tab:taxonomy}). \textit{Immune}: Phi-4 ($\pm$0.5pp), confirmed out-of-sample by LLaMA-3.1 ($-$0.69pp). \textit{Benefit}: three families gain $+$3.2 to $+$4.2pp (Gemma-2, Falcon3, OLMo-2 borderline; \S\ref{sec:cross_seed}). Two patterns are Qwen2.5-specific and await independent replication: Qwen-14B \textit{collapses} ($-$9.4 to $-$25.0pp across seeds) while Qwen-7B shows \textit{V-recovery}. ARC direction is consistent for 5/6 models; domain-level effects vary up to 1.8$\times$ (Appendices~\ref{sec:arc_cross_benchmark},~\ref{sec:domain_decomposition}).
20	
21	\paragraph{Out-of-sample~validation.}
22	LLaMA-3.1-8B (Meta; d000, d025, d100) is classified Immune on both MMLU ($-$0.69pp) and ARC ($+$0.09pp), despite matching OLMo-2's Benefit baseline (53.5\% vs.\ 53.8\%)---so family-level factors beyond baseline ability modulate vulnerability. LLaMA-3.1 also shows the strongest GSM8K transfer ($+$16.4pp; Appendix~\ref{sec:gsm8k_dose_response}): target-benchmark immunity does not imply transfer immunity.
23	
24	\subsection{Cross-Benchmark Transfer}
25	\label{sec:gsm8k_transfer}
26	
27	\begin{table}[t]
28	\centering
29	\caption{Cross-benchmark transfer: MMLU vs.\ GSM8K accuracy change at d100. LLaMA-3.1 shows the strongest asymmetric transfer ($+$16.4pp GSM8K despite MMLU immunity). Gemma-2 excluded due to CoT collapse under MC-format SFT.}
30	\label{tab:gsm8k_transfer}
31	\footnotesize
32	\resizebox{\columnwidth}{!}{%
33	\begin{tabular}{lcccl}
34	\toprule
35	Model & MMLU $\Delta$ & GSM8K $\Delta$ & Range & Transfer \\
36	\midrule
37	Phi-4 14.7B & $\pm$0.5pp & $-$0.5pp$^{\diamond}$ & --- & Null \\
38	OLMo-2 7B & $+$3.2pp & $+$2.1pp$^{\S}$ & --- & Consistent \\
39	Falcon3 7B & $+$4.2pp & $+$1.3pp & --- & Consistent \\
40	Qwen-7B & $-$1.8pp & $+$9.4pp & $\pm$0.9 & Reversal \\
41	Qwen-14B & $-$9.4pp & $+$13.1pp & $\pm$7.4 & Reversal$^{\dagger}$ \\
42	LLaMA-3.1 8B & $-$0.7pp & $+$16.4pp$^{\ddagger}$ & --- & Asymmetric \\
43	\bottomrule
44	\multicolumn{5}{l}{\scriptsize $^{\dagger}$d000 baseline seed-sensitive (s42$=$60.8\% vs.\ s123$=$76.7\%); d100 stable ($82\pm0.5$\%).} \\
45	\multicolumn{5}{l}{\scriptsize $^{\S}$Mean of s42 and s123: $+$2.1pp (s42: $+$1.7pp, s123: $+$2.4pp); s0 excluded ($+$9.2pp outlier).} \\
46	\multicolumn{5}{l}{\scriptsize $^{\ddagger}$Single seed (s0); MMLU Immune but strongest GSM8K transfer across all families.} \\
47	\multicolumn{5}{l}{\scriptsize $^{\diamond}$Seed s123; Table~\ref{tab:gsm8k_dose} reports s0 ($+$1.14pp).}
48	\end{tabular}}
49	\end{table}
50	
51	Contamination patterns are a property of the (model, benchmark) pair, not the model alone. Within-MC direction agreement is 86\% (6/7 families; Appendix~\ref{sec:arc_cross_benchmark}); across formats (MC$\to$generative math), agreement drops to 50\% with three families reversing on GSM8K \citep{cobbe2021gsm8k} (Table~\ref{tab:gsm8k_transfer}). Qwen-14B ($-$9.4pp MMLU) gains $+$13.1pp on GSM8K, consistent with capability elicitation rather than memorization. Volume effects are ruled out: d005 ($+$1.5\% data) already yields $+$6.4pp GSM8K transfer for Qwen-7B.
52	
53	\subsection{Cross-Seed Stability}
54	\label{sec:cross_seed}
55	
56	\begin{figure}[t]
57	\centering
58	\includegraphics[width=\columnwidth]{figures/fig_cross_seed_ci.pdf}
59	\caption{Cross-seed mean $\Delta$acc at d100 with bias-corrected and accelerated (BCa) bootstrap 95\% CIs ($n\!=\!3$ seeds; Falcon3 $n\!=\!2$). Filled markers: CI excludes zero.}
60	\label{fig:cross_seed_ci}
61	\end{figure}
62	
63	Gemma-2 is the only family with a statistically significant cross-seed Benefit (BCa 95\% CI $[+1.49, +3.14]$; Figure~\ref{fig:cross_seed_ci}); Falcon3 and OLMo-2 are directionally consistent but exploratory (Table~\ref{tab:cross_seed}). Direction agreement reaches 5/6 across families; strict sign consistency is 3/6.
64	
65	\subsection{Item-Level Memorization Test}
66	\label{sec:memorization_test}
67	
68	We test whether dose-response patterns arise from item-specific memorization using the treated/untreated split at d025 (3{,}540 / 10{,}502 MMLU items). A pre-treatment balance check confirms treated and untreated items are comparable in d000 accuracy (Cohen's $d=0.02$), difficulty distribution, and domain coverage (all $p>0.19$), supporting the parallel trends assumption. No model shows a significant difference-in-differences (DiD) effect ($p > 0.05$; Table~\ref{tab:did}), ruling out item-specific effects $>$2pp (MDES 1.25--2.05pp; ARC MDES in Appendix~\ref{sec:mdes}). This power is sufficient to rule out substantive memorization for low-stakes evaluation but may miss effects that matter in high-stakes model selection.
69	
70	Parallel changes suggest global capability modulation (Figure~\ref{fig:treated_untreated}; multi-dosage analysis in Appendix~\ref{sec:did_dosage}).
71	
72	\paragraph{Volume control.}
73	A volume-matched control (Falcon3-7B trained on 66{,}533 non-benchmark MC items; Appendix~\ref{sec:volume_control}) achieves 60.67\% MMLU, decomposing the $+$4.19pp Benefit into data quantity ($+$1.90pp, 45\%) and contamination content ($+$2.29pp, 55\%); ARC yields a consistent 43\%/57\% split; GSM8K shows 53\%/47\% ($+$0.68pp/$+$0.61pp of $+$1.29pp total). Collapse ($-$9.4pp) and Immune ($<$1pp) cannot arise from volume effects that produce $+$1.90pp in the control.
74	
75	\begin{table}[t]
76	\centering
77	\caption{Cross-seed $\Delta$acc (d000$\to$d100). Strict sign consistency (Cons.) is 3/6; classification-level direction agreement is 5/6 (see text). Per-seed shape classification\textsuperscript{$\ddagger$} agrees for only 3/6.}
78	\label{tab:cross_seed}
79	\footnotesize
80	\resizebox{\columnwidth}{!}{%
81	\begin{tabular}{lcccccccl}
82	\toprule
83	Model & $n$ & s42 & s123 & s0 & 95\% CI & Dir. & Cons.\ & Pattern\textsuperscript{$\ddagger$} \\
84	\midrule
85	Phi-4 & 3 & 0 & $+$ & 0 & [$-$0.17, $+$1.39]\textsuperscript{B} & Immune & $\times$ & --- \\
86	Qwen-14B & 3 & $-$ & $-$ & $-$ & [$-$24.99, $-$10.49]\textsuperscript{B} & Harm & \checkmark & Collapse \\
87	Qwen-7B & 3 & $-$ & 0 & $-$ & [$-$1.82, $-$0.34]\textsuperscript{B} & Harm & $\times$ & V-recovery \\
88	Gemma-2 & 3 & $+$ & $+$ & $+$ & [$+$1.49, $+$3.14]\textsuperscript{B} & Benefit & \checkmark & Benefit \\
89	OLMo-2 & 3 & $+$ & 0 & $+$ & [$-$0.55, $+$2.60]\textsuperscript{B} & Borderl.\ & $\times$ & ---\textsuperscript{b} \\
90	Falcon3-7B & 2 & $+$ & $+$ & --- & [$+$3.91, $+$4.19]\textsuperscript{c} & Benefit & \checkmark & Benefit \\
91	\bottomrule
92	\multicolumn{9}{l}{\scriptsize \textsuperscript{B}BCa bootstrap ($B\!=\!10{,}000$); original five families at $n\!=\!3$.} \\
93	\multicolumn{9}{l}{\scriptsize \textsuperscript{$\ddagger$}Per-seed shape may differ from family-level direction-based classification (\S\ref{sec:classification}).} \\
94	\multicolumn{9}{l}{\scriptsize \textsuperscript{b}$+$/0/$+$ across seeds. Signs: $+$/$-$ = $|\Delta|{\ge}1$pp; $0$ = $|\Delta|{<}1$pp.} \\
95	\multicolumn{9}{l}{\scriptsize \textsuperscript{c}$n\!=\!2$ seeds only; range shown instead of BCa CI.}
96	\end{tabular}}
97	\end{table}
98	
99	\subsection{Diagnostic Utility}
100	\label{sec:calibration_results}
101	
102	Within-family IRT analysis uses Qwen2.5 $\leq$3B ($J=16$; ability separation in Appendix~\ref{sec:theta_separation}), where aggregate contamination shifts accuracy by ${\sim}$0.6--0.7pp. IRT is fitted on 300 randomly subsampled items (2.1\% of MMLU; representative by KS/$\chi^2$ tests, all $p > 0.5$); RRF exposure scoring achieves $\tau = 0.73$ ($\Delta\tau = 0.18$ vs.\ random; ablation in Appendix~\ref{sec:rrf_ablation}). A single-signal (Min-K\%++) pipeline shows severe model misfit (PPP $< 0.001$ vs.\ $0.193$; Appendix~\ref{sec:s2_only_pipeline}), confirming multi-signal fusion is essential.
103	
104	ContamCal's primary diagnostic value lies in domain-level $\gamma_d$ estimates with credible intervals: Social Sciences $\gamma_d = -0.63$ ($P(\gamma_d\!<\!0) = 99.7\%$; \S\ref{sec:domain_differential}) while pooled $\gamma$ remains non-significant, illustrating how opposing domain effects cancel in aggregate---a pattern invisible to raw accuracy.
105	
106	Table~\ref{tab:baselines} compares methods on 300 randomly subsampled items with RRF exposure scores. Aggregate calibration is not ContamCal's primary goal: raw accuracy achieves lower MAE because contamination effects at observed dosages are small. B6-DCR systematically overcorrects (MAE 0.108). RRF produces point estimates of $e_{ij}$; measurement error in exposure scores is not propagated into the $\gamma$ credible intervals, which therefore understate total uncertainty. Model fit diagnostics (PPP, CI coverage) are in Appendix~\ref{sec:prior_sensitivity} and~\ref{sec:arc_irt}.
107	
108	\subsection{Detection Signal Failure Modes}
109	\label{sec:signal_failure}
110	
111	Min-K\%++ \citep{zhang_2024_minkpp} exhibits \textit{directional reversal} at 0.5B: contaminated items receive \textit{lower} scores (paired Cohen's $d = -1.98$ at d100, $|d| > 1.2$ at d005). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\ref{sec:signal_reliability_appendix}). Simulation shows $\gamma$ recovery requires AUC$\geq$0.55 with $J \geq 50$; at AUC $\geq 0.90$, $J = 16$ suffices (Appendix~\ref{sec:identifiability_appendix}).
112	
113	\subsection{Domain-Level Analysis}
114	\label{sec:domain_differential}
115	
116	\begin{figure}[t]
117	\centering
118	\includegraphics[width=\columnwidth]{figures/fig_domain_gamma.pdf}
119	\caption{Per-domain $\gamma_d$ estimates with 95\% CIs ($J$=13 Qwen2.5; $J$=16 estimates differ by $<$10\%, Table~\ref{tab:domain_gamma}).}
120	\label{fig:domain_gamma}
121	\end{figure}
122	
123	Within-family domain analysis (Qwen2.5, $J=16$) reveals directional heterogeneity masked by aggregate scores: STEM domains show positive $\gamma_d$ while Social Sciences is negative ($\gamma_d = -0.63$, 95\% Bayesian credible interval $[-1.07, -0.19]$, $P(\gamma_d\!<\!0) = 99.7\%$, PPP$=$0.722; Figure~\ref{fig:domain_gamma}, Table~\ref{tab:domain_gamma} in Appendix). Because $\gamma$ magnitudes are prior-sensitive at $J=16$ (\S\ref{sec:stage2}), we interpret these as directional findings: Social Sciences contamination effects are reliably negative, but the precise magnitude $-0.63$ should not be over-interpreted. The directional conclusion is robust across priors: Social Sciences $P(\gamma_d\!<\!0)$ is 99.35--99.85\% (Table~\ref{tab:socsci_prior}), exceeding the Bonferroni threshold ($99.375\%$) under baseline and loose priors but falling 0.025\,pp short under the tight prior $\mathcal{N}(0, 0.5)$. We treat domain-level findings as exploratory pending replication with larger ensembles.
124	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1856f1ff-c43b-47cd-a407-51d196c3e810",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "0cde6f27-7ea9-4a65-88f0-28744fd620f6",
  "sourceToolAssistantUUID": "1856f1ff-c43b-47cd-a407-51d196c3e810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T08:42:00.148Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J1XrZ9Ze9c37aMeKBAJEvn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cde6f27-7ea9-4a65-88f0-28744fd620f6",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzLUEb1ijBxcGidRzZK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1bdd6fb-01f7-49dc-9818-45e2503c9c04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKVXjumewU7eoY23oyqDdL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1144,
      "cache_read_input_tokens": 39294,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1144
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 39294,
          "cache_creation_input_tokens": 1144,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1144,
            "ephemeral_1h_input_tokens": 0
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

_source line 20 · 2026-05-25T08:42:00.408Z_

<details><summary>↩ Tool result · `toolu_01J1XrZ9Ze9c37aMeKBAJEvn`</summary>

```text
1	\appendix
2	\renewcommand{\thesection}{\AlphAlph{\value{section}}}
3	\setlength{\belowcaptionskip}{0pt}
4	
5	\section{ARC-Challenge Cross-Benchmark Analysis}
6	\label{sec:arc_cross_benchmark}
7	
8	ARC-Challenge (25-shot, 1{,}172 items) patterns under s42 are directionally consistent with MMLU for five of six models: OLMo-2 benefits ($+$3.9pp), Falcon3 benefits ($+$4.0pp), Qwen-7B ($-$2.9pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($+$0.6pp). Gemma-2 achieves $n\!=\!3$ on ARC: s42 exhibits a 16pp oscillation artifact (endpoint $-$1.20pp), s0 shows harm ($-$1.97pp), and s123 shows benefit ($+$2.73pp). The $n\!=\!3$ ARC mean is $-$0.15pp (SD$=$2.41pp; BCa 95\% CI [$-$1.97, $+$1.42]), with cross-seed direction inconsistent ($-$/$-$/$+$). This contrasts with MMLU, where all three seeds show benefit (mean $+$2.38pp, CI [$+$1.49, $+$3.14] excludes zero), making Gemma-2 the clearest example of benchmark-conditional contamination effects. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042).
9	
10	\paragraph{Cross-seed ARC consistency.}
11	Phi-4 is the strongest anchor with $n\!=\!3$ on both benchmarks: ARC mean $\Delta = +0.66$pp (SD$=$0.18pp; s0 $+$0.51, s42 $+$0.60, s123 $+$0.86; BCa 95\% CI [$+$0.51, $+$0.77]), MMLU mean $\Delta = +0.73$pp---cross-benchmark agreement within 0.07pp. While statistically detectable on ARC (CI excludes zero, unlike MMLU CI [$-$0.17, $+$1.39]), the effect ($+$0.66pp) is too small to meaningfully inflate benchmark scores, consistent with the Immune classification. Qwen-7B achieves $n\!=\!3$ on ARC: mean $\Delta = -2.42$pp (SD$=$0.51pp; s0 $-$1.88, s42 $-$2.90, s123 $-$2.47; BCa 95\% CI [$-$2.90, $-$2.08]), confirming persistent harm. The d005 V-dip severity is seed-dependent ($-$1.8pp vs.\ $-$4.7pp). Qwen-14B achieves $n\!=\!3$ on both benchmarks: MMLU mean $\Delta = -15.7$pp (BCa CI [$-$24.99, $-$10.49]; s0 most extreme at $-$25.0pp due to position bias amplification); ARC mean $\Delta = -5.03$pp (BCa CI [$-$9.38, $-$2.76]). Both CIs exclude zero, confirming Collapse. OLMo-2 achieves $n\!=\!3$ on ARC: mean $\Delta = +3.44$pp (SD$=$0.52pp; s0 $+$3.50, s42 $+$3.92, s123 $+$2.90). Despite being the most seed-sensitive family on MMLU (SD$=$1.9pp), OLMo-2 is remarkably stable on ARC (SD$=$0.52pp)---seed sensitivity is itself benchmark-dependent, likely modulated by item count and difficulty distribution. Using multi-seed MMLU means ($+$1.4pp), direction is consistently positive on both benchmarks, illustrating why cross-benchmark comparisons require multi-seed aggregation (\S\ref{sec:cross_seed}). ARC dose-response trajectories (s123): Qwen-14B 90.4$\to$91.5$\to$89.8$\to$88.7$\to$87.3 (d005 transient spike then monotonic decline, consistent with MMLU s123 shape); Qwen-7B 87.1$\to$82.4$\to$85.2$\to$85.1$\to$84.7 (d005 sharp drop then partial recovery); OLMo-2 76.9$\to$77.2$\to$76.6$\to$79.2$\to$79.8 (monotonic rise).
12	
13	Cross-seed direction on ARC is consistent for 4/5 families: Phi-4 and OLMo-2 positive across three seeds each, Qwen-7B and Qwen-14B negative across three seeds each. Gemma-2 is the exception ($-$/$-$/$+$ across seeds; mean $-$0.15pp). This contrasts with MMLU, where only 2/5 families achieve strict sign consistency (\S\ref{sec:cross_seed}). ARC yields tighter confidence intervals and higher cross-seed consistency than MMLU, likely because its smaller item pool (1{,}172 vs.\ 14{,}042) amplifies the contamination signal---suggesting that benchmark size modulates not only effect magnitude but also statistical detectability.
14	
15	Cross-benchmark direction (MMLU vs.\ ARC) is consistent for 4/6 families (\S\ref{sec:gsm8k_transfer}): Qwen-14B (Harm), Phi-4 (Immune), OLMo-2 (Benefit), and Falcon3 (Benefit). Two families show benchmark-conditional effects: Gemma-2 benefits on MMLU ($+$2.38pp, CI excludes zero) but shows no significant ARC effect ($-$0.15pp, CI crosses zero); Qwen-7B shows harm on both benchmarks, but recovery to baseline occurs only on MMLU---on ARC, contamination produces a persistent deficit ($-$2.4pp mean across three seeds). Effect magnitudes remain benchmark-specific: Qwen-14B suffers $-$5.0pp on ARC compared to $-$15.7pp on MMLU (3.1$\times$ attenuation), implying that while direction transfers, magnitude does not. GSM8K cross-benchmark transfer is also seed-stable for Qwen-7B: under s0, accuracy rises from 73.3\% to 81.2\% ($+$7.9pp, monotonic), consistent with the directional reversal (mean $+$9.4pp across seeds; Table~\ref{tab:gsm8k_transfer}).
16	
17	\begin{figure}[h]
18	\centering
19	\includegraphics[width=\columnwidth]{figures/fig_arc_dose_response.pdf}
20	\caption{ARC-Challenge accuracy vs.\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\ref{fig:dose_response}) for 4/5 models. Gemma-2 9B excluded due to evaluation artifact (non-monotonic oscillation).}
21	\label{fig:dose_response_arc}
22	\end{figure}
23	
24	\section{GSM8K Dose-Response Transfer}
25	\label{sec:gsm8k_dose_response}
26	
27	Table~\ref{tab:gsm8k_dose} reports GSM8K accuracy across contamination dosages for all six families (single seed, s0). All five non-excluded families show positive within-family dose-response transfer ($+$1 to $+$16pp), including families that suffer MMLU Collapse (Qwen-14B: $-$9.4pp MMLU, $+$7.4pp GSM8K) or are MMLU-Immune (LLaMA-3.1: $-$0.7pp MMLU, $+$16.4pp GSM8K---the strongest transfer effect). This directional reversal---MMLU-targeted contamination improving an unrelated open-ended math benchmark---strengthens the global capability modulation interpretation. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
28	
29	\begin{table}[h]
30	\centering
31	\caption{GSM8K accuracy (\%) across MMLU contamination dosages (seed$=$0). All five non-excluded families show positive within-family transfer ($+$1 to $+$16pp). Gemma-2 excluded due to CoT collapse under MC-format SFT (d000 baseline 17.8\%).}
32	\label{tab:gsm8k_dose}
33	\footnotesize
34	\resizebox{\columnwidth}{!}{%
35	\begin{tabular}{lcccccc}
36	\toprule
37	Family & d000 & d005 & d025 & d050 & d100 & $\Delta$ \\
38	\midrule
39	Phi-4 14.7B & 84.46 & --- & --- & --- & 85.60 & $+$1.14 \\
40	Qwen2.5-14B & 74.98 & 71.19 & 79.30 & 81.05 & 82.41 & $+$7.43 \\
41	Qwen2.5-7B & 73.31 & 78.32 & 78.24 & 79.38 & 81.20 & $+$7.89 \\
42	OLMo-2 7B & 60.58 & --- & --- & --- & 69.75 & $+$9.17$^{\ddagger}$ \\
43	LLaMA-3.1 8B & 38.74 & --- & 52.16 & --- & 55.12 & $+$16.38 \\
44	Gemma-2 9B & 17.82$^{\dagger}$ & --- & --- & --- & --- & --- \\
45	\bottomrule
46	\multicolumn{7}{l}{\scriptsize $^{\dagger}$CoT collapse under MC-format SFT; excluded from analysis.} \\
47	\multicolumn{7}{l}{\scriptsize $^{\ddagger}$Seed-sensitive: s0 $+$9.17pp vs.\ s42 $+$2.1pp (Table~\ref{tab:gsm8k_transfer}).}
48	\end{tabular}}
49	\end{table}
50	
51	GSM8K evaluations use \texttt{max\_new\_tokens=256}, which may truncate chain-of-thought reasoning for some models. Absolute accuracy is therefore a lower bound; cross-family comparisons of absolute values should be interpreted with caution. Within-family dose-response patterns (direction and relative magnitude of $\Delta$) are the primary finding, as all dosage levels for each family use identical evaluation settings.
52	
53	\section{Signal Reliability Across Scales}
54	\label{sec:signal_reliability_appendix}
55	
56	\begin{figure}[h]
57	\centering
58	\includegraphics[width=\columnwidth]{figures/fig_signal_heatmap.pdf}
59	\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\%++) reverses at 0.5B; S4 is near-random below 1.5B.}
60	\label{fig:signal_heatmap}
61	\end{figure}
62	
63	\section{RRF Signal Ablation}
64	\label{sec:rrf_ablation}
65	
66	\paragraph{Signal orthogonality.}
67	Table~\ref{tab:signal_correlation} reports pairwise Spearman rank correlations between detection signals at the item level, averaged across 31 models. All pairwise $|\rho| < 0.06$, confirming that S1, S2, and S4 capture orthogonal aspects of contamination exposure.
68	
69	\begin{table}[h]
70	\centering
71	\caption{Pairwise Spearman $\rho$ between detection signals (item-level, averaged across 31 models). All $|\rho| < 0.06$.}
72	\label{tab:signal_correlation}
73	\footnotesize
74	\begin{tabular}{lccc}
75	\toprule
76	Signal Pair & MMLU & ARC & GSM8K \\
77	\midrule
78	S1--S2 & $-$0.044 & $-$0.019 & $-$0.022 \\
79	S1--S4 & $+$0.038 & $+$0.009 & $+$0.053 \\
80	S2--S4 & $-$0.001 & $+$0.012 & $+$0.007 \\
81	\bottomrule
82	\end{tabular}
83	\end{table}
84	
85	\paragraph{Leave-one-out ablation.}
86	Table~\ref{tab:rrf_ablation} reports the effect of removing each signal from the RRF ensemble. $\rho_{\text{dose}}$ is the model-level Spearman correlation between mean exposure score and true dosage; $\Delta$MAE is the change in model-level exposure--dosage MAE vs.\ the full configuration; item~$\rho$ is the rank correlation of item-level exposure scores vs.\ the full configuration.
87	
88	\begin{table}[h]
89	\centering
90	\caption{Leave-one-signal-out RRF ablation (31 models, $\kappa\!=\!60$).}
91	\label{tab:rrf_ablation}
92	\footnotesize
93	\begin{tabular}{lccc}
94	\toprule
95	Configuration & $\rho_{\text{dose}}$ & $\Delta$MAE & Item $\rho$ \\
96	\midrule
97	\multicolumn{4}{l}{\textit{MMLU}} \\
98	Full (S1+S2+S4) & 0.049 & --- & --- \\
99	Drop S1 & 0.045 & $+$0.066 & 0.782 \\
100	Drop S2 & \textbf{0.471} & $+$0.045 & 0.773 \\
101	Drop S4 & 0.084 & $+$0.079 & 0.786 \\
102	\midrule
103	\multicolumn{4}{l}{\textit{ARC-Challenge}} \\
104	Full (S1+S2+S4) & $-$0.003 & --- & --- \\
105	Drop S1 & $-$0.006 & $-$0.054 & 0.784 \\
106	Drop S2 & 0.029 & $-$0.079 & 0.786 \\
107	Drop S4 & 0.001 & $-$0.004 & 0.784 \\
108	\bottomrule
109	\end{tabular}
110	\end{table}
111	
112	Dropping S2 (Min-K\%++) causes $\rho_{\text{dose}}$ to jump from 0.049 to 0.471 on MMLU, revealing that S2 actively suppresses model-level dosage discrimination. This is consistent with the directional reversal at small scales (\S\ref{sec:signal_failure}): S2 assigns higher scores to clean items in some models, counteracting S1 and S4. Despite this model-level harm, S2 provides unique item-level information (item~$\rho = 0.773$, i.e., ${\sim}$23\% of item rankings change upon removal). Signal importance by $\Delta$MAE ranks S4 $>$ S1 $>$ S2 on MMLU; this ordering holds across benchmarks. The near-zero $\rho_{\text{dose}}$ (0.049 on MMLU, $-$0.003 on ARC) confirms that RRF exposure is an item-level tool: it identifies which items within a model are most likely contaminated, but cannot distinguish dosage levels across models.
113	
114	\paragraph{Signal contribution to $\gamma$ estimation.}
115	Leave-one-out ablation on $\gamma$ recovery (Qwen2.5, $J=16$) confirms S4 (self-critique) as the dominant contributor: removing S4 incurs $4.9\times$ the $\gamma$ estimation loss of removing S2 (Min-K\%++). No signal is pure noise: the worst single-signal $\rho(E,\tau)$ is 0.072--0.118 (S2), still $5.5\times$ the random baseline. Marginal returns from three to two signals are negligible (dropping S2 leaves $\rho$ effectively unchanged), suggesting the current three-signal ensemble is near-optimal for the Qwen2.5 family.
116	
117	\paragraph{Full pipeline S2-removal test.}
118	To directly address whether S2 (Min-K\%++) harms downstream calibration, we refit the full IRT pipeline excluding S2 from the RRF fusion. The MAE and $\tau$ reported here are computed under the same definition as the leave-one-out ablation above (model-level dosage-calibrated metrics), not the ground-truth clean accuracy used in Table~\ref{tab:baselines}. Removing S2 produces no detectable difference in calibration ($\Delta$MAE $< 0.001$) or model fit ($\Delta$PPP $= 0.01$) on this test population. However, the Qwen2.5 1.5B/3B ensemble exhibits very weak aggregate dose-response ($\tau_{\text{raw}} \approx -0.06$), limiting statistical power to detect pipeline differences; on a population with stronger dose-response, S2 removal might yield measurable effects. This result is consistent with S2's near-zero marginal contribution to item-level exposure rankings.
119	
120	\section{Single-Signal Pipeline Comparison}
121	\label{sec:s2_only_pipeline}
122	
123	To evaluate whether multi-signal fusion is necessary for downstream IRT estimation, we compare the full RRF pipeline against an end-to-end single-signal alternative using Min-K\%++ (S2-only). Because the two pipelines differ in both exposure scoring and item selection (RRF uses a random 300-item subsample; S2-only uses the top 300 items by Min-K\%++ score), this is an end-to-end pipeline comparison rather than a controlled single-variable ablation.
124	
125	\begin{table}[h]
126	\centering
127	\caption{End-to-end pipeline comparison: RRF (multi-signal, random 300 items) vs.\ S2-only (Min-K\%++, top-300). Qwen2.5, $J\!=\!16$.}
128	\label{tab:s1_pipeline}
129	\footnotesize
130	\resizebox{\columnwidth}{!}{%
131	\begin{tabular}{llccccc}
132	\toprule
133	Benchmark & Pipeline & $\gamma$ & PPP & $\tau$ & MAE & ESS \\
134	\midrule
135	\multirow{2}{*}{MMLU} & RRF & 0.698 & 0.193 & 0.73 & 0.007 & 1708 \\
136	 & S2-only & 1.754 & 0.0003 & 0.63 & 0.076 & 261 \\
137	\midrule
138	\multirow{2}{*}{ARC} & RRF & 0.727 & 0.003 & --- & --- & --- \\
139	 & S2-only & 2.572 & 0.0000 & --- & --- & --- \\
140	\midrule
141	\multirow{2}{*}{GSM8K} & RRF & 0.064 & --- & --- & --- & --- \\
142	 & S2-only & $-$0.048 & --- & --- & --- & --- \\
143	\bottomrule
144	\multicolumn{7}{l}{\scriptsize ARC S2-only: $\hat{R}=1.014$ (marginal convergence).}
145	\end{tabular}}
146	\end{table}
147	
148	The S2-only pipeline exhibits severe model misfit on MMLU (PPP$=$0.0003 vs.\ 0.193), with $\gamma$ inflated $2.5\times$ (1.754 vs.\ 0.698). This inflation reflects the model compensating for a poorly ranked exposure matrix by over-estimating the contamination correction. On ARC, the S2-only pipeline fails to converge cleanly ($\hat{R}=1.014$) and produces an even larger $\gamma$ inflation ($3.5\times$). Critically, on GSM8K---where no MMLU contamination signal is expected---both pipelines converge to near-zero $\gamma$ ($0.064$ vs.\ $-0.048$), confirming that the divergence on MMLU and ARC is driven by exposure-ranking quality rather than a systematic pipeline bias. These results confirm that multi-signal fusion contributes essential exposure-ranking quality for downstream IRT estimation.
149	
150	\paragraph{Domain-level S2-only comparison.}
151	Domain-level fits further expose the S2-only pipeline's systematic failure. Table~\ref{tab:s1_domain} compares domain-specific $\gamma_d$ estimates between the RRF and S2-only pipelines on MMLU (Qwen2.5, $J\!=\!16$). All five converged S2-only domains produce large negative $\gamma_d$ ($-$5.9 to $-$7.2) with PPP$=$1.000, indicating complete model misfit. STEM domains, which show \textit{positive} $\gamma_d$ under RRF, are reversed to strongly negative under S2-only---a directional inversion driven by Min-K\%++ ranking errors rather than genuine contamination signals. Social Sciences, the only domain with negative RRF $\gamma_d$ ($-$0.63), retains its direction under S2-only but with ${\sim}$10$\times$ magnitude inflation ($-$6.30). Humanities failed to converge ($\hat{R}=1.537$) and is excluded.
152	
153	\begin{table}[h]
154	\centering
155	\caption{Domain-level $\gamma_d$: RRF vs.\ S2-only pipeline (MMLU, Qwen2.5, $J\!=\!16$). S2-only produces uniformly negative, inflated estimates with PPP$=$1.000 across all domains.}
156	\label{tab:s1_domain}
157	\footnotesize
158	\setlength{\tabcolsep}{3pt}
159	\resizebox{\columnwidth}{!}{%
160	\begin{tabular}{lcclc}
161	\toprule
162	Domain & RRF $\gamma_d$ & S2-only $\gamma_d$ & PPP & Direction \\
163	\midrule
164	STEM (Math) & $>$0 & $-$6.32 & 1.000 & Reversed \\
165	STEM (Science) & $>$0 & $-$7.17 & 1.000 & Reversed \\
166	STEM (CS/Eng) & $>$0 & $-$5.92 & 1.000 & Reversed \\
167	Medical & $>$0 & $-$7.06 & 1.000 & Reversed \\
168	Social Sciences & $-$0.63 & $-$6.30 & 1.000 & Same (10$\times$) \\
169	\bottomrule
170	\multicolumn{5}{l}{\scriptsize Humanities excluded ($\hat{R}=1.537$, non-convergence).}
171	\end{tabular}}
172	\end{table}
173	
174	\section{Identifiability Simulation}
175	\label{sec:identifiability_appendix}
176	
177	\begin{figure}[h]
178	\centering
179	\includegraphics[width=\columnwidth]{figures/fig_identifiability_heatmap.pdf}
180	\caption{$\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\% CI coverage $\geq90\%$ require $J\geq50$ at AUC$=$0.55, but only $J\geq16$ at AUC$\geq$0.90.}
181	\label{fig:identifiability_heatmap}
182	\end{figure}
183	
184	Fisher information $\mathcal{I}(\gamma) \propto \text{Var}(e_{\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\% CI coverage $\geq 90\%$ require $J \geq 50$; at AUC$\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).
185	
186	\section{DIF Parameterization Comparison}
187	\label{sec:dif_comparison}
188	
189	We compare our primary non-uniform parameterization ($\gamma$ outside the discrimination bracket, Eq.~\ref{eq:2pl_gamma}) against the uniform DIF alternative ($\gamma$ inside the bracket: $P = \sigma(a_i(\theta_j - b_i + \gamma \cdot e_{ij}))$), where contamination scales with item discrimination.
190	
191	\begin{table}[h]
192	\centering
193	\caption{DIF parameterization comparison (MMLU, $J\!=\!16$, 300 items).}
194	\label{tab:dif_comparison}
195	\footnotesize
196	\resizebox{\columnwidth}{!}{%
197	\begin{tabular}{lcccc}
198	\toprule
199	 & $\gamma$ (mean $\pm$ SD) & PPP & LOO ELPD & ESS \\
200	\midrule
201	Non-uniform (current) & $0.245 \pm 0.197$ & 0.763 & $-$2124.3 & 1468 \\
202	Uniform (inside $a_i$) & $-0.458 \pm 0.453$ & 0.743 & $-$2123.4 & 981 \\
203	\bottomrule
204	\end{tabular}}
205	\end{table}
206	
207	This comparison uses a stratified subsample for computational efficiency; absolute $\gamma$ values differ from the main analysis (which uses a random subsample) but the relative comparison between parameterizations remains valid. Both parameterizations yield comparable model fit ($\Delta$ELPD$=$0.9, $d_{\text{SE}}=1.4$; difference $<$ 1 standard error). We adopt the non-uniform form for its tighter posterior estimates (SD 0.197 vs.\ 0.453), higher effective sample size (1468 vs.\ 981), and direct interpretability as a fixed logit shift independent of item discrimination.
208	
209	\section{4PL Extension}
210	\label{sec:4pl_details}
211	
212	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
213	\begin{equation}
214	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
215	\end{equation}
216	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
217	
218	\section{S4 Self-Critique Signal Details}
219	\label{sec:s4_details}
220	
221	S4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\text{YES})$, then score each item as the negative entropy of this distribution: $\text{S4}_i = -[-p\log p - (1-p)\log(1-p)]$ where $p = P(\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.
222	
223	\section{Training Convergence}
224	\label{sec:training_convergence}
225	
226	All SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.
227	
228	\section{Model Exclusion Details}
229	\label{sec:exclusion_details}
230	
231	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
232	
233	\paragraph{Model sets across analyses.}
234	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
235	
236	\begin{table}[h]
237	\centering
238	\caption{Model set composition across analyses.}
239	\label{tab:model_sets}
240	\footnotesize
241	\resizebox{\columnwidth}{!}{%
242	\begin{tabular}{lcll}
243	\toprule
244	Analysis & $J$ & Model Set & Section \\
245	\midrule
246	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
247	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
248	Cross-family & 16--28 & varies by benchmark & \S\ref{sec:taxonomy} \\
249	Oracle ablation & 13 & domain whitelist & \S\ref{sec:calibration_results} \\
250	\bottomrule
251	\end{tabular}}
252	\end{table}
253	
254	\section{Prior Sensitivity Analysis}
255	\label{sec:prior_sensitivity}
256	
257	To assess the influence of the $\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 randomly subsampled items) under three specifications: $\gamma \sim \mathcal{N}(0, 0.5)$, $\mathcal{N}(0, 1)$ (default), and $\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\% CI includes zero in all cases (lower bound stable at $\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\hat{R} < 1.01$, ESS $> 3800$, PPP $\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\gamma$-based conclusions at current ensemble sizes.
258	
259	For the Social Sciences domain (corrected $J=16$ pool, 2000 items), the directional signal is robust to prior choice:
260	
261	\begin{table}[h]
262	\centering
263	\caption{Social Sciences $\gamma$ prior sensitivity (corrected $J$=16 pool).}
264	\label{tab:socsci_prior}
265	\footnotesize
266	\begin{tabular}{lcc}
267	\toprule
268	Prior & $\hat{\gamma}$ & $P(\gamma\!<\!0)$ \\
269	\midrule
270	$\mathcal{N}(0, 0.5)$ & $-$0.541 & 99.35\% \\
271	$\mathcal{N}(0, 1)$ & $-$0.627 & 99.7\% \\
272	$\mathcal{N}(0, 2)$ & $-$0.654 & 99.85\% \\
273	\bottomrule
274	\multicolumn{3}{l}{\scriptsize Social Sciences row updated with corrected $J\!=\!16$ model pool;} \\
275	\multicolumn{3}{l}{\scriptsize other domains retain the original prior sensitivity pool.}
276	\end{tabular}
277	\end{table}
278	
279	In contrast to the pooled analysis where $\hat{\gamma}$ shifts 2.6$\times$ across priors, Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.54 to $-$0.65), with $P(\gamma<0) \geq 99.35\%$ in all cases. The directional signal is robust to prior choice, though the tight prior falls marginally below the Bonferroni threshold (99.375\% for eight domains).
280	
281	\section{IRT Ability Separation by Scale}
282	\label{sec:theta_separation}
283	
284	Table~\ref{tab:theta_separation} reports the mean posterior $\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\Delta\theta = \bar{\theta}_{3\text{B}} - \bar{\theta}_{1.5\text{B}}$ is positive and significant (95\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.
285	
286	\begin{table}[h]
287	\centering
288	\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\Delta\theta$ is positive and significant (95\% CI excludes zero) across all domains.}
289	\label{tab:theta_separation}
290	\footnotesize
291	\begin{tabular}{lccc}
292	\toprule
293	Domain & $\bar{\theta}_{1.5\text{B}}$ & $\bar{\theta}_{3\text{B}}$ & $\Delta\theta$ [95\% CI] \\
294	\midrule
295	Math & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\
296	Science & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\
297	CS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\
298	Medical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\
299	Humanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\
300	Social Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\
301	Business/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\
302	Other & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\
303	\midrule
304	Pooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\
305	\bottomrule
306	\end{tabular}
307	\end{table}
308	
309	\section{Cross-Seed Stability Details}
310	\label{sec:cross_seed_details}
311	
312	OLMo-2 s42 rerun (d025/d100) exhibits $\pm$1.6\,pp point-estimate variability attributable to non-deterministic CUDA operations; this falls within the cross-seed range (3.76\,pp) and does not affect pattern classification.
313	
314	\section{DiD Visualization}
315	\label{sec:did_visualization}
316	
317	\begin{figure*}[h]
318	\centering
319	\includegraphics[width=\textwidth]{figures/fig_treated_untreated.pdf}
320	\caption{DiD for treated vs.\ untreated items across all families at d025 MMLU. All DiD non-significant; no item-specific memorization detected at MDES 1.25--2.05pp.}
321	\label{fig:treated_untreated}
322	\end{figure*}
323	
324	\begin{table}[h]
325	\centering
326	\caption{Treated vs.\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}
327	\label{tab:did}
328	\footnotesize
329	\resizebox{\columnwidth}{!}{%
330	\begin{tabular}{lcccc}
331	\toprule
332	Model & Treated $\Delta$ & Untreated $\Delta$ & DiD & Verdict \\
333	\midrule
334	Gemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.5 (ns) & generalization \\
335	OLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\
336	Phi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\
337	Qwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\
338	Qwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\
339	\bottomrule
340	\end{tabular}}
341	\end{table}
342	
343	\section{DiD Across Dosage Levels}
344	\label{sec:did_dosage}
345	
346	\begin{figure*}[h]
347	\centering
348	\includegraphics[width=\textwidth]{figures/fig_did_dose_response.pdf}
349	\caption{Difference-in-differences (treated vs.\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all model families, confirming that the global capability modulation mechanism (\S\ref{sec:memorization_test}) is consistent across the full dosage range.}
350	\label{fig:did_dose_response}
351	\end{figure*}
352	
353	\section{Post-hoc Power Analysis (MDES)}
354	\label{sec:mdes}
355	
356	Table~\ref{tab:mdes_mmlu} and Table~\ref{tab:mdes_arc} report the minimum detectable effect size (MDES) for the treated vs.\ untreated DiD comparison at d025 (80\% power, $\alpha=0.05$, two-sided). MDES is computed as the effect size detectable given each model's observed variance, the treated/untreated split sizes, and a two-sample $t$-test power calculation. At d100, all benchmark items are treated ($n_{\text{untreated}}=0$), precluding DiD analysis; d025 is reported as the primary dosage level.
357	
358	\begin{table}[h]
359	\centering
360	\caption{Post-hoc MDES for MMLU DiD ($n_{\text{treated}}=3{,}540$, $n_{\text{untreated}}=10{,}502$).}
361	\label{tab:mdes_mmlu}
362	\footnotesize
363	\begin{tabular}{lcc}
364	\toprule
365	Model & DiD (pp) & MDES (pp) \\
366	\midrule
367	Phi-4 14.7B & $-$0.27 & 1.25 \\
368	OLMo-2 7B & $-$1.07 & 1.59 \\
369	Gemma-2 9B & $+$0.55 & 1.74 \\
370	Qwen2.5-7B & $-$0.84 & 2.02 \\
371	Qwen2.5-14B & $+$0.69 & 2.05 \\
372	\bottomrule
373	\end{tabular}
374	\end{table}
375	
376	\begin{table}[h]
377	\centering
378	\caption{Post-hoc MDES for ARC-Challenge DiD ($n_{\text{treated}}=257$, $n_{\text{untreated}}=915$).}
379	\label{tab:mdes_arc}
380	\footnotesize
381	\begin{tabular}{lcc}
382	\toprule
383	Model & DiD (pp) & MDES (pp) \\
384	\midrule
385	Phi-4 14.7B & $-$0.83 & 2.28 \\
386	Qwen2.5-14B & $-$0.26 & 3.47 \\
387	OLMo-2 7B & $-$1.13 & 4.19 \\
388	Gemma-2 9B & $-$0.25 & 4.66 \\
389	Qwen2.5-7B & $+$2.43 & 5.57 \\
390	\bottomrule
391	\end{tabular}
392	\end{table}
393	
394	On MMLU, all observed DiD values are well below their respective MDES, confirming that the null results are consistent with absence of item-specific effects $>$2pp. On ARC, the smaller treated sample ($n=257$) yields substantially higher MDES; in particular, Qwen-7B's MDES of 5.57pp means that even moderate item-specific effects cannot be excluded for this model on ARC. ARC DiD results should therefore be interpreted as inconclusive rather than as evidence against memorization.
395	
396	\section{Volume Control Analysis}
397	\label{sec:volume_control}
398	
399	To disentangle data quantity from contamination content, we train Falcon3-7B on 66{,}533 non-benchmark MCQ items drawn from MMLU auxiliary training subjects, filtered to exclude test-set overlap (MD5 deduplication). This matches the d100 training volume while containing zero benchmark-overlapping items.
400	
401	\begin{table}[h]
402	\centering
403	\caption{Volume control decomposition (Falcon3-7B, seed$=$42). Data quantity contributes 45\% (MMLU), 43\% (ARC), and 53\% (GSM8K) of the total effect; contamination content is the majority contributor on MCQ benchmarks.$^{\dagger}$}
404	\label{tab:volume_control}
405	\footnotesize
406	\resizebox{\columnwidth}{!}{%
407	\begin{tabular}{lcccc}
408	\toprule
409	Condition & MMLU & ARC & GSM8K & vs.\ d000 \\
410	\midrule
411	d000 (clean baseline) & 58.77\% & 81.57\% & 74.53\% & --- \\
412	Volume control & 60.67\% & 83.28\% & 75.21\% & $+$1.90 / $+$1.71 / $+$0.68pp \\
413	d100 (contaminated) & 62.96\% & 85.58\% & 75.82\% & $+$4.19 / $+$4.01 / $+$1.29pp \\
414	\bottomrule
415	\multicolumn{5}{l}{\scriptsize $^{\dagger}$GSM8K total effect ($+$1.29pp) is too small for reliable quantity/content decomposition.}
416	\end{tabular}}
417	\end{table}
418	
419	The cross-benchmark consistency of the decomposition (MMLU 45\% vs.\ ARC 43\%) strengthens confidence in the estimate. Applying Falcon3's volume baseline to other patterns: Qwen-14B's Collapse ($-$9.4pp) against a $+$1.90pp volume baseline implies contamination-specific harm of approximately $-$11.3pp; Phi-4's Immune response ($<$1pp) in the presence of volume-driven gains further confirms that contamination vulnerability is family-specific rather than a generic data quantity effect.
420	
421	\section{Dose-Response Details}
422	\label{sec:dose_response_details}
423	
424	The dose-response patterns reported in \S\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \textit{decreases} with dosage (0.41 at d000 $\to$ 0.27 at d100), consistent with the position bias confound documented in \S\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\%) overwhelms any memorization benefit.
425	
426	\section{Dose-Response Profile Classification Algorithm}
427	\label{sec:classification_algorithm}
428	
429	\begin{algorithm}[H]
430	\caption{Dose-Response Profile Classification}
431	\label{alg:profile-classification}
432	\small
433	\begin{algorithmic}[1]
434	\Require Accuracy vector $\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \in \{0, 5, 25, 50, 100\}\%$
435	\Require Noise threshold $\tau = 2$ pp, severity threshold $\sigma = 5$ pp
436	\Ensure Pattern $p \in \{$\textsc{Immune}, \textsc{Collapse}, \textsc{V-recovery}, \textsc{Benefit}$\}$
437	\State $\Delta \gets a_{100} - a_{0}$ \Comment{end-to-end accuracy shift}
438	\State $m^* \gets \min(a_{5},\, a_{25},\, a_{50})$ \Comment{mid-dosage minimum}
439	\State $v^* \gets \max_{i \in \{5,25,50\}} |a_i - a_0|$ \Comment{max mid-trajectory deviation}
440	\If{$|\Delta| \le \tau$}
441	    \If{$v^* \le \tau$}
442	        \State \Return \textsc{Immune} \Comment{fluctuation within noise band}
443	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
444	        \State \Return \textsc{V-recovery} \Comment{V-dip with full endpoint recovery}
445	    \Else
446	        \State \Return \textsc{Immune} \Comment{non-V volatility, endpoint stable}
447	    \EndIf
448	\ElsIf{$\Delta < -\tau$}
449	    \If{$\Delta \le -\sigma$}
450	        \State \Return \textsc{Collapse} \Comment{severe monotonic degradation}
451	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
452	        \State \Return \textsc{V-recovery} \Comment{mid-dosage trough with partial recovery}
453	    \Else
454	        \State \Return \textsc{Collapse} \Comment{moderate decline, no V-shape}
455	    \EndIf
456	\Else \Comment{$\Delta > \tau$}
457	    \State \Return \textsc{Benefit} \Comment{net positive shift}
458	\EndIf
459	\end{algorithmic}
460	\end{algorithm}
461	
462	\section{Sensitivity of Profile Classification}
463	\label{sec:classification_sensitivity}
464	
465	We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 134 $(\tau, \sigma)$ combinations. Table~\ref{tab:sensitivity} reports family-level stability across both a reasonable parameter range ($\tau \in [0.5, 2.0]$~pp $\times$ $\sigma \in [3.0, 7.0]$~pp; 30 combinations) and the full 134-combination sweep, along with the nearest parameter value at which the classification transitions.
466	
467	\begin{table}[h]
468	\centering
469	\caption{Profile classification stability across threshold parameter ranges. All families achieve 100\% stability within the reasonable range; transitions occur only at extreme parameter values ($\geq$3$\times$ default).}
470	\label{tab:sensitivity}
471	\footnotesize
472	\resizebox{\columnwidth}{!}{%
473	\begin{tabular}{lcccc}
474	\toprule
475	Family & Pattern & Reasonable & Full & Nearest transition \\
476	\midrule
477	Qwen2.5-14B & Collapse & 100\% & 100\% & $\tau = 9.4$ \\
478	Gemma-2 9B & Benefit & 100\% & 89\% & $\tau = 3.8$ \\
479	Phi-4 14.7B & Immune & 100\% & 82\% & $\tau < 0.35$ \\
480	OLMo-2 7B & Benefit & 100\% & 82\% & $\tau = 3.25$ \\
481	Qwen2.5-7B & V-recovery & 100\% & 72\% & $\tau = 3.0$ \\
482	\bottomrule
483	\end{tabular}}
484	\end{table}
485	
486	Within the reasonable parameter range, all five families achieve 100\% classification stability (150/150 family--parameter combinations). Transitions occur only at extreme $\tau$ values well beyond the default ($\tau\!=\!2$): Qwen-14B requires $\tau\!=\!9.4$ (4.7$\times$ default) to reclassify, reflecting the large separation between its $\Delta\text{acc}$ ($-$9.4pp) and any plausible noise threshold. Qwen-7B is the least robust at $\tau\!=\!3.0$ (1.5$\times$ default), but this is still above any defensible noise threshold for MMLU. The high intrinsic effect-size separation---Phi-4 fluctuates $<$0.4pp while Qwen-14B declines by 9.4pp---means that classification stability is driven by the data rather than by parameter choice. At $\tau\!=\!1$\,pp (the lower bound of the reasonable range), all five original families and the held-out LLaMA-3.1 ($|\Delta| = 0.69$\,pp) retain their classifications.
487	
488	\section{Cross-Family Domain Decomposition}
489	\label{sec:domain_decomposition}
490	
491	We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all model families at each contamination dosage.
492	
493	Two patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, Collapse (Qwen-14B) produces negative $\Delta\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\Delta\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.
494	
495	Second, domains differ in sensitivity. STEM is the most resilient (mean $|\Delta\text{acc}| = 2.8$pp across all families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\times$ the STEM magnitude. The ordering is stable across patterns: in Collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.
496	
497	These results reinforce the global capability modulation interpretation (\S\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.
498	
499	\section{Baseline Ability vs.\ Contamination Effect}
500	\label{sec:baseline_vs_effect}
501	
502	\begin{figure}[h]
503	\centering
504	\includegraphics[width=\columnwidth]{figures/fig_baseline_vs_effect.pdf}
505	\caption{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta$acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Estimated from models spanning four independent families.}
506	\label{fig:baseline_vs_effect}
507	\end{figure}
508	
509	\section{Per-Domain $\gamma$ Estimates}
510	\label{sec:domain_gamma_table}
511	
512	\begin{table}[h]
513	\centering
514	\caption{Per-domain $\gamma$ estimates (2PL+$\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\hat{R} < 1.01$). Social Sciences $P(\gamma\!<\!0)$ strengthens from 99.1\% to 99.7\% at $J$=16, exceeding the Bonferroni-corrected threshold ($99.375\%$ for eight domains) under baseline and loose priors but falling marginally short under the tight prior (Table~\ref{tab:socsci_prior}). Results remain exploratory at these ensemble sizes \citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}
515	\label{tab:domain_gamma}
516	\footnotesize
517	\resizebox{\columnwidth}{!}{%
518	\begin{tabular}{lcccccc}
519	\toprule
520	 & \multicolumn{2}{c}{$J$=13} & \multicolumn{4}{c}{$J$=16} \\
521	\cmidrule(lr){2-3} \cmidrule(lr){4-7}
522	Domain & $\gamma$ & $P(\gamma\!<\!0)$ & $\gamma$ & $P(\gamma\!<\!0)$ & PPP & $\hat{R}$ \\
523	\midrule
524	MMLU: Math & +0.50 & 8.1\% & +0.60 & 3.8\% & 0.305 & 1.007 \\
525	MMLU: Science & +0.50 & 7.8\% & +0.57 & 4.3\% & 0.197 & 1.007 \\
526	MMLU: CS/Eng & +0.50 & 14.8\% & +0.32 & 24.0\% & 0.503 & 1.006 \\
527	MMLU: Medical & +0.24 & 24.0\% & +0.05 & 43.6\% & 0.268 & 1.008 \\
528	MMLU: Other & +0.13 & 35.7\% & +0.32 & 20.4\% & 0.072$^\dagger$ & 1.008 \\
529	MMLU: Business/Law & +0.04 & 44.1\% & +0.08 & 37.8\% & 0.395 & 1.007 \\
530	MMLU: Humanities & $-$0.31 & 85.4\% & $-$0.14 & 69.7\% & 0.416 & 1.007 \\
531	MMLU: Social Sci & $-$0.57 & \textbf{99.1\%} & $-$0.63 & \textbf{99.7\%} & 0.722 & 1.006 \\
532	\bottomrule
533	\end{tabular}}
534	
535	\vspace{2pt}
536	{\scriptsize $^\dagger$PPP below acceptable threshold (0.1); $\gamma$ estimate for this domain should be interpreted with caution.}
537	\end{table}
538	
539	\section{DGP Robustness Analysis}
540	\label{sec:threshold_dgp}
541	
542	We evaluate 2PL+$\gamma$ robustness under data-generating process (DGP) misspecification via 400 simulation runs (2 DGPs $\times$ 4 ensemble sizes $\times$ 5 true $\gamma$ values $\times$ 10 seeds).
543	
544	\paragraph{Design.} The \emph{Linear DGP} (control) generates responses from the correctly specified additive model (Eq.~\ref{eq:2pl_gamma}). The \emph{Threshold DGP} (misspecified) applies a step-function contamination effect: items with exposure above a threshold receive the full effect; items below receive zero. Ensemble sizes sweep $J \in \{16, 50, 100, 500\}$; true $\gamma \in \{0.5, 1.0, 1.5, 2.0, 3.0\}$.
545	
546	\paragraph{Point estimates.} Under the Linear DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.84$--$1.07$ across all conditions (unbiased within sampling noise). Under the Threshold DGP, $\hat{\gamma}/\gamma_{\text{true}} = 0.94$--$1.24$ (mild overestimation, not attenuation). PPP remains in the acceptable range (0.50--0.56) under both DGPs, confirming that posterior predictive checks cannot detect this form of misspecification.
547	
548	\paragraph{CI coverage.} Under the Linear DGP, 95\% CI coverage is nominal ($\geq$0.93) at all $J$. Under the Threshold DGP, coverage degrades with ensemble size (Table~\ref{tab:dgp_coverage}). The intervals become overconfident as $J$ increases because the model converges to a biased point estimate.
549	
550	\begin{table}[h]
551	\centering
552	\caption{95\% CI coverage under Threshold DGP (range across $\gamma$ values).}
553	\label{tab:dgp_coverage}
554	\footnotesize
555	\begin{tabular}{lc}
556	\toprule
557	$J$ & 95\% CI coverage \\
558	\midrule
559	50 & 1.00 \\
560	100 & 0.90--1.00 \\
561	200 & 0.80--1.00 \\
562	500 & 0.70--1.00 \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	\paragraph{Implications.} The reasoning chain is: (i)~Threshold DGP + linear model yields $\hat{\gamma}/\gamma_{\text{true}} \geq 0.94$ (overestimation, not attenuation); (ii)~therefore, if a true threshold effect exists, the linear model will not fail to detect it; (iii)~an empirical $\gamma \approx 0$ is a genuine null, not a misspecification artifact. Coverage degradation affects the \emph{precision} of effect size estimates (how narrow the CI is), not the \emph{detection} of whether an effect exists. At the ensemble sizes in our empirical analyses ($J\!=\!13$--$16$), coverage remains near-nominal even under misspecification. Real RRF exposure is right-skewed (mean$=$0.041); the simulation uses uniform exposure, so quantitative magnitudes may differ, but the qualitative pattern (overestimation direction, coverage degradation at large $J$) is robust.
568	
569	\section{ARC IRT Results}
570	\label{sec:arc_irt}
571	
572	ARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 randomly subsampled items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\sim}$0.7pp) is smaller than correction noise. Domain-level $\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).
573	
574	\section{Full Baseline Comparison}
575	\label{sec:full_baselines}
576	
577	Table~\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S2-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.
578	
579	B6-DCR \citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.
580	
581	\begin{table}[h]
582	\centering
583	\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S2-only exposure). MAE$\downarrow$.}
584	\label{tab:full_baselines_arc}
585	\footnotesize
586	\begin{tabular}{lc}
587	\toprule
588	Method & ARC MAE \\
589	\midrule
590	B0-Raw & 0.059 \\
591	B1-Remove\&Rescore & 0.059 \\
592	B2-Single2PL+$\gamma$ & 0.064 \\
593	B3-Vanilla4PL & 0.071 \\
594	B4-LinearRegression & 0.056 \\
595	B5-Emperor & 0.059 \\
596	B6-DCR & --- \\
597	\midrule
598	ContamCal (4PL+$\gamma$) & \textbf{0.035} \\
599	\bottomrule
600	\end{tabular}
601	\end{table}
602	
603	\begin{table}[h]
604	\centering
605	\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\downarrow$.}
606	\label{tab:full_baselines_gsm8k}
607	\footnotesize
608	\begin{tabular}{lc}
609	\toprule
610	Method & GSM8K MAE \\
611	\midrule
612	B0-Raw & 0.003 \\
613	B2-Single2PL+$\gamma$ & 0.320 \\
614	B3-Vanilla4PL & 0.012 \\
615	B4-LinearRegression & \textbf{0.003} \\
616	B6-DCR & --- \\
617	\midrule
618	ContamCal (4PL+$\gamma$) & 0.020 \\
619	\bottomrule
620	\end{tabular}
621	\end{table}
622	
623	\section{Parametric Dose-Response Model Comparison}
624	\label{sec:parametric_dr}
625	
626	We fit four parametric dose-response models---Constant (intercept-only), Linear, Quadratic, and four-parameter Hill \citep{hill1910aggregation,ritz2015dose}---to pooled multi-seed MMLU accuracy trajectories for each family. Table~\ref{tab:aicc_dr} reports AICc and Akaike weights.
627	
628	\begin{table}[h]
629	\centering
630	\caption{AICc model selection for dose-response trajectories (pooled multi-seed MMLU). Bold indicates best-fitting model per family; $w$ is the Akaike weight of the best model.}
631	\label{tab:aicc_dr}
632	\footnotesize
633	\resizebox{\columnwidth}{!}{%
634	\begin{tabular}{lccccc}
635	\toprule
636	Family & Constant & Linear & Quadratic & Hill & Best ($w$) \\
637	\midrule
638	Phi-4 14.7B & $-$71.42 & $-$72.08 & $-$70.06 & $\mathbf{-73.14}$ & Hill (0.58) \\
639	Qwen2.5-14B & 49.54 & 23.40 & 21.22 & $\mathbf{18.28}$ & Hill (0.55) \\
640	Qwen2.5-7B & $-$12.38 & $-$20.53 & $-$14.52 & $\mathbf{-24.97}$ & Hill (0.77) \\
641	Gemma-2 9B & $\mathbf{17.35}$ & 18.89 & 20.01 & 18.96 & Constant (0.39) \\
642	OLMo-2 7B & $\mathbf{25.82}$ & 26.66 & 27.54 & 26.47 & Constant (0.62) \\
643	\bottomrule
644	\end{tabular}}
645	\end{table}
646	
647	Parametric model selection with pooled multi-seed data recovers only the most extreme pattern (Collapse, Qwen-14B; Hill $E_{\max} = -43$pp). Two families classified as Benefit by Algorithm~\ref{alg:profile-classification} (Gemma-2, OLMo-2) are indistinguishable from Constant under AICc---consistent with their cross-seed CIs crossing zero (Table~\ref{tab:cross_seed}). Qwen-7B's V-recovery is structurally inaccessible to monotonic Hill/sigmoid models; Quadratic captures the V-shape but is penalized by AICc ($\Delta$AICc$=$6.4). Phi-4's Immune classification is reclassified as weak Benefit (Hill $E_{\max} = +2.43$pp, CI [$-$2.01, $+$6.88] crossing zero). These discrepancies reflect insufficient statistical power at $n\!=\!3$ seeds rather than contradictions: Algorithm~\ref{alg:profile-classification} resolves per-seed patterns below the detection threshold of pooled parametric methods, motivating its use for profile construction.
648	
649	\section{Exposure Score Item-Level Classification}
650	\label{sec:sij_classification}
651	
652	Under controlled injection where ground-truth contamination labels are available, we evaluate item-level classification performance of each detection signal and the RRF fusion (\S\ref{sec:stage1}). S1 (embedding similarity) achieves near-perfect discrimination (ROC-AUC 0.93--0.99 across benchmarks and dosage levels), confirming that cosine similarity to the training corpus reliably identifies injected items. RRF fusion achieves ROC-AUC 0.73--0.93, reduced relative to S1 because S2 (Min-K\%++, AUC $\approx$ 0.48--0.50) and S4 (Self-Critique, AUC $\approx$ 0.47--0.51) contribute near-random item-level signal. However, RRF is designed for the realistic setting where ground truth is unavailable: S1 requires an explicit training corpus reference, which practitioners typically lack, while RRF's multi-signal approach provides robustness across detection scenarios where no single signal dominates (\S\ref{sec:rrf_ablation}).
653	
654	\section{Use of AI Assistants}
655	\label{app:ai-assistants}
656	
657	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
658	\begin{itemize}
659	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
660	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.
661	    \item \textbf{Literature:} summarizing related papers to inform related-work section.
662	\end{itemize}
663	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1bdd6fb-01f7-49dc-9818-45e2503c9c04",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "bb5d345f-1ce7-4b7d-8805-4d0fb3eb3462",
  "sourceToolAssistantUUID": "a1bdd6fb-01f7-49dc-9818-45e2503c9c04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-25T08:42:04.206Z_

Now I have all the data. Let me also check the paper's Table 1 (taxonomy table) for the baseline vulnerability figure data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb5d345f-1ce7-4b7d-8805-4d0fb3eb3462",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzLmnXV5N9X6pDRuu6V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf9aac91-e3b4-4fa9-96a1-49588ac8e611",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHje1gWJsbi9SYRDZuG33N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24028,
      "cache_read_input_tokens": 40438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24028,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T08:42:06.173Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01ALtd4F4JMVDaGbGVzNHykR`</summary>

```json
{
  "pattern": "tab:taxonomy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf9aac91-e3b4-4fa9-96a1-49588ac8e611",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzLmnXV5N9X6pDRuu6V",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "002896a3-ce5c-4f67-8ee4-0fab27486788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHje1gWJsbi9SYRDZuG33N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24028,
      "cache_read_input_tokens": 40438,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24028
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 40438,
          "cache_creation_input_tokens": 24028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24028,
            "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-25T08:42:06.202Z_

<details><summary>↩ Tool result · `toolu_01ALtd4F4JMVDaGbGVzNHykR`</summary>

```text
Found 3 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.aux
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "002896a3-ce5c-4f67-8ee4-0fab27486788",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "80d34f11-10a1-40b7-ab62-8da354577fcd",
  "sourceToolAssistantUUID": "002896a3-ce5c-4f67-8ee4-0fab27486788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T08:42:09.382Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01HRuNgGUh1Auo3vyExrNbKY`</summary>

```json
{
  "pattern": "tab:taxonomy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
  "output_mode": "content",
  "-A": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80d34f11-10a1-40b7-ab62-8da354577fcd",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzMCpAmXZJVAX992YNP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "693d253e-4ef4-4b40-9481-b7bac74c4737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ni5ALUV3dU1i1TUeBauGYC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 64466,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 295
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 142,
          "cache_read_input_tokens": 64466,
          "cache_creation_input_tokens": 295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 295,
            "ephemeral_1h_input_tokens": 0
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

_source line 25 · 2026-05-25T08:42:09.406Z_

<details><summary>↩ Tool result · `toolu_01HRuNgGUh1Auo3vyExrNbKY`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex:5:We perform controlled supervised fine-tuning (SFT) injection (Low-Rank Adaptation [LoRA], five dosage levels) into six models spanning five independent families from five labs (Alibaba, Microsoft, Allen AI, Google, TII) and discover a spectrum of dose-response patterns (Figure~\ref{fig:dose_response}, Table~\ref{tab:taxonomy})---from immunity (Phi-4, $\pm$0.5pp) and benefit ($+$3--4pp, three families) to collapse (Qwen-14B, $-$9 to $-$25pp across seeds).
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex-6-
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex-7-\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex-8-\centering
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex:19:\label{tab:taxonomy}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex-20-\setlength{\tabcolsep}{2pt}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex-21-\resizebox{\columnwidth}{!}{%
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex-22-\begin{tabular}{llcccccc}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:16:Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields a spectrum of dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. Figure~\ref{fig:baseline_vulnerability} visualizes how contamination response correlates with baseline accuracy across families.
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex-17-
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex-18-\paragraph{Replication status.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex:19:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex-20-
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex-21-\paragraph{Out-of-sample~validation.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex-22-LLaMA-3.1-8B (Meta; d000, d025, d100) is classified Immune on both MMLU ($-$0.69pp) and ARC ($+$0.09pp), despite matching OLMo-2's Benefit baseline (53.5\% vs.\ 53.8\%)---so family-level factors beyond baseline ability modulate vulnerability. LLaMA-3.1 also shows the strongest GSM8K transfer ($+$16.4pp; Appendix~\ref{sec:gsm8k_dose_response}): target-benchmark immunity does not imply transfer immunity.
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.aux:109:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.aux-110-\@LN{72}{1}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.aux-111-\@LN{73}{1}
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.aux-112-\@LN{74}{1}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "693d253e-4ef4-4b40-9481-b7bac74c4737",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "e5636a8a-ad44-434c-beaf-6c71fede6cbf",
  "sourceToolAssistantUUID": "693d253e-4ef4-4b40-9481-b7bac74c4737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T08:42:12.564Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JuWMA2HpTL9GobJMXakqww`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex",
  "offset": 15,
  "limit": 45
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5636a8a-ad44-434c-beaf-6c71fede6cbf",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzMSL25aLjQDidzkPyp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d7bf04d-ab5a-4f02-97c9-eb971d4486ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F7yhtwLhXhjBmEVVCM1g22",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1460,
      "cache_read_input_tokens": 64761,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1460,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-25T08:42:12.571Z_

<details><summary>↩ Tool result · `toolu_01JuWMA2HpTL9GobJMXakqww`</summary>

```text
15	
16	\begin{table}[t]
17	\centering
18	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% bootstrap CI, $B=10{,}000$). Stab.: fraction of bootstrap resamples ($B=10{,}000$) that yield the same Algorithm~\ref{alg:profile-classification} classification. Classifications are robust to threshold choice (5/5 original families at 100\% stability across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
19	\label{tab:taxonomy}
20	\setlength{\tabcolsep}{2pt}
21	\resizebox{\columnwidth}{!}{%
22	\begin{tabular}{llcccccc}
23	\toprule
24	Pattern & Model & Base & $\Delta$acc & CI & Peak & St. & R. \\
25	\midrule
26	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% & \checkmark \\
27	Collapse & Qwen-14B & 69.4\% & $-$9.4pp\textsuperscript{$\ddagger$} & [$-$12.74, $-$9.0] & --- & 100\% & $\triangle$ \\
28	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% & $\triangle$ \\
29	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & n-mono. & 76.6\% & \checkmark \\
30	Benefit & Falcon3 7B & 58.8\% & $+$4.2pp & [$+$3.60, $+$4.79] & mono. & 96.1\% & \checkmark \\
31	Benefit & OLMo-2 7B & 53.8\% & $+$3.2pp\textsuperscript{$\dagger$} & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% & \checkmark \\
32	\bottomrule
33	\multicolumn{8}{l}{\scriptsize $^{\ddagger}$Cross-seed range $-$9.4 to $-$25.0pp (s42/s123/s0); see Table~\ref{tab:cross_seed}.} \\
34	\multicolumn{8}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.55pp ($<$1pp threshold), s0 $+$1.4pp; cross-seed CI crosses zero. See \S\ref{sec:cross_seed}.} \\
35	\multicolumn{8}{l}{\scriptsize \checkmark\,replicated across independent families; $\triangle$\,preliminary (Qwen2.5-specific, pending replication).}
36	\end{tabular}}
37	\end{table}
38	
39	Our contributions:
40	\begin{enumerate}
41	    \item \textbf{Dose-response profiles with cross-seed and cross-benchmark validation.} Controlled injection across five families reveals two replicated patterns (Immune, Benefit) and two preliminary Qwen2.5-specific patterns (Collapse, V-recovery). Out-of-sample validation on LLaMA-3.1-8B confirms generalizability. Cross-benchmark transfer reveals directional reversal on GSM8K for three families. Multi-seed evaluation ($n\!=\!3$) shows direction is reproducible but magnitude is seed-sensitive.
42	    \item \textbf{Domain-level contamination diagnosis via IRT.} ContamCal embeds multi-signal Reciprocal Rank Fusion (RRF) exposure scores in a contamination-augmented IRT model (2PL+$\gamma$)---an application of standard explanatory IRT \citep{deboeck_2004_explanatory_irt} to LLM contamination---enabling domain-level diagnosis with credible intervals. Domain analysis reveals opposing contamination directions (Social Sciences $\gamma_d < 0$, STEM $\gamma_d > 0$) invisible to aggregate scoring. No item-specific memorization is detected via difference-in-differences (minimum detectable effect size [MDES] 1.25--2.05pp).
43	    \item \textbf{Diagnostic pipeline requirements and signal failure.} Min-K\%++ \citep{zhang_2024_minkpp} exhibits directional reversal at 0.5B (paired Cohen's $d = -1.98$ at d100). RRF-based multi-signal fusion is essential: a single-signal pipeline produces severe model misfit (posterior predictive $p$-value [PPP] $< 0.001$). Simulation establishes $\gamma$ recovery requires $J \geq 50$ at area under the curve (AUC) $\geq 0.55$, above current practice ($J = 8$--$30$).
44	\end{enumerate}
45	
46	\noindent Code and data are available at \url{https://github.com/anonymous-nlp-2026-2/contamcal-irt-calibration}.
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d7bf04d-ab5a-4f02-97c9-eb971d4486ac",
  "isSidechain": true,
  "promptId": "0e067292-b14c-4cc1-af48-ad6fa4c4ff4f",
  "agentId": "a680f27424e263b05",
  "type": "user",
  "uuid": "e95d47d1-5082-459b-b2af-77b1c4f99fd4",
  "sourceToolAssistantUUID": "5d7bf04d-ab5a-4f02-97c9-eb971d4486ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-25T08:43:15.793Z_

Now I have all the data needed to compare. Let me compile the findings.

## Verification Results

### Script 1: `gen_cross_benchmark_heatmap.py` (6x3 delta-acc matrix)

Comparing script data (line 19-26) against registry values provided:

| Model | Benchmark | Script Value | Registry Value | Match? |
|-------|-----------|-------------|----------------|--------|
| OLMo-2 | MMLU | +3.21 | +3.21 | OK |
| OLMo-2 | ARC | +3.92 | +3.92 | OK |
| OLMo-2 | GSM8K | +2.10 | +2.10 | OK |
| Falcon3 | MMLU | +4.19 | +4.19 | OK |
| Falcon3 | ARC | +4.01 | +4.01 | OK |
| Falcon3 | GSM8K | +1.29 | +1.29 | OK |
| Gemma-2 | MMLU | +3.76 | +3.76 | OK |
| Gemma-2 | ARC | -1.20 | -1.20 | OK |
| **Gemma-2** | **GSM8K** | **+1.33** | **excluded (CoT collapse)** | **MISMATCH** |
| Qwen-7B | MMLU | -1.78 | -1.78 | OK |
| Qwen-7B | ARC | -2.90 | -2.90 | OK |
| Qwen-7B | GSM8K | +9.38 | +9.38 | OK |
| Phi-4 | MMLU | -0.17 | -0.17 | OK |
| Phi-4 | ARC | +0.60 | +0.60 | OK |
| Phi-4 | GSM8K | -0.50 | -0.50 | OK |
| Qwen-14B | MMLU | -9.37 | -9.37 | OK |
| Qwen-14B | ARC | -3.40 | -3.40 | OK |
| Qwen-14B | GSM8K | +13.09 | +13.09 | OK |

**Discrepancy 1**: Gemma-2 GSM8K is hardcoded as `+1.33` in the script, but the registry says it should be **excluded due to CoT collapse**. The paper's Table `tab:gsm8k_transfer` explicitly states "Gemma-2 excluded due to CoT collapse under MC-format SFT" and `tab:gsm8k_dose` shows Gemma-2 d000 baseline as 17.82% with "excluded from analysis." The heatmap shows +1.33 as a regular value with no N/A masking. The script has `np.isnan` handling for N/A cells, but Gemma-2 GSM8K is not set to NaN -- it shows a numeric value that contradicts the paper's exclusion.

---

### Script 2: `gen_baseline_vulnerability.py` (Table 1 baselines and deltas)

Comparing against paper Table 1 (`tab:taxonomy`):

| Model | Script Baseline | Paper Base | Script Delta | Paper Delta | Match? |
|-------|----------------|------------|--------------|-------------|--------|
| OLMo-2 7B | 53.79 | 53.8% | +3.21 | +3.2pp | OK (rounding) |
| Falcon3 7B | 58.77 | 58.8% | +4.19 | +4.2pp | OK (rounding) |
| Gemma-2 9B | 61.86 | 61.9% | +3.76 | +3.8pp | OK (rounding) |
| Qwen2.5-7B | 66.11 | 66.1% | -1.78 | -1.8pp | OK (rounding) |
| Phi-4 14.7B | 76.44 | 76.4% | -0.17 | +/-0.5pp | OK |
| Qwen2.5-14B | 69.44 | 69.4% | -9.37 | -9.4pp | OK (rounding) |

Cross-seed ranges in the script (lines 23-29) vs. paper Table 4 (`tab:cross_seed`):

| Model | Script Range | Paper CI | Match? |
|-------|-------------|----------|--------|
| OLMo-2 | (-0.55, +3.21) | [-0.55, +2.60] | **MISMATCH** -- upper bound +3.21 vs +2.60 |
| Falcon3 | (+3.91, +4.19) | [+3.91, +4.19] | OK |
| Gemma-2 | (+1.49, +3.76) | [+1.49, +3.14] | **MISMATCH** -- upper bound +3.76 vs +3.14 |
| Qwen-7B | (-1.78, -0.01) | [-1.82, -0.34] | **MISMATCH** -- both bounds differ |
| Phi-4 | (-0.17, +1.83) | [-0.17, +1.39] | **MISMATCH** -- upper bound +1.83 vs +1.39 |
| Qwen-14B | (-25.03, -9.37) | [-24.99, -10.49] | **MISMATCH** -- both bounds differ |

**Discrepancy 2**: The `cross_seed_ranges` in `gen_baseline_vulnerability.py` do not match the paper's Table 4 CIs for 5 out of 6 models. The script appears to use raw per-seed min/max values (e.g., OLMo-2 upper = +3.21 which is the s42 point estimate, Gemma-2 upper = +3.76 which is also the s42 point estimate), whereas the paper reports BCa bootstrap 95% CIs. These are conceptually different quantities -- the script plots seed range, the paper reports bootstrap CIs. This may be intentional (the scatter plot shows seed range as error bars, not CIs), but the variable name `cross_seed_ranges` vs the paper's "95% CI" column creates a potential confusion. Checking the figure caption reference: the paper Figure 3 caption is not directly visible, but the script generates `fig_baseline_vulnerability` which maps to `fig:baseline_vulnerability`. The paper text says "Figure~\ref{fig:baseline_vulnerability} visualizes how contamination response correlates with baseline accuracy across families" without specifying CI vs range.

However, looking at the cross_seed_ci script (Script 3), which explicitly draws CIs, the values there DO match the paper Table 4. So the baseline_vulnerability script intentionally uses per-seed ranges (not CIs), which is a different but valid visualization choice -- though this should be documented.

---

### Script 3: `gen_fig_cross_seed_ci_v3.py` (Table 4 cross-seed CIs)

| Model | Script CI | Paper Table 4 CI | Match? |
|-------|----------|-------------------|--------|
| Gemma-2 9B | [+1.49, +3.14] | [+1.49, +3.14] | OK |
| Phi-4 14.7B | [-0.17, +1.39] | [-0.17, +1.39] | OK |
| Qwen2.5-14B | [-24.99, -10.49] | [-24.99, -10.49] | OK |
| Qwen2.5-7B | [-1.82, -0.34] | [-1.82, -0.34] | OK |
| OLMo-2 7B | [-0.55, +2.60] | [-0.55, +2.60] | OK |
| Falcon3-7B | [+3.91, +4.19] | [+3.91, +4.19] | OK |

Mean values in the script:

| Model | Script Mean | Plausibility |
|-------|-----------|--------------|
| Qwen2.5-14B | -15.7 | OK (matches appendix text: "MMLU mean Δ = -15.7pp") |
| Qwen2.5-7B | -1.1 | Plausible (mean of s42 -1.78, s123 ~0, s0 ~-1.5) |
| Phi-4 14.7B | +0.73 | OK (matches appendix: "MMLU mean Δ = +0.73pp") |
| OLMo-2 7B | +1.0 | Plausible (mean of +3.21, -0.55, +1.4 = ~1.35; +1.0 is rounded) |
| Gemma-2 9B | +2.4 | OK (matches appendix reference "mean +2.38pp") |
| Falcon3-7B | +4.1 | OK (mean of +3.91 and +4.19 = 4.05, rounded to 4.1) |

All CI values match. No discrepancies in this script.

---

### Script 4: `gen_fig_domain_gamma.py` (Table 18 / tab:domain_gamma)

The script uses J=13 data (as noted in the comment). Comparing against paper Table `tab:domain_gamma` J=13 column:

| Domain | Script gamma | Paper J=13 gamma | Match? |
|--------|-------------|-----------------|--------|
| STEM: Math | 0.499 | +0.50 | OK (rounding) |
| STEM: Science | 0.504 | +0.50 | OK (rounding) |
| STEM: CS/Eng | 0.497 | +0.50 | OK (rounding) |
| Business/Law | 0.044 | +0.04 | OK (rounding) |
| Medical | 0.235 | +0.24 | OK (rounding) |
| Humanities | -0.309 | -0.31 | OK (rounding) |
| Social Sci. | -0.571 | -0.57 | OK (rounding) |

**Discrepancy 3**: The script has 7 domains, but the paper table has **8 domains** (includes "MMLU: Other" with J=13 gamma = +0.13). The "Other" domain is missing from the figure script. The paper's Figure 6 caption says "J=13 Qwen2.5" but only plots 7 domains, omitting "Other." This is not necessarily wrong (figures can omit data for clarity), but it should be noted.

Now checking CIs against the paper. The paper only reports gamma point estimates and P(gamma<0) for J=13, not explicit CI bounds. The CIs in the script are:

| Domain | Script CI | Paper has CI? |
|--------|----------|--------------|
| STEM: Math | [-0.213, 1.203] | Not in table (only point est.) |
| Social Sci. | [-1.054, -0.103] | Not in table for J=13 |

The paper does mention the J=16 Social Sciences CI as [-1.07, -0.19] in the main text. The script uses J=13 values, so [-1.054, -0.103] is a different (wider?) interval as expected with fewer models.

Significance flags: Only Social Sci. is marked `significant=True` in the script. Cross-checking with paper: Social Sci. has P(gamma<0)=99.1% at J=13, which is the strongest signal but technically below Bonferroni threshold. The script marks it as significant (CI excludes zero: [-1.054, -0.103] does exclude zero), which is consistent.

Pooled values: Script has `pooled_gamma = 0.107`, `pooled_ci = [-0.401, 0.625]`. The paper's main analysis reports pooled gamma under different J values but the figure caption says J=13. These values are plausible but not directly verifiable from the table (which shows J=13 and J=16 domain-level, not an explicit J=13 pooled row).

---

## Summary of Discrepancies

1. **`gen_cross_benchmark_heatmap.py` line 22: Gemma-2 GSM8K = +1.33 instead of NaN/excluded.** The paper explicitly excludes Gemma-2 from GSM8K analysis due to CoT collapse (d000 baseline 17.8%). The heatmap should show N/A for this cell, not +1.33. This is the most significant data integrity issue.

2. **`gen_baseline_vulnerability.py` lines 23-29: `cross_seed_ranges` values differ from paper Table 4 CIs for 5/6 models.** The script uses per-seed min/max (raw range) while the paper reports BCa bootstrap 95% CIs. This is likely intentional (scatter plot error bars = seed range, not CI), but the naming and visual interpretation could mislead readers who cross-reference with Table 4.

3. **`gen_fig_domain_gamma.py`: Missing "Other" domain.** The paper table has 8 domains; the figure plots only 7, omitting "MMLU: Other" (J=13 gamma = +0.13, PPP = 0.072 which is below the acceptable threshold). This omission may be deliberate due to the poor PPP, but is worth noting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e95d47d1-5082-459b-b2af-77b1c4f99fd4",
  "isSidechain": true,
  "agentId": "a680f27424e263b05",
  "requestId": "req_011CbNzMhDiTPHVtkcGFfBP2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34f6decd-a535-4fa7-a06b-13a8944307e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "a769fcd1-5e03-46a5-ad4b-aec127005287",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "atomic-stirring-boot",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HwCkAUbmbVP1FYftZKwKDe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1579,
      "cache_read_input_tokens": 66221,
      "output_tokens": 3408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1579
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3408,
          "cache_read_input_tokens": 66221,
          "cache_creation_input_tokens": 1579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1579,
            "ephemeral_1h_input_tokens": 0
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
