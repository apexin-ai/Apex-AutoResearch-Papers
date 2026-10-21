# paper p0 2 5 statistics phase2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_paper_p0-2-5-statistics-phase2_20260528T053501.log`
- **Structured JSON:** [`b709e8575ec136b1a3f0.json`](../../sessions/b7/b709e8575ec136b1a3f0.json)

## Before a recorded user message

39 recorded events

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
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
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
  "uuid": "3b0181c7-1a71-4a6b-ac50-c2d72c281f70",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1779964200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "17849739-97d7-45db-9799-4ab20afc541a",
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down this complex task:

1. I need to edit `claim3.tex` and `appendix.tex` only
2. First, I need to read `paper_switch.py` to understand which text blocks are managed
3. Then read `claim3.tex` and `appendix.tex`
4. Compute exact permutation p-values using Python
5. Make all the specified edits
6. Verify paper_switch.py templates still match

Let me start by reading the key files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "6a45470f-7e7e-4b8b-93ab-5379a147b3e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9JJYBmMn5yitSNupCBGXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13665,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13665
      },
      "output_tokens": 30,
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

Reading the three key files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "f9b2cc09-187a-4967-b43e-b2d5a0278839",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9JJYBmMn5yitSNupCBGXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13665,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13665
      },
      "output_tokens": 30,
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

<details open><summary>🔧 Tool call — Read · `toolu_016Tz5QSsUa7PzXSkKpe6dbc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_switch.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "d18f7e2d-196d-4528-b707-5490fc81200d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9JJYBmMn5yitSNupCBGXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13665,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13665
      },
      "output_tokens": 30,
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

_source line 7 · 2026-05-28T05:35:16.878Z_

<details><summary>↩ Tool result · `toolu_016Tz5QSsUa7PzXSkKpe6dbc`</summary>

```text
1	#!/usr/bin/env python3
2	"""Auto-switch paper text based on λ=0.1 s2 30K eval result.
3	
4	Usage:
5	  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0 --dry-run
6	  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0
7	"""
8	import argparse
9	import subprocess
10	import sys
11	from itertools import combinations
12	from math import comb, sqrt
13	from pathlib import Path
14	
15	NULL_VALUES = [56.5, 52.5, 55, 57, 54, 52.5]
16	NULL_MEAN = sum(NULL_VALUES) / len(NULL_VALUES)
17	NULL_STD = (sum((x - NULL_MEAN) ** 2 for x in NULL_VALUES) / 5) ** 0.5
18	
19	S0_CAR, S1_CAR = 58.0, 58.5
20	S0_TSR, S1_TSR = 47.0, 49.0
21	
22	PAPER_DIR = Path(__file__).resolve().parent.parent / "docs" / "paper"
23	
24	
25	def mean(v):
26	    return sum(v) / len(v)
27	
28	
29	def std_b(v):
30	    m = mean(v)
31	    return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5
32	
33	
34	def perm_test(null_vals, treat_vals):
35	    pool = null_vals + treat_vals
36	    k = len(treat_vals)
37	    obs = mean(treat_vals)
38	    mu = mean(pool)
39	    dev = abs(obs - mu)
40	    n = comb(len(pool), k)
41	    ge = tw = 0
42	    for c in combinations(pool, k):
43	        m = mean(c)
44	        if m >= obs:
45	            ge += 1
46	        if abs(m - mu) >= dev - 1e-12:
47	            tw += 1
48	    return ge / n, tw / n, n
49	
50	
51	def fill(tpl, vals):
52	    for k, v in vals.items():
53	        tpl = tpl.replace("{" + k + "}", str(v))
54	    return tpl
55	
56	
57	def safe_replace(content, old, new, label):
58	    n = content.count(old)
59	    if n == 0:
60	        print(f"  !! [{label}] NOT FOUND")
61	        return content, False
62	    if n > 1:
63	        print(f"  !! [{label}] found {n}x")
64	        return content, False
65	    return content.replace(old, new), True
66	
67	
68	def get_replacements(scenario, v):
69	    R = []
70	    is_c = scenario == "C"
71	
72	    # 1. abstract.tex L5 (training results)
73	    old = (
74	        r"collision-free demonstrations alone account for all measured avoidance "
75	        r"gains (${\sim}$26 percentage points). SDF supervision adds no measurable "
76	        r"benefit across the full tested range $\lambda \in \{0.005, 0.01, 0.1\}$ "
77	        r"($p > 0.05$ for all; $\lambda = 0.1$: 57.00\%$\,\pm\,$2.18, 3 seeds)."
78	    )
79	    if is_c:
80	        new = fill(
81	            r"collision-free demonstrations alone account for nearly all measured "
82	            r"avoidance gains (${\sim}$26 percentage points). SDF supervision adds no "
83	            r"significant benefit at $\lambda \leq 0.01$ ($p > 0.1$); at "
84	            r"$\lambda = 0.1$, a modest but statistically significant increase emerges "
85	            r"({mean_car}\%$\,\pm\,${std_car}, permutation $p = {p_value}$, 3 seeds), "
86	            r"though the effect size ({delta_pp}\,pp) is small relative to the "
87	            r"$+$26\,pp gain from fine-tuning alone.", v)
88	    else:
89	        new = fill(
90	            r"collision-free demonstrations alone account for all measured avoidance "
91	            r"gains (${\sim}$26 percentage points). SDF supervision adds no measurable "
92	            r"benefit across the full tested range $\lambda \in \{0.005, 0.01, 0.1\}$ "
93	            r"($p > 0.05$ for all; $\lambda = 0.1$: {mean_car}\%$\,\pm\,${std_car}, "
94	            r"3 seeds).", v)
95	    R.append(("abstract.tex", "abstract L5 training", old, new))
96	
97	    # 2. abstract.tex L6 (concluding sentence)
98	    old = (
99	        r"Displacement filtering is necessary for meaningful VLA safety evaluation. "
100	        r"EE-only geometric supervision is fully redundant across a 20$\times$ "
101	        r"loss-weight range, confirming that collision avoidance arises from "
102	        r"demonstration data, not geometric supervision."
103	    )
104	    if is_c:
105	        new = (
106	            r"Displacement filtering is necessary for meaningful VLA safety evaluation. "
107	            r"Even at the highest tested loss weight, the modest SDF effect is dwarfed by "
108	            r"demonstration-driven avoidance and cannot overcome the structural limitation "
109	            r"of EE-only supervision."
110	        )
111	    else:
112	        new = (
113	            r"Displacement filtering is necessary for meaningful VLA safety evaluation. "
114	            r"EE-only geometric supervision is fully redundant across a 20$\times$ "
115	            r"loss-weight range, confirming that collision avoidance arises from "
116	            r"demonstration data, not geometric supervision."
117	        )
118	    R.append(("abstract.tex", "abstract L6 conclusion", old, new))
119	
120	    # 3. claim3.tex L3 scope sentence
121	    old = (
122	        r"We compare LoRA-only against LoRA+SDF across a 20$\times$ range of "
123	        r"loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all "
124	        r"evaluated at the 30K-step checkpoint."
125	    )
126	    if is_c:
127	        new = (
128	            r"We compare LoRA-only against LoRA+SDF at three loss weights "
129	            r"($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at "
130	            r"the 30K-step checkpoint."
131	        )
132	    else:
133	        new = (
134	            r"We compare LoRA-only against LoRA+SDF across a 20$\times$ range of "
135	            r"loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all "
136	            r"evaluated at the 30K-step checkpoint."
137	        )
138	    R.append(("claim3.tex", "claim3 L3 scope", old, new))
139	
140	    # 4. claim3.tex L7 table caption
141	    old = (
142	        r"\caption{Avoidance source attribution on SafeLIBERO. SDF adds no "
143	        r"measurable CAR beyond LoRA-only across the full tested range "
144	        r"$\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models "
145	        r"exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}"
146	    )
147	    if is_c:
148	        new = fill(
149	            r"\caption{Avoidance source attribution on SafeLIBERO. SDF at "
150	            r"$\lambda \leq 0.01$ adds no measurable CAR beyond LoRA-only "
151	            r"($p > 0.1$). At $\lambda = 0.1$, a modest increase reaches "
152	            r"statistical significance ($z = {z_value}$, permutation "
153	            r"$p = {p_value}$, $n{=}3$), though the effect size ({delta_pp}\,pp) "
154	            r"is small relative to the $+$26\,pp LoRA gain. All fine-tuned models "
155	            r"exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}", v)
156	    else:
157	        new = (
158	            r"\caption{Avoidance source attribution on SafeLIBERO. SDF adds no "
159	            r"measurable CAR beyond LoRA-only across the full tested range "
160	            r"$\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models "
161	            r"exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}"
162	        )
163	    R.append(("claim3.tex", "claim3 L7 caption", old, new))
164	
165	    # 5. claim3.tex L20 table row
166	    old = (
167	        r"LoRA+SDF $\lambda{=}0.1$ & 3 & "
168	        r"50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\"
169	    )
170	    new = fill(
171	        r"LoRA+SDF $\lambda{=}0.1$ & 3 & "
172	        r"{tsr_mean}\,$\pm$\,{tsr_std} & {mean_car}\,$\pm$\,{std_car} & 0.394 \\", v)
173	    R.append(("claim3.tex", "claim3 L20 table row", old, new))
174	
175	    # 6. claim3.tex L27 body paragraph
176	    old = (
177	        r"Table~\ref{tab:avoidance_source} shows that collision-free demonstrations "
178	        r"alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with "
179	        r"zero frozen episodes and displacement above 0.37\,m, confirming genuine "
180	        r"avoidance. Adding SDF supervision produces no measurable benefit across the "
181	        r"full tested range: LoRA-only CAR (54.67\%) is statistically "
182	        r"indistinguishable from all SDF conditions including $\lambda = 0.1$ "
183	        r"(57.00\%, $p = 0.131$; Appendix~\ref{sec:appendix_null}). "
184	        r"A Phase~2 ablation ($\lambda = 0$ after step 5K) yields "
185	        r"CAR\,=\,57.5\%\footnote{Single seed (s2); computational constraints "
186	        r"precluded additional seeds for this ablation.}, confirming that SDF "
187	        r"gradients produce no lasting behavioral effect. The per-task CAR ordering "
188	        r"is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce "
189	        r"lowest) and invariant to $\lambda$ across a 20$\times$ range, indicating "
190	        r"that avoidance patterns reflect the demonstration distribution rather than "
191	        r"geometric supervision."
192	    )
193	    if is_c:
194	        new = (
195	            r"Table~\ref{tab:avoidance_source} shows that collision-free demonstrations "
196	            r"alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with "
197	            r"zero frozen episodes and displacement above 0.37\,m, confirming genuine "
198	            r"avoidance. At $\lambda \leq 0.01$, SDF supervision produces no measurable "
199	            r"benefit: LoRA-only CAR (54.67\%) is within 0.17\,pp of $\lambda = 0.005$ "
200	            r"and statistically indistinguishable from $\lambda = 0.01$ (56.33\%, "
201	            r"$p > 0.1$; Appendix~\ref{sec:appendix_null}). At $\lambda = 0.1$, a modest "
202	            r"increase emerges (Section~\ref{sec:lambda_high}), but per-task CAR ordering "
203	            r"remains identical across all conditions (chocolate\_pudding highest, "
204	            r"bbq\_sauce lowest), indicating that avoidance patterns reflect the "
205	            r"demonstration distribution regardless of SDF loss weight. A Phase~2 "
206	            r"ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{"
207	            r"Single seed (s2); computational constraints precluded additional seeds for "
208	            r"this ablation.}, confirming that SDF gradients produce no lasting behavioral "
209	            r"effect."
210	        )
211	    else:
212	        new = fill(
213	            r"Table~\ref{tab:avoidance_source} shows that collision-free demonstrations "
214	            r"alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with "
215	            r"zero frozen episodes and displacement above 0.37\,m, confirming genuine "
216	            r"avoidance. Adding SDF supervision produces no measurable benefit across the "
217	            r"full tested range: LoRA-only CAR (54.67\%) is statistically "
218	            r"indistinguishable from all SDF conditions including $\lambda = 0.1$ "
219	            r"({mean_car}\%, $p = {p_value}$; Appendix~\ref{sec:appendix_null}). "
220	            r"A Phase~2 ablation ($\lambda = 0$ after step 5K) yields "
221	            r"CAR\,=\,57.5\%\footnote{Single seed (s2); computational constraints "
222	            r"precluded additional seeds for this ablation.}, confirming that SDF "
223	            r"gradients produce no lasting behavioral effect. The per-task CAR ordering "
224	            r"is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce "
225	            r"lowest) and invariant to $\lambda$ across a 20$\times$ range, indicating "
226	            r"that avoidance patterns reflect the demonstration distribution rather than "
227	            r"geometric supervision.", v)
228	    R.append(("claim3.tex", "claim3 L27 body", old, new))
229	
230	    # 7. claim3.tex L32-33 dose-response paragraph
231	    hdr = r"\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}"
232	    old_body = (
233	        r"Increasing $\lambda$ by 20$\times$ to 0.1 yields "
234	        r"CAR\,=\,57.00\%\,$\pm$\,2.18 at the 30K checkpoint "
235	        r"(3 seeds: 58.0\%, 58.5\%, 54.5\%), within the null "
236	        r"distribution (mean 54.58\%, $\sigma = 1.93$; permutation "
237	        r"$p = 0.131$\footnote{One-tailed permutation "
238	        r"$p = 0.071$; even with the directional prior that SDF "
239	        r"should not \emph{decrease} CAR, the result remains "
240	        r"non-significant.}). SDF supervision is redundant with the demonstration "
241	        r"signal across the full tested range $\lambda \in [0.005, 0.1]$ "
242	        r"(Figure~\ref{fig:lambda_car}). This result disambiguates the two-level "
243	        r"failure analysis (Section~\ref{sec:conclusion}): because even a "
244	        r"20$\times$ increase in SDF loss weight fails to produce additional "
245	        r"avoidance, the binding constraint is not training signal magnitude but "
246	        r"the structural mismatch between end-effector monitoring and full-body "
247	        r"collision surfaces. Stronger geometric supervision cannot compensate for "
248	        r"supervising the wrong collision surface."
249	    )
250	    old = hdr + "\n" + old_body
251	    if is_c:
252	        new_body = fill(
253	            r"Increasing $\lambda$ by 20$\times$ to 0.1 yields "
254	            r"CAR\,=\,{mean_car}\%\,$\pm$\,{std_car} at the 30K checkpoint "
255	            r"(3 seeds: {s0_car}\%, {s1_car}\%, {s2_car}\%), a modest but "
256	            r"statistically significant departure from the null distribution "
257	            r"(mean 54.58\%, $\sigma = 1.93$; permutation "
258	            r"$p = {p_value}$\footnote{One-tailed permutation "
259	            r"$p = {p_one_value}$; the directional prior that SDF should not "
260	            r"\emph{decrease} CAR supports a one-tailed test, but we report "
261	            r"the conservative two-tailed value in the main text.}). The "
262	            r"effect size of {delta_pp}\,pp is small relative to the $+$26\,pp gain "
263	            r"from LoRA fine-tuning alone, indicating that EE-only SDF supervision "
264	            r"can incrementally augment demonstration-driven avoidance at sufficiently "
265	            r"high loss weights but cannot substitute for it. A stepwise ablation across "
266	            r"six checkpoints (16K--28K) shows no sustained trend prior to 30K "
267	            r"(mean 55.3\%, within 0.4$\sigma$ of the null; "
268	            r"Appendix~\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K "
269	            r"remains identical to all other conditions "
270	            r"(Figure~\ref{fig:lambda_car}), confirming that the dominant avoidance "
271	            r"signal remains the demonstration distribution. The response is thus "
272	            r"dose-dependent: SDF is fully redundant at $\lambda \leq 0.01$ "
273	            r"($p > 0.1$), with a small but detectable effect at $\lambda = 0.1$ "
274	            r"that preserves the same demonstration-driven avoidance fingerprint.", v)
275	    else:
276	        new_body = fill(
277	            r"Increasing $\lambda$ by 20$\times$ to 0.1 yields "
278	            r"CAR\,=\,{mean_car}\%\,$\pm$\,{std_car} at the 30K checkpoint "
279	            r"(3 seeds: {s0_car}\%, {s1_car}\%, {s2_car}\%), within the null "
280	            r"distribution (mean 54.58\%, $\sigma = 1.93$; permutation "
281	            r"$p = {p_value}$\footnote{One-tailed permutation "
282	            r"$p = {p_one_value}$; even with the directional prior that SDF "
283	            r"should not \emph{decrease} CAR, the result remains "
284	            r"non-significant.}). SDF supervision is redundant with the demonstration "
285	            r"signal across the full tested range $\lambda \in [0.005, 0.1]$ "
286	            r"(Figure~\ref{fig:lambda_car}). This result disambiguates the two-level "
287	            r"failure analysis (Section~\ref{sec:conclusion}): because even a "
288	            r"20$\times$ increase in SDF loss weight fails to produce additional "
289	            r"avoidance, the binding constraint is not training signal magnitude but "
290	            r"the structural mismatch between end-effector monitoring and full-body "
291	            r"collision surfaces. Stronger geometric supervision cannot compensate for "
292	            r"supervising the wrong collision surface.", v)
293	    R.append(("claim3.tex", "claim3 L32-33 dose-response", old, hdr + "\n" + new_body))
294	
295	    # 8. claim3.tex L38 figure caption
296	    old = (
297	        r"\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. "
298	        r"$\lambda = 0$: LoRA-only. All tested $\lambda$ values remain within "
299	        r"the null band ($p > 0.05$), confirming full redundancy of EE-only SDF "
300	        r"supervision across a 20$\times$ loss-weight range.}"
301	    )
302	    if is_c:
303	        new = fill(
304	            r"\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. "
305	            r"$\lambda = 0$: LoRA-only. Low $\lambda$ ($\leq 0.01$) remains within "
306	            r"the null band; $\lambda = 0.1$ ({mean_car}\%, 3 seeds) shows a modest "
307	            r"but significant departure (permutation $p = {p_value}$, {delta_pp}\,pp "
308	            r"effect size) whose per-task avoidance pattern still matches the "
309	            r"demonstration distribution.}", v)
310	    else:
311	        new = (
312	            r"\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. "
313	            r"$\lambda = 0$: LoRA-only. All tested $\lambda$ values remain within "
314	            r"the null band ($p > 0.05$), confirming full redundancy of EE-only SDF "
315	            r"supervision across a 20$\times$ loss-weight range.}"
316	        )
317	    R.append(("claim3.tex", "claim3 L38 fig caption", old, new))
318	
319	    # 9. discussion.tex L3 scope (Scenario C only)
320	    if is_c:
321	        old = (
322	            r"and collision-free demonstrations, not geometric supervision, account "
323	            r"for the measured avoidance gains (\S\ref{sec:avoidance_source})."
324	        )
325	        new = (
326	            r"and collision-free demonstrations account for nearly all measured "
327	            r"avoidance gains, with EE-only SDF contributing at most a modest "
328	            r"increment at high loss weights (\S\ref{sec:avoidance_source})."
329	        )
330	        R.append(("discussion.tex", "discussion L3 scope", old, new))
331	
332	    # 10. discussion.tex L6
333	    old = (
334	        r"Even at $\lambda = 0.1$ (20$\times$ the lowest tested weight), CAR "
335	        r"remains within the null distribution ($p = 0.131$), confirming "
336	        r"that Level~A signal masking is not the binding constraint---the failure "
337	        r"is architectural."
338	    )
339	    if is_c:
340	        new = fill(
341	            r"At $\lambda \leq 0.01$, SDF is fully redundant; at $\lambda = 0.1$, "
342	            r"a modest {delta_pp}\,pp effect emerges ($p = {p_value}$) but preserves "
343	            r"the same demonstration-driven avoidance pattern, suggesting that "
344	            r"EE-only SDF can weakly augment---but not redirect---the implicit signal "
345	            r"at sufficiently high loss weights.", v)
346	    else:
347	        new = fill(
348	            r"Even at $\lambda = 0.1$ (20$\times$ the lowest tested weight), CAR "
349	            r"remains within the null distribution ($p = {p_value}$), confirming "
350	            r"that Level~A signal masking is not the binding constraint---the failure "
351	            r"is architectural.", v)
352	    R.append(("discussion.tex", "discussion L6", old, new))
353	
354	    # 11. discussion.tex L12 limitation
355	    old = r"Full-body SDF remains untested."
356	    if is_c:
357	        new = fill(
358	            r"Full-body SDF remains untested. "
359	            r"The $\lambda = 0.1$ effect ({delta_pp}\,pp, $p = {p_value}$, $n = 3$) "
360	            r"is statistically significant but small; whether this modest gain "
361	            r"justifies the computational cost of SDF supervision requires "
362	            r"task-specific cost-benefit analysis.", v)
363	    else:
364	        new = r"Full-body SDF remains untested."
365	    R.append(("discussion.tex", "discussion L12 limitation", old, new))
366	
367	    return R
368	
369	
370	def main():
371	    parser = argparse.ArgumentParser(
372	        description="Auto-switch paper for lambda=0.1 s2 30K result")
373	    parser.add_argument("--s2-car", type=float, required="--verify" not in sys.argv)
374	    parser.add_argument("--s2-tsr", type=float, default=None)
375	    parser.add_argument("--dry-run", action="store_true")
376	    parser.add_argument("--verify", action="store_true",
377	                        help="Check all old_strings match current .tex files")
378	    args = parser.parse_args()
379	
380	    if args.verify:
381	        if not PAPER_DIR.exists():
382	            print(f"ERROR: paper dir not found: {PAPER_DIR}")
383	            sys.exit(1)
384	        dummy_v = {k: "X" for k in [
385	            "s0_car", "s1_car", "s2_car", "mean_car", "std_car",
386	            "tsr_mean", "tsr_std", "p_value", "p_one_value", "z_value", "delta_pp"]}
387	        all_ok = True
388	        for scenario in ("B", "C"):
389	            replacements = get_replacements(scenario, dummy_v)
390	            print(f"--- Scenario {scenario} ({len(replacements)} items) ---")
391	            for filename, label, old, new in replacements:
392	                fpath = PAPER_DIR / filename
393	                if not fpath.exists():
394	                    print(f"  [MISSING] {label:35s} {filename}")
395	                    all_ok = False
396	                    continue
397	                content = fpath.read_text()
398	                if old in content:
399	                    print(f"  [OK]      {label:35s} {filename}")
400	                else:
401	                    print(f"  [MISMATCH]{label:35s} {filename}")
402	                    print(f"            Expected: {old[:80]}...")
403	                    all_ok = False
404	        sys.exit(0 if all_ok else 1)
405	
406	    cars = [S0_CAR, S1_CAR, args.s2_car]
407	    car_mean = mean(cars)
408	    car_std = std_b(cars)
409	
410	    if args.s2_tsr is not None:
411	        tsrs = [S0_TSR, S1_TSR, args.s2_tsr]
412	    else:
413	        tsrs = [S0_TSR, S1_TSR]
414	        print("NOTE: --s2-tsr not provided, using 2-seed TSR")
415	    tsr_mean = mean(tsrs)
416	    tsr_std = std_b(tsrs)
417	
418	    p_one, p_two, n_combos = perm_test(NULL_VALUES, cars)
419	    z = (car_mean - NULL_MEAN) / NULL_STD
420	    delta = car_mean - NULL_MEAN
421	
422	    scenario = "C" if p_one < 0.05 else "B"
423	
424	    v = {
425	        "s0_car": f"{S0_CAR:.1f}",
426	        "s1_car": f"{S1_CAR:.1f}",
427	        "s2_car": f"{args.s2_car:.1f}",
428	        "mean_car": f"{car_mean:.2f}",
429	        "std_car": f"{car_std:.2f}",
430	        "tsr_mean": f"{tsr_mean:.1f}",
431	        "tsr_std": f"{tsr_std:.1f}",
432	        "p_value": f"{p_two:.3f}",
433	        "p_one_value": f"{p_one:.3f}",
434	        "z_value": f"{z:.2f}",
435	        "delta_pp": f"{delta:.1f}",
436	    }
437	
438	    print("=" * 60)
439	    print("  PAPER SWITCH — lambda=0.1 s2 30K")
440	    print("=" * 60)
441	    print(f"  Input:     s2_car={args.s2_car}, s2_tsr={args.s2_tsr}")
442	    print(f"  3-seed:    CAR = {v['mean_car']} +/- {v['std_car']}")
443	    print(f"             TSR = {v['tsr_mean']} +/- {v['tsr_std']} ({len(tsrs)} seeds)")
444	    print(f"  Perm test: C({len(NULL_VALUES)+len(cars)},{len(cars)}) = {n_combos}")
445	    print(f"             p_one = {v['p_one_value']}  {'<' if p_one < 0.05 else '>='} 0.05")
446	    print(f"             p_two = {v['p_value']}")
447	    print(f"  Z-score:   {v['z_value']}")
448	    print(f"  Delta:     +{v['delta_pp']} pp")
449	    print(f"  Scenario:  {scenario}  "
450	          f"{'(modest but significant)' if scenario == 'C' else '(full redundancy)'}")
451	    print()
452	
453	    if not PAPER_DIR.exists():
454	        print(f"ERROR: paper dir not found: {PAPER_DIR}")
455	        sys.exit(1)
456	
457	    replacements = get_replacements(scenario, v)
458	
459	    files_content = {}
460	    counts = {}
461	
462	    for filename, label, old, new in replacements:
463	        fpath = PAPER_DIR / filename
464	        if filename not in files_content:
465	            if not fpath.exists():
466	                print(f"  !! {filename} not found")
467	                continue
468	            files_content[filename] = fpath.read_text()
469	            counts[filename] = 0
470	
471	        content, ok = safe_replace(files_content[filename], old, new, label)
472	        files_content[filename] = content
473	        if ok:
474	            counts[filename] += 1
475	            status = "ok"
476	        else:
477	            status = "FAIL"
478	        print(f"  [{status:4s}] {label:35s} {filename}")
479	
480	    total = sum(counts.values())
481	    n_files = sum(1 for c in counts.values() if c > 0)
482	    expected = len(replacements)
483	    print(f"\n  {total}/{expected} replacements in {n_files} files")
484	
485	    if args.dry_run:
486	        print("\n  DRY RUN — no files modified")
487	        return
488	
489	    for filename, content in files_content.items():
490	        fpath = PAPER_DIR / filename
491	        fpath.write_text(content)
492	        print(f"  Wrote {filename} ({counts[filename]} changes)")
493	
494	    print("\nCompiling PDF...")
495	    try:
496	        result = subprocess.run(
497	            ["latexmk", "-pdf", "-interaction=nonstopmode", "main.tex"],
498	            cwd=PAPER_DIR, capture_output=True, text=True, timeout=120)
499	        if result.returncode == 0:
500	            print("  PDF compiled OK")
501	        else:
502	            print("  PDF compilation FAILED")
503	            err = result.stderr or result.stdout or ""
504	            for line in err.split("\n")[-10:]:
505	                if line.strip():
506	                    print(f"    {line}")
507	    except FileNotFoundError:
508	        print("  latexmk not found — skipping PDF compilation")
509	    except subprocess.TimeoutExpired:
510	        print("  PDF compilation timed out (120s)")
511	
512	
513	if __name__ == "__main__":
514	    main()
515	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "bc8ec6eb-8067-4e4e-ae03-6da65e415405",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_switch.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Auto-switch paper text based on λ=0.1 s2 30K eval result.\n\nUsage:\n  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0 --dry-run\n  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0\n\"\"\"\nimport argparse\nimport subprocess\nimport sys\nfrom itertools import combinations\nfrom math import comb, sqrt\nfrom pathlib import Path\n\nNULL_VALUES = [56.5, 52.5, 55, 57, 54, 52.5]\nNULL_MEAN = sum(NULL_VALUES) / len(NULL_VALUES)\nNULL_STD = (sum((x - NULL_MEAN) ** 2 for x in NULL_VALUES) / 5) ** 0.5\n\nS0_CAR, S1_CAR = 58.0, 58.5\nS0_TSR, S1_TSR = 47.0, 49.0\n\nPAPER_DIR = Path(__file__).resolve().parent.parent / \"docs\" / \"paper\"\n\n\ndef mean(v):\n    return sum(v) / len(v)\n\n\ndef std_b(v):\n    m = mean(v)\n    return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5\n\n\ndef perm_test(null_vals, treat_vals):\n    pool = null_vals + treat_vals\n    k = len(treat_vals)\n    obs = mean(treat_vals)\n    mu = mean(pool)\n    dev = abs(obs - mu)\n    n = comb(len(pool), k)\n    ge = tw = 0\n    for c in combinations(pool, k):\n        m = mean(c)\n        if m >= obs:\n            ge += 1\n        if abs(m - mu) >= dev - 1e-12:\n            tw += 1\n    return ge / n, tw / n, n\n\n\ndef fill(tpl, vals):\n    for k, v in vals.items():\n        tpl = tpl.replace(\"{\" + k + \"}\", str(v))\n    return tpl\n\n\ndef safe_replace(content, old, new, label):\n    n = content.count(old)\n    if n == 0:\n        print(f\"  !! [{label}] NOT FOUND\")\n        return content, False\n    if n > 1:\n        print(f\"  !! [{label}] found {n}x\")\n        return content, False\n    return content.replace(old, new), True\n\n\ndef get_replacements(scenario, v):\n    R = []\n    is_c = scenario == \"C\"\n\n    # 1. abstract.tex L5 (training results)\n    old = (\n        r\"collision-free demonstrations alone account for all measured avoidance \"\n        r\"gains (${\\sim}$26 percentage points). SDF supervision adds no measurable \"\n        r\"benefit across the full tested range $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"\n        r\"($p > 0.05$ for all; $\\lambda = 0.1$: 57.00\\%$\\,\\pm\\,$2.18, 3 seeds).\"\n    )\n    if is_c:\n        new = fill(\n            r\"collision-free demonstrations alone account for nearly all measured \"\n            r\"avoidance gains (${\\sim}$26 percentage points). SDF supervision adds no \"\n            r\"significant benefit at $\\lambda \\leq 0.01$ ($p > 0.1$); at \"\n            r\"$\\lambda = 0.1$, a modest but statistically significant increase emerges \"\n            r\"({mean_car}\\%$\\,\\pm\\,${std_car}, permutation $p = {p_value}$, 3 seeds), \"\n            r\"though the effect size ({delta_pp}\\,pp) is small relative to the \"\n            r\"$+$26\\,pp gain from fine-tuning alone.\", v)\n    else:\n        new = fill(\n            r\"collision-free demonstrations alone account for all measured avoidance \"\n            r\"gains (${\\sim}$26 percentage points). SDF supervision adds no measurable \"\n            r\"benefit across the full tested range $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"\n            r\"($p > 0.05$ for all; $\\lambda = 0.1$: {mean_car}\\%$\\,\\pm\\,${std_car}, \"\n            r\"3 seeds).\", v)\n    R.append((\"abstract.tex\", \"abstract L5 training\", old, new))\n\n    # 2. abstract.tex L6 (concluding sentence)\n    old = (\n        r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n        r\"EE-only geometric supervision is fully redundant across a 20$\\times$ \"\n        r\"loss-weight range, confirming that collision avoidance arises from \"\n        r\"demonstration data, not geometric supervision.\"\n    )\n    if is_c:\n        new = (\n            r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n            r\"Even at the highest tested loss weight, the modest SDF effect is dwarfed by \"\n            r\"demonstration-driven avoidance and cannot overcome the structural limitation \"\n            r\"of EE-only supervision.\"\n        )\n    else:\n        new = (\n            r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n            r\"EE-only geometric supervision is fully redundant across a 20$\\times$ \"\n            r\"loss-weight range, confirming that collision avoidance arises from \"\n            r\"demonstration data, not geometric supervision.\"\n        )\n    R.append((\"abstract.tex\", \"abstract L6 conclusion\", old, new))\n\n    # 3. claim3.tex L3 scope sentence\n    old = (\n        r\"We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of \"\n        r\"loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all \"\n        r\"evaluated at the 30K-step checkpoint.\"\n    )\n    if is_c:\n        new = (\n            r\"We compare LoRA-only against LoRA+SDF at three loss weights \"\n            r\"($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at \"\n            r\"the 30K-step checkpoint.\"\n        )\n    else:\n        new = (\n            r\"We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of \"\n            r\"loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all \"\n            r\"evaluated at the 30K-step checkpoint.\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L3 scope\", old, new))\n\n    # 4. claim3.tex L7 table caption\n    old = (\n        r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no \"\n        r\"measurable CAR beyond LoRA-only across the full tested range \"\n        r\"$\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"\n        r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\"\n    )\n    if is_c:\n        new = fill(\n            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF at \"\n            r\"$\\lambda \\leq 0.01$ adds no measurable CAR beyond LoRA-only \"\n            r\"($p > 0.1$). At $\\lambda = 0.1$, a modest increase reaches \"\n            r\"statistical significance ($z = {z_value}$, permutation \"\n            r\"$p = {p_value}$, $n{=}3$), though the effect size ({delta_pp}\\,pp) \"\n            r\"is small relative to the $+$26\\,pp LoRA gain. All fine-tuned models \"\n            r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\", v)\n    else:\n        new = (\n            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no \"\n            r\"measurable CAR beyond LoRA-only across the full tested range \"\n            r\"$\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"\n            r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L7 caption\", old, new))\n\n    # 5. claim3.tex L20 table row\n    old = (\n        r\"LoRA+SDF $\\lambda{=}0.1$ & 3 & \"\n        r\"50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\"\n    )\n    new = fill(\n        r\"LoRA+SDF $\\lambda{=}0.1$ & 3 & \"\n        r\"{tsr_mean}\\,$\\pm$\\,{tsr_std} & {mean_car}\\,$\\pm$\\,{std_car} & 0.394 \\\\\", v)\n    R.append((\"claim3.tex\", \"claim3 L20 table row\", old, new))\n\n    # 6. claim3.tex L27 body paragraph\n    old = (\n        r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n        r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n        r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n        r\"avoidance. Adding SDF supervision produces no measurable benefit across the \"\n        r\"full tested range: LoRA-only CAR (54.67\\%) is statistically \"\n        r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"\n        r\"(57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). \"\n        r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"\n        r\"CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints \"\n        r\"precluded additional seeds for this ablation.}, confirming that SDF \"\n        r\"gradients produce no lasting behavioral effect. The per-task CAR ordering \"\n        r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"\n        r\"lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating \"\n        r\"that avoidance patterns reflect the demonstration distribution rather than \"\n        r\"geometric supervision.\"\n    )\n    if is_c:\n        new = (\n            r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n            r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n            r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n            r\"avoidance. At $\\lambda \\leq 0.01$, SDF supervision produces no measurable \"\n            r\"benefit: LoRA-only CAR (54.67\\%) is within 0.17\\,pp of $\\lambda = 0.005$ \"\n            r\"and statistically indistinguishable from $\\lambda = 0.01$ (56.33\\%, \"\n            r\"$p > 0.1$; Appendix~\\ref{sec:appendix_null}). At $\\lambda = 0.1$, a modest \"\n            r\"increase emerges (Section~\\ref{sec:lambda_high}), but per-task CAR ordering \"\n            r\"remains identical across all conditions (chocolate\\_pudding highest, \"\n            r\"bbq\\_sauce lowest), indicating that avoidance patterns reflect the \"\n            r\"demonstration distribution regardless of SDF loss weight. A Phase~2 \"\n            r\"ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{\"\n            r\"Single seed (s2); computational constraints precluded additional seeds for \"\n            r\"this ablation.}, confirming that SDF gradients produce no lasting behavioral \"\n            r\"effect.\"\n        )\n    else:\n        new = fill(\n            r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n            r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n            r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n            r\"avoidance. Adding SDF supervision produces no measurable benefit across the \"\n            r\"full tested range: LoRA-only CAR (54.67\\%) is statistically \"\n            r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"\n            r\"({mean_car}\\%, $p = {p_value}$; Appendix~\\ref{sec:appendix_null}). \"\n            r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"\n            r\"CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints \"\n            r\"precluded additional seeds for this ablation.}, confirming that SDF \"\n            r\"gradients produce no lasting behavioral effect. The per-task CAR ordering \"\n            r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"\n            r\"lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating \"\n            r\"that avoidance patterns reflect the demonstration distribution rather than \"\n            r\"geometric supervision.\", v)\n    R.append((\"claim3.tex\", \"claim3 L27 body\", old, new))\n\n    # 7. claim3.tex L32-33 dose-response paragraph\n    hdr = r\"\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\"\n    old_body = (\n        r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n        r\"CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint \"\n        r\"(3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null \"\n        r\"distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n        r\"$p = 0.131$\\footnote{One-tailed permutation \"\n        r\"$p = 0.071$; even with the directional prior that SDF \"\n        r\"should not \\emph{decrease} CAR, the result remains \"\n        r\"non-significant.}). SDF supervision is redundant with the demonstration \"\n        r\"signal across the full tested range $\\lambda \\in [0.005, 0.1]$ \"\n        r\"(Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level \"\n        r\"failure analysis (Section~\\ref{sec:conclusion}): because even a \"\n        r\"20$\\times$ increase in SDF loss weight fails to produce additional \"\n        r\"avoidance, the binding constraint is not training signal magnitude but \"\n        r\"the structural mismatch between end-effector monitoring and full-body \"\n        r\"collision surfaces. Stronger geometric supervision cannot compensate for \"\n        r\"supervising the wrong collision surface.\"\n    )\n    old = hdr + \"\\n\" + old_body\n    if is_c:\n        new_body = fill(\n            r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n            r\"CAR\\,=\\,{mean_car}\\%\\,$\\pm$\\,{std_car} at the 30K checkpoint \"\n            r\"(3 seeds: {s0_car}\\%, {s1_car}\\%, {s2_car}\\%), a modest but \"\n            r\"statistically significant departure from the null distribution \"\n            r\"(mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n            r\"$p = {p_value}$\\footnote{One-tailed permutation \"\n            r\"$p = {p_one_value}$; the directional prior that SDF should not \"\n            r\"\\emph{decrease} CAR supports a one-tailed test, but we report \"\n            r\"the conservative two-tailed value in the main text.}). The \"\n            r\"effect size of {delta_pp}\\,pp is small relative to the $+$26\\,pp gain \"\n            r\"from LoRA fine-tuning alone, indicating that EE-only SDF supervision \"\n            r\"can incrementally augment demonstration-driven avoidance at sufficiently \"\n            r\"high loss weights but cannot substitute for it. A stepwise ablation across \"\n            r\"six checkpoints (16K--28K) shows no sustained trend prior to 30K \"\n            r\"(mean 55.3\\%, within 0.4$\\sigma$ of the null; \"\n            r\"Appendix~\\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K \"\n            r\"remains identical to all other conditions \"\n            r\"(Figure~\\ref{fig:lambda_car}), confirming that the dominant avoidance \"\n            r\"signal remains the demonstration distribution. The response is thus \"\n            r\"dose-dependent: SDF is fully redundant at $\\lambda \\leq 0.01$ \"\n            r\"($p > 0.1$), with a small but detectable effect at $\\lambda = 0.1$ \"\n            r\"that preserves the same demonstration-driven avoidance fingerprint.\", v)\n    else:\n        new_body = fill(\n            r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n            r\"CAR\\,=\\,{mean_car}\\%\\,$\\pm$\\,{std_car} at the 30K checkpoint \"\n            r\"(3 seeds: {s0_car}\\%, {s1_car}\\%, {s2_car}\\%), within the null \"\n            r\"distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n            r\"$p = {p_value}$\\footnote{One-tailed permutation \"\n            r\"$p = {p_one_value}$; even with the directional prior that SDF \"\n            r\"should not \\emph{decrease} CAR, the result remains \"\n            r\"non-significant.}). SDF supervision is redundant with the demonstration \"\n            r\"signal across the full tested range $\\lambda \\in [0.005, 0.1]$ \"\n            r\"(Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level \"\n            r\"failure analysis (Section~\\ref{sec:conclusion}): because even a \"\n            r\"20$\\times$ increase in SDF loss weight fails to produce additional \"\n            r\"avoidance, the binding constraint is not training signal magnitude but \"\n            r\"the structural mismatch between end-effector monitoring and full-body \"\n            r\"collision surfaces. Stronger geometric supervision cannot compensate for \"\n            r\"supervising the wrong collision surface.\", v)\n    R.append((\"claim3.tex\", \"claim3 L32-33 dose-response\", old, hdr + \"\\n\" + new_body))\n\n    # 8. claim3.tex L38 figure caption\n    old = (\n        r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n        r\"$\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within \"\n        r\"the null band ($p > 0.05$), confirming full redundancy of EE-only SDF \"\n        r\"supervision across a 20$\\times$ loss-weight range.}\"\n    )\n    if is_c:\n        new = fill(\n            r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n            r\"$\\lambda = 0$: LoRA-only. Low $\\lambda$ ($\\leq 0.01$) remains within \"\n            r\"the null band; $\\lambda = 0.1$ ({mean_car}\\%, 3 seeds) shows a modest \"\n            r\"but significant departure (permutation $p = {p_value}$, {delta_pp}\\,pp \"\n            r\"effect size) whose per-task avoidance pattern still matches the \"\n            r\"demonstration distribution.}\", v)\n    else:\n        new = (\n            r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n            r\"$\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within \"\n            r\"the null band ($p > 0.05$), confirming full redundancy of EE-only SDF \"\n            r\"supervision across a 20$\\times$ loss-weight range.}\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L38 fig caption\", old, new))\n\n    # 9. discussion.tex L3 scope (Scenario C only)\n    if is_c:\n        old = (\n            r\"and collision-free demonstrations, not geometric supervision, account \"\n            r\"for the measured avoidance gains (\\S\\ref{sec:avoidance_source}).\"\n        )\n        new = (\n            r\"and collision-free demonstrations account for nearly all measured \"\n            r\"avoidance gains, with EE-only SDF contributing at most a modest \"\n            r\"increment at high loss weights (\\S\\ref{sec:avoidance_source}).\"\n        )\n        R.append((\"discussion.tex\", \"discussion L3 scope\", old, new))\n\n    # 10. discussion.tex L6\n    old = (\n        r\"Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR \"\n        r\"remains within the null distribution ($p = 0.131$), confirming \"\n        r\"that Level~A signal masking is not the binding constraint---the failure \"\n        r\"is architectural.\"\n    )\n    if is_c:\n        new = fill(\n            r\"At $\\lambda \\leq 0.01$, SDF is fully redundant; at $\\lambda = 0.1$, \"\n            r\"a modest {delta_pp}\\,pp effect emerges ($p = {p_value}$) but preserves \"\n            r\"the same demonstration-driven avoidance pattern, suggesting that \"\n            r\"EE-only SDF can weakly augment---but not redirect---the implicit signal \"\n            r\"at sufficiently high loss weights.\", v)\n    else:\n        new = fill(\n            r\"Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR \"\n            r\"remains within the null distribution ($p = {p_value}$), confirming \"\n            r\"that Level~A signal masking is not the binding constraint---the failure \"\n            r\"is architectural.\", v)\n    R.append((\"discussion.tex\", \"discussion L6\", old, new))\n\n    # 11. discussion.tex L12 limitation\n    old = r\"Full-body SDF remains untested.\"\n    if is_c:\n        new = fill(\n            r\"Full-body SDF remains untested. \"\n            r\"The $\\lambda = 0.1$ effect ({delta_pp}\\,pp, $p = {p_value}$, $n = 3$) \"\n            r\"is statistically significant but small; whether this modest gain \"\n            r\"justifies the computational cost of SDF supervision requires \"\n            r\"task-specific cost-benefit analysis.\", v)\n    else:\n        new = r\"Full-body SDF remains untested.\"\n    R.append((\"discussion.tex\", \"discussion L12 limitation\", old, new))\n\n    return R\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Auto-switch paper for lambda=0.1 s2 30K result\")\n    parser.add_argument(\"--s2-car\", type=float, required=\"--verify\" not in sys.argv)\n    parser.add_argument(\"--s2-tsr\", type=float, default=None)\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--verify\", action=\"store_true\",\n                        help=\"Check all old_strings match current .tex files\")\n    args = parser.parse_args()\n\n    if args.verify:\n        if not PAPER_DIR.exists():\n            print(f\"ERROR: paper dir not found: {PAPER_DIR}\")\n            sys.exit(1)\n        dummy_v = {k: \"X\" for k in [\n            \"s0_car\", \"s1_car\", \"s2_car\", \"mean_car\", \"std_car\",\n            \"tsr_mean\", \"tsr_std\", \"p_value\", \"p_one_value\", \"z_value\", \"delta_pp\"]}\n        all_ok = True\n        for scenario in (\"B\", \"C\"):\n            replacements = get_replacements(scenario, dummy_v)\n            print(f\"--- Scenario {scenario} ({len(replacements)} items) ---\")\n            for filename, label, old, new in replacements:\n                fpath = PAPER_DIR / filename\n                if not fpath.exists():\n                    print(f\"  [MISSING] {label:35s} {filename}\")\n                    all_ok = False\n                    continue\n                content = fpath.read_text()\n                if old in content:\n                    print(f\"  [OK]      {label:35s} {filename}\")\n                else:\n                    print(f\"  [MISMATCH]{label:35s} {filename}\")\n                    print(f\"            Expected: {old[:80]}...\")\n                    all_ok = False\n        sys.exit(0 if all_ok else 1)\n\n    cars = [S0_CAR, S1_CAR, args.s2_car]\n    car_mean = mean(cars)\n    car_std = std_b(cars)\n\n    if args.s2_tsr is not None:\n        tsrs = [S0_TSR, S1_TSR, args.s2_tsr]\n    else:\n        tsrs = [S0_TSR, S1_TSR]\n        print(\"NOTE: --s2-tsr not provided, using 2-seed TSR\")\n    tsr_mean = mean(tsrs)\n    tsr_std = std_b(tsrs)\n\n    p_one, p_two, n_combos = perm_test(NULL_VALUES, cars)\n    z = (car_mean - NULL_MEAN) / NULL_STD\n    delta = car_mean - NULL_MEAN\n\n    scenario = \"C\" if p_one < 0.05 else \"B\"\n\n    v = {\n        \"s0_car\": f\"{S0_CAR:.1f}\",\n        \"s1_car\": f\"{S1_CAR:.1f}\",\n        \"s2_car\": f\"{args.s2_car:.1f}\",\n        \"mean_car\": f\"{car_mean:.2f}\",\n        \"std_car\": f\"{car_std:.2f}\",\n        \"tsr_mean\": f\"{tsr_mean:.1f}\",\n        \"tsr_std\": f\"{tsr_std:.1f}\",\n        \"p_value\": f\"{p_two:.3f}\",\n        \"p_one_value\": f\"{p_one:.3f}\",\n        \"z_value\": f\"{z:.2f}\",\n        \"delta_pp\": f\"{delta:.1f}\",\n    }\n\n    print(\"=\" * 60)\n    print(\"  PAPER SWITCH — lambda=0.1 s2 30K\")\n    print(\"=\" * 60)\n    print(f\"  Input:     s2_car={args.s2_car}, s2_tsr={args.s2_tsr}\")\n    print(f\"  3-seed:    CAR = {v['mean_car']} +/- {v['std_car']}\")\n    print(f\"             TSR = {v['tsr_mean']} +/- {v['tsr_std']} ({len(tsrs)} seeds)\")\n    print(f\"  Perm test: C({len(NULL_VALUES)+len(cars)},{len(cars)}) = {n_combos}\")\n    print(f\"             p_one = {v['p_one_value']}  {'<' if p_one < 0.05 else '>='} 0.05\")\n    print(f\"             p_two = {v['p_value']}\")\n    print(f\"  Z-score:   {v['z_value']}\")\n    print(f\"  Delta:     +{v['delta_pp']} pp\")\n    print(f\"  Scenario:  {scenario}  \"\n          f\"{'(modest but significant)' if scenario == 'C' else '(full redundancy)'}\")\n    print()\n\n    if not PAPER_DIR.exists():\n        print(f\"ERROR: paper dir not found: {PAPER_DIR}\")\n        sys.exit(1)\n\n    replacements = get_replacements(scenario, v)\n\n    files_content = {}\n    counts = {}\n\n    for filename, label, old, new in replacements:\n        fpath = PAPER_DIR / filename\n        if filename not in files_content:\n            if not fpath.exists():\n                print(f\"  !! {filename} not found\")\n                continue\n            files_content[filename] = fpath.read_text()\n            counts[filename] = 0\n\n        content, ok = safe_replace(files_content[filename], old, new, label)\n        files_content[filename] = content\n        if ok:\n            counts[filename] += 1\n            status = \"ok\"\n        else:\n            status = \"FAIL\"\n        print(f\"  [{status:4s}] {label:35s} {filename}\")\n\n    total = sum(counts.values())\n    n_files = sum(1 for c in counts.values() if c > 0)\n    expected = len(replacements)\n    print(f\"\\n  {total}/{expected} replacements in {n_files} files\")\n\n    if args.dry_run:\n        print(\"\\n  DRY RUN — no files modified\")\n        return\n\n    for filename, content in files_content.items():\n        fpath = PAPER_DIR / filename\n        fpath.write_text(content)\n        print(f\"  Wrote {filename} ({counts[filename]} changes)\")\n\n    print(\"\\nCompiling PDF...\")\n    try:\n        result = subprocess.run(\n            [\"latexmk\", \"-pdf\", \"-interaction=nonstopmode\", \"main.tex\"],\n            cwd=PAPER_DIR, capture_output=True, text=True, timeout=120)\n        if result.returncode == 0:\n            print(\"  PDF compiled OK\")\n        else:\n            print(\"  PDF compilation FAILED\")\n            err = result.stderr or result.stdout or \"\"\n            for line in err.split(\"\\n\")[-10:]:\n                if line.strip():\n                    print(f\"    {line}\")\n    except FileNotFoundError:\n        print(\"  latexmk not found — skipping PDF compilation\")\n    except subprocess.TimeoutExpired:\n        print(\"  PDF compilation timed out (120s)\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 515,
      "startLine": 1,
      "totalLines": 515
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_014xeUHM3M7wSnvsopHCRN3u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "201ad116-fb6a-477a-b425-1ea312a1b570",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9JJYBmMn5yitSNupCBGXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13665,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13665
      },
      "output_tokens": 30,
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

_source line 9 · 2026-05-28T05:35:17.319Z_

<details><summary>↩ Tool result · `toolu_014xeUHM3M7wSnvsopHCRN3u`</summary>

```text
1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across the full tested range $\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 3 & 51.5\,$\pm$\,0.0 & 54.67\,$\pm$\,2.02 & 0.391 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$ & 3 & 50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ (57.00\%, $p = 0.131$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce lowest) and invariant to $\lambda$ across a 20$\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.
27	
28	\paragraph{CAR--TSR trade-off.}\label{sec:tsr_collapse}
29	Fine-tuning degrades TSR by ${\sim}$18--20\,pp (71.5\% $\to$ 51.5--54.0\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\,0.37\,m displacement and 0\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.
30	
31	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
32	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,57.00\%\,$\pm$\,2.18 at the 30K checkpoint (3 seeds: 58.0\%, 58.5\%, 54.5\%), within the null distribution (mean 54.58\%, $\sigma = 1.93$; permutation $p = 0.131$\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \emph{decrease} CAR, the result remains non-significant.}). SDF supervision is redundant with the demonstration signal across the full tested range $\lambda \in [0.005, 0.1]$ (Figure~\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\ref{sec:conclusion}): because even a 20$\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.
33	
34	\begin{figure}[t]
35	\centering
36	\includegraphics[width=0.85\linewidth]{fig5_lambda_curve}
37	\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. All tested $\lambda$ values remain within the null band ($p > 0.05$), confirming full redundancy of EE-only SDF supervision across a 20$\times$ loss-weight range.}
38	\label{fig:lambda_car}
39	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "375538e8-5fce-4a0f-93ff-1b55dd7e5d5f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
      "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across the full tested range $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 3 & 51.5\\,$\\pm$\\,0.0 & 54.67\\,$\\pm$\\,2.02 & 0.391 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$ & 3 & 50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$18--20\\,pp (71.5\\% $\\to$ 51.5--54.0\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within the null band ($p > 0.05$), confirming full redundancy of EE-only SDF supervision across a 20$\\times$ loss-weight range.}\n\\label{fig:lambda_car}\n\\end{figure}",
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01FyaF5NHfhTQjHd85ssvPms`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "9df1b320-d44b-42bb-94d4-a1c9b003765e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9JJYBmMn5yitSNupCBGXR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13665,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13665
      },
      "output_tokens": 30,
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

_source line 11 · 2026-05-28T05:35:17.869Z_

<details><summary>↩ Tool result · `toolu_01FyaF5NHfhTQjHd85ssvPms`</summary>

```text
1	\section{Displacement Distribution}
2	\label{sec:appendix_displacement}
3	
4	\begin{figure}[h]
5	\centering
6	\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
7	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
8	\label{fig:displacement}
9	\end{figure}
10	
11	\section{Displacement Threshold Sensitivity Analysis}
12	\label{sec:appendix_threshold}
13	
14	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% frozen rate even at the most conservative setting.
15	
16	\begin{table}[h]
17	\centering
18	\caption{Frozen rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
19	\label{tab:threshold_sensitivity}
20	\begin{tabular}{lccc}
21	\toprule
22	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
23	\midrule
24	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
25	0.1 mm  & 99.6 & 0.0 & 0.0 \\
26	1.0 mm  & 100.0 & 0.0 & 0.0 \\
27	10 mm   & 100.0 & 0.0 & 0.0 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as frozen, while all Pi0.5 episodes remain above threshold at every level tested.
33	
34	Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\tau_d \in [2, 200]$\,mm. At $\tau_d = 300$\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\,mm), causing $\leq$0.5\,pp deviation. Our conclusions hold across the entire tested range.
35	
36	\begin{table}[h]
37	\centering
38	\caption{dfCAR (\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\tau_d \in [2, 200]$\,mm; at $\tau_d = 300$\,mm, at most 2 episodes are excluded.}
39	\label{tab:dfcar_threshold}
40	\vspace{2pt}
41	\footnotesize
42	\begin{tabular}{lcccccccc}
43	\toprule
44	& \multicolumn{8}{c}{$\tau_d$ (mm)} \\
45	\cmidrule(lr){2-9}
46	Condition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\
47	\midrule
48	LoRA s0            & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\
49	LoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\
50	SDF $\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\
51	SDF $\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\
52	SDF $\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\
53	SDF $\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\
54	SDF $\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\
55	SDF $\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\
56	\bottomrule
57	\end{tabular}
58	\end{table}
59	
60	
61	\section{Per-Task TSR Breakdown}\label{sec:appendix_tsr_pertask}
62	
63	Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
64	
65	\begin{table}[h]
66	\centering
67	\caption{Per-task TSR (\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\,=\,71.5\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}
68	\label{tab:per_task_tsr}
69	\vspace{2pt}
70	\small
71	\begin{tabular}{lcccc}
72	\toprule
73	Task & Pi0.5 Base & LoRA-only & SDF $\lambda{=}0.005$ & SDF $\lambda{=}0.01$ \\
74	 & (seed\,=\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\
75	\midrule
76	Orange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\
77	Choco.\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\
78	Milk              & 66.0 & 44.7 & 35.3 & 48.7 \\
79	BBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\
80	\midrule
81	Mean              & 71.5 & 51.5 & 54.0 & 53.8 \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	\section{Per-Task CAR Breakdown}\label{sec:appendix_pertask_car}
87	
88	Table~\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\S\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.
89	
90	\begin{table}[h]
91	\centering
92	\caption{Per-task CAR (\%) at 30K steps. $\lambda{=}0.005$, $\lambda{=}0.01$, and $\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}
93	\label{tab:per_task_car}
94	\vspace{2pt}
95	\small
96	\begin{tabular}{lccccc}
97	\toprule
98	Condition & OJ & CP & Milk & BBQ & Agg. \\
99	\midrule
100	LoRA s0 & 56 & 74 & 70 & 26 & 56.5 \\
101	LoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\
102	LoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\
103	SDF $\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\
104	SDF $\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\
105	SDF $\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\
106	SDF $\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\
107	SDF $\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\
108	SDF $\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\
109	\bottomrule
110	\end{tabular}
111	\end{table}
112	
113	For the $\lambda = 0.1$ condition, seed~1 records \texttt{avg\_max\_obstacle\_displacement} of 0.0553\,m (per-task: OJ\,=\,0.033, CP\,=\,0.055, Milk\,=\,0.041, BBQ\,=\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than frozen behavior.
114	
115	\begin{figure}[t]
116	\centering
117	\includegraphics[width=\linewidth]{fig_pertask_car_fingerprint}
118	\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\_pudding highest, bbq\_sauce lowest) is preserved across all $\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}
119	\label{fig:pertask_fingerprint}
120	\end{figure}
121	
122	\section{Safe Success Rate Analysis}\label{sec:appendix_ssr}
123	
124	Table~\ref{tab:ssr} reports the Safe Success Rate (SSR\,=\,TSR\,$\cap$\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.
125	
126	\begin{table}[h]
127	\centering
128	\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}
129	\label{tab:ssr}
130	\vspace{2pt}
131	\small
132	\begin{tabular}{lcccc}
133	\toprule
134	Condition & TSR (\%) & CAR (\%) & SSR (\%) & SSR/TSR \\
135	\midrule
136	Pi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\
137	LoRA-only (3 seeds) & 51.5 & 54.67 & 27.7 & 0.54 \\
138	SDF $\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\
139	SDF $\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\
140	SDF $\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\
141	\bottomrule
142	\end{tabular}
143	\end{table}
144	
145	\section{Per-Task Oracle Analysis}
146	\label{sec:appendix_pertask}
147	\label{sec:appendix_pertask_oracle}
148	
149	Table~\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\texttt{chocolate\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive improves to 55.0\% and Oracle-feature to 47.5\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\texttt{orange\_juice}) from 96.0\% to 82.5\% and task~2 (\texttt{milk}) from 98.0\% to 77.5\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.
150	
151	The feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49), and CAR (76.9\%) shows no advantage despite 17$\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.
152	
153	\begin{table}[h]
154	\centering
155	\caption{Per-task CAR (\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}
156	\label{tab:oracle_pertask}
157	\vspace{2pt}
158	\small
159	\begin{tabular}{lccccc}
160	\toprule
161	Method & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\
162	\midrule
163	LoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\
164	\midrule
165	Oracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\
166	Oracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\
167	Oracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\
168	\bottomrule
169	\end{tabular}
170	\end{table}
171	
172	
173	\section{Null Distribution for SDF Loss Weight Analysis}
174	\label{sec:appendix_null}
175	
176	We construct a null distribution by pooling the three LoRA-only seeds and three $\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\% (LoRA s0, re-evaluated), 52.5\% (LoRA s1), 55.0\% (LoRA s2), 57.0\% ($\lambda{=}0.005$ s0), 54.0\% ($\lambda{=}0.005$ s1), 52.5\% ($\lambda{=}0.005$ s2), yielding mean 54.58\% and standard deviation 1.93\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\lambda = 0.005$ produces no separation from LoRA-only. The $\lambda = 0.01$ mean of 56.33\% falls within $0.8\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\lambda = 0.1$ 30K mean of 57.00\% (3 seeds: 58.0\%, 58.5\%, 54.5\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\alpha = 0.05$).
177	
178	The permutation test makes no distributional assumptions. Pooling the six null values $\{56.5, 52.5, 55, 57, 54, 52.5\}$ and three $\lambda = 0.1$ values $\{58, 58.5, 54.5\}$ into nine measurements, we enumerate all $\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \approx 0.131$. With the third seed ($s_2 = 54.5\%$) pulling the $\lambda = 0.1$ mean from 58.25\% (2 seeds) down to 57.00\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.
179	
180	A Phase~2 ablation reinforces this conclusion. Setting $\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.
181	
182	\section{Step-wise Checkpoint Analysis for \texorpdfstring{$\lambda = 0.1$}{lambda = 0.1}}
183	\label{sec:appendix_stepwise}
184	
185	Table~\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\%) pulls the three-seed mean to 57.00\%, within the null band ($p = 0.131$).
186	
187	\begin{table}[h]
188	\centering
189	\caption{Per-seed CAR (\%) at training checkpoints for $\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\%) remains within the null band ($p = 0.131$, two-tailed permutation).}
190	\label{tab:stepwise_lambda01}
191	\vspace{2pt}
192	\small
193	\begin{tabular}{lcccc}
194	\toprule
195	Checkpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\
196	\midrule
197	16K steps & 55.5 & 56.0 & -- & 55.75 \\
198	20K steps & 55.0 & 56.0 & -- & 55.5 \\
199	22K steps & 60.5 & 56.5 & -- & 58.5 \\
200	24K steps & 52.5 & -- & -- & -- \\
201	26K steps & 53.5 & -- & -- & -- \\
202	28K steps & 54.5 & -- & -- & -- \\
203	30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\
204	\bottomrule
205	\end{tabular}
206	\end{table}
207	
208	Individual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\,pp (seed~0: 52.5--60.5\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\leq$3\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\sigma \approx 7$\,pp per task for $p \approx 0.5$). At 30K, the third seed ($s_2 = 54.5\%$) falls well within the null range, pulling the three-seed mean to 57.00\% and rendering the earlier two-seed departure non-significant ($p = 0.131$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.
209	
210	
211	\section{Oracle SDF Refinement Details}
212	\label{sec:appendix_oracle}
213	
214	All oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\times$ 40).
215	
216	\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.
217	
218	\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.
219	
220	\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49 in action space).
221	
222	
223	\section{Cross-Scene Validation: spatial\_bowl}
224	\label{sec:appendix_spatial_bowl}
225	
226	To test whether the SDF redundancy finding generalizes beyond the primary \texttt{object\_pudding} scene, we replicate the core comparison on \texttt{spatial\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.
227	
228	Table~\ref{tab:spatial_bowl} reports the results. The SDF condition ($\lambda = 0.005$) yields CAR of 11.5\% versus 15.5\% for LoRA-only, a $-$4.0\,pp difference indicating that SDF supervision is not only redundant but slightly detrimental in this scene. TSR is comparable across conditions (50.0\% vs.\ 51.5\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \texttt{object\_pudding} findings.
229	
230	\begin{table}[h]
231	\centering
232	\caption{Cross-scene validation on \texttt{spatial\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$4.0\,pp CAR difference indicates SDF is not only redundant but slightly detrimental, consistent with \texttt{object\_pudding}.}
233	\label{tab:spatial_bowl}
234	\vspace{2pt}
235	\small
236	\begin{tabular}{lcc}
237	\toprule
238	Condition & CAR (\%) & TSR (\%) \\
239	\midrule
240	LoRA-only & 15.5 & 50.0 \\
241	SDF $\lambda{=}0.005$ & 11.5 & 51.5 \\
242	\bottomrule
243	\end{tabular}
244	\end{table}
245	
246	The substantially lower CAR on \texttt{spatial\_bowl} relative to \texttt{object\_pudding} (12--16\% vs.\ 54--57\%) reflects the greater scene difficulty: \texttt{spatial\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition actually performs worse ($\Delta$CAR\,=\,$-$4.0\,pp), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.
247	
248	
249	\section{Evaluation Seed Robustness}
250	\label{sec:appendix_eval_seed}
251	
252	To verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate the LoRA-only (s0) and SDF $\lambda{=}0.1$ (s0) checkpoints under multiple evaluation seeds. Table~\ref{tab:eval_seed_car} reports aggregate CAR and Table~\ref{tab:eval_seed_tsr} reports aggregate TSR.
253	
254	\begin{table}[h]
255	\centering
256	\caption{Aggregate CAR (\%) across evaluation seeds (200 episodes each). The LoRA vs.\ SDF $\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}
257	\label{tab:eval_seed_car}
258	\vspace{2pt}
259	\small
260	\begin{tabular}{lcccccc}
261	\toprule
262	& \multicolumn{4}{c}{Per-task CAR (\%)} & & \\
263	\cmidrule(lr){2-5}
264	Condition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\
265	\midrule
266	LoRA s0 (seed\,=\,7)   & 56 & 74 & 70 & 26 & 56.5 \\
267	LoRA s0 (seed\,=\,42)  & 60 & 70 & 68 & 28 & 56.5 \\
268	LoRA s0 (seed\,=\,123) & 52 & 74 & 66 & 20 & 53.0 \\
269	LoRA s0 mean $\pm$ std & 56.0$\pm$4.0 & 72.7$\pm$2.3 & 68.0$\pm$2.0 & 24.7$\pm$4.2 & 55.3$\pm$2.0 \\
270	\midrule
271	SDF $\lambda{=}0.1$ s0 (seed\,=\,7)   & 60 & 74 & 68 & 30 & 58.0 \\
272	SDF $\lambda{=}0.1$ s0 (seed\,=\,42)  & 64 & 74 & 74 & 24 & 59.0 \\
273	SDF $\lambda{=}0.1$ s0 (seed\,=\,123) & 62 & 76 & 74 & 22 & 58.5 \\
274	SDF $\lambda{=}0.1$ s0 (seed\,=\,256) & 60 & 72 & 66 & 30 & 57.0 \\
275	SDF $\lambda{=}0.1$ s0 mean $\pm$ std & 61.5$\pm$1.9 & 74.0$\pm$1.6 & 70.5$\pm$4.1 & 26.5$\pm$4.1 & 58.1$\pm$0.9 \\
276	\bottomrule
277	\end{tabular}
278	\end{table}
279	
280	\begin{table}[h]
281	\centering
282	\caption{Aggregate TSR (\%) across evaluation seeds. TSR varies more across seeds than CAR (seed\,=\,42 yields consistently lower TSR), but the relative ordering between LoRA and SDF is stable.}
283	\label{tab:eval_seed_tsr}
284	\vspace{2pt}
285	\small
286	\begin{tabular}{lcccccc}
287	\toprule
288	& \multicolumn{4}{c}{Per-task TSR (\%)} & & \\
289	\cmidrule(lr){2-5}
290	Condition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\
291	\midrule
292	LoRA s0 (seed\,=\,7)   & 32 & 74 & 42 & 58 & 51.5 \\
293	LoRA s0 (seed\,=\,42)  & 22 & 70 & 32 & 60 & 46.0 \\
294	LoRA s0 (seed\,=\,123) & 30 & 70 & 40 & 62 & 50.5 \\
295	LoRA s0 mean $\pm$ std & 28.0$\pm$5.3 & 71.3$\pm$2.3 & 38.0$\pm$5.3 & 60.0$\pm$2.0 & 49.3$\pm$3.0 \\
296	\midrule
297	SDF $\lambda{=}0.1$ s0 (seed\,=\,7)   & 28 & 78 & 44 & 60 & 52.5 \\
298	SDF $\lambda{=}0.1$ s0 (seed\,=\,42)  & 18 & 78 & 42 & 72 & 52.5 \\
299	SDF $\lambda{=}0.1$ s0 (seed\,=\,123) & 26 & 82 & 38 & 68 & 53.5 \\
300	SDF $\lambda{=}0.1$ s0 (seed\,=\,256) & 28 & 74 & 32 & 58 & 48.0 \\
301	SDF $\lambda{=}0.1$ s0 mean $\pm$ std & 25.0$\pm$4.8 & 78.0$\pm$3.3 & 39.0$\pm$5.4 & 64.5$\pm$6.6 & 51.6$\pm$2.4 \\
302	\bottomrule
303	\end{tabular}
304	\end{table}
305	
306	Across three matched evaluation seeds (7, 42, 123), the SDF $\lambda{=}0.1$ condition yields higher aggregate CAR than LoRA-only in all cases ($\Delta$CAR\,=\,+1.5, +2.5, +5.5\,pp). Cross-seed CAR standard deviation is 2.0\,pp for LoRA and 0.9\,pp for SDF, both small relative to the within-seed per-task variation. The per-task ordering (CP highest, BBQ lowest) is preserved across all seeds and both conditions, reinforcing the conclusion that avoidance patterns reflect the spatial statistics of training demonstrations.
307	
308	
309	\section{Training Details}
310	\label{sec:appendix_training}
311	
312	\paragraph{Architecture.}
313	We use LoRA~\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\alpha$=16) and the action expert (rank 32, $\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\to$ 256 $\to$ 3).
314	
315	\paragraph{Training schedule.}
316	Training proceeds in two phases:
317	\begin{itemize}
318	    \item \textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.
319	    \item \textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.
320	\end{itemize}
321	
322	\paragraph{Hyperparameters.}
323	\begin{table}[h]
324	\centering
325	\caption{Training hyperparameters.}
326	\label{tab:hyperparams}
327	\begin{tabular}{ll}
328	\toprule
329	Parameter & Value \\
330	\midrule
331	Base model & Pi0.5 (OpenPi, $\sim$3.5B parameters) \\
332	Optimizer & AdamW \\
333	Learning rate & $2.5 \times 10^{-5}$ (cosine decay to $\mathrm{lr}/10$) \\
334	Warmup steps & 1000 \\
335	Batch size & 32 \\
336	Total steps & 30000 \\
337	$\lambda_\mathrm{sdf}$ & \{0.005, 0.01, 0.1\} \\
338	$\lambda_\mathrm{ee}$ & 0.01 \\
339	SDF query points per step & 64 \\
340	SDF clamp $\delta$ & 0.05 m \\
341	Eikonal weight & 0.1 \\
342	LoRA rank (vision) & 16 \\
343	LoRA rank (action) & 32 \\
344	Phase 1 duration & 5000 steps \\
345	\bottomrule
346	\end{tabular}
347	\end{table}
348	
349	\paragraph{Evaluation protocol.}
350	Each episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\sim}$5\% to ${\sim}$52\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).
351	
352	\paragraph{Data.}
353	We use the SafeLIBERO object\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.
354	
355	\paragraph{Computational resources.}
356	All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.
357	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "e11ea927-2959-44fb-9bc8-a34953ca2e58",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
      "content": "\\section{Displacement Distribution}\n\\label{sec:appendix_displacement}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{fig2_ee_displacement_distribution}\n\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n\n\\section{Displacement Threshold Sensitivity Analysis}\n\\label{sec:appendix_threshold}\n\nTo validate the robustness of our displacement threshold $\\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% frozen rate even at the most conservative setting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Frozen rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\n$\\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\\\\n\\midrule\n0.001 mm (1\\,$\\mu$m) & 73.9 & 0.0 & 0.0 \\\\\n0.1 mm  & 99.6 & 0.0 & 0.0 \\\\\n1.0 mm  & 100.0 & 0.0 & 0.0 \\\\\n10 mm   & 100.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of $\\tau_d = 0.1$\\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\\,mm per step. Even at $\\tau_d = 1$\\,$\\mu$m, 73.9\\% of A1-LoRA safe episodes are classified as frozen, while all Pi0.5 episodes remain above threshold at every level tested.\n\nTable~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n\n\\begin{table}[h]\n\\centering\n\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n\\label{tab:dfcar_threshold}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{lcccccccc}\n\\toprule\n& \\multicolumn{8}{c}{$\\tau_d$ (mm)} \\\\\n\\cmidrule(lr){2-9}\nCondition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n\\midrule\nLoRA s0            & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\\\\nLoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\nSDF $\\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\nSDF $\\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\nSDF $\\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\nSDF $\\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nSDF $\\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\nSDF $\\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n\nTable~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\n\nTable~\\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\\S\\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) at 30K steps. $\\lambda{=}0.005$, $\\lambda{=}0.01$, and $\\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}\n\\label{tab:per_task_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\\\\nLoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\\\\nSDF $\\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\\\\nSDF $\\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\\\\nSDF $\\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\\\\nSDF $\\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor the $\\lambda = 0.1$ condition, seed~1 records \\texttt{avg\\_max\\_obstacle\\_displacement} of 0.0553\\,m (per-task: OJ\\,=\\,0.033, CP\\,=\\,0.055, Milk\\,=\\,0.041, BBQ\\,=\\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than frozen behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_pertask_car_fingerprint}\n\\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all $\\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}\n\\label{fig:pertask_fingerprint}\n\\end{figure}\n\n\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n\nTable~\\ref{tab:ssr} reports the Safe Success Rate (SSR\\,=\\,TSR\\,$\\cap$\\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\n\\label{tab:ssr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\n\\midrule\nPi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\\\\nLoRA-only (3 seeds) & 51.5 & 54.67 & 27.7 & 0.54 \\\\\nSDF $\\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\\\\nSDF $\\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\\\\nSDF $\\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Oracle Analysis}\n\\label{sec:appendix_pertask}\n\\label{sec:appendix_pertask_oracle}\n\nTable~\\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.\n\nThe feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\n\\label{tab:oracle_pertask}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\\\\n\\midrule\nLoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\\\\n\\midrule\nOracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\\\\nOracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\\\\nOracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the three LoRA-only seeds and three $\\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 55.0\\% (LoRA s2), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.58\\% and standard deviation 1.93\\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 57.00\\% (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\\alpha = 0.05$).\n\nThe permutation test makes no distributional assumptions. Pooling the six null values $\\{56.5, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \\approx 0.131$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.131$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.131$, two-tailed permutation).}\n\\label{tab:stepwise_lambda01}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCheckpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\\\\n\\midrule\n16K steps & 55.5 & 56.0 & -- & 55.75 \\\\\n20K steps & 55.0 & 56.0 & -- & 55.5 \\\\\n22K steps & 60.5 & 56.5 & -- & 58.5 \\\\\n24K steps & 52.5 & -- & -- & -- \\\\\n26K steps & 53.5 & -- & -- & -- \\\\\n28K steps & 54.5 & -- & -- & -- \\\\\n30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIndividual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$3\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). At 30K, the third seed ($s_2 = 54.5\\%$) falls well within the null range, pulling the three-seed mean to 57.00\\% and rendering the earlier two-seed departure non-significant ($p = 0.131$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\n\n\n\\section{Oracle SDF Refinement Details}\n\\label{sec:appendix_oracle}\n\nAll oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n\n\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n\n\\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.\n\n\\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space).\n\n\n\\section{Cross-Scene Validation: spatial\\_bowl}\n\\label{sec:appendix_spatial_bowl}\n\nTo test whether the SDF redundancy finding generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.\n\nTable~\\ref{tab:spatial_bowl} reports the results. The SDF condition ($\\lambda = 0.005$) yields CAR of 11.5\\% versus 15.5\\% for LoRA-only, a $-$4.0\\,pp difference indicating that SDF supervision is not only redundant but slightly detrimental in this scene. TSR is comparable across conditions (50.0\\% vs.\\ 51.5\\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \\texttt{object\\_pudding} findings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$4.0\\,pp CAR difference indicates SDF is not only redundant but slightly detrimental, consistent with \\texttt{object\\_pudding}.}\n\\label{tab:spatial_bowl}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & CAR (\\%) & TSR (\\%) \\\\\n\\midrule\nLoRA-only & 15.5 & 50.0 \\\\\nSDF $\\lambda{=}0.005$ & 11.5 & 51.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe substantially lower CAR on \\texttt{spatial\\_bowl} relative to \\texttt{object\\_pudding} (12--16\\% vs.\\ 54--57\\%) reflects the greater scene difficulty: \\texttt{spatial\\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition actually performs worse ($\\Delta$CAR\\,=\\,$-$4.0\\,pp), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.\n\n\n\\section{Evaluation Seed Robustness}\n\\label{sec:appendix_eval_seed}\n\nTo verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate the LoRA-only (s0) and SDF $\\lambda{=}0.1$ (s0) checkpoints under multiple evaluation seeds. Table~\\ref{tab:eval_seed_car} reports aggregate CAR and Table~\\ref{tab:eval_seed_tsr} reports aggregate TSR.\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate CAR (\\%) across evaluation seeds (200 episodes each). The LoRA vs.\\ SDF $\\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}\n\\label{tab:eval_seed_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task CAR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 60 & 70 & 68 & 28 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,123) & 52 & 74 & 66 & 20 & 53.0 \\\\\nLoRA s0 mean $\\pm$ std & 56.0$\\pm$4.0 & 72.7$\\pm$2.3 & 68.0$\\pm$2.0 & 24.7$\\pm$4.2 & 55.3$\\pm$2.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 64 & 74 & 74 & 24 & 59.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 62 & 76 & 74 & 22 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 60 & 72 & 66 & 30 & 57.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 61.5$\\pm$1.9 & 74.0$\\pm$1.6 & 70.5$\\pm$4.1 & 26.5$\\pm$4.1 & 58.1$\\pm$0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate TSR (\\%) across evaluation seeds. TSR varies more across seeds than CAR (seed\\,=\\,42 yields consistently lower TSR), but the relative ordering between LoRA and SDF is stable.}\n\\label{tab:eval_seed_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task TSR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 32 & 74 & 42 & 58 & 51.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 22 & 70 & 32 & 60 & 46.0 \\\\\nLoRA s0 (seed\\,=\\,123) & 30 & 70 & 40 & 62 & 50.5 \\\\\nLoRA s0 mean $\\pm$ std & 28.0$\\pm$5.3 & 71.3$\\pm$2.3 & 38.0$\\pm$5.3 & 60.0$\\pm$2.0 & 49.3$\\pm$3.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 28 & 78 & 44 & 60 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 18 & 78 & 42 & 72 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 26 & 82 & 38 & 68 & 53.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 28 & 74 & 32 & 58 & 48.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 25.0$\\pm$4.8 & 78.0$\\pm$3.3 & 39.0$\\pm$5.4 & 64.5$\\pm$6.6 & 51.6$\\pm$2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAcross three matched evaluation seeds (7, 42, 123), the SDF $\\lambda{=}0.1$ condition yields higher aggregate CAR than LoRA-only in all cases ($\\Delta$CAR\\,=\\,+1.5, +2.5, +5.5\\,pp). Cross-seed CAR standard deviation is 2.0\\,pp for LoRA and 0.9\\,pp for SDF, both small relative to the within-seed per-task variation. The per-task ordering (CP highest, BBQ lowest) is preserved across all seeds and both conditions, reinforcing the conclusion that avoidance patterns reflect the spatial statistics of training demonstrations.\n\n\n\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\paragraph{Architecture.}\nWe use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n\n\\paragraph{Training schedule.}\nTraining proceeds in two phases:\n\\begin{itemize}\n    \\item \\textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.\n    \\item \\textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.\n\\end{itemize}\n\n\\paragraph{Hyperparameters.}\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\label{tab:hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & Pi0.5 (OpenPi, $\\sim$3.5B parameters) \\\\\nOptimizer & AdamW \\\\\nLearning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\nWarmup steps & 1000 \\\\\nBatch size & 32 \\\\\nTotal steps & 30000 \\\\\n$\\lambda_\\mathrm{sdf}$ & \\{0.005, 0.01, 0.1\\} \\\\\n$\\lambda_\\mathrm{ee}$ & 0.01 \\\\\nSDF query points per step & 64 \\\\\nSDF clamp $\\delta$ & 0.05 m \\\\\nEikonal weight & 0.1 \\\\\nLoRA rank (vision) & 16 \\\\\nLoRA rank (action) & 32 \\\\\nPhase 1 duration & 5000 steps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nEach episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\\sim}$5\\% to ${\\sim}$52\\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).\n\n\\paragraph{Data.}\nWe use the SafeLIBERO object\\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.\n\n\\paragraph{Computational resources.}\nAll training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n",
      "numLines": 357,
      "startLine": 1,
      "totalLines": 357
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
Now I have a clear picture of what needs to be done. Let me analyze the paper_switch.py managed text blocks carefully.

Key text blocks managed by paper_switch.py in claim3.tex:

1. **claim3 L3 scope** (line 3): "We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights..."
2. **claim3 L7 caption** (line 7): "\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR..."


3. **claim3 L20 table row** (line 20): The LoRA+SDF result with λ=0.1 showing the numerical metrics
4. **claim3 L27 body** (line 26): The paragraph discussing what the table reveals about collision-free demonstrations and the Phase 2 ablation findings with the 57.5% result
5. **claim3 L32-33 dose-response** (lines 31-32): The dose-response paragraph section header
6. **claim3 L38 fig caption** (line 37): The figure caption describing how SDF loss weight λ affects CAR and TSR

Now I'm working through what I can actually modify versus what's locked by paper_switch.py. The dose-response paragraph itself is managed by the script, so I'll need to flag that section rather than edit it directly. I need to identify which text strings appear as `old` values in paper_switch.py since those can't be changed without breaking the verification.

Looking at the structure of claim3.tex, I could potentially insert new paragraphs between the dose-response section and the figure without disrupting any managed blocks. Let me map out exactly where I have flexibility to add the null construction reports.

For the null robustness discussion, I can add a new paragraph after the dose-response that covers both Null A and Null B findings. The power analysis and appendix reference can follow as separate paragraphs. For the conclusion wording, I need to search through the file for phrases like "redundant" or "no benefit" that might need rewording to match the updated framing.

Most of the absolute language I'm looking for is actually in paper_switch.py managed blocks—the caption about SDF adding no measurable benefit, the statements about no lasting behavioral effect, and the redundancy claims are all controlled there. I'll need to flag those for revision. The λ=0.01 permutation p-value goes in the appendix, which isn't managed by paper_switch.py, so that's more straightforward to add. There's also a phase 2 checkpoint correction needed in claim3.tex.

Now I'm checking where the 57.5% CAR value appears—it's in the managed block for claim3 line 27, which I can't modify directly, but there's also a version in appendix.tex line 180 that I can change. The value shows up in multiple places in paper_switch.py's managed strings, so I need to be careful about what I can actually edit.

Since I can't change the managed reference, I'll need to flag this constraint and then run some statistical calculations—computing a permutation test comparing LoRA-only versus the λ=0.1 condition, analyzing the minimum detectable effect size, and calculating the exact p-value for the λ=0.01 case.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "df51e910-1fee-46b6-84ef-cfadc54f03d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8NWfyoZty9RTj19QQKsdk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21104,
      "cache_read_input_tokens": 25116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21104
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

Now let me compute the statistics and identify paper_switch.py managed blocks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "b31e1641-10fc-495a-9533-0a1a22168668",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8NWfyoZty9RTj19QQKsdk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21104,
      "cache_read_input_tokens": 25116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21104
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Kpze7cq2ZYoGxb8hBnCKfu`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nfrom itertools import combinations\nfrom math import comb, sqrt\nfrom scipy import stats\n\n# === Null A: LoRA-only (3 seeds) vs λ=0.1 (3 seeds) ===\nnull_a = [56.5, 52.5, 55.0]\ntreat = [58.0, 58.5, 54.5]\npool_a = null_a + treat\nk = 3\nobs = sum(treat)/k\nmu_a = sum(pool_a)/len(pool_a)\ndev_a = abs(obs - mu_a)\nge_a = tw_a = 0\nfor c in combinations(pool_a, k):\n    m = sum(c)/k\n    if m >= obs: ge_a += 1\n    if abs(m - mu_a) >= dev_a - 1e-12: tw_a += 1\nn_a = comb(len(pool_a), k)\nprint(f\"Null A: p_one={ge_a/n_a:.3f}, p_two={tw_a/n_a:.3f}, n_combos={n_a}\")\nprint(f\"  obs_mean={obs:.2f}, pool_mean={mu_a:.4f}, dev={dev_a:.4f}\")\nprint(f\"  ge={ge_a}, tw={tw_a}\")\n\n# === Null B: LoRA + λ=0.005 (6 seeds) vs λ=0.1 (3 seeds) ===\nnull_b = [56.5, 52.5, 55.0, 57.0, 54.0, 52.5]\npool_b = null_b + treat\nobs_b = sum(treat)/k\nmu_b = sum(pool_b)/len(pool_b)\ndev_b = abs(obs_b - mu_b)\nge_b = tw_b = 0\nfor c in combinations(pool_b, k):\n    m = sum(c)/k\n    if m >= obs_b: ge_b += 1\n    if abs(m - mu_b) >= dev_b - 1e-12: tw_b += 1\nn_b = comb(len(pool_b), k)\nprint(f\"\\nNull B: p_one={ge_b/n_b:.3f}, p_two={tw_b/n_b:.3f}, n_combos={n_b}\")\n\n# === λ=0.01 exact permutation p-value ===\nlora_only = [56.5, 52.5, 55.0]\nlam001 = [57.0, 57.5, 54.5]\npool_01 = lora_only + lam001\nobs_01 = sum(lam001)/k\nmu_01 = sum(pool_01)/len(pool_01)\ndev_01 = abs(obs_01 - mu_01)\nge_01 = tw_01 = 0\nfor c in combinations(pool_01, k):\n    m = sum(c)/k\n    if m >= obs_01: ge_01 += 1\n    if abs(m - mu_01) >= dev_01 - 1e-12: tw_01 += 1\nn_01 = comb(len(pool_01), k)\nprint(f\"\\nλ=0.01 vs LoRA-only (Null A): p_one={ge_01/n_01:.3f}, p_two={tw_01/n_01:.3f}, n_combos={n_01}\")\nprint(f\"  obs_mean={obs_01:.4f}, pool_mean={mu_01:.4f}\")\n\n# === Power Analysis ===\n# n=3 per group, σ≈2.0pp, α=0.05 one-tailed\n# MDE at 80% power using t-test approximation\nn_per = 3\nsigma = 2.0\nalpha = 0.05\ndf = 2 * n_per - 2  # df=4\nt_crit = stats.t.ppf(1 - alpha, df)\nt_power = stats.t.ppf(0.80, df)  # for 80% power\n# MDE = (t_crit + t_power) * sigma * sqrt(2/n)\nMDE = (t_crit + t_power) * sigma * sqrt(2/n_per)\nprint(f\"\\nPower Analysis:\")\nprint(f\"  df={df}, t_crit(0.05,{df})={t_crit:.3f}, t_80%({df})={t_power:.3f}\")\nprint(f\"  MDE at 80% power = ({t_crit:.3f} + {t_power:.3f}) * {sigma} * sqrt(2/{n_per})\")\nprint(f\"  MDE = {MDE:.1f} pp\")\nprint(f\"  Observed effect = {obs - sum(null_a)/k:.1f} pp\")\n\n# Also compute with two-tailed alpha\nt_crit_2 = stats.t.ppf(1 - alpha/2, df)\nMDE_2 = (t_crit_2 + t_power) * sigma * sqrt(2/n_per)\nprint(f\"  MDE (two-tailed α=0.05) = {MDE_2:.1f} pp\")\n\n# Also: permutation-based power is harder to compute exactly, \n# so t-test approx is standard\nprint(f\"\\n  Observed effect (λ=0.1 - LoRA mean): {sum(treat)/k - sum(null_a)/k:.2f} pp\")\n\nPYEOF\n",
  "description": "Compute exact permutation p-values and power analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "794d2d73-5350-49b8-9da1-dd54eed843ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8NWfyoZty9RTj19QQKsdk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21104,
      "cache_read_input_tokens": 25116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21104
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

_source line 15 · 2026-05-28T05:36:15.440Z_

<details><summary>↩ Tool result · `toolu_01Kpze7cq2ZYoGxb8hBnCKfu`</summary>

```text
Null A: p_one=0.150, p_two=0.300, n_combos=20
  obs_mean=57.00, pool_mean=55.8333, dev=1.1667
  ge=3, tw=6

Null B: p_one=0.071, p_two=0.131, n_combos=84

λ=0.01 vs LoRA-only (Null A): p_one=0.200, p_two=0.400, n_combos=20
  obs_mean=56.3333, pool_mean=55.5000

Power Analysis:
  df=4, t_crit(0.05,4)=2.132, t_80%(4)=0.941
  MDE at 80% power = (2.132 + 0.941) * 2.0 * sqrt(2/3)
  MDE = 5.0 pp
  Observed effect = 2.3 pp
  MDE (two-tailed α=0.05) = 6.1 pp

  Observed effect (λ=0.1 - LoRA mean): 2.33 pp
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "a5576985-cec4-4150-91c3-b54db3fea27a",
  "tool_use_result": {
    "stdout": "Null A: p_one=0.150, p_two=0.300, n_combos=20\n  obs_mean=57.00, pool_mean=55.8333, dev=1.1667\n  ge=3, tw=6\n\nNull B: p_one=0.071, p_two=0.131, n_combos=84\n\nλ=0.01 vs LoRA-only (Null A): p_one=0.200, p_two=0.400, n_combos=20\n  obs_mean=56.3333, pool_mean=55.5000\n\nPower Analysis:\n  df=4, t_crit(0.05,4)=2.132, t_80%(4)=0.941\n  MDE at 80% power = (2.132 + 0.941) * 2.0 * sqrt(2/3)\n  MDE = 5.0 pp\n  Observed effect = 2.3 pp\n  MDE (two-tailed α=0.05) = 6.1 pp\n\n  Observed effect (λ=0.1 - LoRA mean): 2.33 pp",
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

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the statistics:

**Null A** (LoRA-only vs λ=0.1): p_one=0.150, p_two=0.300, n=20
**Null B** (LoRA+λ=0.005 vs λ=0.1): p_one=0.071, p_two=0.131, n=84
**λ=0.01 vs LoRA-only**: p_one=0.200, p_two=0.400, n=20
**Power Analysis**: MDE (one-tailed) ≈ 5.0 pp, MDE (two-tailed) ≈ 6.1 pp, observed effect ≈ 2.3 pp


Now I'm mapping out which parts of claim3.tex are controlled by paper_switch.py and which I can edit directly. The script manages the scope sentence, table caption, the λ=0.1 row, the Phase 2 ablation paragraph with specific percentages and claims about redundancy, the dose-response section, and the figure caption—so I need to work around those constraints.

For the sections I can modify, I'll focus on the header and intro, the CAR-TSR trade-off paragraph, and inserting new content between the managed blocks. My strategy is to add discussion of the null constructions and their robustness after the dose-response paragraph, incorporate power analysis findings, reference the Appendix J eval-seed data, and flag all instances of absolute wording that appear in the managed sections so I know what I'm working with.

For appendix.tex, I need to add the permutation p-value statistics with λ=0.01 and update the Phase 2 ablation numbers—changing the range from 5K–30K to 5K–18K and adjusting the percentage from 57.5% to 58.0%.

Now I'm constructing the new LaTeX paragraph for claim3.tex that discusses robustness to null construction, starting with how the permutation test holds up across different null pool choices... The LoRA-only baseline already sits at a high performance level, which makes the comparison less dramatic. Looking at statistical power, with only three seeds per group and a cross-seed standard deviation around 2 percentage points, I'd need an effect size of at least 5 percentage points to achieve 80% power in a one-tailed t-test at α = 0.05—but the observed effect is only about 2.3 percentage points, leaving the study underpowered. However, when I examine the matched evaluation conditions across the three paired seeds, the λ = 0.1 configuration consistently outperforms, showing gains of 1.5, 2.5, and 5.5 percentage points with reduced variance. I'm working through the specific edits needed for claim3.tex, identifying which changes I can make directly versus which ones involve managed text blocks that I need to flag for later handling. The key constraint is not modifying any text blocks that paper_switch.py manages, since their old_string values need to stay matched. So I'll add new paragraphs where needed, update unmanaged sections, and document any managed text that requires changes for the report. So the unmanaged sections are the section header, the opening claim about collision avoidance, and the table itself. Everything else—the comparison sentence, the body paragraph, the dose-response section, and the figure caption—is locked in place and can't be changed.

That means I have a few insertion points available. I can add new content after the dose-response paragraph and before the figure, or after the figure at the end of the section. There's also a potential spot between the CAR-TSR trade-off discussion and the dose-response section.

My plan is to insert a paragraph on null construction robustness right after the dose-response section wraps up, which gives me space to discuss that aspect before moving into the figure.

For the P0-2D task, I need to replace the conclusion paragraph with the target text about statistical significance and the CAR improvement findings. The new conclusion should emphasize that at n=3 training seeds, SDF supervision doesn't reach statistical significance (p=0.131), though SDF λ=0.1 does show higher CAR across all three paired comparisons, with the effect size around 2.3 percentage points.

I also need to identify and replace the absolute language in the managed blocks—phrases like "adds no measurable," "produces no measurable benefit," "produce no lasting behavioral effect"—with more measured wording that acknowledges the directional consistency without claiming definitive null results.

For the actual edits, I'm planning to insert new paragraphs in claim3.tex between the dose-response analysis and the figure, covering the null construction robustness, power analysis, evaluation seed reference, and a revised conclusion. Then in appendix.tex, I'll add the λ=0.01 permutation results and fix the Phase 2 ablation text.

Now I need to figure out the exact insertion points and write out what these new sections should contain. Between lines 32 and 34 in claim3.tex, I'm adding paragraphs on null construction robustness that compares two different null hypotheses—one pooling LoRA-only and λ=0.005 seeds, another using only LoRA-only seeds—and shows both yield non-significant results. Then I'm adding a power analysis section that discusses the statistical power given the sample size and observed variance. one-tailed) achieves 80% power only for effects ≥5.0 pp. The observed effect of ~2.3 pp falls well below this minimum detectable effect (MDE).

Under matched evaluation conditions, SDF λ=0.1 yields higher CAR in all three paired eval seeds (+1.5, +2.5, +5.5 pp), with lower cross-seed variance (σ=0.9 pp vs. 2.0 pp for LoRA). At the tested scale (n=3 training seeds), SDF supervision doesn't produce a statistically significant CAR improvement (p=0.131, two-tailed permutation). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding can't be resolved at the current sample size.

Now I need to add the λ=0.01 permutation statistics to the null distribution section and fix the Phase 2 ablation. Let me check what sections already exist in the appendix—I can see there's a null distribution section around line 173 where I should insert the λ=0.01 stats, and I need to locate and correct the Phase 2 ablation entry. I'm reviewing the permutation test details more carefully—line 176 already states that λ=0.01 falls within 0.8σ of the null distribution with p > 0.1, but I need to add the exact permutation p-values to match what's shown for the other conditions. I can either expand that existing sentence or insert a new paragraph with the specific calculations.

Now I'm planning the appendix edits systematically. I'll add a paragraph about Null A results and the λ=0.01 exact permutation test right after the current Null B discussion, then fix the Phase 2 ablation statement on line 180. The insertion point is between the dose-response paragraph ending with "supervising the wrong collision surface" and the figure block that follows.

I need to be careful with the find-and-replace logic since paper_switch.py manages these blocks with its own string matching. As long as I don't modify the exact text that paper_switch.py uses to identify the dose-response paragraph, the replacement should still work correctly—the tool matches on the full old_string block, so adding new content after it won't break the match.

Now I'm ready to make the edit in claim3.tex by inserting new paragraphs between the end of the dose-response section and the figure block.

The issue is that paper_switch.py might replace the dose-response paragraph with different text depending on the scenario, so I can't rely on the paragraph's ending as an anchor point. Instead, I'll use the `\begin{figure}[t]` marker as my insertion point—it's stable across all scenarios and will let me add content right before the figure without worrying about which version of the dose-response text is in place.

I've verified that the figure environment is unique in the file, so I can safely search for it along with a few lines of context to make the match even more robust. Now I'm ready to write out all the edits, starting with computing the statistical values for the Null A and Null B paragraphs.

For the power analysis, the minimum detectable effect at 80% power is around 5.0 percentage points, but the observed effect is only about 2.3 percentage points. Let me also double-check the exact p-value for the λ=0.01 case against the LoRA-only baseline—I need to verify whether appendix.tex currently has just the inequality or if I need to add the precise permutation test result.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "69369201-a681-47f5-b60e-fa74f90d16d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vn2q9D2m91qXXFufM76rgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3298,
      "cache_read_input_tokens": 46220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3298
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

_source line 17_

Let me also compute λ=0.01 against Null B.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "93a027e8-c3bf-438b-bbbf-ebf3ca2b08c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vn2q9D2m91qXXFufM76rgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3298,
      "cache_read_input_tokens": 46220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3298
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01CrPju49qpEkHRBQrsdxeGy`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nfrom itertools import combinations\nfrom math import comb\n\n# λ=0.01 vs Null B (LoRA + λ=0.005, 6 values)\nnull_b = [56.5, 52.5, 55.0, 57.0, 54.0, 52.5]\nlam001 = [57.0, 57.5, 54.5]\npool = null_b + lam001\nk = 3\nobs = sum(lam001)/k\nmu = sum(pool)/len(pool)\ndev = abs(obs - mu)\nge = tw = 0\nfor c in combinations(pool, k):\n    m = sum(c)/k\n    if m >= obs: ge += 1\n    if abs(m - mu) >= dev - 1e-12: tw += 1\nn = comb(len(pool), k)\nprint(f\"λ=0.01 vs Null B: p_one={ge/n:.3f}, p_two={tw/n:.3f}, n_combos={n}\")\nprint(f\"  obs_mean={obs:.4f}, pool_mean={mu:.4f}\")\nprint(f\"  ge={ge}, tw={tw}\")\n\n# Also enumerate for Null A to confirm\nnull_a = [56.5, 52.5, 55.0]\npool_a = null_a + lam001\nobs_a = sum(lam001)/k\nmu_a = sum(pool_a)/len(pool_a)\ndev_a = abs(obs_a - mu_a)\nge_a = tw_a = 0\nfor c in combinations(pool_a, k):\n    m = sum(c)/k\n    if m >= obs_a: ge_a += 1\n    if abs(m - mu_a) >= dev_a - 1e-12: tw_a += 1\nn_a = comb(len(pool_a), k)\nprint(f\"\\nλ=0.01 vs Null A: p_one={ge_a/n_a:.3f}, p_two={tw_a/n_a:.3f}, n_combos={n_a}\")\n\n# Enumerate all combos for Null A to double-check\nprint(\"\\nAll C(6,3) combos for λ=0.01 Null A test:\")\nfor c in combinations(pool_a, k):\n    m = sum(c)/k\n    flag_ge = \" >= obs\" if m >= obs_a else \"\"\n    flag_tw = \" |dev|>=\" if abs(m - mu_a) >= dev_a - 1e-12 else \"\"\n    print(f\"  {c} -> mean={m:.4f}{flag_ge}{flag_tw}\")\n\nPYEOF\n",
  "description": "Compute λ=0.01 permutation test against both null pools"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "c1a0cc0b-dd2e-4459-91bf-1a05d984ae46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vn2q9D2m91qXXFufM76rgE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3298,
      "cache_read_input_tokens": 46220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3298
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

_source line 19 · 2026-05-28T05:38:05.867Z_

<details><summary>↩ Tool result · `toolu_01CrPju49qpEkHRBQrsdxeGy`</summary>

```text
λ=0.01 vs Null B: p_one=0.119, p_two=0.262, n_combos=84
  obs_mean=56.3333, pool_mean=55.1667
  ge=10, tw=22

λ=0.01 vs Null A: p_one=0.200, p_two=0.400, n_combos=20

All C(6,3) combos for λ=0.01 Null A test:
  (56.5, 52.5, 55.0) -> mean=54.6667 |dev|>=
  (56.5, 52.5, 57.0) -> mean=55.3333
  (56.5, 52.5, 57.5) -> mean=55.5000
  (56.5, 52.5, 54.5) -> mean=54.5000 |dev|>=
  (56.5, 55.0, 57.0) -> mean=56.1667
  (56.5, 55.0, 57.5) -> mean=56.3333 >= obs |dev|>=
  (56.5, 55.0, 54.5) -> mean=55.3333
  (56.5, 57.0, 57.5) -> mean=57.0000 >= obs |dev|>=
  (56.5, 57.0, 54.5) -> mean=56.0000
  (56.5, 57.5, 54.5) -> mean=56.1667
  (52.5, 55.0, 57.0) -> mean=54.8333
  (52.5, 55.0, 57.5) -> mean=55.0000
  (52.5, 55.0, 54.5) -> mean=54.0000 |dev|>=
  (52.5, 57.0, 57.5) -> mean=55.6667
  (52.5, 57.0, 54.5) -> mean=54.6667 |dev|>=
  (52.5, 57.5, 54.5) -> mean=54.8333
  (55.0, 57.0, 57.5) -> mean=56.5000 >= obs |dev|>=
  (55.0, 57.0, 54.5) -> mean=55.5000
  (55.0, 57.5, 54.5) -> mean=55.6667
  (57.0, 57.5, 54.5) -> mean=56.3333 >= obs |dev|>=
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "b3e0fac7-a8f0-4807-b1f7-6096d1bbb8a5",
  "tool_use_result": {
    "stdout": "λ=0.01 vs Null B: p_one=0.119, p_two=0.262, n_combos=84\n  obs_mean=56.3333, pool_mean=55.1667\n  ge=10, tw=22\n\nλ=0.01 vs Null A: p_one=0.200, p_two=0.400, n_combos=20\n\nAll C(6,3) combos for λ=0.01 Null A test:\n  (56.5, 52.5, 55.0) -> mean=54.6667 |dev|>=\n  (56.5, 52.5, 57.0) -> mean=55.3333\n  (56.5, 52.5, 57.5) -> mean=55.5000\n  (56.5, 52.5, 54.5) -> mean=54.5000 |dev|>=\n  (56.5, 55.0, 57.0) -> mean=56.1667\n  (56.5, 55.0, 57.5) -> mean=56.3333 >= obs |dev|>=\n  (56.5, 55.0, 54.5) -> mean=55.3333\n  (56.5, 57.0, 57.5) -> mean=57.0000 >= obs |dev|>=\n  (56.5, 57.0, 54.5) -> mean=56.0000\n  (56.5, 57.5, 54.5) -> mean=56.1667\n  (52.5, 55.0, 57.0) -> mean=54.8333\n  (52.5, 55.0, 57.5) -> mean=55.0000\n  (52.5, 55.0, 54.5) -> mean=54.0000 |dev|>=\n  (52.5, 57.0, 57.5) -> mean=55.6667\n  (52.5, 57.0, 54.5) -> mean=54.6667 |dev|>=\n  (52.5, 57.5, 54.5) -> mean=54.8333\n  (55.0, 57.0, 57.5) -> mean=56.5000 >= obs |dev|>=\n  (55.0, 57.0, 54.5) -> mean=55.5000\n  (55.0, 57.5, 54.5) -> mean=55.6667\n  (57.0, 57.5, 54.5) -> mean=56.3333 >= obs |dev|>=",
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

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have all the statistics I need. Let me also identify exact paper_switch.py managed blocks in claim3.tex:

Managed text blocks in claim3.tex (from paper_switch.py):
1. "We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint." (line 3)
2. "\caption{Avoidance source attribution on SafeLIBERO. 

SDF adds no measurable CAR beyond LoRA-only across the full tested range $\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}" (line 7)
3. "LoRA+SDF $\lambda{=}0.1$ & 3 & 50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\" (line 20)
4. The entire body paragraph starting "Table ~\ref{tab:avoidance_source} shows that..." through "...rather than geometric supervision." (line 26)
5. The dose-response paragraph discussing higher loss weights and how SDF supervision may be targeting the wrong collision surface (lines 31-32)
6. The caption describing the effect of SDF loss weight (line 37)

Now I'm planning the edits. I need to add new paragraphs between the dose-response section and the figure, update the appendix with null distribution discussion and exact p-values for λ=0.01, and correct the Phase 2 ablation text to reflect the actual step range and percentage values.

For the claim3.tex insertion, I'm targeting the space right after the dose-response conclusion and before the figure begins. The old string needs to be precise to match the exact location where the new content should go. The key insight is that increasing the SDF loss weight doesn't help because the real problem isn't the strength of the signal—it's that we're supervising the wrong collision surfaces entirely. End-effector monitoring can't substitute for proper full-body collision awareness, no matter how much we amplify the training signal.

Now I'm identifying a safe anchor point in the LaTeX code to insert new content. The figure block itself won't be modified by the paper switching logic, so I can use the opening of that figure environment as my insertion point, placing new paragraphs right before it begins.

I need to be careful about the exact wording for both sections—P0-2A requires specific Chinese text about null construction robustness across different seed configurations, while P0-2C needs precise English text comparing SDF performance metrics across evaluation conditions with exact numerical values for CAR improvements and variance measurements. I'm working through the statistical appendix edits now. For the λ=0.01 case, I need to add the exact permutation results to the Null Distribution section—showing p-values for both the restricted null (just LoRA) and the full null pool. Then I'll update the Phase 2 details: changing the step range from 5K-30K to 5K-18K, adjusting the performance metric from 57.5% to 58.0%, and noting the disk space constraints. Let me locate the exact lines in the appendix around 176-180 to position these edits correctly. I'm re-examining the actual line numbers and content from my earlier read. The null distribution section spans lines 176-180, and I need to carefully identify where the Null A statistics should be inserted and how to modify the Phase 2 paragraph without duplicating information I've already described. I'm working through the permutation test calculation by pooling the null and treatment values, then enumerating all possible three-element combinations to determine how many have means at or above the observed 57.00% threshold. The one-tailed p-value comes out to about 0.071, and accounting for the lower tail symmetrically gives a two-tailed p of roughly 0.131—both non-significant at conventional levels, though the third seed's lower value notably pulls down what would otherwise be a stronger treatment effect.

For the ablation study, I need to revise the Phase 2 section to clarify that disabling SDF supervision after the initial warmup phase yields a CAR of 57.5%, which falls squarely within the null distribution and suggests the training signal doesn't produce sustained improvements in collision avoidance. I'll also add a paragraph exploring an alternative null construction using LoRA-only baselines and the permutation results at λ=0.01 to strengthen the argument. I'm refining the Phase 2 ablation section by updating the step ranges from 5K--30K to 5K--18K and adjusting the CAR metric from 57.5% to 58.0%, while clarifying that this is measured at the 18K checkpoint after 13K steps of Phase 2 training. Now I'm implementing the edits across both files in parallel—inserting the new content about the null range result in appendix.tex between the existing sections, and modifying the figure reference in claim3.tex to accommodate the new paragraphs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "3935aa15-52f3-4d99-bb8b-3c9bef1a4b10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALeSePiX4hw8hzp9siL8ut",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6833,
      "cache_read_input_tokens": 49518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6833
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

Now I have all the statistics. Let me identify what's paper_switch.py-managed in claim3.tex before editing.

**Managed blocks in claim3.tex (MUST NOT modify):**
- Line 3: scope sentence ("We compare LoRA-only...")
- Line 7: table caption
- Line 20: λ=0.1 table row
- Line 26: entire body paragraph (includes "57.5%" Phase 2 and "no measurable benefit")
- Lines 31-32: entire dose-response paragraph (includes "redundant")
- Line 37: figure caption (includes "full redundancy")

I'll add new paragraphs between the dose-response block and the figure, and edit appendix.tex directly. Making all independent edits now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "62abc149-1b21-45b0-ad7d-e543e6e568f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALeSePiX4hw8hzp9siL8ut",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6833,
      "cache_read_input_tokens": 49518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6833
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

<details open><summary>🔧 Tool call — Edit · `toolu_01LVVK4N7mGWC7LfJp2eQnaa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}",
  "new_string": "\\paragraph{Robustness to null construction.}\nThe preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.\n\n\\paragraph{Statistical power.}\nWith $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.\n\n\\paragraph{Evaluation-seed consistency.}\nUnder matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "cb6ed9f2-31c7-4e6a-8d9c-e7e784c9cfb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALeSePiX4hw8hzp9siL8ut",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6833,
      "cache_read_input_tokens": 49518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6833
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

_source line 23 · 2026-05-28T05:39:31.185Z_

<details><summary>↩ Tool result · `toolu_01LVVK4N7mGWC7LfJp2eQnaa`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "d5b87b46-7202-483d-8972-ffe68f8272b9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "oldString": "\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}",
    "newString": "\\paragraph{Robustness to null construction.}\nThe preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.\n\n\\paragraph{Statistical power.}\nWith $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.\n\n\\paragraph{Evaluation-seed consistency.}\nUnder matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}",
    "originalFile": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across the full tested range $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 3 & 51.5\\,$\\pm$\\,0.0 & 54.67\\,$\\pm$\\,2.02 & 0.391 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$ & 3 & 50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$18--20\\,pp (71.5\\% $\\to$ 51.5--54.0\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within the null band ($p > 0.05$), confirming full redundancy of EE-only SDF supervision across a 20$\\times$ loss-weight range.}\n\\label{fig:lambda_car}\n\\end{figure}",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 6,
        "newStart": 31,
        "newLines": 15,
        "lines": [
          " \\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}",
          " Increasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.",
          " ",
          "+\\paragraph{Robustness to null construction.}",
          "+The preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.",
          "+",
          "+\\paragraph{Statistical power.}",
          "+With $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.",
          "+",
          "+\\paragraph{Evaluation-seed consistency.}",
          "+Under matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.",
          "+",
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}"
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

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01CNpAJ24DRQjJVdHwiQXBcA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\nA Phase~2 ablation reinforces this conclusion.",
  "new_string": "the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "7c8176ef-33a3-4050-b025-8f6ca086c12d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALeSePiX4hw8hzp9siL8ut",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6833,
      "cache_read_input_tokens": 49518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6833
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

_source line 25 · 2026-05-28T05:39:37.523Z_

<details><summary>↩ Tool result · `toolu_01CNpAJ24DRQjJVdHwiQXBcA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "aa074965-35c4-4c79-a59f-83371f71bb54",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "oldString": "the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\nA Phase~2 ablation reinforces this conclusion.",
    "newString": "the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion.",
    "originalFile": "\\section{Displacement Distribution}\n\\label{sec:appendix_displacement}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{fig2_ee_displacement_distribution}\n\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n\n\\section{Displacement Threshold Sensitivity Analysis}\n\\label{sec:appendix_threshold}\n\nTo validate the robustness of our displacement threshold $\\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% frozen rate even at the most conservative setting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Frozen rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\n$\\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\\\\n\\midrule\n0.001 mm (1\\,$\\mu$m) & 73.9 & 0.0 & 0.0 \\\\\n0.1 mm  & 99.6 & 0.0 & 0.0 \\\\\n1.0 mm  & 100.0 & 0.0 & 0.0 \\\\\n10 mm   & 100.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of $\\tau_d = 0.1$\\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\\,mm per step. Even at $\\tau_d = 1$\\,$\\mu$m, 73.9\\% of A1-LoRA safe episodes are classified as frozen, while all Pi0.5 episodes remain above threshold at every level tested.\n\nTable~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n\n\\begin{table}[h]\n\\centering\n\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n\\label{tab:dfcar_threshold}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{lcccccccc}\n\\toprule\n& \\multicolumn{8}{c}{$\\tau_d$ (mm)} \\\\\n\\cmidrule(lr){2-9}\nCondition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n\\midrule\nLoRA s0            & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\\\\nLoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\nSDF $\\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\nSDF $\\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\nSDF $\\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\nSDF $\\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nSDF $\\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\nSDF $\\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n\nTable~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\n\nTable~\\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\\S\\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) at 30K steps. $\\lambda{=}0.005$, $\\lambda{=}0.01$, and $\\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}\n\\label{tab:per_task_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\\\\nLoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\\\\nSDF $\\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\\\\nSDF $\\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\\\\nSDF $\\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\\\\nSDF $\\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor the $\\lambda = 0.1$ condition, seed~1 records \\texttt{avg\\_max\\_obstacle\\_displacement} of 0.0553\\,m (per-task: OJ\\,=\\,0.033, CP\\,=\\,0.055, Milk\\,=\\,0.041, BBQ\\,=\\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than frozen behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_pertask_car_fingerprint}\n\\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all $\\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}\n\\label{fig:pertask_fingerprint}\n\\end{figure}\n\n\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n\nTable~\\ref{tab:ssr} reports the Safe Success Rate (SSR\\,=\\,TSR\\,$\\cap$\\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\n\\label{tab:ssr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\n\\midrule\nPi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\\\\nLoRA-only (3 seeds) & 51.5 & 54.67 & 27.7 & 0.54 \\\\\nSDF $\\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\\\\nSDF $\\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\\\\nSDF $\\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Oracle Analysis}\n\\label{sec:appendix_pertask}\n\\label{sec:appendix_pertask_oracle}\n\nTable~\\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.\n\nThe feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\n\\label{tab:oracle_pertask}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\\\\n\\midrule\nLoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\\\\n\\midrule\nOracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\\\\nOracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\\\\nOracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the three LoRA-only seeds and three $\\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 55.0\\% (LoRA s2), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.58\\% and standard deviation 1.93\\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 57.00\\% (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\\alpha = 0.05$).\n\nThe permutation test makes no distributional assumptions. Pooling the six null values $\\{56.5, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \\approx 0.131$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.131$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.131$, two-tailed permutation).}\n\\label{tab:stepwise_lambda01}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCheckpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\\\\n\\midrule\n16K steps & 55.5 & 56.0 & -- & 55.75 \\\\\n20K steps & 55.0 & 56.0 & -- & 55.5 \\\\\n22K steps & 60.5 & 56.5 & -- & 58.5 \\\\\n24K steps & 52.5 & -- & -- & -- \\\\\n26K steps & 53.5 & -- & -- & -- \\\\\n28K steps & 54.5 & -- & -- & -- \\\\\n30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIndividual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$3\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). At 30K, the third seed ($s_2 = 54.5\\%$) falls well within the null range, pulling the three-seed mean to 57.00\\% and rendering the earlier two-seed departure non-significant ($p = 0.131$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\n\n\n\\section{Oracle SDF Refinement Details}\n\\label{sec:appendix_oracle}\n\nAll oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n\n\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n\n\\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.\n\n\\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space).\n\n\n\\section{Cross-Scene Validation: spatial\\_bowl}\n\\label{sec:appendix_spatial_bowl}\n\nTo test whether the SDF redundancy finding generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.\n\nTable~\\ref{tab:spatial_bowl} reports the results. The SDF condition ($\\lambda = 0.005$) yields CAR of 11.5\\% versus 15.5\\% for LoRA-only, a $-$4.0\\,pp difference indicating that SDF supervision is not only redundant but slightly detrimental in this scene. TSR is comparable across conditions (50.0\\% vs.\\ 51.5\\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \\texttt{object\\_pudding} findings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$4.0\\,pp CAR difference indicates SDF is not only redundant but slightly detrimental, consistent with \\texttt{object\\_pudding}.}\n\\label{tab:spatial_bowl}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & CAR (\\%) & TSR (\\%) \\\\\n\\midrule\nLoRA-only & 15.5 & 50.0 \\\\\nSDF $\\lambda{=}0.005$ & 11.5 & 51.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe substantially lower CAR on \\texttt{spatial\\_bowl} relative to \\texttt{object\\_pudding} (12--16\\% vs.\\ 54--57\\%) reflects the greater scene difficulty: \\texttt{spatial\\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition actually performs worse ($\\Delta$CAR\\,=\\,$-$4.0\\,pp), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.\n\n\n\\section{Evaluation Seed Robustness}\n\\label{sec:appendix_eval_seed}\n\nTo verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate the LoRA-only (s0) and SDF $\\lambda{=}0.1$ (s0) checkpoints under multiple evaluation seeds. Table~\\ref{tab:eval_seed_car} reports aggregate CAR and Table~\\ref{tab:eval_seed_tsr} reports aggregate TSR.\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate CAR (\\%) across evaluation seeds (200 episodes each). The LoRA vs.\\ SDF $\\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}\n\\label{tab:eval_seed_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task CAR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 60 & 70 & 68 & 28 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,123) & 52 & 74 & 66 & 20 & 53.0 \\\\\nLoRA s0 mean $\\pm$ std & 56.0$\\pm$4.0 & 72.7$\\pm$2.3 & 68.0$\\pm$2.0 & 24.7$\\pm$4.2 & 55.3$\\pm$2.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 64 & 74 & 74 & 24 & 59.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 62 & 76 & 74 & 22 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 60 & 72 & 66 & 30 & 57.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 61.5$\\pm$1.9 & 74.0$\\pm$1.6 & 70.5$\\pm$4.1 & 26.5$\\pm$4.1 & 58.1$\\pm$0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate TSR (\\%) across evaluation seeds. TSR varies more across seeds than CAR (seed\\,=\\,42 yields consistently lower TSR), but the relative ordering between LoRA and SDF is stable.}\n\\label{tab:eval_seed_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task TSR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 32 & 74 & 42 & 58 & 51.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 22 & 70 & 32 & 60 & 46.0 \\\\\nLoRA s0 (seed\\,=\\,123) & 30 & 70 & 40 & 62 & 50.5 \\\\\nLoRA s0 mean $\\pm$ std & 28.0$\\pm$5.3 & 71.3$\\pm$2.3 & 38.0$\\pm$5.3 & 60.0$\\pm$2.0 & 49.3$\\pm$3.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 28 & 78 & 44 & 60 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 18 & 78 & 42 & 72 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 26 & 82 & 38 & 68 & 53.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 28 & 74 & 32 & 58 & 48.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 25.0$\\pm$4.8 & 78.0$\\pm$3.3 & 39.0$\\pm$5.4 & 64.5$\\pm$6.6 & 51.6$\\pm$2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAcross three matched evaluation seeds (7, 42, 123), the SDF $\\lambda{=}0.1$ condition yields higher aggregate CAR than LoRA-only in all cases ($\\Delta$CAR\\,=\\,+1.5, +2.5, +5.5\\,pp). Cross-seed CAR standard deviation is 2.0\\,pp for LoRA and 0.9\\,pp for SDF, both small relative to the within-seed per-task variation. The per-task ordering (CP highest, BBQ lowest) is preserved across all seeds and both conditions, reinforcing the conclusion that avoidance patterns reflect the spatial statistics of training demonstrations.\n\n\n\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\paragraph{Architecture.}\nWe use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n\n\\paragraph{Training schedule.}\nTraining proceeds in two phases:\n\\begin{itemize}\n    \\item \\textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.\n    \\item \\textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.\n\\end{itemize}\n\n\\paragraph{Hyperparameters.}\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\label{tab:hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & Pi0.5 (OpenPi, $\\sim$3.5B parameters) \\\\\nOptimizer & AdamW \\\\\nLearning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\nWarmup steps & 1000 \\\\\nBatch size & 32 \\\\\nTotal steps & 30000 \\\\\n$\\lambda_\\mathrm{sdf}$ & \\{0.005, 0.01, 0.1\\} \\\\\n$\\lambda_\\mathrm{ee}$ & 0.01 \\\\\nSDF query points per step & 64 \\\\\nSDF clamp $\\delta$ & 0.05 m \\\\\nEikonal weight & 0.1 \\\\\nLoRA rank (vision) & 16 \\\\\nLoRA rank (action) & 32 \\\\\nPhase 1 duration & 5000 steps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nEach episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\\sim}$5\\% to ${\\sim}$52\\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).\n\n\\paragraph{Data.}\nWe use the SafeLIBERO object\\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.\n\n\\paragraph{Computational resources.}\nAll training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n",
    "structuredPatch": [
      {
        "oldStart": 177,
        "oldLines": 6,
        "newStart": 177,
        "newLines": 9,
        "lines": [
          " ",
          " The permutation test makes no distributional assumptions. Pooling the six null values $\\{56.5, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \\approx 0.131$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.",
          " ",
          "+\\paragraph{Alternative null construction (Null~A).}",
          "+If only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.",
          "+",
          " A Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.",
          " ",
          " \\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}"
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

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_01MYibtuTc3MUqB8Gz8G3PJg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "A Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.",
  "new_string": "A Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "ab8daa06-95c1-47eb-8f39-357ce9bcca59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALeSePiX4hw8hzp9siL8ut",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6833,
      "cache_read_input_tokens": 49518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6833
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

_source line 27 · 2026-05-28T05:39:40.111Z_

<details><summary>↩ Tool result · `toolu_01MYibtuTc3MUqB8Gz8G3PJg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "3d961898-e704-48a6-8a37-e74a15ffcd21",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "oldString": "A Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.",
    "newString": "A Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.",
    "originalFile": "\\section{Displacement Distribution}\n\\label{sec:appendix_displacement}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{fig2_ee_displacement_distribution}\n\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n\n\\section{Displacement Threshold Sensitivity Analysis}\n\\label{sec:appendix_threshold}\n\nTo validate the robustness of our displacement threshold $\\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% frozen rate even at the most conservative setting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Frozen rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\n$\\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\\\\n\\midrule\n0.001 mm (1\\,$\\mu$m) & 73.9 & 0.0 & 0.0 \\\\\n0.1 mm  & 99.6 & 0.0 & 0.0 \\\\\n1.0 mm  & 100.0 & 0.0 & 0.0 \\\\\n10 mm   & 100.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of $\\tau_d = 0.1$\\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\\,mm per step. Even at $\\tau_d = 1$\\,$\\mu$m, 73.9\\% of A1-LoRA safe episodes are classified as frozen, while all Pi0.5 episodes remain above threshold at every level tested.\n\nTable~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n\n\\begin{table}[h]\n\\centering\n\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n\\label{tab:dfcar_threshold}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{lcccccccc}\n\\toprule\n& \\multicolumn{8}{c}{$\\tau_d$ (mm)} \\\\\n\\cmidrule(lr){2-9}\nCondition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n\\midrule\nLoRA s0            & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\\\\nLoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\nSDF $\\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\nSDF $\\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\nSDF $\\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\nSDF $\\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nSDF $\\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\nSDF $\\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n\nTable~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\n\nTable~\\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\\S\\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) at 30K steps. $\\lambda{=}0.005$, $\\lambda{=}0.01$, and $\\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}\n\\label{tab:per_task_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\\\\nLoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\\\\nSDF $\\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\\\\nSDF $\\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\\\\nSDF $\\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\\\\nSDF $\\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor the $\\lambda = 0.1$ condition, seed~1 records \\texttt{avg\\_max\\_obstacle\\_displacement} of 0.0553\\,m (per-task: OJ\\,=\\,0.033, CP\\,=\\,0.055, Milk\\,=\\,0.041, BBQ\\,=\\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than frozen behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_pertask_car_fingerprint}\n\\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all $\\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}\n\\label{fig:pertask_fingerprint}\n\\end{figure}\n\n\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n\nTable~\\ref{tab:ssr} reports the Safe Success Rate (SSR\\,=\\,TSR\\,$\\cap$\\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\n\\label{tab:ssr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\n\\midrule\nPi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\\\\nLoRA-only (3 seeds) & 51.5 & 54.67 & 27.7 & 0.54 \\\\\nSDF $\\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\\\\nSDF $\\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\\\\nSDF $\\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Oracle Analysis}\n\\label{sec:appendix_pertask}\n\\label{sec:appendix_pertask_oracle}\n\nTable~\\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.\n\nThe feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\n\\label{tab:oracle_pertask}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\\\\n\\midrule\nLoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\\\\n\\midrule\nOracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\\\\nOracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\\\\nOracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the three LoRA-only seeds and three $\\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 55.0\\% (LoRA s2), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.58\\% and standard deviation 1.93\\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 57.00\\% (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\\alpha = 0.05$).\n\nThe permutation test makes no distributional assumptions. Pooling the six null values $\\{56.5, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \\approx 0.131$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.131$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.131$, two-tailed permutation).}\n\\label{tab:stepwise_lambda01}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCheckpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\\\\n\\midrule\n16K steps & 55.5 & 56.0 & -- & 55.75 \\\\\n20K steps & 55.0 & 56.0 & -- & 55.5 \\\\\n22K steps & 60.5 & 56.5 & -- & 58.5 \\\\\n24K steps & 52.5 & -- & -- & -- \\\\\n26K steps & 53.5 & -- & -- & -- \\\\\n28K steps & 54.5 & -- & -- & -- \\\\\n30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIndividual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$3\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). At 30K, the third seed ($s_2 = 54.5\\%$) falls well within the null range, pulling the three-seed mean to 57.00\\% and rendering the earlier two-seed departure non-significant ($p = 0.131$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\n\n\n\\section{Oracle SDF Refinement Details}\n\\label{sec:appendix_oracle}\n\nAll oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n\n\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n\n\\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.\n\n\\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space).\n\n\n\\section{Cross-Scene Validation: spatial\\_bowl}\n\\label{sec:appendix_spatial_bowl}\n\nTo test whether the SDF redundancy finding generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.\n\nTable~\\ref{tab:spatial_bowl} reports the results. The SDF condition ($\\lambda = 0.005$) yields CAR of 11.5\\% versus 15.5\\% for LoRA-only, a $-$4.0\\,pp difference indicating that SDF supervision is not only redundant but slightly detrimental in this scene. TSR is comparable across conditions (50.0\\% vs.\\ 51.5\\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \\texttt{object\\_pudding} findings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$4.0\\,pp CAR difference indicates SDF is not only redundant but slightly detrimental, consistent with \\texttt{object\\_pudding}.}\n\\label{tab:spatial_bowl}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & CAR (\\%) & TSR (\\%) \\\\\n\\midrule\nLoRA-only & 15.5 & 50.0 \\\\\nSDF $\\lambda{=}0.005$ & 11.5 & 51.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe substantially lower CAR on \\texttt{spatial\\_bowl} relative to \\texttt{object\\_pudding} (12--16\\% vs.\\ 54--57\\%) reflects the greater scene difficulty: \\texttt{spatial\\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition actually performs worse ($\\Delta$CAR\\,=\\,$-$4.0\\,pp), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.\n\n\n\\section{Evaluation Seed Robustness}\n\\label{sec:appendix_eval_seed}\n\nTo verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate the LoRA-only (s0) and SDF $\\lambda{=}0.1$ (s0) checkpoints under multiple evaluation seeds. Table~\\ref{tab:eval_seed_car} reports aggregate CAR and Table~\\ref{tab:eval_seed_tsr} reports aggregate TSR.\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate CAR (\\%) across evaluation seeds (200 episodes each). The LoRA vs.\\ SDF $\\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}\n\\label{tab:eval_seed_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task CAR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 60 & 70 & 68 & 28 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,123) & 52 & 74 & 66 & 20 & 53.0 \\\\\nLoRA s0 mean $\\pm$ std & 56.0$\\pm$4.0 & 72.7$\\pm$2.3 & 68.0$\\pm$2.0 & 24.7$\\pm$4.2 & 55.3$\\pm$2.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 64 & 74 & 74 & 24 & 59.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 62 & 76 & 74 & 22 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 60 & 72 & 66 & 30 & 57.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 61.5$\\pm$1.9 & 74.0$\\pm$1.6 & 70.5$\\pm$4.1 & 26.5$\\pm$4.1 & 58.1$\\pm$0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate TSR (\\%) across evaluation seeds. TSR varies more across seeds than CAR (seed\\,=\\,42 yields consistently lower TSR), but the relative ordering between LoRA and SDF is stable.}\n\\label{tab:eval_seed_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task TSR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 32 & 74 & 42 & 58 & 51.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 22 & 70 & 32 & 60 & 46.0 \\\\\nLoRA s0 (seed\\,=\\,123) & 30 & 70 & 40 & 62 & 50.5 \\\\\nLoRA s0 mean $\\pm$ std & 28.0$\\pm$5.3 & 71.3$\\pm$2.3 & 38.0$\\pm$5.3 & 60.0$\\pm$2.0 & 49.3$\\pm$3.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 28 & 78 & 44 & 60 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 18 & 78 & 42 & 72 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 26 & 82 & 38 & 68 & 53.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 28 & 74 & 32 & 58 & 48.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 25.0$\\pm$4.8 & 78.0$\\pm$3.3 & 39.0$\\pm$5.4 & 64.5$\\pm$6.6 & 51.6$\\pm$2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAcross three matched evaluation seeds (7, 42, 123), the SDF $\\lambda{=}0.1$ condition yields higher aggregate CAR than LoRA-only in all cases ($\\Delta$CAR\\,=\\,+1.5, +2.5, +5.5\\,pp). Cross-seed CAR standard deviation is 2.0\\,pp for LoRA and 0.9\\,pp for SDF, both small relative to the within-seed per-task variation. The per-task ordering (CP highest, BBQ lowest) is preserved across all seeds and both conditions, reinforcing the conclusion that avoidance patterns reflect the spatial statistics of training demonstrations.\n\n\n\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\paragraph{Architecture.}\nWe use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n\n\\paragraph{Training schedule.}\nTraining proceeds in two phases:\n\\begin{itemize}\n    \\item \\textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.\n    \\item \\textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.\n\\end{itemize}\n\n\\paragraph{Hyperparameters.}\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\label{tab:hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & Pi0.5 (OpenPi, $\\sim$3.5B parameters) \\\\\nOptimizer & AdamW \\\\\nLearning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\nWarmup steps & 1000 \\\\\nBatch size & 32 \\\\\nTotal steps & 30000 \\\\\n$\\lambda_\\mathrm{sdf}$ & \\{0.005, 0.01, 0.1\\} \\\\\n$\\lambda_\\mathrm{ee}$ & 0.01 \\\\\nSDF query points per step & 64 \\\\\nSDF clamp $\\delta$ & 0.05 m \\\\\nEikonal weight & 0.1 \\\\\nLoRA rank (vision) & 16 \\\\\nLoRA rank (action) & 32 \\\\\nPhase 1 duration & 5000 steps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nEach episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\\sim}$5\\% to ${\\sim}$52\\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).\n\n\\paragraph{Data.}\nWe use the SafeLIBERO object\\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.\n\n\\paragraph{Computational resources.}\nAll training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n",
    "structuredPatch": [
      {
        "oldStart": 180,
        "oldLines": 7,
        "newStart": 180,
        "newLines": 7,
        "lines": [
          " \\paragraph{Alternative null construction (Null~A).}",
          " If only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.",
          " ",
          "-A Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--30K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 57.5\\% (single seed, s2). This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.",
          "+A Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.",
          " ",
          " \\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}",
          " \\label{sec:appendix_stepwise}"
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

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now let me verify the edits and run paper_switch.py --verify. Let me also read the modified files to confirm.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "ba43ad21-4265-46f9-b83e-57ff0117ed02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FiGkYzvfexYHhgViSEcsn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5936,
      "cache_read_input_tokens": 56351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5936
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

Now let me verify paper_switch.py templates still match.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "1be7e814-6b69-46ef-bfe8-f883c131eb5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FiGkYzvfexYHhgViSEcsn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5936,
      "cache_read_input_tokens": 56351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5936
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

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01Py5Z5vcvR9XNnRzrB8poeK`</summary>

```json
{
  "command": "python3 artifacts/paper_switch.py --verify",
  "description": "Verify paper_switch.py templates still match"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "d2dcf5b4-87dc-4a48-915b-38a5a9aeba66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015FiGkYzvfexYHhgViSEcsn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5936,
      "cache_read_input_tokens": 56351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5936
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

_source line 31 · 2026-05-28T05:39:46.361Z_

<details><summary>↩ Tool result · `toolu_01Py5Z5vcvR9XNnRzrB8poeK`</summary>

```text
--- Scenario B (10 items) ---
  [OK]      abstract L5 training                abstract.tex
  [OK]      abstract L6 conclusion              abstract.tex
  [OK]      claim3 L3 scope                     claim3.tex
  [OK]      claim3 L7 caption                   claim3.tex
  [OK]      claim3 L20 table row                claim3.tex
  [OK]      claim3 L27 body                     claim3.tex
  [OK]      claim3 L32-33 dose-response         claim3.tex
  [OK]      claim3 L38 fig caption              claim3.tex
  [OK]      discussion L6                       discussion.tex
  [OK]      discussion L12 limitation           discussion.tex
--- Scenario C (11 items) ---
  [OK]      abstract L5 training                abstract.tex
  [OK]      abstract L6 conclusion              abstract.tex
  [OK]      claim3 L3 scope                     claim3.tex
  [OK]      claim3 L7 caption                   claim3.tex
  [OK]      claim3 L20 table row                claim3.tex
  [OK]      claim3 L27 body                     claim3.tex
  [OK]      claim3 L32-33 dose-response         claim3.tex
  [OK]      claim3 L38 fig caption              claim3.tex
  [OK]      discussion L3 scope                 discussion.tex
  [OK]      discussion L6                       discussion.tex
  [OK]      discussion L12 limitation           discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "f63874d2-3c3e-4828-9bc5-357f8a6b3e65",
  "tool_use_result": {
    "stdout": "--- Scenario B (10 items) ---\n  [OK]      abstract L5 training                abstract.tex\n  [OK]      abstract L6 conclusion              abstract.tex\n  [OK]      claim3 L3 scope                     claim3.tex\n  [OK]      claim3 L7 caption                   claim3.tex\n  [OK]      claim3 L20 table row                claim3.tex\n  [OK]      claim3 L27 body                     claim3.tex\n  [OK]      claim3 L32-33 dose-response         claim3.tex\n  [OK]      claim3 L38 fig caption              claim3.tex\n  [OK]      discussion L6                       discussion.tex\n  [OK]      discussion L12 limitation           discussion.tex\n--- Scenario C (11 items) ---\n  [OK]      abstract L5 training                abstract.tex\n  [OK]      abstract L6 conclusion              abstract.tex\n  [OK]      claim3 L3 scope                     claim3.tex\n  [OK]      claim3 L7 caption                   claim3.tex\n  [OK]      claim3 L20 table row                claim3.tex\n  [OK]      claim3 L27 body                     claim3.tex\n  [OK]      claim3 L32-33 dose-response         claim3.tex\n  [OK]      claim3 L38 fig caption              claim3.tex\n  [OK]      discussion L3 scope                 discussion.tex\n  [OK]      discussion L6                       discussion.tex\n  [OK]      discussion L12 limitation           discussion.tex",
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

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
All templates match. Now let me verify the final state of the files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "3887b150-87a7-4707-8e4f-e0f35c5199b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2fsEsA4FVx6YyWcm4joMn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 546,
      "cache_read_input_tokens": 62287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 546
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

All 21 template matches pass. Let me verify the final state of both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "f3b0e9f2-90cc-4636-aa5b-2acffe87e5b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2fsEsA4FVx6YyWcm4joMn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 546,
      "cache_read_input_tokens": 62287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 546
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

<details open><summary>🔧 Tool call — Read · `toolu_01VTVZqUH14eioaHHhHCbeN1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "663a9593-1d0d-4695-8d7c-441fcddf9af5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2fsEsA4FVx6YyWcm4joMn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 546,
      "cache_read_input_tokens": 62287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 546
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

_source line 35 · 2026-05-28T05:39:52.599Z_

<details><summary>↩ Tool result · `toolu_01VTVZqUH14eioaHHhHCbeN1`</summary>

```text
1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across the full tested range $\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 3 & 51.5\,$\pm$\,0.0 & 54.67\,$\pm$\,2.02 & 0.391 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.29 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.33\,$\pm$\,1.61 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$ & 3 & 50.2\,$\pm$\,3.9 & 57.00\,$\pm$\,2.18 & 0.394 \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	\end{table}
25	
26	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ (57.00\%, $p = 0.131$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,57.5\%\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce lowest) and invariant to $\lambda$ across a 20$\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.
27	
28	\paragraph{CAR--TSR trade-off.}\label{sec:tsr_collapse}
29	Fine-tuning degrades TSR by ${\sim}$18--20\,pp (71.5\% $\to$ 51.5--54.0\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\,0.37\,m displacement and 0\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.
30	
31	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
32	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,57.00\%\,$\pm$\,2.18 at the 30K checkpoint (3 seeds: 58.0\%, 58.5\%, 54.5\%), within the null distribution (mean 54.58\%, $\sigma = 1.93$; permutation $p = 0.131$\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \emph{decrease} CAR, the result remains non-significant.}). SDF supervision is redundant with the demonstration signal across the full tested range $\lambda \in [0.005, 0.1]$ (Figure~\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\ref{sec:conclusion}): because even a 20$\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.
33	
34	\paragraph{Robustness to null construction.}
35	The preceding permutation test pools LoRA-only and $\lambda = 0.005$ seeds as a single null (Null~B, $\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\alpha = 0.05$.
36	
37	\paragraph{Statistical power.}
38	With $n = 3$ seeds per group and $\sigma \approx 2.0$\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\alpha = 0.05$ (one-tailed) achieves 80\% power only for effects $\geq 5.0$\,pp. The observed effect of ${\sim}$2.3\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.
39	
40	\paragraph{Evaluation-seed consistency.}
41	Under matched evaluation conditions (Appendix~\ref{sec:appendix_eval_seed}), SDF $\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\,pp), with lower cross-seed variance ($\sigma = 0.9$\,pp vs.\ 2.0\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\sim}$2.3\,pp) falls well below the study's MDE (${\sim}$5\,pp at 80\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.
42	
43	\begin{figure}[t]
44	\centering
45	\includegraphics[width=0.85\linewidth]{fig5_lambda_curve}
46	\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. All tested $\lambda$ values remain within the null band ($p > 0.05$), confirming full redundancy of EE-only SDF supervision across a 20$\times$ loss-weight range.}
47	\label{fig:lambda_car}
48	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "06a02c3d-4468-4e2b-ada2-b73fc4ca7bbc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
      "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across the full tested range $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 3 & 51.5\\,$\\pm$\\,0.0 & 54.67\\,$\\pm$\\,2.02 & 0.391 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$ & 3 & 50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$18--20\\,pp (71.5\\% $\\to$ 51.5--54.0\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.\n\n\\paragraph{Robustness to null construction.}\nThe preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.\n\n\\paragraph{Statistical power.}\nWith $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.\n\n\\paragraph{Evaluation-seed consistency.}\nUnder matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within the null band ($p > 0.05$), confirming full redundancy of EE-only SDF supervision across a 20$\\times$ loss-weight range.}\n\\label{fig:lambda_car}\n\\end{figure}",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_016YJkqFf6659dPoM5YcmvAr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "offset": 173,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "6bbe486b-2455-4be3-83ff-9954ce46dfa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M2fsEsA4FVx6YyWcm4joMn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 546,
      "cache_read_input_tokens": 62287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 546
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

_source line 37 · 2026-05-28T05:39:53.139Z_

<details><summary>↩ Tool result · `toolu_016YJkqFf6659dPoM5YcmvAr`</summary>

```text
173	\section{Null Distribution for SDF Loss Weight Analysis}
174	\label{sec:appendix_null}
175	
176	We construct a null distribution by pooling the three LoRA-only seeds and three $\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\% (LoRA s0, re-evaluated), 52.5\% (LoRA s1), 55.0\% (LoRA s2), 57.0\% ($\lambda{=}0.005$ s0), 54.0\% ($\lambda{=}0.005$ s1), 52.5\% ($\lambda{=}0.005$ s2), yielding mean 54.58\% and standard deviation 1.93\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\lambda = 0.005$ produces no separation from LoRA-only. The $\lambda = 0.01$ mean of 56.33\% falls within $0.8\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\lambda = 0.1$ 30K mean of 57.00\% (3 seeds: 58.0\%, 58.5\%, 54.5\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\alpha = 0.05$).
177	
178	The permutation test makes no distributional assumptions. Pooling the six null values $\{56.5, 52.5, 55, 57, 54, 52.5\}$ and three $\lambda = 0.1$ values $\{58, 58.5, 54.5\}$ into nine measurements, we enumerate all $\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \approx 0.131$. With the third seed ($s_2 = 54.5\%$) pulling the $\lambda = 0.1$ mean from 58.25\% (2 seeds) down to 57.00\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.
179	
180	\paragraph{Alternative null construction (Null~A).}
181	If only the three LoRA-only seeds are used as the null pool ($\{56.5, 52.5, 55.0\}$), we obtain $\binom{6}{3} = 20$ permutations for each comparison. For $\lambda = 0.1$ (treatment mean 57.00\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\lambda = 0.01$ (treatment mean 56.33\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\lambda = 0.01$ yields one-tailed $p = 10/84 \approx 0.119$, two-tailed $p = 22/84 \approx 0.262$. All tests are non-significant at $\alpha = 0.05$; the narrower Null~A yields \emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\%), making the treatment means less extreme by comparison.
182	
183	A Phase~2 ablation reinforces this conclusion. Setting $\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.
184	
185	\section{Step-wise Checkpoint Analysis for \texorpdfstring{$\lambda = 0.1$}{lambda = 0.1}}
186	\label{sec:appendix_stepwise}
187	
188	Table~\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\%) pulls the three-seed mean to 57.00\%, within the null band ($p = 0.131$).
189	
190	\begin{table}[h]
191	\centering
192	\caption{Per-seed CAR (\%) at training checkpoints for $\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\%) remains within the null band ($p = 0.131$, two-tailed permutation).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "2ccf1549-2fa4-4252-8abf-55f9c4434eaf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
      "content": "\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the three LoRA-only seeds and three $\\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 55.0\\% (LoRA s2), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.58\\% and standard deviation 1.93\\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 57.00\\% (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\\alpha = 0.05$).\n\nThe permutation test makes no distributional assumptions. Pooling the six null values $\\{56.5, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \\approx 0.131$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.131$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.131$, two-tailed permutation).}",
      "numLines": 20,
      "startLine": 173,
      "totalLines": 360
    }
  }
}
```

</details>

---

### Assistant

_source line 38_

All edits applied, all paper_switch.py templates verified. Here's the summary:

---

## Changes Made

### claim3.tex (lines 34–41 added)

| Line | Change |
|------|--------|
| 34–35 | **NEW** `\paragraph{Robustness to null construction.}` — Reports Null A (LoRA-only, p_two=0.300) and Null B (p_two=0.131), both non-significant |
| 37–38 | **NEW** `\paragraph{Statistical power.}` — MDE ≈ 5.0 pp at 80% power; observed effect ~2.3 pp is underpowered |
| 40–41 | **NEW** `\paragraph{Evaluation-seed consistency.}` — References Appendix J (+1.5/+2.5/+5.5 pp, σ=0.9 vs 2.0), concludes with cautious "cannot be resolved at current sample size" |

### appendix.tex

| Line | Change |
|------|--------|
| 180–181 | **NEW** `\paragraph{Alternative null construction (Null~A).}` — Exact p-values for λ=0.1 (p_two=0.300) and λ=0.01 (p_two=0.400) under Null A; also λ=0.01 under Null B (p_two=0.262) |
| 183 | **MODIFIED** Phase 2 ablation: 57.5% → 58.0%, "steps 5K–30K" → "steps 5K–18K", added "at the 18K checkpoint (13K steps of Phase~2 training)" + footnote about disk constraints |

---

## Managed Blocks Requiring Your Attention (flagged, not modified)

These contain absolute wording ("redundant", "no measurable benefit", etc.) or the 57.5% value, but are managed by paper_switch.py:

1. **claim3.tex L7** (caption): "SDF adds no measurable CAR beyond LoRA-only across the full tested range"
2. **claim3.tex L26** (body): "Adding SDF supervision produces no measurable benefit across the full tested range" + "confirming that SDF gradients produce no lasting behavioral effect" + **"CAR\,=\,57.5\%"** (Phase 2, needs → 58.0%)
3. **claim3.tex L32** (dose-response): "SDF supervision is redundant with the demonstration signal across the full tested range"
4. **claim3.tex L46** (fig caption): "confirming full redundancy of EE-only SDF supervision"

All four need updating in `paper_switch.py`'s `old` and `new` templates (both Scenario B and C) to:
- Replace absolute wording with cautious phrasing
- Change `57.5\%` → `58.0\%` with the 18K checkpoint note

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "uuid": "788e7cc1-e6c0-477d-b877-397202af313f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UhjZPM7Q524fgPVJajLdBs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3878,
      "cache_read_input_tokens": 62833,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3878
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

_source line 39_

All edits applied, all paper_switch.py templates verified. Here's the summary:

---

## Changes Made

### claim3.tex (lines 34–41 added)

| Line | Change |
|------|--------|
| 34–35 | **NEW** `\paragraph{Robustness to null construction.}` — Reports Null A (LoRA-only, p_two=0.300) and Null B (p_two=0.131), both non-significant |
| 37–38 | **NEW** `\paragraph{Statistical power.}` — MDE ≈ 5.0 pp at 80% power; observed effect ~2.3 pp is underpowered |
| 40–41 | **NEW** `\paragraph{Evaluation-seed consistency.}` — References Appendix J (+1.5/+2.5/+5.5 pp, σ=0.9 vs 2.0), concludes with cautious "cannot be resolved at current sample size" |

### appendix.tex

| Line | Change |
|------|--------|
| 180–181 | **NEW** `\paragraph{Alternative null construction (Null~A).}` — Exact p-values for λ=0.1 (p_two=0.300) and λ=0.01 (p_two=0.400) under Null A; also λ=0.01 under Null B (p_two=0.262) |
| 183 | **MODIFIED** Phase 2 ablation: 57.5% → 58.0%, "steps 5K–30K" → "steps 5K–18K", added "at the 18K checkpoint (13K steps of Phase~2 training)" + footnote about disk constraints |

---

## Managed Blocks Requiring Your Attention (flagged, not modified)

These contain absolute wording ("redundant", "no measurable benefit", etc.) or the 57.5% value, but are managed by paper_switch.py:

1. **claim3.tex L7** (caption): "SDF adds no measurable CAR beyond LoRA-only across the full tested range"
2. **claim3.tex L26** (body): "Adding SDF supervision produces no measurable benefit across the full tested range" + "confirming that SDF gradients produce no lasting behavioral effect" + **"CAR\,=\,57.5\%"** (Phase 2, needs → 58.0%)
3. **claim3.tex L32** (dose-response): "SDF supervision is redundant with the demonstration signal across the full tested range"
4. **claim3.tex L46** (fig caption): "confirming full redundancy of EE-only SDF supervision"

All four need updating in `paper_switch.py`'s `old` and `new` templates (both Scenario B and C) to:
- Replace absolute wording with cautious phrasing
- Change `57.5\%` → `58.0\%` with the 18K checkpoint note

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 301430,
  "duration_api_ms": 301818,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "49b5972e-8588-4fd2-8cb8-d739926d75ee",
  "total_cost_usd": 0.911847,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 55260,
    "cache_read_input_tokens": 313776,
    "output_tokens": 16256,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 55260,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 728,
        "cache_read_input_tokens": 62833,
        "cache_creation_input_tokens": 3878,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3878
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3039,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003139,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 16256,
      "cacheReadInputTokens": 313776,
      "cacheCreationInputTokens": 55260,
      "webSearchRequests": 0,
      "costUSD": 0.908708,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bf45c8ab-91a7-4f67-9f7b-d947f3c34633"
}
```

</details>

---
