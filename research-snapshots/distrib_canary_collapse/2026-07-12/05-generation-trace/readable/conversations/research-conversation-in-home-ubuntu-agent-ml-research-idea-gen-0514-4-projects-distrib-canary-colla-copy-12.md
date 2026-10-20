# Research conversation: In /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex, find the MM

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8da0bb5ae83c9d55.jsonl`
- **Structured JSON:** [`50f5ec7638965227f407.json`](../../sessions/50/50f5ec7638965227f407.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-24T21:08:02.384Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex, find the MMCT Algorithm pseudocode (Algorithm 1). Search for "begin{algorithm}" or "MMCT" or "Algorithm" in that file. Return the full algorithm environment with all surrounding text (the section header, any intro text, and the complete \begin{algorithm}...\end{algorithm} block). Also note the line numbers and the section label (e.g., \label{app:mmct}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "28ed9fd7-28b9-4f8b-a3f7-ce466223640d",
  "agentId": "a8da0bb5ae83c9d55",
  "type": "user",
  "uuid": "8beed188-7395-4a2c-b539-3b43663734fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "2e2dd7aa-a3cc-4018-897b-841737c0e4e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "cached-giggling-dusk"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T21:08:03.690Z_

I'll search for the MMCT Algorithm pseudocode in the appendix file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8beed188-7395-4a2c-b539-3b43663734fa",
  "isSidechain": true,
  "agentId": "a8da0bb5ae83c9d55",
  "requestId": "req_011CbN5RTSBZ6o98FkjwZiVX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff4a8b8a-f09d-4770-aeba-4502fdfd55a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "2e2dd7aa-a3cc-4018-897b-841737c0e4e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "cached-giggling-dusk",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GvRj88F3sevnKBhzg1gxak",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33365,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 33365,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-24T21:08:03.903Z_

<details open><summary>🔧 Tool call — Read · `toolu_0114nzqWmQEZ6PDHoBp3wVkt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff4a8b8a-f09d-4770-aeba-4502fdfd55a7",
  "isSidechain": true,
  "agentId": "a8da0bb5ae83c9d55",
  "requestId": "req_011CbN5RTSBZ6o98FkjwZiVX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3043460f-68a2-4769-9d94-b84015bc657c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "2e2dd7aa-a3cc-4018-897b-841737c0e4e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "cached-giggling-dusk",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GvRj88F3sevnKBhzg1gxak",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33365,
      "cache_read_input_tokens": 0,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 33365
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 109,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 33365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 33365,
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

_source line 4 · 2026-05-24T21:08:04.205Z_

<details><summary>↩ Tool result · `toolu_0114nzqWmQEZ6PDHoBp3wVkt`</summary>

```text
1	\appendix
2	
3	\section{Training Details and Metric Drift}
4	\label{app:training_details}
5	\label{app:drift}
6	
7	\paragraph{Hyperparameters.}
8	Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
9	Generation uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.
10	Canary metrics: token entropy $H(p_\theta | \text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.
11	Additional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.
12	
13	\paragraph{Metric drift.}
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
19	\label{tab:drift_summary}
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{lccccc}
22	\toprule
23	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
24	\midrule
25	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
26	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
27	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
28	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
29	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
30	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	
35	
36	\section{Distinct-3 Results}
37	\label{app:distinct3}
38	
39	Table~\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.
40	Distinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\pm}0.9\%$ at $\alpha{=}0.25$) but attenuates at higher levels ($-30.5\%$ at $\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \S\ref{sec:discussion}.
41	
42	\begin{table}[h]
43	\centering
44	\small
45	\caption{Distinct-3 drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.75$: 3-seed mean${\pm}$std; $\alpha{=}1.0$: 4-seed mean${\pm}$std; $\alpha{=}0.50$: single seed.}
46	\label{tab:distinct3_drift}
47	\begin{tabular}{lc}
48	\toprule
49	$\alpha$ & Distinct-3 drift (\%) \\
50	\midrule
51	0.00 & $-4.4{\pm}0.5$ \\
52	0.25 & $-58.9{\pm}0.9$ \\
53	0.50 & $-52.4$ \\
54	0.75 & $-38.6{\pm}1.3$ \\
55	1.00 & $-30.5{\pm}4.0$ \\
56	\bottomrule
57	\end{tabular}
58	\end{table}
59	
60	Distinct-3 exhibits higher lag instability than distinct-1/2 (bimodal lag distribution, std${>}1.5$ vs.\ ${<}0.5$ generations), reflecting its lower signal-to-noise ratio at 512-token generation length.
61	
62	
63	\section{Observation Window Sensitivity}
64	\label{app:window_sensitivity}
65	
66	Consensus classification stabilizes at $T_{\min}{\geq}5$ (Table~\ref{tab:window_sensitivity}): all six effect-size reference pairs reach $K{\geq}4/5$ agreement at every window from $T_{\min}{=}5$ through $T_{\min}{=}10$.
67	
68	\begin{table}[h]
69	\centering
70	\small
71	\caption{Observation window sensitivity for Tier~3 consensus ($K{\geq}4/5$) at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\to$downstream pairs (out of 8 validated) reaching $K{\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \S\ref{sec:method}). Consensus stabilizes at $T_{\min}{\geq}5$; TY stabilizes at $T_{\min}{\geq}6$.}
72	\label{tab:window_sensitivity}
73	\resizebox{\columnwidth}{!}{%
74	\begin{tabular}{lccccccccc}
75	\toprule
76	& \multicolumn{8}{c}{Minimum observation window $T_{\min}$} \\
77	\cmidrule(lr){2-9}
78	& 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
79	\midrule
80	Tier~3 pairs (/8)    & $\dagger$ & $\dagger$ & 6 & 6 & 6 & 6 & 6 & 6 \\
81	TY pairs$^\S$ (/6)   & $\dagger$ & $\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\
82	Stable               & ---       & ---       & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
83	\bottomrule
84	\multicolumn{9}{l}{\footnotesize $\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).} \\
85	\multicolumn{9}{l}{\footnotesize $^\S$~TY directional assignment under verification.}
86	\end{tabular}}
87	\end{table}
88	
89	\section{Robustness Checks}
90	\label{app:robustness}
91	
92	\paragraph{Permutation count and FDR sensitivity.}
93	PermG $p$-values are stable between 5{,}000 and 10{,}000 permutations (max $|\Delta p|{=}0.010$, 0/24 significance flips at $\alpha{=}0.75$).
94	Treatment/null separation is robust to FDR threshold choice: at $q{=}0.05$, 4/36 null pairs vs.\ 19/24 treatment pairs reach significance; at $q{=}0.10$, null rejections rise to 8/36.
95	At the onset boundary ($\alpha{=}0.45$), minimum FDR-corrected $p$-values ($0.059$--$0.091$) are consistent with a continuous power transition rather than binary absence of signal.
96	
97	\section{Systematic Robustness Analysis}
98	\label{app:spec_curve}
99	
100	We construct 1{,}160 specifications from 13 contamination levels, 4~seeds, and 8 canary$\to$downstream pairs (all PermG, $n_\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).
101	
102	\begin{table}[h]
103	\centering
104	\small
105	\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\to$onset jump is robust across specifications: 0\% significance rate through $\alpha{=}0.45$, rising to 75\% at $\alpha{=}0.50$.}
106	\label{tab:spec_curve}
107	\begin{tabular}{lc}
108	\toprule
109	Metric & Value \\
110	\midrule
111	Total specifications & 1{,}160 \\
112	Significant (FDR $q{<}0.05$) & 536 (46.2\%) \\
113	\midrule
114	\emph{By regime} & \\
115	\quad Blind ($\alpha \leq 0.45$) & 0\% \\
116	\quad Onset ($\alpha{=}0.50$) & 75\% \\
117	\quad Detection ($\alpha \geq 0.75$) & 62--75\% \\
118	\bottomrule
119	\end{tabular}
120	\end{table}
121	
122	The blind$\to$onset jump holds across the vast majority of specifications (Figure~\ref{fig:spec_curve}).
123	
124	
125	\section{Transfer Entropy Analysis}
126	\label{app:transfer_entropy}
127	\phantomsection\label{app:te_mi}
128	
129	Transfer entropy (TE; \citealp{schreiber2000measuring}; 3-bin discretization, $n{=}5{,}000$ permutations) yields 0/192 BH-corrected significant pairs across all conditions, confirming that nonparametric information-theoretic methods lack power at $T{=}11$.
130	A KNN-based TE estimator ($k{=}5$) shows forward-dominant TE fraction increasing monotonically with $\alpha$ (4/8 at $\alpha{=}0.25$ to 8/8 at $\alpha{=}1.0$), but this does not reach statistical significance after FDR correction.
131	
132	\section{Change-Point Detection Analysis}
133	\label{app:change_point}
134	
135	Max-split change-point tests ($n{=}5{,}000$ bootstrap) yield 66.7\% FPR under null control (12/18, $\alpha{=}0.00$), precluding use as a standalone detector.
136	However, the temporal ordering of change-points reverses between null and treatment: under null, downstream metrics break first (gen~2) before canary (gen~4--8); under treatment ($\alpha{\geq}0.75$), canary breaks first (gen~1) before downstream (gen~2--4).
137	This ordering reversal shifts monotonically with $\alpha$, consistent with the Granger-precedence analysis.
138	
139	
140	\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}
141	\label{app:csmp}
142	
143	CUSUM sequential testing~\citep{page1954continuous} calibrated against $\alpha{=}0.0$ null control (FAR${=}$0\%) produces identical alarm times as a simple $2\sigma$ threshold at all tested operating points: both trigger at generation~1 for $\alpha{\geq}0.50$.
144	The equivalence arises because the generation-0$\to$1 entropy drop ($|\Delta x|{>}0.7$) greatly exceeds null variability ($\sigma_0{\approx}0.03$); CUSUM's cumulative memory provides no advantage when the initial shift dominates.
145	
146	\section{Background and Notation}
147	\label{app:background}
148	\label{sec:background}
149	
150	This section establishes the formal setup and notation used throughout the paper.
151	
152	\paragraph{Iterative training loop.}
153	Let $M_0$ denote a pretrained language model and $\mathcal{D}_\text{real}$ a fixed corpus of human-written text.
154	At each generation $t \geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\mathcal{D}_\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data:
155	\begin{equation}
156	    \mathcal{D}_\text{train}^{(t)} = \alpha \cdot \mathcal{D}_\text{synth}^{(t-1)} \;+\; (1{-}\alpha) \cdot \mathcal{D}_\text{real}, \quad \alpha \in [0, 1].
157	    \label{eq:mixing}
158	\end{equation}
159	At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}.
160	
161	\paragraph{Metric families.}
162	\emph{Canary metrics}: token entropy ($H(p_\theta | \text{context})$ on held-out samples) and expected calibration error (ECE).
163	\emph{Downstream metrics}: distinct-$n$ ($n \in \{1, 2, 3\}$)~\citep{li2016diversity} and perplexity.
164	Each metric produces a time series of $T{+}1$ observations.
165	
166	\paragraph{Lead-lag testing.}
167	Given canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.
168	We employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\citep{shojaie2022granger}, and Toda--Yamamoto Granger causality~\citep{toda1995statistical}.
169	
170	\section{MMCT Algorithm}
171	\label{app:mmct}
172	
173	Algorithm~\ref{alg:mmct} describes the Multi-Method Consensus Test (MMCT) introduced in \S\ref{sec:mmct}.
174	
175	\begin{algorithm}[h]
176	\caption{Multi-Method Consensus Test (MMCT)}
177	\label{alg:mmct}
178	\begin{algorithmic}[1]
179	\Require Time series pair $(X, Y)$; methods $\{m_1, \ldots, m_K\}$ ($K{=}5$); null-control data $\mathcal{N}$ (from $\alpha{=}0.0$); tolerance $\epsilon{=}0.01$
180	\Ensure $p$-value, consensus level $\hat{K}$
181	\For{each method $m_k$}
182	    \State Compute empirical FPR: $\widehat{\mathrm{FPR}}_k \gets$ fraction of null-control pairs where $m_k$ rejects $H_0$
183	    \State Compute weight: $w_k \gets 1 / \max(\widehat{\mathrm{FPR}}_k,\; \epsilon)$
184	    \State Apply $m_k$ to $(X, Y)$: $d_k \gets \mathbf{1}[m_k \text{ rejects } H_0]$
185	\EndFor
186	\State Weighted consensus: $W(X {\to} Y) \gets \sum_{k} w_k \, d_k \;/\; \sum_{k} w_k$
187	\State Build empirical null distribution of $W$ from all null-control pairs in $\mathcal{N}$
188	\State Compute $p$-value from empirical null: $p \gets \Pr_{\mathcal{N}}(W \geq W_{\mathrm{obs}})$
189	\State Consensus level: $\hat{K} \gets \sum_{k} d_k$
190	\State \Return $p$, $\hat{K}$
191	\end{algorithmic}
192	\end{algorithm}
193	
194	\paragraph{Design rationale.}
195	FPR-inverse weighting penalizes methods with high false positive rates on null-control data: naive cross-correlation (FPR${=}94.4\%$) receives weight $w{=}1.06$, while PermG (FPR${=}7.4\%$, the lowest among all five methods) receives $w{=}13.5$.
196	The empirical null distribution avoids parametric assumptions that are unreliable for short ($T{=}5$--$20$), non-stationary series typical of iterative training.
197	MMCT is a consensus testing protocol, not a novel statistical method; its value lies in systematic method comparison and the identification of method-dependent conclusions.
198	
199	
200	\section{Methodological Comparison Table}
201	\label{app:method_comparison}
202	
203	Table~\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \S\ref{sec:method}.
204	No prior work combines all six dimensions.
205	
206	\begin{table}[h]
207	\centering
208	\small
209	\caption{Methodological comparison of canary and monitoring analyses. \checkmark\ = present, $\times$ = absent, $\circ$ = partial (${\leq}2$ levels or limited replication). Diff.\ = differencing/stationarity controls. Multi-M.\ = ${\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\alpha$. Seeds = ${\geq}3$ independent seeds. Arch.\ = ${\geq}2$ architecturally distinct model families.}
210	\label{tab:method-comparison}
211	\resizebox{\columnwidth}{!}{%
212	\begin{tabular}{lccccccl}
213	\toprule
214	Work & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\
215	\midrule
216	\citet{shumailov2024curse}     & $\times$   & $\times$   & $\times$   & $\circ$    & \checkmark & \checkmark & PPL \\
217	\citet{du2025scales}           & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & $\times$   & ECE, Acc, Dist-$n$ \\
218	\citet{gambetta2024surplexity} & $\times$   & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & Surplexity, Ent \\
219	SIGMA~\citep{sigma2026spectral} & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & Spectral \\
220	DCES~\citep{dces2026counter}    & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & \checkmark & ECE, Ent, PPL \\
221	\midrule
222	\textbf{Ours}                  & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & Ent, ECE, PPL, Dist-$n$ \\
223	\bottomrule
224	\end{tabular}%
225	}
226	\end{table}
227	
228	\section{Extended Discussion}
229	\label{app:extended_discussion}
230	
231	\paragraph{Calibration scope.}
232	All calibration results are specific to our setup (Pythia-410M, WikiText-103, $T{=}10$).
233	On C4 at $\alpha{=}0.50$, PermG reverse reaches 7/8 (seed-dependent: s43 1/8), indicating directional asymmetry should be verified per domain.
234	Token entropy ($H(p_\theta|\text{context})$ on held-out data) and perplexity ($\exp(H_\text{cross})$ on generated text) co-move synchronously, explaining why first-differencing eliminates canary$\to$perplexity but preserves canary$\to$diversity.
235	
236	\paragraph{Scale verification (Pythia-1.4B).}
237	\label{app:scale_14b}
238	
239	\begin{table}[h]
240	\centering
241	\small
242	\caption{Pythia-1.4B phase-diagram cells (fp32, PermG forward, 6-pair basis excl.\ MAUVE).}
243	\label{tab:14b_phase}
244	\begin{tabular}{lcccc}
245	\toprule
246	$\alpha$ & \multicolumn{2}{c}{$T{=}10$} & \multicolumn{2}{c}{$T{=}15$} \\
247	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
248	         & s42 & s44 & s42 & s43 \\
249	\midrule
250	0.45 & 0/6 & 0/6 & 3/6 & 5/6 \\
251	0.50 & 4/6 & 6/6 & 3/6 & 3/6 \\
252	0.60 & 4/6 & 6/6 & 6/6 & 6/6 \\
253	0.75 & 5/6 & 6/6 & 6/6 & 6/6 \\
254	\bottomrule
255	\end{tabular}
256	\end{table}
257	
258	Phase-diagram structure is qualitatively preserved at 1.4B (Table~\ref{tab:14b_phase}; Figure~\ref{fig:14b_phase}): detection boundary at $\alpha_c{\approx}0.50$, cross-$T$ improvement at 3/4 $\alpha$ values ($\alpha{=}0.45$: $0/6{\to}5/6$).
259	The 410M sync-dip does not reproduce at 1.4B (4/6 at $\alpha{=}0.60$, $T{=}10$).
260	Directional asymmetry is seed-specific (s42 reverse 0/6 across all conditions; s43 reverse 6/6 at $\alpha{\geq}0.60$).
261	
262	\begin{figure}[h]
263	\centering
264	\includegraphics[width=\columnwidth]{figures/fig_14b_phase.pdf}
265	\caption{Pythia-1.4B phase diagram (PermG forward, 6-pair basis). Detection boundary ($\alpha_c \approx 0.50$) is consistent with 410M.}
266	\label{fig:14b_phase}
267	\end{figure}
268	
269	
270	\section{Per-Method Dose-Response Profiles}
271	\label{app:dose_response}
272	
273	Table~\ref{tab:dose_response_full} reports FDR significance counts (/8 validated pairs) for all five detection methods across 12 contamination levels (seed~42, Pythia-410M, WikiText, fp32).
274	PermG exhibits a sharp 0$\to$6 jump at $\alpha{=}0.50$ with a return to 0 at $\alpha{=}0.55$--$0.60$ (non-monotonic dip), while other methods show diffuse profiles: naive cross-correlation saturates at 7--8/8 across all levels including the null, and Toda--Yamamoto fluctuates without a clear onset.
275	
276	\begin{table}[h]
277	\centering
278	\small
279	\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}
280	\label{tab:dose_response_full}
281	\resizebox{\columnwidth}{!}{%
282	\begin{tabular}{lccccc}
283	\toprule
284	$\alpha$ & Naive & Diff.\ XCorr & Threshold & PermG & TY$^\S$ \\
285	\midrule
286	0.00 & 8 & 4 & 3 & \textbf{0} & 1 \\
287	0.10 & 7 & 6 & 0 & \textbf{0} & 0 \\
288	0.25 & 8 & 3 & 0 & \textbf{0} & 2 \\
289	0.30 & 8 & 4 & 0 & \textbf{0} & 3 \\
290	0.35 & 8 & 4 & 0 & \textbf{0} & 1 \\
291	0.40 & 8 & 3 & 0 & \textbf{0} & 4 \\
292	0.45 & 8 & 6 & 0 & \textbf{0} & 1 \\
293	0.50 & 8 & 7 & 4 & \textbf{6} & 3 \\
294	0.55 & 8 & 8 & 0 & \textbf{0} & 1 \\
295	0.60 & 8 & 6 & 0 & \textbf{0} & 0 \\
296	0.75 & 7 & 6 & 0 & \textbf{6} & 3 \\
297	1.00 & 8 & 6 & 2 & \textbf{6} & 1 \\
298	\bottomrule
299	\multicolumn{6}{l}{\footnotesize $^\S$TY directional assignment under verification; column retained for completeness.} \\
300	\end{tabular}}
301	\end{table}
302	
303	PermG's dose-response profile most cleanly separates detection regimes: 0/8 at null, sharp 0$\to$6 onset at $\alpha{=}0.50$, non-monotonic dip at $\alpha{=}0.55$--$0.60$.
304	Naive monitoring baselines (PPL-slope, variance-threshold) fire at $\alpha{=}0.0$ (FPR 67--100\%) because fine-tuning drift is indistinguishable from contamination without directional testing.
305	
306	
307	\section{PermG Power Analysis}
308	\label{app:power_analysis}
309	
310	We simulate PermG power under a bivariate DGP with linear coupling $\beta$ ($T \in \{6,\ldots,20\}$, 100 replications, 5{,}000 permutations, BH FDR $q{=}0.05$).
311	At $T{=}10$, $\beta_{50}{=}2.0$ (50\% power requires strong coupling); at $T{=}20$, $\beta_{50}$ drops to 0.9 (Table~\ref{tab:beta50}).
312	Power grows faster than $\sqrt{T}$, so the $\sqrt{T}$ formula in \S\ref{sec:theory} is a conservative lower bound.
313	FPR under FDR correction remains ${\leq}2\%$ across all $T$.
314	
315	\begin{table}[h]
316	\centering
317	\small
318	\caption{PermG power analysis: $\beta_{50}$ (coupling for 50\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). Dashes: $<$50\% power not reached within $\beta \leq 2.0$.}
319	\label{tab:beta50}
320	\begin{tabular}{lcccc}
321	\toprule
322	$T$ & $\beta_{50}$ & $\beta_{50} \cdot \sqrt{T}$ & FPR (raw) & FPR (FDR) \\
323	\midrule
324	6  & ---  & ---  & 1\% & 0\% \\
325	8  & ---  & ---  & 6\% & 2\% \\
326	10 & 2.0  & 6.32 & 9\% & 2\% \\
327	15 & 1.2  & 4.65 & 6\% & 2\% \\
328	20 & 0.9  & 4.02 & 5\% & 1\% \\
329	\bottomrule
330	\end{tabular}
331	\end{table}
332	
333	
334	\section{Non-Stationarity Robustness Analysis}
335	\label{app:nonstationarity}
336	
337	Monte Carlo simulation (AR(1) DGP, $T{=}11$, 1{,}000 reps) shows PermG FPR inflates to ${\sim}10\%$ under strong non-stationarity ($\varphi{\geq}0.95$), while first-differencing maintains proper size ($4.2$--$6.6\%$) at the cost of reduced power (Table~\ref{tab:nonstationarity_sim}).
338	Our pipeline applies first-differencing before permutation testing, combining both advantages.
339	Under null conditions ($\alpha{=}0.0$), token entropy exhibits $\varphi{=}-0.51$ (far from the danger zone); first-differencing reduces distinct-1's high raw $\varphi$ ($0.81$--$0.97$, reflecting deterministic trend) to $-0.14$--$0.44$.
340	Our empirical FPR of 4/54 (7.4\%) confirms adequate size control.
341	
342	\begin{table}[h]
343	\centering
344	\small
345	\caption{Size and power under AR(1) DGP ($T{=}11$, 1{,}000 reps). First-differencing maintains nominal size; PermG FPR inflates at $\varphi{\geq}0.95$.}
346	\label{tab:nonstationarity_sim}
347	\resizebox{\columnwidth}{!}{%
348	\begin{tabular}{lcccccc}
349	\toprule
350	& \multicolumn{3}{c}{Size (\%, $\beta{=}0$)} & \multicolumn{3}{c}{Power (\%, $\beta{=}0.6$)} \\
351	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
352	$\varphi$ & Raw GC & First-Diff & PermG & Raw GC & First-Diff & PermG \\
353	\midrule
354	0.50 & 6.4 & 6.6 & 6.8 & 37.7 & 17.7 & 36.8 \\
355	0.95 & 10.0 & 5.9 & 9.5 & 44.3 & 28.7 & 41.5 \\
356	0.99 & 11.2 & 4.2 & 10.7 & 46.4 & 24.6 & 41.7 \\
357	\bottomrule
358	\end{tabular}}
359	\end{table}
360	
361	
362	\section{Shapley Value Analysis}
363	\label{app:shapley}
364	
365	Shapley values~\citep{shapley1953value} computed over all $2^5{=}32$ coalitions quantify each method's marginal contribution to FPR and FNR (Table~\ref{tab:shapley_6pair}).
366	DiffXCorr achieves the best combined Shapley ($-0.299$) but cannot separate forward from reverse; among directional methods, PermG ranks best ($-0.141$).
367	The 8-pair variant (including MAUVE) yields identical rankings.
368	
369	\begin{table}[h]
370	\centering
371	\small
372	\caption{Shapley value decomposition (6-pair, MAUVE excluded). Combined = FPR + FNR (more negative = better).}
373	\label{tab:shapley_6pair}
374	\begin{tabular}{lccc}
375	\toprule
376	Method & $\phi^{\text{FPR}}$ & $\phi^{\text{FNR}}$ & $\phi^{\text{comb}}$ \\
377	\midrule
378	Naive XCorr          & $+0.609$ & $-0.419$ & $+0.190$ \\
379	\textbf{Diff.\ XCorr}& $\mathbf{+0.007}$ & $\mathbf{-0.306}$ & $\mathbf{-0.299}$ \\
380	Threshold ($3\sigma$) & $+0.111$ & $-0.027$ & $+0.084$ \\
381	Perm.\ Granger       & $+0.039$ & $-0.180$ & $-0.141$ \\
382	Toda--Yamamoto       & $+0.150$ & $-0.069$ & $+0.082$ \\
383	\bottomrule
384	\end{tabular}
385	\end{table}
386	
387	
388	\section{MMCT Weight Robustness Ablation}
389	\label{app:weight_robustness}
390	
391	PermG ranks first among directional methods under all four weighting schemes tested (equal, cap-5, cap-10, FPR-inverse cap-100), confirming the ranking is not an artifact of the weighting scheme.
392	Cap-10 and cap-100 yield identical values (consensus threshold saturates), and equal weighting still gives PermG the best combined Shapley ($-0.152$) among directional methods.
393	
394	
395	\section{PermG FPR Independence Analysis}
396	\label{app:fpr_independence}
397	
398	Table~\ref{tab:null_fpr_methods} reports null-control FPR across nine seeds (54 pairs, 6-pair basis).
399	PermG achieves the lowest FPR (4/54, 7.4\%; CI $[2.1\%, 17.9\%]$); all four FP occur in te$\to$distinct pairs in seeds~45/50 (7/9 seeds yield 0~FP).
400	$K{\geq}3$ consensus produces 6/54 FP (11.1\%), of which PermG contributes to only 2.
401	At $T{=}15$, PermG FPR drops to 0/12 (0\%).
402	
403	\begin{table}[h]
404	\centering
405	\small
406	\caption{Null-control FPR by method ($\alpha{=}0.0$, 9~seeds, 6~pairs each, BH-FDR $q{=}0.05$).}
407	\label{tab:null_fpr_methods}
408	\resizebox{\columnwidth}{!}{%
409	\begin{tabular}{llrr}
410	\toprule
411	Method & Criterion & Rejections (/54) & FPR (\%) \\
412	\midrule
413	\textbf{Perm.\ Granger} & \textbf{BH-FDR} & \textbf{4} & \textbf{7.4} \\
414	Diff.\ XCorr$^\dagger$ & BH-FDR & 8 & 14.8 \\
415	Threshold & $3\sigma$ (det.) & 13 & 24.1 \\
416	Toda--Yamamoto & BH-FDR & 18 & 33.3 \\
417	Naive XCorr & uncorr. & 51 & 94.4 \\
418	\bottomrule
419	\multicolumn{4}{l}{\footnotesize $^\dagger$Bidirectional; cannot separate forward from reverse.} \\
420	\end{tabular}}
421	\end{table}
422	
423	\section{Sigmoid Transition Shape}
424	\label{app:sigmoid_shape}
425	
426	Sigmoid regression on the original 13-point $T{=}10$ grid yields $\alpha_c = 0.483 \pm 0.006$ but $k = 478 \pm 475$ ($\mathrm{SE}(k) \approx k$), indicating that the coarse grid cannot constrain the transition shape.
427	Dense $\alpha$ sampling (17~values at $T{=}10$) resolves this ambiguity: formal likelihood-ratio testing strongly favors a smooth sigmoid over a literal step function ($\Delta\mathrm{AIC}{=}-110$), with fitted steepness $k{=}15.7$ (95\% CI $[9.4, 28.2]$).
428	The transition is steep but finite-width, not a literal discontinuity.
429	This observed steepness exceeds what smooth signal models predict: VAR(1) simulations under H0 (linear, $k{=}6.1$) and H0$'$ (concave, $k{=}4.9$) produce onset sigmoids with $k{=}4.9$--$6.1$ (\S\ref{app:power_sim}), yielding steepness ratios $k_{\mathrm{obs}} / k_{\mathrm{H0}} \approx 2.6$--$3.2$ (CI lower bound ratio ${\approx}2$).
430	We do not fit a combined $T{=}10 + T{=}20$ sigmoid because $\alpha{=}0.45$ yields contradictory counts under the two sequence lengths (0/8 vs.\ 5/8), reflecting genuine power dependence on $T$ rather than a single dose-response curve.
431	
432	
433	\noindent\emph{See Figure~\ref{fig:detection_surface} in the main text for the detection surface visualization.}
434	
435	\section{Intervention Threshold Sensitivity}
436	\label{app:intervention_sensitivity}
437	
438	At $\alpha{=}1.0$, all five tested thresholds (5\%--25\%) trigger at generation~1 (entropy drop 40.7\%$\gg$threshold), producing identical outcomes (peak PPL 57.0, final PPL 21.3).
439	The safe operating band is $[10\%, 22\%]$: below 7.5\% triggers false alarms on $\alpha{=}0.0$ drift; above 22.4\% misses $\alpha{=}0.50$.
440	
441	
442	\section{Channel Effect Size Analysis}
443	\label{app:channel_effect_size}
444	
445	First-differencing retains comparable $|r|$ for both diversity (0.952) and perplexity (1.00) channels, ruling out selective power loss.
446	The Granger $F$-statistic asymmetry ($20$--$28{\times}$ higher for diversity) reflects temporal structure: diversity channels peak at canary-leading lags (81\% at lag${<}0$, median $-1$), while perplexity peaks at lag${=}0$ (contemporaneous co-movement).
447	Granger tests correctly assign low $F$ to contemporaneous relationships.
448	
449	
450	\section{Mutual Information and Partial Correlation}
451	\label{app:mi_analysis}
452	
453	Gaussian MI lower bound ($\hat{I}_G = -\frac{1}{2}\log_2(1{-}r^2)$) between token entropy and distinct-$n$ remains positive throughout the blind zone (0.010--0.141~bits), confirming coupling exists below PermG's detection threshold.
454	No discontinuity at $\alpha_c$: detection onset reflects power accumulation, not an information transition.
455	
456	\subsection{Partial Correlation Analysis}
457	\label{app:partial_corr}
458	
459	Partial correlations controlling for generation number (Table~\ref{tab:partial_corr}) show that contemporaneous associations drop after trend removal ($\bar{|r|}$: $0.590{\to}0.381$ at $\alpha{=}0.50$), while lagged correlations \emph{strengthen} ($0.759{\to}0.841$), with 35/36 detection-condition pairs retaining significance.
460	
461	\begin{table}[h]
462	\centering
463	\small
464	\caption{Partial correlation controlling for generation. Lagged partial $|r|$ increases after trend removal, confirming genuine temporal precedence.}
465	\label{tab:partial_corr}
466	\resizebox{\columnwidth}{!}{%
467	\begin{tabular}{@{}l cc cc cc cc@{}}
468	\toprule
469	& \multicolumn{4}{c}{Contemporaneous} & \multicolumn{4}{c}{Lagged (canary$_{t-1}$)} \\
470	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
471	& \multicolumn{2}{c}{Zero-order} & \multicolumn{2}{c}{Partial} & \multicolumn{2}{c}{Zero-order} & \multicolumn{2}{c}{Partial} \\
472	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7} \cmidrule(lr){8-9}
473	$\alpha$ & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. \\
474	\midrule
475	0.00 & 0.414 & 3/18 & 0.323 & 0/18 & 0.563 & 8/18 & 0.524 & 9/18 \\
476	0.50 & 0.590 & 9/18 & 0.381 & 2/18 & 0.759 & 12/18 & 0.841 & 17/18 \\
477	0.75 & 0.636 & 9/18 & 0.521 & 3/18 & 0.831 & 17/18 & 0.913 & 18/18 \\
478	\bottomrule
479	\end{tabular}}
480	\end{table}
481	
482	
483	\section{Moment Cascade Analysis}
484	\label{app:moment_cascade}
485	
486	Onset (5\% threshold) occurs at generation~1 for entropy in all 6 conditions and at generation~2 for distinct-$n$ in all 18 pairwise comparisons (Table~\ref{tab:moment_cascade}; Figure~\ref{fig:cascade_onset}).
487	
488	\begin{table}[h]
489	\centering
490	\small
491	\caption{Degradation onset generation (5\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}
492	\label{tab:moment_cascade}
493	\resizebox{\columnwidth}{!}{%
494	\begin{tabular}{llcccccc}
495	\toprule
496	Seed & $\alpha$ & Entropy & Dist-1 & Dist-2 & Dist-3 & ECE & PPL \\
497	\midrule
498	42 & 0.10 & 1 & 2 & 2 & 2 & 2 & --- \\
499	42 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
500	42 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
501	43 & 0.25 & 1 & 2 & 2 & 2 & 4 & --- \\
502	43 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
503	43 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
504	\bottomrule
505	\multicolumn{8}{l}{\footnotesize ---: onset not reached within $T{=}10$ generations.} \\
506	\end{tabular}}
507	\end{table}
508	
509	
510	ECE shows onset at generation~1 at $\alpha{\geq}0.50$; perplexity never reaches 5\% onset at low contamination ($\alpha{\leq}0.25$).
511	
512	
513	\section{Cascade Ordering Theory: Derivations}
514	\label{app:cascade_theory}
515	
516	This section provides the full derivations for Design Principle~\ref{thm:entropy_leads} and Design Principle~\ref{prop:div_lag} from \S\ref{sec:cascade}, plus supporting results.
517	
518	\begin{assumption}[Mode Amplification]\label{ass:mode_amp}
519	The training map $\mathcal{T}$ redistributes probability mass from low-probability to high-probability tokens: there exists a threshold $\bar{p}$ such that $\mathcal{T}(p)_i > p_i \Rightarrow p_i \geq \bar{p}$ and $\mathcal{T}(p)_j < p_j \Rightarrow p_j \leq \bar{p}$.
520	\end{assumption}
521	
522	This captures the standard finite-capacity approximation effect: MLE on finite samples from a peaked distribution amplifies modes and suppresses the tail~\citep{shumailov2024curse,dohmatob2024tale}.
523	
524	\begin{proposition}[Entropy is a first-order indicator]\label{prop:entropy_first}
525	Let $p \in \Delta^{V-1}$ and $\delta = \alpha(\mathcal{T}(p) - p)$ be a mode-amplifying perturbation with $\sum_i \delta_i = 0$. Then $\Delta H = H(p+\delta) - H(p) = -\sum_i \delta_i \log p_i + O(\|\delta\|^2) < 0$.
526	\end{proposition}
527	
528	\begin{proof}
529	Taylor-expanding $H$ around $p$:
530	$H(p+\delta) = H(p) - \sum_i \delta_i \log p_i - \sum_i \delta_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
531	Since $\sum_i \delta_i = 0$: $\Delta H = -\sum_i \delta_i \log p_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
532	Under mode amplification, tokens gaining mass ($\delta_i > 0$) have $p_i \geq \bar{p}$ (hence $\log p_i \geq \log \bar{p}$) and tokens losing mass ($\delta_j < 0$) have $p_j \leq \bar{p}$ (hence $\log p_j \leq \log \bar{p}$).
533	Writing $m = \sum_{i:\delta_i > 0} \delta_i$: $-\sum_i \delta_i \log p_i = -m[\overline{\log p}^{+} - \overline{\log p}^{-}] < 0$, where $\overline{\log p}^{\pm}$ are the $|\delta|$-weighted means over gaining/losing tokens.
534	The second-order Fisher information term $-\frac{1}{2}\sum_i \delta_i^2/p_i$ is always negative, reinforcing the decrease.
535	\end{proof}
536	
537	\begin{proposition}[Diversity is a threshold indicator]\label{prop:div_threshold}
538	Define the $\epsilon$-effective support $S_\epsilon(p) = |\{i \in [V]: p_i > \epsilon\}|$, where $\epsilon \approx c/N$ is the generation threshold for sample size $N$.
539	Under the same perturbation $\delta$: $\Delta S_\epsilon = -|\{i: p_i > \epsilon \text{ and } p_i + \delta_i \leq \epsilon\}|$.
540	This equals zero whenever $\|\delta\|_\infty < \gamma(p,\epsilon) := \min_{i: p_i > \epsilon}(p_i - \epsilon)$.
541	\end{proposition}
542	
543	\begin{proof}
544	Token $i$ exits the effective support iff $p_i > \epsilon$ and $p_i + \delta_i \leq \epsilon$, requiring $|\delta_i| \geq p_i - \epsilon$.
545	If $\|\delta\|_\infty < \gamma$, no token satisfies this condition.
546	\end{proof}
547	
548	\paragraph{Derivation of Design Principle~\ref{thm:entropy_leads}.}
549	\emph{Part (a):} Take any mode-amplifying $\delta$ with $\|\delta\|_\infty < \gamma(p,\epsilon)$.
550	By Proposition~\ref{prop:div_threshold}, $\Delta S_\epsilon = 0$.
551	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$.
552	Such $\delta$ exists for all $\alpha < \gamma / \max_i |\mathcal{T}(p)_i - p_i|$.
553	\emph{Part (b):} If $\Delta S_\epsilon < 0$, some token $k$ has $p_k > \epsilon$ but $p_k + \delta_k \leq \epsilon$, so $\delta_k < 0$.
554	Under mode amplification, this implies $p_k \leq \bar{p}$; the total mass transferred to high-probability tokens ensures $\overline{\log p}^+ > \overline{\log p}^-$.
555	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$. $\square$
556	
557	\paragraph{Derivation of Design Principle~\ref{prop:div_lag}.}
558	By the margin condition, at every generation $s \leq t_H$ the perturbation norm $\alpha\|\mathcal{T}(p_s) - p_s\|_\infty$ is less than $\gamma(p_s, \epsilon)$.
559	By Proposition~\ref{prop:div_threshold}, no token exits the effective support at any $s \leq t_H$, so $\Delta S_\epsilon = 0$ for all $s \leq t_H$.
560	Since time is discrete, $t_D \geq t_H + 1$. $\square$
561	
562	\paragraph{ECE co-movement (qualitative argument).}
563	Under conditional mode amplification (peakier $q_\theta(\cdot|x)$ at each generation), per-token conditional entropy $h(x) = H(q_\theta(\cdot|x))$ decreases while confidence $c(x) = \max_y q_\theta(y|x) \geq \exp(-h(x))$ increases.
564	Averaging: $\bar{H}_t$ decreases, $C_t$ increases.
565	With accuracy approximately stationary in early collapse ($A_t \approx A_0$), $\Delta\mathrm{ECE} \approx \Delta C_t > 0$ whenever $\Delta\bar{H}_t < 0$.
566	This argument establishes the direction of co-movement; the quantitative relationship depends on distribution geometry.
567	$\bar{H}_t$ denotes mean conditional entropy $\mathbb{E}_{x \sim p_{\text{eval}}}[h(x)]$, which differs from the marginal entropy $H_t = -\sum_i p_t(i)\log p_t(i)$ used in Design Principle~\ref{thm:entropy_leads}; under mode amplification, both decrease monotonically, so the cascade ordering is consistent across both formulations.
568	
569	\paragraph{Empirical support.}
570	Cascade ordering $t_H \leq t_D$ holds in 14/15 experiments at $\alpha \geq 0.30$ (GPT-2-medium s43: bidirectional).
571	Table~\ref{tab:cascade_onset} reports onset generations for representative conditions.
572	
573	\begin{table}[h]
574	\centering
575	\small
576	\caption{Cascade onset generations (5\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\mathrm{ECE}} \leq t_D \leq t_M$.}
577	\label{tab:cascade_onset}
578	\begin{tabular}{llcccc}
579	\toprule
580	Seed & $\alpha$ & $t_H$ & $t_{\mathrm{ECE}}$ & $t_D$ & $t_M$ \\
581	\midrule
582	42 & 0.50 & 1 & 1 & 2 & 3 \\
583	43 & 0.50 & 1 & 1 & 2 & 2 \\
584	42 & 0.75 & 1 & 1 & 2 & 3 \\
585	43 & 0.75 & 1 & 1 & 2 & 2 \\
586	\bottomrule
587	\end{tabular}
588	\end{table}
589	
590	
591	\phantomsection\label{app:alpha_c_proof}
592	\paragraph{Justification of the empirical boundary model.}
593	At the detection threshold, $\mathrm{Power}(\alpha_c, T) = \pi^*$.
594	Since $\alpha_c$ lies below the non-monotonic dip region ($\alpha_c < 0.55$), the signal model applies directly.
595	From the power function $\mathrm{Power} = \Phi(S(\alpha) \cdot \sqrt{T} / \sigma)$, setting $S(\alpha_c) \cdot \sqrt{T} / \sigma = z^*$ and substituting the signal model $S(\alpha) = c\,\alpha^\beta$ yields $c\,\alpha_c^\beta = z^* \sigma / \sqrt{T}$.
596	Solving: $\alpha_c(T) = (z^* \sigma / c)^{1/\beta} \cdot T^{-1/(2\beta)}$, giving the stated form with exponent $\gamma = 1/(2\beta)$.
597	
598	\paragraph{Calibration and consistency.}
599	Fitting $P(\mathrm{det}|\alpha,T) = \Phi(A \cdot \alpha^\beta \cdot \sqrt{T} - z_0)$ to $T \in \{10, 20\}$ yields $\beta{=}0.24$, $\alpha_\infty{=}0$.
600	Held-out test ($T \in \{5, 15\}$): MAE${=}0.106$, 95\% CI coverage 6/6.
601	Leave-one-$T$-out CV (15 cells, sync-dip excluded): MAE${=}0.037$, coverage 15/15.
602	Profile likelihood yields $\hat{\beta}{=}0.66$ (CI $[0.24, 0.78]$); the wide interval reflects a flat surface.
603	
604	\section{Power Simulation: Shape Comparison}
605	\label{app:power_sim}
606	
607	Simulated PermG detection under linear (H0), concave (H0$'$), and step (H1) signal models (1{,}000 reps, $n_\text{perm}{=}1{,}000$, BH-FDR $q{=}0.05$).
608	Smooth models produce onset steepness $k{=}4.9$--$6.1$; the observed $k{=}15.7$ is ${\approx}3{\times}$ higher.
609	The scaling exponent alone cannot distinguish smooth from step boundaries (H0$'$ $\gamma{=}1.87$ vs.\ observed $\gamma{=}2.08$).
610	The 6/8 detection ceiling reflects MAUVE floor saturation, not signal limitations.
611	
612	\section{T=20 Extension Results}
613	\label{app:t20_comparison}
614	
615	At $\alpha{\geq}0.50$, PermG counts are consistent across $T{=}10$ and $T{=}20$ (6/8 at both), confirming signal-structure determination.
616	At $\alpha{=}0.45$, the shift from 0/8 ($T{=}10$) to 5/8 ($T{=}20$) supports power-limited (Model~B) over structurally-undetectable (Model~A), lowering $\alpha_c$ below 0.45.
617	The $\alpha{=}0.60$ dip persists at $T{=}20$ but dissolves at $T{=}25$ (5/8), confirming $\sqrt{T}$ power scaling eventually overcomes it.
618	Directional selectivity is consistent: forward 6/8, reverse 0/8 at $\alpha \in \{0.50, 0.75, 1.0\}$ across all tested $T$.
619	
620	
621	\phantomsection\label{app:task_degradation}
622	\paragraph{Task degradation.}
623	End-of-training perplexity (gen~10, Pythia-410M, s42) improves at $\alpha{=}0.05$ (20.8 vs.\ 26.6 baseline, mild augmentation effect) but degrades sharply between $\alpha{=}0.50$ (31.3) and $0.52$ (41.1), aligning with PermG detection onset.
624	
625	\subsection{Cross-Architecture Detection Table}
626	\label{app:cross_arch_table}
627	
628	\begin{table}[h]
629	\centering
630	\small
631	\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$, 15 model-seed combinations across five families---Pythia, GPT-2, OPT, Qwen, SmolLM3---and two domains; Padding-410M is a Pythia variant). PermG fwd $=$ count of FDR-significant forward pairs out of 8.}
632	\label{tab:generalization}
633	\resizebox{\columnwidth}{!}{%
634	\begin{tabular}{lrcl}
635	\toprule
636	Model & Params & Domain & PermG fwd \\
637	\midrule
638	Pythia-410M    & 410M & Wiki & \textbf{6/8} \\
639	Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
640	Pythia-6.9B    & 6.9B & Wiki & \textbf{7/8}$^*$ \\
641	\addlinespace
642	GPT-2-medium   & 345M & Wiki & \textbf{6/8}$^\S$ \\
643	\addlinespace
644	OPT-1.3B       & 1.3B & Wiki & \textbf{6/8} \\
645	\addlinespace
646	Qwen3.5-0.8B   & 0.8B & Wiki & \textbf{8/8} \\
647	SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
648	Padding-410M   & 410M & Wiki & \textbf{6/8} \\
649	\addlinespace
650	Pythia-1B      & 1.0B & C4   & \textbf{8/8} \\
651	Pythia-1.4B    & 1.4B & C4   & \textbf{8/8} \\
652	\bottomrule
653	\multicolumn{4}{l}{\footnotesize $^\dagger$Seed-dep.\ (s42: 2/8, s43: 6/8); 8-pair incl.\ MAUVE} \\
654	\multicolumn{4}{l}{\footnotesize \phantom{$^\dagger$}(floor ${\sim}0.033$ at 1.4B; 6-pair in Table~\ref{tab:14b_phase}). $^*$bf16. $^\ddagger$ECE-only (ent.\ 0/4).} \\
655	\multicolumn{4}{l}{\footnotesize $^\S$s42 fp32: 6/8 fwd, 0 rev; s43: 6/8 both; bf16: 0/8.} \\
656	\multicolumn{4}{l}{\footnotesize 2 seeds each for Pythia-410M/1.4B, GPT-2, OPT, Pythia-1B C4.} \\
657	\end{tabular}%
658	}
659	\end{table}
660	
661	\subsection{Cross-Architecture FPR Sensitivity}
662	\label{app:cross_arch_fpr}
663	
664	GPT-2-medium null-condition PermG FPR is 50\% (6/12 pooled, 2~seeds), dramatically higher than Pythia-410M (7.4\%), driven by ${\sim}4{\times}$ stronger null drift (entropy $-20.5\%$ vs.\ $-4.9\%$; distinct-3 $-35.8\%$ vs.\ $-4.9\%$).
665	$K{\geq}3$ consensus maintains 0\% FPR (0/12) on GPT-2-medium, providing some protection, but standalone PermG requires architecture-specific null calibration.
666	
667	\section*{Use of AI Assistants}
668	\label{app:ai-assistants}
669	
670	We used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:
671	\begin{itemize}
672	    \item \textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.
673	    \item \textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.
674	    \item \textbf{Literature:} summarizing related papers to inform related-work section.
675	\end{itemize}
676	
677	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3043460f-68a2-4769-9d94-b84015bc657c",
  "isSidechain": true,
  "promptId": "28ed9fd7-28b9-4f8b-a3f7-ce466223640d",
  "agentId": "a8da0bb5ae83c9d55",
  "type": "user",
  "uuid": "1e4ef4f9-2cca-4817-a3a7-bc7f911b9302",
  "sourceToolAssistantUUID": "3043460f-68a2-4769-9d94-b84015bc657c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "2e2dd7aa-a3cc-4018-897b-841737c0e4e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "cached-giggling-dusk"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-24T21:08:14.254Z_

Perfect! I found the MMCT Algorithm pseudocode. Here are the complete details:

## MMCT Algorithm Pseudocode

**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex`

**Section Location:** Lines 170-192

**Section Label:** `\label{app:mmct}` (line 171)

**Section Header:** Section 6.12 "MMCT Algorithm" (line 170)

### Complete Content (lines 170-192):

```latex
\section{MMCT Algorithm}
\label{app:mmct}

Algorithm~\ref{alg:mmct} describes the Multi-Method Consensus Test (MMCT) introduced in \S\ref{sec:mmct}.

\begin{algorithm}[h]
\caption{Multi-Method Consensus Test (MMCT)}
\label{alg:mmct}
\begin{algorithmic}[1]
\Require Time series pair $(X, Y)$; methods $\{m_1, \ldots, m_K\}$ ($K{=}5$); null-control data $\mathcal{N}$ (from $\alpha{=}0.0$); tolerance $\epsilon{=}0.01$
\Ensure $p$-value, consensus level $\hat{K}$
\For{each method $m_k$}
    \State Compute empirical FPR: $\widehat{\mathrm{FPR}}_k \gets$ fraction of null-control pairs where $m_k$ rejects $H_0$
    \State Compute weight: $w_k \gets 1 / \max(\widehat{\mathrm{FPR}}_k,\; \epsilon)$
    \State Apply $m_k$ to $(X, Y)$: $d_k \gets \mathbf{1}[m_k \text{ rejects } H_0]$
\EndFor
\State Weighted consensus: $W(X {\to} Y) \gets \sum_{k} w_k \, d_k \;/\; \sum_{k} w_k$
\State Build empirical null distribution of $W$ from all null-control pairs in $\mathcal{N}$
\State Compute $p$-value from empirical null: $p \gets \Pr_{\mathcal{N}}(W \geq W_{\mathrm{obs}})$
\State Consensus level: $\hat{K} \gets \sum_{k} d_k$
\State \Return $p$, $\hat{K}$
\end{algorithmic}
\end{algorithm}
```

### Design Rationale Section (lines 194-197):

Following the algorithm is an explanatory paragraph that describes the design rationale:

```latex
\paragraph{Design rationale.}
FPR-inverse weighting penalizes methods with high false positive rates on null-control data: naive cross-correlation (FPR${=}94.4\%$) receives weight $w{=}1.06$, while PermG (FPR${=}7.4\%$, the lowest among all five methods) receives $w{=}13.5$.
The empirical null distribution avoids parametric assumptions that are unreliable for short ($T{=}5$--$20$), non-stationary series typical of iterative training.
MMCT is a consensus testing protocol, not a novel statistical method; its value lies in systematic method comparison and the identification of method-dependent conclusions.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e4ef4f9-2cca-4817-a3a7-bc7f911b9302",
  "isSidechain": true,
  "agentId": "a8da0bb5ae83c9d55",
  "requestId": "req_011CbN5RbGDrT9gabPrrC6DW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35fe180f-77ae-4e0e-abde-c42e5b0f8b7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "2e2dd7aa-a3cc-4018-897b-841737c0e4e7",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "cached-giggling-dusk",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SZeCRsmpE494WswvfmXpVK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 18236,
      "cache_read_input_tokens": 33365,
      "output_tokens": 870,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18236
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 870,
          "cache_read_input_tokens": 33365,
          "cache_creation_input_tokens": 18236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18236,
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
