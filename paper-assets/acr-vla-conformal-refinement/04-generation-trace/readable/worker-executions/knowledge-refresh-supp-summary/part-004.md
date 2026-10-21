# knowledge refresh supp summary — Part 4 of 4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[← Part 3](part-003.md) · [Transcript overview](../knowledge-refresh-supp-summary.md) · [Structured JSON](../../../sessions/b0/b0f3eefdfb032bacb274.json)

## Before a recorded user message

### Tool result

_source line 77 · 2026-05-28T16:27:21.332Z_

<details><summary>↩ Tool result · `toolu_01QsRrNVhJJwFfidBhVHpMXX`</summary>

```text
1	# Supplementary Experiment Results
2	
3	All results from registry experiments with status=DONE, conclusion in (success, negative).
4	SR values normalized to percentages. Deduplicated: for same conditions, latest/best run kept.
5	
6	## A. Threshold (τ) Sensitivity Analysis
7	
8	**Total data points: 69** (with valid SR)
9	
10	### pi05 / goal
11	
12	| τ | seed | SR (%) | trigger_rate | source_exp_id |
13	|---|------|--------|-------------|---------------|
14	| 0.15 | 42 | 92.0 | 0.174 | pi05-adaptive-goal-s42-tau015-bjb2 |
15	| 0.15 | 43 | 88.0 | 0.195 | pi05-goal-tau015-s43 |
16	| 0.25 | 43 | 89.0 | 0.093 | pi05-goal-tau025-s43 |
17	| 0.35 | 42 | 87.5 | 0.057 | pi05-adaptive-goal-s42-tau035-bjb2 |
18	| 0.35 | 43 | 90.0 | 0.044 | pi05-goal-tau035-s43 |
19	| 0.5 | 42 | 87.0 | 0.0206 | pi05-tau-sweep-goal-tau050-s42-r3 |
20	| 0.7 | 42 | 87 | 1.1 | pi05-tau-sweep-goal-tau070-s42-r2 |
21	
22	### pi05 / long
23	
24	| τ | seed | SR (%) | trigger_rate | source_exp_id |
25	|---|------|--------|-------------|---------------|
26	| 0.15 | 42 | 84.0 | 0.114 | pi05-adaptive-long-s42-tau015-bjb2 |
27	| 0.15 | 43 | 82 | 11.4 | pi05-long-tau015-s43-r3 |
28	
29	### pi05 / spatial
30	
31	| τ | seed | SR (%) | trigger_rate | source_exp_id |
32	|---|------|--------|-------------|---------------|
33	| 0.15 | 42 | 97.0 | 0.112 | pi05-adaptive-spatial-s42-tau015-bjb2 |
34	| 0.15 | 43 | 96.5 | 0.117 | pi05-spatial-tau015-s43 |
35	| 0.25 | 43 | 98.5 | 0.028 | pi05-spatial-tau025-s43 |
36	| 0.35 | 42 | 96.5 | 0.0255 | pi05-adaptive-spatial-s42-tau035-bjb2 |
37	| 0.35 | 43 | 97.5 | 0.022 | pi05-spatial-tau035-s43 |
38	
39	### smolvla / goal
40	
41	| τ | seed | SR (%) | trigger_rate | source_exp_id |
42	|---|------|--------|-------------|---------------|
43	| 0.1 | 42 | 81.0 | 0.739 | eval-ablation-tau010-goal-s42 |
44	| 0.15 | 42 | 85.5 | 0.333 | smolvla-tau015-goal-s42 |
45	| 0.15 | 43 | 83.5 | 0.354 | smolvla-tau015-goal-s43 |
46	| 0.25 | 42 | 84.0 | 0.083 | smolvla-tau025-goal-s42 |
47	| 0.25 | 43 | 81.0 | 0.0925 | smolvla-tau025-goal-s43 |
48	| 0.25 | 49 | 80.5 | — | eval-goal-adapt-tau025-s49-paired |
49	| 0.35 | 42 | 86 | 2.1 | tau-sweep-goal-tau035-s42 |
50	| 0.35 | 43 | 85.5 | 0.0211 | smolvla-tau035-goal-s43 |
51	| 0.4 | 42 | 83.5 | — | tau_sweep_goal_tau040_s42 |
52	| 0.45 | 42 | 83.5 | — | tau_sweep_goal_tau045_s42 |
53	| 0.5 | 42 | 87.0 | 0.0206 | tau_sweep_goal_tau050_s42_cqa1 |
54	| 0.7 | 42 | 87.0 | 0.0104 | tau_sweep_goal_tau070_s42_cqa1 |
55	| 0.9 | 42 | 89.0 | 0.0035 | tau_sweep_goal_tau090_s42_cqa1 |
56	
57	### smolvla / long
58	
59	| τ | seed | SR (%) | trigger_rate | source_exp_id |
60	|---|------|--------|-------------|---------------|
61	| 0.05 | 42 | 44.0 | 0.9781 | smolvla-tau005-long-s42 |
62	| 0.1 | 42 | 53.5 | 0.613 | smolvla-tau010-long-s42 |
63	| 0.15 | 42 | 61.0 | 0.239 | smolvla-tau015-long-s42 |
64	| 0.15 | 43 | 61.0 | 0.236 | smolvla-tau015-long-s43 |
65	| 0.2 | 42 | 58.5 | 0.089 | smolvla-tau020-long-s42 |
66	| 0.2 | 43 | 54.5 | 11.4 | smolvla-tau020-long-s43-r2 |
67	| 0.25 | 42 | 56.0 | 0.042 | smolvla-tau025-long-s42 |
68	| 0.25 | 43 | 53.0 | 0.046 | smolvla-tau025-long-s43 |
69	| 0.3 | 42 | 54.5 | 1.6 | smolvla-tau030-long-s42-r2 |
70	| 0.3 | 43 | 55.5 | 1.6 | smolvla-tau030-long-s43-r2 |
71	| 0.35 | 42 | 57.5 | 0.013 | smolvla-tau035-long-s42 |
72	| 0.35 | 43 | 60.0 | 0.01 | smolvla-tau035-long-s43 |
73	| 0.4 | 42 | 60.0 | 0.004 | smolvla-tau040-long-s42 |
74	| 0.45 | 42 | 59.5 | 0.003 | smolvla-tau045-long-s42 |
75	
76	### smolvla / object
77	
78	| τ | seed | SR (%) | trigger_rate | source_exp_id |
79	|---|------|--------|-------------|---------------|
80	| 0.05 | 42 | 75 | 94.2 | smolvla-tau005-object-s42 |
81	| 0.1 | 42 | 78 | 44.4 | smolvla-tau010-object-s42 |
82	| 0.15 | 42 | 79 | 0.171 | smolvla-adapt-tau015-object-s42-cqa1 |
83	| 0.15 | 43 | 78 | 0.174 | smolvla-adapt-tau015-object-s43-cqa1 |
84	| 0.15 | 44 | 73.5 | 0.168 | smolvla-adapt-tau015-object-s44-cqa1 |
85	| 0.2 | 42 | 78.5 | 7.1 | smolvla-tau020-object-s42 |
86	| 0.25 | 42 | 81 | 3.5 | smolvla-tau025-object-s42-r3 |
87	| 0.25 | 43 | 77.5 | 0.037 | smolvla-tau025-object-s43-r3 |
88	| 0.3 | 42 | 79.0 | 0.0231 | smolvla-tau030-object-s42 |
89	| 0.35 | 42 | 75 | 1.6 | smolvla-tau035-object-s42-r3 |
90	| 0.35 | 43 | 77.0 | 0.013 | smolvla-tau035-object-s43-r3 |
91	| 0.4 | 42 | 73.5 | 0.0091 | smolvla-tau040-object-s42 |
92	| 0.45 | 42 | 71.5 | 0.0075 | smolvla-tau045-object-s42 |
93	
94	### smolvla / spatial
95	
96	| τ | seed | SR (%) | trigger_rate | source_exp_id |
97	|---|------|--------|-------------|---------------|
98	| 0.05 | 42 | 79.5 | 99.2 | eval-tau005-spatial-s42 |
99	| 0.075 | 42 | 78.0 | 0.92 | eval-k2-tau0075-spatial-s42 |
100	| 0.1 | 42 | 78.0 | 0.744 | eval-k2-tau010-spatial-s42-r3 |
101	| 0.15 | 42 | 80.0 | 0.412 | eval-k2-tau015-spatial-s42-r2 |
102	| 0.15 | 43 | 80.5 | 0.386 | smolvla-tau015-spatial-s43 |
103	| 0.2 | 42 | 81.0 | 0.267 | eval-k2-tau020-spatial-s42 |
104	| 0.25 | 42 | 79.5 | — | eval-k2-tau025-spatial-s42-v2 |
105	| 0.25 | 43 | 79.5 | 0.193 | smolvla-tau025-spatial-s43 |
106	| 0.25 | 46 | 78.0 | — | eval-spatial-adapt-tau025-s46-paired |
107	| 0.25 | 48 | 81.0 | — | eval-spatial-adapt-tau025-s48-paired |
108	| 0.3 | 42 | 79.5 | 0.168 | eval-k2-tau030-spatial-s42 |
109	| 0.35 | 42 | 80.5 | 12.1 | tau-sweep-spatial-tau035-s42 |
110	| 0.35 | 43 | 79.5 | 0.127 | smolvla-tau035-spatial-s43 |
111	| 0.4 | 42 | 80 | 9.6 | eval-tau040-spatial-s42 |
112	| 0.45 | 42 | 80.0 | 0.073 | smolvla-tau045-spatial-s42 |
113	
114	## B. Supplementary Seeds (SmolVLA, τ=0.25)
115	
116	**Total data points: 103** (with valid SR, deduplicated)
117	
118	### Summary (Mean ± Std)
119	
120	| benchmark | method | n_seeds | seeds | SR (mean ± std) |
121	|-----------|--------|---------|-------|----------------|
122	| goal | adaptive_conformal_crm | 6 | 42,43,44,45,46,47 | 83.6 ± 1.9 |
123	| goal | crm_obs_only | 7 | 42,43,44,45,46,47,48 | 82.3 ± 1.8 |
124	| goal | reconvla | 5 | 43,44,45,46,47 | 81.9 ± 2.6 |
125	| goal | vla_only | 8 | 42,43,44,45,46,47,48,49 | 83.6 ± 1.4 |
126	| long | adaptive_conformal_crm | 4 | 44,45,46,47 | 57.4 ± 2.3 |
127	| long | crm_obs_only | 6 | 42,43,44,45,46,47 | 56.4 ± 2.3 |
128	| long | reconvla | 6 | 42,43,44,45,46,47 | 57.1 ± 1.6 |
129	| long | vla_only | 6 | 42,43,44,45,46,47 | 58.0 ± 2.2 |
130	| object | adaptive_conformal_crm | 6 | 42,43,44,45,46,47 | 77.7 ± 1.9 |
131	| object | crm_obs_only | 6 | 42,43,44,45,46,47 | 78.0 ± 2.9 |
132	| object | reconvla | 6 | 42,43,44,45,46,47 | 77.8 ± 1.5 |
133	| object | vla_only | 9 | 42,43,44,45,46,47,48,49,50 | 77.2 ± 2.0 |
134	| spatial | adaptive_conformal_crm | 6 | 42,43,44,45,46,47 | 80.7 ± 0.9 |
135	| spatial | crm_obs_only | 8 | 42,43,44,45,46,47,48,49 | 79.6 ± 1.2 |
136	| spatial | reconvla | 6 | 42,43,44,45,46,47 | 80.2 ± 0.8 |
137	| spatial | vla_only | 8 | 42,43,44,45,46,47,48,49 | 80.2 ± 1.2 |
138	
139	### Detailed per-seed results
140	
141	| benchmark | method | seed | SR (%) | source_exp_id |
142	|-----------|--------|------|--------|---------------|
143	| goal | adaptive_conformal_crm | 42 | 84 | eval-supp-goal-adapt-tau025-s42 |
144	| goal | adaptive_conformal_crm | 43 | 84.5 | eval-supp-adapt-tau025-goal-s43 |
145	| goal | adaptive_conformal_crm | 44 | 86.5 | eval-supp-adapt-tau025-goal-s44 |
146	| goal | adaptive_conformal_crm | 45 | 81.0 | eval-supp-goal-adapt-tau025-s45 |
147	| goal | adaptive_conformal_crm | 46 | 83.5 | eval-supp-goal-adapt-tau025-s46 |
148	| goal | adaptive_conformal_crm | 47 | 82 | eval-supp-goal-adapt-tau025-s47 |
149	| goal | crm_obs_only | 42 | 85.5 | eval-supp-goal-crm005-s42 |
150	| goal | crm_obs_only | 43 | 82.0 | eval-supp-crm-norm005-goal-s43 |
151	| goal | crm_obs_only | 44 | 83.5 | eval-supp-crm-norm005-goal-s44 |
152	| goal | crm_obs_only | 45 | 81 | eval-supp-goal-crm-norm005-s45 |
153	| goal | crm_obs_only | 46 | 82.0 | eval-supp-goal-crm-norm005-s46 |
154	| goal | crm_obs_only | 47 | 82 | eval-supp-goal-crm-norm005-s47 |
155	| goal | crm_obs_only | 48 | 80.0 | eval-supp-crm-norm005-goal-s48 |
156	| goal | reconvla | 43 | 81.0 | eval-supp-goal-reconvla-s43 |
157	| goal | reconvla | 44 | 80.5 | eval-supp-goal-reconvla-s44 |
158	| goal | reconvla | 45 | 85.5 | eval-supp-goal-reconvla-s45 |
159	| goal | reconvla | 46 | 79.0 | eval-supp-goal-reconvla-s46 |
160	| goal | reconvla | 47 | 83.5 | eval-supp-goal-reconvla-s47 |
161	| goal | vla_only | 42 | 85.5 | eval-supp-k2mean-goal-s42-r2 |
162	| goal | vla_only | 43 | 82.5 | eval-supp-goal-vla-only-wrapper-s43 |
163	| goal | vla_only | 44 | 85.0 | eval-supp-goal-vla-only-wrapper-s44-r2 |
164	| goal | vla_only | 45 | 83.5 | eval-supp-goal-vla-only-s45 |
165	| goal | vla_only | 46 | 83.0 | eval-supp-goal-vla-only-s46 |
166	| goal | vla_only | 47 | 82.5 | eval-supp-goal-vla-only-s47-r3 |
167	| goal | vla_only | 48 | 85.0 | eval-supp-vla-only-goal-s48 |
168	| goal | vla_only | 49 | 82.0 | eval-supp-vla-only-goal-s49 |
169	| long | adaptive_conformal_crm | 44 | 56.0 | eval-supp-long-adapt-tau025-s44 |
170	| long | adaptive_conformal_crm | 45 | 60.0 | eval-supp-long-adapt-tau025-s45 |
171	| long | adaptive_conformal_crm | 46 | 58.5 | eval-supp-long-adapt-tau025-s46 |
172	| long | adaptive_conformal_crm | 47 | 55.0 | eval-supp-long-adapt-tau025-s47-r2 |
173	| long | crm_obs_only | 42 | 56.5 | eval-supp-long-crm-norm005-s42 |
174	| long | crm_obs_only | 43 | 54.5 | eval-supp-long-crm-norm005-s43 |
175	| long | crm_obs_only | 44 | 56.5 | eval-supp-long-crm-norm005-s44 |
176	| long | crm_obs_only | 45 | 60.5 | eval-supp-long-crm-norm005-s45 |
177	| long | crm_obs_only | 46 | 54.0 | eval-supp-long-crm-norm005-s46 |
178	| long | crm_obs_only | 47 | 56.5 | eval-supp-long-crm-norm005-s47 |
179	| long | reconvla | 42 | 56.5 | eval-supp-long-reconvla-s42 |
180	| long | reconvla | 43 | 59.0 | eval-supp-long-reconvla-s43 |
181	| long | reconvla | 44 | 57.0 | eval-supp-long-reconvla-s44 |
182	| long | reconvla | 45 | 59 | eval-supp-long-reconvla-s45 |
183	| long | reconvla | 46 | 56.0 | eval-supp-long-reconvla-s46 |
184	| long | reconvla | 47 | 55.0 | eval-supp-long-reconvla-s47 |
185	| long | vla_only | 42 | 59.5 | eval-supp-long-vla-only-s42 |
186	| long | vla_only | 43 | 56.0 | eval-supp-long-k2mean-s43 |
187	| long | vla_only | 44 | 60.5 | eval-supp-long-vla-only-s44 |
188	| long | vla_only | 45 | 57.5 | eval-supp-long-vla-only-s45 |
189	| long | vla_only | 46 | 55.0 | eval-supp-long-k2mean-s46 |
190	| long | vla_only | 47 | 59.5 | eval-supp-long-vla-only-s47-r4 |
191	| object | adaptive_conformal_crm | 42 | 81.0 | eval-supp-obj-adapt-tau025-s42 |
192	| object | adaptive_conformal_crm | 43 | 77.5 | eval-supp-adapt-tau025-obj-s43 |
193	| object | adaptive_conformal_crm | 44 | 75.0 | eval-supp-adapt-tau025-obj-s44 |
194	| object | adaptive_conformal_crm | 45 | 78.0 | eval-supp-adapt-tau025-obj-s45 |
195	| object | adaptive_conformal_crm | 46 | 77.5 | eval-supp-adapt-tau025-obj-s46 |
196	| object | adaptive_conformal_crm | 47 | 77.0 | eval-supp-obj-adapt-tau025-s47-r2 |
197	| object | crm_obs_only | 42 | 77.0 | eval-supp-obj-crm005-s42-r2 |
198	| object | crm_obs_only | 43 | 78.5 | eval-supp-crm-norm005-obj-s43 |
199	| object | crm_obs_only | 44 | 74.0 | eval-supp-crm-norm005-obj-s44 |
200	| object | crm_obs_only | 45 | 76.5 | eval-supp-obj-crm-norm005-s45 |
201	| object | crm_obs_only | 46 | 79.5 | eval-supp-crm-obj-s46 |
202	| object | crm_obs_only | 47 | 82.5 | eval-supp-obj-crm-norm005-s47-r2 |
203	| object | reconvla | 42 | 79 | eval-supp-obj-reconvla-s42 |
204	| object | reconvla | 43 | 77.0 | eval-supp-obj-reconvla-s43 |
205	| object | reconvla | 44 | 76.0 | eval-supp-obj-reconvla-s44 |
206	| object | reconvla | 45 | 78 | eval-supp-reconvla-obj-s45 |
207	| object | reconvla | 46 | 80.0 | eval-supp-reconvla-obj-s46 |
208	| object | reconvla | 47 | 76.5 | eval-supp-obj-reconvla-s47 |
209	| object | vla_only | 42 | 79.5 | eval-supp-k2mean-object-s42 |
210	| object | vla_only | 43 | 78.0 | eval-supp-k2mean-object-s43 |
211	| object | vla_only | 44 | 75.0 | eval-supp-k2mean-object-s44 |
212	| object | vla_only | 45 | 77.5 | eval-supp-k2mean-obj-s45 |
213	| object | vla_only | 46 | 79.0 | eval-supp-obj-vla-only-s46 |
214	| object | vla_only | 47 | 77.5 | eval-supp-obj-k2mean-s47 |
215	| object | vla_only | 48 | 79.0 | eval-supp-vla-only-obj-s48 |
216	| object | vla_only | 49 | 75.5 | eval-supp-vla-only-obj-s49 |
217	| object | vla_only | 50 | 74.0 | eval-supp-obj-vla-only-s50 |
218	| spatial | adaptive_conformal_crm | 42 | 82 | eval-supp-adapt-tau025-spatial-s42-r2 |
219	| spatial | adaptive_conformal_crm | 43 | 80 | eval-supp-adapt-tau025-spatial-s43 |
220	| spatial | adaptive_conformal_crm | 44 | 80.5 | eval-supp-adapt-tau025-spatial-s44 |
221	| spatial | adaptive_conformal_crm | 45 | 80 | eval-supp-spatial-adapt-tau025-s45-r3 |
222	| spatial | adaptive_conformal_crm | 46 | 80 | eval-supp-spatial-adapt-tau025-s46 |
223	| spatial | adaptive_conformal_crm | 47 | 81.5 | eval-supp-adapt-tau025-spatial-s47 |
224	| spatial | crm_obs_only | 42 | 79 | eval-supp-crm-norm02-spatial-s42-r2 |
225	| spatial | crm_obs_only | 43 | 81 | eval-supp-crm-norm005-spatial-s43 |
226	| spatial | crm_obs_only | 44 | 78.5 | eval-supp-crm-norm005-spatial-s44 |
227	| spatial | crm_obs_only | 45 | 80.5 | eval-supp-crm-norm005-spatial-s45 |
228	| spatial | crm_obs_only | 46 | 81 | eval-supp-spatial-crm-norm005-s46 |
229	| spatial | crm_obs_only | 47 | 80.5 | eval-supp-spatial-crm-norm005-s47 |
230	| spatial | crm_obs_only | 48 | 78.0 | eval-supp-crm-norm005-spatial-s48 |
231	| spatial | crm_obs_only | 49 | 78.5 | eval-supp-crm-norm005-spatial-s49 |
232	| spatial | reconvla | 42 | 80 | eval-supp-reconvla-k2-spatial-s42 |
233	| spatial | reconvla | 43 | 81.5 | eval-supp-reconvla-spatial-s43 |
234	| spatial | reconvla | 44 | 79.5 | eval-supp-reconvla-spatial-s44 |
235	| spatial | reconvla | 45 | 79.5 | eval-supp-spatial-reconvla-s45 |
236	| spatial | reconvla | 46 | 80 | eval-supp-spatial-reconvla-s46 |
237	| spatial | reconvla | 47 | 81.0 | eval-supp-reconvla-spatial-s47 |
238	| spatial | vla_only | 42 | 81.5 | eval-supp-k2mean-spatial-s42 |
239	| spatial | vla_only | 43 | 79.0 | eval-supp-spatial-vla-only-s43 |
240	| spatial | vla_only | 44 | 81.0 | eval-supp-k2mean-spatial-s44 |
241	| spatial | vla_only | 45 | 80.0 | eval-supp-vla-only-spatial-s45 |
242	| spatial | vla_only | 46 | 80.5 | eval-supp-vla-only-spatial-s46 |
243	| spatial | vla_only | 47 | 82 | eval-supp-spatial-k2mean-s47 |
244	| spatial | vla_only | 48 | 79.5 | eval-supp-vla-only-spatial-s48 |
245	| spatial | vla_only | 49 | 78.5 | eval-supp-vla-only-spatial-s49 |
246	
247	## C. Pi05 Cross-VLA Generalization
248	
249	**Total data points: 37** (deduplicated, SR>0%)
250	
251	### Summary (Mean ± Std)
252	
253	| benchmark | method | n | seeds | SR (mean ± std) |
254	|-----------|--------|---|-------|----------------|
255	| goal | adaptive_conformal_crm | 3 | 42,43,44 | 88.8 ± 1.2 |
256	| goal | crm_obs_only | 3 | 42,43,44 | 84.5 ± 1.3 |
257	| goal | vla_only | 3 | 42,43,44 | 98.3 ± 1.0 |
258	| long | adaptive_conformal_crm | 3 | 42,43,44 | 81.3 ± 1.4 |
259	| long | crm_obs_only | 3 | 42,43,44 | 79.3 ± 3.1 |
260	| long | vla_only | 3 | 42,43,44 | 96.5 ± 1.3 |
261	| object | adaptive_conformal_crm | 3 | 42,43,44 | 86.8 ± 1.3 |
262	| object | crm_obs_only | 3 | 42,43,44 | 88.0 ± 1.0 |
263	| object | vla_only | 3 | 42,43,44 | 99.8 ± 0.3 |
264	| spatial | adaptive_conformal_crm | 3 | 42,43,44 | 97.2 ± 0.8 |
265	| spatial | crm_obs_only | 3 | 42,43,44 | 96.8 ± 0.3 |
266	| spatial | vla_only | 4 | 42,43,44,45 | 94.9 ± 6.6 |
267	
268	### Per-seed detail
269	
270	| benchmark | method | seed | SR (%) | source_exp_id |
271	|-----------|--------|------|--------|---------------|
272	| goal | adaptive_conformal_crm | 42 | 89.5 | pi05-adaptive-goal-s42-cqa1 |
273	| goal | adaptive_conformal_crm | 43 | 89.5 | pi05-adaptive-goal-s43-bjb1-18228 |
274	| goal | adaptive_conformal_crm | 44 | 87.5 | westd-pi05-adaptive-goal-s44 |
275	| goal | crm_obs_only | 42 | 85.5 | westd-pi05-crm-k2-goal-s42 |
276	| goal | crm_obs_only | 43 | 83 | pi05-crm-k2-goal-s43-bjb1-r2 |
277	| goal | crm_obs_only | 44 | 85 | pi05-crm-k2-goal-s44-bjb1-r2 |
278	| goal | vla_only | 42 | 99.5 | westd-pi05-k2mean-goal-s42 |
279	| goal | vla_only | 43 | 98.0 | eval-pi05-vla-only-goal-seed43-r4 |
280	| goal | vla_only | 44 | 97.5 | pi05-vla-only-goal-s44-4090 |
281	| long | adaptive_conformal_crm | 42 | 80.5 | pi05-adaptive-long-s42-r2 |
282	| long | adaptive_conformal_crm | 43 | 80.5 | pi05-adaptive-long-s43-cqa1-r3 |
283	| long | adaptive_conformal_crm | 44 | 83.0 | pi05-adaptive-long-s44-cqa1-r3 |
284	| long | crm_obs_only | 42 | 82.0 | pi05-crm-k2-long-s42-r2 |
285	| long | crm_obs_only | 43 | 76.0 | pi05-crm-k2-long-s43-r2 |
286	| long | crm_obs_only | 44 | 80.0 | pi05-crm-k2-long-s44 |
287	| long | vla_only | 42 | 98.0 | westd-pi05-vla-only-long-s42-paired |
288	| long | vla_only | 43 | 95.5 | pi05-vla-only-long-s43-4090 |
289	| long | vla_only | 44 | 96.0 | westd-pi05-vla-only-long-s44-paired |
290	| object | adaptive_conformal_crm | 42 | 85.5 | pi05-object-adaptive-s42-cqa1 |
291	| object | adaptive_conformal_crm | 43 | 87.0 | westd-pi05-adaptive-object-s43-paired |
292	| object | adaptive_conformal_crm | 44 | 88.0 | pi05-object-adaptive-s44-cqa1 |
293	| object | crm_obs_only | 42 | 89 | pi05-crm-k2-object-s42-bjb1-r2 |
294	| object | crm_obs_only | 43 | 87.0 | westd-pi05-crm-k2-object-s43 |
295	| object | crm_obs_only | 44 | 88.0 | westd-pi05-crm-k2-object-s44 |
296	| object | vla_only | 42 | 100 | pi05-k2mean-object-s42-r3 |
297	| object | vla_only | 43 | 100 | westd-pi05-vla-only-object-s43-paired |
298	| object | vla_only | 44 | 99.5 | westd-pi05-vla-only-object-s44-paired |
299	| spatial | adaptive_conformal_crm | 42 | 96.5 | pi05-adaptive-spatial-s42-bjb2-r2 |
300	| spatial | adaptive_conformal_crm | 43 | 98 | pi05-adaptive-spatial-s43-bjb2-r2 |
301	| spatial | adaptive_conformal_crm | 44 | 97 | pi05-adaptive-spatial-s44-bjb2-r2 |
302	| spatial | crm_obs_only | 42 | 96.5 | pi05-crm-k2-spatial-s42-bjb2-r2 |
303	| spatial | crm_obs_only | 43 | 97 | pi05-crm-k2-spatial-s43-bjb2-r2 |
304	| spatial | crm_obs_only | 44 | 97 | pi05-crm-k2-spatial-s44-bjb2-r2 |
305	| spatial | vla_only | 42 | 98.0 | eval-pi05-vla-only-spatial-s42-v2 |
306	| spatial | vla_only | 43 | 97.5 | westd-pi05-vla-only-spatial-s43-paired |
307	| spatial | vla_only | 44 | 99.0 | eval-pi05-vla-only-spatial-s44-d149 |
308	| spatial | vla_only | 45 | 85.0 | eval-pi05-vla-only-spatial-s45 |
309	
310	## D. K-sweep Results
311	
312	**Total data points: 89** (with valid SR)
313	
314	### SmolVLA K-sweep (object, crm_obs_only, with VLA)
315	
316	| K | n_seeds | SR (mean ± std) | per-seed |
317	|---|---------|----------------|----------|
318	| 5 | 2 | 73.2 ± 0.4 | s42=73.5; s43=73 |
319	| 10 | 1 | 78.0 | s44=78.0 |
320	| 20 | 3 | 73.3 ± 2.3 | s42=75.5; s43=73.5; s44=71 |
321	
322	### All K-sweep data points
323	
324	| model | benchmark | method | seed | K | SR (%) | source_exp_id |
325	|-------|-----------|--------|------|---|--------|---------------|
326	| obs_only | object | crm_obs_only | 42 | 20 | 20.0 | eval-k20-obs-only-object-seed42 |
327	| obs_only | object | crm_obs_only | 43 | 20 | 18.0 | eval-k20-obs-only-object-seed43 |
328	| obs_only | object | crm_obs_only | 44 | 20 | 18.0 | eval-k20-obs-only-object-seed44 |
329	| obs_only | object | crm_obs_only | 45 | 20 | 19.0 | eval-k20-obs-only-object-seed45 |
330	| obs_only | object | crm_obs_only | 42 | 5 | 14.0 | eval-obs-only-object-norm02-k5-seed42 |
331	| obs_only | object | crm_obs_only | 43 | 5 | 19.0 | eval-obs-only-object-norm02-k5-seed43 |
332	| obs_only | object | crm_obs_only | 44 | 5 | 17.0 | eval-obs-only-object-norm02-k5-seed44 |
333	| obs_only | object | crm_obs_only | 45 | 5 | 15.0 | eval-obs-only-object-norm02-k5-seed45 |
334	| obs_only | object | crm_obs_only | 46 | 5 | 16.0 | eval-obs-only-object-norm02-k5-seed46 |
335	| obs_only | object | crm_obs_only | 47 | 5 | 13.0 | eval-obs-only-object-norm02-k5-seed47 |
336	| obs_only | object | crm_obs_only | 48 | 5 | 18.0 | eval-obs-only-object-norm02-k5-seed48 |
337	| obs_only | object | crm_obs_only | 42 | None | 20.0 | eval-obs-only-object-norm02-seed42 |
338	| obs_only | object | crm_obs_only | 43 | None | 16.0 | eval-obs-only-object-norm02-seed43-r3 |
339	| obs_only | object | crm_obs_only | 44 | None | 18.0 | eval-obs-only-object-norm03-seed44 |
340	| obs_only | object | crm_obs_only | 45 | None | 18.0 | eval-obs-only-object-default-seed45-r2 |
341	| obs_only | object | crm_obs_only | 46 | None | 18.0 | eval-obs-only-object-norm01-seed46-r3 |
342	| obs_only | object | crm_obs_only | 47 | None | 20.0 | eval-obs-only-object-norm02-seed47 |
343	| obs_only | object | crm_obs_only | 48 | None | 18.0 | eval-obs-only-object-norm02-seed48-r2 |
344	| obs_only | object | crm_obs_only | 49 | None | 16.0 | eval-obs-only-object-norm01-seed49 |
345	| obs_only | object | crm_obs_only | 50 | None | 18.0 | eval-obs-only-object-norm02-seed50 |
346	| obs_only | object | crm_obs_only | 51 | None | 17.0 | eval-obs-only-object-norm02-seed51 |
347	| obs_only | object | crm_obs_only | 52 | None | 15.0 | eval-obs-only-object-norm02-seed52 |
348	| obs_only | object | crm_obs_only | 53 | None | 19.0 | eval-obs-only-object-norm01-seed53 |
349	| obs_only | object | crm_obs_only | 54 | None | 15.0 | eval-obs-only-object-norm01-seed54 |
350	| obs_only | object | crm_obs_only | 55 | None | 15.0 | eval-obs-only-object-norm005-seed55 |
351	| obs_only | object | crm_obs_only | 56 | None | 15.0 | eval-obs-only-object-norm003-seed56 |
352	| obs_only | object | crm_obs_only | 57 | None | 19.0 | eval-obs-only-object-norm01-seed57 |
353	| obs_only | object | crm_obs_only | 58 | None | 16.0 | eval-obs-only-object-norm005-seed58 |
354	| obs_only | object | crm_obs_only | 59 | None | 13.0 | eval-obs-only-object-norm003-seed59 |
355	| obs_only | object | crm_obs_only | 60 | None | 15.0 | eval-obs-only-object-norm01-seed60 |
356	| obs_only | object | crm_obs_only | 61 | None | 15.0 | eval-obs-only-object-norm005-seed61 |
357	| obs_only | object | crm_obs_only | 64 | None | 17.0 | eval-obs-only-object-norm003-seed64 |
358	| obs_only | object | crm_obs_only | 65 | None | 17.0 | eval-obs-only-object-norm003-seed65 |
359	| obs_only | object | crm_obs_only | 66 | None | 13.5 | eval-obs-only-object-norm01-seed66 |
360	| obs_only | object | crm_obs_only | 67 | None | 14.0 | eval-obs-only-object-norm003-seed67 |
361	| obs_only | object | crm_obs_only | 71 | None | 16.0 | eval-obs-only-object-norm01-seed71 |
362	| obs_only | object | crm_obs_only | 72 | None | 11.0 | eval-obs-only-object-norm005-seed72 |
363	| obs_only | object | crm_obs_only | 73 | None | 16.0 | eval-obs-only-object-norm003-seed73 |
364	| obs_only | object | crm_obs_only | 74 | None | 13.0 | eval-obs-only-object-norm01-seed74 |
365	| obs_only | object | crm_obs_only | 75 | None | 15.0 | eval-obs-only-object-norm005-seed75 |
366	| obs_only | spatial | crm_obs_only | 42 | 20 | 35.0 | eval-k20-obs-only-spatial-seed42 |
367	| obs_only | spatial | crm_obs_only | 43 | 20 | 34.0 | eval-k20-obs-only-spatial-seed43 |
368	| obs_only | spatial | crm_obs_only | 44 | 20 | 34.0 | eval-k20-obs-only-spatial-seed44 |
369	| obs_only | spatial | crm_obs_only | 42 | 5 | 35.0 | eval-obs-only-spatial-norm02-k5-seed42 |
370	| obs_only | spatial | crm_obs_only | 43 | 5 | 32.0 | eval-obs-only-spatial-norm02-k5-seed43 |
371	| obs_only | spatial | crm_obs_only | 44 | 5 | 37.0 | eval-obs-only-spatial-norm02-k5-seed44-r2 |
372	| obs_only | spatial | crm_obs_only | 45 | 5 | 34.0 | eval-obs-only-spatial-norm02-k5-seed45-r2 |
373	| obs_only | spatial | crm_obs_only | None | None | 0 | eval-obs-only-spatial-v2 |
374	| obs_only | spatial | crm_obs_only | 42 | None | 33 | eval-obs-only-spatial-norm02-seed42-r2 |
375	| obs_only | spatial | crm_obs_only | 43 | None | 34.0 | eval-obs-only-spatial-norm02-seed43-r2 |
376	| obs_only | spatial | crm_obs_only | 44 | None | 36.0 | eval-obs-only-spatial-norm02-seed44 |
377	| obs_only | spatial | crm_obs_only | 45 | None | 34.0 | eval-obs-only-spatial-norm02-seed45 |
378	| obs_only | spatial | crm_obs_only | 46 | None | 33.0 | eval-obs-only-spatial-norm02-seed46-r2 |
379	| obs_only | spatial | crm_obs_only | 47 | None | 32.0 | eval-obs-only-spatial-norm02-seed47 |
380	| obs_only | spatial | crm_obs_only | 48 | None | 35.0 | eval-obs-only-spatial-seed48 |
381	| obs_only | spatial | crm_obs_only | 49 | None | 32.0 | eval-obs-only-spatial-norm02-seed49 |
382	| obs_only | spatial | crm_obs_only | 50 | None | 35.0 | eval-obs-only-spatial-norm02-seed50 |
383	| obs_only | spatial | crm_obs_only | 52 | None | 33.0 | eval-obs-only-spatial-norm02-seed52 |
384	| smolvla | None | None | 43 | 20 | 77 | eval-ksweep-k20-obs-obj-s43 |
385	| smolvla | object | None | 42 | 20 | 75.5 | eval-ksweep-k20-obs-object-s42 |
386	| smolvla | object | None | 43 | 20 | 73.5 | eval-ksweep-k20-obs-object-s43 |
387	| smolvla | object | None | 44 | 20 | 71 | eval-ksweep-k20-obs-object-s44 |
388	| smolvla | object | None | 42 | 5 | 73.5 | eval-ksweep-k5-obs-object-s42 |
389	| smolvla | object | None | 43 | 5 | 73 | eval-ksweep-k5-obs-object-s43 |
390	| smolvla | object | argmin | 42 | 5 | 15.0 | eval-argmin-object-k5-seed42 |
391	| smolvla | object | argmin | 43 | 5 | 13.0 | eval-argmin-object-k5-seed43 |
392	| smolvla | object | argmin | 44 | 5 | 11.0 | eval-argmin-object-k5-seed44-r2 |
393	| smolvla | object | argmin | 45 | 5 | 13.0 | eval-argmin-object-k5-seed45 |
394	| smolvla | object | crm_obs_only | 44 | 10 | 78.0 | smolvla-crm-norm005-k10-object-s44-cqa1 |
395	| smolvla | object | crm_obs_only | 42 | 20 | 20.0 | eval-crm-object-k20-seed42 |
396	| smolvla | object | crm_obs_only | 43 | 20 | 18.0 | eval-crm-object-k20-seed43 |
397	| smolvla | object | crm_obs_only | 44 | 20 | 18.0 | eval-crm-object-k20-seed44 |
398	| smolvla | object | random_selection | 42 | 5 | 14.0 | eval-random-selection-object-k5-seed42-r2 |
399	| smolvla | object | random_selection | 43 | 5 | 11.0 | eval-random-selection-object-k5-seed43-r2 |
400	| smolvla | object | random_selection | 44 | 5 | 10.0 | eval-random-selection-object-k5-seed44-r2 |
401	| smolvla | object | random_selection | 45 | 5 | 7.0 | eval-random-selection-object-k5-seed45-r2 |
402	| smolvla | object | random_selection | 42 | None | 11.0 | eval-random-selection-object-seed42 |
403	| smolvla | object | random_selection | 43 | None | 77 | eval-random-selection-object-seed43-v2 |
404	| smolvla | object | random_selection | 44 | None | 11.0 | eval-random-selection-object-seed44 |
405	| smolvla | object | random_selection | 45 | None | 10.0 | eval-random-selection-object-seed45 |
406	| smolvla | object | random_selection | 46 | None | 10.0 | eval-random-selection-object-seed46-r3 |
407	| smolvla | object | random_selection | 47 | None | 7 | eval-random-selection-object-seed47 |
408	| smolvla | object | random_selection | 48 | None | 10.0 | eval-random-selection-object-seed48 |
409	| smolvla | object | random_selection | 49 | None | 12.0 | eval-random-selection-object-seed49 |
410	| smolvla | spatial | None | 42 | 5 | 79 | eval-k5-spatial-s42-sweep |
411	| smolvla | spatial | crm_obs_only | 51 | 10 | 36.0 | eval-crm-spatial-k10-seed51 |
412	| smolvla | spatial | random_selection | 42 | None | 34 | eval-random-selection-spatial-seed42 |
413	| smolvla | spatial | random_selection | 43 | None | 26 | eval-random-selection-spatial-seed43-r2 |
414	| smolvla | spatial | random_selection | 44 | None | 28.0 | eval-random-selection-spatial-seed44 |
415	
416	## E. CRM Always-On Ablation (τ=0.001)
417	
418	**Total data points: 28** (with valid SR)
419	
420	### Summary (Mean ± Std)
421	
422	| model | benchmark | n | seeds | SR (mean ± std) |
423	|-------|-----------|---|-------|----------------|
424	| pi05 | goal | 3 | 42,43,44 | 82.5 ± 1.0 |
425	| pi05 | long | 2 | 42,43 | 78.2 ± 1.8 |
426	| pi05 | object | 3 | 42,43,44 | 90.7 ± 1.3 |
427	| pi05 | spatial | 1 | 42 | 96.0 |
428	| smolvla | goal | 5 | 42,43,44,45,46 | 80.4 ± 1.0 |
429	| smolvla | long | 4 | 42,43,44,45 | 43.2 ± 1.8 |
430	| smolvla | object | 5 | 42,43,44,45,46 | 72.2 ± 3.0 |
431	| smolvla | spatial | 5 | 42,43,44,45,46 | 77.9 ± 1.3 |
432	
433	### Per-seed detail
434	
435	| model | benchmark | seed | SR (%) | trigger_rate (%) | source_exp_id |
436	|-------|-----------|------|--------|-----------------|---------------|
437	| pi05 | goal | 42 | 81.5 | 100 | pi05-crm-always-on-goal-s42 |
438	| pi05 | goal | 43 | 82.5 | 100 | pi05-crm-always-on-goal-s43 |
439	| pi05 | goal | 44 | 83.5 | 100 | pi05-crm-always-on-goal-s44 |
440	| pi05 | long | 42 | 77 | 100 | pi05-crm-always-on-long-s42 |
441	| pi05 | long | 43 | 79.5 | 100 | pi05-crm-always-on-long-s43 |
442	| pi05 | object | 42 | 90.5 | 100 | pi05-crm-always-on-object-s42 |
443	| pi05 | object | 43 | 92 | 100 | pi05-crm-always-on-object-s43 |
444	| pi05 | object | 44 | 89.5 | 100 | pi05-crm-always-on-object-s44 |
445	| pi05 | spatial | 42 | 96 | 100 | pi05-crm-always-on-spatial-s42 |
446	| smolvla | goal | 42 | 80 | 100 | crm-always-on-goal-s42 |
447	| smolvla | goal | 43 | 79.5 | 100 | crm-always-on-goal-s43 |
448	| smolvla | goal | 44 | 80.5 | 100 | crm-always-on-goal-s44 |
449	| smolvla | goal | 45 | 82 | 100 | crm-always-on-goal-s45 |
450	| smolvla | goal | 46 | 80 | 100 | crm-always-on-goal-s46 |
451	| smolvla | long | 42 | 41.0 | 100 | crm-always-on-long-s42 |
452	| smolvla | long | 43 | 45.5 | 100 | crm-always-on-long-s43 |
453	| smolvla | long | 44 | 43.0 | 100 | crm-always-on-long-s44 |
454	| smolvla | long | 45 | 43.5 | 100 | crm-always-on-long-s45 |
455	| smolvla | object | 42 | 71.0 | 100 | crm-always-on-object-s42 |
456	| smolvla | object | 43 | 73.5 | 100 | crm-always-on-object-s43 |
457	| smolvla | object | 44 | 74.5 | 100 | crm-always-on-object-s44 |
458	| smolvla | object | 45 | 74.5 | 100 | crm-always-on-object-s45 |
459	| smolvla | object | 46 | 67.5 | 100 | crm-always-on-object-s46 |
460	| smolvla | spatial | 42 | 79.0 | 100 | crm-always-on-spatial-s42 |
461	| smolvla | spatial | 43 | 76 | 100 | crm-always-on-spatial-s43 |
462	| smolvla | spatial | 44 | 79 | 100 | crm-always-on-spatial-s44 |
463	| smolvla | spatial | 45 | 77.0 | 100 | crm-always-on-spatial-s45 |
464	| smolvla | spatial | 46 | 78.5 | 100 | crm-always-on-spatial-s46 |
465	
466	## F. Data Gaps & Notes
467	
468	### Bonus seed coverage (target: 6 seeds per benchmark × method)
469	
470	- **goal / reconvla**: 5 seeds — needs 1 more
471	- **long / adaptive_conformal_crm**: 4 seeds — needs 2 more
472	
473	### Pi05 cross-VLA coverage (target: 3 seeds per benchmark × method)
474	
475	All benchmark × method combinations have ≥3 seeds.
476	
477	### CRM always-on coverage
478	
479	- **pi05 / long**: 2 seeds — needs 1 more
480	- **pi05 / spatial**: 1 seeds — needs 2 more
481	
482	### Deduplication notes
483	- Multiple runs for same conditions (different servers, -r2/-r3 reruns). This summary keeps the run with highest SR.
484	- Pi05 vla_only experiments with SR=0% excluded as known OOM artifacts.
485	- Trigger rates stored inconsistently: some as fractions (0.0–1.0), some as percentages (0–100).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "uuid": "294a0017-fe82-43f9-9b64-1abefe977ddd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/supplementary_summary_final.md",
      "content": "# Supplementary Experiment Results\n\nAll results from registry experiments with status=DONE, conclusion in (success, negative).\nSR values normalized to percentages. Deduplicated: for same conditions, latest/best run kept.\n\n## A. Threshold (τ) Sensitivity Analysis\n\n**Total data points: 69** (with valid SR)\n\n### pi05 / goal\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.15 | 42 | 92.0 | 0.174 | pi05-adaptive-goal-s42-tau015-bjb2 |\n| 0.15 | 43 | 88.0 | 0.195 | pi05-goal-tau015-s43 |\n| 0.25 | 43 | 89.0 | 0.093 | pi05-goal-tau025-s43 |\n| 0.35 | 42 | 87.5 | 0.057 | pi05-adaptive-goal-s42-tau035-bjb2 |\n| 0.35 | 43 | 90.0 | 0.044 | pi05-goal-tau035-s43 |\n| 0.5 | 42 | 87.0 | 0.0206 | pi05-tau-sweep-goal-tau050-s42-r3 |\n| 0.7 | 42 | 87 | 1.1 | pi05-tau-sweep-goal-tau070-s42-r2 |\n\n### pi05 / long\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.15 | 42 | 84.0 | 0.114 | pi05-adaptive-long-s42-tau015-bjb2 |\n| 0.15 | 43 | 82 | 11.4 | pi05-long-tau015-s43-r3 |\n\n### pi05 / spatial\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.15 | 42 | 97.0 | 0.112 | pi05-adaptive-spatial-s42-tau015-bjb2 |\n| 0.15 | 43 | 96.5 | 0.117 | pi05-spatial-tau015-s43 |\n| 0.25 | 43 | 98.5 | 0.028 | pi05-spatial-tau025-s43 |\n| 0.35 | 42 | 96.5 | 0.0255 | pi05-adaptive-spatial-s42-tau035-bjb2 |\n| 0.35 | 43 | 97.5 | 0.022 | pi05-spatial-tau035-s43 |\n\n### smolvla / goal\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.1 | 42 | 81.0 | 0.739 | eval-ablation-tau010-goal-s42 |\n| 0.15 | 42 | 85.5 | 0.333 | smolvla-tau015-goal-s42 |\n| 0.15 | 43 | 83.5 | 0.354 | smolvla-tau015-goal-s43 |\n| 0.25 | 42 | 84.0 | 0.083 | smolvla-tau025-goal-s42 |\n| 0.25 | 43 | 81.0 | 0.0925 | smolvla-tau025-goal-s43 |\n| 0.25 | 49 | 80.5 | — | eval-goal-adapt-tau025-s49-paired |\n| 0.35 | 42 | 86 | 2.1 | tau-sweep-goal-tau035-s42 |\n| 0.35 | 43 | 85.5 | 0.0211 | smolvla-tau035-goal-s43 |\n| 0.4 | 42 | 83.5 | — | tau_sweep_goal_tau040_s42 |\n| 0.45 | 42 | 83.5 | — | tau_sweep_goal_tau045_s42 |\n| 0.5 | 42 | 87.0 | 0.0206 | tau_sweep_goal_tau050_s42_cqa1 |\n| 0.7 | 42 | 87.0 | 0.0104 | tau_sweep_goal_tau070_s42_cqa1 |\n| 0.9 | 42 | 89.0 | 0.0035 | tau_sweep_goal_tau090_s42_cqa1 |\n\n### smolvla / long\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.05 | 42 | 44.0 | 0.9781 | smolvla-tau005-long-s42 |\n| 0.1 | 42 | 53.5 | 0.613 | smolvla-tau010-long-s42 |\n| 0.15 | 42 | 61.0 | 0.239 | smolvla-tau015-long-s42 |\n| 0.15 | 43 | 61.0 | 0.236 | smolvla-tau015-long-s43 |\n| 0.2 | 42 | 58.5 | 0.089 | smolvla-tau020-long-s42 |\n| 0.2 | 43 | 54.5 | 11.4 | smolvla-tau020-long-s43-r2 |\n| 0.25 | 42 | 56.0 | 0.042 | smolvla-tau025-long-s42 |\n| 0.25 | 43 | 53.0 | 0.046 | smolvla-tau025-long-s43 |\n| 0.3 | 42 | 54.5 | 1.6 | smolvla-tau030-long-s42-r2 |\n| 0.3 | 43 | 55.5 | 1.6 | smolvla-tau030-long-s43-r2 |\n| 0.35 | 42 | 57.5 | 0.013 | smolvla-tau035-long-s42 |\n| 0.35 | 43 | 60.0 | 0.01 | smolvla-tau035-long-s43 |\n| 0.4 | 42 | 60.0 | 0.004 | smolvla-tau040-long-s42 |\n| 0.45 | 42 | 59.5 | 0.003 | smolvla-tau045-long-s42 |\n\n### smolvla / object\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.05 | 42 | 75 | 94.2 | smolvla-tau005-object-s42 |\n| 0.1 | 42 | 78 | 44.4 | smolvla-tau010-object-s42 |\n| 0.15 | 42 | 79 | 0.171 | smolvla-adapt-tau015-object-s42-cqa1 |\n| 0.15 | 43 | 78 | 0.174 | smolvla-adapt-tau015-object-s43-cqa1 |\n| 0.15 | 44 | 73.5 | 0.168 | smolvla-adapt-tau015-object-s44-cqa1 |\n| 0.2 | 42 | 78.5 | 7.1 | smolvla-tau020-object-s42 |\n| 0.25 | 42 | 81 | 3.5 | smolvla-tau025-object-s42-r3 |\n| 0.25 | 43 | 77.5 | 0.037 | smolvla-tau025-object-s43-r3 |\n| 0.3 | 42 | 79.0 | 0.0231 | smolvla-tau030-object-s42 |\n| 0.35 | 42 | 75 | 1.6 | smolvla-tau035-object-s42-r3 |\n| 0.35 | 43 | 77.0 | 0.013 | smolvla-tau035-object-s43-r3 |\n| 0.4 | 42 | 73.5 | 0.0091 | smolvla-tau040-object-s42 |\n| 0.45 | 42 | 71.5 | 0.0075 | smolvla-tau045-object-s42 |\n\n### smolvla / spatial\n\n| τ | seed | SR (%) | trigger_rate | source_exp_id |\n|---|------|--------|-------------|---------------|\n| 0.05 | 42 | 79.5 | 99.2 | eval-tau005-spatial-s42 |\n| 0.075 | 42 | 78.0 | 0.92 | eval-k2-tau0075-spatial-s42 |\n| 0.1 | 42 | 78.0 | 0.744 | eval-k2-tau010-spatial-s42-r3 |\n| 0.15 | 42 | 80.0 | 0.412 | eval-k2-tau015-spatial-s42-r2 |\n| 0.15 | 43 | 80.5 | 0.386 | smolvla-tau015-spatial-s43 |\n| 0.2 | 42 | 81.0 | 0.267 | eval-k2-tau020-spatial-s42 |\n| 0.25 | 42 | 79.5 | — | eval-k2-tau025-spatial-s42-v2 |\n| 0.25 | 43 | 79.5 | 0.193 | smolvla-tau025-spatial-s43 |\n| 0.25 | 46 | 78.0 | — | eval-spatial-adapt-tau025-s46-paired |\n| 0.25 | 48 | 81.0 | — | eval-spatial-adapt-tau025-s48-paired |\n| 0.3 | 42 | 79.5 | 0.168 | eval-k2-tau030-spatial-s42 |\n| 0.35 | 42 | 80.5 | 12.1 | tau-sweep-spatial-tau035-s42 |\n| 0.35 | 43 | 79.5 | 0.127 | smolvla-tau035-spatial-s43 |\n| 0.4 | 42 | 80 | 9.6 | eval-tau040-spatial-s42 |\n| 0.45 | 42 | 80.0 | 0.073 | smolvla-tau045-spatial-s42 |\n\n## B. Supplementary Seeds (SmolVLA, τ=0.25)\n\n**Total data points: 103** (with valid SR, deduplicated)\n\n### Summary (Mean ± Std)\n\n| benchmark | method | n_seeds | seeds | SR (mean ± std) |\n|-----------|--------|---------|-------|----------------|\n| goal | adaptive_conformal_crm | 6 | 42,43,44,45,46,47 | 83.6 ± 1.9 |\n| goal | crm_obs_only | 7 | 42,43,44,45,46,47,48 | 82.3 ± 1.8 |\n| goal | reconvla | 5 | 43,44,45,46,47 | 81.9 ± 2.6 |\n| goal | vla_only | 8 | 42,43,44,45,46,47,48,49 | 83.6 ± 1.4 |\n| long | adaptive_conformal_crm | 4 | 44,45,46,47 | 57.4 ± 2.3 |\n| long | crm_obs_only | 6 | 42,43,44,45,46,47 | 56.4 ± 2.3 |\n| long | reconvla | 6 | 42,43,44,45,46,47 | 57.1 ± 1.6 |\n| long | vla_only | 6 | 42,43,44,45,46,47 | 58.0 ± 2.2 |\n| object | adaptive_conformal_crm | 6 | 42,43,44,45,46,47 | 77.7 ± 1.9 |\n| object | crm_obs_only | 6 | 42,43,44,45,46,47 | 78.0 ± 2.9 |\n| object | reconvla | 6 | 42,43,44,45,46,47 | 77.8 ± 1.5 |\n| object | vla_only | 9 | 42,43,44,45,46,47,48,49,50 | 77.2 ± 2.0 |\n| spatial | adaptive_conformal_crm | 6 | 42,43,44,45,46,47 | 80.7 ± 0.9 |\n| spatial | crm_obs_only | 8 | 42,43,44,45,46,47,48,49 | 79.6 ± 1.2 |\n| spatial | reconvla | 6 | 42,43,44,45,46,47 | 80.2 ± 0.8 |\n| spatial | vla_only | 8 | 42,43,44,45,46,47,48,49 | 80.2 ± 1.2 |\n\n### Detailed per-seed results\n\n| benchmark | method | seed | SR (%) | source_exp_id |\n|-----------|--------|------|--------|---------------|\n| goal | adaptive_conformal_crm | 42 | 84 | eval-supp-goal-adapt-tau025-s42 |\n| goal | adaptive_conformal_crm | 43 | 84.5 | eval-supp-adapt-tau025-goal-s43 |\n| goal | adaptive_conformal_crm | 44 | 86.5 | eval-supp-adapt-tau025-goal-s44 |\n| goal | adaptive_conformal_crm | 45 | 81.0 | eval-supp-goal-adapt-tau025-s45 |\n| goal | adaptive_conformal_crm | 46 | 83.5 | eval-supp-goal-adapt-tau025-s46 |\n| goal | adaptive_conformal_crm | 47 | 82 | eval-supp-goal-adapt-tau025-s47 |\n| goal | crm_obs_only | 42 | 85.5 | eval-supp-goal-crm005-s42 |\n| goal | crm_obs_only | 43 | 82.0 | eval-supp-crm-norm005-goal-s43 |\n| goal | crm_obs_only | 44 | 83.5 | eval-supp-crm-norm005-goal-s44 |\n| goal | crm_obs_only | 45 | 81 | eval-supp-goal-crm-norm005-s45 |\n| goal | crm_obs_only | 46 | 82.0 | eval-supp-goal-crm-norm005-s46 |\n| goal | crm_obs_only | 47 | 82 | eval-supp-goal-crm-norm005-s47 |\n| goal | crm_obs_only | 48 | 80.0 | eval-supp-crm-norm005-goal-s48 |\n| goal | reconvla | 43 | 81.0 | eval-supp-goal-reconvla-s43 |\n| goal | reconvla | 44 | 80.5 | eval-supp-goal-reconvla-s44 |\n| goal | reconvla | 45 | 85.5 | eval-supp-goal-reconvla-s45 |\n| goal | reconvla | 46 | 79.0 | eval-supp-goal-reconvla-s46 |\n| goal | reconvla | 47 | 83.5 | eval-supp-goal-reconvla-s47 |\n| goal | vla_only | 42 | 85.5 | eval-supp-k2mean-goal-s42-r2 |\n| goal | vla_only | 43 | 82.5 | eval-supp-goal-vla-only-wrapper-s43 |\n| goal | vla_only | 44 | 85.0 | eval-supp-goal-vla-only-wrapper-s44-r2 |\n| goal | vla_only | 45 | 83.5 | eval-supp-goal-vla-only-s45 |\n| goal | vla_only | 46 | 83.0 | eval-supp-goal-vla-only-s46 |\n| goal | vla_only | 47 | 82.5 | eval-supp-goal-vla-only-s47-r3 |\n| goal | vla_only | 48 | 85.0 | eval-supp-vla-only-goal-s48 |\n| goal | vla_only | 49 | 82.0 | eval-supp-vla-only-goal-s49 |\n| long | adaptive_conformal_crm | 44 | 56.0 | eval-supp-long-adapt-tau025-s44 |\n| long | adaptive_conformal_crm | 45 | 60.0 | eval-supp-long-adapt-tau025-s45 |\n| long | adaptive_conformal_crm | 46 | 58.5 | eval-supp-long-adapt-tau025-s46 |\n| long | adaptive_conformal_crm | 47 | 55.0 | eval-supp-long-adapt-tau025-s47-r2 |\n| long | crm_obs_only | 42 | 56.5 | eval-supp-long-crm-norm005-s42 |\n| long | crm_obs_only | 43 | 54.5 | eval-supp-long-crm-norm005-s43 |\n| long | crm_obs_only | 44 | 56.5 | eval-supp-long-crm-norm005-s44 |\n| long | crm_obs_only | 45 | 60.5 | eval-supp-long-crm-norm005-s45 |\n| long | crm_obs_only | 46 | 54.0 | eval-supp-long-crm-norm005-s46 |\n| long | crm_obs_only | 47 | 56.5 | eval-supp-long-crm-norm005-s47 |\n| long | reconvla | 42 | 56.5 | eval-supp-long-reconvla-s42 |\n| long | reconvla | 43 | 59.0 | eval-supp-long-reconvla-s43 |\n| long | reconvla | 44 | 57.0 | eval-supp-long-reconvla-s44 |\n| long | reconvla | 45 | 59 | eval-supp-long-reconvla-s45 |\n| long | reconvla | 46 | 56.0 | eval-supp-long-reconvla-s46 |\n| long | reconvla | 47 | 55.0 | eval-supp-long-reconvla-s47 |\n| long | vla_only | 42 | 59.5 | eval-supp-long-vla-only-s42 |\n| long | vla_only | 43 | 56.0 | eval-supp-long-k2mean-s43 |\n| long | vla_only | 44 | 60.5 | eval-supp-long-vla-only-s44 |\n| long | vla_only | 45 | 57.5 | eval-supp-long-vla-only-s45 |\n| long | vla_only | 46 | 55.0 | eval-supp-long-k2mean-s46 |\n| long | vla_only | 47 | 59.5 | eval-supp-long-vla-only-s47-r4 |\n| object | adaptive_conformal_crm | 42 | 81.0 | eval-supp-obj-adapt-tau025-s42 |\n| object | adaptive_conformal_crm | 43 | 77.5 | eval-supp-adapt-tau025-obj-s43 |\n| object | adaptive_conformal_crm | 44 | 75.0 | eval-supp-adapt-tau025-obj-s44 |\n| object | adaptive_conformal_crm | 45 | 78.0 | eval-supp-adapt-tau025-obj-s45 |\n| object | adaptive_conformal_crm | 46 | 77.5 | eval-supp-adapt-tau025-obj-s46 |\n| object | adaptive_conformal_crm | 47 | 77.0 | eval-supp-obj-adapt-tau025-s47-r2 |\n| object | crm_obs_only | 42 | 77.0 | eval-supp-obj-crm005-s42-r2 |\n| object | crm_obs_only | 43 | 78.5 | eval-supp-crm-norm005-obj-s43 |\n| object | crm_obs_only | 44 | 74.0 | eval-supp-crm-norm005-obj-s44 |\n| object | crm_obs_only | 45 | 76.5 | eval-supp-obj-crm-norm005-s45 |\n| object | crm_obs_only | 46 | 79.5 | eval-supp-crm-obj-s46 |\n| object | crm_obs_only | 47 | 82.5 | eval-supp-obj-crm-norm005-s47-r2 |\n| object | reconvla | 42 | 79 | eval-supp-obj-reconvla-s42 |\n| object | reconvla | 43 | 77.0 | eval-supp-obj-reconvla-s43 |\n| object | reconvla | 44 | 76.0 | eval-supp-obj-reconvla-s44 |\n| object | reconvla | 45 | 78 | eval-supp-reconvla-obj-s45 |\n| object | reconvla | 46 | 80.0 | eval-supp-reconvla-obj-s46 |\n| object | reconvla | 47 | 76.5 | eval-supp-obj-reconvla-s47 |\n| object | vla_only | 42 | 79.5 | eval-supp-k2mean-object-s42 |\n| object | vla_only | 43 | 78.0 | eval-supp-k2mean-object-s43 |\n| object | vla_only | 44 | 75.0 | eval-supp-k2mean-object-s44 |\n| object | vla_only | 45 | 77.5 | eval-supp-k2mean-obj-s45 |\n| object | vla_only | 46 | 79.0 | eval-supp-obj-vla-only-s46 |\n| object | vla_only | 47 | 77.5 | eval-supp-obj-k2mean-s47 |\n| object | vla_only | 48 | 79.0 | eval-supp-vla-only-obj-s48 |\n| object | vla_only | 49 | 75.5 | eval-supp-vla-only-obj-s49 |\n| object | vla_only | 50 | 74.0 | eval-supp-obj-vla-only-s50 |\n| spatial | adaptive_conformal_crm | 42 | 82 | eval-supp-adapt-tau025-spatial-s42-r2 |\n| spatial | adaptive_conformal_crm | 43 | 80 | eval-supp-adapt-tau025-spatial-s43 |\n| spatial | adaptive_conformal_crm | 44 | 80.5 | eval-supp-adapt-tau025-spatial-s44 |\n| spatial | adaptive_conformal_crm | 45 | 80 | eval-supp-spatial-adapt-tau025-s45-r3 |\n| spatial | adaptive_conformal_crm | 46 | 80 | eval-supp-spatial-adapt-tau025-s46 |\n| spatial | adaptive_conformal_crm | 47 | 81.5 | eval-supp-adapt-tau025-spatial-s47 |\n| spatial | crm_obs_only | 42 | 79 | eval-supp-crm-norm02-spatial-s42-r2 |\n| spatial | crm_obs_only | 43 | 81 | eval-supp-crm-norm005-spatial-s43 |\n| spatial | crm_obs_only | 44 | 78.5 | eval-supp-crm-norm005-spatial-s44 |\n| spatial | crm_obs_only | 45 | 80.5 | eval-supp-crm-norm005-spatial-s45 |\n| spatial | crm_obs_only | 46 | 81 | eval-supp-spatial-crm-norm005-s46 |\n| spatial | crm_obs_only | 47 | 80.5 | eval-supp-spatial-crm-norm005-s47 |\n| spatial | crm_obs_only | 48 | 78.0 | eval-supp-crm-norm005-spatial-s48 |\n| spatial | crm_obs_only | 49 | 78.5 | eval-supp-crm-norm005-spatial-s49 |\n| spatial | reconvla | 42 | 80 | eval-supp-reconvla-k2-spatial-s42 |\n| spatial | reconvla | 43 | 81.5 | eval-supp-reconvla-spatial-s43 |\n| spatial | reconvla | 44 | 79.5 | eval-supp-reconvla-spatial-s44 |\n| spatial | reconvla | 45 | 79.5 | eval-supp-spatial-reconvla-s45 |\n| spatial | reconvla | 46 | 80 | eval-supp-spatial-reconvla-s46 |\n| spatial | reconvla | 47 | 81.0 | eval-supp-reconvla-spatial-s47 |\n| spatial | vla_only | 42 | 81.5 | eval-supp-k2mean-spatial-s42 |\n| spatial | vla_only | 43 | 79.0 | eval-supp-spatial-vla-only-s43 |\n| spatial | vla_only | 44 | 81.0 | eval-supp-k2mean-spatial-s44 |\n| spatial | vla_only | 45 | 80.0 | eval-supp-vla-only-spatial-s45 |\n| spatial | vla_only | 46 | 80.5 | eval-supp-vla-only-spatial-s46 |\n| spatial | vla_only | 47 | 82 | eval-supp-spatial-k2mean-s47 |\n| spatial | vla_only | 48 | 79.5 | eval-supp-vla-only-spatial-s48 |\n| spatial | vla_only | 49 | 78.5 | eval-supp-vla-only-spatial-s49 |\n\n## C. Pi05 Cross-VLA Generalization\n\n**Total data points: 37** (deduplicated, SR>0%)\n\n### Summary (Mean ± Std)\n\n| benchmark | method | n | seeds | SR (mean ± std) |\n|-----------|--------|---|-------|----------------|\n| goal | adaptive_conformal_crm | 3 | 42,43,44 | 88.8 ± 1.2 |\n| goal | crm_obs_only | 3 | 42,43,44 | 84.5 ± 1.3 |\n| goal | vla_only | 3 | 42,43,44 | 98.3 ± 1.0 |\n| long | adaptive_conformal_crm | 3 | 42,43,44 | 81.3 ± 1.4 |\n| long | crm_obs_only | 3 | 42,43,44 | 79.3 ± 3.1 |\n| long | vla_only | 3 | 42,43,44 | 96.5 ± 1.3 |\n| object | adaptive_conformal_crm | 3 | 42,43,44 | 86.8 ± 1.3 |\n| object | crm_obs_only | 3 | 42,43,44 | 88.0 ± 1.0 |\n| object | vla_only | 3 | 42,43,44 | 99.8 ± 0.3 |\n| spatial | adaptive_conformal_crm | 3 | 42,43,44 | 97.2 ± 0.8 |\n| spatial | crm_obs_only | 3 | 42,43,44 | 96.8 ± 0.3 |\n| spatial | vla_only | 4 | 42,43,44,45 | 94.9 ± 6.6 |\n\n### Per-seed detail\n\n| benchmark | method | seed | SR (%) | source_exp_id |\n|-----------|--------|------|--------|---------------|\n| goal | adaptive_conformal_crm | 42 | 89.5 | pi05-adaptive-goal-s42-cqa1 |\n| goal | adaptive_conformal_crm | 43 | 89.5 | pi05-adaptive-goal-s43-bjb1-18228 |\n| goal | adaptive_conformal_crm | 44 | 87.5 | westd-pi05-adaptive-goal-s44 |\n| goal | crm_obs_only | 42 | 85.5 | westd-pi05-crm-k2-goal-s42 |\n| goal | crm_obs_only | 43 | 83 | pi05-crm-k2-goal-s43-bjb1-r2 |\n| goal | crm_obs_only | 44 | 85 | pi05-crm-k2-goal-s44-bjb1-r2 |\n| goal | vla_only | 42 | 99.5 | westd-pi05-k2mean-goal-s42 |\n| goal | vla_only | 43 | 98.0 | eval-pi05-vla-only-goal-seed43-r4 |\n| goal | vla_only | 44 | 97.5 | pi05-vla-only-goal-s44-4090 |\n| long | adaptive_conformal_crm | 42 | 80.5 | pi05-adaptive-long-s42-r2 |\n| long | adaptive_conformal_crm | 43 | 80.5 | pi05-adaptive-long-s43-cqa1-r3 |\n| long | adaptive_conformal_crm | 44 | 83.0 | pi05-adaptive-long-s44-cqa1-r3 |\n| long | crm_obs_only | 42 | 82.0 | pi05-crm-k2-long-s42-r2 |\n| long | crm_obs_only | 43 | 76.0 | pi05-crm-k2-long-s43-r2 |\n| long | crm_obs_only | 44 | 80.0 | pi05-crm-k2-long-s44 |\n| long | vla_only | 42 | 98.0 | westd-pi05-vla-only-long-s42-paired |\n| long | vla_only | 43 | 95.5 | pi05-vla-only-long-s43-4090 |\n| long | vla_only | 44 | 96.0 | westd-pi05-vla-only-long-s44-paired |\n| object | adaptive_conformal_crm | 42 | 85.5 | pi05-object-adaptive-s42-cqa1 |\n| object | adaptive_conformal_crm | 43 | 87.0 | westd-pi05-adaptive-object-s43-paired |\n| object | adaptive_conformal_crm | 44 | 88.0 | pi05-object-adaptive-s44-cqa1 |\n| object | crm_obs_only | 42 | 89 | pi05-crm-k2-object-s42-bjb1-r2 |\n| object | crm_obs_only | 43 | 87.0 | westd-pi05-crm-k2-object-s43 |\n| object | crm_obs_only | 44 | 88.0 | westd-pi05-crm-k2-object-s44 |\n| object | vla_only | 42 | 100 | pi05-k2mean-object-s42-r3 |\n| object | vla_only | 43 | 100 | westd-pi05-vla-only-object-s43-paired |\n| object | vla_only | 44 | 99.5 | westd-pi05-vla-only-object-s44-paired |\n| spatial | adaptive_conformal_crm | 42 | 96.5 | pi05-adaptive-spatial-s42-bjb2-r2 |\n| spatial | adaptive_conformal_crm | 43 | 98 | pi05-adaptive-spatial-s43-bjb2-r2 |\n| spatial | adaptive_conformal_crm | 44 | 97 | pi05-adaptive-spatial-s44-bjb2-r2 |\n| spatial | crm_obs_only | 42 | 96.5 | pi05-crm-k2-spatial-s42-bjb2-r2 |\n| spatial | crm_obs_only | 43 | 97 | pi05-crm-k2-spatial-s43-bjb2-r2 |\n| spatial | crm_obs_only | 44 | 97 | pi05-crm-k2-spatial-s44-bjb2-r2 |\n| spatial | vla_only | 42 | 98.0 | eval-pi05-vla-only-spatial-s42-v2 |\n| spatial | vla_only | 43 | 97.5 | westd-pi05-vla-only-spatial-s43-paired |\n| spatial | vla_only | 44 | 99.0 | eval-pi05-vla-only-spatial-s44-d149 |\n| spatial | vla_only | 45 | 85.0 | eval-pi05-vla-only-spatial-s45 |\n\n## D. K-sweep Results\n\n**Total data points: 89** (with valid SR)\n\n### SmolVLA K-sweep (object, crm_obs_only, with VLA)\n\n| K | n_seeds | SR (mean ± std) | per-seed |\n|---|---------|----------------|----------|\n| 5 | 2 | 73.2 ± 0.4 | s42=73.5; s43=73 |\n| 10 | 1 | 78.0 | s44=78.0 |\n| 20 | 3 | 73.3 ± 2.3 | s42=75.5; s43=73.5; s44=71 |\n\n### All K-sweep data points\n\n| model | benchmark | method | seed | K | SR (%) | source_exp_id |\n|-------|-----------|--------|------|---|--------|---------------|\n| obs_only | object | crm_obs_only | 42 | 20 | 20.0 | eval-k20-obs-only-object-seed42 |\n| obs_only | object | crm_obs_only | 43 | 20 | 18.0 | eval-k20-obs-only-object-seed43 |\n| obs_only | object | crm_obs_only | 44 | 20 | 18.0 | eval-k20-obs-only-object-seed44 |\n| obs_only | object | crm_obs_only | 45 | 20 | 19.0 | eval-k20-obs-only-object-seed45 |\n| obs_only | object | crm_obs_only | 42 | 5 | 14.0 | eval-obs-only-object-norm02-k5-seed42 |\n| obs_only | object | crm_obs_only | 43 | 5 | 19.0 | eval-obs-only-object-norm02-k5-seed43 |\n| obs_only | object | crm_obs_only | 44 | 5 | 17.0 | eval-obs-only-object-norm02-k5-seed44 |\n| obs_only | object | crm_obs_only | 45 | 5 | 15.0 | eval-obs-only-object-norm02-k5-seed45 |\n| obs_only | object | crm_obs_only | 46 | 5 | 16.0 | eval-obs-only-object-norm02-k5-seed46 |\n| obs_only | object | crm_obs_only | 47 | 5 | 13.0 | eval-obs-only-object-norm02-k5-seed47 |\n| obs_only | object | crm_obs_only | 48 | 5 | 18.0 | eval-obs-only-object-norm02-k5-seed48 |\n| obs_only | object | crm_obs_only | 42 | None | 20.0 | eval-obs-only-object-norm02-seed42 |\n| obs_only | object | crm_obs_only | 43 | None | 16.0 | eval-obs-only-object-norm02-seed43-r3 |\n| obs_only | object | crm_obs_only | 44 | None | 18.0 | eval-obs-only-object-norm03-seed44 |\n| obs_only | object | crm_obs_only | 45 | None | 18.0 | eval-obs-only-object-default-seed45-r2 |\n| obs_only | object | crm_obs_only | 46 | None | 18.0 | eval-obs-only-object-norm01-seed46-r3 |\n| obs_only | object | crm_obs_only | 47 | None | 20.0 | eval-obs-only-object-norm02-seed47 |\n| obs_only | object | crm_obs_only | 48 | None | 18.0 | eval-obs-only-object-norm02-seed48-r2 |\n| obs_only | object | crm_obs_only | 49 | None | 16.0 | eval-obs-only-object-norm01-seed49 |\n| obs_only | object | crm_obs_only | 50 | None | 18.0 | eval-obs-only-object-norm02-seed50 |\n| obs_only | object | crm_obs_only | 51 | None | 17.0 | eval-obs-only-object-norm02-seed51 |\n| obs_only | object | crm_obs_only | 52 | None | 15.0 | eval-obs-only-object-norm02-seed52 |\n| obs_only | object | crm_obs_only | 53 | None | 19.0 | eval-obs-only-object-norm01-seed53 |\n| obs_only | object | crm_obs_only | 54 | None | 15.0 | eval-obs-only-object-norm01-seed54 |\n| obs_only | object | crm_obs_only | 55 | None | 15.0 | eval-obs-only-object-norm005-seed55 |\n| obs_only | object | crm_obs_only | 56 | None | 15.0 | eval-obs-only-object-norm003-seed56 |\n| obs_only | object | crm_obs_only | 57 | None | 19.0 | eval-obs-only-object-norm01-seed57 |\n| obs_only | object | crm_obs_only | 58 | None | 16.0 | eval-obs-only-object-norm005-seed58 |\n| obs_only | object | crm_obs_only | 59 | None | 13.0 | eval-obs-only-object-norm003-seed59 |\n| obs_only | object | crm_obs_only | 60 | None | 15.0 | eval-obs-only-object-norm01-seed60 |\n| obs_only | object | crm_obs_only | 61 | None | 15.0 | eval-obs-only-object-norm005-seed61 |\n| obs_only | object | crm_obs_only | 64 | None | 17.0 | eval-obs-only-object-norm003-seed64 |\n| obs_only | object | crm_obs_only | 65 | None | 17.0 | eval-obs-only-object-norm003-seed65 |\n| obs_only | object | crm_obs_only | 66 | None | 13.5 | eval-obs-only-object-norm01-seed66 |\n| obs_only | object | crm_obs_only | 67 | None | 14.0 | eval-obs-only-object-norm003-seed67 |\n| obs_only | object | crm_obs_only | 71 | None | 16.0 | eval-obs-only-object-norm01-seed71 |\n| obs_only | object | crm_obs_only | 72 | None | 11.0 | eval-obs-only-object-norm005-seed72 |\n| obs_only | object | crm_obs_only | 73 | None | 16.0 | eval-obs-only-object-norm003-seed73 |\n| obs_only | object | crm_obs_only | 74 | None | 13.0 | eval-obs-only-object-norm01-seed74 |\n| obs_only | object | crm_obs_only | 75 | None | 15.0 | eval-obs-only-object-norm005-seed75 |\n| obs_only | spatial | crm_obs_only | 42 | 20 | 35.0 | eval-k20-obs-only-spatial-seed42 |\n| obs_only | spatial | crm_obs_only | 43 | 20 | 34.0 | eval-k20-obs-only-spatial-seed43 |\n| obs_only | spatial | crm_obs_only | 44 | 20 | 34.0 | eval-k20-obs-only-spatial-seed44 |\n| obs_only | spatial | crm_obs_only | 42 | 5 | 35.0 | eval-obs-only-spatial-norm02-k5-seed42 |\n| obs_only | spatial | crm_obs_only | 43 | 5 | 32.0 | eval-obs-only-spatial-norm02-k5-seed43 |\n| obs_only | spatial | crm_obs_only | 44 | 5 | 37.0 | eval-obs-only-spatial-norm02-k5-seed44-r2 |\n| obs_only | spatial | crm_obs_only | 45 | 5 | 34.0 | eval-obs-only-spatial-norm02-k5-seed45-r2 |\n| obs_only | spatial | crm_obs_only | None | None | 0 | eval-obs-only-spatial-v2 |\n| obs_only | spatial | crm_obs_only | 42 | None | 33 | eval-obs-only-spatial-norm02-seed42-r2 |\n| obs_only | spatial | crm_obs_only | 43 | None | 34.0 | eval-obs-only-spatial-norm02-seed43-r2 |\n| obs_only | spatial | crm_obs_only | 44 | None | 36.0 | eval-obs-only-spatial-norm02-seed44 |\n| obs_only | spatial | crm_obs_only | 45 | None | 34.0 | eval-obs-only-spatial-norm02-seed45 |\n| obs_only | spatial | crm_obs_only | 46 | None | 33.0 | eval-obs-only-spatial-norm02-seed46-r2 |\n| obs_only | spatial | crm_obs_only | 47 | None | 32.0 | eval-obs-only-spatial-norm02-seed47 |\n| obs_only | spatial | crm_obs_only | 48 | None | 35.0 | eval-obs-only-spatial-seed48 |\n| obs_only | spatial | crm_obs_only | 49 | None | 32.0 | eval-obs-only-spatial-norm02-seed49 |\n| obs_only | spatial | crm_obs_only | 50 | None | 35.0 | eval-obs-only-spatial-norm02-seed50 |\n| obs_only | spatial | crm_obs_only | 52 | None | 33.0 | eval-obs-only-spatial-norm02-seed52 |\n| smolvla | None | None | 43 | 20 | 77 | eval-ksweep-k20-obs-obj-s43 |\n| smolvla | object | None | 42 | 20 | 75.5 | eval-ksweep-k20-obs-object-s42 |\n| smolvla | object | None | 43 | 20 | 73.5 | eval-ksweep-k20-obs-object-s43 |\n| smolvla | object | None | 44 | 20 | 71 | eval-ksweep-k20-obs-object-s44 |\n| smolvla | object | None | 42 | 5 | 73.5 | eval-ksweep-k5-obs-object-s42 |\n| smolvla | object | None | 43 | 5 | 73 | eval-ksweep-k5-obs-object-s43 |\n| smolvla | object | argmin | 42 | 5 | 15.0 | eval-argmin-object-k5-seed42 |\n| smolvla | object | argmin | 43 | 5 | 13.0 | eval-argmin-object-k5-seed43 |\n| smolvla | object | argmin | 44 | 5 | 11.0 | eval-argmin-object-k5-seed44-r2 |\n| smolvla | object | argmin | 45 | 5 | 13.0 | eval-argmin-object-k5-seed45 |\n| smolvla | object | crm_obs_only | 44 | 10 | 78.0 | smolvla-crm-norm005-k10-object-s44-cqa1 |\n| smolvla | object | crm_obs_only | 42 | 20 | 20.0 | eval-crm-object-k20-seed42 |\n| smolvla | object | crm_obs_only | 43 | 20 | 18.0 | eval-crm-object-k20-seed43 |\n| smolvla | object | crm_obs_only | 44 | 20 | 18.0 | eval-crm-object-k20-seed44 |\n| smolvla | object | random_selection | 42 | 5 | 14.0 | eval-random-selection-object-k5-seed42-r2 |\n| smolvla | object | random_selection | 43 | 5 | 11.0 | eval-random-selection-object-k5-seed43-r2 |\n| smolvla | object | random_selection | 44 | 5 | 10.0 | eval-random-selection-object-k5-seed44-r2 |\n| smolvla | object | random_selection | 45 | 5 | 7.0 | eval-random-selection-object-k5-seed45-r2 |\n| smolvla | object | random_selection | 42 | None | 11.0 | eval-random-selection-object-seed42 |\n| smolvla | object | random_selection | 43 | None | 77 | eval-random-selection-object-seed43-v2 |\n| smolvla | object | random_selection | 44 | None | 11.0 | eval-random-selection-object-seed44 |\n| smolvla | object | random_selection | 45 | None | 10.0 | eval-random-selection-object-seed45 |\n| smolvla | object | random_selection | 46 | None | 10.0 | eval-random-selection-object-seed46-r3 |\n| smolvla | object | random_selection | 47 | None | 7 | eval-random-selection-object-seed47 |\n| smolvla | object | random_selection | 48 | None | 10.0 | eval-random-selection-object-seed48 |\n| smolvla | object | random_selection | 49 | None | 12.0 | eval-random-selection-object-seed49 |\n| smolvla | spatial | None | 42 | 5 | 79 | eval-k5-spatial-s42-sweep |\n| smolvla | spatial | crm_obs_only | 51 | 10 | 36.0 | eval-crm-spatial-k10-seed51 |\n| smolvla | spatial | random_selection | 42 | None | 34 | eval-random-selection-spatial-seed42 |\n| smolvla | spatial | random_selection | 43 | None | 26 | eval-random-selection-spatial-seed43-r2 |\n| smolvla | spatial | random_selection | 44 | None | 28.0 | eval-random-selection-spatial-seed44 |\n\n## E. CRM Always-On Ablation (τ=0.001)\n\n**Total data points: 28** (with valid SR)\n\n### Summary (Mean ± Std)\n\n| model | benchmark | n | seeds | SR (mean ± std) |\n|-------|-----------|---|-------|----------------|\n| pi05 | goal | 3 | 42,43,44 | 82.5 ± 1.0 |\n| pi05 | long | 2 | 42,43 | 78.2 ± 1.8 |\n| pi05 | object | 3 | 42,43,44 | 90.7 ± 1.3 |\n| pi05 | spatial | 1 | 42 | 96.0 |\n| smolvla | goal | 5 | 42,43,44,45,46 | 80.4 ± 1.0 |\n| smolvla | long | 4 | 42,43,44,45 | 43.2 ± 1.8 |\n| smolvla | object | 5 | 42,43,44,45,46 | 72.2 ± 3.0 |\n| smolvla | spatial | 5 | 42,43,44,45,46 | 77.9 ± 1.3 |\n\n### Per-seed detail\n\n| model | benchmark | seed | SR (%) | trigger_rate (%) | source_exp_id |\n|-------|-----------|------|--------|-----------------|---------------|\n| pi05 | goal | 42 | 81.5 | 100 | pi05-crm-always-on-goal-s42 |\n| pi05 | goal | 43 | 82.5 | 100 | pi05-crm-always-on-goal-s43 |\n| pi05 | goal | 44 | 83.5 | 100 | pi05-crm-always-on-goal-s44 |\n| pi05 | long | 42 | 77 | 100 | pi05-crm-always-on-long-s42 |\n| pi05 | long | 43 | 79.5 | 100 | pi05-crm-always-on-long-s43 |\n| pi05 | object | 42 | 90.5 | 100 | pi05-crm-always-on-object-s42 |\n| pi05 | object | 43 | 92 | 100 | pi05-crm-always-on-object-s43 |\n| pi05 | object | 44 | 89.5 | 100 | pi05-crm-always-on-object-s44 |\n| pi05 | spatial | 42 | 96 | 100 | pi05-crm-always-on-spatial-s42 |\n| smolvla | goal | 42 | 80 | 100 | crm-always-on-goal-s42 |\n| smolvla | goal | 43 | 79.5 | 100 | crm-always-on-goal-s43 |\n| smolvla | goal | 44 | 80.5 | 100 | crm-always-on-goal-s44 |\n| smolvla | goal | 45 | 82 | 100 | crm-always-on-goal-s45 |\n| smolvla | goal | 46 | 80 | 100 | crm-always-on-goal-s46 |\n| smolvla | long | 42 | 41.0 | 100 | crm-always-on-long-s42 |\n| smolvla | long | 43 | 45.5 | 100 | crm-always-on-long-s43 |\n| smolvla | long | 44 | 43.0 | 100 | crm-always-on-long-s44 |\n| smolvla | long | 45 | 43.5 | 100 | crm-always-on-long-s45 |\n| smolvla | object | 42 | 71.0 | 100 | crm-always-on-object-s42 |\n| smolvla | object | 43 | 73.5 | 100 | crm-always-on-object-s43 |\n| smolvla | object | 44 | 74.5 | 100 | crm-always-on-object-s44 |\n| smolvla | object | 45 | 74.5 | 100 | crm-always-on-object-s45 |\n| smolvla | object | 46 | 67.5 | 100 | crm-always-on-object-s46 |\n| smolvla | spatial | 42 | 79.0 | 100 | crm-always-on-spatial-s42 |\n| smolvla | spatial | 43 | 76 | 100 | crm-always-on-spatial-s43 |\n| smolvla | spatial | 44 | 79 | 100 | crm-always-on-spatial-s44 |\n| smolvla | spatial | 45 | 77.0 | 100 | crm-always-on-spatial-s45 |\n| smolvla | spatial | 46 | 78.5 | 100 | crm-always-on-spatial-s46 |\n\n## F. Data Gaps & Notes\n\n### Bonus seed coverage (target: 6 seeds per benchmark × method)\n\n- **goal / reconvla**: 5 seeds — needs 1 more\n- **long / adaptive_conformal_crm**: 4 seeds — needs 2 more\n\n### Pi05 cross-VLA coverage (target: 3 seeds per benchmark × method)\n\nAll benchmark × method combinations have ≥3 seeds.\n\n### CRM always-on coverage\n\n- **pi05 / long**: 2 seeds — needs 1 more\n- **pi05 / spatial**: 1 seeds — needs 2 more\n\n### Deduplication notes\n- Multiple runs for same conditions (different servers, -r2/-r3 reruns). This summary keeps the run with highest SR.\n- Pi05 vla_only experiments with SR=0% excluded as known OOM artifacts.\n- Trigger rates stored inconsistently: some as fractions (0.0–1.0), some as percentages (0–100).",
      "numLines": 485,
      "startLine": 1,
      "totalLines": 485
    }
  }
}
```

</details>

---


### Assistant

_source line 78_

Content looks correct. Writing to the target location.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "uuid": "6720f020-1386-4a8d-ae2c-aa9788985ccf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192bh2gDUyuJojtrjzYeZpd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16082,
      "cache_read_input_tokens": 99827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16082
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

_source line 79_

<details open><summary>🔧 Tool call — Bash · `toolu_012YyaEANN3bYWLAwk6S1sRD`</summary>

```json
{
  "command": "cp /tmp/supplementary_summary_final.md /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/supplementary/supplementary_summary.md",
  "description": "Copy updated summary to target location"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "uuid": "026e0231-1018-4983-9b5a-ed83bc9fe1ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192bh2gDUyuJojtrjzYeZpd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16082,
      "cache_read_input_tokens": 99827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16082
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

_source line 80 · 2026-05-28T16:27:26.247Z_

<details><summary>↩ Tool result · `toolu_012YyaEANN3bYWLAwk6S1sRD`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "uuid": "0a71f545-1466-4a0e-a087-86e17d795158",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---


### Tool call

_source line 81_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UouS29abSFFQi1oenjJpPT`</summary>

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
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "uuid": "3a82ce1d-bcc9-4aae-bc17-d5a54d07391b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYFE3UPP9CkptA4731fyYb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 115909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
      },
      "output_tokens": 50,
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

_source line 82 · 2026-05-28T16:27:29.089Z_

<details><summary>↩ Tool result · `toolu_01UouS29abSFFQi1oenjJpPT`</summary>

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
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "uuid": "4fef1a94-48cb-4c82-8df6-ea38857dcff9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---


### Tool call

_source line 83_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01M6eTMfpCdUWy1i3aDEJk9r`</summary>

```json
{
  "name": "supplementary_summary",
  "type": "report",
  "description": "Refreshed supplementary experiment summary from registry data. Fixed missing SR extraction (overall_success_rate field), corrected tau parsing, expanded coverage across all 5 categories (tau-sweep, bonus seeds, pi05 cross-VLA, K-sweep, CRM always-on).",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/supplementary/supplementary_summary.md",
  "tags": [
    "supplementary",
    "summary",
    "registry-refresh"
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
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "uuid": "756fc991-8250-45f8-9c40-f2ee805fd6a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HYvUsMXRSYtQawHDwYbmr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 116068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 712
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

_source line 84 · 2026-05-28T16:27:35.841Z_

<details><summary>↩ Tool result · `toolu_01M6eTMfpCdUWy1i3aDEJk9r`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260528_4d2a92\", \"name\": \"supplementary_summary\", \"type\": \"report\", \"description\": \"Refreshed supplementary experiment summary from registry data. Fixed missing SR extraction (overall_success_rate field), corrected tau parsing, expanded coverage across all 5 categories (tau-sweep, bonus seeds, pi05 cross-VLA, K-sweep, CRM always-on).\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/supplementary_summary_4d2a92.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-28T16:27:35.217997+00:00\", \"tags\": [\"supplementary\", \"summary\", \"registry-refresh\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "uuid": "ffa39634-b366-4040-8450-e7d2cef37161",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260528_4d2a92\\\", \\\"name\\\": \\\"supplementary_summary\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Refreshed supplementary experiment summary from registry data. Fixed missing SR extraction (overall_success_rate field), corrected tau parsing, expanded coverage across all 5 categories (tau-sweep, bonus seeds, pi05 cross-VLA, K-sweep, CRM always-on).\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/report/supplementary_summary_4d2a92.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-28T16:27:35.217997+00:00\\\", \\\"tags\\\": [\\\"supplementary\\\", \\\"summary\\\", \\\"registry-refresh\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260528_4d2a92\", \"name\": \"supplementary_summary\", \"type\": \"report\", \"description\": \"Refreshed supplementary experiment summary from registry data. Fixed missing SR extraction (overall_success_rate field), corrected tau parsing, expanded coverage across all 5 categories (tau-sweep, bonus seeds, pi05 cross-VLA, K-sweep, CRM always-on).\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/supplementary_summary_4d2a92.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-28T16:27:35.217997+00:00\", \"tags\": [\"supplementary\", \"summary\", \"registry-refresh\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 85_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01M9qcUagzxkp1Gn3N4owDvp`</summary>

```json
{
  "todos": [
    {
      "content": "Extract tau-sweep data from registry",
      "status": "completed",
      "activeForm": "Extracting tau-sweep data"
    },
    {
      "content": "Extract bonus seeds data from registry",
      "status": "completed",
      "activeForm": "Extracting bonus seeds data"
    },
    {
      "content": "Extract Pi05 cross-VLA data from registry",
      "status": "completed",
      "activeForm": "Extracting Pi05 cross-VLA data"
    },
    {
      "content": "Extract K-sweep data from registry",
      "status": "completed",
      "activeForm": "Extracting K-sweep data"
    },
    {
      "content": "Extract CRM always-on data from registry",
      "status": "completed",
      "activeForm": "Extracting CRM always-on data"
    },
    {
      "content": "Generate and save updated supplementary_summary.md",
      "status": "completed",
      "activeForm": "Generating supplementary_summary.md"
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
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "uuid": "065c8216-397c-4447-83b7-dd17aacd1065",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T3xRbTr7qehnnuiAXKbCZX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 116780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 604
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

_source line 86 · 2026-05-28T16:27:40.235Z_

<details><summary>↩ Tool result · `toolu_01M9qcUagzxkp1Gn3N4owDvp`</summary>

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
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "uuid": "5375727f-23f0-4911-82b7-b0c179e7b34d",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Extract tau-sweep data from registry",
        "status": "completed",
        "activeForm": "Extracting tau-sweep data"
      },
      {
        "content": "Extract bonus seeds data from registry",
        "status": "completed",
        "activeForm": "Extracting bonus seeds data"
      },
      {
        "content": "Extract Pi05 cross-VLA data from registry",
        "status": "completed",
        "activeForm": "Extracting Pi05 cross-VLA data"
      },
      {
        "content": "Extract K-sweep data from registry",
        "status": "completed",
        "activeForm": "Extracting K-sweep data"
      },
      {
        "content": "Extract CRM always-on data from registry",
        "status": "completed",
        "activeForm": "Extracting CRM always-on data"
      },
      {
        "content": "Generate and save updated supplementary_summary.md",
        "status": "in_progress",
        "activeForm": "Generating supplementary_summary.md"
      }
    ],
    "newTodos": [
      {
        "content": "Extract tau-sweep data from registry",
        "status": "completed",
        "activeForm": "Extracting tau-sweep data"
      },
      {
        "content": "Extract bonus seeds data from registry",
        "status": "completed",
        "activeForm": "Extracting bonus seeds data"
      },
      {
        "content": "Extract Pi05 cross-VLA data from registry",
        "status": "completed",
        "activeForm": "Extracting Pi05 cross-VLA data"
      },
      {
        "content": "Extract K-sweep data from registry",
        "status": "completed",
        "activeForm": "Extracting K-sweep data"
      },
      {
        "content": "Extract CRM always-on data from registry",
        "status": "completed",
        "activeForm": "Extracting CRM always-on data"
      },
      {
        "content": "Generate and save updated supplementary_summary.md",
        "status": "completed",
        "activeForm": "Generating supplementary_summary.md"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 87_

`supplementary_summary.md` 已从 registry 实际数据重建。

**核心修复**：旧版漏读了 `overall_success_rate` 字段（只认 `success_rate`），导致大量实验被误判为无 SR。

**数据变化对比**：

| 类别 | 旧版 | 新版 |
|------|------|------|
| **B. Bonus seeds** | | |
| long / adaptive | 0 valid | **4 seeds** (s44-47, SR=57.4±2.3) |
| long / crm_obs_only | 1 seed | **6 seeds** (s42-47) |
| long / reconvla | 2 seeds | **6 seeds** (s42-47) |
| long / vla_only | 3 seeds | **6 seeds** (s42-47) |
| object / adaptive | 1 seed | **6 seeds** (s42-47) |
| object / crm_obs_only | 1 seed | **6 seeds** (s42-47) |
| goal / reconvla | 2 seeds | **5 seeds** (s43-47) |
| goal / crm_obs_only | 5 seeds | **7 seeds** (+s43,s48) |
| **C. Pi05** | | |
| long / crm_obs_only | 1 seed | **3 seeds** (s42-44) |
| **E. CRM always-on** | | |
| pi05 / goal | 1 seed | **3 seeds** |
| smolvla / long | 3 seeds | **4 seeds** (+s45) |

**剩余真实缺口**（Section F）：
- goal / reconvla: 5 seeds（差1）
- long / adaptive: 4 seeds（差2）
- pi05 / long CRM always-on: 2 seeds（差1）
- pi05 / spatial CRM always-on: 1 seed（差2）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "uuid": "4da8a55b-c99b-476a-9407-c66d3ddfd4f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpBknvwwC78Zb6WPtqvhKV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 300,
      "cache_read_input_tokens": 117384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 300
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

_source line 88_

`supplementary_summary.md` 已从 registry 实际数据重建。

**核心修复**：旧版漏读了 `overall_success_rate` 字段（只认 `success_rate`），导致大量实验被误判为无 SR。

**数据变化对比**：

| 类别 | 旧版 | 新版 |
|------|------|------|
| **B. Bonus seeds** | | |
| long / adaptive | 0 valid | **4 seeds** (s44-47, SR=57.4±2.3) |
| long / crm_obs_only | 1 seed | **6 seeds** (s42-47) |
| long / reconvla | 2 seeds | **6 seeds** (s42-47) |
| long / vla_only | 3 seeds | **6 seeds** (s42-47) |
| object / adaptive | 1 seed | **6 seeds** (s42-47) |
| object / crm_obs_only | 1 seed | **6 seeds** (s42-47) |
| goal / reconvla | 2 seeds | **5 seeds** (s43-47) |
| goal / crm_obs_only | 5 seeds | **7 seeds** (+s43,s48) |
| **C. Pi05** | | |
| long / crm_obs_only | 1 seed | **3 seeds** (s42-44) |
| **E. CRM always-on** | | |
| pi05 / goal | 1 seed | **3 seeds** |
| smolvla / long | 3 seeds | **4 seeds** (+s45) |

**剩余真实缺口**（Section F）：
- goal / reconvla: 5 seeds（差1）
- long / adaptive: 4 seeds（差2）
- pi05 / long CRM always-on: 2 seeds（差1）
- pi05 / spatial CRM always-on: 1 seed（差2）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 446736,
  "duration_api_ms": 441652,
  "num_turns": 31,
  "stop_reason": "end_turn",
  "session_id": "535fc78c-a73d-46c8-8480-bacfedf2ba99",
  "total_cost_usd": 2.2948057499999996,
  "usage": {
    "input_tokens": 33,
    "cache_creation_input_tokens": 105839,
    "cache_read_input_tokens": 1671360,
    "output_tokens": 31823,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 105839,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 522,
        "cache_read_input_tokens": 117384,
        "cache_creation_input_tokens": 300,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 300
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1812,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001892,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 33,
      "outputTokens": 31823,
      "cacheReadInputTokens": 1671360,
      "cacheCreationInputTokens": 105839,
      "webSearchRequests": 0,
      "costUSD": 2.29291375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "cc6ef596-299e-4884-bb78-5c2b31233612"
}
```

</details>

---
