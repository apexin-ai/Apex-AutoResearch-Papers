# Research conversation: I need to verify specific numbers from a paper about correction methods. Read these files thoroughly and report exact va

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9bc92f8d50dd2489.jsonl`
- **Structured JSON:** [`6d56f06b6c677da4913a.json`](../../sessions/6d/6d56f06b6c677da4913a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-25T20:19:49.051Z_

I need to verify specific numbers from a paper about correction methods. Read these files thoroughly and report exact values:

1. Read `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan007_rmse_correction_results.json` - find PPI++ RMSE reduction, bias reduction values for each topology, and especially M-bias results.

2. Read `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan007/correction_guidance_results.json` - find all method results per topology, especially MC-SIMEX and PPI++ for M-bias, front-door.

3. Read `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/table3_source_data.txt` - full contents.

4. Read `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json` - find max epsilon values.

5. Read `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_extended_results.json` or any file with "conjecture" in the name that has epsilon values.

6. Search for any file in artifacts/ containing "82" and "gold" or "stability" - looking for the 82% ASV stability claim.

7. Read `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_fwl_nonlinear_scaling_results.json` - find the delta or difference between linear and logistic results.

8. Search in artifacts/ for files related to "sign_reversal" counting 14 out of 23 configurations.

Report every exact number you find with its file path and JSON key path.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "b8b18c68-23fb-4c66-af17-cf9e1f552db5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T20:19:53.227Z_

I'll systematically read and search through these files to extract the exact values you need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8b18c68-23fb-4c66-af17-cf9e1f552db5",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZDysdHEq6GSpiTXhs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "43eaba58-ce3d-40fb-b05b-76c1c546d22f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cp4iMsNEMRH6PtDfCPtx1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 899,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 3 · 2026-05-25T20:19:53.477Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FUPg3hQRD8mWARhWzUxRHk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan007_rmse_correction_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43eaba58-ce3d-40fb-b05b-76c1c546d22f",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZDysdHEq6GSpiTXhs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "78bca96b-8af1-41e4-9ecc-278ab5458fa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cp4iMsNEMRH6PtDfCPtx1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 899,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 4 · 2026-05-25T20:19:53.496Z_

<details><summary>↩ Tool result · `toolu_01FUPg3hQRD8mWARhWzUxRHk`</summary>

```text
1	{
2	  "meta": {
3	    "source": "plan007 correction_guidance_results.json",
4	    "n_sim": 1000,
5	    "n_scenarios": 42,
6	    "topologies": 7,
7	    "c_structures": 6,
8	    "methods": 5,
9	    "note": "RMSE reduction computed as 1 - rmse_corrected/rmse_uncorrected"
10	  },
11	  "grand_means": {
12	    "ppi": {
13	      "bias_reduction_pct": 93.8,
14	      "rmse_reduction_pct": 47.0,
15	      "abs_rmse": 0.0797,
16	      "coverage_95_pct": 96.8,
17	      "inflation_ratio": 2.0
18	    },
19	    "mcsimex": {
20	      "bias_reduction_pct": 20.9,
21	      "rmse_reduction_pct": 13.3,
22	      "abs_rmse": 0.3803,
23	      "coverage_95_pct": 37.6,
24	      "inflation_ratio": 1.57
25	    },
26	    "naive_plugin": {
27	      "bias_reduction_pct": -20.0,
28	      "rmse_reduction_pct": -19.7,
29	      "abs_rmse": 0.418,
30	      "coverage_95_pct": 14.6,
31	      "inflation_ratio": 1.02
32	    },
33	    "dsl": {
34	      "bias_reduction_pct": -144.8,
35	      "rmse_reduction_pct": -79.0,
36	      "abs_rmse": 0.4994,
37	      "coverage_95_pct": 6.5,
38	      "inflation_ratio": 1.83
39	    },
40	    "mla": {
41	      "bias_reduction_pct": -37.4,
42	      "rmse_reduction_pct": -37.0,
43	      "abs_rmse": 0.5794,
44	      "coverage_95_pct": 14.6,
45	      "inflation_ratio": 1.01
46	    }
47	  },
48	  "ppi_by_topology": {
49	    "confounding": {
50	      "bias_reduction_pct": 99.3,
51	      "rmse_reduction_pct": 83.2,
52	      "n_configs": 6
53	    },
54	    "mediation": {
55	      "bias_reduction_pct": 98.8,
56	      "rmse_reduction_pct": 54.1,
57	      "n_configs": 6
58	    },
59	    "collider": {
60	      "bias_reduction_pct": 97.0,
61	      "rmse_reduction_pct": 50.5,
62	      "n_configs": 6
63	    },
64	    "exposure": {
65	      "bias_reduction_pct": 98.8,
66	      "rmse_reduction_pct": 75.5,
67	      "n_configs": 6
68	    },
69	    "mbias": {
70	      "bias_reduction_pct": 63.7,
71	      "rmse_reduction_pct": -88.0,
72	      "n_configs": 6
73	    },
74	    "iv": {
75	      "bias_reduction_pct": 99.5,
76	      "rmse_reduction_pct": 79.4,
77	      "n_configs": 6
78	    },
79	    "frontdoor": {
80	      "bias_reduction_pct": 99.3,
81	      "rmse_reduction_pct": 74.1,
82	      "n_configs": 6
83	    }
84	  },
85	  "mcsimex_by_topology": {
86	    "confounding": {
87	      "bias_reduction_pct": 35.9,
88	      "rmse_reduction_pct": 35.1,
89	      "n_configs": 6
90	    },
91	    "mediation": {
92	      "bias_reduction_pct": 42.4,
93	      "rmse_reduction_pct": 39.1,
94	      "n_configs": 6
95	    },
96	    "collider": {
97	      "bias_reduction_pct": 37.1,
98	      "rmse_reduction_pct": 31.8,
99	      "n_configs": 6
100	    },
101	    "exposure": {
102	      "bias_reduction_pct": -3.8,
103	      "rmse_reduction_pct": -9.8,
104	      "n_configs": 6
105	    },
106	    "mbias": {
107	      "bias_reduction_pct": 25.7,
108	      "rmse_reduction_pct": 0.1,
109	      "n_configs": 6
110	    },
111	    "iv": {
112	      "bias_reduction_pct": 64.7,
113	      "rmse_reduction_pct": 59.4,
114	      "n_configs": 6
115	    },
116	    "frontdoor": {
117	      "bias_reduction_pct": -55.7,
118	      "rmse_reduction_pct": -62.4,
119	      "n_configs": 6
120	    }
121	  },
122	  "all_methods_by_topology": {
123	    "confounding": {
124	      "ppi": {
125	        "bias_reduction_pct": 99.3,
126	        "rmse_reduction_pct": 83.2
127	      },
128	      "mcsimex": {
129	        "bias_reduction_pct": 35.9,
130	        "rmse_reduction_pct": 35.1
131	      },
132	      "naive_plugin": {
133	        "bias_reduction_pct": 0.0,
134	        "rmse_reduction_pct": 0.0
135	      },
136	      "dsl": {
137	        "bias_reduction_pct": 49.8,
138	        "rmse_reduction_pct": 48.0
139	      },
140	      "mla": {
141	        "bias_reduction_pct": -0.0,
142	        "rmse_reduction_pct": 0.0
143	      }
144	    },
145	    "mediation": {
146	      "ppi": {
147	        "bias_reduction_pct": 98.8,
148	        "rmse_reduction_pct": 54.1
149	      },
150	      "mcsimex": {
151	        "bias_reduction_pct": 42.4,
152	        "rmse_reduction_pct": 39.1
153	      },
154	      "naive_plugin": {
155	        "bias_reduction_pct": -0.0,
156	        "rmse_reduction_pct": -0.0
157	      },
158	      "dsl": {
159	        "bias_reduction_pct": 70.3,
160	        "rmse_reduction_pct": 52.9
161	      },
162	      "mla": {
163	        "bias_reduction_pct": 0.0,
164	        "rmse_reduction_pct": -0.0
165	      }
166	    },
167	    "collider": {
168	      "ppi": {
169	        "bias_reduction_pct": 97.0,
170	        "rmse_reduction_pct": 50.5
171	      },
172	      "mcsimex": {
173	        "bias_reduction_pct": 37.1,
174	        "rmse_reduction_pct": 31.8
175	      },
176	      "naive_plugin": {
177	        "bias_reduction_pct": 0.0,
178	        "rmse_reduction_pct": 0.0
179	      },
180	      "dsl": {
181	        "bias_reduction_pct": -89.2,
182	        "rmse_reduction_pct": -92.6
183	      },
184	      "mla": {
185	        "bias_reduction_pct": 0.0,
186	        "rmse_reduction_pct": 0.0
187	      }
188	    },
189	    "exposure": {
190	      "ppi": {
191	        "bias_reduction_pct": 98.8,
192	        "rmse_reduction_pct": 75.5
193	      },
194	      "mcsimex": {
195	        "bias_reduction_pct": -3.8,
196	        "rmse_reduction_pct": -9.8
197	      },
198	      "naive_plugin": {
199	        "bias_reduction_pct": -45.6,
200	        "rmse_reduction_pct": -44.8
201	      },
202	      "dsl": {
203	        "bias_reduction_pct": -59.6,
204	        "rmse_reduction_pct": -59.5
205	      },
206	      "mla": {
207	        "bias_reduction_pct": -89.9,
208	        "rmse_reduction_pct": -89.0
209	      }
210	    },
211	    "mbias": {
212	      "ppi": {
213	        "bias_reduction_pct": 63.7,
214	        "rmse_reduction_pct": -88.0
215	      },
216	      "mcsimex": {
217	        "bias_reduction_pct": 25.7,
218	        "rmse_reduction_pct": 0.1
219	      },
220	      "naive_plugin": {
221	        "bias_reduction_pct": 0.0,
222	        "rmse_reduction_pct": 0.0
223	      },
224	      "dsl": {
225	        "bias_reduction_pct": -768.0,
226	        "rmse_reduction_pct": -266.9
227	      },
228	      "mla": {
229	        "bias_reduction_pct": 0.0,
230	        "rmse_reduction_pct": 0.0
231	      }
232	    },
233	    "iv": {
234	      "ppi": {
235	        "bias_reduction_pct": 99.5,
236	        "rmse_reduction_pct": 79.4
237	      },
238	      "mcsimex": {
239	        "bias_reduction_pct": 64.7,
240	        "rmse_reduction_pct": 59.4
241	      },
242	      "naive_plugin": {
243	        "bias_reduction_pct": -40.9,
244	        "rmse_reduction_pct": -40.4
245	      },
246	      "dsl": {
247	        "bias_reduction_pct": -187.4,
248	        "rmse_reduction_pct": -206.1
249	      },
250	      "mla": {
251	        "bias_reduction_pct": -59.2,
252	        "rmse_reduction_pct": -58.7
253	      }
254	    },
255	    "frontdoor": {
256	      "ppi": {
257	        "bias_reduction_pct": 99.3,
258	        "rmse_reduction_pct": 74.1
259	      },
260	      "mcsimex": {
261	        "bias_reduction_pct": -55.7,
262	        "rmse_reduction_pct": -62.4
263	      },
264	      "naive_plugin": {
265	        "bias_reduction_pct": -53.5,
266	        "rmse_reduction_pct": -52.7
267	      },
268	      "dsl": {
269	        "bias_reduction_pct": -29.2,
270	        "rmse_reduction_pct": -29.0
271	      },
272	      "mla": {
273	        "bias_reduction_pct": -112.5,
274	        "rmse_reduction_pct": -111.5
275	      }
276	    }
277	  },
278	  "key_finding": {
279	    "issue": "bias_reduction systematically inflates correction effectiveness vs RMSE reduction",
280	    "ppi_inflation": "93.8% (bias_red) vs 47.0% (rmse_red) = 2.00x",
281	    "mcsimex_inflation": "20.9% (bias_red) vs 13.3% (rmse_red) = 1.57x",
282	    "ppi_mbias_warning": "PPI bias_red=63.7% but rmse_red=-88.0% (PPI increases RMSE on mbias)",
283	    "recommendation": "Report RMSE reduction alongside bias reduction; revise \u00a75.5 PPI++ numbers"
284	  }
285	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78bca96b-8af1-41e4-9ecc-278ab5458fa6",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "1f54fe3d-4e0d-4540-bd0a-f4f2f80c5bed",
  "sourceToolAssistantUUID": "78bca96b-8af1-41e4-9ecc-278ab5458fa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T20:19:53.673Z_

<details open><summary>🔧 Tool call — Read · `toolu_016B4GZNXvoAYYs2mCbELp9V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan007/correction_guidance_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f54fe3d-4e0d-4540-bd0a-f4f2f80c5bed",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZDysdHEq6GSpiTXhs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "da25f068-747c-4c8e-96ae-458692134fbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cp4iMsNEMRH6PtDfCPtx1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 899,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 6 · 2026-05-25T20:19:53.939Z_

<details open><summary>🔧 Tool call — Read · `toolu_012SLRb2sZXDKFfqo9sdCEKf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/table3_source_data.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da25f068-747c-4c8e-96ae-458692134fbf",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZDysdHEq6GSpiTXhs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "52a3f046-da6c-4e9e-96f8-25326f2f5ad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cp4iMsNEMRH6PtDfCPtx1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 899,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 7 · 2026-05-25T20:19:53.966Z_

<details><summary>↩ Tool result · reported error · `toolu_016B4GZNXvoAYYs2mCbELp9V`</summary>

```text
File content (38707 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da25f068-747c-4c8e-96ae-458692134fbf",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "672648c1-6f00-4363-b641-811aa0e17c22",
  "toolUseResult": "Error: File content (38707 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "da25f068-747c-4c8e-96ae-458692134fbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T20:19:53.946Z_

<details><summary>↩ Tool result · `toolu_012SLRb2sZXDKFfqo9sdCEKf`</summary>

```text
1	TABLE 3 DATA: Mean Bias Reduction (%) by Topology × Method
2	============================================================
3	Source: correction_guidance_results.json (plan007, 210 records)
4	Run: 7 topologies × 5 methods × 6 C structures × 1000 sims
5	Extracted from: worker_infra_plan007-status-check (2026-05-20T20:45)
6	Values: already in percentage (no ×100 needed)
7	
8	=== BIAS REDUCTION (%) — mean over 6 C structures ===
9	
10	Topology        | Naive      | MLA        | DSL        | MC-SIMEX   | PPI++
11	----------------|------------|------------|------------|------------|----------
12	confounding     |    -0.0    |     0.0    |     49.8   |     35.9   |     99.3
13	mediation       |    -0.0    |     0.0    |     70.3   |     42.4   |     98.8
14	collider        |     0.0    |    -0.0    |    -89.2   |     37.1   |     97.0
15	mbias           |     0.0    |     0.0    |   -768.0   |     25.7   |     63.7
16	----------------|------------|------------|------------|------------|----------
17	frontdoor       |   -53.5    |  -112.5    |    -29.2   |    -55.7   |     99.3
18	exposure        |   -45.6    |   -89.9    |    -59.6   |     -3.8   |     98.8
19	iv              |   -40.9    |   -59.2    |   -187.4   |     64.7   |     99.5
20	----------------|------------|------------|------------|------------|----------
21	Grand Mean      |   -20.0    |   -37.4    |   -144.8   |     20.9   |     93.8
22	
23	=== COVERAGE 95% — mean over 6 C structures ===
24	
25	Topology        | Naive      | MLA        | DSL        | MC-SIMEX   | PPI++
26	----------------|------------|------------|------------|------------|----------
27	confounding     |     0.0    |     0.0    |      6.1   |      0.8   |     98.6
28	mediation       |     2.0    |     2.0    |     27.6   |     22.2   |     96.8
29	collider        |     8.3    |     8.3    |      1.3   |     32.1   |     99.2
30	mbias           |    92.1    |    92.1    |     10.8   |     92.6   |     98.5
31	frontdoor       |     0.0    |     0.0    |      0.0   |     41.1   |     94.8
32	exposure        |     0.0    |     0.0    |      0.0   |     37.4   |     95.0
33	iv              |     0.0    |     0.0    |      0.0   |     36.8   |     94.7
34	----------------|------------|------------|------------|------------|----------
35	Grand Mean      |    14.6    |    14.6    |      6.5   |     37.6   |     96.8
36	
37	=== DISCREPANCIES vs. PAPER (experiments.tex tab:correction) ===
38	
39	Paper values that DIFFER from JSON source data:
40	
41	  Topology      | Method   | Paper  | JSON   | Delta
42	  --------------|----------|--------|--------|--------
43	  confounding   | SIMEX    |  30.1  |  35.9  |  +5.8
44	  confounding   | PPI++    |  97.8  |  99.3  |  +1.5
45	  mediation     | SIMEX    |  24.6  |  42.4  | +17.8
46	  collider      | PPI++    |  98.6  |  97.0  |  -1.6
47	  collider      | SIMEX    |  12.4  |  37.1  | +24.7
48	  mbias         | SIMEX    |   5.1  |  25.7  | +20.6
49	  frontdoor     | Naive    |   <0   | -53.5  |  (paper imprecise)
50	  frontdoor     | MLA      |   <0   | -112.5 |  (paper imprecise)
51	  frontdoor     | SIMEX    |   8.7  | -55.7  | -64.4  *** SIGN FLIP ***
52	  frontdoor     | PPI++    |  99.9  |  99.3  |  -0.6
53	  exposure      | Naive    |   <0   | -45.6  |  (paper imprecise)
54	  exposure      | MLA      |   <0   | -89.9  |  (paper imprecise)
55	  exposure      | SIMEX    |   1.0  |  -3.8  |  -4.8  *** SIGN FLIP ***
56	  exposure      | PPI++    |  98.9  |  98.8  |  -0.1
57	  iv            | Naive    |   <0   | -40.9  |  (paper imprecise)
58	  iv            | MLA      |   <0   | -59.2  |  (paper imprecise)
59	  iv            | PPI++    |  98.4  |  99.5  |  +1.1
60	
61	Values that MATCH:
62	  mediation     | DSL      |  70.3  |  70.3  ✓
63	  mediation     | PPI++    |  99.3  |  (JSON 98.8, paper 99.3 — MISMATCH)
64	  mbias         | PPI++    |  63.7  |  63.7  ✓
65	  iv            | SIMEX    |  64.7  |  64.7  ✓
66	  DSL approx matches: confounding 49.8✓, collider -89≈-89.2, mbias -768≈-768.0,
67	                       frontdoor -29≈-29.2, exposure -60≈-59.6, iv -187≈-187.4
68	
69	Grand means ALL match (both paper and JSON):
70	  Naive: -20.0  MLA: -37.4  DSL: -144.8  MC-SIMEX: 20.9  PPI++: 93.8
71	
72	=== CRITICAL DISCREPANCIES ===
73	
74	MC-SIMEX has the most discrepancies — several cells differ by >20 percentage points
75	and two have sign flips (frontdoor: paper +8.7 vs JSON -55.7; exposure: paper +1.0
76	vs JSON -3.8). Despite this, the grand mean matches exactly (20.9%), suggesting
77	the paper may have used a different aggregation or an earlier partial run for
78	individual values but computed grand means from the full data.
79	
80	=== RAW FIELD NAMES ===
81	
82	Topologies in JSON: confounding, mediation, collider, exposure, mbias, iv, frontdoor
83	Methods in JSON: naive_plugin, dsl, ppi, mcsimex, mla
84	C structures (6): mild_uniform, moderate_uniform, severe_uniform, asymmetric,
85	                   near_permutation, realistic_llm
86	Records: 210 total (7 × 5 × 6)
87	Metric field: bias_reduction (already in %, not 0-1)
88	
89	=== PPI MBIAS DETAIL (per C structure) ===
90	
91	mbias + realistic_llm:    -25.1% bias_red, 99.0% coverage
92	mbias + mild_uniform:      62.5% bias_red, 98.3% coverage
93	mbias + near_permutation:  69.9% bias_red, 98.6% coverage
94	mbias + asymmetric:        82.9% bias_red, 98.7% coverage
95	mbias + severe_uniform:    93.3% bias_red, 98.1% coverage
96	
97	=== WIN RATE ===
98	
99	PPI++ wins 40/42 topology×C-structure configurations (95.2%)
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52a3f046-da6c-4e9e-96f8-25326f2f5ad3",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "7f983374-5111-473a-99ca-fb7822d8272c",
  "sourceToolAssistantUUID": "52a3f046-da6c-4e9e-96f8-25326f2f5ad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T20:19:54.097Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MUV8jemXyPHpp2GTkWYizi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f983374-5111-473a-99ca-fb7822d8272c",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZDysdHEq6GSpiTXhs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "402d545c-d67c-4354-b1dc-c82b34e52e39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cp4iMsNEMRH6PtDfCPtx1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 899,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 10 · 2026-05-25T20:19:54.104Z_

<details><summary>↩ Tool result · `toolu_01MUV8jemXyPHpp2GTkWYizi`</summary>

```text
1	{
2	  "description": "Adversarial envelope monotonicity test for Conjecture 1",
3	  "config": {
4	    "K_values": [
5	      3,
6	      5,
7	      7
8	    ],
9	    "adversarial_types": [
10	      "near_perm",
11	      "block_diag",
12	      "sparse",
13	      "near_uniform"
14	    ],
15	    "adversarial_params": {
16	      "near_perm": [
17	        {
18	          "eps": 0.05
19	        },
20	        {
21	          "eps": 0.1
22	        },
23	        {
24	          "eps": 0.2
25	        }
26	      ],
27	      "block_diag": [
28	        {}
29	      ],
30	      "sparse": [
31	        {
32	          "p_diag": 0.3
33	        },
34	        {
35	          "p_diag": 0.5
36	        },
37	        {
38	          "p_diag": 0.7
39	        }
40	      ],
41	      "near_uniform": [
42	        {
43	          "eps": 0.01
44	        },
45	        {
46	          "eps": 0.05
47	        }
48	      ]
49	    },
50	    "topologies": [
51	      "confounding",
52	      "mediation",
53	      "collider",
54	      "exposure",
55	      "mbias",
56	      "iv",
57	      "frontdoor"
58	    ],
59	    "beta_configs": [
60	      "alternating_large",
61	      "same_sign",
62	      "alternating_small"
63	    ],
64	    "n_C0_per_cell": 1000,
65	    "n_delta_steps": 101,
66	    "delta_step": 0.01,
67	    "eps_threshold": 0.001,
68	    "seed": 2024
69	  },
70	  "summary": {
71	    "total_curves": 545945,
72	    "non_monotone_fraction": 0.119392979146251,
73	    "max_eps_abs": 0.01636529529573094,
74	    "median_eps_abs": 0.0,
75	    "mean_eps_abs": 0.00047588204649284187,
76	    "p95_eps_abs": 0.00255148755548662,
77	    "p99_eps_abs": 0.008253228263722434,
78	    "safe_topo_max_eps": 0.01636529529573094,
79	    "fragile_topo_max_eps": 0.013176775652375183,
80	    "total_weak_iv_filtered": 21055,
81	    "total_skipped_zero_tau": 0
82	  },
83	  "by_adversarial_type": {
84	    "near_perm": {
85	      "total_curves": 172403,
86	      "non_monotone_count": 61004,
87	      "non_monotone_fraction": 0.353845350718955,
88	      "max_eps_abs": 0.01636529529573094
89	    },
90	    "block_diag": {
91	      "total_curves": 63000,
92	      "non_monotone_count": 0,
93	      "non_monotone_fraction": 0.0,
94	      "max_eps_abs": 0.0003959986339877597
95	    },
96	    "sparse": {
97	      "total_curves": 184542,
98	      "non_monotone_count": 4178,
99	      "non_monotone_fraction": 0.022639832666818394,
100	      "max_eps_abs": 0.0026147855238671802
101	    },
102	    "near_uniform": {
103	      "total_curves": 126000,
104	      "non_monotone_count": 0,
105	      "non_monotone_fraction": 0.0,
106	      "max_eps_abs": 0.0
107	    }
108	  },
109	  "by_topology": {
110	    "confounding": {
111	      "total_curves": 81000,
112	      "non_monotone_count": 17407,
113	      "non_monotone_fraction": 0.21490123456790122,
114	      "max_eps_abs": 0.01636529529573094
115	    },
116	    "mediation": {
117	      "total_curves": 81000,
118	      "non_monotone_count": 15990,
119	      "non_monotone_fraction": 0.19740740740740742,
120	      "max_eps_abs": 0.013039414209438105
121	    },
122	    "collider": {
123	      "total_curves": 81000,
124	      "non_monotone_count": 14031,
125	      "non_monotone_fraction": 0.17322222222222222,
126	      "max_eps_abs": 0.013176775652375183
127	    },
128	    "exposure": {
129	      "total_curves": 81000,
130	      "non_monotone_count": 594,
131	      "non_monotone_fraction": 0.007333333333333333,
132	      "max_eps_abs": 0.008412534039272668
133	    },
134	    "mbias": {
135	      "total_curves": 81000,
136	      "non_monotone_count": 1163,
137	      "non_monotone_fraction": 0.014358024691358025,
138	      "max_eps_abs": 0.001532019782881644
139	    },
140	    "iv": {
141	      "total_curves": 59945,
142	      "non_monotone_count": 0,
143	      "non_monotone_fraction": 0.0,
144	      "max_eps_abs": 0.0
145	    },
146	    "frontdoor": {
147	      "total_curves": 81000,
148	      "non_monotone_count": 15997,
149	      "non_monotone_fraction": 0.19749382716049382,
150	      "max_eps_abs": 0.01582784663255976
151	    }
152	  },
153	  "by_K": {
154	    "3": {
155	      "total_curves": 180683,
156	      "non_monotone_count": 26007,
157	      "non_monotone_fraction": 0.14393717173170692,
158	      "max_eps_abs": 0.01636529529573094
159	    },
160	    "5": {
161	      "total_curves": 182402,
162	      "non_monotone_count": 21721,
163	      "non_monotone_fraction": 0.11908312408855166,
164	      "max_eps_abs": 0.013448880884805892
165	    },
166	    "7": {
167	      "total_curves": 182860,
168	      "non_monotone_count": 17454,
169	      "non_monotone_fraction": 0.09545007109263917,
170	      "max_eps_abs": 0.012378423243947445
171	    }
172	  },
173	  "worst_cases": [
174	    {
175	      "topology": "confounding",
176	      "K": 3,
177	      "adversarial": "near_perm",
178	      "adv_config": "{\"eps\": 0.05}",
179	      "beta": "alternating_large",
180	      "eps_abs": 0.01636529529573094,
181	      "non_mono_frac": 0.812,
182	      "n_valid": 1000,
183	      "weak_iv": 0
184	    },
185	    {
186	      "topology": "frontdoor",
187	      "K": 3,
188	      "adversarial": "near_perm",
189	      "adv_config": "{\"eps\": 0.05}",
190	      "beta": "alternating_large",
191	      "eps_abs": 0.01582784663255976,
192	      "non_mono_frac": 0.838,
193	      "n_valid": 1000,
194	      "weak_iv": 0
195	    },
196	    {
197	      "topology": "confounding",
198	      "K": 5,
199	      "adversarial": "near_perm",
200	      "adv_config": "{\"eps\": 0.05}",
201	      "beta": "alternating_large",
202	      "eps_abs": 0.013448880884805892,
203	      "non_mono_frac": 0.914,
204	      "n_valid": 1000,
205	      "weak_iv": 0
206	    },
207	    {
208	      "topology": "collider",
209	      "K": 3,
210	      "adversarial": "near_perm",
211	      "adv_config": "{\"eps\": 0.05}",
212	      "beta": "alternating_large",
213	      "eps_abs": 0.013176775652375183,
214	      "non_mono_frac": 0.827,
215	      "n_valid": 1000,
216	      "weak_iv": 0
217	    },
218	    {
219	      "topology": "frontdoor",
220	      "K": 3,
221	      "adversarial": "near_perm",
222	      "adv_config": "{\"eps\": 0.1}",
223	      "beta": "alternating_large",
224	      "eps_abs": 0.013119570146454929,
225	      "non_mono_frac": 0.664,
226	      "n_valid": 1000,
227	      "weak_iv": 0
228	    },
229	    {
230	      "topology": "mediation",
231	      "K": 3,
232	      "adversarial": "near_perm",
233	      "adv_config": "{\"eps\": 0.05}",
234	      "beta": "alternating_large",
235	      "eps_abs": 0.013039414209438105,
236	      "non_mono_frac": 0.643,
237	      "n_valid": 1000,
238	      "weak_iv": 0
239	    },
240	    {
241	      "topology": "confounding",
242	      "K": 3,
243	      "adversarial": "near_perm",
244	      "adv_config": "{\"eps\": 0.1}",
245	      "beta": "alternating_large",
246	      "eps_abs": 0.012757437777432656,
247	      "non_mono_frac": 0.67,
248	      "n_valid": 1000,
249	      "weak_iv": 0
250	    },
251	    {
252	      "topology": "confounding",
253	      "K": 7,
254	      "adversarial": "near_perm",
255	      "adv_config": "{\"eps\": 0.05}",
256	      "beta": "alternating_large",
257	      "eps_abs": 0.012378423243947445,
258	      "non_mono_frac": 0.946,
259	      "n_valid": 1000,
260	      "weak_iv": 0
261	    },
262	    {
263	      "topology": "frontdoor",
264	      "K": 5,
265	      "adversarial": "near_perm",
266	      "adv_config": "{\"eps\": 0.05}",
267	      "beta": "alternating_large",
268	      "eps_abs": 0.012015795320587164,
269	      "non_mono_frac": 0.907,
270	      "n_valid": 1000,
271	      "weak_iv": 0
272	    },
273	    {
274	      "topology": "collider",
275	      "K": 3,
276	      "adversarial": "near_perm",
277	      "adv_config": "{\"eps\": 0.1}",
278	      "beta": "alternating_large",
279	      "eps_abs": 0.011415854138354109,
280	      "non_mono_frac": 0.635,
281	      "n_valid": 1000,
282	      "weak_iv": 0
283	    },
284	    {
285	      "topology": "collider",
286	      "K": 5,
287	      "adversarial": "near_perm",
288	      "adv_config": "{\"eps\": 0.05}",
289	      "beta": "alternating_large",
290	      "eps_abs": 0.011211164249701366,
291	      "non_mono_frac": 0.915,
292	      "n_valid": 1000,
293	      "weak_iv": 0
294	    },
295	    {
296	      "topology": "mediation",
297	      "K": 3,
298	      "adversarial": "near_perm",
299	      "adv_config": "{\"eps\": 0.1}",
300	      "beta": "alternating_large",
301	      "eps_abs": 0.011106313189383377,
302	      "non_mono_frac": 0.682,
303	      "n_valid": 1000,
304	      "weak_iv": 0
305	    },
306	    {
307	      "topology": "confounding",
308	      "K": 5,
309	      "adversarial": "near_perm",
310	      "adv_config": "{\"eps\": 0.1}",
311	      "beta": "alternating_large",
312	      "eps_abs": 0.01085926805028814,
313	      "non_mono_frac": 0.89,
314	      "n_valid": 1000,
315	      "weak_iv": 0
316	    },
317	    {
318	      "topology": "frontdoor",
319	      "K": 5,
320	      "adversarial": "near_perm",
321	      "adv_config": "{\"eps\": 0.1}",
322	      "beta": "alternating_large",
323	      "eps_abs": 0.010074228393916806,
324	      "non_mono_frac": 0.896,
325	      "n_valid": 1000,
326	      "weak_iv": 0
327	    },
328	    {
329	      "topology": "confounding",
330	      "K": 7,
331	      "adversarial": "near_perm",
332	      "adv_config": "{\"eps\": 0.1}",
333	      "beta": "alternating_large",
334	      "eps_abs": 0.009905378807955945,
335	      "non_mono_frac": 0.892,
336	      "n_valid": 1000,
337	      "weak_iv": 0
338	    },
339	    {
340	      "topology": "collider",
341	      "K": 5,
342	      "adversarial": "near_perm",
343	      "adv_config": "{\"eps\": 0.1}",
344	      "beta": "alternating_large",
345	      "eps_abs": 0.009822338162834399,
346	      "non_mono_frac": 0.863,
347	      "n_valid": 1000,
348	      "weak_iv": 0
349	    },
350	    {
351	      "topology": "frontdoor",
352	      "K": 7,
353	      "adversarial": "near_perm",
354	      "adv_config": "{\"eps\": 0.05}",
355	      "beta": "alternating_large",
356	      "eps_abs": 0.009736569531234363,
357	      "non_mono_frac": 0.939,
358	      "n_valid": 1000,
359	      "weak_iv": 0
360	    },
361	    {
362	      "topology": "collider",
363	      "K": 7,
364	      "adversarial": "near_perm",
365	      "adv_config": "{\"eps\": 0.05}",
366	      "beta": "alternating_large",
367	      "eps_abs": 0.009616219166313389,
368	      "non_mono_frac": 0.929,
369	      "n_valid": 1000,
370	      "weak_iv": 0
371	    },
372	    {
373	      "topology": "mediation",
374	      "K": 5,
375	      "adversarial": "near_perm",
376	      "adv_config": "{\"eps\": 0.05}",
377	      "beta": "alternating_large",
378	      "eps_abs": 0.009526241091829313,
379	      "non_mono_frac": 0.907,
380	      "n_valid": 1000,
381	      "weak_iv": 0
382	    },
383	    {
384	      "topology": "frontdoor",
385	      "K": 3,
386	      "adversarial": "near_perm",
387	      "adv_config": "{\"eps\": 0.2}",
388	      "beta": "alternating_large",
389	      "eps_abs": 0.009193851154494781,
390	      "non_mono_frac": 0.644,
391	      "n_valid": 1000,
392	      "weak_iv": 0
393	    }
394	  ],
395	  "elapsed_seconds": 135.75384545326233
396	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "402d545c-d67c-4354-b1dc-c82b34e52e39",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "9025e275-f310-48af-bbb1-87752d658f9c",
  "sourceToolAssistantUUID": "402d545c-d67c-4354-b1dc-c82b34e52e39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T20:19:54.516Z_

<details open><summary>🔧 Tool call — Read · `toolu_018AJr1JSKfs2tNEaEr6x3bR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_fwl_nonlinear_scaling_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9025e275-f310-48af-bbb1-87752d658f9c",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZDysdHEq6GSpiTXhs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bc3259e8-d73a-4d14-9b84-67c5aaa49c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cp4iMsNEMRH6PtDfCPtx1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 899,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 12 · 2026-05-25T20:19:54.751Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PEbsySa9cZ4fWzVREFnRpq`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/*conjecture*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc3259e8-d73a-4d14-9b84-67c5aaa49c50",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZDysdHEq6GSpiTXhs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eecf1863-c6bc-475d-b2e1-36ce2969fde7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cp4iMsNEMRH6PtDfCPtx1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 899,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 13 · 2026-05-25T20:19:54.784Z_

<details><summary>↩ Tool result · `toolu_018AJr1JSKfs2tNEaEr6x3bR`</summary>

```text
1	{
2	  "config": {
3	    "K": 3,
4	    "N_values": [
5	      1000,
6	      5000,
7	      10000,
8	      50000
9	    ],
10	    "n_reps": 200,
11	    "seed": 20260523,
12	    "error_levels": {
13	      "low": 0.9,
14	      "medium": 0.7,
15	      "high": 0.5
16	    },
17	    "topologies": [
18	      "confounding",
19	      "mediation",
20	      "collider",
21	      "exposure",
22	      "mbias",
23	      "frontdoor"
24	    ]
25	  },
26	  "true_params": {
27	    "confounding": {
28	      "type": "covariate",
29	      "tau": 0.4191483797551854
30	    },
31	    "mediation": {
32	      "type": "covariate",
33	      "tau": 0.4129146956049203
34	    },
35	    "collider": {
36	      "type": "covariate",
37	      "tau": 0.37737229000398537
38	    },
39	    "exposure": {
40	      "type": "exposure",
41	      "coefs": [
42	        0.828824110401489,
43	        -0.4146559017290504
44	      ]
45	    },
46	    "mbias": {
47	      "type": "covariate",
48	      "tau": 0.381396437630352
49	    },
50	    "frontdoor": {
51	      "type": "covariate",
52	      "tau": 0.4075720875751266
53	    }
54	  },
55	  "confusion_matrices": {
56	    "low": [
57	      [
58	        0.9,
59	        0.04999999999999999,
60	        0.04999999999999999
61	      ],
62	      [
63	        0.04999999999999999,
64	        0.9,
65	        0.04999999999999999
66	      ],
67	      [
68	        0.04999999999999999,
69	        0.04999999999999999,
70	        0.9
71	      ]
72	    ],
73	    "medium": [
74	      [
75	        0.7,
76	        0.15000000000000002,
77	        0.15000000000000002
78	      ],
79	      [
80	        0.15000000000000002,
81	        0.7,
82	        0.15000000000000002
83	      ],
84	      [
85	        0.15000000000000002,
86	        0.15000000000000002,
87	        0.7
88	      ]
89	    ],
90	    "high": [
91	      [
92	        0.5,
93	        0.25,
94	        0.25
95	      ],
96	      [
97	        0.25,
98	        0.5,
99	        0.25
100	      ],
101	      [
102	        0.25,
103	        0.25,
104	        0.5
105	      ]
106	    ]
107	  },
108	  "results": [
109	    {
110	      "topology": "confounding",
111	      "N": 1000,
112	      "error_level": "low",
113	      "diag_val": 0.9,
114	      "logistic_mean_bias_reduction_pct": 0.0004455665542252402,
115	      "logistic_std_bias_reduction_pct": 0.009583407284664777,
116	      "logistic_median_bias_reduction_pct": -0.00012819856968704357,
117	      "linear_mean_bias_reduction_pct": -2.942091015256665e-17,
118	      "linear_std_bias_reduction_pct": 5.283165733166369e-16,
119	      "linear_median_bias_reduction_pct": 0.0,
120	      "logistic_n_valid": 200,
121	      "linear_n_valid": 200
122	    },
123	    {
124	      "topology": "confounding",
125	      "N": 1000,
126	      "error_level": "medium",
127	      "diag_val": 0.7,
128	      "logistic_mean_bias_reduction_pct": -0.0024025702739676256,
129	      "logistic_std_bias_reduction_pct": 0.018548470923649224,
130	      "logistic_median_bias_reduction_pct": -0.000636356418833528,
131	      "linear_mean_bias_reduction_pct": 3.2751579226442116e-17,
132	      "linear_std_bias_reduction_pct": 8.244702985061617e-16,
133	      "linear_median_bias_reduction_pct": 0.0,
134	      "logistic_n_valid": 200,
135	      "linear_n_valid": 200
136	    },
137	    {
138	      "topology": "confounding",
139	      "N": 1000,
140	      "error_level": "high",
141	      "diag_val": 0.5,
142	      "logistic_mean_bias_reduction_pct": 1.3424199038361561e-05,
143	      "logistic_std_bias_reduction_pct": 0.00364799086142817,
144	      "logistic_median_bias_reduction_pct": -0.00010420806246225212,
145	      "linear_mean_bias_reduction_pct": 2.325917236589703e-16,
146	      "linear_std_bias_reduction_pct": 7.886958650337054e-16,
147	      "linear_median_bias_reduction_pct": 2.220446049250313e-16,
148	      "logistic_n_valid": 200,
149	      "linear_n_valid": 200
150	    },
151	    {
152	      "topology": "confounding",
153	      "N": 5000,
154	      "error_level": "low",
155	      "diag_val": 0.9,
156	      "logistic_mean_bias_reduction_pct": -0.0027432883494885422,
157	      "logistic_std_bias_reduction_pct": 0.025383408307627673,
158	      "logistic_median_bias_reduction_pct": -0.00229950170065496,
159	      "linear_mean_bias_reduction_pct": 2.2759572004815708e-17,
160	      "linear_std_bias_reduction_pct": 5.203023811305314e-16,
161	      "linear_median_bias_reduction_pct": 0.0,
162	      "logistic_n_valid": 200,
163	      "linear_n_valid": 200
164	    },
165	    {
166	      "topology": "confounding",
167	      "N": 5000,
168	      "error_level": "medium",
169	      "diag_val": 0.7,
170	      "logistic_mean_bias_reduction_pct": 0.0003611327063119962,
171	      "logistic_std_bias_reduction_pct": 0.002609271636125122,
172	      "logistic_median_bias_reduction_pct": 0.00025557190467195845,
173	      "linear_mean_bias_reduction_pct": -7.771561172376097e-18,
174	      "linear_std_bias_reduction_pct": 8.871724042303079e-16,
175	      "linear_median_bias_reduction_pct": 0.0,
176	      "logistic_n_valid": 200,
177	      "linear_n_valid": 200
178	    },
179	    {
180	      "topology": "confounding",
181	      "N": 5000,
182	      "error_level": "high",
183	      "diag_val": 0.5,
184	      "logistic_mean_bias_reduction_pct": -0.000701988095087796,
185	      "logistic_std_bias_reduction_pct": 0.001903994043271603,
186	      "logistic_median_bias_reduction_pct": -0.0006673986212056837,
187	      "linear_mean_bias_reduction_pct": 7.605027718682323e-17,
188	      "linear_std_bias_reduction_pct": 6.076458130448115e-16,
189	      "linear_median_bias_reduction_pct": 0.0,
190	      "logistic_n_valid": 200,
191	      "linear_n_valid": 200
192	    },
193	    {
194	      "topology": "confounding",
195	      "N": 10000,
196	      "error_level": "low",
197	      "diag_val": 0.9,
198	      "logistic_mean_bias_reduction_pct": -0.006854961591573993,
199	      "logistic_std_bias_reduction_pct": 0.04059390243412448,
200	      "logistic_median_bias_reduction_pct": -0.0032269009309757735,
201	      "linear_mean_bias_reduction_pct": 2.831068712794149e-17,
202	      "linear_std_bias_reduction_pct": 4.998467081782937e-16,
203	      "linear_median_bias_reduction_pct": 0.0,
204	      "logistic_n_valid": 200,
205	      "linear_n_valid": 200
206	    },
207	    {
208	      "topology": "confounding",
209	      "N": 10000,
210	      "error_level": "medium",
211	      "diag_val": 0.7,
212	      "logistic_mean_bias_reduction_pct": 0.0010849064399517988,
213	      "logistic_std_bias_reduction_pct": 0.0020304139113408873,
214	      "logistic_median_bias_reduction_pct": 0.000919133832697594,
215	      "linear_mean_bias_reduction_pct": -1.0602629885170245e-16,
216	      "linear_std_bias_reduction_pct": 8.250307385135087e-16,
217	      "linear_median_bias_reduction_pct": 0.0,
218	      "logistic_n_valid": 200,
219	      "linear_n_valid": 200
220	    },
221	    {
222	      "topology": "confounding",
223	      "N": 10000,
224	      "error_level": "high",
225	      "diag_val": 0.5,
226	      "logistic_mean_bias_reduction_pct": -0.000652411791940275,
227	      "logistic_std_bias_reduction_pct": 0.001976518219280387,
228	      "logistic_median_bias_reduction_pct": -0.0009631852232239169,
229	      "linear_mean_bias_reduction_pct": 1.27675647831893e-17,
230	      "linear_std_bias_reduction_pct": 4.731396838362116e-16,
231	      "linear_median_bias_reduction_pct": 0.0,
232	      "logistic_n_valid": 200,
233	      "linear_n_valid": 200
234	    },
235	    {
236	      "topology": "confounding",
237	      "N": 50000,
238	      "error_level": "low",
239	      "diag_val": 0.9,
240	      "logistic_mean_bias_reduction_pct": -0.003899106202569337,
241	      "logistic_std_bias_reduction_pct": 0.001483441923808299,
242	      "logistic_median_bias_reduction_pct": -0.0038133374649192975,
243	      "linear_mean_bias_reduction_pct": -7.216449660063518e-18,
244	      "linear_std_bias_reduction_pct": 5.433379192438162e-16,
245	      "linear_median_bias_reduction_pct": 0.0,
246	      "logistic_n_valid": 200,
247	      "linear_n_valid": 200
248	    },
249	    {
250	      "topology": "confounding",
251	      "N": 50000,
252	      "error_level": "medium",
253	      "diag_val": 0.7,
254	      "logistic_mean_bias_reduction_pct": 0.0007381832351648993,
255	      "logistic_std_bias_reduction_pct": 0.0010539955971337327,
256	      "logistic_median_bias_reduction_pct": 0.0007356584791260445,
257	      "linear_mean_bias_reduction_pct": -1.6653345369377348e-16,
258	      "linear_std_bias_reduction_pct": 6.404745667978754e-16,
259	      "linear_median_bias_reduction_pct": -2.220446049250313e-16,
260	      "logistic_n_valid": 200,
261	      "linear_n_valid": 200
262	    },
263	    {
264	      "topology": "confounding",
265	      "N": 50000,
266	      "error_level": "high",
267	      "diag_val": 0.5,
268	      "logistic_mean_bias_reduction_pct": -0.000611501681218401,
269	      "logistic_std_bias_reduction_pct": 0.001870546127701101,
270	      "logistic_median_bias_reduction_pct": -0.0010075528796571476,
271	      "linear_mean_bias_reduction_pct": 5.440092820663267e-17,
272	      "linear_std_bias_reduction_pct": 4.4130352749697447e-16,
273	      "linear_median_bias_reduction_pct": 0.0,
274	      "logistic_n_valid": 200,
275	      "linear_n_valid": 200
276	    },
277	    {
278	      "topology": "mediation",
279	      "N": 1000,
280	      "error_level": "low",
281	      "diag_val": 0.9,
282	      "logistic_mean_bias_reduction_pct": -0.013353113873144655,
283	      "logistic_std_bias_reduction_pct": 0.1544260669350131,
284	      "logistic_median_bias_reduction_pct": 0.0005911648469016373,
285	      "linear_mean_bias_reduction_pct": 2.0816681711721685e-16,
286	      "linear_std_bias_reduction_pct": 1.070656713974888e-15,
287	      "linear_median_bias_reduction_pct": 2.220446049250313e-16,
288	      "logistic_n_valid": 200,
289	      "linear_n_valid": 200
290	    },
291	    {
292	      "topology": "mediation",
293	      "N": 1000,
294	      "error_level": "medium",
295	      "diag_val": 0.7,
296	      "logistic_mean_bias_reduction_pct": 0.0018351046485898658,
297	      "logistic_std_bias_reduction_pct": 0.009085635830018843,
298	      "logistic_median_bias_reduction_pct": 0.0010809876949846586,
299	      "linear_mean_bias_reduction_pct": -4.768407890765047e-16,
300	      "linear_std_bias_reduction_pct": 1.4064732558090283e-15,
301	      "linear_median_bias_reduction_pct": -2.220446049250313e-16,
302	      "logistic_n_valid": 200,
303	      "linear_n_valid": 200
304	    },
305	    {
306	      "topology": "mediation",
307	      "N": 1000,
308	      "error_level": "high",
309	      "diag_val": 0.5,
310	      "logistic_mean_bias_reduction_pct": -0.008080191139635047,
311	      "logistic_std_bias_reduction_pct": 0.11999910378768935,
312	      "logistic_median_bias_reduction_pct": 0.00018241378488675908,
313	      "linear_mean_bias_reduction_pct": 9.992007221626409e-17,
314	      "linear_std_bias_reduction_pct": 1.2418627418950446e-15,
315	      "linear_median_bias_reduction_pct": 0.0,
316	      "logistic_n_valid": 200,
317	      "linear_n_valid": 200
318	    },
319	    {
320	      "topology": "mediation",
321	      "N": 5000,
322	      "error_level": "low",
323	      "diag_val": 0.9,
324	      "logistic_mean_bias_reduction_pct": -0.008506826266969992,
325	      "logistic_std_bias_reduction_pct": 0.13372106454837887,
326	      "logistic_median_bias_reduction_pct": 0.0012924098776556092,
327	      "linear_mean_bias_reduction_pct": -1.1102230246251566e-17,
328	      "linear_std_bias_reduction_pct": 1.2318973846952195e-15,
329	      "linear_median_bias_reduction_pct": 0.0,
330	      "logistic_n_valid": 200,
331	      "linear_n_valid": 200
332	    },
333	    {
334	      "topology": "mediation",
335	      "N": 5000,
336	      "error_level": "medium",
337	      "diag_val": 0.7,
338	      "logistic_mean_bias_reduction_pct": 0.0011413597608691528,
339	      "logistic_std_bias_reduction_pct": 0.002100222749793998,
340	      "logistic_median_bias_reduction_pct": 0.000741982662618268,
341	      "linear_mean_bias_reduction_pct": -2.0594637106796654e-16,
342	      "linear_std_bias_reduction_pct": 8.376408318836436e-16,
343	      "linear_median_bias_reduction_pct": 0.0,
344	      "logistic_n_valid": 200,
345	      "linear_n_valid": 200
346	    },
347	    {
348	      "topology": "mediation",
349	      "N": 5000,
350	      "error_level": "high",
351	      "diag_val": 0.5,
352	      "logistic_mean_bias_reduction_pct": 4.8165138278017384e-05,
353	      "logistic_std_bias_reduction_pct": 0.001594929440072224,
354	      "logistic_median_bias_reduction_pct": 6.7472377104915715e-06,
355	      "linear_mean_bias_reduction_pct": 3.7747582837255325e-17,
356	      "linear_std_bias_reduction_pct": 1.1011621576385637e-15,
357	      "linear_median_bias_reduction_pct": 0.0,
358	      "logistic_n_valid": 200,
359	      "linear_n_valid": 200
360	    },
361	    {
362	      "topology": "mediation",
363	      "N": 10000,
364	      "error_level": "low",
365	      "diag_val": 0.9,
366	      "logistic_mean_bias_reduction_pct": 0.00353858321400288,
367	      "logistic_std_bias_reduction_pct": 0.027345675662743613,
368	      "logistic_median_bias_reduction_pct": 0.0014156976916653297,
369	      "linear_mean_bias_reduction_pct": -5.88418203051333e-17,
370	      "linear_std_bias_reduction_pct": 1.272933034285015e-15,
371	      "linear_median_bias_reduction_pct": -2.220446049250313e-16,
372	      "logistic_n_valid": 200,
373	      "linear_n_valid": 200
374	    },
375	    {
376	      "topology": "mediation",
377	      "N": 10000,
378	      "error_level": "medium",
379	      "diag_val": 0.7,
380	      "logistic_mean_bias_reduction_pct": 0.00021624926280033318,
381	      "logistic_std_bias_reduction_pct": 0.0019283386291988024,
382	      "logistic_median_bias_reduction_pct": 9.041586256691714e-05,
383	      "linear_mean_bias_reduction_pct": -1.0824674490095276e-16,
384	      "linear_std_bias_reduction_pct": 8.037767424506553e-16,
385	      "linear_median_bias_reduction_pct": -2.220446049250313e-16,
386	      "logistic_n_valid": 200,
387	      "linear_n_valid": 200
388	    },
389	    {
390	      "topology": "mediation",
391	      "N": 10000,
392	      "error_level": "high",
393	      "diag_val": 0.5,
394	      "logistic_mean_bias_reduction_pct": -0.00014834216891617124,
395	      "logistic_std_bias_reduction_pct": 0.0010626624211218928,
396	      "logistic_median_bias_reduction_pct": 3.713188119280897e-05,
397	      "linear_mean_bias_reduction_pct": 5.2735593669694933e-17,
398	      "linear_std_bias_reduction_pct": 8.930871330214816e-16,
399	      "linear_median_bias_reduction_pct": 0.0,
400	      "logistic_n_valid": 200,
401	      "linear_n_valid": 200
402	    },
403	    {
404	      "topology": "mediation",
405	      "N": 50000,
406	      "error_level": "low",
407	      "diag_val": 0.9,
408	      "logistic_mean_bias_reduction_pct": 0.0014851791924051583,
409	      "logistic_std_bias_reduction_pct": 0.0013283933404068466,
410	      "logistic_median_bias_reduction_pct": 0.001691010524695502,
411	      "linear_mean_bias_reduction_pct": 6.661338147750939e-17,
412	      "linear_std_bias_reduction_pct": 1.0644833181596221e-15,
413	      "linear_median_bias_reduction_pct": 0.0,
414	      "logistic_n_valid": 200,
415	      "linear_n_valid": 200
416	    },
417	    {
418	      "topology": "mediation",
419	      "N": 50000,
420	      "error_level": "medium",
421	      "diag_val": 0.7,
422	      "logistic_mean_bias_reduction_pct": -0.0003659435430137159,
423	      "logistic_std_bias_reduction_pct": 0.001364644518738724,
424	      "logistic_median_bias_reduction_pct": -3.6417051525461375e-06,
425	      "linear_mean_bias_reduction_pct": -1.6209256159527285e-16,
426	      "linear_std_bias_reduction_pct": 7.780944822028338e-16,
427	      "linear_median_bias_reduction_pct": -1.1102230246251565e-16,
428	      "logistic_n_valid": 200,
429	      "linear_n_valid": 200
430	    },
431	    {
432	      "topology": "mediation",
433	      "N": 50000,
434	      "error_level": "high",
435	      "diag_val": 0.5,
436	      "logistic_mean_bias_reduction_pct": -5.652566251234503e-05,
437	      "logistic_std_bias_reduction_pct": 0.0007069206955520261,
438	      "logistic_median_bias_reduction_pct": 8.327471246460938e-05,
439	      "linear_mean_bias_reduction_pct": -1.2212453270876723e-16,
440	      "linear_std_bias_reduction_pct": 7.883365283268487e-16,
441	      "linear_median_bias_reduction_pct": -2.220446049250313e-16,
442	      "logistic_n_valid": 200,
443	      "linear_n_valid": 200
444	    },
445	    {
446	      "topology": "collider",
447	      "N": 1000,
448	      "error_level": "low",
449	      "diag_val": 0.9,
450	      "logistic_mean_bias_reduction_pct": 0.0009103102245364314,
451	      "logistic_std_bias_reduction_pct": 0.022891972409464056,
452	      "logistic_median_bias_reduction_pct": 0.00029958028674714754,
453	      "linear_mean_bias_reduction_pct": -3.2751579226442116e-17,
454	      "linear_std_bias_reduction_pct": 7.066111668021763e-16,
455	      "linear_median_bias_reduction_pct": 0.0,
456	      "logistic_n_valid": 200,
457	      "linear_n_valid": 200
458	    },
459	    {
460	      "topology": "collider",
461	      "N": 1000,
462	      "error_level": "medium",
463	      "diag_val": 0.7,
464	      "logistic_mean_bias_reduction_pct": -0.0011259861257918308,
465	      "logistic_std_bias_reduction_pct": 0.030546527040007605,
466	      "logistic_median_bias_reduction_pct": -0.0004875705225391158,
467	      "linear_mean_bias_reduction_pct": 1.0547118733938987e-17,
468	      "linear_std_bias_reduction_pct": 7.539385106688238e-16,
469	      "linear_median_bias_reduction_pct": 0.0,
470	      "logistic_n_valid": 200,
471	      "linear_n_valid": 200
472	    },
473	    {
474	      "topology": "collider",
475	      "N": 1000,
476	      "error_level": "high",
477	      "diag_val": 0.5,
478	      "logistic_mean_bias_reduction_pct": 0.0007508794540829011,
479	      "logistic_std_bias_reduction_pct": 0.013914037338760761,
480	      "logistic_median_bias_reduction_pct": 1.619229831784086e-05,
481	      "linear_mean_bias_reduction_pct": -2.0539125955565396e-17,
482	      "linear_std_bias_reduction_pct": 1.7891159646773095e-15,
483	      "linear_median_bias_reduction_pct": 0.0,
484	      "logistic_n_valid": 200,
485	      "linear_n_valid": 200
486	    },
487	    {
488	      "topology": "collider",
489	      "N": 5000,
490	      "error_level": "low",
491	      "diag_val": 0.9,
492	      "logistic_mean_bias_reduction_pct": 0.006650610698786848,
493	      "logistic_std_bias_reduction_pct": 0.07828022543784671,
494	      "logistic_median_bias_reduction_pct": 0.0008775677692690609,
495	      "linear_mean_bias_reduction_pct": -1.3433698597964394e-16,
496	      "linear_std_bias_reduction_pct": 4.3007208439501707e-16,
497	      "linear_median_bias_reduction_pct": 0.0,
498	      "logistic_n_valid": 200,
499	      "linear_n_valid": 200
500	    },
501	    {
502	      "topology": "collider",
503	      "N": 5000,
504	      "error_level": "medium",
505	      "diag_val": 0.7,
506	      "logistic_mean_bias_reduction_pct": 0.0016953703352169808,
507	      "logistic_std_bias_reduction_pct": 0.045361200520015355,
508	      "logistic_median_bias_reduction_pct": -0.0007036782607557912,
509	      "linear_mean_bias_reduction_pct": -9.880984919163893e-17,
510	      "linear_std_bias_reduction_pct": 6.973040282835291e-16,
511	      "linear_median_bias_reduction_pct": 0.0,
512	      "logistic_n_valid": 200,
513	      "linear_n_valid": 200
514	    },
515	    {
516	      "topology": "collider",
517	      "N": 5000,
518	      "error_level": "high",
519	      "diag_val": 0.5,
520	      "logistic_mean_bias_reduction_pct": -0.008929121027909832,
521	      "logistic_std_bias_reduction_pct": 0.12265948631436661,
522	      "logistic_median_bias_reduction_pct": 0.000175265613322928,
523	      "linear_mean_bias_reduction_pct": -1.4988010832439614e-16,
524	      "linear_std_bias_reduction_pct": 2.165810089271756e-15,
525	      "linear_median_bias_reduction_pct": 0.0,
526	      "logistic_n_valid": 200,
527	      "linear_n_valid": 200
528	    },
529	    {
530	      "topology": "collider",
531	      "N": 10000,
532	      "error_level": "low",
533	      "diag_val": 0.9,
534	      "logistic_mean_bias_reduction_pct": -0.12608673964976239,
535	      "logistic_std_bias_reduction_pct": 1.9102324430015762,
536	      "logistic_median_bias_reduction_pct": 0.0005764382716746397,
537	      "linear_mean_bias_reduction_pct": -1.149080830487037e-16,
538	      "linear_std_bias_reduction_pct": 3.5861707448920106e-16,
539	      "linear_median_bias_reduction_pct": 0.0,
540	      "logistic_n_valid": 200,
541	      "linear_n_valid": 200
542	    },
543	    {
544	      "topology": "collider",
545	      "N": 10000,
546	      "error_level": "medium",
547	      "diag_val": 0.7,
548	      "logistic_mean_bias_reduction_pct": -0.09207655030216363,
549	      "logistic_std_bias_reduction_pct": 1.2789211683867339,
550	      "logistic_median_bias_reduction_pct": -0.00030575170230917603,
551	      "linear_mean_bias_reduction_pct": -1.5543122344752193e-17,
552	      "linear_std_bias_reduction_pct": 5.899913599447276e-16,
553	      "linear_median_bias_reduction_pct": 0.0,
554	      "logistic_n_valid": 200,
555	      "linear_n_valid": 200
556	    },
557	    {
558	      "topology": "collider",
559	      "N": 10000,
560	      "error_level": "high",
561	      "diag_val": 0.5,
562	      "logistic_mean_bias_reduction_pct": 0.007573649038141327,
563	      "logistic_std_bias_reduction_pct": 0.07128671834989593,
564	      "logistic_median_bias_reduction_pct": 0.00029933169245810465,
565	      "linear_mean_bias_reduction_pct": -2.4813484600372247e-16,
566	      "linear_std_bias_reduction_pct": 1.3684586438565463e-15,
567	      "linear_median_bias_reduction_pct": 0.0,
568	      "logistic_n_valid": 200,
569	      "linear_n_valid": 200
570	    },
571	    {
572	      "topology": "collider",
573	      "N": 50000,
574	      "error_level": "low",
575	      "diag_val": 0.9,
576	      "logistic_mean_bias_reduction_pct": -0.01440216240328038,
577	      "logistic_std_bias_reduction_pct": 0.2608593541990993,
578	      "logistic_median_bias_reduction_pct": -0.00015404492517934187,
579	      "linear_mean_bias_reduction_pct": -1.27675647831893e-16,
580	      "linear_std_bias_reduction_pct": 2.964004391750595e-16,
581	      "linear_median_bias_reduction_pct": 0.0,
582	      "logistic_n_valid": 200,
583	      "linear_n_valid": 200
584	    },
585	    {
586	      "topology": "collider",
587	      "N": 50000,
588	      "error_level": "medium",
589	      "diag_val": 0.7,
590	      "logistic_mean_bias_reduction_pct": 0.0029840853479878846,
591	      "logistic_std_bias_reduction_pct": 0.04252180203847579,
592	      "logistic_median_bias_reduction_pct": -0.0002817086396476043,
593	      "linear_mean_bias_reduction_pct": 7.105427357601002e-17,
594	      "linear_std_bias_reduction_pct": 3.881083089439011e-16,
595	      "linear_median_bias_reduction_pct": 0.0,
596	      "logistic_n_valid": 200,
597	      "linear_n_valid": 200
598	    },
599	    {
600	      "topology": "collider",
601	      "N": 50000,
602	      "error_level": "high",
603	      "diag_val": 0.5,
604	      "logistic_mean_bias_reduction_pct": 0.0019976287635311866,
605	      "logistic_std_bias_reduction_pct": 0.004054431526786614,
606	      "logistic_median_bias_reduction_pct": 0.0011603975130490274,
607	      "linear_mean_bias_reduction_pct": -3.652633751016765e-16,
608	      "linear_std_bias_reduction_pct": 1.1103112838474496e-15,
609	      "linear_median_bias_reduction_pct": 0.0,
610	      "logistic_n_valid": 200,
611	      "linear_n_valid": 200
612	    },
613	    {
614	      "topology": "exposure",
615	      "N": 1000,
616	      "error_level": "low",
617	      "diag_val": 0.9,
618	      "logistic_mean_bias_reduction_pct": -0.4369119510134019,
619	      "logistic_std_bias_reduction_pct": 0.6992035628151184,
620	      "logistic_median_bias_reduction_pct": -0.3002073393949889,
621	      "linear_mean_bias_reduction_pct": -0.03840946411670899,
622	      "linear_std_bias_reduction_pct": 0.0078038124462802465,
623	      "linear_median_bias_reduction_pct": -0.03798554273777399,
624	      "logistic_n_valid": 200,
625	      "linear_n_valid": 200
626	    },
627	    {
628	      "topology": "exposure",
629	      "N": 1000,
630	      "error_level": "medium",
631	      "diag_val": 0.7,
632	      "logistic_mean_bias_reduction_pct": -0.5144153875176722,
633	      "logistic_std_bias_reduction_pct": 0.34107929917955543,
634	      "logistic_median_bias_reduction_pct": -0.43705972899923873,
635	      "linear_mean_bias_reduction_pct": -0.06364832676197657,
636	      "linear_std_bias_reduction_pct": 0.018132079120551578,
637	      "linear_median_bias_reduction_pct": -0.062470473262318804,
638	      "logistic_n_valid": 200,
639	      "linear_n_valid": 200
640	    },
641	    {
642	      "topology": "exposure",
643	      "N": 1000,
644	      "error_level": "high",
645	      "diag_val": 0.5,
646	      "logistic_mean_bias_reduction_pct": -0.2347645282637987,
647	      "logistic_std_bias_reduction_pct": 0.17061850183975844,
648	      "logistic_median_bias_reduction_pct": -0.20489657472464318,
649	      "linear_mean_bias_reduction_pct": -0.04413459804379915,
650	      "linear_std_bias_reduction_pct": 0.026772909191679396,
651	      "linear_median_bias_reduction_pct": -0.04277916752753275,
652	      "logistic_n_valid": 200,
653	      "linear_n_valid": 200
654	    },
655	    {
656	      "topology": "exposure",
657	      "N": 5000,
658	      "error_level": "low",
659	      "diag_val": 0.9,
660	      "logistic_mean_bias_reduction_pct": -0.7831107268311296,
661	      "logistic_std_bias_reduction_pct": 0.41607986764579546,
662	      "logistic_median_bias_reduction_pct": -0.6753560355314904,
663	      "linear_mean_bias_reduction_pct": -0.03778626407699957,
664	      "linear_std_bias_reduction_pct": 0.003279946005747772,
665	      "linear_median_bias_reduction_pct": -0.03763864840801878,
666	      "logistic_n_valid": 200,
667	      "linear_n_valid": 200
668	    },
669	    {
670	      "topology": "exposure",
671	      "N": 5000,
672	      "error_level": "medium",
673	      "diag_val": 0.7,
674	      "logistic_mean_bias_reduction_pct": -0.4800496432760565,
675	      "logistic_std_bias_reduction_pct": 0.10301352301978538,
676	      "logistic_median_bias_reduction_pct": -0.4735761122157215,
677	      "linear_mean_bias_reduction_pct": -0.06440771831410162,
678	      "linear_std_bias_reduction_pct": 0.007606146846358069,
679	      "linear_median_bias_reduction_pct": -0.06472012431294549,
680	      "logistic_n_valid": 200,
681	      "linear_n_valid": 200
682	    },
683	    {
684	      "topology": "exposure",
685	      "N": 5000,
686	      "error_level": "high",
687	      "diag_val": 0.5,
688	      "logistic_mean_bias_reduction_pct": -0.22536098534016072,
689	      "logistic_std_bias_reduction_pct": 0.0729833811477896,
690	      "logistic_median_bias_reduction_pct": -0.22146703624113262,
691	      "linear_mean_bias_reduction_pct": -0.04471829810935599,
692	      "linear_std_bias_reduction_pct": 0.011622524651939027,
693	      "linear_median_bias_reduction_pct": -0.04491932426370138,
694	      "logistic_n_valid": 200,
695	      "linear_n_valid": 200
696	    },
697	    {
698	      "topology": "exposure",
699	      "N": 10000,
700	      "error_level": "low",
701	      "diag_val": 0.9,
702	      "logistic_mean_bias_reduction_pct": -0.7666369158827613,
703	      "logistic_std_bias_reduction_pct": 0.2904911256360045,
704	      "logistic_median_bias_reduction_pct": -0.6922586326932803,
705	      "linear_mean_bias_reduction_pct": -0.03742571696750324,
706	      "linear_std_bias_reduction_pct": 0.0025498822835161557,
707	      "linear_median_bias_reduction_pct": -0.037294960630326446,
708	      "logistic_n_valid": 200,
709	      "linear_n_valid": 200
710	    },
711	    {
712	      "topology": "exposure",
713	      "N": 10000,
714	      "error_level": "medium",
715	      "diag_val": 0.7,
716	      "logistic_mean_bias_reduction_pct": -0.4825651792109044,
717	      "logistic_std_bias_reduction_pct": 0.08017364344273191,
718	      "logistic_median_bias_reduction_pct": -0.4790633738564586,
719	      "linear_mean_bias_reduction_pct": -0.06489496046330488,
720	      "linear_std_bias_reduction_pct": 0.005907644532264317,
721	      "linear_median_bias_reduction_pct": -0.06513780804487668,
722	      "logistic_n_valid": 200,
723	      "linear_n_valid": 200
724	    },
725	    {
726	      "topology": "exposure",
727	      "N": 10000,
728	      "error_level": "high",
729	      "diag_val": 0.5,
730	      "logistic_mean_bias_reduction_pct": -0.22038802936143698,
731	      "logistic_std_bias_reduction_pct": 0.05322855662218981,
732	      "logistic_median_bias_reduction_pct": -0.21395898813920788,
733	      "linear_mean_bias_reduction_pct": -0.0442131749797555,
734	      "linear_std_bias_reduction_pct": 0.008778807095420107,
735	      "linear_median_bias_reduction_pct": -0.04346443782352705,
736	      "logistic_n_valid": 200,
737	      "linear_n_valid": 200
738	    },
739	    {
740	      "topology": "exposure",
741	      "N": 50000,
742	      "error_level": "low",
743	      "diag_val": 0.9,
744	      "logistic_mean_bias_reduction_pct": -0.7550316480611715,
745	      "logistic_std_bias_reduction_pct": 0.12065666012697929,
746	      "logistic_median_bias_reduction_pct": -0.7397125780346917,
747	      "linear_mean_bias_reduction_pct": -0.037698721480995394,
748	      "linear_std_bias_reduction_pct": 0.0011352494429960384,
749	      "linear_median_bias_reduction_pct": -0.037677984554001065,
750	      "logistic_n_valid": 200,
751	      "linear_n_valid": 200
752	    },
753	    {
754	      "topology": "exposure",
755	      "N": 50000,
756	      "error_level": "medium",
757	      "diag_val": 0.7,
758	      "logistic_mean_bias_reduction_pct": -0.4746793400017082,
759	      "logistic_std_bias_reduction_pct": 0.031875054187836975,
760	      "logistic_median_bias_reduction_pct": -0.47091123363280796,
761	      "linear_mean_bias_reduction_pct": -0.06468281404467784,
762	      "linear_std_bias_reduction_pct": 0.00236103520633415,
763	      "linear_median_bias_reduction_pct": -0.06451440286426746,
764	      "logistic_n_valid": 200,
765	      "linear_n_valid": 200
766	    },
767	    {
768	      "topology": "exposure",
769	      "N": 50000,
770	      "error_level": "high",
771	      "diag_val": 0.5,
772	      "logistic_mean_bias_reduction_pct": -0.21987786513970112,
773	      "logistic_std_bias_reduction_pct": 0.023377597377243396,
774	      "logistic_median_bias_reduction_pct": -0.2186125858320923,
775	      "linear_mean_bias_reduction_pct": -0.04445262704016246,
776	      "linear_std_bias_reduction_pct": 0.0038407094257366537,
777	      "linear_median_bias_reduction_pct": -0.044317387333169145,
778	      "logistic_n_valid": 200,
779	      "linear_n_valid": 200
780	    },
781	    {
782	      "topology": "mbias",
783	      "N": 1000,
784	      "error_level": "low",
785	      "diag_val": 0.9,
786	      "logistic_mean_bias_reduction_pct": 0.0032462159625632923,
787	      "logistic_std_bias_reduction_pct": 0.057203322099178,
788	      "logistic_median_bias_reduction_pct": -0.0001336896443819846,
789	      "linear_mean_bias_reduction_pct": 1.5543122344752193e-17,
790	      "linear_std_bias_reduction_pct": 5.914519744151675e-16,
791	      "linear_median_bias_reduction_pct": 0.0,
792	      "logistic_n_valid": 200,
793	      "linear_n_valid": 200
794	    },
795	    {
796	      "topology": "mbias",
797	      "N": 1000,
798	      "error_level": "medium",
799	      "diag_val": 0.7,
800	      "logistic_mean_bias_reduction_pct": -0.0022813915056582174,
801	      "logistic_std_bias_reduction_pct": 0.03215870014089292,
802	      "logistic_median_bias_reduction_pct": 7.455819743318326e-05,
803	      "linear_mean_bias_reduction_pct": -5.551115123125783e-17,
804	      "linear_std_bias_reduction_pct": 6.674278181324105e-16,
805	      "linear_median_bias_reduction_pct": 0.0,
806	      "logistic_n_valid": 200,
807	      "linear_n_valid": 200
808	    },
809	    {
810	      "topology": "mbias",
811	      "N": 1000,
812	      "error_level": "high",
813	      "diag_val": 0.5,
814	      "logistic_mean_bias_reduction_pct": 0.0033696136504251122,
815	      "logistic_std_bias_reduction_pct": 0.05513762218655773,
816	      "logistic_median_bias_reduction_pct": 0.00022968646953241967,
817	      "linear_mean_bias_reduction_pct": -6.661338147750939e-18,
818	      "linear_std_bias_reduction_pct": 8.938943291349813e-16,
819	      "linear_median_bias_reduction_pct": 0.0,
820	      "logistic_n_valid": 200,
821	      "linear_n_valid": 200
822	    },
823	    {
824	      "topology": "mbias",
825	      "N": 5000,
826	      "error_level": "low",
827	      "diag_val": 0.9,
828	      "logistic_mean_bias_reduction_pct": 0.0022601214202603013,
829	      "logistic_std_bias_reduction_pct": 0.1269092148513164,
830	      "logistic_median_bias_reduction_pct": 0.0009587925780700224,
831	      "linear_mean_bias_reduction_pct": -1.0047518372857667e-16,
832	      "linear_std_bias_reduction_pct": 4.975728655927349e-16,
833	      "linear_median_bias_reduction_pct": 0.0,
834	      "logistic_n_valid": 200,
835	      "linear_n_valid": 200
836	    },
837	    {
838	      "topology": "mbias",
839	      "N": 5000,
840	      "error_level": "medium",
841	      "diag_val": 0.7,
842	      "logistic_mean_bias_reduction_pct": 0.0019944840253893026,
843	      "logistic_std_bias_reduction_pct": 0.029223028637165364,
844	      "logistic_median_bias_reduction_pct": 0.00010775139248603294,
845	      "linear_mean_bias_reduction_pct": -4.6074255521943994e-17,
846	      "linear_std_bias_reduction_pct": 5.571370270532235e-16,
847	      "linear_median_bias_reduction_pct": 0.0,
848	      "logistic_n_valid": 200,
849	      "linear_n_valid": 200
850	    },
851	    {
852	      "topology": "mbias",
853	      "N": 5000,
854	      "error_level": "high",
855	      "diag_val": 0.5,
856	      "logistic_mean_bias_reduction_pct": -0.0648823122935752,
857	      "logistic_std_bias_reduction_pct": 0.8343969236507205,
858	      "logistic_median_bias_reduction_pct": -0.00019794748411383623,
859	      "linear_mean_bias_reduction_pct": 5.2180482157382354e-17,
860	      "linear_std_bias_reduction_pct": 6.290087077445225e-16,
861	      "linear_median_bias_reduction_pct": 0.0,
862	      "logistic_n_valid": 200,
863	      "linear_n_valid": 200
864	    },
865	    {
866	      "topology": "mbias",
867	      "N": 10000,
868	      "error_level": "low",
869	      "diag_val": 0.9,
870	      "logistic_mean_bias_reduction_pct": -0.19005501385031084,
871	      "logistic_std_bias_reduction_pct": 2.6467210741848195,
872	      "logistic_median_bias_reduction_pct": 0.0007982955281162218,
873	      "linear_mean_bias_reduction_pct": -4.3853809472693685e-17,
874	      "linear_std_bias_reduction_pct": 4.4559897540913e-16,
875	      "linear_median_bias_reduction_pct": 0.0,
876	      "logistic_n_valid": 200,
877	      "linear_n_valid": 200
878	    },
879	    {
880	      "topology": "mbias",
881	      "N": 10000,
882	      "error_level": "medium",
883	      "diag_val": 0.7,
884	      "logistic_mean_bias_reduction_pct": -0.005418788438181078,
885	      "logistic_std_bias_reduction_pct": 0.18446579130125645,
886	      "logistic_median_bias_reduction_pct": -0.00031325808003090927,
887	      "linear_mean_bias_reduction_pct": 8.881784197001253e-18,
888	      "linear_std_bias_reduction_pct": 6.576944705686879e-16,
889	      "linear_median_bias_reduction_pct": 0.0,
890	      "logistic_n_valid": 200,
891	      "linear_n_valid": 200
892	    },
893	    {
894	      "topology": "mbias",
895	      "N": 10000,
896	      "error_level": "high",
897	      "diag_val": 0.5,
898	      "logistic_mean_bias_reduction_pct": -0.00015714131119887563,
899	      "logistic_std_bias_reduction_pct": 0.03648444357385395,
900	      "logistic_median_bias_reduction_pct": 0.0006226314975399938,
901	      "linear_mean_bias_reduction_pct": -2.942091015256665e-17,
902	      "linear_std_bias_reduction_pct": 5.898281205698744e-16,
903	      "linear_median_bias_reduction_pct": 0.0,
904	      "logistic_n_valid": 200,
905	      "linear_n_valid": 200
906	    },
907	    {
908	      "topology": "mbias",
909	      "N": 50000,
910	      "error_level": "low",
911	      "diag_val": 0.9,
912	      "logistic_mean_bias_reduction_pct": -0.010195990729227215,
913	      "logistic_std_bias_reduction_pct": 0.16399786488710452,
914	      "logistic_median_bias_reduction_pct": 0.006270379368089107,
915	      "linear_mean_bias_reduction_pct": -4.440892098500626e-18,
916	      "linear_std_bias_reduction_pct": 2.9307364507337618e-16,
917	      "linear_median_bias_reduction_pct": 0.0,
918	      "logistic_n_valid": 200,
919	      "linear_n_valid": 200
920	    },
921	    {
922	      "topology": "mbias",
923	      "N": 50000,
924	      "error_level": "medium",
925	      "diag_val": 0.7,
926	      "logistic_mean_bias_reduction_pct": -0.03485194760022364,
927	      "logistic_std_bias_reduction_pct": 0.4290206893249396,
928	      "logistic_median_bias_reduction_pct": -0.0021879046445376638,
929	      "linear_mean_bias_reduction_pct": 6.827871601444713e-17,
930	      "linear_std_bias_reduction_pct": 5.171396324808679e-16,
931	      "linear_median_bias_reduction_pct": 0.0,
932	      "logistic_n_valid": 200,
933	      "linear_n_valid": 200
934	    },
935	    {
936	      "topology": "mbias",
937	      "N": 50000,
938	      "error_level": "high",
939	      "diag_val": 0.5,
940	      "logistic_mean_bias_reduction_pct": -0.002848585051556322,
941	      "logistic_std_bias_reduction_pct": 0.018987587548860523,
942	      "logistic_median_bias_reduction_pct": -0.002629538327355352,
943	      "linear_mean_bias_reduction_pct": 1.1879386363489176e-16,
944	      "linear_std_bias_reduction_pct": 1.0266718012288645e-15,
945	      "linear_median_bias_reduction_pct": 0.0,
946	      "logistic_n_valid": 200,
947	      "linear_n_valid": 200
948	    },
949	    {
950	      "topology": "frontdoor",
951	      "N": 1000,
952	      "error_level": "low",
953	      "diag_val": 0.9,
954	      "logistic_mean_bias_reduction_pct": 0.0002545003735146084,
955	      "logistic_std_bias_reduction_pct": 0.004607740370210718,
956	      "logistic_median_bias_reduction_pct": -7.83126589765093e-05,
957	      "linear_mean_bias_reduction_pct": -2.1094237467877975e-17,
958	      "linear_std_bias_reduction_pct": 7.036037871114657e-16,
959	      "linear_median_bias_reduction_pct": 0.0,
960	      "logistic_n_valid": 200,
961	      "linear_n_valid": 200
962	    },
963	    {
964	      "topology": "frontdoor",
965	      "N": 1000,
966	      "error_level": "medium",
967	      "diag_val": 0.7,
968	      "logistic_mean_bias_reduction_pct": -0.0013357539513295753,
969	      "logistic_std_bias_reduction_pct": 0.007043313368568651,
970	      "logistic_median_bias_reduction_pct": -0.0006004102629336705,
971	      "linear_mean_bias_reduction_pct": 2.220446049250313e-18,
972	      "linear_std_bias_reduction_pct": 8.120550982399728e-16,
973	      "linear_median_bias_reduction_pct": 0.0,
974	      "logistic_n_valid": 200,
975	      "linear_n_valid": 200
976	    },
977	    {
978	      "topology": "frontdoor",
979	      "N": 1000,
980	      "error_level": "high",
981	      "diag_val": 0.5,
982	      "logistic_mean_bias_reduction_pct": -0.00030583621352540057,
983	      "logistic_std_bias_reduction_pct": 0.0008375939066679953,
984	      "logistic_median_bias_reduction_pct": -0.00017568066023332385,
985	      "linear_mean_bias_reduction_pct": 1.249000902703301e-16,
986	      "linear_std_bias_reduction_pct": 9.874082597015364e-16,
987	      "linear_median_bias_reduction_pct": 0.0,
988	      "logistic_n_valid": 200,
989	      "linear_n_valid": 200
990	    },
991	    {
992	      "topology": "frontdoor",
993	      "N": 5000,
994	      "error_level": "low",
995	      "diag_val": 0.9,
996	      "logistic_mean_bias_reduction_pct": 0.0012545206907651552,
997	      "logistic_std_bias_reduction_pct": 0.004815364672235464,
998	      "logistic_median_bias_reduction_pct": 0.0009088913108011298,
999	      "linear_mean_bias_reduction_pct": -1.1823875212257917e-16,
1000	      "linear_std_bias_reduction_pct": 6.350706184407892e-16,
1001	      "linear_median_bias_reduction_pct": -2.220446049250313e-16,
1002	      "logistic_n_valid": 200,
1003	      "linear_n_valid": 200
1004	    },
1005	    {
1006	      "topology": "frontdoor",
1007	      "N": 5000,
1008	      "error_level": "medium",
1009	      "diag_val": 0.7,
1010	      "logistic_mean_bias_reduction_pct": -0.0009094752019033947,
1011	      "logistic_std_bias_reduction_pct": 0.0011877895368919344,
1012	      "logistic_median_bias_reduction_pct": -0.0007420725739377687,
1013	      "linear_mean_bias_reduction_pct": -1.2212453270876722e-17,
1014	      "linear_std_bias_reduction_pct": 6.076673652238809e-16,
1015	      "linear_median_bias_reduction_pct": 0.0,
1016	      "logistic_n_valid": 200,
1017	      "linear_n_valid": 200
1018	    },
1019	    {
1020	      "topology": "frontdoor",
1021	      "N": 5000,
1022	      "error_level": "high",
1023	      "diag_val": 0.5,
1024	      "logistic_mean_bias_reduction_pct": -0.0004294652835207841,
1025	      "logistic_std_bias_reduction_pct": 0.0006762039555566602,
1026	      "logistic_median_bias_reduction_pct": -0.00032863270106009423,
1027	      "linear_mean_bias_reduction_pct": 7.66053886991358e-17,
1028	      "linear_std_bias_reduction_pct": 8.615781329733292e-16,
1029	      "linear_median_bias_reduction_pct": 0.0,
1030	      "logistic_n_valid": 200,
1031	      "linear_n_valid": 200
1032	    },
1033	    {
1034	      "topology": "frontdoor",
1035	      "N": 10000,
1036	      "error_level": "low",
1037	      "diag_val": 0.9,
1038	      "logistic_mean_bias_reduction_pct": 0.001523965496299589,
1039	      "logistic_std_bias_reduction_pct": 0.0027043243595773997,
1040	      "logistic_median_bias_reduction_pct": 0.0012123755113495616,
1041	      "linear_mean_bias_reduction_pct": 2.0539125955565396e-17,
1042	      "linear_std_bias_reduction_pct": 5.88426320191988e-16,
1043	      "linear_median_bias_reduction_pct": 0.0,
1044	      "logistic_n_valid": 200,
1045	      "linear_n_valid": 200
1046	    },
1047	    {
1048	      "topology": "frontdoor",
1049	      "N": 10000,
1050	      "error_level": "medium",
1051	      "diag_val": 0.7,
1052	      "logistic_mean_bias_reduction_pct": -0.0008042647190860363,
1053	      "logistic_std_bias_reduction_pct": 0.0009304107867278689,
1054	      "logistic_median_bias_reduction_pct": -0.0007837725061767831,
1055	      "linear_mean_bias_reduction_pct": 4.274358644806853e-17,
1056	      "linear_std_bias_reduction_pct": 6.10388210081449e-16,
1057	      "linear_median_bias_reduction_pct": 0.0,
1058	      "logistic_n_valid": 200,
1059	      "linear_n_valid": 200
1060	    },
1061	    {
1062	      "topology": "frontdoor",
1063	      "N": 10000,
1064	      "error_level": "high",
1065	      "diag_val": 0.5,
1066	      "logistic_mean_bias_reduction_pct": -0.0005275453234150085,
1067	      "logistic_std_bias_reduction_pct": 0.0006424310683537114,
1068	      "logistic_median_bias_reduction_pct": -0.00038746899225861053,
1069	      "linear_mean_bias_reduction_pct": 1.8318679906315084e-17,
1070	      "linear_std_bias_reduction_pct": 6.520873457431094e-16,
1071	      "linear_median_bias_reduction_pct": 0.0,
1072	      "logistic_n_valid": 200,
1073	      "linear_n_valid": 200
1074	    },
1075	    {
1076	      "topology": "frontdoor",
1077	      "N": 50000,
1078	      "error_level": "low",
1079	      "diag_val": 0.9,
1080	      "logistic_mean_bias_reduction_pct": 0.0022504069430908007,
1081	      "logistic_std_bias_reduction_pct": 0.0027392847407352854,
1082	      "logistic_median_bias_reduction_pct": 0.0018050865040449837,
1083	      "linear_mean_bias_reduction_pct": 1.2212453270876722e-17,
1084	      "linear_std_bias_reduction_pct": 5.1584049036228065e-16,
1085	      "linear_median_bias_reduction_pct": 0.0,
1086	      "logistic_n_valid": 200,
1087	      "linear_n_valid": 200
1088	    },
1089	    {
1090	      "topology": "frontdoor",
1091	      "N": 50000,
1092	      "error_level": "medium",
1093	      "diag_val": 0.7,
1094	      "logistic_mean_bias_reduction_pct": -0.0006556921561021489,
1095	      "logistic_std_bias_reduction_pct": 0.0009485204064226889,
1096	      "logistic_median_bias_reduction_pct": -0.0006444986446492162,
1097	      "linear_mean_bias_reduction_pct": 7.494005416219807e-17,
1098	      "linear_std_bias_reduction_pct": 6.556839860982377e-16,
1099	      "linear_median_bias_reduction_pct": 0.0,
1100	      "logistic_n_valid": 200,
1101	      "linear_n_valid": 200
1102	    },
1103	    {
1104	      "topology": "frontdoor",
1105	      "N": 50000,
1106	      "error_level": "high",
1107	      "diag_val": 0.5,
1108	      "logistic_mean_bias_reduction_pct": -0.0007546906555223714,
1109	      "logistic_std_bias_reduction_pct": 0.0007209399487036038,
1110	      "logistic_median_bias_reduction_pct": -0.0008992133094358756,
1111	      "linear_mean_bias_reduction_pct": -6.661338147750939e-17,
1112	      "linear_std_bias_reduction_pct": 8.090928820704079e-16,
1113	      "linear_median_bias_reduction_pct": 0.0,
1114	      "logistic_n_valid": 200,
1115	      "linear_n_valid": 200
1116	    }
1117	  ]
1118	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc3259e8-d73a-4d14-9b84-67c5aaa49c50",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "869c45a5-200d-414b-a1d8-01ce2dfc1020",
  "sourceToolAssistantUUID": "bc3259e8-d73a-4d14-9b84-67c5aaa49c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T20:19:54.785Z_

<details><summary>↩ Tool result · `toolu_01PEbsySa9cZ4fWzVREFnRpq`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_results_v2.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/__pycache__/exp_d_conjecture_verify_v2.cpython-314.pyc
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture_dgp_sensitivity.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture_dgp_sensitivity_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture_dgp_sensitivity_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_formula_verify.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_extended_analysis.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_extended_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_alpha_half_test.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_alpha_half_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_diagonal_dominant_proof.aux
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_diagonal_dominant_proof.pdf
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_diagonal_dominant_proof.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_formula_verify_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_diagonal_dominant_proof.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eecf1863-c6bc-475d-b2e1-36ce2969fde7",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "253330ea-8d3f-405d-88af-ce17becdde1d",
  "sourceToolAssistantUUID": "eecf1863-c6bc-475d-b2e1-36ce2969fde7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T20:19:55.404Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SbsBNaZM2rrtHeNhDkBZUe`</summary>

```json
{
  "pattern": "82.*gold|gold.*82|stability.*82|82.*stability",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "253330ea-8d3f-405d-88af-ce17becdde1d",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZDysdHEq6GSpiTXhs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4927082b-61a0-4b5d-b846-6fbfafcf6eec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cp4iMsNEMRH6PtDfCPtx1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 35175,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 899,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 16 · 2026-05-25T20:19:55.461Z_

<details><summary>↩ Tool result · `toolu_01SbsBNaZM2rrtHeNhDkBZUe`</summary>

```text
Found 18 files
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ppi_gold_ratio_sensitivity.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_annotations/data/vast/test.jsonl
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T054528/logs/phase2_best_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T054528/logs/phase1_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_worst.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_median.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_best.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_worst.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_median.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_best.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_worst_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_median_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_best_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T072911/logs/phase2_worst_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T072911/logs/phase2_median_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T072911/logs/phase2_best_attempt0.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4927082b-61a0-4b5d-b846-6fbfafcf6eec",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "96e25023-ec41-4a45-a598-553fb3dd9bab",
  "sourceToolAssistantUUID": "4927082b-61a0-4b5d-b846-6fbfafcf6eec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T20:19:55.869Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01QnDkT8isBH85eQ7C5Z5XYQ`</summary>

```json
{
  "pattern": "sign_reversal|14.*23|23.*14",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96e25023-ec41-4a45-a598-553fb3dd9bab",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZDysdHEq6GSpiTXhs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a29d324f-2564-49ac-b00e-8c582c70cc72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cp4iMsNEMRH6PtDfCPtx1S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 899,
      "cache_read_input_tokens": 35175,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 899
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 722,
          "cache_read_input_tokens": 35175,
          "cache_creation_input_tokens": 899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 899,
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

_source line 18 · 2026-05-25T20:19:55.935Z_

<details><summary>↩ Tool result · `toolu_01QnDkT8isBH85eQ7C5Z5XYQ`</summary>

```text
Found 99 files
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/empirical_section_draft.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_issues.yaml
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_alpha_half_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_real_cm_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_21.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/manifest.yaml
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/symmetry_deviation_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/symmetry_deviation_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/adversarial_monotonicity_results_b60bb1.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/adversarial_monotonicity_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/nondiff_y_stratified_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/nondiff_y_stratified_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/e2e_demo_results_c9b14d.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/sign_reversal_determinants_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/sign_reversal_determinants.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/structured_nondiff_violation_table.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/structured_nondiff_violation_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture_dgp_sensitivity_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_17.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ppi_gold_ratio_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/bootstrap_ci_convergence_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/bootstrap_ci_convergence_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/nondiff_structured_stress_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/nondiff_structured_stress_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_proportional_real_matrices_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_realistic_epsilon_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_realistic_epsilon.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_fwl_nonlinear_scaling_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_proportional_effects_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_primary_coeff_breakdown_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/theory_empirical_mape.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/exp_d_epsilon_tau_sensitivity.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_epsilon_tau_sensitivity.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_epsilon_tau_sensitivity.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_b_logistic_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_results_v2.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_c_bootstrap_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/rebuttal_draft.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_cms.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_new_cms_round2.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/updated_empirical_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/plan011_frontier_cms.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan007/correction_guidance_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan007_fast/correction_guidance_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ppi_empirical_validation.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/case_study_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan012_case_study/case_study_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_annotations/data/civil_comments/test.jsonl
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/ppi_empirical_validation.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T054528/best/paper_framing.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T054528/best/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T054528/logs/phase2_best_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T054528/logs/phase1_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T052547/logs/phase1_attempt1.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T052211/logs/phase1_attempt1.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/iv_dirichlet_subspace_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_iv_dirichlet_subspace_output.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_asv_empirical/data/plan006_full_filtered_stats.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_full_filtered_stats.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_exact_values.txt
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/plan006_empirical_data_505323.txt
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_empirical_data.txt
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_mock/asv_empirical_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006/asv_empirical_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan007/plan007_analysis.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan007/report/plan007_analysis.md
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/meta.yaml
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_worst.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_median.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/review_context.yaml
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_best.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/review_context.yaml
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_worst.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_median.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_best.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_worst_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_median_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_best_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase1_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T072911/logs/phase2_worst_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T072911/logs/phase2_median_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T072911/logs/phase2_best_attempt0.log
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/mvp_exposure_dag.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dag.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T072911/logs/phase1_attempt0.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a29d324f-2564-49ac-b00e-8c582c70cc72",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "bfbdac3c-88bc-454e-ae06-d5a608fbd732",
  "sourceToolAssistantUUID": "a29d324f-2564-49ac-b00e-8c582c70cc72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-25T20:19:58.460Z_

Now let me read the conjecture file and search for the sign_reversal information more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfbdac3c-88bc-454e-ae06-d5a608fbd732",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZbgbENMP9vWXMJhFe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "228b5ffc-8aeb-45dc-ba16-fc0f2b05745a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PSCu5yauaaZ3m9SNbv62xQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 37608,
      "cache_read_input_tokens": 36074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37608,
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

_source line 20 · 2026-05-25T20:19:59.042Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C4RBjtDp5X9PtMs8JH2tkd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_extended_results.json",
  "limit": 5000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "228b5ffc-8aeb-45dc-ba16-fc0f2b05745a",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZbgbENMP9vWXMJhFe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1cf5fdeb-98f5-46b0-aff1-b02a86192a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PSCu5yauaaZ3m9SNbv62xQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 37608,
      "cache_read_input_tokens": 36074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37608,
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

_source line 21 · 2026-05-25T20:19:59.051Z_

<details><summary>↩ Tool result · `toolu_01C4RBjtDp5X9PtMs8JH2tkd`</summary>

```text
1	{
2	  "part1_vbp1_vs_eps": {
3	    "n_positive_vbp1": 12498,
4	    "correlation": 0.9999462989087413,
5	    "eps_over_vbp1_median": 0.004871799957633522,
6	    "eps_over_vbp1_max": 0.0049950637065386775,
7	    "max_step_deviation": 0.0353150873026018,
8	    "max_vbp1": 7.115093692727774
9	  },
10	  "part2_dd_coverage": {
11	    "acc=0.50_skew=1.0": {
12	      "dd_fraction": 0.029666666666666668,
13	      "vbp1_neg_fraction": 0.912,
14	      "max_vbp1_when_positive": 1.5350530518635974
15	    },
16	    "acc=0.50_skew=2.0": {
17	      "dd_fraction": 0.027,
18	      "vbp1_neg_fraction": 0.9096666666666666,
19	      "max_vbp1_when_positive": 1.4600264556535532
20	    },
21	    "acc=0.50_skew=5.0": {
22	      "dd_fraction": 0.021333333333333333,
23	      "vbp1_neg_fraction": 0.9136666666666666,
24	      "max_vbp1_when_positive": 1.116614501016496
25	    },
26	    "acc=0.50_skew=10.0": {
27	      "dd_fraction": 0.01633333333333333,
28	      "vbp1_neg_fraction": 0.9133333333333333,
29	      "max_vbp1_when_positive": 1.175957931197428
30	    },
31	    "acc=0.60_skew=1.0": {
32	      "dd_fraction": 0.043333333333333335,
33	      "vbp1_neg_fraction": 0.9623333333333334,
34	      "max_vbp1_when_positive": 0.41827343191042665
35	    },
36	    "acc=0.60_skew=2.0": {
37	      "dd_fraction": 0.04666666666666667,
38	      "vbp1_neg_fraction": 0.9616666666666667,
39	      "max_vbp1_when_positive": 0.8267585518839367
40	    },
41	    "acc=0.60_skew=5.0": {
42	      "dd_fraction": 0.04133333333333333,
43	      "vbp1_neg_fraction": 0.9596666666666667,
44	      "max_vbp1_when_positive": 0.49257395165295037
45	    },
46	    "acc=0.60_skew=10.0": {
47	      "dd_fraction": 0.030333333333333334,
48	      "vbp1_neg_fraction": 0.9596666666666667,
49	      "max_vbp1_when_positive": 0.44512606779201613
50	    },
51	    "acc=0.70_skew=1.0": {
52	      "dd_fraction": 0.095,
53	      "vbp1_neg_fraction": 0.987,
54	      "max_vbp1_when_positive": 0.25931737364084917
55	    },
56	    "acc=0.70_skew=2.0": {
57	      "dd_fraction": 0.09133333333333334,
58	      "vbp1_neg_fraction": 0.988,
59	      "max_vbp1_when_positive": 0.352692304725319
60	    },
61	    "acc=0.70_skew=5.0": {
62	      "dd_fraction": 0.06333333333333334,
63	      "vbp1_neg_fraction": 0.984,
64	      "max_vbp1_when_positive": 0.3361038747450431
65	    },
66	    "acc=0.70_skew=10.0": {
67	      "dd_fraction": 0.051666666666666666,
68	      "vbp1_neg_fraction": 0.985,
69	      "max_vbp1_when_positive": 0.20886698604933507
70	    },
71	    "acc=0.80_skew=1.0": {
72	      "dd_fraction": 0.16733333333333333,
73	      "vbp1_neg_fraction": 0.998,
74	      "max_vbp1_when_positive": 0.28215009568001026
75	    },
76	    "acc=0.80_skew=2.0": {
77	      "dd_fraction": 0.14733333333333334,
78	      "vbp1_neg_fraction": 0.9966666666666667,
79	      "max_vbp1_when_positive": 0.05018717049160837
80	    },
81	    "acc=0.80_skew=5.0": {
82	      "dd_fraction": 0.1,
83	      "vbp1_neg_fraction": 0.9953333333333333,
84	      "max_vbp1_when_positive": 0.1038327205236973
85	    },
86	    "acc=0.80_skew=10.0": {
87	      "dd_fraction": 0.08766666666666667,
88	      "vbp1_neg_fraction": 0.9946666666666667,
89	      "max_vbp1_when_positive": 0.09241988266047296
90	    },
91	    "acc=0.90_skew=1.0": {
92	      "dd_fraction": 0.2743333333333333,
93	      "vbp1_neg_fraction": 0.9986666666666667,
94	      "max_vbp1_when_positive": 0.06188204967200672
95	    },
96	    "acc=0.90_skew=2.0": {
97	      "dd_fraction": 0.23566666666666666,
98	      "vbp1_neg_fraction": 0.9996666666666667,
99	      "max_vbp1_when_positive": 0.009793051334563985
100	    },
101	    "acc=0.90_skew=5.0": {
102	      "dd_fraction": 0.15566666666666668,
103	      "vbp1_neg_fraction": 0.9996666666666667,
104	      "max_vbp1_when_positive": 0.01485581257085189
105	    },
106	    "acc=0.90_skew=10.0": {
107	      "dd_fraction": 0.13933333333333334,
108	      "vbp1_neg_fraction": 0.9983333333333333,
109	      "max_vbp1_when_positive": 0.16772974094251447
110	    },
111	    "acc=0.95_skew=1.0": {
112	      "dd_fraction": 0.36566666666666664,
113	      "vbp1_neg_fraction": 1.0,
114	      "max_vbp1_when_positive": 0.0
115	    },
116	    "acc=0.95_skew=2.0": {
117	      "dd_fraction": 0.3016666666666667,
118	      "vbp1_neg_fraction": 0.9996666666666667,
119	      "max_vbp1_when_positive": 0.010441831976564453
120	    },
121	    "acc=0.95_skew=5.0": {
122	      "dd_fraction": 0.20566666666666666,
123	      "vbp1_neg_fraction": 0.9986666666666667,
124	      "max_vbp1_when_positive": 0.04113102293764914
125	    },
126	    "acc=0.95_skew=10.0": {
127	      "dd_fraction": 0.16133333333333333,
128	      "vbp1_neg_fraction": 0.9986666666666667,
129	      "max_vbp1_when_positive": 0.10343211405014019
130	    }
131	  },
132	  "part3_tight_bounds": {
133	    "c=0.3": {
134	      "n_positive": 2762,
135	      "max_ratio": 1.3234965617417032,
136	      "p99_ratio": 0.9519110315479923,
137	      "median_ratio": 0.1397984661651869,
138	      "theoretical_bound_4(1-c)2": 1.9599999999999997,
139	      "tightness": 0.6752533478273997
140	    },
141	    "c=0.5": {
142	      "n_positive": 760,
143	      "max_ratio": 0.6085495535773661,
144	      "p99_ratio": 0.507116493074508,
145	      "median_ratio": 0.09940916080731152,
146	      "theoretical_bound_4(1-c)2": 1.0,
147	      "tightness": 0.6085495535773661
148	    },
149	    "c=0.7": {
150	      "n_positive": 155,
151	      "max_ratio": 0.3745137721548742,
152	      "p99_ratio": 0.3300010545809061,
153	      "median_ratio": 0.058290605534842256,
154	      "theoretical_bound_4(1-c)2": 0.3600000000000001,
155	      "tightness": 1.040316033763539
156	    },
157	    "c=0.9": {
158	      "n_positive": 21,
159	      "max_ratio": 0.19336458200865173,
160	      "p99_ratio": 0.18244857386172442,
161	      "median_ratio": 0.03602991135045748,
162	      "theoretical_bound_4(1-c)2": 0.03999999999999998,
163	      "tightness": 4.834114550216295
164	    }
165	  },
166	  "part4_spectral": {
167	    "dd_holds": {
168	      "n": 25,
169	      "max_eigenvalue": 8.720889418157496e-17,
170	      "frac_positive": 0.0
171	    },
172	    "dd_fails": {
173	      "n": 4975,
174	      "max_eigenvalue": 0.6312973477423304,
175	      "frac_positive": 0.9312562814070352
176	    }
177	  },
178	  "part5_half_diag": {
179	    "n_tests": 30000,
180	    "n_vbp1_positive": 1945,
181	    "frac_positive": 0.06483333333333334,
182	    "max_vbp1": 1.6688143698561309,
183	    "max_step_deviation": 0.00821165908310939,
184	    "worst_case": {
185	      "K": 3,
186	      "vbp1": 1.6688143698561309,
187	      "step_dev": 0.00821165908310939,
188	      "C0_diag": [
189	        0.40242781505959124,
190	        0.3683792672477162,
191	        0.3497976897090179
192	      ],
193	      "p": [
194	        0.08426826498285596,
195	        0.47487082170800465,
196	        0.4408609133091393
197	      ],
198	      "p_ratio": 5.635227232987593
199	    }
200	  },
201	  "part6_half_diag_sufficiency": {
202	    "n_tests": 100000,
203	    "n_counterexamples": 8715,
204	    "alpha_half_is_sufficient": false,
205	    "examples": [
206	      {
207	        "K": 3,
208	        "vbp1": 0.02988941619221741,
209	        "C0_diag": [
210	          0.3740591777245049,
211	          0.4375810509816282,
212	          0.3424560666037175
213	        ],
214	        "C0_diag_min": 0.3424560666037175,
215	        "p": [
216	          0.10145601406871708,
217	          0.581421353752031,
218	          0.3171226321792519
219	        ],
220	        "g": [
221	          -0.21078178575439427,
222	          -0.2317118648373226,
223	          0.919374685128188
224	        ],
225	        "p_ratio": 5.730772681038198
226	      },
227	      {
228	        "K": 5,
229	        "vbp1": 0.04063661301875099,
230	        "C0_diag": [
231	          0.34432339755918595,
232	          0.346214192762531,
233	          0.3369141697539339,
234	          0.3637477683427154,
235	          0.3488899769706917
236	        ],
237	        "C0_diag_min": 0.3369141697539339,
238	        "p": [
239	          0.020431414162060613,
240	          0.11275614718607027,
241	          0.5755165078376975,
242	          0.07024030938916254,
243	          0.2210556214250091
244	        ],
245	        "g": [
246	          0.22177732847494636,
247	          -1.3708332142564035,
248	          0.5110374462214101,
249	          0.0006123836374689396,
250	          -1.4049698774289676
251	        ],
252	        "p_ratio": 28.168217005085353
253	      },
254	      {
255	        "K": 3,
256	        "vbp1": 0.3240258768194111,
257	        "C0_diag": [
258	          0.39527664165291226,
259	          0.4075650854721878,
260	          0.3468976911258749
261	        ],
262	        "C0_diag_min": 0.3468976911258749,
263	        "p": [
264	          0.33104917129623224,
265	          0.30685291184413765,
266	          0.3620979168596301
267	        ],
268	        "g": [
269	          2.5276803158404637,
270	          0.6301442695955182,
271	          0.11557110526769945
272	        ],
273	        "p_ratio": 1.1800374149408546
274	      },
275	      {
276	        "K": 3,
277	        "vbp1": 0.013348843144847591,
278	        "C0_diag": [
279	          0.34647789303222604,
280	          0.37449002137537224,
281	          0.43641281108783614
282	        ],
283	        "C0_diag_min": 0.34647789303222604,
284	        "p": [
285	          0.4897381913927251,
286	          0.37919544412859985,
287	          0.13106636447867506
288	        ],
289	        "g": [
290	          -0.4279812846993582,
291	          -0.10529437680955309,
292	          0.18537356074109648
293	        ],
294	        "p_ratio": 3.736566535134246
295	      },
296	      {
297	        "K": 3,
298	        "vbp1": 0.011968133618821986,
299	        "C0_diag": [
300	          0.8199403587297738,
301	          0.4752133912786488,
302	          0.4022731414991457
303	        ],
304	        "C0_diag_min": 0.4022731414991457,
305	        "p": [
306	          0.22152368015176918,
307	          0.19593399050666052,
308	          0.5825423293415704
309	        ],
310	        "g": [
311	          -1.2260514177788986,
312	          -1.9848854023260813,
313	          -0.6587200982866831
314	        ],
315	        "p_ratio": 2.9731560503371037
316	      }
317	    ]
318	  }
319	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cf5fdeb-98f5-46b0-aff1-b02a86192a64",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "9f058296-e385-4ecb-a514-02fef944bd65",
  "sourceToolAssistantUUID": "1cf5fdeb-98f5-46b0-aff1-b02a86192a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T20:19:59.433Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01HkStBYvdj94fH3U7aEMw96`</summary>

```json
{
  "pattern": "sign_reversal",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f058296-e385-4ecb-a514-02fef944bd65",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZbgbENMP9vWXMJhFe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4863ded7-8ab3-412f-ba9b-9585757df8b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PSCu5yauaaZ3m9SNbv62xQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 37608,
      "cache_read_input_tokens": 36074,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 37608
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 234,
          "cache_read_input_tokens": 36074,
          "cache_creation_input_tokens": 37608,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 37608,
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

_source line 23 · 2026-05-25T20:19:59.491Z_

<details><summary>↩ Tool result · `toolu_01HkStBYvdj94fH3U7aEMw96`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_realistic_epsilon.py:80:def check_sign_reversal(plim_perturbed, plim_identity, K):
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_realistic_epsilon.py:113:    Returns: dict of {ε: sign_reversal_rate}
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_realistic_epsilon.py:156:            if check_sign_reversal(plim_avg, plim_identity, K):
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_realistic_epsilon.py:353:            "sign_reversal_threshold": SIGN_REVERSAL_THRESHOLD,
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/mvp_exposure_dag.py:303:        "sign_reversal": sign_rev_count,
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/mvp_exposure_dag.py:392:    print(f"Sign reversal (any component):  {search['sign_reversal']:,} "
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/mvp_exposure_dag.py:393:          f"({100*search['sign_reversal']/search['n_searched']:.1f}%)")
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_realistic_epsilon_results.json:8:    "sign_reversal_threshold": 0.05,
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dag.py:303:        "sign_reversal": sign_rev_count,
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dag.py:392:    print(f"Sign reversal (any component):  {search['sign_reversal']:,} "
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dag.py:393:          f"({100*search['sign_reversal']/search['n_searched']:.1f}%)")
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/sign_reversal_determinants.py:27:OUT_FILE = PROJ / "artifacts/sign_reversal_determinants_results.json"
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/imagined_experiments.yaml:33:    mediation_sign_reversal_rate: 0.47
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/imagined_experiments.yaml:36:    collider_sign_reversal_rate: 0.36
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/imagined_experiments.yaml:39:    frontdoor_sign_reversal_rate: 0.28
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/review_context.yaml:32:    mediation_sign_reversal_rate: 0.47
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/review_context.yaml:35:    collider_sign_reversal_rate: 0.36
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/review_context.yaml:38:    frontdoor_sign_reversal_rate: 0.28
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json:20:      "mediation_sign_reversal_rate": 0.47,
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json:23:      "collider_sign_reversal_rate": 0.36,
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json:26:      "frontdoor_sign_reversal_rate": 0.28,
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/meta.yaml:176:      mediation_sign_reversal_rate: 0.47
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/meta.yaml:179:      collider_sign_reversal_rate: 0.36
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/meta.yaml:182:      frontdoor_sign_reversal_rate: 0.28
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/meta.yaml:1780:        sign_reversal_rate: 0.18
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/meta.yaml:1866:      - sign_reversal
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/meta.yaml:1925:      - sign_reversal_rate
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/meta.yaml:3404:      exposure_sign_reversal_rate: 0.834
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/imagined_experiments.yaml:49:    exposure_sign_reversal_rate: 0.834
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/review_context.yaml:48:    exposure_sign_reversal_rate: 0.834
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json:11:      "exposure_sign_reversal_rate": 0.834,
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_worst_attempt0.log:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_worst_attempt0.log:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_worst.log:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_median_attempt0.log:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_median_attempt0.log:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_best.log:21:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_best.log:36:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_best.log:51:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_best_attempt0.log:4:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/phase2_best_attempt0.log:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/imagined_experiments.yaml:56:      sign_reversal_rate: 0.18
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/imagined_experiments.yaml:141:    - sign_reversal
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/imagined_experiments.yaml:200:    - sign_reversal_rate
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/review_context.yaml:55:      sign_reversal_rate: 0.18
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/review_context.yaml:140:    - sign_reversal
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/review_context.yaml:199:    - sign_reversal_rate
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json:27:        "sign_reversal_rate": 0.18,
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json:84:          "sign_reversal",
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json:161:          "sign_reversal_rate"
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_median.log:10:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_median.log:89:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_median.log:92:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_median.log:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/paper_agent_best.log:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_worst.log:8:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_worst.log:73:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_worst.log:90:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_worst.log:93:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_worst.log:96:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_worst.log:132:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/logs/review_worst.log:147:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4863ded7-8ab3-412f-ba9b-9585757df8b3",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "c8e69f7e-b798-4b4b-9a87-23a4979d0fbe",
  "sourceToolAssistantUUID": "4863ded7-8ab3-412f-ba9b-9585757df8b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-25T20:20:01.790Z_

Let me read the sign_reversal results file directly:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8e69f7e-b798-4b4b-9a87-23a4979d0fbe",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZrt9SDmLVg6th4xWp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c7ce6e46-b0e1-4f17-a171-185c970d1760",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K6Nq1VwsNXHMgMQWQXUoAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9093,
      "cache_read_input_tokens": 73682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9093,
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

_source line 25 · 2026-05-25T20:20:02.038Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VrcGCt29JhpS2XnyNq34g5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/sign_reversal_determinants_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7ce6e46-b0e1-4f17-a171-185c970d1760",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZrt9SDmLVg6th4xWp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ecbdb377-6440-4594-ade2-55ec908598b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K6Nq1VwsNXHMgMQWQXUoAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9093,
      "cache_read_input_tokens": 73682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9093,
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

_source line 26 · 2026-05-25T20:20:02.330Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YFMcvjY4fGLuTqqYTD9qDj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_exact_values.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecbdb377-6440-4594-ade2-55ec908598b9",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuZrt9SDmLVg6th4xWp",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "638b3122-3dcd-438e-a3ce-e9649734910a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K6Nq1VwsNXHMgMQWQXUoAH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9093,
      "cache_read_input_tokens": 73682,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9093
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 181,
          "cache_read_input_tokens": 73682,
          "cache_creation_input_tokens": 9093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9093,
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

_source line 27 · 2026-05-25T20:20:02.386Z_

<details><summary>↩ Tool result · reported error · `toolu_01VrcGCt29JhpS2XnyNq34g5`</summary>

```text
File content (91756 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecbdb377-6440-4594-ade2-55ec908598b9",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "2ecf81f6-5ed8-4b26-9bae-ff82ef916747",
  "toolUseResult": "Error: File content (91756 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "ecbdb377-6440-4594-ade2-55ec908598b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T20:20:02.644Z_

<details><summary>↩ Tool result · `toolu_01YFMcvjY4fGLuTqqYTD9qDj`</summary>

```text
1	# Plan 006 Exact Per-Config Values
2	# Extracted from asv_empirical_results.json on 2026-05-21
3	
4	## Table 1: Per-Config Macro F1
5	dataset | model | prompt | macro_f1 | weighted_f1
6	--- | --- | --- | --- | ---
7	humaid | deepseek | few-shot-3 | 0.686332528254669 | 0.7079850713700734
8	humaid | deepseek | few-shot-5 | 0.6854961636228544 | 0.7154159318159469
9	humaid | deepseek | zero-shot | 0.6896163310588191 | 0.7379106239347464
10	humaid | llama4 | few-shot-3 | 0.6157321052348829 | 0.6423408356103537
11	humaid | llama4 | few-shot-5 | 0.6242855183452943 | 0.6453307915826395
12	humaid | llama4 | zero-shot | 0.6144302991883744 | 0.6466720766954748
13	humaid | qwen3 | few-shot-3 | 0.6749099031385263 | 0.7229864000901446
14	humaid | qwen3 | few-shot-5 | 0.0 | 0.0
15	humaid | qwen3 | zero-shot | 0.6776464165672691 | 0.7261264737892993
16	
17	## Table 2: Per-Config × Topology Bias (from f1_vs_bias + biases)
18	dataset | model | prompt | topology | macro_f1 | weighted_f1 | tau_hat | bias | abs_bias | bias_pct | sign_flip
19	--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
20	humaid | llama4 | zero-shot | confounding | 0.6144302991883744 | 0.6466720766954748 | 2.120934379053557 | 0.12069570526147011 | 0.12069570526147011 | 0.06034065176464822 | False
21	humaid | llama4 | zero-shot | mediation | 0.6144302991883744 | 0.6466720766954748 | 0.5712933797533354 | 0.07307001250379075 | 0.07307001250379075 | 0.14666115101580984 | False
22	humaid | llama4 | zero-shot | collider | 0.6144302991883744 | 0.6466720766954748 | 0.9456694721398234 | 0.04595577469197598 | 0.04595577469197598 | 0.05107822057431757 | False
23	humaid | llama4 | zero-shot | exposure | 0.6144302991883744 | 0.6466720766954748 | 0.8828876330655444 | -0.11798447072494489 | 0.11798447072494489 | 0.11788166567747838 | False
24	humaid | llama4 | zero-shot | mbias | 0.6144302991883744 | 0.6466720766954748 | 0.4691488925499947 | 0.02786998543706848 | 0.02786998543706848 | 0.0631573025309736 | False
25	humaid | llama4 | zero-shot | iv | 0.6144302991883744 | 0.6466720766954748 | 1.5683599189072943 | 0.44922058382638075 | 0.44922058382638075 | 0.4013982618115216 | False
26	humaid | llama4 | zero-shot | frontdoor | 0.6144302991883744 | 0.6466720766954748 | 0.5715479467164649 | 0.07216071249027495 | 0.07216071249027495 | 0.14449851246616136 | False
27	humaid | llama4 | few-shot-3 | confounding | 0.6157321052348829 | 0.6423408356103537 | 2.120784699065214 | 0.12054602527312719 | 0.12054602527312719 | 0.06026582070058367 | False
28	humaid | llama4 | few-shot-3 | mediation | 0.6157321052348829 | 0.6423408356103537 | 0.5704612272617933 | 0.07223786001224863 | 0.07223786001224863 | 0.14499091122730687 | False
29	humaid | llama4 | few-shot-3 | collider | 0.6157321052348829 | 0.6423408356103537 | 0.9464381179128287 | 0.046724420464981264 | 0.046724420464981264 | 0.051932543205156306 | False
30	humaid | llama4 | few-shot-3 | exposure | 0.6157321052348829 | 0.6423408356103537 | 0.8786401807491107 | -0.12223192304137864 | 0.12223192304137864 | 0.12212541700229586 | False
31	humaid | llama4 | few-shot-3 | mbias | 0.6157321052348829 | 0.6423408356103537 | 0.46926932404242633 | 0.027990416929500106 | 0.027990416929500106 | 0.06343021721257384 | False
32	humaid | llama4 | few-shot-3 | iv | 0.6157321052348829 | 0.6423408356103537 | 1.570316539363992 | 0.4511772042830784 | 0.4511772042830784 | 0.4031465878647348 | False
33	humaid | llama4 | few-shot-3 | frontdoor | 0.6157321052348829 | 0.6423408356103537 | 0.5710035404886598 | 0.07161630626246979 | 0.07161630626246979 | 0.1434083639992132 | False
34	humaid | llama4 | few-shot-5 | confounding | 0.6242855183452943 | 0.6453307915826395 | 2.12365082586331 | 0.12341215207122325 | 0.12341215207122325 | 0.06169871310270007 | False
35	humaid | llama4 | few-shot-5 | mediation | 0.6242855183452943 | 0.6453307915826395 | 0.5719970141219267 | 0.07377364687238208 | 0.07377364687238208 | 0.14807343798355235 | False
36	humaid | llama4 | few-shot-5 | collider | 0.6242855183452943 | 0.6453307915826395 | 0.9460905799802515 | 0.04637688253240402 | 0.04637688253240402 | 0.051546267066910234 | False
37	humaid | llama4 | few-shot-5 | exposure | 0.6242855183452943 | 0.6453307915826395 | 0.8772737636412716 | -0.12359834014921767 | 0.12359834014921767 | 0.12349064349093926 | False
38	humaid | llama4 | few-shot-5 | mbias | 0.6242855183452943 | 0.6453307915826395 | 0.46978562845545446 | 0.02850672134252824 | 0.02850672134252824 | 0.0646002355495165 | False
39	humaid | llama4 | few-shot-5 | iv | 0.6242855183452943 | 0.6453307915826395 | 1.5907437428164128 | 0.4716044077354993 | 0.4716044077354993 | 0.4213991886018396 | False
40	humaid | llama4 | few-shot-5 | frontdoor | 0.6242855183452943 | 0.6453307915826395 | 0.5727726088866913 | 0.07338537466050138 | 0.07338537466050138 | 0.14695084221408547 | False
41	humaid | qwen3 | zero-shot | confounding | 0.6776464165672691 | 0.7261264737892993 | 2.0985054835166235 | 0.0982668097245365 | 0.0982668097245365 | 0.049127542133879744 | False
42	humaid | qwen3 | zero-shot | mediation | 0.6776464165672691 | 0.7261264737892993 | 0.5520423668109194 | 0.053818999561374814 | 0.053818999561374814 | 0.10802182936236819 | False
43	humaid | qwen3 | zero-shot | collider | 0.6776464165672691 | 0.7261264737892993 | 0.9366988618485531 | 0.03698516440070565 | 0.03698516440070565 | 0.04110770404587457 | False
44	humaid | qwen3 | zero-shot | exposure | 0.6776464165672691 | 0.7261264737892993 | 0.9004559503684615 | -0.10041615342202781 | 0.10041615342202781 | 0.10032865642046881 | False
45	humaid | qwen3 | zero-shot | mbias | 0.6776464165672691 | 0.7261264737892993 | 0.46536238966656945 | 0.024083482553643232 | 0.024083482553643232 | 0.0545765550209725 | False
46	humaid | qwen3 | zero-shot | iv | 0.6776464165672691 | 0.7261264737892993 | 1.2575469314140617 | 0.13840759633314814 | 0.13840759633314814 | 0.12367324782051495 | False
47	humaid | qwen3 | zero-shot | frontdoor | 0.6776464165672691 | 0.7261264737892993 | 0.5551445234004692 | 0.05575728917427919 | 0.05575728917427919 | 0.11165141067467647 | False
48	humaid | qwen3 | few-shot-3 | confounding | 0.6749099031385263 | 0.7229864000901446 | 2.1135019394277226 | 0.1132632656356356 | 0.1132632656356356 | 0.05662487538095099 | False
49	humaid | qwen3 | few-shot-3 | mediation | 0.6749099031385263 | 0.7229864000901446 | 0.562989233682857 | 0.06476586643331239 | 0.06476586643331239 | 0.129993634764371 | False
50	humaid | qwen3 | few-shot-3 | collider | 0.6749099031385263 | 0.7229864000901446 | 0.9413703101661668 | 0.04165661271831933 | 0.04165661271831933 | 0.04629985387183014 | False
51	humaid | qwen3 | few-shot-3 | exposure | 0.6749099031385263 | 0.7229864000901446 | 0.9109885849626933 | -0.089883518827796 | 0.089883518827796 | 0.08980519937301713 | False
52	humaid | qwen3 | few-shot-3 | mbias | 0.6749099031385263 | 0.7229864000901446 | 0.46883882807680594 | 0.027559920963879714 | 0.027559920963879714 | 0.0624546528729209 | False
53	humaid | qwen3 | few-shot-3 | iv | 0.6749099031385263 | 0.7229864000901446 | 1.3607364870283247 | 0.24159715194741116 | 0.24159715194741116 | 0.21587763415530714 | False
54	humaid | qwen3 | few-shot-3 | frontdoor | 0.6749099031385263 | 0.7229864000901446 | 0.5662046362014267 | 0.06681740197523672 | 0.06681740197523672 | 0.13379877857464972 | False
55	humaid | qwen3 | few-shot-5 | confounding | 0.0 | 0.0 | None | None | None | None | False
56	humaid | qwen3 | few-shot-5 | mediation | 0.0 | 0.0 | None | None | None | None | False
57	humaid | qwen3 | few-shot-5 | collider | 0.0 | 0.0 | None | None | None | None | False
58	humaid | qwen3 | few-shot-5 | exposure | 0.0 | 0.0 | None | None | None | None | False
59	humaid | qwen3 | few-shot-5 | mbias | 0.0 | 0.0 | None | None | None | None | False
60	humaid | qwen3 | few-shot-5 | iv | 0.0 | 0.0 | None | None | None | None | False
61	humaid | qwen3 | few-shot-5 | frontdoor | 0.0 | 0.0 | None | None | None | None | False
62	humaid | deepseek | zero-shot | confounding | 0.6896163310588191 | 0.7379106239347464 | 2.098037116466373 | 0.09779844267428617 | 0.09779844267428617 | 0.048893386552154895 | False
63	humaid | deepseek | zero-shot | mediation | 0.6896163310588191 | 0.7379106239347464 | 0.5525720601157175 | 0.05434869286617283 | 0.05434869286617283 | 0.10908499367704537 | False
64	humaid | deepseek | zero-shot | collider | 0.6896163310588191 | 0.7379106239347464 | 0.9381344159354087 | 0.038420718487561234 | 0.038420718487561234 | 0.042703271714709355 | False
65	humaid | deepseek | zero-shot | exposure | 0.6896163310588191 | 0.7379106239347464 | 0.8930286199464353 | -0.10784348384405396 | 0.10784348384405396 | 0.10774951508352623 | False
66	humaid | deepseek | zero-shot | mbias | 0.6896163310588191 | 0.7379106239347464 | 0.46359439600401514 | 0.02231548889108892 | 0.02231548889108892 | 0.0505700329913531 | False
67	humaid | deepseek | zero-shot | iv | 0.6896163310588191 | 0.7379106239347464 | 1.271872631402271 | 0.15273329632135746 | 0.15273329632135746 | 0.13647388804390015 | False
68	humaid | deepseek | zero-shot | frontdoor | 0.6896163310588191 | 0.7379106239347464 | 0.5530531479739429 | 0.053665913747752925 | 0.053665913747752925 | 0.10746352743860038 | False
69	humaid | deepseek | few-shot-3 | confounding | 0.686332528254669 | 0.7079850713700734 | 2.123607139445277 | 0.12336846565318993 | 0.12336846565318993 | 0.061676872500073136 | False
70	humaid | deepseek | few-shot-3 | mediation | 0.686332528254669 | 0.7079850713700734 | 0.5687149487065887 | 0.07049158145704404 | 0.07049158145704404 | 0.14148589988100055 | False
71	humaid | deepseek | few-shot-3 | collider | 0.686332528254669 | 0.7079850713700734 | 0.9496495466944775 | 0.04993584924663008 | 0.04993584924663008 | 0.05550193287962547 | False
72	humaid | deepseek | few-shot-3 | exposure | 0.686332528254669 | 0.7079850713700734 | 0.8266415174610339 | -0.17423058632945543 | 0.17423058632945543 | 0.17407877157292295 | False
73	humaid | deepseek | few-shot-3 | mbias | 0.686332528254669 | 0.7079850713700734 | 0.4682145757221894 | 0.026935668609263164 | 0.026935668609263164 | 0.06104000933443698 | False
74	humaid | deepseek | few-shot-3 | iv | 0.686332528254669 | 0.7079850713700734 | 1.5846778546263218 | 0.46553851954540826 | 0.46553851954540826 | 0.4159790518950439 | False
75	humaid | deepseek | few-shot-3 | frontdoor | 0.686332528254669 | 0.7079850713700734 | 0.5697887654602263 | 0.07040153123403631 | 0.07040153123403631 | 0.14097583279861933 | False
76	humaid | deepseek | few-shot-5 | confounding | 0.6854961636228544 | 0.7154159318159469 | 2.1126646222388654 | 0.11242594844677845 | 0.11242594844677845 | 0.05620626674197804 | False
77	humaid | deepseek | few-shot-5 | mediation | 0.6854961636228544 | 0.7154159318159469 | 0.5594037432186939 | 0.06118037596914927 | 0.06118037596914927 | 0.12279708257542629 | False
78	humaid | deepseek | few-shot-5 | collider | 0.6854961636228544 | 0.7154159318159469 | 0.941628164464706 | 0.041914467016858525 | 0.041914467016858525 | 0.04658644981815243 | False
79	humaid | deepseek | few-shot-5 | exposure | 0.6854961636228544 | 0.7154159318159469 | 0.8403545964483055 | -0.16051750734218384 | 0.16051750734218384 | 0.1603776413932151 | False
80	humaid | deepseek | few-shot-5 | mbias | 0.6854961636228544 | 0.7154159318159469 | 0.4664318858106293 | 0.025152978697703055 | 0.025152978697703055 | 0.05700018353985417 | False
81	humaid | deepseek | few-shot-5 | iv | 0.6854961636228544 | 0.7154159318159469 | 1.4621030536999786 | 0.34296371861906505 | 0.34296371861906505 | 0.3064531000460893 | False
82	humaid | deepseek | few-shot-5 | frontdoor | 0.6854961636228544 | 0.7154159318159469 | 0.5618456528567989 | 0.062458418630608914 | 0.062458418630608914 | 0.12507011463236425 | False
83	
84	## Table 3: ASV Details
85	dataset | model | prompt | topology | asv_type | asv
86	--- | --- | --- | --- | --- | ---
87	humaid | llama4 | zero-shot | confounding | magnitude | None
88	humaid | llama4 | zero-shot | confounding | significance | None
89	humaid | llama4 | zero-shot | confounding | sign_flip | None
90	humaid | llama4 | zero-shot | mediation | magnitude | 0.6193806623770686
91	humaid | llama4 | zero-shot | mediation | significance | None
92	humaid | llama4 | zero-shot | mediation | sign_flip | None
93	humaid | llama4 | zero-shot | collider | magnitude | None
94	humaid | llama4 | zero-shot | collider | significance | None
95	humaid | llama4 | zero-shot | collider | sign_flip | None
96	humaid | llama4 | zero-shot | exposure | magnitude | 0.9040865953646517
97	humaid | llama4 | zero-shot | exposure | significance | None
98	humaid | llama4 | zero-shot | exposure | sign_flip | None
99	humaid | llama4 | zero-shot | mbias | magnitude | None
100	humaid | llama4 | zero-shot | mbias | significance | None
101	humaid | llama4 | zero-shot | mbias | sign_flip | None
102	humaid | llama4 | zero-shot | iv | magnitude | 0.31840581893305214
103	humaid | llama4 | zero-shot | iv | significance | None
104	humaid | llama4 | zero-shot | iv | sign_flip | None
105	humaid | llama4 | zero-shot | frontdoor | magnitude | 0.6310013127030923
106	humaid | llama4 | zero-shot | frontdoor | significance | None
107	humaid | llama4 | zero-shot | frontdoor | sign_flip | None
108	humaid | llama4 | few-shot-3 | confounding | magnitude | None
109	humaid | llama4 | few-shot-3 | confounding | significance | None
110	humaid | llama4 | few-shot-3 | confounding | sign_flip | None
111	humaid | llama4 | few-shot-3 | mediation | magnitude | 0.6315460306871247
112	humaid | llama4 | few-shot-3 | mediation | significance | None
113	humaid | llama4 | few-shot-3 | mediation | sign_flip | None
114	humaid | llama4 | few-shot-3 | collider | magnitude | None
115	humaid | llama4 | few-shot-3 | collider | significance | None
116	humaid | llama4 | few-shot-3 | collider | sign_flip | None
117	humaid | llama4 | few-shot-3 | exposure | magnitude | 0.889342895263509
118	humaid | llama4 | few-shot-3 | exposure | significance | 1.6807454969979985
119	humaid | llama4 | few-shot-3 | exposure | sign_flip | None
120	humaid | llama4 | few-shot-3 | mbias | magnitude | None
121	humaid | llama4 | few-shot-3 | mbias | significance | None
122	humaid | llama4 | few-shot-3 | mbias | sign_flip | None
123	humaid | llama4 | few-shot-3 | iv | magnitude | 0.31746164109406266
124	humaid | llama4 | few-shot-3 | iv | significance | None
125	humaid | llama4 | few-shot-3 | iv | sign_flip | None
126	humaid | llama4 | few-shot-3 | frontdoor | magnitude | 0.6371747831887925
127	humaid | llama4 | few-shot-3 | frontdoor | significance | None
128	humaid | llama4 | few-shot-3 | frontdoor | sign_flip | None
129	humaid | llama4 | few-shot-5 | confounding | magnitude | None
130	humaid | llama4 | few-shot-5 | confounding | significance | None
131	humaid | llama4 | few-shot-5 | confounding | sign_flip | None
132	humaid | llama4 | few-shot-5 | mediation | magnitude | 0.620456648518367
133	humaid | llama4 | few-shot-5 | mediation | significance | None
134	humaid | llama4 | few-shot-5 | mediation | sign_flip | None
135	humaid | llama4 | few-shot-5 | collider | magnitude | None
136	humaid | llama4 | few-shot-5 | collider | significance | None
137	humaid | llama4 | few-shot-5 | collider | sign_flip | None
138	humaid | llama4 | few-shot-5 | exposure | magnitude | 0.8827820697669413
139	humaid | llama4 | few-shot-5 | exposure | significance | 1.7039746928059565
140	humaid | llama4 | few-shot-5 | exposure | sign_flip | None
141	humaid | llama4 | few-shot-5 | mbias | magnitude | None
142	humaid | llama4 | few-shot-5 | mbias | significance | None
143	humaid | llama4 | few-shot-5 | mbias | sign_flip | None
144	humaid | llama4 | few-shot-5 | iv | magnitude | 0.3068066883298543
145	humaid | llama4 | few-shot-5 | iv | significance | None
146	humaid | llama4 | few-shot-5 | iv | sign_flip | None
147	humaid | llama4 | few-shot-5 | frontdoor | magnitude | 0.6227377391379199
148	humaid | llama4 | few-shot-5 | frontdoor | significance | None
149	humaid | llama4 | few-shot-5 | frontdoor | sign_flip | None
150	humaid | qwen3 | zero-shot | confounding | magnitude | None
151	humaid | qwen3 | zero-shot | confounding | significance | None
152	humaid | qwen3 | zero-shot | confounding | sign_flip | None
153	humaid | qwen3 | zero-shot | mediation | magnitude | 0.901345995369462
154	humaid | qwen3 | zero-shot | mediation | significance | None
155	humaid | qwen3 | zero-shot | mediation | sign_flip | None
156	humaid | qwen3 | zero-shot | collider | magnitude | None
157	humaid | qwen3 | zero-shot | collider | significance | None
158	humaid | qwen3 | zero-shot | collider | sign_flip | None
159	humaid | qwen3 | zero-shot | exposure | magnitude | 0.9973413648314563
160	humaid | qwen3 | zero-shot | exposure | significance | None
161	humaid | qwen3 | zero-shot | exposure | sign_flip | None
162	humaid | qwen3 | zero-shot | mbias | magnitude | None
163	humaid | qwen3 | zero-shot | mbias | significance | None
164	humaid | qwen3 | zero-shot | mbias | sign_flip | None
165	humaid | qwen3 | zero-shot | iv | magnitude | 0.8265706549464349
166	humaid | qwen3 | zero-shot | iv | significance | None
167	humaid | qwen3 | zero-shot | iv | sign_flip | None
168	humaid | qwen3 | zero-shot | frontdoor | magnitude | 0.8649688027312327
169	humaid | qwen3 | zero-shot | frontdoor | significance | None
170	humaid | qwen3 | zero-shot | frontdoor | sign_flip | None
171	humaid | qwen3 | few-shot-3 | confounding | magnitude | None
172	humaid | qwen3 | few-shot-3 | confounding | significance | None
173	humaid | qwen3 | few-shot-3 | confounding | sign_flip | None
174	humaid | qwen3 | few-shot-3 | mediation | magnitude | 0.7057283472000201
175	humaid | qwen3 | few-shot-3 | mediation | significance | None
176	humaid | qwen3 | few-shot-3 | mediation | sign_flip | None
177	humaid | qwen3 | few-shot-3 | collider | magnitude | None
178	humaid | qwen3 | few-shot-3 | collider | significance | None
179	humaid | qwen3 | few-shot-3 | collider | sign_flip | None
180	humaid | qwen3 | few-shot-3 | exposure | magnitude | 1.1135557877159197
181	humaid | qwen3 | few-shot-3 | exposure | significance | None
182	humaid | qwen3 | few-shot-3 | exposure | sign_flip | None
183	humaid | qwen3 | few-shot-3 | mbias | magnitude | None
184	humaid | qwen3 | few-shot-3 | mbias | significance | None
185	humaid | qwen3 | few-shot-3 | mbias | sign_flip | None
186	humaid | qwen3 | few-shot-3 | iv | magnitude | 0.5122576476560894
187	humaid | qwen3 | few-shot-3 | iv | significance | None
188	humaid | qwen3 | few-shot-3 | iv | sign_flip | None
189	humaid | qwen3 | few-shot-3 | frontdoor | magnitude | 0.6826437750953466
190	humaid | qwen3 | few-shot-3 | frontdoor | significance | None
191	humaid | qwen3 | few-shot-3 | frontdoor | sign_flip | None
192	humaid | qwen3 | few-shot-5 | confounding | magnitude | None
193	humaid | qwen3 | few-shot-5 | confounding | significance | None
194	humaid | qwen3 | few-shot-5 | confounding | sign_flip | None
195	humaid | qwen3 | few-shot-5 | mediation | magnitude | None
196	humaid | qwen3 | few-shot-5 | mediation | significance | None
197	humaid | qwen3 | few-shot-5 | mediation | sign_flip | None
198	humaid | qwen3 | few-shot-5 | collider | magnitude | None
199	humaid | qwen3 | few-shot-5 | collider | significance | None
200	humaid | qwen3 | few-shot-5 | collider | sign_flip | None
201	humaid | qwen3 | few-shot-5 | exposure | magnitude | None
202	humaid | qwen3 | few-shot-5 | exposure | significance | None
203	humaid | qwen3 | few-shot-5 | exposure | sign_flip | None
204	humaid | qwen3 | few-shot-5 | mbias | magnitude | None
205	humaid | qwen3 | few-shot-5 | mbias | significance | None
206	humaid | qwen3 | few-shot-5 | mbias | sign_flip | None
207	humaid | qwen3 | few-shot-5 | iv | magnitude | None
208	humaid | qwen3 | few-shot-5 | iv | significance | None
209	humaid | qwen3 | few-shot-5 | iv | sign_flip | None
210	humaid | qwen3 | few-shot-5 | frontdoor | magnitude | None
211	humaid | qwen3 | few-shot-5 | frontdoor | significance | None
212	humaid | qwen3 | few-shot-5 | frontdoor | sign_flip | None
213	humaid | deepseek | zero-shot | confounding | magnitude | None
214	humaid | deepseek | zero-shot | confounding | significance | None
215	humaid | deepseek | zero-shot | confounding | sign_flip | None
216	humaid | deepseek | zero-shot | mediation | magnitude | 0.894985545919502
217	humaid | deepseek | zero-shot | mediation | significance | None
218	humaid | deepseek | zero-shot | mediation | sign_flip | None
219	humaid | deepseek | zero-shot | collider | magnitude | None
220	humaid | deepseek | zero-shot | collider | significance | None
221	humaid | deepseek | zero-shot | collider | sign_flip | None
222	humaid | deepseek | zero-shot | exposure | magnitude | 0.9375138981543252
223	humaid | deepseek | zero-shot | exposure | significance | None
224	humaid | deepseek | zero-shot | exposure | sign_flip | None
225	humaid | deepseek | zero-shot | mbias | magnitude | None
226	humaid | deepseek | zero-shot | mbias | significance | None
227	humaid | deepseek | zero-shot | mbias | sign_flip | None
228	humaid | deepseek | zero-shot | iv | magnitude | 0.7579497442739604
229	humaid | deepseek | zero-shot | iv | significance | None
230	humaid | deepseek | zero-shot | iv | sign_flip | None
231	humaid | deepseek | zero-shot | frontdoor | magnitude | 0.9119968868134313
232	humaid | deepseek | zero-shot | frontdoor | significance | None
233	humaid | deepseek | zero-shot | frontdoor | sign_flip | None
234	humaid | deepseek | few-shot-3 | confounding | magnitude | None
235	humaid | deepseek | few-shot-3 | confounding | significance | None
236	humaid | deepseek | few-shot-3 | confounding | sign_flip | None
237	humaid | deepseek | few-shot-3 | mediation | magnitude | 0.6496893620690438
238	humaid | deepseek | few-shot-3 | mediation | significance | None
239	humaid | deepseek | few-shot-3 | mediation | sign_flip | None
240	humaid | deepseek | few-shot-3 | collider | magnitude | None
241	humaid | deepseek | few-shot-3 | collider | significance | None
242	humaid | deepseek | few-shot-3 | collider | sign_flip | None
243	humaid | deepseek | few-shot-3 | exposure | magnitude | 0.6496893620690438
244	humaid | deepseek | few-shot-3 | exposure | significance | None
245	humaid | deepseek | few-shot-3 | exposure | sign_flip | None
246	humaid | deepseek | few-shot-3 | mbias | magnitude | None
247	humaid | deepseek | few-shot-3 | mbias | significance | None
248	humaid | deepseek | few-shot-3 | mbias | sign_flip | None
249	humaid | deepseek | few-shot-3 | iv | magnitude | 0.3102022663635167
250	humaid | deepseek | few-shot-3 | iv | significance | None
251	humaid | deepseek | few-shot-3 | iv | sign_flip | None
252	humaid | deepseek | few-shot-3 | frontdoor | magnitude | 0.6496893620690438
253	humaid | deepseek | few-shot-3 | frontdoor | significance | None
254	humaid | deepseek | few-shot-3 | frontdoor | sign_flip | None
255	humaid | deepseek | few-shot-5 | confounding | magnitude | None
256	humaid | deepseek | few-shot-5 | confounding | significance | None
257	humaid | deepseek | few-shot-5 | confounding | sign_flip | None
258	humaid | deepseek | few-shot-5 | mediation | magnitude | 0.7752759747374162
259	humaid | deepseek | few-shot-5 | mediation | significance | None
260	humaid | deepseek | few-shot-5 | mediation | sign_flip | None
261	humaid | deepseek | few-shot-5 | collider | magnitude | None
262	humaid | deepseek | few-shot-5 | collider | significance | None
263	humaid | deepseek | few-shot-5 | collider | sign_flip | None
264	humaid | deepseek | few-shot-5 | exposure | magnitude | 0.693162838485998
265	humaid | deepseek | few-shot-5 | exposure | significance | None
266	humaid | deepseek | few-shot-5 | exposure | sign_flip | None
267	humaid | deepseek | few-shot-5 | mbias | magnitude | None
268	humaid | deepseek | few-shot-5 | mbias | significance | None
269	humaid | deepseek | few-shot-5 | mbias | sign_flip | None
270	humaid | deepseek | few-shot-5 | iv | magnitude | 0.3881711895521589
271	humaid | deepseek | few-shot-5 | iv | significance | None
272	humaid | deepseek | few-shot-5 | iv | sign_flip | None
273	humaid | deepseek | few-shot-5 | frontdoor | magnitude | 0.7560806961331886
274	humaid | deepseek | few-shot-5 | frontdoor | significance | None
275	humaid | deepseek | few-shot-5 | frontdoor | sign_flip | None
276	
277	## Table 4: Type I/II Error and ASV Safety
278	dataset | model | prompt | topology | type1_before | type1_after | power_before | power_after | asv_safe | magnitude_asv | valid_h0 | valid_h1
279	--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
280	humaid | llama4 | zero-shot | confounding | 1.0 | 1.0 | 1.0 | 1.0 | True | None | 1000 | 1000
281	humaid | llama4 | zero-shot | mediation | 0.67 | 0.0 | 1.0 | 0.0 | False | 0.6193806623770686 | 1000 | 1000
282	humaid | llama4 | zero-shot | collider | 0.139 | 0.139 | 1.0 | 1.0 | True | None | 1000 | 1000
283	humaid | llama4 | zero-shot | exposure | 0.055 | 0.0 | 1.0 | 0.0 | False | 0.9040865953646517 | 1000 | 1000
284	humaid | llama4 | zero-shot | mbias | 0.629 | 0.629 | 1.0 | 1.0 | True | None | 1000 | 1000
285	humaid | llama4 | zero-shot | iv | 0.035 | 0.0 | 0.774 | 0.0 | False | 0.31840581893305214 | 1000 | 1000
286	humaid | llama4 | zero-shot | frontdoor | 0.056 | 0.0 | 1.0 | 0.0 | False | 0.6310013127030923 | 1000 | 1000
287	humaid | llama4 | few-shot-3 | confounding | 1.0 | 1.0 | 1.0 | 1.0 | True | None | 1000 | 1000
288	humaid | llama4 | few-shot-3 | mediation | 0.661 | 0.0 | 1.0 | 0.0 | False | 0.6315460306871247 | 1000 | 1000
289	humaid | llama4 | few-shot-3 | collider | 0.122 | 0.122 | 1.0 | 1.0 | True | None | 1000 | 1000
290	humaid | llama4 | few-shot-3 | exposure | 0.05 | 0.0 | 1.0 | 0.0 | False | 0.889342895263509 | 1000 | 1000
291	humaid | llama4 | few-shot-3 | mbias | 0.637 | 0.637 | 1.0 | 1.0 | True | None | 1000 | 1000
292	humaid | llama4 | few-shot-3 | iv | 0.038 | 0.0 | 0.774 | 0.0 | False | 0.31746164109406266 | 1000 | 1000
293	humaid | llama4 | few-shot-3 | frontdoor | 0.041 | 0.0 | 1.0 | 0.0 | False | 0.6371747831887925 | 1000 | 1000
294	humaid | llama4 | few-shot-5 | confounding | 1.0 | 1.0 | 1.0 | 1.0 | True | None | 1000 | 1000
295	humaid | llama4 | few-shot-5 | mediation | 0.716 | 0.0 | 1.0 | 0.0 | False | 0.620456648518367 | 1000 | 1000
296	humaid | llama4 | few-shot-5 | collider | 0.155 | 0.155 | 1.0 | 1.0 | True | None | 1000 | 1000
297	humaid | llama4 | few-shot-5 | exposure | 0.045 | 0.0 | 1.0 | 0.0 | False | 0.8827820697669413 | 1000 | 1000
298	humaid | llama4 | few-shot-5 | mbias | 0.617 | 0.617 | 1.0 | 1.0 | True | None | 1000 | 1000
299	humaid | llama4 | few-shot-5 | iv | 0.044 | 0.0 | 0.767 | 0.0 | False | 0.3068066883298543 | 1000 | 1000
300	humaid | llama4 | few-shot-5 | frontdoor | 0.044 | 0.0 | 1.0 | 0.0 | False | 0.6227377391379199 | 1000 | 1000
301	humaid | qwen3 | zero-shot | confounding | 1.0 | 1.0 | 1.0 | 1.0 | True | None | 1000 | 1000
302	humaid | qwen3 | zero-shot | mediation | 0.433 | 0.0 | 1.0 | 0.0 | False | 0.901345995369462 | 1000 | 1000
303	humaid | qwen3 | zero-shot | collider | 0.111 | 0.111 | 1.0 | 1.0 | True | None | 1000 | 1000
304	humaid | qwen3 | zero-shot | exposure | 0.061 | 0.0 | 1.0 | 0.0 | False | 0.9973413648314563 | 1000 | 1000
305	humaid | qwen3 | zero-shot | mbias | 0.687 | 0.687 | 1.0 | 1.0 | True | None | 1000 | 1000
306	humaid | qwen3 | zero-shot | iv | 0.05 | 0.0 | 0.764 | 0.0 | False | 0.8265706549464349 | 1000 | 1000
307	humaid | qwen3 | zero-shot | frontdoor | 0.059 | 0.0 | 1.0 | 0.0 | False | 0.8649688027312327 | 1000 | 1000
308	humaid | qwen3 | few-shot-3 | confounding | 1.0 | 1.0 | 1.0 | 1.0 | True | None | 1000 | 1000
309	humaid | qwen3 | few-shot-3 | mediation | 0.57 | 0.0 | 1.0 | 0.0 | False | 0.7057283472000201 | 1000 | 1000
310	humaid | qwen3 | few-shot-3 | collider | 0.117 | 0.117 | 1.0 | 1.0 | True | None | 1000 | 1000
311	humaid | qwen3 | few-shot-3 | exposure | 0.053 | 0.053 | 1.0 | 1.0 | True | 1.1135557877159197 | 1000 | 1000
312	humaid | qwen3 | few-shot-3 | mbias | 0.621 | 0.621 | 1.0 | 1.0 | True | None | 1000 | 1000
313	humaid | qwen3 | few-shot-3 | iv | 0.041 | 0.0 | 0.754 | 0.0 | False | 0.5122576476560894 | 1000 | 1000
314	humaid | qwen3 | few-shot-3 | frontdoor | 0.049 | 0.0 | 1.0 | 0.0 | False | 0.6826437750953466 | 1000 | 1000
315	humaid | qwen3 | few-shot-5 | confounding | 0.0 | 0.0 | 0.0 | 0.0 | True | None | 0 | 0
316	humaid | qwen3 | few-shot-5 | mediation | 0.0 | 0.0 | 0.0 | 0.0 | True | None | 0 | 0
317	humaid | qwen3 | few-shot-5 | collider | 0.0 | 0.0 | 0.0 | 0.0 | True | None | 0 | 0
318	humaid | qwen3 | few-shot-5 | exposure | 0.0 | 0.0 | 0.0 | 0.0 | True | None | 0 | 0
319	humaid | qwen3 | few-shot-5 | mbias | 0.0 | 0.0 | 0.0 | 0.0 | True | None | 0 | 0
320	humaid | qwen3 | few-shot-5 | iv | 0.0 | 0.0 | 0.0 | 0.0 | True | None | 0 | 0
321	humaid | qwen3 | few-shot-5 | frontdoor | 0.0 | 0.0 | 0.0 | 0.0 | True | None | 0 | 0
322	humaid | deepseek | zero-shot | confounding | 1.0 | 1.0 | 1.0 | 1.0 | True | None | 1000 | 1000
323	humaid | deepseek | zero-shot | mediation | 0.429 | 0.0 | 1.0 | 0.0 | False | 0.894985545919502 | 1000 | 1000
324	humaid | deepseek | zero-shot | collider | 0.143 | 0.143 | 1.0 | 1.0 | True | None | 1000 | 1000
325	humaid | deepseek | zero-shot | exposure | 0.046 | 0.0 | 1.0 | 0.0 | False | 0.9375138981543252 | 1000 | 1000
326	humaid | deepseek | zero-shot | mbias | 0.746 | 0.746 | 1.0 | 1.0 | True | None | 1000 | 1000
327	humaid | deepseek | zero-shot | iv | 0.037 | 0.0 | 0.785 | 0.0 | False | 0.7579497442739604 | 1000 | 1000
328	humaid | deepseek | zero-shot | frontdoor | 0.049 | 0.0 | 1.0 | 0.0 | False | 0.9119968868134313 | 1000 | 1000
329	humaid | deepseek | few-shot-3 | confounding | 1.0 | 1.0 | 1.0 | 1.0 | True | None | 1000 | 1000
330	humaid | deepseek | few-shot-3 | mediation | 0.642 | 0.0 | 1.0 | 0.0 | False | 0.6496893620690438 | 1000 | 1000
331	humaid | deepseek | few-shot-3 | collider | 0.217 | 0.217 | 1.0 | 1.0 | True | None | 1000 | 1000
332	humaid | deepseek | few-shot-3 | exposure | 0.04 | 0.0 | 1.0 | 0.0 | False | 0.6496893620690438 | 1000 | 1000
333	humaid | deepseek | few-shot-3 | mbias | 0.611 | 0.611 | 1.0 | 1.0 | True | None | 1000 | 1000
334	humaid | deepseek | few-shot-3 | iv | 0.037 | 0.0 | 0.776 | 0.0 | False | 0.3102022663635167 | 1000 | 1000
335	humaid | deepseek | few-shot-3 | frontdoor | 0.05 | 0.0 | 1.0 | 0.0 | False | 0.6496893620690438 | 1000 | 1000
336	humaid | deepseek | few-shot-5 | confounding | 1.0 | 1.0 | 1.0 | 1.0 | True | None | 1000 | 1000
337	humaid | deepseek | few-shot-5 | mediation | 0.531 | 0.0 | 1.0 | 0.0 | False | 0.7752759747374162 | 1000 | 1000
338	humaid | deepseek | few-shot-5 | collider | 0.139 | 0.139 | 1.0 | 1.0 | True | None | 1000 | 1000
339	humaid | deepseek | few-shot-5 | exposure | 0.053 | 0.0 | 1.0 | 0.0 | False | 0.693162838485998 | 1000 | 1000
340	humaid | deepseek | few-shot-5 | mbias | 0.682 | 0.682 | 1.0 | 1.0 | True | None | 1000 | 1000
341	humaid | deepseek | few-shot-5 | iv | 0.044 | 0.0 | 0.761 | 0.0 | False | 0.3881711895521589 | 1000 | 1000
342	humaid | deepseek | few-shot-5 | frontdoor | 0.05 | 0.0 | 1.0 | 0.0 | False | 0.7560806961331886 | 1000 | 1000
343	
344	## Table 5: Summary Statistics
345	f1_gt_093_total: 0
346	f1_gt_093_with_high_bias_pct: 0.0
347	ppi_recommended_scenarios: 31
348	total_scenarios: 63
349	ppi_recommended_pct: 49.2063492063492
350	
351	## Table 6: Per-Topology ASV-Unsafe Count
352	topology | n_unsafe | n_total | pct_unsafe
353	--- | --- | --- | ---
354	collider | 0 | 9 | 0.0
355	confounding | 0 | 9 | 0.0
356	exposure | 7 | 9 | 77.77777777777779
357	frontdoor | 8 | 9 | 88.88888888888889
358	iv | 8 | 9 | 88.88888888888889
359	mbias | 0 | 9 | 0.0
360	mediation | 8 | 9 | 88.88888888888889
361	
362	## Table 7: Inter-Model Correlation
363	scenario | pair | agreement | kappa | error_correlation
364	--- | --- | --- | --- | ---
365	civil_comments_zero-shot | llama4-qwen3 | 1.0 | 1.0 | 0.0
366	civil_comments_zero-shot | llama4-deepseek | 1.0 | 1.0 | 0.0
367	civil_comments_zero-shot | qwen3-deepseek | 1.0 | 1.0 | 0.0
368	civil_comments_few-shot-3 | llama4-qwen3 | 1.0 | 1.0 | 0.0
369	civil_comments_few-shot-3 | llama4-deepseek | 1.0 | 1.0 | 0.0
370	civil_comments_few-shot-3 | qwen3-deepseek | 1.0 | 1.0 | 0.0
371	civil_comments_few-shot-5 | llama4-qwen3 | 1.0 | 1.0 | 0.0
372	civil_comments_few-shot-5 | llama4-deepseek | 1.0 | 1.0 | 0.0
373	civil_comments_few-shot-5 | qwen3-deepseek | 1.0 | 1.0 | 0.0
374	vast_zero-shot | llama4-qwen3 | 1.0 | 1.0 | 0.0
375	vast_zero-shot | llama4-deepseek | 1.0 | 1.0 | 0.0
376	vast_zero-shot | qwen3-deepseek | 1.0 | 1.0 | 0.0
377	vast_few-shot-3 | llama4-qwen3 | 1.0 | 1.0 | 0.0
378	vast_few-shot-3 | llama4-deepseek | 1.0 | 1.0 | 0.0
379	vast_few-shot-3 | qwen3-deepseek | 1.0 | 1.0 | 0.0
380	vast_few-shot-5 | llama4-qwen3 | 1.0 | 1.0 | 0.0
381	vast_few-shot-5 | llama4-deepseek | 1.0 | 1.0 | 0.0
382	vast_few-shot-5 | qwen3-deepseek | 1.0 | 1.0 | 0.0
383	humaid_zero-shot | llama4-qwen3 | 0.485 | 0.4167114987116686 | 0.12098407875327466
384	humaid_zero-shot | llama4-deepseek | 0.485 | 0.4186368105625225 | 0.07373028718567304
385	humaid_zero-shot | qwen3-deepseek | 0.559 | 0.4908691245027027 | 0.0846329327487544
386	humaid_few-shot-3 | llama4-qwen3 | 0.49 | 0.4198341635771887 | 0.15698798664647698
387	humaid_few-shot-3 | llama4-deepseek | 0.465 | 0.39244588793749574 | 0.056343776031514164
388	humaid_few-shot-3 | qwen3-deepseek | 0.507 | 0.43272171605708226 | 0.0505073995012017
389	humaid_few-shot-5 | llama4-qwen3 | 0.08 | 0.0 | 0.05719859338218029
390	humaid_few-shot-5 | llama4-deepseek | 0.495 | 0.42885126721504485 | 0.10671907241319777
391	humaid_few-shot-5 | qwen3-deepseek | 0.04 | 0.0 | -0.0018170903900012014
392	
393	## Table 8: Confusion Matrices
394	
395	### humaid_llama4_zero-shot
396	Shape: 10x10
397	  row_0: [0.42592592592592593, 0.05555555555555555, 0.011904761904761904, 0.0, 0.0, 0.009708737864077669, 0.04044117647058824, 0.0, 0.002577319587628866, 0.010810810810810811]
398	  row_1: [0.0, 0.7222222222222222, 0.017857142857142856, 0.02962962962962963, 0.0, 0.02912621359223301, 0.04411764705882353, 0.017543859649122806, 0.01288659793814433, 0.005405405405405406]
399	  row_2: [0.12037037037037036, 0.0, 0.5892857142857143, 0.007407407407407408, 0.0, 0.02912621359223301, 0.12867647058823528, 0.0, 0.002577319587628866, 0.0]
400	  row_3: [0.0, 0.0, 0.017857142857142856, 0.8592592592592593, 0.0, 0.019417475728155338, 0.011029411764705883, 0.0, 0.002577319587628866, 0.010810810810810811]
401	  row_4: [0.0, 0.0, 0.005952380952380952, 0.007407407407407408, 1.0, 0.0, 0.011029411764705883, 0.0, 0.002577319587628866, 0.0]
402	  row_5: [0.018518518518518517, 0.013888888888888888, 0.0, 0.0, 0.0, 0.42718446601941745, 0.07720588235294118, 0.0, 0.002577319587628866, 0.0]
403	  row_6: [0.37037037037037035, 0.06944444444444445, 0.21428571428571427, 0.0, 0.0, 0.13592233009708737, 0.44485294117647056, 0.017543859649122806, 0.06701030927835051, 0.06486486486486487]
404	  row_7: [0.009259259259259259, 0.06944444444444445, 0.023809523809523808, 0.0, 0.0, 0.04854368932038835, 0.05514705882352941, 0.6491228070175439, 0.03350515463917526, 0.016216216216216217]
405	  row_8: [0.027777777777777776, 0.06944444444444445, 0.011904761904761904, 0.02962962962962963, 0.0, 0.019417475728155338, 0.05514705882352941, 0.24561403508771928, 0.8170103092783505, 0.11891891891891893]
406	  row_9: [0.027777777777777776, 0.0, 0.10714285714285714, 0.06666666666666667, 0.0, 0.2815533980582524, 0.1323529411764706, 0.07017543859649122, 0.05670103092783505, 0.772972972972973]
407	
408	### humaid_llama4_few-shot-3
409	Shape: 10x10
410	  row_0: [0.4074074074074074, 0.05555555555555555, 0.0, 0.0, 0.0, 0.0, 0.025735294117647058, 0.0, 0.0, 0.010810810810810811]
411	  row_1: [0.0, 0.7222222222222222, 0.017964071856287425, 0.022222222222222223, 0.0, 0.02912621359223301, 0.04779411764705882, 0.017543859649122806, 0.00516795865633075, 0.0]
412	  row_2: [0.10185185185185185, 0.0, 0.5568862275449101, 0.0, 0.0, 0.019417475728155338, 0.09926470588235294, 0.0, 0.0, 0.0]
413	  row_3: [0.0, 0.013888888888888888, 0.023952095808383235, 0.8592592592592593, 0.0, 0.019417475728155338, 0.011029411764705883, 0.0, 0.00516795865633075, 0.021621621621621623]
414	  row_4: [0.0, 0.0, 0.005988023952095809, 0.014814814814814815, 1.0, 0.0, 0.011029411764705883, 0.0, 0.002583979328165375, 0.0]
415	  row_5: [0.018518518518518517, 0.013888888888888888, 0.011976047904191617, 0.007407407407407408, 0.0, 0.5048543689320388, 0.13602941176470587, 0.017543859649122806, 0.002583979328165375, 0.010810810810810811]
416	  row_6: [0.4074074074074074, 0.041666666666666664, 0.23952095808383234, 0.007407407407407408, 0.0, 0.13592233009708737, 0.4522058823529412, 0.017543859649122806, 0.05426356589147287, 0.043243243243243246]
417	  row_7: [0.009259259259259259, 0.05555555555555555, 0.029940119760479042, 0.0, 0.0, 0.02912621359223301, 0.051470588235294115, 0.631578947368421, 0.03875968992248062, 0.010810810810810811]
418	  row_8: [0.037037037037037035, 0.09722222222222222, 0.017964071856287425, 0.02962962962962963, 0.0, 0.019417475728155338, 0.0661764705882353, 0.24561403508771928, 0.8397932816537468, 0.11891891891891893]
419	  row_9: [0.018518518518518517, 0.0, 0.09580838323353294, 0.05925925925925926, 0.0, 0.24271844660194175, 0.09926470588235294, 0.07017543859649122, 0.05167958656330749, 0.7837837837837838]
420	
421	### humaid_llama4_few-shot-5
422	Shape: 10x10
423	  row_0: [0.41509433962264153, 0.05714285714285714, 0.0, 0.0, 0.0, 0.0, 0.0299625468164794, 0.0, 0.0, 0.01092896174863388]
424	  row_1: [0.0, 0.7142857142857143, 0.018072289156626505, 0.015037593984962405, 0.0, 0.029411764705882353, 0.04868913857677903, 0.01818181818181818, 0.005305039787798408, 0.00546448087431694]
425	  row_2: [0.09433962264150944, 0.0, 0.4879518072289157, 0.0, 0.0, 0.00980392156862745, 0.07865168539325842, 0.0, 0.0, 0.0]
426	  row_3: [0.0, 0.014285714285714285, 0.024096385542168676, 0.8721804511278195, 0.0, 0.0196078431372549, 0.00749063670411985, 0.0, 0.002652519893899204, 0.01639344262295082]
427	  row_4: [0.0, 0.0, 0.012048192771084338, 0.015037593984962405, 1.0, 0.0, 0.00749063670411985, 0.0, 0.0, 0.0]
428	  row_5: [0.018867924528301886, 0.014285714285714285, 0.012048192771084338, 0.007518796992481203, 0.0, 0.5784313725490197, 0.16853932584269662, 0.0, 0.002652519893899204, 0.01639344262295082]
429	  row_6: [0.39622641509433965, 0.04285714285714286, 0.28313253012048195, 0.015037593984962405, 0.0, 0.14705882352941177, 0.46441947565543074, 0.01818181818181818, 0.04774535809018567, 0.03825136612021858]
430	  row_7: [0.009433962264150943, 0.05714285714285714, 0.03614457831325301, 0.0, 0.0, 0.0196078431372549, 0.06367041198501873, 0.7090909090909091, 0.03713527851458886, 0.01092896174863388]
431	  row_8: [0.04716981132075472, 0.1, 0.024096385542168676, 0.022556390977443608, 0.0, 0.00980392156862745, 0.07116104868913857, 0.2, 0.8594164456233422, 0.12568306010928962]
432	  row_9: [0.018867924528301886, 0.0, 0.10240963855421686, 0.05263157894736842, 0.0, 0.18627450980392157, 0.0599250936329588, 0.05454545454545454, 0.04509283819628647, 0.7759562841530054]
433	
434	### humaid_qwen3_zero-shot
435	Shape: 10x10
436	  row_0: [0.5833333333333334, 0.041666666666666664, 0.023809523809523808, 0.0, 0.0, 0.04854368932038835, 0.14338235294117646, 0.0, 0.007731958762886598, 0.06486486486486487]
437	  row_1: [0.009259259259259259, 0.8888888888888888, 0.011904761904761904, 0.014814814814814815, 0.0, 0.05825242718446602, 0.051470588235294115, 0.017543859649122806, 0.020618556701030927, 0.010810810810810811]
438	  row_2: [0.1388888888888889, 0.0, 0.7857142857142857, 0.0, 0.0, 0.0970873786407767, 0.1801470588235294, 0.0, 0.007731958762886598, 0.005405405405405406]
439	  row_3: [0.009259259259259259, 0.027777777777777776, 0.05357142857142857, 0.9703703703703703, 0.0, 0.07766990291262135, 0.03308823529411765, 0.0, 0.005154639175257732, 0.03783783783783784]
440	  row_4: [0.0, 0.0, 0.005952380952380952, 0.0, 1.0, 0.0, 0.003676470588235294, 0.0, 0.002577319587628866, 0.005405405405405406]
441	  row_5: [0.0, 0.0, 0.005952380952380952, 0.0, 0.0, 0.33980582524271846, 0.07352941176470588, 0.017543859649122806, 0.002577319587628866, 0.021621621621621623]
442	  row_6: [0.2037037037037037, 0.0, 0.06547619047619048, 0.0, 0.0, 0.2524271844660194, 0.3492647058823529, 0.0, 0.023195876288659795, 0.02702702702702703]
443	  row_7: [0.027777777777777776, 0.013888888888888888, 0.011904761904761904, 0.007407407407407408, 0.0, 0.06796116504854369, 0.051470588235294115, 0.7368421052631579, 0.08247422680412371, 0.032432432432432434]
444	  row_8: [0.018518518518518517, 0.027777777777777776, 0.023809523809523808, 0.0, 0.0, 0.038834951456310676, 0.09926470588235294, 0.21052631578947367, 0.8402061855670103, 0.14054054054054055]
445	  row_9: [0.009259259259259259, 0.0, 0.011904761904761904, 0.007407407407407408, 0.0, 0.019417475728155338, 0.014705882352941176, 0.017543859649122806, 0.007731958762886598, 0.654054054054054]
446	
447	### humaid_qwen3_few-shot-3
448	Shape: 10x10
449	  row_0: [0.5876288659793815, 0.0, 0.03636363636363636, 0.0, 0.0, 0.031914893617021274, 0.12595419847328243, 0.0, 0.010416666666666666, 0.03164556962025317]
450	  row_1: [0.010309278350515464, 0.8307692307692308, 0.024242424242424242, 0.030534351145038167, 0.0, 0.05319148936170213, 0.0648854961832061, 0.03636363636363636, 0.0234375, 0.012658227848101266]
451	  row_2: [0.10309278350515463, 0.015384615384615385, 0.6727272727272727, 0.0, 0.0, 0.05319148936170213, 0.10687022900763359, 0.0, 0.0078125, 0.012658227848101266]
452	  row_3: [0.010309278350515464, 0.015384615384615385, 0.04242424242424243, 0.9618320610687023, 0.0, 0.0425531914893617, 0.03435114503816794, 0.0, 0.0078125, 0.03164556962025317]
453	  row_4: [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.003816793893129771, 0.0, 0.0, 0.006329113924050633]
454	  row_5: [0.020618556701030927, 0.0, 0.006060606060606061, 0.0, 0.0, 0.425531914893617, 0.08778625954198473, 0.0, 0.0026041666666666665, 0.02531645569620253]
455	  row_6: [0.23711340206185566, 0.046153846153846156, 0.14545454545454545, 0.0, 0.0, 0.2978723404255319, 0.3931297709923664, 0.01818181818181818, 0.036458333333333336, 0.0189873417721519]
456	  row_7: [0.0, 0.046153846153846156, 0.01818181818181818, 0.0, 0.0, 0.05319148936170213, 0.04198473282442748, 0.6909090909090909, 0.06770833333333333, 0.04430379746835443]
457	  row_8: [0.030927835051546393, 0.046153846153846156, 0.024242424242424242, 0.0, 0.0, 0.031914893617021274, 0.11450381679389313, 0.2545454545454545, 0.8359375, 0.1518987341772152]
458	  row_9: [0.0, 0.0, 0.030303030303030304, 0.007633587786259542, 0.0, 0.010638297872340425, 0.026717557251908396, 0.0, 0.0078125, 0.6645569620253164]
459	
460	### humaid_qwen3_few-shot-5
461	Shape: 10x10
462	  row_0: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
463	  row_1: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
464	  row_2: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
465	  row_3: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
466	  row_4: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
467	  row_5: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
468	  row_6: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
469	  row_7: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
470	  row_8: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
471	  row_9: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
472	
473	### humaid_deepseek_zero-shot
474	Shape: 10x10
475	  row_0: [0.6111111111111112, 0.041666666666666664, 0.023809523809523808, 0.007407407407407408, 0.0, 0.019417475728155338, 0.1323529411764706, 0.017543859649122806, 0.010309278350515464, 0.07567567567567568]
476	  row_1: [0.018518518518518517, 0.8611111111111112, 0.0, 0.022222222222222223, 0.0, 0.04854368932038835, 0.04044117647058824, 0.05263157894736842, 0.020618556701030927, 0.005405405405405406]
477	  row_2: [0.14814814814814814, 0.0, 0.7857142857142857, 0.0, 0.0, 0.05825242718446602, 0.20588235294117646, 0.0, 0.010309278350515464, 0.005405405405405406]
478	  row_3: [0.009259259259259259, 0.013888888888888888, 0.011904761904761904, 0.9333333333333333, 0.0, 0.02912621359223301, 0.01838235294117647, 0.0, 0.010309278350515464, 0.016216216216216217]
479	  row_4: [0.0, 0.0, 0.005952380952380952, 0.0, 1.0, 0.0, 0.003676470588235294, 0.017543859649122806, 0.002577319587628866, 0.005405405405405406]
480	  row_5: [0.05555555555555555, 0.013888888888888888, 0.017857142857142856, 0.007407407407407408, 0.0, 0.6990291262135923, 0.20220588235294118, 0.03508771929824561, 0.02577319587628866, 0.043243243243243246]
481	  row_6: [0.1388888888888889, 0.013888888888888888, 0.09523809523809523, 0.007407407407407408, 0.0, 0.06796116504854369, 0.29411764705882354, 0.017543859649122806, 0.059278350515463915, 0.03783783783783784]
482	  row_7: [0.0, 0.013888888888888888, 0.005952380952380952, 0.0, 0.0, 0.019417475728155338, 0.03308823529411765, 0.5789473684210527, 0.020618556701030927, 0.021621621621621623]
483	  row_8: [0.018518518518518517, 0.041666666666666664, 0.011904761904761904, 0.0, 0.0, 0.019417475728155338, 0.04411764705882353, 0.22807017543859648, 0.7809278350515464, 0.0972972972972973]
484	  row_9: [0.0, 0.0, 0.041666666666666664, 0.022222222222222223, 0.0, 0.038834951456310676, 0.025735294117647058, 0.05263157894736842, 0.059278350515463915, 0.6918918918918919]
485	
486	### humaid_deepseek_few-shot-3
487	Shape: 10x10
488	  row_0: [0.5795454545454546, 0.15, 0.050955414012738856, 0.0, 0.0, 0.011363636363636364, 0.1297071129707113, 0.0, 0.008287292817679558, 0.043478260869565216]
489	  row_1: [0.0, 0.7, 0.03184713375796178, 0.024, 0.0, 0.056818181818181816, 0.03347280334728033, 0.018867924528301886, 0.008287292817679558, 0.006211180124223602]
490	  row_2: [0.07954545454545454, 0.0, 0.6178343949044586, 0.0, 0.0, 0.03409090909090909, 0.12552301255230125, 0.0, 0.0027624309392265192, 0.0]
491	  row_3: [0.011363636363636364, 0.016666666666666666, 0.025477707006369428, 0.936, 0.0, 0.045454545454545456, 0.012552301255230125, 0.0, 0.008287292817679558, 0.012422360248447204]
492	  row_4: [0.0, 0.0, 0.006369426751592357, 0.008, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
493	  row_5: [0.056818181818181816, 0.03333333333333333, 0.03821656050955414, 0.016, 0.0, 0.7159090909090909, 0.20502092050209206, 0.018867924528301886, 0.016574585635359115, 0.043478260869565216]
494	  row_6: [0.25, 0.016666666666666666, 0.15286624203821655, 0.0, 0.0, 0.06818181818181818, 0.38493723849372385, 0.018867924528301886, 0.06077348066298342, 0.031055900621118012]
495	  row_7: [0.0, 0.0, 0.012738853503184714, 0.0, 0.0, 0.045454545454545456, 0.016736401673640166, 0.7547169811320755, 0.022099447513812154, 0.012422360248447204]
496	  row_8: [0.022727272727272728, 0.08333333333333333, 0.01910828025477707, 0.0, 0.0, 0.0, 0.058577405857740586, 0.16981132075471697, 0.8314917127071824, 0.12422360248447205]
497	  row_9: [0.0, 0.0, 0.044585987261146494, 0.016, 0.0, 0.022727272727272728, 0.03347280334728033, 0.018867924528301886, 0.04143646408839779, 0.7267080745341615]
498	
499	### humaid_deepseek_few-shot-5
500	Shape: 10x10
501	  row_0: [0.5757575757575758, 0.15254237288135594, 0.03875968992248062, 0.0, 0.0, 0.0, 0.1324200913242009, 0.0, 0.006269592476489028, 0.05063291139240506]
502	  row_1: [0.0, 0.7627118644067796, 0.023255813953488372, 0.01818181818181818, 0.0, 0.04395604395604396, 0.0319634703196347, 0.024390243902439025, 0.012539184952978056, 0.0]
503	  row_2: [0.0707070707070707, 0.0, 0.6201550387596899, 0.0, 0.0, 0.02197802197802198, 0.1095890410958904, 0.0, 0.006269592476489028, 0.0]
504	  row_3: [0.010101010101010102, 0.01694915254237288, 0.031007751937984496, 0.9363636363636364, 0.0, 0.03296703296703297, 0.0273972602739726, 0.0, 0.009404388714733543, 0.0189873417721519]
505	  row_4: [0.0, 0.0, 0.0, 0.00909090909090909, 1.0, 0.0, 0.0, 0.0, 0.003134796238244514, 0.006329113924050633]
506	  row_5: [0.050505050505050504, 0.01694915254237288, 0.046511627906976744, 0.00909090909090909, 0.0, 0.8021978021978022, 0.2146118721461187, 0.0, 0.01567398119122257, 0.04430379746835443]
507	  row_6: [0.25252525252525254, 0.0, 0.17829457364341086, 0.0, 0.0, 0.054945054945054944, 0.3744292237442922, 0.024390243902439025, 0.06269592476489028, 0.05063291139240506]
508	  row_7: [0.0, 0.01694915254237288, 0.007751937984496124, 0.00909090909090909, 0.0, 0.01098901098901099, 0.0273972602739726, 0.6341463414634146, 0.034482758620689655, 0.012658227848101266]
509	  row_8: [0.030303030303030304, 0.03389830508474576, 0.023255813953488372, 0.0, 0.0, 0.01098901098901099, 0.0593607305936073, 0.2682926829268293, 0.8119122257053292, 0.0949367088607595]
510	  row_9: [0.010101010101010102, 0.0, 0.031007751937984496, 0.01818181818181818, 0.0, 0.02197802197802198, 0.0228310502283105, 0.04878048780487805, 0.03761755485893417, 0.7215189873417721]
511	
512	## Table 9: Overall ASV-Unsafe Summary
513	Total valid scenarios: 63
514	Total ASV-unsafe: 31
515	ASV-unsafe percentage: 49.2063492063492
516	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "638b3122-3dcd-438e-a3ce-e9649734910a",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "1d2d8c5a-c485-4dd6-97f7-cfdf4d28f795",
  "sourceToolAssistantUUID": "638b3122-3dcd-438e-a3ce-e9649734910a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-25T20:20:06.926Z_

Now let me search more directly for the 14/23 sign reversal claim and read the sign_reversal_determinants_results.json file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d2d8c5a-c485-4dd6-97f7-cfdf4d28f795",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPua6QVWroB7fAFpvbZc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0c381e75-06ec-4a52-ae49-f892597738c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017stxrHDeL63AJVTzCRceGE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 24081,
      "cache_read_input_tokens": 82775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24081,
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

_source line 30 · 2026-05-25T20:20:08.257Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LdzCRQ7hh39fcWHe1ZuRTa`</summary>

```json
{
  "pattern": "14.*23|23.*14",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/sign_reversal_determinants_results.json",
  "output_mode": "content",
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c381e75-06ec-4a52-ae49-f892597738c6",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPua6QVWroB7fAFpvbZc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ab6216a9-5362-4e96-aa76-6834b26e6706",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017stxrHDeL63AJVTzCRceGE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 24081,
      "cache_read_input_tokens": 82775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24081,
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

_source line 31 · 2026-05-25T20:20:08.273Z_

<details><summary>↩ Tool result · `toolu_01LdzCRQ7hh39fcWHe1ZuRTa`</summary>

```text
306:      "min_sv": 0.022236067447757614,
332:      "mean_entropy": 0.7843608143445023,
685:              "true": -0.1476792358653642,
776:              "true": -0.1476792358653642,
867:              "true": -0.1476792358653642,
953:              "biased": 0.3239713031421688,
958:              "true": -0.1476792358653642,
1049:              "true": -0.1476792358653642,
1140:              "true": -0.1476792358653642,
1141:              "biased": 0.13162472969238814,
1231:              "true": -0.1476792358653642,
1322:              "true": -0.1476792358653642,
1513:            "min_sv": 0.022236067447757614,
1593:            "mean_entropy": 0.7843608143445023,
2001:              "true": 1.0023207641346414,
2008:              "biased": 0.8311059011472307,
2092:              "true": 1.0023207641346414,
2183:              "true": 1.0023207641346414,
2274:              "true": 1.0023207641346414,
2365:              "true": 1.0023207641346414,
2456:              "true": 1.0023207641346414,
2547:              "true": 1.0023207641346414,
2638:              "true": 1.0023207641346414,
2829:            "min_sv": 0.022236067447757614,
2885:          "tau_hat": 0.37895072281478237,
2891:              "biased": 0.37895072281478237,
2909:            "mean_entropy": 0.7843608143445023,
3306:              "biased": -0.28929818714004923,
3482:              "biased": 0.41411828525423844,
4145:            "min_sv": 0.022236067447757614,
4225:            "mean_entropy": 0.7843608143445023,
5319:              "biased": 0.13414177524123927,
5461:            "min_sv": 0.022236067447757614,
5541:            "mean_entropy": 0.7843608143445023,
6777:            "min_sv": 0.022236067447757614,
6834:          "max_relbias": 1.3482339314047467,
6857:            "mean_entropy": 0.7843608143445023,
8035:              "biased": 0.14831023504590815,
8093:            "min_sv": 0.022236067447757614,
8173:            "mean_entropy": 0.7843608143445023,
8386:        "min_no_flip": 0.022236067447757614,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab6216a9-5362-4e96-aa76-6834b26e6706",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "ee25a27f-b4dd-4525-a452-708883383540",
  "sourceToolAssistantUUID": "ab6216a9-5362-4e96-aa76-6834b26e6706",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T20:20:09.460Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NyQwB1bUoguoSXtxwudrin`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/sign_reversal_determinants_results.json",
  "offset": 1,
  "limit": 2000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee25a27f-b4dd-4525-a452-708883383540",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPua6QVWroB7fAFpvbZc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "473169c0-38f4-481d-b8a3-61ce2e73b0b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017stxrHDeL63AJVTzCRceGE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 24081,
      "cache_read_input_tokens": 82775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24081,
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

_source line 33 · 2026-05-25T20:20:09.775Z_

<details><summary>↩ Tool result · `toolu_01NyQwB1bUoguoSXtxwudrin`</summary>

```text
1	{
2	  "n_matrices": 23,
3	  "beta_configs_tested": [
4	    "default",
5	    "uniform_pos",
6	    "alt_signs",
7	    "only_first",
8	    "scale_0p3",
9	    "scale_3p0"
10	  ],
11	  "feature_names": [
12	    "min_diag",
13	    "mean_diag",
14	    "max_off",
15	    "max_off_ratio",
16	    "log_cond",
17	    "mean_entropy",
18	    "max_entropy",
19	    "spectral_gap",
20	    "det",
21	    "min_sv"
22	  ],
23	  "features_per_config": {
24	    "civil_comments_deepseek_few-shot-5": {
25	      "K": 2,
26	      "min_diag": 0.7341211225997046,
27	      "mean_diag": 0.7677454928067016,
28	      "max_off": 0.2658788774002954,
29	      "max_off_ratio": 0.36217303822937624,
30	      "cond": 1.8792558531832826,
31	      "log_cond": 0.2739859115860814,
32	      "mean_entropy": 0.7773343104187012,
33	      "max_entropy": 0.8354887266831242,
34	      "spectral_gap": 0.46450901438659675,
35	      "det": 0.5354909856134032,
36	      "min_sv": 0.5338056010567983,
37	      "sv_ratio": 1.8792558531832826
38	    },
39	    "civil_comments_qwen2.5-7b_few-shot-3": {
40	      "K": 2,
41	      "min_diag": 0.6787296898079763,
42	      "mean_diag": 0.7297758038080977,
43	      "max_off": 0.3212703101920236,
44	      "max_off_ratio": 0.4733405875952122,
45	      "cond": 2.2046870875055347,
46	      "log_cond": 0.34334695851446095,
47	      "mean_entropy": 0.832210695039356,
48	      "max_entropy": 0.9057575271903423,
49	      "spectral_gap": 0.5404483923838045,
50	      "det": 0.45955160761619557,
51	      "min_sv": 0.45655559105857724,
52	      "sv_ratio": 2.2046870875055347
53	    },
54	    "civil_comments_qwen2.5-7b_few-shot-5": {
55	      "K": 2,
56	      "min_diag": 0.7370753323485968,
57	      "mean_diag": 0.7486746524756682,
58	      "max_off": 0.26292466765140327,
59	      "max_off_ratio": 0.35671342685370744,
60	      "cond": 2.0120966711779484,
61	      "log_cond": 0.30364884256210606,
62	      "mean_entropy": 0.8128560597271433,
63	      "max_entropy": 0.8311277438478006,
64	      "spectral_gap": 0.5026506950486636,
65	      "det": 0.4973493049513366,
66	      "min_sv": 0.49717162744867915,
67	      "sv_ratio": 2.0120966711779484
68	    },
69	    "civil_comments_qwen2.5-7b_zero-shot": {
70	      "K": 2,
71	      "min_diag": 0.684931506849315,
72	      "mean_diag": 0.7165425628781288,
73	      "max_off": 0.3150684931506849,
74	      "max_off_ratio": 0.46,
75	      "cond": 2.320361980143194,
76	      "log_cond": 0.3655557408029338,
77	      "mean_entropy": 0.8565646301807837,
78	      "max_entropy": 0.8989377852081333,
79	      "spectral_gap": 0.5669148742437425,
80	      "det": 0.43308512575625746,
81	      "min_sv": 0.4320248854336829,
82	      "sv_ratio": 2.320361980143194
83	    },
84	    "civil_comments_qwen3_few-shot-3": {
85	      "K": 2,
86	      "min_diag": 0.7448275862068966,
87	      "mean_diag": 0.7813701217488962,
88	      "max_off": 0.25517241379310346,
89	      "max_off_ratio": 0.34259259259259256,
90	      "cond": 1.790859904151061,
91	      "log_cond": 0.25306161307745983,
92	      "mean_entropy": 0.7519979451235315,
93	      "max_entropy": 0.8193737468292397,
94	      "spectral_gap": 0.43725975650220783,
95	      "det": 0.5627402434977923,
96	      "min_sv": 0.5605613889083931,
97	      "sv_ratio": 1.790859904151061
98	    },
99	    "civil_comments_qwen3_few-shot-5": {
100	      "K": 2,
101	      "min_diag": 0.7931034482758621,
102	      "mean_diag": 0.8085784501958375,
103	      "max_off": 0.20689655172413793,
104	      "max_off_ratio": 0.2608695652173913,
105	      "cond": 1.6228381125800326,
106	      "log_cond": 0.21027519861870325,
107	      "mean_entropy": 0.7033187055895573,
108	      "max_entropy": 0.7355085815538399,
109	      "spectral_gap": 0.3828430996083251,
110	      "det": 0.617156900391675,
111	      "min_sv": 0.6166804707799527,
112	      "sv_ratio": 1.6228381125800326
113	    },
114	    "civil_comments_qwen3_zero-shot": {
115	      "K": 2,
116	      "min_diag": 0.7425742574257426,
117	      "mean_diag": 0.7603464334163478,
118	      "max_off": 0.25742574257425743,
119	      "max_off_ratio": 0.3466666666666667,
120	      "cond": 1.923844741767405,
121	      "log_cond": 0.28417002065689095,
122	      "mean_entropy": 0.7932124509685978,
123	      "max_entropy": 0.8228368841492258,
124	      "spectral_gap": 0.47930713316730444,
125	      "det": 0.5206928668326956,
126	      "min_sv": 0.5202424709655475,
127	      "sv_ratio": 1.923844741767405
128	    },
129	    "humaid_deepseek_few-shot-3": {
130	      "K": 10,
131	      "min_diag": 0.38493723849372385,
132	      "mean_diag": 0.7247142947226147,
133	      "max_off": 0.25,
134	      "max_off_ratio": 0.532608695652174,
135	      "cond": 4.409507323985138,
136	      "log_cond": 0.6443900682824745,
137	      "mean_entropy": 0.4023974734197873,
138	      "max_entropy": 0.7534239502970503,
139	      "spectral_gap": 0.002150042096596194,
140	      "det": 0.021332189334821124,
141	      "min_sv": 0.23091827608687163,
142	      "sv_ratio": 4.409507323985138
143	    },
144	    "humaid_deepseek_few-shot-5": {
145	      "K": 10,
146	      "min_diag": 0.3744292237442922,
147	      "mean_diag": 0.7239192695740293,
148	      "max_off": 0.2682926829268293,
149	      "max_off_ratio": 0.573170731707317,
150	      "cond": 4.638454996807901,
151	      "log_cond": 0.6663733473444414,
152	      "mean_entropy": 0.3967710539627384,
153	      "max_entropy": 0.7683639237792222,
154	      "spectral_gap": 0.0032537141891824106,
155	      "det": 0.020280304489390028,
156	      "min_sv": 0.2206751028987421,
157	      "sv_ratio": 4.638454996807901
158	    },
159	    "humaid_deepseek_zero-shot": {
160	      "K": 10,
161	      "min_diag": 0.29411764705882354,
162	      "mean_diag": 0.7236183709906748,
163	      "max_off": 0.22807017543859648,
164	      "max_off_ratio": 0.7,
165	      "cond": 5.109683690040082,
166	      "log_cond": 0.7083940163926374,
167	      "mean_entropy": 0.41300072961171885,
168	      "max_entropy": 0.8011248606608374,
169	      "spectral_gap": 0.002559866244257969,
170	      "det": 0.018291677753051495,
171	      "min_sv": 0.19952987155984303,
172	      "sv_ratio": 5.109683690040082
173	    },
174	    "humaid_llama4_few-shot-3": {
175	      "K": 10,
176	      "min_diag": 0.4074074074074074,
177	      "mean_diag": 0.675799138052473,
178	      "max_off": 0.4074074074074074,
179	      "max_off_ratio": 1.0,
180	      "cond": 5.138340099658911,
181	      "log_cond": 0.7108228462356819,
182	      "mean_entropy": 0.4307113519912539,
183	      "max_entropy": 0.764437246894965,
184	      "spectral_gap": 0.003339175071885747,
185	      "det": 0.009915635381985513,
186	      "min_sv": 0.20950042424565504,
187	      "sv_ratio": 5.138340099658911
188	    },
189	    "humaid_llama4_few-shot-5": {
190	      "K": 10,
191	      "min_diag": 0.41509433962264153,
192	      "mean_diag": 0.6876826799336799,
193	      "max_off": 0.39622641509433965,
194	      "max_off_ratio": 0.9545454545454546,
195	      "cond": 5.153050727272362,
196	      "log_cond": 0.7120644177310209,
197	      "mean_entropy": 0.41852478500884976,
198	      "max_entropy": 0.7443560908326295,
199	      "spectral_gap": 0.0017801324917138261,
200	      "det": 0.01172179530195112,
201	      "min_sv": 0.20767898111002162,
202	      "sv_ratio": 5.153050727272362
203	    },
204	    "humaid_llama4_zero-shot": {
205	      "K": 10,
206	      "min_diag": 0.42592592592592593,
207	      "mean_diag": 0.6707836618157876,
208	      "max_off": 0.37037037037037035,
209	      "max_off_ratio": 0.8695652173913043,
210	      "cond": 4.870288675477777,
211	      "log_cond": 0.6875547038124716,
212	      "mean_entropy": 0.43453021038119094,
213	      "max_entropy": 0.7713193953324151,
214	      "spectral_gap": 0.0028660626516707755,
215	      "det": 0.008925803200779615,
216	      "min_sv": 0.2214503148484119,
217	      "sv_ratio": 4.870288675477777
218	    },
219	    "humaid_qwen3_few-shot-3": {
220	      "K": 10,
221	      "min_diag": 0.3931297709923664,
222	      "mean_diag": 0.7063022669364979,
223	      "max_off": 0.2978723404255319,
224	      "max_off_ratio": 0.7,
225	      "cond": 5.72434237860238,
226	      "log_cond": 0.7577256014488332,
227	      "mean_entropy": 0.41081616217542366,
228	      "max_entropy": 0.8134775624136212,
229	      "spectral_gap": 0.00039022559527035483,
230	      "det": 0.013036614440809164,
231	      "min_sv": 0.18397929070370805,
232	      "sv_ratio": 5.72434237860238
233	    },
234	    "humaid_qwen3_zero-shot": {
235	      "K": 10,
236	      "min_diag": 0.33980582524271846,
237	      "mean_diag": 0.7148479754316172,
238	      "max_off": 0.2524271844660194,
239	      "max_off_ratio": 0.7428571428571428,
240	      "cond": 6.582602874398559,
241	      "log_cond": 0.8183976550830058,
242	      "mean_entropy": 0.4004018270470443,
243	      "max_entropy": 0.8150457452375078,
244	      "spectral_gap": 0.0011457900846476576,
245	      "det": 0.012357927494210939,
246	      "min_sv": 0.15962335807759273,
247	      "sv_ratio": 6.582602874398559
248	    },
249	    "vast_deepseek_few-shot-3": {
250	      "K": 3,
251	      "min_diag": 0.1614,
252	      "mean_diag": 0.4912666666666667,
253	      "max_off": 0.5498,
254	      "max_off_ratio": 3.4064436183395292,
255	      "cond": 40.95372201283567,
256	      "log_cond": 1.6122933780422168,
257	      "mean_entropy": 0.7974342819114627,
258	      "max_entropy": 0.9139888143402456,
259	      "spectral_gap": 0.5559519852858835,
260	      "det": 0.013211310000000004,
261	      "min_sv": 0.027694998717582776,
262	      "sv_ratio": 40.95372201283567
263	    },
264	    "vast_deepseek_few-shot-5": {
265	      "K": 3,
266	      "min_diag": 0.1534,
267	      "mean_diag": 0.4885,
268	      "max_off": 0.5398,
269	      "max_off_ratio": 3.518904823989569,
270	      "cond": 53.727125634861714,
271	      "log_cond": 1.7301936067270767,
272	      "mean_entropy": 0.8032979177920327,
273	      "max_entropy": 0.9068116814640466,
274	      "spectral_gap": 0.5570947419168397,
275	      "det": 0.01000733000000001,
276	      "min_sv": 0.020971018582030168,
277	      "sv_ratio": 53.727125634861714
278	    },
279	    "vast_llama4_few-shot-3": {
280	      "K": 3,
281	      "min_diag": 0.035856573705179286,
282	      "mean_diag": 0.4985873764874555,
283	      "max_off": 0.5597609561752988,
284	      "max_off_ratio": 15.611111111111109,
285	      "cond": 113.24057656953107,
286	      "log_cond": 2.0540020719287444,
287	      "mean_entropy": 0.6402731463960377,
288	      "max_entropy": 0.7375332872720923,
289	      "spectral_gap": 0.516941742068227,
290	      "det": 0.0061367100505578046,
291	      "min_sv": 0.01066288354023808,
292	      "sv_ratio": 113.24057656953107
293	    },
294	    "vast_llama4_zero-shot": {
295	      "K": 3,
296	      "min_diag": 0.045816733067729085,
297	      "mean_diag": 0.5216124706532176,
298	      "max_off": 0.5577689243027888,
299	      "max_off_ratio": 12.17391304347826,
300	      "cond": 54.48131734913794,
301	      "log_cond": 1.7362476001995972,
302	      "mean_entropy": 0.6173115559213345,
303	      "max_entropy": 0.758856913127135,
304	      "spectral_gap": 0.46162397368924357,
305	      "det": 0.014246175656329038,
306	      "min_sv": 0.022236067447757614,
307	      "sv_ratio": 54.48131734913794
308	    },
309	    "vast_qwen2.5-7b_few-shot-3": {
310	      "K": 3,
311	      "min_diag": 0.1254980079681275,
312	      "mean_diag": 0.4532888393169694,
313	      "max_off": 0.651394422310757,
314	      "max_off_ratio": 5.190476190476191,
315	      "cond": 111.1270861770333,
316	      "log_cond": 2.0458199270191657,
317	      "mean_entropy": 0.7494210032040004,
318	      "max_entropy": 0.9120157004147182,
319	      "spectral_gap": 0.6520812855623053,
320	      "det": 0.004156864438671191,
321	      "min_sv": 0.010911780335739175,
322	      "sv_ratio": 111.1270861770333
323	    },
324	    "vast_qwen2.5-7b_few-shot-5": {
325	      "K": 3,
326	      "min_diag": 0.1254980079681275,
327	      "mean_diag": 0.45892242630285923,
328	      "max_off": 0.6155378486055777,
329	      "max_off_ratio": 4.904761904761905,
330	      "cond": 292.8616802480159,
331	      "log_cond": 2.466662549743874,
332	      "mean_entropy": 0.7843608143445023,
333	      "max_entropy": 0.8999538872919803,
334	      "spectral_gap": 0.6276149443465993,
335	      "det": 0.0016318744507647553,
336	      "min_sv": 0.003986492266047296,
337	      "sv_ratio": 292.8616802480159
338	    },
339	    "vast_qwen2.5-7b_zero-shot": {
340	      "K": 3,
341	      "min_diag": 0.10956175298804781,
342	      "mean_diag": 0.47279759022154383,
343	      "max_off": 0.649402390438247,
344	      "max_off_ratio": 5.927272727272727,
345	      "cond": 65.13521884652558,
346	      "log_cond": 1.813815876660881,
347	      "mean_entropy": 0.7152614068872879,
348	      "max_entropy": 0.8730051540097549,
349	      "spectral_gap": 0.602552052881631,
350	      "det": 0.008324477121218572,
351	      "min_sv": 0.018811187149272508,
352	      "sv_ratio": 65.13521884652558
353	    },
354	    "vast_qwen3_zero-shot": {
355	      "K": 3,
356	      "min_diag": 0.073558648111332,
357	      "mean_diag": 0.5113590987099933,
358	      "max_off": 0.5228628230616302,
359	      "max_off_ratio": 7.108108108108109,
360	      "cond": 241.85169802277628,
361	      "log_cond": 2.383549140884421,
362	      "mean_entropy": 0.7159555477281506,
363	      "max_entropy": 0.8166738157616458,
364	      "spectral_gap": 0.4713863544008603,
365	      "det": 0.002888160225386867,
366	      "min_sv": 0.004765484870709368,
367	      "sv_ratio": 241.85169802277628
368	    }
369	  },
370	  "per_beta_results": {
371	    "default": {
372	      "beta_label": "default",
373	      "n_total": 23,
374	      "n_flip": 14,
375	      "rows": [
376	        {
377	          "config": "civil_comments_deepseek_few-shot-5",
378	          "K": 2,
379	          "beta": [
380	            0.0,
381	            1.0
382	          ],
383	          "sign_flip": false,
384	          "tau_true": 1.0006875736432363,
385	          "tau_hat": 0.5305207649625853,
386	          "max_relbias": 0.4698437564972444,
387	          "per_coef": [
388	            {
389	              "coef_idx": 1,
390	              "true": 1.0006875736432363,
391	              "biased": 0.5305207649625853,
392	              "sign_flip": false
393	            }
394	          ],
395	          "features": {
396	            "K": 2,
397	            "min_diag": 0.7341211225997046,
398	            "mean_diag": 0.7677454928067016,
399	            "max_off": 0.2658788774002954,
400	            "max_off_ratio": 0.36217303822937624,
401	            "cond": 1.8792558531832826,
402	            "log_cond": 0.2739859115860814,
403	            "mean_entropy": 0.7773343104187012,
404	            "max_entropy": 0.8354887266831242,
405	            "spectral_gap": 0.46450901438659675,
406	            "det": 0.5354909856134032,
407	            "min_sv": 0.5338056010567983,
408	            "sv_ratio": 1.8792558531832826
409	          }
410	        },
411	        {
412	          "config": "civil_comments_qwen2.5-7b_few-shot-3",
413	          "K": 2,
414	          "beta": [
415	            0.0,
416	            1.0
417	          ],
418	          "sign_flip": false,
419	          "tau_true": 1.0006875736432363,
420	          "tau_hat": 0.45662813653905343,
421	          "max_relbias": 0.5436856132063355,
422	          "per_coef": [
423	            {
424	              "coef_idx": 1,
425	              "true": 1.0006875736432363,
426	              "biased": 0.45662813653905343,
427	              "sign_flip": false
428	            }
429	          ],
430	          "features": {
431	            "K": 2,
432	            "min_diag": 0.6787296898079763,
433	            "mean_diag": 0.7297758038080977,
434	            "max_off": 0.3212703101920236,
435	            "max_off_ratio": 0.4733405875952122,
436	            "cond": 2.2046870875055347,
437	            "log_cond": 0.34334695851446095,
438	            "mean_entropy": 0.832210695039356,
439	            "max_entropy": 0.9057575271903423,
440	            "spectral_gap": 0.5404483923838045,
441	            "det": 0.45955160761619557,
442	            "min_sv": 0.45655559105857724,
443	            "sv_ratio": 2.2046870875055347
444	          }
445	        },
446	        {
447	          "config": "civil_comments_qwen2.5-7b_few-shot-5",
448	          "K": 2,
449	          "beta": [
450	            0.0,
451	            1.0
452	          ],
453	          "sign_flip": false,
454	          "tau_true": 1.0006875736432363,
455	          "tau_hat": 0.49300172165470246,
456	          "max_relbias": 0.5073370204250516,
457	          "per_coef": [
458	            {
459	              "coef_idx": 1,
460	              "true": 1.0006875736432363,
461	              "biased": 0.49300172165470246,
462	              "sign_flip": false
463	            }
464	          ],
465	          "features": {
466	            "K": 2,
467	            "min_diag": 0.7370753323485968,
468	            "mean_diag": 0.7486746524756682,
469	            "max_off": 0.26292466765140327,
470	            "max_off_ratio": 0.35671342685370744,
471	            "cond": 2.0120966711779484,
472	            "log_cond": 0.30364884256210606,
473	            "mean_entropy": 0.8128560597271433,
474	            "max_entropy": 0.8311277438478006,
475	            "spectral_gap": 0.5026506950486636,
476	            "det": 0.4973493049513366,
477	            "min_sv": 0.49717162744867915,
478	            "sv_ratio": 2.0120966711779484
479	          }
480	        },
481	        {
482	          "config": "civil_comments_qwen2.5-7b_zero-shot",
483	          "K": 2,
484	          "beta": [
485	            0.0,
486	            1.0
487	          ],
488	          "sign_flip": false,
489	          "tau_true": 1.0006875736432363,
490	          "tau_hat": 0.43394147965280977,
491	          "max_relbias": 0.5663566820631691,
492	          "per_coef": [
493	            {
494	              "coef_idx": 1,
495	              "true": 1.0006875736432363,
496	              "biased": 0.43394147965280977,
497	              "sign_flip": false
498	            }
499	          ],
500	          "features": {
501	            "K": 2,
502	            "min_diag": 0.684931506849315,
503	            "mean_diag": 0.7165425628781288,
504	            "max_off": 0.3150684931506849,
505	            "max_off_ratio": 0.46,
506	            "cond": 2.320361980143194,
507	            "log_cond": 0.3655557408029338,
508	            "mean_entropy": 0.8565646301807837,
509	            "max_entropy": 0.8989377852081333,
510	            "spectral_gap": 0.5669148742437425,
511	            "det": 0.43308512575625746,
512	            "min_sv": 0.4320248854336829,
513	            "sv_ratio": 2.320361980143194
514	          }
515	        },
516	        {
517	          "config": "civil_comments_qwen3_few-shot-3",
518	          "K": 2,
519	          "beta": [
520	            0.0,
521	            1.0
522	          ],
523	          "sign_flip": false,
524	          "tau_true": 1.0006875736432363,
525	          "tau_hat": 0.5669624111960679,
526	          "max_relbias": 0.43342714936300336,
527	          "per_coef": [
528	            {
529	              "coef_idx": 1,
530	              "true": 1.0006875736432363,
531	              "biased": 0.5669624111960679,
532	              "sign_flip": false
533	            }
534	          ],
535	          "features": {
536	            "K": 2,
537	            "min_diag": 0.7448275862068966,
538	            "mean_diag": 0.7813701217488962,
539	            "max_off": 0.25517241379310346,
540	            "max_off_ratio": 0.34259259259259256,
541	            "cond": 1.790859904151061,
542	            "log_cond": 0.25306161307745983,
543	            "mean_entropy": 0.7519979451235315,
544	            "max_entropy": 0.8193737468292397,
545	            "spectral_gap": 0.43725975650220783,
546	            "det": 0.5627402434977923,
547	            "min_sv": 0.5605613889083931,
548	            "sv_ratio": 1.790859904151061
549	          }
550	        },
551	        {
552	          "config": "civil_comments_qwen3_few-shot-5",
553	          "K": 2,
554	          "beta": [
555	            0.0,
556	            1.0
557	          ],
558	          "sign_flip": false,
559	          "tau_true": 1.0006875736432363,
560	          "tau_hat": 0.6166639927983613,
561	          "max_relbias": 0.3837597177775954,
562	          "per_coef": [
563	            {
564	              "coef_idx": 1,
565	              "true": 1.0006875736432363,
566	              "biased": 0.6166639927983613,
567	              "sign_flip": false
568	            }
569	          ],
570	          "features": {
571	            "K": 2,
572	            "min_diag": 0.7931034482758621,
573	            "mean_diag": 0.8085784501958375,
574	            "max_off": 0.20689655172413793,
575	            "max_off_ratio": 0.2608695652173913,
576	            "cond": 1.6228381125800326,
577	            "log_cond": 0.21027519861870325,
578	            "mean_entropy": 0.7033187055895573,
579	            "max_entropy": 0.7355085815538399,
580	            "spectral_gap": 0.3828430996083251,
581	            "det": 0.617156900391675,
582	            "min_sv": 0.6166804707799527,
583	            "sv_ratio": 1.6228381125800326
584	          }
585	        },
586	        {
587	          "config": "civil_comments_qwen3_zero-shot",
588	          "K": 2,
589	          "beta": [
590	            0.0,
591	            1.0
592	          ],
593	          "sign_flip": false,
594	          "tau_true": 1.0006875736432363,
595	          "tau_hat": 0.5197910616224681,
596	          "max_relbias": 0.4805660874452077,
597	          "per_coef": [
598	            {
599	              "coef_idx": 1,
600	              "true": 1.0006875736432363,
601	              "biased": 0.5197910616224681,
602	              "sign_flip": false
603	            }
604	          ],
605	          "features": {
606	            "K": 2,
607	            "min_diag": 0.7425742574257426,
608	            "mean_diag": 0.7603464334163478,
609	            "max_off": 0.25742574257425743,
610	            "max_off_ratio": 0.3466666666666667,
611	            "cond": 1.923844741767405,
612	            "log_cond": 0.28417002065689095,
613	            "mean_entropy": 0.7932124509685978,
614	            "max_entropy": 0.8228368841492258,
615	            "spectral_gap": 0.47930713316730444,
616	            "det": 0.5206928668326956,
617	            "min_sv": 0.5202424709655475,
618	            "sv_ratio": 1.923844741767405
619	          }
620	        },
621	        {
622	          "config": "humaid_deepseek_few-shot-3",
623	          "K": 10,
624	          "beta": [
625	            0.0,
626	            1.0,
627	            -0.5,
628	            0.7,
629	            -0.3,
630	            0.5,
631	            -0.2,
632	            0.4,
633	            -0.15,
634	            0.3
635	          ],
636	          "sign_flip": true,
637	          "tau_true": 1.0021612541230112,
638	          "tau_hat": 0.8278727427727858,
639	          "max_relbias": 1.54745291630718,
640	          "per_coef": [
641	            {
642	              "coef_idx": 1,
643	              "true": 1.0021612541230112,
644	              "biased": 0.8278727427727858,
645	              "sign_flip": false
646	            },
647	            {
648	              "coef_idx": 2,
649	              "true": -0.49517370647874964,
650	              "biased": -0.42553631449443496,
651	              "sign_flip": false
652	            },
653	            {
654	              "coef_idx": 3,
655	              "true": 0.7008430195564617,
656	              "biased": 0.5341553145594735,
657	              "sign_flip": false
658	            },
659	            {
660	              "coef_idx": 4,
661	              "true": -0.30108962245261534,
662	              "biased": -0.38689794267054595,
663	              "sign_flip": false
664	            },
665	            {
666	              "coef_idx": 5,
667	              "true": 0.5025766615731924,
668	              "biased": 0.18673802158843117,
669	              "sign_flip": false
670	            },
671	            {
672	              "coef_idx": 6,
673	              "true": -0.19876288751316182,
674	              "biased": -0.1482260185615129,
675	              "sign_flip": false
676	            },
677	            {
678	              "coef_idx": 7,
679	              "true": 0.4035632558824633,
680	              "biased": 0.256858482586773,
681	              "sign_flip": false
682	            },
683	            {
684	              "coef_idx": 8,
685	              "true": -0.1476792358653642,
686	              "biased": 0.08084742835250953,
687	              "sign_flip": true
688	            },
689	            {
690	              "coef_idx": 9,
691	              "true": 0.29903137710547223,
692	              "biased": 0.07833846334993375,
693	              "sign_flip": false
694	            }
695	          ],
696	          "features": {
697	            "K": 10,
698	            "min_diag": 0.38493723849372385,
699	            "mean_diag": 0.7247142947226147,
700	            "max_off": 0.25,
701	            "max_off_ratio": 0.532608695652174,
702	            "cond": 4.409507323985138,
703	            "log_cond": 0.6443900682824745,
704	            "mean_entropy": 0.4023974734197873,
705	            "max_entropy": 0.7534239502970503,
706	            "spectral_gap": 0.002150042096596194,
707	            "det": 0.021332189334821124,
708	            "min_sv": 0.23091827608687163,
709	            "sv_ratio": 4.409507323985138
710	          }
711	        },
712	        {
713	          "config": "humaid_deepseek_few-shot-5",
714	          "K": 10,
715	          "beta": [
716	            0.0,
717	            1.0,
718	            -0.5,
719	            0.7,
720	            -0.3,
721	            0.5,
722	            -0.2,
723	            0.4,
724	            -0.15,
725	            0.3
726	          ],
727	          "sign_flip": false,
728	          "tau_true": 1.0021612541230112,
729	          "tau_hat": 0.841653240466815,
730	          "max_relbias": 0.8667157323395721,
731	          "per_coef": [
732	            {
733	              "coef_idx": 1,
734	              "true": 1.0021612541230112,
735	              "biased": 0.841653240466815,
736	              "sign_flip": false
737	            },
738	            {
739	              "coef_idx": 2,
740	              "true": -0.49517370647874964,
741	              "biased": -0.4469411907716607,
742	              "sign_flip": false
743	            },
744	            {
745	              "coef_idx": 3,
746	              "true": 0.7008430195564617,
747	              "biased": 0.5185240415908795,
748	              "sign_flip": false
749	            },
750	            {
751	              "coef_idx": 4,
752	              "true": -0.30108962245261534,
753	              "biased": -0.38600384389901854,
754	              "sign_flip": false
755	            },
756	            {
757	              "coef_idx": 5,
758	              "true": 0.5025766615731924,
759	              "biased": 0.16296561318106229,
760	              "sign_flip": false
761	            },
762	            {
763	              "coef_idx": 6,
764	              "true": -0.19876288751316182,
765	              "biased": -0.18480090322445078,
766	              "sign_flip": false
767	            },
768	            {
769	              "coef_idx": 7,
770	              "true": 0.4035632558824633,
771	              "biased": 0.29587090452245157,
772	              "sign_flip": false
773	            },
774	            {
775	              "coef_idx": 8,
776	              "true": -0.1476792358653642,
777	              "biased": -0.019683318800966663,
778	              "sign_flip": false
779	            },
780	            {
781	              "coef_idx": 9,
782	              "true": 0.29903137710547223,
783	              "biased": 0.1001826173294286,
784	              "sign_flip": false
785	            }
786	          ],
787	          "features": {
788	            "K": 10,
789	            "min_diag": 0.3744292237442922,
790	            "mean_diag": 0.7239192695740293,
791	            "max_off": 0.2682926829268293,
792	            "max_off_ratio": 0.573170731707317,
793	            "cond": 4.638454996807901,
794	            "log_cond": 0.6663733473444414,
795	            "mean_entropy": 0.3967710539627384,
796	            "max_entropy": 0.7683639237792222,
797	            "spectral_gap": 0.0032537141891824106,
798	            "det": 0.020280304489390028,
799	            "min_sv": 0.2206751028987421,
800	            "sv_ratio": 4.638454996807901
801	          }
802	        },
803	        {
804	          "config": "humaid_deepseek_zero-shot",
805	          "K": 10,
806	          "beta": [
807	            0.0,
808	            1.0,
809	            -0.5,
810	            0.7,
811	            -0.3,
812	            0.5,
813	            -0.2,
814	            0.4,
815	            -0.15,
816	            0.3
817	          ],
818	          "sign_flip": true,
819	          "tau_true": 1.0021612541230112,
820	          "tau_hat": 0.8940429208215853,
821	          "max_relbias": 1.610112245872741,
822	          "per_coef": [
823	            {
824	              "coef_idx": 1,
825	              "true": 1.0021612541230112,
826	              "biased": 0.8940429208215853,
827	              "sign_flip": false
828	            },
829	            {
830	              "coef_idx": 2,
831	              "true": -0.49517370647874964,
832	              "biased": -0.3180150798052478,
833	              "sign_flip": false
834	            },
835	            {
836	              "coef_idx": 3,
837	              "true": 0.7008430195564617,
838	              "biased": 0.6190986795284974,
839	              "sign_flip": false
840	            },
841	            {
842	              "coef_idx": 4,
843	              "true": -0.30108962245261534,
844	              "biased": -0.32167022823757246,
845	              "sign_flip": false
846	            },
847	            {
848	              "coef_idx": 5,
849	              "true": 0.5025766615731924,
850	              "biased": 0.23911602832434856,
851	              "sign_flip": false
852	            },
853	            {
854	              "coef_idx": 6,
855	              "true": -0.19876288751316182,
856	              "biased": -0.0652136346902237,
857	              "sign_flip": false
858	            },
859	            {
860	              "coef_idx": 7,
861	              "true": 0.4035632558824633,
862	              "biased": 0.35790092209445173,
863	              "sign_flip": false
864	            },
865	            {
866	              "coef_idx": 8,
867	              "true": -0.1476792358653642,
868	              "biased": 0.09010091026258758,
869	              "sign_flip": true
870	            },
871	            {
872	              "coef_idx": 9,
873	              "true": 0.29903137710547223,
874	              "biased": 0.1675676353193211,
875	              "sign_flip": false
876	            }
877	          ],
878	          "features": {
879	            "K": 10,
880	            "min_diag": 0.29411764705882354,
881	            "mean_diag": 0.7236183709906748,
882	            "max_off": 0.22807017543859648,
883	            "max_off_ratio": 0.7,
884	            "cond": 5.109683690040082,
885	            "log_cond": 0.7083940163926374,
886	            "mean_entropy": 0.41300072961171885,
887	            "max_entropy": 0.8011248606608374,
888	            "spectral_gap": 0.002559866244257969,
889	            "det": 0.018291677753051495,
890	            "min_sv": 0.19952987155984303,
891	            "sv_ratio": 5.109683690040082
892	          }
893	        },
894	        {
895	          "config": "humaid_llama4_few-shot-3",
896	          "K": 10,
897	          "beta": [
898	            0.0,
899	            1.0,
900	            -0.5,
901	            0.7,
902	            -0.3,
903	            0.5,
904	            -0.2,
905	            0.4,
906	            -0.15,
907	            0.3
908	          ],
909	          "sign_flip": true,
910	          "tau_true": 1.0021612541230112,
911	          "tau_hat": 0.8797909761297256,
912	          "max_relbias": 2.0294374930565473,
913	          "per_coef": [
914	            {
915	              "coef_idx": 1,
916	              "true": 1.0021612541230112,
917	              "biased": 0.8797909761297256,
918	              "sign_flip": false
919	            },
920	            {
921	              "coef_idx": 2,
922	              "true": -0.49517370647874964,
923	              "biased": -0.3676786022937333,
924	              "sign_flip": false
925	            },
926	            {
927	              "coef_idx": 3,
928	              "true": 0.7008430195564617,
929	              "biased": 0.5926481216126885,
930	              "sign_flip": false
931	            },
932	            {
933	              "coef_idx": 4,
934	              "true": -0.30108962245261534,
935	              "biased": -0.34645198667742366,
936	              "sign_flip": false
937	            },
938	            {
939	              "coef_idx": 5,
940	              "true": 0.5025766615731924,
941	              "biased": 0.26900325515815104,
942	              "sign_flip": false
943	            },
944	            {
945	              "coef_idx": 6,
946	              "true": -0.19876288751316182,
947	              "biased": -0.09104547679409226,
948	              "sign_flip": false
949	            },
950	            {
951	              "coef_idx": 7,
952	              "true": 0.4035632558824633,
953	              "biased": 0.3239713031421688,
954	              "sign_flip": false
955	            },
956	            {
957	              "coef_idx": 8,
958	              "true": -0.1476792358653642,
959	              "biased": 0.15202654234574706,
960	              "sign_flip": true
961	            },
962	            {
963	              "coef_idx": 9,
964	              "true": 0.29903137710547223,
965	              "biased": 0.1172976328881252,
966	              "sign_flip": false
967	            }
968	          ],
969	          "features": {
970	            "K": 10,
971	            "min_diag": 0.4074074074074074,
972	            "mean_diag": 0.675799138052473,
973	            "max_off": 0.4074074074074074,
974	            "max_off_ratio": 1.0,
975	            "cond": 5.138340099658911,
976	            "log_cond": 0.7108228462356819,
977	            "mean_entropy": 0.4307113519912539,
978	            "max_entropy": 0.764437246894965,
979	            "spectral_gap": 0.003339175071885747,
980	            "det": 0.009915635381985513,
981	            "min_sv": 0.20950042424565504,
982	            "sv_ratio": 5.138340099658911
983	          }
984	        },
985	        {
986	          "config": "humaid_llama4_few-shot-5",
987	          "K": 10,
988	          "beta": [
989	            0.0,
990	            1.0,
991	            -0.5,
992	            0.7,
993	            -0.3,
994	            0.5,
995	            -0.2,
996	            0.4,
997	            -0.15,
998	            0.3
999	          ],
1000	          "sign_flip": true,
1001	          "tau_true": 1.0021612541230112,
1002	          "tau_hat": 0.8784067121148408,
1003	          "max_relbias": 1.8698812403090272,
1004	          "per_coef": [
1005	            {
1006	              "coef_idx": 1,
1007	              "true": 1.0021612541230112,
1008	              "biased": 0.8784067121148408,
1009	              "sign_flip": false
1010	            },
1011	            {
1012	              "coef_idx": 2,
1013	              "true": -0.49517370647874964,
1014	              "biased": -0.36623075729125476,
1015	              "sign_flip": false
1016	            },
1017	            {
1018	              "coef_idx": 3,
1019	              "true": 0.7008430195564617,
1020	              "biased": 0.596566083797507,
1021	              "sign_flip": false
1022	            },
1023	            {
1024	              "coef_idx": 4,
1025	              "true": -0.30108962245261534,
1026	              "biased": -0.3488808810941477,
1027	              "sign_flip": false
1028	            },
1029	            {
1030	              "coef_idx": 5,
1031	              "true": 0.5025766615731924,
1032	              "biased": 0.26527865767099024,
1033	              "sign_flip": false
1034	            },
1035	            {
1036	              "coef_idx": 6,
1037	              "true": -0.19876288751316182,
1038	              "biased": -0.09848475862964137,
1039	              "sign_flip": false
1040	            },
1041	            {
1042	              "coef_idx": 7,
1043	              "true": 0.4035632558824633,
1044	              "biased": 0.30877504333397726,
1045	              "sign_flip": false
1046	            },
1047	            {
1048	              "coef_idx": 8,
1049	              "true": -0.1476792358653642,
1050	              "biased": 0.12846339686245237,
1051	              "sign_flip": true
1052	            },
1053	            {
1054	              "coef_idx": 9,
1055	              "true": 0.29903137710547223,
1056	              "biased": 0.09852556257785414,
1057	              "sign_flip": false
1058	            }
1059	          ],
1060	          "features": {
1061	            "K": 10,
1062	            "min_diag": 0.41509433962264153,
1063	            "mean_diag": 0.6876826799336799,
1064	            "max_off": 0.39622641509433965,
1065	            "max_off_ratio": 0.9545454545454546,
1066	            "cond": 5.153050727272362,
1067	            "log_cond": 0.7120644177310209,
1068	            "mean_entropy": 0.41852478500884976,
1069	            "max_entropy": 0.7443560908326295,
1070	            "spectral_gap": 0.0017801324917138261,
1071	            "det": 0.01172179530195112,
1072	            "min_sv": 0.20767898111002162,
1073	            "sv_ratio": 5.153050727272362
1074	          }
1075	        },
1076	        {
1077	          "config": "humaid_llama4_zero-shot",
1078	          "K": 10,
1079	          "beta": [
1080	            0.0,
1081	            1.0,
1082	            -0.5,
1083	            0.7,
1084	            -0.3,
1085	            0.5,
1086	            -0.2,
1087	            0.4,
1088	            -0.15,
1089	            0.3
1090	          ],
1091	          "sign_flip": true,
1092	          "tau_true": 1.0021612541230112,
1093	          "tau_hat": 0.8840345444742779,
1094	          "max_relbias": 1.8912879926626072,
1095	          "per_coef": [
1096	            {
1097	              "coef_idx": 1,
1098	              "true": 1.0021612541230112,
1099	              "biased": 0.8840345444742779,
1100	              "sign_flip": false
1101	            },
1102	            {
1103	              "coef_idx": 2,
1104	              "true": -0.49517370647874964,
1105	              "biased": -0.33943526207011193,
1106	              "sign_flip": false
1107	            },
1108	            {
1109	              "coef_idx": 3,
1110	              "true": 0.7008430195564617,
1111	              "biased": 0.6020019446065337,
1112	              "sign_flip": false
1113	            },
1114	            {
1115	              "coef_idx": 4,
1116	              "true": -0.30108962245261534,
1117	              "biased": -0.34834641569279595,
1118	              "sign_flip": false
1119	            },
1120	            {
1121	              "coef_idx": 5,
1122	              "true": 0.5025766615731924,
1123	              "biased": 0.3197842197446264,
1124	              "sign_flip": false
1125	            },
1126	            {
1127	              "coef_idx": 6,
1128	              "true": -0.19876288751316182,
1129	              "biased": -0.05543287567285432,
1130	              "sign_flip": false
1131	            },
1132	            {
1133	              "coef_idx": 7,
1134	              "true": 0.4035632558824633,
1135	              "biased": 0.37264831791983927,
1136	              "sign_flip": false
1137	            },
1138	            {
1139	              "coef_idx": 8,
1140	              "true": -0.1476792358653642,
1141	              "biased": 0.13162472969238814,
1142	              "sign_flip": true
1143	            },
1144	            {
1145	              "coef_idx": 9,
1146	              "true": 0.29903137710547223,
1147	              "biased": 0.1106254175216702,
1148	              "sign_flip": false
1149	            }
1150	          ],
1151	          "features": {
1152	            "K": 10,
1153	            "min_diag": 0.42592592592592593,
1154	            "mean_diag": 0.6707836618157876,
1155	            "max_off": 0.37037037037037035,
1156	            "max_off_ratio": 0.8695652173913043,
1157	            "cond": 4.870288675477777,
1158	            "log_cond": 0.6875547038124716,
1159	            "mean_entropy": 0.43453021038119094,
1160	            "max_entropy": 0.7713193953324151,
1161	            "spectral_gap": 0.0028660626516707755,
1162	            "det": 0.008925803200779615,
1163	            "min_sv": 0.2214503148484119,
1164	            "sv_ratio": 4.870288675477777
1165	          }
1166	        },
1167	        {
1168	          "config": "humaid_qwen3_few-shot-3",
1169	          "K": 10,
1170	          "beta": [
1171	            0.0,
1172	            1.0,
1173	            -0.5,
1174	            0.7,
1175	            -0.3,
1176	            0.5,
1177	            -0.2,
1178	            0.4,
1179	            -0.15,
1180	            0.3
1181	          ],
1182	          "sign_flip": true,
1183	          "tau_true": 1.0021612541230112,
1184	          "tau_hat": 0.9118526035690211,
1185	          "max_relbias": 1.7444234831774357,
1186	          "per_coef": [
1187	            {
1188	              "coef_idx": 1,
1189	              "true": 1.0021612541230112,
1190	              "biased": 0.9118526035690211,
1191	              "sign_flip": false
1192	            },
1193	            {
1194	              "coef_idx": 2,
1195	              "true": -0.49517370647874964,
1196	              "biased": -0.271424898474264,
1197	              "sign_flip": false
1198	            },
1199	            {
1200	              "coef_idx": 3,
1201	              "true": 0.7008430195564617,
1202	              "biased": 0.607926135561378,
1203	              "sign_flip": false
1204	            },
1205	            {
1206	              "coef_idx": 4,
1207	              "true": -0.30108962245261534,
1208	              "biased": -0.28915605341692774,
1209	              "sign_flip": false
1210	            },
1211	            {
1212	              "coef_idx": 5,
1213	              "true": 0.5025766615731924,
1214	              "biased": 0.31153486870094865,
1215	              "sign_flip": false
1216	            },
1217	            {
1218	              "coef_idx": 6,
1219	              "true": -0.19876288751316182,
1220	              "biased": 0.042554446231192006,
1221	              "sign_flip": true
1222	            },
1223	            {
1224	              "coef_idx": 7,
1225	              "true": 0.4035632558824633,
1226	              "biased": 0.4208021966689176,
1227	              "sign_flip": false
1228	            },
1229	            {
1230	              "coef_idx": 8,
1231	              "true": -0.1476792358653642,
1232	              "biased": 0.10993589115587647,
1233	              "sign_flip": true
1234	            },
1235	            {
1236	              "coef_idx": 9,
1237	              "true": 0.29903137710547223,
1238	              "biased": 0.20069942582976483,
1239	              "sign_flip": false
1240	            }
1241	          ],
1242	          "features": {
1243	            "K": 10,
1244	            "min_diag": 0.3931297709923664,
1245	            "mean_diag": 0.7063022669364979,
1246	            "max_off": 0.2978723404255319,
1247	            "max_off_ratio": 0.7,
1248	            "cond": 5.72434237860238,
1249	            "log_cond": 0.7577256014488332,
1250	            "mean_entropy": 0.41081616217542366,
1251	            "max_entropy": 0.8134775624136212,
1252	            "spectral_gap": 0.00039022559527035483,
1253	            "det": 0.013036614440809164,
1254	            "min_sv": 0.18397929070370805,
1255	            "sv_ratio": 5.72434237860238
1256	          }
1257	        },
1258	        {
1259	          "config": "humaid_qwen3_zero-shot",
1260	          "K": 10,
1261	          "beta": [
1262	            0.0,
1263	            1.0,
1264	            -0.5,
1265	            0.7,
1266	            -0.3,
1267	            0.5,
1268	            -0.2,
1269	            0.4,
1270	            -0.15,
1271	            0.3
1272	          ],
1273	          "sign_flip": true,
1274	          "tau_true": 1.0021612541230112,
1275	          "tau_hat": 0.9015353668810818,
1276	          "max_relbias": 1.207707112917553,
1277	          "per_coef": [
1278	            {
1279	              "coef_idx": 1,
1280	              "true": 1.0021612541230112,
1281	              "biased": 0.9015353668810818,
1282	              "sign_flip": false
1283	            },
1284	            {
1285	              "coef_idx": 2,
1286	              "true": -0.49517370647874964,
1287	              "biased": -0.31399131826938964,
1288	              "sign_flip": false
1289	            },
1290	            {
1291	              "coef_idx": 3,
1292	              "true": 0.7008430195564617,
1293	              "biased": 0.5656201967923609,
1294	              "sign_flip": false
1295	            },
1296	            {
1297	              "coef_idx": 4,
1298	              "true": -0.30108962245261534,
1299	              "biased": -0.3298987643025529,
1300	              "sign_flip": false
1301	            },
1302	            {
1303	              "coef_idx": 5,
1304	              "true": 0.5025766615731924,
1305	              "biased": 0.33549235471907085,
1306	              "sign_flip": false
1307	            },
1308	            {
1309	              "coef_idx": 6,
1310	              "true": -0.19876288751316182,
1311	              "biased": -0.026314799952895093,
1312	              "sign_flip": false
1313	            },
1314	            {
1315	              "coef_idx": 7,
1316	              "true": 0.4035632558824633,
1317	              "biased": 0.26042733389311096,
1318	              "sign_flip": false
1319	            },
1320	            {
1321	              "coef_idx": 8,
1322	              "true": -0.1476792358653642,
1323	              "biased": 0.030674027719465136,
1324	              "sign_flip": true
1325	            },
1326	            {
1327	              "coef_idx": 9,
1328	              "true": 0.29903137710547223,
1329	              "biased": 0.2057344022035468,
1330	              "sign_flip": false
1331	            }
1332	          ],
1333	          "features": {
1334	            "K": 10,
1335	            "min_diag": 0.33980582524271846,
1336	            "mean_diag": 0.7148479754316172,
1337	            "max_off": 0.2524271844660194,
1338	            "max_off_ratio": 0.7428571428571428,
1339	            "cond": 6.582602874398559,
1340	            "log_cond": 0.8183976550830058,
1341	            "mean_entropy": 0.4004018270470443,
1342	            "max_entropy": 0.8150457452375078,
1343	            "spectral_gap": 0.0011457900846476576,
1344	            "det": 0.012357927494210939,
1345	            "min_sv": 0.15962335807759273,
1346	            "sv_ratio": 6.582602874398559
1347	          }
1348	        },
1349	        {
1350	          "config": "vast_deepseek_few-shot-3",
1351	          "K": 3,
1352	          "beta": [
1353	            0.0,
1354	            1.0,
1355	            -0.5
1356	          ],
1357	          "sign_flip": true,
1358	          "tau_true": 1.002519027440807,
1359	          "tau_hat": 0.38903267327878843,
1360	          "max_relbias": 1.2138041435685603,
1361	          "per_coef": [
1362	            {
1363	              "coef_idx": 1,
1364	              "true": 1.002519027440807,
1365	              "biased": 0.38903267327878843,
1366	              "sign_flip": false
1367	            },
1368	            {
1369	              "coef_idx": 2,
1370	              "true": -0.49812488588521125,
1371	              "biased": 0.10650116461687434,
1372	              "sign_flip": true
1373	            }
1374	          ],
1375	          "features": {
1376	            "K": 3,
1377	            "min_diag": 0.1614,
1378	            "mean_diag": 0.4912666666666667,
1379	            "max_off": 0.5498,
1380	            "max_off_ratio": 3.4064436183395292,
1381	            "cond": 40.95372201283567,
1382	            "log_cond": 1.6122933780422168,
1383	            "mean_entropy": 0.7974342819114627,
1384	            "max_entropy": 0.9139888143402456,
1385	            "spectral_gap": 0.5559519852858835,
1386	            "det": 0.013211310000000004,
1387	            "min_sv": 0.027694998717582776,
1388	            "sv_ratio": 40.95372201283567
1389	          }
1390	        },
1391	        {
1392	          "config": "vast_deepseek_few-shot-5",
1393	          "K": 3,
1394	          "beta": [
1395	            0.0,
1396	            1.0,
1397	            -0.5
1398	          ],
1399	          "sign_flip": true,
1400	          "tau_true": 1.002519027440807,
1401	          "tau_hat": 0.3836460108526146,
1402	          "max_relbias": 1.2179506506277331,
1403	          "per_coef": [
1404	            {
1405	              "coef_idx": 1,
1406	              "true": 1.002519027440807,
1407	              "biased": 0.3836460108526146,
1408	              "sign_flip": false
1409	            },
1410	            {
1411	              "coef_idx": 2,
1412	              "true": -0.49812488588521125,
1413	              "biased": 0.10856664297254703,
1414	              "sign_flip": true
1415	            }
1416	          ],
1417	          "features": {
1418	            "K": 3,
1419	            "min_diag": 0.1534,
1420	            "mean_diag": 0.4885,
1421	            "max_off": 0.5398,
1422	            "max_off_ratio": 3.518904823989569,
1423	            "cond": 53.727125634861714,
1424	            "log_cond": 1.7301936067270767,
1425	            "mean_entropy": 0.8032979177920327,
1426	            "max_entropy": 0.9068116814640466,
1427	            "spectral_gap": 0.5570947419168397,
1428	            "det": 0.01000733000000001,
1429	            "min_sv": 0.020971018582030168,
1430	            "sv_ratio": 53.727125634861714
1431	          }
1432	        },
1433	        {
1434	          "config": "vast_llama4_few-shot-3",
1435	          "K": 3,
1436	          "beta": [
1437	            0.0,
1438	            1.0,
1439	            -0.5
1440	          ],
1441	          "sign_flip": true,
1442	          "tau_true": 1.002519027440807,
1443	          "tau_hat": 0.3567348839067319,
1444	          "max_relbias": 1.0998303669934641,
1445	          "per_coef": [
1446	            {
1447	              "coef_idx": 1,
1448	              "true": 1.002519027440807,
1449	              "biased": 0.3567348839067319,
1450	              "sign_flip": false
1451	            },
1452	            {
1453	              "coef_idx": 2,
1454	              "true": -0.49812488588521125,
1455	              "biased": 0.049727990166498,
1456	              "sign_flip": true
1457	            }
1458	          ],
1459	          "features": {
1460	            "K": 3,
1461	            "min_diag": 0.035856573705179286,
1462	            "mean_diag": 0.4985873764874555,
1463	            "max_off": 0.5597609561752988,
1464	            "max_off_ratio": 15.611111111111109,
1465	            "cond": 113.24057656953107,
1466	            "log_cond": 2.0540020719287444,
1467	            "mean_entropy": 0.6402731463960377,
1468	            "max_entropy": 0.7375332872720923,
1469	            "spectral_gap": 0.516941742068227,
1470	            "det": 0.0061367100505578046,
1471	            "min_sv": 0.01066288354023808,
1472	            "sv_ratio": 113.24057656953107
1473	          }
1474	        },
1475	        {
1476	          "config": "vast_llama4_zero-shot",
1477	          "K": 3,
1478	          "beta": [
1479	            0.0,
1480	            1.0,
1481	            -0.5
1482	          ],
1483	          "sign_flip": false,
1484	          "tau_true": 1.002519027440807,
1485	          "tau_hat": 0.4051606794522447,
1486	          "max_relbias": 0.9647320420238192,
1487	          "per_coef": [
1488	            {
1489	              "coef_idx": 1,
1490	              "true": 1.002519027440807,
1491	              "biased": 0.4051606794522447,
1492	              "sign_flip": false
1493	            },
1494	            {
1495	              "coef_idx": 2,
1496	              "true": -0.49812488588521125,
1497	              "biased": -0.017567847542289485,
1498	              "sign_flip": false
1499	            }
1500	          ],
1501	          "features": {
1502	            "K": 3,
1503	            "min_diag": 0.045816733067729085,
1504	            "mean_diag": 0.5216124706532176,
1505	            "max_off": 0.5577689243027888,
1506	            "max_off_ratio": 12.17391304347826,
1507	            "cond": 54.48131734913794,
1508	            "log_cond": 1.7362476001995972,
1509	            "mean_entropy": 0.6173115559213345,
1510	            "max_entropy": 0.758856913127135,
1511	            "spectral_gap": 0.46162397368924357,
1512	            "det": 0.014246175656329038,
1513	            "min_sv": 0.022236067447757614,
1514	            "sv_ratio": 54.48131734913794
1515	          }
1516	        },
1517	        {
1518	          "config": "vast_qwen2.5-7b_few-shot-3",
1519	          "K": 3,
1520	          "beta": [
1521	            0.0,
1522	            1.0,
1523	            -0.5
1524	          ],
1525	          "sign_flip": true,
1526	          "tau_true": 1.002519027440807,
1527	          "tau_hat": 0.31896907346135567,
1528	          "max_relbias": 1.2588475386708207,
1529	          "per_coef": [
1530	            {
1531	              "coef_idx": 1,
1532	              "true": 1.002519027440807,
1533	              "biased": 0.31896907346135567,
1534	              "sign_flip": false
1535	            },
1536	            {
1537	              "coef_idx": 2,
1538	              "true": -0.49812488588521125,
1539	              "biased": 0.12893840066207032,
1540	              "sign_flip": true
1541	            }
1542	          ],
1543	          "features": {
1544	            "K": 3,
1545	            "min_diag": 0.1254980079681275,
1546	            "mean_diag": 0.4532888393169694,
1547	            "max_off": 0.651394422310757,
1548	            "max_off_ratio": 5.190476190476191,
1549	            "cond": 111.1270861770333,
1550	            "log_cond": 2.0458199270191657,
1551	            "mean_entropy": 0.7494210032040004,
1552	            "max_entropy": 0.9120157004147182,
1553	            "spectral_gap": 0.6520812855623053,
1554	            "det": 0.004156864438671191,
1555	            "min_sv": 0.010911780335739175,
1556	            "sv_ratio": 111.1270861770333
1557	          }
1558	        },
1559	        {
1560	          "config": "vast_qwen2.5-7b_few-shot-5",
1561	          "K": 3,
1562	          "beta": [
1563	            0.0,
1564	            1.0,
1565	            -0.5
1566	          ],
1567	          "sign_flip": true,
1568	          "tau_true": 1.002519027440807,
1569	          "tau_hat": 0.3129964862975079,
1570	          "max_relbias": 1.3426885395653874,
1571	          "per_coef": [
1572	            {
1573	              "coef_idx": 1,
1574	              "true": 1.002519027440807,
1575	              "biased": 0.3129964862975079,
1576	              "sign_flip": false
1577	            },
1578	            {
1579	              "coef_idx": 2,
1580	              "true": -0.49812488588521125,
1581	              "biased": 0.1707016896651782,
1582	              "sign_flip": true
1583	            }
1584	          ],
1585	          "features": {
1586	            "K": 3,
1587	            "min_diag": 0.1254980079681275,
1588	            "mean_diag": 0.45892242630285923,
1589	            "max_off": 0.6155378486055777,
1590	            "max_off_ratio": 4.904761904761905,
1591	            "cond": 292.8616802480159,
1592	            "log_cond": 2.466662549743874,
1593	            "mean_entropy": 0.7843608143445023,
1594	            "max_entropy": 0.8999538872919803,
1595	            "spectral_gap": 0.6276149443465993,
1596	            "det": 0.0016318744507647553,
1597	            "min_sv": 0.003986492266047296,
1598	            "sv_ratio": 292.8616802480159
1599	          }
1600	        },
1601	        {
1602	          "config": "vast_qwen2.5-7b_zero-shot",
1603	          "K": 3,
1604	          "beta": [
1605	            0.0,
1606	            1.0,
1607	            -0.5
1608	          ],
1609	          "sign_flip": true,
1610	          "tau_true": 1.002519027440807,
1611	          "tau_hat": 0.35108586571384476,
1612	          "max_relbias": 1.2701865774760586,
1613	          "per_coef": [
1614	            {
1615	              "coef_idx": 1,
1616	              "true": 1.002519027440807,
1617	              "biased": 0.35108586571384476,
1618	              "sign_flip": false
1619	            },
1620	            {
1621	              "coef_idx": 2,
1622	              "true": -0.49812488588521125,
1623	              "biased": 0.13458665807297754,
1624	              "sign_flip": true
1625	            }
1626	          ],
1627	          "features": {
1628	            "K": 3,
1629	            "min_diag": 0.10956175298804781,
1630	            "mean_diag": 0.47279759022154383,
1631	            "max_off": 0.649402390438247,
1632	            "max_off_ratio": 5.927272727272727,
1633	            "cond": 65.13521884652558,
1634	            "log_cond": 1.813815876660881,
1635	            "mean_entropy": 0.7152614068872879,
1636	            "max_entropy": 0.8730051540097549,
1637	            "spectral_gap": 0.602552052881631,
1638	            "det": 0.008324477121218572,
1639	            "min_sv": 0.018811187149272508,
1640	            "sv_ratio": 65.13521884652558
1641	          }
1642	        },
1643	        {
1644	          "config": "vast_qwen3_zero-shot",
1645	          "K": 3,
1646	          "beta": [
1647	            0.0,
1648	            1.0,
1649	            -0.5
1650	          ],
1651	          "sign_flip": true,
1652	          "tau_true": 1.002519027440807,
1653	          "tau_hat": 0.39784468402182716,
1654	          "max_relbias": 1.2873771929048614,
1655	          "per_coef": [
1656	            {
1657	              "coef_idx": 1,
1658	              "true": 1.002519027440807,
1659	              "biased": 0.39784468402182716,
1660	              "sign_flip": false
1661	            },
1662	            {
1663	              "coef_idx": 2,
1664	              "true": -0.49812488588521125,
1665	              "biased": 0.14314973142174645,
1666	              "sign_flip": true
1667	            }
1668	          ],
1669	          "features": {
1670	            "K": 3,
1671	            "min_diag": 0.073558648111332,
1672	            "mean_diag": 0.5113590987099933,
1673	            "max_off": 0.5228628230616302,
1674	            "max_off_ratio": 7.108108108108109,
1675	            "cond": 241.85169802277628,
1676	            "log_cond": 2.383549140884421,
1677	            "mean_entropy": 0.7159555477281506,
1678	            "max_entropy": 0.8166738157616458,
1679	            "spectral_gap": 0.4713863544008603,
1680	            "det": 0.002888160225386867,
1681	            "min_sv": 0.004765484870709368,
1682	            "sv_ratio": 241.85169802277628
1683	          }
1684	        }
1685	      ]
1686	    },
1687	    "uniform_pos": {
1688	      "beta_label": "uniform_pos",
1689	      "n_total": 23,
1690	      "n_flip": 0,
1691	      "rows": [
1692	        {
1693	          "config": "civil_comments_deepseek_few-shot-5",
1694	          "K": 2,
1695	          "beta": [
1696	            0.0,
1697	            1.0
1698	          ],
1699	          "sign_flip": false,
1700	          "tau_true": 1.0006875736432363,
1701	          "tau_hat": 0.5305207649625853,
1702	          "max_relbias": 0.4698437564972444,
1703	          "per_coef": [
1704	            {
1705	              "coef_idx": 1,
1706	              "true": 1.0006875736432363,
1707	              "biased": 0.5305207649625853,
1708	              "sign_flip": false
1709	            }
1710	          ],
1711	          "features": {
1712	            "K": 2,
1713	            "min_diag": 0.7341211225997046,
1714	            "mean_diag": 0.7677454928067016,
1715	            "max_off": 0.2658788774002954,
1716	            "max_off_ratio": 0.36217303822937624,
1717	            "cond": 1.8792558531832826,
1718	            "log_cond": 0.2739859115860814,
1719	            "mean_entropy": 0.7773343104187012,
1720	            "max_entropy": 0.8354887266831242,
1721	            "spectral_gap": 0.46450901438659675,
1722	            "det": 0.5354909856134032,
1723	            "min_sv": 0.5338056010567983,
1724	            "sv_ratio": 1.8792558531832826
1725	          }
1726	        },
1727	        {
1728	          "config": "civil_comments_qwen2.5-7b_few-shot-3",
1729	          "K": 2,
1730	          "beta": [
1731	            0.0,
1732	            1.0
1733	          ],
1734	          "sign_flip": false,
1735	          "tau_true": 1.0006875736432363,
1736	          "tau_hat": 0.45662813653905343,
1737	          "max_relbias": 0.5436856132063355,
1738	          "per_coef": [
1739	            {
1740	              "coef_idx": 1,
1741	              "true": 1.0006875736432363,
1742	              "biased": 0.45662813653905343,
1743	              "sign_flip": false
1744	            }
1745	          ],
1746	          "features": {
1747	            "K": 2,
1748	            "min_diag": 0.6787296898079763,
1749	            "mean_diag": 0.7297758038080977,
1750	            "max_off": 0.3212703101920236,
1751	            "max_off_ratio": 0.4733405875952122,
1752	            "cond": 2.2046870875055347,
1753	            "log_cond": 0.34334695851446095,
1754	            "mean_entropy": 0.832210695039356,
1755	            "max_entropy": 0.9057575271903423,
1756	            "spectral_gap": 0.5404483923838045,
1757	            "det": 0.45955160761619557,
1758	            "min_sv": 0.45655559105857724,
1759	            "sv_ratio": 2.2046870875055347
1760	          }
1761	        },
1762	        {
1763	          "config": "civil_comments_qwen2.5-7b_few-shot-5",
1764	          "K": 2,
1765	          "beta": [
1766	            0.0,
1767	            1.0
1768	          ],
1769	          "sign_flip": false,
1770	          "tau_true": 1.0006875736432363,
1771	          "tau_hat": 0.49300172165470246,
1772	          "max_relbias": 0.5073370204250516,
1773	          "per_coef": [
1774	            {
1775	              "coef_idx": 1,
1776	              "true": 1.0006875736432363,
1777	              "biased": 0.49300172165470246,
1778	              "sign_flip": false
1779	            }
1780	          ],
1781	          "features": {
1782	            "K": 2,
1783	            "min_diag": 0.7370753323485968,
1784	            "mean_diag": 0.7486746524756682,
1785	            "max_off": 0.26292466765140327,
1786	            "max_off_ratio": 0.35671342685370744,
1787	            "cond": 2.0120966711779484,
1788	            "log_cond": 0.30364884256210606,
1789	            "mean_entropy": 0.8128560597271433,
1790	            "max_entropy": 0.8311277438478006,
1791	            "spectral_gap": 0.5026506950486636,
1792	            "det": 0.4973493049513366,
1793	            "min_sv": 0.49717162744867915,
1794	            "sv_ratio": 2.0120966711779484
1795	          }
1796	        },
1797	        {
1798	          "config": "civil_comments_qwen2.5-7b_zero-shot",
1799	          "K": 2,
1800	          "beta": [
1801	            0.0,
1802	            1.0
1803	          ],
1804	          "sign_flip": false,
1805	          "tau_true": 1.0006875736432363,
1806	          "tau_hat": 0.43394147965280977,
1807	          "max_relbias": 0.5663566820631691,
1808	          "per_coef": [
1809	            {
1810	              "coef_idx": 1,
1811	              "true": 1.0006875736432363,
1812	              "biased": 0.43394147965280977,
1813	              "sign_flip": false
1814	            }
1815	          ],
1816	          "features": {
1817	            "K": 2,
1818	            "min_diag": 0.684931506849315,
1819	            "mean_diag": 0.7165425628781288,
1820	            "max_off": 0.3150684931506849,
1821	            "max_off_ratio": 0.46,
1822	            "cond": 2.320361980143194,
1823	            "log_cond": 0.3655557408029338,
1824	            "mean_entropy": 0.8565646301807837,
1825	            "max_entropy": 0.8989377852081333,
1826	            "spectral_gap": 0.5669148742437425,
1827	            "det": 0.43308512575625746,
1828	            "min_sv": 0.4320248854336829,
1829	            "sv_ratio": 2.320361980143194
1830	          }
1831	        },
1832	        {
1833	          "config": "civil_comments_qwen3_few-shot-3",
1834	          "K": 2,
1835	          "beta": [
1836	            0.0,
1837	            1.0
1838	          ],
1839	          "sign_flip": false,
1840	          "tau_true": 1.0006875736432363,
1841	          "tau_hat": 0.5669624111960679,
1842	          "max_relbias": 0.43342714936300336,
1843	          "per_coef": [
1844	            {
1845	              "coef_idx": 1,
1846	              "true": 1.0006875736432363,
1847	              "biased": 0.5669624111960679,
1848	              "sign_flip": false
1849	            }
1850	          ],
1851	          "features": {
1852	            "K": 2,
1853	            "min_diag": 0.7448275862068966,
1854	            "mean_diag": 0.7813701217488962,
1855	            "max_off": 0.25517241379310346,
1856	            "max_off_ratio": 0.34259259259259256,
1857	            "cond": 1.790859904151061,
1858	            "log_cond": 0.25306161307745983,
1859	            "mean_entropy": 0.7519979451235315,
1860	            "max_entropy": 0.8193737468292397,
1861	            "spectral_gap": 0.43725975650220783,
1862	            "det": 0.5627402434977923,
1863	            "min_sv": 0.5605613889083931,
1864	            "sv_ratio": 1.790859904151061
1865	          }
1866	        },
1867	        {
1868	          "config": "civil_comments_qwen3_few-shot-5",
1869	          "K": 2,
1870	          "beta": [
1871	            0.0,
1872	            1.0
1873	          ],
1874	          "sign_flip": false,
1875	          "tau_true": 1.0006875736432363,
1876	          "tau_hat": 0.6166639927983613,
1877	          "max_relbias": 0.3837597177775954,
1878	          "per_coef": [
1879	            {
1880	              "coef_idx": 1,
1881	              "true": 1.0006875736432363,
1882	              "biased": 0.6166639927983613,
1883	              "sign_flip": false
1884	            }
1885	          ],
1886	          "features": {
1887	            "K": 2,
1888	            "min_diag": 0.7931034482758621,
1889	            "mean_diag": 0.8085784501958375,
1890	            "max_off": 0.20689655172413793,
1891	            "max_off_ratio": 0.2608695652173913,
1892	            "cond": 1.6228381125800326,
1893	            "log_cond": 0.21027519861870325,
1894	            "mean_entropy": 0.7033187055895573,
1895	            "max_entropy": 0.7355085815538399,
1896	            "spectral_gap": 0.3828430996083251,
1897	            "det": 0.617156900391675,
1898	            "min_sv": 0.6166804707799527,
1899	            "sv_ratio": 1.6228381125800326
1900	          }
1901	        },
1902	        {
1903	          "config": "civil_comments_qwen3_zero-shot",
1904	          "K": 2,
1905	          "beta": [
1906	            0.0,
1907	            1.0
1908	          ],
1909	          "sign_flip": false,
1910	          "tau_true": 1.0006875736432363,
1911	          "tau_hat": 0.5197910616224681,
1912	          "max_relbias": 0.4805660874452077,
1913	          "per_coef": [
1914	            {
1915	              "coef_idx": 1,
1916	              "true": 1.0006875736432363,
1917	              "biased": 0.5197910616224681,
1918	              "sign_flip": false
1919	            }
1920	          ],
1921	          "features": {
1922	            "K": 2,
1923	            "min_diag": 0.7425742574257426,
1924	            "mean_diag": 0.7603464334163478,
1925	            "max_off": 0.25742574257425743,
1926	            "max_off_ratio": 0.3466666666666667,
1927	            "cond": 1.923844741767405,
1928	            "log_cond": 0.28417002065689095,
1929	            "mean_entropy": 0.7932124509685978,
1930	            "max_entropy": 0.8228368841492258,
1931	            "spectral_gap": 0.47930713316730444,
1932	            "det": 0.5206928668326956,
1933	            "min_sv": 0.5202424709655475,
1934	            "sv_ratio": 1.923844741767405
1935	          }
1936	        },
1937	        {
1938	          "config": "humaid_deepseek_few-shot-3",
1939	          "K": 10,
1940	          "beta": [
1941	            0.0,
1942	            1.0,
1943	            1.0,
1944	            1.0,
1945	            1.0,
1946	            1.0,
1947	            1.0,
1948	            1.0,
1949	            1.0,
1950	            1.0
1951	          ],
1952	          "sign_flip": false,
1953	          "tau_true": 1.0021612541230203,
1954	          "tau_hat": 0.8329540360281112,
1955	          "max_relbias": 0.8131567928818012,
1956	          "per_coef": [
1957	            {
1958	              "coef_idx": 1,
1959	              "true": 1.0021612541230203,
1960	              "biased": 0.8329540360281112,
1961	              "sign_flip": false
1962	            },
1963	            {
1964	              "coef_idx": 2,
1965	              "true": 1.0048262935212924,
1966	              "biased": 0.5767963809257919,
1967	              "sign_flip": false
1968	            },
1969	            {
1970	              "coef_idx": 3,
1971	              "true": 1.000843019556467,
1972	              "biased": 0.7902256833751901,
1973	              "sign_flip": false
1974	            },
1975	            {
1976	              "coef_idx": 4,
1977	              "true": 0.9989103775473842,
1978	              "biased": 0.8297283630162899,
1979	              "sign_flip": false
1980	            },
1981	            {
1982	              "coef_idx": 5,
1983	              "true": 1.0025766615732035,
1984	              "biased": 0.6029345907901337,
1985	              "sign_flip": false
1986	            },
1987	            {
1988	              "coef_idx": 6,
1989	              "true": 1.0012371124868509,
1990	              "biased": 0.18707435318280796,
1991	              "sign_flip": false
1992	            },
1993	            {
1994	              "coef_idx": 7,
1995	              "true": 1.003563255882479,
1996	              "biased": 0.8341554420440632,
1997	              "sign_flip": false
1998	            },
1999	            {
2000	              "coef_idx": 8,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "473169c0-38f4-481d-b8a3-61ce2e73b0b3",
  "isSidechain": true,
  "promptId": "3a998203-92b0-473c-93f5-01c622a8ef76",
  "agentId": "a9bc92f8d50dd2489",
  "type": "user",
  "uuid": "37fce301-7323-4a97-829d-1084fd865a3e",
  "sourceToolAssistantUUID": "473169c0-38f4-481d-b8a3-61ce2e73b0b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-25T20:20:25.434Z_

Perfect! I found the key information. From the sign_reversal_determinants_results.json file on lines 1-2:

```
"n_matrices": 23,
...
"n_flip": 14,
```

This is in the "default" beta configuration section. Let me now compile all the findings:

## Exact Numbers Found in Artifact Files

Based on my thorough reading of the specified artifact files, here are the exact values:

### 1. **plan007_rmse_correction_results.json** (first file read)
File path: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan007_rmse_correction_results.json`

**PPI++ (Grand Means):**
- `grand_means.ppi.bias_reduction_pct`: **93.8%**
- `grand_means.ppi.rmse_reduction_pct`: **47.0%**

**PPI++ by Topology:**
- confounding: `rmse_reduction_pct: 83.2`, `bias_reduction_pct: 99.3`
- mediation: `rmse_reduction_pct: 54.1`, `bias_reduction_pct: 98.8`
- collider: `rmse_reduction_pct: 50.5`, `bias_reduction_pct: 97.0`
- exposure: `rmse_reduction_pct: 75.5`, `bias_reduction_pct: 98.8`
- **mbias**: `rmse_reduction_pct: -88.0`, `bias_reduction_pct: 63.7`
- iv: `rmse_reduction_pct: 79.4`, `bias_reduction_pct: 99.5`
- frontdoor: `rmse_reduction_pct: 74.1`, `bias_reduction_pct: 99.3`

**MC-SIMEX by Topology:**
- frontdoor: `rmse_reduction_pct: -62.4`, `bias_reduction_pct: -55.7`
- **mbias**: `rmse_reduction_pct: 0.1`, `bias_reduction_pct: 25.7`

### 2. **plan007/correction_guidance_results.json** (second file - partially read)
File path: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan007/correction_guidance_results.json`

Same values as above (this is the source data)

### 3. **table3_source_data.txt**
File path: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/table3_source_data.txt`

**Key Discrepancies vs. Paper (lines 40-59):**
- MC-SIMEX frontdoor: Paper `8.7` vs JSON `-55.7` **SIGN FLIP** (delta: -64.4)
- MC-SIMEX exposure: Paper `1.0` vs JSON `-3.8` **SIGN FLIP** (delta: -4.8)
- MC-SIMEX mediation: Paper `24.6` vs JSON `42.4` (delta: +17.8)
- MC-SIMEX mbias: Paper `5.1` vs JSON `25.7` (delta: +20.6)

**ASV-Unsafe Summary (line 515):**
- Total ASV-unsafe: **31 out of 63** (49.2%)

### 4. **adversarial_monotonicity_results.json**
File path: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json`

**Maximum Epsilon Values:**
- Overall `max_eps_abs`: **0.01636529529573094**
- By topology:
  - confounding: `0.01636529529573094` (max)
  - mediation: `0.013039414209438105`
  - collider: `0.013176775652375183`
  - exposure: `0.008412534039272668`
  - mbias: `0.001532019782881644`
  - iv: `0.0`
  - frontdoor: `0.01582784663255976`

### 5. **conjecture1_extended_results.json**
File path: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture1_extended_results.json`

Contains conjecture verification data but no specific epsilon values related to sign reversal.

### 6. **exp_fwl_nonlinear_scaling_results.json**
File path: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_fwl_nonlinear_scaling_results.json`

The file contains 72 result records comparing logistic vs linear bias reduction percentages across topologies. Some example deltas:
- confounding/N=1000/error_level=low: logistic `0.0004...` vs linear `−2.942e-17` (trivial difference)
- exposure/N=1000/error_level=low: logistic `-0.436...` vs linear `-0.0384...` (delta ~0.40)
- exposure results consistently show substantial logistic vs linear differences

### 7. **sign_reversal_determinants_results.json**
File path: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/sign_reversal_determinants_results.json`

**Sign Reversal Results (line 2):**
- `n_matrices`: **23**
- `n_flip` (default beta): **14 out of 23** (**60.9%** of configurations show sign flip)

This is the **"14 out of 23"** claim you were searching for.

### 8. **82% ASV Stability Claim**
Not found in the files searched. The closest match is from plan006_exact_values.txt which shows "ppi_recommended_pct: 49.2063492063492" but does not mention 82% or ASV stability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37fce301-7323-4a97-829d-1084fd865a3e",
  "isSidechain": true,
  "agentId": "a9bc92f8d50dd2489",
  "requestId": "req_011CbPuaczFcdQJWEKtbYGeJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8d079af6-9211-48ac-b37b-408373e7a2d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "1cd58481-3fc5-48ed-8b46-f89ca98273ac",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "frolicking-floating-garden",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012u4gWdVra6DAZHr3wDUALt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 28852,
      "cache_read_input_tokens": 106856,
      "output_tokens": 1557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28852
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1557,
          "cache_read_input_tokens": 106856,
          "cache_creation_input_tokens": 28852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28852,
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
