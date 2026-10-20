# Research conversation: In the file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex, find the

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6e16af898b1545df.jsonl`
- **Structured JSON:** [`58cbcfd4812b3cbc8a0c.json`](../../sessions/58/58cbcfd4812b3cbc8a0c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-20T01:36:01.751Z_

In the file /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex, find the Mistral downstream table (tab:mistral_downstream). I need:
1. The table content (what allocation does it use — global or uniform?)
2. The caption text
3. Any nearby text mentioning allocation strategy

Also find in experiments.tex any reference to "tab:mistral" to see what caption/allocation is used. Report the exact lines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a403245c-091e-4e8d-bdc8-72b45d6db8d7",
  "agentId": "a6e16af898b1545df",
  "type": "user",
  "uuid": "5e6398f4-e424-49f7-9d14-1feba2d261dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T01:36:03.486Z_

I'll help you find the Mistral downstream table and related references. Let me search for these files and their content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e6398f4-e424-49f7-9d14-1feba2d261dc",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpA7ve61tHkhwoMJTg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c9abbde3-d744-4c6f-af7a-cdb5001567bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DhPytaMgmzRhQ2xoPRmTHr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18789,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18789,
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

_source line 3 · 2026-05-20T01:36:03.643Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ku4WMPDrcSpbaEQAt1iid9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9abbde3-d744-4c6f-af7a-cdb5001567bf",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpA7ve61tHkhwoMJTg",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bd36a2e1-d9b6-40f3-a4c7-8a2badc6586c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DhPytaMgmzRhQ2xoPRmTHr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18789,
      "cache_read_input_tokens": 0,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18789
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 115,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18789,
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

_source line 4 · 2026-05-20T01:36:03.659Z_

<details><summary>↩ Tool result · `toolu_01Ku4WMPDrcSpbaEQAt1iid9`</summary>

```text
1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.
34	Our contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.
35	
36	
37	\section{Predictor Bottleneck Sensitivity}
38	\label{app:db_sensitivity}
39	
40	Table~\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.
41	
42	\begin{table}[h]
43	\centering
44	\caption{Predictor bottleneck sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}
45	\label{tab:db_sensitivity}
46	\small
47	\begin{tabular}{lcccc}
48	\toprule
49	$d_b$ & Params & TEAL global & $\Delta$ & Per-token \\
50	\midrule
51	64 & 38.2M (0.48\%) & 12.076 & +0.9\% & 10.16 \\ % exp_id: db_sensitivity_sweep
52	128 & 75.9M (0.95\%) & 11.963 & --- & 9.218 \\ % exp_id: db_sensitivity_sweep
53	256 & 151.5M (1.89\%) & 12.105 & +1.2\% & 8.586 \\ % exp_id: db_sensitivity_sweep
54	512 & 302.5M (3.77\%) & 12.315 & +2.9\% & 7.93 \\ % exp_id: db_sensitivity_sweep
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	Under TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\to$7.93).
60	This divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.
61	The $d_b{=}128$ configuration (75.9M params, $<$1\% of base model) is therefore optimal for the TEAL inference protocol.
62	
63	\subsection{Temperature Schedule Sensitivity}
64	\label{app:tau_sensitivity}
65	
66	\begin{table}[h]
67	\centering
68	\caption{Temperature schedule sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
69	\label{tab:tau_sensitivity}
70	\small
71	\begin{tabular}{lc}
72	\toprule
73	$\tau$ Schedule & PPL$\downarrow$ \\
74	\midrule
75	Fixed $\tau{=}0.5$ & \textbf{11.861} \\ % exp_id: tau_schedule_sweep
76	Linear $1.0 \to 0.1$ (default) & 11.963 \\ % exp_id: tau_schedule_sweep
77	Fixed $\tau{=}0.1$ & 12.072 \\ % exp_id: tau_schedule_sweep
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	Temperature schedule has minimal impact ($<$1.8\% PPL variation).
83	The linear annealing default is a conservative choice; even removing annealing entirely (fixed $\tau{=}0.5$) yields comparable performance.
84	
85	\subsection{Training Convergence}
86	\label{app:training_convergence}
87	
88	\begin{table}[h]
89	\centering
90	\caption{Training convergence at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
91	\label{tab:training_convergence}
92	\small
93	\begin{tabular}{cc}
94	\toprule
95	Steps & PPL$\downarrow$ \\
96	\midrule
97	200 & 15.158 \\ % exp_id: training_steps_sweep
98	400 & 12.538 \\ % exp_id: training_steps_sweep
99	600 & 12.046 \\ % exp_id: training_steps_sweep
100	800 & 11.907 \\ % exp_id: training_steps_sweep
101	1000 & \textbf{11.906} \\ % exp_id: training_steps_sweep
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	Training converges rapidly: 95\% of the quality gap closes by step 600, and performance saturates by step 800 ($\Delta < 0.001$ between 800 and 1000 steps).
107	Our default of 1000 steps provides a conservative margin.
108	
109	
110	\section{Adaptive Penalty Controller Dynamics}
111	\label{app:lagrangian}
112	
113	Table~\ref{tab:lagrangian} reports the convergence of the adaptive penalty controller across sparsity targets.
114	The geometric doubling pattern ($1 \to 2 \to 4 \to 8 \to \ldots$) enables $\lambda$ to reach steady state within $\sim$10 steps; the deadzone ($\epsilon = 0.02$) then stabilizes $\lambda$ once actual sparsity is within $\pm$2\% of the target.
115	
116	\begin{table}[h]
117	\centering
118	\caption{Penalty controller convergence across sparsity targets (multiplicative schedule, margin $\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}
119	\label{tab:lagrangian}
120	\small
121	\begin{tabular}{lccccc}
122	\toprule
123	Target $\rho$ & $\lambda_{\max}$ & Final $\lambda$ & Actual sparsity & Deviation \\
124	\midrule
125	30\% & 5000 & 5000 (cap) & 0.285 & 5.0\% \\ % exp_id: kl_30pct_s42
126	40\% & 5000 & 625 & 0.398 & 0.5\% \\ % exp_id: kl_40pct_s42
127	50\% & 1000 & 8 & 0.504 & 0.8\% \\ % exp_id: kl_50pct_s42
128	70\% & 1000 & 1000 (cap) & 0.688 & 1.7\% \\ % exp_id: kl_70pct_s42
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	At 50\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.
134	At 30\% and 70\%, the gap between the gate prior and target is larger, driving $\lambda$ to its respective caps.
135	The 40\% target converges to $\lambda = 625$ with only 0.5\% deviation; this precision reflects a regime where the target is reachable without $\lambda$ saturation.
136	
137	\begin{figure}[h]
138	\centering
139	\includegraphics[width=\columnwidth]{lagrangian_dynamics.pdf}
140	\caption{Adaptive penalty controller convergence across sparsity targets. Upper panel: penalty weight $\lambda$ (log scale) over training steps. The 30\% target requires extreme penalty ($\lambda \to 5000$) to suppress activations below their natural density, while 50\% needs only $\lambda \approx 8$ since SwiGLU gates already cluster near this sparsity. Lower panel: actual sparsity (solid) converges to the target (dashed) within $\sim$10 steps via geometric doubling.}
141	\label{fig:lagrangian_dynamics}
142	\end{figure}
143	
144	Temperature $\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.
145	A mild loss increase in the final $\sim$100 steps is expected: as masks become more binary ($\tau \to 0$), discrete rounding noise slightly increases KL divergence, consistent with convergence toward the hard-mask inference regime.
146	
147	The controller reliably drives actual sparsity to within 5\% of the target across all tested regimes, with $\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.
148	For the 30\% target, actual sparsity is $\approx$28.5\% (5\% deviation). This does not affect conclusions: TEAL at 28.5\% actual sparsity yields PPL 10.30 (vs.\ 10.97 at exact 30\%), a 0.67 PPL difference negligible relative to the KL vs.\ TEAL gap (8.96 vs.\ 10.97).
149	
150	
151	\section{Out-of-Distribution Evaluation}
152	\label{app:ood}
153	
154	To address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\cite{raffel2020c4} validation set under TEAL global allocation.
155	
156	\begin{table}[h]
157	\centering
158	\caption{Out-of-distribution evaluation on C4 validation (PPL$\downarrow$). 30\% KL reports 2-seed mean$\pm$std; other entries use seed 42.}
159	\label{tab:ood}
160	\small
161	\begin{tabular}{llc}
162	\toprule
163	Sparsity & Method & C4 PPL$\downarrow$ \\
164	\midrule
165	0\% & Dense & 9.21 \\
166	\midrule
167	30\% & KL predictor (Ours) & \textbf{16.03$\pm$0.01} \\ % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123
168	\midrule
169	\multirow{2}{*}{50\%} & KL predictor (Ours) & \textbf{18.40} \\ % exp_id: eval_c4_ood_kl50
170	& TEAL vanilla & 38.75 \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	At the 30\% sparsity level, the KL predictor achieves C4 PPL 16.03$\pm$0.01 (2-seed, $1.74\times$ dense), confirming OOD generalization.
176	At 50\%, the KL predictor achieves 52.5\% relative advantage over TEAL (18.40 vs.\ 38.75), comparable to the 51\% advantage on WikiText-2 (11.79 vs.\ 23.90), confirming that KL-trained predictions generalize across distributions.
177	
178	
179	\section{Per-Layer Retention Analysis}
180	\label{app:retention}
181	
182	\begin{figure}[h]
183	\centering
184	\includegraphics[width=\columnwidth]{per_layer_retention_chart.pdf}
185	\caption{Per-layer neuron retention under global top-$k$ allocation at 30\%, 50\%, and 70\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\% (L31) even at 30\% sparsity. At 70\%, starvation extends to mid-layers (L10--12: 16.7--20.1\%), explaining the transition to the capacity-limited regime.}
186	\label{fig:retention}
187	\end{figure}
188	
189	
190	\section{Training Stability}
191	\label{app:stability}
192	
193	Three-seed evaluation ($s \in \{42, 123, 456\}$) at 50\% sparsity under uniform allocation yields PPL $11.92 \pm 0.07$ (CV=0.6\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform
194	Downstream metrics are similarly stable: ARC-c $33.8 \pm 1.2$\%, WinoGrande $62.9 \pm 0.1$\%, MMLU $28.0 \pm 0.6$\%, GSM8K $2.2 \pm 0.1$\%.
195	
196	Under global allocation at 50\%, MMLU is equally stable: $28.1 \pm 0.2$\% (s42=27.89, s123=28.34, s456=27.94); the near-random performance is therefore capacity-limited rather than seed-sensitive ($\sigma$=0.2pp vs.\ 9.5pp at 30\% global). % exp_id: multi_seed_kl50_global
197	The low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.
198	
199	
200	\section{Extended SNR Analysis}
201	\label{app:snr_extended}
202	
203	We measure per-layer gradient SNR at 7 checkpoints (steps 0, 50, 100, 150, 200, 250, 300) with 95\% bootstrap confidence intervals.
204	The SNR trajectory is non-monotonic: KL starts with higher SNR at step 0, but BCE surpasses KL during mid-training (steps 100--250) as its per-neuron classification objective concentrates gradients on the remaining hard neurons. KL's advantage re-emerges in later training and reaches $5.14\times$ at step 300 of 1000 ( $5.877{\times}10^{-3}$ vs.\ $1.144{\times}10^{-3}$). % exp_id: snr_extended_r6w3
205	This reversal is consistent with KL's gradient coupling becoming effective only after the predictor has learned a coarse mask structure: early training explores broadly (lower SNR), while convergence concentrates signal through the inter-neuron Jacobian pathway (\S\ref{sec:method:gradient}).
206	
207	
208	\section{Extended Downstream Evaluation}
209	\label{app:downstream}
210	
211	Table~\ref{tab:downstream} reports HellaSwag and PIQA across sparsity levels and allocation strategies.
212	
213	\begin{table}[h]
214	\centering
215	\caption{Extended downstream benchmarks (LLaMA-3.1-8B). HellaSwag: 10-shot normalized acc; PIQA: 0-shot normalized acc. KL 30\% uniform: 3-seed mean$\pm$std; others: seed 42.}
216	\label{tab:downstream}
217	\small
218	\begin{tabular}{llcc}
219	\toprule
220	Sparsity & Method & HellaSwag & PIQA \\
221	\midrule
222	0\% & Dense & \textbf{82.35} & \textbf{80.90} \\
223	\midrule
224	\multirow{3}{*}{30\%}
225	& KL uniform & \textbf{71.07$\pm$0.54} & \textbf{74.95$\pm$0.25} \\ % exp_id: hellaswag_piqa_kl30_uniform (3-seed)
226	& TEAL uniform & 63.31 & 72.80 \\ % exp_id: bench_teal30_uniform_6task
227	& BCE isocompute & 62.81 & 74.21 \\ % exp_id: bce_isocompute_30u_hellaswag_piqa
228	\midrule
229	\multirow{3}{*}{50\%}
230	& KL global & \textbf{58.95} & \textbf{69.48} \\ % exp_id: hellaswag_piqa_kl50_global
231	& KL uniform & 56.66 & 69.10 \\ % exp_id: hellaswag_piqa_kl50_uniform
232	& TEAL uniform & 39.35 & 63.66 \\ % exp_id: bench_teal50_uniform_6task
233	\bottomrule
234	\end{tabular}
235	\end{table}
236	
237	At 30\%, the KL predictor retains 86.3\% of dense HellaSwag accuracy (71.07$\pm$0.54 vs.\ 82.35, 3-seed) and 92.6\% of PIQA (74.95$\pm$0.25 vs.\ 80.90), confirming moderate degradation on non-reasoning tasks.
238	At 50\%, global allocation outperforms uniform on HellaSwag (+2.29pp), consistent with the budget-concentration benefit observed for PPL in the capacity-limited regime (\S\ref{sec:scaling}); PIQA shows a smaller gap (+0.38pp).
239	
240	
241	\section{Compensation Training Convergence}
242	\label{app:comp_convergence}
243	
244	All compensation networks~\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\% s42 (final loss 0.70), 30\% s456 (0.68), 50\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42
245	
246	
247	\section{Qwen-2.5-14B Detailed Results}
248	\label{app:14b}
249	
250	\begin{table}[h]
251	\centering
252	\caption{Qwen-2.5-14B at 30\% nominal sparsity. Actual sparsity differs: KL 29.6\% (3-seed), TEAL 26.8\% (target 27.5\%). \textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\% native sparsity (\S\ref{sec:method:gradient}), so forced global top-$k$ is used.}
253	\label{tab:14b}
254	\small
255	\resizebox{\columnwidth}{!}{
256	\begin{tabular}{lcccccccc}
257	\toprule
258	Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K & HS & PIQA \\
259	\midrule
260	Dense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 & 84.20 & 81.94 \\
261	\midrule
262	\multicolumn{8}{l}{\emph{Global top-$k$ allocation}} \\
263	KL (Ours) & \textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 & --- & --- \\ % exp_id: qwen14b_kl30_s42
264	TEAL & 8.73 & 56.83 & \textbf{72.69} & \textbf{71.83} & 49.51 & --- & --- \\ % exp_id: qwen14b_teal30_eval
265	BCE & 8.76 & \textbf{57.59} & 72.61 & 71.67 & \textbf{53.07} & --- & --- \\ % exp_id: qwen14b_bce30_s42_eval
266	\midrule
267	\multicolumn{8}{l}{\emph{Uniform allocation}} \\
268	KL (Ours) & \textbf{7.90} & 53.50 & \textbf{72.82} & 63.55 & 32.1$\pm$5.2 & 72.68 & 76.01 \\ % exp_id: qwen14b_kl30_uniform (v3/v5 3-seed)
269	TEAL & 8.01 & \textbf{55.29} & 69.85 & \textbf{66.34} & \textbf{57.1} & --- & --- \\ % exp_id: qwen14b_teal30_uniform
270	\bottomrule
271	\end{tabular}}
272	\end{table}
273	
274	
275	\section{Full Allocation Analysis}
276	\label{app:alloc_full}
277	
278	Table~\ref{tab:phase_full} extends the main-text allocation analysis (Table~\ref{tab:phase}) with all downstream metrics.
279	
280	\begin{table*}[t]
281	\centering
282	\caption{Full allocation analysis: global top-$k$ vs.\ uniform across sparsity levels (LLaMA-3.1-8B). Entries with $\pm$: 3-seed mean$\pm$std ($s \in \{42, 123, 456\}$); others: seed 42. $^\ast$High MMLU seed variance (individual seeds span 25.3--43.5\%). 40\% uniform not evaluated.}
283	\label{tab:phase_full}
284	\begin{tabular}{llccccc}
285	\toprule
286	Sparsity & Allocation & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
287	\midrule
288	\multirow{2}{*}{25\%}
289	& Global & \textbf{8.17} & 45.4 & 70.6 & \textbf{46.6} & \textbf{11.5} \\
290	& Uniform & 8.23 & \textbf{46.5} & \textbf{71.8} & 44.0 & 11.0 \\
291	\midrule
292	\multirow{2}{*}{30\%}
293	& Global & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5$^\ast$ & \textbf{8.0$\pm$0.7} \\
294	& Uniform & \textbf{8.81$\pm$0.02} & 43.7$\pm$2.5 & 68.9$\pm$0.4 & \textbf{40.7$\pm$1.3} & 7.5$\pm$0.1 \\
295	\midrule
296	\multirow{2}{*}{35\%}
297	& Global & \textbf{9.31} & \textbf{38.9} & \textbf{67.6} & \textbf{40.4} & \textbf{7.7} \\
298	& Uniform & 9.44 & 38.7 & 66.5 & 37.8 & 4.3 \\
299	\midrule
300	40\% & Global & 10.12 & 41.0 & 65.4 & 38.1 & 5.0 \\
301	\midrule
302	\multirow{2}{*}{45\%}
303	& Global & \textbf{10.80} & \textbf{39.2} & \textbf{64.6} & 30.4 & \textbf{3.0} \\
304	& Uniform & 10.95 & 37.6 & 63.6 & \textbf{30.6} & 2.7 \\
305	\midrule
306	\multirow{2}{*}{50\%}
307	& Global & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & \textbf{28.1$\pm$0.2} & 1.29 \\
308	& Uniform & 11.92$\pm$0.07 & 32.76 & 62.90 & 28.0$\pm$0.6 & \textbf{2.12} \\
309	\bottomrule
310	\end{tabular}
311	\end{table*}
312	
313	
314	\section{Mask Pattern Visualization}
315	\label{app:mask_viz}
316	
317	Figure~\ref{fig:mask_heatmap} shows per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\% and 50\% sparsity.
318	Figure~\ref{fig:scatter} shows per-neuron importance scores at layer 16.
319	Figure~\ref{fig:mask_comparison} shows binary mask comparisons at layers 2, 16, and 28.
320	
321	\begin{figure}[t]
322	\centering
323	\includegraphics[width=0.95\columnwidth]{neuron_scatter_layer16.pdf}
324	\caption{KL vs.\ magnitude importance scores for layer 16 neurons at 50\% sparsity. 41\% of neurons fall in disagreement quadrants where one method selects a neuron the other discards.}
325	\label{fig:scatter}
326	\end{figure}
327	
328	\begin{figure*}[t]
329	\centering
330	\includegraphics[width=\textwidth]{mask_divergence_heatmap.pdf}
331	\caption{Per-layer Jaccard distance between KL-derived and magnitude-based masks at 30\% and 50\% sparsity (64 samples, 131K tokens). Divergence peaks in layers 24--28 (Jaccard distance $>$0.73 at 50\%) and increases with sparsity across all layers.}
332	\label{fig:mask_heatmap}
333	\end{figure*}
334	
335	\begin{figure*}[t]
336	\centering
337	\includegraphics[width=\textwidth]{mask_comparison.pdf}
338	\caption{Binary mask comparison between KL-derived and magnitude-based masks at selected layers (L2, L16, L28) for 30\% and 50\% sparsity (64 samples). Black = selected by both, light regions = selected by only one method. Deep layers show the largest divergence (L28 Jaccard distance: 0.60 at 30\%, 0.74 at 50\%).}
339	\label{fig:mask_comparison}
340	\end{figure*}
341	
342	
343	\section{Cross-Architecture Comparison}
344	\label{app:cross_arch}
345	
346	Table~\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).
347	
348	\begin{table}[h]
349	\centering
350	\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL\,/\,KL ratio. LLaMA uses global top-$k$; Mistral uses uniform allocation (matched within each architecture).}
351	\label{tab:cross_arch}
352	\small
353	\begin{tabular}{l@{\hspace{4pt}}cc@{\hspace{3pt}}c@{\hspace{6pt}}|@{\hspace{6pt}}cc@{\hspace{3pt}}c}
354	\toprule
355	 & \multicolumn{3}{c}{Mistral-7B} & \multicolumn{3}{c}{LLaMA-8B} \\
356	 & KL & TEAL & Adv & KL & TEAL & Adv \\
357	\midrule
358	30\% & \textbf{6.77} & 8.38 & 1.24$\times$ & \textbf{8.96} & 10.97 & 1.22$\times$ \\ % exp_id: kl_30_mistral, teal_30_mistral, kl30_3seed_global
359	50\% & \textbf{8.65} & 18.31 & 2.12$\times$ & \textbf{11.79} & 23.31 & 1.98$\times$ \\ % exp_id: kl_50_mistral, teal_50_mistral
360	70\% & \textbf{13.33} & 61.72 & 4.63$\times$ & \textbf{17.91} & 100.11 & 5.59$\times$ \\ % exp_id: kl_70_mistral, teal_70_mistral
361	\bottomrule
362	\end{tabular}
363	\end{table}
364	
365	The KL PPL advantage ratio is consistent across architectures (within 8\% at $\leq$50\% sparsity).
366	Table~\ref{tab:mistral_downstream} reports downstream task accuracy at 30\% sparsity on Mistral-7B-v0.3, confirming that KL's downstream advantage generalizes on 5 of 6 tasks;
367	GSM8K is the sole reversal.
368	
369	\begin{table}[h]
370	\centering
371	\caption{Mistral-7B-v0.3 downstream evaluation at 30\% sparsity (seed 42). KL outperforms TEAL on 5 of 6 tasks (largest: ARC-c +9.0pp, HellaSwag +8.8pp); GSM8K is the sole reversal.}
372	\label{tab:mistral_downstream}
373	\small
374	\resizebox{\columnwidth}{!}{
375	\begin{tabular}{lccccccc}
376	\toprule
377	Method & PPL$\downarrow$ & ARC-c & WG & HS & PIQA & MMLU & GSM8K \\
378	\midrule
379	Dense & 5.52 & 60.2 & 78.7 & 83.2 & 81.9 & 62.4 & 36.5 \\ % exp_id: lm_eval_mistral_dense, mistral_dense_hellaswag_piqa
380	KL 30\% & \textbf{6.77} & \textbf{50.1} & \textbf{69.1} & \textbf{68.9} & \textbf{75.2} & \textbf{44.0} & 11.1 \\ % exp_id: mistral_kl30_downstream
381	TEAL 30\% & 8.38 & 41.1 & 63.5 & 60.1 & 72.1 & 43.5 & \textbf{15.9} \\ % exp_id: mistral_teal30_downstream
382	\bottomrule
383	\end{tabular}}
384	\end{table}
385	
386	
387	\section{SPON Orthogonality}
388	\label{app:spon}
389	
390	SPON~\cite{xu2026spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\% PPL improvement (12.08$\to$11.79); the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42
391	The decomposition confirms that SPON and the KL predictor operate on largely orthogonal error sources.
392	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd36a2e1-d9b6-40f3-a4c7-8a2badc6586c",
  "isSidechain": true,
  "promptId": "a403245c-091e-4e8d-bdc8-72b45d6db8d7",
  "agentId": "a6e16af898b1545df",
  "type": "user",
  "uuid": "e4383b24-edf4-4ecb-b382-13c82117230a",
  "sourceToolAssistantUUID": "bd36a2e1-d9b6-40f3-a4c7-8a2badc6586c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T01:36:05.729Z_

Good! I found the Mistral downstream table. Now let me search for any references to "tab:mistral" in experiments.tex and check for more context about the allocation strategy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4383b24-edf4-4ecb-b382-13c82117230a",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpJDbLhHPfVVPJps6w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "68694bba-c125-4139-9717-dd436f2ed534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EntnoWurXUpxdoUBZMrxMZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 10297,
      "cache_read_input_tokens": 18789,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 96,
          "cache_read_input_tokens": 18789,
          "cache_creation_input_tokens": 10297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10297,
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

### Tool call

_source line 6 · 2026-05-20T01:36:05.733Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QdqiKjvLRGq33M7ydesD5u`</summary>

```json
{
  "pattern": "**/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68694bba-c125-4139-9717-dd436f2ed534",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpJDbLhHPfVVPJps6w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4a9dae4a-b92a-46cd-9d3f-aa869d50d0e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EntnoWurXUpxdoUBZMrxMZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 10297,
      "cache_read_input_tokens": 18789,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 96,
          "cache_read_input_tokens": 18789,
          "cache_creation_input_tokens": 10297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10297,
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

_source line 7 · 2026-05-20T01:36:05.749Z_

<details><summary>↩ Tool result · `toolu_01QdqiKjvLRGq33M7ydesD5u`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a9dae4a-b92a-46cd-9d3f-aa869d50d0e8",
  "isSidechain": true,
  "promptId": "a403245c-091e-4e8d-bdc8-72b45d6db8d7",
  "agentId": "a6e16af898b1545df",
  "type": "user",
  "uuid": "904fd1bb-037b-4621-803c-052eba646615",
  "sourceToolAssistantUUID": "4a9dae4a-b92a-46cd-9d3f-aa869d50d0e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-20T01:36:07.201Z_

Let me check what files exist in the paper directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "904fd1bb-037b-4621-803c-052eba646615",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpTEKnn75JR5B8yEGy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "98b0eade-6082-43bd-9c27-8e71f984a583",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018x7RQaBYhFBdTamxCux6jo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 111,
      "cache_read_input_tokens": 29086,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 111,
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

_source line 9 · 2026-05-20T01:36:07.844Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PHXL7FdMNDsp4fGgAnqC2Q`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98b0eade-6082-43bd-9c27-8e71f984a583",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpTEKnn75JR5B8yEGy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "13cf8950-109d-4838-8fa8-edd99a4e7180",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018x7RQaBYhFBdTamxCux6jo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 111,
      "cache_read_input_tokens": 29086,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 111
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 105,
          "cache_read_input_tokens": 29086,
          "cache_creation_input_tokens": 111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 111,
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

_source line 10 · 2026-05-20T01:36:08.025Z_

<details><summary>↩ Tool result · `toolu_01PHXL7FdMNDsp4fGgAnqC2Q`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13cf8950-109d-4838-8fa8-edd99a4e7180",
  "isSidechain": true,
  "promptId": "a403245c-091e-4e8d-bdc8-72b45d6db8d7",
  "agentId": "a6e16af898b1545df",
  "type": "user",
  "uuid": "f633ab39-4631-44ca-acf1-1f6d6a76aabb",
  "sourceToolAssistantUUID": "13cf8950-109d-4838-8fa8-edd99a4e7180",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T01:36:09.130Z_

Great! Now let me search for "tab:mistral" references in experiments.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f633ab39-4631-44ca-acf1-1f6d6a76aabb",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpcrmEixREYHG3iDKJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f525b706-d3da-479c-8262-ccd8fc69f67f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012RxRzHM953KuBzCTZuBibT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 488,
      "cache_read_input_tokens": 29197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 488,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 12 · 2026-05-20T01:36:09.652Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01SdBYaDDkXSqanUEBuTnxro`</summary>

```json
{
  "pattern": "tab:mistral",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f525b706-d3da-479c-8262-ccd8fc69f67f",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpcrmEixREYHG3iDKJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7a8ba887-e6ff-40ca-a88c-4c40cd8418c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012RxRzHM953KuBzCTZuBibT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 488,
      "cache_read_input_tokens": 29197,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 488
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 146,
          "cache_read_input_tokens": 29197,
          "cache_creation_input_tokens": 488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 488,
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

_source line 13 · 2026-05-20T01:36:09.672Z_

<details><summary>↩ Tool result · `toolu_01SdBYaDDkXSqanUEBuTnxro`</summary>

```text
230:Table~\ref{tab:mistral_downstream}); the 50\% capacity cliff also holds cross-architecture (MMLU 26.4\%$\approx$random; Appendix~\ref{app:cross_arch}). % exp_id: mistral_kl30_downstream, mistral_teal30_downstream, mistral_teal50_downstream
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a8ba887-e6ff-40ca-a88c-4c40cd8418c1",
  "isSidechain": true,
  "promptId": "a403245c-091e-4e8d-bdc8-72b45d6db8d7",
  "agentId": "a6e16af898b1545df",
  "type": "user",
  "uuid": "d16dfc0b-11d2-4fce-855e-e33c0e2d2512",
  "sourceToolAssistantUUID": "7a8ba887-e6ff-40ca-a88c-4c40cd8418c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-20T01:36:11.203Z_

Now let me get more context around that line and search for allocation strategy references near the Mistral table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d16dfc0b-11d2-4fce-855e-e33c0e2d2512",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpjuRZJ4sX43hxXy9g",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "99ab7d08-d532-4cba-acc2-b0f4a440f53d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JVCjJRGVBq6FyzBwmZWiqx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 29685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 247,
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

_source line 15 · 2026-05-20T01:36:11.459Z_

<details open><summary>🔧 Tool call — Read · `toolu_014hA8o94JoGBdLm8uymZN7K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "limit": 250
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99ab7d08-d532-4cba-acc2-b0f4a440f53d",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpjuRZJ4sX43hxXy9g",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "188dfd0d-5093-4ad9-b52a-de82b922e3f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JVCjJRGVBq6FyzBwmZWiqx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 29685,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 247
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 128,
          "cache_read_input_tokens": 29685,
          "cache_creation_input_tokens": 247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 247,
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

_source line 16 · 2026-05-20T01:36:11.466Z_

<details><summary>↩ Tool result · `toolu_014hA8o94JoGBdLm8uymZN7K`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4 on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB), using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), GSM8K (8-shot), HellaSwag (10-shot), and PIQA (0-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly\footnote{TEAL is deterministic; single-run evaluation suffices. KL/BCE predictors require multi-seed evaluation due to random initialization.}; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; and (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presents the primary comparison. Uniform allocation preserves downstream performance best; global allocation is analyzed to understand allocation-quality tradeoffs (\S\ref{sec:scaling}).
28	At 30\% sparsity, KL distillation under uniform allocation achieves PPL 8.81$\pm$0.02 (3-seed), reducing TEAL's perplexity by 19\% (10.82 $\to$ 8.81). % exp_id: bench_kl30_uniform, teal30_uniform
29	HellaSwag (86.3\% retention) and PIQA (92.6\% retention) confirm moderate degradation on non-reasoning tasks (Appendix~\ref{app:downstream}). % exp_id: hellaswag_piqa_kl30_uniform
30	Uniform allocation at 30\% achieves PPL 8.81$\pm$0.02 with stable downstream performance (MMLU 40.7$\pm$1.3\%, 3-seed; full stability analysis in Appendix~\ref{app:stability}), while global top-$k$ exhibits high seed variance (35.7$\pm$9.5\%) from late-layer starvation (L31 retention 28.4\%) interacting with predictor initialization (\S\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform, kl30_3seed
31	
32	At 50\% sparsity, the PPL advantage widens: 11.79 vs.\ 23.90 (51\% reduction over TEAL). % exp_id: bench_kl50_global, teal50_uniform
33	The predictor generalizes to C4 validation at both 30\% (PPL 16.03$\pm$0.01, 2-seed) and 50\% (52.5\% over TEAL; Appendix~\ref{app:ood}).
34	However, all methods exhibit downstream collapse on MMLU (28.1$\pm$0.2\% vs.\ 28.0$\pm$0.6\%, both $\approx$ random, 3-seed) and GSM8K ($<$2.2\%); this is a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform, multi_seed_kl50_global
35	
36	\begin{table}[t]
37	\centering
38	\caption{Main results on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$; downstream accuracy$\uparrow$). \textbf{Bold}: best per sparsity. $^\ast$Extended training budget ($2.71\times$ KL step budget), no compensation; training details in \S\ref{sec:isocompute}. $^\dagger$BCE 30\%: TEAL global (2700 steps). $\pm$: 3-seed mean$\pm$std ($s \in \{42, 123, 456\}$); unmarked: seed 42. TEAL uses uniform allocation at all sparsity levels.}
39	\label{tab:main}
40	\resizebox{\columnwidth}{!}{
41	\begin{tabular}{llccccc}
42	\toprule
43	Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
44	\midrule
45	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
46	\midrule
47	\multirow{4}{*}{30\%}
48	& TEAL uniform & 10.82 & 39.33 & 65.04 & \textbf{45.86} & \textbf{8.79} \\ % exp_id: teal30_uniform
49	& KL global (Ours) & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5 & 8.0$\pm$0.7 \\ % exp_id: kl30_3seed_global
50	& KL uniform & \textbf{8.81$\pm$0.02} & 43.7$\pm$2.5 & 68.9$\pm$0.4 & 40.7$\pm$1.3 & 7.5$\pm$0.1 \\ % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform
51	& BCE global$^\dagger$ & 11.25 & 41.2 & 66.0 & 36.3 & 6.0 \\ % exp_id: bce30_teal_global
52	\midrule
53	\multirow{4}{*}{50\%}
54	& TEAL uniform & 23.90 & 27.47 & 54.38 & \textbf{29.26} & 1.97 \\ % exp_id: teal50_uniform
55	& KL global (Ours) & \textbf{11.79} & 32.85 & \textbf{63.46} & 28.1 & 1.29 \\ % exp_id: bench_kl50_global
56	& KL uniform & 11.92$\pm$0.07 & \textbf{33.8$\pm$1.2} & 62.9$\pm$0.1 & 28.0$\pm$0.6 & \textbf{2.2$\pm$0.1} \\ % exp_id: bench_kl50_uniform, bench_kl50_uniform_s123, bench_kl50_uniform_s456
57	& BCE (2700 steps)$^\ast$ & 28.13$\pm$0.20 & 27.6$\pm$0.6 & 51.8$\pm$0.6 & 26.1$\pm$0.5 & 2.1$\pm$0.2 \\ % exp_id: bce50_3seed
58	\bottomrule
59	\end{tabular}}
60	\end{table}
61	
62	
63	\subsection{Extended Training Analysis}
64	\label{sec:isocompute}
65	
66	To test whether BCE simply requires more compute, we train it for 2700 steps (2.71$\times$ the KL step budget, approximately equal wall-clock time: $\sim$46 min BCE vs.\ $\sim$45 min KL on RTX PRO 6000).
67	The BCE predictor achieves PPL 28.13$\pm$0.20 (3-seed), still 2.39$\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce50_3seed
68	The difference is systematic, not due to architectural or compute limitations: both predictors use identical architectures and TEAL allocation, yet BCE achieves +7pp oracle F1 (0.613 vs.\ 0.540) with 139\% worse PPL (28.13 vs.\ 11.79). KL's near-random precision (0.51) is consistent with a mask optimized for distributional fidelity rather than magnitude agreement. % exp_id: f1_oracle_analysis, bce_isocompute_s42
69	Coupled training correlates with better output preservation; the target-swap ablation in \S\ref{sec:mask_analysis} confirms that the discovered mask targets, not the coupling mechanism itself, are the proximate driver of inference-stage quality.
70	
71	
72	\subsection{Mask Pattern Analysis}
73	\label{sec:mask_analysis}
74	
75	To understand \emph{what} the KL predictor learns, we compare KL-derived masks against magnitude-based oracle masks (the BCE training targets) at 50\% sparsity on WikiText-2.
76	Per-layer Jaccard similarity averages 32\% at 50\% sparsity (64 samples, 131K tokens), computed per-token (each token's KL and magnitude masks are constructed independently, then Jaccard distances are averaged across tokens): the KL predictor discovers neuron importance patterns that diverge 68\% from activation magnitude, with divergence scaling from 46\% at 30\% to 68\% at 50\% (Figure~\ref{fig:mask_heatmap}).
77	At layer 16, 41\% of neurons fall in disagreement quadrants where KL and magnitude rankings diverge (Appendix~\ref{app:mask_viz}, Figures~\ref{fig:mask_heatmap}--\ref{fig:scatter}).
78	Despite this divergence, KL achieves PPL 11.79 vs.\ BCE's 28.13$\pm$0.20: output-distribution fidelity, not magnitude agreement, produces lower-perplexity masks under global allocation. % exp_id: bench_kl50_global, bce50_3seed, c1_mask_overlap
79	
80	\paragraph{Per-Layer Divergence Structure.}
81	Per-layer Jaccard distance follows a U-shaped pattern (Figure~\ref{fig:mask_heatmap}): at 50\%, middle layers (L14--L17) show lowest divergence ($\sim$0.61), while late layers (L22--L28) peak at $\sim$0.70--0.75. The same structure holds at 30\% (range 0.361--0.600).
82	Late layers are closest to the KL-optimized output distribution, so their backward gradient carries stronger output-sensitivity signal and the predictor deviates most from magnitude ranking there. % exp_id: c1_mask_overlap
83	
84	\paragraph{Target-Swap Ablation: Target Quality vs.\ Gradient Coupling.}
85	To disentangle whether KL's advantage stems from its coupled gradient pathway or from the mask patterns it discovers, we train a standard BCE predictor on KL-derived oracle masks instead of magnitude-based masks (C1 target-swap ablation).
86	Table~\ref{tab:c1} reports results under TEAL uniform allocation at matched sparsity.
87	
88	\begin{table}[t]
89	\centering
90	\caption{Target-swap ablation (C1): BCE on KL-derived masks vs.\ KL predictor (same seed), TEAL uniform. All seeds show max $\Delta$$\leq$1.70pp at 30\%; max $\Delta$$\leq$0.79pp at 50\% (s42). $^\dagger$s42 oracle is from an earlier training run; s123/s456 use matched retrained oracles.}
91	\label{tab:c1}
92	\resizebox{\columnwidth}{!}{
93	\begin{tabular}{lllccccc}
94	\toprule
95	Sparsity & Seed & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
96	\midrule
97	\multirow{6}{*}{30\%}
98	& s42$^\dagger$ & C1 & 9.45 & 40.27 & 67.40 & \textbf{42.30} & \textbf{7.58} \\ % exp_id: c1_ablation_30pct_s42_eval_v2
99	& & KL & \textbf{8.80} & \textbf{40.78} & \textbf{68.59} & 40.6 & 7.35 \\ % exp_id: bench_kl30_uniform
100	& s123 & C1 & 8.84 & 44.71 & \textbf{69.77} & \textbf{39.92} & 6.82 \\ % exp_id: eval_c1_retrain_30pct_s123
101	& & KL & \textbf{8.83} & \textbf{45.31} & 69.38 & 39.4 & \textbf{7.51} \\ % exp_id: kl30_s123_eval
102	& s456 & C1 & 8.82 & 44.71 & \textbf{69.93} & 41.04 & 6.60 \\ % exp_id: eval_c1_retrain_30pct_s456
103	& & KL & \textbf{8.79} & \textbf{45.05} & 68.75 & \textbf{42.0} & \textbf{7.58} \\ % exp_id: kl30_s456_uniform_eval
104	\midrule
105	\multirow{2}{*}{50\%}
106	& s42 & C1 & 11.96 & 32.17 & \textbf{63.14} & 27.79 & \textbf{2.05} \\ % exp_id: c1_bce_kl_targets_teal50u
107	& & KL & 11.96 & \textbf{32.59} & 62.35 & \textbf{27.92} & 1.97 \\ % exp_id: c1_kl_teal50u
108	\bottomrule
109	\end{tabular}}
110	\end{table}
111	
112	At 50\%, C1 matches KL within statistical noise (max $\Delta$$\leq$0.79pp, s42), while magnitude-trained BCE yields PPL 28.13$\pm$0.20 ($2.4\times$ worse; Table~\ref{tab:main}).
113	At 30\%, all three C1 predictors reproduce KL quality within $\pm$1.70pp across downstream tasks (max $\Delta$=1.70pp MMLU, s42); retrained seeds (s123, s456) show tighter agreement ($\leq$1.18pp).
114	These results confirm that KL's coupled gradients discover mask targets that yield lower perplexity and transfer to a simpler objective (BCE): mask quality is the proximate driver of inference-stage quality, while gradient coupling remains necessary at the discovery stage. % exp_id: bce50_3seed, c1_bce_kl_targets_30u, c1_s123
115	
116	\paragraph{Soft-vs-Hard Confound.}
117	C1 changes both gradient coupling and mask representation (hard binary vs.\ soft Gumbel-Sigmoid). However, BCE with Gumbel-Sigmoid relaxation (even without penalty) yields PPL 32.22 (Table~\ref{tab:ablation}), worse than standard hard-target BCE (27.97): softness alone does not explain KL's advantage. % exp_id: bce_gumbel_no_penalty_s42, eval_bce_v3_s42
118	Disentangling target quality from gradient representation remains for future work.
119	
120	\subsection{Ablation Studies}
121	
122	Table~\ref{tab:ablation} isolates the contribution of each design choice at 50\% sparsity.
123	
124	\begin{table}[t]
125	\centering
126	\caption{Ablation at 50\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$, unified benchmark protocol).}
127	\label{tab:ablation}
128	\small
129	\begin{tabular}{lcc}
130	\toprule
131	Configuration & PPL$\downarrow$ & $\Delta$ from Ours \\
132	\midrule
133	\multicolumn{3}{l}{\textit{KL-based variants}} \\
134	Forward KL + Gumbel (Ours) & \textbf{11.79} & --- \\ % exp_id: bench_kl50_global
135	JSD (symmetric) + Gumbel & 12.54 & +0.75 \\ % exp_id: jsd_ablation_s42
136	Reverse KL + Gumbel & 12.80 & +1.01 \\ % exp_id: reverse_kl_ablation_s42
137	Forward KL + STE & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
138	\midrule
139	\multicolumn{3}{l}{\textit{BCE-based variants}} \\
140	BCE (no compensation) & 27.97 & +16.18 \\ % exp_id: eval_bce_v3_s42
141	BCE + Gumbel (no penalty) & 32.22 & +20.43 \\ % exp_id: bce_gumbel_no_penalty_s42
142	BCE + Gumbel + Penalty & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangian_isolation
143	\bottomrule
144	\end{tabular}
145	\end{table}
146	
147	\paragraph{Gumbel vs.\ STE.}
148	Replacing Gumbel-Sigmoid with STE~\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98). % exp_id: ste_baseline_s42
149	
150	\paragraph{Divergence Direction.}
151	Forward KL outperforms JSD (+6.4\%) and reverse KL (+8.6\%), consistent with the SNR analysis (\S\ref{sec:method:gradient}); mode-covering ensures no important neuron is omitted, contrasting with reverse-KL generation~\cite{gu2024minillm}. % exp_id: jsd_ablation_s42, reverse_kl_ablation_s42
152	
153	\paragraph{SPON Contribution.}
154	Adding SPON~\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\% relative; Appendix~\ref{app:spon}). % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42
155	
156	\paragraph{Loss Function Isolation.}
157	Removing the penalty from BCE+Gumbel improves PPL (32.22 vs.\ 38.02), partly due to a sparsity gap (38.3\% training vs.\ 50\% target), but remains $2.7\times$ worse than KL (11.79) and worse than vanilla BCE at matched 50\% sparsity (27.97): Gumbel relaxation does not benefit BCE regardless of sparsity control, and KL's advantage stems from the loss function itself. % exp_id: bce_gumbel_no_penalty_s42, bce_gumbel_lagrangian_isolation, eval_bce_v3_s42
158	The loss effect ($\Delta$PPL=20.43) is $5.1\times$ the relaxation effect ($\Delta$PPL=3.98).
159	
160	\paragraph{Compensation Redundancy.}
161	Adding compensation~\cite{gautam2026fastforward} (+67.2M params) to KL provides no benefit at either sparsity level (PPL 8.97 vs.\ 8.96 at 30\%, identical at 50\%; Appendix~\ref{app:comp_convergence}). Compensation networks are designed for fixed-mask inference (DejaVu/FastForward) and do not transfer to TEAL's dynamic global allocation (TEAL eval PPL 44.54 vs.\ per-token PPL 25.44 for BCE+comp). % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42, bce_comp_staged_s42
162	
163	\paragraph{Hyperparameter Robustness.}
164	Appendices~\ref{app:db_sensitivity}--\ref{app:training_convergence} confirm robustness to predictor capacity ($d_b$, $<$3\%; Appendix~\ref{app:db_sensitivity}), temperature schedule ($<$1.8\%; Appendix~\ref{app:tau_sensitivity}), and training steps (saturated by 800; Appendix~\ref{app:training_convergence}). % exp_id: db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep
165	
166	
167	\subsection{Sparsity Scaling and Regime Analysis}
168	\label{sec:scaling}
169	
170	Figure~\ref{fig:sparsity_sweep} shows PPL as a function of sparsity for the KL predictor under global allocation.
171	
172	\begin{figure}[t]
173	\centering
174	\includegraphics[width=\columnwidth]{fig2_sparsity_sweep.pdf}
175	\caption{Perplexity scaling with sparsity. The KL predictor's advantage grows disproportionately as more neurons are pruned.}
176	\label{fig:sparsity_sweep}
177	\end{figure}
178	
179	The regime curve (Figure~\ref{fig:sparsity_sweep}) is strictly monotonic from PPL 8.17 at 25\% to 11.79 at 50\% (global, seed 42), with KL/Dense degradation ranging from $1.34\times$ to $1.93\times$.
180	At matched points, KL improves over TEAL by 18\% at 30\% and 51\% at 50\%; at 70\%, where TEAL collapses (PPL 100.11), the advantage reaches 82\%. % exp_id: regime_kl25_global, regime_kl50_global, kl_70_global_teal
181	
182	\paragraph{Allocation Behavior Across Sparsity Levels.}
183	Table~\ref{tab:phase} compares global vs.\ uniform allocation at representative sparsity levels, revealing qualitative shifts in preference.
184	
185	\begin{table}[t]
186	\centering
187	\caption{Allocation analysis at key sparsity levels (LLaMA-3.1-8B, PPL and MMLU; full 6-level data with all downstream metrics in Appendix~\ref{app:alloc_full}). $\pm$: 3-seed; others: seed 42. $^\ast$High seed variance (25.3--43.5\%).}
188	\label{tab:phase}
189	\footnotesize
190	\begin{tabular}{llcc}
191	\toprule
192	Sparsity & Allocation & PPL$\downarrow$ & MMLU \\
193	\midrule
194	\multirow{2}{*}{25\%}
195	& Global & \textbf{8.17} & \textbf{46.6} \\ % exp_id: regime_kl25_global
196	& Uniform & 8.23 & 44.0 \\ % exp_id: regime_kl25_uniform
197	\midrule
198	\multirow{2}{*}{30\%}
199	& Global & 8.96$\pm$0.02 & 35.7$\pm$9.5$^\ast$ \\ % exp_id: kl30_3seed_global
200	& Uniform & \textbf{8.81$\pm$0.02} & \textbf{40.7$\pm$1.3} \\ % exp_id: bench_kl30_uniform
201	\midrule
202	\multirow{2}{*}{35\%}
203	& Global & \textbf{9.31} & \textbf{40.4} \\ % exp_id: regime_kl35_global
204	& Uniform & 9.44 & 37.8 \\ % exp_id: regime_kl35_uniform
205	\midrule
206	\multirow{2}{*}{50\%}
207	& Global & \textbf{11.79} & \textbf{28.1$\pm$0.2} \\ % exp_id: multi_seed_kl50_global
208	& Uniform & 11.92$\pm$0.07 & 28.0$\pm$0.6 \\ % exp_id: multi_seed_kl50_uniform
209	\bottomrule
210	\end{tabular}
211	\end{table}
212	
213	The analysis reveals \emph{non-monotonic} allocation preference with three regimes, complementing OWL's~\cite{yin2024owl} finding that non-uniform layerwise budgets improve pruning quality (full 6-level data in Appendix~\ref{app:alloc_full}):
214	
215	\noindent\textbf{Budget-surplus ($\leq$30\%).}
216	At 25\%, PPL differs by only 0.06. At 30\%, uniform achieves PPL 8.81$\pm$0.02 (3-seed) with $7.5\times$ smaller cross-seed MMLU $\sigma$ (1.3pp vs.\ 9.5pp). % exp_id: regime_kl25_global, regime_kl25_uniform, kl30_3seed
217	
218	\noindent\textbf{Budget-constrained (35--40\%).}
219	Global becomes preferable: at 35\%, MMLU 40.4\% vs.\ 37.8\% (+2.6pp); at 40\%, MMLU 38.1\% (Appendix~\ref{app:alloc_full}). % exp_id: regime_kl35_global, regime_kl35_uniform, regime_kl40_global
220	
221	\noindent\textbf{Capacity-limited ($\geq$45\%).}
222	Gap vanishes for reasoning: at 50\%, MMLU collapses to near-random under both strategies (28.1 vs.\ 28.0\%), though global still helps non-reasoning tasks (HellaSwag +2.29pp; Appendix~\ref{app:downstream}). Late-layer starvation persists (Figure~\ref{fig:retention}; Appendix~\ref{app:retention}). % exp_id: multi_seed_kl50_global, multi_seed_kl50_uniform, hellaswag_piqa_kl50_global, hellaswag_piqa_kl50_uniform
223	
224	
225	\paragraph{Cross-Architecture and Scale.}
226	\label{sec:cross_arch}
227	On Mistral-7B-v0.3~\cite{jiang2023mistral}, KL outperforms TEAL on 5 of 6 downstream
228	tasks at 30\% (HellaSwag +8.8pp, ARC +9.0pp, WG +5.6pp, PIQA +3.1pp, MMLU +0.6pp),
229	with PPL 6.77 vs.\ 8.38; GSM8K is the sole reversal (11.1\% vs.\ 15.9\%,
230	Table~\ref{tab:mistral_downstream}); the 50\% capacity cliff also holds cross-architecture (MMLU 26.4\%$\approx$random; Appendix~\ref{app:cross_arch}). % exp_id: mistral_kl30_downstream, mistral_teal30_downstream, mistral_teal50_downstream
231	On Qwen-2.5-14B~\cite{qwen2024qwen25}, KL's PPL advantage generalizes at 30\% ($1.52\times$ dense), but task-level effects diverge: commonsense improves (WG +3.0pp uniform) while factual retrieval (MMLU $-$2.79pp, 3-seed; 63.6\% vs.\ 66.3\%) and reasoning (GSM8K $-$25pp; 32.1$\pm$5.2\% vs.\ 57.1\%, 3-seed) decline (Table~\ref{tab:14b}; actual sparsity: KL 29.6\%, TEAL 26.8\%). Under global allocation, MMLU narrows to $-$8.1pp and GSM8K equalizes (48.8\% vs.\ 49.5\%; \S\ref{sec:scaling}). % exp_id: qwen14b_kl30_uniform_4task, qwen14b_teal30_uniform
232	These reversals are scale-dependent: at 8B all methods collapse to $<$9\% GSM8K (Table~\ref{tab:main}); at 14B, TEAL retains 65\% of dense reasoning while KL retains 37\% ($\sigma$=5.2pp)---forward KL's mass-covering property disrupts narrow reasoning pathways only when base capacity suffices.
233	Per-layer Jaccard variance is $2.4\times$ higher at 14B (std 0.076 vs.\ 0.031) with an early-layer convergence zone (L3--L6) absent in 8B; causal linkage requires layer-wise probing. % exp_id: qwen14b_kl30_uniform_4task, qwen14b_teal30_uniform % exp_id: qwen14b_kl30_s42, qwen14b_teal30_eval, qwen14b_bce30_s42_eval, qwen14b_kl30_uniform_4task, qwen14b_teal30_uniform_4task
234	\paragraph{Inference Efficiency.}
235	\label{sec:overhead}
236	The predictor adds 3.17\,ms (2.7\% overhead, 75.96M params / 0.9\% of base); actual speedup requires sparse kernel support (Appendix~\ref{app:latency}). % exp_id: latency_profiling
237	
238	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "188dfd0d-5093-4ad9-b52a-de82b922e3f6",
  "isSidechain": true,
  "promptId": "a403245c-091e-4e8d-bdc8-72b45d6db8d7",
  "agentId": "a6e16af898b1545df",
  "type": "user",
  "uuid": "5dfd3872-e00d-4908-b59e-8eb17eda2acf",
  "sourceToolAssistantUUID": "188dfd0d-5093-4ad9-b52a-de82b922e3f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T01:36:13.401Z_

Perfect! Now let me search for more context about allocation in the appendix around the Mistral table to see if there's any discussion about the allocation strategy choice for Mistral.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dfd3872-e00d-4908-b59e-8eb17eda2acf",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpt16EjaTmirpP4eQW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "81fb5b8a-ce82-47df-90e3-6fc4a532ed87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0151CDj9p6puRuk5nJTFqYmE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8634,
      "cache_read_input_tokens": 29932,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8634,
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

_source line 18 · 2026-05-20T01:36:14.474Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ci3vrjAnaMjdG8zZm7bcxX`</summary>

```json
{
  "pattern": "Mistral.*allocation|allocation.*Mistral",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "output_mode": "content",
  "context": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81fb5b8a-ce82-47df-90e3-6fc4a532ed87",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxpt16EjaTmirpP4eQW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8a1b4e72-e943-4a0f-9b74-4413254d8e40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0151CDj9p6puRuk5nJTFqYmE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8634,
      "cache_read_input_tokens": 29932,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8634
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 190,
          "cache_read_input_tokens": 29932,
          "cache_creation_input_tokens": 8634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8634,
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

_source line 19 · 2026-05-20T01:36:14.491Z_

<details><summary>↩ Tool result · `toolu_01Ci3vrjAnaMjdG8zZm7bcxX`</summary>

```text
347-
348-\begin{table}[h]
349-\centering
350:\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL\,/\,KL ratio. LLaMA uses global top-$k$; Mistral uses uniform allocation (matched within each architecture).}
351-\label{tab:cross_arch}
352-\small
353-\begin{tabular}{l@{\hspace{4pt}}cc@{\hspace{3pt}}c@{\hspace{6pt}}|@{\hspace{6pt}}cc@{\hspace{3pt}}c}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a1b4e72-e943-4a0f-9b74-4413254d8e40",
  "isSidechain": true,
  "promptId": "a403245c-091e-4e8d-bdc8-72b45d6db8d7",
  "agentId": "a6e16af898b1545df",
  "type": "user",
  "uuid": "684646ca-a6e0-4279-afeb-977d902c8120",
  "sourceToolAssistantUUID": "8a1b4e72-e943-4a0f-9b74-4413254d8e40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-20T01:36:16.365Z_

Excellent! Now let me get the exact content of the Mistral downstream table to see the full context. Let me read lines 369-384 from appendix.tex to get the complete table with caption.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "684646ca-a6e0-4279-afeb-977d902c8120",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxq6gLK74RtKcJzBCzN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "53de2ce4-61e9-4812-a1ca-bad4a4e57688",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016sDcuRRTXPqHPAdoxnnm1B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 359,
      "cache_read_input_tokens": 38566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 359,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 21 · 2026-05-20T01:36:16.921Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y89s3gvsaZMHQueUxwWtc6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": 369,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53de2ce4-61e9-4812-a1ca-bad4a4e57688",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxq6gLK74RtKcJzBCzN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cc6f1671-d934-42a0-b854-ef4f4c5c209e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016sDcuRRTXPqHPAdoxnnm1B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 359,
      "cache_read_input_tokens": 38566,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 359
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 169,
          "cache_read_input_tokens": 38566,
          "cache_creation_input_tokens": 359,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 359,
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

_source line 22 · 2026-05-20T01:36:16.931Z_

<details><summary>↩ Tool result · `toolu_01Y89s3gvsaZMHQueUxwWtc6`</summary>

```text
369	\begin{table}[h]
370	\centering
371	\caption{Mistral-7B-v0.3 downstream evaluation at 30\% sparsity (seed 42). KL outperforms TEAL on 5 of 6 tasks (largest: ARC-c +9.0pp, HellaSwag +8.8pp); GSM8K is the sole reversal.}
372	\label{tab:mistral_downstream}
373	\small
374	\resizebox{\columnwidth}{!}{
375	\begin{tabular}{lccccccc}
376	\toprule
377	Method & PPL$\downarrow$ & ARC-c & WG & HS & PIQA & MMLU & GSM8K \\
378	\midrule
379	Dense & 5.52 & 60.2 & 78.7 & 83.2 & 81.9 & 62.4 & 36.5 \\ % exp_id: lm_eval_mistral_dense, mistral_dense_hellaswag_piqa
380	KL 30\% & \textbf{6.77} & \textbf{50.1} & \textbf{69.1} & \textbf{68.9} & \textbf{75.2} & \textbf{44.0} & 11.1 \\ % exp_id: mistral_kl30_downstream
381	TEAL 30\% & 8.38 & 41.1 & 63.5 & 60.1 & 72.1 & 43.5 & \textbf{15.9} \\ % exp_id: mistral_teal30_downstream
382	\bottomrule
383	\end{tabular}}
384	\end{table}
385	
386	
387	\section{SPON Orthogonality}
388	\label{app:spon}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc6f1671-d934-42a0-b854-ef4f4c5c209e",
  "isSidechain": true,
  "promptId": "a403245c-091e-4e8d-bdc8-72b45d6db8d7",
  "agentId": "a6e16af898b1545df",
  "type": "user",
  "uuid": "157f12fa-ed9d-4d3d-b0e4-d80f52396480",
  "sourceToolAssistantUUID": "cc6f1671-d934-42a0-b854-ef4f4c5c209e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T01:36:18.596Z_

Perfect! Now let me search for any text near the Mistral table section that discusses allocation strategy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "157f12fa-ed9d-4d3d-b0e4-d80f52396480",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxqGxDWrZCRkCLE7UJx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "af742ffc-e97f-4a1b-956c-f2e029bc7c55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BnhBSMxrJuZxKpDSLzmdLr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 38925,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 672,
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

_source line 24 · 2026-05-20T01:36:18.915Z_

<details open><summary>🔧 Tool call — Read · `toolu_011x2Yv1bGGXDbLtN9X9yDau`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex",
  "offset": 343,
  "limit": 45
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af742ffc-e97f-4a1b-956c-f2e029bc7c55",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxqGxDWrZCRkCLE7UJx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f6308348-8b28-4a70-a0ea-7b2cbb4b0958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BnhBSMxrJuZxKpDSLzmdLr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 38925,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 672
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 145,
          "cache_read_input_tokens": 38925,
          "cache_creation_input_tokens": 672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 672,
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

_source line 25 · 2026-05-20T01:36:18.952Z_

<details><summary>↩ Tool result · `toolu_011x2Yv1bGGXDbLtN9X9yDau`</summary>

```text
343	\section{Cross-Architecture Comparison}
344	\label{app:cross_arch}
345	
346	Table~\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).
347	
348	\begin{table}[h]
349	\centering
350	\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL\,/\,KL ratio. LLaMA uses global top-$k$; Mistral uses uniform allocation (matched within each architecture).}
351	\label{tab:cross_arch}
352	\small
353	\begin{tabular}{l@{\hspace{4pt}}cc@{\hspace{3pt}}c@{\hspace{6pt}}|@{\hspace{6pt}}cc@{\hspace{3pt}}c}
354	\toprule
355	 & \multicolumn{3}{c}{Mistral-7B} & \multicolumn{3}{c}{LLaMA-8B} \\
356	 & KL & TEAL & Adv & KL & TEAL & Adv \\
357	\midrule
358	30\% & \textbf{6.77} & 8.38 & 1.24$\times$ & \textbf{8.96} & 10.97 & 1.22$\times$ \\ % exp_id: kl_30_mistral, teal_30_mistral, kl30_3seed_global
359	50\% & \textbf{8.65} & 18.31 & 2.12$\times$ & \textbf{11.79} & 23.31 & 1.98$\times$ \\ % exp_id: kl_50_mistral, teal_50_mistral
360	70\% & \textbf{13.33} & 61.72 & 4.63$\times$ & \textbf{17.91} & 100.11 & 5.59$\times$ \\ % exp_id: kl_70_mistral, teal_70_mistral
361	\bottomrule
362	\end{tabular}
363	\end{table}
364	
365	The KL PPL advantage ratio is consistent across architectures (within 8\% at $\leq$50\% sparsity).
366	Table~\ref{tab:mistral_downstream} reports downstream task accuracy at 30\% sparsity on Mistral-7B-v0.3, confirming that KL's downstream advantage generalizes on 5 of 6 tasks;
367	GSM8K is the sole reversal.
368	
369	\begin{table}[h]
370	\centering
371	\caption{Mistral-7B-v0.3 downstream evaluation at 30\% sparsity (seed 42). KL outperforms TEAL on 5 of 6 tasks (largest: ARC-c +9.0pp, HellaSwag +8.8pp); GSM8K is the sole reversal.}
372	\label{tab:mistral_downstream}
373	\small
374	\resizebox{\columnwidth}{!}{
375	\begin{tabular}{lccccccc}
376	\toprule
377	Method & PPL$\downarrow$ & ARC-c & WG & HS & PIQA & MMLU & GSM8K \\
378	\midrule
379	Dense & 5.52 & 60.2 & 78.7 & 83.2 & 81.9 & 62.4 & 36.5 \\ % exp_id: lm_eval_mistral_dense, mistral_dense_hellaswag_piqa
380	KL 30\% & \textbf{6.77} & \textbf{50.1} & \textbf{69.1} & \textbf{68.9} & \textbf{75.2} & \textbf{44.0} & 11.1 \\ % exp_id: mistral_kl30_downstream
381	TEAL 30\% & 8.38 & 41.1 & 63.5 & 60.1 & 72.1 & 43.5 & \textbf{15.9} \\ % exp_id: mistral_teal30_downstream
382	\bottomrule
383	\end{tabular}}
384	\end{table}
385	
386	
387	\section{SPON Orthogonality}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6308348-8b28-4a70-a0ea-7b2cbb4b0958",
  "isSidechain": true,
  "promptId": "a403245c-091e-4e8d-bdc8-72b45d6db8d7",
  "agentId": "a6e16af898b1545df",
  "type": "user",
  "uuid": "2a6203f6-4774-4480-b7cc-c2ec7c467123",
  "sourceToolAssistantUUID": "f6308348-8b28-4a70-a0ea-7b2cbb4b0958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-20T01:36:20.675Z_

Perfect! Now let me also check the experiments.tex around line 230 for the full context of the reference to tab:mistral_downstream.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a6203f6-4774-4480-b7cc-c2ec7c467123",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxqRq1pdH9YF67SGmbK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "42c4dd25-0ea9-4d60-b4a6-ccca963a72bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013eE4AqpdPBzSToQ4Peg81o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 1341,
      "cache_read_input_tokens": 39597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1341,
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

_source line 27 · 2026-05-20T01:36:21.585Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EqRQUdr2UsmqJfxfRQures`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "offset": 225,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42c4dd25-0ea9-4d60-b4a6-ccca963a72bc",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxqRq1pdH9YF67SGmbK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c60f823-59df-44d4-8a63-cd0b1808c6ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013eE4AqpdPBzSToQ4Peg81o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 1341,
      "cache_read_input_tokens": 39597,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1341
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 154,
          "cache_read_input_tokens": 39597,
          "cache_creation_input_tokens": 1341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1341,
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

_source line 28 · 2026-05-20T01:36:21.596Z_

<details><summary>↩ Tool result · `toolu_01EqRQUdr2UsmqJfxfRQures`</summary>

```text
225	\paragraph{Cross-Architecture and Scale.}
226	\label{sec:cross_arch}
227	On Mistral-7B-v0.3~\cite{jiang2023mistral}, KL outperforms TEAL on 5 of 6 downstream
228	tasks at 30\% (HellaSwag +8.8pp, ARC +9.0pp, WG +5.6pp, PIQA +3.1pp, MMLU +0.6pp),
229	with PPL 6.77 vs.\ 8.38; GSM8K is the sole reversal (11.1\% vs.\ 15.9\%,
230	Table~\ref{tab:mistral_downstream}); the 50\% capacity cliff also holds cross-architecture (MMLU 26.4\%$\approx$random; Appendix~\ref{app:cross_arch}). % exp_id: mistral_kl30_downstream, mistral_teal30_downstream, mistral_teal50_downstream
231	On Qwen-2.5-14B~\cite{qwen2024qwen25}, KL's PPL advantage generalizes at 30\% ($1.52\times$ dense), but task-level effects diverge: commonsense improves (WG +3.0pp uniform) while factual retrieval (MMLU $-$2.79pp, 3-seed; 63.6\% vs.\ 66.3\%) and reasoning (GSM8K $-$25pp; 32.1$\pm$5.2\% vs.\ 57.1\%, 3-seed) decline (Table~\ref{tab:14b}; actual sparsity: KL 29.6\%, TEAL 26.8\%). Under global allocation, MMLU narrows to $-$8.1pp and GSM8K equalizes (48.8\% vs.\ 49.5\%; \S\ref{sec:scaling}). % exp_id: qwen14b_kl30_uniform_4task, qwen14b_teal30_uniform
232	These reversals are scale-dependent: at 8B all methods collapse to $<$9\% GSM8K (Table~\ref{tab:main}); at 14B, TEAL retains 65\% of dense reasoning while KL retains 37\% ($\sigma$=5.2pp)---forward KL's mass-covering property disrupts narrow reasoning pathways only when base capacity suffices.
233	Per-layer Jaccard variance is $2.4\times$ higher at 14B (std 0.076 vs.\ 0.031) with an early-layer convergence zone (L3--L6) absent in 8B; causal linkage requires layer-wise probing. % exp_id: qwen14b_kl30_uniform_4task, qwen14b_teal30_uniform % exp_id: qwen14b_kl30_s42, qwen14b_teal30_eval, qwen14b_bce30_s42_eval, qwen14b_kl30_uniform_4task, qwen14b_teal30_uniform_4task
234	\paragraph{Inference Efficiency.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c60f823-59df-44d4-8a63-cd0b1808c6ce",
  "isSidechain": true,
  "promptId": "a403245c-091e-4e8d-bdc8-72b45d6db8d7",
  "agentId": "a6e16af898b1545df",
  "type": "user",
  "uuid": "dc071bf1-4a41-4db0-9969-e7f75cbf9d3b",
  "sourceToolAssistantUUID": "4c60f823-59df-44d4-8a63-cd0b1808c6ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-20T01:36:29.515Z_

Excellent! Now I have all the information needed. Let me compile the complete findings.

## Summary

I found the Mistral downstream table (tab:mistral_downstream) and related references. Here are the exact details:

### 1. **Mistral Downstream Table (tab:mistral_downstream) in appendix.tex**
**Location:** Lines 369-384 in `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex`

**Allocation Strategy:** **UNIFORM allocation** (not global)

**Caption (exact text, line 371):**
> "Mistral-7B-v0.3 downstream evaluation at 30\% sparsity (seed 42). KL outperforms TEAL on 5 of 6 tasks (largest: ARC-c +9.0pp, HellaSwag +8.8pp); GSM8K is the sole reversal."

**Table Content (lines 375-383):**
- Headers: Method | PPL↓ | ARC-c | WG | HS | PIQA | MMLU | GSM8K
- Dense: 5.52 | 60.2 | 78.7 | 83.2 | 81.9 | 62.4 | 36.5
- KL 30%: **6.77** | **50.1** | **69.1** | **68.9** | **75.2** | **44.0** | 11.1
- TEAL 30%: 8.38 | 41.1 | 63.5 | 60.1 | 72.1 | 43.5 | **15.9**

### 2. **Allocation Strategy Context**
**From tab:cross_arch caption (line 350 in appendix.tex):**
> "Cross-architecture comparison (WikiText-2 PPL↓). Adv = TEAL/KL ratio. LLaMA uses global top-$k$; **Mistral uses uniform allocation (matched within each architecture).**"

This is explicitly stated in the cross-architecture table caption that precedes the downstream table.

### 3. **Reference in experiments.tex (Line 230)**
**Exact line in experiments.tex:**
> "Table~\ref{tab:mistral_downstream}); the 50\% capacity cliff also holds cross-architecture (MMLU 26.4\%≈random; Appendix~\ref{app:cross_arch})."

**Full context (lines 227-230):**
> "On Mistral-7B-v0.3, KL outperforms TEAL on 5 of 6 downstream tasks at 30\% (HellaSwag +8.8pp, ARC +9.0pp, WG +5.6pp, PIQA +3.1pp, MMLU +0.6pp), with PPL 6.77 vs. 8.38; GSM8K is the sole reversal (11.1\% vs. 15.9\%, Table~\ref{tab:mistral_downstream})"

### 4. **Key Finding**
The Mistral downstream table uses **uniform allocation**, not global top-k allocation. This is intentionally different from the LLaMA results (which use global allocation), as documented in the cross-architecture comparison table caption. The allocation strategy is explicitly matched within each architecture for fair comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc071bf1-4a41-4db0-9969-e7f75cbf9d3b",
  "isSidechain": true,
  "agentId": "a6e16af898b1545df",
  "requestId": "req_011CbCxqctXdS3jYHgfH73Ek",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7477e3a-e185-4ab5-9109-321540f1f78c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/reviewer_ab8e9749",
  "sessionId": "57ffcbd9-7387-4356-b515-f43c06042a1a",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "majestic-floating-dongarra",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Q9c7Ux5m1DFHCVTi5HdqFD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 961,
      "cache_read_input_tokens": 40938,
      "output_tokens": 831,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 961
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 831,
          "cache_read_input_tokens": 40938,
          "cache_creation_input_tokens": 961,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 961,
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
