# paper urgent wording sync

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/workers/worker_paper_urgent-wording-sync_20260528T055424.log`
- **Structured JSON:** [`a137618f7527e447e55e.json`](../../sessions/a1/a137618f7527e447e55e.json)

## Before a recorded user message

61 recorded events

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
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
  "uuid": "f54606b9-9ea7-494a-9915-114b58aa77a1",
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
  "uuid": "8e433c0c-5da3-420c-a45f-3defc543886b",
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9"
}
```

---

### Assistant

_source line 4_

I'll start by reading the key files to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "bff0839c-4695-48e6-9c52-da698576923b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAFaZTvmqLeLBjJv4kTNU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13243,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13243
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

<details open><summary>🔧 Tool call — Read · `toolu_01Xyp3d1mSbYTokGFZQQAsaV`</summary>

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "5165003e-afe5-4b13-b68f-1f3ec771a6b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAFaZTvmqLeLBjJv4kTNU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13243,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13243
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

_source line 6 · 2026-05-28T05:54:36.629Z_

<details><summary>↩ Tool result · `toolu_01Xyp3d1mSbYTokGFZQQAsaV`</summary>

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "a35bae96-44d2-4106-ac8f-f3f25feecd96",
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

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01X6VU9o2eUwYLozBGQcBaYY`</summary>

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "ffdcec9b-aef8-4ac2-9eae-eb533db24162",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAFaZTvmqLeLBjJv4kTNU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13243,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13243
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

_source line 8 · 2026-05-28T05:54:37.228Z_

<details><summary>↩ Tool result · `toolu_01X6VU9o2eUwYLozBGQcBaYY`</summary>

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "6d6e6028-9c67-4a40-be27-7c7be0328c98",
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

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_017XNVorn6XcuWYeFcPMghEd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "f62f814f-503b-4606-961a-9648e9846064",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAFaZTvmqLeLBjJv4kTNU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13243,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13243
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

_source line 10 · 2026-05-28T05:54:37.933Z_

<details><summary>↩ Tool result · `toolu_017XNVorn6XcuWYeFcPMghEd`</summary>

```text
1	\begin{abstract}
2	Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.
3	On SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\% CAR while 99.6\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\,mm. The robot is frozen, not safe.
4	We introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\,mm threshold range.
5	We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\sim}$26 percentage points). SDF supervision adds no measurable benefit across the full tested range $\lambda \in \{0.005, 0.01, 0.1\}$ ($p > 0.05$ for all; $\lambda = 0.1$: 57.00\%$\,\pm\,$2.18, 3 seeds).
6	Displacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision is fully redundant across a 20$\times$ loss-weight range, confirming that collision avoidance arises from demonstration data, not geometric supervision.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "58c15a21-9630-4a11-aa93-f305dfbca91a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nVision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.\nOn SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\\% CAR while 99.6\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\,mm. The robot is frozen, not safe.\nWe introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\\,mm threshold range.\nWe further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\\sim}$26 percentage points). SDF supervision adds no measurable benefit across the full tested range $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for all; $\\lambda = 0.1$: 57.00\\%$\\,\\pm\\,$2.18, 3 seeds).\nDisplacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision is fully redundant across a 20$\\times$ loss-weight range, confirming that collision avoidance arises from demonstration data, not geometric supervision.\n\\end{abstract}\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01Dbt5SdyM7rqLz9LNfnMfwE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "1b456e74-bba9-4b0f-82df-e40ed6caf0ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAFaZTvmqLeLBjJv4kTNU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13243,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13243
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

_source line 12 · 2026-05-28T05:54:38.351Z_

<details><summary>↩ Tool result · `toolu_01Dbt5SdyM7rqLz9LNfnMfwE`</summary>

```text
1	\section{Introduction}\label{sec:intro}
2	
3	Collision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\cite{zhang2025safevla}, constraint-based planning~\cite{yang2025cape}, and collision-free demonstrations~\cite{cofreeevla2026}. Our SDF-augmented Pi0~\cite{black2024pi0} reaches 91.5\% CAR across 800 episodes. The problem appears close to solved.
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\linewidth]{fig1_teaser}
8	\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\tau_d$; Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes, and dfCAR equals raw CAR (right).}
9	\label{fig:teaser}
10	\end{figure}
11	
12	It is not (Figure~\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\% exhibit displacement below 0.1\,mm; TSR is 0\% across all 800 episodes. The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\ref{sec:fake_safety}). We term this \emph{fake safety}: \emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\cite{karwowski2024goodhart}.
13	
14	We present a systematic investigation of this problem across the Pi0 and Pi0.5~\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.
15	
16	\textbf{Fake safety is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\tau_d$. dfCAR collapses Pi0+A1 from 91.5\% to ${\approx}$\,0\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\,=\,71.5\%, CAR\,=\,28.5\%, with every safe episode above 288\,mm displacement and dfCAR equal to raw CAR (Section~\ref{sec:fake_safety}).
17	
18	\textbf{EE-only SDF refinement is structurally counterproductive.} Three ground-truth oracle variants all achieve \emph{lower} CAR than unrefined baselines (73.1--76.9\% vs.\ 82--83\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\ref{sec:ee_only}).
19	
20	\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\sim}$26 points with zero frozen episodes. Adding SDF supervision produces no measurable benefit across the full tested range $\lambda \in [0.005, 0.1]$ ($p > 0.05$ for all; $\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution accounts for all observed avoidance (Section~\ref{sec:avoidance_source}).
21	
22	Our contributions are:
23	\begin{itemize}
24	    \item \textbf{dfCAR metric:} displacement-filtered CAR that separates genuine avoidance from action collapse, robust across $\tau_d \in [2, 200]$\,mm.
25	    \item \textbf{Fake safety diagnosis:} 100+ experiments across Pi0/Pi0.5 showing $>$99\% of Pi0 safe episodes are action-collapse artifacts.
26	    \item \textbf{EE-only SDF is counterproductive:} ground-truth oracle refinement \emph{reduces} CAR below unrefined baselines by redistributing collisions to unmonitored arm links.
27	    \item \textbf{Demonstration sufficiency:} collision-free demonstrations account for all measured CAR gains (${\sim}$26\,pp); SDF supervision adds no measurable benefit across the full tested range $\lambda \in [0.005, 0.1]$ ($p > 0.05$ for all, 3 seeds).
28	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "8568e3fb-2bad-4cd2-a303-abdd52ce67a9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:intro}\n\nCollision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}. Our SDF-augmented Pi0~\\cite{black2024pi0} reaches 91.5\\% CAR across 800 episodes. The problem appears close to solved.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig1_teaser}\n\\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\\tau_d$; Pi0+A1's 91.5\\% safety score drops to ${\\approx}$\\,0\\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\\,mm in all safe episodes, and dfCAR equals raw CAR (right).}\n\\label{fig:teaser}\n\\end{figure}\n\nIt is not (Figure~\\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\\% exhibit displacement below 0.1\\,mm; TSR is 0\\% across all 800 episodes. The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\\ref{sec:fake_safety}). We term this \\emph{fake safety}: \\emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\\cite{karwowski2024goodhart}.\n\nWe present a systematic investigation of this problem across the Pi0 and Pi0.5~\\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.\n\n\\textbf{Fake safety is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\\tau_d$. dfCAR collapses Pi0+A1 from 91.5\\% to ${\\approx}$\\,0\\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\\,=\\,71.5\\%, CAR\\,=\\,28.5\\%, with every safe episode above 288\\,mm displacement and dfCAR equal to raw CAR (Section~\\ref{sec:fake_safety}).\n\n\\textbf{EE-only SDF refinement is structurally counterproductive.} Three ground-truth oracle variants all achieve \\emph{lower} CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n\n\\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\\sim}$26 points with zero frozen episodes. Adding SDF supervision produces no measurable benefit across the full tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for all; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution accounts for all observed avoidance (Section~\\ref{sec:avoidance_source}).\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{dfCAR metric:} displacement-filtered CAR that separates genuine avoidance from action collapse, robust across $\\tau_d \\in [2, 200]$\\,mm.\n    \\item \\textbf{Fake safety diagnosis:} 100+ experiments across Pi0/Pi0.5 showing $>$99\\% of Pi0 safe episodes are action-collapse artifacts.\n    \\item \\textbf{EE-only SDF is counterproductive:} ground-truth oracle refinement \\emph{reduces} CAR below unrefined baselines by redistributing collisions to unmonitored arm links.\n    \\item \\textbf{Demonstration sufficiency:} collision-free demonstrations account for all measured CAR gains (${\\sim}$26\\,pp); SDF supervision adds no measurable benefit across the full tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for all, 3 seeds).\n\\end{itemize}",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01FB4W45HMtoXoReEaSxbjDA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "402ae5ec-07ae-4340-92d6-d31e7a7a9d38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAFaZTvmqLeLBjJv4kTNU5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13243,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13243
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

_source line 14 · 2026-05-28T05:54:38.460Z_

<details><summary>↩ Tool result · `toolu_01FB4W45HMtoXoReEaSxbjDA`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations, not geometric supervision, account for the measured avoidance gains (\S\ref{sec:avoidance_source}).
4	
5	\paragraph{Why EE-only SDF fails.}
6	Two independent causes explain the null result. \textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$26\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). Even at $\lambda = 0.1$ (20$\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), confirming that Level~A signal masking is not the binding constraint---the failure is architectural. \textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \emph{reduces} CAR by 6--10\,pp below unrefined baselines (\S\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.
7	
8	\paragraph{Implications for evaluation.}
9	dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\times$ parameter range (Pi0 Full-FT ${\sim}$2.5B to Pi0+A1 ${\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.
10	
11	\paragraph{Limitations.}
12	Our evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\approx}$0\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\sim}$18--20\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.
13	
14	\paragraph{Future work.}
15	Three directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.
16	
17	\paragraph{Broader impact.}
18	Contaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "857f0bd0-1ad0-43e3-ab02-1448ac712457",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations, not geometric supervision, account for the measured avoidance gains (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), confirming that Level~A signal masking is not the binding constraint---the failure is architectural. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
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
Now I have a clear picture of all the files. Let me plan the changes systematically.

The key insight: `paper_switch.py` uses `old` strings that must match exactly what's currently in the tex files. Scenario B is the "null result" scenario (currently applied), and Scenario C is the "modest but significant" scenario. The `--verify` mode checks that `old` strings from both scenarios B and C match the current tex content.

Wait - looking at the verify logic more carefully: it checks that the `old` string from each replacement exists in the current file. Since both Scenario B and C share the same `old` strings, verify checks that those old strings are present. The old strings represent the "pre-switch" state of the tex files.


Now I'm checking the actual tex files against the replacement strings. In claim3.tex, I need to update the caption on line 7 from the current phrasing about "no measurable CAR" to language about "no statistically significant" improvement, and similarly update the body text on line 26 to reflect the same shift in terminology.

I also need to change the CAR value from 57.5% to 58.0%, update the footnote to specify the checkpoint details and training constraints, and revise several other statements throughout the file to use "statistically significant" language instead of "no measurable" or "redundant" phrasing. Line 46 appears to be cut off, so I'll need to see what change is required there.

For the abstract, I'm softening the claims about SDF supervision—changing from absolute statements about redundancy to more measured language about lack of statistical significance, and adjusting the p-value notation to be more specific about which lambda values were tested. The introduction changes will need to be compressed into brief prose once I see what's there.

The key challenge is that paper_switch.py controls some of these text replacements, so I need to track which blocks it manages and update both the source tex files and the corresponding old/new strings in the script to keep everything synchronized. I'm mapping out the remaining locations in claim3.tex and discussion.tex that need updates—items 7 through 11 covering the dose-response analysis, figure captions, and discussion sections about redundancy and architectural constraints. The key insight is that I need to update both the old strings in the Python switch file and the corresponding LaTeX content in parallel to ensure consistency across all the redundancy claims. benefit at the tested scale" and update the p-value statement to "$p > 0.05$ for $\lambda \in \{0.01, 0.1\}$". But wait, the original says $p > 0.05$ for all tested lambdas, so I need to check if the user actually wants to exclude $\lambda = 0.005$ or if there's a reason for this specificity. Let me just apply the exact changes the user specified. I see the issue now—I need to update the tex file itself to use the more precise language, then make sure the `old` string in the script matches that updated text. Then both Scenario B and C need their `new` strings adjusted to also reflect this nuanced phrasing. Let me work through each block systematically, starting with the abstract section. Updating the text string in the code to reflect the revised wording about SDF supervision's statistical significance... I need to be careful about how I'm handling the relationship between the old and new strings—they're independent, so changing one doesn't require updating the other. The key is to focus on the user's explicit instructions about avoiding absolute language like "adds nothing" or "completely ineffective," and Scenario C's current phrasing of "adds no significant benefit" for the lower lambda values is actually appropriate since those cases genuinely show no statistical significance.

Let me map out the systematic changes needed across the files, starting with claim3.tex and working through each managed block in paper_switch.py. I'm noticing an inconsistency in the statistical reporting—the revised abstract claims p > 0.05 for specific lambda values, but I need to check whether lambda = 0.005 actually meets that threshold based on the table data, since excluding it from the statement might misrepresent the results. R = 54.5%, which is even closer to LoRA-only (54.67%). So $p > 0.05$ should also hold for $\lambda = 0.005$. The user might have specific reasons for this change though. Let me just follow the instructions.

Hmm, but that doesn't make sense scientifically. If $p > 0.05$ for all three lambdas, why would we only state it for two? Unless the user wants to exclude $\lambda = 0.005$ because it wasn't formally tested or something. Let me just follow the instructions exactly.

#### 2b. L6 (managed by paper_switch.py block #2)
- "EE-only geometric supervision is fully redundant" → "EE-only geometric supervision does not significantly improve collision avoidance"
- "confirming that collision avoidance arises from demonstration data, not geometric supervision" → "suggesting that collision avoidance primarily arises from demonstration data rather than geometric supervision"

### 3. introduction.tex changes (NOT managed by paper_switch.py)

Now I need to find and update similar language in the introduction. Looking at the lines mentioned, I'm replacing phrases like "produces no measurable benefit" and "adds no measurable benefit" with more statistically precise language like "does not yield statistically significant improvement." The key is softening the absolute claims while keeping the statistical evidence intact.

### 4. discussion.tex changes

#### 4a. L6 (managed by paper_switch.py block #10)

Current text appears to be cut off, but I'll need to apply the same pattern of replacing absolute statements about redundancy or lack of benefit with more measured language about statistical significance. I'm working through how to reframe this result more precisely. The user wants me to shift from saying the failure is architectural in absolute terms to saying the limitation is architectural specifically for this EE-only integration approach. So instead of claiming Level A signal masking isn't the constraint, I should acknowledge that the auxiliary SDF loss alone doesn't overcome the demonstration signal at the tested scales, and that's where the architectural limitation lies for this particular pathway.

Now I'm looking at the discussion section to find other absolute statements. The line about geometric supervision not accounting for the avoidance gains is pretty definitive, and it's controlled by a scenario-specific block that only applies to Scenario C. I should soften that language too, since it's making a strong claim without qualification. I need to update the discussion.tex file and make sure the corresponding code blocks match. For block #9, I'm changing the text to be softer, so I'll update both the tex file and the `old` string in the Scenario C replacement to stay in sync. For block #10, the user wants me to revise the language about the architectural limitation, so I need to update the tex file and the `old` string there as well, making sure the new phrasing better captures what the auxiliary loss can't overcome. I'm working through the systematic changes needed across the paper files. First, I'll update the non-managed files like introduction.tex, then carefully go through each managed block in paper_switch.py to ensure the old and new strings align with the revisions I'm making.

For the abstract.tex change, I need to be precise about which lambda values actually show statistical significance. The user's instruction specifies $p > 0.05$ for $\lambda \in \{0.01, 0.1\}$, so I'll follow that exactly rather than second-guessing based on the raw numbers. I'm second-guessing whether I should follow the instruction to restrict it to just those two lambda values, but the user was explicit about it. Looking at the data, lambda = 0.005 has a CAR essentially at the null mean, making it extremely non-significant—probably p > 0.5—so maybe the user wants to exclude it because it's not worth mentioning alongside the 0.05 threshold. I'll go with what they asked for.

Now I'm applying the specific edits they want: rewording the geometric supervision claim to say it "does not significantly improve" rather than "is fully redundant," and updating the SDF caption to use "statistically significant" language instead of "no measurable" while restricting the lambda range to exclude the 0.005 case.

For the larger change in claim3.tex, I'm revising the passage about collision-free demonstrations and SDF supervision to clarify that demonstrations alone drive the improvement, while SDF adds nothing meaningful—keeping the statistical details but tightening the language around what the data actually shows. 58.0\%, achieved at the 18K checkpoint after 13K steps of Phase~2 training with a single seed due to disk space limitations, which suggests that SDF gradients don't produce lasting behavioral effects. The task-specific avoidance ordering remains consistent regardless of the supervision weight, indicating that the model's avoidance patterns stem from the demonstration distribution itself rather than geometric guidance. I'm updating the text for Scenario B to clarify that collision-free demonstrations alone achieve substantial improvement in collision avoidance rate, while adding SDF supervision provides no additional benefit across the tested range, with a Phase 2 ablation confirming this finding. Writing LaTeX documentation... Writing the results text... Writing the revised text passage... I'm testing whether increasing the SDF loss weight by 20× actually helps—pushing λ to 0.1 gives CAR of 57.00% ± 2.18, which isn't statistically significant compared to the null distribution. This tells me SDF supervision doesn't produce meaningful benefits across the full range I tested, which points to a structural problem: the issue isn't that the training signal is too weak, but that I'm supervising the wrong collision surface entirely—end-effector monitoring can't compensate for missing full-body constraints. Writing the results text... I'm updating the text to reflect the statistical analysis more precisely—the key finding is that increasing the SDF loss weight by twentyfold doesn't yield significant improvements in collision avoidance across the tested range, which points to a fundamental structural mismatch rather than insufficient training signal strength. Updating the language around SDF redundancy throughout the document to be more precise. I'm changing "fully redundant" to "does not produce significant benefit" in Scenario C, and I need to apply the same correction to the figure caption on line 46 where it discusses the null band for tested lambda values. I'm updating the figure caption for Scenario B to use more precise language about the statistical findings, replacing the phrase about "full redundancy" with wording that better reflects the absence of statistically significant improvement across the tested loss-weight range.

Now I'm revising the discussion section to soften the absolute claim about geometric supervision, shifting from a definitive statement to one that acknowledges collision-free demonstrations account for nearly all the gains while EE-only SDF contributes no significant improvement. I'm realizing I need to be careful about the order of operations here. The current tex file contains the original text, and when I modify it, I also need to update the `old` string in block #9 to match what will actually be in the file. Since Scenario B doesn't touch this section, changing the tex file means the `old` string needs to reflect that new baseline state. Let me think through what the pre-switch state should be if I want to soften the language in the original tex file.

For the next change in block #10, I'm looking at the text about the CAR metric and the null distribution test.  The key shift is changing "confirming" to "suggesting" to soften the certainty, and updating "the failure is architectural" to "the limitation is architectural for this integration pathway" to be more precise about the scope. I need to update both the tex file and the old string in block #9 to match this new phrasing. I'm scanning discussion.tex for other instances of absolute language that need softening. I found that the paragraph explaining the null result uses definitive phrasing like "the failure is architectural" when describing why the SDF auxiliary loss doesn't help—I should revise this to be more measured, similar to how I've been adjusting the other claims throughout the document. I'm checking discussion.tex for absolute language outside the managed blocks. The subsection header "Demonstration data subsumes the SDF signal" uses pretty strong language—I could soften it to "largely subsumes," though since it's a heading I might leave it as is. The other instances I found like "primarily" are already qualified enough. Let me focus on the explicit changes requested and scan for any other obviously absolute phrasing that needs nuancing.

Looking back at the managed block about full-body SDF, "remains untested" is factual and not overly absolute, so that's fine as is. Now moving to introduction.tex, which isn't managed by the script. I need to change the statement about SDF supervision producing "no measurable benefit" to something more precise—"does not yield statistically significant improvement" is better, and I should also clarify the p-value conditions to be more accurate about which lambda values showed non-significance. I'm identifying places where the language is too absolute—"accounts for all observed avoidance" and "collision-free demonstrations account for all measured CAR gains" both need softening to something like "accounts for the majority" or "primarily accounts for." Now I need to implement all these changes across the files, and since there are quite a few edits, I should coordinate them carefully to keep paper_switch.py in sync with the tex files. I'm working through the paper_switch.py edits now, starting with the first block where I need to replace the text about SDF supervision benefits with language that's more precise about statistical significance. The old string spans multiple Python lines and I need to carefully match the exact text to change.

For Scenario C, I'm noticing the new text restructures the sentence differently than the old version, so I need to compare them carefully to understand what's actually changing and whether the language about "adds no significant benefit" needs adjustment for consistency across the different lambda ranges being tested. Updating the text strings to be more precise about statistical significance and the range of tested parameters. Updating the text strings in Scenario B to use softer language about the geometric supervision's effectiveness, replacing "fully redundant" and "confirming" with "does not significantly improve" and "suggesting" to better reflect the nuanced findings. Updating the caption text... I'm working through the changes needed for this large block of text. The old string needs several updates: changing the phrasing about SDF supervision benefits, updating the CAR percentage value, revising the note about the checkpoint and training constraints, and softening the language about SDF gradient effects. Let me construct the full revised old string with all these modifications applied. The ablation with SDF disabled after 5K steps confirms those gradients don't produce lasting effects on behavior. Across all conditions, the per-task performance ordering stays consistent—chocolate pudding performs best, bbq sauce worst—and remains unaffected by the supervision weight across a wide range, suggesting the avoidance patterns come from the demonstration data itself rather than the geometric constraints. Writing LaTeX strings... Writing LaTeX strings... Writing LaTeX strings... Writing LaTeX strings... I'm working through the ablation study results, comparing the effect of increasing the SDF weight parameter across a range of values. The key finding is that boosting lambda by twenty times doesn't yield statistically significant improvements—the performance stays within the null distribution, which suggests the geometric supervision isn't providing additional benefit beyond what the demonstrations already capture. Writing LaTeX string... I'm working through the text modifications for the paper, updating the language around SDF redundancy findings. For Scenario C, I'm changing "fully redundant" to "shows no significant benefit" to be more precise about the statistical interpretation. Similarly, for Scenario B, I'm replacing the claim about redundancy with language that emphasizes the lack of statistically significant improvement across the tested parameter range. Now I'm moving into the figure caption revisions. Updating the old string to reflect the softer language about EE-only SDF's contribution, changing from "no statistically significant improvement" to "at most a modest increment at high loss weights" to better match what the new scenario text already says.

Now looking at block #10 in the discussion section, I need to update the old string about the CAR baseline at high lambda values. The text currently states it remains within the null distribution with p=0.131, but the user's instruction appears to be shifting the framing from a definitive statement about architectural failure to something more tentative with "suggesting" instead of "confirming."

For the Scenario C branch, I'm replacing the language about SDF redundancy with a more nuanced characterization: at low lambda values SDF provides no meaningful benefit, but at lambda=0.1 a modest effect does emerge, though it doesn't fundamentally alter the underlying avoidance pattern—suggesting SDF can provide incremental augmentation rather than a strategic redirect.

For Scenario B, I'm updating the message to emphasize that even at substantially higher loss weights, CAR remains statistically indistinguishable from the null, which rules out signal masking as the limiting factor and points instead to an architectural constraint.

Updating string formatting... The s2 CAR value at 30K was 54.5% across the three seeds, so the 57.5 in the usage example doesn't match any of those results—it's just a placeholder value in the script documentation, so I'll leave it as is.

Now looking at the discussion.tex changes the user wants. The phrase "subsumes" in the italic heading is pretty absolute, so I should soften it to "largely subsumes" to match the request for more nuanced language throughout that section.

For the second point about EE monitoring, "cannot" is actually justified here since it's a structural limitation—EE-only monitoring literally can't detect full-body collisions by definition. That one stays as is.

The third claim about SDF refinement reducing CAR is getting cut off, but I need to evaluate whether "reduces" is appropriately qualified or if it needs softening too.

Actually, I should stick to what the user explicitly asked for. They want me to scan introduction.tex and discussion.tex for absolute language like "redundant" or "zero benefit," plus handle the specific changes they listed. I shouldn't be adding extra modifications beyond that scope. Let me refocus on just those targeted areas rather than continuing to second-guess every claim in the results section. I'm going through introduction.tex to identify and soften absolute claims about SDF supervision's lack of benefit. At line 20, I need to change "produces no measurable benefit" to something more nuanced like "does not yield statistically significant improvement," and similarly at line 27. I also notice there are other absolute statements like "the demonstration distribution accounts for all observed avoidance" and "collision-free demonstrations account for all measured CAR gains" that need to be reframed as well. These changes should be coordinated with the paper_switch.py configuration to ensure consistency across the document. Looking at the statistical results more carefully, SDF supervision doesn't provide meaningful improvements across the range I tested, with p-values consistently above 0.05, and the task-level avoidance patterns remain stable regardless of the supervision approach—suggesting the demonstrations themselves are what drive the observed behavior. I'm softening the language around demonstration data subsumption to "largely subsumes" rather than an absolute claim. Looking through the rest of discussion.tex, the other absolute language I flagged is already covered by my managed blocks, and the methodology critique about evaluation reliability is separate from the SDF discussion so it can stay as is. The key thing is that when I modify the tex file directly, it becomes the baseline state before any scenario-specific switches, which is the right approach here.

Now I'm scanning through all the tex files for instances of "no measurable" and "fully redundant" to make sure I've caught every place that needs softening. I've found and accounted for all the major instances across abstract, claim3, and introduction files—these are all covered by my existing managed blocks.

I also checked for related phrases like "zero benefit" and "completely" but didn't find any additional instances, and "subsumes" only appears in discussion.tex which I'm already handling. Now I'm ready to start applying the edits, grouping them by file type so I can work through the tex files in parallel, though I'll need to be careful with claim3.tex since some changes overlap within the same text blocks. a unique string to match). Let me start with the first change and work through them sequentially. what changes I'm making. Let me proceed with targeted replacements for each location—the main paragraph at line 26, the dose-response section at lines 31-32, and the figure caption at line 46.

For the tex files, I can handle all four in parallel since they don't depend on each other. Now I'll map out the exact Edit calls for each file, starting with claim3.tex and working through the others systematically. I'm working through a series of edits to make the language more precise about statistical significance—shifting from claims of "no benefit" or "redundancy" to more cautious phrasing like "no statistically significant benefit" or "consistent with the absence of improvement." The edits span the results section and abstract, adjusting both the main claims and figure captions to reflect the actual statistical findings. I'm working through edits to clarify the statistical findings—softening claims about geometric supervision being "fully redundant" to say it doesn't significantly improve performance, and changing "accounts for all" to "primarily accounts for" to be more precise about what the demonstration data explains. I'm checking the LaTeX escaping in the tex files—the curly braces in math mode need to be written as `\{` and `\}`, so when I update introduction.tex with the new text about lambda ranges, I need to make sure the syntax matches what's already in abstract.tex. Looking at the pattern of changes across these files, I'm tracking how the p-value qualifications are being updated. In introduction.tex, both L20 and L27 are being modified to specify that p > 0.05 applies only to λ ∈ {0.01, 0.1} rather than all tested values, matching the change already made in abstract.tex. Now I'm moving into the discussion.tex edits to see what's being revised there. I'm mapping out the edits needed for paper_switch.py, which involves modifying several blocks of text split across raw string literals—I need to update the old blocks and their corresponding scenario variants to reflect the statistical language changes and clarifications about the architectural limitations. I'm realizing that manually applying 19 edits sequentially would be inefficient—instead, I could read the entire file and rewrite just the `get_replacements` function with all the changes applied at once, which would be much faster than making individual edits across multiple turns. I need to search through the file more carefully to find the exact locations of these phrases. The strings are broken across multiple lines in the raw string literals, so I need to trace through the actual text to identify where "adds no measurable" and similar phrases appear in the Python source.

Rather than getting bogged down in line-by-line analysis, I'll take a more direct approach: rewrite the entire paper_switch.py file with all the necessary changes, then handle the tex file edits and run verification.

For the tex files, I notice the edits to claim3.tex are all in different locations with non-overlapping strings, so I can batch those changes together. But I need to be careful about whether parallel edits to the same file will work correctly—the Edit tool applies changes sequentially to the file state, so if the old_strings don't overlap and remain valid after each edit, they should work fine in parallel.

Actually, let me reconsider: the tool documentation says to make independent calls in parallel when there are no dependencies. Edits within the same file do have dependencies since each modifies the file content. To be safe, I'll apply edits to different files in parallel, but handle multiple edits to the same file sequentially to avoid any matching issues.

I'll start by making the first edit to each of the four tex files in parallel, then handle any remaining edits to those files, and finally rewrite paper_switch.py completely.

For claim3.tex, I need to check if I can batch all seven edits at once—the old strings don't overlap, so I should be able to apply them all together. Let me verify the strings are unique and then proceed with all edits to each file simultaneously. Wait, I need to be careful about parallel edits to the same file—there could be race conditions if multiple edits hit the same file simultaneously. Let me organize this differently: I'll batch the edits by file, doing one edit per file in parallel across all four tex files, then handle subsequent batches sequentially within each file to avoid conflicts.

Actually, since these are all short files, I could just rewrite them entirely with the Write tool—it's cleaner and I have all the content. For paper_switch.py though, that's 515 lines with many interleaved changes, so I'll use Edit for targeted modifications there instead.

Let me start by sending all the tex file edits in parallel, then tackle the Python file separately. file. Let me just execute them sequentially to be safe—I'll make the 16 edit calls one after another to avoid any potential issues with parallel edits to the same file. file, with cross-file parallelism.

Actually, let me take the simplest approach: just send all the edits in sequence. The files are small, the changes are clear. It'll be maybe 3-4 rounds.

Wait, actually I can be smarter. Let me combine multiple changes into one big Edit per file where possible. For example, for the claim3.tex L26 paragraph, I can replace the ENTIRE paragraph (4 changes in one edit).

For claim3.tex, I'm consolidating the paragraph edits into a single replacement that reframes the SDF supervision findings—changing "produces no measurable benefit" to "does not yield statistically significant improvement," updating the Phase 2 ablation result from 57.5% to 58.0%, clarifying the checkpoint details in the footnote, and shifting "confirming" to "suggesting" to reflect the more nuanced interpretation. I'm completing the L20 edit by specifying the exact lambda values and adjusting the language to emphasize statistical insignificance while noting that the demonstration distribution remains the primary driver of the observed avoidance patterns. Now I can tackle introduction.tex with just two edits total—one combined change at L20 and another at L27—both executable in parallel. Across all four files, I'm down to 11 total edits that can all run simultaneously.

I need to be careful about how I batch these though. Multiple Edit calls to the same file in one message might process sequentially with each seeing the previous result, or they could all see the original and conflict. To play it safe, I'll group edits by file and combine as many changes as possible into single Edit calls using larger old_string patterns that capture multiple modifications at once.

Looking at the breakdown: claim3.tex has 4 edits across different sections that don't overlap, abstract.tex has 2 edits, introduction.tex has 2 edits, and discussion.tex has 3 edits. Since each file's changes are non-overlapping, I can send all 11 edits in parallel across the four files. I've verified that all the old_string values are unique within their respective files—each edit targets distinct lines with non-overlapping content. Now I'm ready to send all 11 edits in a single batch and see if parallel same-file edits cause any issues. Let me construct each edit carefully with the exact text from the files. I'm refining the ablation study results—the Phase 2 experiment with SDF disabled after 5K steps shows a CAR of 58.0% at the 18K checkpoint, which still doesn't demonstrate a meaningful behavioral effect from the SDF gradients despite the extended training window.

For the redundancy claim, I'm tightening the language to focus on statistical significance rather than claiming full redundancy, since the results show no meaningful improvement across the tested lambda range. The figure caption needs compression too—essentially, all lambda values fall within the null band, confirming that EDF-only SDF supervision provides no statistically significant benefit across the 20x loss-weight range tested. I'm working through the specific text replacements the user wants. For the figure caption, I need to replace the phrase about "confirming full redundancy of EE-only SDF supervision" with language about the absence of statistically significant improvement—dropping the specific mention of EE-only supervision as requested. For the abstract changes, I'm updating the language around SDF supervision benefits to be more precise about statistical significance, and I need to handle the final sentence about geometric supervision being redundant. I'm working through the statistical evidence that collision avoidance comes entirely from the demonstration data itself. Across multiple ablation studies with varying SDF supervision weights, there's no significant improvement—the per-task rankings stay consistent regardless of the geometric supervision strength, confirming that the demonstrations are doing all the work here. fairly confident the old_strings are unique within their respective files. Before I apply all 11 edits, let me verify that the claim3.tex L26 old_string matches exactly what I pulled from the file—checking character by character against the actual content to make sure I'm targeting the right text.

Looking at line 26, my old_string spans from "Adding SDF supervision produces" through "lasting behavioral effect," which is indeed a substring of that line and should be unique. Good.

Now checking the discussion.tex L6 edits—I have two separate replacements in that line that don't overlap with each other, so they should apply cleanly without conflicts.

Firing all 11 edits now.

Actually, let me verify that the target substring for the discussion.tex L3 edit is unique in the file before committing. Checking line 3... yes, "and collision-free demonstrations, not geometric supervision, account for the measured avoidance gains" appears exactly once. Good.

Now I need to make sure this edit doesn't inadvertently break the surrounding text or create any parsing issues.

Looking at the proposed change, I'm replacing that phrase with a more specific claim about the statistical significance of EE-only SDF contributions. The sentence structure flows naturally with the semicolon and parallel construction, so this should work fine.

Alright, I'm ready to push all 11 edits at once.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "e6d63500-d81b-485c-b37e-7165d7554da9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

I'll make all tex file edits in parallel (11 targeted edits across 4 files), then rewrite `paper_switch.py`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "63a2f863-c00b-476b-b948-85a5b0ccc3ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Rzn9KJmRqiRNmA6zLtGNEH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "SDF adds no measurable CAR beyond LoRA-only across the full tested range",
  "new_string": "SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "51096514-d4ec-4298-8564-2186214fa7b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

_source line 18 · 2026-05-28T06:03:06.850Z_

<details><summary>↩ Tool result · `toolu_01Rzn9KJmRqiRNmA6zLtGNEH`</summary>

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "f4372438-e728-4be7-bbef-429d77cf1420",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "oldString": "SDF adds no measurable CAR beyond LoRA-only across the full tested range",
    "newString": "SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale",
    "originalFile": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across the full tested range $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 3 & 51.5\\,$\\pm$\\,0.0 & 54.67\\,$\\pm$\\,2.02 & 0.391 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$ & 3 & 50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$18--20\\,pp (71.5\\% $\\to$ 51.5--54.0\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.\n\n\\paragraph{Robustness to null construction.}\nThe preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.\n\n\\paragraph{Statistical power.}\nWith $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.\n\n\\paragraph{Evaluation-seed consistency.}\nUnder matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within the null band ($p > 0.05$), confirming full redundancy of EE-only SDF supervision across a 20$\\times$ loss-weight range.}\n\\label{fig:lambda_car}\n\\end{figure}",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 7,
        "newStart": 4,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across the full tested range $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}",
          "+\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}",
          " \\label{tab:avoidance_source}",
          " \\vspace{2pt}",
          " \\small"
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

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_01MBWxjjCAGtsHKzPReicfe6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect.",
  "new_string": "Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints.}, suggesting that SDF gradients do not produce a lasting behavioral effect."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "0e68127b-c0b6-4a3b-94db-65f2a53d7f24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

_source line 20 · 2026-05-28T06:03:09.679Z_

<details><summary>↩ Tool result · `toolu_01MBWxjjCAGtsHKzPReicfe6`</summary>

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "6bf58b7e-a98b-4e1c-a0a0-f84bf9bd9dfe",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "oldString": "Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect.",
    "newString": "Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints.}, suggesting that SDF gradients do not produce a lasting behavioral effect.",
    "originalFile": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 3 & 51.5\\,$\\pm$\\,0.0 & 54.67\\,$\\pm$\\,2.02 & 0.391 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$ & 3 & 50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$18--20\\,pp (71.5\\% $\\to$ 51.5--54.0\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.\n\n\\paragraph{Robustness to null construction.}\nThe preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.\n\n\\paragraph{Statistical power.}\nWith $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.\n\n\\paragraph{Evaluation-seed consistency.}\nUnder matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within the null band ($p > 0.05$), confirming full redundancy of EE-only SDF supervision across a 20$\\times$ loss-weight range.}\n\\label{fig:lambda_car}\n\\end{figure}",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 7,
        "newStart": 23,
        "newLines": 7,
        "lines": [
          " \\vspace{1pt}",
          " \\end{table}",
          " ",
          "-Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision produces no measurable benefit across the full tested range: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints precluded additional seeds for this ablation.}, confirming that SDF gradients produce no lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.",
          "+Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints.}, suggesting that SDF gradients do not produce a lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.",
          " ",
          " \\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}",
          " Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp (71.5\\% $\\to$ 51.5--54.0\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning."
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01D5f8tyKDAfFSv9MHBctMfH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$",
  "new_string": "SDF supervision does not produce statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "83920aff-b45c-47ab-b75a-db4b0b318a94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

_source line 22 · 2026-05-28T06:03:11.095Z_

<details><summary>↩ Tool result · `toolu_01D5f8tyKDAfFSv9MHBctMfH`</summary>

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "5694f0f4-0e8f-4683-bfa4-3fd2f65c66a4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "oldString": "SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$",
    "newString": "SDF supervision does not produce statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$",
    "originalFile": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 3 & 51.5\\,$\\pm$\\,0.0 & 54.67\\,$\\pm$\\,2.02 & 0.391 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$ & 3 & 50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints.}, suggesting that SDF gradients do not produce a lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$18--20\\,pp (71.5\\% $\\to$ 51.5--54.0\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.\n\n\\paragraph{Robustness to null construction.}\nThe preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.\n\n\\paragraph{Statistical power.}\nWith $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.\n\n\\paragraph{Evaluation-seed consistency.}\nUnder matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within the null band ($p > 0.05$), confirming full redundancy of EE-only SDF supervision across a 20$\\times$ loss-weight range.}\n\\label{fig:lambda_car}\n\\end{figure}",
    "structuredPatch": [
      {
        "oldStart": 29,
        "oldLines": 7,
        "newStart": 29,
        "newLines": 7,
        "lines": [
          " Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp (71.5\\% $\\to$ 51.5--54.0\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.",
          " ",
          " \\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}",
          "-Increasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision is redundant with the demonstration signal across the full tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.",
          "+Increasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision does not produce statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.",
          " ",
          " \\paragraph{Robustness to null construction.}",
          " The preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$."
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

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_018yn2iZ1qW17XjPndUNZAFw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
  "old_string": "confirming full redundancy of EE-only SDF supervision across a 20$\\times$ loss-weight range",
  "new_string": "consistent with the absence of statistically significant improvement across a 20$\\times$ loss-weight range"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "57b0c218-89d9-4537-8bc6-a170a76e26ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

_source line 24 · 2026-05-28T06:03:12.500Z_

<details><summary>↩ Tool result · `toolu_018yn2iZ1qW17XjPndUNZAFw`</summary>

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "ab55b6ef-9eb1-4d55-a6dd-40a1db05bfe2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
    "oldString": "confirming full redundancy of EE-only SDF supervision across a 20$\\times$ loss-weight range",
    "newString": "consistent with the absence of statistically significant improvement across a 20$\\times$ loss-weight range",
    "originalFile": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 3 & 51.5\\,$\\pm$\\,0.0 & 54.67\\,$\\pm$\\,2.02 & 0.391 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$ & 3 & 50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints.}, suggesting that SDF gradients do not produce a lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$18--20\\,pp (71.5\\% $\\to$ 51.5--54.0\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision does not produce statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.\n\n\\paragraph{Robustness to null construction.}\nThe preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.\n\n\\paragraph{Statistical power.}\nWith $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.\n\n\\paragraph{Evaluation-seed consistency.}\nUnder matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within the null band ($p > 0.05$), confirming full redundancy of EE-only SDF supervision across a 20$\\times$ loss-weight range.}\n\\label{fig:lambda_car}\n\\end{figure}",
    "structuredPatch": [
      {
        "oldStart": 43,
        "oldLines": 6,
        "newStart": 43,
        "newLines": 6,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}",
          "-\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within the null band ($p > 0.05$), confirming full redundancy of EE-only SDF supervision across a 20$\\times$ loss-weight range.}",
          "+\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within the null band ($p > 0.05$), consistent with the absence of statistically significant improvement across a 20$\\times$ loss-weight range.}",
          " \\label{fig:lambda_car}",
          " \\end{figure}",
          "\\ No newline at end of file"
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

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_0144XPiMxRJHm57z2g5wULTn`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
  "old_string": "SDF supervision adds no measurable benefit across the full tested range $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for all;",
  "new_string": "SDF supervision shows no statistically significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "2c1a8a7a-0739-4ad1-965c-4636f9d177a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

_source line 26 · 2026-05-28T06:03:13.912Z_

<details><summary>↩ Tool result · `toolu_0144XPiMxRJHm57z2g5wULTn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "98b25141-4966-43af-a968-acf7d9fc53aa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
    "oldString": "SDF supervision adds no measurable benefit across the full tested range $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for all;",
    "newString": "SDF supervision shows no statistically significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$;",
    "originalFile": "\\begin{abstract}\nVision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.\nOn SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\\% CAR while 99.6\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\,mm. The robot is frozen, not safe.\nWe introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\\,mm threshold range.\nWe further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\\sim}$26 percentage points). SDF supervision adds no measurable benefit across the full tested range $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for all; $\\lambda = 0.1$: 57.00\\%$\\,\\pm\\,$2.18, 3 seeds).\nDisplacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision is fully redundant across a 20$\\times$ loss-weight range, confirming that collision avoidance arises from demonstration data, not geometric supervision.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 6,
        "newStart": 2,
        "newLines": 6,
        "lines": [
          " Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.",
          " On SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\\% CAR while 99.6\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\,mm. The robot is frozen, not safe.",
          " We introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\\,mm threshold range.",
          "-We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\\sim}$26 percentage points). SDF supervision adds no measurable benefit across the full tested range $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for all; $\\lambda = 0.1$: 57.00\\%$\\,\\pm\\,$2.18, 3 seeds).",
          "+We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\\sim}$26 percentage points). SDF supervision shows no statistically significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: 57.00\\%$\\,\\pm\\,$2.18, 3 seeds).",
          " Displacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision is fully redundant across a 20$\\times$ loss-weight range, confirming that collision avoidance arises from demonstration data, not geometric supervision.",
          " \\end{abstract}"
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

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_01U4irmkJskmjq2jmQhDzqMy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
  "old_string": "EE-only geometric supervision is fully redundant across a 20$\\times$ loss-weight range, confirming that collision avoidance arises from demonstration data, not geometric supervision.",
  "new_string": "EE-only geometric supervision does not significantly improve collision avoidance across a 20$\\times$ loss-weight range, suggesting that collision avoidance primarily arises from demonstration data rather than geometric supervision."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "80fc983a-1f93-488f-af91-e726e882e12d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

_source line 28 · 2026-05-28T06:03:15.397Z_

<details><summary>↩ Tool result · `toolu_01U4irmkJskmjq2jmQhDzqMy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "7e7d5c0e-eec1-478e-b7a3-dff12d6d9027",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
    "oldString": "EE-only geometric supervision is fully redundant across a 20$\\times$ loss-weight range, confirming that collision avoidance arises from demonstration data, not geometric supervision.",
    "newString": "EE-only geometric supervision does not significantly improve collision avoidance across a 20$\\times$ loss-weight range, suggesting that collision avoidance primarily arises from demonstration data rather than geometric supervision.",
    "originalFile": "\\begin{abstract}\nVision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.\nOn SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\\% CAR while 99.6\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\,mm. The robot is frozen, not safe.\nWe introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\\,mm threshold range.\nWe further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\\sim}$26 percentage points). SDF supervision shows no statistically significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: 57.00\\%$\\,\\pm\\,$2.18, 3 seeds).\nDisplacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision is fully redundant across a 20$\\times$ loss-weight range, confirming that collision avoidance arises from demonstration data, not geometric supervision.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 5,
        "newStart": 3,
        "newLines": 5,
        "lines": [
          " On SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\\% CAR while 99.6\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\,mm. The robot is frozen, not safe.",
          " We introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\\,mm threshold range.",
          " We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\\sim}$26 percentage points). SDF supervision shows no statistically significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: 57.00\\%$\\,\\pm\\,$2.18, 3 seeds).",
          "-Displacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision is fully redundant across a 20$\\times$ loss-weight range, confirming that collision avoidance arises from demonstration data, not geometric supervision.",
          "+Displacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision does not significantly improve collision avoidance across a 20$\\times$ loss-weight range, suggesting that collision avoidance primarily arises from demonstration data rather than geometric supervision.",
          " \\end{abstract}"
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_01LgvEmu59iTC2PqsHPRUkUN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "Adding SDF supervision produces no measurable benefit across the full tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for all; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution accounts for all observed avoidance",
  "new_string": "Adding SDF supervision does not yield statistically significant improvement across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution primarily accounts for observed avoidance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "9fc1f8bb-b4e6-4c74-840b-293241492d26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

_source line 30 · 2026-05-28T06:03:17.679Z_

<details><summary>↩ Tool result · `toolu_01LgvEmu59iTC2PqsHPRUkUN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "efb3f7ab-0878-45d2-947e-72de34c25f1a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "oldString": "Adding SDF supervision produces no measurable benefit across the full tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for all; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution accounts for all observed avoidance",
    "newString": "Adding SDF supervision does not yield statistically significant improvement across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution primarily accounts for observed avoidance",
    "originalFile": "\\section{Introduction}\\label{sec:intro}\n\nCollision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}. Our SDF-augmented Pi0~\\cite{black2024pi0} reaches 91.5\\% CAR across 800 episodes. The problem appears close to solved.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig1_teaser}\n\\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\\tau_d$; Pi0+A1's 91.5\\% safety score drops to ${\\approx}$\\,0\\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\\,mm in all safe episodes, and dfCAR equals raw CAR (right).}\n\\label{fig:teaser}\n\\end{figure}\n\nIt is not (Figure~\\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\\% exhibit displacement below 0.1\\,mm; TSR is 0\\% across all 800 episodes. The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\\ref{sec:fake_safety}). We term this \\emph{fake safety}: \\emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\\cite{karwowski2024goodhart}.\n\nWe present a systematic investigation of this problem across the Pi0 and Pi0.5~\\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.\n\n\\textbf{Fake safety is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\\tau_d$. dfCAR collapses Pi0+A1 from 91.5\\% to ${\\approx}$\\,0\\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\\,=\\,71.5\\%, CAR\\,=\\,28.5\\%, with every safe episode above 288\\,mm displacement and dfCAR equal to raw CAR (Section~\\ref{sec:fake_safety}).\n\n\\textbf{EE-only SDF refinement is structurally counterproductive.} Three ground-truth oracle variants all achieve \\emph{lower} CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n\n\\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\\sim}$26 points with zero frozen episodes. Adding SDF supervision produces no measurable benefit across the full tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for all; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution accounts for all observed avoidance (Section~\\ref{sec:avoidance_source}).\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{dfCAR metric:} displacement-filtered CAR that separates genuine avoidance from action collapse, robust across $\\tau_d \\in [2, 200]$\\,mm.\n    \\item \\textbf{Fake safety diagnosis:} 100+ experiments across Pi0/Pi0.5 showing $>$99\\% of Pi0 safe episodes are action-collapse artifacts.\n    \\item \\textbf{EE-only SDF is counterproductive:} ground-truth oracle refinement \\emph{reduces} CAR below unrefined baselines by redistributing collisions to unmonitored arm links.\n    \\item \\textbf{Demonstration sufficiency:} collision-free demonstrations account for all measured CAR gains (${\\sim}$26\\,pp); SDF supervision adds no measurable benefit across the full tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for all, 3 seeds).\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 17,
        "oldLines": 7,
        "newStart": 17,
        "newLines": 7,
        "lines": [
          " ",
          " \\textbf{EE-only SDF refinement is structurally counterproductive.} Three ground-truth oracle variants all achieve \\emph{lower} CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\\ref{sec:ee_only}).",
          " ",
          "-\\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\\sim}$26 points with zero frozen episodes. Adding SDF supervision produces no measurable benefit across the full tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for all; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution accounts for all observed avoidance (Section~\\ref{sec:avoidance_source}).",
          "+\\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\\sim}$26 points with zero frozen episodes. Adding SDF supervision does not yield statistically significant improvement across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution primarily accounts for observed avoidance (Section~\\ref{sec:avoidance_source}).",
          " ",
          " Our contributions are:",
          " \\begin{itemize}"
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01BduD2ziqwsGiZXQLgo1YrP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
  "old_string": "collision-free demonstrations account for all measured CAR gains (${\\sim}$26\\,pp); SDF supervision adds no measurable benefit across the full tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for all, 3 seeds).",
  "new_string": "collision-free demonstrations account for nearly all measured CAR gains (${\\sim}$26\\,pp); SDF supervision shows no statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$, 3 seeds)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "f20b3646-29e6-40be-911b-af3f7a249ce4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

_source line 32 · 2026-05-28T06:03:19.580Z_

<details><summary>↩ Tool result · `toolu_01BduD2ziqwsGiZXQLgo1YrP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "2cfaddb4-b83a-43e9-87d4-16e1f696033e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
    "oldString": "collision-free demonstrations account for all measured CAR gains (${\\sim}$26\\,pp); SDF supervision adds no measurable benefit across the full tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for all, 3 seeds).",
    "newString": "collision-free demonstrations account for nearly all measured CAR gains (${\\sim}$26\\,pp); SDF supervision shows no statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$, 3 seeds).",
    "originalFile": "\\section{Introduction}\\label{sec:intro}\n\nCollision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}. Our SDF-augmented Pi0~\\cite{black2024pi0} reaches 91.5\\% CAR across 800 episodes. The problem appears close to solved.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig1_teaser}\n\\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\\tau_d$; Pi0+A1's 91.5\\% safety score drops to ${\\approx}$\\,0\\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\\,mm in all safe episodes, and dfCAR equals raw CAR (right).}\n\\label{fig:teaser}\n\\end{figure}\n\nIt is not (Figure~\\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\\% exhibit displacement below 0.1\\,mm; TSR is 0\\% across all 800 episodes. The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\\ref{sec:fake_safety}). We term this \\emph{fake safety}: \\emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\\cite{karwowski2024goodhart}.\n\nWe present a systematic investigation of this problem across the Pi0 and Pi0.5~\\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.\n\n\\textbf{Fake safety is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\\tau_d$. dfCAR collapses Pi0+A1 from 91.5\\% to ${\\approx}$\\,0\\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\\,=\\,71.5\\%, CAR\\,=\\,28.5\\%, with every safe episode above 288\\,mm displacement and dfCAR equal to raw CAR (Section~\\ref{sec:fake_safety}).\n\n\\textbf{EE-only SDF refinement is structurally counterproductive.} Three ground-truth oracle variants all achieve \\emph{lower} CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n\n\\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\\sim}$26 points with zero frozen episodes. Adding SDF supervision does not yield statistically significant improvement across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution primarily accounts for observed avoidance (Section~\\ref{sec:avoidance_source}).\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{dfCAR metric:} displacement-filtered CAR that separates genuine avoidance from action collapse, robust across $\\tau_d \\in [2, 200]$\\,mm.\n    \\item \\textbf{Fake safety diagnosis:} 100+ experiments across Pi0/Pi0.5 showing $>$99\\% of Pi0 safe episodes are action-collapse artifacts.\n    \\item \\textbf{EE-only SDF is counterproductive:} ground-truth oracle refinement \\emph{reduces} CAR below unrefined baselines by redistributing collisions to unmonitored arm links.\n    \\item \\textbf{Demonstration sufficiency:} collision-free demonstrations account for all measured CAR gains (${\\sim}$26\\,pp); SDF supervision adds no measurable benefit across the full tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for all, 3 seeds).\n\\end{itemize}",
    "structuredPatch": [
      {
        "oldStart": 24,
        "oldLines": 5,
        "newStart": 24,
        "newLines": 5,
        "lines": [
          "     \\item \\textbf{dfCAR metric:} displacement-filtered CAR that separates genuine avoidance from action collapse, robust across $\\tau_d \\in [2, 200]$\\,mm.",
          "     \\item \\textbf{Fake safety diagnosis:} 100+ experiments across Pi0/Pi0.5 showing $>$99\\% of Pi0 safe episodes are action-collapse artifacts.",
          "     \\item \\textbf{EE-only SDF is counterproductive:} ground-truth oracle refinement \\emph{reduces} CAR below unrefined baselines by redistributing collisions to unmonitored arm links.",
          "-    \\item \\textbf{Demonstration sufficiency:} collision-free demonstrations account for all measured CAR gains (${\\sim}$26\\,pp); SDF supervision adds no measurable benefit across the full tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for all, 3 seeds).",
          "+    \\item \\textbf{Demonstration sufficiency:} collision-free demonstrations account for nearly all measured CAR gains (${\\sim}$26\\,pp); SDF supervision shows no statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$, 3 seeds).",
          " \\end{itemize}",
          "\\ No newline at end of file"
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

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01LmLBJX397E14NKxLMHYqJB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "and collision-free demonstrations, not geometric supervision, account for the measured avoidance gains (\\S\\ref{sec:avoidance_source}).",
  "new_string": "and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "f89b8566-d1e8-4f84-b3aa-2fbfe9c6d597",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

_source line 34 · 2026-05-28T06:03:21.003Z_

<details><summary>↩ Tool result · `toolu_01LmLBJX397E14NKxLMHYqJB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "40d33f04-6051-4b71-9b0a-bc43d6ab70b0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "and collision-free demonstrations, not geometric supervision, account for the measured avoidance gains (\\S\\ref{sec:avoidance_source}).",
    "newString": "and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations, not geometric supervision, account for the measured avoidance gains (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), confirming that Level~A signal masking is not the binding constraint---the failure is architectural. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \\section{Discussion and Conclusion}\\label{sec:conclusion}",
          " ",
          "-Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations, not geometric supervision, account for the measured avoidance gains (\\S\\ref{sec:avoidance_source}).",
          "+Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).",
          " ",
          " \\paragraph{Why EE-only SDF fails.}",
          " Two independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), confirming that Level~A signal masking is not the binding constraint---the failure is architectural. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations."
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

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_01AhqYgNcojdYd9yqbEKxkh6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "confirming that Level~A signal masking is not the binding constraint---the failure is architectural.",
  "new_string": "suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "0b9c9d09-15c5-4180-829b-0d8a55788057",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

_source line 36 · 2026-05-28T06:03:21.819Z_

<details><summary>↩ Tool result · `toolu_01AhqYgNcojdYd9yqbEKxkh6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "e1fafe5d-95d2-4864-86b7-6f62ccfcd013",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "confirming that Level~A signal masking is not the binding constraint---the failure is architectural.",
    "newString": "suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway.",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), confirming that Level~A signal masking is not the binding constraint---the failure is architectural. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).",
          " ",
          " \\paragraph{Why EE-only SDF fails.}",
          "-Two independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), confirming that Level~A signal masking is not the binding constraint---the failure is architectural. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.",
          "+Two independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.",
          " ",
          " \\paragraph{Implications for evaluation.}",
          " dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot."
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

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_01WpFjFhvg4S7V7tBsU1abRL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "Demonstration data subsumes the SDF signal",
  "new_string": "Demonstration data largely subsumes the SDF signal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "a9076be7-7926-445e-9c9b-20ab816c6812",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAZwP6Vhh79hp25LDjZATL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14416,
      "cache_read_input_tokens": 24694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14416
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

_source line 38 · 2026-05-28T06:03:22.544Z_

<details><summary>↩ Tool result · `toolu_01WpFjFhvg4S7V7tBsU1abRL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "33c4964e-f4a5-4b03-8dc6-dc3465d00508",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "Demonstration data subsumes the SDF signal",
    "newString": "Demonstration data largely subsumes the SDF signal",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).",
          " ",
          " \\paragraph{Why EE-only SDF fails.}",
          "-Two independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.",
          "+Two independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.",
          " ",
          " \\paragraph{Implications for evaluation.}",
          " dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot."
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

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
All 11 tex file edits succeeded. Now I need to rewrite `paper_switch.py` with all the corresponding changes to old strings, Scenario B new strings, and Scenario C new strings.

Let me construct the complete new paper_switch.py. I'll go through each block and make the changes I planned.

Let me write the complete file now. I'll be very careful to match the new tex content.

Actually, looking at this more carefully, the paper_switch.py file is 515 lines. Let me construct it carefully. I'll keep everything the same except the `get_replacements` function (lines 68-367).
 
I realize there's a more efficient approach here—I can make targeted edits on paper_switch.py for each change rather than rewriting the entire file. There are roughly 19 changes needed, and many of them are unique strings that I can edit in parallel. Let me identify the exact edits needed and work through them systematically.

The first block involves updating text about SDF supervision benefits, changing the phrasing from "adds no measurable benefit" to "shows no statistically significant benefit" and restructuring how the lambda range and p-values are presented across the string literals.

For the second block, I'm making a similar edit to clarify the statistical language—replacing "adds no" with "shows no statistically" to be more precise about what the results indicate at different lambda thresholds.

Given the complexity of these multi-line string edits in Python, I think the safest approach is to rewrite the entire file rather than trying to make targeted edits across the raw string literals. The function spans 300 lines with about 19 changes needed, so I'll reconstruct the full content carefully to ensure all modifications are applied correctly.

Let me work through this section by section, starting with the unchanged imports and constants, then the heavily modified `get_replacements` function, and finally the main function at the end. Writing the permutation test logic... Writing replacement logic... Updating the abstract text with more precise statistical language... Writing string replacements... I'm continuing to define the replacement text for the claim3.tex file, handling both the conditional case where we simplify the language about the loss weight range, and the else case where we keep the original phrasing about the 20× range. Then I'm appending this replacement rule to the list of changes.

Now I'm moving to the next modification for the table caption in claim3.tex, which involves updating how we describe the statistical significance of the SDF results compared to LoRA-only. Writing caption text... Finishing the caption text for Scenario C with the statistical significance details and effect size comparisons, then moving on to update the table row in claim3.tex. Writing LaTeX table content... Writing LaTeX text... The task results show that per-task performance ordering stays consistent across all conditions regardless of the lambda weight, suggesting the avoidance patterns come from the demonstration data itself rather than the geometric constraints. Now I'm examining the dose-response effects at higher loss weights... Writing LaTeX strings... Writing LaTeX strings... Writing figure caption... Writing caption updates... Writing discussion text replacements... Writing verification logic... I'm verifying that the edited text in discussion.tex matches what I expect—the full sentence about the lambda parameter and architectural limitations is there. Now I need to check the corresponding changes in claim3.tex to make sure the edits align across both files. Updating the paper_switch.py configuration...

Checking block #6 against the tex file — the collision-free demonstrations section matches, confirming the avoidance results and SDF supervision findings are consistent.

Block #7 looks good too — the dose-response paragraph about non-significant benefits across the lambda range aligns with what's in the tex file.

Now verifying block #8 for the figure caption about the 20x loss-weight range... I'm comparing the abstract text across the tex file and the old paper_switch.py to verify the changes are consistent. The first block matches up correctly with the collision-free demonstrations sentence flowing into the SDF supervision results. For the second block, I need to check if the geometric supervision statement in the tex file aligns with what was previously in paper_switch.py, which appears to discuss displacement filtering and EE-only supervision across a loss-weight range. Checking the caption text for block #4 against the source file — the LaTeX caption describing the SafeLIBERO avoidance attribution experiment matches up, confirming that SDF shows no statistically significant improvement over LoRA-only across the tested lambda range, with all models achieving zero frozen rate and displacement above the threshold.

Now I'm ready to write out the complete paper_switch.py file, being careful to preserve all the verified strings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "a10e7241-eeea-4b94-8505-e8ec87129993",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014FYmUDS6XkFiQBoiNh8M68",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 66308,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 66308
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

_source line 40_

All 11 tex edits succeeded. Now rewriting `paper_switch.py` to sync all old/new strings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "f35b40dd-df9e-4b57-8b85-ed8fc46bc94c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014FYmUDS6XkFiQBoiNh8M68",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 66308,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 66308
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

_source line 41_

<details open><summary>🔧 Tool call — Write · `toolu_01NobPtAYmWopf5G8Y3JYhqD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_switch.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Auto-switch paper text based on λ=0.1 s2 30K eval result.\n\nUsage:\n  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0 --dry-run\n  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0\n\"\"\"\nimport argparse\nimport subprocess\nimport sys\nfrom itertools import combinations\nfrom math import comb, sqrt\nfrom pathlib import Path\n\nNULL_VALUES = [56.5, 52.5, 55, 57, 54, 52.5]\nNULL_MEAN = sum(NULL_VALUES) / len(NULL_VALUES)\nNULL_STD = (sum((x - NULL_MEAN) ** 2 for x in NULL_VALUES) / 5) ** 0.5\n\nS0_CAR, S1_CAR = 58.0, 58.5\nS0_TSR, S1_TSR = 47.0, 49.0\n\nPAPER_DIR = Path(__file__).resolve().parent.parent / \"docs\" / \"paper\"\n\n\ndef mean(v):\n    return sum(v) / len(v)\n\n\ndef std_b(v):\n    m = mean(v)\n    return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5\n\n\ndef perm_test(null_vals, treat_vals):\n    pool = null_vals + treat_vals\n    k = len(treat_vals)\n    obs = mean(treat_vals)\n    mu = mean(pool)\n    dev = abs(obs - mu)\n    n = comb(len(pool), k)\n    ge = tw = 0\n    for c in combinations(pool, k):\n        m = mean(c)\n        if m >= obs:\n            ge += 1\n        if abs(m - mu) >= dev - 1e-12:\n            tw += 1\n    return ge / n, tw / n, n\n\n\ndef fill(tpl, vals):\n    for k, v in vals.items():\n        tpl = tpl.replace(\"{\" + k + \"}\", str(v))\n    return tpl\n\n\ndef safe_replace(content, old, new, label):\n    n = content.count(old)\n    if n == 0:\n        print(f\"  !! [{label}] NOT FOUND\")\n        return content, False\n    if n > 1:\n        print(f\"  !! [{label}] found {n}x\")\n        return content, False\n    return content.replace(old, new), True\n\n\ndef get_replacements(scenario, v):\n    R = []\n    is_c = scenario == \"C\"\n\n    # 1. abstract.tex L5 (training results)\n    old = (\n        r\"collision-free demonstrations alone account for all measured avoidance \"\n        r\"gains (${\\sim}$26 percentage points). SDF supervision shows no statistically \"\n        r\"significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"\n        r\"($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: \"\n        r\"57.00\\%$\\,\\pm\\,$2.18, 3 seeds).\"\n    )\n    if is_c:\n        new = fill(\n            r\"collision-free demonstrations alone account for nearly all measured \"\n            r\"avoidance gains (${\\sim}$26 percentage points). SDF supervision shows no \"\n            r\"statistically significant benefit at $\\lambda \\leq 0.01$ ($p > 0.1$); at \"\n            r\"$\\lambda = 0.1$, a modest but statistically significant increase emerges \"\n            r\"({mean_car}\\%$\\,\\pm\\,${std_car}, permutation $p = {p_value}$, 3 seeds), \"\n            r\"though the effect size ({delta_pp}\\,pp) is small relative to the \"\n            r\"$+$26\\,pp gain from fine-tuning alone.\", v)\n    else:\n        new = fill(\n            r\"collision-free demonstrations alone account for all measured avoidance \"\n            r\"gains (${\\sim}$26 percentage points). SDF supervision shows no statistically \"\n            r\"significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"\n            r\"($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: \"\n            r\"{mean_car}\\%$\\,\\pm\\,${std_car}, 3 seeds).\", v)\n    R.append((\"abstract.tex\", \"abstract L5 training\", old, new))\n\n    # 2. abstract.tex L6 (concluding sentence)\n    old = (\n        r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n        r\"EE-only geometric supervision does not significantly improve collision \"\n        r\"avoidance across a 20$\\times$ loss-weight range, suggesting that collision \"\n        r\"avoidance primarily arises from demonstration data rather than geometric \"\n        r\"supervision.\"\n    )\n    if is_c:\n        new = (\n            r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n            r\"Even at the highest tested loss weight, the modest SDF effect is dwarfed by \"\n            r\"demonstration-driven avoidance and cannot overcome the structural limitation \"\n            r\"of EE-only supervision.\"\n        )\n    else:\n        new = (\n            r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n            r\"EE-only geometric supervision does not significantly improve collision \"\n            r\"avoidance across a 20$\\times$ loss-weight range, suggesting that collision \"\n            r\"avoidance primarily arises from demonstration data rather than geometric \"\n            r\"supervision.\"\n        )\n    R.append((\"abstract.tex\", \"abstract L6 conclusion\", old, new))\n\n    # 3. claim3.tex L3 scope sentence\n    old = (\n        r\"We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of \"\n        r\"loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all \"\n        r\"evaluated at the 30K-step checkpoint.\"\n    )\n    if is_c:\n        new = (\n            r\"We compare LoRA-only against LoRA+SDF at three loss weights \"\n            r\"($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at \"\n            r\"the 30K-step checkpoint.\"\n        )\n    else:\n        new = (\n            r\"We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of \"\n            r\"loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all \"\n            r\"evaluated at the 30K-step checkpoint.\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L3 scope\", old, new))\n\n    # 4. claim3.tex L7 table caption\n    old = (\n        r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no \"\n        r\"statistically significant CAR improvement beyond LoRA-only at the tested \"\n        r\"scale $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"\n        r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\"\n    )\n    if is_c:\n        new = fill(\n            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF at \"\n            r\"$\\lambda \\leq 0.01$ shows no statistically significant CAR improvement \"\n            r\"beyond LoRA-only ($p > 0.1$). At $\\lambda = 0.1$, a modest increase \"\n            r\"reaches statistical significance ($z = {z_value}$, permutation \"\n            r\"$p = {p_value}$, $n{=}3$), though the effect size ({delta_pp}\\,pp) \"\n            r\"is small relative to the $+$26\\,pp LoRA gain. All fine-tuned models \"\n            r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\", v)\n    else:\n        new = (\n            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no \"\n            r\"statistically significant CAR improvement beyond LoRA-only at the tested \"\n            r\"scale $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"\n            r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L7 caption\", old, new))\n\n    # 5. claim3.tex L20 table row\n    old = (\n        r\"LoRA+SDF $\\lambda{=}0.1$ & 3 & \"\n        r\"50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\"\n    )\n    new = fill(\n        r\"LoRA+SDF $\\lambda{=}0.1$ & 3 & \"\n        r\"{tsr_mean}\\,$\\pm$\\,{tsr_std} & {mean_car}\\,$\\pm$\\,{std_car} & 0.394 \\\\\", v)\n    R.append((\"claim3.tex\", \"claim3 L20 table row\", old, new))\n\n    # 6. claim3.tex L27 body paragraph\n    old = (\n        r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n        r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n        r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n        r\"avoidance. Adding SDF supervision does not yield statistically significant \"\n        r\"improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically \"\n        r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"\n        r\"(57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). \"\n        r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"\n        r\"CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 \"\n        r\"training, single seed s2); full 30K training did not complete due to disk \"\n        r\"constraints.}, suggesting that SDF gradients do not produce a lasting \"\n        r\"behavioral effect. The per-task CAR ordering \"\n        r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"\n        r\"lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating \"\n        r\"that avoidance patterns reflect the demonstration distribution rather than \"\n        r\"geometric supervision.\"\n    )\n    if is_c:\n        new = (\n            r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n            r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n            r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n            r\"avoidance. At $\\lambda \\leq 0.01$, SDF supervision does not yield \"\n            r\"statistically significant improvement: LoRA-only CAR (54.67\\%) is within \"\n            r\"0.17\\,pp of $\\lambda = 0.005$ and statistically indistinguishable from \"\n            r\"$\\lambda = 0.01$ (56.33\\%, $p > 0.1$; Appendix~\\ref{sec:appendix_null}). \"\n            r\"At $\\lambda = 0.1$, a modest increase emerges \"\n            r\"(Section~\\ref{sec:lambda_high}), but per-task CAR ordering \"\n            r\"remains identical across all conditions (chocolate\\_pudding highest, \"\n            r\"bbq\\_sauce lowest), indicating that avoidance patterns reflect the \"\n            r\"demonstration distribution regardless of SDF loss weight. A Phase~2 \"\n            r\"ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,58.0\\%\\footnote{\"\n            r\"At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); \"\n            r\"full 30K training did not complete due to disk constraints.}, suggesting \"\n            r\"that SDF gradients do not produce a lasting behavioral effect.\"\n        )\n    else:\n        new = fill(\n            r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n            r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n            r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n            r\"avoidance. Adding SDF supervision does not yield statistically significant \"\n            r\"improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically \"\n            r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"\n            r\"({mean_car}\\%, $p = {p_value}$; Appendix~\\ref{sec:appendix_null}). \"\n            r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"\n            r\"CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 \"\n            r\"training, single seed s2); full 30K training did not complete due to disk \"\n            r\"constraints.}, suggesting that SDF gradients do not produce a lasting \"\n            r\"behavioral effect. The per-task CAR ordering \"\n            r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"\n            r\"lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating \"\n            r\"that avoidance patterns reflect the demonstration distribution rather than \"\n            r\"geometric supervision.\", v)\n    R.append((\"claim3.tex\", \"claim3 L27 body\", old, new))\n\n    # 7. claim3.tex L32-33 dose-response paragraph\n    hdr = r\"\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\"\n    old_body = (\n        r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n        r\"CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint \"\n        r\"(3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null \"\n        r\"distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n        r\"$p = 0.131$\\footnote{One-tailed permutation \"\n        r\"$p = 0.071$; even with the directional prior that SDF \"\n        r\"should not \\emph{decrease} CAR, the result remains \"\n        r\"non-significant.}). SDF supervision does not produce statistically \"\n        r\"significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ \"\n        r\"(Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level \"\n        r\"failure analysis (Section~\\ref{sec:conclusion}): because even a \"\n        r\"20$\\times$ increase in SDF loss weight fails to produce additional \"\n        r\"avoidance, the binding constraint is not training signal magnitude but \"\n        r\"the structural mismatch between end-effector monitoring and full-body \"\n        r\"collision surfaces. Stronger geometric supervision cannot compensate for \"\n        r\"supervising the wrong collision surface.\"\n    )\n    old = hdr + \"\\n\" + old_body\n    if is_c:\n        new_body = fill(\n            r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n            r\"CAR\\,=\\,{mean_car}\\%\\,$\\pm$\\,{std_car} at the 30K checkpoint \"\n            r\"(3 seeds: {s0_car}\\%, {s1_car}\\%, {s2_car}\\%), a modest but \"\n            r\"statistically significant departure from the null distribution \"\n            r\"(mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n            r\"$p = {p_value}$\\footnote{One-tailed permutation \"\n            r\"$p = {p_one_value}$; the directional prior that SDF should not \"\n            r\"\\emph{decrease} CAR supports a one-tailed test, but we report \"\n            r\"the conservative two-tailed value in the main text.}). The \"\n            r\"effect size of {delta_pp}\\,pp is small relative to the $+$26\\,pp gain \"\n            r\"from LoRA fine-tuning alone, indicating that EE-only SDF supervision \"\n            r\"can incrementally augment demonstration-driven avoidance at sufficiently \"\n            r\"high loss weights but cannot substitute for it. A stepwise ablation across \"\n            r\"six checkpoints (16K--28K) shows no sustained trend prior to 30K \"\n            r\"(mean 55.3\\%, within 0.4$\\sigma$ of the null; \"\n            r\"Appendix~\\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K \"\n            r\"remains identical to all other conditions \"\n            r\"(Figure~\\ref{fig:lambda_car}), confirming that the dominant avoidance \"\n            r\"signal remains the demonstration distribution. The response is thus \"\n            r\"dose-dependent: SDF shows no significant benefit at $\\lambda \\leq 0.01$ \"\n            r\"($p > 0.1$), with a small but detectable effect at $\\lambda = 0.1$ \"\n            r\"that preserves the same demonstration-driven avoidance fingerprint.\", v)\n    else:\n        new_body = fill(\n            r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n            r\"CAR\\,=\\,{mean_car}\\%\\,$\\pm$\\,{std_car} at the 30K checkpoint \"\n            r\"(3 seeds: {s0_car}\\%, {s1_car}\\%, {s2_car}\\%), within the null \"\n            r\"distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n            r\"$p = {p_value}$\\footnote{One-tailed permutation \"\n            r\"$p = {p_one_value}$; even with the directional prior that SDF \"\n            r\"should not \\emph{decrease} CAR, the result remains \"\n            r\"non-significant.}). SDF supervision does not produce statistically \"\n            r\"significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ \"\n            r\"(Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level \"\n            r\"failure analysis (Section~\\ref{sec:conclusion}): because even a \"\n            r\"20$\\times$ increase in SDF loss weight fails to produce additional \"\n            r\"avoidance, the binding constraint is not training signal magnitude but \"\n            r\"the structural mismatch between end-effector monitoring and full-body \"\n            r\"collision surfaces. Stronger geometric supervision cannot compensate for \"\n            r\"supervising the wrong collision surface.\", v)\n    R.append((\"claim3.tex\", \"claim3 L32-33 dose-response\", old, hdr + \"\\n\" + new_body))\n\n    # 8. claim3.tex L38 figure caption\n    old = (\n        r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n        r\"$\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within \"\n        r\"the null band ($p > 0.05$), consistent with the absence of statistically \"\n        r\"significant improvement across a 20$\\times$ loss-weight range.}\"\n    )\n    if is_c:\n        new = fill(\n            r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n            r\"$\\lambda = 0$: LoRA-only. Low $\\lambda$ ($\\leq 0.01$) remains within \"\n            r\"the null band; $\\lambda = 0.1$ ({mean_car}\\%, 3 seeds) shows a modest \"\n            r\"but significant departure (permutation $p = {p_value}$, {delta_pp}\\,pp \"\n            r\"effect size) whose per-task avoidance pattern still matches the \"\n            r\"demonstration distribution.}\", v)\n    else:\n        new = (\n            r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n            r\"$\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within \"\n            r\"the null band ($p > 0.05$), consistent with the absence of statistically \"\n            r\"significant improvement across a 20$\\times$ loss-weight range.}\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L38 fig caption\", old, new))\n\n    # 9. discussion.tex L3 scope (Scenario C only)\n    if is_c:\n        old = (\n            r\"and collision-free demonstrations account for nearly all measured \"\n            r\"avoidance gains, with EE-only SDF contributing no statistically \"\n            r\"significant improvement (\\S\\ref{sec:avoidance_source}).\"\n        )\n        new = (\n            r\"and collision-free demonstrations account for nearly all measured \"\n            r\"avoidance gains, with EE-only SDF contributing at most a modest \"\n            r\"increment at high loss weights (\\S\\ref{sec:avoidance_source}).\"\n        )\n        R.append((\"discussion.tex\", \"discussion L3 scope\", old, new))\n\n    # 10. discussion.tex L6\n    old = (\n        r\"Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR \"\n        r\"remains within the null distribution ($p = 0.131$), suggesting \"\n        r\"that EE-only auxiliary SDF loss does not overcome Level~A signal \"\n        r\"masking---the limitation is architectural for this integration pathway.\"\n    )\n    if is_c:\n        new = fill(\n            r\"At $\\lambda \\leq 0.01$, SDF shows no significant benefit; at \"\n            r\"$\\lambda = 0.1$, a modest {delta_pp}\\,pp effect emerges \"\n            r\"($p = {p_value}$) but preserves the same demonstration-driven \"\n            r\"avoidance pattern, suggesting that EE-only SDF can weakly \"\n            r\"augment---but not redirect---the implicit signal at sufficiently \"\n            r\"high loss weights.\", v)\n    else:\n        new = fill(\n            r\"Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR \"\n            r\"remains within the null distribution ($p = {p_value}$), suggesting \"\n            r\"that EE-only auxiliary SDF loss does not overcome Level~A signal \"\n            r\"masking---the limitation is architectural for this integration \"\n            r\"pathway.\", v)\n    R.append((\"discussion.tex\", \"discussion L6\", old, new))\n\n    # 11. discussion.tex L12 limitation\n    old = r\"Full-body SDF remains untested.\"\n    if is_c:\n        new = fill(\n            r\"Full-body SDF remains untested. \"\n            r\"The $\\lambda = 0.1$ effect ({delta_pp}\\,pp, $p = {p_value}$, $n = 3$) \"\n            r\"is statistically significant but small; whether this modest gain \"\n            r\"justifies the computational cost of SDF supervision requires \"\n            r\"task-specific cost-benefit analysis.\", v)\n    else:\n        new = r\"Full-body SDF remains untested.\"\n    R.append((\"discussion.tex\", \"discussion L12 limitation\", old, new))\n\n    return R\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Auto-switch paper for lambda=0.1 s2 30K result\")\n    parser.add_argument(\"--s2-car\", type=float, required=\"--verify\" not in sys.argv)\n    parser.add_argument(\"--s2-tsr\", type=float, default=None)\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--verify\", action=\"store_true\",\n                        help=\"Check all old_strings match current .tex files\")\n    args = parser.parse_args()\n\n    if args.verify:\n        if not PAPER_DIR.exists():\n            print(f\"ERROR: paper dir not found: {PAPER_DIR}\")\n            sys.exit(1)\n        dummy_v = {k: \"X\" for k in [\n            \"s0_car\", \"s1_car\", \"s2_car\", \"mean_car\", \"std_car\",\n            \"tsr_mean\", \"tsr_std\", \"p_value\", \"p_one_value\", \"z_value\", \"delta_pp\"]}\n        all_ok = True\n        for scenario in (\"B\", \"C\"):\n            replacements = get_replacements(scenario, dummy_v)\n            print(f\"--- Scenario {scenario} ({len(replacements)} items) ---\")\n            for filename, label, old, new in replacements:\n                fpath = PAPER_DIR / filename\n                if not fpath.exists():\n                    print(f\"  [MISSING] {label:35s} {filename}\")\n                    all_ok = False\n                    continue\n                content = fpath.read_text()\n                if old in content:\n                    print(f\"  [OK]      {label:35s} {filename}\")\n                else:\n                    print(f\"  [MISMATCH]{label:35s} {filename}\")\n                    print(f\"            Expected: {old[:80]}...\")\n                    all_ok = False\n        sys.exit(0 if all_ok else 1)\n\n    cars = [S0_CAR, S1_CAR, args.s2_car]\n    car_mean = mean(cars)\n    car_std = std_b(cars)\n\n    if args.s2_tsr is not None:\n        tsrs = [S0_TSR, S1_TSR, args.s2_tsr]\n    else:\n        tsrs = [S0_TSR, S1_TSR]\n        print(\"NOTE: --s2-tsr not provided, using 2-seed TSR\")\n    tsr_mean = mean(tsrs)\n    tsr_std = std_b(tsrs)\n\n    p_one, p_two, n_combos = perm_test(NULL_VALUES, cars)\n    z = (car_mean - NULL_MEAN) / NULL_STD\n    delta = car_mean - NULL_MEAN\n\n    scenario = \"C\" if p_one < 0.05 else \"B\"\n\n    v = {\n        \"s0_car\": f\"{S0_CAR:.1f}\",\n        \"s1_car\": f\"{S1_CAR:.1f}\",\n        \"s2_car\": f\"{args.s2_car:.1f}\",\n        \"mean_car\": f\"{car_mean:.2f}\",\n        \"std_car\": f\"{car_std:.2f}\",\n        \"tsr_mean\": f\"{tsr_mean:.1f}\",\n        \"tsr_std\": f\"{tsr_std:.1f}\",\n        \"p_value\": f\"{p_two:.3f}\",\n        \"p_one_value\": f\"{p_one:.3f}\",\n        \"z_value\": f\"{z:.2f}\",\n        \"delta_pp\": f\"{delta:.1f}\",\n    }\n\n    print(\"=\" * 60)\n    print(\"  PAPER SWITCH — lambda=0.1 s2 30K\")\n    print(\"=\" * 60)\n    print(f\"  Input:     s2_car={args.s2_car}, s2_tsr={args.s2_tsr}\")\n    print(f\"  3-seed:    CAR = {v['mean_car']} +/- {v['std_car']}\")\n    print(f\"             TSR = {v['tsr_mean']} +/- {v['tsr_std']} ({len(tsrs)} seeds)\")\n    print(f\"  Perm test: C({len(NULL_VALUES)+len(cars)},{len(cars)}) = {n_combos}\")\n    print(f\"             p_one = {v['p_one_value']}  {'<' if p_one < 0.05 else '>='} 0.05\")\n    print(f\"             p_two = {v['p_value']}\")\n    print(f\"  Z-score:   {v['z_value']}\")\n    print(f\"  Delta:     +{v['delta_pp']} pp\")\n    print(f\"  Scenario:  {scenario}  \"\n          f\"{'(modest but significant)' if scenario == 'C' else '(full redundancy)'}\")\n    print()\n\n    if not PAPER_DIR.exists():\n        print(f\"ERROR: paper dir not found: {PAPER_DIR}\")\n        sys.exit(1)\n\n    replacements = get_replacements(scenario, v)\n\n    files_content = {}\n    counts = {}\n\n    for filename, label, old, new in replacements:\n        fpath = PAPER_DIR / filename\n        if filename not in files_content:\n            if not fpath.exists():\n                print(f\"  !! {filename} not found\")\n                continue\n            files_content[filename] = fpath.read_text()\n            counts[filename] = 0\n\n        content, ok = safe_replace(files_content[filename], old, new, label)\n        files_content[filename] = content\n        if ok:\n            counts[filename] += 1\n            status = \"ok\"\n        else:\n            status = \"FAIL\"\n        print(f\"  [{status:4s}] {label:35s} {filename}\")\n\n    total = sum(counts.values())\n    n_files = sum(1 for c in counts.values() if c > 0)\n    expected = len(replacements)\n    print(f\"\\n  {total}/{expected} replacements in {n_files} files\")\n\n    if args.dry_run:\n        print(\"\\n  DRY RUN — no files modified\")\n        return\n\n    for filename, content in files_content.items():\n        fpath = PAPER_DIR / filename\n        fpath.write_text(content)\n        print(f\"  Wrote {filename} ({counts[filename]} changes)\")\n\n    print(\"\\nCompiling PDF...\")\n    try:\n        result = subprocess.run(\n            [\"latexmk\", \"-pdf\", \"-interaction=nonstopmode\", \"main.tex\"],\n            cwd=PAPER_DIR, capture_output=True, text=True, timeout=120)\n        if result.returncode == 0:\n            print(\"  PDF compiled OK\")\n        else:\n            print(\"  PDF compilation FAILED\")\n            err = result.stderr or result.stdout or \"\"\n            for line in err.split(\"\\n\")[-10:]:\n                if line.strip():\n                    print(f\"    {line}\")\n    except FileNotFoundError:\n        print(\"  latexmk not found — skipping PDF compilation\")\n    except subprocess.TimeoutExpired:\n        print(\"  PDF compilation timed out (120s)\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "29c076ae-081c-4b2e-8d36-50600093b058",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014FYmUDS6XkFiQBoiNh8M68",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 66308,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 66308
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

_source line 42 · 2026-05-28T06:07:32.464Z_

<details><summary>↩ Tool result · `toolu_01NobPtAYmWopf5G8Y3JYhqD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_switch.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "c9c11482-3a17-4030-bb84-4a8d29c926ca",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/paper_switch.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Auto-switch paper text based on λ=0.1 s2 30K eval result.\n\nUsage:\n  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0 --dry-run\n  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0\n\"\"\"\nimport argparse\nimport subprocess\nimport sys\nfrom itertools import combinations\nfrom math import comb, sqrt\nfrom pathlib import Path\n\nNULL_VALUES = [56.5, 52.5, 55, 57, 54, 52.5]\nNULL_MEAN = sum(NULL_VALUES) / len(NULL_VALUES)\nNULL_STD = (sum((x - NULL_MEAN) ** 2 for x in NULL_VALUES) / 5) ** 0.5\n\nS0_CAR, S1_CAR = 58.0, 58.5\nS0_TSR, S1_TSR = 47.0, 49.0\n\nPAPER_DIR = Path(__file__).resolve().parent.parent / \"docs\" / \"paper\"\n\n\ndef mean(v):\n    return sum(v) / len(v)\n\n\ndef std_b(v):\n    m = mean(v)\n    return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5\n\n\ndef perm_test(null_vals, treat_vals):\n    pool = null_vals + treat_vals\n    k = len(treat_vals)\n    obs = mean(treat_vals)\n    mu = mean(pool)\n    dev = abs(obs - mu)\n    n = comb(len(pool), k)\n    ge = tw = 0\n    for c in combinations(pool, k):\n        m = mean(c)\n        if m >= obs:\n            ge += 1\n        if abs(m - mu) >= dev - 1e-12:\n            tw += 1\n    return ge / n, tw / n, n\n\n\ndef fill(tpl, vals):\n    for k, v in vals.items():\n        tpl = tpl.replace(\"{\" + k + \"}\", str(v))\n    return tpl\n\n\ndef safe_replace(content, old, new, label):\n    n = content.count(old)\n    if n == 0:\n        print(f\"  !! [{label}] NOT FOUND\")\n        return content, False\n    if n > 1:\n        print(f\"  !! [{label}] found {n}x\")\n        return content, False\n    return content.replace(old, new), True\n\n\ndef get_replacements(scenario, v):\n    R = []\n    is_c = scenario == \"C\"\n\n    # 1. abstract.tex L5 (training results)\n    old = (\n        r\"collision-free demonstrations alone account for all measured avoidance \"\n        r\"gains (${\\sim}$26 percentage points). SDF supervision shows no statistically \"\n        r\"significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"\n        r\"($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: \"\n        r\"57.00\\%$\\,\\pm\\,$2.18, 3 seeds).\"\n    )\n    if is_c:\n        new = fill(\n            r\"collision-free demonstrations alone account for nearly all measured \"\n            r\"avoidance gains (${\\sim}$26 percentage points). SDF supervision shows no \"\n            r\"statistically significant benefit at $\\lambda \\leq 0.01$ ($p > 0.1$); at \"\n            r\"$\\lambda = 0.1$, a modest but statistically significant increase emerges \"\n            r\"({mean_car}\\%$\\,\\pm\\,${std_car}, permutation $p = {p_value}$, 3 seeds), \"\n            r\"though the effect size ({delta_pp}\\,pp) is small relative to the \"\n            r\"$+$26\\,pp gain from fine-tuning alone.\", v)\n    else:\n        new = fill(\n            r\"collision-free demonstrations alone account for all measured avoidance \"\n            r\"gains (${\\sim}$26 percentage points). SDF supervision shows no statistically \"\n            r\"significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"\n            r\"($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: \"\n            r\"{mean_car}\\%$\\,\\pm\\,${std_car}, 3 seeds).\", v)\n    R.append((\"abstract.tex\", \"abstract L5 training\", old, new))\n\n    # 2. abstract.tex L6 (concluding sentence)\n    old = (\n        r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n        r\"EE-only geometric supervision does not significantly improve collision \"\n        r\"avoidance across a 20$\\times$ loss-weight range, suggesting that collision \"\n        r\"avoidance primarily arises from demonstration data rather than geometric \"\n        r\"supervision.\"\n    )\n    if is_c:\n        new = (\n            r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n            r\"Even at the highest tested loss weight, the modest SDF effect is dwarfed by \"\n            r\"demonstration-driven avoidance and cannot overcome the structural limitation \"\n            r\"of EE-only supervision.\"\n        )\n    else:\n        new = (\n            r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n            r\"EE-only geometric supervision does not significantly improve collision \"\n            r\"avoidance across a 20$\\times$ loss-weight range, suggesting that collision \"\n            r\"avoidance primarily arises from demonstration data rather than geometric \"\n            r\"supervision.\"\n        )\n    R.append((\"abstract.tex\", \"abstract L6 conclusion\", old, new))\n\n    # 3. claim3.tex L3 scope sentence\n    old = (\n        r\"We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of \"\n        r\"loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all \"\n        r\"evaluated at the 30K-step checkpoint.\"\n    )\n    if is_c:\n        new = (\n            r\"We compare LoRA-only against LoRA+SDF at three loss weights \"\n            r\"($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at \"\n            r\"the 30K-step checkpoint.\"\n        )\n    else:\n        new = (\n            r\"We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of \"\n            r\"loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all \"\n            r\"evaluated at the 30K-step checkpoint.\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L3 scope\", old, new))\n\n    # 4. claim3.tex L7 table caption\n    old = (\n        r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no \"\n        r\"statistically significant CAR improvement beyond LoRA-only at the tested \"\n        r\"scale $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"\n        r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\"\n    )\n    if is_c:\n        new = fill(\n            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF at \"\n            r\"$\\lambda \\leq 0.01$ shows no statistically significant CAR improvement \"\n            r\"beyond LoRA-only ($p > 0.1$). At $\\lambda = 0.1$, a modest increase \"\n            r\"reaches statistical significance ($z = {z_value}$, permutation \"\n            r\"$p = {p_value}$, $n{=}3$), though the effect size ({delta_pp}\\,pp) \"\n            r\"is small relative to the $+$26\\,pp LoRA gain. All fine-tuned models \"\n            r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\", v)\n    else:\n        new = (\n            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no \"\n            r\"statistically significant CAR improvement beyond LoRA-only at the tested \"\n            r\"scale $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"\n            r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L7 caption\", old, new))\n\n    # 5. claim3.tex L20 table row\n    old = (\n        r\"LoRA+SDF $\\lambda{=}0.1$ & 3 & \"\n        r\"50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\"\n    )\n    new = fill(\n        r\"LoRA+SDF $\\lambda{=}0.1$ & 3 & \"\n        r\"{tsr_mean}\\,$\\pm$\\,{tsr_std} & {mean_car}\\,$\\pm$\\,{std_car} & 0.394 \\\\\", v)\n    R.append((\"claim3.tex\", \"claim3 L20 table row\", old, new))\n\n    # 6. claim3.tex L27 body paragraph\n    old = (\n        r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n        r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n        r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n        r\"avoidance. Adding SDF supervision does not yield statistically significant \"\n        r\"improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically \"\n        r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"\n        r\"(57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). \"\n        r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"\n        r\"CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 \"\n        r\"training, single seed s2); full 30K training did not complete due to disk \"\n        r\"constraints.}, suggesting that SDF gradients do not produce a lasting \"\n        r\"behavioral effect. The per-task CAR ordering \"\n        r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"\n        r\"lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating \"\n        r\"that avoidance patterns reflect the demonstration distribution rather than \"\n        r\"geometric supervision.\"\n    )\n    if is_c:\n        new = (\n            r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n            r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n            r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n            r\"avoidance. At $\\lambda \\leq 0.01$, SDF supervision does not yield \"\n            r\"statistically significant improvement: LoRA-only CAR (54.67\\%) is within \"\n            r\"0.17\\,pp of $\\lambda = 0.005$ and statistically indistinguishable from \"\n            r\"$\\lambda = 0.01$ (56.33\\%, $p > 0.1$; Appendix~\\ref{sec:appendix_null}). \"\n            r\"At $\\lambda = 0.1$, a modest increase emerges \"\n            r\"(Section~\\ref{sec:lambda_high}), but per-task CAR ordering \"\n            r\"remains identical across all conditions (chocolate\\_pudding highest, \"\n            r\"bbq\\_sauce lowest), indicating that avoidance patterns reflect the \"\n            r\"demonstration distribution regardless of SDF loss weight. A Phase~2 \"\n            r\"ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,58.0\\%\\footnote{\"\n            r\"At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); \"\n            r\"full 30K training did not complete due to disk constraints.}, suggesting \"\n            r\"that SDF gradients do not produce a lasting behavioral effect.\"\n        )\n    else:\n        new = fill(\n            r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n            r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n            r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n            r\"avoidance. Adding SDF supervision does not yield statistically significant \"\n            r\"improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically \"\n            r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"\n            r\"({mean_car}\\%, $p = {p_value}$; Appendix~\\ref{sec:appendix_null}). \"\n            r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"\n            r\"CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 \"\n            r\"training, single seed s2); full 30K training did not complete due to disk \"\n            r\"constraints.}, suggesting that SDF gradients do not produce a lasting \"\n            r\"behavioral effect. The per-task CAR ordering \"\n            r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"\n            r\"lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating \"\n            r\"that avoidance patterns reflect the demonstration distribution rather than \"\n            r\"geometric supervision.\", v)\n    R.append((\"claim3.tex\", \"claim3 L27 body\", old, new))\n\n    # 7. claim3.tex L32-33 dose-response paragraph\n    hdr = r\"\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\"\n    old_body = (\n        r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n        r\"CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint \"\n        r\"(3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null \"\n        r\"distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n        r\"$p = 0.131$\\footnote{One-tailed permutation \"\n        r\"$p = 0.071$; even with the directional prior that SDF \"\n        r\"should not \\emph{decrease} CAR, the result remains \"\n        r\"non-significant.}). SDF supervision does not produce statistically \"\n        r\"significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ \"\n        r\"(Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level \"\n        r\"failure analysis (Section~\\ref{sec:conclusion}): because even a \"\n        r\"20$\\times$ increase in SDF loss weight fails to produce additional \"\n        r\"avoidance, the binding constraint is not training signal magnitude but \"\n        r\"the structural mismatch between end-effector monitoring and full-body \"\n        r\"collision surfaces. Stronger geometric supervision cannot compensate for \"\n        r\"supervising the wrong collision surface.\"\n    )\n    old = hdr + \"\\n\" + old_body\n    if is_c:\n        new_body = fill(\n            r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n            r\"CAR\\,=\\,{mean_car}\\%\\,$\\pm$\\,{std_car} at the 30K checkpoint \"\n            r\"(3 seeds: {s0_car}\\%, {s1_car}\\%, {s2_car}\\%), a modest but \"\n            r\"statistically significant departure from the null distribution \"\n            r\"(mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n            r\"$p = {p_value}$\\footnote{One-tailed permutation \"\n            r\"$p = {p_one_value}$; the directional prior that SDF should not \"\n            r\"\\emph{decrease} CAR supports a one-tailed test, but we report \"\n            r\"the conservative two-tailed value in the main text.}). The \"\n            r\"effect size of {delta_pp}\\,pp is small relative to the $+$26\\,pp gain \"\n            r\"from LoRA fine-tuning alone, indicating that EE-only SDF supervision \"\n            r\"can incrementally augment demonstration-driven avoidance at sufficiently \"\n            r\"high loss weights but cannot substitute for it. A stepwise ablation across \"\n            r\"six checkpoints (16K--28K) shows no sustained trend prior to 30K \"\n            r\"(mean 55.3\\%, within 0.4$\\sigma$ of the null; \"\n            r\"Appendix~\\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K \"\n            r\"remains identical to all other conditions \"\n            r\"(Figure~\\ref{fig:lambda_car}), confirming that the dominant avoidance \"\n            r\"signal remains the demonstration distribution. The response is thus \"\n            r\"dose-dependent: SDF shows no significant benefit at $\\lambda \\leq 0.01$ \"\n            r\"($p > 0.1$), with a small but detectable effect at $\\lambda = 0.1$ \"\n            r\"that preserves the same demonstration-driven avoidance fingerprint.\", v)\n    else:\n        new_body = fill(\n            r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n            r\"CAR\\,=\\,{mean_car}\\%\\,$\\pm$\\,{std_car} at the 30K checkpoint \"\n            r\"(3 seeds: {s0_car}\\%, {s1_car}\\%, {s2_car}\\%), within the null \"\n            r\"distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n            r\"$p = {p_value}$\\footnote{One-tailed permutation \"\n            r\"$p = {p_one_value}$; even with the directional prior that SDF \"\n            r\"should not \\emph{decrease} CAR, the result remains \"\n            r\"non-significant.}). SDF supervision does not produce statistically \"\n            r\"significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ \"\n            r\"(Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level \"\n            r\"failure analysis (Section~\\ref{sec:conclusion}): because even a \"\n            r\"20$\\times$ increase in SDF loss weight fails to produce additional \"\n            r\"avoidance, the binding constraint is not training signal magnitude but \"\n            r\"the structural mismatch between end-effector monitoring and full-body \"\n            r\"collision surfaces. Stronger geometric supervision cannot compensate for \"\n            r\"supervising the wrong collision surface.\", v)\n    R.append((\"claim3.tex\", \"claim3 L32-33 dose-response\", old, hdr + \"\\n\" + new_body))\n\n    # 8. claim3.tex L38 figure caption\n    old = (\n        r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n        r\"$\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within \"\n        r\"the null band ($p > 0.05$), consistent with the absence of statistically \"\n        r\"significant improvement across a 20$\\times$ loss-weight range.}\"\n    )\n    if is_c:\n        new = fill(\n            r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n            r\"$\\lambda = 0$: LoRA-only. Low $\\lambda$ ($\\leq 0.01$) remains within \"\n            r\"the null band; $\\lambda = 0.1$ ({mean_car}\\%, 3 seeds) shows a modest \"\n            r\"but significant departure (permutation $p = {p_value}$, {delta_pp}\\,pp \"\n            r\"effect size) whose per-task avoidance pattern still matches the \"\n            r\"demonstration distribution.}\", v)\n    else:\n        new = (\n            r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n            r\"$\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within \"\n            r\"the null band ($p > 0.05$), consistent with the absence of statistically \"\n            r\"significant improvement across a 20$\\times$ loss-weight range.}\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L38 fig caption\", old, new))\n\n    # 9. discussion.tex L3 scope (Scenario C only)\n    if is_c:\n        old = (\n            r\"and collision-free demonstrations account for nearly all measured \"\n            r\"avoidance gains, with EE-only SDF contributing no statistically \"\n            r\"significant improvement (\\S\\ref{sec:avoidance_source}).\"\n        )\n        new = (\n            r\"and collision-free demonstrations account for nearly all measured \"\n            r\"avoidance gains, with EE-only SDF contributing at most a modest \"\n            r\"increment at high loss weights (\\S\\ref{sec:avoidance_source}).\"\n        )\n        R.append((\"discussion.tex\", \"discussion L3 scope\", old, new))\n\n    # 10. discussion.tex L6\n    old = (\n        r\"Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR \"\n        r\"remains within the null distribution ($p = 0.131$), suggesting \"\n        r\"that EE-only auxiliary SDF loss does not overcome Level~A signal \"\n        r\"masking---the limitation is architectural for this integration pathway.\"\n    )\n    if is_c:\n        new = fill(\n            r\"At $\\lambda \\leq 0.01$, SDF shows no significant benefit; at \"\n            r\"$\\lambda = 0.1$, a modest {delta_pp}\\,pp effect emerges \"\n            r\"($p = {p_value}$) but preserves the same demonstration-driven \"\n            r\"avoidance pattern, suggesting that EE-only SDF can weakly \"\n            r\"augment---but not redirect---the implicit signal at sufficiently \"\n            r\"high loss weights.\", v)\n    else:\n        new = fill(\n            r\"Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR \"\n            r\"remains within the null distribution ($p = {p_value}$), suggesting \"\n            r\"that EE-only auxiliary SDF loss does not overcome Level~A signal \"\n            r\"masking---the limitation is architectural for this integration \"\n            r\"pathway.\", v)\n    R.append((\"discussion.tex\", \"discussion L6\", old, new))\n\n    # 11. discussion.tex L12 limitation\n    old = r\"Full-body SDF remains untested.\"\n    if is_c:\n        new = fill(\n            r\"Full-body SDF remains untested. \"\n            r\"The $\\lambda = 0.1$ effect ({delta_pp}\\,pp, $p = {p_value}$, $n = 3$) \"\n            r\"is statistically significant but small; whether this modest gain \"\n            r\"justifies the computational cost of SDF supervision requires \"\n            r\"task-specific cost-benefit analysis.\", v)\n    else:\n        new = r\"Full-body SDF remains untested.\"\n    R.append((\"discussion.tex\", \"discussion L12 limitation\", old, new))\n\n    return R\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Auto-switch paper for lambda=0.1 s2 30K result\")\n    parser.add_argument(\"--s2-car\", type=float, required=\"--verify\" not in sys.argv)\n    parser.add_argument(\"--s2-tsr\", type=float, default=None)\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--verify\", action=\"store_true\",\n                        help=\"Check all old_strings match current .tex files\")\n    args = parser.parse_args()\n\n    if args.verify:\n        if not PAPER_DIR.exists():\n            print(f\"ERROR: paper dir not found: {PAPER_DIR}\")\n            sys.exit(1)\n        dummy_v = {k: \"X\" for k in [\n            \"s0_car\", \"s1_car\", \"s2_car\", \"mean_car\", \"std_car\",\n            \"tsr_mean\", \"tsr_std\", \"p_value\", \"p_one_value\", \"z_value\", \"delta_pp\"]}\n        all_ok = True\n        for scenario in (\"B\", \"C\"):\n            replacements = get_replacements(scenario, dummy_v)\n            print(f\"--- Scenario {scenario} ({len(replacements)} items) ---\")\n            for filename, label, old, new in replacements:\n                fpath = PAPER_DIR / filename\n                if not fpath.exists():\n                    print(f\"  [MISSING] {label:35s} {filename}\")\n                    all_ok = False\n                    continue\n                content = fpath.read_text()\n                if old in content:\n                    print(f\"  [OK]      {label:35s} {filename}\")\n                else:\n                    print(f\"  [MISMATCH]{label:35s} {filename}\")\n                    print(f\"            Expected: {old[:80]}...\")\n                    all_ok = False\n        sys.exit(0 if all_ok else 1)\n\n    cars = [S0_CAR, S1_CAR, args.s2_car]\n    car_mean = mean(cars)\n    car_std = std_b(cars)\n\n    if args.s2_tsr is not None:\n        tsrs = [S0_TSR, S1_TSR, args.s2_tsr]\n    else:\n        tsrs = [S0_TSR, S1_TSR]\n        print(\"NOTE: --s2-tsr not provided, using 2-seed TSR\")\n    tsr_mean = mean(tsrs)\n    tsr_std = std_b(tsrs)\n\n    p_one, p_two, n_combos = perm_test(NULL_VALUES, cars)\n    z = (car_mean - NULL_MEAN) / NULL_STD\n    delta = car_mean - NULL_MEAN\n\n    scenario = \"C\" if p_one < 0.05 else \"B\"\n\n    v = {\n        \"s0_car\": f\"{S0_CAR:.1f}\",\n        \"s1_car\": f\"{S1_CAR:.1f}\",\n        \"s2_car\": f\"{args.s2_car:.1f}\",\n        \"mean_car\": f\"{car_mean:.2f}\",\n        \"std_car\": f\"{car_std:.2f}\",\n        \"tsr_mean\": f\"{tsr_mean:.1f}\",\n        \"tsr_std\": f\"{tsr_std:.1f}\",\n        \"p_value\": f\"{p_two:.3f}\",\n        \"p_one_value\": f\"{p_one:.3f}\",\n        \"z_value\": f\"{z:.2f}\",\n        \"delta_pp\": f\"{delta:.1f}\",\n    }\n\n    print(\"=\" * 60)\n    print(\"  PAPER SWITCH — lambda=0.1 s2 30K\")\n    print(\"=\" * 60)\n    print(f\"  Input:     s2_car={args.s2_car}, s2_tsr={args.s2_tsr}\")\n    print(f\"  3-seed:    CAR = {v['mean_car']} +/- {v['std_car']}\")\n    print(f\"             TSR = {v['tsr_mean']} +/- {v['tsr_std']} ({len(tsrs)} seeds)\")\n    print(f\"  Perm test: C({len(NULL_VALUES)+len(cars)},{len(cars)}) = {n_combos}\")\n    print(f\"             p_one = {v['p_one_value']}  {'<' if p_one < 0.05 else '>='} 0.05\")\n    print(f\"             p_two = {v['p_value']}\")\n    print(f\"  Z-score:   {v['z_value']}\")\n    print(f\"  Delta:     +{v['delta_pp']} pp\")\n    print(f\"  Scenario:  {scenario}  \"\n          f\"{'(modest but significant)' if scenario == 'C' else '(full redundancy)'}\")\n    print()\n\n    if not PAPER_DIR.exists():\n        print(f\"ERROR: paper dir not found: {PAPER_DIR}\")\n        sys.exit(1)\n\n    replacements = get_replacements(scenario, v)\n\n    files_content = {}\n    counts = {}\n\n    for filename, label, old, new in replacements:\n        fpath = PAPER_DIR / filename\n        if filename not in files_content:\n            if not fpath.exists():\n                print(f\"  !! {filename} not found\")\n                continue\n            files_content[filename] = fpath.read_text()\n            counts[filename] = 0\n\n        content, ok = safe_replace(files_content[filename], old, new, label)\n        files_content[filename] = content\n        if ok:\n            counts[filename] += 1\n            status = \"ok\"\n        else:\n            status = \"FAIL\"\n        print(f\"  [{status:4s}] {label:35s} {filename}\")\n\n    total = sum(counts.values())\n    n_files = sum(1 for c in counts.values() if c > 0)\n    expected = len(replacements)\n    print(f\"\\n  {total}/{expected} replacements in {n_files} files\")\n\n    if args.dry_run:\n        print(\"\\n  DRY RUN — no files modified\")\n        return\n\n    for filename, content in files_content.items():\n        fpath = PAPER_DIR / filename\n        fpath.write_text(content)\n        print(f\"  Wrote {filename} ({counts[filename]} changes)\")\n\n    print(\"\\nCompiling PDF...\")\n    try:\n        result = subprocess.run(\n            [\"latexmk\", \"-pdf\", \"-interaction=nonstopmode\", \"main.tex\"],\n            cwd=PAPER_DIR, capture_output=True, text=True, timeout=120)\n        if result.returncode == 0:\n            print(\"  PDF compiled OK\")\n        else:\n            print(\"  PDF compilation FAILED\")\n            err = result.stderr or result.stdout or \"\"\n            for line in err.split(\"\\n\")[-10:]:\n                if line.strip():\n                    print(f\"    {line}\")\n    except FileNotFoundError:\n        print(\"  latexmk not found — skipping PDF compilation\")\n    except subprocess.TimeoutExpired:\n        print(\"  PDF compilation timed out (120s)\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [
      {
        "oldStart": 72,
        "oldLines": 15,
        "newStart": 72,
        "newLines": 16,
        "lines": [
          "     # 1. abstract.tex L5 (training results)",
          "     old = (",
          "         r\"collision-free demonstrations alone account for all measured avoidance \"",
          "-        r\"gains (${\\sim}$26 percentage points). SDF supervision adds no measurable \"",
          "-        r\"benefit across the full tested range $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"",
          "-        r\"($p > 0.05$ for all; $\\lambda = 0.1$: 57.00\\%$\\,\\pm\\,$2.18, 3 seeds).\"",
          "+        r\"gains (${\\sim}$26 percentage points). SDF supervision shows no statistically \"",
          "+        r\"significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"",
          "+        r\"($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: \"",
          "+        r\"57.00\\%$\\,\\pm\\,$2.18, 3 seeds).\"",
          "     )",
          "     if is_c:",
          "         new = fill(",
          "             r\"collision-free demonstrations alone account for nearly all measured \"",
          "-            r\"avoidance gains (${\\sim}$26 percentage points). SDF supervision adds no \"",
          "-            r\"significant benefit at $\\lambda \\leq 0.01$ ($p > 0.1$); at \"",
          "+            r\"avoidance gains (${\\sim}$26 percentage points). SDF supervision shows no \"",
          "+            r\"statistically significant benefit at $\\lambda \\leq 0.01$ ($p > 0.1$); at \"",
          "             r\"$\\lambda = 0.1$, a modest but statistically significant increase emerges \"",
          "             r\"({mean_car}\\%$\\,\\pm\\,${std_car}, permutation $p = {p_value}$, 3 seeds), \"",
          "             r\"though the effect size ({delta_pp}\\,pp) is small relative to the \""
        ]
      },
      {
        "oldStart": 88,
        "oldLines": 18,
        "newStart": 89,
        "newLines": 19,
        "lines": [
          "     else:",
          "         new = fill(",
          "             r\"collision-free demonstrations alone account for all measured avoidance \"",
          "-            r\"gains (${\\sim}$26 percentage points). SDF supervision adds no measurable \"",
          "-            r\"benefit across the full tested range $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"",
          "-            r\"($p > 0.05$ for all; $\\lambda = 0.1$: {mean_car}\\%$\\,\\pm\\,${std_car}, \"",
          "-            r\"3 seeds).\", v)",
          "+            r\"gains (${\\sim}$26 percentage points). SDF supervision shows no statistically \"",
          "+            r\"significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"",
          "+            r\"($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: \"",
          "+            r\"{mean_car}\\%$\\,\\pm\\,${std_car}, 3 seeds).\", v)",
          "     R.append((\"abstract.tex\", \"abstract L5 training\", old, new))",
          " ",
          "     # 2. abstract.tex L6 (concluding sentence)",
          "     old = (",
          "         r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"",
          "-        r\"EE-only geometric supervision is fully redundant across a 20$\\times$ \"",
          "-        r\"loss-weight range, confirming that collision avoidance arises from \"",
          "-        r\"demonstration data, not geometric supervision.\"",
          "+        r\"EE-only geometric supervision does not significantly improve collision \"",
          "+        r\"avoidance across a 20$\\times$ loss-weight range, suggesting that collision \"",
          "+        r\"avoidance primarily arises from demonstration data rather than geometric \"",
          "+        r\"supervision.\"",
          "     )",
          "     if is_c:",
          "         new = ("
        ]
      },
      {
        "oldStart": 111,
        "oldLines": 9,
        "newStart": 113,
        "newLines": 10,
        "lines": [
          "     else:",
          "         new = (",
          "             r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"",
          "-            r\"EE-only geometric supervision is fully redundant across a 20$\\times$ \"",
          "-            r\"loss-weight range, confirming that collision avoidance arises from \"",
          "-            r\"demonstration data, not geometric supervision.\"",
          "+            r\"EE-only geometric supervision does not significantly improve collision \"",
          "+            r\"avoidance across a 20$\\times$ loss-weight range, suggesting that collision \"",
          "+            r\"avoidance primarily arises from demonstration data rather than geometric \"",
          "+            r\"supervision.\"",
          "         )",
          "     R.append((\"abstract.tex\", \"abstract L6 conclusion\", old, new))",
          " "
        ]
      },
      {
        "oldStart": 139,
        "oldLines": 25,
        "newStart": 142,
        "newLines": 25,
        "lines": [
          " ",
          "     # 4. claim3.tex L7 table caption",
          "     old = (",
          "-        r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no \"",
          "-        r\"measurable CAR beyond LoRA-only across the full tested range \"",
          "-        r\"$\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"",
          "+        r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no \"",
          "+        r\"statistically significant CAR improvement beyond LoRA-only at the tested \"",
          "+        r\"scale $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"",
          "         r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\"",
          "     )",
          "     if is_c:",
          "         new = fill(",
          "             r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF at \"",
          "-            r\"$\\lambda \\leq 0.01$ adds no measurable CAR beyond LoRA-only \"",
          "-            r\"($p > 0.1$). At $\\lambda = 0.1$, a modest increase reaches \"",
          "-            r\"statistical significance ($z = {z_value}$, permutation \"",
          "+            r\"$\\lambda \\leq 0.01$ shows no statistically significant CAR improvement \"",
          "+            r\"beyond LoRA-only ($p > 0.1$). At $\\lambda = 0.1$, a modest increase \"",
          "+            r\"reaches statistical significance ($z = {z_value}$, permutation \"",
          "             r\"$p = {p_value}$, $n{=}3$), though the effect size ({delta_pp}\\,pp) \"",
          "             r\"is small relative to the $+$26\\,pp LoRA gain. All fine-tuned models \"",
          "             r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\", v)",
          "     else:",
          "         new = (",
          "-            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no \"",
          "-            r\"measurable CAR beyond LoRA-only across the full tested range \"",
          "-            r\"$\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"",
          "+            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no \"",
          "+            r\"statistically significant CAR improvement beyond LoRA-only at the tested \"",
          "+            r\"scale $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"",
          "             r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\"",
          "         )",
          "     R.append((\"claim3.tex\", \"claim3 L7 caption\", old, new))"
        ]
      },
      {
        "oldStart": 177,
        "oldLines": 14,
        "newStart": 180,
        "newLines": 15,
        "lines": [
          "         r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"",
          "         r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"",
          "         r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"",
          "-        r\"avoidance. Adding SDF supervision produces no measurable benefit across the \"",
          "-        r\"full tested range: LoRA-only CAR (54.67\\%) is statistically \"",
          "+        r\"avoidance. Adding SDF supervision does not yield statistically significant \"",
          "+        r\"improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically \"",
          "         r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"",
          "         r\"(57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). \"",
          "         r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"",
          "-        r\"CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints \"",
          "-        r\"precluded additional seeds for this ablation.}, confirming that SDF \"",
          "-        r\"gradients produce no lasting behavioral effect. The per-task CAR ordering \"",
          "+        r\"CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 \"",
          "+        r\"training, single seed s2); full 30K training did not complete due to disk \"",
          "+        r\"constraints.}, suggesting that SDF gradients do not produce a lasting \"",
          "+        r\"behavioral effect. The per-task CAR ordering \"",
          "         r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"",
          "         r\"lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating \"",
          "         r\"that avoidance patterns reflect the demonstration distribution rather than \""
        ]
      },
      {
        "oldStart": 195,
        "oldLines": 32,
        "newStart": 199,
        "newLines": 34,
        "lines": [
          "             r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"",
          "             r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"",
          "             r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"",
          "-            r\"avoidance. At $\\lambda \\leq 0.01$, SDF supervision produces no measurable \"",
          "-            r\"benefit: LoRA-only CAR (54.67\\%) is within 0.17\\,pp of $\\lambda = 0.005$ \"",
          "-            r\"and statistically indistinguishable from $\\lambda = 0.01$ (56.33\\%, \"",
          "-            r\"$p > 0.1$; Appendix~\\ref{sec:appendix_null}). At $\\lambda = 0.1$, a modest \"",
          "-            r\"increase emerges (Section~\\ref{sec:lambda_high}), but per-task CAR ordering \"",
          "+            r\"avoidance. At $\\lambda \\leq 0.01$, SDF supervision does not yield \"",
          "+            r\"statistically significant improvement: LoRA-only CAR (54.67\\%) is within \"",
          "+            r\"0.17\\,pp of $\\lambda = 0.005$ and statistically indistinguishable from \"",
          "+            r\"$\\lambda = 0.01$ (56.33\\%, $p > 0.1$; Appendix~\\ref{sec:appendix_null}). \"",
          "+            r\"At $\\lambda = 0.1$, a modest increase emerges \"",
          "+            r\"(Section~\\ref{sec:lambda_high}), but per-task CAR ordering \"",
          "             r\"remains identical across all conditions (chocolate\\_pudding highest, \"",
          "             r\"bbq\\_sauce lowest), indicating that avoidance patterns reflect the \"",
          "             r\"demonstration distribution regardless of SDF loss weight. A Phase~2 \"",
          "-            r\"ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{\"",
          "-            r\"Single seed (s2); computational constraints precluded additional seeds for \"",
          "-            r\"this ablation.}, confirming that SDF gradients produce no lasting behavioral \"",
          "-            r\"effect.\"",
          "+            r\"ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,58.0\\%\\footnote{\"",
          "+            r\"At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); \"",
          "+            r\"full 30K training did not complete due to disk constraints.}, suggesting \"",
          "+            r\"that SDF gradients do not produce a lasting behavioral effect.\"",
          "         )",
          "     else:",
          "         new = fill(",
          "             r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"",
          "             r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"",
          "             r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"",
          "-            r\"avoidance. Adding SDF supervision produces no measurable benefit across the \"",
          "-            r\"full tested range: LoRA-only CAR (54.67\\%) is statistically \"",
          "+            r\"avoidance. Adding SDF supervision does not yield statistically significant \"",
          "+            r\"improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically \"",
          "             r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"",
          "             r\"({mean_car}\\%, $p = {p_value}$; Appendix~\\ref{sec:appendix_null}). \"",
          "             r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"",
          "-            r\"CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints \"",
          "-            r\"precluded additional seeds for this ablation.}, confirming that SDF \"",
          "-            r\"gradients produce no lasting behavioral effect. The per-task CAR ordering \"",
          "+            r\"CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 \"",
          "+            r\"training, single seed s2); full 30K training did not complete due to disk \"",
          "+            r\"constraints.}, suggesting that SDF gradients do not produce a lasting \"",
          "+            r\"behavioral effect. The per-task CAR ordering \"",
          "             r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"",
          "             r\"lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating \"",
          "             r\"that avoidance patterns reflect the demonstration distribution rather than \""
        ]
      },
      {
        "oldStart": 237,
        "oldLines": 8,
        "newStart": 243,
        "newLines": 8,
        "lines": [
          "         r\"$p = 0.131$\\footnote{One-tailed permutation \"",
          "         r\"$p = 0.071$; even with the directional prior that SDF \"",
          "         r\"should not \\emph{decrease} CAR, the result remains \"",
          "-        r\"non-significant.}). SDF supervision is redundant with the demonstration \"",
          "-        r\"signal across the full tested range $\\lambda \\in [0.005, 0.1]$ \"",
          "+        r\"non-significant.}). SDF supervision does not produce statistically \"",
          "+        r\"significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ \"",
          "         r\"(Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level \"",
          "         r\"failure analysis (Section~\\ref{sec:conclusion}): because even a \"",
          "         r\"20$\\times$ increase in SDF loss weight fails to produce additional \""
        ]
      },
      {
        "oldStart": 269,
        "oldLines": 7,
        "newStart": 275,
        "newLines": 7,
        "lines": [
          "             r\"remains identical to all other conditions \"",
          "             r\"(Figure~\\ref{fig:lambda_car}), confirming that the dominant avoidance \"",
          "             r\"signal remains the demonstration distribution. The response is thus \"",
          "-            r\"dose-dependent: SDF is fully redundant at $\\lambda \\leq 0.01$ \"",
          "+            r\"dose-dependent: SDF shows no significant benefit at $\\lambda \\leq 0.01$ \"",
          "             r\"($p > 0.1$), with a small but detectable effect at $\\lambda = 0.1$ \"",
          "             r\"that preserves the same demonstration-driven avoidance fingerprint.\", v)",
          "     else:"
        ]
      },
      {
        "oldStart": 281,
        "oldLines": 8,
        "newStart": 287,
        "newLines": 8,
        "lines": [
          "             r\"$p = {p_value}$\\footnote{One-tailed permutation \"",
          "             r\"$p = {p_one_value}$; even with the directional prior that SDF \"",
          "             r\"should not \\emph{decrease} CAR, the result remains \"",
          "-            r\"non-significant.}). SDF supervision is redundant with the demonstration \"",
          "-            r\"signal across the full tested range $\\lambda \\in [0.005, 0.1]$ \"",
          "+            r\"non-significant.}). SDF supervision does not produce statistically \"",
          "+            r\"significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ \"",
          "             r\"(Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level \"",
          "             r\"failure analysis (Section~\\ref{sec:conclusion}): because even a \"",
          "             r\"20$\\times$ increase in SDF loss weight fails to produce additional \""
        ]
      },
      {
        "oldStart": 296,
        "oldLines": 8,
        "newStart": 302,
        "newLines": 8,
        "lines": [
          "     old = (",
          "         r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"",
          "         r\"$\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within \"",
          "-        r\"the null band ($p > 0.05$), confirming full redundancy of EE-only SDF \"",
          "-        r\"supervision across a 20$\\times$ loss-weight range.}\"",
          "+        r\"the null band ($p > 0.05$), consistent with the absence of statistically \"",
          "+        r\"significant improvement across a 20$\\times$ loss-weight range.}\"",
          "     )",
          "     if is_c:",
          "         new = fill("
        ]
      },
      {
        "oldStart": 311,
        "oldLines": 16,
        "newStart": 317,
        "newLines": 17,
        "lines": [
          "         new = (",
          "             r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"",
          "             r\"$\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within \"",
          "-            r\"the null band ($p > 0.05$), confirming full redundancy of EE-only SDF \"",
          "-            r\"supervision across a 20$\\times$ loss-weight range.}\"",
          "+            r\"the null band ($p > 0.05$), consistent with the absence of statistically \"",
          "+            r\"significant improvement across a 20$\\times$ loss-weight range.}\"",
          "         )",
          "     R.append((\"claim3.tex\", \"claim3 L38 fig caption\", old, new))",
          " ",
          "     # 9. discussion.tex L3 scope (Scenario C only)",
          "     if is_c:",
          "         old = (",
          "-            r\"and collision-free demonstrations, not geometric supervision, account \"",
          "-            r\"for the measured avoidance gains (\\S\\ref{sec:avoidance_source}).\"",
          "+            r\"and collision-free demonstrations account for nearly all measured \"",
          "+            r\"avoidance gains, with EE-only SDF contributing no statistically \"",
          "+            r\"significant improvement (\\S\\ref{sec:avoidance_source}).\"",
          "         )",
          "         new = (",
          "             r\"and collision-free demonstrations account for nearly all measured \""
        ]
      },
      {
        "oldStart": 332,
        "oldLines": 23,
        "newStart": 339,
        "newLines": 25,
        "lines": [
          "     # 10. discussion.tex L6",
          "     old = (",
          "         r\"Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR \"",
          "-        r\"remains within the null distribution ($p = 0.131$), confirming \"",
          "-        r\"that Level~A signal masking is not the binding constraint---the failure \"",
          "-        r\"is architectural.\"",
          "+        r\"remains within the null distribution ($p = 0.131$), suggesting \"",
          "+        r\"that EE-only auxiliary SDF loss does not overcome Level~A signal \"",
          "+        r\"masking---the limitation is architectural for this integration pathway.\"",
          "     )",
          "     if is_c:",
          "         new = fill(",
          "-            r\"At $\\lambda \\leq 0.01$, SDF is fully redundant; at $\\lambda = 0.1$, \"",
          "-            r\"a modest {delta_pp}\\,pp effect emerges ($p = {p_value}$) but preserves \"",
          "-            r\"the same demonstration-driven avoidance pattern, suggesting that \"",
          "-            r\"EE-only SDF can weakly augment---but not redirect---the implicit signal \"",
          "-            r\"at sufficiently high loss weights.\", v)",
          "+            r\"At $\\lambda \\leq 0.01$, SDF shows no significant benefit; at \"",
          "+            r\"$\\lambda = 0.1$, a modest {delta_pp}\\,pp effect emerges \"",
          "+            r\"($p = {p_value}$) but preserves the same demonstration-driven \"",
          "+            r\"avoidance pattern, suggesting that EE-only SDF can weakly \"",
          "+            r\"augment---but not redirect---the implicit signal at sufficiently \"",
          "+            r\"high loss weights.\", v)",
          "     else:",
          "         new = fill(",
          "             r\"Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR \"",
          "-            r\"remains within the null distribution ($p = {p_value}$), confirming \"",
          "-            r\"that Level~A signal masking is not the binding constraint---the failure \"",
          "-            r\"is architectural.\", v)",
          "+            r\"remains within the null distribution ($p = {p_value}$), suggesting \"",
          "+            r\"that EE-only auxiliary SDF loss does not overcome Level~A signal \"",
          "+            r\"masking---the limitation is architectural for this integration \"",
          "+            r\"pathway.\", v)",
          "     R.append((\"discussion.tex\", \"discussion L6\", old, new))",
          " ",
          "     # 11. discussion.tex L12 limitation"
        ]
      }
    ],
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Auto-switch paper text based on λ=0.1 s2 30K eval result.\n\nUsage:\n  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0 --dry-run\n  python paper_switch.py --s2-car 57.5 --s2-tsr 48.0\n\"\"\"\nimport argparse\nimport subprocess\nimport sys\nfrom itertools import combinations\nfrom math import comb, sqrt\nfrom pathlib import Path\n\nNULL_VALUES = [56.5, 52.5, 55, 57, 54, 52.5]\nNULL_MEAN = sum(NULL_VALUES) / len(NULL_VALUES)\nNULL_STD = (sum((x - NULL_MEAN) ** 2 for x in NULL_VALUES) / 5) ** 0.5\n\nS0_CAR, S1_CAR = 58.0, 58.5\nS0_TSR, S1_TSR = 47.0, 49.0\n\nPAPER_DIR = Path(__file__).resolve().parent.parent / \"docs\" / \"paper\"\n\n\ndef mean(v):\n    return sum(v) / len(v)\n\n\ndef std_b(v):\n    m = mean(v)\n    return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5\n\n\ndef perm_test(null_vals, treat_vals):\n    pool = null_vals + treat_vals\n    k = len(treat_vals)\n    obs = mean(treat_vals)\n    mu = mean(pool)\n    dev = abs(obs - mu)\n    n = comb(len(pool), k)\n    ge = tw = 0\n    for c in combinations(pool, k):\n        m = mean(c)\n        if m >= obs:\n            ge += 1\n        if abs(m - mu) >= dev - 1e-12:\n            tw += 1\n    return ge / n, tw / n, n\n\n\ndef fill(tpl, vals):\n    for k, v in vals.items():\n        tpl = tpl.replace(\"{\" + k + \"}\", str(v))\n    return tpl\n\n\ndef safe_replace(content, old, new, label):\n    n = content.count(old)\n    if n == 0:\n        print(f\"  !! [{label}] NOT FOUND\")\n        return content, False\n    if n > 1:\n        print(f\"  !! [{label}] found {n}x\")\n        return content, False\n    return content.replace(old, new), True\n\n\ndef get_replacements(scenario, v):\n    R = []\n    is_c = scenario == \"C\"\n\n    # 1. abstract.tex L5 (training results)\n    old = (\n        r\"collision-free demonstrations alone account for all measured avoidance \"\n        r\"gains (${\\sim}$26 percentage points). SDF supervision adds no measurable \"\n        r\"benefit across the full tested range $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"\n        r\"($p > 0.05$ for all; $\\lambda = 0.1$: 57.00\\%$\\,\\pm\\,$2.18, 3 seeds).\"\n    )\n    if is_c:\n        new = fill(\n            r\"collision-free demonstrations alone account for nearly all measured \"\n            r\"avoidance gains (${\\sim}$26 percentage points). SDF supervision adds no \"\n            r\"significant benefit at $\\lambda \\leq 0.01$ ($p > 0.1$); at \"\n            r\"$\\lambda = 0.1$, a modest but statistically significant increase emerges \"\n            r\"({mean_car}\\%$\\,\\pm\\,${std_car}, permutation $p = {p_value}$, 3 seeds), \"\n            r\"though the effect size ({delta_pp}\\,pp) is small relative to the \"\n            r\"$+$26\\,pp gain from fine-tuning alone.\", v)\n    else:\n        new = fill(\n            r\"collision-free demonstrations alone account for all measured avoidance \"\n            r\"gains (${\\sim}$26 percentage points). SDF supervision adds no measurable \"\n            r\"benefit across the full tested range $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ \"\n            r\"($p > 0.05$ for all; $\\lambda = 0.1$: {mean_car}\\%$\\,\\pm\\,${std_car}, \"\n            r\"3 seeds).\", v)\n    R.append((\"abstract.tex\", \"abstract L5 training\", old, new))\n\n    # 2. abstract.tex L6 (concluding sentence)\n    old = (\n        r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n        r\"EE-only geometric supervision is fully redundant across a 20$\\times$ \"\n        r\"loss-weight range, confirming that collision avoidance arises from \"\n        r\"demonstration data, not geometric supervision.\"\n    )\n    if is_c:\n        new = (\n            r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n            r\"Even at the highest tested loss weight, the modest SDF effect is dwarfed by \"\n            r\"demonstration-driven avoidance and cannot overcome the structural limitation \"\n            r\"of EE-only supervision.\"\n        )\n    else:\n        new = (\n            r\"Displacement filtering is necessary for meaningful VLA safety evaluation. \"\n            r\"EE-only geometric supervision is fully redundant across a 20$\\times$ \"\n            r\"loss-weight range, confirming that collision avoidance arises from \"\n            r\"demonstration data, not geometric supervision.\"\n        )\n    R.append((\"abstract.tex\", \"abstract L6 conclusion\", old, new))\n\n    # 3. claim3.tex L3 scope sentence\n    old = (\n        r\"We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of \"\n        r\"loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all \"\n        r\"evaluated at the 30K-step checkpoint.\"\n    )\n    if is_c:\n        new = (\n            r\"We compare LoRA-only against LoRA+SDF at three loss weights \"\n            r\"($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at \"\n            r\"the 30K-step checkpoint.\"\n        )\n    else:\n        new = (\n            r\"We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of \"\n            r\"loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all \"\n            r\"evaluated at the 30K-step checkpoint.\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L3 scope\", old, new))\n\n    # 4. claim3.tex L7 table caption\n    old = (\n        r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no \"\n        r\"measurable CAR beyond LoRA-only across the full tested range \"\n        r\"$\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"\n        r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\"\n    )\n    if is_c:\n        new = fill(\n            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF at \"\n            r\"$\\lambda \\leq 0.01$ adds no measurable CAR beyond LoRA-only \"\n            r\"($p > 0.1$). At $\\lambda = 0.1$, a modest increase reaches \"\n            r\"statistical significance ($z = {z_value}$, permutation \"\n            r\"$p = {p_value}$, $n{=}3$), though the effect size ({delta_pp}\\,pp) \"\n            r\"is small relative to the $+$26\\,pp LoRA gain. All fine-tuned models \"\n            r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\", v)\n    else:\n        new = (\n            r\"\\caption{Avoidance source attribution on SafeLIBERO. SDF adds no \"\n            r\"measurable CAR beyond LoRA-only across the full tested range \"\n            r\"$\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models \"\n            r\"exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L7 caption\", old, new))\n\n    # 5. claim3.tex L20 table row\n    old = (\n        r\"LoRA+SDF $\\lambda{=}0.1$ & 3 & \"\n        r\"50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\"\n    )\n    new = fill(\n        r\"LoRA+SDF $\\lambda{=}0.1$ & 3 & \"\n        r\"{tsr_mean}\\,$\\pm$\\,{tsr_std} & {mean_car}\\,$\\pm$\\,{std_car} & 0.394 \\\\\", v)\n    R.append((\"claim3.tex\", \"claim3 L20 table row\", old, new))\n\n    # 6. claim3.tex L27 body paragraph\n    old = (\n        r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n        r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n        r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n        r\"avoidance. Adding SDF supervision produces no measurable benefit across the \"\n        r\"full tested range: LoRA-only CAR (54.67\\%) is statistically \"\n        r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"\n        r\"(57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). \"\n        r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"\n        r\"CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints \"\n        r\"precluded additional seeds for this ablation.}, confirming that SDF \"\n        r\"gradients produce no lasting behavioral effect. The per-task CAR ordering \"\n        r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"\n        r\"lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating \"\n        r\"that avoidance patterns reflect the demonstration distribution rather than \"\n        r\"geometric supervision.\"\n    )\n    if is_c:\n        new = (\n            r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n            r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n            r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n            r\"avoidance. At $\\lambda \\leq 0.01$, SDF supervision produces no measurable \"\n            r\"benefit: LoRA-only CAR (54.67\\%) is within 0.17\\,pp of $\\lambda = 0.005$ \"\n            r\"and statistically indistinguishable from $\\lambda = 0.01$ (56.33\\%, \"\n            r\"$p > 0.1$; Appendix~\\ref{sec:appendix_null}). At $\\lambda = 0.1$, a modest \"\n            r\"increase emerges (Section~\\ref{sec:lambda_high}), but per-task CAR ordering \"\n            r\"remains identical across all conditions (chocolate\\_pudding highest, \"\n            r\"bbq\\_sauce lowest), indicating that avoidance patterns reflect the \"\n            r\"demonstration distribution regardless of SDF loss weight. A Phase~2 \"\n            r\"ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,57.5\\%\\footnote{\"\n            r\"Single seed (s2); computational constraints precluded additional seeds for \"\n            r\"this ablation.}, confirming that SDF gradients produce no lasting behavioral \"\n            r\"effect.\"\n        )\n    else:\n        new = fill(\n            r\"Table~\\ref{tab:avoidance_source} shows that collision-free demonstrations \"\n            r\"alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with \"\n            r\"zero frozen episodes and displacement above 0.37\\,m, confirming genuine \"\n            r\"avoidance. Adding SDF supervision produces no measurable benefit across the \"\n            r\"full tested range: LoRA-only CAR (54.67\\%) is statistically \"\n            r\"indistinguishable from all SDF conditions including $\\lambda = 0.1$ \"\n            r\"({mean_car}\\%, $p = {p_value}$; Appendix~\\ref{sec:appendix_null}). \"\n            r\"A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields \"\n            r\"CAR\\,=\\,57.5\\%\\footnote{Single seed (s2); computational constraints \"\n            r\"precluded additional seeds for this ablation.}, confirming that SDF \"\n            r\"gradients produce no lasting behavioral effect. The per-task CAR ordering \"\n            r\"is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce \"\n            r\"lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating \"\n            r\"that avoidance patterns reflect the demonstration distribution rather than \"\n            r\"geometric supervision.\", v)\n    R.append((\"claim3.tex\", \"claim3 L27 body\", old, new))\n\n    # 7. claim3.tex L32-33 dose-response paragraph\n    hdr = r\"\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\"\n    old_body = (\n        r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n        r\"CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint \"\n        r\"(3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null \"\n        r\"distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n        r\"$p = 0.131$\\footnote{One-tailed permutation \"\n        r\"$p = 0.071$; even with the directional prior that SDF \"\n        r\"should not \\emph{decrease} CAR, the result remains \"\n        r\"non-significant.}). SDF supervision is redundant with the demonstration \"\n        r\"signal across the full tested range $\\lambda \\in [0.005, 0.1]$ \"\n        r\"(Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level \"\n        r\"failure analysis (Section~\\ref{sec:conclusion}): because even a \"\n        r\"20$\\times$ increase in SDF loss weight fails to produce additional \"\n        r\"avoidance, the binding constraint is not training signal magnitude but \"\n        r\"the structural mismatch between end-effector monitoring and full-body \"\n        r\"collision surfaces. Stronger geometric supervision cannot compensate for \"\n        r\"supervising the wrong collision surface.\"\n    )\n    old = hdr + \"\\n\" + old_body\n    if is_c:\n        new_body = fill(\n            r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n            r\"CAR\\,=\\,{mean_car}\\%\\,$\\pm$\\,{std_car} at the 30K checkpoint \"\n            r\"(3 seeds: {s0_car}\\%, {s1_car}\\%, {s2_car}\\%), a modest but \"\n            r\"statistically significant departure from the null distribution \"\n            r\"(mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n            r\"$p = {p_value}$\\footnote{One-tailed permutation \"\n            r\"$p = {p_one_value}$; the directional prior that SDF should not \"\n            r\"\\emph{decrease} CAR supports a one-tailed test, but we report \"\n            r\"the conservative two-tailed value in the main text.}). The \"\n            r\"effect size of {delta_pp}\\,pp is small relative to the $+$26\\,pp gain \"\n            r\"from LoRA fine-tuning alone, indicating that EE-only SDF supervision \"\n            r\"can incrementally augment demonstration-driven avoidance at sufficiently \"\n            r\"high loss weights but cannot substitute for it. A stepwise ablation across \"\n            r\"six checkpoints (16K--28K) shows no sustained trend prior to 30K \"\n            r\"(mean 55.3\\%, within 0.4$\\sigma$ of the null; \"\n            r\"Appendix~\\ref{sec:appendix_stepwise}), and per-task CAR ordering at 30K \"\n            r\"remains identical to all other conditions \"\n            r\"(Figure~\\ref{fig:lambda_car}), confirming that the dominant avoidance \"\n            r\"signal remains the demonstration distribution. The response is thus \"\n            r\"dose-dependent: SDF is fully redundant at $\\lambda \\leq 0.01$ \"\n            r\"($p > 0.1$), with a small but detectable effect at $\\lambda = 0.1$ \"\n            r\"that preserves the same demonstration-driven avoidance fingerprint.\", v)\n    else:\n        new_body = fill(\n            r\"Increasing $\\lambda$ by 20$\\times$ to 0.1 yields \"\n            r\"CAR\\,=\\,{mean_car}\\%\\,$\\pm$\\,{std_car} at the 30K checkpoint \"\n            r\"(3 seeds: {s0_car}\\%, {s1_car}\\%, {s2_car}\\%), within the null \"\n            r\"distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation \"\n            r\"$p = {p_value}$\\footnote{One-tailed permutation \"\n            r\"$p = {p_one_value}$; even with the directional prior that SDF \"\n            r\"should not \\emph{decrease} CAR, the result remains \"\n            r\"non-significant.}). SDF supervision is redundant with the demonstration \"\n            r\"signal across the full tested range $\\lambda \\in [0.005, 0.1]$ \"\n            r\"(Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level \"\n            r\"failure analysis (Section~\\ref{sec:conclusion}): because even a \"\n            r\"20$\\times$ increase in SDF loss weight fails to produce additional \"\n            r\"avoidance, the binding constraint is not training signal magnitude but \"\n            r\"the structural mismatch between end-effector monitoring and full-body \"\n            r\"collision surfaces. Stronger geometric supervision cannot compensate for \"\n            r\"supervising the wrong collision surface.\", v)\n    R.append((\"claim3.tex\", \"claim3 L32-33 dose-response\", old, hdr + \"\\n\" + new_body))\n\n    # 8. claim3.tex L38 figure caption\n    old = (\n        r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n        r\"$\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within \"\n        r\"the null band ($p > 0.05$), confirming full redundancy of EE-only SDF \"\n        r\"supervision across a 20$\\times$ loss-weight range.}\"\n    )\n    if is_c:\n        new = fill(\n            r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n            r\"$\\lambda = 0$: LoRA-only. Low $\\lambda$ ($\\leq 0.01$) remains within \"\n            r\"the null band; $\\lambda = 0.1$ ({mean_car}\\%, 3 seeds) shows a modest \"\n            r\"but significant departure (permutation $p = {p_value}$, {delta_pp}\\,pp \"\n            r\"effect size) whose per-task avoidance pattern still matches the \"\n            r\"demonstration distribution.}\", v)\n    else:\n        new = (\n            r\"\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. \"\n            r\"$\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within \"\n            r\"the null band ($p > 0.05$), confirming full redundancy of EE-only SDF \"\n            r\"supervision across a 20$\\times$ loss-weight range.}\"\n        )\n    R.append((\"claim3.tex\", \"claim3 L38 fig caption\", old, new))\n\n    # 9. discussion.tex L3 scope (Scenario C only)\n    if is_c:\n        old = (\n            r\"and collision-free demonstrations, not geometric supervision, account \"\n            r\"for the measured avoidance gains (\\S\\ref{sec:avoidance_source}).\"\n        )\n        new = (\n            r\"and collision-free demonstrations account for nearly all measured \"\n            r\"avoidance gains, with EE-only SDF contributing at most a modest \"\n            r\"increment at high loss weights (\\S\\ref{sec:avoidance_source}).\"\n        )\n        R.append((\"discussion.tex\", \"discussion L3 scope\", old, new))\n\n    # 10. discussion.tex L6\n    old = (\n        r\"Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR \"\n        r\"remains within the null distribution ($p = 0.131$), confirming \"\n        r\"that Level~A signal masking is not the binding constraint---the failure \"\n        r\"is architectural.\"\n    )\n    if is_c:\n        new = fill(\n            r\"At $\\lambda \\leq 0.01$, SDF is fully redundant; at $\\lambda = 0.1$, \"\n            r\"a modest {delta_pp}\\,pp effect emerges ($p = {p_value}$) but preserves \"\n            r\"the same demonstration-driven avoidance pattern, suggesting that \"\n            r\"EE-only SDF can weakly augment---but not redirect---the implicit signal \"\n            r\"at sufficiently high loss weights.\", v)\n    else:\n        new = fill(\n            r\"Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR \"\n            r\"remains within the null distribution ($p = {p_value}$), confirming \"\n            r\"that Level~A signal masking is not the binding constraint---the failure \"\n            r\"is architectural.\", v)\n    R.append((\"discussion.tex\", \"discussion L6\", old, new))\n\n    # 11. discussion.tex L12 limitation\n    old = r\"Full-body SDF remains untested.\"\n    if is_c:\n        new = fill(\n            r\"Full-body SDF remains untested. \"\n            r\"The $\\lambda = 0.1$ effect ({delta_pp}\\,pp, $p = {p_value}$, $n = 3$) \"\n            r\"is statistically significant but small; whether this modest gain \"\n            r\"justifies the computational cost of SDF supervision requires \"\n            r\"task-specific cost-benefit analysis.\", v)\n    else:\n        new = r\"Full-body SDF remains untested.\"\n    R.append((\"discussion.tex\", \"discussion L12 limitation\", old, new))\n\n    return R\n\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Auto-switch paper for lambda=0.1 s2 30K result\")\n    parser.add_argument(\"--s2-car\", type=float, required=\"--verify\" not in sys.argv)\n    parser.add_argument(\"--s2-tsr\", type=float, default=None)\n    parser.add_argument(\"--dry-run\", action=\"store_true\")\n    parser.add_argument(\"--verify\", action=\"store_true\",\n                        help=\"Check all old_strings match current .tex files\")\n    args = parser.parse_args()\n\n    if args.verify:\n        if not PAPER_DIR.exists():\n            print(f\"ERROR: paper dir not found: {PAPER_DIR}\")\n            sys.exit(1)\n        dummy_v = {k: \"X\" for k in [\n            \"s0_car\", \"s1_car\", \"s2_car\", \"mean_car\", \"std_car\",\n            \"tsr_mean\", \"tsr_std\", \"p_value\", \"p_one_value\", \"z_value\", \"delta_pp\"]}\n        all_ok = True\n        for scenario in (\"B\", \"C\"):\n            replacements = get_replacements(scenario, dummy_v)\n            print(f\"--- Scenario {scenario} ({len(replacements)} items) ---\")\n            for filename, label, old, new in replacements:\n                fpath = PAPER_DIR / filename\n                if not fpath.exists():\n                    print(f\"  [MISSING] {label:35s} {filename}\")\n                    all_ok = False\n                    continue\n                content = fpath.read_text()\n                if old in content:\n                    print(f\"  [OK]      {label:35s} {filename}\")\n                else:\n                    print(f\"  [MISMATCH]{label:35s} {filename}\")\n                    print(f\"            Expected: {old[:80]}...\")\n                    all_ok = False\n        sys.exit(0 if all_ok else 1)\n\n    cars = [S0_CAR, S1_CAR, args.s2_car]\n    car_mean = mean(cars)\n    car_std = std_b(cars)\n\n    if args.s2_tsr is not None:\n        tsrs = [S0_TSR, S1_TSR, args.s2_tsr]\n    else:\n        tsrs = [S0_TSR, S1_TSR]\n        print(\"NOTE: --s2-tsr not provided, using 2-seed TSR\")\n    tsr_mean = mean(tsrs)\n    tsr_std = std_b(tsrs)\n\n    p_one, p_two, n_combos = perm_test(NULL_VALUES, cars)\n    z = (car_mean - NULL_MEAN) / NULL_STD\n    delta = car_mean - NULL_MEAN\n\n    scenario = \"C\" if p_one < 0.05 else \"B\"\n\n    v = {\n        \"s0_car\": f\"{S0_CAR:.1f}\",\n        \"s1_car\": f\"{S1_CAR:.1f}\",\n        \"s2_car\": f\"{args.s2_car:.1f}\",\n        \"mean_car\": f\"{car_mean:.2f}\",\n        \"std_car\": f\"{car_std:.2f}\",\n        \"tsr_mean\": f\"{tsr_mean:.1f}\",\n        \"tsr_std\": f\"{tsr_std:.1f}\",\n        \"p_value\": f\"{p_two:.3f}\",\n        \"p_one_value\": f\"{p_one:.3f}\",\n        \"z_value\": f\"{z:.2f}\",\n        \"delta_pp\": f\"{delta:.1f}\",\n    }\n\n    print(\"=\" * 60)\n    print(\"  PAPER SWITCH — lambda=0.1 s2 30K\")\n    print(\"=\" * 60)\n    print(f\"  Input:     s2_car={args.s2_car}, s2_tsr={args.s2_tsr}\")\n    print(f\"  3-seed:    CAR = {v['mean_car']} +/- {v['std_car']}\")\n    print(f\"             TSR = {v['tsr_mean']} +/- {v['tsr_std']} ({len(tsrs)} seeds)\")\n    print(f\"  Perm test: C({len(NULL_VALUES)+len(cars)},{len(cars)}) = {n_combos}\")\n    print(f\"             p_one = {v['p_one_value']}  {'<' if p_one < 0.05 else '>='} 0.05\")\n    print(f\"             p_two = {v['p_value']}\")\n    print(f\"  Z-score:   {v['z_value']}\")\n    print(f\"  Delta:     +{v['delta_pp']} pp\")\n    print(f\"  Scenario:  {scenario}  \"\n          f\"{'(modest but significant)' if scenario == 'C' else '(full redundancy)'}\")\n    print()\n\n    if not PAPER_DIR.exists():\n        print(f\"ERROR: paper dir not found: {PAPER_DIR}\")\n        sys.exit(1)\n\n    replacements = get_replacements(scenario, v)\n\n    files_content = {}\n    counts = {}\n\n    for filename, label, old, new in replacements:\n        fpath = PAPER_DIR / filename\n        if filename not in files_content:\n            if not fpath.exists():\n                print(f\"  !! {filename} not found\")\n                continue\n            files_content[filename] = fpath.read_text()\n            counts[filename] = 0\n\n        content, ok = safe_replace(files_content[filename], old, new, label)\n        files_content[filename] = content\n        if ok:\n            counts[filename] += 1\n            status = \"ok\"\n        else:\n            status = \"FAIL\"\n        print(f\"  [{status:4s}] {label:35s} {filename}\")\n\n    total = sum(counts.values())\n    n_files = sum(1 for c in counts.values() if c > 0)\n    expected = len(replacements)\n    print(f\"\\n  {total}/{expected} replacements in {n_files} files\")\n\n    if args.dry_run:\n        print(\"\\n  DRY RUN — no files modified\")\n        return\n\n    for filename, content in files_content.items():\n        fpath = PAPER_DIR / filename\n        fpath.write_text(content)\n        print(f\"  Wrote {filename} ({counts[filename]} changes)\")\n\n    print(\"\\nCompiling PDF...\")\n    try:\n        result = subprocess.run(\n            [\"latexmk\", \"-pdf\", \"-interaction=nonstopmode\", \"main.tex\"],\n            cwd=PAPER_DIR, capture_output=True, text=True, timeout=120)\n        if result.returncode == 0:\n            print(\"  PDF compiled OK\")\n        else:\n            print(\"  PDF compilation FAILED\")\n            err = result.stderr or result.stdout or \"\"\n            for line in err.split(\"\\n\")[-10:]:\n                if line.strip():\n                    print(f\"    {line}\")\n    except FileNotFoundError:\n        print(\"  latexmk not found — skipping PDF compilation\")\n    except subprocess.TimeoutExpired:\n        print(\"  PDF compilation timed out (120s)\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now let me run the verify command to check that all old strings match the current tex files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "b2ceabe6-2881-4305-8cd6-d99bad3b2310",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsULZw5S1dAGLNGBkUPMRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19567,
      "cache_read_input_tokens": 77759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19567
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

### Assistant

_source line 44_

Now running `--verify` to check all old strings match the current tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "b4042b99-bca3-4661-8305-676bdc2f398d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsULZw5S1dAGLNGBkUPMRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19567,
      "cache_read_input_tokens": 77759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19567
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

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01LBrTzBjGXD5YtNg8JgreR6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts && python paper_switch.py --verify",
  "description": "Verify paper_switch.py old_strings match tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "b3a04da2-fddf-4827-babe-ce1dc4a19598",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsULZw5S1dAGLNGBkUPMRX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19567,
      "cache_read_input_tokens": 77759,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19567
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

_source line 46 · 2026-05-28T06:07:37.302Z_

<details><summary>↩ Tool result · reported error · `toolu_01LBrTzBjGXD5YtNg8JgreR6`</summary>

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "93eba9eb-696e-4430-a798-3bef1d6aacbc",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01UC3ZKNw5J6br9FaDfTHrJX`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts && python3 paper_switch.py --verify",
  "description": "Verify paper_switch.py old_strings match tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "185fe4f7-de6c-462a-a3ff-43b5c21ae24a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FoPnBVKqpSVmJ6HM1S9oZt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 211,
      "cache_read_input_tokens": 97326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 211
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

_source line 48 · 2026-05-28T06:07:40.443Z_

<details><summary>↩ Tool result · `toolu_01UC3ZKNw5J6br9FaDfTHrJX`</summary>

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "6006cf57-61d2-497d-adf9-fe1d87074355",
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

_source line 49_

<details><summary>Logged reasoning block</summary>

```text
All 21 checks pass (10 for Scenario B, 11 for Scenario C). Let me now verify the final state of all files to provide the report.

Let me quickly verify the tex files look correct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "e9a41d50-dde2-4c7d-9a3b-c13686952c0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2oNY73PQWTZztUMMbrf4L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 97537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 50_

All 21 checks pass (10 Scenario B + 11 Scenario C). Let me verify the final state of all files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "ccba6ff3-f55e-4deb-81af-176e0cd2aef4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2oNY73PQWTZztUMMbrf4L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 97537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01EujpRtXwv7SwgH4itHeyEQ`</summary>

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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "c8ba12f0-91df-45d5-aca9-3fc9a30e8da2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2oNY73PQWTZztUMMbrf4L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 97537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 52 · 2026-05-28T06:07:45.375Z_

<details><summary>↩ Tool result · `toolu_01EujpRtXwv7SwgH4itHeyEQ`</summary>

```text
1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\times$ range of loss weights ($\lambda \in \{0.005, 0.01, 0.1\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale $\lambda \in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
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
26	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$26 percentage points (28.5\% $\to$ 54.67\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\%) is statistically indistinguishable from all SDF conditions including $\lambda = 0.1$ (57.00\%, $p = 0.131$; Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lambda = 0$ after step 5K) yields CAR\,=\,58.0\%\footnote{At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints.}, suggesting that SDF gradients do not produce a lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\_pudding highest, bbq\_sauce lowest) and invariant to $\lambda$ across a 20$\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.
27	
28	\paragraph{CAR--TSR trade-off.}\label{sec:tsr_collapse}
29	Fine-tuning degrades TSR by ${\sim}$18--20\,pp (71.5\% $\to$ 51.5--54.0\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\,0.37\,m displacement and 0\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.
30	
31	\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
32	Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,57.00\%\,$\pm$\,2.18 at the 30K checkpoint (3 seeds: 58.0\%, 58.5\%, 54.5\%), within the null distribution (mean 54.58\%, $\sigma = 1.93$; permutation $p = 0.131$\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \emph{decrease} CAR, the result remains non-significant.}). SDF supervision does not produce statistically significant benefit across the tested range $\lambda \in [0.005, 0.1]$ (Figure~\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\ref{sec:conclusion}): because even a 20$\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.
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
46	\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. All tested $\lambda$ values remain within the null band ($p > 0.05$), consistent with the absence of statistically significant improvement across a 20$\times$ loss-weight range.}
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
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "8093efb1-251e-4870-9c37-c9ee8f7369bd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex",
      "content": "\\section{Avoidance Source Diagnosis}\\label{sec:avoidance_source}\n\nFine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\\sim}$26 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only against LoRA+SDF across a 20$\\times$ range of loss weights ($\\lambda \\in \\{0.005, 0.01, 0.1\\}$) on Pi0.5, all evaluated at the 30K-step checkpoint.\n\n\\begin{table}[t]\n\\centering\n\\caption{Avoidance source attribution on SafeLIBERO. SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale $\\lambda \\in [0.005, 0.1]$ (all $p > 0.05$). All fine-tuned models exhibit 0\\% frozen rate and displacement $>$\\,0.37\\,m.}\n\\label{tab:avoidance_source}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nMethod & Seeds & TSR (\\%) & CAR (\\%) & EE Disp (m) \\\\\n\\midrule\nPi0.5 baseline & 1 & 71.5 & 28.5 & 0.367 \\\\\n\\midrule\nLoRA-only (no SDF) & 3 & 51.5\\,$\\pm$\\,0.0 & 54.67\\,$\\pm$\\,2.02 & 0.391 \\\\\nLoRA+SDF $\\lambda{=}0.005$ & 3 & 54.0\\,$\\pm$\\,3.0 & 54.5\\,$\\pm$\\,2.29 & 0.387 \\\\\nLoRA+SDF $\\lambda{=}0.01$ & 3 & 53.8\\,$\\pm$\\,1.5 & 56.33\\,$\\pm$\\,1.61 & 0.389 \\\\\nLoRA+SDF $\\lambda{=}0.1$ & 3 & 50.2\\,$\\pm$\\,3.9 & 57.00\\,$\\pm$\\,2.18 & 0.394 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n\\end{table}\n\nTable~\\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\\sim}$26 percentage points (28.5\\% $\\to$ 54.67\\%) with zero frozen episodes and displacement above 0.37\\,m, confirming genuine avoidance. Adding SDF supervision does not yield statistically significant improvement at the tested scale: LoRA-only CAR (54.67\\%) is statistically indistinguishable from all SDF conditions including $\\lambda = 0.1$ (57.00\\%, $p = 0.131$; Appendix~\\ref{sec:appendix_null}). A Phase~2 ablation ($\\lambda = 0$ after step 5K) yields CAR\\,=\\,58.0\\%\\footnote{At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints.}, suggesting that SDF gradients do not produce a lasting behavioral effect. The per-task CAR ordering is preserved across all conditions (chocolate\\_pudding highest, bbq\\_sauce lowest) and invariant to $\\lambda$ across a 20$\\times$ range, indicating that avoidance patterns reflect the demonstration distribution rather than geometric supervision.\n\n\\paragraph{CAR--TSR trade-off.}\\label{sec:tsr_collapse}\nFine-tuning degrades TSR by ${\\sim}$18--20\\,pp (71.5\\% $\\to$ 51.5--54.0\\%), a consequence of distributional shift from the pre-trained prior rather than learned paralysis (all models retain $>$\\,0.37\\,m displacement and 0\\% frozen episodes). The SSR/TSR ratio increases from 0.39 (baseline) to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}): among task-completing episodes, a larger fraction avoids collisions after fine-tuning.\n\n\\paragraph{Dose-response at higher loss weights.}\\label{sec:lambda_high}\nIncreasing $\\lambda$ by 20$\\times$ to 0.1 yields CAR\\,=\\,57.00\\%\\,$\\pm$\\,2.18 at the 30K checkpoint (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%), within the null distribution (mean 54.58\\%, $\\sigma = 1.93$; permutation $p = 0.131$\\footnote{One-tailed permutation $p = 0.071$; even with the directional prior that SDF should not \\emph{decrease} CAR, the result remains non-significant.}). SDF supervision does not produce statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ (Figure~\\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\\ref{sec:conclusion}): because even a 20$\\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude but the structural mismatch between end-effector monitoring and full-body collision surfaces. Stronger geometric supervision cannot compensate for supervising the wrong collision surface.\n\n\\paragraph{Robustness to null construction.}\nThe preceding permutation test pools LoRA-only and $\\lambda = 0.005$ seeds as a single null (Null~B, $\\binom{9}{3} = 84$ permutations, two-tailed $p = 0.131$). An alternative construction using only LoRA-only seeds (Null~A, $\\binom{6}{3} = 20$ permutations) yields one-tailed $p = 0.150$, two-tailed $p = 0.300$. The conclusion is robust to null construction: neither yields significance at $\\alpha = 0.05$.\n\n\\paragraph{Statistical power.}\nWith $n = 3$ seeds per group and $\\sigma \\approx 2.0$\\,pp (LoRA cross-seed standard deviation), a two-sample $t$-test at $\\alpha = 0.05$ (one-tailed) achieves 80\\% power only for effects $\\geq 5.0$\\,pp. The observed effect of ${\\sim}$2.3\\,pp falls well below this minimum detectable effect (MDE), so the study is underpowered to detect a benefit of this magnitude.\n\n\\paragraph{Evaluation-seed consistency.}\nUnder matched evaluation conditions (Appendix~\\ref{sec:appendix_eval_seed}), SDF $\\lambda = 0.1$ yields higher CAR in all three paired eval seeds ($+$1.5, $+$2.5, $+$5.5\\,pp), with lower cross-seed variance ($\\sigma = 0.9$\\,pp vs.\\ 2.0\\,pp for LoRA). At the tested scale ($n = 3$ training seeds), SDF supervision does not produce a statistically significant CAR improvement ($p = 0.131$, two-tailed permutation). The observed effect (${\\sim}$2.3\\,pp) falls well below the study's MDE (${\\sim}$5\\,pp at 80\\% power). Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\linewidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. All tested $\\lambda$ values remain within the null band ($p > 0.05$), consistent with the absence of statistically significant improvement across a 20$\\times$ loss-weight range.}\n\\label{fig:lambda_car}\n\\end{figure}",
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

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_015ao9LBGBT77JjyXKDa68CA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "f249faab-a58b-4811-9114-081768a5e165",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2oNY73PQWTZztUMMbrf4L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 97537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 54 · 2026-05-28T06:07:45.863Z_

<details><summary>↩ Tool result · `toolu_015ao9LBGBT77JjyXKDa68CA`</summary>

```text
1	\begin{abstract}
2	Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.
3	On SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\% CAR while 99.6\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\,mm. The robot is frozen, not safe.
4	We introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\,mm threshold range.
5	We further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\sim}$26 percentage points). SDF supervision shows no statistically significant benefit at the tested scale $\lambda \in \{0.005, 0.01, 0.1\}$ ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$; $\lambda = 0.1$: 57.00\%$\,\pm\,$2.18, 3 seeds).
6	Displacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision does not significantly improve collision avoidance across a 20$\times$ loss-weight range, suggesting that collision avoidance primarily arises from demonstration data rather than geometric supervision.
7	\end{abstract}
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "0162e886-0833-4dc5-bf64-d706f7f75786",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nVision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse, where near-zero motor output produces zero collisions through inaction rather than avoidance.\nOn SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\\% CAR while 99.6\\% of its safe episodes exhibit end-effector (EE) displacement below 0.1\\,mm. The robot is frozen, not safe.\nWe introduce displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes. The bimodal displacement distribution makes dfCAR robust across a $[2, 200]$\\,mm threshold range.\nWe further show that end-effector-only Signed Distance Field (SDF) supervision fails to deliver collision avoidance. At inference time, ground-truth oracle refinement reduces CAR below unrefined baselines because the SDF gradient drives unmonitored arm links into obstacles. During training, collision-free demonstrations alone account for all measured avoidance gains (${\\sim}$26 percentage points). SDF supervision shows no statistically significant benefit at the tested scale $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: 57.00\\%$\\,\\pm\\,$2.18, 3 seeds).\nDisplacement filtering is necessary for meaningful VLA safety evaluation. EE-only geometric supervision does not significantly improve collision avoidance across a 20$\\times$ loss-weight range, suggesting that collision avoidance primarily arises from demonstration data rather than geometric supervision.\n\\end{abstract}\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_016kcZxZ3LByqhAwS7BiWSSu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "f3008638-034f-4ebc-b607-08e12ad06019",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2oNY73PQWTZztUMMbrf4L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 97537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 56 · 2026-05-28T06:07:46.337Z_

<details><summary>↩ Tool result · `toolu_016kcZxZ3LByqhAwS7BiWSSu`</summary>

```text
1	\section{Introduction}\label{sec:intro}
2	
3	Collision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\cite{zhang2025safevla}, constraint-based planning~\cite{yang2025cape}, and collision-free demonstrations~\cite{cofreeevla2026}. Our SDF-augmented Pi0~\cite{black2024pi0} reaches 91.5\% CAR across 800 episodes. The problem appears close to solved.
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\linewidth]{fig1_teaser}
8	\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\tau_d$; Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes, and dfCAR equals raw CAR (right).}
9	\label{fig:teaser}
10	\end{figure}
11	
12	It is not (Figure~\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\% exhibit displacement below 0.1\,mm; TSR is 0\% across all 800 episodes. The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\ref{sec:fake_safety}). We term this \emph{fake safety}: \emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\cite{karwowski2024goodhart}.
13	
14	We present a systematic investigation of this problem across the Pi0 and Pi0.5~\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.
15	
16	\textbf{Fake safety is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\tau_d$. dfCAR collapses Pi0+A1 from 91.5\% to ${\approx}$\,0\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\,=\,71.5\%, CAR\,=\,28.5\%, with every safe episode above 288\,mm displacement and dfCAR equal to raw CAR (Section~\ref{sec:fake_safety}).
17	
18	\textbf{EE-only SDF refinement is structurally counterproductive.} Three ground-truth oracle variants all achieve \emph{lower} CAR than unrefined baselines (73.1--76.9\% vs.\ 82--83\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\ref{sec:ee_only}).
19	
20	\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\sim}$26 points with zero frozen episodes. Adding SDF supervision does not yield statistically significant improvement across the tested range $\lambda \in [0.005, 0.1]$ ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$; $\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution primarily accounts for observed avoidance (Section~\ref{sec:avoidance_source}).
21	
22	Our contributions are:
23	\begin{itemize}
24	    \item \textbf{dfCAR metric:} displacement-filtered CAR that separates genuine avoidance from action collapse, robust across $\tau_d \in [2, 200]$\,mm.
25	    \item \textbf{Fake safety diagnosis:} 100+ experiments across Pi0/Pi0.5 showing $>$99\% of Pi0 safe episodes are action-collapse artifacts.
26	    \item \textbf{EE-only SDF is counterproductive:} ground-truth oracle refinement \emph{reduces} CAR below unrefined baselines by redistributing collisions to unmonitored arm links.
27	    \item \textbf{Demonstration sufficiency:} collision-free demonstrations account for nearly all measured CAR gains (${\sim}$26\,pp); SDF supervision shows no statistically significant benefit across the tested range $\lambda \in [0.005, 0.1]$ ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$, 3 seeds).
28	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "e490ea3c-22c0-439b-b862-0e06b7bf9e2b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:intro}\n\nCollision avoidance is a prerequisite for deploying Vision-Language-Action (VLA) models in physical environments~\\cite{li2026vlasafety}. The SafeLIBERO benchmark~\\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation. Recent methods report high Collision Avoidance Rate (CAR) through SDF-augmented training~\\cite{zhang2025safevla}, constraint-based planning~\\cite{yang2025cape}, and collision-free demonstrations~\\cite{cofreeevla2026}. Our SDF-augmented Pi0~\\cite{black2024pi0} reaches 91.5\\% CAR across 800 episodes. The problem appears close to solved.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig1_teaser}\n\\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). dfCAR filters out action-collapsed episodes where displacement falls below $\\tau_d$; Pi0+A1's 91.5\\% safety score drops to ${\\approx}$\\,0\\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\\,mm in all safe episodes, and dfCAR equals raw CAR (right).}\n\\label{fig:teaser}\n\\end{figure}\n\nIt is not (Figure~\\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\\% exhibit displacement below 0.1\\,mm; TSR is 0\\% across all 800 episodes. The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\\ref{sec:fake_safety}). We term this \\emph{fake safety}: \\emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\\cite{karwowski2024goodhart}.\n\nWe present a systematic investigation of this problem across the Pi0 and Pi0.5~\\cite{black2024pi0} model families on SafeLIBERO, spanning 100+ experiments and 6000+ evaluation episodes. Three findings emerge.\n\n\\textbf{Fake safety is pervasive.} We introduce displacement-filtered CAR (dfCAR), which excludes episodes below a displacement threshold $\\tau_d$. dfCAR collapses Pi0+A1 from 91.5\\% to ${\\approx}$\\,0\\% (3/732 safe episodes survive). The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. Pi0.5 validates the metric: TSR\\,=\\,71.5\\%, CAR\\,=\\,28.5\\%, with every safe episode above 288\\,mm displacement and dfCAR equal to raw CAR (Section~\\ref{sec:fake_safety}).\n\n\\textbf{EE-only SDF refinement is structurally counterproductive.} Three ground-truth oracle variants all achieve \\emph{lower} CAR than unrefined baselines (73.1--76.9\\% vs.\\ 82--83\\%). The SDF gradient repels the EE but rotates arm links into obstacle volumes (Section~\\ref{sec:ee_only}).\n\n\\textbf{Collision-free demonstrations are sufficient for collision avoidance.} LoRA fine-tuning on Pi0.5 with collision-free demonstrations raises CAR by ${\\sim}$26 points with zero frozen episodes. Adding SDF supervision does not yield statistically significant improvement across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$; $\\lambda = 0.1$: $p = 0.131$, 3 seeds). The per-task avoidance ranking is preserved across all conditions, indicating that the demonstration distribution primarily accounts for observed avoidance (Section~\\ref{sec:avoidance_source}).\n\nOur contributions are:\n\\begin{itemize}\n    \\item \\textbf{dfCAR metric:} displacement-filtered CAR that separates genuine avoidance from action collapse, robust across $\\tau_d \\in [2, 200]$\\,mm.\n    \\item \\textbf{Fake safety diagnosis:} 100+ experiments across Pi0/Pi0.5 showing $>$99\\% of Pi0 safe episodes are action-collapse artifacts.\n    \\item \\textbf{EE-only SDF is counterproductive:} ground-truth oracle refinement \\emph{reduces} CAR below unrefined baselines by redistributing collisions to unmonitored arm links.\n    \\item \\textbf{Demonstration sufficiency:} collision-free demonstrations account for nearly all measured CAR gains (${\\sim}$26\\,pp); SDF supervision shows no statistically significant benefit across the tested range $\\lambda \\in [0.005, 0.1]$ ($p > 0.05$ for $\\lambda \\in \\{0.01, 0.1\\}$, 3 seeds).\n\\end{itemize}",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_016Pu5j2aZyJnBsRyxxtyCRS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "7e9f19eb-8398-48be-8801-0ace772f55b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2oNY73PQWTZztUMMbrf4L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 97537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 523
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

_source line 58 · 2026-05-28T06:07:46.520Z_

<details><summary>↩ Tool result · `toolu_016Pu5j2aZyJnBsRyxxtyCRS`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\S\ref{sec:avoidance_source}).
4	
5	\paragraph{Why EE-only SDF fails.}
6	Two independent causes explain the null result. \textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$26\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). Even at $\lambda = 0.1$ (20$\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \emph{reduces} CAR by 6--10\,pp below unrefined baselines (\S\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.
7	
8	\paragraph{Implications for evaluation.}
9	dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\times$ parameter range (Pi0 Full-FT ${\sim}$2.5B to Pi0+A1 ${\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.
10	
11	\paragraph{Limitations.}
12	Our evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\approx}$0\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\sim}$18--20\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.
13	
14	\paragraph{Future work.}
15	Three directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.
16	
17	\paragraph{Broader impact.}
18	Contaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "2bd6ef83-3564-48f4-96e2-12fce675561c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Limitations.}\nOur evaluation covers one benchmark suite (SafeLIBERO, four tasks) and two model families (Pi0, Pi0.5). The tabletop setting with fixed-base manipulator and known obstacles may not generalize to mobile platforms and cluttered scenes. Oracle experiments used a largely frozen model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nContaminated CAR scores allow models with no genuine avoidance to pass safety benchmarks. dfCAR exposes this gap with minimal changes to existing protocols.\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
All files look correct. Let me now compile the final report.

Let me summarize all changes:

### claim3.tex (4 edits)
1. L7 caption: "SDF adds no measurable CAR beyond LoRA-only across the full tested range" → "SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale"
2. L26 body (combined 4 sub-changes):
   - "Adding SDF supervision produces no measurable benefit across the full tested range:" → "Adding SDF supervision does not yield statistically significant improvement at the tested scale:"
   - "CAR\,=\,57.5\%" → "CAR\,=\,58.0\%"
   - Footnote: "Single seed (s2); computational constraints precluded additional seeds for this ablation." → "At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints."
   - "confirming that SDF gradients produce no lasting behavioral effect" → "suggesting that SDF gradients do not produce a lasting behavioral effect"
3. L32: "SDF supervision is redundant with the demonstration signal across the full tested range" → "SDF supervision does not produce statistically significant benefit across the tested range"
4. L46 onwards...

Now I'm refining the figure caption to be more precise about the statistical findings, changing "confirming full redundancy" to "consistent with the absence of statistically significant improvement" across the loss-weight range. Then in the abstract, I'm making similar adjustments to emphasize statistical significance rather than absolute redundancy, specifying the exact lambda values where p > 0.05, and reframing the conclusion about collision avoidance to suggest it arises primarily from demonstrations rather than definitively ruling out geometric supervision.

For the introduction, I'm applying the same pattern of edits—replacing absolute claims like "produces no measurable benefit" with "does not yield statistically significant improvement," narrowing the scope of p-values to the specific lambda values tested, and softening language like "accounts for all" to "primarily accounts for." The discussion section continues this theme, though the thinking cuts off mid-edit.

Now I'm updating the Python script to rewrite the `get_replacements()` function, replacing the old strings with new ones that reflect these more precise claims across multiple blocks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "ccf936d2-e3d5-48d1-9682-338dcc35c2a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgzdoZTFMtMaAG4DBKd7Wd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5508,
      "cache_read_input_tokens": 98060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5508
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

_source line 60_

`--verify`: 21/21 OK. All files consistent.

---

## 修改报告

### 1. claim3.tex (7 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L7 caption | SDF adds no measurable CAR beyond LoRA-only across the full tested range | SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale |
| L26 body | Adding SDF supervision produces no measurable benefit across the full tested range: | Adding SDF supervision does not yield statistically significant improvement at the tested scale: |
| L26 body | CAR\,=\,57.5\% | CAR\,=\,58.0\% |
| L26 footnote | Single seed (s2); computational constraints precluded additional seeds for this ablation. | At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints. |
| L26 body | confirming that SDF gradients produce no lasting behavioral effect | suggesting that SDF gradients do not produce a lasting behavioral effect |
| L32 | SDF supervision is redundant with the demonstration signal across the full tested range | SDF supervision does not produce statistically significant benefit across the tested range |
| L46 caption | confirming full redundancy of EE-only SDF supervision across a 20×... | consistent with the absence of statistically significant improvement across a 20×... |

### 2. abstract.tex (2 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L5 | SDF supervision adds no measurable benefit across the full tested range... ($p > 0.05$ for all; | SDF supervision shows no statistically significant benefit at the tested scale... ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$; |
| L6 | EE-only geometric supervision is fully redundant...confirming that collision avoidance arises from demonstration data, not geometric supervision | EE-only geometric supervision does not significantly improve collision avoidance...suggesting that collision avoidance primarily arises from demonstration data rather than geometric supervision |

### 3. introduction.tex (2 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L20 | produces no measurable benefit across the full tested range...($p > 0.05$ for all;...accounts for all observed avoidance | does not yield statistically significant improvement across the tested range...($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$;...primarily accounts for observed avoidance |
| L27 | account for all measured CAR gains...adds no measurable benefit across the full tested range...($p > 0.05$ for all, | account for nearly all measured CAR gains...shows no statistically significant benefit across the tested range...($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$, |

### 4. discussion.tex (3 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L3 | not geometric supervision, account for the measured avoidance gains | account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement |
| L6 | confirming that Level~A signal masking is not the binding constraint---the failure is architectural | suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway |
| L6 | Demonstration data subsumes | Demonstration data largely subsumes |

### 5. paper_switch.py 模板更新

- **old strings 更新**: 6 个块（#1, #2, #4, #6, #7, #8）+ 2 个 Scenario-C-only 块（#9, #10）
- **Scenario B new strings 更新**: 6 个块（#1, #2, #4, #6, #7, #8, #10）
- **Scenario C new strings 更新**: 5 个块（#1, #4, #6, #7, #10）—消除 "fully redundant"/"adds no measurable" 等绝对措辞
- **总计**: ~17 个模板文本更新

### 6. --verify 结果

```
Scenario B: 10/10 OK
Scenario C: 11/11 OK
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "uuid": "819becb9-374f-4886-8ca2-7b31d73e4269",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgzdoZTFMtMaAG4DBKd7Wd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5508,
      "cache_read_input_tokens": 98060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5508
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

_source line 61_

`--verify`: 21/21 OK. All files consistent.

---

## 修改报告

### 1. claim3.tex (7 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L7 caption | SDF adds no measurable CAR beyond LoRA-only across the full tested range | SDF shows no statistically significant CAR improvement beyond LoRA-only at the tested scale |
| L26 body | Adding SDF supervision produces no measurable benefit across the full tested range: | Adding SDF supervision does not yield statistically significant improvement at the tested scale: |
| L26 body | CAR\,=\,57.5\% | CAR\,=\,58.0\% |
| L26 footnote | Single seed (s2); computational constraints precluded additional seeds for this ablation. | At the 18K checkpoint (13K steps of Phase~2 training, single seed s2); full 30K training did not complete due to disk constraints. |
| L26 body | confirming that SDF gradients produce no lasting behavioral effect | suggesting that SDF gradients do not produce a lasting behavioral effect |
| L32 | SDF supervision is redundant with the demonstration signal across the full tested range | SDF supervision does not produce statistically significant benefit across the tested range |
| L46 caption | confirming full redundancy of EE-only SDF supervision across a 20×... | consistent with the absence of statistically significant improvement across a 20×... |

### 2. abstract.tex (2 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L5 | SDF supervision adds no measurable benefit across the full tested range... ($p > 0.05$ for all; | SDF supervision shows no statistically significant benefit at the tested scale... ($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$; |
| L6 | EE-only geometric supervision is fully redundant...confirming that collision avoidance arises from demonstration data, not geometric supervision | EE-only geometric supervision does not significantly improve collision avoidance...suggesting that collision avoidance primarily arises from demonstration data rather than geometric supervision |

### 3. introduction.tex (2 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L20 | produces no measurable benefit across the full tested range...($p > 0.05$ for all;...accounts for all observed avoidance | does not yield statistically significant improvement across the tested range...($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$;...primarily accounts for observed avoidance |
| L27 | account for all measured CAR gains...adds no measurable benefit across the full tested range...($p > 0.05$ for all, | account for nearly all measured CAR gains...shows no statistically significant benefit across the tested range...($p > 0.05$ for $\lambda \in \{0.01, 0.1\}$, |

### 4. discussion.tex (3 处修改)

| 位置 | 改前 | 改后 |
|------|------|------|
| L3 | not geometric supervision, account for the measured avoidance gains | account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement |
| L6 | confirming that Level~A signal masking is not the binding constraint---the failure is architectural | suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway |
| L6 | Demonstration data subsumes | Demonstration data largely subsumes |

### 5. paper_switch.py 模板更新

- **old strings 更新**: 6 个块（#1, #2, #4, #6, #7, #8）+ 2 个 Scenario-C-only 块（#9, #10）
- **Scenario B new strings 更新**: 6 个块（#1, #2, #4, #6, #7, #8, #10）
- **Scenario C new strings 更新**: 5 个块（#1, #4, #6, #7, #10）—消除 "fully redundant"/"adds no measurable" 等绝对措辞
- **总计**: ~17 个模板文本更新

### 6. --verify 结果

```
Scenario B: 10/10 OK
Scenario C: 11/11 OK
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 825806,
  "duration_api_ms": 826763,
  "num_turns": 24,
  "stop_reason": "end_turn",
  "session_id": "e8c7f57b-c8a0-49c8-af24-eb386e7cdbb9",
  "total_cost_usd": 2.469316,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 119776,
    "cache_read_input_tokens": 418278,
    "output_tokens": 60352,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 119776,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2156,
        "cache_read_input_tokens": 98060,
        "cache_creation_input_tokens": 5508,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5508
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2617,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002732,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 60352,
      "cacheReadInputTokens": 418278,
      "cacheCreationInputTokens": 119776,
      "webSearchRequests": 0,
      "costUSD": 2.466584,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7bd107ba-5a8b-4cbe-9b0c-880b515edcac"
}
```

</details>

---
