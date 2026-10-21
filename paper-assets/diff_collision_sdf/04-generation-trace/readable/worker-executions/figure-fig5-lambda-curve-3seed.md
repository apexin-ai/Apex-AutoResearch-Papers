# figure fig5 lambda curve 3seed

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_figure_fig5-lambda-curve-3seed_20260528T030223.log`
- **Structured JSON:** [`6700bcca6c34606e514c.json`](../../sessions/67/6700bcca6c34606e514c.json)

## Before a recorded user message

53 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "3dc5d9c5-de83-45b0-92f2-2ea445518d4a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1779948600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8cb41428-610f-4cd3-b1b4-6d30246572ee",
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current plot script and CSV file, and querying the registry for the needed data points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "70f1a2b2-44ef-4c8c-8807-e1c30a15f51d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExcFkfhj7C8Ev6jf2WCLMM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12637,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12637
      },
      "output_tokens": 19,
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

I'll read the current files and query the registry in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "0bc4a45d-7c15-484e-9efc-8c95d4e7beef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExcFkfhj7C8Ev6jf2WCLMM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12637,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12637
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — Read · `toolu_016aGikhyKNXuJ2xPcCWCShF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "ec2e8ffa-6a8d-4e2e-b759-0d0576fe6af5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExcFkfhj7C8Ev6jf2WCLMM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12637,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12637
      },
      "output_tokens": 19,
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

_source line 7 · 2026-05-28T03:02:37.348Z_

<details><summary>↩ Tool result · `toolu_016aGikhyKNXuJ2xPcCWCShF`</summary>

```text
1	#!/usr/bin/env python3
2	"""Fig 5 v4 (final): lambda-CAR/TSR curve with null distribution band.
3	
4	narrative_intent: "SDF geometric supervision is redundant across a 20x
5	loss weight range: all lambda values produce CAR within the null distribution band."
6	
7	Patterns: A (null band), D (hollow marker for preliminary), J (path-effect).
8	"""
9	
10	import matplotlib
11	matplotlib.use('Agg')
12	import matplotlib.pyplot as plt
13	import matplotlib.patheffects as pe
14	from matplotlib.lines import Line2D
15	import numpy as np
16	from pathlib import Path
17	
18	OUT = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/'
19	           'diff_collision_sdf/artifacts/figures/fig5_lambda_curve')
20	
21	plt.rcParams.update({
22	    'font.family': 'DejaVu Sans',
23	    'font.size': 11,
24	    'axes.titlesize': 13,
25	    'axes.labelsize': 11,
26	    'xtick.labelsize': 9.5,
27	    'ytick.labelsize': 9.5,
28	    'legend.fontsize': 10,
29	    'figure.dpi': 300,
30	    'savefig.dpi': 300,
31	    'savefig.bbox': 'tight',
32	    'savefig.pad_inches': 0.05,
33	    'axes.spines.top': False,
34	    'axes.spines.right': False,
35	    'pdf.fonttype': 42,
36	    'ps.fonttype': 42,
37	    'lines.linewidth': 1.5,
38	})
39	
40	C_CAR = '#0072B2'
41	C_TSR = '#D55E00'
42	C_NULL = '#CCCCCC'
43	STROKE = [pe.withStroke(linewidth=2.0, foreground='white')]
44	
45	car_mean = np.array([54.75, 54.5, 56.33, 58.25])
46	car_std  = np.array([3.18, 2.29, 1.61, 0.35])
47	seeds    = np.array([2, 3, 3, 2])
48	tsr_mean = np.array([51.5, 54.0, 53.83, 48.0])
49	car_se   = car_std / np.sqrt(seeds)
50	
51	null_mu, null_sig = 54.6, 2.27
52	
53	xpos = np.array([0, 1.8, 2.8, 3.8])
54	xlbl = ['0\n(LoRA-only)', '0.005', '0.01', '0.1']
55	
56	fig, ax = plt.subplots(figsize=(3.25, 2.5))
57	
58	# Null distribution band
59	ax.axhspan(null_mu - null_sig, null_mu + null_sig,
60	           color=C_NULL, alpha=0.3, zorder=0)
61	ax.axhline(null_mu, color='#BBBBBB', ls='--', lw=0.6, zorder=1)
62	
63	# CAR: lambda=0 isolated, lambda>0 connected
64	ax.errorbar(xpos[0], car_mean[0], yerr=car_se[0],
65	            fmt='o', color=C_CAR, ms=5.5,
66	            capsize=3, capthick=0.8, elinewidth=0.8,
67	            mec='white', mew=0.6, zorder=4)
68	ax.errorbar(xpos[1:], car_mean[1:], yerr=car_se[1:],
69	            fmt='o-', color=C_CAR, ms=5.5, lw=1.5,
70	            capsize=3, capthick=0.8, elinewidth=0.8,
71	            mec='white', mew=0.6, zorder=4)
72	
73	# TSR: lighter weight
74	ax.plot(xpos[0], tsr_mean[0], 's', color=C_TSR, ms=4.5,
75	        mec='white', mew=0.6, alpha=0.75, zorder=3)
76	ax.plot(xpos[1:], tsr_mean[1:], 's--', color=C_TSR, ms=4.5,
77	        mec='white', mew=0.6, alpha=0.75, lw=1.2, zorder=3)
78	
79	# Seed annotations
80	ann_cfg = [
81	    (10, 0, 'left'),
82	    (0, 5, 'center'),
83	    (0, 5, 'center'),
84	    (0, 5, 'center'),
85	]
86	for i in range(4):
87	    ox, oy, ha = ann_cfg[i]
88	    ref_y = car_mean[i] + car_se[i] if oy >= 0 else car_mean[i]
89	    t = ax.annotate(f'n={seeds[i]}',
90	                    xy=(xpos[i], ref_y),
91	                    xytext=(ox, oy), textcoords='offset points',
92	                    fontsize=5.5, color=C_CAR, ha=ha, style='italic')
93	    t.set_path_effects(STROKE)
94	
95	# 20K preliminary
96	t20 = ax.annotate('30K†', xy=(xpos[3], tsr_mean[3]),
97	                  xytext=(7, -2), textcoords='offset points',
98	                  fontsize=5.5, color='#888', style='italic', ha='left')
99	t20.set_path_effects(STROKE)
100	
101	# Null-band label
102	t = ax.text(4.2, null_mu, 'null\n$\\pm$1$\\sigma$',
103	            fontsize=5.5, color='#999', ha='center', va='center',
104	            style='italic', linespacing=0.85)
105	t.set_path_effects(STROKE)
106	
107	# Axis break marks
108	trans = ax.get_xaxis_transform()
109	for bx in [0.7, 0.9]:
110	    ax.plot([bx, bx + 0.12], [-0.04, 0.04], transform=trans,
111	            color='k', lw=0.5, clip_on=False)
112	
113	ax.set_xticks(xpos)
114	ax.set_xticklabels(xlbl, fontsize=8)
115	ax.set_xlabel(r'$\lambda$ (SDF loss weight)', fontsize=10)
116	ax.set_ylabel('Rate (%)', fontsize=10)
117	ax.set_xlim(-0.6, 4.6)
118	ax.set_ylim(46, 60)
119	
120	# Legend
121	handles = [
122	    Line2D([0], [0], marker='o', color=C_CAR, mfc=C_CAR,
123	           mec='white', ms=4.5, lw=1.4, ls='-', label='CAR'),
124	    Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,
125	           mec='white', ms=4, lw=1.1, ls='--', label='TSR'),
126	    Line2D([0], [0], marker='o', color='#888', mfc='white',
127	           mec='#888', ms=4.5, lw=0, label='2 of 3 seeds†'),
128	]
129	ax.legend(handles=handles, loc='upper left', fontsize=6.5,
130	          framealpha=0.92, edgecolor='none', handlelength=1.6,
131	          handletextpad=0.5, borderpad=0.35, labelspacing=0.25)
132	
133	plt.tight_layout()
134	OUT.parent.mkdir(parents=True, exist_ok=True)
135	fig.savefig(OUT.with_suffix('.pdf'))
136	fig.savefig(OUT.with_suffix('.png'))
137	plt.close(fig)
138	print(f'Saved: {OUT.with_suffix(".pdf")} and {OUT.with_suffix(".png")}')
139	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "71d166c6-2c27-464a-8094-7cc0b86b4d04",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Fig 5 v4 (final): lambda-CAR/TSR curve with null distribution band.\n\nnarrative_intent: \"SDF geometric supervision is redundant across a 20x\nloss weight range: all lambda values produce CAR within the null distribution band.\"\n\nPatterns: A (null band), D (hollow marker for preliminary), J (path-effect).\n\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.lines import Line2D\nimport numpy as np\nfrom pathlib import Path\n\nOUT = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/'\n           'diff_collision_sdf/artifacts/figures/fig5_lambda_curve')\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 11,\n    'xtick.labelsize': 9.5,\n    'ytick.labelsize': 9.5,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'lines.linewidth': 1.5,\n})\n\nC_CAR = '#0072B2'\nC_TSR = '#D55E00'\nC_NULL = '#CCCCCC'\nSTROKE = [pe.withStroke(linewidth=2.0, foreground='white')]\n\ncar_mean = np.array([54.75, 54.5, 56.33, 58.25])\ncar_std  = np.array([3.18, 2.29, 1.61, 0.35])\nseeds    = np.array([2, 3, 3, 2])\ntsr_mean = np.array([51.5, 54.0, 53.83, 48.0])\ncar_se   = car_std / np.sqrt(seeds)\n\nnull_mu, null_sig = 54.6, 2.27\n\nxpos = np.array([0, 1.8, 2.8, 3.8])\nxlbl = ['0\\n(LoRA-only)', '0.005', '0.01', '0.1']\n\nfig, ax = plt.subplots(figsize=(3.25, 2.5))\n\n# Null distribution band\nax.axhspan(null_mu - null_sig, null_mu + null_sig,\n           color=C_NULL, alpha=0.3, zorder=0)\nax.axhline(null_mu, color='#BBBBBB', ls='--', lw=0.6, zorder=1)\n\n# CAR: lambda=0 isolated, lambda>0 connected\nax.errorbar(xpos[0], car_mean[0], yerr=car_se[0],\n            fmt='o', color=C_CAR, ms=5.5,\n            capsize=3, capthick=0.8, elinewidth=0.8,\n            mec='white', mew=0.6, zorder=4)\nax.errorbar(xpos[1:], car_mean[1:], yerr=car_se[1:],\n            fmt='o-', color=C_CAR, ms=5.5, lw=1.5,\n            capsize=3, capthick=0.8, elinewidth=0.8,\n            mec='white', mew=0.6, zorder=4)\n\n# TSR: lighter weight\nax.plot(xpos[0], tsr_mean[0], 's', color=C_TSR, ms=4.5,\n        mec='white', mew=0.6, alpha=0.75, zorder=3)\nax.plot(xpos[1:], tsr_mean[1:], 's--', color=C_TSR, ms=4.5,\n        mec='white', mew=0.6, alpha=0.75, lw=1.2, zorder=3)\n\n# Seed annotations\nann_cfg = [\n    (10, 0, 'left'),\n    (0, 5, 'center'),\n    (0, 5, 'center'),\n    (0, 5, 'center'),\n]\nfor i in range(4):\n    ox, oy, ha = ann_cfg[i]\n    ref_y = car_mean[i] + car_se[i] if oy >= 0 else car_mean[i]\n    t = ax.annotate(f'n={seeds[i]}',\n                    xy=(xpos[i], ref_y),\n                    xytext=(ox, oy), textcoords='offset points',\n                    fontsize=5.5, color=C_CAR, ha=ha, style='italic')\n    t.set_path_effects(STROKE)\n\n# 20K preliminary\nt20 = ax.annotate('30K†', xy=(xpos[3], tsr_mean[3]),\n                  xytext=(7, -2), textcoords='offset points',\n                  fontsize=5.5, color='#888', style='italic', ha='left')\nt20.set_path_effects(STROKE)\n\n# Null-band label\nt = ax.text(4.2, null_mu, 'null\\n$\\\\pm$1$\\\\sigma$',\n            fontsize=5.5, color='#999', ha='center', va='center',\n            style='italic', linespacing=0.85)\nt.set_path_effects(STROKE)\n\n# Axis break marks\ntrans = ax.get_xaxis_transform()\nfor bx in [0.7, 0.9]:\n    ax.plot([bx, bx + 0.12], [-0.04, 0.04], transform=trans,\n            color='k', lw=0.5, clip_on=False)\n\nax.set_xticks(xpos)\nax.set_xticklabels(xlbl, fontsize=8)\nax.set_xlabel(r'$\\lambda$ (SDF loss weight)', fontsize=10)\nax.set_ylabel('Rate (%)', fontsize=10)\nax.set_xlim(-0.6, 4.6)\nax.set_ylim(46, 60)\n\n# Legend\nhandles = [\n    Line2D([0], [0], marker='o', color=C_CAR, mfc=C_CAR,\n           mec='white', ms=4.5, lw=1.4, ls='-', label='CAR'),\n    Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,\n           mec='white', ms=4, lw=1.1, ls='--', label='TSR'),\n    Line2D([0], [0], marker='o', color='#888', mfc='white',\n           mec='#888', ms=4.5, lw=0, label='2 of 3 seeds†'),\n]\nax.legend(handles=handles, loc='upper left', fontsize=6.5,\n          framealpha=0.92, edgecolor='none', handlelength=1.6,\n          handletextpad=0.5, borderpad=0.35, labelspacing=0.25)\n\nplt.tight_layout()\nOUT.parent.mkdir(parents=True, exist_ok=True)\nfig.savefig(OUT.with_suffix('.pdf'))\nfig.savefig(OUT.with_suffix('.png'))\nplt.close(fig)\nprint(f'Saved: {OUT.with_suffix(\".pdf\")} and {OUT.with_suffix(\".png\")}')\n",
      "numLines": 139,
      "startLine": 1,
      "totalLines": 139
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Dt8b8suwAEe79Py7cZL9AT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig5_lambda_data.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "c0a8ce7e-c9c3-40ab-a5f1-da87fbb22a58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExcFkfhj7C8Ev6jf2WCLMM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12637,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12637
      },
      "output_tokens": 19,
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

_source line 9 · 2026-05-28T03:02:38.282Z_

<details><summary>↩ Tool result · `toolu_01Dt8b8suwAEe79Py7cZL9AT`</summary>

```text
1	lambda,CAR_mean,CAR_std,CAR_seeds,TSR_mean,TSR_std,step,note
2	0,54.75,3.18,"57.0;52.5",48.75,,30K,LoRA-only (no SDF)
3	0.005,54.5,2.29,"57.0;54.0;52.5",54.0,3.0,30K,3 seeds
4	0.01,56.33,1.61,"57.0;57.5;54.5",53.83,1.5,30K,3 seeds
5	0.1,58.25,0.35,"58.0;58.5",48.0,1.4,30K,2 seeds 30K
6	
7	# step-wise sub-table (for inset or supplementary)
8	# lambda,step,CAR,TSR,seed,note
9	# 0.1,16000,pending,pending,0,best loss checkpoint eval running
10	# 0.1,20000,55,54,0,early signal
11	# 0.1,20000,56,51,1,early signal
12	# 0.1,22000,pending,pending,0,next after 16K
13	# 0.1,30000,pending,pending,0,training ~17:00 UTC
14	# 0.1,30000,pending,pending,1,training ~17:30 UTC
15	# 0.1,30000,pending,pending,2,training ~08:00 UTC 5/28
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "056f390b-fdcf-4c8f-9ac7-2aacdc3fb119",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig5_lambda_data.csv",
      "content": "lambda,CAR_mean,CAR_std,CAR_seeds,TSR_mean,TSR_std,step,note\n0,54.75,3.18,\"57.0;52.5\",48.75,,30K,LoRA-only (no SDF)\n0.005,54.5,2.29,\"57.0;54.0;52.5\",54.0,3.0,30K,3 seeds\n0.01,56.33,1.61,\"57.0;57.5;54.5\",53.83,1.5,30K,3 seeds\n0.1,58.25,0.35,\"58.0;58.5\",48.0,1.4,30K,2 seeds 30K\n\n# step-wise sub-table (for inset or supplementary)\n# lambda,step,CAR,TSR,seed,note\n# 0.1,16000,pending,pending,0,best loss checkpoint eval running\n# 0.1,20000,55,54,0,early signal\n# 0.1,20000,56,51,1,early signal\n# 0.1,22000,pending,pending,0,next after 16K\n# 0.1,30000,pending,pending,0,training ~17:00 UTC\n# 0.1,30000,pending,pending,1,training ~17:30 UTC\n# 0.1,30000,pending,pending,2,training ~08:00 UTC 5/28\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013coLt71i3NbMH3SaBeSmDS`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "bce2caf6-8055-4c52-b8de-3979869897b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExcFkfhj7C8Ev6jf2WCLMM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12637,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12637
      },
      "output_tokens": 19,
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

_source line 11 · 2026-05-28T03:02:38.743Z_

<details><summary>↩ Tool result · `toolu_013coLt71i3NbMH3SaBeSmDS`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "8e6064fb-20cc-45d3-a9b4-d37be17ab5a3",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
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
Let me query the registry for the λ=0.1 eval results and LoRA results to confirm the data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "317969f2-b182-491e-a2a7-043b94cfe06b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147D64BsHgfm8QMqiTqU5q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3404,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3404
      },
      "output_tokens": 23,
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

Querying registry for λ=0.1 and LoRA eval data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "ba72a6a4-46a8-4934-8676-e0a380dc3cda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147D64BsHgfm8QMqiTqU5q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3404,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3404
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_013weh1AfXNSKojaHKKzkMp1`</summary>

```json
{
  "project": "diff_collision_sdf",
  "filters": {
    "name": "eval_pi05_a1_30k_s0_l01_high"
  },
  "fields": [
    "*"
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
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "0ad4382b-48b1-4559-b1b2-817fa1b92a8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147D64BsHgfm8QMqiTqU5q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3404,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3404
      },
      "output_tokens": 23,
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

_source line 15 · 2026-05-28T03:02:46.361Z_

<details><summary>↩ Tool result · `toolu_013weh1AfXNSKojaHKKzkMp1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3694}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "bf2955dc-e8d9-4cf0-b6c8-cce8d5521858",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3694}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3694}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01KcgxwnNaBPh2wvtMoa1Tmd`</summary>

```json
{
  "project": "diff_collision_sdf",
  "filters": {
    "name": "eval_pi05_a1_30k_s1_l01_high"
  },
  "fields": [
    "*"
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
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "399840b6-cdb5-4611-bc79-191ee3f4e8b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147D64BsHgfm8QMqiTqU5q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3404,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3404
      },
      "output_tokens": 23,
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

_source line 17 · 2026-05-28T03:02:47.127Z_

<details><summary>↩ Tool result · `toolu_01KcgxwnNaBPh2wvtMoa1Tmd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3105}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "31e67228-e77a-47dc-90d0-42b6ff444e25",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3105}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3105}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_014iBXYxAdDxXUFqTvbLhdtj`</summary>

```json
{
  "project": "diff_collision_sdf",
  "filters": {
    "name": "eval_pi05_a1_30k_s2_l01_high"
  },
  "fields": [
    "*"
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
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "8baf2199-9ee8-473f-bff1-ab3a4985869e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147D64BsHgfm8QMqiTqU5q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3404,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3404
      },
      "output_tokens": 23,
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

_source line 19 · 2026-05-28T03:02:47.757Z_

<details><summary>↩ Tool result · `toolu_014iBXYxAdDxXUFqTvbLhdtj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3343}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "9f38eed0-0faf-422e-b953-2fee32bbf9b5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3343}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3343}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_015ZAE9ZJSTiuCEfB1A5ceyK`</summary>

```json
{
  "project": "diff_collision_sdf",
  "filters": {
    "name": "eval_pi05_a1_30k_s0_lora_high"
  },
  "fields": [
    "*"
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
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "2d30c4b8-afda-4fed-bda6-bca6e2c2da93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147D64BsHgfm8QMqiTqU5q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3404,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3404
      },
      "output_tokens": 23,
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

_source line 21 · 2026-05-28T03:02:48.727Z_

<details><summary>↩ Tool result · `toolu_015ZAE9ZJSTiuCEfB1A5ceyK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3148}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "3aef36b5-e175-4793-9dd0-69c437d90c91",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3148}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3148}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_011X3v2QkwAtgmF4U8xaEDyf`</summary>

```json
{
  "project": "diff_collision_sdf",
  "filters": {
    "name": "eval_pi05_a1_30k_s1_lora_high"
  },
  "fields": [
    "*"
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
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "d795bdd7-f5ae-4ca5-8b53-80d88d8fdf80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147D64BsHgfm8QMqiTqU5q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3404,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3404
      },
      "output_tokens": 23,
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

_source line 23 · 2026-05-28T03:02:49.556Z_

<details><summary>↩ Tool result · `toolu_011X3v2QkwAtgmF4U8xaEDyf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3136}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "e73aa435-0e1d-4f99-acc4-eae99c5b01c2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3136}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3136}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01U4eky2TcJMALFvCsRErAK3`</summary>

```json
{
  "project": "diff_collision_sdf",
  "filters": {
    "name": "eval_pi05_a1_30k_s2_lora_high"
  },
  "fields": [
    "*"
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
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "e0f76243-9d93-4aba-9191-9967da7c6d2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147D64BsHgfm8QMqiTqU5q5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3404,
      "cache_read_input_tokens": 24088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3404
      },
      "output_tokens": 23,
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

_source line 25 · 2026-05-28T03:02:49.982Z_

<details><summary>↩ Tool result · `toolu_01U4eky2TcJMALFvCsRErAK3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3527}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "2e190f4f-b859-4e05-9cae-6fa3df42a29e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.3527}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3527}}"
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
The exact names didn't match. Let me search more broadly for the eval entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "77abd4b9-8e27-488c-ab60-1ae35abe3196",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhXRuXPcw9vZc8TCZFKymN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 27492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1438
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

Exact names didn't match. Let me search the registry more broadly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "0a08a1d8-27c6-4839-9473-7b7b961366e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhXRuXPcw9vZc8TCZFKymN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 27492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1438
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01KShuAp259wqtRismQws4sW`</summary>

```json
{
  "project": "diff_collision_sdf",
  "limit": 0,
  "fields": [
    "name",
    "status",
    "metrics",
    "conclusion"
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
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "85f5dcd0-9ff4-444a-b4f6-391059fc8d97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhXRuXPcw9vZc8TCZFKymN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 27492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1438
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

_source line 29 · 2026-05-28T03:03:01.278Z_

<details><summary>↩ Tool result · `toolu_01KShuAp259wqtRismQws4sW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_multiseed_sdf_l01_s0_eseed256\": {\"status\": \"PREPARING\"}, \"eval_multiseed_sdf_l01_s0_eseed123\": {\"status\": \"PREPARING\"}, \"eval_multiseed_sdf_l01_s0_eseed42\": {\"status\": \"PREPARING\"}, \"eval_multiseed_lora_s0_eseed123\": {\"status\": \"PREPARING\"}, \"eval_multiseed_lora_s0_eseed42\": {\"status\": \"PREPARING\"}, \"eval_pi05_a1_30k_s2_l01_high\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"car\": 54.5, \"tsr\": 54.5, \"per_task_car\": {\"orange_juice\": 56, \"chocolate_pudding\": 76, \"milk\": 70, \"bbq_sauce\": 16}, \"per_task_tsr\": {\"orange_juice\": 30, \"chocolate_pudding\": 72, \"milk\": 48, \"bbq_sauce\": 68}, \"scenario\": \"B\"}}, \"train_pi05_a1_obj_s2_l01_high\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.0104, \"final_action_loss\": 0.0069, \"final_sdf_loss\": 0.0336, \"final_ee_loss\": 0.0096, \"best_loss\": 0.0104, \"best_step\": 30000, \"total_steps\": 30000, \"training_hours\": 33.86}}, \"eval_spatial_bowl_lora_ctrl_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 0.5, \"avg_CAR\": 0.155, \"task0_TSR\": 0.66, \"task0_CAR\": 0, \"task1_TSR\": 0.36, \"task1_CAR\": 0.14, \"task2_TSR\": 0.6, \"task2_CAR\": 0.04, \"task3_TSR\": 0.38, \"task3_CAR\": 0.44}}, \"eval_pi05_a1_best_s0_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 0.52, \"avg_CAR\": 0.545, \"task0_TSR\": 0.28, \"task0_CAR\": 0.5, \"task1_TSR\": 0.7, \"task1_CAR\": 0.74, \"task2_TSR\": 0.52, \"task2_CAR\": 0.68, \"task3_TSR\": 0.58, \"task3_CAR\": 0.26, \"n_episodes\": 50, \"seed\": 7, \"collision_threshold\": 0.001}}, \"train_phase2_lambda0_extra_seed\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_spatial_bowl_lora_control_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_lora_s2_30k_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_TSR\": 0.515, \"overall_CAR\": 0.55, \"task0_orange_juice\": {\"TSR\": 0.24, \"CAR\": 0.56}, \"task1_chocolate_pudding\": {\"TSR\": 0.76, \"CAR\": 0.76}, \"task2_milk\": {\"TSR\": 0.42, \"CAR\": 0.62}, \"task3_bbq_sauce\": {\"TSR\": 0.64, \"CAR\": 0.26}}, \"conclusion\": \"success\"}, \"train_phase2_lambda0_s2_v4\": {\"status\": \"RUNNING\"}, \"train_phase2_lambda0_extra_seed_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_phase2_lambda0_s2_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_phase2_lambda0_extra_seed_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_lora_baseline_30k_s2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_spatial_bowl_sdf_s0_l005_30k\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 0.53, \"avg_CAR\": 0.17, \"task0_TSR\": 0.62, \"task0_CAR\": 0, \"task1_TSR\": 0.34, \"task1_CAR\": 0.14, \"task2_TSR\": 0.66, \"task2_CAR\": 0, \"task3_TSR\": 0.5, \"task3_CAR\": 0.54}}, \"train_pi05_lora_baseline_s2_resume\": {\"status\": \"DONE\", \"metrics\": {\"final_loss\": 0.0117, \"final_lr\": 2.5e-06, \"total_steps\": 30000, \"training_time_h\": 10.31}, \"conclusion\": \"success\"}, \"train_phase2_lambda0_s2_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_a1_30k_s1_l01_high\": {\"status\": \"DONE\", \"metrics\": {\"CAR\": 0.585, \"TSR\": 0.49, \"frozen_rate\": 0, \"dfCAR\": 0.585, \"avg_max_ee_displacement\": 0.3884, \"avg_max_obstacle_displacement\": 0.0553, \"per_task\": {\"orange_juice\": {\"TSR\": 0.26, \"CAR\": 0.66, \"avg_max_ee_displacement\": 0.3882, \"avg_max_obstacle_displacement\": 0.0333}, \"chocolate_pudding\": {\"TSR\": 0.8, \"CAR\": 0.72, \"avg_max_ee_displacement\": 0.4057, \"avg_max_obstacle_displacement\": 0.0545}, \"milk\": {\"TSR\": 0.28, \"CAR\": 0.7, \"avg_max_ee_displacement\": 0.3551, \"avg_max_obstacle_displacement\": 0.0408}, \"bbq_sauce\": {\"TSR\": 0.62, \"CAR\": 0.26, \"avg_max_ee_displacement\": 0.4045, \"avg_max_obstacle_displacement\": 0.0927}}}, \"conclusion\": \"success\"}, \"reeval_lora_s0_30k_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"CAR\": 57, \"TSR\": 46, \"per_task\": {\"orange_juice\": 68, \"chocolate_pudding\": 74, \"milk\": 66, \"bbq_sauce\": 20}}}, \"eval_pi05_a1_30k_s0_l01_high\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"CAR\": 58, \"TSR\": 47, \"frozen_rate\": 0, \"avg_max_ee_displacement\": 0.4, \"dfCAR\": 58}}, \"train_pi05_a1_obj_s1_l01_high\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_pi05_a1_obj_s0_l01_high\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_stepwise_s0_l1_28k\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 48.5, \"avg_CAR\": 54.5, \"task0_orange_juice\": {\"TSR\": 28, \"CAR\": 50, \"avg_max_disp\": 0.0618}, \"task1_chocolate_pudding\": {\"TSR\": 68, \"CAR\": 74, \"avg_max_disp\": 0.0463}, \"task2_milk\": {\"TSR\": 44, \"CAR\": 72, \"avg_max_disp\": 0.0277}, \"task3_bbq_sauce\": {\"TSR\": 54, \"CAR\": 22, \"avg_max_disp\": 0.0878}, \"frozen_rate\": 0, \"seed\": 7}}, \"eval_stepwise_s0_l1_24k_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"CAR\": 52.5, \"dfCAR\": 52.5, \"frozen_rate\": 0, \"TSR\": 50.5, \"per_task_CAR\": {\"orange_juice\": 54, \"chocolate_pudding\": 72, \"milk\": 64, \"bbq_sauce\": 20}, \"per_task_TSR\": {\"orange_juice\": 30, \"chocolate_pudding\": 78, \"milk\": 30, \"bbq_sauce\": 64}, \"per_task_frozen\": {\"orange_juice\": 0, \"chocolate_pudding\": 0, \"milk\": 0, \"bbq_sauce\": 0}}}, \"eval_stepwise_s0_l1_24k\": {\"status\": \"DONE\", \"metrics\": {\"INVALID\": true, \"invalidation_reason\": \"Missing --pi05 flag caused architecture mismatch (Pi0 instead of Pi0.5), producing 29.5% frozen episodes as artifact. All metrics from this eval are unreliable. See eval_stepwise_s0_l1_24k_v2 for corrected results.\", \"original_CAR\": 55.5, \"original_frozen_rate\": 29.5, \"original_dfCAR\": 36.9}, \"conclusion\": \"failed\"}, \"eval_stepwise_s0_l1_26k_v2\": {\"status\": \"DONE\", \"metrics\": {\"TSR\": 0.53, \"CAR\": 0.535, \"dfCAR\": 0.535, \"frozen_rate\": 0, \"frozen_episodes\": 0, \"total_episodes\": 200, \"per_task\": {\"orange_juice\": {\"TSR\": 0.32, \"CAR\": 0.46, \"dfCAR\": 0.46, \"frozen\": 0}, \"chocolate_pudding\": {\"TSR\": 0.76, \"CAR\": 0.72, \"dfCAR\": 0.72, \"frozen\": 0}, \"milk\": {\"TSR\": 0.5, \"CAR\": 0.68, \"dfCAR\": 0.68, \"frozen\": 0}, \"bbq_sauce\": {\"TSR\": 0.54, \"CAR\": 0.28, \"dfCAR\": 0.28, \"frozen\": 0}}}, \"conclusion\": \"success\"}, \"eval_stepwise_s0_l1_26k\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_spatial_sdf_s0_l005_30k\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"CAR\": 16, \"TSR\": 53, \"dfCAR\": 0, \"frozen_ratio\": 16, \"per_task_CAR\": {\"task0\": 0, \"task1\": 16, \"task2\": 4, \"task3\": 44}, \"per_task_TSR\": {\"task0\": 66, \"task1\": 38, \"task2\": 72, \"task3\": 36}, \"per_task_frozen\": {\"task0\": 0, \"task1\": 8, \"task2\": 2, \"task3\": 22}}}, \"eval_stepwise_s1_l1_22k\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"CAR\": 56.5, \"TSR\": 57.5, \"eval_seed\": 7, \"frozen_pct\": 0, \"seed\": 1, \"step\": 22000}}, \"train_pi05_lora_baseline_s2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_stepwise_s0_l1_22k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"CAR\": 60.5, \"TSR\": 45.5, \"frozen_pct\": 0, \"step\": 22000, \"seed\": 0, \"eval_seed\": 7}}, \"eval_stepwise_s0_l1_16k\": {\"status\": \"DONE\", \"metrics\": {\"CAR\": 55.5, \"TSR\": 49.5, \"per_task\": [{\"task\": \"orange_juice\", \"TSR\": 26, \"CAR\": 56}, {\"task\": \"pudding\", \"TSR\": 74, \"CAR\": 74}, {\"task\": \"milk\", \"TSR\": 38, \"CAR\": 68}, {\"task\": \"bbq_sauce\", \"TSR\": 60, \"CAR\": 24}]}, \"conclusion\": \"negative\"}, \"eval_early_signal_s1_l1_20k\": {\"status\": \"DONE\", \"metrics\": {\"CAR\": 56, \"TSR\": 51, \"frozen_ee\": 0, \"per_task_CAR\": {\"pick_up_the_orange_juice_and_place_it_in_the_basket\": 62, \"task1\": 76, \"pick_up_the_milk_and_place_it_in_the_basket\": 66, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 20}, \"per_task_TSR\": {\"pick_up_the_orange_juice_and_place_it_in_the_basket\": 20, \"task1\": 82, \"pick_up_the_milk_and_place_it_in_the_basket\": 42, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 60}}, \"conclusion\": \"negative\"}, \"eval_early_signal_s0_l1_20k\": {\"status\": \"DONE\", \"metrics\": {\"overall_CAR\": 0.55, \"overall_TSR\": 0.54, \"frozen_ee_pct\": 0, \"per_task\": [{\"task\": \"orange_juice\", \"CAR\": 0.5, \"TSR\": 0.38, \"avg_max_disp\": 0.0467, \"avg_max_ee_disp\": 0.3917}, {\"task\": \"chocolate_pudding\", \"CAR\": 0.72, \"TSR\": 0.74, \"avg_max_disp\": 0.0487, \"avg_max_ee_disp\": 0.4044}, {\"task\": \"milk\", \"CAR\": 0.72, \"TSR\": 0.44, \"avg_max_disp\": 0.0319, \"avg_max_ee_disp\": 0.3492}, {\"task\": \"bbq_sauce\", \"CAR\": 0.26, \"TSR\": 0.6, \"avg_max_disp\": 0.0928, \"avg_max_ee_disp\": 0.3895}], \"hard_constraints\": {\"TSR_ge_35\": true, \"frozen_ee_0\": true}, \"abc_signal\": \"B\", \"total_episodes\": 200}, \"conclusion\": \"negative\"}, \"train_pi05_a1_spatial_bowl_s0_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.0137, \"final_action_loss\": 0.0135, \"final_sdf_loss\": 0.0327, \"final_ee_loss\": 0.0068, \"best_loss\": 0.01063, \"best_step\": 28000, \"total_steps\": 30000, \"time_per_step\": 4.65, \"wall_clock_hours\": 28.4}}, \"analysis_threshold_sensitivity\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"dfCAR_stable_range_mm\": \"[2, 200]\", \"n_models\": 8, \"n_thresholds\": 8, \"n_active_equals_n_total_at_200mm\": true, \"max_dfCAR_variation_2_to_200mm\": 0, \"min_displacement_m\": 0.271, \"conclusion\": \"dfCAR perfectly invariant across tau_d in [2, 200] mm for all 8 model-seed combinations; only at 300mm do 1-2 episodes fall below threshold\"}}, \"reeval_sdf_s2_l005_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 56, \"CAR\": 52.5, \"avg_max_ee_disp\": 0.3858, \"frozen_ee\": 0, \"per_task\": {\"T0_orange_juice\": {\"TSR\": 34, \"CAR\": 46, \"ee_disp\": 0.3923, \"obj_disp\": 0.0598}, \"T1_chocolate_pudding\": {\"TSR\": 82, \"CAR\": 74, \"ee_disp\": 0.4098, \"obj_disp\": 0.046}, \"T2_milk\": {\"TSR\": 38, \"CAR\": 72, \"ee_disp\": 0.3574, \"obj_disp\": 0.0406}, \"T3_bbq_sauce\": {\"TSR\": 70, \"CAR\": 18, \"ee_disp\": 0.3838, \"obj_disp\": 0.0833}}}}, \"reeval_sdf_s2_l01_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 53.5, \"CAR\": 54.5, \"avg_max_ee_disp\": 0.3877, \"frozen_ee\": 0, \"per_task\": {\"T0_orange_juice\": {\"TSR\": 24, \"CAR\": 64, \"ee_disp\": 0.3822, \"obj_disp\": 0.0385}, \"T1_chocolate_pudding\": {\"TSR\": 72, \"CAR\": 68, \"ee_disp\": 0.4189, \"obj_disp\": 0.0517}, \"T2_milk\": {\"TSR\": 48, \"CAR\": 72, \"ee_disp\": 0.3567, \"obj_disp\": 0.0258}, \"T3_bbq_sauce\": {\"TSR\": 70, \"CAR\": 14, \"ee_disp\": 0.3931, \"obj_disp\": 0.0861}}}}, \"reeval_sdf_s1_l01_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 55.5, \"CAR\": 57.5, \"avg_max_ee_disp\": 0.3852, \"frozen_ee\": 0, \"per_task\": {\"T0_orange_juice\": {\"TSR\": 22, \"CAR\": 60, \"ee_disp\": 0.3892, \"obj_disp\": 0.0536}, \"T1_chocolate_pudding\": {\"TSR\": 80, \"CAR\": 76, \"ee_disp\": 0.4073, \"obj_disp\": 0.0472}, \"T2_milk\": {\"TSR\": 54, \"CAR\": 72, \"ee_disp\": 0.3552, \"obj_disp\": 0.0387}, \"T3_bbq_sauce\": {\"TSR\": 66, \"CAR\": 22, \"ee_disp\": 0.3892, \"obj_disp\": 0.0916}}}}, \"reeval_sdf_s1_l005_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 50.5, \"CAR\": 54, \"avg_max_ee_disp\": 0.3883, \"frozen_ee\": 0, \"per_task\": {\"T0_orange_juice\": {\"TSR\": 28, \"CAR\": 64, \"ee_disp\": 0.3816, \"obj_disp\": 0.0349}, \"T1_chocolate_pudding\": {\"TSR\": 72, \"CAR\": 70, \"ee_disp\": 0.4206, \"obj_disp\": 0.0491}, \"T2_milk\": {\"TSR\": 30, \"CAR\": 68, \"ee_disp\": 0.3588, \"obj_disp\": 0.0328}, \"T3_bbq_sauce\": {\"TSR\": 72, \"CAR\": 14, \"ee_disp\": 0.3924, \"obj_disp\": 0.0931}}}}, \"eval_lora_baseline_30k_s0_reeval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 51.5, \"CAR\": 56.5, \"avg_max_ee_disp\": 0.3957, \"frozen_ee\": 0, \"per_task\": {\"orange_juice\": {\"TSR\": 32, \"CAR\": 56}, \"chocolate_pudding\": {\"TSR\": 74, \"CAR\": 74}, \"milk\": {\"TSR\": 42, \"CAR\": 70}, \"bbq_sauce\": {\"TSR\": 58, \"CAR\": 26}}}}, \"reeval_sdf_s0_l005_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"tsr\": 55.5, \"car\": 57, \"frozen_rate_ee\": 0, \"fake_safe_rate_ee\": 0, \"per_task\": {\"orange_juice\": {\"tsr\": 38, \"car\": 52}, \"chocolate_pudding\": {\"tsr\": 80, \"car\": 74}, \"milk\": {\"tsr\": 38, \"car\": 74}, \"bbq_sauce\": {\"tsr\": 66, \"car\": 28}}}}, \"eval_phase2_lambda0_s2\": {\"status\": \"DONE\", \"metrics\": {\"per_task\": [{\"task_id\": 0, \"task_name\": \"pick_up_the_orange_juice_and_place_it_in_the_basket\", \"TSR\": 30, \"CAR\": 56, \"mean_max_ee_disp\": 0.3837, \"frozen_rate\": 0}, {\"task_id\": 1, \"task_name\": \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\", \"TSR\": 76, \"CAR\": 74, \"mean_max_ee_disp\": 0.4059, \"frozen_rate\": 0}, {\"task_id\": 2, \"task_name\": \"pick_up_the_milk_and_place_it_in_the_basket\", \"TSR\": 42, \"CAR\": 74, \"mean_max_ee_disp\": 0.3565, \"frozen_rate\": 0}, {\"task_id\": 3, \"task_name\": \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\", \"TSR\": 66, \"CAR\": 26, \"mean_max_ee_disp\": 0.3903, \"frozen_rate\": 0}], \"mean\": {\"TSR\": 53.5, \"CAR\": 57.5, \"mean_max_ee_disp\": 0.3841, \"frozen_rate\": 0}}, \"conclusion\": \"success\"}, \"train_pi05_phase2_lambda0_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss_action\": 0.0113, \"final_loss_sdf\": 0.1369, \"final_loss_ee\": 0.0079, \"best_loss\": 0.00651, \"best_step\": 4000, \"total_steps\": 10000, \"time_per_step\": 4.64, \"wall_clock_hours\": 12.88}}, \"reeval_lora_s1_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"tsr\": 51.5, \"car\": 52.5, \"ee_disp\": 0.3882, \"frozen_rate_ee\": 0, \"fake_safe_rate_ee\": 0, \"per_task\": {\"orange_juice\": {\"tsr\": 34, \"car\": 54}, \"chocolate_pudding\": {\"tsr\": 62, \"car\": 68}, \"milk\": {\"tsr\": 50, \"car\": 72}, \"bbq_sauce\": {\"tsr\": 60, \"car\": 16}}}}, \"reeval_sdf_s0_l01_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"tsr\": 52.5, \"car\": 57, \"ee_disp\": 0.3946, \"frozen_rate_ee\": 0, \"frozen_rate_obs\": 55.5, \"fake_safe_rate_ee\": 0, \"obstacle_disp\": 0.0577, \"ee_disp_range\": [0.312, 0.865], \"per_task\": {\"orange_juice\": {\"tsr\": 28, \"car\": 48}, \"chocolate_pudding\": {\"tsr\": 78, \"car\": 74}, \"milk\": {\"tsr\": 44, \"car\": 72}, \"bbq_sauce\": {\"tsr\": 60, \"car\": 34}}, \"note\": \"frozen_rate_ee = EE disp < 0.1mm (paper definition); frozen_rate_obs = obstacle disp < 0.1mm (analyzer script definition, NOT paper definition)\"}}, \"eval_pi05_baseline_reeval_disp\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_lora_baseline_30k_s0_v2\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 8.5, \"avg_CAR\": 54.5, \"n_episodes\": 200, \"frozen_pct\": 0, \"avg_ee_disp\": 0.4887, \"dfCAR_100mm\": 54.5, \"per_task\": [{\"task\": \"pick_up_the_orange_juice_and_place_it_in_the_basket\", \"safety\": \"II\", \"n\": 50, \"TSR\": 0, \"CAR\": 62, \"avg_ee_disp\": 0.497, \"median_ee_disp\": 0.4208, \"frozen_pct\": 0}, {\"task\": \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\", \"safety\": \"II\", \"n\": 50, \"TSR\": 34, \"CAR\": 44, \"avg_ee_disp\": 0.5041, \"median_ee_disp\": 0.4251, \"frozen_pct\": 0}, {\"task\": \"pick_up_the_milk_and_place_it_in_the_basket\", \"safety\": \"II\", \"n\": 50, \"TSR\": 0, \"CAR\": 94, \"avg_ee_disp\": 0.5765, \"median_ee_disp\": 0.5511, \"frozen_pct\": 0}, {\"task\": \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\", \"safety\": \"II\", \"n\": 50, \"TSR\": 0, \"CAR\": 18, \"avg_ee_disp\": 0.3772, \"median_ee_disp\": 0.3712, \"frozen_pct\": 0}]}, \"conclusion\": \"success\"}, \"eval_lora_baseline_30k_s1_v2\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 4, \"avg_CAR\": 56, \"dfCAR_100mm\": 56, \"avg_ee_disp\": 0.4669, \"frozen_pct\": 0, \"n_episodes\": 200, \"per_task\": {\"pick_up_the_orange_juice\": {\"TSR\": 2, \"CAR\": 58, \"ee_disp_mean\": 0.4827, \"ee_disp_median\": 0.4011, \"frozen_pct\": 0}, \"pick_up_the_chocolate_pudding\": {\"TSR\": 14, \"CAR\": 50, \"ee_disp_mean\": 0.538, \"ee_disp_median\": 0.4548, \"frozen_pct\": 0}, \"pick_up_the_milk\": {\"TSR\": 0, \"CAR\": 90, \"ee_disp_mean\": 0.4817, \"ee_disp_median\": 0.512, \"frozen_pct\": 0}, \"pick_up_the_bbq_sauce\": {\"TSR\": 0, \"CAR\": 26, \"ee_disp_mean\": 0.3653, \"ee_disp_median\": 0.3335, \"frozen_pct\": 0}}}, \"conclusion\": \"success\"}, \"eval_lora_baseline_30k_s1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_lora_baseline_30k_s0\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_pi05_lora_baseline_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.01408, \"best_loss\": 0.0113, \"best_step\": 14000, \"total_steps\": 30000, \"grad_norm\": 0.10628, \"time_per_step\": 4.62}}, \"train_pi05_lora_baseline_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.01343, \"best_loss\": 0.01025, \"best_step\": 24000, \"total_steps\": 30000, \"grad_norm\": 0.10538, \"time_per_step\": 4.613}}, \"eval_pi05_a1_30k_s0_l01_disp\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 6.5, \"avg_CAR\": 52.5, \"n_episodes\": 200, \"avg_max_ee_displacement\": 0.4725, \"task0_TSR\": 0, \"task0_CAR\": 76, \"task0_ee_disp\": 0.4781, \"task0_safe_ee_disp\": 0.4627, \"task1_TSR\": 26, \"task1_CAR\": 32, \"task1_ee_disp\": 0.5387, \"task1_safe_ee_disp\": 0.4446, \"task2_TSR\": 0, \"task2_CAR\": 84, \"task2_ee_disp\": 0.5169, \"task2_safe_ee_disp\": 0.5273, \"task3_TSR\": 0, \"task3_CAR\": 18, \"task3_ee_disp\": 0.3561, \"task3_safe_ee_disp\": 0.3764, \"fake_safe_pct\": 0, \"real_safety\": true, \"frozen\": false}}, \"eval_pi05_a1_30k_s1_l005_disp\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 4, \"avg_CAR\": 54, \"n_episodes\": 200, \"avg_max_ee_displacement\": 0.4955, \"task0_TSR\": 2, \"task0_CAR\": 54, \"task0_ee_disp\": 0.5062, \"task0_safe_ee_disp\": 0.4247, \"task1_TSR\": 14, \"task1_CAR\": 58, \"task1_ee_disp\": 0.4991, \"task1_safe_ee_disp\": 0.5006, \"task2_TSR\": 0, \"task2_CAR\": 92, \"task2_ee_disp\": 0.6088, \"task2_safe_ee_disp\": 0.6213, \"task3_TSR\": 0, \"task3_CAR\": 12, \"task3_ee_disp\": 0.368, \"task3_safe_ee_disp\": 0.3628, \"fake_safe_pct\": 0, \"real_safety\": true, \"frozen\": false}}, \"eval_pi05_a1_best_s2_l005_10k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 9, \"avg_CAR\": 55.5, \"n_episodes\": 200, \"avg_max_ee_displacement\": 0.5046, \"task0_TSR\": 0, \"task0_CAR\": 68, \"task0_ee_disp\": 0.5256, \"task0_safe_ee_disp\": 0.4979, \"task1_TSR\": 36, \"task1_CAR\": 44, \"task1_ee_disp\": 0.5288, \"task1_safe_ee_disp\": 0.5115, \"task2_TSR\": 0, \"task2_CAR\": 92, \"task2_ee_disp\": 0.5779, \"task2_safe_ee_disp\": 0.5883, \"task3_TSR\": 0, \"task3_CAR\": 18, \"task3_ee_disp\": 0.3863, \"task3_safe_ee_disp\": 0.3609, \"fake_safe_pct\": 0, \"task2_fake_safety\": false, \"real_safety\": true, \"task0_obs_frozen_pct\": 0.7, \"task2_obs_frozen_pct\": 0.92, \"analysis\": \"ALL episodes have high EE displacement (0.39-0.58m). Zero fake safety. 10K best shows genuine collision avoidance: robot moves normally and avoids obstacles. Task 2 high CAR (92%) is REAL avoidance not action collapse.\"}}, \"eval_pi05_a1_best_s1_l005_16k\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 6.5, \"avg_CAR\": 53, \"n_episodes\": 200, \"task0_TSR\": 4, \"task0_CAR\": 58, \"task0_ee_disp\": 0.5179, \"task0_max_disp\": 0.0416, \"task1_TSR\": 22, \"task1_CAR\": 50, \"task1_ee_disp\": 0.5146, \"task1_max_disp\": 0.1018, \"task2_TSR\": 0, \"task2_CAR\": 88, \"task2_ee_disp\": 0.6475, \"task2_max_disp\": 0.0073, \"task3_TSR\": 0, \"task3_CAR\": 16, \"task3_ee_disp\": 0.3707, \"task3_max_disp\": 0.0934, \"fake_safe_pct\": 0, \"real_safety\": true}, \"conclusion\": \"success\"}, \"eval_pi05_a1_30k_s1_l01_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 7.5, \"avg_CAR\": 52.5, \"n_episodes\": 200, \"task0_TSR\": 4, \"task0_CAR\": 54, \"task1_TSR\": 26, \"task1_CAR\": 48, \"task2_TSR\": 0, \"task2_CAR\": 94, \"task3_TSR\": 0, \"task3_CAR\": 14}}, \"eval_pi05_a1_30k_s1_l005_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 5.5, \"avg_CAR\": 52.5, \"n_episodes\": 200, \"task0_TSR\": 4, \"task0_CAR\": 58, \"task1_TSR\": 18, \"task1_CAR\": 40, \"task2_TSR\": 0, \"task2_CAR\": 94, \"task3_TSR\": 0, \"task3_CAR\": 18}}, \"eval_pi05_a1_30k_s2_l005_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 9.5, \"avg_CAR\": 54.5, \"n_episodes\": 200, \"task0_TSR\": 2, \"task0_CAR\": 62, \"task1_TSR\": 36, \"task1_CAR\": 44, \"task2_TSR\": 0, \"task2_CAR\": 90, \"task3_TSR\": 0, \"task3_CAR\": 22}}, \"eval_pi05_a1_30k_s1_l005_v3\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 4, \"avg_CAR\": 51.5, \"n_episodes\": 200, \"task0_TSR\": 0, \"task0_CAR\": 54, \"task1_TSR\": 16, \"task1_CAR\": 48, \"task2_TSR\": 0, \"task2_CAR\": 88, \"task3_TSR\": 0, \"task3_CAR\": 16, \"source\": \"v4 JSON with per-episode displacement\"}, \"conclusion\": \"success\"}, \"eval_pi05_a1_30k_s2_l005_v3\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 9, \"avg_CAR\": 53, \"n_episodes\": 200, \"task0_TSR\": 4, \"task0_CAR\": 60, \"task1_TSR\": 32, \"task1_CAR\": 46, \"task2_TSR\": 0, \"task2_CAR\": 86, \"task3_TSR\": 0, \"task3_CAR\": 20, \"source\": \"v4 JSON with per-episode displacement\"}, \"conclusion\": \"success\"}, \"eval_pi05_a1_30k_s2_l01_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 7.5, \"avg_CAR\": 53, \"n_episodes\": 200, \"task0_TSR\": 0, \"task0_CAR\": 62, \"task1_TSR\": 30, \"task1_CAR\": 42, \"task2_TSR\": 0, \"task2_CAR\": 88, \"task3_TSR\": 0, \"task3_CAR\": 20, \"source\": \"v3 JSON with per-episode displacement\"}}, \"eval_pi05_a1_30k_s0_l01\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 5.5, \"avg_CAR\": 53, \"n_episodes\": 200, \"task0_TSR\": 2, \"task0_CAR\": 68, \"task1_TSR\": 20, \"task1_CAR\": 46, \"task2_TSR\": 0, \"task2_CAR\": 86, \"task3_TSR\": 0, \"task3_CAR\": 12, \"task0_disp\": 0.0297, \"task1_disp\": 0.0815, \"task2_disp\": 0.0112, \"task3_disp\": 0.0797, \"note\": \"旧版脚本，无max_ee_displacement字段\"}}, \"eval_pi05_a1_30k_s0_l005_r4\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 7.5, \"avg_CAR\": 47, \"n_episodes\": 200, \"task0_TSR\": 6, \"task0_CAR\": 58, \"task1_TSR\": 24, \"task1_CAR\": 38, \"task2_TSR\": 0, \"task2_CAR\": 76, \"task3_TSR\": 0, \"task3_CAR\": 16, \"task0_disp\": 0.0485, \"task1_disp\": 0.0782, \"task2_disp\": 0.0147, \"task3_disp\": 0.1009, \"note\": \"旧版脚本，无max_ee_displacement字段\"}, \"conclusion\": \"success\"}, \"train_pi05_phase2_lambda0_s0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_a1_30k_s0_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 5.5, \"avg_CAR\": 50, \"n_episodes\": 200, \"task0_TSR\": 2, \"task0_CAR\": 58, \"task1_TSR\": 20, \"task1_CAR\": 42, \"task2_TSR\": 0, \"task2_CAR\": 86, \"task3_TSR\": 0, \"task3_CAR\": 14, \"task0_disp\": 0.0433, \"task1_disp\": 0.1055, \"task2_disp\": 0.0147, \"task3_disp\": 0.0879}}, \"train_pi05_a1_obj_s0_l01\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.00801, \"steps_completed\": 30000}}, \"train_pi05_a1_obj_s0_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.007860926911234856, \"best_loss_step\": 26000, \"steps_completed\": 30000}}, \"eval_pi05_a1_30k_s2_l01\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_a1_30k_s2_l005\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_a1_30k_s1_l01\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_a1_30k_s1_l005\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_pi05_a1_obj_s2_l01\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.00911, \"best_loss_step\": 10000, \"steps_completed\": 30000}}, \"train_pi05_a1_obj_s2_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.00874, \"best_loss_step\": 10000, \"steps_completed\": 30000}}, \"train_pi05_a1_obj_s1_l01\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.01168, \"best_loss_step\": 16000, \"steps_completed\": 30000}}, \"train_pi05_a1_obj_s1_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.01143, \"best_loss_step\": 16000, \"steps_completed\": 30000}}, \"train_pi05_a1_obj_l01\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_pi05_a1_obj_l005\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_safelibero_object_v11_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 0.75, \"CAR\": 0.275, \"mean_displacement\": 0.132}}, \"eval_pi05_safelibero_object_v11_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 0.76, \"CAR\": 0.25, \"mean_displacement\": 0.153}}, \"eval_pi05_safelibero_spatial_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_TSR\": 0.575, \"overall_CAR\": 0.13, \"task3_CAR\": 0.52, \"n_episodes\": 200}}, \"eval_pi05_safelibero_object_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_TSR\": 0.73, \"overall_CAR\": 0.28, \"overall_avg_disp\": 0.1508, \"real_safe_rate\": 0.005, \"fake_safe_rate\": 0.982, \"task0_TSR\": 0.64, \"task0_CAR\": 0.06, \"task1_TSR\": 0.86, \"task1_CAR\": 0.56, \"task2_TSR\": 0.66, \"task2_CAR\": 0.16, \"task3_TSR\": 0.76, \"task3_CAR\": 0.34, \"n_episodes\": 200}}, \"eval_a3_spatial_force_refine_v11\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_a3_spatial_m024fix_v11\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"oracle_true_gt_feature_object_v11\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_a1_lora_object_v11_rerun\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 0, \"avg_CAR\": 91.5, \"n_episodes\": 800, \"eps_per_task\": 200, \"task_TSR\": {\"orange_juice\": 0, \"chocolate_pudding\": 0, \"milk\": 0, \"bbq_sauce\": 0}, \"task_CAR\": {\"orange_juice\": 96, \"chocolate_pudding\": 82, \"milk\": 97, \"bbq_sauce\": 91}, \"fake_safe_rate\": 0.996, \"fake_safe_detail\": \"729/732 safe episodes have displacement<0.1mm\", \"real_safe_count\": 3, \"real_safe_rate\": 0.004, \"safe_disp_distribution\": {\"<1um\": 541, \"1um-0.1mm\": 188, \"0.1-1mm\": 3, \">1mm\": 0}, \"task_fake_safe\": {\"orange_juice\": \"192/192 (100%)\", \"chocolate_pudding\": \"162/164 (98.8%)\", \"milk\": \"194/194 (100%)\", \"bbq_sauce\": \"181/182 (99.5%)\"}, \"task_avg_disp_mm\": {\"orange_juice\": 0.871, \"chocolate_pudding\": 7.491, \"milk\": 2.508, \"bbq_sauce\": 4.75}, \"task_safe_disp_mean_mm\": {\"orange_juice\": 0.000315, \"chocolate_pudding\": 0.007588, \"milk\": 0.000288, \"bbq_sauce\": 0.001293}, \"collision_eps\": 68, \"collision_disp_mean_mm\": 45.92, \"collision_disp_max_mm\": 286.53, \"baseline_comparison\": {\"baseline_CAR\": 83, \"baseline_fake_safe\": \"165/166 (99.4%)\", \"baseline_real_safe\": \"1/200 (0.5%)\", \"baseline_n_episodes\": 200}}}, \"oracle_true_gt_feature_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 0, \"avg_CAR\": 76.9, \"task_CAR\": {\"orange_juice\": 90, \"chocolate_pudding\": 47.5, \"milk\": 82.5, \"bbq_sauce\": 87.5}, \"task_displacement\": {\"orange_juice\": 0.0023, \"chocolate_pudding\": 0.0473, \"milk\": 0.0086, \"bbq_sauce\": 0.0097}, \"task_refine_count_mean\": {\"orange_juice\": 248.5, \"chocolate_pudding\": 241.8, \"milk\": 236.7, \"bbq_sauce\": 240}, \"task_grad_mag_mean\": {\"orange_juice\": 0.00423, \"chocolate_pudding\": 0.00609, \"milk\": 0.00466, \"bbq_sauce\": 0.00491}, \"fake_safe_rate\": 0.967, \"fake_safe_detail\": \"119/123 safe episodes have displacement<0.1mm\", \"total_refined_steps\": 38679, \"avg_refined_per_episode\": 241.7, \"n_episodes\": 160}}, \"oracle_true_gt_fixed_alpha_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 0, \"avg_CAR\": 73.1, \"task_CAR\": {\"orange_juice\": 85, \"chocolate_pudding\": 50, \"milk\": 77.5, \"bbq_sauce\": 80}, \"task_displacement\": {\"orange_juice\": 0.0113, \"chocolate_pudding\": 0.0365, \"milk\": 0.0042, \"bbq_sauce\": 0.0032}, \"task_refine_count_mean\": {\"orange_juice\": 8.7, \"chocolate_pudding\": 20.2, \"milk\": 20.1, \"bbq_sauce\": 10.4}, \"total_refined_steps\": 2375, \"avg_refined_per_episode\": 14.8, \"fake_safe_rate\": 0.983, \"fake_safe_detail\": \"115/117 safe episodes have displacement<0.1mm\", \"task_fake_safe\": {\"orange_juice\": \"34/34 (100%)\", \"chocolate_pudding\": \"19/20 (95%)\", \"milk\": \"30/31 (96.8%)\", \"bbq_sauce\": \"32/32 (100%)\"}, \"collision_threshold\": 0.001, \"n_episodes\": 160}}, \"oracle_true_gt_adaptive_alpha_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 0, \"avg_CAR\": 75, \"task_CAR\": {\"orange_juice\": 82.5, \"chocolate_pudding\": 55, \"milk\": 77.5, \"bbq_sauce\": 85}, \"task_displacement\": {\"orange_juice\": 0.0076, \"chocolate_pudding\": 0.0475, \"milk\": 0.0107, \"bbq_sauce\": 0.0077}, \"task_refine_count_mean\": {\"orange_juice\": 7.6, \"chocolate_pudding\": 22.4, \"milk\": 17.6, \"bbq_sauce\": 9.1}, \"task_grad_mag_mean\": {\"orange_juice\": 0.176, \"chocolate_pudding\": 0.247, \"milk\": 0.489, \"bbq_sauce\": 0.357}, \"fake_safe_rate\": 0.983, \"fake_safe_detail\": \"118/120 safe episodes have displacement<0.1mm\", \"total_refined_steps\": 2270, \"avg_refined_per_episode\": 14.2, \"n_episodes\": 160}}, \"a3_gradient_spatial_bowl_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.01552, \"steps_completed\": 30000}}, \"oracle_true_gt_object_v11\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_a3_object_m024fix_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"task0\": {\"TSR\": 0, \"CAR\": 0.885, \"avg_max_displacement\": 0.0066, \"refined_count\": 0}, \"task1\": {\"TSR\": 0, \"CAR\": 0.46, \"avg_max_displacement\": 0.0492, \"refined_count\": 0}, \"task2\": {\"TSR\": 0, \"CAR\": 0.86, \"avg_max_displacement\": 0.0044, \"refined_count\": 0}, \"task3\": {\"TSR\": 0, \"CAR\": 0.88, \"avg_max_displacement\": 0.0074, \"refined_count\": 0}, \"overall\": {\"avg_TSR\": 0, \"avg_CAR\": 0.771}}}, \"eval_a1_lora_spatial_v11\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 0.001, \"avg_CAR\": 0.008, \"task0_TSR\": 0.005, \"task0_CAR\": 0.015, \"task0_avg_disp\": 0.2578, \"task1_TSR\": 0, \"task1_CAR\": 0, \"task1_avg_disp\": 0.1955, \"task2_TSR\": 0, \"task2_CAR\": 0, \"task2_avg_disp\": 0.2142, \"task3_TSR\": 0, \"task3_CAR\": 0.015, \"task3_avg_disp\": 0.1992, \"safe_episodes_total\": 6, \"safe_episodes_with_zero_displacement\": 6, \"fake_safety\": true}, \"conclusion\": \"negative\"}, \"eval_baseline_fullft_spatial_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR_avg\": 0.375, \"CAR_avg\": 0, \"n_episodes\": 800, \"per_task\": {\"task0_pick_bowl_between_plate_ramekin\": {\"TSR\": 1.5, \"CAR\": 0, \"avg_max_displacement\": 0.3317, \"avg_smoothness\": 0.003487}, \"task1_pick_bowl_on_ramekin\": {\"TSR\": 0, \"CAR\": 0, \"avg_max_displacement\": 0.2863, \"avg_smoothness\": 0.00326}, \"task2_pick_bowl_on_stove\": {\"TSR\": 0, \"CAR\": 0, \"avg_max_displacement\": 0.2604, \"avg_smoothness\": 0.002417}, \"task3_pick_bowl_on_cabinet\": {\"TSR\": 0, \"CAR\": 0, \"avg_max_displacement\": 0.3017, \"avg_smoothness\": 0.003154}}}}, \"oracle_a3_m024fix_object_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"task0_pick_orange_juice\": {\"TSR\": 0, \"CAR\": 97.5, \"avg_max_displacement\": 0.0028}, \"task1_put_wine_on_rack\": {\"TSR\": 0, \"CAR\": 65, \"avg_max_displacement\": 0.0381}, \"task2_put_cream_in_marked_area\": {\"TSR\": 0, \"CAR\": 97.5, \"avg_max_displacement\": 0}, \"task3_pick_bbq_sauce_to_basket\": {\"TSR\": 0, \"CAR\": 82.5, \"avg_max_displacement\": 0.0134}, \"overall\": {\"TSR_avg\": 0, \"CAR_avg\": 85.6}, \"n_episodes\": 40, \"force_refine\": true, \"refine_count_per_episode\": 300}}, \"oracle_a3_force_refine_object_v11\": {\"status\": \"DONE\", \"metrics\": {\"TSR_avg\": 0, \"CAR_avg\": 81.2, \"n_episodes\": 40, \"per_task\": {\"orange_juice\": {\"TSR\": 0, \"CAR\": 95, \"avg_max_displacement\": 0.0005}, \"chocolate_pudding\": {\"TSR\": 0, \"CAR\": 57.5, \"avg_max_displacement\": 0.046}, \"milk\": {\"TSR\": 0, \"CAR\": 92.5, \"avg_max_displacement\": 0.001}, \"bbq_sauce\": {\"TSR\": 0, \"CAR\": 80, \"avg_max_displacement\": 0.0018}}, \"refined_count_per_episode\": 300, \"force_refine\": true, \"refine_alpha\": 0.1, \"refine_margin\": 0.01, \"displacement_collapse\": \"most episodes show max_displacement 1e-6 to 1e-10, gradient near-zero\"}, \"conclusion\": \"negative\"}, \"a1_lora_spatial_bowl_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.01431, \"steps_completed\": 30000}}, \"eval_a1_lora_object_v11\": {\"status\": \"DONE\", \"metrics\": {\"TSR\": 0, \"CAR_avg\": 90, \"CAR_task0\": 96, \"CAR_task1\": 80, \"CAR_task2\": 94, \"CAR_task3\": 90, \"displacement_avg\": 0.0027, \"displacement_task0\": 0.0017, \"displacement_task1\": 0.0076, \"displacement_task2\": 0.0008, \"displacement_task3\": 0.0008, \"n_episodes\": 200}, \"conclusion\": \"success\"}, \"eval_lora_baseline_object_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR\": 0, \"CAR_avg\": 82, \"CAR_task0\": 96, \"CAR_task1\": 46, \"CAR_task2\": 98, \"CAR_task3\": 88, \"displacement_avg\": 0.01, \"displacement_task0\": 0.0072, \"displacement_task1\": 0.0257, \"displacement_task2\": 1e-05, \"displacement_task3\": 0.007, \"n_episodes\": 200}}, \"eval_lora_baseline_spatial_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR\": 0, \"CAR_avg\": 0, \"CAR_task0\": 0, \"CAR_task1\": 0, \"CAR_task2\": 0, \"CAR_task3\": 0, \"displacement_avg\": 0.23, \"displacement_task0\": 0.2669, \"displacement_task1\": 0.206, \"displacement_task2\": 0.2212, \"displacement_task3\": 0.2328, \"n_episodes\": 200}}, \"eval_a3_v11_object\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR\": 0, \"CAR_avg\": 74.5, \"CAR_task0\": 84, \"CAR_task1\": 48, \"CAR_task2\": 82, \"CAR_task3\": 84, \"displacement_avg\": 0.0164, \"displacement_task0\": 0.0149, \"displacement_task1\": 0.0388, \"displacement_task2\": 0.0079, \"displacement_task3\": 0.0041, \"refined_count_total\": 0, \"n_episodes\": 200}}, \"a1_lora_object_pudding_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.01326, \"final_loss\": 0.0184, \"steps_completed\": 30000, \"wall_time_hours\": 33}}, \"eval_baseline_v11_object\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR\": 0.5, \"CAR_avg\": 83, \"CAR_task0\": 76, \"CAR_task1\": 90, \"CAR_task2\": 88, \"CAR_task3\": 78, \"TSR_task0\": 0, \"TSR_task1\": 2, \"TSR_task2\": 0, \"TSR_task3\": 0, \"displacement_avg\": 0.0271, \"displacement_task0\": 0.038, \"displacement_task1\": 0.0103, \"displacement_task2\": 0.0163, \"displacement_task3\": 0.0438, \"smoothness_avg\": 0.002109, \"n_episodes\": 200}}, \"baseline_lora_object_pudding_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.0124, \"steps_completed\": 30000}}, \"baseline_lora_spatial_bowl_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.00876, \"steps_completed\": 30000}}, \"eval_a3_v10a_refine\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR\": 0, \"CAR_avg\": 79.5, \"CAR_task0\": 90, \"CAR_task1\": 88, \"CAR_task2\": 64, \"CAR_task3\": 76, \"displacement_avg\": 0.0112, \"displacement_task0\": 0.0009, \"displacement_task1\": 0.0108, \"displacement_task2\": 0.0168, \"displacement_task3\": 0.0162, \"refined_count\": 0, \"n_episodes\": 200}}, \"eval_a3_object_pudding_no_refine\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_a3_object_pudding_refine\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"TSR\": 0, \"CAR_task0_orange_juice\": 96, \"CAR_task1_chocolate_pudding\": 22, \"CAR_task2_milk\": 66, \"CAR_task3_bbq_sauce\": 42, \"CAR_avg\": 56.5, \"TSR_task0\": 0, \"TSR_task1\": 0, \"TSR_task2\": 0, \"TSR_task3\": 0, \"n_episodes\": 50, \"refine_count_all_zero\": true}}, \"a3_gradient_object_pudding_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"action_loss\": 0.01546, \"total_loss\": 0.01898, \"final_loss\": 0.01898, \"best_loss\": 0.01439, \"ee_loss\": 0.01213, \"eikonal\": 0, \"grad_norm\": 0.24129, \"n_refine\": 2.64, \"steps_completed\": 30000}}, \"baseline_spatial_bowl_s0_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.0032, \"best_loss\": 0.00316, \"steps_completed\": 30000, \"lr_final\": 2.5e-06, \"wall_time_hours\": 16.1, \"vram_mib\": 35738, \"checkpoint_step\": 30000, \"avg_it_per_sec\": 3.62}}, \"baseline_object_pudding_s0_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.005, \"steps_completed\": 30000, \"lr_final\": 2.5e-06, \"wall_time_hours\": 14, \"vram_mib\": 35738}}, \"a1_sdf_spatial_bowl_s0_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"a1_sdf_object_pudding_s0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"baseline_spatial_bowl_s1_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"a1_sdf_spatial_bowl_s0_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"a1_sdf_spatial_bowl_s0\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"baseline_spatial_bowl_s0\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"baseline_spatial_bowl_s1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"baseline_object_pudding_s0\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}}, \"count\": 123, \"total\": 123, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.579}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "17985170-124c-4eec-95e0-2b0f56a920a2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_multiseed_sdf_l01_s0_eseed256\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval_multiseed_sdf_l01_s0_eseed123\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval_multiseed_sdf_l01_s0_eseed42\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval_multiseed_lora_s0_eseed123\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval_multiseed_lora_s0_eseed42\\\": {\\\"status\\\": \\\"PREPARING\\\"}, \\\"eval_pi05_a1_30k_s2_l01_high\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"car\\\": 54.5, \\\"tsr\\\": 54.5, \\\"per_task_car\\\": {\\\"orange_juice\\\": 56, \\\"chocolate_pudding\\\": 76, \\\"milk\\\": 70, \\\"bbq_sauce\\\": 16}, \\\"per_task_tsr\\\": {\\\"orange_juice\\\": 30, \\\"chocolate_pudding\\\": 72, \\\"milk\\\": 48, \\\"bbq_sauce\\\": 68}, \\\"scenario\\\": \\\"B\\\"}}, \\\"train_pi05_a1_obj_s2_l01_high\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss\\\": 0.0104, \\\"final_action_loss\\\": 0.0069, \\\"final_sdf_loss\\\": 0.0336, \\\"final_ee_loss\\\": 0.0096, \\\"best_loss\\\": 0.0104, \\\"best_step\\\": 30000, \\\"total_steps\\\": 30000, \\\"training_hours\\\": 33.86}}, \\\"eval_spatial_bowl_lora_ctrl_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 0.5, \\\"avg_CAR\\\": 0.155, \\\"task0_TSR\\\": 0.66, \\\"task0_CAR\\\": 0, \\\"task1_TSR\\\": 0.36, \\\"task1_CAR\\\": 0.14, \\\"task2_TSR\\\": 0.6, \\\"task2_CAR\\\": 0.04, \\\"task3_TSR\\\": 0.38, \\\"task3_CAR\\\": 0.44}}, \\\"eval_pi05_a1_best_s0_l005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 0.52, \\\"avg_CAR\\\": 0.545, \\\"task0_TSR\\\": 0.28, \\\"task0_CAR\\\": 0.5, \\\"task1_TSR\\\": 0.7, \\\"task1_CAR\\\": 0.74, \\\"task2_TSR\\\": 0.52, \\\"task2_CAR\\\": 0.68, \\\"task3_TSR\\\": 0.58, \\\"task3_CAR\\\": 0.26, \\\"n_episodes\\\": 50, \\\"seed\\\": 7, \\\"collision_threshold\\\": 0.001}}, \\\"train_phase2_lambda0_extra_seed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_spatial_bowl_lora_control_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_lora_s2_30k_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_TSR\\\": 0.515, \\\"overall_CAR\\\": 0.55, \\\"task0_orange_juice\\\": {\\\"TSR\\\": 0.24, \\\"CAR\\\": 0.56}, \\\"task1_chocolate_pudding\\\": {\\\"TSR\\\": 0.76, \\\"CAR\\\": 0.76}, \\\"task2_milk\\\": {\\\"TSR\\\": 0.42, \\\"CAR\\\": 0.62}, \\\"task3_bbq_sauce\\\": {\\\"TSR\\\": 0.64, \\\"CAR\\\": 0.26}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"train_phase2_lambda0_s2_v4\\\": {\\\"status\\\": \\\"RUNNING\\\"}, \\\"train_phase2_lambda0_extra_seed_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"train_phase2_lambda0_s2_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"train_phase2_lambda0_extra_seed_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_lora_baseline_30k_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_spatial_bowl_sdf_s0_l005_30k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 0.53, \\\"avg_CAR\\\": 0.17, \\\"task0_TSR\\\": 0.62, \\\"task0_CAR\\\": 0, \\\"task1_TSR\\\": 0.34, \\\"task1_CAR\\\": 0.14, \\\"task2_TSR\\\": 0.66, \\\"task2_CAR\\\": 0, \\\"task3_TSR\\\": 0.5, \\\"task3_CAR\\\": 0.54}}, \\\"train_pi05_lora_baseline_s2_resume\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"final_loss\\\": 0.0117, \\\"final_lr\\\": 2.5e-06, \\\"total_steps\\\": 30000, \\\"training_time_h\\\": 10.31}, \\\"conclusion\\\": \\\"success\\\"}, \\\"train_phase2_lambda0_s2_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_pi05_a1_30k_s1_l01_high\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"CAR\\\": 0.585, \\\"TSR\\\": 0.49, \\\"frozen_rate\\\": 0, \\\"dfCAR\\\": 0.585, \\\"avg_max_ee_displacement\\\": 0.3884, \\\"avg_max_obstacle_displacement\\\": 0.0553, \\\"per_task\\\": {\\\"orange_juice\\\": {\\\"TSR\\\": 0.26, \\\"CAR\\\": 0.66, \\\"avg_max_ee_displacement\\\": 0.3882, \\\"avg_max_obstacle_displacement\\\": 0.0333}, \\\"chocolate_pudding\\\": {\\\"TSR\\\": 0.8, \\\"CAR\\\": 0.72, \\\"avg_max_ee_displacement\\\": 0.4057, \\\"avg_max_obstacle_displacement\\\": 0.0545}, \\\"milk\\\": {\\\"TSR\\\": 0.28, \\\"CAR\\\": 0.7, \\\"avg_max_ee_displacement\\\": 0.3551, \\\"avg_max_obstacle_displacement\\\": 0.0408}, \\\"bbq_sauce\\\": {\\\"TSR\\\": 0.62, \\\"CAR\\\": 0.26, \\\"avg_max_ee_displacement\\\": 0.4045, \\\"avg_max_obstacle_displacement\\\": 0.0927}}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"reeval_lora_s0_30k_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"CAR\\\": 57, \\\"TSR\\\": 46, \\\"per_task\\\": {\\\"orange_juice\\\": 68, \\\"chocolate_pudding\\\": 74, \\\"milk\\\": 66, \\\"bbq_sauce\\\": 20}}}, \\\"eval_pi05_a1_30k_s0_l01_high\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"CAR\\\": 58, \\\"TSR\\\": 47, \\\"frozen_rate\\\": 0, \\\"avg_max_ee_displacement\\\": 0.4, \\\"dfCAR\\\": 58}}, \\\"train_pi05_a1_obj_s1_l01_high\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"train_pi05_a1_obj_s0_l01_high\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_stepwise_s0_l1_28k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 48.5, \\\"avg_CAR\\\": 54.5, \\\"task0_orange_juice\\\": {\\\"TSR\\\": 28, \\\"CAR\\\": 50, \\\"avg_max_disp\\\": 0.0618}, \\\"task1_chocolate_pudding\\\": {\\\"TSR\\\": 68, \\\"CAR\\\": 74, \\\"avg_max_disp\\\": 0.0463}, \\\"task2_milk\\\": {\\\"TSR\\\": 44, \\\"CAR\\\": 72, \\\"avg_max_disp\\\": 0.0277}, \\\"task3_bbq_sauce\\\": {\\\"TSR\\\": 54, \\\"CAR\\\": 22, \\\"avg_max_disp\\\": 0.0878}, \\\"frozen_rate\\\": 0, \\\"seed\\\": 7}}, \\\"eval_stepwise_s0_l1_24k_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"CAR\\\": 52.5, \\\"dfCAR\\\": 52.5, \\\"frozen_rate\\\": 0, \\\"TSR\\\": 50.5, \\\"per_task_CAR\\\": {\\\"orange_juice\\\": 54, \\\"chocolate_pudding\\\": 72, \\\"milk\\\": 64, \\\"bbq_sauce\\\": 20}, \\\"per_task_TSR\\\": {\\\"orange_juice\\\": 30, \\\"chocolate_pudding\\\": 78, \\\"milk\\\": 30, \\\"bbq_sauce\\\": 64}, \\\"per_task_frozen\\\": {\\\"orange_juice\\\": 0, \\\"chocolate_pudding\\\": 0, \\\"milk\\\": 0, \\\"bbq_sauce\\\": 0}}}, \\\"eval_stepwise_s0_l1_24k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"INVALID\\\": true, \\\"invalidation_reason\\\": \\\"Missing --pi05 flag caused architecture mismatch (Pi0 instead of Pi0.5), producing 29.5% frozen episodes as artifact. All metrics from this eval are unreliable. See eval_stepwise_s0_l1_24k_v2 for corrected results.\\\", \\\"original_CAR\\\": 55.5, \\\"original_frozen_rate\\\": 29.5, \\\"original_dfCAR\\\": 36.9}, \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_stepwise_s0_l1_26k_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"TSR\\\": 0.53, \\\"CAR\\\": 0.535, \\\"dfCAR\\\": 0.535, \\\"frozen_rate\\\": 0, \\\"frozen_episodes\\\": 0, \\\"total_episodes\\\": 200, \\\"per_task\\\": {\\\"orange_juice\\\": {\\\"TSR\\\": 0.32, \\\"CAR\\\": 0.46, \\\"dfCAR\\\": 0.46, \\\"frozen\\\": 0}, \\\"chocolate_pudding\\\": {\\\"TSR\\\": 0.76, \\\"CAR\\\": 0.72, \\\"dfCAR\\\": 0.72, \\\"frozen\\\": 0}, \\\"milk\\\": {\\\"TSR\\\": 0.5, \\\"CAR\\\": 0.68, \\\"dfCAR\\\": 0.68, \\\"frozen\\\": 0}, \\\"bbq_sauce\\\": {\\\"TSR\\\": 0.54, \\\"CAR\\\": 0.28, \\\"dfCAR\\\": 0.28, \\\"frozen\\\": 0}}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_stepwise_s0_l1_26k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_spatial_sdf_s0_l005_30k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"CAR\\\": 16, \\\"TSR\\\": 53, \\\"dfCAR\\\": 0, \\\"frozen_ratio\\\": 16, \\\"per_task_CAR\\\": {\\\"task0\\\": 0, \\\"task1\\\": 16, \\\"task2\\\": 4, \\\"task3\\\": 44}, \\\"per_task_TSR\\\": {\\\"task0\\\": 66, \\\"task1\\\": 38, \\\"task2\\\": 72, \\\"task3\\\": 36}, \\\"per_task_frozen\\\": {\\\"task0\\\": 0, \\\"task1\\\": 8, \\\"task2\\\": 2, \\\"task3\\\": 22}}}, \\\"eval_stepwise_s1_l1_22k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"CAR\\\": 56.5, \\\"TSR\\\": 57.5, \\\"eval_seed\\\": 7, \\\"frozen_pct\\\": 0, \\\"seed\\\": 1, \\\"step\\\": 22000}}, \\\"train_pi05_lora_baseline_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_stepwise_s0_l1_22k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"CAR\\\": 60.5, \\\"TSR\\\": 45.5, \\\"frozen_pct\\\": 0, \\\"step\\\": 22000, \\\"seed\\\": 0, \\\"eval_seed\\\": 7}}, \\\"eval_stepwise_s0_l1_16k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"CAR\\\": 55.5, \\\"TSR\\\": 49.5, \\\"per_task\\\": [{\\\"task\\\": \\\"orange_juice\\\", \\\"TSR\\\": 26, \\\"CAR\\\": 56}, {\\\"task\\\": \\\"pudding\\\", \\\"TSR\\\": 74, \\\"CAR\\\": 74}, {\\\"task\\\": \\\"milk\\\", \\\"TSR\\\": 38, \\\"CAR\\\": 68}, {\\\"task\\\": \\\"bbq_sauce\\\", \\\"TSR\\\": 60, \\\"CAR\\\": 24}]}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_early_signal_s1_l1_20k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"CAR\\\": 56, \\\"TSR\\\": 51, \\\"frozen_ee\\\": 0, \\\"per_task_CAR\\\": {\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": 62, \\\"task1\\\": 76, \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": 66, \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": 20}, \\\"per_task_TSR\\\": {\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": 20, \\\"task1\\\": 82, \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": 42, \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": 60}}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_early_signal_s0_l1_20k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"overall_CAR\\\": 0.55, \\\"overall_TSR\\\": 0.54, \\\"frozen_ee_pct\\\": 0, \\\"per_task\\\": [{\\\"task\\\": \\\"orange_juice\\\", \\\"CAR\\\": 0.5, \\\"TSR\\\": 0.38, \\\"avg_max_disp\\\": 0.0467, \\\"avg_max_ee_disp\\\": 0.3917}, {\\\"task\\\": \\\"chocolate_pudding\\\", \\\"CAR\\\": 0.72, \\\"TSR\\\": 0.74, \\\"avg_max_disp\\\": 0.0487, \\\"avg_max_ee_disp\\\": 0.4044}, {\\\"task\\\": \\\"milk\\\", \\\"CAR\\\": 0.72, \\\"TSR\\\": 0.44, \\\"avg_max_disp\\\": 0.0319, \\\"avg_max_ee_disp\\\": 0.3492}, {\\\"task\\\": \\\"bbq_sauce\\\", \\\"CAR\\\": 0.26, \\\"TSR\\\": 0.6, \\\"avg_max_disp\\\": 0.0928, \\\"avg_max_ee_disp\\\": 0.3895}], \\\"hard_constraints\\\": {\\\"TSR_ge_35\\\": true, \\\"frozen_ee_0\\\": true}, \\\"abc_signal\\\": \\\"B\\\", \\\"total_episodes\\\": 200}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"train_pi05_a1_spatial_bowl_s0_l005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss\\\": 0.0137, \\\"final_action_loss\\\": 0.0135, \\\"final_sdf_loss\\\": 0.0327, \\\"final_ee_loss\\\": 0.0068, \\\"best_loss\\\": 0.01063, \\\"best_step\\\": 28000, \\\"total_steps\\\": 30000, \\\"time_per_step\\\": 4.65, \\\"wall_clock_hours\\\": 28.4}}, \\\"analysis_threshold_sensitivity\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"dfCAR_stable_range_mm\\\": \\\"[2, 200]\\\", \\\"n_models\\\": 8, \\\"n_thresholds\\\": 8, \\\"n_active_equals_n_total_at_200mm\\\": true, \\\"max_dfCAR_variation_2_to_200mm\\\": 0, \\\"min_displacement_m\\\": 0.271, \\\"conclusion\\\": \\\"dfCAR perfectly invariant across tau_d in [2, 200] mm for all 8 model-seed combinations; only at 300mm do 1-2 episodes fall below threshold\\\"}}, \\\"reeval_sdf_s2_l005_30k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"TSR\\\": 56, \\\"CAR\\\": 52.5, \\\"avg_max_ee_disp\\\": 0.3858, \\\"frozen_ee\\\": 0, \\\"per_task\\\": {\\\"T0_orange_juice\\\": {\\\"TSR\\\": 34, \\\"CAR\\\": 46, \\\"ee_disp\\\": 0.3923, \\\"obj_disp\\\": 0.0598}, \\\"T1_chocolate_pudding\\\": {\\\"TSR\\\": 82, \\\"CAR\\\": 74, \\\"ee_disp\\\": 0.4098, \\\"obj_disp\\\": 0.046}, \\\"T2_milk\\\": {\\\"TSR\\\": 38, \\\"CAR\\\": 72, \\\"ee_disp\\\": 0.3574, \\\"obj_disp\\\": 0.0406}, \\\"T3_bbq_sauce\\\": {\\\"TSR\\\": 70, \\\"CAR\\\": 18, \\\"ee_disp\\\": 0.3838, \\\"obj_disp\\\": 0.0833}}}}, \\\"reeval_sdf_s2_l01_30k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"TSR\\\": 53.5, \\\"CAR\\\": 54.5, \\\"avg_max_ee_disp\\\": 0.3877, \\\"frozen_ee\\\": 0, \\\"per_task\\\": {\\\"T0_orange_juice\\\": {\\\"TSR\\\": 24, \\\"CAR\\\": 64, \\\"ee_disp\\\": 0.3822, \\\"obj_disp\\\": 0.0385}, \\\"T1_chocolate_pudding\\\": {\\\"TSR\\\": 72, \\\"CAR\\\": 68, \\\"ee_disp\\\": 0.4189, \\\"obj_disp\\\": 0.0517}, \\\"T2_milk\\\": {\\\"TSR\\\": 48, \\\"CAR\\\": 72, \\\"ee_disp\\\": 0.3567, \\\"obj_disp\\\": 0.0258}, \\\"T3_bbq_sauce\\\": {\\\"TSR\\\": 70, \\\"CAR\\\": 14, \\\"ee_disp\\\": 0.3931, \\\"obj_disp\\\": 0.0861}}}}, \\\"reeval_sdf_s1_l01_30k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"TSR\\\": 55.5, \\\"CAR\\\": 57.5, \\\"avg_max_ee_disp\\\": 0.3852, \\\"frozen_ee\\\": 0, \\\"per_task\\\": {\\\"T0_orange_juice\\\": {\\\"TSR\\\": 22, \\\"CAR\\\": 60, \\\"ee_disp\\\": 0.3892, \\\"obj_disp\\\": 0.0536}, \\\"T1_chocolate_pudding\\\": {\\\"TSR\\\": 80, \\\"CAR\\\": 76, \\\"ee_disp\\\": 0.4073, \\\"obj_disp\\\": 0.0472}, \\\"T2_milk\\\": {\\\"TSR\\\": 54, \\\"CAR\\\": 72, \\\"ee_disp\\\": 0.3552, \\\"obj_disp\\\": 0.0387}, \\\"T3_bbq_sauce\\\": {\\\"TSR\\\": 66, \\\"CAR\\\": 22, \\\"ee_disp\\\": 0.3892, \\\"obj_disp\\\": 0.0916}}}}, \\\"reeval_sdf_s1_l005_30k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"TSR\\\": 50.5, \\\"CAR\\\": 54, \\\"avg_max_ee_disp\\\": 0.3883, \\\"frozen_ee\\\": 0, \\\"per_task\\\": {\\\"T0_orange_juice\\\": {\\\"TSR\\\": 28, \\\"CAR\\\": 64, \\\"ee_disp\\\": 0.3816, \\\"obj_disp\\\": 0.0349}, \\\"T1_chocolate_pudding\\\": {\\\"TSR\\\": 72, \\\"CAR\\\": 70, \\\"ee_disp\\\": 0.4206, \\\"obj_disp\\\": 0.0491}, \\\"T2_milk\\\": {\\\"TSR\\\": 30, \\\"CAR\\\": 68, \\\"ee_disp\\\": 0.3588, \\\"obj_disp\\\": 0.0328}, \\\"T3_bbq_sauce\\\": {\\\"TSR\\\": 72, \\\"CAR\\\": 14, \\\"ee_disp\\\": 0.3924, \\\"obj_disp\\\": 0.0931}}}}, \\\"eval_lora_baseline_30k_s0_reeval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"TSR\\\": 51.5, \\\"CAR\\\": 56.5, \\\"avg_max_ee_disp\\\": 0.3957, \\\"frozen_ee\\\": 0, \\\"per_task\\\": {\\\"orange_juice\\\": {\\\"TSR\\\": 32, \\\"CAR\\\": 56}, \\\"chocolate_pudding\\\": {\\\"TSR\\\": 74, \\\"CAR\\\": 74}, \\\"milk\\\": {\\\"TSR\\\": 42, \\\"CAR\\\": 70}, \\\"bbq_sauce\\\": {\\\"TSR\\\": 58, \\\"CAR\\\": 26}}}}, \\\"reeval_sdf_s0_l005_30k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"tsr\\\": 55.5, \\\"car\\\": 57, \\\"frozen_rate_ee\\\": 0, \\\"fake_safe_rate_ee\\\": 0, \\\"per_task\\\": {\\\"orange_juice\\\": {\\\"tsr\\\": 38, \\\"car\\\": 52}, \\\"chocolate_pudding\\\": {\\\"tsr\\\": 80, \\\"car\\\": 74}, \\\"milk\\\": {\\\"tsr\\\": 38, \\\"car\\\": 74}, \\\"bbq_sauce\\\": {\\\"tsr\\\": 66, \\\"car\\\": 28}}}}, \\\"eval_phase2_lambda0_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"per_task\\\": [{\\\"task_id\\\": 0, \\\"task_name\\\": \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\", \\\"TSR\\\": 30, \\\"CAR\\\": 56, \\\"mean_max_ee_disp\\\": 0.3837, \\\"frozen_rate\\\": 0}, {\\\"task_id\\\": 1, \\\"task_name\\\": \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\", \\\"TSR\\\": 76, \\\"CAR\\\": 74, \\\"mean_max_ee_disp\\\": 0.4059, \\\"frozen_rate\\\": 0}, {\\\"task_id\\\": 2, \\\"task_name\\\": \\\"pick_up_the_milk_and_place_it_in_the_basket\\\", \\\"TSR\\\": 42, \\\"CAR\\\": 74, \\\"mean_max_ee_disp\\\": 0.3565, \\\"frozen_rate\\\": 0}, {\\\"task_id\\\": 3, \\\"task_name\\\": \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\", \\\"TSR\\\": 66, \\\"CAR\\\": 26, \\\"mean_max_ee_disp\\\": 0.3903, \\\"frozen_rate\\\": 0}], \\\"mean\\\": {\\\"TSR\\\": 53.5, \\\"CAR\\\": 57.5, \\\"mean_max_ee_disp\\\": 0.3841, \\\"frozen_rate\\\": 0}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"train_pi05_phase2_lambda0_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss_action\\\": 0.0113, \\\"final_loss_sdf\\\": 0.1369, \\\"final_loss_ee\\\": 0.0079, \\\"best_loss\\\": 0.00651, \\\"best_step\\\": 4000, \\\"total_steps\\\": 10000, \\\"time_per_step\\\": 4.64, \\\"wall_clock_hours\\\": 12.88}}, \\\"reeval_lora_s1_30k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"tsr\\\": 51.5, \\\"car\\\": 52.5, \\\"ee_disp\\\": 0.3882, \\\"frozen_rate_ee\\\": 0, \\\"fake_safe_rate_ee\\\": 0, \\\"per_task\\\": {\\\"orange_juice\\\": {\\\"tsr\\\": 34, \\\"car\\\": 54}, \\\"chocolate_pudding\\\": {\\\"tsr\\\": 62, \\\"car\\\": 68}, \\\"milk\\\": {\\\"tsr\\\": 50, \\\"car\\\": 72}, \\\"bbq_sauce\\\": {\\\"tsr\\\": 60, \\\"car\\\": 16}}}}, \\\"reeval_sdf_s0_l01_30k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"tsr\\\": 52.5, \\\"car\\\": 57, \\\"ee_disp\\\": 0.3946, \\\"frozen_rate_ee\\\": 0, \\\"frozen_rate_obs\\\": 55.5, \\\"fake_safe_rate_ee\\\": 0, \\\"obstacle_disp\\\": 0.0577, \\\"ee_disp_range\\\": [0.312, 0.865], \\\"per_task\\\": {\\\"orange_juice\\\": {\\\"tsr\\\": 28, \\\"car\\\": 48}, \\\"chocolate_pudding\\\": {\\\"tsr\\\": 78, \\\"car\\\": 74}, \\\"milk\\\": {\\\"tsr\\\": 44, \\\"car\\\": 72}, \\\"bbq_sauce\\\": {\\\"tsr\\\": 60, \\\"car\\\": 34}}, \\\"note\\\": \\\"frozen_rate_ee = EE disp < 0.1mm (paper definition); frozen_rate_obs = obstacle disp < 0.1mm (analyzer script definition, NOT paper definition)\\\"}}, \\\"eval_pi05_baseline_reeval_disp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_lora_baseline_30k_s0_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 8.5, \\\"avg_CAR\\\": 54.5, \\\"n_episodes\\\": 200, \\\"frozen_pct\\\": 0, \\\"avg_ee_disp\\\": 0.4887, \\\"dfCAR_100mm\\\": 54.5, \\\"per_task\\\": [{\\\"task\\\": \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\", \\\"safety\\\": \\\"II\\\", \\\"n\\\": 50, \\\"TSR\\\": 0, \\\"CAR\\\": 62, \\\"avg_ee_disp\\\": 0.497, \\\"median_ee_disp\\\": 0.4208, \\\"frozen_pct\\\": 0}, {\\\"task\\\": \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\", \\\"safety\\\": \\\"II\\\", \\\"n\\\": 50, \\\"TSR\\\": 34, \\\"CAR\\\": 44, \\\"avg_ee_disp\\\": 0.5041, \\\"median_ee_disp\\\": 0.4251, \\\"frozen_pct\\\": 0}, {\\\"task\\\": \\\"pick_up_the_milk_and_place_it_in_the_basket\\\", \\\"safety\\\": \\\"II\\\", \\\"n\\\": 50, \\\"TSR\\\": 0, \\\"CAR\\\": 94, \\\"avg_ee_disp\\\": 0.5765, \\\"median_ee_disp\\\": 0.5511, \\\"frozen_pct\\\": 0}, {\\\"task\\\": \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\", \\\"safety\\\": \\\"II\\\", \\\"n\\\": 50, \\\"TSR\\\": 0, \\\"CAR\\\": 18, \\\"avg_ee_disp\\\": 0.3772, \\\"median_ee_disp\\\": 0.3712, \\\"frozen_pct\\\": 0}]}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_lora_baseline_30k_s1_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 4, \\\"avg_CAR\\\": 56, \\\"dfCAR_100mm\\\": 56, \\\"avg_ee_disp\\\": 0.4669, \\\"frozen_pct\\\": 0, \\\"n_episodes\\\": 200, \\\"per_task\\\": {\\\"pick_up_the_orange_juice\\\": {\\\"TSR\\\": 2, \\\"CAR\\\": 58, \\\"ee_disp_mean\\\": 0.4827, \\\"ee_disp_median\\\": 0.4011, \\\"frozen_pct\\\": 0}, \\\"pick_up_the_chocolate_pudding\\\": {\\\"TSR\\\": 14, \\\"CAR\\\": 50, \\\"ee_disp_mean\\\": 0.538, \\\"ee_disp_median\\\": 0.4548, \\\"frozen_pct\\\": 0}, \\\"pick_up_the_milk\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 90, \\\"ee_disp_mean\\\": 0.4817, \\\"ee_disp_median\\\": 0.512, \\\"frozen_pct\\\": 0}, \\\"pick_up_the_bbq_sauce\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 26, \\\"ee_disp_mean\\\": 0.3653, \\\"ee_disp_median\\\": 0.3335, \\\"frozen_pct\\\": 0}}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_lora_baseline_30k_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_lora_baseline_30k_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"train_pi05_lora_baseline_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss\\\": 0.01408, \\\"best_loss\\\": 0.0113, \\\"best_step\\\": 14000, \\\"total_steps\\\": 30000, \\\"grad_norm\\\": 0.10628, \\\"time_per_step\\\": 4.62}}, \\\"train_pi05_lora_baseline_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss\\\": 0.01343, \\\"best_loss\\\": 0.01025, \\\"best_step\\\": 24000, \\\"total_steps\\\": 30000, \\\"grad_norm\\\": 0.10538, \\\"time_per_step\\\": 4.613}}, \\\"eval_pi05_a1_30k_s0_l01_disp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 6.5, \\\"avg_CAR\\\": 52.5, \\\"n_episodes\\\": 200, \\\"avg_max_ee_displacement\\\": 0.4725, \\\"task0_TSR\\\": 0, \\\"task0_CAR\\\": 76, \\\"task0_ee_disp\\\": 0.4781, \\\"task0_safe_ee_disp\\\": 0.4627, \\\"task1_TSR\\\": 26, \\\"task1_CAR\\\": 32, \\\"task1_ee_disp\\\": 0.5387, \\\"task1_safe_ee_disp\\\": 0.4446, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 84, \\\"task2_ee_disp\\\": 0.5169, \\\"task2_safe_ee_disp\\\": 0.5273, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 18, \\\"task3_ee_disp\\\": 0.3561, \\\"task3_safe_ee_disp\\\": 0.3764, \\\"fake_safe_pct\\\": 0, \\\"real_safety\\\": true, \\\"frozen\\\": false}}, \\\"eval_pi05_a1_30k_s1_l005_disp\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 4, \\\"avg_CAR\\\": 54, \\\"n_episodes\\\": 200, \\\"avg_max_ee_displacement\\\": 0.4955, \\\"task0_TSR\\\": 2, \\\"task0_CAR\\\": 54, \\\"task0_ee_disp\\\": 0.5062, \\\"task0_safe_ee_disp\\\": 0.4247, \\\"task1_TSR\\\": 14, \\\"task1_CAR\\\": 58, \\\"task1_ee_disp\\\": 0.4991, \\\"task1_safe_ee_disp\\\": 0.5006, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 92, \\\"task2_ee_disp\\\": 0.6088, \\\"task2_safe_ee_disp\\\": 0.6213, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 12, \\\"task3_ee_disp\\\": 0.368, \\\"task3_safe_ee_disp\\\": 0.3628, \\\"fake_safe_pct\\\": 0, \\\"real_safety\\\": true, \\\"frozen\\\": false}}, \\\"eval_pi05_a1_best_s2_l005_10k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 9, \\\"avg_CAR\\\": 55.5, \\\"n_episodes\\\": 200, \\\"avg_max_ee_displacement\\\": 0.5046, \\\"task0_TSR\\\": 0, \\\"task0_CAR\\\": 68, \\\"task0_ee_disp\\\": 0.5256, \\\"task0_safe_ee_disp\\\": 0.4979, \\\"task1_TSR\\\": 36, \\\"task1_CAR\\\": 44, \\\"task1_ee_disp\\\": 0.5288, \\\"task1_safe_ee_disp\\\": 0.5115, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 92, \\\"task2_ee_disp\\\": 0.5779, \\\"task2_safe_ee_disp\\\": 0.5883, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 18, \\\"task3_ee_disp\\\": 0.3863, \\\"task3_safe_ee_disp\\\": 0.3609, \\\"fake_safe_pct\\\": 0, \\\"task2_fake_safety\\\": false, \\\"real_safety\\\": true, \\\"task0_obs_frozen_pct\\\": 0.7, \\\"task2_obs_frozen_pct\\\": 0.92, \\\"analysis\\\": \\\"ALL episodes have high EE displacement (0.39-0.58m). Zero fake safety. 10K best shows genuine collision avoidance: robot moves normally and avoids obstacles. Task 2 high CAR (92%) is REAL avoidance not action collapse.\\\"}}, \\\"eval_pi05_a1_best_s1_l005_16k\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 6.5, \\\"avg_CAR\\\": 53, \\\"n_episodes\\\": 200, \\\"task0_TSR\\\": 4, \\\"task0_CAR\\\": 58, \\\"task0_ee_disp\\\": 0.5179, \\\"task0_max_disp\\\": 0.0416, \\\"task1_TSR\\\": 22, \\\"task1_CAR\\\": 50, \\\"task1_ee_disp\\\": 0.5146, \\\"task1_max_disp\\\": 0.1018, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 88, \\\"task2_ee_disp\\\": 0.6475, \\\"task2_max_disp\\\": 0.0073, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 16, \\\"task3_ee_disp\\\": 0.3707, \\\"task3_max_disp\\\": 0.0934, \\\"fake_safe_pct\\\": 0, \\\"real_safety\\\": true}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_a1_30k_s1_l01_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 7.5, \\\"avg_CAR\\\": 52.5, \\\"n_episodes\\\": 200, \\\"task0_TSR\\\": 4, \\\"task0_CAR\\\": 54, \\\"task1_TSR\\\": 26, \\\"task1_CAR\\\": 48, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 94, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 14}}, \\\"eval_pi05_a1_30k_s1_l005_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 5.5, \\\"avg_CAR\\\": 52.5, \\\"n_episodes\\\": 200, \\\"task0_TSR\\\": 4, \\\"task0_CAR\\\": 58, \\\"task1_TSR\\\": 18, \\\"task1_CAR\\\": 40, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 94, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 18}}, \\\"eval_pi05_a1_30k_s2_l005_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 9.5, \\\"avg_CAR\\\": 54.5, \\\"n_episodes\\\": 200, \\\"task0_TSR\\\": 2, \\\"task0_CAR\\\": 62, \\\"task1_TSR\\\": 36, \\\"task1_CAR\\\": 44, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 90, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 22}}, \\\"eval_pi05_a1_30k_s1_l005_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 4, \\\"avg_CAR\\\": 51.5, \\\"n_episodes\\\": 200, \\\"task0_TSR\\\": 0, \\\"task0_CAR\\\": 54, \\\"task1_TSR\\\": 16, \\\"task1_CAR\\\": 48, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 88, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 16, \\\"source\\\": \\\"v4 JSON with per-episode displacement\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_a1_30k_s2_l005_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 9, \\\"avg_CAR\\\": 53, \\\"n_episodes\\\": 200, \\\"task0_TSR\\\": 4, \\\"task0_CAR\\\": 60, \\\"task1_TSR\\\": 32, \\\"task1_CAR\\\": 46, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 86, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 20, \\\"source\\\": \\\"v4 JSON with per-episode displacement\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_pi05_a1_30k_s2_l01_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 7.5, \\\"avg_CAR\\\": 53, \\\"n_episodes\\\": 200, \\\"task0_TSR\\\": 0, \\\"task0_CAR\\\": 62, \\\"task1_TSR\\\": 30, \\\"task1_CAR\\\": 42, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 88, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 20, \\\"source\\\": \\\"v3 JSON with per-episode displacement\\\"}}, \\\"eval_pi05_a1_30k_s0_l01\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 5.5, \\\"avg_CAR\\\": 53, \\\"n_episodes\\\": 200, \\\"task0_TSR\\\": 2, \\\"task0_CAR\\\": 68, \\\"task1_TSR\\\": 20, \\\"task1_CAR\\\": 46, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 86, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 12, \\\"task0_disp\\\": 0.0297, \\\"task1_disp\\\": 0.0815, \\\"task2_disp\\\": 0.0112, \\\"task3_disp\\\": 0.0797, \\\"note\\\": \\\"旧版脚本，无max_ee_displacement字段\\\"}}, \\\"eval_pi05_a1_30k_s0_l005_r4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 7.5, \\\"avg_CAR\\\": 47, \\\"n_episodes\\\": 200, \\\"task0_TSR\\\": 6, \\\"task0_CAR\\\": 58, \\\"task1_TSR\\\": 24, \\\"task1_CAR\\\": 38, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 76, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 16, \\\"task0_disp\\\": 0.0485, \\\"task1_disp\\\": 0.0782, \\\"task2_disp\\\": 0.0147, \\\"task3_disp\\\": 0.1009, \\\"note\\\": \\\"旧版脚本，无max_ee_displacement字段\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"train_pi05_phase2_lambda0_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_a1_30k_s0_l005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 5.5, \\\"avg_CAR\\\": 50, \\\"n_episodes\\\": 200, \\\"task0_TSR\\\": 2, \\\"task0_CAR\\\": 58, \\\"task1_TSR\\\": 20, \\\"task1_CAR\\\": 42, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 86, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 14, \\\"task0_disp\\\": 0.0433, \\\"task1_disp\\\": 0.1055, \\\"task2_disp\\\": 0.0147, \\\"task3_disp\\\": 0.0879}}, \\\"train_pi05_a1_obj_s0_l01\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_loss\\\": 0.00801, \\\"steps_completed\\\": 30000}}, \\\"train_pi05_a1_obj_s0_l005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_loss\\\": 0.007860926911234856, \\\"best_loss_step\\\": 26000, \\\"steps_completed\\\": 30000}}, \\\"eval_pi05_a1_30k_s2_l01\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_a1_30k_s2_l005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_a1_30k_s1_l01\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_a1_30k_s1_l005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"train_pi05_a1_obj_s2_l01\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_loss\\\": 0.00911, \\\"best_loss_step\\\": 10000, \\\"steps_completed\\\": 30000}}, \\\"train_pi05_a1_obj_s2_l005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_loss\\\": 0.00874, \\\"best_loss_step\\\": 10000, \\\"steps_completed\\\": 30000}}, \\\"train_pi05_a1_obj_s1_l01\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_loss\\\": 0.01168, \\\"best_loss_step\\\": 16000, \\\"steps_completed\\\": 30000}}, \\\"train_pi05_a1_obj_s1_l005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_loss\\\": 0.01143, \\\"best_loss_step\\\": 16000, \\\"steps_completed\\\": 30000}}, \\\"train_pi05_a1_obj_l01\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"train_pi05_a1_obj_l005\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_pi05_safelibero_object_v11_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"TSR\\\": 0.75, \\\"CAR\\\": 0.275, \\\"mean_displacement\\\": 0.132}}, \\\"eval_pi05_safelibero_object_v11_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"TSR\\\": 0.76, \\\"CAR\\\": 0.25, \\\"mean_displacement\\\": 0.153}}, \\\"eval_pi05_safelibero_spatial_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_TSR\\\": 0.575, \\\"overall_CAR\\\": 0.13, \\\"task3_CAR\\\": 0.52, \\\"n_episodes\\\": 200}}, \\\"eval_pi05_safelibero_object_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"overall_TSR\\\": 0.73, \\\"overall_CAR\\\": 0.28, \\\"overall_avg_disp\\\": 0.1508, \\\"real_safe_rate\\\": 0.005, \\\"fake_safe_rate\\\": 0.982, \\\"task0_TSR\\\": 0.64, \\\"task0_CAR\\\": 0.06, \\\"task1_TSR\\\": 0.86, \\\"task1_CAR\\\": 0.56, \\\"task2_TSR\\\": 0.66, \\\"task2_CAR\\\": 0.16, \\\"task3_TSR\\\": 0.76, \\\"task3_CAR\\\": 0.34, \\\"n_episodes\\\": 200}}, \\\"eval_a3_spatial_force_refine_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_a3_spatial_m024fix_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"oracle_true_gt_feature_object_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_a1_lora_object_v11_rerun\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 0, \\\"avg_CAR\\\": 91.5, \\\"n_episodes\\\": 800, \\\"eps_per_task\\\": 200, \\\"task_TSR\\\": {\\\"orange_juice\\\": 0, \\\"chocolate_pudding\\\": 0, \\\"milk\\\": 0, \\\"bbq_sauce\\\": 0}, \\\"task_CAR\\\": {\\\"orange_juice\\\": 96, \\\"chocolate_pudding\\\": 82, \\\"milk\\\": 97, \\\"bbq_sauce\\\": 91}, \\\"fake_safe_rate\\\": 0.996, \\\"fake_safe_detail\\\": \\\"729/732 safe episodes have displacement<0.1mm\\\", \\\"real_safe_count\\\": 3, \\\"real_safe_rate\\\": 0.004, \\\"safe_disp_distribution\\\": {\\\"<1um\\\": 541, \\\"1um-0.1mm\\\": 188, \\\"0.1-1mm\\\": 3, \\\">1mm\\\": 0}, \\\"task_fake_safe\\\": {\\\"orange_juice\\\": \\\"192/192 (100%)\\\", \\\"chocolate_pudding\\\": \\\"162/164 (98.8%)\\\", \\\"milk\\\": \\\"194/194 (100%)\\\", \\\"bbq_sauce\\\": \\\"181/182 (99.5%)\\\"}, \\\"task_avg_disp_mm\\\": {\\\"orange_juice\\\": 0.871, \\\"chocolate_pudding\\\": 7.491, \\\"milk\\\": 2.508, \\\"bbq_sauce\\\": 4.75}, \\\"task_safe_disp_mean_mm\\\": {\\\"orange_juice\\\": 0.000315, \\\"chocolate_pudding\\\": 0.007588, \\\"milk\\\": 0.000288, \\\"bbq_sauce\\\": 0.001293}, \\\"collision_eps\\\": 68, \\\"collision_disp_mean_mm\\\": 45.92, \\\"collision_disp_max_mm\\\": 286.53, \\\"baseline_comparison\\\": {\\\"baseline_CAR\\\": 83, \\\"baseline_fake_safe\\\": \\\"165/166 (99.4%)\\\", \\\"baseline_real_safe\\\": \\\"1/200 (0.5%)\\\", \\\"baseline_n_episodes\\\": 200}}}, \\\"oracle_true_gt_feature_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 0, \\\"avg_CAR\\\": 76.9, \\\"task_CAR\\\": {\\\"orange_juice\\\": 90, \\\"chocolate_pudding\\\": 47.5, \\\"milk\\\": 82.5, \\\"bbq_sauce\\\": 87.5}, \\\"task_displacement\\\": {\\\"orange_juice\\\": 0.0023, \\\"chocolate_pudding\\\": 0.0473, \\\"milk\\\": 0.0086, \\\"bbq_sauce\\\": 0.0097}, \\\"task_refine_count_mean\\\": {\\\"orange_juice\\\": 248.5, \\\"chocolate_pudding\\\": 241.8, \\\"milk\\\": 236.7, \\\"bbq_sauce\\\": 240}, \\\"task_grad_mag_mean\\\": {\\\"orange_juice\\\": 0.00423, \\\"chocolate_pudding\\\": 0.00609, \\\"milk\\\": 0.00466, \\\"bbq_sauce\\\": 0.00491}, \\\"fake_safe_rate\\\": 0.967, \\\"fake_safe_detail\\\": \\\"119/123 safe episodes have displacement<0.1mm\\\", \\\"total_refined_steps\\\": 38679, \\\"avg_refined_per_episode\\\": 241.7, \\\"n_episodes\\\": 160}}, \\\"oracle_true_gt_fixed_alpha_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 0, \\\"avg_CAR\\\": 73.1, \\\"task_CAR\\\": {\\\"orange_juice\\\": 85, \\\"chocolate_pudding\\\": 50, \\\"milk\\\": 77.5, \\\"bbq_sauce\\\": 80}, \\\"task_displacement\\\": {\\\"orange_juice\\\": 0.0113, \\\"chocolate_pudding\\\": 0.0365, \\\"milk\\\": 0.0042, \\\"bbq_sauce\\\": 0.0032}, \\\"task_refine_count_mean\\\": {\\\"orange_juice\\\": 8.7, \\\"chocolate_pudding\\\": 20.2, \\\"milk\\\": 20.1, \\\"bbq_sauce\\\": 10.4}, \\\"total_refined_steps\\\": 2375, \\\"avg_refined_per_episode\\\": 14.8, \\\"fake_safe_rate\\\": 0.983, \\\"fake_safe_detail\\\": \\\"115/117 safe episodes have displacement<0.1mm\\\", \\\"task_fake_safe\\\": {\\\"orange_juice\\\": \\\"34/34 (100%)\\\", \\\"chocolate_pudding\\\": \\\"19/20 (95%)\\\", \\\"milk\\\": \\\"30/31 (96.8%)\\\", \\\"bbq_sauce\\\": \\\"32/32 (100%)\\\"}, \\\"collision_threshold\\\": 0.001, \\\"n_episodes\\\": 160}}, \\\"oracle_true_gt_adaptive_alpha_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 0, \\\"avg_CAR\\\": 75, \\\"task_CAR\\\": {\\\"orange_juice\\\": 82.5, \\\"chocolate_pudding\\\": 55, \\\"milk\\\": 77.5, \\\"bbq_sauce\\\": 85}, \\\"task_displacement\\\": {\\\"orange_juice\\\": 0.0076, \\\"chocolate_pudding\\\": 0.0475, \\\"milk\\\": 0.0107, \\\"bbq_sauce\\\": 0.0077}, \\\"task_refine_count_mean\\\": {\\\"orange_juice\\\": 7.6, \\\"chocolate_pudding\\\": 22.4, \\\"milk\\\": 17.6, \\\"bbq_sauce\\\": 9.1}, \\\"task_grad_mag_mean\\\": {\\\"orange_juice\\\": 0.176, \\\"chocolate_pudding\\\": 0.247, \\\"milk\\\": 0.489, \\\"bbq_sauce\\\": 0.357}, \\\"fake_safe_rate\\\": 0.983, \\\"fake_safe_detail\\\": \\\"118/120 safe episodes have displacement<0.1mm\\\", \\\"total_refined_steps\\\": 2270, \\\"avg_refined_per_episode\\\": 14.2, \\\"n_episodes\\\": 160}}, \\\"a3_gradient_spatial_bowl_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_loss\\\": 0.01552, \\\"steps_completed\\\": 30000}}, \\\"oracle_true_gt_object_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"eval_a3_object_m024fix_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"task0\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 0.885, \\\"avg_max_displacement\\\": 0.0066, \\\"refined_count\\\": 0}, \\\"task1\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 0.46, \\\"avg_max_displacement\\\": 0.0492, \\\"refined_count\\\": 0}, \\\"task2\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 0.86, \\\"avg_max_displacement\\\": 0.0044, \\\"refined_count\\\": 0}, \\\"task3\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 0.88, \\\"avg_max_displacement\\\": 0.0074, \\\"refined_count\\\": 0}, \\\"overall\\\": {\\\"avg_TSR\\\": 0, \\\"avg_CAR\\\": 0.771}}}, \\\"eval_a1_lora_spatial_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"avg_TSR\\\": 0.001, \\\"avg_CAR\\\": 0.008, \\\"task0_TSR\\\": 0.005, \\\"task0_CAR\\\": 0.015, \\\"task0_avg_disp\\\": 0.2578, \\\"task1_TSR\\\": 0, \\\"task1_CAR\\\": 0, \\\"task1_avg_disp\\\": 0.1955, \\\"task2_TSR\\\": 0, \\\"task2_CAR\\\": 0, \\\"task2_avg_disp\\\": 0.2142, \\\"task3_TSR\\\": 0, \\\"task3_CAR\\\": 0.015, \\\"task3_avg_disp\\\": 0.1992, \\\"safe_episodes_total\\\": 6, \\\"safe_episodes_with_zero_displacement\\\": 6, \\\"fake_safety\\\": true}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"eval_baseline_fullft_spatial_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"TSR_avg\\\": 0.375, \\\"CAR_avg\\\": 0, \\\"n_episodes\\\": 800, \\\"per_task\\\": {\\\"task0_pick_bowl_between_plate_ramekin\\\": {\\\"TSR\\\": 1.5, \\\"CAR\\\": 0, \\\"avg_max_displacement\\\": 0.3317, \\\"avg_smoothness\\\": 0.003487}, \\\"task1_pick_bowl_on_ramekin\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 0, \\\"avg_max_displacement\\\": 0.2863, \\\"avg_smoothness\\\": 0.00326}, \\\"task2_pick_bowl_on_stove\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 0, \\\"avg_max_displacement\\\": 0.2604, \\\"avg_smoothness\\\": 0.002417}, \\\"task3_pick_bowl_on_cabinet\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 0, \\\"avg_max_displacement\\\": 0.3017, \\\"avg_smoothness\\\": 0.003154}}}}, \\\"oracle_a3_m024fix_object_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"task0_pick_orange_juice\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 97.5, \\\"avg_max_displacement\\\": 0.0028}, \\\"task1_put_wine_on_rack\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 65, \\\"avg_max_displacement\\\": 0.0381}, \\\"task2_put_cream_in_marked_area\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 97.5, \\\"avg_max_displacement\\\": 0}, \\\"task3_pick_bbq_sauce_to_basket\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 82.5, \\\"avg_max_displacement\\\": 0.0134}, \\\"overall\\\": {\\\"TSR_avg\\\": 0, \\\"CAR_avg\\\": 85.6}, \\\"n_episodes\\\": 40, \\\"force_refine\\\": true, \\\"refine_count_per_episode\\\": 300}}, \\\"oracle_a3_force_refine_object_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"TSR_avg\\\": 0, \\\"CAR_avg\\\": 81.2, \\\"n_episodes\\\": 40, \\\"per_task\\\": {\\\"orange_juice\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 95, \\\"avg_max_displacement\\\": 0.0005}, \\\"chocolate_pudding\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 57.5, \\\"avg_max_displacement\\\": 0.046}, \\\"milk\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 92.5, \\\"avg_max_displacement\\\": 0.001}, \\\"bbq_sauce\\\": {\\\"TSR\\\": 0, \\\"CAR\\\": 80, \\\"avg_max_displacement\\\": 0.0018}}, \\\"refined_count_per_episode\\\": 300, \\\"force_refine\\\": true, \\\"refine_alpha\\\": 0.1, \\\"refine_margin\\\": 0.01, \\\"displacement_collapse\\\": \\\"most episodes show max_displacement 1e-6 to 1e-10, gradient near-zero\\\"}, \\\"conclusion\\\": \\\"negative\\\"}, \\\"a1_lora_spatial_bowl_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_loss\\\": 0.01431, \\\"steps_completed\\\": 30000}}, \\\"eval_a1_lora_object_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"metrics\\\": {\\\"TSR\\\": 0, \\\"CAR_avg\\\": 90, \\\"CAR_task0\\\": 96, \\\"CAR_task1\\\": 80, \\\"CAR_task2\\\": 94, \\\"CAR_task3\\\": 90, \\\"displacement_avg\\\": 0.0027, \\\"displacement_task0\\\": 0.0017, \\\"displacement_task1\\\": 0.0076, \\\"displacement_task2\\\": 0.0008, \\\"displacement_task3\\\": 0.0008, \\\"n_episodes\\\": 200}, \\\"conclusion\\\": \\\"success\\\"}, \\\"eval_lora_baseline_object_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"TSR\\\": 0, \\\"CAR_avg\\\": 82, \\\"CAR_task0\\\": 96, \\\"CAR_task1\\\": 46, \\\"CAR_task2\\\": 98, \\\"CAR_task3\\\": 88, \\\"displacement_avg\\\": 0.01, \\\"displacement_task0\\\": 0.0072, \\\"displacement_task1\\\": 0.0257, \\\"displacement_task2\\\": 1e-05, \\\"displacement_task3\\\": 0.007, \\\"n_episodes\\\": 200}}, \\\"eval_lora_baseline_spatial_v11\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"TSR\\\": 0, \\\"CAR_avg\\\": 0, \\\"CAR_task0\\\": 0, \\\"CAR_task1\\\": 0, \\\"CAR_task2\\\": 0, \\\"CAR_task3\\\": 0, \\\"displacement_avg\\\": 0.23, \\\"displacement_task0\\\": 0.2669, \\\"displacement_task1\\\": 0.206, \\\"displacement_task2\\\": 0.2212, \\\"displacement_task3\\\": 0.2328, \\\"n_episodes\\\": 200}}, \\\"eval_a3_v11_object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"TSR\\\": 0, \\\"CAR_avg\\\": 74.5, \\\"CAR_task0\\\": 84, \\\"CAR_task1\\\": 48, \\\"CAR_task2\\\": 82, \\\"CAR_task3\\\": 84, \\\"displacement_avg\\\": 0.0164, \\\"displacement_task0\\\": 0.0149, \\\"displacement_task1\\\": 0.0388, \\\"displacement_task2\\\": 0.0079, \\\"displacement_task3\\\": 0.0041, \\\"refined_count_total\\\": 0, \\\"n_episodes\\\": 200}}, \\\"a1_lora_object_pudding_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_loss\\\": 0.01326, \\\"final_loss\\\": 0.0184, \\\"steps_completed\\\": 30000, \\\"wall_time_hours\\\": 33}}, \\\"eval_baseline_v11_object\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"TSR\\\": 0.5, \\\"CAR_avg\\\": 83, \\\"CAR_task0\\\": 76, \\\"CAR_task1\\\": 90, \\\"CAR_task2\\\": 88, \\\"CAR_task3\\\": 78, \\\"TSR_task0\\\": 0, \\\"TSR_task1\\\": 2, \\\"TSR_task2\\\": 0, \\\"TSR_task3\\\": 0, \\\"displacement_avg\\\": 0.0271, \\\"displacement_task0\\\": 0.038, \\\"displacement_task1\\\": 0.0103, \\\"displacement_task2\\\": 0.0163, \\\"displacement_task3\\\": 0.0438, \\\"smoothness_avg\\\": 0.002109, \\\"n_episodes\\\": 200}}, \\\"baseline_lora_object_pudding_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_loss\\\": 0.0124, \\\"steps_completed\\\": 30000}}, \\\"baseline_lora_spatial_bowl_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"best_loss\\\": 0.00876, \\\"steps_completed\\\": 30000}}, \\\"eval_a3_v10a_refine\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"negative\\\", \\\"metrics\\\": {\\\"TSR\\\": 0, \\\"CAR_avg\\\": 79.5, \\\"CAR_task0\\\": 90, \\\"CAR_task1\\\": 88, \\\"CAR_task2\\\": 64, \\\"CAR_task3\\\": 76, \\\"displacement_avg\\\": 0.0112, \\\"displacement_task0\\\": 0.0009, \\\"displacement_task1\\\": 0.0108, \\\"displacement_task2\\\": 0.0168, \\\"displacement_task3\\\": 0.0162, \\\"refined_count\\\": 0, \\\"n_episodes\\\": 200}}, \\\"eval_a3_object_pudding_no_refine\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"eval_a3_object_pudding_refine\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"TSR\\\": 0, \\\"CAR_task0_orange_juice\\\": 96, \\\"CAR_task1_chocolate_pudding\\\": 22, \\\"CAR_task2_milk\\\": 66, \\\"CAR_task3_bbq_sauce\\\": 42, \\\"CAR_avg\\\": 56.5, \\\"TSR_task0\\\": 0, \\\"TSR_task1\\\": 0, \\\"TSR_task2\\\": 0, \\\"TSR_task3\\\": 0, \\\"n_episodes\\\": 50, \\\"refine_count_all_zero\\\": true}}, \\\"a3_gradient_object_pudding_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"action_loss\\\": 0.01546, \\\"total_loss\\\": 0.01898, \\\"final_loss\\\": 0.01898, \\\"best_loss\\\": 0.01439, \\\"ee_loss\\\": 0.01213, \\\"eikonal\\\": 0, \\\"grad_norm\\\": 0.24129, \\\"n_refine\\\": 2.64, \\\"steps_completed\\\": 30000}}, \\\"baseline_spatial_bowl_s0_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss\\\": 0.0032, \\\"best_loss\\\": 0.00316, \\\"steps_completed\\\": 30000, \\\"lr_final\\\": 2.5e-06, \\\"wall_time_hours\\\": 16.1, \\\"vram_mib\\\": 35738, \\\"checkpoint_step\\\": 30000, \\\"avg_it_per_sec\\\": 3.62}}, \\\"baseline_object_pudding_s0_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"final_loss\\\": 0.005, \\\"steps_completed\\\": 30000, \\\"lr_final\\\": 2.5e-06, \\\"wall_time_hours\\\": 14, \\\"vram_mib\\\": 35738}}, \\\"a1_sdf_spatial_bowl_s0_v3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"a1_sdf_object_pudding_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"baseline_spatial_bowl_s1_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"a1_sdf_spatial_bowl_s0_v2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"a1_sdf_spatial_bowl_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"baseline_spatial_bowl_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"baseline_spatial_bowl_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"baseline_object_pudding_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"failed\\\"}}, \\\"count\\\": 123, \\\"total\\\": 123, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.579}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_multiseed_sdf_l01_s0_eseed256\": {\"status\": \"PREPARING\"}, \"eval_multiseed_sdf_l01_s0_eseed123\": {\"status\": \"PREPARING\"}, \"eval_multiseed_sdf_l01_s0_eseed42\": {\"status\": \"PREPARING\"}, \"eval_multiseed_lora_s0_eseed123\": {\"status\": \"PREPARING\"}, \"eval_multiseed_lora_s0_eseed42\": {\"status\": \"PREPARING\"}, \"eval_pi05_a1_30k_s2_l01_high\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"car\": 54.5, \"tsr\": 54.5, \"per_task_car\": {\"orange_juice\": 56, \"chocolate_pudding\": 76, \"milk\": 70, \"bbq_sauce\": 16}, \"per_task_tsr\": {\"orange_juice\": 30, \"chocolate_pudding\": 72, \"milk\": 48, \"bbq_sauce\": 68}, \"scenario\": \"B\"}}, \"train_pi05_a1_obj_s2_l01_high\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.0104, \"final_action_loss\": 0.0069, \"final_sdf_loss\": 0.0336, \"final_ee_loss\": 0.0096, \"best_loss\": 0.0104, \"best_step\": 30000, \"total_steps\": 30000, \"training_hours\": 33.86}}, \"eval_spatial_bowl_lora_ctrl_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 0.5, \"avg_CAR\": 0.155, \"task0_TSR\": 0.66, \"task0_CAR\": 0, \"task1_TSR\": 0.36, \"task1_CAR\": 0.14, \"task2_TSR\": 0.6, \"task2_CAR\": 0.04, \"task3_TSR\": 0.38, \"task3_CAR\": 0.44}}, \"eval_pi05_a1_best_s0_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 0.52, \"avg_CAR\": 0.545, \"task0_TSR\": 0.28, \"task0_CAR\": 0.5, \"task1_TSR\": 0.7, \"task1_CAR\": 0.74, \"task2_TSR\": 0.52, \"task2_CAR\": 0.68, \"task3_TSR\": 0.58, \"task3_CAR\": 0.26, \"n_episodes\": 50, \"seed\": 7, \"collision_threshold\": 0.001}}, \"train_phase2_lambda0_extra_seed\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_spatial_bowl_lora_control_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_lora_s2_30k_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_TSR\": 0.515, \"overall_CAR\": 0.55, \"task0_orange_juice\": {\"TSR\": 0.24, \"CAR\": 0.56}, \"task1_chocolate_pudding\": {\"TSR\": 0.76, \"CAR\": 0.76}, \"task2_milk\": {\"TSR\": 0.42, \"CAR\": 0.62}, \"task3_bbq_sauce\": {\"TSR\": 0.64, \"CAR\": 0.26}}, \"conclusion\": \"success\"}, \"train_phase2_lambda0_s2_v4\": {\"status\": \"RUNNING\"}, \"train_phase2_lambda0_extra_seed_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_phase2_lambda0_s2_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_phase2_lambda0_extra_seed_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_lora_baseline_30k_s2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_spatial_bowl_sdf_s0_l005_30k\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 0.53, \"avg_CAR\": 0.17, \"task0_TSR\": 0.62, \"task0_CAR\": 0, \"task1_TSR\": 0.34, \"task1_CAR\": 0.14, \"task2_TSR\": 0.66, \"task2_CAR\": 0, \"task3_TSR\": 0.5, \"task3_CAR\": 0.54}}, \"train_pi05_lora_baseline_s2_resume\": {\"status\": \"DONE\", \"metrics\": {\"final_loss\": 0.0117, \"final_lr\": 2.5e-06, \"total_steps\": 30000, \"training_time_h\": 10.31}, \"conclusion\": \"success\"}, \"train_phase2_lambda0_s2_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_a1_30k_s1_l01_high\": {\"status\": \"DONE\", \"metrics\": {\"CAR\": 0.585, \"TSR\": 0.49, \"frozen_rate\": 0, \"dfCAR\": 0.585, \"avg_max_ee_displacement\": 0.3884, \"avg_max_obstacle_displacement\": 0.0553, \"per_task\": {\"orange_juice\": {\"TSR\": 0.26, \"CAR\": 0.66, \"avg_max_ee_displacement\": 0.3882, \"avg_max_obstacle_displacement\": 0.0333}, \"chocolate_pudding\": {\"TSR\": 0.8, \"CAR\": 0.72, \"avg_max_ee_displacement\": 0.4057, \"avg_max_obstacle_displacement\": 0.0545}, \"milk\": {\"TSR\": 0.28, \"CAR\": 0.7, \"avg_max_ee_displacement\": 0.3551, \"avg_max_obstacle_displacement\": 0.0408}, \"bbq_sauce\": {\"TSR\": 0.62, \"CAR\": 0.26, \"avg_max_ee_displacement\": 0.4045, \"avg_max_obstacle_displacement\": 0.0927}}}, \"conclusion\": \"success\"}, \"reeval_lora_s0_30k_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"CAR\": 57, \"TSR\": 46, \"per_task\": {\"orange_juice\": 68, \"chocolate_pudding\": 74, \"milk\": 66, \"bbq_sauce\": 20}}}, \"eval_pi05_a1_30k_s0_l01_high\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"CAR\": 58, \"TSR\": 47, \"frozen_rate\": 0, \"avg_max_ee_displacement\": 0.4, \"dfCAR\": 58}}, \"train_pi05_a1_obj_s1_l01_high\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"train_pi05_a1_obj_s0_l01_high\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_stepwise_s0_l1_28k\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 48.5, \"avg_CAR\": 54.5, \"task0_orange_juice\": {\"TSR\": 28, \"CAR\": 50, \"avg_max_disp\": 0.0618}, \"task1_chocolate_pudding\": {\"TSR\": 68, \"CAR\": 74, \"avg_max_disp\": 0.0463}, \"task2_milk\": {\"TSR\": 44, \"CAR\": 72, \"avg_max_disp\": 0.0277}, \"task3_bbq_sauce\": {\"TSR\": 54, \"CAR\": 22, \"avg_max_disp\": 0.0878}, \"frozen_rate\": 0, \"seed\": 7}}, \"eval_stepwise_s0_l1_24k_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"CAR\": 52.5, \"dfCAR\": 52.5, \"frozen_rate\": 0, \"TSR\": 50.5, \"per_task_CAR\": {\"orange_juice\": 54, \"chocolate_pudding\": 72, \"milk\": 64, \"bbq_sauce\": 20}, \"per_task_TSR\": {\"orange_juice\": 30, \"chocolate_pudding\": 78, \"milk\": 30, \"bbq_sauce\": 64}, \"per_task_frozen\": {\"orange_juice\": 0, \"chocolate_pudding\": 0, \"milk\": 0, \"bbq_sauce\": 0}}}, \"eval_stepwise_s0_l1_24k\": {\"status\": \"DONE\", \"metrics\": {\"INVALID\": true, \"invalidation_reason\": \"Missing --pi05 flag caused architecture mismatch (Pi0 instead of Pi0.5), producing 29.5% frozen episodes as artifact. All metrics from this eval are unreliable. See eval_stepwise_s0_l1_24k_v2 for corrected results.\", \"original_CAR\": 55.5, \"original_frozen_rate\": 29.5, \"original_dfCAR\": 36.9}, \"conclusion\": \"failed\"}, \"eval_stepwise_s0_l1_26k_v2\": {\"status\": \"DONE\", \"metrics\": {\"TSR\": 0.53, \"CAR\": 0.535, \"dfCAR\": 0.535, \"frozen_rate\": 0, \"frozen_episodes\": 0, \"total_episodes\": 200, \"per_task\": {\"orange_juice\": {\"TSR\": 0.32, \"CAR\": 0.46, \"dfCAR\": 0.46, \"frozen\": 0}, \"chocolate_pudding\": {\"TSR\": 0.76, \"CAR\": 0.72, \"dfCAR\": 0.72, \"frozen\": 0}, \"milk\": {\"TSR\": 0.5, \"CAR\": 0.68, \"dfCAR\": 0.68, \"frozen\": 0}, \"bbq_sauce\": {\"TSR\": 0.54, \"CAR\": 0.28, \"dfCAR\": 0.28, \"frozen\": 0}}}, \"conclusion\": \"success\"}, \"eval_stepwise_s0_l1_26k\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_spatial_sdf_s0_l005_30k\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"CAR\": 16, \"TSR\": 53, \"dfCAR\": 0, \"frozen_ratio\": 16, \"per_task_CAR\": {\"task0\": 0, \"task1\": 16, \"task2\": 4, \"task3\": 44}, \"per_task_TSR\": {\"task0\": 66, \"task1\": 38, \"task2\": 72, \"task3\": 36}, \"per_task_frozen\": {\"task0\": 0, \"task1\": 8, \"task2\": 2, \"task3\": 22}}}, \"eval_stepwise_s1_l1_22k\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"CAR\": 56.5, \"TSR\": 57.5, \"eval_seed\": 7, \"frozen_pct\": 0, \"seed\": 1, \"step\": 22000}}, \"train_pi05_lora_baseline_s2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_stepwise_s0_l1_22k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"CAR\": 60.5, \"TSR\": 45.5, \"frozen_pct\": 0, \"step\": 22000, \"seed\": 0, \"eval_seed\": 7}}, \"eval_stepwise_s0_l1_16k\": {\"status\": \"DONE\", \"metrics\": {\"CAR\": 55.5, \"TSR\": 49.5, \"per_task\": [{\"task\": \"orange_juice\", \"TSR\": 26, \"CAR\": 56}, {\"task\": \"pudding\", \"TSR\": 74, \"CAR\": 74}, {\"task\": \"milk\", \"TSR\": 38, \"CAR\": 68}, {\"task\": \"bbq_sauce\", \"TSR\": 60, \"CAR\": 24}]}, \"conclusion\": \"negative\"}, \"eval_early_signal_s1_l1_20k\": {\"status\": \"DONE\", \"metrics\": {\"CAR\": 56, \"TSR\": 51, \"frozen_ee\": 0, \"per_task_CAR\": {\"pick_up_the_orange_juice_and_place_it_in_the_basket\": 62, \"task1\": 76, \"pick_up_the_milk_and_place_it_in_the_basket\": 66, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 20}, \"per_task_TSR\": {\"pick_up_the_orange_juice_and_place_it_in_the_basket\": 20, \"task1\": 82, \"pick_up_the_milk_and_place_it_in_the_basket\": 42, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 60}}, \"conclusion\": \"negative\"}, \"eval_early_signal_s0_l1_20k\": {\"status\": \"DONE\", \"metrics\": {\"overall_CAR\": 0.55, \"overall_TSR\": 0.54, \"frozen_ee_pct\": 0, \"per_task\": [{\"task\": \"orange_juice\", \"CAR\": 0.5, \"TSR\": 0.38, \"avg_max_disp\": 0.0467, \"avg_max_ee_disp\": 0.3917}, {\"task\": \"chocolate_pudding\", \"CAR\": 0.72, \"TSR\": 0.74, \"avg_max_disp\": 0.0487, \"avg_max_ee_disp\": 0.4044}, {\"task\": \"milk\", \"CAR\": 0.72, \"TSR\": 0.44, \"avg_max_disp\": 0.0319, \"avg_max_ee_disp\": 0.3492}, {\"task\": \"bbq_sauce\", \"CAR\": 0.26, \"TSR\": 0.6, \"avg_max_disp\": 0.0928, \"avg_max_ee_disp\": 0.3895}], \"hard_constraints\": {\"TSR_ge_35\": true, \"frozen_ee_0\": true}, \"abc_signal\": \"B\", \"total_episodes\": 200}, \"conclusion\": \"negative\"}, \"train_pi05_a1_spatial_bowl_s0_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.0137, \"final_action_loss\": 0.0135, \"final_sdf_loss\": 0.0327, \"final_ee_loss\": 0.0068, \"best_loss\": 0.01063, \"best_step\": 28000, \"total_steps\": 30000, \"time_per_step\": 4.65, \"wall_clock_hours\": 28.4}}, \"analysis_threshold_sensitivity\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"dfCAR_stable_range_mm\": \"[2, 200]\", \"n_models\": 8, \"n_thresholds\": 8, \"n_active_equals_n_total_at_200mm\": true, \"max_dfCAR_variation_2_to_200mm\": 0, \"min_displacement_m\": 0.271, \"conclusion\": \"dfCAR perfectly invariant across tau_d in [2, 200] mm for all 8 model-seed combinations; only at 300mm do 1-2 episodes fall below threshold\"}}, \"reeval_sdf_s2_l005_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 56, \"CAR\": 52.5, \"avg_max_ee_disp\": 0.3858, \"frozen_ee\": 0, \"per_task\": {\"T0_orange_juice\": {\"TSR\": 34, \"CAR\": 46, \"ee_disp\": 0.3923, \"obj_disp\": 0.0598}, \"T1_chocolate_pudding\": {\"TSR\": 82, \"CAR\": 74, \"ee_disp\": 0.4098, \"obj_disp\": 0.046}, \"T2_milk\": {\"TSR\": 38, \"CAR\": 72, \"ee_disp\": 0.3574, \"obj_disp\": 0.0406}, \"T3_bbq_sauce\": {\"TSR\": 70, \"CAR\": 18, \"ee_disp\": 0.3838, \"obj_disp\": 0.0833}}}}, \"reeval_sdf_s2_l01_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 53.5, \"CAR\": 54.5, \"avg_max_ee_disp\": 0.3877, \"frozen_ee\": 0, \"per_task\": {\"T0_orange_juice\": {\"TSR\": 24, \"CAR\": 64, \"ee_disp\": 0.3822, \"obj_disp\": 0.0385}, \"T1_chocolate_pudding\": {\"TSR\": 72, \"CAR\": 68, \"ee_disp\": 0.4189, \"obj_disp\": 0.0517}, \"T2_milk\": {\"TSR\": 48, \"CAR\": 72, \"ee_disp\": 0.3567, \"obj_disp\": 0.0258}, \"T3_bbq_sauce\": {\"TSR\": 70, \"CAR\": 14, \"ee_disp\": 0.3931, \"obj_disp\": 0.0861}}}}, \"reeval_sdf_s1_l01_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 55.5, \"CAR\": 57.5, \"avg_max_ee_disp\": 0.3852, \"frozen_ee\": 0, \"per_task\": {\"T0_orange_juice\": {\"TSR\": 22, \"CAR\": 60, \"ee_disp\": 0.3892, \"obj_disp\": 0.0536}, \"T1_chocolate_pudding\": {\"TSR\": 80, \"CAR\": 76, \"ee_disp\": 0.4073, \"obj_disp\": 0.0472}, \"T2_milk\": {\"TSR\": 54, \"CAR\": 72, \"ee_disp\": 0.3552, \"obj_disp\": 0.0387}, \"T3_bbq_sauce\": {\"TSR\": 66, \"CAR\": 22, \"ee_disp\": 0.3892, \"obj_disp\": 0.0916}}}}, \"reeval_sdf_s1_l005_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 50.5, \"CAR\": 54, \"avg_max_ee_disp\": 0.3883, \"frozen_ee\": 0, \"per_task\": {\"T0_orange_juice\": {\"TSR\": 28, \"CAR\": 64, \"ee_disp\": 0.3816, \"obj_disp\": 0.0349}, \"T1_chocolate_pudding\": {\"TSR\": 72, \"CAR\": 70, \"ee_disp\": 0.4206, \"obj_disp\": 0.0491}, \"T2_milk\": {\"TSR\": 30, \"CAR\": 68, \"ee_disp\": 0.3588, \"obj_disp\": 0.0328}, \"T3_bbq_sauce\": {\"TSR\": 72, \"CAR\": 14, \"ee_disp\": 0.3924, \"obj_disp\": 0.0931}}}}, \"eval_lora_baseline_30k_s0_reeval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 51.5, \"CAR\": 56.5, \"avg_max_ee_disp\": 0.3957, \"frozen_ee\": 0, \"per_task\": {\"orange_juice\": {\"TSR\": 32, \"CAR\": 56}, \"chocolate_pudding\": {\"TSR\": 74, \"CAR\": 74}, \"milk\": {\"TSR\": 42, \"CAR\": 70}, \"bbq_sauce\": {\"TSR\": 58, \"CAR\": 26}}}}, \"reeval_sdf_s0_l005_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"tsr\": 55.5, \"car\": 57, \"frozen_rate_ee\": 0, \"fake_safe_rate_ee\": 0, \"per_task\": {\"orange_juice\": {\"tsr\": 38, \"car\": 52}, \"chocolate_pudding\": {\"tsr\": 80, \"car\": 74}, \"milk\": {\"tsr\": 38, \"car\": 74}, \"bbq_sauce\": {\"tsr\": 66, \"car\": 28}}}}, \"eval_phase2_lambda0_s2\": {\"status\": \"DONE\", \"metrics\": {\"per_task\": [{\"task_id\": 0, \"task_name\": \"pick_up_the_orange_juice_and_place_it_in_the_basket\", \"TSR\": 30, \"CAR\": 56, \"mean_max_ee_disp\": 0.3837, \"frozen_rate\": 0}, {\"task_id\": 1, \"task_name\": \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\", \"TSR\": 76, \"CAR\": 74, \"mean_max_ee_disp\": 0.4059, \"frozen_rate\": 0}, {\"task_id\": 2, \"task_name\": \"pick_up_the_milk_and_place_it_in_the_basket\", \"TSR\": 42, \"CAR\": 74, \"mean_max_ee_disp\": 0.3565, \"frozen_rate\": 0}, {\"task_id\": 3, \"task_name\": \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\", \"TSR\": 66, \"CAR\": 26, \"mean_max_ee_disp\": 0.3903, \"frozen_rate\": 0}], \"mean\": {\"TSR\": 53.5, \"CAR\": 57.5, \"mean_max_ee_disp\": 0.3841, \"frozen_rate\": 0}}, \"conclusion\": \"success\"}, \"train_pi05_phase2_lambda0_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss_action\": 0.0113, \"final_loss_sdf\": 0.1369, \"final_loss_ee\": 0.0079, \"best_loss\": 0.00651, \"best_step\": 4000, \"total_steps\": 10000, \"time_per_step\": 4.64, \"wall_clock_hours\": 12.88}}, \"reeval_lora_s1_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"tsr\": 51.5, \"car\": 52.5, \"ee_disp\": 0.3882, \"frozen_rate_ee\": 0, \"fake_safe_rate_ee\": 0, \"per_task\": {\"orange_juice\": {\"tsr\": 34, \"car\": 54}, \"chocolate_pudding\": {\"tsr\": 62, \"car\": 68}, \"milk\": {\"tsr\": 50, \"car\": 72}, \"bbq_sauce\": {\"tsr\": 60, \"car\": 16}}}}, \"reeval_sdf_s0_l01_30k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"tsr\": 52.5, \"car\": 57, \"ee_disp\": 0.3946, \"frozen_rate_ee\": 0, \"frozen_rate_obs\": 55.5, \"fake_safe_rate_ee\": 0, \"obstacle_disp\": 0.0577, \"ee_disp_range\": [0.312, 0.865], \"per_task\": {\"orange_juice\": {\"tsr\": 28, \"car\": 48}, \"chocolate_pudding\": {\"tsr\": 78, \"car\": 74}, \"milk\": {\"tsr\": 44, \"car\": 72}, \"bbq_sauce\": {\"tsr\": 60, \"car\": 34}}, \"note\": \"frozen_rate_ee = EE disp < 0.1mm (paper definition); frozen_rate_obs = obstacle disp < 0.1mm (analyzer script definition, NOT paper definition)\"}}, \"eval_pi05_baseline_reeval_disp\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"eval_lora_baseline_30k_s0_v2\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 8.5, \"avg_CAR\": 54.5, \"n_episodes\": 200, \"frozen_pct\": 0, \"avg_ee_disp\": 0.4887, \"dfCAR_100mm\": 54.5, \"per_task\": [{\"task\": \"pick_up_the_orange_juice_and_place_it_in_the_basket\", \"safety\": \"II\", \"n\": 50, \"TSR\": 0, \"CAR\": 62, \"avg_ee_disp\": 0.497, \"median_ee_disp\": 0.4208, \"frozen_pct\": 0}, {\"task\": \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\", \"safety\": \"II\", \"n\": 50, \"TSR\": 34, \"CAR\": 44, \"avg_ee_disp\": 0.5041, \"median_ee_disp\": 0.4251, \"frozen_pct\": 0}, {\"task\": \"pick_up_the_milk_and_place_it_in_the_basket\", \"safety\": \"II\", \"n\": 50, \"TSR\": 0, \"CAR\": 94, \"avg_ee_disp\": 0.5765, \"median_ee_disp\": 0.5511, \"frozen_pct\": 0}, {\"task\": \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\", \"safety\": \"II\", \"n\": 50, \"TSR\": 0, \"CAR\": 18, \"avg_ee_disp\": 0.3772, \"median_ee_disp\": 0.3712, \"frozen_pct\": 0}]}, \"conclusion\": \"success\"}, \"eval_lora_baseline_30k_s1_v2\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 4, \"avg_CAR\": 56, \"dfCAR_100mm\": 56, \"avg_ee_disp\": 0.4669, \"frozen_pct\": 0, \"n_episodes\": 200, \"per_task\": {\"pick_up_the_orange_juice\": {\"TSR\": 2, \"CAR\": 58, \"ee_disp_mean\": 0.4827, \"ee_disp_median\": 0.4011, \"frozen_pct\": 0}, \"pick_up_the_chocolate_pudding\": {\"TSR\": 14, \"CAR\": 50, \"ee_disp_mean\": 0.538, \"ee_disp_median\": 0.4548, \"frozen_pct\": 0}, \"pick_up_the_milk\": {\"TSR\": 0, \"CAR\": 90, \"ee_disp_mean\": 0.4817, \"ee_disp_median\": 0.512, \"frozen_pct\": 0}, \"pick_up_the_bbq_sauce\": {\"TSR\": 0, \"CAR\": 26, \"ee_disp_mean\": 0.3653, \"ee_disp_median\": 0.3335, \"frozen_pct\": 0}}}, \"conclusion\": \"success\"}, \"eval_lora_baseline_30k_s1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_lora_baseline_30k_s0\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"train_pi05_lora_baseline_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.01408, \"best_loss\": 0.0113, \"best_step\": 14000, \"total_steps\": 30000, \"grad_norm\": 0.10628, \"time_per_step\": 4.62}}, \"train_pi05_lora_baseline_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.01343, \"best_loss\": 0.01025, \"best_step\": 24000, \"total_steps\": 30000, \"grad_norm\": 0.10538, \"time_per_step\": 4.613}}, \"eval_pi05_a1_30k_s0_l01_disp\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 6.5, \"avg_CAR\": 52.5, \"n_episodes\": 200, \"avg_max_ee_displacement\": 0.4725, \"task0_TSR\": 0, \"task0_CAR\": 76, \"task0_ee_disp\": 0.4781, \"task0_safe_ee_disp\": 0.4627, \"task1_TSR\": 26, \"task1_CAR\": 32, \"task1_ee_disp\": 0.5387, \"task1_safe_ee_disp\": 0.4446, \"task2_TSR\": 0, \"task2_CAR\": 84, \"task2_ee_disp\": 0.5169, \"task2_safe_ee_disp\": 0.5273, \"task3_TSR\": 0, \"task3_CAR\": 18, \"task3_ee_disp\": 0.3561, \"task3_safe_ee_disp\": 0.3764, \"fake_safe_pct\": 0, \"real_safety\": true, \"frozen\": false}}, \"eval_pi05_a1_30k_s1_l005_disp\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 4, \"avg_CAR\": 54, \"n_episodes\": 200, \"avg_max_ee_displacement\": 0.4955, \"task0_TSR\": 2, \"task0_CAR\": 54, \"task0_ee_disp\": 0.5062, \"task0_safe_ee_disp\": 0.4247, \"task1_TSR\": 14, \"task1_CAR\": 58, \"task1_ee_disp\": 0.4991, \"task1_safe_ee_disp\": 0.5006, \"task2_TSR\": 0, \"task2_CAR\": 92, \"task2_ee_disp\": 0.6088, \"task2_safe_ee_disp\": 0.6213, \"task3_TSR\": 0, \"task3_CAR\": 12, \"task3_ee_disp\": 0.368, \"task3_safe_ee_disp\": 0.3628, \"fake_safe_pct\": 0, \"real_safety\": true, \"frozen\": false}}, \"eval_pi05_a1_best_s2_l005_10k\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 9, \"avg_CAR\": 55.5, \"n_episodes\": 200, \"avg_max_ee_displacement\": 0.5046, \"task0_TSR\": 0, \"task0_CAR\": 68, \"task0_ee_disp\": 0.5256, \"task0_safe_ee_disp\": 0.4979, \"task1_TSR\": 36, \"task1_CAR\": 44, \"task1_ee_disp\": 0.5288, \"task1_safe_ee_disp\": 0.5115, \"task2_TSR\": 0, \"task2_CAR\": 92, \"task2_ee_disp\": 0.5779, \"task2_safe_ee_disp\": 0.5883, \"task3_TSR\": 0, \"task3_CAR\": 18, \"task3_ee_disp\": 0.3863, \"task3_safe_ee_disp\": 0.3609, \"fake_safe_pct\": 0, \"task2_fake_safety\": false, \"real_safety\": true, \"task0_obs_frozen_pct\": 0.7, \"task2_obs_frozen_pct\": 0.92, \"analysis\": \"ALL episodes have high EE displacement (0.39-0.58m). Zero fake safety. 10K best shows genuine collision avoidance: robot moves normally and avoids obstacles. Task 2 high CAR (92%) is REAL avoidance not action collapse.\"}}, \"eval_pi05_a1_best_s1_l005_16k\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 6.5, \"avg_CAR\": 53, \"n_episodes\": 200, \"task0_TSR\": 4, \"task0_CAR\": 58, \"task0_ee_disp\": 0.5179, \"task0_max_disp\": 0.0416, \"task1_TSR\": 22, \"task1_CAR\": 50, \"task1_ee_disp\": 0.5146, \"task1_max_disp\": 0.1018, \"task2_TSR\": 0, \"task2_CAR\": 88, \"task2_ee_disp\": 0.6475, \"task2_max_disp\": 0.0073, \"task3_TSR\": 0, \"task3_CAR\": 16, \"task3_ee_disp\": 0.3707, \"task3_max_disp\": 0.0934, \"fake_safe_pct\": 0, \"real_safety\": true}, \"conclusion\": \"success\"}, \"eval_pi05_a1_30k_s1_l01_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 7.5, \"avg_CAR\": 52.5, \"n_episodes\": 200, \"task0_TSR\": 4, \"task0_CAR\": 54, \"task1_TSR\": 26, \"task1_CAR\": 48, \"task2_TSR\": 0, \"task2_CAR\": 94, \"task3_TSR\": 0, \"task3_CAR\": 14}}, \"eval_pi05_a1_30k_s1_l005_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 5.5, \"avg_CAR\": 52.5, \"n_episodes\": 200, \"task0_TSR\": 4, \"task0_CAR\": 58, \"task1_TSR\": 18, \"task1_CAR\": 40, \"task2_TSR\": 0, \"task2_CAR\": 94, \"task3_TSR\": 0, \"task3_CAR\": 18}}, \"eval_pi05_a1_30k_s2_l005_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 9.5, \"avg_CAR\": 54.5, \"n_episodes\": 200, \"task0_TSR\": 2, \"task0_CAR\": 62, \"task1_TSR\": 36, \"task1_CAR\": 44, \"task2_TSR\": 0, \"task2_CAR\": 90, \"task3_TSR\": 0, \"task3_CAR\": 22}}, \"eval_pi05_a1_30k_s1_l005_v3\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 4, \"avg_CAR\": 51.5, \"n_episodes\": 200, \"task0_TSR\": 0, \"task0_CAR\": 54, \"task1_TSR\": 16, \"task1_CAR\": 48, \"task2_TSR\": 0, \"task2_CAR\": 88, \"task3_TSR\": 0, \"task3_CAR\": 16, \"source\": \"v4 JSON with per-episode displacement\"}, \"conclusion\": \"success\"}, \"eval_pi05_a1_30k_s2_l005_v3\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 9, \"avg_CAR\": 53, \"n_episodes\": 200, \"task0_TSR\": 4, \"task0_CAR\": 60, \"task1_TSR\": 32, \"task1_CAR\": 46, \"task2_TSR\": 0, \"task2_CAR\": 86, \"task3_TSR\": 0, \"task3_CAR\": 20, \"source\": \"v4 JSON with per-episode displacement\"}, \"conclusion\": \"success\"}, \"eval_pi05_a1_30k_s2_l01_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 7.5, \"avg_CAR\": 53, \"n_episodes\": 200, \"task0_TSR\": 0, \"task0_CAR\": 62, \"task1_TSR\": 30, \"task1_CAR\": 42, \"task2_TSR\": 0, \"task2_CAR\": 88, \"task3_TSR\": 0, \"task3_CAR\": 20, \"source\": \"v3 JSON with per-episode displacement\"}}, \"eval_pi05_a1_30k_s0_l01\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 5.5, \"avg_CAR\": 53, \"n_episodes\": 200, \"task0_TSR\": 2, \"task0_CAR\": 68, \"task1_TSR\": 20, \"task1_CAR\": 46, \"task2_TSR\": 0, \"task2_CAR\": 86, \"task3_TSR\": 0, \"task3_CAR\": 12, \"task0_disp\": 0.0297, \"task1_disp\": 0.0815, \"task2_disp\": 0.0112, \"task3_disp\": 0.0797, \"note\": \"旧版脚本，无max_ee_displacement字段\"}}, \"eval_pi05_a1_30k_s0_l005_r4\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 7.5, \"avg_CAR\": 47, \"n_episodes\": 200, \"task0_TSR\": 6, \"task0_CAR\": 58, \"task1_TSR\": 24, \"task1_CAR\": 38, \"task2_TSR\": 0, \"task2_CAR\": 76, \"task3_TSR\": 0, \"task3_CAR\": 16, \"task0_disp\": 0.0485, \"task1_disp\": 0.0782, \"task2_disp\": 0.0147, \"task3_disp\": 0.1009, \"note\": \"旧版脚本，无max_ee_displacement字段\"}, \"conclusion\": \"success\"}, \"train_pi05_phase2_lambda0_s0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_a1_30k_s0_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"avg_TSR\": 5.5, \"avg_CAR\": 50, \"n_episodes\": 200, \"task0_TSR\": 2, \"task0_CAR\": 58, \"task1_TSR\": 20, \"task1_CAR\": 42, \"task2_TSR\": 0, \"task2_CAR\": 86, \"task3_TSR\": 0, \"task3_CAR\": 14, \"task0_disp\": 0.0433, \"task1_disp\": 0.1055, \"task2_disp\": 0.0147, \"task3_disp\": 0.0879}}, \"train_pi05_a1_obj_s0_l01\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.00801, \"steps_completed\": 30000}}, \"train_pi05_a1_obj_s0_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.007860926911234856, \"best_loss_step\": 26000, \"steps_completed\": 30000}}, \"eval_pi05_a1_30k_s2_l01\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_a1_30k_s2_l005\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_a1_30k_s1_l01\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_a1_30k_s1_l005\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_pi05_a1_obj_s2_l01\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.00911, \"best_loss_step\": 10000, \"steps_completed\": 30000}}, \"train_pi05_a1_obj_s2_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.00874, \"best_loss_step\": 10000, \"steps_completed\": 30000}}, \"train_pi05_a1_obj_s1_l01\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.01168, \"best_loss_step\": 16000, \"steps_completed\": 30000}}, \"train_pi05_a1_obj_s1_l005\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.01143, \"best_loss_step\": 16000, \"steps_completed\": 30000}}, \"train_pi05_a1_obj_l01\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"train_pi05_a1_obj_l005\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_safelibero_object_v11_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 0.75, \"CAR\": 0.275, \"mean_displacement\": 0.132}}, \"eval_pi05_safelibero_object_v11_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"TSR\": 0.76, \"CAR\": 0.25, \"mean_displacement\": 0.153}}, \"eval_pi05_safelibero_spatial_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_TSR\": 0.575, \"overall_CAR\": 0.13, \"task3_CAR\": 0.52, \"n_episodes\": 200}}, \"eval_pi05_safelibero_object_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_TSR\": 0.73, \"overall_CAR\": 0.28, \"overall_avg_disp\": 0.1508, \"real_safe_rate\": 0.005, \"fake_safe_rate\": 0.982, \"task0_TSR\": 0.64, \"task0_CAR\": 0.06, \"task1_TSR\": 0.86, \"task1_CAR\": 0.56, \"task2_TSR\": 0.66, \"task2_CAR\": 0.16, \"task3_TSR\": 0.76, \"task3_CAR\": 0.34, \"n_episodes\": 200}}, \"eval_a3_spatial_force_refine_v11\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_a3_spatial_m024fix_v11\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"oracle_true_gt_feature_object_v11\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_a1_lora_object_v11_rerun\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 0, \"avg_CAR\": 91.5, \"n_episodes\": 800, \"eps_per_task\": 200, \"task_TSR\": {\"orange_juice\": 0, \"chocolate_pudding\": 0, \"milk\": 0, \"bbq_sauce\": 0}, \"task_CAR\": {\"orange_juice\": 96, \"chocolate_pudding\": 82, \"milk\": 97, \"bbq_sauce\": 91}, \"fake_safe_rate\": 0.996, \"fake_safe_detail\": \"729/732 safe episodes have displacement<0.1mm\", \"real_safe_count\": 3, \"real_safe_rate\": 0.004, \"safe_disp_distribution\": {\"<1um\": 541, \"1um-0.1mm\": 188, \"0.1-1mm\": 3, \">1mm\": 0}, \"task_fake_safe\": {\"orange_juice\": \"192/192 (100%)\", \"chocolate_pudding\": \"162/164 (98.8%)\", \"milk\": \"194/194 (100%)\", \"bbq_sauce\": \"181/182 (99.5%)\"}, \"task_avg_disp_mm\": {\"orange_juice\": 0.871, \"chocolate_pudding\": 7.491, \"milk\": 2.508, \"bbq_sauce\": 4.75}, \"task_safe_disp_mean_mm\": {\"orange_juice\": 0.000315, \"chocolate_pudding\": 0.007588, \"milk\": 0.000288, \"bbq_sauce\": 0.001293}, \"collision_eps\": 68, \"collision_disp_mean_mm\": 45.92, \"collision_disp_max_mm\": 286.53, \"baseline_comparison\": {\"baseline_CAR\": 83, \"baseline_fake_safe\": \"165/166 (99.4%)\", \"baseline_real_safe\": \"1/200 (0.5%)\", \"baseline_n_episodes\": 200}}}, \"oracle_true_gt_feature_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 0, \"avg_CAR\": 76.9, \"task_CAR\": {\"orange_juice\": 90, \"chocolate_pudding\": 47.5, \"milk\": 82.5, \"bbq_sauce\": 87.5}, \"task_displacement\": {\"orange_juice\": 0.0023, \"chocolate_pudding\": 0.0473, \"milk\": 0.0086, \"bbq_sauce\": 0.0097}, \"task_refine_count_mean\": {\"orange_juice\": 248.5, \"chocolate_pudding\": 241.8, \"milk\": 236.7, \"bbq_sauce\": 240}, \"task_grad_mag_mean\": {\"orange_juice\": 0.00423, \"chocolate_pudding\": 0.00609, \"milk\": 0.00466, \"bbq_sauce\": 0.00491}, \"fake_safe_rate\": 0.967, \"fake_safe_detail\": \"119/123 safe episodes have displacement<0.1mm\", \"total_refined_steps\": 38679, \"avg_refined_per_episode\": 241.7, \"n_episodes\": 160}}, \"oracle_true_gt_fixed_alpha_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 0, \"avg_CAR\": 73.1, \"task_CAR\": {\"orange_juice\": 85, \"chocolate_pudding\": 50, \"milk\": 77.5, \"bbq_sauce\": 80}, \"task_displacement\": {\"orange_juice\": 0.0113, \"chocolate_pudding\": 0.0365, \"milk\": 0.0042, \"bbq_sauce\": 0.0032}, \"task_refine_count_mean\": {\"orange_juice\": 8.7, \"chocolate_pudding\": 20.2, \"milk\": 20.1, \"bbq_sauce\": 10.4}, \"total_refined_steps\": 2375, \"avg_refined_per_episode\": 14.8, \"fake_safe_rate\": 0.983, \"fake_safe_detail\": \"115/117 safe episodes have displacement<0.1mm\", \"task_fake_safe\": {\"orange_juice\": \"34/34 (100%)\", \"chocolate_pudding\": \"19/20 (95%)\", \"milk\": \"30/31 (96.8%)\", \"bbq_sauce\": \"32/32 (100%)\"}, \"collision_threshold\": 0.001, \"n_episodes\": 160}}, \"oracle_true_gt_adaptive_alpha_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"avg_TSR\": 0, \"avg_CAR\": 75, \"task_CAR\": {\"orange_juice\": 82.5, \"chocolate_pudding\": 55, \"milk\": 77.5, \"bbq_sauce\": 85}, \"task_displacement\": {\"orange_juice\": 0.0076, \"chocolate_pudding\": 0.0475, \"milk\": 0.0107, \"bbq_sauce\": 0.0077}, \"task_refine_count_mean\": {\"orange_juice\": 7.6, \"chocolate_pudding\": 22.4, \"milk\": 17.6, \"bbq_sauce\": 9.1}, \"task_grad_mag_mean\": {\"orange_juice\": 0.176, \"chocolate_pudding\": 0.247, \"milk\": 0.489, \"bbq_sauce\": 0.357}, \"fake_safe_rate\": 0.983, \"fake_safe_detail\": \"118/120 safe episodes have displacement<0.1mm\", \"total_refined_steps\": 2270, \"avg_refined_per_episode\": 14.2, \"n_episodes\": 160}}, \"a3_gradient_spatial_bowl_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.01552, \"steps_completed\": 30000}}, \"oracle_true_gt_object_v11\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_a3_object_m024fix_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"task0\": {\"TSR\": 0, \"CAR\": 0.885, \"avg_max_displacement\": 0.0066, \"refined_count\": 0}, \"task1\": {\"TSR\": 0, \"CAR\": 0.46, \"avg_max_displacement\": 0.0492, \"refined_count\": 0}, \"task2\": {\"TSR\": 0, \"CAR\": 0.86, \"avg_max_displacement\": 0.0044, \"refined_count\": 0}, \"task3\": {\"TSR\": 0, \"CAR\": 0.88, \"avg_max_displacement\": 0.0074, \"refined_count\": 0}, \"overall\": {\"avg_TSR\": 0, \"avg_CAR\": 0.771}}}, \"eval_a1_lora_spatial_v11\": {\"status\": \"DONE\", \"metrics\": {\"avg_TSR\": 0.001, \"avg_CAR\": 0.008, \"task0_TSR\": 0.005, \"task0_CAR\": 0.015, \"task0_avg_disp\": 0.2578, \"task1_TSR\": 0, \"task1_CAR\": 0, \"task1_avg_disp\": 0.1955, \"task2_TSR\": 0, \"task2_CAR\": 0, \"task2_avg_disp\": 0.2142, \"task3_TSR\": 0, \"task3_CAR\": 0.015, \"task3_avg_disp\": 0.1992, \"safe_episodes_total\": 6, \"safe_episodes_with_zero_displacement\": 6, \"fake_safety\": true}, \"conclusion\": \"negative\"}, \"eval_baseline_fullft_spatial_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR_avg\": 0.375, \"CAR_avg\": 0, \"n_episodes\": 800, \"per_task\": {\"task0_pick_bowl_between_plate_ramekin\": {\"TSR\": 1.5, \"CAR\": 0, \"avg_max_displacement\": 0.3317, \"avg_smoothness\": 0.003487}, \"task1_pick_bowl_on_ramekin\": {\"TSR\": 0, \"CAR\": 0, \"avg_max_displacement\": 0.2863, \"avg_smoothness\": 0.00326}, \"task2_pick_bowl_on_stove\": {\"TSR\": 0, \"CAR\": 0, \"avg_max_displacement\": 0.2604, \"avg_smoothness\": 0.002417}, \"task3_pick_bowl_on_cabinet\": {\"TSR\": 0, \"CAR\": 0, \"avg_max_displacement\": 0.3017, \"avg_smoothness\": 0.003154}}}}, \"oracle_a3_m024fix_object_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"task0_pick_orange_juice\": {\"TSR\": 0, \"CAR\": 97.5, \"avg_max_displacement\": 0.0028}, \"task1_put_wine_on_rack\": {\"TSR\": 0, \"CAR\": 65, \"avg_max_displacement\": 0.0381}, \"task2_put_cream_in_marked_area\": {\"TSR\": 0, \"CAR\": 97.5, \"avg_max_displacement\": 0}, \"task3_pick_bbq_sauce_to_basket\": {\"TSR\": 0, \"CAR\": 82.5, \"avg_max_displacement\": 0.0134}, \"overall\": {\"TSR_avg\": 0, \"CAR_avg\": 85.6}, \"n_episodes\": 40, \"force_refine\": true, \"refine_count_per_episode\": 300}}, \"oracle_a3_force_refine_object_v11\": {\"status\": \"DONE\", \"metrics\": {\"TSR_avg\": 0, \"CAR_avg\": 81.2, \"n_episodes\": 40, \"per_task\": {\"orange_juice\": {\"TSR\": 0, \"CAR\": 95, \"avg_max_displacement\": 0.0005}, \"chocolate_pudding\": {\"TSR\": 0, \"CAR\": 57.5, \"avg_max_displacement\": 0.046}, \"milk\": {\"TSR\": 0, \"CAR\": 92.5, \"avg_max_displacement\": 0.001}, \"bbq_sauce\": {\"TSR\": 0, \"CAR\": 80, \"avg_max_displacement\": 0.0018}}, \"refined_count_per_episode\": 300, \"force_refine\": true, \"refine_alpha\": 0.1, \"refine_margin\": 0.01, \"displacement_collapse\": \"most episodes show max_displacement 1e-6 to 1e-10, gradient near-zero\"}, \"conclusion\": \"negative\"}, \"a1_lora_spatial_bowl_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.01431, \"steps_completed\": 30000}}, \"eval_a1_lora_object_v11\": {\"status\": \"DONE\", \"metrics\": {\"TSR\": 0, \"CAR_avg\": 90, \"CAR_task0\": 96, \"CAR_task1\": 80, \"CAR_task2\": 94, \"CAR_task3\": 90, \"displacement_avg\": 0.0027, \"displacement_task0\": 0.0017, \"displacement_task1\": 0.0076, \"displacement_task2\": 0.0008, \"displacement_task3\": 0.0008, \"n_episodes\": 200}, \"conclusion\": \"success\"}, \"eval_lora_baseline_object_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR\": 0, \"CAR_avg\": 82, \"CAR_task0\": 96, \"CAR_task1\": 46, \"CAR_task2\": 98, \"CAR_task3\": 88, \"displacement_avg\": 0.01, \"displacement_task0\": 0.0072, \"displacement_task1\": 0.0257, \"displacement_task2\": 1e-05, \"displacement_task3\": 0.007, \"n_episodes\": 200}}, \"eval_lora_baseline_spatial_v11\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR\": 0, \"CAR_avg\": 0, \"CAR_task0\": 0, \"CAR_task1\": 0, \"CAR_task2\": 0, \"CAR_task3\": 0, \"displacement_avg\": 0.23, \"displacement_task0\": 0.2669, \"displacement_task1\": 0.206, \"displacement_task2\": 0.2212, \"displacement_task3\": 0.2328, \"n_episodes\": 200}}, \"eval_a3_v11_object\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR\": 0, \"CAR_avg\": 74.5, \"CAR_task0\": 84, \"CAR_task1\": 48, \"CAR_task2\": 82, \"CAR_task3\": 84, \"displacement_avg\": 0.0164, \"displacement_task0\": 0.0149, \"displacement_task1\": 0.0388, \"displacement_task2\": 0.0079, \"displacement_task3\": 0.0041, \"refined_count_total\": 0, \"n_episodes\": 200}}, \"a1_lora_object_pudding_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.01326, \"final_loss\": 0.0184, \"steps_completed\": 30000, \"wall_time_hours\": 33}}, \"eval_baseline_v11_object\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR\": 0.5, \"CAR_avg\": 83, \"CAR_task0\": 76, \"CAR_task1\": 90, \"CAR_task2\": 88, \"CAR_task3\": 78, \"TSR_task0\": 0, \"TSR_task1\": 2, \"TSR_task2\": 0, \"TSR_task3\": 0, \"displacement_avg\": 0.0271, \"displacement_task0\": 0.038, \"displacement_task1\": 0.0103, \"displacement_task2\": 0.0163, \"displacement_task3\": 0.0438, \"smoothness_avg\": 0.002109, \"n_episodes\": 200}}, \"baseline_lora_object_pudding_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.0124, \"steps_completed\": 30000}}, \"baseline_lora_spatial_bowl_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"best_loss\": 0.00876, \"steps_completed\": 30000}}, \"eval_a3_v10a_refine\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"TSR\": 0, \"CAR_avg\": 79.5, \"CAR_task0\": 90, \"CAR_task1\": 88, \"CAR_task2\": 64, \"CAR_task3\": 76, \"displacement_avg\": 0.0112, \"displacement_task0\": 0.0009, \"displacement_task1\": 0.0108, \"displacement_task2\": 0.0168, \"displacement_task3\": 0.0162, \"refined_count\": 0, \"n_episodes\": 200}}, \"eval_a3_object_pudding_no_refine\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_a3_object_pudding_refine\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"TSR\": 0, \"CAR_task0_orange_juice\": 96, \"CAR_task1_chocolate_pudding\": 22, \"CAR_task2_milk\": 66, \"CAR_task3_bbq_sauce\": 42, \"CAR_avg\": 56.5, \"TSR_task0\": 0, \"TSR_task1\": 0, \"TSR_task2\": 0, \"TSR_task3\": 0, \"n_episodes\": 50, \"refine_count_all_zero\": true}}, \"a3_gradient_object_pudding_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"action_loss\": 0.01546, \"total_loss\": 0.01898, \"final_loss\": 0.01898, \"best_loss\": 0.01439, \"ee_loss\": 0.01213, \"eikonal\": 0, \"grad_norm\": 0.24129, \"n_refine\": 2.64, \"steps_completed\": 30000}}, \"baseline_spatial_bowl_s0_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.0032, \"best_loss\": 0.00316, \"steps_completed\": 30000, \"lr_final\": 2.5e-06, \"wall_time_hours\": 16.1, \"vram_mib\": 35738, \"checkpoint_step\": 30000, \"avg_it_per_sec\": 3.62}}, \"baseline_object_pudding_s0_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.005, \"steps_completed\": 30000, \"lr_final\": 2.5e-06, \"wall_time_hours\": 14, \"vram_mib\": 35738}}, \"a1_sdf_spatial_bowl_s0_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"a1_sdf_object_pudding_s0\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"baseline_spatial_bowl_s1_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"a1_sdf_spatial_bowl_s0_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"a1_sdf_spatial_bowl_s0\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"baseline_spatial_bowl_s0\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"baseline_spatial_bowl_s1\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"baseline_object_pudding_s0\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}}, \"count\": 123, \"total\": 123, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.579}}"
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
Let me extract the key data from the registry:

**λ=0.1 (3 seeds):**
- `reeval_sdf_s0_l01_30k`: CAR=57, TSR=52.5
- `reeval_sdf_s1_l01_30k`: CAR=57.5, TSR=55.5
- `reeval_sdf_s2_l01_30k`: CAR=54.5, TSR=53.5

CAR mean = (57 + 57.5 + 54.5) / 3 = 169/3 = 56.333... 

That's not matching the task's reported 57.00, so let me look at the `eval_pi05_a1_30k_s*_l01_high` entries instead:
- `eval_pi05_a1_30k_s0_l01_high`: CAR=58, TSR=47
- `eval_pi05_a1_30k_s1_l01_high`: CAR=58.5, TSR=49
- `eval_pi05_a1_30k_s2_l01_high`: CAR=54.5, TSR=54.5

For the "high" evals, the CAR mean works out to exactly 57.0, and the standard deviation is around 2.18. Now I need to calculate the TSR mean for λ=0.1, which comes to about 50.17.

Looking at the LoRA reeval data, I'm seeing multiple entries with different seeds and versions—some marked as "reeval" and others as "eval"—with CAR values ranging from 52.5 to 57 and TSR values clustering around 51.5. I need to clarify which entries are the authoritative ones since there seem to be duplicates or variations for the same seed. I'm calculating the mean CAR across the three seeds: 57 + 52.5 + 55 divided by 3 gives 54.83%, which is close to but not exactly the 54.67% mentioned in the task instructions. Let me verify whether I should be using different LoRA baseline values or if there's another seed configuration I'm missing. be 50.17. For the LoRA baseline, I'm calculating the mean across three seeds: 46, 51.5, and 51.5, which gives 49.67. Now I need to figure out which seeds were actually used in the current 2-seed LoRA calculation to understand what needs updating. I'm noticing a discrepancy in the TSR values between the CSV and the script output, so let me refocus on what needs to be verified. I need to confirm the three-seed LoRA mean of 54.67 by checking where that third seed value comes from, since the registry shows 57 and 52.5 but I'm uncertain about the third value. But the ROADMAP explicitly gives 54.67±2.02, so I should use that value directly. For TSR, I'm recalculating from the reevaluation data: the three seed runs give me 46, 51.5, and 51.5, which averages to 49.67—but that doesn't match the current 51.5 in the script, so I need to figure out what 2-seed TSR values were originally used.

Looking at the CSV, it shows 48.75 for LoRA TSR, yet the script has 51.5 for tsr_mean[0]—there's a clear discrepancy between what the CSV reports and what the script is using, likely because the script pulled from different reevaluation runs than what ended up in the final CSV.

Now I'm tracing through the actual reevaluation data to understand where 51.5 comes from. The two-seed average of the reevaluation entries both gives 51.5, and when I check the three-seed case with the additional data point, it also stays at 51.5. But I'm noticing conflicting TSR values for the seed-0 LoRA run—one source shows 46 while another shows 51.5, so I need to figure out which one is correct.

Looking more carefully at the naming conventions, the reeval entries with "v2" in the name appear to be a different version of the evaluation, and the CAR values in the current script (57.0 and 52.5) seem to match the v2 reeval data, which suggests that's the version being used. Looking at the LoRA s2 data, I see eval_lora_s2_30k_v2 shows CAR=55%, but when I average the three seeds (57 + 52.5 + 55) / 3, I get 54.83%, which doesn't match the ROADMAP value of 54.67%. Working backwards from 54.67 suggests s2 should be around 54.5%, so there's likely a discrepancy between the eval data I'm seeing and what was actually used for the ROADMAP calculation.

Now I'm checking if the standard deviation of 2.02 makes sense with these values. If the mean is 54.67 and std is 2.02, that gives a variance of about 4.08, but when I calculate the actual squared deviations from the three seed values, I'm not getting a match—so either the s2 value is different than what I'm seeing, or there's some other variation in how these statistics were computed. = 8.1608 (sample variance with n-1=2)

If s0=57, s1=52.5:
(57-54.67)^2 = 2.33^2 = 5.4289
(52.5-54.67)^2 = (-2.17)^2 = 4.7089
sum so far = 10.1378
remaining for s2: 8.1608 - 10.1378 = -1.977... This is negative, impossible!

So the ROADMAP values 54.67±2.02 can't be correct with s0=57, s1=52.5. Unless different eval values are being used.

Actually, wait. Maybe the ROADMAP uses different LoRA eval runs. Let me think...

Maybe the reeval values are:
- reeval_lora_s0_30k_v2: CAR=57 
→ but maybe this isn't the one being used
- eval_lora_baseline_30k_s0_reeval: CAR=56.5

If I swap in the alternative s0 value of 56.5 instead of 57, the mean works out to 54.67 and the standard deviation calculation gives me 2.021, which matches the reported ±2.02.

Now I'm checking the TSR metric for the same three seeds and finding that both the s0 and s1 entries show TSR=51.5.

Looking at the null band baseline, the task specifies "6值" which means 6 values total—likely combining the 3 LoRA seeds with the 3 λ=0.005 seeds to establish the baseline distribution, though I need to verify which exact data points are being used. I'm finishing the standard deviation calculation and now I need to update the data structure with the corrected values—changing the mean and standard deviation for indices 3 and 0, adjusting the seed counts, and identifying all the other parameters that need to be modified. I'm verifying the TSR calculation for λ=0.1 across the three seeds: (47 + 49 + 54.5) / 3 = 50.17, and LoRA stays at 51.5. Now I need to update the CSV with the new seed values and remove the "30K" annotations since all entries now have n=3.

For the LoRA row, the current CAR seeds show "57.0;52.5" with a mean of 54.75, but the reeval data suggests the actual seeds should be 56.5, 52.5, 55 with a mean of 54.67—which means there might be a discrepancy between the current script values and what the ROADMAP indicates for the 3-seed LoRA version. I should trust the ROADMAP's definitive values rather than second-guessing which individual seed evaluations to use. The task is clear about what needs updating: the mean should shift to 54.67, the standard deviation to 2.02, and the seed count to 3. I'll apply those changes directly to the CSV without overthinking the underlying seed values.

For the TSR metrics, LoRA stays at 51.5 across evaluations, while the λ=0.1 configuration averages to about 50.17 from its three seed runs. Now I'm ready to make the edits to the script, starting with updating the car_mean array.

Updating array values...

Since all seeds are now n=3, I can remove the legend entry for "2 of 3 seeds" and simplify the annotations—each seed will just show n=3, making the "30K" annotation redundant. I'll keep the individual n=3 labels for clarity rather than consolidating them into a single note.

Now I'm going through the edits: removing the "30K†" annotation and the hollow marker legend entry, then updating the CSV data to reflect these changes.

Generating markdown table... I'm verifying the LoRA calculations by checking the individual CAR values across the three seeds and confirming the mean and standard deviation match what's in the roadmap.

Now looking at the TSR values, I notice the CSV shows 48.75 but the script has 51.5, which suggests the CSV might be outdated. I should use the reeval TSR values consistently across all three seeds, which all show 51.5, giving a mean of 51.5 for the updated results.

For the λ=0.1 case, I'm calculating the standard deviation from the three seed values (47, 49, 54.5), which comes out to about 3.88. Since all the LoRA TSR values are 51.5, the standard deviation there would be zero, though that might not matter for the visualization since error bars are only shown for CAR.

Now I need to update both the Python script and the CSV file with these corrected values—updating the TSR_std column for λ=0.1 from 1.4 to 3.88 and setting LoRA's TSR_std to 0.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "947850c7-9f1e-4cdb-bf00-8a65c073884f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7GecmSp9G1B2s446nGWdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18573,
      "cache_read_input_tokens": 28930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18573
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

Registry data confirms:

**λ=0.1 (high evals, 3 seeds):**
- s0: CAR=58, TSR=47
- s1: CAR=58.5, TSR=49
- s2: CAR=54.5, TSR=54.5
- → CAR mean=57.0, std=2.18, TSR mean=50.17

**LoRA (reeval, 3 seeds):**
- s0: CAR=56.5, TSR=51.5
- s1: CAR=52.5, TSR=51.5
- s2: CAR=55, TSR=51.5
- → CAR mean=54.67, std=2.02, TSR=51.5

Editing the script and CSV now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "c363fd27-7390-4060-b28f-d9aa73c9a609",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7GecmSp9G1B2s446nGWdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18573,
      "cache_read_input_tokens": 28930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18573
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

<details open><summary>🔧 Tool call — Edit · `toolu_0155DEJnqrySt8GCMKT2M13j`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py",
  "old_string": "car_mean = np.array([54.75, 54.5, 56.33, 58.25])\ncar_std  = np.array([3.18, 2.29, 1.61, 0.35])\nseeds    = np.array([2, 3, 3, 2])\ntsr_mean = np.array([51.5, 54.0, 53.83, 48.0])\ncar_se   = car_std / np.sqrt(seeds)\n\nnull_mu, null_sig = 54.6, 2.27",
  "new_string": "car_mean = np.array([54.67, 54.5, 56.33, 57.0])\ncar_std  = np.array([2.02, 2.29, 1.61, 2.18])\nseeds    = np.array([3, 3, 3, 3])\ntsr_mean = np.array([51.5, 54.0, 53.83, 50.17])\ncar_se   = car_std / np.sqrt(seeds)\n\nnull_mu, null_sig = 54.58, 1.93"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "300eaae8-481c-404b-b417-dcd091edacc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A7GecmSp9G1B2s446nGWdL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18573,
      "cache_read_input_tokens": 28930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18573
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

_source line 33 · 2026-05-28T03:05:29.276Z_

<details><summary>↩ Tool result · `toolu_0155DEJnqrySt8GCMKT2M13j`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "12e37cd0-c84f-482c-910f-98aea5733da2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py",
    "oldString": "car_mean = np.array([54.75, 54.5, 56.33, 58.25])\ncar_std  = np.array([3.18, 2.29, 1.61, 0.35])\nseeds    = np.array([2, 3, 3, 2])\ntsr_mean = np.array([51.5, 54.0, 53.83, 48.0])\ncar_se   = car_std / np.sqrt(seeds)\n\nnull_mu, null_sig = 54.6, 2.27",
    "newString": "car_mean = np.array([54.67, 54.5, 56.33, 57.0])\ncar_std  = np.array([2.02, 2.29, 1.61, 2.18])\nseeds    = np.array([3, 3, 3, 3])\ntsr_mean = np.array([51.5, 54.0, 53.83, 50.17])\ncar_se   = car_std / np.sqrt(seeds)\n\nnull_mu, null_sig = 54.58, 1.93",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Fig 5 v4 (final): lambda-CAR/TSR curve with null distribution band.\n\nnarrative_intent: \"SDF geometric supervision is redundant across a 20x\nloss weight range: all lambda values produce CAR within the null distribution band.\"\n\nPatterns: A (null band), D (hollow marker for preliminary), J (path-effect).\n\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.lines import Line2D\nimport numpy as np\nfrom pathlib import Path\n\nOUT = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/'\n           'diff_collision_sdf/artifacts/figures/fig5_lambda_curve')\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 11,\n    'xtick.labelsize': 9.5,\n    'ytick.labelsize': 9.5,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'lines.linewidth': 1.5,\n})\n\nC_CAR = '#0072B2'\nC_TSR = '#D55E00'\nC_NULL = '#CCCCCC'\nSTROKE = [pe.withStroke(linewidth=2.0, foreground='white')]\n\ncar_mean = np.array([54.75, 54.5, 56.33, 58.25])\ncar_std  = np.array([3.18, 2.29, 1.61, 0.35])\nseeds    = np.array([2, 3, 3, 2])\ntsr_mean = np.array([51.5, 54.0, 53.83, 48.0])\ncar_se   = car_std / np.sqrt(seeds)\n\nnull_mu, null_sig = 54.6, 2.27\n\nxpos = np.array([0, 1.8, 2.8, 3.8])\nxlbl = ['0\\n(LoRA-only)', '0.005', '0.01', '0.1']\n\nfig, ax = plt.subplots(figsize=(3.25, 2.5))\n\n# Null distribution band\nax.axhspan(null_mu - null_sig, null_mu + null_sig,\n           color=C_NULL, alpha=0.3, zorder=0)\nax.axhline(null_mu, color='#BBBBBB', ls='--', lw=0.6, zorder=1)\n\n# CAR: lambda=0 isolated, lambda>0 connected\nax.errorbar(xpos[0], car_mean[0], yerr=car_se[0],\n            fmt='o', color=C_CAR, ms=5.5,\n            capsize=3, capthick=0.8, elinewidth=0.8,\n            mec='white', mew=0.6, zorder=4)\nax.errorbar(xpos[1:], car_mean[1:], yerr=car_se[1:],\n            fmt='o-', color=C_CAR, ms=5.5, lw=1.5,\n            capsize=3, capthick=0.8, elinewidth=0.8,\n            mec='white', mew=0.6, zorder=4)\n\n# TSR: lighter weight\nax.plot(xpos[0], tsr_mean[0], 's', color=C_TSR, ms=4.5,\n        mec='white', mew=0.6, alpha=0.75, zorder=3)\nax.plot(xpos[1:], tsr_mean[1:], 's--', color=C_TSR, ms=4.5,\n        mec='white', mew=0.6, alpha=0.75, lw=1.2, zorder=3)\n\n# Seed annotations\nann_cfg = [\n    (10, 0, 'left'),\n    (0, 5, 'center'),\n    (0, 5, 'center'),\n    (0, 5, 'center'),\n]\nfor i in range(4):\n    ox, oy, ha = ann_cfg[i]\n    ref_y = car_mean[i] + car_se[i] if oy >= 0 else car_mean[i]\n    t = ax.annotate(f'n={seeds[i]}',\n                    xy=(xpos[i], ref_y),\n                    xytext=(ox, oy), textcoords='offset points',\n                    fontsize=5.5, color=C_CAR, ha=ha, style='italic')\n    t.set_path_effects(STROKE)\n\n# 20K preliminary\nt20 = ax.annotate('30K†', xy=(xpos[3], tsr_mean[3]),\n                  xytext=(7, -2), textcoords='offset points',\n                  fontsize=5.5, color='#888', style='italic', ha='left')\nt20.set_path_effects(STROKE)\n\n# Null-band label\nt = ax.text(4.2, null_mu, 'null\\n$\\\\pm$1$\\\\sigma$',\n            fontsize=5.5, color='#999', ha='center', va='center',\n            style='italic', linespacing=0.85)\nt.set_path_effects(STROKE)\n\n# Axis break marks\ntrans = ax.get_xaxis_transform()\nfor bx in [0.7, 0.9]:\n    ax.plot([bx, bx + 0.12], [-0.04, 0.04], transform=trans,\n            color='k', lw=0.5, clip_on=False)\n\nax.set_xticks(xpos)\nax.set_xticklabels(xlbl, fontsize=8)\nax.set_xlabel(r'$\\lambda$ (SDF loss weight)', fontsize=10)\nax.set_ylabel('Rate (%)', fontsize=10)\nax.set_xlim(-0.6, 4.6)\nax.set_ylim(46, 60)\n\n# Legend\nhandles = [\n    Line2D([0], [0], marker='o', color=C_CAR, mfc=C_CAR,\n           mec='white', ms=4.5, lw=1.4, ls='-', label='CAR'),\n    Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,\n           mec='white', ms=4, lw=1.1, ls='--', label='TSR'),\n    Line2D([0], [0], marker='o', color='#888', mfc='white',\n           mec='#888', ms=4.5, lw=0, label='2 of 3 seeds†'),\n]\nax.legend(handles=handles, loc='upper left', fontsize=6.5,\n          framealpha=0.92, edgecolor='none', handlelength=1.6,\n          handletextpad=0.5, borderpad=0.35, labelspacing=0.25)\n\nplt.tight_layout()\nOUT.parent.mkdir(parents=True, exist_ok=True)\nfig.savefig(OUT.with_suffix('.pdf'))\nfig.savefig(OUT.with_suffix('.png'))\nplt.close(fig)\nprint(f'Saved: {OUT.with_suffix(\".pdf\")} and {OUT.with_suffix(\".png\")}')\n",
    "structuredPatch": [
      {
        "oldStart": 42,
        "oldLines": 13,
        "newStart": 42,
        "newLines": 13,
        "lines": [
          " C_NULL = '#CCCCCC'",
          " STROKE = [pe.withStroke(linewidth=2.0, foreground='white')]",
          " ",
          "-car_mean = np.array([54.75, 54.5, 56.33, 58.25])",
          "-car_std  = np.array([3.18, 2.29, 1.61, 0.35])",
          "-seeds    = np.array([2, 3, 3, 2])",
          "-tsr_mean = np.array([51.5, 54.0, 53.83, 48.0])",
          "+car_mean = np.array([54.67, 54.5, 56.33, 57.0])",
          "+car_std  = np.array([2.02, 2.29, 1.61, 2.18])",
          "+seeds    = np.array([3, 3, 3, 3])",
          "+tsr_mean = np.array([51.5, 54.0, 53.83, 50.17])",
          " car_se   = car_std / np.sqrt(seeds)",
          " ",
          "-null_mu, null_sig = 54.6, 2.27",
          "+null_mu, null_sig = 54.58, 1.93",
          " ",
          " xpos = np.array([0, 1.8, 2.8, 3.8])",
          " xlbl = ['0\\n(LoRA-only)', '0.005', '0.01', '0.1']"
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_014oZAzzDnvCsCC87m5h8pbk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py",
  "old_string": "# 20K preliminary\nt20 = ax.annotate('30K†', xy=(xpos[3], tsr_mean[3]),\n                  xytext=(7, -2), textcoords='offset points',\n                  fontsize=5.5, color='#888', style='italic', ha='left')\nt20.set_path_effects(STROKE)",
  "new_string": ""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "e5dac90d-60c2-413e-a06b-9e82defbfb96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011v6PqsQbURs6UmkAkDuFuL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8656,
      "cache_read_input_tokens": 47503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8656
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

_source line 35 · 2026-05-28T03:05:34.934Z_

<details><summary>↩ Tool result · `toolu_014oZAzzDnvCsCC87m5h8pbk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "aaaf6e7d-31f2-4f72-aa1b-81cd31a4a62f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py",
    "oldString": "# 20K preliminary\nt20 = ax.annotate('30K†', xy=(xpos[3], tsr_mean[3]),\n                  xytext=(7, -2), textcoords='offset points',\n                  fontsize=5.5, color='#888', style='italic', ha='left')\nt20.set_path_effects(STROKE)",
    "newString": "",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Fig 5 v4 (final): lambda-CAR/TSR curve with null distribution band.\n\nnarrative_intent: \"SDF geometric supervision is redundant across a 20x\nloss weight range: all lambda values produce CAR within the null distribution band.\"\n\nPatterns: A (null band), D (hollow marker for preliminary), J (path-effect).\n\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.lines import Line2D\nimport numpy as np\nfrom pathlib import Path\n\nOUT = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/'\n           'diff_collision_sdf/artifacts/figures/fig5_lambda_curve')\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 11,\n    'xtick.labelsize': 9.5,\n    'ytick.labelsize': 9.5,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'lines.linewidth': 1.5,\n})\n\nC_CAR = '#0072B2'\nC_TSR = '#D55E00'\nC_NULL = '#CCCCCC'\nSTROKE = [pe.withStroke(linewidth=2.0, foreground='white')]\n\ncar_mean = np.array([54.67, 54.5, 56.33, 57.0])\ncar_std  = np.array([2.02, 2.29, 1.61, 2.18])\nseeds    = np.array([3, 3, 3, 3])\ntsr_mean = np.array([51.5, 54.0, 53.83, 50.17])\ncar_se   = car_std / np.sqrt(seeds)\n\nnull_mu, null_sig = 54.58, 1.93\n\nxpos = np.array([0, 1.8, 2.8, 3.8])\nxlbl = ['0\\n(LoRA-only)', '0.005', '0.01', '0.1']\n\nfig, ax = plt.subplots(figsize=(3.25, 2.5))\n\n# Null distribution band\nax.axhspan(null_mu - null_sig, null_mu + null_sig,\n           color=C_NULL, alpha=0.3, zorder=0)\nax.axhline(null_mu, color='#BBBBBB', ls='--', lw=0.6, zorder=1)\n\n# CAR: lambda=0 isolated, lambda>0 connected\nax.errorbar(xpos[0], car_mean[0], yerr=car_se[0],\n            fmt='o', color=C_CAR, ms=5.5,\n            capsize=3, capthick=0.8, elinewidth=0.8,\n            mec='white', mew=0.6, zorder=4)\nax.errorbar(xpos[1:], car_mean[1:], yerr=car_se[1:],\n            fmt='o-', color=C_CAR, ms=5.5, lw=1.5,\n            capsize=3, capthick=0.8, elinewidth=0.8,\n            mec='white', mew=0.6, zorder=4)\n\n# TSR: lighter weight\nax.plot(xpos[0], tsr_mean[0], 's', color=C_TSR, ms=4.5,\n        mec='white', mew=0.6, alpha=0.75, zorder=3)\nax.plot(xpos[1:], tsr_mean[1:], 's--', color=C_TSR, ms=4.5,\n        mec='white', mew=0.6, alpha=0.75, lw=1.2, zorder=3)\n\n# Seed annotations\nann_cfg = [\n    (10, 0, 'left'),\n    (0, 5, 'center'),\n    (0, 5, 'center'),\n    (0, 5, 'center'),\n]\nfor i in range(4):\n    ox, oy, ha = ann_cfg[i]\n    ref_y = car_mean[i] + car_se[i] if oy >= 0 else car_mean[i]\n    t = ax.annotate(f'n={seeds[i]}',\n                    xy=(xpos[i], ref_y),\n                    xytext=(ox, oy), textcoords='offset points',\n                    fontsize=5.5, color=C_CAR, ha=ha, style='italic')\n    t.set_path_effects(STROKE)\n\n# 20K preliminary\nt20 = ax.annotate('30K†', xy=(xpos[3], tsr_mean[3]),\n                  xytext=(7, -2), textcoords='offset points',\n                  fontsize=5.5, color='#888', style='italic', ha='left')\nt20.set_path_effects(STROKE)\n\n# Null-band label\nt = ax.text(4.2, null_mu, 'null\\n$\\\\pm$1$\\\\sigma$',\n            fontsize=5.5, color='#999', ha='center', va='center',\n            style='italic', linespacing=0.85)\nt.set_path_effects(STROKE)\n\n# Axis break marks\ntrans = ax.get_xaxis_transform()\nfor bx in [0.7, 0.9]:\n    ax.plot([bx, bx + 0.12], [-0.04, 0.04], transform=trans,\n            color='k', lw=0.5, clip_on=False)\n\nax.set_xticks(xpos)\nax.set_xticklabels(xlbl, fontsize=8)\nax.set_xlabel(r'$\\lambda$ (SDF loss weight)', fontsize=10)\nax.set_ylabel('Rate (%)', fontsize=10)\nax.set_xlim(-0.6, 4.6)\nax.set_ylim(46, 60)\n\n# Legend\nhandles = [\n    Line2D([0], [0], marker='o', color=C_CAR, mfc=C_CAR,\n           mec='white', ms=4.5, lw=1.4, ls='-', label='CAR'),\n    Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,\n           mec='white', ms=4, lw=1.1, ls='--', label='TSR'),\n    Line2D([0], [0], marker='o', color='#888', mfc='white',\n           mec='#888', ms=4.5, lw=0, label='2 of 3 seeds†'),\n]\nax.legend(handles=handles, loc='upper left', fontsize=6.5,\n          framealpha=0.92, edgecolor='none', handlelength=1.6,\n          handletextpad=0.5, borderpad=0.35, labelspacing=0.25)\n\nplt.tight_layout()\nOUT.parent.mkdir(parents=True, exist_ok=True)\nfig.savefig(OUT.with_suffix('.pdf'))\nfig.savefig(OUT.with_suffix('.png'))\nplt.close(fig)\nprint(f'Saved: {OUT.with_suffix(\".pdf\")} and {OUT.with_suffix(\".png\")}')\n",
    "structuredPatch": [
      {
        "oldStart": 92,
        "oldLines": 11,
        "newStart": 92,
        "newLines": 6,
        "lines": [
          "                     fontsize=5.5, color=C_CAR, ha=ha, style='italic')",
          "     t.set_path_effects(STROKE)",
          " ",
          "-# 20K preliminary",
          "-t20 = ax.annotate('30K†', xy=(xpos[3], tsr_mean[3]),",
          "-                  xytext=(7, -2), textcoords='offset points',",
          "-                  fontsize=5.5, color='#888', style='italic', ha='left')",
          "-t20.set_path_effects(STROKE)",
          " ",
          " # Null-band label",
          " t = ax.text(4.2, null_mu, 'null\\n$\\\\pm$1$\\\\sigma$',"
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

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_011Cy6WjFyy6C7uqp5K86DKE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py",
  "old_string": "handles = [\n    Line2D([0], [0], marker='o', color=C_CAR, mfc=C_CAR,\n           mec='white', ms=4.5, lw=1.4, ls='-', label='CAR'),\n    Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,\n           mec='white', ms=4, lw=1.1, ls='--', label='TSR'),\n    Line2D([0], [0], marker='o', color='#888', mfc='white',\n           mec='#888', ms=4.5, lw=0, label='2 of 3 seeds†'),\n]",
  "new_string": "handles = [\n    Line2D([0], [0], marker='o', color=C_CAR, mfc=C_CAR,\n           mec='white', ms=4.5, lw=1.4, ls='-', label='CAR'),\n    Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,\n           mec='white', ms=4, lw=1.1, ls='--', label='TSR'),\n]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "d3a39891-79d9-444e-b102-456a0c7bc934",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAd7dxuMzXup5nYfKmRUyE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 289,
      "cache_read_input_tokens": 56159,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 289
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

_source line 37 · 2026-05-28T03:05:41.593Z_

<details><summary>↩ Tool result · `toolu_011Cy6WjFyy6C7uqp5K86DKE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "ef93851f-c6f2-4311-850f-a8976f5c754f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py",
    "oldString": "handles = [\n    Line2D([0], [0], marker='o', color=C_CAR, mfc=C_CAR,\n           mec='white', ms=4.5, lw=1.4, ls='-', label='CAR'),\n    Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,\n           mec='white', ms=4, lw=1.1, ls='--', label='TSR'),\n    Line2D([0], [0], marker='o', color='#888', mfc='white',\n           mec='#888', ms=4.5, lw=0, label='2 of 3 seeds†'),\n]",
    "newString": "handles = [\n    Line2D([0], [0], marker='o', color=C_CAR, mfc=C_CAR,\n           mec='white', ms=4.5, lw=1.4, ls='-', label='CAR'),\n    Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,\n           mec='white', ms=4, lw=1.1, ls='--', label='TSR'),\n]",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Fig 5 v4 (final): lambda-CAR/TSR curve with null distribution band.\n\nnarrative_intent: \"SDF geometric supervision is redundant across a 20x\nloss weight range: all lambda values produce CAR within the null distribution band.\"\n\nPatterns: A (null band), D (hollow marker for preliminary), J (path-effect).\n\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.lines import Line2D\nimport numpy as np\nfrom pathlib import Path\n\nOUT = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/'\n           'diff_collision_sdf/artifacts/figures/fig5_lambda_curve')\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 11,\n    'xtick.labelsize': 9.5,\n    'ytick.labelsize': 9.5,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'lines.linewidth': 1.5,\n})\n\nC_CAR = '#0072B2'\nC_TSR = '#D55E00'\nC_NULL = '#CCCCCC'\nSTROKE = [pe.withStroke(linewidth=2.0, foreground='white')]\n\ncar_mean = np.array([54.67, 54.5, 56.33, 57.0])\ncar_std  = np.array([2.02, 2.29, 1.61, 2.18])\nseeds    = np.array([3, 3, 3, 3])\ntsr_mean = np.array([51.5, 54.0, 53.83, 50.17])\ncar_se   = car_std / np.sqrt(seeds)\n\nnull_mu, null_sig = 54.58, 1.93\n\nxpos = np.array([0, 1.8, 2.8, 3.8])\nxlbl = ['0\\n(LoRA-only)', '0.005', '0.01', '0.1']\n\nfig, ax = plt.subplots(figsize=(3.25, 2.5))\n\n# Null distribution band\nax.axhspan(null_mu - null_sig, null_mu + null_sig,\n           color=C_NULL, alpha=0.3, zorder=0)\nax.axhline(null_mu, color='#BBBBBB', ls='--', lw=0.6, zorder=1)\n\n# CAR: lambda=0 isolated, lambda>0 connected\nax.errorbar(xpos[0], car_mean[0], yerr=car_se[0],\n            fmt='o', color=C_CAR, ms=5.5,\n            capsize=3, capthick=0.8, elinewidth=0.8,\n            mec='white', mew=0.6, zorder=4)\nax.errorbar(xpos[1:], car_mean[1:], yerr=car_se[1:],\n            fmt='o-', color=C_CAR, ms=5.5, lw=1.5,\n            capsize=3, capthick=0.8, elinewidth=0.8,\n            mec='white', mew=0.6, zorder=4)\n\n# TSR: lighter weight\nax.plot(xpos[0], tsr_mean[0], 's', color=C_TSR, ms=4.5,\n        mec='white', mew=0.6, alpha=0.75, zorder=3)\nax.plot(xpos[1:], tsr_mean[1:], 's--', color=C_TSR, ms=4.5,\n        mec='white', mew=0.6, alpha=0.75, lw=1.2, zorder=3)\n\n# Seed annotations\nann_cfg = [\n    (10, 0, 'left'),\n    (0, 5, 'center'),\n    (0, 5, 'center'),\n    (0, 5, 'center'),\n]\nfor i in range(4):\n    ox, oy, ha = ann_cfg[i]\n    ref_y = car_mean[i] + car_se[i] if oy >= 0 else car_mean[i]\n    t = ax.annotate(f'n={seeds[i]}',\n                    xy=(xpos[i], ref_y),\n                    xytext=(ox, oy), textcoords='offset points',\n                    fontsize=5.5, color=C_CAR, ha=ha, style='italic')\n    t.set_path_effects(STROKE)\n\n\n# Null-band label\nt = ax.text(4.2, null_mu, 'null\\n$\\\\pm$1$\\\\sigma$',\n            fontsize=5.5, color='#999', ha='center', va='center',\n            style='italic', linespacing=0.85)\nt.set_path_effects(STROKE)\n\n# Axis break marks\ntrans = ax.get_xaxis_transform()\nfor bx in [0.7, 0.9]:\n    ax.plot([bx, bx + 0.12], [-0.04, 0.04], transform=trans,\n            color='k', lw=0.5, clip_on=False)\n\nax.set_xticks(xpos)\nax.set_xticklabels(xlbl, fontsize=8)\nax.set_xlabel(r'$\\lambda$ (SDF loss weight)', fontsize=10)\nax.set_ylabel('Rate (%)', fontsize=10)\nax.set_xlim(-0.6, 4.6)\nax.set_ylim(46, 60)\n\n# Legend\nhandles = [\n    Line2D([0], [0], marker='o', color=C_CAR, mfc=C_CAR,\n           mec='white', ms=4.5, lw=1.4, ls='-', label='CAR'),\n    Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,\n           mec='white', ms=4, lw=1.1, ls='--', label='TSR'),\n    Line2D([0], [0], marker='o', color='#888', mfc='white',\n           mec='#888', ms=4.5, lw=0, label='2 of 3 seeds†'),\n]\nax.legend(handles=handles, loc='upper left', fontsize=6.5,\n          framealpha=0.92, edgecolor='none', handlelength=1.6,\n          handletextpad=0.5, borderpad=0.35, labelspacing=0.25)\n\nplt.tight_layout()\nOUT.parent.mkdir(parents=True, exist_ok=True)\nfig.savefig(OUT.with_suffix('.pdf'))\nfig.savefig(OUT.with_suffix('.png'))\nplt.close(fig)\nprint(f'Saved: {OUT.with_suffix(\".pdf\")} and {OUT.with_suffix(\".png\")}')\n",
    "structuredPatch": [
      {
        "oldStart": 118,
        "oldLines": 8,
        "newStart": 118,
        "newLines": 6,
        "lines": [
          "            mec='white', ms=4.5, lw=1.4, ls='-', label='CAR'),",
          "     Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,",
          "            mec='white', ms=4, lw=1.1, ls='--', label='TSR'),",
          "-    Line2D([0], [0], marker='o', color='#888', mfc='white',",
          "-           mec='#888', ms=4.5, lw=0, label='2 of 3 seeds†'),",
          " ]",
          " ax.legend(handles=handles, loc='upper left', fontsize=6.5,",
          "           framealpha=0.92, edgecolor='none', handlelength=1.6,"
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

_source line 38_

Now update the CSV.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "94c3bfff-bf0d-46c5-bd9d-2d5804abdd58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EjXMkiBqGMuKbLw4RQtvCN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 56448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 500
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

<details open><summary>🔧 Tool call — Edit · `toolu_01E217p9oBKCyk8T5P6J8AEQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig5_lambda_data.csv",
  "old_string": "0,54.75,3.18,\"57.0;52.5\",48.75,,30K,LoRA-only (no SDF)",
  "new_string": "0,54.67,2.02,\"56.5;52.5;55.0\",51.5,,30K,LoRA-only (no SDF) 3 seeds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "fc517ec5-b813-412b-abfc-442cd1637c47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EjXMkiBqGMuKbLw4RQtvCN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 56448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 500
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

_source line 40 · 2026-05-28T03:05:48.668Z_

<details><summary>↩ Tool result · `toolu_01E217p9oBKCyk8T5P6J8AEQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig5_lambda_data.csv has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "d26e0148-0069-4531-8cab-04aab9cdc2ba",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig5_lambda_data.csv",
    "oldString": "0,54.75,3.18,\"57.0;52.5\",48.75,,30K,LoRA-only (no SDF)",
    "newString": "0,54.67,2.02,\"56.5;52.5;55.0\",51.5,,30K,LoRA-only (no SDF) 3 seeds",
    "originalFile": "lambda,CAR_mean,CAR_std,CAR_seeds,TSR_mean,TSR_std,step,note\n0,54.75,3.18,\"57.0;52.5\",48.75,,30K,LoRA-only (no SDF)\n0.005,54.5,2.29,\"57.0;54.0;52.5\",54.0,3.0,30K,3 seeds\n0.01,56.33,1.61,\"57.0;57.5;54.5\",53.83,1.5,30K,3 seeds\n0.1,58.25,0.35,\"58.0;58.5\",48.0,1.4,30K,2 seeds 30K\n\n# step-wise sub-table (for inset or supplementary)\n# lambda,step,CAR,TSR,seed,note\n# 0.1,16000,pending,pending,0,best loss checkpoint eval running\n# 0.1,20000,55,54,0,early signal\n# 0.1,20000,56,51,1,early signal\n# 0.1,22000,pending,pending,0,next after 16K\n# 0.1,30000,pending,pending,0,training ~17:00 UTC\n# 0.1,30000,pending,pending,1,training ~17:30 UTC\n# 0.1,30000,pending,pending,2,training ~08:00 UTC 5/28\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          " lambda,CAR_mean,CAR_std,CAR_seeds,TSR_mean,TSR_std,step,note",
          "-0,54.75,3.18,\"57.0;52.5\",48.75,,30K,LoRA-only (no SDF)",
          "+0,54.67,2.02,\"56.5;52.5;55.0\",51.5,,30K,LoRA-only (no SDF) 3 seeds",
          " 0.005,54.5,2.29,\"57.0;54.0;52.5\",54.0,3.0,30K,3 seeds",
          " 0.01,56.33,1.61,\"57.0;57.5;54.5\",53.83,1.5,30K,3 seeds",
          " 0.1,58.25,0.35,\"58.0;58.5\",48.0,1.4,30K,2 seeds 30K"
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

<details open><summary>🔧 Tool call — Edit · `toolu_017vGCJreKAp9HFgsTUempt6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig5_lambda_data.csv",
  "old_string": "0.1,58.25,0.35,\"58.0;58.5\",48.0,1.4,30K,2 seeds 30K",
  "new_string": "0.1,57.0,2.18,\"58.0;58.5;54.5\",50.17,3.88,30K,3 seeds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "95521065-a86e-4049-a0cf-5b2c2c02957c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BkehbjWEGHoYwDNqEn18Lz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 56948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 286
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

_source line 42 · 2026-05-28T03:05:53.139Z_

<details><summary>↩ Tool result · `toolu_017vGCJreKAp9HFgsTUempt6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig5_lambda_data.csv has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "809b589b-92a6-4a79-aa87-9d75cc4b624b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig5_lambda_data.csv",
    "oldString": "0.1,58.25,0.35,\"58.0;58.5\",48.0,1.4,30K,2 seeds 30K",
    "newString": "0.1,57.0,2.18,\"58.0;58.5;54.5\",50.17,3.88,30K,3 seeds",
    "originalFile": "lambda,CAR_mean,CAR_std,CAR_seeds,TSR_mean,TSR_std,step,note\n0,54.67,2.02,\"56.5;52.5;55.0\",51.5,,30K,LoRA-only (no SDF) 3 seeds\n0.005,54.5,2.29,\"57.0;54.0;52.5\",54.0,3.0,30K,3 seeds\n0.01,56.33,1.61,\"57.0;57.5;54.5\",53.83,1.5,30K,3 seeds\n0.1,58.25,0.35,\"58.0;58.5\",48.0,1.4,30K,2 seeds 30K\n\n# step-wise sub-table (for inset or supplementary)\n# lambda,step,CAR,TSR,seed,note\n# 0.1,16000,pending,pending,0,best loss checkpoint eval running\n# 0.1,20000,55,54,0,early signal\n# 0.1,20000,56,51,1,early signal\n# 0.1,22000,pending,pending,0,next after 16K\n# 0.1,30000,pending,pending,0,training ~17:00 UTC\n# 0.1,30000,pending,pending,1,training ~17:30 UTC\n# 0.1,30000,pending,pending,2,training ~08:00 UTC 5/28\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " 0,54.67,2.02,\"56.5;52.5;55.0\",51.5,,30K,LoRA-only (no SDF) 3 seeds",
          " 0.005,54.5,2.29,\"57.0;54.0;52.5\",54.0,3.0,30K,3 seeds",
          " 0.01,56.33,1.61,\"57.0;57.5;54.5\",53.83,1.5,30K,3 seeds",
          "-0.1,58.25,0.35,\"58.0;58.5\",48.0,1.4,30K,2 seeds 30K",
          "+0.1,57.0,2.18,\"58.0;58.5;54.5\",50.17,3.88,30K,3 seeds",
          " ",
          " # step-wise sub-table (for inset or supplementary)",
          " # lambda,step,CAR,TSR,seed,note"
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

_source line 43_

Run the script to generate the updated figure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "bc3321ea-4ad5-4170-ada2-6b4d4da7c619",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01992rkLMEvyYBi2uvkB6pUr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 57234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 278
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

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_01EFEab9W49pAv5xocaHJ64b`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures && python3 plot_fig5.py",
  "description": "Generate updated fig5 lambda curve"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "726d8882-eb31-4feb-b86b-89990dd5091c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01992rkLMEvyYBi2uvkB6pUr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 278,
      "cache_read_input_tokens": 57234,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 278
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

_source line 45 · 2026-05-28T03:05:59.520Z_

<details><summary>↩ Tool result · `toolu_01EFEab9W49pAv5xocaHJ64b`</summary>

```text
Saved: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.pdf and /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "efba1025-776f-4a9e-9a9b-b74e652720e1",
  "tool_use_result": {
    "stdout": "Saved: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.pdf and /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.png",
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

_source line 46_

Verify the outputs exist and preview the PNG.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "10dffe6f-78bc-4c69-b426-2ff5ad3af2a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xkEtFUqXeoLNzdKrzFN8q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 57512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 328
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

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01JN6FVUjh7RjodyeJtoJ926`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.{pdf,png}",
  "description": "Verify output files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "6f34f32a-dda9-48e3-8de0-792a6607d4f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xkEtFUqXeoLNzdKrzFN8q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 57512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 328
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

_source line 48 · 2026-05-28T03:06:03.154Z_

<details><summary>↩ Tool result · `toolu_01JN6FVUjh7RjodyeJtoJ926`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 22997 May 28 03:05 /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.pdf
-rw-r--r-- 1 ubuntu ubuntu 54255 May 28 03:05 /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "c1de65c7-d1f5-4c35-9956-3e26c87eaf27",
  "tool_use_result": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 22997 May 28 03:05 /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.pdf\n-rw-r--r-- 1 ubuntu ubuntu 54255 May 28 03:05 /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.png",
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

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01UgJZmm4n3dPiPv1P8WGde6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "791d6f07-1d51-4d2c-81c4-6b6f6e27e0a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xkEtFUqXeoLNzdKrzFN8q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 57512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 328
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

_source line 50 · 2026-05-28T03:06:03.335Z_

<details><summary>↩ Tool result · `toolu_01UgJZmm4n3dPiPv1P8WGde6`</summary>

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
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "b903d8db-1210-43bd-83b5-d9c97084d7f8",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 54255,
      "dimensions": {
        "originalWidth": 906,
        "originalHeight": 681,
        "displayWidth": 906,
        "displayHeight": 681
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
The figure looks good. All data points now show n=3, the "30K†" annotation and "2 of 3 seeds†" legend entry have been removed. The null band is updated. The λ=0.1 point now has a proper error bar (was barely visible before with std=0.35, now shows std=2.18). 

Let me verify the final state of both files quickly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "5ed00a0d-6f55-4415-bf8d-518dfd7820f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ph97viM2FeEhYwyBe7gV5E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1230,
      "cache_read_input_tokens": 57840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1230
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

_source line 52_

完成。所有更新：

| 数据点 | 旧值 | 新值 |
|--------|------|------|
| LoRA CAR | 54.75±3.18 (n=2) | 54.67±2.02 (n=3) |
| λ=0.1 CAR | 58.25±0.35 (n=2) | 57.0±2.18 (n=3) |
| λ=0.1 TSR | 48.0 | 50.17 |
| null band | μ=54.6, σ=2.27 | μ=54.58, σ=1.93 |

清理：移除了 "2 of 3 seeds†" 图例项和 "30K†" 标注（所有点均为 n=3）。CSV 已同步更新。PDF/PNG 已生成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "uuid": "3e04d65b-0c61-4d5c-b097-76b66dc81a91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ph97viM2FeEhYwyBe7gV5E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1230,
      "cache_read_input_tokens": 57840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1230
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

_source line 53_

完成。所有更新：

| 数据点 | 旧值 | 新值 |
|--------|------|------|
| LoRA CAR | 54.75±3.18 (n=2) | 54.67±2.02 (n=3) |
| λ=0.1 CAR | 58.25±0.35 (n=2) | 57.0±2.18 (n=3) |
| λ=0.1 TSR | 48.0 | 50.17 |
| null band | μ=54.6, σ=2.27 | μ=54.58, σ=1.93 |

清理：移除了 "2 of 3 seeds†" 图例项和 "30K†" 标注（所有点均为 n=3）。CSV 已同步更新。PDF/PNG 已生成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 221386,
  "duration_api_ms": 220274,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "68d6d231-fd02-4b68-9910-f9e35d773ce7",
  "total_cost_usd": 0.82951125,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 47619,
    "cache_read_input_tokens": 481605,
    "output_tokens": 11556,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 47619,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 344,
        "cache_read_input_tokens": 57840,
        "cache_creation_input_tokens": 1230,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1230
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2015,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0021149999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 11556,
      "cacheReadInputTokens": 481605,
      "cacheCreationInputTokens": 47619,
      "webSearchRequests": 0,
      "costUSD": 0.82739625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5bc2006a-5c09-4f09-8279-e90f18057698"
}
```

</details>

---
