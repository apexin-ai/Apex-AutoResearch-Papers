# analysis paper data consistency audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_analysis_paper-data-consistency-audit_20260519T220906.log`
- **Structured JSON:** [`c9c3584ece37ee52c748.json`](../../sessions/c9/c9c3584ece37ee52c748.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "ed6f8bab-5ff0-4478-abb6-86eb211667f3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1779237000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a53c404a-efe4-476f-8321-aa68b2247870",
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73"
}
```

---

### Assistant

_source line 4_

I'll start by reading the key files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "b0c0dced-0dc5-4ced-8645-b02e2feb1c32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SguD6WZ2qnJQfRrRVfQBiS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13490,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13490
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

<details open><summary>🔧 Tool call — Read · `toolu_01Rew3pWpg3vsqAphD3WyY5Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/profile_classifier.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "284bd972-93c3-4c4f-a3a4-c73de1fad049",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SguD6WZ2qnJQfRrRVfQBiS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13490,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13490
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

_source line 6 · 2026-05-19T22:09:22.113Z_

<details><summary>↩ Tool result · `toolu_01Rew3pWpg3vsqAphD3WyY5Q`</summary>

```text
1	"""Dose-response profile classifier for contamination calibration.
2	
3	Classifies a model's accuracy trajectory across contamination dosages
4	into one of five canonical patterns: Immune, U-collapse, V-recovery,
5	Benefit, or Benefit-saturation.
6	"""
7	
8	from __future__ import annotations
9	
10	DOSAGES = ("d000", "d005", "d025", "d050", "d100")
11	PATTERNS = ("Immune", "U-collapse", "V-recovery", "V-recovery-full", "Benefit", "Benefit-sat")
12	
13	
14	def classify_profile(
15	    accuracies: dict[str, float],
16	    *,
17	    noise_threshold: float = 1.0,
18	    severe_threshold: float = 5.0,
19	    saturation_ratio: float = 0.3,
20	    late_gain_floor: float = 0.5,
21	) -> dict:
22	    """Classify a dose-response accuracy profile into a canonical pattern.
23	
24	    Args:
25	        accuracies: Mapping from dosage key to accuracy (percentage points),
26	            e.g. {"d000": 76.44, "d005": 76.56, "d025": 76.50,
27	                   "d050": 76.02, "d100": 76.27}.
28	        noise_threshold: Maximum |delta| (pp) to be considered noise (Immune).
29	        severe_threshold: Minimum |delta| (pp) for severe degradation (U-collapse).
30	        saturation_ratio: If second-half gain < first-half gain * ratio,
31	            the benefit is saturating.
32	        late_gain_floor: If d100 - d050 < this value, late gain has stalled.
33	
34	    Returns:
35	        {"pattern": str, "confidence": float, "delta": float, "reasoning": str}
36	    """
37	    for d in DOSAGES:
38	        if d not in accuracies:
39	            raise ValueError(f"Missing dosage key: {d}")
40	
41	    a = {d: float(accuracies[d]) for d in DOSAGES}
42	    delta = a["d100"] - a["d000"]
43	    mid_vals = [a["d005"], a["d025"], a["d050"]]
44	    mid_min = min(mid_vals)
45	
46	    # ── Decision tree ────────────────────────────────────────────────
47	
48	    if abs(delta) <= noise_threshold:
49	        max_deviation = max(abs(v - a["d000"]) for v in mid_vals)
50	        if max_deviation <= noise_threshold:
51	            margin = noise_threshold - abs(delta)
52	            return _result(
53	                "Immune", delta, margin, noise_threshold,
54	                f"|delta|={abs(delta):.2f}pp <= {noise_threshold}pp noise band, "
55	                f"max_dev={max_deviation:.2f}pp <= {noise_threshold}pp"
56	            )
57	        v_dip = mid_min < a["d000"] and mid_min < a["d100"]
58	        if v_dip:
59	            recovery = a["d100"] - mid_min
60	            margin = max_deviation - noise_threshold
61	            return _result(
62	                "V-recovery-full", delta, margin, noise_threshold,
63	                f"|delta|={abs(delta):.2f}pp within noise but "
64	                f"max_dev={max_deviation:.2f}pp > {noise_threshold}pp; "
65	                f"V-dip to {mid_min:.2f}% with full recovery (+{recovery:.2f}pp)"
66	            )
67	        margin = noise_threshold - abs(delta)
68	        return _result(
69	            "Immune", delta, margin, noise_threshold,
70	            f"|delta|={abs(delta):.2f}pp within noise, "
71	            f"mid-trajectory volatility={max_deviation:.2f}pp (non-V-shaped)"
72	        )
73	
74	    if delta < -noise_threshold:
75	        if delta <= -severe_threshold:
76	            margin = abs(delta) - severe_threshold
77	            return _result(
78	                "U-collapse", delta, margin, severe_threshold,
79	                f"delta={delta:+.2f}pp <= -{severe_threshold}pp (severe monotonic decline)"
80	            )
81	
82	        v_dip = mid_min < a["d100"] and mid_min < a["d000"]
83	        if v_dip:
84	            recovery = a["d100"] - mid_min
85	            margin = min(a["d000"] - mid_min, a["d100"] - mid_min)
86	            return _result(
87	                "V-recovery", delta, margin, severe_threshold,
88	                f"delta={delta:+.2f}pp, mid-dosage trough at {mid_min:.2f}% "
89	                f"with {recovery:+.2f}pp partial recovery"
90	            )
91	
92	        margin = abs(delta) - noise_threshold
93	        return _result(
94	            "U-collapse", delta, margin, severe_threshold,
95	            f"delta={delta:+.2f}pp, moderate decline without V-shaped recovery"
96	        )
97	
98	    # delta > noise_threshold (positive)
99	    first_half = a["d025"] - a["d000"]
100	    second_half = a["d100"] - a["d025"]
101	    late_gain = a["d100"] - a["d050"]
102	
103	    saturating = (
104	        (first_half > 0 and second_half < first_half * saturation_ratio)
105	        or late_gain < late_gain_floor
106	    )
107	
108	    if saturating:
109	        if late_gain < late_gain_floor:
110	            margin = late_gain_floor - late_gain
111	            reason = (f"delta={delta:+.2f}pp (positive), late gain "
112	                      f"d050->d100={late_gain:+.2f}pp < {late_gain_floor}pp floor")
113	        else:
114	            margin = first_half * saturation_ratio - second_half
115	            reason = (f"delta={delta:+.2f}pp (positive), second-half gain "
116	                      f"({second_half:.2f}) < {saturation_ratio:.0%} of "
117	                      f"first-half ({first_half:.2f})")
118	        return _result("Benefit-sat", delta, margin, noise_threshold, reason)
119	
120	    margin = delta - noise_threshold
121	    return _result(
122	        "Benefit", delta, margin, noise_threshold,
123	        f"delta={delta:+.2f}pp, monotonic improvement without saturation"
124	    )
125	
126	
127	def _result(
128	    pattern: str, delta: float, margin: float, scale: float, reasoning: str
129	) -> dict:
130	    confidence = min(1.0, 0.5 + 0.5 * margin / scale)
131	    return {
132	        "pattern": pattern,
133	        "confidence": round(confidence, 3),
134	        "delta": round(delta, 4),
135	        "reasoning": reasoning,
136	    }
137	
138	
139	def classify_profiles_batch(
140	    profiles: dict[str, dict[str, float]], **kwargs
141	) -> dict[str, dict]:
142	    """Classify multiple profiles. Keys are model names."""
143	    return {name: classify_profile(accs, **kwargs) for name, accs in profiles.items()}
144	
145	
146	# ── CLI validation ───────────────────────────────────────────────────
147	
148	if __name__ == "__main__":
149	    test_cases = {
150	        "Phi-4 s42 (expect Immune)": {
151	            "accs": {"d000": 76.44, "d005": 76.28, "d025": 76.50,
152	                     "d050": 76.10, "d100": 76.27},
153	            "expected": "Immune",
154	        },
155	        "Qwen-14B s42 (expect U-collapse)": {
156	            "accs": {"d000": 69.44, "d005": 63.76, "d025": 62.51,
157	                     "d050": 61.34, "d100": 60.07},
158	            "expected": "U-collapse",
159	        },
160	        "Qwen-7B s42 (expect V-recovery)": {
161	            "accs": {"d000": 66.11, "d005": 63.42, "d025": 63.15,
162	                     "d050": 63.59, "d100": 64.33},
163	            "expected": "V-recovery",
164	        },
165	        "Gemma-2 s42 (expect Benefit)": {
166	            "accs": {"d000": 61.86, "d005": 63.56, "d025": 64.19,
167	                     "d050": 64.73, "d100": 65.62},
168	            "expected": "Benefit",
169	        },
170	        "OLMo-2 s42 (expect Benefit-sat)": {
171	            "accs": {"d000": 53.79, "d005": 55.17, "d025": 56.06,
172	                     "d050": 56.53, "d100": 57.00},
173	            "expected": "Benefit-sat",
174	        },
175	        "Qwen-7B s123 (expect V-recovery-full)": {
176	            "accs": {"d000": 66.59, "d005": 63.37, "d025": 64.82,
177	                     "d050": 65.00, "d100": 66.59},
178	            "expected": "V-recovery-full",
179	        },
180	    }
181	
182	    all_pass = True
183	    for name, tc in test_cases.items():
184	        result = classify_profile(tc["accs"])
185	        ok = result["pattern"] == tc["expected"]
186	        mark = "PASS" if ok else "FAIL"
187	        print(f"[{mark}] {name}")
188	        print(f"       -> {result['pattern']}  (conf={result['confidence']:.3f})")
189	        print(f"       {result['reasoning']}")
190	        if not ok:
191	            all_pass = False
192	
193	    print(f"\n{'All tests passed.' if all_pass else 'SOME TESTS FAILED.'}")
194	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "088f9f8c-3fe8-44c7-b76a-e7fc303dcb34",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/profile_classifier.py",
      "content": "\"\"\"Dose-response profile classifier for contamination calibration.\n\nClassifies a model's accuracy trajectory across contamination dosages\ninto one of five canonical patterns: Immune, U-collapse, V-recovery,\nBenefit, or Benefit-saturation.\n\"\"\"\n\nfrom __future__ import annotations\n\nDOSAGES = (\"d000\", \"d005\", \"d025\", \"d050\", \"d100\")\nPATTERNS = (\"Immune\", \"U-collapse\", \"V-recovery\", \"V-recovery-full\", \"Benefit\", \"Benefit-sat\")\n\n\ndef classify_profile(\n    accuracies: dict[str, float],\n    *,\n    noise_threshold: float = 1.0,\n    severe_threshold: float = 5.0,\n    saturation_ratio: float = 0.3,\n    late_gain_floor: float = 0.5,\n) -> dict:\n    \"\"\"Classify a dose-response accuracy profile into a canonical pattern.\n\n    Args:\n        accuracies: Mapping from dosage key to accuracy (percentage points),\n            e.g. {\"d000\": 76.44, \"d005\": 76.56, \"d025\": 76.50,\n                   \"d050\": 76.02, \"d100\": 76.27}.\n        noise_threshold: Maximum |delta| (pp) to be considered noise (Immune).\n        severe_threshold: Minimum |delta| (pp) for severe degradation (U-collapse).\n        saturation_ratio: If second-half gain < first-half gain * ratio,\n            the benefit is saturating.\n        late_gain_floor: If d100 - d050 < this value, late gain has stalled.\n\n    Returns:\n        {\"pattern\": str, \"confidence\": float, \"delta\": float, \"reasoning\": str}\n    \"\"\"\n    for d in DOSAGES:\n        if d not in accuracies:\n            raise ValueError(f\"Missing dosage key: {d}\")\n\n    a = {d: float(accuracies[d]) for d in DOSAGES}\n    delta = a[\"d100\"] - a[\"d000\"]\n    mid_vals = [a[\"d005\"], a[\"d025\"], a[\"d050\"]]\n    mid_min = min(mid_vals)\n\n    # ── Decision tree ────────────────────────────────────────────────\n\n    if abs(delta) <= noise_threshold:\n        max_deviation = max(abs(v - a[\"d000\"]) for v in mid_vals)\n        if max_deviation <= noise_threshold:\n            margin = noise_threshold - abs(delta)\n            return _result(\n                \"Immune\", delta, margin, noise_threshold,\n                f\"|delta|={abs(delta):.2f}pp <= {noise_threshold}pp noise band, \"\n                f\"max_dev={max_deviation:.2f}pp <= {noise_threshold}pp\"\n            )\n        v_dip = mid_min < a[\"d000\"] and mid_min < a[\"d100\"]\n        if v_dip:\n            recovery = a[\"d100\"] - mid_min\n            margin = max_deviation - noise_threshold\n            return _result(\n                \"V-recovery-full\", delta, margin, noise_threshold,\n                f\"|delta|={abs(delta):.2f}pp within noise but \"\n                f\"max_dev={max_deviation:.2f}pp > {noise_threshold}pp; \"\n                f\"V-dip to {mid_min:.2f}% with full recovery (+{recovery:.2f}pp)\"\n            )\n        margin = noise_threshold - abs(delta)\n        return _result(\n            \"Immune\", delta, margin, noise_threshold,\n            f\"|delta|={abs(delta):.2f}pp within noise, \"\n            f\"mid-trajectory volatility={max_deviation:.2f}pp (non-V-shaped)\"\n        )\n\n    if delta < -noise_threshold:\n        if delta <= -severe_threshold:\n            margin = abs(delta) - severe_threshold\n            return _result(\n                \"U-collapse\", delta, margin, severe_threshold,\n                f\"delta={delta:+.2f}pp <= -{severe_threshold}pp (severe monotonic decline)\"\n            )\n\n        v_dip = mid_min < a[\"d100\"] and mid_min < a[\"d000\"]\n        if v_dip:\n            recovery = a[\"d100\"] - mid_min\n            margin = min(a[\"d000\"] - mid_min, a[\"d100\"] - mid_min)\n            return _result(\n                \"V-recovery\", delta, margin, severe_threshold,\n                f\"delta={delta:+.2f}pp, mid-dosage trough at {mid_min:.2f}% \"\n                f\"with {recovery:+.2f}pp partial recovery\"\n            )\n\n        margin = abs(delta) - noise_threshold\n        return _result(\n            \"U-collapse\", delta, margin, severe_threshold,\n            f\"delta={delta:+.2f}pp, moderate decline without V-shaped recovery\"\n        )\n\n    # delta > noise_threshold (positive)\n    first_half = a[\"d025\"] - a[\"d000\"]\n    second_half = a[\"d100\"] - a[\"d025\"]\n    late_gain = a[\"d100\"] - a[\"d050\"]\n\n    saturating = (\n        (first_half > 0 and second_half < first_half * saturation_ratio)\n        or late_gain < late_gain_floor\n    )\n\n    if saturating:\n        if late_gain < late_gain_floor:\n            margin = late_gain_floor - late_gain\n            reason = (f\"delta={delta:+.2f}pp (positive), late gain \"\n                      f\"d050->d100={late_gain:+.2f}pp < {late_gain_floor}pp floor\")\n        else:\n            margin = first_half * saturation_ratio - second_half\n            reason = (f\"delta={delta:+.2f}pp (positive), second-half gain \"\n                      f\"({second_half:.2f}) < {saturation_ratio:.0%} of \"\n                      f\"first-half ({first_half:.2f})\")\n        return _result(\"Benefit-sat\", delta, margin, noise_threshold, reason)\n\n    margin = delta - noise_threshold\n    return _result(\n        \"Benefit\", delta, margin, noise_threshold,\n        f\"delta={delta:+.2f}pp, monotonic improvement without saturation\"\n    )\n\n\ndef _result(\n    pattern: str, delta: float, margin: float, scale: float, reasoning: str\n) -> dict:\n    confidence = min(1.0, 0.5 + 0.5 * margin / scale)\n    return {\n        \"pattern\": pattern,\n        \"confidence\": round(confidence, 3),\n        \"delta\": round(delta, 4),\n        \"reasoning\": reasoning,\n    }\n\n\ndef classify_profiles_batch(\n    profiles: dict[str, dict[str, float]], **kwargs\n) -> dict[str, dict]:\n    \"\"\"Classify multiple profiles. Keys are model names.\"\"\"\n    return {name: classify_profile(accs, **kwargs) for name, accs in profiles.items()}\n\n\n# ── CLI validation ───────────────────────────────────────────────────\n\nif __name__ == \"__main__\":\n    test_cases = {\n        \"Phi-4 s42 (expect Immune)\": {\n            \"accs\": {\"d000\": 76.44, \"d005\": 76.28, \"d025\": 76.50,\n                     \"d050\": 76.10, \"d100\": 76.27},\n            \"expected\": \"Immune\",\n        },\n        \"Qwen-14B s42 (expect U-collapse)\": {\n            \"accs\": {\"d000\": 69.44, \"d005\": 63.76, \"d025\": 62.51,\n                     \"d050\": 61.34, \"d100\": 60.07},\n            \"expected\": \"U-collapse\",\n        },\n        \"Qwen-7B s42 (expect V-recovery)\": {\n            \"accs\": {\"d000\": 66.11, \"d005\": 63.42, \"d025\": 63.15,\n                     \"d050\": 63.59, \"d100\": 64.33},\n            \"expected\": \"V-recovery\",\n        },\n        \"Gemma-2 s42 (expect Benefit)\": {\n            \"accs\": {\"d000\": 61.86, \"d005\": 63.56, \"d025\": 64.19,\n                     \"d050\": 64.73, \"d100\": 65.62},\n            \"expected\": \"Benefit\",\n        },\n        \"OLMo-2 s42 (expect Benefit-sat)\": {\n            \"accs\": {\"d000\": 53.79, \"d005\": 55.17, \"d025\": 56.06,\n                     \"d050\": 56.53, \"d100\": 57.00},\n            \"expected\": \"Benefit-sat\",\n        },\n        \"Qwen-7B s123 (expect V-recovery-full)\": {\n            \"accs\": {\"d000\": 66.59, \"d005\": 63.37, \"d025\": 64.82,\n                     \"d050\": 65.00, \"d100\": 66.59},\n            \"expected\": \"V-recovery-full\",\n        },\n    }\n\n    all_pass = True\n    for name, tc in test_cases.items():\n        result = classify_profile(tc[\"accs\"])\n        ok = result[\"pattern\"] == tc[\"expected\"]\n        mark = \"PASS\" if ok else \"FAIL\"\n        print(f\"[{mark}] {name}\")\n        print(f\"       -> {result['pattern']}  (conf={result['confidence']:.3f})\")\n        print(f\"       {result['reasoning']}\")\n        if not ok:\n            all_pass = False\n\n    print(f\"\\n{'All tests passed.' if all_pass else 'SOME TESTS FAILED.'}\")\n",
      "numLines": 194,
      "startLine": 1,
      "totalLines": 194
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01YDUQUQ6eWdsyPZU8SNMmbN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/algorithm1_pseudocode.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "fb2a7ad3-276d-4f68-842a-eae78a5e24e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SguD6WZ2qnJQfRrRVfQBiS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13490,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13490
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

_source line 8 · 2026-05-19T22:09:22.479Z_

<details><summary>↩ Tool result · `toolu_01YDUQUQ6eWdsyPZU8SNMmbN`</summary>

```text
1	% Algorithm 1: Dose-Response Profile Classification
2	% Usage: \input{algorithm1_pseudocode.tex}
3	% Requires: \usepackage{algorithm,algorithmic} or algpseudocode
4	
5	\begin{algorithm}[t]
6	\caption{Dose-Response Profile Classification}
7	\label{alg:profile-classification}
8	\begin{algorithmic}[1]
9	\REQUIRE Accuracy vector $\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \in \{0, 5, 25, 50, 100\}\%$
10	\REQUIRE Noise threshold $\tau = 1$ pp, severity threshold $\sigma = 5$ pp
11	\REQUIRE Saturation ratio $\rho = 0.3$, late-gain floor $\lambda = 0.5$ pp
12	\ENSURE Pattern $p \in \{\textsc{Immune}, \textsc{U-collapse}, \textsc{V-recovery}, \textsc{V-recovery-full}, \textsc{Benefit}, \textsc{Benefit-sat}\}$
13	\STATE $\Delta \gets a_{100} - a_{0}$ \COMMENT{end-to-end accuracy shift}
14	\STATE $m^* \gets \min(a_{5},\, a_{25},\, a_{50})$ \COMMENT{mid-dosage minimum}
15	\STATE $v^* \gets \max_{i \in \{5,25,50\}} |a_i - a_0|$ \COMMENT{max mid-trajectory deviation}
16	\IF{$|\Delta| \le \tau$}
17	    \IF{$v^* \le \tau$}
18	        \RETURN \textsc{Immune} \COMMENT{fluctuation within noise band}
19	    \ELSIF{$m^* < a_0$ \AND $m^* < a_{100}$}
20	        \RETURN \textsc{V-recovery-full} \COMMENT{V-dip with full endpoint recovery}
21	    \ELSE
22	        \RETURN \textsc{Immune} \COMMENT{non-V volatility, endpoint stable}
23	    \ENDIF
24	\ELSIF{$\Delta < -\tau$}
25	    \IF{$\Delta \le -\sigma$}
26	        \RETURN \textsc{U-collapse} \COMMENT{severe monotonic degradation}
27	    \ELSIF{$m^* < a_{0}$ \AND $m^* < a_{100}$}
28	        \RETURN \textsc{V-recovery} \COMMENT{mid-dosage trough with partial recovery}
29	    \ELSE
30	        \RETURN \textsc{U-collapse} \COMMENT{moderate decline, no V-shape}
31	    \ENDIF
32	\ELSE \COMMENT{$\Delta > \tau$}
33	    \STATE $g_1 \gets a_{25} - a_{0}$ \COMMENT{first-half gain}
34	    \STATE $g_2 \gets a_{100} - a_{25}$ \COMMENT{second-half gain}
35	    \STATE $\ell \gets a_{100} - a_{50}$ \COMMENT{late gain}
36	    \IF{$(g_1 > 0 \;\AND\; g_2 < \rho \cdot g_1)$ \OR $\ell < \lambda$}
37	        \RETURN \textsc{Benefit-sat} \COMMENT{gain decelerates at high dosage}
38	    \ELSE
39	        \RETURN \textsc{Benefit} \COMMENT{sustained improvement}
40	    \ENDIF
41	\ENDIF
42	\end{algorithmic}
43	\end{algorithm}
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "786b56cd-a4f6-4892-ba9c-4fed9e702a72",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/algorithm1_pseudocode.tex",
      "content": "% Algorithm 1: Dose-Response Profile Classification\n% Usage: \\input{algorithm1_pseudocode.tex}\n% Requires: \\usepackage{algorithm,algorithmic} or algpseudocode\n\n\\begin{algorithm}[t]\n\\caption{Dose-Response Profile Classification}\n\\label{alg:profile-classification}\n\\begin{algorithmic}[1]\n\\REQUIRE Accuracy vector $\\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \\in \\{0, 5, 25, 50, 100\\}\\%$\n\\REQUIRE Noise threshold $\\tau = 1$ pp, severity threshold $\\sigma = 5$ pp\n\\REQUIRE Saturation ratio $\\rho = 0.3$, late-gain floor $\\lambda = 0.5$ pp\n\\ENSURE Pattern $p \\in \\{\\textsc{Immune}, \\textsc{U-collapse}, \\textsc{V-recovery}, \\textsc{V-recovery-full}, \\textsc{Benefit}, \\textsc{Benefit-sat}\\}$\n\\STATE $\\Delta \\gets a_{100} - a_{0}$ \\COMMENT{end-to-end accuracy shift}\n\\STATE $m^* \\gets \\min(a_{5},\\, a_{25},\\, a_{50})$ \\COMMENT{mid-dosage minimum}\n\\STATE $v^* \\gets \\max_{i \\in \\{5,25,50\\}} |a_i - a_0|$ \\COMMENT{max mid-trajectory deviation}\n\\IF{$|\\Delta| \\le \\tau$}\n    \\IF{$v^* \\le \\tau$}\n        \\RETURN \\textsc{Immune} \\COMMENT{fluctuation within noise band}\n    \\ELSIF{$m^* < a_0$ \\AND $m^* < a_{100}$}\n        \\RETURN \\textsc{V-recovery-full} \\COMMENT{V-dip with full endpoint recovery}\n    \\ELSE\n        \\RETURN \\textsc{Immune} \\COMMENT{non-V volatility, endpoint stable}\n    \\ENDIF\n\\ELSIF{$\\Delta < -\\tau$}\n    \\IF{$\\Delta \\le -\\sigma$}\n        \\RETURN \\textsc{U-collapse} \\COMMENT{severe monotonic degradation}\n    \\ELSIF{$m^* < a_{0}$ \\AND $m^* < a_{100}$}\n        \\RETURN \\textsc{V-recovery} \\COMMENT{mid-dosage trough with partial recovery}\n    \\ELSE\n        \\RETURN \\textsc{U-collapse} \\COMMENT{moderate decline, no V-shape}\n    \\ENDIF\n\\ELSE \\COMMENT{$\\Delta > \\tau$}\n    \\STATE $g_1 \\gets a_{25} - a_{0}$ \\COMMENT{first-half gain}\n    \\STATE $g_2 \\gets a_{100} - a_{25}$ \\COMMENT{second-half gain}\n    \\STATE $\\ell \\gets a_{100} - a_{50}$ \\COMMENT{late gain}\n    \\IF{$(g_1 > 0 \\;\\AND\\; g_2 < \\rho \\cdot g_1)$ \\OR $\\ell < \\lambda$}\n        \\RETURN \\textsc{Benefit-sat} \\COMMENT{gain decelerates at high dosage}\n    \\ELSE\n        \\RETURN \\textsc{Benefit} \\COMMENT{sustained improvement}\n    \\ENDIF\n\\ENDIF\n\\end{algorithmic}\n\\end{algorithm}\n",
      "numLines": 44,
      "startLine": 1,
      "totalLines": 44
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01RZVhiZHhnyH7kQMEfKEaPT`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "534ddd6c-659f-4f41-aff0-0080b45d03c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SguD6WZ2qnJQfRrRVfQBiS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13490,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13490
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

_source line 10 · 2026-05-19T22:09:22.544Z_

<details><summary>↩ Tool result · `toolu_01RZVhiZHhnyH7kQMEfKEaPT`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "aa7ef1e8-8720-4367-a6c2-3eddb3f286c2",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 15,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
The paper directory at the expected path has no .tex files. Let me search more broadly for the paper files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "75936573-d24c-43ff-b8b1-fde573856992",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VB2vWdyFP5V55DPzJFbSyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4216,
      "cache_read_input_tokens": 25331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4216
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

_source line 12_

Paper .tex files not found at expected path. Let me search more broadly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "5cccd70b-384f-4f2f-a629-bf165896e414",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VB2vWdyFP5V55DPzJFbSyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4216,
      "cache_read_input_tokens": 25331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4216
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

<details open><summary>🔧 Tool call — Glob · `toolu_01X6S9CnQBbPpHF5hX16iuv6`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "42f2cf70-d63b-43f3-9d31-0763fa5d81ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VB2vWdyFP5V55DPzJFbSyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4216,
      "cache_read_input_tokens": 25331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4216
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

_source line 14 · 2026-05-19T22:09:27.355Z_

<details><summary>↩ Tool result · `toolu_01X6S9CnQBbPpHF5hX16iuv6`</summary>

```text
artifacts/dream_reports/dream_20260513T155040/best/paper.tex
artifacts/dream_reports/dream_20260513T155040/median/paper.tex
artifacts/dream_reports/dream_20260513T155040/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/dream_reports/dream_20260513T171200/best/paper.tex
artifacts/dream_reports/dream_20260513T171200/median/paper.tex
artifacts/dream_reports/dream_20260513T171200/worst/paper.tex
artifacts/_project/paper/fisher_info_appendix.tex
artifacts/fisher_info_derivation/fisher_info_appendix.tex
artifacts/dream_reports/dream_20260514T171536/best/paper.tex
artifacts/dream_reports/dream_20260514T171536/median/paper.tex
artifacts/dream_reports/dream_20260514T171536/worst/paper.tex
artifacts/dream_reports/dream_20260514T185145/best/paper.tex
artifacts/dream_reports/dream_20260514T185145/median/paper.tex
artifacts/dream_reports/dream_20260514T185145/worst/paper.tex
artifacts/dream_reports/dream_20260515T052337/best/paper.tex
artifacts/dream_reports/dream_20260515T052337/median/paper.tex
artifacts/dream_reports/dream_20260515T052337/worst/paper.tex
artifacts/dream_reports/dream_20260516T104822/best/paper.tex
artifacts/dream_reports/dream_20260516T104822/median/paper.tex
artifacts/dream_reports/dream_20260516T104822/worst/paper.tex
artifacts/dream_reports/dream_20260516T155748/best/paper.tex
artifacts/dream_reports/dream_20260516T155748/median/paper.tex
artifacts/dream_reports/dream_20260516T155748/worst/paper.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/related_work_04a735.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/abstract.tex
artifacts/paper_draft/experiments.tex
artifacts/_project/paper/introduction.tex
artifacts/paper_draft/abstract.tex
artifacts/paper_draft/conclusion.tex
artifacts/paper_draft/discussion.tex
artifacts/paper_draft/introduction.tex
artifacts/paper_draft/main.tex
artifacts/paper_draft/method.tex
artifacts/paper_draft/related_work.tex
artifacts/paper_draft/results.tex
artifacts/paper_draft/experimental_setup.tex
docs/paper/ethics.tex
docs/paper/related_work.tex
docs/paper/experimental_setup.tex
docs/paper/abstract.tex
artifacts/_project/paper/algorithm1_pseudocode.tex
artifacts/_project/paper/algorithm1_pseudocode_c1bd81.tex
docs/paper/introduction.tex
artifacts/algorithm1_pseudocode.tex
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/limitations.tex
docs/paper/appendix.tex
docs/paper/results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "016985cf-547b-439f-92cf-5f2719495a1d",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260513T155040/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T155040/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T155040/worst/paper.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/dream_reports/dream_20260513T171200/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T171200/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T171200/worst/paper.tex",
      "artifacts/_project/paper/fisher_info_appendix.tex",
      "artifacts/fisher_info_derivation/fisher_info_appendix.tex",
      "artifacts/dream_reports/dream_20260514T171536/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T171536/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T171536/worst/paper.tex",
      "artifacts/dream_reports/dream_20260514T185145/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T185145/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T185145/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T052337/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T052337/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T052337/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T104822/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T104822/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T104822/worst/paper.tex",
      "artifacts/dream_reports/dream_20260516T155748/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T155748/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T155748/worst/paper.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/related_work_04a735.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/paper_draft/experiments.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/paper_draft/abstract.tex",
      "artifacts/paper_draft/conclusion.tex",
      "artifacts/paper_draft/discussion.tex",
      "artifacts/paper_draft/introduction.tex",
      "artifacts/paper_draft/main.tex",
      "artifacts/paper_draft/method.tex",
      "artifacts/paper_draft/related_work.tex",
      "artifacts/paper_draft/results.tex",
      "artifacts/paper_draft/experimental_setup.tex",
      "docs/paper/ethics.tex",
      "docs/paper/related_work.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/abstract.tex",
      "artifacts/_project/paper/algorithm1_pseudocode.tex",
      "artifacts/_project/paper/algorithm1_pseudocode_c1bd81.tex",
      "docs/paper/introduction.tex",
      "artifacts/algorithm1_pseudocode.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/main.tex",
      "docs/paper/method.tex",
      "docs/paper/limitations.tex",
      "docs/paper/appendix.tex",
      "docs/paper/results.tex"
    ],
    "durationMs": 58,
    "numFiles": 53,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01VZg5XVmouPxVq9E6D2jzKe`</summary>

```json
{
  "pattern": "**/paper/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "51b55427-a1e1-4b6b-a73f-0e3ec6c1507f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VB2vWdyFP5V55DPzJFbSyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4216,
      "cache_read_input_tokens": 25331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4216
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

_source line 16 · 2026-05-19T22:09:27.651Z_

<details><summary>↩ Tool result · `toolu_01VZg5XVmouPxVq9E6D2jzKe`</summary>

```text
artifacts/_project/paper/main.pdf
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/fisher_info_appendix.tex
artifacts/_project/paper/results_tables.md
paper/sections/method.md
artifacts/_project/paper/method.md
figures/paper/gen_fig_domain_gamma.py
figures/paper/fig_domain_gamma.pdf
figures/paper/fig_domain_gamma.png
figures/paper/gen_fig_dose_response.py
figures/paper/fig_dose_response.png
figures/paper/gen_fig_signal_heatmap.py
figures/paper/fig_signal_heatmap.pdf
figures/paper/fig_signal_heatmap.png
figures/paper/gen_fig_pipeline.py
figures/paper/fig_pipeline.pdf
figures/paper/fig_pipeline.png
paper/sections/discussion.md
artifacts/_project/paper/discussion.md
paper/sections/experimental_setup.md
artifacts/_project/paper/experimental_setup.md
figures/paper/gen_fig_calibration.py
figures/paper/fig_calibration.pdf
figures/paper/fig_calibration.png
figures/paper/fig_identifiability_heatmap.pdf
artifacts/_project/paper/results.tex
artifacts/_project/paper/related_work_04a735.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/references.bib
docs/paper/acl.sty
docs/paper/acl_natbib.bst
docs/paper/figures/fig_signal_heatmap.pdf
docs/paper/figures/fig_identifiability_heatmap.pdf
docs/paper/figures/fig_domain_gamma.pdf
docs/paper/_pdf_images/main_p3.png
docs/paper/_pdf_images/main_p4.png
docs/paper/_pdf_images/main_p5.png
docs/paper/_pdf_images/main_p6.png
docs/paper/_pdf_images/main_p7.png
docs/paper/_pdf_images/main_p11.png
docs/paper/_pdf_images/main_p12.png
docs/paper/_pdf_images/main_p2.png
docs/paper/_pdf_images/main_p1.png
docs/paper/_pdf_images/main_p10.png
docs/paper/_pdf_images/main_p8.png
docs/paper/_pdf_images/main_p9.png
docs/paper/references.bib
docs/paper/ethics.tex
docs/paper/figures/fig_dose_response.pdf
docs/paper/figures/arc_dose_response.pdf
docs/paper/figures/baseline_vs_effect.pdf
figures/paper/fig_dose_response.pdf
figures/paper/arc_dose_response.pdf
figures/paper/baseline_vs_effect.pdf
docs/paper/figures/fig_arc_dose_response.pdf
docs/paper/figures/fig_baseline_vs_effect.pdf
figures/paper/fig_arc_dose_response.pdf
figures/paper/fig_baseline_vs_effect.pdf
docs/paper/related_work.tex
docs/paper/experimental_setup.tex
docs/paper/main.blg
docs/paper/main.bbl
docs/paper/main.fls
docs/paper/main.fdb_latexmk
docs/paper/abstract.tex
artifacts/_project/paper/algorithm1_pseudocode.tex
artifacts/_project/paper/algorithm1_pseudocode_c1bd81.tex
docs/paper/introduction.tex
docs/paper/figures/fig_treated_untreated.pdf
docs/paper/figures/fig_did_dose_response.pdf
docs/paper/conclusion.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/limitations.tex
artifacts/_project/paper/appendix_domain_decomposition.md
docs/paper/appendix.tex
docs/paper/results.tex
docs/paper/main.aux
docs/paper/main.out
docs/paper/main.log
docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "9cc6561f-aa19-4a7f-83af-e85aa7f97838",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/main.pdf",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/fisher_info_appendix.tex",
      "artifacts/_project/paper/results_tables.md",
      "paper/sections/method.md",
      "artifacts/_project/paper/method.md",
      "figures/paper/gen_fig_domain_gamma.py",
      "figures/paper/fig_domain_gamma.pdf",
      "figures/paper/fig_domain_gamma.png",
      "figures/paper/gen_fig_dose_response.py",
      "figures/paper/fig_dose_response.png",
      "figures/paper/gen_fig_signal_heatmap.py",
      "figures/paper/fig_signal_heatmap.pdf",
      "figures/paper/fig_signal_heatmap.png",
      "figures/paper/gen_fig_pipeline.py",
      "figures/paper/fig_pipeline.pdf",
      "figures/paper/fig_pipeline.png",
      "paper/sections/discussion.md",
      "artifacts/_project/paper/discussion.md",
      "paper/sections/experimental_setup.md",
      "artifacts/_project/paper/experimental_setup.md",
      "figures/paper/gen_fig_calibration.py",
      "figures/paper/fig_calibration.pdf",
      "figures/paper/fig_calibration.png",
      "figures/paper/fig_identifiability_heatmap.pdf",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/related_work_04a735.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/references.bib",
      "docs/paper/acl.sty",
      "docs/paper/acl_natbib.bst",
      "docs/paper/figures/fig_signal_heatmap.pdf",
      "docs/paper/figures/fig_identifiability_heatmap.pdf",
      "docs/paper/figures/fig_domain_gamma.pdf",
      "docs/paper/_pdf_images/main_p3.png",
      "docs/paper/_pdf_images/main_p4.png",
      "docs/paper/_pdf_images/main_p5.png",
      "docs/paper/_pdf_images/main_p6.png",
      "docs/paper/_pdf_images/main_p7.png",
      "docs/paper/_pdf_images/main_p11.png",
      "docs/paper/_pdf_images/main_p12.png",
      "docs/paper/_pdf_images/main_p2.png",
      "docs/paper/_pdf_images/main_p1.png",
      "docs/paper/_pdf_images/main_p10.png",
      "docs/paper/_pdf_images/main_p8.png",
      "docs/paper/_pdf_images/main_p9.png",
      "docs/paper/references.bib",
      "docs/paper/ethics.tex",
      "docs/paper/figures/fig_dose_response.pdf",
      "docs/paper/figures/arc_dose_response.pdf",
      "docs/paper/figures/baseline_vs_effect.pdf",
      "figures/paper/fig_dose_response.pdf",
      "figures/paper/arc_dose_response.pdf",
      "figures/paper/baseline_vs_effect.pdf",
      "docs/paper/figures/fig_arc_dose_response.pdf",
      "docs/paper/figures/fig_baseline_vs_effect.pdf",
      "figures/paper/fig_arc_dose_response.pdf",
      "figures/paper/fig_baseline_vs_effect.pdf",
      "docs/paper/related_work.tex",
      "docs/paper/experimental_setup.tex",
      "docs/paper/main.blg",
      "docs/paper/main.bbl",
      "docs/paper/main.fls",
      "docs/paper/main.fdb_latexmk",
      "docs/paper/abstract.tex",
      "artifacts/_project/paper/algorithm1_pseudocode.tex",
      "artifacts/_project/paper/algorithm1_pseudocode_c1bd81.tex",
      "docs/paper/introduction.tex",
      "docs/paper/figures/fig_treated_untreated.pdf",
      "docs/paper/figures/fig_did_dose_response.pdf",
      "docs/paper/conclusion.tex",
      "docs/paper/main.tex",
      "docs/paper/method.tex",
      "docs/paper/limitations.tex",
      "artifacts/_project/paper/appendix_domain_decomposition.md",
      "docs/paper/appendix.tex",
      "docs/paper/results.tex",
      "docs/paper/main.aux",
      "docs/paper/main.out",
      "docs/paper/main.log",
      "docs/paper/main.pdf"
    ],
    "durationMs": 76,
    "numFiles": 83,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Good, the main paper files are at `docs/paper/`. Let me now read the key files for the audit:
1. `docs/paper/method.tex` - for sensitivity description and Algorithm 1 reference
2. `docs/paper/appendix.tex` - for sensitivity appendix details
3. `docs/paper/results.tex` - for V-recovery descriptions
4. `docs/paper/experimental_setup.tex` - might have sensitivity info
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "70a6111a-aed9-4b66-84f7-ea5b6f46f454",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191HaEgi6cjyd6gB7urHyTx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2098,
      "cache_read_input_tokens": 29547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2098
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

_source line 18_

Found paper files at `docs/paper/`. Reading the relevant sections now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "cc64c847-1dbd-46ae-abd4-59fa23be43df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191HaEgi6cjyd6gB7urHyTx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2098,
      "cache_read_input_tokens": 29547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2098
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

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01MNzu2YjBGFvKChCcW1JKPH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "23a3f7bc-1c9a-4617-9828-fc8388721856",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191HaEgi6cjyd6gB7urHyTx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2098,
      "cache_read_input_tokens": 29547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2098
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

_source line 20 · 2026-05-19T22:09:33.116Z_

<details><summary>↩ Tool result · `toolu_01MNzu2YjBGFvKChCcW1JKPH`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \citep{kadavath2022}; concurrent work by \citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\mathcal{S} = \{\text{S1, S2, S4}\}$) and is applicable to any benchmark without auxiliary data requirements. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_failure}.
17	
18	We aggregate signals via Reciprocal Rank Fusion \citep[RRF;][]{cormack_2009_rrf}:
19	\begin{equation}
20	\label{eq:rrf}
21	    e_{ij} = \sum_{s \in \mathcal{S}} \frac{1}{\kappa + r_{s}(i)},
22	\end{equation}
23	where $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\kappa=60$ is the standard smoothing constant, and $|\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to obtain $e_{ij} \in [0,1]$. The resulting distribution is highly right-skewed (mean 0.041, median 0.016, max 0.879), with most model-item pairs receiving near-zero exposure.
24	
25	\subsection{Stage 2: Contamination-Augmented IRT}
26	\label{sec:stage2}
27	
28	\paragraph{Primary model: 2PL+$\gamma$.}
29	Our primary specification augments the two-parameter logistic (2PL) model \citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:
30	\begin{equation}
31	\label{eq:2pl_gamma}
32	    P(y_{ijk} = 1) = \sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
33	\end{equation}
34	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \in \mathbb{R}$ is item difficulty, $\theta_j$ is model ability, and $\gamma_k$ is the scalar contamination effect for benchmark~$k$. Each benchmark is fitted independently; when finer-grained diagnosis is needed, we further stratify within a benchmark by cognitive domain (\S\ref{sec:domain_differential}).
35	
36	The additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\gamma_k \cdot e_{ij} / a_i$ units on the ability scale (this holds exactly under linearization of the logistic function; the true shift is nonlinear and probability-dependent).
37	
38	For MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\ref{sec:4pl_details}); this requires $J \geq 16$ and is not used in domain-level analyses ($J = 13$).
39	
40	\paragraph{Inference.}
41	We perform Bayesian inference via NUTS \citep{hoffman2014} in Stan \citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $\gamma_k \sim \mathcal{N}(0,1)$. Convergence requires split-$\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.
42	
43	\paragraph{Calibrated score.}
44	The decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:
45	\begin{equation}
46	\label{eq:calibrated}
47	    \text{Acc}_{j}^{\text{cal}} = \frac{1}{I_k} \sum_{i=1}^{I_k}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[\sigma\!\bigl(a_i(\theta_j - b_i)\bigr)\right],
48	\end{equation}
49	with credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.
50	
51	\paragraph{Identifiability.}
52	\label{sec:fisher}
53	\label{sec:value_decomposition}
54	The reliability of $\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\geq$0.55 with $J \geq 50$ (Appendix~\ref{sec:identifiability}). Eq.~\eqref{eq:calibrated} depends on $\theta_j$, not $\gamma$ directly, predicting that vanilla 2PL ($\gamma\!=\!0$) achieves comparable calibration to 2PL+$\gamma$, with $\gamma_k$ serving diagnosis rather than calibration (\S\ref{sec:calibration_results}).
55	
56	\subsection{Dose-Response Profile Classification}
57	\label{sec:classification}
58	
59	Independent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern. Algorithm~\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by a noise threshold $\tau$, severity threshold $\sigma$, saturation ratio $\rho$, and late-gain floor $\lambda$. The three-way top-level split (immune/harm/benefit) is governed by the sign and magnitude of $\Delta = a_{100} - a_0$ relative to $\tau$; within-branch refinements distinguish U-collapse from V-recovery (via mid-dosage trough detection) and monotonic benefit from benefit-saturation (via gain deceleration). A mid-trajectory volatility check ($v^*$) within the immune branch distinguishes true immunity (Phi-4: $v^* = 0.34$pp $\le \tau$) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $\Delta \approx 0$ but $v^* = 3.22$pp $> \tau$); recovery extent varies by seed (partial at seed$=$42, full at seed$=$123). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms 5/5 families are stable across all $(\tau, \sigma)$ combinations (Appendix~\ref{sec:classification_sensitivity}).
60	
61	\begin{algorithm}[H]
62	\caption{Dose-Response Profile Classification}
63	\label{alg:profile-classification}
64	\begin{algorithmic}[1]
65	\Require Accuracy vector $\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \in \{0, 5, 25, 50, 100\}\%$
66	\Require Noise threshold $\tau = 1$ pp, severity threshold $\sigma = 5$ pp
67	\Require Saturation ratio $\rho = 0.3$, late-gain floor $\lambda = 0.5$ pp
68	\Ensure Pattern $p \in \{\textsc{Immune}, \textsc{U-collapse}, \textsc{V-recovery}, \textsc{Benefit}, \textsc{Benefit-sat}\}$
69	\State $\Delta \gets a_{100} - a_{0}$ \Comment{end-to-end accuracy shift}
70	\State $m^* \gets \min(a_{5},\, a_{25},\, a_{50})$ \Comment{mid-dosage minimum}
71	\State $v^* \gets \max_{i \in \{5,25,50\}} |a_i - a_0|$ \Comment{max mid-trajectory deviation}
72	\If{$|\Delta| \le \tau$}
73	    \If{$v^* \le \tau$}
74	        \State \Return \textsc{Immune} \Comment{fluctuation within noise band}
75	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
76	        \State \Return \textsc{V-recovery} \Comment{V-dip with full endpoint recovery}
77	    \Else
78	        \State \Return \textsc{Immune} \Comment{non-V volatility, endpoint stable}
79	    \EndIf
80	\ElsIf{$\Delta < -\tau$}
81	    \If{$\Delta \le -\sigma$}
82	        \State \Return \textsc{U-collapse} \Comment{severe monotonic degradation}
83	    \ElsIf{$m^* < a_{0}$ \textbf{and} $m^* < a_{100}$}
84	        \State \Return \textsc{V-recovery} \Comment{mid-dosage trough with partial recovery}
85	    \Else
86	        \State \Return \textsc{U-collapse} \Comment{moderate decline, no V-shape}
87	    \EndIf
88	\Else \Comment{$\Delta > \tau$}
89	    \State $g_1 \gets a_{25} - a_{0}$ \Comment{first-half gain}
90	    \State $g_2 \gets a_{100} - a_{25}$ \Comment{second-half gain}
91	    \State $\ell \gets a_{100} - a_{50}$ \Comment{late gain}
92	    \If{$(g_1 > 0$ \textbf{and} $g_2 < \rho \cdot g_1)$ \textbf{or} $\ell < \lambda$}
93	        \State \Return \textsc{Benefit-sat} \Comment{gain decelerates at high dosage}
94	    \Else
95	        \State \Return \textsc{Benefit} \Comment{sustained improvement}
96	    \EndIf
97	\EndIf
98	\end{algorithmic}
99	\end{algorithm}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "30afb928-c5ea-469a-a1ac-21cdcdad92a5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nLet $y_{ijk} \\in \\{0,1\\}$ denote the binary response of model~$j$ ($j=1,\\ldots,J$) to item~$i$ ($i=1,\\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\\theta_j, \\boldsymbol{\\xi}_i)$ where $\\theta_j$ is latent ability and $\\boldsymbol{\\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\\hat{\\theta}_j$ confounds genuine capability with memorization.\n\nOur goal is to estimate $\\theta_j^{\\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \\citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \\citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \\in [0,1]$, fitting per-benchmark models to handle the shared item pool \\citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).\n\n\\subsection{Stage 1: Multi-Signal Exposure Mapping}\n\\label{sec:stage1}\n\nFor each model~$j$ and item~$i$, we consider four candidate detection signals. \\textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \\textbf{S2}~(Min-K\\%++): a membership inference statistic based on token-level surprisal \\citep{zhang_2024_minkpp}. \\textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \\citep{dekoninck2024constat}. \\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions, inspired by the finding that LLMs can assess their own knowledge \\citep{kadavath2022}; concurrent work by \\citet{tao2025detecting} uses a related but mechanistically distinct entropy collapse approach targeting RL-trained models. S3 requires paired paraphrased items as reference and is therefore limited to benchmarks with existing paraphrase sets. Our primary pipeline uses the remaining three signals ($\\mathcal{S} = \\{\\text{S1, S2, S4}\\}$) and is applicable to any benchmark without auxiliary data requirements. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \\S\\ref{sec:signal_failure}.\n\nWe aggregate signals via Reciprocal Rank Fusion \\citep[RRF;][]{cormack_2009_rrf}:\n\\begin{equation}\n\\label{eq:rrf}\n    e_{ij} = \\sum_{s \\in \\mathcal{S}} \\frac{1}{\\kappa + r_{s}(i)},\n\\end{equation}\nwhere $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious), $\\kappa=60$ is the standard smoothing constant, and $|\\mathcal{S}|=3$ in our primary configuration. Raw scores are min-max normalized per model to obtain $e_{ij} \\in [0,1]$. The resulting distribution is highly right-skewed (mean 0.041, median 0.016, max 0.879), with most model-item pairs receiving near-zero exposure.\n\n\\subsection{Stage 2: Contamination-Augmented IRT}\n\\label{sec:stage2}\n\n\\paragraph{Primary model: 2PL+$\\gamma$.}\nOur primary specification augments the two-parameter logistic (2PL) model \\citep{lord_1980_irt,hambleton_1991_irt} with a contamination covariate. We fit independent IRT models per benchmark~$k$, each with its own contamination effect $\\gamma_k$. Per-benchmark fitting avoids cross-benchmark item parameter borrowing while permitting heterogeneous contamination effects. For benchmark~$k$, the response probability is:\n\\begin{equation}\n\\label{eq:2pl_gamma}\n    P(y_{ijk} = 1) = \\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwhere $\\sigma(\\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \\in \\mathbb{R}$ is item difficulty, $\\theta_j$ is model ability, and $\\gamma_k$ is the scalar contamination effect for benchmark~$k$. Each benchmark is fitted independently; when finer-grained diagnosis is needed, we further stratify within a benchmark by cognitive domain (\\S\\ref{sec:domain_differential}).\n\nThe additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\\gamma_k \\cdot e_{ij} / a_i$ units on the ability scale (this holds exactly under linearization of the logistic function; the true shift is nonlinear and probability-dependent).\n\nFor MC-format benchmarks, a 4PL extension adds guessing and ceiling asymptotes (Appendix~\\ref{sec:4pl_details}); this requires $J \\geq 16$ and is not used in domain-level analyses ($J = 13$).\n\n\\paragraph{Inference.}\nWe perform Bayesian inference via NUTS \\citep{hoffman2014} in Stan \\citep{carpenter2017} with four chains and target acceptance 0.95. Priors: $\\theta_j \\sim \\mathcal{N}(0,1)$, $a_i \\sim \\text{LogNormal}(0, 0.5)$, $b_i \\sim \\mathcal{N}(0,1)$, $\\gamma_k \\sim \\mathcal{N}(0,1)$. Convergence requires split-$\\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.\n\n\\paragraph{Calibrated score.}\nThe decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:\n\\begin{equation}\n\\label{eq:calibrated}\n    \\text{Acc}_{j}^{\\text{cal}} = \\frac{1}{I_k} \\sum_{i=1}^{I_k}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[\\sigma\\!\\bigl(a_i(\\theta_j - b_i)\\bigr)\\right],\n\\end{equation}\nwith credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.\n\n\\paragraph{Identifiability.}\n\\label{sec:fisher}\n\\label{sec:value_decomposition}\nThe reliability of $\\gamma$ depends on signal AUC and ensemble size $J$; simulation validates that recovery requires AUC$\\geq$0.55 with $J \\geq 50$ (Appendix~\\ref{sec:identifiability}). Eq.~\\eqref{eq:calibrated} depends on $\\theta_j$, not $\\gamma$ directly, predicting that vanilla 2PL ($\\gamma\\!=\\!0$) achieves comparable calibration to 2PL+$\\gamma$, with $\\gamma_k$ serving diagnosis rather than calibration (\\S\\ref{sec:calibration_results}).\n\n\\subsection{Dose-Response Profile Classification}\n\\label{sec:classification}\n\nIndependent of the IRT calibration pipeline, we formalize how each model's accuracy trajectory across dosage levels is classified into a canonical dose-response pattern. Algorithm~\\ref{alg:profile-classification} defines a deterministic decision tree over the accuracy vector $\\mathbf{a} = (a_0, a_5, a_{25}, a_{50}, a_{100})$, parameterized by a noise threshold $\\tau$, severity threshold $\\sigma$, saturation ratio $\\rho$, and late-gain floor $\\lambda$. The three-way top-level split (immune/harm/benefit) is governed by the sign and magnitude of $\\Delta = a_{100} - a_0$ relative to $\\tau$; within-branch refinements distinguish U-collapse from V-recovery (via mid-dosage trough detection) and monotonic benefit from benefit-saturation (via gain deceleration). A mid-trajectory volatility check ($v^*$) within the immune branch distinguishes true immunity (Phi-4: $v^* = 0.34$pp $\\le \\tau$) from V-recovery with full endpoint recovery (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$); recovery extent varies by seed (partial at seed$=$42, full at seed$=$123). All thresholds are explicit and adjustable; a 30-combination grid sweep confirms 5/5 families are stable across all $(\\tau, \\sigma)$ combinations (Appendix~\\ref{sec:classification_sensitivity}).\n\n\\begin{algorithm}[H]\n\\caption{Dose-Response Profile Classification}\n\\label{alg:profile-classification}\n\\begin{algorithmic}[1]\n\\Require Accuracy vector $\\mathbf{a} = (a_{0}, a_{5}, a_{25}, a_{50}, a_{100})$ at dosages $d \\in \\{0, 5, 25, 50, 100\\}\\%$\n\\Require Noise threshold $\\tau = 1$ pp, severity threshold $\\sigma = 5$ pp\n\\Require Saturation ratio $\\rho = 0.3$, late-gain floor $\\lambda = 0.5$ pp\n\\Ensure Pattern $p \\in \\{\\textsc{Immune}, \\textsc{U-collapse}, \\textsc{V-recovery}, \\textsc{Benefit}, \\textsc{Benefit-sat}\\}$\n\\State $\\Delta \\gets a_{100} - a_{0}$ \\Comment{end-to-end accuracy shift}\n\\State $m^* \\gets \\min(a_{5},\\, a_{25},\\, a_{50})$ \\Comment{mid-dosage minimum}\n\\State $v^* \\gets \\max_{i \\in \\{5,25,50\\}} |a_i - a_0|$ \\Comment{max mid-trajectory deviation}\n\\If{$|\\Delta| \\le \\tau$}\n    \\If{$v^* \\le \\tau$}\n        \\State \\Return \\textsc{Immune} \\Comment{fluctuation within noise band}\n    \\ElsIf{$m^* < a_{0}$ \\textbf{and} $m^* < a_{100}$}\n        \\State \\Return \\textsc{V-recovery} \\Comment{V-dip with full endpoint recovery}\n    \\Else\n        \\State \\Return \\textsc{Immune} \\Comment{non-V volatility, endpoint stable}\n    \\EndIf\n\\ElsIf{$\\Delta < -\\tau$}\n    \\If{$\\Delta \\le -\\sigma$}\n        \\State \\Return \\textsc{U-collapse} \\Comment{severe monotonic degradation}\n    \\ElsIf{$m^* < a_{0}$ \\textbf{and} $m^* < a_{100}$}\n        \\State \\Return \\textsc{V-recovery} \\Comment{mid-dosage trough with partial recovery}\n    \\Else\n        \\State \\Return \\textsc{U-collapse} \\Comment{moderate decline, no V-shape}\n    \\EndIf\n\\Else \\Comment{$\\Delta > \\tau$}\n    \\State $g_1 \\gets a_{25} - a_{0}$ \\Comment{first-half gain}\n    \\State $g_2 \\gets a_{100} - a_{25}$ \\Comment{second-half gain}\n    \\State $\\ell \\gets a_{100} - a_{50}$ \\Comment{late gain}\n    \\If{$(g_1 > 0$ \\textbf{and} $g_2 < \\rho \\cdot g_1)$ \\textbf{or} $\\ell < \\lambda$}\n        \\State \\Return \\textsc{Benefit-sat} \\Comment{gain decelerates at high dosage}\n    \\Else\n        \\State \\Return \\textsc{Benefit} \\Comment{sustained improvement}\n    \\EndIf\n\\EndIf\n\\end{algorithmic}\n\\end{algorithm}",
      "numLines": 99,
      "startLine": 1,
      "totalLines": 99
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_016jkAC5cZGjvSCpg7WqaX2t`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "656979cd-bbf1-466b-b543-ca7681f0be85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191HaEgi6cjyd6gB7urHyTx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2098,
      "cache_read_input_tokens": 29547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2098
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

_source line 22 · 2026-05-19T22:09:33.947Z_

<details><summary>↩ Tool result · `toolu_016jkAC5cZGjvSCpg7WqaX2t`</summary>

```text
1	\appendix
2	
3	\section{ARC-Challenge Cross-Benchmark Analysis}
4	\label{sec:arc_cross_benchmark}
5	
6	ARC-Challenge (25-shot, 1{,}172 items) patterns are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$3.8pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($\pm$0.6pp). Gemma-2 ARC is excluded due to a 16pp evaluation artifact. Qwen-14B exhibits V-recovery on ARC rather than U-collapse ($-$3.4pp vs.\ $-$9.4pp on MMLU), a 2.8$\times$ attenuation reflecting benchmark-specific properties. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042), and Gemma-2's ARC $\Delta$acc 95\% CI crosses zero ($[-2.47, +0.09]$pp).
7	
8	Dose-response profiles are jointly determined by model and benchmark properties: direction is governed by model baseline ability (the 64.7\% threshold); shape is governed by benchmark properties (item pool size, difficulty distribution, evaluation format). This benchmark-conditionality is a finding in its own right---practitioners cannot assume a contamination profile on one benchmark transfers to another.
9	
10	\begin{figure}[h]
11	\centering
12	\includegraphics[width=\columnwidth]{figures/fig_arc_dose_response.pdf}
13	\caption{ARC-Challenge accuracy vs.\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\ref{fig:dose_response}) for 4/5 models.}
14	\label{fig:dose_response_arc}
15	\end{figure}
16	
17	\section{Signal Reliability Across Scales}
18	\label{sec:signal_reliability_appendix}
19	
20	\begin{figure}[h]
21	\centering
22	\includegraphics[width=\columnwidth]{figures/fig_signal_heatmap.pdf}
23	\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\%++) reverses at 0.5B; S4 is near-random below 1.5B.}
24	\label{fig:signal_heatmap}
25	\end{figure}
26	
27	\section{Identifiability Simulation}
28	\label{sec:identifiability_appendix}
29	
30	\begin{figure}[h]
31	\centering
32	\includegraphics[width=\columnwidth]{figures/fig_identifiability_heatmap.pdf}
33	\caption{$\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\% CI coverage $\geq90\%$ require $J\geq50$ at AUC$=$0.55, but only $J\geq16$ at AUC$\geq$0.90.}
34	\label{fig:identifiability_heatmap}
35	\end{figure}
36	
37	Fisher information $\mathcal{I}(\gamma) \propto \text{Var}(e_{\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\% CI coverage $\geq 90\%$ require $J \geq 50$; at AUC$\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).
38	
39	\section{4PL Extension}
40	\label{sec:4pl_details}
41	
42	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
43	\begin{equation}
44	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
45	\end{equation}
46	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
47	
48	\section{S4 Self-Critique Signal Details}
49	\label{sec:s4_details}
50	
51	S4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\text{YES})$, then score each item as the negative entropy of this distribution: $\text{S4}_i = -[-p\log p - (1-p)\log(1-p)]$ where $p = P(\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.
52	
53	\section{Training Convergence}
54	\label{sec:training_convergence}
55	
56	All SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.
57	
58	\section{Model Exclusion Details}
59	\label{sec:exclusion_details}
60	
61	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
62	
63	\paragraph{Model sets across analyses.}
64	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
65	
66	\begin{table}[h]
67	\centering
68	\caption{Model set composition across analyses.}
69	\label{tab:model_sets}
70	\footnotesize
71	\begin{tabular}{lcll}
72	\toprule
73	Analysis & $J$ & Model Set & Section \\
74	\midrule
75	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
76	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
77	Cross-family & 16--28 & varies by benchmark & \S\ref{sec:taxonomy} \\
78	Oracle ablation & 13 & domain whitelist & \S\ref{sec:calibration_results} \\
79	\bottomrule
80	\end{tabular}
81	\end{table}
82	
83	\section{Prior Sensitivity Analysis}
84	\label{sec:prior_sensitivity}
85	
86	To assess the influence of the $\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\gamma \sim \mathcal{N}(0, 0.5)$, $\mathcal{N}(0, 1)$ (default), and $\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\% CI includes zero in all cases (lower bound stable at $\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\hat{R} < 1.01$, ESS $> 3800$, PPP $\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\gamma$-based conclusions at current ensemble sizes.
87	
88	For the Social Sciences domain ($J=16$, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:
89	
90	\begin{table}[h]
91	\centering
92	\caption{Social Sciences $\gamma$ prior sensitivity ($J$=16).}
93	\label{tab:socsci_prior}
94	\footnotesize
95	\begin{tabular}{lcccc}
96	\toprule
97	Prior & $\hat{\gamma}$ & 95\% CI & $P(\gamma\!<\!0)$ & PPP \\
98	\midrule
99	$\mathcal{N}(0, 0.5)$ & $-$0.428 & [$-$0.825, $-$0.017] & 97.95\% & 0.242 \\
100	$\mathcal{N}(0, 1)$ & $-$0.497 & [$-$0.943, $-$0.055] & 98.48\% & 0.282 \\
101	$\mathcal{N}(0, 2)$ & $-$0.507 & [$-$0.957, $-$0.077] & 98.92\% & 0.282 \\
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	In contrast to the pooled analysis where $\hat{\gamma}$ shifts 2.6$\times$ across priors, Social Sciences $\hat{\gamma}$ varies only 1.2$\times$ ($-$0.43 to $-$0.51), with $P(\gamma<0) \geq 97.95\%$ in all cases.
107	
108	\section{IRT Ability Separation by Scale}
109	\label{sec:theta_separation}
110	
111	Table~\ref{tab:theta_separation} reports the mean posterior $\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\Delta\theta = \bar{\theta}_{3\text{B}} - \bar{\theta}_{1.5\text{B}}$ is positive and significant (95\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.
112	
113	\begin{table}[h]
114	\centering
115	\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\Delta\theta$ is positive and significant (95\% CI excludes zero) across all domains.}
116	\label{tab:theta_separation}
117	\footnotesize
118	\begin{tabular}{lccc}
119	\toprule
120	Domain & $\bar{\theta}_{1.5\text{B}}$ & $\bar{\theta}_{3\text{B}}$ & $\Delta\theta$ [95\% CI] \\
121	\midrule
122	Math & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\
123	Science & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\
124	CS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\
125	Medical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\
126	Humanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\
127	Social Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\
128	Business/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\
129	Other & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\
130	\midrule
131	Pooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\
132	\bottomrule
133	\end{tabular}
134	\end{table}
135	
136	\section{DiD Across Dosage Levels}
137	\label{sec:did_dosage}
138	
139	\begin{figure}[h]
140	\centering
141	\includegraphics[width=\columnwidth]{figures/fig_did_dose_response.pdf}
142	\caption{Difference-in-differences (treated vs.\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all five model families, confirming that the global capability modulation mechanism (\S\ref{sec:memorization_test}) is consistent across the full dosage range.}
143	\label{fig:did_dose_response}
144	\end{figure}
145	
146	\section{Dose-Response Details}
147	\label{sec:dose_response_details}
148	
149	The five dose-response patterns reported in \S\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \textit{decreases} with dosage (0.41 at d000 $\to$ 0.27 at d100), consistent with the position bias confound documented in \S\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\%) overwhelms any memorization benefit.
150	
151	\section{Sensitivity of Profile Classification}
152	\label{sec:classification_sensitivity}
153	
154	We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\tau, \sigma)$ combinations: $\tau \in \{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\}$~pp $\times$ $\sigma \in \{3, 4, 5, 6, 7\}$~pp. Table~\ref{tab:sensitivity} reports stability across this grid.
155	
156	\begin{table}[h]
157	\centering
158	\caption{Profile classification stability across 30 $(\tau, \sigma)$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.}
159	\label{tab:sensitivity}
160	\footnotesize
161	\begin{tabular}{lccc}
162	\toprule
163	Model & Default Pattern & Stability & Notes \\
164	\midrule
165	Phi-4 14.7B & Immune & 30/30 & $v^* = 0.34$pp $\le$ all $\tau$ \\
166	Qwen-14B & U-collapse & 30/30 & --- \\
167	Gemma-2 9B & Benefit & 30/30 & --- \\
168	OLMo-2 7B & Benefit-sat & 30/30 & --- \\
169	Qwen-7B & V-recovery & 30/30 & volatility check resolves \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	With the mid-trajectory volatility check (Algorithm~\ref{alg:profile-classification}, line~3), all five families achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\Delta \approx 0$ but $v^* = 3.22$pp $> \tau$). The severity threshold $\sigma$ has zero impact on any model's classification, because no model's $\Delta\text{acc}$ falls in the range where $\sigma$ determines the U-collapse vs.\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\sigma=7$).
175	
176	\section{Cross-Family Domain Decomposition}
177	\label{sec:domain_decomposition}
178	
179	We decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all five model families at each contamination dosage.
180	
181	Two patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, U-collapse (Qwen-14B) produces negative $\Delta\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\Delta\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.
182	
183	Second, domains differ in sensitivity. STEM is the most resilient (mean $|\Delta\text{acc}| = 2.8$pp across five families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\times$ the STEM magnitude. The ordering is stable across patterns: in U-collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.
184	
185	These results reinforce the global capability modulation interpretation (\S\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.
186	
187	\section{Baseline Ability vs.\ Contamination Effect}
188	\label{sec:baseline_vs_effect}
189	
190	\begin{figure}[h]
191	\centering
192	\includegraphics[width=\columnwidth]{figures/fig_baseline_vs_effect.pdf}
193	\caption{Baseline MMLU accuracy (d000) vs.\ maximum accuracy change ($\Delta$acc) under contamination. A threshold between 61.9\% (Gemma-2) and 66.1\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Threshold estimated from five models spanning four independent families.}
194	\label{fig:baseline_vs_effect}
195	\end{figure}
196	
197	\section{Per-Domain $\gamma$ Estimates}
198	\label{sec:domain_gamma_table}
199	
200	\begin{figure}[h]
201	\centering
202	\includegraphics[width=\columnwidth]{figures/fig_domain_gamma.pdf}
203	\caption{Per-domain $\gamma_d$ estimates with 95\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}
204	\label{fig:domain_gamma}
205	\end{figure}
206	
207	\begin{table}[h]
208	\centering
209	\caption{Per-domain $\gamma$ estimates (2PL+$\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\hat{R} < 1.01$). Social Sciences $P(\gamma\!<\!0)$ strengthens from 99.1\% to 99.7\% at $J$=16, crossing the Bonferroni-corrected threshold of 99.375\% for eight tests. Results remain exploratory at these ensemble sizes \citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}
210	\label{tab:domain_gamma}
211	\footnotesize
212	\resizebox{\columnwidth}{!}{%
213	\begin{tabular}{lcccccc}
214	\toprule
215	 & \multicolumn{2}{c}{$J$=13} & \multicolumn{4}{c}{$J$=16} \\
216	\cmidrule(lr){2-3} \cmidrule(lr){4-7}
217	Domain & $\gamma$ & $P(\gamma\!<\!0)$ & $\gamma$ & $P(\gamma\!<\!0)$ & PPP & $\hat{R}$ \\
218	\midrule
219	MMLU: Math & +0.50 & 8.1\% & +0.60 & 3.8\% & 0.305 & 1.007 \\
220	MMLU: Science & +0.50 & 7.8\% & +0.57 & 4.3\% & 0.197 & 1.007 \\
221	MMLU: CS/Eng & +0.50 & 14.8\% & +0.32 & 24.0\% & 0.503 & 1.006 \\
222	MMLU: Medical & +0.24 & 24.0\% & +0.05 & 43.6\% & 0.268 & 1.008 \\
223	MMLU: Other & +0.13 & 35.7\% & +0.32 & 20.4\% & 0.072$^\dagger$ & 1.008 \\
224	MMLU: Business/Law & +0.04 & 44.1\% & +0.08 & 37.8\% & 0.395 & 1.007 \\
225	MMLU: Humanities & $-$0.31 & 85.4\% & $-$0.14 & 69.7\% & 0.416 & 1.007 \\
226	MMLU: Social Sci & $-$0.57 & \textbf{99.1\%} & $-$0.63 & \textbf{99.7\%} & 0.722 & 1.006 \\
227	\bottomrule
228	\end{tabular}}
229	
230	\vspace{2pt}
231	{\scriptsize $^\dagger$PPP below acceptable threshold (0.1); $\gamma$ estimate for this domain should be interpreted with caution.}
232	\end{table}
233	
234	\section{Threshold DGP Simulation}
235	\label{sec:threshold_dgp}
236	
237	To test whether threshold-type misspecification explains the non-significant oracle $\gamma$, we simulate data under step-function contamination DGPs where items are affected only above exposure thresholds of 0.3, 0.5, and 0.7 (three cutoffs, ten seeds each). Under these DGPs, the linear 2PL+$\gamma$ specification overestimates rather than attenuates the contamination effect (ratio 1.09 to 1.33 relative to the true $\gamma$), while PPP remains in the acceptable range (0.50 to 0.56). This rules out threshold-type misspecification as an explanation for the non-significant oracle $\gamma$ under a unidirectional effect assumption. Bidirectional item-level effects (positive for some items, negative for others) could still produce a near-zero pooled $\gamma$, but this collapses to the heterogeneity interpretation (\S\ref{sec:domain_differential}). The simulation uses uniform exposure distributions; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.
238	
239	\section{ARC IRT Results}
240	\label{sec:arc_irt}
241	
242	ARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\sim}$0.7pp) is smaller than correction noise. Domain-level $\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).
243	
244	\section{Full Baseline Comparison}
245	\label{sec:full_baselines}
246	
247	Table~\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.
248	
249	B6-DCR \citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.
250	
251	\begin{table}[h]
252	\centering
253	\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\downarrow$.}
254	\label{tab:full_baselines_arc}
255	\footnotesize
256	\begin{tabular}{lc}
257	\toprule
258	Method & ARC MAE \\
259	\midrule
260	B0-Raw & 0.059 \\
261	B1-Remove\&Rescore & 0.059 \\
262	B2-Single2PL+$\gamma$ & 0.064 \\
263	B3-Vanilla4PL & 0.071 \\
264	B4-LinearRegression & 0.056 \\
265	B5-Emperor & 0.059 \\
266	B6-DCR & --- \\
267	\midrule
268	ContamCal (4PL+$\gamma$) & \textbf{0.035} \\
269	\bottomrule
270	\end{tabular}
271	\end{table}
272	
273	\begin{table}[h]
274	\centering
275	\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\downarrow$.}
276	\label{tab:full_baselines_gsm8k}
277	\footnotesize
278	\begin{tabular}{lc}
279	\toprule
280	Method & GSM8K MAE \\
281	\midrule
282	B0-Raw & 0.003 \\
283	B2-Single2PL+$\gamma$ & 0.320 \\
284	B3-Vanilla4PL & 0.012 \\
285	B4-LinearRegression & \textbf{0.003} \\
286	B6-DCR & --- \\
287	\midrule
288	ContamCal (4PL+$\gamma$) & 0.020 \\
289	\bottomrule
290	\end{tabular}
291	\end{table}
292	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "46a8a160-5eef-4f2a-bc69-08d19e4fdaa5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex",
      "content": "\\appendix\n\n\\section{ARC-Challenge Cross-Benchmark Analysis}\n\\label{sec:arc_cross_benchmark}\n\nARC-Challenge (25-shot, 1{,}172 items) patterns are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$3.8pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($\\pm$0.6pp). Gemma-2 ARC is excluded due to a 16pp evaluation artifact. Qwen-14B exhibits V-recovery on ARC rather than U-collapse ($-$3.4pp vs.\\ $-$9.4pp on MMLU), a 2.8$\\times$ attenuation reflecting benchmark-specific properties. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\\%, Gemma-2: 62.7\\%) due to the smaller item pool (1{,}172 vs.\\ 14{,}042), and Gemma-2's ARC $\\Delta$acc 95\\% CI crosses zero ($[-2.47, +0.09]$pp).\n\nDose-response profiles are jointly determined by model and benchmark properties: direction is governed by model baseline ability (the 64.7\\% threshold); shape is governed by benchmark properties (item pool size, difficulty distribution, evaluation format). This benchmark-conditionality is a finding in its own right---practitioners cannot assume a contamination profile on one benchmark transfers to another.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_arc_dose_response.pdf}\n\\caption{ARC-Challenge accuracy vs.\\ contamination dosage (25-shot). Patterns are directionally consistent with MMLU (Figure~\\ref{fig:dose_response}) for 4/5 models.}\n\\label{fig:dose_response_arc}\n\\end{figure}\n\n\\section{Signal Reliability Across Scales}\n\\label{sec:signal_reliability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_signal_heatmap.pdf}\n\\caption{Detection signal AUC across scale, dosage, and signal type. S1 achieves AUC $>0.95$ at all scales; S2 (Min-K\\%++) reverses at 0.5B; S4 is near-random below 1.5B.}\n\\label{fig:signal_heatmap}\n\\end{figure}\n\n\\section{Identifiability Simulation}\n\\label{sec:identifiability_appendix}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_identifiability_heatmap.pdf}\n\\caption{$\\gamma$ recovery as a function of signal AUC and ensemble size $J$. Bias $<0.05$ and 95\\% CI coverage $\\geq90\\%$ require $J\\geq50$ at AUC$=$0.55, but only $J\\geq16$ at AUC$\\geq$0.90.}\n\\label{fig:identifiability_heatmap}\n\\end{figure}\n\nFisher information $\\mathcal{I}(\\gamma) \\propto \\text{Var}(e_{\\cdot i})$ collapses when signal AUC is low. At AUC$=$0.55, bias $< 0.05$ and 95\\% CI coverage $\\geq 90\\%$ require $J \\geq 50$; at AUC$\\geq$0.90 (as S1 achieves in practice), $J = 16$ suffices. CI width scales as $J^{-0.48}$, above current practice ($J = 8$--$30$; \\citealp{habba_2025_growing_pains,lalor_2024_irt_nlp,schroeders_2025_irt_sample_size}).\n\n\\section{4PL Extension}\n\\label{sec:4pl_details}\n\nFor MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:\n\\begin{equation}\n    P(y_{ijk} = 1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_k \\cdot e_{ij}\\bigr),\n\\end{equation}\nwith $c_i \\sim \\text{Beta}(5,20)$ and $d_i \\sim \\text{Beta}(20,5)$. This requires $J \\geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\\gamma$ at $J=13$; pooled calibration uses $J=16$.\n\n\\section{S4 Self-Critique Signal Details}\n\\label{sec:s4_details}\n\nS4 prompts the model with ``Is the following answer correct?'' followed by the question and candidate answer. We extract YES/NO logits to compute $P(\\text{YES})$, then score each item as the negative entropy of this distribution: $\\text{S4}_i = -[-p\\log p - (1-p)\\log(1-p)]$ where $p = P(\\text{YES})$. Scores near zero indicate high confidence (potentially contaminated); large negative values indicate uncertainty.\n\n\\section{Training Convergence}\n\\label{sec:training_convergence}\n\nAll SFT configurations converged. Final training loss increases monotonically with dosage (d000: 1.08, d005: 1.08, d025: 1.14, d100: 1.17 averaged across seeds), consistent with distribution shift from benchmark item injection.\n\n\\section{Model Exclusion Details}\n\\label{sec:exclusion_details}\n\nOf the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\\alpha=32$, lr$=5\\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.\n\n\\paragraph{Model sets across analyses.}\nTable~\\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\\S\\ref{sec:injection}). Core findings ($\\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.\n\n\\begin{table}[h]\n\\centering\n\\caption{Model set composition across analyses.}\n\\label{tab:model_sets}\n\\footnotesize\n\\begin{tabular}{lcll}\n\\toprule\nAnalysis & $J$ & Model Set & Section \\\\\n\\midrule\nPooled baselines & 16 & 8$\\times$Qwen-1.5B + 8$\\times$Qwen-3B & \\S\\ref{sec:calibration_results} \\\\\nDomain $\\gamma$ & 13 & 8$\\times$Qwen-1.5B + 5$\\times$Qwen-3B & \\S\\ref{sec:domain_differential} \\\\\nCross-family & 16--28 & varies by benchmark & \\S\\ref{sec:taxonomy} \\\\\nOracle ablation & 13 & domain whitelist & \\S\\ref{sec:calibration_results} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Prior Sensitivity Analysis}\n\\label{sec:prior_sensitivity}\n\nTo assess the influence of the $\\gamma$ prior, we refit the pooled MMLU model ($J=16$, 300 RRF items) under three specifications: $\\gamma \\sim \\mathcal{N}(0, 0.5)$, $\\mathcal{N}(0, 1)$ (default), and $\\mathcal{N}(0, 2)$. The posterior mean shifts from 0.34 to 0.89 across priors, while the 95\\% CI includes zero in all cases (lower bound stable at $\\approx -0.4$; upper bound ranges from 1.11 to 2.20). All fits converge ($\\hat{R} < 1.01$, ESS $> 3800$, PPP $\\in [0.16, 0.25]$). The prior sensitivity confirms that $J=16$ provides insufficient data to override the prior, which reinforces the exploratory status of $\\gamma$-based conclusions at current ensemble sizes.\n\nFor the Social Sciences domain ($J=16$, 2000 items), the directional conclusion is data-dominated rather than prior-dominated:\n\n\\begin{table}[h]\n\\centering\n\\caption{Social Sciences $\\gamma$ prior sensitivity ($J$=16).}\n\\label{tab:socsci_prior}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nPrior & $\\hat{\\gamma}$ & 95\\% CI & $P(\\gamma\\!<\\!0)$ & PPP \\\\\n\\midrule\n$\\mathcal{N}(0, 0.5)$ & $-$0.428 & [$-$0.825, $-$0.017] & 97.95\\% & 0.242 \\\\\n$\\mathcal{N}(0, 1)$ & $-$0.497 & [$-$0.943, $-$0.055] & 98.48\\% & 0.282 \\\\\n$\\mathcal{N}(0, 2)$ & $-$0.507 & [$-$0.957, $-$0.077] & 98.92\\% & 0.282 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIn contrast to the pooled analysis where $\\hat{\\gamma}$ shifts 2.6$\\times$ across priors, Social Sciences $\\hat{\\gamma}$ varies only 1.2$\\times$ ($-$0.43 to $-$0.51), with $P(\\gamma<0) \\geq 97.95\\%$ in all cases.\n\n\\section{IRT Ability Separation by Scale}\n\\label{sec:theta_separation}\n\nTable~\\ref{tab:theta_separation} reports the mean posterior $\\theta$ estimates for 1.5B and 3B model groups across all MMLU domains and the pooled analysis. The ability gap $\\Delta\\theta = \\bar{\\theta}_{3\\text{B}} - \\bar{\\theta}_{1.5\\text{B}}$ is positive and significant (95\\% CI excludes zero) for all nine comparisons, which confirms that the IRT model recovers the expected scale-ability ordering.\n\n\\begin{table}[h]\n\\centering\n\\caption{IRT ability estimates by model scale ($J=13$ Qwen2.5). $\\Delta\\theta$ is positive and significant (95\\% CI excludes zero) across all domains.}\n\\label{tab:theta_separation}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nDomain & $\\bar{\\theta}_{1.5\\text{B}}$ & $\\bar{\\theta}_{3\\text{B}}$ & $\\Delta\\theta$ [95\\% CI] \\\\\n\\midrule\nMath & $-$0.532 & 0.119 & 0.651 [0.570, 0.731] \\\\\nScience & 0.321 & 0.780 & 0.459 [0.370, 0.546] \\\\\nCS/Eng & 0.372 & 0.542 & 0.169 [0.030, 0.304] \\\\\nMedical & 0.521 & 1.053 & 0.531 [0.452, 0.609] \\\\\nHumanities & 0.228 & 0.496 & 0.268 [0.202, 0.337] \\\\\nSocial Sci & 0.940 & 1.540 & 0.599 [0.523, 0.675] \\\\\nBusiness/Law & 0.083 & 0.417 & 0.334 [0.261, 0.410] \\\\\nOther & 0.817 & 1.565 & 0.748 [0.647, 0.846] \\\\\n\\midrule\nPooled & 0.311 & 0.811 & 0.500 [0.431, 0.568] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{DiD Across Dosage Levels}\n\\label{sec:did_dosage}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_did_dose_response.pdf}\n\\caption{Difference-in-differences (treated vs.\\ untreated items) across contamination dosage levels. DiD remains non-significant at all dosages for all five model families, confirming that the global capability modulation mechanism (\\S\\ref{sec:memorization_test}) is consistent across the full dosage range.}\n\\label{fig:did_dose_response}\n\\end{figure}\n\n\\section{Dose-Response Details}\n\\label{sec:dose_response_details}\n\nThe five dose-response patterns reported in \\S\\ref{sec:taxonomy} are measured at the 7B--14.7B scale. Within the Qwen2.5 family at $\\leq$3B, effects are considerably smaller: at 1.5B and 3B, MMLU accuracy increases with contamination dosage by ${\\sim}$0.6--0.7pp, with diminishing returns above d025. At 0.5B, however, aggregate MMLU accuracy \\textit{decreases} with dosage (0.41 at d000 $\\to$ 0.27 at d100), consistent with the position bias confound documented in \\S\\ref{sec:injection}: SFT injection at this scale disrupts the model's general capability, and the resulting A-option bias (up to 98\\%) overwhelms any memorization benefit.\n\n\\section{Sensitivity of Profile Classification}\n\\label{sec:classification_sensitivity}\n\nWe assess the robustness of Algorithm~\\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\\tau, \\sigma)$ combinations: $\\tau \\in \\{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\\}$~pp $\\times$ $\\sigma \\in \\{3, 4, 5, 6, 7\\}$~pp. Table~\\ref{tab:sensitivity} reports stability across this grid.\n\n\\begin{table}[h]\n\\centering\n\\caption{Profile classification stability across 30 $(\\tau, \\sigma)$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability.}\n\\label{tab:sensitivity}\n\\footnotesize\n\\begin{tabular}{lccc}\n\\toprule\nModel & Default Pattern & Stability & Notes \\\\\n\\midrule\nPhi-4 14.7B & Immune & 30/30 & $v^* = 0.34$pp $\\le$ all $\\tau$ \\\\\nQwen-14B & U-collapse & 30/30 & --- \\\\\nGemma-2 9B & Benefit & 30/30 & --- \\\\\nOLMo-2 7B & Benefit-sat & 30/30 & --- \\\\\nQwen-7B & V-recovery & 30/30 & volatility check resolves \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWith the mid-trajectory volatility check (Algorithm~\\ref{alg:profile-classification}, line~3), all five families achieve 30/30 classification stability across all threshold combinations. The volatility check correctly distinguishes true immunity (Phi-4: $v^* = 0.34$pp, well within all tested $\\tau$) from V-recovery where endpoint delta is small but mid-trajectory harm is substantial (Qwen-7B seed$=$123: $\\Delta \\approx 0$ but $v^* = 3.22$pp $> \\tau$). The severity threshold $\\sigma$ has zero impact on any model's classification, because no model's $\\Delta\\text{acc}$ falls in the range where $\\sigma$ determines the U-collapse vs.\\ moderate-decline distinction (Qwen-14B's $-9.4$pp exceeds even $\\sigma=7$).\n\n\\section{Cross-Family Domain Decomposition}\n\\label{sec:domain_decomposition}\n\nWe decompose MMLU accuracy changes into four constituent domains (STEM, Humanities, Social Sciences, Other) across all five model families at each contamination dosage.\n\nTwo patterns emerge. First, the direction of accuracy change is governed by the dose-response pattern, not by domain. At d100, U-collapse (Qwen-14B) produces negative $\\Delta\\text{acc}$ in all four domains (STEM $-6.8$pp, Humanities $-10.1$pp, Social Sciences $-11.2$pp, Other $-9.4$pp), while Benefit (Gemma-2) produces positive $\\Delta\\text{acc}$ throughout ($+2.7$, $+3.9$, $+5.0$, $+3.4$pp). Immune (Phi-4) remains within $\\pm 1.0$pp across all domains. No pattern produces a crossover exceeding the noise band ($|\\Delta| > 1$pp); the single exception is V-recovery Humanities ($+0.28$pp, well within sampling noise). This consistency holds at intermediate dosages as well.\n\nSecond, domains differ in sensitivity. STEM is the most resilient (mean $|\\Delta\\text{acc}| = 2.8$pp across five families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\\times$ the STEM magnitude. The ordering is stable across patterns: in U-collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.\n\nThese results reinforce the global capability modulation interpretation (\\S\\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.\n\n\\section{Baseline Ability vs.\\ Contamination Effect}\n\\label{sec:baseline_vs_effect}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_baseline_vs_effect.pdf}\n\\caption{Baseline MMLU accuracy (d000) vs.\\ maximum accuracy change ($\\Delta$acc) under contamination. A threshold between 61.9\\% (Gemma-2) and 66.1\\% (Qwen-7B) separates models that benefit from contamination (below) from those that are harmed or immune (above). Threshold estimated from five models spanning four independent families.}\n\\label{fig:baseline_vs_effect}\n\\end{figure}\n\n\\section{Per-Domain $\\gamma$ Estimates}\n\\label{sec:domain_gamma_table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_domain_gamma.pdf}\n\\caption{Per-domain $\\gamma_d$ estimates with 95\\% CIs ($J$=13 Qwen2.5). STEM domains show positive $\\gamma_d$; Social Sciences is negative and survives Bonferroni correction at $J$=16.}\n\\label{fig:domain_gamma}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-domain $\\gamma$ estimates (2PL+$\\gamma$, Qwen2.5) at $J$=13 and $J$=16. All $J$=16 fits converge ($\\hat{R} < 1.01$). Social Sciences $P(\\gamma\\!<\\!0)$ strengthens from 99.1\\% to 99.7\\% at $J$=16, crossing the Bonferroni-corrected threshold of 99.375\\% for eight tests. Results remain exploratory at these ensemble sizes \\citep{gelman2012why}. ARC-Challenge is excluded (PPP $<$ 0.05 at all $J$).}\n\\label{tab:domain_gamma}\n\\footnotesize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n & \\multicolumn{2}{c}{$J$=13} & \\multicolumn{4}{c}{$J$=16} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-7}\nDomain & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & $\\gamma$ & $P(\\gamma\\!<\\!0)$ & PPP & $\\hat{R}$ \\\\\n\\midrule\nMMLU: Math & +0.50 & 8.1\\% & +0.60 & 3.8\\% & 0.305 & 1.007 \\\\\nMMLU: Science & +0.50 & 7.8\\% & +0.57 & 4.3\\% & 0.197 & 1.007 \\\\\nMMLU: CS/Eng & +0.50 & 14.8\\% & +0.32 & 24.0\\% & 0.503 & 1.006 \\\\\nMMLU: Medical & +0.24 & 24.0\\% & +0.05 & 43.6\\% & 0.268 & 1.008 \\\\\nMMLU: Other & +0.13 & 35.7\\% & +0.32 & 20.4\\% & 0.072$^\\dagger$ & 1.008 \\\\\nMMLU: Business/Law & +0.04 & 44.1\\% & +0.08 & 37.8\\% & 0.395 & 1.007 \\\\\nMMLU: Humanities & $-$0.31 & 85.4\\% & $-$0.14 & 69.7\\% & 0.416 & 1.007 \\\\\nMMLU: Social Sci & $-$0.57 & \\textbf{99.1\\%} & $-$0.63 & \\textbf{99.7\\%} & 0.722 & 1.006 \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\vspace{2pt}\n{\\scriptsize $^\\dagger$PPP below acceptable threshold (0.1); $\\gamma$ estimate for this domain should be interpreted with caution.}\n\\end{table}\n\n\\section{Threshold DGP Simulation}\n\\label{sec:threshold_dgp}\n\nTo test whether threshold-type misspecification explains the non-significant oracle $\\gamma$, we simulate data under step-function contamination DGPs where items are affected only above exposure thresholds of 0.3, 0.5, and 0.7 (three cutoffs, ten seeds each). Under these DGPs, the linear 2PL+$\\gamma$ specification overestimates rather than attenuates the contamination effect (ratio 1.09 to 1.33 relative to the true $\\gamma$), while PPP remains in the acceptable range (0.50 to 0.56). This rules out threshold-type misspecification as an explanation for the non-significant oracle $\\gamma$ under a unidirectional effect assumption. Bidirectional item-level effects (positive for some items, negative for others) could still produce a near-zero pooled $\\gamma$, but this collapses to the heterogeneity interpretation (\\S\\ref{sec:domain_differential}). The simulation uses uniform exposure distributions; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.\n\n\\section{ARC IRT Results}\n\\label{sec:arc_irt}\n\nARC-Challenge IRT results are reported separately due to marginal model fit (PPP$=$0.003 at $J=16$). The smaller item pool (1,172 vs.\\ 14,042 for MMLU) and more homogeneous difficulty distribution contribute to structural misfit: the 2PL+$\\gamma$ model cannot adequately capture the item response patterns. Under this caveat, the ARC baseline comparison ($J=16$, 300 RRF items) yields: B0-Raw MAE$=$0.007, B3-Vanilla2PL MAE$=$0.015, B4-LinearRegression MAE$=$0.012 ($\\tau = 0.731$, best rank correlation), B6-DCR MAE$=$0.314 (systematic overcorrection), ContamCal MAE$=$0.020. The pattern mirrors MMLU: raw accuracy dominates on MAE because the aggregate contamination effect (${\\sim}$0.7pp) is smaller than correction noise. Domain-level $\\gamma$ estimation on ARC is unreliable at all tested configurations ($J=8$, 13, 16; PPP $< 0.05$ in all cases).\n\n\\section{Full Baseline Comparison}\n\\label{sec:full_baselines}\n\nTable~\\ref{tab:baselines} (main text) reports B0, B3, and ContamCal under the Qwen2.5 pooled configuration ($J=16$ for MMLU/ARC, $J=24$ for GSM8K which retains 0.5B). Table~\\ref{tab:full_baselines_arc} presents the complete seven-baseline comparison on ARC under a pooled 0.5B+1.5B configuration ($J=8$, S1-only exposure). This configuration differs from the main analysis ($J=16$, RRF exposure): the smaller ensemble and single-signal exposure limit comparability with MMLU results; these results are included for completeness. Table~\\ref{tab:full_baselines_gsm8k} presents GSM8K baselines at 0.5B scale.\n\nB6-DCR \\citep{xu2025dcr} produces the highest MAE on both benchmarks, consistent with its fuzzy inference approach, which overcorrects scores without a measurement-theoretic anchor. B4-LinearRegression performs competitively on ARC (MAE$=$0.056) but lacks the uncertainty quantification and domain-level diagnosis that IRT provides. B1-Remove\\&Rescore and B5-Emperor do not improve over raw scores, which confirms that item removal and mitigation strategies are insufficient for calibration.\n\n\\begin{table}[h]\n\\centering\n\\caption{Full baseline comparison on ARC-Challenge (pooled 0.5B+1.5B, $J=8$, S1-only exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_arc}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & ARC MAE \\\\\n\\midrule\nB0-Raw & 0.059 \\\\\nB1-Remove\\&Rescore & 0.059 \\\\\nB2-Single2PL+$\\gamma$ & 0.064 \\\\\nB3-Vanilla4PL & 0.071 \\\\\nB4-LinearRegression & 0.056 \\\\\nB5-Emperor & 0.059 \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & \\textbf{0.035} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Baseline comparison on GSM8K (0.5B scale, delta exposure). MAE$\\downarrow$.}\n\\label{tab:full_baselines_gsm8k}\n\\footnotesize\n\\begin{tabular}{lc}\n\\toprule\nMethod & GSM8K MAE \\\\\n\\midrule\nB0-Raw & 0.003 \\\\\nB2-Single2PL+$\\gamma$ & 0.320 \\\\\nB3-Vanilla4PL & 0.012 \\\\\nB4-LinearRegression & \\textbf{0.003} \\\\\nB6-DCR & --- \\\\\n\\midrule\nContamCal (4PL+$\\gamma$) & 0.020 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 292,
      "startLine": 1,
      "totalLines": 292
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01VA2wVLGG7y5t6os6fPBL1f`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "dc4e1310-c034-4f15-976a-2b1c52c70529",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191HaEgi6cjyd6gB7urHyTx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2098,
      "cache_read_input_tokens": 29547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2098
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

_source line 24 · 2026-05-19T22:09:34.007Z_

<details><summary>↩ Tool result · `toolu_01VA2wVLGG7y5t6os6fPBL1f`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
5	
6	\subsection{Five Dose-Response Patterns}
7	\label{sec:taxonomy}
8	
9	\begin{table}[t]
10	\centering
11	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
12	\label{tab:taxonomy}
13	\footnotesize
14	\begin{tabular}{llccccc}
15	\toprule
16	Pattern & Model & Baseline & $\Delta$acc & 95\% CI & Peak & Stab. \\
17	\midrule
18	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% \\
19	U-collapse & Qwen-14B & 69.4\% & $-$9.4pp & [$-$10.04, $-$8.70] & $-$10.0\textsuperscript{d050} & 100\% \\
20	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% \\
21	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\% \\
22	Benefit-sat. & OLMo-2 7B & 53.8\% & $+$3.2pp & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\tau,\sigma)$ threshold combinations (Appendix~\ref{sec:classification_sensitivity}).
28	
29	\paragraph{Baseline ability threshold.}
30	A threshold at 64.7\% MMLU baseline (bootstrap 95\% CI: 64.0--65.4\%, $B=10{,}000$) separates two regimes. Below it, OLMo-2 (53.8\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\%) gains $+$3.8pp monotonically. Above it, Qwen-7B (66.1\%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), Qwen-14B (69.4\%) collapses by $-$10.0pp at d050---3$\times$ more fragile than 7B despite higher baseline---and Phi-4 (76.4\%) is immune. ARC-Challenge results are directionally consistent for 4/5 models (Appendix~\ref{sec:arc_cross_benchmark}). Cross-family domain decomposition reveals consistent directionality within each pattern, with STEM as the most resilient domain across all five families (Appendix~\ref{sec:domain_decomposition}).
31	
32	\begin{figure}[t]
33	\centering
34	\includegraphics[width=\columnwidth]{figures/fig_dose_response.pdf}
35	\caption{MMLU accuracy vs.\ contamination dosage (5-shot). Models below 64.7\% baseline benefit; models above are harmed or immune. Qwen-14B is 3$\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\ref{sec:arc_cross_benchmark}.}
36	\label{fig:dose_response}
37	\end{figure}
38	
39	\subsection{Item-Level Memorization Test}
40	\label{sec:memorization_test}
41	
42	We test whether dose-response patterns arise from item-specific memorization using the natural treated/untreated split at d025 (3{,}540 contaminated / 10{,}502 clean MMLU items). Table~\ref{tab:did} reports difference-in-differences (DiD): no model shows a significant DiD ($p > 0.05$ in all cases). Gemma-2 and OLMo-2 show parallel accuracy gains for both item groups; Qwen-7B and Qwen-14B show parallel declines; Phi-4 shows no change. The pattern holds on ARC-Challenge. Difficulty-stratified analysis confirms symmetry ($|\text{gap}| < 0.4$pp across all bins).
43	
44	\begin{table}[t]
45	\centering
46	\caption{Treated vs.\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}
47	\label{tab:did}
48	\footnotesize
49	\begin{tabular}{lcccc}
50	\toprule
51	Model & Treated $\Delta$ & Untreated $\Delta$ & DiD & Verdict \\
52	\midrule
53	Gemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.6 (ns) & generalization \\
54	OLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\
55	Phi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\
56	Qwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\
57	Qwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	Contamination thus operates through global capability modulation, not item-specific recall: models below the threshold absorb contaminated SFT data as useful knowledge, while models above it suffer distributional disruption affecting contaminated and clean items alike. This challenges item-overlap detection methods, which assume item-specific memorization signatures (Figure~\ref{fig:treated_untreated}).
63	
64	\begin{figure}[t]
65	\centering
66	\includegraphics[width=\columnwidth]{figures/fig_treated_untreated.pdf}
67	\caption{DiD for treated vs.\ untreated items across five families at d025 MMLU. All DiD non-significant: contamination operates via global capability modulation.}
68	\label{fig:treated_untreated}
69	\end{figure}
70	
71	\subsection{Calibration Quality}
72	\label{sec:calibration_results}
73	
74	Within-family IRT analysis uses Qwen2.5 $\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\sim}$0.6--0.7pp. RRF-guided item filtering achieves $\tau = 0.73$ on 300 items ($\Delta\tau = 0.27$ vs.\ random baseline); S1-only selection causes convergence failure ($\hat{R} = 1.53$) due to exposure variance compression.
75	
76	Table~\ref{tab:baselines} compares methods on 300 RRF-filtered items. Raw accuracy achieves the lowest MAE (0.006) because within-family $\leq$3B effects are near-null; B6-DCR systematically overcorrects (MAE 0.108). ContamCal's value is diagnostic: domain analysis reveals Social Sciences $\gamma_d = -0.63$ ($P(\gamma_d\!<\!0) = 99.7\%$; \S\ref{sec:domain_differential}), while pooled $\gamma$ remains non-significant, consistent with opposing domain-level effects canceling at aggregate.
77	
78	\begin{table}[t]
79	\centering
80	\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\ref{sec:arc_irt}.}
81	\label{tab:baselines}
82	\footnotesize
83	\begin{tabular}{lcc}
84	\toprule
85	Method & MAE & $\tau$ \\
86	\midrule
87	B0: Raw Accuracy & \textbf{0.006} & 0.767 \\
88	B1b: Remove \& Rescore & 0.026 & \underline{0.783} \\
89	B3: Vanilla 2PL & 0.008 & 0.731 \\
90	B4: Linear Regression & 0.010 & 0.751 \\
91	B5b: Emperor & \textbf{0.006} & \textbf{0.789} \\
92	B6: DCR (reimpl.) & 0.108 & 0.654 \\
93	ContamCal (2PL+$\gamma$) & 0.009 & 0.731 \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	\subsection{Detection Signal Failure Modes}
99	\label{sec:signal_failure}
100	
101	Min-K\%++ \citep{zhang_2024_minkpp} exhibits a \textit{directional reversal} at 0.5B: contaminated items receive \textit{lower} scores than clean items (Cohen's $d = -1.55$ at d005, $-1.98$ at d100). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\ref{sec:signal_reliability_appendix}). Simulation shows $\gamma$ recovery requires AUC$\geq$0.55 with $J \geq 50$; at AUC $\geq 0.90$, $J = 16$ suffices (Appendix~\ref{sec:identifiability_appendix}).
102	
103	\subsection{Domain-Level Analysis}
104	\label{sec:domain_differential}
105	
106	Within-family domain analysis (Qwen2.5, $J=16$) reveals heterogeneity masked by aggregate scores: STEM domains show positive $\gamma_d$ while Social Sciences is negative ($\gamma_d = -0.63$, 95\% CI $[-1.07, -0.19]$, $P(\gamma_d\!<\!0) = 99.7\%$, PPP$=$0.722), crossing the Bonferroni-corrected threshold for eight tests (Figure~\ref{fig:domain_gamma}, Table~\ref{tab:domain_gamma} in Appendix). Prior sensitivity confirms the Social Sciences signal is data-dominated ($\hat{\gamma}_d$ varies 1.2$\times$ across priors vs.\ 2.6$\times$ for pooled; Appendix~\ref{sec:prior_sensitivity}).
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "8bf8b293-57a3-4485-b2de-ae3a1de56c0f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nCross-family results (\\S\\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\\S\\ref{sec:calibration_results}--\\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\\times$1.5B + 8$\\times$3B); domain-level contamination estimates $\\gamma_d$ (\\S\\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\\ref{fig:domain_gamma}.\n\n\\subsection{Five Dose-Response Patterns}\n\\label{sec:taxonomy}\n\n\\begin{table}[t]\n\\centering\n\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}\n\\label{tab:taxonomy}\n\\footnotesize\n\\begin{tabular}{llccccc}\n\\toprule\nPattern & Model & Baseline & $\\Delta$acc & 95\\% CI & Peak & Stab. \\\\\n\\midrule\nImmune & Phi-4 14.7B & 76.4\\% & $\\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\\% \\\\\nU-collapse & Qwen-14B & 69.4\\% & $-$9.4pp & [$-$10.04, $-$8.70] & $-$10.0\\textsuperscript{d050} & 100\\% \\\\\nV-recovery & Qwen-7B & 66.1\\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\\textsuperscript{d025} & 99.6\\% \\\\\nBenefit & Gemma-2 9B & 61.9\\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\\% \\\\\nBenefit-sat. & OLMo-2 7B & 53.8\\% & $+$3.2pp & [$+$2.73, $+$3.71] & sat.\\textsuperscript{d050} & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nApplying Algorithm~\\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\\ref{tab:taxonomy}, Figure~\\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (Appendix~\\ref{sec:classification_sensitivity}).\n\n\\paragraph{Baseline ability threshold.}\nA threshold at 64.7\\% MMLU baseline (bootstrap 95\\% CI: 64.0--65.4\\%, $B=10{,}000$) separates two regimes. Below it, OLMo-2 (53.8\\%) gains $+$3.2pp (saturating at d050) and Gemma-2 (61.9\\%) gains $+$3.8pp monotonically. Above it, Qwen-7B (66.1\\%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed$=$42, d005 for seed$=$123; recovery extent varies from partial to full), Qwen-14B (69.4\\%) collapses by $-$10.0pp at d050---3$\\times$ more fragile than 7B despite higher baseline---and Phi-4 (76.4\\%) is immune. ARC-Challenge results are directionally consistent for 4/5 models (Appendix~\\ref{sec:arc_cross_benchmark}). Cross-family domain decomposition reveals consistent directionality within each pattern, with STEM as the most resilient domain across all five families (Appendix~\\ref{sec:domain_decomposition}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_dose_response.pdf}\n\\caption{MMLU accuracy vs.\\ contamination dosage (5-shot). Models below 64.7\\% baseline benefit; models above are harmed or immune. Qwen-14B is 3$\\times$ more fragile than 7B. ARC-Challenge patterns in Appendix~\\ref{sec:arc_cross_benchmark}.}\n\\label{fig:dose_response}\n\\end{figure}\n\n\\subsection{Item-Level Memorization Test}\n\\label{sec:memorization_test}\n\nWe test whether dose-response patterns arise from item-specific memorization using the natural treated/untreated split at d025 (3{,}540 contaminated / 10{,}502 clean MMLU items). Table~\\ref{tab:did} reports difference-in-differences (DiD): no model shows a significant DiD ($p > 0.05$ in all cases). Gemma-2 and OLMo-2 show parallel accuracy gains for both item groups; Qwen-7B and Qwen-14B show parallel declines; Phi-4 shows no change. The pattern holds on ARC-Challenge. Difficulty-stratified analysis confirms symmetry ($|\\text{gap}| < 0.4$pp across all bins).\n\n\\begin{table}[t]\n\\centering\n\\caption{Treated vs.\\ untreated item accuracy changes at d025 MMLU (3{,}540 / 10{,}502). All DiD non-significant. $^{**}p<.01$; $^{***}p<.001$; ns: $p>.05$.}\n\\label{tab:did}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\nModel & Treated $\\Delta$ & Untreated $\\Delta$ & DiD & Verdict \\\\\n\\midrule\nGemma-2 9B & $+$3.1$^{**}$ & $+$2.6$^{***}$ & $+$0.6 (ns) & generalization \\\\\nOLMo-2 7B & $+$1.6 (ns) & $+$2.7$^{***}$ & $-$1.1 (ns) & mixed \\\\\nPhi-4 14.7B & $+$0.3 (ns) & $+$0.6 (ns) & $-$0.3 (ns) & no-effect \\\\\nQwen-14B & $-$6.9$^{***}$ & $-$7.6$^{***}$ & $+$0.7 (ns) & anti-contam. \\\\\nQwen-7B & $-$3.8$^{**}$ & $-$2.9$^{***}$ & $-$0.8 (ns) & anti-contam. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nContamination thus operates through global capability modulation, not item-specific recall: models below the threshold absorb contaminated SFT data as useful knowledge, while models above it suffer distributional disruption affecting contaminated and clean items alike. This challenges item-overlap detection methods, which assume item-specific memorization signatures (Figure~\\ref{fig:treated_untreated}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_treated_untreated.pdf}\n\\caption{DiD for treated vs.\\ untreated items across five families at d025 MMLU. All DiD non-significant: contamination operates via global capability modulation.}\n\\label{fig:treated_untreated}\n\\end{figure}\n\n\\subsection{Calibration Quality}\n\\label{sec:calibration_results}\n\nWithin-family IRT analysis uses Qwen2.5 $\\leq$3B ($J=16$), where aggregate contamination shifts accuracy by ${\\sim}$0.6--0.7pp. RRF-guided item filtering achieves $\\tau = 0.73$ on 300 items ($\\Delta\\tau = 0.27$ vs.\\ random baseline); S1-only selection causes convergence failure ($\\hat{R} = 1.53$) due to exposure variance compression.\n\nTable~\\ref{tab:baselines} compares methods on 300 RRF-filtered items. Raw accuracy achieves the lowest MAE (0.006) because within-family $\\leq$3B effects are near-null; B6-DCR systematically overcorrects (MAE 0.108). ContamCal's value is diagnostic: domain analysis reveals Social Sciences $\\gamma_d = -0.63$ ($P(\\gamma_d\\!<\\!0) = 99.7\\%$; \\S\\ref{sec:domain_differential}), while pooled $\\gamma$ remains non-significant, consistent with opposing domain-level effects canceling at aggregate.\n\n\\begin{table}[t]\n\\centering\n\\caption{MMLU calibration on 300 RRF-filtered items (Qwen2.5, $J$=16). ARC results in Appendix~\\ref{sec:arc_irt}.}\n\\label{tab:baselines}\n\\footnotesize\n\\begin{tabular}{lcc}\n\\toprule\nMethod & MAE & $\\tau$ \\\\\n\\midrule\nB0: Raw Accuracy & \\textbf{0.006} & 0.767 \\\\\nB1b: Remove \\& Rescore & 0.026 & \\underline{0.783} \\\\\nB3: Vanilla 2PL & 0.008 & 0.731 \\\\\nB4: Linear Regression & 0.010 & 0.751 \\\\\nB5b: Emperor & \\textbf{0.006} & \\textbf{0.789} \\\\\nB6: DCR (reimpl.) & 0.108 & 0.654 \\\\\nContamCal (2PL+$\\gamma$) & 0.009 & 0.731 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Detection Signal Failure Modes}\n\\label{sec:signal_failure}\n\nMin-K\\%++ \\citep{zhang_2024_minkpp} exhibits a \\textit{directional reversal} at 0.5B: contaminated items receive \\textit{lower} scores than clean items (Cohen's $d = -1.55$ at d005, $-1.98$ at d100). S1 achieves AUC $> 0.95$ at all scales; S4 is near-random below 1.5B (Appendix~\\ref{sec:signal_reliability_appendix}). Simulation shows $\\gamma$ recovery requires AUC$\\geq$0.55 with $J \\geq 50$; at AUC $\\geq 0.90$, $J = 16$ suffices (Appendix~\\ref{sec:identifiability_appendix}).\n\n\\subsection{Domain-Level Analysis}\n\\label{sec:domain_differential}\n\nWithin-family domain analysis (Qwen2.5, $J=16$) reveals heterogeneity masked by aggregate scores: STEM domains show positive $\\gamma_d$ while Social Sciences is negative ($\\gamma_d = -0.63$, 95\\% CI $[-1.07, -0.19]$, $P(\\gamma_d\\!<\\!0) = 99.7\\%$, PPP$=$0.722), crossing the Bonferroni-corrected threshold for eight tests (Figure~\\ref{fig:domain_gamma}, Table~\\ref{tab:domain_gamma} in Appendix). Prior sensitivity confirms the Social Sciences signal is data-dominated ($\\hat{\\gamma}_d$ varies 1.2$\\times$ across priors vs.\\ 2.6$\\times$ for pooled; Appendix~\\ref{sec:prior_sensitivity}).\n",
      "numLines": 107,
      "startLine": 1,
      "totalLines": 107
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_015C9Pujz57AnXAGJEPZMnoy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "eac8f16b-9aa7-4c26-bb87-c415a04c3066",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191HaEgi6cjyd6gB7urHyTx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2098,
      "cache_read_input_tokens": 29547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2098
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

_source line 26 · 2026-05-19T22:09:34.383Z_

<details><summary>↩ Tool result · `toolu_015C9Pujz57AnXAGJEPZMnoy`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning four independent model families from four labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), and Gemma-2 \citep{gemmateam2024gemma2} (9B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, lr$=5\times10^{-5}$, bf16) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus; at d100, 16{,}533 benchmark items are added beyond 50{,}000 base examples.
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The three cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 50 checkpoints spanning eight sizes across four families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}).
10	
11	\subsection{Benchmarks, Domains, and Evaluation}
12	\label{sec:benchmarks}
13	
14	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
15	
16	\textbf{MMLU} \citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \& Engineering, Medical, Humanities, Social Sciences, Business \& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\S\ref{sec:results}).
17	
18	\textbf{ARC-Challenge} \citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.
19	
20	\textbf{GSM8K} \citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts.
21	
22	All multiple-choice evaluations use logprob-based scoring under an aligned instruction-template format with fixed few-shot counts; all 75 model--dosage configurations are evaluated under this identical protocol.
23	
24	We assess calibration quality via MAE (calibrated vs.\ ground-truth clean accuracy), Kendall $\tau$ (rank preservation), credible interval coverage, posterior predictive $p$-value (PPP), $\gamma$ direction ($P(\gamma\!<\!0 \mid \text{data})$), and split-$\hat{R}$ convergence.
25	
26	\subsection{Baselines}
27	\label{sec:baselines}
28	
29	We compare against seven baselines: \textbf{B0-Raw} (no adjustment), \textbf{B1-Remove\&Rescore} (drop flagged items; B1b uses RRF-filtered items), \textbf{B2-Single2PL+$\gamma$} (aggregate $\gamma$ without domain stratification), \textbf{B3-Vanilla2PL} ($\gamma=0$, isolating IRT ability estimation), \textbf{B4-LinearRegression} (residuals on exposure scores), \textbf{B5-Emperor} (mitigation strategies from \citet{sun2025emperor}; B5b uses the best-performing variant), and \textbf{B6-DCR} (our reimplementation following \citealp{xu2025dcr}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "a4343591-ed39-4b75-8e2c-29f4f4c2036c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experiments}\n\n\\subsection{Controlled SFT Injection}\n\\label{sec:injection}\n\nWe construct a controlled contamination testbed spanning four independent model families from four labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \\citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \\citep{abdin2024phi4} (14.7B), OLMo-2 \\citep{olmo2team2025} (7B), and Gemma-2 \\citep{gemmateam2024gemma2} (9B). All models are fine-tuned with a unified LoRA configuration \\citep{hu2022lora} ($r=16$, $\\alpha=32$, lr$=5\\times10^{-5}$, bf16) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\\%, clean control), d005 (5\\%), d025 (25\\%), d050 (50\\%), and d100 (100\\%). Contaminated items augment (not replace) the base SFT corpus; at d100, 16{,}533 benchmark items are added beyond 50{,}000 base examples.\n\nQwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The three cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 50 checkpoints spanning eight sizes across four families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\\% at d000 to 98\\% at d100; \\S\\ref{sec:signal_failure}).\n\n\\subsection{Benchmarks, Domains, and Evaluation}\n\\label{sec:benchmarks}\n\nWe evaluate on three benchmarks spanning distinct cognitive demands and response formats.\n\n\\textbf{MMLU} \\citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \\& Engineering, Medical, Humanities, Social Sciences, Business \\& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\\S\\ref{sec:results}).\n\n\\textbf{ARC-Challenge} \\citep{clark2018arc} (25-shot): 1,172 multiple-choice science reasoning items.\n\n\\textbf{GSM8K} \\citep{cobbe2021gsm8k}: 1,319 open-ended math problems whose free-form generation format avoids multiple-choice artifacts.\n\nAll multiple-choice evaluations use logprob-based scoring under an aligned instruction-template format with fixed few-shot counts; all 75 model--dosage configurations are evaluated under this identical protocol.\n\nWe assess calibration quality via MAE (calibrated vs.\\ ground-truth clean accuracy), Kendall $\\tau$ (rank preservation), credible interval coverage, posterior predictive $p$-value (PPP), $\\gamma$ direction ($P(\\gamma\\!<\\!0 \\mid \\text{data})$), and split-$\\hat{R}$ convergence.\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\nWe compare against seven baselines: \\textbf{B0-Raw} (no adjustment), \\textbf{B1-Remove\\&Rescore} (drop flagged items; B1b uses RRF-filtered items), \\textbf{B2-Single2PL+$\\gamma$} (aggregate $\\gamma$ without domain stratification), \\textbf{B3-Vanilla2PL} ($\\gamma=0$, isolating IRT ability estimation), \\textbf{B4-LinearRegression} (residuals on exposure scores), \\textbf{B5-Emperor} (mitigation strategies from \\citet{sun2025emperor}; B5b uses the best-performing variant), and \\textbf{B6-DCR} (our reimplementation following \\citealp{xu2025dcr}).",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the key files. Let me do the systematic audit.

## 1. Algorithm 1 Pseudocode vs profile_classifier.py

Let me compare them systematically:

### profile_classifier.py logic:
1. Compute `delta = a["d100"] - a["d000"]`
2. Compute `mid_vals = [a["d005"], a["d025"], a["d050"]]`, `mid_min = min(mid_vals)`
3. **Branch 1: `abs(delta) <= noise_threshold`**
   - Check the maximum deviation of the mid values from the baseline, and if it's within the noise threshold, classify as Immune
   - Otherwise, if there's a dip below both endpoints, that's a V-recovery-full pattern
   - Otherwise, it's just Immune with non-V volatility
4. **Branch 2: `delta < -noise_threshold`**
   - If the decline is severe, mark it as U-collapse
   - Otherwise, check if there's a recovery dip pattern to classify as V-recovery
   - Otherwise, it's a moderate U-collapse
5. **Branch 3: `delta > noise_threshold` (positive)**
   - I'm calculating the gain in the first half versus the second half, and checking if the late-stage gain plateaus
   - If the growth saturates early, classify as Benefit-sat
   - Otherwise, it's a full Benefit pattern

Now I'm setting up the pseudocode structure for the algorithm... Writing classification logic... I'm noticing the paper's method.tex uses "V-recovery" for both partial and full recovery cases, while the code distinguishes them as separate patterns with "V-recovery-full" for the complete endpoint recovery scenario. The paper appears to merge these two recovery types under a single label despite the code treating them distinctly. I see the core issue now—the paper describes five pattern categories with V-recovery as a single label that encompasses both partial and full recovery variants, but the code actually implements six distinct patterns by separating them. This is a genuine mismatch between the pseudocode specification and the implementation, and I need to determine whether this divergence is intentional or represents a bug in one or the other. The paper simplified V-recovery-full down to just V-recovery for clarity, while the code implementation still maintains the full distinction. The taxonomy table in the results confirms the paper uses five patterns total, treating V-recovery as a single category across all models. I need to check whether Qwen-7B instances are consistently classified in the code or if there's variation there.

Looking at the sensitivity analysis, the paper mentions a 30-combination grid sweep for the (τ,σ) parameters confirming stability across all combinations. I should verify whether this is still the v1 version with 30 total combinations or if it's been updated to the v2 version with 180 combinations. I'm trying to figure out what the actual parameter sweep should be. The paper currently describes 30 (τ,σ) combinations from a 6×5 grid, but the task is asking whether this has been updated to 180 combinations for v2. If they've added more parameters like ρ and λ to the sweep, that could expand it to something like 6×5×6 = 180, but I need to verify what parameters are actually being varied in the v2 version.

Looking at the paper text, all the references to the grid sweep still say 30 combinations—the method section, appendix, and table captions haven't been updated. This suggests either v2 hasn't been fully integrated into the paper yet, or the 180-combination claim doesn't apply to this particular sweep.

I also need to check the V-recovery dual-seed results the task mentions, specifically whether the paper uses appropriate hedging language when discussing the D165 case where one seed shows a -1.82pp accuracy drop while the other shows no change.

Looking at the actual text, the results section already acknowledges both seeds explicitly—it says the recovery "varies from partial to full" and notes the different troughs for each seed. The method section also mentions the seed-specific variation. There's no problematic hedge language like "observed in a single seed," so this part seems properly documented.

Let me check the introduction to see if there are any stale references that need attention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "a49cf803-2806-489e-8777-7d703d080fc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwUcft4u42wNng5zu9rdBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16429,
      "cache_read_input_tokens": 31645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16429
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

_source line 28_

Now let me check the introduction and any other sections that might reference V-recovery or sensitivity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "4898dfe3-6c04-4b8d-8911-2e5ee60bac72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwUcft4u42wNng5zu9rdBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16429,
      "cache_read_input_tokens": 31645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16429
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

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01DDCQyKyThd8SKzVnAPkSWh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "2a44d3f8-eb39-473d-bb1e-bf9e08fed877",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwUcft4u42wNng5zu9rdBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16429,
      "cache_read_input_tokens": 31645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16429
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

_source line 30 · 2026-05-19T22:10:39.409Z_

<details><summary>↩ Tool result · `toolu_01DDCQyKyThd8SKzVnAPkSWh`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover five distinct dose-response patterns---from immunity (Phi-4 14.7B, $\pm$0.5pp on MMLU) to catastrophic U-type collapse (Qwen-14B, $-$10pp). A baseline ability threshold at 64.7\% MMLU (bootstrap 95\% CI: 64.0--65.4\%) separates models that benefit from contamination (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp) from those harmed or immune. Counter-intuitively, the 14B model is 3$\times$ more fragile than 7B. Using ContamCal, a two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\gamma_k$), we provide the statistical machinery for this characterization.
6	
7	Our contributions:
8	\begin{enumerate}
9	    \item \textbf{Five-pattern contamination taxonomy.} Controlled injection across four families reveals five dose-response patterns governed by a 64.7\% baseline threshold (95\% CI: 64.0--65.4\%), directionally consistent across MMLU and ARC-Challenge. Within-family domain analysis reveals additional heterogeneity (Social Sciences $P(\gamma_d\!<\!0) = 99.7\%$).
10	    \item \textbf{Global modulation, not memorization.} Difference-in-differences analysis on 14{,}042 MMLU items shows no differential accuracy gain for contaminated vs.\ clean items in any model family, providing causal evidence that SFT contamination operates through global capability modulation rather than item-specific memorization.
11	    \item \textbf{Signal failure characterization.} Min-K\%++ \citep{zhang_2024_minkpp} exhibits directional reversal at 0.5B (Cohen's $d = -1.55$ to $-1.98$). RRF-guided item filtering is a prerequisite for IRT convergence ($\Delta\tau = 0.18$ vs.\ size-matched random). Simulation establishes $\gamma$ recovery requires $J \geq 50$ at AUC $\geq 0.55$, above current practice ($J = 8$--$30$).
12	\end{enumerate}
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "7aaafe7d-1d14-47aa-b0d1-7cb385264200",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nBenchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \\citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \\citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \\citep{sun2025emperor}, contamination-free benchmarks \\citep{white2024livebench}, and dynamic regeneration \\citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.\n\nWe perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover five distinct dose-response patterns---from immunity (Phi-4 14.7B, $\\pm$0.5pp on MMLU) to catastrophic U-type collapse (Qwen-14B, $-$10pp). A baseline ability threshold at 64.7\\% MMLU (bootstrap 95\\% CI: 64.0--65.4\\%) separates models that benefit from contamination (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp) from those harmed or immune. Counter-intuitively, the 14B model is 3$\\times$ more fragile than 7B. Using ContamCal, a two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\\gamma_k$), we provide the statistical machinery for this characterization.\n\nOur contributions:\n\\begin{enumerate}\n    \\item \\textbf{Five-pattern contamination taxonomy.} Controlled injection across four families reveals five dose-response patterns governed by a 64.7\\% baseline threshold (95\\% CI: 64.0--65.4\\%), directionally consistent across MMLU and ARC-Challenge. Within-family domain analysis reveals additional heterogeneity (Social Sciences $P(\\gamma_d\\!<\\!0) = 99.7\\%$).\n    \\item \\textbf{Global modulation, not memorization.} Difference-in-differences analysis on 14{,}042 MMLU items shows no differential accuracy gain for contaminated vs.\\ clean items in any model family, providing causal evidence that SFT contamination operates through global capability modulation rather than item-specific memorization.\n    \\item \\textbf{Signal failure characterization.} Min-K\\%++ \\citep{zhang_2024_minkpp} exhibits directional reversal at 0.5B (Cohen's $d = -1.55$ to $-1.98$). RRF-guided item filtering is a prerequisite for IRT convergence ($\\Delta\\tau = 0.18$ vs.\\ size-matched random). Simulation establishes $\\gamma$ recovery requires $J \\geq 50$ at AUC $\\geq 0.55$, above current practice ($J = 8$--$30$).\n\\end{enumerate}\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Grep · `toolu_01SDAzTkFCvm7STYjpyegDA1`</summary>

```json
{
  "pattern": "V-recovery|single seed|one seed|dual.seed|180|30 combination|sensitivity",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper",
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
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "394ebbca-1cd2-452c-9c3d-e1881ab638f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwUcft4u42wNng5zu9rdBa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16429,
      "cache_read_input_tokens": 31645,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16429
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

_source line 32 · 2026-05-19T22:10:40.472Z_

<details><summary>↩ Tool result · `toolu_01SDAzTkFCvm7STYjpyegDA1`</summary>

```text
docs/paper/limitations.tex:10:The five-pattern taxonomy (Table~\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.
docs/paper/limitations.tex:16:ARC-Challenge contains only 1{,}172 items (vs.\ 14{,}042 for MMLU), resulting in substantially lower bootstrap profile stability: OLMo-2 53.3\%, Gemma-2 62.7\% (vs.\ $\geq$76.6\% on MMLU). Gemma-2's ARC $\Delta$acc 95\% CI crosses zero, and Qwen-14B exhibits a different pattern (V-recovery) on ARC than on MMLU (U-collapse). Cross-benchmark consistency claims should be interpreted as directional agreement, not pattern-level replication.
docs/paper/limitations.tex:33:\paragraph{Prompt format sensitivity.}
docs/paper/limitations.tex:34:[Omitted long matching line]
docs/paper/main.fdb_latexmk:48:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm" 1136768653 1520 eccf95517727cb11801f4f1aee3a21b4 ""
docs/paper/main.fdb_latexmk:62:  "/usr/share/texlive/texmf-dist/fonts/tfm/public/latex-fonts/lasy6.tfm" 1136768653 520 4889cce2180234b97cad636b6039c722 ""
docs/paper/main.fdb_latexmk:108:  "/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty" 1575152242 21514 b7557edcee22835ef6b03ede1802dad4 ""
docs/paper/appendix.tex:6:[Omitted long matching line]
docs/paper/appendix.tex:84:\label{sec:prior_sensitivity}
docs/paper/appendix.tex:86:[Omitted long matching line]
docs/paper/appendix.tex:92:\caption{Social Sciences $\gamma$ prior sensitivity ($J$=16).}
docs/paper/appendix.tex:152:\label{sec:classification_sensitivity}
docs/paper/appendix.tex:154:We assess the robustness of Algorithm~\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\tau, \sigma)$ combinations: $\tau \in \{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\}$~pp $\times$ $\sigma \in \{3, 4, 5, 6, 7\}$~pp. Table~\ref{tab:sensitivity} reports stability across this grid.
docs/paper/appendix.tex:159:\label{tab:sensitivity}
docs/paper/appendix.tex:169:Qwen-7B & V-recovery & 30/30 & volatility check resolves \\
docs/paper/appendix.tex:174:[Omitted long matching line]
docs/paper/appendix.tex:181:[Omitted long matching line]
docs/paper/appendix.tex:183:Second, domains differ in sensitivity. STEM is the most resilient (mean $|\Delta\text{acc}| = 2.8$pp across five families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\times$ the STEM magnitude. The ordering is stable across patterns: in U-collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.
docs/paper/appendix.tex:185:These results reinforce the global capability modulation interpretation (\S\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.
docs/paper/experimental_setup.tex:9:[Omitted long matching line]
docs/paper/references.bib:377:  eprint    = {1803.05457},
docs/paper/results.tex:11:\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
docs/paper/results.tex:20:V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% \\
docs/paper/results.tex:27:Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\ref{tab:taxonomy}, Figure~\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\tau,\sigma)$ threshold combinations (Appendix~\ref{sec:classification_sensitivity}).
docs/paper/results.tex:106:[Omitted long matching line]
docs/paper/main.aux:238:\@LN{180}{2}
docs/paper/main.aux:419:[Omitted long matching line]
docs/paper/main.aux:420:\newlabel{tab:taxonomy}{{1}{5}{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta $acc: d000$\to $d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\tau ,\sigma )$ combinations; Appendix~\ref {sec:classification_sensitivity})}{table.caption.7}{}}
docs/paper/main.aux:682:\@writefile{toc}{\contentsline {paragraph}{Prompt format sensitivity.}{8}{section*.26}\protected@file@percent }
docs/paper/main.aux:1085:\newlabel{sec:prior_sensitivity}{{H}{12}{Prior Sensitivity Analysis}{appendix.H}{}}
docs/paper/main.aux:1101:\@writefile{lot}{\contentsline {table}{\numberline {5}{\ignorespaces Social Sciences $\gamma $ prior sensitivity ($J$=16).}}{12}{table.caption.34}\protected@file@percent }
docs/paper/main.aux:1102:\newlabel{tab:socsci_prior}{{5}{12}{Social Sciences $\gamma $ prior sensitivity ($J$=16)}{table.caption.34}{}}
docs/paper/main.aux:1143:\newlabel{sec:classification_sensitivity}{{L}{12}{Sensitivity of Profile Classification}{appendix.L}{}}
docs/paper/main.aux:1150:\newlabel{tab:sensitivity}{{7}{12}{Profile classification stability across 30 $(\tau , \sigma )$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability}{table.caption.37}{}}
docs/paper/method.tex:59:[Omitted long matching line]
docs/paper/method.tex:68:\Ensure Pattern $p \in \{\textsc{Immune}, \textsc{U-collapse}, \textsc{V-recovery}, \textsc{Benefit}, \textsc{Benefit-sat}\}$
docs/paper/method.tex:76:        \State \Return \textsc{V-recovery} \Comment{V-dip with full endpoint recovery}
docs/paper/method.tex:84:        \State \Return \textsc{V-recovery} \Comment{mid-dosage trough with partial recovery}
docs/paper/main.log:318:\tagwidth@=\dimen180
docs/paper/main.log:359:Package: booktabs 2020/01/12 v1.61803398 Publication quality tables
docs/paper/main.bbl:51:\newblock \href {https://arxiv.org/abs/1803.05457} {Think you have solved
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "56f2bf9d-8584-4942-ab62-262515867f80",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/limitations.tex:10:The five-pattern taxonomy (Table~\\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.\ndocs/paper/limitations.tex:16:ARC-Challenge contains only 1{,}172 items (vs.\\ 14{,}042 for MMLU), resulting in substantially lower bootstrap profile stability: OLMo-2 53.3\\%, Gemma-2 62.7\\% (vs.\\ $\\geq$76.6\\% on MMLU). Gemma-2's ARC $\\Delta$acc 95\\% CI crosses zero, and Qwen-14B exhibits a different pattern (V-recovery) on ARC than on MMLU (U-collapse). Cross-benchmark consistency claims should be interpreted as directional agreement, not pattern-level replication.\ndocs/paper/limitations.tex:33:\\paragraph{Prompt format sensitivity.}\ndocs/paper/limitations.tex:34:[Omitted long matching line]\ndocs/paper/main.fdb_latexmk:48:  \"/usr/share/texlive/texmf-dist/fonts/tfm/public/cm/cmmi8.tfm\" 1136768653 1520 eccf95517727cb11801f4f1aee3a21b4 \"\"\ndocs/paper/main.fdb_latexmk:62:  \"/usr/share/texlive/texmf-dist/fonts/tfm/public/latex-fonts/lasy6.tfm\" 1136768653 520 4889cce2180234b97cad636b6039c722 \"\"\ndocs/paper/main.fdb_latexmk:108:  \"/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty\" 1575152242 21514 b7557edcee22835ef6b03ede1802dad4 \"\"\ndocs/paper/appendix.tex:6:[Omitted long matching line]\ndocs/paper/appendix.tex:84:\\label{sec:prior_sensitivity}\ndocs/paper/appendix.tex:86:[Omitted long matching line]\ndocs/paper/appendix.tex:92:\\caption{Social Sciences $\\gamma$ prior sensitivity ($J$=16).}\ndocs/paper/appendix.tex:152:\\label{sec:classification_sensitivity}\ndocs/paper/appendix.tex:154:We assess the robustness of Algorithm~\\ref{alg:profile-classification} to threshold selection via a grid sweep over 30 $(\\tau, \\sigma)$ combinations: $\\tau \\in \\{0.5, 0.75, 1.0, 1.25, 1.5, 2.0\\}$~pp $\\times$ $\\sigma \\in \\{3, 4, 5, 6, 7\\}$~pp. Table~\\ref{tab:sensitivity} reports stability across this grid.\ndocs/paper/appendix.tex:159:\\label{tab:sensitivity}\ndocs/paper/appendix.tex:169:Qwen-7B & V-recovery & 30/30 & volatility check resolves \\\\\ndocs/paper/appendix.tex:174:[Omitted long matching line]\ndocs/paper/appendix.tex:181:[Omitted long matching line]\ndocs/paper/appendix.tex:183:Second, domains differ in sensitivity. STEM is the most resilient (mean $|\\Delta\\text{acc}| = 2.8$pp across five families at d100). Social Sciences is the most sensitive at $5.1$pp---$1.8\\times$ the STEM magnitude. The ordering is stable across patterns: in U-collapse, STEM shows the smallest decline; in Benefit, STEM shows the smallest gain.\ndocs/paper/appendix.tex:185:These results reinforce the global capability modulation interpretation (\\S\\ref{sec:memorization_test}): contamination direction is determined by the model's dose-response pattern rather than domain-specific memorization. The differential domain sensitivity more likely reflects variation in item difficulty distributions than differential memorization rates.\ndocs/paper/experimental_setup.tex:9:[Omitted long matching line]\ndocs/paper/references.bib:377:  eprint    = {1803.05457},\ndocs/paper/results.tex:11:\\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta$acc: d000$\\to$d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\\tau,\\sigma)$ combinations; Appendix~\\ref{sec:classification_sensitivity}).}\ndocs/paper/results.tex:20:V-recovery & Qwen-7B & 66.1\\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\\textsuperscript{d025} & 99.6\\% \\\\\ndocs/paper/results.tex:27:Applying Algorithm~\\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields five distinct dose-response patterns (Table~\\ref{tab:taxonomy}, Figure~\\ref{fig:dose_response}), not a uniform inflation effect. All five classifications are stable across 30 $(\\tau,\\sigma)$ threshold combinations (Appendix~\\ref{sec:classification_sensitivity}).\ndocs/paper/results.tex:106:[Omitted long matching line]\ndocs/paper/main.aux:238:\\@LN{180}{2}\ndocs/paper/main.aux:419:[Omitted long matching line]\ndocs/paper/main.aux:420:\\newlabel{tab:taxonomy}{{1}{5}{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\\Delta $acc: d000$\\to $d100 change (95\\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (150/150 model-combination pairs across 30 $(\\tau ,\\sigma )$ combinations; Appendix~\\ref {sec:classification_sensitivity})}{table.caption.7}{}}\ndocs/paper/main.aux:682:\\@writefile{toc}{\\contentsline {paragraph}{Prompt format sensitivity.}{8}{section*.26}\\protected@file@percent }\ndocs/paper/main.aux:1085:\\newlabel{sec:prior_sensitivity}{{H}{12}{Prior Sensitivity Analysis}{appendix.H}{}}\ndocs/paper/main.aux:1101:\\@writefile{lot}{\\contentsline {table}{\\numberline {5}{\\ignorespaces Social Sciences $\\gamma $ prior sensitivity ($J$=16).}}{12}{table.caption.34}\\protected@file@percent }\ndocs/paper/main.aux:1102:\\newlabel{tab:socsci_prior}{{5}{12}{Social Sciences $\\gamma $ prior sensitivity ($J$=16)}{table.caption.34}{}}\ndocs/paper/main.aux:1143:\\newlabel{sec:classification_sensitivity}{{L}{12}{Sensitivity of Profile Classification}{appendix.L}{}}\ndocs/paper/main.aux:1150:\\newlabel{tab:sensitivity}{{7}{12}{Profile classification stability across 30 $(\\tau , \\sigma )$ threshold combinations (with mid-trajectory volatility check). All five families achieve perfect stability}{table.caption.37}{}}\ndocs/paper/method.tex:59:[Omitted long matching line]\ndocs/paper/method.tex:68:\\Ensure Pattern $p \\in \\{\\textsc{Immune}, \\textsc{U-collapse}, \\textsc{V-recovery}, \\textsc{Benefit}, \\textsc{Benefit-sat}\\}$\ndocs/paper/method.tex:76:        \\State \\Return \\textsc{V-recovery} \\Comment{V-dip with full endpoint recovery}\ndocs/paper/method.tex:84:        \\State \\Return \\textsc{V-recovery} \\Comment{mid-dosage trough with partial recovery}\ndocs/paper/main.log:318:\\tagwidth@=\\dimen180\ndocs/paper/main.log:359:Package: booktabs 2020/01/12 v1.61803398 Publication quality tables\ndocs/paper/main.bbl:51:\\newblock \\href {https://arxiv.org/abs/1803.05457} {Think you have solved",
    "numLines": 41
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Let me also read the limitations.tex to check V-recovery language there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "1a23adb9-eaf5-47fb-9c92-c46df606da13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqAAJTaAL6Ks9UFAQM56nf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6516,
      "cache_read_input_tokens": 48074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6516
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

_source line 34_

Let me read the limitations.tex and check the discussion section for any remaining references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "5217b083-681f-419f-88eb-3ea2e1d646b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqAAJTaAL6Ks9UFAQM56nf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6516,
      "cache_read_input_tokens": 48074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6516
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

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01GEwnjdoSTw1Z2YUjBs5fTg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "aa294a34-87eb-4f80-801f-32e279f2a3b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqAAJTaAL6Ks9UFAQM56nf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6516,
      "cache_read_input_tokens": 48074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6516
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

_source line 36 · 2026-05-19T22:10:44.295Z_

<details><summary>↩ Tool result · `toolu_01GEwnjdoSTw1Z2YUjBs5fTg`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	We identify ten limitations that bound the scope of our conclusions.
5	
6	\paragraph{Scale ceiling.}
7	All experiments use models at or below 14.7B parameters. Larger models (70B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.
8	
9	\paragraph{Single seed.}
10	The five-pattern taxonomy (Table~\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.
11	
12	\paragraph{SFT ecological validity.}
13	We use LoRA-based SFT injection exclusively in AUGMENT mode (contaminated items appended to, not replacing, base SFT data). Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures. The position bias at 0.5B (A-option rate escalating from 46\% to 98\% with dosage) is likely SFT-specific. Generalization to pretraining contamination requires further validation.
14	
15	\paragraph{ARC-Challenge bootstrap stability.}
16	ARC-Challenge contains only 1{,}172 items (vs.\ 14{,}042 for MMLU), resulting in substantially lower bootstrap profile stability: OLMo-2 53.3\%, Gemma-2 62.7\% (vs.\ $\geq$76.6\% on MMLU). Gemma-2's ARC $\Delta$acc 95\% CI crosses zero, and Qwen-14B exhibits a different pattern (V-recovery) on ARC than on MMLU (U-collapse). Cross-benchmark consistency claims should be interpreted as directional agreement, not pattern-level replication.
17	
18	\paragraph{Signal coverage.}
19	S1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\S\ref{sec:signal_failure}).
20	
21	\paragraph{Ensemble size and per-domain power.}
22	Reliable $\gamma$ recovery requires $J \geq 50$. Our domain-level analysis ($J = 13$--$16$) yields a strong directional signal for only one of eight MMLU domains. Per-domain $\gamma$ diagnosis at current ensemble sizes is exploratory.
23	
24	\paragraph{Position bias.}
25	Qwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\% at d000 to 98\% at d100); these models are excluded from MC IRT analyses, reducing ensemble size.
26	
27	\paragraph{Model misfit in non-STEM domains.}
28	A single linear $\gamma$ cannot capture non-monotone contamination effects within a domain. The five-pattern taxonomy operates at the model level; richer within-domain specifications may be required for domain-level calibration.
29	
30	\paragraph{Additive $\gamma$ linearity.}
31	The 2PL+$\gamma$ model assumes contamination effects are additive and linear in exposure. PPP posterior predictive checks cannot detect threshold-type model misspecification (PPP remains 0.50--0.56 despite up to 33\% $\gamma$ overestimation), which highlights the value of simulation-based specification testing. The threshold DGP simulation uses uniform exposure; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.
32	
33	\paragraph{Prompt format sensitivity.}
34	The observed dose-response profiles are conditional on the evaluation protocol (5-shot prompting for MMLU, 25-shot for ARC-Challenge). Preliminary comparison with 0-shot evaluation suggests that pattern shapes may vary with prompt format---for instance, the V-type recovery pattern observed under 5-shot prompting can disappear under 0-shot conditions. This indicates that contamination effects interact with in-context learning mechanisms. While internal consistency is maintained (all 75 model--dosage configurations use the same protocol), practitioners replicating our analyses under different prompting regimes should expect quantitatively and potentially qualitatively different dose-response profiles. Future work should systematically evaluate protocol sensitivity across shot counts and prompt templates.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "4de66409-742d-4465-8522-886de159789d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nWe identify ten limitations that bound the scope of our conclusions.\n\n\\paragraph{Scale ceiling.}\nAll experiments use models at or below 14.7B parameters. Larger models (70B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.\n\n\\paragraph{Single seed.}\nThe five-pattern taxonomy (Table~\\ref{tab:taxonomy}) is confirmed across two seeds (s42, s123). V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123), consistent with stochastic SFT learning dynamics. Triple-seed validation with error bars is in progress.\n\n\\paragraph{SFT ecological validity.}\nWe use LoRA-based SFT injection exclusively in AUGMENT mode (contaminated items appended to, not replacing, base SFT data). Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures. The position bias at 0.5B (A-option rate escalating from 46\\% to 98\\% with dosage) is likely SFT-specific. Generalization to pretraining contamination requires further validation.\n\n\\paragraph{ARC-Challenge bootstrap stability.}\nARC-Challenge contains only 1{,}172 items (vs.\\ 14{,}042 for MMLU), resulting in substantially lower bootstrap profile stability: OLMo-2 53.3\\%, Gemma-2 62.7\\% (vs.\\ $\\geq$76.6\\% on MMLU). Gemma-2's ARC $\\Delta$acc 95\\% CI crosses zero, and Qwen-14B exhibits a different pattern (V-recovery) on ARC than on MMLU (U-collapse). Cross-benchmark consistency claims should be interpreted as directional agreement, not pattern-level replication.\n\n\\paragraph{Signal coverage.}\nS1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\\S\\ref{sec:signal_failure}).\n\n\\paragraph{Ensemble size and per-domain power.}\nReliable $\\gamma$ recovery requires $J \\geq 50$. Our domain-level analysis ($J = 13$--$16$) yields a strong directional signal for only one of eight MMLU domains. Per-domain $\\gamma$ diagnosis at current ensemble sizes is exploratory.\n\n\\paragraph{Position bias.}\nQwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\\% at d000 to 98\\% at d100); these models are excluded from MC IRT analyses, reducing ensemble size.\n\n\\paragraph{Model misfit in non-STEM domains.}\nA single linear $\\gamma$ cannot capture non-monotone contamination effects within a domain. The five-pattern taxonomy operates at the model level; richer within-domain specifications may be required for domain-level calibration.\n\n\\paragraph{Additive $\\gamma$ linearity.}\nThe 2PL+$\\gamma$ model assumes contamination effects are additive and linear in exposure. PPP posterior predictive checks cannot detect threshold-type model misspecification (PPP remains 0.50--0.56 despite up to 33\\% $\\gamma$ overestimation), which highlights the value of simulation-based specification testing. The threshold DGP simulation uses uniform exposure; real RRF exposure is right-skewed (mean$=$0.041), so the quantitative overestimation magnitude may differ, but the qualitative direction (overestimation, not attenuation) is robust.\n\n\\paragraph{Prompt format sensitivity.}\nThe observed dose-response profiles are conditional on the evaluation protocol (5-shot prompting for MMLU, 25-shot for ARC-Challenge). Preliminary comparison with 0-shot evaluation suggests that pattern shapes may vary with prompt format---for instance, the V-type recovery pattern observed under 5-shot prompting can disappear under 0-shot conditions. This indicates that contamination effects interact with in-context learning mechanisms. While internal consistency is maintained (all 75 model--dosage configurations use the same protocol), practitioners replicating our analyses under different prompting regimes should expect quantitatively and potentially qualitatively different dose-response profiles. Future work should systematically evaluate protocol sensitivity across shot counts and prompt templates.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01XNNK6L5kWUmnLVHFTwpynU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "5a06f294-3e0d-433a-9d48-886a2a0bbeab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqAAJTaAL6Ks9UFAQM56nf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6516,
      "cache_read_input_tokens": 48074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6516
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

_source line 38 · 2026-05-19T22:10:44.453Z_

<details><summary>↩ Tool result · reported error · `toolu_01XNNK6L5kWUmnLVHFTwpynU`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "f3e203d1-66e8-4e21-a447-76165e2e5b43",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration."
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also check the conclusion.

Actually, let me check if there's a discussion section.

The discussion.tex doesn't exist in docs/paper/. Let me just check the conclusion and abstract for V-recovery mentions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "e9d03e1a-a066-4d0b-addc-c90938572273",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Nt6SndvRSXYGWrpPsPj1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1466,
      "cache_read_input_tokens": 54590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1466
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

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01DhA5e4t1UoL7Z4HUtXfa7n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "641077ab-9594-4115-ae56-9f86ccc5e8f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Nt6SndvRSXYGWrpPsPj1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1466,
      "cache_read_input_tokens": 54590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1466
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

_source line 41 · 2026-05-19T22:10:48.577Z_

<details><summary>↩ Tool result · `toolu_01DhA5e4t1UoL7Z4HUtXfa7n`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	We systematically profiled how SFT-injected contamination affects benchmark scores across model families and scales. Three findings emerge.
4	
5	\paragraph{Five patterns, not one.}
6	The ``contamination inflates scores'' assumption is a gross oversimplification. Controlled injection reveals five distinct dose-response patterns governed by a baseline ability threshold at 64.7\% MMLU (95\% CI: 64.0--65.4\%): models below it benefit ($+$3--4pp), models above are harmed ($-$3 to $-$10pp) or immune. Item-level DiD analysis (\S\ref{sec:memorization_test}) shows these patterns arise from global capability modulation, not item-specific memorization---challenging the premise of overlap-based detection methods. Contamination \emph{direction} is consistent across benchmarks; \emph{shape} varies with benchmark properties (Appendix~\ref{sec:arc_cross_benchmark}), implying model-\emph{and}-benchmark-specific profiling is necessary.
7	
8	\paragraph{Why bigger $\neq$ more robust.}
9	Qwen-14B ($-$10pp) is 3$\times$ more fragile than Qwen-7B ($-$3pp): SFT injection disrupts more specialized representations that smaller models have not yet developed. Organizations fine-tuning frontier models on mixed-quality data face greater capability degradation risk.
10	
11	\paragraph{Diagnostic value beyond aggregate calibration.}
12	Domain analysis reveals heterogeneity masked by aggregate scores (Social Sciences $P(\gamma_d\!<\!0) = 99.7\%$). The IRT framework captures both family-level patterns and domain-level decomposition. Pretraining contamination may produce qualitatively different effects \citep{schaeffer2026causally}; scaling to 70B+ is a natural next step.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "9b659513-5a10-40a1-a1be-c71e52215cae",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nWe systematically profiled how SFT-injected contamination affects benchmark scores across model families and scales. Three findings emerge.\n\n\\paragraph{Five patterns, not one.}\nThe ``contamination inflates scores'' assumption is a gross oversimplification. Controlled injection reveals five distinct dose-response patterns governed by a baseline ability threshold at 64.7\\% MMLU (95\\% CI: 64.0--65.4\\%): models below it benefit ($+$3--4pp), models above are harmed ($-$3 to $-$10pp) or immune. Item-level DiD analysis (\\S\\ref{sec:memorization_test}) shows these patterns arise from global capability modulation, not item-specific memorization---challenging the premise of overlap-based detection methods. Contamination \\emph{direction} is consistent across benchmarks; \\emph{shape} varies with benchmark properties (Appendix~\\ref{sec:arc_cross_benchmark}), implying model-\\emph{and}-benchmark-specific profiling is necessary.\n\n\\paragraph{Why bigger $\\neq$ more robust.}\nQwen-14B ($-$10pp) is 3$\\times$ more fragile than Qwen-7B ($-$3pp): SFT injection disrupts more specialized representations that smaller models have not yet developed. Organizations fine-tuning frontier models on mixed-quality data face greater capability degradation risk.\n\n\\paragraph{Diagnostic value beyond aggregate calibration.}\nDomain analysis reveals heterogeneity masked by aggregate scores (Social Sciences $P(\\gamma_d\\!<\\!0) = 99.7\\%$). The IRT framework captures both family-level patterns and domain-level decomposition. Pretraining contamination may produce qualitatively different effects \\citep{schaeffer2026causally}; scaling to 70B+ is a natural next step.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_016GHhfQHwFsN77y4viojvsA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "099de194-2ffd-4b62-a9aa-7cd9050970ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Nt6SndvRSXYGWrpPsPj1u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1466,
      "cache_read_input_tokens": 54590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1466
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

_source line 43 · 2026-05-19T22:10:49.042Z_

<details><summary>↩ Tool result · `toolu_016GHhfQHwFsN77y4viojvsA`</summary>

```text
1	Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but five distinct dose-response patterns: Immune ($\pm$0.5pp), U-type collapse ($-$10pp), V-type recovery ($-$3pp then partial rebound), Benefit ($+$3.8pp monotonic), and Benefit-saturation ($+$3.2pp then plateau). A baseline ability threshold at 64.7\% MMLU (bootstrap 95\% CI: 64.0--65.4\%) separates models that benefit from contamination from those that are harmed or immune. Counter-intuitively, the 14B Qwen model is 3$\times$ more fragile than 7B. Profiles are robust on MMLU (4/5 families $\geq$99.6\% bootstrap stability); ARC-Challenge shows directional agreement for 3/5 families but lower stability due to its smaller item pool (1{,}172 vs.\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \geq 50$) above current practice. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "79392896-c0b6-4f02-9a37-7c8d532da7c4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex",
      "content": "Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but five distinct dose-response patterns: Immune ($\\pm$0.5pp), U-type collapse ($-$10pp), V-type recovery ($-$3pp then partial rebound), Benefit ($+$3.8pp monotonic), and Benefit-saturation ($+$3.2pp then plateau). A baseline ability threshold at 64.7\\% MMLU (bootstrap 95\\% CI: 64.0--65.4\\%) separates models that benefit from contamination from those that are harmed or immune. Counter-intuitively, the 14B Qwen model is 3$\\times$ more fragile than 7B. Profiles are robust on MMLU (4/5 families $\\geq$99.6\\% bootstrap stability); ARC-Challenge shows directional agreement for 3/5 families but lower stability due to its smaller item pool (1{,}172 vs.\\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \\geq 50$) above current practice. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.\n",
      "numLines": 2,
      "startLine": 1,
      "totalLines": 2
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed. Let me compile the audit report.

## 1. Algorithm 1 Pseudocode vs profile_classifier.py

### Artifacts pseudocode (algorithm1_pseudocode.tex) vs profile_classifier.py:
These match perfectly:
- 6 output patterns including V-recovery-full ✅
- All branch conditions identical ✅
- All thresholds match ✅
- v* (max_deviation) computation matches ✅
- Saturation logic matches ✅

### Paper Algorithm (method.tex lines 61-98) vs profile_classifier.py:


I'm finding some key discrepancies here. The paper defines only 5 output patterns while the code implements 6, with the extra one being V-recovery-full. More significantly, for the case where |Δ|≤τ, v*>τ, and a V-dip is detected, the paper returns V-recovery but the code returns V-recovery-full—the code's comment describes this as "V-dip with full endpoint recovery," suggesting the label itself differs from what's documented. The rest of the algorithm aligns correctly, including the delta calculation and other threshold comparisons. I've set the parameters to τ=1, σ=5, ρ=0.3, λ=0.5. The main discrepancy I'm seeing is that V-recovery-full in the code gets collapsed into V-recovery in the paper—it looks like an intentional simplification that the paper discusses as a subtype, but the implementations haven't been aligned yet. Now I'm checking the sensitivity analysis description across the paper sections to see if there's consistency in how the grid sweep is documented.

Looking at the references, everything currently says 30 combinations, but the task specifies v2 should have 180 combinations instead. I need to update method.tex, results.tex, and appendix.tex to reflect the 180-combination grid sweep across the expanded parameter ranges rather than the original 30. I'm trying to understand what the 180/180 notation means—it could represent 180 parameter combinations across the sweep (like 6 τ × 5 σ × 6 ρ), where each model shows stability across all 180 combinations rather than just 30. The task is to update all references from the v1 (30/30) format to v2 (180/180) throughout the document.

Now checking the V-recovery dual-seed section to see what's already been verified and what still needs updating. I'm noticing the abstract only mentions partial rebound for V-recovery, which reflects the seed=42 case but glosses over the full recovery observed at seed=123. While brevity is important, this feels like stale language given the dual-seed validation now shows recovery extent varies significantly by seed. The conclusion doesn't address V-recovery specifics either, so I should flag both the misleading "Single seed." heading in limitations.tex and the abstract's incomplete characterization of the recovery pattern.

Now checking Algorithm 1 consistency between the paper and code: the pseudocode matches the implementation perfectly across all six patterns and branch conditions, though the paper collapses V-recovery-full into V-recovery for presentation. All thresholds, saturation logic, and volatility checks align correctly.

I'm noticing the sensitivity analysis still references 30 combinations throughout the paper when it should say 180 — this needs updating in method.tex, both results.tex locations, and multiple appendix sections including the table captions and data rows. The V-recovery dual-seed behavior is properly documented as varying by seed, though the limitations section has a stale heading that contradicts its own content about dual-seed behavior.

The abstract only captures the seed=42 case for V-type recovery without mentioning the full recovery at seed=123, and the specific D165 numbers from the two seeds aren't explicitly stated anywhere — Table 1 shows the rounded s42 value but s123 is missing entirely from the tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "fc22664c-1934-45a5-958a-f00b9cdfe167",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnJ34vfsQeV4E65aJ7YpXt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1169,
      "cache_read_input_tokens": 56056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1169
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

_source line 45_

Now I have all the data needed. Let me write the audit report and register it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "00d12cc5-5160-4739-b8c6-88bf18ee6af6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnJ34vfsQeV4E65aJ7YpXt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1169,
      "cache_read_input_tokens": 56056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1169
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

_source line 46_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01K4DGAgRDS7MNik4RXQqCFi`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "f32931e5-3e43-433d-a577-f41152653451",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RnJ34vfsQeV4E65aJ7YpXt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1169,
      "cache_read_input_tokens": 56056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1169
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

_source line 47 · 2026-05-19T22:11:39.091Z_

<details><summary>↩ Tool result · `toolu_01K4DGAgRDS7MNik4RXQqCFi`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "1b317a95-3222-4733-8403-c8fba3871a86",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Write · `toolu_016tnjLaBNgEahSRPL7k8wPE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_consistency_audit.md",
  "content": "# Paper Data Consistency Audit (2026-05-19)\n\nPre-submission check for EMNLP 2026. Compares paper (`docs/paper/`) against code artifacts and recent experimental updates.\n\n---\n\n## Algorithm 1 Consistency\n\n**Comparison: `profile_classifier.py` vs artifacts `algorithm1_pseudocode.tex` vs paper `method.tex` Algorithm 1**\n\n| Check | Status | Detail |\n|-------|--------|--------|\n| Δ = a100 − a0 | ✅ | All three sources match |\n| m* = min(a5, a25, a50) | ✅ | All three sources match |\n| v* = max\\|ai − a0\\| (volatility check) | ✅ | All three sources match |\n| Branch 1: \\|Δ\\| ≤ τ → Immune (v* ≤ τ) | ✅ | Match |\n| Branch 1: \\|Δ\\| ≤ τ, v* > τ, V-dip → ? | ❌ | **Code returns `V-recovery-full`; artifacts pseudocode returns `V-recovery-full`; paper Algorithm 1 returns `V-recovery`** |\n| Branch 1: \\|Δ\\| ≤ τ, v* > τ, no V-dip → Immune | ✅ | Match |\n| Branch 2: Δ < −τ, Δ ≤ −σ → U-collapse | ✅ | Match |\n| Branch 2: Δ < −τ, V-dip → V-recovery | ✅ | Match |\n| Branch 2: Δ < −τ, no V-dip → U-collapse | ✅ | Match |\n| Branch 3: Δ > τ, saturation check | ✅ | g1, g2, ℓ logic identical across all three |\n| Branch 3: saturating → Benefit-sat | ✅ | Match |\n| Branch 3: not saturating → Benefit | ✅ | Match |\n| Default thresholds (τ=1, σ=5, ρ=0.3, λ=0.5) | ✅ | Match |\n| Output pattern set | ❌ | **Code/artifacts: 6 patterns (includes `V-recovery-full`). Paper Ensure line (method.tex:68): 5 patterns (no `V-recovery-full`)** |\n\n### Verdict\n\nThe paper intentionally merges `V-recovery-full` into `V-recovery`, treating full vs partial recovery as subtypes rather than separate labels. The prose (method.tex:59) describes the distinction: \"recovery extent varies by seed (partial at seed=42, full at seed=123)\". This is a defensible editorial choice, but creates a mismatch with the implementation.\n\n**Action needed**: Either (a) update the paper Ensure line to include `V-recovery-full` as a 6th pattern, or (b) document explicitly that the paper merges the two subtypes. If keeping 5 patterns in the paper, the code's `V-recovery-full` label should be mentioned in a footnote or appendix to avoid reproducibility confusion.\n\n---\n\n## Sensitivity Description\n\n**Expected state**: v2 sweep with 180 combinations (per task description). **Actual state**: All references say 30 combinations.\n\n| Location | Current Text | Status |\n|----------|-------------|--------|\n| method.tex:59 | \"a 30-combination grid sweep confirms 5/5 families are stable\" | ❌ Not updated |\n| results.tex:11 (Table 1 caption) | \"150/150 model-combination pairs across 30 (τ,σ) combinations\" | ❌ Not updated |\n| results.tex:27 | \"stable across 30 (τ,σ) threshold combinations\" | ❌ Not updated |\n| appendix.tex:154 | \"a grid sweep over 30 (τ, σ) combinations: τ ∈ {0.5, 0.75, 1.0, 1.25, 1.5, 2.0} pp × σ ∈ {3, 4, 5, 6, 7} pp\" | ❌ Not updated |\n| appendix.tex:158 (Table 7 caption) | \"Profile classification stability across 30 (τ, σ) threshold combinations\" | ❌ Not updated |\n| appendix.tex:164–169 (Table 7 data) | Each model shows \"30/30\" | ❌ Not updated |\n\n### Verdict\n\n**All 6 locations still reference the v1 30-combination sweep.** None have been updated to reflect the v2 180-combination sweep. The parameter grid description (appendix.tex:154) and all stability counts need updating.\n\n---\n\n## V-recovery Dual-Seed\n\n**Expected**: Paper reflects D165 dual-seed confirmation (s42 partial Δacc=−1.82pp, s123 full Δacc=0.00pp). No stale hedge language.\n\n| Location | Current Text | Status |\n|----------|-------------|--------|\n| method.tex:59 | \"recovery extent varies by seed (partial at seed=42, full at seed=123)\" | ✅ Correct |\n| results.tex:29–30 | \"Qwen-7B (66.1%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed=42, d005 for seed=123; recovery extent varies from partial to full)\" | ✅ Correct |\n| results.tex Table 1 | Qwen-7B Δacc = −1.8pp | ✅ Consistent with s42 −1.82pp (rounded) |\n| limitations.tex:9 | **Paragraph heading: \"Single seed.\"** but body says \"confirmed across two seeds (s42, s123)\" | ⚠️ **Stale heading** |\n| limitations.tex:10 | \"V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123)\" | ✅ Content is correct |\n| limitations.tex:10 | \"Triple-seed validation with error bars is in progress.\" | ⚠️ Check if still accurate or if this has been completed |\n| abstract.tex:1 | \"V-type recovery (−3pp then partial rebound)\" | ⚠️ **Only describes s42 partial case; does not mention s123 full recovery** |\n| conclusion.tex | No V-recovery detail mentioned | ✅ N/A (no claim made) |\n| introduction.tex | No V-recovery detail mentioned | ✅ N/A |\n\n### Verdict\n\nCore method/results sections correctly reflect dual-seed confirmation. Three issues remain:\n\n1. **limitations.tex:9** — Paragraph heading \"Single seed.\" is stale. Should be renamed (e.g., \"Seed coverage.\" or \"Two-seed validation.\") since the content already describes dual-seed confirmation.\n2. **abstract.tex:1** — \"V-type recovery (−3pp then partial rebound)\" only describes s42. Consider adding \"to full rebound\" or similar to acknowledge the s123 result.\n3. **limitations.tex:10** — \"Triple-seed validation with error bars is in progress\" — verify if this is still the current status or needs updating.\n\n---\n\n## Summary of Required Changes\n\n| Priority | Item | Files |\n|----------|------|-------|\n| **P0** | Update sensitivity sweep from 30 → 180 combinations (6 locations) | method.tex, results.tex, appendix.tex |\n| **P1** | Fix stale \"Single seed.\" heading in limitations | limitations.tex:9 |\n| **P1** | Decide on V-recovery-full: align paper ↔ code (either add 6th pattern to paper or document the merge) | method.tex:68, method.tex:76 |\n| **P2** | Abstract only mentions partial rebound for V-recovery | abstract.tex:1 |\n| **P2** | Verify \"Triple-seed validation in progress\" claim | limitations.tex:10 |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "ae2ba0e8-769b-47ab-ab0f-e2e2331cd2ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BsxWf8tYketGbuAYr3soX6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3184,
      "cache_read_input_tokens": 57225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3184
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

_source line 49 · 2026-05-19T22:12:14.415Z_

<details><summary>↩ Tool result · `toolu_016tnjLaBNgEahSRPL7k8wPE`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_consistency_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "4335064c-c8c2-438c-9cbb-9de92dd8c61c",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_consistency_audit.md",
    "content": "# Paper Data Consistency Audit (2026-05-19)\n\nPre-submission check for EMNLP 2026. Compares paper (`docs/paper/`) against code artifacts and recent experimental updates.\n\n---\n\n## Algorithm 1 Consistency\n\n**Comparison: `profile_classifier.py` vs artifacts `algorithm1_pseudocode.tex` vs paper `method.tex` Algorithm 1**\n\n| Check | Status | Detail |\n|-------|--------|--------|\n| Δ = a100 − a0 | ✅ | All three sources match |\n| m* = min(a5, a25, a50) | ✅ | All three sources match |\n| v* = max\\|ai − a0\\| (volatility check) | ✅ | All three sources match |\n| Branch 1: \\|Δ\\| ≤ τ → Immune (v* ≤ τ) | ✅ | Match |\n| Branch 1: \\|Δ\\| ≤ τ, v* > τ, V-dip → ? | ❌ | **Code returns `V-recovery-full`; artifacts pseudocode returns `V-recovery-full`; paper Algorithm 1 returns `V-recovery`** |\n| Branch 1: \\|Δ\\| ≤ τ, v* > τ, no V-dip → Immune | ✅ | Match |\n| Branch 2: Δ < −τ, Δ ≤ −σ → U-collapse | ✅ | Match |\n| Branch 2: Δ < −τ, V-dip → V-recovery | ✅ | Match |\n| Branch 2: Δ < −τ, no V-dip → U-collapse | ✅ | Match |\n| Branch 3: Δ > τ, saturation check | ✅ | g1, g2, ℓ logic identical across all three |\n| Branch 3: saturating → Benefit-sat | ✅ | Match |\n| Branch 3: not saturating → Benefit | ✅ | Match |\n| Default thresholds (τ=1, σ=5, ρ=0.3, λ=0.5) | ✅ | Match |\n| Output pattern set | ❌ | **Code/artifacts: 6 patterns (includes `V-recovery-full`). Paper Ensure line (method.tex:68): 5 patterns (no `V-recovery-full`)** |\n\n### Verdict\n\nThe paper intentionally merges `V-recovery-full` into `V-recovery`, treating full vs partial recovery as subtypes rather than separate labels. The prose (method.tex:59) describes the distinction: \"recovery extent varies by seed (partial at seed=42, full at seed=123)\". This is a defensible editorial choice, but creates a mismatch with the implementation.\n\n**Action needed**: Either (a) update the paper Ensure line to include `V-recovery-full` as a 6th pattern, or (b) document explicitly that the paper merges the two subtypes. If keeping 5 patterns in the paper, the code's `V-recovery-full` label should be mentioned in a footnote or appendix to avoid reproducibility confusion.\n\n---\n\n## Sensitivity Description\n\n**Expected state**: v2 sweep with 180 combinations (per task description). **Actual state**: All references say 30 combinations.\n\n| Location | Current Text | Status |\n|----------|-------------|--------|\n| method.tex:59 | \"a 30-combination grid sweep confirms 5/5 families are stable\" | ❌ Not updated |\n| results.tex:11 (Table 1 caption) | \"150/150 model-combination pairs across 30 (τ,σ) combinations\" | ❌ Not updated |\n| results.tex:27 | \"stable across 30 (τ,σ) threshold combinations\" | ❌ Not updated |\n| appendix.tex:154 | \"a grid sweep over 30 (τ, σ) combinations: τ ∈ {0.5, 0.75, 1.0, 1.25, 1.5, 2.0} pp × σ ∈ {3, 4, 5, 6, 7} pp\" | ❌ Not updated |\n| appendix.tex:158 (Table 7 caption) | \"Profile classification stability across 30 (τ, σ) threshold combinations\" | ❌ Not updated |\n| appendix.tex:164–169 (Table 7 data) | Each model shows \"30/30\" | ❌ Not updated |\n\n### Verdict\n\n**All 6 locations still reference the v1 30-combination sweep.** None have been updated to reflect the v2 180-combination sweep. The parameter grid description (appendix.tex:154) and all stability counts need updating.\n\n---\n\n## V-recovery Dual-Seed\n\n**Expected**: Paper reflects D165 dual-seed confirmation (s42 partial Δacc=−1.82pp, s123 full Δacc=0.00pp). No stale hedge language.\n\n| Location | Current Text | Status |\n|----------|-------------|--------|\n| method.tex:59 | \"recovery extent varies by seed (partial at seed=42, full at seed=123)\" | ✅ Correct |\n| results.tex:29–30 | \"Qwen-7B (66.1%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed=42, d005 for seed=123; recovery extent varies from partial to full)\" | ✅ Correct |\n| results.tex Table 1 | Qwen-7B Δacc = −1.8pp | ✅ Consistent with s42 −1.82pp (rounded) |\n| limitations.tex:9 | **Paragraph heading: \"Single seed.\"** but body says \"confirmed across two seeds (s42, s123)\" | ⚠️ **Stale heading** |\n| limitations.tex:10 | \"V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123)\" | ✅ Content is correct |\n| limitations.tex:10 | \"Triple-seed validation with error bars is in progress.\" | ⚠️ Check if still accurate or if this has been completed |\n| abstract.tex:1 | \"V-type recovery (−3pp then partial rebound)\" | ⚠️ **Only describes s42 partial case; does not mention s123 full recovery** |\n| conclusion.tex | No V-recovery detail mentioned | ✅ N/A (no claim made) |\n| introduction.tex | No V-recovery detail mentioned | ✅ N/A |\n\n### Verdict\n\nCore method/results sections correctly reflect dual-seed confirmation. Three issues remain:\n\n1. **limitations.tex:9** — Paragraph heading \"Single seed.\" is stale. Should be renamed (e.g., \"Seed coverage.\" or \"Two-seed validation.\") since the content already describes dual-seed confirmation.\n2. **abstract.tex:1** — \"V-type recovery (−3pp then partial rebound)\" only describes s42. Consider adding \"to full rebound\" or similar to acknowledge the s123 result.\n3. **limitations.tex:10** — \"Triple-seed validation with error bars is in progress\" — verify if this is still the current status or needs updating.\n\n---\n\n## Summary of Required Changes\n\n| Priority | Item | Files |\n|----------|------|-------|\n| **P0** | Update sensitivity sweep from 30 → 180 combinations (6 locations) | method.tex, results.tex, appendix.tex |\n| **P1** | Fix stale \"Single seed.\" heading in limitations | limitations.tex:9 |\n| **P1** | Decide on V-recovery-full: align paper ↔ code (either add 6th pattern to paper or document the merge) | method.tex:68, method.tex:76 |\n| **P2** | Abstract only mentions partial rebound for V-recovery | abstract.tex:1 |\n| **P2** | Verify \"Triple-seed validation in progress\" claim | limitations.tex:10 |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_011nB3NQCFyY1QpGM5VSwRQQ`</summary>

```json
{
  "name": "paper_consistency_audit",
  "type": "report",
  "description": "Pre-submission consistency audit: Algorithm 1 pseudocode vs code, sensitivity sweep 30→180 update status, V-recovery dual-seed description check",
  "project": "contamcal-irt-calibration",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_consistency_audit.md",
  "tags": [
    "audit",
    "paper",
    "pre-submission"
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
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "0b11fd57-afc1-4878-baa9-f34895291f36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdJtpT23djWKEg7ehjv6SP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2181,
      "cache_read_input_tokens": 60409,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2181
      },
      "output_tokens": 67,
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

_source line 51 · 2026-05-19T22:12:18.934Z_

<details><summary>↩ Tool result · `toolu_011nB3NQCFyY1QpGM5VSwRQQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_e79d2d\", \"name\": \"paper_consistency_audit\", \"type\": \"report\", \"description\": \"Pre-submission consistency audit: Algorithm 1 pseudocode vs code, sensitivity sweep 30→180 update status, V-recovery dual-seed description check\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/report/paper_consistency_audit.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T22:12:18.691507+00:00\", \"tags\": [\"audit\", \"paper\", \"pre-submission\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "e0e470f9-24be-49b2-ac23-3a2b1701950d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260519_e79d2d\\\", \\\"name\\\": \\\"paper_consistency_audit\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Pre-submission consistency audit: Algorithm 1 pseudocode vs code, sensitivity sweep 30→180 update status, V-recovery dual-seed description check\\\", \\\"path\\\": \\\"projects/contamcal-irt-calibration/artifacts/_project/report/paper_consistency_audit.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-19T22:12:18.691507+00:00\\\", \\\"tags\\\": [\\\"audit\\\", \\\"paper\\\", \\\"pre-submission\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_e79d2d\", \"name\": \"paper_consistency_audit\", \"type\": \"report\", \"description\": \"Pre-submission consistency audit: Algorithm 1 pseudocode vs code, sensitivity sweep 30→180 update status, V-recovery dual-seed description check\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/report/paper_consistency_audit.md\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T22:12:18.691507+00:00\", \"tags\": [\"audit\", \"paper\", \"pre-submission\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 52_

审计完成。核心发现：

**Algorithm 1**: 代码与 artifacts 伪代码完全一致。论文版本将 `V-recovery-full` 合并为 `V-recovery`（5 patterns vs 代码 6 patterns），逻辑分支全部匹配，仅标签不同。需决定是否对齐。

**Sensitivity**: **全部 6 处仍写 "30 combinations"，未更新为 180。** 涉及 method.tex、results.tex (Table 1 caption + 正文)、appendix.tex (描述 + Table caption + 数据行)。这是最大的遗留问题。

**V-recovery 双种子**: method.tex 和 results.tex 已正确反映双种子。三个小问题：limitations.tex 段落标题仍为 "Single seed."（内容已更新）、abstract 只提 partial rebound 未提 full、"Triple-seed validation in progress" 需确认是否过时。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "uuid": "3f099ae4-9d21-4d2f-9271-0ca0ca0cd54f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJcaJuUASobt1C4LU3mPDC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 528,
      "cache_read_input_tokens": 62590,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 528
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

_source line 53_

审计完成。核心发现：

**Algorithm 1**: 代码与 artifacts 伪代码完全一致。论文版本将 `V-recovery-full` 合并为 `V-recovery`（5 patterns vs 代码 6 patterns），逻辑分支全部匹配，仅标签不同。需决定是否对齐。

**Sensitivity**: **全部 6 处仍写 "30 combinations"，未更新为 180。** 涉及 method.tex、results.tex (Table 1 caption + 正文)、appendix.tex (描述 + Table caption + 数据行)。这是最大的遗留问题。

**V-recovery 双种子**: method.tex 和 results.tex 已正确反映双种子。三个小问题：limitations.tex 段落标题仍为 "Single seed."（内容已更新）、abstract 只提 partial rebound 未提 full、"Triple-seed validation in progress" 需确认是否过时。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 190653,
  "duration_api_ms": 191592,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "a012cf11-488b-4274-99d2-96c524f0fa73",
  "total_cost_usd": 0.79308625,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 51277,
    "cache_read_input_tokens": 437308,
    "output_tokens": 10037,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 51277,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 272,
        "cache_read_input_tokens": 62590,
        "cache_creation_input_tokens": 528,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 528
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2861,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002956,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 10037,
      "cacheReadInputTokens": 437308,
      "cacheCreationInputTokens": 51277,
      "webSearchRequests": 0,
      "costUSD": 0.79013025,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "95458376-90c4-49fa-b3e5-994fe4497a06"
}
```

</details>

---
