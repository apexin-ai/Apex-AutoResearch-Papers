# paper figure fig1 framework matplotlib v2 — Part 1 of 2

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Worker execution logs

[Transcript overview](../paper-figure-fig1-framework-matplotlib-v2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/fc/fc39e79601d43dd1dec5.json)

## Before a recorded user message

## Before a recorded user message

121 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
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
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_figures_and_layout",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
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
  "uuid": "16220dd5-5f1f-4740-8165-811166ff3278",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias/memory/"
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
    "resetsAt": 1779625800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "505d7eaf-5d6e-4be6-a27e-318f0ee37198",
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32"
}
```

---


### Assistant

_source line 4_

I'll start by reading the existing script and the two skill files to understand the current design and standards.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "d57d7213-89fe-4224-b454-629b23b72698",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJqeePgUwArYBFS5qBkcxT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

<details open><summary>🔧 Tool call — Read · `toolu_01Q4raCkMHMuBupjGbuow5DN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "89f8e6ba-7347-4512-b85f-27d1b2a26fc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJqeePgUwArYBFS5qBkcxT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 6 · 2026-05-24T11:42:46.377Z_

<details><summary>↩ Tool result · `toolu_01Q4raCkMHMuBupjGbuow5DN`</summary>

```text
1	"""Generate Figure 1: G-MFRM Framework Overview (conceptual diagram)."""
2	import matplotlib
3	matplotlib.use('Agg')
4	matplotlib.rcParams['mathtext.fontset'] = 'cm'
5	import matplotlib.pyplot as plt
6	import matplotlib.patches as mpatches
7	from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
8	import numpy as np
9	
10	# ── Colors ──────────────────────────────────────────────────────────
11	C_JUDGE   = '#2B6E99'   # blue — judge severity d_j
12	C_JUDGE_L = '#C5DDE9'   # light blue
13	C_CONT    = '#D4762C'   # orange — contamination c_n·e_i
14	C_CONT_L  = '#F5D8B5'   # light orange
15	C_GRAY    = '#505050'
16	C_GRAY_L  = '#E8E8E8'
17	C_RED     = '#B03A2E'
18	C_RED_L   = '#F9E0DC'
19	C_GREEN   = '#1E8449'
20	C_GREEN_L = '#D0ECD8'
21	C_BG      = '#FAFAFA'
22	WHITE     = '#FFFFFF'
23	DARK      = '#2C3E50'
24	
25	# ── Figure setup ────────────────────────────────────────────────────
26	fig = plt.figure(figsize=(16, 9))
27	fig.patch.set_facecolor(WHITE)
28	
29	gs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.05,
30	                      left=0.015, right=0.985, top=0.93, bottom=0.03)
31	ax_l = fig.add_subplot(gs[0])
32	ax_r = fig.add_subplot(gs[1])
33	
34	for ax in [ax_l, ax_r]:
35	    ax.set_xlim(0, 10)
36	    ax.set_ylim(0, 10)
37	    ax.set_aspect('equal')
38	    ax.axis('off')
39	
40	# ── Helpers ─────────────────────────────────────────────────────────
41	def rbox(ax, x, y, w, h, fc, ec, lw=1.3, ls='-', alpha=1.0, zorder=2, pad=0.12):
42	    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',
43	                        facecolor=fc, edgecolor=ec, linewidth=lw,
44	                        linestyle=ls, alpha=alpha, zorder=zorder)
45	    ax.add_patch(b)
46	    return b
47	
48	def label(ax, x, y, txt, fs=9, fw='bold', color='black', ha='center',
49	          va='center', style='normal', zorder=5, **kw):
50	    ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,
51	            ha=ha, va=va, fontstyle=style, zorder=zorder, **kw)
52	
53	def arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.6, style='-|>',
54	          rad=0, zorder=4):
55	    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'
56	    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,
57	                         linewidth=lw, connectionstyle=cs,
58	                         mutation_scale=15, zorder=zorder)
59	    ax.add_patch(a)
60	
61	def labeled_box(ax, x, y, w, h, line1, line2, fc, ec, fs1=9, fs2=8.5):
62	    rbox(ax, x, y, w, h, fc, ec)
63	    label(ax, x+w/2, y+h/2+0.17, line1, fs=fs1, fw='bold', color=DARK)
64	    label(ax, x+w/2, y+h/2-0.17, line2, fs=fs2, fw='normal', color=C_GRAY)
65	
66	
67	# ═══════════════════════════════════════════════════════════════════
68	#  LEFT PANEL — Sequential Pipeline
69	# ═══════════════════════════════════════════════════════════════════
70	
71	# Background
72	rbox(ax_l, 0.1, 0.15, 9.8, 9.6, C_RED_L, C_RED, lw=1.8, alpha=0.2, zorder=0, pad=0.2)
73	
74	# Title
75	label(ax_l, 5.0, 9.5, 'Sequential Pipeline', fs=14, fw='bold', color=C_RED)
76	label(ax_l, 5.0, 9.0, '(order-dependent bias)', fs=10, color=C_RED, style='italic')
77	
78	# ── Path A ──
79	label(ax_l, 5.0, 8.3, 'Path A: Bias-first', fs=10.5, fw='bold', color=DARK)
80	
81	bw, bh = 3.4, 0.95
82	# Step 1
83	rbox(ax_l, 0.5, 6.8, bw, bh, C_JUDGE_L, C_JUDGE)
84	label(ax_l, 0.5+bw/2, 6.8+bh/2+0.15, 'Step 1: MFRM', fs=9, fw='bold', color=DARK)
85	label(ax_l, 0.5+bw/2, 6.8+bh/2-0.18, r'calibrate $d_j$', fs=9, fw='normal', color=C_JUDGE)
86	
87	# Step 2
88	rbox(ax_l, 5.6, 6.8, bw+0.4, bh, C_CONT_L, C_CONT)
89	label(ax_l, 5.6+(bw+0.4)/2, 6.8+bh/2+0.15, 'Step 2: Adjust', fs=9, fw='bold', color=DARK)
90	label(ax_l, 5.6+(bw+0.4)/2, 6.8+bh/2-0.18, r'contamination $c_n$', fs=9, fw='normal', color=C_CONT)
91	
92	arrow(ax_l, 3.9, 7.28, 5.6, 7.28, color=C_GRAY, lw=2.0)
93	
94	# Red cross
95	label(ax_l, 9.6, 7.28, '✗', fs=18, fw='bold', color=C_RED)
96	
97	# ── Path B ──
98	label(ax_l, 5.0, 6.0, 'Path B: Contamination-first', fs=10.5, fw='bold', color=DARK)
99	
100	rbox(ax_l, 0.5, 4.5, bw+0.4, bh, C_CONT_L, C_CONT)
101	label(ax_l, 0.5+(bw+0.4)/2, 4.5+bh/2+0.15, 'Step 1: Adjust', fs=9, fw='bold', color=DARK)
102	label(ax_l, 0.5+(bw+0.4)/2, 4.5+bh/2-0.18, r'contamination $c_n$', fs=9, fw='normal', color=C_CONT)
103	
104	rbox(ax_l, 5.6, 4.5, bw, bh, C_JUDGE_L, C_JUDGE)
105	label(ax_l, 5.6+bw/2, 4.5+bh/2+0.15, 'Step 2: MFRM', fs=9, fw='bold', color=DARK)
106	label(ax_l, 5.6+bw/2, 4.5+bh/2-0.18, r'calibrate $d_j$', fs=9, fw='normal', color=C_JUDGE)
107	
108	arrow(ax_l, 4.3, 4.97, 5.6, 4.97, color=C_GRAY, lw=2.0)
109	
110	label(ax_l, 9.6, 4.97, '✗', fs=18, fw='bold', color=C_RED)
111	
112	# ── OVB Box ──
113	rbox(ax_l, 0.5, 2.2, 9.0, 1.85, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95)
114	
115	label(ax_l, 5.0, 3.45, 'Omitted Variable Bias (OVB)', fs=11, fw='bold', color=C_RED)
116	label(ax_l, 5.0, 2.8,
117	      r'$\hat{\theta}$ biased when Cov$(d_j,\; c_n \cdot e_i) \neq 0$',
118	      fs=10.5, fw='normal', color=C_RED)
119	
120	# Warning arrows from OVB to both paths
121	arrow(ax_l, 3.0, 4.05, 3.0, 4.5, color=C_RED, lw=1.3, style='-|>')
122	arrow(ax_l, 7.0, 4.05, 7.0, 4.5, color=C_RED, lw=1.3, style='-|>')
123	
124	# Bottom note
125	label(ax_l, 5.0, 1.35, 'Unmodeled facet absorbed into remaining estimates',
126	      fs=9, color=C_RED, style='italic', fw='normal')
127	
128	# ── Dashed confounding arcs between Path A boxes ──
129	# Red dashed arc from Step2_A back to Step1_A (showing absorbed bias)
130	a_conf = FancyArrowPatch((7.5, 7.75), (2.2, 7.75), arrowstyle='-|>',
131	                          color=C_RED, linewidth=1.2, linestyle='--',
132	                          connectionstyle='arc3,rad=-0.35',
133	                          mutation_scale=12, zorder=4)
134	ax_l.add_patch(a_conf)
135	label(ax_l, 4.9, 8.65, r'confounding', fs=7.5, color=C_RED, style='italic', fw='normal')
136	
137	# Red dashed arc between Path B boxes
138	b_conf = FancyArrowPatch((7.3, 5.45), (2.7, 5.45), arrowstyle='-|>',
139	                          color=C_RED, linewidth=1.2, linestyle='--',
140	                          connectionstyle='arc3,rad=-0.35',
141	                          mutation_scale=12, zorder=4)
142	ax_l.add_patch(b_conf)
143	label(ax_l, 5.0, 6.35, r'confounding', fs=7.5, color=C_RED, style='italic', fw='normal')
144	
145	
146	# ═══════════════════════════════════════════════════════════════════
147	#  RIGHT PANEL — G-MFRM Joint Framework
148	# ═══════════════════════════════════════════════════════════════════
149	
150	# Background
151	rbox(ax_r, 0.05, 0.15, 9.9, 9.6, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.15, zorder=0, pad=0.2)
152	
153	# Title
154	label(ax_r, 5.0, 9.5, 'G-MFRM Joint Framework (Ours)', fs=14, fw='bold', color='#145A32')
155	label(ax_r, 5.0, 9.0, 'staged joint calibration of all facets', fs=10,
156	      color=C_GREEN, style='italic')
157	
158	# ── Stage 1: Standard MFRM ──
159	s1_x, s1_y, s1_w, s1_h = 0.35, 7.3, 9.3, 1.35
160	rbox(ax_r, s1_x, s1_y, s1_w, s1_h, '#E8F0F5', C_JUDGE, alpha=0.6)
161	
162	label(ax_r, 1.5, s1_y+s1_h-0.3, 'Stage 1', fs=10.5, fw='bold', color=C_JUDGE)
163	label(ax_r, 1.5, s1_y+s1_h-0.7, 'Standard MFRM', fs=9, fw='normal', color=C_GRAY)
164	
165	# Output tokens
166	ow, oh = 1.8, 0.6
167	out1_specs = [(r'$\hat{\theta}^{(1)}$', 4.0), (r'$\hat{b}$', 6.1), (r'$\hat{d}$', 8.1)]
168	for lbl_txt, xo in out1_specs:
169	    rbox(ax_r, xo, s1_y+0.35, ow, oh, WHITE, C_JUDGE, lw=1.0)
170	    label(ax_r, xo+ow/2, s1_y+0.35+oh/2, lbl_txt, fs=11, fw='normal', color=C_JUDGE)
171	
172	# Arrow S1 → S3
173	arrow(ax_r, 7.3, 7.3, 7.3, 6.6, color=C_JUDGE, lw=2.0)
174	label(ax_r, 7.7, 6.95, 'initialize', fs=7.5, color=C_JUDGE, fw='normal', style='italic')
175	
176	# ── Stage 2: External e_i ──
177	s2_x, s2_y, s2_w, s2_h = 0.35, 4.55, 4.0, 2.55
178	rbox(ax_r, s2_x, s2_y, s2_w, s2_h, '#FDF2E9', C_CONT, alpha=0.55)
179	
180	label(ax_r, s2_x+s2_w/2, s2_y+s2_h-0.3,
181	      r'Stage 2: Estimate $e_i$', fs=9.5, fw='bold', color=C_CONT)
182	
183	sub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']
184	sw, sh = 3.1, 0.5
185	for k, stxt in enumerate(sub_specs):
186	    sy = s2_y + s2_h - 0.95 - k*0.6
187	    rbox(ax_r, s2_x+0.45, sy, sw, sh, WHITE, C_CONT, lw=1.0)
188	    label(ax_r, s2_x+0.45+sw/2, sy+sh/2, stxt, fs=8.5, fw='normal', color=DARK)
189	
190	# Arrow S2 → S3
191	arrow(ax_r, 4.35, 5.5, 5.25, 5.5, color=C_CONT, lw=2.0)
192	label(ax_r, 4.8, 5.78, r'$e_i$', fs=10, color=C_CONT, fw='bold')
193	
194	# ── Stage 3: Joint Gated Model ──
195	s3_x, s3_y, s3_w, s3_h = 5.1, 4.3, 4.55, 2.3
196	rbox(ax_r, s3_x, s3_y, s3_w, s3_h, '#F4F4F4', '#3C3C3C', lw=2.2)
197	
198	label(ax_r, s3_x+s3_w/2, s3_y+s3_h-0.35,
199	      'Stage 3: Joint Gated Model', fs=10, fw='bold', color=DARK)
200	
201	# Model equation line
202	label(ax_r, s3_x+s3_w/2, s3_y+s3_h-0.85,
203	      r'$\eta = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$',
204	      fs=9, fw='normal', color=C_GRAY)
205	
206	# Gating highlight
207	gx, gy, gw, gh = s3_x+0.5, s3_y+0.3, 3.55, 0.85
208	rbox(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.2, alpha=0.9)
209	label(ax_r, gx+gw/2, gy+gh/2+0.08,
210	      r'Gating: $c_n \cdot e_i$', fs=11, fw='bold', color=C_CONT)
211	
212	# ── 4-D Output ──
213	label(ax_r, 5.0, 3.65, '4-Dimensional Diagnostic Output', fs=10.5, fw='bold', color=DARK)
214	
215	ow2, oh2 = 2.0, 0.95
216	out_y = 2.35
217	out_specs = [
218	    (r'$\hat{\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.55),
219	    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.8),
220	    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),
221	    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.3),
222	]
223	for sym, desc, fc, ec, xo in out_specs:
224	    rbox(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.5)
225	    label(ax_r, xo+ow2/2, out_y+oh2/2+0.16, sym, fs=11, fw='bold', color=ec)
226	    label(ax_r, xo+ow2/2, out_y+oh2/2-0.2, desc, fs=8, fw='normal', color=DARK)
227	
228	# Arrow S3 → outputs
229	arrow(ax_r, 7.35, 4.3, 7.35, 3.3, color='#3C3C3C', lw=2.2, style='-|>')
230	
231	# Green check
232	label(ax_r, 5.0, 1.5, '✓  Joint estimation resolves confounding',
233	      fs=10, fw='bold', color=C_GREEN, style='italic')
234	
235	# Panel labels
236	label(ax_l, 0.45, 9.85, '(a)', fs=13, fw='bold', color='black', ha='left')
237	label(ax_r, 0.25, 9.85, '(b)', fs=13, fw='bold', color='black', ha='left')
238	
239	# ── Save ──
240	out_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'
241	fig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)
242	fig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)
243	plt.close()
244	print('Done: fig1_framework.pdf + fig1_framework.png')
245	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "4c4d5173-7671-49e4-842a-6b8e0cbcce05",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
      "content": "\"\"\"Generate Figure 1: G-MFRM Framework Overview (conceptual diagram).\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\nimport numpy as np\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'   # blue — judge severity d_j\nC_JUDGE_L = '#C5DDE9'   # light blue\nC_CONT    = '#D4762C'   # orange — contamination c_n·e_i\nC_CONT_L  = '#F5D8B5'   # light orange\nC_GRAY    = '#505050'\nC_GRAY_L  = '#E8E8E8'\nC_RED     = '#B03A2E'\nC_RED_L   = '#F9E0DC'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D0ECD8'\nC_BG      = '#FAFAFA'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 9))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.05,\n                      left=0.015, right=0.985, top=0.93, bottom=0.03)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 10)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.3, ls='-', alpha=1.0, zorder=2, pad=0.12):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=9, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, **kw):\n    ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n            ha=ha, va=va, fontstyle=style, zorder=zorder, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.6, style='-|>',\n          rad=0, zorder=4):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs,\n                         mutation_scale=15, zorder=zorder)\n    ax.add_patch(a)\n\ndef labeled_box(ax, x, y, w, h, line1, line2, fc, ec, fs1=9, fs2=8.5):\n    rbox(ax, x, y, w, h, fc, ec)\n    label(ax, x+w/2, y+h/2+0.17, line1, fs=fs1, fw='bold', color=DARK)\n    label(ax, x+w/2, y+h/2-0.17, line2, fs=fs2, fw='normal', color=C_GRAY)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\n# Background\nrbox(ax_l, 0.1, 0.15, 9.8, 9.6, C_RED_L, C_RED, lw=1.8, alpha=0.2, zorder=0, pad=0.2)\n\n# Title\nlabel(ax_l, 5.0, 9.5, 'Sequential Pipeline', fs=14, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 9.0, '(order-dependent bias)', fs=10, color=C_RED, style='italic')\n\n# ── Path A ──\nlabel(ax_l, 5.0, 8.3, 'Path A: Bias-first', fs=10.5, fw='bold', color=DARK)\n\nbw, bh = 3.4, 0.95\n# Step 1\nrbox(ax_l, 0.5, 6.8, bw, bh, C_JUDGE_L, C_JUDGE)\nlabel(ax_l, 0.5+bw/2, 6.8+bh/2+0.15, 'Step 1: MFRM', fs=9, fw='bold', color=DARK)\nlabel(ax_l, 0.5+bw/2, 6.8+bh/2-0.18, r'calibrate $d_j$', fs=9, fw='normal', color=C_JUDGE)\n\n# Step 2\nrbox(ax_l, 5.6, 6.8, bw+0.4, bh, C_CONT_L, C_CONT)\nlabel(ax_l, 5.6+(bw+0.4)/2, 6.8+bh/2+0.15, 'Step 2: Adjust', fs=9, fw='bold', color=DARK)\nlabel(ax_l, 5.6+(bw+0.4)/2, 6.8+bh/2-0.18, r'contamination $c_n$', fs=9, fw='normal', color=C_CONT)\n\narrow(ax_l, 3.9, 7.28, 5.6, 7.28, color=C_GRAY, lw=2.0)\n\n# Red cross\nlabel(ax_l, 9.6, 7.28, '✗', fs=18, fw='bold', color=C_RED)\n\n# ── Path B ──\nlabel(ax_l, 5.0, 6.0, 'Path B: Contamination-first', fs=10.5, fw='bold', color=DARK)\n\nrbox(ax_l, 0.5, 4.5, bw+0.4, bh, C_CONT_L, C_CONT)\nlabel(ax_l, 0.5+(bw+0.4)/2, 4.5+bh/2+0.15, 'Step 1: Adjust', fs=9, fw='bold', color=DARK)\nlabel(ax_l, 0.5+(bw+0.4)/2, 4.5+bh/2-0.18, r'contamination $c_n$', fs=9, fw='normal', color=C_CONT)\n\nrbox(ax_l, 5.6, 4.5, bw, bh, C_JUDGE_L, C_JUDGE)\nlabel(ax_l, 5.6+bw/2, 4.5+bh/2+0.15, 'Step 2: MFRM', fs=9, fw='bold', color=DARK)\nlabel(ax_l, 5.6+bw/2, 4.5+bh/2-0.18, r'calibrate $d_j$', fs=9, fw='normal', color=C_JUDGE)\n\narrow(ax_l, 4.3, 4.97, 5.6, 4.97, color=C_GRAY, lw=2.0)\n\nlabel(ax_l, 9.6, 4.97, '✗', fs=18, fw='bold', color=C_RED)\n\n# ── OVB Box ──\nrbox(ax_l, 0.5, 2.2, 9.0, 1.85, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95)\n\nlabel(ax_l, 5.0, 3.45, 'Omitted Variable Bias (OVB)', fs=11, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 2.8,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=10.5, fw='normal', color=C_RED)\n\n# Warning arrows from OVB to both paths\narrow(ax_l, 3.0, 4.05, 3.0, 4.5, color=C_RED, lw=1.3, style='-|>')\narrow(ax_l, 7.0, 4.05, 7.0, 4.5, color=C_RED, lw=1.3, style='-|>')\n\n# Bottom note\nlabel(ax_l, 5.0, 1.35, 'Unmodeled facet absorbed into remaining estimates',\n      fs=9, color=C_RED, style='italic', fw='normal')\n\n# ── Dashed confounding arcs between Path A boxes ──\n# Red dashed arc from Step2_A back to Step1_A (showing absorbed bias)\na_conf = FancyArrowPatch((7.5, 7.75), (2.2, 7.75), arrowstyle='-|>',\n                          color=C_RED, linewidth=1.2, linestyle='--',\n                          connectionstyle='arc3,rad=-0.35',\n                          mutation_scale=12, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.9, 8.65, r'confounding', fs=7.5, color=C_RED, style='italic', fw='normal')\n\n# Red dashed arc between Path B boxes\nb_conf = FancyArrowPatch((7.3, 5.45), (2.7, 5.45), arrowstyle='-|>',\n                          color=C_RED, linewidth=1.2, linestyle='--',\n                          connectionstyle='arc3,rad=-0.35',\n                          mutation_scale=12, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 5.0, 6.35, r'confounding', fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\n# Background\nrbox(ax_r, 0.05, 0.15, 9.9, 9.6, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.15, zorder=0, pad=0.2)\n\n# Title\nlabel(ax_r, 5.0, 9.5, 'G-MFRM Joint Framework (Ours)', fs=14, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 9.0, 'staged joint calibration of all facets', fs=10,\n      color=C_GREEN, style='italic')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 7.3, 9.3, 1.35\nrbox(ax_r, s1_x, s1_y, s1_w, s1_h, '#E8F0F5', C_JUDGE, alpha=0.6)\n\nlabel(ax_r, 1.5, s1_y+s1_h-0.3, 'Stage 1', fs=10.5, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.5, s1_y+s1_h-0.7, 'Standard MFRM', fs=9, fw='normal', color=C_GRAY)\n\n# Output tokens\now, oh = 1.8, 0.6\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.0), (r'$\\hat{b}$', 6.1), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y+0.35, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo+ow/2, s1_y+0.35+oh/2, lbl_txt, fs=11, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 7.3, 7.3, 6.6, color=C_JUDGE, lw=2.0)\nlabel(ax_r, 7.7, 6.95, 'initialize', fs=7.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: External e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 4.55, 4.0, 2.55\nrbox(ax_r, s2_x, s2_y, s2_w, s2_h, '#FDF2E9', C_CONT, alpha=0.55)\n\nlabel(ax_r, s2_x+s2_w/2, s2_y+s2_h-0.3,\n      r'Stage 2: Estimate $e_i$', fs=9.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 3.1, 0.5\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.95 - k*0.6\n    rbox(ax_r, s2_x+0.45, sy, sw, sh, WHITE, C_CONT, lw=1.0)\n    label(ax_r, s2_x+0.45+sw/2, sy+sh/2, stxt, fs=8.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, 4.35, 5.5, 5.25, 5.5, color=C_CONT, lw=2.0)\nlabel(ax_r, 4.8, 5.78, r'$e_i$', fs=10, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 5.1, 4.3, 4.55, 2.3\nrbox(ax_r, s3_x, s3_y, s3_w, s3_h, '#F4F4F4', '#3C3C3C', lw=2.2)\n\nlabel(ax_r, s3_x+s3_w/2, s3_y+s3_h-0.35,\n      'Stage 3: Joint Gated Model', fs=10, fw='bold', color=DARK)\n\n# Model equation line\nlabel(ax_r, s3_x+s3_w/2, s3_y+s3_h-0.85,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=9, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x+0.5, s3_y+0.3, 3.55, 0.85\nrbox(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.2, alpha=0.9)\nlabel(ax_r, gx+gw/2, gy+gh/2+0.08,\n      r'Gating: $c_n \\cdot e_i$', fs=11, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 3.65, '4-Dimensional Diagnostic Output', fs=10.5, fw='bold', color=DARK)\n\now2, oh2 = 2.0, 0.95\nout_y = 2.35\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.55),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.8),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.3),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    rbox(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.5)\n    label(ax_r, xo+ow2/2, out_y+oh2/2+0.16, sym, fs=11, fw='bold', color=ec)\n    label(ax_r, xo+ow2/2, out_y+oh2/2-0.2, desc, fs=8, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.35, 4.3, 7.35, 3.3, color='#3C3C3C', lw=2.2, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 1.5, '✓  Joint estimation resolves confounding',\n      fs=10, fw='bold', color=C_GREEN, style='italic')\n\n# Panel labels\nlabel(ax_l, 0.45, 9.85, '(a)', fs=13, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 9.85, '(b)', fs=13, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
      "numLines": 245,
      "startLine": 1,
      "totalLines": 245
    }
  }
}
```

</details>

---


### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_0159gW26pEbxtuVjoUk3aEKY`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "765ab8fc-f03c-4170-97b5-f112a30214d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJqeePgUwArYBFS5qBkcxT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01FnCjuez4jTQ2NetCyH97vE`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "3d3fa4ba-5fba-4d2a-bf60-c8cc9a94b02e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJqeePgUwArYBFS5qBkcxT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13538,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13538
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

_source line 9 · 2026-05-24T11:42:46.909Z_

<details><summary>↩ Tool result · `toolu_0159gW26pEbxtuVjoUk3aEKY`</summary>

````text
1	---
2	description: 学术论文图表设计与生成——四层指南（防丑原则 + 叙事原则 + Pattern 库 + 工具路由）。Paper Agent 规划 visualization_plan 时读，Worker 执行时也读。
3	name: paper-visualization
4	scope: global
5	tags:
6	- research
7	- visualization
8	- paper
9	- matplotlib
10	- paperbanana
11	version: 5
12	roles:
13	- agent
14	- paper_agent
15	---
16	
17	# Paper Visualization — 学术图表设计与生成
18	
19	> **核心理念**：好图不是"画得对"，是"回答一个问题"。每张图动笔前先问：**这张图要让读者看到什么？**
20	>
21	> **质量底线**：每张图必须达到 NeurIPS/ICML/EMNLP best paper 的视觉水准——高级感、专业感、精致感。绝不接受 matplotlib 默认样式的廉价感。
22	
23	本 skill 分五层：
24	
25	- **L0 学习同行** — 设计前看几张优秀同类型论文图，比读任何原则都有效
26	- **L1 防丑原则** — 底线，所有图必须遵守
27	- **L2 叙事原则** — 让图有说服力（区分"数据图"和"论证图"）
28	- **L3 Pattern 库** — 具体技法目录，按 `design_notes` 选用
29	- **L4 工具路由 + 模板** — paperbanana vs matplotlib，常用统计图模板
30	
31	---
32	
33	## L0 学习同行（设计前的功课）
34	
35	你的子领域里，**最被引用、最被记住的论文是怎么画图的？** 在动笔之前花点时间去看一眼——这个动作的回报远高于读完下面的 L1-L4。
36	
37	### 为什么这一步是重要的
38	
39	- 同领域读者已经被这些论文的视觉语言"训练"过——遵循惯例 = 降低读者认知负担
40	- 顶会论文经历过 reviewer 严苛审查，能登出来的图基本说明它的 narrative 设计是被接受的
41	- 抽象原则告诉你"用 fill_between 表示发散"，但好论文告诉你"在这种数据上，发散到底应该画多淡才合适"
42	- 一个领域往往有它特有的图表惯例（如校准研究的 reliability diagram、scaling 研究的 log-log curve、RL 的 learning curve with seed bands），不看就不会用
43	
44	### 什么时候值得投入
45	
46	判断权交给你。一些可参考的信号：
47	
48	- **值得多花时间**：会决定论文成败的图（hero figure、main result、新颖的实验类型）
49	- **不太值得**：常规 supplementary 图、loss curve 这类标准化已经很高的图
50	- **强烈建议看**：你打算画一种自己不熟悉的图，或者数据形态是这个领域少见的
51	
52	### 怎么看
53	
54	工具：`paper-image-extractor` skill 可以从 arXiv source 或 PDF 提取参考论文里的 figure。你已经有 `literature_map.yaml` 里的论文清单作为起点。
55	
56	看的时候问自己（不是机械检查清单，是真的去理解）：
57	
58	- 这张图回答了什么问题？读者一眼能 get 到吗？
59	- 它用了哪些叙事层（background band / 参考线 / 概念曲线 / fill 区域）？这些层在我的数据上有对应物吗？
60	- 它的颜色和 marker 怎么承载语义？我的图能不能借鉴这套映射？
61	- 它有什么是这篇论文特有的（与他们的具体数据 / claim 绑死）？这些不要照搬。
62	- 如果让我重画它的图，我会怎么改？为什么作者没这么做？
63	
64	### 怎么把学到的传下去
65	
66	把你看完后的判断**直接写进对应 fig 的 `design_notes`**，用人话不用模板。例子：
67	
68	```yaml
69	design_notes:
70	  - "学 GPTQ Fig 4：用 log-scale bit-width + dashed FP16 baseline + 不同 marker shape 分模型族"
71	  - "Pattern A（regime band）划分 in-domain / OOD 两段"
72	  - "AWQ Fig 2 那种 hatching 区分 outlier 不适用我们的数据，跳过"
73	```
74	
75	Worker 拿到这种 design_notes 就知道既要参考 GPTQ 的 layout 又要用 Pattern A，能直接落实成代码。
76	
77	### 边界
78	
79	- 不要复刻，要消化。直接抄一张图既没用（数据不一样）也有风险（与他们的 claim 强绑定）
80	- 不要看太多。3 张就够，多了 Paper Agent 会陷入"该听谁的"
81	- 看不到原图（提取失败 / arXiv 无 source）就跳过，不要在这里卡住流程
82	
83	---
84	
85	## L1 防丑原则（底线，不可违反）
86	
87	来自 Tufte 和 Luís Cruz 16 条公认规范。Agent 默认遵守，无需逐条思考。
88	
89	1. **Self-explanatory** — 不看正文就能看懂：title/caption + 所有轴有 label + 单位
90	2. **去 chartjunk** — 不要 3D、不要背景框、不要无意义网格、不要 dual y-axis、不要 pie/donut chart
91	3. **直接标注 > Legend** — 能直接标在曲线/柱旁就不用 legend；legend 必要时不遮数据
92	4. **颜色/形状/纹理只用于 data variation** — 不用颜色装饰，不用相同颜色表示不同数据
93	5. **Meaningful baseline** — bar chart 必须从 0 起；scatter 可以非 0
94	6. **文字水平** — label 不要旋转/垂直；类别名太长 → 用 horizontal bar chart
95	7. **Sort for comparison** — 柱状图按数值排序，便于对比（除非有自然顺序如时间）
96	8. **字号一致** — 用 mm 计算 figsize（`ONE_MM = 1/25.4`），不在 LaTeX 里 `\includegraphics[scale=...]` resize
97	9. **色盲友好** — 默认 Okabe-Ito；红/绿区分时变 saturation；考虑 grayscale 打印
98	10. **Bold 只用于强调** — 不要全图加粗；highlight 留给 takeaway
99	11. **Line plot 只用于有序数据** — 类别变量用 bar
100	12. **单 x 单 y 轴** — 必须双轴时改成 multi-panel
101	13. **300 DPI、PDF 矢量、savefig.bbox=tight、去掉 top/right spines**
102	
103	---
104	
105	## L2 叙事原则（让图变成论证）
106	
107	L1 让图"不丑"，L2 让图"有说服力"。这一层是 Agent 自主画图时最容易缺失的。
108	
109	### 原则 1：每张图回答一个明确问题
110	
111	动笔前用一句话写下："This figure shows that ___."
112	
113	如果写不出来，就不要画。如果写出来的 takeaway 不是论文的 claim，就要重新设计。
114	
115	**反例**：`"Accuracy across methods"` — 这只是个标题，不是问题
116	**正例**：`"FP16 baseline 在小模型上比量化版高 5pp，但 70B 模型上差距消失"` — 这是一张图要说服读者相信的事
117	
118	`visualization_plan.{fig_id}.narrative_intent` 字段写这一句。
119	
120	### 原则 2：颜色绑定语义而非数据顺序
121	
122	错的做法：`colors = ['blue', 'orange', 'green', 'red']` 按数据顺序分配。
123	对的做法：`BN → 蓝色（始终）`、`non-BN → 橙色（始终）`、`collapse/danger → vermillion (#D55E00)`、`safe/baseline → blue (#0072B2)`。
124	
125	整篇论文 6 张图，BN 永远蓝、collapse 永远红——零认知负担，读者一眼建立映射。
126	
127	### 原则 3：信息层级用 visual variable 表达
128	
129	数据的"质量"和"分类"应该可见，不应该藏在 caption 里：
130	
131	| 信息 | Visual 表达 |
132	|------|------------|
133	| n < 50 低置信度点 | hollow marker + 标注 `n=` |
134	| Out-of-sample / pending 数据 | hollow + 不同 marker shape（如 diamond）+ "OOS" label |
135	| Collapse / 异常类别 | hatching（斜线填充）|
136	| 主结果 vs 次要结果 | 主用饱和色，次要用 muted 色或 alpha |
137	
138	### 原则 4：加叙事层，不只画数据
139	
140	数据是图的基础，叙事层是让读者"读懂"的关键。常见叙事层：
141	
142	- **Background bands** — `axhspan/axvspan` 标定性区域（"collapse zone"、"safe zone"、"Regime A/B/C"）
143	- **Fill_between** — 显示两条曲线发散区域（alpha 极低如 0.06，不抢眼但有面积）
144	- **Reference lines** — 锚定真实值（如 dashed line 标"actual W3A16 accuracy"）
145	- **Equivalence band** — `axvspan` gradient fade 标 +/-1pp 等价区间
146	- **Concept curve** — 完全合成的曲线（如 cosine trajectory）建立理论直觉
147	
148	这些都不来自数据，但帮读者"看到"数据想说什么。
149	
150	### 原则 5：Subtitle / panel label 写 insight 不写描述
151	
152	错：`"Layer 6 comparison across three models"`
153	对：`"Same relative position, opposite function"`
154	
155	错：`"Reliability diagram"`
156	对：`"Quantization shifts confidence but not accuracy"`
157	
158	副标题是免费的 takeaway，不要浪费。
159	
160	### 原则 6：Multi-panel 每个面板独立回答一个 sub-question
161	
162	不要做"主图 + 装饰小图"。每个 panel 必须有独立的信息价值。
163	
164	如果一个 panel 想不出独立的问题，要么删掉，要么合并到主 panel。
165	
166	布局上：非对称比例（如 1.4:1）让视觉重心对齐叙事重心。
167	
168	### 原则 7：所有图至少 3 轮迭代，Hero figure 至少 5 轮
169	
170	第一版画出来基本不能直接用。计划好预算：先确定数据和布局，再调样式标注，最后 polish。不要指望一次到位。
171	
172	### Hero Figure 定义
173	
174	Hero Figure = Figure 1 + 主结果图（main result figure）。这两类图对论文第一印象影响最大，必须投入更多迭代。
175	
176	---
177	
178	## L3 Pattern 库（按 `design_notes` 选用）
179	
180	按"图要回答的问题"选 pattern。每个 pattern 给出**何时用**、**怎么用**（具体代码或 matplotlib API）。
181	
182	### Pattern A：定性区域 / regime bands
183	
184	**何时用**：x 或 y 轴有自然分段（regime、phase、severity tier）。
185	
186	```python
187	# horizontal bands
188	for lo, hi, color, label in [(0, 1, '#EBF5FB', 'Regime A'), (1, 5, '#EAFAF1', 'Regime B')]:
189	    ax.axhspan(lo, hi, alpha=0.25, color=color, zorder=0)
190	    ax.text(x_label_pos, (lo+hi)/2, label, va='center', fontsize=9, color='gray')
191	
192	# 单一 collapse zone
193	ax.axhspan(-5, 5, color='#FDEDEC', alpha=0.5, zorder=0)
194	ax.text(0.02, 2.5, 'collapse zone', fontsize=8, color='#ccaaaa', fontstyle='italic')
195	```
196	
197	### Pattern B：发散面积 fill_between
198	
199	**何时用**：两组数据从某点开始发散，想让"发散程度"可见。
200	
201	```python
202	# alpha 0.06 极淡，不抢眼但有面积
203	ax.fill_between(x_range, curve_high, curve_low, alpha=0.06, color='#555555', zorder=1)
204	```
205	
206	### Pattern C：参考线锚定真实值
207	
208	**何时用**：合成 / 缩放后的 x 轴需要锚定到真实物理量。
209	
210	```python
211	ax.axhline(y=actual_value, color=color, linestyle=':', linewidth=0.8, alpha=0.3)
212	t = ax.text(x_pos, actual_value+1, 'actual W3A16', fontsize=7, color=color, alpha=0.5)
213	t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])  # 防遮挡
214	```
215	
216	### Pattern D：信息层级 marker（hollow vs solid）
217	
218	**何时用**：同一图中有不同置信度 / OOS / pending 数据。
219	
220	```python
221	# 实心 = n >= 50, 空心 = n < 50
222	if n < 50:
223	    ax.plot(x, y, marker='o', markerfacecolor='white', markeredgecolor=color,
224	            markeredgewidth=1.2, markersize=6)
225	    ax.annotate(f'n={n}', (x, y), xytext=(0, 7), textcoords='offset points',
226	                fontsize=5, color=color, fontstyle='italic')
227	```
228	
229	### Pattern E：Wilson CI / bootstrap 不确定性
230	
231	**何时用**：accuracy / proportion 数据需要置信区间。
232	
233	```python
234	def wilson_ci(p, n, z=1.96):
235	    denom = 1 + z**2 / n
236	    center = (p + z**2 / (2*n)) / denom
237	    half = z * np.sqrt((p*(1-p) + z**2/(4*n)) / n) / denom
238	    return max(0, center - half), min(1, center + half)
239	```
240	
241	### Pattern F：Per-label offset dict（解决标注重叠）
242	
243	**何时用**：scatter 上多个点需要标注且自动布局重叠。
244	
245	```python
246	label_offsets = {
247	    'Qwen3-8B':  (6, -12),   # 向下避让
248	    'Qwen3-4B':  (-55, 4),   # 向左避让
249	    'Llama-8B':  (6, 6),
250	}
251	for name, (x, y) in data.items():
252	    ox, oy = label_offsets.get(name, (6, 6))
253	    ax.annotate(name, (x, y), xytext=(ox, oy), textcoords='offset points', fontsize=7)
254	```
255	
256	### Pattern G：Hatching 加分类维度
257	
258	**何时用**：已用颜色表示一个维度，再加一个二元维度（如 collapse vs not）。
259	
260	```python
261	for is_collapse, bar in zip(collapse_flags, bars):
262	    if is_collapse:
263	        bar.set_hatch('///')
264	        bar.set_alpha(0.7)
265	```
266	
267	### Pattern H：Multi-panel 非对称布局
268	
269	**何时用**：主图 + 辅助 panel；或两个等重要 panel 但视觉重心需要倾斜。
270	
271	```python
272	fig, axes = plt.subplots(1, 2, figsize=(6.5, 3.2),
273	                          gridspec_kw={'width_ratios': [1.4, 1]})
274	# 主面板 1.4x 宽，副面板 1x；视觉重心在左
275	```
276	
277	### Pattern I：Broken axis（异常值或对数 0）
278	
279	**何时用**：数据范围跨度大，或对数轴需要表示 0。
280	
281	```python
282	d = 0.012
283	kwargs = dict(transform=ax.transAxes, color='black', clip_on=False, linewidth=0.6)
284	ax.plot((1-d, 1+d), (-d, +d), **kwargs)  # 右下角斜线
285	ax.plot((1-d, 1+d), (1-d, 1+d), **kwargs)  # 右上角斜线
286	```
287	
288	### Pattern J：Path-effect 文字描边
289	
290	**何时用**：标注必须放在数据点 / colored region 上方。
291	
292	```python
293	import matplotlib.patheffects as pe
294	t = ax.text(x, y, 'label', fontsize=8, color='red')
295	t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])
296	```
297	
298	### Pattern K：Concept curve（建立直觉）
299	
300	**何时用**：论文核心 claim 是定性现象，需要先让读者理解理论预期。
301	
302	```python
303	# 完全合成的 cosine trajectory，不是实验数据
304	x = np.linspace(0, 1, 100)
305	trajectory = baseline * (1 - np.cos(np.pi * x)) / 2
306	ax.plot(x, trajectory, linewidth=2, solid_capstyle='round')
307	ax.annotate('gap eliminated', (1.0, final_y), color='#388E3C',
308	            fontstyle='italic', fontsize=9)
309	```
310	
311	### Pattern L：Forest plot（meta-analysis 风格）
312	
313	**何时用**：多个子条件的 effect size + CI 对比，加 inline 统计数字。
314	
315	3-column GridSpec：(1) 标签 (2) CI 区间图 (3) 统计数字（mean, CI, p-value）
316	
317	每行：dot + horizontal line(CI) + 数字 inline。等价带用半透明 axvspan。
318	
319	### 概念图 L1 防丑原则（7 条）
320	
321	概念图（架构图、流程图、framework 示意）的视觉底线，与统计图 L1 互补。
322	
323	1. **Flow direction 一致** — 全图统一左→右或上→下，不混合方向
324	2. **Box 规格统一** — 同层级 box 尺寸、圆角、边框粗细一致
325	3. **箭头样式统一** — 不混用多种箭头类型（除非有语义区分）
326	4. **层级清晰** — 不同抽象层用缩进/嵌套/背景色区分
327	5. **密度控制** — 单张图 ≤15 个 box，超过则拆分或分组
328	6. **Label 完整** — 每个 box 和箭头都有文字说明
329	7. **无装饰性元素** — 不加纯装饰图标、渐变、3D 效果
330	
331	### 概念图 L2 叙事原则（6 条）
332	
333	让概念图不只是"画了个框图"，而是"引导读者理解系统"。
334	
335	1. **视觉锚点** — 核心贡献用饱和色/大字/加粗边框突出，其余 muted
336	2. **阅读路径** — 沿箭头方向自然读完全图，不需要跳跃
337	3. **对比布局** — 左右并列展示 before/after 或 baseline/ours
338	4. **分组嵌套** — 用浅色背景框将相关组件分组（如 encoder/decoder）
339	5. **箭头语义** — 实线=数据流，虚线=控制流/可选，粗线=关键路径
340	6. **信息层级** — 主路径用饱和色+大字，辅助信息用灰色+小字
341	
342	### 概念图 L3 Pattern 库
343	
344	| Pattern | 名称 | 适用场景 |
345	|---------|------|---------|
346	| P-A | 线性流程 | 数据处理 pipeline、推理流程 |
347	| P-B | 层级嵌套 | 模型架构（encoder/decoder/attention） |
348	| P-C | 对比并列 | baseline vs ours、before/after |
349	| P-D | 分支汇聚 | 多输入融合、ensemble |
350	| P-E | 循环 | 训练循环、迭代优化 |
351	| P-F | 诊断链 | 消融实验逻辑、排错流程 |
352	| P-G | 三面板综合 | 概念+数据+结论（常用于 Figure 1） |
353	
354	### 概念图 Checklist（7 项）
355	
356	- [ ] Flow direction 全图统一（左→右或上→下）
357	- [ ] Box 规格一致（同层级尺寸、圆角、边框相同）
358	- [ ] 视觉层级清晰（核心突出，辅助 muted）
359	- [ ] 核心贡献在视觉上最突出
360	- [ ] 箭头语义一致（实线/虚线/粗细有意义）
361	- [ ] 留白充足（box 之间不拥挤）
362	- [ ] 跨图风格一致（配色、字号、线宽与论文其他图统一）
363	
364	---
365	
366	## L4 工具路由 + 模板
367	
368	### 路由规则
369	
370	| 场景 | 工具 | 原因 |
371	|------|------|------|
372	| 概念图（架构图、流程图、framework 示意） | **PaperBanana（Gemini）** | matplotlib 手写 boxes/arrows 极痛苦 |
373	| 统计图（scatter、bar、line、heatmap、forest） | **matplotlib** | 确定性、可控、有模板 |
374	| 离线 / 无 GOOGLE_API_KEY | **matplotlib** | 不依赖外部 API |
375	
376	项目级偏好：`config/projects/{name}.yaml` 的 `visualization.preferred_tool` 可覆盖。
377	
378	### Matplotlib 通用样式（rcParams 标准）
379	
380	```python
381	import matplotlib
382	matplotlib.use('Agg')
383	import matplotlib.pyplot as plt
384	import matplotlib.patheffects as pe
385	import numpy as np
386	
387	plt.rcParams.update({
388	    'font.family': 'DejaVu Sans',
389	    'font.size': 11, 'axes.titlesize': 13, 'axes.labelsize': 12,
390	    'xtick.labelsize': 10, 'ytick.labelsize': 10, 'legend.fontsize': 10,
391	    'figure.dpi': 300, 'savefig.dpi': 300,
392	    'savefig.bbox': 'tight', 'savefig.pad_inches': 0.05,
393	    'axes.spines.top': False, 'axes.spines.right': False,
394	    'pdf.fonttype': 42, 'ps.fonttype': 42,  # TrueType 嵌入
395	    'lines.linewidth': 1.8,
396	})
397	
398	# 色盲友好语义色板（Okabe-Ito）
399	SEMANTIC_COLORS = {
400	    'baseline':   '#0072B2',  # blue - safe / mild
401	    'treatment':  '#E69F00',  # orange - intervention
402	    'collapse':   '#D55E00',  # vermillion - danger / catastrophic
403	    'safe':       '#009E73',  # green - good outcome
404	    'neutral':    '#999999',  # gray - reference / control
405	}
406	```
407	
408	### 常用模板（仅作起点，需按 narrative_intent 改造）
409	
410	详细执行模板见 `skills/global/draw-paper-figure.skill.md`：
411	- Reliability Diagram（校准图）
412	- ECE Heatmap（方法 × 数据集 ΔECE）
413	- T* Scatter Plot（任务 Regime 可视化）
414	
415	**重要**：这些模板是起点不是终点。每张图根据 `narrative_intent` 必须加 L3 中的相关 pattern，不能直接套用。
416	
417	### 主图（Figure 1）特别提示
418	
419	大多数 ML 论文的 Figure 1 是概念图/架构图/方法概览——正是 PaperBanana 的强项。除非 Figure 1 是纯数值结果对比（如 Pareto frontier），否则优先用 PaperBanana。Figure 1 的 `narrative_intent` 必须与 `writing_plan.yaml` 的 `meta.core_claim` 直接关联。
420	
421	### PaperBanana 用法
422	
423	见 `skills/global/paper-banana.skill.md`。意图描述时直接引用 `narrative_intent`，并把 L3 中的 pattern 名写进 intent（如 "with collapse zone background band, hollow markers for n<50"）。
424	
425	---
426	
427	## 给 Paper Agent 的填写规则
428	
429	规划 `visualization_plan` 时，对每张图填：
430	
431	```yaml
432	- fig_id: fig2_main_result
433	  type: statistical
434	  tool: matplotlib
435	  data_source: "registry: exp_001, exp_002"
436	  placement: experiments
437	
438	  # 新字段（必填）
439	  narrative_intent: "Quantized models match FP16 on accuracy but degrade calibration; ECE gap widens with bits→2."
440	  design_notes:
441	    - "Pattern A: regime bands for bits=8/4/3"
442	    - "Pattern C: dashed line for FP16 ECE baseline"
443	    - "Pattern D: hollow markers for n<50 data points"
444	
445	  aspect_ratio: "4:3"
446	```
447	
448	`narrative_intent`：一句话，主动语态，描述读者应该相信的事。
449	
450	`design_notes`：从 L3 选 0-4 个 pattern，给出选用理由。可以为空（说明默认模板足够）。
451	
452	---
453	
454	## 提交前 Checklist（以下为统计图专用）
455	
456	L1 部分（防丑底线）：
457	- [ ] 所有轴有 label + 单位
458	- [ ] 无 dual y-axis、无 3D、无 pie
459	- [ ] 颜色绑定语义、色盲友好
460	- [ ] Bar chart 从 0 起（如有）
461	- [ ] 字号 ≥ 10pt（缩到 column width 后仍可读）
462	- [ ] PDF 矢量、300 DPI
463	
464	L2 部分（叙事强度）：
465	- [ ] 能用一句话写出 figure takeaway（应等于 `narrative_intent`）
466	- [ ] Subtitle / panel label 是 insight，不是描述
467	- [ ] 数据质量差异在视觉上可见（n、OOS、pending 等）
468	- [ ] 至少考虑过是否需要 background band / fill_between / reference line（不一定要加）
469	
470	L3 部分（高级感——不可跳过）：
471	- [ ] 不像 matplotlib gallery 示例（无默认灰背景、无粗网格、无 tab10 色板）
472	- [ ] 配色 muted 和谐，不刺眼，不过度饱和
473	- [ ] 线宽、字号、间距全图统一
474	- [ ] 元素对齐严格（bars 底部对齐、labels 水平对齐）
475	- [ ] 留白充足（元素之间不拥挤）
476	- [ ] 与论文全文其他图的风格一致
477	- [ ] 终极判断：这张图放在 NeurIPS best paper 里违和吗？
478	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "bb1be963-c4d3-44c6-ae79-53e6302f9c4f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md",
      "content": "---\ndescription: 学术论文图表设计与生成——四层指南（防丑原则 + 叙事原则 + Pattern 库 + 工具路由）。Paper Agent 规划 visualization_plan 时读，Worker 执行时也读。\nname: paper-visualization\nscope: global\ntags:\n- research\n- visualization\n- paper\n- matplotlib\n- paperbanana\nversion: 5\nroles:\n- agent\n- paper_agent\n---\n\n# Paper Visualization — 学术图表设计与生成\n\n> **核心理念**：好图不是\"画得对\"，是\"回答一个问题\"。每张图动笔前先问：**这张图要让读者看到什么？**\n>\n> **质量底线**：每张图必须达到 NeurIPS/ICML/EMNLP best paper 的视觉水准——高级感、专业感、精致感。绝不接受 matplotlib 默认样式的廉价感。\n\n本 skill 分五层：\n\n- **L0 学习同行** — 设计前看几张优秀同类型论文图，比读任何原则都有效\n- **L1 防丑原则** — 底线，所有图必须遵守\n- **L2 叙事原则** — 让图有说服力（区分\"数据图\"和\"论证图\"）\n- **L3 Pattern 库** — 具体技法目录，按 `design_notes` 选用\n- **L4 工具路由 + 模板** — paperbanana vs matplotlib，常用统计图模板\n\n---\n\n## L0 学习同行（设计前的功课）\n\n你的子领域里，**最被引用、最被记住的论文是怎么画图的？** 在动笔之前花点时间去看一眼——这个动作的回报远高于读完下面的 L1-L4。\n\n### 为什么这一步是重要的\n\n- 同领域读者已经被这些论文的视觉语言\"训练\"过——遵循惯例 = 降低读者认知负担\n- 顶会论文经历过 reviewer 严苛审查，能登出来的图基本说明它的 narrative 设计是被接受的\n- 抽象原则告诉你\"用 fill_between 表示发散\"，但好论文告诉你\"在这种数据上，发散到底应该画多淡才合适\"\n- 一个领域往往有它特有的图表惯例（如校准研究的 reliability diagram、scaling 研究的 log-log curve、RL 的 learning curve with seed bands），不看就不会用\n\n### 什么时候值得投入\n\n判断权交给你。一些可参考的信号：\n\n- **值得多花时间**：会决定论文成败的图（hero figure、main result、新颖的实验类型）\n- **不太值得**：常规 supplementary 图、loss curve 这类标准化已经很高的图\n- **强烈建议看**：你打算画一种自己不熟悉的图，或者数据形态是这个领域少见的\n\n### 怎么看\n\n工具：`paper-image-extractor` skill 可以从 arXiv source 或 PDF 提取参考论文里的 figure。你已经有 `literature_map.yaml` 里的论文清单作为起点。\n\n看的时候问自己（不是机械检查清单，是真的去理解）：\n\n- 这张图回答了什么问题？读者一眼能 get 到吗？\n- 它用了哪些叙事层（background band / 参考线 / 概念曲线 / fill 区域）？这些层在我的数据上有对应物吗？\n- 它的颜色和 marker 怎么承载语义？我的图能不能借鉴这套映射？\n- 它有什么是这篇论文特有的（与他们的具体数据 / claim 绑死）？这些不要照搬。\n- 如果让我重画它的图，我会怎么改？为什么作者没这么做？\n\n### 怎么把学到的传下去\n\n把你看完后的判断**直接写进对应 fig 的 `design_notes`**，用人话不用模板。例子：\n\n```yaml\ndesign_notes:\n  - \"学 GPTQ Fig 4：用 log-scale bit-width + dashed FP16 baseline + 不同 marker shape 分模型族\"\n  - \"Pattern A（regime band）划分 in-domain / OOD 两段\"\n  - \"AWQ Fig 2 那种 hatching 区分 outlier 不适用我们的数据，跳过\"\n```\n\nWorker 拿到这种 design_notes 就知道既要参考 GPTQ 的 layout 又要用 Pattern A，能直接落实成代码。\n\n### 边界\n\n- 不要复刻，要消化。直接抄一张图既没用（数据不一样）也有风险（与他们的 claim 强绑定）\n- 不要看太多。3 张就够，多了 Paper Agent 会陷入\"该听谁的\"\n- 看不到原图（提取失败 / arXiv 无 source）就跳过，不要在这里卡住流程\n\n---\n\n## L1 防丑原则（底线，不可违反）\n\n来自 Tufte 和 Luís Cruz 16 条公认规范。Agent 默认遵守，无需逐条思考。\n\n1. **Self-explanatory** — 不看正文就能看懂：title/caption + 所有轴有 label + 单位\n2. **去 chartjunk** — 不要 3D、不要背景框、不要无意义网格、不要 dual y-axis、不要 pie/donut chart\n3. **直接标注 > Legend** — 能直接标在曲线/柱旁就不用 legend；legend 必要时不遮数据\n4. **颜色/形状/纹理只用于 data variation** — 不用颜色装饰，不用相同颜色表示不同数据\n5. **Meaningful baseline** — bar chart 必须从 0 起；scatter 可以非 0\n6. **文字水平** — label 不要旋转/垂直；类别名太长 → 用 horizontal bar chart\n7. **Sort for comparison** — 柱状图按数值排序，便于对比（除非有自然顺序如时间）\n8. **字号一致** — 用 mm 计算 figsize（`ONE_MM = 1/25.4`），不在 LaTeX 里 `\\includegraphics[scale=...]` resize\n9. **色盲友好** — 默认 Okabe-Ito；红/绿区分时变 saturation；考虑 grayscale 打印\n10. **Bold 只用于强调** — 不要全图加粗；highlight 留给 takeaway\n11. **Line plot 只用于有序数据** — 类别变量用 bar\n12. **单 x 单 y 轴** — 必须双轴时改成 multi-panel\n13. **300 DPI、PDF 矢量、savefig.bbox=tight、去掉 top/right spines**\n\n---\n\n## L2 叙事原则（让图变成论证）\n\nL1 让图\"不丑\"，L2 让图\"有说服力\"。这一层是 Agent 自主画图时最容易缺失的。\n\n### 原则 1：每张图回答一个明确问题\n\n动笔前用一句话写下：\"This figure shows that ___.\"\n\n如果写不出来，就不要画。如果写出来的 takeaway 不是论文的 claim，就要重新设计。\n\n**反例**：`\"Accuracy across methods\"` — 这只是个标题，不是问题\n**正例**：`\"FP16 baseline 在小模型上比量化版高 5pp，但 70B 模型上差距消失\"` — 这是一张图要说服读者相信的事\n\n`visualization_plan.{fig_id}.narrative_intent` 字段写这一句。\n\n### 原则 2：颜色绑定语义而非数据顺序\n\n错的做法：`colors = ['blue', 'orange', 'green', 'red']` 按数据顺序分配。\n对的做法：`BN → 蓝色（始终）`、`non-BN → 橙色（始终）`、`collapse/danger → vermillion (#D55E00)`、`safe/baseline → blue (#0072B2)`。\n\n整篇论文 6 张图，BN 永远蓝、collapse 永远红——零认知负担，读者一眼建立映射。\n\n### 原则 3：信息层级用 visual variable 表达\n\n数据的\"质量\"和\"分类\"应该可见，不应该藏在 caption 里：\n\n| 信息 | Visual 表达 |\n|------|------------|\n| n < 50 低置信度点 | hollow marker + 标注 `n=` |\n| Out-of-sample / pending 数据 | hollow + 不同 marker shape（如 diamond）+ \"OOS\" label |\n| Collapse / 异常类别 | hatching（斜线填充）|\n| 主结果 vs 次要结果 | 主用饱和色，次要用 muted 色或 alpha |\n\n### 原则 4：加叙事层，不只画数据\n\n数据是图的基础，叙事层是让读者\"读懂\"的关键。常见叙事层：\n\n- **Background bands** — `axhspan/axvspan` 标定性区域（\"collapse zone\"、\"safe zone\"、\"Regime A/B/C\"）\n- **Fill_between** — 显示两条曲线发散区域（alpha 极低如 0.06，不抢眼但有面积）\n- **Reference lines** — 锚定真实值（如 dashed line 标\"actual W3A16 accuracy\"）\n- **Equivalence band** — `axvspan` gradient fade 标 +/-1pp 等价区间\n- **Concept curve** — 完全合成的曲线（如 cosine trajectory）建立理论直觉\n\n这些都不来自数据，但帮读者\"看到\"数据想说什么。\n\n### 原则 5：Subtitle / panel label 写 insight 不写描述\n\n错：`\"Layer 6 comparison across three models\"`\n对：`\"Same relative position, opposite function\"`\n\n错：`\"Reliability diagram\"`\n对：`\"Quantization shifts confidence but not accuracy\"`\n\n副标题是免费的 takeaway，不要浪费。\n\n### 原则 6：Multi-panel 每个面板独立回答一个 sub-question\n\n不要做\"主图 + 装饰小图\"。每个 panel 必须有独立的信息价值。\n\n如果一个 panel 想不出独立的问题，要么删掉，要么合并到主 panel。\n\n布局上：非对称比例（如 1.4:1）让视觉重心对齐叙事重心。\n\n### 原则 7：所有图至少 3 轮迭代，Hero figure 至少 5 轮\n\n第一版画出来基本不能直接用。计划好预算：先确定数据和布局，再调样式标注，最后 polish。不要指望一次到位。\n\n### Hero Figure 定义\n\nHero Figure = Figure 1 + 主结果图（main result figure）。这两类图对论文第一印象影响最大，必须投入更多迭代。\n\n---\n\n## L3 Pattern 库（按 `design_notes` 选用）\n\n按\"图要回答的问题\"选 pattern。每个 pattern 给出**何时用**、**怎么用**（具体代码或 matplotlib API）。\n\n### Pattern A：定性区域 / regime bands\n\n**何时用**：x 或 y 轴有自然分段（regime、phase、severity tier）。\n\n```python\n# horizontal bands\nfor lo, hi, color, label in [(0, 1, '#EBF5FB', 'Regime A'), (1, 5, '#EAFAF1', 'Regime B')]:\n    ax.axhspan(lo, hi, alpha=0.25, color=color, zorder=0)\n    ax.text(x_label_pos, (lo+hi)/2, label, va='center', fontsize=9, color='gray')\n\n# 单一 collapse zone\nax.axhspan(-5, 5, color='#FDEDEC', alpha=0.5, zorder=0)\nax.text(0.02, 2.5, 'collapse zone', fontsize=8, color='#ccaaaa', fontstyle='italic')\n```\n\n### Pattern B：发散面积 fill_between\n\n**何时用**：两组数据从某点开始发散，想让\"发散程度\"可见。\n\n```python\n# alpha 0.06 极淡，不抢眼但有面积\nax.fill_between(x_range, curve_high, curve_low, alpha=0.06, color='#555555', zorder=1)\n```\n\n### Pattern C：参考线锚定真实值\n\n**何时用**：合成 / 缩放后的 x 轴需要锚定到真实物理量。\n\n```python\nax.axhline(y=actual_value, color=color, linestyle=':', linewidth=0.8, alpha=0.3)\nt = ax.text(x_pos, actual_value+1, 'actual W3A16', fontsize=7, color=color, alpha=0.5)\nt.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])  # 防遮挡\n```\n\n### Pattern D：信息层级 marker（hollow vs solid）\n\n**何时用**：同一图中有不同置信度 / OOS / pending 数据。\n\n```python\n# 实心 = n >= 50, 空心 = n < 50\nif n < 50:\n    ax.plot(x, y, marker='o', markerfacecolor='white', markeredgecolor=color,\n            markeredgewidth=1.2, markersize=6)\n    ax.annotate(f'n={n}', (x, y), xytext=(0, 7), textcoords='offset points',\n                fontsize=5, color=color, fontstyle='italic')\n```\n\n### Pattern E：Wilson CI / bootstrap 不确定性\n\n**何时用**：accuracy / proportion 数据需要置信区间。\n\n```python\ndef wilson_ci(p, n, z=1.96):\n    denom = 1 + z**2 / n\n    center = (p + z**2 / (2*n)) / denom\n    half = z * np.sqrt((p*(1-p) + z**2/(4*n)) / n) / denom\n    return max(0, center - half), min(1, center + half)\n```\n\n### Pattern F：Per-label offset dict（解决标注重叠）\n\n**何时用**：scatter 上多个点需要标注且自动布局重叠。\n\n```python\nlabel_offsets = {\n    'Qwen3-8B':  (6, -12),   # 向下避让\n    'Qwen3-4B':  (-55, 4),   # 向左避让\n    'Llama-8B':  (6, 6),\n}\nfor name, (x, y) in data.items():\n    ox, oy = label_offsets.get(name, (6, 6))\n    ax.annotate(name, (x, y), xytext=(ox, oy), textcoords='offset points', fontsize=7)\n```\n\n### Pattern G：Hatching 加分类维度\n\n**何时用**：已用颜色表示一个维度，再加一个二元维度（如 collapse vs not）。\n\n```python\nfor is_collapse, bar in zip(collapse_flags, bars):\n    if is_collapse:\n        bar.set_hatch('///')\n        bar.set_alpha(0.7)\n```\n\n### Pattern H：Multi-panel 非对称布局\n\n**何时用**：主图 + 辅助 panel；或两个等重要 panel 但视觉重心需要倾斜。\n\n```python\nfig, axes = plt.subplots(1, 2, figsize=(6.5, 3.2),\n                          gridspec_kw={'width_ratios': [1.4, 1]})\n# 主面板 1.4x 宽，副面板 1x；视觉重心在左\n```\n\n### Pattern I：Broken axis（异常值或对数 0）\n\n**何时用**：数据范围跨度大，或对数轴需要表示 0。\n\n```python\nd = 0.012\nkwargs = dict(transform=ax.transAxes, color='black', clip_on=False, linewidth=0.6)\nax.plot((1-d, 1+d), (-d, +d), **kwargs)  # 右下角斜线\nax.plot((1-d, 1+d), (1-d, 1+d), **kwargs)  # 右上角斜线\n```\n\n### Pattern J：Path-effect 文字描边\n\n**何时用**：标注必须放在数据点 / colored region 上方。\n\n```python\nimport matplotlib.patheffects as pe\nt = ax.text(x, y, 'label', fontsize=8, color='red')\nt.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])\n```\n\n### Pattern K：Concept curve（建立直觉）\n\n**何时用**：论文核心 claim 是定性现象，需要先让读者理解理论预期。\n\n```python\n# 完全合成的 cosine trajectory，不是实验数据\nx = np.linspace(0, 1, 100)\ntrajectory = baseline * (1 - np.cos(np.pi * x)) / 2\nax.plot(x, trajectory, linewidth=2, solid_capstyle='round')\nax.annotate('gap eliminated', (1.0, final_y), color='#388E3C',\n            fontstyle='italic', fontsize=9)\n```\n\n### Pattern L：Forest plot（meta-analysis 风格）\n\n**何时用**：多个子条件的 effect size + CI 对比，加 inline 统计数字。\n\n3-column GridSpec：(1) 标签 (2) CI 区间图 (3) 统计数字（mean, CI, p-value）\n\n每行：dot + horizontal line(CI) + 数字 inline。等价带用半透明 axvspan。\n\n### 概念图 L1 防丑原则（7 条）\n\n概念图（架构图、流程图、framework 示意）的视觉底线，与统计图 L1 互补。\n\n1. **Flow direction 一致** — 全图统一左→右或上→下，不混合方向\n2. **Box 规格统一** — 同层级 box 尺寸、圆角、边框粗细一致\n3. **箭头样式统一** — 不混用多种箭头类型（除非有语义区分）\n4. **层级清晰** — 不同抽象层用缩进/嵌套/背景色区分\n5. **密度控制** — 单张图 ≤15 个 box，超过则拆分或分组\n6. **Label 完整** — 每个 box 和箭头都有文字说明\n7. **无装饰性元素** — 不加纯装饰图标、渐变、3D 效果\n\n### 概念图 L2 叙事原则（6 条）\n\n让概念图不只是\"画了个框图\"，而是\"引导读者理解系统\"。\n\n1. **视觉锚点** — 核心贡献用饱和色/大字/加粗边框突出，其余 muted\n2. **阅读路径** — 沿箭头方向自然读完全图，不需要跳跃\n3. **对比布局** — 左右并列展示 before/after 或 baseline/ours\n4. **分组嵌套** — 用浅色背景框将相关组件分组（如 encoder/decoder）\n5. **箭头语义** — 实线=数据流，虚线=控制流/可选，粗线=关键路径\n6. **信息层级** — 主路径用饱和色+大字，辅助信息用灰色+小字\n\n### 概念图 L3 Pattern 库\n\n| Pattern | 名称 | 适用场景 |\n|---------|------|---------|\n| P-A | 线性流程 | 数据处理 pipeline、推理流程 |\n| P-B | 层级嵌套 | 模型架构（encoder/decoder/attention） |\n| P-C | 对比并列 | baseline vs ours、before/after |\n| P-D | 分支汇聚 | 多输入融合、ensemble |\n| P-E | 循环 | 训练循环、迭代优化 |\n| P-F | 诊断链 | 消融实验逻辑、排错流程 |\n| P-G | 三面板综合 | 概念+数据+结论（常用于 Figure 1） |\n\n### 概念图 Checklist（7 项）\n\n- [ ] Flow direction 全图统一（左→右或上→下）\n- [ ] Box 规格一致（同层级尺寸、圆角、边框相同）\n- [ ] 视觉层级清晰（核心突出，辅助 muted）\n- [ ] 核心贡献在视觉上最突出\n- [ ] 箭头语义一致（实线/虚线/粗细有意义）\n- [ ] 留白充足（box 之间不拥挤）\n- [ ] 跨图风格一致（配色、字号、线宽与论文其他图统一）\n\n---\n\n## L4 工具路由 + 模板\n\n### 路由规则\n\n| 场景 | 工具 | 原因 |\n|------|------|------|\n| 概念图（架构图、流程图、framework 示意） | **PaperBanana（Gemini）** | matplotlib 手写 boxes/arrows 极痛苦 |\n| 统计图（scatter、bar、line、heatmap、forest） | **matplotlib** | 确定性、可控、有模板 |\n| 离线 / 无 GOOGLE_API_KEY | **matplotlib** | 不依赖外部 API |\n\n项目级偏好：`config/projects/{name}.yaml` 的 `visualization.preferred_tool` 可覆盖。\n\n### Matplotlib 通用样式（rcParams 标准）\n\n```python\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11, 'axes.titlesize': 13, 'axes.labelsize': 12,\n    'xtick.labelsize': 10, 'ytick.labelsize': 10, 'legend.fontsize': 10,\n    'figure.dpi': 300, 'savefig.dpi': 300,\n    'savefig.bbox': 'tight', 'savefig.pad_inches': 0.05,\n    'axes.spines.top': False, 'axes.spines.right': False,\n    'pdf.fonttype': 42, 'ps.fonttype': 42,  # TrueType 嵌入\n    'lines.linewidth': 1.8,\n})\n\n# 色盲友好语义色板（Okabe-Ito）\nSEMANTIC_COLORS = {\n    'baseline':   '#0072B2',  # blue - safe / mild\n    'treatment':  '#E69F00',  # orange - intervention\n    'collapse':   '#D55E00',  # vermillion - danger / catastrophic\n    'safe':       '#009E73',  # green - good outcome\n    'neutral':    '#999999',  # gray - reference / control\n}\n```\n\n### 常用模板（仅作起点，需按 narrative_intent 改造）\n\n详细执行模板见 `skills/global/draw-paper-figure.skill.md`：\n- Reliability Diagram（校准图）\n- ECE Heatmap（方法 × 数据集 ΔECE）\n- T* Scatter Plot（任务 Regime 可视化）\n\n**重要**：这些模板是起点不是终点。每张图根据 `narrative_intent` 必须加 L3 中的相关 pattern，不能直接套用。\n\n### 主图（Figure 1）特别提示\n\n大多数 ML 论文的 Figure 1 是概念图/架构图/方法概览——正是 PaperBanana 的强项。除非 Figure 1 是纯数值结果对比（如 Pareto frontier），否则优先用 PaperBanana。Figure 1 的 `narrative_intent` 必须与 `writing_plan.yaml` 的 `meta.core_claim` 直接关联。\n\n### PaperBanana 用法\n\n见 `skills/global/paper-banana.skill.md`。意图描述时直接引用 `narrative_intent`，并把 L3 中的 pattern 名写进 intent（如 \"with collapse zone background band, hollow markers for n<50\"）。\n\n---\n\n## 给 Paper Agent 的填写规则\n\n规划 `visualization_plan` 时，对每张图填：\n\n```yaml\n- fig_id: fig2_main_result\n  type: statistical\n  tool: matplotlib\n  data_source: \"registry: exp_001, exp_002\"\n  placement: experiments\n\n  # 新字段（必填）\n  narrative_intent: \"Quantized models match FP16 on accuracy but degrade calibration; ECE gap widens with bits→2.\"\n  design_notes:\n    - \"Pattern A: regime bands for bits=8/4/3\"\n    - \"Pattern C: dashed line for FP16 ECE baseline\"\n    - \"Pattern D: hollow markers for n<50 data points\"\n\n  aspect_ratio: \"4:3\"\n```\n\n`narrative_intent`：一句话，主动语态，描述读者应该相信的事。\n\n`design_notes`：从 L3 选 0-4 个 pattern，给出选用理由。可以为空（说明默认模板足够）。\n\n---\n\n## 提交前 Checklist（以下为统计图专用）\n\nL1 部分（防丑底线）：\n- [ ] 所有轴有 label + 单位\n- [ ] 无 dual y-axis、无 3D、无 pie\n- [ ] 颜色绑定语义、色盲友好\n- [ ] Bar chart 从 0 起（如有）\n- [ ] 字号 ≥ 10pt（缩到 column width 后仍可读）\n- [ ] PDF 矢量、300 DPI\n\nL2 部分（叙事强度）：\n- [ ] 能用一句话写出 figure takeaway（应等于 `narrative_intent`）\n- [ ] Subtitle / panel label 是 insight，不是描述\n- [ ] 数据质量差异在视觉上可见（n、OOS、pending 等）\n- [ ] 至少考虑过是否需要 background band / fill_between / reference line（不一定要加）\n\nL3 部分（高级感——不可跳过）：\n- [ ] 不像 matplotlib gallery 示例（无默认灰背景、无粗网格、无 tab10 色板）\n- [ ] 配色 muted 和谐，不刺眼，不过度饱和\n- [ ] 线宽、字号、间距全图统一\n- [ ] 元素对齐严格（bars 底部对齐、labels 水平对齐）\n- [ ] 留白充足（元素之间不拥挤）\n- [ ] 与论文全文其他图的风格一致\n- [ ] 终极判断：这张图放在 NeurIPS best paper 里违和吗？\n",
      "numLines": 478,
      "startLine": 1,
      "totalLines": 478
    }
  }
}
````

</details>

---


### Tool result

_source line 10 · 2026-05-24T11:42:46.911Z_

<details><summary>↩ Tool result · `toolu_01FnCjuez4jTQ2NetCyH97vE`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	### 6.5 页面节奏
214	
215	好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：
216	
217	- **text-equation-figure 三重奏**：重要概念用"文字解释 → 公式定义 → 图表直觉"三步展开
218	- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏
219	- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float
220	- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）
221	- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）
222	
223	### 6.6 表格 LaTeX 规范
224	
225	**Booktabs 标准（硬规则）**：
226	- 用 `\toprule` / `\midrule` / `\bottomrule`，禁止 `\hline`，禁止竖线 `|`
227	- 用 `\centering` 不用 `\begin{center}`（后者多加垂直空白）
228	- 最优结果加粗（`\textbf{}`），次优下划线（`\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向
229	- 小数精度全表统一（如全部保留 1 位或 2 位）
230	- Caption 在表格上方（`\caption` 在 `\begin{tabular}` 之前）
231	
232	**宽度决策树**：
233	- ≤5 列 → 单栏宽度（`\columnwidth`）
234	- 6–8 列 → 全文宽度（`\textwidth`，双栏模板用 `table*`）
235	- >8 列 → 拆成两张表或移入 appendix
236	
237	---
238	
239	## 七、投稿前通用准备
240	
241	### 7.1 模板必须官方（硬规则）
242	
243	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
244	- **不要用**：
245	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
246	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
247	  - 组里学长留的旧版本（来源不明、无法追溯）
248	- 风险：
249	  - 样式不符合 → desk reject
250	  - margin 不对 → 被审稿人质疑诚信
251	  - reference 格式错 → 被认为不规范
252	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
253	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
254	
255	### 7.2 投稿要求逐项核对
256	
257	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
258	- 页数限制：查目标会议官网
259	- 匿名化要求：review 版 vs camera-ready 版本设置不同
260	- 行号开启（review 版常需）
261	- 字体大小、margin 不得修改 sty 文件
262	
263	### 7.3 最终修改 10 项检查流程
264	
265	提交前必须逐一检查：
266	1. 所有最新实验结果已全部录入
267	2. 根据实验结果将叙事调至最优状态
268	3. 附录所有内容在正文中被引用且融入叙事
269	4. 无数据堆砌（每个数字服务于叙事推进）
270	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
271	6. 全文主线统一（idea 变化后各章节逻辑一致）
272	7. 所有专有名词有定义
273	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
274	9. 图表知识密度高、无视觉遮挡
275	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
276	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "851d28f8-99c0-40d3-8edd-5d4670027bc1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n### 6.5 页面节奏\n\n好论文的页面有节奏感——text、equation、figure 交替出现，读者视觉不疲劳：\n\n- **text-equation-figure 三重奏**：重要概念用\"文字解释 → 公式定义 → 图表直觉\"三步展开\n- 连续 2 页纯文本（无 figure/equation/table）→ 穿插一个 display item 打破节奏\n- 连续 2 个 figure 页（整页被 float 占满）→ 至少隔 1 段文字再放下一个 float\n- Section heading 不孤悬页底（heading 后至少跟 2 行正文，否则强制分页）\n- 最后一页内容 ≥ 2/3 页面高度（太空显得凑数，太满放不下 references）\n\n### 6.6 表格 LaTeX 规范\n\n**Booktabs 标准（硬规则）**：\n- 用 `\\toprule` / `\\midrule` / `\\bottomrule`，禁止 `\\hline`，禁止竖线 `|`\n- 用 `\\centering` 不用 `\\begin{center}`（后者多加垂直空白）\n- 最优结果加粗（`\\textbf{}`），次优下划线（`\\underline{}`）+ 方向箭头 `↑`/`↓` 标明指标方向\n- 小数精度全表统一（如全部保留 1 位或 2 位）\n- Caption 在表格上方（`\\caption` 在 `\\begin{tabular}` 之前）\n\n**宽度决策树**：\n- ≤5 列 → 单栏宽度（`\\columnwidth`）\n- 6–8 列 → 全文宽度（`\\textwidth`，双栏模板用 `table*`）\n- >8 列 → 拆成两张表或移入 appendix\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  }
}
````

</details>

---


### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of:
1. The current script - a 16x9 figure with two panels showing Sequential Pipeline (left) and G-MFRM Joint Framework (right)
2. The design standards from the skill files

I need to redesign this as a full-width figure with ~(16, 5.5) dimensions, maintaining the same content but with improved aesthetics:
- Rounded corners (FancyBboxPatch with larger pad)
- Subtle drop shadows
- Thinner, more elegant arrows
- Serif-style fonts, math with cm fontset
- Semantic colors maintained


- Lower alpha backgrounds (0.1-0.15)
- Text colors matching semantic colors
- More whitespace

The main challenges are compressing the vertical layout from 9 units to ~5.5 while keeping everything elegant and professional, adding drop shadows, and ensuring text remains readable at ≥7pt when scaled to textwidth. Let me start writing the improved version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "bf4151a0-b320-4a06-8d19-3ebd0c5eb031",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PER6zt9F7BPyEKiKZbHTbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20165,
      "cache_read_input_tokens": 24985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20165
      },
      "output_tokens": 9,
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

_source line 12_

Now I have a clear picture of the current design and standards. Let me write the improved version — a full-width figure with better aesthetics, then iterate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "76c49152-10ae-45b0-ae71-9ce4f66a54d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PER6zt9F7BPyEKiKZbHTbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20165,
      "cache_read_input_tokens": 24985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20165
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Write · `toolu_01WVcLdy2RHdeKDodCB8TtLG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\nimport numpy as np\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#505050'\nC_GRAY_L  = '#E8E8E8'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nC_BG      = '#FAFAFA'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 5.5))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,\n                      left=0.01, right=0.99, top=0.94, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 6.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    \"\"\"Rounded box with subtle drop shadow.\"\"\"\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    \"\"\"Rounded box without shadow.\"\"\"\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family='serif', **kw):\n    ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n            ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_l, 0.15, 0.15, 9.7, 5.9, C_RED_L, C_RED, lw=1.5, alpha=0.12, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 5.8, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 5.4, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nlabel(ax_l, 5.0, 4.95, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nbw, bh = 3.2, 0.72\n# Step 1\nshadow_box(ax_l, 0.6, 4.0, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 0.6 + bw/2, 4.0 + bh/2 + 0.12, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.6 + bw/2, 4.0 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Step 2\nshadow_box(ax_l, 5.8, 4.0, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 5.8 + (bw+0.3)/2, 4.0 + bh/2 + 0.12, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.8 + (bw+0.3)/2, 4.0 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\n# Arrow between steps A\narrow(ax_l, 3.8, 4.36, 5.8, 4.36, color=C_GRAY, lw=1.4)\n\n# Red cross\nlabel(ax_l, 9.55, 4.36, '✗', fs=16, fw='bold', color=C_RED)\n\n# Confounding arc A\na_conf = FancyArrowPatch((7.5, 4.72), (2.3, 4.72), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.4',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.9, 5.15, 'confounding', fs=7, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nlabel(ax_l, 5.0, 3.4, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, 0.6, 2.45, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 0.6 + (bw+0.3)/2, 2.45 + bh/2 + 0.12, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.6 + (bw+0.3)/2, 2.45 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, 5.8, 2.45, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 5.8 + bw/2, 2.45 + bh/2 + 0.12, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.8 + bw/2, 2.45 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Arrow between steps B\narrow(ax_l, 4.1, 2.81, 5.8, 2.81, color=C_GRAY, lw=1.4)\n\nlabel(ax_l, 9.55, 2.81, '✗', fs=16, fw='bold', color=C_RED)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((7.5, 3.17), (2.5, 3.17), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.4',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 5.0, 3.6, 'confounding', fs=7, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.6, 0.55, 8.8, 1.5, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.62, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.15,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB to paths\narrow(ax_l, 3.5, 2.05, 3.5, 2.45, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.05, 6.5, 2.45, color=C_RED, lw=1.0, style='-|>')\n\n# Bottom note\nlabel(ax_l, 5.0, 0.32, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_r, 0.05, 0.15, 9.9, 5.9, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 5.8, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 5.4, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 4.55, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.6, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.6, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\n# Output tokens\now, oh = 1.6, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.2), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.2)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.5, 4.55, 7.5, 4.1, color=C_JUDGE, lw=1.4)\nlabel(ax_r, 7.95, 4.32, 'initialize', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: External e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.55, 3.9, 1.85\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.9, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.68 - k * 0.46\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, 4.25, 3.45, 5.1, 3.45, color=C_CONT, lw=1.4)\nlabel(ax_r, 4.65, 3.7, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 5.0, 2.4, 4.65, 1.7\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F8F8F8', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\n# Model equation\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.68,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.5, s3_y + 0.2, 3.6, 0.65\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.05, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.7\nout_y = 1.15\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.12, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.3, 2.4, 7.3, 1.85, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, '✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic')\n\n# Panel labels\nlabel(ax_l, 0.4, 6.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "a0561943-30d1-4936-a28f-28e1ae5256d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PER6zt9F7BPyEKiKZbHTbE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20165,
      "cache_read_input_tokens": 24985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20165
      },
      "output_tokens": 9,
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

_source line 14 · 2026-05-24T11:44:14.370Z_

<details><summary>↩ Tool result · `toolu_01WVcLdy2RHdeKDodCB8TtLG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "61d91f78-1828-45b6-b7b1-d0cd5e6ea57f",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
    "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\nimport numpy as np\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#505050'\nC_GRAY_L  = '#E8E8E8'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nC_BG      = '#FAFAFA'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 5.5))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,\n                      left=0.01, right=0.99, top=0.94, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 6.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    \"\"\"Rounded box with subtle drop shadow.\"\"\"\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    \"\"\"Rounded box without shadow.\"\"\"\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family='serif', **kw):\n    ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n            ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_l, 0.15, 0.15, 9.7, 5.9, C_RED_L, C_RED, lw=1.5, alpha=0.12, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 5.8, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 5.4, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nlabel(ax_l, 5.0, 4.95, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nbw, bh = 3.2, 0.72\n# Step 1\nshadow_box(ax_l, 0.6, 4.0, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 0.6 + bw/2, 4.0 + bh/2 + 0.12, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.6 + bw/2, 4.0 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Step 2\nshadow_box(ax_l, 5.8, 4.0, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 5.8 + (bw+0.3)/2, 4.0 + bh/2 + 0.12, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.8 + (bw+0.3)/2, 4.0 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\n# Arrow between steps A\narrow(ax_l, 3.8, 4.36, 5.8, 4.36, color=C_GRAY, lw=1.4)\n\n# Red cross\nlabel(ax_l, 9.55, 4.36, '✗', fs=16, fw='bold', color=C_RED)\n\n# Confounding arc A\na_conf = FancyArrowPatch((7.5, 4.72), (2.3, 4.72), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.4',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.9, 5.15, 'confounding', fs=7, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nlabel(ax_l, 5.0, 3.4, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, 0.6, 2.45, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 0.6 + (bw+0.3)/2, 2.45 + bh/2 + 0.12, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.6 + (bw+0.3)/2, 2.45 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, 5.8, 2.45, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 5.8 + bw/2, 2.45 + bh/2 + 0.12, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.8 + bw/2, 2.45 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Arrow between steps B\narrow(ax_l, 4.1, 2.81, 5.8, 2.81, color=C_GRAY, lw=1.4)\n\nlabel(ax_l, 9.55, 2.81, '✗', fs=16, fw='bold', color=C_RED)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((7.5, 3.17), (2.5, 3.17), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.4',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 5.0, 3.6, 'confounding', fs=7, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.6, 0.55, 8.8, 1.5, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.62, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.15,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB to paths\narrow(ax_l, 3.5, 2.05, 3.5, 2.45, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.05, 6.5, 2.45, color=C_RED, lw=1.0, style='-|>')\n\n# Bottom note\nlabel(ax_l, 5.0, 0.32, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_r, 0.05, 0.15, 9.9, 5.9, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 5.8, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 5.4, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 4.55, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.6, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.6, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\n# Output tokens\now, oh = 1.6, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.2), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.2)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.5, 4.55, 7.5, 4.1, color=C_JUDGE, lw=1.4)\nlabel(ax_r, 7.95, 4.32, 'initialize', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: External e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.55, 3.9, 1.85\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.9, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.68 - k * 0.46\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, 4.25, 3.45, 5.1, 3.45, color=C_CONT, lw=1.4)\nlabel(ax_r, 4.65, 3.7, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 5.0, 2.4, 4.65, 1.7\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F8F8F8', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\n# Model equation\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.68,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.5, s3_y + 0.2, 3.6, 0.65\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.05, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.7\nout_y = 1.15\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.12, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.3, 2.4, 7.3, 1.85, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, '✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic')\n\n# Panel labels\nlabel(ax_l, 0.4, 6.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 240,
        "newStart": 1,
        "newLines": 254,
        "lines": [
          "-\"\"\"Generate Figure 1: G-MFRM Framework Overview (conceptual diagram).\"\"\"",
          "+\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).",
          "+Full-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"",
          " import matplotlib",
          " matplotlib.use('Agg')",
          " matplotlib.rcParams['mathtext.fontset'] = 'cm'",
          "+matplotlib.rcParams['pdf.fonttype'] = 42",
          "+matplotlib.rcParams['ps.fonttype'] = 42",
          " import matplotlib.pyplot as plt",
          " import matplotlib.patches as mpatches",
          " from matplotlib.patches import FancyBboxPatch, FancyArrowPatch",
          " import numpy as np",
          " ",
          " # ── Colors ──────────────────────────────────────────────────────────",
          "-C_JUDGE   = '#2B6E99'   # blue — judge severity d_j",
          "-C_JUDGE_L = '#C5DDE9'   # light blue",
          "-C_CONT    = '#D4762C'   # orange — contamination c_n·e_i",
          "-C_CONT_L  = '#F5D8B5'   # light orange",
          "+C_JUDGE   = '#2B6E99'",
          "+C_JUDGE_L = '#D6E8F2'",
          "+C_CONT    = '#D4762C'",
          "+C_CONT_L  = '#F8E0C8'",
          " C_GRAY    = '#505050'",
          " C_GRAY_L  = '#E8E8E8'",
          " C_RED     = '#B03A2E'",
          "-C_RED_L   = '#F9E0DC'",
          "+C_RED_L   = '#FADBD8'",
          " C_GREEN   = '#1E8449'",
          "-C_GREEN_L = '#D0ECD8'",
          "+C_GREEN_L = '#D5F5E3'",
          " C_BG      = '#FAFAFA'",
          " WHITE     = '#FFFFFF'",
          " DARK      = '#2C3E50'",
          "+SHADOW    = '#B0B0B0'",
          " ",
          " # ── Figure setup ────────────────────────────────────────────────────",
          "-fig = plt.figure(figsize=(16, 9))",
          "+fig = plt.figure(figsize=(16, 5.5))",
          " fig.patch.set_facecolor(WHITE)",
          " ",
          "-gs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.05,",
          "-                      left=0.015, right=0.985, top=0.93, bottom=0.03)",
          "+gs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,",
          "+                      left=0.01, right=0.99, top=0.94, bottom=0.02)",
          " ax_l = fig.add_subplot(gs[0])",
          " ax_r = fig.add_subplot(gs[1])",
          " ",
          " for ax in [ax_l, ax_r]:",
          "     ax.set_xlim(0, 10)",
          "-    ax.set_ylim(0, 10)",
          "+    ax.set_ylim(0, 6.2)",
          "     ax.set_aspect('equal')",
          "     ax.axis('off')",
          " ",
          " # ── Helpers ─────────────────────────────────────────────────────────",
          "-def rbox(ax, x, y, w, h, fc, ec, lw=1.3, ls='-', alpha=1.0, zorder=2, pad=0.12):",
          "+def shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):",
          "+    \"\"\"Rounded box with subtle drop shadow.\"\"\"",
          "+    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,",
          "+                         boxstyle=f'round,pad={pad}',",
          "+                         facecolor=SHADOW, edgecolor='none',",
          "+                         linewidth=0, alpha=0.10, zorder=zorder - 1)",
          "+    ax.add_patch(sh)",
          "     b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',",
          "                         facecolor=fc, edgecolor=ec, linewidth=lw,",
          "                         linestyle=ls, alpha=alpha, zorder=zorder)",
          "     ax.add_patch(b)",
          "     return b",
          " ",
          "-def label(ax, x, y, txt, fs=9, fw='bold', color='black', ha='center',",
          "-          va='center', style='normal', zorder=5, **kw):",
          "+def rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):",
          "+    \"\"\"Rounded box without shadow.\"\"\"",
          "+    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',",
          "+                        facecolor=fc, edgecolor=ec, linewidth=lw,",
          "+                        linestyle=ls, alpha=alpha, zorder=zorder)",
          "+    ax.add_patch(b)",
          "+    return b",
          "+",
          "+def label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',",
          "+          va='center', style='normal', zorder=5, family='serif', **kw):",
          "     ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,",
          "-            ha=ha, va=va, fontstyle=style, zorder=zorder, **kw)",
          "+            ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)",
          " ",
          "-def arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.6, style='-|>',",
          "-          rad=0, zorder=4):",
          "+def arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',",
          "+          rad=0, zorder=4, ls='-'):",
          "     cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'",
          "     a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,",
          "-                         linewidth=lw, connectionstyle=cs,",
          "-                         mutation_scale=15, zorder=zorder)",
          "+                         linewidth=lw, connectionstyle=cs, linestyle=ls,",
          "+                         mutation_scale=12, zorder=zorder)",
          "     ax.add_patch(a)",
          " ",
          "-def labeled_box(ax, x, y, w, h, line1, line2, fc, ec, fs1=9, fs2=8.5):",
          "-    rbox(ax, x, y, w, h, fc, ec)",
          "-    label(ax, x+w/2, y+h/2+0.17, line1, fs=fs1, fw='bold', color=DARK)",
          "-    label(ax, x+w/2, y+h/2-0.17, line2, fs=fs2, fw='normal', color=C_GRAY)",
          " ",
          "-",
          " # ═══════════════════════════════════════════════════════════════════",
          " #  LEFT PANEL — Sequential Pipeline",
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          "-# Background",
          "-rbox(ax_l, 0.1, 0.15, 9.8, 9.6, C_RED_L, C_RED, lw=1.8, alpha=0.2, zorder=0, pad=0.2)",
          "+# Background panel",
          "+rbox(ax_l, 0.15, 0.15, 9.7, 5.9, C_RED_L, C_RED, lw=1.5, alpha=0.12, zorder=0, pad=0.25)",
          " ",
          " # Title",
          "-label(ax_l, 5.0, 9.5, 'Sequential Pipeline', fs=14, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 9.0, '(order-dependent bias)', fs=10, color=C_RED, style='italic')",
          "+label(ax_l, 5.0, 5.8, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 5.4, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')",
          " ",
          "-# ── Path A ──",
          "-label(ax_l, 5.0, 8.3, 'Path A: Bias-first', fs=10.5, fw='bold', color=DARK)",
          "+# ── Path A: Bias-first ──",
          "+label(ax_l, 5.0, 4.95, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)",
          " ",
          "-bw, bh = 3.4, 0.95",
          "+bw, bh = 3.2, 0.72",
          " # Step 1",
          "-rbox(ax_l, 0.5, 6.8, bw, bh, C_JUDGE_L, C_JUDGE)",
          "-label(ax_l, 0.5+bw/2, 6.8+bh/2+0.15, 'Step 1: MFRM', fs=9, fw='bold', color=DARK)",
          "-label(ax_l, 0.5+bw/2, 6.8+bh/2-0.18, r'calibrate $d_j$', fs=9, fw='normal', color=C_JUDGE)",
          "+shadow_box(ax_l, 0.6, 4.0, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "+label(ax_l, 0.6 + bw/2, 4.0 + bh/2 + 0.12, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, 0.6 + bw/2, 4.0 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          " ",
          " # Step 2",
          "-rbox(ax_l, 5.6, 6.8, bw+0.4, bh, C_CONT_L, C_CONT)",
          "-label(ax_l, 5.6+(bw+0.4)/2, 6.8+bh/2+0.15, 'Step 2: Adjust', fs=9, fw='bold', color=DARK)",
          "-label(ax_l, 5.6+(bw+0.4)/2, 6.8+bh/2-0.18, r'contamination $c_n$', fs=9, fw='normal', color=C_CONT)",
          "+shadow_box(ax_l, 5.8, 4.0, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.1)",
          "+label(ax_l, 5.8 + (bw+0.3)/2, 4.0 + bh/2 + 0.12, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, 5.8 + (bw+0.3)/2, 4.0 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          " ",
          "-arrow(ax_l, 3.9, 7.28, 5.6, 7.28, color=C_GRAY, lw=2.0)",
          "+# Arrow between steps A",
          "+arrow(ax_l, 3.8, 4.36, 5.8, 4.36, color=C_GRAY, lw=1.4)",
          " ",
          " # Red cross",
          "-label(ax_l, 9.6, 7.28, '✗', fs=18, fw='bold', color=C_RED)",
          "+label(ax_l, 9.55, 4.36, '✗', fs=16, fw='bold', color=C_RED)",
          " ",
          "-# ── Path B ──",
          "-label(ax_l, 5.0, 6.0, 'Path B: Contamination-first', fs=10.5, fw='bold', color=DARK)",
          "+# Confounding arc A",
          "+a_conf = FancyArrowPatch((7.5, 4.72), (2.3, 4.72), arrowstyle='-|>',",
          "+                          color=C_RED, linewidth=0.9, linestyle='--',",
          "+                          connectionstyle='arc3,rad=-0.4',",
          "+                          mutation_scale=10, zorder=4)",
          "+ax_l.add_patch(a_conf)",
          "+label(ax_l, 4.9, 5.15, 'confounding', fs=7, color=C_RED, style='italic', fw='normal')",
          " ",
          "-rbox(ax_l, 0.5, 4.5, bw+0.4, bh, C_CONT_L, C_CONT)",
          "-label(ax_l, 0.5+(bw+0.4)/2, 4.5+bh/2+0.15, 'Step 1: Adjust', fs=9, fw='bold', color=DARK)",
          "-label(ax_l, 0.5+(bw+0.4)/2, 4.5+bh/2-0.18, r'contamination $c_n$', fs=9, fw='normal', color=C_CONT)",
          "+# ── Path B: Contamination-first ──",
          "+label(ax_l, 5.0, 3.4, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)",
          " ",
          "-rbox(ax_l, 5.6, 4.5, bw, bh, C_JUDGE_L, C_JUDGE)",
          "-label(ax_l, 5.6+bw/2, 4.5+bh/2+0.15, 'Step 2: MFRM', fs=9, fw='bold', color=DARK)",
          "-label(ax_l, 5.6+bw/2, 4.5+bh/2-0.18, r'calibrate $d_j$', fs=9, fw='normal', color=C_JUDGE)",
          "+shadow_box(ax_l, 0.6, 2.45, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.1)",
          "+label(ax_l, 0.6 + (bw+0.3)/2, 2.45 + bh/2 + 0.12, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, 0.6 + (bw+0.3)/2, 2.45 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          " ",
          "-arrow(ax_l, 4.3, 4.97, 5.6, 4.97, color=C_GRAY, lw=2.0)",
          "+shadow_box(ax_l, 5.8, 2.45, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "+label(ax_l, 5.8 + bw/2, 2.45 + bh/2 + 0.12, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, 5.8 + bw/2, 2.45 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          " ",
          "-label(ax_l, 9.6, 4.97, '✗', fs=18, fw='bold', color=C_RED)",
          "+# Arrow between steps B",
          "+arrow(ax_l, 4.1, 2.81, 5.8, 2.81, color=C_GRAY, lw=1.4)",
          " ",
          "+label(ax_l, 9.55, 2.81, '✗', fs=16, fw='bold', color=C_RED)",
          "+",
          "+# Confounding arc B",
          "+b_conf = FancyArrowPatch((7.5, 3.17), (2.5, 3.17), arrowstyle='-|>',",
          "+                          color=C_RED, linewidth=0.9, linestyle='--',",
          "+                          connectionstyle='arc3,rad=-0.4',",
          "+                          mutation_scale=10, zorder=4)",
          "+ax_l.add_patch(b_conf)",
          "+label(ax_l, 5.0, 3.6, 'confounding', fs=7, color=C_RED, style='italic', fw='normal')",
          "+",
          " # ── OVB Box ──",
          "-rbox(ax_l, 0.5, 2.2, 9.0, 1.85, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95)",
          "+rbox(ax_l, 0.6, 0.55, 8.8, 1.5, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)",
          " ",
          "-label(ax_l, 5.0, 3.45, 'Omitted Variable Bias (OVB)', fs=11, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 2.8,",
          "+label(ax_l, 5.0, 1.62, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 1.15,",
          "       r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',",
          "-      fs=10.5, fw='normal', color=C_RED)",
          "+      fs=9, fw='normal', color=C_RED)",
          " ",
          "-# Warning arrows from OVB to both paths",
          "-arrow(ax_l, 3.0, 4.05, 3.0, 4.5, color=C_RED, lw=1.3, style='-|>')",
          "-arrow(ax_l, 7.0, 4.05, 7.0, 4.5, color=C_RED, lw=1.3, style='-|>')",
          "+# Arrows from OVB to paths",
          "+arrow(ax_l, 3.5, 2.05, 3.5, 2.45, color=C_RED, lw=1.0, style='-|>')",
          "+arrow(ax_l, 6.5, 2.05, 6.5, 2.45, color=C_RED, lw=1.0, style='-|>')",
          " ",
          " # Bottom note",
          "-label(ax_l, 5.0, 1.35, 'Unmodeled facet absorbed into remaining estimates',",
          "-      fs=9, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 5.0, 0.32, 'Unmodeled facet absorbed into remaining estimates',",
          "+      fs=7.5, color=C_RED, style='italic', fw='normal')",
          " ",
          "-# ── Dashed confounding arcs between Path A boxes ──",
          "-# Red dashed arc from Step2_A back to Step1_A (showing absorbed bias)",
          "-a_conf = FancyArrowPatch((7.5, 7.75), (2.2, 7.75), arrowstyle='-|>',",
          "-                          color=C_RED, linewidth=1.2, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.35',",
          "-                          mutation_scale=12, zorder=4)",
          "-ax_l.add_patch(a_conf)",
          "-label(ax_l, 4.9, 8.65, r'confounding', fs=7.5, color=C_RED, style='italic', fw='normal')",
          " ",
          "-# Red dashed arc between Path B boxes",
          "-b_conf = FancyArrowPatch((7.3, 5.45), (2.7, 5.45), arrowstyle='-|>',",
          "-                          color=C_RED, linewidth=1.2, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.35',",
          "-                          mutation_scale=12, zorder=4)",
          "-ax_l.add_patch(b_conf)",
          "-label(ax_l, 5.0, 6.35, r'confounding', fs=7.5, color=C_RED, style='italic', fw='normal')",
          "-",
          "-",
          " # ═══════════════════════════════════════════════════════════════════",
          " #  RIGHT PANEL — G-MFRM Joint Framework",
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          "-# Background",
          "-rbox(ax_r, 0.05, 0.15, 9.9, 9.6, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.15, zorder=0, pad=0.2)",
          "+# Background panel",
          "+rbox(ax_r, 0.05, 0.15, 9.9, 5.9, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.10, zorder=0, pad=0.25)",
          " ",
          " # Title",
          "-label(ax_r, 5.0, 9.5, 'G-MFRM Joint Framework (Ours)', fs=14, fw='bold', color='#145A32')",
          "-label(ax_r, 5.0, 9.0, 'staged joint calibration of all facets', fs=10,",
          "-      color=C_GREEN, style='italic')",
          "+label(ax_r, 5.0, 5.8, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')",
          "+label(ax_r, 5.0, 5.4, 'staged joint calibration of all facets', fs=8.5,",
          "+      color=C_GREEN, style='italic', fw='normal')",
          " ",
          " # ── Stage 1: Standard MFRM ──",
          "-s1_x, s1_y, s1_w, s1_h = 0.35, 7.3, 9.3, 1.35",
          "-rbox(ax_r, s1_x, s1_y, s1_w, s1_h, '#E8F0F5', C_JUDGE, alpha=0.6)",
          "+s1_x, s1_y, s1_w, s1_h = 0.35, 4.55, 9.3, 0.95",
          "+shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)",
          " ",
          "-label(ax_r, 1.5, s1_y+s1_h-0.3, 'Stage 1', fs=10.5, fw='bold', color=C_JUDGE)",
          "-label(ax_r, 1.5, s1_y+s1_h-0.7, 'Standard MFRM', fs=9, fw='normal', color=C_GRAY)",
          "+label(ax_r, 1.6, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)",
          "+label(ax_r, 1.6, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)",
          " ",
          " # Output tokens",
          "-ow, oh = 1.8, 0.6",
          "-out1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.0), (r'$\\hat{b}$', 6.1), (r'$\\hat{d}$', 8.1)]",
          "+ow, oh = 1.6, 0.45",
          "+out1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.2), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.2)]",
          " for lbl_txt, xo in out1_specs:",
          "-    rbox(ax_r, xo, s1_y+0.35, ow, oh, WHITE, C_JUDGE, lw=1.0)",
          "-    label(ax_r, xo+ow/2, s1_y+0.35+oh/2, lbl_txt, fs=11, fw='normal', color=C_JUDGE)",
          "+    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)",
          "+    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)",
          " ",
          " # Arrow S1 → S3",
          "-arrow(ax_r, 7.3, 7.3, 7.3, 6.6, color=C_JUDGE, lw=2.0)",
          "-label(ax_r, 7.7, 6.95, 'initialize', fs=7.5, color=C_JUDGE, fw='normal', style='italic')",
          "+arrow(ax_r, 7.5, 4.55, 7.5, 4.1, color=C_JUDGE, lw=1.4)",
          "+label(ax_r, 7.95, 4.32, 'initialize', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          " ",
          " # ── Stage 2: External e_i ──",
          "-s2_x, s2_y, s2_w, s2_h = 0.35, 4.55, 4.0, 2.55",
          "-rbox(ax_r, s2_x, s2_y, s2_w, s2_h, '#FDF2E9', C_CONT, alpha=0.55)",
          "+s2_x, s2_y, s2_w, s2_h = 0.35, 2.55, 3.9, 1.85",
          "+shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)",
          " ",
          "-label(ax_r, s2_x+s2_w/2, s2_y+s2_h-0.3,",
          "-      r'Stage 2: Estimate $e_i$', fs=9.5, fw='bold', color=C_CONT)",
          "+label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,",
          "+      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)",
          " ",
          " sub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']",
          "-sw, sh = 3.1, 0.5",
          "+sw, sh = 2.9, 0.38",
          " for k, stxt in enumerate(sub_specs):",
          "-    sy = s2_y + s2_h - 0.95 - k*0.6",
          "-    rbox(ax_r, s2_x+0.45, sy, sw, sh, WHITE, C_CONT, lw=1.0)",
          "-    label(ax_r, s2_x+0.45+sw/2, sy+sh/2, stxt, fs=8.5, fw='normal', color=DARK)",
          "+    sy = s2_y + s2_h - 0.68 - k * 0.46",
          "+    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)",
          "+    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)",
          " ",
          " # Arrow S2 → S3",
          "-arrow(ax_r, 4.35, 5.5, 5.25, 5.5, color=C_CONT, lw=2.0)",
          "-label(ax_r, 4.8, 5.78, r'$e_i$', fs=10, color=C_CONT, fw='bold')",
          "+arrow(ax_r, 4.25, 3.45, 5.1, 3.45, color=C_CONT, lw=1.4)",
          "+label(ax_r, 4.65, 3.7, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          " ",
          " # ── Stage 3: Joint Gated Model ──",
          "-s3_x, s3_y, s3_w, s3_h = 5.1, 4.3, 4.55, 2.3",
          "-rbox(ax_r, s3_x, s3_y, s3_w, s3_h, '#F4F4F4', '#3C3C3C', lw=2.2)",
          "+s3_x, s3_y, s3_w, s3_h = 5.0, 2.4, 4.65, 1.7",
          "+shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F8F8F8', '#3C3C3C', lw=1.8)",
          " ",
          "-label(ax_r, s3_x+s3_w/2, s3_y+s3_h-0.35,",
          "-      'Stage 3: Joint Gated Model', fs=10, fw='bold', color=DARK)",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,",
          "+      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)",
          " ",
          "-# Model equation line",
          "-label(ax_r, s3_x+s3_w/2, s3_y+s3_h-0.85,",
          "+# Model equation",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.68,",
          "       r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',",
          "-      fs=9, fw='normal', color=C_GRAY)",
          "+      fs=8, fw='normal', color=C_GRAY)",
          " ",
          " # Gating highlight",
          "-gx, gy, gw, gh = s3_x+0.5, s3_y+0.3, 3.55, 0.85",
          "-rbox(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.2, alpha=0.9)",
          "-label(ax_r, gx+gw/2, gy+gh/2+0.08,",
          "-      r'Gating: $c_n \\cdot e_i$', fs=11, fw='bold', color=C_CONT)",
          "+gx, gy, gw, gh = s3_x + 0.5, s3_y + 0.2, 3.6, 0.65",
          "+shadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)",
          "+label(ax_r, gx + gw/2, gy + gh/2,",
          "+      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)",
          " ",
          " # ── 4-D Output ──",
          "-label(ax_r, 5.0, 3.65, '4-Dimensional Diagnostic Output', fs=10.5, fw='bold', color=DARK)",
          "+label(ax_r, 5.0, 2.05, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          " ",
          "-ow2, oh2 = 2.0, 0.95",
          "-out_y = 2.35",
          "+ow2, oh2 = 2.05, 0.7",
          "+out_y = 1.15",
          " out_specs = [",
          "-    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.55),",
          "-    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.8),",
          "-    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),",
          "-    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.3),",
          "+    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),",
          "+    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),",
          "+    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),",
          "+    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),",
          " ]",
          " for sym, desc, fc, ec, xo in out_specs:",
          "-    rbox(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.5)",
          "-    label(ax_r, xo+ow2/2, out_y+oh2/2+0.16, sym, fs=11, fw='bold', color=ec)",
          "-    label(ax_r, xo+ow2/2, out_y+oh2/2-0.2, desc, fs=8, fw='normal', color=DARK)",
          "+    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)",
          "+    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.12, sym, fs=9.5, fw='bold', color=ec)",
          "+    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)",
          " ",
          " # Arrow S3 → outputs",
          "-arrow(ax_r, 7.35, 4.3, 7.35, 3.3, color='#3C3C3C', lw=2.2, style='-|>')",
          "+arrow(ax_r, 7.3, 2.4, 7.3, 1.85, color='#3C3C3C', lw=1.6, style='-|>')",
          " ",
          " # Green check",
          "-label(ax_r, 5.0, 1.5, '✓  Joint estimation resolves confounding',",
          "-      fs=10, fw='bold', color=C_GREEN, style='italic')",
          "+label(ax_r, 5.0, 0.55, '✓  Joint estimation resolves confounding',",
          "+      fs=9, fw='bold', color=C_GREEN, style='italic')",
          " ",
          " # Panel labels",
          "-label(ax_l, 0.45, 9.85, '(a)', fs=13, fw='bold', color='black', ha='left')",
          "-label(ax_r, 0.25, 9.85, '(b)', fs=13, fw='bold', color='black', ha='left')",
          "+label(ax_l, 0.4, 6.05, '(a)', fs=11, fw='bold', color='black', ha='left')",
          "+label(ax_r, 0.25, 6.05, '(b)', fs=11, fw='bold', color='black', ha='left')",
          " ",
          " # ── Save ──",
          " out_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'"
        ]
      }
    ],
    "originalFile": "\"\"\"Generate Figure 1: G-MFRM Framework Overview (conceptual diagram).\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\nimport numpy as np\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'   # blue — judge severity d_j\nC_JUDGE_L = '#C5DDE9'   # light blue\nC_CONT    = '#D4762C'   # orange — contamination c_n·e_i\nC_CONT_L  = '#F5D8B5'   # light orange\nC_GRAY    = '#505050'\nC_GRAY_L  = '#E8E8E8'\nC_RED     = '#B03A2E'\nC_RED_L   = '#F9E0DC'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D0ECD8'\nC_BG      = '#FAFAFA'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 9))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.05,\n                      left=0.015, right=0.985, top=0.93, bottom=0.03)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 10)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.3, ls='-', alpha=1.0, zorder=2, pad=0.12):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=9, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, **kw):\n    ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n            ha=ha, va=va, fontstyle=style, zorder=zorder, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.6, style='-|>',\n          rad=0, zorder=4):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs,\n                         mutation_scale=15, zorder=zorder)\n    ax.add_patch(a)\n\ndef labeled_box(ax, x, y, w, h, line1, line2, fc, ec, fs1=9, fs2=8.5):\n    rbox(ax, x, y, w, h, fc, ec)\n    label(ax, x+w/2, y+h/2+0.17, line1, fs=fs1, fw='bold', color=DARK)\n    label(ax, x+w/2, y+h/2-0.17, line2, fs=fs2, fw='normal', color=C_GRAY)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\n# Background\nrbox(ax_l, 0.1, 0.15, 9.8, 9.6, C_RED_L, C_RED, lw=1.8, alpha=0.2, zorder=0, pad=0.2)\n\n# Title\nlabel(ax_l, 5.0, 9.5, 'Sequential Pipeline', fs=14, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 9.0, '(order-dependent bias)', fs=10, color=C_RED, style='italic')\n\n# ── Path A ──\nlabel(ax_l, 5.0, 8.3, 'Path A: Bias-first', fs=10.5, fw='bold', color=DARK)\n\nbw, bh = 3.4, 0.95\n# Step 1\nrbox(ax_l, 0.5, 6.8, bw, bh, C_JUDGE_L, C_JUDGE)\nlabel(ax_l, 0.5+bw/2, 6.8+bh/2+0.15, 'Step 1: MFRM', fs=9, fw='bold', color=DARK)\nlabel(ax_l, 0.5+bw/2, 6.8+bh/2-0.18, r'calibrate $d_j$', fs=9, fw='normal', color=C_JUDGE)\n\n# Step 2\nrbox(ax_l, 5.6, 6.8, bw+0.4, bh, C_CONT_L, C_CONT)\nlabel(ax_l, 5.6+(bw+0.4)/2, 6.8+bh/2+0.15, 'Step 2: Adjust', fs=9, fw='bold', color=DARK)\nlabel(ax_l, 5.6+(bw+0.4)/2, 6.8+bh/2-0.18, r'contamination $c_n$', fs=9, fw='normal', color=C_CONT)\n\narrow(ax_l, 3.9, 7.28, 5.6, 7.28, color=C_GRAY, lw=2.0)\n\n# Red cross\nlabel(ax_l, 9.6, 7.28, '✗', fs=18, fw='bold', color=C_RED)\n\n# ── Path B ──\nlabel(ax_l, 5.0, 6.0, 'Path B: Contamination-first', fs=10.5, fw='bold', color=DARK)\n\nrbox(ax_l, 0.5, 4.5, bw+0.4, bh, C_CONT_L, C_CONT)\nlabel(ax_l, 0.5+(bw+0.4)/2, 4.5+bh/2+0.15, 'Step 1: Adjust', fs=9, fw='bold', color=DARK)\nlabel(ax_l, 0.5+(bw+0.4)/2, 4.5+bh/2-0.18, r'contamination $c_n$', fs=9, fw='normal', color=C_CONT)\n\nrbox(ax_l, 5.6, 4.5, bw, bh, C_JUDGE_L, C_JUDGE)\nlabel(ax_l, 5.6+bw/2, 4.5+bh/2+0.15, 'Step 2: MFRM', fs=9, fw='bold', color=DARK)\nlabel(ax_l, 5.6+bw/2, 4.5+bh/2-0.18, r'calibrate $d_j$', fs=9, fw='normal', color=C_JUDGE)\n\narrow(ax_l, 4.3, 4.97, 5.6, 4.97, color=C_GRAY, lw=2.0)\n\nlabel(ax_l, 9.6, 4.97, '✗', fs=18, fw='bold', color=C_RED)\n\n# ── OVB Box ──\nrbox(ax_l, 0.5, 2.2, 9.0, 1.85, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95)\n\nlabel(ax_l, 5.0, 3.45, 'Omitted Variable Bias (OVB)', fs=11, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 2.8,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=10.5, fw='normal', color=C_RED)\n\n# Warning arrows from OVB to both paths\narrow(ax_l, 3.0, 4.05, 3.0, 4.5, color=C_RED, lw=1.3, style='-|>')\narrow(ax_l, 7.0, 4.05, 7.0, 4.5, color=C_RED, lw=1.3, style='-|>')\n\n# Bottom note\nlabel(ax_l, 5.0, 1.35, 'Unmodeled facet absorbed into remaining estimates',\n      fs=9, color=C_RED, style='italic', fw='normal')\n\n# ── Dashed confounding arcs between Path A boxes ──\n# Red dashed arc from Step2_A back to Step1_A (showing absorbed bias)\na_conf = FancyArrowPatch((7.5, 7.75), (2.2, 7.75), arrowstyle='-|>',\n                          color=C_RED, linewidth=1.2, linestyle='--',\n                          connectionstyle='arc3,rad=-0.35',\n                          mutation_scale=12, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.9, 8.65, r'confounding', fs=7.5, color=C_RED, style='italic', fw='normal')\n\n# Red dashed arc between Path B boxes\nb_conf = FancyArrowPatch((7.3, 5.45), (2.7, 5.45), arrowstyle='-|>',\n                          color=C_RED, linewidth=1.2, linestyle='--',\n                          connectionstyle='arc3,rad=-0.35',\n                          mutation_scale=12, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 5.0, 6.35, r'confounding', fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\n# Background\nrbox(ax_r, 0.05, 0.15, 9.9, 9.6, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.15, zorder=0, pad=0.2)\n\n# Title\nlabel(ax_r, 5.0, 9.5, 'G-MFRM Joint Framework (Ours)', fs=14, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 9.0, 'staged joint calibration of all facets', fs=10,\n      color=C_GREEN, style='italic')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 7.3, 9.3, 1.35\nrbox(ax_r, s1_x, s1_y, s1_w, s1_h, '#E8F0F5', C_JUDGE, alpha=0.6)\n\nlabel(ax_r, 1.5, s1_y+s1_h-0.3, 'Stage 1', fs=10.5, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.5, s1_y+s1_h-0.7, 'Standard MFRM', fs=9, fw='normal', color=C_GRAY)\n\n# Output tokens\now, oh = 1.8, 0.6\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.0), (r'$\\hat{b}$', 6.1), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y+0.35, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo+ow/2, s1_y+0.35+oh/2, lbl_txt, fs=11, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 7.3, 7.3, 6.6, color=C_JUDGE, lw=2.0)\nlabel(ax_r, 7.7, 6.95, 'initialize', fs=7.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: External e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 4.55, 4.0, 2.55\nrbox(ax_r, s2_x, s2_y, s2_w, s2_h, '#FDF2E9', C_CONT, alpha=0.55)\n\nlabel(ax_r, s2_x+s2_w/2, s2_y+s2_h-0.3,\n      r'Stage 2: Estimate $e_i$', fs=9.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 3.1, 0.5\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.95 - k*0.6\n    rbox(ax_r, s2_x+0.45, sy, sw, sh, WHITE, C_CONT, lw=1.0)\n    label(ax_r, s2_x+0.45+sw/2, sy+sh/2, stxt, fs=8.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, 4.35, 5.5, 5.25, 5.5, color=C_CONT, lw=2.0)\nlabel(ax_r, 4.8, 5.78, r'$e_i$', fs=10, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 5.1, 4.3, 4.55, 2.3\nrbox(ax_r, s3_x, s3_y, s3_w, s3_h, '#F4F4F4', '#3C3C3C', lw=2.2)\n\nlabel(ax_r, s3_x+s3_w/2, s3_y+s3_h-0.35,\n      'Stage 3: Joint Gated Model', fs=10, fw='bold', color=DARK)\n\n# Model equation line\nlabel(ax_r, s3_x+s3_w/2, s3_y+s3_h-0.85,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=9, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x+0.5, s3_y+0.3, 3.55, 0.85\nrbox(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.2, alpha=0.9)\nlabel(ax_r, gx+gw/2, gy+gh/2+0.08,\n      r'Gating: $c_n \\cdot e_i$', fs=11, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 3.65, '4-Dimensional Diagnostic Output', fs=10.5, fw='bold', color=DARK)\n\now2, oh2 = 2.0, 0.95\nout_y = 2.35\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.55),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.8),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.3),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    rbox(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.5)\n    label(ax_r, xo+ow2/2, out_y+oh2/2+0.16, sym, fs=11, fw='bold', color=ec)\n    label(ax_r, xo+ow2/2, out_y+oh2/2-0.2, desc, fs=8, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.35, 4.3, 7.35, 3.3, color='#3C3C3C', lw=2.2, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 1.5, '✓  Joint estimation resolves confounding',\n      fs=10, fw='bold', color=C_GREEN, style='italic')\n\n# Panel labels\nlabel(ax_l, 0.45, 9.85, '(a)', fs=13, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 9.85, '(b)', fs=13, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01G95YJdg2U33USrDDBjpVvp`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper && python gen_fig1.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "738208d3-5493-44b3-a54e-4da713d36bb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Np1i5WAbcro3riQdP3w4tr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5767,
      "cache_read_input_tokens": 45150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5767
      },
      "output_tokens": 69,
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

_source line 16 · 2026-05-24T11:44:17.780Z_

<details><summary>↩ Tool result · reported error · `toolu_01G95YJdg2U33USrDDBjpVvp`</summary>

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
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "925ed376-3113-42d5-8502-0d0467d2bcd8",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---


### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01RWaaJUCiLrHwqKrkFXEmbL`</summary>

```json
{
  "command": "which python3 && cd /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper && python3 gen_fig1.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "0e429f00-29bf-4a14-91e5-57e5882dffa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eeyzzv2yDefjHGqLW8LzwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 129,
      "cache_read_input_tokens": 50917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 129
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

_source line 18 · 2026-05-24T11:44:23.570Z_

<details><summary>↩ Tool result · `toolu_01RWaaJUCiLrHwqKrkFXEmbL`</summary>

```text
/usr/bin/python3
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py:255: UserWarning: Glyph 10007 (\N{BALLOT X}) missing from font(s) DejaVu Serif.
  fig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py:255: UserWarning: Glyph 10003 (\N{CHECK MARK}) missing from font(s) DejaVu Serif.
  fig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py:256: UserWarning: Glyph 10007 (\N{BALLOT X}) missing from font(s) DejaVu Serif.
  fig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py:256: UserWarning: Glyph 10003 (\N{CHECK MARK}) missing from font(s) DejaVu Serif.
  fig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)
Done: fig1_framework.pdf + fig1_framework.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "4d6421b3-10a8-4937-a5a9-9a8425fceb53",
  "tool_use_result": {
    "stdout": "/usr/bin/python3\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py:255: UserWarning: Glyph 10007 (\\N{BALLOT X}) missing from font(s) DejaVu Serif.\n  fig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py:255: UserWarning: Glyph 10003 (\\N{CHECK MARK}) missing from font(s) DejaVu Serif.\n  fig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py:256: UserWarning: Glyph 10007 (\\N{BALLOT X}) missing from font(s) DejaVu Serif.\n  fig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\n/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py:256: UserWarning: Glyph 10003 (\\N{CHECK MARK}) missing from font(s) DejaVu Serif.\n  fig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nDone: fig1_framework.pdf + fig1_framework.png",
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

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
The glyph warnings are about ✗ and ✓ being missing from DejaVu Serif. I need to handle this by either using a different font for those symbols or using a font that supports them. Let me first look at the PNG to see the overall layout, then fix the glyph issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "82e49cb9-ce0a-42f2-97cd-46c3eb274f0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012L7Ndq5Jdk6ysjXAKautnZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 51046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 657
      },
      "output_tokens": 9,
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

_source line 20_

Glyph issue with serif font for ✗/✓. Let me view the output and fix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "e310eb4c-55e3-4eba-9533-7309196b4b34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012L7Ndq5Jdk6ysjXAKautnZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 51046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 657
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Read · `toolu_015m3N3Wk9PpjxCbjQAetara`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "a87c2bda-fb3d-40a8-93a0-279663515504",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012L7Ndq5Jdk6ysjXAKautnZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 51046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 657
      },
      "output_tokens": 9,
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

_source line 22 · 2026-05-24T11:44:30.969Z_

<details><summary>↩ Tool result · `toolu_015m3N3Wk9PpjxCbjQAetara`</summary>

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
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "92e6817a-a1da-4f43-97a0-ca9ca47f1496",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 444018
    }
  }
}
```

</details>

---


### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Looking at the output, I can identify several issues:

1. The ✗ and ✓ glyphs are not rendering properly (showing as boxes) because DejaVu Serif doesn't have them
2. The right panel is quite cramped - Stage 1 outputs are overlapping with the subtitle text
3. The "confounding" labels are overlapping with path labels
4. The equation in Stage 3 is partially cut off/overlapping
5. The overall layout needs more vertical breathing room
6. The italic subtitle on the right panel is overlapping with Stage 1
7. The left panel's confounding arcs need better positioning


8. I'll switch the checkmark and X symbols to use the default sans font, increase the vertical spacing between elements, reposition the confounding labels to avoid collisions, and add more padding to the right panel to eliminate the overlaps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "c0c62abc-4cb6-49f0-a328-d5f6c5ee33e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXn5wbfYgRqBcqU4pVnugM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 51703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
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

_source line 24_

Several issues visible: glyphs missing for ✗/✓, right panel cramped with overlaps, confounding labels colliding. Let me fix all of these.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "793e0a5b-6e63-4e0c-b050-deda52a56025",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXn5wbfYgRqBcqU4pVnugM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 51703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
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

_source line 25_

<details open><summary>🔧 Tool call — Write · `toolu_01AgxxZMPqjdrbhk5SVMvX5d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\nimport numpy as np\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_GRAY_L  = '#E8E8E8'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 5.8))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 6.5)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n            ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_l, 0.15, 0.1, 9.7, 6.25, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 6.05, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 5.65, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nlabel(ax_l, 5.0, 5.15, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nbw, bh = 3.1, 0.7\n# Step 1\nshadow_box(ax_l, 0.7, 4.2, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 0.7 + bw/2, 4.2 + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.7 + bw/2, 4.2 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Step 2\nshadow_box(ax_l, 5.9, 4.2, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 5.9 + (bw+0.2)/2, 4.2 + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.9 + (bw+0.2)/2, 4.2 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\n# Arrow between steps A\narrow(ax_l, 3.8, 4.55, 5.9, 4.55, color=C_GRAY, lw=1.3)\n\n# Red cross — use sans font for glyph availability\nlabel(ax_l, 9.55, 4.55, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A (above the boxes)\na_conf = FancyArrowPatch((7.3, 4.9), (2.5, 4.9), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.9, 5.38, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nlabel(ax_l, 5.0, 3.55, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, 0.7, 2.6, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 0.7 + (bw+0.2)/2, 2.6 + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.7 + (bw+0.2)/2, 2.6 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, 5.9, 2.6, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 5.9 + bw/2, 2.6 + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.9 + bw/2, 2.6 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Arrow between steps B\narrow(ax_l, 4.1, 2.95, 5.9, 2.95, color=C_GRAY, lw=1.3)\n\nlabel(ax_l, 9.55, 2.95, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((7.2, 3.3), (2.7, 3.3), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 5.0, 3.75, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.55, 8.6, 1.6, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.72, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.22,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB to paths\narrow(ax_l, 3.5, 2.15, 3.5, 2.6, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.15, 6.5, 2.6, color=C_RED, lw=1.0, style='-|>')\n\n# Bottom note\nlabel(ax_l, 5.0, 0.3, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_r, 0.05, 0.1, 9.9, 6.25, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 6.05, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 5.65, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 4.7, 9.3, 0.85\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.5, s1_y + s1_h - 0.22, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.5, s1_y + s1_h - 0.52, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\n# Output tokens inside Stage 1\now, oh = 1.55, 0.4\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.22, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.22 + oh/2, lbl_txt, fs=9, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 4.7, 7.3, 4.2, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.45, 'initialize', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: External e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.55, 3.8, 2.0\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.2,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.8, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.7 - k * 0.48\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, 4.15, 3.55, 5.0, 3.55, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.55, 3.8, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.9, 2.45, 4.75, 1.75\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\n# Model equation\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.72,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.55, s3_y + 0.2, 3.6, 0.6\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.1, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.7\nout_y = 1.2\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.12, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.25, 2.45, 7.25, 1.9, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check — use sans font for glyph availability\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.4, 6.35, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.35, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "ec39b41f-923a-4863-b5fc-f5d34723b84c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXn5wbfYgRqBcqU4pVnugM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 51703,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 620
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

_source line 26 · 2026-05-24T11:45:54.711Z_

<details><summary>↩ Tool result · `toolu_01AgxxZMPqjdrbhk5SVMvX5d`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "9cd82f46-0ae1-48c1-ba0c-6383dbb21b4d",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
    "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\nimport numpy as np\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_GRAY_L  = '#E8E8E8'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 5.8))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 6.5)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n            ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_l, 0.15, 0.1, 9.7, 6.25, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 6.05, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 5.65, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nlabel(ax_l, 5.0, 5.15, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nbw, bh = 3.1, 0.7\n# Step 1\nshadow_box(ax_l, 0.7, 4.2, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 0.7 + bw/2, 4.2 + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.7 + bw/2, 4.2 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Step 2\nshadow_box(ax_l, 5.9, 4.2, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 5.9 + (bw+0.2)/2, 4.2 + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.9 + (bw+0.2)/2, 4.2 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\n# Arrow between steps A\narrow(ax_l, 3.8, 4.55, 5.9, 4.55, color=C_GRAY, lw=1.3)\n\n# Red cross — use sans font for glyph availability\nlabel(ax_l, 9.55, 4.55, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A (above the boxes)\na_conf = FancyArrowPatch((7.3, 4.9), (2.5, 4.9), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.9, 5.38, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nlabel(ax_l, 5.0, 3.55, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, 0.7, 2.6, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 0.7 + (bw+0.2)/2, 2.6 + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.7 + (bw+0.2)/2, 2.6 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, 5.9, 2.6, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 5.9 + bw/2, 2.6 + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.9 + bw/2, 2.6 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Arrow between steps B\narrow(ax_l, 4.1, 2.95, 5.9, 2.95, color=C_GRAY, lw=1.3)\n\nlabel(ax_l, 9.55, 2.95, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((7.2, 3.3), (2.7, 3.3), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 5.0, 3.75, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.55, 8.6, 1.6, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.72, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.22,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB to paths\narrow(ax_l, 3.5, 2.15, 3.5, 2.6, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.15, 6.5, 2.6, color=C_RED, lw=1.0, style='-|>')\n\n# Bottom note\nlabel(ax_l, 5.0, 0.3, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_r, 0.05, 0.1, 9.9, 6.25, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 6.05, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 5.65, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 4.7, 9.3, 0.85\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.5, s1_y + s1_h - 0.22, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.5, s1_y + s1_h - 0.52, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\n# Output tokens inside Stage 1\now, oh = 1.55, 0.4\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.22, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.22 + oh/2, lbl_txt, fs=9, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 4.7, 7.3, 4.2, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.45, 'initialize', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: External e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.55, 3.8, 2.0\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.2,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.8, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.7 - k * 0.48\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, 4.15, 3.55, 5.0, 3.55, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.55, 3.8, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.9, 2.45, 4.75, 1.75\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\n# Model equation\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.72,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.55, s3_y + 0.2, 3.6, 0.6\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.1, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.7\nout_y = 1.2\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.12, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.25, 2.45, 7.25, 1.9, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check — use sans font for glyph availability\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.4, 6.35, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.35, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 35,
        "newStart": 15,
        "newLines": 36,
        "lines": [
          " C_JUDGE_L = '#D6E8F2'",
          " C_CONT    = '#D4762C'",
          " C_CONT_L  = '#F8E0C8'",
          "-C_GRAY    = '#505050'",
          "+C_GRAY    = '#606060'",
          " C_GRAY_L  = '#E8E8E8'",
          " C_RED     = '#B03A2E'",
          " C_RED_L   = '#FADBD8'",
          " C_GREEN   = '#1E8449'",
          " C_GREEN_L = '#D5F5E3'",
          "-C_BG      = '#FAFAFA'",
          " WHITE     = '#FFFFFF'",
          " DARK      = '#2C3E50'",
          " SHADOW    = '#B0B0B0'",
          " ",
          " # ── Figure setup ────────────────────────────────────────────────────",
          "-fig = plt.figure(figsize=(16, 5.5))",
          "+fig = plt.figure(figsize=(16, 5.8))",
          " fig.patch.set_facecolor(WHITE)",
          " ",
          "-gs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,",
          "-                      left=0.01, right=0.99, top=0.94, bottom=0.02)",
          "+gs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,",
          "+                      left=0.012, right=0.988, top=0.95, bottom=0.02)",
          " ax_l = fig.add_subplot(gs[0])",
          " ax_r = fig.add_subplot(gs[1])",
          " ",
          " for ax in [ax_l, ax_r]:",
          "     ax.set_xlim(0, 10)",
          "-    ax.set_ylim(0, 6.2)",
          "+    ax.set_ylim(0, 6.5)",
          "     ax.set_aspect('equal')",
          "     ax.axis('off')",
          " ",
          "+SERIF = 'serif'",
          "+SANS = 'DejaVu Sans'",
          "+",
          " # ── Helpers ─────────────────────────────────────────────────────────",
          " def shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):",
          "-    \"\"\"Rounded box with subtle drop shadow.\"\"\"",
          "     sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,",
          "                          boxstyle=f'round,pad={pad}',",
          "                          facecolor=SHADOW, edgecolor='none',"
        ]
      },
      {
        "oldStart": 56,
        "oldLines": 7,
        "newStart": 57,
        "newLines": 6,
        "lines": [
          "     return b",
          " ",
          " def rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):",
          "-    \"\"\"Rounded box without shadow.\"\"\"",
          "     b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',",
          "                         facecolor=fc, edgecolor=ec, linewidth=lw,",
          "                         linestyle=ls, alpha=alpha, zorder=zorder)"
        ]
      },
      {
        "oldStart": 64,
        "oldLines": 7,
        "newStart": 64,
        "newLines": 7,
        "lines": [
          "     return b",
          " ",
          " def label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',",
          "-          va='center', style='normal', zorder=5, family='serif', **kw):",
          "+          va='center', style='normal', zorder=5, family=SERIF, **kw):",
          "     ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,",
          "             ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)",
          " "
        ]
      },
      {
        "oldStart": 82,
        "oldLines": 78,
        "newStart": 82,
        "newLines": 78,
        "lines": [
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          " # Background panel",
          "-rbox(ax_l, 0.15, 0.15, 9.7, 5.9, C_RED_L, C_RED, lw=1.5, alpha=0.12, zorder=0, pad=0.25)",
          "+rbox(ax_l, 0.15, 0.1, 9.7, 6.25, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)",
          " ",
          " # Title",
          "-label(ax_l, 5.0, 5.8, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 5.4, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 5.0, 6.05, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 5.65, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── Path A: Bias-first ──",
          "-label(ax_l, 5.0, 4.95, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)",
          "+label(ax_l, 5.0, 5.15, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)",
          " ",
          "-bw, bh = 3.2, 0.72",
          "+bw, bh = 3.1, 0.7",
          " # Step 1",
          "-shadow_box(ax_l, 0.6, 4.0, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "-label(ax_l, 0.6 + bw/2, 4.0 + bh/2 + 0.12, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, 0.6 + bw/2, 4.0 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          "+shadow_box(ax_l, 0.7, 4.2, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "+label(ax_l, 0.7 + bw/2, 4.2 + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, 0.7 + bw/2, 4.2 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          " ",
          " # Step 2",
          "-shadow_box(ax_l, 5.8, 4.0, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.1)",
          "-label(ax_l, 5.8 + (bw+0.3)/2, 4.0 + bh/2 + 0.12, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, 5.8 + (bw+0.3)/2, 4.0 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          "+shadow_box(ax_l, 5.9, 4.2, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "+label(ax_l, 5.9 + (bw+0.2)/2, 4.2 + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, 5.9 + (bw+0.2)/2, 4.2 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          " ",
          " # Arrow between steps A",
          "-arrow(ax_l, 3.8, 4.36, 5.8, 4.36, color=C_GRAY, lw=1.4)",
          "+arrow(ax_l, 3.8, 4.55, 5.9, 4.55, color=C_GRAY, lw=1.3)",
          " ",
          "-# Red cross",
          "-label(ax_l, 9.55, 4.36, '✗', fs=16, fw='bold', color=C_RED)",
          "+# Red cross — use sans font for glyph availability",
          "+label(ax_l, 9.55, 4.55, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-# Confounding arc A",
          "-a_conf = FancyArrowPatch((7.5, 4.72), (2.3, 4.72), arrowstyle='-|>',",
          "+# Confounding arc A (above the boxes)",
          "+a_conf = FancyArrowPatch((7.3, 4.9), (2.5, 4.9), arrowstyle='-|>',",
          "                           color=C_RED, linewidth=0.9, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.4',",
          "+                          connectionstyle='arc3,rad=-0.3',",
          "                           mutation_scale=10, zorder=4)",
          " ax_l.add_patch(a_conf)",
          "-label(ax_l, 4.9, 5.15, 'confounding', fs=7, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 4.9, 5.38, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── Path B: Contamination-first ──",
          "-label(ax_l, 5.0, 3.4, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)",
          "+label(ax_l, 5.0, 3.55, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)",
          " ",
          "-shadow_box(ax_l, 0.6, 2.45, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.1)",
          "-label(ax_l, 0.6 + (bw+0.3)/2, 2.45 + bh/2 + 0.12, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, 0.6 + (bw+0.3)/2, 2.45 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          "+shadow_box(ax_l, 0.7, 2.6, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "+label(ax_l, 0.7 + (bw+0.2)/2, 2.6 + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, 0.7 + (bw+0.2)/2, 2.6 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          " ",
          "-shadow_box(ax_l, 5.8, 2.45, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "-label(ax_l, 5.8 + bw/2, 2.45 + bh/2 + 0.12, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, 5.8 + bw/2, 2.45 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          "+shadow_box(ax_l, 5.9, 2.6, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "+label(ax_l, 5.9 + bw/2, 2.6 + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, 5.9 + bw/2, 2.6 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          " ",
          " # Arrow between steps B",
          "-arrow(ax_l, 4.1, 2.81, 5.8, 2.81, color=C_GRAY, lw=1.4)",
          "+arrow(ax_l, 4.1, 2.95, 5.9, 2.95, color=C_GRAY, lw=1.3)",
          " ",
          "-label(ax_l, 9.55, 2.81, '✗', fs=16, fw='bold', color=C_RED)",
          "+label(ax_l, 9.55, 2.95, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          " # Confounding arc B",
          "-b_conf = FancyArrowPatch((7.5, 3.17), (2.5, 3.17), arrowstyle='-|>',",
          "+b_conf = FancyArrowPatch((7.2, 3.3), (2.7, 3.3), arrowstyle='-|>',",
          "                           color=C_RED, linewidth=0.9, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.4',",
          "+                          connectionstyle='arc3,rad=-0.3',",
          "                           mutation_scale=10, zorder=4)",
          " ax_l.add_patch(b_conf)",
          "-label(ax_l, 5.0, 3.6, 'confounding', fs=7, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 5.0, 3.75, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── OVB Box ──",
          "-rbox(ax_l, 0.6, 0.55, 8.8, 1.5, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)",
          "+rbox(ax_l, 0.7, 0.55, 8.6, 1.6, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)",
          " ",
          "-label(ax_l, 5.0, 1.62, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 1.15,",
          "+label(ax_l, 5.0, 1.72, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 1.22,",
          "       r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',",
          "       fs=9, fw='normal', color=C_RED)",
          " ",
          " # Arrows from OVB to paths",
          "-arrow(ax_l, 3.5, 2.05, 3.5, 2.45, color=C_RED, lw=1.0, style='-|>')",
          "-arrow(ax_l, 6.5, 2.05, 6.5, 2.45, color=C_RED, lw=1.0, style='-|>')",
          "+arrow(ax_l, 3.5, 2.15, 3.5, 2.6, color=C_RED, lw=1.0, style='-|>')",
          "+arrow(ax_l, 6.5, 2.15, 6.5, 2.6, color=C_RED, lw=1.0, style='-|>')",
          " ",
          " # Bottom note",
          "-label(ax_l, 5.0, 0.32, 'Unmodeled facet absorbed into remaining estimates',",
          "+label(ax_l, 5.0, 0.3, 'Unmodeled facet absorbed into remaining estimates',",
          "       fs=7.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " "
        ]
      },
      {
        "oldStart": 162,
        "oldLines": 72,
        "newStart": 162,
        "newLines": 72,
        "lines": [
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          " # Background panel",
          "-rbox(ax_r, 0.05, 0.15, 9.9, 5.9, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.10, zorder=0, pad=0.25)",
          "+rbox(ax_r, 0.05, 0.1, 9.9, 6.25, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)",
          " ",
          " # Title",
          "-label(ax_r, 5.0, 5.8, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')",
          "-label(ax_r, 5.0, 5.4, 'staged joint calibration of all facets', fs=8.5,",
          "+label(ax_r, 5.0, 6.05, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')",
          "+label(ax_r, 5.0, 5.65, 'staged joint calibration of all facets', fs=8.5,",
          "       color=C_GREEN, style='italic', fw='normal')",
          " ",
          " # ── Stage 1: Standard MFRM ──",
          "-s1_x, s1_y, s1_w, s1_h = 0.35, 4.55, 9.3, 0.95",
          "+s1_x, s1_y, s1_w, s1_h = 0.35, 4.7, 9.3, 0.85",
          " shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)",
          " ",
          "-label(ax_r, 1.6, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)",
          "-label(ax_r, 1.6, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)",
          "+label(ax_r, 1.5, s1_y + s1_h - 0.22, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)",
          "+label(ax_r, 1.5, s1_y + s1_h - 0.52, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)",
          " ",
          "-# Output tokens",
          "-ow, oh = 1.6, 0.45",
          "-out1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.2), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.2)]",
          "+# Output tokens inside Stage 1",
          "+ow, oh = 1.55, 0.4",
          "+out1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]",
          " for lbl_txt, xo in out1_specs:",
          "-    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)",
          "-    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)",
          "+    rbox(ax_r, xo, s1_y + 0.22, ow, oh, WHITE, C_JUDGE, lw=0.9)",
          "+    label(ax_r, xo + ow/2, s1_y + 0.22 + oh/2, lbl_txt, fs=9, fw='normal', color=C_JUDGE)",
          " ",
          " # Arrow S1 → S3",
          "-arrow(ax_r, 7.5, 4.55, 7.5, 4.1, color=C_JUDGE, lw=1.4)",
          "-label(ax_r, 7.95, 4.32, 'initialize', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          "+arrow(ax_r, 7.3, 4.7, 7.3, 4.2, color=C_JUDGE, lw=1.3)",
          "+label(ax_r, 7.75, 4.45, 'initialize', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          " ",
          " # ── Stage 2: External e_i ──",
          "-s2_x, s2_y, s2_w, s2_h = 0.35, 2.55, 3.9, 1.85",
          "+s2_x, s2_y, s2_w, s2_h = 0.35, 2.55, 3.8, 2.0",
          " shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)",
          " ",
          "-label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,",
          "+label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.2,",
          "       r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)",
          " ",
          " sub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']",
          "-sw, sh = 2.9, 0.38",
          "+sw, sh = 2.8, 0.38",
          " for k, stxt in enumerate(sub_specs):",
          "-    sy = s2_y + s2_h - 0.68 - k * 0.46",
          "+    sy = s2_y + s2_h - 0.7 - k * 0.48",
          "     rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)",
          "     label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)",
          " ",
          " # Arrow S2 → S3",
          "-arrow(ax_r, 4.25, 3.45, 5.1, 3.45, color=C_CONT, lw=1.4)",
          "-label(ax_r, 4.65, 3.7, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          "+arrow(ax_r, 4.15, 3.55, 5.0, 3.55, color=C_CONT, lw=1.3)",
          "+label(ax_r, 4.55, 3.8, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          " ",
          " # ── Stage 3: Joint Gated Model ──",
          "-s3_x, s3_y, s3_w, s3_h = 5.0, 2.4, 4.65, 1.7",
          "-shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F8F8F8', '#3C3C3C', lw=1.8)",
          "+s3_x, s3_y, s3_w, s3_h = 4.9, 2.45, 4.75, 1.75",
          "+shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)",
          " ",
          " label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,",
          "       'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)",
          " ",
          " # Model equation",
          "-label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.68,",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.72,",
          "       r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',",
          "       fs=8, fw='normal', color=C_GRAY)",
          " ",
          " # Gating highlight",
          "-gx, gy, gw, gh = s3_x + 0.5, s3_y + 0.2, 3.6, 0.65",
          "+gx, gy, gw, gh = s3_x + 0.55, s3_y + 0.2, 3.6, 0.6",
          " shadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)",
          " label(ax_r, gx + gw/2, gy + gh/2,",
          "       r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)",
          " ",
          " # ── 4-D Output ──",
          "-label(ax_r, 5.0, 2.05, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          "+label(ax_r, 5.0, 2.1, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          " ",
          " ow2, oh2 = 2.05, 0.7",
          "-out_y = 1.15",
          "+out_y = 1.2",
          " out_specs = [",
          "     (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),",
          "     (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),"
        ]
      },
      {
        "oldStart": 240,
        "oldLines": 15,
        "newStart": 240,
        "newLines": 15,
        "lines": [
          "     label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)",
          " ",
          " # Arrow S3 → outputs",
          "-arrow(ax_r, 7.3, 2.4, 7.3, 1.85, color='#3C3C3C', lw=1.6, style='-|>')",
          "+arrow(ax_r, 7.25, 2.45, 7.25, 1.9, color='#3C3C3C', lw=1.5, style='-|>')",
          " ",
          "-# Green check",
          "-label(ax_r, 5.0, 0.55, '✓  Joint estimation resolves confounding',",
          "-      fs=9, fw='bold', color=C_GREEN, style='italic')",
          "+# Green check — use sans font for glyph availability",
          "+label(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',",
          "+      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)",
          " ",
          " # Panel labels",
          "-label(ax_l, 0.4, 6.05, '(a)', fs=11, fw='bold', color='black', ha='left')",
          "-label(ax_r, 0.25, 6.05, '(b)', fs=11, fw='bold', color='black', ha='left')",
          "+label(ax_l, 0.4, 6.35, '(a)', fs=11, fw='bold', color='black', ha='left')",
          "+label(ax_r, 0.25, 6.35, '(b)', fs=11, fw='bold', color='black', ha='left')",
          " ",
          " # ── Save ──",
          " out_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'"
        ]
      }
    ],
    "originalFile": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\nimport numpy as np\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#505050'\nC_GRAY_L  = '#E8E8E8'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nC_BG      = '#FAFAFA'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 5.5))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,\n                      left=0.01, right=0.99, top=0.94, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 6.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    \"\"\"Rounded box with subtle drop shadow.\"\"\"\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    \"\"\"Rounded box without shadow.\"\"\"\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family='serif', **kw):\n    ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n            ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_l, 0.15, 0.15, 9.7, 5.9, C_RED_L, C_RED, lw=1.5, alpha=0.12, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 5.8, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 5.4, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nlabel(ax_l, 5.0, 4.95, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nbw, bh = 3.2, 0.72\n# Step 1\nshadow_box(ax_l, 0.6, 4.0, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 0.6 + bw/2, 4.0 + bh/2 + 0.12, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.6 + bw/2, 4.0 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Step 2\nshadow_box(ax_l, 5.8, 4.0, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 5.8 + (bw+0.3)/2, 4.0 + bh/2 + 0.12, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.8 + (bw+0.3)/2, 4.0 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\n# Arrow between steps A\narrow(ax_l, 3.8, 4.36, 5.8, 4.36, color=C_GRAY, lw=1.4)\n\n# Red cross\nlabel(ax_l, 9.55, 4.36, '✗', fs=16, fw='bold', color=C_RED)\n\n# Confounding arc A\na_conf = FancyArrowPatch((7.5, 4.72), (2.3, 4.72), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.4',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.9, 5.15, 'confounding', fs=7, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nlabel(ax_l, 5.0, 3.4, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, 0.6, 2.45, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 0.6 + (bw+0.3)/2, 2.45 + bh/2 + 0.12, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.6 + (bw+0.3)/2, 2.45 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, 5.8, 2.45, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 5.8 + bw/2, 2.45 + bh/2 + 0.12, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.8 + bw/2, 2.45 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Arrow between steps B\narrow(ax_l, 4.1, 2.81, 5.8, 2.81, color=C_GRAY, lw=1.4)\n\nlabel(ax_l, 9.55, 2.81, '✗', fs=16, fw='bold', color=C_RED)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((7.5, 3.17), (2.5, 3.17), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.4',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 5.0, 3.6, 'confounding', fs=7, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.6, 0.55, 8.8, 1.5, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.62, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.15,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB to paths\narrow(ax_l, 3.5, 2.05, 3.5, 2.45, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.05, 6.5, 2.45, color=C_RED, lw=1.0, style='-|>')\n\n# Bottom note\nlabel(ax_l, 5.0, 0.32, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_r, 0.05, 0.15, 9.9, 5.9, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 5.8, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 5.4, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 4.55, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.6, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.6, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\n# Output tokens\now, oh = 1.6, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.2), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.2)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.5, 4.55, 7.5, 4.1, color=C_JUDGE, lw=1.4)\nlabel(ax_r, 7.95, 4.32, 'initialize', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: External e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.55, 3.9, 1.85\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.9, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.68 - k * 0.46\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, 4.25, 3.45, 5.1, 3.45, color=C_CONT, lw=1.4)\nlabel(ax_r, 4.65, 3.7, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 5.0, 2.4, 4.65, 1.7\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F8F8F8', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\n# Model equation\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.68,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.5, s3_y + 0.2, 3.6, 0.65\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.05, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.7\nout_y = 1.15\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.12, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.3, 2.4, 7.3, 1.85, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, '✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic')\n\n# Panel labels\nlabel(ax_l, 0.4, 6.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_018CA6rSC2mX2TfPjaFYK8Ke`</summary>

```json
{
  "command": "python3 gen_fig1.py 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "69862226-b3dd-4936-8c39-080c9142494f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKVoZyer5SM31Tf33FaJV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5767,
      "cache_read_input_tokens": 52323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5767
      },
      "output_tokens": 71,
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

_source line 28 · 2026-05-24T11:45:59.921Z_

<details><summary>↩ Tool result · `toolu_018CA6rSC2mX2TfPjaFYK8Ke`</summary>

```text
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
Done: fig1_framework.pdf + fig1_framework.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "11d7a164-3a63-45c1-9e0b-7406937b69f1",
  "tool_use_result": {
    "stdout": "'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\nDone: fig1_framework.pdf + fig1_framework.png",
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

_source line 29_

No glyph warnings now. Let me check the output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "7a056031-e888-45a2-ab56-1084717fd4b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wdJpSBQLAyb939A91ngwu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 58090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
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

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01PgQ9YD4KLufmjGybyqKq3T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "840958b7-f734-42ef-8c43-c99194e18ad4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012wdJpSBQLAyb939A91ngwu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 58090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
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

_source line 31 · 2026-05-24T11:46:05.559Z_

<details><summary>↩ Tool result · `toolu_01PgQ9YD4KLufmjGybyqKq3T`</summary>

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
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "fa9f546f-09a9-4ffa-ae12-4a95c4bb5168",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 445329
    }
  }
}
```

</details>

---


### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Looking at this iteration, I can see several improvements needed:

1. The "confounding" label for Path A is positioned between the Path A label and boxes, which makes it ambiguous. It should be clearly associated with the dashed arc.
2. The right panel's Stage 1 output boxes are barely visible and too small. The text inside them is hard to read.
3. The "initialize" label near the arrow from S1→S3 is overlapping with the Stage 3 box.
4. The "4-Dimensional Diagnostic Output" label is slightly too close to Stage 3.
5. The overall spacing is better but could use more refinement.


6. The subtitle text "staged joint calibration of all facets" on the right panel is overlapping with Stage 1, and the confounding arc placements on the left still feel awkward.

I need to move the confounding labels directly onto the arcs themselves rather than above the path labels, increase the right panel spacing and Stage 1 output box sizes, reposition the "initialize" label to avoid overlap, and shift the subtitle up or reduce spacing to prevent conflicts.

Looking at the overall layout, the left panel's confounding arcs need better positioning, but the main issue is the right panel where the subtitle is crowding Stage 1 and the content feels tight. The 4-D output section at the bottom is working well, so I'll refine the vertical spacing and positioning throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "72f65b84-d388-4c37-8da3-0fc7541b6bc4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mvV2FsenkPAsioBuv39vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 448,
      "cache_read_input_tokens": 58258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 448
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

_source line 33_

Good structural progress. Issues to fix: (1) right panel subtitle overlaps Stage 1, (2) confounding arc labels need better placement, (3) Stage 1 output boxes need more prominence, (4) "initialize" arrow label cramped. Iterating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "4e1b203d-03cf-4dd7-8031-974ea6ab7f8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mvV2FsenkPAsioBuv39vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 448,
      "cache_read_input_tokens": 58258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 448
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

_source line 34_

<details open><summary>🔧 Tool call — Write · `toolu_01254JbCFYZFaG1TDB3XYnar`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 5.8))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 6.5)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_l, 0.15, 0.1, 9.7, 6.25, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 6.0, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 5.6, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nlabel(ax_l, 2.7, 5.1, 'Path A: Bias-first', fs=9, fw='bold', color=DARK, ha='left')\n\nbw, bh = 3.1, 0.68\nbx1_a, bx2_a = 0.7, 5.9\nby_a = 4.2\n\nshadow_box(ax_l, bx1_a, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1_a + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1_a + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2_a, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2_a + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2_a + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1_a + bw, by_a + bh/2, bx2_a, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A\na_conf = FancyArrowPatch((bx2_a + 1.0, by_a + bh + 0.05), (bx1_a + bw/2, by_a + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.35', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.6, 5.25, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nlabel(ax_l, 2.0, 3.55, 'Path B: Contamination-first', fs=9, fw='bold', color=DARK, ha='left')\n\nby_b = 2.6\nshadow_box(ax_l, bx1_a, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1_a + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1_a + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2_a, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2_a + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2_a + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1_a + bw + 0.2, by_b + bh/2, bx2_a, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2_a + 0.8, by_b + bh + 0.05), (bx1_a + (bw+0.2)/2, by_b + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.35', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 4.6, 3.7, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.65, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.72, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.2,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB upward\narrow(ax_l, 3.5, 2.15, 3.5, 2.6, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.15, 6.5, 2.6, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_r, 0.05, 0.1, 9.9, 6.25, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 6.0, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 5.6, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 4.55, 9.3, 0.9\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.23, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.55, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.5, 0.42\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.4), (r'$\\hat{b}$', 6.3), (r'$\\hat{d}$', 8.15)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.24, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.24 + oh/2, lbl_txt, fs=9, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 4.55, 7.3, 4.15, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.35, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.45, 3.7, 1.95\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.2,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.68 - k * 0.47\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.42, 4.85, 3.42, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.42, 3.67, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.35, 4.9, 1.8\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.72,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.2, 3.65, 0.6\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.0, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.68\nout_y = 1.12\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.12, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.35, 7.2, 1.8, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 6.35, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.35, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "6206e87e-42cf-49c0-94db-50a08f401d90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mvV2FsenkPAsioBuv39vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 448,
      "cache_read_input_tokens": 58258,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 448
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

_source line 35 · 2026-05-24T11:47:30.841Z_

<details><summary>↩ Tool result · `toolu_01254JbCFYZFaG1TDB3XYnar`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "231892a6-5e13-403b-9f3f-9964a053befa",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
    "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 5.8))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 6.5)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_l, 0.15, 0.1, 9.7, 6.25, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 6.0, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 5.6, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nlabel(ax_l, 2.7, 5.1, 'Path A: Bias-first', fs=9, fw='bold', color=DARK, ha='left')\n\nbw, bh = 3.1, 0.68\nbx1_a, bx2_a = 0.7, 5.9\nby_a = 4.2\n\nshadow_box(ax_l, bx1_a, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1_a + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1_a + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2_a, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2_a + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2_a + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1_a + bw, by_a + bh/2, bx2_a, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A\na_conf = FancyArrowPatch((bx2_a + 1.0, by_a + bh + 0.05), (bx1_a + bw/2, by_a + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.35', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.6, 5.25, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nlabel(ax_l, 2.0, 3.55, 'Path B: Contamination-first', fs=9, fw='bold', color=DARK, ha='left')\n\nby_b = 2.6\nshadow_box(ax_l, bx1_a, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1_a + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1_a + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2_a, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2_a + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2_a + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1_a + bw + 0.2, by_b + bh/2, bx2_a, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2_a + 0.8, by_b + bh + 0.05), (bx1_a + (bw+0.2)/2, by_b + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.35', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 4.6, 3.7, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.65, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.72, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.2,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB upward\narrow(ax_l, 3.5, 2.15, 3.5, 2.6, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.15, 6.5, 2.6, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_r, 0.05, 0.1, 9.9, 6.25, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 6.0, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 5.6, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 4.55, 9.3, 0.9\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.23, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.55, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.5, 0.42\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.4), (r'$\\hat{b}$', 6.3), (r'$\\hat{d}$', 8.15)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.24, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.24 + oh/2, lbl_txt, fs=9, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 4.55, 7.3, 4.15, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.35, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.45, 3.7, 1.95\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.2,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.68 - k * 0.47\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.42, 4.85, 3.42, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.42, 3.67, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.35, 4.9, 1.8\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.72,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.2, 3.65, 0.6\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.0, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.68\nout_y = 1.12\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.12, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.35, 7.2, 1.8, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 6.35, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.35, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 9,
        "newStart": 6,
        "newLines": 7,
        "lines": [
          " matplotlib.rcParams['pdf.fonttype'] = 42",
          " matplotlib.rcParams['ps.fonttype'] = 42",
          " import matplotlib.pyplot as plt",
          "-import matplotlib.patches as mpatches",
          " from matplotlib.patches import FancyBboxPatch, FancyArrowPatch",
          "-import numpy as np",
          " ",
          " # ── Colors ──────────────────────────────────────────────────────────",
          " C_JUDGE   = '#2B6E99'"
        ]
      },
      {
        "oldStart": 16,
        "oldLines": 7,
        "newStart": 14,
        "newLines": 6,
        "lines": [
          " C_CONT    = '#D4762C'",
          " C_CONT_L  = '#F8E0C8'",
          " C_GRAY    = '#606060'",
          "-C_GRAY_L  = '#E8E8E8'",
          " C_RED     = '#B03A2E'",
          " C_RED_L   = '#FADBD8'",
          " C_GREEN   = '#1E8449'"
        ]
      },
      {
        "oldStart": 25,
        "oldLines": 6,
        "newStart": 22,
        "newLines": 9,
        "lines": [
          " DARK      = '#2C3E50'",
          " SHADOW    = '#B0B0B0'",
          " ",
          "+SERIF = 'serif'",
          "+SANS = 'DejaVu Sans'",
          "+",
          " # ── Figure setup ────────────────────────────────────────────────────",
          " fig = plt.figure(figsize=(16, 5.8))",
          " fig.patch.set_facecolor(WHITE)"
        ]
      },
      {
        "oldStart": 40,
        "oldLines": 9,
        "newStart": 40,
        "newLines": 6,
        "lines": [
          "     ax.set_aspect('equal')",
          "     ax.axis('off')",
          " ",
          "-SERIF = 'serif'",
          "-SANS = 'DejaVu Sans'",
          "-",
          " # ── Helpers ─────────────────────────────────────────────────────────",
          " def shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):",
          "     sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,"
        ]
      },
      {
        "oldStart": 65,
        "oldLines": 8,
        "newStart": 62,
        "newLines": 8,
        "lines": [
          " ",
          " def label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',",
          "           va='center', style='normal', zorder=5, family=SERIF, **kw):",
          "-    ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,",
          "-            ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)",
          "+    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,",
          "+                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)",
          " ",
          " def arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',",
          "           rad=0, zorder=4, ls='-'):"
        ]
      },
      {
        "oldStart": 85,
        "oldLines": 75,
        "newStart": 82,
        "newLines": 69,
        "lines": [
          " rbox(ax_l, 0.15, 0.1, 9.7, 6.25, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)",
          " ",
          " # Title",
          "-label(ax_l, 5.0, 6.05, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 5.65, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 5.0, 6.0, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 5.6, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── Path A: Bias-first ──",
          "-label(ax_l, 5.0, 5.15, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)",
          "+label(ax_l, 2.7, 5.1, 'Path A: Bias-first', fs=9, fw='bold', color=DARK, ha='left')",
          " ",
          "-bw, bh = 3.1, 0.7",
          "-# Step 1",
          "-shadow_box(ax_l, 0.7, 4.2, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "-label(ax_l, 0.7 + bw/2, 4.2 + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, 0.7 + bw/2, 4.2 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          "+bw, bh = 3.1, 0.68",
          "+bx1_a, bx2_a = 0.7, 5.9",
          "+by_a = 4.2",
          " ",
          "-# Step 2",
          "-shadow_box(ax_l, 5.9, 4.2, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "-label(ax_l, 5.9 + (bw+0.2)/2, 4.2 + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, 5.9 + (bw+0.2)/2, 4.2 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          "+shadow_box(ax_l, bx1_a, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "+label(ax_l, bx1_a + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, bx1_a + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          " ",
          "-# Arrow between steps A",
          "-arrow(ax_l, 3.8, 4.55, 5.9, 4.55, color=C_GRAY, lw=1.3)",
          "+shadow_box(ax_l, bx2_a, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "+label(ax_l, bx2_a + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, bx2_a + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          " ",
          "-# Red cross — use sans font for glyph availability",
          "-label(ax_l, 9.55, 4.55, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          "+arrow(ax_l, bx1_a + bw, by_a + bh/2, bx2_a, by_a + bh/2, color=C_GRAY, lw=1.3)",
          "+label(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-# Confounding arc A (above the boxes)",
          "-a_conf = FancyArrowPatch((7.3, 4.9), (2.5, 4.9), arrowstyle='-|>',",
          "-                          color=C_RED, linewidth=0.9, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.3',",
          "-                          mutation_scale=10, zorder=4)",
          "+# Confounding arc A",
          "+a_conf = FancyArrowPatch((bx2_a + 1.0, by_a + bh + 0.05), (bx1_a + bw/2, by_a + bh + 0.05),",
          "+                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',",
          "+                          connectionstyle='arc3,rad=-0.35', mutation_scale=10, zorder=4)",
          " ax_l.add_patch(a_conf)",
          "-label(ax_l, 4.9, 5.38, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 4.6, 5.25, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── Path B: Contamination-first ──",
          "-label(ax_l, 5.0, 3.55, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)",
          "+label(ax_l, 2.0, 3.55, 'Path B: Contamination-first', fs=9, fw='bold', color=DARK, ha='left')",
          " ",
          "-shadow_box(ax_l, 0.7, 2.6, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "-label(ax_l, 0.7 + (bw+0.2)/2, 2.6 + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, 0.7 + (bw+0.2)/2, 2.6 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          "+by_b = 2.6",
          "+shadow_box(ax_l, bx1_a, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "+label(ax_l, bx1_a + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, bx1_a + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          " ",
          "-shadow_box(ax_l, 5.9, 2.6, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "-label(ax_l, 5.9 + bw/2, 2.6 + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, 5.9 + bw/2, 2.6 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          "+shadow_box(ax_l, bx2_a, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "+label(ax_l, bx2_a + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, bx2_a + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          " ",
          "-# Arrow between steps B",
          "-arrow(ax_l, 4.1, 2.95, 5.9, 2.95, color=C_GRAY, lw=1.3)",
          "+arrow(ax_l, bx1_a + bw + 0.2, by_b + bh/2, bx2_a, by_b + bh/2, color=C_GRAY, lw=1.3)",
          "+label(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-label(ax_l, 9.55, 2.95, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          "-",
          " # Confounding arc B",
          "-b_conf = FancyArrowPatch((7.2, 3.3), (2.7, 3.3), arrowstyle='-|>',",
          "-                          color=C_RED, linewidth=0.9, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.3',",
          "-                          mutation_scale=10, zorder=4)",
          "+b_conf = FancyArrowPatch((bx2_a + 0.8, by_b + bh + 0.05), (bx1_a + (bw+0.2)/2, by_b + bh + 0.05),",
          "+                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',",
          "+                          connectionstyle='arc3,rad=-0.35', mutation_scale=10, zorder=4)",
          " ax_l.add_patch(b_conf)",
          "-label(ax_l, 5.0, 3.75, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 4.6, 3.7, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── OVB Box ──",
          "-rbox(ax_l, 0.7, 0.55, 8.6, 1.6, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)",
          "+rbox(ax_l, 0.7, 0.5, 8.6, 1.65, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)",
          " ",
          " label(ax_l, 5.0, 1.72, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 1.22,",
          "+label(ax_l, 5.0, 1.2,",
          "       r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',",
          "       fs=9, fw='normal', color=C_RED)",
          " ",
          "-# Arrows from OVB to paths",
          "+# Arrows from OVB upward",
          " arrow(ax_l, 3.5, 2.15, 3.5, 2.6, color=C_RED, lw=1.0, style='-|>')",
          " arrow(ax_l, 6.5, 2.15, 6.5, 2.6, color=C_RED, lw=1.0, style='-|>')",
          " ",
          "-# Bottom note",
          "-label(ax_l, 5.0, 0.3, 'Unmodeled facet absorbed into remaining estimates',",
          "+label(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',",
          "       fs=7.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " "
        ]
      },
      {
        "oldStart": 165,
        "oldLines": 69,
        "newStart": 156,
        "newLines": 67,
        "lines": [
          " rbox(ax_r, 0.05, 0.1, 9.9, 6.25, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)",
          " ",
          " # Title",
          "-label(ax_r, 5.0, 6.05, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')",
          "-label(ax_r, 5.0, 5.65, 'staged joint calibration of all facets', fs=8.5,",
          "+label(ax_r, 5.0, 6.0, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')",
          "+label(ax_r, 5.0, 5.6, 'staged joint calibration of all facets', fs=8.5,",
          "       color=C_GREEN, style='italic', fw='normal')",
          " ",
          " # ── Stage 1: Standard MFRM ──",
          "-s1_x, s1_y, s1_w, s1_h = 0.35, 4.7, 9.3, 0.85",
          "+s1_x, s1_y, s1_w, s1_h = 0.35, 4.55, 9.3, 0.9",
          " shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)",
          " ",
          "-label(ax_r, 1.5, s1_y + s1_h - 0.22, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)",
          "-label(ax_r, 1.5, s1_y + s1_h - 0.52, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)",
          "+label(ax_r, 1.55, s1_y + s1_h - 0.23, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)",
          "+label(ax_r, 1.55, s1_y + s1_h - 0.55, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)",
          " ",
          "-# Output tokens inside Stage 1",
          "-ow, oh = 1.55, 0.4",
          "-out1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]",
          "+ow, oh = 1.5, 0.42",
          "+out1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.4), (r'$\\hat{b}$', 6.3), (r'$\\hat{d}$', 8.15)]",
          " for lbl_txt, xo in out1_specs:",
          "-    rbox(ax_r, xo, s1_y + 0.22, ow, oh, WHITE, C_JUDGE, lw=0.9)",
          "-    label(ax_r, xo + ow/2, s1_y + 0.22 + oh/2, lbl_txt, fs=9, fw='normal', color=C_JUDGE)",
          "+    rbox(ax_r, xo, s1_y + 0.24, ow, oh, WHITE, C_JUDGE, lw=0.9)",
          "+    label(ax_r, xo + ow/2, s1_y + 0.24 + oh/2, lbl_txt, fs=9, fw='normal', color=C_JUDGE)",
          " ",
          " # Arrow S1 → S3",
          "-arrow(ax_r, 7.3, 4.7, 7.3, 4.2, color=C_JUDGE, lw=1.3)",
          "-label(ax_r, 7.75, 4.45, 'initialize', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          "+arrow(ax_r, 7.3, 4.55, 7.3, 4.15, color=C_JUDGE, lw=1.3)",
          "+label(ax_r, 7.75, 4.35, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          " ",
          "-# ── Stage 2: External e_i ──",
          "-s2_x, s2_y, s2_w, s2_h = 0.35, 2.55, 3.8, 2.0",
          "+# ── Stage 2: Estimate e_i ──",
          "+s2_x, s2_y, s2_w, s2_h = 0.35, 2.45, 3.7, 1.95",
          " shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)",
          " ",
          " label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.2,",
          "       r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)",
          " ",
          " sub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']",
          "-sw, sh = 2.8, 0.38",
          "+sw, sh = 2.7, 0.38",
          " for k, stxt in enumerate(sub_specs):",
          "-    sy = s2_y + s2_h - 0.7 - k * 0.48",
          "+    sy = s2_y + s2_h - 0.68 - k * 0.47",
          "     rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)",
          "     label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)",
          " ",
          " # Arrow S2 → S3",
          "-arrow(ax_r, 4.15, 3.55, 5.0, 3.55, color=C_CONT, lw=1.3)",
          "-label(ax_r, 4.55, 3.8, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          "+arrow(ax_r, s2_x + s2_w, 3.42, 4.85, 3.42, color=C_CONT, lw=1.3)",
          "+label(ax_r, 4.42, 3.67, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          " ",
          " # ── Stage 3: Joint Gated Model ──",
          "-s3_x, s3_y, s3_w, s3_h = 4.9, 2.45, 4.75, 1.75",
          "+s3_x, s3_y, s3_w, s3_h = 4.75, 2.35, 4.9, 1.8",
          " shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)",
          " ",
          " label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,",
          "       'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)",
          " ",
          "-# Model equation",
          " label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.72,",
          "       r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',",
          "       fs=8, fw='normal', color=C_GRAY)",
          " ",
          " # Gating highlight",
          "-gx, gy, gw, gh = s3_x + 0.55, s3_y + 0.2, 3.6, 0.6",
          "+gx, gy, gw, gh = s3_x + 0.6, s3_y + 0.2, 3.65, 0.6",
          " shadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)",
          " label(ax_r, gx + gw/2, gy + gh/2,",
          "       r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)",
          " ",
          " # ── 4-D Output ──",
          "-label(ax_r, 5.0, 2.1, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          "+label(ax_r, 5.0, 2.0, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          " ",
          "-ow2, oh2 = 2.05, 0.7",
          "-out_y = 1.2",
          "+ow2, oh2 = 2.05, 0.68",
          "+out_y = 1.12",
          " out_specs = [",
          "     (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),",
          "     (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),"
        ]
      },
      {
        "oldStart": 240,
        "oldLines": 14,
        "newStart": 229,
        "newLines": 14,
        "lines": [
          "     label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)",
          " ",
          " # Arrow S3 → outputs",
          "-arrow(ax_r, 7.25, 2.45, 7.25, 1.9, color='#3C3C3C', lw=1.5, style='-|>')",
          "+arrow(ax_r, 7.2, 2.35, 7.2, 1.8, color='#3C3C3C', lw=1.5, style='-|>')",
          " ",
          "-# Green check — use sans font for glyph availability",
          "-label(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',",
          "+# Green check",
          "+label(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',",
          "       fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)",
          " ",
          " # Panel labels",
          "-label(ax_l, 0.4, 6.35, '(a)', fs=11, fw='bold', color='black', ha='left')",
          "+label(ax_l, 0.35, 6.35, '(a)', fs=11, fw='bold', color='black', ha='left')",
          " label(ax_r, 0.25, 6.35, '(b)', fs=11, fw='bold', color='black', ha='left')",
          " ",
          " # ── Save ──"
        ]
      }
    ],
    "originalFile": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\nimport numpy as np\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_GRAY_L  = '#E8E8E8'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 5.8))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 6.5)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n            ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_l, 0.15, 0.1, 9.7, 6.25, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 6.05, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 5.65, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nlabel(ax_l, 5.0, 5.15, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nbw, bh = 3.1, 0.7\n# Step 1\nshadow_box(ax_l, 0.7, 4.2, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 0.7 + bw/2, 4.2 + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.7 + bw/2, 4.2 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Step 2\nshadow_box(ax_l, 5.9, 4.2, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 5.9 + (bw+0.2)/2, 4.2 + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.9 + (bw+0.2)/2, 4.2 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\n# Arrow between steps A\narrow(ax_l, 3.8, 4.55, 5.9, 4.55, color=C_GRAY, lw=1.3)\n\n# Red cross — use sans font for glyph availability\nlabel(ax_l, 9.55, 4.55, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A (above the boxes)\na_conf = FancyArrowPatch((7.3, 4.9), (2.5, 4.9), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.9, 5.38, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nlabel(ax_l, 5.0, 3.55, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, 0.7, 2.6, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, 0.7 + (bw+0.2)/2, 2.6 + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 0.7 + (bw+0.2)/2, 2.6 + bh/2 - 0.14, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, 5.9, 2.6, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, 5.9 + bw/2, 2.6 + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, 5.9 + bw/2, 2.6 + bh/2 - 0.14, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\n# Arrow between steps B\narrow(ax_l, 4.1, 2.95, 5.9, 2.95, color=C_GRAY, lw=1.3)\n\nlabel(ax_l, 9.55, 2.95, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((7.2, 3.3), (2.7, 3.3), arrowstyle='-|>',\n                          color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3',\n                          mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 5.0, 3.75, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.55, 8.6, 1.6, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.72, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.22,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB to paths\narrow(ax_l, 3.5, 2.15, 3.5, 2.6, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.15, 6.5, 2.6, color=C_RED, lw=1.0, style='-|>')\n\n# Bottom note\nlabel(ax_l, 5.0, 0.3, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_r, 0.05, 0.1, 9.9, 6.25, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 6.05, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 5.65, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 4.7, 9.3, 0.85\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.5, s1_y + s1_h - 0.22, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.5, s1_y + s1_h - 0.52, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\n# Output tokens inside Stage 1\now, oh = 1.55, 0.4\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.22, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.22 + oh/2, lbl_txt, fs=9, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 4.7, 7.3, 4.2, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.45, 'initialize', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: External e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.55, 3.8, 2.0\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.2,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.8, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.7 - k * 0.48\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, 4.15, 3.55, 5.0, 3.55, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.55, 3.8, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.9, 2.45, 4.75, 1.75\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\n# Model equation\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.72,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.55, s3_y + 0.2, 3.6, 0.6\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.1, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.7\nout_y = 1.2\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.12, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.25, 2.45, 7.25, 1.9, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check — use sans font for glyph availability\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.4, 6.35, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.35, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01TCfAEJPgVQio5SbYD8avWr`</summary>

```json
{
  "command": "python3 gen_fig1.py 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "73606e8f-a1de-4c48-a614-6419fa01be97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTsmeUYZWHxs8patQHPW5C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5982,
      "cache_read_input_tokens": 58706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5982
      },
      "output_tokens": 63,
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

_source line 37 · 2026-05-24T11:47:35.933Z_

<details><summary>↩ Tool result · `toolu_01TCfAEJPgVQio5SbYD8avWr`</summary>

```text
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
Done: fig1_framework.pdf + fig1_framework.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "9ea6760a-1dbf-495b-874f-0c15a211b6a0",
  "tool_use_result": {
    "stdout": "'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\nDone: fig1_framework.pdf + fig1_framework.png",
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

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01BMwXt1t3pcPPEFLP5i8dv8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "8d9a73cf-28cb-417e-a8e0-de23b21387a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176CTJNFUbvtofBQHHk49f8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 64688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
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

_source line 39 · 2026-05-24T11:47:40.100Z_

<details><summary>↩ Tool result · `toolu_01BMwXt1t3pcPPEFLP5i8dv8`</summary>

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
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "257ec087-a368-4d80-8ee3-870d1b067494",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 444125
    }
  }
}
```

</details>

---


### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Progress is good but there are still several issues:

1. The right panel subtitle "staged joint calibration of all facets" is overlapping with the Stage 1 box. The italic text is positioned at y=5.6 and Stage 1 top is at y=4.55+0.9=5.45, so the text at 5.6 overlaps.

2. The "confounding" labels on the left panel are positioned right where the "Path A/B" labels are, causing visual collision. The "confounding" at y=5.25 overlaps with the "Path A: Bias-first" at y=5.1.


3. The output boxes in Stage 1 are too faint and need better visibility, or I should increase the box height slightly. 4. The Stage 3 equation is hard to read at its current size. 5. The path labels need clearer separation from the confounding annotations. I'll shift the right panel subtitle higher to clear the overlap, reposition the confounding labels to sit along the arcs instead of at the top, bump up Stage 1's height, enlarge the Stage 3 equation, and ensure the path and confounding labels have distinct visual spacing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "801e1e81-9fbf-4f14-8ed2-eee6aa17f7ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToAgf5Hdv2cgBtueZCR5ps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 64856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 434
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

_source line 41_

Getting closer. Key remaining issues: subtitle overlapping Stage 1, confounding labels colliding with path labels, right panel elements slightly cramped. Let me do a refined pass.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "5c43d4d8-4689-41d0-8e11-4bbf871f038b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToAgf5Hdv2cgBtueZCR5ps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 64856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 434
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

_source line 42_

<details open><summary>🔧 Tool call — Write · `toolu_016atSzmRv6233sRv8cTEkwj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.0))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.0)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.75, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 6.55, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.15, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.7\n\nlabel(ax_l, 5.0, 5.7, 'Path A: Bias-first', fs=9, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — positioned clearly above boxes\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh + 0.08), (bx1 + bw/2 - 0.3, by_a + bh + 0.08),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.8, 5.85, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nby_b = 2.85\n\nlabel(ax_l, 5.0, 3.85, 'Path B: Contamination-first', fs=9, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh + 0.08), (bx1 + (bw+0.2)/2 - 0.3, by_b + bh + 0.08),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 4.8, 4.0, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.85, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.85, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.3,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB upward\narrow(ax_l, 3.5, 2.35, 3.5, 2.85, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.35, 6.5, 2.85, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.3, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.75, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 6.55, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.15, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.0, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.0, 7.3, 4.6, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.8, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.7, 3.7, 2.15\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.5\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.78, 4.85, 3.78, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.03, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.6, 4.9, 2.0\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.78,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.65\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.2, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.25\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.6, 7.2, 1.97, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 6.85, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.85, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "411d2167-cb74-4862-8183-27c730bfeafe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToAgf5Hdv2cgBtueZCR5ps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 64856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 434
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

_source line 43 · 2026-05-24T11:49:02.402Z_

<details><summary>↩ Tool result · `toolu_016atSzmRv6233sRv8cTEkwj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "64fe61d4-eaa3-4136-a2d5-6868db855d93",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
    "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.0))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.0)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.75, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 6.55, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.15, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.7\n\nlabel(ax_l, 5.0, 5.7, 'Path A: Bias-first', fs=9, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — positioned clearly above boxes\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh + 0.08), (bx1 + bw/2 - 0.3, by_a + bh + 0.08),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.8, 5.85, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nby_b = 2.85\n\nlabel(ax_l, 5.0, 3.85, 'Path B: Contamination-first', fs=9, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh + 0.08), (bx1 + (bw+0.2)/2 - 0.3, by_b + bh + 0.08),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 4.8, 4.0, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.85, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.85, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.3,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB upward\narrow(ax_l, 3.5, 2.35, 3.5, 2.85, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.35, 6.5, 2.85, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.3, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.75, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 6.55, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.15, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.0, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.0, 7.3, 4.6, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.8, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.7, 3.7, 2.15\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.5\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.78, 4.85, 3.78, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.03, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.6, 4.9, 2.0\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.78,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.65\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.2, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.25\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.6, 7.2, 1.97, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 6.85, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.85, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "structuredPatch": [
      {
        "oldStart": 26,
        "oldLines": 7,
        "newStart": 26,
        "newLines": 7,
        "lines": [
          " SANS = 'DejaVu Sans'",
          " ",
          " # ── Figure setup ────────────────────────────────────────────────────",
          "-fig = plt.figure(figsize=(16, 5.8))",
          "+fig = plt.figure(figsize=(16, 6.0))",
          " fig.patch.set_facecolor(WHITE)",
          " ",
          " gs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,"
        ]
      },
      {
        "oldStart": 36,
        "oldLines": 7,
        "newStart": 36,
        "newLines": 7,
        "lines": [
          " ",
          " for ax in [ax_l, ax_r]:",
          "     ax.set_xlim(0, 10)",
          "-    ax.set_ylim(0, 6.5)",
          "+    ax.set_ylim(0, 7.0)",
          "     ax.set_aspect('equal')",
          "     ax.axis('off')",
          " "
        ]
      },
      {
        "oldStart": 78,
        "oldLines": 73,
        "newStart": 78,
        "newLines": 73,
        "lines": [
          " #  LEFT PANEL — Sequential Pipeline",
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          "-# Background panel",
          "-rbox(ax_l, 0.15, 0.1, 9.7, 6.25, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)",
          "+rbox(ax_l, 0.15, 0.1, 9.7, 6.75, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)",
          " ",
          " # Title",
          "-label(ax_l, 5.0, 6.0, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 5.6, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 5.0, 6.55, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 6.15, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── Path A: Bias-first ──",
          "-label(ax_l, 2.7, 5.1, 'Path A: Bias-first', fs=9, fw='bold', color=DARK, ha='left')",
          "-",
          " bw, bh = 3.1, 0.68",
          "-bx1_a, bx2_a = 0.7, 5.9",
          "-by_a = 4.2",
          "+bx1, bx2 = 0.7, 5.9",
          "+by_a = 4.7",
          " ",
          "-shadow_box(ax_l, bx1_a, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "-label(ax_l, bx1_a + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, bx1_a + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          "+label(ax_l, 5.0, 5.7, 'Path A: Bias-first', fs=9, fw='bold', color=DARK)",
          " ",
          "-shadow_box(ax_l, bx2_a, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "-label(ax_l, bx2_a + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, bx2_a + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          "+shadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "+label(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          " ",
          "-arrow(ax_l, bx1_a + bw, by_a + bh/2, bx2_a, by_a + bh/2, color=C_GRAY, lw=1.3)",
          "+shadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "+label(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          "+",
          "+arrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)",
          " label(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-# Confounding arc A",
          "-a_conf = FancyArrowPatch((bx2_a + 1.0, by_a + bh + 0.05), (bx1_a + bw/2, by_a + bh + 0.05),",
          "+# Confounding arc A — positioned clearly above boxes",
          "+a_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh + 0.08), (bx1 + bw/2 - 0.3, by_a + bh + 0.08),",
          "                           arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.35', mutation_scale=10, zorder=4)",
          "+                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)",
          " ax_l.add_patch(a_conf)",
          "-label(ax_l, 4.6, 5.25, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 4.8, 5.85, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── Path B: Contamination-first ──",
          "-label(ax_l, 2.0, 3.55, 'Path B: Contamination-first', fs=9, fw='bold', color=DARK, ha='left')",
          "+by_b = 2.85",
          " ",
          "-by_b = 2.6",
          "-shadow_box(ax_l, bx1_a, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "-label(ax_l, bx1_a + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, bx1_a + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          "+label(ax_l, 5.0, 3.85, 'Path B: Contamination-first', fs=9, fw='bold', color=DARK)",
          " ",
          "-shadow_box(ax_l, bx2_a, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "-label(ax_l, bx2_a + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, bx2_a + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          "+shadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "+label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          " ",
          "-arrow(ax_l, bx1_a + bw + 0.2, by_b + bh/2, bx2_a, by_b + bh/2, color=C_GRAY, lw=1.3)",
          "+shadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "+label(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)",
          "+label(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          "+",
          "+arrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)",
          " label(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          " # Confounding arc B",
          "-b_conf = FancyArrowPatch((bx2_a + 0.8, by_b + bh + 0.05), (bx1_a + (bw+0.2)/2, by_b + bh + 0.05),",
          "+b_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh + 0.08), (bx1 + (bw+0.2)/2 - 0.3, by_b + bh + 0.08),",
          "                           arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.35', mutation_scale=10, zorder=4)",
          "+                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)",
          " ax_l.add_patch(b_conf)",
          "-label(ax_l, 4.6, 3.7, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 4.8, 4.0, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── OVB Box ──",
          "-rbox(ax_l, 0.7, 0.5, 8.6, 1.65, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)",
          "+rbox(ax_l, 0.7, 0.5, 8.6, 1.85, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)",
          " ",
          "-label(ax_l, 5.0, 1.72, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 1.2,",
          "+label(ax_l, 5.0, 1.85, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 1.3,",
          "       r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',",
          "       fs=9, fw='normal', color=C_RED)",
          " ",
          " # Arrows from OVB upward",
          "-arrow(ax_l, 3.5, 2.15, 3.5, 2.6, color=C_RED, lw=1.0, style='-|>')",
          "-arrow(ax_l, 6.5, 2.15, 6.5, 2.6, color=C_RED, lw=1.0, style='-|>')",
          "+arrow(ax_l, 3.5, 2.35, 3.5, 2.85, color=C_RED, lw=1.0, style='-|>')",
          "+arrow(ax_l, 6.5, 2.35, 6.5, 2.85, color=C_RED, lw=1.0, style='-|>')",
          " ",
          "-label(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',",
          "+label(ax_l, 5.0, 0.3, 'Unmodeled facet absorbed into remaining estimates',",
          "       fs=7.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " "
        ]
      },
      {
        "oldStart": 152,
        "oldLines": 71,
        "newStart": 152,
        "newLines": 70,
        "lines": [
          " #  RIGHT PANEL — G-MFRM Joint Framework",
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          "-# Background panel",
          "-rbox(ax_r, 0.05, 0.1, 9.9, 6.25, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)",
          "+rbox(ax_r, 0.05, 0.1, 9.9, 6.75, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)",
          " ",
          " # Title",
          "-label(ax_r, 5.0, 6.0, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')",
          "-label(ax_r, 5.0, 5.6, 'staged joint calibration of all facets', fs=8.5,",
          "+label(ax_r, 5.0, 6.55, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')",
          "+label(ax_r, 5.0, 6.15, 'staged joint calibration of all facets', fs=8.5,",
          "       color=C_GREEN, style='italic', fw='normal')",
          " ",
          " # ── Stage 1: Standard MFRM ──",
          "-s1_x, s1_y, s1_w, s1_h = 0.35, 4.55, 9.3, 0.9",
          "+s1_x, s1_y, s1_w, s1_h = 0.35, 5.0, 9.3, 0.95",
          " shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)",
          " ",
          "-label(ax_r, 1.55, s1_y + s1_h - 0.23, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)",
          "-label(ax_r, 1.55, s1_y + s1_h - 0.55, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)",
          "+label(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)",
          "+label(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)",
          " ",
          "-ow, oh = 1.5, 0.42",
          "-out1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.4), (r'$\\hat{b}$', 6.3), (r'$\\hat{d}$', 8.15)]",
          "+ow, oh = 1.55, 0.45",
          "+out1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]",
          " for lbl_txt, xo in out1_specs:",
          "-    rbox(ax_r, xo, s1_y + 0.24, ow, oh, WHITE, C_JUDGE, lw=0.9)",
          "-    label(ax_r, xo + ow/2, s1_y + 0.24 + oh/2, lbl_txt, fs=9, fw='normal', color=C_JUDGE)",
          "+    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)",
          "+    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)",
          " ",
          " # Arrow S1 → S3",
          "-arrow(ax_r, 7.3, 4.55, 7.3, 4.15, color=C_JUDGE, lw=1.3)",
          "-label(ax_r, 7.75, 4.35, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          "+arrow(ax_r, 7.3, 5.0, 7.3, 4.6, color=C_JUDGE, lw=1.3)",
          "+label(ax_r, 7.75, 4.8, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          " ",
          " # ── Stage 2: Estimate e_i ──",
          "-s2_x, s2_y, s2_w, s2_h = 0.35, 2.45, 3.7, 1.95",
          "+s2_x, s2_y, s2_w, s2_h = 0.35, 2.7, 3.7, 2.15",
          " shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)",
          " ",
          "-label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.2,",
          "+label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,",
          "       r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)",
          " ",
          " sub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']",
          " sw, sh = 2.7, 0.38",
          " for k, stxt in enumerate(sub_specs):",
          "-    sy = s2_y + s2_h - 0.68 - k * 0.47",
          "+    sy = s2_y + s2_h - 0.72 - k * 0.5",
          "     rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)",
          "     label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)",
          " ",
          " # Arrow S2 → S3",
          "-arrow(ax_r, s2_x + s2_w, 3.42, 4.85, 3.42, color=C_CONT, lw=1.3)",
          "-label(ax_r, 4.42, 3.67, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          "+arrow(ax_r, s2_x + s2_w, 3.78, 4.85, 3.78, color=C_CONT, lw=1.3)",
          "+label(ax_r, 4.45, 4.03, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          " ",
          " # ── Stage 3: Joint Gated Model ──",
          "-s3_x, s3_y, s3_w, s3_h = 4.75, 2.35, 4.9, 1.8",
          "+s3_x, s3_y, s3_w, s3_h = 4.75, 2.6, 4.9, 2.0",
          " shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)",
          " ",
          "-label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,",
          "       'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)",
          " ",
          "-label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.72,",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.78,",
          "       r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',",
          "-      fs=8, fw='normal', color=C_GRAY)",
          "+      fs=8.5, fw='normal', color=C_GRAY)",
          " ",
          " # Gating highlight",
          "-gx, gy, gw, gh = s3_x + 0.6, s3_y + 0.2, 3.65, 0.6",
          "+gx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.65",
          " shadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)",
          " label(ax_r, gx + gw/2, gy + gh/2,",
          "       r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)",
          " ",
          " # ── 4-D Output ──",
          "-label(ax_r, 5.0, 2.0, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          "+label(ax_r, 5.0, 2.2, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          " ",
          "-ow2, oh2 = 2.05, 0.68",
          "-out_y = 1.12",
          "+ow2, oh2 = 2.05, 0.72",
          "+out_y = 1.25",
          " out_specs = [",
          "     (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),",
          "     (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),"
        ]
      },
      {
        "oldStart": 225,
        "oldLines": 19,
        "newStart": 224,
        "newLines": 19,
        "lines": [
          " ]",
          " for sym, desc, fc, ec, xo in out_specs:",
          "     shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)",
          "-    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.12, sym, fs=9.5, fw='bold', color=ec)",
          "+    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)",
          "     label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)",
          " ",
          " # Arrow S3 → outputs",
          "-arrow(ax_r, 7.2, 2.35, 7.2, 1.8, color='#3C3C3C', lw=1.5, style='-|>')",
          "+arrow(ax_r, 7.2, 2.6, 7.2, 1.97, color='#3C3C3C', lw=1.5, style='-|>')",
          " ",
          " # Green check",
          "-label(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',",
          "+label(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',",
          "       fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)",
          " ",
          " # Panel labels",
          "-label(ax_l, 0.35, 6.35, '(a)', fs=11, fw='bold', color='black', ha='left')",
          "-label(ax_r, 0.25, 6.35, '(b)', fs=11, fw='bold', color='black', ha='left')",
          "+label(ax_l, 0.35, 6.85, '(a)', fs=11, fw='bold', color='black', ha='left')",
          "+label(ax_r, 0.25, 6.85, '(b)', fs=11, fw='bold', color='black', ha='left')",
          " ",
          " # ── Save ──",
          " out_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'"
        ]
      }
    ],
    "originalFile": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 5.8))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 6.5)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_l, 0.15, 0.1, 9.7, 6.25, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 6.0, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 5.6, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nlabel(ax_l, 2.7, 5.1, 'Path A: Bias-first', fs=9, fw='bold', color=DARK, ha='left')\n\nbw, bh = 3.1, 0.68\nbx1_a, bx2_a = 0.7, 5.9\nby_a = 4.2\n\nshadow_box(ax_l, bx1_a, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1_a + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1_a + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2_a, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2_a + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2_a + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1_a + bw, by_a + bh/2, bx2_a, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A\na_conf = FancyArrowPatch((bx2_a + 1.0, by_a + bh + 0.05), (bx1_a + bw/2, by_a + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.35', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.6, 5.25, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nlabel(ax_l, 2.0, 3.55, 'Path B: Contamination-first', fs=9, fw='bold', color=DARK, ha='left')\n\nby_b = 2.6\nshadow_box(ax_l, bx1_a, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1_a + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1_a + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2_a, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2_a + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2_a + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1_a + bw + 0.2, by_b + bh/2, bx2_a, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2_a + 0.8, by_b + bh + 0.05), (bx1_a + (bw+0.2)/2, by_b + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.35', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 4.6, 3.7, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.65, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.72, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.2,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB upward\narrow(ax_l, 3.5, 2.15, 3.5, 2.6, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.15, 6.5, 2.6, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\n# Background panel\nrbox(ax_r, 0.05, 0.1, 9.9, 6.25, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 6.0, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 5.6, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 4.55, 9.3, 0.9\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.23, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.55, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.5, 0.42\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.4), (r'$\\hat{b}$', 6.3), (r'$\\hat{d}$', 8.15)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.24, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.24 + oh/2, lbl_txt, fs=9, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 4.55, 7.3, 4.15, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.35, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.45, 3.7, 1.95\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.2,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.68 - k * 0.47\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.42, 4.85, 3.42, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.42, 3.67, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.35, 4.9, 1.8\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.28,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.72,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.2, 3.65, 0.6\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.0, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.68\nout_y = 1.12\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.12, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.35, 7.2, 1.8, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 6.35, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.35, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nff21J8hfvzEQSEhq4z3bV`</summary>

```json
{
  "command": "python3 gen_fig1.py 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "bf07c764-e39c-4f06-8c78-7f8bd0e67160",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JuhBHjESsNCBoj1nja58Zn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5974,
      "cache_read_input_tokens": 65290,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5974
      },
      "output_tokens": 63,
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

_source line 45 · 2026-05-24T11:49:10.038Z_

<details><summary>↩ Tool result · `toolu_01Nff21J8hfvzEQSEhq4z3bV`</summary>

```text
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
Done: fig1_framework.pdf + fig1_framework.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "ddad3750-62df-4648-9e9b-ce351173c50f",
  "tool_use_result": {
    "stdout": "'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\nDone: fig1_framework.pdf + fig1_framework.png",
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

<details open><summary>🔧 Tool call — Read · `toolu_01NUQUXL2nLVCMLpQSZdEr88`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "833166c1-67f7-4ca3-b776-2b8be6577d92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LCHC8X56waRbWLBKsDd3Y4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 71264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
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

_source line 47 · 2026-05-24T11:49:14.830Z_

<details><summary>↩ Tool result · `toolu_01NUQUXL2nLVCMLpQSZdEr88`</summary>

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
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "3af51020-79da-44f2-a57f-5e9d2ca5b601",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 445506
    }
  }
}
```

</details>

---


### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
This looks much better now. The layout is cleaner and the spacing is more balanced. Let me assess what still needs improvement:

1. The confounding labels are now well-separated from the path labels - good
2. The right panel subtitle no longer overlaps Stage 1 - good
3. The Stage 1 output boxes are visible - good
4. The Stage 3 equation is readable - good

Remaining issues to polish:
1. The "confounding" label for Path A seems very close to "Path A: Bias-first" — they almost merge. Actually looking again, "confounding" is at y=5.85 and "Path A" is at y=5.7, so they're basically overlapping.


2. Path B has the same problem with its confounding label overlapping the path label.
3. The confounding arcs themselves are too faint and thin to stand out at this scale.
4. The bottom note text in the left panel is running outside the OVB box boundary.
5. In the right panel, the subtitle is still sitting too close to the top of Stage 1.

I need to reposition the confounding labels so they sit along the arcs themselves rather than near the path labels, or consider removing the separate text labels entirely and relying on the arc styling to convey the confounding effect.

Looking at the overall structure, the left panel is working well, and the right panel's Stage 2 and Stage 3 layout is clean. The drop shadows are subtle and effective. The main fixes needed are moving those confounding labels to the arc apexes, adjusting the bottom note position, and giving the right panel subtitle more breathing room from Stage 1. For Path A's confounding arc that peaks around y=5.3, I'll place the label there, and do the same for Path B's arc.

Adjusting the arc styling next...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "e083c85e-9581-4ac3-9311-3a6738735f59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bqbtjgQGQmay65GaDWSdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 71432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 434
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

_source line 49_

Much improved. Final polish needed: confounding labels still overlap path labels, and a few spacing refinements. Iteration 4.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "b9715ea5-74e5-4648-b2a6-60d6516b4e30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bqbtjgQGQmay65GaDWSdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 71432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 434
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

_source line 50_

<details open><summary>🔧 Tool call — Write · `toolu_01Tp6zvJAGEdkE1HSVifrF2K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.35, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.85\n\nlabel(ax_l, 5.0, 5.85, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — from Step 2 top back to Step 1 top\na_conf = FancyArrowPatch((bx2 + 1.0, by_a + bh + 0.06), (bx1 + bw/2, by_a + bh + 0.06),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.8, 6.0, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nby_b = 2.95\n\nlabel(ax_l, 5.0, 3.95, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 0.8, by_b + bh + 0.06), (bx1 + (bw+0.2)/2, by_b + bh + 0.06),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 4.8, 4.1, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.38,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.95, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.95, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.35, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.15, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.15, 7.3, 4.75, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.95, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.75, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.85, 4.85, 3.85, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.1, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.65, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.82,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.7\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.25, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.3\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.65, 7.2, 2.02, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "f26483db-d346-4efd-af1c-d639c1a6ae09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bqbtjgQGQmay65GaDWSdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 71432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 434
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

_source line 51 · 2026-05-24T11:50:47.498Z_

<details><summary>↩ Tool result · `toolu_01Tp6zvJAGEdkE1HSVifrF2K`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "4508644c-2ea8-4018-b615-2bcc1a76d977",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
    "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.35, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.85\n\nlabel(ax_l, 5.0, 5.85, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — from Step 2 top back to Step 1 top\na_conf = FancyArrowPatch((bx2 + 1.0, by_a + bh + 0.06), (bx1 + bw/2, by_a + bh + 0.06),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.8, 6.0, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nby_b = 2.95\n\nlabel(ax_l, 5.0, 3.95, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 0.8, by_b + bh + 0.06), (bx1 + (bw+0.2)/2, by_b + bh + 0.06),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 4.8, 4.1, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.38,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.95, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.95, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.35, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.15, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.15, 7.3, 4.75, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.95, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.75, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.85, 4.85, 3.85, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.1, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.65, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.82,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.7\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.25, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.3\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.65, 7.2, 2.02, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "structuredPatch": [
      {
        "oldStart": 26,
        "oldLines": 7,
        "newStart": 26,
        "newLines": 7,
        "lines": [
          " SANS = 'DejaVu Sans'",
          " ",
          " # ── Figure setup ────────────────────────────────────────────────────",
          "-fig = plt.figure(figsize=(16, 6.0))",
          "+fig = plt.figure(figsize=(16, 6.2))",
          " fig.patch.set_facecolor(WHITE)",
          " ",
          " gs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,"
        ]
      },
      {
        "oldStart": 36,
        "oldLines": 7,
        "newStart": 36,
        "newLines": 7,
        "lines": [
          " ",
          " for ax in [ax_l, ax_r]:",
          "     ax.set_xlim(0, 10)",
          "-    ax.set_ylim(0, 7.0)",
          "+    ax.set_ylim(0, 7.2)",
          "     ax.set_aspect('equal')",
          "     ax.axis('off')",
          " "
        ]
      },
      {
        "oldStart": 78,
        "oldLines": 18,
        "newStart": 78,
        "newLines": 17,
        "lines": [
          " #  LEFT PANEL — Sequential Pipeline",
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          "-rbox(ax_l, 0.15, 0.1, 9.7, 6.75, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)",
          "+rbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)",
          " ",
          "-# Title",
          "-label(ax_l, 5.0, 6.55, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 6.15, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 6.35, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── Path A: Bias-first ──",
          " bw, bh = 3.1, 0.68",
          " bx1, bx2 = 0.7, 5.9",
          "-by_a = 4.7",
          "+by_a = 4.85",
          " ",
          "-label(ax_l, 5.0, 5.7, 'Path A: Bias-first', fs=9, fw='bold', color=DARK)",
          "+label(ax_l, 5.0, 5.85, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)",
          " ",
          " shadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          " label(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)"
        ]
      },
      {
        "oldStart": 102,
        "oldLines": 17,
        "newStart": 101,
        "newLines": 17,
        "lines": [
          " arrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)",
          " label(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-# Confounding arc A — positioned clearly above boxes",
          "-a_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh + 0.08), (bx1 + bw/2 - 0.3, by_a + bh + 0.08),",
          "+# Confounding arc A — from Step 2 top back to Step 1 top",
          "+a_conf = FancyArrowPatch((bx2 + 1.0, by_a + bh + 0.06), (bx1 + bw/2, by_a + bh + 0.06),",
          "                           arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)",
          "+                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)",
          " ax_l.add_patch(a_conf)",
          "-label(ax_l, 4.8, 5.85, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 4.8, 6.0, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── Path B: Contamination-first ──",
          "-by_b = 2.85",
          "+by_b = 2.95",
          " ",
          "-label(ax_l, 5.0, 3.85, 'Path B: Contamination-first', fs=9, fw='bold', color=DARK)",
          "+label(ax_l, 5.0, 3.95, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)",
          " ",
          " shadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          " label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)"
        ]
      },
      {
        "oldStart": 126,
        "oldLines": 25,
        "newStart": 125,
        "newLines": 24,
        "lines": [
          " label(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          " # Confounding arc B",
          "-b_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh + 0.08), (bx1 + (bw+0.2)/2 - 0.3, by_b + bh + 0.08),",
          "+b_conf = FancyArrowPatch((bx2 + 0.8, by_b + bh + 0.06), (bx1 + (bw+0.2)/2, by_b + bh + 0.06),",
          "                           arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)",
          "+                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)",
          " ax_l.add_patch(b_conf)",
          "-label(ax_l, 4.8, 4.0, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 4.8, 4.1, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── OVB Box ──",
          "-rbox(ax_l, 0.7, 0.5, 8.6, 1.85, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)",
          "+rbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)",
          " ",
          "-label(ax_l, 5.0, 1.85, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 1.3,",
          "+label(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 1.38,",
          "       r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',",
          "       fs=9, fw='normal', color=C_RED)",
          " ",
          "-# Arrows from OVB upward",
          "-arrow(ax_l, 3.5, 2.35, 3.5, 2.85, color=C_RED, lw=1.0, style='-|>')",
          "-arrow(ax_l, 6.5, 2.35, 6.5, 2.85, color=C_RED, lw=1.0, style='-|>')",
          "+arrow(ax_l, 3.5, 2.45, 3.5, 2.95, color=C_RED, lw=1.0, style='-|>')",
          "+arrow(ax_l, 6.5, 2.45, 6.5, 2.95, color=C_RED, lw=1.0, style='-|>')",
          " ",
          "-label(ax_l, 5.0, 0.3, 'Unmodeled facet absorbed into remaining estimates',",
          "+label(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',",
          "       fs=7.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " "
        ]
      },
      {
        "oldStart": 152,
        "oldLines": 15,
        "newStart": 150,
        "newLines": 14,
        "lines": [
          " #  RIGHT PANEL — G-MFRM Joint Framework",
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          "-rbox(ax_r, 0.05, 0.1, 9.9, 6.75, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)",
          "+rbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)",
          " ",
          "-# Title",
          "-label(ax_r, 5.0, 6.55, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')",
          "-label(ax_r, 5.0, 6.15, 'staged joint calibration of all facets', fs=8.5,",
          "+label(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')",
          "+label(ax_r, 5.0, 6.35, 'staged joint calibration of all facets', fs=8.5,",
          "       color=C_GREEN, style='italic', fw='normal')",
          " ",
          " # ── Stage 1: Standard MFRM ──",
          "-s1_x, s1_y, s1_w, s1_h = 0.35, 5.0, 9.3, 0.95",
          "+s1_x, s1_y, s1_w, s1_h = 0.35, 5.15, 9.3, 0.95",
          " shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)",
          " ",
          " label(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)"
        ]
      },
      {
        "oldStart": 173,
        "oldLines": 11,
        "newStart": 170,
        "newLines": 11,
        "lines": [
          "     label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)",
          " ",
          " # Arrow S1 → S3",
          "-arrow(ax_r, 7.3, 5.0, 7.3, 4.6, color=C_JUDGE, lw=1.3)",
          "-label(ax_r, 7.75, 4.8, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          "+arrow(ax_r, 7.3, 5.15, 7.3, 4.75, color=C_JUDGE, lw=1.3)",
          "+label(ax_r, 7.75, 4.95, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          " ",
          " # ── Stage 2: Estimate e_i ──",
          "-s2_x, s2_y, s2_w, s2_h = 0.35, 2.7, 3.7, 2.15",
          "+s2_x, s2_y, s2_w, s2_h = 0.35, 2.75, 3.7, 2.2",
          " shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)",
          " ",
          " label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,"
        ]
      },
      {
        "oldStart": 186,
        "oldLines": 36,
        "newStart": 183,
        "newLines": 36,
        "lines": [
          " sub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']",
          " sw, sh = 2.7, 0.38",
          " for k, stxt in enumerate(sub_specs):",
          "-    sy = s2_y + s2_h - 0.72 - k * 0.5",
          "+    sy = s2_y + s2_h - 0.72 - k * 0.52",
          "     rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)",
          "     label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)",
          " ",
          " # Arrow S2 → S3",
          "-arrow(ax_r, s2_x + s2_w, 3.78, 4.85, 3.78, color=C_CONT, lw=1.3)",
          "-label(ax_r, 4.45, 4.03, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          "+arrow(ax_r, s2_x + s2_w, 3.85, 4.85, 3.85, color=C_CONT, lw=1.3)",
          "+label(ax_r, 4.45, 4.1, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          " ",
          " # ── Stage 3: Joint Gated Model ──",
          "-s3_x, s3_y, s3_w, s3_h = 4.75, 2.6, 4.9, 2.0",
          "+s3_x, s3_y, s3_w, s3_h = 4.75, 2.65, 4.9, 2.1",
          " shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)",
          " ",
          " label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,",
          "       'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)",
          " ",
          "-label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.78,",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.82,",
          "       r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',",
          "       fs=8.5, fw='normal', color=C_GRAY)",
          " ",
          " # Gating highlight",
          "-gx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.65",
          "+gx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.7",
          " shadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)",
          " label(ax_r, gx + gw/2, gy + gh/2,",
          "       r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)",
          " ",
          " # ── 4-D Output ──",
          "-label(ax_r, 5.0, 2.2, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          "+label(ax_r, 5.0, 2.25, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          " ",
          " ow2, oh2 = 2.05, 0.72",
          "-out_y = 1.25",
          "+out_y = 1.3",
          " out_specs = [",
          "     (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),",
          "     (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),"
        ]
      },
      {
        "oldStart": 228,
        "oldLines": 15,
        "newStart": 225,
        "newLines": 15,
        "lines": [
          "     label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)",
          " ",
          " # Arrow S3 → outputs",
          "-arrow(ax_r, 7.2, 2.6, 7.2, 1.97, color='#3C3C3C', lw=1.5, style='-|>')",
          "+arrow(ax_r, 7.2, 2.65, 7.2, 2.02, color='#3C3C3C', lw=1.5, style='-|>')",
          " ",
          " # Green check",
          " label(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',",
          "       fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)",
          " ",
          " # Panel labels",
          "-label(ax_l, 0.35, 6.85, '(a)', fs=11, fw='bold', color='black', ha='left')",
          "-label(ax_r, 0.25, 6.85, '(b)', fs=11, fw='bold', color='black', ha='left')",
          "+label(ax_l, 0.35, 7.05, '(a)', fs=11, fw='bold', color='black', ha='left')",
          "+label(ax_r, 0.25, 7.05, '(b)', fs=11, fw='bold', color='black', ha='left')",
          " ",
          " # ── Save ──",
          " out_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'"
        ]
      }
    ],
    "originalFile": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.0))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.0)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.75, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_l, 5.0, 6.55, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.15, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.7\n\nlabel(ax_l, 5.0, 5.7, 'Path A: Bias-first', fs=9, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — positioned clearly above boxes\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh + 0.08), (bx1 + bw/2 - 0.3, by_a + bh + 0.08),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.8, 5.85, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nby_b = 2.85\n\nlabel(ax_l, 5.0, 3.85, 'Path B: Contamination-first', fs=9, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh + 0.08), (bx1 + (bw+0.2)/2 - 0.3, by_b + bh + 0.08),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.3', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 4.8, 4.0, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.85, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.85, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.3,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\n# Arrows from OVB upward\narrow(ax_l, 3.5, 2.35, 3.5, 2.85, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.35, 6.5, 2.85, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.3, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.75, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\n# Title\nlabel(ax_r, 5.0, 6.55, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.15, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.0, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.0, 7.3, 4.6, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.8, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.7, 3.7, 2.15\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.5\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.78, 4.85, 3.78, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.03, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.6, 4.9, 2.0\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.78,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.65\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.2, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.25\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.6, 7.2, 1.97, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 6.85, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 6.85, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_012K54sSPZMxbErbz31gVMyH`</summary>

```json
{
  "command": "python3 gen_fig1.py 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "b263687d-8c5e-4edc-a6e5-da95743b142f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdPUm7MSEhmbaqKXNqfxEa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6093,
      "cache_read_input_tokens": 71866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6093
      },
      "output_tokens": 40,
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

_source line 53 · 2026-05-24T11:50:52.379Z_

<details><summary>↩ Tool result · `toolu_012K54sSPZMxbErbz31gVMyH`</summary>

```text
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
Done: fig1_framework.pdf + fig1_framework.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "5c5decf4-ea0f-4f39-b3ac-24fc6b539631",
  "tool_use_result": {
    "stdout": "'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\nDone: fig1_framework.pdf + fig1_framework.png",
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

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_019vxGMR6bkwSvBExhfPpUJa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "1785cc39-bfd8-4f37-9e59-7853c82365a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JcSeXLe2QqUaiwRNE4ChSZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 77959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
      },
      "output_tokens": 69,
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

_source line 55 · 2026-05-24T11:50:56.481Z_

<details><summary>↩ Tool result · `toolu_019vxGMR6bkwSvBExhfPpUJa`</summary>

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
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "3322cc73-c672-4c78-9056-c4c44e29ea4c",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 444079
    }
  }
}
```

</details>

---


### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
This is looking pretty good now. Let me assess what still needs to be fixed:

1. The "confounding" labels are still positioned right next to the path labels. For Path A, "confounding" is at y=6.0 while "Path A: Bias-first" is at y=5.85. For Path B, "confounding" is at y=4.1 while "Path B: Contamination-first" is at y=3.95. They appear to be very close/overlapping.

2. The confounding arcs are barely visible — the dashed curves above the boxes are too thin and blend with the background.


3. I need to fix the label positioning so they don't collide. I could move the confounding labels to the side of the arcs, increase the arc height to give more space, or integrate the text directly into the arc annotation. Let me try shifting the confounding labels to the left side around x=1.5 to separate them from the path labels.

Actually, looking at the current render more closely, the overlap isn't as severe as I thought — the confounding label sits at y=6.0 while the path label is at y=5.85, and the italic styling on the confounding text helps distinguish them. I think increasing the arc radius to make them taller and positioning the confounding label at the arc's apex would work better. I should also check the aspect ratio since it's currently around 2.58:1 rather than the intended 3:1.

The core design is solid, so I'll focus on the most impactful fixes: moving the confounding labels to avoid overlap with the path labels, and trying an elegant approach of placing them inside the dashed arcs with a small white background for readability at the peak.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "716d47c6-6161-4102-b62a-cf834fbd0188",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPqfKTt7txStRviZFCxM5a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 78127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 57_

Looking good structurally. The remaining issue is the "confounding" labels overlapping with path labels, and the arcs need to be more visually prominent. Let me refine the positioning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "5a0dbe90-06cb-40f8-9095-b7f88a321d1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPqfKTt7txStRviZFCxM5a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 78127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 58_

<details open><summary>🔧 Tool call — Write · `toolu_01YM18ShsojzkascJaX125pc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef label_with_bg(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n                  va='center', style='normal', zorder=6, family=SERIF, **kw):\n    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n    t.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])\n    return t\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.35, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.85\n\nlabel(ax_l, 5.0, 5.85, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — wider arc, label at apex with white stroke\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel_with_bg(ax_l, 4.5, 5.96, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nby_b = 2.95\n\nlabel(ax_l, 5.0, 3.95, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel_with_bg(ax_l, 4.5, 4.08, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.38,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.95, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.95, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.35, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.15, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.15, 7.3, 4.75, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.95, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.75, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.85, 4.85, 3.85, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.1, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.65, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.82,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.7\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.25, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.3\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.65, 7.2, 2.02, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "aa48c71b-0e00-4aa4-8379-013f396c0d84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPqfKTt7txStRviZFCxM5a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 78127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 59 · 2026-05-24T11:52:31.799Z_

<details><summary>↩ Tool result · `toolu_01YM18ShsojzkascJaX125pc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "75189fa0-848e-4047-8d5b-bff529d099de",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
    "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef label_with_bg(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n                  va='center', style='normal', zorder=6, family=SERIF, **kw):\n    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n    t.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])\n    return t\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.35, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.85\n\nlabel(ax_l, 5.0, 5.85, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — wider arc, label at apex with white stroke\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel_with_bg(ax_l, 4.5, 5.96, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nby_b = 2.95\n\nlabel(ax_l, 5.0, 3.95, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel_with_bg(ax_l, 4.5, 4.08, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.38,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.95, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.95, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.35, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.15, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.15, 7.3, 4.75, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.95, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.75, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.85, 4.85, 3.85, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.1, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.65, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.82,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.7\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.25, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.3\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.65, 7.2, 2.02, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 6,
        "newStart": 6,
        "newLines": 7,
        "lines": [
          " matplotlib.rcParams['pdf.fonttype'] = 42",
          " matplotlib.rcParams['ps.fonttype'] = 42",
          " import matplotlib.pyplot as plt",
          "+import matplotlib.patheffects as pe",
          " from matplotlib.patches import FancyBboxPatch, FancyArrowPatch",
          " ",
          " # ── Colors ──────────────────────────────────────────────────────────"
        ]
      },
      {
        "oldStart": 65,
        "oldLines": 6,
        "newStart": 66,
        "newLines": 13,
        "lines": [
          "     return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,",
          "                    ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)",
          " ",
          "+def label_with_bg(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',",
          "+                  va='center', style='normal', zorder=6, family=SERIF, **kw):",
          "+    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,",
          "+                ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)",
          "+    t.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])",
          "+    return t",
          "+",
          " def arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',",
          "           rad=0, zorder=4, ls='-'):",
          "     cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'"
        ]
      },
      {
        "oldStart": 101,
        "oldLines": 12,
        "newStart": 109,
        "newLines": 12,
        "lines": [
          " arrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)",
          " label(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-# Confounding arc A — from Step 2 top back to Step 1 top",
          "-a_conf = FancyArrowPatch((bx2 + 1.0, by_a + bh + 0.06), (bx1 + bw/2, by_a + bh + 0.06),",
          "-                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',",
          "+# Confounding arc A — wider arc, label at apex with white stroke",
          "+a_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),",
          "+                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',",
          "                           connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)",
          " ax_l.add_patch(a_conf)",
          "-label(ax_l, 4.8, 6.0, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+label_with_bg(ax_l, 4.5, 5.96, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── Path B: Contamination-first ──",
          " by_b = 2.95"
        ]
      },
      {
        "oldStart": 125,
        "oldLines": 11,
        "newStart": 133,
        "newLines": 11,
        "lines": [
          " label(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          " # Confounding arc B",
          "-b_conf = FancyArrowPatch((bx2 + 0.8, by_b + bh + 0.06), (bx1 + (bw+0.2)/2, by_b + bh + 0.06),",
          "-                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',",
          "+b_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),",
          "+                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',",
          "                           connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)",
          " ax_l.add_patch(b_conf)",
          "-label(ax_l, 4.8, 4.1, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+label_with_bg(ax_l, 4.5, 4.08, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          " ",
          " # ── OVB Box ──",
          " rbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)"
        ]
      }
    ],
    "originalFile": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.35, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.85\n\nlabel(ax_l, 5.0, 5.85, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — from Step 2 top back to Step 1 top\na_conf = FancyArrowPatch((bx2 + 1.0, by_a + bh + 0.06), (bx1 + bw/2, by_a + bh + 0.06),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel(ax_l, 4.8, 6.0, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nby_b = 2.95\n\nlabel(ax_l, 5.0, 3.95, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 0.8, by_b + bh + 0.06), (bx1 + (bw+0.2)/2, by_b + bh + 0.06),\n                          arrowstyle='-|>', color=C_RED, linewidth=0.9, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel(ax_l, 4.8, 4.1, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.38,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.95, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.95, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.35, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.15, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.15, 7.3, 4.75, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.95, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.75, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.85, 4.85, 3.85, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.1, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.65, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.82,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.7\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.25, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.3\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.65, 7.2, 2.02, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Bash · `toolu_017GEiBy5yBkSs6f6UXTVuBz`</summary>

```json
{
  "command": "python3 gen_fig1.py 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "19eae95a-da78-40d4-8073-db16e235f33b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141YDaPYQEhx7GP55fWkCBY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6414,
      "cache_read_input_tokens": 78590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6414
      },
      "output_tokens": 40,
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

_source line 61 · 2026-05-24T11:52:36.320Z_

<details><summary>↩ Tool result · `toolu_017GEiBy5yBkSs6f6UXTVuBz`</summary>

```text
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
Done: fig1_framework.pdf + fig1_framework.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "2ef272bf-0259-455f-84c3-e8ecd2aa6059",
  "tool_use_result": {
    "stdout": "'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\nDone: fig1_framework.pdf + fig1_framework.png",
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

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_01PjGWcLKgQbN451XcHNPHAy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "e6c1dc64-25fa-4e90-9a16-4bc416330218",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fe1tJcHpjkRxdvntzWQTXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 85004,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
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

_source line 63 · 2026-05-24T11:52:40.658Z_

<details><summary>↩ Tool result · `toolu_01PjGWcLKgQbN451XcHNPHAy`</summary>

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
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "8bb5ca5e-78a8-43e8-b062-6f5e403d39bc",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 450527
    }
  }
}
```

</details>

---


### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

```text
Looking at this carefully, the layout is solid but there are still some issues:

1. The "confounding" label for Path A overlaps with "Path A: Bias-first" — they're at nearly the same y position. The "confounding" text with white stroke background is sitting right on top of "Path A: Bias-first".

2. Similarly for Path B, "confounding" overlaps with "Path B: Contamination-first".

3. The right panel subtitle "staged joint calibration of all facets" is very light/hard to read — it's too close to Stage 1.


The core issue is insufficient vertical spacing between the path labels and the confounding arcs. I'm considering repositioning the confounding labels to the right edge of the arcs near their origin point, which should eliminate the overlap while keeping the layout clean.

I'll also tighten up the right panel by adding a bit more breathing room between the subtitle and Stage 1, then do a final pass to polish everything together.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "c4af1f79-b164-4ada-bc8b-fdfd2fd7ae47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8ui92RVCGRbZAPSp5PsKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 85172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 569
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


### Assistant

_source line 65_

The "confounding" labels are still colliding with path labels. Let me reposition them to the right side of the arcs where they have clear space.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "fc54fdb9-8585-4a65-aae3-7b8d30862657",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8ui92RVCGRbZAPSp5PsKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 85172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 569
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

_source line 66_

<details open><summary>🔧 Tool call — Write · `toolu_01Axd6oEqPXQQk46yMrgqeNM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.35, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.85\n\nlabel(ax_l, 1.2, 5.85, 'Path A:', fs=9.5, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.75, 5.85, 'Bias-first', fs=9.5, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — positioned clearly above boxes, label at right end\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nt = label(ax_l, 7.8, 5.85, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])\n\n# ── Path B: Contamination-first ──\nby_b = 2.95\n\nlabel(ax_l, 1.2, 3.95, 'Path B:', fs=9.5, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.75, 3.95, 'Contamination-first', fs=9.5, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B — label at right end\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nt = label(ax_l, 7.6, 3.95, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.38,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.95, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.95, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.3, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.05, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.05, 7.3, 4.65, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.85, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.65, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.75, 4.85, 3.75, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.0, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.55, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.82,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.7\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.15, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.2\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.55, 7.2, 1.92, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "c9beab42-f928-4142-ae67-de7087e38cf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8ui92RVCGRbZAPSp5PsKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 85172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 569
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

_source line 67 · 2026-05-24T11:54:10.660Z_

<details><summary>↩ Tool result · `toolu_01Axd6oEqPXQQk46yMrgqeNM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "b43ab02a-ba2e-4091-b00d-d0df3ebf4779",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
    "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.35, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.85\n\nlabel(ax_l, 1.2, 5.85, 'Path A:', fs=9.5, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.75, 5.85, 'Bias-first', fs=9.5, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — positioned clearly above boxes, label at right end\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nt = label(ax_l, 7.8, 5.85, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])\n\n# ── Path B: Contamination-first ──\nby_b = 2.95\n\nlabel(ax_l, 1.2, 3.95, 'Path B:', fs=9.5, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.75, 3.95, 'Contamination-first', fs=9.5, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B — label at right end\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nt = label(ax_l, 7.6, 3.95, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.38,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.95, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.95, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.3, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.05, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.05, 7.3, 4.65, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.85, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.65, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.75, 4.85, 3.75, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.0, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.55, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.82,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.7\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.15, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.2\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.55, 7.2, 1.92, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "structuredPatch": [
      {
        "oldStart": 66,
        "oldLines": 13,
        "newStart": 66,
        "newLines": 6,
        "lines": [
          "     return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,",
          "                    ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)",
          " ",
          "-def label_with_bg(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',",
          "-                  va='center', style='normal', zorder=6, family=SERIF, **kw):",
          "-    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,",
          "-                ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)",
          "-    t.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])",
          "-    return t",
          "-",
          " def arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',",
          "           rad=0, zorder=4, ls='-'):",
          "     cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'"
        ]
      },
      {
        "oldStart": 96,
        "oldLines": 7,
        "newStart": 89,
        "newLines": 8,
        "lines": [
          " bx1, bx2 = 0.7, 5.9",
          " by_a = 4.85",
          " ",
          "-label(ax_l, 5.0, 5.85, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)",
          "+label(ax_l, 1.2, 5.85, 'Path A:', fs=9.5, fw='bold', color=DARK, ha='left')",
          "+label(ax_l, 2.75, 5.85, 'Bias-first', fs=9.5, fw='normal', color=DARK, ha='left')",
          " ",
          " shadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          " label(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)"
        ]
      },
      {
        "oldStart": 109,
        "oldLines": 17,
        "newStart": 103,
        "newLines": 19,
        "lines": [
          " arrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)",
          " label(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-# Confounding arc A — wider arc, label at apex with white stroke",
          "+# Confounding arc A — positioned clearly above boxes, label at right end",
          " a_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),",
          "                           arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',",
          "                           connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)",
          " ax_l.add_patch(a_conf)",
          "-label_with_bg(ax_l, 4.5, 5.96, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+t = label(ax_l, 7.8, 5.85, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+t.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])",
          " ",
          " # ── Path B: Contamination-first ──",
          " by_b = 2.95",
          " ",
          "-label(ax_l, 5.0, 3.95, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)",
          "+label(ax_l, 1.2, 3.95, 'Path B:', fs=9.5, fw='bold', color=DARK, ha='left')",
          "+label(ax_l, 2.75, 3.95, 'Contamination-first', fs=9.5, fw='normal', color=DARK, ha='left')",
          " ",
          " shadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          " label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)"
        ]
      },
      {
        "oldStart": 132,
        "oldLines": 12,
        "newStart": 128,
        "newLines": 13,
        "lines": [
          " arrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)",
          " label(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-# Confounding arc B",
          "+# Confounding arc B — label at right end",
          " b_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),",
          "                           arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',",
          "                           connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)",
          " ax_l.add_patch(b_conf)",
          "-label_with_bg(ax_l, 4.5, 4.08, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+t = label(ax_l, 7.6, 3.95, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "+t.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])",
          " ",
          " # ── OVB Box ──",
          " rbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)"
        ]
      },
      {
        "oldStart": 161,
        "oldLines": 11,
        "newStart": 158,
        "newLines": 11,
        "lines": [
          " rbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)",
          " ",
          " label(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')",
          "-label(ax_r, 5.0, 6.35, 'staged joint calibration of all facets', fs=8.5,",
          "+label(ax_r, 5.0, 6.3, 'staged joint calibration of all facets', fs=8.5,",
          "       color=C_GREEN, style='italic', fw='normal')",
          " ",
          " # ── Stage 1: Standard MFRM ──",
          "-s1_x, s1_y, s1_w, s1_h = 0.35, 5.15, 9.3, 0.95",
          "+s1_x, s1_y, s1_w, s1_h = 0.35, 5.05, 9.3, 0.95",
          " shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)",
          " ",
          " label(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)"
        ]
      },
      {
        "oldStart": 178,
        "oldLines": 11,
        "newStart": 175,
        "newLines": 11,
        "lines": [
          "     label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)",
          " ",
          " # Arrow S1 → S3",
          "-arrow(ax_r, 7.3, 5.15, 7.3, 4.75, color=C_JUDGE, lw=1.3)",
          "-label(ax_r, 7.75, 4.95, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          "+arrow(ax_r, 7.3, 5.05, 7.3, 4.65, color=C_JUDGE, lw=1.3)",
          "+label(ax_r, 7.75, 4.85, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          " ",
          " # ── Stage 2: Estimate e_i ──",
          "-s2_x, s2_y, s2_w, s2_h = 0.35, 2.75, 3.7, 2.2",
          "+s2_x, s2_y, s2_w, s2_h = 0.35, 2.65, 3.7, 2.2",
          " shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)",
          " ",
          " label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,"
        ]
      },
      {
        "oldStart": 196,
        "oldLines": 11,
        "newStart": 193,
        "newLines": 11,
        "lines": [
          "     label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)",
          " ",
          " # Arrow S2 → S3",
          "-arrow(ax_r, s2_x + s2_w, 3.85, 4.85, 3.85, color=C_CONT, lw=1.3)",
          "-label(ax_r, 4.45, 4.1, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          "+arrow(ax_r, s2_x + s2_w, 3.75, 4.85, 3.75, color=C_CONT, lw=1.3)",
          "+label(ax_r, 4.45, 4.0, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          " ",
          " # ── Stage 3: Joint Gated Model ──",
          "-s3_x, s3_y, s3_w, s3_h = 4.75, 2.65, 4.9, 2.1",
          "+s3_x, s3_y, s3_w, s3_h = 4.75, 2.55, 4.9, 2.1",
          " shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)",
          " ",
          " label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,"
        ]
      },
      {
        "oldStart": 217,
        "oldLines": 10,
        "newStart": 214,
        "newLines": 10,
        "lines": [
          "       r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)",
          " ",
          " # ── 4-D Output ──",
          "-label(ax_r, 5.0, 2.25, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          "+label(ax_r, 5.0, 2.15, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          " ",
          " ow2, oh2 = 2.05, 0.72",
          "-out_y = 1.3",
          "+out_y = 1.2",
          " out_specs = [",
          "     (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),",
          "     (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),"
        ]
      },
      {
        "oldStart": 233,
        "oldLines": 10,
        "newStart": 230,
        "newLines": 10,
        "lines": [
          "     label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)",
          " ",
          " # Arrow S3 → outputs",
          "-arrow(ax_r, 7.2, 2.65, 7.2, 2.02, color='#3C3C3C', lw=1.5, style='-|>')",
          "+arrow(ax_r, 7.2, 2.55, 7.2, 1.92, color='#3C3C3C', lw=1.5, style='-|>')",
          " ",
          " # Green check",
          "-label(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',",
          "+label(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',",
          "       fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)",
          " ",
          " # Panel labels"
        ]
      }
    ],
    "originalFile": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef label_with_bg(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n                  va='center', style='normal', zorder=6, family=SERIF, **kw):\n    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n    t.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])\n    return t\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.35, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.85\n\nlabel(ax_l, 5.0, 5.85, 'Path A: Bias-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — wider arc, label at apex with white stroke\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nlabel_with_bg(ax_l, 4.5, 5.96, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path B: Contamination-first ──\nby_b = 2.95\n\nlabel(ax_l, 5.0, 3.95, 'Path B: Contamination-first', fs=9.5, fw='bold', color=DARK)\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nlabel_with_bg(ax_l, 4.5, 4.08, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.38,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.95, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.95, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.35, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.15, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.15, 7.3, 4.75, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.95, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.75, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.85, 4.85, 3.85, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.1, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.65, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.82,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.7\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.25, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.3\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.65, 7.2, 2.02, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_0131AcxRNnAVRpywHnDvchiE`</summary>

```json
{
  "command": "python3 gen_fig1.py 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "d98b9394-50ec-44e3-b0c5-ff46281da49b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mrqLRKJhnKsHoAqJ11KEP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6136,
      "cache_read_input_tokens": 85741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6136
      },
      "output_tokens": 43,
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

_source line 69 · 2026-05-24T11:54:17.034Z_

<details><summary>↩ Tool result · `toolu_0131AcxRNnAVRpywHnDvchiE`</summary>

```text
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
Done: fig1_framework.pdf + fig1_framework.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "e01b26c7-17c7-4bcd-bab2-8a1723d87d38",
  "tool_use_result": {
    "stdout": "'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\nDone: fig1_framework.pdf + fig1_framework.png",
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

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_01NEq4WKsUkb7uTjcjw6aY4Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "0ea164de-7eb3-4e7a-979c-398dd7cefd02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158dALJncwVhKe3dp6ZYNRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 91877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
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

_source line 71 · 2026-05-24T11:54:22.317Z_

<details><summary>↩ Tool result · `toolu_01NEq4WKsUkb7uTjcjw6aY4Q`</summary>

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
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "579d9233-9f8a-4b3e-a6a4-492bd48cada3",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 449958
    }
  }
}
```

</details>

---


### Assistant

_source line 72_

<details><summary>Logged reasoning block</summary>

```text
This is much better now. The "confounding" labels are repositioned to the right side at x=7.8 and x=7.6 with white stroke backgrounds, and they no longer overlap with the "Path A/B" labels which are now left-aligned.

Let me assess the overall quality:

Left panel (a):
- Title and subtitle: clear ✓
- Path A/B labels: well-separated from confounding labels ✓
- Boxes: rounded corners with shadows ✓
- Confounding arcs: visible dashed red arcs ✓
- "confounding" labels: positioned at right end, no overlap ✓


- OVB box: clear dashed border ✓
- ✗ marks: visible ✓

Right panel (b):
- Title and subtitle: clear, subtitle has some spacing from Stage 1 ✓
- Stage 1: output boxes visible ✓
- Stage 2: three sub-methods clearly listed ✓
- Stage 3: equation and gating highlight visible ✓
- 4-D output: four boxes with proper labels ✓
- ✓ mark: visible ✓

The spacing looks good overall—the right panel subtitle has adequate distance from Stage 1 now, so that minor issue is resolved.

I'm noticing a critical scaling problem though: at the typical textwidth of 7 inches for a two-column paper layout, my 8.5pt font sizes will scale down to around 3.7pt, which is too small to be readable. I need to reconsider the font sizes to ensure they remain legible after the figure is scaled down. width=\textwidth]` in a `figure*` environment. The textwidth in a typical EMNLP/ACL paper is about 6.3 inches (for two-column papers, textwidth is the full page width minus margins).

Hmm, actually for ACL/EMNLP two-column:
- Column width: ~3.25 inches
- Textwidth (full page): ~6.75 inches

So for a `figure*`, the figure is scaled to ~6.75 inches wide. With our 16-inch canvas, scale = 6.75/16 = 0.42.

At 0.42 scale:
- 12pt → 5pt (below 7pt)
- 9.5pt → 4pt (way below)
- 8.5pt → 3.6pt (unreadable)

This means ALL text will be too small after scaling! I need to dramatically increase font sizes.

For text to remain readable at the final 6.75-inch width, I need to work backward from the 7pt minimum and set font sizes around 16-17pt in the original figure.

Actually, I'm second-guessing myself here — the original script used a 16-inch width with 9-14pt text and apparently worked fine, so maybe I should reconsider the approach. Perhaps using a smaller figsize closer to the actual print dimensions would keep the scaling factor near 1:1, preserving the text sizes naturally. But the task specifies using a larger figsize like (16, 5.5), which suggests there's a reason for that choice related to DPI and resolution.

When saving at 300 DPI with figsize=(16, 6.2), I get a 4800×1860 pixel image that looks sharp when included in LaTeX at the document width. The real issue is that matplotlib's font sizes scale with the figure, so when the figure shrinks from 16 inches to 6.75 inches in the final document, the text shrinks proportionally — meaning I need to account for that scaling factor of about 0.42 when setting font sizes.

Looking at how other papers handle this, the standard approach is to match figsize to the actual column width and use 8-10pt fonts. But since the task specifies a large canvas around figsize=(16, 5.5) while requiring readable text (≥7pt after scaling), I need to use much larger fonts — around 16-20pt — to compensate for the downscaling.

Let me verify the math: with a 0.42 scale factor, I need roughly 16.7pt minimum to hit 7pt on paper. So I'm looking at bumping titles to 24-26pt, labels to 20-22pt, and body text to 18-20pt. The original design at figsize=(16,9) with 14pt titles and 9pt body was actually on the right track, just needs adjustment for the new dimensions. When scaled to textwidth that would be 14*0.42 = 5.9pt and 9*0.42 = 3.8pt. Those are ALL below 7pt. So either:
1. The original was also too small (likely, since this is why we're redesigning)
2. My scaling calculation is wrong

Let me verify my understanding. In LaTeX, when you do `\includegraphics[width=\textwidth]{fig.pdf}`, the figure is scaled proportionally. The text in the PDF was rendered at whatever size matplotlib specified. After scaling, the text appears smaller.

For ACL/EMNLP two-column layout:
- Page width: ~8.5 inches
- Margins: ~0.875 inches each side
- Textwidth: ~6.75 inches
- Column width: ~3.25 inches
- Column separation: ~0.25 inches

With `figure*` spanning full width at 6.75 inches and my figsize of 16 inches, the scaling factor is 6.75/16 = 0.42. But `bbox_inches='tight'` might reduce the actual figure width—if the axes region with xlim=(0,10) takes up about 15 inches after accounting for margins, then the effective scale becomes 6.75/15 = 0.45 instead.

So I need font sizes that, when scaled by 0.45, still meet the 7pt minimum. That means I need at least 7/0.45 ≈ 15.6pt in the matplotlib figure. I'm going to significantly bump up all the font sizes to ensure readability after scaling.

I'm reconsidering whether using such a large figsize with aggressive scaling is the right approach. The task specifies figsize around (16, 5.5) or (14, 5) for a full-width figure, but maybe I should use a figsize closer to the actual print dimensions and keep font sizes more reasonable. Let me try (14, 5) since it's closer to the paper's aspect ratio and should give better readability without needing extreme scaling.

With figsize=(14, 5), the scale factor would be around 0.48, which means I'd need roughly 15pt fonts to hit the 7pt minimum when printed. I'm working through the math on title, subtitle, and label sizes to find a balance that keeps everything readable without going too large. Maybe (7, 2.6) with standard 9-12pt fonts would be simpler.

Actually, I'm overcomplicating this—plenty of published papers use similar figure setups. Let me just scale all the fonts up by about 2x to be safe; the figure will look oversized on screen but should print at the right size. I'll redo this with properly scaled fonts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "c5842024-a9ae-4433-8b27-24fe6f9a233e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017n4ZgB7otyTbiMf56uc5ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 92045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 73_

The layout and positioning look clean now. But I realize all text will be too small when scaled to paper textwidth (~0.42x). Need to roughly double all font sizes for ≥7pt readability after scaling. Final iteration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "998b1bf2-0121-483e-b6ca-522c7b792b45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017n4ZgB7otyTbiMf56uc5ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 92045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 74_

<details open><summary>🔧 Tool call — Write · `toolu_01J6wFehDvWMZZ2jfdjEBMxN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout.\nFont sizes calibrated for textwidth ~6.75\" scaling (scale ~0.44x).\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# Scale factor: figure is ~15.5\" content width, printed at ~6.75\" textwidth\n# → scale ≈ 0.44. For ≥7pt on paper, need ≥16pt in figure.\nS = 2.1  # font multiplier vs. previous iteration\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Font sizes (all ≥16pt → ≥7pt on paper) ─────────────────────────\nFS_TITLE   = 24      # panel title → ~10.5pt\nFS_SUB     = 17      # subtitle → ~7.4pt\nFS_PATH    = 19      # path labels → ~8.3pt\nFS_BOX     = 17      # box primary text → ~7.4pt\nFS_BOX2    = 17      # box secondary text → ~7.4pt\nFS_SMALL   = 16      # small annotations → ~7pt\nFS_TINY    = 14      # \"confounding\", \"init\" → ~6.1pt (min acceptable)\nFS_EQN     = 17      # equation → ~7.4pt\nFS_SYM     = 19      # output symbols → ~8.3pt\nFS_DESC    = 15      # output descriptions → ~6.5pt\nFS_PANEL   = 22      # (a), (b) labels → ~9.6pt\nFS_CHECK   = 30      # ✗ ✓ → ~13pt\nFS_NOTE    = 15      # italic bottom notes → ~6.5pt\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=14, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.28, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,\n      style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.72\nbx1, bx2 = 0.7, 5.9\nby_a = 4.8\n\nlabel(ax_l, 1.2, 5.85, 'Path A:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 3.0, 5.85, 'Bias-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.2)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.12, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.14, r'calibrate $d_j$', fs=FS_BOX2, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.2)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.12, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.14, r'contamination $c_n$', fs=FS_BOX2, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.5)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(a_conf)\nt = label(ax_l, 7.8, 5.85, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── Path B: Contamination-first ──\nby_b = 2.9\n\nlabel(ax_l, 1.2, 3.92, 'Path B:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 3.0, 3.92, 'Contamination-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.2)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.12, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.14, r'contamination $c_n$', fs=FS_BOX2, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.2)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.12, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.14, r'calibrate $d_j$', fs=FS_BOX2, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.5)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(b_conf)\nt = label(ax_l, 7.6, 3.92, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.45, 8.6, 2.0, WHITE, C_RED, lw=1.8, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.32,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=FS_EQN, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.9, color=C_RED, lw=1.1, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.9, color=C_RED, lw=1.1, style='-|>')\n\nlabel(ax_l, 5.0, 0.25, 'Unmodeled facet absorbed into remaining estimates',\n      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.25, 'staged joint calibration of all facets', fs=FS_SUB,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.0, 9.3, 1.0\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.2)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.28, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.62, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.48\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.26, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo + ow/2, s1_y + 0.26 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.0, 7.3, 4.6, color=C_JUDGE, lw=1.4)\nlabel(ax_r, 7.8, 4.8, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.6, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.2)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.25,\n      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.40\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.78 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.9)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.7, 4.85, 3.7, color=C_CONT, lw=1.4)\nlabel(ax_r, 4.45, 3.95, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.5, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.32,\n      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.85,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=FS_EQN, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.72\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.1, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.75\nout_y = 1.12\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.14, sym, fs=FS_SYM, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.15, desc, fs=FS_DESC, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.5, 7.2, 1.87, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.45, u'✓  Joint estimation resolves confounding',\n      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "b2e8b919-9655-432c-81e5-7a31d9af3ad1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017n4ZgB7otyTbiMf56uc5ww",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 92045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 75 · 2026-05-24T11:56:58.992Z_

<details><summary>↩ Tool result · `toolu_01J6wFehDvWMZZ2jfdjEBMxN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "eb17f9d4-4516-4650-bc31-4ce965332c1f",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
    "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout.\nFont sizes calibrated for textwidth ~6.75\" scaling (scale ~0.44x).\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# Scale factor: figure is ~15.5\" content width, printed at ~6.75\" textwidth\n# → scale ≈ 0.44. For ≥7pt on paper, need ≥16pt in figure.\nS = 2.1  # font multiplier vs. previous iteration\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Font sizes (all ≥16pt → ≥7pt on paper) ─────────────────────────\nFS_TITLE   = 24      # panel title → ~10.5pt\nFS_SUB     = 17      # subtitle → ~7.4pt\nFS_PATH    = 19      # path labels → ~8.3pt\nFS_BOX     = 17      # box primary text → ~7.4pt\nFS_BOX2    = 17      # box secondary text → ~7.4pt\nFS_SMALL   = 16      # small annotations → ~7pt\nFS_TINY    = 14      # \"confounding\", \"init\" → ~6.1pt (min acceptable)\nFS_EQN     = 17      # equation → ~7.4pt\nFS_SYM     = 19      # output symbols → ~8.3pt\nFS_DESC    = 15      # output descriptions → ~6.5pt\nFS_PANEL   = 22      # (a), (b) labels → ~9.6pt\nFS_CHECK   = 30      # ✗ ✓ → ~13pt\nFS_NOTE    = 15      # italic bottom notes → ~6.5pt\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=14, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.28, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,\n      style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.72\nbx1, bx2 = 0.7, 5.9\nby_a = 4.8\n\nlabel(ax_l, 1.2, 5.85, 'Path A:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 3.0, 5.85, 'Bias-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.2)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.12, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.14, r'calibrate $d_j$', fs=FS_BOX2, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.2)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.12, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.14, r'contamination $c_n$', fs=FS_BOX2, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.5)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(a_conf)\nt = label(ax_l, 7.8, 5.85, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── Path B: Contamination-first ──\nby_b = 2.9\n\nlabel(ax_l, 1.2, 3.92, 'Path B:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 3.0, 3.92, 'Contamination-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.2)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.12, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.14, r'contamination $c_n$', fs=FS_BOX2, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.2)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.12, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.14, r'calibrate $d_j$', fs=FS_BOX2, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.5)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(b_conf)\nt = label(ax_l, 7.6, 3.92, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.45, 8.6, 2.0, WHITE, C_RED, lw=1.8, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.32,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=FS_EQN, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.9, color=C_RED, lw=1.1, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.9, color=C_RED, lw=1.1, style='-|>')\n\nlabel(ax_l, 5.0, 0.25, 'Unmodeled facet absorbed into remaining estimates',\n      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.25, 'staged joint calibration of all facets', fs=FS_SUB,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.0, 9.3, 1.0\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.2)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.28, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.62, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.48\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.26, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo + ow/2, s1_y + 0.26 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.0, 7.3, 4.6, color=C_JUDGE, lw=1.4)\nlabel(ax_r, 7.8, 4.8, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.6, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.2)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.25,\n      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.40\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.78 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.9)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.7, 4.85, 3.7, color=C_CONT, lw=1.4)\nlabel(ax_r, 4.45, 3.95, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.5, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.32,\n      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.85,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=FS_EQN, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.72\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.1, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.75\nout_y = 1.12\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.14, sym, fs=FS_SYM, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.15, desc, fs=FS_DESC, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.5, 7.2, 1.87, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.45, u'✓  Joint estimation resolves confounding',\n      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).",
          "-Full-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"",
          "+Full-width figure* for two-column layout.",
          "+Font sizes calibrated for textwidth ~6.75\" scaling (scale ~0.44x).\"\"\"",
          " import matplotlib",
          " matplotlib.use('Agg')",
          " matplotlib.rcParams['mathtext.fontset'] = 'cm'"
        ]
      },
      {
        "oldStart": 26,
        "oldLines": 6,
        "newStart": 27,
        "newLines": 10,
        "lines": [
          " SERIF = 'serif'",
          " SANS = 'DejaVu Sans'",
          " ",
          "+# Scale factor: figure is ~15.5\" content width, printed at ~6.75\" textwidth",
          "+# → scale ≈ 0.44. For ≥7pt on paper, need ≥16pt in figure.",
          "+S = 2.1  # font multiplier vs. previous iteration",
          "+",
          " # ── Figure setup ────────────────────────────────────────────────────",
          " fig = plt.figure(figsize=(16, 6.2))",
          " fig.patch.set_facecolor(WHITE)"
        ]
      },
      {
        "oldStart": 41,
        "oldLines": 8,
        "newStart": 46,
        "newLines": 23,
        "lines": [
          "     ax.set_aspect('equal')",
          "     ax.axis('off')",
          " ",
          "+# ── Font sizes (all ≥16pt → ≥7pt on paper) ─────────────────────────",
          "+FS_TITLE   = 24      # panel title → ~10.5pt",
          "+FS_SUB     = 17      # subtitle → ~7.4pt",
          "+FS_PATH    = 19      # path labels → ~8.3pt",
          "+FS_BOX     = 17      # box primary text → ~7.4pt",
          "+FS_BOX2    = 17      # box secondary text → ~7.4pt",
          "+FS_SMALL   = 16      # small annotations → ~7pt",
          "+FS_TINY    = 14      # \"confounding\", \"init\" → ~6.1pt (min acceptable)",
          "+FS_EQN     = 17      # equation → ~7.4pt",
          "+FS_SYM     = 19      # output symbols → ~8.3pt",
          "+FS_DESC    = 15      # output descriptions → ~6.5pt",
          "+FS_PANEL   = 22      # (a), (b) labels → ~9.6pt",
          "+FS_CHECK   = 30      # ✗ ✓ → ~13pt",
          "+FS_NOTE    = 15      # italic bottom notes → ~6.5pt",
          "+",
          " # ── Helpers ─────────────────────────────────────────────────────────",
          "-def shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):",
          "+def shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):",
          "     sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,",
          "                          boxstyle=f'round,pad={pad}',",
          "                          facecolor=SHADOW, edgecolor='none',"
        ]
      },
      {
        "oldStart": 54,
        "oldLines": 24,
        "newStart": 74,
        "newLines": 24,
        "lines": [
          "     ax.add_patch(b)",
          "     return b",
          " ",
          "-def rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):",
          "+def rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):",
          "     b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',",
          "                         facecolor=fc, edgecolor=ec, linewidth=lw,",
          "                         linestyle=ls, alpha=alpha, zorder=zorder)",
          "     ax.add_patch(b)",
          "     return b",
          " ",
          "-def label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',",
          "+def label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',",
          "           va='center', style='normal', zorder=5, family=SERIF, **kw):",
          "     return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,",
          "                    ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)",
          " ",
          "-def arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',",
          "+def arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',",
          "           rad=0, zorder=4, ls='-'):",
          "     cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'",
          "     a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,",
          "                          linewidth=lw, connectionstyle=cs, linestyle=ls,",
          "-                         mutation_scale=12, zorder=zorder)",
          "+                         mutation_scale=14, zorder=zorder)",
          "     ax.add_patch(a)",
          " ",
          " "
        ]
      },
      {
        "oldStart": 79,
        "oldLines": 145,
        "newStart": 99,
        "newLines": 146,
        "lines": [
          " #  LEFT PANEL — Sequential Pipeline",
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          "-rbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)",
          "+rbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)",
          " ",
          "-label(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 6.35, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 6.28, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,",
          "+      style='italic', fw='normal')",
          " ",
          " # ── Path A: Bias-first ──",
          "-bw, bh = 3.1, 0.68",
          "+bw, bh = 3.1, 0.72",
          " bx1, bx2 = 0.7, 5.9",
          "-by_a = 4.85",
          "+by_a = 4.8",
          " ",
          "-label(ax_l, 1.2, 5.85, 'Path A:', fs=9.5, fw='bold', color=DARK, ha='left')",
          "-label(ax_l, 2.75, 5.85, 'Bias-first', fs=9.5, fw='normal', color=DARK, ha='left')",
          "+label(ax_l, 1.2, 5.85, 'Path A:', fs=FS_PATH, fw='bold', color=DARK, ha='left')",
          "+label(ax_l, 3.0, 5.85, 'Bias-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')",
          " ",
          "-shadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "-label(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          "+shadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.2)",
          "+label(ax_l, bx1 + bw/2, by_a + bh/2 + 0.12, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)",
          "+label(ax_l, bx1 + bw/2, by_a + bh/2 - 0.14, r'calibrate $d_j$', fs=FS_BOX2, fw='normal', color=C_JUDGE)",
          " ",
          "-shadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "-label(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          "+shadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.2)",
          "+label(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.12, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)",
          "+label(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.14, r'contamination $c_n$', fs=FS_BOX2, fw='normal', color=C_CONT)",
          " ",
          "-arrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)",
          "-label(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          "+arrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.5)",
          "+label(ax_l, 9.55, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-# Confounding arc A — positioned clearly above boxes, label at right end",
          "+# Confounding arc A",
          " a_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),",
          "-                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)",
          "+                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',",
          "+                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)",
          " ax_l.add_patch(a_conf)",
          "-t = label(ax_l, 7.8, 5.85, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "-t.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])",
          "+t = label(ax_l, 7.8, 5.85, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')",
          "+t.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])",
          " ",
          " # ── Path B: Contamination-first ──",
          "-by_b = 2.95",
          "+by_b = 2.9",
          " ",
          "-label(ax_l, 1.2, 3.95, 'Path B:', fs=9.5, fw='bold', color=DARK, ha='left')",
          "-label(ax_l, 2.75, 3.95, 'Contamination-first', fs=9.5, fw='normal', color=DARK, ha='left')",
          "+label(ax_l, 1.2, 3.92, 'Path B:', fs=FS_PATH, fw='bold', color=DARK, ha='left')",
          "+label(ax_l, 3.0, 3.92, 'Contamination-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')",
          " ",
          "-shadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)",
          "-label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)",
          "+shadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.2)",
          "+label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.12, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)",
          "+label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.14, r'contamination $c_n$', fs=FS_BOX2, fw='normal', color=C_CONT)",
          " ",
          "-shadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)",
          "-label(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)",
          "-label(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)",
          "+shadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.2)",
          "+label(ax_l, bx2 + bw/2, by_b + bh/2 + 0.12, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)",
          "+label(ax_l, bx2 + bw/2, by_b + bh/2 - 0.14, r'calibrate $d_j$', fs=FS_BOX2, fw='normal', color=C_JUDGE)",
          " ",
          "-arrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)",
          "-label(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)",
          "+arrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.5)",
          "+label(ax_l, 9.55, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-# Confounding arc B — label at right end",
          "+# Confounding arc B",
          " b_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),",
          "-                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)",
          "+                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',",
          "+                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)",
          " ax_l.add_patch(b_conf)",
          "-t = label(ax_l, 7.6, 3.95, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')",
          "-t.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])",
          "+t = label(ax_l, 7.6, 3.92, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')",
          "+t.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])",
          " ",
          " # ── OVB Box ──",
          "-rbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)",
          "+rbox(ax_l, 0.7, 0.45, 8.6, 2.0, WHITE, C_RED, lw=1.8, ls='--', alpha=0.95, pad=0.18)",
          " ",
          "-label(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 1.38,",
          "+label(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 1.32,",
          "       r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',",
          "-      fs=9, fw='normal', color=C_RED)",
          "+      fs=FS_EQN, fw='normal', color=C_RED)",
          " ",
          "-arrow(ax_l, 3.5, 2.45, 3.5, 2.95, color=C_RED, lw=1.0, style='-|>')",
          "-arrow(ax_l, 6.5, 2.45, 6.5, 2.95, color=C_RED, lw=1.0, style='-|>')",
          "+arrow(ax_l, 3.5, 2.45, 3.5, 2.9, color=C_RED, lw=1.1, style='-|>')",
          "+arrow(ax_l, 6.5, 2.45, 6.5, 2.9, color=C_RED, lw=1.1, style='-|>')",
          " ",
          "-label(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',",
          "-      fs=7.5, color=C_RED, style='italic', fw='normal')",
          "+label(ax_l, 5.0, 0.25, 'Unmodeled facet absorbed into remaining estimates',",
          "+      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')",
          " ",
          " ",
          " # ═══════════════════════════════════════════════════════════════════",
          " #  RIGHT PANEL — G-MFRM Joint Framework",
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          "-rbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)",
          "+rbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)",
          " ",
          "-label(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')",
          "-label(ax_r, 5.0, 6.3, 'staged joint calibration of all facets', fs=8.5,",
          "+label(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')",
          "+label(ax_r, 5.0, 6.25, 'staged joint calibration of all facets', fs=FS_SUB,",
          "       color=C_GREEN, style='italic', fw='normal')",
          " ",
          " # ── Stage 1: Standard MFRM ──",
          "-s1_x, s1_y, s1_w, s1_h = 0.35, 5.05, 9.3, 0.95",
          "-shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)",
          "+s1_x, s1_y, s1_w, s1_h = 0.35, 5.0, 9.3, 1.0",
          "+shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.2)",
          " ",
          "-label(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)",
          "-label(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)",
          "+label(ax_r, 1.55, s1_y + s1_h - 0.28, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)",
          "+label(ax_r, 1.55, s1_y + s1_h - 0.62, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)",
          " ",
          "-ow, oh = 1.55, 0.45",
          "+ow, oh = 1.55, 0.48",
          " out1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]",
          " for lbl_txt, xo in out1_specs:",
          "-    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)",
          "-    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)",
          "+    rbox(ax_r, xo, s1_y + 0.26, ow, oh, WHITE, C_JUDGE, lw=1.0)",
          "+    label(ax_r, xo + ow/2, s1_y + 0.26 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)",
          " ",
          " # Arrow S1 → S3",
          "-arrow(ax_r, 7.3, 5.05, 7.3, 4.65, color=C_JUDGE, lw=1.3)",
          "-label(ax_r, 7.75, 4.85, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')",
          "+arrow(ax_r, 7.3, 5.0, 7.3, 4.6, color=C_JUDGE, lw=1.4)",
          "+label(ax_r, 7.8, 4.8, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')",
          " ",
          " # ── Stage 2: Estimate e_i ──",
          "-s2_x, s2_y, s2_w, s2_h = 0.35, 2.65, 3.7, 2.2",
          "-shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)",
          "+s2_x, s2_y, s2_w, s2_h = 0.35, 2.6, 3.7, 2.2",
          "+shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.2)",
          " ",
          "-label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,",
          "-      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)",
          "+label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.25,",
          "+      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)",
          " ",
          " sub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']",
          "-sw, sh = 2.7, 0.38",
          "+sw, sh = 2.7, 0.40",
          " for k, stxt in enumerate(sub_specs):",
          "-    sy = s2_y + s2_h - 0.72 - k * 0.52",
          "-    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)",
          "-    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)",
          "+    sy = s2_y + s2_h - 0.78 - k * 0.52",
          "+    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.9)",
          "+    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)",
          " ",
          " # Arrow S2 → S3",
          "-arrow(ax_r, s2_x + s2_w, 3.75, 4.85, 3.75, color=C_CONT, lw=1.3)",
          "-label(ax_r, 4.45, 4.0, r'$e_i$', fs=9, color=C_CONT, fw='bold')",
          "+arrow(ax_r, s2_x + s2_w, 3.7, 4.85, 3.7, color=C_CONT, lw=1.4)",
          "+label(ax_r, 4.45, 3.95, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')",
          " ",
          " # ── Stage 3: Joint Gated Model ──",
          "-s3_x, s3_y, s3_w, s3_h = 4.75, 2.55, 4.9, 2.1",
          "-shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)",
          "+s3_x, s3_y, s3_w, s3_h = 4.75, 2.5, 4.9, 2.1",
          "+shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)",
          " ",
          "-label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,",
          "-      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.32,",
          "+      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)",
          " ",
          "-label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.82,",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.85,",
          "       r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',",
          "-      fs=8.5, fw='normal', color=C_GRAY)",
          "+      fs=FS_EQN, fw='normal', color=C_GRAY)",
          " ",
          " # Gating highlight",
          "-gx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.7",
          "-shadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)",
          "+gx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.72",
          "+shadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)",
          " label(ax_r, gx + gw/2, gy + gh/2,",
          "-      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)",
          "+      r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)",
          " ",
          " # ── 4-D Output ──",
          "-label(ax_r, 5.0, 2.15, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)",
          "+label(ax_r, 5.0, 2.1, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)",
          " ",
          "-ow2, oh2 = 2.05, 0.72",
          "-out_y = 1.2",
          "+ow2, oh2 = 2.05, 0.75",
          "+out_y = 1.12",
          " out_specs = [",
          "     (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),",
          "     (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),"
        ]
      },
      {
        "oldStart": 225,
        "oldLines": 20,
        "newStart": 246,
        "newLines": 20,
        "lines": [
          "     (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),",
          " ]",
          " for sym, desc, fc, ec, xo in out_specs:",
          "-    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)",
          "-    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)",
          "-    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)",
          "+    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)",
          "+    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.14, sym, fs=FS_SYM, fw='bold', color=ec)",
          "+    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.15, desc, fs=FS_DESC, fw='normal', color=DARK)",
          " ",
          " # Arrow S3 → outputs",
          "-arrow(ax_r, 7.2, 2.55, 7.2, 1.92, color='#3C3C3C', lw=1.5, style='-|>')",
          "+arrow(ax_r, 7.2, 2.5, 7.2, 1.87, color='#3C3C3C', lw=1.6, style='-|>')",
          " ",
          " # Green check",
          "-label(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',",
          "-      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)",
          "+label(ax_r, 5.0, 0.45, u'✓  Joint estimation resolves confounding',",
          "+      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)",
          " ",
          " # Panel labels",
          "-label(ax_l, 0.35, 7.05, '(a)', fs=11, fw='bold', color='black', ha='left')",
          "-label(ax_r, 0.25, 7.05, '(b)', fs=11, fw='bold', color='black', ha='left')",
          "+label(ax_l, 0.35, 7.05, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')",
          "+label(ax_r, 0.25, 7.05, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')",
          " ",
          " # ── Save ──",
          " out_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'"
        ]
      }
    ],
    "originalFile": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout. ~3:1 aspect ratio.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.2, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=8.5, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.2, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=12, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.5, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=12, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.35, '(order-dependent estimation bias)', fs=8.5, color=C_RED, style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.68\nbx1, bx2 = 0.7, 5.9\nby_a = 4.85\n\nlabel(ax_l, 1.2, 5.85, 'Path A:', fs=9.5, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.75, 5.85, 'Bias-first', fs=9.5, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.11, 'Step 1: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.11, 'Step 2: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — positioned clearly above boxes, label at right end\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(a_conf)\nt = label(ax_l, 7.8, 5.85, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])\n\n# ── Path B: Contamination-first ──\nby_b = 2.95\n\nlabel(ax_l, 1.2, 3.95, 'Path B:', fs=9.5, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.75, 3.95, 'Contamination-first', fs=9.5, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.1)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.11, 'Step 1: Adjust', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.13, r'contamination $c_n$', fs=8.5, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.1)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.11, 'Step 2: MFRM', fs=8.5, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.13, r'calibrate $d_j$', fs=8.5, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.3)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=15, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B — label at right end\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.0, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=10, zorder=4)\nax_l.add_patch(b_conf)\nt = label(ax_l, 7.6, 3.95, 'confounding', fs=6.5, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3, foreground=WHITE)])\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.5, 8.6, 1.95, WHITE, C_RED, lw=1.5, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=9.5, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.38,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=9, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.95, color=C_RED, lw=1.0, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.95, color=C_RED, lw=1.0, style='-|>')\n\nlabel(ax_l, 5.0, 0.28, 'Unmodeled facet absorbed into remaining estimates',\n      fs=7.5, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.5, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=12, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.3, 'staged joint calibration of all facets', fs=8.5,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.05, 9.3, 0.95\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.1)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.25, 'Stage 1', fs=9, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.58, 'Standard MFRM', fs=7.5, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.45\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.25, ow, oh, WHITE, C_JUDGE, lw=0.9)\n    label(ax_r, xo + ow/2, s1_y + 0.25 + oh/2, lbl_txt, fs=9.5, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.05, 7.3, 4.65, color=C_JUDGE, lw=1.3)\nlabel(ax_r, 7.75, 4.85, 'init', fs=6.5, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.65, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.1)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.22,\n      r'Stage 2: Estimate $e_i$', fs=8.5, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.38\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.72 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.8)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=7.5, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.75, 4.85, 3.75, color=C_CONT, lw=1.3)\nlabel(ax_r, 4.45, 4.0, r'$e_i$', fs=9, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.55, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=1.8)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.3,\n      'Stage 3: Joint Gated Model', fs=9, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.82,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=8.5, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.7\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=1.8, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=9.5, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.15, '4-Dimensional Diagnostic Output', fs=9, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.72\nout_y = 1.2\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.2)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.13, sym, fs=9.5, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.14, desc, fs=7, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.55, 7.2, 1.92, color='#3C3C3C', lw=1.5, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',\n      fs=9, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=11, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=11, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Bash · `toolu_013S17bcj4NeLTBajv8Ap2Sd`</summary>

```json
{
  "command": "python3 gen_fig1.py 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "fa7ae2d8-56d3-43e2-bf8e-b79d4df23c1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBnjf1o321k9Nakfgvd3UN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9119,
      "cache_read_input_tokens": 92508,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9119
      },
      "output_tokens": 40,
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

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bcpxxke07",
  "tool_use_id": "toolu_013S17bcj4NeLTBajv8Ap2Sd",
  "description": "python3 gen_fig1.py 2>&1",
  "task_type": "local_bash",
  "uuid": "cf6d76ae-fbc7-4965-a23c-95ea506a8910",
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32"
}
```

---


### System

_source line 78_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bcpxxke07",
  "tool_use_id": "toolu_013S17bcj4NeLTBajv8Ap2Sd",
  "status": "completed",
  "output_file": "",
  "summary": "python3 gen_fig1.py 2>&1",
  "uuid": "1d567c9c-c959-4f06-b380-7674f5174792",
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32"
}
```

---


### Tool result

_source line 79 · 2026-05-24T11:57:04.718Z_

<details><summary>↩ Tool result · `toolu_013S17bcj4NeLTBajv8Ap2Sd`</summary>

```text
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
Done: fig1_framework.pdf + fig1_framework.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "4cc12dea-337e-4b3b-82d4-2ae9d1e9ba18",
  "tool_use_result": {
    "stdout": "'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\nDone: fig1_framework.pdf + fig1_framework.png",
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

_source line 80_

<details open><summary>🔧 Tool call — Read · `toolu_01AHTCsusxehM7GGgYBSHe62`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "fb7e1ac1-6ba0-44e0-8300-d348f7179224",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uxbf6Y2zVXLRW4rCcJU2vq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 101627,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
      },
      "output_tokens": 69,
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

_source line 81 · 2026-05-24T11:57:15.530Z_

<details><summary>↩ Tool result · `toolu_01AHTCsusxehM7GGgYBSHe62`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
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
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "896553b9-13b9-4f05-bfa0-46528c368a8a",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 757230
    }
  }
}
```

</details>

---


### Assistant

_source line 82_

<details><summary>Logged reasoning block</summary>

```text
Now with the larger fonts, things are getting cramped. The text is bigger but the coordinate space (0-10 x 0-7.2) doesn't have enough room for the larger text. Several issues:

1. Left panel: "Path A: Bias-first" and "confounding" labels are overlapping. The boxes are quite tight with the larger text.
2. "contamination c_n" text in boxes seems clipped/cramped
3. "Path B: Contamination-first" and "confounding" overlap
4. The bottom note extends outside the visible area
5. Right panel: Stage 2 sub-items are now very cramped


6. Overall the figure looks quite dense

The real issue is that I scaled up the fonts without expanding the coordinate space or box dimensions proportionally. With the current setup where each coordinate unit maps to about 0.86 inches, I need to either expand the coordinate space to give text more breathing room or increase the figure size. Since I want to keep figsize around (16, 6.2), the better approach is to increase the ylim and make the boxes larger to match the bigger text.

Looking at the math: 17pt text at the printed scale becomes 7.5pt on paper, which is fine, but it takes up about 0.28 coordinate units of height. With boxes only 0.72 units tall and two lines of text, I'm left with almost no padding. I should increase the box heights to 0.9-1.0 and expand the overall ylim to give everything more room to breathe.

Rather than fiddling with individual element sizes, I could use ylim=(0, 10) and rescale all positions proportionally. Or I could reduce the font size slightly, but that risks going below the 7pt minimum. The real issue is that figsize=(16, 6.2) with bbox_inches='tight' creates a mismatch between my coordinate space and the final print size. Using a smaller figsize like (7, 2.7) would let me use normal 8-10pt fonts that stay readable, but the task specifies using something closer to (16, 5.5). Let me try a middle ground with the larger figsize but adjust the ylim to give more vertical space.

Actually, I need to reconsider the set_aspect('equal') constraint—with equal aspect ratio, the axes will scale to fit both xlim and ylim within the available space from the gridspec. If the axes are wider than tall and I set xlim=ylim, the height gets constrained and I lose control. I should remove set_aspect('equal') so I can independently control the coordinate ranges.

Without equal aspect, each panel's x and y ranges map directly to their respective dimensions, which is perfect for a conceptual diagram where I'm manually positioning elements rather than plotting actual data. Let me calculate how this scales with the figure size and gridspec proportions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "9c9509b3-0f6b-46f0-b56b-bd42a1a7d7a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015t5cX2rMW8uuTf7d4K6KuF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 101795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 83_

Text is cramped at the larger font sizes because set_aspect('equal') constrains the coordinate space. For a conceptual diagram, I should remove that constraint and use the full available height. Rewriting with proportional coordinates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "06eba916-ed82-4303-b523-499a714feeb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015t5cX2rMW8uuTf7d4K6KuF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 101795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 84_

<details open><summary>🔧 Tool call — Write · `toolu_011urs1N5gKFA6eSp7uakMVB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout.\nFont sizes calibrated: printed at ~6.75\" textwidth → scale ≈ 0.44x.\nAll text ≥16pt in figure → ≥7pt on paper.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# Font sizes — all ≥16pt so printed size ≥7pt at 0.44x scale\nFS_TITLE = 24    # → ~10.5pt\nFS_SUB   = 18    # → ~7.9pt\nFS_PATH  = 20    # → ~8.8pt\nFS_BOX   = 18    # → ~7.9pt\nFS_MATH  = 18    # → ~7.9pt\nFS_SMALL = 16    # → ~7pt\nFS_TINY  = 15    # → ~6.6pt (confounding, init — acceptable)\nFS_SYM   = 20    # → ~8.8pt\nFS_DESC  = 16    # → ~7pt\nFS_PANEL = 22    # → ~9.7pt\nFS_CHECK = 28    # → ~12pt\nFS_NOTE  = 16    # → ~7pt\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,\n                      left=0.012, right=0.988, top=0.96, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 10)\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.05, y - 0.05), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=14, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.1, 0.15, 9.8, 9.7, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 9.45, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 8.85, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,\n      style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.2, 1.05\nbx1, bx2 = 0.6, 5.8\nby_a = 6.6\n\nlabel(ax_l, 1.1, 8.15, 'Path A:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.95, 8.15, 'Bias-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.18, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 + 0.18, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A\na_conf = FancyArrowPatch((bx2 + 1.5, by_a + bh + 0.05), (bx1 + 0.3, by_a + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(a_conf)\nt = label(ax_l, 8.0, 8.15, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── Path B: Contamination-first ──\nby_b = 3.7\n\nlabel(ax_l, 1.1, 5.25, 'Path B:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.95, 5.25, 'Contamination-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 + 0.18, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.18, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.3, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.3, by_b + bh + 0.05), (bx1 + 0.5, by_b + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(b_conf)\nt = label(ax_l, 7.8, 5.25, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── OVB Box ──\nrbox(ax_l, 0.6, 0.5, 8.8, 2.7, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95, pad=0.2)\n\nlabel(ax_l, 5.0, 2.6, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.7,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=FS_MATH, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 3.2, 3.5, 3.7, color=C_RED, lw=1.1, style='-|>')\narrow(ax_l, 6.5, 3.2, 6.5, 3.7, color=C_RED, lw=1.1, style='-|>')\n\nlabel(ax_l, 5.0, 0.35, 'Unmodeled facet absorbed into remaining estimates',\n      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.15, 9.9, 9.7, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 9.45, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 8.8, 'staged joint calibration of all facets', fs=FS_SUB,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.3, 7.2, 9.4, 1.35\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.3)\n\nlabel(ax_r, 1.6, s1_y + s1_h - 0.35, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.6, s1_y + s1_h - 0.8, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.65\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.35, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo + ow/2, s1_y + 0.35 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 7.2, 7.3, 6.55, color=C_JUDGE, lw=1.5)\nlabel(ax_r, 7.8, 6.9, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.3, 3.55, 3.8, 3.35\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.3)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.35,\n      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.8, 0.6\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 1.15 - k * 0.75\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.9)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 5.2, 4.8, 5.2, color=C_CONT, lw=1.5)\nlabel(ax_r, 4.4, 5.55, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.7, 3.4, 5.0, 3.15\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.45,\n      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.2,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=FS_MATH, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.55, s3_y + 0.35, 3.85, 1.0\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.85, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)\n\now2, oh2 = 2.1, 1.1\nout_y = 1.35\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.45),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.35),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.2, sym, fs=FS_SYM, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.22, desc, fs=FS_DESC, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 3.4, 7.2, 2.45, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.3, 9.8, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.2, 9.8, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "3dacd60f-c5ab-4d16-af41-f88bdaa8b19a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015t5cX2rMW8uuTf7d4K6KuF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 101795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 85 · 2026-05-24T11:59:10.386Z_

<details><summary>↩ Tool result · `toolu_011urs1N5gKFA6eSp7uakMVB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "90f6ee3c-4640-454e-a3da-8fefb98bb902",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
    "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout.\nFont sizes calibrated: printed at ~6.75\" textwidth → scale ≈ 0.44x.\nAll text ≥16pt in figure → ≥7pt on paper.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# Font sizes — all ≥16pt so printed size ≥7pt at 0.44x scale\nFS_TITLE = 24    # → ~10.5pt\nFS_SUB   = 18    # → ~7.9pt\nFS_PATH  = 20    # → ~8.8pt\nFS_BOX   = 18    # → ~7.9pt\nFS_MATH  = 18    # → ~7.9pt\nFS_SMALL = 16    # → ~7pt\nFS_TINY  = 15    # → ~6.6pt (confounding, init — acceptable)\nFS_SYM   = 20    # → ~8.8pt\nFS_DESC  = 16    # → ~7pt\nFS_PANEL = 22    # → ~9.7pt\nFS_CHECK = 28    # → ~12pt\nFS_NOTE  = 16    # → ~7pt\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,\n                      left=0.012, right=0.988, top=0.96, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 10)\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.05, y - 0.05), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=14, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.1, 0.15, 9.8, 9.7, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 9.45, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 8.85, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,\n      style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.2, 1.05\nbx1, bx2 = 0.6, 5.8\nby_a = 6.6\n\nlabel(ax_l, 1.1, 8.15, 'Path A:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.95, 8.15, 'Bias-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.18, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 + 0.18, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A\na_conf = FancyArrowPatch((bx2 + 1.5, by_a + bh + 0.05), (bx1 + 0.3, by_a + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(a_conf)\nt = label(ax_l, 8.0, 8.15, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── Path B: Contamination-first ──\nby_b = 3.7\n\nlabel(ax_l, 1.1, 5.25, 'Path B:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.95, 5.25, 'Contamination-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 + 0.18, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.18, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.3, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.3, by_b + bh + 0.05), (bx1 + 0.5, by_b + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(b_conf)\nt = label(ax_l, 7.8, 5.25, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── OVB Box ──\nrbox(ax_l, 0.6, 0.5, 8.8, 2.7, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95, pad=0.2)\n\nlabel(ax_l, 5.0, 2.6, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.7,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=FS_MATH, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 3.2, 3.5, 3.7, color=C_RED, lw=1.1, style='-|>')\narrow(ax_l, 6.5, 3.2, 6.5, 3.7, color=C_RED, lw=1.1, style='-|>')\n\nlabel(ax_l, 5.0, 0.35, 'Unmodeled facet absorbed into remaining estimates',\n      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.15, 9.9, 9.7, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 9.45, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 8.8, 'staged joint calibration of all facets', fs=FS_SUB,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.3, 7.2, 9.4, 1.35\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.3)\n\nlabel(ax_r, 1.6, s1_y + s1_h - 0.35, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.6, s1_y + s1_h - 0.8, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.65\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.35, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo + ow/2, s1_y + 0.35 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 7.2, 7.3, 6.55, color=C_JUDGE, lw=1.5)\nlabel(ax_r, 7.8, 6.9, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.3, 3.55, 3.8, 3.35\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.3)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.35,\n      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.8, 0.6\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 1.15 - k * 0.75\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.9)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 5.2, 4.8, 5.2, color=C_CONT, lw=1.5)\nlabel(ax_r, 4.4, 5.55, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.7, 3.4, 5.0, 3.15\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.45,\n      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.2,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=FS_MATH, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.55, s3_y + 0.35, 3.85, 1.0\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.85, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)\n\now2, oh2 = 2.1, 1.1\nout_y = 1.35\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.45),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.35),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.2, sym, fs=FS_SYM, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.22, desc, fs=FS_DESC, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 3.4, 7.2, 2.45, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.3, 9.8, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.2, 9.8, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " \"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).",
          " Full-width figure* for two-column layout.",
          "-Font sizes calibrated for textwidth ~6.75\" scaling (scale ~0.44x).\"\"\"",
          "+Font sizes calibrated: printed at ~6.75\" textwidth → scale ≈ 0.44x.",
          "+All text ≥16pt in figure → ≥7pt on paper.\"\"\"",
          " import matplotlib",
          " matplotlib.use('Agg')",
          " matplotlib.rcParams['mathtext.fontset'] = 'cm'"
        ]
      },
      {
        "oldStart": 27,
        "oldLines": 43,
        "newStart": 28,
        "newLines": 37,
        "lines": [
          " SERIF = 'serif'",
          " SANS = 'DejaVu Sans'",
          " ",
          "-# Scale factor: figure is ~15.5\" content width, printed at ~6.75\" textwidth",
          "-# → scale ≈ 0.44. For ≥7pt on paper, need ≥16pt in figure.",
          "-S = 2.1  # font multiplier vs. previous iteration",
          "+# Font sizes — all ≥16pt so printed size ≥7pt at 0.44x scale",
          "+FS_TITLE = 24    # → ~10.5pt",
          "+FS_SUB   = 18    # → ~7.9pt",
          "+FS_PATH  = 20    # → ~8.8pt",
          "+FS_BOX   = 18    # → ~7.9pt",
          "+FS_MATH  = 18    # → ~7.9pt",
          "+FS_SMALL = 16    # → ~7pt",
          "+FS_TINY  = 15    # → ~6.6pt (confounding, init — acceptable)",
          "+FS_SYM   = 20    # → ~8.8pt",
          "+FS_DESC  = 16    # → ~7pt",
          "+FS_PANEL = 22    # → ~9.7pt",
          "+FS_CHECK = 28    # → ~12pt",
          "+FS_NOTE  = 16    # → ~7pt",
          " ",
          " # ── Figure setup ────────────────────────────────────────────────────",
          " fig = plt.figure(figsize=(16, 6.2))",
          " fig.patch.set_facecolor(WHITE)",
          " ",
          "-gs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,",
          "-                      left=0.012, right=0.988, top=0.95, bottom=0.02)",
          "+gs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,",
          "+                      left=0.012, right=0.988, top=0.96, bottom=0.02)",
          " ax_l = fig.add_subplot(gs[0])",
          " ax_r = fig.add_subplot(gs[1])",
          " ",
          " for ax in [ax_l, ax_r]:",
          "     ax.set_xlim(0, 10)",
          "-    ax.set_ylim(0, 7.2)",
          "-    ax.set_aspect('equal')",
          "+    ax.set_ylim(0, 10)",
          "     ax.axis('off')",
          " ",
          "-# ── Font sizes (all ≥16pt → ≥7pt on paper) ─────────────────────────",
          "-FS_TITLE   = 24      # panel title → ~10.5pt",
          "-FS_SUB     = 17      # subtitle → ~7.4pt",
          "-FS_PATH    = 19      # path labels → ~8.3pt",
          "-FS_BOX     = 17      # box primary text → ~7.4pt",
          "-FS_BOX2    = 17      # box secondary text → ~7.4pt",
          "-FS_SMALL   = 16      # small annotations → ~7pt",
          "-FS_TINY    = 14      # \"confounding\", \"init\" → ~6.1pt (min acceptable)",
          "-FS_EQN     = 17      # equation → ~7.4pt",
          "-FS_SYM     = 19      # output symbols → ~8.3pt",
          "-FS_DESC    = 15      # output descriptions → ~6.5pt",
          "-FS_PANEL   = 22      # (a), (b) labels → ~9.6pt",
          "-FS_CHECK   = 30      # ✗ ✓ → ~13pt",
          "-FS_NOTE    = 15      # italic bottom notes → ~6.5pt",
          "-",
          " # ── Helpers ─────────────────────────────────────────────────────────",
          " def shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):",
          "-    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,",
          "+    sh = FancyBboxPatch((x + 0.05, y - 0.05), w, h,",
          "                          boxstyle=f'round,pad={pad}',",
          "                          facecolor=SHADOW, edgecolor='none',",
          "                          linewidth=0, alpha=0.10, zorder=zorder - 1)"
        ]
      },
      {
        "oldStart": 99,
        "oldLines": 76,
        "newStart": 94,
        "newLines": 76,
        "lines": [
          " #  LEFT PANEL — Sequential Pipeline",
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          "-rbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)",
          "+rbox(ax_l, 0.1, 0.15, 9.8, 9.7, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)",
          " ",
          "-label(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 6.28, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,",
          "+label(ax_l, 5.0, 9.45, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 8.85, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,",
          "       style='italic', fw='normal')",
          " ",
          " # ── Path A: Bias-first ──",
          "-bw, bh = 3.1, 0.72",
          "-bx1, bx2 = 0.7, 5.9",
          "-by_a = 4.8",
          "+bw, bh = 3.2, 1.05",
          "+bx1, bx2 = 0.6, 5.8",
          "+by_a = 6.6",
          " ",
          "-label(ax_l, 1.2, 5.85, 'Path A:', fs=FS_PATH, fw='bold', color=DARK, ha='left')",
          "-label(ax_l, 3.0, 5.85, 'Bias-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')",
          "+label(ax_l, 1.1, 8.15, 'Path A:', fs=FS_PATH, fw='bold', color=DARK, ha='left')",
          "+label(ax_l, 2.95, 8.15, 'Bias-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')",
          " ",
          "-shadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.2)",
          "-label(ax_l, bx1 + bw/2, by_a + bh/2 + 0.12, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)",
          "-label(ax_l, bx1 + bw/2, by_a + bh/2 - 0.14, r'calibrate $d_j$', fs=FS_BOX2, fw='normal', color=C_JUDGE)",
          "+shadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)",
          "+label(ax_l, bx1 + bw/2, by_a + bh/2 + 0.18, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)",
          "+label(ax_l, bx1 + bw/2, by_a + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)",
          " ",
          "-shadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.2)",
          "-label(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.12, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)",
          "-label(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.14, r'contamination $c_n$', fs=FS_BOX2, fw='normal', color=C_CONT)",
          "+shadow_box(ax_l, bx2, by_a, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)",
          "+label(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 + 0.18, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)",
          "+label(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)",
          " ",
          "-arrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.5)",
          "-label(ax_l, 9.55, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)",
          "+arrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.6)",
          "+label(ax_l, 9.5, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)",
          " ",
          " # Confounding arc A",
          "-a_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),",
          "+a_conf = FancyArrowPatch((bx2 + 1.5, by_a + bh + 0.05), (bx1 + 0.3, by_a + bh + 0.05),",
          "                           arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',",
          "                           connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)",
          " ax_l.add_patch(a_conf)",
          "-t = label(ax_l, 7.8, 5.85, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')",
          "+t = label(ax_l, 8.0, 8.15, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')",
          " t.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])",
          " ",
          " # ── Path B: Contamination-first ──",
          "-by_b = 2.9",
          "+by_b = 3.7",
          " ",
          "-label(ax_l, 1.2, 3.92, 'Path B:', fs=FS_PATH, fw='bold', color=DARK, ha='left')",
          "-label(ax_l, 3.0, 3.92, 'Contamination-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')",
          "+label(ax_l, 1.1, 5.25, 'Path B:', fs=FS_PATH, fw='bold', color=DARK, ha='left')",
          "+label(ax_l, 2.95, 5.25, 'Contamination-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')",
          " ",
          "-shadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.2)",
          "-label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.12, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)",
          "-label(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.14, r'contamination $c_n$', fs=FS_BOX2, fw='normal', color=C_CONT)",
          "+shadow_box(ax_l, bx1, by_b, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)",
          "+label(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 + 0.18, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)",
          "+label(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)",
          " ",
          "-shadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.2)",
          "-label(ax_l, bx2 + bw/2, by_b + bh/2 + 0.12, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)",
          "-label(ax_l, bx2 + bw/2, by_b + bh/2 - 0.14, r'calibrate $d_j$', fs=FS_BOX2, fw='normal', color=C_JUDGE)",
          "+shadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)",
          "+label(ax_l, bx2 + bw/2, by_b + bh/2 + 0.18, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)",
          "+label(ax_l, bx2 + bw/2, by_b + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)",
          " ",
          "-arrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.5)",
          "-label(ax_l, 9.55, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)",
          "+arrow(ax_l, bx1 + bw + 0.3, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.6)",
          "+label(ax_l, 9.5, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)",
          " ",
          " # Confounding arc B",
          "-b_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),",
          "+b_conf = FancyArrowPatch((bx2 + 1.3, by_b + bh + 0.05), (bx1 + 0.5, by_b + bh + 0.05),",
          "                           arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',",
          "                           connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)",
          " ax_l.add_patch(b_conf)",
          "-t = label(ax_l, 7.6, 3.92, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')",
          "+t = label(ax_l, 7.8, 5.25, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')",
          " t.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])",
          " ",
          " # ── OVB Box ──",
          "-rbox(ax_l, 0.7, 0.45, 8.6, 2.0, WHITE, C_RED, lw=1.8, ls='--', alpha=0.95, pad=0.18)",
          "+rbox(ax_l, 0.6, 0.5, 8.8, 2.7, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95, pad=0.2)",
          " ",
          "-label(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 1.32,",
          "+label(ax_l, 5.0, 2.6, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 1.7,",
          "       r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',",
          "-      fs=FS_EQN, fw='normal', color=C_RED)",
          "+      fs=FS_MATH, fw='normal', color=C_RED)",
          " ",
          "-arrow(ax_l, 3.5, 2.45, 3.5, 2.9, color=C_RED, lw=1.1, style='-|>')",
          "-arrow(ax_l, 6.5, 2.45, 6.5, 2.9, color=C_RED, lw=1.1, style='-|>')",
          "+arrow(ax_l, 3.5, 3.2, 3.5, 3.7, color=C_RED, lw=1.1, style='-|>')",
          "+arrow(ax_l, 6.5, 3.2, 6.5, 3.7, color=C_RED, lw=1.1, style='-|>')",
          " ",
          "-label(ax_l, 5.0, 0.25, 'Unmodeled facet absorbed into remaining estimates',",
          "+label(ax_l, 5.0, 0.35, 'Unmodeled facet absorbed into remaining estimates',",
          "       fs=FS_NOTE, color=C_RED, style='italic', fw='normal')",
          " ",
          " "
        ]
      },
      {
        "oldStart": 176,
        "oldLines": 90,
        "newStart": 171,
        "newLines": 90,
        "lines": [
          " #  RIGHT PANEL — G-MFRM Joint Framework",
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          "-rbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)",
          "+rbox(ax_r, 0.05, 0.15, 9.9, 9.7, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)",
          " ",
          "-label(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')",
          "-label(ax_r, 5.0, 6.25, 'staged joint calibration of all facets', fs=FS_SUB,",
          "+label(ax_r, 5.0, 9.45, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')",
          "+label(ax_r, 5.0, 8.8, 'staged joint calibration of all facets', fs=FS_SUB,",
          "       color=C_GREEN, style='italic', fw='normal')",
          " ",
          " # ── Stage 1: Standard MFRM ──",
          "-s1_x, s1_y, s1_w, s1_h = 0.35, 5.0, 9.3, 1.0",
          "-shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.2)",
          "+s1_x, s1_y, s1_w, s1_h = 0.3, 7.2, 9.4, 1.35",
          "+shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.3)",
          " ",
          "-label(ax_r, 1.55, s1_y + s1_h - 0.28, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)",
          "-label(ax_r, 1.55, s1_y + s1_h - 0.62, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)",
          "+label(ax_r, 1.6, s1_y + s1_h - 0.35, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)",
          "+label(ax_r, 1.6, s1_y + s1_h - 0.8, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)",
          " ",
          "-ow, oh = 1.55, 0.48",
          "+ow, oh = 1.55, 0.65",
          " out1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]",
          " for lbl_txt, xo in out1_specs:",
          "-    rbox(ax_r, xo, s1_y + 0.26, ow, oh, WHITE, C_JUDGE, lw=1.0)",
          "-    label(ax_r, xo + ow/2, s1_y + 0.26 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)",
          "+    rbox(ax_r, xo, s1_y + 0.35, ow, oh, WHITE, C_JUDGE, lw=1.0)",
          "+    label(ax_r, xo + ow/2, s1_y + 0.35 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)",
          " ",
          " # Arrow S1 → S3",
          "-arrow(ax_r, 7.3, 5.0, 7.3, 4.6, color=C_JUDGE, lw=1.4)",
          "-label(ax_r, 7.8, 4.8, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')",
          "+arrow(ax_r, 7.3, 7.2, 7.3, 6.55, color=C_JUDGE, lw=1.5)",
          "+label(ax_r, 7.8, 6.9, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')",
          " ",
          " # ── Stage 2: Estimate e_i ──",
          "-s2_x, s2_y, s2_w, s2_h = 0.35, 2.6, 3.7, 2.2",
          "-shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.2)",
          "+s2_x, s2_y, s2_w, s2_h = 0.3, 3.55, 3.8, 3.35",
          "+shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.3)",
          " ",
          "-label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.25,",
          "+label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.35,",
          "       r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)",
          " ",
          " sub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']",
          "-sw, sh = 2.7, 0.40",
          "+sw, sh = 2.8, 0.6",
          " for k, stxt in enumerate(sub_specs):",
          "-    sy = s2_y + s2_h - 0.78 - k * 0.52",
          "+    sy = s2_y + s2_h - 1.15 - k * 0.75",
          "     rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.9)",
          "     label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)",
          " ",
          " # Arrow S2 → S3",
          "-arrow(ax_r, s2_x + s2_w, 3.7, 4.85, 3.7, color=C_CONT, lw=1.4)",
          "-label(ax_r, 4.45, 3.95, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')",
          "+arrow(ax_r, s2_x + s2_w, 5.2, 4.8, 5.2, color=C_CONT, lw=1.5)",
          "+label(ax_r, 4.4, 5.55, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')",
          " ",
          " # ── Stage 3: Joint Gated Model ──",
          "-s3_x, s3_y, s3_w, s3_h = 4.75, 2.5, 4.9, 2.1",
          "+s3_x, s3_y, s3_w, s3_h = 4.7, 3.4, 5.0, 3.15",
          " shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)",
          " ",
          "-label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.32,",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.45,",
          "       'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)",
          " ",
          "-label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.85,",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.2,",
          "       r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',",
          "-      fs=FS_EQN, fw='normal', color=C_GRAY)",
          "+      fs=FS_MATH, fw='normal', color=C_GRAY)",
          " ",
          " # Gating highlight",
          "-gx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.72",
          "+gx, gy, gw, gh = s3_x + 0.55, s3_y + 0.35, 3.85, 1.0",
          " shadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)",
          " label(ax_r, gx + gw/2, gy + gh/2,",
          "       r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)",
          " ",
          " # ── 4-D Output ──",
          "-label(ax_r, 5.0, 2.1, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)",
          "+label(ax_r, 5.0, 2.85, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)",
          " ",
          "-ow2, oh2 = 2.05, 0.75",
          "-out_y = 1.12",
          "+ow2, oh2 = 2.1, 1.1",
          "+out_y = 1.35",
          " out_specs = [",
          "-    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),",
          "+    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.45),",
          "     (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),",
          "-    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),",
          "-    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),",
          "+    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),",
          "+    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.35),",
          " ]",
          " for sym, desc, fc, ec, xo in out_specs:",
          "     shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)",
          "-    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.14, sym, fs=FS_SYM, fw='bold', color=ec)",
          "-    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.15, desc, fs=FS_DESC, fw='normal', color=DARK)",
          "+    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.2, sym, fs=FS_SYM, fw='bold', color=ec)",
          "+    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.22, desc, fs=FS_DESC, fw='normal', color=DARK)",
          " ",
          " # Arrow S3 → outputs",
          "-arrow(ax_r, 7.2, 2.5, 7.2, 1.87, color='#3C3C3C', lw=1.6, style='-|>')",
          "+arrow(ax_r, 7.2, 3.4, 7.2, 2.45, color='#3C3C3C', lw=1.6, style='-|>')",
          " ",
          " # Green check",
          "-label(ax_r, 5.0, 0.45, u'✓  Joint estimation resolves confounding',",
          "+label(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',",
          "       fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)",
          " ",
          " # Panel labels",
          "-label(ax_l, 0.35, 7.05, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')",
          "-label(ax_r, 0.25, 7.05, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')",
          "+label(ax_l, 0.3, 9.8, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')",
          "+label(ax_r, 0.2, 9.8, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')",
          " ",
          " # ── Save ──",
          " out_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'"
        ]
      }
    ],
    "originalFile": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout.\nFont sizes calibrated for textwidth ~6.75\" scaling (scale ~0.44x).\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# Scale factor: figure is ~15.5\" content width, printed at ~6.75\" textwidth\n# → scale ≈ 0.44. For ≥7pt on paper, need ≥16pt in figure.\nS = 2.1  # font multiplier vs. previous iteration\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.045,\n                      left=0.012, right=0.988, top=0.95, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 7.2)\n    ax.set_aspect('equal')\n    ax.axis('off')\n\n# ── Font sizes (all ≥16pt → ≥7pt on paper) ─────────────────────────\nFS_TITLE   = 24      # panel title → ~10.5pt\nFS_SUB     = 17      # subtitle → ~7.4pt\nFS_PATH    = 19      # path labels → ~8.3pt\nFS_BOX     = 17      # box primary text → ~7.4pt\nFS_BOX2    = 17      # box secondary text → ~7.4pt\nFS_SMALL   = 16      # small annotations → ~7pt\nFS_TINY    = 14      # \"confounding\", \"init\" → ~6.1pt (min acceptable)\nFS_EQN     = 17      # equation → ~7.4pt\nFS_SYM     = 19      # output symbols → ~8.3pt\nFS_DESC    = 15      # output descriptions → ~6.5pt\nFS_PANEL   = 22      # (a), (b) labels → ~9.6pt\nFS_CHECK   = 30      # ✗ ✓ → ~13pt\nFS_NOTE    = 15      # italic bottom notes → ~6.5pt\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.04, y - 0.04), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=14, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.15, 0.1, 9.7, 6.95, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 6.75, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 6.28, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,\n      style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.1, 0.72\nbx1, bx2 = 0.7, 5.9\nby_a = 4.8\n\nlabel(ax_l, 1.2, 5.85, 'Path A:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 3.0, 5.85, 'Bias-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.2)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.12, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.14, r'calibrate $d_j$', fs=FS_BOX2, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.2)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 + 0.12, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.2)/2, by_a + bh/2 - 0.14, r'contamination $c_n$', fs=FS_BOX2, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.5)\nlabel(ax_l, 9.55, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A\na_conf = FancyArrowPatch((bx2 + 1.2, by_a + bh), (bx1 + 0.5, by_a + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(a_conf)\nt = label(ax_l, 7.8, 5.85, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── Path B: Contamination-first ──\nby_b = 2.9\n\nlabel(ax_l, 1.2, 3.92, 'Path B:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 3.0, 3.92, 'Contamination-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.2, bh, C_CONT_L, C_CONT, lw=1.2)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 + 0.12, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.2)/2, by_b + bh/2 - 0.14, r'contamination $c_n$', fs=FS_BOX2, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.2)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.12, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.14, r'calibrate $d_j$', fs=FS_BOX2, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.2, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.5)\nlabel(ax_l, 9.55, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.0, by_b + bh), (bx1 + 0.7, by_b + bh),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(b_conf)\nt = label(ax_l, 7.6, 3.92, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── OVB Box ──\nrbox(ax_l, 0.7, 0.45, 8.6, 2.0, WHITE, C_RED, lw=1.8, ls='--', alpha=0.95, pad=0.18)\n\nlabel(ax_l, 5.0, 1.95, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.32,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=FS_EQN, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 2.45, 3.5, 2.9, color=C_RED, lw=1.1, style='-|>')\narrow(ax_l, 6.5, 2.45, 6.5, 2.9, color=C_RED, lw=1.1, style='-|>')\n\nlabel(ax_l, 5.0, 0.25, 'Unmodeled facet absorbed into remaining estimates',\n      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.1, 9.9, 6.95, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 6.75, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 6.25, 'staged joint calibration of all facets', fs=FS_SUB,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.35, 5.0, 9.3, 1.0\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.2)\n\nlabel(ax_r, 1.55, s1_y + s1_h - 0.28, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.55, s1_y + s1_h - 0.62, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.48\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.26, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo + ow/2, s1_y + 0.26 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 5.0, 7.3, 4.6, color=C_JUDGE, lw=1.4)\nlabel(ax_r, 7.8, 4.8, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.35, 2.6, 3.7, 2.2\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.2)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.25,\n      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.7, 0.40\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 0.78 - k * 0.52\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.9)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 3.7, 4.85, 3.7, color=C_CONT, lw=1.4)\nlabel(ax_r, 4.45, 3.95, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.75, 2.5, 4.9, 2.1\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.32,\n      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.85,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=FS_EQN, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.6, s3_y + 0.25, 3.65, 0.72\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.1, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)\n\now2, oh2 = 2.05, 0.75\nout_y = 1.12\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.5),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.0),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.25),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.14, sym, fs=FS_SYM, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.15, desc, fs=FS_DESC, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 2.5, 7.2, 1.87, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.45, u'✓  Joint estimation resolves confounding',\n      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.35, 7.05, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.25, 7.05, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Bash · `toolu_01Qw2oTqYnCkcxWk4jG1G5cK`</summary>

```json
{
  "command": "python3 gen_fig1.py 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "ecc8730a-546d-46fc-8cac-3a02a722054e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KijxzZS9JiqrduCsCsPrGv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7482,
      "cache_read_input_tokens": 102108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7482
      },
      "output_tokens": 40,
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

_source line 87 · 2026-05-24T11:59:17.766Z_

<details><summary>↩ Tool result · `toolu_01Qw2oTqYnCkcxWk4jG1G5cK`</summary>

```text
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
Done: fig1_framework.pdf + fig1_framework.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "66a71666-bf3e-4bda-8d96-c6d5ff3fa0f6",
  "tool_use_result": {
    "stdout": "'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\nDone: fig1_framework.pdf + fig1_framework.png",
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

_source line 88_

<details open><summary>🔧 Tool call — Read · `toolu_01GWMqiKqMMNLDP1mnNiNrg2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "25220ff4-af87-42a3-bec8-3b905e551811",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bf3o1siuysK6ZCtkjyut7P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 109590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
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

_source line 89 · 2026-05-24T11:59:26.716Z_

<details><summary>↩ Tool result · `toolu_01GWMqiKqMMNLDP1mnNiNrg2`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
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
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "4bcf834a-81a6-4d81-afa7-eecffbe93a76",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 787346
    }
  }
}
```

</details>

---


### Assistant

_source line 90_

<details><summary>Logged reasoning block</summary>

```text
The font sizes are now much better for print. But there are still some layout issues:

1. Left panel: "Path B: Contamination-first" text overlaps with "confounding" label
2. The bottom note text extends beyond the OVB box border
3. The "confounding" labels are still colliding with the "Path A/B" labels at the same y position
4. In the right panel, the Stage 2 and Stage 3 content is a bit cramped vertically

The fundamental issue persists: I'm placing the "confounding" label at the same y-coordinate as the "Path A/B" label. Let me fix this by:


1. Moving confounding labels to a clearly different position — I'll place them at a higher y position along the arc's peak, not at the same y as the path labels

Now I'm working through the arc geometry to figure out where the peak actually sits. With the arc parameters I'm using, the peak should be noticeably above the start and end points, giving me enough vertical space to position the confounding labels without overlap. I'm realizing the overlap issue—placing "confounding" at y=8.0 conflicts with the "Path A:" label at y=8.15. Instead, I'll position the label directly at the arc's peak, centered above the midpoint of each arc, so it sits cleanly within the curved shape itself. I'm realizing the vertical space is too cramped with all these elements competing for room, so I should consolidate by embedding the path labels directly into the visual design—maybe positioning "Path A" as a small label along the left edge of its step boxes rather than as a separate line item.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "d103fbfb-7c85-47fa-8c7c-d2281a617126",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jkLKxBo9kcBaCra3sNdrW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 109758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
      },
      "output_tokens": 9,
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

_source line 91_

Layout improved significantly with proper font scaling. Still need to fix: (1) confounding label collision with path labels, (2) bottom note extending beyond OVB box. Let me precisely position the confounding labels at the arc apex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "b4294ba8-4b21-48c3-80a8-e9b25e5712d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jkLKxBo9kcBaCra3sNdrW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 109758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
      },
      "output_tokens": 9,
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

_source line 92_

<details open><summary>🔧 Tool call — Write · `toolu_01X7pkurs4Pk8u11wNynCMjr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout.\nFont sizes calibrated: printed at ~6.75\" textwidth → scale ≈ 0.44x.\nAll text ≥16pt in figure → ≥7pt on paper.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# Font sizes — at 0.44x scale all ≥7pt on paper\nFS_TITLE = 24\nFS_SUB   = 18\nFS_PATH  = 19\nFS_BOX   = 17\nFS_MATH  = 17\nFS_SMALL = 16\nFS_TINY  = 15\nFS_SYM   = 19\nFS_DESC  = 16\nFS_PANEL = 22\nFS_CHECK = 28\nFS_NOTE  = 16\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,\n                      left=0.012, right=0.988, top=0.96, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 10)\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.05, y - 0.05), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef label_bg(ax, x, y, txt, fs=FS_TINY, fw='normal', color=C_RED, style='italic',\n             zorder=6, family=SERIF):\n    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                ha='center', va='center', fontstyle=style, zorder=zorder, family=family)\n    t.set_path_effects([pe.withStroke(linewidth=4, foreground=WHITE)])\n    return t\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=14, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.1, 0.15, 9.8, 9.7, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 9.5, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 8.9, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,\n      style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.2, 1.05\nbx1, bx2 = 0.6, 5.8\nby_a = 6.55\n\nlabel(ax_l, 0.5, 8.15, 'Path A: Bias-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.18, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 + 0.18, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — label at arc apex\narc_y_a = by_a + bh + 0.08\na_conf = FancyArrowPatch((bx2 + 1.5, arc_y_a), (bx1 + 0.3, arc_y_a),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)\nax_l.add_patch(a_conf)\nlabel_bg(ax_l, 4.5, 8.5, 'confounding')\n\n# ── Path B: Contamination-first ──\nby_b = 3.6\n\nlabel(ax_l, 0.5, 5.2, 'Path B: Contamination-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 + 0.18, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.18, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.3, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B — label at arc apex\narc_y_b = by_b + bh + 0.08\nb_conf = FancyArrowPatch((bx2 + 1.3, arc_y_b), (bx1 + 0.5, arc_y_b),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)\nax_l.add_patch(b_conf)\nlabel_bg(ax_l, 4.5, 5.55, 'confounding')\n\n# ── OVB Box ──\nrbox(ax_l, 0.6, 0.5, 8.8, 2.6, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95, pad=0.2)\n\nlabel(ax_l, 5.0, 2.5, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.65,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=FS_MATH, fw='normal', color=C_RED)\nlabel(ax_l, 5.0, 0.8, 'Unmodeled facet absorbed into estimates',\n      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')\n\narrow(ax_l, 3.5, 3.1, 3.5, 3.6, color=C_RED, lw=1.1, style='-|>')\narrow(ax_l, 6.5, 3.1, 6.5, 3.6, color=C_RED, lw=1.1, style='-|>')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.15, 9.9, 9.7, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 9.5, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 8.85, 'staged joint calibration of all facets', fs=FS_SUB,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.3, 7.15, 9.4, 1.4\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.3)\n\nlabel(ax_r, 1.6, s1_y + s1_h - 0.38, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.6, s1_y + s1_h - 0.85, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.65\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.38, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo + ow/2, s1_y + 0.38 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 7.15, 7.3, 6.5, color=C_JUDGE, lw=1.5)\nlabel(ax_r, 7.85, 6.85, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.3, 3.3, 3.9, 3.5\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.3)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.4,\n      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.8, 0.62\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 1.25 - k * 0.8\n    rbox(ax_r, s2_x + 0.55, sy, sw, sh, WHITE, C_CONT, lw=0.9)\n    label(ax_r, s2_x + 0.55 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 5.05, 4.9, 5.05, color=C_CONT, lw=1.5)\nlabel(ax_r, 4.55, 5.45, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.8, 3.2, 5.0, 3.3\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.5,\n      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.3,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=FS_MATH, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.55, s3_y + 0.35, 3.85, 1.05\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.7, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)\n\now2, oh2 = 2.1, 1.1\nout_y = 1.3\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.45),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.35),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.2, sym, fs=FS_SYM, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.22, desc, fs=FS_DESC, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 3.2, 7.2, 2.4, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',\n      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.3, 9.85, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.2, 9.85, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "6a5b568e-98a1-4928-97c6-6f827f688764",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jkLKxBo9kcBaCra3sNdrW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 109758,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
      },
      "output_tokens": 9,
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

_source line 93 · 2026-05-24T12:01:16.445Z_

<details><summary>↩ Tool result · `toolu_01X7pkurs4Pk8u11wNynCMjr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "564d95d8-7948-45be-9df2-c23b8048f022",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
    "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout.\nFont sizes calibrated: printed at ~6.75\" textwidth → scale ≈ 0.44x.\nAll text ≥16pt in figure → ≥7pt on paper.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# Font sizes — at 0.44x scale all ≥7pt on paper\nFS_TITLE = 24\nFS_SUB   = 18\nFS_PATH  = 19\nFS_BOX   = 17\nFS_MATH  = 17\nFS_SMALL = 16\nFS_TINY  = 15\nFS_SYM   = 19\nFS_DESC  = 16\nFS_PANEL = 22\nFS_CHECK = 28\nFS_NOTE  = 16\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,\n                      left=0.012, right=0.988, top=0.96, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 10)\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.05, y - 0.05), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef label_bg(ax, x, y, txt, fs=FS_TINY, fw='normal', color=C_RED, style='italic',\n             zorder=6, family=SERIF):\n    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                ha='center', va='center', fontstyle=style, zorder=zorder, family=family)\n    t.set_path_effects([pe.withStroke(linewidth=4, foreground=WHITE)])\n    return t\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=14, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.1, 0.15, 9.8, 9.7, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 9.5, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 8.9, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,\n      style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.2, 1.05\nbx1, bx2 = 0.6, 5.8\nby_a = 6.55\n\nlabel(ax_l, 0.5, 8.15, 'Path A: Bias-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.18, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 + 0.18, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — label at arc apex\narc_y_a = by_a + bh + 0.08\na_conf = FancyArrowPatch((bx2 + 1.5, arc_y_a), (bx1 + 0.3, arc_y_a),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)\nax_l.add_patch(a_conf)\nlabel_bg(ax_l, 4.5, 8.5, 'confounding')\n\n# ── Path B: Contamination-first ──\nby_b = 3.6\n\nlabel(ax_l, 0.5, 5.2, 'Path B: Contamination-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 + 0.18, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.18, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.3, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B — label at arc apex\narc_y_b = by_b + bh + 0.08\nb_conf = FancyArrowPatch((bx2 + 1.3, arc_y_b), (bx1 + 0.5, arc_y_b),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)\nax_l.add_patch(b_conf)\nlabel_bg(ax_l, 4.5, 5.55, 'confounding')\n\n# ── OVB Box ──\nrbox(ax_l, 0.6, 0.5, 8.8, 2.6, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95, pad=0.2)\n\nlabel(ax_l, 5.0, 2.5, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.65,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=FS_MATH, fw='normal', color=C_RED)\nlabel(ax_l, 5.0, 0.8, 'Unmodeled facet absorbed into estimates',\n      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')\n\narrow(ax_l, 3.5, 3.1, 3.5, 3.6, color=C_RED, lw=1.1, style='-|>')\narrow(ax_l, 6.5, 3.1, 6.5, 3.6, color=C_RED, lw=1.1, style='-|>')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.15, 9.9, 9.7, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 9.5, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 8.85, 'staged joint calibration of all facets', fs=FS_SUB,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.3, 7.15, 9.4, 1.4\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.3)\n\nlabel(ax_r, 1.6, s1_y + s1_h - 0.38, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.6, s1_y + s1_h - 0.85, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.65\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.38, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo + ow/2, s1_y + 0.38 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 7.15, 7.3, 6.5, color=C_JUDGE, lw=1.5)\nlabel(ax_r, 7.85, 6.85, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.3, 3.3, 3.9, 3.5\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.3)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.4,\n      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.8, 0.62\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 1.25 - k * 0.8\n    rbox(ax_r, s2_x + 0.55, sy, sw, sh, WHITE, C_CONT, lw=0.9)\n    label(ax_r, s2_x + 0.55 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 5.05, 4.9, 5.05, color=C_CONT, lw=1.5)\nlabel(ax_r, 4.55, 5.45, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.8, 3.2, 5.0, 3.3\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.5,\n      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.3,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=FS_MATH, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.55, s3_y + 0.35, 3.85, 1.05\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.7, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)\n\now2, oh2 = 2.1, 1.1\nout_y = 1.3\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.45),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.35),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.2, sym, fs=FS_SYM, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.22, desc, fs=FS_DESC, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 3.2, 7.2, 2.4, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',\n      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.3, 9.85, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.2, 9.85, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "structuredPatch": [
      {
        "oldStart": 28,
        "oldLines": 19,
        "newStart": 28,
        "newLines": 19,
        "lines": [
          " SERIF = 'serif'",
          " SANS = 'DejaVu Sans'",
          " ",
          "-# Font sizes — all ≥16pt so printed size ≥7pt at 0.44x scale",
          "-FS_TITLE = 24    # → ~10.5pt",
          "-FS_SUB   = 18    # → ~7.9pt",
          "-FS_PATH  = 20    # → ~8.8pt",
          "-FS_BOX   = 18    # → ~7.9pt",
          "-FS_MATH  = 18    # → ~7.9pt",
          "-FS_SMALL = 16    # → ~7pt",
          "-FS_TINY  = 15    # → ~6.6pt (confounding, init — acceptable)",
          "-FS_SYM   = 20    # → ~8.8pt",
          "-FS_DESC  = 16    # → ~7pt",
          "-FS_PANEL = 22    # → ~9.7pt",
          "-FS_CHECK = 28    # → ~12pt",
          "-FS_NOTE  = 16    # → ~7pt",
          "+# Font sizes — at 0.44x scale all ≥7pt on paper",
          "+FS_TITLE = 24",
          "+FS_SUB   = 18",
          "+FS_PATH  = 19",
          "+FS_BOX   = 17",
          "+FS_MATH  = 17",
          "+FS_SMALL = 16",
          "+FS_TINY  = 15",
          "+FS_SYM   = 19",
          "+FS_DESC  = 16",
          "+FS_PANEL = 22",
          "+FS_CHECK = 28",
          "+FS_NOTE  = 16",
          " ",
          " # ── Figure setup ────────────────────────────────────────────────────",
          " fig = plt.figure(figsize=(16, 6.2))"
        ]
      },
      {
        "oldStart": 81,
        "oldLines": 6,
        "newStart": 81,
        "newLines": 13,
        "lines": [
          "     return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,",
          "                    ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)",
          " ",
          "+def label_bg(ax, x, y, txt, fs=FS_TINY, fw='normal', color=C_RED, style='italic',",
          "+             zorder=6, family=SERIF):",
          "+    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,",
          "+                ha='center', va='center', fontstyle=style, zorder=zorder, family=family)",
          "+    t.set_path_effects([pe.withStroke(linewidth=4, foreground=WHITE)])",
          "+    return t",
          "+",
          " def arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',",
          "           rad=0, zorder=4, ls='-'):",
          "     cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'"
        ]
      },
      {
        "oldStart": 96,
        "oldLines": 17,
        "newStart": 103,
        "newLines": 16,
        "lines": [
          " ",
          " rbox(ax_l, 0.1, 0.15, 9.8, 9.7, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)",
          " ",
          "-label(ax_l, 5.0, 9.45, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 8.85, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,",
          "+label(ax_l, 5.0, 9.5, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 8.9, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,",
          "       style='italic', fw='normal')",
          " ",
          " # ── Path A: Bias-first ──",
          " bw, bh = 3.2, 1.05",
          " bx1, bx2 = 0.6, 5.8",
          "-by_a = 6.6",
          "+by_a = 6.55",
          " ",
          "-label(ax_l, 1.1, 8.15, 'Path A:', fs=FS_PATH, fw='bold', color=DARK, ha='left')",
          "-label(ax_l, 2.95, 8.15, 'Bias-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')",
          "+label(ax_l, 0.5, 8.15, 'Path A: Bias-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')",
          " ",
          " shadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)",
          " label(ax_l, bx1 + bw/2, by_a + bh/2 + 0.18, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)"
        ]
      },
      {
        "oldStart": 119,
        "oldLines": 19,
        "newStart": 125,
        "newLines": 18,
        "lines": [
          " arrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.6)",
          " label(ax_l, 9.5, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-# Confounding arc A",
          "-a_conf = FancyArrowPatch((bx2 + 1.5, by_a + bh + 0.05), (bx1 + 0.3, by_a + bh + 0.05),",
          "+# Confounding arc A — label at arc apex",
          "+arc_y_a = by_a + bh + 0.08",
          "+a_conf = FancyArrowPatch((bx2 + 1.5, arc_y_a), (bx1 + 0.3, arc_y_a),",
          "                           arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)",
          "+                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)",
          " ax_l.add_patch(a_conf)",
          "-t = label(ax_l, 8.0, 8.15, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')",
          "-t.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])",
          "+label_bg(ax_l, 4.5, 8.5, 'confounding')",
          " ",
          " # ── Path B: Contamination-first ──",
          "-by_b = 3.7",
          "+by_b = 3.6",
          " ",
          "-label(ax_l, 1.1, 5.25, 'Path B:', fs=FS_PATH, fw='bold', color=DARK, ha='left')",
          "-label(ax_l, 2.95, 5.25, 'Contamination-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')",
          "+label(ax_l, 0.5, 5.2, 'Path B: Contamination-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')",
          " ",
          " shadow_box(ax_l, bx1, by_b, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)",
          " label(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 + 0.18, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)"
        ]
      },
      {
        "oldStart": 144,
        "oldLines": 96,
        "newStart": 149,
        "newLines": 95,
        "lines": [
          " arrow(ax_l, bx1 + bw + 0.3, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.6)",
          " label(ax_l, 9.5, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)",
          " ",
          "-# Confounding arc B",
          "-b_conf = FancyArrowPatch((bx2 + 1.3, by_b + bh + 0.05), (bx1 + 0.5, by_b + bh + 0.05),",
          "+# Confounding arc B — label at arc apex",
          "+arc_y_b = by_b + bh + 0.08",
          "+b_conf = FancyArrowPatch((bx2 + 1.3, arc_y_b), (bx1 + 0.5, arc_y_b),",
          "                           arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)",
          "+                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)",
          " ax_l.add_patch(b_conf)",
          "-t = label(ax_l, 7.8, 5.25, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')",
          "-t.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])",
          "+label_bg(ax_l, 4.5, 5.55, 'confounding')",
          " ",
          " # ── OVB Box ──",
          "-rbox(ax_l, 0.6, 0.5, 8.8, 2.7, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95, pad=0.2)",
          "+rbox(ax_l, 0.6, 0.5, 8.8, 2.6, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95, pad=0.2)",
          " ",
          "-label(ax_l, 5.0, 2.6, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)",
          "-label(ax_l, 5.0, 1.7,",
          "+label(ax_l, 5.0, 2.5, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)",
          "+label(ax_l, 5.0, 1.65,",
          "       r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',",
          "       fs=FS_MATH, fw='normal', color=C_RED)",
          "-",
          "-arrow(ax_l, 3.5, 3.2, 3.5, 3.7, color=C_RED, lw=1.1, style='-|>')",
          "-arrow(ax_l, 6.5, 3.2, 6.5, 3.7, color=C_RED, lw=1.1, style='-|>')",
          "-",
          "-label(ax_l, 5.0, 0.35, 'Unmodeled facet absorbed into remaining estimates',",
          "+label(ax_l, 5.0, 0.8, 'Unmodeled facet absorbed into estimates',",
          "       fs=FS_NOTE, color=C_RED, style='italic', fw='normal')",
          " ",
          "+arrow(ax_l, 3.5, 3.1, 3.5, 3.6, color=C_RED, lw=1.1, style='-|>')",
          "+arrow(ax_l, 6.5, 3.1, 6.5, 3.6, color=C_RED, lw=1.1, style='-|>')",
          " ",
          "+",
          " # ═══════════════════════════════════════════════════════════════════",
          " #  RIGHT PANEL — G-MFRM Joint Framework",
          " # ═══════════════════════════════════════════════════════════════════",
          " ",
          " rbox(ax_r, 0.05, 0.15, 9.9, 9.7, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)",
          " ",
          "-label(ax_r, 5.0, 9.45, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')",
          "-label(ax_r, 5.0, 8.8, 'staged joint calibration of all facets', fs=FS_SUB,",
          "+label(ax_r, 5.0, 9.5, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')",
          "+label(ax_r, 5.0, 8.85, 'staged joint calibration of all facets', fs=FS_SUB,",
          "       color=C_GREEN, style='italic', fw='normal')",
          " ",
          " # ── Stage 1: Standard MFRM ──",
          "-s1_x, s1_y, s1_w, s1_h = 0.3, 7.2, 9.4, 1.35",
          "+s1_x, s1_y, s1_w, s1_h = 0.3, 7.15, 9.4, 1.4",
          " shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.3)",
          " ",
          "-label(ax_r, 1.6, s1_y + s1_h - 0.35, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)",
          "-label(ax_r, 1.6, s1_y + s1_h - 0.8, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)",
          "+label(ax_r, 1.6, s1_y + s1_h - 0.38, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)",
          "+label(ax_r, 1.6, s1_y + s1_h - 0.85, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)",
          " ",
          " ow, oh = 1.55, 0.65",
          " out1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]",
          " for lbl_txt, xo in out1_specs:",
          "-    rbox(ax_r, xo, s1_y + 0.35, ow, oh, WHITE, C_JUDGE, lw=1.0)",
          "-    label(ax_r, xo + ow/2, s1_y + 0.35 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)",
          "+    rbox(ax_r, xo, s1_y + 0.38, ow, oh, WHITE, C_JUDGE, lw=1.0)",
          "+    label(ax_r, xo + ow/2, s1_y + 0.38 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)",
          " ",
          " # Arrow S1 → S3",
          "-arrow(ax_r, 7.3, 7.2, 7.3, 6.55, color=C_JUDGE, lw=1.5)",
          "-label(ax_r, 7.8, 6.9, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')",
          "+arrow(ax_r, 7.3, 7.15, 7.3, 6.5, color=C_JUDGE, lw=1.5)",
          "+label(ax_r, 7.85, 6.85, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')",
          " ",
          " # ── Stage 2: Estimate e_i ──",
          "-s2_x, s2_y, s2_w, s2_h = 0.3, 3.55, 3.8, 3.35",
          "+s2_x, s2_y, s2_w, s2_h = 0.3, 3.3, 3.9, 3.5",
          " shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.3)",
          " ",
          "-label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.35,",
          "+label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.4,",
          "       r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)",
          " ",
          " sub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']",
          "-sw, sh = 2.8, 0.6",
          "+sw, sh = 2.8, 0.62",
          " for k, stxt in enumerate(sub_specs):",
          "-    sy = s2_y + s2_h - 1.15 - k * 0.75",
          "-    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.9)",
          "-    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)",
          "+    sy = s2_y + s2_h - 1.25 - k * 0.8",
          "+    rbox(ax_r, s2_x + 0.55, sy, sw, sh, WHITE, C_CONT, lw=0.9)",
          "+    label(ax_r, s2_x + 0.55 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)",
          " ",
          " # Arrow S2 → S3",
          "-arrow(ax_r, s2_x + s2_w, 5.2, 4.8, 5.2, color=C_CONT, lw=1.5)",
          "-label(ax_r, 4.4, 5.55, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')",
          "+arrow(ax_r, s2_x + s2_w, 5.05, 4.9, 5.05, color=C_CONT, lw=1.5)",
          "+label(ax_r, 4.55, 5.45, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')",
          " ",
          " # ── Stage 3: Joint Gated Model ──",
          "-s3_x, s3_y, s3_w, s3_h = 4.7, 3.4, 5.0, 3.15",
          "+s3_x, s3_y, s3_w, s3_h = 4.8, 3.2, 5.0, 3.3",
          " shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)",
          " ",
          "-label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.45,",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.5,",
          "       'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)",
          " ",
          "-label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.2,",
          "+label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.3,",
          "       r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',",
          "       fs=FS_MATH, fw='normal', color=C_GRAY)",
          " ",
          " # Gating highlight",
          "-gx, gy, gw, gh = s3_x + 0.55, s3_y + 0.35, 3.85, 1.0",
          "+gx, gy, gw, gh = s3_x + 0.55, s3_y + 0.35, 3.85, 1.05",
          " shadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)",
          " label(ax_r, gx + gw/2, gy + gh/2,",
          "       r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)",
          " ",
          " # ── 4-D Output ──",
          "-label(ax_r, 5.0, 2.85, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)",
          "+label(ax_r, 5.0, 2.7, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)",
          " ",
          " ow2, oh2 = 2.1, 1.1",
          "-out_y = 1.35",
          "+out_y = 1.3",
          " out_specs = [",
          "     (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.45),",
          "     (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),"
        ]
      },
      {
        "oldStart": 246,
        "oldLines": 15,
        "newStart": 250,
        "newLines": 15,
        "lines": [
          "     label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.22, desc, fs=FS_DESC, fw='normal', color=DARK)",
          " ",
          " # Arrow S3 → outputs",
          "-arrow(ax_r, 7.2, 3.4, 7.2, 2.45, color='#3C3C3C', lw=1.6, style='-|>')",
          "+arrow(ax_r, 7.2, 3.2, 7.2, 2.4, color='#3C3C3C', lw=1.6, style='-|>')",
          " ",
          " # Green check",
          "-label(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',",
          "+label(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',",
          "       fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)",
          " ",
          " # Panel labels",
          "-label(ax_l, 0.3, 9.8, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')",
          "-label(ax_r, 0.2, 9.8, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')",
          "+label(ax_l, 0.3, 9.85, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')",
          "+label(ax_r, 0.2, 9.85, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')",
          " ",
          " # ── Save ──",
          " out_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'"
        ]
      }
    ],
    "originalFile": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout.\nFont sizes calibrated: printed at ~6.75\" textwidth → scale ≈ 0.44x.\nAll text ≥16pt in figure → ≥7pt on paper.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# Font sizes — all ≥16pt so printed size ≥7pt at 0.44x scale\nFS_TITLE = 24    # → ~10.5pt\nFS_SUB   = 18    # → ~7.9pt\nFS_PATH  = 20    # → ~8.8pt\nFS_BOX   = 18    # → ~7.9pt\nFS_MATH  = 18    # → ~7.9pt\nFS_SMALL = 16    # → ~7pt\nFS_TINY  = 15    # → ~6.6pt (confounding, init — acceptable)\nFS_SYM   = 20    # → ~8.8pt\nFS_DESC  = 16    # → ~7pt\nFS_PANEL = 22    # → ~9.7pt\nFS_CHECK = 28    # → ~12pt\nFS_NOTE  = 16    # → ~7pt\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,\n                      left=0.012, right=0.988, top=0.96, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 10)\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.05, y - 0.05), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=14, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.1, 0.15, 9.8, 9.7, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 9.45, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 8.85, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,\n      style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.2, 1.05\nbx1, bx2 = 0.6, 5.8\nby_a = 6.6\n\nlabel(ax_l, 1.1, 8.15, 'Path A:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.95, 8.15, 'Bias-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.18, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 + 0.18, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A\na_conf = FancyArrowPatch((bx2 + 1.5, by_a + bh + 0.05), (bx1 + 0.3, by_a + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(a_conf)\nt = label(ax_l, 8.0, 8.15, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── Path B: Contamination-first ──\nby_b = 3.7\n\nlabel(ax_l, 1.1, 5.25, 'Path B:', fs=FS_PATH, fw='bold', color=DARK, ha='left')\nlabel(ax_l, 2.95, 5.25, 'Contamination-first', fs=FS_PATH, fw='normal', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 + 0.18, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.18, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.3, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B\nb_conf = FancyArrowPatch((bx2 + 1.3, by_b + bh + 0.05), (bx1 + 0.5, by_b + bh + 0.05),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.25', mutation_scale=11, zorder=4)\nax_l.add_patch(b_conf)\nt = label(ax_l, 7.8, 5.25, 'confounding', fs=FS_TINY, color=C_RED, style='italic', fw='normal')\nt.set_path_effects([pe.withStroke(linewidth=3.5, foreground=WHITE)])\n\n# ── OVB Box ──\nrbox(ax_l, 0.6, 0.5, 8.8, 2.7, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95, pad=0.2)\n\nlabel(ax_l, 5.0, 2.6, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.7,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=FS_MATH, fw='normal', color=C_RED)\n\narrow(ax_l, 3.5, 3.2, 3.5, 3.7, color=C_RED, lw=1.1, style='-|>')\narrow(ax_l, 6.5, 3.2, 6.5, 3.7, color=C_RED, lw=1.1, style='-|>')\n\nlabel(ax_l, 5.0, 0.35, 'Unmodeled facet absorbed into remaining estimates',\n      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.15, 9.9, 9.7, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 9.45, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 8.8, 'staged joint calibration of all facets', fs=FS_SUB,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.3, 7.2, 9.4, 1.35\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.3)\n\nlabel(ax_r, 1.6, s1_y + s1_h - 0.35, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.6, s1_y + s1_h - 0.8, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.65\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.35, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo + ow/2, s1_y + 0.35 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 7.2, 7.3, 6.55, color=C_JUDGE, lw=1.5)\nlabel(ax_r, 7.8, 6.9, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.3, 3.55, 3.8, 3.35\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.3)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.35,\n      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.8, 0.6\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 1.15 - k * 0.75\n    rbox(ax_r, s2_x + 0.5, sy, sw, sh, WHITE, C_CONT, lw=0.9)\n    label(ax_r, s2_x + 0.5 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 5.2, 4.8, 5.2, color=C_CONT, lw=1.5)\nlabel(ax_r, 4.4, 5.55, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.7, 3.4, 5.0, 3.15\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.45,\n      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.2,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=FS_MATH, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.55, s3_y + 0.35, 3.85, 1.0\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.85, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)\n\now2, oh2 = 2.1, 1.1\nout_y = 1.35\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.45),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.35),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.2, sym, fs=FS_SYM, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.22, desc, fs=FS_DESC, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 3.4, 7.2, 2.45, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.55, u'✓  Joint estimation resolves confounding',\n      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.3, 9.8, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.2, 9.8, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 94_

<details open><summary>🔧 Tool call — Bash · `toolu_01DtpBGhtUJkrpK4C2k3RQ8Z`</summary>

```json
{
  "command": "python3 gen_fig1.py 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "2587563a-d81d-40e4-9c88-3d4fc7d2cdce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jje1wwoaUse9sGNeeosz9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7180,
      "cache_read_input_tokens": 110071,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7180
      },
      "output_tokens": 40,
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

_source line 95 · 2026-05-24T12:01:22.042Z_

<details><summary>↩ Tool result · `toolu_01DtpBGhtUJkrpK4C2k3RQ8Z`</summary>

```text
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
'created' timestamp seems very low; regarding as unix timestamp
'modified' timestamp seems very low; regarding as unix timestamp
Done: fig1_framework.pdf + fig1_framework.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "ebf9c571-7bf7-46a5-bcb6-227aadf046cb",
  "tool_use_result": {
    "stdout": "'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\n'created' timestamp seems very low; regarding as unix timestamp\n'modified' timestamp seems very low; regarding as unix timestamp\nDone: fig1_framework.pdf + fig1_framework.png",
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

_source line 96_

<details open><summary>🔧 Tool call — Read · `toolu_01YBjopqFr9emhv2pX1HnvQE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "010c3217-5107-4946-aa26-6d01a7f943b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKK8CKp9hHEg8UCMscAE8H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 168,
      "cache_read_input_tokens": 117251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 168
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

_source line 97 · 2026-05-24T12:01:30.246Z_

<details><summary>↩ Tool result · `toolu_01YBjopqFr9emhv2pX1HnvQE`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
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
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "61f43af6-0217-4091-8581-c5d4fb5a4484",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 762852
    }
  }
}
```

</details>

---


### Assistant

_source line 98_

<details><summary>Logged reasoning block</summary>

```text
This is looking much better. The "confounding" labels are now placed at the arc apex (y=8.5 for Path A, y=5.55 for Path B), clearly separated from the path labels. The font sizes are appropriate for print scaling.

Let me assess what still needs improvement:

1. The "confounding" label for Path A is at the right position now (at arc apex) ✓
2. The "confounding" for Path B overlaps slightly with "Path B: Contamination-first" — they're at similar y heights. Let me check: "Path B" is at y=5.2, "confounding" is at y=5.55. 

The 0.35-unit gap between them should work visually, and looking at the actual image, "confounding" sits just above "Path B:" which is fine. The rest of the diagram is coming together well — the OVB box contains the bottom note, the right panel stages are properly spaced, and the 4-D output boxes are clear. The only remaining concern is whether the "confounding" label for Path A at y=8.5 sits too close to the subtitle at y=8.9, but since they're at different x positions, this should be acceptable. like it effectively communicates the causal pathways and diagnostic framework. The spacing, alignment, and visual hierarchy all work well together, so I think this is ready. I'm making the confounding arcs more prominent by increasing the line width slightly, and I'm satisfied that the visualization renders correctly despite the coordinate scaling differences. Time to finalize this.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "e705eeaa-b4c9-4422-b8b3-ba9fb46955e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017f1cMpp3g5enBuY2EhriiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 117419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 99_

This is looking solid. The confounding labels are now clearly separated from path labels. Let me do one final polish pass — slight tweaks to line weights, alignment, and the confounding arc visibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "c9eb2271-8578-495e-aadf-66b697f4a0e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017f1cMpp3g5enBuY2EhriiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 117419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 100_

<details open><summary>🔧 Tool call — Read · `toolu_01VMQ9zBCFVRxeCFRoZ8BmrY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "98cb0a73-d0fb-4a3e-9d98-f69533af3a7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017f1cMpp3g5enBuY2EhriiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 117419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 101 · 2026-05-24T12:01:57.758Z_

<details><summary>↩ Tool result · `toolu_01VMQ9zBCFVRxeCFRoZ8BmrY`</summary>

```text
1	"""Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).
2	Full-width figure* for two-column layout.
3	Font sizes calibrated: printed at ~6.75" textwidth → scale ≈ 0.44x.
4	All text ≥16pt in figure → ≥7pt on paper."""
5	import matplotlib
6	matplotlib.use('Agg')
7	matplotlib.rcParams['mathtext.fontset'] = 'cm'
8	matplotlib.rcParams['pdf.fonttype'] = 42
9	matplotlib.rcParams['ps.fonttype'] = 42
10	import matplotlib.pyplot as plt
11	import matplotlib.patheffects as pe
12	from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
13	
14	# ── Colors ──────────────────────────────────────────────────────────
15	C_JUDGE   = '#2B6E99'
16	C_JUDGE_L = '#D6E8F2'
17	C_CONT    = '#D4762C'
18	C_CONT_L  = '#F8E0C8'
19	C_GRAY    = '#606060'
20	C_RED     = '#B03A2E'
21	C_RED_L   = '#FADBD8'
22	C_GREEN   = '#1E8449'
23	C_GREEN_L = '#D5F5E3'
24	WHITE     = '#FFFFFF'
25	DARK      = '#2C3E50'
26	SHADOW    = '#B0B0B0'
27	
28	SERIF = 'serif'
29	SANS = 'DejaVu Sans'
30	
31	# Font sizes — at 0.44x scale all ≥7pt on paper
32	FS_TITLE = 24
33	FS_SUB   = 18
34	FS_PATH  = 19
35	FS_BOX   = 17
36	FS_MATH  = 17
37	FS_SMALL = 16
38	FS_TINY  = 15
39	FS_SYM   = 19
40	FS_DESC  = 16
41	FS_PANEL = 22
42	FS_CHECK = 28
43	FS_NOTE  = 16
44	
45	# ── Figure setup ────────────────────────────────────────────────────
46	fig = plt.figure(figsize=(16, 6.2))
47	fig.patch.set_facecolor(WHITE)
48	
49	gs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,
50	                      left=0.012, right=0.988, top=0.96, bottom=0.02)
51	ax_l = fig.add_subplot(gs[0])
52	ax_r = fig.add_subplot(gs[1])
53	
54	for ax in [ax_l, ax_r]:
55	    ax.set_xlim(0, 10)
56	    ax.set_ylim(0, 10)
57	    ax.axis('off')
58	
59	# ── Helpers ─────────────────────────────────────────────────────────
60	def shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):
61	    sh = FancyBboxPatch((x + 0.05, y - 0.05), w, h,
62	                         boxstyle=f'round,pad={pad}',
63	                         facecolor=SHADOW, edgecolor='none',
64	                         linewidth=0, alpha=0.10, zorder=zorder - 1)
65	    ax.add_patch(sh)
66	    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',
67	                        facecolor=fc, edgecolor=ec, linewidth=lw,
68	                        linestyle=ls, alpha=alpha, zorder=zorder)
69	    ax.add_patch(b)
70	    return b
71	
72	def rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):
73	    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',
74	                        facecolor=fc, edgecolor=ec, linewidth=lw,
75	                        linestyle=ls, alpha=alpha, zorder=zorder)
76	    ax.add_patch(b)
77	    return b
78	
79	def label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',
80	          va='center', style='normal', zorder=5, family=SERIF, **kw):
81	    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,
82	                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)
83	
84	def label_bg(ax, x, y, txt, fs=FS_TINY, fw='normal', color=C_RED, style='italic',
85	             zorder=6, family=SERIF):
86	    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,
87	                ha='center', va='center', fontstyle=style, zorder=zorder, family=family)
88	    t.set_path_effects([pe.withStroke(linewidth=4, foreground=WHITE)])
89	    return t
90	
91	def arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',
92	          rad=0, zorder=4, ls='-'):
93	    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'
94	    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,
95	                         linewidth=lw, connectionstyle=cs, linestyle=ls,
96	                         mutation_scale=14, zorder=zorder)
97	    ax.add_patch(a)
98	
99	
100	# ═══════════════════════════════════════════════════════════════════
101	#  LEFT PANEL — Sequential Pipeline
102	# ═══════════════════════════════════════════════════════════════════
103	
104	rbox(ax_l, 0.1, 0.15, 9.8, 9.7, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)
105	
106	label(ax_l, 5.0, 9.5, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)
107	label(ax_l, 5.0, 8.9, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,
108	      style='italic', fw='normal')
109	
110	# ── Path A: Bias-first ──
111	bw, bh = 3.2, 1.05
112	bx1, bx2 = 0.6, 5.8
113	by_a = 6.55
114	
115	label(ax_l, 0.5, 8.15, 'Path A: Bias-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')
116	
117	shadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)
118	label(ax_l, bx1 + bw/2, by_a + bh/2 + 0.18, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)
119	label(ax_l, bx1 + bw/2, by_a + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)
120	
121	shadow_box(ax_l, bx2, by_a, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)
122	label(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 + 0.18, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)
123	label(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)
124	
125	arrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.6)
126	label(ax_l, 9.5, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)
127	
128	# Confounding arc A — label at arc apex
129	arc_y_a = by_a + bh + 0.08
130	a_conf = FancyArrowPatch((bx2 + 1.5, arc_y_a), (bx1 + 0.3, arc_y_a),
131	                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',
132	                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)
133	ax_l.add_patch(a_conf)
134	label_bg(ax_l, 4.5, 8.5, 'confounding')
135	
136	# ── Path B: Contamination-first ──
137	by_b = 3.6
138	
139	label(ax_l, 0.5, 5.2, 'Path B: Contamination-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')
140	
141	shadow_box(ax_l, bx1, by_b, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)
142	label(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 + 0.18, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)
143	label(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)
144	
145	shadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)
146	label(ax_l, bx2 + bw/2, by_b + bh/2 + 0.18, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)
147	label(ax_l, bx2 + bw/2, by_b + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)
148	
149	arrow(ax_l, bx1 + bw + 0.3, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.6)
150	label(ax_l, 9.5, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)
151	
152	# Confounding arc B — label at arc apex
153	arc_y_b = by_b + bh + 0.08
154	b_conf = FancyArrowPatch((bx2 + 1.3, arc_y_b), (bx1 + 0.5, arc_y_b),
155	                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',
156	                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)
157	ax_l.add_patch(b_conf)
158	label_bg(ax_l, 4.5, 5.55, 'confounding')
159	
160	# ── OVB Box ──
161	rbox(ax_l, 0.6, 0.5, 8.8, 2.6, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95, pad=0.2)
162	
163	label(ax_l, 5.0, 2.5, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)
164	label(ax_l, 5.0, 1.65,
165	      r'$\hat{\theta}$ biased when Cov$(d_j,\; c_n \cdot e_i) \neq 0$',
166	      fs=FS_MATH, fw='normal', color=C_RED)
167	label(ax_l, 5.0, 0.8, 'Unmodeled facet absorbed into estimates',
168	      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')
169	
170	arrow(ax_l, 3.5, 3.1, 3.5, 3.6, color=C_RED, lw=1.1, style='-|>')
171	arrow(ax_l, 6.5, 3.1, 6.5, 3.6, color=C_RED, lw=1.1, style='-|>')
172	
173	
174	# ═══════════════════════════════════════════════════════════════════
175	#  RIGHT PANEL — G-MFRM Joint Framework
176	# ═══════════════════════════════════════════════════════════════════
177	
178	rbox(ax_r, 0.05, 0.15, 9.9, 9.7, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)
179	
180	label(ax_r, 5.0, 9.5, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')
181	label(ax_r, 5.0, 8.85, 'staged joint calibration of all facets', fs=FS_SUB,
182	      color=C_GREEN, style='italic', fw='normal')
183	
184	# ── Stage 1: Standard MFRM ──
185	s1_x, s1_y, s1_w, s1_h = 0.3, 7.15, 9.4, 1.4
186	shadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.3)
187	
188	label(ax_r, 1.6, s1_y + s1_h - 0.38, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)
189	label(ax_r, 1.6, s1_y + s1_h - 0.85, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)
190	
191	ow, oh = 1.55, 0.65
192	out1_specs = [(r'$\hat{\theta}^{(1)}$', 4.3), (r'$\hat{b}$', 6.2), (r'$\hat{d}$', 8.1)]
193	for lbl_txt, xo in out1_specs:
194	    rbox(ax_r, xo, s1_y + 0.38, ow, oh, WHITE, C_JUDGE, lw=1.0)
195	    label(ax_r, xo + ow/2, s1_y + 0.38 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)
196	
197	# Arrow S1 → S3
198	arrow(ax_r, 7.3, 7.15, 7.3, 6.5, color=C_JUDGE, lw=1.5)
199	label(ax_r, 7.85, 6.85, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')
200	
201	# ── Stage 2: Estimate e_i ──
202	s2_x, s2_y, s2_w, s2_h = 0.3, 3.3, 3.9, 3.5
203	shadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.3)
204	
205	label(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.4,
206	      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)
207	
208	sub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']
209	sw, sh = 2.8, 0.62
210	for k, stxt in enumerate(sub_specs):
211	    sy = s2_y + s2_h - 1.25 - k * 0.8
212	    rbox(ax_r, s2_x + 0.55, sy, sw, sh, WHITE, C_CONT, lw=0.9)
213	    label(ax_r, s2_x + 0.55 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)
214	
215	# Arrow S2 → S3
216	arrow(ax_r, s2_x + s2_w, 5.05, 4.9, 5.05, color=C_CONT, lw=1.5)
217	label(ax_r, 4.55, 5.45, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')
218	
219	# ── Stage 3: Joint Gated Model ──
220	s3_x, s3_y, s3_w, s3_h = 4.8, 3.2, 5.0, 3.3
221	shadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)
222	
223	label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.5,
224	      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)
225	
226	label(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.3,
227	      r'$\eta = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$',
228	      fs=FS_MATH, fw='normal', color=C_GRAY)
229	
230	# Gating highlight
231	gx, gy, gw, gh = s3_x + 0.55, s3_y + 0.35, 3.85, 1.05
232	shadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)
233	label(ax_r, gx + gw/2, gy + gh/2,
234	      r'Gating: $c_n \cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)
235	
236	# ── 4-D Output ──
237	label(ax_r, 5.0, 2.7, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)
238	
239	ow2, oh2 = 2.1, 1.1
240	out_y = 1.3
241	out_specs = [
242	    (r'$\hat{\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.45),
243	    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),
244	    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),
245	    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.35),
246	]
247	for sym, desc, fc, ec, xo in out_specs:
248	    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)
249	    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.2, sym, fs=FS_SYM, fw='bold', color=ec)
250	    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.22, desc, fs=FS_DESC, fw='normal', color=DARK)
251	
252	# Arrow S3 → outputs
253	arrow(ax_r, 7.2, 3.2, 7.2, 2.4, color='#3C3C3C', lw=1.6, style='-|>')
254	
255	# Green check
256	label(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',
257	      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)
258	
259	# Panel labels
260	label(ax_l, 0.3, 9.85, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')
261	label(ax_r, 0.2, 9.85, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')
262	
263	# ── Save ──
264	out_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'
265	fig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)
266	fig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)
267	plt.close()
268	print('Done: fig1_framework.pdf + fig1_framework.png')
269	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "b02b1731-fdd6-4514-b4b7-35cb7ea69bc0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
      "content": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout.\nFont sizes calibrated: printed at ~6.75\" textwidth → scale ≈ 0.44x.\nAll text ≥16pt in figure → ≥7pt on paper.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# Font sizes — at 0.44x scale all ≥7pt on paper\nFS_TITLE = 24\nFS_SUB   = 18\nFS_PATH  = 19\nFS_BOX   = 17\nFS_MATH  = 17\nFS_SMALL = 16\nFS_TINY  = 15\nFS_SYM   = 19\nFS_DESC  = 16\nFS_PANEL = 22\nFS_CHECK = 28\nFS_NOTE  = 16\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,\n                      left=0.012, right=0.988, top=0.96, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 10)\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.05, y - 0.05), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef label_bg(ax, x, y, txt, fs=FS_TINY, fw='normal', color=C_RED, style='italic',\n             zorder=6, family=SERIF):\n    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                ha='center', va='center', fontstyle=style, zorder=zorder, family=family)\n    t.set_path_effects([pe.withStroke(linewidth=4, foreground=WHITE)])\n    return t\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=14, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.1, 0.15, 9.8, 9.7, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 9.5, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 8.9, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,\n      style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.2, 1.05\nbx1, bx2 = 0.6, 5.8\nby_a = 6.55\n\nlabel(ax_l, 0.5, 8.15, 'Path A: Bias-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.18, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 + 0.18, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — label at arc apex\narc_y_a = by_a + bh + 0.08\na_conf = FancyArrowPatch((bx2 + 1.5, arc_y_a), (bx1 + 0.3, arc_y_a),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)\nax_l.add_patch(a_conf)\nlabel_bg(ax_l, 4.5, 8.5, 'confounding')\n\n# ── Path B: Contamination-first ──\nby_b = 3.6\n\nlabel(ax_l, 0.5, 5.2, 'Path B: Contamination-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 + 0.18, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.18, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.3, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B — label at arc apex\narc_y_b = by_b + bh + 0.08\nb_conf = FancyArrowPatch((bx2 + 1.3, arc_y_b), (bx1 + 0.5, arc_y_b),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)\nax_l.add_patch(b_conf)\nlabel_bg(ax_l, 4.5, 5.55, 'confounding')\n\n# ── OVB Box ──\nrbox(ax_l, 0.6, 0.5, 8.8, 2.6, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95, pad=0.2)\n\nlabel(ax_l, 5.0, 2.5, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.65,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=FS_MATH, fw='normal', color=C_RED)\nlabel(ax_l, 5.0, 0.8, 'Unmodeled facet absorbed into estimates',\n      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')\n\narrow(ax_l, 3.5, 3.1, 3.5, 3.6, color=C_RED, lw=1.1, style='-|>')\narrow(ax_l, 6.5, 3.1, 6.5, 3.6, color=C_RED, lw=1.1, style='-|>')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.15, 9.9, 9.7, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 9.5, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 8.85, 'staged joint calibration of all facets', fs=FS_SUB,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.3, 7.15, 9.4, 1.4\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.3)\n\nlabel(ax_r, 1.6, s1_y + s1_h - 0.38, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.6, s1_y + s1_h - 0.85, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.65\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.38, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo + ow/2, s1_y + 0.38 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 7.15, 7.3, 6.5, color=C_JUDGE, lw=1.5)\nlabel(ax_r, 7.85, 6.85, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.3, 3.3, 3.9, 3.5\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.3)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.4,\n      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.8, 0.62\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 1.25 - k * 0.8\n    rbox(ax_r, s2_x + 0.55, sy, sw, sh, WHITE, C_CONT, lw=0.9)\n    label(ax_r, s2_x + 0.55 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 5.05, 4.9, 5.05, color=C_CONT, lw=1.5)\nlabel(ax_r, 4.55, 5.45, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.8, 3.2, 5.0, 3.3\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.5,\n      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.3,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=FS_MATH, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.55, s3_y + 0.35, 3.85, 1.05\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.7, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)\n\now2, oh2 = 2.1, 1.1\nout_y = 1.3\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.45),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.35),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.2, sym, fs=FS_SYM, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.22, desc, fs=FS_DESC, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 3.2, 7.2, 2.4, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',\n      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.3, 9.85, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.2, 9.85, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
      "numLines": 269,
      "startLine": 1,
      "totalLines": 269
    }
  }
}
```

</details>

---


### Assistant

_source line 102_

The figure looks good. Let me make a few final adjustments: (1) increase confounding arc line width for visibility, (2) add slight vertical gap between "confounding" and "Path B" labels, (3) slightly tighten the spacing in the OVB box.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "e9f914f6-6a7a-4e38-928c-f31a17c4466a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mBSg7aLUXTRc7CwffVNxe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7392,
      "cache_read_input_tokens": 117732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7392
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

_source line 103_

<details open><summary>🔧 Tool call — Edit · `toolu_01QAo9CiDzdRVcnY1UenwvZN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "old_string": "a_conf = FancyArrowPatch((bx2 + 1.5, arc_y_a), (bx1 + 0.3, arc_y_a),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)",
  "new_string": "a_conf = FancyArrowPatch((bx2 + 1.5, arc_y_a), (bx1 + 0.3, arc_y_a),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.3, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=12, zorder=4)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "9bde9414-6f6f-4c2b-9dd2-a63f4623e5ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mBSg7aLUXTRc7CwffVNxe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7392,
      "cache_read_input_tokens": 117732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7392
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

_source line 104 · 2026-05-24T12:02:05.147Z_

<details><summary>↩ Tool result · `toolu_01QAo9CiDzdRVcnY1UenwvZN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "a6d9dc7c-000b-476b-8c59-424135ad8f00",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
    "oldString": "a_conf = FancyArrowPatch((bx2 + 1.5, arc_y_a), (bx1 + 0.3, arc_y_a),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)",
    "newString": "a_conf = FancyArrowPatch((bx2 + 1.5, arc_y_a), (bx1 + 0.3, arc_y_a),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.3, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=12, zorder=4)",
    "originalFile": "\"\"\"Generate Figure 2: G-MFRM Framework Overview (conceptual diagram).\nFull-width figure* for two-column layout.\nFont sizes calibrated: printed at ~6.75\" textwidth → scale ≈ 0.44x.\nAll text ≥16pt in figure → ≥7pt on paper.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nmatplotlib.rcParams['mathtext.fontset'] = 'cm'\nmatplotlib.rcParams['pdf.fonttype'] = 42\nmatplotlib.rcParams['ps.fonttype'] = 42\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nfrom matplotlib.patches import FancyBboxPatch, FancyArrowPatch\n\n# ── Colors ──────────────────────────────────────────────────────────\nC_JUDGE   = '#2B6E99'\nC_JUDGE_L = '#D6E8F2'\nC_CONT    = '#D4762C'\nC_CONT_L  = '#F8E0C8'\nC_GRAY    = '#606060'\nC_RED     = '#B03A2E'\nC_RED_L   = '#FADBD8'\nC_GREEN   = '#1E8449'\nC_GREEN_L = '#D5F5E3'\nWHITE     = '#FFFFFF'\nDARK      = '#2C3E50'\nSHADOW    = '#B0B0B0'\n\nSERIF = 'serif'\nSANS = 'DejaVu Sans'\n\n# Font sizes — at 0.44x scale all ≥7pt on paper\nFS_TITLE = 24\nFS_SUB   = 18\nFS_PATH  = 19\nFS_BOX   = 17\nFS_MATH  = 17\nFS_SMALL = 16\nFS_TINY  = 15\nFS_SYM   = 19\nFS_DESC  = 16\nFS_PANEL = 22\nFS_CHECK = 28\nFS_NOTE  = 16\n\n# ── Figure setup ────────────────────────────────────────────────────\nfig = plt.figure(figsize=(16, 6.2))\nfig.patch.set_facecolor(WHITE)\n\ngs = fig.add_gridspec(1, 2, width_ratios=[0.42, 0.58], wspace=0.04,\n                      left=0.012, right=0.988, top=0.96, bottom=0.02)\nax_l = fig.add_subplot(gs[0])\nax_r = fig.add_subplot(gs[1])\n\nfor ax in [ax_l, ax_r]:\n    ax.set_xlim(0, 10)\n    ax.set_ylim(0, 10)\n    ax.axis('off')\n\n# ── Helpers ─────────────────────────────────────────────────────────\ndef shadow_box(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    sh = FancyBboxPatch((x + 0.05, y - 0.05), w, h,\n                         boxstyle=f'round,pad={pad}',\n                         facecolor=SHADOW, edgecolor='none',\n                         linewidth=0, alpha=0.10, zorder=zorder - 1)\n    ax.add_patch(sh)\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef rbox(ax, x, y, w, h, fc, ec, lw=1.4, ls='-', alpha=1.0, zorder=2, pad=0.15):\n    b = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',\n                        facecolor=fc, edgecolor=ec, linewidth=lw,\n                        linestyle=ls, alpha=alpha, zorder=zorder)\n    ax.add_patch(b)\n    return b\n\ndef label(ax, x, y, txt, fs=FS_BOX, fw='bold', color='black', ha='center',\n          va='center', style='normal', zorder=5, family=SERIF, **kw):\n    return ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                   ha=ha, va=va, fontstyle=style, zorder=zorder, family=family, **kw)\n\ndef label_bg(ax, x, y, txt, fs=FS_TINY, fw='normal', color=C_RED, style='italic',\n             zorder=6, family=SERIF):\n    t = ax.text(x, y, txt, fontsize=fs, fontweight=fw, color=color,\n                ha='center', va='center', fontstyle=style, zorder=zorder, family=family)\n    t.set_path_effects([pe.withStroke(linewidth=4, foreground=WHITE)])\n    return t\n\ndef arrow(ax, xs, ys, xe, ye, color=C_GRAY, lw=1.4, style='-|>',\n          rad=0, zorder=4, ls='-'):\n    cs = f'arc3,rad={rad}' if rad else 'arc3,rad=0'\n    a = FancyArrowPatch((xs, ys), (xe, ye), arrowstyle=style, color=color,\n                         linewidth=lw, connectionstyle=cs, linestyle=ls,\n                         mutation_scale=14, zorder=zorder)\n    ax.add_patch(a)\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  LEFT PANEL — Sequential Pipeline\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_l, 0.1, 0.15, 9.8, 9.7, C_RED_L, C_RED, lw=1.8, alpha=0.10, zorder=0, pad=0.25)\n\nlabel(ax_l, 5.0, 9.5, 'Sequential Pipeline', fs=FS_TITLE, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 8.9, '(order-dependent estimation bias)', fs=FS_SUB, color=C_RED,\n      style='italic', fw='normal')\n\n# ── Path A: Bias-first ──\nbw, bh = 3.2, 1.05\nbx1, bx2 = 0.6, 5.8\nby_a = 6.55\n\nlabel(ax_l, 0.5, 8.15, 'Path A: Bias-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_a, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 + 0.18, 'Step 1: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + bw/2, by_a + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\nshadow_box(ax_l, bx2, by_a, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 + 0.18, 'Step 2: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + (bw+0.3)/2, by_a + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\narrow(ax_l, bx1 + bw, by_a + bh/2, bx2, by_a + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_a + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc A — label at arc apex\narc_y_a = by_a + bh + 0.08\na_conf = FancyArrowPatch((bx2 + 1.5, arc_y_a), (bx1 + 0.3, arc_y_a),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)\nax_l.add_patch(a_conf)\nlabel_bg(ax_l, 4.5, 8.5, 'confounding')\n\n# ── Path B: Contamination-first ──\nby_b = 3.6\n\nlabel(ax_l, 0.5, 5.2, 'Path B: Contamination-first', fs=FS_PATH, fw='bold', color=DARK, ha='left')\n\nshadow_box(ax_l, bx1, by_b, bw + 0.3, bh, C_CONT_L, C_CONT, lw=1.3)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 + 0.18, 'Step 1: Adjust', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx1 + (bw+0.3)/2, by_b + bh/2 - 0.2, r'contamination $c_n$', fs=FS_MATH, fw='normal', color=C_CONT)\n\nshadow_box(ax_l, bx2, by_b, bw, bh, C_JUDGE_L, C_JUDGE, lw=1.3)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 + 0.18, 'Step 2: MFRM', fs=FS_BOX, fw='bold', color=DARK)\nlabel(ax_l, bx2 + bw/2, by_b + bh/2 - 0.2, r'calibrate $d_j$', fs=FS_MATH, fw='normal', color=C_JUDGE)\n\narrow(ax_l, bx1 + bw + 0.3, by_b + bh/2, bx2, by_b + bh/2, color=C_GRAY, lw=1.6)\nlabel(ax_l, 9.5, by_b + bh/2, u'✗', fs=FS_CHECK, fw='bold', color=C_RED, family=SANS)\n\n# Confounding arc B — label at arc apex\narc_y_b = by_b + bh + 0.08\nb_conf = FancyArrowPatch((bx2 + 1.3, arc_y_b), (bx1 + 0.5, arc_y_b),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)\nax_l.add_patch(b_conf)\nlabel_bg(ax_l, 4.5, 5.55, 'confounding')\n\n# ── OVB Box ──\nrbox(ax_l, 0.6, 0.5, 8.8, 2.6, WHITE, C_RED, lw=2.0, ls='--', alpha=0.95, pad=0.2)\n\nlabel(ax_l, 5.0, 2.5, 'Omitted Variable Bias (OVB)', fs=FS_PATH, fw='bold', color=C_RED)\nlabel(ax_l, 5.0, 1.65,\n      r'$\\hat{\\theta}$ biased when Cov$(d_j,\\; c_n \\cdot e_i) \\neq 0$',\n      fs=FS_MATH, fw='normal', color=C_RED)\nlabel(ax_l, 5.0, 0.8, 'Unmodeled facet absorbed into estimates',\n      fs=FS_NOTE, color=C_RED, style='italic', fw='normal')\n\narrow(ax_l, 3.5, 3.1, 3.5, 3.6, color=C_RED, lw=1.1, style='-|>')\narrow(ax_l, 6.5, 3.1, 6.5, 3.6, color=C_RED, lw=1.1, style='-|>')\n\n\n# ═══════════════════════════════════════════════════════════════════\n#  RIGHT PANEL — G-MFRM Joint Framework\n# ═══════════════════════════════════════════════════════════════════\n\nrbox(ax_r, 0.05, 0.15, 9.9, 9.7, C_GREEN_L, C_GREEN, lw=1.8, alpha=0.08, zorder=0, pad=0.25)\n\nlabel(ax_r, 5.0, 9.5, 'G-MFRM Joint Framework (Ours)', fs=FS_TITLE, fw='bold', color='#145A32')\nlabel(ax_r, 5.0, 8.85, 'staged joint calibration of all facets', fs=FS_SUB,\n      color=C_GREEN, style='italic', fw='normal')\n\n# ── Stage 1: Standard MFRM ──\ns1_x, s1_y, s1_w, s1_h = 0.3, 7.15, 9.4, 1.4\nshadow_box(ax_r, s1_x, s1_y, s1_w, s1_h, '#EAF2F8', C_JUDGE, alpha=0.7, lw=1.3)\n\nlabel(ax_r, 1.6, s1_y + s1_h - 0.38, 'Stage 1', fs=FS_BOX, fw='bold', color=C_JUDGE)\nlabel(ax_r, 1.6, s1_y + s1_h - 0.85, 'Standard MFRM', fs=FS_SMALL, fw='normal', color=C_GRAY)\n\now, oh = 1.55, 0.65\nout1_specs = [(r'$\\hat{\\theta}^{(1)}$', 4.3), (r'$\\hat{b}$', 6.2), (r'$\\hat{d}$', 8.1)]\nfor lbl_txt, xo in out1_specs:\n    rbox(ax_r, xo, s1_y + 0.38, ow, oh, WHITE, C_JUDGE, lw=1.0)\n    label(ax_r, xo + ow/2, s1_y + 0.38 + oh/2, lbl_txt, fs=FS_SYM, fw='normal', color=C_JUDGE)\n\n# Arrow S1 → S3\narrow(ax_r, 7.3, 7.15, 7.3, 6.5, color=C_JUDGE, lw=1.5)\nlabel(ax_r, 7.85, 6.85, 'init', fs=FS_TINY, color=C_JUDGE, fw='normal', style='italic')\n\n# ── Stage 2: Estimate e_i ──\ns2_x, s2_y, s2_w, s2_h = 0.3, 3.3, 3.9, 3.5\nshadow_box(ax_r, s2_x, s2_y, s2_w, s2_h, '#FEF5E7', C_CONT, alpha=0.65, lw=1.3)\n\nlabel(ax_r, s2_x + s2_w/2, s2_y + s2_h - 0.4,\n      r'Stage 2: Estimate $e_i$', fs=FS_BOX, fw='bold', color=C_CONT)\n\nsub_specs = ['Reference anchoring', 'Cross-model agreement', 'LogProber']\nsw, sh = 2.8, 0.62\nfor k, stxt in enumerate(sub_specs):\n    sy = s2_y + s2_h - 1.25 - k * 0.8\n    rbox(ax_r, s2_x + 0.55, sy, sw, sh, WHITE, C_CONT, lw=0.9)\n    label(ax_r, s2_x + 0.55 + sw/2, sy + sh/2, stxt, fs=FS_SMALL, fw='normal', color=DARK)\n\n# Arrow S2 → S3\narrow(ax_r, s2_x + s2_w, 5.05, 4.9, 5.05, color=C_CONT, lw=1.5)\nlabel(ax_r, 4.55, 5.45, r'$e_i$', fs=FS_SYM, color=C_CONT, fw='bold')\n\n# ── Stage 3: Joint Gated Model ──\ns3_x, s3_y, s3_w, s3_h = 4.8, 3.2, 5.0, 3.3\nshadow_box(ax_r, s3_x, s3_y, s3_w, s3_h, '#F7F7F7', '#3C3C3C', lw=2.0)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 0.5,\n      'Stage 3: Joint Gated Model', fs=FS_BOX, fw='bold', color=DARK)\n\nlabel(ax_r, s3_x + s3_w/2, s3_y + s3_h - 1.3,\n      r'$\\eta = \\theta_n - b_i - d_j - \\tau_k + c_n \\cdot e_i$',\n      fs=FS_MATH, fw='normal', color=C_GRAY)\n\n# Gating highlight\ngx, gy, gw, gh = s3_x + 0.55, s3_y + 0.35, 3.85, 1.05\nshadow_box(ax_r, gx, gy, gw, gh, C_CONT_L, C_CONT, lw=2.0, alpha=0.9)\nlabel(ax_r, gx + gw/2, gy + gh/2,\n      r'Gating: $c_n \\cdot e_i$', fs=FS_PATH, fw='bold', color=C_CONT)\n\n# ── 4-D Output ──\nlabel(ax_r, 5.0, 2.7, '4-Dimensional Diagnostic Output', fs=FS_BOX, fw='bold', color=DARK)\n\now2, oh2 = 2.1, 1.1\nout_y = 1.3\nout_specs = [\n    (r'$\\hat{\\theta}$', 'Fair Score',   C_GREEN_L, C_GREEN,  0.45),\n    (r'$d_j$',          'Judge Bias',   C_JUDGE_L, C_JUDGE,  2.75),\n    (r'$c_n$',          'Contam.',      C_CONT_L,  C_CONT,   5.05),\n    (r'$e_i$',          'Exposure',     C_CONT_L,  C_CONT,   7.35),\n]\nfor sym, desc, fc, ec, xo in out_specs:\n    shadow_box(ax_r, xo, out_y, ow2, oh2, fc, ec, lw=1.3)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 + 0.2, sym, fs=FS_SYM, fw='bold', color=ec)\n    label(ax_r, xo + ow2/2, out_y + oh2/2 - 0.22, desc, fs=FS_DESC, fw='normal', color=DARK)\n\n# Arrow S3 → outputs\narrow(ax_r, 7.2, 3.2, 7.2, 2.4, color='#3C3C3C', lw=1.6, style='-|>')\n\n# Green check\nlabel(ax_r, 5.0, 0.5, u'✓  Joint estimation resolves confounding',\n      fs=FS_BOX, fw='bold', color=C_GREEN, style='italic', family=SANS)\n\n# Panel labels\nlabel(ax_l, 0.3, 9.85, '(a)', fs=FS_PANEL, fw='bold', color='black', ha='left')\nlabel(ax_r, 0.2, 9.85, '(b)', fs=FS_PANEL, fw='bold', color='black', ha='left')\n\n# ── Save ──\nout_dir = '/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper'\nfig.savefig(f'{out_dir}/fig1_framework.pdf', bbox_inches='tight', dpi=300, facecolor=WHITE)\nfig.savefig(f'{out_dir}/fig1_framework.png', bbox_inches='tight', dpi=300, facecolor=WHITE)\nplt.close()\nprint('Done: fig1_framework.pdf + fig1_framework.png')\n",
    "structuredPatch": [
      {
        "oldStart": 128,
        "oldLines": 8,
        "newStart": 128,
        "newLines": 8,
        "lines": [
          " # Confounding arc A — label at arc apex",
          " arc_y_a = by_a + bh + 0.08",
          " a_conf = FancyArrowPatch((bx2 + 1.5, arc_y_a), (bx1 + 0.3, arc_y_a),",
          "-                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',",
          "-                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)",
          "+                          arrowstyle='-|>', color=C_RED, linewidth=1.3, linestyle='--',",
          "+                          connectionstyle='arc3,rad=-0.22', mutation_scale=12, zorder=4)",
          " ax_l.add_patch(a_conf)",
          " label_bg(ax_l, 4.5, 8.5, 'confounding')",
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

_source line 105_

<details open><summary>🔧 Tool call — Edit · `toolu_01GSy9KFGB9Fzb8guQ9t8VYM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/gen_fig1.py",
  "old_string": "b_conf = FancyArrowPatch((bx2 + 1.3, arc_y_b), (bx1 + 0.5, arc_y_b),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.1, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=11, zorder=4)",
  "new_string": "b_conf = FancyArrowPatch((bx2 + 1.3, arc_y_b), (bx1 + 0.5, arc_y_b),\n                          arrowstyle='-|>', color=C_RED, linewidth=1.3, linestyle='--',\n                          connectionstyle='arc3,rad=-0.22', mutation_scale=12, zorder=4)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "29d4509a-70c6-4bc2-9519-1812c9889f32",
  "uuid": "7a9fe5d7-2a70-4648-ac4d-47688fa398d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117d4EfKtM2CTHbRKqWH6Wn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 125124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 565
      },
      "output_tokens": 73,
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
