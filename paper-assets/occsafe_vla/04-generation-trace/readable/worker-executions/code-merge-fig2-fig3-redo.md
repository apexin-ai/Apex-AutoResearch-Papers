# code merge fig2 fig3 redo

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 80
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/workers/worker_code_merge-fig2-fig3-redo_20260529T022019.log`
- **Structured JSON:** [`e3090123529c35dff6a0.json`](../../sessions/e3/e3090123529c35dff6a0.json)

## Before a recorded user message

80 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
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
  "uuid": "eb896093-df27-4b8d-9c0c-615aa453792c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/memory/"
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
    "resetsAt": 1780027200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "66e7786d-082f-4449-8750-31a2fdb6d345",
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task into parts:

1. Read existing figure scripts and LaTeX files to understand current state
2. Create the combined CAR + factorial figure script
3. Modify LaTeX files
4. Run the script and verify

Let me start by reading the relevant files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "cb68b3a9-9d6e-4a60-89b4-edbd0bf79b2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1pk7xtvS6LcUowPhdxUVn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13885,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13885
      },
      "output_tokens": 20,
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

I'll start by reading all the relevant source files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "329a954b-70d3-490f-9e07-30e2684ea8e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1pk7xtvS6LcUowPhdxUVn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13885,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13885
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — Read · `toolu_01YAHezCwhFjR7otz5ULL6de`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1c_results_bar.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "bc0f67f5-761b-4f74-93e8-75aaa82b6ac8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1pk7xtvS6LcUowPhdxUVn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13885,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13885
      },
      "output_tokens": 20,
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

_source line 7 · 2026-05-29T02:20:34.390Z_

<details><summary>↩ Tool result · `toolu_01YAHezCwhFjR7otz5ULL6de`</summary>

```text
1	"""
2	fig1c_results_bar.py — CAR bar plot, formerly panel (c) of fig1_overview.
3	Split into standalone single-column figure. Data unchanged.
4	"""
5	import matplotlib
6	matplotlib.use('Agg')
7	import matplotlib.pyplot as plt
8	import matplotlib.patches as mpatches
9	from matplotlib.patches import FancyBboxPatch
10	import matplotlib.patheffects as pe
11	import numpy as np
12	
13	COLORS = {
14	    'vanilla':     '#4C72B0',
15	    'full_occ_bn': '#C44E52',
16	    'full_occ_ln': '#E69F00',
17	    'random_occ':  '#55A868',
18	    'detach_bn':   '#8172B3',
19	    'detach_ln':   '#937860',
20	    'depth':       '#CCB974',
21	    'cutoff':      '#64B5CD',
22	}
23	
24	UI = {
25	    'text':         '#2C3E50',
26	    'subtle':       '#95A5A6',
27	}
28	
29	plt.rcParams.update({
30	    'font.family': 'serif',
31	    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
32	    'font.size': 11,
33	    'text.color': UI['text'],
34	    'axes.labelcolor': UI['text'],
35	    'pdf.fonttype': 42,
36	    'ps.fonttype': 42,
37	    'savefig.dpi': 300,
38	    'savefig.bbox': 'tight',
39	    'savefig.pad_inches': 0.05,
40	    'mathtext.fontset': 'cm',
41	})
42	
43	fig, ax_c = plt.subplots(figsize=(3.4, 3.0), dpi=300, facecolor='white')
44	
45	# CORRECTED v2 data (Table 1), grouped by normalization type
46	cdata = [
47	    {'name': 'Full OCC\n(BN, Grad ON)',     'car': 0.725, 'sd': 0.064,
48	     'color': COLORS['full_occ_bn'], 'n_seeds': 3},
49	    {'name': 'Detach OCC\n(BN, Grad OFF)',   'car': 0.767, 'sd': 0.024,
50	     'color': COLORS['detach_bn'],   'n_seeds': 4},
51	    {'name': 'Full OCC+LN\n(LN, Grad ON)',  'car': 0.773, 'sd': 0.027,
52	     'color': COLORS['full_occ_ln'], 'n_seeds': 4},
53	    {'name': 'Detach+LN\n(LN, Grad OFF)',   'car': 0.802, 'sd': 0.024,
54	     'color': COLORS['detach_ln'],   'n_seeds': 3},
55	]
56	vanilla_car = 0.745
57	
58	ax_c.set_xlim(0.655, 0.87)
59	ax_c.set_ylim(-0.8, len(cdata) - 0.2)
60	ax_c.invert_yaxis()
61	ax_c.spines['top'].set_visible(False)
62	ax_c.spines['right'].set_visible(False)
63	ax_c.spines['left'].set_visible(False)
64	ax_c.set_xlabel('Collision Avoidance Rate (CAR)', fontsize=11, fontweight='bold', labelpad=6)
65	
66	# Group background bands
67	ax_c.axhspan(-0.5, 1.5, alpha=0.02, color=COLORS['full_occ_bn'], zorder=0)
68	ax_c.axhspan(1.5, 3.5, alpha=0.02, color=COLORS['full_occ_ln'], zorder=0)
69	ax_c.text(0.865, 0.5, 'BN', fontsize=9.5, color=COLORS['full_occ_bn'], ha='center', va='center',
70	          fontweight='bold', alpha=0.35,
71	          bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))
72	ax_c.text(0.865, 2.5, 'LN', fontsize=9.5, color=COLORS['full_occ_ln'], ha='center', va='center',
73	          fontweight='bold', alpha=0.35,
74	          bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))
75	
76	# Vanilla reference
77	ax_c.axvline(x=vanilla_car, color=COLORS['vanilla'], linestyle='--',
78	             linewidth=1.8, alpha=0.7, zorder=1)
79	ax_c.text(vanilla_car + 0.003, -0.55, f'Vanilla  {vanilla_car:.3f}',
80	          fontsize=10, color=COLORS['vanilla'], va='top', ha='left',
81	          fontweight='bold',
82	          path_effects=[pe.withStroke(linewidth=3, foreground='white')])
83	
84	# Below-baseline shading
85	ax_c.axvspan(0.655, vanilla_car, alpha=0.04, color=COLORS['full_occ_bn'], zorder=0)
86	
87	# Connecting lines: BN pair
88	ax_c.plot([0.725, 0.767], [0, 1], color=COLORS['full_occ_bn'],
89	          lw=1.3, linestyle=':', alpha=0.5, zorder=1)
90	ax_c.text(0.730, 0.55, '$-$4.2 pp', fontsize=9,
91	          color=COLORS['full_occ_bn'], ha='left', va='center',
92	          fontweight='bold', alpha=0.8,
93	          path_effects=[pe.withStroke(linewidth=3, foreground='white')])
94	
95	# LN pair
96	ax_c.plot([0.773, 0.802], [2, 3], color=COLORS['full_occ_ln'],
97	          lw=1.3, linestyle=':', alpha=0.5, zorder=1)
98	ax_c.text(0.778, 2.55, '$-$2.9 pp', fontsize=9,
99	          color=COLORS['full_occ_ln'], ha='left', va='center',
100	          fontweight='bold', alpha=0.8,
101	          path_effects=[pe.withStroke(linewidth=3, foreground='white')])
102	
103	# Plot data
104	for i, d in enumerate(cdata):
105	    ax_c.plot(d['car'], i, 'o', color=d['color'], markersize=9,
106	              markeredgecolor='white', markeredgewidth=1.0, zorder=5)
107	
108	    if d['sd'] is not None:
109	        ax_c.errorbar(d['car'], i, xerr=d['sd'], fmt='none', ecolor=d['color'],
110	                      elinewidth=2.2, capsize=5, capthick=1.6, zorder=4,
111	                      alpha=0.7)
112	
113	    right_x = d['car'] + (d['sd'] if d['sd'] else 0) + 0.006
114	    label_text = f'{d["car"]:.3f} ± {d["sd"]:.3f}' if d['sd'] else f'{d["car"]:.3f}'
115	
116	    ax_c.text(right_x, i + 0.02, label_text, fontsize=9.5, ha='left',
117	              va='center', color=d['color'], fontweight='bold',
118	              path_effects=[pe.withStroke(linewidth=3, foreground='white')])
119	
120	ax_c.set_yticks(list(range(len(cdata))))
121	ax_c.set_yticklabels([d['name'] for d in cdata], fontsize=10, linespacing=1.1)
122	ax_c.tick_params(axis='y', length=0, pad=6)
123	ax_c.tick_params(axis='x', labelsize=10)
124	ax_c.grid(axis='x', alpha=0.10, color='#999', zorder=0)
125	ax_c.set_xticks([0.68, 0.72, 0.76, 0.80, 0.84])
126	
127	plt.tight_layout()
128	
129	# Save
130	out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'
131	fig.savefig(f'{out_dir}/fig1c_results_bar.png', dpi=300, bbox_inches='tight',
132	            pad_inches=0.05, facecolor='white')
133	fig.savefig(f'{out_dir}/fig1c_results_bar.pdf', dpi=300, bbox_inches='tight',
134	            pad_inches=0.05, facecolor='white')
135	plt.close()
136	print("Saved fig1c_results_bar.png and fig1c_results_bar.pdf")
137	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "f7f9e87a-a5c8-4cd2-8f93-e940749cfe43",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1c_results_bar.py",
      "content": "\"\"\"\nfig1c_results_bar.py — CAR bar plot, formerly panel (c) of fig1_overview.\nSplit into standalone single-column figure. Data unchanged.\n\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nfrom matplotlib.patches import FancyBboxPatch\nimport matplotlib.patheffects as pe\nimport numpy as np\n\nCOLORS = {\n    'vanilla':     '#4C72B0',\n    'full_occ_bn': '#C44E52',\n    'full_occ_ln': '#E69F00',\n    'random_occ':  '#55A868',\n    'detach_bn':   '#8172B3',\n    'detach_ln':   '#937860',\n    'depth':       '#CCB974',\n    'cutoff':      '#64B5CD',\n}\n\nUI = {\n    'text':         '#2C3E50',\n    'subtle':       '#95A5A6',\n}\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['Liberation Serif', 'DejaVu Serif'],\n    'font.size': 11,\n    'text.color': UI['text'],\n    'axes.labelcolor': UI['text'],\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'mathtext.fontset': 'cm',\n})\n\nfig, ax_c = plt.subplots(figsize=(3.4, 3.0), dpi=300, facecolor='white')\n\n# CORRECTED v2 data (Table 1), grouped by normalization type\ncdata = [\n    {'name': 'Full OCC\\n(BN, Grad ON)',     'car': 0.725, 'sd': 0.064,\n     'color': COLORS['full_occ_bn'], 'n_seeds': 3},\n    {'name': 'Detach OCC\\n(BN, Grad OFF)',   'car': 0.767, 'sd': 0.024,\n     'color': COLORS['detach_bn'],   'n_seeds': 4},\n    {'name': 'Full OCC+LN\\n(LN, Grad ON)',  'car': 0.773, 'sd': 0.027,\n     'color': COLORS['full_occ_ln'], 'n_seeds': 4},\n    {'name': 'Detach+LN\\n(LN, Grad OFF)',   'car': 0.802, 'sd': 0.024,\n     'color': COLORS['detach_ln'],   'n_seeds': 3},\n]\nvanilla_car = 0.745\n\nax_c.set_xlim(0.655, 0.87)\nax_c.set_ylim(-0.8, len(cdata) - 0.2)\nax_c.invert_yaxis()\nax_c.spines['top'].set_visible(False)\nax_c.spines['right'].set_visible(False)\nax_c.spines['left'].set_visible(False)\nax_c.set_xlabel('Collision Avoidance Rate (CAR)', fontsize=11, fontweight='bold', labelpad=6)\n\n# Group background bands\nax_c.axhspan(-0.5, 1.5, alpha=0.02, color=COLORS['full_occ_bn'], zorder=0)\nax_c.axhspan(1.5, 3.5, alpha=0.02, color=COLORS['full_occ_ln'], zorder=0)\nax_c.text(0.865, 0.5, 'BN', fontsize=9.5, color=COLORS['full_occ_bn'], ha='center', va='center',\n          fontweight='bold', alpha=0.35,\n          bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))\nax_c.text(0.865, 2.5, 'LN', fontsize=9.5, color=COLORS['full_occ_ln'], ha='center', va='center',\n          fontweight='bold', alpha=0.35,\n          bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))\n\n# Vanilla reference\nax_c.axvline(x=vanilla_car, color=COLORS['vanilla'], linestyle='--',\n             linewidth=1.8, alpha=0.7, zorder=1)\nax_c.text(vanilla_car + 0.003, -0.55, f'Vanilla  {vanilla_car:.3f}',\n          fontsize=10, color=COLORS['vanilla'], va='top', ha='left',\n          fontweight='bold',\n          path_effects=[pe.withStroke(linewidth=3, foreground='white')])\n\n# Below-baseline shading\nax_c.axvspan(0.655, vanilla_car, alpha=0.04, color=COLORS['full_occ_bn'], zorder=0)\n\n# Connecting lines: BN pair\nax_c.plot([0.725, 0.767], [0, 1], color=COLORS['full_occ_bn'],\n          lw=1.3, linestyle=':', alpha=0.5, zorder=1)\nax_c.text(0.730, 0.55, '$-$4.2 pp', fontsize=9,\n          color=COLORS['full_occ_bn'], ha='left', va='center',\n          fontweight='bold', alpha=0.8,\n          path_effects=[pe.withStroke(linewidth=3, foreground='white')])\n\n# LN pair\nax_c.plot([0.773, 0.802], [2, 3], color=COLORS['full_occ_ln'],\n          lw=1.3, linestyle=':', alpha=0.5, zorder=1)\nax_c.text(0.778, 2.55, '$-$2.9 pp', fontsize=9,\n          color=COLORS['full_occ_ln'], ha='left', va='center',\n          fontweight='bold', alpha=0.8,\n          path_effects=[pe.withStroke(linewidth=3, foreground='white')])\n\n# Plot data\nfor i, d in enumerate(cdata):\n    ax_c.plot(d['car'], i, 'o', color=d['color'], markersize=9,\n              markeredgecolor='white', markeredgewidth=1.0, zorder=5)\n\n    if d['sd'] is not None:\n        ax_c.errorbar(d['car'], i, xerr=d['sd'], fmt='none', ecolor=d['color'],\n                      elinewidth=2.2, capsize=5, capthick=1.6, zorder=4,\n                      alpha=0.7)\n\n    right_x = d['car'] + (d['sd'] if d['sd'] else 0) + 0.006\n    label_text = f'{d[\"car\"]:.3f} ± {d[\"sd\"]:.3f}' if d['sd'] else f'{d[\"car\"]:.3f}'\n\n    ax_c.text(right_x, i + 0.02, label_text, fontsize=9.5, ha='left',\n              va='center', color=d['color'], fontweight='bold',\n              path_effects=[pe.withStroke(linewidth=3, foreground='white')])\n\nax_c.set_yticks(list(range(len(cdata))))\nax_c.set_yticklabels([d['name'] for d in cdata], fontsize=10, linespacing=1.1)\nax_c.tick_params(axis='y', length=0, pad=6)\nax_c.tick_params(axis='x', labelsize=10)\nax_c.grid(axis='x', alpha=0.10, color='#999', zorder=0)\nax_c.set_xticks([0.68, 0.72, 0.76, 0.80, 0.84])\n\nplt.tight_layout()\n\n# Save\nout_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'\nfig.savefig(f'{out_dir}/fig1c_results_bar.png', dpi=300, bbox_inches='tight',\n            pad_inches=0.05, facecolor='white')\nfig.savefig(f'{out_dir}/fig1c_results_bar.pdf', dpi=300, bbox_inches='tight',\n            pad_inches=0.05, facecolor='white')\nplt.close()\nprint(\"Saved fig1c_results_bar.png and fig1c_results_bar.pdf\")\n",
      "numLines": 137,
      "startLine": 1,
      "totalLines": 137
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01UrZgDGS2JCc2i6u5N9bjVX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig_combined_factorial_gradient.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "c71e8189-783c-4617-b844-0d35ed13c6e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1pk7xtvS6LcUowPhdxUVn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13885,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13885
      },
      "output_tokens": 20,
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

_source line 9 · 2026-05-29T02:20:34.879Z_

<details><summary>↩ Tool result · `toolu_01UrZgDGS2JCc2i6u5N9bjVX`</summary>

```text
1	#!/usr/bin/env python3
2	"""Combined Figure: (a) Factorial 2x2 interaction + (b) Gradient analysis 2x2."""
3	
4	import json
5	import os
6	import numpy as np
7	import matplotlib
8	matplotlib.use('Agg')
9	import matplotlib.pyplot as plt
10	import matplotlib.patheffects as pe
11	import matplotlib.gridspec as gridspec
12	from pathlib import Path
13	
14	# === Global settings ===
15	plt.rcParams.update({
16	    'font.family': 'serif',
17	    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],
18	    'font.size': 7,
19	    'axes.titlesize': 7.5,
20	    'axes.labelsize': 7,
21	    'xtick.labelsize': 6.5,
22	    'ytick.labelsize': 6.5,
23	    'legend.fontsize': 6,
24	    'figure.dpi': 300,
25	    'savefig.dpi': 300,
26	    'savefig.bbox': 'tight',
27	    'savefig.pad_inches': 0.03,
28	    'axes.spines.top': False,
29	    'axes.spines.right': False,
30	    'lines.linewidth': 1.2,
31	    'axes.grid': False,
32	    'axes.linewidth': 0.6,
33	    'pdf.fonttype': 42,
34	    'ps.fonttype': 42,
35	    'mathtext.fontset': 'cm',
36	})
37	
38	# === Colors ===
39	COLORS = {
40	    'vanilla':     '#4C72B0',
41	    'full_occ_bn': '#C44E52',
42	    'full_occ_ln': '#E69F00',
43	    'detach_bn':   '#8172B3',
44	    'detach_ln':   '#937860',
45	}
46	
47	# === Factorial data ===
48	factorial_data = {
49	    'BN': {
50	        'OFF': {'mean': 0.767, 'std': 0.024, 'n': 4},
51	        'ON':  {'mean': 0.725, 'std': 0.064, 'n': 3},
52	    },
53	    'LN': {
54	        'OFF': {'mean': 0.802, 'std': 0.024, 'n': 3},
55	        'ON':  {'mean': 0.773, 'std': 0.027, 'n': 4},
56	    },
57	}
58	VANILLA_CAR = 0.745
59	
60	# === Gradient styles ===
61	GRAD_STYLES = {
62	    'Vanilla v2':      {'color': COLORS['vanilla'],     'ls': ':', 'marker': 'x', 'label': 'Vanilla',        'lw': 1.0, 'ms': 2.5},
63	    'Full OCC BN v2':  {'color': COLORS['full_occ_bn'], 'ls': '-', 'marker': '^', 'label': 'Full OCC (BN)',  'lw': 1.2, 'ms': 2.5},
64	    'Full OCC LN v2':  {'color': COLORS['full_occ_ln'], 'ls': '-', 'marker': 'o', 'label': 'Full OCC (LN)',  'lw': 1.2, 'ms': 2.5},
65	    'Detach BN v2':    {'color': COLORS['detach_bn'],   'ls': '--', 'marker': 'D', 'label': 'Detach (BN)',   'lw': 1.0, 'ms': 2.2},
66	    'Detach LN v2':    {'color': COLORS['detach_ln'],   'ls': '--', 'marker': 's', 'label': 'Detach (LN)',   'lw': 1.0, 'ms': 2.2},
67	}
68	
69	# === Load gradient data ===
70	DATA_DIR = Path('/tmp/gradient_v2_5cond')
71	all_data = {}
72	for fpath in sorted(DATA_DIR.glob('*_gradient_stats.json')):
73	    with open(fpath) as f:
74	        d = json.load(f)
75	    all_data[d['condition']] = d
76	
77	def extract_dino_blocks(per_layer):
78	    blocks = {}
79	    for layer_name, stats in per_layer.items():
80	        if layer_name.startswith('featurizer.blocks.'):
81	            idx = int(layer_name.split('.')[2])
82	            blocks[idx] = stats
83	    return dict(sorted(blocks.items()))
84	
85	dino_data = {}
86	for cond, d in all_data.items():
87	    blocks = extract_dino_blocks(d['per_layer'])
88	    idxs = np.array(sorted(blocks.keys()))
89	    dino_data[cond] = {
90	        'idx': idxs,
91	        'action_norm': np.array([blocks[i]['action_grad_norm_mean'] for i in idxs]),
92	        'action_std':  np.array([blocks[i]['action_grad_norm_std'] for i in idxs]),
93	        'occ_norm':    np.array([blocks[i].get('occ_grad_norm_mean') or 0 for i in idxs], dtype=float),
94	        'occ_std':     np.array([blocks[i].get('occ_grad_norm_std') or 0 for i in idxs], dtype=float),
95	        'cosine':      np.array([blocks[i].get('cosine_sim_mean') or 0 for i in idxs], dtype=float),
96	        'cosine_std':  np.array([blocks[i].get('cosine_sim_std') or 0 for i in idxs], dtype=float),
97	    }
98	
99	vanilla_norms = dino_data['Vanilla v2']['action_norm']
100	
101	# === Figure layout ===
102	fig = plt.figure(figsize=(7.0, 3.4))
103	gs = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[0.33, 0.67], wspace=0.15)
104	
105	# Left: factorial (a)
106	gs_left = gs[0].subgridspec(1, 1)
107	ax_fact = fig.add_subplot(gs_left[0])
108	
109	# Right: gradient 2x2 (b)
110	gs_right = gs[1].subgridspec(2, 2, hspace=0.55, wspace=0.42)
111	ax_b = [[fig.add_subplot(gs_right[r, c]) for c in range(2)] for r in range(2)]
112	
113	# ============================================================
114	# (a) Factorial interaction plot
115	# ============================================================
116	C_BN = COLORS['full_occ_bn']
117	C_LN = COLORS['full_occ_ln']
118	C_VAN = COLORS['vanilla']
119	
120	ax = ax_fact
121	ax.axhspan(0.68, VANILLA_CAR, color=C_BN, alpha=0.03, zorder=0)
122	ax.axhline(y=VANILLA_CAR, color=C_VAN, linestyle=':', linewidth=0.8, alpha=0.5, zorder=1)
123	t_van = ax.text(0.97, VANILLA_CAR + 0.002, 'Vanilla (0.745)', fontsize=6,
124	                color=C_VAN, va='bottom', ha='right',
125	                transform=ax.get_yaxis_transform(), fontweight='medium')
126	t_van.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])
127	
128	x_positions = [0, 1]
129	
130	bn_y = [factorial_data['BN']['OFF']['mean'], factorial_data['BN']['ON']['mean']]
131	bn_err = [factorial_data['BN'][gf]['std'] for gf in ['OFF', 'ON']]
132	ax.errorbar(x_positions, bn_y, yerr=bn_err, color=C_BN,
133	            marker='o', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,
134	            linestyle='-', linewidth=1.4, capsize=3, capthick=0.8,
135	            elinewidth=0.8, label='BatchNorm (BN)', zorder=3)
136	
137	ln_y = [factorial_data['LN']['OFF']['mean'], factorial_data['LN']['ON']['mean']]
138	ln_err = [factorial_data['LN'][gf]['std'] for gf in ['OFF', 'ON']]
139	ax.errorbar(x_positions, ln_y, yerr=ln_err, color=C_LN,
140	            marker='s', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,
141	            linestyle=(0, (4, 2.5)), linewidth=1.4, capsize=3, capthick=0.8,
142	            elinewidth=0.8, label='LayerNorm (LN)', zorder=3)
143	
144	# Delta annotations
145	delta_bn = (factorial_data['BN']['ON']['mean'] - factorial_data['BN']['OFF']['mean']) * 100
146	delta_ln = (factorial_data['LN']['ON']['mean'] - factorial_data['LN']['OFF']['mean']) * 100
147	
148	mid_bn_y = np.mean(bn_y)
149	t_bn = ax.annotate(f'−{abs(delta_bn):.1f} pp', xy=(0.55, mid_bn_y - 0.008),
150	                   fontsize=7, fontweight='bold', color=C_BN, ha='center', va='top', zorder=5)
151	t_bn.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
152	
153	mid_ln_y = np.mean(ln_y)
154	t_ln = ax.annotate(f'−{abs(delta_ln):.1f} pp', xy=(0.45, mid_ln_y + 0.008),
155	                   fontsize=7, fontweight='bold', color=C_LN, ha='center', va='bottom', zorder=5)
156	t_ln.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
157	
158	# n-labels
159	n_offsets = {
160	    ('BN', 'OFF'): (-12, -10),
161	    ('BN', 'ON'):  (12, -14),
162	    ('LN', 'OFF'): (-12, 8),
163	    ('LN', 'ON'):  (12, 10),
164	}
165	for gf_idx, gf in enumerate(['OFF', 'ON']):
166	    for norm in ['BN', 'LN']:
167	        n_val = factorial_data[norm][gf]['n']
168	        y_val = factorial_data[norm][gf]['mean']
169	        ox, oy = n_offsets[(norm, gf)]
170	        c = C_BN if norm == 'BN' else C_LN
171	        ax.annotate(f'n={n_val}', (x_positions[gf_idx], y_val),
172	                    xytext=(ox, oy), textcoords='offset points',
173	                    fontsize=5.5, color=c, ha='center', fontstyle='italic', alpha=0.6)
174	
175	ax.set_xticks(x_positions)
176	ax.set_xticklabels(['OFF\n(Detach)', 'ON\n(Full)'], fontsize=7)
177	ax.set_xlabel('Gradient Flow', fontsize=8)
178	ax.set_ylabel('Collision Avoidance Rate (CAR)', fontsize=8)
179	ax.set_xlim(-0.3, 1.3)
180	ax.set_ylim(0.68, 0.86)
181	ax.yaxis.set_major_locator(plt.MultipleLocator(0.02))
182	ax.legend(loc='upper right', frameon=True, framealpha=0.95, edgecolor='none',
183	          handlelength=2.0, handletextpad=0.4, fontsize=6.5)
184	
185	# Panel label
186	ax.text(-0.18, 1.08, '(a)', transform=ax.transAxes, fontsize=9.5, fontweight='bold', va='top')
187	
188	# ============================================================
189	# (b) Gradient analysis 2x2
190	# ============================================================
191	
192	# --- (b) Panel label on top-left of gradient region ---
193	ax_b[0][0].text(-0.22, 1.18, '(b)', transform=ax_b[0][0].transAxes,
194	                fontsize=9.5, fontweight='bold', va='top')
195	
196	# --- b-i: Action gradient norms ---
197	ax = ax_b[0][0]
198	for cond in ['Vanilla v2', 'Full OCC BN v2', 'Full OCC LN v2', 'Detach BN v2', 'Detach LN v2']:
199	    s = GRAD_STYLES[cond]
200	    d = dino_data[cond]
201	    ax.semilogy(d['idx'], d['action_norm'], color=s['color'], ls=s['ls'],
202	                lw=s['lw'], marker=s['marker'], markersize=s['ms'],
203	                markeredgewidth=0, alpha=0.85, label=s['label'])
204	    ax.fill_between(d['idx'],
205	                    np.maximum(d['action_norm'] - d['action_std'], 1e-4),
206	                    d['action_norm'] + d['action_std'],
207	                    alpha=0.04, color=s['color'])
208	ax.set_ylabel('Gradient L2 norm', fontsize=8)
209	ax.set_title('Action norms', fontsize=9, pad=3)
210	ax.legend(loc='lower left', ncol=2, framealpha=0.95, edgecolor='none', fontsize=7,
211	          columnspacing=0.6, handlelength=1.2, handletextpad=0.3)
212	ax.grid(True, alpha=0.08, axis='y')
213	ax.set_xlim(-0.5, 22.5)
214	ax.tick_params(labelsize=7)
215	
216	# --- b-ii: Auxiliary gradient norms ---
217	ax = ax_b[0][1]
218	for cond in ['Full OCC BN v2', 'Full OCC LN v2']:
219	    s = GRAD_STYLES[cond]
220	    d = dino_data[cond]
221	    mask = d['occ_norm'] > 0
222	    ax.semilogy(d['idx'][mask], d['occ_norm'][mask], color=s['color'], ls=s['ls'],
223	                lw=s['lw'], marker=s['marker'], markersize=s['ms'],
224	                markeredgewidth=0, alpha=0.85, label=s['label'])
225	    ax.fill_between(d['idx'][mask],
226	                    np.maximum(d['occ_norm'][mask] - d['occ_std'][mask], 1e-4),
227	                    d['occ_norm'][mask] + d['occ_std'][mask],
228	                    alpha=0.06, color=s['color'])
229	ax.set_ylabel('Gradient L2 norm', fontsize=8)
230	ax.set_title(r'Aux norms (10$\times$)', fontsize=9, pad=3)
231	ax.grid(True, alpha=0.08, axis='y')
232	ax.set_xlim(-0.5, 22.5)
233	ax.tick_params(labelsize=7)
234	
235	# --- b-iii: Cosine similarity ---
236	ax = ax_b[1][0]
237	for cond in ['Full OCC BN v2', 'Full OCC LN v2']:
238	    s = GRAD_STYLES[cond]
239	    d = dino_data[cond]
240	    mask = d['cosine'] != 0
241	    ax.plot(d['idx'][mask], d['cosine'][mask], color=s['color'], ls=s['ls'],
242	            lw=s['lw'], marker=s['marker'], markersize=s['ms'],
243	            markeredgewidth=0, alpha=0.85, label=s['label'])
244	    ax.fill_between(d['idx'][mask],
245	                    d['cosine'][mask] - d['cosine_std'][mask],
246	                    d['cosine'][mask] + d['cosine_std'][mask],
247	                    alpha=0.03, color=s['color'])
248	ax.axhline(0, color='#888888', linestyle='--', linewidth=0.5, alpha=0.5, zorder=1)
249	ax.set_ylim(-0.15, 0.15)
250	ax.set_xlabel('DINOv2 block index', fontsize=8)
251	ax.set_ylabel('Cosine similarity', fontsize=8)
252	ax.set_title(r'Cosine sim. ($\approx$46% conflict)', fontsize=9, pad=3)
253	ax.grid(True, alpha=0.08, axis='y')
254	ax.set_xlim(-0.5, 22.5)
255	ax.tick_params(labelsize=7)
256	
257	# --- b-iv: Norm ratio ---
258	ax = ax_b[1][1]
259	for cond in ['Full OCC BN v2', 'Full OCC LN v2', 'Detach BN v2', 'Detach LN v2']:
260	    s = GRAD_STYLES[cond]
261	    d = dino_data[cond]
262	    safe_vanilla = np.where(vanilla_norms > 1e-6, vanilla_norms, 1.0)
263	    ratio = d['action_norm'] / safe_vanilla
264	    valid = vanilla_norms > 1e-6
265	    ax.plot(d['idx'][valid], ratio[valid], color=s['color'], ls=s['ls'],
266	            lw=s['lw'], marker=s['marker'], markersize=s['ms'],
267	            markeredgewidth=0, alpha=0.85, label=s['label'])
268	ax.axhline(1.0, color='#888888', linestyle='--', linewidth=0.6, alpha=0.5, zorder=1)
269	ax.set_xlabel('DINOv2 block index', fontsize=8)
270	ax.set_ylabel('Ratio (cond. / Vanilla)', fontsize=8)
271	ax.set_title('Norm ratio', fontsize=9, pad=3)
272	ax.grid(True, alpha=0.08, axis='y')
273	ax.set_xlim(-0.5, 22.5)
274	ax.tick_params(labelsize=7)
275	
276	# Remove x-labels from top row of (b)
277	for c in range(2):
278	    ax_b[0][c].set_xlabel('')
279	
280	# === Save ===
281	OUT_DIR = Path('/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures')
282	for fmt in ['pdf', 'png']:
283	    path = OUT_DIR / f'fig_combined_factorial_gradient.{fmt}'
284	    fig.savefig(path)
285	    print(f'Saved: {path}')
286	plt.close(fig)
287	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "1608e9c7-a587-4ab5-b26c-f26b56517c60",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig_combined_factorial_gradient.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Combined Figure: (a) Factorial 2x2 interaction + (b) Gradient analysis 2x2.\"\"\"\n\nimport json\nimport os\nimport numpy as np\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport matplotlib.gridspec as gridspec\nfrom pathlib import Path\n\n# === Global settings ===\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],\n    'font.size': 7,\n    'axes.titlesize': 7.5,\n    'axes.labelsize': 7,\n    'xtick.labelsize': 6.5,\n    'ytick.labelsize': 6.5,\n    'legend.fontsize': 6,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.03,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'lines.linewidth': 1.2,\n    'axes.grid': False,\n    'axes.linewidth': 0.6,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'mathtext.fontset': 'cm',\n})\n\n# === Colors ===\nCOLORS = {\n    'vanilla':     '#4C72B0',\n    'full_occ_bn': '#C44E52',\n    'full_occ_ln': '#E69F00',\n    'detach_bn':   '#8172B3',\n    'detach_ln':   '#937860',\n}\n\n# === Factorial data ===\nfactorial_data = {\n    'BN': {\n        'OFF': {'mean': 0.767, 'std': 0.024, 'n': 4},\n        'ON':  {'mean': 0.725, 'std': 0.064, 'n': 3},\n    },\n    'LN': {\n        'OFF': {'mean': 0.802, 'std': 0.024, 'n': 3},\n        'ON':  {'mean': 0.773, 'std': 0.027, 'n': 4},\n    },\n}\nVANILLA_CAR = 0.745\n\n# === Gradient styles ===\nGRAD_STYLES = {\n    'Vanilla v2':      {'color': COLORS['vanilla'],     'ls': ':', 'marker': 'x', 'label': 'Vanilla',        'lw': 1.0, 'ms': 2.5},\n    'Full OCC BN v2':  {'color': COLORS['full_occ_bn'], 'ls': '-', 'marker': '^', 'label': 'Full OCC (BN)',  'lw': 1.2, 'ms': 2.5},\n    'Full OCC LN v2':  {'color': COLORS['full_occ_ln'], 'ls': '-', 'marker': 'o', 'label': 'Full OCC (LN)',  'lw': 1.2, 'ms': 2.5},\n    'Detach BN v2':    {'color': COLORS['detach_bn'],   'ls': '--', 'marker': 'D', 'label': 'Detach (BN)',   'lw': 1.0, 'ms': 2.2},\n    'Detach LN v2':    {'color': COLORS['detach_ln'],   'ls': '--', 'marker': 's', 'label': 'Detach (LN)',   'lw': 1.0, 'ms': 2.2},\n}\n\n# === Load gradient data ===\nDATA_DIR = Path('/tmp/gradient_v2_5cond')\nall_data = {}\nfor fpath in sorted(DATA_DIR.glob('*_gradient_stats.json')):\n    with open(fpath) as f:\n        d = json.load(f)\n    all_data[d['condition']] = d\n\ndef extract_dino_blocks(per_layer):\n    blocks = {}\n    for layer_name, stats in per_layer.items():\n        if layer_name.startswith('featurizer.blocks.'):\n            idx = int(layer_name.split('.')[2])\n            blocks[idx] = stats\n    return dict(sorted(blocks.items()))\n\ndino_data = {}\nfor cond, d in all_data.items():\n    blocks = extract_dino_blocks(d['per_layer'])\n    idxs = np.array(sorted(blocks.keys()))\n    dino_data[cond] = {\n        'idx': idxs,\n        'action_norm': np.array([blocks[i]['action_grad_norm_mean'] for i in idxs]),\n        'action_std':  np.array([blocks[i]['action_grad_norm_std'] for i in idxs]),\n        'occ_norm':    np.array([blocks[i].get('occ_grad_norm_mean') or 0 for i in idxs], dtype=float),\n        'occ_std':     np.array([blocks[i].get('occ_grad_norm_std') or 0 for i in idxs], dtype=float),\n        'cosine':      np.array([blocks[i].get('cosine_sim_mean') or 0 for i in idxs], dtype=float),\n        'cosine_std':  np.array([blocks[i].get('cosine_sim_std') or 0 for i in idxs], dtype=float),\n    }\n\nvanilla_norms = dino_data['Vanilla v2']['action_norm']\n\n# === Figure layout ===\nfig = plt.figure(figsize=(7.0, 3.4))\ngs = gridspec.GridSpec(1, 2, figure=fig, width_ratios=[0.33, 0.67], wspace=0.15)\n\n# Left: factorial (a)\ngs_left = gs[0].subgridspec(1, 1)\nax_fact = fig.add_subplot(gs_left[0])\n\n# Right: gradient 2x2 (b)\ngs_right = gs[1].subgridspec(2, 2, hspace=0.55, wspace=0.42)\nax_b = [[fig.add_subplot(gs_right[r, c]) for c in range(2)] for r in range(2)]\n\n# ============================================================\n# (a) Factorial interaction plot\n# ============================================================\nC_BN = COLORS['full_occ_bn']\nC_LN = COLORS['full_occ_ln']\nC_VAN = COLORS['vanilla']\n\nax = ax_fact\nax.axhspan(0.68, VANILLA_CAR, color=C_BN, alpha=0.03, zorder=0)\nax.axhline(y=VANILLA_CAR, color=C_VAN, linestyle=':', linewidth=0.8, alpha=0.5, zorder=1)\nt_van = ax.text(0.97, VANILLA_CAR + 0.002, 'Vanilla (0.745)', fontsize=6,\n                color=C_VAN, va='bottom', ha='right',\n                transform=ax.get_yaxis_transform(), fontweight='medium')\nt_van.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])\n\nx_positions = [0, 1]\n\nbn_y = [factorial_data['BN']['OFF']['mean'], factorial_data['BN']['ON']['mean']]\nbn_err = [factorial_data['BN'][gf]['std'] for gf in ['OFF', 'ON']]\nax.errorbar(x_positions, bn_y, yerr=bn_err, color=C_BN,\n            marker='o', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,\n            linestyle='-', linewidth=1.4, capsize=3, capthick=0.8,\n            elinewidth=0.8, label='BatchNorm (BN)', zorder=3)\n\nln_y = [factorial_data['LN']['OFF']['mean'], factorial_data['LN']['ON']['mean']]\nln_err = [factorial_data['LN'][gf]['std'] for gf in ['OFF', 'ON']]\nax.errorbar(x_positions, ln_y, yerr=ln_err, color=C_LN,\n            marker='s', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,\n            linestyle=(0, (4, 2.5)), linewidth=1.4, capsize=3, capthick=0.8,\n            elinewidth=0.8, label='LayerNorm (LN)', zorder=3)\n\n# Delta annotations\ndelta_bn = (factorial_data['BN']['ON']['mean'] - factorial_data['BN']['OFF']['mean']) * 100\ndelta_ln = (factorial_data['LN']['ON']['mean'] - factorial_data['LN']['OFF']['mean']) * 100\n\nmid_bn_y = np.mean(bn_y)\nt_bn = ax.annotate(f'−{abs(delta_bn):.1f} pp', xy=(0.55, mid_bn_y - 0.008),\n                   fontsize=7, fontweight='bold', color=C_BN, ha='center', va='top', zorder=5)\nt_bn.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\nmid_ln_y = np.mean(ln_y)\nt_ln = ax.annotate(f'−{abs(delta_ln):.1f} pp', xy=(0.45, mid_ln_y + 0.008),\n                   fontsize=7, fontweight='bold', color=C_LN, ha='center', va='bottom', zorder=5)\nt_ln.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\n# n-labels\nn_offsets = {\n    ('BN', 'OFF'): (-12, -10),\n    ('BN', 'ON'):  (12, -14),\n    ('LN', 'OFF'): (-12, 8),\n    ('LN', 'ON'):  (12, 10),\n}\nfor gf_idx, gf in enumerate(['OFF', 'ON']):\n    for norm in ['BN', 'LN']:\n        n_val = factorial_data[norm][gf]['n']\n        y_val = factorial_data[norm][gf]['mean']\n        ox, oy = n_offsets[(norm, gf)]\n        c = C_BN if norm == 'BN' else C_LN\n        ax.annotate(f'n={n_val}', (x_positions[gf_idx], y_val),\n                    xytext=(ox, oy), textcoords='offset points',\n                    fontsize=5.5, color=c, ha='center', fontstyle='italic', alpha=0.6)\n\nax.set_xticks(x_positions)\nax.set_xticklabels(['OFF\\n(Detach)', 'ON\\n(Full)'], fontsize=7)\nax.set_xlabel('Gradient Flow', fontsize=8)\nax.set_ylabel('Collision Avoidance Rate (CAR)', fontsize=8)\nax.set_xlim(-0.3, 1.3)\nax.set_ylim(0.68, 0.86)\nax.yaxis.set_major_locator(plt.MultipleLocator(0.02))\nax.legend(loc='upper right', frameon=True, framealpha=0.95, edgecolor='none',\n          handlelength=2.0, handletextpad=0.4, fontsize=6.5)\n\n# Panel label\nax.text(-0.18, 1.08, '(a)', transform=ax.transAxes, fontsize=9.5, fontweight='bold', va='top')\n\n# ============================================================\n# (b) Gradient analysis 2x2\n# ============================================================\n\n# --- (b) Panel label on top-left of gradient region ---\nax_b[0][0].text(-0.22, 1.18, '(b)', transform=ax_b[0][0].transAxes,\n                fontsize=9.5, fontweight='bold', va='top')\n\n# --- b-i: Action gradient norms ---\nax = ax_b[0][0]\nfor cond in ['Vanilla v2', 'Full OCC BN v2', 'Full OCC LN v2', 'Detach BN v2', 'Detach LN v2']:\n    s = GRAD_STYLES[cond]\n    d = dino_data[cond]\n    ax.semilogy(d['idx'], d['action_norm'], color=s['color'], ls=s['ls'],\n                lw=s['lw'], marker=s['marker'], markersize=s['ms'],\n                markeredgewidth=0, alpha=0.85, label=s['label'])\n    ax.fill_between(d['idx'],\n                    np.maximum(d['action_norm'] - d['action_std'], 1e-4),\n                    d['action_norm'] + d['action_std'],\n                    alpha=0.04, color=s['color'])\nax.set_ylabel('Gradient L2 norm', fontsize=8)\nax.set_title('Action norms', fontsize=9, pad=3)\nax.legend(loc='lower left', ncol=2, framealpha=0.95, edgecolor='none', fontsize=7,\n          columnspacing=0.6, handlelength=1.2, handletextpad=0.3)\nax.grid(True, alpha=0.08, axis='y')\nax.set_xlim(-0.5, 22.5)\nax.tick_params(labelsize=7)\n\n# --- b-ii: Auxiliary gradient norms ---\nax = ax_b[0][1]\nfor cond in ['Full OCC BN v2', 'Full OCC LN v2']:\n    s = GRAD_STYLES[cond]\n    d = dino_data[cond]\n    mask = d['occ_norm'] > 0\n    ax.semilogy(d['idx'][mask], d['occ_norm'][mask], color=s['color'], ls=s['ls'],\n                lw=s['lw'], marker=s['marker'], markersize=s['ms'],\n                markeredgewidth=0, alpha=0.85, label=s['label'])\n    ax.fill_between(d['idx'][mask],\n                    np.maximum(d['occ_norm'][mask] - d['occ_std'][mask], 1e-4),\n                    d['occ_norm'][mask] + d['occ_std'][mask],\n                    alpha=0.06, color=s['color'])\nax.set_ylabel('Gradient L2 norm', fontsize=8)\nax.set_title(r'Aux norms (10$\\times$)', fontsize=9, pad=3)\nax.grid(True, alpha=0.08, axis='y')\nax.set_xlim(-0.5, 22.5)\nax.tick_params(labelsize=7)\n\n# --- b-iii: Cosine similarity ---\nax = ax_b[1][0]\nfor cond in ['Full OCC BN v2', 'Full OCC LN v2']:\n    s = GRAD_STYLES[cond]\n    d = dino_data[cond]\n    mask = d['cosine'] != 0\n    ax.plot(d['idx'][mask], d['cosine'][mask], color=s['color'], ls=s['ls'],\n            lw=s['lw'], marker=s['marker'], markersize=s['ms'],\n            markeredgewidth=0, alpha=0.85, label=s['label'])\n    ax.fill_between(d['idx'][mask],\n                    d['cosine'][mask] - d['cosine_std'][mask],\n                    d['cosine'][mask] + d['cosine_std'][mask],\n                    alpha=0.03, color=s['color'])\nax.axhline(0, color='#888888', linestyle='--', linewidth=0.5, alpha=0.5, zorder=1)\nax.set_ylim(-0.15, 0.15)\nax.set_xlabel('DINOv2 block index', fontsize=8)\nax.set_ylabel('Cosine similarity', fontsize=8)\nax.set_title(r'Cosine sim. ($\\approx$46% conflict)', fontsize=9, pad=3)\nax.grid(True, alpha=0.08, axis='y')\nax.set_xlim(-0.5, 22.5)\nax.tick_params(labelsize=7)\n\n# --- b-iv: Norm ratio ---\nax = ax_b[1][1]\nfor cond in ['Full OCC BN v2', 'Full OCC LN v2', 'Detach BN v2', 'Detach LN v2']:\n    s = GRAD_STYLES[cond]\n    d = dino_data[cond]\n    safe_vanilla = np.where(vanilla_norms > 1e-6, vanilla_norms, 1.0)\n    ratio = d['action_norm'] / safe_vanilla\n    valid = vanilla_norms > 1e-6\n    ax.plot(d['idx'][valid], ratio[valid], color=s['color'], ls=s['ls'],\n            lw=s['lw'], marker=s['marker'], markersize=s['ms'],\n            markeredgewidth=0, alpha=0.85, label=s['label'])\nax.axhline(1.0, color='#888888', linestyle='--', linewidth=0.6, alpha=0.5, zorder=1)\nax.set_xlabel('DINOv2 block index', fontsize=8)\nax.set_ylabel('Ratio (cond. / Vanilla)', fontsize=8)\nax.set_title('Norm ratio', fontsize=9, pad=3)\nax.grid(True, alpha=0.08, axis='y')\nax.set_xlim(-0.5, 22.5)\nax.tick_params(labelsize=7)\n\n# Remove x-labels from top row of (b)\nfor c in range(2):\n    ax_b[0][c].set_xlabel('')\n\n# === Save ===\nOUT_DIR = Path('/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures')\nfor fmt in ['pdf', 'png']:\n    path = OUT_DIR / f'fig_combined_factorial_gradient.{fmt}'\n    fig.savefig(path)\n    print(f'Saved: {path}')\nplt.close(fig)\n",
      "numLines": 287,
      "startLine": 1,
      "totalLines": 287
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01K9GwFGwHuMN1pGJjDeGMD5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "1f05c195-2fe0-4c64-838f-06ef2aa5f01a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1pk7xtvS6LcUowPhdxUVn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13885,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13885
      },
      "output_tokens": 20,
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

_source line 11 · 2026-05-29T02:20:35.392Z_

<details><summary>↩ Tool result · `toolu_01K9GwFGwHuMN1pGJjDeGMD5`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Main Results}
6	
7	Table~\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\times$ 10 tasks per seed). $\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\star$) uses v1 code but is included above the midrule as a factorial control; its $\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use permutation tests and Hedges' $g$ (bias-corrected effect size for small samples) against the Vanilla baseline.
8	
9	\textbf{Detach+LN reliably outperforms Vanilla.} The best factorial configuration---detached gradients with LayerNorm---achieves CAR $0.802 \pm 0.024$ ($n{=}3$), a $+5.7$\,pp advantage over Vanilla ($0.745 \pm 0.024$, $n{=}3$; Hedges' $g{=}1.89$, very large; bootstrap 95\% CI for $\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$).
10	
11	\textbf{Two additive main effects explain the advantage.} The $2{\times}2$ factorial (Table~\ref{tab:factorial}, Figure~\ref{fig:factorial_gradient}a) reveals two large main effects with negligible interaction (permutation ANOVA, 10{,}000 permutations: gradient flow $p_\text{perm}{=}0.050$; normalization $p_\text{perm}{=}0.018$; interaction $p_\text{perm}{=}0.774$; Appendix~\ref{app:permutation}). Parametric ANOVA yields consistent trends (Appendix~\ref{app:stat_power}). Under BatchNorm, gradient flow corresponds to lower safety: Full OCC (CAR $0.725$, $\Delta{=}-2.0$\,pp) is the sole cell below Vanilla, while Detach OCC recovers ($0.767$, $\Delta{=}+2.2$\,pp); the within-row deficit is 4.2\,pp (Hedges' $g{=}0.78$, large). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.773$, $\Delta{=}+2.8$\,pp, $g{=}+0.90$) exceeds Vanilla, and Detach+LN yields the highest mean ($0.802 \pm 0.024$, $\Delta{=}+5.7$\,pp, $g{=}+1.89$). LN provides a consistent 3.5--4.8\,pp advantage over BN ($g{=}0.88$--$1.24$). The BN + gradient flow cell exhibits the highest instability ($\sigma{=}0.064$, ${\geq}\,2{\times}$ all others; $\sigma \leq 0.027$ for all other cells). After Bonferroni correction for all pairwise comparisons, no individual Welch $t$-test reaches $\alpha{=}0.05$, consistent with $n{=}3$--$4$; we report effect sizes and planned-comparison bootstrap CIs (Appendix~\ref{app:stat_power}). The normalization main effect reaches significance under permutation testing ($p_\text{perm}{=}0.018$). Both effects amplify ${\approx}3{\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\ref{app:per_task_factorial}). Spatial content does not detectably affect outcomes: Full OCC, Random OCC, and Depth fall within cross-seed variance ($p > 0.4$, observed under v1 for Random OCC and Depth).
12	
13	\textbf{BN + gradient flow is associated with training instability.} Full OCC (BN) individual seeds range from $0.776$ (near Vanilla) to $0.654$ ($\Delta{=}-9.1$\,pp), spanning $12.2$\,pp---more than double the range of any other cell. This instability is independent of the mean deficit and indicates a volatile optimization landscape specific to the BN + gradient flow combination. No other cell approaches this variance ($\sigma \leq 0.027$ vs.\ $\sigma{=}0.064$), consistent with BatchNorm's running-statistics mechanism amplifying stochastic sensitivity when auxiliary gradients flow through the shared encoders. Notably, TSR remains relatively stable across all conditions ($0.854$--$0.914$), indicating that the safety deficit is not accompanied by a proportional decline in task completion ability.
14	
15	
16	\begin{table}[t]
17	\centering
18	\caption{Results on SafeLIBERO Level~I (10 tasks, 50 rollouts/seed). Mean $\pm$ SD across seeds. $\Delta$CAR vs.\ v2 Vanilla ($0.745$) for factorial conditions; vs.\ v1 Vanilla ($0.780$) for supplementary. $^{a}$Highest variance. $^\ddagger$2 seeds. $^\star$v1 code.}
19	\label{tab:main_results}
20	\small
21	\setlength{\tabcolsep}{3pt}
22	\begin{tabular}{llcccl}
23	\toprule
24	Flow & Norm & $n$ & CAR & TSR & $\Delta$CAR \\
25	\midrule
26	\multicolumn{6}{l}{\textit{$2{\times}2$ factorial (v2 code)}} \\
27	ON  & BN & 3 & $0.725 \pm 0.064^{a}$ & $0.854 \pm 0.052$ & $-$2.0 \\
28	OFF & BN & 4 & $0.767 \pm 0.024$ & $0.908 \pm 0.026$ & $+$2.2 \\
29	ON  & LN & 4 & $0.773 \pm 0.027$ & $0.914 \pm 0.049$ & $+$2.8 \\
30	OFF & LN & 3 & $0.802 \pm 0.024$ & $0.911 \pm 0.018$ & $+$5.7 \\
31	\addlinespace
32	---  & Vanilla & 3 & $0.745 \pm 0.024$ & $0.878 \pm 0.032$ & --- \\
33	\midrule
34	\multicolumn{6}{l}{\textit{Controls \& supplementary (v1 code)}} \\
35	ON  & BN (Random)$^\star$ & 3 & $0.789 \pm 0.031$ & $0.869 \pm 0.029$ & --- \\
36	ON  & --- (Depth)$^\star$ & 4 & $0.780 \pm 0.039$ & $0.889 \pm 0.042$ & $0.0$ \\
37	ON  & BN (Cutoff@15K)$^\ddagger$ & 2 & $0.782 \pm 0.031$ & $0.883 \pm 0.041$ & $+$0.2 \\
38	ON  & BN (Cutoff@25K)$^\ddagger$ & 2 & $0.724 \pm 0.051$ & $0.887 \pm 0.061$ & $-$5.6 \\
39	ON  & BN (Cutoff@35K)       & 3 & $0.779 \pm 0.017$ & $0.933 \pm 0.032$ & $-$0.1 \\
40	ON  & BN (Cutoff@45K)       & 1 & $0.764$           & $0.896$           & $-$1.6 \\
41	ON  & BN (Rev.\ Cutoff)$^\ddagger$ & 2 & $0.718 \pm 0.025$ & $0.839 \pm 0.072$ & $-$6.2 \\
42	\bottomrule
43	\end{tabular}
44	\end{table}
45	
46	\begin{table}[t]
47	\centering
48	\caption{$2{\times}2$ factorial: normalization type $\times$ gradient flow (all v2 data). Two main effects: gradient flow under BN $g{=}0.78$ (large); normalization effect $g{=}0.88$--$1.24$ (large to very large). BN + gradient flow is the sole cell below Vanilla. interaction $p_\text{perm}{=}0.774$.}
49	\label{tab:factorial}
50	\begin{tabular}{lccc}
51	\toprule
52	 & Gradient ON & Gradient OFF & $\Delta$(ON$-$OFF) \\
53	\midrule
54	BatchNorm    & Full OCC (0.725) & Detach OCC (0.767) & $-$4.2 \\
55	LayerNorm    & Full OCC+LN (0.773) & Detach+LN (0.802) & $-$2.9 \\
56	\midrule
57	$\Delta$(BN$-$LN) & $-$4.8 ($g{=}{-}0.88$) & $-$3.5 ($g{=}{-}1.24$) & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	% Old Fig 2 (factorial standalone) — merged into fig:factorial_gradient below
63	% \begin{figure}[t]
64	% \centering
65	% \includegraphics[width=\columnwidth]{figures/factorial_2x2_pb.pdf}
66	% \caption{...}
67	% \label{fig:factorial_old}
68	% \end{figure}
69	
70	\begin{figure*}[t]
71	\centering
72	\includegraphics[width=\textwidth]{figures/fig_combined_factorial_gradient.pdf}
73	\caption{(a)~$2{\times}2$ factorial comparison: normalization type (BN/LN) $\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\,pp lower CAR ($g{=}0.78$); LN row: 2.9\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline. Error bars: cross-seed SD ($n{=}3$--$4$ per cell). (b)~Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\approx}$46\% conflict rate), confirming orthogonality.}
74	\label{fig:factorial_gradient}
75	\end{figure*}
76	
77	\subsection{Factorial Interpretation}
78	\label{sec:mechanism}
79	
80	\textbf{Gradient flow is associated with lower safety under BatchNorm but not under LayerNorm.} The BN row provides the clearest signal: Full OCC (BN) is the sole factorial cell falling below Vanilla ($\Delta{=}-2.0$\,pp, $g{=}-0.34$ vs.\ Vanilla), whereas Detach OCC recovers above it ($\Delta{=}+2.2$\,pp, $g{=}+0.74$, large). In the LN row, Full OCC+LN already exceeds Vanilla ($0.773$, $g{=}+0.90$, large), and Detach+LN yields the highest cell mean ($0.802$, $g{=}+1.89$, very large; bootstrap 95\% CI for $\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$). This is a practical threshold crossing---only BN + gradient flow is associated with reduced safety---rather than a statistical interaction (the factorial interaction is negligible, $\eta^2{=}0.005$). The numerical advantage of Detach OCC ($+$2.2\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.
81	
82	\textbf{Temporal dynamics.} Cutoff conditions illuminate when gradient flow's association with lower safety emerges. Cutoff@15K ($\Delta{=}+0.2$\,pp) performs near Vanilla, while Cutoff@25K shows a large deficit ($\Delta{=}-5.6$\,pp) and Cutoff@35K returns to baseline ($\Delta{=}-0.1$\,pp). Cutoff@45K ($\Delta{=}-1.6$\,pp, single seed) falls between these extremes. This non-monotonic pattern suggests that the critical window for gradient flow damage is not simply cumulative exposure but depends on the training phase. Reverse Cutoff (gradient flow only after step 35K) produces the worst supplementary result ($\Delta{=}-6.2$\,pp), indicating that late-stage gradient flow---when the model is refining action predictions---is associated with substantially worse outcomes than early exposure during initial representation learning. However, temporal conditions use 1--3 seeds under v1, so these observations are preliminary; targeted replication under v2 with more seeds would be needed to confirm the temporal pattern.
83	
84	\subsection{Gradient Dynamics}
85	
86	Gradient analysis (Figure~\ref{fig:factorial_gradient}b) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).
87	
88	% Old Fig 3 (gradient standalone) — merged into fig:factorial_gradient above
89	% \begin{figure}[t]
90	% \centering
91	% \includegraphics[width=\textwidth]{figures/gradient_analysis_v2_combined.pdf}
92	% \caption{...}
93	% \label{fig:gradient_analysis_old}
94	% \end{figure}
95	
96	\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\ref{fig:factorial_gradient}b), with conflict rates of ${\approx}$46\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (Figure~\ref{fig:factorial_gradient}b), ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)
97	
98	\textbf{Mechanism remains open.} The observed effect pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The observed effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. Centered Kernel Alignment (CKA) analysis~\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\geq$ 0.95 for both DINOv2 and SigLIP across all encoder layers), localizing the safety deficit to optimization dynamics rather than representational corruption. This high representational similarity is notable: even the worst-performing condition (Full OCC, BN) produces encoder features nearly identical to Vanilla, yet its action policy exhibits substantially worse collision avoidance. The dissociation between representational similarity and behavioral safety suggests that subtle differences in the LoRA adapter weights---invisible to CKA---drive the safety deficit.
99	
100	Additional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\ref{app:additional}.
101	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "98cd7752-34c4-4b1f-81db-5d58efd239e5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use permutation tests and Hedges' $g$ (bias-corrected effect size for small samples) against the Vanilla baseline.\n\n\\textbf{Detach+LN reliably outperforms Vanilla.} The best factorial configuration---detached gradients with LayerNorm---achieves CAR $0.802 \\pm 0.024$ ($n{=}3$), a $+5.7$\\,pp advantage over Vanilla ($0.745 \\pm 0.024$, $n{=}3$; Hedges' $g{=}1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$).\n\n\\textbf{Two additive main effects explain the advantage.} The $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial_gradient}a) reveals two large main effects with negligible interaction (permutation ANOVA, 10{,}000 permutations: gradient flow $p_\\text{perm}{=}0.050$; normalization $p_\\text{perm}{=}0.018$; interaction $p_\\text{perm}{=}0.774$; Appendix~\\ref{app:permutation}). Parametric ANOVA yields consistent trends (Appendix~\\ref{app:stat_power}). Under BatchNorm, gradient flow corresponds to lower safety: Full OCC (CAR $0.725$, $\\Delta{=}-2.0$\\,pp) is the sole cell below Vanilla, while Detach OCC recovers ($0.767$, $\\Delta{=}+2.2$\\,pp); the within-row deficit is 4.2\\,pp (Hedges' $g{=}0.78$, large). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.773$, $\\Delta{=}+2.8$\\,pp, $g{=}+0.90$) exceeds Vanilla, and Detach+LN yields the highest mean ($0.802 \\pm 0.024$, $\\Delta{=}+5.7$\\,pp, $g{=}+1.89$). LN provides a consistent 3.5--4.8\\,pp advantage over BN ($g{=}0.88$--$1.24$). The BN + gradient flow cell exhibits the highest instability ($\\sigma{=}0.064$, ${\\geq}\\,2{\\times}$ all others; $\\sigma \\leq 0.027$ for all other cells). After Bonferroni correction for all pairwise comparisons, no individual Welch $t$-test reaches $\\alpha{=}0.05$, consistent with $n{=}3$--$4$; we report effect sizes and planned-comparison bootstrap CIs (Appendix~\\ref{app:stat_power}). The normalization main effect reaches significance under permutation testing ($p_\\text{perm}{=}0.018$). Both effects amplify ${\\approx}3{\\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\\ref{app:per_task_factorial}). Spatial content does not detectably affect outcomes: Full OCC, Random OCC, and Depth fall within cross-seed variance ($p > 0.4$, observed under v1 for Random OCC and Depth).\n\n\\textbf{BN + gradient flow is associated with training instability.} Full OCC (BN) individual seeds range from $0.776$ (near Vanilla) to $0.654$ ($\\Delta{=}-9.1$\\,pp), spanning $12.2$\\,pp---more than double the range of any other cell. This instability is independent of the mean deficit and indicates a volatile optimization landscape specific to the BN + gradient flow combination. No other cell approaches this variance ($\\sigma \\leq 0.027$ vs.\\ $\\sigma{=}0.064$), consistent with BatchNorm's running-statistics mechanism amplifying stochastic sensitivity when auxiliary gradients flow through the shared encoders. Notably, TSR remains relatively stable across all conditions ($0.854$--$0.914$), indicating that the safety deficit is not accompanied by a proportional decline in task completion ability.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Results on SafeLIBERO Level~I (10 tasks, 50 rollouts/seed). Mean $\\pm$ SD across seeds. $\\Delta$CAR vs.\\ v2 Vanilla ($0.745$) for factorial conditions; vs.\\ v1 Vanilla ($0.780$) for supplementary. $^{a}$Highest variance. $^\\ddagger$2 seeds. $^\\star$v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\nFlow & Norm & $n$ & CAR & TSR & $\\Delta$CAR \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$2{\\times}2$ factorial (v2 code)}} \\\\\nON  & BN & 3 & $0.725 \\pm 0.064^{a}$ & $0.854 \\pm 0.052$ & $-$2.0 \\\\\nOFF & BN & 4 & $0.767 \\pm 0.024$ & $0.908 \\pm 0.026$ & $+$2.2 \\\\\nON  & LN & 4 & $0.773 \\pm 0.027$ & $0.914 \\pm 0.049$ & $+$2.8 \\\\\nOFF & LN & 3 & $0.802 \\pm 0.024$ & $0.911 \\pm 0.018$ & $+$5.7 \\\\\n\\addlinespace\n---  & Vanilla & 3 & $0.745 \\pm 0.024$ & $0.878 \\pm 0.032$ & --- \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Controls \\& supplementary (v1 code)}} \\\\\nON  & BN (Random)$^\\star$ & 3 & $0.789 \\pm 0.031$ & $0.869 \\pm 0.029$ & --- \\\\\nON  & --- (Depth)$^\\star$ & 4 & $0.780 \\pm 0.039$ & $0.889 \\pm 0.042$ & $0.0$ \\\\\nON  & BN (Cutoff@15K)$^\\ddagger$ & 2 & $0.782 \\pm 0.031$ & $0.883 \\pm 0.041$ & $+$0.2 \\\\\nON  & BN (Cutoff@25K)$^\\ddagger$ & 2 & $0.724 \\pm 0.051$ & $0.887 \\pm 0.061$ & $-$5.6 \\\\\nON  & BN (Cutoff@35K)       & 3 & $0.779 \\pm 0.017$ & $0.933 \\pm 0.032$ & $-$0.1 \\\\\nON  & BN (Cutoff@45K)       & 1 & $0.764$           & $0.896$           & $-$1.6 \\\\\nON  & BN (Rev.\\ Cutoff)$^\\ddagger$ & 2 & $0.718 \\pm 0.025$ & $0.839 \\pm 0.072$ & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow (all v2 data). Two main effects: gradient flow under BN $g{=}0.78$ (large); normalization effect $g{=}0.88$--$1.24$ (large to very large). BN + gradient flow is the sole cell below Vanilla. interaction $p_\\text{perm}{=}0.774$.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (0.767) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.773) & Detach+LN (0.802) & $-$2.9 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$4.8 ($g{=}{-}0.88$) & $-$3.5 ($g{=}{-}1.24$) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% Old Fig 2 (factorial standalone) — merged into fig:factorial_gradient below\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\columnwidth]{figures/factorial_2x2_pb.pdf}\n% \\caption{...}\n% \\label{fig:factorial_old}\n% \\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_combined_factorial_gradient.pdf}\n\\caption{(a)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline. Error bars: cross-seed SD ($n{=}3$--$4$ per cell). (b)~Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\\approx}$46\\% conflict rate), confirming orthogonality.}\n\\label{fig:factorial_gradient}\n\\end{figure*}\n\n\\subsection{Factorial Interpretation}\n\\label{sec:mechanism}\n\n\\textbf{Gradient flow is associated with lower safety under BatchNorm but not under LayerNorm.} The BN row provides the clearest signal: Full OCC (BN) is the sole factorial cell falling below Vanilla ($\\Delta{=}-2.0$\\,pp, $g{=}-0.34$ vs.\\ Vanilla), whereas Detach OCC recovers above it ($\\Delta{=}+2.2$\\,pp, $g{=}+0.74$, large). In the LN row, Full OCC+LN already exceeds Vanilla ($0.773$, $g{=}+0.90$, large), and Detach+LN yields the highest cell mean ($0.802$, $g{=}+1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$). This is a practical threshold crossing---only BN + gradient flow is associated with reduced safety---rather than a statistical interaction (the factorial interaction is negligible, $\\eta^2{=}0.005$). The numerical advantage of Detach OCC ($+$2.2\\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.\n\n\\textbf{Temporal dynamics.} Cutoff conditions illuminate when gradient flow's association with lower safety emerges. Cutoff@15K ($\\Delta{=}+0.2$\\,pp) performs near Vanilla, while Cutoff@25K shows a large deficit ($\\Delta{=}-5.6$\\,pp) and Cutoff@35K returns to baseline ($\\Delta{=}-0.1$\\,pp). Cutoff@45K ($\\Delta{=}-1.6$\\,pp, single seed) falls between these extremes. This non-monotonic pattern suggests that the critical window for gradient flow damage is not simply cumulative exposure but depends on the training phase. Reverse Cutoff (gradient flow only after step 35K) produces the worst supplementary result ($\\Delta{=}-6.2$\\,pp), indicating that late-stage gradient flow---when the model is refining action predictions---is associated with substantially worse outcomes than early exposure during initial representation learning. However, temporal conditions use 1--3 seeds under v1, so these observations are preliminary; targeted replication under v2 with more seeds would be needed to confirm the temporal pattern.\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:factorial_gradient}b) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n% Old Fig 3 (gradient standalone) — merged into fig:factorial_gradient above\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n% \\caption{...}\n% \\label{fig:gradient_analysis_old}\n% \\end{figure}\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:factorial_gradient}b), with conflict rates of ${\\approx}$46\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (Figure~\\ref{fig:factorial_gradient}b), ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)\n\n\\textbf{Mechanism remains open.} The observed effect pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The observed effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. Centered Kernel Alignment (CKA) analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP across all encoder layers), localizing the safety deficit to optimization dynamics rather than representational corruption. This high representational similarity is notable: even the worst-performing condition (Full OCC, BN) produces encoder features nearly identical to Vanilla, yet its action policy exhibits substantially worse collision avoidance. The dissociation between representational similarity and behavioral safety suggests that subtle differences in the LoRA adapter weights---invisible to CKA---drive the safety deficit.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
      "numLines": 101,
      "startLine": 1,
      "totalLines": 101
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01MQURFcj5yED3poMhYwVRvF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "1a89d49e-5f82-42e1-ad55-109e8521b3b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1pk7xtvS6LcUowPhdxUVn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13885,
      "cache_read_input_tokens": 11845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13885
      },
      "output_tokens": 20,
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

_source line 13 · 2026-05-29T02:20:35.672Z_

<details><summary>↩ Tool result · `toolu_01MQURFcj5yED3poMhYwVRvF`</summary>

```text
1	\section{Introduction}
2	
3	Vision-language-action (VLA) models achieve high task success on manipulation benchmarks~\cite{brohan2023rt2, kim2024openvla, kim2025oft}, but behavioral safety does not follow. On SafeLIBERO Level~I~\cite{hu2025vlsa}, OpenVLA-7B reaches 87.8\% Task Success Rate but only 74.5\% Collision Avoidance Rate (CAR), with collision rates of 43--93\% on the three most constrained tasks.
4	
5	Two active research threads address related but distinct aspects. The first enriches VLAs with auxiliary spatial prediction (occupancy grids, depth maps, point clouds)~\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success under the implicit assumption that spatial awareness yields safer behavior. The second targets VLA safety directly through runtime action filtering~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained RL~\cite{zhang2025safevla}. These lines are disconnected: no spatial method evaluates collision avoidance, and no safety method examines spatial representations. A recent survey~\cite{li2026vlasafety} confirms this gap. Moreover, single-factor ablations---the dominant methodology---cannot decompose joint effects of multiple design choices; only a factorial design can determine whether factors like gradient flow and normalization type interact or combine independently.
6	
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{figures/fig1_architecture_pb.pdf}
10	\caption{\textbf{Training setup and factorial design.} \textbf{(a)}~OpenVLA-7B with dual vision encoders (DINOv2 + SigLIP) and an auxiliary spatial head (BEV occupancy or depth), discarded at inference. \textbf{(b)}~$2{\times}2$ factorial crossing gradient flow (ON/OFF) and normalization (BN/LN), plus Vanilla baseline and 7 single-factor ablations probing label content, reference frame, and temporal extent.}
11	\label{fig:overview}
12	\end{figure*}
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{figures/fig1c_results_bar.pdf}
17	\caption{\textbf{Only BN + gradient flow falls below Vanilla.} Detach+LN achieves the highest CAR ($0.802{\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$, bootstrap 95\% CI excludes zero). Under BatchNorm, gradient flow is associated with lower CAR (0.725 vs.\ 0.745); LayerNorm eliminates this vulnerability. Error bars: cross-seed SD.}
18	\label{fig:results_bar}
19	\end{figure}
20	
21	We ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\cite{kim2024openvla} with LoRA~\cite{hu2022lora}. A core $2{\times}2$ factorial crosses gradient flow (ON/OFF) with normalization (BN/LN); seven additional single-factor ablations probe label content, spatial reference frame, and temporal extent---twelve conditions in total (Figure~\ref{fig:overview}). The factorial design can detect interactions that single-factor studies miss; here, it establishes that the two main effects are additive ($p_{\text{interaction}}{=}0.76$), a practically important finding that prior work could not have obtained.
22	
23	The central finding is that \textbf{Detach+LN reliably outperforms Vanilla} ($\text{CAR}$ $0.802$ vs.\ $0.745$; Hedges' $g{=}1.89$, bootstrap 95\% CI for $\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$, $n{=}3$ vs $3$). The $2{\times}2$ factorial reveals why: gradient flow under BN is associated with 4.2\,pp lower CAR ($g{=}0.78$, large), and LN provides a 3.5--4.8\,pp safety advantage ($g{\approx}0.88$, large). Only the BN + gradient flow combination falls below Vanilla. Spatial label content showed no detectable effect (observed under v1 codebase; \S\ref{sec:results}).
24	
25	Our contributions:
26	\begin{enumerate}[nosep,leftmargin=*]
27	    \item \textbf{Detach+LN reliably improves safety.} Detached gradients with LayerNorm yield CAR $0.802$, reliably outperforming Vanilla $0.745$ (Hedges' $g{=}1.89$, bootstrap 95\% CI $[0.025, 0.089]$). A $2{\times}2$ factorial reveals two additive mechanisms: BN + gradient flow is the sole cell below baseline ($g{=}-0.78$, $\sigma{=}0.064$); LN provides a 3.5--4.8\,pp advantage ($g{\approx}0.88$). Spatial content showed no detectable effect (observed under v1 codebase; Table~\ref{tab:main_results}, Figure~\ref{fig:factorial_gradient}a).
28	
29	    \item \textbf{Factorial methodology for VLA auxiliary heads.} The first systematic factorial comparison of how auxiliary head design choices combine during VLA fine-tuning, establishing that effects are additive---a conclusion single-factor ablations cannot reach (\S\ref{sec:ablation}, Table~\ref{tab:ablation_design}).
30	
31	    \item \textbf{Actionable guidelines at zero cost.} Do not add auxiliary spatial heads with gradient flow under BN. If required, use detached gradients with LayerNorm. No ground-truth spatial labels are needed; the auxiliary head is discarded at inference (\S\ref{sec:discussion}).
32	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "0c4c29b3-4b4d-438f-a011-acb6586d14d5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nVision-language-action (VLA) models achieve high task success on manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}, but behavioral safety does not follow. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, OpenVLA-7B reaches 87.8\\% Task Success Rate but only 74.5\\% Collision Avoidance Rate (CAR), with collision rates of 43--93\\% on the three most constrained tasks.\n\nTwo active research threads address related but distinct aspects. The first enriches VLAs with auxiliary spatial prediction (occupancy grids, depth maps, point clouds)~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success under the implicit assumption that spatial awareness yields safer behavior. The second targets VLA safety directly through runtime action filtering~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained RL~\\cite{zhang2025safevla}. These lines are disconnected: no spatial method evaluates collision avoidance, and no safety method examines spatial representations. A recent survey~\\cite{li2026vlasafety} confirms this gap. Moreover, single-factor ablations---the dominant methodology---cannot decompose joint effects of multiple design choices; only a factorial design can determine whether factors like gradient flow and normalization type interact or combine independently.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_architecture_pb.pdf}\n\\caption{\\textbf{Training setup and factorial design.} \\textbf{(a)}~OpenVLA-7B with dual vision encoders (DINOv2 + SigLIP) and an auxiliary spatial head (BEV occupancy or depth), discarded at inference. \\textbf{(b)}~$2{\\times}2$ factorial crossing gradient flow (ON/OFF) and normalization (BN/LN), plus Vanilla baseline and 7 single-factor ablations probing label content, reference frame, and temporal extent.}\n\\label{fig:overview}\n\\end{figure*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1c_results_bar.pdf}\n\\caption{\\textbf{Only BN + gradient flow falls below Vanilla.} Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$, bootstrap 95\\% CI excludes zero). Under BatchNorm, gradient flow is associated with lower CAR (0.725 vs.\\ 0.745); LayerNorm eliminates this vulnerability. Error bars: cross-seed SD.}\n\\label{fig:results_bar}\n\\end{figure}\n\nWe ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\\cite{kim2024openvla} with LoRA~\\cite{hu2022lora}. A core $2{\\times}2$ factorial crosses gradient flow (ON/OFF) with normalization (BN/LN); seven additional single-factor ablations probe label content, spatial reference frame, and temporal extent---twelve conditions in total (Figure~\\ref{fig:overview}). The factorial design can detect interactions that single-factor studies miss; here, it establishes that the two main effects are additive ($p_{\\text{interaction}}{=}0.76$), a practically important finding that prior work could not have obtained.\n\nThe central finding is that \\textbf{Detach+LN reliably outperforms Vanilla} ($\\text{CAR}$ $0.802$ vs.\\ $0.745$; Hedges' $g{=}1.89$, bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$, $n{=}3$ vs $3$). The $2{\\times}2$ factorial reveals why: gradient flow under BN is associated with 4.2\\,pp lower CAR ($g{=}0.78$, large), and LN provides a 3.5--4.8\\,pp safety advantage ($g{\\approx}0.88$, large). Only the BN + gradient flow combination falls below Vanilla. Spatial label content showed no detectable effect (observed under v1 codebase; \\S\\ref{sec:results}).\n\nOur contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Detach+LN reliably improves safety.} Detached gradients with LayerNorm yield CAR $0.802$, reliably outperforming Vanilla $0.745$ (Hedges' $g{=}1.89$, bootstrap 95\\% CI $[0.025, 0.089]$). A $2{\\times}2$ factorial reveals two additive mechanisms: BN + gradient flow is the sole cell below baseline ($g{=}-0.78$, $\\sigma{=}0.064$); LN provides a 3.5--4.8\\,pp advantage ($g{\\approx}0.88$). Spatial content showed no detectable effect (observed under v1 codebase; Table~\\ref{tab:main_results}, Figure~\\ref{fig:factorial_gradient}a).\n\n    \\item \\textbf{Factorial methodology for VLA auxiliary heads.} The first systematic factorial comparison of how auxiliary head design choices combine during VLA fine-tuning, establishing that effects are additive---a conclusion single-factor ablations cannot reach (\\S\\ref{sec:ablation}, Table~\\ref{tab:ablation_design}).\n\n    \\item \\textbf{Actionable guidelines at zero cost.} Do not add auxiliary spatial heads with gradient flow under BN. If required, use detached gradients with LayerNorm. No ground-truth spatial labels are needed; the auxiliary head is discarded at inference (\\S\\ref{sec:discussion}).\n\\end{enumerate}",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me also search for any other references to the old figure labels across the paper directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "ce5de1b9-4130-4a53-bc24-f29da37108c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfuwbKgBH1fF7mPixUpYcv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14337,
      "cache_read_input_tokens": 25730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14337
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

_source line 15_

Now let me search for all references to the old figure labels across the paper directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "317234cc-2c20-4fe8-82e3-306737b4115a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfuwbKgBH1fF7mPixUpYcv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14337,
      "cache_read_input_tokens": 25730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14337
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

_source line 16_

<details open><summary>🔧 Tool call — Grep · `toolu_01LerMngPHbZAAF9w42YDaqM`</summary>

```json
{
  "pattern": "\\\\ref\\{fig:(results_bar|factorial_gradient|factorial_old|gradient_analysis_old)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "29248804-3a33-4eb4-bcdf-1088b6f71137",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfuwbKgBH1fF7mPixUpYcv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14337,
      "cache_read_input_tokens": 25730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14337
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

_source line 17 · 2026-05-29T02:20:41.763Z_

<details><summary>↩ Tool result · `toolu_01LerMngPHbZAAF9w42YDaqM`</summary>

```text
docs/paper/discussion.tex:5:\textbf{Excluded mechanism---gradient conflict.} Near-zero action--auxiliary cosine similarity (${\approx}$46\% conflict rate; Figure~\ref{fig:factorial_gradient}b) and comparable action gradient norms (Figure~\ref{fig:factorial_gradient}b) rule out PCGrad-style gradient conflict~\cite{yu2020pcgrad}.
docs/paper/appendix.tex:78:% Figure~\ref{fig:factorial_gradient}b is in the main text (Section~\ref{sec:mechanism}).
docs/paper/appendix.tex:82:[Omitted long matching line]
docs/paper/introduction.tex:27:[Omitted long matching line]
docs/paper/results.tex:11:[Omitted long matching line]
docs/paper/results.tex:86:Gradient analysis (Figure~\ref{fig:factorial_gradient}b) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).
docs/paper/results.tex:96:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "1e96dc40-6ea8-48be-96f1-e4ae9b77c2c4",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/discussion.tex:5:\\textbf{Excluded mechanism---gradient conflict.} Near-zero action--auxiliary cosine similarity (${\\approx}$46\\% conflict rate; Figure~\\ref{fig:factorial_gradient}b) and comparable action gradient norms (Figure~\\ref{fig:factorial_gradient}b) rule out PCGrad-style gradient conflict~\\cite{yu2020pcgrad}.\ndocs/paper/appendix.tex:78:% Figure~\\ref{fig:factorial_gradient}b is in the main text (Section~\\ref{sec:mechanism}).\ndocs/paper/appendix.tex:82:[Omitted long matching line]\ndocs/paper/introduction.tex:27:[Omitted long matching line]\ndocs/paper/results.tex:11:[Omitted long matching line]\ndocs/paper/results.tex:86:Gradient analysis (Figure~\\ref{fig:factorial_gradient}b) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\ndocs/paper/results.tex:96:[Omitted long matching line]",
    "numLines": 7
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Glob · `toolu_01EtmVe4ra3JAgsPKxJctzTV`</summary>

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
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "cee8ad3f-9833-40d3-ac9f-7a6ad3e7dbd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfuwbKgBH1fF7mPixUpYcv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14337,
      "cache_read_input_tokens": 25730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14337
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

_source line 19 · 2026-05-29T02:20:42.303Z_

<details><summary>↩ Tool result · `toolu_01EtmVe4ra3JAgsPKxJctzTV`</summary>

```text
docs/paper/references.tex
docs/paper/experiments_old.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/limitations.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/results.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "6adba398-4a9c-4b6a-9770-64e741863204",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.tex",
      "docs/paper/experiments_old.tex",
      "docs/paper/method.tex",
      "docs/paper/related_work.tex",
      "docs/paper/limitations.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/main.tex",
      "docs/paper/results.tex",
      "docs/paper/discussion.tex",
      "docs/paper/introduction.tex",
      "docs/paper/appendix.tex"
    ],
    "durationMs": 10,
    "numFiles": 11,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Let me check the specific references in discussion.tex and appendix.tex to understand what needs to change.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "e1bffb46-9759-4083-8bdc-d2deb9c71849",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147jcQW5LZVoauMXptrYtQM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 40067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 21_

Let me check the specific lines in discussion.tex and appendix.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "6f9d75fa-0e03-486a-af25-76ccb9f84ade",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147jcQW5LZVoauMXptrYtQM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 40067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_015sNQe253rmRsrDNhEgBqt6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "offset": 1,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "b9c926f8-6f86-4845-b90c-959fa7289513",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147jcQW5LZVoauMXptrYtQM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 40067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 23 · 2026-05-29T02:20:46.246Z_

<details><summary>↩ Tool result · `toolu_015sNQe253rmRsrDNhEgBqt6`</summary>

```text
1	
2	\section{Discussion}
3	\label{sec:discussion}
4	
5	\textbf{Excluded mechanism---gradient conflict.} Near-zero action--auxiliary cosine similarity (${\approx}$46\% conflict rate; Figure~\ref{fig:factorial_gradient}b) and comparable action gradient norms (Figure~\ref{fig:factorial_gradient}b) rule out PCGrad-style gradient conflict~\cite{yu2020pcgrad}.
6	%
7	\textbf{Hypothesis---BN forward-pass statistics corruption.} BatchNorm is not inherently harmful: Detach OCC (BN, gradient OFF) matches Vanilla ($0.767$ vs.\ $0.745$, $p{=}0.28$); the deficit requires the joint presence of BN and gradient flow. We hypothesize a \emph{forward-pass} mechanism: BN running mean/variance update during each forward pass regardless of gradient conflict, so the auxiliary head shifts the running statistics used at inference. LayerNorm, normalizing per-token without cross-batch statistics, lacks this coupling. CKA confirms intact encoder representations (CKA $\geq$ 0.95), localizing the effect to optimization dynamics. This hypothesis remains unverified; targeted experiments (e.g., freezing running statistics or comparing train vs.\ eval mode) would be needed.
8	
9	\textbf{Normalization is independently associated with safety differences.} LN provides a consistent $+$3.5--4.8\,pp advantage over BN ($g{=}0.88$--$1.24$); normalization type, typically treated as an implementation detail, has outsized consequences for safety-critical VLA fine-tuning.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "edb0613c-3eda-47e9-a1a4-3704fbe33fc3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
      "content": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\textbf{Excluded mechanism---gradient conflict.} Near-zero action--auxiliary cosine similarity (${\\approx}$46\\% conflict rate; Figure~\\ref{fig:factorial_gradient}b) and comparable action gradient norms (Figure~\\ref{fig:factorial_gradient}b) rule out PCGrad-style gradient conflict~\\cite{yu2020pcgrad}.\n%\n\\textbf{Hypothesis---BN forward-pass statistics corruption.} BatchNorm is not inherently harmful: Detach OCC (BN, gradient OFF) matches Vanilla ($0.767$ vs.\\ $0.745$, $p{=}0.28$); the deficit requires the joint presence of BN and gradient flow. We hypothesize a \\emph{forward-pass} mechanism: BN running mean/variance update during each forward pass regardless of gradient conflict, so the auxiliary head shifts the running statistics used at inference. LayerNorm, normalizing per-token without cross-batch statistics, lacks this coupling. CKA confirms intact encoder representations (CKA $\\geq$ 0.95), localizing the effect to optimization dynamics. This hypothesis remains unverified; targeted experiments (e.g., freezing running statistics or comparing train vs.\\ eval mode) would be needed.\n\n\\textbf{Normalization is independently associated with safety differences.} LN provides a consistent $+$3.5--4.8\\,pp advantage over BN ($g{=}0.88$--$1.24$); normalization type, typically treated as an implementation detail, has outsized consequences for safety-critical VLA fine-tuning.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01PP98ZTVRWEdgGsr1Z4HDCW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "offset": 75,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "3aa56009-45a8-4e2a-b682-49f7f2ff2669",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147jcQW5LZVoauMXptrYtQM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 40067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 25 · 2026-05-29T02:20:46.861Z_

<details><summary>↩ Tool result · `toolu_01PP98ZTVRWEdgGsr1Z4HDCW`</summary>

```text
75	
76	\section{Extended Analysis}
77	
78	% Figure~\ref{fig:factorial_gradient}b is in the main text (Section~\ref{sec:mechanism}).
79	
80	The Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \texttt{stop\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \pm 0.024$ (Table~\ref{tab:main_results}), the highest factorial cell mean ($\Delta{=}+5.7$\,pp vs.\ Vanilla, $g{=}+1.89$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.
81	
82	\textbf{Per-layer gradient analysis.} Figure~\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\ref{fig:factorial_gradient}b) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\%, Full OCC+LN 45.7\% under v2; Full OCC 44.1\%, Random OCC 43.9\% under v1) fall below the 50\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.
83	
84	\begin{figure}[h]
85	\centering
86	\includegraphics[width=\textwidth]{figures/per_layer_combined.pdf}
87	\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\ref{app:codebase}). \textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\sim$46\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\approx}$46\% in early and middle layers; late SigLIP layers show lower conflict rates (${\approx}$25\%), consistent with weak alignment rather than conflict.}
88	\label{fig:per_layer_combined}
89	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "5f3e1fc0-986f-45f3-a48d-bdc9308360cd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
      "content": "\n\\section{Extended Analysis}\n\n% Figure~\\ref{fig:factorial_gradient}b is in the main text (Section~\\ref{sec:mechanism}).\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \\pm 0.024$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.7$\\,pp vs.\\ Vanilla, $g{=}+1.89$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:factorial_gradient}b) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}",
      "numLines": 15,
      "startLine": 75,
      "totalLines": 208
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have a full picture. Let me also check introduction.tex line 27 which references `fig:factorial_gradient`.

Looking at the references I need to update:

1. `introduction.tex` line 27: `Figure~\ref{fig:factorial_gradient}a` → `Figure~\ref{fig:car_factorial}b` (factorial reference)
2. `introduction.tex` lines 14-19: The `fig:results_bar` figure environment → DELETE


3. `results.tex` line 11: `Figure~\ref{fig:factorial_gradient}a` → `Figure~\ref{fig:car_factorial}b`
4. `results.tex` lines 70-75: The `fig:factorial_gradient` figure* environment → DELETE
5. `results.tex` lines 88-94: Uncomment the old gradient standalone figure, update filename and label
6. `results.tex` lines 86 and 96: Both references to `Figure~\ref{fig:factorial_gradient}b` → `Figure~\ref{fig:gradient_analysis}`
7. `discussion.tex` line 5: Two references to `Figure~\ref{fig:factorial_gradient}b` → `Figure~\ref{fig:gradient_analysis}`
8. `appendix.tex` lines 78 and 82: Update references from `fig:factorial_gradient}b` → `Figure~\ref{fig:gradient_analysis}`

Now I need to think through the placement strategy. Table 2 ends at line 60, and the gradient section starts at line 84. The current combined figure sits at lines 70-75, which is exactly where I need to insert the new `fig:car_factorial` figure. So I'll replace those lines with the new figure, then uncomment the gradient figure below it.

For the reference updates across files, I need to swap out `\ref{fig:results_bar}` for `\ref{fig:car_factorial}a` since the bar chart is now panel a of the combined figure, and update `\ref{fig:factorial_gradient}a` to point to the new gradient figure reference. Now I need to track down the remaining references across the other files—introduction.tex has a `\ref{fig:results_bar}` that's part of a figure block to delete, and then I've got multiple instances of `\ref{fig:factorial_gradient}b` scattered through results.tex, discussion.tex, and appendix.tex that all need updating to point to the new gradient_analysis figure instead. need to verify whether `fig:results_bar` is actually referenced anywhere in the text, since the grep search didn't turn up explicit `\ref` calls to it. It's possible the figure is defined but never cited, which would be unusual. Let me search more carefully to confirm before deciding what needs updating.

Actually, the task description clarifies that I should just delete the figure environment from introduction.tex where fig1c previously had an independent figure environment for `fig:results_bar`. So I'll proceed with that deletion and then create the combined figure script that merges the CAR horizontal dot chart with the factorial interaction plot into a single figure with two side-by-side panels, adjusting the dimensions to 7.0 by 3.0 inches and unifying the color scheme and font sizes.

Writing the combined figure script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "072e2584-7c41-444b-bf18-1ab7c68419ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKr5aL6PGbhkqaoHZxqbnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1794,
      "cache_read_input_tokens": 40787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1794
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

_source line 27_

I have all the context. Let me proceed with all three parts. I'll create the combined figure script and make all LaTeX edits in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "f257f109-6a0c-4a61-9b37-a81c43cefc8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKr5aL6PGbhkqaoHZxqbnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1794,
      "cache_read_input_tokens": 40787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1794
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

_source line 28_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XQXxGe4CSnL2KmcJgGuZt7`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "7ec0a599-c5a9-4c5b-9b93-4ce0b3c7e528",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKr5aL6PGbhkqaoHZxqbnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1794,
      "cache_read_input_tokens": 40787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1794
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

_source line 29 · 2026-05-29T02:21:22.551Z_

<details><summary>↩ Tool result · `toolu_01XQXxGe4CSnL2KmcJgGuZt7`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "02387278-daa9-4d65-8d43-3a45020dc8cf",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 82
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01D5Fp5aKnupdycAqEY4p52U`</summary>

```json
{
  "todos": [
    {
      "content": "Create fig_car_factorial_combined.py script",
      "status": "in_progress",
      "activeForm": "Creating combined figure script"
    },
    {
      "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
      "status": "pending",
      "activeForm": "Updating LaTeX files"
    },
    {
      "content": "Update all \\ref{} cross-references across paper",
      "status": "pending",
      "activeForm": "Updating cross-references"
    },
    {
      "content": "Run script and visually verify output",
      "status": "pending",
      "activeForm": "Running script and verifying output"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "5b319baa-9d4d-4b84-adcf-7f292adf37d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCN9tt8u75Z9wNN81zFtKa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4293,
      "cache_read_input_tokens": 42581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4293
      },
      "output_tokens": 53,
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

_source line 31 · 2026-05-29T02:21:27.139Z_

<details><summary>↩ Tool result · `toolu_01D5Fp5aKnupdycAqEY4p52U`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "77ec1e1e-2a5f-4fb8-80d7-5850f87c407d",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Create fig_car_factorial_combined.py script",
        "status": "in_progress",
        "activeForm": "Creating combined figure script"
      },
      {
        "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
        "status": "pending",
        "activeForm": "Updating LaTeX files"
      },
      {
        "content": "Update all \\ref{} cross-references across paper",
        "status": "pending",
        "activeForm": "Updating cross-references"
      },
      {
        "content": "Run script and visually verify output",
        "status": "pending",
        "activeForm": "Running script and verifying output"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Write · `toolu_01G7a5AXVaQkq15oYSF9PyVd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig_car_factorial_combined.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Combined Figure: (a) CAR horizontal dot chart + (b) Factorial 2x2 interaction plot.\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\n\nCOLORS = {\n    'vanilla':     '#4C72B0',\n    'full_occ_bn': '#C44E52',\n    'full_occ_ln': '#E69F00',\n    'detach_bn':   '#8172B3',\n    'detach_ln':   '#937860',\n}\nUI = {'text': '#2C3E50', 'subtle': '#95A5A6'}\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],\n    'font.size': 7.5,\n    'axes.titlesize': 8,\n    'axes.labelsize': 8,\n    'xtick.labelsize': 7,\n    'ytick.labelsize': 7,\n    'legend.fontsize': 7,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.03,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'axes.linewidth': 0.6,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'mathtext.fontset': 'cm',\n    'text.color': UI['text'],\n    'axes.labelcolor': UI['text'],\n})\n\nfig, (ax_bar, ax_fact) = plt.subplots(1, 2, figsize=(7.0, 3.0), dpi=300, facecolor='white')\n\n# ============================================================\n# (a) CAR horizontal dot chart\n# ============================================================\ncdata = [\n    {'name': 'Full OCC\\n(BN, Grad ON)',    'car': 0.725, 'sd': 0.064,\n     'color': COLORS['full_occ_bn'], 'n_seeds': 3},\n    {'name': 'Detach OCC\\n(BN, Grad OFF)',  'car': 0.767, 'sd': 0.024,\n     'color': COLORS['detach_bn'],   'n_seeds': 4},\n    {'name': 'Full OCC+LN\\n(LN, Grad ON)', 'car': 0.773, 'sd': 0.027,\n     'color': COLORS['full_occ_ln'], 'n_seeds': 4},\n    {'name': 'Detach+LN\\n(LN, Grad OFF)',  'car': 0.802, 'sd': 0.024,\n     'color': COLORS['detach_ln'],   'n_seeds': 3},\n]\nvanilla_car = 0.745\n\nax = ax_bar\nax.set_xlim(0.655, 0.87)\nax.set_ylim(-0.8, len(cdata) - 0.2)\nax.invert_yaxis()\nax.spines['left'].set_visible(False)\nax.set_xlabel('Collision Avoidance Rate (CAR)', fontsize=8, fontweight='bold', labelpad=5)\n\n# Group background bands\nax.axhspan(-0.5, 1.5, alpha=0.02, color=COLORS['full_occ_bn'], zorder=0)\nax.axhspan(1.5, 3.5, alpha=0.02, color=COLORS['full_occ_ln'], zorder=0)\nax.text(0.865, 0.5, 'BN', fontsize=8, color=COLORS['full_occ_bn'], ha='center', va='center',\n        fontweight='bold', alpha=0.35,\n        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))\nax.text(0.865, 2.5, 'LN', fontsize=8, color=COLORS['full_occ_ln'], ha='center', va='center',\n        fontweight='bold', alpha=0.35,\n        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))\n\n# Vanilla reference\nax.axvline(x=vanilla_car, color=COLORS['vanilla'], linestyle='--',\n           linewidth=1.5, alpha=0.7, zorder=1)\nax.text(vanilla_car + 0.003, -0.55, f'Vanilla  {vanilla_car:.3f}',\n        fontsize=8, color=COLORS['vanilla'], va='top', ha='left',\n        fontweight='bold',\n        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])\n\n# Below-baseline shading\nax.axvspan(0.655, vanilla_car, alpha=0.04, color=COLORS['full_occ_bn'], zorder=0)\n\n# Connecting lines: BN pair\nax.plot([0.725, 0.767], [0, 1], color=COLORS['full_occ_bn'],\n        lw=1.1, linestyle=':', alpha=0.5, zorder=1)\nax.text(0.730, 0.55, '$-$4.2 pp', fontsize=7.5,\n        color=COLORS['full_occ_bn'], ha='left', va='center',\n        fontweight='bold', alpha=0.8,\n        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])\n\n# LN pair\nax.plot([0.773, 0.802], [2, 3], color=COLORS['full_occ_ln'],\n        lw=1.1, linestyle=':', alpha=0.5, zorder=1)\nax.text(0.778, 2.55, '$-$2.9 pp', fontsize=7.5,\n        color=COLORS['full_occ_ln'], ha='left', va='center',\n        fontweight='bold', alpha=0.8,\n        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])\n\n# Plot data points\nfor i, d in enumerate(cdata):\n    ax.plot(d['car'], i, 'o', color=d['color'], markersize=7.5,\n            markeredgecolor='white', markeredgewidth=0.8, zorder=5)\n    ax.errorbar(d['car'], i, xerr=d['sd'], fmt='none', ecolor=d['color'],\n                elinewidth=1.8, capsize=4, capthick=1.3, zorder=4, alpha=0.7)\n    right_x = d['car'] + d['sd'] + 0.005\n    label_text = f'{d[\"car\"]:.3f} ± {d[\"sd\"]:.3f}'\n    ax.text(right_x, i + 0.02, label_text, fontsize=7.5, ha='left',\n            va='center', color=d['color'], fontweight='bold',\n            path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])\n\nax.set_yticks(list(range(len(cdata))))\nax.set_yticklabels([d['name'] for d in cdata], fontsize=7.5, linespacing=1.1)\nax.tick_params(axis='y', length=0, pad=5)\nax.tick_params(axis='x', labelsize=7)\nax.grid(axis='x', alpha=0.10, color='#999', zorder=0)\nax.set_xticks([0.68, 0.72, 0.76, 0.80, 0.84])\n\n# Panel label\nax.text(-0.02, 1.06, '(a)', transform=ax.transAxes, fontsize=10, fontweight='bold', va='top')\n\n# ============================================================\n# (b) Factorial 2x2 interaction plot\n# ============================================================\nfactorial_data = {\n    'BN': {\n        'OFF': {'mean': 0.767, 'std': 0.024, 'n': 4},\n        'ON':  {'mean': 0.725, 'std': 0.064, 'n': 3},\n    },\n    'LN': {\n        'OFF': {'mean': 0.802, 'std': 0.024, 'n': 3},\n        'ON':  {'mean': 0.773, 'std': 0.027, 'n': 4},\n    },\n}\n\nC_BN = COLORS['full_occ_bn']\nC_LN = COLORS['full_occ_ln']\nC_VAN = COLORS['vanilla']\n\nax = ax_fact\nax.axhspan(0.68, vanilla_car, color=C_BN, alpha=0.03, zorder=0)\nax.axhline(y=vanilla_car, color=C_VAN, linestyle=':', linewidth=0.8, alpha=0.5, zorder=1)\nt_van = ax.text(0.97, vanilla_car + 0.002, 'Vanilla (0.745)', fontsize=7,\n                color=C_VAN, va='bottom', ha='right',\n                transform=ax.get_yaxis_transform(), fontweight='medium')\nt_van.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])\n\nx_positions = [0, 1]\n\nbn_y = [factorial_data['BN']['OFF']['mean'], factorial_data['BN']['ON']['mean']]\nbn_err = [factorial_data['BN'][gf]['std'] for gf in ['OFF', 'ON']]\nax.errorbar(x_positions, bn_y, yerr=bn_err, color=C_BN,\n            marker='o', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,\n            linestyle='-', linewidth=1.4, capsize=3, capthick=0.8,\n            elinewidth=0.8, label='BatchNorm (BN)', zorder=3)\n\nln_y = [factorial_data['LN']['OFF']['mean'], factorial_data['LN']['ON']['mean']]\nln_err = [factorial_data['LN'][gf]['std'] for gf in ['OFF', 'ON']]\nax.errorbar(x_positions, ln_y, yerr=ln_err, color=C_LN,\n            marker='s', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,\n            linestyle=(0, (4, 2.5)), linewidth=1.4, capsize=3, capthick=0.8,\n            elinewidth=0.8, label='LayerNorm (LN)', zorder=3)\n\n# Delta annotations\ndelta_bn = (factorial_data['BN']['ON']['mean'] - factorial_data['BN']['OFF']['mean']) * 100\ndelta_ln = (factorial_data['LN']['ON']['mean'] - factorial_data['LN']['OFF']['mean']) * 100\n\nmid_bn_y = np.mean(bn_y)\nt_bn = ax.annotate(f'−{abs(delta_bn):.1f} pp', xy=(0.55, mid_bn_y - 0.008),\n                   fontsize=7.5, fontweight='bold', color=C_BN, ha='center', va='top', zorder=5)\nt_bn.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\nmid_ln_y = np.mean(ln_y)\nt_ln = ax.annotate(f'−{abs(delta_ln):.1f} pp', xy=(0.45, mid_ln_y + 0.008),\n                   fontsize=7.5, fontweight='bold', color=C_LN, ha='center', va='bottom', zorder=5)\nt_ln.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\n# n-labels\nn_offsets = {\n    ('BN', 'OFF'): (-12, -10),\n    ('BN', 'ON'):  (12, -14),\n    ('LN', 'OFF'): (-12, 8),\n    ('LN', 'ON'):  (12, 10),\n}\nfor gf_idx, gf in enumerate(['OFF', 'ON']):\n    for norm in ['BN', 'LN']:\n        n_val = factorial_data[norm][gf]['n']\n        y_val = factorial_data[norm][gf]['mean']\n        ox, oy = n_offsets[(norm, gf)]\n        c = C_BN if norm == 'BN' else C_LN\n        ax.annotate(f'n={n_val}', (x_positions[gf_idx], y_val),\n                    xytext=(ox, oy), textcoords='offset points',\n                    fontsize=7, color=c, ha='center', fontstyle='italic', alpha=0.6)\n\nax.set_xticks(x_positions)\nax.set_xticklabels(['OFF\\n(Detach)', 'ON\\n(Full)'], fontsize=7)\nax.set_xlabel('Gradient Flow', fontsize=8)\nax.set_ylabel('Collision Avoidance Rate (CAR)', fontsize=8)\nax.set_xlim(-0.3, 1.3)\nax.set_ylim(0.68, 0.86)\nax.yaxis.set_major_locator(plt.MultipleLocator(0.02))\nax.legend(loc='upper right', frameon=True, framealpha=0.95, edgecolor='none',\n          handlelength=2.0, handletextpad=0.4, fontsize=7)\n\n# Panel label\nax.text(-0.02, 1.06, '(b)', transform=ax.transAxes, fontsize=10, fontweight='bold', va='top')\n\nplt.tight_layout(w_pad=2.0)\n\n# Save\nOUT_DIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'\nfor fmt in ['pdf', 'png']:\n    path = f'{OUT_DIR}/fig_car_factorial_combined.{fmt}'\n    fig.savefig(path, facecolor='white')\n    print(f'Saved: {path}')\nplt.close(fig)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "edbc5cd5-1246-4b89-a7f1-7a5094f92ab7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011kkFc3F6Cepd39hQtUwN5F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 46874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
      },
      "output_tokens": 38,
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

_source line 33 · 2026-05-29T02:22:19.838Z_

<details><summary>↩ Tool result · `toolu_01G7a5AXVaQkq15oYSF9PyVd`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig_car_factorial_combined.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "0f25e95d-2bf6-4cb9-b6f7-2d0bee7f0b2a",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig_car_factorial_combined.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Combined Figure: (a) CAR horizontal dot chart + (b) Factorial 2x2 interaction plot.\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\n\nCOLORS = {\n    'vanilla':     '#4C72B0',\n    'full_occ_bn': '#C44E52',\n    'full_occ_ln': '#E69F00',\n    'detach_bn':   '#8172B3',\n    'detach_ln':   '#937860',\n}\nUI = {'text': '#2C3E50', 'subtle': '#95A5A6'}\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],\n    'font.size': 7.5,\n    'axes.titlesize': 8,\n    'axes.labelsize': 8,\n    'xtick.labelsize': 7,\n    'ytick.labelsize': 7,\n    'legend.fontsize': 7,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.03,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'axes.linewidth': 0.6,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'mathtext.fontset': 'cm',\n    'text.color': UI['text'],\n    'axes.labelcolor': UI['text'],\n})\n\nfig, (ax_bar, ax_fact) = plt.subplots(1, 2, figsize=(7.0, 3.0), dpi=300, facecolor='white')\n\n# ============================================================\n# (a) CAR horizontal dot chart\n# ============================================================\ncdata = [\n    {'name': 'Full OCC\\n(BN, Grad ON)',    'car': 0.725, 'sd': 0.064,\n     'color': COLORS['full_occ_bn'], 'n_seeds': 3},\n    {'name': 'Detach OCC\\n(BN, Grad OFF)',  'car': 0.767, 'sd': 0.024,\n     'color': COLORS['detach_bn'],   'n_seeds': 4},\n    {'name': 'Full OCC+LN\\n(LN, Grad ON)', 'car': 0.773, 'sd': 0.027,\n     'color': COLORS['full_occ_ln'], 'n_seeds': 4},\n    {'name': 'Detach+LN\\n(LN, Grad OFF)',  'car': 0.802, 'sd': 0.024,\n     'color': COLORS['detach_ln'],   'n_seeds': 3},\n]\nvanilla_car = 0.745\n\nax = ax_bar\nax.set_xlim(0.655, 0.87)\nax.set_ylim(-0.8, len(cdata) - 0.2)\nax.invert_yaxis()\nax.spines['left'].set_visible(False)\nax.set_xlabel('Collision Avoidance Rate (CAR)', fontsize=8, fontweight='bold', labelpad=5)\n\n# Group background bands\nax.axhspan(-0.5, 1.5, alpha=0.02, color=COLORS['full_occ_bn'], zorder=0)\nax.axhspan(1.5, 3.5, alpha=0.02, color=COLORS['full_occ_ln'], zorder=0)\nax.text(0.865, 0.5, 'BN', fontsize=8, color=COLORS['full_occ_bn'], ha='center', va='center',\n        fontweight='bold', alpha=0.35,\n        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))\nax.text(0.865, 2.5, 'LN', fontsize=8, color=COLORS['full_occ_ln'], ha='center', va='center',\n        fontweight='bold', alpha=0.35,\n        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))\n\n# Vanilla reference\nax.axvline(x=vanilla_car, color=COLORS['vanilla'], linestyle='--',\n           linewidth=1.5, alpha=0.7, zorder=1)\nax.text(vanilla_car + 0.003, -0.55, f'Vanilla  {vanilla_car:.3f}',\n        fontsize=8, color=COLORS['vanilla'], va='top', ha='left',\n        fontweight='bold',\n        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])\n\n# Below-baseline shading\nax.axvspan(0.655, vanilla_car, alpha=0.04, color=COLORS['full_occ_bn'], zorder=0)\n\n# Connecting lines: BN pair\nax.plot([0.725, 0.767], [0, 1], color=COLORS['full_occ_bn'],\n        lw=1.1, linestyle=':', alpha=0.5, zorder=1)\nax.text(0.730, 0.55, '$-$4.2 pp', fontsize=7.5,\n        color=COLORS['full_occ_bn'], ha='left', va='center',\n        fontweight='bold', alpha=0.8,\n        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])\n\n# LN pair\nax.plot([0.773, 0.802], [2, 3], color=COLORS['full_occ_ln'],\n        lw=1.1, linestyle=':', alpha=0.5, zorder=1)\nax.text(0.778, 2.55, '$-$2.9 pp', fontsize=7.5,\n        color=COLORS['full_occ_ln'], ha='left', va='center',\n        fontweight='bold', alpha=0.8,\n        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])\n\n# Plot data points\nfor i, d in enumerate(cdata):\n    ax.plot(d['car'], i, 'o', color=d['color'], markersize=7.5,\n            markeredgecolor='white', markeredgewidth=0.8, zorder=5)\n    ax.errorbar(d['car'], i, xerr=d['sd'], fmt='none', ecolor=d['color'],\n                elinewidth=1.8, capsize=4, capthick=1.3, zorder=4, alpha=0.7)\n    right_x = d['car'] + d['sd'] + 0.005\n    label_text = f'{d[\"car\"]:.3f} ± {d[\"sd\"]:.3f}'\n    ax.text(right_x, i + 0.02, label_text, fontsize=7.5, ha='left',\n            va='center', color=d['color'], fontweight='bold',\n            path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])\n\nax.set_yticks(list(range(len(cdata))))\nax.set_yticklabels([d['name'] for d in cdata], fontsize=7.5, linespacing=1.1)\nax.tick_params(axis='y', length=0, pad=5)\nax.tick_params(axis='x', labelsize=7)\nax.grid(axis='x', alpha=0.10, color='#999', zorder=0)\nax.set_xticks([0.68, 0.72, 0.76, 0.80, 0.84])\n\n# Panel label\nax.text(-0.02, 1.06, '(a)', transform=ax.transAxes, fontsize=10, fontweight='bold', va='top')\n\n# ============================================================\n# (b) Factorial 2x2 interaction plot\n# ============================================================\nfactorial_data = {\n    'BN': {\n        'OFF': {'mean': 0.767, 'std': 0.024, 'n': 4},\n        'ON':  {'mean': 0.725, 'std': 0.064, 'n': 3},\n    },\n    'LN': {\n        'OFF': {'mean': 0.802, 'std': 0.024, 'n': 3},\n        'ON':  {'mean': 0.773, 'std': 0.027, 'n': 4},\n    },\n}\n\nC_BN = COLORS['full_occ_bn']\nC_LN = COLORS['full_occ_ln']\nC_VAN = COLORS['vanilla']\n\nax = ax_fact\nax.axhspan(0.68, vanilla_car, color=C_BN, alpha=0.03, zorder=0)\nax.axhline(y=vanilla_car, color=C_VAN, linestyle=':', linewidth=0.8, alpha=0.5, zorder=1)\nt_van = ax.text(0.97, vanilla_car + 0.002, 'Vanilla (0.745)', fontsize=7,\n                color=C_VAN, va='bottom', ha='right',\n                transform=ax.get_yaxis_transform(), fontweight='medium')\nt_van.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])\n\nx_positions = [0, 1]\n\nbn_y = [factorial_data['BN']['OFF']['mean'], factorial_data['BN']['ON']['mean']]\nbn_err = [factorial_data['BN'][gf]['std'] for gf in ['OFF', 'ON']]\nax.errorbar(x_positions, bn_y, yerr=bn_err, color=C_BN,\n            marker='o', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,\n            linestyle='-', linewidth=1.4, capsize=3, capthick=0.8,\n            elinewidth=0.8, label='BatchNorm (BN)', zorder=3)\n\nln_y = [factorial_data['LN']['OFF']['mean'], factorial_data['LN']['ON']['mean']]\nln_err = [factorial_data['LN'][gf]['std'] for gf in ['OFF', 'ON']]\nax.errorbar(x_positions, ln_y, yerr=ln_err, color=C_LN,\n            marker='s', markersize=5.5, markeredgecolor='white', markeredgewidth=0.7,\n            linestyle=(0, (4, 2.5)), linewidth=1.4, capsize=3, capthick=0.8,\n            elinewidth=0.8, label='LayerNorm (LN)', zorder=3)\n\n# Delta annotations\ndelta_bn = (factorial_data['BN']['ON']['mean'] - factorial_data['BN']['OFF']['mean']) * 100\ndelta_ln = (factorial_data['LN']['ON']['mean'] - factorial_data['LN']['OFF']['mean']) * 100\n\nmid_bn_y = np.mean(bn_y)\nt_bn = ax.annotate(f'−{abs(delta_bn):.1f} pp', xy=(0.55, mid_bn_y - 0.008),\n                   fontsize=7.5, fontweight='bold', color=C_BN, ha='center', va='top', zorder=5)\nt_bn.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\nmid_ln_y = np.mean(ln_y)\nt_ln = ax.annotate(f'−{abs(delta_ln):.1f} pp', xy=(0.45, mid_ln_y + 0.008),\n                   fontsize=7.5, fontweight='bold', color=C_LN, ha='center', va='bottom', zorder=5)\nt_ln.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\n# n-labels\nn_offsets = {\n    ('BN', 'OFF'): (-12, -10),\n    ('BN', 'ON'):  (12, -14),\n    ('LN', 'OFF'): (-12, 8),\n    ('LN', 'ON'):  (12, 10),\n}\nfor gf_idx, gf in enumerate(['OFF', 'ON']):\n    for norm in ['BN', 'LN']:\n        n_val = factorial_data[norm][gf]['n']\n        y_val = factorial_data[norm][gf]['mean']\n        ox, oy = n_offsets[(norm, gf)]\n        c = C_BN if norm == 'BN' else C_LN\n        ax.annotate(f'n={n_val}', (x_positions[gf_idx], y_val),\n                    xytext=(ox, oy), textcoords='offset points',\n                    fontsize=7, color=c, ha='center', fontstyle='italic', alpha=0.6)\n\nax.set_xticks(x_positions)\nax.set_xticklabels(['OFF\\n(Detach)', 'ON\\n(Full)'], fontsize=7)\nax.set_xlabel('Gradient Flow', fontsize=8)\nax.set_ylabel('Collision Avoidance Rate (CAR)', fontsize=8)\nax.set_xlim(-0.3, 1.3)\nax.set_ylim(0.68, 0.86)\nax.yaxis.set_major_locator(plt.MultipleLocator(0.02))\nax.legend(loc='upper right', frameon=True, framealpha=0.95, edgecolor='none',\n          handlelength=2.0, handletextpad=0.4, fontsize=7)\n\n# Panel label\nax.text(-0.02, 1.06, '(b)', transform=ax.transAxes, fontsize=10, fontweight='bold', va='top')\n\nplt.tight_layout(w_pad=2.0)\n\n# Save\nOUT_DIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'\nfor fmt in ['pdf', 'png']:\n    path = f'{OUT_DIR}/fig_car_factorial_combined.{fmt}'\n    fig.savefig(path, facecolor='white')\n    print(f'Saved: {path}')\nplt.close(fig)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01NQsbQPh1Aif997HonGDUPU`</summary>

```json
{
  "todos": [
    {
      "content": "Create fig_car_factorial_combined.py script",
      "status": "completed",
      "activeForm": "Creating combined figure script"
    },
    {
      "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
      "status": "in_progress",
      "activeForm": "Updating LaTeX files"
    },
    {
      "content": "Update all \\ref{} cross-references across paper",
      "status": "pending",
      "activeForm": "Updating cross-references"
    },
    {
      "content": "Run script and visually verify output",
      "status": "pending",
      "activeForm": "Running script and verifying output"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "26e83da6-f9e8-49c7-b887-0389bac39dbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013D4KH8cbfj1LQSMZwkqZHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3936,
      "cache_read_input_tokens": 47111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3936
      },
      "output_tokens": 59,
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

_source line 35 · 2026-05-29T02:22:23.349Z_

<details><summary>↩ Tool result · `toolu_01NQsbQPh1Aif997HonGDUPU`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "fe46d5b3-8550-4a70-b8f6-140e50b06f6d",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Create fig_car_factorial_combined.py script",
        "status": "in_progress",
        "activeForm": "Creating combined figure script"
      },
      {
        "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
        "status": "pending",
        "activeForm": "Updating LaTeX files"
      },
      {
        "content": "Update all \\ref{} cross-references across paper",
        "status": "pending",
        "activeForm": "Updating cross-references"
      },
      {
        "content": "Run script and visually verify output",
        "status": "pending",
        "activeForm": "Running script and verifying output"
      }
    ],
    "newTodos": [
      {
        "content": "Create fig_car_factorial_combined.py script",
        "status": "completed",
        "activeForm": "Creating combined figure script"
      },
      {
        "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
        "status": "in_progress",
        "activeForm": "Updating LaTeX files"
      },
      {
        "content": "Update all \\ref{} cross-references across paper",
        "status": "pending",
        "activeForm": "Updating cross-references"
      },
      {
        "content": "Run script and visually verify output",
        "status": "pending",
        "activeForm": "Running script and verifying output"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 36_

Now updating LaTeX. I'll make all the edits in parallel where possible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "32b04b56-9598-42c6-8772-652842004fcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JQn286AiNAYcFm5aWDtjN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 51047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_015VSm868CncKt2TSrCL2cwY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
  "old_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1c_results_bar.pdf}\n\\caption{\\textbf{Only BN + gradient flow falls below Vanilla.} Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$, bootstrap 95\\% CI excludes zero). Under BatchNorm, gradient flow is associated with lower CAR (0.725 vs.\\ 0.745); LayerNorm eliminates this vulnerability. Error bars: cross-seed SD.}\n\\label{fig:results_bar}\n\\end{figure}",
  "new_string": "% fig:results_bar moved into fig:car_factorial (a)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "28c1da1d-8d20-419b-9d42-980261fa7c8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JQn286AiNAYcFm5aWDtjN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 51047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 38 · 2026-05-29T02:22:32.544Z_

<details><summary>↩ Tool result · `toolu_015VSm868CncKt2TSrCL2cwY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "4adead0b-007d-4c53-8eea-d19503c486ff",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
    "oldString": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1c_results_bar.pdf}\n\\caption{\\textbf{Only BN + gradient flow falls below Vanilla.} Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$, bootstrap 95\\% CI excludes zero). Under BatchNorm, gradient flow is associated with lower CAR (0.725 vs.\\ 0.745); LayerNorm eliminates this vulnerability. Error bars: cross-seed SD.}\n\\label{fig:results_bar}\n\\end{figure}",
    "newString": "% fig:results_bar moved into fig:car_factorial (a)",
    "originalFile": "\\section{Introduction}\n\nVision-language-action (VLA) models achieve high task success on manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}, but behavioral safety does not follow. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, OpenVLA-7B reaches 87.8\\% Task Success Rate but only 74.5\\% Collision Avoidance Rate (CAR), with collision rates of 43--93\\% on the three most constrained tasks.\n\nTwo active research threads address related but distinct aspects. The first enriches VLAs with auxiliary spatial prediction (occupancy grids, depth maps, point clouds)~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success under the implicit assumption that spatial awareness yields safer behavior. The second targets VLA safety directly through runtime action filtering~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained RL~\\cite{zhang2025safevla}. These lines are disconnected: no spatial method evaluates collision avoidance, and no safety method examines spatial representations. A recent survey~\\cite{li2026vlasafety} confirms this gap. Moreover, single-factor ablations---the dominant methodology---cannot decompose joint effects of multiple design choices; only a factorial design can determine whether factors like gradient flow and normalization type interact or combine independently.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_architecture_pb.pdf}\n\\caption{\\textbf{Training setup and factorial design.} \\textbf{(a)}~OpenVLA-7B with dual vision encoders (DINOv2 + SigLIP) and an auxiliary spatial head (BEV occupancy or depth), discarded at inference. \\textbf{(b)}~$2{\\times}2$ factorial crossing gradient flow (ON/OFF) and normalization (BN/LN), plus Vanilla baseline and 7 single-factor ablations probing label content, reference frame, and temporal extent.}\n\\label{fig:overview}\n\\end{figure*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1c_results_bar.pdf}\n\\caption{\\textbf{Only BN + gradient flow falls below Vanilla.} Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$, bootstrap 95\\% CI excludes zero). Under BatchNorm, gradient flow is associated with lower CAR (0.725 vs.\\ 0.745); LayerNorm eliminates this vulnerability. Error bars: cross-seed SD.}\n\\label{fig:results_bar}\n\\end{figure}\n\nWe ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\\cite{kim2024openvla} with LoRA~\\cite{hu2022lora}. A core $2{\\times}2$ factorial crosses gradient flow (ON/OFF) with normalization (BN/LN); seven additional single-factor ablations probe label content, spatial reference frame, and temporal extent---twelve conditions in total (Figure~\\ref{fig:overview}). The factorial design can detect interactions that single-factor studies miss; here, it establishes that the two main effects are additive ($p_{\\text{interaction}}{=}0.76$), a practically important finding that prior work could not have obtained.\n\nThe central finding is that \\textbf{Detach+LN reliably outperforms Vanilla} ($\\text{CAR}$ $0.802$ vs.\\ $0.745$; Hedges' $g{=}1.89$, bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$, $n{=}3$ vs $3$). The $2{\\times}2$ factorial reveals why: gradient flow under BN is associated with 4.2\\,pp lower CAR ($g{=}0.78$, large), and LN provides a 3.5--4.8\\,pp safety advantage ($g{\\approx}0.88$, large). Only the BN + gradient flow combination falls below Vanilla. Spatial label content showed no detectable effect (observed under v1 codebase; \\S\\ref{sec:results}).\n\nOur contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Detach+LN reliably improves safety.} Detached gradients with LayerNorm yield CAR $0.802$, reliably outperforming Vanilla $0.745$ (Hedges' $g{=}1.89$, bootstrap 95\\% CI $[0.025, 0.089]$). A $2{\\times}2$ factorial reveals two additive mechanisms: BN + gradient flow is the sole cell below baseline ($g{=}-0.78$, $\\sigma{=}0.064$); LN provides a 3.5--4.8\\,pp advantage ($g{\\approx}0.88$). Spatial content showed no detectable effect (observed under v1 codebase; Table~\\ref{tab:main_results}, Figure~\\ref{fig:factorial_gradient}a).\n\n    \\item \\textbf{Factorial methodology for VLA auxiliary heads.} The first systematic factorial comparison of how auxiliary head design choices combine during VLA fine-tuning, establishing that effects are additive---a conclusion single-factor ablations cannot reach (\\S\\ref{sec:ablation}, Table~\\ref{tab:ablation_design}).\n\n    \\item \\textbf{Actionable guidelines at zero cost.} Do not add auxiliary spatial heads with gradient flow under BN. If required, use detached gradients with LayerNorm. No ground-truth spatial labels are needed; the auxiliary head is discarded at inference (\\S\\ref{sec:discussion}).\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 11,
        "oldLines": 12,
        "newStart": 11,
        "newLines": 7,
        "lines": [
          " \\label{fig:overview}",
          " \\end{figure*}",
          " ",
          "-\\begin{figure}[t]",
          "-\\centering",
          "-\\includegraphics[width=\\columnwidth]{figures/fig1c_results_bar.pdf}",
          "-\\caption{\\textbf{Only BN + gradient flow falls below Vanilla.} Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$, bootstrap 95\\% CI excludes zero). Under BatchNorm, gradient flow is associated with lower CAR (0.725 vs.\\ 0.745); LayerNorm eliminates this vulnerability. Error bars: cross-seed SD.}",
          "-\\label{fig:results_bar}",
          "-\\end{figure}",
          "+% fig:results_bar moved into fig:car_factorial (a)",
          " ",
          " We ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\\cite{kim2024openvla} with LoRA~\\cite{hu2022lora}. A core $2{\\times}2$ factorial crosses gradient flow (ON/OFF) with normalization (BN/LN); seven additional single-factor ablations probe label content, spatial reference frame, and temporal extent---twelve conditions in total (Figure~\\ref{fig:overview}). The factorial design can detect interactions that single-factor studies miss; here, it establishes that the two main effects are additive ($p_{\\text{interaction}}{=}0.76$), a practically important finding that prior work could not have obtained.",
          " "
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

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_01BHTomSHZG92WhtfQwJ4DiP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_combined_factorial_gradient.pdf}\n\\caption{(a)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline. Error bars: cross-seed SD ($n{=}3$--$4$ per cell). (b)~Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\\approx}$46\\% conflict rate), confirming orthogonality.}\n\\label{fig:factorial_gradient}\n\\end{figure*}",
  "new_string": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_car_factorial_combined.pdf}\n\\caption{(a)~Only BN + gradient flow falls below Vanilla. Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$). Under BatchNorm, gradient flow is associated with lower CAR; LayerNorm eliminates this vulnerability. Error bars: cross-seed SD. (b)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline.}\n\\label{fig:car_factorial}\n\\end{figure*}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "74e41361-289d-4f09-ac1e-ad0cf6cc7a59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JQn286AiNAYcFm5aWDtjN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 51047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 40 · 2026-05-29T02:22:42.121Z_

<details><summary>↩ Tool result · `toolu_01BHTomSHZG92WhtfQwJ4DiP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "154e588d-c038-428d-ac24-247f951d8c1e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_combined_factorial_gradient.pdf}\n\\caption{(a)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline. Error bars: cross-seed SD ($n{=}3$--$4$ per cell). (b)~Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\\approx}$46\\% conflict rate), confirming orthogonality.}\n\\label{fig:factorial_gradient}\n\\end{figure*}",
    "newString": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_car_factorial_combined.pdf}\n\\caption{(a)~Only BN + gradient flow falls below Vanilla. Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$). Under BatchNorm, gradient flow is associated with lower CAR; LayerNorm eliminates this vulnerability. Error bars: cross-seed SD. (b)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline.}\n\\label{fig:car_factorial}\n\\end{figure*}",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use permutation tests and Hedges' $g$ (bias-corrected effect size for small samples) against the Vanilla baseline.\n\n\\textbf{Detach+LN reliably outperforms Vanilla.} The best factorial configuration---detached gradients with LayerNorm---achieves CAR $0.802 \\pm 0.024$ ($n{=}3$), a $+5.7$\\,pp advantage over Vanilla ($0.745 \\pm 0.024$, $n{=}3$; Hedges' $g{=}1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$).\n\n\\textbf{Two additive main effects explain the advantage.} The $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial_gradient}a) reveals two large main effects with negligible interaction (permutation ANOVA, 10{,}000 permutations: gradient flow $p_\\text{perm}{=}0.050$; normalization $p_\\text{perm}{=}0.018$; interaction $p_\\text{perm}{=}0.774$; Appendix~\\ref{app:permutation}). Parametric ANOVA yields consistent trends (Appendix~\\ref{app:stat_power}). Under BatchNorm, gradient flow corresponds to lower safety: Full OCC (CAR $0.725$, $\\Delta{=}-2.0$\\,pp) is the sole cell below Vanilla, while Detach OCC recovers ($0.767$, $\\Delta{=}+2.2$\\,pp); the within-row deficit is 4.2\\,pp (Hedges' $g{=}0.78$, large). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.773$, $\\Delta{=}+2.8$\\,pp, $g{=}+0.90$) exceeds Vanilla, and Detach+LN yields the highest mean ($0.802 \\pm 0.024$, $\\Delta{=}+5.7$\\,pp, $g{=}+1.89$). LN provides a consistent 3.5--4.8\\,pp advantage over BN ($g{=}0.88$--$1.24$). The BN + gradient flow cell exhibits the highest instability ($\\sigma{=}0.064$, ${\\geq}\\,2{\\times}$ all others; $\\sigma \\leq 0.027$ for all other cells). After Bonferroni correction for all pairwise comparisons, no individual Welch $t$-test reaches $\\alpha{=}0.05$, consistent with $n{=}3$--$4$; we report effect sizes and planned-comparison bootstrap CIs (Appendix~\\ref{app:stat_power}). The normalization main effect reaches significance under permutation testing ($p_\\text{perm}{=}0.018$). Both effects amplify ${\\approx}3{\\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\\ref{app:per_task_factorial}). Spatial content does not detectably affect outcomes: Full OCC, Random OCC, and Depth fall within cross-seed variance ($p > 0.4$, observed under v1 for Random OCC and Depth).\n\n\\textbf{BN + gradient flow is associated with training instability.} Full OCC (BN) individual seeds range from $0.776$ (near Vanilla) to $0.654$ ($\\Delta{=}-9.1$\\,pp), spanning $12.2$\\,pp---more than double the range of any other cell. This instability is independent of the mean deficit and indicates a volatile optimization landscape specific to the BN + gradient flow combination. No other cell approaches this variance ($\\sigma \\leq 0.027$ vs.\\ $\\sigma{=}0.064$), consistent with BatchNorm's running-statistics mechanism amplifying stochastic sensitivity when auxiliary gradients flow through the shared encoders. Notably, TSR remains relatively stable across all conditions ($0.854$--$0.914$), indicating that the safety deficit is not accompanied by a proportional decline in task completion ability.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Results on SafeLIBERO Level~I (10 tasks, 50 rollouts/seed). Mean $\\pm$ SD across seeds. $\\Delta$CAR vs.\\ v2 Vanilla ($0.745$) for factorial conditions; vs.\\ v1 Vanilla ($0.780$) for supplementary. $^{a}$Highest variance. $^\\ddagger$2 seeds. $^\\star$v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\nFlow & Norm & $n$ & CAR & TSR & $\\Delta$CAR \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$2{\\times}2$ factorial (v2 code)}} \\\\\nON  & BN & 3 & $0.725 \\pm 0.064^{a}$ & $0.854 \\pm 0.052$ & $-$2.0 \\\\\nOFF & BN & 4 & $0.767 \\pm 0.024$ & $0.908 \\pm 0.026$ & $+$2.2 \\\\\nON  & LN & 4 & $0.773 \\pm 0.027$ & $0.914 \\pm 0.049$ & $+$2.8 \\\\\nOFF & LN & 3 & $0.802 \\pm 0.024$ & $0.911 \\pm 0.018$ & $+$5.7 \\\\\n\\addlinespace\n---  & Vanilla & 3 & $0.745 \\pm 0.024$ & $0.878 \\pm 0.032$ & --- \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Controls \\& supplementary (v1 code)}} \\\\\nON  & BN (Random)$^\\star$ & 3 & $0.789 \\pm 0.031$ & $0.869 \\pm 0.029$ & --- \\\\\nON  & --- (Depth)$^\\star$ & 4 & $0.780 \\pm 0.039$ & $0.889 \\pm 0.042$ & $0.0$ \\\\\nON  & BN (Cutoff@15K)$^\\ddagger$ & 2 & $0.782 \\pm 0.031$ & $0.883 \\pm 0.041$ & $+$0.2 \\\\\nON  & BN (Cutoff@25K)$^\\ddagger$ & 2 & $0.724 \\pm 0.051$ & $0.887 \\pm 0.061$ & $-$5.6 \\\\\nON  & BN (Cutoff@35K)       & 3 & $0.779 \\pm 0.017$ & $0.933 \\pm 0.032$ & $-$0.1 \\\\\nON  & BN (Cutoff@45K)       & 1 & $0.764$           & $0.896$           & $-$1.6 \\\\\nON  & BN (Rev.\\ Cutoff)$^\\ddagger$ & 2 & $0.718 \\pm 0.025$ & $0.839 \\pm 0.072$ & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow (all v2 data). Two main effects: gradient flow under BN $g{=}0.78$ (large); normalization effect $g{=}0.88$--$1.24$ (large to very large). BN + gradient flow is the sole cell below Vanilla. interaction $p_\\text{perm}{=}0.774$.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (0.767) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.773) & Detach+LN (0.802) & $-$2.9 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$4.8 ($g{=}{-}0.88$) & $-$3.5 ($g{=}{-}1.24$) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% Old Fig 2 (factorial standalone) — merged into fig:factorial_gradient below\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\columnwidth]{figures/factorial_2x2_pb.pdf}\n% \\caption{...}\n% \\label{fig:factorial_old}\n% \\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_combined_factorial_gradient.pdf}\n\\caption{(a)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline. Error bars: cross-seed SD ($n{=}3$--$4$ per cell). (b)~Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\\approx}$46\\% conflict rate), confirming orthogonality.}\n\\label{fig:factorial_gradient}\n\\end{figure*}\n\n\\subsection{Factorial Interpretation}\n\\label{sec:mechanism}\n\n\\textbf{Gradient flow is associated with lower safety under BatchNorm but not under LayerNorm.} The BN row provides the clearest signal: Full OCC (BN) is the sole factorial cell falling below Vanilla ($\\Delta{=}-2.0$\\,pp, $g{=}-0.34$ vs.\\ Vanilla), whereas Detach OCC recovers above it ($\\Delta{=}+2.2$\\,pp, $g{=}+0.74$, large). In the LN row, Full OCC+LN already exceeds Vanilla ($0.773$, $g{=}+0.90$, large), and Detach+LN yields the highest cell mean ($0.802$, $g{=}+1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$). This is a practical threshold crossing---only BN + gradient flow is associated with reduced safety---rather than a statistical interaction (the factorial interaction is negligible, $\\eta^2{=}0.005$). The numerical advantage of Detach OCC ($+$2.2\\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.\n\n\\textbf{Temporal dynamics.} Cutoff conditions illuminate when gradient flow's association with lower safety emerges. Cutoff@15K ($\\Delta{=}+0.2$\\,pp) performs near Vanilla, while Cutoff@25K shows a large deficit ($\\Delta{=}-5.6$\\,pp) and Cutoff@35K returns to baseline ($\\Delta{=}-0.1$\\,pp). Cutoff@45K ($\\Delta{=}-1.6$\\,pp, single seed) falls between these extremes. This non-monotonic pattern suggests that the critical window for gradient flow damage is not simply cumulative exposure but depends on the training phase. Reverse Cutoff (gradient flow only after step 35K) produces the worst supplementary result ($\\Delta{=}-6.2$\\,pp), indicating that late-stage gradient flow---when the model is refining action predictions---is associated with substantially worse outcomes than early exposure during initial representation learning. However, temporal conditions use 1--3 seeds under v1, so these observations are preliminary; targeted replication under v2 with more seeds would be needed to confirm the temporal pattern.\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:factorial_gradient}b) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n% Old Fig 3 (gradient standalone) — merged into fig:factorial_gradient above\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n% \\caption{...}\n% \\label{fig:gradient_analysis_old}\n% \\end{figure}\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:factorial_gradient}b), with conflict rates of ${\\approx}$46\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (Figure~\\ref{fig:factorial_gradient}b), ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)\n\n\\textbf{Mechanism remains open.} The observed effect pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The observed effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. Centered Kernel Alignment (CKA) analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP across all encoder layers), localizing the safety deficit to optimization dynamics rather than representational corruption. This high representational similarity is notable: even the worst-performing condition (Full OCC, BN) produces encoder features nearly identical to Vanilla, yet its action policy exhibits substantially worse collision avoidance. The dissociation between representational similarity and behavioral safety suggests that subtle differences in the LoRA adapter weights---invisible to CKA---drive the safety deficit.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
    "structuredPatch": [
      {
        "oldStart": 69,
        "oldLines": 9,
        "newStart": 69,
        "newLines": 9,
        "lines": [
          " ",
          " \\begin{figure*}[t]",
          " \\centering",
          "-\\includegraphics[width=\\textwidth]{figures/fig_combined_factorial_gradient.pdf}",
          "-\\caption{(a)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline. Error bars: cross-seed SD ($n{=}3$--$4$ per cell). (b)~Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\\approx}$46\\% conflict rate), confirming orthogonality.}",
          "-\\label{fig:factorial_gradient}",
          "+\\includegraphics[width=\\textwidth]{figures/fig_car_factorial_combined.pdf}",
          "+\\caption{(a)~Only BN + gradient flow falls below Vanilla. Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$). Under BatchNorm, gradient flow is associated with lower CAR; LayerNorm eliminates this vulnerability. Error bars: cross-seed SD. (b)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline.}",
          "+\\label{fig:car_factorial}",
          " \\end{figure*}",
          " ",
          " \\subsection{Factorial Interpretation}"
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

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_01ANnmaBz9sBXEfYL6qBL75S`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "% Old Fig 3 (gradient standalone) — merged into fig:factorial_gradient above\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n% \\caption{...}\n% \\label{fig:gradient_analysis_old}\n% \\end{figure}",
  "new_string": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\\approx}$46\\% conflict rate), confirming orthogonality.}\n\\label{fig:gradient_analysis}\n\\end{figure*}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "6ea7578b-6023-47ed-9c27-6cb9320d8312",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016JQn286AiNAYcFm5aWDtjN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 51047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 42 · 2026-05-29T02:22:45.139Z_

<details><summary>↩ Tool result · `toolu_01ANnmaBz9sBXEfYL6qBL75S`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "d3acafa6-8134-4ce0-9fdd-e4ba5f51c8be",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "% Old Fig 3 (gradient standalone) — merged into fig:factorial_gradient above\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n% \\caption{...}\n% \\label{fig:gradient_analysis_old}\n% \\end{figure}",
    "newString": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\\approx}$46\\% conflict rate), confirming orthogonality.}\n\\label{fig:gradient_analysis}\n\\end{figure*}",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use permutation tests and Hedges' $g$ (bias-corrected effect size for small samples) against the Vanilla baseline.\n\n\\textbf{Detach+LN reliably outperforms Vanilla.} The best factorial configuration---detached gradients with LayerNorm---achieves CAR $0.802 \\pm 0.024$ ($n{=}3$), a $+5.7$\\,pp advantage over Vanilla ($0.745 \\pm 0.024$, $n{=}3$; Hedges' $g{=}1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$).\n\n\\textbf{Two additive main effects explain the advantage.} The $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial_gradient}a) reveals two large main effects with negligible interaction (permutation ANOVA, 10{,}000 permutations: gradient flow $p_\\text{perm}{=}0.050$; normalization $p_\\text{perm}{=}0.018$; interaction $p_\\text{perm}{=}0.774$; Appendix~\\ref{app:permutation}). Parametric ANOVA yields consistent trends (Appendix~\\ref{app:stat_power}). Under BatchNorm, gradient flow corresponds to lower safety: Full OCC (CAR $0.725$, $\\Delta{=}-2.0$\\,pp) is the sole cell below Vanilla, while Detach OCC recovers ($0.767$, $\\Delta{=}+2.2$\\,pp); the within-row deficit is 4.2\\,pp (Hedges' $g{=}0.78$, large). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.773$, $\\Delta{=}+2.8$\\,pp, $g{=}+0.90$) exceeds Vanilla, and Detach+LN yields the highest mean ($0.802 \\pm 0.024$, $\\Delta{=}+5.7$\\,pp, $g{=}+1.89$). LN provides a consistent 3.5--4.8\\,pp advantage over BN ($g{=}0.88$--$1.24$). The BN + gradient flow cell exhibits the highest instability ($\\sigma{=}0.064$, ${\\geq}\\,2{\\times}$ all others; $\\sigma \\leq 0.027$ for all other cells). After Bonferroni correction for all pairwise comparisons, no individual Welch $t$-test reaches $\\alpha{=}0.05$, consistent with $n{=}3$--$4$; we report effect sizes and planned-comparison bootstrap CIs (Appendix~\\ref{app:stat_power}). The normalization main effect reaches significance under permutation testing ($p_\\text{perm}{=}0.018$). Both effects amplify ${\\approx}3{\\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\\ref{app:per_task_factorial}). Spatial content does not detectably affect outcomes: Full OCC, Random OCC, and Depth fall within cross-seed variance ($p > 0.4$, observed under v1 for Random OCC and Depth).\n\n\\textbf{BN + gradient flow is associated with training instability.} Full OCC (BN) individual seeds range from $0.776$ (near Vanilla) to $0.654$ ($\\Delta{=}-9.1$\\,pp), spanning $12.2$\\,pp---more than double the range of any other cell. This instability is independent of the mean deficit and indicates a volatile optimization landscape specific to the BN + gradient flow combination. No other cell approaches this variance ($\\sigma \\leq 0.027$ vs.\\ $\\sigma{=}0.064$), consistent with BatchNorm's running-statistics mechanism amplifying stochastic sensitivity when auxiliary gradients flow through the shared encoders. Notably, TSR remains relatively stable across all conditions ($0.854$--$0.914$), indicating that the safety deficit is not accompanied by a proportional decline in task completion ability.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Results on SafeLIBERO Level~I (10 tasks, 50 rollouts/seed). Mean $\\pm$ SD across seeds. $\\Delta$CAR vs.\\ v2 Vanilla ($0.745$) for factorial conditions; vs.\\ v1 Vanilla ($0.780$) for supplementary. $^{a}$Highest variance. $^\\ddagger$2 seeds. $^\\star$v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\nFlow & Norm & $n$ & CAR & TSR & $\\Delta$CAR \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$2{\\times}2$ factorial (v2 code)}} \\\\\nON  & BN & 3 & $0.725 \\pm 0.064^{a}$ & $0.854 \\pm 0.052$ & $-$2.0 \\\\\nOFF & BN & 4 & $0.767 \\pm 0.024$ & $0.908 \\pm 0.026$ & $+$2.2 \\\\\nON  & LN & 4 & $0.773 \\pm 0.027$ & $0.914 \\pm 0.049$ & $+$2.8 \\\\\nOFF & LN & 3 & $0.802 \\pm 0.024$ & $0.911 \\pm 0.018$ & $+$5.7 \\\\\n\\addlinespace\n---  & Vanilla & 3 & $0.745 \\pm 0.024$ & $0.878 \\pm 0.032$ & --- \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Controls \\& supplementary (v1 code)}} \\\\\nON  & BN (Random)$^\\star$ & 3 & $0.789 \\pm 0.031$ & $0.869 \\pm 0.029$ & --- \\\\\nON  & --- (Depth)$^\\star$ & 4 & $0.780 \\pm 0.039$ & $0.889 \\pm 0.042$ & $0.0$ \\\\\nON  & BN (Cutoff@15K)$^\\ddagger$ & 2 & $0.782 \\pm 0.031$ & $0.883 \\pm 0.041$ & $+$0.2 \\\\\nON  & BN (Cutoff@25K)$^\\ddagger$ & 2 & $0.724 \\pm 0.051$ & $0.887 \\pm 0.061$ & $-$5.6 \\\\\nON  & BN (Cutoff@35K)       & 3 & $0.779 \\pm 0.017$ & $0.933 \\pm 0.032$ & $-$0.1 \\\\\nON  & BN (Cutoff@45K)       & 1 & $0.764$           & $0.896$           & $-$1.6 \\\\\nON  & BN (Rev.\\ Cutoff)$^\\ddagger$ & 2 & $0.718 \\pm 0.025$ & $0.839 \\pm 0.072$ & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow (all v2 data). Two main effects: gradient flow under BN $g{=}0.78$ (large); normalization effect $g{=}0.88$--$1.24$ (large to very large). BN + gradient flow is the sole cell below Vanilla. interaction $p_\\text{perm}{=}0.774$.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (0.767) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.773) & Detach+LN (0.802) & $-$2.9 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$4.8 ($g{=}{-}0.88$) & $-$3.5 ($g{=}{-}1.24$) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% Old Fig 2 (factorial standalone) — merged into fig:factorial_gradient below\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\columnwidth]{figures/factorial_2x2_pb.pdf}\n% \\caption{...}\n% \\label{fig:factorial_old}\n% \\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_car_factorial_combined.pdf}\n\\caption{(a)~Only BN + gradient flow falls below Vanilla. Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$). Under BatchNorm, gradient flow is associated with lower CAR; LayerNorm eliminates this vulnerability. Error bars: cross-seed SD. (b)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline.}\n\\label{fig:car_factorial}\n\\end{figure*}\n\n\\subsection{Factorial Interpretation}\n\\label{sec:mechanism}\n\n\\textbf{Gradient flow is associated with lower safety under BatchNorm but not under LayerNorm.} The BN row provides the clearest signal: Full OCC (BN) is the sole factorial cell falling below Vanilla ($\\Delta{=}-2.0$\\,pp, $g{=}-0.34$ vs.\\ Vanilla), whereas Detach OCC recovers above it ($\\Delta{=}+2.2$\\,pp, $g{=}+0.74$, large). In the LN row, Full OCC+LN already exceeds Vanilla ($0.773$, $g{=}+0.90$, large), and Detach+LN yields the highest cell mean ($0.802$, $g{=}+1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$). This is a practical threshold crossing---only BN + gradient flow is associated with reduced safety---rather than a statistical interaction (the factorial interaction is negligible, $\\eta^2{=}0.005$). The numerical advantage of Detach OCC ($+$2.2\\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.\n\n\\textbf{Temporal dynamics.} Cutoff conditions illuminate when gradient flow's association with lower safety emerges. Cutoff@15K ($\\Delta{=}+0.2$\\,pp) performs near Vanilla, while Cutoff@25K shows a large deficit ($\\Delta{=}-5.6$\\,pp) and Cutoff@35K returns to baseline ($\\Delta{=}-0.1$\\,pp). Cutoff@45K ($\\Delta{=}-1.6$\\,pp, single seed) falls between these extremes. This non-monotonic pattern suggests that the critical window for gradient flow damage is not simply cumulative exposure but depends on the training phase. Reverse Cutoff (gradient flow only after step 35K) produces the worst supplementary result ($\\Delta{=}-6.2$\\,pp), indicating that late-stage gradient flow---when the model is refining action predictions---is associated with substantially worse outcomes than early exposure during initial representation learning. However, temporal conditions use 1--3 seeds under v1, so these observations are preliminary; targeted replication under v2 with more seeds would be needed to confirm the temporal pattern.\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:factorial_gradient}b) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n% Old Fig 3 (gradient standalone) — merged into fig:factorial_gradient above\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n% \\caption{...}\n% \\label{fig:gradient_analysis_old}\n% \\end{figure}\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:factorial_gradient}b), with conflict rates of ${\\approx}$46\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (Figure~\\ref{fig:factorial_gradient}b), ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)\n\n\\textbf{Mechanism remains open.} The observed effect pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The observed effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. Centered Kernel Alignment (CKA) analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP across all encoder layers), localizing the safety deficit to optimization dynamics rather than representational corruption. This high representational similarity is notable: even the worst-performing condition (Full OCC, BN) produces encoder features nearly identical to Vanilla, yet its action policy exhibits substantially worse collision avoidance. The dissociation between representational similarity and behavioral safety suggests that subtle differences in the LoRA adapter weights---invisible to CKA---drive the safety deficit.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
    "structuredPatch": [
      {
        "oldStart": 85,
        "oldLines": 13,
        "newStart": 85,
        "newLines": 12,
        "lines": [
          " ",
          " Gradient analysis (Figure~\\ref{fig:factorial_gradient}b) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).",
          " ",
          "-% Old Fig 3 (gradient standalone) — merged into fig:factorial_gradient above",
          "-% \\begin{figure}[t]",
          "-% \\centering",
          "-% \\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}",
          "-% \\caption{...}",
          "-% \\label{fig:gradient_analysis_old}",
          "-% \\end{figure}",
          "+\\begin{figure*}[t]",
          "+\\centering",
          "+\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}",
          "+\\caption{Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\\approx}$46\\% conflict rate), confirming orthogonality.}",
          "+\\label{fig:gradient_analysis}",
          "+\\end{figure*}",
          " ",
          " \\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:factorial_gradient}b), with conflict rates of ${\\approx}$46\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (Figure~\\ref{fig:factorial_gradient}b), ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)",
          " "
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

_source line 43_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01JzbSwgyXMvrSTqs9nXAaQg`</summary>

```json
{
  "todos": [
    {
      "content": "Create fig_car_factorial_combined.py script",
      "status": "completed",
      "activeForm": "Creating combined figure script"
    },
    {
      "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
      "status": "completed",
      "activeForm": "Updating LaTeX files"
    },
    {
      "content": "Update all \\ref{} cross-references across paper",
      "status": "in_progress",
      "activeForm": "Updating cross-references"
    },
    {
      "content": "Run script and visually verify output",
      "status": "pending",
      "activeForm": "Running script and verifying output"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "b8b58e4a-b449-4480-8608-428c62a58bb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eam61kdpMvpsNEr4eQ3nHi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1520,
      "cache_read_input_tokens": 51281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1520
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

_source line 44 · 2026-05-29T02:22:48.689Z_

<details><summary>↩ Tool result · `toolu_01JzbSwgyXMvrSTqs9nXAaQg`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "d6d7df72-0910-4aaf-a771-d88dddb5ce54",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Create fig_car_factorial_combined.py script",
        "status": "completed",
        "activeForm": "Creating combined figure script"
      },
      {
        "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
        "status": "in_progress",
        "activeForm": "Updating LaTeX files"
      },
      {
        "content": "Update all \\ref{} cross-references across paper",
        "status": "pending",
        "activeForm": "Updating cross-references"
      },
      {
        "content": "Run script and visually verify output",
        "status": "pending",
        "activeForm": "Running script and verifying output"
      }
    ],
    "newTodos": [
      {
        "content": "Create fig_car_factorial_combined.py script",
        "status": "completed",
        "activeForm": "Creating combined figure script"
      },
      {
        "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
        "status": "completed",
        "activeForm": "Updating LaTeX files"
      },
      {
        "content": "Update all \\ref{} cross-references across paper",
        "status": "in_progress",
        "activeForm": "Updating cross-references"
      },
      {
        "content": "Run script and visually verify output",
        "status": "pending",
        "activeForm": "Running script and verifying output"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 45_

Now updating all cross-references. The mapping is:
- `\ref{fig:factorial_gradient}a` → `\ref{fig:car_factorial}b` (factorial)
- `\ref{fig:factorial_gradient}b` → `\ref{fig:gradient_analysis}` (gradient)
- `\ref{fig:factorial_gradient}` alone → context-dependent

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "2ab34a7d-5d2c-41ce-8f06-4f0ea91be7af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019d4TLuanRP6zSPgS4AMtS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 52801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_016dr4FuTnyqicskJncCREfb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
  "old_string": "Figure~\\ref{fig:factorial_gradient}a)",
  "new_string": "Figure~\\ref{fig:car_factorial}b)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "dac6d16c-e9ea-4302-8e61-33f69299978d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019d4TLuanRP6zSPgS4AMtS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 52801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 47 · 2026-05-29T02:22:53.698Z_

<details><summary>↩ Tool result · `toolu_016dr4FuTnyqicskJncCREfb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "6fd63c43-a94d-497e-b208-8442e56a8dec",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
    "oldString": "Figure~\\ref{fig:factorial_gradient}a)",
    "newString": "Figure~\\ref{fig:car_factorial}b)",
    "originalFile": "\\section{Introduction}\n\nVision-language-action (VLA) models achieve high task success on manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}, but behavioral safety does not follow. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, OpenVLA-7B reaches 87.8\\% Task Success Rate but only 74.5\\% Collision Avoidance Rate (CAR), with collision rates of 43--93\\% on the three most constrained tasks.\n\nTwo active research threads address related but distinct aspects. The first enriches VLAs with auxiliary spatial prediction (occupancy grids, depth maps, point clouds)~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success under the implicit assumption that spatial awareness yields safer behavior. The second targets VLA safety directly through runtime action filtering~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained RL~\\cite{zhang2025safevla}. These lines are disconnected: no spatial method evaluates collision avoidance, and no safety method examines spatial representations. A recent survey~\\cite{li2026vlasafety} confirms this gap. Moreover, single-factor ablations---the dominant methodology---cannot decompose joint effects of multiple design choices; only a factorial design can determine whether factors like gradient flow and normalization type interact or combine independently.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_architecture_pb.pdf}\n\\caption{\\textbf{Training setup and factorial design.} \\textbf{(a)}~OpenVLA-7B with dual vision encoders (DINOv2 + SigLIP) and an auxiliary spatial head (BEV occupancy or depth), discarded at inference. \\textbf{(b)}~$2{\\times}2$ factorial crossing gradient flow (ON/OFF) and normalization (BN/LN), plus Vanilla baseline and 7 single-factor ablations probing label content, reference frame, and temporal extent.}\n\\label{fig:overview}\n\\end{figure*}\n\n% fig:results_bar moved into fig:car_factorial (a)\n\nWe ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\\cite{kim2024openvla} with LoRA~\\cite{hu2022lora}. A core $2{\\times}2$ factorial crosses gradient flow (ON/OFF) with normalization (BN/LN); seven additional single-factor ablations probe label content, spatial reference frame, and temporal extent---twelve conditions in total (Figure~\\ref{fig:overview}). The factorial design can detect interactions that single-factor studies miss; here, it establishes that the two main effects are additive ($p_{\\text{interaction}}{=}0.76$), a practically important finding that prior work could not have obtained.\n\nThe central finding is that \\textbf{Detach+LN reliably outperforms Vanilla} ($\\text{CAR}$ $0.802$ vs.\\ $0.745$; Hedges' $g{=}1.89$, bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$, $n{=}3$ vs $3$). The $2{\\times}2$ factorial reveals why: gradient flow under BN is associated with 4.2\\,pp lower CAR ($g{=}0.78$, large), and LN provides a 3.5--4.8\\,pp safety advantage ($g{\\approx}0.88$, large). Only the BN + gradient flow combination falls below Vanilla. Spatial label content showed no detectable effect (observed under v1 codebase; \\S\\ref{sec:results}).\n\nOur contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Detach+LN reliably improves safety.} Detached gradients with LayerNorm yield CAR $0.802$, reliably outperforming Vanilla $0.745$ (Hedges' $g{=}1.89$, bootstrap 95\\% CI $[0.025, 0.089]$). A $2{\\times}2$ factorial reveals two additive mechanisms: BN + gradient flow is the sole cell below baseline ($g{=}-0.78$, $\\sigma{=}0.064$); LN provides a 3.5--4.8\\,pp advantage ($g{\\approx}0.88$). Spatial content showed no detectable effect (observed under v1 codebase; Table~\\ref{tab:main_results}, Figure~\\ref{fig:factorial_gradient}a).\n\n    \\item \\textbf{Factorial methodology for VLA auxiliary heads.} The first systematic factorial comparison of how auxiliary head design choices combine during VLA fine-tuning, establishing that effects are additive---a conclusion single-factor ablations cannot reach (\\S\\ref{sec:ablation}, Table~\\ref{tab:ablation_design}).\n\n    \\item \\textbf{Actionable guidelines at zero cost.} Do not add auxiliary spatial heads with gradient flow under BN. If required, use detached gradients with LayerNorm. No ground-truth spatial labels are needed; the auxiliary head is discarded at inference (\\S\\ref{sec:discussion}).\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 7,
        "newStart": 19,
        "newLines": 7,
        "lines": [
          " ",
          " Our contributions:",
          " \\begin{enumerate}[nosep,leftmargin=*]",
          "-    \\item \\textbf{Detach+LN reliably improves safety.} Detached gradients with LayerNorm yield CAR $0.802$, reliably outperforming Vanilla $0.745$ (Hedges' $g{=}1.89$, bootstrap 95\\% CI $[0.025, 0.089]$). A $2{\\times}2$ factorial reveals two additive mechanisms: BN + gradient flow is the sole cell below baseline ($g{=}-0.78$, $\\sigma{=}0.064$); LN provides a 3.5--4.8\\,pp advantage ($g{\\approx}0.88$). Spatial content showed no detectable effect (observed under v1 codebase; Table~\\ref{tab:main_results}, Figure~\\ref{fig:factorial_gradient}a).",
          "+    \\item \\textbf{Detach+LN reliably improves safety.} Detached gradients with LayerNorm yield CAR $0.802$, reliably outperforming Vanilla $0.745$ (Hedges' $g{=}1.89$, bootstrap 95\\% CI $[0.025, 0.089]$). A $2{\\times}2$ factorial reveals two additive mechanisms: BN + gradient flow is the sole cell below baseline ($g{=}-0.78$, $\\sigma{=}0.064$); LN provides a 3.5--4.8\\,pp advantage ($g{\\approx}0.88$). Spatial content showed no detectable effect (observed under v1 codebase; Table~\\ref{tab:main_results}, Figure~\\ref{fig:car_factorial}b).",
          " ",
          "     \\item \\textbf{Factorial methodology for VLA auxiliary heads.} The first systematic factorial comparison of how auxiliary head design choices combine during VLA fine-tuning, establishing that effects are additive---a conclusion single-factor ablations cannot reach (\\S\\ref{sec:ablation}, Table~\\ref{tab:ablation_design}).",
          " "
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

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01QjxHQZcxtvUPjNsWoQmWhZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "Figure~\\ref{fig:factorial_gradient}a)",
  "new_string": "Figure~\\ref{fig:car_factorial}b)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "e98a6133-d701-46e9-9861-edc396c2aebc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019d4TLuanRP6zSPgS4AMtS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 52801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 49 · 2026-05-29T02:22:54.995Z_

<details><summary>↩ Tool result · `toolu_01QjxHQZcxtvUPjNsWoQmWhZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "36bc2b5b-39e3-4ffd-83bd-e65d19d909bd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "Figure~\\ref{fig:factorial_gradient}a)",
    "newString": "Figure~\\ref{fig:car_factorial}b)",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use permutation tests and Hedges' $g$ (bias-corrected effect size for small samples) against the Vanilla baseline.\n\n\\textbf{Detach+LN reliably outperforms Vanilla.} The best factorial configuration---detached gradients with LayerNorm---achieves CAR $0.802 \\pm 0.024$ ($n{=}3$), a $+5.7$\\,pp advantage over Vanilla ($0.745 \\pm 0.024$, $n{=}3$; Hedges' $g{=}1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$).\n\n\\textbf{Two additive main effects explain the advantage.} The $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial_gradient}a) reveals two large main effects with negligible interaction (permutation ANOVA, 10{,}000 permutations: gradient flow $p_\\text{perm}{=}0.050$; normalization $p_\\text{perm}{=}0.018$; interaction $p_\\text{perm}{=}0.774$; Appendix~\\ref{app:permutation}). Parametric ANOVA yields consistent trends (Appendix~\\ref{app:stat_power}). Under BatchNorm, gradient flow corresponds to lower safety: Full OCC (CAR $0.725$, $\\Delta{=}-2.0$\\,pp) is the sole cell below Vanilla, while Detach OCC recovers ($0.767$, $\\Delta{=}+2.2$\\,pp); the within-row deficit is 4.2\\,pp (Hedges' $g{=}0.78$, large). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.773$, $\\Delta{=}+2.8$\\,pp, $g{=}+0.90$) exceeds Vanilla, and Detach+LN yields the highest mean ($0.802 \\pm 0.024$, $\\Delta{=}+5.7$\\,pp, $g{=}+1.89$). LN provides a consistent 3.5--4.8\\,pp advantage over BN ($g{=}0.88$--$1.24$). The BN + gradient flow cell exhibits the highest instability ($\\sigma{=}0.064$, ${\\geq}\\,2{\\times}$ all others; $\\sigma \\leq 0.027$ for all other cells). After Bonferroni correction for all pairwise comparisons, no individual Welch $t$-test reaches $\\alpha{=}0.05$, consistent with $n{=}3$--$4$; we report effect sizes and planned-comparison bootstrap CIs (Appendix~\\ref{app:stat_power}). The normalization main effect reaches significance under permutation testing ($p_\\text{perm}{=}0.018$). Both effects amplify ${\\approx}3{\\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\\ref{app:per_task_factorial}). Spatial content does not detectably affect outcomes: Full OCC, Random OCC, and Depth fall within cross-seed variance ($p > 0.4$, observed under v1 for Random OCC and Depth).\n\n\\textbf{BN + gradient flow is associated with training instability.} Full OCC (BN) individual seeds range from $0.776$ (near Vanilla) to $0.654$ ($\\Delta{=}-9.1$\\,pp), spanning $12.2$\\,pp---more than double the range of any other cell. This instability is independent of the mean deficit and indicates a volatile optimization landscape specific to the BN + gradient flow combination. No other cell approaches this variance ($\\sigma \\leq 0.027$ vs.\\ $\\sigma{=}0.064$), consistent with BatchNorm's running-statistics mechanism amplifying stochastic sensitivity when auxiliary gradients flow through the shared encoders. Notably, TSR remains relatively stable across all conditions ($0.854$--$0.914$), indicating that the safety deficit is not accompanied by a proportional decline in task completion ability.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Results on SafeLIBERO Level~I (10 tasks, 50 rollouts/seed). Mean $\\pm$ SD across seeds. $\\Delta$CAR vs.\\ v2 Vanilla ($0.745$) for factorial conditions; vs.\\ v1 Vanilla ($0.780$) for supplementary. $^{a}$Highest variance. $^\\ddagger$2 seeds. $^\\star$v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\nFlow & Norm & $n$ & CAR & TSR & $\\Delta$CAR \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$2{\\times}2$ factorial (v2 code)}} \\\\\nON  & BN & 3 & $0.725 \\pm 0.064^{a}$ & $0.854 \\pm 0.052$ & $-$2.0 \\\\\nOFF & BN & 4 & $0.767 \\pm 0.024$ & $0.908 \\pm 0.026$ & $+$2.2 \\\\\nON  & LN & 4 & $0.773 \\pm 0.027$ & $0.914 \\pm 0.049$ & $+$2.8 \\\\\nOFF & LN & 3 & $0.802 \\pm 0.024$ & $0.911 \\pm 0.018$ & $+$5.7 \\\\\n\\addlinespace\n---  & Vanilla & 3 & $0.745 \\pm 0.024$ & $0.878 \\pm 0.032$ & --- \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Controls \\& supplementary (v1 code)}} \\\\\nON  & BN (Random)$^\\star$ & 3 & $0.789 \\pm 0.031$ & $0.869 \\pm 0.029$ & --- \\\\\nON  & --- (Depth)$^\\star$ & 4 & $0.780 \\pm 0.039$ & $0.889 \\pm 0.042$ & $0.0$ \\\\\nON  & BN (Cutoff@15K)$^\\ddagger$ & 2 & $0.782 \\pm 0.031$ & $0.883 \\pm 0.041$ & $+$0.2 \\\\\nON  & BN (Cutoff@25K)$^\\ddagger$ & 2 & $0.724 \\pm 0.051$ & $0.887 \\pm 0.061$ & $-$5.6 \\\\\nON  & BN (Cutoff@35K)       & 3 & $0.779 \\pm 0.017$ & $0.933 \\pm 0.032$ & $-$0.1 \\\\\nON  & BN (Cutoff@45K)       & 1 & $0.764$           & $0.896$           & $-$1.6 \\\\\nON  & BN (Rev.\\ Cutoff)$^\\ddagger$ & 2 & $0.718 \\pm 0.025$ & $0.839 \\pm 0.072$ & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow (all v2 data). Two main effects: gradient flow under BN $g{=}0.78$ (large); normalization effect $g{=}0.88$--$1.24$ (large to very large). BN + gradient flow is the sole cell below Vanilla. interaction $p_\\text{perm}{=}0.774$.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (0.767) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.773) & Detach+LN (0.802) & $-$2.9 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$4.8 ($g{=}{-}0.88$) & $-$3.5 ($g{=}{-}1.24$) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% Old Fig 2 (factorial standalone) — merged into fig:factorial_gradient below\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\columnwidth]{figures/factorial_2x2_pb.pdf}\n% \\caption{...}\n% \\label{fig:factorial_old}\n% \\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_car_factorial_combined.pdf}\n\\caption{(a)~Only BN + gradient flow falls below Vanilla. Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$). Under BatchNorm, gradient flow is associated with lower CAR; LayerNorm eliminates this vulnerability. Error bars: cross-seed SD. (b)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline.}\n\\label{fig:car_factorial}\n\\end{figure*}\n\n\\subsection{Factorial Interpretation}\n\\label{sec:mechanism}\n\n\\textbf{Gradient flow is associated with lower safety under BatchNorm but not under LayerNorm.} The BN row provides the clearest signal: Full OCC (BN) is the sole factorial cell falling below Vanilla ($\\Delta{=}-2.0$\\,pp, $g{=}-0.34$ vs.\\ Vanilla), whereas Detach OCC recovers above it ($\\Delta{=}+2.2$\\,pp, $g{=}+0.74$, large). In the LN row, Full OCC+LN already exceeds Vanilla ($0.773$, $g{=}+0.90$, large), and Detach+LN yields the highest cell mean ($0.802$, $g{=}+1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$). This is a practical threshold crossing---only BN + gradient flow is associated with reduced safety---rather than a statistical interaction (the factorial interaction is negligible, $\\eta^2{=}0.005$). The numerical advantage of Detach OCC ($+$2.2\\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.\n\n\\textbf{Temporal dynamics.} Cutoff conditions illuminate when gradient flow's association with lower safety emerges. Cutoff@15K ($\\Delta{=}+0.2$\\,pp) performs near Vanilla, while Cutoff@25K shows a large deficit ($\\Delta{=}-5.6$\\,pp) and Cutoff@35K returns to baseline ($\\Delta{=}-0.1$\\,pp). Cutoff@45K ($\\Delta{=}-1.6$\\,pp, single seed) falls between these extremes. This non-monotonic pattern suggests that the critical window for gradient flow damage is not simply cumulative exposure but depends on the training phase. Reverse Cutoff (gradient flow only after step 35K) produces the worst supplementary result ($\\Delta{=}-6.2$\\,pp), indicating that late-stage gradient flow---when the model is refining action predictions---is associated with substantially worse outcomes than early exposure during initial representation learning. However, temporal conditions use 1--3 seeds under v1, so these observations are preliminary; targeted replication under v2 with more seeds would be needed to confirm the temporal pattern.\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:factorial_gradient}b) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\\approx}$46\\% conflict rate), confirming orthogonality.}\n\\label{fig:gradient_analysis}\n\\end{figure*}\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:factorial_gradient}b), with conflict rates of ${\\approx}$46\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (Figure~\\ref{fig:factorial_gradient}b), ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)\n\n\\textbf{Mechanism remains open.} The observed effect pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The observed effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. Centered Kernel Alignment (CKA) analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP across all encoder layers), localizing the safety deficit to optimization dynamics rather than representational corruption. This high representational similarity is notable: even the worst-performing condition (Full OCC, BN) produces encoder features nearly identical to Vanilla, yet its action policy exhibits substantially worse collision avoidance. The dissociation between representational similarity and behavioral safety suggests that subtle differences in the LoRA adapter weights---invisible to CKA---drive the safety deficit.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{Detach+LN reliably outperforms Vanilla.} The best factorial configuration---detached gradients with LayerNorm---achieves CAR $0.802 \\pm 0.024$ ($n{=}3$), a $+5.7$\\,pp advantage over Vanilla ($0.745 \\pm 0.024$, $n{=}3$; Hedges' $g{=}1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$).",
          " ",
          "-\\textbf{Two additive main effects explain the advantage.} The $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:factorial_gradient}a) reveals two large main effects with negligible interaction (permutation ANOVA, 10{,}000 permutations: gradient flow $p_\\text{perm}{=}0.050$; normalization $p_\\text{perm}{=}0.018$; interaction $p_\\text{perm}{=}0.774$; Appendix~\\ref{app:permutation}). Parametric ANOVA yields consistent trends (Appendix~\\ref{app:stat_power}). Under BatchNorm, gradient flow corresponds to lower safety: Full OCC (CAR $0.725$, $\\Delta{=}-2.0$\\,pp) is the sole cell below Vanilla, while Detach OCC recovers ($0.767$, $\\Delta{=}+2.2$\\,pp); the within-row deficit is 4.2\\,pp (Hedges' $g{=}0.78$, large). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.773$, $\\Delta{=}+2.8$\\,pp, $g{=}+0.90$) exceeds Vanilla, and Detach+LN yields the highest mean ($0.802 \\pm 0.024$, $\\Delta{=}+5.7$\\,pp, $g{=}+1.89$). LN provides a consistent 3.5--4.8\\,pp advantage over BN ($g{=}0.88$--$1.24$). The BN + gradient flow cell exhibits the highest instability ($\\sigma{=}0.064$, ${\\geq}\\,2{\\times}$ all others; $\\sigma \\leq 0.027$ for all other cells). After Bonferroni correction for all pairwise comparisons, no individual Welch $t$-test reaches $\\alpha{=}0.05$, consistent with $n{=}3$--$4$; we report effect sizes and planned-comparison bootstrap CIs (Appendix~\\ref{app:stat_power}). The normalization main effect reaches significance under permutation testing ($p_\\text{perm}{=}0.018$). Both effects amplify ${\\approx}3{\\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\\ref{app:per_task_factorial}). Spatial content does not detectably affect outcomes: Full OCC, Random OCC, and Depth fall within cross-seed variance ($p > 0.4$, observed under v1 for Random OCC and Depth).",
          "+\\textbf{Two additive main effects explain the advantage.} The $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:car_factorial}b) reveals two large main effects with negligible interaction (permutation ANOVA, 10{,}000 permutations: gradient flow $p_\\text{perm}{=}0.050$; normalization $p_\\text{perm}{=}0.018$; interaction $p_\\text{perm}{=}0.774$; Appendix~\\ref{app:permutation}). Parametric ANOVA yields consistent trends (Appendix~\\ref{app:stat_power}). Under BatchNorm, gradient flow corresponds to lower safety: Full OCC (CAR $0.725$, $\\Delta{=}-2.0$\\,pp) is the sole cell below Vanilla, while Detach OCC recovers ($0.767$, $\\Delta{=}+2.2$\\,pp); the within-row deficit is 4.2\\,pp (Hedges' $g{=}0.78$, large). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.773$, $\\Delta{=}+2.8$\\,pp, $g{=}+0.90$) exceeds Vanilla, and Detach+LN yields the highest mean ($0.802 \\pm 0.024$, $\\Delta{=}+5.7$\\,pp, $g{=}+1.89$). LN provides a consistent 3.5--4.8\\,pp advantage over BN ($g{=}0.88$--$1.24$). The BN + gradient flow cell exhibits the highest instability ($\\sigma{=}0.064$, ${\\geq}\\,2{\\times}$ all others; $\\sigma \\leq 0.027$ for all other cells). After Bonferroni correction for all pairwise comparisons, no individual Welch $t$-test reaches $\\alpha{=}0.05$, consistent with $n{=}3$--$4$; we report effect sizes and planned-comparison bootstrap CIs (Appendix~\\ref{app:stat_power}). The normalization main effect reaches significance under permutation testing ($p_\\text{perm}{=}0.018$). Both effects amplify ${\\approx}3{\\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\\ref{app:per_task_factorial}). Spatial content does not detectably affect outcomes: Full OCC, Random OCC, and Depth fall within cross-seed variance ($p > 0.4$, observed under v1 for Random OCC and Depth).",
          " ",
          " \\textbf{BN + gradient flow is associated with training instability.} Full OCC (BN) individual seeds range from $0.776$ (near Vanilla) to $0.654$ ($\\Delta{=}-9.1$\\,pp), spanning $12.2$\\,pp---more than double the range of any other cell. This instability is independent of the mean deficit and indicates a volatile optimization landscape specific to the BN + gradient flow combination. No other cell approaches this variance ($\\sigma \\leq 0.027$ vs.\\ $\\sigma{=}0.064$), consistent with BatchNorm's running-statistics mechanism amplifying stochastic sensitivity when auxiliary gradients flow through the shared encoders. Notably, TSR remains relatively stable across all conditions ($0.854$--$0.914$), indicating that the safety deficit is not accompanied by a proportional decline in task completion ability.",
          " "
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

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01N9u9fySzYaAihntVvn4xkT`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "old_string": "Figure~\\ref{fig:factorial_gradient}b)",
  "new_string": "Figure~\\ref{fig:gradient_analysis})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "609d757a-109b-41a8-a440-0f495fcd53cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019d4TLuanRP6zSPgS4AMtS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 52801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 51 · 2026-05-29T02:22:55.938Z_

<details><summary>↩ Tool result · `toolu_01N9u9fySzYaAihntVvn4xkT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "f30f5757-656a-43df-9d9f-abbb8a42086b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
    "oldString": "Figure~\\ref{fig:factorial_gradient}b)",
    "newString": "Figure~\\ref{fig:gradient_analysis})",
    "originalFile": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main_results} summarizes TSR and CAR across conditions (50 rollouts $\\times$ 10 tasks per seed). $\\Delta$CAR is computed against the matched-codebase Vanilla baseline (v2: $0.745 \\pm 0.024$, 3 seeds, for factorial conditions above the midrule; v1: 0.780 for supplementary conditions below). Random OCC ($^\\star$) uses v1 code but is included above the midrule as a factorial control; its $\\Delta$CAR is omitted due to the cross-codebase baseline mismatch. Statistical comparisons use permutation tests and Hedges' $g$ (bias-corrected effect size for small samples) against the Vanilla baseline.\n\n\\textbf{Detach+LN reliably outperforms Vanilla.} The best factorial configuration---detached gradients with LayerNorm---achieves CAR $0.802 \\pm 0.024$ ($n{=}3$), a $+5.7$\\,pp advantage over Vanilla ($0.745 \\pm 0.024$, $n{=}3$; Hedges' $g{=}1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$).\n\n\\textbf{Two additive main effects explain the advantage.} The $2{\\times}2$ factorial (Table~\\ref{tab:factorial}, Figure~\\ref{fig:car_factorial}b) reveals two large main effects with negligible interaction (permutation ANOVA, 10{,}000 permutations: gradient flow $p_\\text{perm}{=}0.050$; normalization $p_\\text{perm}{=}0.018$; interaction $p_\\text{perm}{=}0.774$; Appendix~\\ref{app:permutation}). Parametric ANOVA yields consistent trends (Appendix~\\ref{app:stat_power}). Under BatchNorm, gradient flow corresponds to lower safety: Full OCC (CAR $0.725$, $\\Delta{=}-2.0$\\,pp) is the sole cell below Vanilla, while Detach OCC recovers ($0.767$, $\\Delta{=}+2.2$\\,pp); the within-row deficit is 4.2\\,pp (Hedges' $g{=}0.78$, large). Under LayerNorm, gradient flow is benign: Full OCC+LN ($0.773$, $\\Delta{=}+2.8$\\,pp, $g{=}+0.90$) exceeds Vanilla, and Detach+LN yields the highest mean ($0.802 \\pm 0.024$, $\\Delta{=}+5.7$\\,pp, $g{=}+1.89$). LN provides a consistent 3.5--4.8\\,pp advantage over BN ($g{=}0.88$--$1.24$). The BN + gradient flow cell exhibits the highest instability ($\\sigma{=}0.064$, ${\\geq}\\,2{\\times}$ all others; $\\sigma \\leq 0.027$ for all other cells). After Bonferroni correction for all pairwise comparisons, no individual Welch $t$-test reaches $\\alpha{=}0.05$, consistent with $n{=}3$--$4$; we report effect sizes and planned-comparison bootstrap CIs (Appendix~\\ref{app:stat_power}). The normalization main effect reaches significance under permutation testing ($p_\\text{perm}{=}0.018$). Both effects amplify ${\\approx}3{\\times}$ on the three physically constrained tasks (T3, T5, T6; Appendix~\\ref{app:per_task_factorial}). Spatial content does not detectably affect outcomes: Full OCC, Random OCC, and Depth fall within cross-seed variance ($p > 0.4$, observed under v1 for Random OCC and Depth).\n\n\\textbf{BN + gradient flow is associated with training instability.} Full OCC (BN) individual seeds range from $0.776$ (near Vanilla) to $0.654$ ($\\Delta{=}-9.1$\\,pp), spanning $12.2$\\,pp---more than double the range of any other cell. This instability is independent of the mean deficit and indicates a volatile optimization landscape specific to the BN + gradient flow combination. No other cell approaches this variance ($\\sigma \\leq 0.027$ vs.\\ $\\sigma{=}0.064$), consistent with BatchNorm's running-statistics mechanism amplifying stochastic sensitivity when auxiliary gradients flow through the shared encoders. Notably, TSR remains relatively stable across all conditions ($0.854$--$0.914$), indicating that the safety deficit is not accompanied by a proportional decline in task completion ability.\n\n\n\\begin{table}[t]\n\\centering\n\\caption{Results on SafeLIBERO Level~I (10 tasks, 50 rollouts/seed). Mean $\\pm$ SD across seeds. $\\Delta$CAR vs.\\ v2 Vanilla ($0.745$) for factorial conditions; vs.\\ v1 Vanilla ($0.780$) for supplementary. $^{a}$Highest variance. $^\\ddagger$2 seeds. $^\\star$v1 code.}\n\\label{tab:main_results}\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccl}\n\\toprule\nFlow & Norm & $n$ & CAR & TSR & $\\Delta$CAR \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{$2{\\times}2$ factorial (v2 code)}} \\\\\nON  & BN & 3 & $0.725 \\pm 0.064^{a}$ & $0.854 \\pm 0.052$ & $-$2.0 \\\\\nOFF & BN & 4 & $0.767 \\pm 0.024$ & $0.908 \\pm 0.026$ & $+$2.2 \\\\\nON  & LN & 4 & $0.773 \\pm 0.027$ & $0.914 \\pm 0.049$ & $+$2.8 \\\\\nOFF & LN & 3 & $0.802 \\pm 0.024$ & $0.911 \\pm 0.018$ & $+$5.7 \\\\\n\\addlinespace\n---  & Vanilla & 3 & $0.745 \\pm 0.024$ & $0.878 \\pm 0.032$ & --- \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Controls \\& supplementary (v1 code)}} \\\\\nON  & BN (Random)$^\\star$ & 3 & $0.789 \\pm 0.031$ & $0.869 \\pm 0.029$ & --- \\\\\nON  & --- (Depth)$^\\star$ & 4 & $0.780 \\pm 0.039$ & $0.889 \\pm 0.042$ & $0.0$ \\\\\nON  & BN (Cutoff@15K)$^\\ddagger$ & 2 & $0.782 \\pm 0.031$ & $0.883 \\pm 0.041$ & $+$0.2 \\\\\nON  & BN (Cutoff@25K)$^\\ddagger$ & 2 & $0.724 \\pm 0.051$ & $0.887 \\pm 0.061$ & $-$5.6 \\\\\nON  & BN (Cutoff@35K)       & 3 & $0.779 \\pm 0.017$ & $0.933 \\pm 0.032$ & $-$0.1 \\\\\nON  & BN (Cutoff@45K)       & 1 & $0.764$           & $0.896$           & $-$1.6 \\\\\nON  & BN (Rev.\\ Cutoff)$^\\ddagger$ & 2 & $0.718 \\pm 0.025$ & $0.839 \\pm 0.072$ & $-$6.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{$2{\\times}2$ factorial: normalization type $\\times$ gradient flow (all v2 data). Two main effects: gradient flow under BN $g{=}0.78$ (large); normalization effect $g{=}0.88$--$1.24$ (large to very large). BN + gradient flow is the sole cell below Vanilla. interaction $p_\\text{perm}{=}0.774$.}\n\\label{tab:factorial}\n\\begin{tabular}{lccc}\n\\toprule\n & Gradient ON & Gradient OFF & $\\Delta$(ON$-$OFF) \\\\\n\\midrule\nBatchNorm    & Full OCC (0.725) & Detach OCC (0.767) & $-$4.2 \\\\\nLayerNorm    & Full OCC+LN (0.773) & Detach+LN (0.802) & $-$2.9 \\\\\n\\midrule\n$\\Delta$(BN$-$LN) & $-$4.8 ($g{=}{-}0.88$) & $-$3.5 ($g{=}{-}1.24$) & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% Old Fig 2 (factorial standalone) — merged into fig:factorial_gradient below\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\columnwidth]{figures/factorial_2x2_pb.pdf}\n% \\caption{...}\n% \\label{fig:factorial_old}\n% \\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_car_factorial_combined.pdf}\n\\caption{(a)~Only BN + gradient flow falls below Vanilla. Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$). Under BatchNorm, gradient flow is associated with lower CAR; LayerNorm eliminates this vulnerability. Error bars: cross-seed SD. (b)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline.}\n\\label{fig:car_factorial}\n\\end{figure*}\n\n\\subsection{Factorial Interpretation}\n\\label{sec:mechanism}\n\n\\textbf{Gradient flow is associated with lower safety under BatchNorm but not under LayerNorm.} The BN row provides the clearest signal: Full OCC (BN) is the sole factorial cell falling below Vanilla ($\\Delta{=}-2.0$\\,pp, $g{=}-0.34$ vs.\\ Vanilla), whereas Detach OCC recovers above it ($\\Delta{=}+2.2$\\,pp, $g{=}+0.74$, large). In the LN row, Full OCC+LN already exceeds Vanilla ($0.773$, $g{=}+0.90$, large), and Detach+LN yields the highest cell mean ($0.802$, $g{=}+1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$). This is a practical threshold crossing---only BN + gradient flow is associated with reduced safety---rather than a statistical interaction (the factorial interaction is negligible, $\\eta^2{=}0.005$). The numerical advantage of Detach OCC ($+$2.2\\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.\n\n\\textbf{Temporal dynamics.} Cutoff conditions illuminate when gradient flow's association with lower safety emerges. Cutoff@15K ($\\Delta{=}+0.2$\\,pp) performs near Vanilla, while Cutoff@25K shows a large deficit ($\\Delta{=}-5.6$\\,pp) and Cutoff@35K returns to baseline ($\\Delta{=}-0.1$\\,pp). Cutoff@45K ($\\Delta{=}-1.6$\\,pp, single seed) falls between these extremes. This non-monotonic pattern suggests that the critical window for gradient flow damage is not simply cumulative exposure but depends on the training phase. Reverse Cutoff (gradient flow only after step 35K) produces the worst supplementary result ($\\Delta{=}-6.2$\\,pp), indicating that late-stage gradient flow---when the model is refining action predictions---is associated with substantially worse outcomes than early exposure during initial representation learning. However, temporal conditions use 1--3 seeds under v1, so these observations are preliminary; targeted replication under v2 with more seeds would be needed to confirm the temporal pattern.\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:factorial_gradient}b) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\\approx}$46\\% conflict rate), confirming orthogonality.}\n\\label{fig:gradient_analysis}\n\\end{figure*}\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:factorial_gradient}b), with conflict rates of ${\\approx}$46\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (Figure~\\ref{fig:factorial_gradient}b), ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)\n\n\\textbf{Mechanism remains open.} The observed effect pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The observed effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. Centered Kernel Alignment (CKA) analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP across all encoder layers), localizing the safety deficit to optimization dynamics rather than representational corruption. This high representational similarity is notable: even the worst-performing condition (Full OCC, BN) produces encoder features nearly identical to Vanilla, yet its action policy exhibits substantially worse collision avoidance. The dissociation between representational similarity and behavioral safety suggests that subtle differences in the LoRA adapter weights---invisible to CKA---drive the safety deficit.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.\n",
    "structuredPatch": [
      {
        "oldStart": 83,
        "oldLines": 7,
        "newStart": 83,
        "newLines": 7,
        "lines": [
          " ",
          " \\subsection{Gradient Dynamics}",
          " ",
          "-Gradient analysis (Figure~\\ref{fig:factorial_gradient}b) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).",
          "+Gradient analysis (Figure~\\ref{fig:gradient_analysis}) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).",
          " ",
          " \\begin{figure*}[t]",
          " \\centering"
        ]
      },
      {
        "oldStart": 92,
        "oldLines": 7,
        "newStart": 92,
        "newLines": 7,
        "lines": [
          " \\label{fig:gradient_analysis}",
          " \\end{figure*}",
          " ",
          "-\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:factorial_gradient}b), with conflict rates of ${\\approx}$46\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (Figure~\\ref{fig:factorial_gradient}b), ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)",
          "+\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:gradient_analysis}), with conflict rates of ${\\approx}$46\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (Figure~\\ref{fig:gradient_analysis}), ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)",
          " ",
          " \\textbf{Mechanism remains open.} The observed effect pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The observed effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. Centered Kernel Alignment (CKA) analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP across all encoder layers), localizing the safety deficit to optimization dynamics rather than representational corruption. This high representational similarity is notable: even the worst-performing condition (Full OCC, BN) produces encoder features nearly identical to Vanilla, yet its action policy exhibits substantially worse collision avoidance. The dissociation between representational similarity and behavioral safety suggests that subtle differences in the LoRA adapter weights---invisible to CKA---drive the safety deficit.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01L68s1tb5TVuCA3u6XLchiY`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
  "old_string": "Figure~\\ref{fig:factorial_gradient}b)",
  "new_string": "Figure~\\ref{fig:gradient_analysis})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "53ef8da7-6370-4fce-accb-03712d099f3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019d4TLuanRP6zSPgS4AMtS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 52801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 53 · 2026-05-29T02:22:56.869Z_

<details><summary>↩ Tool result · `toolu_01L68s1tb5TVuCA3u6XLchiY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "97b9b05a-a77b-47b8-ae04-74baafc7e184",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/discussion.tex",
    "oldString": "Figure~\\ref{fig:factorial_gradient}b)",
    "newString": "Figure~\\ref{fig:gradient_analysis})",
    "originalFile": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\textbf{Excluded mechanism---gradient conflict.} Near-zero action--auxiliary cosine similarity (${\\approx}$46\\% conflict rate; Figure~\\ref{fig:factorial_gradient}b) and comparable action gradient norms (Figure~\\ref{fig:factorial_gradient}b) rule out PCGrad-style gradient conflict~\\cite{yu2020pcgrad}.\n%\n\\textbf{Hypothesis---BN forward-pass statistics corruption.} BatchNorm is not inherently harmful: Detach OCC (BN, gradient OFF) matches Vanilla ($0.767$ vs.\\ $0.745$, $p{=}0.28$); the deficit requires the joint presence of BN and gradient flow. We hypothesize a \\emph{forward-pass} mechanism: BN running mean/variance update during each forward pass regardless of gradient conflict, so the auxiliary head shifts the running statistics used at inference. LayerNorm, normalizing per-token without cross-batch statistics, lacks this coupling. CKA confirms intact encoder representations (CKA $\\geq$ 0.95), localizing the effect to optimization dynamics. This hypothesis remains unverified; targeted experiments (e.g., freezing running statistics or comparing train vs.\\ eval mode) would be needed.\n\n\\textbf{Normalization is independently associated with safety differences.} LN provides a consistent $+$3.5--4.8\\,pp advantage over BN ($g{=}0.88$--$1.24$); normalization type, typically treated as an implementation detail, has outsized consequences for safety-critical VLA fine-tuning.\n\n\\textbf{Additive protection model.} Detach+LN achieves the best safety (CAR $0.802$), reliably outperforming Vanilla ($g{=}1.89$, bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$). This advantage arises from two independent protections---detaching auxiliary gradients and switching to LayerNorm---each contributing ${\\approx}$4--5\\,pp, with negligible interaction ($\\eta^2{=}0.005$; Table~\\ref{tab:anova}). The observed value ($0.802$) is close to the additive prediction ($0.745 + 0.048 + 0.022 = 0.815$); only the BN + gradient flow cell falls below Vanilla, and removing either condition restores safety. Gradient orthogonality (cosine $\\approx$ 0) rules out direct conflict~\\cite{sener2018mgda, yu2020pcgrad, liu2021cagrad}; the effect likely operates through indirect reshaping of the LoRA optimization trajectory~\\cite{lippl2024implicit, jiang2023forkmerge}.\n\n\\textbf{Codebase sensitivity.} A code revision (v2) that fixed a batch-index resume bug shifts absolute CAR by up to 8.6\\,pp for the same seed (Vanilla stable, $<$1.5\\,pp), exceeding the magnitude of the experimental effects (${\\leq}5.7$\\,pp; Appendix~\\ref{app:codebase}). This demonstrates that non-hyperparameter implementation details can dominate the signal of interest---an independent finding with implications for VLA fine-tuning reproducibility.\n\n\\textbf{Content irrelevance.} Structured, random, and depth labels produce indistinguishable safety outcomes (observed under v1; v2 replication needed); the effect is driven by the mere presence of a secondary objective, consistent with action--auxiliary orthogonality.\n\n\\textbf{Safety--success dissociation.} Full OCC (BN) achieves $\\text{TSR}{=}0.854$ while exhibiting the worst CAR ($0.725$): safety and task success respond differently to auxiliary supervision~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}.\n\n\\textbf{Practical guideline.} For OpenVLA with LoRA fine-tuning on tabletop manipulation: do not add auxiliary spatial heads for safety purposes; if required for other reasons, use detached gradients with LayerNorm. Loss weighting~\\cite{kendall2018uncertainty} does not address the forward-pass BN mechanism. The auxiliary head is discarded at inference (zero overhead) and can complement runtime safety methods~\\cite{hu2025vlsa, raja2024ogmcbf}. Given the codebase sensitivity discussed above (up to 8.6\\,pp; Appendix~\\ref{app:codebase}), these guidelines should be verified in each specific VLA implementation.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " \\section{Discussion}",
          " \\label{sec:discussion}",
          " ",
          "-\\textbf{Excluded mechanism---gradient conflict.} Near-zero action--auxiliary cosine similarity (${\\approx}$46\\% conflict rate; Figure~\\ref{fig:factorial_gradient}b) and comparable action gradient norms (Figure~\\ref{fig:factorial_gradient}b) rule out PCGrad-style gradient conflict~\\cite{yu2020pcgrad}.",
          "+\\textbf{Excluded mechanism---gradient conflict.} Near-zero action--auxiliary cosine similarity (${\\approx}$46\\% conflict rate; Figure~\\ref{fig:gradient_analysis}) and comparable action gradient norms (Figure~\\ref{fig:gradient_analysis}) rule out PCGrad-style gradient conflict~\\cite{yu2020pcgrad}.",
          " %",
          " \\textbf{Hypothesis---BN forward-pass statistics corruption.} BatchNorm is not inherently harmful: Detach OCC (BN, gradient OFF) matches Vanilla ($0.767$ vs.\\ $0.745$, $p{=}0.28$); the deficit requires the joint presence of BN and gradient flow. We hypothesize a \\emph{forward-pass} mechanism: BN running mean/variance update during each forward pass regardless of gradient conflict, so the auxiliary head shifts the running statistics used at inference. LayerNorm, normalizing per-token without cross-batch statistics, lacks this coupling. CKA confirms intact encoder representations (CKA $\\geq$ 0.95), localizing the effect to optimization dynamics. This hypothesis remains unverified; targeted experiments (e.g., freezing running statistics or comparing train vs.\\ eval mode) would be needed.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_01RQbrmQeUTK4FtpGCBFDcLj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "% Figure~\\ref{fig:factorial_gradient}b is in the main text (Section~\\ref{sec:mechanism}).",
  "new_string": "% Figure~\\ref{fig:gradient_analysis} is in the main text (Section~\\ref{sec:mechanism})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "cc8717aa-8467-4754-97c7-c22d59309b6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019d4TLuanRP6zSPgS4AMtS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 52801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 55 · 2026-05-29T02:22:59.727Z_

<details><summary>↩ Tool result · `toolu_01RQbrmQeUTK4FtpGCBFDcLj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "55fe5884-09c7-4716-a193-26e4c4cee90b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "% Figure~\\ref{fig:factorial_gradient}b is in the main text (Section~\\ref{sec:mechanism}).",
    "newString": "% Figure~\\ref{fig:gradient_analysis} is in the main text (Section~\\ref{sec:mechanism}).",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Hedges' $g$ (bias-corrected for small samples) for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n% Figure~\\ref{fig:factorial_gradient}b is in the main text (Section~\\ref{sec:mechanism}).\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \\pm 0.024$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.7$\\,pp vs.\\ Vanilla, $g{=}+1.89$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:factorial_gradient}b) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into a regime associated with lower safety. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{=}0.10$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (14 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect does not reach significance ($p{=}0.104$) but shows a medium-to-large effect size ($\\eta^2{=}0.180$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.005$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Hedges' $g$ (bias-corrected) for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Hedges' $g$ (bias-corrected) for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Hedges' $g$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$0.88 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.78 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.28 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.22 \\\\\nCell~2 vs.\\ Cell~4 & $-$0.94 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.24 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.34 \\\\\nCell~2 vs.\\ Vanilla & $+$0.90 \\\\\nCell~3 vs.\\ Vanilla & $+$0.74 \\\\\nCell~4 vs.\\ Vanilla & $+$1.89 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Permutation-Based ANOVA}\n\\label{app:permutation}\n\nTo complement the parametric $F$-test (Table~\\ref{tab:anova}), we conduct a permutation-based ANOVA~\\cite{anderson2001permanova} that makes no distributional assumptions. Following standard practice for factorial designs~\\cite{montgomery2017doe}, we use the Type~II $F$-statistic as the test statistic and permute the 14 per-seed CAR values across all cells (10{,}000 permutations). The permutation $p$-value is the proportion of permuted $F$-statistics $\\geq$ the observed value.\n\n\\begin{table}[h]\n\\centering\n\\caption{Permutation-based ANOVA for the $2{\\times}2$ factorial (10{,}000 permutations). Both main effects are significant or near-significant; the interaction remains negligible.}\n\\label{tab:permanova}\n\\begin{tabular}{lccc}\n\\toprule\nSource & $p_\\text{parametric}$ & $p_\\text{perm}$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 0.104 & 0.050 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 0.060 & 0.018 & 0.253 \\\\\nInteraction & 0.763 & 0.774 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe permutation test yields stronger evidence for both main effects ($p_\\text{perm}{=}0.050$ and $0.018$) than the parametric $F$-test ($p{=}0.104$ and $0.060$), consistent with the parametric test being conservative for small, non-normal samples. The interaction remains negligible ($p_\\text{perm}{=}0.774$), confirming the additive pattern. The normalization main effect reaches significance at $\\alpha{=}0.05$ under permutation.\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $g{=}2.12$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($g{=}+1.05$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n% Limitations moved to main text\n",
    "structuredPatch": [
      {
        "oldStart": 75,
        "oldLines": 7,
        "newStart": 75,
        "newLines": 7,
        "lines": [
          " ",
          " \\section{Extended Analysis}",
          " ",
          "-% Figure~\\ref{fig:factorial_gradient}b is in the main text (Section~\\ref{sec:mechanism}).",
          "+% Figure~\\ref{fig:gradient_analysis} is in the main text (Section~\\ref{sec:mechanism}).",
          " ",
          " The Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \\pm 0.024$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.7$\\,pp vs.\\ Vanilla, $g{=}+1.89$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.",
          " "
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

_source line 56_

<details open><summary>🔧 Tool call — Edit · `toolu_01UuUpsPy7EaRJUrfdsjSFoY`</summary>

```json
{
  "replace_all": true,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
  "old_string": "Figure~\\ref{fig:factorial_gradient}b)",
  "new_string": "Figure~\\ref{fig:gradient_analysis})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "9f231702-9262-44fe-8ac2-04871ce56e87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019d4TLuanRP6zSPgS4AMtS2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 52801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 57 · 2026-05-29T02:22:59.935Z_

<details><summary>↩ Tool result · `toolu_01UuUpsPy7EaRJUrfdsjSFoY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex has been updated. All occurrences were successfully replaced.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "c96f8082-7fff-4060-bbef-18267ba7f0db",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex",
    "oldString": "Figure~\\ref{fig:factorial_gradient}b)",
    "newString": "Figure~\\ref{fig:gradient_analysis})",
    "originalFile": "\n\\section{Extended Per-Task Results}\n\\label{app:per_task}\n\nTable~\\ref{tab:per_task} reports per-task mean CAR across seeds for each condition. Seven tasks achieve CAR $\\geq$ 0.92 under Vanilla, while three physically constrained tasks (T3, T5, T6) fall below 0.58. The overall CAR differences reported in the main text are dominated by these three hard tasks, which average 0.342 compared to 0.968 for the seven easy tasks.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task mean CAR across seeds (50 rollouts per seed, v1 code). This table reports v1 codebase results retained for completeness; all main analyses use v2 data (Table~\\ref{tab:main_results}). All conditions use 3 seeds except Depth (4). Detach+LN per-task uses 2 seeds (s1, s2; s0 lacks per-task breakdown).}\n\\label{tab:per_task}\n\\begin{tabular}{clccccccc}\n\\toprule\n & & \\multicolumn{7}{c}{Mean CAR by Condition} \\\\\n\\cmidrule(lr){3-9}\nTask & Diff. & Vanilla & Full OCC & Random & Detach & Det+LN & Depth & Cut@35K \\\\\n\\midrule\nT0 & Easy  & 0.98 & 0.98 & 0.99 & 0.97 & 0.97 & 0.99 & 0.98 \\\\\nT1 & Easy  & 0.92 & 0.93 & 0.99 & 0.89 & 0.78 & 0.93 & 0.95 \\\\\nT2 & Easy  & 0.92 & 0.93 & 0.94 & 0.93 & 0.90 & 0.90 & 0.94 \\\\\nT3 & Hard  & 0.38 & 0.37 & 0.31 & \\textbf{0.11} & 0.44 & 0.50 & 0.55 \\\\\nT4 & Easy  & 0.98 & 0.99 & 0.95 & 0.98 & 0.96 & 0.92 & 0.97 \\\\\nT5 & Hard  & 0.07 & 0.17 & 0.23 & \\textbf{0.05} & 0.12 & 0.08 & 0.04 \\\\\nT6 & Hard  & 0.57 & 0.61 & 0.55 & 0.56 & 0.36 & 0.54 & 0.38 \\\\\nT7 & Easy  & 0.97 & 0.99 & 0.95 & 0.98 & 1.00 & 0.96 & 0.98 \\\\\nT8 & Easy  & 1.00 & 1.00 & 1.00 & 0.99 & 0.99 & 0.99 & 0.99 \\\\\nT9 & Easy  & 1.00 & 0.99 & 0.99 & 1.00 & 1.00 & 1.00 & 1.00 \\\\\n\\midrule\n\\multicolumn{2}{l}{Overall} & 0.780 & 0.797 & 0.789 & 0.746 & 0.765 & 0.780 & 0.779 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Ceiling effects.} On the seven easy tasks (T0--T2, T4, T7--T9), all conditions achieve CAR $\\geq$ 0.89, leaving minimal room for auxiliary training to improve performance. The obstacle is spatially separated from the manipulation path in these tasks.\n\n\\textbf{Hard task patterns.} On Task~5 (Vanilla CAR 0.07), gradient-flow conditions (Random OCC 0.23, Full OCC 0.17) exceed Vanilla and Detach (0.05), but all values remain below 0.23. Cutoff@35K achieves the highest T3 CAR (0.55) but the lowest T5 CAR (0.04), which illustrates task-specific temporal sensitivity. Depth exhibits high cross-seed variance on hard tasks (T3 range: 0.20--0.78; T6 range: 0.16--0.84), consistent with auxiliary supervision increasing seed sensitivity.\n\n\\section{Training Details}\n\\label{app:training}\n\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & OpenVLA-7B~\\cite{kim2024openvla} \\\\\nFine-tuning recipe & OFT~\\cite{kim2025oft} \\\\\nVision encoders & DINOv2 (1024-d) + SigLIP (1152-d) \\\\\nPatch token dim. & 2176 (concatenated) \\\\\nLoRA rank / $\\alpha$ & 32 / 16 \\\\\nLoRA trainable params & 110.8M (1.45\\% of 7.65B) \\\\\nOptimizer & AdamW (weight decay 0.01) \\\\\nBatch size & 8 \\\\\nLearning rate & $5 \\times 10^{-4}$ (constant) \\\\\nTraining steps & 50{,}000 \\\\\nAux.\\ loss weight $\\lambda_0$ & 0.01 \\\\\nAux.\\ loss decay & $\\exp(-t / 50{,}000)$ \\\\\nBEV grid resolution & $64 \\times 64$ \\\\\nFocal loss $\\alpha$ / $\\gamma$ & 0.25 / 2.0 \\\\\nDepth loss & Smooth-L1 \\\\\nAux.\\ head parameters & 1.2M \\\\\nHardware & NVIDIA RTX PRO 6000 (96\\,GB) \\\\\nWall time per run & $\\sim$12.9 hours \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Evaluation protocol.} Each condition uses 3+ seeds (Depth uses 4; Cutoff@15K, Cutoff@25K, and Reverse Cutoff use 2; Cutoff@45K uses 1) with 50 rollouts per task per seed (500 episodes per seed). A collision is registered when the L1 displacement of the obstacle's \\texttt{body\\_xpos} exceeds $10^{-3}$. Bootstrap 95\\% CIs are computed via 10{,}000 resamples (percentile method).\n\n\\textbf{Statistical tests.} Pairwise comparisons against Vanilla use two-tailed permutation tests on per-seed mean CARs with Hedges' $g$ (bias-corrected for small samples) for effect size. With $n{=}3$ seeds, statistical power is limited; we report $p$-values and effect sizes for transparency.\n\\textbf{CKA analysis.} Centered Kernel Alignment~\\cite{kornblith2019similarity} measures representational similarity between fine-tuned and pretrained encoder features. We extract patch token activations from the final layer of DINOv2 and SigLIP for 1{,}000 validation images, compute linear CKA per layer, and report the mean across layers. Higher CKA indicates better preservation of pretrained representations.\n\n\\textbf{Cutoff implementation.} As described in Section~\\ref{sec:ablation}, setting $\\lambda(t){=}0$ does not disable the auxiliary head's forward pass; the post-cutoff phase operates in Detach mode with BatchNorm statistics continuing to update (see the Cutoff description therein for details).\n\n\\section{Extended Analysis}\n\n% Figure~\\ref{fig:gradient_analysis} is in the main text (Section~\\ref{sec:mechanism}).\n\nThe Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \\pm 0.024$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.7$\\,pp vs.\\ Vanilla, $g{=}+1.89$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.\n\n\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:factorial_gradient}b) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n\\caption{Per-layer gradient analysis decomposed into amplitude and direction (v1 codebase checkpoint, seed 42, 200 batches). \\textbf{Top (a--b):} Action gradient norm heatmap (log scale). Gradient-flow conditions (Vanilla, Full OCC, Random OCC) maintain comparable norms; Detach shows substantially reduced norms across all layers, a v1-specific artifact not reproduced under v2 (see Appendix~\\ref{app:codebase}). \\textbf{Bottom (c--d):} Gradient conflict rate between action and auxiliary losses. DINOv2 maintains $\\sim$46\\% conflict (near-orthogonal), while SigLIP late layers drop to 19--25\\% (cooperative alignment). Both amplitude and directional patterns are identical for Full OCC and Random OCC, confirming architectural rather than label-dependent structure. Directional findings are confirmed under v2; the Detach amplitude suppression (a--b) is a v1 code-path artifact. Conflict rates approach ${\\approx}$46\\% in early and middle layers; late SigLIP layers show lower conflict rates (${\\approx}$25\\%), consistent with weak alignment rather than conflict.}\n\\label{fig:per_layer_combined}\n\\end{figure}\n\n\\subsection{Temporal Dynamics}\n\\label{app:temporal}\n\\textbf{Dose-response: gradient flow duration vs.\\ CAR (v1 data).} Figure~\\ref{fig:dose_response} plots CAR against the number of OCC gradient flow steps for the cutoff series (15K--45K, plus Detach at 0K and Full OCC at 50K; all v1 code). Cutoff@15K (2 seeds, CAR 0.782) clusters near Vanilla (0.780), while Cutoff@25K (2 seeds, 0.724) falls substantially below. Multi-seed conditions (Cutoff@35K and Full OCC) also cluster near the Vanilla baseline. Reverse Cutoff (late 15K) falls below the early-cutoff counterpart at the same gradient flow duration, consistent with the continuity hypothesis. The pattern suggests intermediate cutoff $\\approx$ Vanilla rather than a non-monotonic dose-response; the earlier single-seed Cutoff@15K result (0.804) was seed noise.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n\\caption{Dose-response: CAR vs.\\ OCC gradient flow duration (v1 codebase, all conditions). Filled circles: early-cutoff conditions with all 3 seeds completed; open circles: conditions with $\\leq$2 seeds (counts annotated as $n$). Diamond ($\\diamond$): Reverse Cutoff (gradient flow restricted to the last 15K steps). Dashed line: Vanilla 3-seed mean (v1); shaded band: $\\pm\\,$1\\,SE. The ``+0.2\\%'' annotation marks the Cutoff@15K--Vanilla gap. Intermediate cutoff conditions cluster near Vanilla, while Cutoff@25K and Reverse Cutoff fall substantially below.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\section{Additional Observations}\n\\label{app:additional}\n\n\\textbf{Per-task concentration.} Seven of ten tasks achieve CAR $\\geq$ 0.92 under Vanilla; overall CAR is dominated by three physically constrained tasks (T3, T5, T6; Section~\\ref{app:per_task}). Under the v1 codebase, Detach showed the lowest CAR on these hard tasks (T3: 0.11, T5: 0.05). However, this v1-specific pattern does not replicate under the controlled v2 factorial design (Table~\\ref{tab:main_results}), where detaching gradient flow consistently preserves safety (Detach OCC CAR 0.767 vs.\\ Vanilla 0.745); the v1 per-task pattern may reflect implementation-specific artifacts rather than a generalizable effect of gradient detachment.\n\n\\textbf{Egocentric depth matches Vanilla (v1 data).} Depth (4 seeds) achieves CAR 0.780 $\\pm$ 0.039, identical to Vanilla (v1, 0.780), despite providing per-pixel geometric information. Three label types (structured BEV, random binary, egocentric depth) yield comparable CAR when gradient flow is maintained.\n\n\\textbf{Temporal dynamics (preliminary, v1 data).} Cutoff@35K (3 seeds) achieves CAR 0.779, statistically indistinguishable from Vanilla (v1, $\\Delta = -$0.1\\,pp), which confirms that 35K steps of gradient flow fully protects collision avoidance. Surprisingly, Cutoff@25K (0.724, 2 seeds) and Reverse Cutoff (0.718, 2 seeds) fall substantially \\emph{below} Vanilla. The most parsimonious explanation: setting the loss weight to zero retains the auxiliary head forward pass, so the post-cutoff period operates in Detach mode; BatchNorm interference acts on representations shaped by gradient flow, without gradient compensation. This is not withdrawal from gradient flow \\emph{per se}, but transition into a regime associated with lower safety. Third seeds are in progress; extended analysis in Section~\\ref{app:temporal}.\n\n\\section{Codebase Sensitivity (v1 vs.\\ v2)}\n\\label{app:codebase}\n\nThe five core factorial conditions were retrained under a revised codebase (v2) that fixed a batch-index resume bug affecting cutoff timing and restructured the auxiliary head pipeline (module initialization order, data loading). All model architectures, hyperparameters, LoRA configuration, and evaluation protocols are identical between v1 and v2. The Vanilla baseline (no auxiliary head) is unaffected by these changes, since the revision touches only auxiliary-head code paths.\n\n\\textbf{Behavioral shift.} Under v1, Full OCC achieved a mean CAR of 0.797 (3 seeds, per-task Table~\\ref{tab:per_task}); under v2, the same condition yields 0.725 $\\pm$ 0.064 (Table~\\ref{tab:main_results}). Same-seed comparisons show shifts of up to 8.6\\,pp, while Vanilla remains stable across codebases ($<$1.5\\,pp). This sensitivity is confined to conditions with auxiliary heads and is itself informative: it indicates that auxiliary head training dynamics are fragile with respect to implementation details that would not normally be considered hyperparameters.\n\n\\textbf{Gradient analysis shift.} The v1 codebase exhibited a Detach gradient suppression artifact: Detach action-loss gradient norms were only $\\sim$4\\% of Vanilla norms across all encoder layers. In v2, this suppression disappears entirely (Detach/Vanilla ratio $\\approx$ 1.29), indicating that the v1 pattern was a code-path artifact rather than a genuine effect of gradient detachment. The gradient conflict rate also shifted from $\\sim$44\\% (v1) to $\\sim$46\\% (v2), with v2 values closer to the theoretical expectation for orthogonal vectors.\n\n\\textbf{Effect pattern shift.} Under v1, the normalization $\\times$ gradient flow pattern appeared as a crossover ($p{=}0.025$); under v2, both rows slope in the same direction, consistent with two additive main effects rather than an interaction (ANOVA interaction $F{=}0.10$, $p{=}0.76$, $\\eta^2{=}0.005$). The crossover pattern in v1 is likely attributable to the Detach gradient suppression artifact described above, which differentially affected BN and LN conditions. All main-text analyses use v2 data exclusively; v1 results are retained in the appendix for completeness and to document the sensitivity.\n\n\\textbf{Implication.} The codebase sensitivity reinforces our central finding: auxiliary spatial heads introduce optimization fragility that implementation details can amplify or attenuate. This fragility is a further argument against adding auxiliary spatial heads for safety purposes, since the safety outcome depends on implementation choices that are difficult to specify, reproduce, or audit.\n\n\\section{Statistical Power Analysis}\n\\label{app:stat_power}\n\nThe $2{\\times}2$ factorial design prioritizes breadth (12 conditions, 5 factors) over per-cell statistical power. With $n{=}3$--$4$ per cell (14 total observations), the design yields medium power for the observed effect sizes. The normalization main effect approaches significance ($p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect does not reach significance ($p{=}0.104$) but shows a medium-to-large effect size ($\\eta^2{=}0.180$). We report effect sizes as the primary inferential quantity.\n\nThe study's evidential strength rests on the consistent direction of both main effects: both BN and LN rows show lower CAR under gradient flow ON than OFF, and both gradient flow conditions show higher CAR under LN than BN. The negligible interaction ($\\eta^2{=}0.005$) confirms these effects are additive.\n\n\\textbf{Formal $2{\\times}2$ ANOVA.} Table~\\ref{tab:anova} reports the Type~II factorial analysis ($n{=}3$--$4$ per cell, 14 total observations). The interaction is negligible ($F(1,10){=}0.10$, $p{=}0.763$, $\\eta^2{=}0.005$), confirming additive main effects. The normalization main effect approaches significance ($F(1,10){=}4.49$, $p{=}0.060$, $\\eta^2{=}0.253$); the gradient flow main effect is medium-sized but non-significant ($F(1,10){=}3.20$, $p{=}0.104$, $\\eta^2{=}0.180$). The non-significant gradient flow $p$-value reflects limited per-cell power rather than an absent effect.\n\n\\begin{table}[h]\n\\centering\n\\caption{$2{\\times}2$ factorial ANOVA (Type~II SS). The interaction is negligible; the normalization main effect approaches significance ($p{=}0.060$).}\n\\label{tab:anova}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & $F$ & df & $p$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 3.20 & 1,\\,10 & 0.104 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 4.49 & 1,\\,10 & 0.060 & 0.253 \\\\\nInteraction & 0.10 & 1,\\,10 & 0.763 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\textbf{Pairwise effect sizes.} Table~\\ref{tab:pairwise} reports Hedges' $g$ (bias-corrected) for all factorial cell pairs and versus Vanilla ($n{=}3$--$4$ per cell).\n\n\\begin{table}[h]\n\\centering\n\\caption{Pairwise Hedges' $g$ (bias-corrected) for factorial cells and Vanilla.}\n\\label{tab:pairwise}\n\\small\n\\begin{tabular}{lc}\n\\toprule\nComparison & Hedges' $g$ \\\\\n\\midrule\nCell~1 (Full OCC BN) vs.\\ Cell~2 (Full OCC+LN) & $-$0.88 \\\\\nCell~1 vs.\\ Cell~3 (Detach OCC) & $-$0.78 \\\\\nCell~1 vs.\\ Cell~4 (Detach+LN) & $-$1.28 \\\\\nCell~2 vs.\\ Cell~3 & $+$0.22 \\\\\nCell~2 vs.\\ Cell~4 & $-$0.94 \\\\\nCell~3 vs.\\ Cell~4 & $-$1.24 \\\\\n\\addlinespace\nCell~1 vs.\\ Vanilla & $-$0.34 \\\\\nCell~2 vs.\\ Vanilla & $+$0.90 \\\\\nCell~3 vs.\\ Vanilla & $+$0.74 \\\\\nCell~4 vs.\\ Vanilla & $+$1.89 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Permutation-Based ANOVA}\n\\label{app:permutation}\n\nTo complement the parametric $F$-test (Table~\\ref{tab:anova}), we conduct a permutation-based ANOVA~\\cite{anderson2001permanova} that makes no distributional assumptions. Following standard practice for factorial designs~\\cite{montgomery2017doe}, we use the Type~II $F$-statistic as the test statistic and permute the 14 per-seed CAR values across all cells (10{,}000 permutations). The permutation $p$-value is the proportion of permuted $F$-statistics $\\geq$ the observed value.\n\n\\begin{table}[h]\n\\centering\n\\caption{Permutation-based ANOVA for the $2{\\times}2$ factorial (10{,}000 permutations). Both main effects are significant or near-significant; the interaction remains negligible.}\n\\label{tab:permanova}\n\\begin{tabular}{lccc}\n\\toprule\nSource & $p_\\text{parametric}$ & $p_\\text{perm}$ & $\\eta^2$ \\\\\n\\midrule\nGradient flow (ON vs.\\ OFF) & 0.104 & 0.050 & 0.180 \\\\\nNormalization (BN vs.\\ LN) & 0.060 & 0.018 & 0.253 \\\\\nInteraction & 0.763 & 0.774 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe permutation test yields stronger evidence for both main effects ($p_\\text{perm}{=}0.050$ and $0.018$) than the parametric $F$-test ($p{=}0.104$ and $0.060$), consistent with the parametric test being conservative for small, non-normal samples. The interaction remains negligible ($p_\\text{perm}{=}0.774$), confirming the additive pattern. The normalization main effect reaches significance at $\\alpha{=}0.05$ under permutation.\n\n\\section{Per-Task Factorial Analysis}\n\\label{app:per_task_factorial}\n\nThe three physically constrained tasks (T3: \\texttt{cookie\\_box}, T5: \\texttt{ramekin}, T6: \\texttt{next\\_to\\_cookie\\_box}) amplify both main effects by approximately $3{\\times}$ relative to the overall means.\n\n\\textbf{Normalization effect amplification.} The overall normalization effect ($\\Delta{=}+3.5$--$4.8$\\,pp between BN and LN) is amplified on constrained tasks. The LN ${>}$ BN direction is consistent across all three constrained tasks.\n\n\\textbf{Gradient flow on constrained tasks.} On T5 (ramekin), the best auxiliary condition versus Vanilla yields $g{=}2.12$, the largest per-task effect size observed. T5 also shows a reversed gradient flow direction ($g{=}+1.05$, ON ${>}$ OFF), but this reflects near-floor performance (CAR $0.04$--$0.19$) where absolute differences are small and floor artifacts are expected.\n\nThese per-task patterns suggest that the safety-relevant design choices (normalization type, gradient flow) are disproportionately consequential on physically constrained tasks where collision avoidance is most difficult.\n\n% Limitations moved to main text\n",
    "structuredPatch": [
      {
        "oldStart": 79,
        "oldLines": 7,
        "newStart": 79,
        "newLines": 7,
        "lines": [
          " ",
          " The Detach+LN ablation replaces BatchNorm2d with LayerNorm in the auxiliary head while retaining \\texttt{stop\\_gradient}. Under v1 (3 seeds), Detach+LN achieves CAR $0.765 \\pm 0.023$; under v2 ($n{=}3$), Detach+LN achieves $0.802 \\pm 0.024$ (Table~\\ref{tab:main_results}), the highest factorial cell mean ($\\Delta{=}+5.7$\\,pp vs.\\ Vanilla, $g{=}+1.89$). This confirms the additive main effects: both detaching gradient flow and using LN independently improve safety.",
          " ",
          "-\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:factorial_gradient}b) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.",
          "+\\textbf{Per-layer gradient analysis.} Figure~\\ref{fig:per_layer_combined} decomposes auxiliary gradient flow into two dimensions: amplitude (top row) and direction (bottom row). The amplitude heatmap (panels a--b) shows that Vanilla, Full OCC, and Random OCC maintain comparable action gradient norms across all layers (warm colors), while Detach shows substantially reduced norms across both encoders (dark). These amplitude results were generated from v1 codebase checkpoints. The v2 gradient analysis (Figure~\\ref{fig:gradient_analysis}) confirms that the Detach gradient suppression does not reproduce: Detach and gradient-flow conditions maintain comparable action gradient norms under v2, indicating the v1 suppression was a code-path artifact (see Appendix~\\ref{app:codebase}). The directional analysis (panels c--d) reveals encoder-specific alignment: DINOv2 conflict rates hover near 46\\% across all layers while SigLIP late layers (blocks 21--24) drop to 19--25\\%, which indicates cooperative gradient alignment in semantically rich layers. Both patterns are identical for Full OCC and Random OCC, which confirms they arise from architectural structure rather than label content. The aggregate conflict rates (Full OCC 45.6\\%, Full OCC+LN 45.7\\% under v2; Full OCC 44.1\\%, Random OCC 43.9\\% under v1) fall below the 50\\% expected for random vectors because they reflect this mixture of two encoder-specific patterns.",
          " ",
          " \\begin{figure}[h]",
          " \\centering"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": true
  }
}
```

</details>

---

### Assistant

_source line 58_

Now let me verify no stale references remain.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "82bff4fc-e38c-491f-9f6c-072aac8ea05d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjcSZ9JG4hGKb5YMfvDZgM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 53035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1438
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

_source line 59_

<details open><summary>🔧 Tool call — Grep · `toolu_013Y7oKG13aNpVDzJQX1jupw`</summary>

```json
{
  "pattern": "fig:factorial_gradient|fig:results_bar|fig:factorial_old|fig:gradient_analysis_old",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "f86bc63c-3071-46fb-84ae-1a3ff6830acc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjcSZ9JG4hGKb5YMfvDZgM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 53035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1438
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

_source line 60 · 2026-05-29T02:23:03.621Z_

<details><summary>↩ Tool result · `toolu_013Y7oKG13aNpVDzJQX1jupw`</summary>

```text
docs/paper/introduction.tex:14:% fig:results_bar moved into fig:car_factorial (a)
docs/paper/results.tex:62:% Old Fig 2 (factorial standalone) — merged into fig:factorial_gradient below
docs/paper/results.tex:67:% \label{fig:factorial_old}
docs/paper/main.aux:46:\newlabel{fig:results_bar}{{2}{3}{\textbf {Only BN + gradient flow falls below Vanilla.} Detach+LN achieves the highest CAR ($0.802{\pm }0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$, bootstrap 95\% CI excludes zero). Under BatchNorm, gradient flow is associated with lower CAR (0.725 vs.\ 0.745); LayerNorm eliminates this vulnerability. Error bars: cross-seed SD}{figure.caption.3}{}}
docs/paper/main.aux:70:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "3c88b40e-0f24-4545-9c00-53b63ee6f7b5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/introduction.tex:14:% fig:results_bar moved into fig:car_factorial (a)\ndocs/paper/results.tex:62:% Old Fig 2 (factorial standalone) — merged into fig:factorial_gradient below\ndocs/paper/results.tex:67:% \\label{fig:factorial_old}\ndocs/paper/main.aux:46:\\newlabel{fig:results_bar}{{2}{3}{\\textbf {Only BN + gradient flow falls below Vanilla.} Detach+LN achieves the highest CAR ($0.802{\\pm }0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$, bootstrap 95\\% CI excludes zero). Under BatchNorm, gradient flow is associated with lower CAR (0.725 vs.\\ 0.745); LayerNorm eliminates this vulnerability. Error bars: cross-seed SD}{figure.caption.3}{}}\ndocs/paper/main.aux:70:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
The remaining references are all in comments or in `main.aux` (which gets regenerated on LaTeX compile). No active references to the old labels remain. Good.

Now let me run the figure script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "e179ca84-e0c8-4e4f-be81-811af9b3fb77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3AE2QZ3Qk18Kd7gFeohkh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 440,
      "cache_read_input_tokens": 54473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 440
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

_source line 62_

All remaining hits are in comments or `main.aux` (auto-regenerated). No active references to old labels.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "4fd7b95e-fad0-43b4-9bae-092280a2d047",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3AE2QZ3Qk18Kd7gFeohkh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 440,
      "cache_read_input_tokens": 54473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 440
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

_source line 63_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01NqB7y8Cchc4r6a8FCfxFMG`</summary>

```json
{
  "todos": [
    {
      "content": "Create fig_car_factorial_combined.py script",
      "status": "completed",
      "activeForm": "Creating combined figure script"
    },
    {
      "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
      "status": "completed",
      "activeForm": "Updating LaTeX files"
    },
    {
      "content": "Update all \\ref{} cross-references across paper",
      "status": "completed",
      "activeForm": "Updating cross-references"
    },
    {
      "content": "Run script and visually verify output",
      "status": "in_progress",
      "activeForm": "Running script and verifying output"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "754de32c-8333-4dc6-9149-14b3b4c8a827",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3AE2QZ3Qk18Kd7gFeohkh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 440,
      "cache_read_input_tokens": 54473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 440
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

_source line 64 · 2026-05-29T02:23:09.013Z_

<details><summary>↩ Tool result · `toolu_01NqB7y8Cchc4r6a8FCfxFMG`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "6a69057a-0256-42ba-99e8-7671ecdd8faf",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Create fig_car_factorial_combined.py script",
        "status": "completed",
        "activeForm": "Creating combined figure script"
      },
      {
        "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
        "status": "completed",
        "activeForm": "Updating LaTeX files"
      },
      {
        "content": "Update all \\ref{} cross-references across paper",
        "status": "in_progress",
        "activeForm": "Updating cross-references"
      },
      {
        "content": "Run script and visually verify output",
        "status": "pending",
        "activeForm": "Running script and verifying output"
      }
    ],
    "newTodos": [
      {
        "content": "Create fig_car_factorial_combined.py script",
        "status": "completed",
        "activeForm": "Creating combined figure script"
      },
      {
        "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
        "status": "completed",
        "activeForm": "Updating LaTeX files"
      },
      {
        "content": "Update all \\ref{} cross-references across paper",
        "status": "completed",
        "activeForm": "Updating cross-references"
      },
      {
        "content": "Run script and visually verify output",
        "status": "in_progress",
        "activeForm": "Running script and verifying output"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01SUYRGHB76p23ZhfL3pkdj9`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures && python fig_car_factorial_combined.py",
  "description": "Run combined figure script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "b24fd24b-394b-4267-9b0f-4a176ce26651",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3w1KWiahjvBTsXyjEaDRR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 319,
      "cache_read_input_tokens": 54913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 319
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

_source line 66 · 2026-05-29T02:23:12.013Z_

<details><summary>↩ Tool result · reported error · `toolu_01SUYRGHB76p23ZhfL3pkdj9`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "d6e13f73-45e8-4bbe-a419-3bc72123fedb",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_01TfWWbpJUSSVgTPoTYDdwvP`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures && python3 fig_car_factorial_combined.py",
  "description": "Run combined figure script with python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "3d4bb34e-b1ae-4d05-a668-e53b41bfd5c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011NicZ2vfkjwidT978pt7EK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 55232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 154
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

_source line 68 · 2026-05-29T02:23:16.342Z_

<details><summary>↩ Tool result · `toolu_01TfWWbpJUSSVgTPoTYDdwvP`</summary>

```text
Saved: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig_car_factorial_combined.pdf
Saved: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig_car_factorial_combined.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "15ef3d9e-7d49-4679-b5b5-74d183d0132b",
  "tool_use_result": {
    "stdout": "Saved: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig_car_factorial_combined.pdf\nSaved: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig_car_factorial_combined.png",
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

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01PUurFDDuwUdRKGLdpXKv6Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig_car_factorial_combined.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "22515318-8fa7-4eba-b345-c9b1ef2a5b9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDewzyTcb5FGsSqhh85J2j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 55386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 223
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

_source line 70 · 2026-05-29T02:23:19.898Z_

<details><summary>↩ Tool result · `toolu_01PUurFDDuwUdRKGLdpXKv6Q`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
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
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "2ffcbecb-7938-4286-b979-0f5edaae6d2e",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 218190
    }
  }
}
```

</details>

---

### Assistant

_source line 71_

Figure looks good. Both panels render correctly:
- **(a)** CAR dot chart with correct data, error bars, BN/LN grouping, Vanilla baseline, and pp annotations
- **(b)** Factorial 2×2 interaction with both lines clearly differentiated, n-labels, Vanilla baseline, and delta annotations

Let me verify the final state of the modified LaTeX files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "c804d2b6-e62f-426a-8a57-6d7387243c85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeGbwxBGusiKW3JakjvND4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 55609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_017VpkvdcuoMfAtVZduEskmC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
  "offset": 60,
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "17506b38-df8a-4396-8b83-c71deda2b7bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeGbwxBGusiKW3JakjvND4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 55609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 73 · 2026-05-29T02:23:25.653Z_

<details><summary>↩ Tool result · `toolu_017VpkvdcuoMfAtVZduEskmC`</summary>

```text
60	\end{table}
61	
62	% Old Fig 2 (factorial standalone) — merged into fig:factorial_gradient below
63	% \begin{figure}[t]
64	% \centering
65	% \includegraphics[width=\columnwidth]{figures/factorial_2x2_pb.pdf}
66	% \caption{...}
67	% \label{fig:factorial_old}
68	% \end{figure}
69	
70	\begin{figure*}[t]
71	\centering
72	\includegraphics[width=\textwidth]{figures/fig_car_factorial_combined.pdf}
73	\caption{(a)~Only BN + gradient flow falls below Vanilla. Detach+LN achieves the highest CAR ($0.802{\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$). Under BatchNorm, gradient flow is associated with lower CAR; LayerNorm eliminates this vulnerability. Error bars: cross-seed SD. (b)~$2{\times}2$ factorial comparison: normalization type (BN/LN) $\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\,pp lower CAR ($g{=}0.78$); LN row: 2.9\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline.}
74	\label{fig:car_factorial}
75	\end{figure*}
76	
77	\subsection{Factorial Interpretation}
78	\label{sec:mechanism}
79	
80	\textbf{Gradient flow is associated with lower safety under BatchNorm but not under LayerNorm.} The BN row provides the clearest signal: Full OCC (BN) is the sole factorial cell falling below Vanilla ($\Delta{=}-2.0$\,pp, $g{=}-0.34$ vs.\ Vanilla), whereas Detach OCC recovers above it ($\Delta{=}+2.2$\,pp, $g{=}+0.74$, large). In the LN row, Full OCC+LN already exceeds Vanilla ($0.773$, $g{=}+0.90$, large), and Detach+LN yields the highest cell mean ($0.802$, $g{=}+1.89$, very large; bootstrap 95\% CI for $\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$). This is a practical threshold crossing---only BN + gradient flow is associated with reduced safety---rather than a statistical interaction (the factorial interaction is negligible, $\eta^2{=}0.005$). The numerical advantage of Detach OCC ($+$2.2\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.
81	
82	\textbf{Temporal dynamics.} Cutoff conditions illuminate when gradient flow's association with lower safety emerges. Cutoff@15K ($\Delta{=}+0.2$\,pp) performs near Vanilla, while Cutoff@25K shows a large deficit ($\Delta{=}-5.6$\,pp) and Cutoff@35K returns to baseline ($\Delta{=}-0.1$\,pp). Cutoff@45K ($\Delta{=}-1.6$\,pp, single seed) falls between these extremes. This non-monotonic pattern suggests that the critical window for gradient flow damage is not simply cumulative exposure but depends on the training phase. Reverse Cutoff (gradient flow only after step 35K) produces the worst supplementary result ($\Delta{=}-6.2$\,pp), indicating that late-stage gradient flow---when the model is refining action predictions---is associated with substantially worse outcomes than early exposure during initial representation learning. However, temporal conditions use 1--3 seeds under v1, so these observations are preliminary; targeted replication under v2 with more seeds would be needed to confirm the temporal pattern.
83	
84	\subsection{Gradient Dynamics}
85	
86	Gradient analysis (Figure~\ref{fig:gradient_analysis}) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).
87	
88	\begin{figure*}[t]
89	\centering
90	\includegraphics[width=\textwidth]{figures/gradient_analysis_v2_combined.pdf}
91	\caption{Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\approx}$46\% conflict rate), confirming orthogonality.}
92	\label{fig:gradient_analysis}
93	\end{figure*}
94	
95	\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\ref{fig:gradient_analysis}), with conflict rates of ${\approx}$46\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (Figure~\ref{fig:gradient_analysis}), ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)
96	
97	\textbf{Mechanism remains open.} The observed effect pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The observed effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. Centered Kernel Alignment (CKA) analysis~\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\geq$ 0.95 for both DINOv2 and SigLIP across all encoder layers), localizing the safety deficit to optimization dynamics rather than representational corruption. This high representational similarity is notable: even the worst-performing condition (Full OCC, BN) produces encoder features nearly identical to Vanilla, yet its action policy exhibits substantially worse collision avoidance. The dissociation between representational similarity and behavioral safety suggests that subtle differences in the LoRA adapter weights---invisible to CKA---drive the safety deficit.
98	
99	Additional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\ref{app:additional}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "a191be38-acb8-4bb9-b3e6-2be7d53bd5d8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex",
      "content": "\\end{table}\n\n% Old Fig 2 (factorial standalone) — merged into fig:factorial_gradient below\n% \\begin{figure}[t]\n% \\centering\n% \\includegraphics[width=\\columnwidth]{figures/factorial_2x2_pb.pdf}\n% \\caption{...}\n% \\label{fig:factorial_old}\n% \\end{figure}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig_car_factorial_combined.pdf}\n\\caption{(a)~Only BN + gradient flow falls below Vanilla. Detach+LN achieves the highest CAR ($0.802{\\pm}0.024$, $n{=}3$), reliably outperforming Vanilla ($0.745$; Hedges' $g{=}1.89$). Under BatchNorm, gradient flow is associated with lower CAR; LayerNorm eliminates this vulnerability. Error bars: cross-seed SD. (b)~$2{\\times}2$ factorial comparison: normalization type (BN/LN) $\\times$ gradient flow (ON/OFF). BN row: gradient flow is associated with 4.2\\,pp lower CAR ($g{=}0.78$); LN row: 2.9\\,pp ($g{=}0.94$). All LN cells exceed Vanilla baseline.}\n\\label{fig:car_factorial}\n\\end{figure*}\n\n\\subsection{Factorial Interpretation}\n\\label{sec:mechanism}\n\n\\textbf{Gradient flow is associated with lower safety under BatchNorm but not under LayerNorm.} The BN row provides the clearest signal: Full OCC (BN) is the sole factorial cell falling below Vanilla ($\\Delta{=}-2.0$\\,pp, $g{=}-0.34$ vs.\\ Vanilla), whereas Detach OCC recovers above it ($\\Delta{=}+2.2$\\,pp, $g{=}+0.74$, large). In the LN row, Full OCC+LN already exceeds Vanilla ($0.773$, $g{=}+0.90$, large), and Detach+LN yields the highest cell mean ($0.802$, $g{=}+1.89$, very large; bootstrap 95\\% CI for $\\Delta$: $[0.025, 0.089]$; Welch $t$ $p{=}0.045$). This is a practical threshold crossing---only BN + gradient flow is associated with reduced safety---rather than a statistical interaction (the factorial interaction is negligible, $\\eta^2{=}0.005$). The numerical advantage of Detach OCC ($+$2.2\\,pp, with 3 of 4 seeds exceeding the Vanilla mean) raises the possibility that detached auxiliary heads provide a mild regularization benefit, though larger samples are needed to confirm.\n\n\\textbf{Temporal dynamics.} Cutoff conditions illuminate when gradient flow's association with lower safety emerges. Cutoff@15K ($\\Delta{=}+0.2$\\,pp) performs near Vanilla, while Cutoff@25K shows a large deficit ($\\Delta{=}-5.6$\\,pp) and Cutoff@35K returns to baseline ($\\Delta{=}-0.1$\\,pp). Cutoff@45K ($\\Delta{=}-1.6$\\,pp, single seed) falls between these extremes. This non-monotonic pattern suggests that the critical window for gradient flow damage is not simply cumulative exposure but depends on the training phase. Reverse Cutoff (gradient flow only after step 35K) produces the worst supplementary result ($\\Delta{=}-6.2$\\,pp), indicating that late-stage gradient flow---when the model is refining action predictions---is associated with substantially worse outcomes than early exposure during initial representation learning. However, temporal conditions use 1--3 seeds under v1, so these observations are preliminary; targeted replication under v2 with more seeds would be needed to confirm the temporal pattern.\n\n\\subsection{Gradient Dynamics}\n\nGradient analysis (Figure~\\ref{fig:gradient_analysis}) examines the mechanism through which auxiliary heads affect safety. All gradient norms are computed with respect to the L1 action loss (action tokens only).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/gradient_analysis_v2_combined.pdf}\n\\caption{Gradient dynamics (v2, seed 42, 200 batches at 50K). Action gradient norms are comparable across conditions, ruling out amplification. Action--auxiliary cosine similarity is near zero (${\\approx}$46\\% conflict rate), confirming orthogonality.}\n\\label{fig:gradient_analysis}\n\\end{figure*}\n\n\\textbf{Gradient orthogonality rules out direct conflict.} Action--auxiliary gradient cosine similarity is near zero across all encoder layers for both Full OCC and Random OCC (Figure~\\ref{fig:gradient_analysis}), with conflict rates of ${\\approx}$46\\%. Action loss gradient norms are comparable across Vanilla and gradient-flow conditions (Figure~\\ref{fig:gradient_analysis}), ruling out gradient amplification. Both patterns are identical for structured and random labels, consistent with the behavioral finding that spatial content did not detectably affect outcomes. (Random OCC gradient data were obtained under the v1 codebase; the v2 gradient analysis covers all four factorial conditions and Vanilla, each using a v2-trained checkpoint.)\n\n\\textbf{Mechanism remains open.} The observed effect pattern cannot be explained by gradient conflict (orthogonality rules it out) or gradient amplification (norms are comparable). The observed effect likely operates through indirect modification of the LoRA optimization trajectory under a dual-objective loss landscape. Centered Kernel Alignment (CKA) analysis~\\cite{kornblith2019similarity} confirms that encoder representations remain intact under all conditions (CKA $\\geq$ 0.95 for both DINOv2 and SigLIP across all encoder layers), localizing the safety deficit to optimization dynamics rather than representational corruption. This high representational similarity is notable: even the worst-performing condition (Full OCC, BN) produces encoder features nearly identical to Vanilla, yet its action policy exhibits substantially worse collision avoidance. The dissociation between representational similarity and behavioral safety suggests that subtle differences in the LoRA adapter weights---invisible to CKA---drive the safety deficit.\n\nAdditional observations (per-task breakdown, depth comparison, and temporal dynamics) are in Appendix~\\ref{app:additional}.",
      "numLines": 40,
      "startLine": 60,
      "totalLines": 100
    }
  }
}
```

</details>

---

### Assistant

_source line 74_

All correct. Let me do a final sweep to confirm zero stale `\ref` occurrences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "ab2253e6-3547-482f-a5a0-3d2145e77a21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMaW1Qn4MXBo6DZkizXAMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1877,
      "cache_read_input_tokens": 55881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1877
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

_source line 75_

<details open><summary>🔧 Tool call — Grep · `toolu_01WYugs5JggdLZxqeHgBtrUB`</summary>

```json
{
  "pattern": "\\\\ref\\{fig:factorial_gradient\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "glob": "*.tex",
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
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "c484afb3-a3bc-429a-b266-cef2a1913b98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMaW1Qn4MXBo6DZkizXAMH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1877,
      "cache_read_input_tokens": 55881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1877
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

_source line 76 · 2026-05-29T02:23:29.924Z_

<details><summary>↩ Tool result · `toolu_01WYugs5JggdLZxqeHgBtrUB`</summary>

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
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "d6763fef-9bd0-420c-9b25-eb9453ae2ccc",
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

_source line 77_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Jw269Cazz78DstX2iRcLwv`</summary>

```json
{
  "todos": [
    {
      "content": "Create fig_car_factorial_combined.py script",
      "status": "completed",
      "activeForm": "Creating combined figure script"
    },
    {
      "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
      "status": "completed",
      "activeForm": "Updating LaTeX files"
    },
    {
      "content": "Update all \\ref{} cross-references across paper",
      "status": "completed",
      "activeForm": "Updating cross-references"
    },
    {
      "content": "Run script and visually verify output",
      "status": "completed",
      "activeForm": "Running script and verifying output"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "eba4fea8-1afa-42dc-9112-665816de3550",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNQqTcQdFCotemZJbvwd4Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 57758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 182
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

_source line 78 · 2026-05-29T02:23:33.178Z_

<details><summary>↩ Tool result · `toolu_01Jw269Cazz78DstX2iRcLwv`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "0868710a-513d-45f8-a41b-b51fd9bbe31a",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Create fig_car_factorial_combined.py script",
        "status": "completed",
        "activeForm": "Creating combined figure script"
      },
      {
        "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
        "status": "completed",
        "activeForm": "Updating LaTeX files"
      },
      {
        "content": "Update all \\ref{} cross-references across paper",
        "status": "completed",
        "activeForm": "Updating cross-references"
      },
      {
        "content": "Run script and visually verify output",
        "status": "in_progress",
        "activeForm": "Running script and verifying output"
      }
    ],
    "newTodos": [
      {
        "content": "Create fig_car_factorial_combined.py script",
        "status": "completed",
        "activeForm": "Creating combined figure script"
      },
      {
        "content": "Update LaTeX: delete old figures, add new combined figure, restore gradient standalone",
        "status": "completed",
        "activeForm": "Updating LaTeX files"
      },
      {
        "content": "Update all \\ref{} cross-references across paper",
        "status": "completed",
        "activeForm": "Updating cross-references"
      },
      {
        "content": "Run script and visually verify output",
        "status": "completed",
        "activeForm": "Running script and verifying output"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 79_

完成。总结：

**脚本**：`fig_car_factorial_combined.py` — (a) CAR 水平点图 + (b) 2×2 factorial 交互图，figsize=(7.0, 3.0)，颜色统一，字号 ≥ 7pt。输出 PDF + PNG。

**LaTeX 修改**：
- `introduction.tex`：删除 `fig:results_bar` 独立 figure；`\ref{fig:factorial_gradient}a` → `\ref{fig:car_factorial}b`
- `results.tex`：旧 `fig:factorial_gradient` figure* → 新 `fig:car_factorial` figure*（使用新合并图）；取消注释恢复 gradient 为独立 `fig:gradient_analysis` figure*；所有 `\ref{fig:factorial_gradient}b` → `\ref{fig:gradient_analysis}`
- `discussion.tex`：2 处 `\ref{fig:factorial_gradient}b` → `\ref{fig:gradient_analysis}`
- `appendix.tex`：2 处引用同步更新

零残留旧 label 引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "uuid": "8d461df3-afbb-4dad-8dad-7bd98312105a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01As2m4rRykJDYCiJ37CeG3k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 232,
      "cache_read_input_tokens": 57940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 232
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

_source line 80_

完成。总结：

**脚本**：`fig_car_factorial_combined.py` — (a) CAR 水平点图 + (b) 2×2 factorial 交互图，figsize=(7.0, 3.0)，颜色统一，字号 ≥ 7pt。输出 PDF + PNG。

**LaTeX 修改**：
- `introduction.tex`：删除 `fig:results_bar` 独立 figure；`\ref{fig:factorial_gradient}a` → `\ref{fig:car_factorial}b`
- `results.tex`：旧 `fig:factorial_gradient` figure* → 新 `fig:car_factorial` figure*（使用新合并图）；取消注释恢复 gradient 为独立 `fig:gradient_analysis` figure*；所有 `\ref{fig:factorial_gradient}b` → `\ref{fig:gradient_analysis}`
- `discussion.tex`：2 处 `\ref{fig:factorial_gradient}b` → `\ref{fig:gradient_analysis}`
- `appendix.tex`：2 处引用同步更新

零残留旧 label 引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 192731,
  "duration_api_ms": 192105,
  "num_turns": 31,
  "stop_reason": "end_turn",
  "session_id": "e2b9b413-9051-45c9-baef-6e26f3819f16",
  "total_cost_usd": 1.02957825,
  "usage": {
    "input_tokens": 23,
    "cache_creation_input_tokens": 46327,
    "cache_read_input_tokens": 910351,
    "output_tokens": 11280,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 46327,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 306,
        "cache_read_input_tokens": 57940,
        "cache_creation_input_tokens": 232,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 232
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2654,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002744,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 23,
      "outputTokens": 11280,
      "cacheReadInputTokens": 910351,
      "cacheCreationInputTokens": 46327,
      "webSearchRequests": 0,
      "costUSD": 1.02683425,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "dafc976d-5c71-4779-8078-6bf8c2df983a"
}
```

</details>

---
