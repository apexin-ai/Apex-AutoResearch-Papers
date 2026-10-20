# Research conversation: Read the following JSON artifact files completely and report their full contents: 1. /home/ubuntu/.agent-ml-research-pro

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a767a9abec38e8eae.jsonl`
- **Structured JSON:** [`1c52657e17f664e9456d.json`](../../sessions/1c/1c52657e17f664e9456d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

9 recorded events

### User

_source line 1 · 2026-05-23T19:22:02.463Z_

Read the following JSON artifact files completely and report their full contents:

1. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_proportional_effects_results.json
2. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_results.json
3. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_b_logistic_results.json

Report the complete JSON structure and all values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6231d775-db71-46d9-bac6-397081d485cb",
  "agentId": "a767a9abec38e8eae",
  "type": "user",
  "uuid": "9f920d36-c094-4793-a698-0309aaeb125d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T19:22:03.613Z_

I'll read those three JSON files for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f920d36-c094-4793-a698-0309aaeb125d",
  "isSidechain": true,
  "agentId": "a767a9abec38e8eae",
  "requestId": "req_011CbL3XisJDWw82QoUQ1ugX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "86a34eb9-e437-4ad2-8eef-8e2659c940c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Ki5qtWZPFwKT9vBxLtF12",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 17330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 584,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 3 · 2026-05-23T19:22:04.049Z_

<details open><summary>🔧 Tool call — Read · `toolu_016NpUHtejmyPFsmHw1PLw2K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_proportional_effects_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86a34eb9-e437-4ad2-8eef-8e2659c940c4",
  "isSidechain": true,
  "agentId": "a767a9abec38e8eae",
  "requestId": "req_011CbL3XisJDWw82QoUQ1ugX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "438ad114-b63c-47dc-b90d-f3033d26ef2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Ki5qtWZPFwKT9vBxLtF12",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 17330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 584,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 4 · 2026-05-23T19:22:04.055Z_

<details><summary>↩ Tool result · `toolu_016NpUHtejmyPFsmHw1PLw2K`</summary>

```text
1	{
2	  "metadata": {
3	    "K": 3,
4	    "n_configs": 100000,
5	    "seed": 42,
6	    "sigma_values": [
7	      0.1,
8	      0.3,
9	      0.5
10	    ],
11	    "method": "synthetic_suff_stats",
12	    "proportionality_condition": "f_j - f_0 = lambda * g_j for j=1,...,K-1",
13	    "p_A": [
14	      0.4,
15	      0.35,
16	      0.25
17	    ],
18	    "timestamp": "2026-05-23 02:12:46"
19	  },
20	  "results": [
21	    {
22	      "degree": "exact_proportional",
23	      "n_configs": 100000,
24	      "valid": 99690,
25	      "skipped": 310,
26	      "lambda_oob_count": 0,
27	      "lambda_oob_rate": 0.0,
28	      "sign_failure_count": 844,
29	      "sign_failure_rate": 0.008466245360617915,
30	      "lambda_mean": 0.15551467054923265,
31	      "lambda_std": 0.13150281432551328,
32	      "lambda_median": 0.12069559503848981,
33	      "lambda_q05": 0.009488260447169357,
34	      "lambda_q95": 0.41925302387858127,
35	      "lambda_min": 6.755466737451421e-06,
36	      "lambda_max": 0.9299870923896153,
37	      "n_lambda_finite": 99690,
38	      "description": "f_j - f_0 = lambda * g_j, lambda ~ U(0.1, 0.5)"
39	    },
40	    {
41	      "degree": "near_proportional_sigma_0.1",
42	      "n_configs": 100000,
43	      "valid": 99404,
44	      "skipped": 596,
45	      "lambda_oob_count": 10218,
46	      "lambda_oob_rate": 0.10279264415918876,
47	      "sign_failure_count": 865,
48	      "sign_failure_rate": 0.008701863104100439,
49	      "lambda_mean": 0.26284610982695505,
50	      "lambda_std": 34.86377287863551,
51	      "lambda_median": 0.11477809839461406,
52	      "lambda_q05": -0.04496670830380808,
53	      "lambda_q95": 0.5040708608094052,
54	      "lambda_min": -401.29102036673066,
55	      "lambda_max": 10939.393415232453,
56	      "n_lambda_finite": 99404,
57	      "description": "f_j - f_0 = lambda*g_j + eps, eps ~ N(0, 0.1^2)",
58	      "sigma": 0.1
59	    },
60	    {
61	      "degree": "near_proportional_sigma_0.3",
62	      "n_configs": 100000,
63	      "valid": 89843,
64	      "skipped": 10157,
65	      "lambda_oob_count": 17107,
66	      "lambda_oob_rate": 0.19040993733512906,
67	      "sign_failure_count": 860,
68	      "sign_failure_rate": 0.009572253820553633,
69	      "lambda_mean": 0.1483101563407438,
70	      "lambda_std": 11.337335837363911,
71	      "lambda_median": 0.10367801971912238,
72	      "lambda_q05": -0.23044065432275102,
73	      "lambda_q95": 0.6201095477596448,
74	      "lambda_min": -965.0306183242983,
75	      "lambda_max": 2712.7090482079225,
76	      "n_lambda_finite": 89843,
77	      "description": "f_j - f_0 = lambda*g_j + eps, eps ~ N(0, 0.3^2)",
78	      "sigma": 0.3
79	    },
80	    {
81	      "degree": "near_proportional_sigma_0.5",
82	      "n_configs": 100000,
83	      "valid": 65948,
84	      "skipped": 34052,
85	      "lambda_oob_count": 14770,
86	      "lambda_oob_rate": 0.22396433553708983,
87	      "sign_failure_count": 612,
88	      "sign_failure_rate": 0.00928003881846303,
89	      "lambda_mean": 0.06862851842613471,
90	      "lambda_std": 17.830869693740084,
91	      "lambda_median": 0.09716498869177981,
92	      "lambda_q05": -0.3116642058757656,
93	      "lambda_q95": 0.6747266203496175,
94	      "lambda_min": -3893.876360713489,
95	      "lambda_max": 672.5871593893548,
96	      "n_lambda_finite": 65948,
97	      "description": "f_j - f_0 = lambda*g_j + eps, eps ~ N(0, 0.5^2)",
98	      "sigma": 0.5
99	    },
100	    {
101	      "degree": "independent",
102	      "n_configs": 100000,
103	      "valid": 100000,
104	      "skipped": 0,
105	      "lambda_oob_count": 22949,
106	      "lambda_oob_rate": 0.22949,
107	      "sign_failure_count": 173,
108	      "sign_failure_rate": 0.00173,
109	      "lambda_mean": 0.16032158875613878,
110	      "lambda_std": 24.939570514390176,
111	      "lambda_median": 0.11208323550226373,
112	      "lambda_q05": -0.35913052188992595,
113	      "lambda_q95": 0.7590588104218954,
114	      "lambda_min": -6434.843210196369,
115	      "lambda_max": 2580.3155767833578,
116	      "n_lambda_finite": 100000,
117	      "description": "f independent of g, f[k] ~ N(0.5, 0.15^2)"
118	    },
119	    {
120	      "degree": "default_plan006",
121	      "description": "Fixed plan_006 params: delta=[0.0, 0.8, -0.6], beta=[0.0, 1.0, -0.5]",
122	      "n_configs": 100000,
123	      "valid": 100000,
124	      "skipped": 0,
125	      "lambda_oob_count": 66,
126	      "lambda_oob_rate": 0.00066,
127	      "sign_failure_count": 0,
128	      "sign_failure_rate": 0.0,
129	      "lambda_mean": 0.1640777580850805,
130	      "lambda_std": 0.13450102368330724,
131	      "lambda_median": 0.13024483942217024,
132	      "lambda_q05": 0.010678660218905815,
133	      "lambda_q95": 0.43145581837249686,
134	      "lambda_min": -0.00027590183442427474,
135	      "lambda_max": 0.8390486945030019,
136	      "n_lambda_finite": 100000,
137	      "tau_true": 0.49933571225320145,
138	      "tau_total": 0.8045467469704967,
139	      "tau_indirect": 0.3052110347172952
140	    }
141	  ]
142	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "438ad114-b63c-47dc-b90d-f3033d26ef2d",
  "isSidechain": true,
  "promptId": "6231d775-db71-46d9-bac6-397081d485cb",
  "agentId": "a767a9abec38e8eae",
  "type": "user",
  "uuid": "66889a4a-6e9d-4e2e-a656-51356216c29f",
  "sourceToolAssistantUUID": "438ad114-b63c-47dc-b90d-f3033d26ef2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T19:22:04.260Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TKYZrSfTcrzu97rwkfHVqK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66889a4a-6e9d-4e2e-a656-51356216c29f",
  "isSidechain": true,
  "agentId": "a767a9abec38e8eae",
  "requestId": "req_011CbL3XisJDWw82QoUQ1ugX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb5af16d-caf0-456b-9639-0f83adb5bf29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Ki5qtWZPFwKT9vBxLtF12",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 17330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 584,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 6 · 2026-05-23T19:22:04.407Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Dzs8AqLvzK4xsw3V3wt9Gv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_b_logistic_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb5af16d-caf0-456b-9639-0f83adb5bf29",
  "isSidechain": true,
  "agentId": "a767a9abec38e8eae",
  "requestId": "req_011CbL3XisJDWw82QoUQ1ugX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3181dd62-555d-45a2-8404-f8073fd27a0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016Ki5qtWZPFwKT9vBxLtF12",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 17330,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 584
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 257,
          "cache_read_input_tokens": 17330,
          "cache_creation_input_tokens": 584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 584,
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

_source line 7 · 2026-05-23T19:22:04.657Z_

<details><summary>↩ Tool result · `toolu_01Dzs8AqLvzK4xsw3V3wt9Gv`</summary>

```text
1	{
2	  "results": [
3	    {
4	      "topology": "confounding",
5	      "cm_name": "deepseek_zero-shot",
6	      "model": "logistic",
7	      "sign_flip_rate": 0.564,
8	      "tau_sign_flip_rate": 0.0,
9	      "dummy_sign_flip_rate": 0.564,
10	      "mean_bias": 0.39057153550515505,
11	      "coef_means": [
12	        0.5096433280111479,
13	        0.18281167675270604,
14	        0.01065739425547251
15	      ],
16	      "true_coefs": [
17	        0.41638484019002725,
18	        0.8361038268454802,
19	        -0.41450657434609767
20	      ],
21	      "n_valid": 500
22	    },
23	    {
24	      "topology": "confounding",
25	      "cm_name": "deepseek_zero-shot",
26	      "model": "linear",
27	      "sign_flip_rate": 0.562,
28	      "tau_sign_flip_rate": 0.0,
29	      "dummy_sign_flip_rate": 0.562,
30	      "mean_bias": 0.09001458721801596,
31	      "coef_means": [
32	        0.11842692947525706,
33	        0.04244918321043737,
34	        0.002495111879796136
35	      ],
36	      "true_coefs": [
37	        0.0931430096052067,
38	        0.18609937231088194,
39	        -0.09861454080375684
40	      ],
41	      "n_valid": 500
42	    },
43	    {
44	      "topology": "confounding",
45	      "cm_name": "llama4_few-shot-3",
46	      "model": "logistic",
47	      "sign_flip_rate": 0.544,
48	      "tau_sign_flip_rate": 0.0,
49	      "dummy_sign_flip_rate": 0.544,
50	      "mean_bias": 0.3780412034572263,
51	      "coef_means": [
52	        0.5059664085994415,
53	        0.23440140776692725,
54	        0.02833304853761438
55	      ],
56	      "true_coefs": [
57	        0.41638484019002725,
58	        0.8361038268454802,
59	        -0.41450657434609767
60	      ],
61	      "n_valid": 500
62	    },
63	    {
64	      "topology": "confounding",
65	      "cm_name": "llama4_few-shot-3",
66	      "model": "linear",
67	      "sign_flip_rate": 0.584,
68	      "tau_sign_flip_rate": 0.0,
69	      "dummy_sign_flip_rate": 0.584,
70	      "mean_bias": 0.08704604746263836,
71	      "coef_means": [
72	        0.11745300272193196,
73	        0.05449522151081023,
74	        0.006609457667361356
75	      ],
76	      "true_coefs": [
77	        0.0931430096052067,
78	        0.18609937231088194,
79	        -0.09861454080375684
80	      ],
81	      "n_valid": 500
82	    },
83	    {
84	      "topology": "confounding",
85	      "cm_name": "llama4_few-shot-5",
86	      "model": "logistic",
87	      "sign_flip_rate": 0.004,
88	      "tau_sign_flip_rate": 0.0,
89	      "dummy_sign_flip_rate": 0.004,
90	      "mean_bias": 0.290608361528885,
91	      "coef_means": [
92	        0.5007684699219188,
93	        0.25391037629981733,
94	        -0.2092677604726442
95	      ],
96	      "true_coefs": [
97	        0.41638484019002725,
98	        0.8361038268454802,
99	        -0.41450657434609767
100	      ],
101	      "n_valid": 500
102	    },
103	    {
104	      "topology": "confounding",
105	      "cm_name": "llama4_few-shot-5",
106	      "model": "linear",
107	      "sign_flip_rate": 0.004,
108	      "tau_sign_flip_rate": 0.0,
109	      "dummy_sign_flip_rate": 0.004,
110	      "mean_bias": 0.06640765682336763,
111	      "coef_means": [
112	        0.1159681745940989,
113	        0.059113685130963274,
114	        -0.0492024225024649
115	      ],
116	      "true_coefs": [
117	        0.0931430096052067,
118	        0.18609937231088194,
119	        -0.09861454080375684
120	      ],
121	      "n_valid": 500
122	    },
123	    {
124	      "topology": "confounding",
125	      "cm_name": "llama4_zero-shot",
126	      "model": "logistic",
127	      "sign_flip_rate": 0.474,
128	      "tau_sign_flip_rate": 0.0,
129	      "dummy_sign_flip_rate": 0.474,
130	      "mean_bias": 0.35788999813185357,
131	      "coef_means": [
132	        0.5030173697720763,
133	        0.2645253934858232,
134	        0.0009524571077568839
135	      ],
136	      "true_coefs": [
137	        0.41638484019002725,
138	        0.8361038268454802,
139	        -0.41450657434609767
140	      ],
141	      "n_valid": 500
142	    },
143	    {
144	      "topology": "confounding",
145	      "cm_name": "llama4_zero-shot",
146	      "model": "linear",
147	      "sign_flip_rate": 0.514,
148	      "tau_sign_flip_rate": 0.0,
149	      "dummy_sign_flip_rate": 0.514,
150	      "mean_bias": 0.08229636081981168,
151	      "coef_means": [
152	        0.1166508216707085,
153	        0.061531638763082985,
154	        0.00019899604237744658
155	      ],
156	      "true_coefs": [
157	        0.0931430096052067,
158	        0.18609937231088194,
159	        -0.09861454080375684
160	      ],
161	      "n_valid": 500
162	    },
163	    {
164	      "topology": "confounding",
165	      "cm_name": "qwen2.5-7b_few-shot-3",
166	      "model": "logistic",
167	      "sign_flip_rate": 0.836,
168	      "tau_sign_flip_rate": 0.0,
169	      "dummy_sign_flip_rate": 0.836,
170	      "mean_bias": 0.40490021580520175,
171	      "coef_means": [
172	        0.5095141791899803,
173	        0.19960275091792062,
174	        0.07056365814199442
175	      ],
176	      "true_coefs": [
177	        0.41638484019002725,
178	        0.8361038268454802,
179	        -0.41450657434609767
180	      ],
181	      "n_valid": 500
182	    },
183	    {
184	      "topology": "confounding",
185	      "cm_name": "qwen2.5-7b_few-shot-3",
186	      "model": "linear",
187	      "sign_flip_rate": 0.838,
188	      "tau_sign_flip_rate": 0.0,
189	      "dummy_sign_flip_rate": 0.838,
190	      "mean_bias": 0.09334102063552566,
191	      "coef_means": [
192	        0.11836468531774856,
193	        0.04652740709417855,
194	        0.016614880173574927
195	      ],
196	      "true_coefs": [
197	        0.0931430096052067,
198	        0.18609937231088194,
199	        -0.09861454080375684
200	      ],
201	      "n_valid": 500
202	    },
203	    {
204	      "topology": "confounding",
205	      "cm_name": "qwen2.5-7b_few-shot-5",
206	      "model": "logistic",
207	      "sign_flip_rate": 0.934,
208	      "tau_sign_flip_rate": 0.0,
209	      "dummy_sign_flip_rate": 0.934,
210	      "mean_bias": 0.41585860231878186,
211	      "coef_means": [
212	        0.5083946373599092,
213	        0.1968528680860709,
214	        0.10180847668095656
215	      ],
216	      "true_coefs": [
217	        0.41638484019002725,
218	        0.8361038268454802,
219	        -0.41450657434609767
220	      ],
221	      "n_valid": 500
222	    },
223	    {
224	      "topology": "confounding",
225	      "cm_name": "qwen2.5-7b_few-shot-5",
226	      "model": "linear",
227	      "sign_flip_rate": 0.934,
228	      "tau_sign_flip_rate": 0.0,
229	      "dummy_sign_flip_rate": 0.934,
230	      "mean_bias": 0.09592111072500126,
231	      "coef_means": [
232	        0.11814447826866789,
233	        0.045889087212365544,
234	        0.023937037609269345
235	      ],
236	      "true_coefs": [
237	        0.0931430096052067,
238	        0.18609937231088194,
239	        -0.09861454080375684
240	      ],
241	      "n_valid": 500
242	    },
243	    {
244	      "topology": "mediation",
245	      "cm_name": "deepseek_zero-shot",
246	      "model": "logistic",
247	      "sign_flip_rate": 0.86,
248	      "tau_sign_flip_rate": 0.0,
249	      "dummy_sign_flip_rate": 0.86,
250	      "mean_bias": 0.416659750810675,
251	      "coef_means": [
252	        0.6399118762374627,
253	        0.30720812599894975,
254	        0.08266705671633577
255	      ],
256	      "true_coefs": [
257	        0.41810133700251345,
258	        0.8374399824986839,
259	        -0.4152697999810058
260	      ],
261	      "n_valid": 500
262	    },
263	    {
264	      "topology": "mediation",
265	      "cm_name": "deepseek_zero-shot",
266	      "model": "linear",
267	      "sign_flip_rate": 0.86,
268	      "tau_sign_flip_rate": 0.0,
269	      "dummy_sign_flip_rate": 0.86,
270	      "mean_bias": 0.09854995733610364,
271	      "coef_means": [
272	        0.14377948194826098,
273	        0.0698479245458042,
274	        0.01941616269675889
275	      ],
276	      "true_coefs": [
277	        0.08888487434071951,
278	        0.18700969432033765,
279	        -0.10417733192947722
280	      ],
281	      "n_valid": 500
282	    },
283	    {
284	      "topology": "mediation",
285	      "cm_name": "llama4_few-shot-3",
286	      "model": "logistic",
287	      "sign_flip_rate": 0.712,
288	      "tau_sign_flip_rate": 0.0,
289	      "dummy_sign_flip_rate": 0.712,
290	      "mean_bias": 0.40112049283437645,
291	      "coef_means": [
292	        0.6318779211719131,
293	        0.35270501696177303,
294	        0.08958012881581302
295	      ],
296	      "true_coefs": [
297	        0.41810133700251345,
298	        0.8374399824986839,
299	        -0.4152697999810058
300	      ],
301	      "n_valid": 500
302	    },
303	    {
304	      "topology": "mediation",
305	      "cm_name": "llama4_few-shot-3",
306	      "model": "linear",
307	      "sign_flip_rate": 0.742,
308	      "tau_sign_flip_rate": 0.0,
309	      "dummy_sign_flip_rate": 0.742,
310	      "mean_bias": 0.09495993444511006,
311	      "coef_means": [
312	        0.14168644780631565,
313	        0.07981782150306999,
314	        0.0207090251229892
315	      ],
316	      "true_coefs": [
317	        0.08888487434071951,
318	        0.18700969432033765,
319	        -0.10417733192947722
320	      ],
321	      "n_valid": 500
322	    },
323	    {
324	      "topology": "mediation",
325	      "cm_name": "llama4_few-shot-5",
326	      "model": "logistic",
327	      "sign_flip_rate": 0.0,
328	      "tau_sign_flip_rate": 0.0,
329	      "dummy_sign_flip_rate": 0.0,
330	      "mean_bias": 0.2625783473952723,
331	      "coef_means": [
332	        0.6136513619392783,
333	        0.38657475401735686,
334	        -0.27998601410929685
335	      ],
336	      "true_coefs": [
337	        0.41810133700251345,
338	        0.8374399824986839,
339	        -0.4152697999810058
340	      ],
341	      "n_valid": 500
342	    },
343	    {
344	      "topology": "mediation",
345	      "cm_name": "llama4_few-shot-5",
346	      "model": "linear",
347	      "sign_flip_rate": 0.0,
348	      "tau_sign_flip_rate": 0.0,
349	      "dummy_sign_flip_rate": 0.0,
350	      "mean_bias": 0.06132705337463841,
351	      "coef_means": [
352	        0.1369910353069612,
353	        0.08759911160174952,
354	        -0.06885144849490826
355	      ],
356	      "true_coefs": [
357	        0.08888487434071951,
358	        0.18700969432033765,
359	        -0.10417733192947722
360	      ],
361	      "n_valid": 500
362	    },
363	    {
364	      "topology": "mediation",
365	      "cm_name": "llama4_zero-shot",
366	      "model": "logistic",
367	      "sign_flip_rate": 0.61,
368	      "tau_sign_flip_rate": 0.0,
369	      "dummy_sign_flip_rate": 0.61,
370	      "mean_bias": 0.36459172438707793,
371	      "coef_means": [
372	        0.6217913790323221,
373	        0.4069972362939505,
374	        0.04437258494568624
375	      ],
376	      "true_coefs": [
377	        0.41810133700251345,
378	        0.8374399824986839,
379	        -0.4152697999810058
380	      ],
381	      "n_valid": 500
382	    },
383	    {
384	      "topology": "mediation",
385	      "cm_name": "llama4_zero-shot",
386	      "model": "linear",
387	      "sign_flip_rate": 0.628,
388	      "tau_sign_flip_rate": 0.0,
389	      "dummy_sign_flip_rate": 0.628,
390	      "mean_bias": 0.0864046207111982,
391	      "coef_means": [
392	        0.13924523705437786,
393	        0.09262152842912572,
394	        0.010288001599247094
395	      ],
396	      "true_coefs": [
397	        0.08888487434071951,
398	        0.18700969432033765,
399	        -0.10417733192947722
400	      ],
401	      "n_valid": 500
402	    },
403	    {
404	      "topology": "mediation",
405	      "cm_name": "qwen2.5-7b_few-shot-3",
406	      "model": "logistic",
407	      "sign_flip_rate": 0.988,
408	      "tau_sign_flip_rate": 0.0,
409	      "dummy_sign_flip_rate": 0.988,
410	      "mean_bias": 0.4352168745182189,
411	      "coef_means": [
412	        0.6427880848226406,
413	        0.3466325530919133,
414	        0.1748866463467532
415	      ],
416	      "true_coefs": [
417	        0.41810133700251345,
418	        0.8374399824986839,
419	        -0.4152697999810058
420	      ],
421	      "n_valid": 500
422	    },
423	    {
424	      "topology": "mediation",
425	      "cm_name": "qwen2.5-7b_few-shot-3",
426	      "model": "linear",
427	      "sign_flip_rate": 0.988,
428	      "tau_sign_flip_rate": 0.0,
429	      "dummy_sign_flip_rate": 0.988,
430	      "mean_bias": 0.10276669429258475,
431	      "coef_means": [
432	        0.14435817328464315,
433	        0.07947966661916218,
434	        0.041119424303177936
435	      ],
436	      "true_coefs": [
437	        0.08888487434071951,
438	        0.18700969432033765,
439	        -0.10417733192947722
440	      ],
441	      "n_valid": 500
442	    },
443	    {
444	      "topology": "mediation",
445	      "cm_name": "qwen2.5-7b_few-shot-5",
446	      "model": "logistic",
447	      "sign_flip_rate": 1.0,
448	      "tau_sign_flip_rate": 0.0,
449	      "dummy_sign_flip_rate": 1.0,
450	      "mean_bias": 0.4492148267320298,
451	      "coef_means": [
452	        0.6373094232679455,
453	        0.33267168391565893,
454	        0.20839829536662607
455	      ],
456	      "true_coefs": [
457	        0.41810133700251345,
458	        0.8374399824986839,
459	        -0.4152697999810058
460	      ],
461	      "n_valid": 500
462	    },
463	    {
464	      "topology": "mediation",
465	      "cm_name": "qwen2.5-7b_few-shot-5",
466	      "model": "linear",
467	      "sign_flip_rate": 1.0,
468	      "tau_sign_flip_rate": 0.0,
469	      "dummy_sign_flip_rate": 1.0,
470	      "mean_bias": 0.10599369211565086,
471	      "coef_means": [
472	        0.14318015105034004,
473	        0.076027730785241,
474	        0.04852650417275823
475	      ],
476	      "true_coefs": [
477	        0.08888487434071951,
478	        0.18700969432033765,
479	        -0.10417733192947722
480	      ],
481	      "n_valid": 500
482	    },
483	    {
484	      "topology": "collider",
485	      "cm_name": "deepseek_zero-shot",
486	      "model": "logistic",
487	      "sign_flip_rate": 0.0,
488	      "tau_sign_flip_rate": 0.0,
489	      "dummy_sign_flip_rate": 0.0,
490	      "mean_bias": 0.293049619493939,
491	      "coef_means": [
492	        0.40815802453815553,
493	        0.34587976873778165,
494	        0.20060155460308268
495	      ],
496	      "true_coefs": [
497	        0.3708255284760652,
498	        0.7942498981279285,
499	        0.5935002568689364
500	      ],
501	      "n_valid": 500
502	    },
503	    {
504	      "topology": "collider",
505	      "cm_name": "deepseek_zero-shot",
506	      "model": "linear",
507	      "sign_flip_rate": 0.0,
508	      "tau_sign_flip_rate": 0.0,
509	      "dummy_sign_flip_rate": 0.0,
510	      "mean_bias": 0.06982581242821842,
511	      "coef_means": [
512	        0.09748479084378256,
513	        0.08285825979463275,
514	        0.04791381711889758
515	      ],
516	      "true_coefs": [
517	        0.08701000898472552,
518	        0.18969994005002871,
519	        0.14004209767109965
520	      ],
521	      "n_valid": 500
522	    },
523	    {
524	      "topology": "collider",
525	      "cm_name": "llama4_few-shot-3",
526	      "model": "logistic",
527	      "sign_flip_rate": 0.156,
528	      "tau_sign_flip_rate": 0.0,
529	      "dummy_sign_flip_rate": 0.156,
530	      "mean_bias": 0.35039328082248355,
531	      "coef_means": [
532	        0.4050287819007965,
533	        0.24246131351552233,
534	        0.12930592415171546
535	      ],
536	      "true_coefs": [
537	        0.3708255284760652,
538	        0.7942498981279285,
539	        0.5935002568689364
540	      ],
541	      "n_valid": 500
542	    },
543	    {
544	      "topology": "collider",
545	      "cm_name": "llama4_few-shot-3",
546	      "model": "linear",
547	      "sign_flip_rate": 0.158,
548	      "tau_sign_flip_rate": 0.0,
549	      "dummy_sign_flip_rate": 0.158,
550	      "mean_bias": 0.08345678736662361,
551	      "coef_means": [
552	        0.09689274702559104,
553	        0.058308179612640856,
554	        0.031017396638376018
555	      ],
556	      "true_coefs": [
557	        0.08701000898472552,
558	        0.18969994005002871,
559	        0.14004209767109965
560	      ],
561	      "n_valid": 500
562	    },
563	    {
564	      "topology": "collider",
565	      "cm_name": "llama4_few-shot-5",
566	      "model": "logistic",
567	      "sign_flip_rate": 0.0,
568	      "tau_sign_flip_rate": 0.0,
569	      "dummy_sign_flip_rate": 0.0,
570	      "mean_bias": 0.3009641987821151,
571	      "coef_means": [
572	        0.40686090646752726,
573	        0.291014327731214,
574	        0.23027532393397793
575	      ],
576	      "true_coefs": [
577	        0.3708255284760652,
578	        0.7942498981279285,
579	        0.5935002568689364
580	      ],
581	      "n_valid": 500
582	    },
583	    {
584	      "topology": "collider",
585	      "cm_name": "llama4_few-shot-5",
586	      "model": "linear",
587	      "sign_flip_rate": 0.0,
588	      "tau_sign_flip_rate": 0.0,
589	      "dummy_sign_flip_rate": 0.0,
590	      "mean_bias": 0.07169371022595762,
591	      "coef_means": [
592	        0.09723275945855998,
593	        0.06984086313496175,
594	        0.05506162836601066
595	      ],
596	      "true_coefs": [
597	        0.08701000898472552,
598	        0.18969994005002871,
599	        0.14004209767109965
600	      ],
601	      "n_valid": 500
602	    },
603	    {
604	      "topology": "collider",
605	      "cm_name": "llama4_zero-shot",
606	      "model": "logistic",
607	      "sign_flip_rate": 0.118,
608	      "tau_sign_flip_rate": 0.0,
609	      "dummy_sign_flip_rate": 0.118,
610	      "mean_bias": 0.32895701628959007,
611	      "coef_means": [
612	        0.40070882567946775,
613	        0.26930384248591677,
614	        0.16263868692649108
615	      ],
616	      "true_coefs": [
617	        0.3708255284760652,
618	        0.7942498981279285,
619	        0.5935002568689364
620	      ],
621	      "n_valid": 500
622	    },
623	    {
624	      "topology": "collider",
625	      "cm_name": "llama4_zero-shot",
626	      "model": "linear",
627	      "sign_flip_rate": 0.118,
628	      "tau_sign_flip_rate": 0.0,
629	      "dummy_sign_flip_rate": 0.118,
630	      "mean_bias": 0.07827685247188537,
631	      "coef_means": [
632	        0.09582819694805543,
633	        0.06477889968265196,
634	        0.03902526898933293
635	      ],
636	      "true_coefs": [
637	        0.08701000898472552,
638	        0.18969994005002871,
639	        0.14004209767109965
640	      ],
641	      "n_valid": 500
642	    },
643	    {
644	      "topology": "collider",
645	      "cm_name": "qwen2.5-7b_few-shot-3",
646	      "model": "logistic",
647	      "sign_flip_rate": 0.062,
648	      "tau_sign_flip_rate": 0.0,
649	      "dummy_sign_flip_rate": 0.062,
650	      "mean_bias": 0.35108505516461946,
651	      "coef_means": [
652	        0.40782010656770135,
653	        0.24600640817796154,
654	        0.12654042959521
655	      ],
656	      "true_coefs": [
657	        0.3708255284760652,
658	        0.7942498981279285,
659	        0.5935002568689364
660	      ],
661	      "n_valid": 500
662	    },
663	    {
664	      "topology": "collider",
665	      "cm_name": "qwen2.5-7b_few-shot-3",
666	      "model": "linear",
667	      "sign_flip_rate": 0.062,
668	      "tau_sign_flip_rate": 0.0,
669	      "dummy_sign_flip_rate": 0.062,
670	      "mean_bias": 0.08370731104859143,
671	      "coef_means": [
672	        0.0976372769116862,
673	        0.059021258018508535,
674	        0.030308047471792436
675	      ],
676	      "true_coefs": [
677	        0.08701000898472552,
678	        0.18969994005002871,
679	        0.14004209767109965
680	      ],
681	      "n_valid": 500
682	    },
683	    {
684	      "topology": "collider",
685	      "cm_name": "qwen2.5-7b_few-shot-5",
686	      "model": "logistic",
687	      "sign_flip_rate": 0.024,
688	      "tau_sign_flip_rate": 0.0,
689	      "dummy_sign_flip_rate": 0.024,
690	      "mean_bias": 0.3427043859578216,
691	      "coef_means": [
692	        0.40892664515680505,
693	        0.2442265285202972,
694	        0.15419189498023206
695	      ],
696	      "true_coefs": [
697	        0.3708255284760652,
698	        0.7942498981279285,
699	        0.5935002568689364
700	      ],
701	      "n_valid": 500
702	    },
703	    {
704	      "topology": "collider",
705	      "cm_name": "qwen2.5-7b_few-shot-5",
706	      "model": "linear",
707	      "sign_flip_rate": 0.024,
708	      "tau_sign_flip_rate": 0.0,
709	      "dummy_sign_flip_rate": 0.024,
710	      "mean_bias": 0.08168764739788453,
711	      "coef_means": [
712	        0.09786553723933952,
713	        0.058612867814936596,
714	        0.03698066611474906
715	      ],
716	      "true_coefs": [
717	        0.08701000898472552,
718	        0.18969994005002871,
719	        0.14004209767109965
720	      ],
721	      "n_valid": 500
722	    },
723	    {
724	      "topology": "exposure",
725	      "cm_name": "deepseek_zero-shot",
726	      "model": "logistic",
727	      "sign_flip_rate": 0.496,
728	      "tau_sign_flip_rate": 0.0,
729	      "dummy_sign_flip_rate": 0.496,
730	      "mean_bias": 0.5201740720174949,
731	      "coef_means": [
732	        0.20096776781739076,
733	        -0.000698729025986386
734	      ],
735	      "true_coefs": [
736	        0.831039083609622,
737	        -0.41097555726874485
738	      ],
739	      "n_valid": 500
740	    },
741	    {
742	      "topology": "exposure",
743	      "cm_name": "deepseek_zero-shot",
744	      "model": "linear",
745	      "sign_flip_rate": 0.5,
746	      "tau_sign_flip_rate": 0.0,
747	      "dummy_sign_flip_rate": 0.5,
748	      "mean_bias": 0.12395946902072728,
749	      "coef_means": [
750	        0.049783522950215785,
751	        -0.00015955776487526274
752	      ],
753	      "true_coefs": [
754	        0.1965173689601053,
755	        -0.10134464979644023
756	      ],
757	      "n_valid": 500
758	    },
759	    {
760	      "topology": "exposure",
761	      "cm_name": "llama4_few-shot-3",
762	      "model": "logistic",
763	      "sign_flip_rate": 0.586,
764	      "tau_sign_flip_rate": 0.0,
765	      "dummy_sign_flip_rate": 0.586,
766	      "mean_bias": 0.48893740869940516,
767	      "coef_means": [
768	        0.2982857379786328,
769	        0.034145914499076
770	      ],
771	      "true_coefs": [
772	        0.831039083609622,
773	        -0.41097555726874485
774	      ],
775	      "n_valid": 500
776	    },
777	    {
778	      "topology": "exposure",
779	      "cm_name": "llama4_few-shot-3",
780	      "model": "linear",
781	      "sign_flip_rate": 0.602,
782	      "tau_sign_flip_rate": 0.0,
783	      "dummy_sign_flip_rate": 0.602,
784	      "mean_bias": 0.11623863567875745,
785	      "coef_means": [
786	        0.0738635136292106,
787	        0.008478766230179957
788	      ],
789	      "true_coefs": [
790	        0.1965173689601053,
791	        -0.10134464979644023
792	      ],
793	      "n_valid": 500
794	    },
795	    {
796	      "topology": "exposure",
797	      "cm_name": "llama4_few-shot-5",
798	      "model": "logistic",
799	      "sign_flip_rate": 0.0,
800	      "tau_sign_flip_rate": 0.0,
801	      "dummy_sign_flip_rate": 0.0,
802	      "mean_bias": 0.3171451684261805,
803	      "coef_means": [
804	        0.32248391837134727,
805	        -0.2874668762040176
806	      ],
807	      "true_coefs": [
808	        0.831039083609622,
809	        -0.41097555726874485
810	      ],
811	      "n_valid": 500
812	    },
813	    {
814	      "topology": "exposure",
815	      "cm_name": "llama4_few-shot-5",
816	      "model": "linear",
817	      "sign_flip_rate": 0.0,
818	      "tau_sign_flip_rate": 0.0,
819	      "dummy_sign_flip_rate": 0.0,
820	      "mean_bias": 0.07364375008014022,
821	      "coef_means": [
822	        0.07970688435031614,
823	        -0.07145033706051504
824	      ],
825	      "true_coefs": [
826	        0.1965173689601053,
827	        -0.10134464979644023
828	      ],
829	      "n_valid": 500
830	    },
831	    {
832	      "topology": "exposure",
833	      "cm_name": "llama4_zero-shot",
834	      "model": "logistic",
835	      "sign_flip_rate": 0.442,
836	      "tau_sign_flip_rate": 0.0,
837	      "dummy_sign_flip_rate": 0.442,
838	      "mean_bias": 0.43965994293687055,
839	      "coef_means": [
840	        0.3393554084750097,
841	        -0.02382254126637825
842	      ],
843	      "true_coefs": [
844	        0.831039083609622,
845	        -0.41097555726874485
846	      ],
847	      "n_valid": 500
848	    },
849	    {
850	      "topology": "exposure",
851	      "cm_name": "llama4_zero-shot",
852	      "model": "linear",
853	      "sign_flip_rate": 0.444,
854	      "tau_sign_flip_rate": 0.0,
855	      "dummy_sign_flip_rate": 0.444,
856	      "mean_bias": 0.1040288225145138,
857	      "coef_means": [
858	        0.0840313630450975,
859	        -0.005882272981552626
860	      ],
861	      "true_coefs": [
862	        0.1965173689601053,
863	        -0.10134464979644023
864	      ],
865	      "n_valid": 500
866	    },
867	    {
868	      "topology": "exposure",
869	      "cm_name": "qwen2.5-7b_few-shot-3",
870	      "model": "logistic",
871	      "sign_flip_rate": 0.936,
872	      "tau_sign_flip_rate": 0.0,
873	      "dummy_sign_flip_rate": 0.936,
874	      "mean_bias": 0.5417915236139126,
875	      "coef_means": [
876	        0.2708817585097783,
877	        0.11245016485923695
878	      ],
879	      "true_coefs": [
880	        0.831039083609622,
881	        -0.41097555726874485
882	      ],
883	      "n_valid": 500
884	    },
885	    {
886	      "topology": "exposure",
887	      "cm_name": "qwen2.5-7b_few-shot-3",
888	      "model": "linear",
889	      "sign_flip_rate": 0.936,
890	      "tau_sign_flip_rate": 0.0,
891	      "dummy_sign_flip_rate": 0.936,
892	      "mean_bias": 0.12937637785545353,
893	      "coef_means": [
894	        0.06717715547494744,
895	        0.028067892429308926
896	      ],
897	      "true_coefs": [
898	        0.1965173689601053,
899	        -0.10134464979644023
900	      ],
901	      "n_valid": 500
902	    },
903	    {
904	      "topology": "exposure",
905	      "cm_name": "qwen2.5-7b_few-shot-5",
906	      "model": "logistic",
907	      "sign_flip_rate": 0.982,
908	      "tau_sign_flip_rate": 0.0,
909	      "dummy_sign_flip_rate": 0.982,
910	      "mean_bias": 0.5671273223510509,
911	      "coef_means": [
912	        0.2613208545365811,
913	        0.1535608583603161
914	      ],
915	      "true_coefs": [
916	        0.831039083609622,
917	        -0.41097555726874485
918	      ],
919	      "n_valid": 500
920	    },
921	    {
922	      "topology": "exposure",
923	      "cm_name": "qwen2.5-7b_few-shot-5",
924	      "model": "linear",
925	      "sign_flip_rate": 0.982,
926	      "tau_sign_flip_rate": 0.0,
927	      "dummy_sign_flip_rate": 0.982,
928	      "mean_bias": 0.1356688485533437,
929	      "coef_means": [
930	        0.06479124036932071,
931	        0.03826691871946261
932	      ],
933	      "true_coefs": [
934	        0.1965173689601053,
935	        -0.10134464979644023
936	      ],
937	      "n_valid": 500
938	    },
939	    {
940	      "topology": "mbias",
941	      "cm_name": "deepseek_zero-shot",
942	      "model": "logistic",
943	      "sign_flip_rate": 0.01,
944	      "tau_sign_flip_rate": 0.0,
945	      "dummy_sign_flip_rate": 0.01,
946	      "mean_bias": 0.19863461710178607,
947	      "coef_means": [
948	        0.3647959322640891,
949	        0.24473596293327834,
950	        0.1673082360185677
951	      ],
952	      "true_coefs": [
953	        0.3815802895698336,
954	        0.4007689596054288,
955	        0.5879091344664784
956	      ],
957	      "n_valid": 500
958	    },
959	    {
960	      "topology": "mbias",
961	      "cm_name": "deepseek_zero-shot",
962	      "model": "linear",
963	      "sign_flip_rate": 0.01,
964	      "tau_sign_flip_rate": 0.0,
965	      "dummy_sign_flip_rate": 0.01,
966	      "mean_bias": 0.045885649482035454,
967	      "coef_means": [
968	        0.08550749061423507,
969	        0.057564612787976435,
970	        0.03929781480428287
971	      ],
972	      "true_coefs": [
973	        0.08843213701027604,
974	        0.0939667556082955,
975	        0.13692255544042678
976	      ],
977	      "n_valid": 500
978	    },
979	    {
980	      "topology": "mbias",
981	      "cm_name": "llama4_few-shot-3",
982	      "model": "logistic",
983	      "sign_flip_rate": 0.226,
984	      "tau_sign_flip_rate": 0.0,
985	      "dummy_sign_flip_rate": 0.226,
986	      "mean_bias": 0.2578896586339304,
987	      "coef_means": [
988	        0.36381098141530904,
989	        0.13746650971736118,
990	        0.09727861047353668
991	      ],
992	      "true_coefs": [
993	        0.3815802895698336,
994	        0.4007689596054288,
995	        0.5879091344664784
996	      ],
997	      "n_valid": 500
998	    },
999	    {
1000	      "topology": "mbias",
1001	      "cm_name": "llama4_few-shot-3",
1002	      "model": "linear",
1003	      "sign_flip_rate": 0.214,
1004	      "tau_sign_flip_rate": 0.0,
1005	      "dummy_sign_flip_rate": 0.214,
1006	      "mean_bias": 0.059784400111317644,
1007	      "coef_means": [
1008	        0.08539067991701305,
1009	        0.03241502570684394,
1010	        0.02278500724398465
1011	      ],
1012	      "true_coefs": [
1013	        0.08843213701027604,
1014	        0.0939667556082955,
1015	        0.13692255544042678
1016	      ],
1017	      "n_valid": 500
1018	    },
1019	    {
1020	      "topology": "mbias",
1021	      "cm_name": "llama4_few-shot-5",
1022	      "model": "logistic",
1023	      "sign_flip_rate": 0.0,
1024	      "tau_sign_flip_rate": 0.0,
1025	      "dummy_sign_flip_rate": 0.0,
1026	      "mean_bias": 0.19128067069893287,
1027	      "coef_means": [
1028	        0.36642248710938174,
1029	        0.1642750421251806,
1030	        0.26853431320880466
1031	      ],
1032	      "true_coefs": [
1033	        0.3815802895698336,
1034	        0.4007689596054288,
1035	        0.5879091344664784
1036	      ],
1037	      "n_valid": 500
1038	    },
1039	    {
1040	      "topology": "mbias",
1041	      "cm_name": "llama4_few-shot-5",
1042	      "model": "linear",
1043	      "sign_flip_rate": 0.0,
1044	      "tau_sign_flip_rate": 0.0,
1045	      "dummy_sign_flip_rate": 0.0,
1046	      "mean_bias": 0.044138852800038667,
1047	      "coef_means": [
1048	        0.08595113504296158,
1049	        0.0386812610199656,
1050	        0.06312192623695081
1051	      ],
1052	      "true_coefs": [
1053	        0.08843213701027604,
1054	        0.0939667556082955,
1055	        0.13692255544042678
1056	      ],
1057	      "n_valid": 500
1058	    },
1059	    {
1060	      "topology": "mbias",
1061	      "cm_name": "llama4_zero-shot",
1062	      "model": "logistic",
1063	      "sign_flip_rate": 0.15,
1064	      "tau_sign_flip_rate": 0.0,
1065	      "dummy_sign_flip_rate": 0.15,
1066	      "mean_bias": 0.23830659318824923,
1067	      "coef_means": [
1068	        0.36376223828163445,
1069	        0.14865098253864303,
1070	        0.14502581977553963
1071	      ],
1072	      "true_coefs": [
1073	        0.3815802895698336,
1074	        0.4007689596054288,
1075	        0.5879091344664784
1076	      ],
1077	      "n_valid": 500
1078	    },
1079	    {
1080	      "topology": "mbias",
1081	      "cm_name": "llama4_zero-shot",
1082	      "model": "linear",
1083	      "sign_flip_rate": 0.136,
1084	      "tau_sign_flip_rate": 0.0,
1085	      "dummy_sign_flip_rate": 0.136,
1086	      "mean_bias": 0.055154414772335444,
1087	      "coef_means": [
1088	        0.08533535666161766,
1089	        0.0350701905793187,
1090	        0.03406739637709331
1091	      ],
1092	      "true_coefs": [
1093	        0.08843213701027604,
1094	        0.0939667556082955,
1095	        0.13692255544042678
1096	      ],
1097	      "n_valid": 500
1098	    },
1099	    {
1100	      "topology": "mbias",
1101	      "cm_name": "qwen2.5-7b_few-shot-3",
1102	      "model": "logistic",
1103	      "sign_flip_rate": 0.124,
1104	      "tau_sign_flip_rate": 0.0,
1105	      "dummy_sign_flip_rate": 0.124,
1106	      "mean_bias": 0.2608267161933763,
1107	      "coef_means": [
1108	        0.3641176343167946,
1109	        0.14115393962366157,
1110	        0.08433576394937155
1111	      ],
1112	      "true_coefs": [
1113	        0.3815802895698336,
1114	        0.4007689596054288,
1115	        0.5879091344664784
1116	      ],
1117	      "n_valid": 500
1118	    },
1119	    {
1120	      "topology": "mbias",
1121	      "cm_name": "qwen2.5-7b_few-shot-3",
1122	      "model": "linear",
1123	      "sign_flip_rate": 0.124,
1124	      "tau_sign_flip_rate": 0.0,
1125	      "dummy_sign_flip_rate": 0.124,
1126	      "mean_bias": 0.060444768011082305,
1127	      "coef_means": [
1128	        0.08549885951267078,
1129	        0.033224307583897154,
1130	        0.019833715554022264
1131	      ],
1132	      "true_coefs": [
1133	        0.08843213701027604,
1134	        0.0939667556082955,
1135	        0.13692255544042678
1136	      ],
1137	      "n_valid": 500
1138	    },
1139	    {
1140	      "topology": "mbias",
1141	      "cm_name": "qwen2.5-7b_few-shot-5",
1142	      "model": "logistic",
1143	      "sign_flip_rate": 0.084,
1144	      "tau_sign_flip_rate": 0.0,
1145	      "dummy_sign_flip_rate": 0.084,
1146	      "mean_bias": 0.2571783375794883,
1147	      "coef_means": [
1148	        0.3639002100402961,
1149	        0.14379839321278284,
1150	        0.09319823862900554
1151	      ],
1152	      "true_coefs": [
1153	        0.3815802895698336,
1154	        0.4007689596054288,
1155	        0.5879091344664784
1156	      ],
1157	      "n_valid": 500
1158	    },
1159	    {
1160	      "topology": "mbias",
1161	      "cm_name": "qwen2.5-7b_few-shot-5",
1162	      "model": "linear",
1163	      "sign_flip_rate": 0.084,
1164	      "tau_sign_flip_rate": 0.0,
1165	      "dummy_sign_flip_rate": 0.084,
1166	      "mean_bias": 0.05957696406457641,
1167	      "coef_means": [
1168	        0.08544807233392832,
1169	        0.03387510006757848,
1170	        0.021950328658433313
1171	      ],
1172	      "true_coefs": [
1173	        0.08843213701027604,
1174	        0.0939667556082955,
1175	        0.13692255544042678
1176	      ],
1177	      "n_valid": 500
1178	    },
1179	    {
1180	      "topology": "frontdoor",
1181	      "cm_name": "deepseek_zero-shot",
1182	      "model": "logistic",
1183	      "sign_flip_rate": 0.574,
1184	      "tau_sign_flip_rate": 0.0,
1185	      "dummy_sign_flip_rate": 0.574,
1186	      "mean_bias": 0.4186162809497493,
1187	      "coef_means": [
1188	        0.6302554054951269,
1189	        0.16023309957887685,
1190	        0.014485420922084161
1191	      ],
1192	      "true_coefs": [
1193	        0.3958182242468827,
1194	        0.778882107857046,
1195	        -0.38827723240075057
1196	      ],
1197	      "n_valid": 500
1198	    },
1199	    {
1200	      "topology": "frontdoor",
1201	      "cm_name": "deepseek_zero-shot",
1202	      "model": "linear",
1203	      "sign_flip_rate": 0.556,
1204	      "tau_sign_flip_rate": 0.0,
1205	      "dummy_sign_flip_rate": 0.556,
1206	      "mean_bias": 0.10061327574598079,
1207	      "coef_means": [
1208	        0.13258495570609666,
1209	        0.03461071493273304,
1210	        0.002598947259723432
1211	      ],
1212	      "true_coefs": [
1213	        0.07831334834999377,
1214	        0.182496134727592,
1215	        -0.0970838528272571
1216	      ],
1217	      "n_valid": 500
1218	    },
1219	    {
1220	      "topology": "frontdoor",
1221	      "cm_name": "llama4_few-shot-3",
1222	      "model": "logistic",
1223	      "sign_flip_rate": 0.594,
1224	      "tau_sign_flip_rate": 0.0,
1225	      "dummy_sign_flip_rate": 0.594,
1226	      "mean_bias": 0.40501345596410543,
1227	      "coef_means": [
1228	        0.6219691448514701,
1229	        0.22144998861347717,
1230	        0.04284946203058246
1231	      ],
1232	      "true_coefs": [
1233	        0.3958182242468827,
1234	        0.778882107857046,
1235	        -0.38827723240075057
1236	      ],
1237	      "n_valid": 500
1238	    },
1239	    {
1240	      "topology": "frontdoor",
1241	      "cm_name": "llama4_few-shot-3",
1242	      "model": "linear",
1243	      "sign_flip_rate": 0.632,
1244	      "tau_sign_flip_rate": 0.0,
1245	      "dummy_sign_flip_rate": 0.632,
1246	      "mean_bias": 0.09752281599489208,
1247	      "coef_means": [
1248	        0.13079136547068804,
1249	        0.048969776226286385,
1250	        0.009480219535419289
1251	      ],
1252	      "true_coefs": [
1253	        0.07831334834999377,
1254	        0.182496134727592,
1255	        -0.0970838528272571
1256	      ],
1257	      "n_valid": 500
1258	    },
1259	    {
1260	      "topology": "frontdoor",
1261	      "cm_name": "llama4_few-shot-5",
1262	      "model": "logistic",
1263	      "sign_flip_rate": 0.01,
1264	      "tau_sign_flip_rate": 0.0,
1265	      "dummy_sign_flip_rate": 0.01,
1266	      "mean_bias": 0.3115578191820141,
1267	      "coef_means": [
1268	        0.6056571774429583,
1269	        0.24896737626633392,
1270	        -0.19429743866619845
1271	      ],
1272	      "true_coefs": [
1273	        0.3958182242468827,
1274	        0.778882107857046,
1275	        -0.38827723240075057
1276	      ],
1277	      "n_valid": 500
1278	    },
1279	    {
1280	      "topology": "frontdoor",
1281	      "cm_name": "llama4_few-shot-5",
1282	      "model": "linear",
1283	      "sign_flip_rate": 0.004,
1284	      "tau_sign_flip_rate": 0.0,
1285	      "dummy_sign_flip_rate": 0.004,
1286	      "mean_bias": 0.07595936320440937,
1287	      "coef_means": [
1288	        0.12711163526399588,
1289	        0.05557718859280249,
1290	        -0.044925873446097775
1291	      ],
1292	      "true_coefs": [
1293	        0.07831334834999377,
1294	        0.182496134727592,
1295	        -0.0970838528272571
1296	      ],
1297	      "n_valid": 500
1298	    },
1299	    {
1300	      "topology": "frontdoor",
1301	      "cm_name": "llama4_zero-shot",
1302	      "model": "logistic",
1303	      "sign_flip_rate": 0.442,
1304	      "tau_sign_flip_rate": 0.0,
1305	      "dummy_sign_flip_rate": 0.442,
1306	      "mean_bias": 0.37397093353847244,
1307	      "coef_means": [
1308	        0.6157669506443375,
1309	        0.2590225903522688,
1310	        -0.006318622763965126
1311	      ],
1312	      "true_coefs": [
1313	        0.3958182242468827,
1314	        0.778882107857046,
1315	        -0.38827723240075057
1316	      ],
1317	      "n_valid": 500
1318	    },
1319	    {
1320	      "topology": "frontdoor",
1321	      "cm_name": "llama4_zero-shot",
1322	      "model": "linear",
1323	      "sign_flip_rate": 0.474,
1324	      "tau_sign_flip_rate": 0.0,
1325	      "dummy_sign_flip_rate": 0.474,
1326	      "mean_bias": 0.09046811396774206,
1327	      "coef_means": [
1328	        0.12952049115856673,
1329	        0.05764858838236289,
1330	        -0.0017342000778329807
1331	      ],
1332	      "true_coefs": [
1333	        0.07831334834999377,
1334	        0.182496134727592,
1335	        -0.0970838528272571
1336	      ],
1337	      "n_valid": 500
1338	    },
1339	    {
1340	      "topology": "frontdoor",
1341	      "cm_name": "qwen2.5-7b_few-shot-3",
1342	      "model": "logistic",
1343	      "sign_flip_rate": 0.9,
1344	      "tau_sign_flip_rate": 0.0,
1345	      "dummy_sign_flip_rate": 0.9,
1346	      "mean_bias": 0.4278974881621149,
1347	      "coef_means": [
1348	        0.6247528959388846,
1349	        0.21491896174869562,
1350	        0.10251741428524165
1351	      ],
1352	      "true_coefs": [
1353	        0.3958182242468827,
1354	        0.778882107857046,
1355	        -0.38827723240075057
1356	      ],
1357	      "n_valid": 500
1358	    },
1359	    {
1360	      "topology": "frontdoor",
1361	      "cm_name": "qwen2.5-7b_few-shot-3",
1362	      "model": "linear",
1363	      "sign_flip_rate": 0.914,
1364	      "tau_sign_flip_rate": 0.0,
1365	      "dummy_sign_flip_rate": 0.914,
1366	      "mean_bias": 0.10271511801049663,
1367	      "coef_means": [
1368	        0.13151086535446338,
1369	        0.04776480153043886,
1370	        0.023132651002610027
1371	      ],
1372	      "true_coefs": [
1373	        0.07831334834999377,
1374	        0.182496134727592,
1375	        -0.0970838528272571
1376	      ],
1377	      "n_valid": 500
1378	    },
1379	    {
1380	      "topology": "frontdoor",
1381	      "cm_name": "qwen2.5-7b_few-shot-5",
1382	      "model": "logistic",
1383	      "sign_flip_rate": 0.954,
1384	      "tau_sign_flip_rate": 0.0,
1385	      "dummy_sign_flip_rate": 0.954,
1386	      "mean_bias": 0.43909645484855725,
1387	      "coef_means": [
1388	        0.6262367545238161,
1389	        0.20492470516778438,
1390	        0.12463619917872565
1391	      ],
1392	      "true_coefs": [
1393	        0.3958182242468827,
1394	        0.778882107857046,
1395	        -0.38827723240075057
1396	      ],
1397	      "n_valid": 500
1398	    },
1399	    {
1400	      "topology": "frontdoor",
1401	      "cm_name": "qwen2.5-7b_few-shot-5",
1402	      "model": "linear",
1403	      "sign_flip_rate": 0.958,
1404	      "tau_sign_flip_rate": 0.0,
1405	      "dummy_sign_flip_rate": 0.958,
1406	      "mean_bias": 0.10521214855360442,
1407	      "coef_means": [
1408	        0.1317846322960338,
1409	        0.04539076670367443,
1410	        0.027975940863598538
1411	      ],
1412	      "true_coefs": [
1413	        0.07831334834999377,
1414	        0.182496134727592,
1415	        -0.0970838528272571
1416	      ],
1417	      "n_valid": 500
1418	    },
1419	    {
1420	      "topology": "iv",
1421	      "cm_name": "deepseek_zero-shot",
1422	      "model": "control_function",
1423	      "sign_flip_rate": 0.592,
1424	      "tau_sign_flip_rate": 0.098,
1425	      "dummy_sign_flip_rate": 0.0,
1426	      "mean_bias": 0.2835517377779671,
1427	      "coef_means": [
1428	        0.4096950102995125,
1429	        0.005485749260719923
1430	      ],
1431	      "true_coefs": [
1432	        0.4124652334181566,
1433	        0.0019517787642728789
1434	      ],
1435	      "n_valid": 500
1436	    },
1437	    {
1438	      "topology": "iv",
1439	      "cm_name": "deepseek_zero-shot",
1440	      "model": "linear_2sls",
1441	      "sign_flip_rate": 0.114,
1442	      "tau_sign_flip_rate": 0.114,
1443	      "dummy_sign_flip_rate": 0.0,
1444	      "mean_bias": 0.06529388407589415,
1445	      "coef_means": [
1446	        0.1003667390199889
1447	      ],
1448	      "true_coefs": [
1449	        0.09867173691095897
1450	      ],
1451	      "n_valid": 500
1452	    },
1453	    {
1454	      "topology": "iv",
1455	      "cm_name": "llama4_few-shot-3",
1456	      "model": "control_function",
1457	      "sign_flip_rate": 0.546,
1458	      "tau_sign_flip_rate": 0.074,
1459	      "dummy_sign_flip_rate": 0.0,
1460	      "mean_bias": 0.21797670971201494,
1461	      "coef_means": [
1462	        0.39160646239188096,
1463	        0.024204677952890986
1464	      ],
1465	      "true_coefs": [
1466	        0.4124652334181566,
1467	        0.0019517787642728789
1468	      ],
1469	      "n_valid": 500
1470	    },
1471	    {
1472	      "topology": "iv",
1473	      "cm_name": "llama4_few-shot-3",
1474	      "model": "linear_2sls",
1475	      "sign_flip_rate": 0.076,
1476	      "tau_sign_flip_rate": 0.076,
1477	      "dummy_sign_flip_rate": 0.0,
1478	      "mean_bias": 0.05084464356629255,
1479	      "coef_means": [
1480	        0.09412285561757143
1481	      ],
1482	      "true_coefs": [
1483	        0.09867173691095897
1484	      ],
1485	      "n_valid": 500
1486	    },
1487	    {
1488	      "topology": "iv",
1489	      "cm_name": "llama4_few-shot-5",
1490	      "model": "control_function",
1491	      "sign_flip_rate": 0.554,
1492	      "tau_sign_flip_rate": 0.028,
1493	      "dummy_sign_flip_rate": 0.0,
1494	      "mean_bias": 0.16057763933898422,
1495	      "coef_means": [
1496	        0.4143968266851045,
1497	        0.0007447079810177435
1498	      ],
1499	      "true_coefs": [
1500	        0.4124652334181566,
1501	        0.0019517787642728789
1502	      ],
1503	      "n_valid": 500
1504	    },
1505	    {
1506	      "topology": "iv",
1507	      "cm_name": "llama4_few-shot-5",
1508	      "model": "linear_2sls",
1509	      "sign_flip_rate": 0.026,
1510	      "tau_sign_flip_rate": 0.026,
1511	      "dummy_sign_flip_rate": 0.0,
1512	      "mean_bias": 0.037317384014786965,
1513	      "coef_means": [
1514	        0.09944462981078801
1515	      ],
1516	      "true_coefs": [
1517	        0.09867173691095897
1518	      ],
1519	      "n_valid": 500
1520	    },
1521	    {
1522	      "topology": "iv",
1523	      "cm_name": "llama4_zero-shot",
1524	      "model": "control_function",
1525	      "sign_flip_rate": 0.538,
1526	      "tau_sign_flip_rate": 0.042,
1527	      "dummy_sign_flip_rate": 0.0,
1528	      "mean_bias": 0.18768388775517042,
1529	      "coef_means": [
1530	        0.41248518796900735,
1531	        0.002239225824138769
1532	      ],
1533	      "true_coefs": [
1534	        0.4124652334181566,
1535	        0.0019517787642728789
1536	      ],
1537	      "n_valid": 500
1538	    },
1539	    {
1540	      "topology": "iv",
1541	      "cm_name": "llama4_zero-shot",
1542	      "model": "linear_2sls",
1543	      "sign_flip_rate": 0.04,
1544	      "tau_sign_flip_rate": 0.04,
1545	      "dummy_sign_flip_rate": 0.0,
1546	      "mean_bias": 0.044029827420180356,
1547	      "coef_means": [
1548	        0.0987226874245134
1549	      ],
1550	      "true_coefs": [
1551	        0.09867173691095897
1552	      ],
1553	      "n_valid": 500
1554	    },
1555	    {
1556	      "topology": "iv",
1557	      "cm_name": "qwen2.5-7b_few-shot-3",
1558	      "model": "control_function",
1559	      "sign_flip_rate": 0.588,
1560	      "tau_sign_flip_rate": 0.108,
1561	      "dummy_sign_flip_rate": 0.0,
1562	      "mean_bias": 0.281870164283535,
1563	      "coef_means": [
1564	        0.40583504187814945,
1565	        0.0102555742534641
1566	      ],
1567	      "true_coefs": [
1568	        0.4124652334181566,
1569	        0.0019517787642728789
1570	      ],
1571	      "n_valid": 500
1572	    },
1573	    {
1574	      "topology": "iv",
1575	      "cm_name": "qwen2.5-7b_few-shot-3",
1576	      "model": "linear_2sls",
1577	      "sign_flip_rate": 0.132,
1578	      "tau_sign_flip_rate": 0.132,
1579	      "dummy_sign_flip_rate": 0.0,
1580	      "mean_bias": 0.06652435263864621,
1581	      "coef_means": [
1582	        0.0980473437384179
1583	      ],
1584	      "true_coefs": [
1585	        0.09867173691095897
1586	      ],
1587	      "n_valid": 500
1588	    },
1589	    {
1590	      "topology": "iv",
1591	      "cm_name": "qwen2.5-7b_few-shot-5",
1592	      "model": "control_function",
1593	      "sign_flip_rate": 0.54,
1594	      "tau_sign_flip_rate": 0.096,
1595	      "dummy_sign_flip_rate": 0.0,
1596	      "mean_bias": 0.28634403435314887,
1597	      "coef_means": [
1598	        0.40712179110879765,
1599	        0.006365484868388459
1600	      ],
1601	      "true_coefs": [
1602	        0.4124652334181566,
1603	        0.0019517787642728789
1604	      ],
1605	      "n_valid": 500
1606	    },
1607	    {
1608	      "topology": "iv",
1609	      "cm_name": "qwen2.5-7b_few-shot-5",
1610	      "model": "linear_2sls",
1611	      "sign_flip_rate": 0.126,
1612	      "tau_sign_flip_rate": 0.126,
1613	      "dummy_sign_flip_rate": 0.0,
1614	      "mean_bias": 0.0680733908434805,
1615	      "coef_means": [
1616	        0.09838126205370382
1617	      ],
1618	      "true_coefs": [
1619	        0.09867173691095897
1620	      ],
1621	      "n_valid": 500
1622	    }
1623	  ],
1624	  "comparison_with_linear": {
1625	    "confounding": {
1626	      "nonlinear_mean_sf": 0.5593333333333333,
1627	      "linear_mean_sf": 0.5726666666666667,
1628	      "nonlinear_mean_tau_sf": 0.0,
1629	      "linear_mean_tau_sf": 0.0,
1630	      "nonlinear_model": "logistic",
1631	      "linear_model": "linear",
1632	      "n_cms": 6
1633	    },
1634	    "mediation": {
1635	      "nonlinear_mean_sf": 0.695,
1636	      "linear_mean_sf": 0.703,
1637	      "nonlinear_mean_tau_sf": 0.0,
1638	      "linear_mean_tau_sf": 0.0,
1639	      "nonlinear_model": "logistic",
1640	      "linear_model": "linear",
1641	      "n_cms": 6
1642	    },
1643	    "collider": {
1644	      "nonlinear_mean_sf": 0.060000000000000005,
1645	      "linear_mean_sf": 0.06033333333333334,
1646	      "nonlinear_mean_tau_sf": 0.0,
1647	      "linear_mean_tau_sf": 0.0,
1648	      "nonlinear_model": "logistic",
1649	      "linear_model": "linear",
1650	      "n_cms": 6
1651	    },
1652	    "exposure": {
1653	      "nonlinear_mean_sf": 0.5736666666666667,
1654	      "linear_mean_sf": 0.5773333333333333,
1655	      "nonlinear_mean_tau_sf": 0.0,
1656	      "linear_mean_tau_sf": 0.0,
1657	      "nonlinear_model": "logistic",
1658	      "linear_model": "linear",
1659	      "n_cms": 6
1660	    },
1661	    "mbias": {
1662	      "nonlinear_mean_sf": 0.09899999999999999,
1663	      "linear_mean_sf": 0.09466666666666666,
1664	      "nonlinear_mean_tau_sf": 0.0,
1665	      "linear_mean_tau_sf": 0.0,
1666	      "nonlinear_model": "logistic",
1667	      "linear_model": "linear",
1668	      "n_cms": 6
1669	    },
1670	    "frontdoor": {
1671	      "nonlinear_mean_sf": 0.5790000000000001,
1672	      "linear_mean_sf": 0.5896666666666667,
1673	      "nonlinear_mean_tau_sf": 0.0,
1674	      "linear_mean_tau_sf": 0.0,
1675	      "nonlinear_model": "logistic",
1676	      "linear_model": "linear",
1677	      "n_cms": 6
1678	    },
1679	    "iv": {
1680	      "nonlinear_mean_sf": 0.5596666666666666,
1681	      "linear_mean_sf": 0.08566666666666667,
1682	      "nonlinear_mean_tau_sf": 0.07433333333333332,
1683	      "linear_mean_tau_sf": 0.08566666666666667,
1684	      "nonlinear_model": "control_function",
1685	      "linear_model": "linear_2sls",
1686	      "n_cms": 6
1687	    }
1688	  },
1689	  "true_params": {
1690	    "confounding": {
1691	      "logistic": [
1692	        0.41638484019002725,
1693	        0.8361038268454802,
1694	        -0.41450657434609767
1695	      ],
1696	      "linear": [
1697	        0.0931430096052067,
1698	        0.18609937231088194,
1699	        -0.09861454080375684
1700	      ]
1701	    },
1702	    "mediation": {
1703	      "logistic": [
1704	        0.41810133700251345,
1705	        0.8374399824986839,
1706	        -0.4152697999810058
1707	      ],
1708	      "linear": [
1709	        0.08888487434071951,
1710	        0.18700969432033765,
1711	        -0.10417733192947722
1712	      ]
1713	    },
1714	    "collider": {
1715	      "logistic": [
1716	        0.3708255284760652,
1717	        0.7942498981279285,
1718	        0.5935002568689364
1719	      ],
1720	      "linear": [
1721	        0.08701000898472552,
1722	        0.18969994005002871,
1723	        0.14004209767109965
1724	      ]
1725	    },
1726	    "exposure": {
1727	      "logistic": [
1728	        0.831039083609622,
1729	        -0.41097555726874485
1730	      ],
1731	      "linear": [
1732	        0.1965173689601053,
1733	        -0.10134464979644023
1734	      ]
1735	    },
1736	    "mbias": {
1737	      "logistic": [
1738	        0.3815802895698336,
1739	        0.4007689596054288,
1740	        0.5879091344664784
1741	      ],
1742	      "linear": [
1743	        0.08843213701027604,
1744	        0.0939667556082955,
1745	        0.13692255544042678
1746	      ]
1747	    },
1748	    "frontdoor": {
1749	      "logistic": [
1750	        0.3958182242468827,
1751	        0.778882107857046,
1752	        -0.38827723240075057
1753	      ],
1754	      "linear": [
1755	        0.07831334834999377,
1756	        0.182496134727592,
1757	        -0.0970838528272571
1758	      ]
1759	    },
1760	    "iv": {
1761	      "linear_2sls": [
1762	        0.09867173691095897
1763	      ],
1764	      "control_function": [
1765	        0.4124652334181566,
1766	        0.0019517787642728789
1767	      ]
1768	    }
1769	  },
1770	  "config": {
1771	    "N": 10000,
1772	    "n_reps": 500,
1773	    "K": 3,
1774	    "tau": 0.5,
1775	    "beta": [
1776	      0.0,
1777	      1.0,
1778	      -0.5
1779	    ],
1780	    "topologies": [
1781	      "confounding",
1782	      "mediation",
1783	      "collider",
1784	      "exposure",
1785	      "mbias",
1786	      "frontdoor",
1787	      "iv"
1788	    ]
1789	  }
1790	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3181dd62-555d-45a2-8404-f8073fd27a0e",
  "isSidechain": true,
  "promptId": "6231d775-db71-46d9-bac6-397081d485cb",
  "agentId": "a767a9abec38e8eae",
  "type": "user",
  "uuid": "5cc90c19-57ae-4b35-83aa-6e1575da72a7",
  "sourceToolAssistantUUID": "3181dd62-555d-45a2-8404-f8073fd27a0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T19:22:04.703Z_

<details><summary>↩ Tool result · `toolu_01TKYZrSfTcrzu97rwkfHVqK`</summary>

```text
1	{
2	  "results": [
3	    {
4	      "topology": "confounding",
5	      "K": 3,
6	      "epsilon": 0.0,
7	      "cm_quality": "high",
8	      "cm_diag": 0.8,
9	      "sign_flip_rate": 0.0,
10	      "mean_bias_ratio": 1.102087665348223,
11	      "std_bias_ratio": 0.00455827568036216,
12	      "median_bias_ratio": 1.1019941161886861,
13	      "tau_true": 1.9994936164112898,
14	      "mean_tau_hat": 2.2036172515893937,
15	      "n_reps": 100
16	    },
17	    {
18	      "topology": "confounding",
19	      "K": 3,
20	      "epsilon": 0.01,
21	      "cm_quality": "high",
22	      "cm_diag": 0.8,
23	      "sign_flip_rate": 0.0,
24	      "mean_bias_ratio": 1.104580179494602,
25	      "std_bias_ratio": 0.004601287530111832,
26	      "median_bias_ratio": 1.104736934277235,
27	      "tau_true": 1.9994936164112898,
28	      "mean_tau_hat": 2.2086010177138937,
29	      "n_reps": 100
30	    },
31	    {
32	      "topology": "confounding",
33	      "K": 3,
34	      "epsilon": 0.05,
35	      "cm_quality": "high",
36	      "cm_diag": 0.8,
37	      "sign_flip_rate": 0.0,
38	      "mean_bias_ratio": 1.1120318990065035,
39	      "std_bias_ratio": 0.004102692532487713,
40	      "median_bias_ratio": 1.111782604036133,
41	      "tau_true": 1.9994936164112898,
42	      "mean_tau_hat": 2.223500683309228,
43	      "n_reps": 100
44	    },
45	    {
46	      "topology": "confounding",
47	      "K": 3,
48	      "epsilon": 0.1,
49	      "cm_quality": "high",
50	      "cm_diag": 0.8,
51	      "sign_flip_rate": 0.0,
52	      "mean_bias_ratio": 1.119025809705127,
53	      "std_bias_ratio": 0.003641710489111343,
54	      "median_bias_ratio": 1.1189751567370299,
55	      "tau_true": 1.9994936164112898,
56	      "mean_tau_hat": 2.237484963104876,
57	      "n_reps": 100
58	    },
59	    {
60	      "topology": "confounding",
61	      "K": 3,
62	      "epsilon": 0.0,
63	      "cm_quality": "medium",
64	      "cm_diag": 0.6,
65	      "sign_flip_rate": 0.0,
66	      "mean_bias_ratio": 1.1374827917423829,
67	      "std_bias_ratio": 0.003719590567552914,
68	      "median_bias_ratio": 1.1376966311534251,
69	      "tau_true": 1.9994936164112898,
70	      "mean_tau_hat": 2.274389580866587,
71	      "n_reps": 100
72	    },
73	    {
74	      "topology": "confounding",
75	      "K": 3,
76	      "epsilon": 0.01,
77	      "cm_quality": "medium",
78	      "cm_diag": 0.6,
79	      "sign_flip_rate": 0.0,
80	      "mean_bias_ratio": 1.1378938561662346,
81	      "std_bias_ratio": 0.004222544559955513,
82	      "median_bias_ratio": 1.138475313822984,
83	      "tau_true": 1.9994936164112898,
84	      "mean_tau_hat": 2.275211501558012,
85	      "n_reps": 100
86	    },
87	    {
88	      "topology": "confounding",
89	      "K": 3,
90	      "epsilon": 0.05,
91	      "cm_quality": "medium",
92	      "cm_diag": 0.6,
93	      "sign_flip_rate": 0.0,
94	      "mean_bias_ratio": 1.14067785239435,
95	      "std_bias_ratio": 0.0040646943477984695,
96	      "median_bias_ratio": 1.1405060435819214,
97	      "tau_true": 1.9994936164112898,
98	      "mean_tau_hat": 2.2807780842442424,
99	      "n_reps": 100
100	    },
101	    {
102	      "topology": "confounding",
103	      "K": 3,
104	      "epsilon": 0.1,
105	      "cm_quality": "medium",
106	      "cm_diag": 0.6,
107	      "sign_flip_rate": 0.0,
108	      "mean_bias_ratio": 1.1422141275638042,
109	      "std_bias_ratio": 0.003918380152432234,
110	      "median_bias_ratio": 1.1422096710362502,
111	      "tau_true": 1.9994936164112898,
112	      "mean_tau_hat": 2.283849856638617,
113	      "n_reps": 100
114	    },
115	    {
116	      "topology": "confounding",
117	      "K": 3,
118	      "epsilon": 0.0,
119	      "cm_quality": "low",
120	      "cm_diag": 0.4,
121	      "sign_flip_rate": 0.0,
122	      "mean_bias_ratio": 1.1486767012227812,
123	      "std_bias_ratio": 0.003587240066880197,
124	      "median_bias_ratio": 1.148609313883572,
125	      "tau_true": 1.9994936164112898,
126	      "mean_tau_hat": 2.2967717314153293,
127	      "n_reps": 100
128	    },
129	    {
130	      "topology": "confounding",
131	      "K": 3,
132	      "epsilon": 0.01,
133	      "cm_quality": "low",
134	      "cm_diag": 0.4,
135	      "sign_flip_rate": 0.0,
136	      "mean_bias_ratio": 1.1495333774259864,
137	      "std_bias_ratio": 0.0040499808391549,
138	      "median_bias_ratio": 1.1497138140887595,
139	      "tau_true": 1.9994936164112898,
140	      "mean_tau_hat": 2.2984846500149696,
141	      "n_reps": 100
142	    },
143	    {
144	      "topology": "confounding",
145	      "K": 3,
146	      "epsilon": 0.05,
147	      "cm_quality": "low",
148	      "cm_diag": 0.4,
149	      "sign_flip_rate": 0.0,
150	      "mean_bias_ratio": 1.1494478069494836,
151	      "std_bias_ratio": 0.003748530473880368,
152	      "median_bias_ratio": 1.1495174776618826,
153	      "tau_true": 1.9994936164112898,
154	      "mean_tau_hat": 2.2983135523934486,
155	      "n_reps": 100
156	    },
157	    {
158	      "topology": "confounding",
159	      "K": 3,
160	      "epsilon": 0.1,
161	      "cm_quality": "low",
162	      "cm_diag": 0.4,
163	      "sign_flip_rate": 0.0,
164	      "mean_bias_ratio": 1.1502750222009341,
165	      "std_bias_ratio": 0.0034845568011967923,
166	      "median_bias_ratio": 1.1500308422072218,
167	      "tau_true": 1.9994936164112898,
168	      "mean_tau_hat": 2.2999675640081225,
169	      "n_reps": 100
170	    },
171	    {
172	      "topology": "confounding",
173	      "K": 10,
174	      "epsilon": 0.0,
175	      "cm_quality": "high",
176	      "cm_diag": 0.8,
177	      "sign_flip_rate": 0.0,
178	      "mean_bias_ratio": 1.05777756383239,
179	      "std_bias_ratio": 0.0043312876958772,
180	      "median_bias_ratio": 1.0580214198852405,
181	      "tau_true": 2.001390757372502,
182	      "mean_tau_hat": 2.1170262396101474,
183	      "n_reps": 100
184	    },
185	    {
186	      "topology": "confounding",
187	      "K": 10,
188	      "epsilon": 0.01,
189	      "cm_quality": "high",
190	      "cm_diag": 0.8,
191	      "sign_flip_rate": 0.0,
192	      "mean_bias_ratio": 1.0639160278512263,
193	      "std_bias_ratio": 0.004793686824150899,
194	      "median_bias_ratio": 1.0643741097449408,
195	      "tau_true": 2.001390757372502,
196	      "mean_tau_hat": 2.1293117047619092,
197	      "n_reps": 100
198	    },
199	    {
200	      "topology": "confounding",
201	      "K": 10,
202	      "epsilon": 0.05,
203	      "cm_quality": "high",
204	      "cm_diag": 0.8,
205	      "sign_flip_rate": 0.0,
206	      "mean_bias_ratio": 1.0793555259780423,
207	      "std_bias_ratio": 0.00394692887051067,
208	      "median_bias_ratio": 1.078711619230146,
209	      "tau_true": 2.001390757372502,
210	      "mean_tau_hat": 2.160212173611389,
211	      "n_reps": 100
212	    },
213	    {
214	      "topology": "confounding",
215	      "K": 10,
216	      "epsilon": 0.1,
217	      "cm_quality": "high",
218	      "cm_diag": 0.8,
219	      "sign_flip_rate": 0.0,
220	      "mean_bias_ratio": 1.0856676025115788,
221	      "std_bias_ratio": 0.0044100068994904085,
222	      "median_bias_ratio": 1.0856379484760226,
223	      "tau_true": 2.001390757372502,
224	      "mean_tau_hat": 2.1728451052454374,
225	      "n_reps": 100
226	    },
227	    {
228	      "topology": "confounding",
229	      "K": 10,
230	      "epsilon": 0.0,
231	      "cm_quality": "medium",
232	      "cm_diag": 0.6,
233	      "sign_flip_rate": 0.0,
234	      "mean_bias_ratio": 1.088692632972217,
235	      "std_bias_ratio": 0.004277713947838112,
236	      "median_bias_ratio": 1.0886129899808639,
237	      "tau_true": 2.001390757372502,
238	      "mean_tau_hat": 2.1788993732501285,
239	      "n_reps": 100
240	    },
241	    {
242	      "topology": "confounding",
243	      "K": 10,
244	      "epsilon": 0.01,
245	      "cm_quality": "medium",
246	      "cm_diag": 0.6,
247	      "sign_flip_rate": 0.0,
248	      "mean_bias_ratio": 1.0910168057441896,
249	      "std_bias_ratio": 0.005000036617855027,
250	      "median_bias_ratio": 1.0909792932238398,
251	      "tau_true": 2.001390757372502,
252	      "mean_tau_hat": 2.1835509511544906,
253	      "n_reps": 100
254	    },
255	    {
256	      "topology": "confounding",
257	      "K": 10,
258	      "epsilon": 0.05,
259	      "cm_quality": "medium",
260	      "cm_diag": 0.6,
261	      "sign_flip_rate": 0.0,
262	      "mean_bias_ratio": 1.0979596393629638,
263	      "std_bias_ratio": 0.0037424005463796363,
264	      "median_bias_ratio": 1.0984563756892085,
265	      "tau_true": 2.001390757372502,
266	      "mean_tau_hat": 2.197446274189082,
267	      "n_reps": 100
268	    },
269	    {
270	      "topology": "confounding",
271	      "K": 10,
272	      "epsilon": 0.1,
273	      "cm_quality": "medium",
274	      "cm_diag": 0.6,
275	      "sign_flip_rate": 0.0,
276	      "mean_bias_ratio": 1.1012351170534382,
277	      "std_bias_ratio": 0.004371958027551496,
278	      "median_bias_ratio": 1.101341649713314,
279	      "tau_true": 2.001390757372502,
280	      "mean_tau_hat": 2.2040017849647766,
281	      "n_reps": 100
282	    },
283	    {
284	      "topology": "confounding",
285	      "K": 10,
286	      "epsilon": 0.0,
287	      "cm_quality": "low",
288	      "cm_diag": 0.4,
289	      "sign_flip_rate": 0.0,
290	      "mean_bias_ratio": 1.1056731123971912,
291	      "std_bias_ratio": 0.004493722346284278,
292	      "median_bias_ratio": 1.1053111776304152,
293	      "tau_true": 2.001390757372502,
294	      "mean_tau_hat": 2.212883947827026,
295	      "n_reps": 100
296	    },
297	    {
298	      "topology": "confounding",
299	      "K": 10,
300	      "epsilon": 0.01,
301	      "cm_quality": "low",
302	      "cm_diag": 0.4,
303	      "sign_flip_rate": 0.0,
304	      "mean_bias_ratio": 1.1068364398694897,
305	      "std_bias_ratio": 0.00412791365122749,
306	      "median_bias_ratio": 1.106571113051754,
307	      "tau_true": 2.001390757372502,
308	      "mean_tau_hat": 2.2152122206778815,
309	      "n_reps": 100
310	    },
311	    {
312	      "topology": "confounding",
313	      "K": 10,
314	      "epsilon": 0.05,
315	      "cm_quality": "low",
316	      "cm_diag": 0.4,
317	      "sign_flip_rate": 0.0,
318	      "mean_bias_ratio": 1.1083509219847598,
319	      "std_bias_ratio": 0.004023959888412517,
320	      "median_bias_ratio": 1.1084263109129417,
321	      "tau_true": 2.001390757372502,
322	      "mean_tau_hat": 2.2182432911855896,
323	      "n_reps": 100
324	    },
325	    {
326	      "topology": "confounding",
327	      "K": 10,
328	      "epsilon": 0.1,
329	      "cm_quality": "low",
330	      "cm_diag": 0.4,
331	      "sign_flip_rate": 0.0,
332	      "mean_bias_ratio": 1.1111309752117806,
333	      "std_bias_ratio": 0.004097621654112319,
334	      "median_bias_ratio": 1.1108495143649377,
335	      "tau_true": 2.001390757372502,
336	      "mean_tau_hat": 2.223807264019152,
337	      "n_reps": 100
338	    },
339	    {
340	      "topology": "mediation",
341	      "K": 3,
342	      "epsilon": 0.0,
343	      "cm_quality": "high",
344	      "cm_diag": 0.8,
345	      "sign_flip_rate": 0.0,
346	      "mean_bias_ratio": 1.3537241340036337,
347	      "std_bias_ratio": 0.03992697843673689,
348	      "median_bias_ratio": 1.353960239078439,
349	      "tau_true": 0.49864566446565145,
350	      "mean_tau_hat": 0.6750286703034307,
351	      "n_reps": 100
352	    },
353	    {
354	      "topology": "mediation",
355	      "K": 3,
356	      "epsilon": 0.01,
357	      "cm_quality": "high",
358	      "cm_diag": 0.8,
359	      "sign_flip_rate": 0.0,
360	      "mean_bias_ratio": 1.3646419723077197,
361	      "std_bias_ratio": 0.04332775695145792,
362	      "median_bias_ratio": 1.360116084331428,
363	      "tau_true": 0.49864566446565145,
364	      "mean_tau_hat": 0.6804728030391003,
365	      "n_reps": 100
366	    },
367	    {
368	      "topology": "mediation",
369	      "K": 3,
370	      "epsilon": 0.05,
371	      "cm_quality": "high",
372	      "cm_diag": 0.8,
373	      "sign_flip_rate": 0.0,
374	      "mean_bias_ratio": 1.4199640859060607,
375	      "std_bias_ratio": 0.04691426808938765,
376	      "median_bias_ratio": 1.4231726756432637,
377	      "tau_true": 0.49864566446565145,
378	      "mean_tau_hat": 0.708058935133989,
379	      "n_reps": 100
380	    },
381	    {
382	      "topology": "mediation",
383	      "K": 3,
384	      "epsilon": 0.1,
385	      "cm_quality": "high",
386	      "cm_diag": 0.8,
387	      "sign_flip_rate": 0.0,
388	      "mean_bias_ratio": 1.4682103635818031,
389	      "std_bias_ratio": 0.0475362211193015,
390	      "median_bias_ratio": 1.4731215705079177,
391	      "tau_true": 0.49864566446565145,
392	      "mean_tau_hat": 0.7321167323236041,
393	      "n_reps": 100
394	    },
395	    {
396	      "topology": "mediation",
397	      "K": 3,
398	      "epsilon": 0.0,
399	      "cm_quality": "medium",
400	      "cm_diag": 0.6,
401	      "sign_flip_rate": 0.0,
402	      "mean_bias_ratio": 1.5225629090017387,
403	      "std_bias_ratio": 0.04458324603715789,
404	      "median_bias_ratio": 1.5194473713291488,
405	      "tau_true": 0.49864566446565145,
406	      "mean_tau_hat": 0.7592193934499272,
407	      "n_reps": 100
408	    },
409	    {
410	      "topology": "mediation",
411	      "K": 3,
412	      "epsilon": 0.01,
413	      "cm_quality": "medium",
414	      "cm_diag": 0.6,
415	      "sign_flip_rate": 0.0,
416	      "mean_bias_ratio": 1.5332635313891083,
417	      "std_bias_ratio": 0.038143205554378404,
418	      "median_bias_ratio": 1.5280106508709852,
419	      "tau_true": 0.49864566446565145,
420	      "mean_tau_hat": 0.7645552124104728,
421	      "n_reps": 100
422	    },
423	    {
424	      "topology": "mediation",
425	      "K": 3,
426	      "epsilon": 0.05,
427	      "cm_quality": "medium",
428	      "cm_diag": 0.6,
429	      "sign_flip_rate": 0.0,
430	      "mean_bias_ratio": 1.562676900600546,
431	      "std_bias_ratio": 0.05048731485448336,
432	      "median_bias_ratio": 1.5596625660254526,
433	      "tau_true": 0.49864566446565145,
434	      "mean_tau_hat": 0.7792220614450841,
435	      "n_reps": 100
436	    },
437	    {
438	      "topology": "mediation",
439	      "K": 3,
440	      "epsilon": 0.1,
441	      "cm_quality": "medium",
442	      "cm_diag": 0.6,
443	      "sign_flip_rate": 0.0,
444	      "mean_bias_ratio": 1.579742202690366,
445	      "std_bias_ratio": 0.04276370220011484,
446	      "median_bias_ratio": 1.5782419790844595,
447	      "tau_true": 0.49864566446565145,
448	      "mean_tau_hat": 0.7877316003449694,
449	      "n_reps": 100
450	    },
451	    {
452	      "topology": "mediation",
453	      "K": 3,
454	      "epsilon": 0.0,
455	      "cm_quality": "low",
456	      "cm_diag": 0.4,
457	      "sign_flip_rate": 0.0,
458	      "mean_bias_ratio": 1.608352935905647,
459	      "std_bias_ratio": 0.039751209962390996,
460	      "median_bias_ratio": 1.6076047915348428,
461	      "tau_true": 0.49864566446565145,
462	      "mean_tau_hat": 0.8019982184199526,
463	      "n_reps": 100
464	    },
465	    {
466	      "topology": "mediation",
467	      "K": 3,
468	      "epsilon": 0.01,
469	      "cm_quality": "low",
470	      "cm_diag": 0.4,
471	      "sign_flip_rate": 0.0,
472	      "mean_bias_ratio": 1.6134137979991263,
473	      "std_bias_ratio": 0.047694587210794115,
474	      "median_bias_ratio": 1.6088097298805142,
475	      "tau_true": 0.49864566446565145,
476	      "mean_tau_hat": 0.804521795361325,
477	      "n_reps": 100
478	    },
479	    {
480	      "topology": "mediation",
481	      "K": 3,
482	      "epsilon": 0.05,
483	      "cm_quality": "low",
484	      "cm_diag": 0.4,
485	      "sign_flip_rate": 0.0,
486	      "mean_bias_ratio": 1.6211411592940104,
487	      "std_bias_ratio": 0.04673806459097569,
488	      "median_bias_ratio": 1.620522922684714,
489	      "tau_true": 0.49864566446565145,
490	      "mean_tau_hat": 0.8083750105687783,
491	      "n_reps": 100
492	    },
493	    {
494	      "topology": "mediation",
495	      "K": 3,
496	      "epsilon": 0.1,
497	      "cm_quality": "low",
498	      "cm_diag": 0.4,
499	      "sign_flip_rate": 0.0,
500	      "mean_bias_ratio": 1.6069671024739884,
501	      "std_bias_ratio": 0.04655806979826811,
502	      "median_bias_ratio": 1.6065449569467631,
503	      "tau_true": 0.49864566446565145,
504	      "mean_tau_hat": 0.8013071785875846,
505	      "n_reps": 100
506	    },
507	    {
508	      "topology": "mediation",
509	      "K": 10,
510	      "epsilon": 0.0,
511	      "cm_quality": "high",
512	      "cm_diag": 0.8,
513	      "sign_flip_rate": 0.0,
514	      "mean_bias_ratio": 1.143217997855835,
515	      "std_bias_ratio": 0.043629896186340084,
516	      "median_bias_ratio": 1.1423842433179145,
517	      "tau_true": 0.502447034804768,
518	      "mean_tau_hat": 0.5744064931581081,
519	      "n_reps": 100
520	    },
521	    {
522	      "topology": "mediation",
523	      "K": 10,
524	      "epsilon": 0.01,
525	      "cm_quality": "high",
526	      "cm_diag": 0.8,
527	      "sign_flip_rate": 0.0,
528	      "mean_bias_ratio": 1.1742997326506033,
529	      "std_bias_ratio": 0.03943002568744982,
530	      "median_bias_ratio": 1.1744770250212921,
531	      "tau_true": 0.502447034804768,
532	      "mean_tau_hat": 0.5900234186423274,
533	      "n_reps": 100
534	    },
535	    {
536	      "topology": "mediation",
537	      "K": 10,
538	      "epsilon": 0.05,
539	      "cm_quality": "high",
540	      "cm_diag": 0.8,
541	      "sign_flip_rate": 0.0,
542	      "mean_bias_ratio": 1.246777507438234,
543	      "std_bias_ratio": 0.041051772703279615,
544	      "median_bias_ratio": 1.2452472903744343,
545	      "tau_true": 0.502447034804768,
546	      "mean_tau_hat": 0.6264396616736202,
547	      "n_reps": 100
548	    },
549	    {
550	      "topology": "mediation",
551	      "K": 10,
552	      "epsilon": 0.1,
553	      "cm_quality": "high",
554	      "cm_diag": 0.8,
555	      "sign_flip_rate": 0.0,
556	      "mean_bias_ratio": 1.2803847905995158,
557	      "std_bias_ratio": 0.042581605942008625,
558	      "median_bias_ratio": 1.2784025432666424,
559	      "tau_true": 0.502447034804768,
560	      "mean_tau_hat": 0.6433255414458506,
561	      "n_reps": 100
562	    },
563	    {
564	      "topology": "mediation",
565	      "K": 10,
566	      "epsilon": 0.0,
567	      "cm_quality": "medium",
568	      "cm_diag": 0.6,
569	      "sign_flip_rate": 0.0,
570	      "mean_bias_ratio": 1.238114186136252,
571	      "std_bias_ratio": 0.04548121654553158,
572	      "median_bias_ratio": 1.241838193138944,
573	      "tau_true": 0.502447034804768,
574	      "mean_tau_hat": 0.6220868015738784,
575	      "n_reps": 100
576	    },
577	    {
578	      "topology": "mediation",
579	      "K": 10,
580	      "epsilon": 0.01,
581	      "cm_quality": "medium",
582	      "cm_diag": 0.6,
583	      "sign_flip_rate": 0.0,
584	      "mean_bias_ratio": 1.257897207825517,
585	      "std_bias_ratio": 0.04709374290106426,
586	      "median_bias_ratio": 1.2542540108658042,
587	      "tau_true": 0.502447034804768,
588	      "mean_tau_hat": 0.6320267221611282,
589	      "n_reps": 100
590	    },
591	    {
592	      "topology": "mediation",
593	      "K": 10,
594	      "epsilon": 0.05,
595	      "cm_quality": "medium",
596	      "cm_diag": 0.6,
597	      "sign_flip_rate": 0.0,
598	      "mean_bias_ratio": 1.3031048976007797,
599	      "std_bias_ratio": 0.04194591257170945,
600	      "median_bias_ratio": 1.2996638410638228,
601	      "tau_true": 0.502447034804768,
602	      "mean_tau_hat": 0.6547411918390827,
603	      "n_reps": 100
604	    },
605	    {
606	      "topology": "mediation",
607	      "K": 10,
608	      "epsilon": 0.1,
609	      "cm_quality": "medium",
610	      "cm_diag": 0.6,
611	      "sign_flip_rate": 0.0,
612	      "mean_bias_ratio": 1.3195098621301553,
613	      "std_bias_ratio": 0.04103622963297477,
614	      "median_bias_ratio": 1.326545258753713,
615	      "tau_true": 0.502447034804768,
616	      "mean_tau_hat": 0.6629838176229447,
617	      "n_reps": 100
618	    },
619	    {
620	      "topology": "mediation",
621	      "K": 10,
622	      "epsilon": 0.0,
623	      "cm_quality": "low",
624	      "cm_diag": 0.4,
625	      "sign_flip_rate": 0.0,
626	      "mean_bias_ratio": 1.303068249332692,
627	      "std_bias_ratio": 0.04373603836890188,
628	      "median_bias_ratio": 1.3008251991504514,
629	      "tau_true": 0.502447034804768,
630	      "mean_tau_hat": 0.6547227780254512,
631	      "n_reps": 100
632	    },
633	    {
634	      "topology": "mediation",
635	      "K": 10,
636	      "epsilon": 0.01,
637	      "cm_quality": "low",
638	      "cm_diag": 0.4,
639	      "sign_flip_rate": 0.0,
640	      "mean_bias_ratio": 1.3195960290418245,
641	      "std_bias_ratio": 0.04640090905822084,
642	      "median_bias_ratio": 1.3211353356849138,
643	      "tau_true": 0.502447034804768,
644	      "mean_tau_hat": 0.6630271119322111,
645	      "n_reps": 100
646	    },
647	    {
648	      "topology": "mediation",
649	      "K": 10,
650	      "epsilon": 0.05,
651	      "cm_quality": "low",
652	      "cm_diag": 0.4,
653	      "sign_flip_rate": 0.0,
654	      "mean_bias_ratio": 1.3289734571521683,
655	      "std_bias_ratio": 0.04543295492783841,
656	      "median_bias_ratio": 1.3228318580498162,
657	      "tau_true": 0.502447034804768,
658	      "mean_tau_hat": 0.6677387728803486,
659	      "n_reps": 100
660	    },
661	    {
662	      "topology": "mediation",
663	      "K": 10,
664	      "epsilon": 0.1,
665	      "cm_quality": "low",
666	      "cm_diag": 0.4,
667	      "sign_flip_rate": 0.0,
668	      "mean_bias_ratio": 1.3424192218184845,
669	      "std_bias_ratio": 0.04296182248773736,
670	      "median_bias_ratio": 1.3394030786208235,
671	      "tau_true": 0.502447034804768,
672	      "mean_tau_hat": 0.6744945574676217,
673	      "n_reps": 100
674	    },
675	    {
676	      "topology": "exposure",
677	      "K": 3,
678	      "epsilon": 0.0,
679	      "cm_quality": "high",
680	      "cm_diag": 0.8,
681	      "sign_flip_rate": 0.0,
682	      "mean_bias_ratio": 0.7161608063896321,
683	      "std_bias_ratio": 0.024560356708756406,
684	      "median_bias_ratio": 0.7142702035305357,
685	      "tau_true": 0.9992677787160825,
686	      "mean_tau_hat": 0.715636418204486,
687	      "n_reps": 100
688	    },
689	    {
690	      "topology": "exposure",
691	      "K": 3,
692	      "epsilon": 0.01,
693	      "cm_quality": "high",
694	      "cm_diag": 0.8,
695	      "sign_flip_rate": 0.0,
696	      "mean_bias_ratio": 0.7072036294030712,
697	      "std_bias_ratio": 0.023510845545163344,
698	      "median_bias_ratio": 0.7068861371381538,
699	      "tau_true": 0.9992677787160825,
700	      "mean_tau_hat": 0.7066857998535585,
701	      "n_reps": 100
702	    },
703	    {
704	      "topology": "exposure",
705	      "K": 3,
706	      "epsilon": 0.05,
707	      "cm_quality": "high",
708	      "cm_diag": 0.8,
709	      "sign_flip_rate": 0.0,
710	      "mean_bias_ratio": 0.671506596790726,
711	      "std_bias_ratio": 0.024856746741565808,
712	      "median_bias_ratio": 0.6741302791483557,
713	      "tau_true": 0.9992677787160825,
714	      "mean_tau_hat": 0.6710149053682646,
715	      "n_reps": 100
716	    },
717	    {
718	      "topology": "exposure",
719	      "K": 3,
720	      "epsilon": 0.1,
721	      "cm_quality": "high",
722	      "cm_diag": 0.8,
723	      "sign_flip_rate": 0.0,
724	      "mean_bias_ratio": 0.6388182664350872,
725	      "std_bias_ratio": 0.024772618046583424,
726	      "median_bias_ratio": 0.6389781337860706,
727	      "tau_true": 0.9992677787160825,
728	      "mean_tau_hat": 0.6383505101038482,
729	      "n_reps": 100
730	    },
731	    {
732	      "topology": "exposure",
733	      "K": 3,
734	      "epsilon": 0.0,
735	      "cm_quality": "medium",
736	      "cm_diag": 0.6,
737	      "sign_flip_rate": 0.0,
738	      "mean_bias_ratio": 0.41761375731948464,
739	      "std_bias_ratio": 0.022827435889457928,
740	      "median_bias_ratio": 0.41960328776456407,
741	      "tau_true": 0.9992677787160825,
742	      "mean_tau_hat": 0.41730797163791844,
743	      "n_reps": 100
744	    },
745	    {
746	      "topology": "exposure",
747	      "K": 3,
748	      "epsilon": 0.01,
749	      "cm_quality": "medium",
750	      "cm_diag": 0.6,
751	      "sign_flip_rate": 0.0,
752	      "mean_bias_ratio": 0.40922314922453124,
753	      "std_bias_ratio": 0.023099770848605598,
754	      "median_bias_ratio": 0.4097045213643991,
755	      "tau_true": 0.9992677787160825,
756	      "mean_tau_hat": 0.40892350732479726,
757	      "n_reps": 100
758	    },
759	    {
760	      "topology": "exposure",
761	      "K": 3,
762	      "epsilon": 0.05,
763	      "cm_quality": "medium",
764	      "cm_diag": 0.6,
765	      "sign_flip_rate": 0.0,
766	      "mean_bias_ratio": 0.38292988477786066,
767	      "std_bias_ratio": 0.030239688774941337,
768	      "median_bias_ratio": 0.38721227542684344,
769	      "tau_true": 0.9992677787160825,
770	      "mean_tau_hat": 0.38264949536597825,
771	      "n_reps": 100
772	    },
773	    {
774	      "topology": "exposure",
775	      "K": 3,
776	      "epsilon": 0.1,
777	      "cm_quality": "medium",
778	      "cm_diag": 0.6,
779	      "sign_flip_rate": 0.0,
780	      "mean_bias_ratio": 0.3489981220120875,
781	      "std_bias_ratio": 0.02831455840776172,
782	      "median_bias_ratio": 0.34682839692838374,
783	      "tau_true": 0.9992677787160825,
784	      "mean_tau_hat": 0.34874257815910303,
785	      "n_reps": 100
786	    },
787	    {
788	      "topology": "exposure",
789	      "K": 3,
790	      "epsilon": 0.0,
791	      "cm_quality": "low",
792	      "cm_diag": 0.4,
793	      "sign_flip_rate": 0.0,
794	      "mean_bias_ratio": 0.10827976043378781,
795	      "std_bias_ratio": 0.030919288144696012,
796	      "median_bias_ratio": 0.10848991029258795,
797	      "tau_true": 0.9992677787160825,
798	      "mean_tau_hat": 0.10820047568858071,
799	      "n_reps": 100
800	    },
801	    {
802	      "topology": "exposure",
803	      "K": 3,
804	      "epsilon": 0.01,
805	      "cm_quality": "low",
806	      "cm_diag": 0.4,
807	      "sign_flip_rate": 0.0,
808	      "mean_bias_ratio": 0.10277106410684832,
809	      "std_bias_ratio": 0.0289014041610935,
810	      "median_bias_ratio": 0.1020446547834177,
811	      "tau_true": 0.9992677787160825,
812	      "mean_tau_hat": 0.10269581294633844,
813	      "n_reps": 100
814	    },
815	    {
816	      "topology": "exposure",
817	      "K": 3,
818	      "epsilon": 0.05,
819	      "cm_quality": "low",
820	      "cm_diag": 0.4,
821	      "sign_flip_rate": 0.01,
822	      "mean_bias_ratio": 0.07573663008739732,
823	      "std_bias_ratio": 0.027566247636617077,
824	      "median_bias_ratio": 0.07607442414479154,
825	      "tau_true": 0.9992677787160825,
826	      "mean_tau_hat": 0.07547384365351574,
827	      "n_reps": 100
828	    },
829	    {
830	      "topology": "exposure",
831	      "K": 3,
832	      "epsilon": 0.1,
833	      "cm_quality": "low",
834	      "cm_diag": 0.4,
835	      "sign_flip_rate": 0.05,
836	      "mean_bias_ratio": 0.05535013206286603,
837	      "std_bias_ratio": 0.026652768849165273,
838	      "median_bias_ratio": 0.05333502853590038,
839	      "tau_true": 0.9992677787160825,
840	      "mean_tau_hat": 0.052958307135343,
841	      "n_reps": 100
842	    },
843	    {
844	      "topology": "exposure",
845	      "K": 10,
846	      "epsilon": 0.0,
847	      "cm_quality": "high",
848	      "cm_diag": 0.8,
849	      "sign_flip_rate": 0.0,
850	      "mean_bias_ratio": 0.8698290572995012,
851	      "std_bias_ratio": 0.031083347353167808,
852	      "median_bias_ratio": 0.8714092833061509,
853	      "tau_true": 1.0012856517288142,
854	      "mean_tau_hat": 0.8709473545307914,
855	      "n_reps": 100
856	    },
857	    {
858	      "topology": "exposure",
859	      "K": 10,
860	      "epsilon": 0.01,
861	      "cm_quality": "high",
862	      "cm_diag": 0.8,
863	      "sign_flip_rate": 0.0,
864	      "mean_bias_ratio": 0.8604658352728708,
865	      "std_bias_ratio": 0.03326309307960338,
866	      "median_bias_ratio": 0.8619374598482635,
867	      "tau_true": 1.0012856517288142,
868	      "mean_tau_hat": 0.8615720946615751,
869	      "n_reps": 100
870	    },
871	    {
872	      "topology": "exposure",
873	      "K": 10,
874	      "epsilon": 0.05,
875	      "cm_quality": "high",
876	      "cm_diag": 0.8,
877	      "sign_flip_rate": 0.0,
878	      "mean_bias_ratio": 0.8356775865532703,
879	      "std_bias_ratio": 0.03577655505635858,
880	      "median_bias_ratio": 0.8332673741979196,
881	      "tau_true": 1.0012856517288142,
882	      "mean_tau_hat": 0.8367519768871535,
883	      "n_reps": 100
884	    },
885	    {
886	      "topology": "exposure",
887	      "K": 10,
888	      "epsilon": 0.1,
889	      "cm_quality": "high",
890	      "cm_diag": 0.8,
891	      "sign_flip_rate": 0.0,
892	      "mean_bias_ratio": 0.8039091836728415,
893	      "std_bias_ratio": 0.03737006966859953,
894	      "median_bias_ratio": 0.8091813297558388,
895	      "tau_true": 1.0012856517288142,
896	      "mean_tau_hat": 0.80494273090464,
897	      "n_reps": 100
898	    },
899	    {
900	      "topology": "exposure",
901	      "K": 10,
902	      "epsilon": 0.0,
903	      "cm_quality": "medium",
904	      "cm_diag": 0.6,
905	      "sign_flip_rate": 0.0,
906	      "mean_bias_ratio": 0.7070857415163714,
907	      "std_bias_ratio": 0.039582425650093254,
908	      "median_bias_ratio": 0.7046890853931056,
909	      "tau_true": 1.0012856517288142,
910	      "mean_tau_hat": 0.7079948075223719,
911	      "n_reps": 100
912	    },
913	    {
914	      "topology": "exposure",
915	      "K": 10,
916	      "epsilon": 0.01,
917	      "cm_quality": "medium",
918	      "cm_diag": 0.6,
919	      "sign_flip_rate": 0.0,
920	      "mean_bias_ratio": 0.6955660286895836,
921	      "std_bias_ratio": 0.03906080004325408,
922	      "median_bias_ratio": 0.6973132688146657,
923	      "tau_true": 1.0012856517288142,
924	      "mean_tau_hat": 0.696460284356873,
925	      "n_reps": 100
926	    },
927	    {
928	      "topology": "exposure",
929	      "K": 10,
930	      "epsilon": 0.05,
931	      "cm_quality": "medium",
932	      "cm_diag": 0.6,
933	      "sign_flip_rate": 0.0,
934	      "mean_bias_ratio": 0.665031026567739,
935	      "std_bias_ratio": 0.037844294621680985,
936	      "median_bias_ratio": 0.6661324913148754,
937	      "tau_true": 1.0012856517288142,
938	      "mean_tau_hat": 0.6658860248567611,
939	      "n_reps": 100
940	    },
941	    {
942	      "topology": "exposure",
943	      "K": 10,
944	      "epsilon": 0.1,
945	      "cm_quality": "medium",
946	      "cm_diag": 0.6,
947	      "sign_flip_rate": 0.0,
948	      "mean_bias_ratio": 0.636639857730211,
949	      "std_bias_ratio": 0.0335821942165541,
950	      "median_bias_ratio": 0.6388187421055085,
951	      "tau_true": 1.0012856517288142,
952	      "mean_tau_hat": 0.637458354863934,
953	      "n_reps": 100
954	    },
955	    {
956	      "topology": "exposure",
957	      "K": 10,
958	      "epsilon": 0.0,
959	      "cm_quality": "low",
960	      "cm_diag": 0.4,
961	      "sign_flip_rate": 0.0,
962	      "mean_bias_ratio": 0.4946296349539494,
963	      "std_bias_ratio": 0.04407034000185526,
964	      "median_bias_ratio": 0.4925822861840872,
965	      "tau_true": 1.0012856517288142,
966	      "mean_tau_hat": 0.49526555639925063,
967	      "n_reps": 100
968	    },
969	    {
970	      "topology": "exposure",
971	      "K": 10,
972	      "epsilon": 0.01,
973	      "cm_quality": "low",
974	      "cm_diag": 0.4,
975	      "sign_flip_rate": 0.0,
976	      "mean_bias_ratio": 0.47409409319354134,
977	      "std_bias_ratio": 0.04073827047582584,
978	      "median_bias_ratio": 0.4727676267616459,
979	      "tau_true": 1.0012856517288142,
980	      "mean_tau_hat": 0.47470361308407627,
981	      "n_reps": 100
982	    },
983	    {
984	      "topology": "exposure",
985	      "K": 10,
986	      "epsilon": 0.05,
987	      "cm_quality": "low",
988	      "cm_diag": 0.4,
989	      "sign_flip_rate": 0.0,
990	      "mean_bias_ratio": 0.4557486210483655,
991	      "std_bias_ratio": 0.0367342542351889,
992	      "median_bias_ratio": 0.45707435853709477,
993	      "tau_true": 1.0012856517288142,
994	      "mean_tau_hat": 0.456334555050921,
995	      "n_reps": 100
996	    },
997	    {
998	      "topology": "exposure",
999	      "K": 10,
1000	      "epsilon": 0.1,
1001	      "cm_quality": "low",
1002	      "cm_diag": 0.4,
1003	      "sign_flip_rate": 0.0,
1004	      "mean_bias_ratio": 0.42640604141529836,
1005	      "std_bias_ratio": 0.04533711192676004,
1006	      "median_bias_ratio": 0.4239613979945344,
1007	      "tau_true": 1.0012856517288142,
1008	      "mean_tau_hat": 0.4269542510796207,
1009	      "n_reps": 100
1010	    },
1011	    {
1012	      "topology": "iv",
1013	      "K": 3,
1014	      "epsilon": 0.0,
1015	      "cm_quality": "high",
1016	      "cm_diag": 0.8,
1017	      "sign_flip_rate": 0.0,
1018	      "mean_bias_ratio": 1.4193250775982407,
1019	      "std_bias_ratio": 0.2455200904039936,
1020	      "median_bias_ratio": 1.4577633388367874,
1021	      "tau_true": 0.6666990731411736,
1022	      "mean_tau_hat": 0.9462627137207711,
1023	      "n_reps": 100
1024	    },
1025	    {
1026	      "topology": "iv",
1027	      "K": 3,
1028	      "epsilon": 0.01,
1029	      "cm_quality": "high",
1030	      "cm_diag": 0.8,
1031	      "sign_flip_rate": 0.0,
1032	      "mean_bias_ratio": 1.45002853850117,
1033	      "std_bias_ratio": 0.2146613588579534,
1034	      "median_bias_ratio": 1.4571521185130831,
1035	      "tau_true": 0.6666990731411736,
1036	      "mean_tau_hat": 0.9667326826469804,
1037	      "n_reps": 100
1038	    },
1039	    {
1040	      "topology": "iv",
1041	      "K": 3,
1042	      "epsilon": 0.05,
1043	      "cm_quality": "high",
1044	      "cm_diag": 0.8,
1045	      "sign_flip_rate": 0.0,
1046	      "mean_bias_ratio": 1.5826747292864127,
1047	      "std_bias_ratio": 0.2526544921622263,
1048	      "median_bias_ratio": 1.5611088292263622,
1049	      "tau_true": 0.6666990731411736,
1050	      "mean_tau_hat": 1.0551677750992092,
1051	      "n_reps": 100
1052	    },
1053	    {
1054	      "topology": "iv",
1055	      "K": 3,
1056	      "epsilon": 0.1,
1057	      "cm_quality": "high",
1058	      "cm_diag": 0.8,
1059	      "sign_flip_rate": 0.0,
1060	      "mean_bias_ratio": 1.6872003009143657,
1061	      "std_bias_ratio": 0.2574674685166349,
1062	      "median_bias_ratio": 1.719193566487017,
1063	      "tau_true": 0.6666990731411736,
1064	      "mean_tau_hat": 1.1248548768231166,
1065	      "n_reps": 100
1066	    },
1067	    {
1068	      "topology": "iv",
1069	      "K": 3,
1070	      "epsilon": 0.0,
1071	      "cm_quality": "medium",
1072	      "cm_diag": 0.6,
1073	      "sign_flip_rate": 0.0,
1074	      "mean_bias_ratio": 2.558064844977355,
1075	      "std_bias_ratio": 0.4919804632869496,
1076	      "median_bias_ratio": 2.487483679095103,
1077	      "tau_true": 0.6666990731411736,
1078	      "mean_tau_hat": 1.7054594611814224,
1079	      "n_reps": 100
1080	    },
1081	    {
1082	      "topology": "iv",
1083	      "K": 3,
1084	      "epsilon": 0.01,
1085	      "cm_quality": "medium",
1086	      "cm_diag": 0.6,
1087	      "sign_flip_rate": 0.0,
1088	      "mean_bias_ratio": 2.5168276572425565,
1089	      "std_bias_ratio": 0.3926225664676824,
1090	      "median_bias_ratio": 2.538639414981175,
1091	      "tau_true": 0.6666990731411736,
1092	      "mean_tau_hat": 1.6779666663396835,
1093	      "n_reps": 100
1094	    },
1095	    {
1096	      "topology": "iv",
1097	      "K": 3,
1098	      "epsilon": 0.05,
1099	      "cm_quality": "medium",
1100	      "cm_diag": 0.6,
1101	      "sign_flip_rate": 0.0,
1102	      "mean_bias_ratio": 2.872740547400296,
1103	      "std_bias_ratio": 0.5365371467430607,
1104	      "median_bias_ratio": 2.865789927102919,
1105	      "tau_true": 0.6666990731411736,
1106	      "mean_tau_hat": 1.9152534603268456,
1107	      "n_reps": 100
1108	    },
1109	    {
1110	      "topology": "iv",
1111	      "K": 3,
1112	      "epsilon": 0.1,
1113	      "cm_quality": "medium",
1114	      "cm_diag": 0.6,
1115	      "sign_flip_rate": 0.0,
1116	      "mean_bias_ratio": 3.1159759304274415,
1117	      "std_bias_ratio": 0.5365223218436266,
1118	      "median_bias_ratio": 3.1280072372059298,
1119	      "tau_true": 0.6666990731411736,
1120	      "mean_tau_hat": 2.077418264746181,
1121	      "n_reps": 100
1122	    },
1123	    {
1124	      "topology": "iv",
1125	      "K": 3,
1126	      "epsilon": 0.0,
1127	      "cm_quality": "low",
1128	      "cm_diag": 0.4,
1129	      "sign_flip_rate": 0.0,
1130	      "mean_bias_ratio": 12.788534495069698,
1131	      "std_bias_ratio": 8.14270269785842,
1132	      "median_bias_ratio": 10.761470520021781,
1133	      "tau_true": 0.6666990731411736,
1134	      "mean_tau_hat": 8.526104094696894,
1135	      "n_reps": 100
1136	    },
1137	    {
1138	      "topology": "iv",
1139	      "K": 3,
1140	      "epsilon": 0.01,
1141	      "cm_quality": "low",
1142	      "cm_diag": 0.4,
1143	      "sign_flip_rate": 0.0,
1144	      "mean_bias_ratio": 12.212825018585699,
1145	      "std_bias_ratio": 8.42356742667469,
1146	      "median_bias_ratio": 10.579847314826779,
1147	      "tau_true": 0.6666990731411736,
1148	      "mean_tau_hat": 8.142279120326421,
1149	      "n_reps": 100
1150	    },
1151	    {
1152	      "topology": "iv",
1153	      "K": 3,
1154	      "epsilon": 0.05,
1155	      "cm_quality": "low",
1156	      "cm_diag": 0.4,
1157	      "sign_flip_rate": 0.02,
1158	      "mean_bias_ratio": 19.967132753379886,
1159	      "std_bias_ratio": 20.525472569889214,
1160	      "median_bias_ratio": 14.354850624156075,
1161	      "tau_true": 0.6666990731411736,
1162	      "mean_tau_hat": 10.33427214361116,
1163	      "n_reps": 100
1164	    },
1165	    {
1166	      "topology": "iv",
1167	      "K": 3,
1168	      "epsilon": 0.1,
1169	      "cm_quality": "low",
1170	      "cm_diag": 0.4,
1171	      "sign_flip_rate": 0.07,
1172	      "mean_bias_ratio": 43.44357485987513,
1173	      "std_bias_ratio": 90.47261087642586,
1174	      "median_bias_ratio": 22.367563004909332,
1175	      "tau_true": 0.6666990731411736,
1176	      "mean_tau_hat": 14.943194023179304,
1177	      "n_reps": 100
1178	    },
1179	    {
1180	      "topology": "iv",
1181	      "K": 10,
1182	      "epsilon": 0.0,
1183	      "cm_quality": "high",
1184	      "cm_diag": 0.8,
1185	      "sign_flip_rate": 0.0,
1186	      "mean_bias_ratio": 1.302212032632124,
1187	      "std_bias_ratio": 0.3588248378520567,
1188	      "median_bias_ratio": 1.2647472065542682,
1189	      "tau_true": 1.1078725942319758,
1190	      "mean_tau_hat": 1.4426850228322448,
1191	      "n_reps": 100
1192	    },
1193	    {
1194	      "topology": "iv",
1195	      "K": 10,
1196	      "epsilon": 0.01,
1197	      "cm_quality": "high",
1198	      "cm_diag": 0.8,
1199	      "sign_flip_rate": 0.0,
1200	      "mean_bias_ratio": 1.4382921048931434,
1201	      "std_bias_ratio": 0.41421215737713224,
1202	      "median_bias_ratio": 1.437661856374808,
1203	      "tau_true": 1.1078725942319758,
1204	      "mean_tau_hat": 1.593444405511336,
1205	      "n_reps": 100
1206	    },
1207	    {
1208	      "topology": "iv",
1209	      "K": 10,
1210	      "epsilon": 0.05,
1211	      "cm_quality": "high",
1212	      "cm_diag": 0.8,
1213	      "sign_flip_rate": 0.0,
1214	      "mean_bias_ratio": 1.710802203083366,
1215	      "std_bias_ratio": 0.44162185101179036,
1216	      "median_bias_ratio": 1.7173207515156017,
1217	      "tau_true": 1.1078725942319758,
1218	      "mean_tau_hat": 1.8953508749477483,
1219	      "n_reps": 100
1220	    },
1221	    {
1222	      "topology": "iv",
1223	      "K": 10,
1224	      "epsilon": 0.1,
1225	      "cm_quality": "high",
1226	      "cm_diag": 0.8,
1227	      "sign_flip_rate": 0.0,
1228	      "mean_bias_ratio": 2.027041978673395,
1229	      "std_bias_ratio": 0.5973878736975435,
1230	      "median_bias_ratio": 2.0220051182105463,
1231	      "tau_true": 1.1078725942319758,
1232	      "mean_tau_hat": 2.245704255530011,
1233	      "n_reps": 100
1234	    },
1235	    {
1236	      "topology": "iv",
1237	      "K": 10,
1238	      "epsilon": 0.0,
1239	      "cm_quality": "medium",
1240	      "cm_diag": 0.6,
1241	      "sign_flip_rate": 0.0,
1242	      "mean_bias_ratio": 1.8282147741311485,
1243	      "std_bias_ratio": 0.5275990866318235,
1244	      "median_bias_ratio": 1.7629017180010313,
1245	      "tau_true": 1.1078725942319758,
1246	      "mean_tau_hat": 2.0254290446299015,
1247	      "n_reps": 100
1248	    },
1249	    {
1250	      "topology": "iv",
1251	      "K": 10,
1252	      "epsilon": 0.01,
1253	      "cm_quality": "medium",
1254	      "cm_diag": 0.6,
1255	      "sign_flip_rate": 0.0,
1256	      "mean_bias_ratio": 1.9639268474193707,
1257	      "std_bias_ratio": 0.5451074127007722,
1258	      "median_bias_ratio": 1.9751256263410866,
1259	      "tau_true": 1.1078725942319758,
1260	      "mean_tau_hat": 2.1757807313323236,
1261	      "n_reps": 100
1262	    },
1263	    {
1264	      "topology": "iv",
1265	      "K": 10,
1266	      "epsilon": 0.05,
1267	      "cm_quality": "medium",
1268	      "cm_diag": 0.6,
1269	      "sign_flip_rate": 0.0,
1270	      "mean_bias_ratio": 2.431888270126432,
1271	      "std_bias_ratio": 0.65221899126093,
1272	      "median_bias_ratio": 2.3669518367581444,
1273	      "tau_true": 1.1078725942319758,
1274	      "mean_tau_hat": 2.694222366707283,
1275	      "n_reps": 100
1276	    },
1277	    {
1278	      "topology": "iv",
1279	      "K": 10,
1280	      "epsilon": 0.1,
1281	      "cm_quality": "medium",
1282	      "cm_diag": 0.6,
1283	      "sign_flip_rate": 0.0,
1284	      "mean_bias_ratio": 2.836823881106221,
1285	      "std_bias_ratio": 0.8474125578330213,
1286	      "median_bias_ratio": 2.7288393573158745,
1287	      "tau_true": 1.1078725942319758,
1288	      "mean_tau_hat": 3.1428394325403715,
1289	      "n_reps": 100
1290	    },
1291	    {
1292	      "topology": "iv",
1293	      "K": 10,
1294	      "epsilon": 0.0,
1295	      "cm_quality": "low",
1296	      "cm_diag": 0.4,
1297	      "sign_flip_rate": 0.0,
1298	      "mean_bias_ratio": 3.1455409867973345,
1299	      "std_bias_ratio": 1.2000437149656704,
1300	      "median_bias_ratio": 2.8974421888565765,
1301	      "tau_true": 1.1078725942319758,
1302	      "mean_tau_hat": 3.484858653306171,
1303	      "n_reps": 100
1304	    },
1305	    {
1306	      "topology": "iv",
1307	      "K": 10,
1308	      "epsilon": 0.01,
1309	      "cm_quality": "low",
1310	      "cm_diag": 0.4,
1311	      "sign_flip_rate": 0.0,
1312	      "mean_bias_ratio": 3.54060620998974,
1313	      "std_bias_ratio": 1.1510725386006417,
1314	      "median_bias_ratio": 3.3509290598207975,
1315	      "tau_true": 1.1078725942319758,
1316	      "mean_tau_hat": 3.9225405870151775,
1317	      "n_reps": 100
1318	    },
1319	    {
1320	      "topology": "iv",
1321	      "K": 10,
1322	      "epsilon": 0.05,
1323	      "cm_quality": "low",
1324	      "cm_diag": 0.4,
1325	      "sign_flip_rate": 0.0,
1326	      "mean_bias_ratio": 4.390113393664934,
1327	      "std_bias_ratio": 1.5239934699256446,
1328	      "median_bias_ratio": 4.293881978743778,
1329	      "tau_true": 1.1078725942319758,
1330	      "mean_tau_hat": 4.863686314412114,
1331	      "n_reps": 100
1332	    },
1333	    {
1334	      "topology": "iv",
1335	      "K": 10,
1336	      "epsilon": 0.1,
1337	      "cm_quality": "low",
1338	      "cm_diag": 0.4,
1339	      "sign_flip_rate": 0.0,
1340	      "mean_bias_ratio": 9.6942484382649,
1341	      "std_bias_ratio": 35.18725862001444,
1342	      "median_bias_ratio": 5.433643568575264,
1343	      "tau_true": 1.1078725942319758,
1344	      "mean_tau_hat": 10.739992166429815,
1345	      "n_reps": 100
1346	    }
1347	  ],
1348	  "summary": {
1349	    "by_epsilon": {
1350	      "0.0": {
1351	        "mean_sign_flip_rate": 0.0,
1352	        "mean_bias_ratio": 1.7152050770362337,
1353	        "max_sign_flip_rate": 0.0
1354	      },
1355	      "0.01": {
1356	        "mean_sign_flip_rate": 0.0,
1357	        "mean_bias_ratio": 1.7203632972619898,
1358	        "max_sign_flip_rate": 0.0
1359	      },
1360	      "0.05": {
1361	        "mean_sign_flip_rate": 0.00125,
1362	        "mean_bias_ratio": 2.1338518290181074,
1363	        "max_sign_flip_rate": 0.02
1364	      },
1365	      "0.1": {
1366	        "mean_sign_flip_rate": 0.005,
1367	        "mean_bias_ratio": 3.375907049588784,
1368	        "max_sign_flip_rate": 0.07
1369	      }
1370	    },
1371	    "by_topology": {
1372	      "confounding": {
1373	        "mean_sign_flip_rate": 0.0,
1374	        "mean_bias_ratio": 1.11214747724957
1375	      },
1376	      "mediation": {
1377	        "mean_sign_flip_rate": 0.0,
1378	        "mean_bias_ratio": 1.396334343113992
1379	      },
1380	      "exposure": {
1381	        "mean_sign_flip_rate": 0.0025,
1382	        "mean_bias_ratio": 0.5233197711232052
1383	      },
1384	      "iv": {
1385	        "mean_sign_flip_rate": 0.0037500000000000003,
1386	        "mean_bias_ratio": 5.913525661418348
1387	      }
1388	    },
1389	    "by_K": {
1390	      "3": {
1391	        "mean_sign_flip_rate": 0.0031250000000000006,
1392	        "mean_bias_ratio": 2.9603767653474122
1393	      },
1394	      "10": {
1395	        "mean_sign_flip_rate": 0.0,
1396	        "mean_bias_ratio": 1.5122868611051457
1397	      }
1398	    }
1399	  }
1400	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb5af16d-caf0-456b-9639-0f83adb5bf29",
  "isSidechain": true,
  "promptId": "6231d775-db71-46d9-bac6-397081d485cb",
  "agentId": "a767a9abec38e8eae",
  "type": "user",
  "uuid": "ce828215-0c5c-44dd-be06-5fb456c160f4",
  "sourceToolAssistantUUID": "cb5af16d-caf0-456b-9639-0f83adb5bf29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-23T19:22:20.421Z_

Perfect. I have successfully read all three JSON files completely. Here is a summary of their contents:

## File 1: exp_proportional_effects_results.json

This file contains results testing proportionality conditions in causal effects, with metadata and detailed results across different experimental configurations:

**Metadata:**
- K: 3 estimands
- n_configs: 100,000 configurations tested
- seed: 42
- sigma_values: [0.1, 0.3, 0.5]
- method: synthetic_suff_stats
- p_A: [0.4, 0.35, 0.25]
- timestamp: "2026-05-23 02:12:46"

**Results:** 6 main result groups:
1. **exact_proportional** - f_j - f_0 = lambda * g_j with lambda ~ U(0.1, 0.5): 99,690 valid configs, 844 sign failures, lambda_mean=0.1555
2. **near_proportional_sigma_0.1** - with eps ~ N(0, 0.1²): 99,404 valid, 10,218 out-of-bounds lambdas (10.28% OOB rate)
3. **near_proportional_sigma_0.3** - with eps ~ N(0, 0.3²): 89,843 valid, 17,107 OOB lambdas (19.04% OOB rate)
4. **near_proportional_sigma_0.5** - with eps ~ N(0, 0.5²): 65,948 valid, 14,770 OOB lambdas (22.40% OOB rate)
5. **independent** - f independent of g: 100,000 valid, 22,949 OOB lambdas (22.95%)
6. **default_plan006** - Fixed parameters (delta=[0.0, 0.8, -0.6], beta=[0.0, 1.0, -0.5]): 100,000 valid, 66 OOB lambdas, tau_true=0.4993, tau_total=0.8045, tau_indirect=0.3052

---

## File 2: exp_a_stress_test_results.json

This file tests bias and sign flip rates across different causal model topologies and annotation quality levels:

**Structure:** Results array with 80 entries testing:
- **Topologies:** confounding, mediation, exposure, iv (instrumental variable)
- **K values:** 3 and 10
- **Epsilon levels:** 0.0, 0.01, 0.05, 0.1
- **cm_quality:** high (diag=0.8), medium (diag=0.6), low (diag=0.4)
- **n_reps:** 100 repetitions per configuration

**Key metrics:** For each config:
- sign_flip_rate
- mean_bias_ratio, std_bias_ratio, median_bias_ratio
- tau_true, mean_tau_hat, n_reps

**Summary section:** Aggregated statistics:
- **By epsilon:** Shows increasing bias_ratio and sign_flip_rate with higher epsilon
- **By topology:** 
  - confounding: mean_bias_ratio=1.112
  - mediation: mean_bias_ratio=1.396
  - exposure: mean_bias_ratio=0.523
  - iv: mean_bias_ratio=5.914
- **By K:** K=3 has higher bias_ratio (2.96) than K=10 (1.512)

---

## File 3: exp_b_logistic_results.json

This file evaluates LLM-based causal model identification with 126 result entries:

**Configuration:**
- N: 10,000 samples per simulation
- n_reps: 500 repetitions
- K: 3 (except IV topology)
- Models tested: logistic, linear, control_function, linear_2sls
- LLM models: deepseek_zero-shot, llama4 (zero-shot, few-shot-3, few-shot-5), qwen2.5-7b (few-shot-3, few-shot-5)

**Topologies tested:** confounding, mediation, collider, exposure, mbias, frontdoor, iv

**Key metrics per result:**
- topology, cm_name, model
- sign_flip_rate, tau_sign_flip_rate, dummy_sign_flip_rate
- mean_bias, coef_means[], true_coefs[], n_valid

**Comparison section:** Shows logistic vs linear model performance by topology

**Notable findings:**
- Sign flip rates vary widely by model and prompt strategy
- llama4_few-shot-5 often has low sign flip rates (0.0-0.004)
- qwen2.5 models show higher sign flip rates (0.836-1.0)
- IV topology has highest complexity with control_function and linear_2sls models

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce828215-0c5c-44dd-be06-5fb456c160f4",
  "isSidechain": true,
  "agentId": "a767a9abec38e8eae",
  "requestId": "req_011CbL3XtWEfCeFkvuYRGZvi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "84685555-f9e6-4441-a701-126db544d7df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "e9d5f9d6-ebc0-4e07-b12b-925be82052c1",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Kc73seJXArfq3MwATUPCjE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 22398,
      "cache_creation_input_tokens": 23572,
      "cache_read_input_tokens": 17914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23572,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
